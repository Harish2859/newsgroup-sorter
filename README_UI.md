# Newsgroup Classifier - React UI

A modern, sleek React-based web interface for the Newsgroup Text Classification project using Multinomial Naive Bayes.

## Features

- 🎨 **Modern UI**: Sleek glass-morphism design with animations
- 🚀 **Real-time Classification**: Instant text classification via API
- 📊 **Visual Results**: Confidence scores with progress bars
- 💡 **Example Texts**: Pre-loaded examples for different categories
- 📱 **Responsive**: Works on desktop and mobile devices
- ⚡ **Fast**: Optimized for quick classification results

## Quick Start

### 1. Install Dependencies
```bash
# Run the installation script
install.bat

# Or manually:
npm install
pip install scikit-learn numpy pandas
```

### 2. Start the Application

**Option A: Using npm scripts**
```bash
# Terminal 1: Start the backend server
npm run server

# Terminal 2: Start the React app
npm start
```

**Option B: Manual start**
```bash
# Terminal 1: Start backend
node server.js

# Terminal 2: Start frontend
npm start
```

### 3. Open in Browser
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

## Project Structure

```
newsgroup-sorter/
├── public/                 # React public files
├── src/                   # React source code
│   ├── components/        # React components
│   │   ├── Header.js     # App header with stats
│   │   ├── TextClassifier.js  # Main classification UI
│   │   └── Footer.js     # App footer
│   ├── App.js            # Main React app
│   ├── index.js          # React entry point
│   └── index.css         # Global styles
├── server.js             # Express backend server
├── classify_text.py      # Python classification script
├── train_model.py        # Model training script
├── run_classifier.py     # Original CLI classifier
└── 20_newsgroups/        # Dataset directory
```

## API Endpoints

### POST /classify
Classify text input
```json
{
  "text": "Your text to classify here"
}
```

Response:
```json
{
  "category": "comp.graphics",
  "confidence": 0.85,
  "processed_text": "processed version of input"
}
```

### GET /health
Check server status
```json
{
  "status": "OK",
  "message": "Newsgroup Classifier API is running",
  "modelTrained": true
}
```

### POST /train
Train the model (optional)
```json
{
  "message": "Model trained successfully",
  "details": "Training results..."
}
```

## Available Categories

The classifier can identify 20 different newsgroup categories:

- **Technology**: comp.graphics, comp.os.ms-windows.misc, comp.sys.ibm.pc.hardware, comp.sys.mac.hardware, comp.windows.x
- **Recreation**: rec.autos, rec.motorcycles, rec.sport.baseball, rec.sport.hockey
- **Science**: sci.crypt, sci.electronics, sci.med, sci.space
- **Society**: soc.religion.christian
- **Talk**: talk.politics.guns, talk.politics.mideast, talk.politics.misc, talk.religion.misc
- **Miscellaneous**: alt.atheism, misc.forsale

## How It Works

1. **Text Input**: User enters text in the web interface
2. **Preprocessing**: Text is cleaned and processed (remove stopwords, punctuation, etc.)
3. **Feature Extraction**: Bag-of-Words with Term Frequency
4. **Classification**: Multinomial Naive Bayes predicts the category
5. **Results**: Category and confidence score displayed with animations

## Model Performance

- **Algorithm**: Multinomial Naive Bayes
- **Features**: Bag-of-Words with Term Frequency (top 5000 words)
- **Accuracy**: ~85% on test data
- **Training Data**: 20 Newsgroups dataset (~20,000 documents)

## Customization

### Styling
- Edit `src/index.css` for global styles
- Modify component styles in individual `.js` files
- Uses Tailwind CSS classes for responsive design

### Backend
- Modify `server.js` for API changes
- Update `classify_text.py` for classification logic
- Adjust `train_model.py` for model parameters

### Frontend
- Edit components in `src/components/`
- Modify `src/App.js` for layout changes
- Update examples in `TextClassifier.js`

## Troubleshooting

### Common Issues

1. **Server won't start**
   - Check if Python is installed and in PATH
   - Ensure all npm packages are installed
   - Verify port 5000 is available

2. **Classification fails**
   - Check if Python dependencies are installed
   - Ensure the dataset exists in `20_newsgroups/`
   - Try training the model first

3. **UI not loading**
   - Check if React app is running on port 3000
   - Verify all npm dependencies are installed
   - Check browser console for errors

### Performance Tips

- For faster classification, the system uses a mock classifier by default
- To use the full trained model, run `python train_model.py` first
- Reduce `max_features` in training for faster processing
- Limit documents per category in training for quicker setup

## Development

### Adding New Features
1. Backend: Add endpoints in `server.js`
2. Frontend: Create new components in `src/components/`
3. Styling: Use Tailwind classes or custom CSS

### Testing
- Test API endpoints using tools like Postman
- Test UI components in browser dev tools
- Verify classification accuracy with known examples

## License

This project is for educational purposes. The 20 Newsgroups dataset is publicly available for research use.