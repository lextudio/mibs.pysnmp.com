# SNMP MIB module (NOVELSAT-MODULATOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOVELSAT-MODULATOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:04 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(nsRoot,) = mibBuilder.importSymbols(
    "NOVELSAT-ROOT-MIB",
    "nsRoot")

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

nsModulator = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 3)
)
nsModulator.setRevisions(
        ("2010-09-12 15:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsModConfig_ObjectIdentity = ObjectIdentity
nsModConfig = _NsModConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1)
)
if mibBuilder.loadTexts:
    nsModConfig.setStatus("current")
_NsModConfigLine_ObjectIdentity = ObjectIdentity
nsModConfigLine = _NsModConfigLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1)
)
if mibBuilder.loadTexts:
    nsModConfigLine.setStatus("current")


class _NsModConfigLineTXStatus_Type(Integer32):
    """Custom type nsModConfigLineTXStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("notApplicable", 255))
    )


_NsModConfigLineTXStatus_Type.__name__ = "Integer32"
_NsModConfigLineTXStatus_Object = MibScalar
nsModConfigLineTXStatus = _NsModConfigLineTXStatus_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 1),
    _NsModConfigLineTXStatus_Type()
)
nsModConfigLineTXStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLineTXStatus.setStatus("current")


class _NsModConfigLineMode_Type(Integer32):
    """Custom type nsModConfigLineMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("dsng", 1),
          ("dvbs", 0),
          ("dvbs2", 2),
          ("notApplicable", 255),
          ("ns3", 3))
    )


_NsModConfigLineMode_Type.__name__ = "Integer32"
_NsModConfigLineMode_Object = MibScalar
nsModConfigLineMode = _NsModConfigLineMode_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 2),
    _NsModConfigLineMode_Type()
)
nsModConfigLineMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLineMode.setStatus("current")


class _NsModConfigLineChPriority_Type(Integer32):
    """Custom type nsModConfigLineChPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ch1", 1),
          ("ch2", 2),
          ("equal", 0),
          ("notApplicable", 255))
    )


_NsModConfigLineChPriority_Type.__name__ = "Integer32"
_NsModConfigLineChPriority_Object = MibScalar
nsModConfigLineChPriority = _NsModConfigLineChPriority_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 4),
    _NsModConfigLineChPriority_Type()
)
nsModConfigLineChPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLineChPriority.setStatus("current")


class _NsModConfigLineRollOff_Type(Integer32):
    """Custom type nsModConfigLineRollOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 255),
          ("rollOff005", 0),
          ("rollOff010", 1),
          ("rollOff015", 2),
          ("rollOff020", 3),
          ("rollOff025", 4),
          ("rollOff035", 5))
    )


_NsModConfigLineRollOff_Type.__name__ = "Integer32"
_NsModConfigLineRollOff_Object = MibScalar
nsModConfigLineRollOff = _NsModConfigLineRollOff_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 5),
    _NsModConfigLineRollOff_Type()
)
nsModConfigLineRollOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLineRollOff.setStatus("current")


class _NsModConfigLineSineStatus_Type(Integer32):
    """Custom type nsModConfigLineSineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 255),
          ("off", 0),
          ("on", 1))
    )


_NsModConfigLineSineStatus_Type.__name__ = "Integer32"
_NsModConfigLineSineStatus_Object = MibScalar
nsModConfigLineSineStatus = _NsModConfigLineSineStatus_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 6),
    _NsModConfigLineSineStatus_Type()
)
nsModConfigLineSineStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLineSineStatus.setStatus("current")
_NsModConfigLineRFFreq_Type = Unsigned32
_NsModConfigLineRFFreq_Object = MibScalar
nsModConfigLineRFFreq = _NsModConfigLineRFFreq_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 7),
    _NsModConfigLineRFFreq_Type()
)
nsModConfigLineRFFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLineRFFreq.setStatus("current")


class _NsModConfigLineSymbolRate_Type(Integer32):
    """Custom type nsModConfigLineSymbolRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50000, 72000000),
    )


_NsModConfigLineSymbolRate_Type.__name__ = "Integer32"
_NsModConfigLineSymbolRate_Object = MibScalar
nsModConfigLineSymbolRate = _NsModConfigLineSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 8),
    _NsModConfigLineSymbolRate_Type()
)
nsModConfigLineSymbolRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLineSymbolRate.setStatus("current")


class _NsModConfigLinePower_Type(Integer32):
    """Custom type nsModConfigLinePower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3000, 0),
    )


_NsModConfigLinePower_Type.__name__ = "Integer32"
_NsModConfigLinePower_Object = MibScalar
nsModConfigLinePower = _NsModConfigLinePower_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 9),
    _NsModConfigLinePower_Type()
)
nsModConfigLinePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLinePower.setStatus("current")


class _NsModConfigLineGoldSeq_Type(Integer32):
    """Custom type nsModConfigLineGoldSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262141),
    )


_NsModConfigLineGoldSeq_Type.__name__ = "Integer32"
_NsModConfigLineGoldSeq_Object = MibScalar
nsModConfigLineGoldSeq = _NsModConfigLineGoldSeq_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 10),
    _NsModConfigLineGoldSeq_Type()
)
nsModConfigLineGoldSeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLineGoldSeq.setStatus("current")


class _NsModConfigLineDualChState_Type(Integer32):
    """Custom type nsModConfigLineDualChState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("dual", 0),
          ("notApplicable", 255),
          ("single", 1))
    )


_NsModConfigLineDualChState_Type.__name__ = "Integer32"
_NsModConfigLineDualChState_Object = MibScalar
nsModConfigLineDualChState = _NsModConfigLineDualChState_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 11),
    _NsModConfigLineDualChState_Type()
)
nsModConfigLineDualChState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLineDualChState.setStatus("current")
_NsModConfigLineBitRate_Type = Integer32
_NsModConfigLineBitRate_Object = MibScalar
nsModConfigLineBitRate = _NsModConfigLineBitRate_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 12),
    _NsModConfigLineBitRate_Type()
)
nsModConfigLineBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLineBitRate.setStatus("current")


class _NsModConfigLinePowerUpTXState_Type(Integer32):
    """Custom type nsModConfigLinePowerUpTXState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notApplicable", 255))
    )


_NsModConfigLinePowerUpTXState_Type.__name__ = "Integer32"
_NsModConfigLinePowerUpTXState_Object = MibScalar
nsModConfigLinePowerUpTXState = _NsModConfigLinePowerUpTXState_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 13),
    _NsModConfigLinePowerUpTXState_Type()
)
nsModConfigLinePowerUpTXState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLinePowerUpTXState.setStatus("current")


class _NsModConfigLineAcmMode_Type(Integer32):
    """Custom type nsModConfigLineAcmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enableCh1", 1),
          ("enableCh1Ch2", 3),
          ("enableCh2", 2),
          ("notApplicable", 255))
    )


_NsModConfigLineAcmMode_Type.__name__ = "Integer32"
_NsModConfigLineAcmMode_Object = MibScalar
nsModConfigLineAcmMode = _NsModConfigLineAcmMode_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 14),
    _NsModConfigLineAcmMode_Type()
)
nsModConfigLineAcmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLineAcmMode.setStatus("current")


class _NsModConfigLineOutputLevelMode_Type(Integer32):
    """Custom type nsModConfigLineOutputLevelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("constantEnvelope", 1),
          ("constantPower", 0),
          ("notApplicable", 255))
    )


_NsModConfigLineOutputLevelMode_Type.__name__ = "Integer32"
_NsModConfigLineOutputLevelMode_Object = MibScalar
nsModConfigLineOutputLevelMode = _NsModConfigLineOutputLevelMode_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 15),
    _NsModConfigLineOutputLevelMode_Type()
)
nsModConfigLineOutputLevelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLineOutputLevelMode.setStatus("current")


class _NsModConfigLineChannel1Bandwidth_Type(Integer32):
    """Custom type nsModConfigLineChannel1Bandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NsModConfigLineChannel1Bandwidth_Type.__name__ = "Integer32"
_NsModConfigLineChannel1Bandwidth_Object = MibScalar
nsModConfigLineChannel1Bandwidth = _NsModConfigLineChannel1Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 16),
    _NsModConfigLineChannel1Bandwidth_Type()
)
nsModConfigLineChannel1Bandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLineChannel1Bandwidth.setStatus("current")


class _NsModConfigLineChannel2Bandwidth_Type(Integer32):
    """Custom type nsModConfigLineChannel2Bandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NsModConfigLineChannel2Bandwidth_Type.__name__ = "Integer32"
_NsModConfigLineChannel2Bandwidth_Object = MibScalar
nsModConfigLineChannel2Bandwidth = _NsModConfigLineChannel2Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 17),
    _NsModConfigLineChannel2Bandwidth_Type()
)
nsModConfigLineChannel2Bandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLineChannel2Bandwidth.setStatus("current")


