/*
 * This Java source file was generated by the Gradle 'init' task.
 */
package jiijijj;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class AppTest {

    @Test
    public void testVacioComptarElements() {
        int[] prueba = {};
        Gestor g = new Gestor(prueba);
        assertEquals(0, g.comptarElements());
    }

    @Test
    public void testVacioRetornarPrimer() {
        int[] prueba = {};
        Gestor g = new Gestor(prueba);
        assertEquals(0, g.retornarPrimer());
    }

    @Test
    public void testVacioRetornarDarrer() {
        int[] prueba = {};
        Gestor g = new Gestor(prueba);
        assertEquals(0, g.retornarDarrer());
    }

    @Test
    public void testVacioRetornarTercer() {
        int[] prueba = {};
        Gestor g = new Gestor(prueba);
        assertEquals(0, g.retornarTercer());
    }

    @Test
    public void testVacioSumaElements() {
        int[] prueba = {};
        Gestor g = new Gestor(prueba);
        assertEquals(0, g.sumaElements());
    }

    @Test
    public void testVacioMitjanaElements() {
        int[] prueba = {};
        Gestor g = new Gestor(prueba);
        assertEquals(0, g.mitjanaElements());
    }
    @Test
    public void testcomptarElements() {
        int[] prueba = {1, 2, 3, 56, 78};
        Gestor g = new Gestor(prueba);
        assertEquals(5, g.comptarElements());
    }

    @Test
    public void testretornarPrimer() {
        int[] prueba = {1, 2, 3, 56, 78};
        Gestor g = new Gestor(prueba);
        assertEquals(1, g.retornarPrimer());
    }

    @Test
    public void testretornarDarrer() {
        int[] prueba = {1, 2, 3, 56, 78};
        Gestor g = new Gestor(prueba);
        assertEquals(78, g.retornarDarrer());
    }

    @Test
    public void testretornarTercer() {
        int[] prueba = {1, 2, 3, 56, 78};
        Gestor g = new Gestor(prueba);
        assertEquals(3, g.retornarTercer());
    }

    @Test
    public void testsumaElements() {
        int[] prueba = {1, 2, 3, 56, 78};
        Gestor g = new Gestor(prueba);
        assertEquals(140, g.sumaElements());
    }

    @Test
    public void testmitjanaElements() {
        int[] prueba = {1, 2, 3, 56, 78};
        Gestor g = new Gestor(prueba);
        assertEquals(28, g.mitjanaElements());
    }

    @Test
    public void testRetornarTercerMenor() {
        int[] prueba = {1, 2};
        Gestor g = new Gestor(prueba);
        assertEquals(0, g.retornarTercer());
        
    }

    @Test
    public void testsumaElementsNegativos() {
        int[] prueba = {1, -2, 1, -3, 6};
        Gestor g = new Gestor(prueba);
        assertEquals(3, g.sumaElements());
    }

    @Test
    public void testmitjanaElementsNegativos() {
        int[] prueba = {1, 1, -3, -3, 2};
        Gestor g = new Gestor(prueba);
        assertEquals(-0.4, g.mitjanaElements());
    }

    


}