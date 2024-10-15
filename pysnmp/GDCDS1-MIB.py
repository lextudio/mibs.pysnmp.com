# SNMP MIB module (GDCDS1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GDCDS1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:13 2024
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

(ds1,) = mibBuilder.importSymbols(
    "RFC1406-MIB",
    "ds1")

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
 enterprises,
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "enterprises",
    "iso",
    "transmission")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Gdc_ObjectIdentity = ObjectIdentity
gdc = _Gdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498)
)
_Csu_ObjectIdentity = ObjectIdentity
csu = _Csu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 2)
)
_CsuConfigTable_Object = MibTable
csuConfigTable = _CsuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 1)
)
if mibBuilder.loadTexts:
    csuConfigTable.setStatus("mandatory")
_CsuConfigEntry_Object = MibTableRow
csuConfigEntry = _CsuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 1, 1)
)
csuConfigEntry.setIndexNames(
    (0, "GDCDS1-MIB", "csuConfigLineIndex"),
)
if mibBuilder.loadTexts:
    csuConfigEntry.setStatus("mandatory")
_CsuConfigLineIndex_Type = Integer32
_CsuConfigLineIndex_Object = MibTableColumn
csuConfigLineIndex = _CsuConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 1, 1, 1),
    _CsuConfigLineIndex_Type()
)
csuConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuConfigLineIndex.setStatus("mandatory")


class _CsuOnesDensity_Type(Integer32):
    """Custom type csuOnesDensity based on Integer32"""
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
        *(("csu8N1Restrict", 4),
          ("csuMax15Zeros", 2),
          ("csuMax39Zeros", 3),
          ("csuMin1in8", 5),
          ("inhibit", 1))
    )


_CsuOnesDensity_Type.__name__ = "Integer32"
_CsuOnesDensity_Object = MibTableColumn
csuOnesDensity = _CsuOnesDensity_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 1, 1, 2),
    _CsuOnesDensity_Type()
)
csuOnesDensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuOnesDensity.setStatus("mandatory")


class _CsuFrontPanel_Type(Integer32):
    """Custom type csuFrontPanel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("inhibit", 1))
    )


_CsuFrontPanel_Type.__name__ = "Integer32"
_CsuFrontPanel_Object = MibTableColumn
csuFrontPanel = _CsuFrontPanel_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 1, 1, 3),
    _CsuFrontPanel_Type()
)
csuFrontPanel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuFrontPanel.setStatus("mandatory")


class _CsuInbandLoop_Type(Integer32):
    """Custom type csuInbandLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("inhibit", 1))
    )


_CsuInbandLoop_Type.__name__ = "Integer32"
_CsuInbandLoop_Object = MibTableColumn
csuInbandLoop = _CsuInbandLoop_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 1, 1, 4),
    _CsuInbandLoop_Type()
)
csuInbandLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuInbandLoop.setStatus("mandatory")


class _CsuILBFrame_Type(Integer32):
    """Custom type csuILBFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("framed", 2),
          ("unframed", 1))
    )


_CsuILBFrame_Type.__name__ = "Integer32"
_CsuILBFrame_Object = MibTableColumn
csuILBFrame = _CsuILBFrame_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 1, 1, 5),
    _CsuILBFrame_Type()
)
csuILBFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuILBFrame.setStatus("mandatory")


class _CsuLineBuildOutCtrl_Type(Integer32):
    """Custom type csuLineBuildOutCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csuAuto", 2),
          ("csuMan", 1))
    )


_CsuLineBuildOutCtrl_Type.__name__ = "Integer32"
_CsuLineBuildOutCtrl_Object = MibTableColumn
csuLineBuildOutCtrl = _CsuLineBuildOutCtrl_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 1, 1, 6),
    _CsuLineBuildOutCtrl_Type()
)
csuLineBuildOutCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuLineBuildOutCtrl.setStatus("mandatory")


class _CsuLineBuildOutValue_Type(Integer32):
    """Custom type csuLineBuildOutValue based on Integer32"""
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
        *(("csu00dB", 2),
          ("csu150dB", 4),
          ("csu75dB", 3),
          ("other", 1))
    )


_CsuLineBuildOutValue_Type.__name__ = "Integer32"
_CsuLineBuildOutValue_Object = MibTableColumn
csuLineBuildOutValue = _CsuLineBuildOutValue_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 1, 1, 7),
    _CsuLineBuildOutValue_Type()
)
csuLineBuildOutValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuLineBuildOutValue.setStatus("mandatory")


class _CsuLineTypeCtrl_Type(Integer32):
    """Custom type csuLineTypeCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("csuAuto", 3),
          ("csuMan", 2),
          ("none", 1))
    )


_CsuLineTypeCtrl_Type.__name__ = "Integer32"
_CsuLineTypeCtrl_Object = MibTableColumn
csuLineTypeCtrl = _CsuLineTypeCtrl_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 1, 1, 8),
    _CsuLineTypeCtrl_Type()
)
csuLineTypeCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuLineTypeCtrl.setStatus("mandatory")


class _CsuAISLoopdown_Type(Integer32):
    """Custom type csuAISLoopdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_CsuAISLoopdown_Type.__name__ = "Integer32"
_CsuAISLoopdown_Object = MibTableColumn
csuAISLoopdown = _CsuAISLoopdown_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 1, 1, 9),
    _CsuAISLoopdown_Type()
)
csuAISLoopdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuAISLoopdown.setStatus("mandatory")


class _CsuPreEqualizer_Type(Integer32):
    """Custom type csuPreEqualizer based on Integer32"""
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
        *(("csu130ft", 2),
          ("csu260ft", 3),
          ("csu390ft", 4),
          ("csu530ft", 5),
          ("csu655ft", 6),
          ("csuNoEqual", 1))
    )


_CsuPreEqualizer_Type.__name__ = "Integer32"
_CsuPreEqualizer_Object = MibTableColumn
csuPreEqualizer = _CsuPreEqualizer_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 1, 1, 10),
    _CsuPreEqualizer_Type()
)
csuPreEqualizer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuPreEqualizer.setStatus("mandatory")


class _CsuInitialize_Type(Integer32):
    """Custom type csuInitialize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("csu24HourCounter", 2),
          ("csuAlarmHistory", 1),
          ("csuFactoryDefaults", 3))
    )


_CsuInitialize_Type.__name__ = "Integer32"
_CsuInitialize_Object = MibTableColumn
csuInitialize = _CsuInitialize_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 1, 1, 11),
    _CsuInitialize_Type()
)
csuInitialize.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    csuInitialize.setStatus("mandatory")


class _CsuTime_Type(DisplayString):
    """Custom type csuTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_CsuTime_Type.__name__ = "DisplayString"
_CsuTime_Object = MibTableColumn
csuTime = _CsuTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 1, 1, 12),
    _CsuTime_Type()
)
csuTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuTime.setStatus("mandatory")


class _CsuDate_Type(DisplayString):
    """Custom type csuDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CsuDate_Type.__name__ = "DisplayString"
_CsuDate_Object = MibTableColumn
csuDate = _CsuDate_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 1, 1, 13),
    _CsuDate_Type()
)
csuDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuDate.setStatus("mandatory")


class _CsuTestType_Type(Integer32):
    """Custom type csuTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csuLLB", 1),
          ("csuTLB", 2))
    )


_CsuTestType_Type.__name__ = "Integer32"
_CsuTestType_Object = MibTableColumn
csuTestType = _CsuTestType_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 1, 1, 14),
    _CsuTestType_Type()
)
csuTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuTestType.setStatus("mandatory")


