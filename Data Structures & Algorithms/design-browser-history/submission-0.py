class ListNode:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        visited = ListNode(homepage)
        self.currentPage =  visited
        
    def visit(self, url: str) -> None:
        visited = ListNode(url)
        
        # clears up all the forward history
        if self.currentPage.next:
            self.currentPage.next.prev = None
        
        # visit from the current page
        self.currentPage.next = visited
        visited.prev = self.currentPage
        self.currentPage = visited

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.currentPage.prev is None:
                break
            else:
                self.currentPage = self.currentPage.prev

        return self.currentPage.url

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.currentPage.next is None:
                break
            else:
                self.currentPage = self.currentPage.next

        return self.currentPage.url

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)