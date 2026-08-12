tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
def usingstack(t):
    stack=[]
    for i in t:
        if i not in "+-*/":
            stack.append(int(i))
        else:
            b=int(stack.pop())
            a=int(stack.pop())
            match (i):
                case ("+"):
                    stack.append(a+b)
                case ("*"):
                    stack.append(a*b)
                case ("-"):
                    stack.append(a-b)
                case ("/"):
                    stack.append(a/b)
    return stack[-1]
print(usingstack(tokens))