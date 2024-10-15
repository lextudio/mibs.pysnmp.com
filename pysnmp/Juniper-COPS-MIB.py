# SNMP MIB module (Juniper-COPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-COPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:54 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniName,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniName")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

juniCopsProtocolMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37)
)
juniCopsProtocolMIB.setRevisions(
        ("2002-09-16 21:44",
         "2002-01-14 19:01",
         "2000-02-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniCopsProtocolObjects_ObjectIdentity = ObjectIdentity
juniCopsProtocolObjects = _JuniCopsProtocolObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1)
)
_JuniCopsProtocolCfg_ObjectIdentity = ObjectIdentity
juniCopsProtocolCfg = _JuniCopsProtocolCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 1)
)
_JuniCopsProtocolStatus_ObjectIdentity = ObjectIdentity
juniCopsProtocolStatus = _JuniCopsProtocolStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 2)
)
_JuniCopsProtocolStatistics_ObjectIdentity = ObjectIdentity
juniCopsProtocolStatistics = _JuniCopsProtocolStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3)
)
_JuniCopsProtocolStatisticsScalars_ObjectIdentity = ObjectIdentity
juniCopsProtocolStatisticsScalars = _JuniCopsProtocolStatisticsScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1)
)
_JuniCopsProtocolSessionsCreated_Type = Counter32
_JuniCopsProtocolSessionsCreated_Object = MibScalar
juniCopsProtocolSessionsCreated = _JuniCopsProtocolSessionsCreated_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 1),
    _JuniCopsProtocolSessionsCreated_Type()
)
juniCopsProtocolSessionsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolSessionsCreated.setStatus("current")
_JuniCopsProtocolSessionsDeleted_Type = Counter32
_JuniCopsProtocolSessionsDeleted_Object = MibScalar
juniCopsProtocolSessionsDeleted = _JuniCopsProtocolSessionsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 2),
    _JuniCopsProtocolSessionsDeleted_Type()
)
juniCopsProtocolSessionsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolSessionsDeleted.setStatus("current")
_JuniCopsProtocolCurrentSessions_Type = Counter32
_JuniCopsProtocolCurrentSessions_Object = MibScalar
juniCopsProtocolCurrentSessions = _JuniCopsProtocolCurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 3),
    _JuniCopsProtocolCurrentSessions_Type()
)
juniCopsProtocolCurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolCurrentSessions.setStatus("current")
_JuniCopsProtocolBytesReceived_Type = Counter32
_JuniCopsProtocolBytesReceived_Object = MibScalar
juniCopsProtocolBytesReceived = _JuniCopsProtocolBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 4),
    _JuniCopsProtocolBytesReceived_Type()
)
juniCopsProtocolBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolBytesReceived.setStatus("current")
_JuniCopsProtocolPacketsReceived_Type = Counter32
_JuniCopsProtocolPacketsReceived_Object = MibScalar
juniCopsProtocolPacketsReceived = _JuniCopsProtocolPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 5),
    _JuniCopsProtocolPacketsReceived_Type()
)
juniCopsProtocolPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolPacketsReceived.setStatus("current")
_JuniCopsProtocolBytesSent_Type = Counter32
_JuniCopsProtocolBytesSent_Object = MibScalar
juniCopsProtocolBytesSent = _JuniCopsProtocolBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 6),
    _JuniCopsProtocolBytesSent_Type()
)
juniCopsProtocolBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolBytesSent.setStatus("current")
_JuniCopsProtocolPacketsSent_Type = Counter32
_JuniCopsProtocolPacketsSent_Object = MibScalar
juniCopsProtocolPacketsSent = _JuniCopsProtocolPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 7),
    _JuniCopsProtocolPacketsSent_Type()
)
juniCopsProtocolPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolPacketsSent.setStatus("current")
_JuniCopsProtocolKeepAlivesReceived_Type = Counter32
_JuniCopsProtocolKeepAlivesReceived_Object = MibScalar
juniCopsProtocolKeepAlivesReceived = _JuniCopsProtocolKeepAlivesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 8),
    _JuniCopsProtocolKeepAlivesReceived_Type()
)
juniCopsProtocolKeepAlivesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolKeepAlivesReceived.setStatus("current")
_JuniCopsProtocolKeepAlivesSent_Type = Counter32
_JuniCopsProtocolKeepAlivesSent_Object = MibScalar
juniCopsProtocolKeepAlivesSent = _JuniCopsProtocolKeepAlivesSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 9),
    _JuniCopsProtocolKeepAlivesSent_Type()
)
juniCopsProtocolKeepAlivesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolKeepAlivesSent.setStatus("current")
_JuniCopsProtocolSession_ObjectIdentity = ObjectIdentity
juniCopsProtocolSession = _JuniCopsProtocolSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4)
)
_JuniCopsProtocolSessionTable_Object = MibTable
juniCopsProtocolSessionTable = _JuniCopsProtocolSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1)
)
if mibBuilder.loadTexts:
    juniCopsProtocolSessionTable.setStatus("current")
