class DictToObject:
    """
    Converts a dictionary into an object.
    Recursively converts nested dictionaries and lists.

    Attributes are dynamically created from dictionary keys.

    Example:

    ```
    data = {
        "user": {
            "name": "John Doe",
            "age": 30,
            "address": {
                "city": "Springfield",
                "country": "USA"
            }
        }
    }
    obj = DictToObject(data)
    print(obj.user.name)  # Output: John Doe
    print(obj.user.address.city)  # Output: Springfield
    print(obj.user.address.zip_code)  # Output: None
    ```
    """

    def __init__(self, dictionary=None):
        dictionary = {} if dictionary is None else dictionary
        self._validate_dict(dictionary)

        for key, value in dictionary.items():
            setattr(self, key, self._convert(value))

    def __setattr__(self, key, value):
        super().__setattr__(key, self._convert(value))

    def __getattr__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        return None

    def _validate_dict(self, obj):
        if not isinstance(obj, dict):
            raise ValueError(
                f"obj must be of type dict, not {type(obj)}.")

    def _convert(self, value):
        if isinstance(value, dict):
            return DictToObject(value)
        elif isinstance(value, list):
            return [self._convert(item) for item in value]
        else:
            return value

    def update(self, dictionary: dict):
        """
        Updates the object with the given dictionary.

        The dictionary's keys and values will be converted into attributes
        of the object. If a value is a dictionary, it will be recursively
        converted into a nested DictToObject. If a value is a list, each
        element will be converted accordingly.

        Example:

        ```
        obj.update({"user": {"name": "Jane Doe", "address": {"zip_code": "12345"}}})
        print(obj.user.name)  # Output: Jane Doe
        print(obj.user.address.zip_code)  # Output: 12345
        ```
        """
        self._validate_dict(dictionary)
        for key, value in dictionary.items():
            setattr(self, key, self._convert(value))

    def to_dict(self):
        """Returns the current object converted into a dictionary"""
        result = {}
        for key, value in self.__dict__.items():
            if isinstance(value, DictToObject):
                result[key] = value.to_dict()
            elif isinstance(value, list):
                result[key] = [item.to_dict() if isinstance(
                    item, DictToObject) else item for item in value]
            else:
                result[key] = value
        return result
