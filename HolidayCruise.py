def flight_Destination_Price(numOf_Passengers, flightDist_KM, direct_Flight, flightDuration_DAYS, Airline, Airport_Terminal):                    ##Defines conditions for the flight to holiday destination where the cruise will sail from
    FlightPrice = (numOf_Passengers * (flightDist_KM * direct_Flight * flightDuration_DAYS * Airline) * Airport_Terminal)
    return FlightPrice


numOfPassengers = int(raw_input("Please enter number of passengers you wish to book for your flight:"))
infantPassengers = int(raw_input("How many passengers you wish to book are of 2 years of age or under:"))
totalPassengers = numOfPassengers - infantPassengers
print("TOTAL FLIGHT PASSENGERS booked: " + str(totalPassengers))



FlightDistance = float(raw_input("Enter the distance you will travel (km):"))
FlightDistancePrice = FlightDistance / 3


directReturnFlightPrice = 0

directReturnFlight = raw_input("Do wish to book a direct flight? (Yes/No):")
if directReturnFlight == 'Yes':
    directReturnFlightPrice = float(1.35)
else:
    directReturnFlightPrice = float(1)

FlightDuration = float(raw_input("Enter the duration of your flight (Hrs):"))
FlightDurationDays = FlightDuration / 24

AirlineCompany = raw_input("From the following list of Airlines:\n\n British Airways\n Virgin Atlantic\n Norwegian Air\n Qatar Airways\n Emirates\n EgyptAir\n Thomas Cook\n Air Malaysia\n Air Baltic\n Canada Air\n Ryanair\n Turkish Airlines\n\nEnter the Airline Company you wish to book with:")
if AirlineCompany == 'British Airways':
    AirlineCompany = 1.25
elif AirlineCompany == 'Virgin Atlantic':
    AirlineCompany = 1.32
elif AirlineCompany == 'Norwegian Air':
    AirlineCompany = 1.15
elif AirlineCompany == 'Qatar Airways':
    AirlineCompany = 1.37
elif AirlineCompany == 'Emirates':
    AirlineCompany = 1.4
elif AirlineCompany == 'EgyptAir':
    AirlineCompany = 1.2    
elif AirlineCompany == 'Thomas Cook':
    AirlineCompany = 1.2
elif AirlineCompany == 'Air Malaysia':
    AirlineCompany = 1.22
elif AirlineCompany == 'Air Baltic':
    AirlineCompany = 1.12    
elif AirlineCompany == 'Canada Air':
    AirlineCompany = 1.19
elif AirlineCompany == 'Turkish Airlines':
    AirlineCompany = 1.29
elif AirlineCompany == 'Ryanair':
    AirlineCompany = 1.07
else:
    print("Airline company not available.")    
    

AirportTerminal = raw_input("Enter the Airport Terminal you will be departing from\n Heathrow Terminal 1\n Heathrow Terminal 2\n Heathrow Terminal 3\n Heathrow Terminal 4\n Heathrow Terminal 5\n Gatwick South\n Gatwick North\nEnter your choice here:")
if AirportTerminal == 'Gatwick South':
    AirportTerminal = 1.03
elif AirportTerminal == 'Gatwick North':
    AirportTerminal = 1.06  
elif AirportTerminal == 'Heathrow Terminal 1':
    AirportTerminal = 1.10
elif AirportTerminal == 'Heathrow Terminal 2':
    AirportTerminal = 1.15    
elif AirportTerminal == 'Heathrow Terminal 3':
    AirportTerminal = 1.11      
elif AirportTerminal == 'Heathrow Terminal 4':
    AirportTerminal = 1.13
elif AirportTerminal == 'Heathrow Terminal 5':
    AirportTerminal = 1.11

    
TotalFlightPrice = flight_Destination_Price(totalPassengers, FlightDistancePrice, directReturnFlightPrice, FlightDurationDays, AirlineCompany, AirportTerminal)
print("Flight TOTAL PRICE: £" + str(TotalFlightPrice))







#New method                     

def return_Flight_Price(TotalFlightPrice, direct_Flight, num_Of_Days, price_Per_Day):                                                  ##Defines conditions for the return flight
    returnPrice = TotalFlightPrice * (direct_Flight * (num_Of_Days * 0.02))
    return returnPrice


directReturnFlightPrice = 0

returnFlight = raw_input("Do your wish to book a return flight? (Yes/No): ")
if returnFlight == 'Yes':

    holidayDuration = float(raw_input("Enter the duration of your break (Days):"))
    returnPriceFlight = return_Flight_Price(float(TotalFlightPrice), float(directReturnFlightPrice), float(holidayDuration), float(0.02))
    print("FLIGHT PRICE: £" + str(returnPriceFlight))
