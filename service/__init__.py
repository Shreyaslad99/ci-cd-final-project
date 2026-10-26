"""Counter REST API service package."""
from flask import Flask

app = Flask(__name__)

from service import routes  # noqa: E402,F401

app.logger.info("*" * 70)
app.logger.info("SERVICERUNNING")
app.logger.info("*" * 70)
