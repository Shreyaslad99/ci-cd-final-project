"""Routes for the counter API."""
from flask import abort, jsonify, url_for
from service import app
from service.common import status

COUNTERS = {}


@app.get("/health")
def health():
    """Return a health status."""
    return jsonify(status="OK"), status.HTTP_200_OK


@app.get("/")
def index():
    """Return basic API metadata."""
    return jsonify(
        status=status.HTTP_200_OK,
        message="Counter REST API",
        version="1.0.0",
        url=url_for("list_counters", _external=True),
    )


@app.get("/counters")
def list_counters():
    """List all counters."""
    return jsonify([{"name": name, "counter": value} for name, value in COUNTERS.items()])


@app.post("/counters/<name>")
def create_counter(name):
    """Create a counter if it does not already exist."""
    if name in COUNTERS:
        abort(status.HTTP_409_CONFLICT, description=f"Counter {name} already exists")
    COUNTERS[name] = 0
    return (
        jsonify(name=name, counter=0),
        status.HTTP_201_CREATED,
        {"Location": url_for("read_counter", name=name, _external=True)},
    )


@app.get("/counters/<name>")
def read_counter(name):
    """Read a named counter."""
    if name not in COUNTERS:
        abort(status.HTTP_404_NOT_FOUND, description=f"Counter {name} does not exist")
    return jsonify(name=name, counter=COUNTERS[name]), status.HTTP_200_OK


@app.put("/counters/<name>")
def update_counter(name):
    """Increment a named counter."""
    if name not in COUNTERS:
        abort(status.HTTP_404_NOT_FOUND, description=f"Counter {name} does not exist")
    COUNTERS[name] += 1
    return jsonify(name=name, counter=COUNTERS[name]), status.HTTP_200_OK


@app.delete("/counters/<name>")
def delete_counter(name):
    """Delete a named counter; deleting a missing counter is harmless."""
    COUNTERS.pop(name, None)
    return "", status.HTTP_204_NO_CONTENT


def reset_counters():
    """Clear in-memory counters for tests."""
    COUNTERS.clear()
