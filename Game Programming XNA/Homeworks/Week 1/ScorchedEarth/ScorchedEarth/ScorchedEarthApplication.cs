namespace ScorchedEarth
{
    using System;

    /// <summary>
    /// Scorched Earth Game
    /// </summary>
    public class ScorchedEarthApplication
    {
        /// <summary>
        /// Main game engine, that calculates required parameters of shell.
        /// </summary>
        public static void Main()
        {
            const float GravityAcceleration = 9.8f;

            Console.WriteLine("Welcome");
            Console.WriteLine("This application will calculate the maximum height of the shell");
            Console.WriteLine("and the distance it will travel along the ground.");
            Console.WriteLine();

            // read and calculate initial angle of the shell
            Console.Write("Enter initial angle of shell (degrees): ");
            double initialAngle = double.Parse(Console.ReadLine()) * (Math.PI / 180);

            // read initial speed
            Console.Write("Enter initial speed of shell: ");
            float initialSpeed = float.Parse(Console.ReadLine());

            // calculates velocity at start
            double velocityAtStartX = initialSpeed * Math.Cos(initialAngle);
            double velocityAtStartY = initialSpeed * Math.Sin(initialAngle);

            // calculates time until shell reaches apex
            double timeToApex = velocityAtStartY / GravityAcceleration;

            // calculates heigth of shell at apex
            double heightAtApex = velocityAtStartY * velocityAtStartY / (2 * GravityAcceleration);

            // calculates distance shell travels horizontally 
            double travelDistanceHorizontaly = velocityAtStartX * 2 * timeToApex;

            // Output results of the calculations
            Console.WriteLine();
            Console.WriteLine("Shell trajectory max height is: {0:F3}", heightAtApex);
            Console.WriteLine("Shell trajectory max distance is: {0:F3}", travelDistanceHorizontaly);
            Console.WriteLine();
        }
    }
}
