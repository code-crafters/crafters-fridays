package retoCrafters001;
+
+import java.util.Scanner;
+
+
+public class Solution {
+
+	public static void main(String[] args) {
+		Scanner in = new Scanner (System.in);
+		
+		int t = in.nextInt();//numero de casos
+		int[] results = new int[t]; //guarda los resultados
+		
+		
+	    for(int i = 0; i < t; i++){
+	        int n = in.nextInt();
+	        
+	        //calcula el numero de digitos del numero
+	        int m,aux,digit,contd=0;
+	        aux=n;
+	   
+	        while(aux != 0){
+	            contd++; 
+	            aux/=10;
+	        }
+	        
+	        //calcula la potencia maxima
+	        m = (int)Math.pow(10,contd-1);
+	        
+	        //procesa el numero y cuenta cuantos digitos son divisores
+	        aux=n;
+	        int cont=0;
+	        while(aux!=0)
+	        {
+	           digit = aux/m;
+	           aux%=m;
+	           m/=10; 
+	           if(digit!=0 && n%digit==0)
+	               cont++;
+	        }
+	        //agrega el resultado a el arreglo
+	        results[i]=cont;
+	    }
+	    in.close();
+	    
+	    for(int r=0;r<t;r++)
+	        System.out.println(results[r]);
+	}
+
+}
