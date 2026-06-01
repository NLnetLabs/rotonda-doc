# Standard Library


## Types
```{toctree}
:maxdepth: 1
AsPath <AsPath/index>
Asn <Asn/index>
AsnRange <AsnRange/index>
BgpMsg <BgpMsg/index>
BmpMsg <BmpMsg/index>
Community <Community/index>
IngressInfo <IngressInfo/index>
IpAddr <IpAddr/index>
LargeCommunity <LargeCommunity/index>
List[T] <List[T]/index>
Log <Log/index>
LogEntry <LogEntry/index>
Metrics <Metrics/index>
Option[T] <Option[T]/index>
PathAttributes <PathAttributes/index>
Prefix <Prefix/index>
Route <Route/index>
RovStatus <RovStatus/index>
RovStatusUpdate <RovStatusUpdate/index>
Rpki <Rpki/index>
String <String/index>
StringBuf <StringBuf/index>
StringBytes <StringBytes/index>
StringChars <StringChars/index>
StringLines <StringLines/index>
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
## Functions
````{roto:function} command(cmd: String, args: List[String]) -> bool
Execute an external command.

The `args` list of arguments is passed to the command.
See also <https://doc.rust-lang.org/std/process/struct.Command.html#method.args>.
````