class _CsuReceiveLevel_Type(DisplayString):
    """Custom type csuReceiveLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CsuReceiveLevel_Type.__name__ = "DisplayString"
_CsuReceiveLevel_Object = MibTableColumn
csuReceiveLevel = _CsuReceiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 1, 1, 15),
    _CsuReceiveLevel_Type()
)
csuReceiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuReceiveLevel.setStatus("mandatory")
_CsuChanConfigTable_Object = MibTable
csuChanConfigTable = _CsuChanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 2)
)
if mibBuilder.loadTexts:
    csuChanConfigTable.setStatus("mandatory")
_CsuChanConfigEntry_Object = MibTableRow
csuChanConfigEntry = _CsuChanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 2, 1)
)
csuChanConfigEntry.setIndexNames(
    (0, "GDCDS1-MIB", "csuChanConfigLineIndex"),
    (0, "GDCDS1-MIB", "csuChanConfigNum"),
)
if mibBuilder.loadTexts:
    csuChanConfigEntry.setStatus("mandatory")
_CsuChanConfigLineIndex_Type = Integer32
_CsuChanConfigLineIndex_Object = MibTableColumn
csuChanConfigLineIndex = _CsuChanConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 2, 1, 1),
    _CsuChanConfigLineIndex_Type()
)
csuChanConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuChanConfigLineIndex.setStatus("mandatory")
_CsuChanConfigNum_Type = Integer32
_CsuChanConfigNum_Object = MibTableColumn
csuChanConfigNum = _CsuChanConfigNum_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 2, 1, 2),
    _CsuChanConfigNum_Type()
)
csuChanConfigNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuChanConfigNum.setStatus("mandatory")


class _CsuStartDS0_Type(Integer32):
    """Custom type csuStartDS0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_CsuStartDS0_Type.__name__ = "Integer32"
_CsuStartDS0_Object = MibTableColumn
csuStartDS0 = _CsuStartDS0_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 2, 1, 3),
    _CsuStartDS0_Type()
)
csuStartDS0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuStartDS0.setStatus("mandatory")


class _CsuRTSCTS_Type(Integer32):
    """Custom type csuRTSCTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("csuCTSDelayed", 2),
          ("csuCTSForcedOn", 3),
          ("other", 1))
    )


_CsuRTSCTS_Type.__name__ = "Integer32"
_CsuRTSCTS_Object = MibTableColumn
csuRTSCTS = _CsuRTSCTS_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 2, 1, 4),
    _CsuRTSCTS_Type()
)
csuRTSCTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuRTSCTS.setStatus("mandatory")


class _CsuControlModeIdle_Type(Integer32):
    """Custom type csuControlModeIdle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CsuControlModeIdle_Type.__name__ = "Integer32"
_CsuControlModeIdle_Object = MibTableColumn
csuControlModeIdle = _CsuControlModeIdle_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 2, 1, 5),
    _CsuControlModeIdle_Type()
)
csuControlModeIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuControlModeIdle.setStatus("mandatory")


class _CsuRDLInbandCode_Type(Integer32):
    """Custom type csuRDLInbandCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("csuFixed", 3),
          ("csuPN127", 2),
          ("other", 1))
    )


_CsuRDLInbandCode_Type.__name__ = "Integer32"
_CsuRDLInbandCode_Object = MibTableColumn
csuRDLInbandCode = _CsuRDLInbandCode_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 2, 1, 6),
    _CsuRDLInbandCode_Type()
)
csuRDLInbandCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuRDLInbandCode.setStatus("mandatory")
_CsuChanRate_Type = Integer32
_CsuChanRate_Object = MibTableColumn
csuChanRate = _CsuChanRate_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 2, 1, 7),
    _CsuChanRate_Type()
)
csuChanRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuChanRate.setStatus("mandatory")


class _CsuAlternateDS0_Type(Integer32):
    """Custom type csuAlternateDS0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CsuAlternateDS0_Type.__name__ = "Integer32"
_CsuAlternateDS0_Object = MibTableColumn
csuAlternateDS0 = _CsuAlternateDS0_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 2, 1, 8),
    _CsuAlternateDS0_Type()
)
csuAlternateDS0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuAlternateDS0.setStatus("mandatory")


class _CsuRespondRDL_Type(Integer32):
    """Custom type csuRespondRDL based on Integer32"""
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


_CsuRespondRDL_Type.__name__ = "Integer32"
_CsuRespondRDL_Object = MibTableColumn
csuRespondRDL = _CsuRespondRDL_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 2, 1, 9),
    _CsuRespondRDL_Type()
)
csuRespondRDL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuRespondRDL.setStatus("mandatory")


class _CsuInbandDLTimeout_Type(Integer32):
    """Custom type csuInbandDLTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csuEnable10Min", 2),
          ("inhibit", 1))
    )


_CsuInbandDLTimeout_Type.__name__ = "Integer32"
_CsuInbandDLTimeout_Object = MibTableColumn
csuInbandDLTimeout = _CsuInbandDLTimeout_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 2, 1, 10),
    _CsuInbandDLTimeout_Type()
)
csuInbandDLTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuInbandDLTimeout.setStatus("mandatory")


class _CsuChanStatus_Type(Integer32):
    """Custom type csuChanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CsuChanStatus_Type.__name__ = "Integer32"
_CsuChanStatus_Object = MibTableColumn
csuChanStatus = _CsuChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 2, 1, 11),
    _CsuChanStatus_Type()
)
csuChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuChanStatus.setStatus("mandatory")


class _CsuChan6456_Type(Integer32):
    """Custom type csuChan6456 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode56", 1),
          ("mode64", 2))
    )


_CsuChan6456_Type.__name__ = "Integer32"
_CsuChan6456_Object = MibScalar
csuChan6456 = _CsuChan6456_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 2, 1, 12),
    _CsuChan6456_Type()
)
csuChan6456.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuChan6456.setStatus("mandatory")
_CsuIndicatorTable_Object = MibTable
csuIndicatorTable = _CsuIndicatorTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 3)
)
if mibBuilder.loadTexts:
    csuIndicatorTable.setStatus("mandatory")
_CsuIndicatorEntry_Object = MibTableRow
csuIndicatorEntry = _CsuIndicatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 3, 1)
)
csuIndicatorEntry.setIndexNames(
    (0, "GDCDS1-MIB", "csuIndicatorIndex"),
)
if mibBuilder.loadTexts:
    csuIndicatorEntry.setStatus("mandatory")
_CsuIndicatorIndex_Type = Integer32
_CsuIndicatorIndex_Object = MibTableColumn
csuIndicatorIndex = _CsuIndicatorIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 3, 1, 1),
    _CsuIndicatorIndex_Type()
)
csuIndicatorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuIndicatorIndex.setStatus("mandatory")


class _CsuIndicatorOOF_Type(Integer32):
    """Custom type csuIndicatorOOF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-synchronized", 1),
          ("synchronized", 2),
          ("unframed", 3))
    )


_CsuIndicatorOOF_Type.__name__ = "Integer32"
_CsuIndicatorOOF_Object = MibTableColumn
csuIndicatorOOF = _CsuIndicatorOOF_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 3, 1, 2),
    _CsuIndicatorOOF_Type()
)
csuIndicatorOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuIndicatorOOF.setStatus("mandatory")


class _CsuIndicatorNNS_Type(Integer32):
    """Custom type csuIndicatorNNS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-signal", 1),
          ("signal", 2))
    )


_CsuIndicatorNNS_Type.__name__ = "Integer32"
_CsuIndicatorNNS_Object = MibTableColumn
csuIndicatorNNS = _CsuIndicatorNNS_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 3, 1, 3),
    _CsuIndicatorNNS_Type()
)
csuIndicatorNNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuIndicatorNNS.setStatus("mandatory")


class _CsuIndicatorYEL_Type(Integer32):
    """Custom type csuIndicatorYEL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-receiving", 1),
          ("receiving", 2),
          ("unframed", 3))
    )


_CsuIndicatorYEL_Type.__name__ = "Integer32"
_CsuIndicatorYEL_Object = MibTableColumn
csuIndicatorYEL = _CsuIndicatorYEL_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 3, 1, 4),
    _CsuIndicatorYEL_Type()
)
csuIndicatorYEL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuIndicatorYEL.setStatus("mandatory")


