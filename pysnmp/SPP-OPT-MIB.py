# SNMP MIB module (SPP-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SPP-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:24 2024
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
_Cdx6500PPCTSPPPortTable_Object = MibTable
cdx6500PPCTSPPPortTable = _Cdx6500PPCTSPPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 30)
)
if mibBuilder.loadTexts:
    cdx6500PPCTSPPPortTable.setStatus("mandatory")
_Cdx6500PPCTSPPPortEntry_Object = MibTableRow
cdx6500PPCTSPPPortEntry = _Cdx6500PPCTSPPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 30, 1)
)
cdx6500PPCTSPPPortEntry.setIndexNames(
    (0, "SPP-OPT-MIB", "cdx6500SPPPCfgPortNum"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTSPPPortEntry.setStatus("mandatory")


class _Cdx6500SPPPCfgPortNum_Type(Integer32):
    """Custom type cdx6500SPPPCfgPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500SPPPCfgPortNum_Type.__name__ = "Integer32"
_Cdx6500SPPPCfgPortNum_Object = MibTableColumn
cdx6500SPPPCfgPortNum = _Cdx6500SPPPCfgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 30, 1, 1),
    _Cdx6500SPPPCfgPortNum_Type()
)
cdx6500SPPPCfgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPCfgPortNum.setStatus("mandatory")


class _Cdx6500SPPPCfgPortType_Type(Integer32):
    """Custom type cdx6500SPPPCfgPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            52
        )
    )
    namedValues = NamedValues(
        ("spp", 52)
    )


_Cdx6500SPPPCfgPortType_Type.__name__ = "Integer32"
_Cdx6500SPPPCfgPortType_Object = MibTableColumn
cdx6500SPPPCfgPortType = _Cdx6500SPPPCfgPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 30, 1, 2),
    _Cdx6500SPPPCfgPortType_Type()
)
cdx6500SPPPCfgPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPCfgPortType.setStatus("mandatory")


class _Cdx6500SPPPCfgPortSpeed_Type(Integer32):
    """Custom type cdx6500SPPPCfgPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              7,
              12,
              13,
              14,
              15,
              98)
        )
    )
    namedValues = NamedValues(
        *(("speed1200", 3),
          ("speed1800", 7),
          ("speed19200", 15),
          ("speed2400", 12),
          ("speed300", 2),
          ("speed4800", 13),
          ("speed600", 4),
          ("speed7200", 98),
          ("speed9600", 14))
    )


_Cdx6500SPPPCfgPortSpeed_Type.__name__ = "Integer32"
_Cdx6500SPPPCfgPortSpeed_Object = MibTableColumn
cdx6500SPPPCfgPortSpeed = _Cdx6500SPPPCfgPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 30, 1, 3),
    _Cdx6500SPPPCfgPortSpeed_Type()
)
cdx6500SPPPCfgPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPCfgPortSpeed.setStatus("mandatory")


class _Cdx6500SPPPCfgInterchTimeout_Type(Integer32):
    """Custom type cdx6500SPPPCfgInterchTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(51,
              100,
              150,
              200,
              250)
        )
    )
    namedValues = NamedValues(
        *(("time100", 100),
          ("time150", 150),
          ("time200", 200),
          ("time250", 250),
          ("time50", 51))
    )


_Cdx6500SPPPCfgInterchTimeout_Type.__name__ = "Integer32"
_Cdx6500SPPPCfgInterchTimeout_Object = MibTableColumn
cdx6500SPPPCfgInterchTimeout = _Cdx6500SPPPCfgInterchTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 30, 1, 4),
    _Cdx6500SPPPCfgInterchTimeout_Type()
)
cdx6500SPPPCfgInterchTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPCfgInterchTimeout.setStatus("mandatory")


class _Cdx6500SPPPCfgSLCNum_Type(Integer32):
    """Custom type cdx6500SPPPCfgSLCNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Cdx6500SPPPCfgSLCNum_Type.__name__ = "Integer32"
_Cdx6500SPPPCfgSLCNum_Object = MibTableColumn
cdx6500SPPPCfgSLCNum = _Cdx6500SPPPCfgSLCNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 30, 1, 5),
    _Cdx6500SPPPCfgSLCNum_Type()
)
cdx6500SPPPCfgSLCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPCfgSLCNum.setStatus("mandatory")


class _Cdx6500SPPPCfgSLCLineNum_Type(Integer32):
    """Custom type cdx6500SPPPCfgSLCLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Cdx6500SPPPCfgSLCLineNum_Type.__name__ = "Integer32"
_Cdx6500SPPPCfgSLCLineNum_Object = MibTableColumn
cdx6500SPPPCfgSLCLineNum = _Cdx6500SPPPCfgSLCLineNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 30, 1, 6),
    _Cdx6500SPPPCfgSLCLineNum_Type()
)
cdx6500SPPPCfgSLCLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPCfgSLCLineNum.setStatus("mandatory")
_Cdx6500SPPPCfgStnIDList_Type = DisplayString
_Cdx6500SPPPCfgStnIDList_Object = MibTableColumn
cdx6500SPPPCfgStnIDList = _Cdx6500SPPPCfgStnIDList_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 30, 1, 7),
    _Cdx6500SPPPCfgStnIDList_Type()
)
cdx6500SPPPCfgStnIDList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPCfgStnIDList.setStatus("mandatory")


class _Cdx6500SPPPCfgProtocolID_Type(DisplayString):
    """Custom type cdx6500SPPPCfgProtocolID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Cdx6500SPPPCfgProtocolID_Type.__name__ = "DisplayString"
_Cdx6500SPPPCfgProtocolID_Object = MibTableColumn
cdx6500SPPPCfgProtocolID = _Cdx6500SPPPCfgProtocolID_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 30, 1, 8),
    _Cdx6500SPPPCfgProtocolID_Type()
)
cdx6500SPPPCfgProtocolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPCfgProtocolID.setStatus("mandatory")


class _Cdx6500SPPPCfgQueueSize_Type(Integer32):
    """Custom type cdx6500SPPPCfgQueueSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_Cdx6500SPPPCfgQueueSize_Type.__name__ = "Integer32"
