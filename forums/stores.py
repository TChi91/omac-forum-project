class MemberStore:
    members = []
    last_id = 1

    def get_all(self):
        return MemberStore.members

    def add(self, member):
            member.id = MemberStore.last_id
            MemberStore.members.append(member)
            MemberStore.last_id += 1

    def get_by_id(self, id):
        all_members = MemberStore.members
        result = None
        for member in all_members:
            if member.id == id:
                result = member
                break
        return result

    def delete(self, id):
        member = self.get_by_id(id)
        if member is None:
            print "Member doesn't exist"
        else:
            MemberStore.members.remove(member)
            print "Member Deleted with success"


    def entity_exists(self, member):
        result = True
        if self.get_by_id(member.id) is None:
            result = False
        return result




class PostStore:
    posts = []
    last_id = 1

    def get_all(self):
        return PostStore.posts

    def add(self, post):
        post.id = PostStore.last_id
        PostStore.posts.append(post)
        PostStore.last_id += 1

    def get_by_id(self,id):
        all_posts = PostStore.posts
        result = None
        for post in all_posts:
            if post.id == id:
                result = post
                break
        return result

    def delete(self,id):
        for post in PostStore.posts:
            if post.id == id:
                PostStore.posts.remove(post)
                print "Post deleted with success"
                break
            print "post doesn't exist"

    def entity_exists(self,post):
        if post in PostStore.posts:
            print "Post exist"
        else:
            print "Post doesn't exist"
