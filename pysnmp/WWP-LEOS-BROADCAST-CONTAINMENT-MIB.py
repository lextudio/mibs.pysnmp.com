# SNMP MIB module (WWP-LEOS-BROADCAST-CONTAINMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-BROADCAST-CONTAINMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:46 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosBroadcastContainmentMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8)
)
wwpLeosBroadcastContainmentMIB.setRevisions(
        ("2012-03-08 00:00",
         "2012-03-02 00:00",
         "2009-02-05 00:00",
         "2008-06-25 00:00",
         "2008-06-18 21:00",
         "2007-06-02 21:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class WwpLeosBroadcastContainmentCapabilitiesMap(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_WwpLeosBroadcastContainmentMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosBroadcastContainmentMIBObjects = _WwpLeosBroadcastContainmentMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 1)
)
_WwpLeosBroadcastContainmentCapability_Type = WwpLeosBroadcastContainmentCapabilitiesMap
_WwpLeosBroadcastContainmentCapability_Object = MibScalar
wwpLeosBroadcastContainmentCapability = _WwpLeosBroadcastContainmentCapability_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 1, 1),
    _WwpLeosBroadcastContainmentCapability_Type()
)
wwpLeosBroadcastContainmentCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBroadcastContainmentCapability.setStatus("current")
_WwpLeosBroadcastContainmentPktDroppedStats_Type = Counter32
_WwpLeosBroadcastContainmentPktDroppedStats_Object = MibScalar
wwpLeosBroadcastContainmentPktDroppedStats = _WwpLeosBroadcastContainmentPktDroppedStats_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 1, 2),
    _WwpLeosBroadcastContainmentPktDroppedStats_Type()
)
wwpLeosBroadcastContainmentPktDroppedStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBroadcastContainmentPktDroppedStats.setStatus("current")
_WwpLeosBroadcastContainmentFilterTable_Object = MibTable
wwpLeosBroadcastContainmentFilterTable = _WwpLeosBroadcastContainmentFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 1, 4)
)
if mibBuilder.loadTexts:
    wwpLeosBroadcastContainmentFilterTable.setStatus("current")
_WwpLeosBroadcastContainmentFilterEntry_Object = MibTableRow
wwpLeosBroadcastContainmentFilterEntry = _WwpLeosBroadcastContainmentFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 1, 4, 1)
)
wwpLeosBroadcastContainmentFilterEntry.setIndexNames(
    (0, "WWP-LEOS-BROADCAST-CONTAINMENT-MIB", "wwpLeosBroadcastContainmentIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosBroadcastContainmentFilterEntry.setStatus("current")


class _WwpLeosBroadcastContainmentIndex_Type(Integer32):
    """Custom type wwpLeosBroadcastContainmentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_WwpLeosBroadcastContainmentIndex_Type.__name__ = "Integer32"
_WwpLeosBroadcastContainmentIndex_Object = MibTableColumn
wwpLeosBroadcastContainmentIndex = _WwpLeosBroadcastContainmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 1, 4, 1, 1),
    _WwpLeosBroadcastContainmentIndex_Type()
)
wwpLeosBroadcastContainmentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBroadcastContainmentIndex.setStatus("current")


class _WwpLeosBroadcastContainmentFilterName_Type(DisplayString):
    """Custom type wwpLeosBroadcastContainmentFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_WwpLeosBroadcastContainmentFilterName_Type.__name__ = "DisplayString"
_WwpLeosBroadcastContainmentFilterName_Object = MibTableColumn
wwpLeosBroadcastContainmentFilterName = _WwpLeosBroadcastContainmentFilterName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 1, 4, 1, 2),
    _WwpLeosBroadcastContainmentFilterName_Type()
)
wwpLeosBroadcastContainmentFilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosBroadcastContainmentFilterName.setStatus("current")


