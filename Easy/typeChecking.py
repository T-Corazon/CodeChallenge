#~ You have created a simple programming language. Right now, it only 
#~ supports variable declaration statements, number and string types, 
#~ and several operations on them.

#~ Values of string type can be concatenated via + operation and can be 
#~ created using string literals of the form '<any char except '>', i.e. 
#~ it's a sequence of characters enclosed in single quotes.

#~ Values of the number type support all common arithmetic 
#~ operations: +, -, *, and /. number is an arbitrary-precision number that
 #~ can be created using number literals of the form <one or more decimal 
 #~ digits><dot . or nothing><zero or more digits>. In other words, it's a 
 #~ sequence of digits (0-9), possibly separated by or ending on a dot ..

#~ Variable declaration statements or let statements assign a value to a 
#~ certain identifier, and have the form 
#~ let <id> = <id or literal> <<op> <id or literal> zero or more times>, 
#~ where id is a Latin letter followed by zero or more Latin letters or 
#~ digits and op is one of +, -, * or /. Note that each token in the let 
#~ statement can be separated by more than 1 space.

#~ To make writing programs easier while catching as many errors at
 #~ compile time as you can, you decided to implement type inference 
 #~ in your language.

#~ Since your language is rather basic, the type checking algorithm is 
#~ simple. You just need to check that:

#~ The variable in the let statement has the same type as the right-hand side;
#~ String literals have string type and number literals have number type;
#~ Arithmetic operations can only be applied to values of number type, and 
#~ strings can only be concatenated with other strings.
#~ Given the the sequence of let statements as the array codeLines, where
 #~ each string is a new let statement, check whether all operations are 
 #~ applied to the values of the proper type.

#~ Return "OK" if there were no typing errors. Or, if there are typing
 #~ errors, return the first line with mismatched types.

#~ It's guaranteed that all lines in codeLines represent syntactically 
#~ valid let statements, i.e. there only could be type errors.

#~ Example

#~ For codeLines = ["let x = y + 2", "let y = 1.5"], the output should be
#~ typeChecking(codeLines) = "OK"
#~ For codeLines = ["let x = 12 + 42 - '1'"], the output should be
#~ typeChecking(codeLines) = "let x = 12 + 42 - '1'"
#~ You would return this line because you can't subtract strings and numbers.

#~ For codeLines = ["let x = 0 * y", "let y = '0'"], the output should be
#~ typeChecking(codeLines) = "let y = '0'"
#~ From let x = 0 * y, you can infer that y must be a number, but in 
#~ let y = '0' it is assigned a string which causes an typing error in 
#~ that line.

#~ Input/Output

#~ [time limit] 4000ms (py3)
#~ [input] array.string codeLines

#~ An array of syntactically correct let statements representing the 
#~ consecutive lines of code.
#~ All tokens (id, op, etc.) in the statement are separated by an arbitrary
 #~ positive number of spaces ().

#~ Guaranteed constraints:
#~ 1 <= codeLines.length <= 5*10^4,
#~ 9 <= codeLines[i].length <= 180.

#~ [output] string

#~ Return "OK" if there were no typing errors, or else return the first
 #~ line with mismatched types otherwise.
 
def typeChecking(codeLines):



