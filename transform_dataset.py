import pandas as pd

output_dir = ('./dataset/Clean_Raisin_Dataset.xlsx')
df = pd.read_excel('./dataset/Raisin_Dataset.xlsx')

def labels_are_int(r: pd.DataFrame.values):
  # Area
  if(type(r['Area']) is not int):
    raise TypeError(f"field Area, {r['Area']} is an instance of {type(r['Area'])} but expected int")
  # ConvexArea
  if(type(r['ConvexArea']) is not int):
    raise TypeError(f"field ConvexArea, {r['ConvexArea']} is an instance of {type(r['ConvexArea'])} but expected int")

def labels_are_float(r: pd.DataFrame.values):
  # MajorAxisLength
  if(type(r['MajorAxisLength']) is not float):
    raise TypeError(f"field MajorAxisLength, {r['MajorAxisLength']} is an instance of {type(r['MajorAxisLength'])} but expected float")
  # MinorAxisLength
  if(type(r['MinorAxisLength']) is not float):
    raise TypeError(f"field MinorAxisLength, {r['MinorAxisLength']} is an instance of {type(r['MinorAxisLength'])} but expected float")
  # Eccentricity
  if(type(r['Eccentricity']) is not float):
    raise TypeError(f"field Eccentricity, {r['Eccentricity']} is an instance of {type(r['Eccentricity'])} but expected float")
  # Extent
  if(type(r['Extent']) is not float):
    raise TypeError(f"field Extent, {r['Extent']} is an instance of {type(r['Extent'])} but expected float")
  # Perimeter
  if(type(r['Perimeter']) is not float):
    raise TypeError(f"field Perimeter, {r['Perimeter']} is an instance of {type(r['Perimeter'])} but expected float")

def class_is_str(r: pd.DataFrame.values):
  # Area
  if(type(r['Class']) is not str):
    raise TypeError(f"field Class, {r['Class']} is an instance of {type(r['Class'])} but expected int")

# create the binary class label
binary_class = []

for i, r in df.iterrows():
  for j, v in r.items():
    # verify if the dt is complete
    if(v is None or v == ""):
      raise ValueError("")

  # verify if the next labels are int
  labels_are_int(r)
  
  # verify if the next labels are float
  labels_are_float(r)

  # verify if the class is string
  class_is_str(r)

  # class datatype transform
  if(r['Class'] == "Kecimen"):
    binary_class.append(0)
  if(r['Class'] == "Besni"):
    binary_class.append(1)

# replace the categorical class to the binary class
df['Class'].update(binary_class)

# save the cleaned dataset
excel_df = df.to_excel(output_dir, index=False)
print("Transformed and saved")
