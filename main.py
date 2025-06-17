from flask import Flask

app = Flask(__name__)

# Importa as rotas depois que o app foi criado
from views import *

if __name__ == "__main__":
    app.run(debug=True)
