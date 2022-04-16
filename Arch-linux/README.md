
# Configuracion de Arch Linux

## Listado de instalaciones en pacstrap
Estas son las instalaciones realizadas durante la instalación de arch linux.
+ base
+ base-devel
+ linux
+ linux-firmware
+ networkmanager
+ grub
+ efibootmgr
+ os-prober

Se debe de activar ***os-prober***, se debe modificar el archivo /etc/default/grub y colocar al final.
~~~
GRUB_DISABLE_OS_PROBER=false
~~~

## Internet
Para usar networkmanager se debe primero de habilitar.
~~~
systemctl enable NetworkManager

nmcli d
nmcli r wifi on
nmcli d wifi list
nmcli d wifi connect nombre_wifi password contraseña
~~~

## Sistema
Listado de instalaciones para que funcione el entorno grafico.
+ xf86-input-synaptics
+ lightdm
+ lightdm-gtk-greeter
+ mesa
+ xorg
+ qtile
Para que funcione el touchpath de las laptos se instala ###xf86-input-synaptics###.

Para el entorno grafico se usa ***mesa y xorg***. ***xorg*** tiene conflicto con la distribución de teclado, se debe ejecutar el siguiente comando en la terminal de arch.
~~~
localectl set-keymap --no-convert la-latin1
~~~

### Activar ligthdm
Para que funcione debe ser activado e iniciado.
~~~
systemctl enable lightdm.service
systemctl start ligthdm.service
~~~

### Fuente
Para instalar la fuente instalar ***yay*** primero.
~~~
yay -S nerd-fonts-ubuntu-mono
sudo pacman -S ttf-dejavu ttf-liberation noto-fonts
~~~

## QTILE
Ahora viene la configuración de ***qtile***. Primero el listado de programas que estan ligados a la configuración.
+ rofi

Para usarl la configuración se debe de remplazar los archivos de configuración.
En la ruta /home/user/.config/qtile remplazar el archivo ***config.py***.

El tema de rofi es android_notification no razi.
Para que funcione la opacidad se instala picom y se ejecuta el comando picom &
## Audio
Se debe instalar pulseaudio y pavucontrol y con el ultimo actvar el audio, de debe reiniciar.

## Alacritty
La configuracion de la terminal esta en el archivo alacratty.yml 
Primero en .config crear el directorio alacratty. Luego colocar el archivo de configuracion en el directorio recien creado.

Para que funcione la opacidad se debe instalar ***picom***. Y para activar activar.
~~~
picom &
~~~

## Fondo de pantalla
Es necesario instalar feh. Y ejecutar.
~~~
feh --bg-scale 'ruta'
~~~
# Comandos al iniciar sesión
Para no tener que repetir los comandos cada vez que se inicia sesión.
Instalar ***xorg-xinit***. Y crear el archivo **~/*.xprofile*** en la carpeta de usuario.

