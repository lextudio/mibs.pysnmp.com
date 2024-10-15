# SNMP MIB module (SONUS-SOFTWARE-UPGRADE-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-SOFTWARE-UPGRADE-SERVICES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:09 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")

(sonusEventClass,
 sonusEventDescription,
 sonusEventLevel,
 sonusShelfIndex) = mibBuilder.importSymbols(
    "SONUS-COMMON-MIB",
    "sonusEventClass",
    "sonusEventDescription",
    "sonusEventLevel",
    "sonusShelfIndex")

(sonusServicesMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusServicesMIBs")


# MODULE-IDENTITY

sonusSoftwareUpgradeServicesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SonusSoftwareUpgradeState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("cnsReset", 14),
          ("delay1", 3),
          ("done", 18),
          ("firstPns", 13),
          ("idle", 0),
          ("init", 2),
          ("pnsReset", 16),
          ("prepare", 11),
          ("query", 1),
          ("spsReset", 15),
          ("start", 4),
          ("stopCalls", 12),
          ("sxDelay", 17),
          ("sxOne", 5),
          ("sxTwoRx", 8),
          ("sxTwoTx", 7),
          ("sxTwoWait", 9),
          ("variant", 10),
          ("waitSync", 6))
    )



# MIB Managed Objects in the order of their OIDs

_SonusSoftwareUpgradeServicesMIBObjects_ObjectIdentity = ObjectIdentity
sonusSoftwareUpgradeServicesMIBObjects = _SonusSoftwareUpgradeServicesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1)
)
_SonusSwUpgradeShelfAdmnTable_Object = MibTable
sonusSwUpgradeShelfAdmnTable = _SonusSwUpgradeShelfAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 1)
)
if mibBuilder.loadTexts:
    sonusSwUpgradeShelfAdmnTable.setStatus("current")
_SonusSwUpgradeShelfAdmnEntry_Object = MibTableRow
sonusSwUpgradeShelfAdmnEntry = _SonusSwUpgradeShelfAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 1, 1)
)
sonusSwUpgradeShelfAdmnEntry.setIndexNames(
    (0, "SONUS-SOFTWARE-UPGRADE-SERVICES-MIB", "sonusSwUpgradeShelfAdmnShelfIndex"),
)
if mibBuilder.loadTexts:
    sonusSwUpgradeShelfAdmnEntry.setStatus("current")


class _SonusSwUpgradeShelfAdmnShelfIndex_Type(Integer32):
    """Custom type sonusSwUpgradeShelfAdmnShelfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusSwUpgradeShelfAdmnShelfIndex_Type.__name__ = "Integer32"
_SonusSwUpgradeShelfAdmnShelfIndex_Object = MibTableColumn
sonusSwUpgradeShelfAdmnShelfIndex = _SonusSwUpgradeShelfAdmnShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 1, 1, 1),
    _SonusSwUpgradeShelfAdmnShelfIndex_Type()
)
sonusSwUpgradeShelfAdmnShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSwUpgradeShelfAdmnShelfIndex.setStatus("current")


class _SonusSwUpgradeShelfAdmnInit_Type(Integer32):
    """Custom type sonusSwUpgradeShelfAdmnInit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initialize", 2),
          ("ready", 1))
    )


_SonusSwUpgradeShelfAdmnInit_Type.__name__ = "Integer32"
_SonusSwUpgradeShelfAdmnInit_Object = MibTableColumn
sonusSwUpgradeShelfAdmnInit = _SonusSwUpgradeShelfAdmnInit_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 1, 1, 2),
    _SonusSwUpgradeShelfAdmnInit_Type()
)
sonusSwUpgradeShelfAdmnInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSwUpgradeShelfAdmnInit.setStatus("current")


