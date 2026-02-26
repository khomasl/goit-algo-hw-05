import collections
from pathlib import Path
import sys


def parse_log_line(line: str) -> dict:
    log = {}
    log_line = line.split(' ')
    log["date"] = log_line[0]
    log["time"] = log_line[1]
    log["level"] = log_line[2].upper()
    log["info"] = ' '.join(log_line[3:])
    return log


def load_logs(file_path: str) -> list:
    absolute_path = Path(file_path)

    if not absolute_path.exists() or not absolute_path.is_file():
        print('Log file not found')
        return
    
    logs = []
    try:
        with open(absolute_path, 'r', encoding='utf-8') as fh:
            for line in fh.readlines():
                logs.append(parse_log_line(line.strip()))

        return logs
    except Exception as e:
        print(f'{e} with file')


def filter_logs_by_level(logs: list, level: str) -> list:
    # v1
    return list(filter(lambda log: log['level'] == level.upper(), logs))
    # v2
    # return [log for log in logs if log['level'] == level.upper()]


def count_logs_by_level(logs: list) -> dict:
    levels = [log['level'] for log in logs]
    return dict(collections.Counter(levels).most_common())


def display_log_counts(counts: dict):
    # space count after level
    def s_c(level: str) -> int:
        return 15 - len(level)
    
    print('Рівень логування | Кількість')
    print('-----------------|----------')

    for level in counts.keys():
        print(level, ' '*s_c(level), '|', counts[level])


def display_log_details(logs: list, level: str):
    def print_details(date, time, level, info):
        print(f"{date} {time} - {info}")

    filter_logs = filter_logs_by_level(logs, level) 
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for log in filter_logs:
        print_details(**log)

def main():
    logs = load_logs(sys.argv[1])
    if not logs: return
    
    # f.e. [{"INFO": 4}, {"DEBUG": 3},...]
    counts = count_logs_by_level(logs)

    display_log_counts(counts)
    
    if len(sys.argv) > 2:
        display_log_details(logs, sys.argv[2])


if __name__ == "__main__":
    main()
