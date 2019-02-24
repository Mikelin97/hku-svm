import requests


def getfile(string): 
	file_url = "https://legalref.judiciary.hk/doc/judg/word/vetted/other/en/2018/DCCC000731_2018.docx"

	r = requests.get(file_url, stream = True) 

	with open("python.docx", "wb") as docx: 
		
		for chunk in r.iter_content(chunk_size = 1024): 
			if chunk: 
				docx.write(chunk) 


