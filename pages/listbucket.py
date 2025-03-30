
import streamlit as st
from google.cloud import storage

# titel = "List Bucket"
st.title("List Bucket")

# connect to a Cloud Storage bucket and list all the files in a certain bucket
storage_client = storage.Client()
bucket_name = "edis-hkl"
blobs = storage_client.list_blobs(bucket_name)
for blob in blobs:
    st.write(blob.name)
    