class _NsModConfigLineSpectrumInvert_Type(Integer32):
    """Custom type nsModConfigLineSpectrumInvert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 255),
          ("off", 0),
          ("on", 1))
    )


_NsModConfigLineSpectrumInvert_Type.__name__ = "Integer32"
_NsModConfigLineSpectrumInvert_Object = MibScalar
nsModConfigLineSpectrumInvert = _NsModConfigLineSpectrumInvert_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 18),
    _NsModConfigLineSpectrumInvert_Type()
)
nsModConfigLineSpectrumInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLineSpectrumInvert.setStatus("current")
_NsModConfigLineRecommendedBitRate_Type = Integer32
_NsModConfigLineRecommendedBitRate_Object = MibScalar
nsModConfigLineRecommendedBitRate = _NsModConfigLineRecommendedBitRate_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 19),
    _NsModConfigLineRecommendedBitRate_Type()
)
nsModConfigLineRecommendedBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModConfigLineRecommendedBitRate.setStatus("current")


class _NsModConfigLineLOFreq_Type(Unsigned32):
    """Custom type nsModConfigLineLOFreq based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000000000),
    )


_NsModConfigLineLOFreq_Type.__name__ = "Unsigned32"
_NsModConfigLineLOFreq_Object = MibScalar
nsModConfigLineLOFreq = _NsModConfigLineLOFreq_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 20),
    _NsModConfigLineLOFreq_Type()
)
nsModConfigLineLOFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLineLOFreq.setStatus("current")


class _NsModConfigLineAcmUseManagementIp_Type(Integer32):
    """Custom type nsModConfigLineAcmUseManagementIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notApplicable", 255))
    )


_NsModConfigLineAcmUseManagementIp_Type.__name__ = "Integer32"
_NsModConfigLineAcmUseManagementIp_Object = MibScalar
nsModConfigLineAcmUseManagementIp = _NsModConfigLineAcmUseManagementIp_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 21),
    _NsModConfigLineAcmUseManagementIp_Type()
)
nsModConfigLineAcmUseManagementIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLineAcmUseManagementIp.setStatus("current")
_NsModConfigLineAcmIpAddress_Type = IpAddress
_NsModConfigLineAcmIpAddress_Object = MibScalar
nsModConfigLineAcmIpAddress = _NsModConfigLineAcmIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 22),
    _NsModConfigLineAcmIpAddress_Type()
)
nsModConfigLineAcmIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLineAcmIpAddress.setStatus("current")
_NsModConfigLineAcmIpNetmask_Type = IpAddress
_NsModConfigLineAcmIpNetmask_Object = MibScalar
nsModConfigLineAcmIpNetmask = _NsModConfigLineAcmIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 23),
    _NsModConfigLineAcmIpNetmask_Type()
)
nsModConfigLineAcmIpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLineAcmIpNetmask.setStatus("current")


class _NsModConfigLineAupcMode_Type(Integer32):
    """Custom type nsModConfigLineAupcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notApplicable", 255))
    )


_NsModConfigLineAupcMode_Type.__name__ = "Integer32"
_NsModConfigLineAupcMode_Object = MibScalar
nsModConfigLineAupcMode = _NsModConfigLineAupcMode_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 24),
    _NsModConfigLineAupcMode_Type()
)
nsModConfigLineAupcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLineAupcMode.setStatus("current")


class _NsModConfigLineAupcSatRxFreq_Type(Integer32):
    """Custom type nsModConfigLineAupcSatRxFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 40000),
    )


_NsModConfigLineAupcSatRxFreq_Type.__name__ = "Integer32"
_NsModConfigLineAupcSatRxFreq_Object = MibScalar
nsModConfigLineAupcSatRxFreq = _NsModConfigLineAupcSatRxFreq_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 25),
    _NsModConfigLineAupcSatRxFreq_Type()
)
nsModConfigLineAupcSatRxFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLineAupcSatRxFreq.setStatus("current")


class _NsModConfigLineAupcSatRxPolarity_Type(Integer32):
    """Custom type nsModConfigLineAupcSatRxPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("circular-left", 2),
          ("circular-right", 3),
          ("horizontal", 1),
          ("notApplicable", 255),
          ("vertical", 0))
    )


_NsModConfigLineAupcSatRxPolarity_Type.__name__ = "Integer32"
_NsModConfigLineAupcSatRxPolarity_Object = MibScalar
nsModConfigLineAupcSatRxPolarity = _NsModConfigLineAupcSatRxPolarity_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 26),
    _NsModConfigLineAupcSatRxPolarity_Type()
)
nsModConfigLineAupcSatRxPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLineAupcSatRxPolarity.setStatus("current")


class _NsModConfigLineAupcSatTxFreq_Type(Integer32):
    """Custom type nsModConfigLineAupcSatTxFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 40000),
    )


_NsModConfigLineAupcSatTxFreq_Type.__name__ = "Integer32"
_NsModConfigLineAupcSatTxFreq_Object = MibScalar
nsModConfigLineAupcSatTxFreq = _NsModConfigLineAupcSatTxFreq_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 27),
    _NsModConfigLineAupcSatTxFreq_Type()
)
nsModConfigLineAupcSatTxFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLineAupcSatTxFreq.setStatus("current")


class _NsModConfigLineAupcSatTxPolarity_Type(Integer32):
    """Custom type nsModConfigLineAupcSatTxPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("circular-left", 2),
          ("circular-right", 3),
          ("horizontal", 1),
          ("notApplicable", 255),
          ("vertical", 0))
    )


_NsModConfigLineAupcSatTxPolarity_Type.__name__ = "Integer32"
_NsModConfigLineAupcSatTxPolarity_Object = MibScalar
nsModConfigLineAupcSatTxPolarity = _NsModConfigLineAupcSatTxPolarity_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 28),
    _NsModConfigLineAupcSatTxPolarity_Type()
)
nsModConfigLineAupcSatTxPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLineAupcSatTxPolarity.setStatus("current")


class _NsModConfigLineAupcMaxGain_Type(Integer32):
    """Custom type nsModConfigLineAupcMaxGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_NsModConfigLineAupcMaxGain_Type.__name__ = "Integer32"
_NsModConfigLineAupcMaxGain_Object = MibScalar
nsModConfigLineAupcMaxGain = _NsModConfigLineAupcMaxGain_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 29),
    _NsModConfigLineAupcMaxGain_Type()
)
nsModConfigLineAupcMaxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLineAupcMaxGain.setStatus("current")


class _NsModConfigLineAupcMaxAttn_Type(Integer32):
    """Custom type nsModConfigLineAupcMaxAttn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_NsModConfigLineAupcMaxAttn_Type.__name__ = "Integer32"
_NsModConfigLineAupcMaxAttn_Object = MibScalar
nsModConfigLineAupcMaxAttn = _NsModConfigLineAupcMaxAttn_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 1, 30),
    _NsModConfigLineAupcMaxAttn_Type()
)
nsModConfigLineAupcMaxAttn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigLineAupcMaxAttn.setStatus("current")
_NsModConfigChannel_ObjectIdentity = ObjectIdentity
nsModConfigChannel = _NsModConfigChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 2)
)
if mibBuilder.loadTexts:
    nsModConfigChannel.setStatus("current")
_NsModConfigChannelTable_Object = MibTable
nsModConfigChannelTable = _NsModConfigChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    nsModConfigChannelTable.setStatus("current")
_NsModConfigChannelEntry_Object = MibTableRow
nsModConfigChannelEntry = _NsModConfigChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 2, 1, 1)
)
nsModConfigChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nsModConfigChannelEntry.setStatus("current")


class _NsModConfigChStatus_Type(Integer32):
    """Custom type nsModConfigChStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("notApplicable", 255))
    )


_NsModConfigChStatus_Type.__name__ = "Integer32"
_NsModConfigChStatus_Object = MibTableColumn
nsModConfigChStatus = _NsModConfigChStatus_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 2, 1, 1, 1),
    _NsModConfigChStatus_Type()
)
nsModConfigChStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigChStatus.setStatus("current")


class _NsModConfigChSource_Type(Integer32):
    """Custom type nsModConfigChSource based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("asi1", 2),
          ("asi2", 3),
          ("disable", 5),
          ("g703", 6),
          ("gbeA", 0),
          ("gbeB", 1),
          ("gigE", 4),
          ("notApplicable", 255),
          ("test1", 7),
          ("test2", 8))
    )


_NsModConfigChSource_Type.__name__ = "Integer32"
_NsModConfigChSource_Object = MibTableColumn
nsModConfigChSource = _NsModConfigChSource_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 2, 1, 1, 2),
    _NsModConfigChSource_Type()
)
nsModConfigChSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigChSource.setStatus("current")


class _NsModConfigChNPD_Type(Integer32):
    """Custom type nsModConfigChNPD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("addition", 1),
          ("deletion", 2),
          ("none", 0),
          ("notApplicable", 255))
    )


_NsModConfigChNPD_Type.__name__ = "Integer32"
_NsModConfigChNPD_Object = MibTableColumn
nsModConfigChNPD = _NsModConfigChNPD_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 2, 1, 1, 3),
    _NsModConfigChNPD_Type()
)
nsModConfigChNPD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigChNPD.setStatus("current")


class _NsModConfigChFrameSize_Type(Integer32):
    """Custom type nsModConfigChFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("notApplicable", 255),
          ("short", 1))
    )


_NsModConfigChFrameSize_Type.__name__ = "Integer32"
_NsModConfigChFrameSize_Object = MibTableColumn
nsModConfigChFrameSize = _NsModConfigChFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 2, 1, 1, 4),
    _NsModConfigChFrameSize_Type()
)
nsModConfigChFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigChFrameSize.setStatus("current")


