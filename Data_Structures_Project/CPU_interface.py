# CPUInterface.py

import os
from CPUInventory import CpuInventory

class Interface:

    @staticmethod
    def Cpuinterface_cl():
        print("===================================")
        print("WELCOME TO THE CPU INVENTORY SYSTEM")
        print("===================================")

        cInventory = CpuInventory()
        cInventory.create_inventory("CPU_Info.txt")

        running = True

        while running:
            print("[0] - Exit program")
            print("[1] - Search for CPUs below a certain price")
            print("[2] - Search for CPUs above a certain max clock speed")
            print("[3] - Search for CPUs below a certain max power draw")
            print("[4] - Search for CPUs based on brand")
            print("[5] - Show all items")

            option = int(input("Please pick from 0-5: "))

            if option == 0:
                print("Thank you, have a nice day!")
                running = False
            elif option == 1:
                price = int(input("Enter the maximum price number in dollars you want to see: "))
                priceR = cInventory.search_price(price)
                Interface.print_cpu_list(priceR)
            elif option == 2:
                maxclock = float(input("Enter the lowest clock speed in gigahertz you want to see: "))
                maxclockR = cInventory.search_maxclock(maxclock)
                Interface.print_cpu_list(maxclockR)
            elif option == 3:
                TDP = int(input("Enter the maximum power draw in watts you want to see: "))
                TDPR = cInventory.search_TDP(TDP)
                Interface.print_cpu_list(TDPR)
            elif option == 4:
                brand = int(input("Enter 1 for Intel, 2 for AMD: "))
                if brand == 1:
                    BRD = str("Intel")
                elif brand == 2:
                    BRD = str("Amd")
                else:
                    print("Invalid Input.")
                    continue
                brandR = cInventory.search_brand(BRD)
                Interface.print_cpu_list(brandR)
            elif option == 5:
                CPU_info = open("CPU_InfoALL.txt")
                file_content = CPU_info.read()
                print(file_content + "\n")
                OF = option
                option = 15
            else:
                print("Invalid Input.")

    @staticmethod
    def print_cpu_list(cpu_list):
        if len(cpu_list) == 0:
            print("No CPUs found.")
        else:
            print("Here are the CPUs:")
            for cpu in cpu_list:
                cpu.prnt_CPU()
        input("Press Enter to return to the main menu.")
        os.system('clear')  # Use 'cls' on Windows

if __name__ == "__main__":
    Interface.Cpuinterface_cl()
