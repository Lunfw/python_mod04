from sys import stderr, exit


def diagnosis(file: str) -> tuple:
    temp: list[str, str] = ['', '']
    try:
        open(file, 'r')
    except FileNotFoundError:
        temp[0] = " Archive not found in storage matrix"
        temp[1] = " Crisis handled, system stable\n"
    except PermissionError:
        temp[0] = " Security protocols deny access"
        temp[1] = " Crisis handled, security maintened\n"
    finally:
        if (temp[0] == '' or temp[1] == ''):
            temp[0] = ' Could not diagnose'
            temp[1] = ' Unknown Error\n'
    return tuple(temp)


def lib_archive() -> tuple:
    temp: tuple[str] = (
        'lost_archive.txt',
        'classified_vault.txt',
        'standard_archive.txt'
    )
    return temp


def crisis_response_protocol() -> None:
    '''
        #   Opens and reads a file through stdout.
    '''
    temp: tuple[str] = lib_archive()
    for i in temp:
        can_close: bool = True
        try:
            with open(i, 'r') as file:
                print(f'ROUTINE ACCESS: Attempting access to {i}')
                print(f"Archive recovered - ``{file.read()}''")
            print('STATUS: Normal operations resumed\n')
        except Exception:
            print(
                f"CRISIS ALERT: Attempting access to '{i}'...", file=stderr
            )
            diagnosed: tuple = diagnosis(i)
            print(f'RESPONSE: {diagnosed[0]}')
            print(f'STATUS: {diagnosed[1]}')
            can_close = False
        finally:
            if (can_close):
                file.close()


def main() -> None:
    '''
        #   Small main program.
    '''
    print('=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n')
    crisis_response_protocol()
    print('All crisis scenarios handled successfully. Archives secure.')
    exit(1)


if (__name__ == '__main__'):
    main()