class _NsModConfigChModulation_Type(Integer32):
    """Custom type nsModConfigChModulation based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("modulation16Apsk", 4),
          ("modulation16Qam", 3),
          ("modulation32Apsk", 5),
          ("modulation64Apsk", 6),
          ("modulation8Psk", 2),
          ("modulationBpsk", 0),
          ("modulationQpsk", 1),
          ("notApplicable", 255))
    )


_NsModConfigChModulation_Type.__name__ = "Integer32"
_NsModConfigChModulation_Object = MibTableColumn
nsModConfigChModulation = _NsModConfigChModulation_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 2, 1, 1, 5),
    _NsModConfigChModulation_Type()
)
nsModConfigChModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigChModulation.setStatus("current")


class _NsModConfigChFECRate_Type(Integer32):
    """Custom type nsModConfigChFECRate based on Integer32"""
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
              20,
              21,
              22,
              23,
              24,
              25,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fec11Div15", 17),
          ("fec13Div30", 4),
          ("fec17Div30", 11),
          ("fec19Div30", 14),
          ("fec1Div2", 8),
          ("fec1Div3", 2),
          ("fec1Div4", 1),
          ("fec1Div5", 0),
          ("fec22Div45", 7),
          ("fec28Div45", 13),
          ("fec2Div3", 15),
          ("fec2Div5", 3),
          ("fec32Div45", 16),
          ("fec37Div45", 21),
          ("fec3Div4", 18),
          ("fec3Div5", 12),
          ("fec4Div5", 20),
          ("fec4Div9", 5),
          ("fec5Div6", 22),
          ("fec5Div9", 10),
          ("fec7Div15", 6),
          ("fec7Div8", 23),
          ("fec7Div9", 19),
          ("fec8Div15", 9),
          ("fec8Div9", 24),
          ("fec9Div10", 25),
          ("notApplicable", 255))
    )


_NsModConfigChFECRate_Type.__name__ = "Integer32"
_NsModConfigChFECRate_Object = MibTableColumn
nsModConfigChFECRate = _NsModConfigChFECRate_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 2, 1, 1, 6),
    _NsModConfigChFECRate_Type()
)
nsModConfigChFECRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigChFECRate.setStatus("current")


class _NsModConfigChPilot_Type(Integer32):
    """Custom type nsModConfigChPilot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 255),
          ("pilot16Slots", 2),
          ("pilot8Slots", 1),
          ("pilotNo", 0))
    )


_NsModConfigChPilot_Type.__name__ = "Integer32"
_NsModConfigChPilot_Object = MibTableColumn
nsModConfigChPilot = _NsModConfigChPilot_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 2, 1, 1, 7),
    _NsModConfigChPilot_Type()
)
nsModConfigChPilot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigChPilot.setStatus("current")


class _NsModConfigChISSY_Type(Integer32):
    """Custom type nsModConfigChISSY based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("issy2Bytes", 1),
          ("issy3Bytes", 2),
          ("issyDisabled", 0),
          ("notApplicable", 255))
    )


_NsModConfigChISSY_Type.__name__ = "Integer32"
_NsModConfigChISSY_Object = MibTableColumn
nsModConfigChISSY = _NsModConfigChISSY_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 2, 1, 1, 8),
    _NsModConfigChISSY_Type()
)
nsModConfigChISSY.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigChISSY.setStatus("current")


class _NsModConfigChStreamFormat_Type(Integer32):
    """Custom type nsModConfigChStreamFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("genericContinuous", 3),
          ("genericPacketsized", 2),
          ("notApplicable", 255),
          ("transport188", 0),
          ("transport204", 1))
    )


_NsModConfigChStreamFormat_Type.__name__ = "Integer32"
_NsModConfigChStreamFormat_Object = MibTableColumn
nsModConfigChStreamFormat = _NsModConfigChStreamFormat_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 2, 1, 1, 9),
    _NsModConfigChStreamFormat_Type()
)
nsModConfigChStreamFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigChStreamFormat.setStatus("current")


class _NsModConfigChPacketSize_Type(Integer32):
    """Custom type nsModConfigChPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsModConfigChPacketSize_Type.__name__ = "Integer32"
_NsModConfigChPacketSize_Object = MibTableColumn
nsModConfigChPacketSize = _NsModConfigChPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 2, 1, 1, 10),
    _NsModConfigChPacketSize_Type()
)
nsModConfigChPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigChPacketSize.setStatus("current")


class _NsModConfigChSyncByte_Type(Integer32):
    """Custom type nsModConfigChSyncByte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NsModConfigChSyncByte_Type.__name__ = "Integer32"
_NsModConfigChSyncByte_Object = MibTableColumn
nsModConfigChSyncByte = _NsModConfigChSyncByte_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 2, 1, 1, 11),
    _NsModConfigChSyncByte_Type()
)
nsModConfigChSyncByte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigChSyncByte.setStatus("current")


class _NsModConfigChIsi_Type(Integer32):
    """Custom type nsModConfigChIsi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NsModConfigChIsi_Type.__name__ = "Integer32"
_NsModConfigChIsi_Object = MibTableColumn
nsModConfigChIsi = _NsModConfigChIsi_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 2, 1, 1, 12),
    _NsModConfigChIsi_Type()
)
nsModConfigChIsi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigChIsi.setStatus("current")


class _NsModConfigChPCRRestamping_Type(Integer32):
    """Custom type nsModConfigChPCRRestamping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("notApplicable", 255))
    )


_NsModConfigChPCRRestamping_Type.__name__ = "Integer32"
_NsModConfigChPCRRestamping_Object = MibTableColumn
nsModConfigChPCRRestamping = _NsModConfigChPCRRestamping_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 2, 1, 1, 13),
    _NsModConfigChPCRRestamping_Type()
)
nsModConfigChPCRRestamping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigChPCRRestamping.setStatus("current")


class _NsModConfigChMpegProcessingMode_Type(Integer32):
    """Custom type nsModConfigChMpegProcessingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("dataAdjust", 1),
          ("notApplicable", 255),
          ("off", 0),
          ("partialDataAdjust", 3),
          ("symbolAdjust", 2))
    )


_NsModConfigChMpegProcessingMode_Type.__name__ = "Integer32"
_NsModConfigChMpegProcessingMode_Object = MibTableColumn
nsModConfigChMpegProcessingMode = _NsModConfigChMpegProcessingMode_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 2, 1, 1, 14),
    _NsModConfigChMpegProcessingMode_Type()
)
nsModConfigChMpegProcessingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigChMpegProcessingMode.setStatus("current")
_NsModConfigChBitRate_Type = Integer32
_NsModConfigChBitRate_Object = MibTableColumn
nsModConfigChBitRate = _NsModConfigChBitRate_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 2, 1, 1, 15),
    _NsModConfigChBitRate_Type()
)
nsModConfigChBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigChBitRate.setStatus("current")
_NsModConfigChBitRatePercent_Type = Integer32
_NsModConfigChBitRatePercent_Object = MibTableColumn
nsModConfigChBitRatePercent = _NsModConfigChBitRatePercent_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 2, 1, 1, 16),
    _NsModConfigChBitRatePercent_Type()
)
nsModConfigChBitRatePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModConfigChBitRatePercent.setStatus("current")


class _NsModConfigChTSProtect_Type(Integer32):
    """Custom type nsModConfigChTSProtect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notApplicable", 255))
    )


_NsModConfigChTSProtect_Type.__name__ = "Integer32"
_NsModConfigChTSProtect_Object = MibTableColumn
nsModConfigChTSProtect = _NsModConfigChTSProtect_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 2, 1, 1, 17),
    _NsModConfigChTSProtect_Type()
)
nsModConfigChTSProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigChTSProtect.setStatus("current")
_NsModConfigInterface_ObjectIdentity = ObjectIdentity
nsModConfigInterface = _NsModConfigInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 3)
)
if mibBuilder.loadTexts:
    nsModConfigInterface.setStatus("current")
_NsModConfigInterfaceTestTable_Object = MibTable
nsModConfigInterfaceTestTable = _NsModConfigInterfaceTestTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    nsModConfigInterfaceTestTable.setStatus("current")
_NsModConfigInterfaceTestEntry_Object = MibTableRow
nsModConfigInterfaceTestEntry = _NsModConfigInterfaceTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 3, 1, 1)
)
nsModConfigInterfaceTestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nsModConfigInterfaceTestEntry.setStatus("current")


class _NsModConfigInterfaceTestPattern_Type(Integer32):
    """Custom type nsModConfigInterfaceTestPattern based on Integer32"""
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
              20,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 255),
          ("pattern00FF", 19),
          ("pattern2BitAlternate", 11),
          ("pattern2Pwr11Neg1", 2),
          ("pattern2Pwr15Neg1", 3),
          ("pattern2Pwr20Neg1", 4),
          ("pattern2Pwr23Neg1", 5),
          ("pattern2Pwr29Neg1", 6),
          ("pattern2Pwr31Neg1", 7),
          ("pattern2Pwr7Neg1", 0),
          ("pattern2Pwr9Neg1", 1),
          ("pattern55AA", 16),
          ("pattern6699", 17),
          ("pattern6Ones", 14),
          ("pattern6Zeros", 15),
          ("pattern7Ones", 12),
          ("pattern7Zeros", 13),
          ("patternAllOnes", 9),
          ("patternAllZeros", 8),
          ("patternBitAlternate", 10),
          ("patternC33C", 18),
          ("patternSAWTOOTH", 20))
    )


