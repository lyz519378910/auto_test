import yaml


class YamlOperation:
    def __init__(self, locat_file):
        with open(locat_file) as yaml_file:
            self.data = yaml.load(yaml_file, yaml.FullLoader)

    def get_locator(self, page, local):
        return self.data[page][local]

# if __name__ == '__main__':
#     y = YamlOperation()
#     print(y.get_locator('LoginPage','username'))


