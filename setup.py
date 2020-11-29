#import sys
print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))
import lib.epdconfig


""" from setuptools import setup
setup(
    name='waveshare-epd',
    description='Waveshare e-Paper Display',
    author='Waveshare',
    package_dir={'': 'lib'},
    packages=['waveshare_epd'],
) """