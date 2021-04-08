def main():
    target_number = int(input('Input number: '))
    while (check_number := int(input('Your idea? '))) != target_number:
        print('Your number {} my number. Try again'
                .format('>' if check_number > target_number else '<'))
    else:
        print(f'You win! My number is {target_number}')

if __name__ == '__main__':
    main()

