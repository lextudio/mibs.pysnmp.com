# SNMP MIB module (EIA-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EIA-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:42 2024
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
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatOtherStatsGroup_ObjectIdentity = ObjectIdentity
cdx6500StatOtherStatsGroup = _Cdx6500StatOtherStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2)
)
_Cdx6500StatEIATable_Object = MibTable
cdx6500StatEIATable = _Cdx6500StatEIATable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 7)
)
if mibBuilder.loadTexts:
    cdx6500StatEIATable.setStatus("mandatory")
_Cdx6500StatEIAEntry_Object = MibTableRow
cdx6500StatEIAEntry = _Cdx6500StatEIAEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 7, 1)
)
cdx6500StatEIAEntry.setIndexNames(
    (0, "EIA-OPT-MIB", "cdx6500StatEIAEntryPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500StatEIAEntry.setStatus("mandatory")


class _Cdx6500StatEIAEntryPortNumber_Type(Integer32):
    """Custom type cdx6500StatEIAEntryPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500StatEIAEntryPortNumber_Type.__name__ = "Integer32"
_Cdx6500StatEIAEntryPortNumber_Object = MibTableColumn
cdx6500StatEIAEntryPortNumber = _Cdx6500StatEIAEntryPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 7, 1, 1),
    _Cdx6500StatEIAEntryPortNumber_Type()
)
cdx6500StatEIAEntryPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatEIAEntryPortNumber.setStatus("mandatory")


class _Cdx6500StatEIAEntryDimType_Type(Integer32):
    """Custom type cdx6500StatEIAEntryDimType based on Integer32"""
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
              10,
              50)
        )
    )
    namedValues = NamedValues(
        *(("dimTypeDsu", 8),
          ("dimTypeEia232d", 2),
          ("dimTypeEia530", 7),
          ("dimTypeI430", 10),
          ("dimTypeNone", 0),
          ("dimTypeNotInstalled", 1),
          ("dimTypeV11", 6),
          ("dimTypeV35", 4),
          ("dimTypeV36", 5),
          ("dimTypeX21", 3),
          ("newvalDimTypeNone", 50))
    )


_Cdx6500StatEIAEntryDimType_Type.__name__ = "Integer32"
_Cdx6500StatEIAEntryDimType_Object = MibTableColumn
cdx6500StatEIAEntryDimType = _Cdx6500StatEIAEntryDimType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 7, 1, 2),
    _Cdx6500StatEIAEntryDimType_Type()
)
cdx6500StatEIAEntryDimType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatEIAEntryDimType.setStatus("mandatory")


class _Cdx6500StatEIAEntryDimCfgn_Type(Integer32):
    """Custom type cdx6500StatEIAEntryDimCfgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("dimCfgnDce", 1),
          ("dimCfgnDte", 0),
          ("newvalDimCfgnDte", 50))
    )


_Cdx6500StatEIAEntryDimCfgn_Type.__name__ = "Integer32"
_Cdx6500StatEIAEntryDimCfgn_Object = MibTableColumn
cdx6500StatEIAEntryDimCfgn = _Cdx6500StatEIAEntryDimCfgn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 7, 1, 3),
    _Cdx6500StatEIAEntryDimCfgn_Type()
)
cdx6500StatEIAEntryDimCfgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatEIAEntryDimCfgn.setStatus("mandatory")
_Cdx6500StatEIAEntryEiaState_Type = DisplayString
_Cdx6500StatEIAEntryEiaState_Object = MibTableColumn
cdx6500StatEIAEntryEiaState = _Cdx6500StatEIAEntryEiaState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 7, 1, 4),
    _Cdx6500StatEIAEntryEiaState_Type()
)
cdx6500StatEIAEntryEiaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatEIAEntryEiaState.setStatus("mandatory")
_Cdx6500StatEIAEntryConnType_Type = DisplayString
_Cdx6500StatEIAEntryConnType_Object = MibTableColumn
cdx6500StatEIAEntryConnType = _Cdx6500StatEIAEntryConnType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 7, 1, 5),
    _Cdx6500StatEIAEntryConnType_Type()
)
cdx6500StatEIAEntryConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatEIAEntryConnType.setStatus("mandatory")
_Cdx6500StatEIAEntrySignalStatus_Type = DisplayString
_Cdx6500StatEIAEntrySignalStatus_Object = MibTableColumn
cdx6500StatEIAEntrySignalStatus = _Cdx6500StatEIAEntrySignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 7, 1, 6),
    _Cdx6500StatEIAEntrySignalStatus_Type()
)
cdx6500StatEIAEntrySignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatEIAEntrySignalStatus.setStatus("mandatory")
_IsgVGIsdnEIAStatTable_Object = MibTable
isgVGIsdnEIAStatTable = _IsgVGIsdnEIAStatTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 8)
)
if mibBuilder.loadTexts:
    isgVGIsdnEIAStatTable.setStatus("mandatory")
