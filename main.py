from loguru import logger

from core.game import Laitner

try:
    game = Laitner((720, 480))
    game.loop()
except Exception:
    logger.add('file_{time}.log')
    logger.exception('What?')
