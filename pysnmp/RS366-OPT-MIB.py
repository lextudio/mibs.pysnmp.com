# SNMP MIB module (RS366-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RS366-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:25 2024
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
_Cdx6500PPCTRS366PortTable_Object = MibTable
cdx6500PPCTRS366PortTable = _Cdx6500PPCTRS366PortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 21)
)
if mibBuilder.loadTexts:
    cdx6500PPCTRS366PortTable.setStatus("mandatory")
_Cdx6500PPCTRS366PortEntry_Object = MibTableRow
cdx6500PPCTRS366PortEntry = _Cdx6500PPCTRS366PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 21, 1)
)
cdx6500PPCTRS366PortEntry.setIndexNames(
    (0, "RS366-OPT-MIB", "cdx6500RS366CfgPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTRS366PortEntry.setStatus("mandatory")


class _Cdx6500RS366CfgPortNumber_Type(Integer32):
    """Custom type cdx6500RS366CfgPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_Cdx6500RS366CfgPortNumber_Type.__name__ = "Integer32"
_Cdx6500RS366CfgPortNumber_Object = MibTableColumn
cdx6500RS366CfgPortNumber = _Cdx6500RS366CfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 21, 1, 1),
    _Cdx6500RS366CfgPortNumber_Type()
)
cdx6500RS366CfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500RS366CfgPortNumber.setStatus("mandatory")


class _Cdx6500RS366CfgADataPortNumber_Type(Integer32):
    """Custom type cdx6500RS366CfgADataPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500RS366CfgADataPortNumber_Type.__name__ = "Integer32"
_Cdx6500RS366CfgADataPortNumber_Object = MibTableColumn
cdx6500RS366CfgADataPortNumber = _Cdx6500RS366CfgADataPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 21, 1, 2),
    _Cdx6500RS366CfgADataPortNumber_Type()
)
cdx6500RS366CfgADataPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500RS366CfgADataPortNumber.setStatus("mandatory")


class _Cdx6500RS366CfgContXferMode_Type(Integer32):
    """Custom type cdx6500RS366CfgContXferMode based on Integer32"""
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
        *(("modeebt", 2),
          ("modeeon", 1),
          ("modenull", 0),
          ("newvalmodenull", 50))
    )


_Cdx6500RS366CfgContXferMode_Type.__name__ = "Integer32"
_Cdx6500RS366CfgContXferMode_Object = MibTableColumn
cdx6500RS366CfgContXferMode = _Cdx6500RS366CfgContXferMode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 21, 1, 3),
    _Cdx6500RS366CfgContXferMode_Type()
)
cdx6500RS366CfgContXferMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500RS366CfgContXferMode.setStatus("mandatory")


class _Cdx6500RS366CfgMaxAddrDigits_Type(Integer32):
    """Custom type cdx6500RS366CfgMaxAddrDigits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Cdx6500RS366CfgMaxAddrDigits_Type.__name__ = "Integer32"
_Cdx6500RS366CfgMaxAddrDigits_Object = MibTableColumn
cdx6500RS366CfgMaxAddrDigits = _Cdx6500RS366CfgMaxAddrDigits_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 21, 1, 4),
    _Cdx6500RS366CfgMaxAddrDigits_Type()
)
cdx6500RS366CfgMaxAddrDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500RS366CfgMaxAddrDigits.setStatus("mandatory")


class _Cdx6500RS366CfgMaxRespTime_Type(Integer32):
    """Custom type cdx6500RS366CfgMaxRespTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              32,
              48,
              50,
              96)
        )
    )
    namedValues = NamedValues(
        *(("newvalSec0", 50),
          ("sec0", 0),
          ("sec32", 32),
          ("sec48", 48),
          ("sec96", 96))
    )


_Cdx6500RS366CfgMaxRespTime_Type.__name__ = "Integer32"
_Cdx6500RS366CfgMaxRespTime_Object = MibTableColumn
cdx6500RS366CfgMaxRespTime = _Cdx6500RS366CfgMaxRespTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 21, 1, 5),
    _Cdx6500RS366CfgMaxRespTime_Type()
)
cdx6500RS366CfgMaxRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500RS366CfgMaxRespTime.setStatus("mandatory")


