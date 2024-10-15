# SNMP MIB module (BRIDGE-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BRIDGE-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:14 2024
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



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class BridgeId(OctetString):
    """Custom type BridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )




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
_Cdx6500PCTBridgeGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTBridgeGroup = _Cdx6500PCTBridgeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6)
)
_Cdx6500PCTPortStaticAddrTable_Object = MibTable
cdx6500PCTPortStaticAddrTable = _Cdx6500PCTPortStaticAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cdx6500PCTPortStaticAddrTable.setStatus("mandatory")
_Cdx6500PCTPortStaticAddrEntry_Object = MibTableRow
cdx6500PCTPortStaticAddrEntry = _Cdx6500PCTPortStaticAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 1, 1)
)
cdx6500PCTPortStaticAddrEntry.setIndexNames(
    (0, "BRIDGE-OPT-MIB", "cdx6500LfcmStaticAddrEntryNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PCTPortStaticAddrEntry.setStatus("mandatory")
_Cdx6500LfcmStaticAddrEntryNumber_Type = Integer32
_Cdx6500LfcmStaticAddrEntryNumber_Object = MibTableColumn
cdx6500LfcmStaticAddrEntryNumber = _Cdx6500LfcmStaticAddrEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 1, 1, 1),
    _Cdx6500LfcmStaticAddrEntryNumber_Type()
)
cdx6500LfcmStaticAddrEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmStaticAddrEntryNumber.setStatus("mandatory")
_Cdx6500LfcmStaticMacAddr_Type = MacAddress
_Cdx6500LfcmStaticMacAddr_Object = MibTableColumn
cdx6500LfcmStaticMacAddr = _Cdx6500LfcmStaticMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 1, 1, 2),
    _Cdx6500LfcmStaticMacAddr_Type()
)
cdx6500LfcmStaticMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmStaticMacAddr.setStatus("mandatory")


class _Cdx6500LfcmStaticIncSrcLinkAct_Type(DisplayString):
    """Custom type cdx6500LfcmStaticIncSrcLinkAct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 9),
    )


_Cdx6500LfcmStaticIncSrcLinkAct_Type.__name__ = "DisplayString"
_Cdx6500LfcmStaticIncSrcLinkAct_Object = MibTableColumn
cdx6500LfcmStaticIncSrcLinkAct = _Cdx6500LfcmStaticIncSrcLinkAct_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 1, 1, 3),
    _Cdx6500LfcmStaticIncSrcLinkAct_Type()
)
cdx6500LfcmStaticIncSrcLinkAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmStaticIncSrcLinkAct.setStatus("mandatory")


class _Cdx6500LfcmStaticOutSrcLinkAct_Type(DisplayString):
    """Custom type cdx6500LfcmStaticOutSrcLinkAct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 9),
    )


_Cdx6500LfcmStaticOutSrcLinkAct_Type.__name__ = "DisplayString"
_Cdx6500LfcmStaticOutSrcLinkAct_Object = MibTableColumn
cdx6500LfcmStaticOutSrcLinkAct = _Cdx6500LfcmStaticOutSrcLinkAct_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 1, 1, 4),
    _Cdx6500LfcmStaticOutSrcLinkAct_Type()
)
cdx6500LfcmStaticOutSrcLinkAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmStaticOutSrcLinkAct.setStatus("mandatory")


class _Cdx6500LfcmStaticIncDestLinkAct_Type(DisplayString):
    """Custom type cdx6500LfcmStaticIncDestLinkAct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 9),
    )


_Cdx6500LfcmStaticIncDestLinkAct_Type.__name__ = "DisplayString"
_Cdx6500LfcmStaticIncDestLinkAct_Object = MibTableColumn
cdx6500LfcmStaticIncDestLinkAct = _Cdx6500LfcmStaticIncDestLinkAct_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 1, 1, 5),
    _Cdx6500LfcmStaticIncDestLinkAct_Type()
)
cdx6500LfcmStaticIncDestLinkAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmStaticIncDestLinkAct.setStatus("mandatory")


class _Cdx6500LfcmStaticOutDestLinkAct_Type(DisplayString):
    """Custom type cdx6500LfcmStaticOutDestLinkAct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 9),
    )


_Cdx6500LfcmStaticOutDestLinkAct_Type.__name__ = "DisplayString"
_Cdx6500LfcmStaticOutDestLinkAct_Object = MibTableColumn
cdx6500LfcmStaticOutDestLinkAct = _Cdx6500LfcmStaticOutDestLinkAct_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 1, 1, 6),
    _Cdx6500LfcmStaticOutDestLinkAct_Type()
)
cdx6500LfcmStaticOutDestLinkAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmStaticOutDestLinkAct.setStatus("mandatory")
_Cdx6500LfcmStaticIncSrcList_Type = DisplayString
_Cdx6500LfcmStaticIncSrcList_Object = MibTableColumn
cdx6500LfcmStaticIncSrcList = _Cdx6500LfcmStaticIncSrcList_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 1, 1, 7),
    _Cdx6500LfcmStaticIncSrcList_Type()
)
cdx6500LfcmStaticIncSrcList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmStaticIncSrcList.setStatus("mandatory")
_Cdx6500LfcmStaticOutSrcList_Type = DisplayString
_Cdx6500LfcmStaticOutSrcList_Object = MibTableColumn
cdx6500LfcmStaticOutSrcList = _Cdx6500LfcmStaticOutSrcList_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 1, 1, 8),
    _Cdx6500LfcmStaticOutSrcList_Type()
)
cdx6500LfcmStaticOutSrcList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmStaticOutSrcList.setStatus("mandatory")
_Cdx6500LfcmStaticIncDestList_Type = DisplayString
_Cdx6500LfcmStaticIncDestList_Object = MibTableColumn
cdx6500LfcmStaticIncDestList = _Cdx6500LfcmStaticIncDestList_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 1, 1, 9),
    _Cdx6500LfcmStaticIncDestList_Type()
)
cdx6500LfcmStaticIncDestList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmStaticIncDestList.setStatus("mandatory")
_Cdx6500LfcmStaticOutDestList_Type = DisplayString
_Cdx6500LfcmStaticOutDestList_Object = MibTableColumn
cdx6500LfcmStaticOutDestList = _Cdx6500LfcmStaticOutDestList_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 1, 1, 10),
    _Cdx6500LfcmStaticOutDestList_Type()
)
cdx6500LfcmStaticOutDestList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmStaticOutDestList.setStatus("mandatory")
_Cdx6500LfcmStaticMacMask_Type = MacAddress
_Cdx6500LfcmStaticMacMask_Object = MibTableColumn
cdx6500LfcmStaticMacMask = _Cdx6500LfcmStaticMacMask_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 1, 1, 11),
    _Cdx6500LfcmStaticMacMask_Type()
)
cdx6500LfcmStaticMacMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmStaticMacMask.setStatus("mandatory")
_Cdx6500PCTPortStaticProtTable_Object = MibTable
cdx6500PCTPortStaticProtTable = _Cdx6500PCTPortStaticProtTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    cdx6500PCTPortStaticProtTable.setStatus("mandatory")
_Cdx6500PCTPortStaticProtEntry_Object = MibTableRow
cdx6500PCTPortStaticProtEntry = _Cdx6500PCTPortStaticProtEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 2, 1)
)
cdx6500PCTPortStaticProtEntry.setIndexNames(
    (0, "BRIDGE-OPT-MIB", "cdx6500LfcmStaticProtEntryNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PCTPortStaticProtEntry.setStatus("mandatory")
_Cdx6500LfcmStaticProtEntryNumber_Type = Integer32
_Cdx6500LfcmStaticProtEntryNumber_Object = MibTableColumn
cdx6500LfcmStaticProtEntryNumber = _Cdx6500LfcmStaticProtEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 2, 1, 1),
    _Cdx6500LfcmStaticProtEntryNumber_Type()
)
cdx6500LfcmStaticProtEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmStaticProtEntryNumber.setStatus("mandatory")


class _Cdx6500LfcmStaticType_Type(Integer32):
    """Custom type cdx6500LfcmStaticType based on Integer32"""
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
        *(("dsap", 0),
          ("eType", 2),
          ("newvalDsap", 50),
          ("snap", 1))
    )


_Cdx6500LfcmStaticType_Type.__name__ = "Integer32"
_Cdx6500LfcmStaticType_Object = MibTableColumn
cdx6500LfcmStaticType = _Cdx6500LfcmStaticType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 2, 1, 2),
    _Cdx6500LfcmStaticType_Type()
)
cdx6500LfcmStaticType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmStaticType.setStatus("mandatory")
_Cdx6500LfcmStaticValue_Type = DisplayString
_Cdx6500LfcmStaticValue_Object = MibTableColumn
cdx6500LfcmStaticValue = _Cdx6500LfcmStaticValue_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 2, 1, 3),
    _Cdx6500LfcmStaticValue_Type()
)
cdx6500LfcmStaticValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmStaticValue.setStatus("mandatory")


class _Cdx6500LfcmStaticIncProtLinkAct_Type(DisplayString):
    """Custom type cdx6500LfcmStaticIncProtLinkAct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 9),
    )


_Cdx6500LfcmStaticIncProtLinkAct_Type.__name__ = "DisplayString"
_Cdx6500LfcmStaticIncProtLinkAct_Object = MibTableColumn
cdx6500LfcmStaticIncProtLinkAct = _Cdx6500LfcmStaticIncProtLinkAct_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 2, 1, 4),
    _Cdx6500LfcmStaticIncProtLinkAct_Type()
)
cdx6500LfcmStaticIncProtLinkAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmStaticIncProtLinkAct.setStatus("mandatory")


class _Cdx6500LfcmStaticOutProtLinkAct_Type(DisplayString):
    """Custom type cdx6500LfcmStaticOutProtLinkAct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 9),
    )


_Cdx6500LfcmStaticOutProtLinkAct_Type.__name__ = "DisplayString"
_Cdx6500LfcmStaticOutProtLinkAct_Object = MibTableColumn
cdx6500LfcmStaticOutProtLinkAct = _Cdx6500LfcmStaticOutProtLinkAct_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 2, 1, 5),
    _Cdx6500LfcmStaticOutProtLinkAct_Type()
)
cdx6500LfcmStaticOutProtLinkAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmStaticOutProtLinkAct.setStatus("mandatory")
_Cdx6500LfcmStaticIncProtList_Type = DisplayString
_Cdx6500LfcmStaticIncProtList_Object = MibTableColumn
cdx6500LfcmStaticIncProtList = _Cdx6500LfcmStaticIncProtList_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 2, 1, 6),
    _Cdx6500LfcmStaticIncProtList_Type()
)
cdx6500LfcmStaticIncProtList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmStaticIncProtList.setStatus("mandatory")
_Cdx6500LfcmStaticOutProtList_Type = DisplayString
_Cdx6500LfcmStaticOutProtList_Object = MibTableColumn
cdx6500LfcmStaticOutProtList = _Cdx6500LfcmStaticOutProtList_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 2, 1, 7),
    _Cdx6500LfcmStaticOutProtList_Type()
)
cdx6500LfcmStaticOutProtList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmStaticOutProtList.setStatus("mandatory")
_Cdx6500LfcmStaticValue1_Type = DisplayString
_Cdx6500LfcmStaticValue1_Object = MibTableColumn
cdx6500LfcmStaticValue1 = _Cdx6500LfcmStaticValue1_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 2, 1, 8),
    _Cdx6500LfcmStaticValue1_Type()
)
cdx6500LfcmStaticValue1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmStaticValue1.setStatus("mandatory")
_Cdx6500LfcmStaticValue2_Type = DisplayString
_Cdx6500LfcmStaticValue2_Object = MibTableColumn
cdx6500LfcmStaticValue2 = _Cdx6500LfcmStaticValue2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 2, 1, 9),
    _Cdx6500LfcmStaticValue2_Type()
)
cdx6500LfcmStaticValue2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmStaticValue2.setStatus("mandatory")
_Cdx6500PCTSrLinkTable_Object = MibTable
cdx6500PCTSrLinkTable = _Cdx6500PCTSrLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 3)
)
if mibBuilder.loadTexts:
    cdx6500PCTSrLinkTable.setStatus("mandatory")
_Cdx6500PCTSrLinkEntry_Object = MibTableRow
cdx6500PCTSrLinkEntry = _Cdx6500PCTSrLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 3, 1)
)
cdx6500PCTSrLinkEntry.setIndexNames(
    (0, "BRIDGE-OPT-MIB", "cdx6500LfcmSrLink"),
)
if mibBuilder.loadTexts:
    cdx6500PCTSrLinkEntry.setStatus("mandatory")
_Cdx6500LfcmSrLink_Type = Integer32
_Cdx6500LfcmSrLink_Object = MibTableColumn
cdx6500LfcmSrLink = _Cdx6500LfcmSrLink_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 3, 1, 1),
    _Cdx6500LfcmSrLink_Type()
)
cdx6500LfcmSrLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmSrLink.setStatus("mandatory")
_Cdx6500LfcmSrLinkHopCount_Type = Integer32
_Cdx6500LfcmSrLinkHopCount_Object = MibTableColumn
cdx6500LfcmSrLinkHopCount = _Cdx6500LfcmSrLinkHopCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 3, 1, 2),
    _Cdx6500LfcmSrLinkHopCount_Type()
)
cdx6500LfcmSrLinkHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmSrLinkHopCount.setStatus("mandatory")
_Cdx6500LfcmSrLinkBridgeNum_Type = Integer32
_Cdx6500LfcmSrLinkBridgeNum_Object = MibTableColumn
cdx6500LfcmSrLinkBridgeNum = _Cdx6500LfcmSrLinkBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 3, 1, 3),
    _Cdx6500LfcmSrLinkBridgeNum_Type()
)
cdx6500LfcmSrLinkBridgeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmSrLinkBridgeNum.setStatus("mandatory")
_Cdx6500LfcmSrLinkTargetSegment_Type = Integer32
_Cdx6500LfcmSrLinkTargetSegment_Object = MibTableColumn
cdx6500LfcmSrLinkTargetSegment = _Cdx6500LfcmSrLinkTargetSegment_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 3, 1, 4),
    _Cdx6500LfcmSrLinkTargetSegment_Type()
)
cdx6500LfcmSrLinkTargetSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmSrLinkTargetSegment.setStatus("mandatory")
_Cdx6500LfcmSrLinkLargestFrame_Type = Integer32
_Cdx6500LfcmSrLinkLargestFrame_Object = MibTableColumn
cdx6500LfcmSrLinkLargestFrame = _Cdx6500LfcmSrLinkLargestFrame_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 3, 1, 5),
    _Cdx6500LfcmSrLinkLargestFrame_Type()
)
cdx6500LfcmSrLinkLargestFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmSrLinkLargestFrame.setStatus("mandatory")


class _Cdx6500LfcmSrLinkMode_Type(Integer32):
    """Custom type cdx6500LfcmSrLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("rfc1294", 2),
          ("trans", 3))
    )


_Cdx6500LfcmSrLinkMode_Type.__name__ = "Integer32"
_Cdx6500LfcmSrLinkMode_Object = MibTableColumn
cdx6500LfcmSrLinkMode = _Cdx6500LfcmSrLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 3, 1, 6),
    _Cdx6500LfcmSrLinkMode_Type()
)
cdx6500LfcmSrLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmSrLinkMode.setStatus("mandatory")
_Cdx6500LfcmSrLinkVsegNum_Type = DisplayString
_Cdx6500LfcmSrLinkVsegNum_Object = MibTableColumn
cdx6500LfcmSrLinkVsegNum = _Cdx6500LfcmSrLinkVsegNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 3, 1, 7),
    _Cdx6500LfcmSrLinkVsegNum_Type()
)
cdx6500LfcmSrLinkVsegNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmSrLinkVsegNum.setStatus("mandatory")
_Cdx6500PCTStaticLinkTable_Object = MibTable
cdx6500PCTStaticLinkTable = _Cdx6500PCTStaticLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 4)
)
if mibBuilder.loadTexts:
    cdx6500PCTStaticLinkTable.setStatus("mandatory")
_Cdx6500PCTStaticLinkEntry_Object = MibTableRow
cdx6500PCTStaticLinkEntry = _Cdx6500PCTStaticLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 4, 1)
)
cdx6500PCTStaticLinkEntry.setIndexNames(
    (0, "BRIDGE-OPT-MIB", "cdx6500LfcmLinkStaticAddress"),
    (0, "BRIDGE-OPT-MIB", "cdx6500LfcmLinkStaticReceivePort"),
)
if mibBuilder.loadTexts:
    cdx6500PCTStaticLinkEntry.setStatus("mandatory")
_Cdx6500LfcmLinkStaticAddress_Type = MacAddress
_Cdx6500LfcmLinkStaticAddress_Object = MibTableColumn
cdx6500LfcmLinkStaticAddress = _Cdx6500LfcmLinkStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 4, 1, 1),
    _Cdx6500LfcmLinkStaticAddress_Type()
)
cdx6500LfcmLinkStaticAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLinkStaticAddress.setStatus("mandatory")
_Cdx6500LfcmLinkStaticReceivePort_Type = Integer32
_Cdx6500LfcmLinkStaticReceivePort_Object = MibTableColumn
cdx6500LfcmLinkStaticReceivePort = _Cdx6500LfcmLinkStaticReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 4, 1, 2),
    _Cdx6500LfcmLinkStaticReceivePort_Type()
)
cdx6500LfcmLinkStaticReceivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLinkStaticReceivePort.setStatus("mandatory")
_Cdx6500LfcmLinkStaticAllowToGoTo_Type = OctetString
_Cdx6500LfcmLinkStaticAllowToGoTo_Object = MibTableColumn
cdx6500LfcmLinkStaticAllowToGoTo = _Cdx6500LfcmLinkStaticAllowToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 4, 1, 3),
    _Cdx6500LfcmLinkStaticAllowToGoTo_Type()
)
cdx6500LfcmLinkStaticAllowToGoTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLinkStaticAllowToGoTo.setStatus("mandatory")


class _Cdx6500LfcmLinkStaticStatus_Type(Integer32):
    """Custom type cdx6500LfcmLinkStaticStatus based on Integer32"""
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
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 5),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_Cdx6500LfcmLinkStaticStatus_Type.__name__ = "Integer32"
_Cdx6500LfcmLinkStaticStatus_Object = MibTableColumn
cdx6500LfcmLinkStaticStatus = _Cdx6500LfcmLinkStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 4, 1, 4),
    _Cdx6500LfcmLinkStaticStatus_Type()
)
cdx6500LfcmLinkStaticStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLinkStaticStatus.setStatus("mandatory")
_Cdx6500PCTLtrmStnTable_Object = MibTable
cdx6500PCTLtrmStnTable = _Cdx6500PCTLtrmStnTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 5)
)
if mibBuilder.loadTexts:
    cdx6500PCTLtrmStnTable.setStatus("mandatory")