class _SonusSwUpgradeShelfAdmnUpgradeNow_Type(Integer32):
    """Custom type sonusSwUpgradeShelfAdmnUpgradeNow based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("upgrade", 2))
    )


_SonusSwUpgradeShelfAdmnUpgradeNow_Type.__name__ = "Integer32"
_SonusSwUpgradeShelfAdmnUpgradeNow_Object = MibTableColumn
sonusSwUpgradeShelfAdmnUpgradeNow = _SonusSwUpgradeShelfAdmnUpgradeNow_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 1, 1, 3),
    _SonusSwUpgradeShelfAdmnUpgradeNow_Type()
)
sonusSwUpgradeShelfAdmnUpgradeNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSwUpgradeShelfAdmnUpgradeNow.setStatus("current")


class _SonusSwUpgradeShelfAdmnHalt_Type(Integer32):
    """Custom type sonusSwUpgradeShelfAdmnHalt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("halt", 2),
          ("ready", 1))
    )


_SonusSwUpgradeShelfAdmnHalt_Type.__name__ = "Integer32"
_SonusSwUpgradeShelfAdmnHalt_Object = MibTableColumn
sonusSwUpgradeShelfAdmnHalt = _SonusSwUpgradeShelfAdmnHalt_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 1, 1, 4),
    _SonusSwUpgradeShelfAdmnHalt_Type()
)
sonusSwUpgradeShelfAdmnHalt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSwUpgradeShelfAdmnHalt.setStatus("current")


class _SonusSwUpgradeShelfAdmnCommitDirectory_Type(Integer32):
    """Custom type sonusSwUpgradeShelfAdmnCommitDirectory based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("commit", 2),
          ("ready", 1))
    )


_SonusSwUpgradeShelfAdmnCommitDirectory_Type.__name__ = "Integer32"
_SonusSwUpgradeShelfAdmnCommitDirectory_Object = MibTableColumn
sonusSwUpgradeShelfAdmnCommitDirectory = _SonusSwUpgradeShelfAdmnCommitDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 1, 1, 5),
    _SonusSwUpgradeShelfAdmnCommitDirectory_Type()
)
sonusSwUpgradeShelfAdmnCommitDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSwUpgradeShelfAdmnCommitDirectory.setStatus("current")


class _SonusSwUpgradeShelfAdmnDirectory_Type(DisplayString):
    """Custom type sonusSwUpgradeShelfAdmnDirectory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SonusSwUpgradeShelfAdmnDirectory_Type.__name__ = "DisplayString"
_SonusSwUpgradeShelfAdmnDirectory_Object = MibTableColumn
sonusSwUpgradeShelfAdmnDirectory = _SonusSwUpgradeShelfAdmnDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 1, 1, 6),
    _SonusSwUpgradeShelfAdmnDirectory_Type()
)
sonusSwUpgradeShelfAdmnDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSwUpgradeShelfAdmnDirectory.setStatus("current")


class _SonusSwUpgradeShelfAdmnOverrideFeatureCheck_Type(Integer32):
    """Custom type sonusSwUpgradeShelfAdmnOverrideFeatureCheck based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("override", 2),
          ("ready", 1))
    )


_SonusSwUpgradeShelfAdmnOverrideFeatureCheck_Type.__name__ = "Integer32"
_SonusSwUpgradeShelfAdmnOverrideFeatureCheck_Object = MibTableColumn
sonusSwUpgradeShelfAdmnOverrideFeatureCheck = _SonusSwUpgradeShelfAdmnOverrideFeatureCheck_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 1, 1, 7),
    _SonusSwUpgradeShelfAdmnOverrideFeatureCheck_Type()
)
sonusSwUpgradeShelfAdmnOverrideFeatureCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSwUpgradeShelfAdmnOverrideFeatureCheck.setStatus("current")
_SonusSwUpgradeShelfStatTable_Object = MibTable
sonusSwUpgradeShelfStatTable = _SonusSwUpgradeShelfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 2)
)
if mibBuilder.loadTexts:
    sonusSwUpgradeShelfStatTable.setStatus("current")
_SonusSwUpgradeShelfStatEntry_Object = MibTableRow
sonusSwUpgradeShelfStatEntry = _SonusSwUpgradeShelfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 2, 1)
)
sonusSwUpgradeShelfStatEntry.setIndexNames(
    (0, "SONUS-SOFTWARE-UPGRADE-SERVICES-MIB", "sonusSwUpgradeShelfStatShelfIndex"),
)
if mibBuilder.loadTexts:
    sonusSwUpgradeShelfStatEntry.setStatus("current")


class _SonusSwUpgradeShelfStatShelfIndex_Type(Integer32):
    """Custom type sonusSwUpgradeShelfStatShelfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusSwUpgradeShelfStatShelfIndex_Type.__name__ = "Integer32"
