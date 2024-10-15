# SNMP MIB module (MX25-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MX25-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:12 2024
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
    "enterprises",
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
_Cdx6500PPCTMX25PortTables_ObjectIdentity = ObjectIdentity
cdx6500PPCTMX25PortTables = _Cdx6500PPCTMX25PortTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4)
)
_Cdx6500PPCTMX25PortTable_Object = MibTable
cdx6500PPCTMX25PortTable = _Cdx6500PPCTMX25PortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cdx6500PPCTMX25PortTable.setStatus("mandatory")
_Cdx6500PPCTMX25PortEntry_Object = MibTableRow
cdx6500PPCTMX25PortEntry = _Cdx6500PPCTMX25PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 1, 1)
)
cdx6500PPCTMX25PortEntry.setIndexNames(
    (0, "MX25-OPT-MIB", "cdx6500mx25pCfgPortNum"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTMX25PortEntry.setStatus("mandatory")


class _Cdx6500mx25pCfgPortNum_Type(Integer32):
    """Custom type cdx6500mx25pCfgPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500mx25pCfgPortNum_Type.__name__ = "Integer32"
_Cdx6500mx25pCfgPortNum_Object = MibTableColumn
cdx6500mx25pCfgPortNum = _Cdx6500mx25pCfgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 1, 1, 1),
    _Cdx6500mx25pCfgPortNum_Type()
)
cdx6500mx25pCfgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25pCfgPortNum.setStatus("mandatory")


class _Cdx6500mx25pSubType_Type(Integer32):
    """Custom type cdx6500mx25pSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("newvalMaster", 50),
          ("slave", 1))
    )


_Cdx6500mx25pSubType_Type.__name__ = "Integer32"
_Cdx6500mx25pSubType_Object = MibTableColumn
cdx6500mx25pSubType = _Cdx6500mx25pSubType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 1, 1, 2),
    _Cdx6500mx25pSubType_Type()
)
cdx6500mx25pSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25pSubType.setStatus("mandatory")
_Cdx6500PPCTMX25MPortTable_Object = MibTable
cdx6500PPCTMX25MPortTable = _Cdx6500PPCTMX25MPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cdx6500PPCTMX25MPortTable.setStatus("mandatory")
_Cdx6500PPCTMX25MPortEntry_Object = MibTableRow
cdx6500PPCTMX25MPortEntry = _Cdx6500PPCTMX25MPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 2, 1)
)
cdx6500PPCTMX25MPortEntry.setIndexNames(
    (0, "MX25-OPT-MIB", "cdx6500mx25mpCfgPortNum"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTMX25MPortEntry.setStatus("mandatory")


class _Cdx6500mx25mpCfgPortNum_Type(Integer32):
    """Custom type cdx6500mx25mpCfgPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500mx25mpCfgPortNum_Type.__name__ = "Integer32"
_Cdx6500mx25mpCfgPortNum_Object = MibTableColumn
cdx6500mx25mpCfgPortNum = _Cdx6500mx25mpCfgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 2, 1, 1),
    _Cdx6500mx25mpCfgPortNum_Type()
)
cdx6500mx25mpCfgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25mpCfgPortNum.setStatus("mandatory")


class _Cdx6500mx25mpSubType_Type(Integer32):
    """Custom type cdx6500mx25mpSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              50)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("newvalMaster", 50))
    )


_Cdx6500mx25mpSubType_Type.__name__ = "Integer32"
_Cdx6500mx25mpSubType_Object = MibTableColumn
cdx6500mx25mpSubType = _Cdx6500mx25mpSubType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 2, 1, 2),
    _Cdx6500mx25mpSubType_Type()
)
cdx6500mx25mpSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25mpSubType.setStatus("mandatory")


class _Cdx6500mx25mpClockSource_Type(Integer32):
    """Custom type cdx6500mx25mpClockSource based on Integer32"""
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


_Cdx6500mx25mpClockSource_Type.__name__ = "Integer32"
_Cdx6500mx25mpClockSource_Object = MibTableColumn
cdx6500mx25mpClockSource = _Cdx6500mx25mpClockSource_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 2, 1, 3),
    _Cdx6500mx25mpClockSource_Type()
)
cdx6500mx25mpClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25mpClockSource.setStatus("mandatory")


class _Cdx6500mx25mpClockSpeed_Type(Integer32):
    """Custom type cdx6500mx25mpClockSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 80000),
    )


_Cdx6500mx25mpClockSpeed_Type.__name__ = "Integer32"
_Cdx6500mx25mpClockSpeed_Object = MibTableColumn
cdx6500mx25mpClockSpeed = _Cdx6500mx25mpClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 2, 1, 4),
    _Cdx6500mx25mpClockSpeed_Type()
)
cdx6500mx25mpClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25mpClockSpeed.setStatus("mandatory")


class _Cdx6500mx25mpStationCnt_Type(Integer32):
    """Custom type cdx6500mx25mpStationCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Cdx6500mx25mpStationCnt_Type.__name__ = "Integer32"
_Cdx6500mx25mpStationCnt_Object = MibTableColumn
cdx6500mx25mpStationCnt = _Cdx6500mx25mpStationCnt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 2, 1, 5),
    _Cdx6500mx25mpStationCnt_Type()
)
cdx6500mx25mpStationCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25mpStationCnt.setStatus("mandatory")


class _Cdx6500mx25mpPollTimer_Type(Integer32):
    """Custom type cdx6500mx25mpPollTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500mx25mpPollTimer_Type.__name__ = "Integer32"
_Cdx6500mx25mpPollTimer_Object = MibTableColumn
cdx6500mx25mpPollTimer = _Cdx6500mx25mpPollTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 2, 1, 6),
    _Cdx6500mx25mpPollTimer_Type()
)
cdx6500mx25mpPollTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25mpPollTimer.setStatus("mandatory")


class _Cdx6500mx25mpPollPeriod_Type(Integer32):
    """Custom type cdx6500mx25mpPollPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 250),
    )


_Cdx6500mx25mpPollPeriod_Type.__name__ = "Integer32"
_Cdx6500mx25mpPollPeriod_Object = MibTableColumn
cdx6500mx25mpPollPeriod = _Cdx6500mx25mpPollPeriod_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 2, 1, 7),
    _Cdx6500mx25mpPollPeriod_Type()
)
cdx6500mx25mpPollPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25mpPollPeriod.setStatus("mandatory")


class _Cdx6500mx25mpTries_Type(Integer32):
    """Custom type cdx6500mx25mpTries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Cdx6500mx25mpTries_Type.__name__ = "Integer32"
_Cdx6500mx25mpTries_Object = MibTableColumn
cdx6500mx25mpTries = _Cdx6500mx25mpTries_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 2, 1, 8),
    _Cdx6500mx25mpTries_Type()
)
cdx6500mx25mpTries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25mpTries.setStatus("mandatory")


class _Cdx6500mx25mpRestartTimer_Type(Integer32):
    """Custom type cdx6500mx25mpRestartTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Cdx6500mx25mpRestartTimer_Type.__name__ = "Integer32"
_Cdx6500mx25mpRestartTimer_Object = MibTableColumn
cdx6500mx25mpRestartTimer = _Cdx6500mx25mpRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 2, 1, 9),
    _Cdx6500mx25mpRestartTimer_Type()
)
cdx6500mx25mpRestartTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25mpRestartTimer.setStatus("mandatory")


class _Cdx6500mx25mpResetTimer_Type(Integer32):
    """Custom type cdx6500mx25mpResetTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Cdx6500mx25mpResetTimer_Type.__name__ = "Integer32"
_Cdx6500mx25mpResetTimer_Object = MibTableColumn
cdx6500mx25mpResetTimer = _Cdx6500mx25mpResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 2, 1, 10),
    _Cdx6500mx25mpResetTimer_Type()
)
cdx6500mx25mpResetTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25mpResetTimer.setStatus("mandatory")


class _Cdx6500mx25mpCallTimer_Type(Integer32):
    """Custom type cdx6500mx25mpCallTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 200),
    )


