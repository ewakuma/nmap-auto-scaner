import time
from nmap_scanner import run_nmap_scan
from email_sender import send_email

# Параметри сканування Nmap
server_address = 'type IP'
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
        critical_changes, old_result, new_result = run_nmap_scan(server_address, nmap_args)

        if critical_changes:
            message = f'Warning, {recipient_name}!\n\n'
            message += 'Critical changes:\n\n'
            message += '\n'.join(critical_changes)
            message += '\n\nOld result:\n\n'
            message += '\n'.join(old_result)
            message += '\n\nNew result:\n\n'
            message += '\n'.join(new_result)

            send_email(smtp_server, smtp_port, sender_email, sender_password, recipient_email, recipient_name, message)
        else:
            print("Результати сканування не змінилися")

    except Exception as e:
        print(f"Сталася помилка: {e}")

    # Затримка в секундах перед наступним скануванням
    time.sleep(60)
