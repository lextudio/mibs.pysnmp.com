# SNMP MIB module (SDLC-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SDLC-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:12 2024
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
 enterprises,
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "mgmt")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class Counter16(Integer32):
    """Custom type Counter16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Codex_ObjectIdentity = ObjectIdentity
codex = _Codex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449)
)
_CdxProductSpecific_ObjectIdentity = ObjectIdentity
cdxProductSpecific = _CdxProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2)
)
_Cdx6500_ObjectIdentity = ObjectIdentity
cdx6500 = _Cdx6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1)
)
_Cdx6500Configuration_ObjectIdentity = ObjectIdentity
cdx6500Configuration = _Cdx6500Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2)
)
_Cdx6500CfgProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgProtocolGroup = _Cdx6500CfgProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1)
)
_Cdx6500PCTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTPortProtocolGroup = _Cdx6500PCTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1)
)
_Cdx6500PCTSDLCPortTable_Object = MibTable
cdx6500PCTSDLCPortTable = _Cdx6500PCTSDLCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 12)
)
if mibBuilder.loadTexts:
    cdx6500PCTSDLCPortTable.setStatus("mandatory")
_Cdx6500PCTSDLCPortEntry_Object = MibTableRow
cdx6500PCTSDLCPortEntry = _Cdx6500PCTSDLCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 12, 1)
)
cdx6500PCTSDLCPortEntry.setIndexNames(
    (0, "SDLC-OPT-MIB", "cdx6500sdlcpCfgPortNum"),
)
if mibBuilder.loadTexts:
    cdx6500PCTSDLCPortEntry.setStatus("mandatory")


class _Cdx6500sdlcpCfgPortNum_Type(Integer32):
    """Custom type cdx6500sdlcpCfgPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500sdlcpCfgPortNum_Type.__name__ = "Integer32"
_Cdx6500sdlcpCfgPortNum_Object = MibTableColumn
cdx6500sdlcpCfgPortNum = _Cdx6500sdlcpCfgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 12, 1, 1),
    _Cdx6500sdlcpCfgPortNum_Type()
)
cdx6500sdlcpCfgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpCfgPortNum.setStatus("mandatory")


class _Cdx6500sdlcpSubType_Type(Integer32):
    """Custom type cdx6500sdlcpSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("hpad", 0),
          ("newvalHpad", 50),
          ("tpad", 1))
    )


_Cdx6500sdlcpSubType_Type.__name__ = "Integer32"
_Cdx6500sdlcpSubType_Object = MibTableColumn
cdx6500sdlcpSubType = _Cdx6500sdlcpSubType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 12, 1, 2),
    _Cdx6500sdlcpSubType_Type()
)
cdx6500sdlcpSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpSubType.setStatus("mandatory")


class _Cdx6500sdlcpTxCoding_Type(Integer32):
    """Custom type cdx6500sdlcpTxCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvalNrz", 50),
          ("nrz", 0),
          ("nrzi", 1))
    )


_Cdx6500sdlcpTxCoding_Type.__name__ = "Integer32"
_Cdx6500sdlcpTxCoding_Object = MibTableColumn
cdx6500sdlcpTxCoding = _Cdx6500sdlcpTxCoding_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 12, 1, 3),
    _Cdx6500sdlcpTxCoding_Type()
)
cdx6500sdlcpTxCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpTxCoding.setStatus("mandatory")


class _Cdx6500sdlcpLineType_Type(Integer32):
    """Custom type cdx6500sdlcpLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("fdx", 1),
          ("hdx", 0),
          ("hdxdce", 2),
          ("newvalHdx", 50))
    )


_Cdx6500sdlcpLineType_Type.__name__ = "Integer32"
_Cdx6500sdlcpLineType_Object = MibTableColumn
cdx6500sdlcpLineType = _Cdx6500sdlcpLineType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 12, 1, 4),
    _Cdx6500sdlcpLineType_Type()
)
cdx6500sdlcpLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpLineType.setStatus("mandatory")


class _Cdx6500sdlcpTxType_Type(Integer32):
    """Custom type cdx6500sdlcpTxType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvalTws", 50),
          ("twa", 1),
          ("tws", 0))
    )


_Cdx6500sdlcpTxType_Type.__name__ = "Integer32"
_Cdx6500sdlcpTxType_Object = MibTableColumn
cdx6500sdlcpTxType = _Cdx6500sdlcpTxType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 12, 1, 5),
    _Cdx6500sdlcpTxType_Type()
)
cdx6500sdlcpTxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpTxType.setStatus("mandatory")


class _Cdx6500sdlcpSendSigDelay_Type(Integer32):
    """Custom type cdx6500sdlcpSendSigDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("deprecatedObj", 1)
    )


_Cdx6500sdlcpSendSigDelay_Type.__name__ = "Integer32"
_Cdx6500sdlcpSendSigDelay_Object = MibTableColumn
cdx6500sdlcpSendSigDelay = _Cdx6500sdlcpSendSigDelay_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 12, 1, 6),
    _Cdx6500sdlcpSendSigDelay_Type()
)
cdx6500sdlcpSendSigDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpSendSigDelay.setStatus("deprecated")


class _Cdx6500sdlcpClock_Type(Integer32):
    """Custom type cdx6500sdlcpClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("ext", 1),
          ("int", 0),
          ("newvalInt", 50))
    )


_Cdx6500sdlcpClock_Type.__name__ = "Integer32"
_Cdx6500sdlcpClock_Object = MibTableColumn
cdx6500sdlcpClock = _Cdx6500sdlcpClock_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 12, 1, 7),
    _Cdx6500sdlcpClock_Type()
)
cdx6500sdlcpClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpClock.setStatus("mandatory")


class _Cdx6500sdlcpClockSpeed_Type(Integer32):
    """Custom type cdx6500sdlcpClockSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 80000),
    )


_Cdx6500sdlcpClockSpeed_Type.__name__ = "Integer32"
_Cdx6500sdlcpClockSpeed_Object = MibTableColumn
cdx6500sdlcpClockSpeed = _Cdx6500sdlcpClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 12, 1, 8),
    _Cdx6500sdlcpClockSpeed_Type()
)
cdx6500sdlcpClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpClockSpeed.setStatus("mandatory")


class _Cdx6500sdlcpNumControllers_Type(Integer32):
    """Custom type cdx6500sdlcpNumControllers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Cdx6500sdlcpNumControllers_Type.__name__ = "Integer32"
_Cdx6500sdlcpNumControllers_Object = MibTableColumn
cdx6500sdlcpNumControllers = _Cdx6500sdlcpNumControllers_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 12, 1, 9),
    _Cdx6500sdlcpNumControllers_Type()
)
cdx6500sdlcpNumControllers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpNumControllers.setStatus("mandatory")


class _Cdx6500sdlcpPollTimer_Type(Integer32):
    """Custom type cdx6500sdlcpPollTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500sdlcpPollTimer_Type.__name__ = "Integer32"
_Cdx6500sdlcpPollTimer_Object = MibTableColumn
cdx6500sdlcpPollTimer = _Cdx6500sdlcpPollTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 12, 1, 10),
    _Cdx6500sdlcpPollTimer_Type()
)
cdx6500sdlcpPollTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpPollTimer.setStatus("mandatory")


class _Cdx6500sdlcpPollFrequency_Type(Integer32):
    """Custom type cdx6500sdlcpPollFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 250),
    )


_Cdx6500sdlcpPollFrequency_Type.__name__ = "Integer32"
_Cdx6500sdlcpPollFrequency_Object = MibTableColumn
cdx6500sdlcpPollFrequency = _Cdx6500sdlcpPollFrequency_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 12, 1, 11),
    _Cdx6500sdlcpPollFrequency_Type()
)
cdx6500sdlcpPollFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpPollFrequency.setStatus("mandatory")


class _Cdx6500sdlcpTries_Type(Integer32):
    """Custom type cdx6500sdlcpTries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Cdx6500sdlcpTries_Type.__name__ = "Integer32"
_Cdx6500sdlcpTries_Object = MibTableColumn
cdx6500sdlcpTries = _Cdx6500sdlcpTries_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 12, 1, 12),
    _Cdx6500sdlcpTries_Type()
)
cdx6500sdlcpTries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpTries.setStatus("mandatory")


class _Cdx6500sdlcpOptions_Type(DisplayString):
    """Custom type cdx6500sdlcpOptions based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 5),
    )


_Cdx6500sdlcpOptions_Type.__name__ = "DisplayString"
_Cdx6500sdlcpOptions_Object = MibTableColumn
cdx6500sdlcpOptions = _Cdx6500sdlcpOptions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 12, 1, 13),
    _Cdx6500sdlcpOptions_Type()
)
cdx6500sdlcpOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpOptions.setStatus("mandatory")


class _Cdx6500sdlcpPortAddress_Type(DisplayString):
    """Custom type cdx6500sdlcpPortAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500sdlcpPortAddress_Type.__name__ = "DisplayString"
_Cdx6500sdlcpPortAddress_Object = MibTableColumn
cdx6500sdlcpPortAddress = _Cdx6500sdlcpPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 12, 1, 14),
    _Cdx6500sdlcpPortAddress_Type()
)
cdx6500sdlcpPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpPortAddress.setStatus("mandatory")


class _Cdx6500sdlcpPortOptions_Type(DisplayString):
    """Custom type cdx6500sdlcpPortOptions based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 4),
    )


_Cdx6500sdlcpPortOptions_Type.__name__ = "DisplayString"
_Cdx6500sdlcpPortOptions_Object = MibTableColumn
cdx6500sdlcpPortOptions = _Cdx6500sdlcpPortOptions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 12, 1, 15),
    _Cdx6500sdlcpPortOptions_Type()
)
cdx6500sdlcpPortOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpPortOptions.setStatus("mandatory")


class _Cdx6500sdlcpHPADResponseDelay_Type(Integer32):
    """Custom type cdx6500sdlcpHPADResponseDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              50,
              51,
              100,
              150,
              200)
        )
    )
    namedValues = NamedValues(
        *(("msec0", 0),
          ("msec100", 100),
          ("msec150", 150),
          ("msec200", 200),
          ("msec50", 51),
          ("newvalMsec0", 50))
    )


_Cdx6500sdlcpHPADResponseDelay_Type.__name__ = "Integer32"
_Cdx6500sdlcpHPADResponseDelay_Object = MibTableColumn
cdx6500sdlcpHPADResponseDelay = _Cdx6500sdlcpHPADResponseDelay_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 12, 1, 16),
    _Cdx6500sdlcpHPADResponseDelay_Type()
)
cdx6500sdlcpHPADResponseDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpHPADResponseDelay.setStatus("mandatory")


class _Cdx6500sdlcpMaxFrameSize_Type(Integer32):
    """Custom type cdx6500sdlcpMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Cdx6500sdlcpMaxFrameSize_Type.__name__ = "Integer32"
_Cdx6500sdlcpMaxFrameSize_Object = MibTableColumn
cdx6500sdlcpMaxFrameSize = _Cdx6500sdlcpMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 12, 1, 17),
    _Cdx6500sdlcpMaxFrameSize_Type()
)
cdx6500sdlcpMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpMaxFrameSize.setStatus("mandatory")


