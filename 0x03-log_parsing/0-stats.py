#!/usr/bin/python3
"""
A script for parsing HTTP request logs.
"""
import sys
import re


def extract_input(input_line):
    """
    Extracts sections of a line of an HTTP request log.
    """
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    resp_match = re.fullmatch(log_fmt, input_line)
    if resp_match is not None:
        return {
            'status_code': resp_match.group('status_code'),
            'file_size': int(resp_match.group('file_size'))
        }
    return None


def print_statistics(total_file_size, status_codes_stats):
    """
    Prints the accumulated statistics of the HTTP request log.
    """
    print('File size: {:d}'.format(total_file_size))
    for status_code in sorted(status_codes_stats.keys()):
        if status_codes_stats[status_code] > 0:
            print('{}: {}'.format(status_code,
                  status_codes_stats[status_code]))


def run():
    """
    Starts the log parser.
    """
    total_file_size = 0
    status_codes_stats = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_info = extract_input(line.strip())
            if line_info:
                total_file_size += line_info['file_size']
                if line_info['status_code'] in status_codes_stats:
                    status_codes_stats[line_info['status_code']] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except KeyboardInterrupt:
        pass
    finally:
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()
