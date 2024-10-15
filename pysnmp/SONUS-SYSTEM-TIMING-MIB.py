# SNMP MIB module (SONUS-SYSTEM-TIMING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-SYSTEM-TIMING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:12 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(sonusEventClass,
 sonusEventDescription,
 sonusEventLevel,
 sonusShelfIndex,
 sonusSlotIndex) = mibBuilder.importSymbols(
    "SONUS-COMMON-MIB",
    "sonusEventClass",
    "sonusEventDescription",
    "sonusEventLevel",
    "sonusShelfIndex",
    "sonusSlotIndex")

(sonusSystemMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusSystemMIBs")

(HwTypeID,
 SonusAdminState,
 SonusEventString,
 SonusMtaSlotIndex,
 SonusShelfIndex,
 SonusSlotIndex,
 SonusTimingSource) = mibBuilder.importSymbols(
    "SONUS-TC",
    "HwTypeID",
    "SonusAdminState",
    "SonusEventString",
    "SonusMtaSlotIndex",
    "SonusShelfIndex",
    "SonusSlotIndex",
    "SonusTimingSource")


# MODULE-IDENTITY

sonusSystemTimingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusSystemTimingMIBObjects_ObjectIdentity = ObjectIdentity
sonusSystemTimingMIBObjects = _SonusSystemTimingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1)
)
_SonusStShelfAdmnTable_Object = MibTable
sonusStShelfAdmnTable = _SonusStShelfAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    sonusStShelfAdmnTable.setStatus("current")
_SonusStShelfAdmnEntry_Object = MibTableRow
sonusStShelfAdmnEntry = _SonusStShelfAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 1, 1)
)
sonusStShelfAdmnEntry.setIndexNames(
    (0, "SONUS-SYSTEM-TIMING-MIB", "sonusStShelfAdmnShelfIndex"),
)
if mibBuilder.loadTexts:
    sonusStShelfAdmnEntry.setStatus("current")
_SonusStShelfAdmnShelfIndex_Type = SonusShelfIndex
_SonusStShelfAdmnShelfIndex_Object = MibTableColumn
sonusStShelfAdmnShelfIndex = _SonusStShelfAdmnShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 1, 1, 1),
    _SonusStShelfAdmnShelfIndex_Type()
)
sonusStShelfAdmnShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStShelfAdmnShelfIndex.setStatus("current")


class _SonusStShelfAdmnFailoverGuardTime_Type(Integer32):
    """Custom type sonusStShelfAdmnFailoverGuardTime based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_SonusStShelfAdmnFailoverGuardTime_Type.__name__ = "Integer32"
_SonusStShelfAdmnFailoverGuardTime_Object = MibTableColumn
sonusStShelfAdmnFailoverGuardTime = _SonusStShelfAdmnFailoverGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 1, 1, 2),
    _SonusStShelfAdmnFailoverGuardTime_Type()
)
sonusStShelfAdmnFailoverGuardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStShelfAdmnFailoverGuardTime.setStatus("current")


class _SonusStShelfAdmnRecoveryGuardTime_Type(Integer32):
    """Custom type sonusStShelfAdmnRecoveryGuardTime based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 120),
    )


_SonusStShelfAdmnRecoveryGuardTime_Type.__name__ = "Integer32"
_SonusStShelfAdmnRecoveryGuardTime_Object = MibTableColumn
sonusStShelfAdmnRecoveryGuardTime = _SonusStShelfAdmnRecoveryGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 1, 1, 3),
    _SonusStShelfAdmnRecoveryGuardTime_Type()
)
sonusStShelfAdmnRecoveryGuardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStShelfAdmnRecoveryGuardTime.setStatus("current")


class _SonusStShelfAdmnTransmitRemoteAlarm_Type(Integer32):
    """Custom type sonusStShelfAdmnTransmitRemoteAlarm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusStShelfAdmnTransmitRemoteAlarm_Type.__name__ = "Integer32"
_SonusStShelfAdmnTransmitRemoteAlarm_Object = MibTableColumn
sonusStShelfAdmnTransmitRemoteAlarm = _SonusStShelfAdmnTransmitRemoteAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 1, 1, 4),
    _SonusStShelfAdmnTransmitRemoteAlarm_Type()
)
sonusStShelfAdmnTransmitRemoteAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStShelfAdmnTransmitRemoteAlarm.setStatus("current")


class _SonusStShelfAdmnRevertRefSwitching_Type(Integer32):
    """Custom type sonusStShelfAdmnRevertRefSwitching based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusStShelfAdmnRevertRefSwitching_Type.__name__ = "Integer32"
_SonusStShelfAdmnRevertRefSwitching_Object = MibTableColumn
sonusStShelfAdmnRevertRefSwitching = _SonusStShelfAdmnRevertRefSwitching_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 1, 1, 5),
    _SonusStShelfAdmnRevertRefSwitching_Type()
)
sonusStShelfAdmnRevertRefSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStShelfAdmnRevertRefSwitching.setStatus("current")


class _SonusStShelfAdmnRevertMtaSwitching_Type(Integer32):
    """Custom type sonusStShelfAdmnRevertMtaSwitching based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusStShelfAdmnRevertMtaSwitching_Type.__name__ = "Integer32"
_SonusStShelfAdmnRevertMtaSwitching_Object = MibTableColumn
sonusStShelfAdmnRevertMtaSwitching = _SonusStShelfAdmnRevertMtaSwitching_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 1, 1, 6),
    _SonusStShelfAdmnRevertMtaSwitching_Type()
)
sonusStShelfAdmnRevertMtaSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStShelfAdmnRevertMtaSwitching.setStatus("current")


class _SonusStShelfAdmnRevertInsertDelay_Type(Integer32):
    """Custom type sonusStShelfAdmnRevertInsertDelay based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 300),
    )


