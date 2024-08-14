from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def find_similar_sentences(dataset, query):

    model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')

    query_embedding = [model.encode(query)]
    embedding_sentences = [ [model.encode(sentence)] for sentence in dataset ]

    max_similarity = -111111
    index = -1
    for i in range(len(dataset)):
        # Calculate cosine similarity
        sentence = embedding_sentences[i]
        similarity = cosine_similarity(query_embedding, sentence)[0][0]
        if similarity > max_similarity:
            max_similarity = similarity
            index = i

    return dataset[index], max_similarity



dataset = [
    "AI is revolutionizing the healthcare industry.",
    "Machine learning models require vast amounts of data.",
    "The pharmaceutical industry benefits greatly from computer vision.",
    "Transformers are powerful models for natural language processing tasks.",
    "Data privacy is a significant concern in AI applications.",
]

sentence_input = "AI is reovlution!"
find_similar_sentences(dataset, sentence_input)