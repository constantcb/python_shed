file_path = ''
open_mode = 'r'
open_encoding = 'utf-8'

print_from = ''
print_to = ''


def end_limit(line, found_end):
    if not print_to == '' and print_to in line and not found_end:
        return True


def start_limit(line, found_start):
    if not print_from == '' and print_from in line and not found_start:
        return True


def format_link_header(found_start, found_end, line, lst):
    if found_start and not found_end and line.startswith('#'):
        split = line.removesuffix('\n').split(" ", 1)
        replaced = split[1].replace(" ", "-")
        lst.append('[' + split[1].replace("-", " ") + '](#' + replaced.lower() + ')')


def format_list(elements):
    for i in elements:
        print('%-12s' % i)


def get_links():
    f = open(file_path, mode=open_mode, encoding=open_encoding)

    found_start = False
    found_end = False
    lst = list()

    for line in f:
        found_end = end_limit(line, found_end)
        format_link_header(found_start, found_end, line, lst)
        found_start = start_limit(line, found_start)

    else:
        print(lst)
    format_list(lst)


if __name__ == '__main__':
    get_links()
