package com.example.demo;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Block {
    final int x;
    final int y;
    int count;

    public Block(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public Block(int x, int y, int count) {
        this.x = x;
        this.y = y;
        this.count = count;
    }

    @Override
    public boolean equals(Object obj) {
        Block target = (Block) obj;
        return target.x == x && target.y == y;
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }
}


class Solution {
    private Deque<Block> deque = new ArrayDeque<>();
    private final Move move;
    private int answer = Integer.MAX_VALUE;
    private final Map<Block, Boolean> visited = new HashMap<>();

    public Solution(int N) {
        this.move = new Move(N);
    }
    public void invoke(Block now, Block end) {
        deque.add(now);
        visited.put(now, Boolean.TRUE);
        while (!deque.isEmpty()) {
            now = deque.pollFirst();
            if (now.equals(end)) {
                answer = Math.min(answer, now.count);
                return;
            }
            
            move.invoke(now).stream()
                    .filter(block -> !visited.containsKey(block))
                    .forEach(block -> {
                        visited.put(block, Boolean.TRUE);
                        deque.add(block);
                    });
        }

    }
    public int getAnswer() {
        if (answer == Integer.MAX_VALUE)
            return -1;
        return answer;
    }
}


class Move {
    private final int N;
    private int[][] canMove = {{-2, -1}, {-2, 1}, {0, -2}, {0, 2}, {2, -1}, {2, 1}};

    public Move(int n) {
        N = n;
    }

    public List<Block> invoke(Block block) {
        List<Block> blocks = new ArrayList<>();
        for (int[] move : canMove) {
            int newX = block.x + move[0];
            int newY = block.y + move[1];
            if (isValidMove(newX, newY)) {
                blocks.add(new Block(newX, newY, block.count + 1));
            }
        }
        return blocks;
    }

    private boolean isValidMove(int x, int y) {
        return x <= N && x >= 0 && y <= N && y >= 0;
    }
}

public class Main {
    private static void run() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        String[] s = br.readLine().split(" ");
        Block start = new Block(Integer.parseInt(s[0]), Integer.parseInt(s[1]));
        Block end = new Block(Integer.parseInt(s[2]), Integer.parseInt(s[3]));
        Solution solution = new Solution(n);
        solution.invoke(start, end);
        System.out.println(solution.getAnswer());
    }

    public static void main(String[] args) throws IOException {
        run();

    }
}
