from lexer import lexer
from parser import parser

code = '''
fn greet(name) {
    show "Hello " + name
}

x = 10
if x > 5 {
    show "Big"
} elseif x == 5 {
    show "Equal"
} else {
    show "Small"
}

repeat 5 {
    show x
}

class Dog {
    show "Dog created"
}
'''

parser.parse(code)
