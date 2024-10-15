# SNMP MIB module (TDLC-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TDLC-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:01 2024
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
_Cdx6500PPCTTDLCPortTable_Object = MibTable
cdx6500PPCTTDLCPortTable = _Cdx6500PPCTTDLCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 33)
)
if mibBuilder.loadTexts:
    cdx6500PPCTTDLCPortTable.setStatus("mandatory")
_Cdx6500PPCTTDLCPortEntry_Object = MibTableRow
cdx6500PPCTTDLCPortEntry = _Cdx6500PPCTTDLCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 33, 1)
)
cdx6500PPCTTDLCPortEntry.setIndexNames(
    (0, "TDLC-OPT-MIB", "tdlcPCfgPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTTDLCPortEntry.setStatus("mandatory")


class _TdlcPCfgPortNumber_Type(Integer32):
    """Custom type tdlcPCfgPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_TdlcPCfgPortNumber_Type.__name__ = "Integer32"
_TdlcPCfgPortNumber_Object = MibTableColumn
tdlcPCfgPortNumber = _TdlcPCfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 33, 1, 1),
    _TdlcPCfgPortNumber_Type()
)
tdlcPCfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPCfgPortNumber.setStatus("mandatory")


class _TdlcPCfgPortType_Type(Integer32):
    """Custom type tdlcPCfgPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            49
        )
    )
    namedValues = NamedValues(
        ("tdlc", 49)
    )


_TdlcPCfgPortType_Type.__name__ = "Integer32"
_TdlcPCfgPortType_Object = MibTableColumn
tdlcPCfgPortType = _TdlcPCfgPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 33, 1, 2),
    _TdlcPCfgPortType_Type()
)
tdlcPCfgPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPCfgPortType.setStatus("mandatory")


class _TdlcPCfgPortSpeed_Type(Integer32):
    """Custom type tdlcPCfgPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("speed1200", 4),
          ("speed19200", 16),
          ("speed2400", 13),
          ("speed300", 3),
          ("speed4800", 14),
          ("speed9600", 15))
    )


_TdlcPCfgPortSpeed_Type.__name__ = "Integer32"
_TdlcPCfgPortSpeed_Object = MibTableColumn
tdlcPCfgPortSpeed = _TdlcPCfgPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 33, 1, 3),
    _TdlcPCfgPortSpeed_Type()
)
tdlcPCfgPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPCfgPortSpeed.setStatus("mandatory")


class _TdlcPCfgConnType_Type(Integer32):
    """Custom type tdlcPCfgConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("dtr", 2),
          ("nc", 100),
          ("simp", 1))
    )


_TdlcPCfgConnType_Type.__name__ = "Integer32"
_TdlcPCfgConnType_Object = MibTableColumn
tdlcPCfgConnType = _TdlcPCfgConnType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 33, 1, 4),
    _TdlcPCfgConnType_Type()
)
tdlcPCfgConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPCfgConnType.setStatus("mandatory")


class _TdlcPCfgCRCOption_Type(Integer32):
    """Custom type tdlcPCfgCRCOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("nc", 100),
          ("normal", 1),
          ("transp", 2))
    )


_TdlcPCfgCRCOption_Type.__name__ = "Integer32"
_TdlcPCfgCRCOption_Object = MibTableColumn
tdlcPCfgCRCOption = _TdlcPCfgCRCOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 33, 1, 5),
    _TdlcPCfgCRCOption_Type()
)
tdlcPCfgCRCOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPCfgCRCOption.setStatus("mandatory")


class _TdlcPCfgTANControl_Type(Integer32):
    """Custom type tdlcPCfgTANControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("nc", 100),
          ("no", 1),
          ("yes", 2))
    )


_TdlcPCfgTANControl_Type.__name__ = "Integer32"
_TdlcPCfgTANControl_Object = MibTableColumn
tdlcPCfgTANControl = _TdlcPCfgTANControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 33, 1, 6),
    _TdlcPCfgTANControl_Type()
)
tdlcPCfgTANControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPCfgTANControl.setStatus("mandatory")


