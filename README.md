# Text Summarizer (Python)

A lightweight, **Extractive Text Summarizer** built with Python and NLTK. This tool analyzes the frequency of words within a text to identify and extract the most meaningful sentences, providing a concise summary without requiring heavy Deep Learning models.

## 🚀 Features

  * **Preprocessing:** Automatically removes stop words (common words like "the", "is", "and") and punctuation.
  * **Word Scoring:** Uses a normalized frequency distribution algorithm to weight word importance.
  * **Sentence Ranking:** Scores sentences based on the cumulative weight of the words they contain.
  * **Customizable:** Easily adjust the summary length (number of sentences).

## 🧠 How it Works

The summarizer follows a four-step statistical pipeline:

1.  **Tokenization:** Breaks the text into individual words and sentences.
2.  **Frequency Analysis:** Creates a dictionary of word frequencies, excluding "stop words."
3.  **Normalization:** Divides each word count by the maximum frequency to keep scores between $0$ and $1$.
4.  **Selection:** Sums the scores of words within each sentence and uses a heap queue (`heapq`) to extract the top $N$ sentences.
