
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI,status, Request
from fastapi.responses import JSONResponse


"""
We live witht he .src in the project here cause we are not done setting up the git subrepository full setup
A user would simply have the same withotu .src.
    from autofastdantic.serve.login import make_login
    from autofastdantic.serve.crud import make_crud
"""

from autofastdantic.src.serve.login import make_login
from autofastdantic.src.serve.crud import make_crud


from models import Artwork, Artist, Competition, Judge, User
from logging import Logger
import os
logger = Logger("__main__")
app = FastAPI()


crud_models = [Artwork, Artist, Competition, Judge]
make_crud(app, crud_models)
make_login(app, User)


if __name__ == "__main__":
    if os.environ.get("env", "prod").lower() == "debug":
        #https://stackoverflow.com/questions/58642528/displaying-of-fastapi-validation-errors-to-end-users
        @app.exception_handler(RequestValidationError)
        async def validation_exception_handler(request: Request, exc: RequestValidationError):
            exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
            logger.error(request, exc_str)
            content = {'status_code': 10422, 'message': exc_str, 'data': None}
            return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)