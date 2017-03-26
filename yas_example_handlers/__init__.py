import time

from yas import RegexHandler
from yas_example_handlers.yaml_file_config import YamlConfiguration


class ExampleCreateHandler(RegexHandler):

    def __init__(self, bot_name, api_call, log=print):
        super().__init__('(?:create)\ ([-\w]+)', bot_name, api_call, log=log)

    def handle(self, data, reply):
        match_groups = self.current_match.groups()
        self.__create(*match_groups, reply=reply)

    def __create(self, thing_to_create, reply=None):
        reply(f'Creating {thing_to_create}')
        self.log('INFO', f"Created {thing_to_create}")

class ExampleSleepHandler(RegexHandler):

    def __init__(self, bot_name, api_call, log=print):
        super().__init__('(?:sleep)\ ([-\d]+)', bot_name, api_call, log=log)

    def handle(self, data, reply):
        sleep_seconds = int(self.current_match.groups()[0])
        time.sleep(sleep_seconds)
        reply(f'Slept for {sleep_seconds}')
