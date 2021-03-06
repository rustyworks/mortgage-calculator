import os

from app import create_app
from flask_script import Manager


app = create_app(os.environ.get('FLASK_CONFIG', 'development'))
manager = Manager(app)


if __name__ == '__main__':
    manager.run()
