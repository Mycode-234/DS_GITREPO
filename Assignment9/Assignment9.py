import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer

# Ensure necessary NLTK resources are downloaded
def download_nltk_resources():
    """Download necessary NLTK resources if not already available."""
    resources = ['punkt', 'stopwords', 'vader_lexicon']
    for resource in resources:
        try:
            if resource == 'punkt':
                nltk.data.find('tokenizers/punkt')
            elif resource == 'stopwords':
                nltk.data.find('corpora/stopwords')
            else:
                nltk.data.find('sentiment/vader_lexicon')
        except LookupError:
            nltk.download(resource)

download_nltk_resources()

def create_summary(input_text):
    """Create a summary of the input text by scoring sentences based on word frequencies."""
    stop_words_set = set(stopwords.words('english'))
    tokens = word_tokenize(input_text.lower())

    # Remove stop words
    filtered_words = [word for word in tokens if word.isalpha() and word not in stop_words_set]

    # Calculate word frequencies
    frequency_distribution = nltk.FreqDist(filtered_words)

    # Tokenize input text into sentences
    sentence_list = sent_tokenize(input_text)

    if not sentence_list:
        return "No sentences available for summarization."

    # Score sentences based on word frequencies
    sentence_scores_dict = {}
    for sentence in sentence_list:
        for word in word_tokenize(sentence.lower()):
            if word in frequency_distribution:
                if sentence not in sentence_scores_dict:
                    sentence_scores_dict[sentence] = frequency_distribution[word]
                else:
                    sentence_scores_dict[sentence] += frequency_distribution[word]

    if not sentence_scores_dict:
        return "No sentences could be scored for the summary."

    # Sort and select top sentences
    top_sentences = sorted(sentence_scores_dict, key=sentence_scores_dict.get, reverse=True)[:3]  # Select top 3 sentences
    summary_result = ' '.join(top_sentences).replace(";", ".").replace(".", ". ").strip()

    return summary_result

# Read reviews from a specified text file
input_file = 'input.txt'  # Update with your actual file path
with open(input_file, 'r') as file:
    review_lines = file.readlines()

# Initialize sentiment analysis tool
sentiment_analyzer = SentimentIntensityAnalyzer()

# Classify reviews based on sentiment
positive_list = []
neutral_list = []
negative_list = []

for line in review_lines:
    cleaned_review = line.strip()
    sentiment_score = sentiment_analyzer.polarity_scores(cleaned_review)
    compound_score = sentiment_score['compound']

    if compound_score >= 0.5:
        positive_list.append(cleaned_review)
    elif compound_score <= -0.2:
        negative_list.append(cleaned_review)
    else:
        neutral_list.append(cleaned_review)

# Summarize reviews in each sentiment category
positive_reviews_text = "\n".join(positive_list)
neutral_reviews_text = "\n".join(neutral_list)
negative_reviews_text = "\n".join(negative_list)

positive_summary_result = create_summary(positive_reviews_text)
neutral_summary_result = create_summary(neutral_reviews_text)
negative_summary_result = create_summary(negative_reviews_text)

# Output the summaries
print("Positive Review Summary:", positive_summary_result)
print("Neutral Review Summary:", neutral_summary_result)
print("Negative Review Summary:", negative_summary_result)

# Save summaries to corresponding files
with open('positive_review_summary.txt', 'w') as pos_file:
    pos_file.write(positive_summary_result)

with open('neutral_review_summary.txt', 'w') as neu_file:
    neu_file.write(neutral_summary_result)

with open('negative_review_summary.txt', 'w') as neg_file:
    neg_file.write(negative_summary_result)

print("Summaries have been saved to positive_review_summary.txt, neutral_review_summary.txt, and negative_review_summary.txt.")

# Plotting the count of reviews in each sentiment category
categories = ['Positive', 'Neutral', 'Negative']
counts_list = [len(positive_list), len(neutral_list), len(negative_list)]

plt.bar(categories, counts_list, color=['green', 'gray', 'red'])
plt.title('Review Count by Sentiment Category')
plt.xlabel('Sentiment Category')
plt.ylabel('Review Count')
plt.ylim(0, max(counts_list) + 5)  # Adjust y-axis limit
plt.show()
