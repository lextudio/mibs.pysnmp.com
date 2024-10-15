# SNMP MIB module (CISCO-WAN-VISM-TONE-PLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-VISM-TONE-PLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:00 2024
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

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

vismTonePlanGrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 24)
)
vismTonePlanGrpMIB.setRevisions(
        ("2003-12-17 00:00",
         "2003-04-23 00:00",
         "2002-07-19 00:00",
         "2001-12-26 00:00",
         "2001-08-05 00:00",
         "2001-04-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VismTonePlanGrpMIBObjects_ObjectIdentity = ObjectIdentity
vismTonePlanGrpMIBObjects = _VismTonePlanGrpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1)
)
_VismTonePlan_ObjectIdentity = ObjectIdentity
vismTonePlan = _VismTonePlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1)
)
_VismTonePlanControlGrp_ObjectIdentity = ObjectIdentity
vismTonePlanControlGrp = _VismTonePlanControlGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 1)
)
_TonePlanCurrentSize_Type = Integer32
_TonePlanCurrentSize_Object = MibScalar
tonePlanCurrentSize = _TonePlanCurrentSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 1, 1),
    _TonePlanCurrentSize_Type()
)
tonePlanCurrentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tonePlanCurrentSize.setStatus("current")
_VismTonePlanTableGrp_ObjectIdentity = ObjectIdentity
vismTonePlanTableGrp = _VismTonePlanTableGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2)
)
_VismTonePlanTable_Object = MibTable
vismTonePlanTable = _VismTonePlanTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    vismTonePlanTable.setStatus("current")
_VismTonePlanEntry_Object = MibTableRow
vismTonePlanEntry = _VismTonePlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2, 1, 1)
)
vismTonePlanEntry.setIndexNames(
    (0, "CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanIndex"),
)
if mibBuilder.loadTexts:
    vismTonePlanEntry.setStatus("current")


class _TonePlanIndex_Type(Integer32):
    """Custom type tonePlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TonePlanIndex_Type.__name__ = "Integer32"
_TonePlanIndex_Object = MibTableColumn
tonePlanIndex = _TonePlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2, 1, 1, 1),
    _TonePlanIndex_Type()
)
tonePlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tonePlanIndex.setStatus("current")


class _TonePlanEntryStatus_Type(Integer32):
    """Custom type tonePlanEntryStatus based on Integer32"""
    defaultValue = 1

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
        *(("configured", 2),
          ("lostFile", 4),
          ("reloading", 3),
          ("unused", 1))
    )


_TonePlanEntryStatus_Type.__name__ = "Integer32"
_TonePlanEntryStatus_Object = MibTableColumn
tonePlanEntryStatus = _TonePlanEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2, 1, 1, 2),
    _TonePlanEntryStatus_Type()
)
tonePlanEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tonePlanEntryStatus.setStatus("current")


class _TonePlanProvisionFlag_Type(Integer32):
    """Custom type tonePlanProvisionFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("builtIn", 1),
          ("provisionable", 2))
    )


_TonePlanProvisionFlag_Type.__name__ = "Integer32"
_TonePlanProvisionFlag_Object = MibTableColumn
tonePlanProvisionFlag = _TonePlanProvisionFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2, 1, 1, 3),
    _TonePlanProvisionFlag_Type()
)
tonePlanProvisionFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tonePlanProvisionFlag.setStatus("current")


class _TonePlanRegionName_Type(DisplayString):
    """Custom type tonePlanRegionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TonePlanRegionName_Type.__name__ = "DisplayString"
_TonePlanRegionName_Object = MibTableColumn
tonePlanRegionName = _TonePlanRegionName_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2, 1, 1, 4),
    _TonePlanRegionName_Type()
)
tonePlanRegionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tonePlanRegionName.setStatus("current")


class _TonePlanVersionNumber_Type(Integer32):
    """Custom type tonePlanVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TonePlanVersionNumber_Type.__name__ = "Integer32"
_TonePlanVersionNumber_Object = MibTableColumn
tonePlanVersionNumber = _TonePlanVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2, 1, 1, 5),
    _TonePlanVersionNumber_Type()
)
tonePlanVersionNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tonePlanVersionNumber.setStatus("current")


