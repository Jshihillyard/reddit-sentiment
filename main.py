from api_handler import get_submission_query, get_comment_query
from data_process import tokenizationPosts, tokenizationComments
from sentiment import sentiment_analysis
from transformers import RobertaTokenizer
import torch


data = []

userInput = False
while userInput == False:
    option = input('Would you like to browse submissions or comments? ')
    if(option == 'submissions'):
        redditTopic = input("Enter a subject/person for sentiment analysis ")
        data = get_submission_query(redditTopic)
        tokenized_text = tokenizationPosts(data)
        userInput = True
    elif(option == 'comments'):
        redditTopic = input("Enter a subject/person for sentiment analysis ")
        data = get_comment_query(redditTopic)
        tokenized_text = tokenizationComments(data)
        userInput = True
    else:
        print("You didn't enter submissions or comments. Please try again. ")

predicted_categories = sentiment_analysis(tokenized_text)
print(f"Here is the sentiment breakdown towards{redditTopic}")
print(predicted_categories)