class _TdlcPCfgPagTerminalID_Type(Integer32):
    """Custom type tdlcPCfgPagTerminalID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_TdlcPCfgPagTerminalID_Type.__name__ = "Integer32"
_TdlcPCfgPagTerminalID_Object = MibTableColumn
tdlcPCfgPagTerminalID = _TdlcPCfgPagTerminalID_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 33, 1, 7),
    _TdlcPCfgPagTerminalID_Type()
)
tdlcPCfgPagTerminalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPCfgPagTerminalID.setStatus("mandatory")


class _TdlcPCfgResponseControl_Type(Integer32):
    """Custom type tdlcPCfgResponseControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("nc", 100),
          ("no", 1),
          ("yes", 2))
    )


_TdlcPCfgResponseControl_Type.__name__ = "Integer32"
_TdlcPCfgResponseControl_Object = MibTableColumn
tdlcPCfgResponseControl = _TdlcPCfgResponseControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 33, 1, 8),
    _TdlcPCfgResponseControl_Type()
)
tdlcPCfgResponseControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPCfgResponseControl.setStatus("mandatory")


class _TdlcPCfgElectricalInterfaceType_Type(Integer32):
    """Custom type tdlcPCfgElectricalInterfaceType based on Integer32"""
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


_TdlcPCfgElectricalInterfaceType_Type.__name__ = "Integer32"
_TdlcPCfgElectricalInterfaceType_Object = MibTableColumn
tdlcPCfgElectricalInterfaceType = _TdlcPCfgElectricalInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 33, 1, 9),
    _TdlcPCfgElectricalInterfaceType_Type()
)
tdlcPCfgElectricalInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPCfgElectricalInterfaceType.setStatus("mandatory")


class _TdlcPCfgV24ElectricalInterfaceOption_Type(Integer32):
    """Custom type tdlcPCfgV24ElectricalInterfaceOption based on Integer32"""
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


_TdlcPCfgV24ElectricalInterfaceOption_Type.__name__ = "Integer32"
_TdlcPCfgV24ElectricalInterfaceOption_Object = MibTableColumn
tdlcPCfgV24ElectricalInterfaceOption = _TdlcPCfgV24ElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 33, 1, 10),
    _TdlcPCfgV24ElectricalInterfaceOption_Type()
)
tdlcPCfgV24ElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPCfgV24ElectricalInterfaceOption.setStatus("mandatory")


class _TdlcPCfgHighSpeedElectricalInterfaceOption_Type(Integer32):
    """Custom type tdlcPCfgHighSpeedElectricalInterfaceOption based on Integer32"""
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


_TdlcPCfgHighSpeedElectricalInterfaceOption_Type.__name__ = "Integer32"
_TdlcPCfgHighSpeedElectricalInterfaceOption_Object = MibTableColumn
tdlcPCfgHighSpeedElectricalInterfaceOption = _TdlcPCfgHighSpeedElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 33, 1, 11),
    _TdlcPCfgHighSpeedElectricalInterfaceOption_Type()
)
tdlcPCfgHighSpeedElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPCfgHighSpeedElectricalInterfaceOption.setStatus("mandatory")
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
_Cdx6500PPSTTDLCPStatTable_ObjectIdentity = ObjectIdentity
cdx6500PPSTTDLCPStatTable = _Cdx6500PPSTTDLCPStatTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34)
)
_TdlcPGenStatTable_Object = MibTable
tdlcPGenStatTable = _TdlcPGenStatTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 1)
)
if mibBuilder.loadTexts:
    tdlcPGenStatTable.setStatus("mandatory")
_TdlcPGenStatEntry_Object = MibTableRow
tdlcPGenStatEntry = _TdlcPGenStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 1, 1)
)
tdlcPGenStatEntry.setIndexNames(
    (0, "TDLC-OPT-MIB", "tdlcPGStatPortNumber"),
)
if mibBuilder.loadTexts:
    tdlcPGenStatEntry.setStatus("mandatory")


class _TdlcPGStatPortNumber_Type(Integer32):
    """Custom type tdlcPGStatPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_TdlcPGStatPortNumber_Type.__name__ = "Integer32"
_TdlcPGStatPortNumber_Object = MibTableColumn
tdlcPGStatPortNumber = _TdlcPGStatPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 1, 1, 1),
    _TdlcPGStatPortNumber_Type()
)
tdlcPGStatPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPGStatPortNumber.setStatus("mandatory")


class _TdlcPGStatPortType_Type(Integer32):
    """Custom type tdlcPGStatPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            48
        )
    )
    namedValues = NamedValues(
        ("tdlc", 48)
    )


