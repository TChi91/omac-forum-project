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
        all_members = self.get_all()
        result = None
        for member in all_members:
            if member.id == id:
                result = member
                break
        return result

    def get_by_name(self,name):
        all_members = self.get_all()
        result = None
        for member in all_members:
            if member.name == name:
                result = name
                break
        return result

    def delete(self, id):
        member = self.get_by_id(id)
        MemberStore.members.remove(member)
        print "Member Deleted with success"

    def entity_exists(self, member):
        result = True
        if self.get_by_id(member.id) is None:
            result = False
        return result

    def update(self, member):
        result = member
        all_members = self.get_all()
        for index, current_member in enumerate(all_members):
            if current_member.id == member.id:
                all_members[index] = member
                break
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
        all_posts = self.get_all()
        result = None
        for post in all_posts:
            if post.id == id:
                result = post
                break
        return result

    def get_by_title(self,title):
        all_posts = self.get_all()
        result = None
        for post in all_posts:
            if post.title == title:
                result = title
                break
        return result

    def delete(self, id):
        post = self.get_by_id(id)
        if post is None:
            print "post doesn't exist"
        else:
            PostStore.posts.remove(post)
            print "Post Deleted with success"

    def entity_exists(self, post):
        result = True
        if self.get_by_id(post.id) is None:
            result = False
        return result