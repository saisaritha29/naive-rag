import os
import weaviate

from dotenv import load_dotenv
from weaviate.classes.init import Auth

load_dotenv()

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WEAVIATE_URL"),
    auth_credentials=Auth.api_key(os.getenv("WEAVIATE_API_KEY"))
)

collection = client.collections.use("DocumentChunk")

# Read the document
with open("documents/notes.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Split text into small chunks
chunk_size = 500

chunks = []

for i in range(0, len(text), chunk_size):
    chunk = text[i:i + chunk_size]

    chunks.append({
        "content": chunk,
        "source": "notes.txt"
    })

# Insert chunks into Weaviate
collection.data.insert_many(chunks)

print(f"Successfully inserted {len(chunks)} chunks!")

client.close()