from flask import Flask

from app_helper import setup_metrics

from my_logger import get_logger

app = Flask(__name__)
log = get_logger(__name__)
setup_metrics(app)


@app.route('/test/')
def test():
    log.info('hitting /test/ endpoint')
    return 'rest'


@app.route('/test1/')
def test1():
    log.info('hitting /test1/ endpoint')
    try:
        1/0
    except Exception as e:
        log.exception(e)
        raise
    return 'rest'


@app.errorhandler(500)
def handle_500(error):
    log.error(f'something went wrong {error}')
    return str(error), 500


@app.errorhandler(404)
def handle_404(error):
    log.error(f'404 page not found {error}')
    return str(error), 404


if __name__ == '__main__':
    app.run(port=5001)
