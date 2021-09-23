from flask import Flask, render_template, request
app = Flask(__name__)  

data = [
    ['cristobal','Cristóbal Ugarte','Profesor','Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat ut cumque voluptatum distinctio libero, repudiandae fuga voluptate, repellendus facilis natus vero architecto quas ex iusto optio vel nisi obcaecati nam.'],
    ['cami','Camila Pozas','Ayudante','Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat ut cumque voluptatum distinctio libero, repudiandae fuga voluptate, repellendus facilis natus vero architecto quas ex iusto optio vel nisi obcaecati nam.'],
    ['nofoto','Jon Doe','Ayudante 2','Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat ut cumque voluptatum distinctio libero, repudiandae fuga voluptate, repellendus facilis natus vero architecto quas ex iusto optio vel nisi obcaecati nam.'],
    ['nofoto','Jane Doe','Ayudante 3','Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat ut cumque voluptatum distinctio libero, repudiandae fuga voluptate, repellendus facilis natus vero architecto quas ex iusto optio vel nisi obcaecati nam.'],
    ['nofoto','John Doe','Ayudante 4','Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat ut cumque voluptatum distinctio libero, repudiandae fuga voluptate, repellendus facilis natus vero architecto quas ex iusto optio vel nisi obcaecati nam.'],
    ['nofoto','Yun Doe','Ayudante 5','Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat ut cumque voluptatum distinctio libero, repudiandae fuga voluptate, repellendus facilis natus vero architecto quas ex iusto optio vel nisi obcaecati nam.'],
]

@app.route('/')          
def hello_world():
    count = len(data)
    return render_template('index.html',personas = data, count = count)

@app.route('/persona/<id>')
def persona(id):
    persona = data[int(id)]
    return render_template('person.html',persona = persona)

if __name__=="__main__":   
    app.run(debug=True)    
