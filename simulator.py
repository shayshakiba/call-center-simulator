import sys
from time import sleep
from threading import Thread
from random import choice
from queue import Queue


class Operator(Thread):
    work_duration = 0

    def __init__(self, name):
        Thread.__init__(self)

        self.name = name

    def run(self):
        while not callers.empty():
            customer = callers.get()

            self.handle_caller(customer)

            self.take_a_break()

    def handle_caller(self, caller):
        print(
            f'{self.name} answered a call from {caller.name} categorized as {caller.call_category}...')

        if caller.call_category == 'customer_service':
            call_duration = 0.3
        elif caller.call_category == 'technical_support':
            call_duration = 0.5
        elif caller.call_category == 'sales_support':
            call_duration = 0.2

        if caller.has_weak_signal:
            call_duration += 0.1

        sleep(call_duration)

        print(
            f'{self.name} finished talking to {caller.name} after {round(call_duration, 1)} second(s).')

        self.work_duration += call_duration

        # the caller is directed to fill the survey
        caller.start()

    def take_a_break(self):
        print(f'{self.name} took a break...')

        break_duration = 0.1
        if self.need_extended_break():
            break_duration += 0.5

            self.work_duration = 0

        sleep(break_duration)

        print(f'{self.name} returned after {round(break_duration, 1)} second(s).')

    def need_extended_break(self):
        return self.work_duration > 1.0


class Caller(Thread):
    def __init__(self, name, call_category, has_weak_signal):
        Thread.__init__(self)

        self.name = name
        self.call_category = call_category
        self.has_weak_signal = has_weak_signal

    def run(self):
        self.fill_survey()

        if self.want_to_send_feedback():
            self.send_feedback()

        print(f'{self.name} ended the call.')

    def fill_survey(self):
        print(f'{self.name} started filling survey...')

        sleep(0.1)

        print(f'{self.name} finished filling survey.')

    def send_feedback(self):
        print(f'{self.name} started sending feedback...')

        sleep(0.2)

        print(f'{self.name} finished sending feedback.')

    def want_to_send_feedback(self):
        return choice([True, False])


def initialize_operators(input_file):
    number_of_operators = int(input_file.readline().strip())

    for operator_index in range(1, number_of_operators + 1):
        operators.append(Operator(f'Operator {operator_index}'))


def initialize_callers(input_file):
    for line in input_file:
        caller_info = line.strip().split(" ")

        # gets the caller's name and their call category
        name, call_category = caller_info[0:2]

        # checks if the caller has a weak signal
        has_weak_signal = 'weak_signal' in caller_info[2:]

        callers.put(Caller(name, call_category, has_weak_signal))


def start_operators():
    for operator in operators:
        operator.start()


def simulate_call_center(input_file_path):
    with open(input_file_path, 'r') as input_file:
        initialize_operators(input_file)
        initialize_callers(input_file)

    start_operators()


if __name__ == '__main__':
    global operators, callers

    operators = []
    callers = Queue()

    simulate_call_center(sys.argv[1])
