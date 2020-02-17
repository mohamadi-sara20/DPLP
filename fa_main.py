import os
import sys

if __name__ == "__main__":
    path = sys.argv[1]
    os.system(f'python3 fa_2_rst2txt.py {path}')
    os.system(f'python3 fa_3_txt2conll.py {path}')
    os.system(f'python fa_segmenter.py {path}')
    os.system(f'python fa_rstparser.py {path}')
