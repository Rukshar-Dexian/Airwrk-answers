# Load pipeline from transformers
from transformers import pipeline
# Load the summarization pipeline. Set facebook/bart-large-cnn as the model to use for summarization
'''
"facebook/bart-large-cnn" refers to a specific model that has been trained on a 
large dataset to perform text summarization. This model is provided by Facebook 
and is based on the BART (Bidirectional and Auto-Regressive Transformers) 
architecture, which is effective for tasks that require understanding and 
generating natural language. The large-cnn part indicates that this particular 
 variant is optimized for summarization tasks similar to those tackled by 
 traditional CNN news-style summaries.

'''

def create_summarizer(text):

    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    # Generate the summary
    summary = summarizer(text, max_length=150, min_length=40)

    return summary[0]['summary_text']

text = "The rapid development of AI technologies has transformed industries across the globe."
create_summarizer(text )