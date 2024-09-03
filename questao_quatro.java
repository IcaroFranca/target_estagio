import java.util.Locale;

public class questao_quatro {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		
		double sp = 67836.43, rj = 36678.66, mg = 29229.88, es = 27165.48, outros = 19849.53;
		double total = sp + rj + mg + es + outros;
		
		
		System.out.printf("SP: %.2f (%.2f%%)%n", sp, (sp / total) * 100);
		System.out.printf("RJ: %.2f (%.2f%%)%n", rj, (rj / total) * 100);
		System.out.printf("MG: %.2f (%.2f%%)%n", mg, (mg / total) * 100);
		System.out.printf("ES: %.2f (%.2f%%)%n", es, (es / total) * 100);
		System.out.printf("Outros: %.2f (%.2f%%)%n", outros, (outros / total) * 100);
		System.out.printf("Total: %.2f (%.2f%%)%n", total, (total / total) * 100);
		
	}

}