class _CsuIndicatorAIS_Type(Integer32):
    """Custom type csuIndicatorAIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-receiving", 1),
          ("receiving", 2),
          ("unframed", 3))
    )


_CsuIndicatorAIS_Type.__name__ = "Integer32"
_CsuIndicatorAIS_Object = MibTableColumn
csuIndicatorAIS = _CsuIndicatorAIS_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 3, 1, 5),
    _CsuIndicatorAIS_Type()
)
csuIndicatorAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuIndicatorAIS.setStatus("mandatory")


class _CsuIndicatorNLB_Type(Integer32):
    """Custom type csuIndicatorNLB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopback", 2),
          ("not-loopback", 1))
    )


_CsuIndicatorNLB_Type.__name__ = "Integer32"
_CsuIndicatorNLB_Object = MibTableColumn
csuIndicatorNLB = _CsuIndicatorNLB_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 3, 1, 6),
    _CsuIndicatorNLB_Type()
)
csuIndicatorNLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuIndicatorNLB.setStatus("mandatory")


class _CsuIndicatorBPV_Type(Integer32):
    """Custom type csuIndicatorBPV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-receiving", 1),
          ("receiving", 2))
    )


_CsuIndicatorBPV_Type.__name__ = "Integer32"
_CsuIndicatorBPV_Object = MibTableColumn
csuIndicatorBPV = _CsuIndicatorBPV_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 3, 1, 7),
    _CsuIndicatorBPV_Type()
)
csuIndicatorBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuIndicatorBPV.setStatus("mandatory")


class _CsuIndicatorCRC_Type(Integer32):
    """Custom type csuIndicatorCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-receiving", 1),
          ("receiving", 2),
          ("unframed", 3))
    )


_CsuIndicatorCRC_Type.__name__ = "Integer32"
_CsuIndicatorCRC_Object = MibTableColumn
csuIndicatorCRC = _CsuIndicatorCRC_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 3, 1, 8),
    _CsuIndicatorCRC_Type()
)
csuIndicatorCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuIndicatorCRC.setStatus("mandatory")


class _CsuIndicatorTSY_Type(Integer32):
    """Custom type csuIndicatorTSY based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-synchronized", 1),
          ("synchronized", 2),
          ("unframed", 3))
    )


_CsuIndicatorTSY_Type.__name__ = "Integer32"
_CsuIndicatorTSY_Object = MibTableColumn
csuIndicatorTSY = _CsuIndicatorTSY_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 3, 1, 9),
    _CsuIndicatorTSY_Type()
)
csuIndicatorTSY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuIndicatorTSY.setStatus("mandatory")


class _CsuIndicatorTNS_Type(Integer32):
    """Custom type csuIndicatorTNS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-receiving", 1),
          ("receiving", 2))
    )


_CsuIndicatorTNS_Type.__name__ = "Integer32"
_CsuIndicatorTNS_Object = MibTableColumn
csuIndicatorTNS = _CsuIndicatorTNS_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 3, 1, 10),
    _CsuIndicatorTNS_Type()
)
csuIndicatorTNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuIndicatorTNS.setStatus("mandatory")


class _CsuIndicatorOS_Type(Integer32):
    """Custom type csuIndicatorOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-receiving", 1),
          ("receiving", 2))
    )


_CsuIndicatorOS_Type.__name__ = "Integer32"
_CsuIndicatorOS_Object = MibTableColumn
csuIndicatorOS = _CsuIndicatorOS_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 3, 1, 11),
    _CsuIndicatorOS_Type()
)
csuIndicatorOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuIndicatorOS.setStatus("mandatory")


class _CsuIndicatorLAD_Type(Integer32):
    """Custom type csuIndicatorLAD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-receiving", 1),
          ("receiving", 2))
    )


_CsuIndicatorLAD_Type.__name__ = "Integer32"
_CsuIndicatorLAD_Object = MibTableColumn
csuIndicatorLAD = _CsuIndicatorLAD_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 3, 1, 12),
    _CsuIndicatorLAD_Type()
)
csuIndicatorLAD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuIndicatorLAD.setStatus("mandatory")


class _CsuIndicatorCascadeOOF_Type(Integer32):
    """Custom type csuIndicatorCascadeOOF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-synchronized", 1),
          ("synchronized", 2))
    )


_CsuIndicatorCascadeOOF_Type.__name__ = "Integer32"
_CsuIndicatorCascadeOOF_Object = MibTableColumn
csuIndicatorCascadeOOF = _CsuIndicatorCascadeOOF_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 3, 1, 13),
    _CsuIndicatorCascadeOOF_Type()
)
csuIndicatorCascadeOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuIndicatorCascadeOOF.setStatus("mandatory")


class _CsuIndicatorCascadeNS_Type(Integer32):
    """Custom type csuIndicatorCascadeNS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-receiving", 1),
          ("receiving", 2))
    )


_CsuIndicatorCascadeNS_Type.__name__ = "Integer32"
_CsuIndicatorCascadeNS_Object = MibTableColumn
csuIndicatorCascadeNS = _CsuIndicatorCascadeNS_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 3, 1, 14),
    _CsuIndicatorCascadeNS_Type()
)
csuIndicatorCascadeNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuIndicatorCascadeNS.setStatus("mandatory")


class _CsuIndicatorNetworkLT_Type(Integer32):
    """Custom type csuIndicatorNetworkLT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("not-active", 1))
    )


_CsuIndicatorNetworkLT_Type.__name__ = "Integer32"
_CsuIndicatorNetworkLT_Object = MibTableColumn
csuIndicatorNetworkLT = _CsuIndicatorNetworkLT_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 3, 1, 15),
    _CsuIndicatorNetworkLT_Type()
)
csuIndicatorNetworkLT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuIndicatorNetworkLT.setStatus("mandatory")


class _CsuIndicatorNetworkST_Type(Integer32):
    """Custom type csuIndicatorNetworkST based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active-DS0", 2),
          ("active-DS1", 3),
          ("not-active", 1))
    )


_CsuIndicatorNetworkST_Type.__name__ = "Integer32"
_CsuIndicatorNetworkST_Object = MibTableColumn
csuIndicatorNetworkST = _CsuIndicatorNetworkST_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 3, 1, 16),
    _CsuIndicatorNetworkST_Type()
)
csuIndicatorNetworkST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuIndicatorNetworkST.setStatus("mandatory")


class _CsuIndicatorNetworkRT_Type(Integer32):
    """Custom type csuIndicatorNetworkRT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("not-active", 1))
    )


_CsuIndicatorNetworkRT_Type.__name__ = "Integer32"
_CsuIndicatorNetworkRT_Object = MibTableColumn
csuIndicatorNetworkRT = _CsuIndicatorNetworkRT_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 3, 1, 17),
    _CsuIndicatorNetworkRT_Type()
)
csuIndicatorNetworkRT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuIndicatorNetworkRT.setStatus("mandatory")


class _CsuIndicatorChannelRDL_Type(Integer32):
    """Custom type csuIndicatorChannelRDL based on Integer32"""
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
        *(("active-chA", 2),
          ("active-chAB", 4),
          ("active-chB", 3),
          ("not-active", 1))
    )


_CsuIndicatorChannelRDL_Type.__name__ = "Integer32"
_CsuIndicatorChannelRDL_Object = MibTableColumn
csuIndicatorChannelRDL = _CsuIndicatorChannelRDL_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 3, 1, 18),
    _CsuIndicatorChannelRDL_Type()
)
csuIndicatorChannelRDL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuIndicatorChannelRDL.setStatus("mandatory")


class _CsuIndicatorChannelST_Type(Integer32):
    """Custom type csuIndicatorChannelST based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active-chA", 2),
          ("active-chB", 3),
          ("not-active", 1))
    )


_CsuIndicatorChannelST_Type.__name__ = "Integer32"
_CsuIndicatorChannelST_Object = MibTableColumn
csuIndicatorChannelST = _CsuIndicatorChannelST_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 3, 1, 19),
    _CsuIndicatorChannelST_Type()
)
csuIndicatorChannelST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuIndicatorChannelST.setStatus("mandatory")


class _CsuIndicatorChannelDL_Type(Integer32):
    """Custom type csuIndicatorChannelDL based on Integer32"""
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
        *(("active-chA", 2),
          ("active-chAB", 4),
          ("active-chB", 3),
          ("not-active", 1))
    )


