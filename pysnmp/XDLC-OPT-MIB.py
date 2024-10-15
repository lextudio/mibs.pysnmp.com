# SNMP MIB module (XDLC-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XDLC-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:40 2024
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
_Cdx6500PPCTXDLCPortTable_Object = MibTable
cdx6500PPCTXDLCPortTable = _Cdx6500PPCTXDLCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 13)
)
if mibBuilder.loadTexts:
    cdx6500PPCTXDLCPortTable.setStatus("mandatory")
_Cdx6500PPCTXDLCPortEntry_Object = MibTableRow
cdx6500PPCTXDLCPortEntry = _Cdx6500PPCTXDLCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 13, 1)
)
cdx6500PPCTXDLCPortEntry.setIndexNames(
    (0, "XDLC-OPT-MIB", "cdx6500xdlcpCfgPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTXDLCPortEntry.setStatus("mandatory")


class _Cdx6500xdlcpCfgPortNumber_Type(Integer32):
    """Custom type cdx6500xdlcpCfgPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500xdlcpCfgPortNumber_Type.__name__ = "Integer32"
_Cdx6500xdlcpCfgPortNumber_Object = MibTableColumn
cdx6500xdlcpCfgPortNumber = _Cdx6500xdlcpCfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 13, 1, 1),
    _Cdx6500xdlcpCfgPortNumber_Type()
)
cdx6500xdlcpCfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpCfgPortNumber.setStatus("mandatory")


class _Cdx6500xdlcpPortControl_Type(DisplayString):
    """Custom type cdx6500xdlcpPortControl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 4),
    )


_Cdx6500xdlcpPortControl_Type.__name__ = "DisplayString"
_Cdx6500xdlcpPortControl_Object = MibTableColumn
cdx6500xdlcpPortControl = _Cdx6500xdlcpPortControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 13, 1, 2),
    _Cdx6500xdlcpPortControl_Type()
)
cdx6500xdlcpPortControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpPortControl.setStatus("mandatory")


class _Cdx6500xdlcpTxCoding_Type(Integer32):
    """Custom type cdx6500xdlcpTxCoding based on Integer32"""
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


_Cdx6500xdlcpTxCoding_Type.__name__ = "Integer32"
_Cdx6500xdlcpTxCoding_Object = MibTableColumn
cdx6500xdlcpTxCoding = _Cdx6500xdlcpTxCoding_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 13, 1, 3),
    _Cdx6500xdlcpTxCoding_Type()
)
cdx6500xdlcpTxCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpTxCoding.setStatus("mandatory")


class _Cdx6500xdlcpLineType_Type(Integer32):
    """Custom type cdx6500xdlcpLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("fdx", 1)
    )


_Cdx6500xdlcpLineType_Type.__name__ = "Integer32"
_Cdx6500xdlcpLineType_Object = MibTableColumn
cdx6500xdlcpLineType = _Cdx6500xdlcpLineType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 13, 1, 4),
    _Cdx6500xdlcpLineType_Type()
)
cdx6500xdlcpLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpLineType.setStatus("mandatory")


class _Cdx6500xdlcpTxType_Type(Integer32):
    """Custom type cdx6500xdlcpTxType based on Integer32"""
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


_Cdx6500xdlcpTxType_Type.__name__ = "Integer32"
_Cdx6500xdlcpTxType_Object = MibTableColumn
cdx6500xdlcpTxType = _Cdx6500xdlcpTxType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 13, 1, 5),
    _Cdx6500xdlcpTxType_Type()
)
cdx6500xdlcpTxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpTxType.setStatus("mandatory")


class _Cdx6500xdlcpClockSource_Type(Integer32):
    """Custom type cdx6500xdlcpClockSource based on Integer32"""
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


_Cdx6500xdlcpClockSource_Type.__name__ = "Integer32"
_Cdx6500xdlcpClockSource_Object = MibTableColumn
cdx6500xdlcpClockSource = _Cdx6500xdlcpClockSource_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 13, 1, 6),
    _Cdx6500xdlcpClockSource_Type()
)
cdx6500xdlcpClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpClockSource.setStatus("mandatory")


class _Cdx6500xdlcpClockSpeed_Type(Integer32):
    """Custom type cdx6500xdlcpClockSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 80000),
    )


_Cdx6500xdlcpClockSpeed_Type.__name__ = "Integer32"
_Cdx6500xdlcpClockSpeed_Object = MibTableColumn
cdx6500xdlcpClockSpeed = _Cdx6500xdlcpClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 13, 1, 7),
    _Cdx6500xdlcpClockSpeed_Type()
)
cdx6500xdlcpClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpClockSpeed.setStatus("mandatory")


class _Cdx6500xdlcpStationCnt_Type(Integer32):
    """Custom type cdx6500xdlcpStationCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Cdx6500xdlcpStationCnt_Type.__name__ = "Integer32"
_Cdx6500xdlcpStationCnt_Object = MibTableColumn
cdx6500xdlcpStationCnt = _Cdx6500xdlcpStationCnt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 13, 1, 8),
    _Cdx6500xdlcpStationCnt_Type()
)
cdx6500xdlcpStationCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpStationCnt.setStatus("mandatory")


class _Cdx6500xdlcpPollTimer_Type(Integer32):
    """Custom type cdx6500xdlcpPollTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500xdlcpPollTimer_Type.__name__ = "Integer32"
_Cdx6500xdlcpPollTimer_Object = MibTableColumn
cdx6500xdlcpPollTimer = _Cdx6500xdlcpPollTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 13, 1, 9),
    _Cdx6500xdlcpPollTimer_Type()
)
cdx6500xdlcpPollTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpPollTimer.setStatus("mandatory")


class _Cdx6500xdlcpPollPeriod_Type(Integer32):
    """Custom type cdx6500xdlcpPollPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 250),
    )


_Cdx6500xdlcpPollPeriod_Type.__name__ = "Integer32"
_Cdx6500xdlcpPollPeriod_Object = MibTableColumn
cdx6500xdlcpPollPeriod = _Cdx6500xdlcpPollPeriod_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 13, 1, 10),
    _Cdx6500xdlcpPollPeriod_Type()
)
cdx6500xdlcpPollPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpPollPeriod.setStatus("mandatory")


class _Cdx6500xdlcpTries_Type(Integer32):
    """Custom type cdx6500xdlcpTries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Cdx6500xdlcpTries_Type.__name__ = "Integer32"
_Cdx6500xdlcpTries_Object = MibTableColumn
cdx6500xdlcpTries = _Cdx6500xdlcpTries_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 13, 1, 11),
    _Cdx6500xdlcpTries_Type()
)
cdx6500xdlcpTries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpTries.setStatus("mandatory")


class _Cdx6500xdlcpPortOptions_Type(DisplayString):
    """Custom type cdx6500xdlcpPortOptions based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_Cdx6500xdlcpPortOptions_Type.__name__ = "DisplayString"
_Cdx6500xdlcpPortOptions_Object = MibTableColumn
cdx6500xdlcpPortOptions = _Cdx6500xdlcpPortOptions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 13, 1, 12),
    _Cdx6500xdlcpPortOptions_Type()
)
cdx6500xdlcpPortOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpPortOptions.setStatus("mandatory")


class _Cdx6500xdlcpPortAddress_Type(DisplayString):
    """Custom type cdx6500xdlcpPortAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500xdlcpPortAddress_Type.__name__ = "DisplayString"
_Cdx6500xdlcpPortAddress_Object = MibTableColumn
cdx6500xdlcpPortAddress = _Cdx6500xdlcpPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 13, 1, 13),
    _Cdx6500xdlcpPortAddress_Type()
)
cdx6500xdlcpPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpPortAddress.setStatus("mandatory")


class _Cdx6500xdlcpRestartTimer_Type(Integer32):
    """Custom type cdx6500xdlcpRestartTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Cdx6500xdlcpRestartTimer_Type.__name__ = "Integer32"
_Cdx6500xdlcpRestartTimer_Object = MibTableColumn
cdx6500xdlcpRestartTimer = _Cdx6500xdlcpRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 13, 1, 14),
    _Cdx6500xdlcpRestartTimer_Type()
)
cdx6500xdlcpRestartTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpRestartTimer.setStatus("mandatory")


class _Cdx6500xdlcpResetTimer_Type(Integer32):
    """Custom type cdx6500xdlcpResetTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Cdx6500xdlcpResetTimer_Type.__name__ = "Integer32"
_Cdx6500xdlcpResetTimer_Object = MibTableColumn
cdx6500xdlcpResetTimer = _Cdx6500xdlcpResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 13, 1, 15),
    _Cdx6500xdlcpResetTimer_Type()
)
cdx6500xdlcpResetTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpResetTimer.setStatus("mandatory")


class _Cdx6500xdlcpCallTimer_Type(Integer32):
    """Custom type cdx6500xdlcpCallTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Cdx6500xdlcpCallTimer_Type.__name__ = "Integer32"
_Cdx6500xdlcpCallTimer_Object = MibTableColumn
cdx6500xdlcpCallTimer = _Cdx6500xdlcpCallTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 13, 1, 16),
    _Cdx6500xdlcpCallTimer_Type()
)
cdx6500xdlcpCallTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpCallTimer.setStatus("mandatory")


class _Cdx6500xdlcpClearTimer_Type(Integer32):
    """Custom type cdx6500xdlcpClearTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Cdx6500xdlcpClearTimer_Type.__name__ = "Integer32"
_Cdx6500xdlcpClearTimer_Object = MibTableColumn
cdx6500xdlcpClearTimer = _Cdx6500xdlcpClearTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 13, 1, 17),
    _Cdx6500xdlcpClearTimer_Type()
)
cdx6500xdlcpClearTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpClearTimer.setStatus("mandatory")


class _Cdx6500xdlcpMaxFrameSize_Type(Integer32):
    """Custom type cdx6500xdlcpMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_Cdx6500xdlcpMaxFrameSize_Type.__name__ = "Integer32"
_Cdx6500xdlcpMaxFrameSize_Object = MibTableColumn
cdx6500xdlcpMaxFrameSize = _Cdx6500xdlcpMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 13, 1, 18),
    _Cdx6500xdlcpMaxFrameSize_Type()
)
cdx6500xdlcpMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpMaxFrameSize.setStatus("mandatory")


class _Cdx6500xdlcpElectricalInterfaceType_Type(Integer32):
    """Custom type cdx6500xdlcpElectricalInterfaceType based on Integer32"""
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


_Cdx6500xdlcpElectricalInterfaceType_Type.__name__ = "Integer32"
_Cdx6500xdlcpElectricalInterfaceType_Object = MibTableColumn
cdx6500xdlcpElectricalInterfaceType = _Cdx6500xdlcpElectricalInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 13, 1, 19),
    _Cdx6500xdlcpElectricalInterfaceType_Type()
)
cdx6500xdlcpElectricalInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpElectricalInterfaceType.setStatus("mandatory")


class _Cdx6500xdlcpV24ElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500xdlcpV24ElectricalInterfaceOption based on Integer32"""
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


_Cdx6500xdlcpV24ElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500xdlcpV24ElectricalInterfaceOption_Object = MibTableColumn
cdx6500xdlcpV24ElectricalInterfaceOption = _Cdx6500xdlcpV24ElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 13, 1, 20),
    _Cdx6500xdlcpV24ElectricalInterfaceOption_Type()
)
cdx6500xdlcpV24ElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpV24ElectricalInterfaceOption.setStatus("mandatory")


class _Cdx6500xdlcpHighSpeedElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500xdlcpHighSpeedElectricalInterfaceOption based on Integer32"""
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


_Cdx6500xdlcpHighSpeedElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500xdlcpHighSpeedElectricalInterfaceOption_Object = MibTableColumn
cdx6500xdlcpHighSpeedElectricalInterfaceOption = _Cdx6500xdlcpHighSpeedElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 13, 1, 21),
    _Cdx6500xdlcpHighSpeedElectricalInterfaceOption_Type()
)
cdx6500xdlcpHighSpeedElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpHighSpeedElectricalInterfaceOption.setStatus("mandatory")
_Cdx6500PCTStationProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTStationProtocolGroup = _Cdx6500PCTStationProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3)
)
_Cdx6500SPCTXDLCStationTable_ObjectIdentity = ObjectIdentity
cdx6500SPCTXDLCStationTable = _Cdx6500SPCTXDLCStationTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5)
)
_Cdx6500SPCTXDLCStnTable_Object = MibTable
cdx6500SPCTXDLCStnTable = _Cdx6500SPCTXDLCStnTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    cdx6500SPCTXDLCStnTable.setStatus("mandatory")
_Cdx6500SPCTXDLCStnEntry_Object = MibTableRow
cdx6500SPCTXDLCStnEntry = _Cdx6500SPCTXDLCStnEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 1, 1)
)
cdx6500SPCTXDLCStnEntry.setIndexNames(
    (0, "XDLC-OPT-MIB", "cdx6500xdlcsCfgPortNumber"),
    (0, "XDLC-OPT-MIB", "cdx6500xdlcsCfgStationNumber"),
)
if mibBuilder.loadTexts:
    cdx6500SPCTXDLCStnEntry.setStatus("mandatory")


class _Cdx6500xdlcsCfgPortNumber_Type(Integer32):
    """Custom type cdx6500xdlcsCfgPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500xdlcsCfgPortNumber_Type.__name__ = "Integer32"
_Cdx6500xdlcsCfgPortNumber_Object = MibTableColumn
cdx6500xdlcsCfgPortNumber = _Cdx6500xdlcsCfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 1, 1, 1),
    _Cdx6500xdlcsCfgPortNumber_Type()
)
cdx6500xdlcsCfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsCfgPortNumber.setStatus("mandatory")


class _Cdx6500xdlcsCfgStationNumber_Type(Integer32):
    """Custom type cdx6500xdlcsCfgStationNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Cdx6500xdlcsCfgStationNumber_Type.__name__ = "Integer32"
_Cdx6500xdlcsCfgStationNumber_Object = MibTableColumn
cdx6500xdlcsCfgStationNumber = _Cdx6500xdlcsCfgStationNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 1, 1, 2),
    _Cdx6500xdlcsCfgStationNumber_Type()
)
cdx6500xdlcsCfgStationNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsCfgStationNumber.setStatus("mandatory")


class _Cdx6500xdlcsStationType_Type(Integer32):
    """Custom type cdx6500xdlcsStationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("mx25", 1),
          ("newvalSdlc", 50),
          ("sdlc", 0))
    )


_Cdx6500xdlcsStationType_Type.__name__ = "Integer32"
_Cdx6500xdlcsStationType_Object = MibTableColumn
cdx6500xdlcsStationType = _Cdx6500xdlcsStationType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 1, 1, 3),
    _Cdx6500xdlcsStationType_Type()
)
cdx6500xdlcsStationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsStationType.setStatus("mandatory")
_Cdx6500SPCTXDLCSDLCStnTable_Object = MibTable
cdx6500SPCTXDLCSDLCStnTable = _Cdx6500SPCTXDLCSDLCStnTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 2)
)
if mibBuilder.loadTexts:
    cdx6500SPCTXDLCSDLCStnTable.setStatus("mandatory")
_Cdx6500SPCTXDLCSDLCStnEntry_Object = MibTableRow
cdx6500SPCTXDLCSDLCStnEntry = _Cdx6500SPCTXDLCSDLCStnEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 2, 1)
)
cdx6500SPCTXDLCSDLCStnEntry.setIndexNames(
    (0, "XDLC-OPT-MIB", "cdx6500xdlcsdlcCfgPortNum"),
    (0, "XDLC-OPT-MIB", "cdx6500xdlcsdlcCfgStationNum"),
)
if mibBuilder.loadTexts:
    cdx6500SPCTXDLCSDLCStnEntry.setStatus("mandatory")


class _Cdx6500xdlcsdlcCfgPortNum_Type(Integer32):
    """Custom type cdx6500xdlcsdlcCfgPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500xdlcsdlcCfgPortNum_Type.__name__ = "Integer32"
_Cdx6500xdlcsdlcCfgPortNum_Object = MibTableColumn
cdx6500xdlcsdlcCfgPortNum = _Cdx6500xdlcsdlcCfgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 2, 1, 1),
    _Cdx6500xdlcsdlcCfgPortNum_Type()
)
cdx6500xdlcsdlcCfgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcCfgPortNum.setStatus("mandatory")


class _Cdx6500xdlcsdlcCfgStationNum_Type(Integer32):
    """Custom type cdx6500xdlcsdlcCfgStationNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Cdx6500xdlcsdlcCfgStationNum_Type.__name__ = "Integer32"
_Cdx6500xdlcsdlcCfgStationNum_Object = MibTableColumn
cdx6500xdlcsdlcCfgStationNum = _Cdx6500xdlcsdlcCfgStationNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 2, 1, 2),
    _Cdx6500xdlcsdlcCfgStationNum_Type()
)
cdx6500xdlcsdlcCfgStationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcCfgStationNum.setStatus("mandatory")


class _Cdx6500xdlcsdlcStationAddress_Type(DisplayString):
    """Custom type cdx6500xdlcsdlcStationAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_Cdx6500xdlcsdlcStationAddress_Type.__name__ = "DisplayString"
_Cdx6500xdlcsdlcStationAddress_Object = MibTableColumn
cdx6500xdlcsdlcStationAddress = _Cdx6500xdlcsdlcStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 2, 1, 3),
    _Cdx6500xdlcsdlcStationAddress_Type()
)
cdx6500xdlcsdlcStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcStationAddress.setStatus("mandatory")


class _Cdx6500xdlcsdlcFrameWinSize_Type(Integer32):
    """Custom type cdx6500xdlcsdlcFrameWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Cdx6500xdlcsdlcFrameWinSize_Type.__name__ = "Integer32"
_Cdx6500xdlcsdlcFrameWinSize_Object = MibTableColumn
cdx6500xdlcsdlcFrameWinSize = _Cdx6500xdlcsdlcFrameWinSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 2, 1, 4),
    _Cdx6500xdlcsdlcFrameWinSize_Type()
)
cdx6500xdlcsdlcFrameWinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcFrameWinSize.setStatus("mandatory")


class _Cdx6500xdlcsdlcAutocallMnem_Type(DisplayString):
    """Custom type cdx6500xdlcsdlcAutocallMnem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Cdx6500xdlcsdlcAutocallMnem_Type.__name__ = "DisplayString"
_Cdx6500xdlcsdlcAutocallMnem_Object = MibTableColumn
cdx6500xdlcsdlcAutocallMnem = _Cdx6500xdlcsdlcAutocallMnem_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 2, 1, 5),
    _Cdx6500xdlcsdlcAutocallMnem_Type()
)
cdx6500xdlcsdlcAutocallMnem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcAutocallMnem.setStatus("mandatory")


class _Cdx6500xdlcsdlcProtocolID_Type(DisplayString):
    """Custom type cdx6500xdlcsdlcProtocolID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Cdx6500xdlcsdlcProtocolID_Type.__name__ = "DisplayString"
_Cdx6500xdlcsdlcProtocolID_Object = MibTableColumn
cdx6500xdlcsdlcProtocolID = _Cdx6500xdlcsdlcProtocolID_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 2, 1, 6),
    _Cdx6500xdlcsdlcProtocolID_Type()
)
cdx6500xdlcsdlcProtocolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcProtocolID.setStatus("mandatory")


class _Cdx6500xdlcsdlcCUG_Type(DisplayString):
    """Custom type cdx6500xdlcsdlcCUG based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_Cdx6500xdlcsdlcCUG_Type.__name__ = "DisplayString"
_Cdx6500xdlcsdlcCUG_Object = MibTableColumn
cdx6500xdlcsdlcCUG = _Cdx6500xdlcsdlcCUG_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 2, 1, 7),
    _Cdx6500xdlcsdlcCUG_Type()
)
cdx6500xdlcsdlcCUG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcCUG.setStatus("mandatory")


class _Cdx6500xdlcsdlcOptions_Type(DisplayString):
    """Custom type cdx6500xdlcsdlcOptions based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 24),
    )


_Cdx6500xdlcsdlcOptions_Type.__name__ = "DisplayString"
_Cdx6500xdlcsdlcOptions_Object = MibTableColumn
cdx6500xdlcsdlcOptions = _Cdx6500xdlcsdlcOptions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 2, 1, 8),
    _Cdx6500xdlcsdlcOptions_Type()
)
cdx6500xdlcsdlcOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcOptions.setStatus("mandatory")


