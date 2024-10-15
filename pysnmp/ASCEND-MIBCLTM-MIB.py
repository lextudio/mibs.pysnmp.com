# SNMP MIB module (ASCEND-MIBCLTM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBCLTM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:20 2024
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

_MibcltmCmd_ObjectIdentity = ObjectIdentity
mibcltmCmd = _MibcltmCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 66)
)
_MibcltmCmdTable_Object = MibTable
mibcltmCmdTable = _MibcltmCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1)
)
if mibBuilder.loadTexts:
    mibcltmCmdTable.setStatus("mandatory")
_MibcltmCmdEntry_Object = MibTableRow
mibcltmCmdEntry = _MibcltmCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1)
)
mibcltmCmdEntry.setIndexNames(
    (0, "ASCEND-MIBCLTM-MIB", "cltmCmd-Index-o"),
)
if mibBuilder.loadTexts:
    mibcltmCmdEntry.setStatus("mandatory")
_CltmCmd_Index_o_Type = Integer32
_CltmCmd_Index_o_Object = MibScalar
cltmCmd_Index_o = _CltmCmd_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 1),
    _CltmCmd_Index_o_Type()
)
cltmCmd_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmCmd_Index_o.setStatus("mandatory")


class _CltmCmd_CltmSlot_Type(Integer32):
    """Custom type cltmCmd_CltmSlot based on Integer32"""
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


_CltmCmd_CltmSlot_Type.__name__ = "Integer32"
_CltmCmd_CltmSlot_Object = MibScalar
cltmCmd_CltmSlot = _CltmCmd_CltmSlot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 2),
    _CltmCmd_CltmSlot_Type()
)
cltmCmd_CltmSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmCmd_CltmSlot.setStatus("mandatory")
_CltmCmd_TestTimeStamp_Type = Integer32
_CltmCmd_TestTimeStamp_Object = MibScalar
cltmCmd_TestTimeStamp = _CltmCmd_TestTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 3),
    _CltmCmd_TestTimeStamp_Type()
)
cltmCmd_TestTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmCmd_TestTimeStamp.setStatus("mandatory")
_CltmCmd_TestSequence_Type = Integer32
_CltmCmd_TestSequence_Object = MibScalar
cltmCmd_TestSequence = _CltmCmd_TestSequence_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 4),
    _CltmCmd_TestSequence_Type()
)
cltmCmd_TestSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltmCmd_TestSequence.setStatus("mandatory")


class _CltmCmd_TestOperation_Type(Integer32):
    """Custom type cltmCmd_TestOperation based on Integer32"""
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
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40)
        )
    )
    namedValues = NamedValues(
        *(("btapTest", 27),
          ("calibTest", 11),
          ("cltmDownload", 18),
          ("cltmReset", 16),
          ("cltmVersion", 17),
          ("detAturTest", 26),
          ("detRingerTest", 25),
          ("detaptorTest", 40),
          ("dmmAcdelTest", 34),
          ("dmmAllTest", 21),
          ("dmmCapeTest", 20),
          ("dmmDcdelTest", 19),
          ("dmmLbalTest", 35),
          ("dmmSoakTest", 36),
          ("dmmTest", 2),
          ("lineBgnsTest", 4),
          ("lineCldetTest", 7),
          ("lineFcllocTest", 29),
          ("lineImpreadTest", 10),
          ("lineImpstartTest", 8),
          ("lineImpstopTest", 9),
          ("lineInlsTest", 3),
          ("lineLpresTest", 6),
          ("lineShortlocTest", 30),
          ("lineSignsTest", 5),
          ("measDtaTest", 39),
          ("measVoiceTest", 38),
          ("none", 1),
          ("sendVoiceTest", 37),
          ("setBypassTest", 32),
          ("setResponderTest", 31),
          ("splitterDetectTest", 33),
          ("stopToneTest", 24),
          ("tdrGet", 15),
          ("tdrSet", 14),
          ("toneRecv", 13),
          ("toneSend", 12),
          ("txCtrlToneTest", 22),
          ("txTraceToneTest", 23),
          ("voiceDetTest", 28))
    )


