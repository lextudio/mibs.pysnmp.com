# SNMP MIB module (SALIX-MGMCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SALIX-MGMCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:31 2024
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

(platform1,) = mibBuilder.importSymbols(
    "SALIX-MIB",
    "platform1")

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

salixMgmcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SalixMgmcpMIBObjects_ObjectIdentity = ObjectIdentity
salixMgmcpMIBObjects = _SalixMgmcpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1)
)
_SalixMgmcpIpdcObjects_ObjectIdentity = ObjectIdentity
salixMgmcpIpdcObjects = _SalixMgmcpIpdcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 1)
)
_IpdcSessionTable_Object = MibTable
ipdcSessionTable = _IpdcSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ipdcSessionTable.setStatus("current")
_IpdcSessionEntry_Object = MibTableRow
ipdcSessionEntry = _IpdcSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 1, 1, 1)
)
ipdcSessionEntry.setIndexNames(
    (0, "SALIX-MGMCP-MIB", "ipdcSessionIndex"),
)
if mibBuilder.loadTexts:
    ipdcSessionEntry.setStatus("current")
_IpdcSessionIndex_Type = Integer32
_IpdcSessionIndex_Object = MibTableColumn
ipdcSessionIndex = _IpdcSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 1, 1, 1, 1),
    _IpdcSessionIndex_Type()
)
ipdcSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipdcSessionIndex.setStatus("current")
_IpdcSessionLocalIpAddress_Type = IpAddress
_IpdcSessionLocalIpAddress_Object = MibTableColumn
ipdcSessionLocalIpAddress = _IpdcSessionLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 1, 1, 1, 2),
    _IpdcSessionLocalIpAddress_Type()
)
ipdcSessionLocalIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipdcSessionLocalIpAddress.setStatus("current")


class _IpdcSessionLocalPort_Type(Integer32):
    """Custom type ipdcSessionLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpdcSessionLocalPort_Type.__name__ = "Integer32"
_IpdcSessionLocalPort_Object = MibTableColumn
ipdcSessionLocalPort = _IpdcSessionLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 1, 1, 1, 3),
    _IpdcSessionLocalPort_Type()
)
ipdcSessionLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipdcSessionLocalPort.setStatus("current")
_IpdcSessionMediaControllerIpAddress_Type = IpAddress
_IpdcSessionMediaControllerIpAddress_Object = MibTableColumn
ipdcSessionMediaControllerIpAddress = _IpdcSessionMediaControllerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 1, 1, 1, 4),
    _IpdcSessionMediaControllerIpAddress_Type()
)
ipdcSessionMediaControllerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipdcSessionMediaControllerIpAddress.setStatus("current")


class _IpdcSessionMediaControllerPort_Type(Integer32):
    """Custom type ipdcSessionMediaControllerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpdcSessionMediaControllerPort_Type.__name__ = "Integer32"
_IpdcSessionMediaControllerPort_Object = MibTableColumn
ipdcSessionMediaControllerPort = _IpdcSessionMediaControllerPort_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 1, 1, 1, 5),
    _IpdcSessionMediaControllerPort_Type()
)
ipdcSessionMediaControllerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipdcSessionMediaControllerPort.setStatus("current")
_IpdcSessionStatsTable_Object = MibTable
ipdcSessionStatsTable = _IpdcSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ipdcSessionStatsTable.setStatus("current")
_IpdcSessionStatsEntry_Object = MibTableRow
ipdcSessionStatsEntry = _IpdcSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 1, 2, 1)
)
ipdcSessionStatsEntry.setIndexNames(
    (0, "SALIX-MGMCP-MIB", "ipdcSessionIndex"),
)
if mibBuilder.loadTexts:
    ipdcSessionStatsEntry.setStatus("current")