_Cdx6500PCTLtrmStnEntry_Object = MibTableRow
cdx6500PCTLtrmStnEntry = _Cdx6500PCTLtrmStnEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 5, 1)
)
cdx6500PCTLtrmStnEntry.setIndexNames(
    (0, "BRIDGE-OPT-MIB", "cdx6500LfcmLtrmStnEntryNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PCTLtrmStnEntry.setStatus("mandatory")
_Cdx6500LfcmLtrmStnEntryNumber_Type = Integer32
_Cdx6500LfcmLtrmStnEntryNumber_Object = MibTableColumn
cdx6500LfcmLtrmStnEntryNumber = _Cdx6500LfcmLtrmStnEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 5, 1, 1),
    _Cdx6500LfcmLtrmStnEntryNumber_Type()
)
cdx6500LfcmLtrmStnEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmStnEntryNumber.setStatus("mandatory")
_Cdx6500LfcmLtrmMacAddress_Type = MacAddress
_Cdx6500LfcmLtrmMacAddress_Object = MibTableColumn
cdx6500LfcmLtrmMacAddress = _Cdx6500LfcmLtrmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 5, 1, 2),
    _Cdx6500LfcmLtrmMacAddress_Type()
)
cdx6500LfcmLtrmMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmMacAddress.setStatus("mandatory")
_Cdx6500LfcmLtrmSap_Type = Integer32
_Cdx6500LfcmLtrmSap_Object = MibTableColumn
cdx6500LfcmLtrmSap = _Cdx6500LfcmLtrmSap_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 5, 1, 3),
    _Cdx6500LfcmLtrmSap_Type()
)
cdx6500LfcmLtrmSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmSap.setStatus("mandatory")
_Cdx6500LfcmLtrmProfileName_Type = DisplayString
_Cdx6500LfcmLtrmProfileName_Object = MibTableColumn
cdx6500LfcmLtrmProfileName = _Cdx6500LfcmLtrmProfileName_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 5, 1, 4),
    _Cdx6500LfcmLtrmProfileName_Type()
)
cdx6500LfcmLtrmProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmProfileName.setStatus("mandatory")
_Cdx6500PCTLtrmProfTable_Object = MibTable
cdx6500PCTLtrmProfTable = _Cdx6500PCTLtrmProfTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 6)
)
if mibBuilder.loadTexts:
    cdx6500PCTLtrmProfTable.setStatus("mandatory")
_Cdx6500PCTLtrmProfEntry_Object = MibTableRow
cdx6500PCTLtrmProfEntry = _Cdx6500PCTLtrmProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 6, 1)
)
cdx6500PCTLtrmProfEntry.setIndexNames(
    (0, "BRIDGE-OPT-MIB", "cdx6500LfcmLtrmProfEntryNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PCTLtrmProfEntry.setStatus("mandatory")
_Cdx6500LfcmLtrmProfEntryNumber_Type = Integer32
_Cdx6500LfcmLtrmProfEntryNumber_Object = MibTableColumn
cdx6500LfcmLtrmProfEntryNumber = _Cdx6500LfcmLtrmProfEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 6, 1, 1),
    _Cdx6500LfcmLtrmProfEntryNumber_Type()
)
cdx6500LfcmLtrmProfEntryNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmProfEntryNumber.setStatus("mandatory")
_Cdx6500LfcmLtrmProfLlcName_Type = DisplayString
_Cdx6500LfcmLtrmProfLlcName_Object = MibTableColumn
cdx6500LfcmLtrmProfLlcName = _Cdx6500LfcmLtrmProfLlcName_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 6, 1, 2),
    _Cdx6500LfcmLtrmProfLlcName_Type()
)
cdx6500LfcmLtrmProfLlcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmProfLlcName.setStatus("mandatory")
_Cdx6500LfcmLtrmProfTimeout1_Type = Integer32
_Cdx6500LfcmLtrmProfTimeout1_Object = MibTableColumn
cdx6500LfcmLtrmProfTimeout1 = _Cdx6500LfcmLtrmProfTimeout1_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 6, 1, 3),
    _Cdx6500LfcmLtrmProfTimeout1_Type()
)
cdx6500LfcmLtrmProfTimeout1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmProfTimeout1.setStatus("mandatory")
_Cdx6500LfcmLtrmProfTimeout2_Type = Integer32
_Cdx6500LfcmLtrmProfTimeout2_Object = MibTableColumn
cdx6500LfcmLtrmProfTimeout2 = _Cdx6500LfcmLtrmProfTimeout2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 6, 1, 4),
    _Cdx6500LfcmLtrmProfTimeout2_Type()
)
cdx6500LfcmLtrmProfTimeout2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmProfTimeout2.setStatus("mandatory")
_Cdx6500LfcmLtrmProfTimeout3_Type = Integer32
_Cdx6500LfcmLtrmProfTimeout3_Object = MibTableColumn
cdx6500LfcmLtrmProfTimeout3 = _Cdx6500LfcmLtrmProfTimeout3_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 6, 1, 5),
    _Cdx6500LfcmLtrmProfTimeout3_Type()
)
cdx6500LfcmLtrmProfTimeout3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmProfTimeout3.setStatus("mandatory")
_Cdx6500LfcmLtrmProfN2_Type = Integer32
_Cdx6500LfcmLtrmProfN2_Object = MibTableColumn
cdx6500LfcmLtrmProfN2 = _Cdx6500LfcmLtrmProfN2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 6, 1, 6),
    _Cdx6500LfcmLtrmProfN2_Type()
)
cdx6500LfcmLtrmProfN2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmProfN2.setStatus("mandatory")
_Cdx6500LfcmLtrmProfN3_Type = Integer32
_Cdx6500LfcmLtrmProfN3_Object = MibTableColumn
cdx6500LfcmLtrmProfN3 = _Cdx6500LfcmLtrmProfN3_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 6, 1, 7),
    _Cdx6500LfcmLtrmProfN3_Type()
)
cdx6500LfcmLtrmProfN3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmProfN3.setStatus("mandatory")
_Cdx6500LfcmLtrmProfTxWindowsize_Type = Integer32
_Cdx6500LfcmLtrmProfTxWindowsize_Object = MibTableColumn
cdx6500LfcmLtrmProfTxWindowsize = _Cdx6500LfcmLtrmProfTxWindowsize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 6, 1, 8),
    _Cdx6500LfcmLtrmProfTxWindowsize_Type()
)
cdx6500LfcmLtrmProfTxWindowsize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmProfTxWindowsize.setStatus("mandatory")
_Cdx6500dot1dBridgeCfgGroup_ObjectIdentity = ObjectIdentity
cdx6500dot1dBridgeCfgGroup = _Cdx6500dot1dBridgeCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7)
)
_Cdx6500dot1dBasePortCfg_ObjectIdentity = ObjectIdentity
cdx6500dot1dBasePortCfg = _Cdx6500dot1dBasePortCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7, 1)
)
_Cdx6500LfcmBridgeLfMode_Type = Integer32
_Cdx6500LfcmBridgeLfMode_Object = MibScalar
cdx6500LfcmBridgeLfMode = _Cdx6500LfcmBridgeLfMode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7, 1, 1),
    _Cdx6500LfcmBridgeLfMode_Type()
)
cdx6500LfcmBridgeLfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmBridgeLfMode.setStatus("deprecated")


class _Cdx6500LfcmWanDataPri_Type(Integer32):
    """Custom type cdx6500LfcmWanDataPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              50)
        )
    )
    namedValues = NamedValues(
        *(("high", 4),
          ("low", 0),
          ("med", 2),
          ("newvalLow", 50))
    )


_Cdx6500LfcmWanDataPri_Type.__name__ = "Integer32"
_Cdx6500LfcmWanDataPri_Object = MibScalar
cdx6500LfcmWanDataPri = _Cdx6500LfcmWanDataPri_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7, 1, 2),
    _Cdx6500LfcmWanDataPri_Type()
)
cdx6500LfcmWanDataPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmWanDataPri.setStatus("mandatory")
_Cdx6500LfcmLearnOnlyPeriod_Type = Integer32
_Cdx6500LfcmLearnOnlyPeriod_Object = MibScalar
cdx6500LfcmLearnOnlyPeriod = _Cdx6500LfcmLearnOnlyPeriod_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7, 1, 3),
    _Cdx6500LfcmLearnOnlyPeriod_Type()
)
cdx6500LfcmLearnOnlyPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmLearnOnlyPeriod.setStatus("mandatory")
_Cdx6500LfcmLssRingNumber_Type = DisplayString
_Cdx6500LfcmLssRingNumber_Object = MibScalar
cdx6500LfcmLssRingNumber = _Cdx6500LfcmLssRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7, 1, 4),
    _Cdx6500LfcmLssRingNumber_Type()
)
cdx6500LfcmLssRingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmLssRingNumber.setStatus("mandatory")
_Cdx6500LfcmBridgedProtocols_Type = DisplayString
_Cdx6500LfcmBridgedProtocols_Object = MibScalar
cdx6500LfcmBridgedProtocols = _Cdx6500LfcmBridgedProtocols_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7, 1, 5),
    _Cdx6500LfcmBridgedProtocols_Type()
)
cdx6500LfcmBridgedProtocols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmBridgedProtocols.setStatus("mandatory")


class _Cdx6500LfcmMaxBridgeLinks_Type(Integer32):
    """Custom type cdx6500LfcmMaxBridgeLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Cdx6500LfcmMaxBridgeLinks_Type.__name__ = "Integer32"
_Cdx6500LfcmMaxBridgeLinks_Object = MibScalar
cdx6500LfcmMaxBridgeLinks = _Cdx6500LfcmMaxBridgeLinks_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7, 1, 6),
    _Cdx6500LfcmMaxBridgeLinks_Type()
)
cdx6500LfcmMaxBridgeLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmMaxBridgeLinks.setStatus("mandatory")
_Cdx6500LfcmBridgeId_Type = Integer32
_Cdx6500LfcmBridgeId_Object = MibScalar
cdx6500LfcmBridgeId = _Cdx6500LfcmBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7, 1, 7),
    _Cdx6500LfcmBridgeId_Type()
)
cdx6500LfcmBridgeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmBridgeId.setStatus("mandatory")
_Cdx6500dot1dStpPortCfg_ObjectIdentity = ObjectIdentity
cdx6500dot1dStpPortCfg = _Cdx6500dot1dStpPortCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7, 2)
)


class _Cdx6500LfcmStpControl_Type(Integer32):
    """Custom type cdx6500LfcmStpControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("man", 1),
          ("newvalAuto", 50))
    )


_Cdx6500LfcmStpControl_Type.__name__ = "Integer32"
_Cdx6500LfcmStpControl_Object = MibScalar
cdx6500LfcmStpControl = _Cdx6500LfcmStpControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7, 2, 1),
    _Cdx6500LfcmStpControl_Type()
)
cdx6500LfcmStpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmStpControl.setStatus("mandatory")
_Cdx6500LfcmStpBadHelloThreshold_Type = Integer32
_Cdx6500LfcmStpBadHelloThreshold_Object = MibScalar
cdx6500LfcmStpBadHelloThreshold = _Cdx6500LfcmStpBadHelloThreshold_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7, 2, 2),
    _Cdx6500LfcmStpBadHelloThreshold_Type()
)
cdx6500LfcmStpBadHelloThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmStpBadHelloThreshold.setStatus("mandatory")
_Cdx6500LfcmStpBadHelloTimeout_Type = Integer32
_Cdx6500LfcmStpBadHelloTimeout_Object = MibScalar
cdx6500LfcmStpBadHelloTimeout = _Cdx6500LfcmStpBadHelloTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7, 2, 3),
    _Cdx6500LfcmStpBadHelloTimeout_Type()
)
cdx6500LfcmStpBadHelloTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmStpBadHelloTimeout.setStatus("mandatory")
_Cdx6500LtrmCfg_ObjectIdentity = ObjectIdentity
cdx6500LtrmCfg = _Cdx6500LtrmCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7, 3)
)
_Cdx6500LfcmLtrmWanTimeout1_Type = Integer32
_Cdx6500LfcmLtrmWanTimeout1_Object = MibScalar
cdx6500LfcmLtrmWanTimeout1 = _Cdx6500LfcmLtrmWanTimeout1_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7, 3, 1),
    _Cdx6500LfcmLtrmWanTimeout1_Type()
)
cdx6500LfcmLtrmWanTimeout1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmWanTimeout1.setStatus("mandatory")
_Cdx6500LfcmLtrmWanTimeout2_Type = Integer32
_Cdx6500LfcmLtrmWanTimeout2_Object = MibScalar
cdx6500LfcmLtrmWanTimeout2 = _Cdx6500LfcmLtrmWanTimeout2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7, 3, 2),
    _Cdx6500LfcmLtrmWanTimeout2_Type()
)
cdx6500LfcmLtrmWanTimeout2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmWanTimeout2.setStatus("mandatory")
_Cdx6500LfcmLtrmWanTimeout3_Type = Integer32
_Cdx6500LfcmLtrmWanTimeout3_Object = MibScalar
cdx6500LfcmLtrmWanTimeout3 = _Cdx6500LfcmLtrmWanTimeout3_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7, 3, 3),
    _Cdx6500LfcmLtrmWanTimeout3_Type()
)
cdx6500LfcmLtrmWanTimeout3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmWanTimeout3.setStatus("mandatory")
_Cdx6500LfcmLtrmWanN2_Type = Integer32
_Cdx6500LfcmLtrmWanN2_Object = MibScalar
cdx6500LfcmLtrmWanN2 = _Cdx6500LfcmLtrmWanN2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7, 3, 4),
    _Cdx6500LfcmLtrmWanN2_Type()
)
cdx6500LfcmLtrmWanN2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmWanN2.setStatus("mandatory")
_Cdx6500LfcmLtrmWanN3_Type = Integer32
_Cdx6500LfcmLtrmWanN3_Object = MibScalar
cdx6500LfcmLtrmWanN3 = _Cdx6500LfcmLtrmWanN3_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7, 3, 5),
    _Cdx6500LfcmLtrmWanN3_Type()
)
cdx6500LfcmLtrmWanN3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmWanN3.setStatus("mandatory")
_Cdx6500LfcmLtrmWanTxWindowSize_Type = Integer32
_Cdx6500LfcmLtrmWanTxWindowSize_Object = MibScalar
cdx6500LfcmLtrmWanTxWindowSize = _Cdx6500LfcmLtrmWanTxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7, 3, 6),
    _Cdx6500LfcmLtrmWanTxWindowSize_Type()
)
cdx6500LfcmLtrmWanTxWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmWanTxWindowSize.setStatus("mandatory")
_Cdx6500LfcmBaseLlcLtrmDataPri_Type = Integer32
_Cdx6500LfcmBaseLlcLtrmDataPri_Object = MibScalar
cdx6500LfcmBaseLlcLtrmDataPri = _Cdx6500LfcmBaseLlcLtrmDataPri_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7, 3, 7),
    _Cdx6500LfcmBaseLlcLtrmDataPri_Type()
)
cdx6500LfcmBaseLlcLtrmDataPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmBaseLlcLtrmDataPri.setStatus("mandatory")
_Cdx6500LssCfg_ObjectIdentity = ObjectIdentity
cdx6500LssCfg = _Cdx6500LssCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7, 4)
)
_Cdx6500LfcmLssVirtualPortMacAddr_Type = MacAddress
_Cdx6500LfcmLssVirtualPortMacAddr_Object = MibScalar
cdx6500LfcmLssVirtualPortMacAddr = _Cdx6500LfcmLssVirtualPortMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7, 4, 1),
    _Cdx6500LfcmLssVirtualPortMacAddr_Type()
)
cdx6500LfcmLssVirtualPortMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmLssVirtualPortMacAddr.setStatus("mandatory")
_Cdx6500LfcmLssBridgeId_Type = Integer32
_Cdx6500LfcmLssBridgeId_Object = MibScalar
cdx6500LfcmLssBridgeId = _Cdx6500LfcmLssBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7, 4, 2),
    _Cdx6500LfcmLssBridgeId_Type()
)
cdx6500LfcmLssBridgeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmLssBridgeId.setStatus("mandatory")
_Cdx6500LfcmLssNotificationInter_Type = Integer32
_Cdx6500LfcmLssNotificationInter_Object = MibScalar
cdx6500LfcmLssNotificationInter = _Cdx6500LfcmLssNotificationInter_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7, 4, 3),
    _Cdx6500LfcmLssNotificationInter_Type()
)
cdx6500LfcmLssNotificationInter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLssNotificationInter.setStatus("mandatory")
_Cdx6500LfcmLssCalculationInter_Type = Integer32
_Cdx6500LfcmLssCalculationInter_Object = MibScalar
cdx6500LfcmLssCalculationInter = _Cdx6500LfcmLssCalculationInter_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7, 4, 4),
    _Cdx6500LfcmLssCalculationInter_Type()
)
cdx6500LfcmLssCalculationInter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLssCalculationInter.setStatus("deprecated")


class _Cdx6500LfcmLssPathTraceCtrl_Type(Integer32):
    """Custom type cdx6500LfcmLssPathTraceCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("newvalDisable", 50))
    )


_Cdx6500LfcmLssPathTraceCtrl_Type.__name__ = "Integer32"
_Cdx6500LfcmLssPathTraceCtrl_Object = MibScalar
cdx6500LfcmLssPathTraceCtrl = _Cdx6500LfcmLssPathTraceCtrl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 7, 4, 5),
    _Cdx6500LfcmLssPathTraceCtrl_Type()
)
cdx6500LfcmLssPathTraceCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmLssPathTraceCtrl.setStatus("mandatory")
_Cdx6500PCTTbPermTable_Object = MibTable
cdx6500PCTTbPermTable = _Cdx6500PCTTbPermTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 8)
)
if mibBuilder.loadTexts:
    cdx6500PCTTbPermTable.setStatus("mandatory")
