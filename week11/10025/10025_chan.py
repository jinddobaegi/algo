import sys
sys.stdin = open('week11/10025/10025.txt')
input = sys.stdin.readline

def max_catch_ice():
    global max_ice
    for bearpositon in range(magichand, len(newplace)-magichand):
        print("bearpositon",bearpositon)
        catch_ice = 0
        for j in range(bearpositon-magichand, bearpositon+magichand+1):
            print("j",j)
            catch_ice += newplace[j]
        if catch_ice > max_ice:
            max_ice = catch_ice
    

baskets, magichand = map(int, input().split())
print("magichand",magichand)
place = [0] * 1000001
find_maxlocation = 0
max_ice = 0
for _ in range(baskets):
    ice, location = map(int, input().split())
    place[location] = ice
    if find_maxlocation < location:
        find_maxlocation = location

newplace = place[:find_maxlocation+1]
print("newplace",newplace)

max_catch_ice()

print(max_ice)


