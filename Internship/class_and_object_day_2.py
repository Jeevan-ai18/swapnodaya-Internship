# For the Given code add the comments, Creator_name, Location and their display methods .
# Note comments should be a list of strings.
#
# Add a delete method to delete the last comments when ever that method is
# called with respective object.


class Instagram:
    def __init__(self, title, description, comments, creator_name, location):
        self.title = title
        self.description = description
        self.likes = 0
        self.comments = comments
        self.creator_name = creator_name
        self.location = location

    def display_title(self):
        print("The title of the reel is ", self.title)

    def display_description(self):
        print("The description of the reel is ", self.description)

    def display_likes(self):
        print("The likes of the reel is ", self.likes)

    def liked(self):
        self.likes += 1

    def disliked(self):
        if self.likes > 0:
            self.likes -= 1

    def addcommments(self, comments):
        self.comments += comments

    def deletecomments(self):
        if self.comments:
            self.comments.pop()

    def Dcomments(self):
        print("The comments")
        for c in self.comments:
            print(c)

    def Dcreator_name(self):
        print("The creator of the reel is ", self.creator_name)

    def Dlocation(self):
        print("The location of the reel is ", self.location)


reel1 = Instagram("dancing", "dancing with friends", ["nice dancing", "car", "crazy"], "jeevan", "banglore")
# 0
reel1.disliked()  # 0
reel1.liked()  # 1
reel1.Dcomments()
reel1.deletecomments()
reel1.Dcreator_name()
reel1.Dlocation()
reel1.Dcomments()

reel2 = Instagram("finance minister conference", "finance minister conference with friends", "good", "jeevan1",
                  "mandya")
reel1.liked()  # 2
# 0
reel2.liked()  # 1
reel1.disliked()  # 1
reel1.display_likes()
reel2.display_likes()

print(id(reel1))
print(id(reel2))
