from os.path import abspath, basename, dirname, join


# ##### PATH CONFIGURATION ################################

# fetch FastAPI's project directory
BASE_DIR = dirname(dirname(abspath(__file__)))

# the name of the whole site
SITE_NAME = basename(BASE_DIR)

# look for templates here
# This is an internal setting, used in the TEMPLATES directive
PROJECT_TEMPLATES_ROOT = join(BASE_DIR, 'assets', 'templates')

PROJECT_STATIC_ROOT = join(BASE_DIR, 'assets', 'static')

MEDIA_ROOT = join(BASE_DIR, 'media')
