from sys import exit


def file_open(filename: str) -> bool:
    '''
        #   Opens a file then cats it.
    '''
    print(f'Accessing Storage Vault: {filename}')
    try:
        with open(filename, 'r') as file:
            print('Connection established...\n')
            print('RECOVERED DATA:')
            print(file.read())
    except FileNotFoundError:
        print(f"# Failed to decrypt fragment '{filename}' -> Does not exist\n")
        return (False)
    finally:
        file.close()
    return (True)


def main() -> None:
    '''
        #   Small main program.
    '''

    print('=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n')
    if (file_open('ancient_fragment.txt')):
        print('\nData recovery complete. Storage unit disconnected.')
        return
    print('\nData recovery failed. Disconnecting.')
    exit(1)


if (__name__ == '__main__'):
    main()
