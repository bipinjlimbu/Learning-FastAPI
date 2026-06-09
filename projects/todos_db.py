from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends

DATABASE_URL = "sqlite:///./todos.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class TodoItem(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    completed = Column(String)
    
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
app = FastAPI()

@app.post("/todos")
def create_todo(title: str, completed: str = "false", db: Session = Depends(get_db)):
    todo = TodoItem(title=title, completed=completed)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
        "message": "Todo item created successfully",
        "data": todo
    }
    
@app.get("/todos")
def read_todos(db: Session = Depends(get_db)):
    todos = db.query(TodoItem).all()
    return {
        "todos": todos
    }
