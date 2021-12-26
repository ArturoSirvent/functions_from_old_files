
#lo ponemos en un directorio y nos buscará todas las .py y .ipynb files dentro, y nos creará
#un 

##?? Tiene un problema y es que si partimos el nombre de la funcion en dos, no se como extraer toda la informacion de esto
#mediante expresiones regulares.

def find_files(base_dir):
    #returns a list of all the absolute paths for the .py and .ipynb files
    #it requieres glob and os

    names=([glob.glob(f"{base_dir}/**/*{i}",recursive=True) for i in [".py",".ipynb"]])
    names=[i for j in names for i in j]

    if names:
        return names
        #return [os.path.join(base_dir,i) for i in names]
    else:
    
        print("Files .py and .ipynb not found")
        return



def get_func_names_and_args(list_paths,get_args=False):

    dict_final={}
    for i in list_paths:

        name=os.path.basename(i)
        print(name)
        if name=="list_funciones_in_files.py":
            continue
        
        with open(i,"r") as f:
            text=f.read()
        if get_args:
            #func_names=re.findall(r"def (\w+\([-\.\",\w_= ()\[\]]+\)):",text)
            func_names=re.findall(r"def .*:",text)
        else:
            #func_names=re.findall(r"def (\w+)\([-\.-\",\w_= ]+\):",text)
            func_names=re.findall(r"def (\w+)\(.*:",text)
        dict_final[name]=func_names
    return dict_final


def master_get_funcs(base_dir,get_args=True):
    list_files=find_files(base_dir)
    aux=get_func_names_and_args(list_files,get_args=get_args)
    return aux

if __name__ == "__main__":
    import os 
    import glob 
    import re

    dir_aux=os.getcwd()
    output_aux=master_get_funcs(dir_aux)
    with open(os.path.join(dir_aux,"functions_in_directory.txt"),"w") as f:
        for i in output_aux:
            f.write(f"* {str(i)}")
            f.write("\n")
            for j in output_aux[i]:
                f.write(f"\t* {str(j)} \n")
                
            #f.write("\n\n")

