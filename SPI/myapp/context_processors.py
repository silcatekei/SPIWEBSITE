import os
from django.conf import settings

def slider_images(request):
    """Load all image filenames from the 'static/images/slider' folder"""
    
    # Get the full path of the slider folder inside STATICFILES_DIRS
    slider_folder = os.path.join(settings.STATICFILES_DIRS[0], 'images', 'slider')

    if not os.path.exists(slider_folder):
        return {'image_files': []}  # Return an empty list if the folder doesn't exist

    # List all image files inside the folder
    image_files = [
        f"images/slider/{f}" for f in os.listdir(slider_folder)
        if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))
    ]

    return {'image_files': image_files}
