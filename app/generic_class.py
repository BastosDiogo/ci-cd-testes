api_registry = {}

class MainClass(type):
    """Meta class to generate other class."""
    required_api_methods = ['start', 'shutdown']

    def __new__(mcs, class_name, bases, class_dict):
        cls = super().__new__(mcs, class_name, bases, class_dict)

        if not class_dict.get('__is_api_base__', False):
            for method_name in mcs.required_api_methods:
                if not any(method_name in base.__dict__ for base in cls.__mro__):
                    raise TypeError(
                        f"Class '{class_name}' must implement the required method '{method_name}' "
                        "(either directly or via inheritance)."
                    )
            api_registry[class_name] = cls

        return cls

class GenericAPI(metaclass=MainClass):
    """Class generic to simulate APIs creations."""
    __is_api_base__ = True

    def __init__(self):
        for method_name in MainClass.required_api_methods:
            method = getattr(self, method_name, None)
            if not callable(method):
                raise RuntimeError(
                    f"Instance of class '{self.__class__.__name__}' is invalid: "
                    f"required method '{method_name}()' is missing or not callable at runtime."
                )