_IpdcSessionStatsPacketsRcvd_Type = Counter32
_IpdcSessionStatsPacketsRcvd_Object = MibTableColumn
ipdcSessionStatsPacketsRcvd = _IpdcSessionStatsPacketsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 1, 2, 1, 2),
    _IpdcSessionStatsPacketsRcvd_Type()
)
ipdcSessionStatsPacketsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipdcSessionStatsPacketsRcvd.setStatus("current")
_IpdcSessionStatsPacketsSent_Type = Counter32
_IpdcSessionStatsPacketsSent_Object = MibTableColumn
ipdcSessionStatsPacketsSent = _IpdcSessionStatsPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 1, 2, 1, 3),
    _IpdcSessionStatsPacketsSent_Type()
)
ipdcSessionStatsPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipdcSessionStatsPacketsSent.setStatus("current")
_IpdcSessionStatsBytesRcvd_Type = Counter32
_IpdcSessionStatsBytesRcvd_Object = MibTableColumn
ipdcSessionStatsBytesRcvd = _IpdcSessionStatsBytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 1, 2, 1, 4),
    _IpdcSessionStatsBytesRcvd_Type()
)
ipdcSessionStatsBytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipdcSessionStatsBytesRcvd.setStatus("current")
_IpdcSessionStatsBytesSent_Type = Counter32
_IpdcSessionStatsBytesSent_Object = MibTableColumn
ipdcSessionStatsBytesSent = _IpdcSessionStatsBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 1, 2, 1, 5),
    _IpdcSessionStatsBytesSent_Type()
)
ipdcSessionStatsBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipdcSessionStatsBytesSent.setStatus("current")
_IpdcSessionStatsMessagesRejected_Type = Counter32
_IpdcSessionStatsMessagesRejected_Object = MibTableColumn
ipdcSessionStatsMessagesRejected = _IpdcSessionStatsMessagesRejected_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 1, 2, 1, 6),
    _IpdcSessionStatsMessagesRejected_Type()
)
ipdcSessionStatsMessagesRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipdcSessionStatsMessagesRejected.setStatus("current")
_IpdcSessionStatsUnacknowledgedRequests_Type = Counter32
_IpdcSessionStatsUnacknowledgedRequests_Object = MibTableColumn
ipdcSessionStatsUnacknowledgedRequests = _IpdcSessionStatsUnacknowledgedRequests_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 1, 2, 1, 7),
    _IpdcSessionStatsUnacknowledgedRequests_Type()
)
ipdcSessionStatsUnacknowledgedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipdcSessionStatsUnacknowledgedRequests.setStatus("current")


class _IpdcSystemType_Type(DisplayString):
    """Custom type ipdcSystemType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_IpdcSystemType_Type.__name__ = "DisplayString"
_IpdcSystemType_Object = MibScalar
ipdcSystemType = _IpdcSystemType_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 1, 3),
    _IpdcSystemType_Type()
)
ipdcSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipdcSystemType.setStatus("current")


class _IpdcSystemID_Type(DisplayString):
    """Custom type ipdcSystemID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_IpdcSystemID_Type.__name__ = "DisplayString"
_IpdcSystemID_Object = MibScalar
ipdcSystemID = _IpdcSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 1, 4),
    _IpdcSystemID_Type()
)
ipdcSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipdcSystemID.setStatus("current")


class _IpdcBayNumber_Type(DisplayString):
    """Custom type ipdcBayNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IpdcBayNumber_Type.__name__ = "DisplayString"
_IpdcBayNumber_Object = MibScalar
ipdcBayNumber = _IpdcBayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 1, 5),
    _IpdcBayNumber_Type()
)
ipdcBayNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipdcBayNumber.setStatus("current")
_IpdcHeartbeatObjects_ObjectIdentity = ObjectIdentity
ipdcHeartbeatObjects = _IpdcHeartbeatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 1, 6)
)
_IpdcHeartbeatFrequency_Type = Integer32
_IpdcHeartbeatFrequency_Object = MibScalar
ipdcHeartbeatFrequency = _IpdcHeartbeatFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 1, 6, 1),
    _IpdcHeartbeatFrequency_Type()
)
ipdcHeartbeatFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipdcHeartbeatFrequency.setStatus("current")


class _IpdcHeartbeatPrimaryEnable_Type(Integer32):
    """Custom type ipdcHeartbeatPrimaryEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpdcHeartbeatPrimaryEnable_Type.__name__ = "Integer32"
