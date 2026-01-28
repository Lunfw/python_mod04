from sys import stdout, stderr, exit


def stream_management() -> bool:
    '''
        #   'stdout' and 'stderr' demonstration.
    '''
    id: str = input('Input Stream active. Enter archivist ID: ')
    status: str = input('Input Stream active. Enter status report: ')

    print(f'[STANDARD] Archive status from {id}: {status}', file=stdout)
    print(
        '[ALERT] System diagnostic: Communication channels verified',
        file=stderr
    )
    print('[STANDARD] Data transmission complete\n', file=stdout)
    return (True)


def main() -> None:
    '''
        #   Small main program.
    '''
    print('=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n')
    if (stream_management()):
        print('Three-channel communication test successful.')
        return
    print('Issues about the code... :(')
    exit(1)


if (__name__ == '__main__'):
    main()