_Cdx6500SPPPCfgQueueSize_Object = MibTableColumn
cdx6500SPPPCfgQueueSize = _Cdx6500SPPPCfgQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 30, 1, 9),
    _Cdx6500SPPPCfgQueueSize_Type()
)
cdx6500SPPPCfgQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPCfgQueueSize.setStatus("mandatory")


class _Cdx6500SPPPCfgBlockingThresh_Type(Integer32):
    """Custom type cdx6500SPPPCfgBlockingThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_Cdx6500SPPPCfgBlockingThresh_Type.__name__ = "Integer32"
_Cdx6500SPPPCfgBlockingThresh_Object = MibTableColumn
cdx6500SPPPCfgBlockingThresh = _Cdx6500SPPPCfgBlockingThresh_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 30, 1, 10),
    _Cdx6500SPPPCfgBlockingThresh_Type()
)
cdx6500SPPPCfgBlockingThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPCfgBlockingThresh.setStatus("mandatory")


class _Cdx6500SPPPCfgUnblockThresh_Type(Integer32):
    """Custom type cdx6500SPPPCfgUnblockThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_Cdx6500SPPPCfgUnblockThresh_Type.__name__ = "Integer32"
_Cdx6500SPPPCfgUnblockThresh_Object = MibTableColumn
cdx6500SPPPCfgUnblockThresh = _Cdx6500SPPPCfgUnblockThresh_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 30, 1, 11),
    _Cdx6500SPPPCfgUnblockThresh_Type()
)
cdx6500SPPPCfgUnblockThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPCfgUnblockThresh.setStatus("mandatory")


class _Cdx6500SPPPCfgElectricalInterfaceType_Type(Integer32):
    """Custom type cdx6500SPPPCfgElectricalInterfaceType based on Integer32"""
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


_Cdx6500SPPPCfgElectricalInterfaceType_Type.__name__ = "Integer32"
_Cdx6500SPPPCfgElectricalInterfaceType_Object = MibTableColumn
cdx6500SPPPCfgElectricalInterfaceType = _Cdx6500SPPPCfgElectricalInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 30, 1, 12),
    _Cdx6500SPPPCfgElectricalInterfaceType_Type()
)
cdx6500SPPPCfgElectricalInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPCfgElectricalInterfaceType.setStatus("mandatory")


class _Cdx6500SPPPCfgV24ElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500SPPPCfgV24ElectricalInterfaceOption based on Integer32"""
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


_Cdx6500SPPPCfgV24ElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500SPPPCfgV24ElectricalInterfaceOption_Object = MibTableColumn
cdx6500SPPPCfgV24ElectricalInterfaceOption = _Cdx6500SPPPCfgV24ElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 30, 1, 13),
    _Cdx6500SPPPCfgV24ElectricalInterfaceOption_Type()
)
cdx6500SPPPCfgV24ElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPCfgV24ElectricalInterfaceOption.setStatus("mandatory")


class _Cdx6500SPPPCfgHighSpeedElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500SPPPCfgHighSpeedElectricalInterfaceOption based on Integer32"""
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


_Cdx6500SPPPCfgHighSpeedElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500SPPPCfgHighSpeedElectricalInterfaceOption_Object = MibTableColumn
cdx6500SPPPCfgHighSpeedElectricalInterfaceOption = _Cdx6500SPPPCfgHighSpeedElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 30, 1, 14),
    _Cdx6500SPPPCfgHighSpeedElectricalInterfaceOption_Type()
)
cdx6500SPPPCfgHighSpeedElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPCfgHighSpeedElectricalInterfaceOption.setStatus("mandatory")
_Cdx6500PCTStationProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTStationProtocolGroup = _Cdx6500PCTStationProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3)
)
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
_Cdx6500PPSTSPPPStatsTable_Object = MibTable
cdx6500PPSTSPPPStatsTable = _Cdx6500PPSTSPPPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 31)
)
if mibBuilder.loadTexts:
    cdx6500PPSTSPPPStatsTable.setStatus("mandatory")
_Cdx6500PPSTSPPPStatEntry_Object = MibTableRow
cdx6500PPSTSPPPStatEntry = _Cdx6500PPSTSPPPStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 31, 1)
)
cdx6500PPSTSPPPStatEntry.setIndexNames(
    (0, "SPP-OPT-MIB", "cdx6500SPPPStatPortNum"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTSPPPStatEntry.setStatus("mandatory")


class _Cdx6500SPPPStatPortNum_Type(Integer32):
    """Custom type cdx6500SPPPStatPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500SPPPStatPortNum_Type.__name__ = "Integer32"
_Cdx6500SPPPStatPortNum_Object = MibTableColumn
cdx6500SPPPStatPortNum = _Cdx6500SPPPStatPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 31, 1, 1),
    _Cdx6500SPPPStatPortNum_Type()
)
cdx6500SPPPStatPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPStatPortNum.setStatus("mandatory")


class _Cdx6500SPPPStatPortStatus_Type(Integer32):
    """Custom type cdx6500SPPPStatPortStatus based on Integer32"""
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


_Cdx6500SPPPStatPortStatus_Type.__name__ = "Integer32"
_Cdx6500SPPPStatPortStatus_Object = MibTableColumn
cdx6500SPPPStatPortStatus = _Cdx6500SPPPStatPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 31, 1, 2),
    _Cdx6500SPPPStatPortStatus_Type()
)
cdx6500SPPPStatPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPStatPortStatus.setStatus("mandatory")


class _Cdx6500SPPPStatPortType_Type(Integer32):
    """Custom type cdx6500SPPPStatPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            52
        )
    )
    namedValues = NamedValues(
        ("spp", 52)
    )


_Cdx6500SPPPStatPortType_Type.__name__ = "Integer32"
_Cdx6500SPPPStatPortType_Object = MibTableColumn
cdx6500SPPPStatPortType = _Cdx6500SPPPStatPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 31, 1, 3),
    _Cdx6500SPPPStatPortType_Type()
)
cdx6500SPPPStatPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPStatPortType.setStatus("mandatory")


