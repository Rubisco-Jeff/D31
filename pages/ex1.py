import streamlit as st
from utilities.ai_embedding import text_small_embedding
from utilities.ai_inference import gpt4o_mini_inference, gpt4o_mini_inference_yes_no
from utilities.chroma_db import get_or_create_persistent_chromadb_client_and_collection, add_document_chunk_to_chroma_collection, query_chromadb_collection, delete_chromadb_collection
from utilities.documents import upload_document, read_document, chunk_document, download_document, delete_document
from utilities.layout import page_config

if "problem" not in st.session_state:
    st.session_state.problem = None

if "response" not in st.session_state:
    st.session_state.response = None

# this is the main problem/response
if "sub_problem_1" not in st.session_state:
    st.session_state.sub_problem_1 = None

if "sub_response_1" not in st.session_state:
    st.session_state.sub_response_1 = None

# this is the first sub problem/response
if "sub_problem_2" not in st.session_state:
    st.session_state.sub_problem_2 = None

if "sub_response_2" not in st.session_state:
    st.session_state.sub_response_2 = None

# this is the second sub problem/response
if "sub_problem_3" not in st.session_state:
    st.session_state.sub_problem_3 = None

if "sub_response_3" not in st.session_state:
    st.session_state.sub_response_3 = None

st.subheader("Main Problem")

st.session_state.problem = "Should I get a coffee now?"

st.write(st.session_state.problem)

st.subheader("Sub Problems")

st.session_state.sub_problem_1 = "Did I have a coffee in the last two hours?"
st.session_state.sub_response_1 = st.selectbox(
    st.session_state.sub_problem_1,
    ("yes", "no", "unsure"),
    index=1
)
st.session_state.sub_response1 = gpt4o_mini_inference_yes_no(
    "you are anexpert in ansering questions.",
    f"""your task """
)


st.session_state.sub_problem_2 = "Did I get eight hours of sleep?"
st.session_state.sub_response_2 = st.selectbox(
    st.session_state.sub_problem_2,
    ("yes", "no", "unsure"),
    index=1
)

st.subheader("Solving Problem")