class _Cdx6500sdlcpRtsCtsDelay_Type(Integer32):
    """Custom type cdx6500sdlcpRtsCtsDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_Cdx6500sdlcpRtsCtsDelay_Type.__name__ = "Integer32"
_Cdx6500sdlcpRtsCtsDelay_Object = MibTableColumn
cdx6500sdlcpRtsCtsDelay = _Cdx6500sdlcpRtsCtsDelay_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 12, 1, 18),
    _Cdx6500sdlcpRtsCtsDelay_Type()
)
cdx6500sdlcpRtsCtsDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpRtsCtsDelay.setStatus("mandatory")


class _Cdx6500sdlcpElectricalInterfaceType_Type(Integer32):
    """Custom type cdx6500sdlcpElectricalInterfaceType based on Integer32"""
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
        *(("none", 5),
          ("v24", 1),
          ("v35", 2),
          ("v36", 3),
          ("x21", 4))
    )


_Cdx6500sdlcpElectricalInterfaceType_Type.__name__ = "Integer32"
_Cdx6500sdlcpElectricalInterfaceType_Object = MibTableColumn
cdx6500sdlcpElectricalInterfaceType = _Cdx6500sdlcpElectricalInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 12, 1, 19),
    _Cdx6500sdlcpElectricalInterfaceType_Type()
)
cdx6500sdlcpElectricalInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpElectricalInterfaceType.setStatus("mandatory")


class _Cdx6500sdlcpV24ElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500sdlcpV24ElectricalInterfaceOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ri", 1),
          ("tm", 2))
    )


_Cdx6500sdlcpV24ElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500sdlcpV24ElectricalInterfaceOption_Object = MibTableColumn
cdx6500sdlcpV24ElectricalInterfaceOption = _Cdx6500sdlcpV24ElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 12, 1, 20),
    _Cdx6500sdlcpV24ElectricalInterfaceOption_Type()
)
cdx6500sdlcpV24ElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpV24ElectricalInterfaceOption.setStatus("mandatory")


class _Cdx6500sdlcpHighSpeedElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500sdlcpHighSpeedElectricalInterfaceOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("xover", 2))
    )


_Cdx6500sdlcpHighSpeedElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500sdlcpHighSpeedElectricalInterfaceOption_Object = MibTableColumn
cdx6500sdlcpHighSpeedElectricalInterfaceOption = _Cdx6500sdlcpHighSpeedElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 12, 1, 21),
    _Cdx6500sdlcpHighSpeedElectricalInterfaceOption_Type()
)
cdx6500sdlcpHighSpeedElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpHighSpeedElectricalInterfaceOption.setStatus("mandatory")
_Cdx6500PCTStationProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTStationProtocolGroup = _Cdx6500PCTStationProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3)
)
_Cdx6500SPCTSDLCStationTable_Object = MibTable
cdx6500SPCTSDLCStationTable = _Cdx6500SPCTSDLCStationTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cdx6500SPCTSDLCStationTable.setStatus("mandatory")
_Cdx6500SPCTSDLCStationEntry_Object = MibTableRow
cdx6500SPCTSDLCStationEntry = _Cdx6500SPCTSDLCStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 4, 1)
)
cdx6500SPCTSDLCStationEntry.setIndexNames(
    (0, "SDLC-OPT-MIB", "cdx6500sdlcsCfgPortNum"),
    (0, "SDLC-OPT-MIB", "cdx6500sdlcsCfgStationNum"),
)
if mibBuilder.loadTexts:
    cdx6500SPCTSDLCStationEntry.setStatus("mandatory")


class _Cdx6500sdlcsCfgPortNum_Type(Integer32):
    """Custom type cdx6500sdlcsCfgPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500sdlcsCfgPortNum_Type.__name__ = "Integer32"
_Cdx6500sdlcsCfgPortNum_Object = MibTableColumn
cdx6500sdlcsCfgPortNum = _Cdx6500sdlcsCfgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 4, 1, 1),
    _Cdx6500sdlcsCfgPortNum_Type()
)
cdx6500sdlcsCfgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsCfgPortNum.setStatus("mandatory")


class _Cdx6500sdlcsCfgStationNum_Type(Integer32):
    """Custom type cdx6500sdlcsCfgStationNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Cdx6500sdlcsCfgStationNum_Type.__name__ = "Integer32"
_Cdx6500sdlcsCfgStationNum_Object = MibTableColumn
cdx6500sdlcsCfgStationNum = _Cdx6500sdlcsCfgStationNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 4, 1, 2),
    _Cdx6500sdlcsCfgStationNum_Type()
)
cdx6500sdlcsCfgStationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsCfgStationNum.setStatus("mandatory")


class _Cdx6500sdlcsStationAddr_Type(DisplayString):
    """Custom type cdx6500sdlcsStationAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_Cdx6500sdlcsStationAddr_Type.__name__ = "DisplayString"
_Cdx6500sdlcsStationAddr_Object = MibTableColumn
cdx6500sdlcsStationAddr = _Cdx6500sdlcsStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 4, 1, 3),
    _Cdx6500sdlcsStationAddr_Type()
)
cdx6500sdlcsStationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsStationAddr.setStatus("mandatory")


class _Cdx6500sdlcsFrameWinSize_Type(Integer32):
    """Custom type cdx6500sdlcsFrameWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Cdx6500sdlcsFrameWinSize_Type.__name__ = "Integer32"
_Cdx6500sdlcsFrameWinSize_Object = MibTableColumn
cdx6500sdlcsFrameWinSize = _Cdx6500sdlcsFrameWinSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 4, 1, 4),
    _Cdx6500sdlcsFrameWinSize_Type()
)
cdx6500sdlcsFrameWinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsFrameWinSize.setStatus("mandatory")


class _Cdx6500sdlcsAutocallMnem_Type(DisplayString):
    """Custom type cdx6500sdlcsAutocallMnem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cdx6500sdlcsAutocallMnem_Type.__name__ = "DisplayString"
_Cdx6500sdlcsAutocallMnem_Object = MibTableColumn
cdx6500sdlcsAutocallMnem = _Cdx6500sdlcsAutocallMnem_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 4, 1, 5),
    _Cdx6500sdlcsAutocallMnem_Type()
)
cdx6500sdlcsAutocallMnem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsAutocallMnem.setStatus("mandatory")


class _Cdx6500sdlcsProtocolID_Type(DisplayString):
    """Custom type cdx6500sdlcsProtocolID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Cdx6500sdlcsProtocolID_Type.__name__ = "DisplayString"
_Cdx6500sdlcsProtocolID_Object = MibTableColumn
cdx6500sdlcsProtocolID = _Cdx6500sdlcsProtocolID_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 4, 1, 6),
    _Cdx6500sdlcsProtocolID_Type()
)
cdx6500sdlcsProtocolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsProtocolID.setStatus("mandatory")


class _Cdx6500sdlcsCUG_Type(DisplayString):
    """Custom type cdx6500sdlcsCUG based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(23, 23),
    )


_Cdx6500sdlcsCUG_Type.__name__ = "DisplayString"
_Cdx6500sdlcsCUG_Object = MibTableColumn
cdx6500sdlcsCUG = _Cdx6500sdlcsCUG_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 4, 1, 7),
    _Cdx6500sdlcsCUG_Type()
)
cdx6500sdlcsCUG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsCUG.setStatus("mandatory")


class _Cdx6500sdlcsOptions_Type(DisplayString):
    """Custom type cdx6500sdlcsOptions based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 4),
    )


_Cdx6500sdlcsOptions_Type.__name__ = "DisplayString"
_Cdx6500sdlcsOptions_Object = MibTableColumn
cdx6500sdlcsOptions = _Cdx6500sdlcsOptions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 4, 1, 8),
    _Cdx6500sdlcsOptions_Type()
)
cdx6500sdlcsOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsOptions.setStatus("mandatory")


class _Cdx6500sdlcsStationID_Type(DisplayString):
    """Custom type cdx6500sdlcsStationID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Cdx6500sdlcsStationID_Type.__name__ = "DisplayString"
_Cdx6500sdlcsStationID_Object = MibTableColumn
cdx6500sdlcsStationID = _Cdx6500sdlcsStationID_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 4, 1, 9),
    _Cdx6500sdlcsStationID_Type()
)
cdx6500sdlcsStationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsStationID.setStatus("mandatory")


class _Cdx6500sdlcsBillingFlag_Type(Integer32):
    """Custom type cdx6500sdlcsBillingFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvaloff", 50),
          ("off", 0),
          ("on", 1))
    )


_Cdx6500sdlcsBillingFlag_Type.__name__ = "Integer32"
_Cdx6500sdlcsBillingFlag_Object = MibTableColumn
cdx6500sdlcsBillingFlag = _Cdx6500sdlcsBillingFlag_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 4, 1, 10),
    _Cdx6500sdlcsBillingFlag_Type()
)
cdx6500sdlcsBillingFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsBillingFlag.setStatus("mandatory")


class _Cdx6500sdlcsStnSubaddress_Type(DisplayString):
    """Custom type cdx6500sdlcsStnSubaddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_Cdx6500sdlcsStnSubaddress_Type.__name__ = "DisplayString"
_Cdx6500sdlcsStnSubaddress_Object = MibTableColumn
cdx6500sdlcsStnSubaddress = _Cdx6500sdlcsStnSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 4, 1, 11),
    _Cdx6500sdlcsStnSubaddress_Type()
)
cdx6500sdlcsStnSubaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsStnSubaddress.setStatus("mandatory")


class _Cdx6500sdlcsGroupAddress_Type(DisplayString):
    """Custom type cdx6500sdlcsGroupAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_Cdx6500sdlcsGroupAddress_Type.__name__ = "DisplayString"
_Cdx6500sdlcsGroupAddress_Object = MibTableColumn
cdx6500sdlcsGroupAddress = _Cdx6500sdlcsGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 4, 1, 12),
    _Cdx6500sdlcsGroupAddress_Type()
)
cdx6500sdlcsGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsGroupAddress.setStatus("mandatory")


class _Cdx6500sdlcsX25Password_Type(DisplayString):
    """Custom type cdx6500sdlcsX25Password based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Cdx6500sdlcsX25Password_Type.__name__ = "DisplayString"
_Cdx6500sdlcsX25Password_Object = MibTableColumn
cdx6500sdlcsX25Password = _Cdx6500sdlcsX25Password_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 4, 1, 13),
    _Cdx6500sdlcsX25Password_Type()
)
cdx6500sdlcsX25Password.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsX25Password.setStatus("mandatory")


class _Cdx6500sdlcsProtectionLevel_Type(Integer32):
    """Custom type cdx6500sdlcsProtectionLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("cponly", 1),
          ("fulldcp", 2),
          ("newvalnone", 50),
          ("none", 0))
    )


_Cdx6500sdlcsProtectionLevel_Type.__name__ = "Integer32"
_Cdx6500sdlcsProtectionLevel_Object = MibTableColumn
cdx6500sdlcsProtectionLevel = _Cdx6500sdlcsProtectionLevel_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 4, 1, 14),
    _Cdx6500sdlcsProtectionLevel_Type()
)
cdx6500sdlcsProtectionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsProtectionLevel.setStatus("mandatory")


class _Cdx6500sdlcsReconnectTimeout_Type(Integer32):
    """Custom type cdx6500sdlcsReconnectTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Cdx6500sdlcsReconnectTimeout_Type.__name__ = "Integer32"
_Cdx6500sdlcsReconnectTimeout_Object = MibTableColumn
cdx6500sdlcsReconnectTimeout = _Cdx6500sdlcsReconnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 4, 1, 15),
    _Cdx6500sdlcsReconnectTimeout_Type()
)
cdx6500sdlcsReconnectTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsReconnectTimeout.setStatus("mandatory")


class _Cdx6500sdlcsReconnectLimit_Type(Integer32):
    """Custom type cdx6500sdlcsReconnectLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500sdlcsReconnectLimit_Type.__name__ = "Integer32"
_Cdx6500sdlcsReconnectLimit_Object = MibTableColumn
cdx6500sdlcsReconnectLimit = _Cdx6500sdlcsReconnectLimit_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 4, 1, 16),
    _Cdx6500sdlcsReconnectLimit_Type()
)
cdx6500sdlcsReconnectLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsReconnectLimit.setStatus("mandatory")


class _Cdx6500sdlcsTrafficPriority_Type(Integer32):
    """Custom type cdx6500sdlcsTrafficPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              50)
        )
    )
    namedValues = NamedValues(
        *(("hipriority", 2),
          ("lowpriority", 0),
          ("medpriority", 1),
          ("newvallowpriority", 50),
          ("xppriority", 3))
    )


_Cdx6500sdlcsTrafficPriority_Type.__name__ = "Integer32"
_Cdx6500sdlcsTrafficPriority_Object = MibTableColumn
cdx6500sdlcsTrafficPriority = _Cdx6500sdlcsTrafficPriority_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 4, 1, 17),
    _Cdx6500sdlcsTrafficPriority_Type()
)
cdx6500sdlcsTrafficPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsTrafficPriority.setStatus("optional")


class _Cdx6500sdlcsCallTimer_Type(Integer32):
    """Custom type cdx6500sdlcsCallTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_Cdx6500sdlcsCallTimer_Type.__name__ = "Integer32"
_Cdx6500sdlcsCallTimer_Object = MibTableColumn
cdx6500sdlcsCallTimer = _Cdx6500sdlcsCallTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 4, 1, 18),
    _Cdx6500sdlcsCallTimer_Type()
)
cdx6500sdlcsCallTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsCallTimer.setStatus("mandatory")


class _Cdx6500sdlcsIdleTimer_Type(Integer32):
    """Custom type cdx6500sdlcsIdleTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Cdx6500sdlcsIdleTimer_Type.__name__ = "Integer32"
_Cdx6500sdlcsIdleTimer_Object = MibTableColumn
cdx6500sdlcsIdleTimer = _Cdx6500sdlcsIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 4, 1, 19),
    _Cdx6500sdlcsIdleTimer_Type()
)
cdx6500sdlcsIdleTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsIdleTimer.setStatus("mandatory")


class _Cdx6500sdlcsVerConnTimer_Type(Integer32):
    """Custom type cdx6500sdlcsVerConnTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Cdx6500sdlcsVerConnTimer_Type.__name__ = "Integer32"
_Cdx6500sdlcsVerConnTimer_Object = MibTableColumn
cdx6500sdlcsVerConnTimer = _Cdx6500sdlcsVerConnTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 4, 1, 20),
    _Cdx6500sdlcsVerConnTimer_Type()
)
cdx6500sdlcsVerConnTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsVerConnTimer.setStatus("mandatory")


class _Cdx6500sdlcsUnsusWaitTimer_Type(Integer32):
    """Custom type cdx6500sdlcsUnsusWaitTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Cdx6500sdlcsUnsusWaitTimer_Type.__name__ = "Integer32"
