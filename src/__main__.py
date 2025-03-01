from fastapi import FastAPI
import uvicorn

from src.notes.routers import list_router

# Declaring the FastAPI App
app = FastAPI(
    title='To-do Application',
    description="""
        This is the source code for the CRUD API's. The course is meant for learning how to implement HTTP methods (POST, GET, PUT, PATCH, UPDATE) in the backend of the application.
    """,
    root_path="/api"
)

# Registering the App Routers
app.include_router(list_router)


# Starting the app
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000, reload=True)
