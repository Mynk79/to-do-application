from fastapi import APIRouter, HTTPException, status, Request
from fastapi.responses import JSONResponse, Response
import os, json

from app.db import DATABASE_FILE_PATH
from .models import ToDoList

list_router = APIRouter(
    prefix='/api/v1/lists',
    tags=['list-items']
)


# Route to Create a New List
@list_router.post('')
def create_new_list(to_do_list: ToDoList):

    if os.path.exists(DATABASE_FILE_PATH):

        with open(DATABASE_FILE_PATH) as file:
            existing_data = json.load(file)

        # Assigning ID to each item
        for item_index, item in enumerate(to_do_list.items, start=1):
            item.id = item_index

        # Adding the details into database object
        to_do_list.id = existing_data.get('index')
        existing_data['index'] += 1

        _db_object = to_do_list.model_dump()
        _db_object.update({
            'item_index': len(to_do_list.items) + 1
        })

        existing_data['data'].extend([_db_object])

        # Updating the details into the database
        with open(DATABASE_FILE_PATH, 'w') as file:
            json.dump(existing_data, file, indent=5)

    else:

        # Creating the database object
        to_do_list.id = 1

        # Assigning ID to each item
        for item_index, item in enumerate(to_do_list.items, start=1):
            item.id = item_index

        # Adding the details into database object
        _db_object = to_do_list.model_dump()
        _db_object.update({
            'item_index': len(to_do_list.items) + 1
        })

        _table_first_entry = {
            'index': 2,
            'data': [_db_object]
        }

        # Updating the details into the database
        with open(DATABASE_FILE_PATH, 'a') as file:
            json.dump(_table_first_entry, file, indent=5)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED, 
        content={
            'data': _db_object,
            'status': 'true'
        }
    )



# Route to retrieve a specific to-do list
@list_router.get("/{list_id}")
def get_specific_list(list_id: int):

    if not os.path.exists(DATABASE_FILE_PATH):

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                'error': [{'list_id': f'List with ID {list_id} does not Exists'}],
                'status': 'false'
            }
        )

    with open(DATABASE_FILE_PATH) as file:
        existing_data = json.load(file)

    for to_do_list in existing_data.get('data'):

        if to_do_list.get('id') == list_id:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    'data': to_do_list,
                    'status': 'true'
                }
            )
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={
            'error': [{'list_id': f'List with ID {list_id} does not Exists'}],
            'status': 'false'
        }
    )
    


# Route to delete a specific list 
@list_router.delete('/{list_id}')
def get_specific_list(list_id: int):

    if not os.path.exists(DATABASE_FILE_PATH):

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                'error': [{'list_id': f'List with ID {list_id} does not Exists'}],
                'status': 'false'
            }
        )

    with open(DATABASE_FILE_PATH) as file:
        existing_data = json.load(file)

    for to_do_list in existing_data.get('data'):

        if to_do_list.get('id') == list_id:
            existing_data.get('data').remove(to_do_list)

            with open(DATABASE_FILE_PATH, 'w') as file:
                json.dump(existing_data, file, indent=5)

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={
            'error': [{'list_id': f'List with ID {list_id} does not Exists'}],
            'status': 'false'
        }
    )



# Route to retrieve all the to-do lists (Summary View)
@list_router.get('')
async def get_all_lists(request: Request, limit: int = 5, offset: int = 5):

    if not os.path.exists(DATABASE_FILE_PATH):
        return JSONResponse(
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
        existing_data = json.load(file)

    _total_data = existing_data.get('data')[offset:limit+offset]

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'data': {
                'lists': _total_data,
                'count': len(_total_data),
                'next': f'{request.base_url}{request.url.path.replace("/","", 1)}?limit={limit}&offset={offset+limit}'
            },
            'status': 'true'
        }
    )



    


    