_Cdx6500sdlcsUnsusWaitTimer_Object = MibTableColumn
cdx6500sdlcsUnsusWaitTimer = _Cdx6500sdlcsUnsusWaitTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 4, 1, 21),
    _Cdx6500sdlcsUnsusWaitTimer_Type()
)
cdx6500sdlcsUnsusWaitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsUnsusWaitTimer.setStatus("mandatory")


class _Cdx6500sdlcsMaxCallAttempts_Type(Integer32):
    """Custom type cdx6500sdlcsMaxCallAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500sdlcsMaxCallAttempts_Type.__name__ = "Integer32"
_Cdx6500sdlcsMaxCallAttempts_Object = MibTableColumn
cdx6500sdlcsMaxCallAttempts = _Cdx6500sdlcsMaxCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 4, 1, 22),
    _Cdx6500sdlcsMaxCallAttempts_Type()
)
cdx6500sdlcsMaxCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsMaxCallAttempts.setStatus("mandatory")
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500StatProtocolGroup = _Cdx6500StatProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1)
)
_Cdx6500PSTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTPortProtocolGroup = _Cdx6500PSTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1)
)
_Cdx6500PPSTSDLCPortTable_Object = MibTable
cdx6500PPSTSDLCPortTable = _Cdx6500PPSTSDLCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12)
)
if mibBuilder.loadTexts:
    cdx6500PPSTSDLCPortTable.setStatus("mandatory")
_Cdx6500PPSTSDLCPortEntry_Object = MibTableRow
cdx6500PPSTSDLCPortEntry = _Cdx6500PPSTSDLCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1)
)
cdx6500PPSTSDLCPortEntry.setIndexNames(
    (0, "SDLC-OPT-MIB", "cdx6500sdlcpStatsPortNum"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTSDLCPortEntry.setStatus("mandatory")


class _Cdx6500sdlcpStatsPortNum_Type(Integer32):
    """Custom type cdx6500sdlcpStatsPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500sdlcpStatsPortNum_Type.__name__ = "Integer32"
_Cdx6500sdlcpStatsPortNum_Object = MibTableColumn
cdx6500sdlcpStatsPortNum = _Cdx6500sdlcpStatsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 1),
    _Cdx6500sdlcpStatsPortNum_Type()
)
cdx6500sdlcpStatsPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpStatsPortNum.setStatus("mandatory")


class _Cdx6500sdlcpPortStatus_Type(Integer32):
    """Custom type cdx6500sdlcpPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              50)
        )
    )
    namedValues = NamedValues(
        *(("busyout", 2),
          ("disabled", 0),
          ("down", 4),
          ("enabled", 1),
          ("newvaldisabled", 50),
          ("up", 3))
    )


_Cdx6500sdlcpPortStatus_Type.__name__ = "Integer32"
_Cdx6500sdlcpPortStatus_Object = MibTableColumn
cdx6500sdlcpPortStatus = _Cdx6500sdlcpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 2),
    _Cdx6500sdlcpPortStatus_Type()
)
cdx6500sdlcpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpPortStatus.setStatus("mandatory")
_Cdx6500sdlcpPortSpeed_Type = Integer32
_Cdx6500sdlcpPortSpeed_Object = MibTableColumn
cdx6500sdlcpPortSpeed = _Cdx6500sdlcpPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 3),
    _Cdx6500sdlcpPortSpeed_Type()
)
cdx6500sdlcpPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpPortSpeed.setStatus("mandatory")
_Cdx6500sdlcpCharInTotal_Type = Counter32
_Cdx6500sdlcpCharInTotal_Object = MibTableColumn
cdx6500sdlcpCharInTotal = _Cdx6500sdlcpCharInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 4),
    _Cdx6500sdlcpCharInTotal_Type()
)
cdx6500sdlcpCharInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpCharInTotal.setStatus("mandatory")
_Cdx6500sdlcpCharOutTotal_Type = Counter32
_Cdx6500sdlcpCharOutTotal_Object = MibTableColumn
cdx6500sdlcpCharOutTotal = _Cdx6500sdlcpCharOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 5),
    _Cdx6500sdlcpCharOutTotal_Type()
)
cdx6500sdlcpCharOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpCharOutTotal.setStatus("mandatory")
_Cdx6500sdlcpCharsInPerSec_Type = Integer32
_Cdx6500sdlcpCharsInPerSec_Object = MibTableColumn
cdx6500sdlcpCharsInPerSec = _Cdx6500sdlcpCharsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 6),
    _Cdx6500sdlcpCharsInPerSec_Type()
)
cdx6500sdlcpCharsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpCharsInPerSec.setStatus("mandatory")
_Cdx6500sdlcpCharsOutPerSec_Type = Integer32
_Cdx6500sdlcpCharsOutPerSec_Object = MibTableColumn
cdx6500sdlcpCharsOutPerSec = _Cdx6500sdlcpCharsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 7),
    _Cdx6500sdlcpCharsOutPerSec_Type()
)
cdx6500sdlcpCharsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpCharsOutPerSec.setStatus("mandatory")
_Cdx6500sdlcpFrameInTotal_Type = Counter32
_Cdx6500sdlcpFrameInTotal_Object = MibTableColumn
cdx6500sdlcpFrameInTotal = _Cdx6500sdlcpFrameInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 8),
    _Cdx6500sdlcpFrameInTotal_Type()
)
cdx6500sdlcpFrameInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpFrameInTotal.setStatus("mandatory")
_Cdx6500sdlcpFrameOutTotal_Type = Counter32
_Cdx6500sdlcpFrameOutTotal_Object = MibTableColumn
cdx6500sdlcpFrameOutTotal = _Cdx6500sdlcpFrameOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 9),
    _Cdx6500sdlcpFrameOutTotal_Type()
)
cdx6500sdlcpFrameOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpFrameOutTotal.setStatus("mandatory")
_Cdx6500sdlcpFramesInPerSec_Type = Integer32
_Cdx6500sdlcpFramesInPerSec_Object = MibTableColumn
cdx6500sdlcpFramesInPerSec = _Cdx6500sdlcpFramesInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 10),
    _Cdx6500sdlcpFramesInPerSec_Type()
)
cdx6500sdlcpFramesInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpFramesInPerSec.setStatus("mandatory")
_Cdx6500sdlcpFramesOutPerSec_Type = Integer32
_Cdx6500sdlcpFramesOutPerSec_Object = MibTableColumn
cdx6500sdlcpFramesOutPerSec = _Cdx6500sdlcpFramesOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 11),
    _Cdx6500sdlcpFramesOutPerSec_Type()
)
cdx6500sdlcpFramesOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpFramesOutPerSec.setStatus("mandatory")


class _Cdx6500sdlcpStateChange_Type(DisplayString):
    """Custom type cdx6500sdlcpStateChange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Cdx6500sdlcpStateChange_Type.__name__ = "DisplayString"
