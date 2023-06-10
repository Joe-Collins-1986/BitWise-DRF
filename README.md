# BitWise - API

# Table Of Contents

- [Bitwise Site Links](#bitwise-site-links)
  - [Live API](#live-api)
  - [Live BitWise Site](#live-bitwise-site)
  - [Frontend Repo](#frontend-repo)
- [Bitwise Backend Overview](#bitwise-backend-overview)
  - [Project Introduction](#project-introduction)
- [Project Planning](#project-planning)
  - [Problem Statement](#problem-statement)
  - [Mind Map](#mind-map)
  - [API Objectives](#api-objectives)
  - [User Stories](#user-stories)
  - [Priority Matrix](#priority-matrix)
  - [Entity Relationship Diagram](#entity-relationship-diagram)
  - [Agile Methodology](#agile-methodology)
- [API Build](#api-build)
  - [Models]
  - [Views]
  - [Serializers]
  - [Permissons]
  - [Settings]
  - [CRUD - Endpoint Map]
- [Further Development]
- [Technologies Used]
  - [Languages Used]
  - [Frameworks Used]
  - [Libraries Used]
  - [Developer Tools]
- [Testing]
  - [Testing Document]
  - [Further Testing]
  - [Development Bugs]
  - [Key Learns]
- [Deployment]
  - [Deployment Document]
- [Credits]
  - [Development Resources]
  - [Media and Content Resources]
  - [Acknowledgements]

<br>

# Bitwise Site Links

## [Live API](https://bitwise-code-blog.herokuapp.com/#languages-update)

## [Live BitWise Site](https://bit-wise-front-end.vercel.app/)

## [Frontend Repo](https://github.com/Joe-Collins-1986/BitWise-Front-End)

<br>

# Bitwise Backend Overview

## Project Introduction

**Note:** For the purpose of this project a fictitious client has been generated to provide scope for:

- testing my API devlopment utilising Python through the use of a Django REST Framework (DRF).
- testing my Frontend development utilising HTML, CSS and JavaScript through the use of React (for more information on the frontend development visit my [BitWise Frontend Repo](https://github.com/Joe-Collins-1986/BitWise-Front-End))

The backend for this BitWise project has been developed with Django Rest Framework (DRF) for generation of an API. It provides various endpoints for user authentication, profile management, article handling, comments, likes, and more.

These endpoints will by utilised by the frontend application for development of a site where users post coding articles to the programming community.

Following discussions with the client this site will initially be tailored to written articles with the potential to expand to video uploads, live streaming and purchasable tutorials.

   <br>

# Project Planning

## Problem Statement

The client wishes to develop a social sharing platform targetted towards the programming community.

The developer worked with the client and focus groups consisting of programmers with varying levels of experience to establish the following problem statement. This was then used to establish some basic considerations which could be taken forward into a mind mapping session.

![Problem Statement](readme-assets/planning/brainstorming.png)
<br>
If you have a LucidChart account, you can also view this Problem Statement [here](https://lucid.app/lucidspark/ddcc77ae-81e5-48bb-a143-1d8d08517e84/edit?page=0_0&invitationId=inv_33957d7f-3414-4f5b-afb7-62686062836a#).
<br>

## Mind Map

The below image provides an initial mind-map into the features which might be appropriate for the BitWise API based on the problem statement. This will aide in the development of User Stories.

![Mind Map](readme-assets/planning/mind-map.png)
<br>
If you have a LucidChart account, you can also view this Mind-Map [here](https://lucid.app/lucidspark/92bb6c34-c508-4ed3-81f9-8e426a018834/edit?viewport_loc=-424%2C-51%2C1937%2C2060%2C0_0&invitationId=inv_e1afcf88-79d6-418d-b020-bca52437b6bf).
<br>

## API Objectives

<details>
    <summary style="font-weight:bold">Backend Requirements</summary>

The client wants a well structured backend with strong security and an administration panel allowing superusers CRUD functionality withing pre-built models to aide front end testing and API maintainance.

- Django REST authorisation established.
- SessionAuthentication for development and testing of DRF
- Permissions built for API CRUD.
- Development and Live databases set up.
- Static files and images housed on cloud server and linked to backend.
- API documentation developed to detail API endpoints and CRUD setup.

---

</details>

<details>
    <summary style="font-weight:bold">Frontend Requirements</summary>

The client wants the frontend developer to have JWT authorisation, access to all the required serialized data for the established models as well as query filters set up.

- Frontend granted access to make axios requests to API.
- JWTCookieAuthentication for external front end site.
- Models meet front end requirements.
- CRUD functionality meet front end requirements.
- Serializers built to pass appropriate data to endpoints used on interface.
- Error messages presented back through API for duplication attempts.
- Filters built to restrict quuery sets requested.
- Paginated API results to reduce payload requirements.

---

   </details>

## User Stories

All User Stories are detailed on my GitHub account as issues [here](https://github.com/Joe-Collins-1986/BitWise-DRF/issues?q=is%3Aissue+is%3Aclosed).<br>

These also breakdown:

- Tasks required for each User Story completion.
- Acceptance Criteria for each User Story.

    <details>
        <summary style="font-weight:bold">Example</summary>

  ![Example User Story](readme-assets/planning/example-user-story.png)

    </details>

## Priority Matrix

The below graphs map out the feasibility of the backend features considered against the user value they provide to help establish the priority they have as part of the build.

<details>
    <summary style="font-weight:bold">High Level Priority Matrix</summary>

![High Level Priority Matrix](readme-assets/planning/high-level-priority-matrix.png)
<br>

</details>

<details>
    <summary style="font-weight:bold">Detailed Priority Matrix</summary>

![Detailed Priority Matrix](readme-assets/planning/detailed-priority-matrix.png)
<br>

If you have a LucidChart account, you can also view this priority matrix [here](https://lucid.app/lucidspark/0daa104b-7056-4351-b4f9-e2e77701b480/edit?viewport_loc=769%2C650%2C6475%2C6256%2C0_0&invitationId=inv_e5bb265c-e341-41fd-9c04-266266ad9a61).
<br>

</details>

## Entity Relationship Diagram

The below demonstrates the API models and their attributes as well as documenting how they interact.

![DataBase ER Diagram](readme-assets/planning/entity-relationship-diagram.png)<br>

If you have a LucidChart account, you can also view this functions flow [here](https://lucid.app/lucidchart/9582ec18-126e-4b88-b601-011cb64f6e74/edit?viewport_loc=121%2C-170%2C1656%2C1932%2C0_0&invitationId=inv_0eff3f1b-ba36-4160-a99a-1fa7881fa18a).
<br>

# API Build

## Agile Methodology

An Agile methodology was applied to the development and implementation of this project.

The project development as a whole was was run in multiple iterations/sprints each targeting a number of User Stories. However, due to the relience of the frontend development on the API the first iteration/sprint was assigned to the Backend in it's entirety.

Each User Story was moved out of a backlog and assigned to the iteration with a priority label (Must Have, Should Have, Could Have). **Note:** Due the completion of all userstories within the iteration assinged deadline there was no reason to move any of the user stories back to Backlog and generate a following backend iteration with revised priority labels.

To manage the Agile backend iteration I used the projects function within my GitHub account, pulling User Stories into a KanBan Board.

For site of the project in GitHub detailing the completed User Stories for the backend iteration please click [here](https://github.com/users/Joe-Collins-1986/projects/9).

**Note:** It should be noted that the priority label was in relation to it's prioriry within the iteration, not the project as a whole.

## Models

<details>
    <summary style="font-weight:bold">Article Model</summary>

| Field Name       | Field Type                 | Description                             |
| ---------------- | -------------------------- | --------------------------------------- |
| owner            | ForeignKey (User)          | User who owns the article               |
| created_at       | DateTimeField              | Date and time of creation               |
| updated_at       | DateTimeField              | Date and time of last update            |
| article_title    | CharField (max_length=255) | Title of the article                    |
| article_content  | TextField                  | Content of the article                  |
| primary_language | CharField (max_length=25)  | Primary language of the article         |
| github_link      | URLField                   | Link to the article's GitHub repository |

</details>

<details>
    <summary style="font-weight:bold">Comment Model</summary>

| Field Name | Field Type           | Description                          |
| ---------- | -------------------- | ------------------------------------ |
| owner      | ForeignKey (User)    | User who owns the comment            |
| article    | ForeignKey (Article) | Article to which the comment belongs |
| created_at | DateTimeField        | Date and time of creation            |
| updated_at | DateTimeField        | Date and time of last update         |
| body       | TextField            | Content of the comment               |

</details>

<details>
    <summary style="font-weight:bold">Profile Model</summary>

| Field Name   | Field Type                | Description                                                     |
| ------------ | ------------------------- | --------------------------------------------------------------- |
| owner        | OneToOneField (User)      | User who owns the profile                                       |
| created_at   | DateTimeField             | Date and time of creation                                       |
| profile_name | CharField (max_length=50) | Name of the profile                                             |
| bio          | TextField                 | Biography or description of the profile                         |
| image        | ResizedImageField         | Profile image, resized and stored in specified upload directory |

</details>

<details>
    <summary style="font-weight:bold">Follower Model</summary>

| Field Name | Field Type        | Description                                        |
| ---------- | ----------------- | -------------------------------------------------- |
| owner      | ForeignKey (User) | User who is the owner of the follower relationship |
| followed   | ForeignKey (User) | User who is being followed by the owner            |
| created_at | DateTimeField     | Date and time of creation                          |

</details>

<details>
    <summary style="font-weight:bold">Language Model</summary>

Certainly! Here's the markdown table representing the Language model:

sql
Copy code
| Field Name | Field Type | Description |
|-------------|-----------------------------|------------------------------------------------|
| owner | ForeignKey (User) | User who owns the language experience |
| language | CharField (max_length=25) | Name of the language |
| confidence | IntegerField | Confidence level in the language (1-100) |
| used_since | DateField (null=True) | Date when the language started being used |

</details>

<details>
    <summary style="font-weight:bold">Like Model</summary>

| Field Name | Field Type           | Description                 |
| ---------- | -------------------- | --------------------------- |
| owner      | ForeignKey (User)    | User who owns the like      |
| article    | ForeignKey (Article) | Article that is being liked |
| created_at | DateTimeField        | Date and time of creation   |

</details>

## Views

<details>
    <summary style="font-weight:bold">Article View</summary>

### ArticleList

The ArticleList view is a Django view that provides the necessary functionality to list and create articles. It inherits from generics.ListCreateAPIView, which is a generic view provided by the Django REST Framework.

Features

- List out all the articles:
  Inheriting from generics.ListCreateAPIView provides the necessary functionality to list all articles. The queryset is defined to fetch articles from the database, annotated with counts of comments and likes, and ordered by the creation date in descending order.

- The ArticleList view uses the ArticleSerializer for serializing and deserializing article data.

- The permission classes used for this view allow authenticated users to perform read (list) operations but require authentication for write (create) operations. This is specified by permissions.IsAuthenticatedOrReadOnly.

- The perform_create method is overridden to automatically set the owner field of the created article to the authenticated user (request.user).

Added filtering functionality provided by the DjangoFilterBackend.

- Add search filter against article owner and article title:
  Articles can be searched based on the article owner (owner\_\_username) and article title (article_title). The search functionality is provided by the filters.SearchFilter backend.

- Filter order by counts and date of likes and comments:
  Articles can be ordered based on the counts and dates of likes and comments. The ordering fields available are comments_count and likes_count. The ordering functionality is provided by the filters.OrderingFilter backend.

- Filter by fieldsets - following, followed, article language, profile:
  Articles can be filtered based on different fieldsets, including:

  - owner**followed**owner\_\_profile: Filter articles based on the profiles of users who are followed by the owner of the article.
  - likes**owner**profile: Filter articles based on the profiles of users who have liked the article.
  - owner\_\_profile: Filter articles based on the profile of the article owner.
  - primary_language: Filter articles based on the primary language of the article.

By utilizing the ArticleList view, users can efficiently list, create, search, order, and filter articles based on various criteria.

### ArticleDetail

The same Article serializer_class and permission_classes are used used for this view, and the permission_classes attribute sets the permission classes, with IsOwnerOrReadOnly being the only permission class defined.

As with the ArticleList, the ArticleDetail view also annotates the queryset with counts of comments and likes, and orders the queryset by the creation date in descending order.

The serializer_class specifies the serializer to use for this view, and the permission_classes attribute sets the permission classes, with IsOwnerOrReadOnly being the only permission class defined.

By using the IsOwnerOrReadOnly permission class, only the owner of the article will have permission to update or delete the article information, while other users will only have read-only access.

Overall, the ArticleDetail view provides the necessary functionality for retrieving, updating, and deleting a specific article while ensuring that only the owner of the article can modify its data.

</details>

<details>
    <summary style="font-weight:bold">Comment View</summary>

</details>

## Serializers

## Permissons

## Settings

## CRUD - Endpoint Map

To detail the API CRUD functionality in full an API documentation page has been developed [here](https://bitwise-code-blog.herokuapp.com/#)

<details>
    <summary style="font-weight:bold">API Documentation Page Excert</summary>

![API Documentation](readme-assets/build/api-doc.png)

</details>

<details>
    <summary style="font-weight:bold">CRUD Table</summary>

| TOPIC     | URL                            | LIST/READ<br>(GET)   | CREATE<br>(POST)                                                                         | UPDATE<br>(PUT) | PARTIAL UPDATE<br>(PATCH) | DELETE<br>(DELETE) | OVERALL  |
| --------- | ------------------------------ | -------------------- | ---------------------------------------------------------------------------------------- | --------------- | ------------------------- | ------------------ | -------- |
| AUTH      | /dj-rest-auth/registration/    | ❌                   | ✅                                                                                       | ❌              | ❌                        | ❌                 | C        |
| AUTH      | /dj-rest-auth/login/           | ❌                   | ✅                                                                                       | ❌              | ❌                        | ❌                 | C        |
| AUTH      | /dj-rest-auth/logout/          | EXISITS BUT NOT USED | ✅                                                                                       | ❌              | ❌                        | ❌                 | C (USED) |
| AUTH      | /dj-rest-auth/user/            | ✅                   | GENERATED ON REGISTRATION.                                                               | ✅              | ✅                        | ❌                 | RU       |
| AUTH      | /dj-rest-auth/password/change/ | ❌                   | ✅                                                                                       | ❌              | ❌                        | ❌                 | C        |
| AUTH      | /dj-rest-auth/token/refresh/   | ❌                   | ✅                                                                                       | ❌              | ❌                        | ❌                 | C        |
|           |
| ARTICLES  | /articles/                     | ✅                   | ✅                                                                                       | ❌              | ❌                        | ❌                 |          |
| ARTICLES  | /articles/{id}/                | ✅                   | ❌                                                                                       | ✅              | ✅                        | ✅                 | CRUD     |
|           |                                |                      |
| COMMENTS  | /comments/                     | ✅                   | ✅                                                                                       | ❌              | ❌                        | ❌                 |          |
| COMMENTS  | /comments/{id}/                | ✅                   | ❌                                                                                       | ✅              | ✅                        | ✅                 | CRUD     |
|           |                                |                      |                                                                                          |                 |                           |                    |          |
| PROFILES  | /profiles/                     | ✅                   | AUTO GENERATED ON USER REGISTRATION VIA SIGNAL. NO ABILITY TO CREATE VIA API SUBMISSION. | ❌              | ❌                        | ❌                 |          |
| PROFILES  | /profiles/{id}/                | ✅                   | ❌                                                                                       | ✅              | ✅                        | ❌                 | RU       |
|           |                                |                      |                                                                                          |                 |                           |                    |          |
| FOLLOWERS | /followers/                    | ✅                   | ✅                                                                                       | ❌              | ❌                        | ❌                 |          |
| FOLLOWERS | /followers/{id}/               | ✅                   | ❌                                                                                       | ❌              | ❌                        | ✅                 | CRD      |
|           |                                |
| LANGUAGES | /languages/                    | ✅                   | ✅                                                                                       | ❌              | ❌                        | ❌                 |          |
| LANGUAGES | /languages/{id}/               | ✅                   | ❌                                                                                       | ✅              | ✅                        | ✅                 | CRUD     |
|           |                                |
| LIKES     | /likes/                        | ✅                   | ✅                                                                                       | ❌              | ❌                        | ❌                 |          |
| LIKES     | /likes/{id}/                   | ✅                   | ❌                                                                                       | ❌              | ❌                        | ✅                 | CRD      |

**Note:** Additional endpoints exist for auth functionality. Only detailed ones used.<br>
For further insight into endpoinds see API ducmentation [link](https://bitwise-code-blog.herokuapp.com/#)

- Website used to convert excel to markdown: [here](https://tabletomarkdown.com/convert-spreadsheet-to-markdown/)
- Website used to convert back to excel incase updates required: [here](https://tableconvert.com/markdown-to-excel)

</details>