import sys
import os


def txt2parse(file_path):
    infile = f'{file_path}.txt'
    outfile = f'{file_path}.parse'
    
    os.system(f'java -jar ../BahraniParser/parser/BerkeleyParser-1.7.jar -gr ../BahraniParser/parser/SAZEH_Train_4_cycle.gr -inputFile {infile} -outputFile {outfile}')

if __name__ == "__main__":
    print('====================== text 2 parse =================')
    path = sys.argv[1]
    if path.endswith('/'):
        path = path[:len(path)-1]
    all_files = os.listdir(path)
    for filename in all_files:
        if not filename.endswith('.txt'):
            continue
        filename = filename.split('.txt')[0]
        try:
            txt2parse(f'{path}/{filename}')
        except Exception as ex:
            print('###################################################')
            print(filename)
            print(ex)
