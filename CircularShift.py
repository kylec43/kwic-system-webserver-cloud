class CircularShift:

	def __init__(self, lineManager, noiseWords):

		self._offsets = []
		self._getWordOffsets(lineManager, noiseWords)

		


	def getOffsets(self):
		return self._offsets



	def _getWordOffsets(self, lineManager, noiseWords = None):

		i = 0
		while i < lineManager.getLineCount():

			if lineManager.getLineLength(i) == 0:
				i+=1
				continue
			
			
			last_char = ''
			offset_index = 0
			k = 0
			word = ''
			while k < lineManager.getLineLength(i):


				currentChar = lineManager.getChar(i, k)

				if currentChar == ' ' and last_char == ' ':
					k += 1
					continue
				elif currentChar == ' ' and last_char != ' ':
					if word.lower() not in noiseWords:
						self._offsets.append([i, offset_index])
					word = ''
				elif currentChar != ' ' and last_char != ' ':
					word += currentChar
				else:
					word += currentChar.lower()
					offset_index = k

				last_char = currentChar
				k += 1		

			if last_char != ' ':
				self._offsets.append([i, offset_index])
				
			i+=1



			
		


	