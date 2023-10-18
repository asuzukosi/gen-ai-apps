import langchain
import os
from langchain.text_splitter import CharacterTextSplitter
from PyPDF2 import PdfReader


class Code:
    pass

class Markdown:
    pass

class PDF:
    def __init__(self, files=None, path=None):
        if not files and not path:
            raise Exception("You need to either specify the list of pdf files or the path to where the pdf files are located")
        if files:
            self.files = files
        else:
            self.files = [os.path.join(path,file) for file in os.listdir(path) if file.lower().endswith("pdf")]
        self.chunks = None
        
    def load_chunks(self):
        text = ""
        for file in self.files:
            reader = PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
        self.chunks = get_chunk_texts(text)
        
    def get_chunks(self):
        return self.chunks
    

class Website:
    pass


def get_chunk_texts(text):
    text_splitter = CharacterTextSplitter(
        separator = " ",
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
        )
    chunks = text_splitter.split_text(text)
    return chunks


pdf = PDF(path="/Users/kosisochukwuasuzu/Developer/machine_learning/gen-ai-apps/src/apps/content_search/files")
pdf.load_chunks()
print(len(pdf.get_chunks()))