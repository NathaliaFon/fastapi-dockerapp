from fastapi import  APIRouter, FastAPI, Depends, HTTPException, status, Response

from database import engine,SessionLocal, Base
from schema import UsersSchema
from sqlalchemy.orm import Session
from models import User

#cria a tabela
Base.metadata.create_all(bind=engine)
router = APIRouter(prefix="/users")   

def get_db():
    try:
        db = SessionLocal()
        #TODO 
        yield db
    finally:
        db.close()


@router.post("/add")
async def add_user(request:UsersSchema, db: Session = Depends(get_db)):
    user_on_db = User(id=request.id, username=request.username, password=request.password, user_email=request.user_email)
    db.add(user_on_db)
    db.commit()
    db.refresh(user_on_db)
    return user_on_db

@router.get("/{user_username}", description="Listar usuários por \"username\"")
def get_users_by_username(user_username,db: Session = Depends(get_db)):
    user_on_db = db.query(User).filter(User.item == user_username).first()
    return user_on_db

@router.get("/users/list")
async def get_users(db: Session = Depends(get_db)):
    users= db.query(User).all()
    return users


@router.delete("/{id}", description="Deletar o usuário pelo id")
def delete_user(id: int, db: Session = Depends(get_db)):
    user_on_db = db.query(User).filter(User.id == id).first()
    if user_on_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Nenhum usuário com esse id')
    db.delete(user_on_db)
    db.commit()
    return f"O usuário com o id: {id} foi deletado.", Response(status_code=status.HTTP_200_OK)

# @app.put("/produto/{id}",response_model=User)
# async def update_produto(request:UsersSchema, id: int, db: Session = Depends(get_db)):
#     produto_on_db = db.query(User).filter(User.id == id).first()
#     print(produto_on_db)
#     if produto_on_db is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sem produto com este id')
#     produto_on_db = User(id=request.id, item=request.item, peso=request.peso, numero_caixas=request.numero_caixas)
#     db.up
#     db.(produto_on_db)
#     db.commit()
#     db.refresh(produto_on_db)
#     return produto_on_db, Response(status_code=status.HTTP_204_NO_CONTENT)


# router = APIRouter()
