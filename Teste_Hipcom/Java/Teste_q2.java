import java.util.Scanner;

public class Teste_q2 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String opc = "";
		
		
		do {
			
			System.out.println("Digite a quantidade desejada: ");
			int tam = sc.nextInt();
			quant(tam);
			
			System.out.println();
			System.out.println("Gostaria de continuar? S/N");
			
			opc = sc.next();
			
		}while (opc.equals("S") || opc.equals("s"));
	
		
	sc.close();
	
	
	}
	
	
	
	
	public static void quant(Integer num) {
		
		for (int i = 0; i < num; i++) {
			System.out.print("#");
		}
		System.out.println();
		
	}
}
