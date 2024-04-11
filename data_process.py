import json
from transformers import RobertaTokenizer

def tokenizationComments(data):
    tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
    reddit_comments = [comment['body'] for comment in data]

    tokenized_comments = [tokenizer.tokenize(comment) for comment in reddit_comments]
    tokenized_comments = [' '.join(tokens) for tokens in tokenized_comments]

    return tokenized_comments

def tokenizationPosts(data):
    tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
    reddit_post = [post['selftext'] for post in data]

    tokenized_posts = [tokenizer.tokenize(post) for post in reddit_post]
    tokenized_posts = [' '.join(tokens) for tokens in tokenized_posts]

    return tokenized_posts