_CsuIndicatorChannelDL_Type.__name__ = "Integer32"
_CsuIndicatorChannelDL_Object = MibTableColumn
csuIndicatorChannelDL = _CsuIndicatorChannelDL_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 3, 1, 20),
    _CsuIndicatorChannelDL_Type()
)
csuIndicatorChannelDL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuIndicatorChannelDL.setStatus("mandatory")


class _CsuIndicatorChannelLL_Type(Integer32):
    """Custom type csuIndicatorChannelLL based on Integer32"""
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
        *(("active-chA", 2),
          ("active-chAB", 4),
          ("active-chB", 3),
          ("not-active", 1))
    )


_CsuIndicatorChannelLL_Type.__name__ = "Integer32"
_CsuIndicatorChannelLL_Object = MibTableColumn
csuIndicatorChannelLL = _CsuIndicatorChannelLL_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 3, 1, 21),
    _CsuIndicatorChannelLL_Type()
)
csuIndicatorChannelLL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuIndicatorChannelLL.setStatus("mandatory")


class _CsuIndicatorMode_Type(Integer32):
    """Custom type csuIndicatorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hard", 2),
          ("none", 1),
          ("soft", 3))
    )


_CsuIndicatorMode_Type.__name__ = "Integer32"
_CsuIndicatorMode_Object = MibTableColumn
csuIndicatorMode = _CsuIndicatorMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 3, 1, 22),
    _CsuIndicatorMode_Type()
)
csuIndicatorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuIndicatorMode.setStatus("mandatory")


class _CsuIndicatorDS0LB_Type(Integer32):
    """Custom type csuIndicatorDS0LB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopback", 2),
          ("not-loopback", 1))
    )


_CsuIndicatorDS0LB_Type.__name__ = "Integer32"
_CsuIndicatorDS0LB_Object = MibTableColumn
csuIndicatorDS0LB = _CsuIndicatorDS0LB_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 3, 1, 23),
    _CsuIndicatorDS0LB_Type()
)
csuIndicatorDS0LB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuIndicatorDS0LB.setStatus("mandatory")
_CsuSelftestDiagTable_Object = MibTable
csuSelftestDiagTable = _CsuSelftestDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 4)
)
if mibBuilder.loadTexts:
    csuSelftestDiagTable.setStatus("mandatory")
_CsuSelftestDiagEntry_Object = MibTableRow
csuSelftestDiagEntry = _CsuSelftestDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 4, 1)
)
csuSelftestDiagEntry.setIndexNames(
    (0, "GDCDS1-MIB", "csuSelftestDiagLineIndex"),
)
if mibBuilder.loadTexts:
    csuSelftestDiagEntry.setStatus("mandatory")
_CsuSelftestDiagLineIndex_Type = Integer32
_CsuSelftestDiagLineIndex_Object = MibTableColumn
csuSelftestDiagLineIndex = _CsuSelftestDiagLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 4, 1, 1),
    _CsuSelftestDiagLineIndex_Type()
)
csuSelftestDiagLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuSelftestDiagLineIndex.setStatus("mandatory")


class _CsuDiagSelftest_Type(Integer32):
    """Custom type csuDiagSelftest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CsuDiagSelftest_Type.__name__ = "Integer32"
_CsuDiagSelftest_Object = MibTableColumn
csuDiagSelftest = _CsuDiagSelftest_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 4, 1, 2),
    _CsuDiagSelftest_Type()
)
csuDiagSelftest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuDiagSelftest.setStatus("obsolete")


class _CsuGDCSelftestPattern_Type(Integer32):
    """Custom type csuGDCSelftestPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("csu2047", 2),
          ("csuPROG", 3),
          ("other", 1))
    )


_CsuGDCSelftestPattern_Type.__name__ = "Integer32"
_CsuGDCSelftestPattern_Object = MibTableColumn
csuGDCSelftestPattern = _CsuGDCSelftestPattern_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 4, 1, 3),
    _CsuGDCSelftestPattern_Type()
)
csuGDCSelftestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuGDCSelftestPattern.setStatus("mandatory")


class _CsuSelftestUserPattern_Type(DisplayString):
    """Custom type csuSelftestUserPattern based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_CsuSelftestUserPattern_Type.__name__ = "DisplayString"
_CsuSelftestUserPattern_Object = MibTableColumn
csuSelftestUserPattern = _CsuSelftestUserPattern_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 4, 1, 4),
    _CsuSelftestUserPattern_Type()
)
csuSelftestUserPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuSelftestUserPattern.setStatus("mandatory")


class _CsuSelftestFrame_Type(Integer32):
    """Custom type csuSelftestFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("framed", 2),
          ("unframed", 1))
    )


_CsuSelftestFrame_Type.__name__ = "Integer32"
_CsuSelftestFrame_Object = MibTableColumn
csuSelftestFrame = _CsuSelftestFrame_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 4, 1, 5),
    _CsuSelftestFrame_Type()
)
csuSelftestFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuSelftestFrame.setStatus("mandatory")


class _CsuSelftestResults_Type(DisplayString):
    """Custom type csuSelftestResults based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CsuSelftestResults_Type.__name__ = "DisplayString"
_CsuSelftestResults_Object = MibTableColumn
csuSelftestResults = _CsuSelftestResults_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 4, 1, 6),
    _CsuSelftestResults_Type()
)
csuSelftestResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuSelftestResults.setStatus("mandatory")
_CsuSelftestTime_Type = TimeTicks
_CsuSelftestTime_Object = MibTableColumn
csuSelftestTime = _CsuSelftestTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 4, 1, 7),
    _CsuSelftestTime_Type()
)
csuSelftestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuSelftestTime.setStatus("mandatory")
_CsuLoopbackDiagTable_Object = MibTable
csuLoopbackDiagTable = _CsuLoopbackDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 5)
)
if mibBuilder.loadTexts:
    csuLoopbackDiagTable.setStatus("mandatory")
_CsuLoopbackDiagEntry_Object = MibTableRow
csuLoopbackDiagEntry = _CsuLoopbackDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 5, 1)
)
csuLoopbackDiagEntry.setIndexNames(
    (0, "GDCDS1-MIB", "csuLoopbackDiagLineIndex"),
)
if mibBuilder.loadTexts:
    csuLoopbackDiagEntry.setStatus("mandatory")
_CsuLoopbackDiagLineIndex_Type = Integer32
_CsuLoopbackDiagLineIndex_Object = MibTableColumn
csuLoopbackDiagLineIndex = _CsuLoopbackDiagLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 5, 1, 1),
    _CsuLoopbackDiagLineIndex_Type()
)
csuLoopbackDiagLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuLoopbackDiagLineIndex.setStatus("mandatory")


class _CsuGDCLoopback_Type(Integer32):
    """Custom type csuGDCLoopback based on Integer32"""
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
        *(("csuCascadeDigitalLoop", 4),
          ("csuLocalTest", 2),
          ("csuNILoop", 3),
          ("csuRemoteLoop", 5),
          ("other", 1))
    )


_CsuGDCLoopback_Type.__name__ = "Integer32"
_CsuGDCLoopback_Object = MibTableColumn
csuGDCLoopback = _CsuGDCLoopback_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 5, 1, 2),
    _CsuGDCLoopback_Type()
)
csuGDCLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuGDCLoopback.setStatus("mandatory")
_CsuDS0DiagTable_Object = MibTable
csuDS0DiagTable = _CsuDS0DiagTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 6)
)
if mibBuilder.loadTexts:
    csuDS0DiagTable.setStatus("mandatory")
_CsuDS0DiagEntry_Object = MibTableRow
csuDS0DiagEntry = _CsuDS0DiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 6, 1)
)
csuDS0DiagEntry.setIndexNames(
    (0, "GDCDS1-MIB", "csuDS0LineIndex"),
)
if mibBuilder.loadTexts:
    csuDS0DiagEntry.setStatus("mandatory")
_CsuDS0LineIndex_Type = Integer32
_CsuDS0LineIndex_Object = MibTableColumn
csuDS0LineIndex = _CsuDS0LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 6, 1, 1),
    _CsuDS0LineIndex_Type()
)
csuDS0LineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuDS0LineIndex.setStatus("mandatory")


class _CsuDS0Num_Type(Integer32):
    """Custom type csuDS0Num based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_CsuDS0Num_Type.__name__ = "Integer32"
