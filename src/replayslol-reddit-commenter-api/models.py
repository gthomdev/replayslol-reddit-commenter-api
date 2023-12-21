from sqlalchemy import Boolean, Column, Integer, String
from database import Base


class RedditComment(Base):
    __tablename__ = "reddit_comments"
    id = Column(Integer, primary_key=True, index=True)
    region = Column(String)
    summoner_name = Column(String)
    submission_id = Column(String)
    date_submitted = Column(String)
    link = Column(String)
    game_id = Column(String)
    has_been_picked_up = Column(Boolean)
    has_been_replied_to = Column(Boolean)
    patch = Column(String)
    replay_link = Column(String)
    reddit_link = Column(String)
    subreddit = Column(String)
    ready_to_be_replied_to = Column(Boolean)
    error = Column(String)
    media_id = Column(String)

class RedditCommentUpdate(Base):
    __tablename__ = "reddit_comments_updates"
    id = Column(Integer, primary_key=True, index=True)
    region = Column(String)
    summoner_name = Column(String)
    submission_id = Column(String)
    date_submitted = Column(String)
    link = Column(String)
    game_id = Column(String)
    has_been_picked_up = Column(Boolean)
    has_been_replied_to = Column(Boolean)
    patch = Column(String)
    replay_link = Column(String)
    reddit_link = Column(String)
    subreddit = Column(String)
    ready_to_be_replied_to = Column(Boolean)
    error = Column(String)
    media_id = Column(String)