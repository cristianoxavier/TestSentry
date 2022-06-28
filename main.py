import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration
import os

os.getenv("DNS_SENTRY")

sentry_sdk.init(
    dsn=DNS_SENTRY,
    integrations=[
        FlaskIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

app = Flask(__name__)


@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0

if __name__ == '__main__':
    app.run()