class _Cdx6500SPPPStatPortSpeed_Type(Integer32):
    """Custom type cdx6500SPPPStatPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              7,
              12,
              13,
              14,
              15,
              98)
        )
    )
    namedValues = NamedValues(
        *(("speed1200", 3),
          ("speed1800", 7),
          ("speed19200", 15),
          ("speed2400", 12),
          ("speed300", 2),
          ("speed4800", 13),
          ("speed600", 4),
          ("speed7200", 98),
          ("speed9600", 14))
    )


_Cdx6500SPPPStatPortSpeed_Type.__name__ = "Integer32"
_Cdx6500SPPPStatPortSpeed_Object = MibTableColumn
cdx6500SPPPStatPortSpeed = _Cdx6500SPPPStatPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 31, 1, 4),
    _Cdx6500SPPPStatPortSpeed_Type()
)
cdx6500SPPPStatPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPStatPortSpeed.setStatus("mandatory")
_Cdx6500SPPPStatPortUtilIn_Type = Integer32
_Cdx6500SPPPStatPortUtilIn_Object = MibTableColumn
cdx6500SPPPStatPortUtilIn = _Cdx6500SPPPStatPortUtilIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 31, 1, 5),
    _Cdx6500SPPPStatPortUtilIn_Type()
)
cdx6500SPPPStatPortUtilIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPStatPortUtilIn.setStatus("mandatory")
_Cdx6500SPPPStatPortUtilOut_Type = Integer32
_Cdx6500SPPPStatPortUtilOut_Object = MibTableColumn
cdx6500SPPPStatPortUtilOut = _Cdx6500SPPPStatPortUtilOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 31, 1, 6),
    _Cdx6500SPPPStatPortUtilOut_Type()
)
cdx6500SPPPStatPortUtilOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPStatPortUtilOut.setStatus("mandatory")
_Cdx6500SPPPStatSLCNum_Type = Integer32
_Cdx6500SPPPStatSLCNum_Object = MibTableColumn
cdx6500SPPPStatSLCNum = _Cdx6500SPPPStatSLCNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 31, 1, 7),
    _Cdx6500SPPPStatSLCNum_Type()
)
cdx6500SPPPStatSLCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPStatSLCNum.setStatus("mandatory")
_Cdx6500SPPPStatSLCLineNum_Type = Integer32
_Cdx6500SPPPStatSLCLineNum_Object = MibTableColumn
cdx6500SPPPStatSLCLineNum = _Cdx6500SPPPStatSLCLineNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 31, 1, 8),
    _Cdx6500SPPPStatSLCLineNum_Type()
)
cdx6500SPPPStatSLCLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPStatSLCLineNum.setStatus("mandatory")


class _Cdx6500SPPPStatFlowCntrlState_Type(Integer32):
    """Custom type cdx6500SPPPStatFlowCntrlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("unblocked", 2))
    )


_Cdx6500SPPPStatFlowCntrlState_Type.__name__ = "Integer32"
_Cdx6500SPPPStatFlowCntrlState_Object = MibTableColumn
cdx6500SPPPStatFlowCntrlState = _Cdx6500SPPPStatFlowCntrlState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 31, 1, 9),
    _Cdx6500SPPPStatFlowCntrlState_Type()
)
cdx6500SPPPStatFlowCntrlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPStatFlowCntrlState.setStatus("mandatory")
_Cdx6500SPPPStatLastStatsReset_Type = DisplayString
_Cdx6500SPPPStatLastStatsReset_Object = MibTableColumn
cdx6500SPPPStatLastStatsReset = _Cdx6500SPPPStatLastStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 31, 1, 10),
    _Cdx6500SPPPStatLastStatsReset_Type()
)
cdx6500SPPPStatLastStatsReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPStatLastStatsReset.setStatus("mandatory")
_Cdx6500SPPPStatChrsIn_Type = Counter32
_Cdx6500SPPPStatChrsIn_Object = MibTableColumn
cdx6500SPPPStatChrsIn = _Cdx6500SPPPStatChrsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 31, 1, 11),
    _Cdx6500SPPPStatChrsIn_Type()
)
cdx6500SPPPStatChrsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPStatChrsIn.setStatus("mandatory")
_Cdx6500SPPPStatChrsOut_Type = Counter32
_Cdx6500SPPPStatChrsOut_Object = MibTableColumn
cdx6500SPPPStatChrsOut = _Cdx6500SPPPStatChrsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 31, 1, 12),
    _Cdx6500SPPPStatChrsOut_Type()
)
cdx6500SPPPStatChrsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPStatChrsOut.setStatus("mandatory")
_Cdx6500SPPPStatFramesIn_Type = Counter32
_Cdx6500SPPPStatFramesIn_Object = MibTableColumn
cdx6500SPPPStatFramesIn = _Cdx6500SPPPStatFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 31, 1, 13),
    _Cdx6500SPPPStatFramesIn_Type()
)
cdx6500SPPPStatFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPStatFramesIn.setStatus("mandatory")
_Cdx6500SPPPStatFramesOut_Type = Counter32
_Cdx6500SPPPStatFramesOut_Object = MibTableColumn
cdx6500SPPPStatFramesOut = _Cdx6500SPPPStatFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 31, 1, 14),
    _Cdx6500SPPPStatFramesOut_Type()
)
cdx6500SPPPStatFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPStatFramesOut.setStatus("mandatory")
_Cdx6500SPPPStatChrsInPerSec_Type = Integer32
_Cdx6500SPPPStatChrsInPerSec_Object = MibTableColumn
cdx6500SPPPStatChrsInPerSec = _Cdx6500SPPPStatChrsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 31, 1, 15),
    _Cdx6500SPPPStatChrsInPerSec_Type()
)
cdx6500SPPPStatChrsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPStatChrsInPerSec.setStatus("mandatory")
_Cdx6500SPPPStatChrsOutPerSec_Type = Integer32
_Cdx6500SPPPStatChrsOutPerSec_Object = MibTableColumn
cdx6500SPPPStatChrsOutPerSec = _Cdx6500SPPPStatChrsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 31, 1, 16),
    _Cdx6500SPPPStatChrsOutPerSec_Type()
)
cdx6500SPPPStatChrsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPStatChrsOutPerSec.setStatus("mandatory")
_Cdx6500SPPPStatFramesInPerSec_Type = Integer32
_Cdx6500SPPPStatFramesInPerSec_Object = MibTableColumn
cdx6500SPPPStatFramesInPerSec = _Cdx6500SPPPStatFramesInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 31, 1, 17),
    _Cdx6500SPPPStatFramesInPerSec_Type()
)
cdx6500SPPPStatFramesInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPStatFramesInPerSec.setStatus("mandatory")
_Cdx6500SPPPStatFramesOutPerSec_Type = Integer32
_Cdx6500SPPPStatFramesOutPerSec_Object = MibTableColumn
cdx6500SPPPStatFramesOutPerSec = _Cdx6500SPPPStatFramesOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 31, 1, 18),
    _Cdx6500SPPPStatFramesOutPerSec_Type()
)
cdx6500SPPPStatFramesOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPStatFramesOutPerSec.setStatus("mandatory")
_Cdx6500SPPPStatNoOfErrorFrames_Type = Integer32
_Cdx6500SPPPStatNoOfErrorFrames_Object = MibTableColumn
cdx6500SPPPStatNoOfErrorFrames = _Cdx6500SPPPStatNoOfErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 31, 1, 19),
    _Cdx6500SPPPStatNoOfErrorFrames_Type()
)
cdx6500SPPPStatNoOfErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPStatNoOfErrorFrames.setStatus("mandatory")
_Cdx6500SPPPStatNoOfStns_Type = Integer32
_Cdx6500SPPPStatNoOfStns_Object = MibTableColumn
cdx6500SPPPStatNoOfStns = _Cdx6500SPPPStatNoOfStns_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 31, 1, 20),
    _Cdx6500SPPPStatNoOfStns_Type()
)
cdx6500SPPPStatNoOfStns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPPStatNoOfStns.setStatus("mandatory")
_Cdx6500PSTStationProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTStationProtocolGroup = _Cdx6500PSTStationProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3)
)
_Cdx6500SPSTSPPStnStatTable_Object = MibTable
cdx6500SPSTSPPStnStatTable = _Cdx6500SPSTSPPStnStatTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9)
)
if mibBuilder.loadTexts:
    cdx6500SPSTSPPStnStatTable.setStatus("mandatory")
