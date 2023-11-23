from uuid import uuid4, UUID
from fastapi import FastAPI
from typing import List
from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        id= UUID("45e34661-75ac-416a-93d0-e76ab2c34c95"),
        first_name= 'Dennis',
        last_name= 'Chilinga',
        gender= Gender.male,
        roles= [Role.user]
    ),
    User(
        id= uuid4(),
        first_name= 'Eunice',
        last_name= 'Ndelemani',
        gender= Gender.female,
        roles= [Role.student, Role.admin]
    ),
    User(
        id= uuid4(),
        first_name= 'Gerald',
        last_name= 'Chilinga',
        gender= Gender.female,
        roles= [Role.user, Role.admin, Role.student]
    )
    
    
    
]
@app.get("/")
async def root():
    return {"Hello" : "Dennis"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;
