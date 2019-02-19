from scrapy.conf import settings 
from scrapy.exporters import CsvItemExporter 

class KjriCsvItemExporter(CsvItemExporter): 

	def __init__(self, *args, **kwargs): 
		delimiter = settings.get('CSV_DELIMITER', ',')
		kwargs['delimiter'] = delimiter

		fiedls_to_export = settings.get('FIEDLS_TO_EXPORT', [])

		if fiedls_to_export: 
			kwargs['fiedls_to_export'] = fiedls_to_export

		super(KjriCsvItemExporter, self).__init__(*args, **kwargs)
