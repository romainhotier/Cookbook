import json
import jsonpickle


class Nutriments(object):

    def __init__(self, **kwargs):
        """ Nutriments model.

        - calories = Nutriments' calories value
        - carbohydrates = Nutriments' carbohydrates value
        - fats = Nutriments' fats value
        - proteins = Nutriments' proteins value
        - portion = coefficient for calories calculation

        Returns
        -------
        ResponseBody
        """
        self.calories = 0
        self.carbohydrates = 0
        self.fats = 0
        self.proteins = 0
        self.portion = 1
        if "serialize" in kwargs:
            self.set_attributes(kwargs["serialize"])

    def get_attributes(self):
        """ Get Nutriments attributes.

        Returns
        -------
        list
            Nutriments attributes.
        """
        return [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]

    def set_attributes(self, data):
        """ Set Nutriments attributes.

        Parameters
        ----------
        data : dict
            Json.

        """
        try:
            for key, value in data.items():
                if key in self.get_attributes():
                    self.__setattr__(key, value)
        except AttributeError:
            pass

    def get_as_json(self):
        """ Return Nutriments as a dict.

        Return
        ----------
        dict
            Nutriments as Json.

        """
        return json.loads(jsonpickle.encode(self, unpicklable=False))
