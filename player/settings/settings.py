from const import STOP_CODE
from core import error_logger
from core.file_io import read_data_json, write_data_json
from core.helpers.prompt import prompt
from core.repl import REPL
from strings import GO_BACK, SETTINGS

SETTINGS_FILE = "settings"
PRINT_DELAY = "PRINT_DELAY"


class Settings:

    structure = {}
    settings = {PRINT_DELAY: 0}

    @classmethod
    def _get_structure(cls):
        cls.structure = {
            SETTINGS: {
                f"Print delay -- emulates older computer terminals (ms): {cls.settings[PRINT_DELAY]}": cls.set_print_delay,
                GO_BACK: STOP_CODE,
            }
        }
        return cls.structure

    @classmethod
    def open_settings_menu(cls):
        cls.load_settings_from_disk()
        cls.repl = REPL(cls._get_structure(), type="Settings")
        cls.repl.run(SETTINGS)

    @classmethod
    def set_print_delay(cls):
        new_val = int(
            prompt(
                f"Set new print delay (currently set to {cls.settings[PRINT_DELAY]})"
            )
        )
        cls.settings[PRINT_DELAY] = new_val
        cls.update_settings()

    @classmethod
    def get_print_delay(cls):
        return cls.settings[PRINT_DELAY]

    @classmethod
    def update_settings(cls):
        cls.repl.set_structure(cls._get_structure())
        cls.save_settings_to_disk()

    @classmethod
    def save_settings_to_disk(cls):
        write_data_json(SETTINGS_FILE, cls.settings)

    @classmethod
    def load_settings_from_disk(cls):
        try:
            cls.settings = read_data_json(SETTINGS_FILE)
        except Exception as e:
            error_logger.log_error(f"Error while loading settings from disk: {e}")
