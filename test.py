import gensim
import jieba
import numpy as np
from scipy.linalg import norm

model_file = 'news_12g_baidubaike_20g_novel_90g_embedding_64.bin'
model = gensim.models.KeyedVectors.load_word2vec_format(model_file, binary=True)

def vector_similarity(s1, s2):
    def sentence_vector(s):
        words = jieba.lcut(s)
        v = np.zeros(64)
        for word in words:
            v += model[word]
        v /= len(words)
        return v
    
    v1, v2 = sentence_vector(s1), sentence_vector(s2)
    # print(v1, v2)
    return np.dot(v1, v2) / (norm(v1) * norm(v2))
    # return v1, v2

def output(input_seq):
    f1 = open('question.txt', 'r')
    question = f1.read()
    question_list = question.split('\n')
    
    f2 = open('answer.txt', 'r')
    answer = f2.read()
    answer_list = answer.split('\n')
    
    target = input_seq
    max = {
        "a": 0
        }

    for string in question_list:
        temp = {string: vector_similarity(string, target)}
        if list(max.values())[0] < list(temp.values())[0]:
            max = temp
        # print(string, vector_similarity(string, target))
    index = question_list.index(list(max.keys())[0])
    f1.close()
    f2.close()
    return answer_list[index]
# 测试