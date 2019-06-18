import random

syllabary = []
vowels = { 'a', 'i', 'e', 'o', 'u' }
consonants = { 'd', 't', 's', 'z', 'k', 'g', 'h', 'b', 'p', 'm', 'n', 'w', 'y' }
for c in consonants:
    syllabary.extend([f'{c}{v}' for v in vowels])

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        

        for i in range(numUsers):
            # generates random names using a syllabary, somewhat unnaturally!
            randomName = ''
            for i in range(random.randrange(2,5)):
                randomName += syllabary[random.randrange(0,len(syllabary))]
            self.addUser(randomName.capitalize())

        for user in self.users:
            for i in range(random.randrange(0,avgFriendships*2+1)):
                randomFriend = random.randrange(1,len(self.users))

                if randomFriend == user or randomFriend in self.friendships.get(user):
                    i -= 1
                elif randomFriend < user:
                    self.addFriendship(randomFriend, user)
                else:
                    self.addFriendship(user, randomFriend)

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        queue = [ [userID] ]
        visited = { } # Note that this is a dictionary, not a set
        verts = self.friendships

        for i in range(len(verts)):
            path = queue.pop(0)
            visit = path[-1]
            branches = set(self._unvisited_edges(visit,visited))
            for i in branches:
                full_path = path + [i]
                visited[i] = full_path
                queue.append(full_path)

            if len(queue) == 0:
                break

        return visited

    def _unvisited_edges(self, vertex, visited):
        verts = self.friendships
        return [i for i in verts.get(vertex) if i not in visited]


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
