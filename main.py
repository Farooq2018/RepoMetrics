from gitingest import ingest
import streamlit as st
from urllib.parse import urlparse

def validate_github_url(url):
    """Validate and format GitHub URL"""
    try:
        parsed = urlparse(url)
        if not parsed.scheme:
            url = 'https://' + url
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        if 'github.com' not in url:
            return None
        return url.strip()
    except:
        return None

st.title('RepoMetrics Demo')
st.write('Welcome to RepoMetrics Demo App, where you can get metrics about your Repo')

# summary, tree, content = ingest("https://github.com/Farooq2018/Job-Portal-Web")
# print(summary)

github_url = st.text_input('Enter your GitHub URL:')

if github_url: #Check if URL is provided
    valid_url = validate_github_url(github_url)
    if valid_url:
        st.write(f"Processing repository: {valid_url}") # Debug print
        print(valid_url)
        #valid_url_str = f'"{valid_url}"'
        #print(valid_url_str)
        try:
            st.write("Starting ingest process...")
            summary, tree, content = ingest(valid_url)
            st.write("Ingest successful!")
            st.write(summary)
        except Exception as e:
            st.error(f"Error processing the URL: {str(e)}")
    else:
        st.info('Please enter a valid GitHub repository URL')
else:
    st.info('Please enter a GitHub URL to analyze')