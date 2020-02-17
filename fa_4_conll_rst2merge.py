from bs4 import BeautifulSoup
import sys
import stanfordnlp
import re
import os

def merge(nlp, file_path):
    merge = open(file_path + '.merge', 'w')
    conll = open(file_path + '.conll', 'r').readlines()
    rs3 = open(file_path + '.rs3', 'r').read()
    rs3 = '<xml>' + rs3 + '</xml>'
    soup = BeautifulSoup(rs3, features='lxml')
    seg_ind = 1
    tok_ind = 0
    segments = soup.find_all('segment')

    for segment in segments:
        tok_char_ind = 0
        for ch in segment.text:
            if re.match(r'\s', ch):
                continue
            if (tok_ind >= len(conll)):
                raise Exception(f'index out of range: \nword: char_ind:{tok_char_ind}, tok_ind:{tok_ind}, seg_ind: {seg_ind}')
            word = conll[tok_ind].split('\t')[2]
            word_ch = word[tok_char_ind]
            if re.match(r'\s', word_ch):
                tok_char_ind += 1
                continue
            
            if word_ch != ch:
                raise Exception(f'word mismatch: \nword: {word}, char_ind:{tok_char_ind}, tok_ind:{tok_ind}, seg_ind: {seg_ind}')

            tok_char_ind += 1
            if (tok_char_ind >= len(word)):
                conll[tok_ind] = conll[tok_ind].strip() +  '\t' + str(seg_ind) 
                tok_ind += 1
                tok_char_ind = 0
        seg_ind += 1

    text = '\n'.join(conll)
    merge.write(text)

if __name__ == "__main__":
    print('====================== conll 2 merge =================')
    nlp = stanfordnlp.Pipeline('tokenize',lang='fa')
    path = sys.argv[1]
    if path.endswith('/'):
        path = path[:len(path)-1]
    all_files = os.listdir(path)
    for filename in all_files:
        if not filename.endswith('.conll'):
            continue
        filename = filename.split('.conll')[0]
        try:
            merge(nlp, f'{path}/{filename}')
        except Exception as ex:
            print('###################################################')
            if os.path.exists(f'{filename}.merge'):
                os.remove(f'{filename}.merge')
            print(filename)
            print(ex)