_SonusStShelfAdmnRevertInsertDelay_Type.__name__ = "Integer32"
_SonusStShelfAdmnRevertInsertDelay_Object = MibTableColumn
sonusStShelfAdmnRevertInsertDelay = _SonusStShelfAdmnRevertInsertDelay_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 1, 1, 7),
    _SonusStShelfAdmnRevertInsertDelay_Type()
)
sonusStShelfAdmnRevertInsertDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStShelfAdmnRevertInsertDelay.setStatus("current")


class _SonusStShelfAdmnFreeRunAlarm_Type(Integer32):
    """Custom type sonusStShelfAdmnFreeRunAlarm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusStShelfAdmnFreeRunAlarm_Type.__name__ = "Integer32"
_SonusStShelfAdmnFreeRunAlarm_Object = MibTableColumn
sonusStShelfAdmnFreeRunAlarm = _SonusStShelfAdmnFreeRunAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 1, 1, 8),
    _SonusStShelfAdmnFreeRunAlarm_Type()
)
sonusStShelfAdmnFreeRunAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStShelfAdmnFreeRunAlarm.setStatus("current")


class _SonusStShelfAdmnTimingSourceAction_Type(Integer32):
    """Custom type sonusStShelfAdmnTimingSourceAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("resequence", 2))
    )


_SonusStShelfAdmnTimingSourceAction_Type.__name__ = "Integer32"
_SonusStShelfAdmnTimingSourceAction_Object = MibTableColumn
sonusStShelfAdmnTimingSourceAction = _SonusStShelfAdmnTimingSourceAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 1, 1, 9),
    _SonusStShelfAdmnTimingSourceAction_Type()
)
sonusStShelfAdmnTimingSourceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStShelfAdmnTimingSourceAction.setStatus("current")
_SonusStShelfAdmnRowStatus_Type = RowStatus
_SonusStShelfAdmnRowStatus_Object = MibTableColumn
sonusStShelfAdmnRowStatus = _SonusStShelfAdmnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 1, 1, 10),
    _SonusStShelfAdmnRowStatus_Type()
)
sonusStShelfAdmnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStShelfAdmnRowStatus.setStatus("current")


class _SonusStShelfAdmnSourceReconfigAlg_Type(Integer32):
    """Custom type sonusStShelfAdmnSourceReconfigAlg based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ordered-list", 1),
          ("ssm-quality", 2))
    )


_SonusStShelfAdmnSourceReconfigAlg_Type.__name__ = "Integer32"
_SonusStShelfAdmnSourceReconfigAlg_Object = MibTableColumn
sonusStShelfAdmnSourceReconfigAlg = _SonusStShelfAdmnSourceReconfigAlg_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 1, 1, 11),
    _SonusStShelfAdmnSourceReconfigAlg_Type()
)
sonusStShelfAdmnSourceReconfigAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStShelfAdmnSourceReconfigAlg.setStatus("current")


class _SonusStShelfAdmnMtaSourceAffinity_Type(Integer32):
    """Custom type sonusStShelfAdmnMtaSourceAffinity based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("sticky", 2))
    )


_SonusStShelfAdmnMtaSourceAffinity_Type.__name__ = "Integer32"
_SonusStShelfAdmnMtaSourceAffinity_Object = MibTableColumn
sonusStShelfAdmnMtaSourceAffinity = _SonusStShelfAdmnMtaSourceAffinity_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 1, 1, 12),
    _SonusStShelfAdmnMtaSourceAffinity_Type()
)
sonusStShelfAdmnMtaSourceAffinity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStShelfAdmnMtaSourceAffinity.setStatus("current")
_SonusStShelfStatTable_Object = MibTable
sonusStShelfStatTable = _SonusStShelfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    sonusStShelfStatTable.setStatus("current")
_SonusStShelfStatEntry_Object = MibTableRow
sonusStShelfStatEntry = _SonusStShelfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 2, 1)
)
sonusStShelfStatEntry.setIndexNames(
    (0, "SONUS-SYSTEM-TIMING-MIB", "sonusStShelfStatShelfIndex"),
)
if mibBuilder.loadTexts:
    sonusStShelfStatEntry.setStatus("current")
_SonusStShelfStatShelfIndex_Type = SonusShelfIndex
_SonusStShelfStatShelfIndex_Object = MibTableColumn
sonusStShelfStatShelfIndex = _SonusStShelfStatShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 2, 1, 1),
    _SonusStShelfStatShelfIndex_Type()
)
sonusStShelfStatShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStShelfStatShelfIndex.setStatus("current")
_SonusStShelfStatActiveMtaSlot_Type = SonusMtaSlotIndex
_SonusStShelfStatActiveMtaSlot_Object = MibTableColumn
sonusStShelfStatActiveMtaSlot = _SonusStShelfStatActiveMtaSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 2, 1, 2),
    _SonusStShelfStatActiveMtaSlot_Type()
)
sonusStShelfStatActiveMtaSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStShelfStatActiveMtaSlot.setStatus("current")
_SonusStShelfStatActiveSource_Type = SonusTimingSource
_SonusStShelfStatActiveSource_Object = MibTableColumn
sonusStShelfStatActiveSource = _SonusStShelfStatActiveSource_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 2, 1, 3),
    _SonusStShelfStatActiveSource_Type()
)
sonusStShelfStatActiveSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStShelfStatActiveSource.setStatus("current")
_SonusStMtaAdmnTable_Object = MibTable
sonusStMtaAdmnTable = _SonusStMtaAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    sonusStMtaAdmnTable.setStatus("current")
_SonusStMtaAdmnEntry_Object = MibTableRow
sonusStMtaAdmnEntry = _SonusStMtaAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 3, 1)
)
sonusStMtaAdmnEntry.setIndexNames(
    (0, "SONUS-SYSTEM-TIMING-MIB", "sonusStMtaAdmnShelfIndex"),
    (0, "SONUS-SYSTEM-TIMING-MIB", "sonusStMtaAdmnMtaSlotIndex"),
)
if mibBuilder.loadTexts:
    sonusStMtaAdmnEntry.setStatus("current")
