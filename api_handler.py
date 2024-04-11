import requests

def get_comment_query(query):
    endpoint = f"https://api.pullpush.io/reddit/search/comment/?q={query}"
    comment_data = requests.get(endpoint)
    comment_data = comment_data.json()["data"]  
    return comment_data

def get_submission_query(query):
    endpoint = f"https://api.pullpush.io/reddit/search/submission/?q={query}"
    submission_data = requests.get(endpoint)
    submission_data = submission_data.json()["data"]  
    return submission_data

#hugging face transformers
    #roberta
    #distilbert
    #building a frontend
#AAAAAAAAAAAAAAAAAAAAAPiUtAEAAAAAbGuhP%2Ftucc1z6ZdAzvRQCe6zdeE%3Dib4rHbAneRHjXsSC42h8dHVnacrIVc1Qo7rOUS1LI3e0wmbTaM
#Bearer token
#1211550517727395840-ZuAAUoi4F49sUNHpMf9yasjOvBwTk5
#access token
#rU9AfAEzLNG2ORTfZkSi7sqMhLTuHU0gAIpSB7GEwBVn0
#access token secret
#XYhCPfFvmVqMg4N5MWFr2zzOb
#API Key
#xCPnRu2AuKaI24g3ca7w0Ir7hWMB24LDOMhdV7gR4poDMW6Gdl
#API Key secret 


