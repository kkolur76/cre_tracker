import os
import csv
import pandas as pd


build_permits_path = "/Users/keshav/Downloads/Build Permits"


def txt2csv(input_path, output_path, cols):
    for file in os.listdir(input_path):
        if file.endswith('.txt'):
            result = []
            with open(os.path.join(input_path, file), 'r') as fn:
                file_lines = fn.readlines()
            for line in file_lines:
                cur_result = []
                cur_line = line.strip().split(' ')
                for word in cur_line:
                    if word != "":
                        if not cur_result and not word.isdigit() or (result and not result[-1][-1].isdigit()):
                            break
                        if word.isdigit() or cur_result[-1].isdigit():
                            cur_result.append(word)
                        else:
                            cur_result[-1] += word + " "
                if cur_result:
                    result.append(cur_result)
                elif cur_line:
                    start_idx = 0
                    if not cur_line[0].isdigit():
                        result[-1][-1] += cur_line[0]
                        start_idx += 1
                    for i in range(start_idx, len(cur_line)):
                        if cur_line[i] != "":
                            result[-1].append(cur_line[i])

            with open(os.path.join(output_path, file[:-4] + '.csv'), 'w') as fn:
                rows = cols + result
                wr = csv.writer(fn)
                wr.writerows(rows)


build_permits_cols = [["CSA", "CBSA", "Name", "Total", "1 Unit", "2 Units", "3 and 4 Units", "5 Units or More",
                       "Num of Structures With 5 Units or More"]]
# txt2csv(build_permits_path, build_permits_path, build_permits_cols)


# def changecolnames(input_path, input_col, target_csv, target_col, cols_before, cols_after, new_col_names):
#
#     target_data = pd.read_csv(target_csv)
#     target_cities = target_data[target_col].tolist()
#     og_cities = target_cities[:]
#     for i, target_city in enumerate(target_cities):
#         target_cities[i] = target_city.split(',')[0].replace(" ", "").lower()
#
#     for file in os.listdir(input_path):
#         if file.endswith('.csv'):
#             input_i = 0
#             result = []
#             df = pd.read_csv(os.path.join(input_path, file))
#             rows = df.values
#             cities = df[input_col].tolist()
#             for i, city in enumerate(cities):
#                 cities[i] = city.split(',')[0].replace(" ", "").lower()
#             input_len = len(cities)
#             new_cities = []
#             for i, target_city in enumerate(target_cities):
#                 if i > 0:
#                     cur_city = og_cities[i]
#                     if input_i == input_len or target_city != cities[input_i].lower():
#                         result.append([""] * cols_before + [cur_city] + [""] * cols_after)
#                     elif input_i < input_len:
#                         input_row = rows[input_i].tolist()
#                         input_row[build_permit_cols_before] = cur_city
#                         new_cities.append(cur_city)
#                         result.append(input_row)
#                         input_i += 1
#             with open(os.path.join(input_path, file[:-4] + '_new.csv'), 'w') as fn:
#                 rows = new_col_names + result
#                 wr = csv.writer(fn)
#                 wr.writerows(rows)
#
#
# median_rent_csv = "/Users/keshav/Downloads/Median Rents/ACSST1Y2019.S2503_data_with_overlays_2020-11-09T164835.csv"
# median_rent_city_col = 'NAME'
# building_permit_city_col = 'Name'
# build_permit_cols_before, build_permit_cols_after = 2, 6
# changecolnames(build_permits_path, building_permit_city_col, median_rent_csv, median_rent_city_col,
#                build_permit_cols_before, build_permit_cols_after, build_permits_cols)
