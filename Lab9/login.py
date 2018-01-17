import logging
import calculate

loger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename="app.log", level=logging.INFO)

    logging.INFO("start")
    calculate.funkcja()
    logging.info("Koniec")
    logging.debug("debug")

if __name__ == '__main__':
    main()
