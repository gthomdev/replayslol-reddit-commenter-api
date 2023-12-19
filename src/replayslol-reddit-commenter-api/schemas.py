from pydantic import BaseModel


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