class _TonePlanFileName_Type(DisplayString):
    """Custom type tonePlanFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TonePlanFileName_Type.__name__ = "DisplayString"
_TonePlanFileName_Object = MibTableColumn
tonePlanFileName = _TonePlanFileName_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2, 1, 1, 6),
    _TonePlanFileName_Type()
)
tonePlanFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tonePlanFileName.setStatus("current")
_VismConfigToneDetectGrp_ObjectIdentity = ObjectIdentity
vismConfigToneDetectGrp = _VismConfigToneDetectGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3)
)
_VismConfigToneDetectTable_Object = MibTable
vismConfigToneDetectTable = _VismConfigToneDetectTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    vismConfigToneDetectTable.setStatus("current")
_VismConfigToneDetectEntry_Object = MibTableRow
vismConfigToneDetectEntry = _VismConfigToneDetectEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1)
)
vismConfigToneDetectEntry.setIndexNames(
    (0, "CISCO-WAN-VISM-TONE-PLAN-MIB", "vismConfigToneDetectNum"),
)
if mibBuilder.loadTexts:
    vismConfigToneDetectEntry.setStatus("current")


class _VismConfigToneDetectNum_Type(Integer32):
    """Custom type vismConfigToneDetectNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_VismConfigToneDetectNum_Type.__name__ = "Integer32"
_VismConfigToneDetectNum_Object = MibTableColumn
vismConfigToneDetectNum = _VismConfigToneDetectNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 1),
    _VismConfigToneDetectNum_Type()
)
vismConfigToneDetectNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismConfigToneDetectNum.setStatus("current")


class _VismEventCode_Type(Integer32):
    """Custom type vismEventCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VismEventCode_Type.__name__ = "Integer32"
_VismEventCode_Object = MibTableColumn
vismEventCode = _VismEventCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 2),
    _VismEventCode_Type()
)
vismEventCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismEventCode.setStatus("current")
_VismConfigToneDetectRowStatus_Type = RowStatus
_VismConfigToneDetectRowStatus_Object = MibTableColumn
vismConfigToneDetectRowStatus = _VismConfigToneDetectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 3),
    _VismConfigToneDetectRowStatus_Type()
)
vismConfigToneDetectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismConfigToneDetectRowStatus.setStatus("current")


class _VismFreqMaxDeviation_Type(Integer32):
    """Custom type vismFreqMaxDeviation based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 125),
    )


_VismFreqMaxDeviation_Type.__name__ = "Integer32"
_VismFreqMaxDeviation_Object = MibTableColumn
vismFreqMaxDeviation = _VismFreqMaxDeviation_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 4),
    _VismFreqMaxDeviation_Type()
)
vismFreqMaxDeviation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismFreqMaxDeviation.setStatus("current")
if mibBuilder.loadTexts:
    vismFreqMaxDeviation.setUnits("Hz")


class _VismFreqMaxPower_Type(Integer32):
    """Custom type vismFreqMaxPower based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_VismFreqMaxPower_Type.__name__ = "Integer32"
_VismFreqMaxPower_Object = MibTableColumn
vismFreqMaxPower = _VismFreqMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 5),
    _VismFreqMaxPower_Type()
)
vismFreqMaxPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismFreqMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    vismFreqMaxPower.setUnits("dB")


class _VismFreqMinPower_Type(Integer32):
    """Custom type vismFreqMinPower based on Integer32"""
    defaultValue = 35

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 35),
    )


_VismFreqMinPower_Type.__name__ = "Integer32"
_VismFreqMinPower_Object = MibTableColumn
vismFreqMinPower = _VismFreqMinPower_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 6),
    _VismFreqMinPower_Type()
)
vismFreqMinPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismFreqMinPower.setStatus("current")
if mibBuilder.loadTexts:
    vismFreqMinPower.setUnits("dB")


class _VismFreqPowerTwist_Type(Integer32):
    """Custom type vismFreqPowerTwist based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_VismFreqPowerTwist_Type.__name__ = "Integer32"
_VismFreqPowerTwist_Object = MibTableColumn
vismFreqPowerTwist = _VismFreqPowerTwist_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 7),
    _VismFreqPowerTwist_Type()
)
vismFreqPowerTwist.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismFreqPowerTwist.setStatus("current")
if mibBuilder.loadTexts:
    vismFreqPowerTwist.setUnits("dB")


