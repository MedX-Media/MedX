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
1. Fork the repository.
2. Head over to the [issues section](https://github.com/MedX-Media/MedX/issues) and pick those labeled "development", and contribute to any issue you'd like.
3. Consider Development Principles:
    - Programming:
        - Check out [MedX src directory](https://github.com/MedX-Media/MedX/tree/main/src)
        - Write clean and well-organized code as much as possible.
        - Comment your code to ensure others can easily understand it.
    - Designing:
        - Check out [MedX design directory](https://github.com/MedX-Media/MedX/tree/main/design)
        - Design your ideas with any tools you want such as Figma, Photoshop, etc.
        - Put your output in the directory with a suitable file name.
4. Once you've resolved an issue, submit a pull request from "your fork" to "MedX development branch", including a detailed explanation.
That's it! You've contributed to MedX as a developer.

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

برای مستندسازی فرآیند ایجاد فایل `pre-commit` و فرمت کردن کدها در پروژه‌تان، می‌توانید یک فایل Markdown (مثلاً `SETUP.md` یا `CONTRIBUTING.md`) بسازید و مراحل و توضیحات مربوطه را در آن قرار دهید. در ادامه یک نمونه مستندات برای این کار آورده شده است:

---

# Setup Pre-Commit Hook for Code Formatting

## Introduction
This document outlines the steps to set up a pre-commit hook for automatic code formatting in our project. By implementing this hook, we can ensure that all code is properly formatted before it is committed to the repository.

## Prerequisites
Before proceeding, ensure that the following tools are installed:

- **Python** (and pip)
- **Node.js** (and npm)
- **Black** (for Python formatting)
- **Prettier** (for HTML, CSS, and JavaScript formatting)
- **isort** (for sorting Python imports)

## Steps to Create a Pre-Commit Hook

### 1. Navigate to the Git Hooks Directory
Go to the `.git/hooks` directory in your project:
```bash
cd .git/hooks
```

### 2. Create the Pre-Commit File
Create a new file named `pre-commit`:
```bash
touch pre-commit
```

### 3. Add Formatting Commands
Open the `pre-commit` file in a text editor and add the following code:

```bash
#!/bin/sh

# Format Python files with Black
echo "Formatting Python files..."
black .

# Format HTML, CSS, and JavaScript files with Prettier
echo "Formatting HTML, CSS, and JavaScript files..."
npx prettier --write "**/*.html" "**/*.css" "**/*.js"

# Sort imports for Python files
echo "Sorting imports in Python files..."
isort .

echo "Pre-commit formatting done."
```

### 4. Make the Pre-Commit File Executable
Make the `pre-commit` file executable by running:
```bash
chmod +x pre-commit
```

### 5. Testing the Pre-Commit Hook
To test the pre-commit hook, make some changes to your code and then attempt to commit:
```bash
git add .
git commit -m "Test pre-commit hook"
```

### 6. Additional Notes
- Ensure that **Black** and **Prettier** are installed as dependencies in your project.
- You can customize the pre-commit hook by adding any other formatting or linting tools you prefer.

## Conclusion
By following these steps, you can set up a pre-commit hook that automatically formats your code before each commit. This helps maintain code quality and consistency across the project.

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
