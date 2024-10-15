# SNMP MIB module (SNMP540-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNMP540-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:12 2024
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

(dsu,) = mibBuilder.importSymbols(
    "DDS-MIB",
    "dsu")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Snmp540_ObjectIdentity = ObjectIdentity
snmp540 = _Snmp540_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4)
)


class _Snmp540MIBversion_Type(DisplayString):
    """Custom type snmp540MIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Snmp540MIBversion_Type.__name__ = "DisplayString"
_Snmp540MIBversion_Object = MibScalar
snmp540MIBversion = _Snmp540MIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 1),
    _Snmp540MIBversion_Type()
)
snmp540MIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp540MIBversion.setStatus("mandatory")
_Snmp540Config_ObjectIdentity = ObjectIdentity
snmp540Config = _Snmp540Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 2)
)


class _Snmp540ActivateCfg_Type(Integer32):
    """Custom type snmp540ActivateCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activateNewCfg", 2),
          ("noChange", 1))
    )


_Snmp540ActivateCfg_Type.__name__ = "Integer32"
_Snmp540ActivateCfg_Object = MibScalar
snmp540ActivateCfg = _Snmp540ActivateCfg_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 2, 1),
    _Snmp540ActivateCfg_Type()
)
snmp540ActivateCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp540ActivateCfg.setStatus("mandatory")


class _Snmp540DtePortType_Type(Integer32):
    """Custom type snmp540DtePortType based on Integer32"""
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
          ("rs232", 1),
          ("v35", 2))
    )


_Snmp540DtePortType_Type.__name__ = "Integer32"
_Snmp540DtePortType_Object = MibScalar
snmp540DtePortType = _Snmp540DtePortType_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 2, 2),
    _Snmp540DtePortType_Type()
)
snmp540DtePortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp540DtePortType.setStatus("mandatory")
_Snmp540EiaTestControl_ObjectIdentity = ObjectIdentity
snmp540EiaTestControl = _Snmp540EiaTestControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 2, 3)
)


class _Snmp540EiaRlcontrol_Type(Integer32):
    """Custom type snmp540EiaRlcontrol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("block", 2))
    )


_Snmp540EiaRlcontrol_Type.__name__ = "Integer32"
_Snmp540EiaRlcontrol_Object = MibScalar
snmp540EiaRlcontrol = _Snmp540EiaRlcontrol_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 2, 3, 1),
    _Snmp540EiaRlcontrol_Type()
)
snmp540EiaRlcontrol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp540EiaRlcontrol.setStatus("mandatory")


class _Snmp540EiaLlcontrol_Type(Integer32):
    """Custom type snmp540EiaLlcontrol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("block", 2))
    )


_Snmp540EiaLlcontrol_Type.__name__ = "Integer32"
_Snmp540EiaLlcontrol_Object = MibScalar
snmp540EiaLlcontrol = _Snmp540EiaLlcontrol_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 2, 3, 2),
    _Snmp540EiaLlcontrol_Type()
)
snmp540EiaLlcontrol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp540EiaLlcontrol.setStatus("mandatory")


class _Snmp540EiaTmcontrol_Type(Integer32):
    """Custom type snmp540EiaTmcontrol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("block", 2))
    )


_Snmp540EiaTmcontrol_Type.__name__ = "Integer32"
_Snmp540EiaTmcontrol_Object = MibScalar
snmp540EiaTmcontrol = _Snmp540EiaTmcontrol_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 2, 3, 3),
    _Snmp540EiaTmcontrol_Type()
)
snmp540EiaTmcontrol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp540EiaTmcontrol.setStatus("mandatory")


class _Snmp540LlbDetect_Type(Integer32):
    """Custom type snmp540LlbDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("block", 2))
    )


_Snmp540LlbDetect_Type.__name__ = "Integer32"
_Snmp540LlbDetect_Object = MibScalar
snmp540LlbDetect = _Snmp540LlbDetect_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 2, 3, 4),
    _Snmp540LlbDetect_Type()
)
snmp540LlbDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp540LlbDetect.setStatus("mandatory")
_Snmp540Control_ObjectIdentity = ObjectIdentity
snmp540Control = _Snmp540Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 3)
)


