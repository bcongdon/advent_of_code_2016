import java.util.HashMap;
import java.util.Queue;
import java.util.LinkedList;
import java.util.ArrayList;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

import java.io.UnsupportedEncodingException;

import java.math.BigInteger;

class State {
    public final int x;
    public final int y;
    public final String path;
    public State(int x, int y, String path){
        this.x = x;
        this.y = y;
        this.path = path;
    }
}

class Day17 {

    static boolean PART2 = false;

    static String pathfind(String key){
        Queue<State> bfs_q = new LinkedList<State>();
        String max_sol = "";
        bfs_q.add(new State(0, 0, ""));
        while(bfs_q.peek() != null) {
            State c = bfs_q.remove();
            if(c.x > 3 || c.x < 0 || c.y > 3 || c.y < 0) continue;
            if(c.x == 3 && c.y == 3) {
                if(PART2){
                    if(c.path.length() > max_sol.length()){
                        max_sol = c.path;
                    }
                    continue;
                }
                else {
                    return c.path;
                }
            }
            String h = get_hash(key + c.path).substring(0, 4);
            if("bcdef".indexOf(h.charAt(0)) != -1){
                bfs_q.add(new State(c.x, c.y - 1, c.path + "U"));
            }
            if("bcdef".indexOf(h.charAt(1)) != -1){
                bfs_q.add(new State(c.x, c.y + 1, c.path + "D"));
            }
            if("bcdef".indexOf(h.charAt(2)) != -1){
                bfs_q.add(new State(c.x - 1, c.y, c.path + "L"));
            }
            if("bcdef".indexOf(h.charAt(3)) != -1){
                bfs_q.add(new State(c.x + 1, c.y, c.path + "R"));
            }
        }
        return max_sol;
    }

    static String get_hash(String key){
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] dig = md.digest( key.getBytes("UTF-8"));
            return bytesToHex(dig);
        }
        catch (NoSuchAlgorithmException e){
            System.out.println(e);
        }
        catch (UnsupportedEncodingException e){
            System.out.println(e);
        }
        return "";
    }

    public static String bytesToHex(byte[] b_arr) {
        final StringBuilder builder = new StringBuilder();
        for(int i = 0; i < b_arr.length; i++) {
            builder.append(String.format("%02x", b_arr[i]));
        }
        return builder.toString();
    }

    public static void main(String[] args) {
        System.out.println(pathfind("hijkl").equals(""));
        System.out.println(pathfind("ihgpwlah").equals("DDRRRD"));
        System.out.println(pathfind("kglvqrro").equals("DDUDRLRRUDRD"));
        System.out.println(pathfind("ulqzkmiv").equals("DRURDRUDDLLDLUURRDULRLDUUDDDRR"));

        System.out.println("Part 1: " + pathfind("veumntbg"));

        PART2 = true;

        System.out.println(pathfind("ihgpwlah").length() == 370);
        System.out.println(pathfind("kglvqrro").length() == 492);
        System.out.println(pathfind("ulqzkmiv").length() == 830);

        System.out.println("Part 2: " + pathfind("veumntbg").length());
    }
}
    