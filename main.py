from fastapi import FastAPI,Path,UploadFile
from pydantic import BaseModel
import csv,tabula

def retrvd(rno,fnm):
    fobj=open(fnm,"r")
    csvrdr=csv.reader(fobj)
    for i in csvrdr:
        print(i[0])
        if i[0].lower()==rno.lower():
            return 1,i
    return 0,
app=FastAPI()

@app.get("/login")
async def logd(unm: str, pwd : str):
        fobj=open("/home/jsj001/login.csv","r")
        csvr=csv.reader(fobj)
        for i in csvr:
            if i[0]==unm:
                if i[1]==pwd:
                    return True
                return False
        return False
        
@app.post("/reset")
async def rst(unm: str, pwd : str , npwd: str, npwdo: str):
        fobj=open("/home/jsj001/login.csv","r")
        csvr=csv.reader(fobj)
        k=[]
        for i in csvr:
            k.append(i)
        for i in k:
            if i[0]==unm:
                if i[1]==pwd:
                    if npwd==npwdo:
                        i[1]=npwd
                        return {"message":"Password resetted successfully"}
                    return {"message":"Passwords are not same"}
                return {"message":"wrong password"}
        return {"message":"username doesn't exist"}     

@app.get("/rinp")
async def c_item(rno: str ):
    
     	x= retrvd(rno,"mess.csv")
     	if x[0]:
     	    return x[1]
     	else :
     	    return ["data not found try again"]

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    content = await file.read()
    fobj=open("temp.pdf","wb")
    fobj.write(content)
    df= tabula.read_pdf("temp.pdf",pages="all")[0]
    #df.to_csv("mess.csv")
    tabula.convert_into("temp.pdf","mess.csv",output_format="csv",pages="all")
    '''fobj=open(messno+".csv","w")
    fobj.write(str(content))'''
    fobj.close()
    
    #print(content)
    return {"filename": file.filename}