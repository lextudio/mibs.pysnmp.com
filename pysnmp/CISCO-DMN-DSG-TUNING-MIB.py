# SNMP MIB module (CISCO-DMN-DSG-TUNING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-TUNING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:37 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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

ciscoDSGTuning = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5)
)
ciscoDSGTuning.setRevisions(
        ("2012-11-19 08:00",
         "2010-10-13 08:00",
         "2010-08-03 09:00",
         "2010-06-17 06:00",
         "2010-05-03 11:00",
         "2010-04-12 09:00",
         "2010-03-22 05:00",
         "2010-02-12 15:00",
         "2010-01-18 15:00",
         "2009-12-20 15:00",
         "2009-11-22 15:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ActiveTuning_ObjectIdentity = ObjectIdentity
activeTuning = _ActiveTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 1)
)


class _ActiveTuningInput_Type(Integer32):
    """Custom type activeTuningInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("asi", 1),
          ("ipi", 6),
          ("none", 255),
          ("rf1", 2),
          ("rf2", 3),
          ("rf3", 4),
          ("rf4", 5))
    )


_ActiveTuningInput_Type.__name__ = "Integer32"
_ActiveTuningInput_Object = MibScalar
activeTuningInput = _ActiveTuningInput_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 1, 1),
    _ActiveTuningInput_Type()
)
activeTuningInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeTuningInput.setStatus("current")


class _ActiveTuningValidateOrbPos_Type(Integer32):
    """Custom type activeTuningValidateOrbPos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("writeOnly", 1),
          ("yes", 2))
    )


_ActiveTuningValidateOrbPos_Type.__name__ = "Integer32"
_ActiveTuningValidateOrbPos_Object = MibScalar
activeTuningValidateOrbPos = _ActiveTuningValidateOrbPos_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 1, 2),
    _ActiveTuningValidateOrbPos_Type()
)
activeTuningValidateOrbPos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeTuningValidateOrbPos.setStatus("current")


class _ActiveTuningChScan_Type(Integer32):
    """Custom type activeTuningChScan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("scan", 1),
          ("writeOnly", 2))
    )


_ActiveTuningChScan_Type.__name__ = "Integer32"
_ActiveTuningChScan_Object = MibScalar
activeTuningChScan = _ActiveTuningChScan_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 1, 3),
    _ActiveTuningChScan_Type()
)
activeTuningChScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeTuningChScan.setStatus("current")
_ActiveTuningTable_ObjectIdentity = ObjectIdentity
activeTuningTable = _ActiveTuningTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2)
)
_ActiveTunerTable_Object = MibTable
activeTunerTable = _ActiveTunerTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 1)
)
if mibBuilder.loadTexts:
    activeTunerTable.setStatus("current")
_ActiveTunerEntry_Object = MibTableRow
activeTunerEntry = _ActiveTunerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 1, 1)
)
activeTunerEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-TUNING-MIB", "activeTunerIndex"),
)
if mibBuilder.loadTexts:
    activeTunerEntry.setStatus("current")


class _ActiveTunerIndex_Type(Integer32):
    """Custom type activeTunerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ActiveTunerIndex_Type.__name__ = "Integer32"
_ActiveTunerIndex_Object = MibTableColumn
activeTunerIndex = _ActiveTunerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 1, 1, 1),
    _ActiveTunerIndex_Type()
)
activeTunerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    activeTunerIndex.setStatus("current")


class _ActiveTunerRFInput_Type(Integer32):
    """Custom type activeTunerRFInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 255),
          ("rf1", 2),
          ("rf2", 3),
          ("rf3", 4),
          ("rf4", 5))
    )


_ActiveTunerRFInput_Type.__name__ = "Integer32"
_ActiveTunerRFInput_Object = MibTableColumn
activeTunerRFInput = _ActiveTunerRFInput_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 1, 1, 2),
    _ActiveTunerRFInput_Type()
)
activeTunerRFInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeTunerRFInput.setStatus("current")


class _ActiveTunerFreq_Type(Integer32):
    """Custom type activeTunerFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000000),
    )


_ActiveTunerFreq_Type.__name__ = "Integer32"
_ActiveTunerFreq_Object = MibTableColumn
activeTunerFreq = _ActiveTunerFreq_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 1, 1, 3),
    _ActiveTunerFreq_Type()
)
activeTunerFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeTunerFreq.setStatus("current")


class _ActiveTunerSymbolRate_Type(Integer32):
    """Custom type activeTunerSymbolRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 450000),
    )


_ActiveTunerSymbolRate_Type.__name__ = "Integer32"
_ActiveTunerSymbolRate_Object = MibTableColumn
activeTunerSymbolRate = _ActiveTunerSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 1, 1, 4),
    _ActiveTunerSymbolRate_Type()
)
activeTunerSymbolRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeTunerSymbolRate.setStatus("current")


class _ActiveTunerDVBSFEC_Type(Integer32):
    """Custom type activeTunerDVBSFEC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              6,
              7,
              10)
        )
    )
    namedValues = NamedValues(
        *(("auto", 10),
          ("fiveSixths", 6),
          ("oneHalf", 1),
          ("sevenEigths", 7),
          ("threeQuarters", 4),
          ("twoThirds", 3))
    )


_ActiveTunerDVBSFEC_Type.__name__ = "Integer32"
_ActiveTunerDVBSFEC_Object = MibTableColumn
activeTunerDVBSFEC = _ActiveTunerDVBSFEC_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 1, 1, 5),
    _ActiveTunerDVBSFEC_Type()
)
activeTunerDVBSFEC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeTunerDVBSFEC.setStatus("current")


class _ActiveTunerModulation_Type(Integer32):
    """Custom type activeTunerModulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dvbs", 1),
          ("dvbs2", 2))
    )


_ActiveTunerModulation_Type.__name__ = "Integer32"
_ActiveTunerModulation_Object = MibTableColumn
activeTunerModulation = _ActiveTunerModulation_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 1, 1, 6),
    _ActiveTunerModulation_Type()
)
activeTunerModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeTunerModulation.setStatus("current")


class _ActiveTunerRollOff_Type(Integer32):
    """Custom type activeTunerRollOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("f20", 3),
          ("f25", 2),
          ("f35", 1))
    )


_ActiveTunerRollOff_Type.__name__ = "Integer32"
_ActiveTunerRollOff_Object = MibTableColumn
activeTunerRollOff = _ActiveTunerRollOff_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 1, 1, 7),
    _ActiveTunerRollOff_Type()
)
activeTunerRollOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeTunerRollOff.setStatus("current")


class _ActiveTunerIQ_Type(Integer32):
    """Custom type activeTunerIQ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("inverted", 1),
          ("nonInverted", 2))
    )


_ActiveTunerIQ_Type.__name__ = "Integer32"
_ActiveTunerIQ_Object = MibTableColumn
activeTunerIQ = _ActiveTunerIQ_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 1, 1, 8),
    _ActiveTunerIQ_Type()
)
activeTunerIQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeTunerIQ.setStatus("current")
_ActiveInputTable_Object = MibTable
activeInputTable = _ActiveInputTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 2)
)
if mibBuilder.loadTexts:
    activeInputTable.setStatus("current")
_ActiveInputEntry_Object = MibTableRow
activeInputEntry = _ActiveInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 2, 1)
)
activeInputEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-TUNING-MIB", "activeInputRFIndex"),
)
if mibBuilder.loadTexts:
    activeInputEntry.setStatus("current")


class _ActiveInputRFIndex_Type(Integer32):
    """Custom type activeInputRFIndex based on Integer32"""
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
        *(("rf1", 1),
          ("rf2", 2),
          ("rf3", 3),
          ("rf4", 4))
    )


_ActiveInputRFIndex_Type.__name__ = "Integer32"
_ActiveInputRFIndex_Object = MibTableColumn
activeInputRFIndex = _ActiveInputRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 2, 1, 1),
    _ActiveInputRFIndex_Type()
)
activeInputRFIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    activeInputRFIndex.setStatus("current")


class _ActiveInputLNBType_Type(Integer32):
    """Custom type activeInputLNBType based on Integer32"""
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
        *(("advanced", 4),
          ("cBand", 1),
          ("dualKuBand", 3),
          ("singleKuBand", 2))
    )


_ActiveInputLNBType_Type.__name__ = "Integer32"
_ActiveInputLNBType_Object = MibTableColumn
activeInputLNBType = _ActiveInputLNBType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 2, 1, 2),
    _ActiveInputLNBType_Type()
)
activeInputLNBType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeInputLNBType.setStatus("current")


class _ActiveInputLNBTrim_Type(Integer32):
    """Custom type activeInputLNBTrim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000000),
    )


_ActiveInputLNBTrim_Type.__name__ = "Integer32"
_ActiveInputLNBTrim_Object = MibTableColumn
activeInputLNBTrim = _ActiveInputLNBTrim_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 2, 1, 3),
    _ActiveInputLNBTrim_Type()
)
activeInputLNBTrim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeInputLNBTrim.setStatus("current")


class _ActiveInputLNBTrim2_Type(Integer32):
    """Custom type activeInputLNBTrim2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000000),
    )


_ActiveInputLNBTrim2_Type.__name__ = "Integer32"
_ActiveInputLNBTrim2_Object = MibTableColumn
activeInputLNBTrim2 = _ActiveInputLNBTrim2_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 2, 1, 4),
    _ActiveInputLNBTrim2_Type()
)
activeInputLNBTrim2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeInputLNBTrim2.setStatus("current")


class _ActiveInputLocalOscFreq1_Type(Integer32):
    """Custom type activeInputLocalOscFreq1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000000),
    )


_ActiveInputLocalOscFreq1_Type.__name__ = "Integer32"
_ActiveInputLocalOscFreq1_Object = MibTableColumn
activeInputLocalOscFreq1 = _ActiveInputLocalOscFreq1_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 2, 1, 5),
    _ActiveInputLocalOscFreq1_Type()
)
activeInputLocalOscFreq1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeInputLocalOscFreq1.setStatus("current")


class _ActiveInputLocalOscFreq2_Type(Integer32):
    """Custom type activeInputLocalOscFreq2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000000),
    )


_ActiveInputLocalOscFreq2_Type.__name__ = "Integer32"
_ActiveInputLocalOscFreq2_Object = MibTableColumn
activeInputLocalOscFreq2 = _ActiveInputLocalOscFreq2_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 2, 1, 6),
    _ActiveInputLocalOscFreq2_Type()
)
activeInputLocalOscFreq2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeInputLocalOscFreq2.setStatus("current")


class _ActiveInputCrossOver_Type(Integer32):
    """Custom type activeInputCrossOver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000000),
    )


