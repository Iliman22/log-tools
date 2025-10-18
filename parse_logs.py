import sys
from collections import Counter

def parse_log(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    total_lines = len(lines)
    errors = [line for line in lines if "ERROR" in line]
    warnings = [line for line in lines if "WARNING" in line]

    print(f"Total lines: {total_lines}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    # Считаем IP-адреса (простая проверка: точка 3 раза)
    ips = [word for line in lines for word in line.split() if word.count('.') == 3]
    top_ips = Counter(ips).most_common(5)

    print("\nTop 5 IP addresses:")
    for ip, count in top_ips:
        print(f"{ip}: {count}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parser.py <logfile>")
        sys.exit(1)

    log_file = sys.argv[1]
    parse_log(log_file)
