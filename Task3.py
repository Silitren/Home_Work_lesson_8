class CustomError(Exception):

    def __init__(self, txt):
        self.txt = txt


print("Для остановки программы введите stop")
check_list = []
while True:
    value_input = input('Введите число в список:')
    try:
        if value_input == 'stop':
            break
        elif not value_input.isdigit():
            raise CustomError("Нас не обманешь!")
        check_list.append(value_input)
    except CustomError as ce:
        print(ce)
print(check_list)