_IpdcHeartbeatPrimaryEnable_Object = MibScalar
ipdcHeartbeatPrimaryEnable = _IpdcHeartbeatPrimaryEnable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 1, 6, 2),
    _IpdcHeartbeatPrimaryEnable_Type()
)
ipdcHeartbeatPrimaryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipdcHeartbeatPrimaryEnable.setStatus("current")


class _IpdcHeartbeatSecondaryEnable_Type(Integer32):
    """Custom type ipdcHeartbeatSecondaryEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpdcHeartbeatSecondaryEnable_Type.__name__ = "Integer32"
_IpdcHeartbeatSecondaryEnable_Object = MibScalar
ipdcHeartbeatSecondaryEnable = _IpdcHeartbeatSecondaryEnable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 1, 6, 3),
    _IpdcHeartbeatSecondaryEnable_Type()
)
ipdcHeartbeatSecondaryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipdcHeartbeatSecondaryEnable.setStatus("current")
_IpdcLoggerObjects_ObjectIdentity = ObjectIdentity
ipdcLoggerObjects = _IpdcLoggerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 1, 7)
)


class _IpdcLoggerEnable_Type(Integer32):
    """Custom type ipdcLoggerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpdcLoggerEnable_Type.__name__ = "Integer32"
_IpdcLoggerEnable_Object = MibScalar
ipdcLoggerEnable = _IpdcLoggerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 1, 7, 1),
    _IpdcLoggerEnable_Type()
)
ipdcLoggerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipdcLoggerEnable.setStatus("current")
_SalixMgmcpSgcpObjects_ObjectIdentity = ObjectIdentity
salixMgmcpSgcpObjects = _SalixMgmcpSgcpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 2)
)


