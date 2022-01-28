"""Vacancy: https://kaliningrad.hh.ru/vacancy/50927402."""
import asyncio
import sys
from hashlib import sha256
from random import SystemRandom


async def my_info(name, vacancy, salary):
    """Return given values of arguments and outputs sha256 hash from the read data.

    Script, runs asynchronous tasks and displays them.
    After a random amount of time (up to 5 seconds) script outputs
    name, job title, expected salary level in a year.
    After all asynchronous tasks are done, the script reads stdin and
    outputs sha256 hash from the read data.

    Args:
        name : str
            Employee name
        vacancy : str
            Vacancy title
        salary : int
            Salary in rubles
    """
    # Outputs the values of the args
    employee_card = [name, vacancy, salary]
    for _, card_val in enumerate(employee_card):
        crypto = SystemRandom()
        await asyncio.sleep(crypto.randrange(5))
        print(card_val)

    # Reads stdin and outputs sha256 hash
    for hash_message in sys.stdin:
        print(
            'Entered data:',
            sha256(hash_message.encode('utf-8')).hexdigest().strip('\n'),
        )
        break

# Setting values for args
asyncio.run(my_info(
    name='Vladislav Henkel',
    vacancy='Python Developer Trainee',
    salary=35000,
))
