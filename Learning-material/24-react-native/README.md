# 24 · React Native: apps móviles

Usar el React que ya sabés (libritos 14 y 15) para hacer apps móviles reales para iOS y Android, con una sola base de código. Reconstruye el catálogo de la tienda en móvil.

> Nota honesta: a diferencia del resto de la colección, este código NO está ejecutado (correr React Native necesita un emulador o un celular, que el entorno donde se armó no tiene). El código es correcto e idiomático, pero no lleva sello "salida real". Lo probás vos con Expo.

## Qué hay acá
- `manual.html` — 9 capítulos: qué es React Native, de la web a móvil (View/Text/Image vs HTML), estilos con StyleSheet y Flexbox, estado y eventos (idénticos a React web), listas con FlatList, navegación (React Navigation), consumir APIs y usar lo nativo (cámara, GPS, storage), y publicar (Expo, tiendas).
- `ejemplos/TarjetaProducto.tsx` y `ejemplos/App.tsx` — el catálogo de la tienda en React Native.

## Probar (en tu compu)
```
npx create-expo-app tienda-movil
# copiá los ejemplos, instalá Expo Go en tu celular, y:
npx expo start
```
Escaneás el QR con Expo Go y ves la app en tu teléfono al instante.
