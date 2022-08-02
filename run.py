import uvicorn
from params import SERVER_HOST, SERVER_PORT



if __name__ == '__main__':

    # Run the API with uvicorn server
    uvicorn.run("main:app", host=SERVER_HOST, port=SERVER_PORT, log_level="info", reload=True)