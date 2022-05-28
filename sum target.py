def search(terms=[]):
    total=sum(j for j in terms)
    if total>target:
        return
    if total==target:
        print(terms)
        return
    if total<target:
        for i in items:
            terms+=[i]
            search(terms)
            terms.pop()
    
def fill_items(items):
    x=1
    while x!=0 :
        x=int(input('give a number: '))
        items+=[x]
    items.pop()

items=[]
fill_items(items)
print(items)
target=int(input('give the target: '))
search()