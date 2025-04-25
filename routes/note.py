from fastapi import APIRouter
from models.note import Note
from config.db import conn
from schemas.note import noteEntity,notesEntity
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from bson import ObjectId


note=APIRouter()

templates=Jinja2Templates(directory="templates")
@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.Notes.Notes.find({}).limit(20)
    newDocs = []
    # for doc in docs:
    #     print(doc["Shayari"])
    for doc in docs:
        newDocs.append({
            "id": str(doc["_id"]),  # Convert ObjectId to string
            "title": doc["title"],
            "desc": doc["desc"],
            "important": doc.get("important", False)
        })
    return templates.TemplateResponse( "index.html",
        {"request":request,"newDocs":newDocs}
    )

@note.post("/")
async def create_item(request: Request):
    form=await request.form()
    formDict=dict(form)
    # Convert important to boolean
    formDict["important"] = True if formDict.get("important") == "on" else False
    note=conn.Notes.Notes.insert_one(formDict)
    return RedirectResponse(url="/", status_code=303)

@note.delete("/delete/{note_id}")
async def delete_note(note_id: str):
    try:
        # Convert string ID to ObjectId and delete the note
        result = conn.Notes.Notes.delete_one({"_id": ObjectId(note_id)})
        if result.deleted_count == 1:
            return JSONResponse(content={"success": True, "message": "Note deleted successfully"})
        else:
            return JSONResponse(content={"success": False, "message": "Note not found"}, status_code=404)
    except Exception as e:
        return JSONResponse(content={"success": False, "message": str(e)}, status_code=500)

    