_CltmCmd_TestOperation_Type.__name__ = "Integer32"
_CltmCmd_TestOperation_Object = MibScalar
cltmCmd_TestOperation = _CltmCmd_TestOperation_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 5),
    _CltmCmd_TestOperation_Type()
)
cltmCmd_TestOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_TestOperation.setStatus("mandatory")


class _CltmCmd_DmmType_Type(Integer32):
    """Custom type cltmCmd_DmmType based on Integer32"""
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
        *(("acVoltage", 3),
          ("capacitance", 4),
          ("dcVoltage", 2),
          ("resistance", 1))
    )


_CltmCmd_DmmType_Type.__name__ = "Integer32"
_CltmCmd_DmmType_Object = MibScalar
cltmCmd_DmmType = _CltmCmd_DmmType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 6),
    _CltmCmd_DmmType_Type()
)
cltmCmd_DmmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_DmmType.setStatus("mandatory")


class _CltmCmd_DmmLead_Type(Integer32):
    """Custom type cltmCmd_DmmLead based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ringSleeve", 3),
          ("tipRing", 1),
          ("tipSleeve", 2))
    )


_CltmCmd_DmmLead_Type.__name__ = "Integer32"
_CltmCmd_DmmLead_Object = MibScalar
cltmCmd_DmmLead = _CltmCmd_DmmLead_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 7),
    _CltmCmd_DmmLead_Type()
)
cltmCmd_DmmLead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_DmmLead.setStatus("mandatory")


class _CltmCmd_BackgroundNoiseFilter_Type(Integer32):
    """Custom type cltmCmd_BackgroundNoiseFilter based on Integer32"""
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
        *(("e", 2),
          ("f", 3),
          ("g", 4),
          ("psd", 1))
    )


_CltmCmd_BackgroundNoiseFilter_Type.__name__ = "Integer32"
_CltmCmd_BackgroundNoiseFilter_Object = MibScalar
cltmCmd_BackgroundNoiseFilter = _CltmCmd_BackgroundNoiseFilter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 8),
    _CltmCmd_BackgroundNoiseFilter_Type()
)
cltmCmd_BackgroundNoiseFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_BackgroundNoiseFilter.setStatus("mandatory")


class _CltmCmd_BackgroundNoiseTermination_Type(Integer32):
    """Custom type cltmCmd_BackgroundNoiseTermination based on Integer32"""
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
        *(("bridge100", 3),
          ("bridge135", 4),
          ("term100", 1),
          ("term135", 2))
    )


_CltmCmd_BackgroundNoiseTermination_Type.__name__ = "Integer32"
_CltmCmd_BackgroundNoiseTermination_Object = MibScalar
cltmCmd_BackgroundNoiseTermination = _CltmCmd_BackgroundNoiseTermination_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 9),
    _CltmCmd_BackgroundNoiseTermination_Type()
)
cltmCmd_BackgroundNoiseTermination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_BackgroundNoiseTermination.setStatus("mandatory")


class _CltmCmd_LoopResistanceUnit_Type(Integer32):
    """Custom type cltmCmd_LoopResistanceUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("english", 2),
          ("metric", 1))
    )


