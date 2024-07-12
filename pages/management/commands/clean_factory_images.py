from pathlib import Path
from django.core.management.base import BaseCommand, CommandParser
from web.settings import MEDIA_ROOT
from ipdb import set_trace

def delete_factory_images(directory, start_string='factory_'):
    # Create a Path object for the directory
    dir_path = MEDIA_ROOT / directory
    
    # Iterate through all files in the directory
    for file_path in dir_path.glob('*'):
        # Check if it's a file and if the substring is in the filename
        if file_path.is_file() and file_path.name[:8] == start_string:
            try:
                file_path.unlink()
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

class Command(BaseCommand):
    help = 'remove factory boy made images'

    def add_arguments(self, parser):
        parser.add_argument(
            '--image_dir', type=str, help='image folder name',
            default='person', required=False
        )
    
    def handle(self, *args, **options):
        image_dir = options['image_dir']
        delete_factory_images(image_dir)
        self.stdout.write(
            f'Factory images under [{image_dir}/] have been removed.'
        )