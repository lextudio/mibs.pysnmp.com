# SNMP MIB module (DSD-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DSD-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:35 2024
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
_Cdx6500CfgGeneralGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgGeneralGroup = _Cdx6500CfgGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2)
)
_Cdx6500GCTDSDTable_Object = MibTable
cdx6500GCTDSDTable = _Cdx6500GCTDSDTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 15)
)
if mibBuilder.loadTexts:
    cdx6500GCTDSDTable.setStatus("mandatory")
_Cdx6500dsdCfgEntry_Object = MibTableRow
cdx6500dsdCfgEntry = _Cdx6500dsdCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 15, 1)
)
cdx6500dsdCfgEntry.setIndexNames(
    (0, "DSD-OPT-MIB", "cdx6500dsdCfgMainChanNum"),
)
if mibBuilder.loadTexts:
    cdx6500dsdCfgEntry.setStatus("mandatory")


class _Cdx6500dsdCfgMainChanNum_Type(Integer32):
    """Custom type cdx6500dsdCfgMainChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Cdx6500dsdCfgMainChanNum_Type.__name__ = "Integer32"
_Cdx6500dsdCfgMainChanNum_Object = MibTableColumn
cdx6500dsdCfgMainChanNum = _Cdx6500dsdCfgMainChanNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 15, 1, 1),
    _Cdx6500dsdCfgMainChanNum_Type()
)
cdx6500dsdCfgMainChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dsdCfgMainChanNum.setStatus("mandatory")
_Cdx6500dsdMainChanAddr_Type = DisplayString
_Cdx6500dsdMainChanAddr_Object = MibTableColumn
cdx6500dsdMainChanAddr = _Cdx6500dsdMainChanAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 15, 1, 2),
    _Cdx6500dsdMainChanAddr_Type()
)
cdx6500dsdMainChanAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dsdMainChanAddr.setStatus("mandatory")


class _Cdx6500dsdCallControl_Type(Integer32):
    """Custom type cdx6500dsdCallControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("callOptAuto", 1),
          ("newvalCallOptNone", 50))
    )


_Cdx6500dsdCallControl_Type.__name__ = "Integer32"
_Cdx6500dsdCallControl_Object = MibTableColumn
cdx6500dsdCallControl = _Cdx6500dsdCallControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 15, 1, 3),
    _Cdx6500dsdCallControl_Type()
)
cdx6500dsdCallControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dsdCallControl.setStatus("mandatory")


class _Cdx6500dsdMainChanAutocallMnem_Type(DisplayString):
    """Custom type cdx6500dsdMainChanAutocallMnem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Cdx6500dsdMainChanAutocallMnem_Type.__name__ = "DisplayString"
_Cdx6500dsdMainChanAutocallMnem_Object = MibTableColumn
cdx6500dsdMainChanAutocallMnem = _Cdx6500dsdMainChanAutocallMnem_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 15, 1, 4),
    _Cdx6500dsdMainChanAutocallMnem_Type()
)
cdx6500dsdMainChanAutocallMnem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dsdMainChanAutocallMnem.setStatus("mandatory")


class _Cdx6500dsdAutocallTimeout_Type(Integer32):
    """Custom type cdx6500dsdAutocallTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Cdx6500dsdAutocallTimeout_Type.__name__ = "Integer32"
_Cdx6500dsdAutocallTimeout_Object = MibTableColumn
cdx6500dsdAutocallTimeout = _Cdx6500dsdAutocallTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 15, 1, 5),
    _Cdx6500dsdAutocallTimeout_Type()
)
cdx6500dsdAutocallTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dsdAutocallTimeout.setStatus("mandatory")


