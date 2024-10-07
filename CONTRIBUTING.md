# Contribution Guide
[Persian version | نسخه فارسی](https://docs.google.com/document/d/1MqN3kFYmRMHa3mB40iO6MYB1kc_zbUaMOvsouq6bRU0/edit?usp=sharing)

Welcome to MedX's contribution guide! All contributions, big or small, are valuable, even in this guide! so feel free to share your ideas!

## Why Contribute?
The reasons people contribute to open-source projects like MedX are as diverse as the contributors themselves. Here are just a few motivations you might resonate with:

1. ***Learning and Growth:***  
    Contributing to open-source projects is an excellent way to learn new skills and expand your knowledge. Whether you're coding, designing, writing, or managing, you'll gain hands-on experience that can accelerate your personal and professional growth.
2. ***Building a Portfolio:***  
    Every contribution you make adds to your portfolio. This is especially valuable if you're looking to showcase your skills to potential employers or collaborators. Open-source contributions are proof of your abilities.
3. ***Community and Networking:***  
    By contributing to MedX, you become part of a global community of like-minded individuals. This is an opportunity to network, collaborate, and learn from others who share your passion for health-tech and open-source development.
4. ***Making an Impact:***  
    Your contributions to MedX directly impact the world of health-tech. By helping to create and refine tools, resources, and content, you're playing a part in shaping the future of healthcare.
5. ***Giving Back:***  
    For many, contributing to open-source is a way to give back to a community that has provided them with so much. If you've benefited from open-source projects in the past, contributing to MedX is a way to return the favor.
6. ***Bridging Health and Technology:***  
    With the rapid development of new technologies, you can play a role in connecting health and technology. By contributing to MedX, you can help expand this growing community and enhance the integration between health and technology.

The spectrum of "whys" is vast, and your reason for contributing is valid, no matter what it is. We encourage you to share your unique "why" by contributing to this document. Your perspective could inspire others to join in! Thank you for being part of MedX. Your contributions, whatever the motivation, are invaluable.

## How to Contribute?
You are free to contribute to the MedX open-source project based on your interests and abilities, wherever you "want" and "can".

### Want to contribute to website development?
1. Fork the repository  
    Fork the repository to your own GitHub account to get started:
    - Go to the [MedX repository](https://github.com/MedX-Media/MedX) on GitHub.
    - Click the "Fork" button at the top of the page to create a copy of the repository in your GitHub account.
2. Clone the Repository  
    After forking the repository, clone it to your local machine so you can make changes:
    ```
    git clone https://github.com/YOUR_USERNAME/MedX.git
    ```
    Make sure to replace YOUR_USERNAME with your GitHub username.
3. Head over to the [issues section](https://github.com/MedX-Media/MedX/issues)  
    Browse the list of issues in the repository. Look for issues labeled "development," and choose the one you'd like to contribute to. Be sure to communicate your intent to work on an issue by commenting on it.
4. Create a New Branch  
    Before making any changes, create a new branch to work on. It’s a good practice to create a separate branch for each issue or feature:
    ```
    git checkout -b issue-name
    ```
    Replace issue-name with a descriptive name that relates to the issue or feature you’re working on.
5. Consider Development Principles:
    - Programming:
        - Check out [MedX src directory](https://github.com/MedX-Media/MedX/tree/main/src)
        - Write clean and well-organized code as much as possible.
        - Comment your code to ensure others can easily understand it.
    - Designing:
        - Check out [MedX design directory](https://github.com/MedX-Media/MedX/tree/main/design)
        - Design your ideas with any tools you want such as Figma, Photoshop, etc.
        - Put your output in the directory with a suitable file name.
6. Add and Commit Your Changes  
    Once you've made the necessary changes, stage and commit them to your local repository:
    ```
    git add .
    ```
    ```
    git commit -m "A brief description of your changes"
    ```
7. Push Changes to Your Fork  
    Push your changes to the forked repository in your GitHub account:
    ```
    git push origin issue-name
    ```
8. Submit a Pull Request  
    Once your changes are pushed to your fork, it's time to submit a pull request:
    - Go to your forked repository on GitHub.
    - Click the "Pull Request" button.
    - Select the MedX `development` branch as the **base** and `your` branch as the **compare**.
    - Write a detailed description of the changes you made, explaining how it resolves the issue or contributes to the project.
    - Submit the pull request.
9. That's it! You've contributed to MedX as a developer.

### Want to help with content creation?
1. You can choose the topic! Just make sure it's related to health tech.
2. Prepare a featured image for the post with a 1:1 aspect ratio. Feel free to use AI tools to create it if you'd like.
3. Consider Content Principles:
    - Your content can freely be a mix of text, images, videos, etc.
    - Your content must be authentic (You shouldn't use ai).
    - You shouldn't copy/translate it from anyone else on the internet.
    - You should write in Persian language, considering all its grammatical, spelling, and punctuation tips.
    - Make sure to include the sources you used at the end of your post.
    - You can use any content in your blog post, including images, videos, gits, etc. but if it's too long or too heavy, please upload it somewhere else and share its link in the blog.
4. To have your content considered for publication, you can email it to "medxmedia1@gmail.com" or our [Telegram admin](t.me/@MedX_admin). Send us your content with your full name and a photo of yourself, so we can feature you as the post's author on the website. We're also working on a self-service system for the next weeks, allowing you to post your content with all the website's features directly.
That's it! You've contributed to MedX as a content creator.

#### certified writers
Anyone can write on MedX's platform. However, to maintain content quality, we require a team of "certified writers". To become a certified writer, you can schedule a meeting with our Head of Writers. Before scheduling, please ensure you meet the eligibility criteria:
- You are passionate about empowering med people to know about health-tech-related topics.
- You are a good writer with a portfolio of written work. Please provide links to your samples.
- You have a strong understanding of the topics you wish to write about, backed by relevant experience or qualifications. Please provide links to your works/projects.

If you think you meet these criteria, we invite you to [set a meeting](https://calendly.com/medxmedia1/30min). Our [Telegram admin](t.me/@MedX_admin) is also available to answer any questions you may have.

---

## Issues

### What Are Issues? Why Do We Need Them?
Issues are tasks or improvements identified by the community to enhance the project. They help to keep track of bugs, enhancements, and features.

### When to Create an Issue?
An issue should be created when:
- You want to start working on something.
- You identify something that needs to be worked on, either by yourself or others.

### How to Create an Issue?
1. Navigate to the [issues section](https://github.com/MedX-Media/MedX/issues).
2. Click the "New Issue" button.
3. Set the title and description as clear and detailed as possible.
4. Specify other details:
    - **Assignee**: Every issue must be assigned to at least one person. This could be yourself or a team of people.
    - **Label**: Apply at least one label to every issue. Use correct labels that accurately reflect the issue's nature.  
        For example:  
        - 'good first issue': Suitable for new contributors.  
        - 'bug': Reports a defect or error.  
        - 'enhancement': Suggests a new feature or improvement.
    - **Project**: Select the relevant project the issue belongs to.
    - **Milestone**: Set the milestone related to the issue, if applicable.
5. Submit the issue.

### Where Can We Discuss Issues?
You can discuss issues on their individual pages or in the [MedX discussion](https://github.com/MedX-Media/MedX/discussions) section.

---



*Wait a few days please, it's being completed...*
