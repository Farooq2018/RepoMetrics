import streamlit as st
from bleach.html5lib_shim import convert_entities
from gitingest import ingest
from urllib.parse import urlparse
import traceback
import asyncio
import sys

# Fix for Windows: enable subprocess support in asyncio
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

def validate_github_url(url):
    """Ensure the URL is well-formed and points to GitHub."""
    try:
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        parsed = urlparse(url)
        if 'github.com' not in parsed.netloc:
            return None
        return url.strip()
    except:
        return None

# Streamlit UI
st.title('RepoMetrics Demo')
st.write('Welcome to RepoMetrics Demo App, where you can get metrics about your Repo')

github_url = st.text_input('Enter your GitHub URL:')

if github_url:
    valid_url = validate_github_url(github_url)
    if valid_url:
        st.write(f"Processing repository: {valid_url}")
        try:
            st.spinner("Ingesting repository data...")
            summary, tree, content = ingest(valid_url)
            st.success("Ingest successful!")
            st.write(summary)
        except Exception as e:
            st.error(f"❌ Error processing the URL: {str(e)}")
            st.code(traceback.format_exc(), language='python')
    else:
        st.warning("Please enter a valid GitHub URL.")
else:
    st.info("Enter a GitHub URL to begin.")