_SonusSwUpgradeShelfStatShelfIndex_Object = MibTableColumn
sonusSwUpgradeShelfStatShelfIndex = _SonusSwUpgradeShelfStatShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 2, 1, 1),
    _SonusSwUpgradeShelfStatShelfIndex_Type()
)
sonusSwUpgradeShelfStatShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSwUpgradeShelfStatShelfIndex.setStatus("current")


class _SonusSwUpgradeShelfStatStatus_Type(Integer32):
    """Custom type sonusSwUpgradeShelfStatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("busy", 2),
          ("commitRequired", 5),
          ("complete", 3),
          ("idle", 1),
          ("incomplete", 4))
    )


_SonusSwUpgradeShelfStatStatus_Type.__name__ = "Integer32"
_SonusSwUpgradeShelfStatStatus_Object = MibTableColumn
sonusSwUpgradeShelfStatStatus = _SonusSwUpgradeShelfStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 2, 1, 2),
    _SonusSwUpgradeShelfStatStatus_Type()
)
sonusSwUpgradeShelfStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSwUpgradeShelfStatStatus.setStatus("current")


class _SonusSwUpgradeShelfStatCurSlot_Type(Integer32):
    """Custom type sonusSwUpgradeShelfStatCurSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusSwUpgradeShelfStatCurSlot_Type.__name__ = "Integer32"
_SonusSwUpgradeShelfStatCurSlot_Object = MibTableColumn
sonusSwUpgradeShelfStatCurSlot = _SonusSwUpgradeShelfStatCurSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 2, 1, 3),
    _SonusSwUpgradeShelfStatCurSlot_Type()
)
sonusSwUpgradeShelfStatCurSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSwUpgradeShelfStatCurSlot.setStatus("current")


class _SonusSwUpgradeShelfStatSlotRemain_Type(Integer32):
    """Custom type sonusSwUpgradeShelfStatSlotRemain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusSwUpgradeShelfStatSlotRemain_Type.__name__ = "Integer32"
_SonusSwUpgradeShelfStatSlotRemain_Object = MibTableColumn
sonusSwUpgradeShelfStatSlotRemain = _SonusSwUpgradeShelfStatSlotRemain_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 2, 1, 4),
    _SonusSwUpgradeShelfStatSlotRemain_Type()
)
sonusSwUpgradeShelfStatSlotRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSwUpgradeShelfStatSlotRemain.setStatus("current")
_SonusSwUpgradeShelfStatGroupRemain_Type = Integer32
_SonusSwUpgradeShelfStatGroupRemain_Object = MibTableColumn
sonusSwUpgradeShelfStatGroupRemain = _SonusSwUpgradeShelfStatGroupRemain_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 2, 1, 5),
    _SonusSwUpgradeShelfStatGroupRemain_Type()
)
sonusSwUpgradeShelfStatGroupRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSwUpgradeShelfStatGroupRemain.setStatus("current")
_SonusSwUpgradeShelfStatDuration_Type = Counter32
_SonusSwUpgradeShelfStatDuration_Object = MibTableColumn
sonusSwUpgradeShelfStatDuration = _SonusSwUpgradeShelfStatDuration_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 2, 1, 6),
    _SonusSwUpgradeShelfStatDuration_Type()
)
sonusSwUpgradeShelfStatDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSwUpgradeShelfStatDuration.setStatus("current")
_SonusSwUpgradeShelfStatStartTime_Type = DateAndTime
_SonusSwUpgradeShelfStatStartTime_Object = MibTableColumn
sonusSwUpgradeShelfStatStartTime = _SonusSwUpgradeShelfStatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 2, 1, 7),
    _SonusSwUpgradeShelfStatStartTime_Type()
)
sonusSwUpgradeShelfStatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSwUpgradeShelfStatStartTime.setStatus("current")


class _SonusSwUpgradeShelfStatLastReason_Type(Integer32):
    """Custom type sonusSwUpgradeShelfStatLastReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("fileUnavailable", 5),
          ("flashUpdateInProgress", 7),
          ("initTimeout", 2),
          ("internalQueryTimeout", 17),
          ("internalResourceUnavailable", 18),
          ("internalRtmError", 19),
          ("internalTimerUnavailable", 16),
          ("manualHalt", 3),
          ("mnsNotSynced", 14),
          ("mnsSwitchover", 20),
          ("none", 0),
          ("notActive", 15),
          ("parametersNotSaved", 6),
          ("rebootTimeout", 13),
          ("redundSlotActive", 8),
          ("successfulCompletion", 1),
          ("switchover1Timeout", 9),
          ("switchover2Timeout", 11),
          ("sync1Timeout", 10),
          ("sync2Timeout", 12),
          ("upgradeNotRequired", 4))
    )


