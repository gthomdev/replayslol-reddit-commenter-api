from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from typing import Annotated, Optional
import models
from schemas import UpdateRedditComment
from database import get_db, engine
from config import Config
import uvicorn

app = FastAPI()
config = Config()
token_auth_scheme = HTTPBearer()
host_address, valid_tokens, ssl_certfile, ssl_keyfile = config.host_address, config.valid_tokens, config.ssl_certfile, config.ssl_keyfile
models.Base.metadata.create_all(bind=engine)
db_dependency = Annotated[Session, Depends(get_db)]


def validate_token(http_auth_credentials: HTTPAuthorizationCredentials = Depends(token_auth_scheme)):
    if http_auth_credentials.scheme != "Bearer":
        print(str(http_auth_credentials))
        raise HTTPException(status_code=403, detail="Invalid authentication scheme")
    if http_auth_credentials.credentials not in valid_tokens:
        raise HTTPException(status_code=403, detail="Invalid token")

@app.get("/reddit_comments/")
async def get_reddit_comment(db: db_dependency,
                             token: Annotated[str, Depends(validate_token)],
                             id: Optional[int] = None,
                             region: Optional[str] = None,
                             summoner_name: Optional[str] = None,
                             date_submitted: Optional[str] = None,
                             link: Optional[str] = None,
                             game_id: Optional[str] = None,
                             has_been_picked_up: Optional[bool] = None,
                             has_been_replied_to: Optional[bool] = None,
                             patch: Optional[str] = None,
                             replay_link: Optional[str] = None,
                             reddit_link: Optional[str] = None,
                             subreddit: Optional[str] = None,
                             ready_to_be_replied_to: Optional[bool] = None,
                             error: Optional[str] = None,

                             media_id: Optional[str] = None,
                             ):
    query = db.query(models.RedditComment)
    if id is not None:
        query = query.filter(models.RedditComment.id == id)
    if region is not None:
        query = query.filter(models.RedditComment.region == region)
    if summoner_name is not None:
        query = query.filter(models.RedditComment.summoner_name == summoner_name)
    if date_submitted is not None:
        query = query.filter(models.RedditComment.date_submitted == date_submitted)
    if link is not None:
        query = query.filter(models.RedditComment.link == link)
    if game_id is not None:
        query = query.filter(models.RedditComment.game_id == game_id)
    if has_been_picked_up is not None:
        query = query.filter(models.RedditComment.has_been_picked_up == has_been_picked_up)
    if has_been_replied_to is not None:
        query = query.filter(models.RedditComment.has_been_replied_to == has_been_replied_to)
    if patch is not None:
        query = query.filter(models.RedditComment.patch == patch)
    if replay_link is not None:
        query = query.filter(models.RedditComment.replay_link == replay_link)
    if reddit_link is not None:
        query = query.filter(models.RedditComment.reddit_link == reddit_link)
    if subreddit is not None:
        query = query.filter(models.RedditComment.subreddit == subreddit)
    if ready_to_be_replied_to is not None:
        query = query.filter(models.RedditComment.ready_to_be_replied_to == ready_to_be_replied_to)
    if error is not None:
        query = query.filter(models.RedditComment.error == error)
    if media_id is not None:
        query = query.filter(models.RedditComment.media_id == media_id)
    return query.all() if not None else HTTPException(status_code=404, detail="RedditComment not found")


@app.patch("/reddit_comments/update-by-row-id/{row_id}")
async def update_reddit_comment_by_row_id(db: db_dependency,
                                          token: Annotated[str, Depends(validate_token)],
                                          row_id: int,
                                          update_data: UpdateRedditComment):
    comment = db.query(models.RedditComment).filter(models.RedditComment.id == row_id).first()
    if comment is None:
        raise HTTPException(status_code=404, detail="RedditComment not found")
    for var, value in vars(update_data).items():
        if value is not None:
            setattr(comment, var, value)
    db.commit()
    db.refresh(comment)
    return comment


@app.patch("/reddit_comments/update-by-media-id/{media_id}")
async def update_reddit_comment_by_row_id(db: db_dependency,
                                          token: Annotated[str, Depends(validate_token)],
                                          media_id: str,
                                          update_data: UpdateRedditComment):
    comment = db.query(models.RedditComment).filter(models.RedditComment.media_id == media_id).first()
    if comment is None:
        raise HTTPException(status_code=404, detail="RedditComment not found")
    for var, value in vars(update_data).items():
        if value is not None:
            setattr(comment, var, value)
    db.commit()
    db.refresh(comment)
    return comment

if __name__ == "__main__":
    uvicorn.run(app, host=host_address, port=443, ssl_certfile=ssl_certfile, ssl_keyfile=ssl_keyfile)