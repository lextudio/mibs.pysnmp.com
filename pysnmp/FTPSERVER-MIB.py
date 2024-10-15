# SNMP MIB module (FTPSERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FTPSERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:43 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FtpServer_ObjectIdentity = ObjectIdentity
ftpServer = _FtpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 2)
)
_FtpStatistics_ObjectIdentity = ObjectIdentity
ftpStatistics = _FtpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 2, 1)
)
_TotalBytesSentHighWord_Type = Counter32
_TotalBytesSentHighWord_Object = MibScalar
totalBytesSentHighWord = _TotalBytesSentHighWord_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 2, 1, 1),
    _TotalBytesSentHighWord_Type()
)
totalBytesSentHighWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBytesSentHighWord.setStatus("mandatory")
_TotalBytesSentLowWord_Type = Counter32
_TotalBytesSentLowWord_Object = MibScalar
totalBytesSentLowWord = _TotalBytesSentLowWord_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 2, 1, 2),
    _TotalBytesSentLowWord_Type()
)
totalBytesSentLowWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBytesSentLowWord.setStatus("mandatory")
_TotalBytesReceivedHighWord_Type = Counter32
_TotalBytesReceivedHighWord_Object = MibScalar
totalBytesReceivedHighWord = _TotalBytesReceivedHighWord_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 2, 1, 3),
    _TotalBytesReceivedHighWord_Type()
)
totalBytesReceivedHighWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBytesReceivedHighWord.setStatus("mandatory")
_TotalBytesReceivedLowWord_Type = Counter32
_TotalBytesReceivedLowWord_Object = MibScalar
totalBytesReceivedLowWord = _TotalBytesReceivedLowWord_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 2, 1, 4),
    _TotalBytesReceivedLowWord_Type()
)
totalBytesReceivedLowWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBytesReceivedLowWord.setStatus("mandatory")
_TotalFilesSent_Type = Counter32
_TotalFilesSent_Object = MibScalar
totalFilesSent = _TotalFilesSent_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 2, 1, 5),
    _TotalFilesSent_Type()
)
totalFilesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalFilesSent.setStatus("mandatory")
_TotalFilesReceived_Type = Counter32
_TotalFilesReceived_Object = MibScalar
totalFilesReceived = _TotalFilesReceived_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 2, 1, 6),
    _TotalFilesReceived_Type()
)
totalFilesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalFilesReceived.setStatus("mandatory")
_CurrentAnonymousUsers_Type = Integer32
_CurrentAnonymousUsers_Object = MibScalar
currentAnonymousUsers = _CurrentAnonymousUsers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 2, 1, 7),
    _CurrentAnonymousUsers_Type()
)
currentAnonymousUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAnonymousUsers.setStatus("mandatory")
_CurrentNonAnonymousUsers_Type = Integer32
_CurrentNonAnonymousUsers_Object = MibScalar
currentNonAnonymousUsers = _CurrentNonAnonymousUsers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 2, 1, 8),
    _CurrentNonAnonymousUsers_Type()
)
currentNonAnonymousUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentNonAnonymousUsers.setStatus("mandatory")
_TotalAnonymousUsers_Type = Counter32
_TotalAnonymousUsers_Object = MibScalar
totalAnonymousUsers = _TotalAnonymousUsers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 2, 1, 9),
    _TotalAnonymousUsers_Type()
)
totalAnonymousUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalAnonymousUsers.setStatus("mandatory")
_TotalNonAnonymousUsers_Type = Counter32
_TotalNonAnonymousUsers_Object = MibScalar
totalNonAnonymousUsers = _TotalNonAnonymousUsers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 2, 1, 10),
    _TotalNonAnonymousUsers_Type()
)
totalNonAnonymousUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalNonAnonymousUsers.setStatus("mandatory")
_MaxAnonymousUsers_Type = Counter32
_MaxAnonymousUsers_Object = MibScalar
maxAnonymousUsers = _MaxAnonymousUsers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 2, 1, 11),
    _MaxAnonymousUsers_Type()
)
maxAnonymousUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxAnonymousUsers.setStatus("mandatory")
_MaxNonAnonymousUsers_Type = Counter32
_MaxNonAnonymousUsers_Object = MibScalar
maxNonAnonymousUsers = _MaxNonAnonymousUsers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 2, 1, 12),
    _MaxNonAnonymousUsers_Type()
)
maxNonAnonymousUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNonAnonymousUsers.setStatus("mandatory")
_CurrentConnections_Type = Integer32
_CurrentConnections_Object = MibScalar
currentConnections = _CurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 2, 1, 13),
    _CurrentConnections_Type()
)
currentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentConnections.setStatus("mandatory")
_MaxConnections_Type = Counter32
_MaxConnections_Object = MibScalar
maxConnections = _MaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 2, 1, 14),
    _MaxConnections_Type()
)
maxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxConnections.setStatus("mandatory")
_ConnectionAttempts_Type = Counter32
_ConnectionAttempts_Object = MibScalar
connectionAttempts = _ConnectionAttempts_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 2, 1, 15),
    _ConnectionAttempts_Type()
)
connectionAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionAttempts.setStatus("mandatory")
_LogonAttempts_Type = Counter32
_LogonAttempts_Object = MibScalar
logonAttempts = _LogonAttempts_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 7, 2, 1, 16),
    _LogonAttempts_Type()
)
logonAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logonAttempts.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FTPSERVER-MIB",
    **{"ftpServer": ftpServer,
       "ftpStatistics": ftpStatistics,
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
       "logonAttempts": logonAttempts}
)
