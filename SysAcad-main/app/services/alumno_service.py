from app.models import Alumno
from app.repositories.alumno_repositorio import AlumnoRepository

class AlumnoService:
    """
    Servicio para gestionar las Alumno.
    """
    @staticmethod
    def crear_alumno(alumno: Alumno):
        """
        Crea una nueva alumno en la base de datos.
        :param alumno: Alumno a crear.
        :return: Alumno creada.
        """
        AlumnoRepository.crear(alumno)
    
    @staticmethod
    def buscar_por_id(id: int) -> Alumno:
        """
        Busca una alumno por su ID.
        :param id: ID de la Alumno a buscar.
        :return: Alumno encontrada o None si no se encuentra.
        """
        return AlumnoRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Alumno]:
        """
        Busca todas las alumno en la base de datos.
        :return: Lista de alumno.
        """
        return AlumnoRepository.buscar_todos()
    
    @staticmethod
    def actualizar_alumno(id: int, alumno: Alumno) -> Alumno:
        """
        Actualiza una alumno existente en la base de datos.
        :param id: ID de la alumno a actualizar.
        :param alumno: Objeto Alumno con los nuevos datos.
        :return: Objeto Alumno actualizada.
        """
        alumno_existente = AlumnoRepository.buscar_por_id(id)
        if not alumno_existente:
            return None
        alumno_existente.nombre = alumno.nombre
        alumno_existente.apellido = alumno.apellido
        alumno_existente.nro_legajo = alumno.nro_legajo
        alumno_existente.nro_documento = alumno.nro_documento
        alumno_existente.fecha_nacimiento = alumno.fecha_nacimiento
        alumno_existente.sexo = alumno.sexo
        alumno_existente.fecha_ingreso = alumno.fecha_ingreso
        return alumno_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Alumno:
        """
        Borra una alumno por su ID.
        :param id: ID de la alumno a borrar.
        :return: Objeto Alumno borrado o None si no se encuentra.
        """

        alumno = AlumnoRepository.borrar_por_id(id)
        if not alumno:
            return None

        return alumno

#pregunta 4
#pip install reportlab
#pip install json
#primero instalamos las bibliotecas necesarias para la nueva funcionalidad
#luego en este archivo creo las nuevas funciones de la consigna
from app.models.alumno import Alumno
from app.models.facultad import Facultad
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import json

class AlumnoService:
    def __init__(self):
        self.alumnos = Alumno.query.all()
        self.facultades = Facultad.query.all()

    def get_alumno(self, id):
        return Alumno.query.get(id)

    def get_facultad(self, id):
        return Facultad.query.get(id)

    def generar_pdf(self, id):
        alumno = self.get_alumno(id)
        facultad = self.get_facultad(alumno.facultad_id)
        c = canvas.Canvas("alumno.pdf", pagesize=letter)
        c.drawString(100, 750, "Nro de Legajo: " + str(alumno.nro_legajo))
        c.drawString(100, 700, "Apellido y Nombre: " + alumno.apellido + ", " + alumno.nombre)
        c.drawString(100, 650, "Facultad: " + facultad.nombre)
        c.save()

    def generar_json(self, id):
        alumno = self.get_alumno(id)
        facultad = self.get_facultad(alumno.facultad_id)
        data = {
            "nro_legajo": alumno.nro_legajo,
            "apellido": alumno.apellido,
            "nombre": alumno.nombre,
            "facultad": facultad.nombre
        }
        return json.dumps(data)