class _Cdx6500xdlcsdlcXID_Type(DisplayString):
    """Custom type cdx6500xdlcsdlcXID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500xdlcsdlcXID_Type.__name__ = "DisplayString"
_Cdx6500xdlcsdlcXID_Object = MibTableColumn
cdx6500xdlcsdlcXID = _Cdx6500xdlcsdlcXID_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 2, 1, 9),
    _Cdx6500xdlcsdlcXID_Type()
)
cdx6500xdlcsdlcXID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcXID.setStatus("mandatory")


class _Cdx6500xdlcsdlcStnSubaddress_Type(DisplayString):
    """Custom type cdx6500xdlcsdlcStnSubaddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_Cdx6500xdlcsdlcStnSubaddress_Type.__name__ = "DisplayString"
_Cdx6500xdlcsdlcStnSubaddress_Object = MibTableColumn
cdx6500xdlcsdlcStnSubaddress = _Cdx6500xdlcsdlcStnSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 2, 1, 10),
    _Cdx6500xdlcsdlcStnSubaddress_Type()
)
cdx6500xdlcsdlcStnSubaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcStnSubaddress.setStatus("mandatory")


class _Cdx6500xdlcsdlcBillingRecords_Type(Integer32):
    """Custom type cdx6500xdlcsdlcBillingRecords based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvalOff", 50),
          ("off", 0),
          ("on", 1))
    )


_Cdx6500xdlcsdlcBillingRecords_Type.__name__ = "Integer32"
_Cdx6500xdlcsdlcBillingRecords_Object = MibTableColumn
cdx6500xdlcsdlcBillingRecords = _Cdx6500xdlcsdlcBillingRecords_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 2, 1, 11),
    _Cdx6500xdlcsdlcBillingRecords_Type()
)
cdx6500xdlcsdlcBillingRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcBillingRecords.setStatus("mandatory")


class _Cdx6500xdlcsdlcProtectionLevel_Type(Integer32):
    """Custom type cdx6500xdlcsdlcProtectionLevel based on Integer32"""
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
        *(("cpOnly", 1),
          ("fullDcp", 2),
          ("newvalNone", 50),
          ("none", 0))
    )


_Cdx6500xdlcsdlcProtectionLevel_Type.__name__ = "Integer32"
_Cdx6500xdlcsdlcProtectionLevel_Object = MibTableColumn
cdx6500xdlcsdlcProtectionLevel = _Cdx6500xdlcsdlcProtectionLevel_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 2, 1, 12),
    _Cdx6500xdlcsdlcProtectionLevel_Type()
)
cdx6500xdlcsdlcProtectionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcProtectionLevel.setStatus("mandatory")


class _Cdx6500xdlcsdlcReconnectTimeout_Type(Integer32):
    """Custom type cdx6500xdlcsdlcReconnectTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Cdx6500xdlcsdlcReconnectTimeout_Type.__name__ = "Integer32"
_Cdx6500xdlcsdlcReconnectTimeout_Object = MibTableColumn
cdx6500xdlcsdlcReconnectTimeout = _Cdx6500xdlcsdlcReconnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 2, 1, 13),
    _Cdx6500xdlcsdlcReconnectTimeout_Type()
)
cdx6500xdlcsdlcReconnectTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcReconnectTimeout.setStatus("mandatory")


class _Cdx6500xdlcsdlcReconnectLimit_Type(Integer32):
    """Custom type cdx6500xdlcsdlcReconnectLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500xdlcsdlcReconnectLimit_Type.__name__ = "Integer32"
_Cdx6500xdlcsdlcReconnectLimit_Object = MibTableColumn
cdx6500xdlcsdlcReconnectLimit = _Cdx6500xdlcsdlcReconnectLimit_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 2, 1, 14),
    _Cdx6500xdlcsdlcReconnectLimit_Type()
)
cdx6500xdlcsdlcReconnectLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcReconnectLimit.setStatus("mandatory")


class _Cdx6500xdlcsdlcCallTimer_Type(Integer32):
    """Custom type cdx6500xdlcsdlcCallTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_Cdx6500xdlcsdlcCallTimer_Type.__name__ = "Integer32"
_Cdx6500xdlcsdlcCallTimer_Object = MibTableColumn
cdx6500xdlcsdlcCallTimer = _Cdx6500xdlcsdlcCallTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 2, 1, 15),
    _Cdx6500xdlcsdlcCallTimer_Type()
)
cdx6500xdlcsdlcCallTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcCallTimer.setStatus("mandatory")


class _Cdx6500xdlcsdlcIdleTimer_Type(Integer32):
    """Custom type cdx6500xdlcsdlcIdleTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Cdx6500xdlcsdlcIdleTimer_Type.__name__ = "Integer32"
_Cdx6500xdlcsdlcIdleTimer_Object = MibTableColumn
cdx6500xdlcsdlcIdleTimer = _Cdx6500xdlcsdlcIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 2, 1, 16),
    _Cdx6500xdlcsdlcIdleTimer_Type()
)
cdx6500xdlcsdlcIdleTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcIdleTimer.setStatus("mandatory")


class _Cdx6500xdlcsdlcVerConnTimer_Type(Integer32):
    """Custom type cdx6500xdlcsdlcVerConnTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Cdx6500xdlcsdlcVerConnTimer_Type.__name__ = "Integer32"
_Cdx6500xdlcsdlcVerConnTimer_Object = MibTableColumn
cdx6500xdlcsdlcVerConnTimer = _Cdx6500xdlcsdlcVerConnTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 2, 1, 17),
    _Cdx6500xdlcsdlcVerConnTimer_Type()
)
cdx6500xdlcsdlcVerConnTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcVerConnTimer.setStatus("mandatory")


class _Cdx6500xdlcsdlcUnsusWaitTimer_Type(Integer32):
    """Custom type cdx6500xdlcsdlcUnsusWaitTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Cdx6500xdlcsdlcUnsusWaitTimer_Type.__name__ = "Integer32"
_Cdx6500xdlcsdlcUnsusWaitTimer_Object = MibTableColumn
cdx6500xdlcsdlcUnsusWaitTimer = _Cdx6500xdlcsdlcUnsusWaitTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 2, 1, 18),
    _Cdx6500xdlcsdlcUnsusWaitTimer_Type()
)
cdx6500xdlcsdlcUnsusWaitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcUnsusWaitTimer.setStatus("mandatory")
_Cdx6500SPCTXDLCMX25StnTable_Object = MibTable
cdx6500SPCTXDLCMX25StnTable = _Cdx6500SPCTXDLCMX25StnTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 3)
)
if mibBuilder.loadTexts:
    cdx6500SPCTXDLCMX25StnTable.setStatus("mandatory")
_Cdx6500SPCTXDLCMX25StnEntry_Object = MibTableRow
cdx6500SPCTXDLCMX25StnEntry = _Cdx6500SPCTXDLCMX25StnEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 3, 1)
)
cdx6500SPCTXDLCMX25StnEntry.setIndexNames(
    (0, "XDLC-OPT-MIB", "cdx6500xdlcmx25CfgPortNum"),
    (0, "XDLC-OPT-MIB", "cdx6500xdlcmx25CfgStationNum"),
)
if mibBuilder.loadTexts:
    cdx6500SPCTXDLCMX25StnEntry.setStatus("mandatory")


class _Cdx6500xdlcmx25CfgPortNum_Type(Integer32):
    """Custom type cdx6500xdlcmx25CfgPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500xdlcmx25CfgPortNum_Type.__name__ = "Integer32"
_Cdx6500xdlcmx25CfgPortNum_Object = MibTableColumn
cdx6500xdlcmx25CfgPortNum = _Cdx6500xdlcmx25CfgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 3, 1, 1),
    _Cdx6500xdlcmx25CfgPortNum_Type()
)
cdx6500xdlcmx25CfgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25CfgPortNum.setStatus("mandatory")


class _Cdx6500xdlcmx25CfgStationNum_Type(Integer32):
    """Custom type cdx6500xdlcmx25CfgStationNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Cdx6500xdlcmx25CfgStationNum_Type.__name__ = "Integer32"
_Cdx6500xdlcmx25CfgStationNum_Object = MibTableColumn
cdx6500xdlcmx25CfgStationNum = _Cdx6500xdlcmx25CfgStationNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 3, 1, 2),
    _Cdx6500xdlcmx25CfgStationNum_Type()
)
cdx6500xdlcmx25CfgStationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25CfgStationNum.setStatus("mandatory")


class _Cdx6500xdlcmx25StationAddress_Type(DisplayString):
    """Custom type cdx6500xdlcmx25StationAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_Cdx6500xdlcmx25StationAddress_Type.__name__ = "DisplayString"
_Cdx6500xdlcmx25StationAddress_Object = MibTableColumn
cdx6500xdlcmx25StationAddress = _Cdx6500xdlcmx25StationAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 3, 1, 3),
    _Cdx6500xdlcmx25StationAddress_Type()
)
cdx6500xdlcmx25StationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25StationAddress.setStatus("mandatory")


class _Cdx6500xdlcmx25PVCChannels_Type(Integer32):
    """Custom type cdx6500xdlcmx25PVCChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Cdx6500xdlcmx25PVCChannels_Type.__name__ = "Integer32"
_Cdx6500xdlcmx25PVCChannels_Object = MibTableColumn
cdx6500xdlcmx25PVCChannels = _Cdx6500xdlcmx25PVCChannels_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 3, 1, 4),
    _Cdx6500xdlcmx25PVCChannels_Type()
)
cdx6500xdlcmx25PVCChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25PVCChannels.setStatus("mandatory")


class _Cdx6500xdlcmx25StartingPVC_Type(Integer32):
    """Custom type cdx6500xdlcmx25StartingPVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500xdlcmx25StartingPVC_Type.__name__ = "Integer32"
_Cdx6500xdlcmx25StartingPVC_Object = MibTableColumn
cdx6500xdlcmx25StartingPVC = _Cdx6500xdlcmx25StartingPVC_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 3, 1, 5),
    _Cdx6500xdlcmx25StartingPVC_Type()
)
cdx6500xdlcmx25StartingPVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25StartingPVC.setStatus("mandatory")


class _Cdx6500xdlcmx25SVCChannels_Type(Integer32):
    """Custom type cdx6500xdlcmx25SVCChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500xdlcmx25SVCChannels_Type.__name__ = "Integer32"
_Cdx6500xdlcmx25SVCChannels_Object = MibTableColumn
cdx6500xdlcmx25SVCChannels = _Cdx6500xdlcmx25SVCChannels_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 3, 1, 6),
    _Cdx6500xdlcmx25SVCChannels_Type()
)
cdx6500xdlcmx25SVCChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25SVCChannels.setStatus("mandatory")


class _Cdx6500xdlcmx25StartingSVC_Type(Integer32):
    """Custom type cdx6500xdlcmx25StartingSVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500xdlcmx25StartingSVC_Type.__name__ = "Integer32"
_Cdx6500xdlcmx25StartingSVC_Object = MibTableColumn
cdx6500xdlcmx25StartingSVC = _Cdx6500xdlcmx25StartingSVC_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 3, 1, 7),
    _Cdx6500xdlcmx25StartingSVC_Type()
)
cdx6500xdlcmx25StartingSVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25StartingSVC.setStatus("mandatory")


class _Cdx6500xdlcmx25FrameWinSize_Type(Integer32):
    """Custom type cdx6500xdlcmx25FrameWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Cdx6500xdlcmx25FrameWinSize_Type.__name__ = "Integer32"
_Cdx6500xdlcmx25FrameWinSize_Object = MibTableColumn
cdx6500xdlcmx25FrameWinSize = _Cdx6500xdlcmx25FrameWinSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 3, 1, 8),
    _Cdx6500xdlcmx25FrameWinSize_Type()
)
cdx6500xdlcmx25FrameWinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25FrameWinSize.setStatus("mandatory")


class _Cdx6500xdlcmx25PacketWinSize_Type(Integer32):
    """Custom type cdx6500xdlcmx25PacketWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Cdx6500xdlcmx25PacketWinSize_Type.__name__ = "Integer32"
_Cdx6500xdlcmx25PacketWinSize_Object = MibTableColumn
cdx6500xdlcmx25PacketWinSize = _Cdx6500xdlcmx25PacketWinSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 3, 1, 9),
    _Cdx6500xdlcmx25PacketWinSize_Type()
)
cdx6500xdlcmx25PacketWinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25PacketWinSize.setStatus("mandatory")


class _Cdx6500xdlcmx25Options_Type(DisplayString):
    """Custom type cdx6500xdlcmx25Options based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_Cdx6500xdlcmx25Options_Type.__name__ = "DisplayString"
_Cdx6500xdlcmx25Options_Object = MibTableColumn
cdx6500xdlcmx25Options = _Cdx6500xdlcmx25Options_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 3, 1, 10),
    _Cdx6500xdlcmx25Options_Type()
)
cdx6500xdlcmx25Options.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25Options.setStatus("mandatory")


class _Cdx6500xdlcmx25RCDestination_Type(DisplayString):
    """Custom type cdx6500xdlcmx25RCDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cdx6500xdlcmx25RCDestination_Type.__name__ = "DisplayString"
_Cdx6500xdlcmx25RCDestination_Object = MibTableColumn
cdx6500xdlcmx25RCDestination = _Cdx6500xdlcmx25RCDestination_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 3, 1, 11),
    _Cdx6500xdlcmx25RCDestination_Type()
)
cdx6500xdlcmx25RCDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25RCDestination.setStatus("mandatory")


class _Cdx6500xdlcmx25CUG_Type(DisplayString):
    """Custom type cdx6500xdlcmx25CUG based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_Cdx6500xdlcmx25CUG_Type.__name__ = "DisplayString"
_Cdx6500xdlcmx25CUG_Object = MibTableColumn
cdx6500xdlcmx25CUG = _Cdx6500xdlcmx25CUG_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 3, 1, 12),
    _Cdx6500xdlcmx25CUG_Type()
)
cdx6500xdlcmx25CUG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25CUG.setStatus("mandatory")


class _Cdx6500xdlcmx25BillingRecords_Type(Integer32):
    """Custom type cdx6500xdlcmx25BillingRecords based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvalOff", 50),
          ("off", 0),
          ("on", 1))
    )


_Cdx6500xdlcmx25BillingRecords_Type.__name__ = "Integer32"
_Cdx6500xdlcmx25BillingRecords_Object = MibTableColumn
cdx6500xdlcmx25BillingRecords = _Cdx6500xdlcmx25BillingRecords_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 3, 1, 13),
    _Cdx6500xdlcmx25BillingRecords_Type()
)
cdx6500xdlcmx25BillingRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25BillingRecords.setStatus("mandatory")


class _Cdx6500xdlcmx25UpperQueue_Type(Integer32):
    """Custom type cdx6500xdlcmx25UpperQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 15),
    )


_Cdx6500xdlcmx25UpperQueue_Type.__name__ = "Integer32"
_Cdx6500xdlcmx25UpperQueue_Object = MibTableColumn
cdx6500xdlcmx25UpperQueue = _Cdx6500xdlcmx25UpperQueue_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 3, 1, 14),
    _Cdx6500xdlcmx25UpperQueue_Type()
)
cdx6500xdlcmx25UpperQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25UpperQueue.setStatus("mandatory")


class _Cdx6500xdlcmx25LowerQueue_Type(Integer32):
    """Custom type cdx6500xdlcmx25LowerQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Cdx6500xdlcmx25LowerQueue_Type.__name__ = "Integer32"
_Cdx6500xdlcmx25LowerQueue_Object = MibTableColumn
cdx6500xdlcmx25LowerQueue = _Cdx6500xdlcmx25LowerQueue_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 5, 3, 1, 15),
    _Cdx6500xdlcmx25LowerQueue_Type()
)
cdx6500xdlcmx25LowerQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25LowerQueue.setStatus("mandatory")
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
_Cdx6500PPSTXDLCPortTable_Object = MibTable
cdx6500PPSTXDLCPortTable = _Cdx6500PPSTXDLCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13)
)
if mibBuilder.loadTexts:
    cdx6500PPSTXDLCPortTable.setStatus("mandatory")
_Cdx6500PPSTXDLCPortEntry_Object = MibTableRow
cdx6500PPSTXDLCPortEntry = _Cdx6500PPSTXDLCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1)
)
cdx6500PPSTXDLCPortEntry.setIndexNames(
    (0, "XDLC-OPT-MIB", "cdx6500xdlcpStatsPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTXDLCPortEntry.setStatus("mandatory")


class _Cdx6500xdlcpStatsPortNumber_Type(Integer32):
    """Custom type cdx6500xdlcpStatsPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500xdlcpStatsPortNumber_Type.__name__ = "Integer32"
_Cdx6500xdlcpStatsPortNumber_Object = MibTableColumn
cdx6500xdlcpStatsPortNumber = _Cdx6500xdlcpStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 1),
    _Cdx6500xdlcpStatsPortNumber_Type()
)
cdx6500xdlcpStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpStatsPortNumber.setStatus("mandatory")


class _Cdx6500xdlcpPortStatus_Type(Integer32):
    """Custom type cdx6500xdlcpPortStatus based on Integer32"""
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
        *(("busyOut", 2),
          ("disabled", 0),
          ("down", 4),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("up", 3))
    )


_Cdx6500xdlcpPortStatus_Type.__name__ = "Integer32"
_Cdx6500xdlcpPortStatus_Object = MibTableColumn
cdx6500xdlcpPortStatus = _Cdx6500xdlcpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 2),
    _Cdx6500xdlcpPortStatus_Type()
)
cdx6500xdlcpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpPortStatus.setStatus("mandatory")
_Cdx6500xdlcpPortSpeed_Type = Integer32
_Cdx6500xdlcpPortSpeed_Object = MibTableColumn
cdx6500xdlcpPortSpeed = _Cdx6500xdlcpPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 3),
    _Cdx6500xdlcpPortSpeed_Type()
)
cdx6500xdlcpPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpPortSpeed.setStatus("mandatory")


class _Cdx6500xdlcpUtilizationIn_Type(Integer32):
    """Custom type cdx6500xdlcpUtilizationIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500xdlcpUtilizationIn_Type.__name__ = "Integer32"
_Cdx6500xdlcpUtilizationIn_Object = MibTableColumn
cdx6500xdlcpUtilizationIn = _Cdx6500xdlcpUtilizationIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 4),
    _Cdx6500xdlcpUtilizationIn_Type()
)
cdx6500xdlcpUtilizationIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpUtilizationIn.setStatus("mandatory")


