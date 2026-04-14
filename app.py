from flask import Flask
from flask_cors import CORS
from routes.cliente import cliente_bp
import os

app = Flask(__name__)
CORS(app)

app.register_blueprint(cliente_bp, url_prefix="/api")

# 👇 ESTO VA SIEMPRE AL FINAL
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)