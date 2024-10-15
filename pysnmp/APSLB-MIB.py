# SNMP MIB module (APSLB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APSLB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:59 2024
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

(acmepacketMgmt,) = mibBuilder.importSymbols(
    "ACMEPACKET-SMI",
    "acmepacketMgmt")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetVersion,
 InetZoneIndex) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetVersion",
    "InetZoneIndex")

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

apSLBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApSLBMIBObjects_ObjectIdentity = ObjectIdentity
apSLBMIBObjects = _ApSLBMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 1)
)
_ApSLBMIBGeneralObjects_ObjectIdentity = ObjectIdentity
apSLBMIBGeneralObjects = _ApSLBMIBGeneralObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 1, 1)
)
_ApSLBStatsEndpointsCurrent_Type = Unsigned32
_ApSLBStatsEndpointsCurrent_Object = MibScalar
apSLBStatsEndpointsCurrent = _ApSLBStatsEndpointsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 1, 1, 1),
    _ApSLBStatsEndpointsCurrent_Type()
)
apSLBStatsEndpointsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSLBStatsEndpointsCurrent.setStatus("current")
if mibBuilder.loadTexts:
    apSLBStatsEndpointsCurrent.setUnits("endpoints")
_ApSLBStatsEndpointsDenied_Type = Unsigned32
_ApSLBStatsEndpointsDenied_Object = MibScalar
apSLBStatsEndpointsDenied = _ApSLBStatsEndpointsDenied_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 1, 1, 2),
    _ApSLBStatsEndpointsDenied_Type()
)
apSLBStatsEndpointsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSLBStatsEndpointsDenied.setStatus("current")
if mibBuilder.loadTexts:
    apSLBStatsEndpointsDenied.setUnits("endpoints")
_ApSLBEndpointCapacity_Type = Unsigned32
_ApSLBEndpointCapacity_Object = MibScalar
apSLBEndpointCapacity = _ApSLBEndpointCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 1, 1, 3),
    _ApSLBEndpointCapacity_Type()
)
apSLBEndpointCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSLBEndpointCapacity.setStatus("current")
if mibBuilder.loadTexts:
    apSLBEndpointCapacity.setUnits("endpoints")


class _ApSLBEndpointCapacityUpperThresh_Type(Unsigned32):
    """Custom type apSLBEndpointCapacityUpperThresh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ApSLBEndpointCapacityUpperThresh_Type.__name__ = "Unsigned32"
_ApSLBEndpointCapacityUpperThresh_Object = MibScalar
apSLBEndpointCapacityUpperThresh = _ApSLBEndpointCapacityUpperThresh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 1, 1, 4),
    _ApSLBEndpointCapacityUpperThresh_Type()
)
apSLBEndpointCapacityUpperThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSLBEndpointCapacityUpperThresh.setStatus("current")


class _ApSLBEndpointCapacityLowerThresh_Type(Unsigned32):
    """Custom type apSLBEndpointCapacityLowerThresh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ApSLBEndpointCapacityLowerThresh_Type.__name__ = "Unsigned32"
_ApSLBEndpointCapacityLowerThresh_Object = MibScalar
apSLBEndpointCapacityLowerThresh = _ApSLBEndpointCapacityLowerThresh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 1, 1, 5),
    _ApSLBEndpointCapacityLowerThresh_Type()
)
apSLBEndpointCapacityLowerThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSLBEndpointCapacityLowerThresh.setStatus("current")
_ApSLBStatsUntrustedEndpointsCurrent_Type = Unsigned32
_ApSLBStatsUntrustedEndpointsCurrent_Object = MibScalar
apSLBStatsUntrustedEndpointsCurrent = _ApSLBStatsUntrustedEndpointsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 1, 1, 6),
    _ApSLBStatsUntrustedEndpointsCurrent_Type()
)
apSLBStatsUntrustedEndpointsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSLBStatsUntrustedEndpointsCurrent.setStatus("current")
if mibBuilder.loadTexts:
    apSLBStatsUntrustedEndpointsCurrent.setUnits("endpoints")
