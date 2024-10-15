# SNMP MIB module (Zhone-VOICE-ANALOG-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Zhone-VOICE-ANALOG-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:23:16 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(zhoneModules,
 zhonePhysical) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneModules",
    "zhonePhysical")

(ZhoneRowStatus,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneRowStatus")


# MODULE-IDENTITY

zhoneVoiceAnalogIf_MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 13)
)
zhoneVoiceAnalogIf_MIB.setRevisions(
        ("2009-05-05 02:36",
         "2008-03-26 17:45",
         "2007-11-01 02:30",
         "2005-09-06 11:14",
         "2005-08-08 15:00",
         "2005-05-11 15:20",
         "2005-05-02 17:22",
         "2004-10-07 11:34",
         "2001-10-10 11:19",
         "2001-02-15 18:52",
         "2000-09-12 14:21")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhoneVaIfObjects_ObjectIdentity = ObjectIdentity
zhoneVaIfObjects = _ZhoneVaIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6)
)
_ZhoneVaIfGeneralObjects_ObjectIdentity = ObjectIdentity
zhoneVaIfGeneralObjects = _ZhoneVaIfGeneralObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 1)
)
_ZhoneVaIfCfgTable_Object = MibTable
zhoneVaIfCfgTable = _ZhoneVaIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1)
)
if mibBuilder.loadTexts:
    zhoneVaIfCfgTable.setStatus("current")
_ZhoneVaIfCfgEntry_Object = MibTableRow
zhoneVaIfCfgEntry = _ZhoneVaIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1)
)
zhoneVaIfCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zhoneVaIfCfgEntry.setStatus("current")


class _ZhoneVaIfCfgImpedance_Type(Integer32):
    """Custom type zhoneVaIfCfgImpedance based on Integer32"""
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
        *(("ohms600Complex", 3),
          ("ohms600Real", 2),
          ("ohms900Complex", 4),
          ("ohmsComplex1", 5),
          ("ohmsComplex2", 6),
          ("other", 1))
    )


_ZhoneVaIfCfgImpedance_Type.__name__ = "Integer32"
_ZhoneVaIfCfgImpedance_Object = MibTableColumn
zhoneVaIfCfgImpedance = _ZhoneVaIfCfgImpedance_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1, 1),
    _ZhoneVaIfCfgImpedance_Type()
)
zhoneVaIfCfgImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfCfgImpedance.setStatus("current")


class _ZhoneVaIfCfgReceiveTLP_Type(Integer32):
    """Custom type zhoneVaIfCfgReceiveTLP based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("fxsRtlp0db", 10),
          ("fxsRtlp1db", 11),
          ("fxsRtlp2db", 12),
          ("fxsRtlp3db", 13),
          ("fxsRtlpN1db", 9),
          ("fxsRtlpN2db", 8),
          ("fxsRtlpN3db", 7),
          ("fxsRtlpN4db", 6),
          ("fxsRtlpN5db", 5),
          ("fxsRtlpN6db", 4),
          ("fxsRtlpN7db", 3),
          ("fxsRtlpN8db", 2),
          ("fxsRtlpN9db", 1),
          ("rTlpNummeric", 14))
    )


_ZhoneVaIfCfgReceiveTLP_Type.__name__ = "Integer32"
_ZhoneVaIfCfgReceiveTLP_Object = MibTableColumn
zhoneVaIfCfgReceiveTLP = _ZhoneVaIfCfgReceiveTLP_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1, 2),
    _ZhoneVaIfCfgReceiveTLP_Type()
)
zhoneVaIfCfgReceiveTLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfCfgReceiveTLP.setStatus("current")


class _ZhoneVaIfCfgTransmitTLP_Type(Integer32):
    """Custom type zhoneVaIfCfgTransmitTLP based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("fxsTtlp0db", 10),
          ("fxsTtlp1db", 9),
          ("fxsTtlp2db", 8),
          ("fxsTtlp3db", 7),
          ("fxsTtlp4db", 6),
          ("fxsTtlp5db", 5),
          ("fxsTtlp6db", 4),
          ("fxsTtlp7db", 3),
          ("fxsTtlp8db", 2),
          ("fxsTtlp9db", 1),
          ("fxsTtlpN1db", 11),
          ("fxsTtlpN2db", 12),
          ("fxsTtlpN3db", 13),
          ("tTlpNummeric", 14))
    )


_ZhoneVaIfCfgTransmitTLP_Type.__name__ = "Integer32"
_ZhoneVaIfCfgTransmitTLP_Object = MibTableColumn
zhoneVaIfCfgTransmitTLP = _ZhoneVaIfCfgTransmitTLP_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1, 3),
    _ZhoneVaIfCfgTransmitTLP_Type()
)
zhoneVaIfCfgTransmitTLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfCfgTransmitTLP.setStatus("current")


class _ZhoneVaIfCfgTrunkConditioning_Type(Integer32):
    """Custom type zhoneVaIfCfgTrunkConditioning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("busy", 3),
          ("idle", 2),
          ("off", 1))
    )


_ZhoneVaIfCfgTrunkConditioning_Type.__name__ = "Integer32"
_ZhoneVaIfCfgTrunkConditioning_Object = MibTableColumn
zhoneVaIfCfgTrunkConditioning = _ZhoneVaIfCfgTrunkConditioning_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1, 4),
    _ZhoneVaIfCfgTrunkConditioning_Type()
)
zhoneVaIfCfgTrunkConditioning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfCfgTrunkConditioning.setStatus("current")


class _ZhoneVaIfCfgLineType_Type(Integer32):
    """Custom type zhoneVaIfCfgLineType based on Integer32"""
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
        *(("ebs", 4),
          ("em", 3),
          ("fxo", 2),
          ("fxs", 1))
    )


_ZhoneVaIfCfgLineType_Type.__name__ = "Integer32"
_ZhoneVaIfCfgLineType_Object = MibTableColumn
zhoneVaIfCfgLineType = _ZhoneVaIfCfgLineType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1, 5),
    _ZhoneVaIfCfgLineType_Type()
)
zhoneVaIfCfgLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVaIfCfgLineType.setStatus("current")


class _ZhoneVaIfCfgIntegratedDSP_Type(TruthValue):
    """Custom type zhoneVaIfCfgIntegratedDSP based on TruthValue"""


_ZhoneVaIfCfgIntegratedDSP_Object = MibTableColumn
zhoneVaIfCfgIntegratedDSP = _ZhoneVaIfCfgIntegratedDSP_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1, 6),
    _ZhoneVaIfCfgIntegratedDSP_Type()
)
zhoneVaIfCfgIntegratedDSP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVaIfCfgIntegratedDSP.setStatus("current")


class _ZhoneVaIfCfgLineCapabilities_Type(Bits):
    """Custom type zhoneVaIfCfgLineCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("em", 2),
          ("fxo", 1),
          ("fxs", 0))
    )

