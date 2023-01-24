import os

from cryptography.fernet import Fernet


class PasswordManager:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.password_file = None
        self.password_dict = {}

    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, "wb") as f:
            f.write(self.key)

    def load_key(self, path):
        with open(path, "rb") as f:
            self.key = f.read()

    def create_file(self, path, initial_values=None):
        self.password_file = path

        if initial_values is not None:
            for k, v in initial_values.items():
                self.add_password(k, v)

    def load_file(self, path):
        self.password_file = path

        with open(path, "r") as f:
            for line in f.readlines():
                site, encrypt_pass = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypt_pass.encode()).decode()

        return self.password_dict

    def add_password(self, site, password):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file, "a+") as f:
                encrypt_pass = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypt_pass.decode() + "\n")

    def delete_password(self, site, path):
        del self.password_dict[site]
        pass_dict = {}

        with open(path, "r") as f:
            for line in f.readlines():
                site, encrypt_pass = line.split(":")
                pass_dict[site] = Fernet(self.key).decrypt(encrypt_pass.encode()).decode()

        del pass_dict[site]
        os.remove(path)
        self.create_file(path, pass_dict)

    def delete_all(self, path):
        os.remove(path)
        self.password_dict.clear()

    def get_password(self, path, site):
        load_pass = self.load_file(path)
        return load_pass[site]

    def get_password_once(self, site):
        return self.password_dict[site]

    def get_beautiful_passwords(self, path):
        main = ""
        for k, v in self.load_file(path).items():
            main += k + " = " + v + "\n"

        return main


if __name__ == '__main__':
    passwords = {
        "email": "123241",
        "vk": "fsag21421"
    }

    pm = PasswordManager()
    pm.load_key("other_files/key.key")
    pm.add_password("humana", "585858")
    print(pm.load_file("other_files/12.pass"))