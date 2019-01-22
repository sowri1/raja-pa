import http.client as httplib
def in_on():
	conn = httplib.HTTPConnection("www.google.com", timeout=5)
	try:
		conn.request("HEAD", "/")
		conn.close()
		return True
	except:
		conn.close()
		return False
if __name__=="__main__":
	print(in_on())