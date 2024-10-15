# SNMP MIB module (Juniper-IP-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-IP-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:35 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

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


# MODULE-IDENTITY

juniIpPolicyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13)
)
juniIpPolicyMIB.setRevisions(
        ("2007-01-25 08:34",
         "2006-07-25 04:13",
         "2006-01-10 14:21",
         "2004-02-05 14:21",
         "2003-02-05 14:21",
         "2003-02-04 22:30",
         "2002-01-03 15:06",
         "2000-07-20 00:00",
         "1998-11-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniIpPolicyName(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class JuniIpPolicyPolicy(Integer32, TextualConvention):
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



class JuniIpDynRedistributeProtocol(Integer32, TextualConvention):
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
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("ipRedistrProtocolBgp", 6),
          ("ipRedistrProtocolConnected", 5),
          ("ipRedistrProtocolDefaultRoute", 17),
          ("ipRedistrProtocolDvmrp", 11),
          ("ipRedistrProtocolDvmrpAggregate", 12),
          ("ipRedistrProtocolHidden", 13),
          ("ipRedistrProtocolIsis", 1),
          ("ipRedistrProtocolMBgp", 7),
          ("ipRedistrProtocolOspf", 3),
          ("ipRedistrProtocolOspfExtern", 10),
          ("ipRedistrProtocolOspfIntern", 9),
          ("ipRedistrProtocolOwnerAccess", 14),
          ("ipRedistrProtocolOwnerAccessInternal", 15),
          ("ipRedistrProtocolOwnerDialout", 16),
          ("ipRedistrProtocolRip", 2),
          ("ipRedistrProtocolStatic", 4),
          ("ipRedistrProtocolStaticLow", 8))
    )



class JuniIpRedistributeProtocol(Integer32, TextualConvention):
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
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("ipRedistrProtocolAccess", 9),
          ("ipRedistrProtocolAccessInternal", 10),
          ("ipRedistrProtocolBgp", 2),
          ("ipRedistrProtocolConnected", 7),
          ("ipRedistrProtocolDefaultRoute", 8),
          ("ipRedistrProtocolDialout", 12),
          ("ipRedistrProtocolDvmrp", 11),
          ("ipRedistrProtocolIsis", 5),
          ("ipRedistrProtocolLdpUcast", 15),
          ("ipRedistrProtocolMBgp", 3),
          ("ipRedistrProtocolOspf", 4),
          ("ipRedistrProtocolOspfM", 13),
          ("ipRedistrProtocolRip", 6),
          ("ipRedistrProtocolStatic", 1),
          ("ipRedistrProtocolStaticMcast", 14))
    )



class JuniIpPolicyAdminStatus(Integer32, TextualConvention):
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



class JuniIpPolicyExtendedCommunity(OctetString, TextualConvention):
    status = "current"
    displayHint = "22a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )



# MIB Managed Objects in the order of their OIDs

_JuniIpPolicyObjects_ObjectIdentity = ObjectIdentity
juniIpPolicyObjects = _JuniIpPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1)
)
_JuniIpAccessList_ObjectIdentity = ObjectIdentity
juniIpAccessList = _JuniIpAccessList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 1)
)
_JuniIpAccessListTable_Object = MibTable
juniIpAccessListTable = _JuniIpAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 1, 1)
)
if mibBuilder.loadTexts:
    juniIpAccessListTable.setStatus("current")
_JuniIpAccessListEntry_Object = MibTableRow
juniIpAccessListEntry = _JuniIpAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 1, 1, 1)
)
juniIpAccessListEntry.setIndexNames(
    (0, "Juniper-IP-POLICY-MIB", "juniIpAccessListId"),
    (0, "Juniper-IP-POLICY-MIB", "juniIpAccessListElemId"),
)
if mibBuilder.loadTexts:
    juniIpAccessListEntry.setStatus("current")


class _JuniIpAccessListId_Type(Integer32):
    """Custom type juniIpAccessListId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_JuniIpAccessListId_Type.__name__ = "Integer32"
_JuniIpAccessListId_Object = MibTableColumn
juniIpAccessListId = _JuniIpAccessListId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 1, 1, 1, 1),
    _JuniIpAccessListId_Type()
)
juniIpAccessListId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpAccessListId.setStatus("current")


class _JuniIpAccessListElemId_Type(Integer32):
    """Custom type juniIpAccessListElemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_JuniIpAccessListElemId_Type.__name__ = "Integer32"
_JuniIpAccessListElemId_Object = MibTableColumn
juniIpAccessListElemId = _JuniIpAccessListElemId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 1, 1, 1, 2),
    _JuniIpAccessListElemId_Type()
)
juniIpAccessListElemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpAccessListElemId.setStatus("current")
_JuniIpAccessListRowStatus_Type = RowStatus
_JuniIpAccessListRowStatus_Object = MibTableColumn
juniIpAccessListRowStatus = _JuniIpAccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 1, 1, 1, 3),
    _JuniIpAccessListRowStatus_Type()
)
juniIpAccessListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAccessListRowStatus.setStatus("current")


class _JuniIpAccessListAction_Type(JuniIpPolicyPolicy):
    """Custom type juniIpAccessListAction based on JuniIpPolicyPolicy"""


_JuniIpAccessListAction_Object = MibTableColumn
juniIpAccessListAction = _JuniIpAccessListAction_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 1, 1, 1, 4),
    _JuniIpAccessListAction_Type()
)
juniIpAccessListAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAccessListAction.setStatus("current")


class _JuniIpAccessListSrc_Type(IpAddress):
    """Custom type juniIpAccessListSrc based on IpAddress"""
    defaultHexValue = "00000000"


_JuniIpAccessListSrc_Object = MibTableColumn
juniIpAccessListSrc = _JuniIpAccessListSrc_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 1, 1, 1, 5),
    _JuniIpAccessListSrc_Type()
)
juniIpAccessListSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAccessListSrc.setStatus("current")


class _JuniIpAccessListSrcMask_Type(IpAddress):
    """Custom type juniIpAccessListSrcMask based on IpAddress"""
    defaultHexValue = "00000000"


_JuniIpAccessListSrcMask_Object = MibTableColumn
juniIpAccessListSrcMask = _JuniIpAccessListSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 1, 1, 1, 6),
    _JuniIpAccessListSrcMask_Type()
)
juniIpAccessListSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAccessListSrcMask.setStatus("current")


class _JuniIpAccessListDst_Type(IpAddress):
    """Custom type juniIpAccessListDst based on IpAddress"""
    defaultHexValue = "00000000"


_JuniIpAccessListDst_Object = MibTableColumn
juniIpAccessListDst = _JuniIpAccessListDst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 1, 1, 1, 7),
    _JuniIpAccessListDst_Type()
)
juniIpAccessListDst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAccessListDst.setStatus("current")


class _JuniIpAccessListDstMask_Type(IpAddress):
    """Custom type juniIpAccessListDstMask based on IpAddress"""
    defaultHexValue = "00000000"


_JuniIpAccessListDstMask_Object = MibTableColumn
juniIpAccessListDstMask = _JuniIpAccessListDstMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 1, 1, 1, 8),
    _JuniIpAccessListDstMask_Type()
)
juniIpAccessListDstMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAccessListDstMask.setStatus("current")


class _JuniIpAccessListProtocol_Type(Integer32):
    """Custom type juniIpAccessListProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniIpAccessListProtocol_Type.__name__ = "Integer32"
_JuniIpAccessListProtocol_Object = MibTableColumn
juniIpAccessListProtocol = _JuniIpAccessListProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 1, 1, 1, 9),
    _JuniIpAccessListProtocol_Type()
)
juniIpAccessListProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAccessListProtocol.setStatus("current")
_JuniIpNamedAccessList_ObjectIdentity = ObjectIdentity
juniIpNamedAccessList = _JuniIpNamedAccessList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 2)
)
_JuniIpNamedAccessListTable_Object = MibTable
juniIpNamedAccessListTable = _JuniIpNamedAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 2, 1)
)
if mibBuilder.loadTexts:
    juniIpNamedAccessListTable.setStatus("current")
_JuniIpNamedAccessListEntry_Object = MibTableRow
juniIpNamedAccessListEntry = _JuniIpNamedAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 2, 1, 1)
)
juniIpNamedAccessListEntry.setIndexNames(
    (0, "Juniper-IP-POLICY-MIB", "juniIpNamedAccessListName"),
    (0, "Juniper-IP-POLICY-MIB", "juniIpNamedAccessListElemId"),
)
if mibBuilder.loadTexts:
    juniIpNamedAccessListEntry.setStatus("current")
_JuniIpNamedAccessListName_Type = JuniIpPolicyName
_JuniIpNamedAccessListName_Object = MibTableColumn
juniIpNamedAccessListName = _JuniIpNamedAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 2, 1, 1, 1),
    _JuniIpNamedAccessListName_Type()
)
juniIpNamedAccessListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpNamedAccessListName.setStatus("current")


class _JuniIpNamedAccessListElemId_Type(Integer32):
    """Custom type juniIpNamedAccessListElemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_JuniIpNamedAccessListElemId_Type.__name__ = "Integer32"
