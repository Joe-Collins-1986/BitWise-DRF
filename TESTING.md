# Testing

Back to Readme [here](README.md)

# Table Of Contents

- [Python Unit Testing](#python-unit-testing)
- [Python Validation Testing](#python-validation-testing)
- [User Story Testing](#user-story-testing)
- [Manual Testing](#user-testing)

<br>

---

## Python Unit Testing

Unit Testing coverage<br>
![Summary Unit Tests](readme-assets/unit_testing/summary-report.png)

(excluding settings and manage.py files)

**Note** See Bitwise App coverage below for detail on the one missing coverage element.

See below for details on each app:

<details>
      <summary style="font-weight:bold">Article App</summary>
   
Article app covered to 100%:

![Article Unit Tests](readme-assets/unit_testing/articles.png)<br>

---

</details>

<details>
      <summary style="font-weight:bold">Bitwise App</summary>
   
Bitwise app - One missing element:

The single missed coverage element is in relation to a missing test for the IsRecipientOrReadOnly permission where the individual has SAFE_METHOD permissions. This is because the build is set up so only show recommended articles to the recipient. However, I wished to keep this permision in place for potential future changes where I may make to allow the creator to view recomendations they have made but not ammend/delete them. As a result this was left as missing coverage.

![BitWise Unit Tests](readme-assets/unit_testing/bitwise.png)<br>

![BitWise Unit Test Detail](readme-assets/unit_testing/bitwise-detail.png)<br>

---

</details>

<details>
      <summary style="font-weight:bold">Comment App</summary>
   
Comment app covered to 100%:

![Comment Unit Tests](readme-assets/unit_testing/comments.png)<br>

---

</details>

<details>
      <summary style="font-weight:bold">Follower App</summary>
   
Follower app covered to 100%:

![Follower Unit Tests](readme-assets/unit_testing/followers.png)<br>

---

</details>

<details>
      <summary style="font-weight:bold">Language App</summary>
   
Language app covered to 100%:

![Language Unit Tests](readme-assets/unit_testing/languages.png)<br>

---

</details>

<details>
      <summary style="font-weight:bold">Like App</summary>
   
Like app covered to 100%:

![Like Unit Tests](readme-assets/unit_testing/likes.png)<br>

---

</details>

<details>
      <summary style="font-weight:bold">Profile App</summary>
   
Profile app covered to 100%:

![Profile Unit Tests](readme-assets/unit_testing/profiles.png)<br>

---

</details>

<details>
      <summary style="font-weight:bold">Recommended App</summary>
   
Recommended app covered to 100%:

![Recommended Unit Tests](readme-assets/unit_testing/recommended.png)<br>

---

</details>

<details>
      <summary style="font-weight:bold">Link App</summary>
   
Link app covered to 100%:

![Link Unit Tests](readme-assets/unit_testing/links.png)<br>

---

</details>

</details>

## Python Validation Testing

<details>
      <summary style="font-weight:bold">Article</summary>
<br>

Admin:

![Admin](readme-assets/pep8/articles/admin.png)

---

Models:

![Models](readme-assets/pep8/articles/models.png)

---

Views:

![Views](readme-assets/pep8/articles/views.png)

---

Serializers:

![Serializers](readme-assets/pep8/articles/serializers.png)

---

URLs:

![URLs](readme-assets/pep8/articles/urls.png)

---

</details>

<details>
      <summary style="font-weight:bold">Article Tests</summary>
<br>

Models:

![Models](readme-assets/pep8/articles-tests/test-model.png)

---

Views:

![Views](readme-assets/pep8/articles-tests/test-views.png)

---

Serializers:

![Serializers](readme-assets/pep8/articles-tests/test-serializers.png)

---

</details>

<details>
      <summary style="font-weight:bold">BitWise</summary>
<br>

Permissons:

![Permissons](readme-assets/pep8/bitwise/permissions.png)

---

Views:

![Views](readme-assets/pep8/bitwise/views.png)

---

Serializers:

![Serializers](readme-assets/pep8/bitwise/serializers.png)

---

URLs:

![URLs](readme-assets/pep8/bitwise/urls.png)

---

</details>

<details>
      <summary style="font-weight:bold">BitWise Tests</summary>
<br>

Views:

![Views](readme-assets/pep8/bitwise-tests/test-views.png)

---

</details>

<details>
      <summary style="font-weight:bold">Comments</summary>
<br>

Admin:

![Admin](readme-assets/pep8/comments/admin.png)

---

Models:

![Models](readme-assets/pep8/comments/models.png)

---

Views:

![Views](readme-assets/pep8/comments/views.png)

---

Serializers:

![Serializers](readme-assets/pep8/comments/serializers.png)

---

URLs:

![URLs](readme-assets/pep8/comments/urls.png)

---

</details>

<details>
      <summary style="font-weight:bold">Comments Tests</summary>
<br>

Models:

![Models](readme-assets/pep8/comments-tests/test-models.png)

---

Views:

![Views](readme-assets/pep8/comments-tests/test-views.png)

---

Serializers:

![Serializers](readme-assets/pep8/comments-tests/test-serializers.png)

---

</details>

<details>
      <summary style="font-weight:bold">Followers</summary>
<br>

Admin:

![Admin](readme-assets/pep8/followers/admin.png)

---

Models:

![Models](readme-assets/pep8/followers/models.png)

---

Views:

![Views](readme-assets/pep8/followers/views.png)

---

Serializers:

![Serializers](readme-assets/pep8/followers/serializers.png)

---

URLs:

![URLs](readme-assets/pep8/followers/urls.png)

---

</details>

<details>
      <summary style="font-weight:bold">Followers Tests</summary>
<br>

Models:

![Models](readme-assets/pep8/followers-tests/test-models.png)

---

Views:

![Views](readme-assets/pep8/followers-tests/test-views.png)

---

Serializers:

![Serializers](readme-assets/pep8/followers-tests/test-serializers.png)

---

</details>

<details>
      <summary style="font-weight:bold">Languages</summary>
<br>

Admin:

![Admin](readme-assets/pep8/languages/admin.png)

---

Models:

![Models](readme-assets/pep8/languages/models.png)

---

Views:

![Views](readme-assets/pep8/languages/views.png)

---

Serializers:

![Serializers](readme-assets/pep8/languages/serializers.png)

---

URLs:

![URLs](readme-assets/pep8/languages/urls.png)

---

</details>

<details>
      <summary style="font-weight:bold">Languages Tests</summary>
<br>

Models:

![Models](readme-assets/pep8/languages-tests/test-models.png)

---

Views:

![Views](readme-assets/pep8/languages-tests/test-views.png)

---

Serializers:

![Serializers](readme-assets/pep8/languages-tests/test-serializers.png)

---

</details>

<details>
      <summary style="font-weight:bold">Likes</summary>
<br>

Admin:

![Admin](readme-assets/pep8/likes/admin.png)

---

Models:

![Models](readme-assets/pep8/likes/models.png)

---

Views:

![Views](readme-assets/pep8/likes/views.png)

---

Serializers:

![Serializers](readme-assets/pep8/likes/serializers.png)

---

URLs:

![URLs](readme-assets/pep8/likes/urls.png)

---

</details>

<details>
      <summary style="font-weight:bold">Likes Tests</summary>
<br>

Models:

![Models](readme-assets/pep8/likes-tests/test-models.png)

---

Views:

![Views](readme-assets/pep8/likes-tests/test-views.png)

---

Serializers:

![Serializers](readme-assets/pep8/likes-tests/test-serializers.png)

---

</details>

<details>
      <summary style="font-weight:bold">Profiles</summary>
<br>

Admin:

![Admin](readme-assets/pep8/profiles/admin.png)

---

Models:

![Models](readme-assets/pep8/profiles/models.png)

---

Views:

![Views](readme-assets/pep8/profiles/views.png)

---

Serializers:

![Serializers](readme-assets/pep8/profiles/serializers.png)

---

URLs:

![URLs](readme-assets/pep8/profiles/urls.png)

---

</details>

<details>
      <summary style="font-weight:bold">Profiles Tests</summary>
<br>

Models:

![Models](readme-assets/pep8/profiles-tests/test-model.png)

---

Views:

![Views](readme-assets/pep8/profiles-tests/test-views.png)

---

Serializers:

![Serializers](readme-assets/pep8/profiles-tests/test-serializers.png)

---

</details>

<details>
      <summary style="font-weight:bold">Recommended</summary>
<br>

Admin:

![Admin](readme-assets/pep8/recommended/admin.png)

---

Models:

![Models](readme-assets/pep8/recommended/models.png)

---

Views:

![Views](readme-assets/pep8/recommended/views.png)

---

Serializers:

![Serializers](readme-assets/pep8/recommended/serializers.png)

---

URLs:

![URLs](readme-assets/pep8/recommended/urls.png)

---

</details>

<details>
      <summary style="font-weight:bold">Recommended Tests</summary>
<br>

Models:

![Models](readme-assets/pep8/recommended-tests/test-models.png)

---

Views:

![Views](readme-assets/pep8/recommended-tests/test-views.png)

---

</details>

<details>
      <summary style="font-weight:bold">Links</summary>
<br>

Admin:

![Admin](readme-assets/pep8/links/admin.png)

---

Models:

![Models](readme-assets/pep8/links/models.png)

---

Views:

![Views](readme-assets/pep8/links/views.png)

---

Serializers:

![Serializers](readme-assets/pep8/links/serializers.png)

---

URLs:

![URLs](readme-assets/pep8/links/urls.png)

---

</details>

<details>
      <summary style="font-weight:bold">Links Tests</summary>
<br>

Models:

![Models](readme-assets/pep8/links-tests/test-model.png)

---

Views:

![Views](readme-assets/pep8/links-tests/test-views.png)

---

Serializers:

![Serializers](readme-assets/pep8/links-tests/test-serializers.png)

---

</details>

## User Story Testing

### User Stories Acceptance Criteria

Each User Story documented (as an issue) in the Backend Project Iterations [here](https://github.com/Joe-Collins-1986/BitWise-DRF/projects?query=is%3Aclosed) have Acceptance Criteria documented on GitHub which needed to be achieved before marking the User Sory to complete.

To view these access the User Story Issues.

Example Screenshot of User Story in Iteration:
<br>

![Example Screenshot Of a User Story](readme-assets/planning/example-user-story.png)

## Manual Testing

### Articles:

#### CRUD TESTING IN DEV ENV

| CRUD Article Testing                 | ✅  |
| ------------------------------------ | --- |
| Create                               | ✅  |
| Read                                 | ✅  |
| Delete                               | ✅  |
| Update                               | ✅  |
| Create restricted to authorised user | ✅  |
| Update & Delete restricted to owner  | ✅  |

#### GET ARTICLES

| Articles                                       | Result                                                                                         |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| results returned                               | ✅ [link](https://bitwise-code-blog.herokuapp.com/articles/)                                   |
| page filter returns page                       | ✅ [link](https://bitwise-code-blog.herokuapp.com/articles/?page=1)                            |
| invalid page returns "detail": "Invalid page." | ✅ [link](https://bitwise-code-blog.herokuapp.com/articles/?page=9999)                         |
| search filter works for owner                  | ✅ [link](https://bitwise-code-blog.herokuapp.com/articles/?search=Joe)                        |
| search filter works for title                  | ✅ [link](https://bitwise-code-blog.herokuapp.com/articles/?search=article)                    |
| order by comment count                         | ✅ [link](https://bitwise-code-blog.herokuapp.com/articles/?ordering=-comments_count)          |
| order by likes count                           | ✅ [link](https://bitwise-code-blog.herokuapp.com/articles/?ordering=-likes_count)             |
| all articles being followed by profile 1       | ✅ [link](https://bitwise-code-blog.herokuapp.com/articles/?owner__followed__owner__profile=1) |
| all articles liked by profile 1                | ✅ [link](https://bitwise-code-blog.herokuapp.com/articles/?likes__owner__profile=1)           |
| all articles written about Python              | ✅ [link](https://bitwise-code-blog.herokuapp.com/articles/?primary_language=Python)           |
| specific article                               | ✅ [link](https://bitwise-code-blog.herokuapp.com/articles/2/)                                 |

### Comments:

#### CRUD TESTING IN DEV ENV

| CRUD Comment Testing                 | ✅  |
| ------------------------------------ | --- |
| Create                               | ✅  |
| Read                                 | ✅  |
| Delete                               | ✅  |
| Update                               | ✅  |
| Create restricted to authorised user | ✅  |
| Update & Delete restricted to owner  | ✅  |

#### GET COMMENTS

| Comments                                       | Result                                                                 |
| ---------------------------------------------- | ---------------------------------------------------------------------- |
| results returned                               | ✅ [link](https://bitwise-code-blog.herokuapp.com/comments/)           |
| page filter returns page                       | ✅ [link](https://bitwise-code-blog.herokuapp.com/comments/?page=1)    |
| invalid page returns "detail": "Invalid page." | ✅ [link](https://bitwise-code-blog.herokuapp.com/comments/?page=9999) |
| returns comment linked to specific article     | ✅ [link](https://bitwise-code-blog.herokuapp.com/comments/?article=2) |
| specific comment                               | ✅ [link](https://bitwise-code-blog.herokuapp.com/comments/11/)        |

### Followers:

#### CRUD TESTING IN DEV ENV

| CRUD Follower Testing                | ✅  |
| ------------------------------------ | --- |
| Create                               | ✅  |
| Read                                 | ✅  |
| Delete                               | ✅  |
| Create restricted to authorised user | ✅  |
| Delete restricted to owner           | ✅  |

#### GET FOLLOWERS

| Followers                                      | Result                                                                  |
| ---------------------------------------------- | ----------------------------------------------------------------------- |
| results returned                               | ✅ [link](https://bitwise-code-blog.herokuapp.com/followers/)           |
| page filter returns page                       | ✅ [link](https://bitwise-code-blog.herokuapp.com/followers/?page=1)    |
| invalid page returns "detail": "Invalid page." | ✅ [link](https://bitwise-code-blog.herokuapp.com/followers/?page=9999) |
| specific follower                              | ✅ [link](https://bitwise-code-blog.herokuapp.com/followers/100/)       |

### Languages:

#### CRUD TESTING IN DEV ENV

| CRUD Languages Testing               | ✅  |
| ------------------------------------ | --- |
| Create                               | ✅  |
| Read                                 | ✅  |
| Update                               | ✅  |
| Delete                               | ✅  |
| Create restricted to authorised user | ✅  |
| Update & Delete restricted to owner  | ✅  |

#### GET LANGUAGES

| Languages                                      | Result                                                                         |
| ---------------------------------------------- | ------------------------------------------------------------------------------ |
| results returned                               | ✅ [link](https://bitwise-code-blog.herokuapp.com/languages/)                  |
| page filter returns page                       | ✅ [link](https://bitwise-code-blog.herokuapp.com/languages/?page=1)           |
| invalid page returns "detail": "Invalid page." | ✅ [link](https://bitwise-code-blog.herokuapp.com/languages/?page=9999)        |
| returns language linked to specific profile    | ✅ [link](https://bitwise-code-blog.herokuapp.com/languages/?owner__profile=1) |
| specific language                              | ✅ [link](https://bitwise-code-blog.herokuapp.com/languages/63/)               |

### Likes:

#### CRUD TESTING IN DEV ENV

| CRUD Likes Testing                   | ✅  |
| ------------------------------------ | --- |
| Create                               | ✅  |
| Read                                 | ✅  |
| Delete                               | ✅  |
| Create restricted to authorised user | ✅  |
| Delete restricted to owner           | ✅  |

#### GET LIKES

| Likes                                          | Result                                                              |
| ---------------------------------------------- | ------------------------------------------------------------------- |
| results returned                               | ✅ [link](https://bitwise-code-blog.herokuapp.com/likes/)           |
| page filter returns page                       | ✅ [link](https://bitwise-code-blog.herokuapp.com/likes/?page=1)    |
| invalid page returns "detail": "Invalid page." | ✅ [link](https://bitwise-code-blog.herokuapp.com/likes/?page=9999) |
| specific like                                  | ✅ [link](https://bitwise-code-blog.herokuapp.com/likes/20/)        |

### Profiles:

#### CRUD TESTING IN DEV ENV

| CRUD Profiles Testing      | ✅  |
| -------------------------- | --- |
| Read                       | ✅  |
| Update restricted to owner | ✅  |

#### GET PROFILES

| Profiles                                       | Result                                                                                             |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| results returned                               | ✅ [link](https://bitwise-code-blog.herokuapp.com/profiles/)                                       |
| page filter returns page                       | ✅ [link](https://bitwise-code-blog.herokuapp.com/profiles/?page=1)                                |
| invalid page returns "detail": "Invalid page." | ✅ [link](https://bitwise-code-blog.herokuapp.com/profiles/?page=9999)                             |
| search filter works for profile name           | ✅ [link](https://bitwise-code-blog.herokuapp.com/profiles/?search=joe)                            |
| order by article count                         | ✅ [link](https://bitwise-code-blog.herokuapp.com/profiles/?ordering=-article_count)               |
| order by followed count                        | ✅ [link](https://bitwise-code-blog.herokuapp.com/profiles/?ordering=-followed_count)              |
| order by following count                       | ✅ [link](https://bitwise-code-blog.herokuapp.com/profiles/?ordering=-following_count)             |
| order by language count                        | ✅ [link](https://bitwise-code-blog.herokuapp.com/profiles/?ordering=-languages_count)             |
| all profiles following profile 1               | ✅ [link](https://bitwise-code-blog.herokuapp.com/profiles/?owner__following__followed__profile=1) |
| all profiles followed by profile 1             | ✅ [link](https://bitwise-code-blog.herokuapp.com/profiles/?owner__followed__owner__profile=1)     |
| All profiles that have knowledge of HTML       | ✅ [link](https://bitwise-code-blog.herokuapp.com/profiles/?owner__languages__language=HTML)       |
| specific profile                               | ✅ [link](https://bitwise-code-blog.herokuapp.com/profiles/1/)                                     |

### Recommendations:

#### CRUD TESTING IN DEV ENV

| CRUD Recommendation Testing          | ✅  |
| ------------------------------------ | --- |
| Create                               | ✅  |
| Read                                 | ✅  |
| Delete                               | ✅  |
| Create restricted to authorised user | ✅  |
| Delete restricted to recipient       | ✅  |

#### GET RECOMMENDATIONS

To test the following links you must be logged in to an account with recommendations assigned to you or will recieve "Authentication credentials were not provided."

| Recommendations                                | Result                                                                       |
| ---------------------------------------------- | ---------------------------------------------------------------------------- |
| results returned                               | ✅ [link](https://bitwise-code-blog.herokuapp.com/recomendations/)           |
| page filter                                    | ✅ [link](https://bitwise-code-blog.herokuapp.com/recomendations/?page=1)    |
| invalid page returns "detail": "Invalid page." | ✅ [link](https://bitwise-code-blog.herokuapp.com/recomendations/?page=9999) |

### Links:

#### CRUD TESTING IN DEV ENV

| CRUD Link Testing                    | ✅  |
| ------------------------------------ | --- |
| Create                               | ✅  |
| Read                                 | ✅  |
| Update                               | ✅  |
| Delete                               | ✅  |
| Create restricted to authorised user | ✅  |
| Update & Delete restricted to owner  | ✅  |

#### GET LINKS

| Links                                          | Result                                                                     |
| ---------------------------------------------- | -------------------------------------------------------------------------- |
| results returned                               | ✅ [link](https://bitwise-code-blog.herokuapp.com/links/)                  |
| page filter                                    | ✅ [link](https://bitwise-code-blog.herokuapp.com/links/?page=1)           |
| invalid page returns "detail": "Invalid page." | ✅ [link](https://bitwise-code-blog.herokuapp.com/links/?page=9999)        |
| filter links by owner's profile                | ✅ [link](https://bitwise-code-blog.herokuapp.com/links/?owner__profile=1) |
| filter links by owner's profile                | ✅ [link](https://bitwise-code-blog.herokuapp.com/links/?article=2)        |
| specific link                                  | ✅ [link](https://bitwise-code-blog.herokuapp.com/links/16/)               |
