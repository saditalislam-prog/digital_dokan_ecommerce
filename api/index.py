import os
import sys

# Add the 'backend' folder to sys.path so 'config' and 'store' can be found
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(CURRENT_DIR)
BACKEND_DIR = os.path.join(ROOT_DIR, 'backend')

if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from config.wsgi import application

# Vercel entry point
app = application