_JuniIpNamedAccessListElemId_Object = MibTableColumn
juniIpNamedAccessListElemId = _JuniIpNamedAccessListElemId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 2, 1, 1, 2),
    _JuniIpNamedAccessListElemId_Type()
)
juniIpNamedAccessListElemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpNamedAccessListElemId.setStatus("current")
_JuniIpNamedAccessListRowStatus_Type = RowStatus
_JuniIpNamedAccessListRowStatus_Object = MibTableColumn
juniIpNamedAccessListRowStatus = _JuniIpNamedAccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 2, 1, 1, 3),
    _JuniIpNamedAccessListRowStatus_Type()
)
juniIpNamedAccessListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpNamedAccessListRowStatus.setStatus("current")


class _JuniIpNamedAccessListAction_Type(JuniIpPolicyPolicy):
    """Custom type juniIpNamedAccessListAction based on JuniIpPolicyPolicy"""


_JuniIpNamedAccessListAction_Object = MibTableColumn
juniIpNamedAccessListAction = _JuniIpNamedAccessListAction_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 2, 1, 1, 4),
    _JuniIpNamedAccessListAction_Type()
)
juniIpNamedAccessListAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpNamedAccessListAction.setStatus("current")


class _JuniIpNamedAccessListSrc_Type(IpAddress):
    """Custom type juniIpNamedAccessListSrc based on IpAddress"""
    defaultHexValue = "00000000"


_JuniIpNamedAccessListSrc_Object = MibTableColumn
juniIpNamedAccessListSrc = _JuniIpNamedAccessListSrc_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 2, 1, 1, 5),
    _JuniIpNamedAccessListSrc_Type()
)
juniIpNamedAccessListSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpNamedAccessListSrc.setStatus("current")


class _JuniIpNamedAccessListSrcMask_Type(IpAddress):
    """Custom type juniIpNamedAccessListSrcMask based on IpAddress"""
    defaultHexValue = "00000000"


_JuniIpNamedAccessListSrcMask_Object = MibTableColumn
juniIpNamedAccessListSrcMask = _JuniIpNamedAccessListSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 2, 1, 1, 6),
    _JuniIpNamedAccessListSrcMask_Type()
)
juniIpNamedAccessListSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpNamedAccessListSrcMask.setStatus("current")


class _JuniIpNamedAccessListDst_Type(IpAddress):
    """Custom type juniIpNamedAccessListDst based on IpAddress"""
    defaultHexValue = "00000000"


_JuniIpNamedAccessListDst_Object = MibTableColumn
juniIpNamedAccessListDst = _JuniIpNamedAccessListDst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 2, 1, 1, 7),
    _JuniIpNamedAccessListDst_Type()
)
juniIpNamedAccessListDst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpNamedAccessListDst.setStatus("current")


class _JuniIpNamedAccessListDstMask_Type(IpAddress):
    """Custom type juniIpNamedAccessListDstMask based on IpAddress"""
    defaultHexValue = "00000000"


_JuniIpNamedAccessListDstMask_Object = MibTableColumn
juniIpNamedAccessListDstMask = _JuniIpNamedAccessListDstMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 2, 1, 1, 8),
    _JuniIpNamedAccessListDstMask_Type()
)
juniIpNamedAccessListDstMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpNamedAccessListDstMask.setStatus("current")


class _JuniIpNamedAccessListProtocol_Type(Integer32):
    """Custom type juniIpNamedAccessListProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniIpNamedAccessListProtocol_Type.__name__ = "Integer32"
_JuniIpNamedAccessListProtocol_Object = MibTableColumn
juniIpNamedAccessListProtocol = _JuniIpNamedAccessListProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 2, 1, 1, 9),
    _JuniIpNamedAccessListProtocol_Type()
)
juniIpNamedAccessListProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpNamedAccessListProtocol.setStatus("current")
_JuniIpAspAccessList_ObjectIdentity = ObjectIdentity
juniIpAspAccessList = _JuniIpAspAccessList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 3)
)
_JuniIpAspAccessTable_Object = MibTable
juniIpAspAccessTable = _JuniIpAspAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 3, 1)
)
if mibBuilder.loadTexts:
    juniIpAspAccessTable.setStatus("current")
_JuniIpAspAccessEntry_Object = MibTableRow
juniIpAspAccessEntry = _JuniIpAspAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 3, 1, 1)
)
juniIpAspAccessEntry.setIndexNames(
    (0, "Juniper-IP-POLICY-MIB", "juniIpAspAccessName"),
    (0, "Juniper-IP-POLICY-MIB", "juniIpAspAccessElemId"),
)
if mibBuilder.loadTexts:
    juniIpAspAccessEntry.setStatus("current")
_JuniIpAspAccessName_Type = JuniIpPolicyName
_JuniIpAspAccessName_Object = MibTableColumn
juniIpAspAccessName = _JuniIpAspAccessName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 3, 1, 1, 1),
    _JuniIpAspAccessName_Type()
)
juniIpAspAccessName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpAspAccessName.setStatus("current")


class _JuniIpAspAccessElemId_Type(Integer32):
    """Custom type juniIpAspAccessElemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_JuniIpAspAccessElemId_Type.__name__ = "Integer32"
_JuniIpAspAccessElemId_Object = MibTableColumn
juniIpAspAccessElemId = _JuniIpAspAccessElemId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 3, 1, 1, 2),
    _JuniIpAspAccessElemId_Type()
)
juniIpAspAccessElemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpAspAccessElemId.setStatus("current")
_JuniIpAspAccessCreatedInternally_Type = TruthValue
_JuniIpAspAccessCreatedInternally_Object = MibTableColumn
juniIpAspAccessCreatedInternally = _JuniIpAspAccessCreatedInternally_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 3, 1, 1, 3),
    _JuniIpAspAccessCreatedInternally_Type()
)
juniIpAspAccessCreatedInternally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpAspAccessCreatedInternally.setStatus("current")
_JuniIpAspAccessPolicy_Type = JuniIpPolicyPolicy
_JuniIpAspAccessPolicy_Object = MibTableColumn
juniIpAspAccessPolicy = _JuniIpAspAccessPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 3, 1, 1, 4),
    _JuniIpAspAccessPolicy_Type()
)
juniIpAspAccessPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAspAccessPolicy.setStatus("current")


class _JuniIpAspAccessExpression_Type(OctetString):
    """Custom type juniIpAspAccessExpression based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_JuniIpAspAccessExpression_Type.__name__ = "OctetString"
_JuniIpAspAccessExpression_Object = MibTableColumn
juniIpAspAccessExpression = _JuniIpAspAccessExpression_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 3, 1, 1, 5),
    _JuniIpAspAccessExpression_Type()
)
juniIpAspAccessExpression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAspAccessExpression.setStatus("current")
_JuniIpAspAccessRowStatus_Type = RowStatus
_JuniIpAspAccessRowStatus_Object = MibTableColumn
juniIpAspAccessRowStatus = _JuniIpAspAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 3, 1, 1, 6),
    _JuniIpAspAccessRowStatus_Type()
)
juniIpAspAccessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpAspAccessRowStatus.setStatus("current")
_JuniIpPrefixList_ObjectIdentity = ObjectIdentity
juniIpPrefixList = _JuniIpPrefixList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 4)
)
_JuniIpPrefixListTable_Object = MibTable
juniIpPrefixListTable = _JuniIpPrefixListTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 4, 1)
)
if mibBuilder.loadTexts:
    juniIpPrefixListTable.setStatus("current")
_JuniIpPrefixListEntry_Object = MibTableRow
juniIpPrefixListEntry = _JuniIpPrefixListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 4, 1, 1)
)
juniIpPrefixListEntry.setIndexNames(
    (0, "Juniper-IP-POLICY-MIB", "juniIpPrefixListName"),
    (0, "Juniper-IP-POLICY-MIB", "juniIpPrefixListElemId"),
    (0, "Juniper-IP-POLICY-MIB", "juniIpPrefixListIpAddress"),
    (0, "Juniper-IP-POLICY-MIB", "juniIpPrefixListLength"),
)
if mibBuilder.loadTexts:
    juniIpPrefixListEntry.setStatus("current")
_JuniIpPrefixListName_Type = JuniIpPolicyName
_JuniIpPrefixListName_Object = MibTableColumn
juniIpPrefixListName = _JuniIpPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 4, 1, 1, 1),
    _JuniIpPrefixListName_Type()
)
juniIpPrefixListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpPrefixListName.setStatus("current")


class _JuniIpPrefixListElemId_Type(Integer32):
    """Custom type juniIpPrefixListElemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_JuniIpPrefixListElemId_Type.__name__ = "Integer32"
