# body_weight = 93  # kg
body_weight = 181.2 / 2.2  # kg
height = 177.8  # cm
age = 24

BMR = 10 * body_weight + 6.25 * height - 5 * age + 5  # basal metabolic rate i.e. calories burnt doing nothing
activity_multiplier = 1.17  # sedentary + training = 1.2 - 1.5 1.16 = working from home w/ lil walking
guesstimated_maintenance = BMR * activity_multiplier
# deficit = 0.12  # 10%
# recomposition_cals = round(guesstimated_maintenance * (1-deficit))  # 5-10% deficit
bold = '\033[1m'
end = '\033[0;0m'

print(bold + "BMR: " + end, round(BMR))
# print("Recomposition Calories: ", recomposition_cals, "(", round(deficit*100), "% deficit)")

body_fat = 12  # 12 - 15
lean_mass = 1 - (body_fat / 100)
body_fat_multiplier = 1.3  # 1.2 - 1.6 g/LBM - closer to 1.2 the higher the body fat %
recomp_protein = (body_weight * 2.2) * lean_mass * body_fat_multiplier
fat_percentage = 0.3  # range from 20-35% - 20% is leaner side
# more active benefit from carbs as can be utilised for energy - less active benefit more from higher fat

deficit_list = [0, 5, 10, 12, 15, 20]
for i in deficit_list:
    deficit = i
    recomposition_cals = round(guesstimated_maintenance * (1 - (deficit * 0.01)))  # 5-10% deficit
    fat_intake = (recomposition_cals * fat_percentage) / 9  # 9 calories per gram of fat
    remaining_calories = recomposition_cals - (recomp_protein * 4) - (fat_intake * 9)
    carb_intake = remaining_calories / 4  # 4 cals per gram of carbs
    print()
    if i == 0:
        print(bold + "Guesstimated Maintenance: " + end, round(guesstimated_maintenance))
    else:
        print(bold + "Recomposition Calories: " + end, recomposition_cals, "(", deficit, "% deficit )")
    print(bold + "Protein intake:" + end, str(round(recomp_protein)) + 'g',
          bold + "Fat intake:" + end, str(round(fat_intake)) + 'g',
          bold + "Carb intake:" + end, str(round(carb_intake)) + 'g')
    print()

# print("Protein intake: ", str(round(recomp_protein)) + 'g')
# print("Fat intake: ", str(round(fat_intake)) + 'g')
# # print(remaining_calories)
# print("Carb intake: ", str(round(carb_intake)) + 'g')
