class HttpErrorsSchemas:
    """class to build schemas of errors"""

    def __init__(self) -> None:
        self.schema = {}

    def bad_request(self, message: str = "incorrect payload"):
        self.schema = {**self.schema, 400: {"description": message}}
        return self

    def conflict(self, message: str):
        self.schema = {**self.schema, 409: {"description": message}}
        return self

    def not_found(self, message: str):
        self.schema = {**self.schema, 404: {"description": message}}
        return self

    def access_denied(self, message: str = "access_denied"):
        self.schema = {**self.schema, 403: {"description": message}}
        return self

    def unprocessable_entity(self, message: str = "unprocessable entity"):
        self.schema = {
            **self.schema,
            422: {"description": message},
        }
        return self

    def unauthorized(self, message: str = "unauthorized"):
        self.schema = {**self.schema, 401: {"description": message}}
        return self

    def locked(self, message: str = "Locked"):
        self.schema = {**self.schema, 423: {"description": message}}
        return self

    def build(self):
        return self.schema
