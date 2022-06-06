import example_pb2

f = open("examplefile.txt","rb")
example2 = example_pb2.Example()
example2.ParseFromString(f.read())
f.close()

def test_b():
    assert example2.b == False #By default, field b is true.

def test_d():
    assert example2.d == 3.14

def test_r():
    assert len(example2.r) == 2
    assert example2.r[1].e == example_pb2.Example.E2