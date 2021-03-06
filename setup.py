from setuptools import setup

setup(
	name='orpheus',
	version='1.0.1',
	description='OrpheusDB command line tool',
	packages=['orpheus', 'orpheus.main'],
	url='http://orpheus-db.github.io/',
    # py_modules=['db',
	 		# 	'encryption',
	 		# 	'metadata',
	 		# 	'orpheus_const',
	 		# 	'orpheus_exceptions',
	 		# 	'orpheus_sqlparse',
	 		# 	'relation',
	 		# 	'orpheus_schema_parser',
	 		# 	'user_control',
	 		# 	'version',
	 		# 	'access',
	 		# 	'click_entry'],
	#py_modules=['click_entry'],
	install_requires=[
	    'Click', 'psycopg2', 'PyYAML', 'pandas', 'pyparsing', 'sqlparse'
		#'Click'
	],
	license='MIT',
	entry_points='''
		[console_scripts]
		orpheus=orpheus.main.click_entry:cli
	'''
)
