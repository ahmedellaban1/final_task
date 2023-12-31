import random
from datetime import date


def file_rename(file_name, number_digit):
    min_value = 10 ** (number_digit - 1)
    max_value = (10 ** number_digit) - 1
    name, extension = file_name.split('.')
    random_number = random.randint(min_value, max_value)
    formatted_date = date.today().strftime("%m-%Y")
    return extension, random_number, formatted_date

# to create an uploader us file_uploader() to and custom return
# def model_image_uploader(instance, file_name):
#     file = file_rename(file_name, 10)
#     return f'Model/{file[2]}/{file[1]}_{instance.name}.{file[0]}'
