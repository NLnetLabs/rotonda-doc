# Standard Library


## Types
```{toctree}
:maxdepth: 1
AsPath <AsPath/index>
Asn <Asn/index>
AsnLists <AsnLists/index>
BgpMsg <BgpMsg/index>
BmpMsg <BmpMsg/index>
Community <Community/index>
IngressInfo <IngressInfo/index>
InsertionInfo <InsertionInfo/index>
IpAddr <IpAddr/index>
LargeCommunity <LargeCommunity/index>
List[T] <List[T]/index>
Log <Log/index>
LogEntry <LogEntry/index>
Metrics <Metrics/index>
Option[T] <Option[T]/index>
OriginAsn <OriginAsn/index>
PathAttributes <PathAttributes/index>
PerPeerHeader <PerPeerHeader/index>
Prefix <Prefix/index>
PrefixLists <PrefixLists/index>
Route <Route/index>
RovStatus <RovStatus/index>
RovStatusUpdate <RovStatusUpdate/index>
Rpki <Rpki/index>
String <String/index>
StringBuf <StringBuf/index>
Verdict[A, R] <Verdict[A, R]/index>
VrpUpdate <VrpUpdate/index>
bool <bool/index>
char <char/index>
f32 <f32/index>
f64 <f64/index>
i16 <i16/index>
i32 <i32/index>
i64 <i64/index>
i8 <i8/index>
u16 <u16/index>
u32 <u32/index>
u64 <u64/index>
u8 <u8/index>
```
## Constants
`````{roto:constant} NO_ADVERTISE: Community
The well-known NO_ADVERTISE community (RFC1997)
`````

`````{roto:constant} NO_EXPORT: Community
The well-known NO_EXPORT community (RFC1997)
`````

`````{roto:constant} NO_EXPORT_SUBCONFED: Community
The well-known NO_EXPORT_SUBCONFED community (RFC1997)
`````

`````{roto:constant} NO_PEER: Community
The well-known NO_PEER community (RFC1997)
`````

## Functions
````{roto:function} fmt_asn(asn: Asn) -> String
````

