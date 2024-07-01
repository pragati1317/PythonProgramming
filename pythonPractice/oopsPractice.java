/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
import java.util.ArrayList; 

 class Student {
   
        
        String name;
        int mathsMark;
        
        public Student(String name){
            this.name=name;
            this.mathsMark=0;
        }
        
        public Student(String name, int mathsMark){
            this.name=name;
            this.mathsMark=mathsMark;
        }
        
        public double average(ArrayList<Integer> nums){
            int ln=nums.size(); 
             
             double sum=0;
            for(int i=0; i<ln; i++){
                sum+=nums.get(i);
            }
            return sum/ln;
        }
    } 
public class Main
{
    // static String collegeName="Sgsits Indore";
  
   
	public static void main(String[] args) {
		System.out.println("Hello World");
		ArrayList<Integer> marks= new ArrayList<>(6); 
		marks.add(47);
		marks.add(85); 
		marks.add(90); 
		marks.add(72); 
		marks.add(89); 
		
		Student s1 = new Student("Pragati", 95);
		marks.add(s1.mathsMark); 
		System.out.println(s1.average(marks)); 
	}
}
