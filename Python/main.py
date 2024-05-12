from dao.ICarLeaseRepositoryImpl import ICarLeaseRepositoryImpl as I
from model import *
from datetime import datetime
from myexception import *
import pyodbc
from tabulate import tabulate

def carManagementMenu():

    print("---------------CAR MANAGER MENU---------------")
    print("1. Add a car")
    print("2. Remove a car")
    print("3. List available cars")
    print("4. List rented cars")
    print("5. Find a car by ID")
    print("6. Back to main menu")
    print("----------------------------------------------")


def customerManagementMenu():
    print("------------CUSTOMER MANAGER MENU--------------")
    print("1. Add a customer")
    print("2. Remove a customer")
    print("3. List customers")
    print("4. Find a customer by ID")
    print("5. Back to main menu")
    print("----------------------------------------------")


def leaseManagementMenu():
    print("-------------LEASE MANAGER MENU---------------")
    print("1. Create a lease")
    print("2. Return a car")
    print("3. List active leases")
    print("4. List lease history")
    print("5. Back to main menu")
    print("----------------------------------------------")


def paymentManagementMenu():
    print("------------PAYMENT MANAGER MENU--------------")
    print("1. Pay for a lease")
    print("2. Back to main menu")
    print("----------------------------------------------")


def mainMenu():
    print("===============================================")
    print("Welcome to the Car Lease Management System")
    print("1. Car management")
    print("2. Customer management")
    print("3. Lease management")
    print("4. Payment management")
    print("5. Exit")
    print("===============================================")