_Cdx6500PCTTbPermEntry_Object = MibTableRow
cdx6500PCTTbPermEntry = _Cdx6500PCTTbPermEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 8, 1)
)
cdx6500PCTTbPermEntry.setIndexNames(
    (0, "BRIDGE-OPT-MIB", "cdx6500LfcmTbEntry"),
)
if mibBuilder.loadTexts:
    cdx6500PCTTbPermEntry.setStatus("mandatory")
_Cdx6500LfcmTbEntry_Type = Integer32
_Cdx6500LfcmTbEntry_Object = MibTableColumn
cdx6500LfcmTbEntry = _Cdx6500LfcmTbEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 8, 1, 1),
    _Cdx6500LfcmTbEntry_Type()
)
cdx6500LfcmTbEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTbEntry.setStatus("mandatory")
_Cdx6500LfcmTpPortLocalMacAddress_Type = MacAddress
_Cdx6500LfcmTpPortLocalMacAddress_Object = MibTableColumn
cdx6500LfcmTpPortLocalMacAddress = _Cdx6500LfcmTpPortLocalMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 8, 1, 2),
    _Cdx6500LfcmTpPortLocalMacAddress_Type()
)
cdx6500LfcmTpPortLocalMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmTpPortLocalMacAddress.setStatus("mandatory")
_Cdx6500LfcmTpPortBridgeLinkNums_Type = Integer32
_Cdx6500LfcmTpPortBridgeLinkNums_Object = MibTableColumn
cdx6500LfcmTpPortBridgeLinkNums = _Cdx6500LfcmTpPortBridgeLinkNums_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 8, 1, 3),
    _Cdx6500LfcmTpPortBridgeLinkNums_Type()
)
cdx6500LfcmTpPortBridgeLinkNums.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmTpPortBridgeLinkNums.setStatus("mandatory")
_Cdx6500PCTdot1dBaseLinkTable_Object = MibTable
cdx6500PCTdot1dBaseLinkTable = _Cdx6500PCTdot1dBaseLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 9)
)
if mibBuilder.loadTexts:
    cdx6500PCTdot1dBaseLinkTable.setStatus("mandatory")
_Cdx6500PCTdot1dBaseLinkEntry_Object = MibTableRow
cdx6500PCTdot1dBaseLinkEntry = _Cdx6500PCTdot1dBaseLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 9, 1)
)
cdx6500PCTdot1dBaseLinkEntry.setIndexNames(
    (0, "BRIDGE-OPT-MIB", "cdx6500LfcmBaseLinkIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PCTdot1dBaseLinkEntry.setStatus("mandatory")
_Cdx6500LfcmBaseLinkIndex_Type = Integer32
_Cdx6500LfcmBaseLinkIndex_Object = MibTableColumn
cdx6500LfcmBaseLinkIndex = _Cdx6500LfcmBaseLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 9, 1, 1),
    _Cdx6500LfcmBaseLinkIndex_Type()
)
cdx6500LfcmBaseLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmBaseLinkIndex.setStatus("mandatory")
_Cdx6500LfcmLinkType_Type = DisplayString
_Cdx6500LfcmLinkType_Object = MibTableColumn
cdx6500LfcmLinkType = _Cdx6500LfcmLinkType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 9, 1, 2),
    _Cdx6500LfcmLinkType_Type()
)
cdx6500LfcmLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmLinkType.setStatus("mandatory")


class _Cdx6500LfcmMacAddrFilterAction_Type(Integer32):
    """Custom type cdx6500LfcmMacAddrFilterAction based on Integer32"""
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
        *(("block", 1),
          ("newvalPass", 50),
          ("none", 2),
          ("pass", 0))
    )


_Cdx6500LfcmMacAddrFilterAction_Type.__name__ = "Integer32"
_Cdx6500LfcmMacAddrFilterAction_Object = MibTableColumn
cdx6500LfcmMacAddrFilterAction = _Cdx6500LfcmMacAddrFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 9, 1, 3),
    _Cdx6500LfcmMacAddrFilterAction_Type()
)
cdx6500LfcmMacAddrFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmMacAddrFilterAction.setStatus("mandatory")


class _Cdx6500LfcmProtocolFilterAction_Type(Integer32):
    """Custom type cdx6500LfcmProtocolFilterAction based on Integer32"""
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
        *(("block", 1),
          ("newvalPass", 50),
          ("none", 2),
          ("pass", 0))
    )


_Cdx6500LfcmProtocolFilterAction_Type.__name__ = "Integer32"
_Cdx6500LfcmProtocolFilterAction_Object = MibTableColumn
cdx6500LfcmProtocolFilterAction = _Cdx6500LfcmProtocolFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 9, 1, 4),
    _Cdx6500LfcmProtocolFilterAction_Type()
)
cdx6500LfcmProtocolFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmProtocolFilterAction.setStatus("mandatory")


class _Cdx6500LfcmStpLinkManState_Type(Integer32):
    """Custom type cdx6500LfcmStpLinkManState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9,
              50)
        )
    )
    namedValues = NamedValues(
        *(("block", 9),
          ("forward", 0),
          ("newvalForward", 50))
    )


_Cdx6500LfcmStpLinkManState_Type.__name__ = "Integer32"
_Cdx6500LfcmStpLinkManState_Object = MibTableColumn
cdx6500LfcmStpLinkManState = _Cdx6500LfcmStpLinkManState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 9, 1, 5),
    _Cdx6500LfcmStpLinkManState_Type()
)
cdx6500LfcmStpLinkManState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmStpLinkManState.setStatus("mandatory")


class _Cdx6500LfcmNbiosFilterAction_Type(Integer32):
    """Custom type cdx6500LfcmNbiosFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("none", 3),
          ("pass", 1))
    )


_Cdx6500LfcmNbiosFilterAction_Type.__name__ = "Integer32"
_Cdx6500LfcmNbiosFilterAction_Object = MibTableColumn
cdx6500LfcmNbiosFilterAction = _Cdx6500LfcmNbiosFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 9, 1, 6),
    _Cdx6500LfcmNbiosFilterAction_Type()
)
cdx6500LfcmNbiosFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmNbiosFilterAction.setStatus("mandatory")
_Cdx6500PCTBasePortTable_Object = MibTable
cdx6500PCTBasePortTable = _Cdx6500PCTBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 10)
)
if mibBuilder.loadTexts:
    cdx6500PCTBasePortTable.setStatus("mandatory")
_Cdx6500PCTBasePortEntry_Object = MibTableRow
cdx6500PCTBasePortEntry = _Cdx6500PCTBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 10, 1)
)
cdx6500PCTBasePortEntry.setIndexNames(
    (0, "BRIDGE-OPT-MIB", "cdx6500LfcmBasePortIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PCTBasePortEntry.setStatus("mandatory")
_Cdx6500LfcmBasePortIndex_Type = Integer32
_Cdx6500LfcmBasePortIndex_Object = MibTableColumn
cdx6500LfcmBasePortIndex = _Cdx6500LfcmBasePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 10, 1, 1),
    _Cdx6500LfcmBasePortIndex_Type()
)
cdx6500LfcmBasePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmBasePortIndex.setStatus("mandatory")


class _Cdx6500LfcmPortAddrFiltAction_Type(Integer32):
    """Custom type cdx6500LfcmPortAddrFiltAction based on Integer32"""
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
        *(("block", 1),
          ("newvalPass", 50),
          ("none", 2),
          ("pass", 0))
    )


_Cdx6500LfcmPortAddrFiltAction_Type.__name__ = "Integer32"
_Cdx6500LfcmPortAddrFiltAction_Object = MibTableColumn
cdx6500LfcmPortAddrFiltAction = _Cdx6500LfcmPortAddrFiltAction_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 10, 1, 2),
    _Cdx6500LfcmPortAddrFiltAction_Type()
)
cdx6500LfcmPortAddrFiltAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmPortAddrFiltAction.setStatus("mandatory")


class _Cdx6500LfcmPortProtFiltAction_Type(Integer32):
    """Custom type cdx6500LfcmPortProtFiltAction based on Integer32"""
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
        *(("block", 1),
          ("newvalPass", 50),
          ("none", 2),
          ("pass", 0))
    )


_Cdx6500LfcmPortProtFiltAction_Type.__name__ = "Integer32"
_Cdx6500LfcmPortProtFiltAction_Object = MibTableColumn
cdx6500LfcmPortProtFiltAction = _Cdx6500LfcmPortProtFiltAction_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 10, 1, 3),
    _Cdx6500LfcmPortProtFiltAction_Type()
)
cdx6500LfcmPortProtFiltAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmPortProtFiltAction.setStatus("mandatory")


class _Cdx6500LfcmPortStptManState_Type(Integer32):
    """Custom type cdx6500LfcmPortStptManState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9,
              50)
        )
    )
    namedValues = NamedValues(
        *(("block", 9),
          ("forward", 0),
          ("newvalForward", 50))
    )


_Cdx6500LfcmPortStptManState_Type.__name__ = "Integer32"
_Cdx6500LfcmPortStptManState_Object = MibTableColumn
cdx6500LfcmPortStptManState = _Cdx6500LfcmPortStptManState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 10, 1, 4),
    _Cdx6500LfcmPortStptManState_Type()
)
cdx6500LfcmPortStptManState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmPortStptManState.setStatus("mandatory")
_Cdx6500PCTNetBiosTable_Object = MibTable
cdx6500PCTNetBiosTable = _Cdx6500PCTNetBiosTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 11)
)
if mibBuilder.loadTexts:
    cdx6500PCTNetBiosTable.setStatus("mandatory")
_Cdx6500PCTNetBiosEntry_Object = MibTableRow
cdx6500PCTNetBiosEntry = _Cdx6500PCTNetBiosEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 11, 1)
)
cdx6500PCTNetBiosEntry.setIndexNames(
    (0, "BRIDGE-OPT-MIB", "cdx6500LfcmNetBiosIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PCTNetBiosEntry.setStatus("mandatory")
_Cdx6500LfcmNetBiosIndex_Type = Integer32
_Cdx6500LfcmNetBiosIndex_Object = MibTableColumn
cdx6500LfcmNetBiosIndex = _Cdx6500LfcmNetBiosIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 11, 1, 1),
    _Cdx6500LfcmNetBiosIndex_Type()
)
cdx6500LfcmNetBiosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmNetBiosIndex.setStatus("mandatory")


class _Cdx6500LfcmNbiosStrType_Type(Integer32):
    """Custom type cdx6500LfcmNbiosStrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii-name", 1),
          ("hex-name", 2))
    )


_Cdx6500LfcmNbiosStrType_Type.__name__ = "Integer32"
_Cdx6500LfcmNbiosStrType_Object = MibTableColumn
cdx6500LfcmNbiosStrType = _Cdx6500LfcmNbiosStrType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 11, 1, 2),
    _Cdx6500LfcmNbiosStrType_Type()
)
cdx6500LfcmNbiosStrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmNbiosStrType.setStatus("mandatory")
_Cdx6500LfcmNbiosAsciiName_Type = DisplayString
_Cdx6500LfcmNbiosAsciiName_Object = MibTableColumn
cdx6500LfcmNbiosAsciiName = _Cdx6500LfcmNbiosAsciiName_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 11, 1, 3),
    _Cdx6500LfcmNbiosAsciiName_Type()
)
cdx6500LfcmNbiosAsciiName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmNbiosAsciiName.setStatus("mandatory")
_Cdx6500LfcmNbiosHexName_Type = DisplayString
_Cdx6500LfcmNbiosHexName_Object = MibTableColumn
cdx6500LfcmNbiosHexName = _Cdx6500LfcmNbiosHexName_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 11, 1, 4),
    _Cdx6500LfcmNbiosHexName_Type()
)
cdx6500LfcmNbiosHexName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmNbiosHexName.setStatus("mandatory")
_Cdx6500LfcmNbiosIncAction_Type = DisplayString
_Cdx6500LfcmNbiosIncAction_Object = MibTableColumn
cdx6500LfcmNbiosIncAction = _Cdx6500LfcmNbiosIncAction_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 11, 1, 5),
    _Cdx6500LfcmNbiosIncAction_Type()
)
cdx6500LfcmNbiosIncAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmNbiosIncAction.setStatus("mandatory")
_Cdx6500LfcmNbiosIncList_Type = DisplayString
_Cdx6500LfcmNbiosIncList_Object = MibTableColumn
cdx6500LfcmNbiosIncList = _Cdx6500LfcmNbiosIncList_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 11, 1, 6),
    _Cdx6500LfcmNbiosIncList_Type()
)
cdx6500LfcmNbiosIncList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmNbiosIncList.setStatus("mandatory")
_Cdx6500LfcmNbiosOutAction_Type = DisplayString
_Cdx6500LfcmNbiosOutAction_Object = MibTableColumn
cdx6500LfcmNbiosOutAction = _Cdx6500LfcmNbiosOutAction_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 11, 1, 7),
    _Cdx6500LfcmNbiosOutAction_Type()
)
cdx6500LfcmNbiosOutAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmNbiosOutAction.setStatus("mandatory")
_Cdx6500LfcmNbiosOutList_Type = DisplayString
_Cdx6500LfcmNbiosOutList_Object = MibTableColumn
cdx6500LfcmNbiosOutList = _Cdx6500LfcmNbiosOutList_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6, 11, 1, 8),
    _Cdx6500LfcmNbiosOutList_Type()
)
cdx6500LfcmNbiosOutList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmNbiosOutList.setStatus("mandatory")
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500StatProtocolGroup = _Cdx6500StatProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1)
)
_Cdx6500PSTBridgeGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTBridgeGroup = _Cdx6500PSTBridgeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5)
)
_Cdx6500PSTSrPortTable_Object = MibTable
cdx6500PSTSrPortTable = _Cdx6500PSTSrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cdx6500PSTSrPortTable.setStatus("mandatory")
_Cdx6500PSTSrPortEntry_Object = MibTableRow
cdx6500PSTSrPortEntry = _Cdx6500PSTSrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 1, 1)
)
cdx6500PSTSrPortEntry.setIndexNames(
    (0, "BRIDGE-OPT-MIB", "cdx6500LfcmSrPortIfIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PSTSrPortEntry.setStatus("mandatory")
_Cdx6500LfcmSrPortIfIndex_Type = Integer32
_Cdx6500LfcmSrPortIfIndex_Object = MibTableColumn
cdx6500LfcmSrPortIfIndex = _Cdx6500LfcmSrPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 1, 1, 1),
    _Cdx6500LfcmSrPortIfIndex_Type()
)
cdx6500LfcmSrPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmSrPortIfIndex.setStatus("mandatory")
_Cdx6500LfcmSrPortFramesRx_Type = Counter32
_Cdx6500LfcmSrPortFramesRx_Object = MibTableColumn
cdx6500LfcmSrPortFramesRx = _Cdx6500LfcmSrPortFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 1, 1, 2),
    _Cdx6500LfcmSrPortFramesRx_Type()
)
cdx6500LfcmSrPortFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmSrPortFramesRx.setStatus("mandatory")
_Cdx6500LfcmSrPortFramesTx_Type = Counter32
_Cdx6500LfcmSrPortFramesTx_Object = MibTableColumn
cdx6500LfcmSrPortFramesTx = _Cdx6500LfcmSrPortFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 1, 1, 3),
    _Cdx6500LfcmSrPortFramesTx_Type()
)
cdx6500LfcmSrPortFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmSrPortFramesTx.setStatus("mandatory")
_Cdx6500LfcmSrPortRingNumber_Type = Integer32
_Cdx6500LfcmSrPortRingNumber_Object = MibTableColumn
cdx6500LfcmSrPortRingNumber = _Cdx6500LfcmSrPortRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 1, 1, 4),
    _Cdx6500LfcmSrPortRingNumber_Type()
)
cdx6500LfcmSrPortRingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmSrPortRingNumber.setStatus("deprecated")
_Cdx6500PSTTpPortTable_Object = MibTable
cdx6500PSTTpPortTable = _Cdx6500PSTTpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cdx6500PSTTpPortTable.setStatus("mandatory")
_Cdx6500PSTTpPortEntry_Object = MibTableRow
cdx6500PSTTpPortEntry = _Cdx6500PSTTpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 2, 1)
)
cdx6500PSTTpPortEntry.setIndexNames(
    (0, "BRIDGE-OPT-MIB", "cdx6500LfcmTpPortIfIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PSTTpPortEntry.setStatus("mandatory")
_Cdx6500LfcmTpPortIfIndex_Type = Integer32
_Cdx6500LfcmTpPortIfIndex_Object = MibTableColumn
cdx6500LfcmTpPortIfIndex = _Cdx6500LfcmTpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 2, 1, 1),
    _Cdx6500LfcmTpPortIfIndex_Type()
)
cdx6500LfcmTpPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpPortIfIndex.setStatus("mandatory")
_Cdx6500LfcmTpPortUnicastRx_Type = Counter32
_Cdx6500LfcmTpPortUnicastRx_Object = MibTableColumn
cdx6500LfcmTpPortUnicastRx = _Cdx6500LfcmTpPortUnicastRx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 2, 1, 2),
    _Cdx6500LfcmTpPortUnicastRx_Type()
)
cdx6500LfcmTpPortUnicastRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpPortUnicastRx.setStatus("mandatory")
_Cdx6500LfcmTpPortUnicastTx_Type = Counter32
_Cdx6500LfcmTpPortUnicastTx_Object = MibTableColumn
cdx6500LfcmTpPortUnicastTx = _Cdx6500LfcmTpPortUnicastTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 2, 1, 3),
    _Cdx6500LfcmTpPortUnicastTx_Type()
)
cdx6500LfcmTpPortUnicastTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpPortUnicastTx.setStatus("mandatory")
_Cdx6500LfcmTpPortMulticastRx_Type = Counter32
_Cdx6500LfcmTpPortMulticastRx_Object = MibTableColumn
cdx6500LfcmTpPortMulticastRx = _Cdx6500LfcmTpPortMulticastRx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 2, 1, 4),
    _Cdx6500LfcmTpPortMulticastRx_Type()
)
cdx6500LfcmTpPortMulticastRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpPortMulticastRx.setStatus("mandatory")
_Cdx6500LfcmTpPortMulticastTx_Type = Counter32
_Cdx6500LfcmTpPortMulticastTx_Object = MibTableColumn
cdx6500LfcmTpPortMulticastTx = _Cdx6500LfcmTpPortMulticastTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 2, 1, 5),
    _Cdx6500LfcmTpPortMulticastTx_Type()
)
cdx6500LfcmTpPortMulticastTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpPortMulticastTx.setStatus("mandatory")
_Cdx6500LfcmTpPortBroadcastRx_Type = Counter32
_Cdx6500LfcmTpPortBroadcastRx_Object = MibTableColumn
cdx6500LfcmTpPortBroadcastRx = _Cdx6500LfcmTpPortBroadcastRx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 2, 1, 6),
    _Cdx6500LfcmTpPortBroadcastRx_Type()
)
cdx6500LfcmTpPortBroadcastRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpPortBroadcastRx.setStatus("mandatory")
_Cdx6500LfcmTpPortBroadcastTx_Type = Counter32
_Cdx6500LfcmTpPortBroadcastTx_Object = MibTableColumn
cdx6500LfcmTpPortBroadcastTx = _Cdx6500LfcmTpPortBroadcastTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 2, 1, 7),
    _Cdx6500LfcmTpPortBroadcastTx_Type()
)
cdx6500LfcmTpPortBroadcastTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpPortBroadcastTx.setStatus("mandatory")
_Cdx6500LfcmTpPortInboundDisc_Type = Counter32
_Cdx6500LfcmTpPortInboundDisc_Object = MibTableColumn
cdx6500LfcmTpPortInboundDisc = _Cdx6500LfcmTpPortInboundDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 2, 1, 8),
    _Cdx6500LfcmTpPortInboundDisc_Type()
)
cdx6500LfcmTpPortInboundDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpPortInboundDisc.setStatus("mandatory")
_Cdx6500LfcmTpPortOutboundDisc_Type = Counter32
_Cdx6500LfcmTpPortOutboundDisc_Object = MibTableColumn
cdx6500LfcmTpPortOutboundDisc = _Cdx6500LfcmTpPortOutboundDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 2, 1, 9),
    _Cdx6500LfcmTpPortOutboundDisc_Type()
)
cdx6500LfcmTpPortOutboundDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpPortOutboundDisc.setStatus("mandatory")
_Cdx6500LfcmTpPortULPInBoundDisc_Type = Counter32
_Cdx6500LfcmTpPortULPInBoundDisc_Object = MibTableColumn
cdx6500LfcmTpPortULPInBoundDisc = _Cdx6500LfcmTpPortULPInBoundDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 2, 1, 10),
    _Cdx6500LfcmTpPortULPInBoundDisc_Type()
)
cdx6500LfcmTpPortULPInBoundDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpPortULPInBoundDisc.setStatus("mandatory")
_Cdx6500LfcmTpPortULPOutBoundDisc_Type = Counter32
_Cdx6500LfcmTpPortULPOutBoundDisc_Object = MibTableColumn
cdx6500LfcmTpPortULPOutBoundDisc = _Cdx6500LfcmTpPortULPOutBoundDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 2, 1, 11),
    _Cdx6500LfcmTpPortULPOutBoundDisc_Type()
)
cdx6500LfcmTpPortULPOutBoundDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpPortULPOutBoundDisc.setStatus("mandatory")
_Cdx6500LfcmTpPortMLPInBoundDisc_Type = Counter32
_Cdx6500LfcmTpPortMLPInBoundDisc_Object = MibTableColumn
cdx6500LfcmTpPortMLPInBoundDisc = _Cdx6500LfcmTpPortMLPInBoundDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 2, 1, 12),
    _Cdx6500LfcmTpPortMLPInBoundDisc_Type()
)
cdx6500LfcmTpPortMLPInBoundDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpPortMLPInBoundDisc.setStatus("mandatory")
_Cdx6500LfcmTpPortMLPOutBoundDisc_Type = Counter32
_Cdx6500LfcmTpPortMLPOutBoundDisc_Object = MibTableColumn
cdx6500LfcmTpPortMLPOutBoundDisc = _Cdx6500LfcmTpPortMLPOutBoundDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 2, 1, 13),
    _Cdx6500LfcmTpPortMLPOutBoundDisc_Type()
)
cdx6500LfcmTpPortMLPOutBoundDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpPortMLPOutBoundDisc.setStatus("mandatory")
_Cdx6500PSTPortFilterTable_Object = MibTable
cdx6500PSTPortFilterTable = _Cdx6500PSTPortFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 3)
)
if mibBuilder.loadTexts:
    cdx6500PSTPortFilterTable.setStatus("mandatory")
