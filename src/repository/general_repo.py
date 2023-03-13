import unittest

from src.domain.student import Student
from src.repository.repository_exception import RepositoryException


class Repository:
    def __init__(self):
        self._objects = []

    def add(self, object):
        for obj in self._objects:
            if obj.id == object.id:
                raise RepositoryException("Duplicate id")
        self._objects.append(object)

    def remove(self, object_id):
        found = False
        for object in self._objects:
            if object.id == object_id:
                found = True
        if found == False:
            raise RepositoryException("Object not in Repository")
        for object in self._objects:
            if object.id == object_id:
                self._objects.remove(object)

    def update(self, object_id, new_name):
        found = False
        for obj in self._objects:
            if obj.id == object_id:
                found = True
        if found == False:
            raise RepositoryException("Object not in repository")
        for obj in self._objects:
            if obj.id == object_id:
                obj.name = new_name

    def find_by_id(self, objectId):
        for obj in self._objects:
            if obj.id == objectId:
                return obj
        return None

    def get_all(self):
        return self._objects

    def __len__(self):
        return len(self._objects)


