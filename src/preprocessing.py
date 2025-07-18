# USED JUPYTER NOTEBOOK TO ANALYSE WHAT NEEDS TO BE CLEANED
from ingestion import parse_pdf
import re
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os,sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "src")))
from config import CHUNK_SIZE,CHUNK_OVERLAP

def clean_text1(text):
    # CLEANING LOGIC FOR PDF 1
    lines = text.split("\n")
    cleaned_lines = []

    for line in lines:
        stripped = line.strip()

        # Remove known headers/footers
        if stripped in ("FINANCIAL POLICIES", "Lake County G overnment"):
            continue


        if re.fullmatch(r"\d+", stripped):
            continue

        cleaned_lines.append(line) 

    return "\n".join(cleaned_lines)
def clean_text2(text):
    # CLEANING LOGIC FOR PDF 2
    lines = text.split("\n")
    cleaned_lines = []

    for line in lines:
        stripped = line.strip()


        if stripped.lower() == "financial policies":
            continue


        if re.fullmatch(r"\d+\s*\|\s*Page", stripped, re.IGNORECASE):
            continue
        if re.fullmatch(r"Page\s+\d+", stripped, re.IGNORECASE):
            continue

        cleaned_lines.append(line)  

    return "\n".join(cleaned_lines)
def clean_text3(text):
    # CLEANING LOGIC FOR PDF 3
    lines = text.split("\n")
    cleaned_lines = []

    for line in lines:
        stripped = line.strip()

        # Remove "Copyright © 2019" exactly (case-insensitive, optional spaces)
        if re.fullmatch(r"Copyright\s+©\s+2019", stripped, re.IGNORECASE):
            continue

        # Remove lines that are just page numbers (e.g., "8")
        if re.fullmatch(r"\d+", stripped):
            continue

        cleaned_lines.append(line)  
    return "\n".join(cleaned_lines)
def clean_text4(text):
    # CLEANING LOGIC FOR PDF 4
    lines = text.split("\n")
    cleaned_lines = []

    for line in lines:
        stripped = line.strip()

        # Removing "Page | X" footer
        if re.fullmatch(r"Page\s*\|\s*\d+", stripped, re.IGNORECASE):
            continue

        # Remove the exact HUD review header/footer line
        if stripped == "May 3, 2016 DRAFT – Pending HUD Legal Counsel Review":
            continue

        cleaned_lines.append(line)  

    return "\n".join(cleaned_lines)

def cleaning(file_path1,file_path2,file_path3,file_path4):
    docs1 = parse_pdf(file_path1)
    docs2 = parse_pdf(file_path2)
    docs3 = parse_pdf(file_path3)
    docs4 = parse_pdf(file_path4)
    cleaned_docs1 = []
    cleaned_docs2 = []
    cleaned_docs3 = []
    cleaned_docs4 = []
    for doc in docs1:
        cleaned_docs1.append(Document(page_content=clean_text1(doc.page_content), metadata=doc.metadata))
    for doc in docs2:
        cleaned_docs2.append(Document(page_content=clean_text2(doc.page_content), metadata=doc.metadata))
    for doc in docs3:
        cleaned_docs3.append(Document(page_content=clean_text3(doc.page_content), metadata=doc.metadata))
    for doc in docs4:
        cleaned_docs4.append(Document(page_content=clean_text4(doc.page_content), metadata=doc.metadata))
    return cleaned_docs1,cleaned_docs2,cleaned_docs3,cleaned_docs4

def chunking(cleaned_docs1,cleaned_docs2,cleaned_docs3,cleaned_docs4,chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    chunks1 = splitter.split_documents(cleaned_docs1)
    chunks2 = splitter.split_documents(cleaned_docs2)
    chunks3 = splitter.split_documents(cleaned_docs3)
    chunks4 = splitter.split_documents(cleaned_docs4)
    return chunks1,chunks2,chunks3,chunks4
def clean_and_chunk(file_path1,file_path2,file_path3,file_path4):
    cleaned_docs1,cleaned_docs2,cleaned_docs3,cleaned_docs4 = cleaning(file_path1,file_path2,file_path3,file_path4)
    chunks1,chunks2,chunks3,chunks4 = chunking(cleaned_docs1,cleaned_docs2,cleaned_docs3,cleaned_docs4)
    return chunks1,chunks2,chunks3,chunks4


# USED JUPYTER NOTEBOOK TO ANALYSE WHAT NEEDS TO BE CLEANED