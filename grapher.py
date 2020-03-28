import random
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import cm
import matplotlib.colors as mcolors
from matplotlib.patches import ConnectionPatch
import numpy as np


pop_gov_df = pd.read_csv('population.csv')
pop_age_sex_df = pd.read_csv('population_sex_age.csv')
pop_over_year_df = pd.read_csv('population_over_years.csv')


def plot_graph_pop_by_gov():
    pop_gov_df.drop('gov_ar', axis=1, inplace=True)
    # print(pop_gov_df.head())
    # print(pop_gov_df.index)
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    print(pop_gov_df.describe(include='all'))

    fig, ax = plt.subplots(figsize=(20, 10))
    # Bars
    width = 0.4
    male_bar = ax.bar(
        2*pop_gov_df.index - width*2, pop_gov_df['male'],
        width, label='Males'
    )
    female_bar = ax.bar(
        2*pop_gov_df.index - width, pop_gov_df['female'],
        width, label='Females'
    )
    total_bar = ax.bar(
        2*pop_gov_df.index, pop_gov_df['total'],
        width, label='Total'
    )
    urban_bar = ax.bar(
        2 * pop_gov_df.index + width, pop_gov_df['urban'],
        width, label='Urban'
    )
    rural_bar = ax.bar(
        2 * pop_gov_df.index + width*2, pop_gov_df['rural'],
        width, label='Rural'
    )

    # Tiles and labels
    ax.set_title('Total population for 1/1/2019')
    ax.set_ylabel('Population (millions)')
    ax.set_xlabel('Governance')

    # Text
    total_pop = float(pop_gov_df['total'].sum())
    print(2*pop_gov_df['gov_en'].count())
    ax.text(pop_gov_df['gov_en'].count(), pop_gov_df['total'].max(),
            'Total Population: %.2f million' % (total_pop/1e+6))

    # for gov in pop_gov_df.index:
    #     ax.text(gov*2, pop_gov_df['total'][gov] * 1.01,
    #             'Total Population: %.2f million' % (pop_gov_df['total'][gov] / 1e+6))

    # Ticks
    ax.set_xticks(2*pop_gov_df.index)
    ax.set_xticklabels(pop_gov_df['gov_en'])

    ax.set_yticks([x for x in range(0,
                   int(10e+6),
                   int(1e+6))])

    plt.xticks(rotation=-45)
    plt.legend()
    plt.show()


def plot_graph_pop_by_gov_pandas():
    global  pop_gov_df
    pop_gov_df.drop('gov_ar', axis=1, inplace=True)
    pd.set_option("display.max_rows", None, "display.max_columns", None)

    print(pop_gov_df.describe(include='all'))
    ax = pop_gov_df.plot.bar(rot=-45)
    # ax.set_xticks([1,...,27])
    # ax.set_xticklabels(pop_gov_df['gov_en'])
    # x= ['gov_en']
    # y = ['male', 'female', 'total']
    # ax = pop_gov_df.plot.bar(x=x, y=y, rot=0)
    plt.show()


def plot_graph_pop_by_gov_vertical():
    pass


