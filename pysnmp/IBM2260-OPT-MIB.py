# SNMP MIB module (IBM2260-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBM2260-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:44 2024
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
_Cdx6500PPCTIBM2260PortTable_Object = MibTable
cdx6500PPCTIBM2260PortTable = _Cdx6500PPCTIBM2260PortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20)
)
if mibBuilder.loadTexts:
    cdx6500PPCTIBM2260PortTable.setStatus("mandatory")
_Cdx6500PPCTIBM2260PortEntry_Object = MibTableRow
cdx6500PPCTIBM2260PortEntry = _Cdx6500PPCTIBM2260PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1)
)
cdx6500PPCTIBM2260PortEntry.setIndexNames(
    (0, "IBM2260-OPT-MIB", "cdx6500IBM2260CfgPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTIBM2260PortEntry.setStatus("mandatory")


class _Cdx6500IBM2260CfgPortNumber_Type(Integer32):
    """Custom type cdx6500IBM2260CfgPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500IBM2260CfgPortNumber_Type.__name__ = "Integer32"
_Cdx6500IBM2260CfgPortNumber_Object = MibTableColumn
cdx6500IBM2260CfgPortNumber = _Cdx6500IBM2260CfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 1),
    _Cdx6500IBM2260CfgPortNumber_Type()
)
cdx6500IBM2260CfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260CfgPortNumber.setStatus("mandatory")


class _Cdx6500IBM2260CfgPadType_Type(Integer32):
    """Custom type cdx6500IBM2260CfgPadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hpad", 2),
          ("tpad", 1))
    )


_Cdx6500IBM2260CfgPadType_Type.__name__ = "Integer32"
_Cdx6500IBM2260CfgPadType_Object = MibTableColumn
cdx6500IBM2260CfgPadType = _Cdx6500IBM2260CfgPadType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 2),
    _Cdx6500IBM2260CfgPadType_Type()
)
cdx6500IBM2260CfgPadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260CfgPadType.setStatus("mandatory")


class _Cdx6500IBM2260CfgPortSpeed_Type(Integer32):
    """Custom type cdx6500IBM2260CfgPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              8,
              13,
              14,
              15,
              16,
              99)
        )
    )
    namedValues = NamedValues(
        *(("speed1200", 4),
          ("speed1800", 8),
          ("speed19200", 16),
          ("speed2400", 13),
          ("speed4800", 14),
          ("speed7200", 99),
          ("speed9600", 15))
    )


_Cdx6500IBM2260CfgPortSpeed_Type.__name__ = "Integer32"
_Cdx6500IBM2260CfgPortSpeed_Object = MibTableColumn
cdx6500IBM2260CfgPortSpeed = _Cdx6500IBM2260CfgPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 3),
    _Cdx6500IBM2260CfgPortSpeed_Type()
)
cdx6500IBM2260CfgPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260CfgPortSpeed.setStatus("mandatory")


class _Cdx6500IBM2260CfgConnType_Type(Integer32):
    """Custom type cdx6500IBM2260CfgConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              16)
        )
    )
    namedValues = NamedValues(
        *(("simp", 1),
          ("simpa", 16))
    )


