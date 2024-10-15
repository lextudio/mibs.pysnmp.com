# SNMP MIB module (ALVARION-CONNECTION-LIMITING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALVARION-CONNECTION-LIMITING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:31 2024
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

(alvarionMgmtV2,) = mibBuilder.importSymbols(
    "ALVARION-SMI",
    "alvarionMgmtV2")

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

alvarionConnectionLimitingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlvarionConnectionLimitingMIBObjects_ObjectIdentity = ObjectIdentity
alvarionConnectionLimitingMIBObjects = _AlvarionConnectionLimitingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 1)
)
_ConnectionLimitingConfig_ObjectIdentity = ObjectIdentity
connectionLimitingConfig = _ConnectionLimitingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 1, 1, 1),
    _ConnectionLimitingMaximumUserConnections_Type()
)
connectionLimitingMaximumUserConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionLimitingMaximumUserConnections.setStatus("current")
_ConnectionLimitingInfo_ObjectIdentity = ObjectIdentity
connectionLimitingInfo = _ConnectionLimitingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 1, 2)
)
_ConnectionLimitingMaximumSystemConnections_Type = Integer32
_ConnectionLimitingMaximumSystemConnections_Object = MibScalar
connectionLimitingMaximumSystemConnections = _ConnectionLimitingMaximumSystemConnections_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 1, 2, 1),
    _ConnectionLimitingMaximumSystemConnections_Type()
)
connectionLimitingMaximumSystemConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionLimitingMaximumSystemConnections.setStatus("current")
_AlvarionConnectionLimitingMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
alvarionConnectionLimitingMIBNotificationPrefix = _AlvarionConnectionLimitingMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 2)
)
_AlvarionConnectionLimitingMIBNotifications_ObjectIdentity = ObjectIdentity
alvarionConnectionLimitingMIBNotifications = _AlvarionConnectionLimitingMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 2, 0)
)
_AlvarionConnectionLimitingMIBConformance_ObjectIdentity = ObjectIdentity
alvarionConnectionLimitingMIBConformance = _AlvarionConnectionLimitingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 3)
)
_AlvarionConnectionLimitingMIBCompliances_ObjectIdentity = ObjectIdentity
alvarionConnectionLimitingMIBCompliances = _AlvarionConnectionLimitingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 3, 1)
)
_AlvarionConnectionLimitingMIBGroups_ObjectIdentity = ObjectIdentity
alvarionConnectionLimitingMIBGroups = _AlvarionConnectionLimitingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 3, 2)
)

# Managed Objects groups

alvarionConnectionLimitingConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 3, 2, 1)
)
alvarionConnectionLimitingConfigMIBGroup.setObjects(
    ("ALVARION-CONNECTION-LIMITING-MIB", "connectionLimitingMaximumUserConnections")
)
if mibBuilder.loadTexts:
    alvarionConnectionLimitingConfigMIBGroup.setStatus("current")

alvarionConnectionLimitingInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 3, 2, 2)
)
alvarionConnectionLimitingInfoMIBGroup.setObjects(
    ("ALVARION-CONNECTION-LIMITING-MIB", "connectionLimitingMaximumSystemConnections")
)
if mibBuilder.loadTexts:
    alvarionConnectionLimitingInfoMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alvarionConnectionLimitingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 3, 1, 1)
)
if mibBuilder.loadTexts:
    alvarionConnectionLimitingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALVARION-CONNECTION-LIMITING-MIB",
    **{"alvarionConnectionLimitingMIB": alvarionConnectionLimitingMIB,
       "alvarionConnectionLimitingMIBObjects": alvarionConnectionLimitingMIBObjects,
       "connectionLimitingConfig": connectionLimitingConfig,
       "connectionLimitingMaximumUserConnections": connectionLimitingMaximumUserConnections,
       "connectionLimitingInfo": connectionLimitingInfo,
       "connectionLimitingMaximumSystemConnections": connectionLimitingMaximumSystemConnections,
       "alvarionConnectionLimitingMIBNotificationPrefix": alvarionConnectionLimitingMIBNotificationPrefix,
       "alvarionConnectionLimitingMIBNotifications": alvarionConnectionLimitingMIBNotifications,
       "alvarionConnectionLimitingMIBConformance": alvarionConnectionLimitingMIBConformance,
       "alvarionConnectionLimitingMIBCompliances": alvarionConnectionLimitingMIBCompliances,
       "alvarionConnectionLimitingMIBCompliance": alvarionConnectionLimitingMIBCompliance,
       "alvarionConnectionLimitingMIBGroups": alvarionConnectionLimitingMIBGroups,
       "alvarionConnectionLimitingConfigMIBGroup": alvarionConnectionLimitingConfigMIBGroup,
       "alvarionConnectionLimitingInfoMIBGroup": alvarionConnectionLimitingInfoMIBGroup}
)