_JuniCopsProtocolSessionEntry_Object = MibTableRow
juniCopsProtocolSessionEntry = _JuniCopsProtocolSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1)
)
juniCopsProtocolSessionEntry.setIndexNames(
    (0, "Juniper-COPS-MIB", "juniCopsProtocolSessionClientType"),
)
if mibBuilder.loadTexts:
    juniCopsProtocolSessionEntry.setStatus("current")


class _JuniCopsProtocolSessionClientType_Type(Integer32):
    """Custom type juniCopsProtocolSessionClientType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniCopsProtocolSessionClientType_Type.__name__ = "Integer32"
_JuniCopsProtocolSessionClientType_Object = MibTableColumn
juniCopsProtocolSessionClientType = _JuniCopsProtocolSessionClientType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 1),
    _JuniCopsProtocolSessionClientType_Type()
)
juniCopsProtocolSessionClientType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniCopsProtocolSessionClientType.setStatus("current")
_JuniCopsProtocolSessionRemoteAddress_Type = IpAddress
_JuniCopsProtocolSessionRemoteAddress_Object = MibTableColumn
juniCopsProtocolSessionRemoteAddress = _JuniCopsProtocolSessionRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 2),
    _JuniCopsProtocolSessionRemoteAddress_Type()
)
juniCopsProtocolSessionRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolSessionRemoteAddress.setStatus("current")
_JuniCopsProtocolSessionRemotePort_Type = Integer32
_JuniCopsProtocolSessionRemotePort_Object = MibTableColumn
juniCopsProtocolSessionRemotePort = _JuniCopsProtocolSessionRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 3),
    _JuniCopsProtocolSessionRemotePort_Type()
)
juniCopsProtocolSessionRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolSessionRemotePort.setStatus("current")
_JuniCopsProtocolSessionBytesReceived_Type = Counter32
_JuniCopsProtocolSessionBytesReceived_Object = MibTableColumn
juniCopsProtocolSessionBytesReceived = _JuniCopsProtocolSessionBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 4),
    _JuniCopsProtocolSessionBytesReceived_Type()
)
juniCopsProtocolSessionBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolSessionBytesReceived.setStatus("current")
_JuniCopsProtocolSessionPacketsReceived_Type = Counter32
_JuniCopsProtocolSessionPacketsReceived_Object = MibTableColumn
juniCopsProtocolSessionPacketsReceived = _JuniCopsProtocolSessionPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 5),
    _JuniCopsProtocolSessionPacketsReceived_Type()
)
juniCopsProtocolSessionPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolSessionPacketsReceived.setStatus("current")
_JuniCopsProtocolSessionBytesSent_Type = Counter32
_JuniCopsProtocolSessionBytesSent_Object = MibTableColumn
juniCopsProtocolSessionBytesSent = _JuniCopsProtocolSessionBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 6),
    _JuniCopsProtocolSessionBytesSent_Type()
)
juniCopsProtocolSessionBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolSessionBytesSent.setStatus("current")
_JuniCopsProtocolSessionPacketsSent_Type = Counter32
_JuniCopsProtocolSessionPacketsSent_Object = MibTableColumn
juniCopsProtocolSessionPacketsSent = _JuniCopsProtocolSessionPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 7),
    _JuniCopsProtocolSessionPacketsSent_Type()
)
juniCopsProtocolSessionPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolSessionPacketsSent.setStatus("current")
_JuniCopsProtocolSessionREQSent_Type = Counter32
_JuniCopsProtocolSessionREQSent_Object = MibTableColumn
juniCopsProtocolSessionREQSent = _JuniCopsProtocolSessionREQSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 8),
    _JuniCopsProtocolSessionREQSent_Type()
)
juniCopsProtocolSessionREQSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolSessionREQSent.setStatus("current")
_JuniCopsProtocolSessionDECReceived_Type = Counter32
_JuniCopsProtocolSessionDECReceived_Object = MibTableColumn
juniCopsProtocolSessionDECReceived = _JuniCopsProtocolSessionDECReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 9),
    _JuniCopsProtocolSessionDECReceived_Type()
)
juniCopsProtocolSessionDECReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolSessionDECReceived.setStatus("current")
_JuniCopsProtocolSessionRPTSent_Type = Counter32
_JuniCopsProtocolSessionRPTSent_Object = MibTableColumn
juniCopsProtocolSessionRPTSent = _JuniCopsProtocolSessionRPTSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 10),
    _JuniCopsProtocolSessionRPTSent_Type()
)
juniCopsProtocolSessionRPTSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolSessionRPTSent.setStatus("current")
_JuniCopsProtocolSessionDRQSent_Type = Counter32
_JuniCopsProtocolSessionDRQSent_Object = MibTableColumn
juniCopsProtocolSessionDRQSent = _JuniCopsProtocolSessionDRQSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 11),
    _JuniCopsProtocolSessionDRQSent_Type()
)
juniCopsProtocolSessionDRQSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolSessionDRQSent.setStatus("current")
_JuniCopsProtocolSessionSSQSent_Type = Counter32
_JuniCopsProtocolSessionSSQSent_Object = MibTableColumn
juniCopsProtocolSessionSSQSent = _JuniCopsProtocolSessionSSQSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 12),
    _JuniCopsProtocolSessionSSQSent_Type()
)
juniCopsProtocolSessionSSQSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolSessionSSQSent.setStatus("current")
_JuniCopsProtocolSessionOPNSent_Type = Counter32
_JuniCopsProtocolSessionOPNSent_Object = MibTableColumn
juniCopsProtocolSessionOPNSent = _JuniCopsProtocolSessionOPNSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 13),
    _JuniCopsProtocolSessionOPNSent_Type()
)
juniCopsProtocolSessionOPNSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolSessionOPNSent.setStatus("current")
_JuniCopsProtocolSessionCATReceived_Type = Counter32
_JuniCopsProtocolSessionCATReceived_Object = MibTableColumn
juniCopsProtocolSessionCATReceived = _JuniCopsProtocolSessionCATReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 14),
    _JuniCopsProtocolSessionCATReceived_Type()
)
juniCopsProtocolSessionCATReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolSessionCATReceived.setStatus("current")
_JuniCopsProtocolSessionCCSent_Type = Counter32
_JuniCopsProtocolSessionCCSent_Object = MibTableColumn
juniCopsProtocolSessionCCSent = _JuniCopsProtocolSessionCCSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 15),
    _JuniCopsProtocolSessionCCSent_Type()
)
juniCopsProtocolSessionCCSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolSessionCCSent.setStatus("current")
_JuniCopsProtocolSessionCCReceived_Type = Counter32
_JuniCopsProtocolSessionCCReceived_Object = MibTableColumn
juniCopsProtocolSessionCCReceived = _JuniCopsProtocolSessionCCReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 16),
    _JuniCopsProtocolSessionCCReceived_Type()
)
juniCopsProtocolSessionCCReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolSessionCCReceived.setStatus("current")
_JuniCopsProtocolSessionSSCSent_Type = Counter32
_JuniCopsProtocolSessionSSCSent_Object = MibTableColumn
juniCopsProtocolSessionSSCSent = _JuniCopsProtocolSessionSSCSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 17),
    _JuniCopsProtocolSessionSSCSent_Type()
)
juniCopsProtocolSessionSSCSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolSessionSSCSent.setStatus("current")
_JuniCopsProtocolSessionLocalAddress_Type = IpAddress
_JuniCopsProtocolSessionLocalAddress_Object = MibTableColumn
juniCopsProtocolSessionLocalAddress = _JuniCopsProtocolSessionLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 18),
    _JuniCopsProtocolSessionLocalAddress_Type()
)
juniCopsProtocolSessionLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolSessionLocalAddress.setStatus("current")
_JuniCopsProtocolSessionTransportRouterName_Type = JuniName
_JuniCopsProtocolSessionTransportRouterName_Object = MibTableColumn
juniCopsProtocolSessionTransportRouterName = _JuniCopsProtocolSessionTransportRouterName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 19),
    _JuniCopsProtocolSessionTransportRouterName_Type()
)
juniCopsProtocolSessionTransportRouterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCopsProtocolSessionTransportRouterName.setStatus("current")
_JuniCopsProtocolMIBConformance_ObjectIdentity = ObjectIdentity
juniCopsProtocolMIBConformance = _JuniCopsProtocolMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4)
)
_JuniCopsProtocolMIBCompliances_ObjectIdentity = ObjectIdentity
juniCopsProtocolMIBCompliances = _JuniCopsProtocolMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4, 1)
)
_JuniCopsProtocolMIBGroups_ObjectIdentity = ObjectIdentity
juniCopsProtocolMIBGroups = _JuniCopsProtocolMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4, 2)
)

# Managed Objects groups

juniCopsProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4, 2, 1)
)
juniCopsProtocolGroup.setObjects(
      *(("Juniper-COPS-MIB", "juniCopsProtocolSessionsCreated"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionsDeleted"),
        ("Juniper-COPS-MIB", "juniCopsProtocolCurrentSessions"),
        ("Juniper-COPS-MIB", "juniCopsProtocolBytesReceived"),
        ("Juniper-COPS-MIB", "juniCopsProtocolPacketsReceived"),
        ("Juniper-COPS-MIB", "juniCopsProtocolBytesSent"),
        ("Juniper-COPS-MIB", "juniCopsProtocolPacketsSent"),
        ("Juniper-COPS-MIB", "juniCopsProtocolKeepAlivesReceived"),
        ("Juniper-COPS-MIB", "juniCopsProtocolKeepAlivesSent"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionRemoteAddress"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionRemotePort"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionBytesReceived"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionPacketsReceived"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionBytesSent"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionPacketsSent"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionREQSent"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionDECReceived"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionRPTSent"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionDRQSent"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionSSQSent"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionOPNSent"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionCATReceived"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionCCSent"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionCCReceived"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionSSCSent"))
)
if mibBuilder.loadTexts:
    juniCopsProtocolGroup.setStatus("obsolete")

juniCopsProtocolGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4, 2, 2)
)
juniCopsProtocolGroup2.setObjects(
      *(("Juniper-COPS-MIB", "juniCopsProtocolSessionsCreated"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionsDeleted"),
        ("Juniper-COPS-MIB", "juniCopsProtocolCurrentSessions"),
        ("Juniper-COPS-MIB", "juniCopsProtocolBytesReceived"),
        ("Juniper-COPS-MIB", "juniCopsProtocolPacketsReceived"),
        ("Juniper-COPS-MIB", "juniCopsProtocolBytesSent"),
        ("Juniper-COPS-MIB", "juniCopsProtocolPacketsSent"),
        ("Juniper-COPS-MIB", "juniCopsProtocolKeepAlivesReceived"),
        ("Juniper-COPS-MIB", "juniCopsProtocolKeepAlivesSent"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionRemoteAddress"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionRemotePort"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionBytesReceived"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionPacketsReceived"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionBytesSent"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionPacketsSent"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionREQSent"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionDECReceived"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionRPTSent"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionDRQSent"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionSSQSent"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionOPNSent"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionCATReceived"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionCCSent"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionCCReceived"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionSSCSent"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionLocalAddress"),
        ("Juniper-COPS-MIB", "juniCopsProtocolSessionTransportRouterName"))
)
if mibBuilder.loadTexts:
    juniCopsProtocolGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniCopsProtocolAuthCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniCopsProtocolAuthCompliance.setStatus(
        "obsolete"
    )

juniCopsProtocolAuthCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniCopsProtocolAuthCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-COPS-MIB",
    **{"juniCopsProtocolMIB": juniCopsProtocolMIB,
       "juniCopsProtocolObjects": juniCopsProtocolObjects,
       "juniCopsProtocolCfg": juniCopsProtocolCfg,
       "juniCopsProtocolStatus": juniCopsProtocolStatus,
       "juniCopsProtocolStatistics": juniCopsProtocolStatistics,
       "juniCopsProtocolStatisticsScalars": juniCopsProtocolStatisticsScalars,
       "juniCopsProtocolSessionsCreated": juniCopsProtocolSessionsCreated,
       "juniCopsProtocolSessionsDeleted": juniCopsProtocolSessionsDeleted,
       "juniCopsProtocolCurrentSessions": juniCopsProtocolCurrentSessions,
       "juniCopsProtocolBytesReceived": juniCopsProtocolBytesReceived,
       "juniCopsProtocolPacketsReceived": juniCopsProtocolPacketsReceived,
       "juniCopsProtocolBytesSent": juniCopsProtocolBytesSent,
       "juniCopsProtocolPacketsSent": juniCopsProtocolPacketsSent,
       "juniCopsProtocolKeepAlivesReceived": juniCopsProtocolKeepAlivesReceived,
       "juniCopsProtocolKeepAlivesSent": juniCopsProtocolKeepAlivesSent,
       "juniCopsProtocolSession": juniCopsProtocolSession,
       "juniCopsProtocolSessionTable": juniCopsProtocolSessionTable,
       "juniCopsProtocolSessionEntry": juniCopsProtocolSessionEntry,
       "juniCopsProtocolSessionClientType": juniCopsProtocolSessionClientType,
       "juniCopsProtocolSessionRemoteAddress": juniCopsProtocolSessionRemoteAddress,
       "juniCopsProtocolSessionRemotePort": juniCopsProtocolSessionRemotePort,
       "juniCopsProtocolSessionBytesReceived": juniCopsProtocolSessionBytesReceived,
       "juniCopsProtocolSessionPacketsReceived": juniCopsProtocolSessionPacketsReceived,
       "juniCopsProtocolSessionBytesSent": juniCopsProtocolSessionBytesSent,
       "juniCopsProtocolSessionPacketsSent": juniCopsProtocolSessionPacketsSent,
       "juniCopsProtocolSessionREQSent": juniCopsProtocolSessionREQSent,
       "juniCopsProtocolSessionDECReceived": juniCopsProtocolSessionDECReceived,
       "juniCopsProtocolSessionRPTSent": juniCopsProtocolSessionRPTSent,
       "juniCopsProtocolSessionDRQSent": juniCopsProtocolSessionDRQSent,
       "juniCopsProtocolSessionSSQSent": juniCopsProtocolSessionSSQSent,
       "juniCopsProtocolSessionOPNSent": juniCopsProtocolSessionOPNSent,
       "juniCopsProtocolSessionCATReceived": juniCopsProtocolSessionCATReceived,
       "juniCopsProtocolSessionCCSent": juniCopsProtocolSessionCCSent,
       "juniCopsProtocolSessionCCReceived": juniCopsProtocolSessionCCReceived,
       "juniCopsProtocolSessionSSCSent": juniCopsProtocolSessionSSCSent,
       "juniCopsProtocolSessionLocalAddress": juniCopsProtocolSessionLocalAddress,
       "juniCopsProtocolSessionTransportRouterName": juniCopsProtocolSessionTransportRouterName,
       "juniCopsProtocolMIBConformance": juniCopsProtocolMIBConformance,
       "juniCopsProtocolMIBCompliances": juniCopsProtocolMIBCompliances,
       "juniCopsProtocolAuthCompliance": juniCopsProtocolAuthCompliance,
       "juniCopsProtocolAuthCompliance2": juniCopsProtocolAuthCompliance2,
       "juniCopsProtocolMIBGroups": juniCopsProtocolMIBGroups,
       "juniCopsProtocolGroup": juniCopsProtocolGroup,
       "juniCopsProtocolGroup2": juniCopsProtocolGroup2}
)
