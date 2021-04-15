class CustomError(Exception):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def div_null(a, b):
        if b == 0:
            print("Вы сошли с ума!?")
        else:
            return print(f"Ваш результат {a / b}")

c = CustomError.div_null(int(input("Введите делимое число: ")), int(input("Введите делить число: ")))



# while True:
#     a = int(input("Введите делимое число: "))
#     b = int(input("Введите делить число: "))
#     try:
#         if b == 0:
#             raise CustomError
#     except CustomError as ce:
#         print(ce)
#     else:
#         print(f"Результат вашего деления: {a / b}")
#         break