_CsuDS0Num_Object = MibTableColumn
csuDS0Num = _CsuDS0Num_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 6, 1, 2),
    _CsuDS0Num_Type()
)
csuDS0Num.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuDS0Num.setStatus("mandatory")


class _CsuTestPattern_Type(Integer32):
    """Custom type csuTestPattern based on Integer32"""
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
        *(("csu2047", 4),
          ("csu511", 2),
          ("csuQRS", 3),
          ("other", 1))
    )


_CsuTestPattern_Type.__name__ = "Integer32"
_CsuTestPattern_Object = MibTableColumn
csuTestPattern = _CsuTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 6, 1, 3),
    _CsuTestPattern_Type()
)
csuTestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuTestPattern.setStatus("mandatory")


class _CsuResetResults_Type(Integer32):
    """Custom type csuResetResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_CsuResetResults_Type.__name__ = "Integer32"
_CsuResetResults_Object = MibTableColumn
csuResetResults = _CsuResetResults_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 6, 1, 4),
    _CsuResetResults_Type()
)
csuResetResults.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    csuResetResults.setStatus("mandatory")


class _CsuBERtest_Type(Integer32):
    """Custom type csuBERtest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds0BERoff", 1),
          ("ds0BERon", 2))
    )


_CsuBERtest_Type.__name__ = "Integer32"
_CsuBERtest_Object = MibTableColumn
csuBERtest = _CsuBERtest_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 6, 1, 5),
    _CsuBERtest_Type()
)
csuBERtest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuBERtest.setStatus("mandatory")


class _CsuCumErrs_Type(DisplayString):
    """Custom type csuCumErrs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CsuCumErrs_Type.__name__ = "DisplayString"
_CsuCumErrs_Object = MibTableColumn
csuCumErrs = _CsuCumErrs_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 6, 1, 6),
    _CsuCumErrs_Type()
)
csuCumErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuCumErrs.setStatus("mandatory")


class _CsuDataBlocks_Type(DisplayString):
    """Custom type csuDataBlocks based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CsuDataBlocks_Type.__name__ = "DisplayString"
_CsuDataBlocks_Object = MibTableColumn
csuDataBlocks = _CsuDataBlocks_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 6, 1, 7),
    _CsuDataBlocks_Type()
)
csuDataBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuDataBlocks.setStatus("mandatory")
_CsuCircuitDelayCtrl_Type = Integer32
_CsuCircuitDelayCtrl_Object = MibTableColumn
csuCircuitDelayCtrl = _CsuCircuitDelayCtrl_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 6, 1, 8),
    _CsuCircuitDelayCtrl_Type()
)
csuCircuitDelayCtrl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    csuCircuitDelayCtrl.setStatus("mandatory")


class _CsuCircuitDelayResult_Type(DisplayString):
    """Custom type csuCircuitDelayResult based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CsuCircuitDelayResult_Type.__name__ = "DisplayString"
_CsuCircuitDelayResult_Object = MibTableColumn
csuCircuitDelayResult = _CsuCircuitDelayResult_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 6, 1, 9),
    _CsuCircuitDelayResult_Type()
)
csuCircuitDelayResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuCircuitDelayResult.setStatus("mandatory")


class _CsuLBtest_Type(Integer32):
    """Custom type csuLBtest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds0LBoff", 1),
          ("ds0LBon", 2))
    )


_CsuLBtest_Type.__name__ = "Integer32"
_CsuLBtest_Object = MibTableColumn
csuLBtest = _CsuLBtest_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 6, 1, 10),
    _CsuLBtest_Type()
)
csuLBtest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuLBtest.setStatus("mandatory")
_CsuChanDiagTable_Object = MibTable
csuChanDiagTable = _CsuChanDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 7)
)
if mibBuilder.loadTexts:
    csuChanDiagTable.setStatus("mandatory")
_CsuChanDiagEntry_Object = MibTableRow
csuChanDiagEntry = _CsuChanDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 7, 1)
)
csuChanDiagEntry.setIndexNames(
    (0, "GDCDS1-MIB", "csuChanLineIndex"),
    (0, "GDCDS1-MIB", "csuChanNum"),
)
if mibBuilder.loadTexts:
    csuChanDiagEntry.setStatus("mandatory")
_CsuChanLineIndex_Type = Integer32
_CsuChanLineIndex_Object = MibTableColumn
csuChanLineIndex = _CsuChanLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 7, 1, 1),
    _CsuChanLineIndex_Type()
)
csuChanLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuChanLineIndex.setStatus("mandatory")
_CsuChanNum_Type = Integer32
_CsuChanNum_Object = MibTableColumn
csuChanNum = _CsuChanNum_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 7, 1, 2),
    _CsuChanNum_Type()
)
csuChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuChanNum.setStatus("mandatory")


class _CsuChanSelftest_Type(Integer32):
    """Custom type csuChanSelftest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CsuChanSelftest_Type.__name__ = "Integer32"
_CsuChanSelftest_Object = MibTableColumn
csuChanSelftest = _CsuChanSelftest_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 7, 1, 3),
    _CsuChanSelftest_Type()
)
csuChanSelftest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuChanSelftest.setStatus("mandatory")


class _CsuChanLoopback_Type(Integer32):
    """Custom type csuChanLoopback based on Integer32"""
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
        *(("csuDL", 3),
          ("csuLL", 4),
          ("csuNoLoop", 1),
          ("csuRDL", 2))
    )


_CsuChanLoopback_Type.__name__ = "Integer32"
_CsuChanLoopback_Object = MibTableColumn
csuChanLoopback = _CsuChanLoopback_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 7, 1, 4),
    _CsuChanLoopback_Type()
)
csuChanLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuChanLoopback.setStatus("mandatory")


class _CsuChanSelftestStatus_Type(DisplayString):
    """Custom type csuChanSelftestStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CsuChanSelftestStatus_Type.__name__ = "DisplayString"
_CsuChanSelftestStatus_Object = MibTableColumn
csuChanSelftestStatus = _CsuChanSelftestStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 7, 1, 5),
    _CsuChanSelftestStatus_Type()
)
csuChanSelftestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuChanSelftestStatus.setStatus("mandatory")
_CsuAlarmHistoryTable_Object = MibTable
csuAlarmHistoryTable = _CsuAlarmHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 8)
)
if mibBuilder.loadTexts:
    csuAlarmHistoryTable.setStatus("mandatory")
_CsuAlarmHistoryEntry_Object = MibTableRow
csuAlarmHistoryEntry = _CsuAlarmHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 8, 1)
)
csuAlarmHistoryEntry.setIndexNames(
    (0, "GDCDS1-MIB", "csuAlarmHistoryIndex"),
    (0, "GDCDS1-MIB", "csuAlarmType"),
)
if mibBuilder.loadTexts:
    csuAlarmHistoryEntry.setStatus("mandatory")
_CsuAlarmHistoryIndex_Type = Integer32
_CsuAlarmHistoryIndex_Object = MibTableColumn
csuAlarmHistoryIndex = _CsuAlarmHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 8, 1, 1),
    _CsuAlarmHistoryIndex_Type()
)
csuAlarmHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuAlarmHistoryIndex.setStatus("mandatory")