_ActiveInputCrossOver_Type.__name__ = "Integer32"
_ActiveInputCrossOver_Object = MibTableColumn
activeInputCrossOver = _ActiveInputCrossOver_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 2, 1, 7),
    _ActiveInputCrossOver_Type()
)
activeInputCrossOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeInputCrossOver.setStatus("current")


class _ActiveInputLocalOscControl_Type(Integer32):
    """Custom type activeInputLocalOscControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("off", 1),
          ("on", 2))
    )


_ActiveInputLocalOscControl_Type.__name__ = "Integer32"
_ActiveInputLocalOscControl_Object = MibTableColumn
activeInputLocalOscControl = _ActiveInputLocalOscControl_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 2, 1, 8),
    _ActiveInputLocalOscControl_Type()
)
activeInputLocalOscControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeInputLocalOscControl.setStatus("current")


class _ActiveInputOrbitalPos_Type(Integer32):
    """Custom type activeInputOrbitalPos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_ActiveInputOrbitalPos_Type.__name__ = "Integer32"
_ActiveInputOrbitalPos_Object = MibTableColumn
activeInputOrbitalPos = _ActiveInputOrbitalPos_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 2, 1, 9),
    _ActiveInputOrbitalPos_Type()
)
activeInputOrbitalPos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeInputOrbitalPos.setStatus("current")


class _ActiveInputEastWestFlag_Type(Integer32):
    """Custom type activeInputEastWestFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("east", 1),
          ("notApplicable", 3),
          ("west", 2))
    )


_ActiveInputEastWestFlag_Type.__name__ = "Integer32"
_ActiveInputEastWestFlag_Object = MibTableColumn
activeInputEastWestFlag = _ActiveInputEastWestFlag_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 2, 1, 10),
    _ActiveInputEastWestFlag_Type()
)
activeInputEastWestFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeInputEastWestFlag.setStatus("current")


class _ActiveInputPolarization_Type(Integer32):
    """Custom type activeInputPolarization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 3),
          ("horizontal", 1),
          ("vertical", 2))
    )


_ActiveInputPolarization_Type.__name__ = "Integer32"
_ActiveInputPolarization_Object = MibTableColumn
activeInputPolarization = _ActiveInputPolarization_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 2, 1, 11),
    _ActiveInputPolarization_Type()
)
activeInputPolarization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeInputPolarization.setStatus("current")


class _ActiveInputSatName_Type(DisplayString):
    """Custom type activeInputSatName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ActiveInputSatName_Type.__name__ = "DisplayString"
_ActiveInputSatName_Object = MibTableColumn
activeInputSatName = _ActiveInputSatName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 2, 1, 12),
    _ActiveInputSatName_Type()
)
activeInputSatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeInputSatName.setStatus("current")


class _ActiveInputLastLNBConfig_Type(Integer32):
    """Custom type activeInputLastLNBConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ActiveInputLastLNBConfig_Type.__name__ = "Integer32"
_ActiveInputLastLNBConfig_Object = MibTableColumn
activeInputLastLNBConfig = _ActiveInputLastLNBConfig_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 2, 1, 13),
    _ActiveInputLastLNBConfig_Type()
)
activeInputLastLNBConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeInputLastLNBConfig.setStatus("current")


class _ActiveInputDiSeqCEnable_Type(Integer32):
    """Custom type activeInputDiSeqCEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ActiveInputDiSeqCEnable_Type.__name__ = "Integer32"
_ActiveInputDiSeqCEnable_Object = MibTableColumn
activeInputDiSeqCEnable = _ActiveInputDiSeqCEnable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 2, 1, 14),
    _ActiveInputDiSeqCEnable_Type()
)
activeInputDiSeqCEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeInputDiSeqCEnable.setStatus("current")


class _ActiveInputDiSeqCSwitch_Type(Integer32):
    """Custom type activeInputDiSeqCSwitch based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("a", 2),
          ("b", 3),
          ("c", 4),
          ("d", 5),
          ("e", 6),
          ("f", 7),
          ("g", 8),
          ("h", 9),
          ("i", 10),
          ("j", 11),
          ("k", 12),
          ("l", 13),
          ("m", 14),
          ("n", 15),
          ("o", 16),
          ("off", 1),
          ("p", 17))
    )


_ActiveInputDiSeqCSwitch_Type.__name__ = "Integer32"
_ActiveInputDiSeqCSwitch_Object = MibTableColumn
activeInputDiSeqCSwitch = _ActiveInputDiSeqCSwitch_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 2, 1, 15),
    _ActiveInputDiSeqCSwitch_Type()
)
activeInputDiSeqCSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeInputDiSeqCSwitch.setStatus("current")
_LnbPowerTable_Object = MibTable
lnbPowerTable = _LnbPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 3)
)
if mibBuilder.loadTexts:
    lnbPowerTable.setStatus("current")
_LnbPowerEntry_Object = MibTableRow
lnbPowerEntry = _LnbPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 3, 1)
)
lnbPowerEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-TUNING-MIB", "lnbPowerIndex"),
)
if mibBuilder.loadTexts:
    lnbPowerEntry.setStatus("current")


class _LnbPowerIndex_Type(Integer32):
    """Custom type lnbPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_LnbPowerIndex_Type.__name__ = "Integer32"
_LnbPowerIndex_Object = MibTableColumn
lnbPowerIndex = _LnbPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 3, 1, 1),
    _LnbPowerIndex_Type()
)
lnbPowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lnbPowerIndex.setStatus("current")


class _LnbPowerInput_Type(Integer32):
    """Custom type lnbPowerInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 255),
          ("rf1", 2),
          ("rf2", 3),
          ("rf3", 4),
          ("rf4", 5))
    )


_LnbPowerInput_Type.__name__ = "Integer32"
_LnbPowerInput_Object = MibTableColumn
lnbPowerInput = _LnbPowerInput_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 3, 1, 2),
    _LnbPowerInput_Type()
)
lnbPowerInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lnbPowerInput.setStatus("current")


class _LnbPowerControl_Type(Integer32):
    """Custom type lnbPowerControl based on Integer32"""
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
        *(("eighteenH", 3),
          ("hNIT", 4),
          ("off", 1),
          ("thirteenV", 2),
          ("vNIT", 5))
    )


_LnbPowerControl_Type.__name__ = "Integer32"
_LnbPowerControl_Object = MibTableColumn
lnbPowerControl = _LnbPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 3, 1, 3),
    _LnbPowerControl_Type()
)
lnbPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lnbPowerControl.setStatus("current")


class _LnbPowerStatus_Type(Integer32):
    """Custom type lnbPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 7),
          ("noLoad", 3),
          ("normal", 2),
          ("notApplicable", 1),
          ("overLoad", 5),
          ("overTemperature", 4),
          ("shortCircuit", 6))
    )


_LnbPowerStatus_Type.__name__ = "Integer32"
_LnbPowerStatus_Object = MibTableColumn
lnbPowerStatus = _LnbPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 2, 3, 1, 4),
    _LnbPowerStatus_Type()
)
lnbPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnbPowerStatus.setStatus("current")
_TuningStatusTable_ObjectIdentity = ObjectIdentity
tuningStatusTable = _TuningStatusTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3)
)
_SatSignalTable_Object = MibTable
satSignalTable = _SatSignalTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1)
)
if mibBuilder.loadTexts:
    satSignalTable.setStatus("current")
_SatSignalEntry_Object = MibTableRow
satSignalEntry = _SatSignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1)
)
satSignalEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-TUNING-MIB", "satSignalIndex"),
)
if mibBuilder.loadTexts:
    satSignalEntry.setStatus("current")


class _SatSignalIndex_Type(Integer32):
    """Custom type satSignalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SatSignalIndex_Type.__name__ = "Integer32"
_SatSignalIndex_Object = MibTableColumn
satSignalIndex = _SatSignalIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 1),
    _SatSignalIndex_Type()
)
satSignalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    satSignalIndex.setStatus("current")


class _SatSignalPvBer_Type(DisplayString):
    """Custom type satSignalPvBer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SatSignalPvBer_Type.__name__ = "DisplayString"
_SatSignalPvBer_Object = MibTableColumn
satSignalPvBer = _SatSignalPvBer_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 2),
    _SatSignalPvBer_Type()
)
satSignalPvBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalPvBer.setStatus("current")


class _SatSignalQPSKBer_Type(DisplayString):
    """Custom type satSignalQPSKBer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SatSignalQPSKBer_Type.__name__ = "DisplayString"
_SatSignalQPSKBer_Object = MibTableColumn
satSignalQPSKBer = _SatSignalQPSKBer_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 3),
    _SatSignalQPSKBer_Type()
)
satSignalQPSKBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalQPSKBer.setStatus("current")


class _SatSignalLdpCber_Type(DisplayString):
    """Custom type satSignalLdpCber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SatSignalLdpCber_Type.__name__ = "DisplayString"
_SatSignalLdpCber_Object = MibTableColumn
satSignalLdpCber = _SatSignalLdpCber_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 4),
    _SatSignalLdpCber_Type()
)
satSignalLdpCber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalLdpCber.setStatus("current")


class _SatSignalCndisp_Type(DisplayString):
    """Custom type satSignalCndisp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SatSignalCndisp_Type.__name__ = "DisplayString"
_SatSignalCndisp_Object = MibTableColumn
satSignalCndisp = _SatSignalCndisp_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 5),
    _SatSignalCndisp_Type()
)
satSignalCndisp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalCndisp.setStatus("current")


class _SatSignalCnMargin_Type(DisplayString):
    """Custom type satSignalCnMargin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SatSignalCnMargin_Type.__name__ = "DisplayString"
_SatSignalCnMargin_Object = MibTableColumn
satSignalCnMargin = _SatSignalCnMargin_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 6),
    _SatSignalCnMargin_Type()
)
satSignalCnMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalCnMargin.setStatus("current")


class _SatSignalLevel_Type(DisplayString):
    """Custom type satSignalLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SatSignalLevel_Type.__name__ = "DisplayString"
_SatSignalLevel_Object = MibTableColumn
satSignalLevel = _SatSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 7),
    _SatSignalLevel_Type()
)
satSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalLevel.setStatus("current")


class _SatSignalSatDishCnMargin_Type(DisplayString):
    """Custom type satSignalSatDishCnMargin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SatSignalSatDishCnMargin_Type.__name__ = "DisplayString"
_SatSignalSatDishCnMargin_Object = MibTableColumn
satSignalSatDishCnMargin = _SatSignalSatDishCnMargin_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 8),
    _SatSignalSatDishCnMargin_Type()
)
satSignalSatDishCnMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalSatDishCnMargin.setStatus("current")


class _SatSignalSatDishSigLevel_Type(DisplayString):
    """Custom type satSignalSatDishSigLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SatSignalSatDishSigLevel_Type.__name__ = "DisplayString"