_Cdx6500SPSTSPPSStatEntry_Object = MibTableRow
cdx6500SPSTSPPSStatEntry = _Cdx6500SPSTSPPSStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1)
)
cdx6500SPSTSPPSStatEntry.setIndexNames(
    (0, "SPP-OPT-MIB", "cdx6500SPPSStatPortNum"),
    (0, "SPP-OPT-MIB", "cdx6500SPPSStatStnId"),
)
if mibBuilder.loadTexts:
    cdx6500SPSTSPPSStatEntry.setStatus("mandatory")


class _Cdx6500SPPSStatPortNum_Type(Integer32):
    """Custom type cdx6500SPPSStatPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500SPPSStatPortNum_Type.__name__ = "Integer32"
_Cdx6500SPPSStatPortNum_Object = MibTableColumn
cdx6500SPPSStatPortNum = _Cdx6500SPPSStatPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 1),
    _Cdx6500SPPSStatPortNum_Type()
)
cdx6500SPPSStatPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatPortNum.setStatus("mandatory")
_Cdx6500SPPSStatStnId_Type = Integer32
_Cdx6500SPPSStatStnId_Object = MibTableColumn
cdx6500SPPSStatStnId = _Cdx6500SPPSStatStnId_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 2),
    _Cdx6500SPPSStatStnId_Type()
)
cdx6500SPPSStatStnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatStnId.setStatus("mandatory")


class _Cdx6500SPPSStatStnStatus_Type(Integer32):
    """Custom type cdx6500SPPSStatStnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              50)
        )
    )
    namedValues = NamedValues(
        *(("busyOut", 2),
          ("down", 4),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("up", 3))
    )


_Cdx6500SPPSStatStnStatus_Type.__name__ = "Integer32"
_Cdx6500SPPSStatStnStatus_Object = MibTableColumn
cdx6500SPPSStatStnStatus = _Cdx6500SPPSStatStnStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 3),
    _Cdx6500SPPSStatStnStatus_Type()
)
cdx6500SPPSStatStnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatStnStatus.setStatus("mandatory")
_Cdx6500SPPSStatSLCNum_Type = Integer32
_Cdx6500SPPSStatSLCNum_Object = MibTableColumn
cdx6500SPPSStatSLCNum = _Cdx6500SPPSStatSLCNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 4),
    _Cdx6500SPPSStatSLCNum_Type()
)
cdx6500SPPSStatSLCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatSLCNum.setStatus("mandatory")
_Cdx6500SPPSStatSLCLineNum_Type = Integer32
_Cdx6500SPPSStatSLCLineNum_Object = MibTableColumn
cdx6500SPPSStatSLCLineNum = _Cdx6500SPPSStatSLCLineNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 5),
    _Cdx6500SPPSStatSLCLineNum_Type()
)
cdx6500SPPSStatSLCLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatSLCLineNum.setStatus("mandatory")


