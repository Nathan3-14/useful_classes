import json

class ModeError(Exception):
    def __init__(self):
        self.message = "No json path specified for json mode"
        super().__init__(self.message)

class Auth:
    def __init__(self, mode: str="json", **kwargs):
        self.mode = mode
        try:
            self.json_path = kwargs["json_path"]
        except KeyError:
            if mode == "json":
                raise ModeError

    def login(self, username, password) -> list:
        def login_json():
            with open(self.json_path, "r") as f:
                self.read_json = json.load(f)
            try:
                if self.read_json[username] == password:
                    return [True, ""]
                else:
                    return [False, "Incorrect username or password"]
            except KeyError:
                return [False, "Incorrect username or password"]
        
        def login_other():
            print(f"Work in progress, this does not exist yet")
        
        if self.mode == "json":
            return login_json()
        

if __name__ == "__main__":
    auth = Auth(json_path="./login.json")
    login = auth.login("nathan", "password")
    if login[0]:
        print("Welcome!")
    else:
        print(login[1])