# Raichu-Scoreboard

## To discuss
- User creation flow: should `Team`s be created before any `User` objects, or should the `User` creation flow be allowed to create `Team`s?
- Rename `Credential.service` to `Credential.team_service`? Technically it's a `TeamService` object, but I'm not sure if the extra clarification is necessary.
- Should it be possible to have multiple `Credential`s with the same `TeamService`? Maybe if they change credentials or something...but maybe this should just edit the original object? We can handle this programmatically so maybe we don't need to do anything with the DB schema.