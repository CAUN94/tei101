from flask import Flask, render_template, request
app = Flask(__name__)    

data = [
    ['cristobal','Cristóbal Ugarte','Profesor','Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat ut cumque voluptatum distinctio libero, repudiandae fuga voluptate, repellendus facilis natus vero architecto quas ex iusto optio vel nisi obcaecati nam.'],
    ['cami','Camila Pozas','Ayudante 1','hndisaohd udsaoihdsa hudsaiodhsoa'],
    ['nofoto','Javier','Docente','hndisaohd u hudsaiodhsoa'],
    ['nofoto','Camila Valdes','Ayudante 2','hndisaohd udsaoihdsa hudsaiodhsoa'],
    ['nofoto','Jon Doe','Ayudante 3','hndisaohd udsaoihdsa hudsaiodhsoa'],
]


@app.route('/')          
def hello_world():
    largo = len(data)
    return render_template('index.html',personas = data, largo = largo)

@app.route('/persona/<id>')
def persona(id):
    persona = data[int(id)-1]
    return render_template('person.html',persona = persona)





if __name__=="__main__":  
    app.run(debug=True)    

