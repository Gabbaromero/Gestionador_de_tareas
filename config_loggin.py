import logging

def config_logging():
    logging.basicConfig(filename='logs.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def registrar_accion(accion, detalles):
    logging.info(f'{accion}: {detalles}')