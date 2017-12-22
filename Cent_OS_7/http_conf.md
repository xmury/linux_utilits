Настройка Сервера Apache
========================

*Установка Apache: **yum install http***
*Установка PHP: **yum install http***

/var/named/vm.zone
---------------
```
  site1   IN A    192.168.10.1                              | DNC имя нашего сайта
  ...
```
/etc/httpd/conf.d/
------------------
```
  cp /usr/share/doc/httpd-2.4.6/httpd-vhosts.conf site.conf | Сюда будем прописывать виртуальные порты  
      <VirtualHost *:80>                                    | Дефолтный порт для сервера
          DocumentRoot "/var/www/sits/site1"                | Местоположение index.php
          ServerName site1.vm.group                         | Адрес сайта
      </VirtualHost>
```

P.S Не забуть перезагрузить службу **named**
