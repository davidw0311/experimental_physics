import os

# dt_string = '10-20-15-50-41'
# dt_string = '10-21-02-09-22' # 1k pts
# dt_string = '10-28-01-07-45' # 5k pts
dt_string = '10-29-01-46-32' # valve level 306 long term
dt_string = '00-00-00-00-00' # simulated
all_image_files = []

graph_type = 'plots/'
# graph_type = 'plots/2d/'
# graph_type = 'plots/3d/'

for file in os.listdir(graph_type):
    if dt_string in file:
        all_image_files.append(graph_type+file)

all_image_files = sorted(all_image_files)

with open("test.md", "w") as f:
    for img_file in all_image_files:
        s = f'<img src="{img_file}" width=150px>\n'
        f.write(s)
        
        