import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.Client()
collection = client.get_or_create_collection("documents")

model = SentenceTransformer("all-MiniLM-L6-v2")
#doc_id = "sample.pdf"
#text = "Sample PDFThis is a simple PDF ﬁle. Fun fun fun.Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus facilisis odio sed mi. Curabitur suscipit. Nullam vel nisi. Etiam semper ipsum ut lectus. Proin aliquam, erat eget pharetra commodo, eros mi condimentum quam, sed commodo justo quam ut velit. Integer a erat. Cras laoreet ligula cursus enim. Aenean scelerisque velit et tellus. Vestibulum dictum aliquet sem. Nulla facilisi. Vestibulum accumsan ante vitae elit. Nulla erat dolor, blandit in, rutrum quis, semper pulvinar, enim. Nullam varius congue risus. Vivamus sollicitudin, metus ut interdum eleifend, nisi tellus pellentesque elit, tristique accumsan eros quam et risus. Suspendisse libero odio, mattis sit amet, aliquet eget, hendrerit vel, nulla. Sed vitae augue. Aliquam erat volutpat. Aliquam feugiat vulputate nisl. Suspendisse quis nulla pretium ante pretium mollis. Proin velit ligula, sagittis at, egestas a, pulvinar quis, nisl.Pellentesque sit amet lectus. Praesent pulvinar, nunc quis iaculis sagittis, justo quam lobortis tortor, sed vestibulum dui metus venenatis est. Nunc cursus ligula. Nulla facilisi. Phasellus ullamcorper consectetuer ante. Duis tincidunt, urna id condimentum luctus, nibh ante vulputate sapien, id sagittis massa orci ut enim. Pellentesque vestibulum convallis sem. Nulla consequat quam ut nisl. Nullam est. Curabitur tincidunt dapibus lorem. Proin velit turpis, scelerisque sit amet, iaculis nec, rhoncus ac, ipsum. Phasellus lorem arcu, feugiat eu, gravida eu, consequat molestie, ipsum. Nullam vel est ut ipsum volutpat feugiat. Aenean pellentesque.In mauris. Pellentesque dui nisi, iaculis eu, rhoncus in, venenatis ac, ante. Ut odio justo, scelerisque vel, facilisis non, commodo a, pede. Cras nec massa sit amet tortor volutpat varius. Donec lacinia, neque a luctus aliquet, pede massa imperdiet ante, at varius lorem pede sed sapien. Fusce erat nibh, aliquet in, eleifend eget, commodo eget, erat. Fusce consectetuer. Cras risus tortor, porttitor nec, tristique sed, convallis semper, eros. Fusce vulputate ipsum a mauris. Phasellus mollis. Curabitur sed urna. Aliquam nec sapien non nibh pulvinar convallis. Vivamus facilisis augue quis quam. Proin cursus aliquet metus. Suspendisse lacinia. Nulla at tellus ac turpis eleifend scelerisque. Maecenas a pede vitae enim commodo interdum. Donec odio. Sed sollicitudin dui vitae justo.Morbi elit nunc, facilisis a, mollis a, molestie at, lectus. Suspendisse eget mauris eu tellus molestie cursus. Duis ut magna at justo dignissim condimentum. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus varius. Ut sit amet diam suscipit mauris ornare aliquam. Sed varius. Duis arcu. Etiam tristique massa eget dui. Phasellus congue. Aenean est erat, tincidunt eget, venenatis quis, commodo at, quam."
def add_to_chroma(doc_id,text):
    chunks = [text[i:i+500] for i in range(0,len(text),500)]
    embeddings = model.encode(chunks).tolist()
    ids = [f"{doc_id}_{i}" for i in range(len(chunks))]
    collection.add(documents = chunks, embeddings = embeddings, ids = ids)
    #print(collection.count())


# query = "What is your main idea?"
def query_chroma(query,top_k = 3):
    query_embedding = model.encode([query]).tolist()
    results = collection.query(query_embeddings = query_embedding, n_results = top_k)
    return results

#add_to_chroma(doc_id,text)
#results = query_chroma(query)
#context = results["documents"][0] if results["documents"] else ""
#print(context)
#import requests
#import os
#payload = {
#        "model" : "mistral",
#        "prompt" : f"Answer the question based on context:\n\nContext:{context}\n\nQuestion:{query}"
#    }
#answer = ""
#response = requests.post("http://localhost:11434/api/generate",json=payload,stream = True)
#for line in response.iter_lines():
#       if line:
#            chunk = line.decode("utf-8")
#            if '"response":' in chunk:
#                answer += chunk.split('"response":')[1].split(",")[0].split("\"")[1]
#
#print(answer)