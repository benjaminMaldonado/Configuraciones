
# Terminal de Linux
---

## Sobre la terminal
Esta es la terminal de linux que utilizo en windows 11.
Son dos aplicaciones de la ****Microsoft Store***.
Ademas de los paquetes instalados en para la terminal de linux.

![La Terminal](.mi-terminal.png) 

### Microsoft Store
Las dos aplicaciones estan disponibles tanto para windows 10 como para
windows 11.

+ Ubuntu 20.04
+ Windows Terminal

La **Windows Terminal** puede ser configurada aprate en la misma aplicación.
En mi caso solo se configuro el tamaño de la fuente y poco más.

### Paquetes
Todos los paquetes fuerosn instalados con ***apt***.
Se especifica un listado de todos en el archivo de *instalaciones.txt*

Algo importante a destacar es que **nautilus** instala un explorador de
archivos aparte del de windows.
La configuración de ***neovim*** esta en otra rama.

## NeoVim
Mi editor de codigo es ***neovim***.
Los archivos de configuración estan en la carpeta **neovim**
, se coloca en el directorio /home/user/.config/nvim.

Se necesita de instalar [vim plug](https://github.com/junegunn/vim-plug) para que funcionen los plugins.
Crear el directorio ***plugger*** dentro del directorio nvim. Y
ejecutar :PlugInstall.

El plugin *coc* es para lenguajes de programación.
Se configura en *coc.vim*, y los lenguajes se configuran en *coc-settings.json*.
Se debe de ejecutar los siguientes comandos.
~~~
:CocInstall coc-pyright
:CocInstall coc-json
:CocInstall coc-tsserver
:CocInstall coc-css
:CocInstall coc-httml
~~~

