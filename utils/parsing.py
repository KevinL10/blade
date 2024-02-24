# from langchain.text_splitter import RecursiveCharacterTextSplitter, Language
# from langchain.document_loaders import DirectoryLoader


# def load_folder_as_chunks(folder):
#     loader = DirectoryLoader(folder, glob="**/*.py")
#     splitter = RecursiveCharacterTextSplitter.from_language(
#         language=Language.PYTHON, chunk_size=500, chunk_overlap=15,
#     )
#     return splitter.split_documents(loader.load())
