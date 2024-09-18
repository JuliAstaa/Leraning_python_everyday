"""  
Given twwo arrays a and b write a function comp(a, b), that checks whether the two arrays have the "same" elements, with the same multiplicaties (the multiplicity of a number is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order

Exmaple: 
input: a = [121, 144, 19, 161, 19, 144, 19, 11] 
       b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
output: True
explanation: a = [121, 144, 19, 161, 19, 144, 19, 11] 
             b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]


Remarks:
- a or b might be [] or {} 
- a or b  might be nil or null or None or nothing (except in C++, COBOL, Crystal, D, Dart, Elixir, Fortran, F#, Haskell, Nim, OCaml, Pascal, Perl, PowerShell, Prolog, PureScript, R, Racket, Rust, Shell, Swift).

If a or b are nil (or null or None, depending on the language), the problem doesn't make sense so return false.
"""

def comp(array1, array2):
    if array1 is None or array2 is None: return False
    
    dipangkatkan = [x ** 2 for x in array1]

    return sorted(dipangkatkan) == sorted(array2)
    
    

print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 36100, 25921, 361, 20736, 361]))
