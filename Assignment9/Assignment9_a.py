import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download NLTK data if not already installed
nltk.download('punkt')
nltk.download('stopwords')

def generate_summary(text):
    """Summarizes the provided text."""
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())

    # Filter out stop words and non-alphabetic tokens
    filtered_tokens = [token for token in tokens if token.isalpha() and token not in stop_words]

    # Compute frequency distribution of the filtered tokens
    word_freq = nltk.FreqDist(filtered_tokens)

    # Split the content into individual sentences
    sentences = sent_tokenize(text)

    # Check if sentences are available for processing
    if not sentences:
        return "No sentences to summarize."

    # Initialize a dictionary to score sentences
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                # Calculate score for each sentence
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_freq[word]

    # Sort the sentences based on their scores in descending order
    if not sentence_scores:
        return "No sentences scored."

    # Select top 3 sentences for the summary
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:3]

    # Concatenate the selected sentences into a summary
    summary_text = ' '.join(top_sentences)

    # Replace specific punctuation for smoother reading
    summary_text = summary_text.replace(";", ".").replace(".", ". ")

    return summary_text.strip()

# Read the reviews from the input file
file_path = 'input.txt'  # Provide the correct path for your file
with open(file_path, 'r') as file:
    reviews = file.readlines()

# Categorize reviews based on basic sentiment analysis
positive_reviews = []
neutral_reviews = []
negative_reviews = []

for review in reviews:
    cleaned_review = review.strip().lower()
    if any(phrase in cleaned_review for phrase in ["fantastic", "love", "great"]):
        positive_reviews.append(cleaned_review)
    elif any(phrase in cleaned_review for phrase in ["decent", "average", "okay"]):
        neutral_reviews.append(cleaned_review)
    else:
        negative_reviews.append(cleaned_review)

# Generate summaries for each category of reviews
combined_positive_reviews = "\n".join(positive_reviews)
combined_neutral_reviews = "\n".join(neutral_reviews)
combined_negative_reviews = "\n".join(negative_reviews)

positive_summary = generate_summary(combined_positive_reviews)
neutral_summary = generate_summary(combined_neutral_reviews)
negative_summary = generate_summary(combined_negative_reviews)

# Display the summaries
print("Summary of Positive Reviews:", positive_summary)
print("Summary of Neutral Reviews:", neutral_summary)
print("Summary of Negative Reviews:", negative_summary)
