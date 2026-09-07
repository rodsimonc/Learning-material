import { View, Text, Pressable, StyleSheet } from "react-native";
import type { Producto } from "../tipos";

interface Props {
  producto: Producto;
  onAgregar: (p: Producto) => void;
}

export function TarjetaProducto({ producto, onAgregar }: Props) {
  return (
    <View style={estilos.tarjeta}>
      <Text style={estilos.cat}>{producto.categoria}</Text>
      <Text style={estilos.nombre}>{producto.nombre}</Text>
      <Text style={estilos.precio}>${producto.precio}</Text>
      <Pressable style={estilos.boton} onPress={() => onAgregar(producto)}>
        <Text style={estilos.botonTexto}>Agregar</Text>
      </Pressable>
    </View>
  );
}

const estilos = StyleSheet.create({
  tarjeta: { backgroundColor: "#fff", borderRadius: 12, padding: 16, marginBottom: 12 },
  cat: { fontSize: 12, color: "#8a96a3", textTransform: "uppercase" },
  nombre: { fontSize: 16, fontWeight: "700", color: "#1c2430", marginVertical: 4 },
  precio: { fontSize: 15, fontWeight: "700", color: "#0d6b6b", marginBottom: 8 },
  boton: { backgroundColor: "#c0392b", borderRadius: 8, padding: 10, alignItems: "center" },
  botonTexto: { color: "#fff", fontWeight: "600" },
});
