from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Annotated
import models
from database import get_db, engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/reddit_comments/{submission_id}")
async def get_reddit_comment(submission_id: str, db: db_dependency):
    comment = db.query(models.RedditComment).filter(models.RedditComment.submission_id == submission_id).first()
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment
