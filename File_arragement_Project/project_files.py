import pathlib 
import os
import shutil



    # ruta=pathlib.Path(".\OneDrive\Desktop\Platzi\Python\CursoPython_inter\python-programs")
    # for file in ruta.iterdir():
    #     print(file.name)
    #print("la Ubicacion es:", os.getcwd())
    
        
def arrange():

    ruta=pathlib.Path("/Users/leona.LAPTOP-20L2TPHV/Downloads/")
    
    diccionario = { key : [v.name for v in ruta.glob(f'*{key}')] for key in {file.suffix for file in ruta.iterdir()}}
    
    for extention, files in diccionario.items():
        #  print(f"extension: {extention}")
        #  print(f"files: {files}")
        pass

    for file in ruta.iterdir():
        if os.path.exists("Documents")==True:
            pass
        else:
            os.mkdir("Documents")
        if os.path.exists("Pictures")==True:
            pass
        else:
            os.mkdir("Pictures")
        if os.path.exists("Programs")==True:
            pass
        else:
            os.mkdir("Programs")
        if os.path.exists("Others")==True:
            pass
        else:
            os.mkdir("Others")
        if os.path.exists("Folders")==False:
            os.mkdir("Folders")

    Folders= "Others","Programs","Pictures","Documents","Folders"    
    foldExt=""
    fol= [file for file in ruta.iterdir() if file.suffix in foldExt]
    for file in fol:  
        if file.name not in Folders:  
            shutil.move(file,"Folders")

    docsExt= ".py",".doc",".docx",".txt",".odt",".xlsx",".ppt",".pptx",".pdf",".html"       
    docs= [file for file in ruta.iterdir() if file.suffix in docsExt]
    for file in docs:    
         shutil.move(file,"Documents")
        
    picExt=   ".png",".jpg"
    pics= [file for file in ruta.iterdir() if file.suffix in picExt]
    for file in pics: 
        shutil.move(file,"Pictures")  

    progExt= ".exe",".msi"
    prog= [file for file in ruta.iterdir() if file.suffix in progExt]
    for file in prog: 
        shutil.move(file,"Programs")  

    others= [file for file in ruta.iterdir() if file.suffix not in (progExt,picExt,docsExt,foldExt)]
    for file in others:           
            shutil.move(file,"Others")


    print("your folder has been classified")
            
if __name__=="__main__":
    
    arrange()