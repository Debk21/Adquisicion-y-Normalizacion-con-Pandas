# Pre-entrega: Adquisición y Normalización con Pandas

## Descripción

En este proyecto realizo un proceso de adquisición, transformación y normalización de datos utilizando Python y Pandas.

Se utilizan dos fuentes de datos en diferentes formatos:

* Un archivo CSV con información de las transacciones.
* Un archivo Excel con información de los productos.

Ambas fuentes se integran mediante el campo `id_producto` y se genera una nueva columna calculada llamada `total_venta`.

El resultado final se exporta en formato Parquet.

---

## Estructura del proyecto

```text
Adquisicion-y-Normalizacion-con-Pandas/
│
├── Datos/
│   ├── transacciones.csv
│   └── productos.xlsx
│
├── adquisicion_normalizacion.py
├── resultado.parquet
└── README.md
```

### Archivos

**`Datos/transacciones.csv`**

Contiene la información de las transacciones:

* `id_transaccion`
* `id_cliente`
* `id_producto`
* `cantidad`
* `fecha`

**`Datos/productos.xlsx`**

Contiene la información del catálogo de productos:

* `id_producto`
* `nombre_producto`
* `categoria`
* `precio_unitario`

**`adquisicion_normalizacion.py`**

Contiene el código Python utilizado para realizar la adquisición, transformación, integración y normalización de los datos.

**`resultado.parquet`**

Contiene el dataset final luego de aplicar todas las transformaciones.

---

## Tecnologías y librerías utilizadas

* Python 3
* Pandas
* OpenPyXL
* PyArrow

### Instalación de librerías

Las librerías necesarias pueden instalarse mediante:

```bash
pip install pandas openpyxl pyarrow
```

---

## Proceso realizado

### 1. Adquisición de datos

Se cargan las dos fuentes de datos utilizando Pandas:

* `transacciones.csv` mediante `pd.read_csv()`.
* `productos.xlsx` mediante `pd.read_excel()`.

De esta forma se integran datos provenientes de dos formatos diferentes.

### 2. Transformación de datos

La columna `fecha` de las transacciones se convierte al tipo de dato datetime utilizando:

```python
transacciones["fecha"] = pd.to_datetime(transacciones["fecha"])
```

Esto permite trabajar correctamente con fechas y realizar posteriormente operaciones temporales sobre los datos.

### 3. Control de valores nulos

Se verifican los valores nulos de ambas fuentes mediante:

```python
transacciones.isnull().sum()
productos.isnull().sum()
```

No se encontraron valores nulos en los datos utilizados, por lo que no fue necesario realizar imputaciones ni eliminar registros.

### 4. Integración de las fuentes

Las tablas se integran utilizando `id_producto` como clave:

```python
datos_finales = pd.merge(
    transacciones,
    productos,
    on="id_producto",
    how="left"
)
```

Se utiliza un `left join` para conservar todas las transacciones y agregar la información correspondiente de los productos.

### 5. Columna calculada

Se crea la columna `total_venta` multiplicando la cantidad vendida por el precio unitario:

```python
datos_finales["total_venta"] = (
    datos_finales["cantidad"] * datos_finales["precio_unitario"]
)
```

Esta transformación permite obtener el importe total correspondiente a cada transacción.

### 6. Exportación

Finalmente, el dataset procesado se guarda en formato Parquet:

```python
datos_finales.to_parquet("resultado.parquet", index=False)
```

El resultado final contiene **16 registros y 9 columnas**.

---

## Reproducibilidad

Para ejecutar el proyecto localmente:

1. Clonar o descargar este repositorio.
2. Abrir una terminal dentro de la carpeta del proyecto.
3. Instalar las dependencias:

```bash
pip install pandas openpyxl pyarrow
```

4. Ejecutar el script:

```bash
python adquisicion_normalizacion.py
```

El proceso leerá los archivos ubicados en la carpeta `Datos`, realizará las transformaciones y generará nuevamente el archivo:

```text
resultado.parquet
```

---

## Resultado

El dataset final integra la información de las transacciones con el catálogo de productos y agrega la variable calculada:

```text
total_venta = cantidad × precio_unitario
```

El archivo final se encuentra disponible en formato **Parquet**, cumpliendo con el requisito de exportación de la actividad.
