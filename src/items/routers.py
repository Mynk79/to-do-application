from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
import os, json

from src.db import DATABASE_FILE_PATH
from .models import Item

item_router = APIRouter(
    prefix='/api/v1/lists'
)


# Route to add a new item to the list
@item_router.post("/{list_id}/items")
def add_item_to_list(list_id: int, item: Item):

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

            item.id = to_do_list.get('item_index')
            to_do_list['items'].extend([item.model_dump()])
            to_do_list['item_index'] += 1

            with open(DATABASE_FILE_PATH, 'w') as file:
                json.dump(existing_data, file, indent=5)

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



# Route to mark the status of item in the list
@item_router.patch("/{list_id}/items/{item_id}/checked_state")
def mark_item_status(list_id: int, item_id: int):

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

            for item in to_do_list.get('items'):

                if item.get('id') == item_id:
                    item['checked'] = True if not item['checked'] else False

                    with open(DATABASE_FILE_PATH, 'w') as file:
                        json.dump(existing_data, file, indent=5)

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
                    'error': [{'item_id': f'Item with ID {item_id} does not Exists'}],
                    'status': 'false'
                }
            )
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={
            'error': [{'list_id': f'List with ID {list_id} does not Exists'}],
            'status': 'false' 
        }
    )



# Route to delete items from the list
@item_router.delete('/{list_id}/items/{item_id}')
def delete_item_list(list_id: int, item_id: int):

    if not os.path.exists(DATABASE_FILE_PATH):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                'error': [{'list_id': f'List with ID {list_id} does not Exists'}],
                'status': 'False'
            }
        )

    with open(DATABASE_FILE_PATH) as file:
        existing_data = json.load(file)

    for to_do_list in existing_data.get('data'):

        if to_do_list.get('id') == list_id:

            for item in to_do_list.get('items'):

                if item.get('id') == item_id:
                    to_do_list.get('items').remove(item)

                    with open(DATABASE_FILE_PATH, 'w') as file:
                        json.dump(existing_data, file, indent=5)

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
                    'error': [{'item_id': f'Item with ID {item_id} does not Exists'}],
                    'status': 'false'
                }
            ) 
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={
            'error': [{'list_id': f'List with ID {list_id} does not Exists'}],
            'status': 'false'
        }
    ) 