def main():
    while True:
        mainMenu()
        choice = int(input("Please Select a Option to Continue: "))
        if choice == 1:
            while True:
                carManagementMenu()
                print()
                option = int(input("Please Select a Option to Continue... "))

                # Add a car
                if option == 1:
                    car = Vehicle()
                    try:
                        print("Car Entry")
                        print()
                        car.make = input("Enter Car Make: ")
                        car.model = input("Enter Car Model: ")
                        car.year = input("Enter Car Year: ")
                        car.dailyrate = float(input("Enter Car Daily Rate: "))
                        car.status = input("Enter Car Status: ")
                        car.passengerCapacity = int(
                            input("Enter Car Passenger Capacity: ")
                        )
                        car.engineCapacity = float(input("Enter Car Engine Capacity: "))
                        I.CarManagement().addCar(car)
                    except ValueError as e:
                        print()
                        print(f"Invalid input: {e}")
                    except Exception as e:
                        print()
                        print(f"An error occurred while inserting in database: {e}")
                    else:
                        print()
                        print(f"Car details: {car} - Car Added Successfully")

                # Remove a car
                elif option == 2:
                    car = Vehicle()
                    try:
                        print("Car Removal")
                        print()
                        car.id = int(input("Enter Car ID: "))
                        I.CarManagement().removeCar(car.id)
                    except ValueError as e:
                        print()
                        print(f"Invalid input: {e}")
                    except Exception as e:
                        print(f"No Records Found: {e}")
                    else:
                        print()
                        print(f"Car-ID: {car.id} - Car Removed Successfully")

                # List available cars
                elif option == 3:
                    result = I.CarManagement().listAvailableCars()
                    table = tabulate(result, headers="firstrow", tablefmt="fancy_grid")
                    print(table)

                # List rented cars
                elif option == 4:
                    result = I.CarManagement().listRentedCars()
                    table = tabulate(result, headers="firstrow", tablefmt="fancy_grid")
                    print(table)

                # Find a car by ID
                elif option == 5:
                    try:
                        print("Car Search")
                        print()
                        car = Vehicle()
                        car.id = int(input("Enter Car ID: "))
                    except ValueError as e:
                        print()
                        print(f"Invalid input: {e}")
                    except Exception as e:
                        print()
                        print(f"No Records Found: {e}")
                    else:
                        result = I.CarManagement().findCarByID(car.id)
                        table = tabulate(result, headers="firstrow", tablefmt="fancy_grid")
                        print(table)

                # Back to main menu
                elif option == 6:
                    break

        # Customer Management
        elif choice == 2:
            while True:

                customerManagementMenu()
                option = int(input("Please Select a Option to Continue... "))

                # Add a customer
                if option == 1:
                    customer = Customer()
                    try:
                        print("Customer Entry")
                        print()
                        customer.id = int(input("Enter Customer ID: "))
                        customer.firstname = input("Enter Customer First Name: ")
                        customer.lastname = input("Enter Customer Last Name: ")
                        customer.email = input("Enter Customer Email: ")
                        customer.phone = input("Enter Customer Phone: ")
                        I.CustomerManagement().addCustomer(customer)
                    except ValueError as e:
                        print()
                        print(f"Invalid input: {e}")
                    except Exception as e:
                        print()
                        print(f"An error occurred while inserting in database: {e}")
                    else:
                        print()
                        print(
                            f"Customer details: {customer} - Customer Added Successfully"
                        )

                # Remove a customer
                elif option == 2:
                    customer = Customer()
                    try:
                        print("Customer Removal")
                        print()
                        customer.id = int(input("Enter Customer ID: "))
                        if I.CustomerManagement().findCustomerByID(customer.id) == []:
                            raise CustomerNotFoundException("Customer not found")
                        I.CustomerManagement().removeCustomer(customer.id)
                    except ValueError as e:
                        print()
                        print(f"Invalid input: {e}")
                    except Exception as e:
                        print()
                        print(f"No Records Found: {e}")
                    else:
                        print()
                        print(
                            f"Customer-ID: {customer.id} - Customer Removed Successfully"
                        )

                # List customers
                elif option == 3:
                    result = I.CustomerManagement().listCustomers()
                    table = tabulate(result, headers="firstrow", tablefmt="fancy_grid")
                    print(table)

                # Find a customer by ID
                elif option == 4:
                    customer = Customer()
                    try:
                        print("Customer Search")
                        print()
                        customer.id = int(input("Enter Customer ID: "))
                        result = I.CustomerManagement().findCustomerByID(customer.id)
                    except ValueError as e:
                        print()
                        print(f"Invalid input: {e}")
                    except Exception as e:
                        try:
                            raise CustomerNotFoundException(customer.id)
                        except CustomerNotFoundException as e:
                            print()
                            print(f"No Records Found: {e}")
                    else:
                        table = tabulate(result, headers="firstrow", tablefmt="fancy_grid")
                        print(table)

                # Back to main menu
                elif option == 5:
                    break

        # Lease Management
        elif choice == 3:

            while True:
                leaseManagementMenu()
                option = int(input("Please Select a Option to Continue... "))

                # Create a lease
                if option == 1:
                    lease = Lease()
                    try:
                        print("Lease Entry")
                        print()
                        lease.customerId = int(input("Enter Customer ID: "))
                        lease.vehicleId = int(input("Enter Vehicle ID: "))
                        lease.startDate = input("Enter Start Date: ")
                        lease.type = input("Enter Lease Type: ")

                        # Check if car and customer exists
                        if I.CarManagement().findCarByID(lease.vehicleId) == []:
                            raise CarNotFoundException(lease.vehicleId)

                        if (
                            I.CustomerManagement().findCustomerByID(lease.customerId)
                            == []
                        ):
                            raise CustomerNotFoundException(lease.customerId)

                        I.LeaseManagement().createLease(lease)
                    except ValueError as e:
                        print()
                        print(f"Invalid input: {e}")
                    except Exception as e:
                        print()
                        print(f"An error occurred while inserting in database: {e}")
                    else:
                        print()
                        print(f"Lease details: {lease} - Lease Created Successfully")

                # Return a car
                elif option == 2:
                    lease = Lease()
                    try:
                        print("Car Return")
                        print()
                        lease.id = int(input("Enter Lease ID: "))
                        lease.endDate = str(datetime.now().date())

                        # Check if lease exists
                        if I.LeaseManagement().findLeaseByID(lease.id) == []:
                            raise LeaseNotFoundException(lease.id)

                        I.LeaseManagement().returnCar(lease.id)
                    except ValueError as e:
                        print()
                        print(f"Invalid input: {e}")
                    except Exception as e:
                        print()
                        print(f"No Records Found: {e}")
                    else:
                        print()
                        print(f"Lease-ID: {lease.id} - Car Returned Successfully")

                # List active leases
                elif option == 3:
                    result = I.LeaseManagement().listActiveLeases()
                    table = tabulate(result, headers="firstrow", tablefmt="fancy_grid")
                    print(table)

                # List lease history
                elif option == 4:
                    result = I.LeaseManagement().listLeaseHistory()
                    table = tabulate(result, headers="firstrow", tablefmt="fancy_grid")
                    print(table)

                # Back to main menu
                elif option == 5:
                    break

        elif choice == 4:
            while True:
                paymentManagementMenu()
                option = int(input("Please Select a Option to Continue... "))

                # Pay for a lease
                if option == 1:
                    payment = Payment()
                    try:
                        print("Payment Entry")
                        print()
                        payment.leaseId = int(input("Enter Lease ID: "))
                        payment.amount = float(input("Enter Payment Amount: "))
                        payment.paymentDate = input("Enter Payment Date: ")
                        I.PaymentManagement().payLease(payment)
                    except ValueError as e:
                        print()
                        print(f"Invalid input: {e}")
                    except pyodbc.IntegrityError as e:
                        try:
                            raise LeaseNotFoundException(payment.leaseId)
                        except LeaseNotFoundException as e:
                            print()
                            print(e)
                    else:
                        print(
                            f"Payment details: {payment} - Payment Recorded Successfully"
                        )

                # Back to main menu
                elif option == 2:
                    break

        # Exit
        elif choice == 5:
            print("Thank you for using the Car Lease Management System")
            exit()


if __name__ == "__main__":

    print("""
░█████╗░░█████╗░██████╗░  ██████╗░███████╗███╗░░██╗████████╗░█████╗░██╗░░░░░
██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔════╝████╗░██║╚══██╔══╝██╔══██╗██║░░░░░
██║░░╚═╝███████║██████╔╝  ██████╔╝█████╗░░██╔██╗██║░░░██║░░░███████║██║░░░░░
██║░░██╗██╔══██║██╔══██╗  ██╔══██╗██╔══╝░░██║╚████║░░░██║░░░██╔══██║██║░░░░░
╚█████╔╝██║░░██║██║░░██║  ██║░░██║███████╗██║░╚███║░░░██║░░░██║░░██║███████╗
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝

░██████╗██╗░░░██╗░██████╗████████╗███████╗███╗░░░███╗
██╔════╝╚██╗░██╔╝██╔════╝╚══██╔══╝██╔════╝████╗░████║
╚█████╗░░╚████╔╝░╚█████╗░░░░██║░░░█████╗░░██╔████╔██║
░╚═══██╗░░╚██╔╝░░░╚═══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║
██████╔╝░░░██║░░░██████╔╝░░░██║░░░███████╗██║░╚═╝░██║
╚═════╝░░░░╚═╝░░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝""")
    main()
