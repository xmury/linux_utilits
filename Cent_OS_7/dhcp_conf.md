#Настройка DHCP

Установка dhcpd - **yum install dhcp**

---
! - В файлах настроек сети подключаемых машин должен быть указан: **BOOTROTO=dhcp**

! - systemctl enable    dhcpd   | Автозапуск
              start             | Запуск
              restart           | Перезагрузка
              stop              | Отключение
---

##Файл конфигурации dhcp: **/etc/dhcp/dhcpd.conf

###Структура
    ---
    Настройки для всех подсетей

    log-facility local7;                                        | ERROR_I_XZ
    ---

    subnet 192.168.1.0 netmask 255.255.255.0 {                  | Указание IP  и Маски сети 
        range 192.168.1.10 192.168.1.100;                       | Диапазон выдаваемых       
        option domain-name-servers 8.8.8.8 , 8.8.4.4;           | DNS сервера     
        option domain-name "my_domain";                         | ERROR_I_XZ
        option routers 192.168.1.1;                             | Шлюз 

        default-lease-time 600;                                 | Время выделения IP (в секундах)  ERROR_I_DOUBT
        max-lease-time 4200;                                    | Максимальное время выделения IP  ERROR_I_DOUBT
    }