_Cdx6500sdlcpStateChange_Object = MibTableColumn
cdx6500sdlcpStateChange = _Cdx6500sdlcpStateChange_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 12),
    _Cdx6500sdlcpStateChange_Type()
)
cdx6500sdlcpStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpStateChange.setStatus("mandatory")
_Cdx6500sdlcpLinkDowns_Type = Counter16
_Cdx6500sdlcpLinkDowns_Object = MibTableColumn
cdx6500sdlcpLinkDowns = _Cdx6500sdlcpLinkDowns_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 13),
    _Cdx6500sdlcpLinkDowns_Type()
)
cdx6500sdlcpLinkDowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpLinkDowns.setStatus("mandatory")
_Cdx6500sdlcpUtilizationIn_Type = Integer32
_Cdx6500sdlcpUtilizationIn_Object = MibTableColumn
cdx6500sdlcpUtilizationIn = _Cdx6500sdlcpUtilizationIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 14),
    _Cdx6500sdlcpUtilizationIn_Type()
)
cdx6500sdlcpUtilizationIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpUtilizationIn.setStatus("mandatory")
_Cdx6500sdlcpUtilizationOut_Type = Integer32
_Cdx6500sdlcpUtilizationOut_Object = MibTableColumn
cdx6500sdlcpUtilizationOut = _Cdx6500sdlcpUtilizationOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 15),
    _Cdx6500sdlcpUtilizationOut_Type()
)
cdx6500sdlcpUtilizationOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpUtilizationOut.setStatus("mandatory")
_Cdx6500sdlcpOverrunErrors_Type = Counter16
_Cdx6500sdlcpOverrunErrors_Object = MibTableColumn
cdx6500sdlcpOverrunErrors = _Cdx6500sdlcpOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 16),
    _Cdx6500sdlcpOverrunErrors_Type()
)
cdx6500sdlcpOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpOverrunErrors.setStatus("mandatory")
_Cdx6500sdlcpUnderrunErrors_Type = Counter16
_Cdx6500sdlcpUnderrunErrors_Object = MibTableColumn
cdx6500sdlcpUnderrunErrors = _Cdx6500sdlcpUnderrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 17),
    _Cdx6500sdlcpUnderrunErrors_Type()
)
cdx6500sdlcpUnderrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpUnderrunErrors.setStatus("mandatory")
_Cdx6500sdlcpCRCErrors_Type = Counter16
_Cdx6500sdlcpCRCErrors_Object = MibTableColumn
cdx6500sdlcpCRCErrors = _Cdx6500sdlcpCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 18),
    _Cdx6500sdlcpCRCErrors_Type()
)
cdx6500sdlcpCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpCRCErrors.setStatus("mandatory")
_Cdx6500sdlcpPacketsQueued_Type = Integer32
_Cdx6500sdlcpPacketsQueued_Object = MibTableColumn
cdx6500sdlcpPacketsQueued = _Cdx6500sdlcpPacketsQueued_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 19),
    _Cdx6500sdlcpPacketsQueued_Type()
)
cdx6500sdlcpPacketsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpPacketsQueued.setStatus("mandatory")
_Cdx6500sdlcpRRInFrames_Type = Counter32
_Cdx6500sdlcpRRInFrames_Object = MibTableColumn
cdx6500sdlcpRRInFrames = _Cdx6500sdlcpRRInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 20),
    _Cdx6500sdlcpRRInFrames_Type()
)
cdx6500sdlcpRRInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpRRInFrames.setStatus("mandatory")
_Cdx6500sdlcpRROutFrames_Type = Counter32
_Cdx6500sdlcpRROutFrames_Object = MibTableColumn
cdx6500sdlcpRROutFrames = _Cdx6500sdlcpRROutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 21),
    _Cdx6500sdlcpRROutFrames_Type()
)
cdx6500sdlcpRROutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpRROutFrames.setStatus("mandatory")
_Cdx6500sdlcpRNRInFrames_Type = Counter32
_Cdx6500sdlcpRNRInFrames_Object = MibTableColumn
cdx6500sdlcpRNRInFrames = _Cdx6500sdlcpRNRInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 22),
    _Cdx6500sdlcpRNRInFrames_Type()
)
cdx6500sdlcpRNRInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpRNRInFrames.setStatus("mandatory")
_Cdx6500sdlcpRNROutFrames_Type = Counter32
_Cdx6500sdlcpRNROutFrames_Object = MibTableColumn
cdx6500sdlcpRNROutFrames = _Cdx6500sdlcpRNROutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 23),
    _Cdx6500sdlcpRNROutFrames_Type()
)
cdx6500sdlcpRNROutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpRNROutFrames.setStatus("mandatory")
_Cdx6500sdlcpSNRMInFrames_Type = Counter32
_Cdx6500sdlcpSNRMInFrames_Object = MibTableColumn
cdx6500sdlcpSNRMInFrames = _Cdx6500sdlcpSNRMInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 24),
    _Cdx6500sdlcpSNRMInFrames_Type()
)
cdx6500sdlcpSNRMInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpSNRMInFrames.setStatus("mandatory")
_Cdx6500sdlcpSNRMOutFrames_Type = Counter32
_Cdx6500sdlcpSNRMOutFrames_Object = MibTableColumn
cdx6500sdlcpSNRMOutFrames = _Cdx6500sdlcpSNRMOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 25),
    _Cdx6500sdlcpSNRMOutFrames_Type()
)
cdx6500sdlcpSNRMOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpSNRMOutFrames.setStatus("mandatory")
_Cdx6500sdlcpUAInFrames_Type = Counter32
_Cdx6500sdlcpUAInFrames_Object = MibTableColumn
cdx6500sdlcpUAInFrames = _Cdx6500sdlcpUAInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 26),
    _Cdx6500sdlcpUAInFrames_Type()
)
cdx6500sdlcpUAInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpUAInFrames.setStatus("mandatory")
_Cdx6500sdlcpUAOutFrames_Type = Counter32
_Cdx6500sdlcpUAOutFrames_Object = MibTableColumn
cdx6500sdlcpUAOutFrames = _Cdx6500sdlcpUAOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 27),
    _Cdx6500sdlcpUAOutFrames_Type()
)
cdx6500sdlcpUAOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpUAOutFrames.setStatus("mandatory")
_Cdx6500sdlcpDMInFrames_Type = Counter32
_Cdx6500sdlcpDMInFrames_Object = MibTableColumn
cdx6500sdlcpDMInFrames = _Cdx6500sdlcpDMInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 28),
    _Cdx6500sdlcpDMInFrames_Type()
)
cdx6500sdlcpDMInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpDMInFrames.setStatus("mandatory")
_Cdx6500sdlcpDMOutFrames_Type = Counter32
_Cdx6500sdlcpDMOutFrames_Object = MibTableColumn
cdx6500sdlcpDMOutFrames = _Cdx6500sdlcpDMOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 29),
    _Cdx6500sdlcpDMOutFrames_Type()
)
cdx6500sdlcpDMOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpDMOutFrames.setStatus("mandatory")
_Cdx6500sdlcpXIDInFrames_Type = Counter32
_Cdx6500sdlcpXIDInFrames_Object = MibTableColumn
cdx6500sdlcpXIDInFrames = _Cdx6500sdlcpXIDInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 30),
    _Cdx6500sdlcpXIDInFrames_Type()
)
cdx6500sdlcpXIDInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpXIDInFrames.setStatus("mandatory")
_Cdx6500sdlcpXIDOutFrames_Type = Counter32
_Cdx6500sdlcpXIDOutFrames_Object = MibTableColumn
cdx6500sdlcpXIDOutFrames = _Cdx6500sdlcpXIDOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 31),
    _Cdx6500sdlcpXIDOutFrames_Type()
)
cdx6500sdlcpXIDOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpXIDOutFrames.setStatus("mandatory")
_Cdx6500sdlcpREJInFrames_Type = Counter32
_Cdx6500sdlcpREJInFrames_Object = MibTableColumn
cdx6500sdlcpREJInFrames = _Cdx6500sdlcpREJInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 32),
    _Cdx6500sdlcpREJInFrames_Type()
)
cdx6500sdlcpREJInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpREJInFrames.setStatus("mandatory")
_Cdx6500sdlcpREJOutFrames_Type = Counter32
_Cdx6500sdlcpREJOutFrames_Object = MibTableColumn
cdx6500sdlcpREJOutFrames = _Cdx6500sdlcpREJOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 33),
    _Cdx6500sdlcpREJOutFrames_Type()
)
cdx6500sdlcpREJOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpREJOutFrames.setStatus("mandatory")
_Cdx6500sdlcpDISCInFrames_Type = Counter32
_Cdx6500sdlcpDISCInFrames_Object = MibTableColumn
cdx6500sdlcpDISCInFrames = _Cdx6500sdlcpDISCInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 34),
    _Cdx6500sdlcpDISCInFrames_Type()
)
cdx6500sdlcpDISCInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpDISCInFrames.setStatus("mandatory")
_Cdx6500sdlcpDISCOutFrames_Type = Counter32
_Cdx6500sdlcpDISCOutFrames_Object = MibTableColumn
cdx6500sdlcpDISCOutFrames = _Cdx6500sdlcpDISCOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 35),
    _Cdx6500sdlcpDISCOutFrames_Type()
)
cdx6500sdlcpDISCOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpDISCOutFrames.setStatus("mandatory")
_Cdx6500sdlcpRDInFrames_Type = Counter32
_Cdx6500sdlcpRDInFrames_Object = MibTableColumn
cdx6500sdlcpRDInFrames = _Cdx6500sdlcpRDInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 36),
    _Cdx6500sdlcpRDInFrames_Type()
)
cdx6500sdlcpRDInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpRDInFrames.setStatus("mandatory")
_Cdx6500sdlcpRDOutFrames_Type = Counter32
_Cdx6500sdlcpRDOutFrames_Object = MibTableColumn
cdx6500sdlcpRDOutFrames = _Cdx6500sdlcpRDOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 37),
    _Cdx6500sdlcpRDOutFrames_Type()
)
cdx6500sdlcpRDOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpRDOutFrames.setStatus("mandatory")
_Cdx6500sdlcpFRMRInFrames_Type = Counter32
_Cdx6500sdlcpFRMRInFrames_Object = MibTableColumn
cdx6500sdlcpFRMRInFrames = _Cdx6500sdlcpFRMRInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 38),
    _Cdx6500sdlcpFRMRInFrames_Type()
)
cdx6500sdlcpFRMRInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpFRMRInFrames.setStatus("mandatory")
_Cdx6500sdlcpFRMROutFrames_Type = Counter32
_Cdx6500sdlcpFRMROutFrames_Object = MibTableColumn
cdx6500sdlcpFRMROutFrames = _Cdx6500sdlcpFRMROutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 39),
    _Cdx6500sdlcpFRMROutFrames_Type()
)
cdx6500sdlcpFRMROutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpFRMROutFrames.setStatus("mandatory")
_Cdx6500sdlcpUPInFrames_Type = Counter32
_Cdx6500sdlcpUPInFrames_Object = MibTableColumn
cdx6500sdlcpUPInFrames = _Cdx6500sdlcpUPInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 40),
    _Cdx6500sdlcpUPInFrames_Type()
)
cdx6500sdlcpUPInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpUPInFrames.setStatus("mandatory")
_Cdx6500sdlcpUPOutFrames_Type = Counter32
_Cdx6500sdlcpUPOutFrames_Object = MibTableColumn
cdx6500sdlcpUPOutFrames = _Cdx6500sdlcpUPOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 41),
    _Cdx6500sdlcpUPOutFrames_Type()
)
cdx6500sdlcpUPOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpUPOutFrames.setStatus("mandatory")
_Cdx6500sdlcpTESTInFrames_Type = Counter32
_Cdx6500sdlcpTESTInFrames_Object = MibTableColumn
cdx6500sdlcpTESTInFrames = _Cdx6500sdlcpTESTInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 42),
    _Cdx6500sdlcpTESTInFrames_Type()
)
cdx6500sdlcpTESTInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpTESTInFrames.setStatus("mandatory")
_Cdx6500sdlcpTESTOutFrames_Type = Counter32
_Cdx6500sdlcpTESTOutFrames_Object = MibTableColumn
cdx6500sdlcpTESTOutFrames = _Cdx6500sdlcpTESTOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 43),
    _Cdx6500sdlcpTESTOutFrames_Type()
)
cdx6500sdlcpTESTOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpTESTOutFrames.setStatus("mandatory")
_Cdx6500sdlcpXIDNullInFrames_Type = Counter32
_Cdx6500sdlcpXIDNullInFrames_Object = MibTableColumn
cdx6500sdlcpXIDNullInFrames = _Cdx6500sdlcpXIDNullInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 44),
    _Cdx6500sdlcpXIDNullInFrames_Type()
)
cdx6500sdlcpXIDNullInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpXIDNullInFrames.setStatus("mandatory")
_Cdx6500sdlcpXIDNullOutFrames_Type = Counter32
_Cdx6500sdlcpXIDNullOutFrames_Object = MibTableColumn
cdx6500sdlcpXIDNullOutFrames = _Cdx6500sdlcpXIDNullOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 45),
    _Cdx6500sdlcpXIDNullOutFrames_Type()
)
cdx6500sdlcpXIDNullOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpXIDNullOutFrames.setStatus("mandatory")
_Cdx6500sdlcpXID0InFrames_Type = Counter32
_Cdx6500sdlcpXID0InFrames_Object = MibTableColumn
cdx6500sdlcpXID0InFrames = _Cdx6500sdlcpXID0InFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 46),
    _Cdx6500sdlcpXID0InFrames_Type()
)
cdx6500sdlcpXID0InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpXID0InFrames.setStatus("mandatory")
_Cdx6500sdlcpXID0OutFrames_Type = Counter32
_Cdx6500sdlcpXID0OutFrames_Object = MibTableColumn
cdx6500sdlcpXID0OutFrames = _Cdx6500sdlcpXID0OutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 47),
    _Cdx6500sdlcpXID0OutFrames_Type()
)
cdx6500sdlcpXID0OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpXID0OutFrames.setStatus("mandatory")
_Cdx6500sdlcpXID1InFrames_Type = Counter32
_Cdx6500sdlcpXID1InFrames_Object = MibTableColumn
cdx6500sdlcpXID1InFrames = _Cdx6500sdlcpXID1InFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 48),
    _Cdx6500sdlcpXID1InFrames_Type()
)
cdx6500sdlcpXID1InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpXID1InFrames.setStatus("mandatory")
_Cdx6500sdlcpXID1OutFrames_Type = Counter32
_Cdx6500sdlcpXID1OutFrames_Object = MibTableColumn
cdx6500sdlcpXID1OutFrames = _Cdx6500sdlcpXID1OutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 49),
    _Cdx6500sdlcpXID1OutFrames_Type()
)
cdx6500sdlcpXID1OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpXID1OutFrames.setStatus("mandatory")
_Cdx6500sdlcpXID3InFrames_Type = Counter32
_Cdx6500sdlcpXID3InFrames_Object = MibTableColumn
cdx6500sdlcpXID3InFrames = _Cdx6500sdlcpXID3InFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 50),
    _Cdx6500sdlcpXID3InFrames_Type()
)
cdx6500sdlcpXID3InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpXID3InFrames.setStatus("mandatory")
_Cdx6500sdlcpXID3OutFrames_Type = Counter32
_Cdx6500sdlcpXID3OutFrames_Object = MibTableColumn
cdx6500sdlcpXID3OutFrames = _Cdx6500sdlcpXID3OutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 12, 1, 51),
    _Cdx6500sdlcpXID3OutFrames_Type()
)
cdx6500sdlcpXID3OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcpXID3OutFrames.setStatus("mandatory")
_Cdx6500PSTStationProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTStationProtocolGroup = _Cdx6500PSTStationProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3)
)
_Cdx6500SPSTSDLCStationTable_Object = MibTable
cdx6500SPSTSDLCStationTable = _Cdx6500SPSTSDLCStationTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cdx6500SPSTSDLCStationTable.setStatus("mandatory")
_Cdx6500SPSTSDLCStationEntry_Object = MibTableRow
cdx6500SPSTSDLCStationEntry = _Cdx6500SPSTSDLCStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1)
)
cdx6500SPSTSDLCStationEntry.setIndexNames(
    (0, "SDLC-OPT-MIB", "cdx6500sdlcsStatsPortNum"),
    (0, "SDLC-OPT-MIB", "cdx6500sdlcsStatsStationNum"),
)
if mibBuilder.loadTexts:
    cdx6500SPSTSDLCStationEntry.setStatus("mandatory")


class _Cdx6500sdlcsStatsPortNum_Type(Integer32):
    """Custom type cdx6500sdlcsStatsPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500sdlcsStatsPortNum_Type.__name__ = "Integer32"
_Cdx6500sdlcsStatsPortNum_Object = MibTableColumn
cdx6500sdlcsStatsPortNum = _Cdx6500sdlcsStatsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 1),
    _Cdx6500sdlcsStatsPortNum_Type()
)
cdx6500sdlcsStatsPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsStatsPortNum.setStatus("mandatory")


class _Cdx6500sdlcsStatsStationNum_Type(Integer32):
    """Custom type cdx6500sdlcsStatsStationNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Cdx6500sdlcsStatsStationNum_Type.__name__ = "Integer32"
_Cdx6500sdlcsStatsStationNum_Object = MibTableColumn
cdx6500sdlcsStatsStationNum = _Cdx6500sdlcsStatsStationNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 2),
    _Cdx6500sdlcsStatsStationNum_Type()
)
cdx6500sdlcsStatsStationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsStatsStationNum.setStatus("mandatory")


class _Cdx6500sdlcsStatsStationAddr_Type(Integer32):
    """Custom type cdx6500sdlcsStatsStationAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500sdlcsStatsStationAddr_Type.__name__ = "Integer32"
_Cdx6500sdlcsStatsStationAddr_Object = MibTableColumn
cdx6500sdlcsStatsStationAddr = _Cdx6500sdlcsStatsStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 3),
    _Cdx6500sdlcsStatsStationAddr_Type()
)
cdx6500sdlcsStatsStationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsStatsStationAddr.setStatus("mandatory")


class _Cdx6500sdlcsQLLCState_Type(DisplayString):
    """Custom type cdx6500sdlcsQLLCState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cdx6500sdlcsQLLCState_Type.__name__ = "DisplayString"