_ZhoneVaIfCfgLineCapabilities_Type.__name__ = "Bits"
_ZhoneVaIfCfgLineCapabilities_Object = MibTableColumn
zhoneVaIfCfgLineCapabilities = _ZhoneVaIfCfgLineCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1, 7),
    _ZhoneVaIfCfgLineCapabilities_Type()
)
zhoneVaIfCfgLineCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVaIfCfgLineCapabilities.setStatus("current")


class _ZhoneVaIfCfgMaintenanceMode_Type(Integer32):
    """Custom type zhoneVaIfCfgMaintenanceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ifAnalogLoopback", 3),
          ("ifDigitalLoopback", 2),
          ("off", 1))
    )


_ZhoneVaIfCfgMaintenanceMode_Type.__name__ = "Integer32"
_ZhoneVaIfCfgMaintenanceMode_Object = MibTableColumn
zhoneVaIfCfgMaintenanceMode = _ZhoneVaIfCfgMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1, 8),
    _ZhoneVaIfCfgMaintenanceMode_Type()
)
zhoneVaIfCfgMaintenanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfCfgMaintenanceMode.setStatus("current")


class _ZhoneVaIfCfgPCMEncoding_Type(Integer32):
    """Custom type zhoneVaIfCfgPCMEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alaw", 1),
          ("mulaw", 2))
    )


_ZhoneVaIfCfgPCMEncoding_Type.__name__ = "Integer32"
_ZhoneVaIfCfgPCMEncoding_Object = MibTableColumn
zhoneVaIfCfgPCMEncoding = _ZhoneVaIfCfgPCMEncoding_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1, 9),
    _ZhoneVaIfCfgPCMEncoding_Type()
)
zhoneVaIfCfgPCMEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfCfgPCMEncoding.setStatus("current")


class _ZhoneVaIfCfgReceiveTLPNum_Type(Integer32):
    """Custom type zhoneVaIfCfgReceiveTLPNum based on Integer32"""
    defaultBinValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-160, 85),
    )


_ZhoneVaIfCfgReceiveTLPNum_Type.__name__ = "Integer32"
_ZhoneVaIfCfgReceiveTLPNum_Object = MibTableColumn
zhoneVaIfCfgReceiveTLPNum = _ZhoneVaIfCfgReceiveTLPNum_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1, 10),
    _ZhoneVaIfCfgReceiveTLPNum_Type()
)
zhoneVaIfCfgReceiveTLPNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfCfgReceiveTLPNum.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVaIfCfgReceiveTLPNum.setUnits("dB/10")


class _ZhoneVaIfCfgTransmitTLPNum_Type(Integer32):
    """Custom type zhoneVaIfCfgTransmitTLPNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-175, 70),
    )


_ZhoneVaIfCfgTransmitTLPNum_Type.__name__ = "Integer32"
_ZhoneVaIfCfgTransmitTLPNum_Object = MibTableColumn
zhoneVaIfCfgTransmitTLPNum = _ZhoneVaIfCfgTransmitTLPNum_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1, 11),
    _ZhoneVaIfCfgTransmitTLPNum_Type()
)
zhoneVaIfCfgTransmitTLPNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfCfgTransmitTLPNum.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVaIfCfgTransmitTLPNum.setUnits("dB/10")


class _ZhoneVaIfCfgLoopCurrent_Type(Integer32):
    """Custom type zhoneVaIfCfgLoopCurrent based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 44),
    )


_ZhoneVaIfCfgLoopCurrent_Type.__name__ = "Integer32"
_ZhoneVaIfCfgLoopCurrent_Object = MibTableColumn
zhoneVaIfCfgLoopCurrent = _ZhoneVaIfCfgLoopCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1, 12),
    _ZhoneVaIfCfgLoopCurrent_Type()
)
zhoneVaIfCfgLoopCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfCfgLoopCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVaIfCfgLoopCurrent.setUnits("mA")


class _ZhoneVaIfCfgRingVoltage_Type(Integer32):
    """Custom type zhoneVaIfCfgRingVoltage based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("b75vrms", 2),
          ("b85vrms", 1),
          ("b92vrms", 3))
    )


_ZhoneVaIfCfgRingVoltage_Type.__name__ = "Integer32"
_ZhoneVaIfCfgRingVoltage_Object = MibTableColumn
zhoneVaIfCfgRingVoltage = _ZhoneVaIfCfgRingVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1, 13),
    _ZhoneVaIfCfgRingVoltage_Type()
)
zhoneVaIfCfgRingVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfCfgRingVoltage.setStatus("current")
_ZhoneVaIfStatusTable_Object = MibTable
zhoneVaIfStatusTable = _ZhoneVaIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 2)
)
if mibBuilder.loadTexts:
    zhoneVaIfStatusTable.setStatus("current")
_ZhoneVaIfStatusEntry_Object = MibTableRow
zhoneVaIfStatusEntry = _ZhoneVaIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    zhoneVaIfStatusEntry.setStatus("current")
_ZhoneVaIfStatusSignalErrors_Type = Counter32
_ZhoneVaIfStatusSignalErrors_Object = MibTableColumn
zhoneVaIfStatusSignalErrors = _ZhoneVaIfStatusSignalErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 2, 1, 1),
    _ZhoneVaIfStatusSignalErrors_Type()
)
zhoneVaIfStatusSignalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVaIfStatusSignalErrors.setStatus("current")


class _ZhoneVaIfStatusInfoType_Type(Integer32):
    """Custom type zhoneVaIfStatusInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("g3Fax", 3),
          ("notype", 1),
          ("voice", 2))
    )


_ZhoneVaIfStatusInfoType_Type.__name__ = "Integer32"
_ZhoneVaIfStatusInfoType_Object = MibTableColumn
zhoneVaIfStatusInfoType = _ZhoneVaIfStatusInfoType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 2, 1, 2),
    _ZhoneVaIfStatusInfoType_Type()
)
zhoneVaIfStatusInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVaIfStatusInfoType.setStatus("current")
_ZhoneVaIfFXSObjects_ObjectIdentity = ObjectIdentity
zhoneVaIfFXSObjects = _ZhoneVaIfFXSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 2)
)
_ZhoneVaIfFXSCfgTable_Object = MibTable
zhoneVaIfFXSCfgTable = _ZhoneVaIfFXSCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 1)
)
if mibBuilder.loadTexts:
    zhoneVaIfFXSCfgTable.setStatus("current")
_ZhoneVaIfFXSCfgEntry_Object = MibTableRow
zhoneVaIfFXSCfgEntry = _ZhoneVaIfFXSCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 1, 1)
)
zhoneVaIfFXSCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zhoneVaIfFXSCfgEntry.setStatus("current")