class _VismFreqMaxDelay_Type(Integer32):
    """Custom type vismFreqMaxDelay based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VismFreqMaxDelay_Type.__name__ = "Integer32"
_VismFreqMaxDelay_Object = MibTableColumn
vismFreqMaxDelay = _VismFreqMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 8),
    _VismFreqMaxDelay_Type()
)
vismFreqMaxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismFreqMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    vismFreqMaxDelay.setUnits("milliseconds")


class _VismMinOnCadence_Type(Integer32):
    """Custom type vismMinOnCadence based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 100),
    )


_VismMinOnCadence_Type.__name__ = "Integer32"
_VismMinOnCadence_Object = MibTableColumn
vismMinOnCadence = _VismMinOnCadence_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 9),
    _VismMinOnCadence_Type()
)
vismMinOnCadence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismMinOnCadence.setStatus("current")
if mibBuilder.loadTexts:
    vismMinOnCadence.setUnits("milliseconds")


class _VismMaxOffCadence_Type(Integer32):
    """Custom type vismMaxOffCadence based on Integer32"""
    defaultValue = 450

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5000),
    )


_VismMaxOffCadence_Type.__name__ = "Integer32"
_VismMaxOffCadence_Object = MibTableColumn
vismMaxOffCadence = _VismMaxOffCadence_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 10),
    _VismMaxOffCadence_Type()
)
vismMaxOffCadence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismMaxOffCadence.setStatus("current")


class _VismFreqNumOfCadenceMatch_Type(Integer32):
    """Custom type vismFreqNumOfCadenceMatch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_VismFreqNumOfCadenceMatch_Type.__name__ = "Integer32"
_VismFreqNumOfCadenceMatch_Object = MibTableColumn
vismFreqNumOfCadenceMatch = _VismFreqNumOfCadenceMatch_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 11),
    _VismFreqNumOfCadenceMatch_Type()
)
vismFreqNumOfCadenceMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismFreqNumOfCadenceMatch.setStatus("current")


class _VismFrequency1_Type(Integer32):
    """Custom type vismFrequency1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(280, 3800),
    )


_VismFrequency1_Type.__name__ = "Integer32"
_VismFrequency1_Object = MibTableColumn
vismFrequency1 = _VismFrequency1_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 12),
    _VismFrequency1_Type()
)
vismFrequency1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismFrequency1.setStatus("current")
if mibBuilder.loadTexts:
    vismFrequency1.setUnits("Hz")


class _VismFrequency2_Type(Integer32):
    """Custom type vismFrequency2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3800),
    )


_VismFrequency2_Type.__name__ = "Integer32"
_VismFrequency2_Object = MibTableColumn
vismFrequency2 = _VismFrequency2_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 13),
    _VismFrequency2_Type()
)
vismFrequency2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismFrequency2.setStatus("current")
if mibBuilder.loadTexts:
    vismFrequency2.setUnits("Hz")


class _VismFreqOnCadence_Type(Integer32):
    """Custom type vismFreqOnCadence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 5000),
    )


_VismFreqOnCadence_Type.__name__ = "Integer32"
_VismFreqOnCadence_Object = MibTableColumn
vismFreqOnCadence = _VismFreqOnCadence_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 14),
    _VismFreqOnCadence_Type()
)
vismFreqOnCadence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismFreqOnCadence.setStatus("current")
if mibBuilder.loadTexts:
    vismFreqOnCadence.setUnits("milliseconds")


class _VismFreqOffCadence_Type(Integer32):
    """Custom type vismFreqOffCadence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5000),
    )


_VismFreqOffCadence_Type.__name__ = "Integer32"
_VismFreqOffCadence_Object = MibTableColumn
vismFreqOffCadence = _VismFreqOffCadence_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 15),
    _VismFreqOffCadence_Type()
)
vismFreqOffCadence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismFreqOffCadence.setStatus("current")
if mibBuilder.loadTexts:
    vismFreqOffCadence.setUnits("milliseconds")
_VismSequentialToneDetectGrp_ObjectIdentity = ObjectIdentity
vismSequentialToneDetectGrp = _VismSequentialToneDetectGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4)
)


class _SeqToneNumOfFrequencies_Type(Integer32):
    """Custom type seqToneNumOfFrequencies based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SeqToneNumOfFrequencies_Type.__name__ = "Integer32"
