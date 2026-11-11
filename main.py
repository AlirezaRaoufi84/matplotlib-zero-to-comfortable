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