class _Cdx6500xdlcpUtilizationOut_Type(Integer32):
    """Custom type cdx6500xdlcpUtilizationOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500xdlcpUtilizationOut_Type.__name__ = "Integer32"
_Cdx6500xdlcpUtilizationOut_Object = MibTableColumn
cdx6500xdlcpUtilizationOut = _Cdx6500xdlcpUtilizationOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 5),
    _Cdx6500xdlcpUtilizationOut_Type()
)
cdx6500xdlcpUtilizationOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpUtilizationOut.setStatus("mandatory")
_Cdx6500xdlcpCharInTotal_Type = Counter32
_Cdx6500xdlcpCharInTotal_Object = MibTableColumn
cdx6500xdlcpCharInTotal = _Cdx6500xdlcpCharInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 6),
    _Cdx6500xdlcpCharInTotal_Type()
)
cdx6500xdlcpCharInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpCharInTotal.setStatus("mandatory")
_Cdx6500xdlcpCharOutTotal_Type = Counter32
_Cdx6500xdlcpCharOutTotal_Object = MibTableColumn
cdx6500xdlcpCharOutTotal = _Cdx6500xdlcpCharOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 7),
    _Cdx6500xdlcpCharOutTotal_Type()
)
cdx6500xdlcpCharOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpCharOutTotal.setStatus("mandatory")
_Cdx6500xdlcpCharsInPerSec_Type = Integer32
_Cdx6500xdlcpCharsInPerSec_Object = MibTableColumn
cdx6500xdlcpCharsInPerSec = _Cdx6500xdlcpCharsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 8),
    _Cdx6500xdlcpCharsInPerSec_Type()
)
cdx6500xdlcpCharsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpCharsInPerSec.setStatus("mandatory")
_Cdx6500xdlcpCharsOutPerSec_Type = Integer32
_Cdx6500xdlcpCharsOutPerSec_Object = MibTableColumn
cdx6500xdlcpCharsOutPerSec = _Cdx6500xdlcpCharsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 9),
    _Cdx6500xdlcpCharsOutPerSec_Type()
)
cdx6500xdlcpCharsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpCharsOutPerSec.setStatus("mandatory")
_Cdx6500xdlcpFrameInTotal_Type = Counter32
_Cdx6500xdlcpFrameInTotal_Object = MibTableColumn
cdx6500xdlcpFrameInTotal = _Cdx6500xdlcpFrameInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 10),
    _Cdx6500xdlcpFrameInTotal_Type()
)
cdx6500xdlcpFrameInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpFrameInTotal.setStatus("mandatory")
_Cdx6500xdlcpFrameOutTotal_Type = Counter32
_Cdx6500xdlcpFrameOutTotal_Object = MibTableColumn
cdx6500xdlcpFrameOutTotal = _Cdx6500xdlcpFrameOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 11),
    _Cdx6500xdlcpFrameOutTotal_Type()
)
cdx6500xdlcpFrameOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpFrameOutTotal.setStatus("mandatory")
_Cdx6500xdlcpFramesInPerSec_Type = Integer32
_Cdx6500xdlcpFramesInPerSec_Object = MibTableColumn
cdx6500xdlcpFramesInPerSec = _Cdx6500xdlcpFramesInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 12),
    _Cdx6500xdlcpFramesInPerSec_Type()
)
cdx6500xdlcpFramesInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpFramesInPerSec.setStatus("mandatory")
_Cdx6500xdlcpFramesOutPerSec_Type = Integer32
_Cdx6500xdlcpFramesOutPerSec_Object = MibTableColumn
cdx6500xdlcpFramesOutPerSec = _Cdx6500xdlcpFramesOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 13),
    _Cdx6500xdlcpFramesOutPerSec_Type()
)
cdx6500xdlcpFramesOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpFramesOutPerSec.setStatus("mandatory")
_Cdx6500xdlcpCRCErrors_Type = Counter16
_Cdx6500xdlcpCRCErrors_Object = MibTableColumn
cdx6500xdlcpCRCErrors = _Cdx6500xdlcpCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 14),
    _Cdx6500xdlcpCRCErrors_Type()
)
cdx6500xdlcpCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpCRCErrors.setStatus("mandatory")
_Cdx6500xdlcpOverrunErrors_Type = Counter16
_Cdx6500xdlcpOverrunErrors_Object = MibTableColumn
cdx6500xdlcpOverrunErrors = _Cdx6500xdlcpOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 15),
    _Cdx6500xdlcpOverrunErrors_Type()
)
cdx6500xdlcpOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpOverrunErrors.setStatus("mandatory")
_Cdx6500xdlcpUnderrunErrors_Type = Counter16
_Cdx6500xdlcpUnderrunErrors_Object = MibTableColumn
cdx6500xdlcpUnderrunErrors = _Cdx6500xdlcpUnderrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 16),
    _Cdx6500xdlcpUnderrunErrors_Type()
)
cdx6500xdlcpUnderrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpUnderrunErrors.setStatus("mandatory")
_Cdx6500xdlcpRNRFramesIn_Type = Counter32
_Cdx6500xdlcpRNRFramesIn_Object = MibTableColumn
cdx6500xdlcpRNRFramesIn = _Cdx6500xdlcpRNRFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 17),
    _Cdx6500xdlcpRNRFramesIn_Type()
)
cdx6500xdlcpRNRFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpRNRFramesIn.setStatus("mandatory")
_Cdx6500xdlcpRNRFramesOut_Type = Counter32
_Cdx6500xdlcpRNRFramesOut_Object = MibTableColumn
cdx6500xdlcpRNRFramesOut = _Cdx6500xdlcpRNRFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 18),
    _Cdx6500xdlcpRNRFramesOut_Type()
)
cdx6500xdlcpRNRFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpRNRFramesOut.setStatus("mandatory")
_Cdx6500xdlcpRRFramesIn_Type = Counter32
_Cdx6500xdlcpRRFramesIn_Object = MibTableColumn
cdx6500xdlcpRRFramesIn = _Cdx6500xdlcpRRFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 19),
    _Cdx6500xdlcpRRFramesIn_Type()
)
cdx6500xdlcpRRFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpRRFramesIn.setStatus("mandatory")
_Cdx6500xdlcpRRFramesOut_Type = Counter32
_Cdx6500xdlcpRRFramesOut_Object = MibTableColumn
cdx6500xdlcpRRFramesOut = _Cdx6500xdlcpRRFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 20),
    _Cdx6500xdlcpRRFramesOut_Type()
)
cdx6500xdlcpRRFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpRRFramesOut.setStatus("mandatory")
_Cdx6500xdlcpREJFramesIn_Type = Counter32
_Cdx6500xdlcpREJFramesIn_Object = MibTableColumn
cdx6500xdlcpREJFramesIn = _Cdx6500xdlcpREJFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 21),
    _Cdx6500xdlcpREJFramesIn_Type()
)
cdx6500xdlcpREJFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpREJFramesIn.setStatus("mandatory")
_Cdx6500xdlcpREJFramesOut_Type = Counter32
_Cdx6500xdlcpREJFramesOut_Object = MibTableColumn
cdx6500xdlcpREJFramesOut = _Cdx6500xdlcpREJFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 22),
    _Cdx6500xdlcpREJFramesOut_Type()
)
cdx6500xdlcpREJFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpREJFramesOut.setStatus("mandatory")
_Cdx6500xdlcpMX25StationsUp_Type = Integer32
_Cdx6500xdlcpMX25StationsUp_Object = MibTableColumn
cdx6500xdlcpMX25StationsUp = _Cdx6500xdlcpMX25StationsUp_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 23),
    _Cdx6500xdlcpMX25StationsUp_Type()
)
cdx6500xdlcpMX25StationsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpMX25StationsUp.setStatus("mandatory")
_Cdx6500xdlcpMX25StationsDown_Type = Integer32
_Cdx6500xdlcpMX25StationsDown_Object = MibTableColumn
cdx6500xdlcpMX25StationsDown = _Cdx6500xdlcpMX25StationsDown_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 24),
    _Cdx6500xdlcpMX25StationsDown_Type()
)
cdx6500xdlcpMX25StationsDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpMX25StationsDown.setStatus("mandatory")
_Cdx6500xdlcpMX25StationsDisabled_Type = Integer32
_Cdx6500xdlcpMX25StationsDisabled_Object = MibTableColumn
cdx6500xdlcpMX25StationsDisabled = _Cdx6500xdlcpMX25StationsDisabled_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 25),
    _Cdx6500xdlcpMX25StationsDisabled_Type()
)
cdx6500xdlcpMX25StationsDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpMX25StationsDisabled.setStatus("mandatory")
_Cdx6500xdlcpSDLCStationsUp_Type = Integer32
_Cdx6500xdlcpSDLCStationsUp_Object = MibTableColumn
cdx6500xdlcpSDLCStationsUp = _Cdx6500xdlcpSDLCStationsUp_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 26),
    _Cdx6500xdlcpSDLCStationsUp_Type()
)
cdx6500xdlcpSDLCStationsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpSDLCStationsUp.setStatus("mandatory")
_Cdx6500xdlcpSDLCStationsDown_Type = Integer32
_Cdx6500xdlcpSDLCStationsDown_Object = MibTableColumn
cdx6500xdlcpSDLCStationsDown = _Cdx6500xdlcpSDLCStationsDown_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 27),
    _Cdx6500xdlcpSDLCStationsDown_Type()
)
cdx6500xdlcpSDLCStationsDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpSDLCStationsDown.setStatus("mandatory")
_Cdx6500xdlcpSDLCStationsDisabled_Type = Integer32
_Cdx6500xdlcpSDLCStationsDisabled_Object = MibTableColumn
cdx6500xdlcpSDLCStationsDisabled = _Cdx6500xdlcpSDLCStationsDisabled_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 28),
    _Cdx6500xdlcpSDLCStationsDisabled_Type()
)
cdx6500xdlcpSDLCStationsDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpSDLCStationsDisabled.setStatus("mandatory")


class _Cdx6500xdlcpStateChange_Type(DisplayString):
    """Custom type cdx6500xdlcpStateChange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Cdx6500xdlcpStateChange_Type.__name__ = "DisplayString"
_Cdx6500xdlcpStateChange_Object = MibTableColumn
cdx6500xdlcpStateChange = _Cdx6500xdlcpStateChange_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 29),
    _Cdx6500xdlcpStateChange_Type()
)
cdx6500xdlcpStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpStateChange.setStatus("mandatory")
_Cdx6500xdlcpLinkDowns_Type = Counter16
_Cdx6500xdlcpLinkDowns_Object = MibTableColumn
cdx6500xdlcpLinkDowns = _Cdx6500xdlcpLinkDowns_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 30),
    _Cdx6500xdlcpLinkDowns_Type()
)
cdx6500xdlcpLinkDowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpLinkDowns.setStatus("mandatory")
_Cdx6500xdlcpPacketsQueued_Type = Integer32
_Cdx6500xdlcpPacketsQueued_Object = MibTableColumn
cdx6500xdlcpPacketsQueued = _Cdx6500xdlcpPacketsQueued_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 31),
    _Cdx6500xdlcpPacketsQueued_Type()
)
cdx6500xdlcpPacketsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpPacketsQueued.setStatus("mandatory")
_Cdx6500xdlcpSNRMInFrames_Type = Counter32
_Cdx6500xdlcpSNRMInFrames_Object = MibTableColumn
cdx6500xdlcpSNRMInFrames = _Cdx6500xdlcpSNRMInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 32),
    _Cdx6500xdlcpSNRMInFrames_Type()
)
cdx6500xdlcpSNRMInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpSNRMInFrames.setStatus("mandatory")
_Cdx6500xdlcpSNRMOutFrames_Type = Counter32
_Cdx6500xdlcpSNRMOutFrames_Object = MibTableColumn
cdx6500xdlcpSNRMOutFrames = _Cdx6500xdlcpSNRMOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 33),
    _Cdx6500xdlcpSNRMOutFrames_Type()
)
cdx6500xdlcpSNRMOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpSNRMOutFrames.setStatus("mandatory")
_Cdx6500xdlcpUAInFrames_Type = Counter32
_Cdx6500xdlcpUAInFrames_Object = MibTableColumn
cdx6500xdlcpUAInFrames = _Cdx6500xdlcpUAInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 34),
    _Cdx6500xdlcpUAInFrames_Type()
)
cdx6500xdlcpUAInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpUAInFrames.setStatus("mandatory")
_Cdx6500xdlcpUAOutFrames_Type = Counter32
_Cdx6500xdlcpUAOutFrames_Object = MibTableColumn
cdx6500xdlcpUAOutFrames = _Cdx6500xdlcpUAOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 35),
    _Cdx6500xdlcpUAOutFrames_Type()
)
cdx6500xdlcpUAOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpUAOutFrames.setStatus("mandatory")
_Cdx6500xdlcpDMInFrames_Type = Counter32
_Cdx6500xdlcpDMInFrames_Object = MibTableColumn
cdx6500xdlcpDMInFrames = _Cdx6500xdlcpDMInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 36),
    _Cdx6500xdlcpDMInFrames_Type()
)
cdx6500xdlcpDMInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpDMInFrames.setStatus("mandatory")
_Cdx6500xdlcpDMOutFrames_Type = Counter32
_Cdx6500xdlcpDMOutFrames_Object = MibTableColumn
cdx6500xdlcpDMOutFrames = _Cdx6500xdlcpDMOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 37),
    _Cdx6500xdlcpDMOutFrames_Type()
)
cdx6500xdlcpDMOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpDMOutFrames.setStatus("mandatory")
_Cdx6500xdlcpXIDInFrames_Type = Counter32
_Cdx6500xdlcpXIDInFrames_Object = MibTableColumn
cdx6500xdlcpXIDInFrames = _Cdx6500xdlcpXIDInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 38),
    _Cdx6500xdlcpXIDInFrames_Type()
)
cdx6500xdlcpXIDInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpXIDInFrames.setStatus("mandatory")
_Cdx6500xdlcpXIDOutFrames_Type = Counter32
_Cdx6500xdlcpXIDOutFrames_Object = MibTableColumn
cdx6500xdlcpXIDOutFrames = _Cdx6500xdlcpXIDOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 39),
    _Cdx6500xdlcpXIDOutFrames_Type()
)
cdx6500xdlcpXIDOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpXIDOutFrames.setStatus("mandatory")
_Cdx6500xdlcpDISCInFrames_Type = Counter32
_Cdx6500xdlcpDISCInFrames_Object = MibTableColumn
cdx6500xdlcpDISCInFrames = _Cdx6500xdlcpDISCInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 40),
    _Cdx6500xdlcpDISCInFrames_Type()
)
cdx6500xdlcpDISCInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpDISCInFrames.setStatus("mandatory")
_Cdx6500xdlcpDISCOutFrames_Type = Counter32
_Cdx6500xdlcpDISCOutFrames_Object = MibTableColumn
cdx6500xdlcpDISCOutFrames = _Cdx6500xdlcpDISCOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 41),
    _Cdx6500xdlcpDISCOutFrames_Type()
)
cdx6500xdlcpDISCOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpDISCOutFrames.setStatus("mandatory")
_Cdx6500xdlcpRDInFrames_Type = Counter32
_Cdx6500xdlcpRDInFrames_Object = MibTableColumn
cdx6500xdlcpRDInFrames = _Cdx6500xdlcpRDInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 42),
    _Cdx6500xdlcpRDInFrames_Type()
)
cdx6500xdlcpRDInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpRDInFrames.setStatus("mandatory")
_Cdx6500xdlcpRDOutFrames_Type = Counter32
_Cdx6500xdlcpRDOutFrames_Object = MibTableColumn
cdx6500xdlcpRDOutFrames = _Cdx6500xdlcpRDOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 43),
    _Cdx6500xdlcpRDOutFrames_Type()
)
cdx6500xdlcpRDOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpRDOutFrames.setStatus("mandatory")
_Cdx6500xdlcpFRMRInFrames_Type = Counter32
_Cdx6500xdlcpFRMRInFrames_Object = MibTableColumn
cdx6500xdlcpFRMRInFrames = _Cdx6500xdlcpFRMRInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 44),
    _Cdx6500xdlcpFRMRInFrames_Type()
)
cdx6500xdlcpFRMRInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpFRMRInFrames.setStatus("mandatory")
_Cdx6500xdlcpFRMROutFrames_Type = Counter32
_Cdx6500xdlcpFRMROutFrames_Object = MibTableColumn
cdx6500xdlcpFRMROutFrames = _Cdx6500xdlcpFRMROutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 45),
    _Cdx6500xdlcpFRMROutFrames_Type()
)
cdx6500xdlcpFRMROutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpFRMROutFrames.setStatus("mandatory")
_Cdx6500xdlcpUPInFrames_Type = Counter32
_Cdx6500xdlcpUPInFrames_Object = MibTableColumn
cdx6500xdlcpUPInFrames = _Cdx6500xdlcpUPInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 46),
    _Cdx6500xdlcpUPInFrames_Type()
)
cdx6500xdlcpUPInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpUPInFrames.setStatus("mandatory")
_Cdx6500xdlcpUPOutFrames_Type = Counter32
_Cdx6500xdlcpUPOutFrames_Object = MibTableColumn
cdx6500xdlcpUPOutFrames = _Cdx6500xdlcpUPOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 47),
    _Cdx6500xdlcpUPOutFrames_Type()
)
cdx6500xdlcpUPOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpUPOutFrames.setStatus("mandatory")
_Cdx6500xdlcpTESTInFrames_Type = Counter32
_Cdx6500xdlcpTESTInFrames_Object = MibTableColumn
cdx6500xdlcpTESTInFrames = _Cdx6500xdlcpTESTInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 48),
    _Cdx6500xdlcpTESTInFrames_Type()
)
cdx6500xdlcpTESTInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpTESTInFrames.setStatus("mandatory")
_Cdx6500xdlcpTESTOutFrames_Type = Counter32
_Cdx6500xdlcpTESTOutFrames_Object = MibTableColumn
cdx6500xdlcpTESTOutFrames = _Cdx6500xdlcpTESTOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 49),
    _Cdx6500xdlcpTESTOutFrames_Type()
)
cdx6500xdlcpTESTOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpTESTOutFrames.setStatus("mandatory")
_Cdx6500xdlcpXIDNullInFrames_Type = Counter32
_Cdx6500xdlcpXIDNullInFrames_Object = MibTableColumn
cdx6500xdlcpXIDNullInFrames = _Cdx6500xdlcpXIDNullInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 50),
    _Cdx6500xdlcpXIDNullInFrames_Type()
)
cdx6500xdlcpXIDNullInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpXIDNullInFrames.setStatus("mandatory")
_Cdx6500xdlcpXIDNullOutFrames_Type = Counter32
_Cdx6500xdlcpXIDNullOutFrames_Object = MibTableColumn
cdx6500xdlcpXIDNullOutFrames = _Cdx6500xdlcpXIDNullOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 51),
    _Cdx6500xdlcpXIDNullOutFrames_Type()
)
cdx6500xdlcpXIDNullOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpXIDNullOutFrames.setStatus("mandatory")
_Cdx6500xdlcpXID0InFrames_Type = Counter32
_Cdx6500xdlcpXID0InFrames_Object = MibTableColumn
cdx6500xdlcpXID0InFrames = _Cdx6500xdlcpXID0InFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 52),
    _Cdx6500xdlcpXID0InFrames_Type()
)
cdx6500xdlcpXID0InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpXID0InFrames.setStatus("mandatory")
_Cdx6500xdlcpXID0OutFrames_Type = Counter32
_Cdx6500xdlcpXID0OutFrames_Object = MibTableColumn
cdx6500xdlcpXID0OutFrames = _Cdx6500xdlcpXID0OutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 53),
    _Cdx6500xdlcpXID0OutFrames_Type()
)
cdx6500xdlcpXID0OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpXID0OutFrames.setStatus("mandatory")
_Cdx6500xdlcpXID1InFrames_Type = Counter32
_Cdx6500xdlcpXID1InFrames_Object = MibTableColumn
cdx6500xdlcpXID1InFrames = _Cdx6500xdlcpXID1InFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 54),
    _Cdx6500xdlcpXID1InFrames_Type()
)
cdx6500xdlcpXID1InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpXID1InFrames.setStatus("mandatory")
_Cdx6500xdlcpXID1OutFrames_Type = Counter32
_Cdx6500xdlcpXID1OutFrames_Object = MibTableColumn
cdx6500xdlcpXID1OutFrames = _Cdx6500xdlcpXID1OutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 55),
    _Cdx6500xdlcpXID1OutFrames_Type()
)
cdx6500xdlcpXID1OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpXID1OutFrames.setStatus("mandatory")
_Cdx6500xdlcpXID3InFrames_Type = Counter32
_Cdx6500xdlcpXID3InFrames_Object = MibTableColumn
cdx6500xdlcpXID3InFrames = _Cdx6500xdlcpXID3InFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 56),
    _Cdx6500xdlcpXID3InFrames_Type()
)
cdx6500xdlcpXID3InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpXID3InFrames.setStatus("mandatory")
_Cdx6500xdlcpXID3OutFrames_Type = Counter32
_Cdx6500xdlcpXID3OutFrames_Object = MibTableColumn
cdx6500xdlcpXID3OutFrames = _Cdx6500xdlcpXID3OutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 13, 1, 57),
    _Cdx6500xdlcpXID3OutFrames_Type()
)
cdx6500xdlcpXID3OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcpXID3OutFrames.setStatus("mandatory")
_Cdx6500PSTStationProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTStationProtocolGroup = _Cdx6500PSTStationProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3)
)
_Cdx6500SPSTXDLCStationTable_ObjectIdentity = ObjectIdentity
cdx6500SPSTXDLCStationTable = _Cdx6500SPSTXDLCStationTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5)
)
_Cdx6500SPSTXDLCSDLCStnTable_Object = MibTable
cdx6500SPSTXDLCSDLCStnTable = _Cdx6500SPSTXDLCSDLCStnTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    cdx6500SPSTXDLCSDLCStnTable.setStatus("mandatory")
_Cdx6500SPSTXDLCSDLCStnEntry_Object = MibTableRow
cdx6500SPSTXDLCSDLCStnEntry = _Cdx6500SPSTXDLCSDLCStnEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1)
)
cdx6500SPSTXDLCSDLCStnEntry.setIndexNames(
    (0, "XDLC-OPT-MIB", "cdx6500xdlcsdlcStatsPortNum"),
    (0, "XDLC-OPT-MIB", "cdx6500xdlcsdlcStatsStationNum"),
)
if mibBuilder.loadTexts:
    cdx6500SPSTXDLCSDLCStnEntry.setStatus("mandatory")