class _CsuAlarmType_Type(Integer32):
    """Custom type csuAlarmType based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("csuAlarmIndication", 3),
          ("csuBipolarViolations", 8),
          ("csuCRCErrors", 9),
          ("csuCascadeLossOfSignal", 12),
          ("csuCascadeOutOfFrame", 13),
          ("csuControlledSlips", 10),
          ("csuExcessiveZeros", 6),
          ("csuFailedSignalState", 4),
          ("csuLowAverageDensity", 7),
          ("csuNetworkLossOfSignal", 1),
          ("csuNetworkOutOfFrame", 2),
          ("csuReceivedYellow", 5),
          ("csuUnavailableSignalState", 11))
    )


_CsuAlarmType_Type.__name__ = "Integer32"
_CsuAlarmType_Object = MibTableColumn
csuAlarmType = _CsuAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 8, 1, 2),
    _CsuAlarmType_Type()
)
csuAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuAlarmType.setStatus("mandatory")


class _CsuAlarmHistoryStart_Type(DisplayString):
    """Custom type csuAlarmHistoryStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_CsuAlarmHistoryStart_Type.__name__ = "DisplayString"
_CsuAlarmHistoryStart_Object = MibTableColumn
csuAlarmHistoryStart = _CsuAlarmHistoryStart_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 8, 1, 3),
    _CsuAlarmHistoryStart_Type()
)
csuAlarmHistoryStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuAlarmHistoryStart.setStatus("mandatory")
_CsuCount_Type = Gauge32
_CsuCount_Object = MibTableColumn
csuCount = _CsuCount_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 8, 1, 4),
    _CsuCount_Type()
)
csuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuCount.setStatus("mandatory")


class _CsuFirstOccur_Type(DisplayString):
    """Custom type csuFirstOccur based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_CsuFirstOccur_Type.__name__ = "DisplayString"
_CsuFirstOccur_Object = MibTableColumn
csuFirstOccur = _CsuFirstOccur_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 8, 1, 5),
    _CsuFirstOccur_Type()
)
csuFirstOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuFirstOccur.setStatus("mandatory")


class _CsuLastOccur_Type(DisplayString):
    """Custom type csuLastOccur based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_CsuLastOccur_Type.__name__ = "DisplayString"
_CsuLastOccur_Object = MibTableColumn
csuLastOccur = _CsuLastOccur_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 8, 1, 6),
    _CsuLastOccur_Type()
)
csuLastOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuLastOccur.setStatus("mandatory")
_CsuSchedPerfRprtTable_Object = MibTable
csuSchedPerfRprtTable = _CsuSchedPerfRprtTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 9)
)
if mibBuilder.loadTexts:
    csuSchedPerfRprtTable.setStatus("mandatory")
_CsuSchedPerfRprtEntry_Object = MibTableRow
csuSchedPerfRprtEntry = _CsuSchedPerfRprtEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 9, 1)
)
csuSchedPerfRprtEntry.setIndexNames(
    (0, "GDCDS1-MIB", "csuSchedPerfRprtIndex"),
    (0, "GDCDS1-MIB", "csuPerfRprtIntervalNumber"),
)
if mibBuilder.loadTexts:
    csuSchedPerfRprtEntry.setStatus("mandatory")
_CsuSchedPerfRprtIndex_Type = Integer32
_CsuSchedPerfRprtIndex_Object = MibTableColumn
csuSchedPerfRprtIndex = _CsuSchedPerfRprtIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 9, 1, 1),
    _CsuSchedPerfRprtIndex_Type()
)
csuSchedPerfRprtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuSchedPerfRprtIndex.setStatus("mandatory")


class _CsuPerfRprtIntervalNumber_Type(Integer32):
    """Custom type csuPerfRprtIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CsuPerfRprtIntervalNumber_Type.__name__ = "Integer32"
_CsuPerfRprtIntervalNumber_Object = MibTableColumn
csuPerfRprtIntervalNumber = _CsuPerfRprtIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 9, 1, 2),
    _CsuPerfRprtIntervalNumber_Type()
)
csuPerfRprtIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuPerfRprtIntervalNumber.setStatus("mandatory")


class _CsuPerfRprtMsg_Type(Integer32):
    """Custom type csuPerfRprtMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_CsuPerfRprtMsg_Type.__name__ = "Integer32"
_CsuPerfRprtMsg_Object = MibTableColumn
csuPerfRprtMsg = _CsuPerfRprtMsg_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 9, 1, 3),
    _CsuPerfRprtMsg_Type()
)
csuPerfRprtMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csuPerfRprtMsg.setStatus("mandatory")


class _CsuCRCErrEvent_Type(Integer32):
    """Custom type csuCRCErrEvent based on Integer32"""
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
        *(("csuGreater320", 7),
          ("csuLess100", 5),
          ("csuLess320", 6),
          ("csuLessFive", 3),
          ("csuLessTen", 4),
          ("csuNoErrors", 1),
          ("csuOneError", 2))
    )


_CsuCRCErrEvent_Type.__name__ = "Integer32"
_CsuCRCErrEvent_Object = MibTableColumn
csuCRCErrEvent = _CsuCRCErrEvent_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 9, 1, 4),
    _CsuCRCErrEvent_Type()
)
csuCRCErrEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuCRCErrEvent.setStatus("mandatory")


class _CsuSEEvent_Type(Integer32):
    """Custom type csuSEEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csuNoErrors", 1),
          ("csuOneOrMore", 2))
    )


_CsuSEEvent_Type.__name__ = "Integer32"
_CsuSEEvent_Object = MibTableColumn
csuSEEvent = _CsuSEEvent_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 9, 1, 5),
    _CsuSEEvent_Type()
)
csuSEEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuSEEvent.setStatus("mandatory")


class _CsuFEEvent_Type(Integer32):
    """Custom type csuFEEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csuNoErrors", 1),
          ("csuOneOrMore", 2))
    )


_CsuFEEvent_Type.__name__ = "Integer32"
_CsuFEEvent_Object = MibTableColumn
csuFEEvent = _CsuFEEvent_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 9, 1, 6),
    _CsuFEEvent_Type()
)
csuFEEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuFEEvent.setStatus("mandatory")


class _CsuCVEvent_Type(Integer32):
    """Custom type csuCVEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csuNoErrors", 1),
          ("csuOneOrMore", 2))
    )


_CsuCVEvent_Type.__name__ = "Integer32"
_CsuCVEvent_Object = MibTableColumn
csuCVEvent = _CsuCVEvent_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 9, 1, 7),
    _CsuCVEvent_Type()
)
csuCVEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuCVEvent.setStatus("mandatory")


class _CsuCSEvent_Type(Integer32):
    """Custom type csuCSEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csuNoErrors", 1),
          ("csuOneOrMore", 2))
    )


_CsuCSEvent_Type.__name__ = "Integer32"
_CsuCSEvent_Object = MibTableColumn
csuCSEvent = _CsuCSEvent_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 9, 1, 8),
    _CsuCSEvent_Type()
)
csuCSEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuCSEvent.setStatus("mandatory")


class _CsuAPLoop_Type(Integer32):
    """Custom type csuAPLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csuInPayload", 2),
          ("csuNoErrors", 1))
    )


_CsuAPLoop_Type.__name__ = "Integer32"
_CsuAPLoop_Object = MibTableColumn
csuAPLoop = _CsuAPLoop_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 9, 1, 9),
    _CsuAPLoop_Type()
)
csuAPLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuAPLoop.setStatus("mandatory")
_CsuCurrentStatsTable_Object = MibTable
csuCurrentStatsTable = _CsuCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 10)
)
if mibBuilder.loadTexts:
    csuCurrentStatsTable.setStatus("mandatory")
_CsuCurrentStatsEntry_Object = MibTableRow
csuCurrentStatsEntry = _CsuCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 10, 1)
)
csuCurrentStatsEntry.setIndexNames(
    (0, "GDCDS1-MIB", "csuCurrentIndex"),
)
if mibBuilder.loadTexts:
    csuCurrentStatsEntry.setStatus("mandatory")
_CsuCurrentIndex_Type = Integer32
_CsuCurrentIndex_Object = MibTableColumn
csuCurrentIndex = _CsuCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 10, 1, 1),
    _CsuCurrentIndex_Type()
)
csuCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuCurrentIndex.setStatus("mandatory")
_CsuCurrentLOFC_Type = Gauge32
_CsuCurrentLOFC_Object = MibTableColumn
csuCurrentLOFC = _CsuCurrentLOFC_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 10, 1, 2),
    _CsuCurrentLOFC_Type()
)
csuCurrentLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuCurrentLOFC.setStatus("mandatory")
_CsuIntervalStatsTable_Object = MibTable
csuIntervalStatsTable = _CsuIntervalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 11)
)
if mibBuilder.loadTexts:
    csuIntervalStatsTable.setStatus("mandatory")
_CsuIntervalStatsEntry_Object = MibTableRow
csuIntervalStatsEntry = _CsuIntervalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 11, 1)
)
csuIntervalStatsEntry.setIndexNames(
    (0, "GDCDS1-MIB", "csuIntervalIndex"),
    (0, "GDCDS1-MIB", "csuIntervalNumber"),
)
if mibBuilder.loadTexts:
    csuIntervalStatsEntry.setStatus("mandatory")
_CsuIntervalIndex_Type = Integer32
_CsuIntervalIndex_Object = MibTableColumn
csuIntervalIndex = _CsuIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 11, 1, 1),
    _CsuIntervalIndex_Type()
)
csuIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuIntervalIndex.setStatus("mandatory")


class _CsuIntervalNumber_Type(Integer32):
    """Custom type csuIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CsuIntervalNumber_Type.__name__ = "Integer32"
