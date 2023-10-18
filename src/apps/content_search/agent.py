import chromadb
import openai
import os
from config import get_info_from_config


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMA_DB_PATH = os.path.join(BASE_DIR, "vectorstores/chroma")

if not os.path.exists(CHROMA_DB_PATH):
    os.makedirs(CHROMA_DB_PATH)
    
chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)

# collection = chroma_client.create_collection(name="test_collection")


print(get_info_from_config("condition_text", os.path.join(BASE_DIR, "config.yaml")))
