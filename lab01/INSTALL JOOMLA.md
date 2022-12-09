# DEBIAN 11 bullseye https://packages.debian.org/

## INSTALAR STACK LAMP
`sudo apt install apache2 mariadb-server php7.4 libapache2-mod-php7.4 php-mysql php7.4-cli unzip -y`

## INSTALAR EXTENSIONES PHP QUE USA JOOMLA
`sudo apt install openssl php7.4-xml php7.4-zip php7.4-mbstring php7.4-json php-imagick php-common php7.4-curl php7.4-gd php7.4-imap php7.4-intl php7.4-ldap php-ssh2 php7.4-sqlite3 php-gd -y`

## ASEGURAR INSTALACION MYSQL
`sudo mysql_secure_installation` 

Enter current password for root (enter for none): ENTER
Switch to unix_socket authentication [Y/n] N
Change the root password? [Y/n] N
Remove anonymous users? [Y/N] Y
Disallow root login remotely? [Y/N] Y
Remove test database and access to it? [Y/N] Y
Reload privilege tables now? [Y/N] Y

## CREAR USUARIO Y BASE DE DATOS Y ASIGNAR PRIVILEGIOS
`
CREATE DATABASE joomla_db;
CREATE USER "joomla_user"@"localhost" IDENTIFIED BY "joomla123";
GRANT ALL PRIVILEGES ON joomla_db.* TO "joomla_user"@"localhost";
FLUSH PRIVILEGES;
`

## CREAR DIRECTORIO PARA JOMLA
`sudo mkdir /var/www/html/joomla`

## DESCARGAR JOOMLA
`sudo wget https://downloads.joomla.org/cms/joomla4/4-0-4/Joomla_4.0.4-Stable-Full_Package.zip`

## DESCOMPRIMIR JOOMLA
`sudo unzip Joomla_4.0.4-Stable-Full_Package.zip -d /var/www/html/joomla`

## CAMBIAR USUARIO Y GRUPO PROPIETARIO | CAMBIAR PERMISOS
`
sudo chown -R www-data:www-data /var/www/html/joomla
sudo chmod -R 755 /var/www/html/joomla
sudo ls -l
`

## CREAR VIRTUALHOST
sudo vi /etc/apache2/sites-available/joomla.conf
<VirtualHost *:80>
     ServerName localhost
     DocumentRoot /var/www/html/joomla/
     
     <Directory /var/www/html/joomla/>
            Options FollowSymlinks
            AllowOverride All
            Require all granted
     </Directory>

     ErrorLog ${APACHE_LOG_DIR}/error.log
     CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

## HABILITAR VIRTUALHOST Y HABILITAR MODULO REWRITE
sudo a2ensite joomla.conf
sudo a2enmod rewrite

## REINICIAR APACHE
sudo systemctl restart apache2

## CONFIGURAR JOOMLA | INTERFAZ WEB
http://192.168.33.31/joomla

### Nombre de su sitio Joomla
`Blog de Prueba`

### Nombre de usuario para su cuenta de súper administrador.
`root`

### Nombre de usuario para su cuenta de superusuario. usada para login http://192.168.33.9/joomla/administrator
`admin`

### Contraseña de la cuenta del súper administrador
`admin@123456`

### Dirección de correo electrónico. del súper administrador
`admin@gmail.com`

### No se pudo eliminar el directorio "installation". Elimínelo manualmente.
`sudo rm -rf /var/www/html/joomla/installation`


