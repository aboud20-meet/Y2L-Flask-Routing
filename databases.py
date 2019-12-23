from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = scoped_session(sessionmaker(bind=engine,autoflush=False))

def add_product(Name, Price, Picture, Description):
	product_object =product(
		Name = Name,
		Price = Price,
		Picture = Picture,
		Description = Description)
	session.add(product_object)
	session.commit()
 

add_product("Turkey Samdwich", 20,"https://www.google.co.il/search?q=turkey+sandwich&safe=strict&client=ubuntu&hs=hep&sxsrf=ACYBGNSWQPV8uGAnuUOrL6eOdpi3O10gkA:1577122934233&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjLhoziqMzmAhUGkRQKHbnFDLsQ_AUoAXoECA8QAw#", "expired")
	

def query_by_id(id, Name):
	product_object =session.query(
		product).filter_by()
	id=their_idfirst()
	

def delete_product(Name):
	product_object =session.query(
		product).filter_by (Name = Name).delete()
	session.commit()


def query_all():
	product_object = session.query(
		product).all()	
	return product_object




def return_product(id):
	product_object = session.query(
		product).filter_by(
		id=their_id).first()
	return product_object



def add_to_cart(productID):
	cart_object = cart(
		cart_ID= productID)
	session.add(cart_object)
	session.commit()