_CltmCmd_LoopResistanceUnit_Type.__name__ = "Integer32"
_CltmCmd_LoopResistanceUnit_Object = MibScalar
cltmCmd_LoopResistanceUnit = _CltmCmd_LoopResistanceUnit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 10),
    _CltmCmd_LoopResistanceUnit_Type()
)
cltmCmd_LoopResistanceUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_LoopResistanceUnit.setStatus("mandatory")
_CltmCmd_LoopResistanceTemp_Type = Integer32
_CltmCmd_LoopResistanceTemp_Object = MibScalar
cltmCmd_LoopResistanceTemp = _CltmCmd_LoopResistanceTemp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 11),
    _CltmCmd_LoopResistanceTemp_Type()
)
cltmCmd_LoopResistanceTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_LoopResistanceTemp.setStatus("mandatory")
_CltmCmd_ImpulseNoiseStartThresh_Type = Integer32
_CltmCmd_ImpulseNoiseStartThresh_Object = MibScalar
cltmCmd_ImpulseNoiseStartThresh = _CltmCmd_ImpulseNoiseStartThresh_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 12),
    _CltmCmd_ImpulseNoiseStartThresh_Type()
)
cltmCmd_ImpulseNoiseStartThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_ImpulseNoiseStartThresh.setStatus("mandatory")
_CltmCmd_ImpulseNoiseStartDelta_Type = Integer32
_CltmCmd_ImpulseNoiseStartDelta_Object = MibScalar
cltmCmd_ImpulseNoiseStartDelta = _CltmCmd_ImpulseNoiseStartDelta_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 13),
    _CltmCmd_ImpulseNoiseStartDelta_Type()
)
cltmCmd_ImpulseNoiseStartDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_ImpulseNoiseStartDelta.setStatus("mandatory")
_CltmCmd_ImpulseNoiseStartMaxCount_Type = Integer32
_CltmCmd_ImpulseNoiseStartMaxCount_Object = MibScalar
cltmCmd_ImpulseNoiseStartMaxCount = _CltmCmd_ImpulseNoiseStartMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 14),
    _CltmCmd_ImpulseNoiseStartMaxCount_Type()
)
cltmCmd_ImpulseNoiseStartMaxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_ImpulseNoiseStartMaxCount.setStatus("mandatory")
_CltmCmd_ImpulseNoiseStartDeadTime_Type = Integer32
_CltmCmd_ImpulseNoiseStartDeadTime_Object = MibScalar
cltmCmd_ImpulseNoiseStartDeadTime = _CltmCmd_ImpulseNoiseStartDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 15),
    _CltmCmd_ImpulseNoiseStartDeadTime_Type()
)
cltmCmd_ImpulseNoiseStartDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_ImpulseNoiseStartDeadTime.setStatus("mandatory")
_CltmCmd_ImpulseNoiseStartTimer_Type = Integer32
_CltmCmd_ImpulseNoiseStartTimer_Object = MibScalar
cltmCmd_ImpulseNoiseStartTimer = _CltmCmd_ImpulseNoiseStartTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 16),
    _CltmCmd_ImpulseNoiseStartTimer_Type()
)
cltmCmd_ImpulseNoiseStartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_ImpulseNoiseStartTimer.setStatus("mandatory")


class _CltmCmd_CalibrationType_Type(Integer32):
    """Custom type cltmCmd_CalibrationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backgroundNoise", 2),
          ("insertionLoss", 1))
    )


_CltmCmd_CalibrationType_Type.__name__ = "Integer32"
_CltmCmd_CalibrationType_Object = MibScalar
cltmCmd_CalibrationType = _CltmCmd_CalibrationType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 17),
    _CltmCmd_CalibrationType_Type()
)
cltmCmd_CalibrationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_CalibrationType.setStatus("mandatory")
_CltmCmd_ToneSendFreq_Type = Integer32
_CltmCmd_ToneSendFreq_Object = MibScalar
cltmCmd_ToneSendFreq = _CltmCmd_ToneSendFreq_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 18),
    _CltmCmd_ToneSendFreq_Type()
)
cltmCmd_ToneSendFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_ToneSendFreq.setStatus("mandatory")
_CltmCmd_ToneSendLevel_Type = Integer32
_CltmCmd_ToneSendLevel_Object = MibScalar
cltmCmd_ToneSendLevel = _CltmCmd_ToneSendLevel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 19),
    _CltmCmd_ToneSendLevel_Type()
)
cltmCmd_ToneSendLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_ToneSendLevel.setStatus("mandatory")
_CltmCmd_ToneSendPeriod_Type = Integer32
_CltmCmd_ToneSendPeriod_Object = MibScalar
cltmCmd_ToneSendPeriod = _CltmCmd_ToneSendPeriod_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 20),
    _CltmCmd_ToneSendPeriod_Type()
)
cltmCmd_ToneSendPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_ToneSendPeriod.setStatus("mandatory")


class _CltmCmd_TdrUnit_Type(Integer32):
    """Custom type cltmCmd_TdrUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("english", 2),
          ("metric", 1))
    )