class _ZhoneVaIfFXSCfgSignalType_Type(Integer32):
    """Custom type zhoneVaIfFXSCfgSignalType based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("fxsGroundStart", 2),
          ("fxsGroundStartAutomatic", 4),
          ("fxsGroundStartImmediate", 5),
          ("fxsLoopStart", 1),
          ("fxsLoopStartFd", 3),
          ("fxsdnGroundStart", 8),
          ("fxsdnGroundStartImmediate", 9),
          ("fxsdnLoopStart", 6),
          ("fxsdnLoopStartFd", 7),
          ("fxsdnwinkGroundStart", 12),
          ("fxsdnwinkGroundStartImmediate", 13),
          ("fxsdnwinkLoopStart", 10),
          ("fxsdnwinkLoopStartFd", 11),
          ("fxstr08SingleParty", 14),
          ("fxstr08UniversalVoiceGrade", 15),
          ("fxstr08UniversalVoiceGradeAutomatic", 16))
    )


_ZhoneVaIfFXSCfgSignalType_Type.__name__ = "Integer32"
_ZhoneVaIfFXSCfgSignalType_Object = MibTableColumn
zhoneVaIfFXSCfgSignalType = _ZhoneVaIfFXSCfgSignalType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 1, 1, 1),
    _ZhoneVaIfFXSCfgSignalType_Type()
)
zhoneVaIfFXSCfgSignalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfFXSCfgSignalType.setStatus("current")


class _ZhoneVaIfFXSRingFrequency_Type(Integer32):
    """Custom type zhoneVaIfFXSRingFrequency based on Integer32"""
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
        *(("ringFrequency20", 3),
          ("ringFrequency25", 1),
          ("ringFrequency30", 4),
          ("ringFrequency50", 2))
    )


_ZhoneVaIfFXSRingFrequency_Type.__name__ = "Integer32"
_ZhoneVaIfFXSRingFrequency_Object = MibTableColumn
zhoneVaIfFXSRingFrequency = _ZhoneVaIfFXSRingFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 1, 1, 2),
    _ZhoneVaIfFXSRingFrequency_Type()
)
zhoneVaIfFXSRingFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfFXSRingFrequency.setStatus("current")


class _ZhoneVaIfFXSRingBack_Type(Integer32):
    """Custom type zhoneVaIfFXSRingBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ZhoneVaIfFXSRingBack_Type.__name__ = "Integer32"
_ZhoneVaIfFXSRingBack_Object = MibTableColumn
zhoneVaIfFXSRingBack = _ZhoneVaIfFXSRingBack_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 1, 1, 3),
    _ZhoneVaIfFXSRingBack_Type()
)
zhoneVaIfFXSRingBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfFXSRingBack.setStatus("current")
_ZhoneVaIfFXSStatusTable_Object = MibTable
zhoneVaIfFXSStatusTable = _ZhoneVaIfFXSStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 2)
)
if mibBuilder.loadTexts:
    zhoneVaIfFXSStatusTable.setStatus("current")
_ZhoneVaIfFXSStatusEntry_Object = MibTableRow
zhoneVaIfFXSStatusEntry = _ZhoneVaIfFXSStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 2, 1)
)
if mibBuilder.loadTexts:
    zhoneVaIfFXSStatusEntry.setStatus("current")


class _ZhoneVaIfFXSHookStatus_Type(Integer32):
    """Custom type zhoneVaIfFXSHookStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offHook", 2),
          ("onHook", 1))
    )


_ZhoneVaIfFXSHookStatus_Type.__name__ = "Integer32"
_ZhoneVaIfFXSHookStatus_Object = MibTableColumn
zhoneVaIfFXSHookStatus = _ZhoneVaIfFXSHookStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 2, 1, 1),
    _ZhoneVaIfFXSHookStatus_Type()
)
zhoneVaIfFXSHookStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVaIfFXSHookStatus.setStatus("current")


class _ZhoneVaIfFXSRingActive_Type(TruthValue):
    """Custom type zhoneVaIfFXSRingActive based on TruthValue"""


_ZhoneVaIfFXSRingActive_Object = MibTableColumn
zhoneVaIfFXSRingActive = _ZhoneVaIfFXSRingActive_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 2, 1, 2),
    _ZhoneVaIfFXSRingActive_Type()
)
zhoneVaIfFXSRingActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVaIfFXSRingActive.setStatus("current")


class _ZhoneVaIfFXSRingGround_Type(TruthValue):
    """Custom type zhoneVaIfFXSRingGround based on TruthValue"""


_ZhoneVaIfFXSRingGround_Object = MibTableColumn
zhoneVaIfFXSRingGround = _ZhoneVaIfFXSRingGround_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 2, 1, 3),
    _ZhoneVaIfFXSRingGround_Type()
)
zhoneVaIfFXSRingGround.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVaIfFXSRingGround.setStatus("current")


class _ZhoneVaIfFXSTipGround_Type(TruthValue):
    """Custom type zhoneVaIfFXSTipGround based on TruthValue"""


_ZhoneVaIfFXSTipGround_Object = MibTableColumn
zhoneVaIfFXSTipGround = _ZhoneVaIfFXSTipGround_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 2, 1, 4),
    _ZhoneVaIfFXSTipGround_Type()
)
zhoneVaIfFXSTipGround.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVaIfFXSTipGround.setStatus("current")
_ZhoneVaIfFXSTimingTable_Object = MibTable
zhoneVaIfFXSTimingTable = _ZhoneVaIfFXSTimingTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 3)
)
if mibBuilder.loadTexts:
    zhoneVaIfFXSTimingTable.setStatus("current")
_ZhoneVaIfFXSTimingEntry_Object = MibTableRow
zhoneVaIfFXSTimingEntry = _ZhoneVaIfFXSTimingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 3, 1)
)
if mibBuilder.loadTexts:
    zhoneVaIfFXSTimingEntry.setStatus("current")


class _ZhoneVaIfFXSTimingDigitDuration_Type(Integer32):
    """Custom type zhoneVaIfFXSTimingDigitDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_ZhoneVaIfFXSTimingDigitDuration_Type.__name__ = "Integer32"
_ZhoneVaIfFXSTimingDigitDuration_Object = MibTableColumn
zhoneVaIfFXSTimingDigitDuration = _ZhoneVaIfFXSTimingDigitDuration_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 3, 1, 1),
    _ZhoneVaIfFXSTimingDigitDuration_Type()
)
zhoneVaIfFXSTimingDigitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfFXSTimingDigitDuration.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVaIfFXSTimingDigitDuration.setUnits("milliseconds")


