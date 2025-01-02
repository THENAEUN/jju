# -*- coding: utf-8 -*-
"""06_01_PDFLoader.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1llCTLHkaq0Jl5D9uUo4SRPRfz6UIrP4K
"""

FILE_PATH = '/content/SPRI_AI_Brief_2023년12월호_F.pdf'

def show_metadata(docs):
  if docs:
    print('[metadata]')
    print(list(docs[0].metadata.keys()))
    print('\n[examples]')
    max_key_length = max(len(k) for k in docs[0].metadata.keys())
    for k, v in docs[0].metadata.items():
      print(f'{k:<{max_key_length}} : {v}')

pip install langchain_community

!pip install -qU pypdf

from langchain_community.document_loaders.pdf import PyPDFLoader
loader = PyPDFLoader(FILE_PATH)

docs = loader.load()

!pip install -qU pypdf

!pip install -qU PyPDFium2

pip install langchain_community

from langchain_community.document_loaders import PyPDFium2Loader
loader = PyPDFium2Loader(FILE_PATH)

docs = loader.load()

print(len(docs))
print(docs[0])
print(docs[0].page_content)

show_metadata(docs)

"""### 4. PDF Miner"""

pip install langchain_community

pip install pdfminer

from langchain_community.document_loaders import PDFMinerLoader

pip install pdfminer.six

loader = PDFMinerLoader(FILE_PATH)

docs = loader.load()

show_metadata(docs)

from langchain_community.document_loaders import PDFMinerPDFasHTMLLoader

loader = PDFMinerPDFasHTMLLoader(FILE_PATH)

docs = loader.load()

print(len(docs))

print(docs[0].page_content[:1000])
