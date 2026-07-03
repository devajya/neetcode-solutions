class Twitter:

    def __init__(self):
        self.timer = 0
        self.posts = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timer += 1
        self.posts[userId].append((self.timer, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = [self.posts[userId][::-1]]
        for followee in self.follows[userId]:
            feed.append(self.posts[followee][::-1])
        
        merged_feed = heapq.merge(*feed, key=lambda x: x[0], reverse=True)

        ans = []
        for _ in range(10):
            try: 
                ans.append(next(merged_feed)[1])
            except StopIteration:
                break
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