_SonusSwUpgradeShelfStatLastReason_Type.__name__ = "Integer32"
_SonusSwUpgradeShelfStatLastReason_Object = MibTableColumn
sonusSwUpgradeShelfStatLastReason = _SonusSwUpgradeShelfStatLastReason_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 2, 1, 8),
    _SonusSwUpgradeShelfStatLastReason_Type()
)
sonusSwUpgradeShelfStatLastReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSwUpgradeShelfStatLastReason.setStatus("current")
_SonusSwUpgradeShelfStatLastState_Type = SonusSoftwareUpgradeState
_SonusSwUpgradeShelfStatLastState_Object = MibTableColumn
sonusSwUpgradeShelfStatLastState = _SonusSwUpgradeShelfStatLastState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 2, 1, 9),
    _SonusSwUpgradeShelfStatLastState_Type()
)
sonusSwUpgradeShelfStatLastState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSwUpgradeShelfStatLastState.setStatus("current")
_SonusSwUpgradeShelfStatState_Type = SonusSoftwareUpgradeState
_SonusSwUpgradeShelfStatState_Object = MibTableColumn
sonusSwUpgradeShelfStatState = _SonusSwUpgradeShelfStatState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 2, 1, 10),
    _SonusSwUpgradeShelfStatState_Type()
)
sonusSwUpgradeShelfStatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSwUpgradeShelfStatState.setStatus("current")
_SonusSwUpgradeSlotStatTable_Object = MibTable
sonusSwUpgradeSlotStatTable = _SonusSwUpgradeSlotStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 3)
)
if mibBuilder.loadTexts:
    sonusSwUpgradeSlotStatTable.setStatus("current")
_SonusSwUpgradeSlotStatEntry_Object = MibTableRow
sonusSwUpgradeSlotStatEntry = _SonusSwUpgradeSlotStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 3, 1)
)
sonusSwUpgradeSlotStatEntry.setIndexNames(
    (0, "SONUS-SOFTWARE-UPGRADE-SERVICES-MIB", "sonusSwUpgradeSlotStatShelfIndex"),
    (0, "SONUS-SOFTWARE-UPGRADE-SERVICES-MIB", "sonusSwUpgradeSlotStatSlotIndex"),
)
if mibBuilder.loadTexts:
    sonusSwUpgradeSlotStatEntry.setStatus("current")


class _SonusSwUpgradeSlotStatShelfIndex_Type(Integer32):
    """Custom type sonusSwUpgradeSlotStatShelfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusSwUpgradeSlotStatShelfIndex_Type.__name__ = "Integer32"
_SonusSwUpgradeSlotStatShelfIndex_Object = MibTableColumn
sonusSwUpgradeSlotStatShelfIndex = _SonusSwUpgradeSlotStatShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 3, 1, 1),
    _SonusSwUpgradeSlotStatShelfIndex_Type()
)
sonusSwUpgradeSlotStatShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSwUpgradeSlotStatShelfIndex.setStatus("current")


class _SonusSwUpgradeSlotStatSlotIndex_Type(Integer32):
    """Custom type sonusSwUpgradeSlotStatSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusSwUpgradeSlotStatSlotIndex_Type.__name__ = "Integer32"
_SonusSwUpgradeSlotStatSlotIndex_Object = MibTableColumn
sonusSwUpgradeSlotStatSlotIndex = _SonusSwUpgradeSlotStatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 3, 1, 2),
    _SonusSwUpgradeSlotStatSlotIndex_Type()
)
sonusSwUpgradeSlotStatSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSwUpgradeSlotStatSlotIndex.setStatus("current")


