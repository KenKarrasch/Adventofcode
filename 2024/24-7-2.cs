using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Diagnostics;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Enter data in format: target: num1 num2 num3\n...");
        List<string> lines = new List<string>();

        string input;
        while (!string.IsNullOrWhiteSpace(input = Console.ReadLine()))
        {
            lines.Add(input);
        }

        Stopwatch stopwatch = Stopwatch.StartNew(); // Start the timer

        BigInteger total = 0;

        foreach (var line in lines)
        {
            var parts = line.Split(':');
            BigInteger target = BigInteger.Parse(parts[0]);
            List<BigInteger> numbers = parts[1].Split(' ', StringSplitOptions.RemoveEmptyEntries).Select(BigInteger.Parse).ToList();

            var result = CanReachTargetIterative(numbers, target);

            if (result.Found)
            {
                Console.WriteLine($"Target {target} can be reached using: {result.Expression}");
                total += target;
            }
            else
            {
                Console.WriteLine($"Target {target} cannot be reached with the given numbers.");
            }
        }

        stopwatch.Stop(); // Stop the timer
        Console.WriteLine($"Part 2 - Total: {total}");
        Console.WriteLine($"Execution Time: {stopwatch.Elapsed}");
    }

    static (bool Found, string Expression) CanReachTargetIterative(List<BigInteger> numbers, BigInteger target)
    {
        var stack = new Stack<(int Index, BigInteger CurrentValue, string Expression)>();
        stack.Push((0, 0, ""));

        while (stack.Count > 0)
        {
            var (index, currentValue, expression) = stack.Pop();

            if (index == numbers.Count)
            {
                if (currentValue == target)
                {
                    return (true, expression);
                }
                continue;
            }

            BigInteger nextNumber = numbers[index];

            // Add the next number
            stack.Push((index + 1, currentValue + nextNumber, expression == "" ? nextNumber.ToString() : $"{expression} + {nextNumber}"));

            // Multiply the next number
            stack.Push((index + 1, currentValue != 0 ? currentValue * nextNumber : nextNumber, expression == "" ? nextNumber.ToString() : $"{expression} * {nextNumber}"));

            // Concatenate the next number with the current value
            if (!string.IsNullOrEmpty(expression))
            {
                BigInteger concatenatedValue = BigInteger.Parse(currentValue.ToString() + nextNumber.ToString());
                stack.Push((index + 1, concatenatedValue, $"({expression} || {nextNumber})"));
            }
        }

        return (false, null);
    }
}