_Cdx6500sdlcsQLLCState_Object = MibTableColumn
cdx6500sdlcsQLLCState = _Cdx6500sdlcsQLLCState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 4),
    _Cdx6500sdlcsQLLCState_Type()
)
cdx6500sdlcsQLLCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsQLLCState.setStatus("mandatory")
_Cdx6500sdlcsCharInTotal_Type = Counter32
_Cdx6500sdlcsCharInTotal_Object = MibTableColumn
cdx6500sdlcsCharInTotal = _Cdx6500sdlcsCharInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 5),
    _Cdx6500sdlcsCharInTotal_Type()
)
cdx6500sdlcsCharInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsCharInTotal.setStatus("mandatory")
_Cdx6500sdlcsCharOutTotal_Type = Counter32
_Cdx6500sdlcsCharOutTotal_Object = MibTableColumn
cdx6500sdlcsCharOutTotal = _Cdx6500sdlcsCharOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 6),
    _Cdx6500sdlcsCharOutTotal_Type()
)
cdx6500sdlcsCharOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsCharOutTotal.setStatus("mandatory")
_Cdx6500sdlcsCharsInPerSec_Type = Integer32
_Cdx6500sdlcsCharsInPerSec_Object = MibTableColumn
cdx6500sdlcsCharsInPerSec = _Cdx6500sdlcsCharsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 7),
    _Cdx6500sdlcsCharsInPerSec_Type()
)
cdx6500sdlcsCharsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsCharsInPerSec.setStatus("mandatory")
_Cdx6500sdlcsCharsOutPerSec_Type = Integer32
_Cdx6500sdlcsCharsOutPerSec_Object = MibTableColumn
cdx6500sdlcsCharsOutPerSec = _Cdx6500sdlcsCharsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 8),
    _Cdx6500sdlcsCharsOutPerSec_Type()
)
cdx6500sdlcsCharsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsCharsOutPerSec.setStatus("mandatory")
_Cdx6500sdlcsFrameInTotal_Type = Counter32
_Cdx6500sdlcsFrameInTotal_Object = MibTableColumn
cdx6500sdlcsFrameInTotal = _Cdx6500sdlcsFrameInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 9),
    _Cdx6500sdlcsFrameInTotal_Type()
)
cdx6500sdlcsFrameInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsFrameInTotal.setStatus("mandatory")
_Cdx6500sdlcsFrameOutTotal_Type = Counter32
_Cdx6500sdlcsFrameOutTotal_Object = MibTableColumn
cdx6500sdlcsFrameOutTotal = _Cdx6500sdlcsFrameOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 10),
    _Cdx6500sdlcsFrameOutTotal_Type()
)
cdx6500sdlcsFrameOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsFrameOutTotal.setStatus("mandatory")
_Cdx6500sdlcsFramesInPerSec_Type = Integer32
_Cdx6500sdlcsFramesInPerSec_Object = MibTableColumn
cdx6500sdlcsFramesInPerSec = _Cdx6500sdlcsFramesInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 11),
    _Cdx6500sdlcsFramesInPerSec_Type()
)
cdx6500sdlcsFramesInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsFramesInPerSec.setStatus("mandatory")
_Cdx6500sdlcsFramesOutPerSec_Type = Integer32
_Cdx6500sdlcsFramesOutPerSec_Object = MibTableColumn
cdx6500sdlcsFramesOutPerSec = _Cdx6500sdlcsFramesOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 12),
    _Cdx6500sdlcsFramesOutPerSec_Type()
)
cdx6500sdlcsFramesOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsFramesOutPerSec.setStatus("mandatory")
_Cdx6500sdlcsQRRInTotal_Type = Counter16
_Cdx6500sdlcsQRRInTotal_Object = MibTableColumn
cdx6500sdlcsQRRInTotal = _Cdx6500sdlcsQRRInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 13),
    _Cdx6500sdlcsQRRInTotal_Type()
)
cdx6500sdlcsQRRInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsQRRInTotal.setStatus("mandatory")
_Cdx6500sdlcsQRROutTotal_Type = Counter16
_Cdx6500sdlcsQRROutTotal_Object = MibTableColumn
cdx6500sdlcsQRROutTotal = _Cdx6500sdlcsQRROutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 14),
    _Cdx6500sdlcsQRROutTotal_Type()
)
cdx6500sdlcsQRROutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsQRROutTotal.setStatus("mandatory")
_Cdx6500sdlcsUtilizationIn_Type = Integer32
_Cdx6500sdlcsUtilizationIn_Object = MibTableColumn
cdx6500sdlcsUtilizationIn = _Cdx6500sdlcsUtilizationIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 15),
    _Cdx6500sdlcsUtilizationIn_Type()
)
cdx6500sdlcsUtilizationIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsUtilizationIn.setStatus("mandatory")
_Cdx6500sdlcsUtilizationOut_Type = Integer32
_Cdx6500sdlcsUtilizationOut_Object = MibTableColumn
cdx6500sdlcsUtilizationOut = _Cdx6500sdlcsUtilizationOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 16),
    _Cdx6500sdlcsUtilizationOut_Type()
)
cdx6500sdlcsUtilizationOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsUtilizationOut.setStatus("mandatory")
_Cdx6500sdlcsPacketsQueued_Type = Integer32
_Cdx6500sdlcsPacketsQueued_Object = MibTableColumn
cdx6500sdlcsPacketsQueued = _Cdx6500sdlcsPacketsQueued_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 17),
    _Cdx6500sdlcsPacketsQueued_Type()
)
cdx6500sdlcsPacketsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsPacketsQueued.setStatus("mandatory")
_Cdx6500sdlcsRRInFrames_Type = Counter32
_Cdx6500sdlcsRRInFrames_Object = MibTableColumn
cdx6500sdlcsRRInFrames = _Cdx6500sdlcsRRInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 18),
    _Cdx6500sdlcsRRInFrames_Type()
)
cdx6500sdlcsRRInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsRRInFrames.setStatus("mandatory")
_Cdx6500sdlcsRROutFrames_Type = Counter32
_Cdx6500sdlcsRROutFrames_Object = MibTableColumn
cdx6500sdlcsRROutFrames = _Cdx6500sdlcsRROutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 19),
    _Cdx6500sdlcsRROutFrames_Type()
)
cdx6500sdlcsRROutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsRROutFrames.setStatus("mandatory")
_Cdx6500sdlcsRNRInFrames_Type = Counter32
_Cdx6500sdlcsRNRInFrames_Object = MibTableColumn
cdx6500sdlcsRNRInFrames = _Cdx6500sdlcsRNRInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 20),
    _Cdx6500sdlcsRNRInFrames_Type()
)
cdx6500sdlcsRNRInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsRNRInFrames.setStatus("mandatory")
_Cdx6500sdlcsRNROutFrames_Type = Counter32
_Cdx6500sdlcsRNROutFrames_Object = MibTableColumn
cdx6500sdlcsRNROutFrames = _Cdx6500sdlcsRNROutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 21),
    _Cdx6500sdlcsRNROutFrames_Type()
)
cdx6500sdlcsRNROutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsRNROutFrames.setStatus("mandatory")
_Cdx6500sdlcsSNRMInFrames_Type = Counter32
_Cdx6500sdlcsSNRMInFrames_Object = MibTableColumn
cdx6500sdlcsSNRMInFrames = _Cdx6500sdlcsSNRMInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 22),
    _Cdx6500sdlcsSNRMInFrames_Type()
)
cdx6500sdlcsSNRMInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsSNRMInFrames.setStatus("mandatory")
_Cdx6500sdlcsSNRMOutFrames_Type = Counter32
_Cdx6500sdlcsSNRMOutFrames_Object = MibTableColumn
cdx6500sdlcsSNRMOutFrames = _Cdx6500sdlcsSNRMOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 23),
    _Cdx6500sdlcsSNRMOutFrames_Type()
)
cdx6500sdlcsSNRMOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsSNRMOutFrames.setStatus("mandatory")
_Cdx6500sdlcsUAInFrames_Type = Counter32
_Cdx6500sdlcsUAInFrames_Object = MibTableColumn
cdx6500sdlcsUAInFrames = _Cdx6500sdlcsUAInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 24),
    _Cdx6500sdlcsUAInFrames_Type()
)
cdx6500sdlcsUAInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsUAInFrames.setStatus("mandatory")
_Cdx6500sdlcsUAOutFrames_Type = Counter32
_Cdx6500sdlcsUAOutFrames_Object = MibTableColumn
cdx6500sdlcsUAOutFrames = _Cdx6500sdlcsUAOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 25),
    _Cdx6500sdlcsUAOutFrames_Type()
)
cdx6500sdlcsUAOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsUAOutFrames.setStatus("mandatory")
_Cdx6500sdlcsDMInFrames_Type = Counter32
_Cdx6500sdlcsDMInFrames_Object = MibTableColumn
cdx6500sdlcsDMInFrames = _Cdx6500sdlcsDMInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 26),
    _Cdx6500sdlcsDMInFrames_Type()
)
cdx6500sdlcsDMInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsDMInFrames.setStatus("mandatory")
_Cdx6500sdlcsDMOutFrames_Type = Counter32
_Cdx6500sdlcsDMOutFrames_Object = MibTableColumn
cdx6500sdlcsDMOutFrames = _Cdx6500sdlcsDMOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 27),
    _Cdx6500sdlcsDMOutFrames_Type()
)
cdx6500sdlcsDMOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsDMOutFrames.setStatus("mandatory")
_Cdx6500sdlcsXIDInFrames_Type = Counter32
_Cdx6500sdlcsXIDInFrames_Object = MibTableColumn
cdx6500sdlcsXIDInFrames = _Cdx6500sdlcsXIDInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 28),
    _Cdx6500sdlcsXIDInFrames_Type()
)
cdx6500sdlcsXIDInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsXIDInFrames.setStatus("mandatory")
_Cdx6500sdlcsXIDOutFrames_Type = Counter32
_Cdx6500sdlcsXIDOutFrames_Object = MibTableColumn
cdx6500sdlcsXIDOutFrames = _Cdx6500sdlcsXIDOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 29),
    _Cdx6500sdlcsXIDOutFrames_Type()
)
cdx6500sdlcsXIDOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsXIDOutFrames.setStatus("mandatory")
_Cdx6500sdlcsREJInFrames_Type = Counter32
_Cdx6500sdlcsREJInFrames_Object = MibTableColumn
cdx6500sdlcsREJInFrames = _Cdx6500sdlcsREJInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 30),
    _Cdx6500sdlcsREJInFrames_Type()
)
cdx6500sdlcsREJInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsREJInFrames.setStatus("mandatory")
_Cdx6500sdlcsREJOutFrames_Type = Counter32
_Cdx6500sdlcsREJOutFrames_Object = MibTableColumn
cdx6500sdlcsREJOutFrames = _Cdx6500sdlcsREJOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 31),
    _Cdx6500sdlcsREJOutFrames_Type()
)
cdx6500sdlcsREJOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsREJOutFrames.setStatus("mandatory")
_Cdx6500sdlcsDISCInFrames_Type = Counter32
_Cdx6500sdlcsDISCInFrames_Object = MibTableColumn
cdx6500sdlcsDISCInFrames = _Cdx6500sdlcsDISCInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 32),
    _Cdx6500sdlcsDISCInFrames_Type()
)
cdx6500sdlcsDISCInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsDISCInFrames.setStatus("mandatory")
_Cdx6500sdlcsDISCOutFrames_Type = Counter32
_Cdx6500sdlcsDISCOutFrames_Object = MibTableColumn
cdx6500sdlcsDISCOutFrames = _Cdx6500sdlcsDISCOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 33),
    _Cdx6500sdlcsDISCOutFrames_Type()
)
cdx6500sdlcsDISCOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsDISCOutFrames.setStatus("mandatory")
_Cdx6500sdlcsRDInFrames_Type = Counter32
_Cdx6500sdlcsRDInFrames_Object = MibTableColumn
cdx6500sdlcsRDInFrames = _Cdx6500sdlcsRDInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 34),
    _Cdx6500sdlcsRDInFrames_Type()
)
cdx6500sdlcsRDInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsRDInFrames.setStatus("mandatory")
_Cdx6500sdlcsRDOutFrames_Type = Counter32
_Cdx6500sdlcsRDOutFrames_Object = MibTableColumn
cdx6500sdlcsRDOutFrames = _Cdx6500sdlcsRDOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 35),
    _Cdx6500sdlcsRDOutFrames_Type()
)
cdx6500sdlcsRDOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsRDOutFrames.setStatus("mandatory")
_Cdx6500sdlcsFRMRInFrames_Type = Counter32
_Cdx6500sdlcsFRMRInFrames_Object = MibTableColumn
cdx6500sdlcsFRMRInFrames = _Cdx6500sdlcsFRMRInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 36),
    _Cdx6500sdlcsFRMRInFrames_Type()
)
cdx6500sdlcsFRMRInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsFRMRInFrames.setStatus("mandatory")
_Cdx6500sdlcsFRMROutFrames_Type = Counter32
_Cdx6500sdlcsFRMROutFrames_Object = MibTableColumn
cdx6500sdlcsFRMROutFrames = _Cdx6500sdlcsFRMROutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 37),
    _Cdx6500sdlcsFRMROutFrames_Type()
)
cdx6500sdlcsFRMROutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsFRMROutFrames.setStatus("mandatory")
_Cdx6500sdlcsUPInFrames_Type = Counter32
_Cdx6500sdlcsUPInFrames_Object = MibTableColumn
cdx6500sdlcsUPInFrames = _Cdx6500sdlcsUPInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 38),
    _Cdx6500sdlcsUPInFrames_Type()
)
cdx6500sdlcsUPInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsUPInFrames.setStatus("mandatory")
_Cdx6500sdlcsUPOutFrames_Type = Counter32
_Cdx6500sdlcsUPOutFrames_Object = MibTableColumn
cdx6500sdlcsUPOutFrames = _Cdx6500sdlcsUPOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 39),
    _Cdx6500sdlcsUPOutFrames_Type()
)
cdx6500sdlcsUPOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsUPOutFrames.setStatus("mandatory")
_Cdx6500sdlcsTESTInFrames_Type = Counter32
_Cdx6500sdlcsTESTInFrames_Object = MibTableColumn
cdx6500sdlcsTESTInFrames = _Cdx6500sdlcsTESTInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 40),
    _Cdx6500sdlcsTESTInFrames_Type()
)
cdx6500sdlcsTESTInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsTESTInFrames.setStatus("mandatory")
_Cdx6500sdlcsTESTOutFrames_Type = Counter32
_Cdx6500sdlcsTESTOutFrames_Object = MibTableColumn
cdx6500sdlcsTESTOutFrames = _Cdx6500sdlcsTESTOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 41),
    _Cdx6500sdlcsTESTOutFrames_Type()
)
cdx6500sdlcsTESTOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsTESTOutFrames.setStatus("mandatory")
_Cdx6500sdlcsQSMInFrames_Type = Counter16
_Cdx6500sdlcsQSMInFrames_Object = MibTableColumn
cdx6500sdlcsQSMInFrames = _Cdx6500sdlcsQSMInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 42),
    _Cdx6500sdlcsQSMInFrames_Type()
)
cdx6500sdlcsQSMInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsQSMInFrames.setStatus("mandatory")
_Cdx6500sdlcsQSMOutFrames_Type = Counter16
_Cdx6500sdlcsQSMOutFrames_Object = MibTableColumn
cdx6500sdlcsQSMOutFrames = _Cdx6500sdlcsQSMOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 43),
    _Cdx6500sdlcsQSMOutFrames_Type()
)
cdx6500sdlcsQSMOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsQSMOutFrames.setStatus("mandatory")
_Cdx6500sdlcsQUAInFrames_Type = Counter16
_Cdx6500sdlcsQUAInFrames_Object = MibTableColumn
cdx6500sdlcsQUAInFrames = _Cdx6500sdlcsQUAInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 44),
    _Cdx6500sdlcsQUAInFrames_Type()
)
cdx6500sdlcsQUAInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsQUAInFrames.setStatus("mandatory")
_Cdx6500sdlcsQUAOutFrames_Type = Counter16
_Cdx6500sdlcsQUAOutFrames_Object = MibTableColumn
cdx6500sdlcsQUAOutFrames = _Cdx6500sdlcsQUAOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 45),
    _Cdx6500sdlcsQUAOutFrames_Type()
)
cdx6500sdlcsQUAOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsQUAOutFrames.setStatus("mandatory")
_Cdx6500sdlcsQRDInFrames_Type = Counter16
_Cdx6500sdlcsQRDInFrames_Object = MibTableColumn
cdx6500sdlcsQRDInFrames = _Cdx6500sdlcsQRDInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 46),
    _Cdx6500sdlcsQRDInFrames_Type()
)
cdx6500sdlcsQRDInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsQRDInFrames.setStatus("mandatory")
_Cdx6500sdlcsQRDOutFrames_Type = Counter16
_Cdx6500sdlcsQRDOutFrames_Object = MibTableColumn
cdx6500sdlcsQRDOutFrames = _Cdx6500sdlcsQRDOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 47),
    _Cdx6500sdlcsQRDOutFrames_Type()
)
cdx6500sdlcsQRDOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsQRDOutFrames.setStatus("mandatory")
_Cdx6500sdlcsQFRMRInFrames_Type = Counter16
_Cdx6500sdlcsQFRMRInFrames_Object = MibTableColumn
cdx6500sdlcsQFRMRInFrames = _Cdx6500sdlcsQFRMRInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 48),
    _Cdx6500sdlcsQFRMRInFrames_Type()
)
cdx6500sdlcsQFRMRInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsQFRMRInFrames.setStatus("mandatory")
_Cdx6500sdlcsQFRMROutFrames_Type = Counter16
_Cdx6500sdlcsQFRMROutFrames_Object = MibTableColumn
cdx6500sdlcsQFRMROutFrames = _Cdx6500sdlcsQFRMROutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 49),
    _Cdx6500sdlcsQFRMROutFrames_Type()
)
cdx6500sdlcsQFRMROutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsQFRMROutFrames.setStatus("mandatory")
_Cdx6500sdlcsQXIDInFrames_Type = Counter16
_Cdx6500sdlcsQXIDInFrames_Object = MibTableColumn
cdx6500sdlcsQXIDInFrames = _Cdx6500sdlcsQXIDInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 50),
    _Cdx6500sdlcsQXIDInFrames_Type()
)
cdx6500sdlcsQXIDInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsQXIDInFrames.setStatus("mandatory")
_Cdx6500sdlcsQXIDOutFrames_Type = Counter16
_Cdx6500sdlcsQXIDOutFrames_Object = MibTableColumn
cdx6500sdlcsQXIDOutFrames = _Cdx6500sdlcsQXIDOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 51),
    _Cdx6500sdlcsQXIDOutFrames_Type()
)
cdx6500sdlcsQXIDOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsQXIDOutFrames.setStatus("mandatory")
_Cdx6500sdlcsQDCInFrames_Type = Counter16
_Cdx6500sdlcsQDCInFrames_Object = MibTableColumn
cdx6500sdlcsQDCInFrames = _Cdx6500sdlcsQDCInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 52),
    _Cdx6500sdlcsQDCInFrames_Type()
)
cdx6500sdlcsQDCInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsQDCInFrames.setStatus("mandatory")
_Cdx6500sdlcsQDCOutFrames_Type = Counter16
_Cdx6500sdlcsQDCOutFrames_Object = MibTableColumn
cdx6500sdlcsQDCOutFrames = _Cdx6500sdlcsQDCOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 53),
    _Cdx6500sdlcsQDCOutFrames_Type()
)
cdx6500sdlcsQDCOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsQDCOutFrames.setStatus("mandatory")
_Cdx6500sdlcsQDMInFrames_Type = Counter16
_Cdx6500sdlcsQDMInFrames_Object = MibTableColumn
cdx6500sdlcsQDMInFrames = _Cdx6500sdlcsQDMInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 54),
    _Cdx6500sdlcsQDMInFrames_Type()
)
cdx6500sdlcsQDMInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsQDMInFrames.setStatus("mandatory")
_Cdx6500sdlcsQDMOutFrames_Type = Counter16
_Cdx6500sdlcsQDMOutFrames_Object = MibTableColumn
cdx6500sdlcsQDMOutFrames = _Cdx6500sdlcsQDMOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 55),
    _Cdx6500sdlcsQDMOutFrames_Type()
)
cdx6500sdlcsQDMOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsQDMOutFrames.setStatus("mandatory")
_Cdx6500sdlcsQTESTInFrames_Type = Counter16
_Cdx6500sdlcsQTESTInFrames_Object = MibTableColumn
cdx6500sdlcsQTESTInFrames = _Cdx6500sdlcsQTESTInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 56),
    _Cdx6500sdlcsQTESTInFrames_Type()
)
cdx6500sdlcsQTESTInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsQTESTInFrames.setStatus("mandatory")
_Cdx6500sdlcsQTESTOutFrames_Type = Counter16
_Cdx6500sdlcsQTESTOutFrames_Object = MibTableColumn
cdx6500sdlcsQTESTOutFrames = _Cdx6500sdlcsQTESTOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 57),
    _Cdx6500sdlcsQTESTOutFrames_Type()
)
cdx6500sdlcsQTESTOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsQTESTOutFrames.setStatus("mandatory")
_Cdx6500sdlcsQSSInFrames_Type = Counter16
_Cdx6500sdlcsQSSInFrames_Object = MibTableColumn
cdx6500sdlcsQSSInFrames = _Cdx6500sdlcsQSSInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 58),
    _Cdx6500sdlcsQSSInFrames_Type()
)
cdx6500sdlcsQSSInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsQSSInFrames.setStatus("mandatory")
_Cdx6500sdlcsQSSOutFrames_Type = Counter16
_Cdx6500sdlcsQSSOutFrames_Object = MibTableColumn
cdx6500sdlcsQSSOutFrames = _Cdx6500sdlcsQSSOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 59),
    _Cdx6500sdlcsQSSOutFrames_Type()
)
cdx6500sdlcsQSSOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsQSSOutFrames.setStatus("mandatory")
_Cdx6500sdlcsQRSInFrames_Type = Counter16
_Cdx6500sdlcsQRSInFrames_Object = MibTableColumn
cdx6500sdlcsQRSInFrames = _Cdx6500sdlcsQRSInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 60),
    _Cdx6500sdlcsQRSInFrames_Type()
)
cdx6500sdlcsQRSInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsQRSInFrames.setStatus("mandatory")
_Cdx6500sdlcsQRSOutFrames_Type = Counter16
_Cdx6500sdlcsQRSOutFrames_Object = MibTableColumn
cdx6500sdlcsQRSOutFrames = _Cdx6500sdlcsQRSOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 61),
    _Cdx6500sdlcsQRSOutFrames_Type()
)
cdx6500sdlcsQRSOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsQRSOutFrames.setStatus("mandatory")
_Cdx6500sdlcsXIDNullInFrames_Type = Counter32
_Cdx6500sdlcsXIDNullInFrames_Object = MibTableColumn
cdx6500sdlcsXIDNullInFrames = _Cdx6500sdlcsXIDNullInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 62),
    _Cdx6500sdlcsXIDNullInFrames_Type()
)
cdx6500sdlcsXIDNullInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsXIDNullInFrames.setStatus("mandatory")
_Cdx6500sdlcsXIDNullOutFrames_Type = Counter32
_Cdx6500sdlcsXIDNullOutFrames_Object = MibTableColumn
cdx6500sdlcsXIDNullOutFrames = _Cdx6500sdlcsXIDNullOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 63),
    _Cdx6500sdlcsXIDNullOutFrames_Type()
)
cdx6500sdlcsXIDNullOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsXIDNullOutFrames.setStatus("mandatory")
_Cdx6500sdlcsXID0InFrames_Type = Counter32
_Cdx6500sdlcsXID0InFrames_Object = MibTableColumn
cdx6500sdlcsXID0InFrames = _Cdx6500sdlcsXID0InFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 64),
    _Cdx6500sdlcsXID0InFrames_Type()
)
cdx6500sdlcsXID0InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsXID0InFrames.setStatus("mandatory")
_Cdx6500sdlcsXID0OutFrames_Type = Counter32
_Cdx6500sdlcsXID0OutFrames_Object = MibTableColumn
cdx6500sdlcsXID0OutFrames = _Cdx6500sdlcsXID0OutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 65),
    _Cdx6500sdlcsXID0OutFrames_Type()
)
cdx6500sdlcsXID0OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsXID0OutFrames.setStatus("mandatory")
_Cdx6500sdlcsXID1InFrames_Type = Counter32
_Cdx6500sdlcsXID1InFrames_Object = MibTableColumn
cdx6500sdlcsXID1InFrames = _Cdx6500sdlcsXID1InFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 66),
    _Cdx6500sdlcsXID1InFrames_Type()
)
cdx6500sdlcsXID1InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsXID1InFrames.setStatus("mandatory")
_Cdx6500sdlcsXID1OutFrames_Type = Counter32
_Cdx6500sdlcsXID1OutFrames_Object = MibTableColumn
cdx6500sdlcsXID1OutFrames = _Cdx6500sdlcsXID1OutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 67),
    _Cdx6500sdlcsXID1OutFrames_Type()
)
cdx6500sdlcsXID1OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsXID1OutFrames.setStatus("mandatory")
_Cdx6500sdlcsXID3InFrames_Type = Counter32
_Cdx6500sdlcsXID3InFrames_Object = MibTableColumn
cdx6500sdlcsXID3InFrames = _Cdx6500sdlcsXID3InFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 68),
    _Cdx6500sdlcsXID3InFrames_Type()
)
cdx6500sdlcsXID3InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsXID3InFrames.setStatus("mandatory")
_Cdx6500sdlcsXID3OutFrames_Type = Counter32
_Cdx6500sdlcsXID3OutFrames_Object = MibTableColumn
cdx6500sdlcsXID3OutFrames = _Cdx6500sdlcsXID3OutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 69),
    _Cdx6500sdlcsXID3OutFrames_Type()
)
cdx6500sdlcsXID3OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsXID3OutFrames.setStatus("mandatory")


