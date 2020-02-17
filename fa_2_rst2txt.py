from bs4 import BeautifulSoup
import sys
import stanfordnlp
import re
import os

def rst2txt(filepath):
    nlp = stanfordnlp.Pipeline('tokenize', lang='fa')
    outfile = open(filepath + '.txt', 'w')
    rs3 = open(filepath + '.rs3', 'r').read()
    rs3 = '<xml>' + rs3 + '</xml>'
    soup = BeautifulSoup(rs3, features='lxml')
    seg_ind = 1
    tok_ind = 0
    segments = soup.find_all('segment')
    doc = ''
    for segment in segments:
        doc_obj = nlp(segment.text)
        tokens = []
        for s in doc_obj.sentences:
            for t in s.tokens:
                doc += t.text + ' '
    doc = re.sub('[ ]{2,}', ' ', doc)
    doc = doc.replace(' .', ' .\n')
    outfile.write(doc.strip())

if __name__ == "__main__":
    print('====================== rst 2 text =================')
    path = sys.argv[1]
    if path.endswith('/'):
        path = path[:len(path)-1]
    all_files = os.listdir(path)
    for filename in all_files:
        if not filename.endswith('.rs3'):
            continue
        filename = filename.split('.rs3')[0]
        try:
            rst2txt(f'{path}/{filename}')
        except Exception as ex:
            print('###################################################')
            print(ex)
            print(filename)