_TdlcPGStatPortType_Type.__name__ = "Integer32"
_TdlcPGStatPortType_Object = MibTableColumn
tdlcPGStatPortType = _TdlcPGStatPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 1, 1, 2),
    _TdlcPGStatPortType_Type()
)
tdlcPGStatPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPGStatPortType.setStatus("mandatory")


class _TdlcPGStatPortStatus_Type(Integer32):
    """Custom type tdlcPGStatPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("up", 2))
    )


_TdlcPGStatPortStatus_Type.__name__ = "Integer32"
_TdlcPGStatPortStatus_Object = MibTableColumn
tdlcPGStatPortStatus = _TdlcPGStatPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 1, 1, 3),
    _TdlcPGStatPortStatus_Type()
)
tdlcPGStatPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPGStatPortStatus.setStatus("mandatory")
_TdlcPGStatPortSpeed_Type = Integer32
_TdlcPGStatPortSpeed_Object = MibTableColumn
tdlcPGStatPortSpeed = _TdlcPGStatPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 1, 1, 4),
    _TdlcPGStatPortSpeed_Type()
)
tdlcPGStatPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPGStatPortSpeed.setStatus("mandatory")
_TdlcPGStatPortUtilIn_Type = Integer32
_TdlcPGStatPortUtilIn_Object = MibTableColumn
tdlcPGStatPortUtilIn = _TdlcPGStatPortUtilIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 1, 1, 5),
    _TdlcPGStatPortUtilIn_Type()
)
tdlcPGStatPortUtilIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPGStatPortUtilIn.setStatus("mandatory")
_TdlcPGStatPortUtilOut_Type = Integer32
_TdlcPGStatPortUtilOut_Object = MibTableColumn
tdlcPGStatPortUtilOut = _TdlcPGStatPortUtilOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 1, 1, 6),
    _TdlcPGStatPortUtilOut_Type()
)
tdlcPGStatPortUtilOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPGStatPortUtilOut.setStatus("mandatory")
_TdlcPGStatParityErrors_Type = Counter32
_TdlcPGStatParityErrors_Object = MibTableColumn
tdlcPGStatParityErrors = _TdlcPGStatParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 1, 1, 7),
    _TdlcPGStatParityErrors_Type()
)
tdlcPGStatParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPGStatParityErrors.setStatus("mandatory")
_TdlcPGStatOverrunErrors_Type = Counter32
_TdlcPGStatOverrunErrors_Object = MibTableColumn
tdlcPGStatOverrunErrors = _TdlcPGStatOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 1, 1, 8),
    _TdlcPGStatOverrunErrors_Type()
)
tdlcPGStatOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPGStatOverrunErrors.setStatus("mandatory")
_TdlcPGStatFramingErrors_Type = Counter32
_TdlcPGStatFramingErrors_Object = MibTableColumn
tdlcPGStatFramingErrors = _TdlcPGStatFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 1, 1, 9),
    _TdlcPGStatFramingErrors_Type()
)
tdlcPGStatFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPGStatFramingErrors.setStatus("mandatory")
_TdlcPDataSummaryStatTable_Object = MibTable
tdlcPDataSummaryStatTable = _TdlcPDataSummaryStatTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 2)
)
if mibBuilder.loadTexts:
    tdlcPDataSummaryStatTable.setStatus("mandatory")
_TdlcPDataSummaryStatEntry_Object = MibTableRow
tdlcPDataSummaryStatEntry = _TdlcPDataSummaryStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 2, 1)
)
tdlcPDataSummaryStatEntry.setIndexNames(
    (0, "TDLC-OPT-MIB", "tdlcPDSStatPortNumber"),
)
if mibBuilder.loadTexts:
    tdlcPDataSummaryStatEntry.setStatus("mandatory")


class _TdlcPDSStatPortNumber_Type(Integer32):
    """Custom type tdlcPDSStatPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_TdlcPDSStatPortNumber_Type.__name__ = "Integer32"
