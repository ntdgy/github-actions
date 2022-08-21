import os
def all_path(dirname:str):
    print(dirname)
    result = []
    for maindir, subdir, file_name_list in os.walk(dirname):
        print(maindir)
        for filename in file_name_list:
            apath = os.path.join(maindir.replace(dirname,''), filename)
            result.append(apath)
    return result


print(all_path(os.getcwd()+'/Dress-Lite'))