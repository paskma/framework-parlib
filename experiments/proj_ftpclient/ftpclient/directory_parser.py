
from ftp_file import FtpFile

_EXAMPLE = (
"drwxrwxr-x  283 0        3003        12288 Aug 30 18:45 gnu\r\n"
+
"-rwxrwxr-x  283 0        3003        12288 Aug 30 18:45 just file\r\n")

def parseListing(listing):
	result = []
	
	if listing is None:
		return None
	
	if len(listing) == 0:
		return result;
	
	lines = listing.split("\n") # character in RPython
	
	for i in lines:
		line = i.strip("\r") # because of the RPyhon split
		if not line:
			continue;
		
		if len(line) > 56:
			name = line[56:]
			isDir = (line[0] == "d")
			result.append(FtpFile(name, isDir))
	
	return result