class _Snmp540UnitReset_Type(Integer32):
    """Custom type snmp540UnitReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_Snmp540UnitReset_Type.__name__ = "Integer32"
_Snmp540UnitReset_Object = MibScalar
snmp540UnitReset = _Snmp540UnitReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 3, 1),
    _Snmp540UnitReset_Type()
)
snmp540UnitReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp540UnitReset.setStatus("mandatory")
_Snmp540AlarmData_ObjectIdentity = ObjectIdentity
snmp540AlarmData = _Snmp540AlarmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 4)
)
_Snmp540PowerUpAlm_ObjectIdentity = ObjectIdentity
snmp540PowerUpAlm = _Snmp540PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 4, 1)
)
_Snmp540CfgChkSumErrAlm_ObjectIdentity = ObjectIdentity
snmp540CfgChkSumErrAlm = _Snmp540CfgChkSumErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 4, 2)
)
_Snmp540StcLoopbackAlm_ObjectIdentity = ObjectIdentity
snmp540StcLoopbackAlm = _Snmp540StcLoopbackAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 4, 3)
)
_Snmp540NoNtwkLoopCurrentAlm_ObjectIdentity = ObjectIdentity
snmp540NoNtwkLoopCurrentAlm = _Snmp540NoNtwkLoopCurrentAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 4, 4)
)
_Snmp540LinePairsReversedAlm_ObjectIdentity = ObjectIdentity
snmp540LinePairsReversedAlm = _Snmp540LinePairsReversedAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 4, 5)
)
_Snmp540NoSignalAlm_ObjectIdentity = ObjectIdentity
snmp540NoSignalAlm = _Snmp540NoSignalAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 4, 6)
)
_Snmp540FpTestAlm_ObjectIdentity = ObjectIdentity
snmp540FpTestAlm = _Snmp540FpTestAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 4, 7)
)
_Snmp540DSRLossAlm_ObjectIdentity = ObjectIdentity
snmp540DSRLossAlm = _Snmp540DSRLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 4, 8)
)
_Snmp540DTRLossAlm_ObjectIdentity = ObjectIdentity
snmp540DTRLossAlm = _Snmp540DTRLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 4, 9)
)
_Snmp540DTPLossAlm_ObjectIdentity = ObjectIdentity
snmp540DTPLossAlm = _Snmp540DTPLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 4, 10)
)
_Snmp540DCDLossAlm_ObjectIdentity = ObjectIdentity
snmp540DCDLossAlm = _Snmp540DCDLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 4, 11)
)
_Snmp540RXDLossAlm_ObjectIdentity = ObjectIdentity
snmp540RXDLossAlm = _Snmp540RXDLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 4, 12)
)
_Snmp540TXDLossAlm_ObjectIdentity = ObjectIdentity
snmp540TXDLossAlm = _Snmp540TXDLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 4, 13)
)
_Snmp540JitterAlm_ObjectIdentity = ObjectIdentity
snmp540JitterAlm = _Snmp540JitterAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 4, 14)
)
_Snmp540BpvAlm_ObjectIdentity = ObjectIdentity
snmp540BpvAlm = _Snmp540BpvAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 4, 15)
)
_Snmp540FrameLossAlm_ObjectIdentity = ObjectIdentity
snmp540FrameLossAlm = _Snmp540FrameLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 4, 16)
)
_Snmp540SignalToNoiseAlm_ObjectIdentity = ObjectIdentity
snmp540SignalToNoiseAlm = _Snmp540SignalToNoiseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 4, 17)
)
_Snmp540RxSignalLowAlm_ObjectIdentity = ObjectIdentity
snmp540RxSignalLowAlm = _Snmp540RxSignalLowAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 4, 18)
)
_Snmp540AlarmCfgThr_ObjectIdentity = ObjectIdentity
snmp540AlarmCfgThr = _Snmp540AlarmCfgThr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 5)
)


class _Snmp540AlarmCfgCountWindow_Type(Integer32):
    """Custom type snmp540AlarmCfgCountWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Snmp540AlarmCfgCountWindow_Type.__name__ = "Integer32"