class _Cdx6500dsdMaxAutocallTries_Type(Integer32):
    """Custom type cdx6500dsdMaxAutocallTries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500dsdMaxAutocallTries_Type.__name__ = "Integer32"
_Cdx6500dsdMaxAutocallTries_Object = MibTableColumn
cdx6500dsdMaxAutocallTries = _Cdx6500dsdMaxAutocallTries_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 15, 1, 6),
    _Cdx6500dsdMaxAutocallTries_Type()
)
cdx6500dsdMaxAutocallTries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dsdMaxAutocallTries.setStatus("mandatory")
_Cdx6500dsdSubChanAddr_Type = DisplayString
_Cdx6500dsdSubChanAddr_Object = MibTableColumn
cdx6500dsdSubChanAddr = _Cdx6500dsdSubChanAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 15, 1, 7),
    _Cdx6500dsdSubChanAddr_Type()
)
cdx6500dsdSubChanAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dsdSubChanAddr.setStatus("mandatory")


class _Cdx6500dsdNumOfSubChans_Type(Integer32):
    """Custom type cdx6500dsdNumOfSubChans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Cdx6500dsdNumOfSubChans_Type.__name__ = "Integer32"
_Cdx6500dsdNumOfSubChans_Object = MibTableColumn
cdx6500dsdNumOfSubChans = _Cdx6500dsdNumOfSubChans_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 15, 1, 8),
    _Cdx6500dsdNumOfSubChans_Type()
)
cdx6500dsdNumOfSubChans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dsdNumOfSubChans.setStatus("mandatory")
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatOtherStatsGroup_ObjectIdentity = ObjectIdentity
cdx6500StatOtherStatsGroup = _Cdx6500StatOtherStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2)
)
_Cdx6500OSTDSDGroup_ObjectIdentity = ObjectIdentity
cdx6500OSTDSDGroup = _Cdx6500OSTDSDGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 2)
)
_Cdx6500dsdMainChanStatTable_Object = MibTable
cdx6500dsdMainChanStatTable = _Cdx6500dsdMainChanStatTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cdx6500dsdMainChanStatTable.setStatus("mandatory")
_Cdx6500dsdMainChanStatEntry_Object = MibTableRow
cdx6500dsdMainChanStatEntry = _Cdx6500dsdMainChanStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 2, 1, 1)
)
cdx6500dsdMainChanStatEntry.setIndexNames(
    (0, "DSD-OPT-MIB", "cdx6500dsdStatMainChanNum"),
)
if mibBuilder.loadTexts:
    cdx6500dsdMainChanStatEntry.setStatus("mandatory")


class _Cdx6500dsdStatMainChanNum_Type(Integer32):
    """Custom type cdx6500dsdStatMainChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Cdx6500dsdStatMainChanNum_Type.__name__ = "Integer32"
_Cdx6500dsdStatMainChanNum_Object = MibTableColumn
cdx6500dsdStatMainChanNum = _Cdx6500dsdStatMainChanNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 2, 1, 1, 1),
    _Cdx6500dsdStatMainChanNum_Type()
)
cdx6500dsdStatMainChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dsdStatMainChanNum.setStatus("mandatory")


class _Cdx6500dsdMainChanType_Type(Integer32):
    """Custom type cdx6500dsdMainChanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvalSvc", 50),
          ("pvc", 1))
    )


_Cdx6500dsdMainChanType_Type.__name__ = "Integer32"
_Cdx6500dsdMainChanType_Object = MibTableColumn
cdx6500dsdMainChanType = _Cdx6500dsdMainChanType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 2, 1, 1, 2),
    _Cdx6500dsdMainChanType_Type()
)
cdx6500dsdMainChanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dsdMainChanType.setStatus("mandatory")