_CltmCmd_TdrUnit_Type.__name__ = "Integer32"
_CltmCmd_TdrUnit_Object = MibScalar
cltmCmd_TdrUnit = _CltmCmd_TdrUnit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 21),
    _CltmCmd_TdrUnit_Type()
)
cltmCmd_TdrUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_TdrUnit.setStatus("mandatory")
_CltmCmd_TdrGauge_Type = Integer32
_CltmCmd_TdrGauge_Object = MibScalar
cltmCmd_TdrGauge = _CltmCmd_TdrGauge_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 22),
    _CltmCmd_TdrGauge_Type()
)
cltmCmd_TdrGauge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_TdrGauge.setStatus("mandatory")
_CltmCmd_TdrVp_Type = Integer32
_CltmCmd_TdrVp_Object = MibScalar
cltmCmd_TdrVp = _CltmCmd_TdrVp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 23),
    _CltmCmd_TdrVp_Type()
)
cltmCmd_TdrVp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_TdrVp.setStatus("mandatory")
_CltmCmd_TdrAvg_Type = Integer32
_CltmCmd_TdrAvg_Object = MibScalar
cltmCmd_TdrAvg = _CltmCmd_TdrAvg_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 24),
    _CltmCmd_TdrAvg_Type()
)
cltmCmd_TdrAvg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_TdrAvg.setStatus("mandatory")


class _CltmCmd_TdrGetType_Type(Integer32):
    """Custom type cltmCmd_TdrGetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_CltmCmd_TdrGetType_Type.__name__ = "Integer32"
_CltmCmd_TdrGetType_Object = MibScalar
cltmCmd_TdrGetType = _CltmCmd_TdrGetType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 25),
    _CltmCmd_TdrGetType_Type()
)
cltmCmd_TdrGetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_TdrGetType.setStatus("mandatory")
_CltmCmd_TdrStartDistance_Type = Integer32
_CltmCmd_TdrStartDistance_Object = MibScalar
cltmCmd_TdrStartDistance = _CltmCmd_TdrStartDistance_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 26),
    _CltmCmd_TdrStartDistance_Type()
)
cltmCmd_TdrStartDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_TdrStartDistance.setStatus("mandatory")
_CltmCmd_TdrMeasurementLength_Type = Integer32
_CltmCmd_TdrMeasurementLength_Object = MibScalar
cltmCmd_TdrMeasurementLength = _CltmCmd_TdrMeasurementLength_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 27),
    _CltmCmd_TdrMeasurementLength_Type()
)
cltmCmd_TdrMeasurementLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_TdrMeasurementLength.setStatus("mandatory")
_CltmCmd_DmmdcdPeriod_Type = Integer32
_CltmCmd_DmmdcdPeriod_Object = MibScalar
cltmCmd_DmmdcdPeriod = _CltmCmd_DmmdcdPeriod_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 28),
    _CltmCmd_DmmdcdPeriod_Type()
)
cltmCmd_DmmdcdPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_DmmdcdPeriod.setStatus("mandatory")
_CltmCmd_DmmdcdVoltage_Type = Integer32
_CltmCmd_DmmdcdVoltage_Object = MibScalar
cltmCmd_DmmdcdVoltage = _CltmCmd_DmmdcdVoltage_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 29),
    _CltmCmd_DmmdcdVoltage_Type()
)
cltmCmd_DmmdcdVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_DmmdcdVoltage.setStatus("mandatory")
_CltmCmd_DmmdcdImpedance_Type = Integer32
_CltmCmd_DmmdcdImpedance_Object = MibScalar
cltmCmd_DmmdcdImpedance = _CltmCmd_DmmdcdImpedance_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 30),
    _CltmCmd_DmmdcdImpedance_Type()
)
cltmCmd_DmmdcdImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_DmmdcdImpedance.setStatus("mandatory")
_CltmCmd_DmmcapPeriod_Type = Integer32
_CltmCmd_DmmcapPeriod_Object = MibScalar
cltmCmd_DmmcapPeriod = _CltmCmd_DmmcapPeriod_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 31),
    _CltmCmd_DmmcapPeriod_Type()
)
cltmCmd_DmmcapPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_DmmcapPeriod.setStatus("mandatory")


class _CltmCmd_DmmallType_Type(Integer32):
    """Custom type cltmCmd_DmmallType based on Integer32"""
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
        *(("acVoltage", 3),
          ("capacitance", 4),
          ("dcVoltage", 2),
          ("resistance", 1))
    )


_CltmCmd_DmmallType_Type.__name__ = "Integer32"
_CltmCmd_DmmallType_Object = MibScalar
cltmCmd_DmmallType = _CltmCmd_DmmallType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 32),
    _CltmCmd_DmmallType_Type()
)
cltmCmd_DmmallType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_DmmallType.setStatus("mandatory")
_CltmCmd_DmmallPeriod_Type = Integer32
_CltmCmd_DmmallPeriod_Object = MibScalar
cltmCmd_DmmallPeriod = _CltmCmd_DmmallPeriod_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 33),
    _CltmCmd_DmmallPeriod_Type()
)
cltmCmd_DmmallPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_DmmallPeriod.setStatus("mandatory")
_CltmCmd_DmmallInputImp_Type = Integer32
_CltmCmd_DmmallInputImp_Object = MibScalar
cltmCmd_DmmallInputImp = _CltmCmd_DmmallInputImp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 34),
    _CltmCmd_DmmallInputImp_Type()
)
cltmCmd_DmmallInputImp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_DmmallInputImp.setStatus("mandatory")


class _CltmCmd_CtoneType_Type(Integer32):
    """Custom type cltmCmd_CtoneType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adsl", 1),
          ("glite", 2))
    )


