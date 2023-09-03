from pydantic import BaseModel


class EmailOutputMessage(BaseModel):
    status: str
    message: str
