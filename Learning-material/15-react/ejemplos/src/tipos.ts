// Los tipos del dominio (del librito 14). Un solo lugar que define la forma
// de los datos, y todo el resto de la app queda protegido.
export interface Producto {
  id: number;
  nombre: string;
  categoria: string;
  precio: number;
}

export interface ItemCarrito {
  producto: Producto;
  cantidad: number;
}