_CltmCmd_CtoneType_Type.__name__ = "Integer32"
_CltmCmd_CtoneType_Object = MibScalar
cltmCmd_CtoneType = _CltmCmd_CtoneType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 35),
    _CltmCmd_CtoneType_Type()
)
cltmCmd_CtoneType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_CtoneType.setStatus("mandatory")


class _CltmCmd_CtoneTone_Type(Integer32):
    """Custom type cltmCmd_CtoneTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("quiet", 1),
          ("restore", 2))
    )


_CltmCmd_CtoneTone_Type.__name__ = "Integer32"
_CltmCmd_CtoneTone_Object = MibScalar
cltmCmd_CtoneTone = _CltmCmd_CtoneTone_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 36),
    _CltmCmd_CtoneTone_Type()
)
cltmCmd_CtoneTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_CtoneTone.setStatus("mandatory")


class _CltmCmd_TtoneLead_Type(Integer32):
    """Custom type cltmCmd_TtoneLead based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ringSleeve", 3),
          ("tipRing", 1),
          ("tipSleeve", 2))
    )


_CltmCmd_TtoneLead_Type.__name__ = "Integer32"
_CltmCmd_TtoneLead_Object = MibScalar
cltmCmd_TtoneLead = _CltmCmd_TtoneLead_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 37),
    _CltmCmd_TtoneLead_Type()
)
cltmCmd_TtoneLead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_TtoneLead.setStatus("mandatory")
_CltmCmd_TtoneLevel_Type = Integer32
_CltmCmd_TtoneLevel_Object = MibScalar
cltmCmd_TtoneLevel = _CltmCmd_TtoneLevel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 38),
    _CltmCmd_TtoneLevel_Type()
)
cltmCmd_TtoneLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_TtoneLevel.setStatus("mandatory")
_CltmCmd_TtonePeriod_Type = Integer32
_CltmCmd_TtonePeriod_Object = MibScalar
cltmCmd_TtonePeriod = _CltmCmd_TtonePeriod_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 39),
    _CltmCmd_TtonePeriod_Type()
)
cltmCmd_TtonePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_TtonePeriod.setStatus("mandatory")
_CltmCmd_BtapStartLength_Type = Integer32
_CltmCmd_BtapStartLength_Object = MibScalar
cltmCmd_BtapStartLength = _CltmCmd_BtapStartLength_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 40),
    _CltmCmd_BtapStartLength_Type()
)
cltmCmd_BtapStartLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_BtapStartLength.setStatus("mandatory")
_CltmCmd_BtapMeasureLength_Type = Integer32
_CltmCmd_BtapMeasureLength_Object = MibScalar
cltmCmd_BtapMeasureLength = _CltmCmd_BtapMeasureLength_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 41),
    _CltmCmd_BtapMeasureLength_Type()
)
cltmCmd_BtapMeasureLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_BtapMeasureLength.setStatus("mandatory")


