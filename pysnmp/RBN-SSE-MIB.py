# SNMP MIB module (RBN-SSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-SSE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:24 2024
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

(IANAItuEventType,
 IANAItuProbableCause) = mibBuilder.importSymbols(
    "IANA-ITU-ALARM-TC-MIB",
    "IANAItuEventType",
    "IANAItuProbableCause")

(ItuPerceivedSeverity,) = mibBuilder.importSymbols(
    "ITU-ALARM-TC-MIB",
    "ItuPerceivedSeverity")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(RbnPercentage,
 RbnSlot) = mibBuilder.importSymbols(
    "RBN-TC",
    "RbnPercentage",
    "RbnSlot")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rbnSseMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48)
)
rbnSseMIB.setRevisions(
        ("2009-09-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnSseMIBNotifications_ObjectIdentity = ObjectIdentity
rbnSseMIBNotifications = _RbnSseMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 0)
)
_RbnSseMIBObjects_ObjectIdentity = ObjectIdentity
rbnSseMIBObjects = _RbnSseMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 1)
)
_RbnFSGroupTable_Object = MibTable
rbnFSGroupTable = _RbnFSGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 1)
)
if mibBuilder.loadTexts:
    rbnFSGroupTable.setStatus("current")
_RbnFSGroupEntry_Object = MibTableRow
rbnFSGroupEntry = _RbnFSGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 1, 1)
)
rbnFSGroupEntry.setIndexNames(
    (0, "RBN-SSE-MIB", "rbnFSGroupName"),
)
if mibBuilder.loadTexts:
    rbnFSGroupEntry.setStatus("current")


class _RbnFSGroupName_Type(SnmpAdminString):
    """Custom type rbnFSGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RbnFSGroupName_Type.__name__ = "SnmpAdminString"
_RbnFSGroupName_Object = MibTableColumn
rbnFSGroupName = _RbnFSGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 1, 1, 1),
    _RbnFSGroupName_Type()
)
rbnFSGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnFSGroupName.setStatus("current")


class _RbnFSGroupState_Type(Integer32):
    """Custom type rbnFSGroupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("noCard", 5),
          ("partial", 3),
          ("stale", 4),
          ("unassigned", 6),
          ("unknown", 0),
          ("up", 1))
    )


_RbnFSGroupState_Type.__name__ = "Integer32"
_RbnFSGroupState_Object = MibTableColumn
rbnFSGroupState = _RbnFSGroupState_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 1, 1, 2),
    _RbnFSGroupState_Type()
)
rbnFSGroupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnFSGroupState.setStatus("current")


class _RbnFSGroupMode_Type(Integer32):
    """Custom type rbnFSGroupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("diskRedundancy", 1),
          ("networkRedundancy", 2),
          ("nonRedundant", 3))
    )


_RbnFSGroupMode_Type.__name__ = "Integer32"
_RbnFSGroupMode_Object = MibTableColumn
rbnFSGroupMode = _RbnFSGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 1, 1, 3),
    _RbnFSGroupMode_Type()
)
rbnFSGroupMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnFSGroupMode.setStatus("current")


class _RbnFSGroupRaidMode_Type(Integer32):
    """Custom type rbnFSGroupRaidMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("independent", 3),
          ("raid0", 1),
          ("raid1", 2),
          ("unknown", 0))
    )


_RbnFSGroupRaidMode_Type.__name__ = "Integer32"
_RbnFSGroupRaidMode_Object = MibTableColumn
rbnFSGroupRaidMode = _RbnFSGroupRaidMode_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 1, 1, 4),
    _RbnFSGroupRaidMode_Type()
)
rbnFSGroupRaidMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnFSGroupRaidMode.setStatus("current")


class _RbnFSGroupRevert_Type(TruthValue):
    """Custom type rbnFSGroupRevert based on TruthValue"""
    defaultValue = 2


