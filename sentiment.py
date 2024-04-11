from transformers import RobertaTokenizer, RobertaForSequenceClassification
import torch

def sentiment_analysis(tokenized_comments):
    
    model = RobertaForSequenceClassification.from_pretrained('roberta-base')
    tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
    ML_data = tokenizer(tokenized_comments, padding=True, truncation=True, return_tensors='pt')

    outputs = model(**ML_data)

    logits = outputs.logits
    predicted_labels = torch.argmax(logits, dim = 1)

    sentiment_counts = {'negative':0, 'neutral':0, 'positive':0}
    for label in predicted_labels:
        if label.item() == 0:
            sentiment = 'negative'
            sentiment_counts[sentiment] += 1
        elif label.item() == 1:
            sentiment = 'neutral'
            sentiment_counts[sentiment] += 1
        else:
            sentiment = 'positive'
            sentiment_counts[sentiment] += 1
    return sentiment_counts











    