class _WwpLeosBroadcastContainmentPktLimit_Type(Integer32):
    """Custom type wwpLeosBroadcastContainmentPktLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 104856000),
    )


_WwpLeosBroadcastContainmentPktLimit_Type.__name__ = "Integer32"
_WwpLeosBroadcastContainmentPktLimit_Object = MibTableColumn
wwpLeosBroadcastContainmentPktLimit = _WwpLeosBroadcastContainmentPktLimit_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 1, 4, 1, 3),
    _WwpLeosBroadcastContainmentPktLimit_Type()
)
wwpLeosBroadcastContainmentPktLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosBroadcastContainmentPktLimit.setStatus("current")
_WwpLeosBroadcastContainmentPktDropState_Type = TruthValue
_WwpLeosBroadcastContainmentPktDropState_Object = MibTableColumn
wwpLeosBroadcastContainmentPktDropState = _WwpLeosBroadcastContainmentPktDropState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 1, 4, 1, 4),
    _WwpLeosBroadcastContainmentPktDropState_Type()
)
wwpLeosBroadcastContainmentPktDropState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBroadcastContainmentPktDropState.setStatus("current")
_WwpLeosBroadcastContainmentStatus_Type = RowStatus
_WwpLeosBroadcastContainmentStatus_Object = MibTableColumn
wwpLeosBroadcastContainmentStatus = _WwpLeosBroadcastContainmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 1, 4, 1, 5),
    _WwpLeosBroadcastContainmentStatus_Type()
)
wwpLeosBroadcastContainmentStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosBroadcastContainmentStatus.setStatus("current")


class _WwpLeosBroadcastContainmentKbps_Type(Integer32):
    """Custom type wwpLeosBroadcastContainmentKbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_WwpLeosBroadcastContainmentKbps_Type.__name__ = "Integer32"
_WwpLeosBroadcastContainmentKbps_Object = MibTableColumn
wwpLeosBroadcastContainmentKbps = _WwpLeosBroadcastContainmentKbps_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 1, 4, 1, 6),
    _WwpLeosBroadcastContainmentKbps_Type()
)
wwpLeosBroadcastContainmentKbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosBroadcastContainmentKbps.setStatus("current")


class _WwpLeosBroadcastContainmentClassifier_Type(Unsigned32):
    """Custom type wwpLeosBroadcastContainmentClassifier based on Unsigned32"""
    defaultValue = 3


_WwpLeosBroadcastContainmentClassifier_Object = MibTableColumn
wwpLeosBroadcastContainmentClassifier = _WwpLeosBroadcastContainmentClassifier_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 1, 4, 1, 7),
    _WwpLeosBroadcastContainmentClassifier_Type()
)
wwpLeosBroadcastContainmentClassifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosBroadcastContainmentClassifier.setStatus("current")
_WwpLeosBroadcastContainmentFilterMemTable_Object = MibTable
wwpLeosBroadcastContainmentFilterMemTable = _WwpLeosBroadcastContainmentFilterMemTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 1, 5)
)
if mibBuilder.loadTexts:
    wwpLeosBroadcastContainmentFilterMemTable.setStatus("current")
_WwpLeosBroadcastContainmentFilterMemEntry_Object = MibTableRow
wwpLeosBroadcastContainmentFilterMemEntry = _WwpLeosBroadcastContainmentFilterMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 1, 5, 1)
)
wwpLeosBroadcastContainmentFilterMemEntry.setIndexNames(
    (0, "WWP-LEOS-BROADCAST-CONTAINMENT-MIB", "wwpLeosBroadcastContainmentIndex"),
    (0, "WWP-LEOS-BROADCAST-CONTAINMENT-MIB", "wwpLeosBroadcastContainmentVlanId"),
    (0, "WWP-LEOS-BROADCAST-CONTAINMENT-MIB", "wwpLeosBroadcastContainmentPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosBroadcastContainmentFilterMemEntry.setStatus("current")


class _WwpLeosBroadcastContainmentVlanId_Type(Integer32):
    """Custom type wwpLeosBroadcastContainmentVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WwpLeosBroadcastContainmentVlanId_Type.__name__ = "Integer32"
_WwpLeosBroadcastContainmentVlanId_Object = MibTableColumn
wwpLeosBroadcastContainmentVlanId = _WwpLeosBroadcastContainmentVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 1, 5, 1, 1),
    _WwpLeosBroadcastContainmentVlanId_Type()
)
wwpLeosBroadcastContainmentVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosBroadcastContainmentVlanId.setStatus("current")


class _WwpLeosBroadcastContainmentPortId_Type(Integer32):
    """Custom type wwpLeosBroadcastContainmentPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WwpLeosBroadcastContainmentPortId_Type.__name__ = "Integer32"
_WwpLeosBroadcastContainmentPortId_Object = MibTableColumn
wwpLeosBroadcastContainmentPortId = _WwpLeosBroadcastContainmentPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 1, 5, 1, 2),
    _WwpLeosBroadcastContainmentPortId_Type()
)
wwpLeosBroadcastContainmentPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosBroadcastContainmentPortId.setStatus("current")
_WwpLeosBroadcastContainmentFilterMemStatus_Type = RowStatus
_WwpLeosBroadcastContainmentFilterMemStatus_Object = MibTableColumn
wwpLeosBroadcastContainmentFilterMemStatus = _WwpLeosBroadcastContainmentFilterMemStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 1, 5, 1, 3),
    _WwpLeosBroadcastContainmentFilterMemStatus_Type()
)
wwpLeosBroadcastContainmentFilterMemStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosBroadcastContainmentFilterMemStatus.setStatus("current")