class _Cdx6500SPPSStatAdjChanState_Type(Integer32):
    """Custom type cdx6500SPPSStatAdjChanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("unblocked", 2))
    )


_Cdx6500SPPSStatAdjChanState_Type.__name__ = "Integer32"
_Cdx6500SPPSStatAdjChanState_Object = MibTableColumn
cdx6500SPPSStatAdjChanState = _Cdx6500SPPSStatAdjChanState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 6),
    _Cdx6500SPPSStatAdjChanState_Type()
)
cdx6500SPPSStatAdjChanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatAdjChanState.setStatus("mandatory")


class _Cdx6500SPPSStatCurrCallSummStatus_Type(Integer32):
    """Custom type cdx6500SPPSStatCurrCallSummStatus based on Integer32"""
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
        *(("called", 4),
          ("calling", 3),
          ("connected", 5),
          ("disconnected", 2),
          ("inhibited", 1),
          ("notDefined", 6))
    )


_Cdx6500SPPSStatCurrCallSummStatus_Type.__name__ = "Integer32"
_Cdx6500SPPSStatCurrCallSummStatus_Object = MibTableColumn
cdx6500SPPSStatCurrCallSummStatus = _Cdx6500SPPSStatCurrCallSummStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 7),
    _Cdx6500SPPSStatCurrCallSummStatus_Type()
)
cdx6500SPPSStatCurrCallSummStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatCurrCallSummStatus.setStatus("mandatory")
_Cdx6500SPPSStatLastClrCauseCode_Type = DisplayString
_Cdx6500SPPSStatLastClrCauseCode_Object = MibTableColumn
cdx6500SPPSStatLastClrCauseCode = _Cdx6500SPPSStatLastClrCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 8),
    _Cdx6500SPPSStatLastClrCauseCode_Type()
)
cdx6500SPPSStatLastClrCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatLastClrCauseCode.setStatus("mandatory")
_Cdx6500SPPSStatLastClrDiagCode_Type = DisplayString
_Cdx6500SPPSStatLastClrDiagCode_Object = MibTableColumn
cdx6500SPPSStatLastClrDiagCode = _Cdx6500SPPSStatLastClrDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 9),
    _Cdx6500SPPSStatLastClrDiagCode_Type()
)
cdx6500SPPSStatLastClrDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatLastClrDiagCode.setStatus("mandatory")
_Cdx6500SPPSStatLastInCalledAddress_Type = DisplayString
_Cdx6500SPPSStatLastInCalledAddress_Object = MibTableColumn
cdx6500SPPSStatLastInCalledAddress = _Cdx6500SPPSStatLastInCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 10),
    _Cdx6500SPPSStatLastInCalledAddress_Type()
)
cdx6500SPPSStatLastInCalledAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatLastInCalledAddress.setStatus("mandatory")
_Cdx6500SPPSStatLastInCallingAddress_Type = DisplayString
_Cdx6500SPPSStatLastInCallingAddress_Object = MibTableColumn
cdx6500SPPSStatLastInCallingAddress = _Cdx6500SPPSStatLastInCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 11),
    _Cdx6500SPPSStatLastInCallingAddress_Type()
)
cdx6500SPPSStatLastInCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatLastInCallingAddress.setStatus("mandatory")
_Cdx6500SPPSStatLastInCallFacilities_Type = DisplayString
_Cdx6500SPPSStatLastInCallFacilities_Object = MibTableColumn
cdx6500SPPSStatLastInCallFacilities = _Cdx6500SPPSStatLastInCallFacilities_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 12),
    _Cdx6500SPPSStatLastInCallFacilities_Type()
)
cdx6500SPPSStatLastInCallFacilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatLastInCallFacilities.setStatus("mandatory")
_Cdx6500SPPSStatLastInCallCUD_Type = DisplayString
_Cdx6500SPPSStatLastInCallCUD_Object = MibTableColumn
cdx6500SPPSStatLastInCallCUD = _Cdx6500SPPSStatLastInCallCUD_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 13),
    _Cdx6500SPPSStatLastInCallCUD_Type()
)
cdx6500SPPSStatLastInCallCUD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatLastInCallCUD.setStatus("mandatory")
_Cdx6500SPPSStatLastOutCalledAddress_Type = DisplayString
_Cdx6500SPPSStatLastOutCalledAddress_Object = MibTableColumn
cdx6500SPPSStatLastOutCalledAddress = _Cdx6500SPPSStatLastOutCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 14),
    _Cdx6500SPPSStatLastOutCalledAddress_Type()
)
cdx6500SPPSStatLastOutCalledAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatLastOutCalledAddress.setStatus("mandatory")
_Cdx6500SPPSStatLastOutCallingAddress_Type = DisplayString
_Cdx6500SPPSStatLastOutCallingAddress_Object = MibTableColumn
cdx6500SPPSStatLastOutCallingAddress = _Cdx6500SPPSStatLastOutCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 15),
    _Cdx6500SPPSStatLastOutCallingAddress_Type()
)
cdx6500SPPSStatLastOutCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatLastOutCallingAddress.setStatus("mandatory")
_Cdx6500SPPSStatLastOutCallFacilities_Type = DisplayString
_Cdx6500SPPSStatLastOutCallFacilities_Object = MibTableColumn
cdx6500SPPSStatLastOutCallFacilities = _Cdx6500SPPSStatLastOutCallFacilities_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 16),
    _Cdx6500SPPSStatLastOutCallFacilities_Type()
)
cdx6500SPPSStatLastOutCallFacilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatLastOutCallFacilities.setStatus("mandatory")
_Cdx6500SPPSStatLastOutCallCUD_Type = DisplayString
_Cdx6500SPPSStatLastOutCallCUD_Object = MibTableColumn
cdx6500SPPSStatLastOutCallCUD = _Cdx6500SPPSStatLastOutCallCUD_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 17),
    _Cdx6500SPPSStatLastOutCallCUD_Type()
)
cdx6500SPPSStatLastOutCallCUD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatLastOutCallCUD.setStatus("mandatory")
_Cdx6500SPPSStatChrsIn_Type = Counter32
_Cdx6500SPPSStatChrsIn_Object = MibTableColumn
cdx6500SPPSStatChrsIn = _Cdx6500SPPSStatChrsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 18),
    _Cdx6500SPPSStatChrsIn_Type()
)
cdx6500SPPSStatChrsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatChrsIn.setStatus("mandatory")
_Cdx6500SPPSStatChrsOut_Type = Counter32
_Cdx6500SPPSStatChrsOut_Object = MibTableColumn
cdx6500SPPSStatChrsOut = _Cdx6500SPPSStatChrsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 19),
    _Cdx6500SPPSStatChrsOut_Type()
)
cdx6500SPPSStatChrsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatChrsOut.setStatus("mandatory")
_Cdx6500SPPSStatFramesIn_Type = Counter32
_Cdx6500SPPSStatFramesIn_Object = MibTableColumn
cdx6500SPPSStatFramesIn = _Cdx6500SPPSStatFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 20),
    _Cdx6500SPPSStatFramesIn_Type()
)
cdx6500SPPSStatFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatFramesIn.setStatus("mandatory")
_Cdx6500SPPSStatFramesOut_Type = Counter32
_Cdx6500SPPSStatFramesOut_Object = MibTableColumn
cdx6500SPPSStatFramesOut = _Cdx6500SPPSStatFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 21),
    _Cdx6500SPPSStatFramesOut_Type()
)
cdx6500SPPSStatFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatFramesOut.setStatus("mandatory")
_Cdx6500SPPSStatChrsInPerSec_Type = Integer32
_Cdx6500SPPSStatChrsInPerSec_Object = MibTableColumn
cdx6500SPPSStatChrsInPerSec = _Cdx6500SPPSStatChrsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 22),
    _Cdx6500SPPSStatChrsInPerSec_Type()
)
cdx6500SPPSStatChrsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatChrsInPerSec.setStatus("mandatory")
_Cdx6500SPPSStatChrsOutPerSec_Type = Integer32
_Cdx6500SPPSStatChrsOutPerSec_Object = MibTableColumn
cdx6500SPPSStatChrsOutPerSec = _Cdx6500SPPSStatChrsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 23),
    _Cdx6500SPPSStatChrsOutPerSec_Type()
)
cdx6500SPPSStatChrsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatChrsOutPerSec.setStatus("mandatory")
_Cdx6500SPPSStatFramesInPerSec_Type = Integer32
_Cdx6500SPPSStatFramesInPerSec_Object = MibTableColumn
cdx6500SPPSStatFramesInPerSec = _Cdx6500SPPSStatFramesInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 24),
    _Cdx6500SPPSStatFramesInPerSec_Type()
)
cdx6500SPPSStatFramesInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatFramesInPerSec.setStatus("mandatory")
_Cdx6500SPPSStatFramesOutPerSec_Type = Integer32
_Cdx6500SPPSStatFramesOutPerSec_Object = MibTableColumn
cdx6500SPPSStatFramesOutPerSec = _Cdx6500SPPSStatFramesOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 25),
    _Cdx6500SPPSStatFramesOutPerSec_Type()
)
cdx6500SPPSStatFramesOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatFramesOutPerSec.setStatus("mandatory")
_Cdx6500SPPSStatNoOfErrorFrames_Type = Integer32
_Cdx6500SPPSStatNoOfErrorFrames_Object = MibTableColumn
cdx6500SPPSStatNoOfErrorFrames = _Cdx6500SPPSStatNoOfErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 26),
    _Cdx6500SPPSStatNoOfErrorFrames_Type()
)
cdx6500SPPSStatNoOfErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatNoOfErrorFrames.setStatus("mandatory")
_Cdx6500SPPSStatStnState_Type = DisplayString
_Cdx6500SPPSStatStnState_Object = MibTableColumn
cdx6500SPPSStatStnState = _Cdx6500SPPSStatStnState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 27),
    _Cdx6500SPPSStatStnState_Type()
)
cdx6500SPPSStatStnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatStnState.setStatus("mandatory")
_Cdx6500SPPSStatLastStatsReset_Type = DisplayString
_Cdx6500SPPSStatLastStatsReset_Object = MibTableColumn
cdx6500SPPSStatLastStatsReset = _Cdx6500SPPSStatLastStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 9, 1, 28),
    _Cdx6500SPPSStatLastStatsReset_Type()
)
cdx6500SPPSStatLastStatsReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SPPSStatLastStatsReset.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)
_Cdx6500ContSPPTable_ObjectIdentity = ObjectIdentity
cdx6500ContSPPTable = _Cdx6500ContSPPTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 13)
)
_Cdx6500ContSPPPortTable_Object = MibTable
cdx6500ContSPPPortTable = _Cdx6500ContSPPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 13, 1)
)
if mibBuilder.loadTexts:
    cdx6500ContSPPPortTable.setStatus("mandatory")
_Cdx6500ContSPPPortEntry_Object = MibTableRow
cdx6500ContSPPPortEntry = _Cdx6500ContSPPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 13, 1, 1)
)
cdx6500ContSPPPortEntry.setIndexNames(
    (0, "SPP-OPT-MIB", "cdx6500ContSPPPortNum"),
)
if mibBuilder.loadTexts:
    cdx6500ContSPPPortEntry.setStatus("mandatory")


class _Cdx6500ContSPPPortNum_Type(Integer32):
    """Custom type cdx6500ContSPPPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500ContSPPPortNum_Type.__name__ = "Integer32"
