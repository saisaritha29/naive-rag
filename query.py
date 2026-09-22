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

question = "What is the difference between Artificial Intelligence and Machine Learning?"

# Search Weaviate
results = collection.query.near_text(
    query=question,
    limit=3
)

print("\nQuestion:")
print(question)

print("\nRetrieved Chunks:")

for result in results.objects:
    print("\n-------------------------")
    print(result.properties["content"])

client.close()