_SonusStMtaAdmnShelfIndex_Type = SonusShelfIndex
_SonusStMtaAdmnShelfIndex_Object = MibTableColumn
sonusStMtaAdmnShelfIndex = _SonusStMtaAdmnShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 3, 1, 1),
    _SonusStMtaAdmnShelfIndex_Type()
)
sonusStMtaAdmnShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStMtaAdmnShelfIndex.setStatus("current")
_SonusStMtaAdmnMtaSlotIndex_Type = SonusMtaSlotIndex
_SonusStMtaAdmnMtaSlotIndex_Object = MibTableColumn
sonusStMtaAdmnMtaSlotIndex = _SonusStMtaAdmnMtaSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 3, 1, 2),
    _SonusStMtaAdmnMtaSlotIndex_Type()
)
sonusStMtaAdmnMtaSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStMtaAdmnMtaSlotIndex.setStatus("current")


class _SonusStMtaAdmnState_Type(SonusAdminState):
    """Custom type sonusStMtaAdmnState based on SonusAdminState"""


_SonusStMtaAdmnState_Object = MibTableColumn
sonusStMtaAdmnState = _SonusStMtaAdmnState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 3, 1, 3),
    _SonusStMtaAdmnState_Type()
)
sonusStMtaAdmnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStMtaAdmnState.setStatus("current")


class _SonusStMtaAdmnLineEncoding_Type(Integer32):
    """Custom type sonusStMtaAdmnLineEncoding based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("b8zs", 2),
          ("hdb3", 3))
    )


_SonusStMtaAdmnLineEncoding_Type.__name__ = "Integer32"
_SonusStMtaAdmnLineEncoding_Object = MibTableColumn
sonusStMtaAdmnLineEncoding = _SonusStMtaAdmnLineEncoding_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 3, 1, 4),
    _SonusStMtaAdmnLineEncoding_Type()
)
sonusStMtaAdmnLineEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStMtaAdmnLineEncoding.setStatus("current")


class _SonusStMtaAdmnSsmChannelBit_Type(Integer32):
    """Custom type sonusStMtaAdmnSsmChannelBit based on Integer32"""
    defaultValue = 1

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
        *(("sa4", 1),
          ("sa5", 2),
          ("sa6", 3),
          ("sa7", 4),
          ("sa8", 5))
    )


_SonusStMtaAdmnSsmChannelBit_Type.__name__ = "Integer32"
_SonusStMtaAdmnSsmChannelBit_Object = MibTableColumn
sonusStMtaAdmnSsmChannelBit = _SonusStMtaAdmnSsmChannelBit_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 3, 1, 5),
    _SonusStMtaAdmnSsmChannelBit_Type()
)
sonusStMtaAdmnSsmChannelBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStMtaAdmnSsmChannelBit.setStatus("current")


class _SonusStMtaAdmnFramerMode_Type(Integer32):
    """Custom type sonusStMtaAdmnFramerMode based on Integer32"""
    defaultValue = 2

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
        *(("d4sf", 1),
          ("esf", 2),
          ("mf", 3),
          ("mf-crc4", 4))
    )


_SonusStMtaAdmnFramerMode_Type.__name__ = "Integer32"
_SonusStMtaAdmnFramerMode_Object = MibTableColumn
sonusStMtaAdmnFramerMode = _SonusStMtaAdmnFramerMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 3, 1, 6),
    _SonusStMtaAdmnFramerMode_Type()
)
sonusStMtaAdmnFramerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStMtaAdmnFramerMode.setStatus("current")


class _SonusStMtaAdmnFramerTransmitYellowAlarm_Type(Integer32):
    """Custom type sonusStMtaAdmnFramerTransmitYellowAlarm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusStMtaAdmnFramerTransmitYellowAlarm_Type.__name__ = "Integer32"
_SonusStMtaAdmnFramerTransmitYellowAlarm_Object = MibTableColumn
sonusStMtaAdmnFramerTransmitYellowAlarm = _SonusStMtaAdmnFramerTransmitYellowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 3, 1, 7),
    _SonusStMtaAdmnFramerTransmitYellowAlarm_Type()
)
sonusStMtaAdmnFramerTransmitYellowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStMtaAdmnFramerTransmitYellowAlarm.setStatus("current")


