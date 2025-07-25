# USO DE HERRAMIENTAS DE VIRTUALIZACIÓN Y CONTENEDORES DOCKER, PARA LA CREACIÓN DE ENTORNOS DE DESARROLLO PORTABLES, CONSISTENTES Y REPRODUCIBLES.
[Sustentacion Proyecto Aplicado](https://www.youtube.com/watch?v=SSEYC4Vh-mA)

[Presentación](https://drive.google.com/file/d/10eiwWyhOTNXFOU4qXh9CvCAx2_DSC_au/view)

[https://repository.unad.edu.co/handle/10596/59287](https://repository.unad.edu.co/handle/10596/59287)

### Multiplataforma: 
![Linux](https://img.shields.io/badge/-Linux-red?logo=linux) ![Windows](https://img.shields.io/badge/-Windows-blue?logo=windows) ![OSX](https://img.shields.io/badge/-OSX-black?logo=apple)

### Dependencias:
- ![Git](https://img.shields.io/badge/Git-latest-green?logo=git)
- ![Git](https://img.shields.io/badge/Virtualbox-v6.1.26-green?logo=virtualbox)
- ![Git](https://img.shields.io/badge/Vagrant-v2.2.19-green?logo=vagrant)


### Modo de uso:
Clone el reposoitorio.

```bash
git clone https://github.com/nullx5/proyecto.git
```

![https://i.imgur.com/zv9Q4Fh.png](https://i.imgur.com/zv9Q4Fh.png)

Muevase al directorio del laboratorio que desea probar e inicie la maquina.

```bash
vagrant up
```
Ingrese a la maquina.

```bash
vagrant ssh
```

Apagar la maquina.

```bash
vagrant halt
```

> ### `Lab01`
- Simple Pila LAMP sobre `Vagrant`.
<img src="https://i.imgur.com/1y6zDiz.png" alt="lab01" style="width:400px;"/>

> ### `Lab02`
- CMS Wordpress y Base de Datos Mysql Sobre Red `Docker`.
<img src="https://i.imgur.com/6Mxuzhy.png" alt="lab02" style="width:400px;"/>

> ### `Lab03`
- Django Framework Web y Base de Datos Postgresql sobre Red `docker-compose`.
<img src="https://i.imgur.com/gSt3BbW.png" alt="lab03" style="width:400px;"/>

> ### `Lab04`
- OWASP Juice Shop: Insecure web application Sobre Red `Docker`.
<img src="https://i.imgur.com/bXy9d5j.png" alt="lab04" style="width:400px;"/>

> ### `Lab05`
- PhpIPAM – Open source IP address management `Docker`.
<img src="https://i.imgur.com/os28UjY.png" alt="lab04" style="width:400px;"/>

### Paquete docker compose
> [!NOTE]
> El paquete `docker-compose` ha quedado obsoleto, usar `docker-compose-v2`
> Usar `sudo docker compose up -d` en lugar de `sudo docker-compose up -d`

### Crear snapshot en Vagrant:

> [!NOTE]
> Recuerda que necesitarás tener la máquina virtual en estado "apagado" si quieres hacer algunos tipos de snapshots.

```
vagrant snapshot save nombre_del_snapshot

vagrant snapshot list

vagrant snapshot restore nombre_del_snapshot

vagrant snapshot delete  nombre_del_snapshot

```



### Solución de Problemas en Linux:
> [!WARNING]
> Si no reconoce la configuración de red, crear el archivo `networks.conf` con el segmento de red asignado en los laboratorios.

```
sudo nvim /etc/vbox/networks.conf
       * 192.168.33.0/24
```
> [!CAUTION] 
> Si da error `"The vboxdrv kernel module is not loaded."`
Falta Oracle VM VirtualBox Support Driver `vboxdrv`
```
Desabilitar secure boot en la BIOS
Desinstalar todos los paquetes libvirt
sudo apt install --reinstall linux-headers-$(uname -r) dkms
sudo init 6
sudo modprobe vboxdrv
sudo apt install --reinstall virtualbox-dkms
sudo lsmod |grep vboxdrv
sudo modinfo vboxdrv
sudo /sbin/vboxconfig
sudo locate vboxdrv

sudo vagrant up
```

[error modprove vboxdrv](https://www.youtube.com/watch?v=kqS8ss-OQzI)

Referencias:
- [docker 1](https://www.youtube.com/watch?v=CzMo4hJvY0g)
- [docker 2](https://www.youtube.com/watch?v=KAdtnhk9WT0)
- [CI/CD Github actions](https://www.youtube.com/watch?v=qM6ZkufsHGc)
- https://bootcamp.295devops.com/
- https://labs.iximiuz.com/playgrounds
- https://killercoda.com/playgrounds/
- https://labs.play-with-docker.com/
- https://github.com/wagoodman/dive
- https://github.com/jesseduffield/lazydocker