_NsModConfigInterfaceTestPattern_Type.__name__ = "Integer32"
_NsModConfigInterfaceTestPattern_Object = MibTableColumn
nsModConfigInterfaceTestPattern = _NsModConfigInterfaceTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 3, 1, 1, 1),
    _NsModConfigInterfaceTestPattern_Type()
)
nsModConfigInterfaceTestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigInterfaceTestPattern.setStatus("current")


class _NsModConfigInterfaceTestInvert_Type(Integer32):
    """Custom type nsModConfigInterfaceTestInvert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("notApplicable", 255),
          ("yes", 1))
    )


_NsModConfigInterfaceTestInvert_Type.__name__ = "Integer32"
_NsModConfigInterfaceTestInvert_Object = MibTableColumn
nsModConfigInterfaceTestInvert = _NsModConfigInterfaceTestInvert_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 3, 1, 1, 2),
    _NsModConfigInterfaceTestInvert_Type()
)
nsModConfigInterfaceTestInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigInterfaceTestInvert.setStatus("current")
_NsModConfigInterfaceASITable_Object = MibTable
nsModConfigInterfaceASITable = _NsModConfigInterfaceASITable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    nsModConfigInterfaceASITable.setStatus("current")
_NsModConfigInterfaceASIEntry_Object = MibTableRow
nsModConfigInterfaceASIEntry = _NsModConfigInterfaceASIEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 3, 2, 1)
)
nsModConfigInterfaceASIEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nsModConfigInterfaceASIEntry.setStatus("current")


class _NsModConfigInterfaceASIDataOrder_Type(Integer32):
    """Custom type nsModConfigInterfaceASIDataOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("lsb", 0),
          ("msb", 1),
          ("notApplicable", 255))
    )


_NsModConfigInterfaceASIDataOrder_Type.__name__ = "Integer32"
_NsModConfigInterfaceASIDataOrder_Object = MibTableColumn
nsModConfigInterfaceASIDataOrder = _NsModConfigInterfaceASIDataOrder_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 3, 2, 1, 1),
    _NsModConfigInterfaceASIDataOrder_Type()
)
nsModConfigInterfaceASIDataOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigInterfaceASIDataOrder.setStatus("current")
_NsModConfigInterfaceEthernetTable_Object = MibTable
nsModConfigInterfaceEthernetTable = _NsModConfigInterfaceEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    nsModConfigInterfaceEthernetTable.setStatus("current")
_NsModConfigInterfaceEthernetEntry_Object = MibTableRow
nsModConfigInterfaceEthernetEntry = _NsModConfigInterfaceEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 3, 3, 1)
)
nsModConfigInterfaceEthernetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nsModConfigInterfaceEthernetEntry.setStatus("current")


class _NsModConfigInterfaceEthernetAutoNegotiation_Type(Integer32):
    """Custom type nsModConfigInterfaceEthernetAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notApplicable", 255))
    )


_NsModConfigInterfaceEthernetAutoNegotiation_Type.__name__ = "Integer32"
_NsModConfigInterfaceEthernetAutoNegotiation_Object = MibTableColumn
nsModConfigInterfaceEthernetAutoNegotiation = _NsModConfigInterfaceEthernetAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 3, 3, 1, 1),
    _NsModConfigInterfaceEthernetAutoNegotiation_Type()
)
nsModConfigInterfaceEthernetAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigInterfaceEthernetAutoNegotiation.setStatus("current")


class _NsModConfigInterfaceEthernetSpeed_Type(Integer32):
    """Custom type nsModConfigInterfaceEthernetSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 255),
          ("speed10", 0),
          ("speed100", 1))
    )


_NsModConfigInterfaceEthernetSpeed_Type.__name__ = "Integer32"
_NsModConfigInterfaceEthernetSpeed_Object = MibTableColumn
nsModConfigInterfaceEthernetSpeed = _NsModConfigInterfaceEthernetSpeed_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 3, 3, 1, 2),
    _NsModConfigInterfaceEthernetSpeed_Type()
)
nsModConfigInterfaceEthernetSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigInterfaceEthernetSpeed.setStatus("current")


class _NsModConfigInterfaceEthernetDuplex_Type(Integer32):
    """Custom type nsModConfigInterfaceEthernetDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 0),
          ("notApplicable", 255))
    )


_NsModConfigInterfaceEthernetDuplex_Type.__name__ = "Integer32"
_NsModConfigInterfaceEthernetDuplex_Object = MibTableColumn
nsModConfigInterfaceEthernetDuplex = _NsModConfigInterfaceEthernetDuplex_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 3, 3, 1, 3),
    _NsModConfigInterfaceEthernetDuplex_Type()
)
nsModConfigInterfaceEthernetDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigInterfaceEthernetDuplex.setStatus("current")


class _NsModConfigInterfaceEthernetEncapsulation_Type(Integer32):
    """Custom type nsModConfigInterfaceEthernetEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("gse", 2),
          ("notApplicable", 255),
          ("nspe", 1),
          ("raw", 0),
          ("ule", 3))
    )


_NsModConfigInterfaceEthernetEncapsulation_Type.__name__ = "Integer32"
_NsModConfigInterfaceEthernetEncapsulation_Object = MibTableColumn
nsModConfigInterfaceEthernetEncapsulation = _NsModConfigInterfaceEthernetEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 3, 3, 1, 4),
    _NsModConfigInterfaceEthernetEncapsulation_Type()
)
nsModConfigInterfaceEthernetEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigInterfaceEthernetEncapsulation.setStatus("current")


class _NsModConfigInterfaceEthernetPid_Type(Integer32):
    """Custom type nsModConfigInterfaceEthernetPid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 8191),
    )


_NsModConfigInterfaceEthernetPid_Type.__name__ = "Integer32"
_NsModConfigInterfaceEthernetPid_Object = MibTableColumn
nsModConfigInterfaceEthernetPid = _NsModConfigInterfaceEthernetPid_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 3, 3, 1, 5),
    _NsModConfigInterfaceEthernetPid_Type()
)
nsModConfigInterfaceEthernetPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigInterfaceEthernetPid.setStatus("current")
_NsModConfigInterfaceGigETable_Object = MibTable
nsModConfigInterfaceGigETable = _NsModConfigInterfaceGigETable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 3, 4)
)
if mibBuilder.loadTexts:
    nsModConfigInterfaceGigETable.setStatus("current")
_NsModConfigInterfaceGigEEntry_Object = MibTableRow
nsModConfigInterfaceGigEEntry = _NsModConfigInterfaceGigEEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 3, 4, 1)
)
nsModConfigInterfaceGigEEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nsModConfigInterfaceGigEEntry.setStatus("current")


class _NsModConfigInterfaceGigEAutoNegotiation_Type(Integer32):
    """Custom type nsModConfigInterfaceGigEAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notApplicable", 255))
    )


_NsModConfigInterfaceGigEAutoNegotiation_Type.__name__ = "Integer32"
_NsModConfigInterfaceGigEAutoNegotiation_Object = MibTableColumn
nsModConfigInterfaceGigEAutoNegotiation = _NsModConfigInterfaceGigEAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 3, 4, 1, 1),
    _NsModConfigInterfaceGigEAutoNegotiation_Type()
)
nsModConfigInterfaceGigEAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigInterfaceGigEAutoNegotiation.setStatus("current")


class _NsModConfigInterfaceGigESpeed_Type(Integer32):
    """Custom type nsModConfigInterfaceGigESpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 255),
          ("speed10", 0),
          ("speed100", 1))
    )


_NsModConfigInterfaceGigESpeed_Type.__name__ = "Integer32"
_NsModConfigInterfaceGigESpeed_Object = MibTableColumn
nsModConfigInterfaceGigESpeed = _NsModConfigInterfaceGigESpeed_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 3, 4, 1, 2),
    _NsModConfigInterfaceGigESpeed_Type()
)
nsModConfigInterfaceGigESpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigInterfaceGigESpeed.setStatus("current")


class _NsModConfigInterfaceGigEDuplex_Type(Integer32):
    """Custom type nsModConfigInterfaceGigEDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 0),
          ("notApplicable", 255))
    )


_NsModConfigInterfaceGigEDuplex_Type.__name__ = "Integer32"
_NsModConfigInterfaceGigEDuplex_Object = MibTableColumn
nsModConfigInterfaceGigEDuplex = _NsModConfigInterfaceGigEDuplex_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 3, 4, 1, 3),
    _NsModConfigInterfaceGigEDuplex_Type()
)
nsModConfigInterfaceGigEDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigInterfaceGigEDuplex.setStatus("current")


class _NsModConfigInterfaceGigEPortType_Type(Integer32):
    """Custom type nsModConfigInterfaceGigEPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 255),
          ("rj45", 0),
          ("sfp", 1))
    )


_NsModConfigInterfaceGigEPortType_Type.__name__ = "Integer32"
_NsModConfigInterfaceGigEPortType_Object = MibTableColumn
nsModConfigInterfaceGigEPortType = _NsModConfigInterfaceGigEPortType_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 3, 4, 1, 5),
    _NsModConfigInterfaceGigEPortType_Type()
)
nsModConfigInterfaceGigEPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigInterfaceGigEPortType.setStatus("current")
_NsModConfigCid_ObjectIdentity = ObjectIdentity
nsModConfigCid = _NsModConfigCid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 4)
)
if mibBuilder.loadTexts:
    nsModConfigCid.setStatus("current")


class _NsModConfigCidState_Type(Integer32):
    """Custom type nsModConfigCidState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("notApplicable", 255))
    )