class _Cdx6500xdlcsdlcStatsPortNum_Type(Integer32):
    """Custom type cdx6500xdlcsdlcStatsPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500xdlcsdlcStatsPortNum_Type.__name__ = "Integer32"
_Cdx6500xdlcsdlcStatsPortNum_Object = MibTableColumn
cdx6500xdlcsdlcStatsPortNum = _Cdx6500xdlcsdlcStatsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 1),
    _Cdx6500xdlcsdlcStatsPortNum_Type()
)
cdx6500xdlcsdlcStatsPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcStatsPortNum.setStatus("mandatory")


class _Cdx6500xdlcsdlcStatsStationNum_Type(Integer32):
    """Custom type cdx6500xdlcsdlcStatsStationNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Cdx6500xdlcsdlcStatsStationNum_Type.__name__ = "Integer32"
_Cdx6500xdlcsdlcStatsStationNum_Object = MibTableColumn
cdx6500xdlcsdlcStatsStationNum = _Cdx6500xdlcsdlcStatsStationNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 2),
    _Cdx6500xdlcsdlcStatsStationNum_Type()
)
cdx6500xdlcsdlcStatsStationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcStatsStationNum.setStatus("mandatory")


class _Cdx6500xdlcsdlcUtilizationIn_Type(Integer32):
    """Custom type cdx6500xdlcsdlcUtilizationIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500xdlcsdlcUtilizationIn_Type.__name__ = "Integer32"
_Cdx6500xdlcsdlcUtilizationIn_Object = MibTableColumn
cdx6500xdlcsdlcUtilizationIn = _Cdx6500xdlcsdlcUtilizationIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 3),
    _Cdx6500xdlcsdlcUtilizationIn_Type()
)
cdx6500xdlcsdlcUtilizationIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcUtilizationIn.setStatus("mandatory")


class _Cdx6500xdlcsdlcUtilizationOut_Type(Integer32):
    """Custom type cdx6500xdlcsdlcUtilizationOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500xdlcsdlcUtilizationOut_Type.__name__ = "Integer32"
_Cdx6500xdlcsdlcUtilizationOut_Object = MibTableColumn
cdx6500xdlcsdlcUtilizationOut = _Cdx6500xdlcsdlcUtilizationOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 4),
    _Cdx6500xdlcsdlcUtilizationOut_Type()
)
cdx6500xdlcsdlcUtilizationOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcUtilizationOut.setStatus("mandatory")
_Cdx6500xdlcsdlcCharInTotal_Type = Counter32
_Cdx6500xdlcsdlcCharInTotal_Object = MibTableColumn
cdx6500xdlcsdlcCharInTotal = _Cdx6500xdlcsdlcCharInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 5),
    _Cdx6500xdlcsdlcCharInTotal_Type()
)
cdx6500xdlcsdlcCharInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcCharInTotal.setStatus("mandatory")
_Cdx6500xdlcsdlcCharOutTotal_Type = Counter32
_Cdx6500xdlcsdlcCharOutTotal_Object = MibTableColumn
cdx6500xdlcsdlcCharOutTotal = _Cdx6500xdlcsdlcCharOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 6),
    _Cdx6500xdlcsdlcCharOutTotal_Type()
)
cdx6500xdlcsdlcCharOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcCharOutTotal.setStatus("mandatory")
_Cdx6500xdlcsdlcCharsInPerSec_Type = Integer32
_Cdx6500xdlcsdlcCharsInPerSec_Object = MibTableColumn
cdx6500xdlcsdlcCharsInPerSec = _Cdx6500xdlcsdlcCharsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 7),
    _Cdx6500xdlcsdlcCharsInPerSec_Type()
)
cdx6500xdlcsdlcCharsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcCharsInPerSec.setStatus("mandatory")
_Cdx6500xdlcsdlcCharsOutPerSec_Type = Integer32
_Cdx6500xdlcsdlcCharsOutPerSec_Object = MibTableColumn
cdx6500xdlcsdlcCharsOutPerSec = _Cdx6500xdlcsdlcCharsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 8),
    _Cdx6500xdlcsdlcCharsOutPerSec_Type()
)
cdx6500xdlcsdlcCharsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcCharsOutPerSec.setStatus("mandatory")
_Cdx6500xdlcsdlcPacketsQueued_Type = Integer32
_Cdx6500xdlcsdlcPacketsQueued_Object = MibTableColumn
cdx6500xdlcsdlcPacketsQueued = _Cdx6500xdlcsdlcPacketsQueued_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 9),
    _Cdx6500xdlcsdlcPacketsQueued_Type()
)
cdx6500xdlcsdlcPacketsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcPacketsQueued.setStatus("mandatory")
_Cdx6500xdlcsdlcFrameInTotal_Type = Counter32
_Cdx6500xdlcsdlcFrameInTotal_Object = MibTableColumn
cdx6500xdlcsdlcFrameInTotal = _Cdx6500xdlcsdlcFrameInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 10),
    _Cdx6500xdlcsdlcFrameInTotal_Type()
)
cdx6500xdlcsdlcFrameInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcFrameInTotal.setStatus("mandatory")
_Cdx6500xdlcsdlcFrameOutTotal_Type = Counter32
_Cdx6500xdlcsdlcFrameOutTotal_Object = MibTableColumn
cdx6500xdlcsdlcFrameOutTotal = _Cdx6500xdlcsdlcFrameOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 11),
    _Cdx6500xdlcsdlcFrameOutTotal_Type()
)
cdx6500xdlcsdlcFrameOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcFrameOutTotal.setStatus("mandatory")
_Cdx6500xdlcsdlcFramesInPerSec_Type = Integer32
_Cdx6500xdlcsdlcFramesInPerSec_Object = MibTableColumn
cdx6500xdlcsdlcFramesInPerSec = _Cdx6500xdlcsdlcFramesInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 12),
    _Cdx6500xdlcsdlcFramesInPerSec_Type()
)
cdx6500xdlcsdlcFramesInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcFramesInPerSec.setStatus("mandatory")
_Cdx6500xdlcsdlcFramesOutPerSec_Type = Integer32
_Cdx6500xdlcsdlcFramesOutPerSec_Object = MibTableColumn
cdx6500xdlcsdlcFramesOutPerSec = _Cdx6500xdlcsdlcFramesOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 13),
    _Cdx6500xdlcsdlcFramesOutPerSec_Type()
)
cdx6500xdlcsdlcFramesOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcFramesOutPerSec.setStatus("mandatory")
_Cdx6500xdlcsdlcRNRFramesIn_Type = Counter32
_Cdx6500xdlcsdlcRNRFramesIn_Object = MibTableColumn
cdx6500xdlcsdlcRNRFramesIn = _Cdx6500xdlcsdlcRNRFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 14),
    _Cdx6500xdlcsdlcRNRFramesIn_Type()
)
cdx6500xdlcsdlcRNRFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcRNRFramesIn.setStatus("mandatory")
_Cdx6500xdlcsdlcRNRFramesOut_Type = Counter32
_Cdx6500xdlcsdlcRNRFramesOut_Object = MibTableColumn
cdx6500xdlcsdlcRNRFramesOut = _Cdx6500xdlcsdlcRNRFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 15),
    _Cdx6500xdlcsdlcRNRFramesOut_Type()
)
cdx6500xdlcsdlcRNRFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcRNRFramesOut.setStatus("mandatory")
_Cdx6500xdlcsdlcRRFramesIn_Type = Counter32
_Cdx6500xdlcsdlcRRFramesIn_Object = MibTableColumn
cdx6500xdlcsdlcRRFramesIn = _Cdx6500xdlcsdlcRRFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 16),
    _Cdx6500xdlcsdlcRRFramesIn_Type()
)
cdx6500xdlcsdlcRRFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcRRFramesIn.setStatus("mandatory")
_Cdx6500xdlcsdlcRRFramesOut_Type = Counter32
_Cdx6500xdlcsdlcRRFramesOut_Object = MibTableColumn
cdx6500xdlcsdlcRRFramesOut = _Cdx6500xdlcsdlcRRFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 17),
    _Cdx6500xdlcsdlcRRFramesOut_Type()
)
cdx6500xdlcsdlcRRFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcRRFramesOut.setStatus("mandatory")
_Cdx6500xdlcsdlcREJFramesIn_Type = Counter32
_Cdx6500xdlcsdlcREJFramesIn_Object = MibTableColumn
cdx6500xdlcsdlcREJFramesIn = _Cdx6500xdlcsdlcREJFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 18),
    _Cdx6500xdlcsdlcREJFramesIn_Type()
)
cdx6500xdlcsdlcREJFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcREJFramesIn.setStatus("mandatory")
_Cdx6500xdlcsdlcREJFramesOut_Type = Counter32
_Cdx6500xdlcsdlcREJFramesOut_Object = MibTableColumn
cdx6500xdlcsdlcREJFramesOut = _Cdx6500xdlcsdlcREJFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 19),
    _Cdx6500xdlcsdlcREJFramesOut_Type()
)
cdx6500xdlcsdlcREJFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcREJFramesOut.setStatus("mandatory")


class _Cdx6500xdlcsdlcQLLCState_Type(DisplayString):
    """Custom type cdx6500xdlcsdlcQLLCState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cdx6500xdlcsdlcQLLCState_Type.__name__ = "DisplayString"
_Cdx6500xdlcsdlcQLLCState_Object = MibTableColumn
cdx6500xdlcsdlcQLLCState = _Cdx6500xdlcsdlcQLLCState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 20),
    _Cdx6500xdlcsdlcQLLCState_Type()
)
cdx6500xdlcsdlcQLLCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcQLLCState.setStatus("mandatory")
_Cdx6500xdlcsdlcQRRIn_Type = Counter16
_Cdx6500xdlcsdlcQRRIn_Object = MibTableColumn
cdx6500xdlcsdlcQRRIn = _Cdx6500xdlcsdlcQRRIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 21),
    _Cdx6500xdlcsdlcQRRIn_Type()
)
cdx6500xdlcsdlcQRRIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcQRRIn.setStatus("mandatory")
_Cdx6500xdlcsdlcQRROut_Type = Counter16
_Cdx6500xdlcsdlcQRROut_Object = MibTableColumn
cdx6500xdlcsdlcQRROut = _Cdx6500xdlcsdlcQRROut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 22),
    _Cdx6500xdlcsdlcQRROut_Type()
)
cdx6500xdlcsdlcQRROut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcQRROut.setStatus("mandatory")
_Cdx6500xdlcsdlcSNRMInFrames_Type = Counter32
_Cdx6500xdlcsdlcSNRMInFrames_Object = MibTableColumn
cdx6500xdlcsdlcSNRMInFrames = _Cdx6500xdlcsdlcSNRMInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 23),
    _Cdx6500xdlcsdlcSNRMInFrames_Type()
)
cdx6500xdlcsdlcSNRMInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcSNRMInFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcSNRMOutFrames_Type = Counter32
_Cdx6500xdlcsdlcSNRMOutFrames_Object = MibTableColumn
cdx6500xdlcsdlcSNRMOutFrames = _Cdx6500xdlcsdlcSNRMOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 24),
    _Cdx6500xdlcsdlcSNRMOutFrames_Type()
)
cdx6500xdlcsdlcSNRMOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcSNRMOutFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcUAInFrames_Type = Counter32
_Cdx6500xdlcsdlcUAInFrames_Object = MibTableColumn
cdx6500xdlcsdlcUAInFrames = _Cdx6500xdlcsdlcUAInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 25),
    _Cdx6500xdlcsdlcUAInFrames_Type()
)
cdx6500xdlcsdlcUAInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcUAInFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcUAOutFrames_Type = Counter32
_Cdx6500xdlcsdlcUAOutFrames_Object = MibTableColumn
cdx6500xdlcsdlcUAOutFrames = _Cdx6500xdlcsdlcUAOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 26),
    _Cdx6500xdlcsdlcUAOutFrames_Type()
)
cdx6500xdlcsdlcUAOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcUAOutFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcDMInFrames_Type = Counter32
_Cdx6500xdlcsdlcDMInFrames_Object = MibTableColumn
cdx6500xdlcsdlcDMInFrames = _Cdx6500xdlcsdlcDMInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 27),
    _Cdx6500xdlcsdlcDMInFrames_Type()
)
cdx6500xdlcsdlcDMInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcDMInFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcDMOutFrames_Type = Counter32
_Cdx6500xdlcsdlcDMOutFrames_Object = MibTableColumn
cdx6500xdlcsdlcDMOutFrames = _Cdx6500xdlcsdlcDMOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 28),
    _Cdx6500xdlcsdlcDMOutFrames_Type()
)
cdx6500xdlcsdlcDMOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcDMOutFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcXIDInFrames_Type = Counter32
_Cdx6500xdlcsdlcXIDInFrames_Object = MibTableColumn
cdx6500xdlcsdlcXIDInFrames = _Cdx6500xdlcsdlcXIDInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 29),
    _Cdx6500xdlcsdlcXIDInFrames_Type()
)
cdx6500xdlcsdlcXIDInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcXIDInFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcXIDOutFrames_Type = Counter32
_Cdx6500xdlcsdlcXIDOutFrames_Object = MibTableColumn
cdx6500xdlcsdlcXIDOutFrames = _Cdx6500xdlcsdlcXIDOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 30),
    _Cdx6500xdlcsdlcXIDOutFrames_Type()
)
cdx6500xdlcsdlcXIDOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcXIDOutFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcDISCInFrames_Type = Counter32
_Cdx6500xdlcsdlcDISCInFrames_Object = MibTableColumn
cdx6500xdlcsdlcDISCInFrames = _Cdx6500xdlcsdlcDISCInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 31),
    _Cdx6500xdlcsdlcDISCInFrames_Type()
)
cdx6500xdlcsdlcDISCInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcDISCInFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcDISCOutFrames_Type = Counter32
_Cdx6500xdlcsdlcDISCOutFrames_Object = MibTableColumn
cdx6500xdlcsdlcDISCOutFrames = _Cdx6500xdlcsdlcDISCOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 32),
    _Cdx6500xdlcsdlcDISCOutFrames_Type()
)
cdx6500xdlcsdlcDISCOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcDISCOutFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcRDInFrames_Type = Counter32
_Cdx6500xdlcsdlcRDInFrames_Object = MibTableColumn
cdx6500xdlcsdlcRDInFrames = _Cdx6500xdlcsdlcRDInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 33),
    _Cdx6500xdlcsdlcRDInFrames_Type()
)
cdx6500xdlcsdlcRDInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcRDInFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcRDOutFrames_Type = Counter32
_Cdx6500xdlcsdlcRDOutFrames_Object = MibTableColumn
cdx6500xdlcsdlcRDOutFrames = _Cdx6500xdlcsdlcRDOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 34),
    _Cdx6500xdlcsdlcRDOutFrames_Type()
)
cdx6500xdlcsdlcRDOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcRDOutFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcFRMRInFrames_Type = Counter32
_Cdx6500xdlcsdlcFRMRInFrames_Object = MibTableColumn
cdx6500xdlcsdlcFRMRInFrames = _Cdx6500xdlcsdlcFRMRInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 35),
    _Cdx6500xdlcsdlcFRMRInFrames_Type()
)
cdx6500xdlcsdlcFRMRInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcFRMRInFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcFRMROutFrames_Type = Counter32
_Cdx6500xdlcsdlcFRMROutFrames_Object = MibTableColumn
cdx6500xdlcsdlcFRMROutFrames = _Cdx6500xdlcsdlcFRMROutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 36),
    _Cdx6500xdlcsdlcFRMROutFrames_Type()
)
cdx6500xdlcsdlcFRMROutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcFRMROutFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcUPInFrames_Type = Counter32
_Cdx6500xdlcsdlcUPInFrames_Object = MibTableColumn
cdx6500xdlcsdlcUPInFrames = _Cdx6500xdlcsdlcUPInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 37),
    _Cdx6500xdlcsdlcUPInFrames_Type()
)
cdx6500xdlcsdlcUPInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcUPInFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcUPOutFrames_Type = Counter32
_Cdx6500xdlcsdlcUPOutFrames_Object = MibTableColumn
cdx6500xdlcsdlcUPOutFrames = _Cdx6500xdlcsdlcUPOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 38),
    _Cdx6500xdlcsdlcUPOutFrames_Type()
)
cdx6500xdlcsdlcUPOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcUPOutFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcTESTInFrames_Type = Counter32
_Cdx6500xdlcsdlcTESTInFrames_Object = MibTableColumn
cdx6500xdlcsdlcTESTInFrames = _Cdx6500xdlcsdlcTESTInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 39),
    _Cdx6500xdlcsdlcTESTInFrames_Type()
)
cdx6500xdlcsdlcTESTInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcTESTInFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcTESTOutFrames_Type = Counter32
_Cdx6500xdlcsdlcTESTOutFrames_Object = MibTableColumn
cdx6500xdlcsdlcTESTOutFrames = _Cdx6500xdlcsdlcTESTOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 40),
    _Cdx6500xdlcsdlcTESTOutFrames_Type()
)
cdx6500xdlcsdlcTESTOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcTESTOutFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcQSMInFrames_Type = Counter16
_Cdx6500xdlcsdlcQSMInFrames_Object = MibTableColumn
cdx6500xdlcsdlcQSMInFrames = _Cdx6500xdlcsdlcQSMInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 41),
    _Cdx6500xdlcsdlcQSMInFrames_Type()
)
cdx6500xdlcsdlcQSMInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcQSMInFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcQSMOutFrames_Type = Counter16
_Cdx6500xdlcsdlcQSMOutFrames_Object = MibTableColumn
cdx6500xdlcsdlcQSMOutFrames = _Cdx6500xdlcsdlcQSMOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 42),
    _Cdx6500xdlcsdlcQSMOutFrames_Type()
)
cdx6500xdlcsdlcQSMOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcQSMOutFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcQUAInFrames_Type = Counter16
_Cdx6500xdlcsdlcQUAInFrames_Object = MibTableColumn
cdx6500xdlcsdlcQUAInFrames = _Cdx6500xdlcsdlcQUAInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 43),
    _Cdx6500xdlcsdlcQUAInFrames_Type()
)
cdx6500xdlcsdlcQUAInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcQUAInFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcQUAOutFrames_Type = Counter16
_Cdx6500xdlcsdlcQUAOutFrames_Object = MibTableColumn
cdx6500xdlcsdlcQUAOutFrames = _Cdx6500xdlcsdlcQUAOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 44),
    _Cdx6500xdlcsdlcQUAOutFrames_Type()
)
cdx6500xdlcsdlcQUAOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcQUAOutFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcQRDInFrames_Type = Counter16
_Cdx6500xdlcsdlcQRDInFrames_Object = MibTableColumn
cdx6500xdlcsdlcQRDInFrames = _Cdx6500xdlcsdlcQRDInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 45),
    _Cdx6500xdlcsdlcQRDInFrames_Type()
)
cdx6500xdlcsdlcQRDInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcQRDInFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcQRDOutFrames_Type = Counter16
_Cdx6500xdlcsdlcQRDOutFrames_Object = MibTableColumn
cdx6500xdlcsdlcQRDOutFrames = _Cdx6500xdlcsdlcQRDOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 46),
    _Cdx6500xdlcsdlcQRDOutFrames_Type()
)
cdx6500xdlcsdlcQRDOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcQRDOutFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcQFRMRInFrames_Type = Counter16
_Cdx6500xdlcsdlcQFRMRInFrames_Object = MibTableColumn
cdx6500xdlcsdlcQFRMRInFrames = _Cdx6500xdlcsdlcQFRMRInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 47),
    _Cdx6500xdlcsdlcQFRMRInFrames_Type()
)
cdx6500xdlcsdlcQFRMRInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcQFRMRInFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcQFRMROutFrames_Type = Counter16
_Cdx6500xdlcsdlcQFRMROutFrames_Object = MibTableColumn
cdx6500xdlcsdlcQFRMROutFrames = _Cdx6500xdlcsdlcQFRMROutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 48),
    _Cdx6500xdlcsdlcQFRMROutFrames_Type()
)
cdx6500xdlcsdlcQFRMROutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcQFRMROutFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcQXIDInFrames_Type = Counter16
_Cdx6500xdlcsdlcQXIDInFrames_Object = MibTableColumn
cdx6500xdlcsdlcQXIDInFrames = _Cdx6500xdlcsdlcQXIDInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 49),
    _Cdx6500xdlcsdlcQXIDInFrames_Type()
)
cdx6500xdlcsdlcQXIDInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcQXIDInFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcQXIDOutFrames_Type = Counter16
_Cdx6500xdlcsdlcQXIDOutFrames_Object = MibTableColumn
cdx6500xdlcsdlcQXIDOutFrames = _Cdx6500xdlcsdlcQXIDOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 50),
    _Cdx6500xdlcsdlcQXIDOutFrames_Type()
)
cdx6500xdlcsdlcQXIDOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcQXIDOutFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcQDCInFrames_Type = Counter16
_Cdx6500xdlcsdlcQDCInFrames_Object = MibTableColumn
cdx6500xdlcsdlcQDCInFrames = _Cdx6500xdlcsdlcQDCInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 51),
    _Cdx6500xdlcsdlcQDCInFrames_Type()
)
cdx6500xdlcsdlcQDCInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcQDCInFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcQDCOutFrames_Type = Counter16
_Cdx6500xdlcsdlcQDCOutFrames_Object = MibTableColumn
cdx6500xdlcsdlcQDCOutFrames = _Cdx6500xdlcsdlcQDCOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 52),
    _Cdx6500xdlcsdlcQDCOutFrames_Type()
)
cdx6500xdlcsdlcQDCOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcQDCOutFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcQDMInFrames_Type = Counter16
_Cdx6500xdlcsdlcQDMInFrames_Object = MibTableColumn
cdx6500xdlcsdlcQDMInFrames = _Cdx6500xdlcsdlcQDMInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 53),
    _Cdx6500xdlcsdlcQDMInFrames_Type()
)
cdx6500xdlcsdlcQDMInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcQDMInFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcQDMOutFrames_Type = Counter16
_Cdx6500xdlcsdlcQDMOutFrames_Object = MibTableColumn
cdx6500xdlcsdlcQDMOutFrames = _Cdx6500xdlcsdlcQDMOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 54),
    _Cdx6500xdlcsdlcQDMOutFrames_Type()
)
cdx6500xdlcsdlcQDMOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcQDMOutFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcQTESTInFrames_Type = Counter16
_Cdx6500xdlcsdlcQTESTInFrames_Object = MibTableColumn
cdx6500xdlcsdlcQTESTInFrames = _Cdx6500xdlcsdlcQTESTInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 55),
    _Cdx6500xdlcsdlcQTESTInFrames_Type()
)
cdx6500xdlcsdlcQTESTInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcQTESTInFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcQTESTOutFrames_Type = Counter16
_Cdx6500xdlcsdlcQTESTOutFrames_Object = MibTableColumn
cdx6500xdlcsdlcQTESTOutFrames = _Cdx6500xdlcsdlcQTESTOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 56),
    _Cdx6500xdlcsdlcQTESTOutFrames_Type()
)
cdx6500xdlcsdlcQTESTOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcQTESTOutFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcQSSInFrames_Type = Counter16
_Cdx6500xdlcsdlcQSSInFrames_Object = MibTableColumn
cdx6500xdlcsdlcQSSInFrames = _Cdx6500xdlcsdlcQSSInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 57),
    _Cdx6500xdlcsdlcQSSInFrames_Type()
)
cdx6500xdlcsdlcQSSInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcQSSInFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcQSSOutFrames_Type = Counter16
_Cdx6500xdlcsdlcQSSOutFrames_Object = MibTableColumn
cdx6500xdlcsdlcQSSOutFrames = _Cdx6500xdlcsdlcQSSOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 58),
    _Cdx6500xdlcsdlcQSSOutFrames_Type()
)
cdx6500xdlcsdlcQSSOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcQSSOutFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcQRSInFrames_Type = Counter16
_Cdx6500xdlcsdlcQRSInFrames_Object = MibTableColumn
cdx6500xdlcsdlcQRSInFrames = _Cdx6500xdlcsdlcQRSInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 59),
    _Cdx6500xdlcsdlcQRSInFrames_Type()
)
cdx6500xdlcsdlcQRSInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcQRSInFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcQRSOutFrames_Type = Counter16
_Cdx6500xdlcsdlcQRSOutFrames_Object = MibTableColumn
cdx6500xdlcsdlcQRSOutFrames = _Cdx6500xdlcsdlcQRSOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 60),
    _Cdx6500xdlcsdlcQRSOutFrames_Type()
)
cdx6500xdlcsdlcQRSOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcQRSOutFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcXIDNullInFrames_Type = Counter32
_Cdx6500xdlcsdlcXIDNullInFrames_Object = MibTableColumn
cdx6500xdlcsdlcXIDNullInFrames = _Cdx6500xdlcsdlcXIDNullInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 61),
    _Cdx6500xdlcsdlcXIDNullInFrames_Type()
)
cdx6500xdlcsdlcXIDNullInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcXIDNullInFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcXIDNullOutFrames_Type = Counter32
_Cdx6500xdlcsdlcXIDNullOutFrames_Object = MibTableColumn
cdx6500xdlcsdlcXIDNullOutFrames = _Cdx6500xdlcsdlcXIDNullOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 62),
    _Cdx6500xdlcsdlcXIDNullOutFrames_Type()
)
cdx6500xdlcsdlcXIDNullOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcXIDNullOutFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcXID0InFrames_Type = Counter32
_Cdx6500xdlcsdlcXID0InFrames_Object = MibTableColumn
cdx6500xdlcsdlcXID0InFrames = _Cdx6500xdlcsdlcXID0InFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 63),
    _Cdx6500xdlcsdlcXID0InFrames_Type()
)
cdx6500xdlcsdlcXID0InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcXID0InFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcXID0OutFrames_Type = Counter32
_Cdx6500xdlcsdlcXID0OutFrames_Object = MibTableColumn
cdx6500xdlcsdlcXID0OutFrames = _Cdx6500xdlcsdlcXID0OutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 64),
    _Cdx6500xdlcsdlcXID0OutFrames_Type()
)
cdx6500xdlcsdlcXID0OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcXID0OutFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcXID1InFrames_Type = Counter32
_Cdx6500xdlcsdlcXID1InFrames_Object = MibTableColumn
cdx6500xdlcsdlcXID1InFrames = _Cdx6500xdlcsdlcXID1InFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 65),
    _Cdx6500xdlcsdlcXID1InFrames_Type()
)
cdx6500xdlcsdlcXID1InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcXID1InFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcXID1OutFrames_Type = Counter32
_Cdx6500xdlcsdlcXID1OutFrames_Object = MibTableColumn
cdx6500xdlcsdlcXID1OutFrames = _Cdx6500xdlcsdlcXID1OutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 66),
    _Cdx6500xdlcsdlcXID1OutFrames_Type()
)
cdx6500xdlcsdlcXID1OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcXID1OutFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcXID3InFrames_Type = Counter32
_Cdx6500xdlcsdlcXID3InFrames_Object = MibTableColumn
cdx6500xdlcsdlcXID3InFrames = _Cdx6500xdlcsdlcXID3InFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 67),
    _Cdx6500xdlcsdlcXID3InFrames_Type()
)
cdx6500xdlcsdlcXID3InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcXID3InFrames.setStatus("mandatory")
_Cdx6500xdlcsdlcXID3OutFrames_Type = Counter32
_Cdx6500xdlcsdlcXID3OutFrames_Object = MibTableColumn
cdx6500xdlcsdlcXID3OutFrames = _Cdx6500xdlcsdlcXID3OutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 68),
    _Cdx6500xdlcsdlcXID3OutFrames_Type()
)
cdx6500xdlcsdlcXID3OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcXID3OutFrames.setStatus("mandatory")


class _Cdx6500xdlcsdlcVSNumber_Type(Integer32):
    """Custom type cdx6500xdlcsdlcVSNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Cdx6500xdlcsdlcVSNumber_Type.__name__ = "Integer32"
