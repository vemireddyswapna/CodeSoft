import java.util.Scanner;

public class CurrencyConverter {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        double usdToInr = 83.0;
        double usdToEur = 0.92;
        double usdToGbp = 0.78;

        System.out.println("===== Currency Converter =====");
        System.out.println("Available currencies:");
        System.out.println("1. USD");
        System.out.println("2. INR");
        System.out.println("3. EUR");
        System.out.println("4. GBP");

        System.out.print("Enter base currency (USD/INR/EUR/GBP): ");
        String base = sc.next().toUpperCase();

        System.out.print("Enter target currency (USD/INR/EUR/GBP): ");
        String target = sc.next().toUpperCase();

        System.out.print("Enter amount: ");
        double amount = sc.nextDouble();

        double amountInUsd = 0;
        double convertedAmount = 0;

        // Convert base currency to USD first
        switch (base) {

            case "USD":
                amountInUsd = amount;
                break;

            case "INR":
                amountInUsd = amount / usdToInr;
                break;

            case "EUR":
                amountInUsd = amount / usdToEur;
                break;

            case "GBP":
                amountInUsd = amount / usdToGbp;
                break;

            default:
                System.out.println("Invalid base currency.");
                return;
        }

        // Convert USD to target currency
        switch (target) {

            case "USD":
                convertedAmount = amountInUsd;
                break;

            case "INR":
                convertedAmount = amountInUsd * usdToInr;
                break;

            case "EUR":
                convertedAmount = amountInUsd * usdToEur;
                break;

            case "GBP":
                convertedAmount = amountInUsd * usdToGbp;
                break;

            default:
                System.out.println("Invalid target currency.");
                return;
        }

        System.out.println("\nConverted Amount: " + convertedAmount + " " + target);

        sc.close();
    }
}
