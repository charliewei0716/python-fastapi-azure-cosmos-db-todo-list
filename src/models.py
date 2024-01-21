from pydantic import BaseModel, Field

class ToDoItem(BaseModel):
    id: str = Field(..., title="The id of the item")
    name: str = Field(..., title="The name of the item")
    description: str | None = Field(default=None, title="The description of the item")
    is_complete: bool = Field(default=False, title="Whether item is completed")