def plot_graph_all():
    pop_gov_df.drop('gov_ar', axis=1, inplace=True)

    pd.set_option("display.max_rows", None, "display.max_columns", None)
    # print(pop_gov_df.describe(include='all'))

    # fig, ax = plt.subplots(figsize=(20, 10))
    plt.figure(
        figsize=(20, 12)
    )
    ax1 = plt.subplot(231)
    width = 0.4
    male_bar = ax1.bar(
        2 * pop_gov_df.index - width * 2, pop_gov_df['male'],
        width, label='Males'
    )
    female_bar = ax1.bar(
        2 * pop_gov_df.index - width, pop_gov_df['female'],
        width, label='Females'
    )
    total_bar = ax1.bar(
        2 * pop_gov_df.index, pop_gov_df['total'],
        width, label='Total'
    )
    # ax1.set_title('Total population for 1/1/2019')
    ax1.set_ylabel('Population (millions)')
    ax1.set_xlabel('Governance')
    ax1.set_title('Population percentages of males and female')
    ax1.legend()

    ax2 = plt.subplot(232)
    total_bar = ax2.bar(
        2 * pop_gov_df.index, pop_gov_df['total'],
        width, label='Total'
    )
    urban_bar = ax2.bar(
        2 * pop_gov_df.index + width, pop_gov_df['urban'],
        width, label='Urban'
    )
    rural_bar = ax2.bar(
        2 * pop_gov_df.index + width * 2, pop_gov_df['rural'],
        width, label='Rural'
    )
    ax2.set_ylabel('Population (millions)')
    ax2.set_xlabel('Governance')
    ax2.set_title('Population percentages of urban and rural')
    ax2.legend()

    target_gov_number = 6
    ax3 = plt.subplot(234)
    # ax3 = plt
    sizes = pop_gov_df['total'] / pop_gov_df['total'].sum()

    theme = plt.get_cmap('hsv')
    # print([theme(1. * i / len(sizes)) for i in range(len(sizes))])
    ax3.set_prop_cycle("color", [theme(1. * i / len(sizes))
                                 for i in range(len(sizes))])

    explode = [0 for x in range(len(sizes))]
    explode[target_gov_number] = 0.1
    explode = tuple(explode)

    patches, labels = ax3.pie(
        sizes, startangle=-65,
        explode=explode
        # colors=plt.get_cmap('jet')
        # radius=5
    )

    pop_gov_df['labels'] = pop_gov_df['gov_en'] + ' ' + (sizes*100).round(2).astype(str) + '%'
    # print(pop_gov_df['labels'])
    ax3.set_title('Total population percentages')

    ax3.legend(
        # patches,
        # (sizes*100).round(2).to_list(),
        labels=pop_gov_df['labels'],
        loc='center right', bbox_to_anchor=(0, 0.5)
        )

    ax4 = plt.subplot(235)
    ratios = [((pop_gov_df['male'][target_gov_number] / pop_gov_df['total'][target_gov_number])).round(2),
              ((pop_gov_df['female'][target_gov_number] / pop_gov_df['total'][target_gov_number])).round(2)
              ]
    xpos = 0
    bottom = 0
    height = 0
    width = 0.2
    for j in range(len(ratios)):
        height = ratios[j]
        ax4.bar(xpos,
                height,
                width,
                bottom=bottom,
                )
        ypos = bottom + ax4.patches[j].get_height() / 2
        bottom += height
        ax4.text(xpos, ypos, "%d%%" % (ax4.patches[j].get_height() * 100),
                 ha='center')

    ax4.axis('off')
    ax4.set_xlim(- 2.5 * width, 2.5 * width)
    ax4.set_title('Male to female percentage of Sharkia Governance')
    ax4.legend(('Males', 'Females'))

    # use ConnectionPatch to draw lines between the two plots
    # get the wedge data
    theta1, theta2 = ax3.patches[target_gov_number].theta1, ax3.patches[target_gov_number].theta2
    center, r = ax3.patches[target_gov_number].center, ax3.patches[target_gov_number].r
    bar_height = sum([item.get_height() for item in ax4.patches])

    # draw top connecting line
    x = r * np.cos(np.pi / 180 * theta2) + center[0]
    y = np.sin(np.pi / 180 * theta2) + center[1]
    con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax4.transData,
                          xyB=(x, y), coordsB=ax3.transData)
    con.set_color([0, 0, 0])
    con.set_linewidth(4)
    ax4.add_artist(con)

    # draw bottom connecting line
    x = r * np.cos(np.pi / 180 * theta1) + center[0]
    y = np.sin(np.pi / 180 * theta1) + center[1]
    con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax4.transData,
                          xyB=(x, y), coordsB=ax3.transData)
    con.set_color([0, 0, 0])
    ax4.add_artist(con)
    con.set_linewidth(4)

    ax5 = plt.subplot(236)
    ratios = [pop_gov_df['urban_per'][target_gov_number],
              100 - pop_gov_df['urban_per'][target_gov_number]
              ]
    xpos = 0
    bottom = 0
    height = 0
    width = 0.2
    for j in range(len(ratios)):
        height = ratios[j]
        ax5.bar(xpos,
                height,
                width,
                bottom=bottom,
                )
        ypos = bottom + ax5.patches[j].get_height() / 2
        bottom += height
        ax5.text(xpos, ypos, "%d%%" % (ax5.patches[j].get_height()),
                 ha='center')

    ax5.axis('off')
    ax5.set_xlim(- 2.5 * width, 2.5 * width)
    ax5.set_title('Urban to Rural percentage of Sharkia Governance')

    ax5.legend(('Urban', 'Rural'))

    # ax4.set_aspect('equal')
    # ax5.set_aspect('equal')

    # ax3.margins(x=0.0, y=0.05)
    # ax4.margins(x=0.0, y=0.05)
    # ax5.margins(x=0.0, y=0.05)

    ax6 = plt.subplot(233)
    ratios = pop_age_sex_df['percentage']
    xpos = 0
    bottom = 0
    height = 0
    width = 0.2
    for j in range(len(ratios)):
        height = ratios[j]
        ax6.bar(xpos,
                height,
                width,
                bottom=bottom,
                )
        ypos = bottom + ax6.patches[j].get_height() / 2
        bottom += height
        ax6.text(xpos, ypos, "%d%%" % (ax6.patches[j].get_height()),
                 ha='center')

    ax6.axis('off')
    ax6.set_xlim(- 2.5 * width, 2.5 * width)
    ax6.legend(pop_age_sex_df['age'])
    ax6.set_title('Percentage of age of population')

    plt.show()



def plot_graph_pop_mid_year():
    fig, ax = plt.subplots(figsize=(10, 8))
    pop_by_million = pop_over_year_df['total'] / 1e+3
    ax.plot(pop_over_year_df['year'], pop_by_million)
    bar_width = .5
    ax.bar(pop_over_year_df['year'], pop_by_million,
           bar_width)
    ax.set_xticks(pop_over_year_df['year'])

    for index in range(len(pop_over_year_df['year'])):
        ax.text(pop_over_year_df['year'][index]-0.5, pop_by_million[index]/2,
                '%.2f million' % (pop_by_million[index]), rotation=45)

    ax.set_title('Total population on mid year over (2002-2018)')
    ax.set_ylabel('Total population (millions)')
    ax.set_xlabel('years')
    plt.show()


if __name__ == '__main__':
    # plot_graph_pop_by_gov()
    # plot_graph_pop_by_gov_pandas()
    # plot_graph_all()
    plot_graph_pop_mid_year()
