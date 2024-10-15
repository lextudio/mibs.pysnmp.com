# SNMP MIB module (CISCO-DIFFSERV-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DIFFSERV-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:04 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(vsanIndex,) = mibBuilder.importSymbols(
    "CISCO-VSAN-MIB",
    "vsanIndex")

(IndexInteger,
 IndexIntegerNextFree,
 diffServClfrEntry) = mibBuilder.importSymbols(
    "DIFFSERV-MIB",
    "IndexInteger",
    "IndexIntegerNextFree",
    "diffServClfrEntry")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
    "iso")

(DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoDiffServExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 381)
)
ciscoDiffServExtMIB.setRevisions(
        ("2004-11-16 00:00",
         "2003-12-18 00:00",
         "2003-12-12 00:00",
         "2003-12-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CdsmDataDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )



class CdsmFcAddrAndMask(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(3, 3),
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(8, 8),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoDiffServExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDiffServExtMIBObjects = _CiscoDiffServExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1)
)
_CdsmConfiguration_ObjectIdentity = ObjectIdentity
cdsmConfiguration = _CdsmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1)
)
_CdsmDataPathTable_Object = MibTable
cdsmDataPathTable = _CdsmDataPathTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cdsmDataPathTable.setStatus("current")
_CdsmDataPathEntry_Object = MibTableRow
cdsmDataPathEntry = _CdsmDataPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 1, 1)
)
cdsmDataPathEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-DIFFSERV-EXT-MIB", "cdsmDataPathDirection"),
)
if mibBuilder.loadTexts:
    cdsmDataPathEntry.setStatus("current")
_CdsmDataPathDirection_Type = CdsmDataDirection
_CdsmDataPathDirection_Object = MibTableColumn
cdsmDataPathDirection = _CdsmDataPathDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 1, 1, 1),
    _CdsmDataPathDirection_Type()
)
cdsmDataPathDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsmDataPathDirection.setStatus("current")
_CdsmDataPathClfrStart_Type = RowPointer
_CdsmDataPathClfrStart_Object = MibTableColumn
cdsmDataPathClfrStart = _CdsmDataPathClfrStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 1, 1, 2),
    _CdsmDataPathClfrStart_Type()
)
cdsmDataPathClfrStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmDataPathClfrStart.setStatus("current")
_CdsmDataPathStatus_Type = RowStatus
_CdsmDataPathStatus_Object = MibTableColumn
cdsmDataPathStatus = _CdsmDataPathStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 1, 1, 3),
    _CdsmDataPathStatus_Type()
)
cdsmDataPathStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmDataPathStatus.setStatus("current")
_CdsmClfrTable_Object = MibTable
cdsmClfrTable = _CdsmClfrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cdsmClfrTable.setStatus("current")
_CdsmClfrEntry_Object = MibTableRow
cdsmClfrEntry = _CdsmClfrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cdsmClfrEntry.setStatus("current")


class _CdsmClfrName_Type(SnmpAdminString):
    """Custom type cdsmClfrName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_CdsmClfrName_Type.__name__ = "SnmpAdminString"
_CdsmClfrName_Object = MibTableColumn
cdsmClfrName = _CdsmClfrName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 2, 1, 1),
    _CdsmClfrName_Type()
)
cdsmClfrName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmClfrName.setStatus("current")
_CdsmClfrNextFreeElement_Type = IndexIntegerNextFree
_CdsmClfrNextFreeElement_Object = MibTableColumn
cdsmClfrNextFreeElement = _CdsmClfrNextFreeElement_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 2, 1, 2),
    _CdsmClfrNextFreeElement_Type()
)
cdsmClfrNextFreeElement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmClfrNextFreeElement.setStatus("current")
_CdsmFCMultiFieldClfrTable_Object = MibTable
cdsmFCMultiFieldClfrTable = _CdsmFCMultiFieldClfrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cdsmFCMultiFieldClfrTable.setStatus("current")
_CdsmFCMultiFieldClfrEntry_Object = MibTableRow
cdsmFCMultiFieldClfrEntry = _CdsmFCMultiFieldClfrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 3, 1)
)
cdsmFCMultiFieldClfrEntry.setIndexNames(
    (0, "CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldClfrId"),
)
if mibBuilder.loadTexts:
    cdsmFCMultiFieldClfrEntry.setStatus("current")
_CdsmFCMultiFieldClfrId_Type = IndexInteger
_CdsmFCMultiFieldClfrId_Object = MibTableColumn
cdsmFCMultiFieldClfrId = _CdsmFCMultiFieldClfrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 3, 1, 1),
    _CdsmFCMultiFieldClfrId_Type()
)
cdsmFCMultiFieldClfrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsmFCMultiFieldClfrId.setStatus("current")


class _CdsmFCMultiFieldClfrName_Type(SnmpAdminString):
    """Custom type cdsmFCMultiFieldClfrName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_CdsmFCMultiFieldClfrName_Type.__name__ = "SnmpAdminString"
