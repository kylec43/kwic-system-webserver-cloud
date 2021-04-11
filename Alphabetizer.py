class Alphabetizer:

	def __init__(self, line_manager, offsets):

		self._sortedOffsets = offsets
		self._qs(line_manager, self._sortedOffsets, 0, len(self._sortedOffsets)-1)


	#Return alphabetized lines
	def GetSortedOffsets(self):
		return self._sortedOffsets


	#quick sort lines in list
	def _qs(self, line_manager, offsets, low, high):

		if low < high:
			part = self._partition(line_manager, offsets, low, high)
			self._qs(line_manager, offsets, part+1, high)
			self._qs(line_manager, offsets, low, part-1)


	def _partition(self, line_manager, offsets, low, high):

		last_small = low-1
		pivotIndex = offsets[high][0]
		pivotOffset = offsets[high][1]

		for i in range(low, high, 1):

			lineIndex = offsets[i][0]
			lineOffset = offsets[i][1]
			if self._lesserThan(line_manager, lineIndex, pivotIndex, lineOffset, pivotOffset):
			#if self._lineOffsetLesserThanPivot(line_manager, line_offset, pivot_offset):
				last_small += 1
				offsets[i], offsets[last_small] = offsets[last_small], offsets[i]

		offsets[last_small+1], offsets[high] = offsets[high], offsets[last_small+1]

		return last_small+1

	

	def _lesserThan(self, lineManager, lineIndex, pivotIndex, lineOffset, pivotOffset):
		
		
		index_i = lineOffset
		index_pivot = pivotOffset

		while True:

			if lineManager.getChar(lineIndex, index_i).isalpha() and lineManager.getChar(pivotIndex, index_pivot).isalpha():
				#check if equal char
				if lineManager.getChar(lineIndex, index_i).lower() == lineManager.getChar(pivotIndex, index_pivot).lower():

					#check if i is capital
					if lineManager.getChar(lineIndex, index_i).isupper() and lineManager.getChar(pivotIndex, index_pivot).islower():
						return False
					#check if pivotIndex is capital
					elif lineManager.getChar(lineIndex, index_i).islower() and lineManager.getChar(pivotIndex, index_pivot).isupper():
						return True
				#if not equal check which is lesser
				else:
					return lineManager.getChar(lineIndex, index_i).lower() < lineManager.getChar(pivotIndex, index_pivot).lower()
			else:
				while not lineManager.getChar(lineIndex, index_i).isalpha():
					index_i += 1
					if index_i == lineManager.getLineLength(lineIndex):
						index_i = 0
					if index_i == lineOffset:
						return True
				while not lineManager.getChar(pivotIndex, index_pivot).isalpha():
					index_pivot += 1
					if index_pivot == lineManager.getLineLength(pivotIndex):
						index_pivot = 0
					if index_pivot == pivotOffset:
						return False
				continue


			index_i += 1
			index_pivot += 1

			if index_i == lineManager.getLineLength(lineIndex):
				index_i = 0
			if index_pivot == lineManager.getLineLength(pivotIndex):
				index_pivot = 0

			if index_i == lineOffset:
				return True
			if index_pivot == pivotOffset:
				return False
