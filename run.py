import os
from resource_keeper import app


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        # Set debug to dev or production mode
        debug=False
    )