_IsgVGIsdnEIAStatEntry_Object = MibTableRow
isgVGIsdnEIAStatEntry = _IsgVGIsdnEIAStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 8, 1)
)
isgVGIsdnEIAStatEntry.setIndexNames(
    (0, "EIA-OPT-MIB", "isgVGIsdnEIAStatPortNum"),
)
if mibBuilder.loadTexts:
    isgVGIsdnEIAStatEntry.setStatus("mandatory")
_IsgVGIsdnEIAStatPortNum_Type = Integer32
_IsgVGIsdnEIAStatPortNum_Object = MibTableColumn
isgVGIsdnEIAStatPortNum = _IsgVGIsdnEIAStatPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 8, 1, 1),
    _IsgVGIsdnEIAStatPortNum_Type()
)
isgVGIsdnEIAStatPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnEIAStatPortNum.setStatus("mandatory")


class _IsgVGIsdnEIAStatDimType_Type(Integer32):
    """Custom type isgVGIsdnEIAStatDimType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            9
        )
    )
    namedValues = NamedValues(
        ("dimTypeIsdn", 9)
    )


_IsgVGIsdnEIAStatDimType_Type.__name__ = "Integer32"
_IsgVGIsdnEIAStatDimType_Object = MibTableColumn
isgVGIsdnEIAStatDimType = _IsgVGIsdnEIAStatDimType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 8, 1, 2),
    _IsgVGIsdnEIAStatDimType_Type()
)
isgVGIsdnEIAStatDimType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnEIAStatDimType.setStatus("mandatory")


class _IsgVGIsdnEIAStatDimCfgn_Type(Integer32):
    """Custom type isgVGIsdnEIAStatDimCfgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("dimIsdnST", 0),
          ("dimIsdnU", 1),
          ("newvalDimIsdnST", 50))
    )


_IsgVGIsdnEIAStatDimCfgn_Type.__name__ = "Integer32"
_IsgVGIsdnEIAStatDimCfgn_Object = MibTableColumn
isgVGIsdnEIAStatDimCfgn = _IsgVGIsdnEIAStatDimCfgn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 8, 1, 3),
    _IsgVGIsdnEIAStatDimCfgn_Type()
)
isgVGIsdnEIAStatDimCfgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnEIAStatDimCfgn.setStatus("mandatory")
_IsgVGIsdnEIAStatTEI_Type = DisplayString
_IsgVGIsdnEIAStatTEI_Object = MibTableColumn
isgVGIsdnEIAStatTEI = _IsgVGIsdnEIAStatTEI_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 8, 1, 4),
    _IsgVGIsdnEIAStatTEI_Type()
)
isgVGIsdnEIAStatTEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnEIAStatTEI.setStatus("mandatory")


class _IsgVGIsdnEIAStatSPBU_Type(Integer32):
    """Custom type isgVGIsdnEIAStatSPBU based on Integer32"""
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
        *(("backup", 1),
          ("disabled", 2),
          ("main", 0),
          ("newvalMain", 50))
    )


_IsgVGIsdnEIAStatSPBU_Type.__name__ = "Integer32"
_IsgVGIsdnEIAStatSPBU_Object = MibTableColumn
isgVGIsdnEIAStatSPBU = _IsgVGIsdnEIAStatSPBU_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 8, 1, 5),
    _IsgVGIsdnEIAStatSPBU_Type()
)
isgVGIsdnEIAStatSPBU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnEIAStatSPBU.setStatus("mandatory")


