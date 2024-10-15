# SNMP MIB module (Unisphere-Data-IP-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-IP-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:17 2024
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")


# MODULE-IDENTITY

usdIpPolicyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13)
)
usdIpPolicyMIB.setRevisions(
        ("2002-01-03 15:06",
         "2000-07-20 00:00",
         "1998-11-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UsdIpPolicyName(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class UsdIpPolicyPolicy(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 0))
    )



class UsdIpRedistributeProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("ipRedistrProtocolAccess", 9),
          ("ipRedistrProtocolAccessInternal", 10),
          ("ipRedistrProtocolBgp", 2),
          ("ipRedistrProtocolConnected", 7),
          ("ipRedistrProtocolDefaultRoute", 8),
          ("ipRedistrProtocolDvmrp", 11),
          ("ipRedistrProtocolIsis", 5),
          ("ipRedistrProtocolMBgp", 3),
          ("ipRedistrProtocolOspf", 4),
          ("ipRedistrProtocolRip", 6),
          ("ipRedistrProtocolStatic", 1))
    )



class UsdIpPolicyAdminStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipPolicyAdminStateDisable", 0),
          ("ipPolicyAdminStateEnable", 1))
    )



class UsdIpPolicyExtendedCommunity(OctetString, TextualConvention):
    status = "current"
    displayHint = "22a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )



# MIB Managed Objects in the order of their OIDs

_UsdIpPolicyObjects_ObjectIdentity = ObjectIdentity
usdIpPolicyObjects = _UsdIpPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1)
)
_UsdIpAccessList_ObjectIdentity = ObjectIdentity
usdIpAccessList = _UsdIpAccessList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 1)
)
_UsdIpAccessListTable_Object = MibTable
usdIpAccessListTable = _UsdIpAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 1, 1)
)
if mibBuilder.loadTexts:
    usdIpAccessListTable.setStatus("current")
_UsdIpAccessListEntry_Object = MibTableRow
usdIpAccessListEntry = _UsdIpAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 1, 1, 1)
)
usdIpAccessListEntry.setIndexNames(
    (0, "Unisphere-Data-IP-POLICY-MIB", "usdIpAccessListId"),
    (0, "Unisphere-Data-IP-POLICY-MIB", "usdIpAccessListElemId"),
)
if mibBuilder.loadTexts:
    usdIpAccessListEntry.setStatus("current")


class _UsdIpAccessListId_Type(Integer32):
    """Custom type usdIpAccessListId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_UsdIpAccessListId_Type.__name__ = "Integer32"
_UsdIpAccessListId_Object = MibTableColumn
usdIpAccessListId = _UsdIpAccessListId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 1, 1, 1, 1),
    _UsdIpAccessListId_Type()
)
usdIpAccessListId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpAccessListId.setStatus("current")


class _UsdIpAccessListElemId_Type(Integer32):
    """Custom type usdIpAccessListElemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_UsdIpAccessListElemId_Type.__name__ = "Integer32"
_UsdIpAccessListElemId_Object = MibTableColumn
usdIpAccessListElemId = _UsdIpAccessListElemId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 1, 1, 1, 2),
    _UsdIpAccessListElemId_Type()
)
usdIpAccessListElemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpAccessListElemId.setStatus("current")
_UsdIpAccessListRowStatus_Type = RowStatus
_UsdIpAccessListRowStatus_Object = MibTableColumn
usdIpAccessListRowStatus = _UsdIpAccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 1, 1, 1, 3),
    _UsdIpAccessListRowStatus_Type()
)
usdIpAccessListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpAccessListRowStatus.setStatus("current")


class _UsdIpAccessListAction_Type(UsdIpPolicyPolicy):
    """Custom type usdIpAccessListAction based on UsdIpPolicyPolicy"""


_UsdIpAccessListAction_Object = MibTableColumn
usdIpAccessListAction = _UsdIpAccessListAction_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 1, 1, 1, 4),
    _UsdIpAccessListAction_Type()
)
usdIpAccessListAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpAccessListAction.setStatus("current")


class _UsdIpAccessListSrc_Type(IpAddress):
    """Custom type usdIpAccessListSrc based on IpAddress"""
    defaultHexValue = "00000000"


_UsdIpAccessListSrc_Object = MibTableColumn
usdIpAccessListSrc = _UsdIpAccessListSrc_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 1, 1, 1, 5),
    _UsdIpAccessListSrc_Type()
)
usdIpAccessListSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpAccessListSrc.setStatus("current")


class _UsdIpAccessListSrcMask_Type(IpAddress):
    """Custom type usdIpAccessListSrcMask based on IpAddress"""
    defaultHexValue = "00000000"


_UsdIpAccessListSrcMask_Object = MibTableColumn
usdIpAccessListSrcMask = _UsdIpAccessListSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 1, 1, 1, 6),
    _UsdIpAccessListSrcMask_Type()
)
usdIpAccessListSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpAccessListSrcMask.setStatus("current")


class _UsdIpAccessListDst_Type(IpAddress):
    """Custom type usdIpAccessListDst based on IpAddress"""
    defaultHexValue = "00000000"


_UsdIpAccessListDst_Object = MibTableColumn
usdIpAccessListDst = _UsdIpAccessListDst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 1, 1, 1, 7),
    _UsdIpAccessListDst_Type()
)
usdIpAccessListDst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpAccessListDst.setStatus("current")


class _UsdIpAccessListDstMask_Type(IpAddress):
    """Custom type usdIpAccessListDstMask based on IpAddress"""
    defaultHexValue = "00000000"


_UsdIpAccessListDstMask_Object = MibTableColumn
usdIpAccessListDstMask = _UsdIpAccessListDstMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 1, 1, 1, 8),
    _UsdIpAccessListDstMask_Type()
)
usdIpAccessListDstMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpAccessListDstMask.setStatus("current")


