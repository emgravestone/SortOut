import os
import datetime

class Document:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def show(self):
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Content: ", self.content)
        print("Created at: ", self.created_at)

class DocumentManager:
    def __init__(self, folder_path):
        self.folder_path = os.path.join('C:/','Users','ethan','MyCode','SortOut','Documents',) //add your own path here
        self.documents = []
        self.load_documents()

    def load_documents(self):
        for file_name in os.listdir(self.folder_path):
            if file_name.endswith(".txt"):
                file_path = os.path.join(self.folder_path, file_name)
                with open(file_path, "r") as f:
                    content = f.read()
                    title = file_name[:-4]
                    document = Document(title, "", content)
                    self.documents.append(document)

    def add_document(self, document):
        file_name = document.title + ".txt"
        file_path = os.path.join(self.folder_path, file_name)
        with open(file_path, "w") as f:
            f.write(document.content)
        self.documents.append(document)

    def list_documents(self):
        print("List of documents:")
        for document in self.documents:
            print(" - " + document.title)

    def get_document(self, title):
        for document in self.documents:
            if document.title == title:
                return document
        return None

folder_path = "documents"
document_manager = DocumentManager(folder_path)

while True:
    print("\nDocument Management System")
    print("1. Add document")
    print("2. List documents")
    print("3. Get document")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        title = input("Enter title: ")
        content = input("Enter content: ")
        document = Document(title, "", content)
        document_manager.add_document(document)
        print("Document added.")
    elif choice == 2:
        document_manager.list_documents()
    elif choice == 3:
        title = input("Enter title: ")
        document = document_manager.get_document(title)
        if document:
            document.show()
        else:
            print("Document not found.")
    elif choice == 4:
        break
    else:
        print("Invalid choice.")
