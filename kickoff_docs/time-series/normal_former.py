#normal_former package

#import Pandas to import csv
import pandas as pd


#ask user to specify the file that they would like to import
def getFile():
	file_location = input('Where is your file located?  I can work with either csv or xlsx files: ')
	file_type = None
	file_n_type = ()
	
	if file_location.endswith('csv'):
		file_type = 'csv'
		file_n_type = [file_location, file_type]
		return file_n_type
	elif file_location.endswith('xlsx'):
		file_type = 'xlsx'
		file_n_type = [file_location, file_type]
		return file_n_type
	else:
		while file_n_type[1] == 'rerun':
			print('Sorry, that was in invalid entry, please enter a valid directory...')
			file_n_type = getFile()
		return ['invalid file location', 'rerun']


#returns a list of the filename and filetype of the
#csv or xlsx provided by user

def getFileType(filename):
	filetype = None
	valid = None
	if filename.endswith('csv') == True:
		filetype = 'csv'
		valid = True
	elif filename.endswith('xlsx') == True:
		filetype = 'xlsx'
		valid = True
	else:
		valid = False
	
	results = [valid, filetype]
		
	return results


#create a new dictionary based on the source dataframe to inlcude:
#keys, column name, and cast of row or column

def updateDict(cols2rows, cols_n_numbers):
	combined = {}
	for col in cols_n_numbers:
		if col not in cols2rows:
			combined[col] = [cols_n_numbers[col], 'column']
		else:
			combined[col] = [cols_n_numbers[col], 'row']
	return combined


#user input for columns that should be row data

def collectRows():
	selection = input('Select columns you\'d like to be rows:')
	return selection


#create df from user specified file

def getDF(file_n_type):
	if file_n_type[1] == 'csv':
		df = pd.read_csv(file_n_type[0])
		return df
	else:
		df = pd.read_excel(file_n_type[0])
		return df


def indexCols(df):
	cols_n_index = []
	for col in enumerate(df.columns):
		cols_n_index.append(col)

	return cols_n_index


def showCols(cols_n_index):
	print('These are the columns with which we\'re working:')
	for index, col in cols_n_index:
		print(str(index) + ': ' + col)



def pickRows(cols_n_index):
	max_col = len(cols_n_index)
	col_count = 0
	cols2rows = []
	selection = 0
	
	print("Enter the number of the column you want to make a row instead. Enter 'x' to exit:")
	user_val = ''
	col_count = 0

	user_val = collectRows()

	while user_val != str('x'): 	
		if int(user_val) > 0 and int(user_val)<= max_col:
			cols2rows.append(int(user_val))
			col_count += 1
		else:
			print('Column out of range and not added to selection, try again...')

		user_val = collectRows()

	count = 0

	return cols2rows

def index_c2r(cols_n_index, cols2rows):
	cols2rows_index = []

	for index, _ in cols_n_index:
		if index in cols2rows:
			cols2rows_index.append(cols_n_index[index])

	return cols2rows_index



def print_c2r(c2ri):
	print('We are going to make the following columns rows:')

	for index, col in c2ri:
		print('Row ' + str(index) + ' named ' + str(col))



def keep_df(og_df, cols2rows):

	keep_cols_df = og_df

	for key, col in cols2rows:
		keep_cols_df = keep_cols_df.drop(col, axis=1)

	return keep_cols_df



def make_shell(c2ri, keep_df):
	tab_df = keep_df
	concat_count = range(1, len(c2ri))

	for count in concat_count:
		tab_df = pd.concat([keep_df, tab_df], axis=0)

	return tab_df



def add_cols2shell(keep_df, tab_df):
	keep_cols_width = keep_df.shape[1]
	
	tab_df['Date'] = ''
	tab_df['Value'] = ''



def dates2rows(c2ri, og_df, tab_df):
	dates = []

	for index, date in c2ri:
		count = 0
		while count < og_df.shape[0]:
			dates.append(date)
			count += 1

	tab_df['Date'] = dates



def vals2rows(c2ri, og_df, tab_df):
	values = []
	col_vals = []

	for index, _ in c2ri:
		row = 0
		while row < og_df.shape[0]:
			values.append(og_df.iat[row, index])
			row += 1

	tab_df['Value'] = values



def export_csv(tab_df, name):
	tab_df.to_csv(name)


































