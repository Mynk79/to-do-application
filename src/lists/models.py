from pydantic import BaseModel, Field

# Register models here

class ToDoList(BaseModel):

    id: str | None = Field(
        default=None, 
        title='ID of the List'
    )
    name: str = Field(title='Title of the List')
    items: list[dict] = Field(
        default=[{}], 
        title='List of all the Items'
    )
