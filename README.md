![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)
# Vocab Venture

The Vocab Venture Game is an engaging and educational project designed to enhance vocabulary and word-guessing skills in a fun and interactive way. Aimed at language enthusiasts, students, and anyone looking to enrich their word knowledge, this game provides an enjoyable platform for learning new words and their meanings. The project's primary goal is to make vocabulary-building an exciting experience, encouraging users to expand their language proficiency while having a great time.

**Target Audience:**
The game is intended for a diverse audience, including language learners, students preparing for exams, and individuals seeking an entertaining way to boost their word comprehension. Whether you're a student looking to improve your vocabulary for academic success or a language enthusiast wanting to explore new words, the Vocab Venture Game offers a dynamic and accessible learning environment suitable for various skill levels.

## Features 

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Codeanywhere and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **August 30th, 2023**
In this section, you should go over the different parts of your project, and describe each in a sentence or so. You will need to explain what value each of the features provides for the user, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

### Existing Features

#### Welcome Message 

- Provides a friendly welcome message to the user, setting a positive tone for the game and creating an inviting atmosphere for a delightful gaming experience.

#### Inital Level Setting

- Sets the initial game level to 1, ensuring a logical start for the user and allowing a seamless progression through increasing levels of difficulty.

#### Game Loop

- Runs a loop for each level, allowing the user to guess words and progress through levels, ensuring a dynamic and engaging gameplay experience.

#### Random Word Selection

- Randomly selects a word from the list for each level, adding variety and unpredictability, keeping the game exciting and different in each playthrough.

#### Hints Display

- Displays hints progressively, making it easier for the user to guess the word, providing valuable assistance and guidance throughout the challenging levels.

#### Attempts Limit

- Limits the number of attempts for each level, adding a challenge to the game and encouraging strategic thinking and careful consideration of each guess.

#### Level Completion 

- Informs the user when they complete a level and congratulates them upon completing all levels, offering a sense of accomplishment and recognition for their progress.

#### Resetting 

- If the user fails to guess the word within the attempts limit, resets the game to Level 1, allowing users to restart and continue enjoying the game without unnecessary frustration.

### Future Features

- **Multiplayer Mode**

A mode that allows users to compete or collaborate with friends or other players. In this mode, users could take turns guessing words or compete in real-time to see who can progress through the levels more quickly. Additionally, a collaborative mode could involve players working together to solve word challenges. This feature adds a social and competitive element to the game, making it more engaging for users who enjoy interactive and shared gaming experiences. It could also include leaderboards to track and display the progress and achievements of individual players or groups, fostering friendly competition and a sense of community.

- **Leaderboard**

The Leaderboard feature enhances the Vocab Venture Game by introducing a dynamic and competitive element, allowing users to track and compare their progress with others. Users can access a real-time leaderboard that showcases the top performers, highlighting their achievements and levels completed. Each player's position on the leaderboard is determined by factors such as the number of levels completed, accuracy in guessing words, and the speed at which they progress.

- **Difficulty Preferences**

Users can choose their preferred difficulty level before starting the game. This caters to players with varying levels of vocabulary proficiency, ensuring an engaging experience for both beginners and advanced users. Difficulty settings can include options for adjusting word complexity, the number of attempts per level, or the intricacy of hints provided.



`http_server`
## Testing 

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.
In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your project’s features and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

A button should appear to click: _Open Preview_ or _Open Browser_.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

In Codeanywhere you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.
You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

To log into the Heroku toolbelt CLI:
If this section grows too long, you may want to split it off into a separate file and link to it from here.

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In Codeanywhere, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.
### Validator Testing 

---
- HTML
    - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcode-institute-org.github.io%2Flove-maths%2F)
- CSS
    - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2Fnu%2F%3Fdoc%3Dhttps%253A%252F%252Fcode-institute-org.github.io%252Flove-maths%252F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
- JavaScript
    - No errors were found when passing through the official [Jshint validator](https://jshint.com/)
      - The following metrics were returned: 
      - There are 11 functions in this file.
      - Function with the largest signature takes 2 arguments, while the median is 0.
      - Largest function has 10 statements in it, while the median is 3.
      - The most complex function has a cyclomatic complexity value of 4 while the median is 2.

Happy coding!
### Unfixed Bugs

You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. 

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://code-institute-org.github.io/love-maths/


## Credits 

In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 

You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign up page are from This Open Source site
- The images used for the gallery page were taken from this other open source site


Congratulations on completing your Readme, you have made another big stride in the direction of being a developer! 

## Other General Project Advice

Below you will find a couple of extra tips that may be helpful when completing your project. Remember that each of these projects will become part of your final portfolio so it’s important to allow enough time to showcase your best work! 

- One of the most basic elements of keeping a healthy commit history is with the commit message. When getting started with your project, read through [this article](https://chris.beams.io/posts/git-commit/) by Chris Beams on How to Write  a Git Commit Message 
  - Make sure to keep the messages in the imperative mood 

- When naming the files in your project directory, make sure to consider meaningful naming of files, point to specific names and sections of content.
  - For example, instead of naming an image used ‘image1.png’ consider naming it ‘landing_page_img.png’. This will ensure that there are clear file paths kept.
