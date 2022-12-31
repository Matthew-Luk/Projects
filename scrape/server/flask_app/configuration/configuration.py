import os


class Config:
    # declare environment variables here w/ their default values
    POSTGRES_URL = ""
    REDIS_URL = ""

    def __init__(self):
        class_variables = [
            attribute for attribute in dir(self)
            if not attribute.startswith('__')
            and not callable(getattr(self, attribute))
        ]

        # check if environment variable is initialized so we can assign to config
        for class_variable in class_variables:
            # if environment variable doesn't exist, leave it as the default value
            if os.environ.get(class_variable, ""):
                self.__dict__[class_variable] = os.environ[class_variable]
