class Twitter:

    def __init__(self):
        self.count = 0
        self.followmap = defaultdict(set)
        self.tweetmap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.count,tweetId])
        self.count +=1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxheap = []
        res = []
        self.followmap[userId].add(userId)
        for foloweeId in self.followmap[userId]:
            if foloweeId in self.tweetmap:
                index =len(self.tweetmap[foloweeId])-1
                count, tweetid = self.tweetmap[foloweeId][index]
                maxheap.append([count,tweetid,foloweeId, index-1])
        heapq.heapify_max(maxheap)

        while maxheap and len(res)<10:
            count,tweetid, foloweeId, index= heapq.heappop_max(maxheap)
            res.append(tweetid)
            if index>=0:
                count , tweetid = self.tweetmap[foloweeId][index]
                heapq.heappush_max(maxheap,[count,tweetid,foloweeId,index-1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
