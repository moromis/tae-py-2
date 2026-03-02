from argparse import ArgumentParser
from core import logger
from main_structure import MAIN, PROGRAMS
from strings import TAE, TAE_DESC, TAE_EPILOG


class ArgsParser:
    @classmethod
    def parse_args(cls):
        parser = ArgumentParser(prog=TAE, description=TAE_DESC, epilog=TAE_EPILOG)
        parser.add_argument("-p", "--program", default=MAIN, choices=PROGRAMS.keys())
        parser.add_argument("-f", "--filename")
        parser.add_argument(
            "-s", "--start", help="overrides --program", action="store_true"
        )
        parser.add_argument("-debug", "--debug", action="store_true")
        parser.add_argument("-v", "--verbose", action="store_false")

        cls.args = parser.parse_args()
        logger.log(str(cls.args))
        return cls.args

    @classmethod
    def get_debug(cls) -> bool:
        if cls.args:
            return cls.args.debug
        else:
            return False