_SatSignalSatDishSigLevel_Object = MibTableColumn
satSignalSatDishSigLevel = _SatSignalSatDishSigLevel_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 9),
    _SatSignalSatDishSigLevel_Type()
)
satSignalSatDishSigLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalSatDishSigLevel.setStatus("current")


class _SatSignalPerDisp_Type(DisplayString):
    """Custom type satSignalPerDisp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SatSignalPerDisp_Type.__name__ = "DisplayString"
_SatSignalPerDisp_Object = MibTableColumn
satSignalPerDisp = _SatSignalPerDisp_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 10),
    _SatSignalPerDisp_Type()
)
satSignalPerDisp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalPerDisp.setStatus("current")


class _SatSignalAfc_Type(DisplayString):
    """Custom type satSignalAfc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SatSignalAfc_Type.__name__ = "DisplayString"
_SatSignalAfc_Object = MibTableColumn
satSignalAfc = _SatSignalAfc_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 11),
    _SatSignalAfc_Type()
)
satSignalAfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalAfc.setStatus("current")


class _SatSignalUncorErrCnt_Type(DisplayString):
    """Custom type satSignalUncorErrCnt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SatSignalUncorErrCnt_Type.__name__ = "DisplayString"
_SatSignalUncorErrCnt_Object = MibTableColumn
satSignalUncorErrCnt = _SatSignalUncorErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 12),
    _SatSignalUncorErrCnt_Type()
)
satSignalUncorErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalUncorErrCnt.setStatus("current")


class _SatSignalCorErrCnt_Type(DisplayString):
    """Custom type satSignalCorErrCnt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SatSignalCorErrCnt_Type.__name__ = "DisplayString"
_SatSignalCorErrCnt_Object = MibTableColumn
satSignalCorErrCnt = _SatSignalCorErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 13),
    _SatSignalCorErrCnt_Type()
)
satSignalCorErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalCorErrCnt.setStatus("current")


class _SatSignalRfLock_Type(Integer32):
    """Custom type satSignalRfLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 2),
          ("noLock", 1))
    )


_SatSignalRfLock_Type.__name__ = "Integer32"
_SatSignalRfLock_Object = MibTableColumn
satSignalRfLock = _SatSignalRfLock_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 14),
    _SatSignalRfLock_Type()
)
satSignalRfLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalRfLock.setStatus("current")


class _SatSignalDnLkFreq_Type(DisplayString):
    """Custom type satSignalDnLkFreq based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SatSignalDnLkFreq_Type.__name__ = "DisplayString"
_SatSignalDnLkFreq_Object = MibTableColumn
satSignalDnLkFreq = _SatSignalDnLkFreq_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 15),
    _SatSignalDnLkFreq_Type()
)
satSignalDnLkFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalDnLkFreq.setStatus("current")


class _SatSignalLbandFreq_Type(DisplayString):
    """Custom type satSignalLbandFreq based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SatSignalLbandFreq_Type.__name__ = "DisplayString"
_SatSignalLbandFreq_Object = MibTableColumn
satSignalLbandFreq = _SatSignalLbandFreq_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 16),
    _SatSignalLbandFreq_Type()
)
satSignalLbandFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalLbandFreq.setStatus("current")


class _SatSignalSymbolRate_Type(DisplayString):
    """Custom type satSignalSymbolRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SatSignalSymbolRate_Type.__name__ = "DisplayString"
_SatSignalSymbolRate_Object = MibTableColumn
satSignalSymbolRate = _SatSignalSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 17),
    _SatSignalSymbolRate_Type()
)
satSignalSymbolRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalSymbolRate.setStatus("current")


class _SatSignalFecRate_Type(Integer32):
    """Custom type satSignalFecRate based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("auto", 11),
          ("eightNinth", 9),
          ("fiveSixth", 7),
          ("fourFifth", 6),
          ("half", 2),
          ("nineTenth", 10),
          ("notApplicable", 1),
          ("sevenEight", 8),
          ("threeFifth", 3),
          ("threeQuater", 5),
          ("twoThird", 4))
    )


_SatSignalFecRate_Type.__name__ = "Integer32"
_SatSignalFecRate_Object = MibTableColumn
satSignalFecRate = _SatSignalFecRate_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 18),
    _SatSignalFecRate_Type()
)
satSignalFecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalFecRate.setStatus("current")


class _SatSignalPolarization_Type(Integer32):
    """Custom type satSignalPolarization based on Integer32"""
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
        *(("auto", 5),
          ("horizontal", 1),
          ("leftCircular", 3),
          ("rightCircular", 4),
          ("vertical", 2))
    )


_SatSignalPolarization_Type.__name__ = "Integer32"
_SatSignalPolarization_Object = MibTableColumn
satSignalPolarization = _SatSignalPolarization_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 19),
    _SatSignalPolarization_Type()
)
satSignalPolarization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalPolarization.setStatus("current")


class _SatSignalModulation_Type(Integer32):
    """Custom type satSignalModulation based on Integer32"""
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
        *(("eightPskDvbs2", 4),
          ("notApplicable", 1),
          ("qpskDvbs", 2),
          ("qpskDvbs2", 3),
          ("sixteenQamDvbs2", 5))
    )


_SatSignalModulation_Type.__name__ = "Integer32"
_SatSignalModulation_Object = MibTableColumn
satSignalModulation = _SatSignalModulation_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 20),
    _SatSignalModulation_Type()
)
satSignalModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalModulation.setStatus("current")


class _SatSignalIQ_Type(Integer32):
    """Custom type satSignalIQ based on Integer32"""
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
        *(("auto", 3),
          ("inverted", 1),
          ("nonlnverted", 2),
          ("notApplicable", 4))
    )


_SatSignalIQ_Type.__name__ = "Integer32"
_SatSignalIQ_Object = MibTableColumn
satSignalIQ = _SatSignalIQ_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 21),
    _SatSignalIQ_Type()
)
satSignalIQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalIQ.setStatus("current")


class _SatSignalLnbPsStatus_Type(Integer32):
    """Custom type satSignalLnbPsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 7),
          ("noLoad", 3),
          ("normal", 2),
          ("notApplicable", 1),
          ("overLoad", 5),
          ("overTemperature", 4),
          ("shortCircuit", 6))
    )


_SatSignalLnbPsStatus_Type.__name__ = "Integer32"
_SatSignalLnbPsStatus_Object = MibTableColumn
satSignalLnbPsStatus = _SatSignalLnbPsStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 22),
    _SatSignalLnbPsStatus_Type()
)
satSignalLnbPsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalLnbPsStatus.setStatus("current")


class _SatSignalPilots_Type(Integer32):
    """Custom type satSignalPilots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("notApplicable", 3),
          ("yes", 2))
    )


_SatSignalPilots_Type.__name__ = "Integer32"
_SatSignalPilots_Object = MibTableColumn
satSignalPilots = _SatSignalPilots_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 23),
    _SatSignalPilots_Type()
)
satSignalPilots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalPilots.setStatus("current")


class _SatSignalLoSelect_Type(Integer32):
    """Custom type satSignalLoSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("off", 1),
          ("on", 2))
    )


_SatSignalLoSelect_Type.__name__ = "Integer32"
_SatSignalLoSelect_Object = MibTableColumn
satSignalLoSelect = _SatSignalLoSelect_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 24),
    _SatSignalLoSelect_Type()
)
satSignalLoSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalLoSelect.setStatus("current")


class _SatSignalPolar_Type(Integer32):
    """Custom type satSignalPolar based on Integer32"""
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
        *(("auto", 5),
          ("horizontal", 1),
          ("leftCircular", 3),
          ("rightCircular", 4),
          ("vertical", 2))
    )


_SatSignalPolar_Type.__name__ = "Integer32"
_SatSignalPolar_Object = MibTableColumn
satSignalPolar = _SatSignalPolar_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 25),
    _SatSignalPolar_Type()
)
satSignalPolar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalPolar.setStatus("current")


class _SatSignalClearSigErrCnt_Type(Integer32):
    """Custom type satSignalClearSigErrCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("writeOnly", 1),
          ("yes", 2))
    )


_SatSignalClearSigErrCnt_Type.__name__ = "Integer32"
_SatSignalClearSigErrCnt_Object = MibTableColumn
satSignalClearSigErrCnt = _SatSignalClearSigErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 26),
    _SatSignalClearSigErrCnt_Type()
)
satSignalClearSigErrCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satSignalClearSigErrCnt.setStatus("current")


class _SatSignalValidateOrbPosDate_Type(DisplayString):
    """Custom type satSignalValidateOrbPosDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SatSignalValidateOrbPosDate_Type.__name__ = "DisplayString"
_SatSignalValidateOrbPosDate_Object = MibTableColumn
satSignalValidateOrbPosDate = _SatSignalValidateOrbPosDate_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 27),
    _SatSignalValidateOrbPosDate_Type()
)
satSignalValidateOrbPosDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalValidateOrbPosDate.setStatus("current")


class _SatSignalValidateOrbPosStat_Type(DisplayString):
    """Custom type satSignalValidateOrbPosStat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SatSignalValidateOrbPosStat_Type.__name__ = "DisplayString"
_SatSignalValidateOrbPosStat_Object = MibTableColumn
satSignalValidateOrbPosStat = _SatSignalValidateOrbPosStat_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 28),
    _SatSignalValidateOrbPosStat_Type()
)
satSignalValidateOrbPosStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalValidateOrbPosStat.setStatus("current")


class _SatSignalChScanStatus_Type(Integer32):
    """Custom type satSignalChScanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("done", 3),
          ("off", 1),
          ("scanning", 2))
    )


_SatSignalChScanStatus_Type.__name__ = "Integer32"
_SatSignalChScanStatus_Object = MibTableColumn
satSignalChScanStatus = _SatSignalChScanStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 29),
    _SatSignalChScanStatus_Type()
)
satSignalChScanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalChScanStatus.setStatus("current")


class _SatSignalSigLevelRaw_Type(DisplayString):
    """Custom type satSignalSigLevelRaw based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_SatSignalSigLevelRaw_Type.__name__ = "DisplayString"
_SatSignalSigLevelRaw_Object = MibTableColumn
satSignalSigLevelRaw = _SatSignalSigLevelRaw_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 30),
    _SatSignalSigLevelRaw_Type()
)
satSignalSigLevelRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalSigLevelRaw.setStatus("current")


class _SatSignalP1DStatus_Type(DisplayString):
    """Custom type satSignalP1DStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_SatSignalP1DStatus_Type.__name__ = "DisplayString"
_SatSignalP1DStatus_Object = MibTableColumn
satSignalP1DStatus = _SatSignalP1DStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 31),
    _SatSignalP1DStatus_Type()
)
satSignalP1DStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalP1DStatus.setStatus("current")