class _ZhoneVaIfFXSTimingInterDigitDuration_Type(Integer32):
    """Custom type zhoneVaIfFXSTimingInterDigitDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_ZhoneVaIfFXSTimingInterDigitDuration_Type.__name__ = "Integer32"
_ZhoneVaIfFXSTimingInterDigitDuration_Object = MibTableColumn
zhoneVaIfFXSTimingInterDigitDuration = _ZhoneVaIfFXSTimingInterDigitDuration_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 3, 1, 2),
    _ZhoneVaIfFXSTimingInterDigitDuration_Type()
)
zhoneVaIfFXSTimingInterDigitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfFXSTimingInterDigitDuration.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVaIfFXSTimingInterDigitDuration.setUnits("milliseconds")
_ZhonePotsRingTable_Object = MibTable
zhonePotsRingTable = _ZhonePotsRingTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 4)
)
if mibBuilder.loadTexts:
    zhonePotsRingTable.setStatus("deprecated")
_ZhonePotsRingEntry_Object = MibTableRow
zhonePotsRingEntry = _ZhonePotsRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 4, 1)
)
zhonePotsRingEntry.setIndexNames(
    (0, "Zhone-VOICE-ANALOG-IF-MIB", "zhonePotsRingIfIndex"),
)
if mibBuilder.loadTexts:
    zhonePotsRingEntry.setStatus("deprecated")
_ZhonePotsRingIfIndex_Type = InterfaceIndex
_ZhonePotsRingIfIndex_Object = MibTableColumn
zhonePotsRingIfIndex = _ZhonePotsRingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 4, 1, 1),
    _ZhonePotsRingIfIndex_Type()
)
zhonePotsRingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhonePotsRingIfIndex.setStatus("deprecated")


class _ZhonePotsRingRingingCadence_Type(Integer32):
    """Custom type zhonePotsRingRingingCadence based on Integer32"""
    defaultValue = 9

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
              10)
        )
    )
    namedValues = NamedValues(
        *(("ring-cadence-common", 9),
          ("ring-cadence-r0", 1),
          ("ring-cadence-r1", 2),
          ("ring-cadence-r2", 3),
          ("ring-cadence-r3", 4),
          ("ring-cadence-r4", 5),
          ("ring-cadence-r5", 6),
          ("ring-cadence-r6", 7),
          ("ring-cadence-r7", 8),
          ("ring-cadence-splash", 10))
    )


_ZhonePotsRingRingingCadence_Type.__name__ = "Integer32"
_ZhonePotsRingRingingCadence_Object = MibTableColumn
zhonePotsRingRingingCadence = _ZhonePotsRingRingingCadence_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 4, 1, 2),
    _ZhonePotsRingRingingCadence_Type()
)
zhonePotsRingRingingCadence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePotsRingRingingCadence.setStatus("deprecated")


class _ZhonePotsRingTimer_Type(Integer32):
    """Custom type zhonePotsRingTimer based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_ZhonePotsRingTimer_Type.__name__ = "Integer32"
_ZhonePotsRingTimer_Object = MibTableColumn
zhonePotsRingTimer = _ZhonePotsRingTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 4, 1, 3),
    _ZhonePotsRingTimer_Type()
)
zhonePotsRingTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePotsRingTimer.setStatus("deprecated")
_ZhonePotsRingRowStatus_Type = ZhoneRowStatus
_ZhonePotsRingRowStatus_Object = MibTableColumn
zhonePotsRingRowStatus = _ZhonePotsRingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 4, 1, 4),
    _ZhonePotsRingRowStatus_Type()
)
zhonePotsRingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhonePotsRingRowStatus.setStatus("deprecated")
_ZhoneVaIfFXOObjects_ObjectIdentity = ObjectIdentity
zhoneVaIfFXOObjects = _ZhoneVaIfFXOObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 3)
)
_ZhoneVaIfFXOCfgTable_Object = MibTable
zhoneVaIfFXOCfgTable = _ZhoneVaIfFXOCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 1)
)
if mibBuilder.loadTexts:
    zhoneVaIfFXOCfgTable.setStatus("current")
_ZhoneVaIfFXOCfgEntry_Object = MibTableRow
zhoneVaIfFXOCfgEntry = _ZhoneVaIfFXOCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 1, 1)
)
zhoneVaIfFXOCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zhoneVaIfFXOCfgEntry.setStatus("current")


class _ZhoneVaIfFXOCfgSignalType_Type(Integer32):
    """Custom type zhoneVaIfFXOCfgSignalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fxoGroundStart", 2),
          ("fxoLoopStart", 1),
          ("fxodpt", 3))
    )


_ZhoneVaIfFXOCfgSignalType_Type.__name__ = "Integer32"
_ZhoneVaIfFXOCfgSignalType_Object = MibTableColumn
zhoneVaIfFXOCfgSignalType = _ZhoneVaIfFXOCfgSignalType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 1, 1, 1),
    _ZhoneVaIfFXOCfgSignalType_Type()
)
zhoneVaIfFXOCfgSignalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfFXOCfgSignalType.setStatus("current")


class _ZhoneVaIfFXOCfgNumberRings_Type(Integer32):
    """Custom type zhoneVaIfFXOCfgNumberRings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ZhoneVaIfFXOCfgNumberRings_Type.__name__ = "Integer32"
_ZhoneVaIfFXOCfgNumberRings_Object = MibTableColumn
zhoneVaIfFXOCfgNumberRings = _ZhoneVaIfFXOCfgNumberRings_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 1, 1, 2),
    _ZhoneVaIfFXOCfgNumberRings_Type()
)
zhoneVaIfFXOCfgNumberRings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfFXOCfgNumberRings.setStatus("current")


class _ZhoneVaIfFXOCfgSupDisconnect_Type(TruthValue):
    """Custom type zhoneVaIfFXOCfgSupDisconnect based on TruthValue"""


_ZhoneVaIfFXOCfgSupDisconnect_Object = MibTableColumn
zhoneVaIfFXOCfgSupDisconnect = _ZhoneVaIfFXOCfgSupDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 1, 1, 3),
    _ZhoneVaIfFXOCfgSupDisconnect_Type()
)
zhoneVaIfFXOCfgSupDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfFXOCfgSupDisconnect.setStatus("current")


class _ZhoneVaIfFXOCfgDialType_Type(Integer32):
    """Custom type zhoneVaIfFXOCfgDialType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtmf", 1),
          ("pulse", 2))
    )


_ZhoneVaIfFXOCfgDialType_Type.__name__ = "Integer32"
_ZhoneVaIfFXOCfgDialType_Object = MibTableColumn
zhoneVaIfFXOCfgDialType = _ZhoneVaIfFXOCfgDialType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 1, 1, 4),
    _ZhoneVaIfFXOCfgDialType_Type()
)
zhoneVaIfFXOCfgDialType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfFXOCfgDialType.setStatus("current")
_ZhoneVaIfFXOStatusTable_Object = MibTable
zhoneVaIfFXOStatusTable = _ZhoneVaIfFXOStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 2)
)
if mibBuilder.loadTexts:
    zhoneVaIfFXOStatusTable.setStatus("current")
_ZhoneVaIfFXOStatusEntry_Object = MibTableRow
zhoneVaIfFXOStatusEntry = _ZhoneVaIfFXOStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 2, 1)
)
if mibBuilder.loadTexts:
    zhoneVaIfFXOStatusEntry.setStatus("current")


class _ZhoneVaIfFXOHookStatus_Type(Integer32):
    """Custom type zhoneVaIfFXOHookStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offHook", 2),
          ("onHook", 1))
    )


_ZhoneVaIfFXOHookStatus_Type.__name__ = "Integer32"
_ZhoneVaIfFXOHookStatus_Object = MibTableColumn
zhoneVaIfFXOHookStatus = _ZhoneVaIfFXOHookStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 2, 1, 1),
    _ZhoneVaIfFXOHookStatus_Type()
)
zhoneVaIfFXOHookStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVaIfFXOHookStatus.setStatus("current")


class _ZhoneVaIfFXORingDetect_Type(TruthValue):
    """Custom type zhoneVaIfFXORingDetect based on TruthValue"""


