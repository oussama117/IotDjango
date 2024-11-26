from pymongo import MongoClient

# client = MongoClient("mongodb+srv://root:samsung55@cluster0.abg3a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
client = MongoClient("mongodb+srv://admin:admin123@cluster0.qq4bi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# db = client['cheepNacklace']
db = client['users_management']
collection = db['necklaceData']

document_count = collection.count_documents({})
# print(f'The collection has {document_count} documents.')
