def fix_cr(input_file,out_file):
	temp_line = ''
	for line in input_file:
		# first number is actual record length
		if len(line[:-1]) == 2991:
			out_file.write(line)
		else:
			temp_line += line[:-1] + ' '
			#print len(temp_line)
			#second number is record length plus one
			if len(temp_line) == 2992:
				out_file.write(temp_line[:-1] + '\n')
				temp_line = ''
