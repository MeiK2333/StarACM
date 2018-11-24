from enum import Enum

from sqlalchemy import Column, Date, DateTime, Integer, String

from StarAcmSpider.db import Base


class Result(Enum):
    RUNNING = -1
    AC = 0
    WA = 1
    TLE = 2
    MLE = 3
    RE = 4
    OLE = 5
    CE = 6
    PE = 7
    OTHER = 233
    SE = 666


class Language(Enum):
    C = 0
    CPP = 1
    JAVA = 2
    PYTHON = 3
    CSHARP = 4
    RUBY = 5
    GO = 6
    PASCAL = 7
    LUA = 8
    HASKELL = 9
    PERL = 10
    JAVASCRIPT = 11
    SWIFT = 12
    SCALA = 13
    KOTLIN = 14
    DELPHI = 15
    NODEJS = 16
    D = 17
    FORTRAN = 18
    PHP = 666
    OTHER = 233


class Solution(Base):
    __tablename__ = 'solutions'

    source = Column(String(64), primary_key=True)
    run_id = Column(String(64), primary_key=True)
    username = Column(String(64), index=True)

    problem_id = Column(String(64))
    result = Column(Integer)  # Result
    time = Column(Integer)
    memory = Column(Integer)
    language = Column(Integer)  # Language
    code_length = Column(Integer)

    submission_time = Column(DateTime)  # like '2015-10-10 18:25:33'