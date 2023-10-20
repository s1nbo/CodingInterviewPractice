#include <vector>

// This is the interface that allows for creating nested lists.
// You should not implement it, or speculate about its implementation
class NestedInteger {
    public:
        // Return true if this NestedInteger holds a single integer, rather than a nested list.
        bool isInteger() const;

        // Return the single integer that this NestedInteger holds, if it holds a single integer
        // The result is undefined if this NestedInteger holds a nested list
        int getInteger() const;
 
        // Return the nested list that this NestedInteger holds, if it holds a nested list
        // The result is undefined if this NestedInteger holds a single integer
        const std::vector<NestedInteger> &getList() const;
 };
 

 class NestedIterator {
    public:
        std::vector<int> ans;
        int idx = 0;
        NestedIterator(std::vector<NestedInteger> &nestedList) {
            nestedIterator(nestedList);
        }
    
        void nestedIterator(const std::vector<NestedInteger> &nested){
            for(const auto& cur : nested){
                if(cur.isInteger()) ans.push_back(cur.getInteger());
                else nestedIterator(cur.getList());
            }
        }
        
        int next() {
            return ans[idx++];
        }
        
        bool hasNext() {
            return idx < ans.size();
        }
    };
    
    /**
     * Your NestedIterator object will be instantiated and called as such:
     * NestedIterator i(nestedList);
     * while (i.hasNext()) cout << i.next();
     */