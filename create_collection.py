import os
import weaviate

from dotenv import load_dotenv
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure, Property, DataType

load_dotenv()

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WEAVIATE_URL"),
    auth_credentials=Auth.api_key(os.getenv("WEAVIATE_API_KEY"))
)

# Create collection
if not client.collections.exists("DocumentChunk"):
    client.collections.create(
        name="DocumentChunk",

        properties=[
            Property(
                name="content",
                data_type=DataType.TEXT
            ),
            Property(
                name="source",
                data_type=DataType.TEXT
            )
        ],

        vector_config=Configure.Vectors.text2vec_weaviate()
    )

    print("DocumentChunk collection created!")
else:
    print("DocumentChunk collection already exists!")

client.close()