class _UsdIpAccessListProtocol_Type(Integer32):
    """Custom type usdIpAccessListProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UsdIpAccessListProtocol_Type.__name__ = "Integer32"
_UsdIpAccessListProtocol_Object = MibTableColumn
usdIpAccessListProtocol = _UsdIpAccessListProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 1, 1, 1, 9),
    _UsdIpAccessListProtocol_Type()
)
usdIpAccessListProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpAccessListProtocol.setStatus("current")
_UsdIpNamedAccessList_ObjectIdentity = ObjectIdentity
usdIpNamedAccessList = _UsdIpNamedAccessList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 2)
)
_UsdIpNamedAccessListTable_Object = MibTable
usdIpNamedAccessListTable = _UsdIpNamedAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 2, 1)
)
if mibBuilder.loadTexts:
    usdIpNamedAccessListTable.setStatus("current")
_UsdIpNamedAccessListEntry_Object = MibTableRow
usdIpNamedAccessListEntry = _UsdIpNamedAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 2, 1, 1)
)
usdIpNamedAccessListEntry.setIndexNames(
    (0, "Unisphere-Data-IP-POLICY-MIB", "usdIpNamedAccessListName"),
    (0, "Unisphere-Data-IP-POLICY-MIB", "usdIpNamedAccessListElemId"),
)
if mibBuilder.loadTexts:
    usdIpNamedAccessListEntry.setStatus("current")
_UsdIpNamedAccessListName_Type = UsdIpPolicyName
_UsdIpNamedAccessListName_Object = MibTableColumn
usdIpNamedAccessListName = _UsdIpNamedAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 2, 1, 1, 1),
    _UsdIpNamedAccessListName_Type()
)
usdIpNamedAccessListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpNamedAccessListName.setStatus("current")


class _UsdIpNamedAccessListElemId_Type(Integer32):
    """Custom type usdIpNamedAccessListElemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_UsdIpNamedAccessListElemId_Type.__name__ = "Integer32"
_UsdIpNamedAccessListElemId_Object = MibTableColumn
usdIpNamedAccessListElemId = _UsdIpNamedAccessListElemId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 2, 1, 1, 2),
    _UsdIpNamedAccessListElemId_Type()
)
usdIpNamedAccessListElemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpNamedAccessListElemId.setStatus("current")
_UsdIpNamedAccessListRowStatus_Type = RowStatus
_UsdIpNamedAccessListRowStatus_Object = MibTableColumn
usdIpNamedAccessListRowStatus = _UsdIpNamedAccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 2, 1, 1, 3),
    _UsdIpNamedAccessListRowStatus_Type()
)
usdIpNamedAccessListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpNamedAccessListRowStatus.setStatus("current")


class _UsdIpNamedAccessListAction_Type(UsdIpPolicyPolicy):
    """Custom type usdIpNamedAccessListAction based on UsdIpPolicyPolicy"""


_UsdIpNamedAccessListAction_Object = MibTableColumn
usdIpNamedAccessListAction = _UsdIpNamedAccessListAction_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 2, 1, 1, 4),
    _UsdIpNamedAccessListAction_Type()
)
usdIpNamedAccessListAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpNamedAccessListAction.setStatus("current")


class _UsdIpNamedAccessListSrc_Type(IpAddress):
    """Custom type usdIpNamedAccessListSrc based on IpAddress"""
    defaultHexValue = "00000000"


_UsdIpNamedAccessListSrc_Object = MibTableColumn
usdIpNamedAccessListSrc = _UsdIpNamedAccessListSrc_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 2, 1, 1, 5),
    _UsdIpNamedAccessListSrc_Type()
)
usdIpNamedAccessListSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpNamedAccessListSrc.setStatus("current")


class _UsdIpNamedAccessListSrcMask_Type(IpAddress):
    """Custom type usdIpNamedAccessListSrcMask based on IpAddress"""
    defaultHexValue = "00000000"


_UsdIpNamedAccessListSrcMask_Object = MibTableColumn
usdIpNamedAccessListSrcMask = _UsdIpNamedAccessListSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 2, 1, 1, 6),
    _UsdIpNamedAccessListSrcMask_Type()
)
usdIpNamedAccessListSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpNamedAccessListSrcMask.setStatus("current")


class _UsdIpNamedAccessListDst_Type(IpAddress):
    """Custom type usdIpNamedAccessListDst based on IpAddress"""
    defaultHexValue = "00000000"


_UsdIpNamedAccessListDst_Object = MibTableColumn
usdIpNamedAccessListDst = _UsdIpNamedAccessListDst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 2, 1, 1, 7),
    _UsdIpNamedAccessListDst_Type()
)
usdIpNamedAccessListDst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpNamedAccessListDst.setStatus("current")


class _UsdIpNamedAccessListDstMask_Type(IpAddress):
    """Custom type usdIpNamedAccessListDstMask based on IpAddress"""
    defaultHexValue = "00000000"


_UsdIpNamedAccessListDstMask_Object = MibTableColumn
usdIpNamedAccessListDstMask = _UsdIpNamedAccessListDstMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 2, 1, 1, 8),
    _UsdIpNamedAccessListDstMask_Type()
)
usdIpNamedAccessListDstMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpNamedAccessListDstMask.setStatus("current")


class _UsdIpNamedAccessListProtocol_Type(Integer32):
    """Custom type usdIpNamedAccessListProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UsdIpNamedAccessListProtocol_Type.__name__ = "Integer32"
_UsdIpNamedAccessListProtocol_Object = MibTableColumn
usdIpNamedAccessListProtocol = _UsdIpNamedAccessListProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 2, 1, 1, 9),
    _UsdIpNamedAccessListProtocol_Type()
)
usdIpNamedAccessListProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpNamedAccessListProtocol.setStatus("current")
_UsdIpAspAccessList_ObjectIdentity = ObjectIdentity
usdIpAspAccessList = _UsdIpAspAccessList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 3)
)
_UsdIpAspAccessTable_Object = MibTable
usdIpAspAccessTable = _UsdIpAspAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 3, 1)
)
if mibBuilder.loadTexts:
    usdIpAspAccessTable.setStatus("current")
_UsdIpAspAccessEntry_Object = MibTableRow
usdIpAspAccessEntry = _UsdIpAspAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 3, 1, 1)
)
usdIpAspAccessEntry.setIndexNames(
    (0, "Unisphere-Data-IP-POLICY-MIB", "usdIpAspAccessName"),
    (0, "Unisphere-Data-IP-POLICY-MIB", "usdIpAspAccessElemId"),
)
if mibBuilder.loadTexts:
    usdIpAspAccessEntry.setStatus("current")
_UsdIpAspAccessName_Type = UsdIpPolicyName
_UsdIpAspAccessName_Object = MibTableColumn
usdIpAspAccessName = _UsdIpAspAccessName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 3, 1, 1, 1),
    _UsdIpAspAccessName_Type()
)
usdIpAspAccessName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpAspAccessName.setStatus("current")


class _UsdIpAspAccessElemId_Type(Integer32):
    """Custom type usdIpAspAccessElemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_UsdIpAspAccessElemId_Type.__name__ = "Integer32"
