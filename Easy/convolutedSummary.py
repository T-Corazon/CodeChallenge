#~ The letters "A", "B", "C", "D" and "E" are the early letters in the 
#~ alphabet (and fairly common), and the letters "V", "W", "X", "Y", "Z" 
#~ are the late letters in the alphabet. To generate a summary of a line, 
#~ remove any other characters asides from the above 10 letters 
#~ (case-insensitive), then convert ABCDE into uppercase and vwxyz 
#~ into lowercase.
#~ Example
#~ For line = "Hello World", the output should be
#~ convolutedSummary(line) = "EwD".
#~ Input/Output
#~ [time limit] 4000ms (py3)
#~ [input] string line
#~ A sentence. It composes of letters and non-letters.
#~ Guaranteed constraints:
#~ 0 <= line.length <= 1000.
#~ [output] string
#~ The (highly convoluted) summary of the sentence. It retains ABCDEVWXYZ 
#~ from the source sentence and they are ported to the corresponding 
#~ letter casing.

def convolutedSummary(line):
	letter_list = []
	result = ''
	line_lower = line.lower()
	for letter in line_lower:
		if letter in 'abcde':
			letter_list.append(letter.upper())
			result += letter.upper()
		elif letter in 'vwxyz':
			letter_list.append(letter)
			result += letter
		else:pass
	return result

line = input("Put your string here:")
print(convolutedSummary(line))

	
	
