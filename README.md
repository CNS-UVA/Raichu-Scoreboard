# Raichu-Scoreboard

## Setup
Run the following command to set up Git hooks:
```sh
git config --local core.hooksPath .githooks/
```

## API Usage

## To discuss
- User creation flow: should `Team`s be created before any `User` objects, or should the `User` creation flow be allowed to create `Team`s?
- Rename `Credential.service` to `Credential.team_service`? Technically it's a `TeamService` object, but I'm not sure if the extra clarification is necessary.
- Should it be possible to have multiple `Credential`s with the same `TeamService`? Maybe if they change credentials or something...but maybe this should just edit the original object? We can handle this programmatically so maybe we don't need to do anything with the DB schema.
- The old scoreboard had an endpoint `/services` that seems to just display each team's status and its current status. However, our schema stores the status of services at a given point in time as `Score` objects. Should `/services` show `Score`s?