_CdsmFCMultiFieldClfrName_Object = MibTableColumn
cdsmFCMultiFieldClfrName = _CdsmFCMultiFieldClfrName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 3, 1, 2),
    _CdsmFCMultiFieldClfrName_Type()
)
cdsmFCMultiFieldClfrName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmFCMultiFieldClfrName.setStatus("current")
_CdsmFCMultiFieldClfrMatch_Type = TruthValue
_CdsmFCMultiFieldClfrMatch_Object = MibTableColumn
cdsmFCMultiFieldClfrMatch = _CdsmFCMultiFieldClfrMatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 3, 1, 3),
    _CdsmFCMultiFieldClfrMatch_Type()
)
cdsmFCMultiFieldClfrMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmFCMultiFieldClfrMatch.setStatus("current")
_CdsmFCMultiFieldClfrStatus_Type = RowStatus
_CdsmFCMultiFieldClfrStatus_Object = MibTableColumn
cdsmFCMultiFieldClfrStatus = _CdsmFCMultiFieldClfrStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 3, 1, 4),
    _CdsmFCMultiFieldClfrStatus_Type()
)
cdsmFCMultiFieldClfrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmFCMultiFieldClfrStatus.setStatus("current")
_CdsmFCMultiFieldClfrNextFreeStmt_Type = IndexIntegerNextFree
_CdsmFCMultiFieldClfrNextFreeStmt_Object = MibTableColumn
cdsmFCMultiFieldClfrNextFreeStmt = _CdsmFCMultiFieldClfrNextFreeStmt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 3, 1, 5),
    _CdsmFCMultiFieldClfrNextFreeStmt_Type()
)
cdsmFCMultiFieldClfrNextFreeStmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmFCMultiFieldClfrNextFreeStmt.setStatus("current")
_CdsmFCMultiFieldMatchStmtTable_Object = MibTable
cdsmFCMultiFieldMatchStmtTable = _CdsmFCMultiFieldMatchStmtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cdsmFCMultiFieldMatchStmtTable.setStatus("current")
_CdsmFCMultiFieldMatchStmtEntry_Object = MibTableRow
cdsmFCMultiFieldMatchStmtEntry = _CdsmFCMultiFieldMatchStmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 4, 1)
)
cdsmFCMultiFieldMatchStmtEntry.setIndexNames(
    (0, "CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldClfrId"),
    (0, "CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldMatchId"),
)
if mibBuilder.loadTexts:
    cdsmFCMultiFieldMatchStmtEntry.setStatus("current")


