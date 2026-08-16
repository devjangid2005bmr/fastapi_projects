from sqlalchemy import create_engine , Column , Integer , String

from sqlalchemy.orm import sessionmaker , declarative_base , Session

from fastapi import FastAPI , Depends , HTTPException

app =FastAPI()

DATABASE_URL = "sqlite:///./test2.db"

engine = create_engine(
    DATABASE_URL , 
    connect_args={"check_same_thread":False}
)

sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"
    
    id  = Column(Integer,primary_key=True , index=True)
    title = Column(String)
    completed = Column(String)
    
Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionLocal()
    
    try:
        yield db
    finally:
        db.close()
        
        
# CRUD OPERATION 

# 1. CREATE API 

@app.post("/todos")
def create_todo(title:str , db:Session=Depends(get_db)):
    todo = Todo(title=title, completed = False)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        "message":"todo created",
        "data":todo
     }
    
    
    
#2. READ DATA API
@app.get("/todos")
def get_todo(db:Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return{
        "Total":len(todos),
        "Data":todos
    }
    
@app.get("/todos{todo_id}")
def get_todo(todo_id:int , db:Session=Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    
    if not todo:
        raise HTTPException(
            status_code=404,
            detail="todo not found"
        )
    return todo

#3. UPDATE API

@app.put("/todos{todo_id}")
def update_todo(todo_id:int , title:str , completed=str ,   db:Session=Depends(get_db)):
    todo= db.query(Todo).filter(Todo.id==todo_id).first()
    
    if not todo:
            raise HTTPException(
                status_code=404,
                detail="todo not found"
            )
    todo.title=title
    todo.completed = completed
    db.commit()
    db.refresh(todo)
    return{
        "message":"data updated",
        "data":todo
    } 
    
    
#4. DELETE

@app.delete("/todos{todo_id}")
def delete_todo(todo_id:int , db:Session=Depends(get_db)):
    todo= db.query(Todo).filter(Todo.id==todo_id).first()   
    if not todo:
            raise HTTPException(
                status_code=404,
                detail="todo not found"
            )
    db.delete(todo)
    db.commit()
    
    
    return{
        "message":"deleted",
        "data":todo
    } 