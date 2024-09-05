from milvusdb.default_embedding_model import convert_to_vectors, encode_query
from milvusdb.milvusdb_client import create_collection_or_truncate, insert_vectors, search
import json

def create_sample_documents():
    documents = [
        "Artificial intelligence was founded as an academic discipline in 1956.",
        "Alan Turing was the first person to conduct substantial research in AI.",
        "Born in Maida Vale, London, Turing was raised in southern England.",
        "Ada Lovelace is considered the first computer programmer for her work on Charles Babbage's early mechanical general-purpose computer.",
        "Grace Hopper was a pioneer in developing computer technology and invented one of the first compiler-related tools.",
        "Tim Berners-Lee is known for inventing the World Wide Web in 1989.",
        "Linus Torvalds created the Linux kernel, a key component of many operating systems, including the Android mobile OS.",
        "John von Neumann contributed significantly to the development of computer architecture, particularly the stored-program concept.",
        "Dennis Ritchie co-created the C programming language and was one of the key figures behind Unix.",
        "Steve Jobs was a co-founder of Apple Inc. and was instrumental in the development of the iPhone and iPad.",
        "Bill Gates co-founded Microsoft and played a significant role in the personal computing revolution with MS-DOS and Windows.",
        "Mark Zuckerberg is the co-founder and CEO of Meta (formerly Facebook), one of the largest social media platforms.",
        "Elon Musk is known for his work with technology companies such as SpaceX and Tesla, contributing to innovation in AI, energy, and transportation.",
        "Claude Shannon is considered the father of information theory and contributed to the development of digital circuits.",
        "Larry Page and Sergey Brin co-founded Google, which revolutionized internet search engines and online advertising.",
        "Jeff Bezos founded Amazon, transforming the company from an online bookstore into a global e-commerce giant.",
        "Nikola Tesla made major contributions to the development of alternating current (AC) electrical systems.",
        "Charles Babbage is often referred to as the 'father of the computer' for designing the first mechanical computer, the Analytical Engine.",
        "Hedy Lamarr, alongside George Antheil, developed a frequency-hopping technology used in modern wireless communication.",
        "Vint Cerf and Bob Kahn are known as the 'fathers of the internet' for their work on TCP/IP, the foundational protocol for data exchange on the internet.",
        "Edsger Dijkstra was a pioneer in computer science, known for Dijkstra's algorithm and his contributions to programming languages.",
        "Margaret Hamilton led the software development for NASA's Apollo missions, contributing to the success of the moon landing.",
        "Douglas Engelbart is credited with inventing the computer mouse and advancing human-computer interaction.",
        "John McCarthy coined the term 'artificial intelligence' and made key contributions to the development of AI programming languages.",
        "Gordon Moore co-founded Intel and formulated Moore's Law, predicting the exponential growth of computing power.",
        "Sheryl Sandberg is known for her leadership at Meta (formerly Facebook) and her advocacy for women in leadership roles."
    ]

    return documents

# Fill the vector collection with sample documents
def fill_vector_collection(collection_name, subject):
    documents = create_sample_documents()
    vectors = convert_to_vectors(documents)
    data = [
        {"id": i, "vector": vectors[i], "text": documents[i], "subject": subject}
        for i in range(len(vectors))
    ]

    create_collection_or_truncate(collection_name)
    return  insert_vectors(collection_name, data)



def main():
    # Fill Vector collection sample
    collection_name="collection_demo"
    subject = "Computing"
    limit = 5
    fill_vector_collection_response = fill_vector_collection(collection_name, subject)
    print(f"Fill Vector Collection Result: {fill_vector_collection_response}")

    while True:
        query = input("Input your query: ")
        query_vectors = encode_query(query)
        search_response = search(collection_name, query_vectors, limit, subject)
        
        # The distance closest to 1 is the vector closest to the query.
        print(f"\n Response: \n {json.dumps(search_response, indent=4)}" )
        

if __name__ == "__main__":
    main()