_JuniIpPrefixListElemId_Object = MibTableColumn
juniIpPrefixListElemId = _JuniIpPrefixListElemId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 4, 1, 1, 2),
    _JuniIpPrefixListElemId_Type()
)
juniIpPrefixListElemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpPrefixListElemId.setStatus("current")
_JuniIpPrefixListIpAddress_Type = IpAddress
_JuniIpPrefixListIpAddress_Object = MibTableColumn
juniIpPrefixListIpAddress = _JuniIpPrefixListIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 4, 1, 1, 3),
    _JuniIpPrefixListIpAddress_Type()
)
juniIpPrefixListIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpPrefixListIpAddress.setStatus("current")


class _JuniIpPrefixListLength_Type(Integer32):
    """Custom type juniIpPrefixListLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_JuniIpPrefixListLength_Type.__name__ = "Integer32"
_JuniIpPrefixListLength_Object = MibTableColumn
juniIpPrefixListLength = _JuniIpPrefixListLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 4, 1, 1, 4),
    _JuniIpPrefixListLength_Type()
)
juniIpPrefixListLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpPrefixListLength.setStatus("current")
_JuniIpPrefixListPolicy_Type = JuniIpPolicyPolicy
_JuniIpPrefixListPolicy_Object = MibTableColumn
juniIpPrefixListPolicy = _JuniIpPrefixListPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 4, 1, 1, 5),
    _JuniIpPrefixListPolicy_Type()
)
juniIpPrefixListPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpPrefixListPolicy.setStatus("current")


class _JuniIpPrefixListGeValue_Type(Integer32):
    """Custom type juniIpPrefixListGeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_JuniIpPrefixListGeValue_Type.__name__ = "Integer32"
_JuniIpPrefixListGeValue_Object = MibTableColumn
juniIpPrefixListGeValue = _JuniIpPrefixListGeValue_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 4, 1, 1, 6),
    _JuniIpPrefixListGeValue_Type()
)
juniIpPrefixListGeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpPrefixListGeValue.setStatus("current")


class _JuniIpPrefixListLeValue_Type(Integer32):
    """Custom type juniIpPrefixListLeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_JuniIpPrefixListLeValue_Type.__name__ = "Integer32"
_JuniIpPrefixListLeValue_Object = MibTableColumn
juniIpPrefixListLeValue = _JuniIpPrefixListLeValue_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 4, 1, 1, 7),
    _JuniIpPrefixListLeValue_Type()
)
juniIpPrefixListLeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpPrefixListLeValue.setStatus("current")
_JuniIpPrefixListDescription_Type = DisplayString
_JuniIpPrefixListDescription_Object = MibTableColumn
juniIpPrefixListDescription = _JuniIpPrefixListDescription_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 4, 1, 1, 8),
    _JuniIpPrefixListDescription_Type()
)
juniIpPrefixListDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpPrefixListDescription.setStatus("current")
_JuniIpPrefixListHitCount_Type = Counter32
_JuniIpPrefixListHitCount_Object = MibTableColumn
juniIpPrefixListHitCount = _JuniIpPrefixListHitCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 4, 1, 1, 9),
    _JuniIpPrefixListHitCount_Type()
)
juniIpPrefixListHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpPrefixListHitCount.setStatus("current")
_JuniIpPrefixListRowStatus_Type = RowStatus
_JuniIpPrefixListRowStatus_Object = MibTableColumn
juniIpPrefixListRowStatus = _JuniIpPrefixListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 4, 1, 1, 10),
    _JuniIpPrefixListRowStatus_Type()
)
juniIpPrefixListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpPrefixListRowStatus.setStatus("current")
_JuniIpPrefixTree_ObjectIdentity = ObjectIdentity
juniIpPrefixTree = _JuniIpPrefixTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 5)
)
_JuniIpPrefixTreeTable_Object = MibTable
juniIpPrefixTreeTable = _JuniIpPrefixTreeTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 5, 1)
)
if mibBuilder.loadTexts:
    juniIpPrefixTreeTable.setStatus("current")
_JuniIpPrefixTreeEntry_Object = MibTableRow
juniIpPrefixTreeEntry = _JuniIpPrefixTreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 5, 1, 1)
)
juniIpPrefixTreeEntry.setIndexNames(
    (0, "Juniper-IP-POLICY-MIB", "juniIpPrefixTreeName"),
    (0, "Juniper-IP-POLICY-MIB", "juniIpPrefixTreeIpAddress"),
    (0, "Juniper-IP-POLICY-MIB", "juniIpPrefixTreeLength"),
)
if mibBuilder.loadTexts:
    juniIpPrefixTreeEntry.setStatus("current")
_JuniIpPrefixTreeName_Type = JuniIpPolicyName
_JuniIpPrefixTreeName_Object = MibTableColumn
juniIpPrefixTreeName = _JuniIpPrefixTreeName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 5, 1, 1, 1),
    _JuniIpPrefixTreeName_Type()
)
juniIpPrefixTreeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpPrefixTreeName.setStatus("current")
_JuniIpPrefixTreeIpAddress_Type = IpAddress
_JuniIpPrefixTreeIpAddress_Object = MibTableColumn
juniIpPrefixTreeIpAddress = _JuniIpPrefixTreeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 5, 1, 1, 2),
    _JuniIpPrefixTreeIpAddress_Type()
)
juniIpPrefixTreeIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpPrefixTreeIpAddress.setStatus("current")


class _JuniIpPrefixTreeLength_Type(Integer32):
    """Custom type juniIpPrefixTreeLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_JuniIpPrefixTreeLength_Type.__name__ = "Integer32"
_JuniIpPrefixTreeLength_Object = MibTableColumn
juniIpPrefixTreeLength = _JuniIpPrefixTreeLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 5, 1, 1, 3),
    _JuniIpPrefixTreeLength_Type()
)
juniIpPrefixTreeLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpPrefixTreeLength.setStatus("current")
_JuniIpPrefixTreePolicy_Type = JuniIpPolicyPolicy
_JuniIpPrefixTreePolicy_Object = MibTableColumn
juniIpPrefixTreePolicy = _JuniIpPrefixTreePolicy_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 5, 1, 1, 4),
    _JuniIpPrefixTreePolicy_Type()
)
juniIpPrefixTreePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpPrefixTreePolicy.setStatus("current")
_JuniIpPrefixTreeDescription_Type = DisplayString
_JuniIpPrefixTreeDescription_Object = MibTableColumn
juniIpPrefixTreeDescription = _JuniIpPrefixTreeDescription_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 5, 1, 1, 5),
    _JuniIpPrefixTreeDescription_Type()
)
juniIpPrefixTreeDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpPrefixTreeDescription.setStatus("current")
_JuniIpPrefixTreeHitCount_Type = Counter32
_JuniIpPrefixTreeHitCount_Object = MibTableColumn
juniIpPrefixTreeHitCount = _JuniIpPrefixTreeHitCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 5, 1, 1, 6),
    _JuniIpPrefixTreeHitCount_Type()
)
juniIpPrefixTreeHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpPrefixTreeHitCount.setStatus("current")
_JuniIpPrefixTreeRowStatus_Type = RowStatus
_JuniIpPrefixTreeRowStatus_Object = MibTableColumn
juniIpPrefixTreeRowStatus = _JuniIpPrefixTreeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 5, 1, 1, 7),
    _JuniIpPrefixTreeRowStatus_Type()
)
juniIpPrefixTreeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpPrefixTreeRowStatus.setStatus("current")
_JuniIpCommunityList_ObjectIdentity = ObjectIdentity
juniIpCommunityList = _JuniIpCommunityList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6)
)
_JuniIpCommunityListTable_Object = MibTable
juniIpCommunityListTable = _JuniIpCommunityListTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 1)
)
if mibBuilder.loadTexts:
    juniIpCommunityListTable.setStatus("current")
