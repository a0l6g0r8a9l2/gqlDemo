# gqlDemo
Демонстрационное приложение о технологии GraphQL
## Overview
[Презентация о GraphQL](https://docs.google.com/presentation/d/1tU2jzV5u2vdLhKcWYWG-EJOjNSYN1DPb8MFXrX7YWmM/edit?usp=sharing)
## Buid image 
> docker run --name demo -d -p 8000:8000 demo-graphql-app
## Run container 
> docker build -t demo-graphql-app .
## GraphiQl (playground)
[demo on vscale](http://79.143.29.162:8000/) или запустите локально (инструкции выше) на localhost:8000
### Create users
> mutation {
  createUser(email: "JonSnow@mail.ru", password: "JonPass", name: "Jon Snow") {
    user {
      id
      name
      email
    }
  }
}
> mutation {
  createUser(email: "DaenerysTargaryen@mail.ru", password: "DaenerysPass", name: "Daenerys Targaryen") {
    user {
      id
      name
      email
    }
  }
}

### Query user
> {
  user(id: 1) {
    name
    posts{
      title,
      date
    }
    followers(last: 3){
      name
    }
  }
}
### Create post
> mutation {
  createPost(content: "content from Jon Snow", title: "Jon Snow 1st post", postedBy: 1) {
    post {
      postId
      title
      content
      date
      author {
        id
        name
      }
    }
  }
}
### FollowUp user
> mutation {
  followUp(followUpId: 1, userId: 2) {
    ok
  }
}
