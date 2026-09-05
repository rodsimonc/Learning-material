"""
Backend SQL de 0: FastAPI + SQLAlchemy + SQLite.
CRUD de 'tareas'. Mismo codigo anda con Postgres cambiando solo la URL.
"""
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, String, Integer, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

# --- Conexion ---
# SQLite para desarrollo. En produccion se cambia por:
# DATABASE_URL = "postgresql+psycopg://usuario:pass@host:5432/basededatos"
DATABASE_URL = "sqlite:///./tareas.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


class Base(DeclarativeBase):
    pass


# --- Modelo = tabla ---
class Tarea(Base):
    __tablename__ = "tareas"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    titulo: Mapped[str] = mapped_column(String(200))
    hecha: Mapped[bool] = mapped_column(Boolean, default=False)


Base.metadata.create_all(engine)  # crea la tabla si no existe


# --- Esquemas de entrada/salida (Pydantic) ---
class TareaIn(BaseModel):
    titulo: str
    hecha: bool = False


class TareaOut(TareaIn):
    id: int


def db():
    with Session(engine) as s:
        yield s


app = FastAPI(title="Backend SQL demo")


@app.post("/tareas", response_model=TareaOut)
def crear(t: TareaIn, s: Session = Depends(db)):
    fila = Tarea(titulo=t.titulo, hecha=t.hecha)
    s.add(fila)
    s.commit()
    s.refresh(fila)
    return TareaOut(id=fila.id, titulo=fila.titulo, hecha=fila.hecha)


@app.get("/tareas", response_model=list[TareaOut])
def listar(s: Session = Depends(db)):
    return [TareaOut(id=f.id, titulo=f.titulo, hecha=f.hecha)
            for f in s.query(Tarea).all()]


@app.get("/tareas/{tid}", response_model=TareaOut)
def ver(tid: int, s: Session = Depends(db)):
    f = s.get(Tarea, tid)
    if not f:
        raise HTTPException(404, "no existe")
    return TareaOut(id=f.id, titulo=f.titulo, hecha=f.hecha)


@app.put("/tareas/{tid}", response_model=TareaOut)
def actualizar(tid: int, t: TareaIn, s: Session = Depends(db)):
    f = s.get(Tarea, tid)
    if not f:
        raise HTTPException(404, "no existe")
    f.titulo, f.hecha = t.titulo, t.hecha
    s.commit()
    s.refresh(f)
    return TareaOut(id=f.id, titulo=f.titulo, hecha=f.hecha)


@app.delete("/tareas/{tid}")
def borrar(tid: int, s: Session = Depends(db)):
    f = s.get(Tarea, tid)
    if not f:
        raise HTTPException(404, "no existe")
    s.delete(f)
    s.commit()
    return {"borrada": tid}
