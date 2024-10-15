# SNMP MIB module (ARISTA-HARDWARE-UTILIZATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARISTA-HARDWARE-UTILIZATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:21 2024
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

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

aristaHardwareUtilizationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 22)
)
aristaHardwareUtilizationMIB.setRevisions(
        ("2016-05-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AristaHardwareUtilizationMibNotifications_ObjectIdentity = ObjectIdentity
aristaHardwareUtilizationMibNotifications = _AristaHardwareUtilizationMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 22, 0)
)
_AristaHardwareUtilizationMibObjects_ObjectIdentity = ObjectIdentity
aristaHardwareUtilizationMibObjects = _AristaHardwareUtilizationMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 22, 1)
)
_AristaHardwareUtilizationTable_Object = MibTable
aristaHardwareUtilizationTable = _AristaHardwareUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 22, 1, 1)
)
if mibBuilder.loadTexts:
    aristaHardwareUtilizationTable.setStatus("current")
_AristaHardwareUtilizationEntry_Object = MibTableRow
aristaHardwareUtilizationEntry = _AristaHardwareUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 22, 1, 1, 1)
)
aristaHardwareUtilizationEntry.setIndexNames(
    (0, "ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationResource"),
    (0, "ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationFeature"),
    (0, "ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationForwardingElement"),
)
if mibBuilder.loadTexts:
    aristaHardwareUtilizationEntry.setStatus("current")


class _AristaHardwareUtilizationResource_Type(DisplayString):
    """Custom type aristaHardwareUtilizationResource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_AristaHardwareUtilizationResource_Type.__name__ = "DisplayString"
_AristaHardwareUtilizationResource_Object = MibTableColumn
aristaHardwareUtilizationResource = _AristaHardwareUtilizationResource_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 22, 1, 1, 1, 1),
    _AristaHardwareUtilizationResource_Type()
)
aristaHardwareUtilizationResource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaHardwareUtilizationResource.setStatus("current")


class _AristaHardwareUtilizationFeature_Type(DisplayString):
    """Custom type aristaHardwareUtilizationFeature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_AristaHardwareUtilizationFeature_Type.__name__ = "DisplayString"
_AristaHardwareUtilizationFeature_Object = MibTableColumn
aristaHardwareUtilizationFeature = _AristaHardwareUtilizationFeature_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 22, 1, 1, 1, 2),
    _AristaHardwareUtilizationFeature_Type()
)
aristaHardwareUtilizationFeature.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaHardwareUtilizationFeature.setStatus("current")