_CsuIntervalNumber_Object = MibTableColumn
csuIntervalNumber = _CsuIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 11, 1, 2),
    _CsuIntervalNumber_Type()
)
csuIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuIntervalNumber.setStatus("mandatory")
_CsuIntervalLOFC_Type = Gauge32
_CsuIntervalLOFC_Object = MibTableColumn
csuIntervalLOFC = _CsuIntervalLOFC_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 11, 1, 3),
    _CsuIntervalLOFC_Type()
)
csuIntervalLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuIntervalLOFC.setStatus("mandatory")
_CsuTotalStatsTable_Object = MibTable
csuTotalStatsTable = _CsuTotalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 12)
)
if mibBuilder.loadTexts:
    csuTotalStatsTable.setStatus("mandatory")
_CsuTotalStatsEntry_Object = MibTableRow
csuTotalStatsEntry = _CsuTotalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 12, 1)
)
csuTotalStatsEntry.setIndexNames(
    (0, "GDCDS1-MIB", "csuTotalIndex"),
)
if mibBuilder.loadTexts:
    csuTotalStatsEntry.setStatus("mandatory")
_CsuTotalIndex_Type = Integer32
_CsuTotalIndex_Object = MibTableColumn
csuTotalIndex = _CsuTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 12, 1, 1),
    _CsuTotalIndex_Type()
)
csuTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuTotalIndex.setStatus("mandatory")
_CsuTotalLOFC_Type = Gauge32
_CsuTotalLOFC_Object = MibTableColumn
csuTotalLOFC = _CsuTotalLOFC_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 12, 1, 2),
    _CsuTotalLOFC_Type()
)
csuTotalLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuTotalLOFC.setStatus("mandatory")
_CsuFarEndCurrentStatsTable_Object = MibTable
csuFarEndCurrentStatsTable = _CsuFarEndCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 13)
)
if mibBuilder.loadTexts:
    csuFarEndCurrentStatsTable.setStatus("mandatory")
_CsuFarEndCurrentStatsEntry_Object = MibTableRow
csuFarEndCurrentStatsEntry = _CsuFarEndCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 13, 1)
)
csuFarEndCurrentStatsEntry.setIndexNames(
    (0, "GDCDS1-MIB", "csuFarEndCurrentIndex"),
)
if mibBuilder.loadTexts:
    csuFarEndCurrentStatsEntry.setStatus("mandatory")
_CsuFarEndCurrentIndex_Type = Integer32
_CsuFarEndCurrentIndex_Object = MibTableColumn
csuFarEndCurrentIndex = _CsuFarEndCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 13, 1, 1),
    _CsuFarEndCurrentIndex_Type()
)
csuFarEndCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuFarEndCurrentIndex.setStatus("mandatory")
_CsuFarEndCurrentLOFC_Type = Gauge32
_CsuFarEndCurrentLOFC_Object = MibTableColumn
csuFarEndCurrentLOFC = _CsuFarEndCurrentLOFC_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 13, 1, 2),
    _CsuFarEndCurrentLOFC_Type()
)
csuFarEndCurrentLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuFarEndCurrentLOFC.setStatus("mandatory")
_CsuFarEndIntervalStatsTable_Object = MibTable
csuFarEndIntervalStatsTable = _CsuFarEndIntervalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 14)
)
if mibBuilder.loadTexts:
    csuFarEndIntervalStatsTable.setStatus("mandatory")
_CsuFarEndIntervalStatsEntry_Object = MibTableRow
csuFarEndIntervalStatsEntry = _CsuFarEndIntervalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 14, 1)
)
csuFarEndIntervalStatsEntry.setIndexNames(
    (0, "GDCDS1-MIB", "csuFarEndIntervalIndex"),
    (0, "GDCDS1-MIB", "csuFarEndIntervalNumber"),
)
if mibBuilder.loadTexts:
    csuFarEndIntervalStatsEntry.setStatus("mandatory")
_CsuFarEndIntervalIndex_Type = Integer32
_CsuFarEndIntervalIndex_Object = MibTableColumn
csuFarEndIntervalIndex = _CsuFarEndIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 14, 1, 1),
    _CsuFarEndIntervalIndex_Type()
)
csuFarEndIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuFarEndIntervalIndex.setStatus("mandatory")


