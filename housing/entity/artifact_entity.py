from collections import namedtuple
from unicodedata import name



DataIngestionArtifact = namedtuple("DataIngestionfact",["train_file_path","test_file_path","is_ingested","message"])

DataValidationArtifact = namedtuple("DataValidationArtifact",
["schema_file_path","report_file_path","report_page_file_path","is_validated","message"])

DataTransformationArtifact = namedtuple("DataTrasformationArtifact",
["is_transformed","message","transformed_train_file_path","transformed_test_file_path","preprocessed_object_file_path"])

