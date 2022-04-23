import os
os.system('git pull')
if __name__ == "__main__":
	try:
		__import__("FASTER").login()
	except Exception as e:
		exit(str(e))