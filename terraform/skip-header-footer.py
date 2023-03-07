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