_RbnFSGroupRevert_Object = MibTableColumn
rbnFSGroupRevert = _RbnFSGroupRevert_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 1, 1, 5),
    _RbnFSGroupRevert_Type()
)
rbnFSGroupRevert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnFSGroupRevert.setStatus("current")
_RbnFSPrimarySlot_Type = RbnSlot
_RbnFSPrimarySlot_Object = MibTableColumn
rbnFSPrimarySlot = _RbnFSPrimarySlot_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 1, 1, 6),
    _RbnFSPrimarySlot_Type()
)
rbnFSPrimarySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnFSPrimarySlot.setStatus("current")
_RbnFSSecondarySlot_Type = RbnSlot
_RbnFSSecondarySlot_Object = MibTableColumn
rbnFSSecondarySlot = _RbnFSSecondarySlot_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 1, 1, 7),
    _RbnFSSecondarySlot_Type()
)
rbnFSSecondarySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnFSSecondarySlot.setStatus("current")
_RbnFSActiveSlot_Type = RbnSlot
_RbnFSActiveSlot_Object = MibTableColumn
rbnFSActiveSlot = _RbnFSActiveSlot_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 1, 1, 8),
    _RbnFSActiveSlot_Type()
)
rbnFSActiveSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnFSActiveSlot.setStatus("current")
_RbnFSPartitionTable_Object = MibTable
rbnFSPartitionTable = _RbnFSPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 2)
)
if mibBuilder.loadTexts:
    rbnFSPartitionTable.setStatus("current")
_RbnFSPartitionEntry_Object = MibTableRow
rbnFSPartitionEntry = _RbnFSPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 2, 1)
)
rbnFSPartitionEntry.setIndexNames(
    (0, "RBN-SSE-MIB", "rbnFSGroupName"),
    (0, "RBN-SSE-MIB", "rbnFSPartitionName"),
)
if mibBuilder.loadTexts:
    rbnFSPartitionEntry.setStatus("current")


class _RbnFSPartitionName_Type(SnmpAdminString):
    """Custom type rbnFSPartitionName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RbnFSPartitionName_Type.__name__ = "SnmpAdminString"
_RbnFSPartitionName_Object = MibTableColumn
rbnFSPartitionName = _RbnFSPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 2, 1, 1),
    _RbnFSPartitionName_Type()
)
rbnFSPartitionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnFSPartitionName.setStatus("current")


class _RbnFSPartitionState_Type(Integer32):
    """Custom type rbnFSPartitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("stale", 3),
          ("up", 1))
    )


_RbnFSPartitionState_Type.__name__ = "Integer32"
_RbnFSPartitionState_Object = MibTableColumn
rbnFSPartitionState = _RbnFSPartitionState_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 2, 1, 2),
    _RbnFSPartitionState_Type()
)
rbnFSPartitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnFSPartitionState.setStatus("current")


class _RbnFSPartitionSize_Type(Unsigned32):
    """Custom type rbnFSPartitionSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RbnFSPartitionSize_Type.__name__ = "Unsigned32"
_RbnFSPartitionSize_Object = MibTableColumn
rbnFSPartitionSize = _RbnFSPartitionSize_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 2, 1, 3),
    _RbnFSPartitionSize_Type()
)
rbnFSPartitionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnFSPartitionSize.setStatus("current")
if mibBuilder.loadTexts:
    rbnFSPartitionSize.setUnits("GBytes")


class _RbnFSPartitionDisk_Type(Unsigned32):
    """Custom type rbnFSPartitionDisk based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RbnFSPartitionDisk_Type.__name__ = "Unsigned32"
_RbnFSPartitionDisk_Object = MibTableColumn
rbnFSPartitionDisk = _RbnFSPartitionDisk_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 2, 1, 4),
    _RbnFSPartitionDisk_Type()
)
rbnFSPartitionDisk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnFSPartitionDisk.setStatus("current")


