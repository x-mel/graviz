# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 04:48:57 2016

@author: mel
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D 
from matplotlib import rc

rc('text', usetex=True)
rc('font',**{'family':'sans-serif','sans-serif':['Geneva']})

col=['indianred', 'dimgray', 'cadetblue']

grades = [ {'value': 79.1, 'label': 'Linear Algebra', 'color': col[0]}, 
            {'value': 77.6, 'label': 'Real Analysis', 'color': col[0]}, 
            {'value': 72, 'label': 'Data Processing', 'color': col[0]},
            {'value': 69.38, 'label': 'Numerical Analysis', 'color': col[0]}, 
            {'value': 75.7, 'label': 'Analytical Mechanics', 'color': col[0]}, 
            {'value': 76.6, 'label': 'Statistics and Probability', 'color': col[0]}, 
            {'value': 91.33, 'label': 'Programming II', 'color': col[0]}, 
            {'value': 79.4, 'label': 'Atomic Physics and Spectroscopy', 'color': col[0]},
            {'value': 71, 'label': 'Statistics and Data Analysis', 'color': col[1]}, 
            {'value': 70, 'label': 'Cosmology', 'color': col[1]}, 
            {'value': 70, 'label': 'Galaxies', 'color': col[1]}, 
            {'value': 70, 'label': 'Introduction to the Cosmos', 'color': col[1]},
            {'value': 91, 'label': 'Modeling Workshop', 'color': col[2]},
            {'value': 91, 'label': 'Distributed Systems', 'color': col[2]},
            {'value': 76, 'label': 'Parallel Programming', 'color': col[2]}]

#g=[i['value'] for i in physics]

g= [79.1, 77.6, 72, 69.38, 75.7, 76.6, 
    91.33, 79.4, 71, 70, 70, 70, 91, 91, 76]

s= ['Linear Algebra', 'Real Analysis', 
    'Data Processing', 'Numerical Analysis', 'Analytical Mechanics', 
    'Statistics and Probability', 'Programming II', 'Atomic Physics and Spectroscopy', 
    'Statistics and Data Analysis', 'Cosmology', 'Galaxies', 
    'Introduction to the Cosmos', 'Modeling Workshop', 
    'Distributed Systems', 'Parallel Programming']

c= [col[0], col[0], col[0], col[0], col[0], col[0], col[0], col[0], 
    col[1], col[1], col[1], col[1], col[2], col[2], col[2]]

data = {'grade' : pd.Series(g, index=s),
        'level' : pd.Series(c, index=s)}


df = pd.DataFrame(data)

# Create a figure of given size
fig = plt.figure(figsize=(13,7))
# Add a subplot
ax = fig.add_subplot(111)
# Set title
ttl = "Academic grades of some relevant subjects (100-point grading scale)"

# Set color transparency (0: transparent; 1: solid)
a = 0.7

df['grade'].plot(kind='barh', ax=ax, alpha=a, legend=False, color=c,
                      edgecolor='w', xlim=(0, 100), title=ttl, width=1)

# Remove grid lines (dotted lines inside plot)
ax.grid(False)
# Remove plot frame
ax.set_frame_on(False)
# Pandas trick: remove weird dotted line on axis
#ax.lines[0].set_visible(False)

# Customize title, set position, allow space on top of plot for title
ax.set_title(ax.get_title(), fontsize=15, alpha=a, ha='left')
plt.subplots_adjust(top=0.8)
ax.title.set_position((0,1.08))

# Set x axis label on top of plot, set label text
#ax.xaxis.set_label_position('bottom')
#xlab = ''
#ax.set_xlabel(xlab, fontsize=8, alpha=a, ha='left')
#ax.xaxis.set_label_coords(0, 1.04)

# Position x tick labels on top
ax.xaxis.tick_top()
# Remove tick lines in x and y axes
ax.yaxis.set_ticks_position('none')

# Customize x tick lables
xticks = [50, 60, 70, 80, 90, 100]
ax.xaxis.set_ticks(xticks)
ax.set_xticklabels(xticks, fontsize=13, alpha=a)

# Customize y tick labels
yticks = [item.get_text() for item in ax.get_yticklabels()]
ax.set_yticklabels(yticks, fontsize=13, color='white', alpha=1, ha='left')
ax.yaxis.set_tick_params(pad=-5)

# Legend
# Create fake labels for legend
l1 = Line2D([], [], linewidth=12, color=col[0], alpha=a) 
l2 = Line2D([], [], linewidth=12, color=col[1], alpha=a) 
l3 = Line2D([], [], linewidth=12, color=col[2], alpha=a)

labels = ['Bachelor in Physics', 'Master in Astrophysics and Cosmology', 'Master in Data Science' ]

# Position legend in lower right part
# Set ncol=3 for horizontally expanding legend
leg = ax.legend([l1, l2, l3], labels, ncol=3, frameon=False, fontsize=11, 
                bbox_to_anchor=[1., 0], handlelength=2, 
                handletextpad=1, columnspacing=2)

# Save figure in png with tight bounding box
#plt.savefig('grades.png', bbox_inches='tight', dpi=300)
plt.savefig('grades.png', dpi=300)