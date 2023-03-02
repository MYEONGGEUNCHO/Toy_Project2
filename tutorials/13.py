'''
uvicorn 13:app --reload

Header Parameters
'''
# from typing import Union

# from fastapi import FastAPI, Header

# app = FastAPI()


# @app.get("/items/")
# async def read_items(user_agent: Union[str, None] = Header(default=None)):
#     return {"User-Agent": user_agent}

'''
Automatic conversion
'''

# from typing import Union

# from fastapi import FastAPI, Header

# app = FastAPI()


# @app.get("/items/")
# async def read_items(
#     strange_header: Union[str, None] = Header(default=None, convert_underscores=False)
# ):
#     return {"strange_header": strange_header}

'''
Duplicate headers
'''

from typing import List, Union

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(x_token: Union[List[str], None] = Header(default=None)):
    return {"X-Token values": x_token}