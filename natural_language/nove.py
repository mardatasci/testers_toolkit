import csv
import nltk
import sys

def extract_nouns_and_verbs(text):
    sentences = nltk.sent_tokenize(text)
    nouns = set()
    verbs = set()
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        tagged_words = nltk.pos_tag(words)
        for word, tag in tagged_words:
            if tag.startswith('NN'):
                nouns.add((word, sentence))
            elif tag.startswith('VB'):
                verbs.add((word, sentence))
    return list(nouns), list(verbs)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py input_file.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        text = f.read()

    nouns, verbs = extract_nouns_and_verbs(text)

    nouns_filename = input("Enter the nouns filename: ")
    with open(nouns_filename, 'w', newline='') as nouns_file:
        writer = csv.writer(nouns_file)
        for noun, sentence in set(nouns):
            writer.writerow([noun, sentence])

    verbs_filename = input("Enter the verbs filename: ")
    with open(verbs_filename, 'w', newline='') as verbs_file:
        writer = csv.writer(verbs_file)
        for verb, sentence in set(verbs):
            writer.writerow([verb, sentence])