_SeqToneNumOfFrequencies_Object = MibScalar
seqToneNumOfFrequencies = _SeqToneNumOfFrequencies_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 1),
    _SeqToneNumOfFrequencies_Type()
)
seqToneNumOfFrequencies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seqToneNumOfFrequencies.setStatus("current")


class _SeqToneEventID_Type(Integer32):
    """Custom type seqToneEventID based on Integer32"""
    defaultValue = 74

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SeqToneEventID_Type.__name__ = "Integer32"
_SeqToneEventID_Object = MibScalar
seqToneEventID = _SeqToneEventID_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 2),
    _SeqToneEventID_Type()
)
seqToneEventID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seqToneEventID.setStatus("current")


class _SeqToneDurationOfEachTone_Type(Integer32):
    """Custom type seqToneDurationOfEachTone based on Integer32"""
    defaultValue = 33

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_SeqToneDurationOfEachTone_Type.__name__ = "Integer32"
_SeqToneDurationOfEachTone_Object = MibScalar
seqToneDurationOfEachTone = _SeqToneDurationOfEachTone_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 3),
    _SeqToneDurationOfEachTone_Type()
)
seqToneDurationOfEachTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seqToneDurationOfEachTone.setStatus("current")


class _SeqToneGapBetweenEachTone_Type(Integer32):
    """Custom type seqToneGapBetweenEachTone based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_SeqToneGapBetweenEachTone_Type.__name__ = "Integer32"
_SeqToneGapBetweenEachTone_Object = MibScalar
seqToneGapBetweenEachTone = _SeqToneGapBetweenEachTone_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 4),
    _SeqToneGapBetweenEachTone_Type()
)
seqToneGapBetweenEachTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seqToneGapBetweenEachTone.setStatus("current")


class _SeqToneDurationDeviation_Type(Integer32):
    """Custom type seqToneDurationDeviation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_SeqToneDurationDeviation_Type.__name__ = "Integer32"
_SeqToneDurationDeviation_Object = MibScalar
seqToneDurationDeviation = _SeqToneDurationDeviation_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 5),
    _SeqToneDurationDeviation_Type()
)
seqToneDurationDeviation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seqToneDurationDeviation.setStatus("current")


class _SeqToneMaximumGapDuration_Type(Integer32):
    """Custom type seqToneMaximumGapDuration based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_SeqToneMaximumGapDuration_Type.__name__ = "Integer32"
_SeqToneMaximumGapDuration_Object = MibScalar
seqToneMaximumGapDuration = _SeqToneMaximumGapDuration_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 6),
    _SeqToneMaximumGapDuration_Type()
)
seqToneMaximumGapDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seqToneMaximumGapDuration.setStatus("current")


class _SeqToneGapDurationDeviation_Type(Integer32):
    """Custom type seqToneGapDurationDeviation based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_SeqToneGapDurationDeviation_Type.__name__ = "Integer32"
_SeqToneGapDurationDeviation_Object = MibScalar
seqToneGapDurationDeviation = _SeqToneGapDurationDeviation_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 7),
    _SeqToneGapDurationDeviation_Type()
)
seqToneGapDurationDeviation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seqToneGapDurationDeviation.setStatus("current")


class _SeqToneFreqDeviation_Type(Integer32):
    """Custom type seqToneFreqDeviation based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_SeqToneFreqDeviation_Type.__name__ = "Integer32"
_SeqToneFreqDeviation_Object = MibScalar
seqToneFreqDeviation = _SeqToneFreqDeviation_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 8),
    _SeqToneFreqDeviation_Type()
)
seqToneFreqDeviation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seqToneFreqDeviation.setStatus("current")


class _SeqTonePowerLevelCeiling_Type(Integer32):
    """Custom type seqTonePowerLevelCeiling based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_SeqTonePowerLevelCeiling_Type.__name__ = "Integer32"