class _Cdx6500sdlcsVSNumber_Type(Integer32):
    """Custom type cdx6500sdlcsVSNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Cdx6500sdlcsVSNumber_Type.__name__ = "Integer32"
_Cdx6500sdlcsVSNumber_Object = MibTableColumn
cdx6500sdlcsVSNumber = _Cdx6500sdlcsVSNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 70),
    _Cdx6500sdlcsVSNumber_Type()
)
cdx6500sdlcsVSNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsVSNumber.setStatus("mandatory")


class _Cdx6500sdlcsVRNumber_Type(Integer32):
    """Custom type cdx6500sdlcsVRNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Cdx6500sdlcsVRNumber_Type.__name__ = "Integer32"
_Cdx6500sdlcsVRNumber_Object = MibTableColumn
cdx6500sdlcsVRNumber = _Cdx6500sdlcsVRNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 71),
    _Cdx6500sdlcsVRNumber_Type()
)
cdx6500sdlcsVRNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsVRNumber.setStatus("mandatory")


class _Cdx6500sdlcsNRNumber_Type(Integer32):
    """Custom type cdx6500sdlcsNRNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Cdx6500sdlcsNRNumber_Type.__name__ = "Integer32"
_Cdx6500sdlcsNRNumber_Object = MibTableColumn
cdx6500sdlcsNRNumber = _Cdx6500sdlcsNRNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 72),
    _Cdx6500sdlcsNRNumber_Type()
)
cdx6500sdlcsNRNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsNRNumber.setStatus("mandatory")


class _Cdx6500sdlcsNSNumber_Type(Integer32):
    """Custom type cdx6500sdlcsNSNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Cdx6500sdlcsNSNumber_Type.__name__ = "Integer32"