_Snmp540AlarmCfgCountWindow_Object = MibScalar
snmp540AlarmCfgCountWindow = _Snmp540AlarmCfgCountWindow_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 5, 1),
    _Snmp540AlarmCfgCountWindow_Type()
)
snmp540AlarmCfgCountWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp540AlarmCfgCountWindow.setStatus("mandatory")
_Snmp540AlarmCfgTable_Object = MibTable
snmp540AlarmCfgTable = _Snmp540AlarmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 5, 2)
)
if mibBuilder.loadTexts:
    snmp540AlarmCfgTable.setStatus("mandatory")
_Snmp540AlarmCfgEntry_Object = MibTableRow
snmp540AlarmCfgEntry = _Snmp540AlarmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 5, 2, 1)
)
snmp540AlarmCfgEntry.setIndexNames(
    (0, "SNMP540-MGMT-MIB", "snmp540AlarmCfgIdentifier"),
)
if mibBuilder.loadTexts:
    snmp540AlarmCfgEntry.setStatus("mandatory")
_Snmp540AlarmCfgIdentifier_Type = ObjectIdentifier
_Snmp540AlarmCfgIdentifier_Object = MibTableColumn
snmp540AlarmCfgIdentifier = _Snmp540AlarmCfgIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 5, 2, 1, 1),
    _Snmp540AlarmCfgIdentifier_Type()
)
snmp540AlarmCfgIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp540AlarmCfgIdentifier.setStatus("mandatory")


class _Snmp540AlarmCfgThreshold_Type(Integer32):
    """Custom type snmp540AlarmCfgThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 99),
    )


_Snmp540AlarmCfgThreshold_Type.__name__ = "Integer32"
_Snmp540AlarmCfgThreshold_Object = MibTableColumn
snmp540AlarmCfgThreshold = _Snmp540AlarmCfgThreshold_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 5, 2, 1, 2),
    _Snmp540AlarmCfgThreshold_Type()
)
snmp540AlarmCfgThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp540AlarmCfgThreshold.setStatus("mandatory")
_Snmp540LineStats_ObjectIdentity = ObjectIdentity
snmp540LineStats = _Snmp540LineStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 6)
)


class _Snmp540LineStatsInterval_Type(Integer32):
    """Custom type snmp540LineStatsInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Snmp540LineStatsInterval_Type.__name__ = "Integer32"
_Snmp540LineStatsInterval_Object = MibScalar
snmp540LineStatsInterval = _Snmp540LineStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 6, 1),
    _Snmp540LineStatsInterval_Type()
)
snmp540LineStatsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp540LineStatsInterval.setStatus("mandatory")


class _Snmp540LineStatsTxLevel_Type(Integer32):
    """Custom type snmp540LineStatsTxLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Snmp540LineStatsTxLevel_Type.__name__ = "Integer32"
_Snmp540LineStatsTxLevel_Object = MibScalar
snmp540LineStatsTxLevel = _Snmp540LineStatsTxLevel_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 6, 2),
    _Snmp540LineStatsTxLevel_Type()
)
snmp540LineStatsTxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp540LineStatsTxLevel.setStatus("mandatory")


class _Snmp540LineStatsRxInterpretation_Type(Integer32):
    """Custom type snmp540LineStatsRxInterpretation based on Integer32"""
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
        *(("allReadingsValid", 4),
          ("noSignal", 1),
          ("notAvailable", 2),
          ("sToNRatioGreaterThanMeasured", 5),
          ("signalToNoiseNotMeasured", 3))
    )


_Snmp540LineStatsRxInterpretation_Type.__name__ = "Integer32"
_Snmp540LineStatsRxInterpretation_Object = MibScalar
snmp540LineStatsRxInterpretation = _Snmp540LineStatsRxInterpretation_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 6, 3),
    _Snmp540LineStatsRxInterpretation_Type()
)
snmp540LineStatsRxInterpretation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp540LineStatsRxInterpretation.setStatus("mandatory")


class _Snmp540LineStatsRxLevel_Type(Integer32):
    """Custom type snmp540LineStatsRxLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 6),
    )


