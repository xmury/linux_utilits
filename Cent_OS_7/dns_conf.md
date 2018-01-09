Настройка DNS
=============

*Установка: **yum install bind bind-utils***


/etc/named.conf
---------------

Прописываем: 
```
    listen_on port 53 { 192.168.10.1; };   | Указываем IP принимающео шлюза
    <...>
    allow-query       { 192.168.10.0; };  | Разрешаем обращаться всем IP
    
    <...>                                 |
    
zone "vm.zone" IN {                       | Имя зоны
    type master;
    file "vm.zone";                       | Указываем имя файла с описанием зоным
};
```

/var/named/
-----------
```
    cp named.localhost vm.zone
        IN SOA @ srv.vm.org.              | /etc/hostname Не забывае про "." в конце
        <...>
        A                   192.168.10.1  | Шлюз
        <...>                             | После АААА
  srv   IN A                192.168.10.1  | Поддомен
  
    chown root:named vm.zone              | Даём доступ DNS к нашей зоне
