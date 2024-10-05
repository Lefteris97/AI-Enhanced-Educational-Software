from fastapi import FastAPI, HTTPException, Depends, status, UploadFile, File
from pydantic import BaseModel
from typing import Annotated, List
from database import engine, SessionLocal
from models import User, PerformanceScore
from sqlalchemy.orm import Session
from fuzzy_logic_model import FuzzyLogicSystem
from datetime import datetime
from zoneinfo import ZoneInfo
from fastapi.middleware.cors import CORSMiddleware
import docx
import language_tool_python

# Define timezone for Greece
GR_TIMEZONE = ZoneInfo('Europe/Athens')

# Instantiate fuzzy logic system
fls = FuzzyLogicSystem()

# Local Language Tool Server
language_tool = language_tool_python.LanguageTool('en-US')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5555"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PageInput(BaseModel):
    user_id: int
    exercises_scores: int
    speaking_scores: int
    listening_scores: int
    class_behaviour:int
    consistency: int
    forum_usage: int

class PageOutput(BaseModel):
    student_id: int
    fname: str
    lname: str

# Response model for performance data
class PerformanceResponse(BaseModel):
    score: float
    date: datetime

    class Config:
        from_attributes = True  # To work seamlessly with SQLAlchemy models

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

# Create annotation for db for the dependency injection
db_dependency = Annotated[Session, Depends(get_db)]  ## Isws dn xreiazetai

# Endpoint to fetch student by ID
@app.get('/student/{user_id}', response_model=PageOutput)
async def get_student(user_id: int, db: Session = Depends(get_db)):
    # Find the user with the user_id and the role 'student'
    user = db.query(User).filter(User.id == user_id, User.role == 'student').first()

    if not user:
        raise HTTPException(status_code=404, detail='Student not found')
    
    return {'student_id': user.id, 'fname': user.fname, 'lname': user.lname}

# Endpoint to add a performance score for a student
@app.post('/student/performance')
async def add_performance(performance_data: PageInput, db: Session = Depends(get_db)):
    # Find the user with the user_id and the role 'student'
    user = db.query(User).filter(User.id == performance_data.user_id, User.role == 'student').first()

    if not user:
        raise HTTPException(status_code=404, detail='Student not found')

    # Calculate the performance score using fuzzy logic model
    performance_score = fls.calculate_performance(
        exercises_scores = performance_data.exercises_scores,
        speaking_scores = performance_data.speaking_scores,
        listening_scores = performance_data.listening_scores,
        class_behaviour = performance_data.class_behaviour,
        consistency = performance_data.consistency,
        forum_usage = performance_data.forum_usage
    )

    if performance_score is None:
        raise HTTPException(status_code=500, detail='Error calculating performance score')

    # Add the calculated performance score to the database
    new_score = PerformanceScore(
        student_id=performance_data.user_id,  
        score=performance_score,           
        date=datetime.now(GR_TIMEZONE) # Get current time in Greece
    )

    db.add(new_score)
    db.commit()

    return {'message': 'Performance added', 'performance': performance_score}

# Endpoint to get student performance scores for graphing
@app.get('/student/performance/{user_id}', response_model=List[PerformanceResponse])
async def get_student_performance(user_id: int, db: Session = Depends(get_db)):
    # Find the user with the user_id and the role 'student'
    user = db.query(User).filter(User.id == user_id, User.role == 'student').first()

    if not user:
        raise HTTPException(status_code=404, detail='Student not found')

    # Retrieve the performance scores with dates
    scores = db.query(PerformanceScore).filter(PerformanceScore.student_id == user_id).all()

    if not scores:
        raise HTTPException(status_code=404, detail='No performance data found for this id')

    # Return the scores formatted correctly
    return scores 


# Endpoint to process the docx and provide feedback
@app.post('/submit_essay')
async def submit_essay(file: UploadFile = File(...)):
    # Check if the file is .docx
    if not file.filename.endswith('.docx'):
        raise HTTPException(status_code=400, detail='Only .docx files are supported!')
    
    try:
         # Move the file to memory and process it
        contents = await file.read()
        with open("temp.docx", "wb") as temp_file:
            temp_file.write(contents)

        # Open the file using python-docx
        doc = docx.Document("temp.docx")
        
        # Extract and concatenate all the text from the docx
        doc_text = "\n".join([para.text for para in doc.paragraphs])

        # Get feedback from LanguageTool
        feedback = language_tool.check(doc_text)

        return {"feedback": feedback}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error processing document: {str(e)}')
