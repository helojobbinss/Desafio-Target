package Exercicio2;
import java.util.Scanner;

public class Fibonacci{
    static long fibonacci(int posicao){
        if(posicao < 2){
            return posicao;
        }
        else{
        return fibonacci( posicao- 1) + fibonacci( posicao- 2);
        }
}
    public static void main(String[] args) {
        Scanner leitor = new Scanner (System.in);
        int num;
        int i;
        System.out.println("Insira um número: ");
        num = leitor.nextInt();
        for(i = 0; i<=30;i++){
            fibonacci(i);
            System.out.println(fibonacci(i));
            if(num == fibonacci(i)){
                System.out.println("O número "+num+" está na posição "+i+1+" da sequência de Fibonacci");
                break;
            }
            if(num< fibonacci(i)){
                System.out.println("O número "+num+" não está na sequencia de Fibonacci");
                break;
            }
        }

        }
}

