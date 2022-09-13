from werkzeug.exceptions import HTTPException
from flask import request
from utils.response_api import ResponseJsonApi
from flask import jsonify
from utils.logger import getLoggerAplication

log = getLoggerAplication("Error Route")


def Error(app):
    @app.errorhandler(Exception)
    def global_handler(e):
        code = 500
        message = str(e)

        if isinstance(e, HTTPException):
            code = e.code

        errors = dict(
            error=e.args,
            message=message.strip(),
            code=code,
            path=request.path,
        )
                    
        log.warning(str(errors))
        return ResponseJsonApi(errors, code)