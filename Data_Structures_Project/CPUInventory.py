
from CPU import Cpu
from sorting_list import SortingAlgorithms


class CpuInventory:
    def __init__(self):
        self.__list_cpu = []  # Creating the list of CPUs

    def search_price(self, price):
        cpu_temp = []  # creates a list object to store CPUs below the price ceiling
        lowest_cpu = []  # creates a list for containing the lowest priced cpu
        lowest_price = 1000000  # creates a variable for storing the lowest price if the user input is too low
        cpu_temp.clear()
        for cpu in self.__list_cpu:
            if cpu.get_price() <= price:
                cpu_temp.append(cpu)
            else:
                if cpu.get_price() <= lowest_price:
                    lowest_price = cpu.get_price()
                    if not lowest_cpu:
                        lowest_cpu.append(cpu)
                    else:
                        lowest_cpu.pop(0)
                        lowest_cpu.append(cpu)
        if not cpu_temp:
            cpu_temp.extend(lowest_cpu)
        return cpu_temp

    def search_maxclock(self, maxclock):
        cpu_temp = []
        above_cpu = []
        above_max = 0
        for cpu in self.__list_cpu:
            if cpu.get_maxclock() >= maxclock:
                cpu_temp.append(cpu)
            else:
                if cpu.get_maxclock() >= above_max:
                    above_max = cpu.get_maxclock()
                    if not above_cpu:
                        above_cpu.append(cpu)
                    else:
                        above_cpu.pop(0)
                        above_cpu.append(cpu)
        if not cpu_temp:
            cpu_temp.extend(above_cpu)
        return cpu_temp

    def search_TDP(self, TDP):
        cpu_temp = []
        lowest_cpu = []
        lowest_TDP = 1000000
        for cpu in self.__list_cpu:
            if cpu.get_TDP() <= TDP:
                cpu_temp.append(cpu)
            else:
                if cpu.get_TDP() <= lowest_TDP:
                    lowest_TDP = cpu.get_TDP()
                    if not lowest_cpu:
                        lowest_cpu.append(cpu)
                    else:
                        lowest_cpu.pop(0)
                        lowest_cpu.append(cpu)
        if not cpu_temp:
            cpu_temp.extend(lowest_cpu)
        return cpu_temp

    def search_brand(self, brand):
        cpu_temp = []
        for cpu in self.__list_cpu:
            if cpu.get_brand().lower() == brand.lower():
                cpu_temp.append(cpu)
        return cpu_temp

    def create_inventory(self, cpu_file):
        with open(cpu_file) as file:
            for line in file:
                cpu_data = line.strip().split(', ')
                cpu = Cpu()
                cpu.set_ID(int(cpu_data[0]))
                cpu.set_name(cpu_data[1])
                cpu.set_price(int(cpu_data[2]))
                cpu.set_maxclock(float(cpu_data[3]))
                cpu.set_TDP(int(cpu_data[4]))
                cpu.set_brand(cpu_data[5])
                self.__list_cpu.append(cpu)

    def sort_cpu_by_benchmark(self):
        SortingAlgorithms.merge_sort(self.__list_cpu, key=lambda x: x.get_maxclock())

    def display_inventory(self):
        for cpu in self.__list_cpu:
            cpu.prnt_CPU()
