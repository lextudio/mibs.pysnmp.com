# SNMP MIB module (Unisphere-Data-COPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-COPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:28 2024
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

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdName,) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdName")


# MODULE-IDENTITY

usdCopsProtocolMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37)
)
usdCopsProtocolMIB.setRevisions(
        ("2002-01-14 19:01",
         "2000-02-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdCopsProtocolObjects_ObjectIdentity = ObjectIdentity
usdCopsProtocolObjects = _UsdCopsProtocolObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1)
)
_UsdCopsProtocolCfg_ObjectIdentity = ObjectIdentity
usdCopsProtocolCfg = _UsdCopsProtocolCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 1)
)
_UsdCopsProtocolStatus_ObjectIdentity = ObjectIdentity
usdCopsProtocolStatus = _UsdCopsProtocolStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 2)
)
_UsdCopsProtocolStatistics_ObjectIdentity = ObjectIdentity
usdCopsProtocolStatistics = _UsdCopsProtocolStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3)
)
_UsdCopsProtocolStatisticsScalars_ObjectIdentity = ObjectIdentity
usdCopsProtocolStatisticsScalars = _UsdCopsProtocolStatisticsScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1)
)
_UsdCopsProtocolSessionsCreated_Type = Counter32
_UsdCopsProtocolSessionsCreated_Object = MibScalar
usdCopsProtocolSessionsCreated = _UsdCopsProtocolSessionsCreated_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 1),
    _UsdCopsProtocolSessionsCreated_Type()
)
usdCopsProtocolSessionsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolSessionsCreated.setStatus("current")
_UsdCopsProtocolSessionsDeleted_Type = Counter32
_UsdCopsProtocolSessionsDeleted_Object = MibScalar
usdCopsProtocolSessionsDeleted = _UsdCopsProtocolSessionsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 2),
    _UsdCopsProtocolSessionsDeleted_Type()
)
usdCopsProtocolSessionsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolSessionsDeleted.setStatus("current")
_UsdCopsProtocolCurrentSessions_Type = Counter32
_UsdCopsProtocolCurrentSessions_Object = MibScalar
usdCopsProtocolCurrentSessions = _UsdCopsProtocolCurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 3),
    _UsdCopsProtocolCurrentSessions_Type()
)
usdCopsProtocolCurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolCurrentSessions.setStatus("current")
_UsdCopsProtocolBytesReceived_Type = Counter32
_UsdCopsProtocolBytesReceived_Object = MibScalar
usdCopsProtocolBytesReceived = _UsdCopsProtocolBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 4),
    _UsdCopsProtocolBytesReceived_Type()
)
usdCopsProtocolBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolBytesReceived.setStatus("current")
_UsdCopsProtocolPacketsReceived_Type = Counter32
_UsdCopsProtocolPacketsReceived_Object = MibScalar
usdCopsProtocolPacketsReceived = _UsdCopsProtocolPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 5),
    _UsdCopsProtocolPacketsReceived_Type()
)
usdCopsProtocolPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolPacketsReceived.setStatus("current")
_UsdCopsProtocolBytesSent_Type = Counter32
_UsdCopsProtocolBytesSent_Object = MibScalar
usdCopsProtocolBytesSent = _UsdCopsProtocolBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 6),
    _UsdCopsProtocolBytesSent_Type()
)
usdCopsProtocolBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolBytesSent.setStatus("current")
_UsdCopsProtocolPacketsSent_Type = Counter32
_UsdCopsProtocolPacketsSent_Object = MibScalar
usdCopsProtocolPacketsSent = _UsdCopsProtocolPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 7),
    _UsdCopsProtocolPacketsSent_Type()
)
usdCopsProtocolPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolPacketsSent.setStatus("current")
_UsdCopsProtocolKeepAlivesReceived_Type = Counter32
_UsdCopsProtocolKeepAlivesReceived_Object = MibScalar
usdCopsProtocolKeepAlivesReceived = _UsdCopsProtocolKeepAlivesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 8),
    _UsdCopsProtocolKeepAlivesReceived_Type()
)
usdCopsProtocolKeepAlivesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolKeepAlivesReceived.setStatus("current")
_UsdCopsProtocolKeepAlivesSent_Type = Counter32
_UsdCopsProtocolKeepAlivesSent_Object = MibScalar
usdCopsProtocolKeepAlivesSent = _UsdCopsProtocolKeepAlivesSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 9),
    _UsdCopsProtocolKeepAlivesSent_Type()
)
usdCopsProtocolKeepAlivesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolKeepAlivesSent.setStatus("current")
_UsdCopsProtocolSession_ObjectIdentity = ObjectIdentity
usdCopsProtocolSession = _UsdCopsProtocolSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4)
)
_UsdCopsProtocolSessionTable_Object = MibTable
usdCopsProtocolSessionTable = _UsdCopsProtocolSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1)
)
if mibBuilder.loadTexts:
    usdCopsProtocolSessionTable.setStatus("current")