class _AristaHardwareUtilizationForwardingElement_Type(DisplayString):
    """Custom type aristaHardwareUtilizationForwardingElement based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_AristaHardwareUtilizationForwardingElement_Type.__name__ = "DisplayString"
_AristaHardwareUtilizationForwardingElement_Object = MibTableColumn
aristaHardwareUtilizationForwardingElement = _AristaHardwareUtilizationForwardingElement_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 22, 1, 1, 1, 3),
    _AristaHardwareUtilizationForwardingElement_Type()
)
aristaHardwareUtilizationForwardingElement.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaHardwareUtilizationForwardingElement.setStatus("current")
_AristaHardwareUtilizationInUseEntries_Type = Counter32
_AristaHardwareUtilizationInUseEntries_Object = MibTableColumn
aristaHardwareUtilizationInUseEntries = _AristaHardwareUtilizationInUseEntries_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 22, 1, 1, 1, 4),
    _AristaHardwareUtilizationInUseEntries_Type()
)
aristaHardwareUtilizationInUseEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaHardwareUtilizationInUseEntries.setStatus("current")
_AristaHardwareUtilizationFreeEntries_Type = Counter32
_AristaHardwareUtilizationFreeEntries_Object = MibTableColumn
aristaHardwareUtilizationFreeEntries = _AristaHardwareUtilizationFreeEntries_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 22, 1, 1, 1, 5),
    _AristaHardwareUtilizationFreeEntries_Type()
)
aristaHardwareUtilizationFreeEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaHardwareUtilizationFreeEntries.setStatus("current")
_AristaHardwareUtilizationCommittedEntries_Type = Counter32
_AristaHardwareUtilizationCommittedEntries_Object = MibTableColumn
aristaHardwareUtilizationCommittedEntries = _AristaHardwareUtilizationCommittedEntries_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 22, 1, 1, 1, 6),
    _AristaHardwareUtilizationCommittedEntries_Type()
)
aristaHardwareUtilizationCommittedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaHardwareUtilizationCommittedEntries.setStatus("current")
_AristaHardwareUtilizationMaxEntries_Type = Counter32
_AristaHardwareUtilizationMaxEntries_Object = MibTableColumn
aristaHardwareUtilizationMaxEntries = _AristaHardwareUtilizationMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 22, 1, 1, 1, 7),
    _AristaHardwareUtilizationMaxEntries_Type()
)
aristaHardwareUtilizationMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaHardwareUtilizationMaxEntries.setStatus("current")
_AristaHardwareUtilizationHighWatermark_Type = Counter32
_AristaHardwareUtilizationHighWatermark_Object = MibTableColumn
aristaHardwareUtilizationHighWatermark = _AristaHardwareUtilizationHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 22, 1, 1, 1, 8),
    _AristaHardwareUtilizationHighWatermark_Type()
)
aristaHardwareUtilizationHighWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaHardwareUtilizationHighWatermark.setStatus("current")
_AristaHardwareUtilizationHighWatermarkTime_Type = TimeStamp
_AristaHardwareUtilizationHighWatermarkTime_Object = MibTableColumn
aristaHardwareUtilizationHighWatermarkTime = _AristaHardwareUtilizationHighWatermarkTime_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 22, 1, 1, 1, 9),
    _AristaHardwareUtilizationHighWatermarkTime_Type()
)
aristaHardwareUtilizationHighWatermarkTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaHardwareUtilizationHighWatermarkTime.setStatus("current")
_AristaHardwareUtilizationMibConformance_ObjectIdentity = ObjectIdentity
aristaHardwareUtilizationMibConformance = _AristaHardwareUtilizationMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 22, 2)
)
_AristaHardwareUtilizationMibCompliances_ObjectIdentity = ObjectIdentity
aristaHardwareUtilizationMibCompliances = _AristaHardwareUtilizationMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 22, 2, 1)
)
_AristaHardwareUtilizationMibGroups_ObjectIdentity = ObjectIdentity
aristaHardwareUtilizationMibGroups = _AristaHardwareUtilizationMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 22, 2, 2)
)

# Managed Objects groups

aristaHardwareUtilizationTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 22, 2, 2, 1)
)
aristaHardwareUtilizationTableGroup.setObjects(
      *(("ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationInUseEntries"),
        ("ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationFreeEntries"),
        ("ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationCommittedEntries"),
        ("ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationMaxEntries"),
        ("ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationHighWatermark"),
        ("ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationHighWatermarkTime"))
)
if mibBuilder.loadTexts:
    aristaHardwareUtilizationTableGroup.setStatus("current")


# Notification objects

aristaHardwareUtilizationAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 30065, 3, 22, 0, 1)
)
aristaHardwareUtilizationAlert.setObjects(
      *(("ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationInUseEntries"),
        ("ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationHighWatermark"),
        ("ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationHighWatermarkTime"))
)
if mibBuilder.loadTexts:
    aristaHardwareUtilizationAlert.setStatus(
        "current"
    )


# Notifications groups

aristaHardwareUtilizationNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 22, 2, 2, 2)
)
aristaHardwareUtilizationNotificationsGroup.setObjects(
    ("ARISTA-HARDWARE-UTILIZATION-MIB", "aristaHardwareUtilizationAlert")
)
if mibBuilder.loadTexts:
    aristaHardwareUtilizationNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aristaHardwareUtilizationMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 22, 2, 1, 1)
)
if mibBuilder.loadTexts:
    aristaHardwareUtilizationMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-HARDWARE-UTILIZATION-MIB",
    **{"aristaHardwareUtilizationMIB": aristaHardwareUtilizationMIB,
       "aristaHardwareUtilizationMibNotifications": aristaHardwareUtilizationMibNotifications,
       "aristaHardwareUtilizationAlert": aristaHardwareUtilizationAlert,
       "aristaHardwareUtilizationMibObjects": aristaHardwareUtilizationMibObjects,
       "aristaHardwareUtilizationTable": aristaHardwareUtilizationTable,
       "aristaHardwareUtilizationEntry": aristaHardwareUtilizationEntry,
       "aristaHardwareUtilizationResource": aristaHardwareUtilizationResource,
       "aristaHardwareUtilizationFeature": aristaHardwareUtilizationFeature,
       "aristaHardwareUtilizationForwardingElement": aristaHardwareUtilizationForwardingElement,
       "aristaHardwareUtilizationInUseEntries": aristaHardwareUtilizationInUseEntries,
       "aristaHardwareUtilizationFreeEntries": aristaHardwareUtilizationFreeEntries,
       "aristaHardwareUtilizationCommittedEntries": aristaHardwareUtilizationCommittedEntries,
       "aristaHardwareUtilizationMaxEntries": aristaHardwareUtilizationMaxEntries,
       "aristaHardwareUtilizationHighWatermark": aristaHardwareUtilizationHighWatermark,
       "aristaHardwareUtilizationHighWatermarkTime": aristaHardwareUtilizationHighWatermarkTime,
       "aristaHardwareUtilizationMibConformance": aristaHardwareUtilizationMibConformance,
       "aristaHardwareUtilizationMibCompliances": aristaHardwareUtilizationMibCompliances,
       "aristaHardwareUtilizationMibCompliance": aristaHardwareUtilizationMibCompliance,
       "aristaHardwareUtilizationMibGroups": aristaHardwareUtilizationMibGroups,
       "aristaHardwareUtilizationTableGroup": aristaHardwareUtilizationTableGroup,
       "aristaHardwareUtilizationNotificationsGroup": aristaHardwareUtilizationNotificationsGroup}
)