_Cdx6500mx25mpCallTimer_Type.__name__ = "Integer32"
_Cdx6500mx25mpCallTimer_Object = MibTableColumn
cdx6500mx25mpCallTimer = _Cdx6500mx25mpCallTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 2, 1, 11),
    _Cdx6500mx25mpCallTimer_Type()
)
cdx6500mx25mpCallTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25mpCallTimer.setStatus("mandatory")


class _Cdx6500mx25mpClearTimer_Type(Integer32):
    """Custom type cdx6500mx25mpClearTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Cdx6500mx25mpClearTimer_Type.__name__ = "Integer32"
_Cdx6500mx25mpClearTimer_Object = MibTableColumn
cdx6500mx25mpClearTimer = _Cdx6500mx25mpClearTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 2, 1, 12),
    _Cdx6500mx25mpClearTimer_Type()
)
cdx6500mx25mpClearTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25mpClearTimer.setStatus("mandatory")


class _Cdx6500mx25mpPortControl_Type(DisplayString):
    """Custom type cdx6500mx25mpPortControl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 8),
    )


_Cdx6500mx25mpPortControl_Type.__name__ = "DisplayString"
_Cdx6500mx25mpPortControl_Object = MibTableColumn
cdx6500mx25mpPortControl = _Cdx6500mx25mpPortControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 2, 1, 13),
    _Cdx6500mx25mpPortControl_Type()
)
cdx6500mx25mpPortControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25mpPortControl.setStatus("mandatory")


class _Cdx6500mx25mpTXEncoding_Type(Integer32):
    """Custom type cdx6500mx25mpTXEncoding based on Integer32"""
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


_Cdx6500mx25mpTXEncoding_Type.__name__ = "Integer32"
_Cdx6500mx25mpTXEncoding_Object = MibTableColumn
cdx6500mx25mpTXEncoding = _Cdx6500mx25mpTXEncoding_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 2, 1, 14),
    _Cdx6500mx25mpTXEncoding_Type()
)
cdx6500mx25mpTXEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25mpTXEncoding.setStatus("mandatory")


class _Cdx6500mx25mpElectricalInterfaceType_Type(Integer32):
    """Custom type cdx6500mx25mpElectricalInterfaceType based on Integer32"""
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


_Cdx6500mx25mpElectricalInterfaceType_Type.__name__ = "Integer32"
_Cdx6500mx25mpElectricalInterfaceType_Object = MibTableColumn
cdx6500mx25mpElectricalInterfaceType = _Cdx6500mx25mpElectricalInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 2, 1, 15),
    _Cdx6500mx25mpElectricalInterfaceType_Type()
)
cdx6500mx25mpElectricalInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25mpElectricalInterfaceType.setStatus("mandatory")


class _Cdx6500mx25mpV24ElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500mx25mpV24ElectricalInterfaceOption based on Integer32"""
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


_Cdx6500mx25mpV24ElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500mx25mpV24ElectricalInterfaceOption_Object = MibTableColumn
cdx6500mx25mpV24ElectricalInterfaceOption = _Cdx6500mx25mpV24ElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 2, 1, 16),
    _Cdx6500mx25mpV24ElectricalInterfaceOption_Type()
)
cdx6500mx25mpV24ElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25mpV24ElectricalInterfaceOption.setStatus("mandatory")


class _Cdx6500mx25mpHighSpeedElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500mx25mpHighSpeedElectricalInterfaceOption based on Integer32"""
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


_Cdx6500mx25mpHighSpeedElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500mx25mpHighSpeedElectricalInterfaceOption_Object = MibTableColumn
cdx6500mx25mpHighSpeedElectricalInterfaceOption = _Cdx6500mx25mpHighSpeedElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 2, 1, 17),
    _Cdx6500mx25mpHighSpeedElectricalInterfaceOption_Type()
)
cdx6500mx25mpHighSpeedElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25mpHighSpeedElectricalInterfaceOption.setStatus("mandatory")
_Cdx6500PPCTMX25SPortTable_Object = MibTable
cdx6500PPCTMX25SPortTable = _Cdx6500PPCTMX25SPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cdx6500PPCTMX25SPortTable.setStatus("mandatory")
_Cdx6500PPCTMX25SPortEntry_Object = MibTableRow
cdx6500PPCTMX25SPortEntry = _Cdx6500PPCTMX25SPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1)
)
cdx6500PPCTMX25SPortEntry.setIndexNames(
    (0, "MX25-OPT-MIB", "cdx6500mx25spCfgPortNum"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTMX25SPortEntry.setStatus("mandatory")


class _Cdx6500mx25spCfgPortNum_Type(Integer32):
    """Custom type cdx6500mx25spCfgPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500mx25spCfgPortNum_Type.__name__ = "Integer32"
_Cdx6500mx25spCfgPortNum_Object = MibTableColumn
cdx6500mx25spCfgPortNum = _Cdx6500mx25spCfgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 1),
    _Cdx6500mx25spCfgPortNum_Type()
)
cdx6500mx25spCfgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spCfgPortNum.setStatus("mandatory")


class _Cdx6500mx25spSubType_Type(Integer32):
    """Custom type cdx6500mx25spSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("slave", 1)
    )


_Cdx6500mx25spSubType_Type.__name__ = "Integer32"
_Cdx6500mx25spSubType_Object = MibTableColumn
cdx6500mx25spSubType = _Cdx6500mx25spSubType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 2),
    _Cdx6500mx25spSubType_Type()
)
cdx6500mx25spSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spSubType.setStatus("mandatory")


class _Cdx6500mx25spClockSource_Type(Integer32):
    """Custom type cdx6500mx25spClockSource based on Integer32"""
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


_Cdx6500mx25spClockSource_Type.__name__ = "Integer32"
_Cdx6500mx25spClockSource_Object = MibTableColumn
cdx6500mx25spClockSource = _Cdx6500mx25spClockSource_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 3),
    _Cdx6500mx25spClockSource_Type()
)
cdx6500mx25spClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spClockSource.setStatus("mandatory")


class _Cdx6500mx25spClockSpeed_Type(Integer32):
    """Custom type cdx6500mx25spClockSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 80000),
    )


_Cdx6500mx25spClockSpeed_Type.__name__ = "Integer32"
_Cdx6500mx25spClockSpeed_Object = MibTableColumn
cdx6500mx25spClockSpeed = _Cdx6500mx25spClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 4),
    _Cdx6500mx25spClockSpeed_Type()
)
cdx6500mx25spClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spClockSpeed.setStatus("mandatory")


class _Cdx6500mx25spStationAddress_Type(DisplayString):
    """Custom type cdx6500mx25spStationAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_Cdx6500mx25spStationAddress_Type.__name__ = "DisplayString"
_Cdx6500mx25spStationAddress_Object = MibTableColumn
cdx6500mx25spStationAddress = _Cdx6500mx25spStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 5),
    _Cdx6500mx25spStationAddress_Type()
)
cdx6500mx25spStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spStationAddress.setStatus("mandatory")


class _Cdx6500mx25spPVCChannels_Type(Integer32):
    """Custom type cdx6500mx25spPVCChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Cdx6500mx25spPVCChannels_Type.__name__ = "Integer32"
_Cdx6500mx25spPVCChannels_Object = MibTableColumn
cdx6500mx25spPVCChannels = _Cdx6500mx25spPVCChannels_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 6),
    _Cdx6500mx25spPVCChannels_Type()
)
cdx6500mx25spPVCChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spPVCChannels.setStatus("mandatory")


class _Cdx6500mx25spStartingPVC_Type(Integer32):
    """Custom type cdx6500mx25spStartingPVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500mx25spStartingPVC_Type.__name__ = "Integer32"
