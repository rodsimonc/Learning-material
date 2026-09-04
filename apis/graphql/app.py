import strawberry
from strawberry.fastapi import GraphQLRouter
from fastapi import FastAPI
from typing import List

@strawberry.type
class Item:
    producto: str
    cantidad: int

@strawberry.type
class Pedido:
    fecha: str
    items: List[Item]

@strawberry.type
class Usuario:
    nombre: str
    pedidos: List[Pedido]

@strawberry.type
class Query:
    @strawberry.field
    def usuario(self, id: int) -> Usuario:
        return Usuario(
            nombre="Carlos",
            pedidos=[Pedido(fecha="2026-08-01", items=[Item(producto="Teclado", cantidad=1)])],
        )

schema = strawberry.Schema(Query)
app = FastAPI()
app.include_router(GraphQLRouter(schema), prefix="/graphql")
