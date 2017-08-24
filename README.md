# ipad-dev

If you need to make changes, this is how you deploy them:
1. Get [apex](https://github.com/apex/apex)
`curl https://raw.githubusercontent.com/apex/apex/master/install.sh | sh`
or
`curl https://raw.githubusercontent.com/apex/apex/master/install.sh | sudo sh` if needed

1. Configure AWS auth:
`aws configure`

1. Deploy
`apex deploy`


Deploy will figure out what has changed since the last deploy and update the appropriate functions in lambda.