_Cdx6500IBM2260CfgConnType_Type.__name__ = "Integer32"
_Cdx6500IBM2260CfgConnType_Object = MibTableColumn
cdx6500IBM2260CfgConnType = _Cdx6500IBM2260CfgConnType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 4),
    _Cdx6500IBM2260CfgConnType_Type()
)
cdx6500IBM2260CfgConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260CfgConnType.setStatus("mandatory")
_Cdx6500IBM2260CfgNumDevice_Type = Integer32
_Cdx6500IBM2260CfgNumDevice_Object = MibTableColumn
cdx6500IBM2260CfgNumDevice = _Cdx6500IBM2260CfgNumDevice_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 5),
    _Cdx6500IBM2260CfgNumDevice_Type()
)
cdx6500IBM2260CfgNumDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260CfgNumDevice.setStatus("mandatory")
_Cdx6500IBM2260CfgServiceTimer_Type = Integer32
_Cdx6500IBM2260CfgServiceTimer_Object = MibTableColumn
cdx6500IBM2260CfgServiceTimer = _Cdx6500IBM2260CfgServiceTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 6),
    _Cdx6500IBM2260CfgServiceTimer_Type()
)
cdx6500IBM2260CfgServiceTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260CfgServiceTimer.setStatus("mandatory")
_Cdx6500IBM2260CfgThreshCtr_Type = Integer32
_Cdx6500IBM2260CfgThreshCtr_Object = MibTableColumn
cdx6500IBM2260CfgThreshCtr = _Cdx6500IBM2260CfgThreshCtr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 7),
    _Cdx6500IBM2260CfgThreshCtr_Type()
)
cdx6500IBM2260CfgThreshCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260CfgThreshCtr.setStatus("mandatory")
_Cdx6500IBM2260CfgRespTimeout_Type = Integer32
_Cdx6500IBM2260CfgRespTimeout_Object = MibTableColumn
cdx6500IBM2260CfgRespTimeout = _Cdx6500IBM2260CfgRespTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 8),
    _Cdx6500IBM2260CfgRespTimeout_Type()
)
cdx6500IBM2260CfgRespTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260CfgRespTimeout.setStatus("mandatory")
_Cdx6500IBM2260CfgPortSubAddr_Type = DisplayString
_Cdx6500IBM2260CfgPortSubAddr_Object = MibTableColumn
cdx6500IBM2260CfgPortSubAddr = _Cdx6500IBM2260CfgPortSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 9),
    _Cdx6500IBM2260CfgPortSubAddr_Type()
)
cdx6500IBM2260CfgPortSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260CfgPortSubAddr.setStatus("mandatory")
_Cdx6500IBM2260CfgPortOpt_Type = DisplayString
_Cdx6500IBM2260CfgPortOpt_Object = MibTableColumn
cdx6500IBM2260CfgPortOpt = _Cdx6500IBM2260CfgPortOpt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 10),
    _Cdx6500IBM2260CfgPortOpt_Type()
)
cdx6500IBM2260CfgPortOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260CfgPortOpt.setStatus("mandatory")
_Cdx6500IBM2260CfgRestConnDest_Type = DisplayString
_Cdx6500IBM2260CfgRestConnDest_Object = MibTableColumn
cdx6500IBM2260CfgRestConnDest = _Cdx6500IBM2260CfgRestConnDest_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 11),
    _Cdx6500IBM2260CfgRestConnDest_Type()
)
cdx6500IBM2260CfgRestConnDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260CfgRestConnDest.setStatus("mandatory")


class _Cdx6500IBM2260CfgBillRec_Type(Integer32):
    """Custom type cdx6500IBM2260CfgBillRec based on Integer32"""
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


_Cdx6500IBM2260CfgBillRec_Type.__name__ = "Integer32"
_Cdx6500IBM2260CfgBillRec_Object = MibTableColumn
cdx6500IBM2260CfgBillRec = _Cdx6500IBM2260CfgBillRec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 12),
    _Cdx6500IBM2260CfgBillRec_Type()
)
cdx6500IBM2260CfgBillRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260CfgBillRec.setStatus("mandatory")


class _Cdx6500IBM2260CfgElectricalInterfaceType_Type(Integer32):
    """Custom type cdx6500IBM2260CfgElectricalInterfaceType based on Integer32"""
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
        *(("v24", 1),
          ("v35", 2),
          ("v36", 3),
          ("x21", 4))
    )


_Cdx6500IBM2260CfgElectricalInterfaceType_Type.__name__ = "Integer32"
_Cdx6500IBM2260CfgElectricalInterfaceType_Object = MibTableColumn
cdx6500IBM2260CfgElectricalInterfaceType = _Cdx6500IBM2260CfgElectricalInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 13),
    _Cdx6500IBM2260CfgElectricalInterfaceType_Type()
)
cdx6500IBM2260CfgElectricalInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260CfgElectricalInterfaceType.setStatus("mandatory")