_UsdIpAspAccessElemId_Object = MibTableColumn
usdIpAspAccessElemId = _UsdIpAspAccessElemId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 3, 1, 1, 2),
    _UsdIpAspAccessElemId_Type()
)
usdIpAspAccessElemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpAspAccessElemId.setStatus("current")
_UsdIpAspAccessCreatedInternally_Type = TruthValue
_UsdIpAspAccessCreatedInternally_Object = MibTableColumn
usdIpAspAccessCreatedInternally = _UsdIpAspAccessCreatedInternally_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 3, 1, 1, 3),
    _UsdIpAspAccessCreatedInternally_Type()
)
usdIpAspAccessCreatedInternally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpAspAccessCreatedInternally.setStatus("current")
_UsdIpAspAccessPolicy_Type = UsdIpPolicyPolicy
_UsdIpAspAccessPolicy_Object = MibTableColumn
usdIpAspAccessPolicy = _UsdIpAspAccessPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 3, 1, 1, 4),
    _UsdIpAspAccessPolicy_Type()
)
usdIpAspAccessPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpAspAccessPolicy.setStatus("current")


class _UsdIpAspAccessExpression_Type(OctetString):
    """Custom type usdIpAspAccessExpression based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 64),
    )


_UsdIpAspAccessExpression_Type.__name__ = "OctetString"
_UsdIpAspAccessExpression_Object = MibTableColumn
usdIpAspAccessExpression = _UsdIpAspAccessExpression_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 3, 1, 1, 5),
    _UsdIpAspAccessExpression_Type()
)
usdIpAspAccessExpression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpAspAccessExpression.setStatus("current")
_UsdIpAspAccessRowStatus_Type = RowStatus
_UsdIpAspAccessRowStatus_Object = MibTableColumn
usdIpAspAccessRowStatus = _UsdIpAspAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 3, 1, 1, 6),
    _UsdIpAspAccessRowStatus_Type()
)
usdIpAspAccessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpAspAccessRowStatus.setStatus("current")
_UsdIpPrefixList_ObjectIdentity = ObjectIdentity
usdIpPrefixList = _UsdIpPrefixList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 4)
)
_UsdIpPrefixListTable_Object = MibTable
usdIpPrefixListTable = _UsdIpPrefixListTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 4, 1)
)
if mibBuilder.loadTexts:
    usdIpPrefixListTable.setStatus("current")
_UsdIpPrefixListEntry_Object = MibTableRow
usdIpPrefixListEntry = _UsdIpPrefixListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 4, 1, 1)
)
usdIpPrefixListEntry.setIndexNames(
    (0, "Unisphere-Data-IP-POLICY-MIB", "usdIpPrefixListName"),
    (0, "Unisphere-Data-IP-POLICY-MIB", "usdIpPrefixListElemId"),
    (0, "Unisphere-Data-IP-POLICY-MIB", "usdIpPrefixListIpAddress"),
    (0, "Unisphere-Data-IP-POLICY-MIB", "usdIpPrefixListLength"),
)
if mibBuilder.loadTexts:
    usdIpPrefixListEntry.setStatus("current")
_UsdIpPrefixListName_Type = UsdIpPolicyName
_UsdIpPrefixListName_Object = MibTableColumn
usdIpPrefixListName = _UsdIpPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 4, 1, 1, 1),
    _UsdIpPrefixListName_Type()
)
usdIpPrefixListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpPrefixListName.setStatus("current")


class _UsdIpPrefixListElemId_Type(Integer32):
    """Custom type usdIpPrefixListElemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_UsdIpPrefixListElemId_Type.__name__ = "Integer32"
_UsdIpPrefixListElemId_Object = MibTableColumn
usdIpPrefixListElemId = _UsdIpPrefixListElemId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 4, 1, 1, 2),
    _UsdIpPrefixListElemId_Type()
)
usdIpPrefixListElemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpPrefixListElemId.setStatus("current")
_UsdIpPrefixListIpAddress_Type = IpAddress
_UsdIpPrefixListIpAddress_Object = MibTableColumn
usdIpPrefixListIpAddress = _UsdIpPrefixListIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 4, 1, 1, 3),
    _UsdIpPrefixListIpAddress_Type()
)
usdIpPrefixListIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpPrefixListIpAddress.setStatus("current")


class _UsdIpPrefixListLength_Type(Integer32):
    """Custom type usdIpPrefixListLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_UsdIpPrefixListLength_Type.__name__ = "Integer32"
_UsdIpPrefixListLength_Object = MibTableColumn
usdIpPrefixListLength = _UsdIpPrefixListLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 4, 1, 1, 4),
    _UsdIpPrefixListLength_Type()
)
usdIpPrefixListLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpPrefixListLength.setStatus("current")
_UsdIpPrefixListPolicy_Type = UsdIpPolicyPolicy
_UsdIpPrefixListPolicy_Object = MibTableColumn
usdIpPrefixListPolicy = _UsdIpPrefixListPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 4, 1, 1, 5),
    _UsdIpPrefixListPolicy_Type()
)
usdIpPrefixListPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpPrefixListPolicy.setStatus("current")


class _UsdIpPrefixListGeValue_Type(Integer32):
    """Custom type usdIpPrefixListGeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_UsdIpPrefixListGeValue_Type.__name__ = "Integer32"
_UsdIpPrefixListGeValue_Object = MibTableColumn
usdIpPrefixListGeValue = _UsdIpPrefixListGeValue_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 4, 1, 1, 6),
    _UsdIpPrefixListGeValue_Type()
)
usdIpPrefixListGeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpPrefixListGeValue.setStatus("current")


