# SentimentSorting
Sentiment Analysis and sorting
1.Import all the required libraries

2.In order to import multiple csv and text file into a data frame we created 2 empty lists namely purpose and name. We are doing this so we can append the name and purpose from the different csv and txt files into a single data frame. We call this the result_df.

3.Sentiment Sorting
After using the library vader we here get a compound score which is normalized between -1 and +1. Based on that compound score we get to know companies with positive and negative score respectively. Solely based on the sentiment compound score we find the companies are best and worst respectively.

4.Scraped the second column of dataframe that is purpose into a list called description.

In order to tokenize it through line 67-74 we create a function which strips the string into individual words. Not based on how frequently they occur we assign it a frequency and eventually check to see the count of words and their frequencies respectively.
