import os
import weaviate

from dotenv import load_dotenv
from weaviate.classes.init import Auth

load_dotenv()

WEAVIATE_URL = os.getenv("WEAVIATE_URL")
WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY")

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WEAVIATE_URL,
    auth_credentials=Auth.api_key(WEAVIATE_API_KEY)
)

print("Connected to Weaviate!")
print("Ready:", client.is_ready())

client.close()