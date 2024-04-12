# Python Lab (CS500L)/Week:01/Lab:01/Q:05
# 20099_MANIRUZZAMAN_MD
# A hotel offers various room types with different pricing structures .....

print("Calculate the hotel bill:")

# Define Consents
STD_RM_RATE_1 = 155
STD_RM_RATE_2 = 160
STD_RM_RATE_3 = 165

DL_RM_RATE_1 = 195
DL_RM_RATE_2 = 210
DL_RM_RATE_3 = 225

ROOM_TAX = 0.12
BREAKFAST = 15
PARKING = 25

DISCOUNT_5_NIGHTS = 0.9

# Get user inputs
room_type = input("Enter room type (Standard or Deluxe) : ").lower()
num_nights = int(input("Enter number of nights               : "))
num_people = int(input("Enter number of people               : "))
breakfast = input("Would you like to take breakfast? (y/n)").lower()
parking = input("Do you need parking? (y/n)").lower()

# Figure out the room rate
if room_type =="standard":
    if num_people == 1:
        room_rate = STD_RM_RATE_1
    elif num_people == 2:
        room_rate = STD_RM_RATE_2
    else:
        room_rate = STD_RM_RATE_3
elif room_type == "deluxe":
    if num_people <=2:
        room_rate = DL_RM_RATE_1
    elif num_people == 3:
        room_rate = DL_RM_RATE_2
    else:
        room_rate = DL_RM_RATE_3
else:
    print ("Invalid room type")

if room_rate is not None:
    # Calculate the room charge
    room_charges = room_rate * num_nights
    if num_nights > 5:
        discount_amount = room_charges * (1 - DISCOUNT_5_NIGHTS)
        room_charges -= discount_amount
    else:
        discount_amount = 0

    # Calculate breakfast
    if breakfast == "y":
        breakfast_charge = num_people * num_nights * BREAKFAST
    elif breakfast == "n":
        breakfast_charge = 0
    else:
        print ("Invalid breakfast")

    # Calculate parking fees
    if parking == 'y':
        parking_fee = num_nights * PARKING
    elif parking == "n":
        parking_fee = 0
    else:
        print ("Invalid parking")

    # Calculate the charges

    room_charges = num_nights * room_rate
    discounted_room_charge = room_charges - discount_amount
    room_charges_with_tax = discounted_room_charge * ROOM_TAX
    total_charges = room_charges_with_tax + breakfast_charge + parking_fee + discounted_room_charge
    sub_total_before_tax = discounted_room_charge + breakfast_charge + parking_fee

    # Print the complete hotel bill
    print("\n")
    print("Hotel Bill:",)
    print(f"Room type                                  : {room_type}")
    print(f"Number of nights                           : {num_nights}")
    print(f"Number of people                           : {num_people}")
    print(f"Room charges (sub-total)                   : ${room_charges:.2f}")
    print(f"Discount Applied for stay over 5 nights    :-${discount_amount:.2f}")
    print(f"Total room charge after discount           : ${discounted_room_charge:.2f}")
    print(f"Breakfast charges                          : ${breakfast_charge:.2f}")
    print(f"Parking fees                               : ${parking_fee:.2f}")
    print(f"Sub-total (without TAX)                    : ${sub_total_before_tax:.2f}")
    print(f"TAX on room charges                        : ${room_charges_with_tax:.2f}")
    print("\n")
    print(f"Total amount (including TAX and fees)      : ${total_charges:.2f}")
else:
    print("Invalid room type.")