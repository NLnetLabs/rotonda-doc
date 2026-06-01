# RovStatus
`````{roto:type} RovStatus
ROV status of a `Route`.
`````


````{roto:function} is_invalid(status: RovStatus) -> bool
Returns 'true' if the status is 'Invalid'.
````

````{roto:function} is_not_found(status: RovStatus) -> bool
Returns 'true' if the status is 'NotFound'.
````

````{roto:function} is_valid(status: RovStatus) -> bool
Returns 'true' if the status is 'Valid'.
````

````{roto:function} to_string(status: RovStatus) -> String
Return the string representation.
````