class _RbnFSPartitionMirrored_Type(Integer32):
    """Custom type rbnFSPartitionMirrored based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_RbnFSPartitionMirrored_Type.__name__ = "Integer32"
_RbnFSPartitionMirrored_Object = MibTableColumn
rbnFSPartitionMirrored = _RbnFSPartitionMirrored_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 2, 1, 5),
    _RbnFSPartitionMirrored_Type()
)
rbnFSPartitionMirrored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnFSPartitionMirrored.setStatus("current")


class _RbnFSPartitionRaiseTriggerPercentage_Type(RbnPercentage):
    """Custom type rbnFSPartitionRaiseTriggerPercentage based on RbnPercentage"""
    defaultValue = 80

    subtypeSpec = RbnPercentage.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 100),
    )


_RbnFSPartitionRaiseTriggerPercentage_Type.__name__ = "RbnPercentage"
_RbnFSPartitionRaiseTriggerPercentage_Object = MibTableColumn
rbnFSPartitionRaiseTriggerPercentage = _RbnFSPartitionRaiseTriggerPercentage_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 2, 1, 6),
    _RbnFSPartitionRaiseTriggerPercentage_Type()
)
rbnFSPartitionRaiseTriggerPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnFSPartitionRaiseTriggerPercentage.setStatus("current")


class _RbnFSPartitionClearTriggerPercentage_Type(RbnPercentage):
    """Custom type rbnFSPartitionClearTriggerPercentage based on RbnPercentage"""
    defaultValue = 70

    subtypeSpec = RbnPercentage.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_RbnFSPartitionClearTriggerPercentage_Type.__name__ = "RbnPercentage"
_RbnFSPartitionClearTriggerPercentage_Object = MibTableColumn
rbnFSPartitionClearTriggerPercentage = _RbnFSPartitionClearTriggerPercentage_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 2, 1, 7),
    _RbnFSPartitionClearTriggerPercentage_Type()
)
rbnFSPartitionClearTriggerPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnFSPartitionClearTriggerPercentage.setStatus("current")
_RbnSseAlarmDateAndTime_Type = DateAndTime
_RbnSseAlarmDateAndTime_Object = MibScalar
rbnSseAlarmDateAndTime = _RbnSseAlarmDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 3),
    _RbnSseAlarmDateAndTime_Type()
)
rbnSseAlarmDateAndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnSseAlarmDateAndTime.setStatus("current")
_RbnSseAlarmSeverity_Type = ItuPerceivedSeverity
_RbnSseAlarmSeverity_Object = MibScalar
rbnSseAlarmSeverity = _RbnSseAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 4),
    _RbnSseAlarmSeverity_Type()
)
rbnSseAlarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnSseAlarmSeverity.setStatus("current")
_RbnSseAlarmProbableCause_Type = IANAItuProbableCause
_RbnSseAlarmProbableCause_Object = MibScalar
rbnSseAlarmProbableCause = _RbnSseAlarmProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 5),
    _RbnSseAlarmProbableCause_Type()
)
rbnSseAlarmProbableCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnSseAlarmProbableCause.setStatus("current")
_RbnSseEventType_Type = IANAItuEventType
_RbnSseEventType_Object = MibScalar
rbnSseEventType = _RbnSseEventType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 6),
    _RbnSseEventType_Type()
)
rbnSseEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnSseEventType.setStatus("current")


class _RbnSseAlarmDescription_Type(SnmpAdminString):
    """Custom type rbnSseAlarmDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RbnSseAlarmDescription_Type.__name__ = "SnmpAdminString"
_RbnSseAlarmDescription_Object = MibScalar
rbnSseAlarmDescription = _RbnSseAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 1, 7),
    _RbnSseAlarmDescription_Type()
)
rbnSseAlarmDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnSseAlarmDescription.setStatus("current")
_RbnSseMIBConformance_ObjectIdentity = ObjectIdentity
rbnSseMIBConformance = _RbnSseMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 2)
)
_RbnSseGroups_ObjectIdentity = ObjectIdentity
rbnSseGroups = _RbnSseGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 2, 1)
)
_RbnSseCompliances_ObjectIdentity = ObjectIdentity
rbnSseCompliances = _RbnSseCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 2, 2)
)

# Managed Objects groups

rbnSseFileServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 2, 1, 1)
)
rbnSseFileServerGroup.setObjects(
      *(("RBN-SSE-MIB", "rbnFSGroupMode"),
        ("RBN-SSE-MIB", "rbnFSGroupState"),
        ("RBN-SSE-MIB", "rbnFSGroupRaidMode"),
        ("RBN-SSE-MIB", "rbnFSGroupRevert"),
        ("RBN-SSE-MIB", "rbnFSPrimarySlot"),
        ("RBN-SSE-MIB", "rbnFSSecondarySlot"),
        ("RBN-SSE-MIB", "rbnFSActiveSlot"))
)
if mibBuilder.loadTexts:
    rbnSseFileServerGroup.setStatus("current")

rbnSsePartitionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 2, 1, 2)
)
rbnSsePartitionGroup.setObjects(
      *(("RBN-SSE-MIB", "rbnFSPartitionSize"),
        ("RBN-SSE-MIB", "rbnFSPartitionState"),
        ("RBN-SSE-MIB", "rbnFSPartitionDisk"),
        ("RBN-SSE-MIB", "rbnFSPartitionMirrored"),
        ("RBN-SSE-MIB", "rbnFSPartitionRaiseTriggerPercentage"),
        ("RBN-SSE-MIB", "rbnFSPartitionClearTriggerPercentage"))
)
if mibBuilder.loadTexts:
    rbnSsePartitionGroup.setStatus("current")

rbnSseEventObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 2, 1, 3)
)
rbnSseEventObjectGroup.setObjects(
      *(("RBN-SSE-MIB", "rbnSseEventType"),
        ("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"),
        ("RBN-SSE-MIB", "rbnSseAlarmDescription"),
        ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"),
        ("RBN-SSE-MIB", "rbnSseAlarmSeverity"))
)
if mibBuilder.loadTexts:
    rbnSseEventObjectGroup.setStatus("current")


# Notification objects

rbnSseFsgSwitchManual = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 0, 1)
)
rbnSseFsgSwitchManual.setObjects(
      *(("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"),
        ("RBN-SSE-MIB", "rbnSseAlarmSeverity"),
        ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"),
        ("RBN-SSE-MIB", "rbnSseEventType"),
        ("RBN-SSE-MIB", "rbnSseAlarmDescription"),
        ("RBN-SSE-MIB", "rbnFSGroupState"))
)
if mibBuilder.loadTexts:
    rbnSseFsgSwitchManual.setStatus(
        "current"
    )

rbnSseFsgSwitchAuto = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 0, 2)
)
rbnSseFsgSwitchAuto.setObjects(
      *(("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"),
        ("RBN-SSE-MIB", "rbnSseAlarmSeverity"),
        ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"),
        ("RBN-SSE-MIB", "rbnSseEventType"),
        ("RBN-SSE-MIB", "rbnSseAlarmDescription"),
        ("RBN-SSE-MIB", "rbnFSGroupState"))
)
if mibBuilder.loadTexts:
    rbnSseFsgSwitchAuto.setStatus(
        "current"
    )

rbnSseFsgSwitchCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 0, 3)
)
rbnSseFsgSwitchCompleted.setObjects(
      *(("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"),
        ("RBN-SSE-MIB", "rbnSseAlarmSeverity"),
        ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"),
        ("RBN-SSE-MIB", "rbnSseEventType"),
        ("RBN-SSE-MIB", "rbnSseAlarmDescription"),
        ("RBN-SSE-MIB", "rbnFSGroupState"))
)
if mibBuilder.loadTexts:
    rbnSseFsgSwitchCompleted.setStatus(
        "current"
    )

rbnSseFsgSwitchFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 0, 4)
)
rbnSseFsgSwitchFail.setObjects(
      *(("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"),
        ("RBN-SSE-MIB", "rbnSseAlarmSeverity"),
        ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"),
        ("RBN-SSE-MIB", "rbnSseEventType"),
        ("RBN-SSE-MIB", "rbnSseAlarmDescription"),
        ("RBN-SSE-MIB", "rbnFSGroupState"))
)
if mibBuilder.loadTexts:
    rbnSseFsgSwitchFail.setStatus(
        "current"
    )

rbnSseFsgSwitchWtr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 0, 5)
)
rbnSseFsgSwitchWtr.setObjects(
      *(("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"),
        ("RBN-SSE-MIB", "rbnSseAlarmSeverity"),
        ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"),
        ("RBN-SSE-MIB", "rbnSseEventType"),
        ("RBN-SSE-MIB", "rbnSseAlarmDescription"),
        ("RBN-SSE-MIB", "rbnFSGroupState"))
)
if mibBuilder.loadTexts:
    rbnSseFsgSwitchWtr.setStatus(
        "current"
    )

rbnSseFsgNotOperational = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 0, 6)
)
rbnSseFsgNotOperational.setObjects(
      *(("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"),
        ("RBN-SSE-MIB", "rbnSseAlarmSeverity"),
        ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"),
        ("RBN-SSE-MIB", "rbnSseEventType"),
        ("RBN-SSE-MIB", "rbnSseAlarmDescription"),
        ("RBN-SSE-MIB", "rbnFSGroupState"))
)
if mibBuilder.loadTexts:
    rbnSseFsgNotOperational.setStatus(
        "current"
    )

rbnSseFsgBlockDeviceFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 0, 7)
)
rbnSseFsgBlockDeviceFail.setObjects(
      *(("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"),
        ("RBN-SSE-MIB", "rbnSseAlarmSeverity"),
        ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"),
        ("RBN-SSE-MIB", "rbnSseEventType"),
        ("RBN-SSE-MIB", "rbnSseAlarmDescription"),
        ("RBN-SSE-MIB", "rbnFSGroupState"))
)
if mibBuilder.loadTexts:
    rbnSseFsgBlockDeviceFail.setStatus(
        "current"
    )

