from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-V2")
import chromadb
with open("sample.txt", "r") as file:
    text =file.read()
#print(text)
#print("No of characters:",len(text))

chunks = []
chunk_size = 25
chunk_overlap = 10
step = chunk_size - chunk_overlap 
for i in range(0, len(text),step):
    chunk = text[i:i+chunk_size]
    chunks.append(chunk)
# print("No of chunks:",len(chunks))
# for i in range(len(chunks)):
#     print(i,chunk)

#embeddings
embeddings= model.encode(chunks)
# print("Embeddings created")
# print("no of embeddings",len(embeddings))
# print(embeddings[0])
# print(embeddings.shape)

#chroma db
client =chromadb.Client()
collection=client.create_collection(name="My_documents")
# print("Collection created successfully")
ids=[]
for i in  range(len(chunks)):
    ids.append(str(i))
collection.add(
    ids=ids,
    documents=chunks,
    embeddings=embeddings.tolist()
)
print("no of items in collection:",collection.count())
# results=collection.get()
# for i in range(len(results["ids"])):
#     print(f"ID: {results['ids'][i]} -> Chunk:{results['documents'][i]}")

col=collection.get(ids=['0'])
print(col)