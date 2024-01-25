class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> d = new HashMap<>();
        d.put('[',']');
        d.put('{','}');
        d.put('(',')');
        Stack<Character> myStack = new Stack<>();
        for (int i=0; i<s.length(); i++){
            char presentChar = s.charAt(i);
            if(d.containsKey(presentChar))
                myStack.push(presentChar);
            else if(!myStack.isEmpty() && d.get(myStack.peek()) == presentChar) 
                myStack.pop();
            else 
                return false;
        }

        return myStack.isEmpty();
        }
    }