_Cdx6500mx25spStartingPVC_Object = MibTableColumn
cdx6500mx25spStartingPVC = _Cdx6500mx25spStartingPVC_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 7),
    _Cdx6500mx25spStartingPVC_Type()
)
cdx6500mx25spStartingPVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spStartingPVC.setStatus("mandatory")


class _Cdx6500mx25spSVCChannels_Type(Integer32):
    """Custom type cdx6500mx25spSVCChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500mx25spSVCChannels_Type.__name__ = "Integer32"
_Cdx6500mx25spSVCChannels_Object = MibTableColumn
cdx6500mx25spSVCChannels = _Cdx6500mx25spSVCChannels_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 8),
    _Cdx6500mx25spSVCChannels_Type()
)
cdx6500mx25spSVCChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spSVCChannels.setStatus("mandatory")


class _Cdx6500mx25spStartingSVC_Type(Integer32):
    """Custom type cdx6500mx25spStartingSVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500mx25spStartingSVC_Type.__name__ = "Integer32"
_Cdx6500mx25spStartingSVC_Object = MibTableColumn
cdx6500mx25spStartingSVC = _Cdx6500mx25spStartingSVC_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 9),
    _Cdx6500mx25spStartingSVC_Type()
)
cdx6500mx25spStartingSVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spStartingSVC.setStatus("mandatory")


class _Cdx6500mx25spPollTimer_Type(Integer32):
    """Custom type cdx6500mx25spPollTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500mx25spPollTimer_Type.__name__ = "Integer32"
_Cdx6500mx25spPollTimer_Object = MibTableColumn
cdx6500mx25spPollTimer = _Cdx6500mx25spPollTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 10),
    _Cdx6500mx25spPollTimer_Type()
)
cdx6500mx25spPollTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spPollTimer.setStatus("mandatory")


class _Cdx6500mx25spTries_Type(Integer32):
    """Custom type cdx6500mx25spTries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Cdx6500mx25spTries_Type.__name__ = "Integer32"
_Cdx6500mx25spTries_Object = MibTableColumn
cdx6500mx25spTries = _Cdx6500mx25spTries_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 11),
    _Cdx6500mx25spTries_Type()
)
cdx6500mx25spTries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spTries.setStatus("mandatory")


class _Cdx6500mx25spFrameWinSize_Type(Integer32):
    """Custom type cdx6500mx25spFrameWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Cdx6500mx25spFrameWinSize_Type.__name__ = "Integer32"
_Cdx6500mx25spFrameWinSize_Object = MibTableColumn
cdx6500mx25spFrameWinSize = _Cdx6500mx25spFrameWinSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 12),
    _Cdx6500mx25spFrameWinSize_Type()
)
cdx6500mx25spFrameWinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spFrameWinSize.setStatus("mandatory")


class _Cdx6500mx25spPacketWinSize_Type(Integer32):
    """Custom type cdx6500mx25spPacketWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Cdx6500mx25spPacketWinSize_Type.__name__ = "Integer32"
_Cdx6500mx25spPacketWinSize_Object = MibTableColumn
cdx6500mx25spPacketWinSize = _Cdx6500mx25spPacketWinSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 13),
    _Cdx6500mx25spPacketWinSize_Type()
)
cdx6500mx25spPacketWinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spPacketWinSize.setStatus("mandatory")


class _Cdx6500mx25spRestartTimer_Type(Integer32):
    """Custom type cdx6500mx25spRestartTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Cdx6500mx25spRestartTimer_Type.__name__ = "Integer32"
_Cdx6500mx25spRestartTimer_Object = MibTableColumn
cdx6500mx25spRestartTimer = _Cdx6500mx25spRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 14),
    _Cdx6500mx25spRestartTimer_Type()
)
cdx6500mx25spRestartTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spRestartTimer.setStatus("mandatory")


class _Cdx6500mx25spResetTimer_Type(Integer32):
    """Custom type cdx6500mx25spResetTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Cdx6500mx25spResetTimer_Type.__name__ = "Integer32"
_Cdx6500mx25spResetTimer_Object = MibTableColumn
cdx6500mx25spResetTimer = _Cdx6500mx25spResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 15),
    _Cdx6500mx25spResetTimer_Type()
)
cdx6500mx25spResetTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spResetTimer.setStatus("mandatory")


class _Cdx6500mx25spCallTimer_Type(Integer32):
    """Custom type cdx6500mx25spCallTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 200),
    )


_Cdx6500mx25spCallTimer_Type.__name__ = "Integer32"
_Cdx6500mx25spCallTimer_Object = MibTableColumn
cdx6500mx25spCallTimer = _Cdx6500mx25spCallTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 16),
    _Cdx6500mx25spCallTimer_Type()
)
cdx6500mx25spCallTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spCallTimer.setStatus("mandatory")


class _Cdx6500mx25spClearTimer_Type(Integer32):
    """Custom type cdx6500mx25spClearTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Cdx6500mx25spClearTimer_Type.__name__ = "Integer32"
_Cdx6500mx25spClearTimer_Object = MibTableColumn
cdx6500mx25spClearTimer = _Cdx6500mx25spClearTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 17),
    _Cdx6500mx25spClearTimer_Type()
)
cdx6500mx25spClearTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spClearTimer.setStatus("mandatory")


class _Cdx6500mx25spMX25Options_Type(DisplayString):
    """Custom type cdx6500mx25spMX25Options based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 22),
    )


_Cdx6500mx25spMX25Options_Type.__name__ = "DisplayString"
_Cdx6500mx25spMX25Options_Object = MibTableColumn
cdx6500mx25spMX25Options = _Cdx6500mx25spMX25Options_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 18),
    _Cdx6500mx25spMX25Options_Type()
)
cdx6500mx25spMX25Options.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spMX25Options.setStatus("mandatory")


class _Cdx6500mx25spRCDestination_Type(DisplayString):
    """Custom type cdx6500mx25spRCDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cdx6500mx25spRCDestination_Type.__name__ = "DisplayString"
_Cdx6500mx25spRCDestination_Object = MibTableColumn
cdx6500mx25spRCDestination = _Cdx6500mx25spRCDestination_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 19),
    _Cdx6500mx25spRCDestination_Type()
)
cdx6500mx25spRCDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spRCDestination.setStatus("mandatory")


class _Cdx6500mx25spCUG_Type(DisplayString):
    """Custom type cdx6500mx25spCUG based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_Cdx6500mx25spCUG_Type.__name__ = "DisplayString"
_Cdx6500mx25spCUG_Object = MibTableColumn
cdx6500mx25spCUG = _Cdx6500mx25spCUG_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 20),
    _Cdx6500mx25spCUG_Type()
)
cdx6500mx25spCUG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spCUG.setStatus("mandatory")


class _Cdx6500mx25spBillingRecords_Type(Integer32):
    """Custom type cdx6500mx25spBillingRecords based on Integer32"""
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


_Cdx6500mx25spBillingRecords_Type.__name__ = "Integer32"
_Cdx6500mx25spBillingRecords_Object = MibTableColumn
cdx6500mx25spBillingRecords = _Cdx6500mx25spBillingRecords_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 21),
    _Cdx6500mx25spBillingRecords_Type()
)
cdx6500mx25spBillingRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spBillingRecords.setStatus("mandatory")


class _Cdx6500mx25spPortControl_Type(DisplayString):
    """Custom type cdx6500mx25spPortControl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 8),
    )


