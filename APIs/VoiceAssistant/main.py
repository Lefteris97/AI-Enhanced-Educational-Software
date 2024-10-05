from fastapi import FastAPI, UploadFile, File, BackgroundTasks, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from audio_handlers import text_to_audio_converter, audio_to_text_converter, write_down_audio

app = FastAPI()

# CORS middleware to allow communication with the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5555"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the request body model
class TextRequest(BaseModel):
    text: str

@app.post("/speak")
async def speak(request: TextRequest, background_tasks: BackgroundTasks):
    return await text_to_audio_converter(request.text, background_tasks)

@app.post("/recognize")
async def recognize_audio(file: UploadFile = File(...)):
    return await audio_to_text_converter(file)

@app.post("/create_note")
async def create_note(request: TextRequest):
    try:
        note_text = request.text
        await write_down_audio(note_text)

        return {"message":"Note saved successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating note: {str(e)}")
