import streamlit as st
from google.cloud import storage


#create a title
st.title("Upload your data")


# create a button to select a file in the local file system of the OS
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    
        # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    #st.write(bytes_data)
    st.write(uploaded_file.name)
    
    
# If the user clicks OK, upload the selected file to a gcp cloud storage bucket
    if st.button('Upload'):
        
        # Upload the file to a gcp cloud storage bucket
        # Create a storage client
        storage_client = storage.Client()
        # Get the bucket
        bucket_name = "edis-hkl"
        bucket = storage_client.bucket(bucket_name)
        # Create a blob
        blob = bucket.blob(uploaded_file.name)
        # Upload the file
        blob.upload_from_string(bytes_data)
        # add a variable to show the value of the variable "bucket_name"
        st.write(f"File uploaded to gcp cloud storage bucket: {bucket_name}")


       
        
    