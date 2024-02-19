#!/usr/bin/python3
"""
Module containing the DBStorage
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    """DBStorage class for SQLAlchemy storage engine
    """
    __engine = None
    __session = None

    def __init__(self):
        """Creates the engine and session for the database
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(os.getenv('HBNB_MYSQL_USER'),
                                             os.getenv('HBNB_MYSQL_PWD'),
                                             os.getenv('HBNB_MYSQL_HOST'),
                                             os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def all(self, cls=None):
        """Query all objects from the current database session
        """
        objects = {}
        if cls:
            query_result = self.__session.query(cls).all()
            for obj in query_result:
                key = "{}.{}".format(cls.__name__, obj.id)
                objects[key] = obj
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for cls in classes:
                query_result = self.__session.query(cls).all()
                for obj in query_result:
                    key = "{}.{}".format(cls.__name__, obj.id)
                    objects[key] = obj
        return objects

    def new(self, obj):
        """Adds the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes the object from the current database session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database and
        creates the current database session from the engine
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """Closes the current session
        """
        self.__session.close()
