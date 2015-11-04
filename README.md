# CMS Lab Carousel

CMS Lab Carousel is A Django app for adding carousel of recent papers, etc. to a Django site with django CMS-specific features.

<!-- Detailed documentation is in the "docs" directory. -->

## Quick start

- Edit the project's `settings.py` file.

    - Add `cms_lab_carousel` and its dependencies to your `INSTALLED_APPS` setting:

        ```python
        INSTALLED_APPS = (
            ...
            'cms_lab_carousel',
            'cms_lab_publications',
            'easy_thumbnails',
            'filer',
            'mptt',
            'taggit',
        )
        ```

    - Specify your media settings, if not already specified:

        ```python
        MEDIA_URL = '/media/'
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        ```

    - Add `easy_thumbnail` settings: 

        ```python
        # For easy_thumbnails to support retina displays (recent MacBooks, iOS)
        THUMBNAIL_HIGH_RESOLUTION = True
        THUMBNAIL_QUALITY = 95
        THUMBNAIL_PROCESSORS = (
            'easy_thumbnails.processors.colorspace',
            'easy_thumbnails.processors.autocrop',
            'filer.thumbnail_processors.scale_and_crop_with_subject_location',
            'easy_thumbnails.processors.filters',
        )
        THUMBNAIL_PRESERVE_EXTENSIONS = ('png', 'gif')
        THUMBNAIL_SUBDIR = 'versions'
        ```

- Include URL configurations for `cms_lab_carousel` in your project's `urls.py` file:

    ```python
    urlpatterns = patterns('',
        ...
        url(r'^carousel/', include('cms_lab_carousel.urls', namespace='carousel')),
        ...
    )
    ```

- Run `python manage.py makemigrations cms_lab_carousel` to create the cms_lab_carousel migrations.

- Run `python manage.py migrate` to create the cms_lab_carousel models.

- Start the development server (`python manage.py runserver`) and visit http://127.0.0.1:8000/

- Create a CMS page and insert the `Carousel Plugin` into a placeholder field.

*Version 0.2.0*
