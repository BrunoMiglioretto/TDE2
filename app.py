from datetime import datetime

from models import Person, Professional
from services.database import session
from utils.database_utils import create_db

from sqlalchemy import select


def create_people():
    people = [Person(
        name="Bruno Miglioretto",
        cpf="06411448908",
        zip="70040912",
        street="Rua dos santos",
        street_number=12,
        complement="APT 239",
        neighborhood="Boa vista",
        city="Curitiba",
        state="PR",
        country="BRL",
        phone="+5541996438691",
        email="bruno@exemple.com",
    ), Person(
        name="João da Silva",
        cpf="31076567045",
        zip="74120080",
        street="Rua 18",
        street_number=12,
        complement=None,
        neighborhood="Boa vista",
        city="Curitiba",
        state="PR",
        country="BRL",
        phone="+5541396438691",
        email="joao@exemple.com",
    ), Person(
        name="John Smith",
        cpf="98765432109",
        zip="543210",
        street="Maple Avenue",
        street_number=30,
        complement="Suite 101",
        neighborhood="Downtown",
        city="Metropolis",
        state="CA",
        country="USA",
        phone="+1122334455",
        email="john@example.com"
    ), Person(
        name="Maria Garcia",
        cpf="34567891234",
        zip="654321",
        street="Oak Street",
        street_number=55,
        complement="",
        neighborhood="West End",
        city="Riverside",
        state="CA",
        country="USA",
        phone="+1987654321",
        email="maria@example.com"
    ), Person(
        name="Luis Rodriguez",
        cpf="78901234567",
        zip="987654",
        street="Pine Street",
        street_number=88,
        complement="APT 305",
        neighborhood="East Side",
        city="Springfield",
        state="IL",
        country="USA",
        phone="+1654321879",
        email="luis@example.com"
    ), Person(
        name="Sophia Johnson",
        cpf="56789012345",
        zip="234567",
        street="Cedar Lane",
        street_number=18,
        complement="",
        neighborhood="North End",
        city="Hill Valley",
        state="CA",
        country="USA",
        phone="+1555123456",
        email="sophia@example.com"
    )]

    session.add_all(people)
    session.commit()


def create_professional():
    stmt = select(Person)
    people = [person for person in session.scalars(stmt)]

    professionals = [Professional(
        enrollment="AKDFJKKKD",
        salary=10000,
        start_date=datetime.now(),
        working_range="Junior",
        speciality="Cardio",
        consultation_fee=80,
        person=people[0],
    ), Professional(
        enrollment="JKLFJSDFE",
        salary=12000,
        start_date=datetime.now(),
        working_range="Senior",
        speciality="Neurology",
        consultation_fee=100,
        person=people[1],
    ), Professional(
        enrollment="IODFJNSDF",
        salary=9500,
        start_date=datetime.now(),
        working_range="Mid-Level",
        speciality="Dermatology",
        consultation_fee=90,
        person=people[2],
    ), Professional(
        enrollment="ALSKDFJSD",
        salary=11000,
        start_date=datetime.now(),
        working_range="Junior",
        speciality="Oncology",
        consultation_fee=85,
        person=people[3],
    ), Professional(
        enrollment="POIUERLKJ",
        salary=11500,
        start_date=datetime.now(),
        working_range="Senior",
        speciality="Orthopedics",
        consultation_fee=110,
        person=people[4],
    ), Professional(
        enrollment="QWERTYUIO",
        salary=10500,
        start_date=datetime.now(),
        working_range="Mid-Level",
        speciality="Gynecology",
        consultation_fee=95,
        person=people[5],
    )]

    session.add_all(professionals)
    session.commit()


if __name__ == "__main__":
    print("Creating database...")
    create_db()

    # create_people()
    create_professional()
