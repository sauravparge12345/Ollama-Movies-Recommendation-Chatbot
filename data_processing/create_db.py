from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from qdrant_client.models import PointStruct


client = QdrantClient(url="http://localhost:6333")

client.delete_collection("movies")

client.create_collection(
    collection_name="movies",
    vectors_config=VectorParams(size=1024, distance=Distance.DOT),
)