_SeqTonePowerLevelCeiling_Object = MibScalar
seqTonePowerLevelCeiling = _SeqTonePowerLevelCeiling_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 9),
    _SeqTonePowerLevelCeiling_Type()
)
seqTonePowerLevelCeiling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seqTonePowerLevelCeiling.setStatus("current")


class _SeqTonePowerLevelFloor_Type(Integer32):
    """Custom type seqTonePowerLevelFloor based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_SeqTonePowerLevelFloor_Type.__name__ = "Integer32"
_SeqTonePowerLevelFloor_Object = MibScalar
seqTonePowerLevelFloor = _SeqTonePowerLevelFloor_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 10),
    _SeqTonePowerLevelFloor_Type()
)
seqTonePowerLevelFloor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seqTonePowerLevelFloor.setStatus("current")


class _SeqToneFrequency1_Type(Integer32):
    """Custom type seqToneFrequency1 based on Integer32"""
    defaultValue = 950

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(280, 3800),
    )


_SeqToneFrequency1_Type.__name__ = "Integer32"
_SeqToneFrequency1_Object = MibScalar
seqToneFrequency1 = _SeqToneFrequency1_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 11),
    _SeqToneFrequency1_Type()
)
seqToneFrequency1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seqToneFrequency1.setStatus("current")


class _SeqToneFrequency2_Type(Integer32):
    """Custom type seqToneFrequency2 based on Integer32"""
    defaultValue = 1400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(280, 3800),
    )


_SeqToneFrequency2_Type.__name__ = "Integer32"
_SeqToneFrequency2_Object = MibScalar
seqToneFrequency2 = _SeqToneFrequency2_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 12),
    _SeqToneFrequency2_Type()
)
seqToneFrequency2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seqToneFrequency2.setStatus("current")


class _SeqToneFrequency3_Type(Integer32):
    """Custom type seqToneFrequency3 based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(280, 3800),
    )


_SeqToneFrequency3_Type.__name__ = "Integer32"
_SeqToneFrequency3_Object = MibScalar
seqToneFrequency3 = _SeqToneFrequency3_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 13),
    _SeqToneFrequency3_Type()
)
seqToneFrequency3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seqToneFrequency3.setStatus("current")


class _SeqToneFrequency4_Type(Integer32):
    """Custom type seqToneFrequency4 based on Integer32"""
    defaultValue = 280

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(280, 3800),
    )


_SeqToneFrequency4_Type.__name__ = "Integer32"
_SeqToneFrequency4_Object = MibScalar
seqToneFrequency4 = _SeqToneFrequency4_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 14),
    _SeqToneFrequency4_Type()
)
seqToneFrequency4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seqToneFrequency4.setStatus("current")


class _SeqToneFrequency5_Type(Integer32):
    """Custom type seqToneFrequency5 based on Integer32"""
    defaultValue = 280

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(280, 3800),
    )


_SeqToneFrequency5_Type.__name__ = "Integer32"
_SeqToneFrequency5_Object = MibScalar
seqToneFrequency5 = _SeqToneFrequency5_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 15),
    _SeqToneFrequency5_Type()
)
seqToneFrequency5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seqToneFrequency5.setStatus("current")


class _SeqToneFrequency6_Type(Integer32):
    """Custom type seqToneFrequency6 based on Integer32"""
    defaultValue = 280

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(280, 3800),
    )


_SeqToneFrequency6_Type.__name__ = "Integer32"
_SeqToneFrequency6_Object = MibScalar
seqToneFrequency6 = _SeqToneFrequency6_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 16),
    _SeqToneFrequency6_Type()
)
seqToneFrequency6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seqToneFrequency6.setStatus("current")


class _SeqToneFrequency7_Type(Integer32):
    """Custom type seqToneFrequency7 based on Integer32"""
    defaultValue = 280

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(280, 3800),
    )


_SeqToneFrequency7_Type.__name__ = "Integer32"
_SeqToneFrequency7_Object = MibScalar
seqToneFrequency7 = _SeqToneFrequency7_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 17),
    _SeqToneFrequency7_Type()
)
seqToneFrequency7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seqToneFrequency7.setStatus("current")


class _SeqToneFrequency8_Type(Integer32):
    """Custom type seqToneFrequency8 based on Integer32"""
    defaultValue = 280

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(280, 3800),
    )


