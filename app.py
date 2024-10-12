from flask import Flask, render_template_string
import juego  # Asegúrate de que el archivo juego.py esté en el mismo directorio

app = Flask(__name__)

# HTML simple para mostrar el juego
template = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Juego Online</title>
  </head>
  <body>
    <h1>Bienvenido al Juego</h1>
    <div id="game">
      <p>{{ game_output }}</p>
    </div>
  </body>
</html>
"""

@app.route('/')
def index():
    # Lógica para ejecutar el juego
    game_output = juego.main()  # Suponiendo que juego.py tiene una función main() que inicia el juego
    return render_template_string(template, game_output=game_output)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
