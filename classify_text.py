#!/usr/bin/env python3
"""
Single text classification script for the web API
"""

import sys
import json
import pickle
import os
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Stopwords list (same as in training)
STOPWORDS = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "aren't", 'as', 'at',
 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 
 'can', "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during',
 'each', 'few', 'for', 'from', 'further', 
 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's",
 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's",
 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself',
 "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself',
 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own',
 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 
 'than', 'that',"that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", 
 "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 
 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's", 'where',
 "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's",'will', 'with', "won't", 'would', "wouldn't", 
 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves']

def preprocess_text(text):
    """Preprocess text (same as training)"""
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation except apostrophes
    text = re.sub(r"[^\w\s']", ' ', text)
    
    # Tokenize
    words = text.split()
    
    # Remove stopwords and short words
    words = [word for word in words if word not in STOPWORDS and len(word) > 2]
    
    # Remove numbers
    words = [word for word in words if not word.isdigit()]
    
    return ' '.join(words)

def load_model():
    """Load the trained model and vectorizer"""
    try:
        with open('model.pkl', 'rb') as f:
            model_data = pickle.load(f)
        return model_data['vectorizer'], model_data['classifier'], model_data['categories']
    except FileNotFoundError:
        # If no saved model, create a simple mock classifier for demo
        return create_mock_classifier()

def create_mock_classifier():
    """Create a mock classifier for demo purposes"""
    categories = [
        'alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc',
        'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x',
        'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball',
        'rec.sport.hockey', 'sci.crypt', 'sci.electronics', 'sci.med',
        'sci.space', 'soc.religion.christian', 'talk.politics.guns',
        'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc'
    ]
    
    # Simple keyword-based classification for demo
    def mock_classify(text):
        text_lower = text.lower()
        
        # Technology keywords
        if any(word in text_lower for word in ['computer', 'software', 'hardware', 'graphics', 'windows', 'mac', 'system']):
            if 'graphics' in text_lower:
                return 'comp.graphics', 0.85
            elif 'windows' in text_lower:
                return 'comp.os.ms-windows.misc', 0.82
            elif 'mac' in text_lower:
                return 'comp.sys.mac.hardware', 0.88
            else:
                return 'comp.sys.ibm.pc.hardware', 0.75
        
        # Sports keywords
        elif any(word in text_lower for word in ['baseball', 'hockey', 'game', 'team', 'player', 'season']):
            if 'baseball' in text_lower:
                return 'rec.sport.baseball', 0.90
            elif 'hockey' in text_lower:
                return 'rec.sport.hockey', 0.87
            else:
                return 'rec.sport.baseball', 0.70
        
        # Science keywords
        elif any(word in text_lower for word in ['science', 'research', 'study', 'data', 'space', 'mars', 'medical']):
            if 'space' in text_lower or 'mars' in text_lower:
                return 'sci.space', 0.92
            elif 'medical' in text_lower or 'health' in text_lower:
                return 'sci.med', 0.85
            elif 'electronic' in text_lower:
                return 'sci.electronics', 0.80
            else:
                return 'sci.space', 0.75
        
        # Religion keywords
        elif any(word in text_lower for word in ['god', 'religion', 'church', 'christian', 'bible', 'faith']):
            if 'christian' in text_lower or 'church' in text_lower:
                return 'soc.religion.christian', 0.88
            elif 'atheism' in text_lower or 'atheist' in text_lower:
                return 'alt.atheism', 0.85
            else:
                return 'talk.religion.misc', 0.75
        
        # Politics keywords
        elif any(word in text_lower for word in ['politics', 'government', 'policy', 'election', 'gun', 'rights']):
            if 'gun' in text_lower:
                return 'talk.politics.guns', 0.85
            elif 'mideast' in text_lower or 'middle east' in text_lower:
                return 'talk.politics.mideast', 0.80
            else:
                return 'talk.politics.misc', 0.72
        
        # Auto keywords
        elif any(word in text_lower for word in ['car', 'auto', 'motorcycle', 'engine', 'drive']):
            if 'motorcycle' in text_lower:
                return 'rec.motorcycles', 0.85
            else:
                return 'rec.autos', 0.80
        
        # Sale keywords
        elif any(word in text_lower for word in ['sale', 'sell', 'buy', 'price', 'offer']):
            return 'misc.forsale', 0.75
        
        # Default
        else:
            return 'misc.forsale', 0.60
    
    return None, mock_classify, categories

def classify_text(text):
    """Classify a single text"""
    vectorizer, classifier, categories = load_model()
    
    # Preprocess the text
    processed_text = preprocess_text(text)
    
    if vectorizer is None:  # Using mock classifier
        category, confidence = classifier(text)
        return {
            'category': category,
            'confidence': confidence,
            'processed_text': processed_text
        }
    
    # Use real classifier
    text_vectorized = vectorizer.transform([processed_text])
    prediction = classifier.predict(text_vectorized)[0]
    probabilities = classifier.predict_proba(text_vectorized)[0]
    confidence = max(probabilities)
    
    return {
        'category': prediction,
        'confidence': float(confidence),
        'processed_text': processed_text
    }

def main():
    if len(sys.argv) != 2:
        print(json.dumps({'error': 'Text argument required'}))
        sys.exit(1)
    
    text = sys.argv[1]
    
    try:
        result = classify_text(text)
        print(json.dumps(result))
    except Exception as e:
        print(json.dumps({'error': str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()