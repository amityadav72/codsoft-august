// Source code is decompiled from a .class file using FernFlower decompiler.
import java.util.Scanner;

public class gradecalculator {
   public gradecalculator() {
   }

   public static void main(String[] var0) {
      float[] var1 = new float[8];
      float var2 = 0.0F;
      Scanner var5 = new Scanner(System.in);
      System.out.print("Enter Marks Obtained in 8 Subjects: ");

      int var4;
      for(var4 = 0; var4 < 8; ++var4) {
         var1[var4] = var5.nextFloat();
      }

      for(var4 = 0; var4 < 8; ++var4) {
         var2 += var1[var4];
      }

      float var3 = var2 / 8.0F;
      System.out.print("\nGrade = ");
      if (var3 >= 94.0F) {
         System.out.println("A");
      } else if (var3 >= 90.0F && var3 < 94.0F) {
         System.out.println("A-");
      } else if (var3 >= 87.0F && var3 < 90.0F) {
         System.out.println("B+");
      } else if (var3 >= 83.0F && var3 < 87.0F) {
         System.out.println("B");
      } else if (var3 >= 80.0F && var3 < 83.0F) {
         System.out.println("B-");
      } else if (var3 >= 77.0F && var3 < 80.0F) {
         System.out.println("C+");
      } else if (var3 >= 73.0F && var3 < 77.0F) {
         System.out.println("C");
      } else if (var3 >= 70.0F && var3 < 73.0F) {
         System.out.println("C-");
      } else if (var3 >= 67.0F && var3 < 70.0F) {
         System.out.println("D+");
      } else if (var3 >= 63.0F && var3 < 67.0F) {
         System.out.println("D");
      } else if (var3 >= 60.0F && var3 < 63.0F) {
         System.out.println("D-");
      } else {
         System.out.println("F");
      }

   }
}
