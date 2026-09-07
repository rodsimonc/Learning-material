import { FlatList, View, Text, StyleSheet } from "react-native";
import { CATALOGO } from "./datos";
import { useCarrito } from "./useCarrito";        // el mismo hook del librito 15
import { TarjetaProducto } from "./TarjetaProducto";

export default function App() {
  const { agregar, total } = useCarrito();
  return (
    <View style={estilos.app}>
      <Text style={estilos.titulo}>Sabores del Barrio</Text>
      <FlatList
        data={CATALOGO}
        keyExtractor={(p) => String(p.id)}
        renderItem={({ item }) => (
          <TarjetaProducto producto={item} onAgregar={agregar} />
        )}
      />
      <Text style={estilos.total}>Total: ${total}</Text>
    </View>
  );
}

const estilos = StyleSheet.create({
  app: { flex: 1, padding: 16, paddingTop: 60, backgroundColor: "#f4f6f8" },
  titulo: { fontSize: 22, fontWeight: "800", color: "#c0392b", marginBottom: 16 },
  total: { fontSize: 18, fontWeight: "800", marginTop: 12 },
});
