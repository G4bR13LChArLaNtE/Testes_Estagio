import java.util.Scanner;

public class Teste_q3 {
	
	public static void main(String[] args) {
		
		String aux = "";
		Scanner sc = new Scanner(System.in);
		
		do {
			
			
		String pal1 = "", pal2 = "";
		
		
		System.out.println("Digite a primeira palavra: ");
		pal1 = sc.next();
		
		
		System.out.println("Digite a segunda palavra: ");
		pal2 = sc.next();		
		
		
		
		if(isAnagrama(pal1, pal2)) {
			System.out.println("As duas palavras são Anagramas!");
		}
		else {
			System.out.println("As duas palavras não são Anagramas!");
		}
		
		
		System.out.println();
		System.out.println("Gostaria de continuar? S/N");
		aux = sc.next();
		
		
		
		
		}while(aux.equals("s")  || aux.equals("S") );
		
		
		sc.close();
	}
	
	
	
	
	



public static boolean isAnagrama(String a, String b) {
	
	int r = 0; 
	
	for(int i = 0; i < a.length(); i++)
		r = r ^ a.charAt(i); // ^ - Operador Xor 
		
	
	for(int i = 0; i < b.length(); i++)
		r = r ^ b.charAt(i); // ^ - Operador Xor 	
		
	
		return (r == 0);
	}
}