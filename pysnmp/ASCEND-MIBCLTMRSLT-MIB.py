# SNMP MIB module (ASCEND-MIBCLTMRSLT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBCLTMRSLT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:22 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibcltmRslt_ObjectIdentity = ObjectIdentity
mibcltmRslt = _MibcltmRslt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 68)
)
_MibcltmRsltTable_Object = MibTable
mibcltmRsltTable = _MibcltmRsltTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1)
)
if mibBuilder.loadTexts:
    mibcltmRsltTable.setStatus("mandatory")
_MibcltmRsltEntry_Object = MibTableRow
mibcltmRsltEntry = _MibcltmRsltEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1)
)
mibcltmRsltEntry.setIndexNames(
    (0, "ASCEND-MIBCLTMRSLT-MIB", "cltmRslt-Index-o"),
)
if mibBuilder.loadTexts:
    mibcltmRsltEntry.setStatus("mandatory")
_CltmRslt_Index_o_Type = Integer32
_CltmRslt_Index_o_Object = MibScalar
cltmRslt_Index_o = _CltmRslt_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 1),
    _CltmRslt_Index_o_Type()
)
cltmRslt_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_Index_o.setStatus("mandatory")


class _CltmRslt_CltmSlot_Type(Integer32):
    """Custom type cltmRslt_CltmSlot based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("anySlot", 1),
          ("slot1", 2),
          ("slot10", 11),
          ("slot11", 12),
          ("slot12", 13),
          ("slot13", 14),
          ("slot14", 15),
          ("slot15", 16),
          ("slot16", 17),
          ("slot2", 3),
          ("slot3", 4),
          ("slot4", 5),
          ("slot5", 6),
          ("slot6", 7),
          ("slot7", 8))
    )


_CltmRslt_CltmSlot_Type.__name__ = "Integer32"
_CltmRslt_CltmSlot_Object = MibScalar
cltmRslt_CltmSlot = _CltmRslt_CltmSlot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 2),
    _CltmRslt_CltmSlot_Type()
)
cltmRslt_CltmSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_CltmSlot.setStatus("mandatory")
_CltmRslt_TestResultTimeStamp_Type = Integer32
_CltmRslt_TestResultTimeStamp_Object = MibScalar
cltmRslt_TestResultTimeStamp = _CltmRslt_TestResultTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 3),
    _CltmRslt_TestResultTimeStamp_Type()
)
cltmRslt_TestResultTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_TestResultTimeStamp.setStatus("mandatory")
_CltmRslt_TestResultSequence_Type = Integer32
_CltmRslt_TestResultSequence_Object = MibScalar
cltmRslt_TestResultSequence = _CltmRslt_TestResultSequence_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 4),
    _CltmRslt_TestResultSequence_Type()
)
cltmRslt_TestResultSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_TestResultSequence.setStatus("mandatory")


class _CltmRslt_TestResultStatus_Type(Integer32):
    """Custom type cltmRslt_TestResultStatus based on Integer32"""
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
        *(("notReady", 1),
          ("notValid", 2),
          ("overRange", 3),
          ("valid", 4))
    )


_CltmRslt_TestResultStatus_Type.__name__ = "Integer32"
_CltmRslt_TestResultStatus_Object = MibScalar
cltmRslt_TestResultStatus = _CltmRslt_TestResultStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 5),
    _CltmRslt_TestResultStatus_Type()
)
cltmRslt_TestResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_TestResultStatus.setStatus("mandatory")
_CltmRslt_DmmResult_Type = Integer32
_CltmRslt_DmmResult_Object = MibScalar
cltmRslt_DmmResult = _CltmRslt_DmmResult_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 6),
    _CltmRslt_DmmResult_Type()
)
cltmRslt_DmmResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_DmmResult.setStatus("mandatory")
_CltmRslt_LoopResistance_Type = Integer32
_CltmRslt_LoopResistance_Object = MibScalar
cltmRslt_LoopResistance = _CltmRslt_LoopResistance_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 7),
    _CltmRslt_LoopResistance_Type()
)
cltmRslt_LoopResistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_LoopResistance.setStatus("mandatory")
_CltmRslt_LoopResistanceLength1_Type = Integer32
_CltmRslt_LoopResistanceLength1_Object = MibScalar
cltmRslt_LoopResistanceLength1 = _CltmRslt_LoopResistanceLength1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 8),
    _CltmRslt_LoopResistanceLength1_Type()
)
cltmRslt_LoopResistanceLength1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_LoopResistanceLength1.setStatus("mandatory")
_CltmRslt_LoopResistanceLength2_Type = Integer32
_CltmRslt_LoopResistanceLength2_Object = MibScalar
cltmRslt_LoopResistanceLength2 = _CltmRslt_LoopResistanceLength2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 9),
    _CltmRslt_LoopResistanceLength2_Type()
)
cltmRslt_LoopResistanceLength2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_LoopResistanceLength2.setStatus("mandatory")
_CltmRslt_LoopResistanceLength3_Type = Integer32
_CltmRslt_LoopResistanceLength3_Object = MibScalar
cltmRslt_LoopResistanceLength3 = _CltmRslt_LoopResistanceLength3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 10),
    _CltmRslt_LoopResistanceLength3_Type()
)
cltmRslt_LoopResistanceLength3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_LoopResistanceLength3.setStatus("mandatory")
_CltmRslt_CoilDetectionCoilCount_Type = Integer32
_CltmRslt_CoilDetectionCoilCount_Object = MibScalar
cltmRslt_CoilDetectionCoilCount = _CltmRslt_CoilDetectionCoilCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 11),
    _CltmRslt_CoilDetectionCoilCount_Type()
)
cltmRslt_CoilDetectionCoilCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_CoilDetectionCoilCount.setStatus("mandatory")
_CltmRslt_ImpulseNoiseReadLowThreshold_Type = Integer32
_CltmRslt_ImpulseNoiseReadLowThreshold_Object = MibScalar
cltmRslt_ImpulseNoiseReadLowThreshold = _CltmRslt_ImpulseNoiseReadLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 12),
    _CltmRslt_ImpulseNoiseReadLowThreshold_Type()
)
cltmRslt_ImpulseNoiseReadLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_ImpulseNoiseReadLowThreshold.setStatus("mandatory")
_CltmRslt_ImpulseNoiseReadMidThreshold_Type = Integer32
_CltmRslt_ImpulseNoiseReadMidThreshold_Object = MibScalar
cltmRslt_ImpulseNoiseReadMidThreshold = _CltmRslt_ImpulseNoiseReadMidThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 13),
    _CltmRslt_ImpulseNoiseReadMidThreshold_Type()
)
cltmRslt_ImpulseNoiseReadMidThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_ImpulseNoiseReadMidThreshold.setStatus("mandatory")
_CltmRslt_ImpulseNoiseReadHighThreshold_Type = Integer32
_CltmRslt_ImpulseNoiseReadHighThreshold_Object = MibScalar
cltmRslt_ImpulseNoiseReadHighThreshold = _CltmRslt_ImpulseNoiseReadHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 14),
    _CltmRslt_ImpulseNoiseReadHighThreshold_Type()
)
cltmRslt_ImpulseNoiseReadHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_ImpulseNoiseReadHighThreshold.setStatus("mandatory")
_CltmRslt_RcvToneFrequency_Type = Integer32
_CltmRslt_RcvToneFrequency_Object = MibScalar
cltmRslt_RcvToneFrequency = _CltmRslt_RcvToneFrequency_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 15),
    _CltmRslt_RcvToneFrequency_Type()
)
cltmRslt_RcvToneFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_RcvToneFrequency.setStatus("mandatory")
_CltmRslt_RcvToneLevel_Type = Integer32
_CltmRslt_RcvToneLevel_Object = MibScalar
cltmRslt_RcvToneLevel = _CltmRslt_RcvToneLevel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 16),
    _CltmRslt_RcvToneLevel_Type()
)
cltmRslt_RcvToneLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_RcvToneLevel.setStatus("mandatory")
_CltmRslt_TdrManualSampleCount_Type = Integer32
_CltmRslt_TdrManualSampleCount_Object = MibScalar
cltmRslt_TdrManualSampleCount = _CltmRslt_TdrManualSampleCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 17),
    _CltmRslt_TdrManualSampleCount_Type()
)
cltmRslt_TdrManualSampleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_TdrManualSampleCount.setStatus("mandatory")
_CltmRslt_TdrAutomaticFaultDistance_Type = Integer32
_CltmRslt_TdrAutomaticFaultDistance_Object = MibScalar
cltmRslt_TdrAutomaticFaultDistance = _CltmRslt_TdrAutomaticFaultDistance_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 18),
    _CltmRslt_TdrAutomaticFaultDistance_Type()
)
cltmRslt_TdrAutomaticFaultDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_TdrAutomaticFaultDistance.setStatus("mandatory")
_CltmRslt_HardwareRevision_Type = Integer32
_CltmRslt_HardwareRevision_Object = MibScalar
cltmRslt_HardwareRevision = _CltmRslt_HardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 19),
    _CltmRslt_HardwareRevision_Type()
)
cltmRslt_HardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_HardwareRevision.setStatus("mandatory")
_CltmRslt_SofwareRevision_Type = Integer32
_CltmRslt_SofwareRevision_Object = MibScalar
cltmRslt_SofwareRevision = _CltmRslt_SofwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 20),
    _CltmRslt_SofwareRevision_Type()
)
cltmRslt_SofwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_SofwareRevision.setStatus("mandatory")
_CltmRslt_DcDeltaResistanceTR_Type = Integer32
_CltmRslt_DcDeltaResistanceTR_Object = MibScalar
cltmRslt_DcDeltaResistanceTR = _CltmRslt_DcDeltaResistanceTR_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 21),
    _CltmRslt_DcDeltaResistanceTR_Type()
)
cltmRslt_DcDeltaResistanceTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_DcDeltaResistanceTR.setStatus("mandatory")
_CltmRslt_DcDeltaResistanceTS_Type = Integer32
_CltmRslt_DcDeltaResistanceTS_Object = MibScalar
cltmRslt_DcDeltaResistanceTS = _CltmRslt_DcDeltaResistanceTS_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 22),
    _CltmRslt_DcDeltaResistanceTS_Type()
)
cltmRslt_DcDeltaResistanceTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_DcDeltaResistanceTS.setStatus("mandatory")
_CltmRslt_DcDeltaResistanceRS_Type = Integer32
_CltmRslt_DcDeltaResistanceRS_Object = MibScalar
cltmRslt_DcDeltaResistanceRS = _CltmRslt_DcDeltaResistanceRS_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 23),
    _CltmRslt_DcDeltaResistanceRS_Type()
)
cltmRslt_DcDeltaResistanceRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_DcDeltaResistanceRS.setStatus("mandatory")
_CltmRslt_DcDeltaVoltageTS_Type = Integer32
_CltmRslt_DcDeltaVoltageTS_Object = MibScalar
cltmRslt_DcDeltaVoltageTS = _CltmRslt_DcDeltaVoltageTS_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 24),
    _CltmRslt_DcDeltaVoltageTS_Type()
)
cltmRslt_DcDeltaVoltageTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_DcDeltaVoltageTS.setStatus("mandatory")
_CltmRslt_DcDeltaVoltageRS_Type = Integer32
_CltmRslt_DcDeltaVoltageRS_Object = MibScalar
cltmRslt_DcDeltaVoltageRS = _CltmRslt_DcDeltaVoltageRS_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 25),
    _CltmRslt_DcDeltaVoltageRS_Type()
)
cltmRslt_DcDeltaVoltageRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_DcDeltaVoltageRS.setStatus("mandatory")
_CltmRslt_CapEquivalentTR_Type = Integer32
_CltmRslt_CapEquivalentTR_Object = MibScalar
cltmRslt_CapEquivalentTR = _CltmRslt_CapEquivalentTR_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 26),
    _CltmRslt_CapEquivalentTR_Type()
)
cltmRslt_CapEquivalentTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_CapEquivalentTR.setStatus("mandatory")
_CltmRslt_CapEquivalentTS_Type = Integer32
_CltmRslt_CapEquivalentTS_Object = MibScalar
cltmRslt_CapEquivalentTS = _CltmRslt_CapEquivalentTS_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 27),
    _CltmRslt_CapEquivalentTS_Type()
)
cltmRslt_CapEquivalentTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_CapEquivalentTS.setStatus("mandatory")
_CltmRslt_CapEquivalentRS_Type = Integer32
_CltmRslt_CapEquivalentRS_Object = MibScalar
cltmRslt_CapEquivalentRS = _CltmRslt_CapEquivalentRS_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 28),
    _CltmRslt_CapEquivalentRS_Type()
)
cltmRslt_CapEquivalentRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_CapEquivalentRS.setStatus("mandatory")
_CltmRslt_DmmAllTR_Type = Integer32
_CltmRslt_DmmAllTR_Object = MibScalar
cltmRslt_DmmAllTR = _CltmRslt_DmmAllTR_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 29),
    _CltmRslt_DmmAllTR_Type()
)
cltmRslt_DmmAllTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_DmmAllTR.setStatus("mandatory")
_CltmRslt_DmmAllTS_Type = Integer32
_CltmRslt_DmmAllTS_Object = MibScalar
cltmRslt_DmmAllTS = _CltmRslt_DmmAllTS_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 30),
    _CltmRslt_DmmAllTS_Type()
)
cltmRslt_DmmAllTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_DmmAllTS.setStatus("mandatory")
_CltmRslt_DmmAllRS_Type = Integer32
_CltmRslt_DmmAllRS_Object = MibScalar
cltmRslt_DmmAllRS = _CltmRslt_DmmAllRS_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 31),
    _CltmRslt_DmmAllRS_Type()
)
cltmRslt_DmmAllRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_DmmAllRS.setStatus("mandatory")
_CltmRslt_Ringer_Type = Integer32
_CltmRslt_Ringer_Object = MibScalar
cltmRslt_Ringer = _CltmRslt_Ringer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 32),
    _CltmRslt_Ringer_Type()
)
cltmRslt_Ringer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_Ringer.setStatus("mandatory")
_CltmRslt_AtuR_Type = Integer32
_CltmRslt_AtuR_Object = MibScalar
cltmRslt_AtuR = _CltmRslt_AtuR_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 33),
    _CltmRslt_AtuR_Type()
)
cltmRslt_AtuR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_AtuR.setStatus("mandatory")
_CltmRslt_BridgeTapNumber_Type = Integer32
_CltmRslt_BridgeTapNumber_Object = MibScalar
cltmRslt_BridgeTapNumber = _CltmRslt_BridgeTapNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 34),
    _CltmRslt_BridgeTapNumber_Type()
)
cltmRslt_BridgeTapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_BridgeTapNumber.setStatus("mandatory")
_CltmRslt_BridgeTapLength_Type = Integer32
_CltmRslt_BridgeTapLength_Object = MibScalar
cltmRslt_BridgeTapLength = _CltmRslt_BridgeTapLength_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 35),
    _CltmRslt_BridgeTapLength_Type()
)
cltmRslt_BridgeTapLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_BridgeTapLength.setStatus("mandatory")


class _CltmRslt_Action_o_Type(Integer32):
    """Custom type cltmRslt_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_CltmRslt_Action_o_Type.__name__ = "Integer32"
