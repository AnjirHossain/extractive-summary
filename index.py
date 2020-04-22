import numpy as np
import networkx as nx
import requests
from nltk.cluster.util import cosine_distance
from bs4 import BeautifulSoup
from timeit import timeit

# Load html from given url
stopwords = [
    "I"
    "me"
    "my"
    "myself"
    "we"
    "our"
    "ours"
    "ourselves"
    "you"
    "you're"
    "you've"
    "you'll"
    "you'd"
    "your"
    "yours"
    "yourself"
    "yourselves"
    "he"
    "him"
    "his"
    "himself"
    "she"
    "she's"
    "her"
    "hers"
    "herself"
    "it"
    "it's"
    "its"
    "itself"
    "they"
    "them"
    "their"
    "theirs"
    "themselves"
    "what"
    "which"
    "who"
    "whom"
    "this"
    "that"
    "that'll"
    "these"
    "those"
    "am"
    "is"
    "are"
    "was"
    "were"
    "be"
    "been"
    "being"
    "have"
    "has"
    "had"
    "having"
    "do"
    "does"
    "did"
    "doing"
    "a"
    "an"
    "the"
    "and"
    "but"
    "if"
    "or"
    "because"
    "as"
    "until"
    "while"
    "of"
    "at"
    "by"
    "for"
    "with"
    "about"
    "against"
    "between"
    "into"
    "through"
    "during"
    "before"
    "after"
    "above"
    "below"
    "to"
    "from"
    "up"
    "down"
    "in"
    "out"
    "on"
    "off"
    "over"
    "under"
    "again"
    "further"
    "then"
    "once"
    "here"
    "there"
    "when"
    "where"
    "why"
    "how"
    "all"
    "any"
    "both"
    "each"
    "few"
    "more"
    "most"
    "other"
    "some"
    "such"
    "no"
    "nor"
    "not"
    "only"
    "own"
    "same"
    "so"
    "than"
    "too"
    "very"
    "can"
    "will"
    "just"
    "don't"
    "should"
    "should've"
    "now"
    "d"
    "ll"
    "ain't"
    "aren't"
    "couldn't"
    "didn't"
    "doesn't"
    "hadn't"
    "hasn't"
    "haven't"
    "isn"
    "isn't"
    "ma"
    "mightn't"
    "mustn't"
    "needn't"
    "shan"
    "shan't"
    "shouldn't"
    "wasn't"
    "weren"
    "weren't"
    "won"
    "won't"
    "wouldn't"
]


def load(url=None):
    if url is None:
        return None

    try:
        return requests.get(url).text
    except requests.exceptions.RequestException as err:
        raise SystemExit("RequestException:load: ", err)
    except requests.exceptions.HTTPError as errh:
        raise SystemExit("Http Error:load: ", errh)
    except requests.exceptions.ConnectionError as errc:
        raise SystemExit("Error Connecting:load: ", errc)
    except requests.exceptions.Timeout as errt:
        raise SystemExit("Timeout Error:load: ", errt)


# Parse and get all text from paragraphs in html


def parse_html(origin_doc=None):
    if origin_doc is None:
        return None

    soup = BeautifulSoup(origin_doc, 'lxml')
    paragraphs = soup('p')
    result = ''

    for p in paragraphs:
        result = result + p.get_text() + ' '

    return result

# Get cleaned text from url


def get_text_from_page(url=None):
    return 'No url provided' if url is None else parse_html(load(url))


#


def tokenize_parsed_html(origin_doc=None):
    if origin_doc is None:
        return None

    soup = BeautifulSoup(origin_doc, 'lxml')
    paragraphs = soup('p')
    result = []

    for p in paragraphs:
        sentences = process_p(p.get_text() + ' ')
        result = result + sentences

    return result

# process each sentence in paragraph


def process_p(origin_doc=None):
    if origin_doc is None:
        return None

    article = origin_doc.split(". ")
    sentences = []

    for sentence in article:
        tokenized_sentence = sentence.replace("[^a-zA-Z]", " ").split(" ")
        sentences.append(tokenized_sentence)

    return sentences


# build similarity matrix
def build_similarity_matrix(sentences, stopwords):
    sentences_len = len(sentences)
    sentences_len_range = range(sentences_len)
    summary_matrix = np.zeros((sentences_len, sentences_len))

    for row in sentences_len_range:
        for column in sentences_len_range:
            if row != column:
                summary_matrix[row][column] = sentence_similarity(
                    sentences[row],
                    sentences[column],
                    stopwords
                )

    return summary_matrix

# TODO: unit test


def sentence_similarity(sentence_a, sentence_b, stopwords):
    a_tokenized = [w.lower() for w in sentence_a]
    b_tokenized = [w.lower() for w in sentence_b]

    all_words = list(set(a_tokenized + b_tokenized))
    all_words_len = len(all_words)

    vector_a = [0] * all_words_len
    vector_b = [0] * all_words_len

    for w in a_tokenized:
        if w not in stopwords:
            vector_a[all_words.index(w)] += 1

    for w in b_tokenized:
        if w not in stopwords:
            vector_b[all_words.index(w)] += 1

    return 1 - cosine_distance(vector_a, vector_b)

# TODO: add damping parameter to graph generation


def generate_summary(doc=None, rank_lower_bound=4):
    if doc is None:
        return 'Error: please provide valid input doc'

    summarized_text = []
    sentences = tokenize_parsed_html(doc)

    # 1) Build similarity matrix
    similarity_matrix = build_similarity_matrix(sentences, stopwords)

    # 2) Rank sentences in similarity matrix
    similarity_graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(similarity_graph)

    # 3) Sort scores and pick top sentences
    ranked_sentences = sorted(
        ((scores[i], s) for i, s in enumerate(sentences)), reverse=True)

    for i in range(rank_lower_bound):
        summarized_text.append(" ".join(ranked_sentences[i][1]))

    # 4) Return summary
    return " ".join(summarized_text)


sentences = load(
    'https://www.theatlantic.com/health/archive/2020/03/how-will-coronavirus-end/608719/'
)

print(generate_summary(sentences, 20))
