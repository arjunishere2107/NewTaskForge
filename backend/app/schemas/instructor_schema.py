from pydantic import BaseModel


class InstructorCreate(BaseModel):

    name: str
    phone: str
    email: str

    type: str