_Cdx6500PSTPortFilterEntry_Object = MibTableRow
cdx6500PSTPortFilterEntry = _Cdx6500PSTPortFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 3, 1)
)
cdx6500PSTPortFilterEntry.setIndexNames(
    (0, "BRIDGE-OPT-MIB", "cdx6500LfcmPortFilterIfIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PSTPortFilterEntry.setStatus("mandatory")
_Cdx6500LfcmPortFilterIfIndex_Type = Integer32
_Cdx6500LfcmPortFilterIfIndex_Object = MibTableColumn
cdx6500LfcmPortFilterIfIndex = _Cdx6500LfcmPortFilterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 3, 1, 1),
    _Cdx6500LfcmPortFilterIfIndex_Type()
)
cdx6500LfcmPortFilterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmPortFilterIfIndex.setStatus("mandatory")
_Cdx6500LfcmPortFilSrcAddrInDisc_Type = Counter32
_Cdx6500LfcmPortFilSrcAddrInDisc_Object = MibTableColumn
cdx6500LfcmPortFilSrcAddrInDisc = _Cdx6500LfcmPortFilSrcAddrInDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 3, 1, 2),
    _Cdx6500LfcmPortFilSrcAddrInDisc_Type()
)
cdx6500LfcmPortFilSrcAddrInDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmPortFilSrcAddrInDisc.setStatus("mandatory")
_Cdx6500LfcmPortFilSrcAddrOutDisc_Type = Counter32
_Cdx6500LfcmPortFilSrcAddrOutDisc_Object = MibTableColumn
cdx6500LfcmPortFilSrcAddrOutDisc = _Cdx6500LfcmPortFilSrcAddrOutDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 3, 1, 3),
    _Cdx6500LfcmPortFilSrcAddrOutDisc_Type()
)
cdx6500LfcmPortFilSrcAddrOutDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmPortFilSrcAddrOutDisc.setStatus("mandatory")
_Cdx6500LfcmPortFilDestAddrInDisc_Type = Counter32
_Cdx6500LfcmPortFilDestAddrInDisc_Object = MibTableColumn
cdx6500LfcmPortFilDestAddrInDisc = _Cdx6500LfcmPortFilDestAddrInDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 3, 1, 4),
    _Cdx6500LfcmPortFilDestAddrInDisc_Type()
)
cdx6500LfcmPortFilDestAddrInDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmPortFilDestAddrInDisc.setStatus("mandatory")
_Cdx6500LfcmPortFilDestAddrOutDisc_Type = Counter32
_Cdx6500LfcmPortFilDestAddrOutDisc_Object = MibTableColumn
cdx6500LfcmPortFilDestAddrOutDisc = _Cdx6500LfcmPortFilDestAddrOutDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 3, 1, 5),
    _Cdx6500LfcmPortFilDestAddrOutDisc_Type()
)
cdx6500LfcmPortFilDestAddrOutDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmPortFilDestAddrOutDisc.setStatus("mandatory")
_Cdx6500LfcmPortFilProtInDisc_Type = Counter32
_Cdx6500LfcmPortFilProtInDisc_Object = MibTableColumn
cdx6500LfcmPortFilProtInDisc = _Cdx6500LfcmPortFilProtInDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 3, 1, 6),
    _Cdx6500LfcmPortFilProtInDisc_Type()
)
cdx6500LfcmPortFilProtInDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmPortFilProtInDisc.setStatus("mandatory")
_Cdx6500LfcmPortFilProtOutDisc_Type = Counter32
_Cdx6500LfcmPortFilProtOutDisc_Object = MibTableColumn
cdx6500LfcmPortFilProtOutDisc = _Cdx6500LfcmPortFilProtOutDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 3, 1, 7),
    _Cdx6500LfcmPortFilProtOutDisc_Type()
)
cdx6500LfcmPortFilProtOutDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmPortFilProtOutDisc.setStatus("mandatory")
_Cdx6500LfcmPortFilTotalInDisc_Type = Counter32
_Cdx6500LfcmPortFilTotalInDisc_Object = MibTableColumn
cdx6500LfcmPortFilTotalInDisc = _Cdx6500LfcmPortFilTotalInDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 3, 1, 8),
    _Cdx6500LfcmPortFilTotalInDisc_Type()
)
cdx6500LfcmPortFilTotalInDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmPortFilTotalInDisc.setStatus("mandatory")
_Cdx6500LfcmPortFilTotalOutDisc_Type = Counter32
_Cdx6500LfcmPortFilTotalOutDisc_Object = MibTableColumn
cdx6500LfcmPortFilTotalOutDisc = _Cdx6500LfcmPortFilTotalOutDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 3, 1, 9),
    _Cdx6500LfcmPortFilTotalOutDisc_Type()
)
cdx6500LfcmPortFilTotalOutDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmPortFilTotalOutDisc.setStatus("mandatory")
_Cdx6500PSTBaseLinkTable_Object = MibTable
cdx6500PSTBaseLinkTable = _Cdx6500PSTBaseLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 4)
)
if mibBuilder.loadTexts:
    cdx6500PSTBaseLinkTable.setStatus("mandatory")
_Cdx6500PSTBaseLinkEntry_Object = MibTableRow
cdx6500PSTBaseLinkEntry = _Cdx6500PSTBaseLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 4, 1)
)
cdx6500PSTBaseLinkEntry.setIndexNames(
    (0, "BRIDGE-OPT-MIB", "cdx6500LfcmBaseLink"),
)
if mibBuilder.loadTexts:
    cdx6500PSTBaseLinkEntry.setStatus("mandatory")
_Cdx6500LfcmBaseLink_Type = Integer32
_Cdx6500LfcmBaseLink_Object = MibTableColumn
cdx6500LfcmBaseLink = _Cdx6500LfcmBaseLink_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 4, 1, 1),
    _Cdx6500LfcmBaseLink_Type()
)
cdx6500LfcmBaseLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmBaseLink.setStatus("mandatory")
_Cdx6500LfcmBaseLinkIfIndex_Type = Integer32
_Cdx6500LfcmBaseLinkIfIndex_Object = MibTableColumn
cdx6500LfcmBaseLinkIfIndex = _Cdx6500LfcmBaseLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 4, 1, 2),
    _Cdx6500LfcmBaseLinkIfIndex_Type()
)
cdx6500LfcmBaseLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmBaseLinkIfIndex.setStatus("mandatory")
_Cdx6500LfcmBaseLinkCircuit_Type = ObjectIdentifier
_Cdx6500LfcmBaseLinkCircuit_Object = MibTableColumn
cdx6500LfcmBaseLinkCircuit = _Cdx6500LfcmBaseLinkCircuit_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 4, 1, 3),
    _Cdx6500LfcmBaseLinkCircuit_Type()
)
cdx6500LfcmBaseLinkCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmBaseLinkCircuit.setStatus("mandatory")


class _Cdx6500LfcmBaseLinkBlStatus_Type(Integer32):
    """Custom type cdx6500LfcmBaseLinkBlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5,
              6,
              7,
              50)
        )
    )
    namedValues = NamedValues(
        *(("active", 6),
          ("configErr", 0),
          ("congested", 4),
          ("inactive", 5),
          ("newvalConfigErr", 50),
          ("swDisabled", 1),
          ("unconfig", 7),
          ("userDisabled", 3))
    )


_Cdx6500LfcmBaseLinkBlStatus_Type.__name__ = "Integer32"
_Cdx6500LfcmBaseLinkBlStatus_Object = MibTableColumn
cdx6500LfcmBaseLinkBlStatus = _Cdx6500LfcmBaseLinkBlStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 4, 1, 4),
    _Cdx6500LfcmBaseLinkBlStatus_Type()
)
cdx6500LfcmBaseLinkBlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmBaseLinkBlStatus.setStatus("mandatory")


class _Cdx6500LfcmBaseLinkClearStats_Type(Integer32):
    """Custom type cdx6500LfcmBaseLinkClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Cdx6500LfcmBaseLinkClearStats_Type.__name__ = "Integer32"
_Cdx6500LfcmBaseLinkClearStats_Object = MibTableColumn
cdx6500LfcmBaseLinkClearStats = _Cdx6500LfcmBaseLinkClearStats_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 4, 1, 5),
    _Cdx6500LfcmBaseLinkClearStats_Type()
)
cdx6500LfcmBaseLinkClearStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500LfcmBaseLinkClearStats.setStatus("mandatory")
_Cdx6500LfcmBaseLinkLastStatReset_Type = DisplayString
_Cdx6500LfcmBaseLinkLastStatReset_Object = MibTableColumn
cdx6500LfcmBaseLinkLastStatReset = _Cdx6500LfcmBaseLinkLastStatReset_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 4, 1, 6),
    _Cdx6500LfcmBaseLinkLastStatReset_Type()
)
cdx6500LfcmBaseLinkLastStatReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmBaseLinkLastStatReset.setStatus("mandatory")


class _Cdx6500LfcmLinkBridgeLinkBoot_Type(Integer32):
    """Custom type cdx6500LfcmLinkBridgeLinkBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("boot", 1)
    )


_Cdx6500LfcmLinkBridgeLinkBoot_Type.__name__ = "Integer32"
_Cdx6500LfcmLinkBridgeLinkBoot_Object = MibTableColumn
cdx6500LfcmLinkBridgeLinkBoot = _Cdx6500LfcmLinkBridgeLinkBoot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 4, 1, 7),
    _Cdx6500LfcmLinkBridgeLinkBoot_Type()
)
cdx6500LfcmLinkBridgeLinkBoot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLinkBridgeLinkBoot.setStatus("mandatory")


class _Cdx6500LfcmLinkBlEnable_Type(Integer32):
    """Custom type cdx6500LfcmLinkBlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_Cdx6500LfcmLinkBlEnable_Type.__name__ = "Integer32"
_Cdx6500LfcmLinkBlEnable_Object = MibTableColumn
cdx6500LfcmLinkBlEnable = _Cdx6500LfcmLinkBlEnable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 4, 1, 8),
    _Cdx6500LfcmLinkBlEnable_Type()
)
cdx6500LfcmLinkBlEnable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLinkBlEnable.setStatus("mandatory")


class _Cdx6500LfcmLinkBlDisable_Type(Integer32):
    """Custom type cdx6500LfcmLinkBlDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("disable", 1)
    )


_Cdx6500LfcmLinkBlDisable_Type.__name__ = "Integer32"
_Cdx6500LfcmLinkBlDisable_Object = MibTableColumn
cdx6500LfcmLinkBlDisable = _Cdx6500LfcmLinkBlDisable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 4, 1, 9),
    _Cdx6500LfcmLinkBlDisable_Type()
)
cdx6500LfcmLinkBlDisable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLinkBlDisable.setStatus("mandatory")


class _Cdx6500LfcmCtrlsLinkSetLinkProt_Type(Integer32):
    """Custom type cdx6500LfcmCtrlsLinkSetLinkProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setUcastProtection", 1)
    )


_Cdx6500LfcmCtrlsLinkSetLinkProt_Type.__name__ = "Integer32"
_Cdx6500LfcmCtrlsLinkSetLinkProt_Object = MibTableColumn
cdx6500LfcmCtrlsLinkSetLinkProt = _Cdx6500LfcmCtrlsLinkSetLinkProt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 4, 1, 10),
    _Cdx6500LfcmCtrlsLinkSetLinkProt_Type()
)
cdx6500LfcmCtrlsLinkSetLinkProt.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500LfcmCtrlsLinkSetLinkProt.setStatus("mandatory")


class _Cdx6500LfcmCtrlsLinkClrLinkProt_Type(Integer32):
    """Custom type cdx6500LfcmCtrlsLinkClrLinkProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearUcastProtection", 1)
    )


_Cdx6500LfcmCtrlsLinkClrLinkProt_Type.__name__ = "Integer32"
_Cdx6500LfcmCtrlsLinkClrLinkProt_Object = MibTableColumn
cdx6500LfcmCtrlsLinkClrLinkProt = _Cdx6500LfcmCtrlsLinkClrLinkProt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 4, 1, 11),
    _Cdx6500LfcmCtrlsLinkClrLinkProt_Type()
)
cdx6500LfcmCtrlsLinkClrLinkProt.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500LfcmCtrlsLinkClrLinkProt.setStatus("mandatory")


class _Cdx6500LfcmCtrlsLinkSetMultProt_Type(Integer32):
    """Custom type cdx6500LfcmCtrlsLinkSetMultProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setMcastProtection", 1)
    )


_Cdx6500LfcmCtrlsLinkSetMultProt_Type.__name__ = "Integer32"
_Cdx6500LfcmCtrlsLinkSetMultProt_Object = MibTableColumn
cdx6500LfcmCtrlsLinkSetMultProt = _Cdx6500LfcmCtrlsLinkSetMultProt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 4, 1, 12),
    _Cdx6500LfcmCtrlsLinkSetMultProt_Type()
)
cdx6500LfcmCtrlsLinkSetMultProt.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500LfcmCtrlsLinkSetMultProt.setStatus("mandatory")


class _Cdx6500LfcmCtrlsLinkClrMultProt_Type(Integer32):
    """Custom type cdx6500LfcmCtrlsLinkClrMultProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearMcastProtection", 1)
    )


_Cdx6500LfcmCtrlsLinkClrMultProt_Type.__name__ = "Integer32"
_Cdx6500LfcmCtrlsLinkClrMultProt_Object = MibTableColumn
cdx6500LfcmCtrlsLinkClrMultProt = _Cdx6500LfcmCtrlsLinkClrMultProt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 4, 1, 13),
    _Cdx6500LfcmCtrlsLinkClrMultProt_Type()
)
cdx6500LfcmCtrlsLinkClrMultProt.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500LfcmCtrlsLinkClrMultProt.setStatus("mandatory")
_Cdx6500PSTSrLinkTable_Object = MibTable
cdx6500PSTSrLinkTable = _Cdx6500PSTSrLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 5)
)
if mibBuilder.loadTexts:
    cdx6500PSTSrLinkTable.setStatus("mandatory")
_Cdx6500PSTSrLinkEntry_Object = MibTableRow
cdx6500PSTSrLinkEntry = _Cdx6500PSTSrLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 5, 1)
)
cdx6500PSTSrLinkEntry.setIndexNames(
    (0, "BRIDGE-OPT-MIB", "cdx6500LfcmSrLinkIfIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PSTSrLinkEntry.setStatus("mandatory")
_Cdx6500LfcmSrLinkIfIndex_Type = Integer32
_Cdx6500LfcmSrLinkIfIndex_Object = MibTableColumn
cdx6500LfcmSrLinkIfIndex = _Cdx6500LfcmSrLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 5, 1, 1),
    _Cdx6500LfcmSrLinkIfIndex_Type()
)
cdx6500LfcmSrLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmSrLinkIfIndex.setStatus("mandatory")


class _Cdx6500LfcmSrLinkSteSpanMode_Type(Integer32):
    """Custom type cdx6500LfcmSrLinkSteSpanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("deprecatedObj", 1)
    )