class _UsdIpPrefixListLeValue_Type(Integer32):
    """Custom type usdIpPrefixListLeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_UsdIpPrefixListLeValue_Type.__name__ = "Integer32"
_UsdIpPrefixListLeValue_Object = MibTableColumn
usdIpPrefixListLeValue = _UsdIpPrefixListLeValue_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 4, 1, 1, 7),
    _UsdIpPrefixListLeValue_Type()
)
usdIpPrefixListLeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpPrefixListLeValue.setStatus("current")
_UsdIpPrefixListDescription_Type = DisplayString
_UsdIpPrefixListDescription_Object = MibTableColumn
usdIpPrefixListDescription = _UsdIpPrefixListDescription_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 4, 1, 1, 8),
    _UsdIpPrefixListDescription_Type()
)
usdIpPrefixListDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpPrefixListDescription.setStatus("current")
_UsdIpPrefixListHitCount_Type = Counter32
_UsdIpPrefixListHitCount_Object = MibTableColumn
usdIpPrefixListHitCount = _UsdIpPrefixListHitCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 4, 1, 1, 9),
    _UsdIpPrefixListHitCount_Type()
)
usdIpPrefixListHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpPrefixListHitCount.setStatus("current")
_UsdIpPrefixListRowStatus_Type = RowStatus
_UsdIpPrefixListRowStatus_Object = MibTableColumn
usdIpPrefixListRowStatus = _UsdIpPrefixListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 4, 1, 1, 10),
    _UsdIpPrefixListRowStatus_Type()
)
usdIpPrefixListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpPrefixListRowStatus.setStatus("current")
_UsdIpPrefixTree_ObjectIdentity = ObjectIdentity
usdIpPrefixTree = _UsdIpPrefixTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 5)
)
_UsdIpPrefixTreeTable_Object = MibTable
usdIpPrefixTreeTable = _UsdIpPrefixTreeTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 5, 1)
)
if mibBuilder.loadTexts:
    usdIpPrefixTreeTable.setStatus("current")
_UsdIpPrefixTreeEntry_Object = MibTableRow
usdIpPrefixTreeEntry = _UsdIpPrefixTreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 5, 1, 1)
)
usdIpPrefixTreeEntry.setIndexNames(
    (0, "Unisphere-Data-IP-POLICY-MIB", "usdIpPrefixTreeName"),
    (0, "Unisphere-Data-IP-POLICY-MIB", "usdIpPrefixTreeIpAddress"),
    (0, "Unisphere-Data-IP-POLICY-MIB", "usdIpPrefixTreeLength"),
)
if mibBuilder.loadTexts:
    usdIpPrefixTreeEntry.setStatus("current")
_UsdIpPrefixTreeName_Type = UsdIpPolicyName
_UsdIpPrefixTreeName_Object = MibTableColumn
usdIpPrefixTreeName = _UsdIpPrefixTreeName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 5, 1, 1, 1),
    _UsdIpPrefixTreeName_Type()
)
usdIpPrefixTreeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpPrefixTreeName.setStatus("current")
_UsdIpPrefixTreeIpAddress_Type = IpAddress
_UsdIpPrefixTreeIpAddress_Object = MibTableColumn
usdIpPrefixTreeIpAddress = _UsdIpPrefixTreeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 5, 1, 1, 2),
    _UsdIpPrefixTreeIpAddress_Type()
)
usdIpPrefixTreeIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpPrefixTreeIpAddress.setStatus("current")


class _UsdIpPrefixTreeLength_Type(Integer32):
    """Custom type usdIpPrefixTreeLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_UsdIpPrefixTreeLength_Type.__name__ = "Integer32"
_UsdIpPrefixTreeLength_Object = MibTableColumn
usdIpPrefixTreeLength = _UsdIpPrefixTreeLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 5, 1, 1, 3),
    _UsdIpPrefixTreeLength_Type()
)
usdIpPrefixTreeLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpPrefixTreeLength.setStatus("current")
_UsdIpPrefixTreePolicy_Type = UsdIpPolicyPolicy
_UsdIpPrefixTreePolicy_Object = MibTableColumn
usdIpPrefixTreePolicy = _UsdIpPrefixTreePolicy_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 5, 1, 1, 4),
    _UsdIpPrefixTreePolicy_Type()
)
usdIpPrefixTreePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpPrefixTreePolicy.setStatus("current")
_UsdIpPrefixTreeDescription_Type = DisplayString
_UsdIpPrefixTreeDescription_Object = MibTableColumn
usdIpPrefixTreeDescription = _UsdIpPrefixTreeDescription_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 5, 1, 1, 5),
    _UsdIpPrefixTreeDescription_Type()
)
usdIpPrefixTreeDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpPrefixTreeDescription.setStatus("current")
_UsdIpPrefixTreeHitCount_Type = Counter32
_UsdIpPrefixTreeHitCount_Object = MibTableColumn
usdIpPrefixTreeHitCount = _UsdIpPrefixTreeHitCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 5, 1, 1, 6),
    _UsdIpPrefixTreeHitCount_Type()
)
usdIpPrefixTreeHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpPrefixTreeHitCount.setStatus("current")
_UsdIpPrefixTreeRowStatus_Type = RowStatus
_UsdIpPrefixTreeRowStatus_Object = MibTableColumn
usdIpPrefixTreeRowStatus = _UsdIpPrefixTreeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 5, 1, 1, 7),
    _UsdIpPrefixTreeRowStatus_Type()
)
usdIpPrefixTreeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpPrefixTreeRowStatus.setStatus("current")
_UsdIpCommunityList_ObjectIdentity = ObjectIdentity
usdIpCommunityList = _UsdIpCommunityList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6)
)
_UsdIpCommunityListTable_Object = MibTable
usdIpCommunityListTable = _UsdIpCommunityListTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 1)
)
if mibBuilder.loadTexts:
    usdIpCommunityListTable.setStatus("current")
_UsdIpCommunityListEntry_Object = MibTableRow
usdIpCommunityListEntry = _UsdIpCommunityListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 1, 1)
)
usdIpCommunityListEntry.setIndexNames(
    (0, "Unisphere-Data-IP-POLICY-MIB", "usdIpCommunityListName"),
    (0, "Unisphere-Data-IP-POLICY-MIB", "usdIpCommunityListElemId"),
)
if mibBuilder.loadTexts:
    usdIpCommunityListEntry.setStatus("current")
_UsdIpCommunityListName_Type = UsdIpPolicyName
_UsdIpCommunityListName_Object = MibTableColumn
usdIpCommunityListName = _UsdIpCommunityListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 1, 1, 1),
    _UsdIpCommunityListName_Type()
)
usdIpCommunityListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpCommunityListName.setStatus("current")


class _UsdIpCommunityListElemId_Type(Integer32):
    """Custom type usdIpCommunityListElemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_UsdIpCommunityListElemId_Type.__name__ = "Integer32"
_UsdIpCommunityListElemId_Object = MibTableColumn
usdIpCommunityListElemId = _UsdIpCommunityListElemId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 1, 1, 2),
    _UsdIpCommunityListElemId_Type()
)
usdIpCommunityListElemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpCommunityListElemId.setStatus("current")
_UsdIpCommunityListCreatedInternally_Type = TruthValue
_UsdIpCommunityListCreatedInternally_Object = MibTableColumn
usdIpCommunityListCreatedInternally = _UsdIpCommunityListCreatedInternally_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 1, 1, 3),
    _UsdIpCommunityListCreatedInternally_Type()
)
usdIpCommunityListCreatedInternally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpCommunityListCreatedInternally.setStatus("current")
_UsdIpCommunityListExtended_Type = TruthValue
_UsdIpCommunityListExtended_Object = MibTableColumn
usdIpCommunityListExtended = _UsdIpCommunityListExtended_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 1, 1, 4),
    _UsdIpCommunityListExtended_Type()
)
usdIpCommunityListExtended.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpCommunityListExtended.setStatus("current")
_UsdIpCommunityListPolicy_Type = UsdIpPolicyPolicy
_UsdIpCommunityListPolicy_Object = MibTableColumn
usdIpCommunityListPolicy = _UsdIpCommunityListPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 1, 1, 5),
    _UsdIpCommunityListPolicy_Type()
)
usdIpCommunityListPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpCommunityListPolicy.setStatus("current")


class _UsdIpCommunityListExpression_Type(OctetString):
    """Custom type usdIpCommunityListExpression based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 32),
    )


