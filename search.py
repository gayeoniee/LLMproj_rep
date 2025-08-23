import meilisearch
from dotenv import load_dotenv
import os
load_dotenv()
meilisearch_master_key = os.getenv("MEILISEARCH_MASTER_KEY")
if meilisearch_master_key:
    os.environ["MEILISEARCH_MASTER_KEY"] = meilisearch_master_key
print("MEILISEARCH Key configured:", "MEILISEARCH_MASTER_KEY" in os.environ)


client = meilisearch.Client('http://127.0.0.1:7700', meilisearch_master_key)

def stock_search(query):    
    return client.index('nasdaq').search(query)
