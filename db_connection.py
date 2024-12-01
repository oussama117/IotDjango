from pymongo import MongoClient

# client = MongoClient("mongodb+srv://root:samsung55@cluster0.abg3a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# client = MongoClient("mongodb+srv://admin:admin123@cluster0.qq4bi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
client = MongoClient("mongodb+srv://mohamedlouati002:G1TGhCm2T1mBp2aR@cluster0.62oql.mongodb.net/?retryWrites=true&w=majority")

# db = client['cheepNacklace']
db = client['AHDProject0']
collection = db['necklacedatas']

document_count = collection.count_documents({})
# print(f'The collection has {document_count} documents.')