class _CltmCmd_Action_o_Type(Integer32):
    """Custom type cltmCmd_Action_o based on Integer32"""
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


_CltmCmd_Action_o_Type.__name__ = "Integer32"
_CltmCmd_Action_o_Object = MibScalar
cltmCmd_Action_o = _CltmCmd_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 42),
    _CltmCmd_Action_o_Type()
)
cltmCmd_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_Action_o.setStatus("mandatory")


class _CltmCmd_FcllocUnit_Type(Integer32):
    """Custom type cltmCmd_FcllocUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("english", 2),
          ("metric", 1))
    )


_CltmCmd_FcllocUnit_Type.__name__ = "Integer32"
_CltmCmd_FcllocUnit_Object = MibScalar
cltmCmd_FcllocUnit = _CltmCmd_FcllocUnit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 43),
    _CltmCmd_FcllocUnit_Type()
)
cltmCmd_FcllocUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_FcllocUnit.setStatus("mandatory")
_CltmCmd_FcllocGauge_Type = Integer32
_CltmCmd_FcllocGauge_Object = MibScalar
cltmCmd_FcllocGauge = _CltmCmd_FcllocGauge_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 44),
    _CltmCmd_FcllocGauge_Type()
)
cltmCmd_FcllocGauge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_FcllocGauge.setStatus("mandatory")


class _CltmCmd_ShortlocUnit_Type(Integer32):
    """Custom type cltmCmd_ShortlocUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("english", 2),
          ("metric", 1))
    )


_CltmCmd_ShortlocUnit_Type.__name__ = "Integer32"
_CltmCmd_ShortlocUnit_Object = MibScalar
cltmCmd_ShortlocUnit = _CltmCmd_ShortlocUnit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 45),
    _CltmCmd_ShortlocUnit_Type()
)
cltmCmd_ShortlocUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_ShortlocUnit.setStatus("mandatory")
_CltmCmd_ShortlocGauge_Type = Integer32
_CltmCmd_ShortlocGauge_Object = MibScalar
cltmCmd_ShortlocGauge = _CltmCmd_ShortlocGauge_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 46),
    _CltmCmd_ShortlocGauge_Type()
)
cltmCmd_ShortlocGauge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_ShortlocGauge.setStatus("mandatory")