_Cdx6500LfcmSrLinkSteSpanMode_Type.__name__ = "Integer32"
_Cdx6500LfcmSrLinkSteSpanMode_Object = MibTableColumn
cdx6500LfcmSrLinkSteSpanMode = _Cdx6500LfcmSrLinkSteSpanMode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 5, 1, 2),
    _Cdx6500LfcmSrLinkSteSpanMode_Type()
)
cdx6500LfcmSrLinkSteSpanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmSrLinkSteSpanMode.setStatus("mandatory")
_Cdx6500LfcmSrLinkSpecInFrames_Type = Counter32
_Cdx6500LfcmSrLinkSpecInFrames_Object = MibTableColumn
cdx6500LfcmSrLinkSpecInFrames = _Cdx6500LfcmSrLinkSpecInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 5, 1, 3),
    _Cdx6500LfcmSrLinkSpecInFrames_Type()
)
cdx6500LfcmSrLinkSpecInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmSrLinkSpecInFrames.setStatus("mandatory")
_Cdx6500LfcmSrLinkSpecOutFrames_Type = Counter32
_Cdx6500LfcmSrLinkSpecOutFrames_Object = MibTableColumn
cdx6500LfcmSrLinkSpecOutFrames = _Cdx6500LfcmSrLinkSpecOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 5, 1, 4),
    _Cdx6500LfcmSrLinkSpecOutFrames_Type()
)
cdx6500LfcmSrLinkSpecOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmSrLinkSpecOutFrames.setStatus("mandatory")
_Cdx6500LfcmSrLinkApeInFrames_Type = Counter32
_Cdx6500LfcmSrLinkApeInFrames_Object = MibTableColumn
cdx6500LfcmSrLinkApeInFrames = _Cdx6500LfcmSrLinkApeInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 5, 1, 5),
    _Cdx6500LfcmSrLinkApeInFrames_Type()
)
cdx6500LfcmSrLinkApeInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmSrLinkApeInFrames.setStatus("mandatory")
_Cdx6500LfcmSrLinkApeOutFrames_Type = Counter32
_Cdx6500LfcmSrLinkApeOutFrames_Object = MibTableColumn
cdx6500LfcmSrLinkApeOutFrames = _Cdx6500LfcmSrLinkApeOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 5, 1, 6),
    _Cdx6500LfcmSrLinkApeOutFrames_Type()
)
cdx6500LfcmSrLinkApeOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmSrLinkApeOutFrames.setStatus("mandatory")
_Cdx6500LfcmSrLinkSteOutFrames_Type = Counter32
_Cdx6500LfcmSrLinkSteOutFrames_Object = MibTableColumn
cdx6500LfcmSrLinkSteOutFrames = _Cdx6500LfcmSrLinkSteOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 5, 1, 7),
    _Cdx6500LfcmSrLinkSteOutFrames_Type()
)
cdx6500LfcmSrLinkSteOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmSrLinkSteOutFrames.setStatus("mandatory")
_Cdx6500LfcmSrLinkSteinFrames_Type = Counter32
_Cdx6500LfcmSrLinkSteinFrames_Object = MibTableColumn
cdx6500LfcmSrLinkSteinFrames = _Cdx6500LfcmSrLinkSteinFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 5, 1, 8),
    _Cdx6500LfcmSrLinkSteinFrames_Type()
)
cdx6500LfcmSrLinkSteinFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmSrLinkSteinFrames.setStatus("mandatory")
_Cdx6500LfcmSrLinkSegMisDisc_Type = Counter32
_Cdx6500LfcmSrLinkSegMisDisc_Object = MibTableColumn
cdx6500LfcmSrLinkSegMisDisc = _Cdx6500LfcmSrLinkSegMisDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 5, 1, 9),
    _Cdx6500LfcmSrLinkSegMisDisc_Type()
)
cdx6500LfcmSrLinkSegMisDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmSrLinkSegMisDisc.setStatus("mandatory")
_Cdx6500LfcmSrLinkDupSegDisc_Type = Counter32
_Cdx6500LfcmSrLinkDupSegDisc_Object = MibTableColumn
cdx6500LfcmSrLinkDupSegDisc = _Cdx6500LfcmSrLinkDupSegDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 5, 1, 10),
    _Cdx6500LfcmSrLinkDupSegDisc_Type()
)
cdx6500LfcmSrLinkDupSegDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmSrLinkDupSegDisc.setStatus("mandatory")
_Cdx6500LfcmSrLinkHopCountExcDisc_Type = Counter32
_Cdx6500LfcmSrLinkHopCountExcDisc_Object = MibTableColumn
cdx6500LfcmSrLinkHopCountExcDisc = _Cdx6500LfcmSrLinkHopCountExcDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 5, 1, 11),
    _Cdx6500LfcmSrLinkHopCountExcDisc_Type()
)
cdx6500LfcmSrLinkHopCountExcDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmSrLinkHopCountExcDisc.setStatus("mandatory")
_Cdx6500LfcmSrLinkTotalFramesRx_Type = Counter32
_Cdx6500LfcmSrLinkTotalFramesRx_Object = MibTableColumn
cdx6500LfcmSrLinkTotalFramesRx = _Cdx6500LfcmSrLinkTotalFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 5, 1, 12),
    _Cdx6500LfcmSrLinkTotalFramesRx_Type()
)
cdx6500LfcmSrLinkTotalFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmSrLinkTotalFramesRx.setStatus("mandatory")
_Cdx6500LfcmSrLinkTotalFramesTx_Type = Counter32
_Cdx6500LfcmSrLinkTotalFramesTx_Object = MibTableColumn
cdx6500LfcmSrLinkTotalFramesTx = _Cdx6500LfcmSrLinkTotalFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 5, 1, 13),
    _Cdx6500LfcmSrLinkTotalFramesTx_Type()
)
cdx6500LfcmSrLinkTotalFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmSrLinkTotalFramesTx.setStatus("mandatory")
_Cdx6500LfcmSrLinkNextRingNumber_Type = Integer32
_Cdx6500LfcmSrLinkNextRingNumber_Object = MibTableColumn
cdx6500LfcmSrLinkNextRingNumber = _Cdx6500LfcmSrLinkNextRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 5, 1, 14),
    _Cdx6500LfcmSrLinkNextRingNumber_Type()
)
cdx6500LfcmSrLinkNextRingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmSrLinkNextRingNumber.setStatus("mandatory")
_Cdx6500PSTTpLinkTable_Object = MibTable
cdx6500PSTTpLinkTable = _Cdx6500PSTTpLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 6)
)
if mibBuilder.loadTexts:
    cdx6500PSTTpLinkTable.setStatus("mandatory")
_Cdx6500PSTTpLinkEntry_Object = MibTableRow
cdx6500PSTTpLinkEntry = _Cdx6500PSTTpLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 6, 1)
)
cdx6500PSTTpLinkEntry.setIndexNames(
    (0, "BRIDGE-OPT-MIB", "cdx6500LfcmTpLink"),
)
if mibBuilder.loadTexts:
    cdx6500PSTTpLinkEntry.setStatus("mandatory")
_Cdx6500LfcmTpLink_Type = Integer32
_Cdx6500LfcmTpLink_Object = MibTableColumn
cdx6500LfcmTpLink = _Cdx6500LfcmTpLink_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 6, 1, 1),
    _Cdx6500LfcmTpLink_Type()
)
cdx6500LfcmTpLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpLink.setStatus("mandatory")
_Cdx6500LfcmTpLinkMaxInfo_Type = Integer32
_Cdx6500LfcmTpLinkMaxInfo_Object = MibTableColumn
cdx6500LfcmTpLinkMaxInfo = _Cdx6500LfcmTpLinkMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 6, 1, 2),
    _Cdx6500LfcmTpLinkMaxInfo_Type()
)
cdx6500LfcmTpLinkMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpLinkMaxInfo.setStatus("mandatory")
_Cdx6500LfcmTpLinkInFrames_Type = Counter32
_Cdx6500LfcmTpLinkInFrames_Object = MibTableColumn
cdx6500LfcmTpLinkInFrames = _Cdx6500LfcmTpLinkInFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 6, 1, 3),
    _Cdx6500LfcmTpLinkInFrames_Type()
)
cdx6500LfcmTpLinkInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpLinkInFrames.setStatus("mandatory")
_Cdx6500LfcmTpLinkOutFrames_Type = Counter32
_Cdx6500LfcmTpLinkOutFrames_Object = MibTableColumn
cdx6500LfcmTpLinkOutFrames = _Cdx6500LfcmTpLinkOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 6, 1, 4),
    _Cdx6500LfcmTpLinkOutFrames_Type()
)
cdx6500LfcmTpLinkOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpLinkOutFrames.setStatus("mandatory")
_Cdx6500LfcmTpLinkInDiscards_Type = Counter32
_Cdx6500LfcmTpLinkInDiscards_Object = MibTableColumn
cdx6500LfcmTpLinkInDiscards = _Cdx6500LfcmTpLinkInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 6, 1, 5),
    _Cdx6500LfcmTpLinkInDiscards_Type()
)
cdx6500LfcmTpLinkInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpLinkInDiscards.setStatus("mandatory")
_Cdx6500LfcmTpLinkUnicastRx_Type = Counter32
_Cdx6500LfcmTpLinkUnicastRx_Object = MibTableColumn
cdx6500LfcmTpLinkUnicastRx = _Cdx6500LfcmTpLinkUnicastRx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 6, 1, 6),
    _Cdx6500LfcmTpLinkUnicastRx_Type()
)
cdx6500LfcmTpLinkUnicastRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpLinkUnicastRx.setStatus("mandatory")
_Cdx6500LfcmTpLinkUnicastTx_Type = Counter32
_Cdx6500LfcmTpLinkUnicastTx_Object = MibTableColumn
cdx6500LfcmTpLinkUnicastTx = _Cdx6500LfcmTpLinkUnicastTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 6, 1, 7),
    _Cdx6500LfcmTpLinkUnicastTx_Type()
)
cdx6500LfcmTpLinkUnicastTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpLinkUnicastTx.setStatus("mandatory")
_Cdx6500LfcmTpLinkMulticastRx_Type = Counter32
_Cdx6500LfcmTpLinkMulticastRx_Object = MibTableColumn
cdx6500LfcmTpLinkMulticastRx = _Cdx6500LfcmTpLinkMulticastRx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 6, 1, 8),
    _Cdx6500LfcmTpLinkMulticastRx_Type()
)
cdx6500LfcmTpLinkMulticastRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpLinkMulticastRx.setStatus("mandatory")
_Cdx6500LfcmTpLinkMulticastTx_Type = Counter32
_Cdx6500LfcmTpLinkMulticastTx_Object = MibTableColumn
cdx6500LfcmTpLinkMulticastTx = _Cdx6500LfcmTpLinkMulticastTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 6, 1, 9),
    _Cdx6500LfcmTpLinkMulticastTx_Type()
)
cdx6500LfcmTpLinkMulticastTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpLinkMulticastTx.setStatus("mandatory")
_Cdx6500LfcmTpLinkBroadcastRx_Type = Counter32
_Cdx6500LfcmTpLinkBroadcastRx_Object = MibTableColumn
cdx6500LfcmTpLinkBroadcastRx = _Cdx6500LfcmTpLinkBroadcastRx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 6, 1, 10),
    _Cdx6500LfcmTpLinkBroadcastRx_Type()
)
cdx6500LfcmTpLinkBroadcastRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpLinkBroadcastRx.setStatus("mandatory")
_Cdx6500LfcmTpLinkBroadcastTx_Type = Counter32
_Cdx6500LfcmTpLinkBroadcastTx_Object = MibTableColumn
cdx6500LfcmTpLinkBroadcastTx = _Cdx6500LfcmTpLinkBroadcastTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 6, 1, 11),
    _Cdx6500LfcmTpLinkBroadcastTx_Type()
)
cdx6500LfcmTpLinkBroadcastTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpLinkBroadcastTx.setStatus("mandatory")
_Cdx6500LfcmTpLinkInBoundDisc_Type = Counter32
_Cdx6500LfcmTpLinkInBoundDisc_Object = MibTableColumn
cdx6500LfcmTpLinkInBoundDisc = _Cdx6500LfcmTpLinkInBoundDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 6, 1, 12),
    _Cdx6500LfcmTpLinkInBoundDisc_Type()
)
cdx6500LfcmTpLinkInBoundDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpLinkInBoundDisc.setStatus("mandatory")
_Cdx6500LfcmTpLinkOutBoundDisc_Type = Counter32
_Cdx6500LfcmTpLinkOutBoundDisc_Object = MibTableColumn
cdx6500LfcmTpLinkOutBoundDisc = _Cdx6500LfcmTpLinkOutBoundDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 6, 1, 13),
    _Cdx6500LfcmTpLinkOutBoundDisc_Type()
)
cdx6500LfcmTpLinkOutBoundDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpLinkOutBoundDisc.setStatus("mandatory")
_Cdx6500LfcmTpLinkULPInBoundDisc_Type = Counter32
_Cdx6500LfcmTpLinkULPInBoundDisc_Object = MibTableColumn
cdx6500LfcmTpLinkULPInBoundDisc = _Cdx6500LfcmTpLinkULPInBoundDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 6, 1, 14),
    _Cdx6500LfcmTpLinkULPInBoundDisc_Type()
)
cdx6500LfcmTpLinkULPInBoundDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpLinkULPInBoundDisc.setStatus("mandatory")
_Cdx6500LfcmTpLinkULPOutBoundDisc_Type = Counter32
_Cdx6500LfcmTpLinkULPOutBoundDisc_Object = MibTableColumn
cdx6500LfcmTpLinkULPOutBoundDisc = _Cdx6500LfcmTpLinkULPOutBoundDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 6, 1, 15),
    _Cdx6500LfcmTpLinkULPOutBoundDisc_Type()
)
cdx6500LfcmTpLinkULPOutBoundDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpLinkULPOutBoundDisc.setStatus("mandatory")
_Cdx6500LfcmTpLinkMLPInBoundDisc_Type = Counter32
_Cdx6500LfcmTpLinkMLPInBoundDisc_Object = MibTableColumn
cdx6500LfcmTpLinkMLPInBoundDisc = _Cdx6500LfcmTpLinkMLPInBoundDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 6, 1, 16),
    _Cdx6500LfcmTpLinkMLPInBoundDisc_Type()
)
cdx6500LfcmTpLinkMLPInBoundDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpLinkMLPInBoundDisc.setStatus("mandatory")
_Cdx6500LfcmTpLinkMLPOutBoundDisc_Type = Counter32
_Cdx6500LfcmTpLinkMLPOutBoundDisc_Object = MibTableColumn
cdx6500LfcmTpLinkMLPOutBoundDisc = _Cdx6500LfcmTpLinkMLPOutBoundDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 6, 1, 17),
    _Cdx6500LfcmTpLinkMLPOutBoundDisc_Type()
)
cdx6500LfcmTpLinkMLPOutBoundDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpLinkMLPOutBoundDisc.setStatus("mandatory")
_Cdx6500PSTStpLinkTable_Object = MibTable
cdx6500PSTStpLinkTable = _Cdx6500PSTStpLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 7)
)
if mibBuilder.loadTexts:
    cdx6500PSTStpLinkTable.setStatus("mandatory")
_Cdx6500PSTStpLinkEntry_Object = MibTableRow
cdx6500PSTStpLinkEntry = _Cdx6500PSTStpLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 7, 1)
)
cdx6500PSTStpLinkEntry.setIndexNames(
    (0, "BRIDGE-OPT-MIB", "cdx6500LfcmStpLink"),
)
if mibBuilder.loadTexts:
    cdx6500PSTStpLinkEntry.setStatus("mandatory")
_Cdx6500LfcmStpLink_Type = Integer32
_Cdx6500LfcmStpLink_Object = MibTableColumn
cdx6500LfcmStpLink = _Cdx6500LfcmStpLink_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 7, 1, 1),
    _Cdx6500LfcmStpLink_Type()
)
cdx6500LfcmStpLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmStpLink.setStatus("mandatory")
_Cdx6500LfcmStpPriority_Type = Integer32
_Cdx6500LfcmStpPriority_Object = MibTableColumn
cdx6500LfcmStpPriority = _Cdx6500LfcmStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 7, 1, 2),
    _Cdx6500LfcmStpPriority_Type()
)
cdx6500LfcmStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmStpPriority.setStatus("mandatory")


class _Cdx6500LfcmStpState_Type(Integer32):
    """Custom type cdx6500LfcmStpState based on Integer32"""
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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_Cdx6500LfcmStpState_Type.__name__ = "Integer32"
_Cdx6500LfcmStpState_Object = MibTableColumn
cdx6500LfcmStpState = _Cdx6500LfcmStpState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 7, 1, 3),
    _Cdx6500LfcmStpState_Type()
)
cdx6500LfcmStpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmStpState.setStatus("mandatory")


