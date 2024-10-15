# SNMP MIB module (ARC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:12 2024
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

(ResourceId,) = mibBuilder.importSymbols(
    "ALARM-MIB",
    "ResourceId")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

arcMibModule = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 117)
)
arcMibModule.setRevisions(
        ("2004-09-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IANAItuProbableCauseOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_ArcTimeIntervals_ObjectIdentity = ObjectIdentity
arcTimeIntervals = _ArcTimeIntervals_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 117, 1)
)
_ArcTITimeInterval_Type = Unsigned32
_ArcTITimeInterval_Object = MibScalar
arcTITimeInterval = _ArcTITimeInterval_Object(
    (1, 3, 6, 1, 2, 1, 117, 1, 1),
    _ArcTITimeInterval_Type()
)
arcTITimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arcTITimeInterval.setStatus("current")
if mibBuilder.loadTexts:
    arcTITimeInterval.setUnits("seconds")
_ArcCDTimeInterval_Type = Unsigned32
_ArcCDTimeInterval_Object = MibScalar
arcCDTimeInterval = _ArcCDTimeInterval_Object(
    (1, 3, 6, 1, 2, 1, 117, 1, 2),
    _ArcCDTimeInterval_Type()
)
arcCDTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arcCDTimeInterval.setStatus("current")
if mibBuilder.loadTexts:
    arcCDTimeInterval.setUnits("seconds")
_ArcObjects_ObjectIdentity = ObjectIdentity
arcObjects = _ArcObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 117, 2)
)
_ArcTable_Object = MibTable
arcTable = _ArcTable_Object(
    (1, 3, 6, 1, 2, 1, 117, 2, 1)
)
if mibBuilder.loadTexts:
    arcTable.setStatus("current")
_ArcEntry_Object = MibTableRow
arcEntry = _ArcEntry_Object(
    (1, 3, 6, 1, 2, 1, 117, 2, 1, 1)
)
arcEntry.setIndexNames(
    (0, "ARC-MIB", "arcIndex"),
    (0, "ARC-MIB", "arcAlarmType"),
    (0, "ARC-MIB", "arcNotificationId"),
)
if mibBuilder.loadTexts:
    arcEntry.setStatus("current")
_ArcIndex_Type = ResourceId
_ArcIndex_Object = MibTableColumn
arcIndex = _ArcIndex_Object(
    (1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 1),
    _ArcIndex_Type()
)
arcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arcIndex.setStatus("current")
_ArcAlarmType_Type = IANAItuProbableCauseOrZero
_ArcAlarmType_Object = MibTableColumn
arcAlarmType = _ArcAlarmType_Object(
    (1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 2),
    _ArcAlarmType_Type()
)
arcAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arcAlarmType.setStatus("current")
_ArcNotificationId_Type = ObjectIdentifier
_ArcNotificationId_Object = MibTableColumn
arcNotificationId = _ArcNotificationId_Object(
    (1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 3),
    _ArcNotificationId_Type()
)
arcNotificationId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arcNotificationId.setStatus("current")


class _ArcState_Type(Integer32):
    """Custom type arcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("nalm", 1),
          ("nalmQI", 2),
          ("nalmQICD", 4),
          ("nalmTI", 3))
    )


_ArcState_Type.__name__ = "Integer32"
_ArcState_Object = MibTableColumn
arcState = _ArcState_Object(
    (1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 4),
    _ArcState_Type()
)
arcState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arcState.setStatus("current")
_ArcNalmTimeRemaining_Type = Unsigned32
_ArcNalmTimeRemaining_Object = MibTableColumn
arcNalmTimeRemaining = _ArcNalmTimeRemaining_Object(
    (1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 5),
    _ArcNalmTimeRemaining_Type()
)
arcNalmTimeRemaining.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arcNalmTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    arcNalmTimeRemaining.setUnits("seconds")
_ArcRowStatus_Type = RowStatus
_ArcRowStatus_Object = MibTableColumn
arcRowStatus = _ArcRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 6),
    _ArcRowStatus_Type()
)
arcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arcRowStatus.setStatus("current")


class _ArcStorageType_Type(StorageType):
    """Custom type arcStorageType based on StorageType"""


_ArcStorageType_Object = MibTableColumn
arcStorageType = _ArcStorageType_Object(
    (1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 7),
    _ArcStorageType_Type()
)
arcStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arcStorageType.setStatus("current")
_ArcConformance_ObjectIdentity = ObjectIdentity
arcConformance = _ArcConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 117, 3)
)
_ArcCompliances_ObjectIdentity = ObjectIdentity
arcCompliances = _ArcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 117, 3, 1)
)
_ArcGroups_ObjectIdentity = ObjectIdentity
arcGroups = _ArcGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 117, 3, 2)
)

# Managed Objects groups

arcSettingGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 117, 3, 2, 1)
)
arcSettingGroup.setObjects(
      *(("ARC-MIB", "arcState"),
        ("ARC-MIB", "arcRowStatus"),
        ("ARC-MIB", "arcStorageType"))
)
if mibBuilder.loadTexts:
    arcSettingGroup.setStatus("current")

arcTIGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 117, 3, 2, 2)
)
arcTIGroup.setObjects(
      *(("ARC-MIB", "arcTITimeInterval"),
        ("ARC-MIB", "arcNalmTimeRemaining"))
)
if mibBuilder.loadTexts:
    arcTIGroup.setStatus("current")

arcQICDGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 117, 3, 2, 3)
)
arcQICDGroup.setObjects(
      *(("ARC-MIB", "arcCDTimeInterval"),
        ("ARC-MIB", "arcNalmTimeRemaining"))
)
if mibBuilder.loadTexts:
    arcQICDGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

arcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 117, 3, 1, 1)
)
if mibBuilder.loadTexts:
    arcCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARC-MIB",
    **{"IANAItuProbableCauseOrZero": IANAItuProbableCauseOrZero,
       "arcMibModule": arcMibModule,
       "arcTimeIntervals": arcTimeIntervals,
       "arcTITimeInterval": arcTITimeInterval,
       "arcCDTimeInterval": arcCDTimeInterval,
       "arcObjects": arcObjects,
       "arcTable": arcTable,
       "arcEntry": arcEntry,
       "arcIndex": arcIndex,
       "arcAlarmType": arcAlarmType,
       "arcNotificationId": arcNotificationId,
       "arcState": arcState,
       "arcNalmTimeRemaining": arcNalmTimeRemaining,
       "arcRowStatus": arcRowStatus,
       "arcStorageType": arcStorageType,
       "arcConformance": arcConformance,
       "arcCompliances": arcCompliances,
       "arcCompliance": arcCompliance,
       "arcGroups": arcGroups,
       "arcSettingGroup": arcSettingGroup,
       "arcTIGroup": arcTIGroup,
       "arcQICDGroup": arcQICDGroup}
)
