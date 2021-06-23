"""

"""

__author__ = "Grigory Vilinov 45107339"
__date__ = "09/03/2019"


from destinations import Destinations

def likes(topic):
    """
    prints questions, takes user input
    Parameter:
        topic(int): User's preference for some activities
    """
    print(f"\nHow much do you like {topic}? (-5 to 5)")
    topic=input("> ")
    return topic

def convert_cost(cost):
    """
    prints questions, takes user input
    Parameter:
        cost(str): travel budget
    Return:
        int: number of dollar signs
    """
    if cost=="$$$":
        cost=3
    elif cost=="$$":
        cost=2
    elif cost=="$":
        cost=1
    return cost

def convert_crime(crime):
    """
    prints questions, takes user input
    Parameter:
        crime(str): travel crime risk
    Return:
        int: crime level
    """
    if crime=="low":
        crime=1
    elif crime=="average":
        crime=2
    else:
        crime=3
    return crime

def convert_season(season):
    """
    prints questions, takes user input
    Parameter:
        season(int): travel during the preferred season
    Return:
        str: season of the year
    """
    if season=="1":
        season='spring'      
    elif season=="2":
        season='summer'        
    elif season=="3":
        season='autumn'     
    elif season=="4":
        season='winter'
    return season

def convert_climate(climate):
    """
    prints questions, takes user input
    Parameter:
        climate(int): preferred climate to travel to travelling
    Return:
        str: climate of the destination
    """
    if climate=="1":
        climate="cold"
    elif climate=="2":
        climate="cool"      
    elif climate=="3":
        climate="moderate"     
    elif climate=="4":
        climate="warm"
    elif climate=="5":
        climate="hot"
    return climate

def main():

    greeting=input("Welcome to Travel Inspiration!\n\nWhat is your name? ")
    print("\nHi,", greeting + "!")

    print("\nWhich continent would you like to travel to?")
    print("  1) Asia")
    print("  2) Africa")
    print("  3) North America")
    print("  4) South America")
    print("  5) Europe")
    print("  6) Oceania")
    print("  7) Antarctica")

    continent=input("> ")
    """
    prints questions, takes user input
    Parameter:
        continent(int): preferred continent for travel destination
    Return:
        str: name of the continent
    """

    if continent=="1":
       continent="asia"
    elif continent=="2":
        continent="africa"
    elif continent=="3":
        continent="north america"
    elif continent=="4":
        continent="south america"
    elif continent=="5":
        continent="europe"
    elif continent=="6":
        continent="oceania"
    elif continent=="7":
        continent="antarctica"

    print("\nWhat is money to you?")
    print("  $$$) No object")
    print("  $$) Spendable, so long as I get value from doing so")
    print("  $) Extremely important; I want to spend as little as possible")

    cost=convert_cost(input("> "))

    print("\nHow much crime is acceptable when you travel?")
    print("  1) Low")
    print("  2) Average")
    print("  3) High")

    crime=convert_crime(input("> "))

    print("\nWill you be travelling with children?")
    print("  1) Yes")
    print("  2) No")

    kids=input("> ")
    """
    prints questions, takes user input
    Parameter:
        kids(int): whether children are also travelling
    Return:
        type: boolean
    """

    if kids=="1":
        kids=True
    elif kids=="2":
        kids=False
        
    print("\nWhich season do you plan to travel in?")
    print("  1) Spring")
    print("  2) Summer")
    print("  3) Autumn")
    print("  4) Winter")

    season=convert_season(input("> "))
    
    print("\nWhat climate do you prefer?")
    print("  1) Cold")
    print("  2) Cool")
    print("  3) Moderate")
    print("  4) Warm")
    print("  5) Hot")

    climate=convert_climate(input("> "))

    print("\nNow we would like to ask you some questions about your interests, on a scale of -5 to 5. -5 indicates strong dislike, whereas 5 indicates strong interest, and 0 indicates indifference.")

    sport_score = likes("sports")
    wildlife_score = likes("wildlife")
    nature_score = likes("nature")
    historical_score = likes("historical sites")
    dining_score = likes("fine dining")
    adventure_score = likes("adventure activities")
    beach_score = likes("the beach")


    top_destination = None

    season_value=0
    max_score = -99999999

    for destination in Destinations().get_all():

        if destination.get_continent() == continent and \
           (destination.is_kid_friendly() == kids or not kids):

            if (convert_cost(cost) >= convert_cost(destination.get_cost())) and \
               (int(crime) >= convert_crime(destination.get_crime())):

                if (convert_climate(climate) == destination.get_climate()):

                    interest_score = int(sport_score)*(destination.get_interest_score("sports")) \
                                        + int(wildlife_score)*(destination.get_interest_score("wildlife")) \
                                        + int(nature_score)*(destination.get_interest_score("nature")) \
                                        + int(historical_score)*(destination.get_interest_score("historical")) \
                                        + int(dining_score)*(destination.get_interest_score("cuisine")) \
                                        + int(adventure_score)*(destination.get_interest_score("adventure")) \
                                        + int(beach_score)*(destination.get_interest_score("beach"))

                    season_value = destination.get_season_factor(season)
                    score = season_value*interest_score

                    if score >= max_score:
                        max_score=score
                        top_destination = destination
                        

    print ("\nThank you for answering all our questions. Your next travel destination is:")
    if top_destination is None:
        print('None')
    else:
        print(format(top_destination.get_name()))


if __name__ == "__main__":
    main()
