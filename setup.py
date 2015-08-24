import os
import sys
from setuptools import setup

if sys.version_info < (3, 2):
    print("Sorry, djangocms-lab-carousel currently requires Python 3.2+.")
    sys.exit(1)

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requires = [
    "Django==1.7.7",
    "Pillow==2.8.1",
    "Unidecode==0.04.17",
    "argparse==1.3.0",
    "dj-database-url==0.3.0",
    "django-classy-tags==0.6.1",
    "django-cms==3.1.0.b1",
    "django-filer==0.9.9",
    "django-mptt==0.6.1",
    "django-polymorphic==0.6.1",
    "django-reversion==1.8.5",
    "django-sekizai==0.8.1",
    "django-treebeard==2.0",
    "djangocms-admin-style==0.2.5",
    "djangocms-column==1.5",
    "djangocms-file==0.1",
    "djangocms-flash==0.2.0",
    "djangocms-googlemap==0.2",
    "djangocms-inherit==0.1",
    "djangocms-installer==0.7.3",
    "djangocms-lab-publications>=0.1.4"
    "djangocms-link==1.5",
    "djangocms-picture==0.1",
    "djangocms-style==1.5",
    "djangocms-teaser==0.1",
    "djangocms-text-ckeditor==2.4.3",
    "djangocms-video==0.1",
    "easy-thumbnails==2.2",
    "html5lib==0.999",
    "pytz==2015.2",
    "requests==2.6.0",
    "six==1.9.0",
]

setup(
    name='djangocms-lab-carousel',
    version='0.1.4',
    packages=['cms_lab_carousel'],
    include_package_data=True,
    license='BSD License',
    description='A Django app for adding carousel of recent papers, etc. to a Django site with django CMS-specific features',
    long_description=README,
    url='https://github.com/mfcovington/djangocms-lab-carousel',
    author='Michael F. Covington',
    author_email='mfcovington@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=install_requires,
)