_JuniIpCommunityListEntry_Object = MibTableRow
juniIpCommunityListEntry = _JuniIpCommunityListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 1, 1)
)
juniIpCommunityListEntry.setIndexNames(
    (0, "Juniper-IP-POLICY-MIB", "juniIpCommunityListName"),
    (0, "Juniper-IP-POLICY-MIB", "juniIpCommunityListElemId"),
)
if mibBuilder.loadTexts:
    juniIpCommunityListEntry.setStatus("current")
_JuniIpCommunityListName_Type = JuniIpPolicyName
_JuniIpCommunityListName_Object = MibTableColumn
juniIpCommunityListName = _JuniIpCommunityListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 1, 1, 1),
    _JuniIpCommunityListName_Type()
)
juniIpCommunityListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpCommunityListName.setStatus("current")


class _JuniIpCommunityListElemId_Type(Integer32):
    """Custom type juniIpCommunityListElemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_JuniIpCommunityListElemId_Type.__name__ = "Integer32"
_JuniIpCommunityListElemId_Object = MibTableColumn
juniIpCommunityListElemId = _JuniIpCommunityListElemId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 1, 1, 2),
    _JuniIpCommunityListElemId_Type()
)
juniIpCommunityListElemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpCommunityListElemId.setStatus("current")
_JuniIpCommunityListCreatedInternally_Type = TruthValue
_JuniIpCommunityListCreatedInternally_Object = MibTableColumn
juniIpCommunityListCreatedInternally = _JuniIpCommunityListCreatedInternally_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 1, 1, 3),
    _JuniIpCommunityListCreatedInternally_Type()
)
juniIpCommunityListCreatedInternally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpCommunityListCreatedInternally.setStatus("current")
_JuniIpCommunityListExtended_Type = TruthValue
_JuniIpCommunityListExtended_Object = MibTableColumn
juniIpCommunityListExtended = _JuniIpCommunityListExtended_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 1, 1, 4),
    _JuniIpCommunityListExtended_Type()
)
juniIpCommunityListExtended.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpCommunityListExtended.setStatus("current")
_JuniIpCommunityListPolicy_Type = JuniIpPolicyPolicy
_JuniIpCommunityListPolicy_Object = MibTableColumn
juniIpCommunityListPolicy = _JuniIpCommunityListPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 1, 1, 5),
    _JuniIpCommunityListPolicy_Type()
)
juniIpCommunityListPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpCommunityListPolicy.setStatus("current")


class _JuniIpCommunityListExpression_Type(OctetString):
    """Custom type juniIpCommunityListExpression based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_JuniIpCommunityListExpression_Type.__name__ = "OctetString"
_JuniIpCommunityListExpression_Object = MibTableColumn
juniIpCommunityListExpression = _JuniIpCommunityListExpression_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 1, 1, 6),
    _JuniIpCommunityListExpression_Type()
)
juniIpCommunityListExpression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpCommunityListExpression.setStatus("current")
_JuniIpCommunityListRowStatus_Type = RowStatus
_JuniIpCommunityListRowStatus_Object = MibTableColumn
juniIpCommunityListRowStatus = _JuniIpCommunityListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 1, 1, 7),
    _JuniIpCommunityListRowStatus_Type()
)
juniIpCommunityListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpCommunityListRowStatus.setStatus("current")
_JuniIpExtCommunityListTable_Object = MibTable
juniIpExtCommunityListTable = _JuniIpExtCommunityListTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 2)
)
if mibBuilder.loadTexts:
    juniIpExtCommunityListTable.setStatus("current")
_JuniIpExtCommunityListEntry_Object = MibTableRow
juniIpExtCommunityListEntry = _JuniIpExtCommunityListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 2, 1)
)
juniIpExtCommunityListEntry.setIndexNames(
    (0, "Juniper-IP-POLICY-MIB", "juniIpExtCommunityListName"),
    (0, "Juniper-IP-POLICY-MIB", "juniIpExtCommunityListElemId"),
)
if mibBuilder.loadTexts:
    juniIpExtCommunityListEntry.setStatus("current")
_JuniIpExtCommunityListName_Type = JuniIpPolicyName
_JuniIpExtCommunityListName_Object = MibTableColumn
juniIpExtCommunityListName = _JuniIpExtCommunityListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 2, 1, 1),
    _JuniIpExtCommunityListName_Type()
)
juniIpExtCommunityListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpExtCommunityListName.setStatus("current")


class _JuniIpExtCommunityListElemId_Type(Integer32):
    """Custom type juniIpExtCommunityListElemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_JuniIpExtCommunityListElemId_Type.__name__ = "Integer32"
_JuniIpExtCommunityListElemId_Object = MibTableColumn
juniIpExtCommunityListElemId = _JuniIpExtCommunityListElemId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 2, 1, 2),
    _JuniIpExtCommunityListElemId_Type()
)
juniIpExtCommunityListElemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpExtCommunityListElemId.setStatus("current")
_JuniIpExtCommunityListCreatedInternally_Type = TruthValue
_JuniIpExtCommunityListCreatedInternally_Object = MibTableColumn
juniIpExtCommunityListCreatedInternally = _JuniIpExtCommunityListCreatedInternally_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 2, 1, 3),
    _JuniIpExtCommunityListCreatedInternally_Type()
)
juniIpExtCommunityListCreatedInternally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpExtCommunityListCreatedInternally.setStatus("current")
_JuniIpExtCommunityListPolicy_Type = JuniIpPolicyPolicy
_JuniIpExtCommunityListPolicy_Object = MibTableColumn
juniIpExtCommunityListPolicy = _JuniIpExtCommunityListPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 2, 1, 4),
    _JuniIpExtCommunityListPolicy_Type()
)
juniIpExtCommunityListPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpExtCommunityListPolicy.setStatus("current")


class _JuniIpExtCommunityListExpression_Type(OctetString):
    """Custom type juniIpExtCommunityListExpression based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 256),
    )


_JuniIpExtCommunityListExpression_Type.__name__ = "OctetString"
_JuniIpExtCommunityListExpression_Object = MibTableColumn
juniIpExtCommunityListExpression = _JuniIpExtCommunityListExpression_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 2, 1, 5),
    _JuniIpExtCommunityListExpression_Type()
)
juniIpExtCommunityListExpression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpExtCommunityListExpression.setStatus("current")
_JuniIpExtCommunityListRowStatus_Type = RowStatus
_JuniIpExtCommunityListRowStatus_Object = MibTableColumn
juniIpExtCommunityListRowStatus = _JuniIpExtCommunityListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 6, 2, 1, 6),
    _JuniIpExtCommunityListRowStatus_Type()
)
juniIpExtCommunityListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpExtCommunityListRowStatus.setStatus("current")
_JuniIpRedistributeList_ObjectIdentity = ObjectIdentity
juniIpRedistributeList = _JuniIpRedistributeList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 7)
)
_JuniIpDynRedistributeTable_Object = MibTable
juniIpDynRedistributeTable = _JuniIpDynRedistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 7, 1)
)
if mibBuilder.loadTexts:
    juniIpDynRedistributeTable.setStatus("current")
_JuniIpDynRedistributeEntry_Object = MibTableRow
juniIpDynRedistributeEntry = _JuniIpDynRedistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 7, 1, 1)
)
juniIpDynRedistributeEntry.setIndexNames(
    (0, "Juniper-IP-POLICY-MIB", "juniIpDynRedistributeToProtocol"),
)
if mibBuilder.loadTexts:
    juniIpDynRedistributeEntry.setStatus("current")
_JuniIpDynRedistributeToProtocol_Type = JuniIpDynRedistributeProtocol
_JuniIpDynRedistributeToProtocol_Object = MibTableColumn
juniIpDynRedistributeToProtocol = _JuniIpDynRedistributeToProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 7, 1, 1, 1),
    _JuniIpDynRedistributeToProtocol_Type()
)
juniIpDynRedistributeToProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpDynRedistributeToProtocol.setStatus("current")


class _JuniIpDynRedistributeState_Type(JuniIpPolicyAdminStatus):
    """Custom type juniIpDynRedistributeState based on JuniIpPolicyAdminStatus"""


