from numpy import asarray, zeros
import pandas as pd
from os import path
from time import time
from nltk.tokenize import sent_tokenize,word_tokenize
import string
import re
from heapq import nlargest
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
import nltk
#from front import fileDialog as fe
def Summarize():
    sentences = []
    print("\t\t\t************* PLEASE WAIT **************\n")
    with open("data.txt","r", encoding="utf8") as file:
        read=file.readlines()
    for s in read:
        sentences.append(nltk.tokenize.sent_tokenize(s))
    sentences = [y for x in sentences for y in x] # flatten list
    clean_sentences = pd.Series(sentences).str.replace("[.!?\\-]", " ")
    clean_sentences = [s.lower() for s in clean_sentences]
    clean_sentences = [s.strip() for s in clean_sentences]

    file_path = path.relpath("C:/Users/RAVIKUMAR/Desktop/SEM 8/Porject/Ravi/kannada_stopwords.txt")
    file = open(file_path, encoding="utf8")
    stop_words=file.read()



    def remove_stopwords(sen):
        sen_new = " ".join([i for i in sen if i not in stop_words])
        return sen_new
    # remove stopwords from the sentences
    clean_sentences = [remove_stopwords(r.split()) for r in clean_sentences]
    # for i in clean_sentences:
    #     print(i)

    # creating word emmbedings
    file_path2 = path.relpath("C:/Users/RAVIKUMAR/Desktop/SEM 8/Porject/wiki.kn - Copy.txt")
    word_embeddings = {}
    f = open(file_path2, encoding='utf-8')
    for line in f:
        values =line.strip().split()
        word = values[0]
        coefs = asarray(values[2:], dtype='float32')
        word_embeddings[word] = coefs
    f.close()
    print("total word vectors for the given article: ",len(word_embeddings))


    #sentense vectors creating

    sentence_vectors = []
    for i in clean_sentences:
        if len(i) != 0:
            vector = sum([word_embeddings.get(w, np.zeros((299,))) for w in i.split()]) / (len(i.split()) + 0.001)
        else:
            vector = np.zeros((299,))
        sentence_vectors.append(vector)
    print("vector ready\n")

      # similarity matrix
    #print("len of the sentense vector",len(sentence_vectors))
    similarity_matrix = np.zeros([len(sentences), len(sentences)])
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i != j:
                similarity_matrix[i][j] = cosine_similarity(sentence_vectors[i].reshape(1, 299), sentence_vectors[j].reshape(1, 299))[0, 0]


    print("matrix ready\n")



#plot
    nx_graph = nx.from_numpy_array(similarity_matrix)
    t1 = time()
    scores = nx.pagerank(nx_graph)
    t2 = time()
    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)

    print("TextRank algorithm Run time : %f " % (t2 - t1), "seconds")
    # Extract top  sentences as the summary
    how_many = int(input("\n\nHow many lines You want to display the Summary?  :"))
    print("\n\n=================this is your Summarized document=============== \n\n")
    #Summarize.summarized_data = []

    for i in range(how_many):
        print(ranked_sentences[i][1])
        #Summarize.summarized_data.append(ranked_sentences[i][1])
    print("\n\n=================this is your original document=============== \n\n")
    original = pd.DataFrame(sentences)
    print(original)
    # stuff to run always here such as class/def
    return






if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   t3=time()
   Summarize()
   t4=time()
   print("total time to execute program code: %f "%(t4-t3),"seconds")
