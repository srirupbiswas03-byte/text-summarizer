import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq
import sys
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

def debugged_summarizer(text, num_sentences=3):
    
    if not text or len(text.strip()) < 20:
        return "Error: Text is too short to summarize."

    try:
        stop_words = set(stopwords.words('english'))
        
        
        word_frequencies = {}
        for word in word_tokenize(text.lower()):
            if word.isalnum() and word not in stop_words:
                word_frequencies[word] = word_frequencies.get(word, 0) + 1
        
        
        if not word_frequencies:
            return "Error: No meaningful words found to analyze."

        max_frequency = max(word_frequencies.values())
        for word in word_frequencies.keys():
            word_frequencies[word] = (word_frequencies[word] / max_frequency)

        
        sentence_list = sent_tokenize(text)
        sentence_scores = {}
        for sent in sentence_list:
            for word in word_tokenize(sent.lower()):
                if word in word_frequencies:
                    sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[word]

        actual_num = min(len(sentence_list), num_sentences)
        summary_sentences = heapq.nlargest(actual_num, sentence_scores, key=sentence_scores.get)
        
        return ' '.join(summary_sentences)

    except Exception as e:
        return f"An unexpected error occurred: {e}"


test_text = """
Environmental pollution, driven by industrialization, transportation, and waste, is a critical global crisis threatening human health and ecosystems. Key types include air pollution (respiratory diseases), water contamination (marine destruction), and soil degradation, causing7 million premature deaths annually, with 80% of ocean pollution originating from land-based sources, demanding urgent mitigation. 
"""
print(debugged_summarizer(test_text, num_sentences=2))