_Cdx6500ContSPPPortNum_Object = MibTableColumn
cdx6500ContSPPPortNum = _Cdx6500ContSPPPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 13, 1, 1, 1),
    _Cdx6500ContSPPPortNum_Type()
)
cdx6500ContSPPPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdx6500ContSPPPortNum.setStatus("mandatory")


class _Cdx6500ContSPPPortBoot_Type(Integer32):
    """Custom type cdx6500ContSPPPortBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("boot", 1)
    )


_Cdx6500ContSPPPortBoot_Type.__name__ = "Integer32"
_Cdx6500ContSPPPortBoot_Object = MibTableColumn
cdx6500ContSPPPortBoot = _Cdx6500ContSPPPortBoot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 13, 1, 1, 2),
    _Cdx6500ContSPPPortBoot_Type()
)
cdx6500ContSPPPortBoot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500ContSPPPortBoot.setStatus("mandatory")


class _Cdx6500ContSPPPortEnable_Type(Integer32):
    """Custom type cdx6500ContSPPPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_Cdx6500ContSPPPortEnable_Type.__name__ = "Integer32"
_Cdx6500ContSPPPortEnable_Object = MibTableColumn
cdx6500ContSPPPortEnable = _Cdx6500ContSPPPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 13, 1, 1, 3),
    _Cdx6500ContSPPPortEnable_Type()
)
cdx6500ContSPPPortEnable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500ContSPPPortEnable.setStatus("mandatory")


class _Cdx6500ContSPPPortDisable_Type(Integer32):
    """Custom type cdx6500ContSPPPortDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("disable", 1)
    )


_Cdx6500ContSPPPortDisable_Type.__name__ = "Integer32"
_Cdx6500ContSPPPortDisable_Object = MibTableColumn
cdx6500ContSPPPortDisable = _Cdx6500ContSPPPortDisable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 13, 1, 1, 4),
    _Cdx6500ContSPPPortDisable_Type()
)
cdx6500ContSPPPortDisable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500ContSPPPortDisable.setStatus("mandatory")


class _Cdx6500ContSPPPortResetStats_Type(Integer32):
    """Custom type cdx6500ContSPPPortResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Cdx6500ContSPPPortResetStats_Type.__name__ = "Integer32"
_Cdx6500ContSPPPortResetStats_Object = MibTableColumn
cdx6500ContSPPPortResetStats = _Cdx6500ContSPPPortResetStats_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 13, 1, 1, 5),
    _Cdx6500ContSPPPortResetStats_Type()
)
cdx6500ContSPPPortResetStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500ContSPPPortResetStats.setStatus("mandatory")
_Cdx6500ContSPPStnTable_Object = MibTable
cdx6500ContSPPStnTable = _Cdx6500ContSPPStnTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 13, 2)
)
if mibBuilder.loadTexts:
    cdx6500ContSPPStnTable.setStatus("mandatory")
