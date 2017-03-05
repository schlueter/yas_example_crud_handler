import re

from yas import YasHandler
from yas_example_crud_handler.yaml_file_config import YamlConfiguration
from yas_example_crud_handler.logging import logger


class ExampleCludHandler(YasHandler, YamlConfiguration):

    def __init__(self, regexp_string):
        super(YasHandler).__init__()
        self.regexp = re.compile(regexp_string)
        logger.log.debug(f"{self.__class__} initialized and matching {regexp_string}!")

    def test(self, data):
        logger.log.debug(f"Testing {data['yas_hash']} against {self.__class__}")
        self.current_match = self.regexp.match(data.get('text'))


class ExampleCreateHandler(ExampleCludHandler):

    def __init__(self):
        super().__init__('(?:create)\ ([-\w]+)')

    def handle(self, data, reply):
        logger.log.info(f"Handling {data['yas_hash']} with {self.__class__}")
        match_groups = self.current_match.groups()
        self.__create(*match_groups, reply=reply)

    def __create(self, thing_to_create):
        reply(f'Creating {thing_to_create}')
        logger.log.info(f"Created {thing_to_create}")