_Cdx6500mx25spPortControl_Type.__name__ = "DisplayString"
_Cdx6500mx25spPortControl_Object = MibTableColumn
cdx6500mx25spPortControl = _Cdx6500mx25spPortControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 22),
    _Cdx6500mx25spPortControl_Type()
)
cdx6500mx25spPortControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spPortControl.setStatus("mandatory")


class _Cdx6500mx25spTXEncoding_Type(Integer32):
    """Custom type cdx6500mx25spTXEncoding based on Integer32"""
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


_Cdx6500mx25spTXEncoding_Type.__name__ = "Integer32"
_Cdx6500mx25spTXEncoding_Object = MibTableColumn
cdx6500mx25spTXEncoding = _Cdx6500mx25spTXEncoding_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 23),
    _Cdx6500mx25spTXEncoding_Type()
)
cdx6500mx25spTXEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spTXEncoding.setStatus("mandatory")


class _Cdx6500mx25spUpperQueue_Type(Integer32):
    """Custom type cdx6500mx25spUpperQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 15),
    )


_Cdx6500mx25spUpperQueue_Type.__name__ = "Integer32"
_Cdx6500mx25spUpperQueue_Object = MibTableColumn
cdx6500mx25spUpperQueue = _Cdx6500mx25spUpperQueue_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 24),
    _Cdx6500mx25spUpperQueue_Type()
)
cdx6500mx25spUpperQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spUpperQueue.setStatus("mandatory")


class _Cdx6500mx25spLowerQueue_Type(Integer32):
    """Custom type cdx6500mx25spLowerQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Cdx6500mx25spLowerQueue_Type.__name__ = "Integer32"
_Cdx6500mx25spLowerQueue_Object = MibTableColumn
cdx6500mx25spLowerQueue = _Cdx6500mx25spLowerQueue_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 25),
    _Cdx6500mx25spLowerQueue_Type()
)
cdx6500mx25spLowerQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spLowerQueue.setStatus("mandatory")


class _Cdx6500mx25spElectricalInterfaceType_Type(Integer32):
    """Custom type cdx6500mx25spElectricalInterfaceType based on Integer32"""
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


_Cdx6500mx25spElectricalInterfaceType_Type.__name__ = "Integer32"
_Cdx6500mx25spElectricalInterfaceType_Object = MibTableColumn
cdx6500mx25spElectricalInterfaceType = _Cdx6500mx25spElectricalInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 26),
    _Cdx6500mx25spElectricalInterfaceType_Type()
)
cdx6500mx25spElectricalInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spElectricalInterfaceType.setStatus("mandatory")


class _Cdx6500mx25spV24ElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500mx25spV24ElectricalInterfaceOption based on Integer32"""
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


_Cdx6500mx25spV24ElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500mx25spV24ElectricalInterfaceOption_Object = MibTableColumn
cdx6500mx25spV24ElectricalInterfaceOption = _Cdx6500mx25spV24ElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 27),
    _Cdx6500mx25spV24ElectricalInterfaceOption_Type()
)
cdx6500mx25spV24ElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spV24ElectricalInterfaceOption.setStatus("mandatory")


class _Cdx6500mx25spHighSpeedElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500mx25spHighSpeedElectricalInterfaceOption based on Integer32"""
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


_Cdx6500mx25spHighSpeedElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500mx25spHighSpeedElectricalInterfaceOption_Object = MibTableColumn
cdx6500mx25spHighSpeedElectricalInterfaceOption = _Cdx6500mx25spHighSpeedElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 4, 3, 1, 28),
    _Cdx6500mx25spHighSpeedElectricalInterfaceOption_Type()
)
cdx6500mx25spHighSpeedElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25spHighSpeedElectricalInterfaceOption.setStatus("mandatory")
_Cdx6500PCTStationProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTStationProtocolGroup = _Cdx6500PCTStationProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3)
)
_Cdx6500SPCTMX25StationTable_Object = MibTable
cdx6500SPCTMX25StationTable = _Cdx6500SPCTMX25StationTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cdx6500SPCTMX25StationTable.setStatus("mandatory")
_Cdx6500SPCTMX25StationEntry_Object = MibTableRow
cdx6500SPCTMX25StationEntry = _Cdx6500SPCTMX25StationEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 1, 1)
)
cdx6500SPCTMX25StationEntry.setIndexNames(
    (0, "MX25-OPT-MIB", "cdx6500mx25sCfgPortNum"),
    (0, "MX25-OPT-MIB", "cdx6500mx25sCfgStationNum"),
)
if mibBuilder.loadTexts:
    cdx6500SPCTMX25StationEntry.setStatus("mandatory")


class _Cdx6500mx25sCfgPortNum_Type(Integer32):
    """Custom type cdx6500mx25sCfgPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500mx25sCfgPortNum_Type.__name__ = "Integer32"
_Cdx6500mx25sCfgPortNum_Object = MibTableColumn
cdx6500mx25sCfgPortNum = _Cdx6500mx25sCfgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 1, 1, 1),
    _Cdx6500mx25sCfgPortNum_Type()
)
cdx6500mx25sCfgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sCfgPortNum.setStatus("mandatory")


class _Cdx6500mx25sCfgStationNum_Type(Integer32):
    """Custom type cdx6500mx25sCfgStationNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Cdx6500mx25sCfgStationNum_Type.__name__ = "Integer32"
_Cdx6500mx25sCfgStationNum_Object = MibTableColumn
cdx6500mx25sCfgStationNum = _Cdx6500mx25sCfgStationNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 1, 1, 2),
    _Cdx6500mx25sCfgStationNum_Type()
)
cdx6500mx25sCfgStationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sCfgStationNum.setStatus("mandatory")


class _Cdx6500mx25sStationAddress_Type(DisplayString):
    """Custom type cdx6500mx25sStationAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_Cdx6500mx25sStationAddress_Type.__name__ = "DisplayString"
_Cdx6500mx25sStationAddress_Object = MibTableColumn
cdx6500mx25sStationAddress = _Cdx6500mx25sStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 1, 1, 3),
    _Cdx6500mx25sStationAddress_Type()
)
cdx6500mx25sStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sStationAddress.setStatus("mandatory")


class _Cdx6500mx25sPVCChannels_Type(Integer32):
    """Custom type cdx6500mx25sPVCChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Cdx6500mx25sPVCChannels_Type.__name__ = "Integer32"
_Cdx6500mx25sPVCChannels_Object = MibTableColumn
cdx6500mx25sPVCChannels = _Cdx6500mx25sPVCChannels_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 1, 1, 4),
    _Cdx6500mx25sPVCChannels_Type()
)
cdx6500mx25sPVCChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sPVCChannels.setStatus("mandatory")


class _Cdx6500mx25sStartingPVC_Type(Integer32):
    """Custom type cdx6500mx25sStartingPVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500mx25sStartingPVC_Type.__name__ = "Integer32"
_Cdx6500mx25sStartingPVC_Object = MibTableColumn
cdx6500mx25sStartingPVC = _Cdx6500mx25sStartingPVC_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 1, 1, 5),
    _Cdx6500mx25sStartingPVC_Type()
)
cdx6500mx25sStartingPVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sStartingPVC.setStatus("mandatory")


class _Cdx6500mx25sSVCChannels_Type(Integer32):
    """Custom type cdx6500mx25sSVCChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500mx25sSVCChannels_Type.__name__ = "Integer32"
_Cdx6500mx25sSVCChannels_Object = MibTableColumn
cdx6500mx25sSVCChannels = _Cdx6500mx25sSVCChannels_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 1, 1, 6),
    _Cdx6500mx25sSVCChannels_Type()
)
cdx6500mx25sSVCChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sSVCChannels.setStatus("mandatory")