_ApSLBStatsTrustedEndpointsCurrent_Type = Unsigned32
_ApSLBStatsTrustedEndpointsCurrent_Object = MibScalar
apSLBStatsTrustedEndpointsCurrent = _ApSLBStatsTrustedEndpointsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 1, 1, 7),
    _ApSLBStatsTrustedEndpointsCurrent_Type()
)
apSLBStatsTrustedEndpointsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSLBStatsTrustedEndpointsCurrent.setStatus("current")
if mibBuilder.loadTexts:
    apSLBStatsTrustedEndpointsCurrent.setUnits("endpoints")
_ApSLBStatsUntrustedEndpointsDenied_Type = Unsigned32
_ApSLBStatsUntrustedEndpointsDenied_Object = MibScalar
apSLBStatsUntrustedEndpointsDenied = _ApSLBStatsUntrustedEndpointsDenied_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 1, 1, 8),
    _ApSLBStatsUntrustedEndpointsDenied_Type()
)
apSLBStatsUntrustedEndpointsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSLBStatsUntrustedEndpointsDenied.setStatus("current")
if mibBuilder.loadTexts:
    apSLBStatsUntrustedEndpointsDenied.setUnits("endpoints")
_ApSLBStatsUntrustedEndpointsAgedOut_Type = Unsigned32
_ApSLBStatsUntrustedEndpointsAgedOut_Object = MibScalar
apSLBStatsUntrustedEndpointsAgedOut = _ApSLBStatsUntrustedEndpointsAgedOut_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 1, 1, 9),
    _ApSLBStatsUntrustedEndpointsAgedOut_Type()
)
apSLBStatsUntrustedEndpointsAgedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSLBStatsUntrustedEndpointsAgedOut.setStatus("current")
if mibBuilder.loadTexts:
    apSLBStatsUntrustedEndpointsAgedOut.setUnits("endpoints")
_ApSLBUntrustedEndpointCapacity_Type = Unsigned32
_ApSLBUntrustedEndpointCapacity_Object = MibScalar
apSLBUntrustedEndpointCapacity = _ApSLBUntrustedEndpointCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 1, 1, 10),
    _ApSLBUntrustedEndpointCapacity_Type()
)
apSLBUntrustedEndpointCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSLBUntrustedEndpointCapacity.setStatus("current")
if mibBuilder.loadTexts:
    apSLBUntrustedEndpointCapacity.setUnits("endpoints")


class _ApSLBUntrustedEndpointCapacityUpperThresh_Type(Unsigned32):
    """Custom type apSLBUntrustedEndpointCapacityUpperThresh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ApSLBUntrustedEndpointCapacityUpperThresh_Type.__name__ = "Unsigned32"
_ApSLBUntrustedEndpointCapacityUpperThresh_Object = MibScalar
apSLBUntrustedEndpointCapacityUpperThresh = _ApSLBUntrustedEndpointCapacityUpperThresh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 1, 1, 11),
    _ApSLBUntrustedEndpointCapacityUpperThresh_Type()
)
apSLBUntrustedEndpointCapacityUpperThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSLBUntrustedEndpointCapacityUpperThresh.setStatus("current")


class _ApSLBUntrustedEndpointCapacityLowerThresh_Type(Unsigned32):
    """Custom type apSLBUntrustedEndpointCapacityLowerThresh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ApSLBUntrustedEndpointCapacityLowerThresh_Type.__name__ = "Unsigned32"
_ApSLBUntrustedEndpointCapacityLowerThresh_Object = MibScalar
apSLBUntrustedEndpointCapacityLowerThresh = _ApSLBUntrustedEndpointCapacityLowerThresh_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 1, 1, 12),
    _ApSLBUntrustedEndpointCapacityLowerThresh_Type()
)
apSLBUntrustedEndpointCapacityLowerThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSLBUntrustedEndpointCapacityLowerThresh.setStatus("current")
_ApSLBNotificationObjects_ObjectIdentity = ObjectIdentity
apSLBNotificationObjects = _ApSLBNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 2)
)
_ApSLBNotificationPrefix_ObjectIdentity = ObjectIdentity
apSLBNotificationPrefix = _ApSLBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 3)
)
_ApSLBNotifications_ObjectIdentity = ObjectIdentity
apSLBNotifications = _ApSLBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 3, 0)
)
_ApSLBConformance_ObjectIdentity = ObjectIdentity
apSLBConformance = _ApSLBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 4)
)
_ApSLBGroups_ObjectIdentity = ObjectIdentity
apSLBGroups = _ApSLBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 4, 1)
)
_ApSLBNotificationGroups_ObjectIdentity = ObjectIdentity
apSLBNotificationGroups = _ApSLBNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 4, 2)
)