_Cdx6500xdlcsdlcVSNumber_Object = MibTableColumn
cdx6500xdlcsdlcVSNumber = _Cdx6500xdlcsdlcVSNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 69),
    _Cdx6500xdlcsdlcVSNumber_Type()
)
cdx6500xdlcsdlcVSNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcVSNumber.setStatus("mandatory")


class _Cdx6500xdlcsdlcVRNumber_Type(Integer32):
    """Custom type cdx6500xdlcsdlcVRNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Cdx6500xdlcsdlcVRNumber_Type.__name__ = "Integer32"
_Cdx6500xdlcsdlcVRNumber_Object = MibTableColumn
cdx6500xdlcsdlcVRNumber = _Cdx6500xdlcsdlcVRNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 70),
    _Cdx6500xdlcsdlcVRNumber_Type()
)
cdx6500xdlcsdlcVRNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcVRNumber.setStatus("mandatory")


class _Cdx6500xdlcsdlcNRNumber_Type(Integer32):
    """Custom type cdx6500xdlcsdlcNRNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Cdx6500xdlcsdlcNRNumber_Type.__name__ = "Integer32"
_Cdx6500xdlcsdlcNRNumber_Object = MibTableColumn
cdx6500xdlcsdlcNRNumber = _Cdx6500xdlcsdlcNRNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 71),
    _Cdx6500xdlcsdlcNRNumber_Type()
)
cdx6500xdlcsdlcNRNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcNRNumber.setStatus("mandatory")


class _Cdx6500xdlcsdlcNSNumber_Type(Integer32):
    """Custom type cdx6500xdlcsdlcNSNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Cdx6500xdlcsdlcNSNumber_Type.__name__ = "Integer32"
_Cdx6500xdlcsdlcNSNumber_Object = MibTableColumn
cdx6500xdlcsdlcNSNumber = _Cdx6500xdlcsdlcNSNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 1, 1, 72),
    _Cdx6500xdlcsdlcNSNumber_Type()
)
cdx6500xdlcsdlcNSNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsdlcNSNumber.setStatus("mandatory")
_Cdx6500SPSTXDLCMX25StnTable_Object = MibTable
cdx6500SPSTXDLCMX25StnTable = _Cdx6500SPSTXDLCMX25StnTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2)
)
if mibBuilder.loadTexts:
    cdx6500SPSTXDLCMX25StnTable.setStatus("mandatory")
_Cdx6500SPSTXDLCMX25StnEntry_Object = MibTableRow
cdx6500SPSTXDLCMX25StnEntry = _Cdx6500SPSTXDLCMX25StnEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1)
)
cdx6500SPSTXDLCMX25StnEntry.setIndexNames(
    (0, "XDLC-OPT-MIB", "cdx6500xdlcmx25StatsPortNum"),
    (0, "XDLC-OPT-MIB", "cdx6500xdlcmx25StatsStationNum"),
)
if mibBuilder.loadTexts:
    cdx6500SPSTXDLCMX25StnEntry.setStatus("mandatory")


class _Cdx6500xdlcmx25StatsPortNum_Type(Integer32):
    """Custom type cdx6500xdlcmx25StatsPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500xdlcmx25StatsPortNum_Type.__name__ = "Integer32"
_Cdx6500xdlcmx25StatsPortNum_Object = MibTableColumn
cdx6500xdlcmx25StatsPortNum = _Cdx6500xdlcmx25StatsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 1),
    _Cdx6500xdlcmx25StatsPortNum_Type()
)
cdx6500xdlcmx25StatsPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25StatsPortNum.setStatus("mandatory")


class _Cdx6500xdlcmx25StatsStationNum_Type(Integer32):
    """Custom type cdx6500xdlcmx25StatsStationNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Cdx6500xdlcmx25StatsStationNum_Type.__name__ = "Integer32"
_Cdx6500xdlcmx25StatsStationNum_Object = MibTableColumn
cdx6500xdlcmx25StatsStationNum = _Cdx6500xdlcmx25StatsStationNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 2),
    _Cdx6500xdlcmx25StatsStationNum_Type()
)
cdx6500xdlcmx25StatsStationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25StatsStationNum.setStatus("mandatory")


class _Cdx6500xdlcmx25UtilizationIn_Type(Integer32):
    """Custom type cdx6500xdlcmx25UtilizationIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500xdlcmx25UtilizationIn_Type.__name__ = "Integer32"
_Cdx6500xdlcmx25UtilizationIn_Object = MibTableColumn
cdx6500xdlcmx25UtilizationIn = _Cdx6500xdlcmx25UtilizationIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 3),
    _Cdx6500xdlcmx25UtilizationIn_Type()
)
cdx6500xdlcmx25UtilizationIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25UtilizationIn.setStatus("mandatory")


