from datetime import datetime
from enum import Enum
from typing import List
from uuid import UUID

from logic.apps.models.modelos import Archivo, TipoArchivo
from logic.libs.excepcion.excepcion import AppException
from logic.libs.sqlite import sqlite

_TABLA = 'ARCHIVOS'


def listado_archivos(id_modelo: any, tipo: TipoArchivo = TipoArchivo.MODELO) -> List[str]:
    """
    Muestra los nombres de los archivos de ese modelo
    """
    consulta = f'SELECT NOMBRE FROM {_TABLA} WHERE ID_MODELO = ? AND TIPO = ?'
    resultado = sqlite.select(consulta, parametros=[id_modelo, tipo.value])
    return [r[0] for r in resultado]


def crear(a: Archivo) -> Archivo:
    """
    Crea un Archivo con sus archivos en la base de datos
    """
    consulta = f"""
        INSERT INTO {_TABLA} (NOMBRE, FECHA_CREACION, UUID_GUARDADO, TIPO, ID_MODELO)
        VALUES (?,?,?,?,?)
    """
    parametros = [a.nombre, a.fecha_creacion,
                  str(a.uuid_guardado), a.tipo.value, a.id_modelo]

    a.id = sqlite.insert(consulta, parametros=parametros)
    return a


def actualizar(a: Archivo) -> Archivo:
    """
    Actualiza un Archivo en la base de datos
    """
    consulta = f"""
        UPDATE {_TABLA}
        SET NOMBRE=?, FECHA_CREACION=?, UUID_GUARDADO=?, TIPO=?, ID_MODELO=?
        WHERE ID = ?
    """
    parametros = [a.nombre, a.fecha_creacion,
                  a.uuid_guardado, a.tipo.value, a.id_modelo, a.id]
    sqlite.ejecutar(consulta, parametros=parametros, commit=True)
    return a


def buscar(id: any) -> Archivo:
    """
    Busca un Archivo por id
    """
    consulta = f"""
        SELECT *
        FROM {_TABLA}
        WHERE ID = ?
    """
    r = sqlite.select(consulta, parametros=[id])
    if not r:
        return None
    r = r[0]
    a = Archivo(id=r[0], nombre=r[1], fecha_creacion=datetime.fromisoformat(r[2]),
                uuid_guardado=UUID(r[3]), tipo=TipoArchivo[r[4]], id_modelo=r[5])
    return a


def buscar_por_filtros(filtros: dict = None) -> List[Archivo]:
    """
    Busca Archivos que cumplan con el filtro
    """
    consulta = f"""
        SELECT * FROM {_TABLA}
    """
    parametros = []
    if filtros:
        consulta += ' WHERE '
        for k, v in filtros.items():
            consulta += f'{str(k).upper()}=? AND '
            parametros.append(v)

    consulta = consulta[:-len(' AND ')]
    resultados = sqlite.select(consulta, parametros=parametros)

    archivos = []
    for r in resultados:
        archivos.append(Archivo(id=r[0], nombre=r[1], fecha_creacion=datetime.fromisoformat(r[2]),
                                uuid_guardado=r[3], tipo=TipoArchivo[r[4]], id_modelo=r[5]))

    return archivos


def borrar(id: any):
    """
    Borra un Archivo por id
    """
    consulta = f"""
        DELETE FROM {_TABLA}
        WHERE ID = ?
    """
    r = sqlite.ejecutar(consulta, parametros=[id], commit=True)
