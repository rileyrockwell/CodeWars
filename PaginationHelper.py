# TODO: complete this class

class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
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
        else:
            return page_count + 1

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        ## if page_index is not in the valid range, return -1 ##
        if page_index > (self.page_count() - 1):
            return -1
        elif page_index < 0:
            return -1

        ## if page_index is in the valid range ##
        items_on_last_page = len(self.collection) % self.items_per_page
        complete_pages = self.item_count() // self.items_per_page

        # the page index for a complete page is always less than the
        # number of complete pages
        if page_index < complete_pages:
            return self.items_per_page

        # the page index for an incomplete page is always 1 more than the
        # number of complete pages
        else:
            return items_on_last_page

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        ## if item_index is not in the valid range, return -1 ##
        if item_index > (len(self.collection) - 1):
            return -1
        elif item_index < 0:
            return -1

        ## if item_index is in the valid range ##
        page_num_array = []

        # create 'reference list' for the eventual dictionary
        array_values = [i for i in range(len(self.collection))]

        # build the page_num_array
        for i in range(len(self.collection)):
            page_num_array.append(i // self.items_per_page)

        # dictionary comprehension for reference
        dict_1 = {k: v for (k, v) in zip(array_values, page_num_array)}

        # reference dictionary comprehension
        return dict_1[item_index]


if __name__ == "__main__":
    helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)

    '''
    print(helper.page_count())  # should == 2
    print(helper.item_count())  # should == 6
    print(helper.page_item_count(0))  # should == 4
    print(helper.page_item_count(1))  # last page - should == 2
    print(helper.page_item_count(2))  # should == -1 since the page is invalid
    print("error")
    # page_index takes an item index and returns the page that it belongs on
    print(helper.page_index(5))  # should == 1 (zero based index)
    print(helper.page_index(2))  # should == 0
    print(helper.page_index(20))  # should == -1
    print(helper.page_index(-10))  # should == -1 because negative indexes are invalid

    print(helper.page_item_count(4))
    print(helper.page_index(5))
    '''
    collection = range(1, 25)
    helper = PaginationHelper(collection, 10)

    assert helper.page_count() == 3, 'page_count is returning incorrect value.'
    assert helper.page_index(23) == 2, 'page_index returned incorrect value'
    assert helper.item_count() == 24, 'item_count returned incorrect value'
