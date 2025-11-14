#!/usr/bin/env python3
"""
Train and save the newsgroup classifier model
"""

import os
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import string
import re

# Same preprocessing as before
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
    """Preprocess text by removing metadata, punctuation, and stopwords"""
    # Remove metadata (everything before first empty line)
    lines = text.split('\n')
    content_start = 0
    for i, line in enumerate(lines):
        if line.strip() == '':
            content_start = i + 1
            break
    
    text = '\n'.join(lines[content_start:])
    
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

def load_data(data_dir):
    """Load newsgroup data from directory structure"""
    documents = []
    labels = []
    
    if not os.path.exists(data_dir):
        print(f"Data directory '{data_dir}' not found!")
        return [], []
    
    # Get all category folders
    categories = [d for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))]
    
    print(f"Found {len(categories)} categories: {categories}")
    
    for category in categories:
        category_path = os.path.join(data_dir, category)
        files = os.listdir(category_path)
        
        print(f"Loading {len(files)} documents from {category}")
        
        for filename in files[:100]:  # Limit to 100 files per category for faster training
            file_path = os.path.join(category_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    processed_content = preprocess_text(content)
                    if processed_content.strip():  # Only add non-empty documents
                        documents.append(processed_content)
                        labels.append(category)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                continue
    
    return documents, labels

def train_and_save_model():
    """Train the model and save it"""
    print("Training Newsgroup Classifier...")
    
    # Load data
    data_dir = "20_newsgroups"
    documents, labels = load_data(data_dir)
    
    if not documents:
        print("No data found! Using mock classifier.")
        return
    
    print(f"Loaded {len(documents)} documents from {len(set(labels))} categories")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        documents, labels, test_size=0.25, random_state=42, stratify=labels
    )
    
    # Vectorize text
    vectorizer = CountVectorizer(
        max_features=5000,
        min_df=2,
        max_df=0.95
    )
    
    X_train_vectorized = vectorizer.fit_transform(X_train)
    X_test_vectorized = vectorizer.transform(X_test)
    
    # Train classifier
    classifier = MultinomialNB(alpha=1.0)
    classifier.fit(X_train_vectorized, y_train)
    
    # Test accuracy
    y_pred = classifier.predict(X_test_vectorized)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Model accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")
    
    # Save model
    model_data = {
        'vectorizer': vectorizer,
        'classifier': classifier,
        'categories': sorted(set(labels)),
        'accuracy': accuracy
    }
    
    with open('model.pkl', 'wb') as f:
        pickle.dump(model_data, f)
    
    print("Model saved as 'model.pkl'")
    print(f"Training complete! Accuracy: {accuracy*100:.2f}%")

if __name__ == "__main__":
    train_and_save_model()