_NsModConfigCidState_Type.__name__ = "Integer32"
_NsModConfigCidState_Object = MibScalar
nsModConfigCidState = _NsModConfigCidState_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 4, 1),
    _NsModConfigCidState_Type()
)
nsModConfigCidState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigCidState.setStatus("current")


class _NsModConfigCidLatitude_Type(DisplayString):
    """Custom type nsModConfigCidLatitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsModConfigCidLatitude_Type.__name__ = "DisplayString"
_NsModConfigCidLatitude_Object = MibScalar
nsModConfigCidLatitude = _NsModConfigCidLatitude_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 4, 2),
    _NsModConfigCidLatitude_Type()
)
nsModConfigCidLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigCidLatitude.setStatus("current")


class _NsModConfigCidLongitude_Type(DisplayString):
    """Custom type nsModConfigCidLongitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsModConfigCidLongitude_Type.__name__ = "DisplayString"
_NsModConfigCidLongitude_Object = MibScalar
nsModConfigCidLongitude = _NsModConfigCidLongitude_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 4, 3),
    _NsModConfigCidLongitude_Type()
)
nsModConfigCidLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigCidLongitude.setStatus("current")


class _NsModConfigCidPhone_Type(DisplayString):
    """Custom type nsModConfigCidPhone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsModConfigCidPhone_Type.__name__ = "DisplayString"
_NsModConfigCidPhone_Object = MibScalar
nsModConfigCidPhone = _NsModConfigCidPhone_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 4, 4),
    _NsModConfigCidPhone_Type()
)
nsModConfigCidPhone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigCidPhone.setStatus("current")


class _NsModConfigCidExtension_Type(DisplayString):
    """Custom type nsModConfigCidExtension based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsModConfigCidExtension_Type.__name__ = "DisplayString"
_NsModConfigCidExtension_Object = MibScalar
nsModConfigCidExtension = _NsModConfigCidExtension_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 4, 5),
    _NsModConfigCidExtension_Type()
)
nsModConfigCidExtension.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigCidExtension.setStatus("current")


class _NsModConfigCidUsertext_Type(DisplayString):
    """Custom type nsModConfigCidUsertext based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsModConfigCidUsertext_Type.__name__ = "DisplayString"
_NsModConfigCidUsertext_Object = MibScalar
nsModConfigCidUsertext = _NsModConfigCidUsertext_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 1, 4, 6),
    _NsModConfigCidUsertext_Type()
)
nsModConfigCidUsertext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModConfigCidUsertext.setStatus("current")
_NsModMonitor_ObjectIdentity = ObjectIdentity
nsModMonitor = _NsModMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2)
)
if mibBuilder.loadTexts:
    nsModMonitor.setStatus("current")
_NsModMonitorInterface_ObjectIdentity = ObjectIdentity
nsModMonitorInterface = _NsModMonitorInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 1)
)
if mibBuilder.loadTexts:
    nsModMonitorInterface.setStatus("current")
_NsModMonitorInterfaceTable_Object = MibTable
nsModMonitorInterfaceTable = _NsModMonitorInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nsModMonitorInterfaceTable.setStatus("current")
_NsModMonitorInterfaceEntry_Object = MibTableRow
nsModMonitorInterfaceEntry = _NsModMonitorInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 1, 1, 1)
)
nsModMonitorInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nsModMonitorInterfaceEntry.setStatus("current")
_NsModMonitorInterfaceDataRate_Type = Counter32
_NsModMonitorInterfaceDataRate_Object = MibTableColumn
nsModMonitorInterfaceDataRate = _NsModMonitorInterfaceDataRate_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 1, 1, 1, 1),
    _NsModMonitorInterfaceDataRate_Type()
)
nsModMonitorInterfaceDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorInterfaceDataRate.setStatus("current")


class _NsModMonitorInterfaceStatus_Type(Integer32):
    """Custom type nsModMonitorInterfaceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 2),
          ("locked", 1),
          ("notApplicable", 255),
          ("notLocked", 0))
    )


_NsModMonitorInterfaceStatus_Type.__name__ = "Integer32"
_NsModMonitorInterfaceStatus_Object = MibTableColumn
nsModMonitorInterfaceStatus = _NsModMonitorInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 1, 1, 1, 2),
    _NsModMonitorInterfaceStatus_Type()
)
nsModMonitorInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorInterfaceStatus.setStatus("current")


class _NsModMonitorInterfaceChannel_Type(Integer32):
    """Custom type nsModMonitorInterfaceChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("channel-1", 1),
          ("channel-2", 2),
          ("none", 0),
          ("notApplicable", 255))
    )


_NsModMonitorInterfaceChannel_Type.__name__ = "Integer32"
_NsModMonitorInterfaceChannel_Object = MibTableColumn
nsModMonitorInterfaceChannel = _NsModMonitorInterfaceChannel_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 1, 1, 1, 3),
    _NsModMonitorInterfaceChannel_Type()
)
nsModMonitorInterfaceChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorInterfaceChannel.setStatus("current")


class _NsModMonitorInterfaceName_Type(DisplayString):
    """Custom type nsModMonitorInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsModMonitorInterfaceName_Type.__name__ = "DisplayString"
_NsModMonitorInterfaceName_Object = MibTableColumn
nsModMonitorInterfaceName = _NsModMonitorInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 1, 1, 1, 4),
    _NsModMonitorInterfaceName_Type()
)
nsModMonitorInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorInterfaceName.setStatus("current")
_NsModMonitorSystem_ObjectIdentity = ObjectIdentity
nsModMonitorSystem = _NsModMonitorSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 2)
)
if mibBuilder.loadTexts:
    nsModMonitorSystem.setStatus("current")
_NsModMonitorSystemBoardTmp_Type = Integer32
_NsModMonitorSystemBoardTmp_Object = MibScalar
nsModMonitorSystemBoardTmp = _NsModMonitorSystemBoardTmp_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 2, 1),
    _NsModMonitorSystemBoardTmp_Type()
)
nsModMonitorSystemBoardTmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorSystemBoardTmp.setStatus("current")


class _NsModMonitorSystem10MHrzClkSource_Type(Integer32):
    """Custom type nsModMonitorSystem10MHrzClkSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 0),
          ("notApplicable", 255))
    )


_NsModMonitorSystem10MHrzClkSource_Type.__name__ = "Integer32"
_NsModMonitorSystem10MHrzClkSource_Object = MibScalar
nsModMonitorSystem10MHrzClkSource = _NsModMonitorSystem10MHrzClkSource_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 2, 2),
    _NsModMonitorSystem10MHrzClkSource_Type()
)
nsModMonitorSystem10MHrzClkSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorSystem10MHrzClkSource.setStatus("current")


class _NsModMonitorSystemRefClkOut_Type(Integer32):
    """Custom type nsModMonitorSystemRefClkOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 255),
          ("off", 0),
          ("on", 1))
    )


_NsModMonitorSystemRefClkOut_Type.__name__ = "Integer32"
_NsModMonitorSystemRefClkOut_Object = MibScalar
nsModMonitorSystemRefClkOut = _NsModMonitorSystemRefClkOut_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 2, 3),
    _NsModMonitorSystemRefClkOut_Type()
)
nsModMonitorSystemRefClkOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorSystemRefClkOut.setStatus("current")


class _NsModMonitorSystemTxPortClk_Type(Integer32):
    """Custom type nsModMonitorSystemTxPortClk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("buc", 2),
          ("lband", 1),
          ("notApplicable", 255),
          ("off", 0))
    )


_NsModMonitorSystemTxPortClk_Type.__name__ = "Integer32"
_NsModMonitorSystemTxPortClk_Object = MibScalar
nsModMonitorSystemTxPortClk = _NsModMonitorSystemTxPortClk_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 2, 4),
    _NsModMonitorSystemTxPortClk_Type()
)
nsModMonitorSystemTxPortClk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorSystemTxPortClk.setStatus("current")
_NsModMonitorEthernet_ObjectIdentity = ObjectIdentity
nsModMonitorEthernet = _NsModMonitorEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 3)
)
if mibBuilder.loadTexts:
    nsModMonitorEthernet.setStatus("current")
_NsModMonitorEthernetTable_Object = MibTable
nsModMonitorEthernetTable = _NsModMonitorEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    nsModMonitorEthernetTable.setStatus("current")
_NsModMonitorEthernetEntry_Object = MibTableRow
nsModMonitorEthernetEntry = _NsModMonitorEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 3, 1, 1)
)
nsModMonitorEthernetEntry.setIndexNames(
    (0, "NOVELSAT-MODULATOR-MIB", "nsModMonitorEthernetStatisticsNumber"),
)
if mibBuilder.loadTexts:
    nsModMonitorEthernetEntry.setStatus("current")
_NsModMonitorEthernetStatisticsNumber_Type = Counter32
_NsModMonitorEthernetStatisticsNumber_Object = MibTableColumn
nsModMonitorEthernetStatisticsNumber = _NsModMonitorEthernetStatisticsNumber_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 3, 1, 1, 1),
    _NsModMonitorEthernetStatisticsNumber_Type()
)
nsModMonitorEthernetStatisticsNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsModMonitorEthernetStatisticsNumber.setStatus("current")


class _NsModMonitorEthernetStatisticsName_Type(DisplayString):
    """Custom type nsModMonitorEthernetStatisticsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsModMonitorEthernetStatisticsName_Type.__name__ = "DisplayString"