_Cdx6500sdlcsNSNumber_Object = MibTableColumn
cdx6500sdlcsNSNumber = _Cdx6500sdlcsNSNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 4, 1, 73),
    _Cdx6500sdlcsNSNumber_Type()
)
cdx6500sdlcsNSNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsNSNumber.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)
_Cdx6500ContSDLC_ObjectIdentity = ObjectIdentity
cdx6500ContSDLC = _Cdx6500ContSDLC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 5)
)
_Cdx6500ContSDLCStationTable_Object = MibTable
cdx6500ContSDLCStationTable = _Cdx6500ContSDLCStationTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 5, 1)
)
if mibBuilder.loadTexts:
    cdx6500ContSDLCStationTable.setStatus("mandatory")
_Cdx6500ContSDLCStationEntry_Object = MibTableRow
cdx6500ContSDLCStationEntry = _Cdx6500ContSDLCStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 5, 1, 1)
)
cdx6500ContSDLCStationEntry.setIndexNames(
    (0, "SDLC-OPT-MIB", "cdx6500sdlcsContPortNum"),
    (0, "SDLC-OPT-MIB", "cdx6500sdlcsContStationNum"),
)
if mibBuilder.loadTexts:
    cdx6500ContSDLCStationEntry.setStatus("mandatory")


class _Cdx6500sdlcsContPortNum_Type(Integer32):
    """Custom type cdx6500sdlcsContPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500sdlcsContPortNum_Type.__name__ = "Integer32"
_Cdx6500sdlcsContPortNum_Object = MibTableColumn
cdx6500sdlcsContPortNum = _Cdx6500sdlcsContPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 5, 1, 1, 1),
    _Cdx6500sdlcsContPortNum_Type()
)
cdx6500sdlcsContPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdx6500sdlcsContPortNum.setStatus("mandatory")


class _Cdx6500sdlcsContStationNum_Type(Integer32):
    """Custom type cdx6500sdlcsContStationNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Cdx6500sdlcsContStationNum_Type.__name__ = "Integer32"
_Cdx6500sdlcsContStationNum_Object = MibTableColumn
cdx6500sdlcsContStationNum = _Cdx6500sdlcsContStationNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 5, 1, 1, 2),
    _Cdx6500sdlcsContStationNum_Type()
)
cdx6500sdlcsContStationNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdx6500sdlcsContStationNum.setStatus("mandatory")


class _Cdx6500sdlcsContBootStation_Type(Integer32):
    """Custom type cdx6500sdlcsContBootStation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boot", 1),
          ("noboot", 2))
    )


_Cdx6500sdlcsContBootStation_Type.__name__ = "Integer32"
_Cdx6500sdlcsContBootStation_Object = MibTableColumn
cdx6500sdlcsContBootStation = _Cdx6500sdlcsContBootStation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 5, 1, 1, 3),
    _Cdx6500sdlcsContBootStation_Type()
)
cdx6500sdlcsContBootStation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsContBootStation.setStatus("mandatory")


class _Cdx6500sdlcsContDisableStation_Type(Integer32):
    """Custom type cdx6500sdlcsContDisableStation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("nodisable", 2))
    )


_Cdx6500sdlcsContDisableStation_Type.__name__ = "Integer32"
_Cdx6500sdlcsContDisableStation_Object = MibTableColumn
cdx6500sdlcsContDisableStation = _Cdx6500sdlcsContDisableStation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 5, 1, 1, 4),
    _Cdx6500sdlcsContDisableStation_Type()
)
cdx6500sdlcsContDisableStation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsContDisableStation.setStatus("mandatory")


class _Cdx6500sdlcsContEnableStation_Type(Integer32):
    """Custom type cdx6500sdlcsContEnableStation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("noenable", 2))
    )


_Cdx6500sdlcsContEnableStation_Type.__name__ = "Integer32"
_Cdx6500sdlcsContEnableStation_Object = MibTableColumn
cdx6500sdlcsContEnableStation = _Cdx6500sdlcsContEnableStation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 5, 1, 1, 5),
    _Cdx6500sdlcsContEnableStation_Type()
)
cdx6500sdlcsContEnableStation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsContEnableStation.setStatus("mandatory")


class _Cdx6500sdlcsContBusyOutStation_Type(Integer32):
    """Custom type cdx6500sdlcsContBusyOutStation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("busyout", 1),
          ("nobusyout", 2))
    )


_Cdx6500sdlcsContBusyOutStation_Type.__name__ = "Integer32"
_Cdx6500sdlcsContBusyOutStation_Object = MibTableColumn
cdx6500sdlcsContBusyOutStation = _Cdx6500sdlcsContBusyOutStation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 5, 1, 1, 6),
    _Cdx6500sdlcsContBusyOutStation_Type()
)
cdx6500sdlcsContBusyOutStation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsContBusyOutStation.setStatus("deprecated")


