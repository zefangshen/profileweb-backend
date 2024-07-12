# development utilities
import random
from faker import Faker
from django.core.files.uploadedfile import SimpleUploadedFile


fake = Faker()

def text_of_length(length):
    """generate text with a given length

    Args:
        length (int): length of the text

    Returns:
        function: return a function that generate texts with a given length
    """
    def _text():
        text = fake.text(max_nb_chars=length)
        return text    
    return _text

def sample_choice(choices):
    """Randomly sample a value from CHOICES 

    Args:
        choices (list): a list of tuples of two values defined in models
    """
    def _choice():
        i = random.randint(0, len(choices) - 1)

        return choices[i][0]
    
    return _choice

def fake_image(name=None, size=(100, 100), format="png"):

    if name is None:
        name = f'factory_{fake.word()}.{format}'

    def _image():

        return SimpleUploadedFile(
            name=name, content=fake.image(size=size, image_format=format),
            content_type=f'image/{format}'
        )

    return _image

def fake_date():
    from datetime import date
    def _date():
        [year, month, day] = [int(x) for x in fake.date().split('-')]
        f_date = date(year, month, day)

        return f_date

    return _date