# Managed Objects groups

apSLBEndpointCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 4, 1, 1)
)
apSLBEndpointCapacityGroup.setObjects(
      *(("APSLB-MIB", "apSLBStatsEndpointsCurrent"),
        ("APSLB-MIB", "apSLBStatsEndpointsDenied"),
        ("APSLB-MIB", "apSLBEndpointCapacity"),
        ("APSLB-MIB", "apSLBEndpointCapacityUpperThresh"),
        ("APSLB-MIB", "apSLBEndpointCapacityLowerThresh"))
)
if mibBuilder.loadTexts:
    apSLBEndpointCapacityGroup.setStatus("current")

apSLBUntrustedEndpointCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 4, 1, 2)
)
apSLBUntrustedEndpointCapacityGroup.setObjects(
      *(("APSLB-MIB", "apSLBStatsUntrustedEndpointsCurrent"),
        ("APSLB-MIB", "apSLBStatsTrustedEndpointsCurrent"),
        ("APSLB-MIB", "apSLBStatsUntrustedEndpointsDenied"),
        ("APSLB-MIB", "apSLBStatsUntrustedEndpointsAgedOut"),
        ("APSLB-MIB", "apSLBUntrustedEndpointCapacity"),
        ("APSLB-MIB", "apSLBUntrustedEndpointCapacityUpperThresh"),
        ("APSLB-MIB", "apSLBUntrustedEndpointCapacityLowerThresh"))
)
if mibBuilder.loadTexts:
    apSLBUntrustedEndpointCapacityGroup.setStatus("current")


# Notification objects

apSLBEndpointCapacityThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 3, 0, 1)
)
apSLBEndpointCapacityThresholdTrap.setObjects(
      *(("APSLB-MIB", "apSLBStatsEndpointsCurrent"),
        ("APSLB-MIB", "apSLBEndpointCapacity"),
        ("APSLB-MIB", "apSLBEndpointCapacityUpperThresh"),
        ("APSLB-MIB", "apSLBEndpointCapacityLowerThresh"))
)
if mibBuilder.loadTexts:
    apSLBEndpointCapacityThresholdTrap.setStatus(
        "current"
    )

apSLBEndpointCapacityThresholdClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 3, 0, 2)
)
apSLBEndpointCapacityThresholdClearTrap.setObjects(
      *(("APSLB-MIB", "apSLBStatsEndpointsCurrent"),
        ("APSLB-MIB", "apSLBEndpointCapacity"),
        ("APSLB-MIB", "apSLBEndpointCapacityUpperThresh"),
        ("APSLB-MIB", "apSLBEndpointCapacityLowerThresh"))
)
if mibBuilder.loadTexts:
    apSLBEndpointCapacityThresholdClearTrap.setStatus(
        "current"
    )

apSLBUntrustedEndpointCapacityThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 3, 0, 3)
)
apSLBUntrustedEndpointCapacityThresholdTrap.setObjects(
      *(("APSLB-MIB", "apSLBStatsUntrustedEndpointsCurrent"),
        ("APSLB-MIB", "apSLBStatsUntrustedEndpointsDenied"),
        ("APSLB-MIB", "apSLBStatsUntrustedEndpointsAgedOut"),
        ("APSLB-MIB", "apSLBUntrustedEndpointCapacity"),
        ("APSLB-MIB", "apSLBUntrustedEndpointCapacityUpperThresh"),
        ("APSLB-MIB", "apSLBUntrustedEndpointCapacityLowerThresh"))
)
if mibBuilder.loadTexts:
    apSLBUntrustedEndpointCapacityThresholdTrap.setStatus(
        "current"
    )

