state_of_us = ["Alabama", "Alaska", "American Samoa", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District of Columbia"
               , "Florida", "Georgia"]
print(state_of_us[8])
state_of_us.append("DC")
print(state_of_us[-6])

print(len(state_of_us))
state_of_us.append("NY")
print(len(state_of_us))
state_of_us.extend(["NC","Hawaii"])
print(state_of_us)
