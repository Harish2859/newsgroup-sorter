import React, { useState } from 'react';
import axios from 'axios';

const TextClassifier = () => {
  const [inputText, setInputText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleClassify = async () => {
    if (!inputText.trim()) {
      setError('Please enter some text');
      return;
    }

    setLoading(true);
    setError('');
    setResult(null);

    try {
      const response = await axios.post('http://localhost:5001/classify', {
        text: inputText
      });
      setResult(response.data);
    } catch (err) {
      setError('Classification failed. Make sure the server is running.');
    } finally {
      setLoading(false);
    }
  };

  const examples = [
    'I just upgraded my graphics card and the performance is amazing!',
    'The baseball season is looking great this year with our new players.',
    'Recent Mars rover data shows evidence of ancient water activity.',
    'I have been studying different biblical interpretations lately.'
  ];

  return (
    <div>
      {/* Input Section */}
      <div className="card">
        <h2 style={{ marginBottom: '16px', fontSize: '1.5rem' }}>Enter Text to Classify</h2>
        
        <textarea
          className="input"
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          placeholder="Type or paste your text here..."
          rows="6"
          style={{ marginBottom: '16px', resize: 'vertical' }}
        />

        <div style={{ display: 'flex', gap: '12px', marginBottom: '16px' }}>
          <button 
            className="btn btn-primary"
            onClick={handleClassify}
            disabled={loading || !inputText.trim()}
          >
            {loading ? 'Classifying...' : 'Classify Text'}
          </button>
          
          <button 
            className="btn btn-secondary"
            onClick={() => {
              setInputText('');
              setResult(null);
              setError('');
            }}
          >
            Clear
          </button>
        </div>

        {error && (
          <div style={{ 
            background: '#fef2f2', 
            border: '2px solid #f87171', 
            borderRadius: '8px', 
            padding: '12px',
            color: '#dc2626'
          }}>
            {error}
          </div>
        )}
      </div>

      {/* Results Section */}
      {result && (
        <div className="result">
          <h3 style={{ marginBottom: '16px', fontSize: '1.25rem' }}>Classification Result</h3>
          
          <div className="grid grid-2">
            <div>
              <p style={{ marginBottom: '8px', fontWeight: '500' }}>Category:</p>
              <p style={{ 
                fontSize: '1.5rem', 
                fontWeight: 'bold', 
                color: '#0ea5e9',
                background: 'white',
                padding: '12px',
                borderRadius: '6px'
              }}>
                {result.category}
              </p>
            </div>
            
            <div>
              <p style={{ marginBottom: '8px', fontWeight: '500' }}>Confidence:</p>
              <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                <div className="progress-bar" style={{ flex: 1 }}>
                  <div 
                    className="progress-fill"
                    style={{ width: `${(result.confidence * 100)}%` }}
                  ></div>
                </div>
                <span style={{ fontWeight: 'bold', fontSize: '1.25rem' }}>
                  {(result.confidence * 100).toFixed(1)}%
                </span>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Examples Section */}
      <div className="card">
        <h3 style={{ marginBottom: '16px', fontSize: '1.25rem' }}>Try These Examples</h3>
        
        <div className="grid grid-2">
          {examples.map((example, index) => (
            <button
              key={index}
              onClick={() => setInputText(example)}
              style={{
                background: '#f8fafc',
                border: '2px solid #e2e8f0',
                borderRadius: '8px',
                padding: '16px',
                textAlign: 'left',
                cursor: 'pointer',
                transition: 'all 0.2s'
              }}
              onMouseOver={(e) => e.target.style.background = '#f1f5f9'}
              onMouseOut={(e) => e.target.style.background = '#f8fafc'}
            >
              {example}
            </button>
          ))}
        </div>
      </div>

      {/* Categories Section */}
      <div className="card">
        <h3 style={{ marginBottom: '16px', fontSize: '1.25rem' }}>Available Categories</h3>
        
        <div className="grid grid-4">
          {[
            'alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc',
            'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x',
            'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball',
            'rec.sport.hockey', 'sci.crypt', 'sci.electronics', 'sci.med',
            'sci.space', 'soc.religion.christian', 'talk.politics.guns',
            'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc'
          ].map((category, index) => (
            <div
              key={index}
              style={{
                background: '#f1f5f9',
                padding: '8px 12px',
                borderRadius: '6px',
                fontSize: '0.875rem',
                textAlign: 'center',
                border: '1px solid #e2e8f0'
              }}
            >
              {category}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default TextClassifier;