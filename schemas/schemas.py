from pydantic import BaseModel


class TrainerBase(BaseModel):
    name: str
    sur_name: str

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    name: str
    sur_name: str
    email: str

    class Config:
        from_attributes = True


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int


class Token(BaseModel):
    access_token: str
    token_type: str
