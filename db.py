# db.py
import os
import pandas as pd
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from config import MEDICINE_CSV, DB_LOCATION

def setup_vector_db():
    embeddings = OllamaEmbeddings(model="mxbai-embed-large")
    add_documents = not os.path.exists(DB_LOCATION)

    if add_documents:
        df = pd.read_csv(MEDICINE_CSV)
        documents = []
        ids = []
        for i, row in df.iterrows():
            content = f"Name: {row['Name']}\nGeneric: {row['Generic Name']}\nUses: {row['Uses']}\nDosage: {row['Typical Dosage']}\nSide Effects: {row['Side Effects']}"
            doc = Document(
                page_content=content,
                metadata={"Name": row["Name"], "Generic": row["Generic Name"]},
                id=str(i)
            )
            documents.append(doc)
            ids.append(str(i))
        vector_store = Chroma(
            collection_name="medicine_information",
            persist_directory=DB_LOCATION,
            embedding_function=embeddings
        )
        vector_store.add_documents(documents=documents, ids=ids)
        vector_store.persist()
    else:
        vector_store = Chroma(
            collection_name="medicine_information",
            persist_directory=DB_LOCATION,
            embedding_function=embeddings
        )

    return vector_store.as_retriever(search_kargs={"k": 5})