_JuniIpDynRedistributeState_Object = MibTableColumn
juniIpDynRedistributeState = _JuniIpDynRedistributeState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 7, 1, 1, 2),
    _JuniIpDynRedistributeState_Type()
)
juniIpDynRedistributeState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpDynRedistributeState.setStatus("current")
_JuniIpDynRedistributeRowStatus_Type = RowStatus
_JuniIpDynRedistributeRowStatus_Object = MibTableColumn
juniIpDynRedistributeRowStatus = _JuniIpDynRedistributeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 7, 1, 1, 3),
    _JuniIpDynRedistributeRowStatus_Type()
)
juniIpDynRedistributeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpDynRedistributeRowStatus.setStatus("current")
_JuniIpRedistributeTable_Object = MibTable
juniIpRedistributeTable = _JuniIpRedistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 7, 2)
)
if mibBuilder.loadTexts:
    juniIpRedistributeTable.setStatus("current")
_JuniIpRedistributeEntry_Object = MibTableRow
juniIpRedistributeEntry = _JuniIpRedistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 7, 2, 1)
)
juniIpRedistributeEntry.setIndexNames(
    (0, "Juniper-IP-POLICY-MIB", "juniIpRedistributeToProtocol"),
    (0, "Juniper-IP-POLICY-MIB", "juniIpRedistributeFromProtocol"),
)
if mibBuilder.loadTexts:
    juniIpRedistributeEntry.setStatus("current")
_JuniIpRedistributeToProtocol_Type = JuniIpRedistributeProtocol
_JuniIpRedistributeToProtocol_Object = MibTableColumn
juniIpRedistributeToProtocol = _JuniIpRedistributeToProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 7, 2, 1, 1),
    _JuniIpRedistributeToProtocol_Type()
)
juniIpRedistributeToProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpRedistributeToProtocol.setStatus("current")
_JuniIpRedistributeFromProtocol_Type = JuniIpRedistributeProtocol
_JuniIpRedistributeFromProtocol_Object = MibTableColumn
juniIpRedistributeFromProtocol = _JuniIpRedistributeFromProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 7, 2, 1, 2),
    _JuniIpRedistributeFromProtocol_Type()
)
juniIpRedistributeFromProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpRedistributeFromProtocol.setStatus("current")


class _JuniIpRedistributeState_Type(JuniIpPolicyAdminStatus):
    """Custom type juniIpRedistributeState based on JuniIpPolicyAdminStatus"""


_JuniIpRedistributeState_Object = MibTableColumn
juniIpRedistributeState = _JuniIpRedistributeState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 7, 2, 1, 3),
    _JuniIpRedistributeState_Type()
)
juniIpRedistributeState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpRedistributeState.setStatus("current")
_JuniIpRedistributeRouteMapName_Type = JuniIpPolicyName
_JuniIpRedistributeRouteMapName_Object = MibTableColumn
juniIpRedistributeRouteMapName = _JuniIpRedistributeRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 7, 2, 1, 4),
    _JuniIpRedistributeRouteMapName_Type()
)
juniIpRedistributeRouteMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpRedistributeRouteMapName.setStatus("current")
_JuniIpRedistributeRowStatus_Type = RowStatus
_JuniIpRedistributeRowStatus_Object = MibTableColumn
juniIpRedistributeRowStatus = _JuniIpRedistributeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 7, 2, 1, 5),
    _JuniIpRedistributeRowStatus_Type()
)
juniIpRedistributeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpRedistributeRowStatus.setStatus("current")
_JuniIpRouteMapTree_ObjectIdentity = ObjectIdentity
juniIpRouteMapTree = _JuniIpRouteMapTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8)
)
_JuniIpRouteMapTable_Object = MibTable
juniIpRouteMapTable = _JuniIpRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 1)
)
if mibBuilder.loadTexts:
    juniIpRouteMapTable.setStatus("current")
_JuniIpRouteMapEntry_Object = MibTableRow
juniIpRouteMapEntry = _JuniIpRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 1, 1)
)
juniIpRouteMapEntry.setIndexNames(
    (0, "Juniper-IP-POLICY-MIB", "juniIpRouteMapName"),
    (0, "Juniper-IP-POLICY-MIB", "juniIpRouteMapSequenceNum"),
    (0, "Juniper-IP-POLICY-MIB", "juniIpRouteMapElemId"),
    (0, "Juniper-IP-POLICY-MIB", "juniIpRouteMapSubElemId"),
)
if mibBuilder.loadTexts:
    juniIpRouteMapEntry.setStatus("current")
_JuniIpRouteMapName_Type = JuniIpPolicyName
_JuniIpRouteMapName_Object = MibTableColumn
juniIpRouteMapName = _JuniIpRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 1, 1, 1),
    _JuniIpRouteMapName_Type()
)
juniIpRouteMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpRouteMapName.setStatus("current")


class _JuniIpRouteMapSequenceNum_Type(Integer32):
    """Custom type juniIpRouteMapSequenceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniIpRouteMapSequenceNum_Type.__name__ = "Integer32"
_JuniIpRouteMapSequenceNum_Object = MibTableColumn
juniIpRouteMapSequenceNum = _JuniIpRouteMapSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 1, 1, 2),
    _JuniIpRouteMapSequenceNum_Type()
)
juniIpRouteMapSequenceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpRouteMapSequenceNum.setStatus("current")


class _JuniIpRouteMapElemId_Type(Integer32):
    """Custom type juniIpRouteMapElemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniIpRouteMapElemId_Type.__name__ = "Integer32"
_JuniIpRouteMapElemId_Object = MibTableColumn
juniIpRouteMapElemId = _JuniIpRouteMapElemId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 1, 1, 3),
    _JuniIpRouteMapElemId_Type()
)
juniIpRouteMapElemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpRouteMapElemId.setStatus("current")


class _JuniIpRouteMapSubElemId_Type(Integer32):
    """Custom type juniIpRouteMapSubElemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniIpRouteMapSubElemId_Type.__name__ = "Integer32"
_JuniIpRouteMapSubElemId_Object = MibTableColumn
juniIpRouteMapSubElemId = _JuniIpRouteMapSubElemId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 1, 1, 4),
    _JuniIpRouteMapSubElemId_Type()
)
juniIpRouteMapSubElemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpRouteMapSubElemId.setStatus("current")
_JuniIpRouteMapCreatedInternally_Type = TruthValue
_JuniIpRouteMapCreatedInternally_Object = MibTableColumn
juniIpRouteMapCreatedInternally = _JuniIpRouteMapCreatedInternally_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 1, 1, 5),
    _JuniIpRouteMapCreatedInternally_Type()
)
juniIpRouteMapCreatedInternally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteMapCreatedInternally.setStatus("current")
_JuniIpRouteMapPolicy_Type = JuniIpPolicyPolicy
_JuniIpRouteMapPolicy_Object = MibTableColumn
juniIpRouteMapPolicy = _JuniIpRouteMapPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 1, 1, 6),
    _JuniIpRouteMapPolicy_Type()
)
juniIpRouteMapPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteMapPolicy.setStatus("current")


class _JuniIpRouteMapDisplay_Type(OctetString):
    """Custom type juniIpRouteMapDisplay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_JuniIpRouteMapDisplay_Type.__name__ = "OctetString"
_JuniIpRouteMapDisplay_Object = MibTableColumn
juniIpRouteMapDisplay = _JuniIpRouteMapDisplay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 1, 1, 7),
    _JuniIpRouteMapDisplay_Type()
)
juniIpRouteMapDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpRouteMapDisplay.setStatus("current")
_JuniIpRouteMapV2Table_Object = MibTable
juniIpRouteMapV2Table = _JuniIpRouteMapV2Table_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 2)
)
if mibBuilder.loadTexts:
    juniIpRouteMapV2Table.setStatus("current")
_JuniIpRouteMapV2Entry_Object = MibTableRow
juniIpRouteMapV2Entry = _JuniIpRouteMapV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 2, 1)
)
juniIpRouteMapV2Entry.setIndexNames(
    (0, "Juniper-IP-POLICY-MIB", "juniIpRouteMapV2Name"),
    (0, "Juniper-IP-POLICY-MIB", "juniIpRouteMapV2SequenceNum"),
)
if mibBuilder.loadTexts:
    juniIpRouteMapV2Entry.setStatus("current")
_JuniIpRouteMapV2Name_Type = JuniIpPolicyName
_JuniIpRouteMapV2Name_Object = MibTableColumn
juniIpRouteMapV2Name = _JuniIpRouteMapV2Name_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 2, 1, 1),
    _JuniIpRouteMapV2Name_Type()
)
juniIpRouteMapV2Name.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpRouteMapV2Name.setStatus("current")


