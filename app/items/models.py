from pydantic import BaseModel, Field

# Register models here

class Item(BaseModel):

    id: int | None = Field(
        default=None, 
        title='ID of the Item'
    )
    name: str = Field(title='Title of the Item')
    checked: bool = Field(
        default=False,
        title='Status of the Item'
    )