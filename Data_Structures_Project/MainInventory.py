#This file is going to be the main inventory for the CPU
#Code wrote by Amer
from CPUInventory import CpuInventory

def main_inventory():

  cInventory = CpuInventory()
  cInventory.create_inventory("CPU_Info.txt")
  price = int(input("Enter the price number: ")) #It is reading the price number and converting it to an integer
  cInventory.search_price(price) #searching for the given price
  # if cpu == None:
    # print("cpu not found")    #writing an if else statement if there's any info
 # else:                       #This is where it output the CPU's information
  #  print("cpu info: \n" + cpu.get_name() + ", \n" + cpu.get_brand() + ", \n$" + str(cpu.get_price()) + ", \n"  + cpu.get_maxclock() + "GHz, \n" + cpu.get_TDP() + 'W. \n')

#Code written by Carlos
def MCX():
  cInventory = CpuInventory()
  cInventory.create_inventory("CPU_Info.txt")
  maxclock = float(input("Enter the max clock speed: ")) #This reads the max clock speed and converts it into an integer.
  cInventory.search_maxclock(maxclock)

def TDP():
  cInventory = CpuInventory()
  cInventory.create_inventory("CPU_Info.txt")
  TDP = int(input("Enter the TDP: ")) #used maxclock instead of tdp -eric
  cInventory.search_TDP(TDP) #used maxclock instead of tdp -eric

#Code by Eric
def BRD():
  cInventory = CpuInventory()
  cInventory.create_inventory("CPU_Info.txt")
  Brand = int(input("Enter 1 for Intel, 2 for AMD: \n"))
  if Brand == 1: #checks if the user selected intel case
    BRD = str("Intel")
    cInventory.search_brand(BRD)
  elif Brand == 2: #otherwise does amd case
    BRD = str("AMD")
    cInventory.search_brand(BRD)
  else:
    print("Invalid Input. Would you like to try again? \n")