from pyexcel.cookbook import merge_all_to_a_book
import glob
def toxlsx():
	merge_all_to_a_book(glob.glob("data.csv"), "put.xlsx")