_Snmp540LineStatsRxLevel_Type.__name__ = "Integer32"
_Snmp540LineStatsRxLevel_Object = MibScalar
snmp540LineStatsRxLevel = _Snmp540LineStatsRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 6, 4),
    _Snmp540LineStatsRxLevel_Type()
)
snmp540LineStatsRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp540LineStatsRxLevel.setStatus("mandatory")


class _Snmp540LineStatsSignalToNoiseRatio_Type(Integer32):
    """Custom type snmp540LineStatsSignalToNoiseRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_Snmp540LineStatsSignalToNoiseRatio_Type.__name__ = "Integer32"
_Snmp540LineStatsSignalToNoiseRatio_Object = MibScalar
snmp540LineStatsSignalToNoiseRatio = _Snmp540LineStatsSignalToNoiseRatio_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 6, 5),
    _Snmp540LineStatsSignalToNoiseRatio_Type()
)
snmp540LineStatsSignalToNoiseRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp540LineStatsSignalToNoiseRatio.setStatus("mandatory")


class _Snmp540LineStatsSignalQuality_Type(Integer32):
    """Custom type snmp540LineStatsSignalQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bad", 3),
          ("fair", 2),
          ("good", 1))
    )


_Snmp540LineStatsSignalQuality_Type.__name__ = "Integer32"
_Snmp540LineStatsSignalQuality_Object = MibScalar
snmp540LineStatsSignalQuality = _Snmp540LineStatsSignalQuality_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 6, 6),
    _Snmp540LineStatsSignalQuality_Type()
)
snmp540LineStatsSignalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp540LineStatsSignalQuality.setStatus("mandatory")


class _Snmp540LineStatsJitter_Type(Integer32):
    """Custom type snmp540LineStatsJitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Snmp540LineStatsJitter_Type.__name__ = "Integer32"
_Snmp540LineStatsJitter_Object = MibScalar
snmp540LineStatsJitter = _Snmp540LineStatsJitter_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 6, 7),
    _Snmp540LineStatsJitter_Type()
)
snmp540LineStatsJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp540LineStatsJitter.setStatus("mandatory")


class _Snmp540LineStatsBpvCount_Type(Integer32):
    """Custom type snmp540LineStatsBpvCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Snmp540LineStatsBpvCount_Type.__name__ = "Integer32"
_Snmp540LineStatsBpvCount_Object = MibScalar
snmp540LineStatsBpvCount = _Snmp540LineStatsBpvCount_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 6, 8),
    _Snmp540LineStatsBpvCount_Type()
)
snmp540LineStatsBpvCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp540LineStatsBpvCount.setStatus("mandatory")


class _Snmp540LineStatsFrameLossCount_Type(Integer32):
    """Custom type snmp540LineStatsFrameLossCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Snmp540LineStatsFrameLossCount_Type.__name__ = "Integer32"
_Snmp540LineStatsFrameLossCount_Object = MibScalar
snmp540LineStatsFrameLossCount = _Snmp540LineStatsFrameLossCount_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 6, 9),
    _Snmp540LineStatsFrameLossCount_Type()
)
snmp540LineStatsFrameLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp540LineStatsFrameLossCount.setStatus("mandatory")
_Snmp540DiagTest_ObjectIdentity = ObjectIdentity
snmp540DiagTest = _Snmp540DiagTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 7)
)


class _Snmp540DiagTestPattern_Type(Integer32):
    """Custom type snmp540DiagTestPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmp540Send15BitPattern", 3),
          ("snmp540Send2047Pattern", 2),
          ("snmp540Send511Pattern", 1))
    )


_Snmp540DiagTestPattern_Type.__name__ = "Integer32"
_Snmp540DiagTestPattern_Object = MibScalar
snmp540DiagTestPattern = _Snmp540DiagTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 7, 1),
    _Snmp540DiagTestPattern_Type()
)
snmp540DiagTestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp540DiagTestPattern.setStatus("mandatory")