class _Cdx6500IBM2260CfgV24ElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500IBM2260CfgV24ElectricalInterfaceOption based on Integer32"""
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


_Cdx6500IBM2260CfgV24ElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500IBM2260CfgV24ElectricalInterfaceOption_Object = MibTableColumn
cdx6500IBM2260CfgV24ElectricalInterfaceOption = _Cdx6500IBM2260CfgV24ElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 14),
    _Cdx6500IBM2260CfgV24ElectricalInterfaceOption_Type()
)
cdx6500IBM2260CfgV24ElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260CfgV24ElectricalInterfaceOption.setStatus("mandatory")


class _Cdx6500IBM2260CfgHighSpeedElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500IBM2260CfgHighSpeedElectricalInterfaceOption based on Integer32"""
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


_Cdx6500IBM2260CfgHighSpeedElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500IBM2260CfgHighSpeedElectricalInterfaceOption_Object = MibTableColumn
cdx6500IBM2260CfgHighSpeedElectricalInterfaceOption = _Cdx6500IBM2260CfgHighSpeedElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 20, 1, 15),
    _Cdx6500IBM2260CfgHighSpeedElectricalInterfaceOption_Type()
)
cdx6500IBM2260CfgHighSpeedElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260CfgHighSpeedElectricalInterfaceOption.setStatus("mandatory")
_Cdx6500PCTStationProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTStationProtocolGroup = _Cdx6500PCTStationProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3)
)
_Cdx6500SPCTIBM2260StationTable_Object = MibTable
cdx6500SPCTIBM2260StationTable = _Cdx6500SPCTIBM2260StationTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 6)
)
if mibBuilder.loadTexts:
    cdx6500SPCTIBM2260StationTable.setStatus("mandatory")
_Cdx6500SPCTIBM2260StationEntry_Object = MibTableRow
cdx6500SPCTIBM2260StationEntry = _Cdx6500SPCTIBM2260StationEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 6, 1)
)
cdx6500SPCTIBM2260StationEntry.setIndexNames(
    (0, "IBM2260-OPT-MIB", "cdx6500IBM2260sCfgPortNum"),
    (0, "IBM2260-OPT-MIB", "cdx6500IBM2260sCfgStationNum"),
)
if mibBuilder.loadTexts:
    cdx6500SPCTIBM2260StationEntry.setStatus("mandatory")


class _Cdx6500IBM2260sCfgPortNum_Type(Integer32):
    """Custom type cdx6500IBM2260sCfgPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500IBM2260sCfgPortNum_Type.__name__ = "Integer32"
_Cdx6500IBM2260sCfgPortNum_Object = MibTableColumn
cdx6500IBM2260sCfgPortNum = _Cdx6500IBM2260sCfgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 6, 1, 1),
    _Cdx6500IBM2260sCfgPortNum_Type()
)
cdx6500IBM2260sCfgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260sCfgPortNum.setStatus("mandatory")


class _Cdx6500IBM2260sCfgStationNum_Type(Integer32):
    """Custom type cdx6500IBM2260sCfgStationNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Cdx6500IBM2260sCfgStationNum_Type.__name__ = "Integer32"
_Cdx6500IBM2260sCfgStationNum_Object = MibTableColumn
cdx6500IBM2260sCfgStationNum = _Cdx6500IBM2260sCfgStationNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 6, 1, 2),
    _Cdx6500IBM2260sCfgStationNum_Type()
)
cdx6500IBM2260sCfgStationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260sCfgStationNum.setStatus("mandatory")