_NsModMonitorEthernetStatisticsName_Object = MibTableColumn
nsModMonitorEthernetStatisticsName = _NsModMonitorEthernetStatisticsName_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 3, 1, 1, 2),
    _NsModMonitorEthernetStatisticsName_Type()
)
nsModMonitorEthernetStatisticsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorEthernetStatisticsName.setStatus("current")
_NsModMonitorEthernetStatisticsValueA_Type = Integer32
_NsModMonitorEthernetStatisticsValueA_Object = MibTableColumn
nsModMonitorEthernetStatisticsValueA = _NsModMonitorEthernetStatisticsValueA_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 3, 1, 1, 3),
    _NsModMonitorEthernetStatisticsValueA_Type()
)
nsModMonitorEthernetStatisticsValueA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorEthernetStatisticsValueA.setStatus("current")
_NsModMonitorEthernetStatisticsValueB_Type = Integer32
_NsModMonitorEthernetStatisticsValueB_Object = MibTableColumn
nsModMonitorEthernetStatisticsValueB = _NsModMonitorEthernetStatisticsValueB_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 3, 1, 1, 4),
    _NsModMonitorEthernetStatisticsValueB_Type()
)
nsModMonitorEthernetStatisticsValueB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorEthernetStatisticsValueB.setStatus("current")
_NsModMonitorAcm_ObjectIdentity = ObjectIdentity
nsModMonitorAcm = _NsModMonitorAcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 4)
)
if mibBuilder.loadTexts:
    nsModMonitorAcm.setStatus("current")
_NsModMonitorAcmTable_Object = MibTable
nsModMonitorAcmTable = _NsModMonitorAcmTable_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    nsModMonitorAcmTable.setStatus("current")
_NsModMonitorAcmEntry_Object = MibTableRow
nsModMonitorAcmEntry = _NsModMonitorAcmEntry_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 4, 1, 1)
)
nsModMonitorAcmEntry.setIndexNames(
    (0, "NOVELSAT-MODULATOR-MIB", "nsModMonitorAcmStatisticsNumber"),
)
if mibBuilder.loadTexts:
    nsModMonitorAcmEntry.setStatus("current")
_NsModMonitorAcmStatisticsNumber_Type = Unsigned32
_NsModMonitorAcmStatisticsNumber_Object = MibTableColumn
nsModMonitorAcmStatisticsNumber = _NsModMonitorAcmStatisticsNumber_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 4, 1, 1, 1),
    _NsModMonitorAcmStatisticsNumber_Type()
)
nsModMonitorAcmStatisticsNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nsModMonitorAcmStatisticsNumber.setStatus("current")
_NsModMonitorAcmStatisticsClientIp_Type = IpAddress
_NsModMonitorAcmStatisticsClientIp_Object = MibTableColumn
nsModMonitorAcmStatisticsClientIp = _NsModMonitorAcmStatisticsClientIp_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 4, 1, 1, 2),
    _NsModMonitorAcmStatisticsClientIp_Type()
)
nsModMonitorAcmStatisticsClientIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorAcmStatisticsClientIp.setStatus("current")


class _NsModMonitorAcmStatisticsClientName_Type(DisplayString):
    """Custom type nsModMonitorAcmStatisticsClientName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsModMonitorAcmStatisticsClientName_Type.__name__ = "DisplayString"
_NsModMonitorAcmStatisticsClientName_Object = MibTableColumn
nsModMonitorAcmStatisticsClientName = _NsModMonitorAcmStatisticsClientName_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 4, 1, 1, 3),
    _NsModMonitorAcmStatisticsClientName_Type()
)
nsModMonitorAcmStatisticsClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorAcmStatisticsClientName.setStatus("current")
_NsModMonitorAcmStatisticsClientSnr_Type = Integer32
_NsModMonitorAcmStatisticsClientSnr_Object = MibTableColumn
nsModMonitorAcmStatisticsClientSnr = _NsModMonitorAcmStatisticsClientSnr_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 4, 1, 1, 4),
    _NsModMonitorAcmStatisticsClientSnr_Type()
)
nsModMonitorAcmStatisticsClientSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorAcmStatisticsClientSnr.setStatus("current")
_NsModMonitorAcmStatisticsClientMargin_Type = Integer32
_NsModMonitorAcmStatisticsClientMargin_Object = MibTableColumn
nsModMonitorAcmStatisticsClientMargin = _NsModMonitorAcmStatisticsClientMargin_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 4, 1, 1, 5),
    _NsModMonitorAcmStatisticsClientMargin_Type()
)
nsModMonitorAcmStatisticsClientMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorAcmStatisticsClientMargin.setStatus("current")


class _NsModMonitorAcmStatisticsChannelNum_Type(Integer32):
    """Custom type nsModMonitorAcmStatisticsChannelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("channel-1", 0),
          ("channel-2", 1),
          ("notApplicable", 255))
    )


_NsModMonitorAcmStatisticsChannelNum_Type.__name__ = "Integer32"
_NsModMonitorAcmStatisticsChannelNum_Object = MibTableColumn
nsModMonitorAcmStatisticsChannelNum = _NsModMonitorAcmStatisticsChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 4, 1, 1, 6),
    _NsModMonitorAcmStatisticsChannelNum_Type()
)
nsModMonitorAcmStatisticsChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorAcmStatisticsChannelNum.setStatus("current")


class _NsModMonitorAcmStatisticsLineMode_Type(Integer32):
    """Custom type nsModMonitorAcmStatisticsLineMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("dsng", 1),
          ("dvbs", 0),
          ("dvbs2", 2),
          ("notApplicable", 255),
          ("ns3", 3))
    )


_NsModMonitorAcmStatisticsLineMode_Type.__name__ = "Integer32"
_NsModMonitorAcmStatisticsLineMode_Object = MibTableColumn
nsModMonitorAcmStatisticsLineMode = _NsModMonitorAcmStatisticsLineMode_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 4, 1, 1, 7),
    _NsModMonitorAcmStatisticsLineMode_Type()
)
nsModMonitorAcmStatisticsLineMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorAcmStatisticsLineMode.setStatus("current")


class _NsModMonitorAcmStatisticsModulation_Type(Integer32):
    """Custom type nsModMonitorAcmStatisticsModulation based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("modulation16Apsk", 4),
          ("modulation16Qam", 3),
          ("modulation32Apsk", 5),
          ("modulation64Apsk", 6),
          ("modulation8Psk", 2),
          ("modulationBpsk", 0),
          ("modulationQpsk", 1),
          ("notApplicable", 255))
    )


_NsModMonitorAcmStatisticsModulation_Type.__name__ = "Integer32"
_NsModMonitorAcmStatisticsModulation_Object = MibTableColumn
nsModMonitorAcmStatisticsModulation = _NsModMonitorAcmStatisticsModulation_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 4, 1, 1, 8),
    _NsModMonitorAcmStatisticsModulation_Type()
)
nsModMonitorAcmStatisticsModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorAcmStatisticsModulation.setStatus("current")


class _NsModMonitorAcmStatisticsFecRate_Type(Integer32):
    """Custom type nsModMonitorAcmStatisticsFecRate based on Integer32"""
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
              20,
              21,
              22,
              23,
              24,
              25,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fec11Div15", 17),
          ("fec13Div30", 4),
          ("fec17Div30", 11),
          ("fec19Div30", 14),
          ("fec1Div2", 8),
          ("fec1Div3", 2),
          ("fec1Div4", 1),
          ("fec1Div5", 0),
          ("fec22Div45", 7),
          ("fec28Div45", 13),
          ("fec2Div3", 15),
          ("fec2Div5", 3),
          ("fec32Div45", 16),
          ("fec37Div45", 21),
          ("fec3Div4", 18),
          ("fec3Div5", 12),
          ("fec4Div5", 20),
          ("fec4Div9", 5),
          ("fec5Div6", 22),
          ("fec5Div9", 10),
          ("fec7Div15", 6),
          ("fec7Div8", 23),
          ("fec7Div9", 19),
          ("fec8Div15", 9),
          ("fec8Div9", 24),
          ("fec9Div10", 25),
          ("notApplicable", 255))
    )


_NsModMonitorAcmStatisticsFecRate_Type.__name__ = "Integer32"
_NsModMonitorAcmStatisticsFecRate_Object = MibTableColumn
nsModMonitorAcmStatisticsFecRate = _NsModMonitorAcmStatisticsFecRate_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 4, 1, 1, 9),
    _NsModMonitorAcmStatisticsFecRate_Type()
)
nsModMonitorAcmStatisticsFecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorAcmStatisticsFecRate.setStatus("current")


