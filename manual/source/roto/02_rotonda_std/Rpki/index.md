# Rpki
`````{roto:type} Rpki
RPKI information retrieved via RTR.
`````


````{roto:function} check_rov(rpki: Rpki, rr: Route) -> RovStatus
Perform Route Origin Validation on the route.

This sets the 'rpki_info' for this Route to Valid, Invalid or
NotFound (RFC6811).

In order for this method to have effect, a 'rtr-in' connector
should be configured, and it should have received VRP data
from the connected RP software.
````