else:
    holidayDuration = 0






#New Method                            

hotelPrice = 0

hotelIncluded = raw_input("Do you wish to book a hotel prior to your cruise (Yes/No):")
if hotelIncluded == 'Yes':
    def hotel(stars_Rating, price_Per_Customer, num_Of_Nights, facilities_Included, car_Park, meals_Included):                      ##Defines conditions for the hotel prior to the cruise
        hotelQuality = (stars_Rating * (price_Per_Customer * num_Of_Nights)) + facilities_Included + car_Park + meals_Included
        return hotelQuality

    hotelStars = int(raw_input("How many stars is the hotel you wish to book:"))                #The number of stars of the hotel is taken into calculation of the total price
    if hotelStars == 1:                                                                         #The higher the number of stars out of 5, the higher the price rate
        starsPrice = 0.8
    elif hotelStars == 2:
        starsPrice = 0.9
    elif hotelStars == 3:
        starsPrice = 1
    elif hotelStars == 4:
        starsPrice = 1.2
    elif hotelStars == 5:
        starsPrice = 1.4
    print("You will be booking with a " + str(hotelStars) + " star hotel.") 


    customerPrice = 0

    numOfCustomers = int(raw_input("How many of you wish to check in:"))                                    #This is to calculate the price per individual depending on the number of adults and children.
    for i in range(0, numOfCustomers):                                                                      
        adultAndOrChild = raw_input("Please enter (Adult/Child) followed by 'Enter' per person:")
        if adultAndOrChild == 'Child':
            customerPrice += float(5)
        elif adultAndOrChild == 'Adult':
            customerPrice += float(10)   
    print("Price per Child: £5.00\n Price per Adult: £10.00\n TOTAL CUSTOMER PRICE: £" + str(customerPrice) + "\n")



    pricePerNight = 0

    numOfNights = int(raw_input("How many nights do you wish to stay:"))                                                        #The customer enters the number of nights he/she wishes to stay
    if numOfNights == 1:
        pricePerNight = float(1)                                                                                                #The price rate is then calculated by dividing the No. of nights by 1.8.
    else:
        pricePerNight = round(float(numOfNights / 1.8),2)
    print("You have chosen to stay for " + str(numOfNights) + " nights at this hotel.\n Price per Night: (NO. of Nights / 1.8)\n TOTAL PRICE PER NIGHT: £" + str(pricePerNight))
        

    GymPrice = 0
    PoolPrice = 0
    JacuzziPrice = 0
    saunaPrice = 0

    totalFacilities = int(raw_input("How many of the following facilites are available (0-4)? (Gym/Swimming Pool/Jaccuzi/Sauna):"))     #The listed facilities are counted as part of the total hotel price
    if totalFacilities == 4:                                                                                                            
        facilitiesPrice = float(15.5)
        print("TOTAL PRICE of facilities: £" + str(facilitiesPrice))
    elif totalFacilities == 0:
        facilitiesPrice = float(0)
        print("TOTAL PRICE of facilities: £" + str(facilitiesPrice))
    else:
        for i in range (0, totalFacilities):
            hotelFacilities = raw_input("Please enter the following facilites available(Gym/Swimming Pool/Jaccuzi/Sauna):")                 #If less than 4 but mroe than 0 facilities are available, the list of facilities are specified to add to the cost of the hotel
            if hotelFacilities == 'Gym':
                GymPrice = float(5)
            elif hotelFacilities == 'Swimming Pool':
                PoolPrice = float(3.75)
            elif hotelFacilities == 'Jaccuzi':
                JaccuziPrice = float(3.75)
            elif hotelFacilities == 'Sauna':
                saunaPrice = float(3)

                facilitiesPrice = GymPrice + PoolPrice + JaccuziPrice + saunaPrice

                print("Gym Price: £5.00 /n Swimming Pool Price: £3.75 /n Jaccuzi Price: £3.75 /n Sauna Price: £3.00 /n" "PRICE FOR HOTEL FACILITIES: £" + str(facilitiesPrice) + "/n")



    carParkPrice = 0

    carParking = raw_input("Is car parking available? (Yes/No):")                           #Car parking fees if included, are calculated
    if carParking == 'Yes':
        disabledCarPark = raw_input("Will you require disabled car park?(Yes/No):")
        if disabledCarPark == 'Yes':
            carParkPrice = float(0)
        elif disabledCarPark == 'No':
            carParkPrice = float(10)
            print("Car Park PRICE: £" + str(carParkPrice))
            
        
        
    mealsIncluded = raw_input("Is breakfast included? (Yes/No):")                          #Breakfast fees if included, are calculated
    if mealsIncluded == 'Yes':
        mealsPrice = int(10)
    else:
        mealsPrice = int (0)
        print("Breakfast Accomodation PRICE: £" + str(mealsPrice))


    hotelPrice = hotel(float(starsPrice), float(customerPrice), float(pricePerNight), float(facilitiesPrice), float(carParkPrice), float(mealsPrice))
    hotelPrice = round(hotelPrice, 2)
    print("OVERALL TOTAL PRICE for this hotel: £" + str(hotelPrice))

