# eBiblioteca

eBiblioteca es una aplicación de escritorio que gestión de URL que permite a los usuarios gestionar recursos educativos, cuentas de usuarios, y más.

## Características

- **Gestión de cuentas:** Crear, iniciar sesión y gestionar cuentas de usuario.
- **Recursos educativos:** Añadir, modificar y eliminar recursos de la biblioteca.
- **Interfaz de usuario amigable:** Interfaz desarrollada usando PyQt para una experiencia de usuario fluida.

## Estructura del Proyecto

- **controller/**: Contiene la lógica de negocio y manejo de datos.
  - `ControllerCreateAccount.py`
  - `ControllerLogin.py`
  - `ControllerResource.py`
  - `ControllerTeacher.py`

- **model/**: Manejo de la lógica de acceso a la base de datos.
  - `eBibliotecaCol.py`
  - `ResourceQueri.py`
  - `UserQueries.py`

- **view/**: Interfaz de usuario y componentes gráficos.
  - `createaccountUI/`
  - `loginUI/`
  - `resourceUI/`
  - `teacherUI/`

- **library.db**: Archivo de base de datos SQLite.

- **main.py**: Punto de entrada principal de la aplicación.

## Requisitos

- Python 3.8 o superior.
- PyQt5 o superior.

## Uso

Ejecuta la aplicación usando el archivo `main.py`:

```bash
python main.py