class _SonusStMtaAdmnLiuTransmitAllOnes_Type(Integer32):
    """Custom type sonusStMtaAdmnLiuTransmitAllOnes based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusStMtaAdmnLiuTransmitAllOnes_Type.__name__ = "Integer32"
_SonusStMtaAdmnLiuTransmitAllOnes_Object = MibTableColumn
sonusStMtaAdmnLiuTransmitAllOnes = _SonusStMtaAdmnLiuTransmitAllOnes_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 3, 1, 8),
    _SonusStMtaAdmnLiuTransmitAllOnes_Type()
)
sonusStMtaAdmnLiuTransmitAllOnes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStMtaAdmnLiuTransmitAllOnes.setStatus("current")


class _SonusStMtaAdmnAction_Type(Integer32):
    """Custom type sonusStMtaAdmnAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("none", 1))
    )


_SonusStMtaAdmnAction_Type.__name__ = "Integer32"
_SonusStMtaAdmnAction_Object = MibTableColumn
sonusStMtaAdmnAction = _SonusStMtaAdmnAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 3, 1, 9),
    _SonusStMtaAdmnAction_Type()
)
sonusStMtaAdmnAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStMtaAdmnAction.setStatus("current")
_SonusStMtaAdmnRowStatus_Type = RowStatus
_SonusStMtaAdmnRowStatus_Object = MibTableColumn
sonusStMtaAdmnRowStatus = _SonusStMtaAdmnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 3, 1, 10),
    _SonusStMtaAdmnRowStatus_Type()
)
sonusStMtaAdmnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStMtaAdmnRowStatus.setStatus("current")
_SonusStMtaStatTable_Object = MibTable
sonusStMtaStatTable = _SonusStMtaStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    sonusStMtaStatTable.setStatus("current")
_SonusStMtaStatEntry_Object = MibTableRow
sonusStMtaStatEntry = _SonusStMtaStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 4, 1)
)
sonusStMtaStatEntry.setIndexNames(
    (0, "SONUS-SYSTEM-TIMING-MIB", "sonusStMtaStatShelfIndex"),
    (0, "SONUS-SYSTEM-TIMING-MIB", "sonusStMtaStatMtaSlotIndex"),
)
if mibBuilder.loadTexts:
    sonusStMtaStatEntry.setStatus("current")
_SonusStMtaStatShelfIndex_Type = SonusShelfIndex
_SonusStMtaStatShelfIndex_Object = MibTableColumn
sonusStMtaStatShelfIndex = _SonusStMtaStatShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 4, 1, 1),
    _SonusStMtaStatShelfIndex_Type()
)
sonusStMtaStatShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStMtaStatShelfIndex.setStatus("current")
_SonusStMtaStatMtaSlotIndex_Type = SonusMtaSlotIndex
_SonusStMtaStatMtaSlotIndex_Object = MibTableColumn
sonusStMtaStatMtaSlotIndex = _SonusStMtaStatMtaSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 4, 1, 2),
    _SonusStMtaStatMtaSlotIndex_Type()
)
sonusStMtaStatMtaSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStMtaStatMtaSlotIndex.setStatus("current")


class _SonusStMtaStatOperStat_Type(Integer32):
    """Custom type sonusStMtaStatOperStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("available", 6),
          ("fault", 2),
          ("inService", 4),
          ("notPresent", 1),
          ("outOfService", 5),
          ("warmupDelay", 3))
    )


_SonusStMtaStatOperStat_Type.__name__ = "Integer32"
_SonusStMtaStatOperStat_Object = MibTableColumn
sonusStMtaStatOperStat = _SonusStMtaStatOperStat_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 4, 1, 3),
    _SonusStMtaStatOperStat_Type()
)
sonusStMtaStatOperStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStMtaStatOperStat.setStatus("current")


class _SonusStMtaStatMtaHwDesc_Type(DisplayString):
    """Custom type sonusStMtaStatMtaHwDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SonusStMtaStatMtaHwDesc_Type.__name__ = "DisplayString"
_SonusStMtaStatMtaHwDesc_Object = MibTableColumn
sonusStMtaStatMtaHwDesc = _SonusStMtaStatMtaHwDesc_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 4, 1, 4),
    _SonusStMtaStatMtaHwDesc_Type()
)
sonusStMtaStatMtaHwDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStMtaStatMtaHwDesc.setStatus("current")
_SonusStMtaStatMtaHwType_Type = HwTypeID
_SonusStMtaStatMtaHwType_Object = MibTableColumn
sonusStMtaStatMtaHwType = _SonusStMtaStatMtaHwType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 4, 1, 5),
    _SonusStMtaStatMtaHwType_Type()
)
sonusStMtaStatMtaHwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStMtaStatMtaHwType.setStatus("current")
_SonusStMtaStatMtaHwTypeRev_Type = Integer32
_SonusStMtaStatMtaHwTypeRev_Object = MibTableColumn
sonusStMtaStatMtaHwTypeRev = _SonusStMtaStatMtaHwTypeRev_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 4, 1, 6),
    _SonusStMtaStatMtaHwTypeRev_Type()
)
sonusStMtaStatMtaHwTypeRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStMtaStatMtaHwTypeRev.setStatus("current")


class _SonusStMtaStatMtaSerialNum_Type(DisplayString):
    """Custom type sonusStMtaStatMtaSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SonusStMtaStatMtaSerialNum_Type.__name__ = "DisplayString"
_SonusStMtaStatMtaSerialNum_Object = MibTableColumn
sonusStMtaStatMtaSerialNum = _SonusStMtaStatMtaSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 4, 1, 7),
    _SonusStMtaStatMtaSerialNum_Type()
)
sonusStMtaStatMtaSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStMtaStatMtaSerialNum.setStatus("current")


class _SonusStMtaStatMtaPartNum_Type(DisplayString):
    """Custom type sonusStMtaStatMtaPartNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SonusStMtaStatMtaPartNum_Type.__name__ = "DisplayString"
