# SNMP MIB module (ALTIGA-TELNET-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-TELNET-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:25 2024
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

(alTelnetMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alTelnetMibModule")

(alStatsTelnet,
 alTelnetGroup) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alStatsTelnet",
    "alTelnetGroup")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

altigaTelnetStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 16, 2)
)
altigaTelnetStatsMibModule.setRevisions(
        ("2002-09-05 13:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaTelnetStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaTelnetStatsMibConformance = _AltigaTelnetStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 16, 2, 1)
)
_AltigaTelnetStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaTelnetStatsMibCompliances = _AltigaTelnetStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 16, 2, 1, 1)
)
_AlStatsTelnetGlobal_ObjectIdentity = ObjectIdentity
alStatsTelnetGlobal = _AlStatsTelnetGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 1)
)
_AlTelnetStatsActiveSessions_Type = Gauge32
_AlTelnetStatsActiveSessions_Object = MibScalar
alTelnetStatsActiveSessions = _AlTelnetStatsActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 1, 1),
    _AlTelnetStatsActiveSessions_Type()
)
alTelnetStatsActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsActiveSessions.setStatus("current")
_AlTelnetStatsAttemptedSessions_Type = Counter32
_AlTelnetStatsAttemptedSessions_Object = MibScalar
alTelnetStatsAttemptedSessions = _AlTelnetStatsAttemptedSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 1, 2),
    _AlTelnetStatsAttemptedSessions_Type()
)
alTelnetStatsAttemptedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsAttemptedSessions.setStatus("current")
_AlTelnetStatsSuccessfulSessions_Type = Counter32
_AlTelnetStatsSuccessfulSessions_Object = MibScalar
alTelnetStatsSuccessfulSessions = _AlTelnetStatsSuccessfulSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 1, 3),
    _AlTelnetStatsSuccessfulSessions_Type()
)
alTelnetStatsSuccessfulSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsSuccessfulSessions.setStatus("current")
_AlTelnetStatsInNetPackets_Type = Counter32
_AlTelnetStatsInNetPackets_Object = MibScalar
alTelnetStatsInNetPackets = _AlTelnetStatsInNetPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 1, 4),
    _AlTelnetStatsInNetPackets_Type()
)
alTelnetStatsInNetPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsInNetPackets.setStatus("current")
_AlTelnetStatsInNetOctets_Type = Counter32
_AlTelnetStatsInNetOctets_Object = MibScalar
alTelnetStatsInNetOctets = _AlTelnetStatsInNetOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 1, 5),
    _AlTelnetStatsInNetOctets_Type()
)
alTelnetStatsInNetOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsInNetOctets.setStatus("current")
_AlTelnetStatsInNetCmdOctets_Type = Counter32
_AlTelnetStatsInNetCmdOctets_Object = MibScalar
alTelnetStatsInNetCmdOctets = _AlTelnetStatsInNetCmdOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 1, 6),
    _AlTelnetStatsInNetCmdOctets_Type()
)
alTelnetStatsInNetCmdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsInNetCmdOctets.setStatus("current")
_AlTelnetStatsInNetDropPackets_Type = Counter32
_AlTelnetStatsInNetDropPackets_Object = MibScalar
alTelnetStatsInNetDropPackets = _AlTelnetStatsInNetDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 1, 7),
    _AlTelnetStatsInNetDropPackets_Type()
)
alTelnetStatsInNetDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsInNetDropPackets.setStatus("current")
_AlTelnetStatsInNetDropOctets_Type = Counter32
_AlTelnetStatsInNetDropOctets_Object = MibScalar
alTelnetStatsInNetDropOctets = _AlTelnetStatsInNetDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 1, 8),
    _AlTelnetStatsInNetDropOctets_Type()
)
alTelnetStatsInNetDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsInNetDropOctets.setStatus("current")
_AlTelnetStatsOutNetPackets_Type = Counter32
_AlTelnetStatsOutNetPackets_Object = MibScalar
alTelnetStatsOutNetPackets = _AlTelnetStatsOutNetPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 1, 9),
    _AlTelnetStatsOutNetPackets_Type()
)
alTelnetStatsOutNetPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsOutNetPackets.setStatus("current")
_AlTelnetStatsOutNetOctets_Type = Counter32
_AlTelnetStatsOutNetOctets_Object = MibScalar
alTelnetStatsOutNetOctets = _AlTelnetStatsOutNetOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 1, 10),
    _AlTelnetStatsOutNetOctets_Type()
)
alTelnetStatsOutNetOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsOutNetOctets.setStatus("current")
_AlTelnetStatsOutNetDropPackets_Type = Counter32
_AlTelnetStatsOutNetDropPackets_Object = MibScalar
alTelnetStatsOutNetDropPackets = _AlTelnetStatsOutNetDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 1, 11),
    _AlTelnetStatsOutNetDropPackets_Type()
)
alTelnetStatsOutNetDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsOutNetDropPackets.setStatus("current")
_AlTelnetStatsOutNetDropOctets_Type = Counter32
_AlTelnetStatsOutNetDropOctets_Object = MibScalar
alTelnetStatsOutNetDropOctets = _AlTelnetStatsOutNetDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 1, 12),
    _AlTelnetStatsOutNetDropOctets_Type()
)
alTelnetStatsOutNetDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsOutNetDropOctets.setStatus("current")
_AlTelnetStatsInShPackets_Type = Counter32
_AlTelnetStatsInShPackets_Object = MibScalar
alTelnetStatsInShPackets = _AlTelnetStatsInShPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 1, 13),
    _AlTelnetStatsInShPackets_Type()
)
alTelnetStatsInShPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsInShPackets.setStatus("current")
_AlTelnetStatsInShOctets_Type = Counter32
_AlTelnetStatsInShOctets_Object = MibScalar
alTelnetStatsInShOctets = _AlTelnetStatsInShOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 1, 14),
    _AlTelnetStatsInShOctets_Type()
)
alTelnetStatsInShOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsInShOctets.setStatus("current")
_AlTelnetStatsInShDropPackets_Type = Counter32
_AlTelnetStatsInShDropPackets_Object = MibScalar
alTelnetStatsInShDropPackets = _AlTelnetStatsInShDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 1, 15),
    _AlTelnetStatsInShDropPackets_Type()
)
alTelnetStatsInShDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsInShDropPackets.setStatus("current")
_AlTelnetStatsInShDropOctets_Type = Counter32
_AlTelnetStatsInShDropOctets_Object = MibScalar
alTelnetStatsInShDropOctets = _AlTelnetStatsInShDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 1, 16),
    _AlTelnetStatsInShDropOctets_Type()
)
alTelnetStatsInShDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsInShDropOctets.setStatus("current")
_AlTelnetStatsOutShPackets_Type = Counter32
_AlTelnetStatsOutShPackets_Object = MibScalar
alTelnetStatsOutShPackets = _AlTelnetStatsOutShPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 1, 17),
    _AlTelnetStatsOutShPackets_Type()
)
alTelnetStatsOutShPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsOutShPackets.setStatus("current")
_AlTelnetStatsOutShOctets_Type = Counter32
_AlTelnetStatsOutShOctets_Object = MibScalar
alTelnetStatsOutShOctets = _AlTelnetStatsOutShOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 1, 18),
    _AlTelnetStatsOutShOctets_Type()
)
alTelnetStatsOutShOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsOutShOctets.setStatus("current")
_AlTelnetStatsOutShDropPackets_Type = Counter32
_AlTelnetStatsOutShDropPackets_Object = MibScalar
alTelnetStatsOutShDropPackets = _AlTelnetStatsOutShDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 1, 19),
    _AlTelnetStatsOutShDropPackets_Type()
)
alTelnetStatsOutShDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsOutShDropPackets.setStatus("current")
_AlTelnetStatsOutShDropOctets_Type = Counter32
_AlTelnetStatsOutShDropOctets_Object = MibScalar
alTelnetStatsOutShDropOctets = _AlTelnetStatsOutShDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 1, 20),
    _AlTelnetStatsOutShDropOctets_Type()
)
alTelnetStatsOutShDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsOutShDropOctets.setStatus("current")
_AlTelnetStatsSessionTable_Object = MibTable
alTelnetStatsSessionTable = _AlTelnetStatsSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 2)
)
if mibBuilder.loadTexts:
    alTelnetStatsSessionTable.setStatus("current")
