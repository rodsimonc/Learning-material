# Track · Datos, de 0 a insights

Un track de análisis de datos, de no saber qué es un DataFrame a limpiar, explorar, visualizar y comunicar datos reales. El hilo conductor es un dataset de ventas de la tienda de alimentos (librito 13): 786 líneas de venta de 3 meses, ensuciadas a propósito para practicar la limpieza.

## Los 8 libritos
1. [Qué es el análisis de datos](01-que-es-el-analisis/) — el proceso, tipos de datos, tidy data. (Conceptual)
2. [Pandas de 0](02-pandas-de-0/) — DataFrame, cargar, seleccionar, filtrar, columnas calculadas. (Código probado)
3. [Limpieza de datos](03-limpieza-de-datos/) — nulos, duplicados, formatos, categorías. Genera `ventas_limpio.csv`. (Código probado)
4. [Análisis exploratorio (EDA)](04-analisis-exploratorio/) — groupby, tablas dinámicas, análisis temporal. (Código probado)
5. [Visualización](05-visualizacion/) — qué gráfico para qué, matplotlib, gráficos honestos. (Gráficos reales)
6. [SQL para análisis](06-sql-para-analisis/) — window functions, CTEs, pandas vs SQL. (Código probado)
7. [Estadística práctica](07-estadistica-practica/) — media/mediana, correlación y las trampas. (Código probado)
8. [BI y comunicar](08-bi-y-comunicar/) — Power BI, buenos dashboards, storytelling de datos. (Conceptual)

## El dataset
`datos/ventas.csv` (crudo, con errores) y `datos/ventas_limpio.csv` (después del librito 3). Cada librito de código trae su propio `ejemplos/` con el script, el dataset y la salida real.

## Correr los ejemplos
```
pip install pandas matplotlib
cd 02-pandas-de-0/ejemplos && python3 02_pandas.py
```

Recorrido: en orden. Cada librito construye sobre el anterior (el 3 limpia lo que el resto usa).
