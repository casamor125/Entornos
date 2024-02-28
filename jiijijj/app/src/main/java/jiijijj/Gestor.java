package jiijijj;


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
        if(this.x.length==0){
            return 0;
        }else   
    return this.x[0];
    }
    
    public int retornarDarrer(){ 
        if(this.x.length==0){
            return 0;
        }else   
    return this.x[x.length-1];
    }
    
    public int retornarTercer(){  
        if(this.x.length==0){
            return 0;
        }else if (this.x.length<=2){
            return 0;
        }else
    return this.x[2];
    }
    
    public int sumaElements(){
        int suma = 0;
        if(this.x.length==0){
            return 0;
        }else{
        for (int i = 0; i < x.length; i++) {
            suma += x[i];
        }
        return suma;
    }
    }
    
    public double mitjanaElements(){
        double mitjana = 0;
        int contador = 0;
        
        if(this.x.length==0){
            return 0;
        }else{
        for (int i = 0; i < x.length; i++) {
            mitjana += x[i];
            contador++;
        }
        return mitjana/contador;
    }
    }
    
}