_AlTelnetStatsSessionEntry_Object = MibTableRow
alTelnetStatsSessionEntry = _AlTelnetStatsSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 2, 1)
)
alTelnetStatsSessionEntry.setIndexNames(
    (0, "ALTIGA-TELNET-STATS-MIB", "alTelnetStatsSessionId"),
)
if mibBuilder.loadTexts:
    alTelnetStatsSessionEntry.setStatus("current")
_AlTelnetStatsSessionRowStatus_Type = RowStatus
_AlTelnetStatsSessionRowStatus_Object = MibTableColumn
alTelnetStatsSessionRowStatus = _AlTelnetStatsSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 2, 1, 1),
    _AlTelnetStatsSessionRowStatus_Type()
)
alTelnetStatsSessionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alTelnetStatsSessionRowStatus.setStatus("current")
_AlTelnetStatsSessionId_Type = Integer32
_AlTelnetStatsSessionId_Object = MibTableColumn
alTelnetStatsSessionId = _AlTelnetStatsSessionId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 2, 1, 2),
    _AlTelnetStatsSessionId_Type()
)
alTelnetStatsSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsSessionId.setStatus("current")
_AlTelnetStatsSessionIpAddr_Type = IpAddress
_AlTelnetStatsSessionIpAddr_Object = MibTableColumn
alTelnetStatsSessionIpAddr = _AlTelnetStatsSessionIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 2, 1, 3),
    _AlTelnetStatsSessionIpAddr_Type()
)
alTelnetStatsSessionIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsSessionIpAddr.setStatus("current")
_AlTelnetStatsSessionSrcPort_Type = Integer32
_AlTelnetStatsSessionSrcPort_Object = MibTableColumn
alTelnetStatsSessionSrcPort = _AlTelnetStatsSessionSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 2, 1, 4),
    _AlTelnetStatsSessionSrcPort_Type()
)
alTelnetStatsSessionSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsSessionSrcPort.setStatus("current")
_AlTelnetStatsSessionName_Type = DisplayString
_AlTelnetStatsSessionName_Object = MibTableColumn
alTelnetStatsSessionName = _AlTelnetStatsSessionName_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 2, 1, 5),
    _AlTelnetStatsSessionName_Type()
)
alTelnetStatsSessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsSessionName.setStatus("current")
_AlTelnetStatsSessionInNetPackets_Type = Counter32
_AlTelnetStatsSessionInNetPackets_Object = MibTableColumn
alTelnetStatsSessionInNetPackets = _AlTelnetStatsSessionInNetPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 2, 1, 6),
    _AlTelnetStatsSessionInNetPackets_Type()
)
alTelnetStatsSessionInNetPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsSessionInNetPackets.setStatus("current")
_AlTelnetStatsSessionInNetOctets_Type = Counter32
_AlTelnetStatsSessionInNetOctets_Object = MibTableColumn
alTelnetStatsSessionInNetOctets = _AlTelnetStatsSessionInNetOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 2, 1, 7),
    _AlTelnetStatsSessionInNetOctets_Type()
)
alTelnetStatsSessionInNetOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsSessionInNetOctets.setStatus("current")
_AlTelnetStatsSessionInNetCmdOctets_Type = Counter32
_AlTelnetStatsSessionInNetCmdOctets_Object = MibTableColumn
alTelnetStatsSessionInNetCmdOctets = _AlTelnetStatsSessionInNetCmdOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 2, 1, 8),
    _AlTelnetStatsSessionInNetCmdOctets_Type()
)
alTelnetStatsSessionInNetCmdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsSessionInNetCmdOctets.setStatus("current")
_AlTelnetStatsSessionInNetDropPackets_Type = Counter32
_AlTelnetStatsSessionInNetDropPackets_Object = MibTableColumn
alTelnetStatsSessionInNetDropPackets = _AlTelnetStatsSessionInNetDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 2, 1, 9),
    _AlTelnetStatsSessionInNetDropPackets_Type()
)
alTelnetStatsSessionInNetDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsSessionInNetDropPackets.setStatus("current")
_AlTelnetStatsSessionInNetDropOctets_Type = Counter32
_AlTelnetStatsSessionInNetDropOctets_Object = MibTableColumn
alTelnetStatsSessionInNetDropOctets = _AlTelnetStatsSessionInNetDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 2, 1, 10),
    _AlTelnetStatsSessionInNetDropOctets_Type()
)
alTelnetStatsSessionInNetDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsSessionInNetDropOctets.setStatus("current")
_AlTelnetStatsSessionOutNetPackets_Type = Counter32
_AlTelnetStatsSessionOutNetPackets_Object = MibTableColumn
alTelnetStatsSessionOutNetPackets = _AlTelnetStatsSessionOutNetPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 2, 1, 11),
    _AlTelnetStatsSessionOutNetPackets_Type()
)
alTelnetStatsSessionOutNetPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsSessionOutNetPackets.setStatus("current")
_AlTelnetStatsSessionOutNetOctets_Type = Counter32
_AlTelnetStatsSessionOutNetOctets_Object = MibTableColumn
alTelnetStatsSessionOutNetOctets = _AlTelnetStatsSessionOutNetOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 2, 1, 12),
    _AlTelnetStatsSessionOutNetOctets_Type()
)
alTelnetStatsSessionOutNetOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsSessionOutNetOctets.setStatus("current")
_AlTelnetStatsSessionOutNetDropPackets_Type = Counter32
_AlTelnetStatsSessionOutNetDropPackets_Object = MibTableColumn
alTelnetStatsSessionOutNetDropPackets = _AlTelnetStatsSessionOutNetDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 2, 1, 13),
    _AlTelnetStatsSessionOutNetDropPackets_Type()
)
alTelnetStatsSessionOutNetDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsSessionOutNetDropPackets.setStatus("current")
_AlTelnetStatsSessionOutNetDropOctets_Type = Counter32
_AlTelnetStatsSessionOutNetDropOctets_Object = MibTableColumn
alTelnetStatsSessionOutNetDropOctets = _AlTelnetStatsSessionOutNetDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 2, 1, 14),
    _AlTelnetStatsSessionOutNetDropOctets_Type()
)
alTelnetStatsSessionOutNetDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsSessionOutNetDropOctets.setStatus("current")
_AlTelnetStatsSessionInShPackets_Type = Counter32
_AlTelnetStatsSessionInShPackets_Object = MibTableColumn
alTelnetStatsSessionInShPackets = _AlTelnetStatsSessionInShPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 2, 1, 15),
    _AlTelnetStatsSessionInShPackets_Type()
)
alTelnetStatsSessionInShPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsSessionInShPackets.setStatus("current")
_AlTelnetStatsSessionInShOctets_Type = Counter32
_AlTelnetStatsSessionInShOctets_Object = MibTableColumn
alTelnetStatsSessionInShOctets = _AlTelnetStatsSessionInShOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 2, 1, 16),
    _AlTelnetStatsSessionInShOctets_Type()
)
alTelnetStatsSessionInShOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsSessionInShOctets.setStatus("current")
_AlTelnetStatsSessionInShDropPackets_Type = Counter32
_AlTelnetStatsSessionInShDropPackets_Object = MibTableColumn
alTelnetStatsSessionInShDropPackets = _AlTelnetStatsSessionInShDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 2, 1, 17),
    _AlTelnetStatsSessionInShDropPackets_Type()
)
alTelnetStatsSessionInShDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsSessionInShDropPackets.setStatus("current")
_AlTelnetStatsSessionInShDropOctets_Type = Counter32
_AlTelnetStatsSessionInShDropOctets_Object = MibTableColumn
alTelnetStatsSessionInShDropOctets = _AlTelnetStatsSessionInShDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 2, 1, 18),
    _AlTelnetStatsSessionInShDropOctets_Type()
)
alTelnetStatsSessionInShDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsSessionInShDropOctets.setStatus("current")
_AlTelnetStatsSessionOutShPackets_Type = Counter32
_AlTelnetStatsSessionOutShPackets_Object = MibTableColumn
alTelnetStatsSessionOutShPackets = _AlTelnetStatsSessionOutShPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 2, 1, 19),
    _AlTelnetStatsSessionOutShPackets_Type()
)
alTelnetStatsSessionOutShPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsSessionOutShPackets.setStatus("current")
_AlTelnetStatsSessionOutShOctets_Type = Counter32
_AlTelnetStatsSessionOutShOctets_Object = MibTableColumn
alTelnetStatsSessionOutShOctets = _AlTelnetStatsSessionOutShOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 2, 1, 20),
    _AlTelnetStatsSessionOutShOctets_Type()
)
alTelnetStatsSessionOutShOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsSessionOutShOctets.setStatus("current")
_AlTelnetStatsSessionOutShDropPackets_Type = Counter32
_AlTelnetStatsSessionOutShDropPackets_Object = MibTableColumn
alTelnetStatsSessionOutShDropPackets = _AlTelnetStatsSessionOutShDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 2, 1, 21),
    _AlTelnetStatsSessionOutShDropPackets_Type()
)
alTelnetStatsSessionOutShDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsSessionOutShDropPackets.setStatus("current")
_AlTelnetStatsSessionOutShDropOctets_Type = Counter32
_AlTelnetStatsSessionOutShDropOctets_Object = MibTableColumn
alTelnetStatsSessionOutShDropOctets = _AlTelnetStatsSessionOutShDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 11, 2, 1, 22),
    _AlTelnetStatsSessionOutShDropOctets_Type()
)
alTelnetStatsSessionOutShDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTelnetStatsSessionOutShDropOctets.setStatus("current")

