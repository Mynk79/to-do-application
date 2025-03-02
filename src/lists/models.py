from pydantic import BaseModel, Field

from src.items.models import Item

# Register models here

class ToDoList(BaseModel):

    id: int | None = Field(
        default=None, 
        title='ID of the List'
    )
    name: str = Field(title='Title of the List')
    items: list[Item] = Field(
        default=[{}], 
        title='List of all the Items'
    )
