from flask import Flask, render_template, url_for

app = Flask(__name__)

productos_tecnologia = [
    {"id": 1, "nombre": "Teclado", "precio": 20},
    {"id": 2, "nombre": "Ratón", "precio": 15},
    {"id": 3, "nombre": "Monitor", "precio": 120},
    {"id": 4, "nombre": "Procesador", "precio": 240},
    {"id": 5, "nombre": "Cámara", "precio": 70},
    {"id": 6, "nombre": "Ea FC 26", "precio": 70},
    {"id": 7, "nombre": "Pokemon Legends ZA", "precio": 60},
    {"id": 8, "nombre": "PS5", "precio": 550},
    {"id": 9, "nombre": "Portatil Lenovo", "precio": 720},
    {"id": 10, "nombre": "Webcam", "precio": 50},
    {"id": 11, "nombre": "Nintendo Switch 2", "precio": 470},
    {"id": 12, "nombre": "Televisión LG 65 pulgadas", "precio": 890},
    {"id": 13, "nombre": "Xiaomi Redmi 13", "precio": 180},
    {"id": 14, "nombre": "iPhone 17 Pro Max", "precio": 1700},
    {"id": 15, "nombre": "Samsung Galaxy S24", "precio": 1500},

]




@app.route('/')
def home():
    return render_template("base.html")

@app.route('/productos')
def productos():
    lista = [x["nombre"] for x in productos_tecnologia]
    return render_template("index.html", lista=lista)

@app.route('/item/<int:id>')
def detalle(id):
    for producto in productos_tecnologia:
        if producto["id"] == id:
            item = producto
            break
    return render_template("detalle.html",
                           id_item=item["id"],
                           nombre_item=item["nombre"],
                           precio_item=item["precio"])


if __name__ == '__main__':
    app.run(debug=True)