class _Cdx6500LfcmStpEnable_Type(Integer32):
    """Custom type cdx6500LfcmStpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cdx6500LfcmStpEnable_Type.__name__ = "Integer32"
_Cdx6500LfcmStpEnable_Object = MibTableColumn
cdx6500LfcmStpEnable = _Cdx6500LfcmStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 7, 1, 4),
    _Cdx6500LfcmStpEnable_Type()
)
cdx6500LfcmStpEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmStpEnable.setStatus("mandatory")
_Cdx6500LfcmStpPathCost_Type = Integer32
_Cdx6500LfcmStpPathCost_Object = MibTableColumn
cdx6500LfcmStpPathCost = _Cdx6500LfcmStpPathCost_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 7, 1, 5),
    _Cdx6500LfcmStpPathCost_Type()
)
cdx6500LfcmStpPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500LfcmStpPathCost.setStatus("mandatory")
_Cdx6500LfcmStpDesignatedRoot_Type = BridgeId
_Cdx6500LfcmStpDesignatedRoot_Object = MibTableColumn
cdx6500LfcmStpDesignatedRoot = _Cdx6500LfcmStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 7, 1, 6),
    _Cdx6500LfcmStpDesignatedRoot_Type()
)
cdx6500LfcmStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmStpDesignatedRoot.setStatus("mandatory")
_Cdx6500LfcmStpDesignatedCost_Type = Integer32
_Cdx6500LfcmStpDesignatedCost_Object = MibTableColumn
cdx6500LfcmStpDesignatedCost = _Cdx6500LfcmStpDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 7, 1, 7),
    _Cdx6500LfcmStpDesignatedCost_Type()
)
cdx6500LfcmStpDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmStpDesignatedCost.setStatus("mandatory")
_Cdx6500LfcmStpDesignatedBridge_Type = BridgeId
_Cdx6500LfcmStpDesignatedBridge_Object = MibTableColumn
cdx6500LfcmStpDesignatedBridge = _Cdx6500LfcmStpDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 7, 1, 8),
    _Cdx6500LfcmStpDesignatedBridge_Type()
)
cdx6500LfcmStpDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmStpDesignatedBridge.setStatus("mandatory")
_Cdx6500LfcmStpDesignatedPort_Type = OctetString
_Cdx6500LfcmStpDesignatedPort_Object = MibTableColumn
cdx6500LfcmStpDesignatedPort = _Cdx6500LfcmStpDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 7, 1, 9),
    _Cdx6500LfcmStpDesignatedPort_Type()
)
cdx6500LfcmStpDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmStpDesignatedPort.setStatus("mandatory")
_Cdx6500LfcmStpForwardTransitions_Type = Counter32
_Cdx6500LfcmStpForwardTransitions_Object = MibTableColumn
cdx6500LfcmStpForwardTransitions = _Cdx6500LfcmStpForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 7, 1, 10),
    _Cdx6500LfcmStpForwardTransitions_Type()
)
cdx6500LfcmStpForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmStpForwardTransitions.setStatus("mandatory")
_Cdx6500PSTStaticStatsLinkTable_Object = MibTable
cdx6500PSTStaticStatsLinkTable = _Cdx6500PSTStaticStatsLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 8)
)
if mibBuilder.loadTexts:
    cdx6500PSTStaticStatsLinkTable.setStatus("mandatory")
_Cdx6500PSTStaticsStatsLinkEntry_Object = MibTableRow
cdx6500PSTStaticsStatsLinkEntry = _Cdx6500PSTStaticsStatsLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 8, 1)
)
cdx6500PSTStaticsStatsLinkEntry.setIndexNames(
    (0, "BRIDGE-OPT-MIB", "cdx6500LfcmLinkFilterIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PSTStaticsStatsLinkEntry.setStatus("mandatory")
_Cdx6500LfcmLinkFilterIndex_Type = Integer32
_Cdx6500LfcmLinkFilterIndex_Object = MibTableColumn
cdx6500LfcmLinkFilterIndex = _Cdx6500LfcmLinkFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 8, 1, 1),
    _Cdx6500LfcmLinkFilterIndex_Type()
)
cdx6500LfcmLinkFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLinkFilterIndex.setStatus("mandatory")
_Cdx6500LfcmLinkFilSrcAddrInDisc_Type = Counter32
_Cdx6500LfcmLinkFilSrcAddrInDisc_Object = MibTableColumn
cdx6500LfcmLinkFilSrcAddrInDisc = _Cdx6500LfcmLinkFilSrcAddrInDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 8, 1, 2),
    _Cdx6500LfcmLinkFilSrcAddrInDisc_Type()
)
cdx6500LfcmLinkFilSrcAddrInDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLinkFilSrcAddrInDisc.setStatus("mandatory")
_Cdx6500LfcmLinkFilSrcAddrOutDisc_Type = Counter32
_Cdx6500LfcmLinkFilSrcAddrOutDisc_Object = MibTableColumn
cdx6500LfcmLinkFilSrcAddrOutDisc = _Cdx6500LfcmLinkFilSrcAddrOutDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 8, 1, 3),
    _Cdx6500LfcmLinkFilSrcAddrOutDisc_Type()
)
cdx6500LfcmLinkFilSrcAddrOutDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLinkFilSrcAddrOutDisc.setStatus("mandatory")
_Cdx6500LfcmLinkFilDestAddrInDisc_Type = Counter32
_Cdx6500LfcmLinkFilDestAddrInDisc_Object = MibTableColumn
cdx6500LfcmLinkFilDestAddrInDisc = _Cdx6500LfcmLinkFilDestAddrInDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 8, 1, 4),
    _Cdx6500LfcmLinkFilDestAddrInDisc_Type()
)
cdx6500LfcmLinkFilDestAddrInDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLinkFilDestAddrInDisc.setStatus("mandatory")
_Cdx6500LfcmLinkFilDestAddrOutDisc_Type = Counter32
_Cdx6500LfcmLinkFilDestAddrOutDisc_Object = MibTableColumn
cdx6500LfcmLinkFilDestAddrOutDisc = _Cdx6500LfcmLinkFilDestAddrOutDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 8, 1, 5),
    _Cdx6500LfcmLinkFilDestAddrOutDisc_Type()
)
cdx6500LfcmLinkFilDestAddrOutDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLinkFilDestAddrOutDisc.setStatus("mandatory")
_Cdx6500LfcmLinkFilProtInDisc_Type = Counter32
_Cdx6500LfcmLinkFilProtInDisc_Object = MibScalar
cdx6500LfcmLinkFilProtInDisc = _Cdx6500LfcmLinkFilProtInDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 8, 1, 6),
    _Cdx6500LfcmLinkFilProtInDisc_Type()
)
cdx6500LfcmLinkFilProtInDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLinkFilProtInDisc.setStatus("mandatory")
_Cdx6500LfcmLinkFilProtOutDisc_Type = Counter32
_Cdx6500LfcmLinkFilProtOutDisc_Object = MibTableColumn
cdx6500LfcmLinkFilProtOutDisc = _Cdx6500LfcmLinkFilProtOutDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 8, 1, 7),
    _Cdx6500LfcmLinkFilProtOutDisc_Type()
)
cdx6500LfcmLinkFilProtOutDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLinkFilProtOutDisc.setStatus("mandatory")
_Cdx6500LfcmLinkFilTotalInDisc_Type = Counter32
_Cdx6500LfcmLinkFilTotalInDisc_Object = MibTableColumn
cdx6500LfcmLinkFilTotalInDisc = _Cdx6500LfcmLinkFilTotalInDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 8, 1, 8),
    _Cdx6500LfcmLinkFilTotalInDisc_Type()
)
cdx6500LfcmLinkFilTotalInDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLinkFilTotalInDisc.setStatus("mandatory")
_Cdx6500LfcmLinkFilTotalOutDisc_Type = Counter32
_Cdx6500LfcmLinkFilTotalOutDisc_Object = MibTableColumn
cdx6500LfcmLinkFilTotalOutDisc = _Cdx6500LfcmLinkFilTotalOutDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 8, 1, 9),
    _Cdx6500LfcmLinkFilTotalOutDisc_Type()
)
cdx6500LfcmLinkFilTotalOutDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLinkFilTotalOutDisc.setStatus("mandatory")
_Cdx6500PSTLtrmStatsTable_Object = MibTable
cdx6500PSTLtrmStatsTable = _Cdx6500PSTLtrmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 9)
)
if mibBuilder.loadTexts:
    cdx6500PSTLtrmStatsTable.setStatus("mandatory")
_Cdx6500PSTLtrmStatsEntry_Object = MibTableRow
cdx6500PSTLtrmStatsEntry = _Cdx6500PSTLtrmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 9, 1)
)
cdx6500PSTLtrmStatsEntry.setIndexNames(
    (0, "BRIDGE-OPT-MIB", "cdx6500LfcmLtrmStatsIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PSTLtrmStatsEntry.setStatus("mandatory")


class _Cdx6500LfcmLtrmStatsIndex_Type(Integer32):
    """Custom type cdx6500LfcmLtrmStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Cdx6500LfcmLtrmStatsIndex_Type.__name__ = "Integer32"
_Cdx6500LfcmLtrmStatsIndex_Object = MibTableColumn
cdx6500LfcmLtrmStatsIndex = _Cdx6500LfcmLtrmStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 9, 1, 1),
    _Cdx6500LfcmLtrmStatsIndex_Type()
)
cdx6500LfcmLtrmStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmStatsIndex.setStatus("mandatory")
_Cdx6500LfcmLtrmStatsDataCharIn_Type = Counter32
_Cdx6500LfcmLtrmStatsDataCharIn_Object = MibTableColumn
cdx6500LfcmLtrmStatsDataCharIn = _Cdx6500LfcmLtrmStatsDataCharIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 9, 1, 2),
    _Cdx6500LfcmLtrmStatsDataCharIn_Type()
)
cdx6500LfcmLtrmStatsDataCharIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmStatsDataCharIn.setStatus("mandatory")
_Cdx6500LfcmLtrmStatsDataCharOut_Type = Counter32
_Cdx6500LfcmLtrmStatsDataCharOut_Object = MibTableColumn
cdx6500LfcmLtrmStatsDataCharOut = _Cdx6500LfcmLtrmStatsDataCharOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 9, 1, 3),
    _Cdx6500LfcmLtrmStatsDataCharOut_Type()
)
cdx6500LfcmLtrmStatsDataCharOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmStatsDataCharOut.setStatus("mandatory")
_Cdx6500LfcmLtrmStatsDataFrIn_Type = Counter32
_Cdx6500LfcmLtrmStatsDataFrIn_Object = MibTableColumn
cdx6500LfcmLtrmStatsDataFrIn = _Cdx6500LfcmLtrmStatsDataFrIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 9, 1, 4),
    _Cdx6500LfcmLtrmStatsDataFrIn_Type()
)
cdx6500LfcmLtrmStatsDataFrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmStatsDataFrIn.setStatus("mandatory")
_Cdx6500LfcmLtrmStatsDataFrOut_Type = Counter32
_Cdx6500LfcmLtrmStatsDataFrOut_Object = MibTableColumn
cdx6500LfcmLtrmStatsDataFrOut = _Cdx6500LfcmLtrmStatsDataFrOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 9, 1, 5),
    _Cdx6500LfcmLtrmStatsDataFrOut_Type()
)
cdx6500LfcmLtrmStatsDataFrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmStatsDataFrOut.setStatus("mandatory")
_Cdx6500LfcmLtrmStatsCtFrRrIn_Type = Counter32
_Cdx6500LfcmLtrmStatsCtFrRrIn_Object = MibTableColumn
cdx6500LfcmLtrmStatsCtFrRrIn = _Cdx6500LfcmLtrmStatsCtFrRrIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 9, 1, 6),
    _Cdx6500LfcmLtrmStatsCtFrRrIn_Type()
)
cdx6500LfcmLtrmStatsCtFrRrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmStatsCtFrRrIn.setStatus("mandatory")
_Cdx6500LfcmLtrmStatsCtFrRrOut_Type = Counter32
_Cdx6500LfcmLtrmStatsCtFrRrOut_Object = MibTableColumn
cdx6500LfcmLtrmStatsCtFrRrOut = _Cdx6500LfcmLtrmStatsCtFrRrOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 9, 1, 7),
    _Cdx6500LfcmLtrmStatsCtFrRrOut_Type()
)
cdx6500LfcmLtrmStatsCtFrRrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmStatsCtFrRrOut.setStatus("mandatory")
_Cdx6500LfcmLtrmStatsCtFrRnrIn_Type = Counter32
_Cdx6500LfcmLtrmStatsCtFrRnrIn_Object = MibTableColumn
cdx6500LfcmLtrmStatsCtFrRnrIn = _Cdx6500LfcmLtrmStatsCtFrRnrIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 9, 1, 8),
    _Cdx6500LfcmLtrmStatsCtFrRnrIn_Type()
)
cdx6500LfcmLtrmStatsCtFrRnrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmStatsCtFrRnrIn.setStatus("mandatory")
_Cdx6500LfcmLtrmStatsCtFrRnrOut_Type = Counter32
_Cdx6500LfcmLtrmStatsCtFrRnrOut_Object = MibTableColumn
cdx6500LfcmLtrmStatsCtFrRnrOut = _Cdx6500LfcmLtrmStatsCtFrRnrOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 9, 1, 9),
    _Cdx6500LfcmLtrmStatsCtFrRnrOut_Type()
)
cdx6500LfcmLtrmStatsCtFrRnrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmStatsCtFrRnrOut.setStatus("mandatory")
_Cdx6500LfcmLtrmStatsCtFrXidIn_Type = Counter32
_Cdx6500LfcmLtrmStatsCtFrXidIn_Object = MibTableColumn
cdx6500LfcmLtrmStatsCtFrXidIn = _Cdx6500LfcmLtrmStatsCtFrXidIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 9, 1, 10),
    _Cdx6500LfcmLtrmStatsCtFrXidIn_Type()
)
cdx6500LfcmLtrmStatsCtFrXidIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmStatsCtFrXidIn.setStatus("mandatory")
_Cdx6500LfcmLtrmStatsCtFrXidOut_Type = Counter32
_Cdx6500LfcmLtrmStatsCtFrXidOut_Object = MibTableColumn
cdx6500LfcmLtrmStatsCtFrXidOut = _Cdx6500LfcmLtrmStatsCtFrXidOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 9, 1, 11),
    _Cdx6500LfcmLtrmStatsCtFrXidOut_Type()
)
cdx6500LfcmLtrmStatsCtFrXidOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmStatsCtFrXidOut.setStatus("mandatory")
_Cdx6500LfcmLtrmStatsCtFrRejIn_Type = Counter32
_Cdx6500LfcmLtrmStatsCtFrRejIn_Object = MibTableColumn
cdx6500LfcmLtrmStatsCtFrRejIn = _Cdx6500LfcmLtrmStatsCtFrRejIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 9, 1, 12),
    _Cdx6500LfcmLtrmStatsCtFrRejIn_Type()
)
cdx6500LfcmLtrmStatsCtFrRejIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmStatsCtFrRejIn.setStatus("mandatory")
_Cdx6500LfcmLtrmStatsCtFrRejOut_Type = Counter32
_Cdx6500LfcmLtrmStatsCtFrRejOut_Object = MibTableColumn
cdx6500LfcmLtrmStatsCtFrRejOut = _Cdx6500LfcmLtrmStatsCtFrRejOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 9, 1, 13),
    _Cdx6500LfcmLtrmStatsCtFrRejOut_Type()
)
cdx6500LfcmLtrmStatsCtFrRejOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmStatsCtFrRejOut.setStatus("mandatory")
_Cdx6500LfcmLtrmStatsCtFrSabmeIn_Type = Counter32
_Cdx6500LfcmLtrmStatsCtFrSabmeIn_Object = MibTableColumn
cdx6500LfcmLtrmStatsCtFrSabmeIn = _Cdx6500LfcmLtrmStatsCtFrSabmeIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 9, 1, 14),
    _Cdx6500LfcmLtrmStatsCtFrSabmeIn_Type()
)
cdx6500LfcmLtrmStatsCtFrSabmeIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmStatsCtFrSabmeIn.setStatus("mandatory")
_Cdx6500LfcmLtrmStatsCtFrSabmeOut_Type = Counter32
_Cdx6500LfcmLtrmStatsCtFrSabmeOut_Object = MibTableColumn
cdx6500LfcmLtrmStatsCtFrSabmeOut = _Cdx6500LfcmLtrmStatsCtFrSabmeOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 9, 1, 15),
    _Cdx6500LfcmLtrmStatsCtFrSabmeOut_Type()
)
cdx6500LfcmLtrmStatsCtFrSabmeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmStatsCtFrSabmeOut.setStatus("mandatory")
_Cdx6500LfcmLtrmStatsTotFrInData_Type = Counter32
_Cdx6500LfcmLtrmStatsTotFrInData_Object = MibTableColumn
cdx6500LfcmLtrmStatsTotFrInData = _Cdx6500LfcmLtrmStatsTotFrInData_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 9, 1, 16),
    _Cdx6500LfcmLtrmStatsTotFrInData_Type()
)
cdx6500LfcmLtrmStatsTotFrInData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmStatsTotFrInData.setStatus("mandatory")
_Cdx6500LfcmLtrmStatsTotFrOutData_Type = Counter32
_Cdx6500LfcmLtrmStatsTotFrOutData_Object = MibTableColumn
cdx6500LfcmLtrmStatsTotFrOutData = _Cdx6500LfcmLtrmStatsTotFrOutData_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 9, 1, 17),
    _Cdx6500LfcmLtrmStatsTotFrOutData_Type()
)
cdx6500LfcmLtrmStatsTotFrOutData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmStatsTotFrOutData.setStatus("mandatory")