class _NsModMonitorAcmStatisticsFrameSize_Type(Integer32):
    """Custom type nsModMonitorAcmStatisticsFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("notApplicable", 255),
          ("short", 1))
    )


_NsModMonitorAcmStatisticsFrameSize_Type.__name__ = "Integer32"
_NsModMonitorAcmStatisticsFrameSize_Object = MibTableColumn
nsModMonitorAcmStatisticsFrameSize = _NsModMonitorAcmStatisticsFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 4, 1, 1, 10),
    _NsModMonitorAcmStatisticsFrameSize_Type()
)
nsModMonitorAcmStatisticsFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorAcmStatisticsFrameSize.setStatus("current")


class _NsModMonitorAcmStatisticsPilot_Type(Integer32):
    """Custom type nsModMonitorAcmStatisticsPilot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 255),
          ("pilot16Slots", 1),
          ("pilot8Slots", 2),
          ("pilotNo", 0))
    )


_NsModMonitorAcmStatisticsPilot_Type.__name__ = "Integer32"
_NsModMonitorAcmStatisticsPilot_Object = MibTableColumn
nsModMonitorAcmStatisticsPilot = _NsModMonitorAcmStatisticsPilot_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 4, 1, 1, 11),
    _NsModMonitorAcmStatisticsPilot_Type()
)
nsModMonitorAcmStatisticsPilot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorAcmStatisticsPilot.setStatus("current")


class _NsModMonitorAcmStatisticsIsLocked_Type(Integer32):
    """Custom type nsModMonitorAcmStatisticsIsLocked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("notApplicable", 255),
          ("yes", 1))
    )


_NsModMonitorAcmStatisticsIsLocked_Type.__name__ = "Integer32"
_NsModMonitorAcmStatisticsIsLocked_Object = MibTableColumn
nsModMonitorAcmStatisticsIsLocked = _NsModMonitorAcmStatisticsIsLocked_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 4, 1, 1, 12),
    _NsModMonitorAcmStatisticsIsLocked_Type()
)
nsModMonitorAcmStatisticsIsLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorAcmStatisticsIsLocked.setStatus("current")


class _NsModMonitorAcmStatisticsIsWorstCase_Type(Integer32):
    """Custom type nsModMonitorAcmStatisticsIsWorstCase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("notApplicable", 255),
          ("yes", 1))
    )


_NsModMonitorAcmStatisticsIsWorstCase_Type.__name__ = "Integer32"
_NsModMonitorAcmStatisticsIsWorstCase_Object = MibTableColumn
nsModMonitorAcmStatisticsIsWorstCase = _NsModMonitorAcmStatisticsIsWorstCase_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 4, 1, 1, 13),
    _NsModMonitorAcmStatisticsIsWorstCase_Type()
)
nsModMonitorAcmStatisticsIsWorstCase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorAcmStatisticsIsWorstCase.setStatus("current")


class _NsModMonitorAcmStatisticsState_Type(Integer32):
    """Custom type nsModMonitorAcmStatisticsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("idle", 3),
          ("lost", 2),
          ("notApplicable", 255),
          ("progress", 1))
    )


_NsModMonitorAcmStatisticsState_Type.__name__ = "Integer32"
_NsModMonitorAcmStatisticsState_Object = MibTableColumn
nsModMonitorAcmStatisticsState = _NsModMonitorAcmStatisticsState_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 4, 1, 1, 14),
    _NsModMonitorAcmStatisticsState_Type()
)
nsModMonitorAcmStatisticsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorAcmStatisticsState.setStatus("current")
_NsModMonitorAcmStatisticsGroup_Type = Unsigned32
_NsModMonitorAcmStatisticsGroup_Object = MibTableColumn
nsModMonitorAcmStatisticsGroup = _NsModMonitorAcmStatisticsGroup_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 4, 1, 1, 15),
    _NsModMonitorAcmStatisticsGroup_Type()
)
nsModMonitorAcmStatisticsGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorAcmStatisticsGroup.setStatus("current")


class _NsModMonitorAcmStatisticsClrCmd_Type(Integer32):
    """Custom type nsModMonitorAcmStatisticsClrCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("execute", 1),
          ("none", 0),
          ("notApplicable", 255))
    )


_NsModMonitorAcmStatisticsClrCmd_Type.__name__ = "Integer32"
_NsModMonitorAcmStatisticsClrCmd_Object = MibScalar
nsModMonitorAcmStatisticsClrCmd = _NsModMonitorAcmStatisticsClrCmd_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 4, 2),
    _NsModMonitorAcmStatisticsClrCmd_Type()
)
nsModMonitorAcmStatisticsClrCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModMonitorAcmStatisticsClrCmd.setStatus("current")
_NsModMonitorAupc_ObjectIdentity = ObjectIdentity
nsModMonitorAupc = _NsModMonitorAupc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 5)
)
if mibBuilder.loadTexts:
    nsModMonitorAupc.setStatus("current")
_NsModMonitorAupcCurrentPower_Type = Integer32
_NsModMonitorAupcCurrentPower_Object = MibScalar
nsModMonitorAupcCurrentPower = _NsModMonitorAupcCurrentPower_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 5, 1),
    _NsModMonitorAupcCurrentPower_Type()
)
nsModMonitorAupcCurrentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorAupcCurrentPower.setStatus("current")
_NsModMonitorAupcMinimalPower_Type = Integer32
_NsModMonitorAupcMinimalPower_Object = MibScalar
nsModMonitorAupcMinimalPower = _NsModMonitorAupcMinimalPower_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 5, 2),
    _NsModMonitorAupcMinimalPower_Type()
)
nsModMonitorAupcMinimalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorAupcMinimalPower.setStatus("current")
_NsModMonitorAupcMaximalPower_Type = Integer32
_NsModMonitorAupcMaximalPower_Object = MibScalar
nsModMonitorAupcMaximalPower = _NsModMonitorAupcMaximalPower_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 5, 3),
    _NsModMonitorAupcMaximalPower_Type()
)
nsModMonitorAupcMaximalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorAupcMaximalPower.setStatus("current")
_NsModMonitorAupcAveragePower_Type = Integer32
_NsModMonitorAupcAveragePower_Object = MibScalar
nsModMonitorAupcAveragePower = _NsModMonitorAupcAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 5, 4),
    _NsModMonitorAupcAveragePower_Type()
)
nsModMonitorAupcAveragePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorAupcAveragePower.setStatus("current")
_NsModMonitorAupcEstimatedUplinkAttn_Type = Integer32
_NsModMonitorAupcEstimatedUplinkAttn_Object = MibScalar
nsModMonitorAupcEstimatedUplinkAttn = _NsModMonitorAupcEstimatedUplinkAttn_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 5, 5),
    _NsModMonitorAupcEstimatedUplinkAttn_Type()
)
nsModMonitorAupcEstimatedUplinkAttn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorAupcEstimatedUplinkAttn.setStatus("current")
_NsModMonitorAupcEstimatedDownlinkAttn_Type = Integer32
_NsModMonitorAupcEstimatedDownlinkAttn_Object = MibScalar
nsModMonitorAupcEstimatedDownlinkAttn = _NsModMonitorAupcEstimatedDownlinkAttn_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 5, 6),
    _NsModMonitorAupcEstimatedDownlinkAttn_Type()
)
nsModMonitorAupcEstimatedDownlinkAttn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsModMonitorAupcEstimatedDownlinkAttn.setStatus("current")


