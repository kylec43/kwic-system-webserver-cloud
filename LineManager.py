class LineManager:

	def __init__(self, lines):
		self._lines = lines

	def getLines(self):
		return self._lines

	def getLineCount(self):
		return len(self._lines)


	def getOffsetLine(self, line_number, offset):
		line = None
		if offset != 0:
			line = self._lines[line_number][offset:] + " " + self._lines[line_number][:offset-1]
		else:
			line = self._lines[line_number][offset:] + " " + self._lines[line_number][:offset]

		return line

	def getLineLength(self, line_index):
		return len(self._lines[line_index])

	def getChar(self, line_index, char_index):
		return self._lines[line_index][char_index]
