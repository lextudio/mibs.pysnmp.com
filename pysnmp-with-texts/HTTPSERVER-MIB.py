"""SNMP MIB module (HTTPSERVER-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HTTPSERVER-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 11:12:14 2024
On host MacBook-Pro.local platform Darwin version 23.4.0 by user lextm
Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]
"""
if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(internetServer,) = mibBuilder.importSymbols(
    "INTERNETSERVER-MIB",
    "internetServer")

(NotificationGroup,
 ModuleCompliance) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "NotificationGroup",
    "ModuleCompliance")

(Counter32,
 ModuleIdentity,
 Bits,
 enterprises,
 Gauge32,
 Counter64,
 NotificationType,
 IpAddress,
 Unsigned32,
 TimeTicks,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 MibIdentifier,
 Integer32,
 ObjectIdentity,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Counter32",
    "ModuleIdentity",
    "Bits",
    "enterprises",
    "Gauge32",
    "Counter64",
    "NotificationType",
    "IpAddress",
    "Unsigned32",
    "TimeTicks",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "MibIdentifier",
    "Integer32",
    "ObjectIdentity",
    "iso")

(TextualConvention,
 DisplayString) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "TextualConvention",
    "DisplayString")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HttpServer_ObjectIdentity = ObjectIdentity
httpServer = _HttpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3)
)
_HttpStatistics_ObjectIdentity = ObjectIdentity
httpStatistics = _HttpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1)
)
_TotalBytesSentHighWord_Type = Counter32
_TotalBytesSentHighWord_Object = MibScalar
totalBytesSentHighWord = _TotalBytesSentHighWord_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 1),
    _TotalBytesSentHighWord_Type()
)
totalBytesSentHighWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBytesSentHighWord.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalBytesSentHighWord.setDescription("""\
This is the high 32-bits of the total number of of BYTEs sent by the HTTP
Server.
""")
_TotalBytesSentLowWord_Type = Counter32
_TotalBytesSentLowWord_Object = MibScalar
totalBytesSentLowWord = _TotalBytesSentLowWord_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 2),
    _TotalBytesSentLowWord_Type()
)
totalBytesSentLowWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBytesSentLowWord.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalBytesSentLowWord.setDescription("""\
This is the low 32-bits of the total number of of BYTEs sent by the HTTP
Server.
""")
_TotalBytesReceivedHighWord_Type = Counter32
_TotalBytesReceivedHighWord_Object = MibScalar
totalBytesReceivedHighWord = _TotalBytesReceivedHighWord_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 3),
    _TotalBytesReceivedHighWord_Type()
)
totalBytesReceivedHighWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBytesReceivedHighWord.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalBytesReceivedHighWord.setDescription("""\
This is the high 32-bits of the total number of of BYTEs received by the HTTP
Server.
""")
_TotalBytesReceivedLowWord_Type = Counter32
_TotalBytesReceivedLowWord_Object = MibScalar
totalBytesReceivedLowWord = _TotalBytesReceivedLowWord_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 4),
    _TotalBytesReceivedLowWord_Type()
)
totalBytesReceivedLowWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBytesReceivedLowWord.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalBytesReceivedLowWord.setDescription("""\
This is the low 32-bits of the total number of of BYTEs received by the HTTP
Server.
""")
_TotalFilesSent_Type = Counter32
_TotalFilesSent_Object = MibScalar
totalFilesSent = _TotalFilesSent_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 5),
    _TotalFilesSent_Type()
)
totalFilesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalFilesSent.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalFilesSent.setDescription("""\
This is the total number of files sent by this HTTP Server.
""")
_TotalFilesReceived_Type = Counter32
_TotalFilesReceived_Object = MibScalar
totalFilesReceived = _TotalFilesReceived_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 6),
    _TotalFilesReceived_Type()
)
totalFilesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalFilesReceived.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalFilesReceived.setDescription("""\
This is the total number of files received by this HTTP Server.
""")
_CurrentAnonymousUsers_Type = Counter32
_CurrentAnonymousUsers_Object = MibScalar
currentAnonymousUsers = _CurrentAnonymousUsers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 7),
    _CurrentAnonymousUsers_Type()
)
currentAnonymousUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAnonymousUsers.setStatus("mandatory")
if mibBuilder.loadTexts:
    currentAnonymousUsers.setDescription("""\
This is the number of anonymous users currently connected to the HTTP Server.
""")
_CurrentNonAnonymousUsers_Type = Counter32
_CurrentNonAnonymousUsers_Object = MibScalar
currentNonAnonymousUsers = _CurrentNonAnonymousUsers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 8),
    _CurrentNonAnonymousUsers_Type()
)
currentNonAnonymousUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentNonAnonymousUsers.setStatus("mandatory")
if mibBuilder.loadTexts:
    currentNonAnonymousUsers.setDescription("""\
This is the number of nonanonymous users currently connected to the HTTP
Server.
""")
_TotalAnonymousUsers_Type = Counter32
_TotalAnonymousUsers_Object = MibScalar
totalAnonymousUsers = _TotalAnonymousUsers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 9),
    _TotalAnonymousUsers_Type()
)
totalAnonymousUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalAnonymousUsers.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalAnonymousUsers.setDescription("""\
This is the total number of anonymous users that have ever connected to the
HTTP Server.
""")
_TotalNonAnonymousUsers_Type = Counter32
_TotalNonAnonymousUsers_Object = MibScalar
totalNonAnonymousUsers = _TotalNonAnonymousUsers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 10),
    _TotalNonAnonymousUsers_Type()
)
totalNonAnonymousUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalNonAnonymousUsers.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalNonAnonymousUsers.setDescription("""\
This is the total number of nonanonymous users that have ever connected to the
HTTP Server.
""")
_MaxAnonymousUsers_Type = Counter32
_MaxAnonymousUsers_Object = MibScalar
maxAnonymousUsers = _MaxAnonymousUsers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 11),
    _MaxAnonymousUsers_Type()
)
maxAnonymousUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxAnonymousUsers.setStatus("mandatory")
if mibBuilder.loadTexts:
    maxAnonymousUsers.setDescription("""\
This is the maximum number of anonymous users simultaneously connected to the
HTTP Server.
""")
_MaxNonAnonymousUsers_Type = Counter32
_MaxNonAnonymousUsers_Object = MibScalar
maxNonAnonymousUsers = _MaxNonAnonymousUsers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 12),
    _MaxNonAnonymousUsers_Type()
)
maxNonAnonymousUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNonAnonymousUsers.setStatus("mandatory")
if mibBuilder.loadTexts:
    maxNonAnonymousUsers.setDescription("""\
This is the maximum number of nonanonymous users simultaneously connected to
the HTTP Server.
""")
_CurrentConnections_Type = Integer32
_CurrentConnections_Object = MibScalar
currentConnections = _CurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 13),
    _CurrentConnections_Type()
)
currentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentConnections.setStatus("mandatory")
if mibBuilder.loadTexts:
    currentConnections.setDescription("""\
This is the current number of connections to the HTTP Server.
""")
_MaxConnections_Type = Counter32
_MaxConnections_Object = MibScalar
maxConnections = _MaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 14),
    _MaxConnections_Type()
)
maxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxConnections.setStatus("mandatory")
if mibBuilder.loadTexts:
    maxConnections.setDescription("""\
This is the maximum number of simultaneous connections to the HTTP Server.
""")
_ConnectionAttempts_Type = Counter32
_ConnectionAttempts_Object = MibScalar
connectionAttempts = _ConnectionAttempts_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 15),
    _ConnectionAttempts_Type()
)
connectionAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionAttempts.setStatus("mandatory")
if mibBuilder.loadTexts:
    connectionAttempts.setDescription("""\
This is the number of connection attempts that have been made to the HTTP
Server.
""")
_LogonAttempts_Type = Counter32
_LogonAttempts_Object = MibScalar
logonAttempts = _LogonAttempts_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 16),
    _LogonAttempts_Type()
)
logonAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logonAttempts.setStatus("mandatory")
if mibBuilder.loadTexts:
    logonAttempts.setDescription("""\
This is the number of logon attempts that have been made to this HTTP Server.
""")
_TotalOptions_Type = Counter32
_TotalOptions_Object = MibScalar
totalOptions = _TotalOptions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 17),
    _TotalOptions_Type()
)
totalOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalOptions.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalOptions.setDescription("""\
This is the number of requests using the OPTIONS method that have been made to
this HTTP Server.
""")
_TotalGets_Type = Counter32
_TotalGets_Object = MibScalar
totalGets = _TotalGets_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 18),
    _TotalGets_Type()
)
totalGets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalGets.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalGets.setDescription("""\
This is the number of requests using the GET method that have been made to this
HTTP Server.
""")
_TotalPosts_Type = Counter32
_TotalPosts_Object = MibScalar
totalPosts = _TotalPosts_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 19),
    _TotalPosts_Type()
)
totalPosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalPosts.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalPosts.setDescription("""\
This is the number of requests using the POST method that have been made to
this HTTP Server.
""")
_TotalHeads_Type = Counter32
_TotalHeads_Object = MibScalar
totalHeads = _TotalHeads_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 20),
    _TotalHeads_Type()
)
totalHeads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalHeads.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalHeads.setDescription("""\
This is the number of requests using the HEAD method that have been made to
this HTTP Server.
""")
_TotalPuts_Type = Counter32
_TotalPuts_Object = MibScalar
totalPuts = _TotalPuts_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 21),
    _TotalPuts_Type()
)
totalPuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalPuts.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalPuts.setDescription("""\
This is the number of requests using the PUT method that have been made to this
HTTP Server.
""")
_TotalDeletes_Type = Counter32
_TotalDeletes_Object = MibScalar
totalDeletes = _TotalDeletes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 22),
    _TotalDeletes_Type()
)
totalDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalDeletes.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalDeletes.setDescription("""\
This is the number of requests using the DELETE method that have been made to
this HTTP Server.
""")
_TotalTraces_Type = Counter32
_TotalTraces_Object = MibScalar
totalTraces = _TotalTraces_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 23),
    _TotalTraces_Type()
)
totalTraces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalTraces.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalTraces.setDescription("""\
This is the number of requests using the TRACE method that have been made to
this HTTP Server.
""")
_TotalMove_Type = Counter32
_TotalMove_Object = MibScalar
totalMove = _TotalMove_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 24),
    _TotalMove_Type()
)
totalMove.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalMove.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalMove.setDescription("""\
This is the number of requests using the MOVE method that have been made to
this HTTP Server.
""")
_TotalCopy_Type = Counter32
_TotalCopy_Object = MibScalar
totalCopy = _TotalCopy_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 25),
    _TotalCopy_Type()
)
totalCopy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalCopy.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalCopy.setDescription("""\
This is the number of requests using the COPY method that have been made to
this HTTP Server.
""")
_TotalMkcol_Type = Counter32
_TotalMkcol_Object = MibScalar
totalMkcol = _TotalMkcol_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 26),
    _TotalMkcol_Type()
)
totalMkcol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalMkcol.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalMkcol.setDescription("""\
This is the number of requests using the MKCOL method that have been made to
this HTTP Server.
""")
_TotalPropfind_Type = Counter32
_TotalPropfind_Object = MibScalar
totalPropfind = _TotalPropfind_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 27),
    _TotalPropfind_Type()
)
totalPropfind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalPropfind.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalPropfind.setDescription("""\
This is the number of requests using the PROPFIND method that have been made to
this HTTP Server.
""")
_TotalProppatch_Type = Counter32
_TotalProppatch_Object = MibScalar
totalProppatch = _TotalProppatch_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 28),
    _TotalProppatch_Type()
)
totalProppatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalProppatch.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalProppatch.setDescription("""\
This is the number of requests using the PROPPATCH method that have been made
to this HTTP Server.
""")
_TotalSearch_Type = Counter32
_TotalSearch_Object = MibScalar
totalSearch = _TotalSearch_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 29),
    _TotalSearch_Type()
)
totalSearch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalSearch.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalSearch.setDescription("""\
This is the number of requests using the MS-SEARCH method that have been made
to this HTTP Server.
""")
_TotalLock_Type = Counter32
_TotalLock_Object = MibScalar
totalLock = _TotalLock_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 30),
    _TotalLock_Type()
)
totalLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalLock.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalLock.setDescription("""\
This is the number of requests using the LOCK method that have been made to
this HTTP Server.
""")
_TotalUnlock_Type = Counter32
_TotalUnlock_Object = MibScalar
totalUnlock = _TotalUnlock_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 31),
    _TotalUnlock_Type()
)
totalUnlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalUnlock.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalUnlock.setDescription("""\
This is the number of requests using the UNLOCK method that have been made to
this HTTP Server.
""")
_TotalOthers_Type = Counter32
_TotalOthers_Object = MibScalar
totalOthers = _TotalOthers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 32),
    _TotalOthers_Type()
)
totalOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalOthers.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalOthers.setDescription("""\
This is the number of requests not using the OPTIONS, GET, HEAD POST, PUT,
DELETE, TRACE, MOVE, COPY, MKCOL, PROPFIND, PROPPATCH, MS-SEARCH, LOCK or
UNLOCK method that have been made to this HTTP Server. This may include LINK or
other methods supported by gateway applications.
""")
_CurrentCGIRequests_Type = Counter32
_CurrentCGIRequests_Object = MibScalar
currentCGIRequests = _CurrentCGIRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 33),
    _CurrentCGIRequests_Type()
)
currentCGIRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentCGIRequests.setStatus("mandatory")
if mibBuilder.loadTexts:
    currentCGIRequests.setDescription("""\
This is the number of Common Gateway Interface (CGI) requests that are
currently being serviced by this HTTP Server.
""")
_CurrentBGIRequests_Type = Counter32
_CurrentBGIRequests_Object = MibScalar
currentBGIRequests = _CurrentBGIRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 34),
    _CurrentBGIRequests_Type()
)
currentBGIRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentBGIRequests.setStatus("mandatory")
if mibBuilder.loadTexts:
    currentBGIRequests.setDescription("""\
This is the number of Binary Gateway Interface (BGI) requests that are
currently being serviced by this HTTP Server.
""")
_TotalCGIRequests_Type = Counter32
_TotalCGIRequests_Object = MibScalar
totalCGIRequests = _TotalCGIRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 35),
    _TotalCGIRequests_Type()
)
totalCGIRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalCGIRequests.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalCGIRequests.setDescription("""\
This is the number of Common Gateway Interface (CGI) requests that have been
made to this HTTP Server.
""")
_TotalBGIRequests_Type = Counter32
_TotalBGIRequests_Object = MibScalar
totalBGIRequests = _TotalBGIRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 36),
    _TotalBGIRequests_Type()
)
totalBGIRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBGIRequests.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalBGIRequests.setDescription("""\
This is the number of Binary Gateway Interface (BGI) requests that have been
made to this HTTP Server.
""")
_MaxCGIRequests_Type = Counter32
_MaxCGIRequests_Object = MibScalar
maxCGIRequests = _MaxCGIRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 37),
    _MaxCGIRequests_Type()
)
maxCGIRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxCGIRequests.setStatus("mandatory")
if mibBuilder.loadTexts:
    maxCGIRequests.setDescription("""\
This is the maximum number of Common Gateway Interface (CGI) requests
simultaneous processed by this HTTP Server.
""")
_MaxBGIRequests_Type = Counter32
_MaxBGIRequests_Object = MibScalar
maxBGIRequests = _MaxBGIRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 38),
    _MaxBGIRequests_Type()
)
maxBGIRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxBGIRequests.setStatus("mandatory")
if mibBuilder.loadTexts:
    maxBGIRequests.setDescription("""\
This is the maximum number of Binary Gateway Interface (BGI) requests
simultaneous processed by this HTTP Server.
""")
_CurrentBlockedRequests_Type = Counter32
_CurrentBlockedRequests_Object = MibScalar
currentBlockedRequests = _CurrentBlockedRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 39),
    _CurrentBlockedRequests_Type()
)
currentBlockedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentBlockedRequests.setStatus("mandatory")
if mibBuilder.loadTexts:
    currentBlockedRequests.setDescription("""\
This is the current number of requests that have been temporarily blocked by
this HTTP Server due to bandwidth throttling settings.
""")
_TotalBlockedRequests_Type = Counter32
_TotalBlockedRequests_Object = MibScalar
totalBlockedRequests = _TotalBlockedRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 40),
    _TotalBlockedRequests_Type()
)
totalBlockedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBlockedRequests.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalBlockedRequests.setDescription("""\
This is the total number of requests that have been temporarily blocked by this
HTTP Server due to bandwidth throttling settings.
""")
_TotalAllowedRequests_Type = Counter32
_TotalAllowedRequests_Object = MibScalar
totalAllowedRequests = _TotalAllowedRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 41),
    _TotalAllowedRequests_Type()
)
totalAllowedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalAllowedRequests.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalAllowedRequests.setDescription("""\
This is the total number of requests that have been allowed by the bandwidth
throttling settings on this HTTP Server.
""")
_TotalRejectedRequests_Type = Counter32
_TotalRejectedRequests_Object = MibScalar
totalRejectedRequests = _TotalRejectedRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 42),
    _TotalRejectedRequests_Type()
)
totalRejectedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalRejectedRequests.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalRejectedRequests.setDescription("""\
This is the total number of requests that have been rejected by this HTTP
Server due to bandwidth throttling settings.
""")
_TotalNotFoundErrors_Type = Counter32
_TotalNotFoundErrors_Object = MibScalar
totalNotFoundErrors = _TotalNotFoundErrors_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 43),
    _TotalNotFoundErrors_Type()
)
totalNotFoundErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalNotFoundErrors.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalNotFoundErrors.setDescription("""\
This is the total number of requests the HTTP server could not satisfy because
the requested resource could not be found.
""")
_TotalLockedErrors_Type = Counter32
_TotalLockedErrors_Object = MibScalar
totalLockedErrors = _TotalLockedErrors_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 44),
    _TotalLockedErrors_Type()
)
totalLockedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalLockedErrors.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalLockedErrors.setDescription("""\
This is the total number of requests the HTTP server could not satisfy because
the requested resource was locked.
""")
_MeasuredBandwidth_Type = Counter32
_MeasuredBandwidth_Object = MibScalar
measuredBandwidth = _MeasuredBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 45),
    _MeasuredBandwidth_Type()
)
measuredBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measuredBandwidth.setStatus("mandatory")
if mibBuilder.loadTexts:
    measuredBandwidth.setDescription("""\
This is the I/O bandwidth used by this HTTP Server, averaged over a minute.
""")
_CurrentCALsforAuthenticatedUsers_Type = Counter32
_CurrentCALsforAuthenticatedUsers_Object = MibScalar
currentCALsforAuthenticatedUsers = _CurrentCALsforAuthenticatedUsers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 46),
    _CurrentCALsforAuthenticatedUsers_Type()
)
currentCALsforAuthenticatedUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentCALsforAuthenticatedUsers.setStatus("mandatory")
if mibBuilder.loadTexts:
    currentCALsforAuthenticatedUsers.setDescription("""\
This is the current count of Client Access Licenses (CALs) available to this
HTTP Server for simultaneous use by authenticated users.
""")
_MaxCALsforAuthenticatedUsers_Type = Counter32
_MaxCALsforAuthenticatedUsers_Object = MibScalar
maxCALsforAuthenticatedUsers = _MaxCALsforAuthenticatedUsers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 47),
    _MaxCALsforAuthenticatedUsers_Type()
)
maxCALsforAuthenticatedUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxCALsforAuthenticatedUsers.setStatus("mandatory")
if mibBuilder.loadTexts:
    maxCALsforAuthenticatedUsers.setDescription("""\
This is the maximum count of Client Access Licenses (CALs) used by this HTTP
Server for simultaneous use by authenticated users.
""")
_TotalCALFailedAuthenticatedUser_Type = Counter32
_TotalCALFailedAuthenticatedUser_Object = MibScalar
totalCALFailedAuthenticatedUser = _TotalCALFailedAuthenticatedUser_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 48),
    _TotalCALFailedAuthenticatedUser_Type()
)
totalCALFailedAuthenticatedUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalCALFailedAuthenticatedUser.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalCALFailedAuthenticatedUser.setDescription("""\
This is the total number of HTTP requests that have failed on this HTTP server
due to a Client Access License (CAL) being unavailable for an authenticated
user.
""")
_CurrentCALsforSecureConnections_Type = Counter32
_CurrentCALsforSecureConnections_Object = MibScalar
currentCALsforSecureConnections = _CurrentCALsforSecureConnections_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 49),
    _CurrentCALsforSecureConnections_Type()
)
currentCALsforSecureConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentCALsforSecureConnections.setStatus("mandatory")
if mibBuilder.loadTexts:
    currentCALsforSecureConnections.setDescription("""\
This is the current count of Client Access Licenses (CALs) available to this
HTTP Server for simultaneous use by secure connections.
""")
_MaxCALsforSecureConnections_Type = Counter32
_MaxCALsforSecureConnections_Object = MibScalar
maxCALsforSecureConnections = _MaxCALsforSecureConnections_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 50),
    _MaxCALsforSecureConnections_Type()
)
maxCALsforSecureConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxCALsforSecureConnections.setStatus("mandatory")
if mibBuilder.loadTexts:
    maxCALsforSecureConnections.setDescription("""\
This is the maximum count of Client Access Licenses (CALs) available to this
Http Server for simultaneous use by secure connections.
""")
_TotalCALFailedSecureConnection_Type = Counter32
_TotalCALFailedSecureConnection_Object = MibScalar
totalCALFailedSecureConnection = _TotalCALFailedSecureConnection_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 3, 1, 51),
    _TotalCALFailedSecureConnection_Type()
)
totalCALFailedSecureConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalCALFailedSecureConnection.setStatus("mandatory")
if mibBuilder.loadTexts:
    totalCALFailedSecureConnection.setDescription("""\
This is the total number of HTTP requests that have failed on this HTTP server
due to a Client Access License (CAL) being unavailable for use by a secure
connection.
""")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HTTPSERVER-MIB",
    **{"httpServer": httpServer,
       "httpStatistics": httpStatistics,
       "totalBytesSentHighWord": totalBytesSentHighWord,
       "totalBytesSentLowWord": totalBytesSentLowWord,
       "totalBytesReceivedHighWord": totalBytesReceivedHighWord,
       "totalBytesReceivedLowWord": totalBytesReceivedLowWord,
       "totalFilesSent": totalFilesSent,
       "totalFilesReceived": totalFilesReceived,
       "currentAnonymousUsers": currentAnonymousUsers,
       "currentNonAnonymousUsers": currentNonAnonymousUsers,
       "totalAnonymousUsers": totalAnonymousUsers,
       "totalNonAnonymousUsers": totalNonAnonymousUsers,
       "maxAnonymousUsers": maxAnonymousUsers,
       "maxNonAnonymousUsers": maxNonAnonymousUsers,
       "currentConnections": currentConnections,
       "maxConnections": maxConnections,
       "connectionAttempts": connectionAttempts,
       "logonAttempts": logonAttempts,
       "totalOptions": totalOptions,
       "totalGets": totalGets,
       "totalPosts": totalPosts,
       "totalHeads": totalHeads,
       "totalPuts": totalPuts,
       "totalDeletes": totalDeletes,
       "totalTraces": totalTraces,
       "totalMove": totalMove,
       "totalCopy": totalCopy,
       "totalMkcol": totalMkcol,
       "totalPropfind": totalPropfind,
       "totalProppatch": totalProppatch,
       "totalSearch": totalSearch,
       "totalLock": totalLock,
       "totalUnlock": totalUnlock,
       "totalOthers": totalOthers,
       "currentCGIRequests": currentCGIRequests,
       "currentBGIRequests": currentBGIRequests,
       "totalCGIRequests": totalCGIRequests,
       "totalBGIRequests": totalBGIRequests,
       "maxCGIRequests": maxCGIRequests,
       "maxBGIRequests": maxBGIRequests,
       "currentBlockedRequests": currentBlockedRequests,
       "totalBlockedRequests": totalBlockedRequests,
       "totalAllowedRequests": totalAllowedRequests,
       "totalRejectedRequests": totalRejectedRequests,
       "totalNotFoundErrors": totalNotFoundErrors,
       "totalLockedErrors": totalLockedErrors,
       "measuredBandwidth": measuredBandwidth,
       "currentCALsforAuthenticatedUsers": currentCALsforAuthenticatedUsers,
       "maxCALsforAuthenticatedUsers": maxCALsforAuthenticatedUsers,
       "totalCALFailedAuthenticatedUser": totalCALFailedAuthenticatedUser,
       "currentCALsforSecureConnections": currentCALsforSecureConnections,
       "maxCALsforSecureConnections": maxCALsforSecureConnections,
       "totalCALFailedSecureConnection": totalCALFailedSecureConnection}
)
