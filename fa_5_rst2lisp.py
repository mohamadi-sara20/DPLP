import discoursegraphs as dg
import sys
import os
import traceback

def rs2lisp(file_path):
	tree = dg.read_rs3tree(file_path+'.rs3')
	dg.write_dis(tree, output_file=file_path+'.dis')

if __name__ == "__main__":
    print('====================== rst 2 lisp =================')
    path = sys.argv[1]
    if path.endswith('/'):
        path = path[:len(path)-1]
    all_files = os.listdir(path)
    for filename in all_files:
 		# process only merged files
        if not filename.endswith('.merge'):
            continue
        filename = filename.split('.merge')[0]
        try:
            rs2lisp(path+'/'+filename)
        except Exception as ex:
            print('###################################################')
            # if os.path.exists(path+'/'+filename+'.dis'):
            # 	os.remove(path+'/'+filename+'.dis')
            print(filename)
            print(ex)
            print(traceback.format_exc())



