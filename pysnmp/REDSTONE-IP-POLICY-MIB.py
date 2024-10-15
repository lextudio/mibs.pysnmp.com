# SNMP MIB module (REDSTONE-IP-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDSTONE-IP-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:41 2024
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

(rsMgmt,) = mibBuilder.importSymbols(
    "REDSTONE-SMI",
    "rsMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rsIpPolicyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 13)
)
rsIpPolicyMIB.setRevisions(
        ("1998-01-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsIpPolicyObjects_ObjectIdentity = ObjectIdentity
rsIpPolicyObjects = _RsIpPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 13, 1)
)
_RsIpAccessList_ObjectIdentity = ObjectIdentity
rsIpAccessList = _RsIpAccessList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1)
)
_RsIpAccessListTable_Object = MibTable
rsIpAccessListTable = _RsIpAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rsIpAccessListTable.setStatus("current")
_RsIpAccessListEntry_Object = MibTableRow
rsIpAccessListEntry = _RsIpAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1)
)
rsIpAccessListEntry.setIndexNames(
    (0, "REDSTONE-IP-POLICY-MIB", "rsIpAccessListId"),
    (0, "REDSTONE-IP-POLICY-MIB", "rsIpAccessListElemId"),
)
if mibBuilder.loadTexts:
    rsIpAccessListEntry.setStatus("current")


class _RsIpAccessListId_Type(Integer32):
    """Custom type rsIpAccessListId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 199),
    )


_RsIpAccessListId_Type.__name__ = "Integer32"
_RsIpAccessListId_Object = MibTableColumn
rsIpAccessListId = _RsIpAccessListId_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 1),
    _RsIpAccessListId_Type()
)
rsIpAccessListId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsIpAccessListId.setStatus("current")


class _RsIpAccessListElemId_Type(Integer32):
    """Custom type rsIpAccessListElemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_RsIpAccessListElemId_Type.__name__ = "Integer32"
_RsIpAccessListElemId_Object = MibTableColumn
rsIpAccessListElemId = _RsIpAccessListElemId_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 2),
    _RsIpAccessListElemId_Type()
)
rsIpAccessListElemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsIpAccessListElemId.setStatus("current")
_RsIpAccessListRowStatus_Type = RowStatus
_RsIpAccessListRowStatus_Object = MibTableColumn
rsIpAccessListRowStatus = _RsIpAccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 3),
    _RsIpAccessListRowStatus_Type()
)
rsIpAccessListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpAccessListRowStatus.setStatus("current")


class _RsIpAccessListAction_Type(Integer32):
    """Custom type rsIpAccessListAction based on Integer32"""
    defaultValue = 0

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


_RsIpAccessListAction_Type.__name__ = "Integer32"
_RsIpAccessListAction_Object = MibTableColumn
rsIpAccessListAction = _RsIpAccessListAction_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 4),
    _RsIpAccessListAction_Type()
)
rsIpAccessListAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpAccessListAction.setStatus("current")


class _RsIpAccessListSrc_Type(IpAddress):
    """Custom type rsIpAccessListSrc based on IpAddress"""
    defaultHexValue = "00000000"


_RsIpAccessListSrc_Object = MibTableColumn
rsIpAccessListSrc = _RsIpAccessListSrc_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 5),
    _RsIpAccessListSrc_Type()
)
rsIpAccessListSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpAccessListSrc.setStatus("current")


class _RsIpAccessListSrcMask_Type(IpAddress):
    """Custom type rsIpAccessListSrcMask based on IpAddress"""
    defaultHexValue = "00000000"


_RsIpAccessListSrcMask_Object = MibTableColumn
rsIpAccessListSrcMask = _RsIpAccessListSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 6),
    _RsIpAccessListSrcMask_Type()
)
rsIpAccessListSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpAccessListSrcMask.setStatus("current")


class _RsIpAccessListDst_Type(IpAddress):
    """Custom type rsIpAccessListDst based on IpAddress"""
    defaultHexValue = "00000000"


