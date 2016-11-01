from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dmz_database_create import users_dmz, Base, services_dmz

engine = create_engine('sqlite:///dmz_database_version-1.0.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()
session.query(users_dmz).delete()
session.query(services_dmz).delete()
session.commit()
new_person = users_dmz(user_name='new person',user_pass=123345345)
session.add(new_person)
session.commit()

# Insert an Address in the address table
new_address = services_dmz(service_name='http', service_protocol="TCP",service_port=80 ,users=new_person)
session.add(new_address)
session.commit()

print(session.query(users_dmz).all())
person = session.query(users_dmz).first()
print(person.user_name)
print(session.query(services_dmz).first().service_name)


