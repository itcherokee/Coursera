namespace ProgrammingAssignment2
{
    using System;
    using Microsoft.Xna.Framework;
    using Microsoft.Xna.Framework.Graphics;
    using Microsoft.Xna.Framework.Input;

    /// <summary>
    /// This is the main type for your game
    /// </summary>
    public class Game1 : Microsoft.Xna.Framework.Game
    {
        const int WINDOW_WIDTH = 800;
        const int WINDOW_HEIGHT = 600;

        GraphicsDeviceManager graphics;
        SpriteBatch spriteBatch;

        // used to store sprites
        private Texture2D sprite0;
        private Texture2D sprite1;
        private Texture2D sprite2;

        // used to handle X and Y velocity speeds
        private int speedX = 0;
        private int speedY = 0;

        // used to handle generating random values
        Random rand = new Random();
        const int CHANGE_DELAY_TIME = 1000;
        int elapsedTime = 0;

        // used to keep track of current sprite and location
        Texture2D currentSprite;
        Rectangle drawRectangle = new Rectangle();

        public Game1()
        {
            graphics = new GraphicsDeviceManager(this);
            Content.RootDirectory = "Content\\Content";

            graphics.PreferredBackBufferWidth = WINDOW_WIDTH;
            graphics.PreferredBackBufferHeight = WINDOW_HEIGHT; ;
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

            sprite0 = Content.Load<Texture2D>("girl0");
            sprite1 = Content.Load<Texture2D>("girl1");
            sprite2 = Content.Load<Texture2D>("girl2");

            currentSprite = sprite0;
        }

        /// <summary>
        /// UnloadContent will be called once per game and is the place to unload
        /// all content.
        /// </summary>
        protected override void UnloadContent()
        {
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

            elapsedTime += gameTime.ElapsedGameTime.Milliseconds;
            if (elapsedTime > CHANGE_DELAY_TIME)
            {
                elapsedTime = 0;

                // Select current sprite by random generation
                int spriteNumber = rand.Next(3);

                // change current sprite
                if (spriteNumber == 0)
                {
                    currentSprite = sprite0;
                }
                else if (spriteNumber == 1)
                {
                    currentSprite = sprite1;
                }
                else if (spriteNumber == 2)
                {
                    currentSprite = sprite2;
                }

                // Set equality between drawRectangel width/height and sprite ones
                drawRectangle.Width = currentSprite.Width;
                drawRectangle.Height = currentSprite.Height;

                // Center sprite in the screen
                drawRectangle.X = (WINDOW_WIDTH - drawRectangle.Width) / 2;
                drawRectangle.Y = (WINDOW_HEIGHT - drawRectangle.Height) / 2;

                // Generate random velocity speeds
                speedX = rand.Next(-4, 5);
                speedY = rand.Next(-4, 5);
            }

            // move sprite(held by drawRectangle) by random speed (by X and by Y)
            drawRectangle.X += speedX;
            drawRectangle.Y += speedY;

            base.Update(gameTime);
        }

        /// <summary>
        /// This is called when the game should draw itself.
        /// </summary>
        /// <param name="gameTime">Provides a snapshot of timing values.</param>
        protected override void Draw(GameTime gameTime)
        {
            GraphicsDevice.Clear(Color.CornflowerBlue);

            // Draw current sprite
            spriteBatch.Begin();
            spriteBatch.Draw(currentSprite, drawRectangle, Color.White);
            spriteBatch.End();

            base.Draw(gameTime);
        }
    }
}