import java.util.Arrays;
import java.util.Collections;
import java.util.List;


public class Teste_q1 {
	

	
	public static void main(String[] args) {
		
		List<Integer> pilhaMeias = Arrays.asList(10, 20, 10, 20, 10, 30, 20, 50, 10);
		 System.out.println("Número de pares formados: "+ numeroParesMeias(pilhaMeias));
	}
	
	private static Integer numeroParesMeias(List<Integer> pilhasMeias) {
		int cont = 0;
		
		Collections.sort(pilhasMeias);
		
		
		for (int j = 0; j < pilhasMeias.size(); j++) {
			if (Collections.frequency(pilhasMeias, pilhasMeias.get(j)) > 1) {
				cont += 1;
			}
			
		}
				
		if (cont % 2 == 0) {
			cont /= 2;
		}else {
			cont = ((cont - 1)/ 2);
		}
	
		return cont;
	
  }
	
}