_UsdIpCommunityListExpression_Type.__name__ = "OctetString"
_UsdIpCommunityListExpression_Object = MibTableColumn
usdIpCommunityListExpression = _UsdIpCommunityListExpression_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 1, 1, 6),
    _UsdIpCommunityListExpression_Type()
)
usdIpCommunityListExpression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpCommunityListExpression.setStatus("current")
_UsdIpCommunityListRowStatus_Type = RowStatus
_UsdIpCommunityListRowStatus_Object = MibTableColumn
usdIpCommunityListRowStatus = _UsdIpCommunityListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 1, 1, 7),
    _UsdIpCommunityListRowStatus_Type()
)
usdIpCommunityListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpCommunityListRowStatus.setStatus("current")
_UsdIpExtCommunityListTable_Object = MibTable
usdIpExtCommunityListTable = _UsdIpExtCommunityListTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 2)
)
if mibBuilder.loadTexts:
    usdIpExtCommunityListTable.setStatus("current")
_UsdIpExtCommunityListEntry_Object = MibTableRow
usdIpExtCommunityListEntry = _UsdIpExtCommunityListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 2, 1)
)
usdIpExtCommunityListEntry.setIndexNames(
    (0, "Unisphere-Data-IP-POLICY-MIB", "usdIpExtCommunityListName"),
    (0, "Unisphere-Data-IP-POLICY-MIB", "usdIpExtCommunityListElemId"),
)
if mibBuilder.loadTexts:
    usdIpExtCommunityListEntry.setStatus("current")
_UsdIpExtCommunityListName_Type = UsdIpPolicyName
_UsdIpExtCommunityListName_Object = MibTableColumn
usdIpExtCommunityListName = _UsdIpExtCommunityListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 2, 1, 1),
    _UsdIpExtCommunityListName_Type()
)
usdIpExtCommunityListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpExtCommunityListName.setStatus("current")


class _UsdIpExtCommunityListElemId_Type(Integer32):
    """Custom type usdIpExtCommunityListElemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_UsdIpExtCommunityListElemId_Type.__name__ = "Integer32"
_UsdIpExtCommunityListElemId_Object = MibTableColumn
usdIpExtCommunityListElemId = _UsdIpExtCommunityListElemId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 2, 1, 2),
    _UsdIpExtCommunityListElemId_Type()
)
usdIpExtCommunityListElemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpExtCommunityListElemId.setStatus("current")
_UsdIpExtCommunityListCreatedInternally_Type = TruthValue
_UsdIpExtCommunityListCreatedInternally_Object = MibTableColumn
usdIpExtCommunityListCreatedInternally = _UsdIpExtCommunityListCreatedInternally_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 2, 1, 3),
    _UsdIpExtCommunityListCreatedInternally_Type()
)
usdIpExtCommunityListCreatedInternally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpExtCommunityListCreatedInternally.setStatus("current")
_UsdIpExtCommunityListPolicy_Type = UsdIpPolicyPolicy
_UsdIpExtCommunityListPolicy_Object = MibTableColumn
usdIpExtCommunityListPolicy = _UsdIpExtCommunityListPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 2, 1, 4),
    _UsdIpExtCommunityListPolicy_Type()
)
usdIpExtCommunityListPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpExtCommunityListPolicy.setStatus("current")


class _UsdIpExtCommunityListExpression_Type(OctetString):
    """Custom type usdIpExtCommunityListExpression based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 256),
    )


_UsdIpExtCommunityListExpression_Type.__name__ = "OctetString"
_UsdIpExtCommunityListExpression_Object = MibTableColumn
usdIpExtCommunityListExpression = _UsdIpExtCommunityListExpression_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 2, 1, 5),
    _UsdIpExtCommunityListExpression_Type()
)
usdIpExtCommunityListExpression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpExtCommunityListExpression.setStatus("current")
_UsdIpExtCommunityListRowStatus_Type = RowStatus
_UsdIpExtCommunityListRowStatus_Object = MibTableColumn
usdIpExtCommunityListRowStatus = _UsdIpExtCommunityListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 2, 1, 6),
    _UsdIpExtCommunityListRowStatus_Type()
)
usdIpExtCommunityListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpExtCommunityListRowStatus.setStatus("current")
_UsdIpRedistributeList_ObjectIdentity = ObjectIdentity
usdIpRedistributeList = _UsdIpRedistributeList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 7)
)
_UsdIpDynRedistributeTable_Object = MibTable
usdIpDynRedistributeTable = _UsdIpDynRedistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 7, 1)
)
if mibBuilder.loadTexts:
    usdIpDynRedistributeTable.setStatus("current")
_UsdIpDynRedistributeEntry_Object = MibTableRow
usdIpDynRedistributeEntry = _UsdIpDynRedistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 7, 1, 1)
)
usdIpDynRedistributeEntry.setIndexNames(
    (0, "Unisphere-Data-IP-POLICY-MIB", "usdIpDynRedistributeToProtocol"),
)
if mibBuilder.loadTexts:
    usdIpDynRedistributeEntry.setStatus("current")
_UsdIpDynRedistributeToProtocol_Type = UsdIpRedistributeProtocol
_UsdIpDynRedistributeToProtocol_Object = MibTableColumn
usdIpDynRedistributeToProtocol = _UsdIpDynRedistributeToProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 7, 1, 1, 1),
    _UsdIpDynRedistributeToProtocol_Type()
)
usdIpDynRedistributeToProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpDynRedistributeToProtocol.setStatus("current")


class _UsdIpDynRedistributeState_Type(UsdIpPolicyAdminStatus):
    """Custom type usdIpDynRedistributeState based on UsdIpPolicyAdminStatus"""


_UsdIpDynRedistributeState_Object = MibTableColumn
usdIpDynRedistributeState = _UsdIpDynRedistributeState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 7, 1, 1, 2),
    _UsdIpDynRedistributeState_Type()
)
usdIpDynRedistributeState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpDynRedistributeState.setStatus("current")
_UsdIpDynRedistributeRowStatus_Type = RowStatus
_UsdIpDynRedistributeRowStatus_Object = MibTableColumn
usdIpDynRedistributeRowStatus = _UsdIpDynRedistributeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 7, 1, 1, 3),
    _UsdIpDynRedistributeRowStatus_Type()
)
usdIpDynRedistributeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpDynRedistributeRowStatus.setStatus("current")
_UsdIpRedistributeTable_Object = MibTable
usdIpRedistributeTable = _UsdIpRedistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 7, 2)
)
if mibBuilder.loadTexts:
    usdIpRedistributeTable.setStatus("current")
