Настройка DHCP
==============

*Установка dhcp - **yum install dhcp***



- В файлах настроек сети подключаемых машин должен быть указан: **BOOTROTO=dhcp**

- systemctl enable    dhcpd   | Автозапуск
            start             | Запуск
            restart           | Перезагрузка
            stop              | Отключение
    


Настройка файла конфигурации
----------------------------

Файл конфигурации dhcp: **/etc/dhcp/dhcpd.conf**

**Структура**

```
option domain-name-servers 10.10.10.1 , 10.11.25.12      | DNS сервера                 [Внешний]
log-facility local7;                                     | ERROR_I_XZ
  
subnet 192.168.1.0 netmask 255.255.255.0 {               | Указание IP  и Маски сети 
  range 192.168.1.10 192.168.1.100;                      | Диапазон выдаваемых       
  option domain-name-servers 8.8.8.8 , 8.8.4.4;          | DNS сервера                 [Внутренний]  
  option domain-name "my_domain";                        | ERROR_I_XZ
  option routers 192.168.1.1;                            | Шлюз 
       
  default-lease-time 600;                                | Время выделения IP (в секундах)  ERROR_I_DOUBT
  max-lease-time 4200;                                   | Максимальное время выделения IP  ERROR_I_DOUBT
}
```
- P.S   *option* указанные вне **subnet** являются общими для всех subnet-ов. 
- Р.P.S Если в **subnet** указаны одни параметры а вне его другие для одного **option**,
        то внешний option заменяется внутренним

Указание порта раздачи IP
-------------------------
```
cp /usr/lib/systemd/system/dhcpd.service /etc/systemd/system/
vi /etc/systemd/system/dhcpd.service
    ExecStart=/usr/sbin/dhcpd -f -cf /etc/dhcp/dhcpd.conf        | Это одна строка
    -user dhcpd -group dhcpd --no-pid <your_interface_name(s)>   | Нужно вместо <your_interface_name(s)>
                                                                 | написать имя порта раздачи. Без <> 
systemctl --system daemon-reload
systemctl restart dhcpd.service
```


Настройка firewall с iptables ERROR_HARDCOR
-------------------------------------------
```
systemctl stop firewalld
systemctl disable firewalld

yum -y install iptables-services

systemctl enable iptables.service
systemctl start iptables.service

iptables -F
iptables -t nat -A POSTROUTING -s 192.10.0/24 -o enp0s3 -j MASQUERADE       | ERROR_I_DOUBT

vi /etc/sysctl.conf
    net.ipv4.ip_forward=1            

iptables-save > /etc/sysconfig/iptables
```