class _IsgVGIsdnEIAStatL1State_Type(Integer32):
    """Custom type isgVGIsdnEIAStatL1State based on Integer32"""
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
              50)
        )
    )
    namedValues = NamedValues(
        *(("l12BDLoop", 6),
          ("l1Active", 2),
          ("l1B1B2Loop", 5),
          ("l1B1Loop", 3),
          ("l1B2Loop", 4),
          ("l1Deactive", 1),
          ("l1Setup", 0),
          ("newvalL1Setup", 50),
          ("unknownState", 7))
    )


_IsgVGIsdnEIAStatL1State_Type.__name__ = "Integer32"
_IsgVGIsdnEIAStatL1State_Object = MibTableColumn
isgVGIsdnEIAStatL1State = _IsgVGIsdnEIAStatL1State_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 8, 1, 6),
    _IsgVGIsdnEIAStatL1State_Type()
)
isgVGIsdnEIAStatL1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnEIAStatL1State.setStatus("mandatory")


class _IsgVGIsdnEIAStatChanType_Type(Integer32):
    """Custom type isgVGIsdnEIAStatChanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              50)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("isdn2B", 4),
          ("isdnB", 5),
          ("isdnB1", 2),
          ("isdnB2", 3),
          ("isdnD", 1),
          ("newvalError", 50))
    )


_IsgVGIsdnEIAStatChanType_Type.__name__ = "Integer32"
_IsgVGIsdnEIAStatChanType_Object = MibTableColumn
isgVGIsdnEIAStatChanType = _IsgVGIsdnEIAStatChanType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 8, 1, 7),
    _IsgVGIsdnEIAStatChanType_Type()
)
isgVGIsdnEIAStatChanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnEIAStatChanType.setStatus("mandatory")


class _IsgVGIsdnEIAStatAccType_Type(Integer32):
    """Custom type isgVGIsdnEIAStatAccType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              50)
        )
    )
    namedValues = NamedValues(
        *(("cktMode", 1),
          ("dPckDisabled", 4),
          ("dPckEnabled", 3),
          ("newvalPermanent", 50),
          ("notConnected", 5),
          ("permanent", 0),
          ("pktMode", 2))
    )


_IsgVGIsdnEIAStatAccType_Type.__name__ = "Integer32"
_IsgVGIsdnEIAStatAccType_Object = MibTableColumn
isgVGIsdnEIAStatAccType = _IsgVGIsdnEIAStatAccType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 8, 1, 8),
    _IsgVGIsdnEIAStatAccType_Type()
)
isgVGIsdnEIAStatAccType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnEIAStatAccType.setStatus("mandatory")
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
    "EIA-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgGeneralGroup": cdx6500CfgGeneralGroup,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatOtherStatsGroup": cdx6500StatOtherStatsGroup,
       "cdx6500StatEIATable": cdx6500StatEIATable,
       "cdx6500StatEIAEntry": cdx6500StatEIAEntry,
       "cdx6500StatEIAEntryPortNumber": cdx6500StatEIAEntryPortNumber,
       "cdx6500StatEIAEntryDimType": cdx6500StatEIAEntryDimType,
       "cdx6500StatEIAEntryDimCfgn": cdx6500StatEIAEntryDimCfgn,
       "cdx6500StatEIAEntryEiaState": cdx6500StatEIAEntryEiaState,
       "cdx6500StatEIAEntryConnType": cdx6500StatEIAEntryConnType,
       "cdx6500StatEIAEntrySignalStatus": cdx6500StatEIAEntrySignalStatus,
       "isgVGIsdnEIAStatTable": isgVGIsdnEIAStatTable,
       "isgVGIsdnEIAStatEntry": isgVGIsdnEIAStatEntry,
       "isgVGIsdnEIAStatPortNum": isgVGIsdnEIAStatPortNum,
       "isgVGIsdnEIAStatDimType": isgVGIsdnEIAStatDimType,
       "isgVGIsdnEIAStatDimCfgn": isgVGIsdnEIAStatDimCfgn,
       "isgVGIsdnEIAStatTEI": isgVGIsdnEIAStatTEI,
       "isgVGIsdnEIAStatSPBU": isgVGIsdnEIAStatSPBU,
       "isgVGIsdnEIAStatL1State": isgVGIsdnEIAStatL1State,
       "isgVGIsdnEIAStatChanType": isgVGIsdnEIAStatChanType,
       "isgVGIsdnEIAStatAccType": isgVGIsdnEIAStatAccType,
       "cdx6500Controls": cdx6500Controls}
)
