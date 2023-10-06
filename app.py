from datetime import datetime

from models import Person, Professional, Patient
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
    ), Person(
        name="Eva Johnson",
        cpf="98765432100",
        zip="543210",
        street="Willow Street",
        street_number=22,
        complement="Suite 301",
        neighborhood="Downtown",
        city="Metropolis",
        state="CA",
        country="USA",
        phone="+1112334455",
        email="eva@example.com"
    ), Person(
        name="Daniel Brown",
        cpf="11122334455",
        zip="332211",
        street="Chestnut Avenue",
        street_number=45,
        complement="",
        neighborhood="West End",
        city="Riverside",
        state="CA",
        country="USA",
        phone="+1987614321",
        email="daniel@example.com"
    ), Person(
        name="Sophie Miller",
        cpf="22233445566",
        zip="998877",
        street="Magnolia Street",
        street_number=78,
        complement="APT 205",
        neighborhood="East Side",
        city="Springfield",
        state="IL",
        country="USA",
        phone="+1614321879",
        email="sophie@example.com"
    ), Person(
        name="William Clark",
        cpf="33344556677",
        zip="112233",
        street="Maple Lane",
        street_number=13,
        complement="",
        neighborhood="North End",
        city="Hill Valley",
        state="CA",
        country="USA",
        phone="+1555113456",
        email="william@example.com"
    ), Person(
        name="Ava Baker",
        cpf="44455667788",
        zip="334455",
        street="Pine Drive",
        street_number=36,
        complement="",
        neighborhood="South Side",
        city="Springfield",
        state="IL",
        country="USA",
        phone="+1444333222",
        email="ava@example.com"
    )]

    session.add_all(people)
    session.commit()


def create_professionals():
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


def create_patients():
    stmt = select(Person)
    people = [person for person in session.scalars(stmt)]

    patients = [Patient(
        weight=56,
        marital_status="single",
        profession="Programmer",
        emergency_contact_name="Alice",
        emergency_contact_phone="390809384",
        birth_date="2013-02-01",
        sex="m",
        health_insurance="Unimed",
        hospitalization_date="2023-10-03",
        person=people[0],
    ), Patient(
        weight=70,
        marital_status="married",
        profession="Teacher",
        emergency_contact_name="John",
        emergency_contact_phone="123456789",
        birth_date=datetime.strptime("1985-07-15", "%Y-%m-%d").date(),
        sex="f",
        health_insurance="BlueCross",
        hospitalization_date=datetime.strptime("2023-09-20", "%Y-%m-%d").date(),
        person=people[1]
    ), Patient(
        weight=85,
        marital_status="divorced",
        profession="Doctor",
        emergency_contact_name="Sarah",
        emergency_contact_phone="987654321",
        birth_date=datetime.strptime("1970-04-23", "%Y-%m-%d").date(),
        sex="m",
        health_insurance="Aetna",
        hospitalization_date=datetime.strptime("2023-11-05", "%Y-%m-%d").date(),
        person=people[2]
    ), Patient(
        weight=62,
        marital_status="single",
        profession="Engineer",
        emergency_contact_name="Michael",
        emergency_contact_phone="555123456",
        birth_date=datetime.strptime("1992-11-10", "%Y-%m-%d").date(),
        sex="f",
        health_insurance="Cigna",
        hospitalization_date=datetime.strptime("2023-10-15", "%Y-%m-%d").date(),
        person=people[3]
    ), Patient(
        weight=75,
        marital_status="married",
        profession="Nurse",
        emergency_contact_name="Emily",
        emergency_contact_phone="678987654",
        birth_date=datetime.strptime("1982-05-30", "%Y-%m-%d").date(),
        sex="m",
        health_insurance="Humana",
        hospitalization_date=datetime.strptime("2023-09-10", "%Y-%m-%d").date(),
        person=people[4]
    ), Patient(
        weight=68,
        marital_status="single",
        profession="Artist",
        emergency_contact_name="Oliver",
        emergency_contact_phone="1122334455",
        birth_date=datetime.strptime("1995-09-02", "%Y-%m-%d").date(),
        sex="f",
        health_insurance="Kaiser",
        hospitalization_date=datetime.strptime("2023-10-25", "%Y-%m-%d").date(),
        person=people[5]
    )]

    session.add_all(patients)
    session.commit()


if __name__ == "__main__":
    print("Creating database...")
    create_db()

    create_people()
    create_professionals()
    create_patients()
