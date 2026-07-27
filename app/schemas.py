from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str

class PromptRequest(BaseModel):
    prompt: str


class PromptResponse(BaseModel):
    response: str