_CltmRslt_Action_o_Object = MibScalar
cltmRslt_Action_o = _CltmRslt_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 36),
    _CltmRslt_Action_o_Type()
)
cltmRslt_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmRslt_Action_o.setStatus("mandatory")
_CltmRslt_VoiceDetection_Type = Integer32
_CltmRslt_VoiceDetection_Object = MibScalar
cltmRslt_VoiceDetection = _CltmRslt_VoiceDetection_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 37),
    _CltmRslt_VoiceDetection_Type()
)
cltmRslt_VoiceDetection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_VoiceDetection.setStatus("mandatory")
_CltmRslt_FirstCoilLocation_Type = Integer32
_CltmRslt_FirstCoilLocation_Object = MibScalar
cltmRslt_FirstCoilLocation = _CltmRslt_FirstCoilLocation_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 38),
    _CltmRslt_FirstCoilLocation_Type()
)
cltmRslt_FirstCoilLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_FirstCoilLocation.setStatus("mandatory")
_CltmRslt_ShortLocation_Type = Integer32
_CltmRslt_ShortLocation_Object = MibScalar
cltmRslt_ShortLocation = _CltmRslt_ShortLocation_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 1, 1, 39),
    _CltmRslt_ShortLocation_Type()
)
cltmRslt_ShortLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_ShortLocation.setStatus("mandatory")
_MibcltmRslt_BridgeTapTableTable_Object = MibTable
mibcltmRslt_BridgeTapTableTable = _MibcltmRslt_BridgeTapTableTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 2)
)
if mibBuilder.loadTexts:
    mibcltmRslt_BridgeTapTableTable.setStatus("mandatory")