class _SatSignalDvbS2FrameLen_Type(Integer32):
    """Custom type satSignalDvbS2FrameLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("longFrame", 2),
          ("notApplicable", 3),
          ("shortFrame", 1))
    )


_SatSignalDvbS2FrameLen_Type.__name__ = "Integer32"
_SatSignalDvbS2FrameLen_Object = MibTableColumn
satSignalDvbS2FrameLen = _SatSignalDvbS2FrameLen_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 32),
    _SatSignalDvbS2FrameLen_Type()
)
satSignalDvbS2FrameLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalDvbS2FrameLen.setStatus("current")


class _SatSignalCnMarginRaw_Type(DisplayString):
    """Custom type satSignalCnMarginRaw based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SatSignalCnMarginRaw_Type.__name__ = "DisplayString"
_SatSignalCnMarginRaw_Object = MibTableColumn
satSignalCnMarginRaw = _SatSignalCnMarginRaw_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 33),
    _SatSignalCnMarginRaw_Type()
)
satSignalCnMarginRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalCnMarginRaw.setStatus("current")


class _SatSignalDvbSQpskErrCount_Type(DisplayString):
    """Custom type satSignalDvbSQpskErrCount based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SatSignalDvbSQpskErrCount_Type.__name__ = "DisplayString"
_SatSignalDvbSQpskErrCount_Object = MibTableColumn
satSignalDvbSQpskErrCount = _SatSignalDvbSQpskErrCount_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 34),
    _SatSignalDvbSQpskErrCount_Type()
)
satSignalDvbSQpskErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalDvbSQpskErrCount.setStatus("current")


class _SatSignalDvbS2LdpcErrCount_Type(DisplayString):
    """Custom type satSignalDvbS2LdpcErrCount based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SatSignalDvbS2LdpcErrCount_Type.__name__ = "DisplayString"
_SatSignalDvbS2LdpcErrCount_Object = MibTableColumn
satSignalDvbS2LdpcErrCount = _SatSignalDvbS2LdpcErrCount_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 35),
    _SatSignalDvbS2LdpcErrCount_Type()
)
satSignalDvbS2LdpcErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalDvbS2LdpcErrCount.setStatus("current")


class _SatSignalPvErrCount_Type(DisplayString):
    """Custom type satSignalPvErrCount based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SatSignalPvErrCount_Type.__name__ = "DisplayString"
_SatSignalPvErrCount_Object = MibTableColumn
satSignalPvErrCount = _SatSignalPvErrCount_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 36),
    _SatSignalPvErrCount_Type()
)
satSignalPvErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalPvErrCount.setStatus("current")


class _SatSignalFecSyncStatus_Type(Integer32):
    """Custom type satSignalFecSyncStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SatSignalFecSyncStatus_Type.__name__ = "Integer32"
_SatSignalFecSyncStatus_Object = MibTableColumn
satSignalFecSyncStatus = _SatSignalFecSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 37),
    _SatSignalFecSyncStatus_Type()
)
satSignalFecSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalFecSyncStatus.setStatus("current")


class _SatSignalPktErrCount_Type(DisplayString):
    """Custom type satSignalPktErrCount based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SatSignalPktErrCount_Type.__name__ = "DisplayString"
_SatSignalPktErrCount_Object = MibTableColumn
satSignalPktErrCount = _SatSignalPktErrCount_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 1, 1, 38),
    _SatSignalPktErrCount_Type()
)
satSignalPktErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satSignalPktErrCount.setStatus("current")
_InputStatusTable_Object = MibTable
inputStatusTable = _InputStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 2)
)
if mibBuilder.loadTexts:
    inputStatusTable.setStatus("current")
_InputStatusEntry_Object = MibTableRow
inputStatusEntry = _InputStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 2, 1)
)
inputStatusEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-TUNING-MIB", "inputStatusIndex"),
)
if mibBuilder.loadTexts:
    inputStatusEntry.setStatus("current")


class _InputStatusIndex_Type(Integer32):
    """Custom type inputStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_InputStatusIndex_Type.__name__ = "Integer32"
_InputStatusIndex_Object = MibTableColumn
inputStatusIndex = _InputStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 2, 1, 1),
    _InputStatusIndex_Type()
)
inputStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inputStatusIndex.setStatus("current")


class _InputStatusCurInput_Type(Integer32):
    """Custom type inputStatusCurInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("rf", 1)
    )


_InputStatusCurInput_Type.__name__ = "Integer32"
_InputStatusCurInput_Object = MibTableColumn
inputStatusCurInput = _InputStatusCurInput_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 2, 1, 2),
    _InputStatusCurInput_Type()
)
inputStatusCurInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputStatusCurInput.setStatus("current")


class _InputStatusSatLock_Type(Integer32):
    """Custom type inputStatusSatLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lockminussignal", 2),
          ("lockplussignal", 3),
          ("nolock", 1))
    )


_InputStatusSatLock_Type.__name__ = "Integer32"
_InputStatusSatLock_Object = MibTableColumn
inputStatusSatLock = _InputStatusSatLock_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 2, 1, 3),
    _InputStatusSatLock_Type()
)
inputStatusSatLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputStatusSatLock.setStatus("current")


class _InputStatusMpgIpLock_Type(Integer32):
    """Custom type inputStatusMpgIpLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 2),
          ("nolock", 1))
    )


_InputStatusMpgIpLock_Type.__name__ = "Integer32"
_InputStatusMpgIpLock_Object = MibTableColumn
inputStatusMpgIpLock = _InputStatusMpgIpLock_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 2, 1, 4),
    _InputStatusMpgIpLock_Type()
)
inputStatusMpgIpLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputStatusMpgIpLock.setStatus("current")


class _InputStatusInputRate_Type(DisplayString):
    """Custom type inputStatusInputRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_InputStatusInputRate_Type.__name__ = "DisplayString"
_InputStatusInputRate_Object = MibTableColumn
inputStatusInputRate = _InputStatusInputRate_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 2, 1, 5),
    _InputStatusInputRate_Type()
)
inputStatusInputRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputStatusInputRate.setStatus("current")


class _InputStatusNetworkName_Type(DisplayString):
    """Custom type inputStatusNetworkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_InputStatusNetworkName_Type.__name__ = "DisplayString"
_InputStatusNetworkName_Object = MibTableColumn
inputStatusNetworkName = _InputStatusNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 2, 1, 6),
    _InputStatusNetworkName_Type()
)
inputStatusNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputStatusNetworkName.setStatus("current")


class _InputStatusNetworkId_Type(DisplayString):
    """Custom type inputStatusNetworkId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_InputStatusNetworkId_Type.__name__ = "DisplayString"
_InputStatusNetworkId_Object = MibTableColumn
inputStatusNetworkId = _InputStatusNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 2, 1, 7),
    _InputStatusNetworkId_Type()
)
inputStatusNetworkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputStatusNetworkId.setStatus("current")


class _InputStatusTransportId_Type(DisplayString):
    """Custom type inputStatusTransportId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_InputStatusTransportId_Type.__name__ = "DisplayString"
_InputStatusTransportId_Object = MibTableColumn
inputStatusTransportId = _InputStatusTransportId_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 2, 1, 8),
    _InputStatusTransportId_Type()
)
inputStatusTransportId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputStatusTransportId.setStatus("current")


class _InputStatusScramblingMode_Type(Integer32):
    """Custom type inputStatusScramblingMode based on Integer32"""
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
        *(("biss1", 4),
          ("biss2", 5),
          ("biss3", 6),
          ("des", 2),
          ("dvb", 3),
          ("unknown", 1))
    )


_InputStatusScramblingMode_Type.__name__ = "Integer32"
_InputStatusScramblingMode_Object = MibTableColumn
inputStatusScramblingMode = _InputStatusScramblingMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 2, 1, 9),
    _InputStatusScramblingMode_Type()
)
inputStatusScramblingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputStatusScramblingMode.setStatus("current")


class _InputStatusTransportError_Type(Integer32):
    """Custom type inputStatusTransportError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 3),
          ("notApplicable", 1),
          ("ok", 2))
    )


_InputStatusTransportError_Type.__name__ = "Integer32"
_InputStatusTransportError_Object = MibTableColumn
inputStatusTransportError = _InputStatusTransportError_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 2, 1, 10),
    _InputStatusTransportError_Type()
)
inputStatusTransportError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputStatusTransportError.setStatus("current")


class _InputStatusAsiLock_Type(Integer32):
    """Custom type inputStatusAsiLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 2),
          ("nolock", 1))
    )


_InputStatusAsiLock_Type.__name__ = "Integer32"
_InputStatusAsiLock_Object = MibTableColumn
inputStatusAsiLock = _InputStatusAsiLock_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 2, 1, 11),
    _InputStatusAsiLock_Type()
)
inputStatusAsiLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputStatusAsiLock.setStatus("current")


class _InputStatusAsiLinkError_Type(Integer32):
    """Custom type inputStatusAsiLinkError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 3),
          ("notApplicable", 1),
          ("ok", 2))
    )


_InputStatusAsiLinkError_Type.__name__ = "Integer32"
_InputStatusAsiLinkError_Object = MibTableColumn
inputStatusAsiLinkError = _InputStatusAsiLinkError_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 2, 1, 12),
    _InputStatusAsiLinkError_Type()
)
inputStatusAsiLinkError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputStatusAsiLinkError.setStatus("current")


class _InputStatusAsiPacketSize_Type(Integer32):
    """Custom type inputStatusAsiPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("oneHundredAndEightyEight", 2),
          ("twoHundredAndFour", 3))
    )


_InputStatusAsiPacketSize_Type.__name__ = "Integer32"
_InputStatusAsiPacketSize_Object = MibTableColumn
inputStatusAsiPacketSize = _InputStatusAsiPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 2, 1, 13),
    _InputStatusAsiPacketSize_Type()
)
inputStatusAsiPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputStatusAsiPacketSize.setStatus("current")


class _InputStatusLastTuneReason_Type(DisplayString):
    """Custom type inputStatusLastTuneReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_InputStatusLastTuneReason_Type.__name__ = "DisplayString"
_InputStatusLastTuneReason_Object = MibTableColumn
inputStatusLastTuneReason = _InputStatusLastTuneReason_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 2, 1, 14),
    _InputStatusLastTuneReason_Type()
)
inputStatusLastTuneReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputStatusLastTuneReason.setStatus("current")