_UsdIpRedistributeEntry_Object = MibTableRow
usdIpRedistributeEntry = _UsdIpRedistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 7, 2, 1)
)
usdIpRedistributeEntry.setIndexNames(
    (0, "Unisphere-Data-IP-POLICY-MIB", "usdIpRedistributeToProtocol"),
    (0, "Unisphere-Data-IP-POLICY-MIB", "usdIpRedistributeFromProtocol"),
)
if mibBuilder.loadTexts:
    usdIpRedistributeEntry.setStatus("current")
_UsdIpRedistributeToProtocol_Type = UsdIpRedistributeProtocol
_UsdIpRedistributeToProtocol_Object = MibTableColumn
usdIpRedistributeToProtocol = _UsdIpRedistributeToProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 7, 2, 1, 1),
    _UsdIpRedistributeToProtocol_Type()
)
usdIpRedistributeToProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpRedistributeToProtocol.setStatus("current")
_UsdIpRedistributeFromProtocol_Type = UsdIpRedistributeProtocol
_UsdIpRedistributeFromProtocol_Object = MibTableColumn
usdIpRedistributeFromProtocol = _UsdIpRedistributeFromProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 7, 2, 1, 2),
    _UsdIpRedistributeFromProtocol_Type()
)
usdIpRedistributeFromProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpRedistributeFromProtocol.setStatus("current")


class _UsdIpRedistributeState_Type(UsdIpPolicyAdminStatus):
    """Custom type usdIpRedistributeState based on UsdIpPolicyAdminStatus"""


_UsdIpRedistributeState_Object = MibTableColumn
usdIpRedistributeState = _UsdIpRedistributeState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 7, 2, 1, 3),
    _UsdIpRedistributeState_Type()
)
usdIpRedistributeState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpRedistributeState.setStatus("current")
_UsdIpRedistributeRouteMapName_Type = UsdIpPolicyName
_UsdIpRedistributeRouteMapName_Object = MibTableColumn
usdIpRedistributeRouteMapName = _UsdIpRedistributeRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 7, 2, 1, 4),
    _UsdIpRedistributeRouteMapName_Type()
)
usdIpRedistributeRouteMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpRedistributeRouteMapName.setStatus("current")
_UsdIpRedistributeRowStatus_Type = RowStatus
_UsdIpRedistributeRowStatus_Object = MibTableColumn
usdIpRedistributeRowStatus = _UsdIpRedistributeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 7, 2, 1, 5),
    _UsdIpRedistributeRowStatus_Type()
)
usdIpRedistributeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdIpRedistributeRowStatus.setStatus("current")
_UsdIpRouteMapTree_ObjectIdentity = ObjectIdentity
usdIpRouteMapTree = _UsdIpRouteMapTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8)
)
_UsdIpRouteMapTable_Object = MibTable
usdIpRouteMapTable = _UsdIpRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 1)
)
if mibBuilder.loadTexts:
    usdIpRouteMapTable.setStatus("current")
_UsdIpRouteMapEntry_Object = MibTableRow
usdIpRouteMapEntry = _UsdIpRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 1, 1)
)
usdIpRouteMapEntry.setIndexNames(
    (0, "Unisphere-Data-IP-POLICY-MIB", "usdIpRouteMapName"),
    (0, "Unisphere-Data-IP-POLICY-MIB", "usdIpRouteMapSequenceNum"),
    (0, "Unisphere-Data-IP-POLICY-MIB", "usdIpRouteMapElemId"),
    (0, "Unisphere-Data-IP-POLICY-MIB", "usdIpRouteMapSubElemId"),
)
if mibBuilder.loadTexts:
    usdIpRouteMapEntry.setStatus("current")
_UsdIpRouteMapName_Type = UsdIpPolicyName
_UsdIpRouteMapName_Object = MibTableColumn
usdIpRouteMapName = _UsdIpRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 1, 1, 1),
    _UsdIpRouteMapName_Type()
)
usdIpRouteMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpRouteMapName.setStatus("current")


class _UsdIpRouteMapSequenceNum_Type(Integer32):
    """Custom type usdIpRouteMapSequenceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdIpRouteMapSequenceNum_Type.__name__ = "Integer32"
_UsdIpRouteMapSequenceNum_Object = MibTableColumn
usdIpRouteMapSequenceNum = _UsdIpRouteMapSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 1, 1, 2),
    _UsdIpRouteMapSequenceNum_Type()
)
usdIpRouteMapSequenceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpRouteMapSequenceNum.setStatus("current")


class _UsdIpRouteMapElemId_Type(Integer32):
    """Custom type usdIpRouteMapElemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdIpRouteMapElemId_Type.__name__ = "Integer32"
_UsdIpRouteMapElemId_Object = MibTableColumn
usdIpRouteMapElemId = _UsdIpRouteMapElemId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 1, 1, 3),
    _UsdIpRouteMapElemId_Type()
)
usdIpRouteMapElemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpRouteMapElemId.setStatus("current")


class _UsdIpRouteMapSubElemId_Type(Integer32):
    """Custom type usdIpRouteMapSubElemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdIpRouteMapSubElemId_Type.__name__ = "Integer32"
_UsdIpRouteMapSubElemId_Object = MibTableColumn
usdIpRouteMapSubElemId = _UsdIpRouteMapSubElemId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 1, 1, 4),
    _UsdIpRouteMapSubElemId_Type()
)
usdIpRouteMapSubElemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdIpRouteMapSubElemId.setStatus("current")
_UsdIpRouteMapCreatedInternally_Type = TruthValue
_UsdIpRouteMapCreatedInternally_Object = MibTableColumn
usdIpRouteMapCreatedInternally = _UsdIpRouteMapCreatedInternally_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 1, 1, 5),
    _UsdIpRouteMapCreatedInternally_Type()
)
usdIpRouteMapCreatedInternally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpRouteMapCreatedInternally.setStatus("current")
_UsdIpRouteMapPolicy_Type = UsdIpPolicyPolicy
_UsdIpRouteMapPolicy_Object = MibTableColumn
usdIpRouteMapPolicy = _UsdIpRouteMapPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 1, 1, 6),
    _UsdIpRouteMapPolicy_Type()
)
usdIpRouteMapPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpRouteMapPolicy.setStatus("current")


class _UsdIpRouteMapDisplay_Type(OctetString):
    """Custom type usdIpRouteMapDisplay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_UsdIpRouteMapDisplay_Type.__name__ = "OctetString"
_UsdIpRouteMapDisplay_Object = MibTableColumn
usdIpRouteMapDisplay = _UsdIpRouteMapDisplay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 1, 1, 7),
    _UsdIpRouteMapDisplay_Type()
)
usdIpRouteMapDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIpRouteMapDisplay.setStatus("current")
_UsdIpPolicyConformance_ObjectIdentity = ObjectIdentity
usdIpPolicyConformance = _UsdIpPolicyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4)
)
_UsdIpPolicyCompliances_ObjectIdentity = ObjectIdentity
usdIpPolicyCompliances = _UsdIpPolicyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 1)
)
_UsdIpPolicyGroups_ObjectIdentity = ObjectIdentity
usdIpPolicyGroups = _UsdIpPolicyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 2)
)

