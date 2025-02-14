from datetime import datetime as dt
from decimal import Decimal as dec
from random import randint, choice 
import custom_module

def randomYear():
  return abs(randint(-6000, 2025))
def destinations(weather):
  if weather == "warm":
    int = randint(1,5)
    warm_places = [bonaire, malta, maldives, india, spain]
    return warm_places[int]

Current_year = dt.now().date().year
Year_travelling = randomYear()


Base_cost = dec(30000)
Multiplier = 2.13756

Cost_to_travel = Base_cost + (dec(Multiplier) * (Year_travelling + Current_year))

print(Cost_to_travel.quantize(dec('0.01')))