class _CdsmFCMultiFieldMatchId_Type(Unsigned32):
    """Custom type cdsmFCMultiFieldMatchId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CdsmFCMultiFieldMatchId_Type.__name__ = "Unsigned32"
_CdsmFCMultiFieldMatchId_Object = MibTableColumn
cdsmFCMultiFieldMatchId = _CdsmFCMultiFieldMatchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 4, 1, 1),
    _CdsmFCMultiFieldMatchId_Type()
)
cdsmFCMultiFieldMatchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsmFCMultiFieldMatchId.setStatus("current")


class _CdsmFCMultiFieldMatchSrcAddr_Type(CdsmFcAddrAndMask):
    """Custom type cdsmFCMultiFieldMatchSrcAddr based on CdsmFcAddrAndMask"""
    defaultHexValue = ""


_CdsmFCMultiFieldMatchSrcAddr_Object = MibTableColumn
cdsmFCMultiFieldMatchSrcAddr = _CdsmFCMultiFieldMatchSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 4, 1, 2),
    _CdsmFCMultiFieldMatchSrcAddr_Type()
)
cdsmFCMultiFieldMatchSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmFCMultiFieldMatchSrcAddr.setStatus("current")


class _CdsmFCMultiFieldMatchDstAddr_Type(CdsmFcAddrAndMask):
    """Custom type cdsmFCMultiFieldMatchDstAddr based on CdsmFcAddrAndMask"""
    defaultHexValue = ""


_CdsmFCMultiFieldMatchDstAddr_Object = MibTableColumn
cdsmFCMultiFieldMatchDstAddr = _CdsmFCMultiFieldMatchDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 4, 1, 3),
    _CdsmFCMultiFieldMatchDstAddr_Type()
)
cdsmFCMultiFieldMatchDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmFCMultiFieldMatchDstAddr.setStatus("current")


class _CdsmFCMultiFieldMatchIntf_Type(InterfaceIndexOrZero):
    """Custom type cdsmFCMultiFieldMatchIntf based on InterfaceIndexOrZero"""
    defaultValue = 0


_CdsmFCMultiFieldMatchIntf_Object = MibTableColumn
cdsmFCMultiFieldMatchIntf = _CdsmFCMultiFieldMatchIntf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 4, 1, 4),
    _CdsmFCMultiFieldMatchIntf_Type()
)
cdsmFCMultiFieldMatchIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmFCMultiFieldMatchIntf.setStatus("current")
_CdsmFCMultiFieldMatchStatus_Type = RowStatus
_CdsmFCMultiFieldMatchStatus_Object = MibTableColumn
cdsmFCMultiFieldMatchStatus = _CdsmFCMultiFieldMatchStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 4, 1, 5),
    _CdsmFCMultiFieldMatchStatus_Type()
)
cdsmFCMultiFieldMatchStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmFCMultiFieldMatchStatus.setStatus("current")


class _CdsmFCMultiFieldMatchWildCard_Type(TruthValue):
    """Custom type cdsmFCMultiFieldMatchWildCard based on TruthValue"""


_CdsmFCMultiFieldMatchWildCard_Object = MibTableColumn
cdsmFCMultiFieldMatchWildCard = _CdsmFCMultiFieldMatchWildCard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 4, 1, 6),
    _CdsmFCMultiFieldMatchWildCard_Type()
)
cdsmFCMultiFieldMatchWildCard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmFCMultiFieldMatchWildCard.setStatus("current")
_CdsmRateLimitTable_Object = MibTable
cdsmRateLimitTable = _CdsmRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cdsmRateLimitTable.setStatus("current")
_CdsmRateLimitEntry_Object = MibTableRow
cdsmRateLimitEntry = _CdsmRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 5, 1)
)
cdsmRateLimitEntry.setIndexNames(
    (0, "CISCO-DIFFSERV-EXT-MIB", "cdsmRateLimitId"),
)
if mibBuilder.loadTexts:
    cdsmRateLimitEntry.setStatus("current")
_CdsmRateLimitId_Type = IndexInteger
_CdsmRateLimitId_Object = MibTableColumn
cdsmRateLimitId = _CdsmRateLimitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 5, 1, 1),
    _CdsmRateLimitId_Type()
)
cdsmRateLimitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsmRateLimitId.setStatus("current")


class _CdsmRateLimitPercent_Type(Unsigned32):
    """Custom type cdsmRateLimitPercent based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CdsmRateLimitPercent_Type.__name__ = "Unsigned32"
_CdsmRateLimitPercent_Object = MibTableColumn
cdsmRateLimitPercent = _CdsmRateLimitPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 5, 1, 2),
    _CdsmRateLimitPercent_Type()
)
cdsmRateLimitPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmRateLimitPercent.setStatus("current")
if mibBuilder.loadTexts:
    cdsmRateLimitPercent.setUnits("percent")
_CdsmSchedulerQTable_Object = MibTable
cdsmSchedulerQTable = _CdsmSchedulerQTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cdsmSchedulerQTable.setStatus("current")
_CdsmSchedulerQEntry_Object = MibTableRow
cdsmSchedulerQEntry = _CdsmSchedulerQEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 6, 1)
)
cdsmSchedulerQEntry.setIndexNames(
    (0, "CISCO-DIFFSERV-EXT-MIB", "cdsmSchedulerQNum"),
)
if mibBuilder.loadTexts:
    cdsmSchedulerQEntry.setStatus("current")


class _CdsmSchedulerQNum_Type(Unsigned32):
    """Custom type cdsmSchedulerQNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CdsmSchedulerQNum_Type.__name__ = "Unsigned32"
_CdsmSchedulerQNum_Object = MibTableColumn
cdsmSchedulerQNum = _CdsmSchedulerQNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 6, 1, 1),
    _CdsmSchedulerQNum_Type()
)
cdsmSchedulerQNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsmSchedulerQNum.setStatus("current")


class _CdsmSchedulerQWeight_Type(Unsigned32):
    """Custom type cdsmSchedulerQWeight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 100),
    )