class _Cdx6500RS366CfgElectricalInterfaceType_Type(Integer32):
    """Custom type cdx6500RS366CfgElectricalInterfaceType based on Integer32"""
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


_Cdx6500RS366CfgElectricalInterfaceType_Type.__name__ = "Integer32"
_Cdx6500RS366CfgElectricalInterfaceType_Object = MibTableColumn
cdx6500RS366CfgElectricalInterfaceType = _Cdx6500RS366CfgElectricalInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 21, 1, 6),
    _Cdx6500RS366CfgElectricalInterfaceType_Type()
)
cdx6500RS366CfgElectricalInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500RS366CfgElectricalInterfaceType.setStatus("mandatory")


class _Cdx6500RS366CfgV24ElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500RS366CfgV24ElectricalInterfaceOption based on Integer32"""
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


_Cdx6500RS366CfgV24ElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500RS366CfgV24ElectricalInterfaceOption_Object = MibTableColumn
cdx6500RS366CfgV24ElectricalInterfaceOption = _Cdx6500RS366CfgV24ElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 21, 1, 7),
    _Cdx6500RS366CfgV24ElectricalInterfaceOption_Type()
)
cdx6500RS366CfgV24ElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500RS366CfgV24ElectricalInterfaceOption.setStatus("mandatory")


class _Cdx6500RS366CfgHighSpeedElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500RS366CfgHighSpeedElectricalInterfaceOption based on Integer32"""
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


_Cdx6500RS366CfgHighSpeedElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500RS366CfgHighSpeedElectricalInterfaceOption_Object = MibTableColumn
cdx6500RS366CfgHighSpeedElectricalInterfaceOption = _Cdx6500RS366CfgHighSpeedElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 21, 1, 8),
    _Cdx6500RS366CfgHighSpeedElectricalInterfaceOption_Type()
)
cdx6500RS366CfgHighSpeedElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500RS366CfgHighSpeedElectricalInterfaceOption.setStatus("mandatory")
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
_Cdx6500PPSTRS366PortTable_Object = MibTable
cdx6500PPSTRS366PortTable = _Cdx6500PPSTRS366PortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 22)
)
if mibBuilder.loadTexts:
    cdx6500PPSTRS366PortTable.setStatus("mandatory")
