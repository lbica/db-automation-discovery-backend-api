from pydantic import BaseModel, EmailStr

# Base schema used internally for inheritance
class UserBase(BaseModel):
    name: str
    email: EmailStr


# DTO for creating a new user (input)
class UserCreate(UserBase):
    password: str


# DTO for updating user info (input)
class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None


# DTO for returning user info to clients (output)
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True  # allows ORM model → Pydantic conversion