_CdsmSchedulerQWeight_Type.__name__ = "Unsigned32"
_CdsmSchedulerQWeight_Object = MibTableColumn
cdsmSchedulerQWeight = _CdsmSchedulerQWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 6, 1, 2),
    _CdsmSchedulerQWeight_Type()
)
cdsmSchedulerQWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdsmSchedulerQWeight.setStatus("current")
_CdsmChkSumTable_Object = MibTable
cdsmChkSumTable = _CdsmChkSumTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cdsmChkSumTable.setStatus("current")
_CdsmChkSumEntry_Object = MibTableRow
cdsmChkSumEntry = _CdsmChkSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 7, 1)
)
cdsmChkSumEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    cdsmChkSumEntry.setStatus("current")
_CdsmChkSumValue_Type = Unsigned32
_CdsmChkSumValue_Object = MibTableColumn
cdsmChkSumValue = _CdsmChkSumValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 1, 1, 7, 1, 1),
    _CdsmChkSumValue_Type()
)
cdsmChkSumValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmChkSumValue.setStatus("current")
_CiscoDiffServExtMIBConform_ObjectIdentity = ObjectIdentity
ciscoDiffServExtMIBConform = _CiscoDiffServExtMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 2)
)
_CiscoDiffServExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDiffServExtMIBCompliances = _CiscoDiffServExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 2, 1)
)
_CiscoDiffServExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDiffServExtMIBGroups = _CiscoDiffServExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 2, 2)
)
diffServClfrEntry.registerAugmentions(
    ("CISCO-DIFFSERV-EXT-MIB",
     "cdsmClfrEntry")
)
cdsmClfrEntry.setIndexNames(*diffServClfrEntry.getIndexNames())

# Managed Objects groups

ciscoDiffServVsanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 2, 2, 1)
)
ciscoDiffServVsanGroup.setObjects(
      *(("CISCO-DIFFSERV-EXT-MIB", "cdsmDataPathClfrStart"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmDataPathStatus"))
)
if mibBuilder.loadTexts:
    ciscoDiffServVsanGroup.setStatus("current")

ciscoDiffServExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 2, 2, 2)
)
ciscoDiffServExtGroup.setObjects(
      *(("CISCO-DIFFSERV-EXT-MIB", "cdsmClfrName"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldClfrName"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldClfrMatch"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldClfrStatus"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldMatchSrcAddr"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldMatchDstAddr"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldMatchIntf"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldMatchStatus"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmRateLimitPercent"))
)
if mibBuilder.loadTexts:
    ciscoDiffServExtGroup.setStatus("deprecated")

ciscoDiffServSchedQGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 2, 2, 3)
)
ciscoDiffServSchedQGroup.setObjects(
    ("CISCO-DIFFSERV-EXT-MIB", "cdsmSchedulerQWeight")
)
if mibBuilder.loadTexts:
    ciscoDiffServSchedQGroup.setStatus("current")

ciscoDiffServExtGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 2, 2, 4)
)
ciscoDiffServExtGroup1.setObjects(
      *(("CISCO-DIFFSERV-EXT-MIB", "cdsmClfrName"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldClfrName"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldClfrMatch"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldClfrStatus"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldMatchSrcAddr"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldMatchDstAddr"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldMatchIntf"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldMatchStatus"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldMatchWildCard"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmRateLimitPercent"))
)
if mibBuilder.loadTexts:
    ciscoDiffServExtGroup1.setStatus("deprecated")

ciscoDiffServChkSumGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 2, 2, 5)
)
ciscoDiffServChkSumGroup.setObjects(
    ("CISCO-DIFFSERV-EXT-MIB", "cdsmChkSumValue")
)
if mibBuilder.loadTexts:
    ciscoDiffServChkSumGroup.setStatus("current")

ciscoDiffServExtGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 2, 2, 6)
)
ciscoDiffServExtGroup2.setObjects(
      *(("CISCO-DIFFSERV-EXT-MIB", "cdsmClfrName"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmClfrNextFreeElement"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldClfrName"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldClfrMatch"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldClfrStatus"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldClfrNextFreeStmt"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldMatchSrcAddr"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldMatchDstAddr"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldMatchIntf"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldMatchStatus"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmFCMultiFieldMatchWildCard"),
        ("CISCO-DIFFSERV-EXT-MIB", "cdsmRateLimitPercent"))
)
if mibBuilder.loadTexts:
    ciscoDiffServExtGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoDiffServExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDiffServExtMIBCompliance.setStatus(
        "deprecated"
    )

ciscoDiffServExtMIBComplianceR1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoDiffServExtMIBComplianceR1.setStatus(
        "deprecated"
    )

