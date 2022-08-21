import os, json
def all_path(dirname:str):
    print(dirname)
    result = []
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            # if '.git' or '.md' in maindir.replace(dirname,''):
            #     continue
            apath = os.path.join(maindir.replace(dirname,''), filename)
            if apath.startswith('/'):
                apath = apath[1:]
            if apath.startswith('.git'):
                continue
            if apath.startswith('.idea'):
                continue
            if apath.endswith('.md'):
                continue
            result.append(apath)
    with open('Dress-Lite.json','w') as f:
        f.write(json.dumps(result))
    return result
        


print(all_path(os.getcwd()+'/Dress-Lite'))