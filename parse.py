import os


def main():
    delete_list_file = 'aluminum_parts_list.txt'
    to_be_deleted = get_files_to_be_deleted(delete_list_file)
    print("%s files in the list to be deleted." % len(to_be_deleted.keys()))

    # Walk the directory tree
    voron_stls = "./VORON2.4"
    found_files = dict()
    for root, dirs, files in os.walk(voron_stls):
        for filename in files:
            if filename in to_be_deleted.keys():
                found_files[os.path.join(root,filename)] = 1

    
    print("Wil delete %s files" % len(found_files.keys())) 
    for filename in found_files.keys():
        print("Deleting %s" % filename)    
        os.remove(filename)
def get_files_to_be_deleted(delete_list_file):
    to_be_deleted = {}
    with open(delete_list_file, 'r') as f:
        for line in f:
            if line.startswith('#'):
                # Ignore commented lines
                continue
            elif '#' in line:
                #Ignore inline comments
                parts = line.split('#')
                to_be_deleted[parts[0].strip()] = 1
            else:
                to_be_deleted[line.strip()] = 1
    return to_be_deleted



if __name__ == "__main__" : main()
