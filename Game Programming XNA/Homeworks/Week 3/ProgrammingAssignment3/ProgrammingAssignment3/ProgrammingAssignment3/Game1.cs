namespace ProgrammingAssignment3
{
    using System;
    using Microsoft.Xna.Framework;
    using Microsoft.Xna.Framework.Graphics;
    using Microsoft.Xna.Framework.Input;

    /// <summary>
    /// This is the main type for your game
    /// </summary>
    public class Game1 : Game
    {
        GraphicsDeviceManager graphics;
        SpriteBatch spriteBatch;

        const int WINDOW_WIDTH = 800;
        const int WINDOW_HEIGHT = 600;

        readonly Random rand = new Random();
        readonly Vector2 centerLocation = new Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2);

        // STUDENTS: declare variables for 3 rock sprites
        private Texture2D sprite0;
        private Texture2D sprite1;
        private Texture2D sprite2;

        // STUDENTS: declare variables for 3 rocks
        private Rock rock0;
        private Rock rock1;
        private Rock rock2;

        // delay support
        const int TOTAL_DELAY_MILLISECONDS = 1000;
        int elapsedDelayMilliseconds = 0;

        // random velocity support
        const float BASE_SPEED = 0.15f;
        readonly Vector2 upLeft = new Vector2(-BASE_SPEED, -BASE_SPEED);
        readonly Vector2 upRight = new Vector2(BASE_SPEED, -BASE_SPEED);
        readonly Vector2 downRight = new Vector2(BASE_SPEED, BASE_SPEED);
        readonly Vector2 downLeft = new Vector2(-BASE_SPEED, BASE_SPEED);

        public Game1()
        {
            graphics = new GraphicsDeviceManager(this);
            Content.RootDirectory = "Content";

            // change resolution
            graphics.PreferredBackBufferWidth = WINDOW_WIDTH;
            graphics.PreferredBackBufferHeight = WINDOW_HEIGHT;
        }

        /// <summary>
        /// Allows the game to perform any initialization it needs to before starting to run.
        /// This is where it can query for any required services and load any non-graphic
        /// related content.  Calling base.Initialize will enumerate through any components
        /// and initialize them as well.
        /// </summary>
        protected override void Initialize()
        {
            base.Initialize();
        }

        /// <summary>
        /// LoadContent will be called once per game and is the place to load
        /// all of your content.
        /// </summary>
        protected override void LoadContent()
        {
            // Create a new SpriteBatch, which can be used to draw textures.
            spriteBatch = new SpriteBatch(GraphicsDevice);

            // Load content for 3 sprites
            sprite0 = Content.Load<Texture2D>("greenrock");
            sprite1 = Content.Load<Texture2D>("magentarock");
            sprite2 = Content.Load<Texture2D>("whiterock");

            // Create a new random rock
            rock0 = GetRandomRock();
        }

        /// <summary>
        /// UnloadContent will be called once per game and is the place to unload
        /// all content.
        /// </summary>
        protected override void UnloadContent()
        {
            Content.Dispose();
        }

        /// <summary>
        /// Allows the game to run logic such as updating the world,
        /// checking for collisions, gathering input, and playing audio.
        /// </summary>
        /// <param name="gameTime">Provides a snapshot of timing values.</param>
        protected override void Update(GameTime gameTime)
        {
            // Allows the game to exit
            if (GamePad.GetState(PlayerIndex.One).Buttons.Back == ButtonState.Pressed)
                this.Exit();

            // Update (position) of each available rock in drawing area
            if (rock0 != null)
            {
                rock0.Update(gameTime);
            }

            if (rock1 != null)
            {
                rock1.Update(gameTime);
            }

            if (rock2 != null)
            {
                rock2.Update(gameTime);
            }

            // update timer
            elapsedDelayMilliseconds += gameTime.ElapsedGameTime.Milliseconds;
            if (elapsedDelayMilliseconds >= TOTAL_DELAY_MILLISECONDS)
            {
                // Check & spawn a new rock if there are less than 3 rocks in drawing area
                if (rock0 == null)
                {
                    rock0 = GetRandomRock();
                }

                if (rock1 == null)
                {
                    rock1 = GetRandomRock();
                }

                if (rock2 == null)
                {
                    rock2 = GetRandomRock();
                }

                // restart timer
                elapsedDelayMilliseconds = 0;
            }

            // Spaw a new rock if any one of current has left the drawing area
            if (rock0 != null && rock0.OutsideWindow)
            {
                rock0 = GetRandomRock();
            }

            if (rock1 != null && rock1.OutsideWindow)
            {
                rock1 = GetRandomRock();
            }

            if (rock2 != null && rock2.OutsideWindow)
            {
                rock2 = GetRandomRock();
            }

            base.Update(gameTime);
        }

        /// <summary>
        /// This is called when the game should draw itself.
        /// </summary>
        /// <param name="gameTime">Provides a snapshot of timing values.</param>
        protected override void Draw(GameTime gameTime)
        {
            GraphicsDevice.Clear(Color.CornflowerBlue);

            // Draw rocks
            spriteBatch.Begin();
            if (rock0 != null)
            {
                rock0.Draw(spriteBatch);
            }

            if (rock1 != null)
            {
                rock1.Draw(spriteBatch);
            }

            if (rock2 != null)
            {
                rock2.Draw(spriteBatch);
            }

            spriteBatch.End();

            base.Draw(gameTime);
        }

        /// <summary>
        /// Gets a rock with a random sprite and velocity
        /// </summary>
        /// <returns>the rock</returns>
        private Rock GetRandomRock()
        {
            // Pick a random rock sprite
            Texture2D sprite = GetRandomSprite();

            // Pick a random velocity 
            Vector2 velocity = GetRandomVelocity();

            // return a new rock, centered in the window, with the random sprite and velocity
            return new Rock(sprite, centerLocation, velocity, WINDOW_WIDTH, WINDOW_HEIGHT);
        }

        /// <summary>
        /// Gets a random sprite
        /// </summary>
        /// <returns>the sprite</returns>
        private Texture2D GetRandomSprite()
        {
            switch (rand.Next(3))
            {
                case 0:
                    return sprite0;
                    break;
                case 1:
                    return sprite1;
                    break;
                default:
                    return sprite2;
            }
        }

        /// <summary>
        /// Gets a random velocity
        /// </summary>
        /// <returns>the velocity</returns>
        private Vector2 GetRandomVelocity()
        {
            // Return a random velocity
            switch (rand.Next(4))
            {
                case 0:
                    return upLeft;
                    break;
                case 1:
                    return upRight;
                    break;
                case 2:
                    return downRight;
                    break;
                default:
                    return downLeft;
            }
        }
    }
}