_MibcltmRslt_BridgeTapTableEntry_Object = MibTableRow
mibcltmRslt_BridgeTapTableEntry = _MibcltmRslt_BridgeTapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 2, 1)
)
mibcltmRslt_BridgeTapTableEntry.setIndexNames(
    (0, "ASCEND-MIBCLTMRSLT-MIB", "cltmRslt-BridgeTapTable-Index-o"),
    (0, "ASCEND-MIBCLTMRSLT-MIB", "cltmRslt-BridgeTapTable-Index1-o"),
)
if mibBuilder.loadTexts:
    mibcltmRslt_BridgeTapTableEntry.setStatus("mandatory")
_CltmRslt_BridgeTapTable_Index_o_Type = Integer32
_CltmRslt_BridgeTapTable_Index_o_Object = MibScalar
cltmRslt_BridgeTapTable_Index_o = _CltmRslt_BridgeTapTable_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 2, 1, 1),
    _CltmRslt_BridgeTapTable_Index_o_Type()
)
cltmRslt_BridgeTapTable_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_BridgeTapTable_Index_o.setStatus("mandatory")
_CltmRslt_BridgeTapTable_Index1_o_Type = Integer32
_CltmRslt_BridgeTapTable_Index1_o_Object = MibScalar
cltmRslt_BridgeTapTable_Index1_o = _CltmRslt_BridgeTapTable_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 2, 1, 2),
    _CltmRslt_BridgeTapTable_Index1_o_Type()
)
cltmRslt_BridgeTapTable_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_BridgeTapTable_Index1_o.setStatus("mandatory")
_CltmRslt_BridgeTapTable_Distance_Type = Integer32
_CltmRslt_BridgeTapTable_Distance_Object = MibScalar
cltmRslt_BridgeTapTable_Distance = _CltmRslt_BridgeTapTable_Distance_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 2, 1, 3),
    _CltmRslt_BridgeTapTable_Distance_Type()
)
cltmRslt_BridgeTapTable_Distance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_BridgeTapTable_Distance.setStatus("mandatory")
_CltmRslt_BridgeTapTable_Length_Type = Integer32
_CltmRslt_BridgeTapTable_Length_Object = MibScalar
cltmRslt_BridgeTapTable_Length = _CltmRslt_BridgeTapTable_Length_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 2, 1, 4),
    _CltmRslt_BridgeTapTable_Length_Type()
)
cltmRslt_BridgeTapTable_Length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_BridgeTapTable_Length.setStatus("mandatory")
_CltmRslt_BridgeTapTable_Confidence_Type = Integer32
_CltmRslt_BridgeTapTable_Confidence_Object = MibScalar
cltmRslt_BridgeTapTable_Confidence = _CltmRslt_BridgeTapTable_Confidence_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 2, 1, 5),
    _CltmRslt_BridgeTapTable_Confidence_Type()
)
cltmRslt_BridgeTapTable_Confidence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_BridgeTapTable_Confidence.setStatus("mandatory")
_MibcltmRslt_TdrDistanceLevelTable_Object = MibTable
mibcltmRslt_TdrDistanceLevelTable = _MibcltmRslt_TdrDistanceLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 3)
)
if mibBuilder.loadTexts:
    mibcltmRslt_TdrDistanceLevelTable.setStatus("mandatory")
