"""Vacancy: https://kaliningrad.hh.ru/vacancy/50927402."""
from random import randrange
from hashlib import sha256
import asyncio
import sys


async def my_info(name='Unspecified', vacancy=None, salary=None):

    """
    :param str name: employer name;
    :param str vacancy: vacancy title;
    :param int salary: salary in rubles;
    # noqa: DAR101
    """

    # script that runs asynchronous tasks
    print('Name:', name)
    await asyncio.sleep(randrange(5))
    print('Vacancy:', vacancy)
    await asyncio.sleep(randrange(5))
    print('Salary:', salary)

    # script read stdin and output sha256
    for info in sys.stdin:
        print('Entered data:', sha256(info.encode('utf-8')).hexdigest().rstrip('\n'))

asyncio.run(my_info(name='Vladislav Henkel',
vacancy='Python Developer Trainee', salary=35000))
