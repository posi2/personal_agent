from qdrant_client import QdrantClient
from prajna.settings import settings

qdrant_client = QdrantClient(
    url="https://57009a61-6c18-4263-87d9-d644500aa652.us-east4-0.gcp.cloud.qdrant.io:6333", 
    api_key=settings.QDRANT_API_KEY,
)

print(qdrant_client.get_collections())
