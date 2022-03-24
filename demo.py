import urllib.request
import random
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from thefuzz import fuzz

# Link of the book https://www.gutenberg.org/ebooks/56836
url = 'https://www.gutenberg.org/files/56836/56836-0.txt'
response = urllib.request.urlopen(url)
data = response.read()  # a `bytes` object
text = data.decode('utf-8')
# print(text) # for testing


def process_file(filename):
    """
    Makes a histogram that contains the words from a file.

    filename: string

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding='UTF8')

    strippables = string.punctuation + string.whitespace

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break

        line = line.replace('-', ' ')

        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    result = 0
    for v in hist.values():
        result += v
    return result
    # return sum(hist.values()) this can be an alternative way to calculate total words


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def most_common_inc_stopwords(hist):
    """Makes a list of word-freq pairs in descending order of frequency ibcluding stopwrods

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    lst = []
    for word, freq in hist.items():
        lst.append((freq, word))
    lst.sort(reverse=True)
    return lst


# Got help from https://github.com/AllenDowney/ThinkPython2/blob/master/code/analyze_book1.py
def print_most_common_inc_stop_words(hist, num=20):
    """Prints the most commons words in a histgram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common_inc_stopwords(hist)
    print('Including stopwords, the most common words are:')
    for freq, word in t[:num]:
        print(word, t, freq)


def most_common_exc_stopwords(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    stopwords = process_file("data/stopwords.txt")
    # print(stopwords.keys())
    lst = []
    for word, freq in hist.items():
        if excluding_stopwords:
            if word in stopwords:
                continue
        lst.append((freq, word))
    lst.sort(reverse=True)
    return lst


# Got help from https://github.com/AllenDowney/ThinkPython2/blob/master/code/analyze_book1.py
def print_most_common_exc_stopwords(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common_exc_stopwords(hist, True)
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, t, freq)


def main():
    # cleaned means no Bibliography and Index
    hist = process_file('data/Cleaned_56836-0.txt')
    notclean_hist = process_file('data/56836-0.txt')
    chapter1 = process_file('data/Chapter_1.txt')
    chapter2 = process_file('data/Chapter_2.txt')
    chapter3 = process_file('data/Chapter_3.txt')
    chapter4 = process_file('data/Chapter_4.txt')

    # print(hist)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    g = most_common_inc_stopwords(hist)
    print("Including the stopwords, the most common 20 words and their frequncies are:")
    print("WORD", "FREQUENCY")
    for freq, word in g[0:20]:
        print(word, freq)

    y = most_common_exc_stopwords(notclean_hist, True)
    print("In the version with Biblioraphy and Index, excluding the stopwords, the most common 20 words and their frequncies are:")
    print("WORD", "FREQUENCY")
    for freq, word in y[0:20]:
        print(word, freq)

    z = most_common_exc_stopwords(hist, True)
    print("Excluding the stopwords, the most common 20 words their frequncies are:")
    print("WORD", "FREQUENCY")
    for freq, word in z[0:20]:
        print(word, freq)

    z = most_common_exc_stopwords(chapter1, True)
    print("In chapter 1, excluding the stopwords, the most common 20 words and their frequncies are:")
    print("WORD", "FREQUENCY")
    for freq, word in z[0:20]:
        print(word, freq)

    z = most_common_exc_stopwords(chapter2, True)
    print("In chapter 2, excluding the stopwords, the most common 20 words and their frequncies are:")
    print("WORD", "FREQUENCY")
    for freq, word in z[0:20]:
        print(word, freq)

    z = most_common_exc_stopwords(chapter3, True)
    print("In chapter 3, excluding the stopwords, the most common 20 words and their frequncies are:")
    print("WORD", "FREQUENCY")
    for freq, word in z[0:20]:
        print(word, freq)

    z = most_common_exc_stopwords(chapter4, True)
    print("In chapter 4, excluding the stopwords, the most common 20 words and their frequncies are:")
    print("WORD", "FREQUENCY")
    for freq, word in z[0:20]:
        print(word, freq)

    chapter_1234 = open('data/Cleaned_56836-0.txt', encoding='UTF8').read()
    chapter_1 = open('data/Chapter_1.txt', encoding='UTF8').read()
    chapter_2 = open('data/Chapter_2.txt', encoding='UTF8').read()
    chapter_3 = open('data/Chapter_3.txt', encoding='UTF8').read()
    chapter_4 = open('data/Chapter_4.txt', encoding='UTF8').read()

    # Got help from https://towardsdatascience.com/a-beginners-guide-to-sentiment-analysis-in-python-95e354ea84f6
    nlp1234 = SentimentIntensityAnalyzer().polarity_scores(chapter_1234)
    nlp1 = SentimentIntensityAnalyzer().polarity_scores(chapter_1)
    nlp2 = SentimentIntensityAnalyzer().polarity_scores(chapter_2)
    nlp3 = SentimentIntensityAnalyzer().polarity_scores(chapter_3)
    nlp4 = SentimentIntensityAnalyzer().polarity_scores(chapter_4)

    print("Using Natural Language Processing, Sentiment Intensity of whole book is", nlp1234)
    print("Using Natural Language Processing, Sentiment Intensity of Chapter 1 is", nlp1)
    print("Using Natural Language Processing, Sentiment Intensity of Chapter 2 is", nlp2)
    print("Using Natural Language Processing, Sentiment Intensity of Chapter 3 is", nlp3)
    print("Using Natural Language Processing, Sentiment Intensity of Chapter 4 is", nlp4)

    chap12 = (fuzz.ratio(chapter_1, chapter_2))
    chap13 = (fuzz.ratio(chapter_1, chapter_3))
    chap14 = (fuzz.ratio(chapter_1, chapter_4))
    chap23 = (fuzz.ratio(chapter_2, chapter_3))
    chap24 = (fuzz.ratio(chapter_2, chapter_4))
    chap34 = (fuzz.ratio(chapter_3, chapter_4))

    print("By using The Fuzz Library which uses Levenshtein Distance, the distance between Chapter 1 and 2 is", chap12)
    print("By using The Fuzz Library which uses Levenshtein Distance, the distance between Chapter 1 and 3 is", chap13)
    print("By using The Fuzz Library which uses Levenshtein Distance, the distance between Chapter 1 and 4 is", chap14)
    print("By using The Fuzz Library which uses Levenshtein Distance, the distance between Chapter 2 and 3 is", chap23)
    print("By using The Fuzz Library which uses Levenshtein Distance, the distance between Chapter 2 and 4 is", chap24)
    print("By using The Fuzz Library which uses Levenshtein Distance, the distance between Chapter 3 and 4 is", chap34)


if __name__ == '__main__':
    main()
