# TODO: complete this class

# Contributors: Alan Hussey

'''
For this exercise you will be strengthening your page-fu mastery.
You will complete the PaginationHelper class,
which is a utility class helpful for querying paging information related to an array.
The class is designed to take in an array of values and an integer indicating how many
items will be allowed per each page. The types of values contained within the collection/array
are not relevant.

The following are some examples of how this class is used:
'''

class PaginationHelper:

    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        # instance properties
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        # check if number of items divides evenly fit into the number of pages,
        # and if not we know the last page will have less than the items_per_page
        # therefore, integer division will generate 1 page less than the
        # number of pages that we need.
        item_count = self.item_count()
        page_count = item_count // self.items_per_page

        if item_count % self.items_per_page == 0:
            return page_count
        return page_count + 1

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        # if page_index equals 2 or greater, then return -1
        if page_index > (self.page_count() - 1):
            return -1
        elif page_index < 0:
            return -1

        # for page_index in the correct interval (i.e., 0 <= page_index <= self.page_count() - 1)
        items_on_last_page = self.item_count() % self.items_per_page
        complete_pages = self.item_count() // self.items_per_page

        # the page index for a complete page is always less than the number of complete pages
        if page_index < complete_pages:
            return self.items_per_page
        # the page index for an incomplete page is always 1 more than the number of complete pages
        else:
            return items_on_last_page

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        # create a dictionary ordering each array element with a corresponding integer value





if __name__ == "__main__":
    helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], 4)

    print(helper.item_count())  # should == 6
    print(helper.page_count())  # should == 2
    print(helper.page_item_count(0))  # should == 4
    print(helper.page_item_count(1))  # last page - should == 2
    print(helper.page_item_count(2))  # should == -1 since the page is invalid

    # page_index takes an item index and returns the page that it belongs on
    # helper.page_index(5)  # should == 1 (zero based index)
    # helper.page_index(2)  # should == 0
    # helper.page_index(20)  # should == -1
    # helper.page_index(-10)  # should == -1 because negative indexes are invalid

    print(helper.page_index(0))
    print(helper.page_index(3))
    print(helper.page_index(4))
    print(helper.page_index(7))
    print(helper.page_index(8))
    print(helper.page_index(9))