class _InputStatusCurD985xInput_Type(DisplayString):
    """Custom type inputStatusCurD985xInput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_InputStatusCurD985xInput_Type.__name__ = "DisplayString"
_InputStatusCurD985xInput_Object = MibTableColumn
inputStatusCurD985xInput = _InputStatusCurD985xInput_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 2, 1, 15),
    _InputStatusCurD985xInput_Type()
)
inputStatusCurD985xInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputStatusCurD985xInput.setStatus("current")


class _InputStatusIpiLinkStatus_Type(DisplayString):
    """Custom type inputStatusIpiLinkStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_InputStatusIpiLinkStatus_Type.__name__ = "DisplayString"
_InputStatusIpiLinkStatus_Object = MibTableColumn
inputStatusIpiLinkStatus = _InputStatusIpiLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 2, 1, 16),
    _InputStatusIpiLinkStatus_Type()
)
inputStatusIpiLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputStatusIpiLinkStatus.setStatus("current")


class _InputStatusIpiSignal_Type(DisplayString):
    """Custom type inputStatusIpiSignal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_InputStatusIpiSignal_Type.__name__ = "DisplayString"
_InputStatusIpiSignal_Object = MibTableColumn
inputStatusIpiSignal = _InputStatusIpiSignal_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 2, 1, 17),
    _InputStatusIpiSignal_Type()
)
inputStatusIpiSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputStatusIpiSignal.setStatus("current")


class _InputStatusIpiFecLock_Type(DisplayString):
    """Custom type inputStatusIpiFecLock based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_InputStatusIpiFecLock_Type.__name__ = "DisplayString"
_InputStatusIpiFecLock_Object = MibTableColumn
inputStatusIpiFecLock = _InputStatusIpiFecLock_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 2, 1, 18),
    _InputStatusIpiFecLock_Type()
)
inputStatusIpiFecLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputStatusIpiFecLock.setStatus("current")


class _InputStatusIpiPcrLock_Type(DisplayString):
    """Custom type inputStatusIpiPcrLock based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_InputStatusIpiPcrLock_Type.__name__ = "DisplayString"
_InputStatusIpiPcrLock_Object = MibTableColumn
inputStatusIpiPcrLock = _InputStatusIpiPcrLock_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 2, 1, 19),
    _InputStatusIpiPcrLock_Type()
)
inputStatusIpiPcrLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputStatusIpiPcrLock.setStatus("current")


class _InputStatusIpiDelLatency_Type(DisplayString):
    """Custom type inputStatusIpiDelLatency based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_InputStatusIpiDelLatency_Type.__name__ = "DisplayString"
_InputStatusIpiDelLatency_Object = MibTableColumn
inputStatusIpiDelLatency = _InputStatusIpiDelLatency_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 2, 1, 20),
    _InputStatusIpiDelLatency_Type()
)
inputStatusIpiDelLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputStatusIpiDelLatency.setStatus("current")
_InputStatusIpiData1SrcIP_Type = IpAddress
_InputStatusIpiData1SrcIP_Object = MibTableColumn
inputStatusIpiData1SrcIP = _InputStatusIpiData1SrcIP_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 2, 1, 21),
    _InputStatusIpiData1SrcIP_Type()
)
inputStatusIpiData1SrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputStatusIpiData1SrcIP.setStatus("current")
_InputStatusIpiData2SrcIP_Type = IpAddress
_InputStatusIpiData2SrcIP_Object = MibTableColumn
inputStatusIpiData2SrcIP = _InputStatusIpiData2SrcIP_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 2, 1, 22),
    _InputStatusIpiData2SrcIP_Type()
)
inputStatusIpiData2SrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputStatusIpiData2SrcIP.setStatus("current")


class _InputStatusIpiData1TsType_Type(DisplayString):
    """Custom type inputStatusIpiData1TsType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_InputStatusIpiData1TsType_Type.__name__ = "DisplayString"
_InputStatusIpiData1TsType_Object = MibTableColumn
inputStatusIpiData1TsType = _InputStatusIpiData1TsType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 2, 1, 23),
    _InputStatusIpiData1TsType_Type()
)
inputStatusIpiData1TsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputStatusIpiData1TsType.setStatus("current")


class _InputStatusIpiData2TsType_Type(DisplayString):
    """Custom type inputStatusIpiData2TsType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_InputStatusIpiData2TsType_Type.__name__ = "DisplayString"
_InputStatusIpiData2TsType_Object = MibTableColumn
inputStatusIpiData2TsType = _InputStatusIpiData2TsType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 3, 2, 1, 24),
    _InputStatusIpiData2TsType_Type()
)
inputStatusIpiData2TsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputStatusIpiData2TsType.setStatus("current")
_SiRcvTable_ObjectIdentity = ObjectIdentity
siRcvTable = _SiRcvTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4)
)
_SiRcvOptionTable_Object = MibTable
siRcvOptionTable = _SiRcvOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 1)
)
if mibBuilder.loadTexts:
    siRcvOptionTable.setStatus("current")
_SiRcvOptionEntry_Object = MibTableRow
siRcvOptionEntry = _SiRcvOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 1, 1)
)
siRcvOptionEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-TUNING-MIB", "siRcvOptionInstance"),
)
if mibBuilder.loadTexts:
    siRcvOptionEntry.setStatus("current")


class _SiRcvOptionInstance_Type(Integer32):
    """Custom type siRcvOptionInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SiRcvOptionInstance_Type.__name__ = "Integer32"
_SiRcvOptionInstance_Object = MibTableColumn
siRcvOptionInstance = _SiRcvOptionInstance_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 1, 1, 1),
    _SiRcvOptionInstance_Type()
)
siRcvOptionInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    siRcvOptionInstance.setStatus("current")


class _SiRcvOptionAcqMode_Type(Integer32):
    """Custom type siRcvOptionAcqMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("basic", 1),
          ("custom", 3))
    )


_SiRcvOptionAcqMode_Type.__name__ = "Integer32"
_SiRcvOptionAcqMode_Object = MibTableColumn
siRcvOptionAcqMode = _SiRcvOptionAcqMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 1, 1, 2),
    _SiRcvOptionAcqMode_Type()
)
siRcvOptionAcqMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siRcvOptionAcqMode.setStatus("current")


class _SiRcvOptionReacq_Type(Integer32):
    """Custom type siRcvOptionReacq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("writeOnly", 1),
          ("yes", 2))
    )


_SiRcvOptionReacq_Type.__name__ = "Integer32"
_SiRcvOptionReacq_Object = MibTableColumn
siRcvOptionReacq = _SiRcvOptionReacq_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 1, 1, 3),
    _SiRcvOptionReacq_Type()
)
siRcvOptionReacq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siRcvOptionReacq.setStatus("current")


class _SiRcvOptionNetID_Type(Integer32):
    """Custom type siRcvOptionNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SiRcvOptionNetID_Type.__name__ = "Integer32"
_SiRcvOptionNetID_Object = MibTableColumn
siRcvOptionNetID = _SiRcvOptionNetID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 1, 1, 4),
    _SiRcvOptionNetID_Type()
)
siRcvOptionNetID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siRcvOptionNetID.setStatus("current")


class _SiRcvOptionInputSel_Type(Integer32):
    """Custom type siRcvOptionInputSel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("swMap", 2),
          ("userCfg", 1))
    )


_SiRcvOptionInputSel_Type.__name__ = "Integer32"
_SiRcvOptionInputSel_Object = MibTableColumn
siRcvOptionInputSel = _SiRcvOptionInputSel_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 1, 1, 5),
    _SiRcvOptionInputSel_Type()
)
siRcvOptionInputSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siRcvOptionInputSel.setStatus("current")


class _SiRcvOptionFreqSel_Type(Integer32):
    """Custom type siRcvOptionFreqSel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nit", 1),
          ("userCfg", 2))
    )


_SiRcvOptionFreqSel_Type.__name__ = "Integer32"
_SiRcvOptionFreqSel_Object = MibTableColumn
siRcvOptionFreqSel = _SiRcvOptionFreqSel_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 1, 1, 6),
    _SiRcvOptionFreqSel_Type()
)
siRcvOptionFreqSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siRcvOptionFreqSel.setStatus("current")


class _SiRcvOptionServListMode_Type(Integer32):
    """Custom type siRcvOptionServListMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 2),
          ("rigorous", 1))
    )


_SiRcvOptionServListMode_Type.__name__ = "Integer32"
_SiRcvOptionServListMode_Object = MibTableColumn
siRcvOptionServListMode = _SiRcvOptionServListMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 1, 1, 7),
    _SiRcvOptionServListMode_Type()
)
siRcvOptionServListMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siRcvOptionServListMode.setStatus("current")


class _SiRcvOptionUseBAT_Type(Integer32):
    """Custom type siRcvOptionUseBAT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SiRcvOptionUseBAT_Type.__name__ = "Integer32"
_SiRcvOptionUseBAT_Object = MibTableColumn
siRcvOptionUseBAT = _SiRcvOptionUseBAT_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 1, 1, 8),
    _SiRcvOptionUseBAT_Type()
)
siRcvOptionUseBAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siRcvOptionUseBAT.setStatus("current")


class _SiRcvOptionUseNIT_Type(Integer32):
    """Custom type siRcvOptionUseNIT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SiRcvOptionUseNIT_Type.__name__ = "Integer32"
_SiRcvOptionUseNIT_Object = MibTableColumn
siRcvOptionUseNIT = _SiRcvOptionUseNIT_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 1, 1, 9),
    _SiRcvOptionUseNIT_Type()
)
siRcvOptionUseNIT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siRcvOptionUseNIT.setStatus("current")


class _SiRcvOptionUseSDT_Type(Integer32):
    """Custom type siRcvOptionUseSDT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SiRcvOptionUseSDT_Type.__name__ = "Integer32"
_SiRcvOptionUseSDT_Object = MibTableColumn
siRcvOptionUseSDT = _SiRcvOptionUseSDT_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 1, 1, 10),
    _SiRcvOptionUseSDT_Type()
)
siRcvOptionUseSDT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siRcvOptionUseSDT.setStatus("current")


class _SiRcvOptionUsePAT_Type(Integer32):
    """Custom type siRcvOptionUsePAT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SiRcvOptionUsePAT_Type.__name__ = "Integer32"
_SiRcvOptionUsePAT_Object = MibTableColumn
siRcvOptionUsePAT = _SiRcvOptionUsePAT_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 1, 1, 11),
    _SiRcvOptionUsePAT_Type()
)
siRcvOptionUsePAT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siRcvOptionUsePAT.setStatus("current")
_SiRcvOptionStatusTable_Object = MibTable
siRcvOptionStatusTable = _SiRcvOptionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 2)
)
if mibBuilder.loadTexts:
    siRcvOptionStatusTable.setStatus("current")
_SiRcvOptionStatusEntry_Object = MibTableRow
siRcvOptionStatusEntry = _SiRcvOptionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 2, 1)
)
siRcvOptionStatusEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-TUNING-MIB", "siRcvOptionStatusInstance"),
)
if mibBuilder.loadTexts:
    siRcvOptionStatusEntry.setStatus("current")


class _SiRcvOptionStatusInstance_Type(Integer32):
    """Custom type siRcvOptionStatusInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SiRcvOptionStatusInstance_Type.__name__ = "Integer32"
