import matplotlib.pyplot as plt
import squarify

# Define the data
categories = ['Clothing', 'Shoes', 'Accessories', 'Appliances']
subcategories = [['Dresses', 'Jackets', 'Coats', 'Jeans'],
                 ['Boots', 'Flats', 'Heels', 'Sandals', 'Sneakers'],
                 ['Bags', 'Belts', 'Sunglasses', 'Hats', 'Socks'],
                 ['Coffee Makers', 'Air Fryers', 'Blenders', 'Pressure Cookers', 'Stand Mixer']]
units_sold = [200, 4600, 1300, 1700, 1800, 900, 2200, 2700, 1500, 2500, 600, 140, 1100, 800, 140, 300, 450, 700, 110]

print(len(subcategories))

# Create the nested tree map
tree_map_data = {}
for i, category in enumerate(categories):
    subcat_data = {}
    for j, subcategory in enumerate(subcategories[i]):
        subcat_data[subcategory] = units_sold[(i*4)+j]
    tree_map_data[category] = subcat_data

# Define the list of colors for the categories and subcategories
cat_colors = ['#5F4BBB', '#E69A8D', '#7CCBA2', '#F7AE4A']

subcat_colors = ['#C8B3E5', '#DDB3E5', '#E8B3E5', '#F3B3E5', '#FEB3E5', '#B8E0D2', '#CCE0D2', '#E0E0D2', '#F4E0D2', '#FFF7C6',                 '#D2B1E2', '#E6B1E2', '#FFB1E2', '#FFD1E2', '#FFF7C6',                 '#B6D1E6', '#C6D1E6', '#D6D1E6', '#E6D1E6', '#F6D1E6']

# Plot the nested tree map
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111, aspect='equal')
i = 0
for category in tree_map_data.keys():
    subcat_data = tree_map_data[category]
    subcat_colors_for_category = subcat_colors[i:i+len(subcat_data)]
    i += len(subcat_data)
    squarify.plot(sizes=subcat_data.values(),
                  label=subcat_data.keys(),
                  color=subcat_colors_for_category,
                  alpha=.7,
                  ax=ax)
    plt.text(0., 0., category, fontsize=15, ha='center', va='center', color='blue')
    plt.axis('off')

plt.title('Sales by Category and Subcategory')
plt.show()