rbnSseFsgPartitionNotOperational = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 0, 8)
)
rbnSseFsgPartitionNotOperational.setObjects(
      *(("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"),
        ("RBN-SSE-MIB", "rbnSseAlarmSeverity"),
        ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"),
        ("RBN-SSE-MIB", "rbnSseEventType"),
        ("RBN-SSE-MIB", "rbnSseAlarmDescription"),
        ("RBN-SSE-MIB", "rbnFSPartitionState"))
)
if mibBuilder.loadTexts:
    rbnSseFsgPartitionNotOperational.setStatus(
        "current"
    )

rbnSseFsgParitionDataSyncing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 0, 9)
)
rbnSseFsgParitionDataSyncing.setObjects(
      *(("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"),
        ("RBN-SSE-MIB", "rbnSseAlarmSeverity"),
        ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"),
        ("RBN-SSE-MIB", "rbnSseEventType"),
        ("RBN-SSE-MIB", "rbnSseAlarmDescription"),
        ("RBN-SSE-MIB", "rbnFSPartitionState"))
)
if mibBuilder.loadTexts:
    rbnSseFsgParitionDataSyncing.setStatus(
        "current"
    )

rbnSseFsgParitionDataSyncFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 0, 10)
)
rbnSseFsgParitionDataSyncFail.setObjects(
      *(("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"),
        ("RBN-SSE-MIB", "rbnSseAlarmSeverity"),
        ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"),
        ("RBN-SSE-MIB", "rbnSseEventType"),
        ("RBN-SSE-MIB", "rbnSseAlarmDescription"),
        ("RBN-SSE-MIB", "rbnFSPartitionState"))
)
if mibBuilder.loadTexts:
    rbnSseFsgParitionDataSyncFail.setStatus(
        "current"
    )

rbnSseFsgPartitionFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 0, 11)
)
rbnSseFsgPartitionFull.setObjects(
      *(("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"),
        ("RBN-SSE-MIB", "rbnSseAlarmSeverity"),
        ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"),
        ("RBN-SSE-MIB", "rbnSseEventType"),
        ("RBN-SSE-MIB", "rbnSseAlarmDescription"),
        ("RBN-SSE-MIB", "rbnFSPartitionState"))
)
if mibBuilder.loadTexts:
    rbnSseFsgPartitionFull.setStatus(
        "current"
    )

rbnSseFsgPartitionLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 0, 12)
)
rbnSseFsgPartitionLow.setObjects(
      *(("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"),
        ("RBN-SSE-MIB", "rbnSseAlarmSeverity"),
        ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"),
        ("RBN-SSE-MIB", "rbnSseEventType"),
        ("RBN-SSE-MIB", "rbnSseAlarmDescription"),
        ("RBN-SSE-MIB", "rbnFSPartitionState"))
)
if mibBuilder.loadTexts:
    rbnSseFsgPartitionLow.setStatus(
        "current"
    )

rbnSseFsgPartitionNotOperStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 0, 13)
)
rbnSseFsgPartitionNotOperStandby.setObjects(
      *(("RBN-SSE-MIB", "rbnSseAlarmDateAndTime"),
        ("RBN-SSE-MIB", "rbnSseAlarmSeverity"),
        ("RBN-SSE-MIB", "rbnSseAlarmProbableCause"),
        ("RBN-SSE-MIB", "rbnSseEventType"),
        ("RBN-SSE-MIB", "rbnSseAlarmDescription"),
        ("RBN-SSE-MIB", "rbnFSPartitionState"))
)
if mibBuilder.loadTexts:
    rbnSseFsgPartitionNotOperStandby.setStatus(
        "current"
    )


# Notifications groups

rbnSseEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 2, 1, 4)
)
rbnSseEventGroup.setObjects(
      *(("RBN-SSE-MIB", "rbnSseFsgSwitchManual"),
        ("RBN-SSE-MIB", "rbnSseFsgSwitchAuto"),
        ("RBN-SSE-MIB", "rbnSseFsgSwitchCompleted"),
        ("RBN-SSE-MIB", "rbnSseFsgSwitchFail"),
        ("RBN-SSE-MIB", "rbnSseFsgSwitchWtr"),
        ("RBN-SSE-MIB", "rbnSseFsgNotOperational"),
        ("RBN-SSE-MIB", "rbnSseFsgBlockDeviceFail"),
        ("RBN-SSE-MIB", "rbnSseFsgPartitionNotOperational"),
        ("RBN-SSE-MIB", "rbnSseFsgParitionDataSyncing"),
        ("RBN-SSE-MIB", "rbnSseFsgParitionDataSyncFail"),
        ("RBN-SSE-MIB", "rbnSseFsgPartitionFull"),
        ("RBN-SSE-MIB", "rbnSseFsgPartitionLow"),
        ("RBN-SSE-MIB", "rbnSseFsgPartitionNotOperStandby"))
)
if mibBuilder.loadTexts:
    rbnSseEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rbnSseMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 48, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rbnSseMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-SSE-MIB",
    **{"rbnSseMIB": rbnSseMIB,
       "rbnSseMIBNotifications": rbnSseMIBNotifications,
       "rbnSseFsgSwitchManual": rbnSseFsgSwitchManual,
       "rbnSseFsgSwitchAuto": rbnSseFsgSwitchAuto,
       "rbnSseFsgSwitchCompleted": rbnSseFsgSwitchCompleted,
       "rbnSseFsgSwitchFail": rbnSseFsgSwitchFail,
       "rbnSseFsgSwitchWtr": rbnSseFsgSwitchWtr,
       "rbnSseFsgNotOperational": rbnSseFsgNotOperational,
       "rbnSseFsgBlockDeviceFail": rbnSseFsgBlockDeviceFail,
       "rbnSseFsgPartitionNotOperational": rbnSseFsgPartitionNotOperational,
       "rbnSseFsgParitionDataSyncing": rbnSseFsgParitionDataSyncing,
       "rbnSseFsgParitionDataSyncFail": rbnSseFsgParitionDataSyncFail,
       "rbnSseFsgPartitionFull": rbnSseFsgPartitionFull,
       "rbnSseFsgPartitionLow": rbnSseFsgPartitionLow,
       "rbnSseFsgPartitionNotOperStandby": rbnSseFsgPartitionNotOperStandby,
       "rbnSseMIBObjects": rbnSseMIBObjects,
       "rbnFSGroupTable": rbnFSGroupTable,
       "rbnFSGroupEntry": rbnFSGroupEntry,
       "rbnFSGroupName": rbnFSGroupName,
       "rbnFSGroupState": rbnFSGroupState,
       "rbnFSGroupMode": rbnFSGroupMode,
       "rbnFSGroupRaidMode": rbnFSGroupRaidMode,
       "rbnFSGroupRevert": rbnFSGroupRevert,
       "rbnFSPrimarySlot": rbnFSPrimarySlot,
       "rbnFSSecondarySlot": rbnFSSecondarySlot,
       "rbnFSActiveSlot": rbnFSActiveSlot,
       "rbnFSPartitionTable": rbnFSPartitionTable,
       "rbnFSPartitionEntry": rbnFSPartitionEntry,
       "rbnFSPartitionName": rbnFSPartitionName,
       "rbnFSPartitionState": rbnFSPartitionState,
       "rbnFSPartitionSize": rbnFSPartitionSize,
       "rbnFSPartitionDisk": rbnFSPartitionDisk,
       "rbnFSPartitionMirrored": rbnFSPartitionMirrored,
       "rbnFSPartitionRaiseTriggerPercentage": rbnFSPartitionRaiseTriggerPercentage,
       "rbnFSPartitionClearTriggerPercentage": rbnFSPartitionClearTriggerPercentage,
       "rbnSseAlarmDateAndTime": rbnSseAlarmDateAndTime,
       "rbnSseAlarmSeverity": rbnSseAlarmSeverity,
       "rbnSseAlarmProbableCause": rbnSseAlarmProbableCause,
       "rbnSseEventType": rbnSseEventType,
       "rbnSseAlarmDescription": rbnSseAlarmDescription,
       "rbnSseMIBConformance": rbnSseMIBConformance,
       "rbnSseGroups": rbnSseGroups,
       "rbnSseFileServerGroup": rbnSseFileServerGroup,
       "rbnSsePartitionGroup": rbnSsePartitionGroup,
       "rbnSseEventObjectGroup": rbnSseEventObjectGroup,
       "rbnSseEventGroup": rbnSseEventGroup,
       "rbnSseCompliances": rbnSseCompliances,
       "rbnSseMIBCompliance": rbnSseMIBCompliance}
)