_ZhoneVaIfFXORingDetect_Object = MibTableColumn
zhoneVaIfFXORingDetect = _ZhoneVaIfFXORingDetect_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 2, 1, 2),
    _ZhoneVaIfFXORingDetect_Type()
)
zhoneVaIfFXORingDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVaIfFXORingDetect.setStatus("current")


class _ZhoneVaIfFXORingGround_Type(TruthValue):
    """Custom type zhoneVaIfFXORingGround based on TruthValue"""


_ZhoneVaIfFXORingGround_Object = MibTableColumn
zhoneVaIfFXORingGround = _ZhoneVaIfFXORingGround_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 2, 1, 3),
    _ZhoneVaIfFXORingGround_Type()
)
zhoneVaIfFXORingGround.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVaIfFXORingGround.setStatus("current")


class _ZhoneVaIfFXOTipGround_Type(TruthValue):
    """Custom type zhoneVaIfFXOTipGround based on TruthValue"""


_ZhoneVaIfFXOTipGround_Object = MibTableColumn
zhoneVaIfFXOTipGround = _ZhoneVaIfFXOTipGround_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 2, 1, 4),
    _ZhoneVaIfFXOTipGround_Type()
)
zhoneVaIfFXOTipGround.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVaIfFXOTipGround.setStatus("current")
_ZhoneVaIfFXOTimingTable_Object = MibTable
zhoneVaIfFXOTimingTable = _ZhoneVaIfFXOTimingTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 3)
)
if mibBuilder.loadTexts:
    zhoneVaIfFXOTimingTable.setStatus("current")
_ZhoneVaIfFXOTimingEntry_Object = MibTableRow
zhoneVaIfFXOTimingEntry = _ZhoneVaIfFXOTimingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 3, 1)
)
if mibBuilder.loadTexts:
    zhoneVaIfFXOTimingEntry.setStatus("current")


class _ZhoneVaIfFXOTimingDigitDuration_Type(Integer32):
    """Custom type zhoneVaIfFXOTimingDigitDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_ZhoneVaIfFXOTimingDigitDuration_Type.__name__ = "Integer32"
_ZhoneVaIfFXOTimingDigitDuration_Object = MibTableColumn
zhoneVaIfFXOTimingDigitDuration = _ZhoneVaIfFXOTimingDigitDuration_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 3, 1, 1),
    _ZhoneVaIfFXOTimingDigitDuration_Type()
)
zhoneVaIfFXOTimingDigitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfFXOTimingDigitDuration.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVaIfFXOTimingDigitDuration.setUnits("milliseconds")


class _ZhoneVaIfFXOTimingInterDigitDuration_Type(Integer32):
    """Custom type zhoneVaIfFXOTimingInterDigitDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_ZhoneVaIfFXOTimingInterDigitDuration_Type.__name__ = "Integer32"
_ZhoneVaIfFXOTimingInterDigitDuration_Object = MibTableColumn
zhoneVaIfFXOTimingInterDigitDuration = _ZhoneVaIfFXOTimingInterDigitDuration_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 3, 1, 2),
    _ZhoneVaIfFXOTimingInterDigitDuration_Type()
)
zhoneVaIfFXOTimingInterDigitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfFXOTimingInterDigitDuration.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVaIfFXOTimingInterDigitDuration.setUnits("milliseconds")


class _ZhoneVaIfFXOTimingPulseRate_Type(Integer32):
    """Custom type zhoneVaIfFXOTimingPulseRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 20),
    )


_ZhoneVaIfFXOTimingPulseRate_Type.__name__ = "Integer32"
_ZhoneVaIfFXOTimingPulseRate_Object = MibTableColumn
zhoneVaIfFXOTimingPulseRate = _ZhoneVaIfFXOTimingPulseRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 3, 1, 3),
    _ZhoneVaIfFXOTimingPulseRate_Type()
)
zhoneVaIfFXOTimingPulseRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfFXOTimingPulseRate.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVaIfFXOTimingPulseRate.setUnits("pps")


class _ZhoneVaIfFXOTimingPulseInterDigitDuration_Type(Integer32):
    """Custom type zhoneVaIfFXOTimingPulseInterDigitDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_ZhoneVaIfFXOTimingPulseInterDigitDuration_Type.__name__ = "Integer32"
_ZhoneVaIfFXOTimingPulseInterDigitDuration_Object = MibTableColumn
zhoneVaIfFXOTimingPulseInterDigitDuration = _ZhoneVaIfFXOTimingPulseInterDigitDuration_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 3, 1, 4),
    _ZhoneVaIfFXOTimingPulseInterDigitDuration_Type()
)
zhoneVaIfFXOTimingPulseInterDigitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfFXOTimingPulseInterDigitDuration.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVaIfFXOTimingPulseInterDigitDuration.setUnits("pps")
_ZhoneVaIfEMObjects_ObjectIdentity = ObjectIdentity
zhoneVaIfEMObjects = _ZhoneVaIfEMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 4)
)
_ZhoneVaIfEMCfgTable_Object = MibTable
zhoneVaIfEMCfgTable = _ZhoneVaIfEMCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 1)
)
if mibBuilder.loadTexts:
    zhoneVaIfEMCfgTable.setStatus("current")
_ZhoneVaIfEMCfgEntry_Object = MibTableRow
zhoneVaIfEMCfgEntry = _ZhoneVaIfEMCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 1, 1)
)
zhoneVaIfEMCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zhoneVaIfEMCfgEntry.setStatus("current")


class _ZhoneVaIfEMCfgSignalType_Type(Integer32):
    """Custom type zhoneVaIfEMCfgSignalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delayDial", 3),
          ("immediateDial", 2),
          ("winkStart", 1))
    )


_ZhoneVaIfEMCfgSignalType_Type.__name__ = "Integer32"
_ZhoneVaIfEMCfgSignalType_Object = MibTableColumn
zhoneVaIfEMCfgSignalType = _ZhoneVaIfEMCfgSignalType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 1, 1, 1),
    _ZhoneVaIfEMCfgSignalType_Type()
)
zhoneVaIfEMCfgSignalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVaIfEMCfgSignalType.setStatus("current")


class _ZhoneVaIfEMCfgOperation_Type(Integer32):
    """Custom type zhoneVaIfEMCfgOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourWires", 2),
          ("twoWires", 1))
    )


_ZhoneVaIfEMCfgOperation_Type.__name__ = "Integer32"
_ZhoneVaIfEMCfgOperation_Object = MibTableColumn
zhoneVaIfEMCfgOperation = _ZhoneVaIfEMCfgOperation_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 1, 1, 2),
    _ZhoneVaIfEMCfgOperation_Type()
)
zhoneVaIfEMCfgOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVaIfEMCfgOperation.setStatus("current")


