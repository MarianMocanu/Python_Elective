class QuickStart {
    public static void main(String[] args) {
        // System.out.println("Hello, World.");
        String[] x = { "qwerty", "mamaliga", "eu", "tu", "ulei" };
        

        for (int i = 0; i < x.length; i++) {
            System.out.println("x[" + i + "] = " + x[i]);
        }

        for (String name : x) {
            System.out.println("name = " + name);
        }

    }
}

// class MyClass{
//     // atribute
//     int age;
//     String name;
//     // metode

//     // constructor
//     MyClass(int x, String y) {
//         age = x;
//         name = y;
//     }

//     MyClass() {
//     }

//     String getDetails() {
//         return "Hello World! Here is " + name + ", he is " + age + " years old";
//     }
    
//     int getAge() {
//         return age;
//     }

//     void changeAge() {
//         age = 0;
//     }
// }