class _Cdx6500xdlcmx25UtilizationOut_Type(Integer32):
    """Custom type cdx6500xdlcmx25UtilizationOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500xdlcmx25UtilizationOut_Type.__name__ = "Integer32"
_Cdx6500xdlcmx25UtilizationOut_Object = MibTableColumn
cdx6500xdlcmx25UtilizationOut = _Cdx6500xdlcmx25UtilizationOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 4),
    _Cdx6500xdlcmx25UtilizationOut_Type()
)
cdx6500xdlcmx25UtilizationOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25UtilizationOut.setStatus("mandatory")
_Cdx6500xdlcmx25CharInTotal_Type = Counter32
_Cdx6500xdlcmx25CharInTotal_Object = MibTableColumn
cdx6500xdlcmx25CharInTotal = _Cdx6500xdlcmx25CharInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 5),
    _Cdx6500xdlcmx25CharInTotal_Type()
)
cdx6500xdlcmx25CharInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25CharInTotal.setStatus("mandatory")
_Cdx6500xdlcmx25CharOutTotal_Type = Counter32
_Cdx6500xdlcmx25CharOutTotal_Object = MibTableColumn
cdx6500xdlcmx25CharOutTotal = _Cdx6500xdlcmx25CharOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 6),
    _Cdx6500xdlcmx25CharOutTotal_Type()
)
cdx6500xdlcmx25CharOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25CharOutTotal.setStatus("mandatory")
_Cdx6500xdlcmx25CharsInPerSec_Type = Integer32
_Cdx6500xdlcmx25CharsInPerSec_Object = MibTableColumn
cdx6500xdlcmx25CharsInPerSec = _Cdx6500xdlcmx25CharsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 7),
    _Cdx6500xdlcmx25CharsInPerSec_Type()
)
cdx6500xdlcmx25CharsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25CharsInPerSec.setStatus("mandatory")
_Cdx6500xdlcmx25CharsOutPerSec_Type = Integer32
_Cdx6500xdlcmx25CharsOutPerSec_Object = MibTableColumn
cdx6500xdlcmx25CharsOutPerSec = _Cdx6500xdlcmx25CharsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 8),
    _Cdx6500xdlcmx25CharsOutPerSec_Type()
)
cdx6500xdlcmx25CharsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25CharsOutPerSec.setStatus("mandatory")
_Cdx6500xdlcmx25PktInTotal_Type = Counter32
_Cdx6500xdlcmx25PktInTotal_Object = MibTableColumn
cdx6500xdlcmx25PktInTotal = _Cdx6500xdlcmx25PktInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 9),
    _Cdx6500xdlcmx25PktInTotal_Type()
)
cdx6500xdlcmx25PktInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25PktInTotal.setStatus("mandatory")
_Cdx6500xdlcmx25PktOutTotal_Type = Counter32
_Cdx6500xdlcmx25PktOutTotal_Object = MibTableColumn
cdx6500xdlcmx25PktOutTotal = _Cdx6500xdlcmx25PktOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 10),
    _Cdx6500xdlcmx25PktOutTotal_Type()
)
cdx6500xdlcmx25PktOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25PktOutTotal.setStatus("mandatory")
_Cdx6500xdlcmx25PktsInPerSec_Type = Integer32
_Cdx6500xdlcmx25PktsInPerSec_Object = MibTableColumn
cdx6500xdlcmx25PktsInPerSec = _Cdx6500xdlcmx25PktsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 11),
    _Cdx6500xdlcmx25PktsInPerSec_Type()
)
cdx6500xdlcmx25PktsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25PktsInPerSec.setStatus("mandatory")
_Cdx6500xdlcmx25PktsOutPerSec_Type = Integer32
_Cdx6500xdlcmx25PktsOutPerSec_Object = MibTableColumn
cdx6500xdlcmx25PktsOutPerSec = _Cdx6500xdlcmx25PktsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 12),
    _Cdx6500xdlcmx25PktsOutPerSec_Type()
)
cdx6500xdlcmx25PktsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25PktsOutPerSec.setStatus("mandatory")
_Cdx6500xdlcmx25PacketsQueued_Type = Integer32
_Cdx6500xdlcmx25PacketsQueued_Object = MibTableColumn
cdx6500xdlcmx25PacketsQueued = _Cdx6500xdlcmx25PacketsQueued_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 13),
    _Cdx6500xdlcmx25PacketsQueued_Type()
)
cdx6500xdlcmx25PacketsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25PacketsQueued.setStatus("mandatory")
_Cdx6500xdlcmx25FrameInTotal_Type = Counter32
_Cdx6500xdlcmx25FrameInTotal_Object = MibTableColumn
cdx6500xdlcmx25FrameInTotal = _Cdx6500xdlcmx25FrameInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 14),
    _Cdx6500xdlcmx25FrameInTotal_Type()
)
cdx6500xdlcmx25FrameInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25FrameInTotal.setStatus("mandatory")
_Cdx6500xdlcmx25FrameOutTotal_Type = Counter32
_Cdx6500xdlcmx25FrameOutTotal_Object = MibTableColumn
cdx6500xdlcmx25FrameOutTotal = _Cdx6500xdlcmx25FrameOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 15),
    _Cdx6500xdlcmx25FrameOutTotal_Type()
)
cdx6500xdlcmx25FrameOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25FrameOutTotal.setStatus("mandatory")
_Cdx6500xdlcmx25FramesInPerSec_Type = Integer32
_Cdx6500xdlcmx25FramesInPerSec_Object = MibTableColumn
cdx6500xdlcmx25FramesInPerSec = _Cdx6500xdlcmx25FramesInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 16),
    _Cdx6500xdlcmx25FramesInPerSec_Type()
)
cdx6500xdlcmx25FramesInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25FramesInPerSec.setStatus("mandatory")
_Cdx6500xdlcmx25FramesOutPerSec_Type = Integer32
_Cdx6500xdlcmx25FramesOutPerSec_Object = MibTableColumn
cdx6500xdlcmx25FramesOutPerSec = _Cdx6500xdlcmx25FramesOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 17),
    _Cdx6500xdlcmx25FramesOutPerSec_Type()
)
cdx6500xdlcmx25FramesOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25FramesOutPerSec.setStatus("mandatory")
_Cdx6500xdlcmx25RNRFramesIn_Type = Counter32
_Cdx6500xdlcmx25RNRFramesIn_Object = MibTableColumn
cdx6500xdlcmx25RNRFramesIn = _Cdx6500xdlcmx25RNRFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 18),
    _Cdx6500xdlcmx25RNRFramesIn_Type()
)
cdx6500xdlcmx25RNRFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25RNRFramesIn.setStatus("mandatory")
_Cdx6500xdlcmx25RNRFramesOut_Type = Counter32
_Cdx6500xdlcmx25RNRFramesOut_Object = MibTableColumn
cdx6500xdlcmx25RNRFramesOut = _Cdx6500xdlcmx25RNRFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 19),
    _Cdx6500xdlcmx25RNRFramesOut_Type()
)
cdx6500xdlcmx25RNRFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25RNRFramesOut.setStatus("mandatory")
_Cdx6500xdlcmx25RRFramesIn_Type = Counter32
_Cdx6500xdlcmx25RRFramesIn_Object = MibTableColumn
cdx6500xdlcmx25RRFramesIn = _Cdx6500xdlcmx25RRFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 20),
    _Cdx6500xdlcmx25RRFramesIn_Type()
)
cdx6500xdlcmx25RRFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25RRFramesIn.setStatus("mandatory")
_Cdx6500xdlcmx25RRFramesOut_Type = Counter32
_Cdx6500xdlcmx25RRFramesOut_Object = MibTableColumn
cdx6500xdlcmx25RRFramesOut = _Cdx6500xdlcmx25RRFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 21),
    _Cdx6500xdlcmx25RRFramesOut_Type()
)
cdx6500xdlcmx25RRFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25RRFramesOut.setStatus("mandatory")
_Cdx6500xdlcmx25REJFramesIn_Type = Counter32
_Cdx6500xdlcmx25REJFramesIn_Object = MibTableColumn
cdx6500xdlcmx25REJFramesIn = _Cdx6500xdlcmx25REJFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 22),
    _Cdx6500xdlcmx25REJFramesIn_Type()
)
cdx6500xdlcmx25REJFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25REJFramesIn.setStatus("mandatory")
_Cdx6500xdlcmx25REJFramesOut_Type = Counter32
_Cdx6500xdlcmx25REJFramesOut_Object = MibTableColumn
cdx6500xdlcmx25REJFramesOut = _Cdx6500xdlcmx25REJFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 23),
    _Cdx6500xdlcmx25REJFramesOut_Type()
)
cdx6500xdlcmx25REJFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25REJFramesOut.setStatus("mandatory")
_Cdx6500xdlcmx25DataPktsIn_Type = Counter32
_Cdx6500xdlcmx25DataPktsIn_Object = MibTableColumn
cdx6500xdlcmx25DataPktsIn = _Cdx6500xdlcmx25DataPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 24),
    _Cdx6500xdlcmx25DataPktsIn_Type()
)
cdx6500xdlcmx25DataPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25DataPktsIn.setStatus("mandatory")
_Cdx6500xdlcmx25DataPktsOut_Type = Counter32
_Cdx6500xdlcmx25DataPktsOut_Object = MibTableColumn
cdx6500xdlcmx25DataPktsOut = _Cdx6500xdlcmx25DataPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 25),
    _Cdx6500xdlcmx25DataPktsOut_Type()
)
cdx6500xdlcmx25DataPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25DataPktsOut.setStatus("mandatory")
_Cdx6500xdlcmx25MaxSVC_Type = Integer32
_Cdx6500xdlcmx25MaxSVC_Object = MibTableColumn
cdx6500xdlcmx25MaxSVC = _Cdx6500xdlcmx25MaxSVC_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 26),
    _Cdx6500xdlcmx25MaxSVC_Type()
)
cdx6500xdlcmx25MaxSVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25MaxSVC.setStatus("mandatory")
_Cdx6500xdlcmx25CurrentSVC_Type = Integer32
_Cdx6500xdlcmx25CurrentSVC_Object = MibTableColumn
cdx6500xdlcmx25CurrentSVC = _Cdx6500xdlcmx25CurrentSVC_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 27),
    _Cdx6500xdlcmx25CurrentSVC_Type()
)
cdx6500xdlcmx25CurrentSVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25CurrentSVC.setStatus("mandatory")
_Cdx6500xdlcmx25MaxPVC_Type = Integer32
_Cdx6500xdlcmx25MaxPVC_Object = MibTableColumn
cdx6500xdlcmx25MaxPVC = _Cdx6500xdlcmx25MaxPVC_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 28),
    _Cdx6500xdlcmx25MaxPVC_Type()
)
cdx6500xdlcmx25MaxPVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25MaxPVC.setStatus("mandatory")
_Cdx6500xdlcmx25CurrentPVC_Type = Integer32
_Cdx6500xdlcmx25CurrentPVC_Object = MibTableColumn
cdx6500xdlcmx25CurrentPVC = _Cdx6500xdlcmx25CurrentPVC_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 29),
    _Cdx6500xdlcmx25CurrentPVC_Type()
)
cdx6500xdlcmx25CurrentPVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25CurrentPVC.setStatus("mandatory")
_Cdx6500xdlcmx25InfoInFrames_Type = Counter32
_Cdx6500xdlcmx25InfoInFrames_Object = MibTableColumn
cdx6500xdlcmx25InfoInFrames = _Cdx6500xdlcmx25InfoInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 30),
    _Cdx6500xdlcmx25InfoInFrames_Type()
)
cdx6500xdlcmx25InfoInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25InfoInFrames.setStatus("mandatory")
_Cdx6500xdlcmx25InfoOutFrames_Type = Counter32
_Cdx6500xdlcmx25InfoOutFrames_Object = MibTableColumn
cdx6500xdlcmx25InfoOutFrames = _Cdx6500xdlcmx25InfoOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 31),
    _Cdx6500xdlcmx25InfoOutFrames_Type()
)
cdx6500xdlcmx25InfoOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25InfoOutFrames.setStatus("mandatory")
_Cdx6500xdlcmx25SNRMInFrames_Type = Counter32
_Cdx6500xdlcmx25SNRMInFrames_Object = MibTableColumn
cdx6500xdlcmx25SNRMInFrames = _Cdx6500xdlcmx25SNRMInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 32),
    _Cdx6500xdlcmx25SNRMInFrames_Type()
)
cdx6500xdlcmx25SNRMInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25SNRMInFrames.setStatus("mandatory")
_Cdx6500xdlcmx25SNRMOutFrames_Type = Counter32
_Cdx6500xdlcmx25SNRMOutFrames_Object = MibTableColumn
cdx6500xdlcmx25SNRMOutFrames = _Cdx6500xdlcmx25SNRMOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 33),
    _Cdx6500xdlcmx25SNRMOutFrames_Type()
)
cdx6500xdlcmx25SNRMOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25SNRMOutFrames.setStatus("mandatory")
_Cdx6500xdlcmx25UAInFrames_Type = Counter32
_Cdx6500xdlcmx25UAInFrames_Object = MibTableColumn
cdx6500xdlcmx25UAInFrames = _Cdx6500xdlcmx25UAInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 34),
    _Cdx6500xdlcmx25UAInFrames_Type()
)
cdx6500xdlcmx25UAInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25UAInFrames.setStatus("mandatory")
_Cdx6500xdlcmx25UAOutFrames_Type = Counter32
_Cdx6500xdlcmx25UAOutFrames_Object = MibTableColumn
cdx6500xdlcmx25UAOutFrames = _Cdx6500xdlcmx25UAOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 35),
    _Cdx6500xdlcmx25UAOutFrames_Type()
)
cdx6500xdlcmx25UAOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25UAOutFrames.setStatus("mandatory")
_Cdx6500xdlcmx25FRMRInFrames_Type = Counter32
_Cdx6500xdlcmx25FRMRInFrames_Object = MibTableColumn
cdx6500xdlcmx25FRMRInFrames = _Cdx6500xdlcmx25FRMRInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 36),
    _Cdx6500xdlcmx25FRMRInFrames_Type()
)
cdx6500xdlcmx25FRMRInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25FRMRInFrames.setStatus("mandatory")
_Cdx6500xdlcmx25FRMROutFrames_Type = Counter32
_Cdx6500xdlcmx25FRMROutFrames_Object = MibTableColumn
cdx6500xdlcmx25FRMROutFrames = _Cdx6500xdlcmx25FRMROutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 37),
    _Cdx6500xdlcmx25FRMROutFrames_Type()
)
cdx6500xdlcmx25FRMROutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25FRMROutFrames.setStatus("mandatory")
_Cdx6500xdlcmx25RRInPkts_Type = Counter32
_Cdx6500xdlcmx25RRInPkts_Object = MibTableColumn
cdx6500xdlcmx25RRInPkts = _Cdx6500xdlcmx25RRInPkts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 38),
    _Cdx6500xdlcmx25RRInPkts_Type()
)
cdx6500xdlcmx25RRInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25RRInPkts.setStatus("mandatory")
_Cdx6500xdlcmx25RROutPkts_Type = Counter32
_Cdx6500xdlcmx25RROutPkts_Object = MibTableColumn
cdx6500xdlcmx25RROutPkts = _Cdx6500xdlcmx25RROutPkts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 39),
    _Cdx6500xdlcmx25RROutPkts_Type()
)
cdx6500xdlcmx25RROutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25RROutPkts.setStatus("mandatory")
_Cdx6500xdlcmx25RNRInPkts_Type = Counter32
_Cdx6500xdlcmx25RNRInPkts_Object = MibTableColumn
cdx6500xdlcmx25RNRInPkts = _Cdx6500xdlcmx25RNRInPkts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 40),
    _Cdx6500xdlcmx25RNRInPkts_Type()
)
cdx6500xdlcmx25RNRInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25RNRInPkts.setStatus("mandatory")
_Cdx6500xdlcmx25RNROutPkts_Type = Counter32
_Cdx6500xdlcmx25RNROutPkts_Object = MibTableColumn
cdx6500xdlcmx25RNROutPkts = _Cdx6500xdlcmx25RNROutPkts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 41),
    _Cdx6500xdlcmx25RNROutPkts_Type()
)
cdx6500xdlcmx25RNROutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25RNROutPkts.setStatus("mandatory")
_Cdx6500xdlcmx25REJInPkts_Type = Counter32
_Cdx6500xdlcmx25REJInPkts_Object = MibTableColumn
cdx6500xdlcmx25REJInPkts = _Cdx6500xdlcmx25REJInPkts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 42),
    _Cdx6500xdlcmx25REJInPkts_Type()
)
cdx6500xdlcmx25REJInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25REJInPkts.setStatus("mandatory")
_Cdx6500xdlcmx25REJOutPkts_Type = Counter32
_Cdx6500xdlcmx25REJOutPkts_Object = MibTableColumn
cdx6500xdlcmx25REJOutPkts = _Cdx6500xdlcmx25REJOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 43),
    _Cdx6500xdlcmx25REJOutPkts_Type()
)
cdx6500xdlcmx25REJOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25REJOutPkts.setStatus("mandatory")
_Cdx6500xdlcmx25InCallReqs_Type = Counter32
_Cdx6500xdlcmx25InCallReqs_Object = MibTableColumn
cdx6500xdlcmx25InCallReqs = _Cdx6500xdlcmx25InCallReqs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 44),
    _Cdx6500xdlcmx25InCallReqs_Type()
)
cdx6500xdlcmx25InCallReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25InCallReqs.setStatus("mandatory")
_Cdx6500xdlcmx25OutCallReqs_Type = Counter32
_Cdx6500xdlcmx25OutCallReqs_Object = MibTableColumn
cdx6500xdlcmx25OutCallReqs = _Cdx6500xdlcmx25OutCallReqs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 45),
    _Cdx6500xdlcmx25OutCallReqs_Type()
)
cdx6500xdlcmx25OutCallReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25OutCallReqs.setStatus("mandatory")
_Cdx6500xdlcmx25InCallAccepts_Type = Counter32
_Cdx6500xdlcmx25InCallAccepts_Object = MibTableColumn
cdx6500xdlcmx25InCallAccepts = _Cdx6500xdlcmx25InCallAccepts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 46),
    _Cdx6500xdlcmx25InCallAccepts_Type()
)
cdx6500xdlcmx25InCallAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25InCallAccepts.setStatus("mandatory")
_Cdx6500xdlcmx25OutCallAccepts_Type = Counter32
_Cdx6500xdlcmx25OutCallAccepts_Object = MibTableColumn
cdx6500xdlcmx25OutCallAccepts = _Cdx6500xdlcmx25OutCallAccepts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 47),
    _Cdx6500xdlcmx25OutCallAccepts_Type()
)
cdx6500xdlcmx25OutCallAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25OutCallAccepts.setStatus("mandatory")
_Cdx6500xdlcmx25InClearReqs_Type = Counter32
_Cdx6500xdlcmx25InClearReqs_Object = MibTableColumn
cdx6500xdlcmx25InClearReqs = _Cdx6500xdlcmx25InClearReqs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 48),
    _Cdx6500xdlcmx25InClearReqs_Type()
)
cdx6500xdlcmx25InClearReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25InClearReqs.setStatus("mandatory")
_Cdx6500xdlcmx25OutClearReqs_Type = Counter32
_Cdx6500xdlcmx25OutClearReqs_Object = MibTableColumn
cdx6500xdlcmx25OutClearReqs = _Cdx6500xdlcmx25OutClearReqs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 49),
    _Cdx6500xdlcmx25OutClearReqs_Type()
)
cdx6500xdlcmx25OutClearReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25OutClearReqs.setStatus("mandatory")
_Cdx6500xdlcmx25InClearConfs_Type = Counter32
_Cdx6500xdlcmx25InClearConfs_Object = MibTableColumn
cdx6500xdlcmx25InClearConfs = _Cdx6500xdlcmx25InClearConfs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 50),
    _Cdx6500xdlcmx25InClearConfs_Type()
)
cdx6500xdlcmx25InClearConfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25InClearConfs.setStatus("mandatory")
_Cdx6500xdlcmx25OutClearConfs_Type = Counter32
_Cdx6500xdlcmx25OutClearConfs_Object = MibTableColumn
cdx6500xdlcmx25OutClearConfs = _Cdx6500xdlcmx25OutClearConfs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 51),
    _Cdx6500xdlcmx25OutClearConfs_Type()
)
cdx6500xdlcmx25OutClearConfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25OutClearConfs.setStatus("mandatory")
_Cdx6500xdlcmx25InInterruptReqs_Type = Counter32
_Cdx6500xdlcmx25InInterruptReqs_Object = MibTableColumn
cdx6500xdlcmx25InInterruptReqs = _Cdx6500xdlcmx25InInterruptReqs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 52),
    _Cdx6500xdlcmx25InInterruptReqs_Type()
)
cdx6500xdlcmx25InInterruptReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25InInterruptReqs.setStatus("mandatory")
_Cdx6500xdlcmx25OutInterruptReqs_Type = Counter32
_Cdx6500xdlcmx25OutInterruptReqs_Object = MibTableColumn
cdx6500xdlcmx25OutInterruptReqs = _Cdx6500xdlcmx25OutInterruptReqs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 53),
    _Cdx6500xdlcmx25OutInterruptReqs_Type()
)
cdx6500xdlcmx25OutInterruptReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25OutInterruptReqs.setStatus("mandatory")
_Cdx6500xdlcmx25InInterruptConfs_Type = Counter32
_Cdx6500xdlcmx25InInterruptConfs_Object = MibTableColumn
cdx6500xdlcmx25InInterruptConfs = _Cdx6500xdlcmx25InInterruptConfs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 54),
    _Cdx6500xdlcmx25InInterruptConfs_Type()
)
cdx6500xdlcmx25InInterruptConfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25InInterruptConfs.setStatus("mandatory")
_Cdx6500xdlcmx25OutInterruptConfs_Type = Counter32
_Cdx6500xdlcmx25OutInterruptConfs_Object = MibTableColumn
cdx6500xdlcmx25OutInterruptConfs = _Cdx6500xdlcmx25OutInterruptConfs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 55),
    _Cdx6500xdlcmx25OutInterruptConfs_Type()
)
cdx6500xdlcmx25OutInterruptConfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25OutInterruptConfs.setStatus("mandatory")
_Cdx6500xdlcmx25InResetReqs_Type = Counter32
_Cdx6500xdlcmx25InResetReqs_Object = MibTableColumn
cdx6500xdlcmx25InResetReqs = _Cdx6500xdlcmx25InResetReqs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 56),
    _Cdx6500xdlcmx25InResetReqs_Type()
)
cdx6500xdlcmx25InResetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25InResetReqs.setStatus("mandatory")
_Cdx6500xdlcmx25OutResetReqs_Type = Counter32
_Cdx6500xdlcmx25OutResetReqs_Object = MibTableColumn
cdx6500xdlcmx25OutResetReqs = _Cdx6500xdlcmx25OutResetReqs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 57),
    _Cdx6500xdlcmx25OutResetReqs_Type()
)
cdx6500xdlcmx25OutResetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25OutResetReqs.setStatus("mandatory")
_Cdx6500xdlcmx25InResetConfs_Type = Counter32
_Cdx6500xdlcmx25InResetConfs_Object = MibTableColumn
cdx6500xdlcmx25InResetConfs = _Cdx6500xdlcmx25InResetConfs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 58),
    _Cdx6500xdlcmx25InResetConfs_Type()
)
cdx6500xdlcmx25InResetConfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25InResetConfs.setStatus("mandatory")
_Cdx6500xdlcmx25OutResetConfs_Type = Counter32
_Cdx6500xdlcmx25OutResetConfs_Object = MibTableColumn
cdx6500xdlcmx25OutResetConfs = _Cdx6500xdlcmx25OutResetConfs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 59),
    _Cdx6500xdlcmx25OutResetConfs_Type()
)
cdx6500xdlcmx25OutResetConfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25OutResetConfs.setStatus("mandatory")
_Cdx6500xdlcmx25InRestartReqs_Type = Counter32
_Cdx6500xdlcmx25InRestartReqs_Object = MibTableColumn
cdx6500xdlcmx25InRestartReqs = _Cdx6500xdlcmx25InRestartReqs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 60),
    _Cdx6500xdlcmx25InRestartReqs_Type()
)
cdx6500xdlcmx25InRestartReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25InRestartReqs.setStatus("mandatory")
_Cdx6500xdlcmx25OutRestartReqs_Type = Counter32
_Cdx6500xdlcmx25OutRestartReqs_Object = MibTableColumn
cdx6500xdlcmx25OutRestartReqs = _Cdx6500xdlcmx25OutRestartReqs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 61),
    _Cdx6500xdlcmx25OutRestartReqs_Type()
)
cdx6500xdlcmx25OutRestartReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25OutRestartReqs.setStatus("mandatory")
_Cdx6500xdlcmx25InRestartConfs_Type = Counter32
_Cdx6500xdlcmx25InRestartConfs_Object = MibTableColumn
cdx6500xdlcmx25InRestartConfs = _Cdx6500xdlcmx25InRestartConfs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 62),
    _Cdx6500xdlcmx25InRestartConfs_Type()
)
cdx6500xdlcmx25InRestartConfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25InRestartConfs.setStatus("mandatory")
_Cdx6500xdlcmx25OutRestartConfs_Type = Counter32
_Cdx6500xdlcmx25OutRestartConfs_Object = MibTableColumn
cdx6500xdlcmx25OutRestartConfs = _Cdx6500xdlcmx25OutRestartConfs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 63),
    _Cdx6500xdlcmx25OutRestartConfs_Type()
)
cdx6500xdlcmx25OutRestartConfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25OutRestartConfs.setStatus("mandatory")
_Cdx6500xdlcmx25LastInLCN_Type = Integer32
_Cdx6500xdlcmx25LastInLCN_Object = MibTableColumn
cdx6500xdlcmx25LastInLCN = _Cdx6500xdlcmx25LastInLCN_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 64),
    _Cdx6500xdlcmx25LastInLCN_Type()
)
cdx6500xdlcmx25LastInLCN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25LastInLCN.setStatus("mandatory")
_Cdx6500xdlcmx25InStatus_Type = DisplayString
_Cdx6500xdlcmx25InStatus_Object = MibTableColumn
cdx6500xdlcmx25InStatus = _Cdx6500xdlcmx25InStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 65),
    _Cdx6500xdlcmx25InStatus_Type()
)
cdx6500xdlcmx25InStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25InStatus.setStatus("mandatory")
_Cdx6500xdlcmx25LICBPCalledAddr_Type = DisplayString
_Cdx6500xdlcmx25LICBPCalledAddr_Object = MibTableColumn
cdx6500xdlcmx25LICBPCalledAddr = _Cdx6500xdlcmx25LICBPCalledAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 66),
    _Cdx6500xdlcmx25LICBPCalledAddr_Type()
)
cdx6500xdlcmx25LICBPCalledAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25LICBPCalledAddr.setStatus("mandatory")
_Cdx6500xdlcmx25LICBPCallingAddr_Type = DisplayString
_Cdx6500xdlcmx25LICBPCallingAddr_Object = MibTableColumn
cdx6500xdlcmx25LICBPCallingAddr = _Cdx6500xdlcmx25LICBPCallingAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 67),
    _Cdx6500xdlcmx25LICBPCallingAddr_Type()
)
cdx6500xdlcmx25LICBPCallingAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25LICBPCallingAddr.setStatus("mandatory")
_Cdx6500xdlcmx25LICBPFacilities_Type = DisplayString
_Cdx6500xdlcmx25LICBPFacilities_Object = MibTableColumn
cdx6500xdlcmx25LICBPFacilities = _Cdx6500xdlcmx25LICBPFacilities_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 68),
    _Cdx6500xdlcmx25LICBPFacilities_Type()
)
cdx6500xdlcmx25LICBPFacilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25LICBPFacilities.setStatus("mandatory")
_Cdx6500xdlcmx25LICBPCUD_Type = DisplayString
_Cdx6500xdlcmx25LICBPCUD_Object = MibTableColumn
cdx6500xdlcmx25LICBPCUD = _Cdx6500xdlcmx25LICBPCUD_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 69),
    _Cdx6500xdlcmx25LICBPCUD_Type()
)
cdx6500xdlcmx25LICBPCUD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25LICBPCUD.setStatus("mandatory")
_Cdx6500xdlcmx25LICAPCalledAddr_Type = DisplayString
_Cdx6500xdlcmx25LICAPCalledAddr_Object = MibTableColumn
cdx6500xdlcmx25LICAPCalledAddr = _Cdx6500xdlcmx25LICAPCalledAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 70),
    _Cdx6500xdlcmx25LICAPCalledAddr_Type()
)
cdx6500xdlcmx25LICAPCalledAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25LICAPCalledAddr.setStatus("mandatory")
_Cdx6500xdlcmx25LICAPCallingAddr_Type = DisplayString
_Cdx6500xdlcmx25LICAPCallingAddr_Object = MibTableColumn
cdx6500xdlcmx25LICAPCallingAddr = _Cdx6500xdlcmx25LICAPCallingAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 71),
    _Cdx6500xdlcmx25LICAPCallingAddr_Type()
)
cdx6500xdlcmx25LICAPCallingAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25LICAPCallingAddr.setStatus("mandatory")
_Cdx6500xdlcmx25LICAPFacilities_Type = DisplayString
_Cdx6500xdlcmx25LICAPFacilities_Object = MibTableColumn
cdx6500xdlcmx25LICAPFacilities = _Cdx6500xdlcmx25LICAPFacilities_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 72),
    _Cdx6500xdlcmx25LICAPFacilities_Type()
)
cdx6500xdlcmx25LICAPFacilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25LICAPFacilities.setStatus("mandatory")
_Cdx6500xdlcmx25LICAPCUD_Type = DisplayString
_Cdx6500xdlcmx25LICAPCUD_Object = MibTableColumn
cdx6500xdlcmx25LICAPCUD = _Cdx6500xdlcmx25LICAPCUD_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 73),
    _Cdx6500xdlcmx25LICAPCUD_Type()
)
cdx6500xdlcmx25LICAPCUD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25LICAPCUD.setStatus("mandatory")
_Cdx6500xdlcmx25LastOutLCN_Type = Integer32
_Cdx6500xdlcmx25LastOutLCN_Object = MibTableColumn
cdx6500xdlcmx25LastOutLCN = _Cdx6500xdlcmx25LastOutLCN_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 74),
    _Cdx6500xdlcmx25LastOutLCN_Type()
)
cdx6500xdlcmx25LastOutLCN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25LastOutLCN.setStatus("mandatory")
_Cdx6500xdlcmx25OutStatus_Type = DisplayString
_Cdx6500xdlcmx25OutStatus_Object = MibTableColumn
cdx6500xdlcmx25OutStatus = _Cdx6500xdlcmx25OutStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 75),
    _Cdx6500xdlcmx25OutStatus_Type()
)
cdx6500xdlcmx25OutStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25OutStatus.setStatus("mandatory")
_Cdx6500xdlcmx25LOCBPCalledAddr_Type = DisplayString
_Cdx6500xdlcmx25LOCBPCalledAddr_Object = MibTableColumn
cdx6500xdlcmx25LOCBPCalledAddr = _Cdx6500xdlcmx25LOCBPCalledAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 76),
    _Cdx6500xdlcmx25LOCBPCalledAddr_Type()
)
cdx6500xdlcmx25LOCBPCalledAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25LOCBPCalledAddr.setStatus("mandatory")
_Cdx6500xdlcmx25LOCBPCallingAddr_Type = DisplayString
_Cdx6500xdlcmx25LOCBPCallingAddr_Object = MibTableColumn
cdx6500xdlcmx25LOCBPCallingAddr = _Cdx6500xdlcmx25LOCBPCallingAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 77),
    _Cdx6500xdlcmx25LOCBPCallingAddr_Type()
)
cdx6500xdlcmx25LOCBPCallingAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25LOCBPCallingAddr.setStatus("mandatory")
_Cdx6500xdlcmx25LOCBPFacilities_Type = DisplayString
_Cdx6500xdlcmx25LOCBPFacilities_Object = MibTableColumn
cdx6500xdlcmx25LOCBPFacilities = _Cdx6500xdlcmx25LOCBPFacilities_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 78),
    _Cdx6500xdlcmx25LOCBPFacilities_Type()
)
cdx6500xdlcmx25LOCBPFacilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25LOCBPFacilities.setStatus("mandatory")
_Cdx6500xdlcmx25LOCBPCUD_Type = DisplayString
_Cdx6500xdlcmx25LOCBPCUD_Object = MibTableColumn
cdx6500xdlcmx25LOCBPCUD = _Cdx6500xdlcmx25LOCBPCUD_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 79),
    _Cdx6500xdlcmx25LOCBPCUD_Type()
)
cdx6500xdlcmx25LOCBPCUD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25LOCBPCUD.setStatus("mandatory")
_Cdx6500xdlcmx25LOCAPCalledAddr_Type = DisplayString
_Cdx6500xdlcmx25LOCAPCalledAddr_Object = MibTableColumn
cdx6500xdlcmx25LOCAPCalledAddr = _Cdx6500xdlcmx25LOCAPCalledAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 80),
    _Cdx6500xdlcmx25LOCAPCalledAddr_Type()
)
cdx6500xdlcmx25LOCAPCalledAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25LOCAPCalledAddr.setStatus("mandatory")
_Cdx6500xdlcmx25LOCAPCallingAddr_Type = DisplayString
_Cdx6500xdlcmx25LOCAPCallingAddr_Object = MibTableColumn
cdx6500xdlcmx25LOCAPCallingAddr = _Cdx6500xdlcmx25LOCAPCallingAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 81),
    _Cdx6500xdlcmx25LOCAPCallingAddr_Type()
)
cdx6500xdlcmx25LOCAPCallingAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25LOCAPCallingAddr.setStatus("mandatory")
_Cdx6500xdlcmx25LOCAPFacilities_Type = DisplayString
_Cdx6500xdlcmx25LOCAPFacilities_Object = MibTableColumn
cdx6500xdlcmx25LOCAPFacilities = _Cdx6500xdlcmx25LOCAPFacilities_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 82),
    _Cdx6500xdlcmx25LOCAPFacilities_Type()
)
cdx6500xdlcmx25LOCAPFacilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25LOCAPFacilities.setStatus("mandatory")
_Cdx6500xdlcmx25LOCAPCUD_Type = DisplayString
_Cdx6500xdlcmx25LOCAPCUD_Object = MibTableColumn
cdx6500xdlcmx25LOCAPCUD = _Cdx6500xdlcmx25LOCAPCUD_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 5, 2, 1, 83),
    _Cdx6500xdlcmx25LOCAPCUD_Type()
)
cdx6500xdlcmx25LOCAPCUD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500xdlcmx25LOCAPCUD.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)
_Cdx6500ContXDLC_ObjectIdentity = ObjectIdentity
cdx6500ContXDLC = _Cdx6500ContXDLC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 7)
)
_Cdx6500ContXDLCStationTable_Object = MibTable
cdx6500ContXDLCStationTable = _Cdx6500ContXDLCStationTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 7, 1)
)
if mibBuilder.loadTexts:
    cdx6500ContXDLCStationTable.setStatus("mandatory")
_Cdx6500ContXDLCStationEntry_Object = MibTableRow
cdx6500ContXDLCStationEntry = _Cdx6500ContXDLCStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 7, 1, 1)
)
cdx6500ContXDLCStationEntry.setIndexNames(
    (0, "XDLC-OPT-MIB", "cdx6500xdlcsContPortNum"),
    (0, "XDLC-OPT-MIB", "cdx6500xdlcsContStationNum"),
)
if mibBuilder.loadTexts:
    cdx6500ContXDLCStationEntry.setStatus("mandatory")


class _Cdx6500xdlcsContPortNum_Type(Integer32):
    """Custom type cdx6500xdlcsContPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500xdlcsContPortNum_Type.__name__ = "Integer32"
