# Proyecto Integrador (pesca)

## Descripción del proyecto
Aplicación de interfaz gráfica desarrollada con Python y KivyMD. Actualmente incluye las pantallas de Inicio, Registro, Login, Home, Perfil y Programadores, con navegación entre ellas y una paleta de colores oliva. Los formularios son demostrativos: por ahora no guardan ni validan usuarios. La temática definitiva y la estructura de la base de datos quedan pendientes.

## Dependencias e instalación
Se necesita Python y KivyMD 2.0.0. Desde una terminal abierta en la carpeta del proyecto, instalar KivyMD con:

```shell
python -m pip install kivymd==2.0.0
```

## Cómo levantar el proyecto
1. Abrir una terminal en la carpeta del proyecto, donde se encuentra `app.py`.
2. Ejecutar la aplicación con:

```shell
python app.py
```

## Estructura de archivos
```text
Proyecto_Integrado_Oliva/
├── app.py
├── README.md
├── bd/
├── clases/
├── home/
│   ├── home.py
│   └── home.kv
├── images/
│   ├── avatar.png
│   ├── foto1.jpeg
│   ├── foto2.jpeg
│   ├── foto3.jpeg
│   └── foto4.jpeg
├── inicio/
│   ├── inicio.py
│   └── inicio.kv
├── login/
│   ├── login.py
│   └── login.kv
├── perfil/
│   ├── perfil.py
│   └── perfil.kv
├── programadores/
│   ├── programadores.py
│   └── programadores.kv
└── registro/
    ├── registro.py
    └── registro.kv
```

## Estructura de la base de datos
Pendiente de definir cuando se establezca la temática y el conjunto de datos del sistema.

## Integrantes, materia y división
- Santiago Andrés Franco Beyoglonian
- Facundo Javier Graña
- Lucas Mateo Marzovilla
- Julián Ignacio Caizos

**Materia:** Taller de Programación  
**Curso:** 4to B Informática
