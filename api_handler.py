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



