# SNMP MIB module (COLUBRIS-CONNECTION-LIMITING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COLUBRIS-CONNECTION-LIMITING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:13 2024
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

(colubrisMgmtV2,) = mibBuilder.importSymbols(
    "COLUBRIS-SMI",
    "colubrisMgmtV2")

(ColubrisNotificationEnable,) = mibBuilder.importSymbols(
    "COLUBRIS-TC",
    "ColubrisNotificationEnable")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

colubrisConnectionLimitingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 18)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ColubrisConnectionLimitingMIBObjects_ObjectIdentity = ObjectIdentity
colubrisConnectionLimitingMIBObjects = _ColubrisConnectionLimitingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 18, 1)
)
_ConnectionLimitingConfig_ObjectIdentity = ObjectIdentity
connectionLimitingConfig = _ConnectionLimitingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 1)
)


class _ConnectionLimitingMaximumUserConnections_Type(Integer32):
    """Custom type connectionLimitingMaximumUserConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 2000),
    )


_ConnectionLimitingMaximumUserConnections_Type.__name__ = "Integer32"
_ConnectionLimitingMaximumUserConnections_Object = MibScalar
connectionLimitingMaximumUserConnections = _ConnectionLimitingMaximumUserConnections_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 1, 1),
    _ConnectionLimitingMaximumUserConnections_Type()
)
connectionLimitingMaximumUserConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionLimitingMaximumUserConnections.setStatus("current")


class _ConnectionLimitingNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type connectionLimitingNotificationEnabled based on ColubrisNotificationEnable"""


_ConnectionLimitingNotificationEnabled_Object = MibScalar
connectionLimitingNotificationEnabled = _ConnectionLimitingNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 1, 2),
    _ConnectionLimitingNotificationEnabled_Type()
)
connectionLimitingNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionLimitingNotificationEnabled.setStatus("current")
_ConnectionLimitingInfo_ObjectIdentity = ObjectIdentity
connectionLimitingInfo = _ConnectionLimitingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 2)
)
_ConnectionLimitingMaximumSystemConnections_Type = Integer32
_ConnectionLimitingMaximumSystemConnections_Object = MibScalar
connectionLimitingMaximumSystemConnections = _ConnectionLimitingMaximumSystemConnections_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 2, 1),
    _ConnectionLimitingMaximumSystemConnections_Type()
)
connectionLimitingMaximumSystemConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionLimitingMaximumSystemConnections.setStatus("current")
_ConnectionLimitingUserMACAddress_Type = MacAddress
_ConnectionLimitingUserMACAddress_Object = MibScalar
connectionLimitingUserMACAddress = _ConnectionLimitingUserMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 2, 2),
    _ConnectionLimitingUserMACAddress_Type()
)
connectionLimitingUserMACAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    connectionLimitingUserMACAddress.setStatus("current")
_ConnectionLimitingUserIPAddress_Type = IpAddress
_ConnectionLimitingUserIPAddress_Object = MibScalar
connectionLimitingUserIPAddress = _ConnectionLimitingUserIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 2, 3),
    _ConnectionLimitingUserIPAddress_Type()
)
connectionLimitingUserIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    connectionLimitingUserIPAddress.setStatus("current")
_ColubrisConnectionLimitingMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
colubrisConnectionLimitingMIBNotificationPrefix = _ColubrisConnectionLimitingMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 18, 2)
)
_ColubrisConnectionLimitingMIBNotifications_ObjectIdentity = ObjectIdentity
colubrisConnectionLimitingMIBNotifications = _ColubrisConnectionLimitingMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 18, 2, 0)
)
_ColubrisConnectionLimitingMIBConformance_ObjectIdentity = ObjectIdentity
colubrisConnectionLimitingMIBConformance = _ColubrisConnectionLimitingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 18, 3)
)
_ColubrisConnectionLimitingMIBCompliances_ObjectIdentity = ObjectIdentity
colubrisConnectionLimitingMIBCompliances = _ColubrisConnectionLimitingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 18, 3, 1)
)
_ColubrisConnectionLimitingMIBGroups_ObjectIdentity = ObjectIdentity
colubrisConnectionLimitingMIBGroups = _ColubrisConnectionLimitingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 18, 3, 2)
)