_Cdx6500ContSPPStnEntry_Object = MibTableRow
cdx6500ContSPPStnEntry = _Cdx6500ContSPPStnEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 13, 2, 1)
)
cdx6500ContSPPStnEntry.setIndexNames(
    (0, "SPP-OPT-MIB", "cdx6500ContSPPPortNum"),
    (0, "SPP-OPT-MIB", "cdx6500ContSPPStnId"),
)
if mibBuilder.loadTexts:
    cdx6500ContSPPStnEntry.setStatus("mandatory")


class _Cdx6500SContSPPPortNum_Type(Integer32):
    """Custom type cdx6500SContSPPPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500SContSPPPortNum_Type.__name__ = "Integer32"
_Cdx6500SContSPPPortNum_Object = MibTableColumn
cdx6500SContSPPPortNum = _Cdx6500SContSPPPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 13, 2, 1, 1),
    _Cdx6500SContSPPPortNum_Type()
)
cdx6500SContSPPPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdx6500SContSPPPortNum.setStatus("mandatory")
_Cdx6500ContSPPStnId_Type = Integer32
_Cdx6500ContSPPStnId_Object = MibTableColumn
cdx6500ContSPPStnId = _Cdx6500ContSPPStnId_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 13, 2, 1, 2),
    _Cdx6500ContSPPStnId_Type()
)
cdx6500ContSPPStnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdx6500ContSPPStnId.setStatus("mandatory")


class _Cdx6500ContSPPStnBoot_Type(Integer32):
    """Custom type cdx6500ContSPPStnBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("boot", 1)
    )


_Cdx6500ContSPPStnBoot_Type.__name__ = "Integer32"
_Cdx6500ContSPPStnBoot_Object = MibTableColumn
cdx6500ContSPPStnBoot = _Cdx6500ContSPPStnBoot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 13, 2, 1, 3),
    _Cdx6500ContSPPStnBoot_Type()
)
cdx6500ContSPPStnBoot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdx6500ContSPPStnBoot.setStatus("mandatory")


class _Cdx6500ContSPPStnEnable_Type(Integer32):
    """Custom type cdx6500ContSPPStnEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_Cdx6500ContSPPStnEnable_Type.__name__ = "Integer32"
_Cdx6500ContSPPStnEnable_Object = MibTableColumn
cdx6500ContSPPStnEnable = _Cdx6500ContSPPStnEnable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 13, 2, 1, 4),
    _Cdx6500ContSPPStnEnable_Type()
)
cdx6500ContSPPStnEnable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500ContSPPStnEnable.setStatus("mandatory")


class _Cdx6500ContSPPStnDisable_Type(Integer32):
    """Custom type cdx6500ContSPPStnDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("disable", 1)
    )


_Cdx6500ContSPPStnDisable_Type.__name__ = "Integer32"
_Cdx6500ContSPPStnDisable_Object = MibTableColumn
cdx6500ContSPPStnDisable = _Cdx6500ContSPPStnDisable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 13, 2, 1, 5),
    _Cdx6500ContSPPStnDisable_Type()
)
cdx6500ContSPPStnDisable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500ContSPPStnDisable.setStatus("mandatory")


