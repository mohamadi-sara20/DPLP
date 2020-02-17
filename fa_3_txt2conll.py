import stanfordnlp
import sys
import os
import re
import traceback

def txt2conll(nlp, file_path):
    with open(f'{file_path}.txt') as f:
        text = f.read()
    outfile = open(f'{file_path}.conll', 'w')
    parse = open(file_path + '.parse', 'r').read()
    parse = re.sub(r'\s', ' ', parse)
    doc = nlp(text)
    # sentence id
    sent_id = 0
    word_ind = 0
    parse_ind = 0
    for i, sentence in enumerate(doc.sentences):
        for word in sentence.words:
            word_lemma = word.lemma
            word_pos_tag = word.upos
            word_dependency_tag = word.dependency_relation
            word_head = word.governor-1
            word_ner = 0
            parse_end = find_partial_parse(parse, parse_ind, word.text)

            if (parse_end < 0):
                word_partial_parse = '_'
            else:
                word_partial_parse = parse[parse_ind: parse_end]
                parse_ind = parse_end

            if (len(word_partial_parse) == 0):
                word_partial_parse = '_'
                
            outfile.write(f'{sent_id}\t{word_ind}\t{word.text}\t{word.lemma}\t{word_pos_tag}\t{word_dependency_tag}\t{word_head}\t{word_ner}\t{word_partial_parse}\n')
            word_ind+=1
        sent_id +=1

def find_partial_parse(text, begin, word):
    index = text.find(word, begin)
    if (index < 0):
        return -1
    index += 1
    while(index < len(text)):
        if (text[index] == '('):
            break
        index += 1
    return index


if __name__ == "__main__":
    print('====================== text 2 conll =================')
    nlp = stanfordnlp.Pipeline('tokenize,pos,lemma,depparse', lang='fa')
    path = sys.argv[1]
    if path.endswith('/'):
        path = path[:len(path)-1]
    all_files = os.listdir(path)
    for filename in all_files:
        if not filename.endswith('.txt'):
            continue
        filename = filename.split('.txt')[0]
        try:
            txt2conll(nlp, f'{path}/{filename}')
        except Exception as ex:
            print('###################################################')
            print(filename)
            print(ex)
            traceback.print_exc()