_MibcltmRslt_TdrDistanceLevelEntry_Object = MibTableRow
mibcltmRslt_TdrDistanceLevelEntry = _MibcltmRslt_TdrDistanceLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 3, 1)
)
mibcltmRslt_TdrDistanceLevelEntry.setIndexNames(
    (0, "ASCEND-MIBCLTMRSLT-MIB", "cltmRslt-TdrDistanceLevel-Index-o"),
    (0, "ASCEND-MIBCLTMRSLT-MIB", "cltmRslt-TdrDistanceLevel-Index1-o"),
)
if mibBuilder.loadTexts:
    mibcltmRslt_TdrDistanceLevelEntry.setStatus("mandatory")
_CltmRslt_TdrDistanceLevel_Index_o_Type = Integer32
_CltmRslt_TdrDistanceLevel_Index_o_Object = MibScalar
cltmRslt_TdrDistanceLevel_Index_o = _CltmRslt_TdrDistanceLevel_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 3, 1, 1),
    _CltmRslt_TdrDistanceLevel_Index_o_Type()
)
cltmRslt_TdrDistanceLevel_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_TdrDistanceLevel_Index_o.setStatus("mandatory")
_CltmRslt_TdrDistanceLevel_Index1_o_Type = Integer32
_CltmRslt_TdrDistanceLevel_Index1_o_Object = MibScalar
cltmRslt_TdrDistanceLevel_Index1_o = _CltmRslt_TdrDistanceLevel_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 3, 1, 2),
    _CltmRslt_TdrDistanceLevel_Index1_o_Type()
)
cltmRslt_TdrDistanceLevel_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_TdrDistanceLevel_Index1_o.setStatus("mandatory")
_CltmRslt_TdrDistanceLevel_Distance_Type = Integer32
_CltmRslt_TdrDistanceLevel_Distance_Object = MibScalar
cltmRslt_TdrDistanceLevel_Distance = _CltmRslt_TdrDistanceLevel_Distance_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 3, 1, 3),
    _CltmRslt_TdrDistanceLevel_Distance_Type()
)
cltmRslt_TdrDistanceLevel_Distance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_TdrDistanceLevel_Distance.setStatus("mandatory")
_CltmRslt_TdrDistanceLevel_Level_Type = Integer32
_CltmRslt_TdrDistanceLevel_Level_Object = MibScalar
cltmRslt_TdrDistanceLevel_Level = _CltmRslt_TdrDistanceLevel_Level_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 3, 1, 4),
    _CltmRslt_TdrDistanceLevel_Level_Type()
)
cltmRslt_TdrDistanceLevel_Level.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_TdrDistanceLevel_Level.setStatus("mandatory")
_MibcltmRslt_PsdFrequencyLevelTable_Object = MibTable
mibcltmRslt_PsdFrequencyLevelTable = _MibcltmRslt_PsdFrequencyLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 4)
)
if mibBuilder.loadTexts:
    mibcltmRslt_PsdFrequencyLevelTable.setStatus("mandatory")
