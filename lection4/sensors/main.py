import html_creator as hc
import xml_generator as xg
import data_provider as dp


# print(hc.create())
# print(xg.create())
xg.new_create(dp.data_collection())
hc.new_create(xg.new_create(dp.data_collection()))
