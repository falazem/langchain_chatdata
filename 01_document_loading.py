import os
import openai
import sys 
from dotenv import load_dotenv, find_dotenv

#for youtube
from langchain.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.blob_loaders import FileSystemBlobLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader

_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key = os.getenv('OPENAI_API_KEY')

#Load a pdf document
# from langchain.document_loaders import PyPDFLoader
# loader = PyPDFLoader("/Users/lamatalje/Documents/Dev/LangChain_ChatData/langchain_chatdata/docs/MachineLearning-Lecture01.pdf")
# pages = loader.load()

#Load a youtube audio document
# url="https://www.youtube.com/watch?v=jGwO_UgTS7I"
# save_dir="/Users/lamatalje/Documents/Dev/LangChain_ChatData/langchain_chatdata/youtube/"

# # Download and transcribe the audio from YouTube
# loader = GenericLoader(
#     YoutubeAudioLoader([url], save_dir),
#     OpenAIWhisperParser()
# )
# docs = loader.load()

from langchain.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://github.com/basecamp/handbook/blob/master/titles-for-programmers.md")
docs = loader.load()
