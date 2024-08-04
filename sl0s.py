from subprocess import Popen, PIPE
import os


green_color = "\033[92m"
blue_color = "\033[94m"
reset_color = "\033[0m"

def start_scan(scanner, flags, url):
    result_separator = "\n********************************************************************************************************************************\n"
    output_filename = f"scan_results_{url.replace('https://', '').replace('http://', '')}.txt"
    
    if scanner == "wapiti":
        command = f"wapiti {flags} {url}"
    elif scanner == "nmap":
        command = f"nmap {flags} {url}"
    elif scanner == "nikto":
        command = f"nikto {flags} {url}"
    elif scanner == "dirsearch":
        command = f"dirsearch {flags} {url}"
    elif scanner == "sqlmap":
        command = f"sqlmap {flags} {url}"        
    else:	
        command = scanner, f" {flags} {url}"  
    
    if command:
        print(f"{green_color}Запуск {scanner} для {url} с флагами {flags}{reset_color}")
        process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        with open(output_filename, "a") as f:
            f.write(f"## Сканирование {scanner} для {url}\n")
            f.write(result_separator)
            f.write(stdout.decode("utf-8", errors="ignore"))
            f.write(stderr.decode("utf-8", errors="ignore"))
            f.write(result_separator)
        return process
    return None

def parse_and_execute(command, url):
    processes = []
    scanners = ['--wapiti', '--nmap', '--nikto', '--dirsearch', '--sqlmap', '--commix']
    
    
    output_filename = f"scan_results_{url.replace('https://', '').replace('http://', '')}.txt"
    if os.path.exists(output_filename):
        os.remove(output_filename)
    
    for scanner in scanners:
        if scanner in command:
            scanner_index = command.index(scanner)
            next_scanner_index = len(command)
            for next_scanner in scanners:
                if next_scanner in command[scanner_index + 1:]:
                    next_scanner_index = command.index(next_scanner, scanner_index + 1)
                    break
            flags = " ".join(command[scanner_index + 1:next_scanner_index])
            process = start_scan(scanner.strip('-'), flags, url)
            if process:
                processes.append(process)
    
  
    for process in processes:
        process.wait()
    
   
    print(f"{green_color}Все сканирования завершены. Открыть результаты? (y/n){reset_color}")
    if input().lower() == 'y':
        os.system(f"xdg-open {output_filename}")

def print_logo():
    logo = blue_color + """
  _____   _       _____     _____ 
 / ____| | |     / __  \   / ____|
| (___   | |    | |  /| | | (___  
 \___ \  | |    | | / | |  \___ \               by [imnoturbadboy | https://github.com/imnoturbadboy]
 ____) | | |___ | |/__| |  ____) |
|_____/  |_____| \_____/  |_____/
    
    """ + reset_color
    print(logo)

print_logo()
print(f"{green_color}Welcome to Simple List of Scanners!{reset_color}")

while True:
    command = input(f"{green_color}Введите команду (например, --nmap -sC -sV http://localhost:8080 или --nmap -sC -sV 192.168.1.1): {reset_color}")
    parts = command.split()
    
    if len(parts) < 3:
        print(f"{green_color}Некорректный ввод. Используйте формат: <флаг сканера> <флаги для сканера> <URL/IP>{reset_color}")
        continue
    
    
    url = None
    for part in parts:
        if part.startswith("http://") or part.startswith("https://") or part.count('.') == 3:
            url = part
            break
    
    if not url:
        print(f"{green_color}Некорректный URL/IP. Убедитесь, что он начинается с http:// или https:// или это корректный IP-адрес.{reset_color}")
        continue
    
    
    parts.remove(url)
    
   
    parse_and_execute(parts, url)
    
    
    print(f"{green_color}Желаете повторить? (y/n){reset_color}")
    answer = input().strip().lower()
    if answer == 'n':
        print(f"{green_color}Программа завершена. Bye-Bye^^{reset_color}")
        break
