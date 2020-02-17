import os
import sys

if __name__ == "__main__":
    for path in ('data/training/', 'data/test/'):
	    os.system(f'python3 fa_1_normalize.py {path}')
	    os.system(f'python3 fa_2_rst2txt.py {path}')
	    os.system(f'python3 fa_2_txt2parse.py {path}')
	    os.system(f'python3 fa_3_txt2conll.py {path}')
	    os.system(f'python3 fa_4_conll_rst2merge.py {path}')
	    os.system(f'python fa_5_rst2lisp.py {path}')
    os.system(f'python discoseg/fa_6_seg_train.py')
    os.system(f'python fa_7_parser_train.py')
