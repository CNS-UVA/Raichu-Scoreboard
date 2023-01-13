# Raichu-Scoreboard

## Setup
Run the following command to set up Git pre-commit hook:
```sh
git config --local core.hooksPath .githooks/
```

## API Usage

To work with the score bot, Raichu has two API endpoints: `/api/credentials` and `/api/scores`. Both endpoints require passing an authorization header in the format `Authorization: Token {TOKEN}`, where `{TOKEN}` can be retrieved by POSTing an account's username and password to `/api/get-token`. 

The credentials endpoint supports GET requests to retrieve a list of serialized JSON objects representing every `Credential` instance. Similarly, the score endpoint supports POST requests to create `Score` instances by deserializing JSON data.
## To discuss
- User creation flow: should `Team`s be created before any `User` objects, or should the `User` creation flow be allowed to create `Team`s?
- Rename `Credential.service` to `Credential.team_service`? Technically it's a `TeamService` object, but I'm not sure if the extra clarification is necessary.
- Should it be possible to have multiple `Credential`s with the same `TeamService`? Maybe if they change credentials or something...but maybe this should just edit the original object? We can handle this programmatically so maybe we don't need to do anything with the DB schema.
- The old scoreboard had an endpoint `/services` that seems to just display each team's status and its current status. However, our schema stores the status of services at a given point in time as `Score` objects. Should `/services` show `Score`s?