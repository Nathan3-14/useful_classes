import json

class ModeError(Exception):
    def __init__(self) -> None:
        self.message = "No json path specified for json mode"
        super().__init__(self.message)

class Auth:
    def __init__(self, mode: str="json", **kwargs) -> None:
        self.mode = mode
        try:
            self.json_path = kwargs["json_path"]
        except KeyError:
            if mode == "json":
                raise ModeError

    def login(self, username, password) -> list[bool, str]:
        def login_json():
            try:
                with open(self.json_path, "r") as f:
                    self.read_json = json.load(f) #* Loads the json file and it's password data
            except Exception as e:
                print(f"Error while reading:\n  {e}")
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
        else:
            return login_other()
        

if __name__ == "__main__":
    my_auth = Auth(mode="json")
    login = my_auth.login("nathan", "password")