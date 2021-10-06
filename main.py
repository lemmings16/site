


from flask import Flask, render_template, request


# Create a flask app
app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)


games = [
  {
    'naam': 'Valorant', 
    'verkochte_kopies': '14 miljoen',
    'spelers_per_dag': '251 duizend', 
    'leeftijden': '1 jaar en 2 maanden', 
    'genres': 'First-Person Shooter(FPS)'
  },
  {
    'naam': 'Minecraft',
    'verkochte_kopies': '200 miljoen',
    'spelers_per_dag': '857 duizend',
    'leeftijden': '10 jaar', 
    'genres': 'Sandbox'
  },
  {
    'naam': 'GTAV',
    'verkochte_kopies': '120 miljoen',
    'spelers_per_dag': '130 duizend',
    'leeftijden': '8 jaar',
    'genres': 'Open World',
  },
   {
    'naam': 'CS:GO',
    'verkochte_kopies': '30 miljoen', 
    'spelers_per_dag': '507 duizend',
    'leeftijden': '9 jaar',
    'genres': 'First-Person Shooter'
  }

]

# Index page (now using the index.html file)
@app.route('/')
def hello():
  return render_template('index.html', games=games)



 
  



@app.route('/game_invoer', methods=['POST'])
def invoer_game():
  invoer_game = request.form['invoer_game']
  return render_template('shop.html', 
                         invoer_game = invoer_game)



if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )



app.run()