_TdlcPDSStatPortNumber_Object = MibTableColumn
tdlcPDSStatPortNumber = _TdlcPDSStatPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 2, 1, 1),
    _TdlcPDSStatPortNumber_Type()
)
tdlcPDSStatPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPDSStatPortNumber.setStatus("mandatory")
_TdlcPDSStatTotalCharIn_Type = Counter32
_TdlcPDSStatTotalCharIn_Object = MibTableColumn
tdlcPDSStatTotalCharIn = _TdlcPDSStatTotalCharIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 2, 1, 2),
    _TdlcPDSStatTotalCharIn_Type()
)
tdlcPDSStatTotalCharIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPDSStatTotalCharIn.setStatus("mandatory")
_TdlcPDSStatTotalCharOut_Type = Counter32
_TdlcPDSStatTotalCharOut_Object = MibTableColumn
tdlcPDSStatTotalCharOut = _TdlcPDSStatTotalCharOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 2, 1, 3),
    _TdlcPDSStatTotalCharOut_Type()
)
tdlcPDSStatTotalCharOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPDSStatTotalCharOut.setStatus("mandatory")
_TdlcPDSStatTotalFramesIn_Type = Counter32
_TdlcPDSStatTotalFramesIn_Object = MibTableColumn
tdlcPDSStatTotalFramesIn = _TdlcPDSStatTotalFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 2, 1, 4),
    _TdlcPDSStatTotalFramesIn_Type()
)
tdlcPDSStatTotalFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPDSStatTotalFramesIn.setStatus("mandatory")
_TdlcPDSStatTotalFramesOut_Type = Counter32
_TdlcPDSStatTotalFramesOut_Object = MibTableColumn
tdlcPDSStatTotalFramesOut = _TdlcPDSStatTotalFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 2, 1, 5),
    _TdlcPDSStatTotalFramesOut_Type()
)
tdlcPDSStatTotalFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPDSStatTotalFramesOut.setStatus("mandatory")
_TdlcPDSStatCharInPerSec_Type = Integer32
_TdlcPDSStatCharInPerSec_Object = MibTableColumn
tdlcPDSStatCharInPerSec = _TdlcPDSStatCharInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 2, 1, 6),
    _TdlcPDSStatCharInPerSec_Type()
)
tdlcPDSStatCharInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPDSStatCharInPerSec.setStatus("mandatory")
_TdlcPDSStatCharOutPerSec_Type = Integer32
_TdlcPDSStatCharOutPerSec_Object = MibTableColumn
tdlcPDSStatCharOutPerSec = _TdlcPDSStatCharOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 2, 1, 7),
    _TdlcPDSStatCharOutPerSec_Type()
)
tdlcPDSStatCharOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPDSStatCharOutPerSec.setStatus("mandatory")
_TdlcPDSStatFramesInPerSec_Type = Integer32
_TdlcPDSStatFramesInPerSec_Object = MibTableColumn
tdlcPDSStatFramesInPerSec = _TdlcPDSStatFramesInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 2, 1, 8),
    _TdlcPDSStatFramesInPerSec_Type()
)
tdlcPDSStatFramesInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPDSStatFramesInPerSec.setStatus("mandatory")
_TdlcPDSStatFramesOutPerSec_Type = Integer32
_TdlcPDSStatFramesOutPerSec_Object = MibTableColumn
tdlcPDSStatFramesOutPerSec = _TdlcPDSStatFramesOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 2, 1, 9),
    _TdlcPDSStatFramesOutPerSec_Type()
)
tdlcPDSStatFramesOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPDSStatFramesOutPerSec.setStatus("mandatory")
_TdlcPFrameSummaryStatTable_Object = MibTable
tdlcPFrameSummaryStatTable = _TdlcPFrameSummaryStatTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3)
)
if mibBuilder.loadTexts:
    tdlcPFrameSummaryStatTable.setStatus("mandatory")
_TdlcPFrameSummaryStatEntry_Object = MibTableRow
tdlcPFrameSummaryStatEntry = _TdlcPFrameSummaryStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1)
)
tdlcPFrameSummaryStatEntry.setIndexNames(
    (0, "TDLC-OPT-MIB", "tdlcPFSStatPortNumber"),
)
if mibBuilder.loadTexts:
    tdlcPFrameSummaryStatEntry.setStatus("mandatory")
