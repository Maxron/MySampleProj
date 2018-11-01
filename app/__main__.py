from app.domain.sayHelloUseCase import SayHello
from app.demo import Demo

def runUseCase():
    print("Hello world")
    hello = SayHello("Wei")
    hello.hello()

def runDemo():
    demo = Demo()
    demo.runDemo()

def main():
    runDemo()
    runUseCase()

if __name__ == '__main__':
    main()