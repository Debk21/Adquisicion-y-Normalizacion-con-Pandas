import pandas as pd

transacciones = pd.read_csv('Datos/transacciones.csv')
productos = pd.read_excel('Datos/productos.xlsx')

transacciones["fecha"] = pd.to_datetime(transacciones["fecha"])   

print(transacciones)
print(transacciones.dtypes)
print(productos)

print(transacciones.isnull().sum())
print(productos.isnull().sum())

#Merge datos
datos_finales = pd.merge(
    transacciones,
    productos,
    on="id_producto",
    how="left"
)
print(datos_finales)

#crear total_venta
datos_finales["total_venta"] = (
    datos_finales["cantidad"] * datos_finales["precio_unitario"]
)

print(datos_finales)

datos_finales.to_parquet("resultados.parquet", index=False)