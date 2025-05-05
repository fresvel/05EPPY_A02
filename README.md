# 05EPPY_A01

## Instalación con make
- 1.- Crear un directorio base
- 2.- Crear un entorno virtual
- 3.- Instalar las herramientas necesarias
- 4.- Clonar el repositorio desde https://github.com/fresvel/05EPPY_A01
- 5.- Entrar en el directorio 05EPPY_A01
- 6.- Compilar
- 7.- Instalar 


```bash
pip install setuptools wheel build
git clone https://github.com/fresvel/05EPPY_A01
cd 05EPPY_A01
make build
make install
web_store
```
## Ejecución
Para iniciar la aplicación, ejecutar:

```bash
web_store
```
## Estructura


| Página                                      | URL                              |
|---------------------------------------------|----------------------------------|
| Página de inicio                            | localhost:8000/home             |
| Página de lista de productos                | localhost:8000/store            |
| Página de resumen de compras, dirección de envío y finalizar | localhost:8000/basket           |
| Página de transacción realizada con éxito   | localhost:8000/bought           |

## Detalles

Esta es una página web se prueba, no existe una base de datos en el backend. Para acceder
se puede usar cualquier usuario y contraseña.