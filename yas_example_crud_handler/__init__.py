import re

from yas import YasHandler
from yas_example_crud_handler.yaml_file_config import YamlConfiguration


class ExampleCludHandler(YasHandler, YamlConfiguration):

    def __init__(self, regexp_string, log=print):
        super(YasHandler).__init__()
        self.regexp = re.compile(regexp_string)
        self.log('INFO', f"{self.__class__} initialized and matching {regexp_string}!")

    def test(self, data):
        self.log('INFO', f"Testing {data['yas_hash']} against {self.__class__}")
        self.current_match = self.regexp.match(data.get('text'))


class ExampleCreateHandler(ExampleCludHandler):

    def __init__(self, log=print):
        super().__init__('(?:create)\ ([-\w]+)', log=log)

    def handle(self, data, reply):
        self.log('INFO', f"Handling {data['yas_hash']} with {self.__class__}")
        match_groups = self.current_match.groups()
        self.__create(*match_groups, reply=reply)

    def __create(self, thing_to_create, reply=None):
        reply(f'Creating {thing_to_create}')
        self.log('INFO', f"Created {thing_to_create}")