_Cdx6500PPSTRS366PortEntry_Object = MibTableRow
cdx6500PPSTRS366PortEntry = _Cdx6500PPSTRS366PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 22, 1)
)
cdx6500PPSTRS366PortEntry.setIndexNames(
    (0, "RS366-OPT-MIB", "cdx6500RS366StatPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTRS366PortEntry.setStatus("mandatory")


class _Cdx6500RS366StatPortNumber_Type(Integer32):
    """Custom type cdx6500RS366StatPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_Cdx6500RS366StatPortNumber_Type.__name__ = "Integer32"
_Cdx6500RS366StatPortNumber_Object = MibTableColumn
cdx6500RS366StatPortNumber = _Cdx6500RS366StatPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 22, 1, 1),
    _Cdx6500RS366StatPortNumber_Type()
)
cdx6500RS366StatPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500RS366StatPortNumber.setStatus("mandatory")
_Cdx6500RS366StatPortStatus_Type = DisplayString
_Cdx6500RS366StatPortStatus_Object = MibTableColumn
cdx6500RS366StatPortStatus = _Cdx6500RS366StatPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 22, 1, 2),
    _Cdx6500RS366StatPortStatus_Type()
)
cdx6500RS366StatPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500RS366StatPortStatus.setStatus("mandatory")
_Cdx6500RS366StatPortState_Type = DisplayString
_Cdx6500RS366StatPortState_Object = MibTableColumn
cdx6500RS366StatPortState = _Cdx6500RS366StatPortState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 22, 1, 3),
    _Cdx6500RS366StatPortState_Type()
)
cdx6500RS366StatPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500RS366StatPortState.setStatus("mandatory")
_Cdx6500RS366StatDataNum_Type = Integer32
_Cdx6500RS366StatDataNum_Object = MibTableColumn
cdx6500RS366StatDataNum = _Cdx6500RS366StatDataNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 22, 1, 4),
    _Cdx6500RS366StatDataNum_Type()
)
cdx6500RS366StatDataNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500RS366StatDataNum.setStatus("mandatory")
_Cdx6500RS366StatTotalCalls_Type = Integer32
_Cdx6500RS366StatTotalCalls_Object = MibTableColumn
cdx6500RS366StatTotalCalls = _Cdx6500RS366StatTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 22, 1, 5),
    _Cdx6500RS366StatTotalCalls_Type()
)
cdx6500RS366StatTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500RS366StatTotalCalls.setStatus("mandatory")
_Cdx6500RS366StatFailedCalls_Type = Integer32
_Cdx6500RS366StatFailedCalls_Object = MibTableColumn
cdx6500RS366StatFailedCalls = _Cdx6500RS366StatFailedCalls_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 22, 1, 6),
    _Cdx6500RS366StatFailedCalls_Type()
)
cdx6500RS366StatFailedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500RS366StatFailedCalls.setStatus("mandatory")
_Cdx6500RS366StatTotalTimeouts_Type = Integer32
_Cdx6500RS366StatTotalTimeouts_Object = MibTableColumn
cdx6500RS366StatTotalTimeouts = _Cdx6500RS366StatTotalTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 22, 1, 7),
    _Cdx6500RS366StatTotalTimeouts_Type()
)
cdx6500RS366StatTotalTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500RS366StatTotalTimeouts.setStatus("mandatory")
_Cdx6500RS366StatTotalIllegalDigits_Type = Integer32
_Cdx6500RS366StatTotalIllegalDigits_Object = MibTableColumn
cdx6500RS366StatTotalIllegalDigits = _Cdx6500RS366StatTotalIllegalDigits_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 22, 1, 8),
    _Cdx6500RS366StatTotalIllegalDigits_Type()
)
cdx6500RS366StatTotalIllegalDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500RS366StatTotalIllegalDigits.setStatus("mandatory")
_Cdx6500RS366StatPortConnected_Type = DisplayString
_Cdx6500RS366StatPortConnected_Object = MibTableColumn
cdx6500RS366StatPortConnected = _Cdx6500RS366StatPortConnected_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 22, 1, 9),
    _Cdx6500RS366StatPortConnected_Type()
)
cdx6500RS366StatPortConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500RS366StatPortConnected.setStatus("mandatory")
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
    "RS366-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PPCTRS366PortTable": cdx6500PPCTRS366PortTable,
       "cdx6500PPCTRS366PortEntry": cdx6500PPCTRS366PortEntry,
       "cdx6500RS366CfgPortNumber": cdx6500RS366CfgPortNumber,
       "cdx6500RS366CfgADataPortNumber": cdx6500RS366CfgADataPortNumber,
       "cdx6500RS366CfgContXferMode": cdx6500RS366CfgContXferMode,
       "cdx6500RS366CfgMaxAddrDigits": cdx6500RS366CfgMaxAddrDigits,
       "cdx6500RS366CfgMaxRespTime": cdx6500RS366CfgMaxRespTime,
       "cdx6500RS366CfgElectricalInterfaceType": cdx6500RS366CfgElectricalInterfaceType,
       "cdx6500RS366CfgV24ElectricalInterfaceOption": cdx6500RS366CfgV24ElectricalInterfaceOption,
       "cdx6500RS366CfgHighSpeedElectricalInterfaceOption": cdx6500RS366CfgHighSpeedElectricalInterfaceOption,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPSTRS366PortTable": cdx6500PPSTRS366PortTable,
       "cdx6500PPSTRS366PortEntry": cdx6500PPSTRS366PortEntry,
       "cdx6500RS366StatPortNumber": cdx6500RS366StatPortNumber,
       "cdx6500RS366StatPortStatus": cdx6500RS366StatPortStatus,
       "cdx6500RS366StatPortState": cdx6500RS366StatPortState,
       "cdx6500RS366StatDataNum": cdx6500RS366StatDataNum,
       "cdx6500RS366StatTotalCalls": cdx6500RS366StatTotalCalls,
       "cdx6500RS366StatFailedCalls": cdx6500RS366StatFailedCalls,
       "cdx6500RS366StatTotalTimeouts": cdx6500RS366StatTotalTimeouts,
       "cdx6500RS366StatTotalIllegalDigits": cdx6500RS366StatTotalIllegalDigits,
       "cdx6500RS366StatPortConnected": cdx6500RS366StatPortConnected,
       "cdx6500Controls": cdx6500Controls}
)