else:
    hotelPrice = int(0)
    print("Cost for HOTELS: £" + str(hotelPrice))




#New Method    

def cruise(cruise_Type, FlightDistancePrice, numOf_Passengers, cabin_Type, numOf_Days):
    priceOfCruise = (cruise_Type * FlightDistancePrice) * (numOf_Passengers * cabin_Type * numOf_Days)                  #Finally the cost of the cruise is determined through: 
    return priceOfCruise                                                                                                            #Type of Cruise 
                                                                                                                                    #Destinations (determined from flight distance)
cruiseRate = 0                                                                                                                      #The number of passengers booked per cabin
                                                                                                                                    #The Cabin Type
cruiseType = raw_input("Please enter which type of Cruise Line you wish to book (Mainstream, Luxury, River, Expedition):")          #The number of days on the cruise
if cruiseType == 'Mainstream':
    MainstreamType = raw_input("From the following list of Cruise Lines:\n\n Carnival\n Celebrity\n Costa\n Cunard\n Disney\n Holland America\n MSC\n Norwegian\n Princess\n Royal Carribean International\n\nPlease enter the Cruise Line you wish to book with:")
    if MainstreamType == 'Carnival':
        cruiseRate = int(1.32)
    elif MainstreamType == 'Celebrity':
        cruiseRate = int(1.4)
    elif MainstreamType == 'Costa':
        cruiseRate = int(1.34)
    elif MainstreamType == 'Cunard':
        cruiseRate = int(1.37)
    elif MainstreamType == 'Disney':
        cruiseRate = int(1.45)
    elif MainstreamType == 'Holland America':
        cruiseRate = int(1.38)
    elif MainstreamType == 'MSC':
        cruiseRate = int(1.33)
    elif MainstreamType == 'Norwegian':
        cruiseRate = int(1.32)
    elif MainstreamType == 'Princess':
        cruiseRate = int(1.41)
    elif MainstreamType == 'Royal Caribbean International':
        cruiseRate = int(1.43)
    print("CRUISE LINE BOOKED: " + MainstreamType + " Cruise Lines")       

elif cruiseType == 'Luxury':
    LuxuryType = raw_input("From the following list of Cruise Lines:\n\n Club\n Crystal\n Hapag-Lloyed\n Oceania\n Paul Guaguin\n Regent Seven Seas\n Seabourn\n Silversea\n Viking Ocean\n Windstar\n\nPlease enter the Cruise Line you wish to book with:")
    if LuxuryType == 'Club':
        cruiseRate = int(1.57)
    elif LuxuryType == 'Crystal':
        cruiseRate = int(1.6)
    elif LuxuryType == 'Hapag-Lloyd':
        cruiseRate = int(1.68)
    elif LuxuryType == 'Oceania':
        cruiseRate = int(1.55)
    elif LuxuryType == 'Regent Seven Seas':
        cruiseRate = int(1.63)
    elif LuxuryType == 'Seaborn':
        cruiseRate = int(1.55)
    elif LuxuryType == 'Silversea':
        cruiseRate = int(1.59)
    elif LuxuryType == 'Viking':
        cruiseRate = int(1.62)
    elif LuxuryType == 'Windstar':
        cruiseRate = int(1.65)
    elif LuxuryType == 'Paul Gauguin':
        cruiseRate = int(1.66)
    print("CRUISE LINE BOOKED: " + LuxuryType + " Cruise Lines")