_TdlcPFSStatPortNumber_Type = Integer32
_TdlcPFSStatPortNumber_Object = MibTableColumn
tdlcPFSStatPortNumber = _TdlcPFSStatPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 1),
    _TdlcPFSStatPortNumber_Type()
)
tdlcPFSStatPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPFSStatPortNumber.setStatus("mandatory")


class _TdlcPFSStatPagTerminalID_Type(Integer32):
    """Custom type tdlcPFSStatPagTerminalID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_TdlcPFSStatPagTerminalID_Type.__name__ = "Integer32"
_TdlcPFSStatPagTerminalID_Object = MibTableColumn
tdlcPFSStatPagTerminalID = _TdlcPFSStatPagTerminalID_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 2),
    _TdlcPFSStatPagTerminalID_Type()
)
tdlcPFSStatPagTerminalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPFSStatPagTerminalID.setStatus("mandatory")


class _TdlcPFSStatLinkState_Type(Integer32):
    """Custom type tdlcPFSStatLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              100)
        )
    )
    namedValues = NamedValues(
        *(("awaitEnqResp", 2),
          ("init", 1),
          ("na", 100),
          ("ready", 3),
          ("transmitting", 4),
          ("trnsmitResponse", 5))
    )


_TdlcPFSStatLinkState_Type.__name__ = "Integer32"
_TdlcPFSStatLinkState_Object = MibTableColumn
tdlcPFSStatLinkState = _TdlcPFSStatLinkState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 3),
    _TdlcPFSStatLinkState_Type()
)
tdlcPFSStatLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPFSStatLinkState.setStatus("mandatory")
_TdlcPFSStatCRCErrors_Type = Counter32
_TdlcPFSStatCRCErrors_Object = MibTableColumn
tdlcPFSStatCRCErrors = _TdlcPFSStatCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 4),
    _TdlcPFSStatCRCErrors_Type()
)
tdlcPFSStatCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPFSStatCRCErrors.setStatus("mandatory")
_TdlcPFSStatLinkFramingErrors_Type = Counter32
_TdlcPFSStatLinkFramingErrors_Object = MibTableColumn
tdlcPFSStatLinkFramingErrors = _TdlcPFSStatLinkFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 5),
    _TdlcPFSStatLinkFramingErrors_Type()
)
tdlcPFSStatLinkFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPFSStatLinkFramingErrors.setStatus("mandatory")
_TdlcPFSStatProtocolErrors_Type = Counter32
_TdlcPFSStatProtocolErrors_Object = MibTableColumn
tdlcPFSStatProtocolErrors = _TdlcPFSStatProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 6),
    _TdlcPFSStatProtocolErrors_Type()
)
tdlcPFSStatProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPFSStatProtocolErrors.setStatus("mandatory")
_TdlcPFSStatENQFramesIn_Type = Counter32
_TdlcPFSStatENQFramesIn_Object = MibTableColumn
tdlcPFSStatENQFramesIn = _TdlcPFSStatENQFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 7),
    _TdlcPFSStatENQFramesIn_Type()
)
tdlcPFSStatENQFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPFSStatENQFramesIn.setStatus("mandatory")
_TdlcPFSStatENQFramesOut_Type = Counter32
_TdlcPFSStatENQFramesOut_Object = MibTableColumn
tdlcPFSStatENQFramesOut = _TdlcPFSStatENQFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 8),
    _TdlcPFSStatENQFramesOut_Type()
)
tdlcPFSStatENQFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPFSStatENQFramesOut.setStatus("mandatory")
_TdlcPFSStatEOTFramesIn_Type = Counter32
_TdlcPFSStatEOTFramesIn_Object = MibTableColumn
tdlcPFSStatEOTFramesIn = _TdlcPFSStatEOTFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 9),
    _TdlcPFSStatEOTFramesIn_Type()
)
tdlcPFSStatEOTFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPFSStatEOTFramesIn.setStatus("mandatory")
_TdlcPFSStatEOTFramesOut_Type = Counter32
_TdlcPFSStatEOTFramesOut_Object = MibTableColumn
tdlcPFSStatEOTFramesOut = _TdlcPFSStatEOTFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 10),
    _TdlcPFSStatEOTFramesOut_Type()
)
tdlcPFSStatEOTFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPFSStatEOTFramesOut.setStatus("mandatory")
_TdlcPFSStatACKFramesIn_Type = Counter32
_TdlcPFSStatACKFramesIn_Object = MibTableColumn
tdlcPFSStatACKFramesIn = _TdlcPFSStatACKFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 11),
    _TdlcPFSStatACKFramesIn_Type()
)
tdlcPFSStatACKFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPFSStatACKFramesIn.setStatus("mandatory")
_TdlcPFSStatACKFramesOut_Type = Counter32
_TdlcPFSStatACKFramesOut_Object = MibTableColumn
tdlcPFSStatACKFramesOut = _TdlcPFSStatACKFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 12),
    _TdlcPFSStatACKFramesOut_Type()
)
tdlcPFSStatACKFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPFSStatACKFramesOut.setStatus("mandatory")
_TdlcPFSStatNAKFramesIn_Type = Counter32
_TdlcPFSStatNAKFramesIn_Object = MibTableColumn
tdlcPFSStatNAKFramesIn = _TdlcPFSStatNAKFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 13),
    _TdlcPFSStatNAKFramesIn_Type()
)
tdlcPFSStatNAKFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPFSStatNAKFramesIn.setStatus("mandatory")
_TdlcPFSStatNAKFramesOut_Type = Counter32
_TdlcPFSStatNAKFramesOut_Object = MibTableColumn
tdlcPFSStatNAKFramesOut = _TdlcPFSStatNAKFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 14),
    _TdlcPFSStatNAKFramesOut_Type()
)
tdlcPFSStatNAKFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPFSStatNAKFramesOut.setStatus("mandatory")
_TdlcPFSStatRSFramesIn_Type = Counter32
_TdlcPFSStatRSFramesIn_Object = MibTableColumn
tdlcPFSStatRSFramesIn = _TdlcPFSStatRSFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 15),
    _TdlcPFSStatRSFramesIn_Type()
)
tdlcPFSStatRSFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPFSStatRSFramesIn.setStatus("mandatory")
_TdlcPFSStatRSFramesOut_Type = Counter32
_TdlcPFSStatRSFramesOut_Object = MibTableColumn
tdlcPFSStatRSFramesOut = _TdlcPFSStatRSFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 16),
    _TdlcPFSStatRSFramesOut_Type()
)
tdlcPFSStatRSFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPFSStatRSFramesOut.setStatus("mandatory")
_TdlcPFSStatCANFramesIn_Type = Counter32
_TdlcPFSStatCANFramesIn_Object = MibTableColumn
tdlcPFSStatCANFramesIn = _TdlcPFSStatCANFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 17),
    _TdlcPFSStatCANFramesIn_Type()
)
tdlcPFSStatCANFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPFSStatCANFramesIn.setStatus("mandatory")
_TdlcPFSStatCANFramesOut_Type = Counter32
_TdlcPFSStatCANFramesOut_Object = MibTableColumn
tdlcPFSStatCANFramesOut = _TdlcPFSStatCANFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 18),
    _TdlcPFSStatCANFramesOut_Type()
)
tdlcPFSStatCANFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPFSStatCANFramesOut.setStatus("mandatory")
_TdlcPFSStatDataFramesInPassed_Type = Counter32
_TdlcPFSStatDataFramesInPassed_Object = MibTableColumn
tdlcPFSStatDataFramesInPassed = _TdlcPFSStatDataFramesInPassed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 19),
    _TdlcPFSStatDataFramesInPassed_Type()
)
tdlcPFSStatDataFramesInPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPFSStatDataFramesInPassed.setStatus("mandatory")
_TdlcPFSStatDataFramesOutPassed_Type = Counter32
_TdlcPFSStatDataFramesOutPassed_Object = MibTableColumn
tdlcPFSStatDataFramesOutPassed = _TdlcPFSStatDataFramesOutPassed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 20),
    _TdlcPFSStatDataFramesOutPassed_Type()
)
tdlcPFSStatDataFramesOutPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPFSStatDataFramesOutPassed.setStatus("mandatory")
_TdlcPFSStatDataFramesInDiscarded_Type = Counter32
_TdlcPFSStatDataFramesInDiscarded_Object = MibTableColumn
tdlcPFSStatDataFramesInDiscarded = _TdlcPFSStatDataFramesInDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 21),
    _TdlcPFSStatDataFramesInDiscarded_Type()
)
tdlcPFSStatDataFramesInDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPFSStatDataFramesInDiscarded.setStatus("mandatory")
_TdlcPFSStatDataFramesOutDiscarded_Type = Counter32
_TdlcPFSStatDataFramesOutDiscarded_Object = MibTableColumn
tdlcPFSStatDataFramesOutDiscarded = _TdlcPFSStatDataFramesOutDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 22),
    _TdlcPFSStatDataFramesOutDiscarded_Type()
)
tdlcPFSStatDataFramesOutDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdlcPFSStatDataFramesOutDiscarded.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)
_Cdx6500ContTDLCTable_ObjectIdentity = ObjectIdentity
cdx6500ContTDLCTable = _Cdx6500ContTDLCTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 16)
)
_Cdx6500ContTDLCPortTable_Object = MibTable
cdx6500ContTDLCPortTable = _Cdx6500ContTDLCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 16, 1)
)
if mibBuilder.loadTexts:
    cdx6500ContTDLCPortTable.setStatus("mandatory")
