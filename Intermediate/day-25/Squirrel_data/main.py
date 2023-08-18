import pandas

squirrel_data = pandas.read_csv('228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')

fur_color = squirrel_data['Primary Fur Color']

# fur_color_list = fur_color.to_list()
# print(fur_color_list)

# for color in fur_color_list:
#     fur_color[color] = fur_color[fur_color == color]

fur_color_gray = fur_color[fur_color == 'Gray']
fur_color_gray_number = fur_color_gray.size

fur_color_red = fur_color[fur_color == 'Cinnamon']
fur_color_red_number = fur_color_red.size


fur_color_black = fur_color[fur_color == 'Black']
fur_color_black_number = fur_color_black.size


squirrel_data_dict = {
    "Fur Color" : ["gray", "red", "black"],
    "Count": [fur_color_gray_number, fur_color_red_number, fur_color_black_number]
}

squirrel_data_frame = pandas.DataFrame(squirrel_data_dict)
squirrel_data_frame.to_csv("squirrel_count.csv")

