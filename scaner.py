#!/usr/bin/env python

import nmap
import difflib
import smtplib as smtp
import os
import time

# Адрес сервера для сканування
server_address = 'type IP'

# Параметри сканування Nmap
nmap_args = '-O -oN nmap_report.txt'

# Параметри SMTP-сервера і облікового запису відправника
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'example@gmail.com'
sender_password = 'type your password'

# Адрес і ім'я отримувача
recipient_email = 'example@gmail.com'
recipient_name = 'Name'

while True:
    try:
        # Виконуємо сканування Nmap
        nm = nmap.PortScanner()
        nm.scan(hosts=server_address, arguments=nmap_args)

        # Отримуємо попередні результати сканування з файлу
        if os.path.exists('nmap_result.txt'):
            with open('nmap_result.txt', 'r') as f:
                old_result = f.read().splitlines()
        else:
            old_result = []

        # Отримуємо нові результати сканування та зберігаємо їх в файл
        with open('nmap_report.txt', 'r') as f:
            new_result = f.read().splitlines()

        with open('nmap_result.txt', 'w') as f:
            f.write('\n'.join(new_result))

        # Знаходимо критичні зміни
        critical_changes = set()
        for port in set(new_result).difference(set(old_result)):
            if 'open' in port:
                critical_changes.add(port)

        # Перевіряємо, чи є критичні зміни
        if critical_changes:
            message = f'Warning, {recipient_name}!\n\n'
            message += 'Critical changes:\n\n'
            message += '\n'.join(critical_changes)
            message += '\n\nOld result:\n\n'
            message += '\n'.join(old_result)
            message += '\n\nNew result:\n\n'
            message += '\n'.join(new_result)

            # Надсилаємо повідомлення електронною поштою
            with smtp.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, recipient_email, message.encode('utf-8'))

        else:
            print("Результати сканування не змінилися")

    except Exception as e:
        print(f"Сталася помилка: {e}")

    # Затримка в секундах перед наступним скануванням
    time.sleep(60)