class _Cdx6500dsdMainChanState_Type(Integer32):
    """Custom type cdx6500dsdMainChanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("dsdCalling", 1),
          ("dsdConnected", 2),
          ("newvalDsdDisconnected", 50))
    )


_Cdx6500dsdMainChanState_Type.__name__ = "Integer32"
_Cdx6500dsdMainChanState_Object = MibTableColumn
cdx6500dsdMainChanState = _Cdx6500dsdMainChanState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 2, 1, 1, 3),
    _Cdx6500dsdMainChanState_Type()
)
cdx6500dsdMainChanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dsdMainChanState.setStatus("mandatory")
_Cdx6500dsdMainChanRemoteAddr_Type = DisplayString
_Cdx6500dsdMainChanRemoteAddr_Object = MibTableColumn
cdx6500dsdMainChanRemoteAddr = _Cdx6500dsdMainChanRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 2, 1, 1, 4),
    _Cdx6500dsdMainChanRemoteAddr_Type()
)
cdx6500dsdMainChanRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dsdMainChanRemoteAddr.setStatus("mandatory")
_Cdx6500dsdMainChanCharIn_Type = Counter32
_Cdx6500dsdMainChanCharIn_Object = MibTableColumn
cdx6500dsdMainChanCharIn = _Cdx6500dsdMainChanCharIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 2, 1, 1, 5),
    _Cdx6500dsdMainChanCharIn_Type()
)
cdx6500dsdMainChanCharIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dsdMainChanCharIn.setStatus("mandatory")
_Cdx6500dsdMainChanCharOut_Type = Counter32
_Cdx6500dsdMainChanCharOut_Object = MibTableColumn
cdx6500dsdMainChanCharOut = _Cdx6500dsdMainChanCharOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 2, 1, 1, 6),
    _Cdx6500dsdMainChanCharOut_Type()
)
cdx6500dsdMainChanCharOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dsdMainChanCharOut.setStatus("mandatory")
_Cdx6500dsdMainChanPktIn_Type = Counter32
_Cdx6500dsdMainChanPktIn_Object = MibTableColumn
cdx6500dsdMainChanPktIn = _Cdx6500dsdMainChanPktIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 2, 1, 1, 7),
    _Cdx6500dsdMainChanPktIn_Type()
)
cdx6500dsdMainChanPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dsdMainChanPktIn.setStatus("mandatory")
_Cdx6500dsdMainChanPktOut_Type = Counter32
_Cdx6500dsdMainChanPktOut_Object = MibTableColumn
cdx6500dsdMainChanPktOut = _Cdx6500dsdMainChanPktOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 2, 1, 1, 8),
    _Cdx6500dsdMainChanPktOut_Type()
)
cdx6500dsdMainChanPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dsdMainChanPktOut.setStatus("mandatory")
_Cdx6500dsdSubChanStatTable_Object = MibTable
cdx6500dsdSubChanStatTable = _Cdx6500dsdSubChanStatTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cdx6500dsdSubChanStatTable.setStatus("mandatory")
_Cdx6500dsdSubChanStatEntry_Object = MibTableRow
cdx6500dsdSubChanStatEntry = _Cdx6500dsdSubChanStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 2, 2, 1)
)
cdx6500dsdSubChanStatEntry.setIndexNames(
    (0, "DSD-OPT-MIB", "cdx6500dsdDropStatMainChanNum"),
    (0, "DSD-OPT-MIB", "cdx6500dsdDropStatSubChanNum"),
)
if mibBuilder.loadTexts:
    cdx6500dsdSubChanStatEntry.setStatus("mandatory")


class _Cdx6500dsdDropStatMainChanNum_Type(Integer32):
    """Custom type cdx6500dsdDropStatMainChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Cdx6500dsdDropStatMainChanNum_Type.__name__ = "Integer32"
_Cdx6500dsdDropStatMainChanNum_Object = MibTableColumn
cdx6500dsdDropStatMainChanNum = _Cdx6500dsdDropStatMainChanNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 2, 2, 1, 1),
    _Cdx6500dsdDropStatMainChanNum_Type()
)
cdx6500dsdDropStatMainChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dsdDropStatMainChanNum.setStatus("mandatory")


class _Cdx6500dsdDropStatSubChanNum_Type(Integer32):
    """Custom type cdx6500dsdDropStatSubChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Cdx6500dsdDropStatSubChanNum_Type.__name__ = "Integer32"
_Cdx6500dsdDropStatSubChanNum_Object = MibTableColumn
cdx6500dsdDropStatSubChanNum = _Cdx6500dsdDropStatSubChanNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 2, 2, 1, 2),
    _Cdx6500dsdDropStatSubChanNum_Type()
)
cdx6500dsdDropStatSubChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dsdDropStatSubChanNum.setStatus("mandatory")


class _Cdx6500dsdSubChanType_Type(Integer32):
    """Custom type cdx6500dsdSubChanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvalSvc", 50),
          ("pvc", 1))
    )


