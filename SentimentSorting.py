import csv
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from collections import Counter

name = []
purpose = []
with open('Vaikunth.txt') as Vaikunth:
    a = Vaikunth.read()
    b = a.split("\n")
    for i in b:
        if 'Name: ' in i:
            x = i[6:]
            name.append(x)
        if 'Purpose: ' in i:
            y = i[9:]
            purpose.append(y)
with open('WebScrOutput.txt') as Kshitij:
    a = Kshitij.read()
    b = a.split("\n")
    for i in b:
        if 'Name: ' in i:
            x = i[6:]
            name.append(x)
        if 'Purpose: ' in i:
            y = i[9:]
            purpose.append(y)
with open('Anirudh.csv') as Anirudh:
    anirudh_data = csv.reader(Anirudh)
    for row in anirudh_data:
        if row[1] != "Name":
            x = row[1]
            y = row[2]
            name.append(x)
            purpose.append(y)
with open('Simran.csv') as Simran:
    simran_data = csv.reader(Simran)
    for row in simran_data:
        if row[1] != "Name":
            x = row[1]
            y = row[2]
            name.append(x)
            purpose.append(y)


result_df = pd.DataFrame({"Name": name, "Purpose": purpose}, index=range(1, 201))
print(result_df)

analyzer = SentimentIntensityAnalyzer()
sent_score = []
for i in range(200):
    x = analyzer.polarity_scores(purpose[i]).get('compound')
    sent_score.append(x)# adding compound score from sentiment analysis to 'result' dataframe
result_df['Compound_Score'] = sent_score# finding row with maximum compound score
print("The company with the highest compound score after conducting Sentiment Analysis is: \n")
print(result_df[result_df.Compound_Score == result_df.Compound_Score.max()])
print("\n")# finding row with minimum compound score
print("The companies with the lowest compound score after conducting Sentiment Analysis is: \n")
print(result_df[result_df.Compound_Score == result_df.Compound_Score.min()])
print("\n")

#
description = []
for i in result_df['Purpose']:
    description.append(i)

tokenized = {}
def frequent_token(text):
    words = text
    words = words.split()
    for t in words:
        if t not in tokenized:
            tokenized[t] = 0
        tokenized[t] += 1
    return tokenized
for i in description:
    frequent_token(i)
    frequentWords = Counter(tokenized)
top_ten = frequentWords.most_common(10)
print("The 10 most common words are:")
for i in top_ten:
    print(i[0], "-", i[1], " ")