_UsdCopsProtocolSessionEntry_Object = MibTableRow
usdCopsProtocolSessionEntry = _UsdCopsProtocolSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1)
)
usdCopsProtocolSessionEntry.setIndexNames(
    (0, "Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionClientType"),
)
if mibBuilder.loadTexts:
    usdCopsProtocolSessionEntry.setStatus("current")


class _UsdCopsProtocolSessionClientType_Type(Integer32):
    """Custom type usdCopsProtocolSessionClientType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdCopsProtocolSessionClientType_Type.__name__ = "Integer32"
_UsdCopsProtocolSessionClientType_Object = MibTableColumn
usdCopsProtocolSessionClientType = _UsdCopsProtocolSessionClientType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 1),
    _UsdCopsProtocolSessionClientType_Type()
)
usdCopsProtocolSessionClientType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdCopsProtocolSessionClientType.setStatus("current")
_UsdCopsProtocolSessionRemoteAddress_Type = IpAddress
_UsdCopsProtocolSessionRemoteAddress_Object = MibTableColumn
usdCopsProtocolSessionRemoteAddress = _UsdCopsProtocolSessionRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 2),
    _UsdCopsProtocolSessionRemoteAddress_Type()
)
usdCopsProtocolSessionRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolSessionRemoteAddress.setStatus("current")
_UsdCopsProtocolSessionRemotePort_Type = Integer32
_UsdCopsProtocolSessionRemotePort_Object = MibTableColumn
usdCopsProtocolSessionRemotePort = _UsdCopsProtocolSessionRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 3),
    _UsdCopsProtocolSessionRemotePort_Type()
)
usdCopsProtocolSessionRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolSessionRemotePort.setStatus("current")
_UsdCopsProtocolSessionBytesReceived_Type = Counter32
_UsdCopsProtocolSessionBytesReceived_Object = MibTableColumn
usdCopsProtocolSessionBytesReceived = _UsdCopsProtocolSessionBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 4),
    _UsdCopsProtocolSessionBytesReceived_Type()
)
usdCopsProtocolSessionBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolSessionBytesReceived.setStatus("current")
_UsdCopsProtocolSessionPacketsReceived_Type = Counter32
_UsdCopsProtocolSessionPacketsReceived_Object = MibTableColumn
usdCopsProtocolSessionPacketsReceived = _UsdCopsProtocolSessionPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 5),
    _UsdCopsProtocolSessionPacketsReceived_Type()
)
usdCopsProtocolSessionPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolSessionPacketsReceived.setStatus("current")
_UsdCopsProtocolSessionBytesSent_Type = Counter32
_UsdCopsProtocolSessionBytesSent_Object = MibTableColumn
usdCopsProtocolSessionBytesSent = _UsdCopsProtocolSessionBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 6),
    _UsdCopsProtocolSessionBytesSent_Type()
)
usdCopsProtocolSessionBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolSessionBytesSent.setStatus("current")
_UsdCopsProtocolSessionPacketsSent_Type = Counter32
_UsdCopsProtocolSessionPacketsSent_Object = MibTableColumn
usdCopsProtocolSessionPacketsSent = _UsdCopsProtocolSessionPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 7),
    _UsdCopsProtocolSessionPacketsSent_Type()
)
usdCopsProtocolSessionPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolSessionPacketsSent.setStatus("current")
_UsdCopsProtocolSessionREQSent_Type = Counter32
_UsdCopsProtocolSessionREQSent_Object = MibTableColumn
usdCopsProtocolSessionREQSent = _UsdCopsProtocolSessionREQSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 8),
    _UsdCopsProtocolSessionREQSent_Type()
)
usdCopsProtocolSessionREQSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolSessionREQSent.setStatus("current")
_UsdCopsProtocolSessionDECReceived_Type = Counter32
_UsdCopsProtocolSessionDECReceived_Object = MibTableColumn
usdCopsProtocolSessionDECReceived = _UsdCopsProtocolSessionDECReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 9),
    _UsdCopsProtocolSessionDECReceived_Type()
)
usdCopsProtocolSessionDECReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolSessionDECReceived.setStatus("current")
_UsdCopsProtocolSessionRPTSent_Type = Counter32
_UsdCopsProtocolSessionRPTSent_Object = MibTableColumn
usdCopsProtocolSessionRPTSent = _UsdCopsProtocolSessionRPTSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 10),
    _UsdCopsProtocolSessionRPTSent_Type()
)
usdCopsProtocolSessionRPTSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolSessionRPTSent.setStatus("current")
_UsdCopsProtocolSessionDRQSent_Type = Counter32
_UsdCopsProtocolSessionDRQSent_Object = MibTableColumn
usdCopsProtocolSessionDRQSent = _UsdCopsProtocolSessionDRQSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 11),
    _UsdCopsProtocolSessionDRQSent_Type()
)
usdCopsProtocolSessionDRQSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolSessionDRQSent.setStatus("current")
_UsdCopsProtocolSessionSSQSent_Type = Counter32
_UsdCopsProtocolSessionSSQSent_Object = MibTableColumn
usdCopsProtocolSessionSSQSent = _UsdCopsProtocolSessionSSQSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 12),
    _UsdCopsProtocolSessionSSQSent_Type()
)
usdCopsProtocolSessionSSQSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolSessionSSQSent.setStatus("current")
_UsdCopsProtocolSessionOPNSent_Type = Counter32
_UsdCopsProtocolSessionOPNSent_Object = MibTableColumn
usdCopsProtocolSessionOPNSent = _UsdCopsProtocolSessionOPNSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 13),
    _UsdCopsProtocolSessionOPNSent_Type()
)
usdCopsProtocolSessionOPNSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolSessionOPNSent.setStatus("current")
_UsdCopsProtocolSessionCATReceived_Type = Counter32
_UsdCopsProtocolSessionCATReceived_Object = MibTableColumn
usdCopsProtocolSessionCATReceived = _UsdCopsProtocolSessionCATReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 14),
    _UsdCopsProtocolSessionCATReceived_Type()
)
usdCopsProtocolSessionCATReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolSessionCATReceived.setStatus("current")
_UsdCopsProtocolSessionCCSent_Type = Counter32
_UsdCopsProtocolSessionCCSent_Object = MibTableColumn
usdCopsProtocolSessionCCSent = _UsdCopsProtocolSessionCCSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 15),
    _UsdCopsProtocolSessionCCSent_Type()
)
usdCopsProtocolSessionCCSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolSessionCCSent.setStatus("current")
_UsdCopsProtocolSessionCCReceived_Type = Counter32
_UsdCopsProtocolSessionCCReceived_Object = MibTableColumn
usdCopsProtocolSessionCCReceived = _UsdCopsProtocolSessionCCReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 16),
    _UsdCopsProtocolSessionCCReceived_Type()
)
usdCopsProtocolSessionCCReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolSessionCCReceived.setStatus("current")
_UsdCopsProtocolSessionSSCSent_Type = Counter32
_UsdCopsProtocolSessionSSCSent_Object = MibTableColumn
usdCopsProtocolSessionSSCSent = _UsdCopsProtocolSessionSSCSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 17),
    _UsdCopsProtocolSessionSSCSent_Type()
)
usdCopsProtocolSessionSSCSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolSessionSSCSent.setStatus("current")
_UsdCopsProtocolSessionLocalAddress_Type = IpAddress
_UsdCopsProtocolSessionLocalAddress_Object = MibTableColumn
usdCopsProtocolSessionLocalAddress = _UsdCopsProtocolSessionLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 18),
    _UsdCopsProtocolSessionLocalAddress_Type()
)
usdCopsProtocolSessionLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolSessionLocalAddress.setStatus("current")
_UsdCopsProtocolSessionTransportRouterName_Type = UsdName
_UsdCopsProtocolSessionTransportRouterName_Object = MibTableColumn
usdCopsProtocolSessionTransportRouterName = _UsdCopsProtocolSessionTransportRouterName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 19),
    _UsdCopsProtocolSessionTransportRouterName_Type()
)
usdCopsProtocolSessionTransportRouterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdCopsProtocolSessionTransportRouterName.setStatus("current")
_UsdCopsProtocolMIBConformance_ObjectIdentity = ObjectIdentity
usdCopsProtocolMIBConformance = _UsdCopsProtocolMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4)
)
_UsdCopsProtocolMIBCompliances_ObjectIdentity = ObjectIdentity
usdCopsProtocolMIBCompliances = _UsdCopsProtocolMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4, 1)
)
_UsdCopsProtocolMIBGroups_ObjectIdentity = ObjectIdentity
usdCopsProtocolMIBGroups = _UsdCopsProtocolMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4, 2)
)

# Managed Objects groups

usdCopsProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4, 2, 1)
)
usdCopsProtocolGroup.setObjects(
      *(("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionsCreated"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionsDeleted"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolCurrentSessions"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolBytesReceived"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolPacketsReceived"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolBytesSent"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolPacketsSent"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolKeepAlivesReceived"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolKeepAlivesSent"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionRemoteAddress"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionRemotePort"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionBytesReceived"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionPacketsReceived"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionBytesSent"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionPacketsSent"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionREQSent"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionDECReceived"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionRPTSent"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionDRQSent"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionSSQSent"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionOPNSent"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionCATReceived"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionCCSent"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionCCReceived"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionSSCSent"))
)
if mibBuilder.loadTexts:
    usdCopsProtocolGroup.setStatus("obsolete")

usdCopsProtocolGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4, 2, 2)
)
usdCopsProtocolGroup2.setObjects(
      *(("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionsCreated"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionsDeleted"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolCurrentSessions"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolBytesReceived"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolPacketsReceived"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolBytesSent"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolPacketsSent"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolKeepAlivesReceived"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolKeepAlivesSent"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionRemoteAddress"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionRemotePort"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionBytesReceived"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionPacketsReceived"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionBytesSent"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionPacketsSent"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionREQSent"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionDECReceived"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionRPTSent"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionDRQSent"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionSSQSent"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionOPNSent"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionCATReceived"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionCCSent"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionCCReceived"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionSSCSent"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionLocalAddress"),
        ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionTransportRouterName"))
)
if mibBuilder.loadTexts:
    usdCopsProtocolGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdCopsProtocolAuthCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdCopsProtocolAuthCompliance.setStatus(
        "obsolete"
    )

usdCopsProtocolAuthCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdCopsProtocolAuthCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-COPS-MIB",
    **{"usdCopsProtocolMIB": usdCopsProtocolMIB,
       "usdCopsProtocolObjects": usdCopsProtocolObjects,
       "usdCopsProtocolCfg": usdCopsProtocolCfg,
       "usdCopsProtocolStatus": usdCopsProtocolStatus,
       "usdCopsProtocolStatistics": usdCopsProtocolStatistics,
       "usdCopsProtocolStatisticsScalars": usdCopsProtocolStatisticsScalars,
       "usdCopsProtocolSessionsCreated": usdCopsProtocolSessionsCreated,
       "usdCopsProtocolSessionsDeleted": usdCopsProtocolSessionsDeleted,
       "usdCopsProtocolCurrentSessions": usdCopsProtocolCurrentSessions,
       "usdCopsProtocolBytesReceived": usdCopsProtocolBytesReceived,
       "usdCopsProtocolPacketsReceived": usdCopsProtocolPacketsReceived,
       "usdCopsProtocolBytesSent": usdCopsProtocolBytesSent,
       "usdCopsProtocolPacketsSent": usdCopsProtocolPacketsSent,
       "usdCopsProtocolKeepAlivesReceived": usdCopsProtocolKeepAlivesReceived,
       "usdCopsProtocolKeepAlivesSent": usdCopsProtocolKeepAlivesSent,
       "usdCopsProtocolSession": usdCopsProtocolSession,
       "usdCopsProtocolSessionTable": usdCopsProtocolSessionTable,
       "usdCopsProtocolSessionEntry": usdCopsProtocolSessionEntry,
       "usdCopsProtocolSessionClientType": usdCopsProtocolSessionClientType,
       "usdCopsProtocolSessionRemoteAddress": usdCopsProtocolSessionRemoteAddress,
       "usdCopsProtocolSessionRemotePort": usdCopsProtocolSessionRemotePort,
       "usdCopsProtocolSessionBytesReceived": usdCopsProtocolSessionBytesReceived,
       "usdCopsProtocolSessionPacketsReceived": usdCopsProtocolSessionPacketsReceived,
       "usdCopsProtocolSessionBytesSent": usdCopsProtocolSessionBytesSent,
       "usdCopsProtocolSessionPacketsSent": usdCopsProtocolSessionPacketsSent,
       "usdCopsProtocolSessionREQSent": usdCopsProtocolSessionREQSent,
       "usdCopsProtocolSessionDECReceived": usdCopsProtocolSessionDECReceived,
       "usdCopsProtocolSessionRPTSent": usdCopsProtocolSessionRPTSent,
       "usdCopsProtocolSessionDRQSent": usdCopsProtocolSessionDRQSent,
       "usdCopsProtocolSessionSSQSent": usdCopsProtocolSessionSSQSent,
       "usdCopsProtocolSessionOPNSent": usdCopsProtocolSessionOPNSent,
       "usdCopsProtocolSessionCATReceived": usdCopsProtocolSessionCATReceived,
       "usdCopsProtocolSessionCCSent": usdCopsProtocolSessionCCSent,
       "usdCopsProtocolSessionCCReceived": usdCopsProtocolSessionCCReceived,
       "usdCopsProtocolSessionSSCSent": usdCopsProtocolSessionSSCSent,
       "usdCopsProtocolSessionLocalAddress": usdCopsProtocolSessionLocalAddress,
       "usdCopsProtocolSessionTransportRouterName": usdCopsProtocolSessionTransportRouterName,
       "usdCopsProtocolMIBConformance": usdCopsProtocolMIBConformance,
       "usdCopsProtocolMIBCompliances": usdCopsProtocolMIBCompliances,
       "usdCopsProtocolAuthCompliance": usdCopsProtocolAuthCompliance,
       "usdCopsProtocolAuthCompliance2": usdCopsProtocolAuthCompliance2,
       "usdCopsProtocolMIBGroups": usdCopsProtocolMIBGroups,
       "usdCopsProtocolGroup": usdCopsProtocolGroup,
       "usdCopsProtocolGroup2": usdCopsProtocolGroup2}
)
