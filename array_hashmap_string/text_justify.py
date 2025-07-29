def justify(words, max_width):
	"""
	Justify words in a given array so that each line is max_width characters long and
	there are no spaces at the end of each line.
	"""
	# current line as a list of words
	_curr_line = []
	# width of current line without spaces
	_curr_width = 0
	res = []
	for word in words:
		# if we can't add current word to current line
        # current word len (without spaces) + new word + space count if new word will be added
		if len(_curr_line) + len(word) + _curr_width > max_width:
			# distribute spaces between words in current line
			for i in range(max_width - _curr_width):
                # spaces go between words (not after the last one).
                # if there's only one word in the line, it avoids division by zero
				_curr_line[i % (len(_curr_line) - 1 or 1)] += ' '
			# add current line to result and reset current line and width
			res.append(''.join(_curr_line))
			_curr_line = []
			_curr_width = 0
		# add word to current line
		_curr_line.append(word)
		# increase current width
		_curr_width += len(word)
	# add last line to result
	res.append(' '.join(_curr_line).ljust(max_width))
	return res

print(justify(["This", "is", "an", "example", "of", "text", "justification."], 16))