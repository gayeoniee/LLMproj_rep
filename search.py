import meilisearch
client = meilisearch.Client('http://127.0.0.1:7700', MEILISEARCH_MASTER_KEY)

def stock_search(query):    
    return client.index('nasdaq').search(query)