class _Cdx6500LfcmLtrmStatsBoot_Type(Integer32):
    """Custom type cdx6500LfcmLtrmStatsBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("boot", 1)
    )


_Cdx6500LfcmLtrmStatsBoot_Type.__name__ = "Integer32"
_Cdx6500LfcmLtrmStatsBoot_Object = MibTableColumn
cdx6500LfcmLtrmStatsBoot = _Cdx6500LfcmLtrmStatsBoot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 9, 1, 18),
    _Cdx6500LfcmLtrmStatsBoot_Type()
)
cdx6500LfcmLtrmStatsBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLtrmStatsBoot.setStatus("mandatory")
_Cdx6500dot1dBridgeStatsGroup_ObjectIdentity = ObjectIdentity
cdx6500dot1dBridgeStatsGroup = _Cdx6500dot1dBridgeStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 10)
)
_Cdx6500dot1dBasePortStats_ObjectIdentity = ObjectIdentity
cdx6500dot1dBasePortStats = _Cdx6500dot1dBasePortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 10, 1)
)
_Cdx6500dot1dTpPortStats_ObjectIdentity = ObjectIdentity
cdx6500dot1dTpPortStats = _Cdx6500dot1dTpPortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 10, 2)
)
_Cdx6500LfcmTpPortLearnedEntries_Type = Integer32
_Cdx6500LfcmTpPortLearnedEntries_Object = MibScalar
cdx6500LfcmTpPortLearnedEntries = _Cdx6500LfcmTpPortLearnedEntries_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 10, 2, 1),
    _Cdx6500LfcmTpPortLearnedEntries_Type()
)
cdx6500LfcmTpPortLearnedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpPortLearnedEntries.setStatus("mandatory")
_Cdx6500LfcmTpPortAvailEntries_Type = Integer32
_Cdx6500LfcmTpPortAvailEntries_Object = MibScalar
cdx6500LfcmTpPortAvailEntries = _Cdx6500LfcmTpPortAvailEntries_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 10, 2, 2),
    _Cdx6500LfcmTpPortAvailEntries_Type()
)
cdx6500LfcmTpPortAvailEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpPortAvailEntries.setStatus("mandatory")
_Cdx6500LfcmTpPortMaximumEntries_Type = Integer32
_Cdx6500LfcmTpPortMaximumEntries_Object = MibScalar
cdx6500LfcmTpPortMaximumEntries = _Cdx6500LfcmTpPortMaximumEntries_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 10, 2, 3),
    _Cdx6500LfcmTpPortMaximumEntries_Type()
)
cdx6500LfcmTpPortMaximumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmTpPortMaximumEntries.setStatus("mandatory")
_Cdx6500dot1dBaseLinkStats_ObjectIdentity = ObjectIdentity
cdx6500dot1dBaseLinkStats = _Cdx6500dot1dBaseLinkStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 10, 3)
)
_Cdx6500LfcmNumLinks_Type = Integer32
_Cdx6500LfcmNumLinks_Object = MibScalar
cdx6500LfcmNumLinks = _Cdx6500LfcmNumLinks_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 10, 3, 1),
    _Cdx6500LfcmNumLinks_Type()
)
cdx6500LfcmNumLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmNumLinks.setStatus("mandatory")
_Cdx6500PSTPortBaseTable_Object = MibTable
cdx6500PSTPortBaseTable = _Cdx6500PSTPortBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 11)
)
if mibBuilder.loadTexts:
    cdx6500PSTPortBaseTable.setStatus("mandatory")
_Cdx6500PSTPortBasePortEntry_Object = MibTableRow
cdx6500PSTPortBasePortEntry = _Cdx6500PSTPortBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 11, 1)
)
cdx6500PSTPortBasePortEntry.setIndexNames(
    (0, "BRIDGE-OPT-MIB", "cdx6500LfcmBasePort"),
)
if mibBuilder.loadTexts:
    cdx6500PSTPortBasePortEntry.setStatus("mandatory")
_Cdx6500LfcmBasePort_Type = Integer32
_Cdx6500LfcmBasePort_Object = MibTableColumn
cdx6500LfcmBasePort = _Cdx6500LfcmBasePort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 11, 1, 1),
    _Cdx6500LfcmBasePort_Type()
)
cdx6500LfcmBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmBasePort.setStatus("mandatory")


class _Cdx6500LfcmBridgeLinkStatus_Type(Integer32):
    """Custom type cdx6500LfcmBridgeLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5,
              6,
              7,
              50)
        )
    )
    namedValues = NamedValues(
        *(("active", 6),
          ("configErr", 0),
          ("congested", 4),
          ("inactive", 5),
          ("newvalConfigErr", 50),
          ("swDisabled", 1),
          ("unconfig", 7),
          ("userDisabled", 3))
    )


_Cdx6500LfcmBridgeLinkStatus_Type.__name__ = "Integer32"
_Cdx6500LfcmBridgeLinkStatus_Object = MibTableColumn
cdx6500LfcmBridgeLinkStatus = _Cdx6500LfcmBridgeLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 11, 1, 2),
    _Cdx6500LfcmBridgeLinkStatus_Type()
)
cdx6500LfcmBridgeLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmBridgeLinkStatus.setStatus("mandatory")


class _Cdx6500LfcmClearStats_Type(Integer32):
    """Custom type cdx6500LfcmClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetStats", 1)
    )


_Cdx6500LfcmClearStats_Type.__name__ = "Integer32"
_Cdx6500LfcmClearStats_Object = MibTableColumn
cdx6500LfcmClearStats = _Cdx6500LfcmClearStats_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 11, 1, 3),
    _Cdx6500LfcmClearStats_Type()
)
cdx6500LfcmClearStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500LfcmClearStats.setStatus("mandatory")
_Cdx6500LfcmLastStatsReset_Type = DisplayString
_Cdx6500LfcmLastStatsReset_Object = MibTableColumn
cdx6500LfcmLastStatsReset = _Cdx6500LfcmLastStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 11, 1, 4),
    _Cdx6500LfcmLastStatsReset_Type()
)
cdx6500LfcmLastStatsReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500LfcmLastStatsReset.setStatus("mandatory")


class _Cdx6500LfcmBridgeBoot_Type(Integer32):
    """Custom type cdx6500LfcmBridgeBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("boot", 1)
    )


_Cdx6500LfcmBridgeBoot_Type.__name__ = "Integer32"
_Cdx6500LfcmBridgeBoot_Object = MibTableColumn
cdx6500LfcmBridgeBoot = _Cdx6500LfcmBridgeBoot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 11, 1, 5),
    _Cdx6500LfcmBridgeBoot_Type()
)
cdx6500LfcmBridgeBoot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500LfcmBridgeBoot.setStatus("mandatory")


class _Cdx6500LfcmPortBridgeLinkBoot_Type(Integer32):
    """Custom type cdx6500LfcmPortBridgeLinkBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("boot", 1)
    )


_Cdx6500LfcmPortBridgeLinkBoot_Type.__name__ = "Integer32"
_Cdx6500LfcmPortBridgeLinkBoot_Object = MibTableColumn
cdx6500LfcmPortBridgeLinkBoot = _Cdx6500LfcmPortBridgeLinkBoot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 11, 1, 6),
    _Cdx6500LfcmPortBridgeLinkBoot_Type()
)
cdx6500LfcmPortBridgeLinkBoot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500LfcmPortBridgeLinkBoot.setStatus("mandatory")


class _Cdx6500LfcmPortBlEnable_Type(Integer32):
    """Custom type cdx6500LfcmPortBlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_Cdx6500LfcmPortBlEnable_Type.__name__ = "Integer32"
_Cdx6500LfcmPortBlEnable_Object = MibTableColumn
cdx6500LfcmPortBlEnable = _Cdx6500LfcmPortBlEnable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 11, 1, 7),
    _Cdx6500LfcmPortBlEnable_Type()
)
cdx6500LfcmPortBlEnable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500LfcmPortBlEnable.setStatus("mandatory")


class _Cdx6500LfcmPortBlDisable_Type(Integer32):
    """Custom type cdx6500LfcmPortBlDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("disable", 1)
    )


_Cdx6500LfcmPortBlDisable_Type.__name__ = "Integer32"
_Cdx6500LfcmPortBlDisable_Object = MibTableColumn
cdx6500LfcmPortBlDisable = _Cdx6500LfcmPortBlDisable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 11, 1, 8),
    _Cdx6500LfcmPortBlDisable_Type()
)
cdx6500LfcmPortBlDisable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500LfcmPortBlDisable.setStatus("mandatory")


class _Cdx6500LfcmCtrlsPortSetLinkProt_Type(Integer32):
    """Custom type cdx6500LfcmCtrlsPortSetLinkProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setUcastProtection", 1)
    )


_Cdx6500LfcmCtrlsPortSetLinkProt_Type.__name__ = "Integer32"
_Cdx6500LfcmCtrlsPortSetLinkProt_Object = MibTableColumn
cdx6500LfcmCtrlsPortSetLinkProt = _Cdx6500LfcmCtrlsPortSetLinkProt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 11, 1, 9),
    _Cdx6500LfcmCtrlsPortSetLinkProt_Type()
)
cdx6500LfcmCtrlsPortSetLinkProt.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500LfcmCtrlsPortSetLinkProt.setStatus("mandatory")


class _Cdx6500LfcmCtrlsPortClrLinkProt_Type(Integer32):
    """Custom type cdx6500LfcmCtrlsPortClrLinkProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearUcastProtection", 1)
    )


_Cdx6500LfcmCtrlsPortClrLinkProt_Type.__name__ = "Integer32"
_Cdx6500LfcmCtrlsPortClrLinkProt_Object = MibTableColumn
cdx6500LfcmCtrlsPortClrLinkProt = _Cdx6500LfcmCtrlsPortClrLinkProt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 11, 1, 10),
    _Cdx6500LfcmCtrlsPortClrLinkProt_Type()
)
cdx6500LfcmCtrlsPortClrLinkProt.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500LfcmCtrlsPortClrLinkProt.setStatus("mandatory")


class _Cdx6500LfcmCtrlsPortSetMultProt_Type(Integer32):
    """Custom type cdx6500LfcmCtrlsPortSetMultProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setMcastProtection", 1)
    )


_Cdx6500LfcmCtrlsPortSetMultProt_Type.__name__ = "Integer32"
_Cdx6500LfcmCtrlsPortSetMultProt_Object = MibTableColumn
cdx6500LfcmCtrlsPortSetMultProt = _Cdx6500LfcmCtrlsPortSetMultProt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 11, 1, 11),
    _Cdx6500LfcmCtrlsPortSetMultProt_Type()
)
cdx6500LfcmCtrlsPortSetMultProt.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500LfcmCtrlsPortSetMultProt.setStatus("mandatory")


