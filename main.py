import matplotlib.pyplot as plt
import numpy as np

years = np.array([1400, 1401, 1402, 1403, 1404, 1405])

euro_values = [
    28903,  # ۱۴۰۰
    57780,  # ۱۴۰۱
    65728,  # ۱۴۰۲
    107580,  # ۱۴۰۳
    191950,  # ۱۴۰۴
    304970,  # ۱۴۰۵
]

dirham_values = [
    8300,  # ۱۴۰۰ (تقریبی)
    10946,  # ۱۴۰۱
    11687,  # ۱۴۰۲
    26895,  # ۱۴۰۳
    35398,  # ۱۴۰۴
    72185,  # ۱۴۰۵
]

dollar_values = np.array(
    [
        26250,  # ۱۴۰۰
        48500,  # ۱۴۰۱
        60350,  # ۱۴۰۲
        91991,  # ۱۴۰۳
        152399,  # ۱۴۰۴
        159820,  # ۱۴۰۵
    ]
)
line_style = dict(
    marker=".",
    markersize="15",
    markerfacecolor="#62013b",
    markeredgecolor="#000000",
    linestyle="solid",
    linewidth=1.5,
)

plt.tick_params(axis="both", colors="#431A04")
plt.title("Currency value in years", fontsize=18, family="Arial")
plt.xlabel("years", fontsize=18)
plt.ylabel("IRR vlaue", fontsize=18)
plt.plot(years, dollar_values, color="#1303f5", **line_style)
plt.plot(years, euro_values, color="#02ad77", **line_style)
plt.plot(years, dirham_values, color="#be2323", **line_style)
plt.xticks(years)
plt.show()

# Grid lines
x = [1, 2, 3, 4, 5, 6, 7]
y = [10, 20, 30, 40, 50, 60, 70]

plt.grid(axis="y", linewidth=2, color="lightgray", line_style="dashed")

# Bar chart
food_cat = np.array(["Grains", "Fruit", "Vegetables", "Protein", "Dairy", "Sweets"])
daily_values = np.array([4, 3, 1, 5, 3, 2])

plt.bar(food_cat, daily_values, color="pink")
# plt.barh(food_cat , daily_values, color='pink') for horizantal bar
plt.title("Daily consumptions")
plt.xlabel("food")
plt.ylabel("Quantity")

plt.show()

# Pie chart

categories = ["math", "science", "religion", "english"]
values = [17.5, 20, 14, 13]
colors = ["red", "blue", "green", "orange"]
plt.pie(
    values,
    labels=categories,
    autopct="%1.1f%%",
    colors=colors,
    explode=[0, 0, 0, 0.1],
    shadow=False,
    startangle=90,
)
plt.title("Imaginary grades")
plt.show()

# scatter graph

study_hourA = np.array([0, 1, 1.2, 2, 2.15, 3, 4.5, 5.7])
gradesA = np.array([13, 15, 17, 16.75, 18.5, 20, 20, 20])

study_hourB = np.array([0, 0, 1, 1, 2, 3, 3.15, 3.30])
gradesB = np.array([11, 12, 12.5, 13, 15.25, 17, 19, 20])
plt.title("Test Score")
plt.scatter(study_hourA, gradesA, color="orange", alpha=0.5, s=140, label="Class A")
plt.scatter(study_hourB, gradesB, color="green", alpha=0.5, s=140, label="Class B")
plt.xlabel("hours studied")
plt.ylabel("Grades")
plt.show()