class _Cdx6500mx25sStartingSVC_Type(Integer32):
    """Custom type cdx6500mx25sStartingSVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500mx25sStartingSVC_Type.__name__ = "Integer32"
_Cdx6500mx25sStartingSVC_Object = MibTableColumn
cdx6500mx25sStartingSVC = _Cdx6500mx25sStartingSVC_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 1, 1, 7),
    _Cdx6500mx25sStartingSVC_Type()
)
cdx6500mx25sStartingSVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sStartingSVC.setStatus("mandatory")


class _Cdx6500mx25sFrameWinSize_Type(Integer32):
    """Custom type cdx6500mx25sFrameWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Cdx6500mx25sFrameWinSize_Type.__name__ = "Integer32"
_Cdx6500mx25sFrameWinSize_Object = MibTableColumn
cdx6500mx25sFrameWinSize = _Cdx6500mx25sFrameWinSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 1, 1, 8),
    _Cdx6500mx25sFrameWinSize_Type()
)
cdx6500mx25sFrameWinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sFrameWinSize.setStatus("mandatory")


class _Cdx6500mx25sPacketWinSize_Type(Integer32):
    """Custom type cdx6500mx25sPacketWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Cdx6500mx25sPacketWinSize_Type.__name__ = "Integer32"
_Cdx6500mx25sPacketWinSize_Object = MibTableColumn
cdx6500mx25sPacketWinSize = _Cdx6500mx25sPacketWinSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 1, 1, 9),
    _Cdx6500mx25sPacketWinSize_Type()
)
cdx6500mx25sPacketWinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sPacketWinSize.setStatus("mandatory")


class _Cdx6500mx25sMX25Options_Type(DisplayString):
    """Custom type cdx6500mx25sMX25Options based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 22),
    )


_Cdx6500mx25sMX25Options_Type.__name__ = "DisplayString"
_Cdx6500mx25sMX25Options_Object = MibTableColumn
cdx6500mx25sMX25Options = _Cdx6500mx25sMX25Options_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 1, 1, 10),
    _Cdx6500mx25sMX25Options_Type()
)
cdx6500mx25sMX25Options.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sMX25Options.setStatus("mandatory")


class _Cdx6500mx25sRCDestination_Type(DisplayString):
    """Custom type cdx6500mx25sRCDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cdx6500mx25sRCDestination_Type.__name__ = "DisplayString"
_Cdx6500mx25sRCDestination_Object = MibTableColumn
cdx6500mx25sRCDestination = _Cdx6500mx25sRCDestination_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 1, 1, 11),
    _Cdx6500mx25sRCDestination_Type()
)
cdx6500mx25sRCDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sRCDestination.setStatus("mandatory")


class _Cdx6500mx25sCUG_Type(DisplayString):
    """Custom type cdx6500mx25sCUG based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_Cdx6500mx25sCUG_Type.__name__ = "DisplayString"
_Cdx6500mx25sCUG_Object = MibTableColumn
cdx6500mx25sCUG = _Cdx6500mx25sCUG_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 1, 1, 12),
    _Cdx6500mx25sCUG_Type()
)
cdx6500mx25sCUG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sCUG.setStatus("mandatory")


class _Cdx6500mx25sBillingRecords_Type(Integer32):
    """Custom type cdx6500mx25sBillingRecords based on Integer32"""
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


_Cdx6500mx25sBillingRecords_Type.__name__ = "Integer32"
_Cdx6500mx25sBillingRecords_Object = MibTableColumn
cdx6500mx25sBillingRecords = _Cdx6500mx25sBillingRecords_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 1, 1, 13),
    _Cdx6500mx25sBillingRecords_Type()
)
cdx6500mx25sBillingRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sBillingRecords.setStatus("mandatory")


class _Cdx6500mx25sUpperQueue_Type(Integer32):
    """Custom type cdx6500mx25sUpperQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 15),
    )


_Cdx6500mx25sUpperQueue_Type.__name__ = "Integer32"
_Cdx6500mx25sUpperQueue_Object = MibTableColumn
cdx6500mx25sUpperQueue = _Cdx6500mx25sUpperQueue_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 1, 1, 14),
    _Cdx6500mx25sUpperQueue_Type()
)
cdx6500mx25sUpperQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sUpperQueue.setStatus("mandatory")


class _Cdx6500mx25sLowerQueue_Type(Integer32):
    """Custom type cdx6500mx25sLowerQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Cdx6500mx25sLowerQueue_Type.__name__ = "Integer32"
_Cdx6500mx25sLowerQueue_Object = MibTableColumn
cdx6500mx25sLowerQueue = _Cdx6500mx25sLowerQueue_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 1, 1, 15),
    _Cdx6500mx25sLowerQueue_Type()
)
cdx6500mx25sLowerQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sLowerQueue.setStatus("mandatory")
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
_Cdx6500PPSTMX25PortTable_Object = MibTable
cdx6500PPSTMX25PortTable = _Cdx6500PPSTMX25PortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cdx6500PPSTMX25PortTable.setStatus("mandatory")
_Cdx6500PPSTMX25PortEntry_Object = MibTableRow
cdx6500PPSTMX25PortEntry = _Cdx6500PPSTMX25PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 4, 1)
)
cdx6500PPSTMX25PortEntry.setIndexNames(
    (0, "MX25-OPT-MIB", "cdx6500mx25pStatsPortNum"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTMX25PortEntry.setStatus("mandatory")


class _Cdx6500mx25pStatsPortNum_Type(Integer32):
    """Custom type cdx6500mx25pStatsPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500mx25pStatsPortNum_Type.__name__ = "Integer32"
_Cdx6500mx25pStatsPortNum_Object = MibTableColumn
cdx6500mx25pStatsPortNum = _Cdx6500mx25pStatsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 4, 1, 1),
    _Cdx6500mx25pStatsPortNum_Type()
)
cdx6500mx25pStatsPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25pStatsPortNum.setStatus("mandatory")


class _Cdx6500mx25pPortStatus_Type(DisplayString):
    """Custom type cdx6500mx25pPortStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 8),
    )


