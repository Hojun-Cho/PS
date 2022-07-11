# 처음엔 findFirst로 시도 => 하지만 사전 순으로 시작한 경로가 없는 경우가 존재함 따라서 재귀를 이용

import java.util.stream.IntStream;

class Solution {
    public static final int START = 0;
    public static final int END = 1;
    public static final String ICN = "ICN";

    List<String> answer = new ArrayList<>();
    boolean[] visited;
    int length = 0;
    String[][] tickets ;

    public String[] solution(String[][] tickets) {
        this.length = tickets.length;
        this.visited = new boolean[length];
        this.tickets = tickets;

        dfs(ICN,ICN,0);
        Collections.sort(answer);

        return answer.get(0).split(" ");
    }

    public void dfs(String now, String path, int totalPath) {
        if (totalPath == length) {
            answer.add(path);
            return;
        }
        IntStream.range(0, length)
                .filter(i -> !visited[i] && now.equals(tickets[i][START]))
                .forEach(i -> {
                    visited[i] = true;
                    dfs(tickets[i][END], path + " " + tickets[i][END], totalPath + 1);
                    visited[i] = false;
                });
    }
}