_RsIpAccessListDst_Object = MibTableColumn
rsIpAccessListDst = _RsIpAccessListDst_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 7),
    _RsIpAccessListDst_Type()
)
rsIpAccessListDst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpAccessListDst.setStatus("current")


class _RsIpAccessListDstMask_Type(IpAddress):
    """Custom type rsIpAccessListDstMask based on IpAddress"""
    defaultHexValue = "00000000"


_RsIpAccessListDstMask_Object = MibTableColumn
rsIpAccessListDstMask = _RsIpAccessListDstMask_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 8),
    _RsIpAccessListDstMask_Type()
)
rsIpAccessListDstMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpAccessListDstMask.setStatus("current")


class _RsIpAccessListProtocol_Type(Integer32):
    """Custom type rsIpAccessListProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RsIpAccessListProtocol_Type.__name__ = "Integer32"
_RsIpAccessListProtocol_Object = MibTableColumn
rsIpAccessListProtocol = _RsIpAccessListProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 9),
    _RsIpAccessListProtocol_Type()
)
rsIpAccessListProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpAccessListProtocol.setStatus("current")
_RsIpPolicyConformance_ObjectIdentity = ObjectIdentity
rsIpPolicyConformance = _RsIpPolicyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 13, 4)
)
_RsIpPolicyCompliances_ObjectIdentity = ObjectIdentity
rsIpPolicyCompliances = _RsIpPolicyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 13, 4, 1)
)
_RsIpPolicyGroups_ObjectIdentity = ObjectIdentity
rsIpPolicyGroups = _RsIpPolicyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 13, 4, 2)
)

# Managed Objects groups

rsIpAccessListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 13, 4, 2, 1)
)
rsIpAccessListGroup.setObjects(
      *(("REDSTONE-IP-POLICY-MIB", "rsIpAccessListRowStatus"),
        ("REDSTONE-IP-POLICY-MIB", "rsIpAccessListAction"),
        ("REDSTONE-IP-POLICY-MIB", "rsIpAccessListSrc"),
        ("REDSTONE-IP-POLICY-MIB", "rsIpAccessListSrcMask"),
        ("REDSTONE-IP-POLICY-MIB", "rsIpAccessListDst"),
        ("REDSTONE-IP-POLICY-MIB", "rsIpAccessListDstMask"),
        ("REDSTONE-IP-POLICY-MIB", "rsIpAccessListProtocol"))
)
if mibBuilder.loadTexts:
    rsIpAccessListGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsIpPolicyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2773, 2, 13, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rsIpPolicyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDSTONE-IP-POLICY-MIB",
    **{"rsIpPolicyMIB": rsIpPolicyMIB,
       "rsIpPolicyObjects": rsIpPolicyObjects,
       "rsIpAccessList": rsIpAccessList,
       "rsIpAccessListTable": rsIpAccessListTable,
       "rsIpAccessListEntry": rsIpAccessListEntry,
       "rsIpAccessListId": rsIpAccessListId,
       "rsIpAccessListElemId": rsIpAccessListElemId,
       "rsIpAccessListRowStatus": rsIpAccessListRowStatus,
       "rsIpAccessListAction": rsIpAccessListAction,
       "rsIpAccessListSrc": rsIpAccessListSrc,
       "rsIpAccessListSrcMask": rsIpAccessListSrcMask,
       "rsIpAccessListDst": rsIpAccessListDst,
       "rsIpAccessListDstMask": rsIpAccessListDstMask,
       "rsIpAccessListProtocol": rsIpAccessListProtocol,
       "rsIpPolicyConformance": rsIpPolicyConformance,
       "rsIpPolicyCompliances": rsIpPolicyCompliances,
       "rsIpPolicyCompliance": rsIpPolicyCompliance,
       "rsIpPolicyGroups": rsIpPolicyGroups,
       "rsIpAccessListGroup": rsIpAccessListGroup}
)
