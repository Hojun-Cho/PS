import java.util.stream.IntStream;

class Solution {
    private static final int ENTRY_COUNT = 8;
    private int answer = 0;
    private String[] entryList = {"A", "C", "F", "J", "M", "N", "R", "T"};
    private boolean visited[] = new boolean[ENTRY_COUNT];

    public int solution(int n, String[] data) {
        dfs("", data);
        return answer;
    }

    private void dfs(String name, String[] data) {
        if (name.length() == ENTRY_COUNT) {
            if (isRight(name, data)) {
                answer += 1;
            }
            return;
        }
        IntStream.range(0, ENTRY_COUNT)
                .filter(i -> !visited[i])
                .forEach(i -> {
                    visited[i] = true;
                    dfs(name + entryList[i], data);
                    visited[i] = false;
                });
    }

    private boolean isRight(String name, String[] datas) {
        for (String data : datas) {
            int p1 = name.indexOf(data.charAt(0));
            int p2 = name.indexOf(data.charAt(2));
            char operation = data.charAt(3);
            int range = Integer.parseInt(String.valueOf(data.charAt(4)));

            if (!isValid(p1, p2, operation, range)) {
                return false;
            }
        }
        return true;
    }

    private boolean isValid(int p1, int p2, char operation, int range) {
        if (operation == '<') {
            if (!(Math.abs(p1 - p2) - 1 < range))
                return false;
        }
        if (operation == '>') {
            if (!(Math.abs(p1 - p2) - 1 > range))
                return false;
        }
        if (operation == '=') {
            if (!(Math.abs(p1 - p2) - 1 == range))
                return false;
        }
        return true;
    }
}
