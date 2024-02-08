import java.util.*;
import java.io.*;
import java.util.LinkedList; //import
import java.util.Queue; //import

public class Main {

    static int N;
    static int K;
    static int[] lists = new int[100001];
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        String[] inputs = input.split(" ");
        N = Integer.parseInt(inputs[0]);
        K = Integer.parseInt(inputs[1]);
        int res = BFS();
        System.out.println(res);

    }
    private static int BFS(){
        int out;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(N);
        lists[N] = 1;
        while(!queue.isEmpty()){
            out = queue.poll();
            if(out == K) return lists[out]-1;

            for (int a : new int[]{out - 1, out + 1, out * 2}) {
                if ((a >= 0 && a <= 100000) && lists[a] == 0 ) {
                    lists[a] = lists[out] + 1;
                    queue.add(a);
                }
            }

        }
        return 0;
    }
}
