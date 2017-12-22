Настройка DHCP
==============

Установка dhcp - **yum install dhcp**

---

- В файлах настроек сети подключаемых машин должен быть указан: **BOOTROTO=dhcp**

- systemctl enable    dhcpd   | Автозапуск
            start             | Запуск
            restart           | Перезагрузка
            stop              | Отключение
              

Настройка файла конфигурации
----------------------------

Файл конфигурации dhcp: **/etc/dhcp/dhcpd.conf**

**Структура**

option domain-name-servers 10.10.10.1 , 10.11.25.12       | DNS сервера                 [Внешний]
log-facility local7;                                      | ERROR_I_XZ
  
subnet 192.168.1.0 netmask 255.255.255.0 {                | Указание IP  и Маски сети 
  range 192.168.1.10 192.168.1.100;                       | Диапазон выдаваемых       
  option domain-name-servers 8.8.8.8 , 8.8.4.4;           | DNS сервера                 [Внутренний]  
  option domain-name "my_domain";                         | ERROR_I_XZ
  option routers 192.168.1.1;                             | Шлюз 
        
  default-lease-time 600;                                 | Время выделения IP (в секундах)  ERROR_I_DOUBT
  max-lease-time 4200;                                    | Максимальное время выделения IP  ERROR_I_DOUBT
}

- P.S   *option* указанные вне **subnet** являются общими для всех subnet-ов. 
- Р.P.S Если в **subnet** указаны одни параметры а вне его другие для одного **option**,
        то внешний option заменяется внутренним

Указание порта раздачи IP
-------------------------

1. cp /usr/lib/systemd/system/dhcpd.service /etc/systemd/system/
2. vi /etc/systemd/system/dhcpd.service
    ExecStart=/usr/sbin/dhcpd -f -cf /etc/dhcp/dhcpd.conf -user dhcpd       | Это одна строка
    -group dhcpd --no-pid <your_interface_name(s)>                          | Нужно просто вместо <your_interface_name(s)>
                                                                            | написать имя порта раздачи. Без <> 
3. systemctl --system daemon-reload
4. systemctl restart dhcpd.service


Настройка firewall с iptables ERROR_HARDCOR
-------------------------------------------

1. systemctl stop firewalld
2. systemctl disable firewalld

3. yum -y install iptables-serv ices

4. systemctl enable iptables.service
5. systemctl start iptables.service

6. iptables -F
7. iptables -t nat -A POSTROUTING -s 192.10.0/24 -o enp0s3 -j MASQUERADE       | ERROR_I_DOUBT

8. iptables-save > /etc/sysconfig/iptables