_Cdx6500mx25pPortStatus_Type.__name__ = "DisplayString"
_Cdx6500mx25pPortStatus_Object = MibTableColumn
cdx6500mx25pPortStatus = _Cdx6500mx25pPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 4, 1, 2),
    _Cdx6500mx25pPortStatus_Type()
)
cdx6500mx25pPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25pPortStatus.setStatus("mandatory")
_Cdx6500mx25pPortSpeed_Type = Integer32
_Cdx6500mx25pPortSpeed_Object = MibTableColumn
cdx6500mx25pPortSpeed = _Cdx6500mx25pPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 4, 1, 3),
    _Cdx6500mx25pPortSpeed_Type()
)
cdx6500mx25pPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25pPortSpeed.setStatus("mandatory")
_Cdx6500mx25pCharInTotal_Type = Counter32
_Cdx6500mx25pCharInTotal_Object = MibTableColumn
cdx6500mx25pCharInTotal = _Cdx6500mx25pCharInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 4, 1, 4),
    _Cdx6500mx25pCharInTotal_Type()
)
cdx6500mx25pCharInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25pCharInTotal.setStatus("mandatory")
_Cdx6500mx25pCharOutTotal_Type = Counter32
_Cdx6500mx25pCharOutTotal_Object = MibTableColumn
cdx6500mx25pCharOutTotal = _Cdx6500mx25pCharOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 4, 1, 5),
    _Cdx6500mx25pCharOutTotal_Type()
)
cdx6500mx25pCharOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25pCharOutTotal.setStatus("mandatory")
_Cdx6500mx25pCharsInPerSec_Type = Integer32
_Cdx6500mx25pCharsInPerSec_Object = MibTableColumn
cdx6500mx25pCharsInPerSec = _Cdx6500mx25pCharsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 4, 1, 6),
    _Cdx6500mx25pCharsInPerSec_Type()
)
cdx6500mx25pCharsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25pCharsInPerSec.setStatus("mandatory")
_Cdx6500mx25pCharsOutPerSec_Type = Integer32
_Cdx6500mx25pCharsOutPerSec_Object = MibTableColumn
cdx6500mx25pCharsOutPerSec = _Cdx6500mx25pCharsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 4, 1, 7),
    _Cdx6500mx25pCharsOutPerSec_Type()
)
cdx6500mx25pCharsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25pCharsOutPerSec.setStatus("mandatory")
_Cdx6500mx25pFrameInTotal_Type = Counter32
_Cdx6500mx25pFrameInTotal_Object = MibTableColumn
cdx6500mx25pFrameInTotal = _Cdx6500mx25pFrameInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 4, 1, 8),
    _Cdx6500mx25pFrameInTotal_Type()
)
cdx6500mx25pFrameInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25pFrameInTotal.setStatus("mandatory")
_Cdx6500mx25pFrameOutTotal_Type = Counter32
_Cdx6500mx25pFrameOutTotal_Object = MibTableColumn
cdx6500mx25pFrameOutTotal = _Cdx6500mx25pFrameOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 4, 1, 9),
    _Cdx6500mx25pFrameOutTotal_Type()
)
cdx6500mx25pFrameOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25pFrameOutTotal.setStatus("mandatory")
_Cdx6500mx25pFramesInPerSec_Type = Integer32
_Cdx6500mx25pFramesInPerSec_Object = MibTableColumn
cdx6500mx25pFramesInPerSec = _Cdx6500mx25pFramesInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 4, 1, 10),
    _Cdx6500mx25pFramesInPerSec_Type()
)
cdx6500mx25pFramesInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25pFramesInPerSec.setStatus("mandatory")
_Cdx6500mx25pFramesOutPerSec_Type = Integer32
_Cdx6500mx25pFramesOutPerSec_Object = MibTableColumn
cdx6500mx25pFramesOutPerSec = _Cdx6500mx25pFramesOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 4, 1, 11),
    _Cdx6500mx25pFramesOutPerSec_Type()
)
cdx6500mx25pFramesOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25pFramesOutPerSec.setStatus("mandatory")
_Cdx6500PSTStationProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTStationProtocolGroup = _Cdx6500PSTStationProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3)
)
_Cdx6500SPSTMX25StationTable_Object = MibTable
cdx6500SPSTMX25StationTable = _Cdx6500SPSTMX25StationTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cdx6500SPSTMX25StationTable.setStatus("mandatory")
_Cdx6500SPSTMX25StationEntry_Object = MibTableRow
cdx6500SPSTMX25StationEntry = _Cdx6500SPSTMX25StationEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 1, 1)
)
cdx6500SPSTMX25StationEntry.setIndexNames(
    (0, "MX25-OPT-MIB", "cdx6500mx25sStatsPortNum"),
    (0, "MX25-OPT-MIB", "cdx6500mx25sStatsStationNum"),
)
if mibBuilder.loadTexts:
    cdx6500SPSTMX25StationEntry.setStatus("mandatory")


class _Cdx6500mx25sStatsPortNum_Type(Integer32):
    """Custom type cdx6500mx25sStatsPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500mx25sStatsPortNum_Type.__name__ = "Integer32"
_Cdx6500mx25sStatsPortNum_Object = MibTableColumn
cdx6500mx25sStatsPortNum = _Cdx6500mx25sStatsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 1, 1, 1),
    _Cdx6500mx25sStatsPortNum_Type()
)
cdx6500mx25sStatsPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sStatsPortNum.setStatus("mandatory")


class _Cdx6500mx25sStatsStationNum_Type(Integer32):
    """Custom type cdx6500mx25sStatsStationNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Cdx6500mx25sStatsStationNum_Type.__name__ = "Integer32"
_Cdx6500mx25sStatsStationNum_Object = MibTableColumn
cdx6500mx25sStatsStationNum = _Cdx6500mx25sStatsStationNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 1, 1, 2),
    _Cdx6500mx25sStatsStationNum_Type()
)
cdx6500mx25sStatsStationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sStatsStationNum.setStatus("mandatory")


class _Cdx6500mx25sStatsStnAddr_Type(DisplayString):
    """Custom type cdx6500mx25sStatsStnAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_Cdx6500mx25sStatsStnAddr_Type.__name__ = "DisplayString"
_Cdx6500mx25sStatsStnAddr_Object = MibTableColumn
cdx6500mx25sStatsStnAddr = _Cdx6500mx25sStatsStnAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 1, 1, 3),
    _Cdx6500mx25sStatsStnAddr_Type()
)
cdx6500mx25sStatsStnAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sStatsStnAddr.setStatus("mandatory")
_Cdx6500mx25sCharInTotal_Type = Counter32
_Cdx6500mx25sCharInTotal_Object = MibTableColumn
cdx6500mx25sCharInTotal = _Cdx6500mx25sCharInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 1, 1, 4),
    _Cdx6500mx25sCharInTotal_Type()
)
cdx6500mx25sCharInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sCharInTotal.setStatus("mandatory")
_Cdx6500mx25sCharOutTotal_Type = Counter32
_Cdx6500mx25sCharOutTotal_Object = MibTableColumn
cdx6500mx25sCharOutTotal = _Cdx6500mx25sCharOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 1, 1, 5),
    _Cdx6500mx25sCharOutTotal_Type()
)
cdx6500mx25sCharOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sCharOutTotal.setStatus("mandatory")
_Cdx6500mx25sCharsInPerSec_Type = Integer32
_Cdx6500mx25sCharsInPerSec_Object = MibTableColumn
cdx6500mx25sCharsInPerSec = _Cdx6500mx25sCharsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 1, 1, 6),
    _Cdx6500mx25sCharsInPerSec_Type()
)
cdx6500mx25sCharsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sCharsInPerSec.setStatus("mandatory")
_Cdx6500mx25sCharsOutPerSec_Type = Integer32
_Cdx6500mx25sCharsOutPerSec_Object = MibTableColumn
cdx6500mx25sCharsOutPerSec = _Cdx6500mx25sCharsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 1, 1, 7),
    _Cdx6500mx25sCharsOutPerSec_Type()
)
cdx6500mx25sCharsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sCharsOutPerSec.setStatus("mandatory")
_Cdx6500mx25sFrameInTotal_Type = Counter32
_Cdx6500mx25sFrameInTotal_Object = MibTableColumn
cdx6500mx25sFrameInTotal = _Cdx6500mx25sFrameInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 1, 1, 8),
    _Cdx6500mx25sFrameInTotal_Type()
)
cdx6500mx25sFrameInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sFrameInTotal.setStatus("mandatory")
_Cdx6500mx25sFrameOutTotal_Type = Counter32
_Cdx6500mx25sFrameOutTotal_Object = MibTableColumn
cdx6500mx25sFrameOutTotal = _Cdx6500mx25sFrameOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 1, 1, 9),
    _Cdx6500mx25sFrameOutTotal_Type()
)
cdx6500mx25sFrameOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sFrameOutTotal.setStatus("mandatory")
_Cdx6500mx25sFramesInPerSec_Type = Integer32
_Cdx6500mx25sFramesInPerSec_Object = MibTableColumn
cdx6500mx25sFramesInPerSec = _Cdx6500mx25sFramesInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 1, 1, 10),
    _Cdx6500mx25sFramesInPerSec_Type()
)
cdx6500mx25sFramesInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sFramesInPerSec.setStatus("mandatory")
_Cdx6500mx25sFramesOutPerSec_Type = Integer32
_Cdx6500mx25sFramesOutPerSec_Object = MibTableColumn
cdx6500mx25sFramesOutPerSec = _Cdx6500mx25sFramesOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 1, 1, 11),
    _Cdx6500mx25sFramesOutPerSec_Type()
)
cdx6500mx25sFramesOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sFramesOutPerSec.setStatus("mandatory")
_Cdx6500mx25sCallCount_Type = Integer32
_Cdx6500mx25sCallCount_Object = MibTableColumn
cdx6500mx25sCallCount = _Cdx6500mx25sCallCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 1, 1, 12),
    _Cdx6500mx25sCallCount_Type()
)
cdx6500mx25sCallCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mx25sCallCount.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)
_Cdx6500ContMX25_ObjectIdentity = ObjectIdentity
cdx6500ContMX25 = _Cdx6500ContMX25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 6)
)
_Cdx6500ContMX25StationTable_Object = MibTable
cdx6500ContMX25StationTable = _Cdx6500ContMX25StationTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 6, 1)
)
if mibBuilder.loadTexts:
    cdx6500ContMX25StationTable.setStatus("mandatory")
_Cdx6500ContMX25StationEntry_Object = MibTableRow
cdx6500ContMX25StationEntry = _Cdx6500ContMX25StationEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 6, 1, 1)
)
cdx6500ContMX25StationEntry.setIndexNames(
    (0, "MX25-OPT-MIB", "cdx6500mx25sContPortNum"),
    (0, "MX25-OPT-MIB", "cdx6500mx25sContStationNum"),
)
if mibBuilder.loadTexts:
    cdx6500ContMX25StationEntry.setStatus("mandatory")


class _Cdx6500mx25sContPortNum_Type(Integer32):
    """Custom type cdx6500mx25sContPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500mx25sContPortNum_Type.__name__ = "Integer32"
