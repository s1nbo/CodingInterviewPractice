#include <vector>
class MyHashMap {
public:
    std::vector<int> map; 
    MyHashMap() {
    }
    
    void put(int key, int value) {
        while(map.size() <= key){
            map.push_back(-1);
        }
        map[key] = value;
        return;
    }
    
    int get(int key) {
        if(map.size() <= key){
            return -1;
        }
        return map[key];
    }
    
    void remove(int key) {
        if(map.size() < key){
            return;
        }
        map[key] = -1;
        return;
    }
};
/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */