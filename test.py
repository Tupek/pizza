def f():
    print('elo')

def decorator(func):
    print('to najpierw')
    dict1 = {}
    array = []
    import pdb
    pdb.set_trace()
    func()

print(decorator(f))