_SiRcvOptionStatusInstance_Object = MibTableColumn
siRcvOptionStatusInstance = _SiRcvOptionStatusInstance_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 2, 1, 1),
    _SiRcvOptionStatusInstance_Type()
)
siRcvOptionStatusInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    siRcvOptionStatusInstance.setStatus("current")


class _SiRcvOptionLastChanReas_Type(Integer32):
    """Custom type siRcvOptionLastChanReas based on Integer32"""
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
        *(("nit", 1),
          ("preset", 4),
          ("uplinkForceRetune", 2),
          ("userEntry", 3))
    )


_SiRcvOptionLastChanReas_Type.__name__ = "Integer32"
_SiRcvOptionLastChanReas_Object = MibTableColumn
siRcvOptionLastChanReas = _SiRcvOptionLastChanReas_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 2, 1, 2),
    _SiRcvOptionLastChanReas_Type()
)
siRcvOptionLastChanReas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siRcvOptionLastChanReas.setStatus("current")


class _SiRcvOptionLastActivated_Type(DisplayString):
    """Custom type siRcvOptionLastActivated based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SiRcvOptionLastActivated_Type.__name__ = "DisplayString"
_SiRcvOptionLastActivated_Object = MibTableColumn
siRcvOptionLastActivated = _SiRcvOptionLastActivated_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 2, 1, 3),
    _SiRcvOptionLastActivated_Type()
)
siRcvOptionLastActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siRcvOptionLastActivated.setStatus("current")


class _SiRcvOptionStatusFreqSel_Type(Integer32):
    """Custom type siRcvOptionStatusFreqSel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nit", 1),
          ("userCfg", 2))
    )


_SiRcvOptionStatusFreqSel_Type.__name__ = "Integer32"
_SiRcvOptionStatusFreqSel_Object = MibTableColumn
siRcvOptionStatusFreqSel = _SiRcvOptionStatusFreqSel_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 2, 1, 4),
    _SiRcvOptionStatusFreqSel_Type()
)
siRcvOptionStatusFreqSel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siRcvOptionStatusFreqSel.setStatus("current")


class _SiRcvOptionStatusServListMode_Type(Integer32):
    """Custom type siRcvOptionStatusServListMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 2),
          ("rigorous", 1))
    )


_SiRcvOptionStatusServListMode_Type.__name__ = "Integer32"
_SiRcvOptionStatusServListMode_Object = MibTableColumn
siRcvOptionStatusServListMode = _SiRcvOptionStatusServListMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 2, 1, 5),
    _SiRcvOptionStatusServListMode_Type()
)
siRcvOptionStatusServListMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siRcvOptionStatusServListMode.setStatus("current")


class _SiRcvOptionStatusUseBAT_Type(Integer32):
    """Custom type siRcvOptionStatusUseBAT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SiRcvOptionStatusUseBAT_Type.__name__ = "Integer32"
_SiRcvOptionStatusUseBAT_Object = MibTableColumn
siRcvOptionStatusUseBAT = _SiRcvOptionStatusUseBAT_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 2, 1, 6),
    _SiRcvOptionStatusUseBAT_Type()
)
siRcvOptionStatusUseBAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siRcvOptionStatusUseBAT.setStatus("current")


class _SiRcvOptionStatusUseNIT_Type(Integer32):
    """Custom type siRcvOptionStatusUseNIT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SiRcvOptionStatusUseNIT_Type.__name__ = "Integer32"
_SiRcvOptionStatusUseNIT_Object = MibTableColumn
siRcvOptionStatusUseNIT = _SiRcvOptionStatusUseNIT_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 2, 1, 7),
    _SiRcvOptionStatusUseNIT_Type()
)
siRcvOptionStatusUseNIT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siRcvOptionStatusUseNIT.setStatus("current")


class _SiRcvOptionStatusUseSDT_Type(Integer32):
    """Custom type siRcvOptionStatusUseSDT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SiRcvOptionStatusUseSDT_Type.__name__ = "Integer32"
_SiRcvOptionStatusUseSDT_Object = MibTableColumn
siRcvOptionStatusUseSDT = _SiRcvOptionStatusUseSDT_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 2, 1, 8),
    _SiRcvOptionStatusUseSDT_Type()
)
siRcvOptionStatusUseSDT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siRcvOptionStatusUseSDT.setStatus("current")


class _SiRcvOptionStatusUsePAT_Type(Integer32):
    """Custom type siRcvOptionStatusUsePAT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SiRcvOptionStatusUsePAT_Type.__name__ = "Integer32"
_SiRcvOptionStatusUsePAT_Object = MibTableColumn
siRcvOptionStatusUsePAT = _SiRcvOptionStatusUsePAT_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 2, 1, 9),
    _SiRcvOptionStatusUsePAT_Type()
)
siRcvOptionStatusUsePAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siRcvOptionStatusUsePAT.setStatus("current")
_SiInfoRxTable_Object = MibTable
siInfoRxTable = _SiInfoRxTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 3)
)
if mibBuilder.loadTexts:
    siInfoRxTable.setStatus("current")
_SiInfoRxEntry_Object = MibTableRow
siInfoRxEntry = _SiInfoRxEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 3, 1)
)
siInfoRxEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-TUNING-MIB", "siInfoRxInstance"),
    (0, "CISCO-DMN-DSG-TUNING-MIB", "siInfoRxIdx"),
)
if mibBuilder.loadTexts:
    siInfoRxEntry.setStatus("current")


class _SiInfoRxInstance_Type(Integer32):
    """Custom type siInfoRxInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SiInfoRxInstance_Type.__name__ = "Integer32"
_SiInfoRxInstance_Object = MibTableColumn
siInfoRxInstance = _SiInfoRxInstance_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 3, 1, 1),
    _SiInfoRxInstance_Type()
)
siInfoRxInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    siInfoRxInstance.setStatus("current")


class _SiInfoRxIdx_Type(Integer32):
    """Custom type siInfoRxIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SiInfoRxIdx_Type.__name__ = "Integer32"
_SiInfoRxIdx_Object = MibTableColumn
siInfoRxIdx = _SiInfoRxIdx_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 3, 1, 2),
    _SiInfoRxIdx_Type()
)
siInfoRxIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    siInfoRxIdx.setStatus("current")


class _SiInfoRxType_Type(Integer32):
    """Custom type siInfoRxType based on Integer32"""
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
              32)
        )
    )
    namedValues = NamedValues(
        *(("aeitES0", 12),
          ("aeitES1", 13),
          ("aeitpf", 10),
          ("bat", 9),
          ("cat", 2),
          ("cdt", 27),
          ("dit", 19),
          ("dpi", 25),
          ("drt", 26),
          ("ecmeven", 22),
          ("ecmodd", 21),
          ("ect", 31),
          ("emm", 23),
          ("invalidtableid", 32),
          ("mat", 29),
          ("mct", 28),
          ("mit", 30),
          ("mpe", 24),
          ("nit", 5),
          ("nitother", 6),
          ("oeitES", 14),
          ("oeitpf", 11),
          ("pat", 1),
          ("pmt", 3),
          ("rst", 16),
          ("sdt", 7),
          ("sdtother", 8),
          ("sit", 20),
          ("st", 17),
          ("tdt", 15),
          ("tot", 18),
          ("tsdt", 4))
    )


_SiInfoRxType_Type.__name__ = "Integer32"
_SiInfoRxType_Object = MibTableColumn
siInfoRxType = _SiInfoRxType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 3, 1, 3),
    _SiInfoRxType_Type()
)
siInfoRxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siInfoRxType.setStatus("current")


class _SiInfoRxIDExt_Type(DisplayString):
    """Custom type siInfoRxIDExt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SiInfoRxIDExt_Type.__name__ = "DisplayString"
_SiInfoRxIDExt_Object = MibTableColumn
siInfoRxIDExt = _SiInfoRxIDExt_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 3, 1, 4),
    _SiInfoRxIDExt_Type()
)
siInfoRxIDExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siInfoRxIDExt.setStatus("current")


class _SiInfoRxUid_Type(DisplayString):
    """Custom type siInfoRxUid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SiInfoRxUid_Type.__name__ = "DisplayString"
_SiInfoRxUid_Object = MibTableColumn
siInfoRxUid = _SiInfoRxUid_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 3, 1, 5),
    _SiInfoRxUid_Type()
)
siInfoRxUid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siInfoRxUid.setStatus("current")


class _SiInfoRxStatus_Type(Integer32):
    """Custom type siInfoRxStatus based on Integer32"""
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
        *(("full", 3),
          ("lost", 6),
          ("none", 1),
          ("partial", 2),
          ("timeout", 5),
          ("update", 4))
    )


_SiInfoRxStatus_Type.__name__ = "Integer32"
_SiInfoRxStatus_Object = MibTableColumn
siInfoRxStatus = _SiInfoRxStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 3, 1, 6),
    _SiInfoRxStatus_Type()
)
siInfoRxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siInfoRxStatus.setStatus("current")


class _SiInfoRxVer_Type(DisplayString):
    """Custom type siInfoRxVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SiInfoRxVer_Type.__name__ = "DisplayString"
_SiInfoRxVer_Object = MibTableColumn
siInfoRxVer = _SiInfoRxVer_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 3, 1, 7),
    _SiInfoRxVer_Type()
)
siInfoRxVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siInfoRxVer.setStatus("current")


class _SiInfoRxPID_Type(DisplayString):
    """Custom type siInfoRxPID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SiInfoRxPID_Type.__name__ = "DisplayString"
_SiInfoRxPID_Object = MibTableColumn
siInfoRxPID = _SiInfoRxPID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 3, 1, 8),
    _SiInfoRxPID_Type()
)
siInfoRxPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siInfoRxPID.setStatus("current")


class _SiInfoRxSections_Type(DisplayString):
    """Custom type siInfoRxSections based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SiInfoRxSections_Type.__name__ = "DisplayString"
_SiInfoRxSections_Object = MibTableColumn
siInfoRxSections = _SiInfoRxSections_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 3, 1, 9),
    _SiInfoRxSections_Type()
)
siInfoRxSections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siInfoRxSections.setStatus("current")
_SiInfoTsTable_Object = MibTable
siInfoTsTable = _SiInfoTsTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 4)
)
if mibBuilder.loadTexts:
    siInfoTsTable.setStatus("current")
