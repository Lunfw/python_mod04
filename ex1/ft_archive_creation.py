from sys import exit


def create_write(filename: str) -> tuple:
    '''
        #   Writes content to a file.
    '''
    string: str = 'ENTRY 00'
    temp: tuple = (
        'New quantum algorithm discovered',
        'Efficiency increased by 347%',
        'Archived by Data Archivist trainee'
    )
    print(f'Initializing new storage unit: {filename}')
    try:
        with open(filename, 'w') as file:
            print('Storage unit created successfully...\n')
            print('Inscribing preservation data...')
            for i in range(3):
                file.write(f'[{string + str(i + 1)}] {temp[i]}\n')
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f'# Failed to write to fragment {filename} -> Does not exist')
        return (False, filename)
    finally:
        file.close()
    return (True, filename)


def main() -> None:
    '''
        #   Small main program.
    '''
    print('=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n')
    temp: tuple = create_write('new_discovery.txt')
    if (temp[0]):
        print('Data inscription complete. Storage unit sealed.')
        print(f"Archive '{temp[1]}' ready for long-term preservation.")
        return
    print('Data inscription failed. Disconnecting.')
    exit(1)


if (__name__ == '__main__'):
    main()
