from pydantic import BaseModel

# Base schema used internally for inheritance
class ProjectBase(BaseModel):
    name: str
    # email: EmailStr


# DTO for creating a new user (input)
class ProjectCreate(ProjectBase):
    password: str


# DTO for updating user info (input)
class ProjectUpdate(BaseModel):
    name: str | None = None
    # email: EmailStr | None = None


# DTO for returning user info to clients (output)
class ProjectResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True  # allows ORM model → Pydantic conversion