class _CltmCmd_ShortlocType_Type(Integer32):
    """Custom type cltmCmd_ShortlocType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detect", 1),
          ("noDetect", 2))
    )


_CltmCmd_ShortlocType_Type.__name__ = "Integer32"
_CltmCmd_ShortlocType_Object = MibScalar
cltmCmd_ShortlocType = _CltmCmd_ShortlocType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 47),
    _CltmCmd_ShortlocType_Type()
)
cltmCmd_ShortlocType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltmCmd_ShortlocType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBCLTM-MIB",
    **{"DisplayString": DisplayString,
       "mibcltmCmd": mibcltmCmd,
       "mibcltmCmdTable": mibcltmCmdTable,
       "mibcltmCmdEntry": mibcltmCmdEntry,
       "cltmCmd-Index-o": cltmCmd_Index_o,
       "cltmCmd-CltmSlot": cltmCmd_CltmSlot,
       "cltmCmd-TestTimeStamp": cltmCmd_TestTimeStamp,
       "cltmCmd-TestSequence": cltmCmd_TestSequence,
       "cltmCmd-TestOperation": cltmCmd_TestOperation,
       "cltmCmd-DmmType": cltmCmd_DmmType,
       "cltmCmd-DmmLead": cltmCmd_DmmLead,
       "cltmCmd-BackgroundNoiseFilter": cltmCmd_BackgroundNoiseFilter,
       "cltmCmd-BackgroundNoiseTermination": cltmCmd_BackgroundNoiseTermination,
       "cltmCmd-LoopResistanceUnit": cltmCmd_LoopResistanceUnit,
       "cltmCmd-LoopResistanceTemp": cltmCmd_LoopResistanceTemp,
       "cltmCmd-ImpulseNoiseStartThresh": cltmCmd_ImpulseNoiseStartThresh,
       "cltmCmd-ImpulseNoiseStartDelta": cltmCmd_ImpulseNoiseStartDelta,
       "cltmCmd-ImpulseNoiseStartMaxCount": cltmCmd_ImpulseNoiseStartMaxCount,
       "cltmCmd-ImpulseNoiseStartDeadTime": cltmCmd_ImpulseNoiseStartDeadTime,
       "cltmCmd-ImpulseNoiseStartTimer": cltmCmd_ImpulseNoiseStartTimer,
       "cltmCmd-CalibrationType": cltmCmd_CalibrationType,
       "cltmCmd-ToneSendFreq": cltmCmd_ToneSendFreq,
       "cltmCmd-ToneSendLevel": cltmCmd_ToneSendLevel,
       "cltmCmd-ToneSendPeriod": cltmCmd_ToneSendPeriod,
       "cltmCmd-TdrUnit": cltmCmd_TdrUnit,
       "cltmCmd-TdrGauge": cltmCmd_TdrGauge,
       "cltmCmd-TdrVp": cltmCmd_TdrVp,
       "cltmCmd-TdrAvg": cltmCmd_TdrAvg,
       "cltmCmd-TdrGetType": cltmCmd_TdrGetType,
       "cltmCmd-TdrStartDistance": cltmCmd_TdrStartDistance,
       "cltmCmd-TdrMeasurementLength": cltmCmd_TdrMeasurementLength,
       "cltmCmd-DmmdcdPeriod": cltmCmd_DmmdcdPeriod,
       "cltmCmd-DmmdcdVoltage": cltmCmd_DmmdcdVoltage,
       "cltmCmd-DmmdcdImpedance": cltmCmd_DmmdcdImpedance,
       "cltmCmd-DmmcapPeriod": cltmCmd_DmmcapPeriod,
       "cltmCmd-DmmallType": cltmCmd_DmmallType,
       "cltmCmd-DmmallPeriod": cltmCmd_DmmallPeriod,
       "cltmCmd-DmmallInputImp": cltmCmd_DmmallInputImp,
       "cltmCmd-CtoneType": cltmCmd_CtoneType,
       "cltmCmd-CtoneTone": cltmCmd_CtoneTone,
       "cltmCmd-TtoneLead": cltmCmd_TtoneLead,
       "cltmCmd-TtoneLevel": cltmCmd_TtoneLevel,
       "cltmCmd-TtonePeriod": cltmCmd_TtonePeriod,
       "cltmCmd-BtapStartLength": cltmCmd_BtapStartLength,
       "cltmCmd-BtapMeasureLength": cltmCmd_BtapMeasureLength,
       "cltmCmd-Action-o": cltmCmd_Action_o,
       "cltmCmd-FcllocUnit": cltmCmd_FcllocUnit,
       "cltmCmd-FcllocGauge": cltmCmd_FcllocGauge,
       "cltmCmd-ShortlocUnit": cltmCmd_ShortlocUnit,
       "cltmCmd-ShortlocGauge": cltmCmd_ShortlocGauge,
       "cltmCmd-ShortlocType": cltmCmd_ShortlocType}
)
