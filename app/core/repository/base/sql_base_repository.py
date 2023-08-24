from fastapi_pagination import Params
from fastapi_pagination.ext.sqlalchemy import paginate

from app.core.database import Base, get_db_session
from app.core.exceptions import AppException

from .crud_repository_interface import CRUDRepositoryInterface


class SQLBaseRepository(CRUDRepositoryInterface):
    model: Base

    def __init__(self):
        """
        Base class to be inherited by all repositories. This class comes with
        base crud functionalities attached

        :param model: base model of the class to be used for queries
        """

    def index(self) -> [Base]:
        """

        :return: {list} returns a list of objects of type model
        """
        with get_db_session() as db_session:
            data = db_session.query(self.model).all()
        return data

    def pagination(self, params: Params) -> [Base]:
        """

        :return: {list} returns a list of objects of type model
        """
        with get_db_session() as db_session:
            data = paginate(db_session.query(self.model), params=params)
        return data

    def create(self, obj_in) -> Base:
        """

        :param obj_in: the data you want to use to create the model
        :return: {object} - Returns an instance object of the model passed
        """
        assert obj_in, "Missing data to be saved"

        with get_db_session() as db_session:
            obj_data = dict(obj_in)
            db_obj = self.model(**obj_data)
            db_session.add(db_obj)
            db_session.commit()
            db_session.refresh(db_obj)
        return db_obj

    def update_by_id(self, obj_id, obj_in) -> Base:
        """
        :param obj_id: {int} id of object to update
        :param obj_in: {dict} update data. This data will be used to update
        any object that matches the id specified
        :return: model_object - Returns an instance object of the model passed
        """
        assert obj_id, "Missing id of object to update"
        assert obj_in, "Missing update data"
        assert isinstance(obj_in, dict), "Update data should be a dictionary"

        db_obj = self.find_by_id(obj_id)
        with get_db_session() as db_session:
            for field in obj_in:
                if hasattr(db_obj, field):
                    setattr(db_obj, field, obj_in[field])
            db_session.add(db_obj)
            db_session.commit()
            db_session.refresh(db_obj)
        return db_obj

    def update(self, filter_params, obj_in):
        """
        :param filter_params: {dict}
        :param obj_in: {dict}
        :return: model_object - Returns an instance object of the model passed
        """
        db_obj = self.find(filter_params)
        with get_db_session() as db_session:
            for field in obj_in:
                if hasattr(db_obj, field):
                    setattr(db_obj, field, obj_in[field])
            db_session.add(db_obj)
            db_session.commit()
            db_session.refresh(db_obj)
        return db_obj

    def delete_by_id(self, obj_id):
        """
        :param obj_id:
        :return:
        """

        db_obj = self.find_by_id(obj_id)
        with get_db_session() as db_session:
            db_session.delete(db_obj)
            db_session.commit()
        return True

    def delete(self, filter_params: dict):
        """
        :param filter_params:
        :return:
        """

        db_obj = self.find(filter_params)
        with get_db_session() as db_session:
            db_session.delete(db_obj)
            db_session.commit()
        return True

    def find_by_id(self, obj_id) -> Base:
        """
        returns an object matching the specified id if it exists in the database
        :param obj_id: id of object to query
        :return: model_object - Returns an instance object of the model passed
        """
        assert obj_id, "Missing id of object for querying"

        with get_db_session() as db_session:
            db_obj = db_session.query(self.model).get(obj_id)
            if not db_obj:
                raise AppException.NotFoundException(error_message=None)
        return db_obj

    def find(self, filter_param: dict) -> Base:
        """
        This method returns the first object that matches the query parameters specified
        :param filter_param {dict}. Parameters to be filtered by
        """
        assert filter_param, "Missing filter parameters"
        assert isinstance(
            filter_param, dict
        ), "Filter parameters should be of type dictionary"

        with get_db_session() as db_session:
            db_obj = db_session.query(self.model).filter_by(**filter_param).first()
            if not db_obj:
                raise AppException.NotFoundException(error_message=None)
        return db_obj

    def find_all(self, filter_param) -> Base:
        """
        This method returns all objects that matches the query
        parameters specified
        """
        assert filter_param, "Missing filter parameters"
        assert isinstance(
            filter_param, dict
        ), "Filter parameters should be of type dictionary"

        with get_db_session() as db_session:
            db_obj = db_session.query(self.model).filter_by(**filter_param).all()
        return db_obj
