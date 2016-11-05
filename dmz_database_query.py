from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dmz_database_create import users_dmz, Base, services_dmz

class dmz_query():
    global engine
    engine = create_engine('sqlite:///dmz_database_version-1.0.db')
    Base.metadata.bind = engine
    global DBSession
    DBSession= sessionmaker(bind=engine)
    global session
    session = DBSession()

    def __init__(self):
        return

    @staticmethod
    def add_user(name, password):
        new_person = users_dmz(user_name=name, user_pass=password)
        session.add(new_person)
        session.commit()
        return "Added"

    @staticmethod
    def delete_user(name , password):
        session.query(users_dmz).filter(users_dmz.user_name==name,users_dmz.user_pass==password).delete()
        session.commit()
        return "Deleted"

    @staticmethod
    def view_user(name,password):
        return (session.query(users_dmz).filter(users_dmz.user_name==name,users_dmz.user_pass==password).first())

    @staticmethod
    def delete_all_users():
        session.query(users_dmz).delete()
        session.query(services_dmz).delete()
        session.commit()
        return "Deleted All Users"

    @staticmethod
    def delete_all_services(self):
        session.query(services_dmz).delete()
        session.commit()
        return "Deleted All Services"

    @staticmethod
    def add_grp(name ,grpid , password):
        session.query(users_dmz).filter(users_dmz.user_name==name,users_dmz.user_pass==password).update({"user_grp":grpid})
        session.commit()
        return "Group Added"

    @staticmethod
    def remove_grp(name, grpid, password):
        session.query(users_dmz).filter(users_dmz.user_name == name, users_dmz.user_pass == password).update({"user_grp": 0})
        session.commit()
        return "Group Removed"

    @staticmethod
    def add_service(user, protocol,port ,name):
        new_address = services_dmz(service_name=name, service_protocol=protocol, service_port=port, users=user)
        session.add(new_address)
        session.commit()
        return "Service Added"

    @staticmethod
    def remove_service(user , protocol  , port , name ):
        session.query(services_dmz).filter(services_dmz.service_name==name,services_dmz.service_port==port,services_dmz.service_protocol==protocol,services_dmz.users==user).delete()
        session.commit()
        return "Service Removed"

    @staticmethod
    def add_service_grp(grp , protocol,port ,name):
        for user in session.query(users_dmz).filter(users_dmz.user_grp==grp).all():
            dmz_query.add_service(user, protocol,port ,name)
        return "Service Added to Group"

    @staticmethod
    def remove_service_grp(grp, protocol, port, name):
        for user in session.query(users_dmz).filter(users_dmz.user_grp == grp).all():
            dmz_query.remove_service(user, protocol, port, name)
        return "Service Removed from Group"
    @staticmethod
    def add_user_ip(name , password , ip):
        session.query(users_dmz).filter(users_dmz.user_name == name, users_dmz.user_pass == password).update({"user_ip": ip})
        #find all rules , push rules
        session.commit()


