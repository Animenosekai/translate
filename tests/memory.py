import os
import psutil
import sys
import traceback

PROCESS = psutil.Process(os.getpid())
MEGA = 10 ** 6
MEGA_STR = ' ' * MEGA


def main():
    try:
        print_memory_usage()
        alloc_max_str()
        alloc_max_array()
    except MemoryError as error:
        # Output expected MemoryErrors.
        log_exception(error)
    except Exception as exception:
        # Output unexpected Exceptions.
        log_exception(exception, False)


def alloc_max_array():
    """Allocates memory for maximum array.
    See: https://stackoverflow.com/a/15495136

    :return: None
    """
    collection = []
    while True:
        try:
            collection.append(MEGA_STR)
        except MemoryError as error:
            # Output expected MemoryErrors.
            log_exception(error)
            break
        except Exception as exception:
            # Output unexpected Exceptions.
            log_exception(exception, False)
    print('Maximum array size:', len(collection) * 10)
    print_memory_usage()


def alloc_max_str():
    """Allocates memory for maximum string.
    See: https://stackoverflow.com/a/15495136

    :return: None
    """
    i = 0
    while True:
        try:
            a = ' ' * (i * 10 * MEGA)
            del a
        except MemoryError as error:
            # Output expected MemoryErrors.
            log_exception(error)
            break
        except Exception as exception:
            # Output unexpected Exceptions.
            log_exception(exception, False)
        i += 1
    max_i = i - 1
    print('Maximum string size:', (max_i * 10 * MEGA))
    print_memory_usage()


def log_exception(exception: BaseException, expected: bool = True):
    """Prints the passed BaseException to the console, including traceback.

    :param exception: The BaseException to output.
    :param expected: Determines if BaseException was expected.
    """
    output = "[{}] {}: {}".format('EXPECTED' if expected else 'UNEXPECTED', type(exception).__name__, exception)
    print(output)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback)


def print_memory_usage():
    """Prints current memory usage stats.
    See: https://stackoverflow.com/a/15495136

    :return: None
    """
    total, available, percent, used, free, active, inactive, wired = psutil.virtual_memory()
    total, available, used, free = total / MEGA, available / MEGA, used / MEGA, free / MEGA
    proc = PROCESS.memory_info()[1] / MEGA
    print('process = %s total = %s available = %s used = %s free = %s percent = %s'
          % (proc, total, available, used, free, percent))


if __name__ == "__main__":
    main()