# Managed Objects groups

colubrisConnectionLimitingConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 18, 3, 2, 1)
)
colubrisConnectionLimitingConfigMIBGroup.setObjects(
      *(("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingMaximumUserConnections"),
        ("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingNotificationEnabled"))
)
if mibBuilder.loadTexts:
    colubrisConnectionLimitingConfigMIBGroup.setStatus("current")

colubrisConnectionLimitingInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 18, 3, 2, 2)
)
colubrisConnectionLimitingInfoMIBGroup.setObjects(
      *(("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingMaximumSystemConnections"),
        ("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingUserMACAddress"),
        ("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingUserIPAddress"))
)
if mibBuilder.loadTexts:
    colubrisConnectionLimitingInfoMIBGroup.setStatus("current")


# Notification objects

connectionLimitingMaximumUserConnectionsReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 18, 2, 0, 1)
)
connectionLimitingMaximumUserConnectionsReached.setObjects(
      *(("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingMaximumUserConnections"),
        ("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingUserMACAddress"),
        ("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingUserIPAddress"))
)
if mibBuilder.loadTexts:
    connectionLimitingMaximumUserConnectionsReached.setStatus(
        "current"
    )


# Notifications groups

colubrisConnectionLimitingNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 18, 3, 2, 3)
)
colubrisConnectionLimitingNotificationGroup.setObjects(
    ("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingMaximumUserConnectionsReached")
)
if mibBuilder.loadTexts:
    colubrisConnectionLimitingNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

colubrisConnectionLimitingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8744, 5, 18, 3, 1, 1)
)
if mibBuilder.loadTexts:
    colubrisConnectionLimitingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-CONNECTION-LIMITING-MIB",
    **{"colubrisConnectionLimitingMIB": colubrisConnectionLimitingMIB,
       "colubrisConnectionLimitingMIBObjects": colubrisConnectionLimitingMIBObjects,
       "connectionLimitingConfig": connectionLimitingConfig,
       "connectionLimitingMaximumUserConnections": connectionLimitingMaximumUserConnections,
       "connectionLimitingNotificationEnabled": connectionLimitingNotificationEnabled,
       "connectionLimitingInfo": connectionLimitingInfo,
       "connectionLimitingMaximumSystemConnections": connectionLimitingMaximumSystemConnections,
       "connectionLimitingUserMACAddress": connectionLimitingUserMACAddress,
       "connectionLimitingUserIPAddress": connectionLimitingUserIPAddress,
       "colubrisConnectionLimitingMIBNotificationPrefix": colubrisConnectionLimitingMIBNotificationPrefix,
       "colubrisConnectionLimitingMIBNotifications": colubrisConnectionLimitingMIBNotifications,
       "connectionLimitingMaximumUserConnectionsReached": connectionLimitingMaximumUserConnectionsReached,
       "colubrisConnectionLimitingMIBConformance": colubrisConnectionLimitingMIBConformance,
       "colubrisConnectionLimitingMIBCompliances": colubrisConnectionLimitingMIBCompliances,
       "colubrisConnectionLimitingMIBCompliance": colubrisConnectionLimitingMIBCompliance,
       "colubrisConnectionLimitingMIBGroups": colubrisConnectionLimitingMIBGroups,
       "colubrisConnectionLimitingConfigMIBGroup": colubrisConnectionLimitingConfigMIBGroup,
       "colubrisConnectionLimitingInfoMIBGroup": colubrisConnectionLimitingInfoMIBGroup,
       "colubrisConnectionLimitingNotificationGroup": colubrisConnectionLimitingNotificationGroup}
)
