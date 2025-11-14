const express = require('express');
const cors = require('cors');
const { spawn } = require('child_process');
const path = require('path');

const app = express();
const PORT = 5001;

// Middleware
app.use(cors());
app.use(express.json());

// Store the trained model (in a real app, you'd load this from disk)
let isModelTrained = false;

// Classification endpoint
app.post('/classify', async (req, res) => {
  try {
    const { text } = req.body;
    
    if (!text || text.trim().length === 0) {
      return res.status(400).json({ error: 'Text is required' });
    }

    // Call Python script for classification
    const pythonProcess = spawn('python', [
      path.join(__dirname, 'classify_text.py'),
      text
    ]);

    let result = '';
    let error = '';

    pythonProcess.stdout.on('data', (data) => {
      result += data.toString();
    });

    pythonProcess.stderr.on('data', (data) => {
      error += data.toString();
    });

    pythonProcess.on('close', (code) => {
      if (code !== 0) {
        console.error('Python script error:', error);
        return res.status(500).json({ 
          error: 'Classification failed',
          details: error 
        });
      }

      try {
        const parsedResult = JSON.parse(result.trim());
        res.json(parsedResult);
      } catch (parseError) {
        console.error('Failed to parse Python output:', result);
        res.status(500).json({ 
          error: 'Failed to parse classification result',
          details: parseError.message 
        });
      }
    });

  } catch (error) {
    console.error('Server error:', error);
    res.status(500).json({ 
      error: 'Internal server error',
      details: error.message 
    });
  }
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({ 
    status: 'OK', 
    message: 'Newsgroup Classifier API is running',
    modelTrained: isModelTrained 
  });
});

// Train model endpoint (optional)
app.post('/train', (req, res) => {
  const pythonProcess = spawn('python', [
    path.join(__dirname, 'train_model.py')
  ]);

  let result = '';
  let error = '';

  pythonProcess.stdout.on('data', (data) => {
    result += data.toString();
  });

  pythonProcess.stderr.on('data', (data) => {
    error += data.toString();
  });

  pythonProcess.on('close', (code) => {
    if (code !== 0) {
      console.error('Training error:', error);
      return res.status(500).json({ 
        error: 'Training failed',
        details: error 
      });
    }

    isModelTrained = true;
    res.json({ 
      message: 'Model trained successfully',
      details: result.trim()
    });
  });
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
  console.log('Endpoints:');
  console.log('  POST /classify - Classify text');
  console.log('  POST /train - Train model');
  console.log('  GET /health - Health check');
});