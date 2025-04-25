from fastapi import APIRouter, Request, Form, HTTPException
from models.note import Note
from config.db import conn
from schemas.note import noteEntity,notesEntity
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from bson import ObjectId
from datetime import datetime


note=APIRouter()

templates=Jinja2Templates(directory="templates")
@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.Notes.Notes.find({}).sort("date", -1).limit(20)
    newDocs = []
    # for doc in docs:
    #     print(doc["Shayari"])
    for doc in docs:
        newDocs.append({
            "id": str(doc["_id"]),  # Convert ObjectId to string
            "title": doc["title"],
            "desc": doc["desc"],
            "important": doc.get("important", False),
            "date": doc["date"]
        })
    return templates.TemplateResponse( "index.html",
        {"request":request,"newDocs":newDocs}
    )

@note.post("/", response_class=HTMLResponse)
async def add_item(request: Request, title: str = Form(...), desc: str = Form(...)):
    conn.Notes.Notes.insert_one({
        "title": title,
        "desc": desc,
        "date": datetime.now(),
        "important": False
    })
    return RedirectResponse(url=note.url_path_for("read_item"), status_code=303)

@note.delete("/delete/{note_id}")
async def delete_item(note_id: str):
    try:
        # Convert string ID to ObjectId and delete the note
        result = conn.Notes.Notes.delete_one({"_id": ObjectId(note_id)})
        if result.deleted_count == 1:
            return JSONResponse(content={"status": "success", "message": "Note deleted successfully"})
        else:
            return JSONResponse(content={"status": "error", "message": "Note not found"}, status_code=404)
    except Exception as e:
        return JSONResponse(content={"status": "error", "message": str(e)}, status_code=500)

@note.put("/toggle-important/{note_id}")
async def toggle_important(note_id: str):
    try:
        # First get the current important status
        note = conn.Notes.Notes.find_one({"_id": ObjectId(note_id)})
        if not note:
            return JSONResponse(content={"status": "error", "message": "Note not found"}, status_code=404)
        
        # Toggle the important status
        new_status = not note.get("important", False)
        result = conn.Notes.Notes.update_one(
            {"_id": ObjectId(note_id)},
            {"$set": {"important": new_status}}
        )
        
        if result.modified_count == 1:
            return JSONResponse(content={
                "status": "success", 
                "message": f"Note marked as {'important' if new_status else 'unimportant'}",
                "is_important": new_status
            })
        else:
            return JSONResponse(content={"status": "error", "message": "Failed to update note"}, status_code=500)
    except Exception as e:
        return JSONResponse(content={"status": "error", "message": str(e)}, status_code=500)

    
