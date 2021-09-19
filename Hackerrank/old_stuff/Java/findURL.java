public class findURL {
    public static boolean youtube(String s) {
        String regex = "(?i)youtube\\.com";
        //String pattern = "YouTube";
        return regex.matches(s);
    }
    public static void main(String[] args){
        String s = "https://www.YouTube.com/watch?v=XwIs1nlDQ2I&featur";
        //String s = "www.YouTube.com";
        String regex = "(?i)\"(.+)youtube\\.com(.+)\"";
        String regex_for_test = "(?i)(.+)youtube\\.com(.+)";

        System.out.println(s.matches(regex_for_test));
    }
}
//https://stackoverflow.com/questions/1379191/why-does-this-java-regex-cause-illegal-escape-character-errors