_SeqToneFrequency8_Type.__name__ = "Integer32"
_SeqToneFrequency8_Object = MibScalar
seqToneFrequency8 = _SeqToneFrequency8_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 18),
    _SeqToneFrequency8_Type()
)
seqToneFrequency8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seqToneFrequency8.setStatus("current")


class _SeqToneFrequency9_Type(Integer32):
    """Custom type seqToneFrequency9 based on Integer32"""
    defaultValue = 280

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(280, 3800),
    )


_SeqToneFrequency9_Type.__name__ = "Integer32"
_SeqToneFrequency9_Object = MibScalar
seqToneFrequency9 = _SeqToneFrequency9_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 19),
    _SeqToneFrequency9_Type()
)
seqToneFrequency9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seqToneFrequency9.setStatus("current")


class _SeqToneFrequency10_Type(Integer32):
    """Custom type seqToneFrequency10 based on Integer32"""
    defaultValue = 280

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(280, 3800),
    )


_SeqToneFrequency10_Type.__name__ = "Integer32"
_SeqToneFrequency10_Object = MibScalar
seqToneFrequency10 = _SeqToneFrequency10_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 20),
    _SeqToneFrequency10_Type()
)
seqToneFrequency10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seqToneFrequency10.setStatus("current")
_VismToneNotificationPrefix_ObjectIdentity = ObjectIdentity
vismToneNotificationPrefix = _VismToneNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 2)
)
_VismToneNotifications_ObjectIdentity = ObjectIdentity
vismToneNotifications = _VismToneNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 2, 0)
)
_VismTonePlanMIBConformance_ObjectIdentity = ObjectIdentity
vismTonePlanMIBConformance = _VismTonePlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 3)
)
_VismTonePlanMIBCompliances_ObjectIdentity = ObjectIdentity
vismTonePlanMIBCompliances = _VismTonePlanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 3, 1)
)
_VismTonePlanMIBGroups_ObjectIdentity = ObjectIdentity
vismTonePlanMIBGroups = _VismTonePlanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 3, 2)
)

# Managed Objects groups

vismTonePlanControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 3, 2, 1)
)
vismTonePlanControlGroup.setObjects(
    ("CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanCurrentSize")
)
if mibBuilder.loadTexts:
    vismTonePlanControlGroup.setStatus("current")

vismTonePlanTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 3, 2, 2)
)
vismTonePlanTableGroup.setObjects(
      *(("CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanEntryStatus"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanProvisionFlag"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanRegionName"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanVersionNumber"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanFileName"))
)
if mibBuilder.loadTexts:
    vismTonePlanTableGroup.setStatus("current")

vismConfigToneDetectTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 3, 2, 3)
)
vismConfigToneDetectTableGroup.setObjects(
      *(("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismConfigToneDetectNum"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismEventCode"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismConfigToneDetectRowStatus"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFreqMaxDeviation"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFreqMaxPower"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFreqMinPower"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFreqPowerTwist"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFreqMaxDelay"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismMinOnCadence"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismMaxOffCadence"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFreqNumOfCadenceMatch"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFrequency1"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFrequency2"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFreqOnCadence"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFreqOffCadence"))
)
if mibBuilder.loadTexts:
    vismConfigToneDetectTableGroup.setStatus("current")

vismSequentialToneDetectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 3, 2, 4)
)
vismSequentialToneDetectGroup.setObjects(
      *(("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneNumOfFrequencies"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneEventID"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneDurationOfEachTone"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneGapBetweenEachTone"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneDurationDeviation"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneMaximumGapDuration"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneGapDurationDeviation"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFreqDeviation"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqTonePowerLevelCeiling"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqTonePowerLevelFloor"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency1"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency2"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency3"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency4"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency5"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency6"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency7"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency8"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency9"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency10"))
)
if mibBuilder.loadTexts:
    vismSequentialToneDetectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

vismTonePlanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 24, 3, 1, 1)
)
if mibBuilder.loadTexts:
    vismTonePlanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-VISM-TONE-PLAN-MIB",
    **{"vismTonePlanGrpMIB": vismTonePlanGrpMIB,
       "vismTonePlanGrpMIBObjects": vismTonePlanGrpMIBObjects,
       "vismTonePlan": vismTonePlan,
       "vismTonePlanControlGrp": vismTonePlanControlGrp,
       "tonePlanCurrentSize": tonePlanCurrentSize,
       "vismTonePlanTableGrp": vismTonePlanTableGrp,
       "vismTonePlanTable": vismTonePlanTable,
       "vismTonePlanEntry": vismTonePlanEntry,
       "tonePlanIndex": tonePlanIndex,
       "tonePlanEntryStatus": tonePlanEntryStatus,
       "tonePlanProvisionFlag": tonePlanProvisionFlag,
       "tonePlanRegionName": tonePlanRegionName,
       "tonePlanVersionNumber": tonePlanVersionNumber,
       "tonePlanFileName": tonePlanFileName,
       "vismConfigToneDetectGrp": vismConfigToneDetectGrp,
       "vismConfigToneDetectTable": vismConfigToneDetectTable,
       "vismConfigToneDetectEntry": vismConfigToneDetectEntry,
       "vismConfigToneDetectNum": vismConfigToneDetectNum,
       "vismEventCode": vismEventCode,
       "vismConfigToneDetectRowStatus": vismConfigToneDetectRowStatus,
       "vismFreqMaxDeviation": vismFreqMaxDeviation,
       "vismFreqMaxPower": vismFreqMaxPower,
       "vismFreqMinPower": vismFreqMinPower,
       "vismFreqPowerTwist": vismFreqPowerTwist,
       "vismFreqMaxDelay": vismFreqMaxDelay,
       "vismMinOnCadence": vismMinOnCadence,
       "vismMaxOffCadence": vismMaxOffCadence,
       "vismFreqNumOfCadenceMatch": vismFreqNumOfCadenceMatch,
       "vismFrequency1": vismFrequency1,
       "vismFrequency2": vismFrequency2,
       "vismFreqOnCadence": vismFreqOnCadence,
       "vismFreqOffCadence": vismFreqOffCadence,
       "vismSequentialToneDetectGrp": vismSequentialToneDetectGrp,
       "seqToneNumOfFrequencies": seqToneNumOfFrequencies,
       "seqToneEventID": seqToneEventID,
       "seqToneDurationOfEachTone": seqToneDurationOfEachTone,
       "seqToneGapBetweenEachTone": seqToneGapBetweenEachTone,
       "seqToneDurationDeviation": seqToneDurationDeviation,
       "seqToneMaximumGapDuration": seqToneMaximumGapDuration,
       "seqToneGapDurationDeviation": seqToneGapDurationDeviation,
       "seqToneFreqDeviation": seqToneFreqDeviation,
       "seqTonePowerLevelCeiling": seqTonePowerLevelCeiling,
       "seqTonePowerLevelFloor": seqTonePowerLevelFloor,
       "seqToneFrequency1": seqToneFrequency1,
       "seqToneFrequency2": seqToneFrequency2,
       "seqToneFrequency3": seqToneFrequency3,
       "seqToneFrequency4": seqToneFrequency4,
       "seqToneFrequency5": seqToneFrequency5,
       "seqToneFrequency6": seqToneFrequency6,
       "seqToneFrequency7": seqToneFrequency7,
       "seqToneFrequency8": seqToneFrequency8,
       "seqToneFrequency9": seqToneFrequency9,
       "seqToneFrequency10": seqToneFrequency10,
       "vismToneNotificationPrefix": vismToneNotificationPrefix,
       "vismToneNotifications": vismToneNotifications,
       "vismTonePlanMIBConformance": vismTonePlanMIBConformance,
       "vismTonePlanMIBCompliances": vismTonePlanMIBCompliances,
       "vismTonePlanMIBCompliance": vismTonePlanMIBCompliance,
       "vismTonePlanMIBGroups": vismTonePlanMIBGroups,
       "vismTonePlanControlGroup": vismTonePlanControlGroup,
       "vismTonePlanTableGroup": vismTonePlanTableGroup,
       "vismConfigToneDetectTableGroup": vismConfigToneDetectTableGroup,
       "vismSequentialToneDetectGroup": vismSequentialToneDetectGroup}
)
