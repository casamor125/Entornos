package gradeltest;

public class Gestor {
    
    //int[] prueba = {1,2,3,56,78}; 
    int[] x;
    public Gestor(int[] x){
    this.x = x;
    }
    
    
    public int comptarElements(){
    
        int contador;
        for (contador = 0; contador < this.x.length; contador++) {
            
        }
    return contador;
    
    }
    public int retornarPrimer(){       
    return this.x[0];
    }
    
    public int retornarDarrer(){   
    return this.x[x.length-1];
    }
    
    public int retornarTercer(){   
    return this.x[2];
    }
    
    public int sumaElements(){
        int suma = 0;
        for (int i = 0; i < x.length; i++) {
            suma += x[i];
        }
        return suma;
    }
    
    public double mitjanaElements(){
        double mitjana = 0;
        int contador = 0;
        for (int i = 0; i < x.length-1; i++) {
            mitjana += x[i];
            contador++;
        }
        return mitjana/contador;
    }
    
}
