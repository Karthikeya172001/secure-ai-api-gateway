from pydantic import BaseModel

class PasswordReset(BaseModel):
    username: str
    new_password: str

class UserCreate(BaseModel):
    username: str
    email: str 
    password: str
    role: str = "user"


class UserLogin(BaseModel):
    username: str
    password: str


class PromptRequest(BaseModel):
    prompt: str


class Token(BaseModel):
    access_token: str
    token_type: str


class UserResponse(BaseModel):
    username: str
    email: str
    role: str


from pydantic import ConfigDict

model_config = ConfigDict(from_attributes=True)