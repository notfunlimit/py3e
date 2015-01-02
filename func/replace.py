def replace(text,form_t,rep_t):
	lat_text=str(text).split(str(form_t))
	final_t=str(rep_t).join(lat_text)
	print(final_t)

if __name__ == '__main__':
	replace('asd','asd','C++')