class _SonusSwUpgradeSlotStatStatus_Type(Integer32):
    """Custom type sonusSwUpgradeSlotStatStatus based on Integer32"""
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
        *(("busy", 2),
          ("complete", 3),
          ("idle", 1),
          ("unknown", 4))
    )


_SonusSwUpgradeSlotStatStatus_Type.__name__ = "Integer32"
_SonusSwUpgradeSlotStatStatus_Object = MibTableColumn
sonusSwUpgradeSlotStatStatus = _SonusSwUpgradeSlotStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 3, 1, 3),
    _SonusSwUpgradeSlotStatStatus_Type()
)
sonusSwUpgradeSlotStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSwUpgradeSlotStatStatus.setStatus("current")


class _SonusSwUpgradeSlotStatUpgrade_Type(Integer32):
    """Custom type sonusSwUpgradeSlotStatUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disrupt", 3),
          ("none", 1),
          ("smooth", 2),
          ("unavailable", 4),
          ("unknown", 5))
    )


_SonusSwUpgradeSlotStatUpgrade_Type.__name__ = "Integer32"
_SonusSwUpgradeSlotStatUpgrade_Object = MibTableColumn
sonusSwUpgradeSlotStatUpgrade = _SonusSwUpgradeSlotStatUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 3, 1, 4),
    _SonusSwUpgradeSlotStatUpgrade_Type()
)
sonusSwUpgradeSlotStatUpgrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSwUpgradeSlotStatUpgrade.setStatus("current")


class _SonusSwUpgradeSlotStatVersion_Type(DisplayString):
    """Custom type sonusSwUpgradeSlotStatVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SonusSwUpgradeSlotStatVersion_Type.__name__ = "DisplayString"
_SonusSwUpgradeSlotStatVersion_Object = MibTableColumn
sonusSwUpgradeSlotStatVersion = _SonusSwUpgradeSlotStatVersion_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 3, 1, 5),
    _SonusSwUpgradeSlotStatVersion_Type()
)
sonusSwUpgradeSlotStatVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSwUpgradeSlotStatVersion.setStatus("current")
_SonusSoftwareUpgradeServicesMIBNotifications_ObjectIdentity = ObjectIdentity
sonusSoftwareUpgradeServicesMIBNotifications = _SonusSoftwareUpgradeServicesMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 2)
)
_SonusSoftwareUpgradeServicesMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusSoftwareUpgradeServicesMIBNotificationsPrefix = _SonusSoftwareUpgradeServicesMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 2, 0)
)
_SonusSoftwareUpgradeServicesMIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusSoftwareUpgradeServicesMIBNotificationsObjects = _SonusSoftwareUpgradeServicesMIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 2, 1)
)

# Managed Objects groups


# Notification objects

sonusSoftwareUpgradeInitiatedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 2, 0, 1)
)
sonusSoftwareUpgradeInitiatedNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-SOFTWARE-UPGRADE-SERVICES-MIB", "sonusSwUpgradeShelfAdmnDirectory"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSoftwareUpgradeInitiatedNotification.setStatus(
        "current"
    )

sonusSoftwareUpgradeTerminatedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 2, 0, 2)
)
sonusSoftwareUpgradeTerminatedNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-SOFTWARE-UPGRADE-SERVICES-MIB", "sonusSwUpgradeShelfAdmnDirectory"),
        ("SONUS-SOFTWARE-UPGRADE-SERVICES-MIB", "sonusSwUpgradeShelfStatLastReason"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSoftwareUpgradeTerminatedNotification.setStatus(
        "current"
    )

sonusSoftwareUpgradeSucceededNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 2, 0, 3)
)
sonusSoftwareUpgradeSucceededNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-SOFTWARE-UPGRADE-SERVICES-MIB", "sonusSwUpgradeShelfAdmnDirectory"),
        ("SONUS-SOFTWARE-UPGRADE-SERVICES-MIB", "sonusSwUpgradeShelfStatLastReason"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSoftwareUpgradeSucceededNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-SOFTWARE-UPGRADE-SERVICES-MIB",
    **{"SonusSoftwareUpgradeState": SonusSoftwareUpgradeState,
       "sonusSoftwareUpgradeServicesMIB": sonusSoftwareUpgradeServicesMIB,
       "sonusSoftwareUpgradeServicesMIBObjects": sonusSoftwareUpgradeServicesMIBObjects,
       "sonusSwUpgradeShelfAdmnTable": sonusSwUpgradeShelfAdmnTable,
       "sonusSwUpgradeShelfAdmnEntry": sonusSwUpgradeShelfAdmnEntry,
       "sonusSwUpgradeShelfAdmnShelfIndex": sonusSwUpgradeShelfAdmnShelfIndex,
       "sonusSwUpgradeShelfAdmnInit": sonusSwUpgradeShelfAdmnInit,
       "sonusSwUpgradeShelfAdmnUpgradeNow": sonusSwUpgradeShelfAdmnUpgradeNow,
       "sonusSwUpgradeShelfAdmnHalt": sonusSwUpgradeShelfAdmnHalt,
       "sonusSwUpgradeShelfAdmnCommitDirectory": sonusSwUpgradeShelfAdmnCommitDirectory,
       "sonusSwUpgradeShelfAdmnDirectory": sonusSwUpgradeShelfAdmnDirectory,
       "sonusSwUpgradeShelfAdmnOverrideFeatureCheck": sonusSwUpgradeShelfAdmnOverrideFeatureCheck,
       "sonusSwUpgradeShelfStatTable": sonusSwUpgradeShelfStatTable,
       "sonusSwUpgradeShelfStatEntry": sonusSwUpgradeShelfStatEntry,
       "sonusSwUpgradeShelfStatShelfIndex": sonusSwUpgradeShelfStatShelfIndex,
       "sonusSwUpgradeShelfStatStatus": sonusSwUpgradeShelfStatStatus,
       "sonusSwUpgradeShelfStatCurSlot": sonusSwUpgradeShelfStatCurSlot,
       "sonusSwUpgradeShelfStatSlotRemain": sonusSwUpgradeShelfStatSlotRemain,
       "sonusSwUpgradeShelfStatGroupRemain": sonusSwUpgradeShelfStatGroupRemain,
       "sonusSwUpgradeShelfStatDuration": sonusSwUpgradeShelfStatDuration,
       "sonusSwUpgradeShelfStatStartTime": sonusSwUpgradeShelfStatStartTime,
       "sonusSwUpgradeShelfStatLastReason": sonusSwUpgradeShelfStatLastReason,
       "sonusSwUpgradeShelfStatLastState": sonusSwUpgradeShelfStatLastState,
       "sonusSwUpgradeShelfStatState": sonusSwUpgradeShelfStatState,
       "sonusSwUpgradeSlotStatTable": sonusSwUpgradeSlotStatTable,
       "sonusSwUpgradeSlotStatEntry": sonusSwUpgradeSlotStatEntry,
       "sonusSwUpgradeSlotStatShelfIndex": sonusSwUpgradeSlotStatShelfIndex,
       "sonusSwUpgradeSlotStatSlotIndex": sonusSwUpgradeSlotStatSlotIndex,
       "sonusSwUpgradeSlotStatStatus": sonusSwUpgradeSlotStatStatus,
       "sonusSwUpgradeSlotStatUpgrade": sonusSwUpgradeSlotStatUpgrade,
       "sonusSwUpgradeSlotStatVersion": sonusSwUpgradeSlotStatVersion,
       "sonusSoftwareUpgradeServicesMIBNotifications": sonusSoftwareUpgradeServicesMIBNotifications,
       "sonusSoftwareUpgradeServicesMIBNotificationsPrefix": sonusSoftwareUpgradeServicesMIBNotificationsPrefix,
       "sonusSoftwareUpgradeInitiatedNotification": sonusSoftwareUpgradeInitiatedNotification,
       "sonusSoftwareUpgradeTerminatedNotification": sonusSoftwareUpgradeTerminatedNotification,
       "sonusSoftwareUpgradeSucceededNotification": sonusSoftwareUpgradeSucceededNotification,
       "sonusSoftwareUpgradeServicesMIBNotificationsObjects": sonusSoftwareUpgradeServicesMIBNotificationsObjects}
)