_SonusStMtaStatMtaPartNum_Object = MibTableColumn
sonusStMtaStatMtaPartNum = _SonusStMtaStatMtaPartNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 4, 1, 8),
    _SonusStMtaStatMtaPartNum_Type()
)
sonusStMtaStatMtaPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStMtaStatMtaPartNum.setStatus("current")
_SonusStTimingSourceTable_Object = MibTable
sonusStTimingSourceTable = _SonusStTimingSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 5)
)
if mibBuilder.loadTexts:
    sonusStTimingSourceTable.setStatus("current")
_SonusStTimingSourceEntry_Object = MibTableRow
sonusStTimingSourceEntry = _SonusStTimingSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 5, 1)
)
sonusStTimingSourceEntry.setIndexNames(
    (0, "SONUS-SYSTEM-TIMING-MIB", "sonusStTimingSourceShelfIndex"),
    (0, "SONUS-SYSTEM-TIMING-MIB", "sonusStTimingSourceMtaSlotIndex"),
    (0, "SONUS-SYSTEM-TIMING-MIB", "sonusStTimingSource"),
)
if mibBuilder.loadTexts:
    sonusStTimingSourceEntry.setStatus("current")
_SonusStTimingSourceShelfIndex_Type = SonusShelfIndex
_SonusStTimingSourceShelfIndex_Object = MibTableColumn
sonusStTimingSourceShelfIndex = _SonusStTimingSourceShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 5, 1, 1),
    _SonusStTimingSourceShelfIndex_Type()
)
sonusStTimingSourceShelfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStTimingSourceShelfIndex.setStatus("current")


class _SonusStTimingSourceMtaSlotIndex_Type(Integer32):
    """Custom type sonusStTimingSourceMtaSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SonusStTimingSourceMtaSlotIndex_Type.__name__ = "Integer32"
_SonusStTimingSourceMtaSlotIndex_Object = MibTableColumn
sonusStTimingSourceMtaSlotIndex = _SonusStTimingSourceMtaSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 5, 1, 2),
    _SonusStTimingSourceMtaSlotIndex_Type()
)
sonusStTimingSourceMtaSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStTimingSourceMtaSlotIndex.setStatus("current")


class _SonusStTimingSource_Type(SonusTimingSource):
    """Custom type sonusStTimingSource based on SonusTimingSource"""


_SonusStTimingSource_Object = MibTableColumn
sonusStTimingSource = _SonusStTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 5, 1, 3),
    _SonusStTimingSource_Type()
)
sonusStTimingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStTimingSource.setStatus("current")


class _SonusStTimingSourceState_Type(SonusAdminState):
    """Custom type sonusStTimingSourceState based on SonusAdminState"""


_SonusStTimingSourceState_Object = MibTableColumn
sonusStTimingSourceState = _SonusStTimingSourceState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 5, 1, 4),
    _SonusStTimingSourceState_Type()
)
sonusStTimingSourceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStTimingSourceState.setStatus("current")


class _SonusStTimingSourceSequenceNum_Type(Integer32):
    """Custom type sonusStTimingSourceSequenceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SonusStTimingSourceSequenceNum_Type.__name__ = "Integer32"
_SonusStTimingSourceSequenceNum_Object = MibTableColumn
sonusStTimingSourceSequenceNum = _SonusStTimingSourceSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 5, 1, 5),
    _SonusStTimingSourceSequenceNum_Type()
)
sonusStTimingSourceSequenceNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStTimingSourceSequenceNum.setStatus("current")


class _SonusStTimingSourceAction_Type(Integer32):
    """Custom type sonusStTimingSourceAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("none", 1))
    )


_SonusStTimingSourceAction_Type.__name__ = "Integer32"
_SonusStTimingSourceAction_Object = MibTableColumn
sonusStTimingSourceAction = _SonusStTimingSourceAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 5, 1, 6),
    _SonusStTimingSourceAction_Type()
)
sonusStTimingSourceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStTimingSourceAction.setStatus("current")
_SonusStTimingSourceRowStatus_Type = RowStatus
_SonusStTimingSourceRowStatus_Object = MibTableColumn
sonusStTimingSourceRowStatus = _SonusStTimingSourceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 5, 1, 7),
    _SonusStTimingSourceRowStatus_Type()
)
sonusStTimingSourceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStTimingSourceRowStatus.setStatus("current")
_SonusStTimingSourceStatTable_Object = MibTable
sonusStTimingSourceStatTable = _SonusStTimingSourceStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 6)
)
if mibBuilder.loadTexts:
    sonusStTimingSourceStatTable.setStatus("current")
_SonusStTimingSourceStatEntry_Object = MibTableRow
sonusStTimingSourceStatEntry = _SonusStTimingSourceStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 6, 1)
)
sonusStTimingSourceStatEntry.setIndexNames(
    (0, "SONUS-SYSTEM-TIMING-MIB", "sonusStTimingSourceStatShelfIndex"),
    (0, "SONUS-SYSTEM-TIMING-MIB", "sonusStTimingSourceStatMtaSlotIndex"),
    (0, "SONUS-SYSTEM-TIMING-MIB", "sonusStTimingSourceStat"),
)
if mibBuilder.loadTexts:
    sonusStTimingSourceStatEntry.setStatus("current")
_SonusStTimingSourceStatShelfIndex_Type = SonusShelfIndex
_SonusStTimingSourceStatShelfIndex_Object = MibTableColumn
sonusStTimingSourceStatShelfIndex = _SonusStTimingSourceStatShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 6, 1, 1),
    _SonusStTimingSourceStatShelfIndex_Type()
)
sonusStTimingSourceStatShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStTimingSourceStatShelfIndex.setStatus("current")
_SonusStTimingSourceStatMtaSlotIndex_Type = SonusMtaSlotIndex
_SonusStTimingSourceStatMtaSlotIndex_Object = MibTableColumn
sonusStTimingSourceStatMtaSlotIndex = _SonusStTimingSourceStatMtaSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 6, 1, 2),
    _SonusStTimingSourceStatMtaSlotIndex_Type()
)
sonusStTimingSourceStatMtaSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStTimingSourceStatMtaSlotIndex.setStatus("current")


class _SonusStTimingSourceStat_Type(SonusTimingSource):
    """Custom type sonusStTimingSourceStat based on SonusTimingSource"""


_SonusStTimingSourceStat_Object = MibTableColumn
sonusStTimingSourceStat = _SonusStTimingSourceStat_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 6, 1, 3),
    _SonusStTimingSourceStat_Type()
)
sonusStTimingSourceStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStTimingSourceStat.setStatus("current")


class _SonusStTimingSourceStatState_Type(Integer32):
    """Custom type sonusStTimingSourceStatState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("cannotlocate", 5),
          ("faulting", 3),
          ("inservice", 2),
          ("notpresent", 6),
          ("outofservice", 4))
    )