_SiInfoTsEntry_Object = MibTableRow
siInfoTsEntry = _SiInfoTsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 4, 1)
)
siInfoTsEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-TUNING-MIB", "siInfoTsInstance"),
    (0, "CISCO-DMN-DSG-TUNING-MIB", "siInfoTsIdx"),
)
if mibBuilder.loadTexts:
    siInfoTsEntry.setStatus("current")


class _SiInfoTsInstance_Type(Integer32):
    """Custom type siInfoTsInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SiInfoTsInstance_Type.__name__ = "Integer32"
_SiInfoTsInstance_Object = MibTableColumn
siInfoTsInstance = _SiInfoTsInstance_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 4, 1, 1),
    _SiInfoTsInstance_Type()
)
siInfoTsInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    siInfoTsInstance.setStatus("current")


class _SiInfoTsIdx_Type(Integer32):
    """Custom type siInfoTsIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SiInfoTsIdx_Type.__name__ = "Integer32"
_SiInfoTsIdx_Object = MibTableColumn
siInfoTsIdx = _SiInfoTsIdx_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 4, 1, 2),
    _SiInfoTsIdx_Type()
)
siInfoTsIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    siInfoTsIdx.setStatus("current")


class _SiInfoTsId_Type(DisplayString):
    """Custom type siInfoTsId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SiInfoTsId_Type.__name__ = "DisplayString"
_SiInfoTsId_Object = MibTableColumn
siInfoTsId = _SiInfoTsId_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 4, 1, 3),
    _SiInfoTsId_Type()
)
siInfoTsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siInfoTsId.setStatus("current")


class _SiInfoTsFreq_Type(DisplayString):
    """Custom type siInfoTsFreq based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SiInfoTsFreq_Type.__name__ = "DisplayString"
_SiInfoTsFreq_Object = MibTableColumn
siInfoTsFreq = _SiInfoTsFreq_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 4, 1, 4),
    _SiInfoTsFreq_Type()
)
siInfoTsFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siInfoTsFreq.setStatus("current")


class _SiInfoTsSymRate_Type(DisplayString):
    """Custom type siInfoTsSymRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SiInfoTsSymRate_Type.__name__ = "DisplayString"
_SiInfoTsSymRate_Object = MibTableColumn
siInfoTsSymRate = _SiInfoTsSymRate_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 4, 1, 5),
    _SiInfoTsSymRate_Type()
)
siInfoTsSymRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siInfoTsSymRate.setStatus("current")


class _SiInfoTsOrbPosn_Type(DisplayString):
    """Custom type siInfoTsOrbPosn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SiInfoTsOrbPosn_Type.__name__ = "DisplayString"
_SiInfoTsOrbPosn_Object = MibTableColumn
siInfoTsOrbPosn = _SiInfoTsOrbPosn_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 4, 1, 6),
    _SiInfoTsOrbPosn_Type()
)
siInfoTsOrbPosn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siInfoTsOrbPosn.setStatus("current")


class _SiInfoTsPolar_Type(Integer32):
    """Custom type siInfoTsPolar based on Integer32"""
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
        *(("auto", 5),
          ("horizontal", 1),
          ("leftCircular", 3),
          ("rightCircular", 4),
          ("vertical", 2))
    )


_SiInfoTsPolar_Type.__name__ = "Integer32"
_SiInfoTsPolar_Object = MibTableColumn
siInfoTsPolar = _SiInfoTsPolar_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 4, 1, 7),
    _SiInfoTsPolar_Type()
)
siInfoTsPolar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siInfoTsPolar.setStatus("current")


class _SiInfoTsFEC_Type(Integer32):
    """Custom type siInfoTsFEC based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("auto", 11),
          ("eightNinth", 9),
          ("fiveSixth", 7),
          ("fourFifth", 6),
          ("half", 2),
          ("nineTenth", 10),
          ("notApplicable", 1),
          ("sevenEighth", 8),
          ("threeFifth", 3),
          ("threeQuarter", 5),
          ("twoThird", 4))
    )


_SiInfoTsFEC_Type.__name__ = "Integer32"
_SiInfoTsFEC_Object = MibTableColumn
siInfoTsFEC = _SiInfoTsFEC_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 4, 1, 8),
    _SiInfoTsFEC_Type()
)
siInfoTsFEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siInfoTsFEC.setStatus("current")


class _SiInfoTsModulation_Type(Integer32):
    """Custom type siInfoTsModulation based on Integer32"""
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
        *(("eightPskDvbS2", 4),
          ("notapplicable", 1),
          ("qpskDvbS", 2),
          ("qpskDvbS2", 3),
          ("sixteenQamDvbsS2", 5))
    )


_SiInfoTsModulation_Type.__name__ = "Integer32"
_SiInfoTsModulation_Object = MibTableColumn
siInfoTsModulation = _SiInfoTsModulation_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 4, 1, 9),
    _SiInfoTsModulation_Type()
)
siInfoTsModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siInfoTsModulation.setStatus("current")


class _SiInfoTsOrgNetID_Type(DisplayString):
    """Custom type siInfoTsOrgNetID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SiInfoTsOrgNetID_Type.__name__ = "DisplayString"
_SiInfoTsOrgNetID_Object = MibTableColumn
siInfoTsOrgNetID = _SiInfoTsOrgNetID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 4, 1, 10),
    _SiInfoTsOrgNetID_Type()
)
siInfoTsOrgNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siInfoTsOrgNetID.setStatus("current")


class _SiInfoTsEastWestFlag_Type(Integer32):
    """Custom type siInfoTsEastWestFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("east", 1),
          ("notApplicable", 3),
          ("west", 2))
    )


_SiInfoTsEastWestFlag_Type.__name__ = "Integer32"
_SiInfoTsEastWestFlag_Object = MibTableColumn
siInfoTsEastWestFlag = _SiInfoTsEastWestFlag_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 4, 1, 11),
    _SiInfoTsEastWestFlag_Type()
)
siInfoTsEastWestFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siInfoTsEastWestFlag.setStatus("current")
_SiInfoVCInfoTable_Object = MibTable
siInfoVCInfoTable = _SiInfoVCInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 5)
)
if mibBuilder.loadTexts:
    siInfoVCInfoTable.setStatus("current")
_SiInfoVCInfoEntry_Object = MibTableRow
siInfoVCInfoEntry = _SiInfoVCInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 5, 1)
)
siInfoVCInfoEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-TUNING-MIB", "siInfoVCInfoInstance"),
    (0, "CISCO-DMN-DSG-TUNING-MIB", "siInfoVCInfoIdx"),
)
if mibBuilder.loadTexts:
    siInfoVCInfoEntry.setStatus("current")


class _SiInfoVCInfoInstance_Type(Integer32):
    """Custom type siInfoVCInfoInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SiInfoVCInfoInstance_Type.__name__ = "Integer32"
_SiInfoVCInfoInstance_Object = MibTableColumn
siInfoVCInfoInstance = _SiInfoVCInfoInstance_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 5, 1, 1),
    _SiInfoVCInfoInstance_Type()
)
siInfoVCInfoInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    siInfoVCInfoInstance.setStatus("current")


class _SiInfoVCInfoIdx_Type(Integer32):
    """Custom type siInfoVCInfoIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 262144),
    )


_SiInfoVCInfoIdx_Type.__name__ = "Integer32"
_SiInfoVCInfoIdx_Object = MibTableColumn
siInfoVCInfoIdx = _SiInfoVCInfoIdx_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 5, 1, 2),
    _SiInfoVCInfoIdx_Type()
)
siInfoVCInfoIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    siInfoVCInfoIdx.setStatus("current")


class _SiInfoVCInfoId_Type(DisplayString):
    """Custom type siInfoVCInfoId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SiInfoVCInfoId_Type.__name__ = "DisplayString"
_SiInfoVCInfoId_Object = MibTableColumn
siInfoVCInfoId = _SiInfoVCInfoId_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 5, 1, 3),
    _SiInfoVCInfoId_Type()
)
siInfoVCInfoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siInfoVCInfoId.setStatus("current")


class _SiInfoVCInfoTxID_Type(DisplayString):
    """Custom type siInfoVCInfoTxID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SiInfoVCInfoTxID_Type.__name__ = "DisplayString"
_SiInfoVCInfoTxID_Object = MibTableColumn
siInfoVCInfoTxID = _SiInfoVCInfoTxID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 5, 1, 4),
    _SiInfoVCInfoTxID_Type()
)
siInfoVCInfoTxID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siInfoVCInfoTxID.setStatus("current")


class _SiInfoVCInfoProgName_Type(DisplayString):
    """Custom type siInfoVCInfoProgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SiInfoVCInfoProgName_Type.__name__ = "DisplayString"
_SiInfoVCInfoProgName_Object = MibTableColumn
siInfoVCInfoProgName = _SiInfoVCInfoProgName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 5, 1, 5),
    _SiInfoVCInfoProgName_Type()
)
siInfoVCInfoProgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siInfoVCInfoProgName.setStatus("current")


class _SiInfoVCInfoPMTPID_Type(DisplayString):
    """Custom type siInfoVCInfoPMTPID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SiInfoVCInfoPMTPID_Type.__name__ = "DisplayString"
_SiInfoVCInfoPMTPID_Object = MibTableColumn
siInfoVCInfoPMTPID = _SiInfoVCInfoPMTPID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 5, 1, 6),
    _SiInfoVCInfoPMTPID_Type()
)
siInfoVCInfoPMTPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siInfoVCInfoPMTPID.setStatus("current")


class _SiInfoVCInfoCHType_Type(Integer32):
    """Custom type siInfoVCInfoCHType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 3),
          ("radio", 2),
          ("tv", 1))
    )


_SiInfoVCInfoCHType_Type.__name__ = "Integer32"
_SiInfoVCInfoCHType_Object = MibTableColumn
siInfoVCInfoCHType = _SiInfoVCInfoCHType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 5, 1, 7),
    _SiInfoVCInfoCHType_Type()
)
siInfoVCInfoCHType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siInfoVCInfoCHType.setStatus("current")


class _SiInfoVCInfoECMPID_Type(DisplayString):
    """Custom type siInfoVCInfoECMPID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SiInfoVCInfoECMPID_Type.__name__ = "DisplayString"
_SiInfoVCInfoECMPID_Object = MibTableColumn
siInfoVCInfoECMPID = _SiInfoVCInfoECMPID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 5, 1, 8),
    _SiInfoVCInfoECMPID_Type()
)
siInfoVCInfoECMPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siInfoVCInfoECMPID.setStatus("current")


class _SiInfoVCInfoAuthorized_Type(Integer32):
    """Custom type siInfoVCInfoAuthorized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SiInfoVCInfoAuthorized_Type.__name__ = "Integer32"
