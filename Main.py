import streamlit as st

# Page configuration must be the first Streamlit command
st.set_page_config(page_title="Financial Text Analyzer",
                   page_icon="📊",
                   layout="wide")

import time
from utils.text_processor import TextPreprocessor
from utils.sentiment_analyzer import SentimentAnalyzer
from utils.llm_handler import LLMHandler

# Custom CSS
st.markdown("""
    <style>
    .stTextInput > div > div > input {
        background-color: #f0f2f6;
    }
    .stTextArea > div > div > textarea {
        background-color: #f0f2f6;
    }
    .main {
        padding: 2rem;
    }
    </style>
    """,
            unsafe_allow_html=True)

# Initialize components with progress indication
with st.spinner("Initializing application components..."):
    text_processor = TextPreprocessor()
    sentiment_analyzer = SentimentAnalyzer()
    llm_handler = LLMHandler()

# Title and description
st.title("📊 Financial Text Analyzer")
st.markdown("""
    Analyze financial texts using advanced NLP and AI techniques.
    Get sentiment analysis, summaries, and insights from your financial content.
""")

# Check LLM status
llm_status = llm_handler.get_status()
if not llm_status["available"]:
    st.warning(f"⚠️ {llm_status['error']}")
    if llm_status.get("local_available", False):
        st.info(
            "📝 Using local processing for text analysis. Some features may be limited."
        )

# Input section
st.header("Input Text")
input_method = st.radio("Choose input method:", ("Paste Text", "Upload File"))

text_input = ""
if input_method == "Paste Text":
    text_input = st.text_area("Enter your financial text here:",
                              height=200,
                              placeholder="Paste your financial text here...")
else:
    uploaded_file = st.file_uploader("Upload a text file", type=['txt'])
    if uploaded_file:
        text_input = uploaded_file.getvalue().decode()

# Process text when submitted
if text_input:
    with st.spinner("Processing text..."):
        # Preprocess text
        cleaned_text = text_processor.clean_text(text_input)
        processed_text = text_processor.preprocess_text(text_input,
                                                        remove_stopwords=False)

        # Create tabs for different analyses
        tab1, tab2, tab3 = st.tabs(
            ["Sentiment Analysis", "Summary & Insights", "Q&A"])

        with tab1:
            st.subheader("Sentiment Analysis")
            sentiment_results = sentiment_analyzer.analyze_sentiment(
                cleaned_text)

            # Display sentiment results
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Overall Sentiment", sentiment_results['sentiment'])
            with col2:
                st.metric("Compound Score",
                          f"{sentiment_results['compound']:.2f}")
            with col3:
                confidence = max(sentiment_results['pos'],
                                 sentiment_results['neg'],
                                 sentiment_results['neu'])
                st.metric("Confidence", f"{confidence:.2f}")

            # Display sentiment chart
            st.plotly_chart(
                sentiment_analyzer.create_sentiment_chart(sentiment_results),
                use_container_width=True)

        with tab2:
            st.subheader("Summary & Key Insights")

            # Generate summary
            with st.spinner("Generating summary..."):
                summary = llm_handler.generate_summary(cleaned_text)
                st.markdown("### Summary")
                if isinstance(summary, dict) and "error" in summary:
                    st.error(summary["error"])
                else:
                    st.write(summary)

            # Extract and display insights
            st.markdown("### Key Insights")
            with st.spinner("Extracting insights..."):
                insights = llm_handler.extract_key_insights(cleaned_text)
                if isinstance(insights, dict) and "error" in insights:
                    st.error(insights["error"])
                else:
                    for insight in insights.get('insights', []):
                        with st.expander(insight['topic']):
                            st.write(insight['detail'])

        with tab3:
            st.subheader("Ask Questions")
            if not llm_status["available"]:
                st.error(
                    "⚠️ Q&A feature is currently unavailable. This feature requires API access."
                )
            else:
                user_question = st.text_input(
                    "Ask a question about the text:",
                    placeholder="E.g., What are the main risks discussed?")

                if user_question:
                    with st.spinner("Generating answer..."):
                        answer = llm_handler.answer_question(
                            cleaned_text, user_question)
                        st.markdown("### Answer")
                        if isinstance(answer, dict) and "error" in answer:
                            st.error(answer["error"])
                        else:
                            st.write(answer)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <p>⚠️ Disclaimer: This tool provides automated analysis and should not be used as the sole basis for financial decisions.
        Always consult with qualified financial advisors for professional guidance.</p>
    </div>
    """,
            unsafe_allow_html=True)