_Cdx6500mx25sContPortNum_Object = MibTableColumn
cdx6500mx25sContPortNum = _Cdx6500mx25sContPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 6, 1, 1, 1),
    _Cdx6500mx25sContPortNum_Type()
)
cdx6500mx25sContPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdx6500mx25sContPortNum.setStatus("mandatory")


class _Cdx6500mx25sContStationNum_Type(Integer32):
    """Custom type cdx6500mx25sContStationNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Cdx6500mx25sContStationNum_Type.__name__ = "Integer32"
_Cdx6500mx25sContStationNum_Object = MibTableColumn
cdx6500mx25sContStationNum = _Cdx6500mx25sContStationNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 6, 1, 1, 2),
    _Cdx6500mx25sContStationNum_Type()
)
cdx6500mx25sContStationNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdx6500mx25sContStationNum.setStatus("mandatory")


class _Cdx6500mx25sContBootStation_Type(Integer32):
    """Custom type cdx6500mx25sContBootStation based on Integer32"""
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


_Cdx6500mx25sContBootStation_Type.__name__ = "Integer32"
_Cdx6500mx25sContBootStation_Object = MibTableColumn
cdx6500mx25sContBootStation = _Cdx6500mx25sContBootStation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 6, 1, 1, 3),
    _Cdx6500mx25sContBootStation_Type()
)
cdx6500mx25sContBootStation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500mx25sContBootStation.setStatus("mandatory")


class _Cdx6500mx25sContDisableStation_Type(Integer32):
    """Custom type cdx6500mx25sContDisableStation based on Integer32"""
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


_Cdx6500mx25sContDisableStation_Type.__name__ = "Integer32"
_Cdx6500mx25sContDisableStation_Object = MibTableColumn
cdx6500mx25sContDisableStation = _Cdx6500mx25sContDisableStation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 6, 1, 1, 4),
    _Cdx6500mx25sContDisableStation_Type()
)
cdx6500mx25sContDisableStation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500mx25sContDisableStation.setStatus("mandatory")


class _Cdx6500mx25sContEnableStation_Type(Integer32):
    """Custom type cdx6500mx25sContEnableStation based on Integer32"""
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


_Cdx6500mx25sContEnableStation_Type.__name__ = "Integer32"
_Cdx6500mx25sContEnableStation_Object = MibTableColumn
cdx6500mx25sContEnableStation = _Cdx6500mx25sContEnableStation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 6, 1, 1, 5),
    _Cdx6500mx25sContEnableStation_Type()
)
cdx6500mx25sContEnableStation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500mx25sContEnableStation.setStatus("mandatory")


class _Cdx6500mx25sContBusyOutStation_Type(Integer32):
    """Custom type cdx6500mx25sContBusyOutStation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("busyOut", 1),
          ("noBusyOut", 2))
    )


_Cdx6500mx25sContBusyOutStation_Type.__name__ = "Integer32"
_Cdx6500mx25sContBusyOutStation_Object = MibTableColumn
cdx6500mx25sContBusyOutStation = _Cdx6500mx25sContBusyOutStation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 6, 1, 1, 6),
    _Cdx6500mx25sContBusyOutStation_Type()
)
cdx6500mx25sContBusyOutStation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500mx25sContBusyOutStation.setStatus("mandatory")


class _Cdx6500mx25sContResetStnStats_Type(Integer32):
    """Custom type cdx6500mx25sContResetStnStats based on Integer32"""
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