class _NsModMonitorAupcResetAvgCmd_Type(Integer32):
    """Custom type nsModMonitorAupcResetAvgCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("execute", 1),
          ("none", 0),
          ("notApplicable", 255))
    )


_NsModMonitorAupcResetAvgCmd_Type.__name__ = "Integer32"
_NsModMonitorAupcResetAvgCmd_Object = MibScalar
nsModMonitorAupcResetAvgCmd = _NsModMonitorAupcResetAvgCmd_Object(
    (1, 3, 6, 1, 4, 1, 37576, 3, 2, 5, 7),
    _NsModMonitorAupcResetAvgCmd_Type()
)
nsModMonitorAupcResetAvgCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nsModMonitorAupcResetAvgCmd.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOVELSAT-MODULATOR-MIB",
    **{"nsModulator": nsModulator,
       "nsModConfig": nsModConfig,
       "nsModConfigLine": nsModConfigLine,
       "nsModConfigLineTXStatus": nsModConfigLineTXStatus,
       "nsModConfigLineMode": nsModConfigLineMode,
       "nsModConfigLineChPriority": nsModConfigLineChPriority,
       "nsModConfigLineRollOff": nsModConfigLineRollOff,
       "nsModConfigLineSineStatus": nsModConfigLineSineStatus,
       "nsModConfigLineRFFreq": nsModConfigLineRFFreq,
       "nsModConfigLineSymbolRate": nsModConfigLineSymbolRate,
       "nsModConfigLinePower": nsModConfigLinePower,
       "nsModConfigLineGoldSeq": nsModConfigLineGoldSeq,
       "nsModConfigLineDualChState": nsModConfigLineDualChState,
       "nsModConfigLineBitRate": nsModConfigLineBitRate,
       "nsModConfigLinePowerUpTXState": nsModConfigLinePowerUpTXState,
       "nsModConfigLineAcmMode": nsModConfigLineAcmMode,
       "nsModConfigLineOutputLevelMode": nsModConfigLineOutputLevelMode,
       "nsModConfigLineChannel1Bandwidth": nsModConfigLineChannel1Bandwidth,
       "nsModConfigLineChannel2Bandwidth": nsModConfigLineChannel2Bandwidth,
       "nsModConfigLineSpectrumInvert": nsModConfigLineSpectrumInvert,
       "nsModConfigLineRecommendedBitRate": nsModConfigLineRecommendedBitRate,
       "nsModConfigLineLOFreq": nsModConfigLineLOFreq,
       "nsModConfigLineAcmUseManagementIp": nsModConfigLineAcmUseManagementIp,
       "nsModConfigLineAcmIpAddress": nsModConfigLineAcmIpAddress,
       "nsModConfigLineAcmIpNetmask": nsModConfigLineAcmIpNetmask,
       "nsModConfigLineAupcMode": nsModConfigLineAupcMode,
       "nsModConfigLineAupcSatRxFreq": nsModConfigLineAupcSatRxFreq,
       "nsModConfigLineAupcSatRxPolarity": nsModConfigLineAupcSatRxPolarity,
       "nsModConfigLineAupcSatTxFreq": nsModConfigLineAupcSatTxFreq,
       "nsModConfigLineAupcSatTxPolarity": nsModConfigLineAupcSatTxPolarity,
       "nsModConfigLineAupcMaxGain": nsModConfigLineAupcMaxGain,
       "nsModConfigLineAupcMaxAttn": nsModConfigLineAupcMaxAttn,
       "nsModConfigChannel": nsModConfigChannel,
       "nsModConfigChannelTable": nsModConfigChannelTable,
       "nsModConfigChannelEntry": nsModConfigChannelEntry,
       "nsModConfigChStatus": nsModConfigChStatus,
       "nsModConfigChSource": nsModConfigChSource,
       "nsModConfigChNPD": nsModConfigChNPD,
       "nsModConfigChFrameSize": nsModConfigChFrameSize,
       "nsModConfigChModulation": nsModConfigChModulation,
       "nsModConfigChFECRate": nsModConfigChFECRate,
       "nsModConfigChPilot": nsModConfigChPilot,
       "nsModConfigChISSY": nsModConfigChISSY,
       "nsModConfigChStreamFormat": nsModConfigChStreamFormat,
       "nsModConfigChPacketSize": nsModConfigChPacketSize,
       "nsModConfigChSyncByte": nsModConfigChSyncByte,
       "nsModConfigChIsi": nsModConfigChIsi,
       "nsModConfigChPCRRestamping": nsModConfigChPCRRestamping,
       "nsModConfigChMpegProcessingMode": nsModConfigChMpegProcessingMode,
       "nsModConfigChBitRate": nsModConfigChBitRate,
       "nsModConfigChBitRatePercent": nsModConfigChBitRatePercent,
       "nsModConfigChTSProtect": nsModConfigChTSProtect,
       "nsModConfigInterface": nsModConfigInterface,
       "nsModConfigInterfaceTestTable": nsModConfigInterfaceTestTable,
       "nsModConfigInterfaceTestEntry": nsModConfigInterfaceTestEntry,
       "nsModConfigInterfaceTestPattern": nsModConfigInterfaceTestPattern,
       "nsModConfigInterfaceTestInvert": nsModConfigInterfaceTestInvert,
       "nsModConfigInterfaceASITable": nsModConfigInterfaceASITable,
       "nsModConfigInterfaceASIEntry": nsModConfigInterfaceASIEntry,
       "nsModConfigInterfaceASIDataOrder": nsModConfigInterfaceASIDataOrder,
       "nsModConfigInterfaceEthernetTable": nsModConfigInterfaceEthernetTable,
       "nsModConfigInterfaceEthernetEntry": nsModConfigInterfaceEthernetEntry,
       "nsModConfigInterfaceEthernetAutoNegotiation": nsModConfigInterfaceEthernetAutoNegotiation,
       "nsModConfigInterfaceEthernetSpeed": nsModConfigInterfaceEthernetSpeed,
       "nsModConfigInterfaceEthernetDuplex": nsModConfigInterfaceEthernetDuplex,
       "nsModConfigInterfaceEthernetEncapsulation": nsModConfigInterfaceEthernetEncapsulation,
       "nsModConfigInterfaceEthernetPid": nsModConfigInterfaceEthernetPid,
       "nsModConfigInterfaceGigETable": nsModConfigInterfaceGigETable,
       "nsModConfigInterfaceGigEEntry": nsModConfigInterfaceGigEEntry,
       "nsModConfigInterfaceGigEAutoNegotiation": nsModConfigInterfaceGigEAutoNegotiation,
       "nsModConfigInterfaceGigESpeed": nsModConfigInterfaceGigESpeed,
       "nsModConfigInterfaceGigEDuplex": nsModConfigInterfaceGigEDuplex,
       "nsModConfigInterfaceGigEPortType": nsModConfigInterfaceGigEPortType,
       "nsModConfigCid": nsModConfigCid,
       "nsModConfigCidState": nsModConfigCidState,
       "nsModConfigCidLatitude": nsModConfigCidLatitude,
       "nsModConfigCidLongitude": nsModConfigCidLongitude,
       "nsModConfigCidPhone": nsModConfigCidPhone,
       "nsModConfigCidExtension": nsModConfigCidExtension,
       "nsModConfigCidUsertext": nsModConfigCidUsertext,
       "nsModMonitor": nsModMonitor,
       "nsModMonitorInterface": nsModMonitorInterface,
       "nsModMonitorInterfaceTable": nsModMonitorInterfaceTable,
       "nsModMonitorInterfaceEntry": nsModMonitorInterfaceEntry,
       "nsModMonitorInterfaceDataRate": nsModMonitorInterfaceDataRate,
       "nsModMonitorInterfaceStatus": nsModMonitorInterfaceStatus,
       "nsModMonitorInterfaceChannel": nsModMonitorInterfaceChannel,
       "nsModMonitorInterfaceName": nsModMonitorInterfaceName,
       "nsModMonitorSystem": nsModMonitorSystem,
       "nsModMonitorSystemBoardTmp": nsModMonitorSystemBoardTmp,
       "nsModMonitorSystem10MHrzClkSource": nsModMonitorSystem10MHrzClkSource,
       "nsModMonitorSystemRefClkOut": nsModMonitorSystemRefClkOut,
       "nsModMonitorSystemTxPortClk": nsModMonitorSystemTxPortClk,
       "nsModMonitorEthernet": nsModMonitorEthernet,
       "nsModMonitorEthernetTable": nsModMonitorEthernetTable,
       "nsModMonitorEthernetEntry": nsModMonitorEthernetEntry,
       "nsModMonitorEthernetStatisticsNumber": nsModMonitorEthernetStatisticsNumber,
       "nsModMonitorEthernetStatisticsName": nsModMonitorEthernetStatisticsName,
       "nsModMonitorEthernetStatisticsValueA": nsModMonitorEthernetStatisticsValueA,
       "nsModMonitorEthernetStatisticsValueB": nsModMonitorEthernetStatisticsValueB,
       "nsModMonitorAcm": nsModMonitorAcm,
       "nsModMonitorAcmTable": nsModMonitorAcmTable,
       "nsModMonitorAcmEntry": nsModMonitorAcmEntry,
       "nsModMonitorAcmStatisticsNumber": nsModMonitorAcmStatisticsNumber,
       "nsModMonitorAcmStatisticsClientIp": nsModMonitorAcmStatisticsClientIp,
       "nsModMonitorAcmStatisticsClientName": nsModMonitorAcmStatisticsClientName,
       "nsModMonitorAcmStatisticsClientSnr": nsModMonitorAcmStatisticsClientSnr,
       "nsModMonitorAcmStatisticsClientMargin": nsModMonitorAcmStatisticsClientMargin,
       "nsModMonitorAcmStatisticsChannelNum": nsModMonitorAcmStatisticsChannelNum,
       "nsModMonitorAcmStatisticsLineMode": nsModMonitorAcmStatisticsLineMode,
       "nsModMonitorAcmStatisticsModulation": nsModMonitorAcmStatisticsModulation,
       "nsModMonitorAcmStatisticsFecRate": nsModMonitorAcmStatisticsFecRate,
       "nsModMonitorAcmStatisticsFrameSize": nsModMonitorAcmStatisticsFrameSize,
       "nsModMonitorAcmStatisticsPilot": nsModMonitorAcmStatisticsPilot,
       "nsModMonitorAcmStatisticsIsLocked": nsModMonitorAcmStatisticsIsLocked,
       "nsModMonitorAcmStatisticsIsWorstCase": nsModMonitorAcmStatisticsIsWorstCase,
       "nsModMonitorAcmStatisticsState": nsModMonitorAcmStatisticsState,
       "nsModMonitorAcmStatisticsGroup": nsModMonitorAcmStatisticsGroup,
       "nsModMonitorAcmStatisticsClrCmd": nsModMonitorAcmStatisticsClrCmd,
       "nsModMonitorAupc": nsModMonitorAupc,
       "nsModMonitorAupcCurrentPower": nsModMonitorAupcCurrentPower,
       "nsModMonitorAupcMinimalPower": nsModMonitorAupcMinimalPower,
       "nsModMonitorAupcMaximalPower": nsModMonitorAupcMaximalPower,
       "nsModMonitorAupcAveragePower": nsModMonitorAupcAveragePower,
       "nsModMonitorAupcEstimatedUplinkAttn": nsModMonitorAupcEstimatedUplinkAttn,
       "nsModMonitorAupcEstimatedDownlinkAttn": nsModMonitorAupcEstimatedDownlinkAttn,
       "nsModMonitorAupcResetAvgCmd": nsModMonitorAupcResetAvgCmd}
)
