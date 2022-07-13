
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_15235 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] answer = new int[N];
        Deque<List<Integer>>  deque = new ArrayDeque<>();

        StringTokenizer stringTokenizer = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < N; i++) {
            deque.add(List.of(i, Integer.parseInt(stringTokenizer.nextToken())));
        }

        int turn = 1;
        while (!deque.isEmpty()) {
            List<Integer> now = deque.pollFirst();
            int index = now.get(0);
            int wantEatCount = now.get(1);

            logic(turn, index, wantEatCount,deque,answer);
            turn += 1;
        }
        for (int x : answer){
            System.out.printf("%d ",x);
        }
    }

    private static void logic(int turn, int index, int wantEatCount, Deque<List<Integer>> deque, int[] answer) {
        if (wantEatCount == 1) {
            answer[index] = turn;
        }else {
            deque.add(List.of(index, wantEatCount - 1));
        }
    }
}
