from collections import deque

# breadth first algorythm
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['tom', 'johny']
graph['anuj'] = []
graph['peggy'] = []
graph['tom'] = []
graph['johny'] = []


def search(name):
    search_queue = deque() # we formed a queue
    search_queue += graph['you'] # we added first pack ('you') to the queue
    searched = []

    while search_queue: #while queue is not empty
        person = search_queue.popleft() # take the first person in queue and check is he a seller
        if not person in searched:
            if person_is_seller(person):
                print(f'{person} is a mango seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


def person_is_seller(name):
    return name[-1] == 'mw '

print(search('you'))