_MibcltmRslt_PsdFrequencyLevelEntry_Object = MibTableRow
mibcltmRslt_PsdFrequencyLevelEntry = _MibcltmRslt_PsdFrequencyLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 4, 1)
)
mibcltmRslt_PsdFrequencyLevelEntry.setIndexNames(
    (0, "ASCEND-MIBCLTMRSLT-MIB", "cltmRslt-PsdFrequencyLevel-Index-o"),
    (0, "ASCEND-MIBCLTMRSLT-MIB", "cltmRslt-PsdFrequencyLevel-Index1-o"),
)
if mibBuilder.loadTexts:
    mibcltmRslt_PsdFrequencyLevelEntry.setStatus("mandatory")
_CltmRslt_PsdFrequencyLevel_Index_o_Type = Integer32
_CltmRslt_PsdFrequencyLevel_Index_o_Object = MibScalar
cltmRslt_PsdFrequencyLevel_Index_o = _CltmRslt_PsdFrequencyLevel_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 4, 1, 1),
    _CltmRslt_PsdFrequencyLevel_Index_o_Type()
)
cltmRslt_PsdFrequencyLevel_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_PsdFrequencyLevel_Index_o.setStatus("mandatory")
_CltmRslt_PsdFrequencyLevel_Index1_o_Type = Integer32
_CltmRslt_PsdFrequencyLevel_Index1_o_Object = MibScalar
cltmRslt_PsdFrequencyLevel_Index1_o = _CltmRslt_PsdFrequencyLevel_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 4, 1, 2),
    _CltmRslt_PsdFrequencyLevel_Index1_o_Type()
)
cltmRslt_PsdFrequencyLevel_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_PsdFrequencyLevel_Index1_o.setStatus("mandatory")
_CltmRslt_PsdFrequencyLevel_Frequency_Type = Integer32
_CltmRslt_PsdFrequencyLevel_Frequency_Object = MibScalar
cltmRslt_PsdFrequencyLevel_Frequency = _CltmRslt_PsdFrequencyLevel_Frequency_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 4, 1, 3),
    _CltmRslt_PsdFrequencyLevel_Frequency_Type()
)
cltmRslt_PsdFrequencyLevel_Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_PsdFrequencyLevel_Frequency.setStatus("mandatory")
_CltmRslt_PsdFrequencyLevel_Level_Type = Integer32
_CltmRslt_PsdFrequencyLevel_Level_Object = MibScalar
cltmRslt_PsdFrequencyLevel_Level = _CltmRslt_PsdFrequencyLevel_Level_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 68, 4, 1, 4),
    _CltmRslt_PsdFrequencyLevel_Level_Type()
)
cltmRslt_PsdFrequencyLevel_Level.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmRslt_PsdFrequencyLevel_Level.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBCLTMRSLT-MIB",
    **{"DisplayString": DisplayString,
       "mibcltmRslt": mibcltmRslt,
       "mibcltmRsltTable": mibcltmRsltTable,
       "mibcltmRsltEntry": mibcltmRsltEntry,
       "cltmRslt-Index-o": cltmRslt_Index_o,
       "cltmRslt-CltmSlot": cltmRslt_CltmSlot,
       "cltmRslt-TestResultTimeStamp": cltmRslt_TestResultTimeStamp,
       "cltmRslt-TestResultSequence": cltmRslt_TestResultSequence,
       "cltmRslt-TestResultStatus": cltmRslt_TestResultStatus,
       "cltmRslt-DmmResult": cltmRslt_DmmResult,
       "cltmRslt-LoopResistance": cltmRslt_LoopResistance,
       "cltmRslt-LoopResistanceLength1": cltmRslt_LoopResistanceLength1,
       "cltmRslt-LoopResistanceLength2": cltmRslt_LoopResistanceLength2,
       "cltmRslt-LoopResistanceLength3": cltmRslt_LoopResistanceLength3,
       "cltmRslt-CoilDetectionCoilCount": cltmRslt_CoilDetectionCoilCount,
       "cltmRslt-ImpulseNoiseReadLowThreshold": cltmRslt_ImpulseNoiseReadLowThreshold,
       "cltmRslt-ImpulseNoiseReadMidThreshold": cltmRslt_ImpulseNoiseReadMidThreshold,
       "cltmRslt-ImpulseNoiseReadHighThreshold": cltmRslt_ImpulseNoiseReadHighThreshold,
       "cltmRslt-RcvToneFrequency": cltmRslt_RcvToneFrequency,
       "cltmRslt-RcvToneLevel": cltmRslt_RcvToneLevel,
       "cltmRslt-TdrManualSampleCount": cltmRslt_TdrManualSampleCount,
       "cltmRslt-TdrAutomaticFaultDistance": cltmRslt_TdrAutomaticFaultDistance,
       "cltmRslt-HardwareRevision": cltmRslt_HardwareRevision,
       "cltmRslt-SofwareRevision": cltmRslt_SofwareRevision,
       "cltmRslt-DcDeltaResistanceTR": cltmRslt_DcDeltaResistanceTR,
       "cltmRslt-DcDeltaResistanceTS": cltmRslt_DcDeltaResistanceTS,
       "cltmRslt-DcDeltaResistanceRS": cltmRslt_DcDeltaResistanceRS,
       "cltmRslt-DcDeltaVoltageTS": cltmRslt_DcDeltaVoltageTS,
       "cltmRslt-DcDeltaVoltageRS": cltmRslt_DcDeltaVoltageRS,
       "cltmRslt-CapEquivalentTR": cltmRslt_CapEquivalentTR,
       "cltmRslt-CapEquivalentTS": cltmRslt_CapEquivalentTS,
       "cltmRslt-CapEquivalentRS": cltmRslt_CapEquivalentRS,
       "cltmRslt-DmmAllTR": cltmRslt_DmmAllTR,
       "cltmRslt-DmmAllTS": cltmRslt_DmmAllTS,
       "cltmRslt-DmmAllRS": cltmRslt_DmmAllRS,
       "cltmRslt-Ringer": cltmRslt_Ringer,
       "cltmRslt-AtuR": cltmRslt_AtuR,
       "cltmRslt-BridgeTapNumber": cltmRslt_BridgeTapNumber,
       "cltmRslt-BridgeTapLength": cltmRslt_BridgeTapLength,
       "cltmRslt-Action-o": cltmRslt_Action_o,
       "cltmRslt-VoiceDetection": cltmRslt_VoiceDetection,
       "cltmRslt-FirstCoilLocation": cltmRslt_FirstCoilLocation,
       "cltmRslt-ShortLocation": cltmRslt_ShortLocation,
       "mibcltmRslt-BridgeTapTableTable": mibcltmRslt_BridgeTapTableTable,
       "mibcltmRslt-BridgeTapTableEntry": mibcltmRslt_BridgeTapTableEntry,
       "cltmRslt-BridgeTapTable-Index-o": cltmRslt_BridgeTapTable_Index_o,
       "cltmRslt-BridgeTapTable-Index1-o": cltmRslt_BridgeTapTable_Index1_o,
       "cltmRslt-BridgeTapTable-Distance": cltmRslt_BridgeTapTable_Distance,
       "cltmRslt-BridgeTapTable-Length": cltmRslt_BridgeTapTable_Length,
       "cltmRslt-BridgeTapTable-Confidence": cltmRslt_BridgeTapTable_Confidence,
       "mibcltmRslt-TdrDistanceLevelTable": mibcltmRslt_TdrDistanceLevelTable,
       "mibcltmRslt-TdrDistanceLevelEntry": mibcltmRslt_TdrDistanceLevelEntry,
       "cltmRslt-TdrDistanceLevel-Index-o": cltmRslt_TdrDistanceLevel_Index_o,
       "cltmRslt-TdrDistanceLevel-Index1-o": cltmRslt_TdrDistanceLevel_Index1_o,
       "cltmRslt-TdrDistanceLevel-Distance": cltmRslt_TdrDistanceLevel_Distance,
       "cltmRslt-TdrDistanceLevel-Level": cltmRslt_TdrDistanceLevel_Level,
       "mibcltmRslt-PsdFrequencyLevelTable": mibcltmRslt_PsdFrequencyLevelTable,
       "mibcltmRslt-PsdFrequencyLevelEntry": mibcltmRslt_PsdFrequencyLevelEntry,
       "cltmRslt-PsdFrequencyLevel-Index-o": cltmRslt_PsdFrequencyLevel_Index_o,
       "cltmRslt-PsdFrequencyLevel-Index1-o": cltmRslt_PsdFrequencyLevel_Index1_o,
       "cltmRslt-PsdFrequencyLevel-Frequency": cltmRslt_PsdFrequencyLevel_Frequency,
       "cltmRslt-PsdFrequencyLevel-Level": cltmRslt_PsdFrequencyLevel_Level}
)
