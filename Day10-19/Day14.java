import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.util.HashMap;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

import java.io.UnsupportedEncodingException;

import java.math.BigInteger;


class Day14 {
    static boolean PART2 = false;
    static HashMap<String, String> digest_map = new HashMap<String, String>();
    static final Pattern three_pat = Pattern.compile("(.)\\1\\1");

    static String contains_triple(String s){
        Matcher m = three_pat.matcher(s);
        if(m.find()) {
            return m.group(1);
        }
        else{
            return "";
        }
    }

    static boolean contains_quintuple(String s, String c){
        Pattern p = Pattern.compile("([" + c + "])\\1\\1\\1\\1");
        Matcher m = p.matcher(s);
        return m.find();
    }

    static boolean is_key(String salt, int idx) {
        String hash = get_hash(salt, Integer.toString(idx));
        String c = contains_triple(hash);
        if(c.equals("")) {
            return false;
        }
        for(int i = 1; i < 1001; i++){
            hash = get_hash(salt, Integer.toString(idx + i));
            if(contains_quintuple(hash, c)) {
                return true;
            }
        }
        return false;
    }

    static String get_hash(String salt, String idx){
        if(digest_map.containsKey(salt + idx)) {
            return digest_map.get(salt + idx);
        }
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] dig = md.digest( (salt + idx).getBytes("UTF-8"));
            String output = bytesToHex(dig);
            if(PART2) {
                for(int i = 0; i < 2016; i ++){
                    dig = md.digest(output.getBytes("UTF-8"));
                    output = bytesToHex(dig);
                }
            }
            digest_map.put(salt + idx, output);
            return output;
        }
        catch (NoSuchAlgorithmException e){
            System.out.println(e);
        }
        catch (UnsupportedEncodingException e){
            System.out.println(e);
        }
        return "";
    }

    static int get_nth_key_index(String salt, int limit) {
        int k_count = 0, i = 0;
        while(k_count < limit) {
            if(is_key(salt, i)) {
                k_count += 1;
            }
            i ++;
        }
        return i - 1;
    }
     
    public static String bytesToHex(byte[] b_arr) {
        final StringBuilder builder = new StringBuilder();
        for(int i = 0; i < b_arr.length; i++) {
            builder.append(String.format("%02x", b_arr[i]));
        }
        return builder.toString();
    }

    public static void main(String[] args) {
        System.out.println(!is_key("abc", 18));
        System.out.println(is_key("abc", 39));
        System.out.println(is_key("abc", 92));
        System.out.println((get_nth_key_index("abc", 64)) == 22728);
        System.out.println("Part 1: " + get_nth_key_index("qzyelonm", 64));

        digest_map.clear();
        PART2 = true;

        System.out.println(!is_key("abc", 5));
        System.out.println(is_key("abc", 10));
        System.out.println("Part 2:" + get_nth_key_index("qzyelonm", 64));
    }

}
