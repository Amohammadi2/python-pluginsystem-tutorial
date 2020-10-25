class DataValidator:

    def __init__(self, data: dict):

        self.data = data

        self.string_constraints: dict = {
            "type": str,
            "min": 3,
            "max": 20,
        }

        self.number_constraints: dict = {
            "type": int,
            "min": 10,
            "max": 100
        }

        self.schema: dict = {
            "first-name": self.string_constraints,
            "last-name": self.string_constraints,
            "grade": self.number_constraints,
        }

    def isValid(self):

        if not len([k for k in self.data.keys() if k in (schema_keys:=self.schema.keys())]) == len(schema_keys):
            print(len([k for k in self.data.keys() if k in (schema_keys:=self.schema.keys())]))
            print(len(list(schema_keys)))
            raise Exception(
                f"these keys should be included in data: {[x for x in self.data.keys() if x not in schema_keys]!r}"
            )

        for key in schema_keys:
            value = self.data[key]
            constraints = self.schema[key]

            
            if not isinstance(value , (cons_type:=constraints["type"])):
                raise Exception(
                    f"the value of type {type(value)} doesn't match with {cons_type}"
                )

            if cons_type == str and not ((m:=constraints["max"]) > len(value) > (n:=constraints["min"])):
                raise Exception(
                    f"the length of string values should range between {m} and {n}"
                )
            elif cons_type == int and not ((m:=constraints["max"]) > value > (n:=constraints["min"])):
                raise Exception(
                    f"numeric values should be from {m} to {n}"
                )

        return True