class _Cdx6500IBM2260sType_Type(Integer32):
    """Custom type cdx6500IBM2260sType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("group", 2),
          ("single", 1))
    )


_Cdx6500IBM2260sType_Type.__name__ = "Integer32"
_Cdx6500IBM2260sType_Object = MibTableColumn
cdx6500IBM2260sType = _Cdx6500IBM2260sType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 6, 1, 3),
    _Cdx6500IBM2260sType_Type()
)
cdx6500IBM2260sType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260sType.setStatus("mandatory")
_Cdx6500IBM2260sStationAddr1_Type = DisplayString
_Cdx6500IBM2260sStationAddr1_Object = MibTableColumn
cdx6500IBM2260sStationAddr1 = _Cdx6500IBM2260sStationAddr1_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 6, 1, 4),
    _Cdx6500IBM2260sStationAddr1_Type()
)
cdx6500IBM2260sStationAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260sStationAddr1.setStatus("mandatory")
_Cdx6500IBM2260sStationAddr2_Type = DisplayString
_Cdx6500IBM2260sStationAddr2_Object = MibTableColumn
cdx6500IBM2260sStationAddr2 = _Cdx6500IBM2260sStationAddr2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 6, 1, 5),
    _Cdx6500IBM2260sStationAddr2_Type()
)
cdx6500IBM2260sStationAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260sStationAddr2.setStatus("mandatory")
_Cdx6500IBM2260sCallMnem_Type = DisplayString
_Cdx6500IBM2260sCallMnem_Object = MibTableColumn
cdx6500IBM2260sCallMnem = _Cdx6500IBM2260sCallMnem_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 6, 1, 6),
    _Cdx6500IBM2260sCallMnem_Type()
)
cdx6500IBM2260sCallMnem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260sCallMnem.setStatus("mandatory")


class _Cdx6500IBM2260sStationEnable_Type(Integer32):
    """Custom type cdx6500IBM2260sStationEnable based on Integer32"""
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


_Cdx6500IBM2260sStationEnable_Type.__name__ = "Integer32"
_Cdx6500IBM2260sStationEnable_Object = MibTableColumn
cdx6500IBM2260sStationEnable = _Cdx6500IBM2260sStationEnable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 6, 1, 7),
    _Cdx6500IBM2260sStationEnable_Type()
)
cdx6500IBM2260sStationEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260sStationEnable.setStatus("mandatory")
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
_Cdx6500PPSTIBM2260PortTable_Object = MibTable
cdx6500PPSTIBM2260PortTable = _Cdx6500PPSTIBM2260PortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19)
)
if mibBuilder.loadTexts:
    cdx6500PPSTIBM2260PortTable.setStatus("mandatory")
_Cdx6500PPSTIBM2260PortEntry_Object = MibTableRow
cdx6500PPSTIBM2260PortEntry = _Cdx6500PPSTIBM2260PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1)
)
cdx6500PPSTIBM2260PortEntry.setIndexNames(
    (0, "IBM2260-OPT-MIB", "cdx6500IBM2260StatPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTIBM2260PortEntry.setStatus("mandatory")


class _Cdx6500IBM2260StatPortNumber_Type(Integer32):
    """Custom type cdx6500IBM2260StatPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500IBM2260StatPortNumber_Type.__name__ = "Integer32"
_Cdx6500IBM2260StatPortNumber_Object = MibTableColumn
cdx6500IBM2260StatPortNumber = _Cdx6500IBM2260StatPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 1),
    _Cdx6500IBM2260StatPortNumber_Type()
)
cdx6500IBM2260StatPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260StatPortNumber.setStatus("mandatory")
_Cdx6500IBM2260StatPortStatus_Type = DisplayString
_Cdx6500IBM2260StatPortStatus_Object = MibTableColumn
cdx6500IBM2260StatPortStatus = _Cdx6500IBM2260StatPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 2),
    _Cdx6500IBM2260StatPortStatus_Type()
)
cdx6500IBM2260StatPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260StatPortStatus.setStatus("mandatory")
_Cdx6500IBM2260StatPortState_Type = DisplayString
_Cdx6500IBM2260StatPortState_Object = MibTableColumn
cdx6500IBM2260StatPortState = _Cdx6500IBM2260StatPortState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 3),
    _Cdx6500IBM2260StatPortState_Type()
)
cdx6500IBM2260StatPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260StatPortState.setStatus("mandatory")


class _Cdx6500IBM2260StatPortSpeed_Type(Integer32):
    """Custom type cdx6500IBM2260StatPortSpeed based on Integer32"""
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
        *(("speed1200", 1),
          ("speed1800", 2),
          ("speed19200", 7),
          ("speed2400", 3),
          ("speed4800", 4),
          ("speed7200", 5),
          ("speed9600", 6))
    )


_Cdx6500IBM2260StatPortSpeed_Type.__name__ = "Integer32"
_Cdx6500IBM2260StatPortSpeed_Object = MibTableColumn
cdx6500IBM2260StatPortSpeed = _Cdx6500IBM2260StatPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 4),
    _Cdx6500IBM2260StatPortSpeed_Type()
)
cdx6500IBM2260StatPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260StatPortSpeed.setStatus("mandatory")


