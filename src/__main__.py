from fastapi import FastAPI
import uvicorn

from src.lists.routers import list_router
from src.items.routers import item_router

# Declaring the FastAPI App
app = FastAPI(
    title='To-do Application',
    description="""
        This is the source code for the CRUD API's. The course is meant for learning how to implement HTTP methods (POST, GET, PUT, PATCH, UPDATE) in the backend of the application.
    """
)

# Registering the App Routers
app.include_router(list_router)
app.include_router(item_router)


# Starting the app
if __name__ == "__main__":
    uvicorn.run('__main__:app', host='0.0.0.0', port=8000)