apSLBUntrustedEndpointCapacityThresholdClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 3, 0, 4)
)
apSLBUntrustedEndpointCapacityThresholdClearTrap.setObjects(
      *(("APSLB-MIB", "apSLBStatsUntrustedEndpointsCurrent"),
        ("APSLB-MIB", "apSLBStatsUntrustedEndpointsDenied"),
        ("APSLB-MIB", "apSLBStatsUntrustedEndpointsAgedOut"),
        ("APSLB-MIB", "apSLBUntrustedEndpointCapacity"),
        ("APSLB-MIB", "apSLBUntrustedEndpointCapacityUpperThresh"),
        ("APSLB-MIB", "apSLBUntrustedEndpointCapacityLowerThresh"))
)
if mibBuilder.loadTexts:
    apSLBUntrustedEndpointCapacityThresholdClearTrap.setStatus(
        "current"
    )


# Notifications groups

apSLBEndpointCapacityNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 4, 2, 1)
)
apSLBEndpointCapacityNotificationsGroup.setObjects(
      *(("APSLB-MIB", "apSLBEndpointCapacityThresholdTrap"),
        ("APSLB-MIB", "apSLBEndpointCapacityThresholdClearTrap"))
)
if mibBuilder.loadTexts:
    apSLBEndpointCapacityNotificationsGroup.setStatus(
        "current"
    )

apSLBUntrustedEndpointCapacityNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 11, 4, 2, 2)
)
apSLBUntrustedEndpointCapacityNotificationsGroup.setObjects(
      *(("APSLB-MIB", "apSLBUntrustedEndpointCapacityThresholdTrap"),
        ("APSLB-MIB", "apSLBUntrustedEndpointCapacityThresholdClearTrap"))
)
if mibBuilder.loadTexts:
    apSLBUntrustedEndpointCapacityNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APSLB-MIB",
    **{"apSLBModule": apSLBModule,
       "apSLBMIBObjects": apSLBMIBObjects,
       "apSLBMIBGeneralObjects": apSLBMIBGeneralObjects,
       "apSLBStatsEndpointsCurrent": apSLBStatsEndpointsCurrent,
       "apSLBStatsEndpointsDenied": apSLBStatsEndpointsDenied,
       "apSLBEndpointCapacity": apSLBEndpointCapacity,
       "apSLBEndpointCapacityUpperThresh": apSLBEndpointCapacityUpperThresh,
       "apSLBEndpointCapacityLowerThresh": apSLBEndpointCapacityLowerThresh,
       "apSLBStatsUntrustedEndpointsCurrent": apSLBStatsUntrustedEndpointsCurrent,
       "apSLBStatsTrustedEndpointsCurrent": apSLBStatsTrustedEndpointsCurrent,
       "apSLBStatsUntrustedEndpointsDenied": apSLBStatsUntrustedEndpointsDenied,
       "apSLBStatsUntrustedEndpointsAgedOut": apSLBStatsUntrustedEndpointsAgedOut,
       "apSLBUntrustedEndpointCapacity": apSLBUntrustedEndpointCapacity,
       "apSLBUntrustedEndpointCapacityUpperThresh": apSLBUntrustedEndpointCapacityUpperThresh,
       "apSLBUntrustedEndpointCapacityLowerThresh": apSLBUntrustedEndpointCapacityLowerThresh,
       "apSLBNotificationObjects": apSLBNotificationObjects,
       "apSLBNotificationPrefix": apSLBNotificationPrefix,
       "apSLBNotifications": apSLBNotifications,
       "apSLBEndpointCapacityThresholdTrap": apSLBEndpointCapacityThresholdTrap,
       "apSLBEndpointCapacityThresholdClearTrap": apSLBEndpointCapacityThresholdClearTrap,
       "apSLBUntrustedEndpointCapacityThresholdTrap": apSLBUntrustedEndpointCapacityThresholdTrap,
       "apSLBUntrustedEndpointCapacityThresholdClearTrap": apSLBUntrustedEndpointCapacityThresholdClearTrap,
       "apSLBConformance": apSLBConformance,
       "apSLBGroups": apSLBGroups,
       "apSLBEndpointCapacityGroup": apSLBEndpointCapacityGroup,
       "apSLBUntrustedEndpointCapacityGroup": apSLBUntrustedEndpointCapacityGroup,
       "apSLBNotificationGroups": apSLBNotificationGroups,
       "apSLBEndpointCapacityNotificationsGroup": apSLBEndpointCapacityNotificationsGroup,
       "apSLBUntrustedEndpointCapacityNotificationsGroup": apSLBUntrustedEndpointCapacityNotificationsGroup}
)
