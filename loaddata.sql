-- DROP TABLE "Posts"
CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);

CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

INSERT INTO Categories ('label') VALUES ('News');
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (1, 1);
INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');




INSERT INTO Posts ('user_id', 'category_id', 'title', 'publication_date', 'image_url', 'content', 'approved') VALUES (1, 2, 'group project', '2022-07-12', 'https://pngtree.com/so/happy', 'everyone did one pull request', 1);

INSERT INTO Tags ('label') VALUES ('SQL');
INSERT INTO Tags ('label') VALUES ('Python');

INSERT INTO `Users` VALUES (null, "Syndney", "Dickson", "sydrocks@gmail.com", "I am a rockstar", "syd", "password", "", "Wed Sep 15 2021 10:14:05 ", 1);
INSERT INTO `Users` VALUES (null, "Camille", "Faulkner", "camrocks@gmail.com", "I am a powerhouse", "cam", "password", "", "Wed Sep 15 2021 10:14:05 ", 1);
INSERT INTO `Users` VALUES (null, "Connor", "Lopshire", "conrocks@gmail.com", "I am an organizer", "con", "password", "", "Wed Sep 15 2021 10:14:05 ", 1);
INSERT INTO `Users` VALUES (null, "Claire", "Morgan-Sanders", "morgrocks@gmail.com", "I am a code genious", "morg", "password", "", "Wed Sep 15 2021 10:14:05 ", 1);
INSERT INTO `Users` VALUES (null, "Tiana", "Robinson", "tiarocks@gmail.com", "I am a goof", "tia", "password", "", "Wed Sep 15 2021 10:14:05 ", 1);

INSERT INTO `Posts` VALUES ( 1, 2, 1, 'testing', '2022-07-20', 'https://pngtree.com/so/happy', 'testing', 1);

INSERT INTO `Comments` VALUES ( null, 1, 1, 'testing');

SELECT
        p.id,
        p.user_id,
        p.category_id,
        p.title,
        p.publication_date,
        p.image_url,
        p.content,
        p.approved,
        c.label,
        u.first_name,
        u.last_name,
        u.email,
        u.bio,
        u.username,
        u.password,
        u.profile_image_url,
        u.created_on,
        u.active

        FROM Posts p
        JOIN Users u
            ON u.id = p.user_id
        JOIN Categories c
            ON c.id = p.category_id
            
INSERT INTO Categories ('label') VALUES ('Code');
INSERT INTO `Posts` VALUES ( null, 1, 1, 'testing', '2022-07-20', 'https://pngtree.com/so/happy', 'testing', 1);

SELECT
      c.id,
      c.post_id,
	    c.author_id,
	    c.content
    FROM Comments c
    Where post_id = 1

INSERT INTO `Posts` VALUES ( null, 4, 1, 'testing', '2022-07-20', 'https://pngtree.com/so/happy', 'testing', 1);

        SELECT
        p.id post_id,
        t.id tag_id,
        t.label

        FROM Tags t
        JOIN PostTags pt
            ON t.id = pt.tag_id
        JOIN Posts p
            ON p.id = pt.post_id
        WHERE p.id = 28