class _WwpLeosBroadcastContainmentGlobalStatus_Type(Integer32):
    """Custom type wwpLeosBroadcastContainmentGlobalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WwpLeosBroadcastContainmentGlobalStatus_Type.__name__ = "Integer32"
_WwpLeosBroadcastContainmentGlobalStatus_Object = MibScalar
wwpLeosBroadcastContainmentGlobalStatus = _WwpLeosBroadcastContainmentGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 1, 6),
    _WwpLeosBroadcastContainmentGlobalStatus_Type()
)
wwpLeosBroadcastContainmentGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBroadcastContainmentGlobalStatus.setStatus("current")


class _WwpLeosBroadcastContainmentGlobalTime_Type(Integer32):
    """Custom type wwpLeosBroadcastContainmentGlobalTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2560),
    )


_WwpLeosBroadcastContainmentGlobalTime_Type.__name__ = "Integer32"
_WwpLeosBroadcastContainmentGlobalTime_Object = MibScalar
wwpLeosBroadcastContainmentGlobalTime = _WwpLeosBroadcastContainmentGlobalTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 1, 7),
    _WwpLeosBroadcastContainmentGlobalTime_Type()
)
wwpLeosBroadcastContainmentGlobalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBroadcastContainmentGlobalTime.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosBroadcastContainmentGlobalTime.setUnits("milli-seconds")


class _WwpLeosBroadcastContainmentIgnoreRapsMessages_Type(Integer32):
    """Custom type wwpLeosBroadcastContainmentIgnoreRapsMessages based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WwpLeosBroadcastContainmentIgnoreRapsMessages_Type.__name__ = "Integer32"
_WwpLeosBroadcastContainmentIgnoreRapsMessages_Object = MibScalar
wwpLeosBroadcastContainmentIgnoreRapsMessages = _WwpLeosBroadcastContainmentIgnoreRapsMessages_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 1, 8),
    _WwpLeosBroadcastContainmentIgnoreRapsMessages_Type()
)
wwpLeosBroadcastContainmentIgnoreRapsMessages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBroadcastContainmentIgnoreRapsMessages.setStatus("current")


class _WwpLeosBroadcastContainmentResourceMode_Type(Integer32):
    """Custom type wwpLeosBroadcastContainmentResourceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WwpLeosBroadcastContainmentResourceMode_Type.__name__ = "Integer32"
_WwpLeosBroadcastContainmentResourceMode_Object = MibScalar
wwpLeosBroadcastContainmentResourceMode = _WwpLeosBroadcastContainmentResourceMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 1, 9),
    _WwpLeosBroadcastContainmentResourceMode_Type()
)
wwpLeosBroadcastContainmentResourceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBroadcastContainmentResourceMode.setStatus("current")
_WwpLeosBroadcastContainmentBytesDroppedStats_Type = Counter64
_WwpLeosBroadcastContainmentBytesDroppedStats_Object = MibScalar
wwpLeosBroadcastContainmentBytesDroppedStats = _WwpLeosBroadcastContainmentBytesDroppedStats_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 1, 10),
    _WwpLeosBroadcastContainmentBytesDroppedStats_Type()
)
wwpLeosBroadcastContainmentBytesDroppedStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBroadcastContainmentBytesDroppedStats.setStatus("current")
_WwpLeosBroadcastContainmentMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosBroadcastContainmentMIBNotificationPrefix = _WwpLeosBroadcastContainmentMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 2)
)
_WwpLeosBroadcastContainmentMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosBroadcastContainmentMIBNotifications = _WwpLeosBroadcastContainmentMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 2, 1)
)
_WwpLeosBroadcastContainmentMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosBroadcastContainmentMIBConformance = _WwpLeosBroadcastContainmentMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 3)
)
_WwpLeosBroadcastContainmentMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosBroadcastContainmentMIBCompliances = _WwpLeosBroadcastContainmentMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 3, 1)
)
_WwpLeosBroadcastContainmentMIGroups_ObjectIdentity = ObjectIdentity
wwpLeosBroadcastContainmentMIGroups = _WwpLeosBroadcastContainmentMIGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 3, 2)
)

# Managed Objects groups


# Notification objects

wwpLeosBcastThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 2, 1, 1)
)
wwpLeosBcastThresholdExceed.setObjects(
      *(("WWP-LEOS-BROADCAST-CONTAINMENT-MIB", "wwpLeosBroadcastContainmentIndex"),
        ("WWP-LEOS-BROADCAST-CONTAINMENT-MIB", "wwpLeosBroadcastContainmentFilterName"))
)
if mibBuilder.loadTexts:
    wwpLeosBcastThresholdExceed.setStatus(
        "current"
    )

wwpLeosBcastThresholdNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 8, 2, 1, 2)
)
wwpLeosBcastThresholdNormal.setObjects(
      *(("WWP-LEOS-BROADCAST-CONTAINMENT-MIB", "wwpLeosBroadcastContainmentIndex"),
        ("WWP-LEOS-BROADCAST-CONTAINMENT-MIB", "wwpLeosBroadcastContainmentFilterName"))
)
if mibBuilder.loadTexts:
    wwpLeosBcastThresholdNormal.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-BROADCAST-CONTAINMENT-MIB",
    **{"WwpLeosBroadcastContainmentCapabilitiesMap": WwpLeosBroadcastContainmentCapabilitiesMap,
       "wwpLeosBroadcastContainmentMIB": wwpLeosBroadcastContainmentMIB,
       "wwpLeosBroadcastContainmentMIBObjects": wwpLeosBroadcastContainmentMIBObjects,
       "wwpLeosBroadcastContainmentCapability": wwpLeosBroadcastContainmentCapability,
       "wwpLeosBroadcastContainmentPktDroppedStats": wwpLeosBroadcastContainmentPktDroppedStats,
       "wwpLeosBroadcastContainmentFilterTable": wwpLeosBroadcastContainmentFilterTable,
       "wwpLeosBroadcastContainmentFilterEntry": wwpLeosBroadcastContainmentFilterEntry,
       "wwpLeosBroadcastContainmentIndex": wwpLeosBroadcastContainmentIndex,
       "wwpLeosBroadcastContainmentFilterName": wwpLeosBroadcastContainmentFilterName,
       "wwpLeosBroadcastContainmentPktLimit": wwpLeosBroadcastContainmentPktLimit,
       "wwpLeosBroadcastContainmentPktDropState": wwpLeosBroadcastContainmentPktDropState,
       "wwpLeosBroadcastContainmentStatus": wwpLeosBroadcastContainmentStatus,
       "wwpLeosBroadcastContainmentKbps": wwpLeosBroadcastContainmentKbps,
       "wwpLeosBroadcastContainmentClassifier": wwpLeosBroadcastContainmentClassifier,
       "wwpLeosBroadcastContainmentFilterMemTable": wwpLeosBroadcastContainmentFilterMemTable,
       "wwpLeosBroadcastContainmentFilterMemEntry": wwpLeosBroadcastContainmentFilterMemEntry,
       "wwpLeosBroadcastContainmentVlanId": wwpLeosBroadcastContainmentVlanId,
       "wwpLeosBroadcastContainmentPortId": wwpLeosBroadcastContainmentPortId,
       "wwpLeosBroadcastContainmentFilterMemStatus": wwpLeosBroadcastContainmentFilterMemStatus,
       "wwpLeosBroadcastContainmentGlobalStatus": wwpLeosBroadcastContainmentGlobalStatus,
       "wwpLeosBroadcastContainmentGlobalTime": wwpLeosBroadcastContainmentGlobalTime,
       "wwpLeosBroadcastContainmentIgnoreRapsMessages": wwpLeosBroadcastContainmentIgnoreRapsMessages,
       "wwpLeosBroadcastContainmentResourceMode": wwpLeosBroadcastContainmentResourceMode,
       "wwpLeosBroadcastContainmentBytesDroppedStats": wwpLeosBroadcastContainmentBytesDroppedStats,
       "wwpLeosBroadcastContainmentMIBNotificationPrefix": wwpLeosBroadcastContainmentMIBNotificationPrefix,
       "wwpLeosBroadcastContainmentMIBNotifications": wwpLeosBroadcastContainmentMIBNotifications,
       "wwpLeosBcastThresholdExceed": wwpLeosBcastThresholdExceed,
       "wwpLeosBcastThresholdNormal": wwpLeosBcastThresholdNormal,
       "wwpLeosBroadcastContainmentMIBConformance": wwpLeosBroadcastContainmentMIBConformance,
       "wwpLeosBroadcastContainmentMIBCompliances": wwpLeosBroadcastContainmentMIBCompliances,
       "wwpLeosBroadcastContainmentMIGroups": wwpLeosBroadcastContainmentMIGroups}
)
