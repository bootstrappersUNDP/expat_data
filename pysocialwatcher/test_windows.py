from pysocialwatcher import watcherAPI
from multiprocessing import freeze_support

if __name__ == '__main__':
	freeze_support()
	watcher = watcherAPI()
	watcher.load_credentials_file("pysocialwatcher/credentials.csv")
	watcher.run_data_collection("pysocialwatcher/input_examples/undp_country.json", "data/")
	# watcher.print_search_targeting_from_query_dataframe("Lived in Serbia")
	# watcherAPI.print_geo_locations_given_query_and_location_type(None, ["region"])