class _Snmp540DiagTestExceptions_Type(Integer32):
    """Custom type snmp540DiagTestExceptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bitsOutOfRange", 2),
          ("noExceptions", 1))
    )


_Snmp540DiagTestExceptions_Type.__name__ = "Integer32"
_Snmp540DiagTestExceptions_Object = MibScalar
snmp540DiagTestExceptions = _Snmp540DiagTestExceptions_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 7, 2),
    _Snmp540DiagTestExceptions_Type()
)
snmp540DiagTestExceptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp540DiagTestExceptions.setStatus("mandatory")
_Snmp540DiagBitErrors_Type = Integer32
_Snmp540DiagBitErrors_Object = MibScalar
snmp540DiagBitErrors = _Snmp540DiagBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 7, 3),
    _Snmp540DiagBitErrors_Type()
)
snmp540DiagBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp540DiagBitErrors.setStatus("mandatory")
_Snmp540DiagBlockErrors_Type = Integer32
_Snmp540DiagBlockErrors_Object = MibScalar
snmp540DiagBlockErrors = _Snmp540DiagBlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 7, 4),
    _Snmp540DiagBlockErrors_Type()
)
snmp540DiagBlockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp540DiagBlockErrors.setStatus("mandatory")


class _Snmp540RlLoopType_Type(Integer32):
    """Custom type snmp540RlLoopType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pn127", 1),
          ("v54", 2))
    )


_Snmp540RlLoopType_Type.__name__ = "Integer32"
_Snmp540RlLoopType_Object = MibScalar
snmp540RlLoopType = _Snmp540RlLoopType_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 7, 5),
    _Snmp540RlLoopType_Type()
)
snmp540RlLoopType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp540RlLoopType.setStatus("mandatory")


class _Snmp540DiagBlocksToSend_Type(Integer32):
    """Custom type snmp540DiagBlocksToSend based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("blocks1", 1),
          ("blocks10", 2),
          ("blocks100", 3),
          ("blocks1000", 5),
          ("blocks10000", 7),
          ("blocks500", 4),
          ("blocks5000", 6),
          ("blocks50000", 8),
          ("external", 9))
    )


_Snmp540DiagBlocksToSend_Type.__name__ = "Integer32"
_Snmp540DiagBlocksToSend_Object = MibScalar
snmp540DiagBlocksToSend = _Snmp540DiagBlocksToSend_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 7, 6),
    _Snmp540DiagBlocksToSend_Type()
)
snmp540DiagBlocksToSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp540DiagBlocksToSend.setStatus("mandatory")


class _Snmp540DiagControl_Type(Integer32):
    """Custom type snmp540DiagControl based on Integer32"""
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
        *(("lineloop", 2),
          ("noTest", 1),
          ("remoteLoop", 3),
          ("resetTestToNorm", 4),
          ("telcoLoop", 5))
    )


_Snmp540DiagControl_Type.__name__ = "Integer32"
_Snmp540DiagControl_Object = MibScalar
snmp540DiagControl = _Snmp540DiagControl_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 7, 7),
    _Snmp540DiagControl_Type()
)
snmp540DiagControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp540DiagControl.setStatus("mandatory")
_Snmp540Led_ObjectIdentity = ObjectIdentity
snmp540Led = _Snmp540Led_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 8)
)


class _Snmp540LedStatus_Type(OctetString):
    """Custom type snmp540LedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Snmp540LedStatus_Type.__name__ = "OctetString"
_Snmp540LedStatus_Object = MibScalar
snmp540LedStatus = _Snmp540LedStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 8, 1),
    _Snmp540LedStatus_Type()
)
snmp540LedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp540LedStatus.setStatus("mandatory")