# Managed Objects groups

usdIpAccessListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 2, 1)
)
usdIpAccessListGroup.setObjects(
      *(("Unisphere-Data-IP-POLICY-MIB", "usdIpAccessListRowStatus"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpAccessListAction"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpAccessListSrc"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpAccessListSrcMask"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpAccessListDst"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpAccessListDstMask"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpAccessListProtocol"))
)
if mibBuilder.loadTexts:
    usdIpAccessListGroup.setStatus("current")

usdIpNamedAccessListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 2, 2)
)
usdIpNamedAccessListGroup.setObjects(
      *(("Unisphere-Data-IP-POLICY-MIB", "usdIpNamedAccessListRowStatus"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpNamedAccessListAction"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpNamedAccessListSrc"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpNamedAccessListSrcMask"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpNamedAccessListDst"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpNamedAccessListDstMask"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpNamedAccessListProtocol"))
)
if mibBuilder.loadTexts:
    usdIpNamedAccessListGroup.setStatus("current")

usdIpAspAccessListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 2, 3)
)
usdIpAspAccessListGroup.setObjects(
      *(("Unisphere-Data-IP-POLICY-MIB", "usdIpAspAccessCreatedInternally"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpAspAccessPolicy"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpAspAccessExpression"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpAspAccessRowStatus"))
)
if mibBuilder.loadTexts:
    usdIpAspAccessListGroup.setStatus("current")

usdIpPrefixListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 2, 4)
)
usdIpPrefixListGroup.setObjects(
      *(("Unisphere-Data-IP-POLICY-MIB", "usdIpPrefixListPolicy"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpPrefixListGeValue"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpPrefixListLeValue"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpPrefixListDescription"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpPrefixListHitCount"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpPrefixListRowStatus"))
)
if mibBuilder.loadTexts:
    usdIpPrefixListGroup.setStatus("current")

usdIpPrefixTreeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 2, 5)
)
usdIpPrefixTreeGroup.setObjects(
      *(("Unisphere-Data-IP-POLICY-MIB", "usdIpPrefixTreePolicy"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpPrefixTreeDescription"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpPrefixTreeHitCount"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpPrefixTreeRowStatus"))
)
if mibBuilder.loadTexts:
    usdIpPrefixTreeGroup.setStatus("current")

usdIpCommunityListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 2, 6)
)
usdIpCommunityListGroup.setObjects(
      *(("Unisphere-Data-IP-POLICY-MIB", "usdIpCommunityListCreatedInternally"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpCommunityListExtended"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpCommunityListPolicy"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpCommunityListExpression"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpCommunityListRowStatus"))
)
if mibBuilder.loadTexts:
    usdIpCommunityListGroup.setStatus("current")

usdIpExtCommunityListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 2, 7)
)
usdIpExtCommunityListGroup.setObjects(
      *(("Unisphere-Data-IP-POLICY-MIB", "usdIpExtCommunityListCreatedInternally"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpExtCommunityListPolicy"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpExtCommunityListExpression"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpExtCommunityListRowStatus"))
)
if mibBuilder.loadTexts:
    usdIpExtCommunityListGroup.setStatus("current")

usdIpRedistributeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 2, 8)
)
usdIpRedistributeGroup.setObjects(
      *(("Unisphere-Data-IP-POLICY-MIB", "usdIpDynRedistributeState"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpDynRedistributeRowStatus"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpRedistributeState"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpRedistributeRouteMapName"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpRedistributeRowStatus"))
)
if mibBuilder.loadTexts:
    usdIpRedistributeGroup.setStatus("current")

usdIpRouteMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 2, 9)
)
usdIpRouteMapGroup.setObjects(
      *(("Unisphere-Data-IP-POLICY-MIB", "usdIpRouteMapCreatedInternally"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpRouteMapPolicy"),
        ("Unisphere-Data-IP-POLICY-MIB", "usdIpRouteMapDisplay"))
)
if mibBuilder.loadTexts:
    usdIpRouteMapGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdIpPolicyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdIpPolicyCompliance.setStatus(
        "obsolete"
    )

usdIpPolicyCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdIpPolicyCompliance2.setStatus(
        "obsolete"
    )

usdIpPolicyCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 1, 3)
)
if mibBuilder.loadTexts:
    usdIpPolicyCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-IP-POLICY-MIB",
    **{"UsdIpPolicyName": UsdIpPolicyName,
       "UsdIpPolicyPolicy": UsdIpPolicyPolicy,
       "UsdIpRedistributeProtocol": UsdIpRedistributeProtocol,
       "UsdIpPolicyAdminStatus": UsdIpPolicyAdminStatus,
       "UsdIpPolicyExtendedCommunity": UsdIpPolicyExtendedCommunity,
       "usdIpPolicyMIB": usdIpPolicyMIB,
       "usdIpPolicyObjects": usdIpPolicyObjects,
       "usdIpAccessList": usdIpAccessList,
       "usdIpAccessListTable": usdIpAccessListTable,
       "usdIpAccessListEntry": usdIpAccessListEntry,
       "usdIpAccessListId": usdIpAccessListId,
       "usdIpAccessListElemId": usdIpAccessListElemId,
       "usdIpAccessListRowStatus": usdIpAccessListRowStatus,
       "usdIpAccessListAction": usdIpAccessListAction,
       "usdIpAccessListSrc": usdIpAccessListSrc,
       "usdIpAccessListSrcMask": usdIpAccessListSrcMask,
       "usdIpAccessListDst": usdIpAccessListDst,
       "usdIpAccessListDstMask": usdIpAccessListDstMask,
       "usdIpAccessListProtocol": usdIpAccessListProtocol,
       "usdIpNamedAccessList": usdIpNamedAccessList,
       "usdIpNamedAccessListTable": usdIpNamedAccessListTable,
       "usdIpNamedAccessListEntry": usdIpNamedAccessListEntry,
       "usdIpNamedAccessListName": usdIpNamedAccessListName,
       "usdIpNamedAccessListElemId": usdIpNamedAccessListElemId,
       "usdIpNamedAccessListRowStatus": usdIpNamedAccessListRowStatus,
       "usdIpNamedAccessListAction": usdIpNamedAccessListAction,
       "usdIpNamedAccessListSrc": usdIpNamedAccessListSrc,
       "usdIpNamedAccessListSrcMask": usdIpNamedAccessListSrcMask,
       "usdIpNamedAccessListDst": usdIpNamedAccessListDst,
       "usdIpNamedAccessListDstMask": usdIpNamedAccessListDstMask,
       "usdIpNamedAccessListProtocol": usdIpNamedAccessListProtocol,
       "usdIpAspAccessList": usdIpAspAccessList,
       "usdIpAspAccessTable": usdIpAspAccessTable,
       "usdIpAspAccessEntry": usdIpAspAccessEntry,
       "usdIpAspAccessName": usdIpAspAccessName,
       "usdIpAspAccessElemId": usdIpAspAccessElemId,
       "usdIpAspAccessCreatedInternally": usdIpAspAccessCreatedInternally,
       "usdIpAspAccessPolicy": usdIpAspAccessPolicy,
       "usdIpAspAccessExpression": usdIpAspAccessExpression,
       "usdIpAspAccessRowStatus": usdIpAspAccessRowStatus,
       "usdIpPrefixList": usdIpPrefixList,
       "usdIpPrefixListTable": usdIpPrefixListTable,
       "usdIpPrefixListEntry": usdIpPrefixListEntry,
       "usdIpPrefixListName": usdIpPrefixListName,
       "usdIpPrefixListElemId": usdIpPrefixListElemId,
       "usdIpPrefixListIpAddress": usdIpPrefixListIpAddress,
       "usdIpPrefixListLength": usdIpPrefixListLength,
       "usdIpPrefixListPolicy": usdIpPrefixListPolicy,
       "usdIpPrefixListGeValue": usdIpPrefixListGeValue,
       "usdIpPrefixListLeValue": usdIpPrefixListLeValue,
       "usdIpPrefixListDescription": usdIpPrefixListDescription,
       "usdIpPrefixListHitCount": usdIpPrefixListHitCount,
       "usdIpPrefixListRowStatus": usdIpPrefixListRowStatus,
       "usdIpPrefixTree": usdIpPrefixTree,
       "usdIpPrefixTreeTable": usdIpPrefixTreeTable,
       "usdIpPrefixTreeEntry": usdIpPrefixTreeEntry,
       "usdIpPrefixTreeName": usdIpPrefixTreeName,
       "usdIpPrefixTreeIpAddress": usdIpPrefixTreeIpAddress,
       "usdIpPrefixTreeLength": usdIpPrefixTreeLength,
       "usdIpPrefixTreePolicy": usdIpPrefixTreePolicy,
       "usdIpPrefixTreeDescription": usdIpPrefixTreeDescription,
       "usdIpPrefixTreeHitCount": usdIpPrefixTreeHitCount,
       "usdIpPrefixTreeRowStatus": usdIpPrefixTreeRowStatus,
       "usdIpCommunityList": usdIpCommunityList,
       "usdIpCommunityListTable": usdIpCommunityListTable,
       "usdIpCommunityListEntry": usdIpCommunityListEntry,
       "usdIpCommunityListName": usdIpCommunityListName,
       "usdIpCommunityListElemId": usdIpCommunityListElemId,
       "usdIpCommunityListCreatedInternally": usdIpCommunityListCreatedInternally,
       "usdIpCommunityListExtended": usdIpCommunityListExtended,
       "usdIpCommunityListPolicy": usdIpCommunityListPolicy,
       "usdIpCommunityListExpression": usdIpCommunityListExpression,
       "usdIpCommunityListRowStatus": usdIpCommunityListRowStatus,
       "usdIpExtCommunityListTable": usdIpExtCommunityListTable,
       "usdIpExtCommunityListEntry": usdIpExtCommunityListEntry,
       "usdIpExtCommunityListName": usdIpExtCommunityListName,
       "usdIpExtCommunityListElemId": usdIpExtCommunityListElemId,
       "usdIpExtCommunityListCreatedInternally": usdIpExtCommunityListCreatedInternally,
       "usdIpExtCommunityListPolicy": usdIpExtCommunityListPolicy,
       "usdIpExtCommunityListExpression": usdIpExtCommunityListExpression,
       "usdIpExtCommunityListRowStatus": usdIpExtCommunityListRowStatus,
       "usdIpRedistributeList": usdIpRedistributeList,
       "usdIpDynRedistributeTable": usdIpDynRedistributeTable,
       "usdIpDynRedistributeEntry": usdIpDynRedistributeEntry,
       "usdIpDynRedistributeToProtocol": usdIpDynRedistributeToProtocol,
       "usdIpDynRedistributeState": usdIpDynRedistributeState,
       "usdIpDynRedistributeRowStatus": usdIpDynRedistributeRowStatus,
       "usdIpRedistributeTable": usdIpRedistributeTable,
       "usdIpRedistributeEntry": usdIpRedistributeEntry,
       "usdIpRedistributeToProtocol": usdIpRedistributeToProtocol,
       "usdIpRedistributeFromProtocol": usdIpRedistributeFromProtocol,
       "usdIpRedistributeState": usdIpRedistributeState,
       "usdIpRedistributeRouteMapName": usdIpRedistributeRouteMapName,
       "usdIpRedistributeRowStatus": usdIpRedistributeRowStatus,
       "usdIpRouteMapTree": usdIpRouteMapTree,
       "usdIpRouteMapTable": usdIpRouteMapTable,
       "usdIpRouteMapEntry": usdIpRouteMapEntry,
       "usdIpRouteMapName": usdIpRouteMapName,
       "usdIpRouteMapSequenceNum": usdIpRouteMapSequenceNum,
       "usdIpRouteMapElemId": usdIpRouteMapElemId,
       "usdIpRouteMapSubElemId": usdIpRouteMapSubElemId,
       "usdIpRouteMapCreatedInternally": usdIpRouteMapCreatedInternally,
       "usdIpRouteMapPolicy": usdIpRouteMapPolicy,
       "usdIpRouteMapDisplay": usdIpRouteMapDisplay,
       "usdIpPolicyConformance": usdIpPolicyConformance,
       "usdIpPolicyCompliances": usdIpPolicyCompliances,
       "usdIpPolicyCompliance": usdIpPolicyCompliance,
       "usdIpPolicyCompliance2": usdIpPolicyCompliance2,
       "usdIpPolicyCompliance3": usdIpPolicyCompliance3,
       "usdIpPolicyGroups": usdIpPolicyGroups,
       "usdIpAccessListGroup": usdIpAccessListGroup,
       "usdIpNamedAccessListGroup": usdIpNamedAccessListGroup,
       "usdIpAspAccessListGroup": usdIpAspAccessListGroup,
       "usdIpPrefixListGroup": usdIpPrefixListGroup,
       "usdIpPrefixTreeGroup": usdIpPrefixTreeGroup,
       "usdIpCommunityListGroup": usdIpCommunityListGroup,
       "usdIpExtCommunityListGroup": usdIpExtCommunityListGroup,
       "usdIpRedistributeGroup": usdIpRedistributeGroup,
       "usdIpRouteMapGroup": usdIpRouteMapGroup}
)