class _Cdx6500IBM2260StatPortUtilin_Type(Integer32):
    """Custom type cdx6500IBM2260StatPortUtilin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500IBM2260StatPortUtilin_Type.__name__ = "Integer32"
_Cdx6500IBM2260StatPortUtilin_Object = MibTableColumn
cdx6500IBM2260StatPortUtilin = _Cdx6500IBM2260StatPortUtilin_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 5),
    _Cdx6500IBM2260StatPortUtilin_Type()
)
cdx6500IBM2260StatPortUtilin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260StatPortUtilin.setStatus("mandatory")


class _Cdx6500IBM2260StatPortUtilOut_Type(Integer32):
    """Custom type cdx6500IBM2260StatPortUtilOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500IBM2260StatPortUtilOut_Type.__name__ = "Integer32"
_Cdx6500IBM2260StatPortUtilOut_Object = MibTableColumn
cdx6500IBM2260StatPortUtilOut = _Cdx6500IBM2260StatPortUtilOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 6),
    _Cdx6500IBM2260StatPortUtilOut_Type()
)
cdx6500IBM2260StatPortUtilOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260StatPortUtilOut.setStatus("mandatory")
_Cdx6500IBM2260StatParityErrors_Type = Integer32
_Cdx6500IBM2260StatParityErrors_Object = MibTableColumn
cdx6500IBM2260StatParityErrors = _Cdx6500IBM2260StatParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 7),
    _Cdx6500IBM2260StatParityErrors_Type()
)
cdx6500IBM2260StatParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260StatParityErrors.setStatus("mandatory")
_Cdx6500IBM2260StatOverrunErrors_Type = Integer32
_Cdx6500IBM2260StatOverrunErrors_Object = MibTableColumn
cdx6500IBM2260StatOverrunErrors = _Cdx6500IBM2260StatOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 8),
    _Cdx6500IBM2260StatOverrunErrors_Type()
)
cdx6500IBM2260StatOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260StatOverrunErrors.setStatus("mandatory")
_Cdx6500IBM2260StatFramingErrors_Type = Integer32
_Cdx6500IBM2260StatFramingErrors_Object = MibTableColumn
cdx6500IBM2260StatFramingErrors = _Cdx6500IBM2260StatFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 9),
    _Cdx6500IBM2260StatFramingErrors_Type()
)
cdx6500IBM2260StatFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260StatFramingErrors.setStatus("mandatory")
_Cdx6500IBM2260StatBCCErrors_Type = Integer32
_Cdx6500IBM2260StatBCCErrors_Object = MibTableColumn
cdx6500IBM2260StatBCCErrors = _Cdx6500IBM2260StatBCCErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 10),
    _Cdx6500IBM2260StatBCCErrors_Type()
)
cdx6500IBM2260StatBCCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260StatBCCErrors.setStatus("mandatory")
_Cdx6500IBM2260StatNoResponse_Type = Integer32
_Cdx6500IBM2260StatNoResponse_Object = MibTableColumn
cdx6500IBM2260StatNoResponse = _Cdx6500IBM2260StatNoResponse_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 11),
    _Cdx6500IBM2260StatNoResponse_Type()
)
cdx6500IBM2260StatNoResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260StatNoResponse.setStatus("mandatory")
_Cdx6500IBM2260StatCharInTotal_Type = Integer32
_Cdx6500IBM2260StatCharInTotal_Object = MibTableColumn
cdx6500IBM2260StatCharInTotal = _Cdx6500IBM2260StatCharInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 12),
    _Cdx6500IBM2260StatCharInTotal_Type()
)
cdx6500IBM2260StatCharInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260StatCharInTotal.setStatus("mandatory")
_Cdx6500IBM2260StatCharOutTotal_Type = Integer32
_Cdx6500IBM2260StatCharOutTotal_Object = MibTableColumn
cdx6500IBM2260StatCharOutTotal = _Cdx6500IBM2260StatCharOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 13),
    _Cdx6500IBM2260StatCharOutTotal_Type()
)
cdx6500IBM2260StatCharOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260StatCharOutTotal.setStatus("mandatory")
_Cdx6500IBM2260StatCharInSecond_Type = Integer32
_Cdx6500IBM2260StatCharInSecond_Object = MibTableColumn
cdx6500IBM2260StatCharInSecond = _Cdx6500IBM2260StatCharInSecond_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 14),
    _Cdx6500IBM2260StatCharInSecond_Type()
)
cdx6500IBM2260StatCharInSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260StatCharInSecond.setStatus("mandatory")
_Cdx6500IBM2260StatCharOutSecond_Type = Integer32
_Cdx6500IBM2260StatCharOutSecond_Object = MibTableColumn
cdx6500IBM2260StatCharOutSecond = _Cdx6500IBM2260StatCharOutSecond_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 15),
    _Cdx6500IBM2260StatCharOutSecond_Type()
)
cdx6500IBM2260StatCharOutSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260StatCharOutSecond.setStatus("mandatory")
_Cdx6500IBM2260StatPosAckIn_Type = Integer32
_Cdx6500IBM2260StatPosAckIn_Object = MibTableColumn
cdx6500IBM2260StatPosAckIn = _Cdx6500IBM2260StatPosAckIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 16),
    _Cdx6500IBM2260StatPosAckIn_Type()
)
cdx6500IBM2260StatPosAckIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260StatPosAckIn.setStatus("mandatory")
_Cdx6500IBM2260StatPosAckOut_Type = Integer32
_Cdx6500IBM2260StatPosAckOut_Object = MibTableColumn
cdx6500IBM2260StatPosAckOut = _Cdx6500IBM2260StatPosAckOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 17),
    _Cdx6500IBM2260StatPosAckOut_Type()
)
cdx6500IBM2260StatPosAckOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260StatPosAckOut.setStatus("mandatory")
_Cdx6500IBM2260StatNegAckIn_Type = Integer32
_Cdx6500IBM2260StatNegAckIn_Object = MibTableColumn
cdx6500IBM2260StatNegAckIn = _Cdx6500IBM2260StatNegAckIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 18),
    _Cdx6500IBM2260StatNegAckIn_Type()
)
cdx6500IBM2260StatNegAckIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260StatNegAckIn.setStatus("mandatory")
_Cdx6500IBM2260StatNegAckOut_Type = Integer32
_Cdx6500IBM2260StatNegAckOut_Object = MibTableColumn
cdx6500IBM2260StatNegAckOut = _Cdx6500IBM2260StatNegAckOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 19),
    _Cdx6500IBM2260StatNegAckOut_Type()
)
cdx6500IBM2260StatNegAckOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260StatNegAckOut.setStatus("mandatory")
_Cdx6500IBM2260StatMsgRetran_Type = Integer32
_Cdx6500IBM2260StatMsgRetran_Object = MibTableColumn
cdx6500IBM2260StatMsgRetran = _Cdx6500IBM2260StatMsgRetran_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 19, 1, 20),
    _Cdx6500IBM2260StatMsgRetran_Type()
)
cdx6500IBM2260StatMsgRetran.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500IBM2260StatMsgRetran.setStatus("mandatory")
_Cdx6500PSTStationProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTStationProtocolGroup = _Cdx6500PSTStationProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3)
)
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM2260-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PPCTIBM2260PortTable": cdx6500PPCTIBM2260PortTable,
       "cdx6500PPCTIBM2260PortEntry": cdx6500PPCTIBM2260PortEntry,
       "cdx6500IBM2260CfgPortNumber": cdx6500IBM2260CfgPortNumber,
       "cdx6500IBM2260CfgPadType": cdx6500IBM2260CfgPadType,
       "cdx6500IBM2260CfgPortSpeed": cdx6500IBM2260CfgPortSpeed,
       "cdx6500IBM2260CfgConnType": cdx6500IBM2260CfgConnType,
       "cdx6500IBM2260CfgNumDevice": cdx6500IBM2260CfgNumDevice,
       "cdx6500IBM2260CfgServiceTimer": cdx6500IBM2260CfgServiceTimer,
       "cdx6500IBM2260CfgThreshCtr": cdx6500IBM2260CfgThreshCtr,
       "cdx6500IBM2260CfgRespTimeout": cdx6500IBM2260CfgRespTimeout,
       "cdx6500IBM2260CfgPortSubAddr": cdx6500IBM2260CfgPortSubAddr,
       "cdx6500IBM2260CfgPortOpt": cdx6500IBM2260CfgPortOpt,
       "cdx6500IBM2260CfgRestConnDest": cdx6500IBM2260CfgRestConnDest,
       "cdx6500IBM2260CfgBillRec": cdx6500IBM2260CfgBillRec,
       "cdx6500IBM2260CfgElectricalInterfaceType": cdx6500IBM2260CfgElectricalInterfaceType,
       "cdx6500IBM2260CfgV24ElectricalInterfaceOption": cdx6500IBM2260CfgV24ElectricalInterfaceOption,
       "cdx6500IBM2260CfgHighSpeedElectricalInterfaceOption": cdx6500IBM2260CfgHighSpeedElectricalInterfaceOption,
       "cdx6500PCTStationProtocolGroup": cdx6500PCTStationProtocolGroup,
       "cdx6500SPCTIBM2260StationTable": cdx6500SPCTIBM2260StationTable,
       "cdx6500SPCTIBM2260StationEntry": cdx6500SPCTIBM2260StationEntry,
       "cdx6500IBM2260sCfgPortNum": cdx6500IBM2260sCfgPortNum,
       "cdx6500IBM2260sCfgStationNum": cdx6500IBM2260sCfgStationNum,
       "cdx6500IBM2260sType": cdx6500IBM2260sType,
       "cdx6500IBM2260sStationAddr1": cdx6500IBM2260sStationAddr1,
       "cdx6500IBM2260sStationAddr2": cdx6500IBM2260sStationAddr2,
       "cdx6500IBM2260sCallMnem": cdx6500IBM2260sCallMnem,
       "cdx6500IBM2260sStationEnable": cdx6500IBM2260sStationEnable,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPSTIBM2260PortTable": cdx6500PPSTIBM2260PortTable,
       "cdx6500PPSTIBM2260PortEntry": cdx6500PPSTIBM2260PortEntry,
       "cdx6500IBM2260StatPortNumber": cdx6500IBM2260StatPortNumber,
       "cdx6500IBM2260StatPortStatus": cdx6500IBM2260StatPortStatus,
       "cdx6500IBM2260StatPortState": cdx6500IBM2260StatPortState,
       "cdx6500IBM2260StatPortSpeed": cdx6500IBM2260StatPortSpeed,
       "cdx6500IBM2260StatPortUtilin": cdx6500IBM2260StatPortUtilin,
       "cdx6500IBM2260StatPortUtilOut": cdx6500IBM2260StatPortUtilOut,
       "cdx6500IBM2260StatParityErrors": cdx6500IBM2260StatParityErrors,
       "cdx6500IBM2260StatOverrunErrors": cdx6500IBM2260StatOverrunErrors,
       "cdx6500IBM2260StatFramingErrors": cdx6500IBM2260StatFramingErrors,
       "cdx6500IBM2260StatBCCErrors": cdx6500IBM2260StatBCCErrors,
       "cdx6500IBM2260StatNoResponse": cdx6500IBM2260StatNoResponse,
       "cdx6500IBM2260StatCharInTotal": cdx6500IBM2260StatCharInTotal,
       "cdx6500IBM2260StatCharOutTotal": cdx6500IBM2260StatCharOutTotal,
       "cdx6500IBM2260StatCharInSecond": cdx6500IBM2260StatCharInSecond,
       "cdx6500IBM2260StatCharOutSecond": cdx6500IBM2260StatCharOutSecond,
       "cdx6500IBM2260StatPosAckIn": cdx6500IBM2260StatPosAckIn,
       "cdx6500IBM2260StatPosAckOut": cdx6500IBM2260StatPosAckOut,
       "cdx6500IBM2260StatNegAckIn": cdx6500IBM2260StatNegAckIn,
       "cdx6500IBM2260StatNegAckOut": cdx6500IBM2260StatNegAckOut,
       "cdx6500IBM2260StatMsgRetran": cdx6500IBM2260StatMsgRetran,
       "cdx6500PSTStationProtocolGroup": cdx6500PSTStationProtocolGroup,
       "cdx6500Controls": cdx6500Controls}
)
