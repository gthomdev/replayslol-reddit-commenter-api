from pydantic import BaseModel
from typing import Optional


class RedditComment(BaseModel):
    id: int
    region: str
    summoner_name: str
    submission_id: str
    date_submitted: str
    link: str
    game_id: str
    has_been_picked_up: bool
    has_been_replied_to: bool
    patch: str
    replay_link: str
    reddit_link: str
    subreddit: str
    ready_to_be_replied_to: bool
    error: str
    media_id: str


class UpdateRedditComment(BaseModel):
    region: Optional[str] = None
    summoner_name: Optional[str] = None
    submission_id: Optional[str] = None
    date_submitted: Optional[str] = None
    link: Optional[str] = None
    game_id: Optional[str] = None
    has_been_picked_up: Optional[bool] = None
    has_been_replied_to: Optional[bool] = None
    patch: Optional[str] = None
    replay_link: Optional[str] = None
    reddit_link: Optional[str] = None
    subreddit: Optional[str] = None
    ready_to_be_replied_to: Optional[bool] = None
    error: Optional[str] = None
    media_id: Optional[str] = None