class _Cdx6500sdlcsContResetStnStats_Type(Integer32):
    """Custom type cdx6500sdlcsContResetStnStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noreset", 2),
          ("reset", 1))
    )


_Cdx6500sdlcsContResetStnStats_Type.__name__ = "Integer32"
_Cdx6500sdlcsContResetStnStats_Object = MibTableColumn
cdx6500sdlcsContResetStnStats = _Cdx6500sdlcsContResetStnStats_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 5, 1, 1, 7),
    _Cdx6500sdlcsContResetStnStats_Type()
)
cdx6500sdlcsContResetStnStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500sdlcsContResetStnStats.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SDLC-OPT-MIB",
    **{"Counter16": Counter16,
       "DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PCTSDLCPortTable": cdx6500PCTSDLCPortTable,
       "cdx6500PCTSDLCPortEntry": cdx6500PCTSDLCPortEntry,
       "cdx6500sdlcpCfgPortNum": cdx6500sdlcpCfgPortNum,
       "cdx6500sdlcpSubType": cdx6500sdlcpSubType,
       "cdx6500sdlcpTxCoding": cdx6500sdlcpTxCoding,
       "cdx6500sdlcpLineType": cdx6500sdlcpLineType,
       "cdx6500sdlcpTxType": cdx6500sdlcpTxType,
       "cdx6500sdlcpSendSigDelay": cdx6500sdlcpSendSigDelay,
       "cdx6500sdlcpClock": cdx6500sdlcpClock,
       "cdx6500sdlcpClockSpeed": cdx6500sdlcpClockSpeed,
       "cdx6500sdlcpNumControllers": cdx6500sdlcpNumControllers,
       "cdx6500sdlcpPollTimer": cdx6500sdlcpPollTimer,
       "cdx6500sdlcpPollFrequency": cdx6500sdlcpPollFrequency,
       "cdx6500sdlcpTries": cdx6500sdlcpTries,
       "cdx6500sdlcpOptions": cdx6500sdlcpOptions,
       "cdx6500sdlcpPortAddress": cdx6500sdlcpPortAddress,
       "cdx6500sdlcpPortOptions": cdx6500sdlcpPortOptions,
       "cdx6500sdlcpHPADResponseDelay": cdx6500sdlcpHPADResponseDelay,
       "cdx6500sdlcpMaxFrameSize": cdx6500sdlcpMaxFrameSize,
       "cdx6500sdlcpRtsCtsDelay": cdx6500sdlcpRtsCtsDelay,
       "cdx6500sdlcpElectricalInterfaceType": cdx6500sdlcpElectricalInterfaceType,
       "cdx6500sdlcpV24ElectricalInterfaceOption": cdx6500sdlcpV24ElectricalInterfaceOption,
       "cdx6500sdlcpHighSpeedElectricalInterfaceOption": cdx6500sdlcpHighSpeedElectricalInterfaceOption,
       "cdx6500PCTStationProtocolGroup": cdx6500PCTStationProtocolGroup,
       "cdx6500SPCTSDLCStationTable": cdx6500SPCTSDLCStationTable,
       "cdx6500SPCTSDLCStationEntry": cdx6500SPCTSDLCStationEntry,
       "cdx6500sdlcsCfgPortNum": cdx6500sdlcsCfgPortNum,
       "cdx6500sdlcsCfgStationNum": cdx6500sdlcsCfgStationNum,
       "cdx6500sdlcsStationAddr": cdx6500sdlcsStationAddr,
       "cdx6500sdlcsFrameWinSize": cdx6500sdlcsFrameWinSize,
       "cdx6500sdlcsAutocallMnem": cdx6500sdlcsAutocallMnem,
       "cdx6500sdlcsProtocolID": cdx6500sdlcsProtocolID,
       "cdx6500sdlcsCUG": cdx6500sdlcsCUG,
       "cdx6500sdlcsOptions": cdx6500sdlcsOptions,
       "cdx6500sdlcsStationID": cdx6500sdlcsStationID,
       "cdx6500sdlcsBillingFlag": cdx6500sdlcsBillingFlag,
       "cdx6500sdlcsStnSubaddress": cdx6500sdlcsStnSubaddress,
       "cdx6500sdlcsGroupAddress": cdx6500sdlcsGroupAddress,
       "cdx6500sdlcsX25Password": cdx6500sdlcsX25Password,
       "cdx6500sdlcsProtectionLevel": cdx6500sdlcsProtectionLevel,
       "cdx6500sdlcsReconnectTimeout": cdx6500sdlcsReconnectTimeout,
       "cdx6500sdlcsReconnectLimit": cdx6500sdlcsReconnectLimit,
       "cdx6500sdlcsTrafficPriority": cdx6500sdlcsTrafficPriority,
       "cdx6500sdlcsCallTimer": cdx6500sdlcsCallTimer,
       "cdx6500sdlcsIdleTimer": cdx6500sdlcsIdleTimer,
       "cdx6500sdlcsVerConnTimer": cdx6500sdlcsVerConnTimer,
       "cdx6500sdlcsUnsusWaitTimer": cdx6500sdlcsUnsusWaitTimer,
       "cdx6500sdlcsMaxCallAttempts": cdx6500sdlcsMaxCallAttempts,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPSTSDLCPortTable": cdx6500PPSTSDLCPortTable,
       "cdx6500PPSTSDLCPortEntry": cdx6500PPSTSDLCPortEntry,
       "cdx6500sdlcpStatsPortNum": cdx6500sdlcpStatsPortNum,
       "cdx6500sdlcpPortStatus": cdx6500sdlcpPortStatus,
       "cdx6500sdlcpPortSpeed": cdx6500sdlcpPortSpeed,
       "cdx6500sdlcpCharInTotal": cdx6500sdlcpCharInTotal,
       "cdx6500sdlcpCharOutTotal": cdx6500sdlcpCharOutTotal,
       "cdx6500sdlcpCharsInPerSec": cdx6500sdlcpCharsInPerSec,
       "cdx6500sdlcpCharsOutPerSec": cdx6500sdlcpCharsOutPerSec,
       "cdx6500sdlcpFrameInTotal": cdx6500sdlcpFrameInTotal,
       "cdx6500sdlcpFrameOutTotal": cdx6500sdlcpFrameOutTotal,
       "cdx6500sdlcpFramesInPerSec": cdx6500sdlcpFramesInPerSec,
       "cdx6500sdlcpFramesOutPerSec": cdx6500sdlcpFramesOutPerSec,
       "cdx6500sdlcpStateChange": cdx6500sdlcpStateChange,
       "cdx6500sdlcpLinkDowns": cdx6500sdlcpLinkDowns,
       "cdx6500sdlcpUtilizationIn": cdx6500sdlcpUtilizationIn,
       "cdx6500sdlcpUtilizationOut": cdx6500sdlcpUtilizationOut,
       "cdx6500sdlcpOverrunErrors": cdx6500sdlcpOverrunErrors,
       "cdx6500sdlcpUnderrunErrors": cdx6500sdlcpUnderrunErrors,
       "cdx6500sdlcpCRCErrors": cdx6500sdlcpCRCErrors,
       "cdx6500sdlcpPacketsQueued": cdx6500sdlcpPacketsQueued,
       "cdx6500sdlcpRRInFrames": cdx6500sdlcpRRInFrames,
       "cdx6500sdlcpRROutFrames": cdx6500sdlcpRROutFrames,
       "cdx6500sdlcpRNRInFrames": cdx6500sdlcpRNRInFrames,
       "cdx6500sdlcpRNROutFrames": cdx6500sdlcpRNROutFrames,
       "cdx6500sdlcpSNRMInFrames": cdx6500sdlcpSNRMInFrames,
       "cdx6500sdlcpSNRMOutFrames": cdx6500sdlcpSNRMOutFrames,
       "cdx6500sdlcpUAInFrames": cdx6500sdlcpUAInFrames,
       "cdx6500sdlcpUAOutFrames": cdx6500sdlcpUAOutFrames,
       "cdx6500sdlcpDMInFrames": cdx6500sdlcpDMInFrames,
       "cdx6500sdlcpDMOutFrames": cdx6500sdlcpDMOutFrames,
       "cdx6500sdlcpXIDInFrames": cdx6500sdlcpXIDInFrames,
       "cdx6500sdlcpXIDOutFrames": cdx6500sdlcpXIDOutFrames,
       "cdx6500sdlcpREJInFrames": cdx6500sdlcpREJInFrames,
       "cdx6500sdlcpREJOutFrames": cdx6500sdlcpREJOutFrames,
       "cdx6500sdlcpDISCInFrames": cdx6500sdlcpDISCInFrames,
       "cdx6500sdlcpDISCOutFrames": cdx6500sdlcpDISCOutFrames,
       "cdx6500sdlcpRDInFrames": cdx6500sdlcpRDInFrames,
       "cdx6500sdlcpRDOutFrames": cdx6500sdlcpRDOutFrames,
       "cdx6500sdlcpFRMRInFrames": cdx6500sdlcpFRMRInFrames,
       "cdx6500sdlcpFRMROutFrames": cdx6500sdlcpFRMROutFrames,
       "cdx6500sdlcpUPInFrames": cdx6500sdlcpUPInFrames,
       "cdx6500sdlcpUPOutFrames": cdx6500sdlcpUPOutFrames,
       "cdx6500sdlcpTESTInFrames": cdx6500sdlcpTESTInFrames,
       "cdx6500sdlcpTESTOutFrames": cdx6500sdlcpTESTOutFrames,
       "cdx6500sdlcpXIDNullInFrames": cdx6500sdlcpXIDNullInFrames,
       "cdx6500sdlcpXIDNullOutFrames": cdx6500sdlcpXIDNullOutFrames,
       "cdx6500sdlcpXID0InFrames": cdx6500sdlcpXID0InFrames,
       "cdx6500sdlcpXID0OutFrames": cdx6500sdlcpXID0OutFrames,
       "cdx6500sdlcpXID1InFrames": cdx6500sdlcpXID1InFrames,
       "cdx6500sdlcpXID1OutFrames": cdx6500sdlcpXID1OutFrames,
       "cdx6500sdlcpXID3InFrames": cdx6500sdlcpXID3InFrames,
       "cdx6500sdlcpXID3OutFrames": cdx6500sdlcpXID3OutFrames,
       "cdx6500PSTStationProtocolGroup": cdx6500PSTStationProtocolGroup,
       "cdx6500SPSTSDLCStationTable": cdx6500SPSTSDLCStationTable,
       "cdx6500SPSTSDLCStationEntry": cdx6500SPSTSDLCStationEntry,
       "cdx6500sdlcsStatsPortNum": cdx6500sdlcsStatsPortNum,
       "cdx6500sdlcsStatsStationNum": cdx6500sdlcsStatsStationNum,
       "cdx6500sdlcsStatsStationAddr": cdx6500sdlcsStatsStationAddr,
       "cdx6500sdlcsQLLCState": cdx6500sdlcsQLLCState,
       "cdx6500sdlcsCharInTotal": cdx6500sdlcsCharInTotal,
       "cdx6500sdlcsCharOutTotal": cdx6500sdlcsCharOutTotal,
       "cdx6500sdlcsCharsInPerSec": cdx6500sdlcsCharsInPerSec,
       "cdx6500sdlcsCharsOutPerSec": cdx6500sdlcsCharsOutPerSec,
       "cdx6500sdlcsFrameInTotal": cdx6500sdlcsFrameInTotal,
       "cdx6500sdlcsFrameOutTotal": cdx6500sdlcsFrameOutTotal,
       "cdx6500sdlcsFramesInPerSec": cdx6500sdlcsFramesInPerSec,
       "cdx6500sdlcsFramesOutPerSec": cdx6500sdlcsFramesOutPerSec,
       "cdx6500sdlcsQRRInTotal": cdx6500sdlcsQRRInTotal,
       "cdx6500sdlcsQRROutTotal": cdx6500sdlcsQRROutTotal,
       "cdx6500sdlcsUtilizationIn": cdx6500sdlcsUtilizationIn,
       "cdx6500sdlcsUtilizationOut": cdx6500sdlcsUtilizationOut,
       "cdx6500sdlcsPacketsQueued": cdx6500sdlcsPacketsQueued,
       "cdx6500sdlcsRRInFrames": cdx6500sdlcsRRInFrames,
       "cdx6500sdlcsRROutFrames": cdx6500sdlcsRROutFrames,
       "cdx6500sdlcsRNRInFrames": cdx6500sdlcsRNRInFrames,
       "cdx6500sdlcsRNROutFrames": cdx6500sdlcsRNROutFrames,
       "cdx6500sdlcsSNRMInFrames": cdx6500sdlcsSNRMInFrames,
       "cdx6500sdlcsSNRMOutFrames": cdx6500sdlcsSNRMOutFrames,
       "cdx6500sdlcsUAInFrames": cdx6500sdlcsUAInFrames,
       "cdx6500sdlcsUAOutFrames": cdx6500sdlcsUAOutFrames,
       "cdx6500sdlcsDMInFrames": cdx6500sdlcsDMInFrames,
       "cdx6500sdlcsDMOutFrames": cdx6500sdlcsDMOutFrames,
       "cdx6500sdlcsXIDInFrames": cdx6500sdlcsXIDInFrames,
       "cdx6500sdlcsXIDOutFrames": cdx6500sdlcsXIDOutFrames,
       "cdx6500sdlcsREJInFrames": cdx6500sdlcsREJInFrames,
       "cdx6500sdlcsREJOutFrames": cdx6500sdlcsREJOutFrames,
       "cdx6500sdlcsDISCInFrames": cdx6500sdlcsDISCInFrames,
       "cdx6500sdlcsDISCOutFrames": cdx6500sdlcsDISCOutFrames,
       "cdx6500sdlcsRDInFrames": cdx6500sdlcsRDInFrames,
       "cdx6500sdlcsRDOutFrames": cdx6500sdlcsRDOutFrames,
       "cdx6500sdlcsFRMRInFrames": cdx6500sdlcsFRMRInFrames,
       "cdx6500sdlcsFRMROutFrames": cdx6500sdlcsFRMROutFrames,
       "cdx6500sdlcsUPInFrames": cdx6500sdlcsUPInFrames,
       "cdx6500sdlcsUPOutFrames": cdx6500sdlcsUPOutFrames,
       "cdx6500sdlcsTESTInFrames": cdx6500sdlcsTESTInFrames,
       "cdx6500sdlcsTESTOutFrames": cdx6500sdlcsTESTOutFrames,
       "cdx6500sdlcsQSMInFrames": cdx6500sdlcsQSMInFrames,
       "cdx6500sdlcsQSMOutFrames": cdx6500sdlcsQSMOutFrames,
       "cdx6500sdlcsQUAInFrames": cdx6500sdlcsQUAInFrames,
       "cdx6500sdlcsQUAOutFrames": cdx6500sdlcsQUAOutFrames,
       "cdx6500sdlcsQRDInFrames": cdx6500sdlcsQRDInFrames,
       "cdx6500sdlcsQRDOutFrames": cdx6500sdlcsQRDOutFrames,
       "cdx6500sdlcsQFRMRInFrames": cdx6500sdlcsQFRMRInFrames,
       "cdx6500sdlcsQFRMROutFrames": cdx6500sdlcsQFRMROutFrames,
       "cdx6500sdlcsQXIDInFrames": cdx6500sdlcsQXIDInFrames,
       "cdx6500sdlcsQXIDOutFrames": cdx6500sdlcsQXIDOutFrames,
       "cdx6500sdlcsQDCInFrames": cdx6500sdlcsQDCInFrames,
       "cdx6500sdlcsQDCOutFrames": cdx6500sdlcsQDCOutFrames,
       "cdx6500sdlcsQDMInFrames": cdx6500sdlcsQDMInFrames,
       "cdx6500sdlcsQDMOutFrames": cdx6500sdlcsQDMOutFrames,
       "cdx6500sdlcsQTESTInFrames": cdx6500sdlcsQTESTInFrames,
       "cdx6500sdlcsQTESTOutFrames": cdx6500sdlcsQTESTOutFrames,
       "cdx6500sdlcsQSSInFrames": cdx6500sdlcsQSSInFrames,
       "cdx6500sdlcsQSSOutFrames": cdx6500sdlcsQSSOutFrames,
       "cdx6500sdlcsQRSInFrames": cdx6500sdlcsQRSInFrames,
       "cdx6500sdlcsQRSOutFrames": cdx6500sdlcsQRSOutFrames,
       "cdx6500sdlcsXIDNullInFrames": cdx6500sdlcsXIDNullInFrames,
       "cdx6500sdlcsXIDNullOutFrames": cdx6500sdlcsXIDNullOutFrames,
       "cdx6500sdlcsXID0InFrames": cdx6500sdlcsXID0InFrames,
       "cdx6500sdlcsXID0OutFrames": cdx6500sdlcsXID0OutFrames,
       "cdx6500sdlcsXID1InFrames": cdx6500sdlcsXID1InFrames,
       "cdx6500sdlcsXID1OutFrames": cdx6500sdlcsXID1OutFrames,
       "cdx6500sdlcsXID3InFrames": cdx6500sdlcsXID3InFrames,
       "cdx6500sdlcsXID3OutFrames": cdx6500sdlcsXID3OutFrames,
       "cdx6500sdlcsVSNumber": cdx6500sdlcsVSNumber,
       "cdx6500sdlcsVRNumber": cdx6500sdlcsVRNumber,
       "cdx6500sdlcsNRNumber": cdx6500sdlcsNRNumber,
       "cdx6500sdlcsNSNumber": cdx6500sdlcsNSNumber,
       "cdx6500Controls": cdx6500Controls,
       "cdx6500ContSDLC": cdx6500ContSDLC,
       "cdx6500ContSDLCStationTable": cdx6500ContSDLCStationTable,
       "cdx6500ContSDLCStationEntry": cdx6500ContSDLCStationEntry,
       "cdx6500sdlcsContPortNum": cdx6500sdlcsContPortNum,
       "cdx6500sdlcsContStationNum": cdx6500sdlcsContStationNum,
       "cdx6500sdlcsContBootStation": cdx6500sdlcsContBootStation,
       "cdx6500sdlcsContDisableStation": cdx6500sdlcsContDisableStation,
       "cdx6500sdlcsContEnableStation": cdx6500sdlcsContEnableStation,
       "cdx6500sdlcsContBusyOutStation": cdx6500sdlcsContBusyOutStation,
       "cdx6500sdlcsContResetStnStats": cdx6500sdlcsContResetStnStats}
)