class _CsuFarEndIntervalNumber_Type(Integer32):
    """Custom type csuFarEndIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CsuFarEndIntervalNumber_Type.__name__ = "Integer32"
_CsuFarEndIntervalNumber_Object = MibTableColumn
csuFarEndIntervalNumber = _CsuFarEndIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 14, 1, 2),
    _CsuFarEndIntervalNumber_Type()
)
csuFarEndIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuFarEndIntervalNumber.setStatus("mandatory")
_CsuFarEndIntervalLOFC_Type = Gauge32
_CsuFarEndIntervalLOFC_Object = MibTableColumn
csuFarEndIntervalLOFC = _CsuFarEndIntervalLOFC_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 14, 1, 3),
    _CsuFarEndIntervalLOFC_Type()
)
csuFarEndIntervalLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuFarEndIntervalLOFC.setStatus("mandatory")
_CsuFarEndTotalStatsTable_Object = MibTable
csuFarEndTotalStatsTable = _CsuFarEndTotalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 15)
)
if mibBuilder.loadTexts:
    csuFarEndTotalStatsTable.setStatus("mandatory")
_CsuFarEndTotalStatsEntry_Object = MibTableRow
csuFarEndTotalStatsEntry = _CsuFarEndTotalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 15, 1)
)
csuFarEndTotalStatsEntry.setIndexNames(
    (0, "GDCDS1-MIB", "csuFarEndTotalIndex"),
)
if mibBuilder.loadTexts:
    csuFarEndTotalStatsEntry.setStatus("mandatory")
_CsuFarEndTotalIndex_Type = Integer32
_CsuFarEndTotalIndex_Object = MibTableColumn
csuFarEndTotalIndex = _CsuFarEndTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 15, 1, 1),
    _CsuFarEndTotalIndex_Type()
)
csuFarEndTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuFarEndTotalIndex.setStatus("mandatory")
_CsuFarEndTotalLOFC_Type = Gauge32
_CsuFarEndTotalLOFC_Object = MibTableColumn
csuFarEndTotalLOFC = _CsuFarEndTotalLOFC_Object(
    (1, 3, 6, 1, 4, 1, 498, 2, 15, 1, 2),
    _CsuFarEndTotalLOFC_Type()
)
csuFarEndTotalLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csuFarEndTotalLOFC.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GDCDS1-MIB",
    **{"gdc": gdc,
       "csu": csu,
       "csuConfigTable": csuConfigTable,
       "csuConfigEntry": csuConfigEntry,
       "csuConfigLineIndex": csuConfigLineIndex,
       "csuOnesDensity": csuOnesDensity,
       "csuFrontPanel": csuFrontPanel,
       "csuInbandLoop": csuInbandLoop,
       "csuILBFrame": csuILBFrame,
       "csuLineBuildOutCtrl": csuLineBuildOutCtrl,
       "csuLineBuildOutValue": csuLineBuildOutValue,
       "csuLineTypeCtrl": csuLineTypeCtrl,
       "csuAISLoopdown": csuAISLoopdown,
       "csuPreEqualizer": csuPreEqualizer,
       "csuInitialize": csuInitialize,
       "csuTime": csuTime,
       "csuDate": csuDate,
       "csuTestType": csuTestType,
       "csuReceiveLevel": csuReceiveLevel,
       "csuChanConfigTable": csuChanConfigTable,
       "csuChanConfigEntry": csuChanConfigEntry,
       "csuChanConfigLineIndex": csuChanConfigLineIndex,
       "csuChanConfigNum": csuChanConfigNum,
       "csuStartDS0": csuStartDS0,
       "csuRTSCTS": csuRTSCTS,
       "csuControlModeIdle": csuControlModeIdle,
       "csuRDLInbandCode": csuRDLInbandCode,
       "csuChanRate": csuChanRate,
       "csuAlternateDS0": csuAlternateDS0,
       "csuRespondRDL": csuRespondRDL,
       "csuInbandDLTimeout": csuInbandDLTimeout,
       "csuChanStatus": csuChanStatus,
       "csuChan6456": csuChan6456,
       "csuIndicatorTable": csuIndicatorTable,
       "csuIndicatorEntry": csuIndicatorEntry,
       "csuIndicatorIndex": csuIndicatorIndex,
       "csuIndicatorOOF": csuIndicatorOOF,
       "csuIndicatorNNS": csuIndicatorNNS,
       "csuIndicatorYEL": csuIndicatorYEL,
       "csuIndicatorAIS": csuIndicatorAIS,
       "csuIndicatorNLB": csuIndicatorNLB,
       "csuIndicatorBPV": csuIndicatorBPV,
       "csuIndicatorCRC": csuIndicatorCRC,
       "csuIndicatorTSY": csuIndicatorTSY,
       "csuIndicatorTNS": csuIndicatorTNS,
       "csuIndicatorOS": csuIndicatorOS,
       "csuIndicatorLAD": csuIndicatorLAD,
       "csuIndicatorCascadeOOF": csuIndicatorCascadeOOF,
       "csuIndicatorCascadeNS": csuIndicatorCascadeNS,
       "csuIndicatorNetworkLT": csuIndicatorNetworkLT,
       "csuIndicatorNetworkST": csuIndicatorNetworkST,
       "csuIndicatorNetworkRT": csuIndicatorNetworkRT,
       "csuIndicatorChannelRDL": csuIndicatorChannelRDL,
       "csuIndicatorChannelST": csuIndicatorChannelST,
       "csuIndicatorChannelDL": csuIndicatorChannelDL,
       "csuIndicatorChannelLL": csuIndicatorChannelLL,
       "csuIndicatorMode": csuIndicatorMode,
       "csuIndicatorDS0LB": csuIndicatorDS0LB,
       "csuSelftestDiagTable": csuSelftestDiagTable,
       "csuSelftestDiagEntry": csuSelftestDiagEntry,
       "csuSelftestDiagLineIndex": csuSelftestDiagLineIndex,
       "csuDiagSelftest": csuDiagSelftest,
       "csuGDCSelftestPattern": csuGDCSelftestPattern,
       "csuSelftestUserPattern": csuSelftestUserPattern,
       "csuSelftestFrame": csuSelftestFrame,
       "csuSelftestResults": csuSelftestResults,
       "csuSelftestTime": csuSelftestTime,
       "csuLoopbackDiagTable": csuLoopbackDiagTable,
       "csuLoopbackDiagEntry": csuLoopbackDiagEntry,
       "csuLoopbackDiagLineIndex": csuLoopbackDiagLineIndex,
       "csuGDCLoopback": csuGDCLoopback,
       "csuDS0DiagTable": csuDS0DiagTable,
       "csuDS0DiagEntry": csuDS0DiagEntry,
       "csuDS0LineIndex": csuDS0LineIndex,
       "csuDS0Num": csuDS0Num,
       "csuTestPattern": csuTestPattern,
       "csuResetResults": csuResetResults,
       "csuBERtest": csuBERtest,
       "csuCumErrs": csuCumErrs,
       "csuDataBlocks": csuDataBlocks,
       "csuCircuitDelayCtrl": csuCircuitDelayCtrl,
       "csuCircuitDelayResult": csuCircuitDelayResult,
       "csuLBtest": csuLBtest,
       "csuChanDiagTable": csuChanDiagTable,
       "csuChanDiagEntry": csuChanDiagEntry,
       "csuChanLineIndex": csuChanLineIndex,
       "csuChanNum": csuChanNum,
       "csuChanSelftest": csuChanSelftest,
       "csuChanLoopback": csuChanLoopback,
       "csuChanSelftestStatus": csuChanSelftestStatus,
       "csuAlarmHistoryTable": csuAlarmHistoryTable,
       "csuAlarmHistoryEntry": csuAlarmHistoryEntry,
       "csuAlarmHistoryIndex": csuAlarmHistoryIndex,
       "csuAlarmType": csuAlarmType,
       "csuAlarmHistoryStart": csuAlarmHistoryStart,
       "csuCount": csuCount,
       "csuFirstOccur": csuFirstOccur,
       "csuLastOccur": csuLastOccur,
       "csuSchedPerfRprtTable": csuSchedPerfRprtTable,
       "csuSchedPerfRprtEntry": csuSchedPerfRprtEntry,
       "csuSchedPerfRprtIndex": csuSchedPerfRprtIndex,
       "csuPerfRprtIntervalNumber": csuPerfRprtIntervalNumber,
       "csuPerfRprtMsg": csuPerfRprtMsg,
       "csuCRCErrEvent": csuCRCErrEvent,
       "csuSEEvent": csuSEEvent,
       "csuFEEvent": csuFEEvent,
       "csuCVEvent": csuCVEvent,
       "csuCSEvent": csuCSEvent,
       "csuAPLoop": csuAPLoop,
       "csuCurrentStatsTable": csuCurrentStatsTable,
       "csuCurrentStatsEntry": csuCurrentStatsEntry,
       "csuCurrentIndex": csuCurrentIndex,
       "csuCurrentLOFC": csuCurrentLOFC,
       "csuIntervalStatsTable": csuIntervalStatsTable,
       "csuIntervalStatsEntry": csuIntervalStatsEntry,
       "csuIntervalIndex": csuIntervalIndex,
       "csuIntervalNumber": csuIntervalNumber,
       "csuIntervalLOFC": csuIntervalLOFC,
       "csuTotalStatsTable": csuTotalStatsTable,
       "csuTotalStatsEntry": csuTotalStatsEntry,
       "csuTotalIndex": csuTotalIndex,
       "csuTotalLOFC": csuTotalLOFC,
       "csuFarEndCurrentStatsTable": csuFarEndCurrentStatsTable,
       "csuFarEndCurrentStatsEntry": csuFarEndCurrentStatsEntry,
       "csuFarEndCurrentIndex": csuFarEndCurrentIndex,
       "csuFarEndCurrentLOFC": csuFarEndCurrentLOFC,
       "csuFarEndIntervalStatsTable": csuFarEndIntervalStatsTable,
       "csuFarEndIntervalStatsEntry": csuFarEndIntervalStatsEntry,
       "csuFarEndIntervalIndex": csuFarEndIntervalIndex,
       "csuFarEndIntervalNumber": csuFarEndIntervalNumber,
       "csuFarEndIntervalLOFC": csuFarEndIntervalLOFC,
       "csuFarEndTotalStatsTable": csuFarEndTotalStatsTable,
       "csuFarEndTotalStatsEntry": csuFarEndTotalStatsEntry,
       "csuFarEndTotalIndex": csuFarEndTotalIndex,
       "csuFarEndTotalLOFC": csuFarEndTotalLOFC}
)