class _ZhoneVaIfEMCfgType_Type(Integer32):
    """Custom type zhoneVaIfEMCfgType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("typeI", 1),
          ("typeII", 2),
          ("typeIIE", 6),
          ("typeIII", 3),
          ("typeIIM", 7),
          ("typeIV", 4),
          ("typeTO", 8),
          ("typeV", 5))
    )


_ZhoneVaIfEMCfgType_Type.__name__ = "Integer32"
_ZhoneVaIfEMCfgType_Object = MibTableColumn
zhoneVaIfEMCfgType = _ZhoneVaIfEMCfgType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 1, 1, 3),
    _ZhoneVaIfEMCfgType_Type()
)
zhoneVaIfEMCfgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfEMCfgType.setStatus("current")


class _ZhoneVaIfEMCfgDialType_Type(Integer32):
    """Custom type zhoneVaIfEMCfgDialType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtmf", 1),
          ("pulse", 2))
    )


_ZhoneVaIfEMCfgDialType_Type.__name__ = "Integer32"
_ZhoneVaIfEMCfgDialType_Object = MibTableColumn
zhoneVaIfEMCfgDialType = _ZhoneVaIfEMCfgDialType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 1, 1, 4),
    _ZhoneVaIfEMCfgDialType_Type()
)
zhoneVaIfEMCfgDialType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVaIfEMCfgDialType.setStatus("current")
_ZhoneVaIfEMStatusTable_Object = MibTable
zhoneVaIfEMStatusTable = _ZhoneVaIfEMStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 2)
)
if mibBuilder.loadTexts:
    zhoneVaIfEMStatusTable.setStatus("current")
_ZhoneVaIfEMStatusEntry_Object = MibTableRow
zhoneVaIfEMStatusEntry = _ZhoneVaIfEMStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 2, 1)
)
if mibBuilder.loadTexts:
    zhoneVaIfEMStatusEntry.setStatus("current")


class _ZhoneVaIfEMInSeizureActive_Type(TruthValue):
    """Custom type zhoneVaIfEMInSeizureActive based on TruthValue"""


_ZhoneVaIfEMInSeizureActive_Object = MibTableColumn
zhoneVaIfEMInSeizureActive = _ZhoneVaIfEMInSeizureActive_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 2, 1, 1),
    _ZhoneVaIfEMInSeizureActive_Type()
)
zhoneVaIfEMInSeizureActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVaIfEMInSeizureActive.setStatus("current")


class _ZhoneVaIfEMOutSeizureActive_Type(TruthValue):
    """Custom type zhoneVaIfEMOutSeizureActive based on TruthValue"""


_ZhoneVaIfEMOutSeizureActive_Object = MibTableColumn
zhoneVaIfEMOutSeizureActive = _ZhoneVaIfEMOutSeizureActive_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 2, 1, 2),
    _ZhoneVaIfEMOutSeizureActive_Type()
)
zhoneVaIfEMOutSeizureActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVaIfEMOutSeizureActive.setStatus("current")
_ZhoneVaIfEMTimingTable_Object = MibTable
zhoneVaIfEMTimingTable = _ZhoneVaIfEMTimingTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 3)
)
if mibBuilder.loadTexts:
    zhoneVaIfEMTimingTable.setStatus("current")
_ZhoneVaIfEMTimingEntry_Object = MibTableRow
zhoneVaIfEMTimingEntry = _ZhoneVaIfEMTimingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 3, 1)
)
if mibBuilder.loadTexts:
    zhoneVaIfEMTimingEntry.setStatus("current")


class _ZhoneVaIfEMTimingDigitDuration_Type(Integer32):
    """Custom type zhoneVaIfEMTimingDigitDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_ZhoneVaIfEMTimingDigitDuration_Type.__name__ = "Integer32"
_ZhoneVaIfEMTimingDigitDuration_Object = MibTableColumn
zhoneVaIfEMTimingDigitDuration = _ZhoneVaIfEMTimingDigitDuration_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 3, 1, 1),
    _ZhoneVaIfEMTimingDigitDuration_Type()
)
zhoneVaIfEMTimingDigitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfEMTimingDigitDuration.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVaIfEMTimingDigitDuration.setUnits("milliseconds")


class _ZhoneVaIfEMTimingInterDigitDuration_Type(Integer32):
    """Custom type zhoneVaIfEMTimingInterDigitDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_ZhoneVaIfEMTimingInterDigitDuration_Type.__name__ = "Integer32"
_ZhoneVaIfEMTimingInterDigitDuration_Object = MibTableColumn
zhoneVaIfEMTimingInterDigitDuration = _ZhoneVaIfEMTimingInterDigitDuration_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 3, 1, 2),
    _ZhoneVaIfEMTimingInterDigitDuration_Type()
)
zhoneVaIfEMTimingInterDigitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfEMTimingInterDigitDuration.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVaIfEMTimingInterDigitDuration.setUnits("milliseconds")


class _ZhoneVaIfEMTimingPulseRate_Type(Integer32):
    """Custom type zhoneVaIfEMTimingPulseRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 20),
    )


_ZhoneVaIfEMTimingPulseRate_Type.__name__ = "Integer32"
_ZhoneVaIfEMTimingPulseRate_Object = MibTableColumn
zhoneVaIfEMTimingPulseRate = _ZhoneVaIfEMTimingPulseRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 3, 1, 3),
    _ZhoneVaIfEMTimingPulseRate_Type()
)
zhoneVaIfEMTimingPulseRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfEMTimingPulseRate.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVaIfEMTimingPulseRate.setUnits("pps")


class _ZhoneVaIfEMTimingPulseInterDigitDuration_Type(Integer32):
    """Custom type zhoneVaIfEMTimingPulseInterDigitDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_ZhoneVaIfEMTimingPulseInterDigitDuration_Type.__name__ = "Integer32"
_ZhoneVaIfEMTimingPulseInterDigitDuration_Object = MibTableColumn
zhoneVaIfEMTimingPulseInterDigitDuration = _ZhoneVaIfEMTimingPulseInterDigitDuration_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 3, 1, 4),
    _ZhoneVaIfEMTimingPulseInterDigitDuration_Type()
)
zhoneVaIfEMTimingPulseInterDigitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfEMTimingPulseInterDigitDuration.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVaIfEMTimingPulseInterDigitDuration.setUnits("milliseconds")


class _ZhoneVaIfEMTimingClearWaitDuration_Type(Integer32):
    """Custom type zhoneVaIfEMTimingClearWaitDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 2000),
    )


_ZhoneVaIfEMTimingClearWaitDuration_Type.__name__ = "Integer32"
_ZhoneVaIfEMTimingClearWaitDuration_Object = MibTableColumn
zhoneVaIfEMTimingClearWaitDuration = _ZhoneVaIfEMTimingClearWaitDuration_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 3, 1, 5),
    _ZhoneVaIfEMTimingClearWaitDuration_Type()
)
zhoneVaIfEMTimingClearWaitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfEMTimingClearWaitDuration.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVaIfEMTimingClearWaitDuration.setUnits("milliseconds")


class _ZhoneVaIfEMTimingMaxWinkWaitDuration_Type(Integer32):
    """Custom type zhoneVaIfEMTimingMaxWinkWaitDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_ZhoneVaIfEMTimingMaxWinkWaitDuration_Type.__name__ = "Integer32"