_SiInfoVCInfoAuthorized_Object = MibTableColumn
siInfoVCInfoAuthorized = _SiInfoVCInfoAuthorized_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 5, 4, 5, 1, 9),
    _SiInfoVCInfoAuthorized_Type()
)
siInfoVCInfoAuthorized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siInfoVCInfoAuthorized.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-TUNING-MIB",
    **{"ciscoDSGTuning": ciscoDSGTuning,
       "activeTuning": activeTuning,
       "activeTuningInput": activeTuningInput,
       "activeTuningValidateOrbPos": activeTuningValidateOrbPos,
       "activeTuningChScan": activeTuningChScan,
       "activeTuningTable": activeTuningTable,
       "activeTunerTable": activeTunerTable,
       "activeTunerEntry": activeTunerEntry,
       "activeTunerIndex": activeTunerIndex,
       "activeTunerRFInput": activeTunerRFInput,
       "activeTunerFreq": activeTunerFreq,
       "activeTunerSymbolRate": activeTunerSymbolRate,
       "activeTunerDVBSFEC": activeTunerDVBSFEC,
       "activeTunerModulation": activeTunerModulation,
       "activeTunerRollOff": activeTunerRollOff,
       "activeTunerIQ": activeTunerIQ,
       "activeInputTable": activeInputTable,
       "activeInputEntry": activeInputEntry,
       "activeInputRFIndex": activeInputRFIndex,
       "activeInputLNBType": activeInputLNBType,
       "activeInputLNBTrim": activeInputLNBTrim,
       "activeInputLNBTrim2": activeInputLNBTrim2,
       "activeInputLocalOscFreq1": activeInputLocalOscFreq1,
       "activeInputLocalOscFreq2": activeInputLocalOscFreq2,
       "activeInputCrossOver": activeInputCrossOver,
       "activeInputLocalOscControl": activeInputLocalOscControl,
       "activeInputOrbitalPos": activeInputOrbitalPos,
       "activeInputEastWestFlag": activeInputEastWestFlag,
       "activeInputPolarization": activeInputPolarization,
       "activeInputSatName": activeInputSatName,
       "activeInputLastLNBConfig": activeInputLastLNBConfig,
       "activeInputDiSeqCEnable": activeInputDiSeqCEnable,
       "activeInputDiSeqCSwitch": activeInputDiSeqCSwitch,
       "lnbPowerTable": lnbPowerTable,
       "lnbPowerEntry": lnbPowerEntry,
       "lnbPowerIndex": lnbPowerIndex,
       "lnbPowerInput": lnbPowerInput,
       "lnbPowerControl": lnbPowerControl,
       "lnbPowerStatus": lnbPowerStatus,
       "tuningStatusTable": tuningStatusTable,
       "satSignalTable": satSignalTable,
       "satSignalEntry": satSignalEntry,
       "satSignalIndex": satSignalIndex,
       "satSignalPvBer": satSignalPvBer,
       "satSignalQPSKBer": satSignalQPSKBer,
       "satSignalLdpCber": satSignalLdpCber,
       "satSignalCndisp": satSignalCndisp,
       "satSignalCnMargin": satSignalCnMargin,
       "satSignalLevel": satSignalLevel,
       "satSignalSatDishCnMargin": satSignalSatDishCnMargin,
       "satSignalSatDishSigLevel": satSignalSatDishSigLevel,
       "satSignalPerDisp": satSignalPerDisp,
       "satSignalAfc": satSignalAfc,
       "satSignalUncorErrCnt": satSignalUncorErrCnt,
       "satSignalCorErrCnt": satSignalCorErrCnt,
       "satSignalRfLock": satSignalRfLock,
       "satSignalDnLkFreq": satSignalDnLkFreq,
       "satSignalLbandFreq": satSignalLbandFreq,
       "satSignalSymbolRate": satSignalSymbolRate,
       "satSignalFecRate": satSignalFecRate,
       "satSignalPolarization": satSignalPolarization,
       "satSignalModulation": satSignalModulation,
       "satSignalIQ": satSignalIQ,
       "satSignalLnbPsStatus": satSignalLnbPsStatus,
       "satSignalPilots": satSignalPilots,
       "satSignalLoSelect": satSignalLoSelect,
       "satSignalPolar": satSignalPolar,
       "satSignalClearSigErrCnt": satSignalClearSigErrCnt,
       "satSignalValidateOrbPosDate": satSignalValidateOrbPosDate,
       "satSignalValidateOrbPosStat": satSignalValidateOrbPosStat,
       "satSignalChScanStatus": satSignalChScanStatus,
       "satSignalSigLevelRaw": satSignalSigLevelRaw,
       "satSignalP1DStatus": satSignalP1DStatus,
       "satSignalDvbS2FrameLen": satSignalDvbS2FrameLen,
       "satSignalCnMarginRaw": satSignalCnMarginRaw,
       "satSignalDvbSQpskErrCount": satSignalDvbSQpskErrCount,
       "satSignalDvbS2LdpcErrCount": satSignalDvbS2LdpcErrCount,
       "satSignalPvErrCount": satSignalPvErrCount,
       "satSignalFecSyncStatus": satSignalFecSyncStatus,
       "satSignalPktErrCount": satSignalPktErrCount,
       "inputStatusTable": inputStatusTable,
       "inputStatusEntry": inputStatusEntry,
       "inputStatusIndex": inputStatusIndex,
       "inputStatusCurInput": inputStatusCurInput,
       "inputStatusSatLock": inputStatusSatLock,
       "inputStatusMpgIpLock": inputStatusMpgIpLock,
       "inputStatusInputRate": inputStatusInputRate,
       "inputStatusNetworkName": inputStatusNetworkName,
       "inputStatusNetworkId": inputStatusNetworkId,
       "inputStatusTransportId": inputStatusTransportId,
       "inputStatusScramblingMode": inputStatusScramblingMode,
       "inputStatusTransportError": inputStatusTransportError,
       "inputStatusAsiLock": inputStatusAsiLock,
       "inputStatusAsiLinkError": inputStatusAsiLinkError,
       "inputStatusAsiPacketSize": inputStatusAsiPacketSize,
       "inputStatusLastTuneReason": inputStatusLastTuneReason,
       "inputStatusCurD985xInput": inputStatusCurD985xInput,
       "inputStatusIpiLinkStatus": inputStatusIpiLinkStatus,
       "inputStatusIpiSignal": inputStatusIpiSignal,
       "inputStatusIpiFecLock": inputStatusIpiFecLock,
       "inputStatusIpiPcrLock": inputStatusIpiPcrLock,
       "inputStatusIpiDelLatency": inputStatusIpiDelLatency,
       "inputStatusIpiData1SrcIP": inputStatusIpiData1SrcIP,
       "inputStatusIpiData2SrcIP": inputStatusIpiData2SrcIP,
       "inputStatusIpiData1TsType": inputStatusIpiData1TsType,
       "inputStatusIpiData2TsType": inputStatusIpiData2TsType,
       "siRcvTable": siRcvTable,
       "siRcvOptionTable": siRcvOptionTable,
       "siRcvOptionEntry": siRcvOptionEntry,
       "siRcvOptionInstance": siRcvOptionInstance,
       "siRcvOptionAcqMode": siRcvOptionAcqMode,
       "siRcvOptionReacq": siRcvOptionReacq,
       "siRcvOptionNetID": siRcvOptionNetID,
       "siRcvOptionInputSel": siRcvOptionInputSel,
       "siRcvOptionFreqSel": siRcvOptionFreqSel,
       "siRcvOptionServListMode": siRcvOptionServListMode,
       "siRcvOptionUseBAT": siRcvOptionUseBAT,
       "siRcvOptionUseNIT": siRcvOptionUseNIT,
       "siRcvOptionUseSDT": siRcvOptionUseSDT,
       "siRcvOptionUsePAT": siRcvOptionUsePAT,
       "siRcvOptionStatusTable": siRcvOptionStatusTable,
       "siRcvOptionStatusEntry": siRcvOptionStatusEntry,
       "siRcvOptionStatusInstance": siRcvOptionStatusInstance,
       "siRcvOptionLastChanReas": siRcvOptionLastChanReas,
       "siRcvOptionLastActivated": siRcvOptionLastActivated,
       "siRcvOptionStatusFreqSel": siRcvOptionStatusFreqSel,
       "siRcvOptionStatusServListMode": siRcvOptionStatusServListMode,
       "siRcvOptionStatusUseBAT": siRcvOptionStatusUseBAT,
       "siRcvOptionStatusUseNIT": siRcvOptionStatusUseNIT,
       "siRcvOptionStatusUseSDT": siRcvOptionStatusUseSDT,
       "siRcvOptionStatusUsePAT": siRcvOptionStatusUsePAT,
       "siInfoRxTable": siInfoRxTable,
       "siInfoRxEntry": siInfoRxEntry,
       "siInfoRxInstance": siInfoRxInstance,
       "siInfoRxIdx": siInfoRxIdx,
       "siInfoRxType": siInfoRxType,
       "siInfoRxIDExt": siInfoRxIDExt,
       "siInfoRxUid": siInfoRxUid,
       "siInfoRxStatus": siInfoRxStatus,
       "siInfoRxVer": siInfoRxVer,
       "siInfoRxPID": siInfoRxPID,
       "siInfoRxSections": siInfoRxSections,
       "siInfoTsTable": siInfoTsTable,
       "siInfoTsEntry": siInfoTsEntry,
       "siInfoTsInstance": siInfoTsInstance,
       "siInfoTsIdx": siInfoTsIdx,
       "siInfoTsId": siInfoTsId,
       "siInfoTsFreq": siInfoTsFreq,
       "siInfoTsSymRate": siInfoTsSymRate,
       "siInfoTsOrbPosn": siInfoTsOrbPosn,
       "siInfoTsPolar": siInfoTsPolar,
       "siInfoTsFEC": siInfoTsFEC,
       "siInfoTsModulation": siInfoTsModulation,
       "siInfoTsOrgNetID": siInfoTsOrgNetID,
       "siInfoTsEastWestFlag": siInfoTsEastWestFlag,
       "siInfoVCInfoTable": siInfoVCInfoTable,
       "siInfoVCInfoEntry": siInfoVCInfoEntry,
       "siInfoVCInfoInstance": siInfoVCInfoInstance,
       "siInfoVCInfoIdx": siInfoVCInfoIdx,
       "siInfoVCInfoId": siInfoVCInfoId,
       "siInfoVCInfoTxID": siInfoVCInfoTxID,
       "siInfoVCInfoProgName": siInfoVCInfoProgName,
       "siInfoVCInfoPMTPID": siInfoVCInfoPMTPID,
       "siInfoVCInfoCHType": siInfoVCInfoCHType,
       "siInfoVCInfoECMPID": siInfoVCInfoECMPID,
       "siInfoVCInfoAuthorized": siInfoVCInfoAuthorized}
)
