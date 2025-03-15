# App.py
# Financial Text Analyzer

A Streamlit-based web application that performs advanced natural language processing and sentiment analysis on financial texts. The application leverages OpenAI's GPT API for generating insights and summaries, with fallback to local processing when needed.

## Features

- 📊 Sentiment Analysis using VADER
- 📝 Text Summarization (OpenAI GPT / Local)
- 🔍 Key Insights Extraction
- ❓ Q&A capabilities for financial texts
- 📈 Interactive visualizations
- 🔄 Fallback processing when API is unavailable

## Prerequisites

- Python 3.8 or higher
- OpenAI API key (optional, for advanced features)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd financial-text-analyzer
```

2. Install the required packages:
```bash
pip install streamlit openai nltk plotly vaderSentiment torch transformers
```

3. Set up your OpenAI API key (optional):
   - Create a `.env` file in the project root
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## Running the Application

1. Start the Streamlit server:
```bash
streamlit run main.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Testing the Application

1. Basic Testing:
   - Paste a sample financial text in the input area
   - Check the sentiment analysis results
   - View the generated summary and insights
   - Try the Q&A feature with sample questions

2. Sample Test Text:
```
Apple Inc. reported strong quarterly earnings, with revenue increasing by 15% year-over-year. 
The company's services segment showed particularly robust growth, while iPhone sales remained steady. 
However, supply chain challenges could pose risks in the upcoming quarters.
```

3. Features to Test:
   - Sentiment Analysis: Check if the sentiment scores and visualization appear
   - Summary: Verify if the text summary is generated
   - Insights: Confirm that key financial insights are extracted
   - Q&A: Test with questions like "What are the potential risks mentioned?"

## Usage Examples

1. Sentiment Analysis:
   - Input financial news articles or earnings reports
   - View sentiment scores and confidence metrics
   - Analyze sentiment trends through the interactive chart

2. Summary & Insights:
   - Get concise summaries of long financial texts
   - Extract key financial insights automatically
   - Topics include trends, performance, market conditions, and risks

3. Q&A Feature:
   - Ask specific questions about the text
   - Get focused answers based on the content
   - Explore different aspects of the financial information

## Error Handling

- If OpenAI API is unavailable, the application falls back to local processing
- Check error messages in the interface for troubleshooting
- Ensure all required packages are properly installed

## Additional Notes

- The application runs on port 5000 by default
- Local processing is available for basic features when API access is limited
- Large texts are automatically truncated to fit model limitations
- Sentiment analysis works offline using VADER

For more information or support, please refer to the documentation or create an issue in the repository.
