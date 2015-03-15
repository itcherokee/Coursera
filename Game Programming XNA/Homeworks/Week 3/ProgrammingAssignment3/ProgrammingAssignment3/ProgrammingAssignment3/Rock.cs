namespace ProgrammingAssignment3
{
    using Microsoft.Xna.Framework;
    using Microsoft.Xna.Framework.Graphics;

    /// <summary>
    /// A rock
    /// </summary>
    public class Rock
    {
        #region Fields

        // drawing support
        readonly Texture2D sprite;
        Rectangle drawRectangle;

        // moving support
        Vector2 velocity;

        // window containment support
        readonly int windowWidth;
        readonly int windowHeight;
        bool outsideWindow = false;

        #endregion

        #region Constructors

        /// <summary>
        /// Constructor
        /// </summary>
        /// <param name="sprite">sprite for the rock</param>
        /// <param name="location">location of the center of the rock</param>
        /// <param name="velocity">velocity of the rock</param>
        /// <param name="windowWidth">window width</param>
        /// <param name="windowHeight">window height</param>
        public Rock(Texture2D sprite, Vector2 location, Vector2 velocity,
            int windowWidth, int windowHeight)
        {
            // save window dimensions
            this.windowWidth = windowWidth;
            this.windowHeight = windowHeight;

            // save sprite and set draw rectangle
            this.sprite = sprite;
            drawRectangle = new Rectangle((int)location.X - sprite.Width / 2,
                (int)location.Y - sprite.Height / 2, sprite.Width, sprite.Height);

            // save velocity
            this.velocity = velocity;
        }

        #endregion

        #region Properties

        /// <summary>
        /// Sets the rock's velocity
        /// </summary>
        public Vector2 Velocity
        {
            set
            {
                velocity.X = value.X;
                velocity.Y = value.Y;
            }
        }

        /// <summary>
        /// Gets whether or not the rock is outside the window
        /// </summary>
        public bool OutsideWindow
        {
            get { return outsideWindow; }
        }

        #endregion

        #region Methods

        /// <summary>
        /// Updates the rock
        /// </summary>
        /// <param name="gameTime">game time</param>
        public void Update(GameTime gameTime)
        {
            if (!this.OutsideWindow)
            {
                // Updates the rock's location
                var distanceX = (int)(this.velocity.X * gameTime.ElapsedGameTime.Milliseconds);
                var distanceY = (int)(this.velocity.Y * gameTime.ElapsedGameTime.Milliseconds);
                this.drawRectangle.X += distanceX;
                this.drawRectangle.Y += distanceY;

                // Checks does rock is outside drawing area
                if (this.drawRectangle.Left > windowWidth || this.drawRectangle.Right < 0)
                {
                    this.outsideWindow = true;
                }

                if (this.drawRectangle.Top > windowHeight || this.drawRectangle.Bottom < 0)
                {
                    this.outsideWindow = true;
                }
            }
        }

        /// <summary>
        /// Draws the rock
        /// </summary>
        /// <param name="spriteBatch">sprite batch</param>
        public void Draw(SpriteBatch spriteBatch)
        {
            if (!this.OutsideWindow)
            {
                spriteBatch.Draw(sprite, drawRectangle, Color.White);
            }
        }

        #endregion
    }
}