_SonusStTimingSourceStatState_Type.__name__ = "Integer32"
_SonusStTimingSourceStatState_Object = MibTableColumn
sonusStTimingSourceStatState = _SonusStTimingSourceStatState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 6, 1, 4),
    _SonusStTimingSourceStatState_Type()
)
sonusStTimingSourceStatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStTimingSourceStatState.setStatus("current")


class _SonusStTimingSourceStatTraceability_Type(Integer32):
    """Custom type sonusStTimingSourceStatTraceability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("dontUse", 10),
          ("g704rsvdql1", 17),
          ("g704rsvdql10", 23),
          ("g704rsvdql12", 24),
          ("g704rsvdql13", 25),
          ("g704rsvdql14", 26),
          ("g704rsvdql3", 18),
          ("g704rsvdql5", 19),
          ("g704rsvdql6", 20),
          ("g704rsvdql7", 21),
          ("g704rsvdql9", 22),
          ("g811", 13),
          ("g812local", 15),
          ("g812transit", 14),
          ("indeterminate", 11),
          ("qualityunknown", 12),
          ("reserved", 9),
          ("sets", 16),
          ("stratum1", 2),
          ("stratum2", 3),
          ("stratum3", 6),
          ("stratum3e", 5),
          ("stratum4", 8),
          ("stratumSonetMinimum", 7),
          ("stratumTNC", 4),
          ("synchronizedunknown", 1))
    )


_SonusStTimingSourceStatTraceability_Type.__name__ = "Integer32"
_SonusStTimingSourceStatTraceability_Object = MibTableColumn
sonusStTimingSourceStatTraceability = _SonusStTimingSourceStatTraceability_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 6, 1, 5),
    _SonusStTimingSourceStatTraceability_Type()
)
sonusStTimingSourceStatTraceability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStTimingSourceStatTraceability.setStatus("current")


class _SonusStTimingSourceStatLineState_Type(Integer32):
    """Custom type sonusStTimingSourceStatLineState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notvalid", 2),
          ("valid", 1))
    )


_SonusStTimingSourceStatLineState_Type.__name__ = "Integer32"
_SonusStTimingSourceStatLineState_Object = MibTableColumn
sonusStTimingSourceStatLineState = _SonusStTimingSourceStatLineState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 6, 1, 6),
    _SonusStTimingSourceStatLineState_Type()
)
sonusStTimingSourceStatLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStTimingSourceStatLineState.setStatus("current")
_SonusStChannelBindingTable_Object = MibTable
sonusStChannelBindingTable = _SonusStChannelBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 7)
)
if mibBuilder.loadTexts:
    sonusStChannelBindingTable.setStatus("current")
_SonusStChannelBindingEntry_Object = MibTableRow
sonusStChannelBindingEntry = _SonusStChannelBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 7, 1)
)
sonusStChannelBindingEntry.setIndexNames(
    (0, "SONUS-SYSTEM-TIMING-MIB", "sonusStChannelBindingShelfIndex"),
    (0, "SONUS-SYSTEM-TIMING-MIB", "sonusStChannelBindingSlotIndex"),
    (0, "SONUS-SYSTEM-TIMING-MIB", "sonusStChannelBindingChannel"),
    (0, "SONUS-SYSTEM-TIMING-MIB", "sonusStChannelBindingRefClk"),
)
if mibBuilder.loadTexts:
    sonusStChannelBindingEntry.setStatus("current")
_SonusStChannelBindingShelfIndex_Type = SonusShelfIndex
_SonusStChannelBindingShelfIndex_Object = MibTableColumn
sonusStChannelBindingShelfIndex = _SonusStChannelBindingShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 7, 1, 1),
    _SonusStChannelBindingShelfIndex_Type()
)
sonusStChannelBindingShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStChannelBindingShelfIndex.setStatus("current")
_SonusStChannelBindingSlotIndex_Type = SonusSlotIndex
_SonusStChannelBindingSlotIndex_Object = MibTableColumn
sonusStChannelBindingSlotIndex = _SonusStChannelBindingSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 7, 1, 2),
    _SonusStChannelBindingSlotIndex_Type()
)
sonusStChannelBindingSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStChannelBindingSlotIndex.setStatus("current")
_SonusStChannelBindingChannel_Type = Integer32
_SonusStChannelBindingChannel_Object = MibTableColumn
sonusStChannelBindingChannel = _SonusStChannelBindingChannel_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 7, 1, 3),
    _SonusStChannelBindingChannel_Type()
)
sonusStChannelBindingChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStChannelBindingChannel.setStatus("current")


