from sys import exit


def secure_vault(filename: str) -> bool:
    '''
        #   'with' statement demonstration.
    '''
    print('Initiating secure vault access...')
    try:
        with open(filename, 'r') as file:
            print('Vault connection established with failsafe procotols\n')
            print('SECURE EXTRACTION:')
            reader = file.read()
            print(reader)
            with open('preserved.txt', 'a') as dup:
                print('SECURE PRESERVATION:')
                dup.write(reader)
                print('[CLASSIFIED] New security protocols archived')
        print('Vault automatically sealed upon completion')
    except FileNotFoundError:
        print('# Could not find fragments. Exited with code 1')
        return (False)
    finally:
        file.close()
        dup.close()
    return (True)


def main() -> None:
    '''
        #   Small main program.
    '''
    print('=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n')
    if (secure_vault('to_extract.txt')):
        print('\nAll vault operations completed with maximum security')
        return
    print('\nVault operations could not be completed')
    exit(1)


if (__name__ == '__main__'):
    main()