_ZhoneVaIfEMTimingMaxWinkWaitDuration_Object = MibTableColumn
zhoneVaIfEMTimingMaxWinkWaitDuration = _ZhoneVaIfEMTimingMaxWinkWaitDuration_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 3, 1, 6),
    _ZhoneVaIfEMTimingMaxWinkWaitDuration_Type()
)
zhoneVaIfEMTimingMaxWinkWaitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfEMTimingMaxWinkWaitDuration.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVaIfEMTimingMaxWinkWaitDuration.setUnits("milliseconds")


class _ZhoneVaIfEMTimingMaxWinkDuration_Type(Integer32):
    """Custom type zhoneVaIfEMTimingMaxWinkDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 3000),
    )


_ZhoneVaIfEMTimingMaxWinkDuration_Type.__name__ = "Integer32"
_ZhoneVaIfEMTimingMaxWinkDuration_Object = MibTableColumn
zhoneVaIfEMTimingMaxWinkDuration = _ZhoneVaIfEMTimingMaxWinkDuration_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 3, 1, 7),
    _ZhoneVaIfEMTimingMaxWinkDuration_Type()
)
zhoneVaIfEMTimingMaxWinkDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfEMTimingMaxWinkDuration.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVaIfEMTimingMaxWinkDuration.setUnits("milliseconds")


class _ZhoneVaIfEMTimingDelayStart_Type(Integer32):
    """Custom type zhoneVaIfEMTimingDelayStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 2000),
    )


_ZhoneVaIfEMTimingDelayStart_Type.__name__ = "Integer32"
_ZhoneVaIfEMTimingDelayStart_Object = MibTableColumn
zhoneVaIfEMTimingDelayStart = _ZhoneVaIfEMTimingDelayStart_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 3, 1, 8),
    _ZhoneVaIfEMTimingDelayStart_Type()
)
zhoneVaIfEMTimingDelayStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfEMTimingDelayStart.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVaIfEMTimingDelayStart.setUnits("milliseconds")


class _ZhoneVaIfEMTimingMaxDelayDuration_Type(Integer32):
    """Custom type zhoneVaIfEMTimingMaxDelayDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_ZhoneVaIfEMTimingMaxDelayDuration_Type.__name__ = "Integer32"
_ZhoneVaIfEMTimingMaxDelayDuration_Object = MibTableColumn
zhoneVaIfEMTimingMaxDelayDuration = _ZhoneVaIfEMTimingMaxDelayDuration_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 3, 1, 9),
    _ZhoneVaIfEMTimingMaxDelayDuration_Type()
)
zhoneVaIfEMTimingMaxDelayDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfEMTimingMaxDelayDuration.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVaIfEMTimingMaxDelayDuration.setUnits("milliseconds")


class _ZhoneVaIfEMTimingMinDelayPulseWidth_Type(Integer32):
    """Custom type zhoneVaIfEMTimingMinDelayPulseWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(140, 5000),
    )