# Managed Objects groups

altigaTelnetStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 11, 2)
)
altigaTelnetStatsGroup.setObjects(
      *(("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsActiveSessions"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsAttemptedSessions"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsSuccessfulSessions"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsInNetPackets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsInNetOctets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsInNetCmdOctets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsInNetDropPackets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsInNetDropOctets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsOutNetPackets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsOutNetOctets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsOutNetDropPackets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsOutNetDropOctets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsInShPackets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsInShOctets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsInShDropPackets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsInShDropOctets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsOutShPackets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsOutShOctets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsOutShDropPackets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsOutShDropOctets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsSessionRowStatus"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsSessionId"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsSessionIpAddr"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsSessionSrcPort"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsSessionName"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsSessionInNetPackets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsSessionInNetOctets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsSessionInNetCmdOctets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsSessionInNetDropPackets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsSessionInNetDropOctets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsSessionOutNetPackets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsSessionOutNetOctets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsSessionOutNetDropPackets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsSessionOutNetDropOctets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsSessionInShPackets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsSessionInShOctets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsSessionInShDropPackets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsSessionInShDropOctets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsSessionOutShPackets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsSessionOutShOctets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsSessionOutShDropPackets"),
        ("ALTIGA-TELNET-STATS-MIB", "alTelnetStatsSessionOutShDropOctets"))
)
if mibBuilder.loadTexts:
    altigaTelnetStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaTelnetStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 16, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaTelnetStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-TELNET-STATS-MIB",
    **{"altigaTelnetStatsMibModule": altigaTelnetStatsMibModule,
       "altigaTelnetStatsMibConformance": altigaTelnetStatsMibConformance,
       "altigaTelnetStatsMibCompliances": altigaTelnetStatsMibCompliances,
       "altigaTelnetStatsMibCompliance": altigaTelnetStatsMibCompliance,
       "altigaTelnetStatsGroup": altigaTelnetStatsGroup,
       "alStatsTelnetGlobal": alStatsTelnetGlobal,
       "alTelnetStatsActiveSessions": alTelnetStatsActiveSessions,
       "alTelnetStatsAttemptedSessions": alTelnetStatsAttemptedSessions,
       "alTelnetStatsSuccessfulSessions": alTelnetStatsSuccessfulSessions,
       "alTelnetStatsInNetPackets": alTelnetStatsInNetPackets,
       "alTelnetStatsInNetOctets": alTelnetStatsInNetOctets,
       "alTelnetStatsInNetCmdOctets": alTelnetStatsInNetCmdOctets,
       "alTelnetStatsInNetDropPackets": alTelnetStatsInNetDropPackets,
       "alTelnetStatsInNetDropOctets": alTelnetStatsInNetDropOctets,
       "alTelnetStatsOutNetPackets": alTelnetStatsOutNetPackets,
       "alTelnetStatsOutNetOctets": alTelnetStatsOutNetOctets,
       "alTelnetStatsOutNetDropPackets": alTelnetStatsOutNetDropPackets,
       "alTelnetStatsOutNetDropOctets": alTelnetStatsOutNetDropOctets,
       "alTelnetStatsInShPackets": alTelnetStatsInShPackets,
       "alTelnetStatsInShOctets": alTelnetStatsInShOctets,
       "alTelnetStatsInShDropPackets": alTelnetStatsInShDropPackets,
       "alTelnetStatsInShDropOctets": alTelnetStatsInShDropOctets,
       "alTelnetStatsOutShPackets": alTelnetStatsOutShPackets,
       "alTelnetStatsOutShOctets": alTelnetStatsOutShOctets,
       "alTelnetStatsOutShDropPackets": alTelnetStatsOutShDropPackets,
       "alTelnetStatsOutShDropOctets": alTelnetStatsOutShDropOctets,
       "alTelnetStatsSessionTable": alTelnetStatsSessionTable,
       "alTelnetStatsSessionEntry": alTelnetStatsSessionEntry,
       "alTelnetStatsSessionRowStatus": alTelnetStatsSessionRowStatus,
       "alTelnetStatsSessionId": alTelnetStatsSessionId,
       "alTelnetStatsSessionIpAddr": alTelnetStatsSessionIpAddr,
       "alTelnetStatsSessionSrcPort": alTelnetStatsSessionSrcPort,
       "alTelnetStatsSessionName": alTelnetStatsSessionName,
       "alTelnetStatsSessionInNetPackets": alTelnetStatsSessionInNetPackets,
       "alTelnetStatsSessionInNetOctets": alTelnetStatsSessionInNetOctets,
       "alTelnetStatsSessionInNetCmdOctets": alTelnetStatsSessionInNetCmdOctets,
       "alTelnetStatsSessionInNetDropPackets": alTelnetStatsSessionInNetDropPackets,
       "alTelnetStatsSessionInNetDropOctets": alTelnetStatsSessionInNetDropOctets,
       "alTelnetStatsSessionOutNetPackets": alTelnetStatsSessionOutNetPackets,
       "alTelnetStatsSessionOutNetOctets": alTelnetStatsSessionOutNetOctets,
       "alTelnetStatsSessionOutNetDropPackets": alTelnetStatsSessionOutNetDropPackets,
       "alTelnetStatsSessionOutNetDropOctets": alTelnetStatsSessionOutNetDropOctets,
       "alTelnetStatsSessionInShPackets": alTelnetStatsSessionInShPackets,
       "alTelnetStatsSessionInShOctets": alTelnetStatsSessionInShOctets,
       "alTelnetStatsSessionInShDropPackets": alTelnetStatsSessionInShDropPackets,
       "alTelnetStatsSessionInShDropOctets": alTelnetStatsSessionInShDropOctets,
       "alTelnetStatsSessionOutShPackets": alTelnetStatsSessionOutShPackets,
       "alTelnetStatsSessionOutShOctets": alTelnetStatsSessionOutShOctets,
       "alTelnetStatsSessionOutShDropPackets": alTelnetStatsSessionOutShDropPackets,
       "alTelnetStatsSessionOutShDropOctets": alTelnetStatsSessionOutShDropOctets}
)
