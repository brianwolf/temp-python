from typing import Dict

from logic.libs.variables.src.enviroment import parse_env_vars


def _make_vars_dict_by_env_file(ruta_archivo: str) -> Dict[str, str]:
    """
    """
    with open(ruta_archivo, 'r') as archivo:
        renglones_archivo = archivo.readlines()

    diccionario_variables = {}
    for renglon in renglones_archivo:

        if renglon.startswith('#') or renglon == '\n':
            continue

        clave, valor = renglon.split('=')

        if '#' in valor:
            valor = valor[:valor.index('#')].strip()

        diccionario_variables[clave] = valor.replace('\n', '')

    return diccionario_variables


def make_vars_dict(ruta_archivo: str) -> Dict[str, str]:
    """
    Genera un diccionario con las variables del archivo enviado por 
    parametro parseadas con sus respectivas variables de ambiente
    """
    default_vars = _make_vars_dict_by_env_file(ruta_archivo)
    return parse_env_vars(default_vars)