class _Cdx6500LfcmCtrlsPortClrMultProt_Type(Integer32):
    """Custom type cdx6500LfcmCtrlsPortClrMultProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearMcastProtection", 1)
    )


_Cdx6500LfcmCtrlsPortClrMultProt_Type.__name__ = "Integer32"
_Cdx6500LfcmCtrlsPortClrMultProt_Object = MibTableColumn
cdx6500LfcmCtrlsPortClrMultProt = _Cdx6500LfcmCtrlsPortClrMultProt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5, 11, 1, 12),
    _Cdx6500LfcmCtrlsPortClrMultProt_Type()
)
cdx6500LfcmCtrlsPortClrMultProt.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500LfcmCtrlsPortClrMultProt.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRIDGE-OPT-MIB",
    **{"MacAddress": MacAddress,
       "DisplayString": DisplayString,
       "BridgeId": BridgeId,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTBridgeGroup": cdx6500PCTBridgeGroup,
       "cdx6500PCTPortStaticAddrTable": cdx6500PCTPortStaticAddrTable,
       "cdx6500PCTPortStaticAddrEntry": cdx6500PCTPortStaticAddrEntry,
       "cdx6500LfcmStaticAddrEntryNumber": cdx6500LfcmStaticAddrEntryNumber,
       "cdx6500LfcmStaticMacAddr": cdx6500LfcmStaticMacAddr,
       "cdx6500LfcmStaticIncSrcLinkAct": cdx6500LfcmStaticIncSrcLinkAct,
       "cdx6500LfcmStaticOutSrcLinkAct": cdx6500LfcmStaticOutSrcLinkAct,
       "cdx6500LfcmStaticIncDestLinkAct": cdx6500LfcmStaticIncDestLinkAct,
       "cdx6500LfcmStaticOutDestLinkAct": cdx6500LfcmStaticOutDestLinkAct,
       "cdx6500LfcmStaticIncSrcList": cdx6500LfcmStaticIncSrcList,
       "cdx6500LfcmStaticOutSrcList": cdx6500LfcmStaticOutSrcList,
       "cdx6500LfcmStaticIncDestList": cdx6500LfcmStaticIncDestList,
       "cdx6500LfcmStaticOutDestList": cdx6500LfcmStaticOutDestList,
       "cdx6500LfcmStaticMacMask": cdx6500LfcmStaticMacMask,
       "cdx6500PCTPortStaticProtTable": cdx6500PCTPortStaticProtTable,
       "cdx6500PCTPortStaticProtEntry": cdx6500PCTPortStaticProtEntry,
       "cdx6500LfcmStaticProtEntryNumber": cdx6500LfcmStaticProtEntryNumber,
       "cdx6500LfcmStaticType": cdx6500LfcmStaticType,
       "cdx6500LfcmStaticValue": cdx6500LfcmStaticValue,
       "cdx6500LfcmStaticIncProtLinkAct": cdx6500LfcmStaticIncProtLinkAct,
       "cdx6500LfcmStaticOutProtLinkAct": cdx6500LfcmStaticOutProtLinkAct,
       "cdx6500LfcmStaticIncProtList": cdx6500LfcmStaticIncProtList,
       "cdx6500LfcmStaticOutProtList": cdx6500LfcmStaticOutProtList,
       "cdx6500LfcmStaticValue1": cdx6500LfcmStaticValue1,
       "cdx6500LfcmStaticValue2": cdx6500LfcmStaticValue2,
       "cdx6500PCTSrLinkTable": cdx6500PCTSrLinkTable,
       "cdx6500PCTSrLinkEntry": cdx6500PCTSrLinkEntry,
       "cdx6500LfcmSrLink": cdx6500LfcmSrLink,
       "cdx6500LfcmSrLinkHopCount": cdx6500LfcmSrLinkHopCount,
       "cdx6500LfcmSrLinkBridgeNum": cdx6500LfcmSrLinkBridgeNum,
       "cdx6500LfcmSrLinkTargetSegment": cdx6500LfcmSrLinkTargetSegment,
       "cdx6500LfcmSrLinkLargestFrame": cdx6500LfcmSrLinkLargestFrame,
       "cdx6500LfcmSrLinkMode": cdx6500LfcmSrLinkMode,
       "cdx6500LfcmSrLinkVsegNum": cdx6500LfcmSrLinkVsegNum,
       "cdx6500PCTStaticLinkTable": cdx6500PCTStaticLinkTable,
       "cdx6500PCTStaticLinkEntry": cdx6500PCTStaticLinkEntry,
       "cdx6500LfcmLinkStaticAddress": cdx6500LfcmLinkStaticAddress,
       "cdx6500LfcmLinkStaticReceivePort": cdx6500LfcmLinkStaticReceivePort,
       "cdx6500LfcmLinkStaticAllowToGoTo": cdx6500LfcmLinkStaticAllowToGoTo,
       "cdx6500LfcmLinkStaticStatus": cdx6500LfcmLinkStaticStatus,
       "cdx6500PCTLtrmStnTable": cdx6500PCTLtrmStnTable,
       "cdx6500PCTLtrmStnEntry": cdx6500PCTLtrmStnEntry,
       "cdx6500LfcmLtrmStnEntryNumber": cdx6500LfcmLtrmStnEntryNumber,
       "cdx6500LfcmLtrmMacAddress": cdx6500LfcmLtrmMacAddress,
       "cdx6500LfcmLtrmSap": cdx6500LfcmLtrmSap,
       "cdx6500LfcmLtrmProfileName": cdx6500LfcmLtrmProfileName,
       "cdx6500PCTLtrmProfTable": cdx6500PCTLtrmProfTable,
       "cdx6500PCTLtrmProfEntry": cdx6500PCTLtrmProfEntry,
       "cdx6500LfcmLtrmProfEntryNumber": cdx6500LfcmLtrmProfEntryNumber,
       "cdx6500LfcmLtrmProfLlcName": cdx6500LfcmLtrmProfLlcName,
       "cdx6500LfcmLtrmProfTimeout1": cdx6500LfcmLtrmProfTimeout1,
       "cdx6500LfcmLtrmProfTimeout2": cdx6500LfcmLtrmProfTimeout2,
       "cdx6500LfcmLtrmProfTimeout3": cdx6500LfcmLtrmProfTimeout3,
       "cdx6500LfcmLtrmProfN2": cdx6500LfcmLtrmProfN2,
       "cdx6500LfcmLtrmProfN3": cdx6500LfcmLtrmProfN3,
       "cdx6500LfcmLtrmProfTxWindowsize": cdx6500LfcmLtrmProfTxWindowsize,
       "cdx6500dot1dBridgeCfgGroup": cdx6500dot1dBridgeCfgGroup,
       "cdx6500dot1dBasePortCfg": cdx6500dot1dBasePortCfg,
       "cdx6500LfcmBridgeLfMode": cdx6500LfcmBridgeLfMode,
       "cdx6500LfcmWanDataPri": cdx6500LfcmWanDataPri,
       "cdx6500LfcmLearnOnlyPeriod": cdx6500LfcmLearnOnlyPeriod,
       "cdx6500LfcmLssRingNumber": cdx6500LfcmLssRingNumber,
       "cdx6500LfcmBridgedProtocols": cdx6500LfcmBridgedProtocols,
       "cdx6500LfcmMaxBridgeLinks": cdx6500LfcmMaxBridgeLinks,
       "cdx6500LfcmBridgeId": cdx6500LfcmBridgeId,
       "cdx6500dot1dStpPortCfg": cdx6500dot1dStpPortCfg,
       "cdx6500LfcmStpControl": cdx6500LfcmStpControl,
       "cdx6500LfcmStpBadHelloThreshold": cdx6500LfcmStpBadHelloThreshold,
       "cdx6500LfcmStpBadHelloTimeout": cdx6500LfcmStpBadHelloTimeout,
       "cdx6500LtrmCfg": cdx6500LtrmCfg,
       "cdx6500LfcmLtrmWanTimeout1": cdx6500LfcmLtrmWanTimeout1,
       "cdx6500LfcmLtrmWanTimeout2": cdx6500LfcmLtrmWanTimeout2,
       "cdx6500LfcmLtrmWanTimeout3": cdx6500LfcmLtrmWanTimeout3,
       "cdx6500LfcmLtrmWanN2": cdx6500LfcmLtrmWanN2,
       "cdx6500LfcmLtrmWanN3": cdx6500LfcmLtrmWanN3,
       "cdx6500LfcmLtrmWanTxWindowSize": cdx6500LfcmLtrmWanTxWindowSize,
       "cdx6500LfcmBaseLlcLtrmDataPri": cdx6500LfcmBaseLlcLtrmDataPri,
       "cdx6500LssCfg": cdx6500LssCfg,
       "cdx6500LfcmLssVirtualPortMacAddr": cdx6500LfcmLssVirtualPortMacAddr,
       "cdx6500LfcmLssBridgeId": cdx6500LfcmLssBridgeId,
       "cdx6500LfcmLssNotificationInter": cdx6500LfcmLssNotificationInter,
       "cdx6500LfcmLssCalculationInter": cdx6500LfcmLssCalculationInter,
       "cdx6500LfcmLssPathTraceCtrl": cdx6500LfcmLssPathTraceCtrl,
       "cdx6500PCTTbPermTable": cdx6500PCTTbPermTable,
       "cdx6500PCTTbPermEntry": cdx6500PCTTbPermEntry,
       "cdx6500LfcmTbEntry": cdx6500LfcmTbEntry,
       "cdx6500LfcmTpPortLocalMacAddress": cdx6500LfcmTpPortLocalMacAddress,
       "cdx6500LfcmTpPortBridgeLinkNums": cdx6500LfcmTpPortBridgeLinkNums,
       "cdx6500PCTdot1dBaseLinkTable": cdx6500PCTdot1dBaseLinkTable,
       "cdx6500PCTdot1dBaseLinkEntry": cdx6500PCTdot1dBaseLinkEntry,
       "cdx6500LfcmBaseLinkIndex": cdx6500LfcmBaseLinkIndex,
       "cdx6500LfcmLinkType": cdx6500LfcmLinkType,
       "cdx6500LfcmMacAddrFilterAction": cdx6500LfcmMacAddrFilterAction,
       "cdx6500LfcmProtocolFilterAction": cdx6500LfcmProtocolFilterAction,
       "cdx6500LfcmStpLinkManState": cdx6500LfcmStpLinkManState,
       "cdx6500LfcmNbiosFilterAction": cdx6500LfcmNbiosFilterAction,
       "cdx6500PCTBasePortTable": cdx6500PCTBasePortTable,
       "cdx6500PCTBasePortEntry": cdx6500PCTBasePortEntry,
       "cdx6500LfcmBasePortIndex": cdx6500LfcmBasePortIndex,
       "cdx6500LfcmPortAddrFiltAction": cdx6500LfcmPortAddrFiltAction,
       "cdx6500LfcmPortProtFiltAction": cdx6500LfcmPortProtFiltAction,
       "cdx6500LfcmPortStptManState": cdx6500LfcmPortStptManState,
       "cdx6500PCTNetBiosTable": cdx6500PCTNetBiosTable,
       "cdx6500PCTNetBiosEntry": cdx6500PCTNetBiosEntry,
       "cdx6500LfcmNetBiosIndex": cdx6500LfcmNetBiosIndex,
       "cdx6500LfcmNbiosStrType": cdx6500LfcmNbiosStrType,
       "cdx6500LfcmNbiosAsciiName": cdx6500LfcmNbiosAsciiName,
       "cdx6500LfcmNbiosHexName": cdx6500LfcmNbiosHexName,
       "cdx6500LfcmNbiosIncAction": cdx6500LfcmNbiosIncAction,
       "cdx6500LfcmNbiosIncList": cdx6500LfcmNbiosIncList,
       "cdx6500LfcmNbiosOutAction": cdx6500LfcmNbiosOutAction,
       "cdx6500LfcmNbiosOutList": cdx6500LfcmNbiosOutList,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTBridgeGroup": cdx6500PSTBridgeGroup,
       "cdx6500PSTSrPortTable": cdx6500PSTSrPortTable,
       "cdx6500PSTSrPortEntry": cdx6500PSTSrPortEntry,
       "cdx6500LfcmSrPortIfIndex": cdx6500LfcmSrPortIfIndex,
       "cdx6500LfcmSrPortFramesRx": cdx6500LfcmSrPortFramesRx,
       "cdx6500LfcmSrPortFramesTx": cdx6500LfcmSrPortFramesTx,
       "cdx6500LfcmSrPortRingNumber": cdx6500LfcmSrPortRingNumber,
       "cdx6500PSTTpPortTable": cdx6500PSTTpPortTable,
       "cdx6500PSTTpPortEntry": cdx6500PSTTpPortEntry,
       "cdx6500LfcmTpPortIfIndex": cdx6500LfcmTpPortIfIndex,
       "cdx6500LfcmTpPortUnicastRx": cdx6500LfcmTpPortUnicastRx,
       "cdx6500LfcmTpPortUnicastTx": cdx6500LfcmTpPortUnicastTx,
       "cdx6500LfcmTpPortMulticastRx": cdx6500LfcmTpPortMulticastRx,
       "cdx6500LfcmTpPortMulticastTx": cdx6500LfcmTpPortMulticastTx,
       "cdx6500LfcmTpPortBroadcastRx": cdx6500LfcmTpPortBroadcastRx,
       "cdx6500LfcmTpPortBroadcastTx": cdx6500LfcmTpPortBroadcastTx,
       "cdx6500LfcmTpPortInboundDisc": cdx6500LfcmTpPortInboundDisc,
       "cdx6500LfcmTpPortOutboundDisc": cdx6500LfcmTpPortOutboundDisc,
       "cdx6500LfcmTpPortULPInBoundDisc": cdx6500LfcmTpPortULPInBoundDisc,
       "cdx6500LfcmTpPortULPOutBoundDisc": cdx6500LfcmTpPortULPOutBoundDisc,
       "cdx6500LfcmTpPortMLPInBoundDisc": cdx6500LfcmTpPortMLPInBoundDisc,
       "cdx6500LfcmTpPortMLPOutBoundDisc": cdx6500LfcmTpPortMLPOutBoundDisc,
       "cdx6500PSTPortFilterTable": cdx6500PSTPortFilterTable,
       "cdx6500PSTPortFilterEntry": cdx6500PSTPortFilterEntry,
       "cdx6500LfcmPortFilterIfIndex": cdx6500LfcmPortFilterIfIndex,
       "cdx6500LfcmPortFilSrcAddrInDisc": cdx6500LfcmPortFilSrcAddrInDisc,
       "cdx6500LfcmPortFilSrcAddrOutDisc": cdx6500LfcmPortFilSrcAddrOutDisc,
       "cdx6500LfcmPortFilDestAddrInDisc": cdx6500LfcmPortFilDestAddrInDisc,
       "cdx6500LfcmPortFilDestAddrOutDisc": cdx6500LfcmPortFilDestAddrOutDisc,
       "cdx6500LfcmPortFilProtInDisc": cdx6500LfcmPortFilProtInDisc,
       "cdx6500LfcmPortFilProtOutDisc": cdx6500LfcmPortFilProtOutDisc,
       "cdx6500LfcmPortFilTotalInDisc": cdx6500LfcmPortFilTotalInDisc,
       "cdx6500LfcmPortFilTotalOutDisc": cdx6500LfcmPortFilTotalOutDisc,
       "cdx6500PSTBaseLinkTable": cdx6500PSTBaseLinkTable,
       "cdx6500PSTBaseLinkEntry": cdx6500PSTBaseLinkEntry,
       "cdx6500LfcmBaseLink": cdx6500LfcmBaseLink,
       "cdx6500LfcmBaseLinkIfIndex": cdx6500LfcmBaseLinkIfIndex,
       "cdx6500LfcmBaseLinkCircuit": cdx6500LfcmBaseLinkCircuit,
       "cdx6500LfcmBaseLinkBlStatus": cdx6500LfcmBaseLinkBlStatus,
       "cdx6500LfcmBaseLinkClearStats": cdx6500LfcmBaseLinkClearStats,
       "cdx6500LfcmBaseLinkLastStatReset": cdx6500LfcmBaseLinkLastStatReset,
       "cdx6500LfcmLinkBridgeLinkBoot": cdx6500LfcmLinkBridgeLinkBoot,
       "cdx6500LfcmLinkBlEnable": cdx6500LfcmLinkBlEnable,
       "cdx6500LfcmLinkBlDisable": cdx6500LfcmLinkBlDisable,
       "cdx6500LfcmCtrlsLinkSetLinkProt": cdx6500LfcmCtrlsLinkSetLinkProt,
       "cdx6500LfcmCtrlsLinkClrLinkProt": cdx6500LfcmCtrlsLinkClrLinkProt,
       "cdx6500LfcmCtrlsLinkSetMultProt": cdx6500LfcmCtrlsLinkSetMultProt,
       "cdx6500LfcmCtrlsLinkClrMultProt": cdx6500LfcmCtrlsLinkClrMultProt,
       "cdx6500PSTSrLinkTable": cdx6500PSTSrLinkTable,
       "cdx6500PSTSrLinkEntry": cdx6500PSTSrLinkEntry,
       "cdx6500LfcmSrLinkIfIndex": cdx6500LfcmSrLinkIfIndex,
       "cdx6500LfcmSrLinkSteSpanMode": cdx6500LfcmSrLinkSteSpanMode,
       "cdx6500LfcmSrLinkSpecInFrames": cdx6500LfcmSrLinkSpecInFrames,
       "cdx6500LfcmSrLinkSpecOutFrames": cdx6500LfcmSrLinkSpecOutFrames,
       "cdx6500LfcmSrLinkApeInFrames": cdx6500LfcmSrLinkApeInFrames,
       "cdx6500LfcmSrLinkApeOutFrames": cdx6500LfcmSrLinkApeOutFrames,
       "cdx6500LfcmSrLinkSteOutFrames": cdx6500LfcmSrLinkSteOutFrames,
       "cdx6500LfcmSrLinkSteinFrames": cdx6500LfcmSrLinkSteinFrames,
       "cdx6500LfcmSrLinkSegMisDisc": cdx6500LfcmSrLinkSegMisDisc,
       "cdx6500LfcmSrLinkDupSegDisc": cdx6500LfcmSrLinkDupSegDisc,
       "cdx6500LfcmSrLinkHopCountExcDisc": cdx6500LfcmSrLinkHopCountExcDisc,
       "cdx6500LfcmSrLinkTotalFramesRx": cdx6500LfcmSrLinkTotalFramesRx,
       "cdx6500LfcmSrLinkTotalFramesTx": cdx6500LfcmSrLinkTotalFramesTx,
       "cdx6500LfcmSrLinkNextRingNumber": cdx6500LfcmSrLinkNextRingNumber,
       "cdx6500PSTTpLinkTable": cdx6500PSTTpLinkTable,
       "cdx6500PSTTpLinkEntry": cdx6500PSTTpLinkEntry,
       "cdx6500LfcmTpLink": cdx6500LfcmTpLink,
       "cdx6500LfcmTpLinkMaxInfo": cdx6500LfcmTpLinkMaxInfo,
       "cdx6500LfcmTpLinkInFrames": cdx6500LfcmTpLinkInFrames,
       "cdx6500LfcmTpLinkOutFrames": cdx6500LfcmTpLinkOutFrames,
       "cdx6500LfcmTpLinkInDiscards": cdx6500LfcmTpLinkInDiscards,
       "cdx6500LfcmTpLinkUnicastRx": cdx6500LfcmTpLinkUnicastRx,
       "cdx6500LfcmTpLinkUnicastTx": cdx6500LfcmTpLinkUnicastTx,
       "cdx6500LfcmTpLinkMulticastRx": cdx6500LfcmTpLinkMulticastRx,
       "cdx6500LfcmTpLinkMulticastTx": cdx6500LfcmTpLinkMulticastTx,
       "cdx6500LfcmTpLinkBroadcastRx": cdx6500LfcmTpLinkBroadcastRx,
       "cdx6500LfcmTpLinkBroadcastTx": cdx6500LfcmTpLinkBroadcastTx,
       "cdx6500LfcmTpLinkInBoundDisc": cdx6500LfcmTpLinkInBoundDisc,
       "cdx6500LfcmTpLinkOutBoundDisc": cdx6500LfcmTpLinkOutBoundDisc,
       "cdx6500LfcmTpLinkULPInBoundDisc": cdx6500LfcmTpLinkULPInBoundDisc,
       "cdx6500LfcmTpLinkULPOutBoundDisc": cdx6500LfcmTpLinkULPOutBoundDisc,
       "cdx6500LfcmTpLinkMLPInBoundDisc": cdx6500LfcmTpLinkMLPInBoundDisc,
       "cdx6500LfcmTpLinkMLPOutBoundDisc": cdx6500LfcmTpLinkMLPOutBoundDisc,
       "cdx6500PSTStpLinkTable": cdx6500PSTStpLinkTable,
       "cdx6500PSTStpLinkEntry": cdx6500PSTStpLinkEntry,
       "cdx6500LfcmStpLink": cdx6500LfcmStpLink,
       "cdx6500LfcmStpPriority": cdx6500LfcmStpPriority,
       "cdx6500LfcmStpState": cdx6500LfcmStpState,
       "cdx6500LfcmStpEnable": cdx6500LfcmStpEnable,
       "cdx6500LfcmStpPathCost": cdx6500LfcmStpPathCost,
       "cdx6500LfcmStpDesignatedRoot": cdx6500LfcmStpDesignatedRoot,
       "cdx6500LfcmStpDesignatedCost": cdx6500LfcmStpDesignatedCost,
       "cdx6500LfcmStpDesignatedBridge": cdx6500LfcmStpDesignatedBridge,
       "cdx6500LfcmStpDesignatedPort": cdx6500LfcmStpDesignatedPort,
       "cdx6500LfcmStpForwardTransitions": cdx6500LfcmStpForwardTransitions,
       "cdx6500PSTStaticStatsLinkTable": cdx6500PSTStaticStatsLinkTable,
       "cdx6500PSTStaticsStatsLinkEntry": cdx6500PSTStaticsStatsLinkEntry,
       "cdx6500LfcmLinkFilterIndex": cdx6500LfcmLinkFilterIndex,
       "cdx6500LfcmLinkFilSrcAddrInDisc": cdx6500LfcmLinkFilSrcAddrInDisc,
       "cdx6500LfcmLinkFilSrcAddrOutDisc": cdx6500LfcmLinkFilSrcAddrOutDisc,
       "cdx6500LfcmLinkFilDestAddrInDisc": cdx6500LfcmLinkFilDestAddrInDisc,
       "cdx6500LfcmLinkFilDestAddrOutDisc": cdx6500LfcmLinkFilDestAddrOutDisc,
       "cdx6500LfcmLinkFilProtInDisc": cdx6500LfcmLinkFilProtInDisc,
       "cdx6500LfcmLinkFilProtOutDisc": cdx6500LfcmLinkFilProtOutDisc,
       "cdx6500LfcmLinkFilTotalInDisc": cdx6500LfcmLinkFilTotalInDisc,
       "cdx6500LfcmLinkFilTotalOutDisc": cdx6500LfcmLinkFilTotalOutDisc,
       "cdx6500PSTLtrmStatsTable": cdx6500PSTLtrmStatsTable,
       "cdx6500PSTLtrmStatsEntry": cdx6500PSTLtrmStatsEntry,
       "cdx6500LfcmLtrmStatsIndex": cdx6500LfcmLtrmStatsIndex,
       "cdx6500LfcmLtrmStatsDataCharIn": cdx6500LfcmLtrmStatsDataCharIn,
       "cdx6500LfcmLtrmStatsDataCharOut": cdx6500LfcmLtrmStatsDataCharOut,
       "cdx6500LfcmLtrmStatsDataFrIn": cdx6500LfcmLtrmStatsDataFrIn,
       "cdx6500LfcmLtrmStatsDataFrOut": cdx6500LfcmLtrmStatsDataFrOut,
       "cdx6500LfcmLtrmStatsCtFrRrIn": cdx6500LfcmLtrmStatsCtFrRrIn,
       "cdx6500LfcmLtrmStatsCtFrRrOut": cdx6500LfcmLtrmStatsCtFrRrOut,
       "cdx6500LfcmLtrmStatsCtFrRnrIn": cdx6500LfcmLtrmStatsCtFrRnrIn,
       "cdx6500LfcmLtrmStatsCtFrRnrOut": cdx6500LfcmLtrmStatsCtFrRnrOut,
       "cdx6500LfcmLtrmStatsCtFrXidIn": cdx6500LfcmLtrmStatsCtFrXidIn,
       "cdx6500LfcmLtrmStatsCtFrXidOut": cdx6500LfcmLtrmStatsCtFrXidOut,
       "cdx6500LfcmLtrmStatsCtFrRejIn": cdx6500LfcmLtrmStatsCtFrRejIn,
       "cdx6500LfcmLtrmStatsCtFrRejOut": cdx6500LfcmLtrmStatsCtFrRejOut,
       "cdx6500LfcmLtrmStatsCtFrSabmeIn": cdx6500LfcmLtrmStatsCtFrSabmeIn,
       "cdx6500LfcmLtrmStatsCtFrSabmeOut": cdx6500LfcmLtrmStatsCtFrSabmeOut,
       "cdx6500LfcmLtrmStatsTotFrInData": cdx6500LfcmLtrmStatsTotFrInData,
       "cdx6500LfcmLtrmStatsTotFrOutData": cdx6500LfcmLtrmStatsTotFrOutData,
       "cdx6500LfcmLtrmStatsBoot": cdx6500LfcmLtrmStatsBoot,
       "cdx6500dot1dBridgeStatsGroup": cdx6500dot1dBridgeStatsGroup,
       "cdx6500dot1dBasePortStats": cdx6500dot1dBasePortStats,
       "cdx6500dot1dTpPortStats": cdx6500dot1dTpPortStats,
       "cdx6500LfcmTpPortLearnedEntries": cdx6500LfcmTpPortLearnedEntries,
       "cdx6500LfcmTpPortAvailEntries": cdx6500LfcmTpPortAvailEntries,
       "cdx6500LfcmTpPortMaximumEntries": cdx6500LfcmTpPortMaximumEntries,
       "cdx6500dot1dBaseLinkStats": cdx6500dot1dBaseLinkStats,
       "cdx6500LfcmNumLinks": cdx6500LfcmNumLinks,
       "cdx6500PSTPortBaseTable": cdx6500PSTPortBaseTable,
       "cdx6500PSTPortBasePortEntry": cdx6500PSTPortBasePortEntry,
       "cdx6500LfcmBasePort": cdx6500LfcmBasePort,
       "cdx6500LfcmBridgeLinkStatus": cdx6500LfcmBridgeLinkStatus,
       "cdx6500LfcmClearStats": cdx6500LfcmClearStats,
       "cdx6500LfcmLastStatsReset": cdx6500LfcmLastStatsReset,
       "cdx6500LfcmBridgeBoot": cdx6500LfcmBridgeBoot,
       "cdx6500LfcmPortBridgeLinkBoot": cdx6500LfcmPortBridgeLinkBoot,
       "cdx6500LfcmPortBlEnable": cdx6500LfcmPortBlEnable,
       "cdx6500LfcmPortBlDisable": cdx6500LfcmPortBlDisable,
       "cdx6500LfcmCtrlsPortSetLinkProt": cdx6500LfcmCtrlsPortSetLinkProt,
       "cdx6500LfcmCtrlsPortClrLinkProt": cdx6500LfcmCtrlsPortClrLinkProt,
       "cdx6500LfcmCtrlsPortSetMultProt": cdx6500LfcmCtrlsPortSetMultProt,
       "cdx6500LfcmCtrlsPortClrMultProt": cdx6500LfcmCtrlsPortClrMultProt}
)