elif cruiseType == 'River':
    RiverType = raw_input("From the following list of Cruise Lines:\n\n A-ROSA\n Amadeus\n AmaWaterways\n American\n American Queen Steamboat Company\n APT\n Avalon\n CroisiEurope\n Crystal River\n Emerald\n Gate 1 Travel\n Grand Circle\n\nPlease enter the Cruise Line you wish to book with:")
    if RiverType == 'A-ROSA':
        cruiseRate = int(1.71)
    elif RiverType == 'Amadeus':
        cruiseRate = int(1.75)
    elif RiverType == 'AmaWaterways':
        cruiseRate = int(1.74)
    elif RiverType == 'American Queen Steamboat Company':
        cruiseRate = int(1.74)
    elif RiverType == 'APT':
        cruiseRate = int(1.7)
    elif RiverType == 'Avalon Waterways':
        cruiseRate = int(1.68)
    elif RiverType == 'CroisiEurope':
        cruiseRate = int(1.68)
    elif RiverType == 'Crystal River':
        cruiseRate = int(1.7)
    elif RiverType == 'Emerald Waterways':
        cruiseRate = int(1.75)
    elif RiverType == 'Gate 1 Travel':
        cruiseRate = int(1.74)
    elif RiverType == 'American':
        cruiseRate = int(1.73)
    elif RiverType == 'Grand Circle':
        cruiseRate = int(1.76)
    print("CRUISE LINE BOOKED: " + RiverType + " Cruise Lines")
        
elif cruiseType == 'Expedition':
    ExpeditionType = raw_input("From the following list of Cruise Lines:\n\n Alaskan Dream\n Blount Small Ship Adventures\n G Adventure\n Hurtigruten\n Lindblad Expeditions-National Geographic\n Ponant\n Poseidon Expeditions\n QuarkExpeditions\n Silversea Expeditions\n UnCruise Adventures\n Zegrahm Expeditions\n\nPlease enter the Cruise Line you wish to book with:")
    if ExpeditionType == 'Alaskan Dream':
        cruiseRate = int(1.83)
    elif ExpeditionType == 'Blount Small Ship Adventures':
        cruiseRate = int(1.8)
    elif ExpeditionType == 'G Adventures':
        cruiseRate = int(1.79)
    elif ExpeditionType == 'Hurtigruten':
        cruiseRate = int(1.77)
    elif ExpeditionType == 'Lindblad Expeditions-National Geographic':
        cruiseRate = int(1.82)
    elif ExpeditionType == 'Ponant':
        cruiseRate = int(1.79)
    elif ExpeditionType == 'Poseidon Expeditions':
        cruiseRate = int(1.78)
    elif ExpeditionType == 'Quark Expeditions':
        cruiseRate = int(1.78)
    elif ExpeditionType == 'Silversea Expeditions':
        cruiseRate = int(1.8)
    elif ExpeditionType == 'UnCruise Adventures':
        cruiseRate = int(1.79)
    elif ExpeditionType == 'Zegrahm Expeditions':
        cruiseRate = int(1.81)
    print("CRUISE LINE BOOKED: " + ExpeditionType + " Cruise Lines")
                 
    
numOfPassengers = int(raw_input("How many of you do wish to book for this cruise:"))
print("Number of Passengers BOOKED: " + str(numOfPassengers))


cabinPriceRate = 0

cabin = raw_input("Of the following list of Cabin Types:\n\n In-Room\n Ocean View\n Balcony\n Mini-Suite\n Suite\n\nPlease enter the Cabin Type you wish to book:")
if cabin == 'In-Room':
    cabinPriceRate = int(1)
elif cabin == 'Ocean View':
    cabinPriceRate = int(1.2)
elif cabin == 'Balcony':
    cabinPriceRate = int(1.4)
elif cabin == 'Mini-Suite':
    cabinPriceRate = int(1.6)     
elif cabin == 'Suite':
    cabinPriceRate = int(1.8) 


sailDaysRate = 0

numOfSailDays = int(raw_input("How many days will you book with this Cruise Line:"))
for i in range(0, numOfSailDays):
    sailDaysRate = float(numOfSailDays / 7)
print("Cruise DURATION: " + str(numOfSailDays) + " Days")

cruisePriceTotal = cruise(float(cruiseRate), float(FlightDistancePrice), float(numOfPassengers), float(cabinPriceRate), float(sailDaysRate))
print("Cruise TOTAL PRICE: £" + str(cruisePriceTotal))





#Final Method

def holiday_OvrlPrice(flight_Destination_Price, return_Flight_Price, hotel, cruise):
    holidaySum = flight_Destination_Price + return_Flight_Price + hotel + cruise
    return holidaySum

totalHolidayPrice = holiday_OvrlPrice(float(TotalFlightPrice), float(returnPriceFlight), float(hotelPrice), float(cruisePriceTotal))                        #The sum total of all holiday expenses are calculated
print("OVERALL HOLIDAY TOTAL PRICE: £" + str(totalHolidayPrice))
