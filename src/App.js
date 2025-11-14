import React, { useState } from 'react';
import TextClassifier from './components/TextClassifier';

function App() {
  return (
    <div className="container">
      <header style={{ textAlign: 'center', marginBottom: '40px' }}>
        <h1 style={{ fontSize: '2.5rem', fontWeight: 'bold', marginBottom: '16px' }}>
          Newsgroup Classifier
        </h1>
        <p style={{ fontSize: '1.1rem', color: '#64748b' }}>
          AI-powered text classification for 20 newsgroup categories
        </p>
      </header>
      
      <TextClassifier />
    </div>
  );
}

export default App;