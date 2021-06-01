import kaggle
import shutil
import os


kaggle.api.authenticate()

kaggle.api.dataset_download_files(
    "crowww/a-large-scale-fish-dataset",
    path="./data/",
    quiet=False,
    unzip=True,
)

# source_folder = "data/NA_Fish_Dataset"
# target_dir = "data/my_fish_dataset/"
# if not os.path.isdir(target_dir):
#     os.mkdir(target_dir)

# for idx_subfolder, subfolder in enumerate(os.listdir(source_folder)):
#     print(f"Copying {subfolder} under {idx_subfolder}")
#     for idx_filename, filename in enumerate(
#         os.listdir(os.path.join(source_folder, subfolder))
#     ):
#         shutil.copy(
#             os.path.join(source_folder, subfolder, filename),
#             os.path.join(target_dir, f"{idx_subfolder:02}_{idx_filename:03}.jpg"),
#         )