class _SgcpUdpPortNumber_Type(Integer32):
    """Custom type sgcpUdpPortNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SgcpUdpPortNumber_Type.__name__ = "Integer32"
_SgcpUdpPortNumber_Object = MibScalar
sgcpUdpPortNumber = _SgcpUdpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 1, 2, 1),
    _SgcpUdpPortNumber_Type()
)
sgcpUdpPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sgcpUdpPortNumber.setStatus("current")
_SalixMgmcpMIBTraps_ObjectIdentity = ObjectIdentity
salixMgmcpMIBTraps = _SalixMgmcpMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 2)
)
_SalixMgmcpMIBTrapPrefix_ObjectIdentity = ObjectIdentity
salixMgmcpMIBTrapPrefix = _SalixMgmcpMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 2, 0)
)
_SalixMgmcpMIBCompliance_ObjectIdentity = ObjectIdentity
salixMgmcpMIBCompliance = _SalixMgmcpMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 3)
)
_IpdcGroups_ObjectIdentity = ObjectIdentity
ipdcGroups = _IpdcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 3, 1)
)
_SgcpGroups_ObjectIdentity = ObjectIdentity
sgcpGroups = _SgcpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 3, 2)
)
_IpdcCompliances_ObjectIdentity = ObjectIdentity
ipdcCompliances = _IpdcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 3, 3)
)
_SgcpCompliances_ObjectIdentity = ObjectIdentity
sgcpCompliances = _SgcpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 3, 4)
)

# Managed Objects groups

ipdcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 3, 1, 1)
)
ipdcGroup.setObjects(
      *(("SALIX-MGMCP-MIB", "ipdcSessionStatsPacketsRcvd"),
        ("SALIX-MGMCP-MIB", "ipdcSessionStatsPacketsSent"),
        ("SALIX-MGMCP-MIB", "ipdcSessionStatsBytesRcvd"),
        ("SALIX-MGMCP-MIB", "ipdcSessionStatsBytesSent"),
        ("SALIX-MGMCP-MIB", "ipdcSessionStatsMessagesRejected"),
        ("SALIX-MGMCP-MIB", "ipdcSessionLocalIpAddress"),
        ("SALIX-MGMCP-MIB", "ipdcSessionLocalPort"),
        ("SALIX-MGMCP-MIB", "ipdcSessionMediaControllerIpAddress"),
        ("SALIX-MGMCP-MIB", "ipdcSessionMediaControllerPort"))
)
if mibBuilder.loadTexts:
    ipdcGroup.setStatus("current")

sgcpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 3, 2, 2)
)
sgcpGroup.setObjects(
    ("SALIX-MGMCP-MIB", "sgcpUdpPortNumber")
)
if mibBuilder.loadTexts:
    sgcpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ipdcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    ipdcCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SALIX-MGMCP-MIB",
    **{"salixMgmcpMIB": salixMgmcpMIB,
       "salixMgmcpMIBObjects": salixMgmcpMIBObjects,
       "salixMgmcpIpdcObjects": salixMgmcpIpdcObjects,
       "ipdcSessionTable": ipdcSessionTable,
       "ipdcSessionEntry": ipdcSessionEntry,
       "ipdcSessionIndex": ipdcSessionIndex,
       "ipdcSessionLocalIpAddress": ipdcSessionLocalIpAddress,
       "ipdcSessionLocalPort": ipdcSessionLocalPort,
       "ipdcSessionMediaControllerIpAddress": ipdcSessionMediaControllerIpAddress,
       "ipdcSessionMediaControllerPort": ipdcSessionMediaControllerPort,
       "ipdcSessionStatsTable": ipdcSessionStatsTable,
       "ipdcSessionStatsEntry": ipdcSessionStatsEntry,
       "ipdcSessionStatsPacketsRcvd": ipdcSessionStatsPacketsRcvd,
       "ipdcSessionStatsPacketsSent": ipdcSessionStatsPacketsSent,
       "ipdcSessionStatsBytesRcvd": ipdcSessionStatsBytesRcvd,
       "ipdcSessionStatsBytesSent": ipdcSessionStatsBytesSent,
       "ipdcSessionStatsMessagesRejected": ipdcSessionStatsMessagesRejected,
       "ipdcSessionStatsUnacknowledgedRequests": ipdcSessionStatsUnacknowledgedRequests,
       "ipdcSystemType": ipdcSystemType,
       "ipdcSystemID": ipdcSystemID,
       "ipdcBayNumber": ipdcBayNumber,
       "ipdcHeartbeatObjects": ipdcHeartbeatObjects,
       "ipdcHeartbeatFrequency": ipdcHeartbeatFrequency,
       "ipdcHeartbeatPrimaryEnable": ipdcHeartbeatPrimaryEnable,
       "ipdcHeartbeatSecondaryEnable": ipdcHeartbeatSecondaryEnable,
       "ipdcLoggerObjects": ipdcLoggerObjects,
       "ipdcLoggerEnable": ipdcLoggerEnable,
       "salixMgmcpSgcpObjects": salixMgmcpSgcpObjects,
       "sgcpUdpPortNumber": sgcpUdpPortNumber,
       "salixMgmcpMIBTraps": salixMgmcpMIBTraps,
       "salixMgmcpMIBTrapPrefix": salixMgmcpMIBTrapPrefix,
       "salixMgmcpMIBCompliance": salixMgmcpMIBCompliance,
       "ipdcGroups": ipdcGroups,
       "ipdcGroup": ipdcGroup,
       "sgcpGroups": sgcpGroups,
       "sgcpGroup": sgcpGroup,
       "ipdcCompliances": ipdcCompliances,
       "ipdcCompliance": ipdcCompliance,
       "sgcpCompliances": sgcpCompliances}
)