_Cdx6500xdlcsContPortNum_Object = MibTableColumn
cdx6500xdlcsContPortNum = _Cdx6500xdlcsContPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 7, 1, 1, 1),
    _Cdx6500xdlcsContPortNum_Type()
)
cdx6500xdlcsContPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdx6500xdlcsContPortNum.setStatus("mandatory")


class _Cdx6500xdlcsContStationNum_Type(Integer32):
    """Custom type cdx6500xdlcsContStationNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Cdx6500xdlcsContStationNum_Type.__name__ = "Integer32"
_Cdx6500xdlcsContStationNum_Object = MibTableColumn
cdx6500xdlcsContStationNum = _Cdx6500xdlcsContStationNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 7, 1, 1, 2),
    _Cdx6500xdlcsContStationNum_Type()
)
cdx6500xdlcsContStationNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdx6500xdlcsContStationNum.setStatus("mandatory")


class _Cdx6500xdlcsContBootStation_Type(Integer32):
    """Custom type cdx6500xdlcsContBootStation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boot", 1),
          ("noBoot", 2))
    )


_Cdx6500xdlcsContBootStation_Type.__name__ = "Integer32"
_Cdx6500xdlcsContBootStation_Object = MibTableColumn
cdx6500xdlcsContBootStation = _Cdx6500xdlcsContBootStation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 7, 1, 1, 3),
    _Cdx6500xdlcsContBootStation_Type()
)
cdx6500xdlcsContBootStation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsContBootStation.setStatus("mandatory")


class _Cdx6500xdlcsContDisableStation_Type(Integer32):
    """Custom type cdx6500xdlcsContDisableStation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("noDisable", 2))
    )


_Cdx6500xdlcsContDisableStation_Type.__name__ = "Integer32"
_Cdx6500xdlcsContDisableStation_Object = MibTableColumn
cdx6500xdlcsContDisableStation = _Cdx6500xdlcsContDisableStation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 7, 1, 1, 4),
    _Cdx6500xdlcsContDisableStation_Type()
)
cdx6500xdlcsContDisableStation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsContDisableStation.setStatus("mandatory")


class _Cdx6500xdlcsContEnableStation_Type(Integer32):
    """Custom type cdx6500xdlcsContEnableStation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("noEnable", 2))
    )


_Cdx6500xdlcsContEnableStation_Type.__name__ = "Integer32"
_Cdx6500xdlcsContEnableStation_Object = MibTableColumn
cdx6500xdlcsContEnableStation = _Cdx6500xdlcsContEnableStation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 7, 1, 1, 5),
    _Cdx6500xdlcsContEnableStation_Type()
)
cdx6500xdlcsContEnableStation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsContEnableStation.setStatus("mandatory")


