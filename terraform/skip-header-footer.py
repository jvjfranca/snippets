from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame

# Create a GlueContext object
glueContext = GlueContext(SparkContext.getOrCreate())

# Define the CSV file path
file_path = '/path/to/csv/file'

# Define the options for reading the file
options = {
    'header': 'true',  # Skip the header row
    'footer': '2'      # Skip the last 2 rows (trailer)
}

# Read the CSV file into a DynamicFrame, ignoring the header and trailer rows
dynamic_frame = glueContext.create_dynamic_frame.from_options(
    'csv',
    options=options,
    format='csv',
    path=file_path
)

# Convert the DynamicFrame to a DataFrame and show the first 10 rows
data_frame = dynamic_frame.toDF()
data_frame.show(10)


###


# Create a GlueContext object
glueContext = GlueContext(SparkContext.getOrCreate())

# Define the table name in the Glue Data Catalog
table_name = 'my_table'

# Define the options for reading the file
options = {
    'header': 'true',  # Skip the header row
    'footer': '2'      # Skip the last 2 rows (trailer)
}

# Create a DynamicFrame from the catalog table, ignoring the header and trailer rows
dynamic_frame = glueContext.create_dynamic_frame.from_catalog(
    database='my_database',
    table_name=table_name,
    transformation_ctx='my_dynamic_frame',
    additional_options=options
)

# Convert the DynamicFrame to a DataFrame and show the first 10 rows
data_frame = dynamic_frame.toDF()
data_frame.show(10)