_Cdx6500mx25sContResetStnStats_Type.__name__ = "Integer32"
_Cdx6500mx25sContResetStnStats_Object = MibTableColumn
cdx6500mx25sContResetStnStats = _Cdx6500mx25sContResetStnStats_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 6, 1, 1, 7),
    _Cdx6500mx25sContResetStnStats_Type()
)
cdx6500mx25sContResetStnStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500mx25sContResetStnStats.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX25-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PPCTMX25PortTables": cdx6500PPCTMX25PortTables,
       "cdx6500PPCTMX25PortTable": cdx6500PPCTMX25PortTable,
       "cdx6500PPCTMX25PortEntry": cdx6500PPCTMX25PortEntry,
       "cdx6500mx25pCfgPortNum": cdx6500mx25pCfgPortNum,
       "cdx6500mx25pSubType": cdx6500mx25pSubType,
       "cdx6500PPCTMX25MPortTable": cdx6500PPCTMX25MPortTable,
       "cdx6500PPCTMX25MPortEntry": cdx6500PPCTMX25MPortEntry,
       "cdx6500mx25mpCfgPortNum": cdx6500mx25mpCfgPortNum,
       "cdx6500mx25mpSubType": cdx6500mx25mpSubType,
       "cdx6500mx25mpClockSource": cdx6500mx25mpClockSource,
       "cdx6500mx25mpClockSpeed": cdx6500mx25mpClockSpeed,
       "cdx6500mx25mpStationCnt": cdx6500mx25mpStationCnt,
       "cdx6500mx25mpPollTimer": cdx6500mx25mpPollTimer,
       "cdx6500mx25mpPollPeriod": cdx6500mx25mpPollPeriod,
       "cdx6500mx25mpTries": cdx6500mx25mpTries,
       "cdx6500mx25mpRestartTimer": cdx6500mx25mpRestartTimer,
       "cdx6500mx25mpResetTimer": cdx6500mx25mpResetTimer,
       "cdx6500mx25mpCallTimer": cdx6500mx25mpCallTimer,
       "cdx6500mx25mpClearTimer": cdx6500mx25mpClearTimer,
       "cdx6500mx25mpPortControl": cdx6500mx25mpPortControl,
       "cdx6500mx25mpTXEncoding": cdx6500mx25mpTXEncoding,
       "cdx6500mx25mpElectricalInterfaceType": cdx6500mx25mpElectricalInterfaceType,
       "cdx6500mx25mpV24ElectricalInterfaceOption": cdx6500mx25mpV24ElectricalInterfaceOption,
       "cdx6500mx25mpHighSpeedElectricalInterfaceOption": cdx6500mx25mpHighSpeedElectricalInterfaceOption,
       "cdx6500PPCTMX25SPortTable": cdx6500PPCTMX25SPortTable,
       "cdx6500PPCTMX25SPortEntry": cdx6500PPCTMX25SPortEntry,
       "cdx6500mx25spCfgPortNum": cdx6500mx25spCfgPortNum,
       "cdx6500mx25spSubType": cdx6500mx25spSubType,
       "cdx6500mx25spClockSource": cdx6500mx25spClockSource,
       "cdx6500mx25spClockSpeed": cdx6500mx25spClockSpeed,
       "cdx6500mx25spStationAddress": cdx6500mx25spStationAddress,
       "cdx6500mx25spPVCChannels": cdx6500mx25spPVCChannels,
       "cdx6500mx25spStartingPVC": cdx6500mx25spStartingPVC,
       "cdx6500mx25spSVCChannels": cdx6500mx25spSVCChannels,
       "cdx6500mx25spStartingSVC": cdx6500mx25spStartingSVC,
       "cdx6500mx25spPollTimer": cdx6500mx25spPollTimer,
       "cdx6500mx25spTries": cdx6500mx25spTries,
       "cdx6500mx25spFrameWinSize": cdx6500mx25spFrameWinSize,
       "cdx6500mx25spPacketWinSize": cdx6500mx25spPacketWinSize,
       "cdx6500mx25spRestartTimer": cdx6500mx25spRestartTimer,
       "cdx6500mx25spResetTimer": cdx6500mx25spResetTimer,
       "cdx6500mx25spCallTimer": cdx6500mx25spCallTimer,
       "cdx6500mx25spClearTimer": cdx6500mx25spClearTimer,
       "cdx6500mx25spMX25Options": cdx6500mx25spMX25Options,
       "cdx6500mx25spRCDestination": cdx6500mx25spRCDestination,
       "cdx6500mx25spCUG": cdx6500mx25spCUG,
       "cdx6500mx25spBillingRecords": cdx6500mx25spBillingRecords,
       "cdx6500mx25spPortControl": cdx6500mx25spPortControl,
       "cdx6500mx25spTXEncoding": cdx6500mx25spTXEncoding,
       "cdx6500mx25spUpperQueue": cdx6500mx25spUpperQueue,
       "cdx6500mx25spLowerQueue": cdx6500mx25spLowerQueue,
       "cdx6500mx25spElectricalInterfaceType": cdx6500mx25spElectricalInterfaceType,
       "cdx6500mx25spV24ElectricalInterfaceOption": cdx6500mx25spV24ElectricalInterfaceOption,
       "cdx6500mx25spHighSpeedElectricalInterfaceOption": cdx6500mx25spHighSpeedElectricalInterfaceOption,
       "cdx6500PCTStationProtocolGroup": cdx6500PCTStationProtocolGroup,
       "cdx6500SPCTMX25StationTable": cdx6500SPCTMX25StationTable,
       "cdx6500SPCTMX25StationEntry": cdx6500SPCTMX25StationEntry,
       "cdx6500mx25sCfgPortNum": cdx6500mx25sCfgPortNum,
       "cdx6500mx25sCfgStationNum": cdx6500mx25sCfgStationNum,
       "cdx6500mx25sStationAddress": cdx6500mx25sStationAddress,
       "cdx6500mx25sPVCChannels": cdx6500mx25sPVCChannels,
       "cdx6500mx25sStartingPVC": cdx6500mx25sStartingPVC,
       "cdx6500mx25sSVCChannels": cdx6500mx25sSVCChannels,
       "cdx6500mx25sStartingSVC": cdx6500mx25sStartingSVC,
       "cdx6500mx25sFrameWinSize": cdx6500mx25sFrameWinSize,
       "cdx6500mx25sPacketWinSize": cdx6500mx25sPacketWinSize,
       "cdx6500mx25sMX25Options": cdx6500mx25sMX25Options,
       "cdx6500mx25sRCDestination": cdx6500mx25sRCDestination,
       "cdx6500mx25sCUG": cdx6500mx25sCUG,
       "cdx6500mx25sBillingRecords": cdx6500mx25sBillingRecords,
       "cdx6500mx25sUpperQueue": cdx6500mx25sUpperQueue,
       "cdx6500mx25sLowerQueue": cdx6500mx25sLowerQueue,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPSTMX25PortTable": cdx6500PPSTMX25PortTable,
       "cdx6500PPSTMX25PortEntry": cdx6500PPSTMX25PortEntry,
       "cdx6500mx25pStatsPortNum": cdx6500mx25pStatsPortNum,
       "cdx6500mx25pPortStatus": cdx6500mx25pPortStatus,
       "cdx6500mx25pPortSpeed": cdx6500mx25pPortSpeed,
       "cdx6500mx25pCharInTotal": cdx6500mx25pCharInTotal,
       "cdx6500mx25pCharOutTotal": cdx6500mx25pCharOutTotal,
       "cdx6500mx25pCharsInPerSec": cdx6500mx25pCharsInPerSec,
       "cdx6500mx25pCharsOutPerSec": cdx6500mx25pCharsOutPerSec,
       "cdx6500mx25pFrameInTotal": cdx6500mx25pFrameInTotal,
       "cdx6500mx25pFrameOutTotal": cdx6500mx25pFrameOutTotal,
       "cdx6500mx25pFramesInPerSec": cdx6500mx25pFramesInPerSec,
       "cdx6500mx25pFramesOutPerSec": cdx6500mx25pFramesOutPerSec,
       "cdx6500PSTStationProtocolGroup": cdx6500PSTStationProtocolGroup,
       "cdx6500SPSTMX25StationTable": cdx6500SPSTMX25StationTable,
       "cdx6500SPSTMX25StationEntry": cdx6500SPSTMX25StationEntry,
       "cdx6500mx25sStatsPortNum": cdx6500mx25sStatsPortNum,
       "cdx6500mx25sStatsStationNum": cdx6500mx25sStatsStationNum,
       "cdx6500mx25sStatsStnAddr": cdx6500mx25sStatsStnAddr,
       "cdx6500mx25sCharInTotal": cdx6500mx25sCharInTotal,
       "cdx6500mx25sCharOutTotal": cdx6500mx25sCharOutTotal,
       "cdx6500mx25sCharsInPerSec": cdx6500mx25sCharsInPerSec,
       "cdx6500mx25sCharsOutPerSec": cdx6500mx25sCharsOutPerSec,
       "cdx6500mx25sFrameInTotal": cdx6500mx25sFrameInTotal,
       "cdx6500mx25sFrameOutTotal": cdx6500mx25sFrameOutTotal,
       "cdx6500mx25sFramesInPerSec": cdx6500mx25sFramesInPerSec,
       "cdx6500mx25sFramesOutPerSec": cdx6500mx25sFramesOutPerSec,
       "cdx6500mx25sCallCount": cdx6500mx25sCallCount,
       "cdx6500Controls": cdx6500Controls,
       "cdx6500ContMX25": cdx6500ContMX25,
       "cdx6500ContMX25StationTable": cdx6500ContMX25StationTable,
       "cdx6500ContMX25StationEntry": cdx6500ContMX25StationEntry,
       "cdx6500mx25sContPortNum": cdx6500mx25sContPortNum,
       "cdx6500mx25sContStationNum": cdx6500mx25sContStationNum,
       "cdx6500mx25sContBootStation": cdx6500mx25sContBootStation,
       "cdx6500mx25sContDisableStation": cdx6500mx25sContDisableStation,
       "cdx6500mx25sContEnableStation": cdx6500mx25sContEnableStation,
       "cdx6500mx25sContBusyOutStation": cdx6500mx25sContBusyOutStation,
       "cdx6500mx25sContResetStnStats": cdx6500mx25sContResetStnStats}
)
