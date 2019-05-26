from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#Init db
db=SQLAlchemy(app)#ORM

#Init ma
ma=Marshmallow(app)#Serialize and Deserialize

#Product Class/Model
class Product(db.Model):
    """This class is the model of a Product"""
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True)
    description=db.Column(db.String(200))
    price=db.Column(db.Float)
    qty=db.Column(db.Integer)

    def __init__(self,name,description,price,qty):
        self.name=name;
        self.description=description
        self.price=price
        self.qty=qty

#Product Schema
class ProductSchema(ma.Schema):
    """This class allow to put what fields you're going to show"""
    class Meta:
        fields=('id','name','description','price','qty')


#Init Schema

product_schema=ProductSchema(strict=True)#To retrieve one product
products_schema=ProductSchema(many=True,strict=True)#To retrieve many products

#Create a product
@app.route('/product',methods=['POST'])
def add_product():
    name=request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    new_product=Product(name,description,price,qty)

    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product)

#Get all products
@app.route('/products',methods=['GET'])
def get_products():
    all_products=Product.query.all()#we use SQLAlchemy
    result=products_schema.dump(all_products)
    return jsonify(result.data)

#Get SINGLE products
@app.route('/product/<id>',methods=['GET'])
def get_product(id):
    product=Product.query.get(id)#we use SQLAlchemy
    return product_schema.jsonify(product)

#Update a product
@app.route('/product/<id>',methods=['PUT'])
def update_product(id):
    product=Product.query.get(id)
    product.name=request.json['name']
    product.description = request.json['description']
    product.price = request.json['price']
    product.qty = request.json['qty']

    db.session.commit()
    return product_schema.jsonify(product)

#Delete a product
@app.route('/product/<id>',methods=['DELETE'])
def delete_product(id):
    product=Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return product_schema.jsonify(product)

if __name__ == '__main__':
    app.run(debug=True)