class _Snmp540DeviceSerialNumber_Type(OctetString):
    """Custom type snmp540DeviceSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Snmp540DeviceSerialNumber_Type.__name__ = "OctetString"
_Snmp540DeviceSerialNumber_Object = MibScalar
snmp540DeviceSerialNumber = _Snmp540DeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 4, 9),
    _Snmp540DeviceSerialNumber_Type()
)
snmp540DeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp540DeviceSerialNumber.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMP540-MGMT-MIB",
    **{"snmp540": snmp540,
       "snmp540MIBversion": snmp540MIBversion,
       "snmp540Config": snmp540Config,
       "snmp540ActivateCfg": snmp540ActivateCfg,
       "snmp540DtePortType": snmp540DtePortType,
       "snmp540EiaTestControl": snmp540EiaTestControl,
       "snmp540EiaRlcontrol": snmp540EiaRlcontrol,
       "snmp540EiaLlcontrol": snmp540EiaLlcontrol,
       "snmp540EiaTmcontrol": snmp540EiaTmcontrol,
       "snmp540LlbDetect": snmp540LlbDetect,
       "snmp540Control": snmp540Control,
       "snmp540UnitReset": snmp540UnitReset,
       "snmp540AlarmData": snmp540AlarmData,
       "snmp540PowerUpAlm": snmp540PowerUpAlm,
       "snmp540CfgChkSumErrAlm": snmp540CfgChkSumErrAlm,
       "snmp540StcLoopbackAlm": snmp540StcLoopbackAlm,
       "snmp540NoNtwkLoopCurrentAlm": snmp540NoNtwkLoopCurrentAlm,
       "snmp540LinePairsReversedAlm": snmp540LinePairsReversedAlm,
       "snmp540NoSignalAlm": snmp540NoSignalAlm,
       "snmp540FpTestAlm": snmp540FpTestAlm,
       "snmp540DSRLossAlm": snmp540DSRLossAlm,
       "snmp540DTRLossAlm": snmp540DTRLossAlm,
       "snmp540DTPLossAlm": snmp540DTPLossAlm,
       "snmp540DCDLossAlm": snmp540DCDLossAlm,
       "snmp540RXDLossAlm": snmp540RXDLossAlm,
       "snmp540TXDLossAlm": snmp540TXDLossAlm,
       "snmp540JitterAlm": snmp540JitterAlm,
       "snmp540BpvAlm": snmp540BpvAlm,
       "snmp540FrameLossAlm": snmp540FrameLossAlm,
       "snmp540SignalToNoiseAlm": snmp540SignalToNoiseAlm,
       "snmp540RxSignalLowAlm": snmp540RxSignalLowAlm,
       "snmp540AlarmCfgThr": snmp540AlarmCfgThr,
       "snmp540AlarmCfgCountWindow": snmp540AlarmCfgCountWindow,
       "snmp540AlarmCfgTable": snmp540AlarmCfgTable,
       "snmp540AlarmCfgEntry": snmp540AlarmCfgEntry,
       "snmp540AlarmCfgIdentifier": snmp540AlarmCfgIdentifier,
       "snmp540AlarmCfgThreshold": snmp540AlarmCfgThreshold,
       "snmp540LineStats": snmp540LineStats,
       "snmp540LineStatsInterval": snmp540LineStatsInterval,
       "snmp540LineStatsTxLevel": snmp540LineStatsTxLevel,
       "snmp540LineStatsRxInterpretation": snmp540LineStatsRxInterpretation,
       "snmp540LineStatsRxLevel": snmp540LineStatsRxLevel,
       "snmp540LineStatsSignalToNoiseRatio": snmp540LineStatsSignalToNoiseRatio,
       "snmp540LineStatsSignalQuality": snmp540LineStatsSignalQuality,
       "snmp540LineStatsJitter": snmp540LineStatsJitter,
       "snmp540LineStatsBpvCount": snmp540LineStatsBpvCount,
       "snmp540LineStatsFrameLossCount": snmp540LineStatsFrameLossCount,
       "snmp540DiagTest": snmp540DiagTest,
       "snmp540DiagTestPattern": snmp540DiagTestPattern,
       "snmp540DiagTestExceptions": snmp540DiagTestExceptions,
       "snmp540DiagBitErrors": snmp540DiagBitErrors,
       "snmp540DiagBlockErrors": snmp540DiagBlockErrors,
       "snmp540RlLoopType": snmp540RlLoopType,
       "snmp540DiagBlocksToSend": snmp540DiagBlocksToSend,
       "snmp540DiagControl": snmp540DiagControl,
       "snmp540Led": snmp540Led,
       "snmp540LedStatus": snmp540LedStatus,
       "snmp540DeviceSerialNumber": snmp540DeviceSerialNumber}
)