class _SonusStChannelBindingRefClk_Type(Integer32):
    """Custom type sonusStChannelBindingRefClk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("refClkA", 1),
          ("refClkB", 2))
    )


_SonusStChannelBindingRefClk_Type.__name__ = "Integer32"
_SonusStChannelBindingRefClk_Object = MibTableColumn
sonusStChannelBindingRefClk = _SonusStChannelBindingRefClk_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 7, 1, 4),
    _SonusStChannelBindingRefClk_Type()
)
sonusStChannelBindingRefClk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusStChannelBindingRefClk.setStatus("current")
_SonusStChannelBindingRowStatus_Type = RowStatus
_SonusStChannelBindingRowStatus_Object = MibTableColumn
sonusStChannelBindingRowStatus = _SonusStChannelBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 1, 7, 1, 5),
    _SonusStChannelBindingRowStatus_Type()
)
sonusStChannelBindingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusStChannelBindingRowStatus.setStatus("current")
_SonusSystemTimingMIBNotifications_ObjectIdentity = ObjectIdentity
sonusSystemTimingMIBNotifications = _SonusSystemTimingMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 2)
)
_SonusSystemTimingMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusSystemTimingMIBNotificationsPrefix = _SonusSystemTimingMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 2, 0)
)
_SonusSystemTimingMIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusSystemTimingMIBNotificationsObjects = _SonusSystemTimingMIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 2, 1)
)
_SonusTimingSource_Type = SonusTimingSource
_SonusTimingSource_Object = MibScalar
sonusTimingSource = _SonusTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 2, 1, 1),
    _SonusTimingSource_Type()
)
sonusTimingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTimingSource.setStatus("current")
_SonusTimingSource2_Type = SonusEventString
_SonusTimingSource2_Object = MibScalar
sonusTimingSource2 = _SonusTimingSource2_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 2, 1, 2),
    _SonusTimingSource2_Type()
)
sonusTimingSource2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTimingSource2.setStatus("current")

# Managed Objects groups


# Notification objects

sonusSystemTimingActiveFailedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 2, 0, 1)
)
sonusSystemTimingActiveFailedNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-SYSTEM-TIMING-MIB", "sonusTimingSource"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSystemTimingActiveFailedNotification.setStatus(
        "current"
    )

sonusSystemTimingActiveSwitchoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 2, 0, 2)
)
sonusSystemTimingActiveSwitchoverNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-SYSTEM-TIMING-MIB", "sonusTimingSource"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSystemTimingActiveSwitchoverNotification.setStatus(
        "current"
    )

sonusSystemTimingOscillatorActiveNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 2, 0, 3)
)
sonusSystemTimingOscillatorActiveNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSystemTimingOscillatorActiveNotification.setStatus(
        "current"
    )

sonusSystemTimingMTAFailedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 2, 0, 4)
)
sonusSystemTimingMTAFailedNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSystemTimingMTAFailedNotification.setStatus(
        "current"
    )

sonusSystemTimingMTAOperationalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 2, 0, 6)
)
sonusSystemTimingMTAOperationalNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSystemTimingMTAOperationalNotification.setStatus(
        "current"
    )

sonusSystemTimingMTATotalFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 3, 2, 0, 7)
)
sonusSystemTimingMTATotalFailureNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSystemTimingMTATotalFailureNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-SYSTEM-TIMING-MIB",
    **{"sonusSystemTimingMIB": sonusSystemTimingMIB,
       "sonusSystemTimingMIBObjects": sonusSystemTimingMIBObjects,
       "sonusStShelfAdmnTable": sonusStShelfAdmnTable,
       "sonusStShelfAdmnEntry": sonusStShelfAdmnEntry,
       "sonusStShelfAdmnShelfIndex": sonusStShelfAdmnShelfIndex,
       "sonusStShelfAdmnFailoverGuardTime": sonusStShelfAdmnFailoverGuardTime,
       "sonusStShelfAdmnRecoveryGuardTime": sonusStShelfAdmnRecoveryGuardTime,
       "sonusStShelfAdmnTransmitRemoteAlarm": sonusStShelfAdmnTransmitRemoteAlarm,
       "sonusStShelfAdmnRevertRefSwitching": sonusStShelfAdmnRevertRefSwitching,
       "sonusStShelfAdmnRevertMtaSwitching": sonusStShelfAdmnRevertMtaSwitching,
       "sonusStShelfAdmnRevertInsertDelay": sonusStShelfAdmnRevertInsertDelay,
       "sonusStShelfAdmnFreeRunAlarm": sonusStShelfAdmnFreeRunAlarm,
       "sonusStShelfAdmnTimingSourceAction": sonusStShelfAdmnTimingSourceAction,
       "sonusStShelfAdmnRowStatus": sonusStShelfAdmnRowStatus,
       "sonusStShelfAdmnSourceReconfigAlg": sonusStShelfAdmnSourceReconfigAlg,
       "sonusStShelfAdmnMtaSourceAffinity": sonusStShelfAdmnMtaSourceAffinity,
       "sonusStShelfStatTable": sonusStShelfStatTable,
       "sonusStShelfStatEntry": sonusStShelfStatEntry,
       "sonusStShelfStatShelfIndex": sonusStShelfStatShelfIndex,
       "sonusStShelfStatActiveMtaSlot": sonusStShelfStatActiveMtaSlot,
       "sonusStShelfStatActiveSource": sonusStShelfStatActiveSource,
       "sonusStMtaAdmnTable": sonusStMtaAdmnTable,
       "sonusStMtaAdmnEntry": sonusStMtaAdmnEntry,
       "sonusStMtaAdmnShelfIndex": sonusStMtaAdmnShelfIndex,
       "sonusStMtaAdmnMtaSlotIndex": sonusStMtaAdmnMtaSlotIndex,
       "sonusStMtaAdmnState": sonusStMtaAdmnState,
       "sonusStMtaAdmnLineEncoding": sonusStMtaAdmnLineEncoding,
       "sonusStMtaAdmnSsmChannelBit": sonusStMtaAdmnSsmChannelBit,
       "sonusStMtaAdmnFramerMode": sonusStMtaAdmnFramerMode,
       "sonusStMtaAdmnFramerTransmitYellowAlarm": sonusStMtaAdmnFramerTransmitYellowAlarm,
       "sonusStMtaAdmnLiuTransmitAllOnes": sonusStMtaAdmnLiuTransmitAllOnes,
       "sonusStMtaAdmnAction": sonusStMtaAdmnAction,
       "sonusStMtaAdmnRowStatus": sonusStMtaAdmnRowStatus,
       "sonusStMtaStatTable": sonusStMtaStatTable,
       "sonusStMtaStatEntry": sonusStMtaStatEntry,
       "sonusStMtaStatShelfIndex": sonusStMtaStatShelfIndex,
       "sonusStMtaStatMtaSlotIndex": sonusStMtaStatMtaSlotIndex,
       "sonusStMtaStatOperStat": sonusStMtaStatOperStat,
       "sonusStMtaStatMtaHwDesc": sonusStMtaStatMtaHwDesc,
       "sonusStMtaStatMtaHwType": sonusStMtaStatMtaHwType,
       "sonusStMtaStatMtaHwTypeRev": sonusStMtaStatMtaHwTypeRev,
       "sonusStMtaStatMtaSerialNum": sonusStMtaStatMtaSerialNum,
       "sonusStMtaStatMtaPartNum": sonusStMtaStatMtaPartNum,
       "sonusStTimingSourceTable": sonusStTimingSourceTable,
       "sonusStTimingSourceEntry": sonusStTimingSourceEntry,
       "sonusStTimingSourceShelfIndex": sonusStTimingSourceShelfIndex,
       "sonusStTimingSourceMtaSlotIndex": sonusStTimingSourceMtaSlotIndex,
       "sonusStTimingSource": sonusStTimingSource,
       "sonusStTimingSourceState": sonusStTimingSourceState,
       "sonusStTimingSourceSequenceNum": sonusStTimingSourceSequenceNum,
       "sonusStTimingSourceAction": sonusStTimingSourceAction,
       "sonusStTimingSourceRowStatus": sonusStTimingSourceRowStatus,
       "sonusStTimingSourceStatTable": sonusStTimingSourceStatTable,
       "sonusStTimingSourceStatEntry": sonusStTimingSourceStatEntry,
       "sonusStTimingSourceStatShelfIndex": sonusStTimingSourceStatShelfIndex,
       "sonusStTimingSourceStatMtaSlotIndex": sonusStTimingSourceStatMtaSlotIndex,
       "sonusStTimingSourceStat": sonusStTimingSourceStat,
       "sonusStTimingSourceStatState": sonusStTimingSourceStatState,
       "sonusStTimingSourceStatTraceability": sonusStTimingSourceStatTraceability,
       "sonusStTimingSourceStatLineState": sonusStTimingSourceStatLineState,
       "sonusStChannelBindingTable": sonusStChannelBindingTable,
       "sonusStChannelBindingEntry": sonusStChannelBindingEntry,
       "sonusStChannelBindingShelfIndex": sonusStChannelBindingShelfIndex,
       "sonusStChannelBindingSlotIndex": sonusStChannelBindingSlotIndex,
       "sonusStChannelBindingChannel": sonusStChannelBindingChannel,
       "sonusStChannelBindingRefClk": sonusStChannelBindingRefClk,
       "sonusStChannelBindingRowStatus": sonusStChannelBindingRowStatus,
       "sonusSystemTimingMIBNotifications": sonusSystemTimingMIBNotifications,
       "sonusSystemTimingMIBNotificationsPrefix": sonusSystemTimingMIBNotificationsPrefix,
       "sonusSystemTimingActiveFailedNotification": sonusSystemTimingActiveFailedNotification,
       "sonusSystemTimingActiveSwitchoverNotification": sonusSystemTimingActiveSwitchoverNotification,
       "sonusSystemTimingOscillatorActiveNotification": sonusSystemTimingOscillatorActiveNotification,
       "sonusSystemTimingMTAFailedNotification": sonusSystemTimingMTAFailedNotification,
       "sonusSystemTimingMTAOperationalNotification": sonusSystemTimingMTAOperationalNotification,
       "sonusSystemTimingMTATotalFailureNotification": sonusSystemTimingMTATotalFailureNotification,
       "sonusSystemTimingMIBNotificationsObjects": sonusSystemTimingMIBNotificationsObjects,
       "sonusTimingSource": sonusTimingSource,
       "sonusTimingSource2": sonusTimingSource2}
)
