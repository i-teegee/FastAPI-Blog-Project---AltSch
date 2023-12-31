from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4


class BlogPostBase(BaseModel):
    title: str
    body: str
    author: str
    


class CreateBlogPost(BlogPostBase):
    id: Optional[UUID] = uuid4()
    created_at: Optional[datetime] = datetime.now()
    published : bool = True


class EditBlogPost(BlogPostBase):
    pass


class Responce(BlogPostBase):
    pass

class BlogRequestBody(BaseModel):
    title: str
    body: str

