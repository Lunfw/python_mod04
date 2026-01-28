from sys import stderr, stdout, exit


def crisis_response_protocol() -> None:
    '''
        #   Opens and reads a file through stdout.
    '''
    temp: tuple[str] = (
        'lost_archive.txt',
        'classified_vault.txt',
        'standard_archive.txt'
    )
    try:
        with open(filename, 'r') as file:
            print(f'ROUTINE ACCESS: Attempting access to {filename}')
            print(f'Archive recovered - ``Knowledge preserved for humanity``')
            print('STATUS: Normal operations resumed')

    except FileNotFoundError:
        print(
            f"CRISIS ALERT: Attempting access to '{filename}'...", file=stderr
        )
        print('RESPONSE: Archive not found in storage matrix', file=stderr)
        print('STATUS: Crisis handled, system stable', file=stdout)
    except PermissionError:
        print('RESPONSE: Security protocols deny access', file=stderr)
        print('STATUS: Crisis handled, security maintained', file=stdout)

    except ValueError:
        print('RESPONSE: Invalid data format', file=stderr)
        print('STATUS: Crisis handled, system stable', file=stdout)
    finally:
        file.close()


def main() -> None:
    '''
        #   Small main program.
    '''
    print('=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n')
    crisis_response_protocol()
    print('\nAll crisis scenarios handled successfully. Archives secure.')
    exit(1)


if (__name__ == '__main__'):
    main()
