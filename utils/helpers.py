from pathlib import Path
from django.db import models

# allow shared methods or attributes
class FileCleanupMixin:
    # self here represent a model instance
    # this class can indicate whether a model contains file fields
    def delete_attached_files(self):
        for field in self._meta.fields:
            if isinstance(field, models.FileField):
                file = getattr(self, field.name)
                file_path = Path(file.path)
                if file_path and file_path.is_file(): 
                    file_path.unlink()

def split_date(date_str):
    [year, month, day] = date_str.split('-')

    return {'year': year, 'month': month, 'day': day}