_ZhoneVaIfEMTimingMinDelayPulseWidth_Type.__name__ = "Integer32"
_ZhoneVaIfEMTimingMinDelayPulseWidth_Object = MibTableColumn
zhoneVaIfEMTimingMinDelayPulseWidth = _ZhoneVaIfEMTimingMinDelayPulseWidth_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 3, 1, 10),
    _ZhoneVaIfEMTimingMinDelayPulseWidth_Type()
)
zhoneVaIfEMTimingMinDelayPulseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVaIfEMTimingMinDelayPulseWidth.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVaIfEMTimingMinDelayPulseWidth.setUnits("milliseconds")
zhoneVaIfCfgEntry.registerAugmentions(
    ("Zhone-VOICE-ANALOG-IF-MIB",
     "zhoneVaIfStatusEntry")
)
zhoneVaIfStatusEntry.setIndexNames(*zhoneVaIfCfgEntry.getIndexNames())
zhoneVaIfFXSCfgEntry.registerAugmentions(
    ("Zhone-VOICE-ANALOG-IF-MIB",
     "zhoneVaIfFXSStatusEntry")
)
zhoneVaIfFXSStatusEntry.setIndexNames(*zhoneVaIfFXSCfgEntry.getIndexNames())
zhoneVaIfFXSCfgEntry.registerAugmentions(
    ("Zhone-VOICE-ANALOG-IF-MIB",
     "zhoneVaIfFXSTimingEntry")
)
zhoneVaIfFXSTimingEntry.setIndexNames(*zhoneVaIfFXSCfgEntry.getIndexNames())
zhoneVaIfFXOCfgEntry.registerAugmentions(
    ("Zhone-VOICE-ANALOG-IF-MIB",
     "zhoneVaIfFXOStatusEntry")
)
zhoneVaIfFXOStatusEntry.setIndexNames(*zhoneVaIfFXOCfgEntry.getIndexNames())
zhoneVaIfFXOCfgEntry.registerAugmentions(
    ("Zhone-VOICE-ANALOG-IF-MIB",
     "zhoneVaIfFXOTimingEntry")
)
zhoneVaIfFXOTimingEntry.setIndexNames(*zhoneVaIfFXOCfgEntry.getIndexNames())
zhoneVaIfEMCfgEntry.registerAugmentions(
    ("Zhone-VOICE-ANALOG-IF-MIB",
     "zhoneVaIfEMStatusEntry")
)
zhoneVaIfEMStatusEntry.setIndexNames(*zhoneVaIfEMCfgEntry.getIndexNames())
zhoneVaIfEMCfgEntry.registerAugmentions(
    ("Zhone-VOICE-ANALOG-IF-MIB",
     "zhoneVaIfEMTimingEntry")
)
zhoneVaIfEMTimingEntry.setIndexNames(*zhoneVaIfEMCfgEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Zhone-VOICE-ANALOG-IF-MIB",
    **{"zhoneVaIfObjects": zhoneVaIfObjects,
       "zhoneVaIfGeneralObjects": zhoneVaIfGeneralObjects,
       "zhoneVaIfCfgTable": zhoneVaIfCfgTable,
       "zhoneVaIfCfgEntry": zhoneVaIfCfgEntry,
       "zhoneVaIfCfgImpedance": zhoneVaIfCfgImpedance,
       "zhoneVaIfCfgReceiveTLP": zhoneVaIfCfgReceiveTLP,
       "zhoneVaIfCfgTransmitTLP": zhoneVaIfCfgTransmitTLP,
       "zhoneVaIfCfgTrunkConditioning": zhoneVaIfCfgTrunkConditioning,
       "zhoneVaIfCfgLineType": zhoneVaIfCfgLineType,
       "zhoneVaIfCfgIntegratedDSP": zhoneVaIfCfgIntegratedDSP,
       "zhoneVaIfCfgLineCapabilities": zhoneVaIfCfgLineCapabilities,
       "zhoneVaIfCfgMaintenanceMode": zhoneVaIfCfgMaintenanceMode,
       "zhoneVaIfCfgPCMEncoding": zhoneVaIfCfgPCMEncoding,
       "zhoneVaIfCfgReceiveTLPNum": zhoneVaIfCfgReceiveTLPNum,
       "zhoneVaIfCfgTransmitTLPNum": zhoneVaIfCfgTransmitTLPNum,
       "zhoneVaIfCfgLoopCurrent": zhoneVaIfCfgLoopCurrent,
       "zhoneVaIfCfgRingVoltage": zhoneVaIfCfgRingVoltage,
       "zhoneVaIfStatusTable": zhoneVaIfStatusTable,
       "zhoneVaIfStatusEntry": zhoneVaIfStatusEntry,
       "zhoneVaIfStatusSignalErrors": zhoneVaIfStatusSignalErrors,
       "zhoneVaIfStatusInfoType": zhoneVaIfStatusInfoType,
       "zhoneVaIfFXSObjects": zhoneVaIfFXSObjects,
       "zhoneVaIfFXSCfgTable": zhoneVaIfFXSCfgTable,
       "zhoneVaIfFXSCfgEntry": zhoneVaIfFXSCfgEntry,
       "zhoneVaIfFXSCfgSignalType": zhoneVaIfFXSCfgSignalType,
       "zhoneVaIfFXSRingFrequency": zhoneVaIfFXSRingFrequency,
       "zhoneVaIfFXSRingBack": zhoneVaIfFXSRingBack,
       "zhoneVaIfFXSStatusTable": zhoneVaIfFXSStatusTable,
       "zhoneVaIfFXSStatusEntry": zhoneVaIfFXSStatusEntry,
       "zhoneVaIfFXSHookStatus": zhoneVaIfFXSHookStatus,
       "zhoneVaIfFXSRingActive": zhoneVaIfFXSRingActive,
       "zhoneVaIfFXSRingGround": zhoneVaIfFXSRingGround,
       "zhoneVaIfFXSTipGround": zhoneVaIfFXSTipGround,
       "zhoneVaIfFXSTimingTable": zhoneVaIfFXSTimingTable,
       "zhoneVaIfFXSTimingEntry": zhoneVaIfFXSTimingEntry,
       "zhoneVaIfFXSTimingDigitDuration": zhoneVaIfFXSTimingDigitDuration,
       "zhoneVaIfFXSTimingInterDigitDuration": zhoneVaIfFXSTimingInterDigitDuration,
       "zhonePotsRingTable": zhonePotsRingTable,
       "zhonePotsRingEntry": zhonePotsRingEntry,
       "zhonePotsRingIfIndex": zhonePotsRingIfIndex,
       "zhonePotsRingRingingCadence": zhonePotsRingRingingCadence,
       "zhonePotsRingTimer": zhonePotsRingTimer,
       "zhonePotsRingRowStatus": zhonePotsRingRowStatus,
       "zhoneVaIfFXOObjects": zhoneVaIfFXOObjects,
       "zhoneVaIfFXOCfgTable": zhoneVaIfFXOCfgTable,
       "zhoneVaIfFXOCfgEntry": zhoneVaIfFXOCfgEntry,
       "zhoneVaIfFXOCfgSignalType": zhoneVaIfFXOCfgSignalType,
       "zhoneVaIfFXOCfgNumberRings": zhoneVaIfFXOCfgNumberRings,
       "zhoneVaIfFXOCfgSupDisconnect": zhoneVaIfFXOCfgSupDisconnect,
       "zhoneVaIfFXOCfgDialType": zhoneVaIfFXOCfgDialType,
       "zhoneVaIfFXOStatusTable": zhoneVaIfFXOStatusTable,
       "zhoneVaIfFXOStatusEntry": zhoneVaIfFXOStatusEntry,
       "zhoneVaIfFXOHookStatus": zhoneVaIfFXOHookStatus,
       "zhoneVaIfFXORingDetect": zhoneVaIfFXORingDetect,
       "zhoneVaIfFXORingGround": zhoneVaIfFXORingGround,
       "zhoneVaIfFXOTipGround": zhoneVaIfFXOTipGround,
       "zhoneVaIfFXOTimingTable": zhoneVaIfFXOTimingTable,
       "zhoneVaIfFXOTimingEntry": zhoneVaIfFXOTimingEntry,
       "zhoneVaIfFXOTimingDigitDuration": zhoneVaIfFXOTimingDigitDuration,
       "zhoneVaIfFXOTimingInterDigitDuration": zhoneVaIfFXOTimingInterDigitDuration,
       "zhoneVaIfFXOTimingPulseRate": zhoneVaIfFXOTimingPulseRate,
       "zhoneVaIfFXOTimingPulseInterDigitDuration": zhoneVaIfFXOTimingPulseInterDigitDuration,
       "zhoneVaIfEMObjects": zhoneVaIfEMObjects,
       "zhoneVaIfEMCfgTable": zhoneVaIfEMCfgTable,
       "zhoneVaIfEMCfgEntry": zhoneVaIfEMCfgEntry,
       "zhoneVaIfEMCfgSignalType": zhoneVaIfEMCfgSignalType,
       "zhoneVaIfEMCfgOperation": zhoneVaIfEMCfgOperation,
       "zhoneVaIfEMCfgType": zhoneVaIfEMCfgType,
       "zhoneVaIfEMCfgDialType": zhoneVaIfEMCfgDialType,
       "zhoneVaIfEMStatusTable": zhoneVaIfEMStatusTable,
       "zhoneVaIfEMStatusEntry": zhoneVaIfEMStatusEntry,
       "zhoneVaIfEMInSeizureActive": zhoneVaIfEMInSeizureActive,
       "zhoneVaIfEMOutSeizureActive": zhoneVaIfEMOutSeizureActive,
       "zhoneVaIfEMTimingTable": zhoneVaIfEMTimingTable,
       "zhoneVaIfEMTimingEntry": zhoneVaIfEMTimingEntry,
       "zhoneVaIfEMTimingDigitDuration": zhoneVaIfEMTimingDigitDuration,
       "zhoneVaIfEMTimingInterDigitDuration": zhoneVaIfEMTimingInterDigitDuration,
       "zhoneVaIfEMTimingPulseRate": zhoneVaIfEMTimingPulseRate,
       "zhoneVaIfEMTimingPulseInterDigitDuration": zhoneVaIfEMTimingPulseInterDigitDuration,
       "zhoneVaIfEMTimingClearWaitDuration": zhoneVaIfEMTimingClearWaitDuration,
       "zhoneVaIfEMTimingMaxWinkWaitDuration": zhoneVaIfEMTimingMaxWinkWaitDuration,
       "zhoneVaIfEMTimingMaxWinkDuration": zhoneVaIfEMTimingMaxWinkDuration,
       "zhoneVaIfEMTimingDelayStart": zhoneVaIfEMTimingDelayStart,
       "zhoneVaIfEMTimingMaxDelayDuration": zhoneVaIfEMTimingMaxDelayDuration,
       "zhoneVaIfEMTimingMinDelayPulseWidth": zhoneVaIfEMTimingMinDelayPulseWidth,
       "zhoneVoiceAnalogIf-MIB": zhoneVoiceAnalogIf_MIB}
)
