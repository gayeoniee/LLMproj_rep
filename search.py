import meilisearch
client = meilisearch.Client('http://127.0.0.1:7700', '14_MRs3BW8jO62eowQOL9Io9drAMPVtX0wA3NlpRghY')

def stock_search(query):    
    return client.index('nasdaq').search(query)