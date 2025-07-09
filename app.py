from flask import Flask
from flasgger import Swagger
from routes.dataset_route import bp

app = Flask(__name__)
Swagger(app)
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)