_Cdx6500ContTDLCPortEntry_Object = MibTableRow
cdx6500ContTDLCPortEntry = _Cdx6500ContTDLCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 16, 1, 1)
)
cdx6500ContTDLCPortEntry.setIndexNames(
    (0, "TDLC-OPT-MIB", "tdlcPContPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500ContTDLCPortEntry.setStatus("mandatory")


class _TdlcPContPortNumber_Type(Integer32):
    """Custom type tdlcPContPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_TdlcPContPortNumber_Type.__name__ = "Integer32"
_TdlcPContPortNumber_Object = MibTableColumn
tdlcPContPortNumber = _TdlcPContPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 16, 1, 1, 1),
    _TdlcPContPortNumber_Type()
)
tdlcPContPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdlcPContPortNumber.setStatus("mandatory")


class _TdlcPContPortControl_Type(Integer32):
    """Custom type tdlcPContPortControl based on Integer32"""
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
        *(("boot", 1),
          ("busyout", 4),
          ("disable", 3),
          ("enable", 2),
          ("resetstats", 5))
    )


_TdlcPContPortControl_Type.__name__ = "Integer32"
_TdlcPContPortControl_Object = MibTableColumn
tdlcPContPortControl = _TdlcPContPortControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 16, 1, 1, 2),
    _TdlcPContPortControl_Type()
)
tdlcPContPortControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tdlcPContPortControl.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TDLC-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PPCTTDLCPortTable": cdx6500PPCTTDLCPortTable,
       "cdx6500PPCTTDLCPortEntry": cdx6500PPCTTDLCPortEntry,
       "tdlcPCfgPortNumber": tdlcPCfgPortNumber,
       "tdlcPCfgPortType": tdlcPCfgPortType,
       "tdlcPCfgPortSpeed": tdlcPCfgPortSpeed,
       "tdlcPCfgConnType": tdlcPCfgConnType,
       "tdlcPCfgCRCOption": tdlcPCfgCRCOption,
       "tdlcPCfgTANControl": tdlcPCfgTANControl,
       "tdlcPCfgPagTerminalID": tdlcPCfgPagTerminalID,
       "tdlcPCfgResponseControl": tdlcPCfgResponseControl,
       "tdlcPCfgElectricalInterfaceType": tdlcPCfgElectricalInterfaceType,
       "tdlcPCfgV24ElectricalInterfaceOption": tdlcPCfgV24ElectricalInterfaceOption,
       "tdlcPCfgHighSpeedElectricalInterfaceOption": tdlcPCfgHighSpeedElectricalInterfaceOption,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPSTTDLCPStatTable": cdx6500PPSTTDLCPStatTable,
       "tdlcPGenStatTable": tdlcPGenStatTable,
       "tdlcPGenStatEntry": tdlcPGenStatEntry,
       "tdlcPGStatPortNumber": tdlcPGStatPortNumber,
       "tdlcPGStatPortType": tdlcPGStatPortType,
       "tdlcPGStatPortStatus": tdlcPGStatPortStatus,
       "tdlcPGStatPortSpeed": tdlcPGStatPortSpeed,
       "tdlcPGStatPortUtilIn": tdlcPGStatPortUtilIn,
       "tdlcPGStatPortUtilOut": tdlcPGStatPortUtilOut,
       "tdlcPGStatParityErrors": tdlcPGStatParityErrors,
       "tdlcPGStatOverrunErrors": tdlcPGStatOverrunErrors,
       "tdlcPGStatFramingErrors": tdlcPGStatFramingErrors,
       "tdlcPDataSummaryStatTable": tdlcPDataSummaryStatTable,
       "tdlcPDataSummaryStatEntry": tdlcPDataSummaryStatEntry,
       "tdlcPDSStatPortNumber": tdlcPDSStatPortNumber,
       "tdlcPDSStatTotalCharIn": tdlcPDSStatTotalCharIn,
       "tdlcPDSStatTotalCharOut": tdlcPDSStatTotalCharOut,
       "tdlcPDSStatTotalFramesIn": tdlcPDSStatTotalFramesIn,
       "tdlcPDSStatTotalFramesOut": tdlcPDSStatTotalFramesOut,
       "tdlcPDSStatCharInPerSec": tdlcPDSStatCharInPerSec,
       "tdlcPDSStatCharOutPerSec": tdlcPDSStatCharOutPerSec,
       "tdlcPDSStatFramesInPerSec": tdlcPDSStatFramesInPerSec,
       "tdlcPDSStatFramesOutPerSec": tdlcPDSStatFramesOutPerSec,
       "tdlcPFrameSummaryStatTable": tdlcPFrameSummaryStatTable,
       "tdlcPFrameSummaryStatEntry": tdlcPFrameSummaryStatEntry,
       "tdlcPFSStatPortNumber": tdlcPFSStatPortNumber,
       "tdlcPFSStatPagTerminalID": tdlcPFSStatPagTerminalID,
       "tdlcPFSStatLinkState": tdlcPFSStatLinkState,
       "tdlcPFSStatCRCErrors": tdlcPFSStatCRCErrors,
       "tdlcPFSStatLinkFramingErrors": tdlcPFSStatLinkFramingErrors,
       "tdlcPFSStatProtocolErrors": tdlcPFSStatProtocolErrors,
       "tdlcPFSStatENQFramesIn": tdlcPFSStatENQFramesIn,
       "tdlcPFSStatENQFramesOut": tdlcPFSStatENQFramesOut,
       "tdlcPFSStatEOTFramesIn": tdlcPFSStatEOTFramesIn,
       "tdlcPFSStatEOTFramesOut": tdlcPFSStatEOTFramesOut,
       "tdlcPFSStatACKFramesIn": tdlcPFSStatACKFramesIn,
       "tdlcPFSStatACKFramesOut": tdlcPFSStatACKFramesOut,
       "tdlcPFSStatNAKFramesIn": tdlcPFSStatNAKFramesIn,
       "tdlcPFSStatNAKFramesOut": tdlcPFSStatNAKFramesOut,
       "tdlcPFSStatRSFramesIn": tdlcPFSStatRSFramesIn,
       "tdlcPFSStatRSFramesOut": tdlcPFSStatRSFramesOut,
       "tdlcPFSStatCANFramesIn": tdlcPFSStatCANFramesIn,
       "tdlcPFSStatCANFramesOut": tdlcPFSStatCANFramesOut,
       "tdlcPFSStatDataFramesInPassed": tdlcPFSStatDataFramesInPassed,
       "tdlcPFSStatDataFramesOutPassed": tdlcPFSStatDataFramesOutPassed,
       "tdlcPFSStatDataFramesInDiscarded": tdlcPFSStatDataFramesInDiscarded,
       "tdlcPFSStatDataFramesOutDiscarded": tdlcPFSStatDataFramesOutDiscarded,
       "cdx6500Controls": cdx6500Controls,
       "cdx6500ContTDLCTable": cdx6500ContTDLCTable,
       "cdx6500ContTDLCPortTable": cdx6500ContTDLCPortTable,
       "cdx6500ContTDLCPortEntry": cdx6500ContTDLCPortEntry,
       "tdlcPContPortNumber": tdlcPContPortNumber,
       "tdlcPContPortControl": tdlcPContPortControl}
)
