# Current Feature


## This Document
This document relates to information specific to the current feature that is being designed and implemented.

## Feature Description
A new endpoint called /pronouns that returns the results as a JSON object following REST API guidlines and practices. This will also require a new DB table called pronouns which lists all of the pronouns in Castillian Spanish including an ID number the pronoun as a string.

## Guidelines

Example: `/practice`

This then calls the db to return the full list of pronouns.

The return payload should contain an object for each example that looks like:

```json
{
	"id": integer,
	"pronoun": string
}
```