class _JuniIpRouteMapV2SequenceNum_Type(Integer32):
    """Custom type juniIpRouteMapV2SequenceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JuniIpRouteMapV2SequenceNum_Type.__name__ = "Integer32"
_JuniIpRouteMapV2SequenceNum_Object = MibTableColumn
juniIpRouteMapV2SequenceNum = _JuniIpRouteMapV2SequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 2, 1, 2),
    _JuniIpRouteMapV2SequenceNum_Type()
)
juniIpRouteMapV2SequenceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpRouteMapV2SequenceNum.setStatus("current")


class _JuniIpRouteMapV2Policy_Type(JuniIpPolicyPolicy):
    """Custom type juniIpRouteMapV2Policy based on JuniIpPolicyPolicy"""


_JuniIpRouteMapV2Policy_Object = MibTableColumn
juniIpRouteMapV2Policy = _JuniIpRouteMapV2Policy_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 2, 1, 3),
    _JuniIpRouteMapV2Policy_Type()
)
juniIpRouteMapV2Policy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpRouteMapV2Policy.setStatus("current")
_JuniIpRouteMapV2RowStatus_Type = RowStatus
_JuniIpRouteMapV2RowStatus_Object = MibTableColumn
juniIpRouteMapV2RowStatus = _JuniIpRouteMapV2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 2, 1, 4),
    _JuniIpRouteMapV2RowStatus_Type()
)
juniIpRouteMapV2RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpRouteMapV2RowStatus.setStatus("current")
_JuniIpRouteMapClauseTable_Object = MibTable
juniIpRouteMapClauseTable = _JuniIpRouteMapClauseTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 3)
)
if mibBuilder.loadTexts:
    juniIpRouteMapClauseTable.setStatus("current")
_JuniIpRouteMapClauseEntry_Object = MibTableRow
juniIpRouteMapClauseEntry = _JuniIpRouteMapClauseEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 3, 1)
)
juniIpRouteMapClauseEntry.setIndexNames(
    (0, "Juniper-IP-POLICY-MIB", "juniIpRouteMapV2Name"),
    (0, "Juniper-IP-POLICY-MIB", "juniIpRouteMapV2SequenceNum"),
    (0, "Juniper-IP-POLICY-MIB", "juniIpRouteMapClauseElemId"),
    (0, "Juniper-IP-POLICY-MIB", "juniIpRouteMapClauseSubElemId"),
)
if mibBuilder.loadTexts:
    juniIpRouteMapClauseEntry.setStatus("current")


class _JuniIpRouteMapClauseElemId_Type(Integer32):
    """Custom type juniIpRouteMapClauseElemId based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              220,
              221,
              222,
              300)
        )
    )
    namedValues = NamedValues(
        *(("matchAccessList", 5),
          ("matchAsPath", 1),
          ("matchCommunity", 2),
          ("matchDistance", 4),
          ("matchExtendedCommunity", 3),
          ("matchLevel", 11),
          ("matchMetric", 12),
          ("matchMetricType", 13),
          ("matchNextHop", 6),
          ("matchNextHopPreList", 8),
          ("matchNextHopPreTree", 10),
          ("matchNotKnown", 0),
          ("matchPolicyList", 17),
          ("matchPrefixList", 7),
          ("matchPrefixTree", 9),
          ("matchRouteType", 15),
          ("matchSetSummary", 300),
          ("matchSource", 16),
          ("matchTag", 14),
          ("setAsPath", 100),
          ("setAsPathCreateList", 101),
          ("setAutoTag", 102),
          ("setCommList", 103),
          ("setCommunity", 106),
          ("setCommunityAdd", 105),
          ("setCommunityCreateList", 108),
          ("setCommunityCreateListAdd", 107),
          ("setCommunityNone", 104),
          ("setDampingCreate", 221),
          ("setDistance", 222),
          ("setExtendedCommunityCreate", 110),
          ("setExtendedCommunityCreateAdd", 109),
          ("setLevel", 115),
          ("setLocalPref", 113),
          ("setMetric", 116),
          ("setMetricType", 117),
          ("setNextHop", 111),
          ("setNextHopPeerAddr", 112),
          ("setOrigin", 119),
          ("setRouteType", 220),
          ("setTag", 118),
          ("setWeight", 114))
    )


_JuniIpRouteMapClauseElemId_Type.__name__ = "Integer32"
_JuniIpRouteMapClauseElemId_Object = MibTableColumn
juniIpRouteMapClauseElemId = _JuniIpRouteMapClauseElemId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 3, 1, 1),
    _JuniIpRouteMapClauseElemId_Type()
)
juniIpRouteMapClauseElemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpRouteMapClauseElemId.setStatus("current")


class _JuniIpRouteMapClauseSubElemId_Type(Integer32):
    """Custom type juniIpRouteMapClauseSubElemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JuniIpRouteMapClauseSubElemId_Type.__name__ = "Integer32"
_JuniIpRouteMapClauseSubElemId_Object = MibTableColumn
juniIpRouteMapClauseSubElemId = _JuniIpRouteMapClauseSubElemId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 3, 1, 2),
    _JuniIpRouteMapClauseSubElemId_Type()
)
juniIpRouteMapClauseSubElemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpRouteMapClauseSubElemId.setStatus("current")


class _JuniIpRouteMapClauseElemIdAddon_Type(Integer32):
    """Custom type juniIpRouteMapClauseElemIdAddon based on Integer32"""
    defaultValue = 0

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("exact", 1),
          ("extCommRt", 5),
          ("extCommSoo", 6),
          ("interfaceValue", 7),
          ("ipAddress", 8),
          ("notApplicable", 0),
          ("relativeNeg", 3),
          ("relativePos", 4))
    )


_JuniIpRouteMapClauseElemIdAddon_Type.__name__ = "Integer32"
_JuniIpRouteMapClauseElemIdAddon_Object = MibTableColumn
juniIpRouteMapClauseElemIdAddon = _JuniIpRouteMapClauseElemIdAddon_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 3, 1, 3),
    _JuniIpRouteMapClauseElemIdAddon_Type()
)
juniIpRouteMapClauseElemIdAddon.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpRouteMapClauseElemIdAddon.setStatus("current")


class _JuniIpRouteMapClauseElementValue_Type(DisplayString):
    """Custom type juniIpRouteMapClauseElementValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_JuniIpRouteMapClauseElementValue_Type.__name__ = "DisplayString"
_JuniIpRouteMapClauseElementValue_Object = MibTableColumn
juniIpRouteMapClauseElementValue = _JuniIpRouteMapClauseElementValue_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 3, 1, 4),
    _JuniIpRouteMapClauseElementValue_Type()
)
juniIpRouteMapClauseElementValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpRouteMapClauseElementValue.setStatus("current")
_JuniIpRouteMapClauseRowStatus_Type = RowStatus
_JuniIpRouteMapClauseRowStatus_Object = MibTableColumn
juniIpRouteMapClauseRowStatus = _JuniIpRouteMapClauseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 1, 8, 3, 1, 5),
    _JuniIpRouteMapClauseRowStatus_Type()
)
juniIpRouteMapClauseRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpRouteMapClauseRowStatus.setStatus("current")
_JuniIpPolicyConformance_ObjectIdentity = ObjectIdentity
juniIpPolicyConformance = _JuniIpPolicyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4)
)
_JuniIpPolicyCompliances_ObjectIdentity = ObjectIdentity
juniIpPolicyCompliances = _JuniIpPolicyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 1)
)
_JuniIpPolicyGroups_ObjectIdentity = ObjectIdentity
juniIpPolicyGroups = _JuniIpPolicyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 2)
)

# Managed Objects groups

juniIpAccessListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 2, 1)
)
juniIpAccessListGroup.setObjects(
      *(("Juniper-IP-POLICY-MIB", "juniIpAccessListRowStatus"),
        ("Juniper-IP-POLICY-MIB", "juniIpAccessListAction"),
        ("Juniper-IP-POLICY-MIB", "juniIpAccessListSrc"),
        ("Juniper-IP-POLICY-MIB", "juniIpAccessListSrcMask"),
        ("Juniper-IP-POLICY-MIB", "juniIpAccessListDst"),
        ("Juniper-IP-POLICY-MIB", "juniIpAccessListDstMask"),
        ("Juniper-IP-POLICY-MIB", "juniIpAccessListProtocol"))
)
if mibBuilder.loadTexts:
    juniIpAccessListGroup.setStatus("current")

juniIpNamedAccessListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 2, 2)
)
juniIpNamedAccessListGroup.setObjects(
      *(("Juniper-IP-POLICY-MIB", "juniIpNamedAccessListRowStatus"),
        ("Juniper-IP-POLICY-MIB", "juniIpNamedAccessListAction"),
        ("Juniper-IP-POLICY-MIB", "juniIpNamedAccessListSrc"),
        ("Juniper-IP-POLICY-MIB", "juniIpNamedAccessListSrcMask"),
        ("Juniper-IP-POLICY-MIB", "juniIpNamedAccessListDst"),
        ("Juniper-IP-POLICY-MIB", "juniIpNamedAccessListDstMask"),
        ("Juniper-IP-POLICY-MIB", "juniIpNamedAccessListProtocol"))
)
if mibBuilder.loadTexts:
    juniIpNamedAccessListGroup.setStatus("current")

juniIpAspAccessListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 2, 3)
)
juniIpAspAccessListGroup.setObjects(
      *(("Juniper-IP-POLICY-MIB", "juniIpAspAccessCreatedInternally"),
        ("Juniper-IP-POLICY-MIB", "juniIpAspAccessPolicy"),
        ("Juniper-IP-POLICY-MIB", "juniIpAspAccessExpression"),
        ("Juniper-IP-POLICY-MIB", "juniIpAspAccessRowStatus"))
)
if mibBuilder.loadTexts:
    juniIpAspAccessListGroup.setStatus("current")

juniIpPrefixListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 2, 4)
)
juniIpPrefixListGroup.setObjects(
      *(("Juniper-IP-POLICY-MIB", "juniIpPrefixListPolicy"),
        ("Juniper-IP-POLICY-MIB", "juniIpPrefixListGeValue"),
        ("Juniper-IP-POLICY-MIB", "juniIpPrefixListLeValue"),
        ("Juniper-IP-POLICY-MIB", "juniIpPrefixListDescription"),
        ("Juniper-IP-POLICY-MIB", "juniIpPrefixListHitCount"),
        ("Juniper-IP-POLICY-MIB", "juniIpPrefixListRowStatus"))
)
if mibBuilder.loadTexts:
    juniIpPrefixListGroup.setStatus("current")

juniIpPrefixTreeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 2, 5)
)
juniIpPrefixTreeGroup.setObjects(
      *(("Juniper-IP-POLICY-MIB", "juniIpPrefixTreePolicy"),
        ("Juniper-IP-POLICY-MIB", "juniIpPrefixTreeDescription"),
        ("Juniper-IP-POLICY-MIB", "juniIpPrefixTreeHitCount"),
        ("Juniper-IP-POLICY-MIB", "juniIpPrefixTreeRowStatus"))
)
if mibBuilder.loadTexts:
    juniIpPrefixTreeGroup.setStatus("current")

juniIpCommunityListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 2, 6)
)
juniIpCommunityListGroup.setObjects(
      *(("Juniper-IP-POLICY-MIB", "juniIpCommunityListCreatedInternally"),
        ("Juniper-IP-POLICY-MIB", "juniIpCommunityListExtended"),
        ("Juniper-IP-POLICY-MIB", "juniIpCommunityListPolicy"),
        ("Juniper-IP-POLICY-MIB", "juniIpCommunityListExpression"),
        ("Juniper-IP-POLICY-MIB", "juniIpCommunityListRowStatus"))
)
if mibBuilder.loadTexts:
    juniIpCommunityListGroup.setStatus("current")

juniIpExtCommunityListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 2, 7)
)
juniIpExtCommunityListGroup.setObjects(
      *(("Juniper-IP-POLICY-MIB", "juniIpExtCommunityListCreatedInternally"),
        ("Juniper-IP-POLICY-MIB", "juniIpExtCommunityListPolicy"),
        ("Juniper-IP-POLICY-MIB", "juniIpExtCommunityListExpression"),
        ("Juniper-IP-POLICY-MIB", "juniIpExtCommunityListRowStatus"))
)
if mibBuilder.loadTexts:
    juniIpExtCommunityListGroup.setStatus("current")

juniIpRedistributeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 2, 8)
)
juniIpRedistributeGroup.setObjects(
      *(("Juniper-IP-POLICY-MIB", "juniIpDynRedistributeState"),
        ("Juniper-IP-POLICY-MIB", "juniIpDynRedistributeRowStatus"),
        ("Juniper-IP-POLICY-MIB", "juniIpRedistributeState"),
        ("Juniper-IP-POLICY-MIB", "juniIpRedistributeRouteMapName"),
        ("Juniper-IP-POLICY-MIB", "juniIpRedistributeRowStatus"))
)
if mibBuilder.loadTexts:
    juniIpRedistributeGroup.setStatus("current")

juniIpRouteMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 2, 9)
)
juniIpRouteMapGroup.setObjects(
      *(("Juniper-IP-POLICY-MIB", "juniIpRouteMapCreatedInternally"),
        ("Juniper-IP-POLICY-MIB", "juniIpRouteMapPolicy"),
        ("Juniper-IP-POLICY-MIB", "juniIpRouteMapDisplay"))
)
if mibBuilder.loadTexts:
    juniIpRouteMapGroup.setStatus("obsolete")

juniIpRouteMapGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 2, 10)
)
juniIpRouteMapGroup2.setObjects(
      *(("Juniper-IP-POLICY-MIB", "juniIpRouteMapCreatedInternally"),
        ("Juniper-IP-POLICY-MIB", "juniIpRouteMapPolicy"),
        ("Juniper-IP-POLICY-MIB", "juniIpRouteMapDisplay"),
        ("Juniper-IP-POLICY-MIB", "juniIpRouteMapV2Policy"),
        ("Juniper-IP-POLICY-MIB", "juniIpRouteMapV2RowStatus"),
        ("Juniper-IP-POLICY-MIB", "juniIpRouteMapClauseElemIdAddon"),
        ("Juniper-IP-POLICY-MIB", "juniIpRouteMapClauseElementValue"),
        ("Juniper-IP-POLICY-MIB", "juniIpRouteMapClauseRowStatus"))
)
if mibBuilder.loadTexts:
    juniIpRouteMapGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniIpPolicyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniIpPolicyCompliance.setStatus(
        "obsolete"
    )

juniIpPolicyCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniIpPolicyCompliance2.setStatus(
        "obsolete"
    )

juniIpPolicyCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 1, 3)
)
if mibBuilder.loadTexts:
    juniIpPolicyCompliance3.setStatus(
        "current"
    )

juniIpPolicyCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13, 4, 1, 4)
)
if mibBuilder.loadTexts:
    juniIpPolicyCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-IP-POLICY-MIB",
    **{"JuniIpPolicyName": JuniIpPolicyName,
       "JuniIpPolicyPolicy": JuniIpPolicyPolicy,
       "JuniIpDynRedistributeProtocol": JuniIpDynRedistributeProtocol,
       "JuniIpRedistributeProtocol": JuniIpRedistributeProtocol,
       "JuniIpPolicyAdminStatus": JuniIpPolicyAdminStatus,
       "JuniIpPolicyExtendedCommunity": JuniIpPolicyExtendedCommunity,
       "juniIpPolicyMIB": juniIpPolicyMIB,
       "juniIpPolicyObjects": juniIpPolicyObjects,
       "juniIpAccessList": juniIpAccessList,
       "juniIpAccessListTable": juniIpAccessListTable,
       "juniIpAccessListEntry": juniIpAccessListEntry,
       "juniIpAccessListId": juniIpAccessListId,
       "juniIpAccessListElemId": juniIpAccessListElemId,
       "juniIpAccessListRowStatus": juniIpAccessListRowStatus,
       "juniIpAccessListAction": juniIpAccessListAction,
       "juniIpAccessListSrc": juniIpAccessListSrc,
       "juniIpAccessListSrcMask": juniIpAccessListSrcMask,
       "juniIpAccessListDst": juniIpAccessListDst,
       "juniIpAccessListDstMask": juniIpAccessListDstMask,
       "juniIpAccessListProtocol": juniIpAccessListProtocol,
       "juniIpNamedAccessList": juniIpNamedAccessList,
       "juniIpNamedAccessListTable": juniIpNamedAccessListTable,
       "juniIpNamedAccessListEntry": juniIpNamedAccessListEntry,
       "juniIpNamedAccessListName": juniIpNamedAccessListName,
       "juniIpNamedAccessListElemId": juniIpNamedAccessListElemId,
       "juniIpNamedAccessListRowStatus": juniIpNamedAccessListRowStatus,
       "juniIpNamedAccessListAction": juniIpNamedAccessListAction,
       "juniIpNamedAccessListSrc": juniIpNamedAccessListSrc,
       "juniIpNamedAccessListSrcMask": juniIpNamedAccessListSrcMask,
       "juniIpNamedAccessListDst": juniIpNamedAccessListDst,
       "juniIpNamedAccessListDstMask": juniIpNamedAccessListDstMask,
       "juniIpNamedAccessListProtocol": juniIpNamedAccessListProtocol,
       "juniIpAspAccessList": juniIpAspAccessList,
       "juniIpAspAccessTable": juniIpAspAccessTable,
       "juniIpAspAccessEntry": juniIpAspAccessEntry,
       "juniIpAspAccessName": juniIpAspAccessName,
       "juniIpAspAccessElemId": juniIpAspAccessElemId,
       "juniIpAspAccessCreatedInternally": juniIpAspAccessCreatedInternally,
       "juniIpAspAccessPolicy": juniIpAspAccessPolicy,
       "juniIpAspAccessExpression": juniIpAspAccessExpression,
       "juniIpAspAccessRowStatus": juniIpAspAccessRowStatus,
       "juniIpPrefixList": juniIpPrefixList,
       "juniIpPrefixListTable": juniIpPrefixListTable,
       "juniIpPrefixListEntry": juniIpPrefixListEntry,
       "juniIpPrefixListName": juniIpPrefixListName,
       "juniIpPrefixListElemId": juniIpPrefixListElemId,
       "juniIpPrefixListIpAddress": juniIpPrefixListIpAddress,
       "juniIpPrefixListLength": juniIpPrefixListLength,
       "juniIpPrefixListPolicy": juniIpPrefixListPolicy,
       "juniIpPrefixListGeValue": juniIpPrefixListGeValue,
       "juniIpPrefixListLeValue": juniIpPrefixListLeValue,
       "juniIpPrefixListDescription": juniIpPrefixListDescription,
       "juniIpPrefixListHitCount": juniIpPrefixListHitCount,
       "juniIpPrefixListRowStatus": juniIpPrefixListRowStatus,
       "juniIpPrefixTree": juniIpPrefixTree,
       "juniIpPrefixTreeTable": juniIpPrefixTreeTable,
       "juniIpPrefixTreeEntry": juniIpPrefixTreeEntry,
       "juniIpPrefixTreeName": juniIpPrefixTreeName,
       "juniIpPrefixTreeIpAddress": juniIpPrefixTreeIpAddress,
       "juniIpPrefixTreeLength": juniIpPrefixTreeLength,
       "juniIpPrefixTreePolicy": juniIpPrefixTreePolicy,
       "juniIpPrefixTreeDescription": juniIpPrefixTreeDescription,
       "juniIpPrefixTreeHitCount": juniIpPrefixTreeHitCount,
       "juniIpPrefixTreeRowStatus": juniIpPrefixTreeRowStatus,
       "juniIpCommunityList": juniIpCommunityList,
       "juniIpCommunityListTable": juniIpCommunityListTable,
       "juniIpCommunityListEntry": juniIpCommunityListEntry,
       "juniIpCommunityListName": juniIpCommunityListName,
       "juniIpCommunityListElemId": juniIpCommunityListElemId,
       "juniIpCommunityListCreatedInternally": juniIpCommunityListCreatedInternally,
       "juniIpCommunityListExtended": juniIpCommunityListExtended,
       "juniIpCommunityListPolicy": juniIpCommunityListPolicy,
       "juniIpCommunityListExpression": juniIpCommunityListExpression,
       "juniIpCommunityListRowStatus": juniIpCommunityListRowStatus,
       "juniIpExtCommunityListTable": juniIpExtCommunityListTable,
       "juniIpExtCommunityListEntry": juniIpExtCommunityListEntry,
       "juniIpExtCommunityListName": juniIpExtCommunityListName,
       "juniIpExtCommunityListElemId": juniIpExtCommunityListElemId,
       "juniIpExtCommunityListCreatedInternally": juniIpExtCommunityListCreatedInternally,
       "juniIpExtCommunityListPolicy": juniIpExtCommunityListPolicy,
       "juniIpExtCommunityListExpression": juniIpExtCommunityListExpression,
       "juniIpExtCommunityListRowStatus": juniIpExtCommunityListRowStatus,
       "juniIpRedistributeList": juniIpRedistributeList,
       "juniIpDynRedistributeTable": juniIpDynRedistributeTable,
       "juniIpDynRedistributeEntry": juniIpDynRedistributeEntry,
       "juniIpDynRedistributeToProtocol": juniIpDynRedistributeToProtocol,
       "juniIpDynRedistributeState": juniIpDynRedistributeState,
       "juniIpDynRedistributeRowStatus": juniIpDynRedistributeRowStatus,
       "juniIpRedistributeTable": juniIpRedistributeTable,
       "juniIpRedistributeEntry": juniIpRedistributeEntry,
       "juniIpRedistributeToProtocol": juniIpRedistributeToProtocol,
       "juniIpRedistributeFromProtocol": juniIpRedistributeFromProtocol,
       "juniIpRedistributeState": juniIpRedistributeState,
       "juniIpRedistributeRouteMapName": juniIpRedistributeRouteMapName,
       "juniIpRedistributeRowStatus": juniIpRedistributeRowStatus,
       "juniIpRouteMapTree": juniIpRouteMapTree,
       "juniIpRouteMapTable": juniIpRouteMapTable,
       "juniIpRouteMapEntry": juniIpRouteMapEntry,
       "juniIpRouteMapName": juniIpRouteMapName,
       "juniIpRouteMapSequenceNum": juniIpRouteMapSequenceNum,
       "juniIpRouteMapElemId": juniIpRouteMapElemId,
       "juniIpRouteMapSubElemId": juniIpRouteMapSubElemId,
       "juniIpRouteMapCreatedInternally": juniIpRouteMapCreatedInternally,
       "juniIpRouteMapPolicy": juniIpRouteMapPolicy,
       "juniIpRouteMapDisplay": juniIpRouteMapDisplay,
       "juniIpRouteMapV2Table": juniIpRouteMapV2Table,
       "juniIpRouteMapV2Entry": juniIpRouteMapV2Entry,
       "juniIpRouteMapV2Name": juniIpRouteMapV2Name,
       "juniIpRouteMapV2SequenceNum": juniIpRouteMapV2SequenceNum,
       "juniIpRouteMapV2Policy": juniIpRouteMapV2Policy,
       "juniIpRouteMapV2RowStatus": juniIpRouteMapV2RowStatus,
       "juniIpRouteMapClauseTable": juniIpRouteMapClauseTable,
       "juniIpRouteMapClauseEntry": juniIpRouteMapClauseEntry,
       "juniIpRouteMapClauseElemId": juniIpRouteMapClauseElemId,
       "juniIpRouteMapClauseSubElemId": juniIpRouteMapClauseSubElemId,
       "juniIpRouteMapClauseElemIdAddon": juniIpRouteMapClauseElemIdAddon,
       "juniIpRouteMapClauseElementValue": juniIpRouteMapClauseElementValue,
       "juniIpRouteMapClauseRowStatus": juniIpRouteMapClauseRowStatus,
       "juniIpPolicyConformance": juniIpPolicyConformance,
       "juniIpPolicyCompliances": juniIpPolicyCompliances,
       "juniIpPolicyCompliance": juniIpPolicyCompliance,
       "juniIpPolicyCompliance2": juniIpPolicyCompliance2,
       "juniIpPolicyCompliance3": juniIpPolicyCompliance3,
       "juniIpPolicyCompliance4": juniIpPolicyCompliance4,
       "juniIpPolicyGroups": juniIpPolicyGroups,
       "juniIpAccessListGroup": juniIpAccessListGroup,
       "juniIpNamedAccessListGroup": juniIpNamedAccessListGroup,
       "juniIpAspAccessListGroup": juniIpAspAccessListGroup,
       "juniIpPrefixListGroup": juniIpPrefixListGroup,
       "juniIpPrefixTreeGroup": juniIpPrefixTreeGroup,
       "juniIpCommunityListGroup": juniIpCommunityListGroup,
       "juniIpExtCommunityListGroup": juniIpExtCommunityListGroup,
       "juniIpRedistributeGroup": juniIpRedistributeGroup,
       "juniIpRouteMapGroup": juniIpRouteMapGroup,
       "juniIpRouteMapGroup2": juniIpRouteMapGroup2}
)