_Cdx6500dsdSubChanType_Type.__name__ = "Integer32"
_Cdx6500dsdSubChanType_Object = MibTableColumn
cdx6500dsdSubChanType = _Cdx6500dsdSubChanType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 2, 2, 1, 3),
    _Cdx6500dsdSubChanType_Type()
)
cdx6500dsdSubChanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dsdSubChanType.setStatus("mandatory")


class _Cdx6500dsdSubChanState_Type(Integer32):
    """Custom type cdx6500dsdSubChanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("dsdCalling", 1),
          ("dsdConnected", 2),
          ("newvalDsdDisconnected", 50))
    )


_Cdx6500dsdSubChanState_Type.__name__ = "Integer32"
_Cdx6500dsdSubChanState_Object = MibTableColumn
cdx6500dsdSubChanState = _Cdx6500dsdSubChanState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 2, 2, 1, 4),
    _Cdx6500dsdSubChanState_Type()
)
cdx6500dsdSubChanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dsdSubChanState.setStatus("mandatory")
_Cdx6500dsdSubChanRemoteAddr_Type = DisplayString
_Cdx6500dsdSubChanRemoteAddr_Object = MibTableColumn
cdx6500dsdSubChanRemoteAddr = _Cdx6500dsdSubChanRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 2, 2, 1, 5),
    _Cdx6500dsdSubChanRemoteAddr_Type()
)
cdx6500dsdSubChanRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dsdSubChanRemoteAddr.setStatus("mandatory")
_Cdx6500dsdSubChanCharIn_Type = Counter32
_Cdx6500dsdSubChanCharIn_Object = MibTableColumn
cdx6500dsdSubChanCharIn = _Cdx6500dsdSubChanCharIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 2, 2, 1, 6),
    _Cdx6500dsdSubChanCharIn_Type()
)
cdx6500dsdSubChanCharIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dsdSubChanCharIn.setStatus("mandatory")
_Cdx6500dsdSubChanCharOut_Type = Counter32
_Cdx6500dsdSubChanCharOut_Object = MibTableColumn
cdx6500dsdSubChanCharOut = _Cdx6500dsdSubChanCharOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 2, 2, 1, 7),
    _Cdx6500dsdSubChanCharOut_Type()
)
cdx6500dsdSubChanCharOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dsdSubChanCharOut.setStatus("mandatory")
_Cdx6500dsdSubChanPktIn_Type = Counter32
_Cdx6500dsdSubChanPktIn_Object = MibTableColumn
cdx6500dsdSubChanPktIn = _Cdx6500dsdSubChanPktIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 2, 2, 1, 8),
    _Cdx6500dsdSubChanPktIn_Type()
)
cdx6500dsdSubChanPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dsdSubChanPktIn.setStatus("mandatory")
_Cdx6500dsdSubChanPktOut_Type = Counter32
_Cdx6500dsdSubChanPktOut_Object = MibTableColumn
cdx6500dsdSubChanPktOut = _Cdx6500dsdSubChanPktOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 2, 2, 1, 9),
    _Cdx6500dsdSubChanPktOut_Type()
)
cdx6500dsdSubChanPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dsdSubChanPktOut.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)
_Cdx6500dsdControls_ObjectIdentity = ObjectIdentity
cdx6500dsdControls = _Cdx6500dsdControls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 3)
)


class _Cdx6500dsdBoot_Type(Integer32):
    """Custom type cdx6500dsdBoot based on Integer32"""
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


_Cdx6500dsdBoot_Type.__name__ = "Integer32"
_Cdx6500dsdBoot_Object = MibScalar
cdx6500dsdBoot = _Cdx6500dsdBoot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 3, 1),
    _Cdx6500dsdBoot_Type()
)
cdx6500dsdBoot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500dsdBoot.setStatus("mandatory")


class _Cdx6500dsdResetStats_Type(Integer32):
    """Custom type cdx6500dsdResetStats based on Integer32"""
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


_Cdx6500dsdResetStats_Type.__name__ = "Integer32"
_Cdx6500dsdResetStats_Object = MibScalar
cdx6500dsdResetStats = _Cdx6500dsdResetStats_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 3, 2),
    _Cdx6500dsdResetStats_Type()
)
cdx6500dsdResetStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500dsdResetStats.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DSD-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgGeneralGroup": cdx6500CfgGeneralGroup,
       "cdx6500GCTDSDTable": cdx6500GCTDSDTable,
       "cdx6500dsdCfgEntry": cdx6500dsdCfgEntry,
       "cdx6500dsdCfgMainChanNum": cdx6500dsdCfgMainChanNum,
       "cdx6500dsdMainChanAddr": cdx6500dsdMainChanAddr,
       "cdx6500dsdCallControl": cdx6500dsdCallControl,
       "cdx6500dsdMainChanAutocallMnem": cdx6500dsdMainChanAutocallMnem,
       "cdx6500dsdAutocallTimeout": cdx6500dsdAutocallTimeout,
       "cdx6500dsdMaxAutocallTries": cdx6500dsdMaxAutocallTries,
       "cdx6500dsdSubChanAddr": cdx6500dsdSubChanAddr,
       "cdx6500dsdNumOfSubChans": cdx6500dsdNumOfSubChans,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatOtherStatsGroup": cdx6500StatOtherStatsGroup,
       "cdx6500OSTDSDGroup": cdx6500OSTDSDGroup,
       "cdx6500dsdMainChanStatTable": cdx6500dsdMainChanStatTable,
       "cdx6500dsdMainChanStatEntry": cdx6500dsdMainChanStatEntry,
       "cdx6500dsdStatMainChanNum": cdx6500dsdStatMainChanNum,
       "cdx6500dsdMainChanType": cdx6500dsdMainChanType,
       "cdx6500dsdMainChanState": cdx6500dsdMainChanState,
       "cdx6500dsdMainChanRemoteAddr": cdx6500dsdMainChanRemoteAddr,
       "cdx6500dsdMainChanCharIn": cdx6500dsdMainChanCharIn,
       "cdx6500dsdMainChanCharOut": cdx6500dsdMainChanCharOut,
       "cdx6500dsdMainChanPktIn": cdx6500dsdMainChanPktIn,
       "cdx6500dsdMainChanPktOut": cdx6500dsdMainChanPktOut,
       "cdx6500dsdSubChanStatTable": cdx6500dsdSubChanStatTable,
       "cdx6500dsdSubChanStatEntry": cdx6500dsdSubChanStatEntry,
       "cdx6500dsdDropStatMainChanNum": cdx6500dsdDropStatMainChanNum,
       "cdx6500dsdDropStatSubChanNum": cdx6500dsdDropStatSubChanNum,
       "cdx6500dsdSubChanType": cdx6500dsdSubChanType,
       "cdx6500dsdSubChanState": cdx6500dsdSubChanState,
       "cdx6500dsdSubChanRemoteAddr": cdx6500dsdSubChanRemoteAddr,
       "cdx6500dsdSubChanCharIn": cdx6500dsdSubChanCharIn,
       "cdx6500dsdSubChanCharOut": cdx6500dsdSubChanCharOut,
       "cdx6500dsdSubChanPktIn": cdx6500dsdSubChanPktIn,
       "cdx6500dsdSubChanPktOut": cdx6500dsdSubChanPktOut,
       "cdx6500Controls": cdx6500Controls,
       "cdx6500dsdControls": cdx6500dsdControls,
       "cdx6500dsdBoot": cdx6500dsdBoot,
       "cdx6500dsdResetStats": cdx6500dsdResetStats}
)