class _Cdx6500xdlcsContResetStnStats_Type(Integer32):
    """Custom type cdx6500xdlcsContResetStnStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 2),
          ("reset", 1))
    )


_Cdx6500xdlcsContResetStnStats_Type.__name__ = "Integer32"
_Cdx6500xdlcsContResetStnStats_Object = MibTableColumn
cdx6500xdlcsContResetStnStats = _Cdx6500xdlcsContResetStnStats_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 7, 1, 1, 6),
    _Cdx6500xdlcsContResetStnStats_Type()
)
cdx6500xdlcsContResetStnStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500xdlcsContResetStnStats.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XDLC-OPT-MIB",
    **{"Counter16": Counter16,
       "DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PPCTXDLCPortTable": cdx6500PPCTXDLCPortTable,
       "cdx6500PPCTXDLCPortEntry": cdx6500PPCTXDLCPortEntry,
       "cdx6500xdlcpCfgPortNumber": cdx6500xdlcpCfgPortNumber,
       "cdx6500xdlcpPortControl": cdx6500xdlcpPortControl,
       "cdx6500xdlcpTxCoding": cdx6500xdlcpTxCoding,
       "cdx6500xdlcpLineType": cdx6500xdlcpLineType,
       "cdx6500xdlcpTxType": cdx6500xdlcpTxType,
       "cdx6500xdlcpClockSource": cdx6500xdlcpClockSource,
       "cdx6500xdlcpClockSpeed": cdx6500xdlcpClockSpeed,
       "cdx6500xdlcpStationCnt": cdx6500xdlcpStationCnt,
       "cdx6500xdlcpPollTimer": cdx6500xdlcpPollTimer,
       "cdx6500xdlcpPollPeriod": cdx6500xdlcpPollPeriod,
       "cdx6500xdlcpTries": cdx6500xdlcpTries,
       "cdx6500xdlcpPortOptions": cdx6500xdlcpPortOptions,
       "cdx6500xdlcpPortAddress": cdx6500xdlcpPortAddress,
       "cdx6500xdlcpRestartTimer": cdx6500xdlcpRestartTimer,
       "cdx6500xdlcpResetTimer": cdx6500xdlcpResetTimer,
       "cdx6500xdlcpCallTimer": cdx6500xdlcpCallTimer,
       "cdx6500xdlcpClearTimer": cdx6500xdlcpClearTimer,
       "cdx6500xdlcpMaxFrameSize": cdx6500xdlcpMaxFrameSize,
       "cdx6500xdlcpElectricalInterfaceType": cdx6500xdlcpElectricalInterfaceType,
       "cdx6500xdlcpV24ElectricalInterfaceOption": cdx6500xdlcpV24ElectricalInterfaceOption,
       "cdx6500xdlcpHighSpeedElectricalInterfaceOption": cdx6500xdlcpHighSpeedElectricalInterfaceOption,
       "cdx6500PCTStationProtocolGroup": cdx6500PCTStationProtocolGroup,
       "cdx6500SPCTXDLCStationTable": cdx6500SPCTXDLCStationTable,
       "cdx6500SPCTXDLCStnTable": cdx6500SPCTXDLCStnTable,
       "cdx6500SPCTXDLCStnEntry": cdx6500SPCTXDLCStnEntry,
       "cdx6500xdlcsCfgPortNumber": cdx6500xdlcsCfgPortNumber,
       "cdx6500xdlcsCfgStationNumber": cdx6500xdlcsCfgStationNumber,
       "cdx6500xdlcsStationType": cdx6500xdlcsStationType,
       "cdx6500SPCTXDLCSDLCStnTable": cdx6500SPCTXDLCSDLCStnTable,
       "cdx6500SPCTXDLCSDLCStnEntry": cdx6500SPCTXDLCSDLCStnEntry,
       "cdx6500xdlcsdlcCfgPortNum": cdx6500xdlcsdlcCfgPortNum,
       "cdx6500xdlcsdlcCfgStationNum": cdx6500xdlcsdlcCfgStationNum,
       "cdx6500xdlcsdlcStationAddress": cdx6500xdlcsdlcStationAddress,
       "cdx6500xdlcsdlcFrameWinSize": cdx6500xdlcsdlcFrameWinSize,
       "cdx6500xdlcsdlcAutocallMnem": cdx6500xdlcsdlcAutocallMnem,
       "cdx6500xdlcsdlcProtocolID": cdx6500xdlcsdlcProtocolID,
       "cdx6500xdlcsdlcCUG": cdx6500xdlcsdlcCUG,
       "cdx6500xdlcsdlcOptions": cdx6500xdlcsdlcOptions,
       "cdx6500xdlcsdlcXID": cdx6500xdlcsdlcXID,
       "cdx6500xdlcsdlcStnSubaddress": cdx6500xdlcsdlcStnSubaddress,
       "cdx6500xdlcsdlcBillingRecords": cdx6500xdlcsdlcBillingRecords,
       "cdx6500xdlcsdlcProtectionLevel": cdx6500xdlcsdlcProtectionLevel,
       "cdx6500xdlcsdlcReconnectTimeout": cdx6500xdlcsdlcReconnectTimeout,
       "cdx6500xdlcsdlcReconnectLimit": cdx6500xdlcsdlcReconnectLimit,
       "cdx6500xdlcsdlcCallTimer": cdx6500xdlcsdlcCallTimer,
       "cdx6500xdlcsdlcIdleTimer": cdx6500xdlcsdlcIdleTimer,
       "cdx6500xdlcsdlcVerConnTimer": cdx6500xdlcsdlcVerConnTimer,
       "cdx6500xdlcsdlcUnsusWaitTimer": cdx6500xdlcsdlcUnsusWaitTimer,
       "cdx6500SPCTXDLCMX25StnTable": cdx6500SPCTXDLCMX25StnTable,
       "cdx6500SPCTXDLCMX25StnEntry": cdx6500SPCTXDLCMX25StnEntry,
       "cdx6500xdlcmx25CfgPortNum": cdx6500xdlcmx25CfgPortNum,
       "cdx6500xdlcmx25CfgStationNum": cdx6500xdlcmx25CfgStationNum,
       "cdx6500xdlcmx25StationAddress": cdx6500xdlcmx25StationAddress,
       "cdx6500xdlcmx25PVCChannels": cdx6500xdlcmx25PVCChannels,
       "cdx6500xdlcmx25StartingPVC": cdx6500xdlcmx25StartingPVC,
       "cdx6500xdlcmx25SVCChannels": cdx6500xdlcmx25SVCChannels,
       "cdx6500xdlcmx25StartingSVC": cdx6500xdlcmx25StartingSVC,
       "cdx6500xdlcmx25FrameWinSize": cdx6500xdlcmx25FrameWinSize,
       "cdx6500xdlcmx25PacketWinSize": cdx6500xdlcmx25PacketWinSize,
       "cdx6500xdlcmx25Options": cdx6500xdlcmx25Options,
       "cdx6500xdlcmx25RCDestination": cdx6500xdlcmx25RCDestination,
       "cdx6500xdlcmx25CUG": cdx6500xdlcmx25CUG,
       "cdx6500xdlcmx25BillingRecords": cdx6500xdlcmx25BillingRecords,
       "cdx6500xdlcmx25UpperQueue": cdx6500xdlcmx25UpperQueue,
       "cdx6500xdlcmx25LowerQueue": cdx6500xdlcmx25LowerQueue,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPSTXDLCPortTable": cdx6500PPSTXDLCPortTable,
       "cdx6500PPSTXDLCPortEntry": cdx6500PPSTXDLCPortEntry,
       "cdx6500xdlcpStatsPortNumber": cdx6500xdlcpStatsPortNumber,
       "cdx6500xdlcpPortStatus": cdx6500xdlcpPortStatus,
       "cdx6500xdlcpPortSpeed": cdx6500xdlcpPortSpeed,
       "cdx6500xdlcpUtilizationIn": cdx6500xdlcpUtilizationIn,
       "cdx6500xdlcpUtilizationOut": cdx6500xdlcpUtilizationOut,
       "cdx6500xdlcpCharInTotal": cdx6500xdlcpCharInTotal,
       "cdx6500xdlcpCharOutTotal": cdx6500xdlcpCharOutTotal,
       "cdx6500xdlcpCharsInPerSec": cdx6500xdlcpCharsInPerSec,
       "cdx6500xdlcpCharsOutPerSec": cdx6500xdlcpCharsOutPerSec,
       "cdx6500xdlcpFrameInTotal": cdx6500xdlcpFrameInTotal,
       "cdx6500xdlcpFrameOutTotal": cdx6500xdlcpFrameOutTotal,
       "cdx6500xdlcpFramesInPerSec": cdx6500xdlcpFramesInPerSec,
       "cdx6500xdlcpFramesOutPerSec": cdx6500xdlcpFramesOutPerSec,
       "cdx6500xdlcpCRCErrors": cdx6500xdlcpCRCErrors,
       "cdx6500xdlcpOverrunErrors": cdx6500xdlcpOverrunErrors,
       "cdx6500xdlcpUnderrunErrors": cdx6500xdlcpUnderrunErrors,
       "cdx6500xdlcpRNRFramesIn": cdx6500xdlcpRNRFramesIn,
       "cdx6500xdlcpRNRFramesOut": cdx6500xdlcpRNRFramesOut,
       "cdx6500xdlcpRRFramesIn": cdx6500xdlcpRRFramesIn,
       "cdx6500xdlcpRRFramesOut": cdx6500xdlcpRRFramesOut,
       "cdx6500xdlcpREJFramesIn": cdx6500xdlcpREJFramesIn,
       "cdx6500xdlcpREJFramesOut": cdx6500xdlcpREJFramesOut,
       "cdx6500xdlcpMX25StationsUp": cdx6500xdlcpMX25StationsUp,
       "cdx6500xdlcpMX25StationsDown": cdx6500xdlcpMX25StationsDown,
       "cdx6500xdlcpMX25StationsDisabled": cdx6500xdlcpMX25StationsDisabled,
       "cdx6500xdlcpSDLCStationsUp": cdx6500xdlcpSDLCStationsUp,
       "cdx6500xdlcpSDLCStationsDown": cdx6500xdlcpSDLCStationsDown,
       "cdx6500xdlcpSDLCStationsDisabled": cdx6500xdlcpSDLCStationsDisabled,
       "cdx6500xdlcpStateChange": cdx6500xdlcpStateChange,
       "cdx6500xdlcpLinkDowns": cdx6500xdlcpLinkDowns,
       "cdx6500xdlcpPacketsQueued": cdx6500xdlcpPacketsQueued,
       "cdx6500xdlcpSNRMInFrames": cdx6500xdlcpSNRMInFrames,
       "cdx6500xdlcpSNRMOutFrames": cdx6500xdlcpSNRMOutFrames,
       "cdx6500xdlcpUAInFrames": cdx6500xdlcpUAInFrames,
       "cdx6500xdlcpUAOutFrames": cdx6500xdlcpUAOutFrames,
       "cdx6500xdlcpDMInFrames": cdx6500xdlcpDMInFrames,
       "cdx6500xdlcpDMOutFrames": cdx6500xdlcpDMOutFrames,
       "cdx6500xdlcpXIDInFrames": cdx6500xdlcpXIDInFrames,
       "cdx6500xdlcpXIDOutFrames": cdx6500xdlcpXIDOutFrames,
       "cdx6500xdlcpDISCInFrames": cdx6500xdlcpDISCInFrames,
       "cdx6500xdlcpDISCOutFrames": cdx6500xdlcpDISCOutFrames,
       "cdx6500xdlcpRDInFrames": cdx6500xdlcpRDInFrames,
       "cdx6500xdlcpRDOutFrames": cdx6500xdlcpRDOutFrames,
       "cdx6500xdlcpFRMRInFrames": cdx6500xdlcpFRMRInFrames,
       "cdx6500xdlcpFRMROutFrames": cdx6500xdlcpFRMROutFrames,
       "cdx6500xdlcpUPInFrames": cdx6500xdlcpUPInFrames,
       "cdx6500xdlcpUPOutFrames": cdx6500xdlcpUPOutFrames,
       "cdx6500xdlcpTESTInFrames": cdx6500xdlcpTESTInFrames,
       "cdx6500xdlcpTESTOutFrames": cdx6500xdlcpTESTOutFrames,
       "cdx6500xdlcpXIDNullInFrames": cdx6500xdlcpXIDNullInFrames,
       "cdx6500xdlcpXIDNullOutFrames": cdx6500xdlcpXIDNullOutFrames,
       "cdx6500xdlcpXID0InFrames": cdx6500xdlcpXID0InFrames,
       "cdx6500xdlcpXID0OutFrames": cdx6500xdlcpXID0OutFrames,
       "cdx6500xdlcpXID1InFrames": cdx6500xdlcpXID1InFrames,
       "cdx6500xdlcpXID1OutFrames": cdx6500xdlcpXID1OutFrames,
       "cdx6500xdlcpXID3InFrames": cdx6500xdlcpXID3InFrames,
       "cdx6500xdlcpXID3OutFrames": cdx6500xdlcpXID3OutFrames,
       "cdx6500PSTStationProtocolGroup": cdx6500PSTStationProtocolGroup,
       "cdx6500SPSTXDLCStationTable": cdx6500SPSTXDLCStationTable,
       "cdx6500SPSTXDLCSDLCStnTable": cdx6500SPSTXDLCSDLCStnTable,
       "cdx6500SPSTXDLCSDLCStnEntry": cdx6500SPSTXDLCSDLCStnEntry,
       "cdx6500xdlcsdlcStatsPortNum": cdx6500xdlcsdlcStatsPortNum,
       "cdx6500xdlcsdlcStatsStationNum": cdx6500xdlcsdlcStatsStationNum,
       "cdx6500xdlcsdlcUtilizationIn": cdx6500xdlcsdlcUtilizationIn,
       "cdx6500xdlcsdlcUtilizationOut": cdx6500xdlcsdlcUtilizationOut,
       "cdx6500xdlcsdlcCharInTotal": cdx6500xdlcsdlcCharInTotal,
       "cdx6500xdlcsdlcCharOutTotal": cdx6500xdlcsdlcCharOutTotal,
       "cdx6500xdlcsdlcCharsInPerSec": cdx6500xdlcsdlcCharsInPerSec,
       "cdx6500xdlcsdlcCharsOutPerSec": cdx6500xdlcsdlcCharsOutPerSec,
       "cdx6500xdlcsdlcPacketsQueued": cdx6500xdlcsdlcPacketsQueued,
       "cdx6500xdlcsdlcFrameInTotal": cdx6500xdlcsdlcFrameInTotal,
       "cdx6500xdlcsdlcFrameOutTotal": cdx6500xdlcsdlcFrameOutTotal,
       "cdx6500xdlcsdlcFramesInPerSec": cdx6500xdlcsdlcFramesInPerSec,
       "cdx6500xdlcsdlcFramesOutPerSec": cdx6500xdlcsdlcFramesOutPerSec,
       "cdx6500xdlcsdlcRNRFramesIn": cdx6500xdlcsdlcRNRFramesIn,
       "cdx6500xdlcsdlcRNRFramesOut": cdx6500xdlcsdlcRNRFramesOut,
       "cdx6500xdlcsdlcRRFramesIn": cdx6500xdlcsdlcRRFramesIn,
       "cdx6500xdlcsdlcRRFramesOut": cdx6500xdlcsdlcRRFramesOut,
       "cdx6500xdlcsdlcREJFramesIn": cdx6500xdlcsdlcREJFramesIn,
       "cdx6500xdlcsdlcREJFramesOut": cdx6500xdlcsdlcREJFramesOut,
       "cdx6500xdlcsdlcQLLCState": cdx6500xdlcsdlcQLLCState,
       "cdx6500xdlcsdlcQRRIn": cdx6500xdlcsdlcQRRIn,
       "cdx6500xdlcsdlcQRROut": cdx6500xdlcsdlcQRROut,
       "cdx6500xdlcsdlcSNRMInFrames": cdx6500xdlcsdlcSNRMInFrames,
       "cdx6500xdlcsdlcSNRMOutFrames": cdx6500xdlcsdlcSNRMOutFrames,
       "cdx6500xdlcsdlcUAInFrames": cdx6500xdlcsdlcUAInFrames,
       "cdx6500xdlcsdlcUAOutFrames": cdx6500xdlcsdlcUAOutFrames,
       "cdx6500xdlcsdlcDMInFrames": cdx6500xdlcsdlcDMInFrames,
       "cdx6500xdlcsdlcDMOutFrames": cdx6500xdlcsdlcDMOutFrames,
       "cdx6500xdlcsdlcXIDInFrames": cdx6500xdlcsdlcXIDInFrames,
       "cdx6500xdlcsdlcXIDOutFrames": cdx6500xdlcsdlcXIDOutFrames,
       "cdx6500xdlcsdlcDISCInFrames": cdx6500xdlcsdlcDISCInFrames,
       "cdx6500xdlcsdlcDISCOutFrames": cdx6500xdlcsdlcDISCOutFrames,
       "cdx6500xdlcsdlcRDInFrames": cdx6500xdlcsdlcRDInFrames,
       "cdx6500xdlcsdlcRDOutFrames": cdx6500xdlcsdlcRDOutFrames,
       "cdx6500xdlcsdlcFRMRInFrames": cdx6500xdlcsdlcFRMRInFrames,
       "cdx6500xdlcsdlcFRMROutFrames": cdx6500xdlcsdlcFRMROutFrames,
       "cdx6500xdlcsdlcUPInFrames": cdx6500xdlcsdlcUPInFrames,
       "cdx6500xdlcsdlcUPOutFrames": cdx6500xdlcsdlcUPOutFrames,
       "cdx6500xdlcsdlcTESTInFrames": cdx6500xdlcsdlcTESTInFrames,
       "cdx6500xdlcsdlcTESTOutFrames": cdx6500xdlcsdlcTESTOutFrames,
       "cdx6500xdlcsdlcQSMInFrames": cdx6500xdlcsdlcQSMInFrames,
       "cdx6500xdlcsdlcQSMOutFrames": cdx6500xdlcsdlcQSMOutFrames,
       "cdx6500xdlcsdlcQUAInFrames": cdx6500xdlcsdlcQUAInFrames,
       "cdx6500xdlcsdlcQUAOutFrames": cdx6500xdlcsdlcQUAOutFrames,
       "cdx6500xdlcsdlcQRDInFrames": cdx6500xdlcsdlcQRDInFrames,
       "cdx6500xdlcsdlcQRDOutFrames": cdx6500xdlcsdlcQRDOutFrames,
       "cdx6500xdlcsdlcQFRMRInFrames": cdx6500xdlcsdlcQFRMRInFrames,
       "cdx6500xdlcsdlcQFRMROutFrames": cdx6500xdlcsdlcQFRMROutFrames,
       "cdx6500xdlcsdlcQXIDInFrames": cdx6500xdlcsdlcQXIDInFrames,
       "cdx6500xdlcsdlcQXIDOutFrames": cdx6500xdlcsdlcQXIDOutFrames,
       "cdx6500xdlcsdlcQDCInFrames": cdx6500xdlcsdlcQDCInFrames,
       "cdx6500xdlcsdlcQDCOutFrames": cdx6500xdlcsdlcQDCOutFrames,
       "cdx6500xdlcsdlcQDMInFrames": cdx6500xdlcsdlcQDMInFrames,
       "cdx6500xdlcsdlcQDMOutFrames": cdx6500xdlcsdlcQDMOutFrames,
       "cdx6500xdlcsdlcQTESTInFrames": cdx6500xdlcsdlcQTESTInFrames,
       "cdx6500xdlcsdlcQTESTOutFrames": cdx6500xdlcsdlcQTESTOutFrames,
       "cdx6500xdlcsdlcQSSInFrames": cdx6500xdlcsdlcQSSInFrames,
       "cdx6500xdlcsdlcQSSOutFrames": cdx6500xdlcsdlcQSSOutFrames,
       "cdx6500xdlcsdlcQRSInFrames": cdx6500xdlcsdlcQRSInFrames,
       "cdx6500xdlcsdlcQRSOutFrames": cdx6500xdlcsdlcQRSOutFrames,
       "cdx6500xdlcsdlcXIDNullInFrames": cdx6500xdlcsdlcXIDNullInFrames,
       "cdx6500xdlcsdlcXIDNullOutFrames": cdx6500xdlcsdlcXIDNullOutFrames,
       "cdx6500xdlcsdlcXID0InFrames": cdx6500xdlcsdlcXID0InFrames,
       "cdx6500xdlcsdlcXID0OutFrames": cdx6500xdlcsdlcXID0OutFrames,
       "cdx6500xdlcsdlcXID1InFrames": cdx6500xdlcsdlcXID1InFrames,
       "cdx6500xdlcsdlcXID1OutFrames": cdx6500xdlcsdlcXID1OutFrames,
       "cdx6500xdlcsdlcXID3InFrames": cdx6500xdlcsdlcXID3InFrames,
       "cdx6500xdlcsdlcXID3OutFrames": cdx6500xdlcsdlcXID3OutFrames,
       "cdx6500xdlcsdlcVSNumber": cdx6500xdlcsdlcVSNumber,
       "cdx6500xdlcsdlcVRNumber": cdx6500xdlcsdlcVRNumber,
       "cdx6500xdlcsdlcNRNumber": cdx6500xdlcsdlcNRNumber,
       "cdx6500xdlcsdlcNSNumber": cdx6500xdlcsdlcNSNumber,
       "cdx6500SPSTXDLCMX25StnTable": cdx6500SPSTXDLCMX25StnTable,
       "cdx6500SPSTXDLCMX25StnEntry": cdx6500SPSTXDLCMX25StnEntry,
       "cdx6500xdlcmx25StatsPortNum": cdx6500xdlcmx25StatsPortNum,
       "cdx6500xdlcmx25StatsStationNum": cdx6500xdlcmx25StatsStationNum,
       "cdx6500xdlcmx25UtilizationIn": cdx6500xdlcmx25UtilizationIn,
       "cdx6500xdlcmx25UtilizationOut": cdx6500xdlcmx25UtilizationOut,
       "cdx6500xdlcmx25CharInTotal": cdx6500xdlcmx25CharInTotal,
       "cdx6500xdlcmx25CharOutTotal": cdx6500xdlcmx25CharOutTotal,
       "cdx6500xdlcmx25CharsInPerSec": cdx6500xdlcmx25CharsInPerSec,
       "cdx6500xdlcmx25CharsOutPerSec": cdx6500xdlcmx25CharsOutPerSec,
       "cdx6500xdlcmx25PktInTotal": cdx6500xdlcmx25PktInTotal,
       "cdx6500xdlcmx25PktOutTotal": cdx6500xdlcmx25PktOutTotal,
       "cdx6500xdlcmx25PktsInPerSec": cdx6500xdlcmx25PktsInPerSec,
       "cdx6500xdlcmx25PktsOutPerSec": cdx6500xdlcmx25PktsOutPerSec,
       "cdx6500xdlcmx25PacketsQueued": cdx6500xdlcmx25PacketsQueued,
       "cdx6500xdlcmx25FrameInTotal": cdx6500xdlcmx25FrameInTotal,
       "cdx6500xdlcmx25FrameOutTotal": cdx6500xdlcmx25FrameOutTotal,
       "cdx6500xdlcmx25FramesInPerSec": cdx6500xdlcmx25FramesInPerSec,
       "cdx6500xdlcmx25FramesOutPerSec": cdx6500xdlcmx25FramesOutPerSec,
       "cdx6500xdlcmx25RNRFramesIn": cdx6500xdlcmx25RNRFramesIn,
       "cdx6500xdlcmx25RNRFramesOut": cdx6500xdlcmx25RNRFramesOut,
       "cdx6500xdlcmx25RRFramesIn": cdx6500xdlcmx25RRFramesIn,
       "cdx6500xdlcmx25RRFramesOut": cdx6500xdlcmx25RRFramesOut,
       "cdx6500xdlcmx25REJFramesIn": cdx6500xdlcmx25REJFramesIn,
       "cdx6500xdlcmx25REJFramesOut": cdx6500xdlcmx25REJFramesOut,
       "cdx6500xdlcmx25DataPktsIn": cdx6500xdlcmx25DataPktsIn,
       "cdx6500xdlcmx25DataPktsOut": cdx6500xdlcmx25DataPktsOut,
       "cdx6500xdlcmx25MaxSVC": cdx6500xdlcmx25MaxSVC,
       "cdx6500xdlcmx25CurrentSVC": cdx6500xdlcmx25CurrentSVC,
       "cdx6500xdlcmx25MaxPVC": cdx6500xdlcmx25MaxPVC,
       "cdx6500xdlcmx25CurrentPVC": cdx6500xdlcmx25CurrentPVC,
       "cdx6500xdlcmx25InfoInFrames": cdx6500xdlcmx25InfoInFrames,
       "cdx6500xdlcmx25InfoOutFrames": cdx6500xdlcmx25InfoOutFrames,
       "cdx6500xdlcmx25SNRMInFrames": cdx6500xdlcmx25SNRMInFrames,
       "cdx6500xdlcmx25SNRMOutFrames": cdx6500xdlcmx25SNRMOutFrames,
       "cdx6500xdlcmx25UAInFrames": cdx6500xdlcmx25UAInFrames,
       "cdx6500xdlcmx25UAOutFrames": cdx6500xdlcmx25UAOutFrames,
       "cdx6500xdlcmx25FRMRInFrames": cdx6500xdlcmx25FRMRInFrames,
       "cdx6500xdlcmx25FRMROutFrames": cdx6500xdlcmx25FRMROutFrames,
       "cdx6500xdlcmx25RRInPkts": cdx6500xdlcmx25RRInPkts,
       "cdx6500xdlcmx25RROutPkts": cdx6500xdlcmx25RROutPkts,
       "cdx6500xdlcmx25RNRInPkts": cdx6500xdlcmx25RNRInPkts,
       "cdx6500xdlcmx25RNROutPkts": cdx6500xdlcmx25RNROutPkts,
       "cdx6500xdlcmx25REJInPkts": cdx6500xdlcmx25REJInPkts,
       "cdx6500xdlcmx25REJOutPkts": cdx6500xdlcmx25REJOutPkts,
       "cdx6500xdlcmx25InCallReqs": cdx6500xdlcmx25InCallReqs,
       "cdx6500xdlcmx25OutCallReqs": cdx6500xdlcmx25OutCallReqs,
       "cdx6500xdlcmx25InCallAccepts": cdx6500xdlcmx25InCallAccepts,
       "cdx6500xdlcmx25OutCallAccepts": cdx6500xdlcmx25OutCallAccepts,
       "cdx6500xdlcmx25InClearReqs": cdx6500xdlcmx25InClearReqs,
       "cdx6500xdlcmx25OutClearReqs": cdx6500xdlcmx25OutClearReqs,
       "cdx6500xdlcmx25InClearConfs": cdx6500xdlcmx25InClearConfs,
       "cdx6500xdlcmx25OutClearConfs": cdx6500xdlcmx25OutClearConfs,
       "cdx6500xdlcmx25InInterruptReqs": cdx6500xdlcmx25InInterruptReqs,
       "cdx6500xdlcmx25OutInterruptReqs": cdx6500xdlcmx25OutInterruptReqs,
       "cdx6500xdlcmx25InInterruptConfs": cdx6500xdlcmx25InInterruptConfs,
       "cdx6500xdlcmx25OutInterruptConfs": cdx6500xdlcmx25OutInterruptConfs,
       "cdx6500xdlcmx25InResetReqs": cdx6500xdlcmx25InResetReqs,
       "cdx6500xdlcmx25OutResetReqs": cdx6500xdlcmx25OutResetReqs,
       "cdx6500xdlcmx25InResetConfs": cdx6500xdlcmx25InResetConfs,
       "cdx6500xdlcmx25OutResetConfs": cdx6500xdlcmx25OutResetConfs,
       "cdx6500xdlcmx25InRestartReqs": cdx6500xdlcmx25InRestartReqs,
       "cdx6500xdlcmx25OutRestartReqs": cdx6500xdlcmx25OutRestartReqs,
       "cdx6500xdlcmx25InRestartConfs": cdx6500xdlcmx25InRestartConfs,
       "cdx6500xdlcmx25OutRestartConfs": cdx6500xdlcmx25OutRestartConfs,
       "cdx6500xdlcmx25LastInLCN": cdx6500xdlcmx25LastInLCN,
       "cdx6500xdlcmx25InStatus": cdx6500xdlcmx25InStatus,
       "cdx6500xdlcmx25LICBPCalledAddr": cdx6500xdlcmx25LICBPCalledAddr,
       "cdx6500xdlcmx25LICBPCallingAddr": cdx6500xdlcmx25LICBPCallingAddr,
       "cdx6500xdlcmx25LICBPFacilities": cdx6500xdlcmx25LICBPFacilities,
       "cdx6500xdlcmx25LICBPCUD": cdx6500xdlcmx25LICBPCUD,
       "cdx6500xdlcmx25LICAPCalledAddr": cdx6500xdlcmx25LICAPCalledAddr,
       "cdx6500xdlcmx25LICAPCallingAddr": cdx6500xdlcmx25LICAPCallingAddr,
       "cdx6500xdlcmx25LICAPFacilities": cdx6500xdlcmx25LICAPFacilities,
       "cdx6500xdlcmx25LICAPCUD": cdx6500xdlcmx25LICAPCUD,
       "cdx6500xdlcmx25LastOutLCN": cdx6500xdlcmx25LastOutLCN,
       "cdx6500xdlcmx25OutStatus": cdx6500xdlcmx25OutStatus,
       "cdx6500xdlcmx25LOCBPCalledAddr": cdx6500xdlcmx25LOCBPCalledAddr,
       "cdx6500xdlcmx25LOCBPCallingAddr": cdx6500xdlcmx25LOCBPCallingAddr,
       "cdx6500xdlcmx25LOCBPFacilities": cdx6500xdlcmx25LOCBPFacilities,
       "cdx6500xdlcmx25LOCBPCUD": cdx6500xdlcmx25LOCBPCUD,
       "cdx6500xdlcmx25LOCAPCalledAddr": cdx6500xdlcmx25LOCAPCalledAddr,
       "cdx6500xdlcmx25LOCAPCallingAddr": cdx6500xdlcmx25LOCAPCallingAddr,
       "cdx6500xdlcmx25LOCAPFacilities": cdx6500xdlcmx25LOCAPFacilities,
       "cdx6500xdlcmx25LOCAPCUD": cdx6500xdlcmx25LOCAPCUD,
       "cdx6500Controls": cdx6500Controls,
       "cdx6500ContXDLC": cdx6500ContXDLC,
       "cdx6500ContXDLCStationTable": cdx6500ContXDLCStationTable,
       "cdx6500ContXDLCStationEntry": cdx6500ContXDLCStationEntry,
       "cdx6500xdlcsContPortNum": cdx6500xdlcsContPortNum,
       "cdx6500xdlcsContStationNum": cdx6500xdlcsContStationNum,
       "cdx6500xdlcsContBootStation": cdx6500xdlcsContBootStation,
       "cdx6500xdlcsContDisableStation": cdx6500xdlcsContDisableStation,
       "cdx6500xdlcsContEnableStation": cdx6500xdlcsContEnableStation,
       "cdx6500xdlcsContResetStnStats": cdx6500xdlcsContResetStnStats}
)
