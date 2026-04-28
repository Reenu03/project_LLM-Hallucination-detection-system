def load_documents(file_path):
    with open(file_path,"r",encoding="utf-8") as file:
        text = file.read()

        documents = text.split("/n/n")
        return documents