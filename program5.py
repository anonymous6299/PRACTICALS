'''
AIM=Data mapping

REL. THEORY=
Data mapping is the process of representing geographical information using maps and coordinates. Latitude and longitude are used to identify locations, while additional data can represent different attributes. Python libraries like Pandas and Matplotlib help visualize geographical data.

CODE=                                                                '''
import matplotlib.pyplot as plt
import pandas as pd

# Create sample geographical dataset
data = {
    'City': ['Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'Bangalore'],
    'Latitude': [28.61, 19.07, 22.57, 13.08, 12.97],
    'Longitude': [77.20, 72.87, 88.36, 80.27, 77.59],
    'Population': [32, 21, 15, 11, 13]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display dataset
print("Geographical Data:")
print(df)

# Create data mapping
plt.figure(figsize=(9, 6))

plt.scatter(df['Longitude'], df['Latitude'],
            s=df['Population'] * 50,
            c=df['Population'],
            cmap='viridis',
            edgecolor='black')

# Add city labels
for i in range(len(df)):
    plt.text(df['Longitude'][i] + 0.3,
             df['Latitude'][i] + 0.3,
             df['City'][i])

# Add labels and title
plt.title("Geographical Data Mapping of Indian Cities")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.colorbar(label="Population (in millions)")
plt.grid(True)
plt.show()

'''
LO=
1.	Learned to represent geographical data.
2.	Understood latitude and longitude coordinates.
3.	Visualized location-based information.
'''