ciscoDiffServExtMIBComplianceR2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 381, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoDiffServExtMIBComplianceR2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DIFFSERV-EXT-MIB",
    **{"CdsmDataDirection": CdsmDataDirection,
       "CdsmFcAddrAndMask": CdsmFcAddrAndMask,
       "ciscoDiffServExtMIB": ciscoDiffServExtMIB,
       "ciscoDiffServExtMIBObjects": ciscoDiffServExtMIBObjects,
       "cdsmConfiguration": cdsmConfiguration,
       "cdsmDataPathTable": cdsmDataPathTable,
       "cdsmDataPathEntry": cdsmDataPathEntry,
       "cdsmDataPathDirection": cdsmDataPathDirection,
       "cdsmDataPathClfrStart": cdsmDataPathClfrStart,
       "cdsmDataPathStatus": cdsmDataPathStatus,
       "cdsmClfrTable": cdsmClfrTable,
       "cdsmClfrEntry": cdsmClfrEntry,
       "cdsmClfrName": cdsmClfrName,
       "cdsmClfrNextFreeElement": cdsmClfrNextFreeElement,
       "cdsmFCMultiFieldClfrTable": cdsmFCMultiFieldClfrTable,
       "cdsmFCMultiFieldClfrEntry": cdsmFCMultiFieldClfrEntry,
       "cdsmFCMultiFieldClfrId": cdsmFCMultiFieldClfrId,
       "cdsmFCMultiFieldClfrName": cdsmFCMultiFieldClfrName,
       "cdsmFCMultiFieldClfrMatch": cdsmFCMultiFieldClfrMatch,
       "cdsmFCMultiFieldClfrStatus": cdsmFCMultiFieldClfrStatus,
       "cdsmFCMultiFieldClfrNextFreeStmt": cdsmFCMultiFieldClfrNextFreeStmt,
       "cdsmFCMultiFieldMatchStmtTable": cdsmFCMultiFieldMatchStmtTable,
       "cdsmFCMultiFieldMatchStmtEntry": cdsmFCMultiFieldMatchStmtEntry,
       "cdsmFCMultiFieldMatchId": cdsmFCMultiFieldMatchId,
       "cdsmFCMultiFieldMatchSrcAddr": cdsmFCMultiFieldMatchSrcAddr,
       "cdsmFCMultiFieldMatchDstAddr": cdsmFCMultiFieldMatchDstAddr,
       "cdsmFCMultiFieldMatchIntf": cdsmFCMultiFieldMatchIntf,
       "cdsmFCMultiFieldMatchStatus": cdsmFCMultiFieldMatchStatus,
       "cdsmFCMultiFieldMatchWildCard": cdsmFCMultiFieldMatchWildCard,
       "cdsmRateLimitTable": cdsmRateLimitTable,
       "cdsmRateLimitEntry": cdsmRateLimitEntry,
       "cdsmRateLimitId": cdsmRateLimitId,
       "cdsmRateLimitPercent": cdsmRateLimitPercent,
       "cdsmSchedulerQTable": cdsmSchedulerQTable,
       "cdsmSchedulerQEntry": cdsmSchedulerQEntry,
       "cdsmSchedulerQNum": cdsmSchedulerQNum,
       "cdsmSchedulerQWeight": cdsmSchedulerQWeight,
       "cdsmChkSumTable": cdsmChkSumTable,
       "cdsmChkSumEntry": cdsmChkSumEntry,
       "cdsmChkSumValue": cdsmChkSumValue,
       "ciscoDiffServExtMIBConform": ciscoDiffServExtMIBConform,
       "ciscoDiffServExtMIBCompliances": ciscoDiffServExtMIBCompliances,
       "ciscoDiffServExtMIBCompliance": ciscoDiffServExtMIBCompliance,
       "ciscoDiffServExtMIBComplianceR1": ciscoDiffServExtMIBComplianceR1,
       "ciscoDiffServExtMIBComplianceR2": ciscoDiffServExtMIBComplianceR2,
       "ciscoDiffServExtMIBGroups": ciscoDiffServExtMIBGroups,
       "ciscoDiffServVsanGroup": ciscoDiffServVsanGroup,
       "ciscoDiffServExtGroup": ciscoDiffServExtGroup,
       "ciscoDiffServSchedQGroup": ciscoDiffServSchedQGroup,
       "ciscoDiffServExtGroup1": ciscoDiffServExtGroup1,
       "ciscoDiffServChkSumGroup": ciscoDiffServChkSumGroup,
       "ciscoDiffServExtGroup2": ciscoDiffServExtGroup2}
)
