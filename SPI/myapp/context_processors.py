import os
from django.conf import settings

import os
from django.conf import settings

def slider_images(request):
    """Load image filenames from 'static/images/slider' and 'static/images/sliderbackup' folders"""
    
    # Get the full path of the slider folder inside STATICFILES_DIRS
    # **Swiper slider images** will be fetched from 'images/slider' folder
    slider_folder = os.path.join(settings.STATICFILES_DIRS[0], 'images', 'slider')

    # **Carousel images** will be fetched from 'images/sliderbackup' folder
    carousel_folder = os.path.join(settings.STATICFILES_DIRS[0], 'images', 'sliderbackup')

    # Load images for the Swiper slider
    if not os.path.exists(slider_folder):
        slider_images = []  # Return an empty list if the folder doesn't exist
    else:
        # List all image files in the 'slider' folder
        slider_images = [
            f"images/slider/{f}" for f in os.listdir(slider_folder)
            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))  # Only include image files
        ]
    
    # Load images for the Bootstrap carousel
    if not os.path.exists(carousel_folder):
        carousel_images = []  # Return an empty list if the folder doesn't exist
    else:
        # List all image files in the 'sliderbackup' folder
        carousel_images = [
            f"images/sliderbackup/{f}" for f in os.listdir(carousel_folder)
            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))  # Only include image files
        ]

    # Return two separate lists: one for the Swiper slider and one for the Bootstrap carousel
    return {'slider_images': slider_images, 'carousel_images': carousel_images}
