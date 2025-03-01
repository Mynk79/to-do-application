from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
import os, json

from src.db import DATABASE_FILE_PATH

list_router = APIRouter(
    prefix='/v1/lists',
    tags=['list-items']
)

# Route to retrieve all the to-do lists (Summary View)
@list_router.get('')
async def get_all_lists():

    if not os.path.exists(DATABASE_FILE_PATH):
        raise JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                'data': {
                    'lists': [],
                    'count': 0
                },
                'status': 'true'
            }
        )
    
    with open(DATABASE_FILE_PATH, 'r') as file:
        list_data = json.load(file)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'data': {
                'lists': list_data,
                'count': len(list_data)
            },
            'status': 'true'
        }
    )


# Route to Create a New List
@list_router.post('')
def create_new_list():

    


    