class _Cdx6500ContSPPStnResetStats_Type(Integer32):
    """Custom type cdx6500ContSPPStnResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Cdx6500ContSPPStnResetStats_Type.__name__ = "Integer32"
_Cdx6500ContSPPStnResetStats_Object = MibTableColumn
cdx6500ContSPPStnResetStats = _Cdx6500ContSPPStnResetStats_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 13, 2, 1, 6),
    _Cdx6500ContSPPStnResetStats_Type()
)
cdx6500ContSPPStnResetStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500ContSPPStnResetStats.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SPP-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PPCTSPPPortTable": cdx6500PPCTSPPPortTable,
       "cdx6500PPCTSPPPortEntry": cdx6500PPCTSPPPortEntry,
       "cdx6500SPPPCfgPortNum": cdx6500SPPPCfgPortNum,
       "cdx6500SPPPCfgPortType": cdx6500SPPPCfgPortType,
       "cdx6500SPPPCfgPortSpeed": cdx6500SPPPCfgPortSpeed,
       "cdx6500SPPPCfgInterchTimeout": cdx6500SPPPCfgInterchTimeout,
       "cdx6500SPPPCfgSLCNum": cdx6500SPPPCfgSLCNum,
       "cdx6500SPPPCfgSLCLineNum": cdx6500SPPPCfgSLCLineNum,
       "cdx6500SPPPCfgStnIDList": cdx6500SPPPCfgStnIDList,
       "cdx6500SPPPCfgProtocolID": cdx6500SPPPCfgProtocolID,
       "cdx6500SPPPCfgQueueSize": cdx6500SPPPCfgQueueSize,
       "cdx6500SPPPCfgBlockingThresh": cdx6500SPPPCfgBlockingThresh,
       "cdx6500SPPPCfgUnblockThresh": cdx6500SPPPCfgUnblockThresh,
       "cdx6500SPPPCfgElectricalInterfaceType": cdx6500SPPPCfgElectricalInterfaceType,
       "cdx6500SPPPCfgV24ElectricalInterfaceOption": cdx6500SPPPCfgV24ElectricalInterfaceOption,
       "cdx6500SPPPCfgHighSpeedElectricalInterfaceOption": cdx6500SPPPCfgHighSpeedElectricalInterfaceOption,
       "cdx6500PCTStationProtocolGroup": cdx6500PCTStationProtocolGroup,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPSTSPPPStatsTable": cdx6500PPSTSPPPStatsTable,
       "cdx6500PPSTSPPPStatEntry": cdx6500PPSTSPPPStatEntry,
       "cdx6500SPPPStatPortNum": cdx6500SPPPStatPortNum,
       "cdx6500SPPPStatPortStatus": cdx6500SPPPStatPortStatus,
       "cdx6500SPPPStatPortType": cdx6500SPPPStatPortType,
       "cdx6500SPPPStatPortSpeed": cdx6500SPPPStatPortSpeed,
       "cdx6500SPPPStatPortUtilIn": cdx6500SPPPStatPortUtilIn,
       "cdx6500SPPPStatPortUtilOut": cdx6500SPPPStatPortUtilOut,
       "cdx6500SPPPStatSLCNum": cdx6500SPPPStatSLCNum,
       "cdx6500SPPPStatSLCLineNum": cdx6500SPPPStatSLCLineNum,
       "cdx6500SPPPStatFlowCntrlState": cdx6500SPPPStatFlowCntrlState,
       "cdx6500SPPPStatLastStatsReset": cdx6500SPPPStatLastStatsReset,
       "cdx6500SPPPStatChrsIn": cdx6500SPPPStatChrsIn,
       "cdx6500SPPPStatChrsOut": cdx6500SPPPStatChrsOut,
       "cdx6500SPPPStatFramesIn": cdx6500SPPPStatFramesIn,
       "cdx6500SPPPStatFramesOut": cdx6500SPPPStatFramesOut,
       "cdx6500SPPPStatChrsInPerSec": cdx6500SPPPStatChrsInPerSec,
       "cdx6500SPPPStatChrsOutPerSec": cdx6500SPPPStatChrsOutPerSec,
       "cdx6500SPPPStatFramesInPerSec": cdx6500SPPPStatFramesInPerSec,
       "cdx6500SPPPStatFramesOutPerSec": cdx6500SPPPStatFramesOutPerSec,
       "cdx6500SPPPStatNoOfErrorFrames": cdx6500SPPPStatNoOfErrorFrames,
       "cdx6500SPPPStatNoOfStns": cdx6500SPPPStatNoOfStns,
       "cdx6500PSTStationProtocolGroup": cdx6500PSTStationProtocolGroup,
       "cdx6500SPSTSPPStnStatTable": cdx6500SPSTSPPStnStatTable,
       "cdx6500SPSTSPPSStatEntry": cdx6500SPSTSPPSStatEntry,
       "cdx6500SPPSStatPortNum": cdx6500SPPSStatPortNum,
       "cdx6500SPPSStatStnId": cdx6500SPPSStatStnId,
       "cdx6500SPPSStatStnStatus": cdx6500SPPSStatStnStatus,
       "cdx6500SPPSStatSLCNum": cdx6500SPPSStatSLCNum,
       "cdx6500SPPSStatSLCLineNum": cdx6500SPPSStatSLCLineNum,
       "cdx6500SPPSStatAdjChanState": cdx6500SPPSStatAdjChanState,
       "cdx6500SPPSStatCurrCallSummStatus": cdx6500SPPSStatCurrCallSummStatus,
       "cdx6500SPPSStatLastClrCauseCode": cdx6500SPPSStatLastClrCauseCode,
       "cdx6500SPPSStatLastClrDiagCode": cdx6500SPPSStatLastClrDiagCode,
       "cdx6500SPPSStatLastInCalledAddress": cdx6500SPPSStatLastInCalledAddress,
       "cdx6500SPPSStatLastInCallingAddress": cdx6500SPPSStatLastInCallingAddress,
       "cdx6500SPPSStatLastInCallFacilities": cdx6500SPPSStatLastInCallFacilities,
       "cdx6500SPPSStatLastInCallCUD": cdx6500SPPSStatLastInCallCUD,
       "cdx6500SPPSStatLastOutCalledAddress": cdx6500SPPSStatLastOutCalledAddress,
       "cdx6500SPPSStatLastOutCallingAddress": cdx6500SPPSStatLastOutCallingAddress,
       "cdx6500SPPSStatLastOutCallFacilities": cdx6500SPPSStatLastOutCallFacilities,
       "cdx6500SPPSStatLastOutCallCUD": cdx6500SPPSStatLastOutCallCUD,
       "cdx6500SPPSStatChrsIn": cdx6500SPPSStatChrsIn,
       "cdx6500SPPSStatChrsOut": cdx6500SPPSStatChrsOut,
       "cdx6500SPPSStatFramesIn": cdx6500SPPSStatFramesIn,
       "cdx6500SPPSStatFramesOut": cdx6500SPPSStatFramesOut,
       "cdx6500SPPSStatChrsInPerSec": cdx6500SPPSStatChrsInPerSec,
       "cdx6500SPPSStatChrsOutPerSec": cdx6500SPPSStatChrsOutPerSec,
       "cdx6500SPPSStatFramesInPerSec": cdx6500SPPSStatFramesInPerSec,
       "cdx6500SPPSStatFramesOutPerSec": cdx6500SPPSStatFramesOutPerSec,
       "cdx6500SPPSStatNoOfErrorFrames": cdx6500SPPSStatNoOfErrorFrames,
       "cdx6500SPPSStatStnState": cdx6500SPPSStatStnState,
       "cdx6500SPPSStatLastStatsReset": cdx6500SPPSStatLastStatsReset,
       "cdx6500Controls": cdx6500Controls,
       "cdx6500ContSPPTable": cdx6500ContSPPTable,
       "cdx6500ContSPPPortTable": cdx6500ContSPPPortTable,
       "cdx6500ContSPPPortEntry": cdx6500ContSPPPortEntry,
       "cdx6500ContSPPPortNum": cdx6500ContSPPPortNum,
       "cdx6500ContSPPPortBoot": cdx6500ContSPPPortBoot,
       "cdx6500ContSPPPortEnable": cdx6500ContSPPPortEnable,
       "cdx6500ContSPPPortDisable": cdx6500ContSPPPortDisable,
       "cdx6500ContSPPPortResetStats": cdx6500ContSPPPortResetStats,
       "cdx6500ContSPPStnTable": cdx6500ContSPPStnTable,
       "cdx6500ContSPPStnEntry": cdx6500ContSPPStnEntry,
       "cdx6500SContSPPPortNum": cdx6500SContSPPPortNum,
       "cdx6500ContSPPStnId": cdx6500ContSPPStnId,
       "cdx6500ContSPPStnBoot": cdx6500ContSPPStnBoot,
       "cdx6500ContSPPStnEnable": cdx6500ContSPPStnEnable,
       "cdx6500ContSPPStnDisable": cdx6500ContSPPStnDisable,
       "cdx6500ContSPPStnResetStats": cdx6500ContSPPStnResetStats}
)
