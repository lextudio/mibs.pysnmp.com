# SNMP MIB module (HUAWEI-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-ACL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:43 2024
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

(huaweiMgmt,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "huaweiMgmt")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwAcl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1)
)
hwAcl.setRevisions(
        ("2015-02-27 21:00",
         "2015-02-07 21:00",
         "2014-10-28 21:00",
         "2014-06-20 09:48",
         "2014-04-09 09:48",
         "2014-03-26 09:26",
         "2014-01-17 13:38",
         "2013-11-28 21:00",
         "2013-10-28 19:00",
         "2013-09-05 00:00",
         "2014-08-05 16:06")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwAclMibObjects_ObjectIdentity = ObjectIdentity
hwAclMibObjects = _HwAclMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1)
)
_HwAclNumGroupTable_Object = MibTable
hwAclNumGroupTable = _HwAclNumGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hwAclNumGroupTable.setStatus("current")
_HwAclNumGroupEntry_Object = MibTableRow
hwAclNumGroupEntry = _HwAclNumGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 2, 1)
)
hwAclNumGroupEntry.setIndexNames(
    (0, "HUAWEI-ACL-MIB", "hwAclNumGroupAclNum"),
)
if mibBuilder.loadTexts:
    hwAclNumGroupEntry.setStatus("current")
_HwAclNumGroupAclNum_Type = Integer32
_HwAclNumGroupAclNum_Object = MibTableColumn
hwAclNumGroupAclNum = _HwAclNumGroupAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 2, 1, 1),
    _HwAclNumGroupAclNum_Type()
)
hwAclNumGroupAclNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclNumGroupAclNum.setStatus("current")


class _HwAclNumGroupMatchOrder_Type(Integer32):
    """Custom type hwAclNumGroupMatchOrder based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("config", 1))
    )


_HwAclNumGroupMatchOrder_Type.__name__ = "Integer32"
_HwAclNumGroupMatchOrder_Object = MibTableColumn
hwAclNumGroupMatchOrder = _HwAclNumGroupMatchOrder_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 2, 1, 2),
    _HwAclNumGroupMatchOrder_Type()
)
hwAclNumGroupMatchOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclNumGroupMatchOrder.setStatus("current")
_HwAclNumGroupSubitemNum_Type = Counter32
_HwAclNumGroupSubitemNum_Object = MibTableColumn
hwAclNumGroupSubitemNum = _HwAclNumGroupSubitemNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 2, 1, 3),
    _HwAclNumGroupSubitemNum_Type()
)
hwAclNumGroupSubitemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclNumGroupSubitemNum.setStatus("current")


class _HwAclNumGroupStep_Type(Integer32):
    """Custom type hwAclNumGroupStep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_HwAclNumGroupStep_Type.__name__ = "Integer32"
_HwAclNumGroupStep_Object = MibTableColumn
hwAclNumGroupStep = _HwAclNumGroupStep_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 2, 1, 4),
    _HwAclNumGroupStep_Type()
)
hwAclNumGroupStep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclNumGroupStep.setStatus("current")


class _HwAclNumGroupDescription_Type(OctetString):
    """Custom type hwAclNumGroupDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HwAclNumGroupDescription_Type.__name__ = "OctetString"
_HwAclNumGroupDescription_Object = MibTableColumn
hwAclNumGroupDescription = _HwAclNumGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 2, 1, 5),
    _HwAclNumGroupDescription_Type()
)
hwAclNumGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclNumGroupDescription.setStatus("current")


class _HwAclNumGroupCountClear_Type(Integer32):
    """Custom type hwAclNumGroupCountClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("notUsed", 2))
    )


_HwAclNumGroupCountClear_Type.__name__ = "Integer32"
_HwAclNumGroupCountClear_Object = MibTableColumn
hwAclNumGroupCountClear = _HwAclNumGroupCountClear_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 2, 1, 6),
    _HwAclNumGroupCountClear_Type()
)
hwAclNumGroupCountClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclNumGroupCountClear.setStatus("current")
_HwAclNumGroupRowStatus_Type = RowStatus
_HwAclNumGroupRowStatus_Object = MibTableColumn
hwAclNumGroupRowStatus = _HwAclNumGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 2, 1, 7),
    _HwAclNumGroupRowStatus_Type()
)
hwAclNumGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclNumGroupRowStatus.setStatus("current")


class _HwAclNumGroupAclName_Type(OctetString):
    """Custom type hwAclNumGroupAclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwAclNumGroupAclName_Type.__name__ = "OctetString"
_HwAclNumGroupAclName_Object = MibTableColumn
hwAclNumGroupAclName = _HwAclNumGroupAclName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 2, 1, 8),
    _HwAclNumGroupAclName_Type()
)
hwAclNumGroupAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclNumGroupAclName.setStatus("current")


class _HwAclNumGroupAclType_Type(Integer32):
    """Custom type hwAclNumGroupAclType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("advanced", 2),
          ("basic", 1),
          ("interface", 5),
          ("link", 3),
          ("mac", 7),
          ("mpls", 6),
          ("ucl", 8),
          ("user", 4))
    )


_HwAclNumGroupAclType_Type.__name__ = "Integer32"
_HwAclNumGroupAclType_Object = MibTableColumn
hwAclNumGroupAclType = _HwAclNumGroupAclType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 2, 1, 9),
    _HwAclNumGroupAclType_Type()
)
hwAclNumGroupAclType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclNumGroupAclType.setStatus("current")
_HwAclBasicRuleTable_Object = MibTable
hwAclBasicRuleTable = _HwAclBasicRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hwAclBasicRuleTable.setStatus("current")
_HwAclBasicRuleEntry_Object = MibTableRow
hwAclBasicRuleEntry = _HwAclBasicRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 4, 1)
)
hwAclBasicRuleEntry.setIndexNames(
    (0, "HUAWEI-ACL-MIB", "hwAclBasicAclNum"),
    (0, "HUAWEI-ACL-MIB", "hwAclBasicSubitem"),
)
if mibBuilder.loadTexts:
    hwAclBasicRuleEntry.setStatus("current")
_HwAclBasicAclNum_Type = Integer32
_HwAclBasicAclNum_Object = MibTableColumn
hwAclBasicAclNum = _HwAclBasicAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 4, 1, 1),
    _HwAclBasicAclNum_Type()
)
hwAclBasicAclNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclBasicAclNum.setStatus("current")
_HwAclBasicSubitem_Type = Unsigned32
_HwAclBasicSubitem_Object = MibTableColumn
hwAclBasicSubitem = _HwAclBasicSubitem_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 4, 1, 2),
    _HwAclBasicSubitem_Type()
)
hwAclBasicSubitem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclBasicSubitem.setStatus("current")


class _HwAclBasicAct_Type(Integer32):
    """Custom type hwAclBasicAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_HwAclBasicAct_Type.__name__ = "Integer32"
_HwAclBasicAct_Object = MibTableColumn
hwAclBasicAct = _HwAclBasicAct_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 4, 1, 3),
    _HwAclBasicAct_Type()
)
hwAclBasicAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclBasicAct.setStatus("current")
_HwAclBasicSrcIp_Type = IpAddress
_HwAclBasicSrcIp_Object = MibTableColumn
hwAclBasicSrcIp = _HwAclBasicSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 4, 1, 4),
    _HwAclBasicSrcIp_Type()
)
hwAclBasicSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclBasicSrcIp.setStatus("current")
_HwAclBasicSrcWild_Type = IpAddress
_HwAclBasicSrcWild_Object = MibTableColumn
hwAclBasicSrcWild = _HwAclBasicSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 4, 1, 5),
    _HwAclBasicSrcWild_Type()
)
hwAclBasicSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclBasicSrcWild.setStatus("current")


class _HwAclBasicTimeRangeIndex_Type(Integer32):
    """Custom type hwAclBasicTimeRangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_HwAclBasicTimeRangeIndex_Type.__name__ = "Integer32"
_HwAclBasicTimeRangeIndex_Object = MibTableColumn
hwAclBasicTimeRangeIndex = _HwAclBasicTimeRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 4, 1, 6),
    _HwAclBasicTimeRangeIndex_Type()
)
hwAclBasicTimeRangeIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclBasicTimeRangeIndex.setStatus("current")


class _HwAclBasicFragments_Type(Integer32):
    """Custom type hwAclBasicFragments based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fragment", 1),
          ("fragmentSpeFirst", 4),
          ("fragmentSubseq", 0),
          ("nonFragment", 2),
          ("nonSubseq", 3),
          ("none", 255))
    )


_HwAclBasicFragments_Type.__name__ = "Integer32"
_HwAclBasicFragments_Object = MibTableColumn
hwAclBasicFragments = _HwAclBasicFragments_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 4, 1, 7),
    _HwAclBasicFragments_Type()
)
hwAclBasicFragments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclBasicFragments.setStatus("current")
_HwAclBasicLog_Type = TruthValue
_HwAclBasicLog_Object = MibTableColumn
hwAclBasicLog = _HwAclBasicLog_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 4, 1, 8),
    _HwAclBasicLog_Type()
)
hwAclBasicLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclBasicLog.setStatus("current")
_HwAclBasicEnable_Type = TruthValue
_HwAclBasicEnable_Object = MibTableColumn
hwAclBasicEnable = _HwAclBasicEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 4, 1, 9),
    _HwAclBasicEnable_Type()
)
hwAclBasicEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclBasicEnable.setStatus("current")
_HwAclBasicCount_Type = Counter64
_HwAclBasicCount_Object = MibTableColumn
hwAclBasicCount = _HwAclBasicCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 4, 1, 10),
    _HwAclBasicCount_Type()
)
hwAclBasicCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclBasicCount.setStatus("current")


class _HwAclBasicVrfName_Type(OctetString):
    """Custom type hwAclBasicVrfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwAclBasicVrfName_Type.__name__ = "OctetString"
_HwAclBasicVrfName_Object = MibTableColumn
hwAclBasicVrfName = _HwAclBasicVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 4, 1, 11),
    _HwAclBasicVrfName_Type()
)
hwAclBasicVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclBasicVrfName.setStatus("current")
_HwAclBasicRowStatus_Type = RowStatus
_HwAclBasicRowStatus_Object = MibTableColumn
hwAclBasicRowStatus = _HwAclBasicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 4, 1, 12),
    _HwAclBasicRowStatus_Type()
)
hwAclBasicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclBasicRowStatus.setStatus("current")


class _HwAclBasicDescription_Type(OctetString):
    """Custom type hwAclBasicDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HwAclBasicDescription_Type.__name__ = "OctetString"
_HwAclBasicDescription_Object = MibTableColumn
hwAclBasicDescription = _HwAclBasicDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 4, 1, 13),
    _HwAclBasicDescription_Type()
)
hwAclBasicDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclBasicDescription.setStatus("current")
_HwAclAdvancedRuleTable_Object = MibTable
hwAclAdvancedRuleTable = _HwAclAdvancedRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hwAclAdvancedRuleTable.setStatus("current")
_HwAclAdvancedRuleEntry_Object = MibTableRow
hwAclAdvancedRuleEntry = _HwAclAdvancedRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1)
)
hwAclAdvancedRuleEntry.setIndexNames(
    (0, "HUAWEI-ACL-MIB", "hwAclAdvancedAclNum"),
    (0, "HUAWEI-ACL-MIB", "hwAclAdvancedSubitem"),
)
if mibBuilder.loadTexts:
    hwAclAdvancedRuleEntry.setStatus("current")
_HwAclAdvancedAclNum_Type = Integer32
_HwAclAdvancedAclNum_Object = MibTableColumn
hwAclAdvancedAclNum = _HwAclAdvancedAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 1),
    _HwAclAdvancedAclNum_Type()
)
hwAclAdvancedAclNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclAdvancedAclNum.setStatus("current")
_HwAclAdvancedSubitem_Type = Unsigned32
_HwAclAdvancedSubitem_Object = MibTableColumn
hwAclAdvancedSubitem = _HwAclAdvancedSubitem_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 2),
    _HwAclAdvancedSubitem_Type()
)
hwAclAdvancedSubitem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclAdvancedSubitem.setStatus("current")


class _HwAclAdvancedAct_Type(Integer32):
    """Custom type hwAclAdvancedAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_HwAclAdvancedAct_Type.__name__ = "Integer32"
_HwAclAdvancedAct_Object = MibTableColumn
hwAclAdvancedAct = _HwAclAdvancedAct_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 3),
    _HwAclAdvancedAct_Type()
)
hwAclAdvancedAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedAct.setStatus("current")


class _HwAclAdvancedProtocol_Type(Integer32):
    """Custom type hwAclAdvancedProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwAclAdvancedProtocol_Type.__name__ = "Integer32"
_HwAclAdvancedProtocol_Object = MibTableColumn
hwAclAdvancedProtocol = _HwAclAdvancedProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 4),
    _HwAclAdvancedProtocol_Type()
)
hwAclAdvancedProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedProtocol.setStatus("current")
_HwAclAdvancedSrcIp_Type = IpAddress
_HwAclAdvancedSrcIp_Object = MibTableColumn
hwAclAdvancedSrcIp = _HwAclAdvancedSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 5),
    _HwAclAdvancedSrcIp_Type()
)
hwAclAdvancedSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedSrcIp.setStatus("current")
_HwAclAdvancedSrcWild_Type = IpAddress
_HwAclAdvancedSrcWild_Object = MibTableColumn
hwAclAdvancedSrcWild = _HwAclAdvancedSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 6),
    _HwAclAdvancedSrcWild_Type()
)
hwAclAdvancedSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedSrcWild.setStatus("current")


class _HwAclAdvancedSrcOp_Type(Integer32):
    """Custom type hwAclAdvancedSrcOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("eq", 2),
          ("gt", 3),
          ("invalid", 0),
          ("lt", 1),
          ("neq", 4),
          ("range", 5))
    )


_HwAclAdvancedSrcOp_Type.__name__ = "Integer32"
_HwAclAdvancedSrcOp_Object = MibTableColumn
hwAclAdvancedSrcOp = _HwAclAdvancedSrcOp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 7),
    _HwAclAdvancedSrcOp_Type()
)
hwAclAdvancedSrcOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedSrcOp.setStatus("current")


class _HwAclAdvancedSrcPort1_Type(Integer32):
    """Custom type hwAclAdvancedSrcPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwAclAdvancedSrcPort1_Type.__name__ = "Integer32"
_HwAclAdvancedSrcPort1_Object = MibTableColumn
hwAclAdvancedSrcPort1 = _HwAclAdvancedSrcPort1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 8),
    _HwAclAdvancedSrcPort1_Type()
)
hwAclAdvancedSrcPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedSrcPort1.setStatus("current")


class _HwAclAdvancedSrcPort2_Type(Integer32):
    """Custom type hwAclAdvancedSrcPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwAclAdvancedSrcPort2_Type.__name__ = "Integer32"
_HwAclAdvancedSrcPort2_Object = MibTableColumn
hwAclAdvancedSrcPort2 = _HwAclAdvancedSrcPort2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 9),
    _HwAclAdvancedSrcPort2_Type()
)
hwAclAdvancedSrcPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedSrcPort2.setStatus("current")
_HwAclAdvancedDestIp_Type = IpAddress
_HwAclAdvancedDestIp_Object = MibTableColumn
hwAclAdvancedDestIp = _HwAclAdvancedDestIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 10),
    _HwAclAdvancedDestIp_Type()
)
hwAclAdvancedDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedDestIp.setStatus("current")
_HwAclAdvancedDestWild_Type = IpAddress
_HwAclAdvancedDestWild_Object = MibTableColumn
hwAclAdvancedDestWild = _HwAclAdvancedDestWild_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 11),
    _HwAclAdvancedDestWild_Type()
)
hwAclAdvancedDestWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedDestWild.setStatus("current")


class _HwAclAdvancedDestOp_Type(Integer32):
    """Custom type hwAclAdvancedDestOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("eq", 2),
          ("gt", 3),
          ("invalid", 0),
          ("lt", 1),
          ("neq", 4),
          ("range", 5))
    )


_HwAclAdvancedDestOp_Type.__name__ = "Integer32"
_HwAclAdvancedDestOp_Object = MibTableColumn
hwAclAdvancedDestOp = _HwAclAdvancedDestOp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 12),
    _HwAclAdvancedDestOp_Type()
)
hwAclAdvancedDestOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedDestOp.setStatus("current")


class _HwAclAdvancedDestPort1_Type(Integer32):
    """Custom type hwAclAdvancedDestPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwAclAdvancedDestPort1_Type.__name__ = "Integer32"
_HwAclAdvancedDestPort1_Object = MibTableColumn
hwAclAdvancedDestPort1 = _HwAclAdvancedDestPort1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 13),
    _HwAclAdvancedDestPort1_Type()
)
hwAclAdvancedDestPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedDestPort1.setStatus("current")


class _HwAclAdvancedDestPort2_Type(Integer32):
    """Custom type hwAclAdvancedDestPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwAclAdvancedDestPort2_Type.__name__ = "Integer32"
_HwAclAdvancedDestPort2_Object = MibTableColumn
hwAclAdvancedDestPort2 = _HwAclAdvancedDestPort2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 14),
    _HwAclAdvancedDestPort2_Type()
)
hwAclAdvancedDestPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedDestPort2.setStatus("current")


class _HwAclAdvancedPrecedence_Type(Integer32):
    """Custom type hwAclAdvancedPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwAclAdvancedPrecedence_Type.__name__ = "Integer32"
_HwAclAdvancedPrecedence_Object = MibTableColumn
hwAclAdvancedPrecedence = _HwAclAdvancedPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 15),
    _HwAclAdvancedPrecedence_Type()
)
hwAclAdvancedPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedPrecedence.setStatus("current")


class _HwAclAdvancedTos_Type(Integer32):
    """Custom type hwAclAdvancedTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(255, 255),
    )


_HwAclAdvancedTos_Type.__name__ = "Integer32"
_HwAclAdvancedTos_Object = MibTableColumn
hwAclAdvancedTos = _HwAclAdvancedTos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 16),
    _HwAclAdvancedTos_Type()
)
hwAclAdvancedTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedTos.setStatus("current")


class _HwAclAdvancedDscp_Type(Integer32):
    """Custom type hwAclAdvancedDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HwAclAdvancedDscp_Type.__name__ = "Integer32"
_HwAclAdvancedDscp_Object = MibTableColumn
hwAclAdvancedDscp = _HwAclAdvancedDscp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 17),
    _HwAclAdvancedDscp_Type()
)
hwAclAdvancedDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedDscp.setStatus("current")


class _HwAclAdvancedEstablish_Type(TruthValue):
    """Custom type hwAclAdvancedEstablish based on TruthValue"""


_HwAclAdvancedEstablish_Object = MibTableColumn
hwAclAdvancedEstablish = _HwAclAdvancedEstablish_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 18),
    _HwAclAdvancedEstablish_Type()
)
hwAclAdvancedEstablish.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedEstablish.setStatus("current")


class _HwAclAdvancedTimeRangeIndex_Type(Integer32):
    """Custom type hwAclAdvancedTimeRangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_HwAclAdvancedTimeRangeIndex_Type.__name__ = "Integer32"
_HwAclAdvancedTimeRangeIndex_Object = MibTableColumn
hwAclAdvancedTimeRangeIndex = _HwAclAdvancedTimeRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 19),
    _HwAclAdvancedTimeRangeIndex_Type()
)
hwAclAdvancedTimeRangeIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedTimeRangeIndex.setStatus("current")


class _HwAclAdvancedIcmpType_Type(Integer32):
    """Custom type hwAclAdvancedIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HwAclAdvancedIcmpType_Type.__name__ = "Integer32"
_HwAclAdvancedIcmpType_Object = MibTableColumn
hwAclAdvancedIcmpType = _HwAclAdvancedIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 20),
    _HwAclAdvancedIcmpType_Type()
)
hwAclAdvancedIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedIcmpType.setStatus("current")


class _HwAclAdvancedIcmpCode_Type(Integer32):
    """Custom type hwAclAdvancedIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HwAclAdvancedIcmpCode_Type.__name__ = "Integer32"
_HwAclAdvancedIcmpCode_Object = MibTableColumn
hwAclAdvancedIcmpCode = _HwAclAdvancedIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 21),
    _HwAclAdvancedIcmpCode_Type()
)
hwAclAdvancedIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedIcmpCode.setStatus("current")


class _HwAclAdvancedFragments_Type(Integer32):
    """Custom type hwAclAdvancedFragments based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fragment", 1),
          ("fragmentSpeFirst", 4),
          ("fragmentSubseq", 0),
          ("nonFragment", 2),
          ("nonSubseq", 3),
          ("none", 255))
    )


_HwAclAdvancedFragments_Type.__name__ = "Integer32"
_HwAclAdvancedFragments_Object = MibTableColumn
hwAclAdvancedFragments = _HwAclAdvancedFragments_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 22),
    _HwAclAdvancedFragments_Type()
)
hwAclAdvancedFragments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedFragments.setStatus("current")
_HwAclAdvancedLog_Type = TruthValue
_HwAclAdvancedLog_Object = MibTableColumn
hwAclAdvancedLog = _HwAclAdvancedLog_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 23),
    _HwAclAdvancedLog_Type()
)
hwAclAdvancedLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedLog.setStatus("current")
_HwAclAdvancedEnable_Type = TruthValue
_HwAclAdvancedEnable_Object = MibTableColumn
hwAclAdvancedEnable = _HwAclAdvancedEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 24),
    _HwAclAdvancedEnable_Type()
)
hwAclAdvancedEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclAdvancedEnable.setStatus("current")
_HwAclAdvancedCount_Type = Counter64
_HwAclAdvancedCount_Object = MibTableColumn
hwAclAdvancedCount = _HwAclAdvancedCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 25),
    _HwAclAdvancedCount_Type()
)
hwAclAdvancedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclAdvancedCount.setStatus("current")


class _HwAclAdvancedVrfName_Type(OctetString):
    """Custom type hwAclAdvancedVrfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwAclAdvancedVrfName_Type.__name__ = "OctetString"
_HwAclAdvancedVrfName_Object = MibTableColumn
hwAclAdvancedVrfName = _HwAclAdvancedVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 26),
    _HwAclAdvancedVrfName_Type()
)
hwAclAdvancedVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedVrfName.setStatus("current")
_HwAclAdvancedRowStatus_Type = RowStatus
_HwAclAdvancedRowStatus_Object = MibTableColumn
hwAclAdvancedRowStatus = _HwAclAdvancedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 27),
    _HwAclAdvancedRowStatus_Type()
)
hwAclAdvancedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedRowStatus.setStatus("current")


class _HwAclAdvancedTcpSyncFlag_Type(Integer32):
    """Custom type hwAclAdvancedTcpSyncFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_HwAclAdvancedTcpSyncFlag_Type.__name__ = "Integer32"
_HwAclAdvancedTcpSyncFlag_Object = MibTableColumn
hwAclAdvancedTcpSyncFlag = _HwAclAdvancedTcpSyncFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 28),
    _HwAclAdvancedTcpSyncFlag_Type()
)
hwAclAdvancedTcpSyncFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedTcpSyncFlag.setStatus("current")


class _HwAclAdvancedDescription_Type(OctetString):
    """Custom type hwAclAdvancedDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HwAclAdvancedDescription_Type.__name__ = "OctetString"
_HwAclAdvancedDescription_Object = MibTableColumn
hwAclAdvancedDescription = _HwAclAdvancedDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 29),
    _HwAclAdvancedDescription_Type()
)
hwAclAdvancedDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedDescription.setStatus("current")


class _HwAclAdvancedSrcPoolName_Type(OctetString):
    """Custom type hwAclAdvancedSrcPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwAclAdvancedSrcPoolName_Type.__name__ = "OctetString"
_HwAclAdvancedSrcPoolName_Object = MibTableColumn
hwAclAdvancedSrcPoolName = _HwAclAdvancedSrcPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 30),
    _HwAclAdvancedSrcPoolName_Type()
)
hwAclAdvancedSrcPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedSrcPoolName.setStatus("current")


class _HwAclAdvancedDestPoolName_Type(OctetString):
    """Custom type hwAclAdvancedDestPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwAclAdvancedDestPoolName_Type.__name__ = "OctetString"
_HwAclAdvancedDestPoolName_Object = MibTableColumn
hwAclAdvancedDestPoolName = _HwAclAdvancedDestPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 31),
    _HwAclAdvancedDestPoolName_Type()
)
hwAclAdvancedDestPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedDestPoolName.setStatus("current")


class _HwAclAdvancedProtocolNew_Type(Integer32):
    """Custom type hwAclAdvancedProtocolNew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HwAclAdvancedProtocolNew_Type.__name__ = "Integer32"
_HwAclAdvancedProtocolNew_Object = MibTableColumn
hwAclAdvancedProtocolNew = _HwAclAdvancedProtocolNew_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 32),
    _HwAclAdvancedProtocolNew_Type()
)
hwAclAdvancedProtocolNew.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedProtocolNew.setStatus("current")


class _HwAclAdvancedVni_Type(Integer32):
    """Custom type hwAclAdvancedVni based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_HwAclAdvancedVni_Type.__name__ = "Integer32"
_HwAclAdvancedVni_Object = MibTableColumn
hwAclAdvancedVni = _HwAclAdvancedVni_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 33),
    _HwAclAdvancedVni_Type()
)
hwAclAdvancedVni.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedVni.setStatus("current")


class _HwAclAdvancedIgmpType_Type(Integer32):
    """Custom type hwAclAdvancedIgmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HwAclAdvancedIgmpType_Type.__name__ = "Integer32"
_HwAclAdvancedIgmpType_Object = MibTableColumn
hwAclAdvancedIgmpType = _HwAclAdvancedIgmpType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 34),
    _HwAclAdvancedIgmpType_Type()
)
hwAclAdvancedIgmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedIgmpType.setStatus("current")


class _HwAclAdvancedTtlOp_Type(Integer32):
    """Custom type hwAclAdvancedTtlOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("eq", 2),
          ("gt", 3),
          ("invalid", 0),
          ("lt", 1),
          ("neq", 4),
          ("range", 5))
    )


_HwAclAdvancedTtlOp_Type.__name__ = "Integer32"
_HwAclAdvancedTtlOp_Object = MibTableColumn
hwAclAdvancedTtlOp = _HwAclAdvancedTtlOp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 35),
    _HwAclAdvancedTtlOp_Type()
)
hwAclAdvancedTtlOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedTtlOp.setStatus("current")


class _HwAclAdvancedTtlExpire_Type(Integer32):
    """Custom type hwAclAdvancedTtlExpire based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwAclAdvancedTtlExpire_Type.__name__ = "Integer32"
_HwAclAdvancedTtlExpire_Object = MibTableColumn
hwAclAdvancedTtlExpire = _HwAclAdvancedTtlExpire_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 36),
    _HwAclAdvancedTtlExpire_Type()
)
hwAclAdvancedTtlExpire.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedTtlExpire.setStatus("current")


class _HwAclAdvancedTtlExpireEnd_Type(Integer32):
    """Custom type hwAclAdvancedTtlExpireEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwAclAdvancedTtlExpireEnd_Type.__name__ = "Integer32"
_HwAclAdvancedTtlExpireEnd_Object = MibTableColumn
hwAclAdvancedTtlExpireEnd = _HwAclAdvancedTtlExpireEnd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 37),
    _HwAclAdvancedTtlExpireEnd_Type()
)
hwAclAdvancedTtlExpireEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedTtlExpireEnd.setStatus("current")


class _HwAclAdvancedPktLenOp_Type(Integer32):
    """Custom type hwAclAdvancedPktLenOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("eq", 2),
          ("gt", 3),
          ("invalid", 0),
          ("lt", 1),
          ("neq", 4),
          ("range", 5))
    )


_HwAclAdvancedPktLenOp_Type.__name__ = "Integer32"
_HwAclAdvancedPktLenOp_Object = MibTableColumn
hwAclAdvancedPktLenOp = _HwAclAdvancedPktLenOp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 38),
    _HwAclAdvancedPktLenOp_Type()
)
hwAclAdvancedPktLenOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedPktLenOp.setStatus("current")


class _HwAclAdvancedPktLenBegin_Type(Integer32):
    """Custom type hwAclAdvancedPktLenBegin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwAclAdvancedPktLenBegin_Type.__name__ = "Integer32"
_HwAclAdvancedPktLenBegin_Object = MibTableColumn
hwAclAdvancedPktLenBegin = _HwAclAdvancedPktLenBegin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 39),
    _HwAclAdvancedPktLenBegin_Type()
)
hwAclAdvancedPktLenBegin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedPktLenBegin.setStatus("current")


class _HwAclAdvancedPktLenEnd_Type(Integer32):
    """Custom type hwAclAdvancedPktLenEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwAclAdvancedPktLenEnd_Type.__name__ = "Integer32"
_HwAclAdvancedPktLenEnd_Object = MibTableColumn
hwAclAdvancedPktLenEnd = _HwAclAdvancedPktLenEnd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 40),
    _HwAclAdvancedPktLenEnd_Type()
)
hwAclAdvancedPktLenEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedPktLenEnd.setStatus("current")


class _HwAclAdvancedTcpFlagMask_Type(Integer32):
    """Custom type hwAclAdvancedTcpFlagMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwAclAdvancedTcpFlagMask_Type.__name__ = "Integer32"
_HwAclAdvancedTcpFlagMask_Object = MibTableColumn
hwAclAdvancedTcpFlagMask = _HwAclAdvancedTcpFlagMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 5, 1, 41),
    _HwAclAdvancedTcpFlagMask_Type()
)
hwAclAdvancedTcpFlagMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAdvancedTcpFlagMask.setStatus("current")
_HwAclIfRuleTable_Object = MibTable
hwAclIfRuleTable = _HwAclIfRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hwAclIfRuleTable.setStatus("current")
_HwAclIfRuleEntry_Object = MibTableRow
hwAclIfRuleEntry = _HwAclIfRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 6, 1)
)
hwAclIfRuleEntry.setIndexNames(
    (0, "HUAWEI-ACL-MIB", "hwAclIfAclNum"),
    (0, "HUAWEI-ACL-MIB", "hwAclIfSubitem"),
)
if mibBuilder.loadTexts:
    hwAclIfRuleEntry.setStatus("current")
_HwAclIfAclNum_Type = Integer32
_HwAclIfAclNum_Object = MibTableColumn
hwAclIfAclNum = _HwAclIfAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 6, 1, 1),
    _HwAclIfAclNum_Type()
)
hwAclIfAclNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclIfAclNum.setStatus("current")
_HwAclIfSubitem_Type = Unsigned32
_HwAclIfSubitem_Object = MibTableColumn
hwAclIfSubitem = _HwAclIfSubitem_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 6, 1, 2),
    _HwAclIfSubitem_Type()
)
hwAclIfSubitem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclIfSubitem.setStatus("current")


class _HwAclIfAct_Type(Integer32):
    """Custom type hwAclIfAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_HwAclIfAct_Type.__name__ = "Integer32"
_HwAclIfAct_Object = MibTableColumn
hwAclIfAct = _HwAclIfAct_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 6, 1, 3),
    _HwAclIfAct_Type()
)
hwAclIfAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIfAct.setStatus("current")
_HwAclIfIndex_Type = Integer32
_HwAclIfIndex_Object = MibTableColumn
hwAclIfIndex = _HwAclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 6, 1, 4),
    _HwAclIfIndex_Type()
)
hwAclIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIfIndex.setStatus("current")
_HwAclIfAny_Type = TruthValue
_HwAclIfAny_Object = MibTableColumn
hwAclIfAny = _HwAclIfAny_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 6, 1, 5),
    _HwAclIfAny_Type()
)
hwAclIfAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIfAny.setStatus("current")


class _HwAclIfTimeRangeIndex_Type(Integer32):
    """Custom type hwAclIfTimeRangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_HwAclIfTimeRangeIndex_Type.__name__ = "Integer32"
_HwAclIfTimeRangeIndex_Object = MibTableColumn
hwAclIfTimeRangeIndex = _HwAclIfTimeRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 6, 1, 6),
    _HwAclIfTimeRangeIndex_Type()
)
hwAclIfTimeRangeIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIfTimeRangeIndex.setStatus("current")
_HwAclIfLog_Type = TruthValue
_HwAclIfLog_Object = MibTableColumn
hwAclIfLog = _HwAclIfLog_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 6, 1, 7),
    _HwAclIfLog_Type()
)
hwAclIfLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIfLog.setStatus("current")
_HwAclIfEnable_Type = TruthValue
_HwAclIfEnable_Object = MibTableColumn
hwAclIfEnable = _HwAclIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 6, 1, 8),
    _HwAclIfEnable_Type()
)
hwAclIfEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclIfEnable.setStatus("current")
_HwAclIfCount_Type = Counter64
_HwAclIfCount_Object = MibTableColumn
hwAclIfCount = _HwAclIfCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 6, 1, 9),
    _HwAclIfCount_Type()
)
hwAclIfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclIfCount.setStatus("current")
_HwAclIfRowStatus_Type = RowStatus
_HwAclIfRowStatus_Object = MibTableColumn
hwAclIfRowStatus = _HwAclIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 6, 1, 11),
    _HwAclIfRowStatus_Type()
)
hwAclIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIfRowStatus.setStatus("current")
_HwAclUserRuleTable_Object = MibTable
hwAclUserRuleTable = _HwAclUserRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hwAclUserRuleTable.setStatus("current")
_HwAclUserRuleEntry_Object = MibTableRow
hwAclUserRuleEntry = _HwAclUserRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1)
)
hwAclUserRuleEntry.setIndexNames(
    (0, "HUAWEI-ACL-MIB", "hwAclUserAclNum"),
    (0, "HUAWEI-ACL-MIB", "hwAclUserSubitem"),
)
if mibBuilder.loadTexts:
    hwAclUserRuleEntry.setStatus("current")
_HwAclUserAclNum_Type = Integer32
_HwAclUserAclNum_Object = MibTableColumn
hwAclUserAclNum = _HwAclUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 1),
    _HwAclUserAclNum_Type()
)
hwAclUserAclNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclUserAclNum.setStatus("current")
_HwAclUserSubitem_Type = Unsigned32
_HwAclUserSubitem_Object = MibTableColumn
hwAclUserSubitem = _HwAclUserSubitem_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 2),
    _HwAclUserSubitem_Type()
)
hwAclUserSubitem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclUserSubitem.setStatus("current")


class _HwAclUserAct_Type(Integer32):
    """Custom type hwAclUserAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_HwAclUserAct_Type.__name__ = "Integer32"
_HwAclUserAct_Object = MibTableColumn
hwAclUserAct = _HwAclUserAct_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 3),
    _HwAclUserAct_Type()
)
hwAclUserAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserAct.setStatus("current")


class _HwAclUserProtocol_Type(Integer32):
    """Custom type hwAclUserProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwAclUserProtocol_Type.__name__ = "Integer32"
_HwAclUserProtocol_Object = MibTableColumn
hwAclUserProtocol = _HwAclUserProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 4),
    _HwAclUserProtocol_Type()
)
hwAclUserProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserProtocol.setStatus("current")
_HwAclUserSrcIp_Type = IpAddress
_HwAclUserSrcIp_Object = MibTableColumn
hwAclUserSrcIp = _HwAclUserSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 5),
    _HwAclUserSrcIp_Type()
)
hwAclUserSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserSrcIp.setStatus("current")
_HwAclUserSrcWild_Type = IpAddress
_HwAclUserSrcWild_Object = MibTableColumn
hwAclUserSrcWild = _HwAclUserSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 6),
    _HwAclUserSrcWild_Type()
)
hwAclUserSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserSrcWild.setStatus("current")


class _HwAclUserSrcOp_Type(Integer32):
    """Custom type hwAclUserSrcOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("eq", 2),
          ("gt", 3),
          ("invalid", 0),
          ("lt", 1),
          ("neq", 4),
          ("range", 5))
    )


_HwAclUserSrcOp_Type.__name__ = "Integer32"
_HwAclUserSrcOp_Object = MibTableColumn
hwAclUserSrcOp = _HwAclUserSrcOp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 7),
    _HwAclUserSrcOp_Type()
)
hwAclUserSrcOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserSrcOp.setStatus("current")


class _HwAclUserSrcPort1_Type(Integer32):
    """Custom type hwAclUserSrcPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwAclUserSrcPort1_Type.__name__ = "Integer32"
_HwAclUserSrcPort1_Object = MibTableColumn
hwAclUserSrcPort1 = _HwAclUserSrcPort1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 8),
    _HwAclUserSrcPort1_Type()
)
hwAclUserSrcPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserSrcPort1.setStatus("current")


class _HwAclUserSrcPort2_Type(Integer32):
    """Custom type hwAclUserSrcPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwAclUserSrcPort2_Type.__name__ = "Integer32"
_HwAclUserSrcPort2_Object = MibTableColumn
hwAclUserSrcPort2 = _HwAclUserSrcPort2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 9),
    _HwAclUserSrcPort2_Type()
)
hwAclUserSrcPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserSrcPort2.setStatus("current")
_HwAclUserDestIp_Type = IpAddress
_HwAclUserDestIp_Object = MibTableColumn
hwAclUserDestIp = _HwAclUserDestIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 10),
    _HwAclUserDestIp_Type()
)
hwAclUserDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserDestIp.setStatus("current")
_HwAclUserDestWild_Type = IpAddress
_HwAclUserDestWild_Object = MibTableColumn
hwAclUserDestWild = _HwAclUserDestWild_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 11),
    _HwAclUserDestWild_Type()
)
hwAclUserDestWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserDestWild.setStatus("current")


class _HwAclUserDestOp_Type(Integer32):
    """Custom type hwAclUserDestOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("eq", 2),
          ("gt", 3),
          ("invalid", 0),
          ("lt", 1),
          ("neq", 4),
          ("range", 5))
    )


_HwAclUserDestOp_Type.__name__ = "Integer32"
_HwAclUserDestOp_Object = MibTableColumn
hwAclUserDestOp = _HwAclUserDestOp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 12),
    _HwAclUserDestOp_Type()
)
hwAclUserDestOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserDestOp.setStatus("current")


class _HwAclUserDestPort1_Type(Integer32):
    """Custom type hwAclUserDestPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwAclUserDestPort1_Type.__name__ = "Integer32"
_HwAclUserDestPort1_Object = MibTableColumn
hwAclUserDestPort1 = _HwAclUserDestPort1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 13),
    _HwAclUserDestPort1_Type()
)
hwAclUserDestPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserDestPort1.setStatus("current")


class _HwAclUserDestPort2_Type(Integer32):
    """Custom type hwAclUserDestPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwAclUserDestPort2_Type.__name__ = "Integer32"
_HwAclUserDestPort2_Object = MibTableColumn
hwAclUserDestPort2 = _HwAclUserDestPort2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 14),
    _HwAclUserDestPort2_Type()
)
hwAclUserDestPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserDestPort2.setStatus("current")


class _HwAclUserPrecedence_Type(Integer32):
    """Custom type hwAclUserPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwAclUserPrecedence_Type.__name__ = "Integer32"
_HwAclUserPrecedence_Object = MibTableColumn
hwAclUserPrecedence = _HwAclUserPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 15),
    _HwAclUserPrecedence_Type()
)
hwAclUserPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserPrecedence.setStatus("current")


class _HwAclUserTos_Type(Integer32):
    """Custom type hwAclUserTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(255, 255),
    )


_HwAclUserTos_Type.__name__ = "Integer32"
_HwAclUserTos_Object = MibTableColumn
hwAclUserTos = _HwAclUserTos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 16),
    _HwAclUserTos_Type()
)
hwAclUserTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserTos.setStatus("current")


class _HwAclUserDscp_Type(Integer32):
    """Custom type hwAclUserDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HwAclUserDscp_Type.__name__ = "Integer32"
_HwAclUserDscp_Object = MibTableColumn
hwAclUserDscp = _HwAclUserDscp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 17),
    _HwAclUserDscp_Type()
)
hwAclUserDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserDscp.setStatus("current")


class _HwAclUserEstablish_Type(TruthValue):
    """Custom type hwAclUserEstablish based on TruthValue"""


_HwAclUserEstablish_Object = MibTableColumn
hwAclUserEstablish = _HwAclUserEstablish_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 18),
    _HwAclUserEstablish_Type()
)
hwAclUserEstablish.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserEstablish.setStatus("current")


class _HwAclUserTimeRangeIndex_Type(Integer32):
    """Custom type hwAclUserTimeRangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_HwAclUserTimeRangeIndex_Type.__name__ = "Integer32"
_HwAclUserTimeRangeIndex_Object = MibTableColumn
hwAclUserTimeRangeIndex = _HwAclUserTimeRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 19),
    _HwAclUserTimeRangeIndex_Type()
)
hwAclUserTimeRangeIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserTimeRangeIndex.setStatus("current")


class _HwAclUserIcmpType_Type(Integer32):
    """Custom type hwAclUserIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HwAclUserIcmpType_Type.__name__ = "Integer32"
_HwAclUserIcmpType_Object = MibTableColumn
hwAclUserIcmpType = _HwAclUserIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 20),
    _HwAclUserIcmpType_Type()
)
hwAclUserIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserIcmpType.setStatus("current")


class _HwAclUserIcmpCode_Type(Integer32):
    """Custom type hwAclUserIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HwAclUserIcmpCode_Type.__name__ = "Integer32"
_HwAclUserIcmpCode_Object = MibTableColumn
hwAclUserIcmpCode = _HwAclUserIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 21),
    _HwAclUserIcmpCode_Type()
)
hwAclUserIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserIcmpCode.setStatus("current")
_HwAclUserFragments_Type = TruthValue
_HwAclUserFragments_Object = MibTableColumn
hwAclUserFragments = _HwAclUserFragments_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 22),
    _HwAclUserFragments_Type()
)
hwAclUserFragments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserFragments.setStatus("current")
_HwAclUserLog_Type = TruthValue
_HwAclUserLog_Object = MibTableColumn
hwAclUserLog = _HwAclUserLog_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 23),
    _HwAclUserLog_Type()
)
hwAclUserLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserLog.setStatus("current")
_HwAclUserEnable_Type = TruthValue
_HwAclUserEnable_Object = MibTableColumn
hwAclUserEnable = _HwAclUserEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 24),
    _HwAclUserEnable_Type()
)
hwAclUserEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclUserEnable.setStatus("current")
_HwAclUserCount_Type = Counter32
_HwAclUserCount_Object = MibTableColumn
hwAclUserCount = _HwAclUserCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 25),
    _HwAclUserCount_Type()
)
hwAclUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclUserCount.setStatus("current")


class _HwAclUserVrfName_Type(OctetString):
    """Custom type hwAclUserVrfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwAclUserVrfName_Type.__name__ = "OctetString"
_HwAclUserVrfName_Object = MibTableColumn
hwAclUserVrfName = _HwAclUserVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 26),
    _HwAclUserVrfName_Type()
)
hwAclUserVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserVrfName.setStatus("current")


class _HwAclUserSrcUserGroupName_Type(OctetString):
    """Custom type hwAclUserSrcUserGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwAclUserSrcUserGroupName_Type.__name__ = "OctetString"
_HwAclUserSrcUserGroupName_Object = MibTableColumn
hwAclUserSrcUserGroupName = _HwAclUserSrcUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 27),
    _HwAclUserSrcUserGroupName_Type()
)
hwAclUserSrcUserGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserSrcUserGroupName.setStatus("current")


class _HwAclUserDestUserGroupName_Type(OctetString):
    """Custom type hwAclUserDestUserGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwAclUserDestUserGroupName_Type.__name__ = "OctetString"
_HwAclUserDestUserGroupName_Object = MibTableColumn
hwAclUserDestUserGroupName = _HwAclUserDestUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 28),
    _HwAclUserDestUserGroupName_Type()
)
hwAclUserDestUserGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserDestUserGroupName.setStatus("current")


class _HwAclUserSrcModeType_Type(Integer32):
    """Custom type hwAclUserSrcModeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_HwAclUserSrcModeType_Type.__name__ = "Integer32"
_HwAclUserSrcModeType_Object = MibTableColumn
hwAclUserSrcModeType = _HwAclUserSrcModeType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 29),
    _HwAclUserSrcModeType_Type()
)
hwAclUserSrcModeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserSrcModeType.setStatus("current")


class _HwAclUserDestModeType_Type(Integer32):
    """Custom type hwAclUserDestModeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_HwAclUserDestModeType_Type.__name__ = "Integer32"
_HwAclUserDestModeType_Object = MibTableColumn
hwAclUserDestModeType = _HwAclUserDestModeType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 30),
    _HwAclUserDestModeType_Type()
)
hwAclUserDestModeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserDestModeType.setStatus("current")
_HwAclUserRowStatus_Type = RowStatus
_HwAclUserRowStatus_Object = MibTableColumn
hwAclUserRowStatus = _HwAclUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 31),
    _HwAclUserRowStatus_Type()
)
hwAclUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserRowStatus.setStatus("current")


class _HwAclUserTcpSyncFlag_Type(Integer32):
    """Custom type hwAclUserTcpSyncFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_HwAclUserTcpSyncFlag_Type.__name__ = "Integer32"
_HwAclUserTcpSyncFlag_Object = MibTableColumn
hwAclUserTcpSyncFlag = _HwAclUserTcpSyncFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 32),
    _HwAclUserTcpSyncFlag_Type()
)
hwAclUserTcpSyncFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserTcpSyncFlag.setStatus("current")


class _HwAclUserSrcUserGroupNum_Type(Integer32):
    """Custom type hwAclUserSrcUserGroupNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
        ValueRangeConstraint(65535, 65535),
    )


_HwAclUserSrcUserGroupNum_Type.__name__ = "Integer32"
_HwAclUserSrcUserGroupNum_Object = MibTableColumn
hwAclUserSrcUserGroupNum = _HwAclUserSrcUserGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 33),
    _HwAclUserSrcUserGroupNum_Type()
)
hwAclUserSrcUserGroupNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserSrcUserGroupNum.setStatus("current")


class _HwAclUserDestUserGroupNum_Type(Integer32):
    """Custom type hwAclUserDestUserGroupNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
        ValueRangeConstraint(65535, 65535),
    )


_HwAclUserDestUserGroupNum_Type.__name__ = "Integer32"
_HwAclUserDestUserGroupNum_Object = MibTableColumn
hwAclUserDestUserGroupNum = _HwAclUserDestUserGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 34),
    _HwAclUserDestUserGroupNum_Type()
)
hwAclUserDestUserGroupNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclUserDestUserGroupNum.setStatus("current")


class _HwAclUserDestDomainName_Type(OctetString):
    """Custom type hwAclUserDestDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 127),
    )


_HwAclUserDestDomainName_Type.__name__ = "OctetString"
_HwAclUserDestDomainName_Object = MibTableColumn
hwAclUserDestDomainName = _HwAclUserDestDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 7, 1, 35),
    _HwAclUserDestDomainName_Type()
)
hwAclUserDestDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclUserDestDomainName.setStatus("current")
_HwAclCompileEnableFlag_Type = TruthValue
_HwAclCompileEnableFlag_Object = MibScalar
hwAclCompileEnableFlag = _HwAclCompileEnableFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 10),
    _HwAclCompileEnableFlag_Type()
)
hwAclCompileEnableFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAclCompileEnableFlag.setStatus("current")
_HwAclCompileNumGroupTable_Object = MibTable
hwAclCompileNumGroupTable = _HwAclCompileNumGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 11)
)
if mibBuilder.loadTexts:
    hwAclCompileNumGroupTable.setStatus("current")
_HwAclCompileNumGroupEntry_Object = MibTableRow
hwAclCompileNumGroupEntry = _HwAclCompileNumGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    hwAclCompileNumGroupEntry.setStatus("current")


class _HwAclCompileNumGroupStatus_Type(Integer32):
    """Custom type hwAclCompileNumGroupStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("changeAfterCompile", 3),
          ("compiled", 2),
          ("notCompile", 1))
    )


_HwAclCompileNumGroupStatus_Type.__name__ = "Integer32"
_HwAclCompileNumGroupStatus_Object = MibTableColumn
hwAclCompileNumGroupStatus = _HwAclCompileNumGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 11, 1, 1),
    _HwAclCompileNumGroupStatus_Type()
)
hwAclCompileNumGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAclCompileNumGroupStatus.setStatus("current")
_HwAclIpv6BasicRuleTable_Object = MibTable
hwAclIpv6BasicRuleTable = _HwAclIpv6BasicRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 12)
)
if mibBuilder.loadTexts:
    hwAclIpv6BasicRuleTable.setStatus("current")
_HwAclIpv6BasicRuleEntry_Object = MibTableRow
hwAclIpv6BasicRuleEntry = _HwAclIpv6BasicRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 12, 1)
)
hwAclIpv6BasicRuleEntry.setIndexNames(
    (0, "HUAWEI-ACL-MIB", "hwAclIpv6BasicAclNum"),
    (0, "HUAWEI-ACL-MIB", "hwAclIpv6BasicSubitem"),
)
if mibBuilder.loadTexts:
    hwAclIpv6BasicRuleEntry.setStatus("current")
_HwAclIpv6BasicAclNum_Type = Integer32
_HwAclIpv6BasicAclNum_Object = MibTableColumn
hwAclIpv6BasicAclNum = _HwAclIpv6BasicAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 12, 1, 1),
    _HwAclIpv6BasicAclNum_Type()
)
hwAclIpv6BasicAclNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclIpv6BasicAclNum.setStatus("current")
_HwAclIpv6BasicSubitem_Type = Unsigned32
_HwAclIpv6BasicSubitem_Object = MibTableColumn
hwAclIpv6BasicSubitem = _HwAclIpv6BasicSubitem_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 12, 1, 2),
    _HwAclIpv6BasicSubitem_Type()
)
hwAclIpv6BasicSubitem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclIpv6BasicSubitem.setStatus("current")


class _HwAclIpv6BasicAct_Type(Integer32):
    """Custom type hwAclIpv6BasicAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_HwAclIpv6BasicAct_Type.__name__ = "Integer32"
_HwAclIpv6BasicAct_Object = MibTableColumn
hwAclIpv6BasicAct = _HwAclIpv6BasicAct_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 12, 1, 3),
    _HwAclIpv6BasicAct_Type()
)
hwAclIpv6BasicAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6BasicAct.setStatus("current")
_HwAclIpv6BasicSrcIp_Type = Ipv6Address
_HwAclIpv6BasicSrcIp_Object = MibTableColumn
hwAclIpv6BasicSrcIp = _HwAclIpv6BasicSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 12, 1, 4),
    _HwAclIpv6BasicSrcIp_Type()
)
hwAclIpv6BasicSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6BasicSrcIp.setStatus("current")


class _HwAclIpv6BasicSrcPrefix_Type(Integer32):
    """Custom type hwAclIpv6BasicSrcPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwAclIpv6BasicSrcPrefix_Type.__name__ = "Integer32"
_HwAclIpv6BasicSrcPrefix_Object = MibTableColumn
hwAclIpv6BasicSrcPrefix = _HwAclIpv6BasicSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 12, 1, 5),
    _HwAclIpv6BasicSrcPrefix_Type()
)
hwAclIpv6BasicSrcPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6BasicSrcPrefix.setStatus("current")


class _HwAclIpv6BasicTimeRangeIndex_Type(Integer32):
    """Custom type hwAclIpv6BasicTimeRangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_HwAclIpv6BasicTimeRangeIndex_Type.__name__ = "Integer32"
_HwAclIpv6BasicTimeRangeIndex_Object = MibTableColumn
hwAclIpv6BasicTimeRangeIndex = _HwAclIpv6BasicTimeRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 12, 1, 6),
    _HwAclIpv6BasicTimeRangeIndex_Type()
)
hwAclIpv6BasicTimeRangeIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6BasicTimeRangeIndex.setStatus("current")


class _HwAclIpv6BasicFragment_Type(Integer32):
    """Custom type hwAclIpv6BasicFragment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fragment", 1),
          ("fragmentSubseq", 0),
          ("none", 255))
    )


_HwAclIpv6BasicFragment_Type.__name__ = "Integer32"
_HwAclIpv6BasicFragment_Object = MibTableColumn
hwAclIpv6BasicFragment = _HwAclIpv6BasicFragment_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 12, 1, 7),
    _HwAclIpv6BasicFragment_Type()
)
hwAclIpv6BasicFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6BasicFragment.setStatus("current")
_HwAclIpv6BasicLog_Type = TruthValue
_HwAclIpv6BasicLog_Object = MibTableColumn
hwAclIpv6BasicLog = _HwAclIpv6BasicLog_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 12, 1, 8),
    _HwAclIpv6BasicLog_Type()
)
hwAclIpv6BasicLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6BasicLog.setStatus("current")
_HwAclIpv6BasicEnable_Type = EnabledStatus
_HwAclIpv6BasicEnable_Object = MibTableColumn
hwAclIpv6BasicEnable = _HwAclIpv6BasicEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 12, 1, 9),
    _HwAclIpv6BasicEnable_Type()
)
hwAclIpv6BasicEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclIpv6BasicEnable.setStatus("current")
_HwAclIpv6BasicCount_Type = Counter64
_HwAclIpv6BasicCount_Object = MibTableColumn
hwAclIpv6BasicCount = _HwAclIpv6BasicCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 12, 1, 10),
    _HwAclIpv6BasicCount_Type()
)
hwAclIpv6BasicCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclIpv6BasicCount.setStatus("current")


class _HwAclIpv6BasicVrfName_Type(OctetString):
    """Custom type hwAclIpv6BasicVrfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwAclIpv6BasicVrfName_Type.__name__ = "OctetString"
_HwAclIpv6BasicVrfName_Object = MibTableColumn
hwAclIpv6BasicVrfName = _HwAclIpv6BasicVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 12, 1, 11),
    _HwAclIpv6BasicVrfName_Type()
)
hwAclIpv6BasicVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6BasicVrfName.setStatus("current")
_HwAclIpv6BasicRowStatus_Type = RowStatus
_HwAclIpv6BasicRowStatus_Object = MibTableColumn
hwAclIpv6BasicRowStatus = _HwAclIpv6BasicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 12, 1, 12),
    _HwAclIpv6BasicRowStatus_Type()
)
hwAclIpv6BasicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6BasicRowStatus.setStatus("current")


class _HwAclIpv6BasicDescription_Type(OctetString):
    """Custom type hwAclIpv6BasicDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HwAclIpv6BasicDescription_Type.__name__ = "OctetString"
_HwAclIpv6BasicDescription_Object = MibTableColumn
hwAclIpv6BasicDescription = _HwAclIpv6BasicDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 12, 1, 13),
    _HwAclIpv6BasicDescription_Type()
)
hwAclIpv6BasicDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6BasicDescription.setStatus("current")
_HwAclIpv6BasicSrcMask_Type = Ipv6Address
_HwAclIpv6BasicSrcMask_Object = MibTableColumn
hwAclIpv6BasicSrcMask = _HwAclIpv6BasicSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 12, 1, 14),
    _HwAclIpv6BasicSrcMask_Type()
)
hwAclIpv6BasicSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6BasicSrcMask.setStatus("current")
_HwAclIpv6AdvancedRuleTable_Object = MibTable
hwAclIpv6AdvancedRuleTable = _HwAclIpv6AdvancedRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13)
)
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedRuleTable.setStatus("current")
_HwAclIpv6AdvancedRuleEntry_Object = MibTableRow
hwAclIpv6AdvancedRuleEntry = _HwAclIpv6AdvancedRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1)
)
hwAclIpv6AdvancedRuleEntry.setIndexNames(
    (0, "HUAWEI-ACL-MIB", "hwAclIpv6AdvancedAclNum"),
    (0, "HUAWEI-ACL-MIB", "hwAclIpv6AdvancedSubitem"),
)
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedRuleEntry.setStatus("current")
_HwAclIpv6AdvancedAclNum_Type = Integer32
_HwAclIpv6AdvancedAclNum_Object = MibTableColumn
hwAclIpv6AdvancedAclNum = _HwAclIpv6AdvancedAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 1),
    _HwAclIpv6AdvancedAclNum_Type()
)
hwAclIpv6AdvancedAclNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedAclNum.setStatus("current")
_HwAclIpv6AdvancedSubitem_Type = Unsigned32
_HwAclIpv6AdvancedSubitem_Object = MibTableColumn
hwAclIpv6AdvancedSubitem = _HwAclIpv6AdvancedSubitem_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 2),
    _HwAclIpv6AdvancedSubitem_Type()
)
hwAclIpv6AdvancedSubitem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedSubitem.setStatus("current")


class _HwAclIpv6AdvancedAct_Type(Integer32):
    """Custom type hwAclIpv6AdvancedAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_HwAclIpv6AdvancedAct_Type.__name__ = "Integer32"
_HwAclIpv6AdvancedAct_Object = MibTableColumn
hwAclIpv6AdvancedAct = _HwAclIpv6AdvancedAct_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 3),
    _HwAclIpv6AdvancedAct_Type()
)
hwAclIpv6AdvancedAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedAct.setStatus("current")


class _HwAclIpv6AdvancedProtocol_Type(Integer32):
    """Custom type hwAclIpv6AdvancedProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwAclIpv6AdvancedProtocol_Type.__name__ = "Integer32"
_HwAclIpv6AdvancedProtocol_Object = MibTableColumn
hwAclIpv6AdvancedProtocol = _HwAclIpv6AdvancedProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 4),
    _HwAclIpv6AdvancedProtocol_Type()
)
hwAclIpv6AdvancedProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedProtocol.setStatus("current")
_HwAclIpv6AdvancedSrcIp_Type = Ipv6Address
_HwAclIpv6AdvancedSrcIp_Object = MibTableColumn
hwAclIpv6AdvancedSrcIp = _HwAclIpv6AdvancedSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 5),
    _HwAclIpv6AdvancedSrcIp_Type()
)
hwAclIpv6AdvancedSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedSrcIp.setStatus("current")


class _HwAclIpv6AdvancedSrcPrefix_Type(Integer32):
    """Custom type hwAclIpv6AdvancedSrcPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwAclIpv6AdvancedSrcPrefix_Type.__name__ = "Integer32"
_HwAclIpv6AdvancedSrcPrefix_Object = MibTableColumn
hwAclIpv6AdvancedSrcPrefix = _HwAclIpv6AdvancedSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 6),
    _HwAclIpv6AdvancedSrcPrefix_Type()
)
hwAclIpv6AdvancedSrcPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedSrcPrefix.setStatus("current")


class _HwAclIpv6AdvancedSrcOp_Type(Integer32):
    """Custom type hwAclIpv6AdvancedSrcOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("eq", 2),
          ("gt", 3),
          ("invalid", 255),
          ("lt", 1),
          ("neq", 4),
          ("range", 5))
    )


_HwAclIpv6AdvancedSrcOp_Type.__name__ = "Integer32"
_HwAclIpv6AdvancedSrcOp_Object = MibTableColumn
hwAclIpv6AdvancedSrcOp = _HwAclIpv6AdvancedSrcOp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 7),
    _HwAclIpv6AdvancedSrcOp_Type()
)
hwAclIpv6AdvancedSrcOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedSrcOp.setStatus("current")


class _HwAclIpv6AdvancedSrcPort1_Type(Integer32):
    """Custom type hwAclIpv6AdvancedSrcPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwAclIpv6AdvancedSrcPort1_Type.__name__ = "Integer32"
_HwAclIpv6AdvancedSrcPort1_Object = MibTableColumn
hwAclIpv6AdvancedSrcPort1 = _HwAclIpv6AdvancedSrcPort1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 8),
    _HwAclIpv6AdvancedSrcPort1_Type()
)
hwAclIpv6AdvancedSrcPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedSrcPort1.setStatus("current")


class _HwAclIpv6AdvancedSrcPort2_Type(Integer32):
    """Custom type hwAclIpv6AdvancedSrcPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwAclIpv6AdvancedSrcPort2_Type.__name__ = "Integer32"
_HwAclIpv6AdvancedSrcPort2_Object = MibTableColumn
hwAclIpv6AdvancedSrcPort2 = _HwAclIpv6AdvancedSrcPort2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 9),
    _HwAclIpv6AdvancedSrcPort2_Type()
)
hwAclIpv6AdvancedSrcPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedSrcPort2.setStatus("current")
_HwAclIpv6AdvancedDestIp_Type = Ipv6Address
_HwAclIpv6AdvancedDestIp_Object = MibTableColumn
hwAclIpv6AdvancedDestIp = _HwAclIpv6AdvancedDestIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 10),
    _HwAclIpv6AdvancedDestIp_Type()
)
hwAclIpv6AdvancedDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedDestIp.setStatus("current")


class _HwAclIpv6AdvancedDestPrefix_Type(Integer32):
    """Custom type hwAclIpv6AdvancedDestPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwAclIpv6AdvancedDestPrefix_Type.__name__ = "Integer32"
_HwAclIpv6AdvancedDestPrefix_Object = MibTableColumn
hwAclIpv6AdvancedDestPrefix = _HwAclIpv6AdvancedDestPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 11),
    _HwAclIpv6AdvancedDestPrefix_Type()
)
hwAclIpv6AdvancedDestPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedDestPrefix.setStatus("current")


class _HwAclIpv6AdvancedDestOp_Type(Integer32):
    """Custom type hwAclIpv6AdvancedDestOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("eq", 2),
          ("gt", 3),
          ("invalid", 255),
          ("lt", 1),
          ("neq", 4),
          ("range", 5))
    )


_HwAclIpv6AdvancedDestOp_Type.__name__ = "Integer32"
_HwAclIpv6AdvancedDestOp_Object = MibTableColumn
hwAclIpv6AdvancedDestOp = _HwAclIpv6AdvancedDestOp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 12),
    _HwAclIpv6AdvancedDestOp_Type()
)
hwAclIpv6AdvancedDestOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedDestOp.setStatus("current")


class _HwAclIpv6AdvancedDestPort1_Type(Integer32):
    """Custom type hwAclIpv6AdvancedDestPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwAclIpv6AdvancedDestPort1_Type.__name__ = "Integer32"
_HwAclIpv6AdvancedDestPort1_Object = MibTableColumn
hwAclIpv6AdvancedDestPort1 = _HwAclIpv6AdvancedDestPort1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 13),
    _HwAclIpv6AdvancedDestPort1_Type()
)
hwAclIpv6AdvancedDestPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedDestPort1.setStatus("current")


class _HwAclIpv6AdvancedDestPort2_Type(Integer32):
    """Custom type hwAclIpv6AdvancedDestPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwAclIpv6AdvancedDestPort2_Type.__name__ = "Integer32"
_HwAclIpv6AdvancedDestPort2_Object = MibTableColumn
hwAclIpv6AdvancedDestPort2 = _HwAclIpv6AdvancedDestPort2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 14),
    _HwAclIpv6AdvancedDestPort2_Type()
)
hwAclIpv6AdvancedDestPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedDestPort2.setStatus("current")


class _HwAclIpv6AdvancedPrecedence_Type(Integer32):
    """Custom type hwAclIpv6AdvancedPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwAclIpv6AdvancedPrecedence_Type.__name__ = "Integer32"
_HwAclIpv6AdvancedPrecedence_Object = MibTableColumn
hwAclIpv6AdvancedPrecedence = _HwAclIpv6AdvancedPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 15),
    _HwAclIpv6AdvancedPrecedence_Type()
)
hwAclIpv6AdvancedPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedPrecedence.setStatus("current")


class _HwAclIpv6AdvancedTos_Type(Integer32):
    """Custom type hwAclIpv6AdvancedTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(255, 255),
    )


_HwAclIpv6AdvancedTos_Type.__name__ = "Integer32"
_HwAclIpv6AdvancedTos_Object = MibTableColumn
hwAclIpv6AdvancedTos = _HwAclIpv6AdvancedTos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 16),
    _HwAclIpv6AdvancedTos_Type()
)
hwAclIpv6AdvancedTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedTos.setStatus("current")


class _HwAclIpv6AdvancedDscp_Type(Integer32):
    """Custom type hwAclIpv6AdvancedDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HwAclIpv6AdvancedDscp_Type.__name__ = "Integer32"
_HwAclIpv6AdvancedDscp_Object = MibTableColumn
hwAclIpv6AdvancedDscp = _HwAclIpv6AdvancedDscp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 17),
    _HwAclIpv6AdvancedDscp_Type()
)
hwAclIpv6AdvancedDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedDscp.setStatus("current")


class _HwAclIpv6AdvancedEstablish_Type(TruthValue):
    """Custom type hwAclIpv6AdvancedEstablish based on TruthValue"""


_HwAclIpv6AdvancedEstablish_Object = MibTableColumn
hwAclIpv6AdvancedEstablish = _HwAclIpv6AdvancedEstablish_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 18),
    _HwAclIpv6AdvancedEstablish_Type()
)
hwAclIpv6AdvancedEstablish.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedEstablish.setStatus("current")


class _HwAclIpv6AdvancedTimeRangeIndex_Type(Integer32):
    """Custom type hwAclIpv6AdvancedTimeRangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_HwAclIpv6AdvancedTimeRangeIndex_Type.__name__ = "Integer32"
_HwAclIpv6AdvancedTimeRangeIndex_Object = MibTableColumn
hwAclIpv6AdvancedTimeRangeIndex = _HwAclIpv6AdvancedTimeRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 19),
    _HwAclIpv6AdvancedTimeRangeIndex_Type()
)
hwAclIpv6AdvancedTimeRangeIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedTimeRangeIndex.setStatus("current")


class _HwAclIpv6AdvancedIcmpType_Type(Integer32):
    """Custom type hwAclIpv6AdvancedIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HwAclIpv6AdvancedIcmpType_Type.__name__ = "Integer32"
_HwAclIpv6AdvancedIcmpType_Object = MibTableColumn
hwAclIpv6AdvancedIcmpType = _HwAclIpv6AdvancedIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 20),
    _HwAclIpv6AdvancedIcmpType_Type()
)
hwAclIpv6AdvancedIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedIcmpType.setStatus("current")


class _HwAclIpv6AdvancedIcmpCode_Type(Integer32):
    """Custom type hwAclIpv6AdvancedIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HwAclIpv6AdvancedIcmpCode_Type.__name__ = "Integer32"
_HwAclIpv6AdvancedIcmpCode_Object = MibTableColumn
hwAclIpv6AdvancedIcmpCode = _HwAclIpv6AdvancedIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 21),
    _HwAclIpv6AdvancedIcmpCode_Type()
)
hwAclIpv6AdvancedIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedIcmpCode.setStatus("current")


class _HwAclIpv6AdvancedFragment_Type(Integer32):
    """Custom type hwAclIpv6AdvancedFragment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fragment", 1),
          ("fragmentSubseq", 0),
          ("none", 255))
    )


_HwAclIpv6AdvancedFragment_Type.__name__ = "Integer32"
_HwAclIpv6AdvancedFragment_Object = MibTableColumn
hwAclIpv6AdvancedFragment = _HwAclIpv6AdvancedFragment_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 22),
    _HwAclIpv6AdvancedFragment_Type()
)
hwAclIpv6AdvancedFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedFragment.setStatus("current")
_HwAclIpv6AdvancedLog_Type = TruthValue
_HwAclIpv6AdvancedLog_Object = MibTableColumn
hwAclIpv6AdvancedLog = _HwAclIpv6AdvancedLog_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 23),
    _HwAclIpv6AdvancedLog_Type()
)
hwAclIpv6AdvancedLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedLog.setStatus("current")
_HwAclIpv6AdvancedEnable_Type = EnabledStatus
_HwAclIpv6AdvancedEnable_Object = MibTableColumn
hwAclIpv6AdvancedEnable = _HwAclIpv6AdvancedEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 24),
    _HwAclIpv6AdvancedEnable_Type()
)
hwAclIpv6AdvancedEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedEnable.setStatus("current")
_HwAclIpv6AdvancedCount_Type = Counter64
_HwAclIpv6AdvancedCount_Object = MibTableColumn
hwAclIpv6AdvancedCount = _HwAclIpv6AdvancedCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 25),
    _HwAclIpv6AdvancedCount_Type()
)
hwAclIpv6AdvancedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedCount.setStatus("current")


class _HwAclIpv6AdvancedVrfName_Type(OctetString):
    """Custom type hwAclIpv6AdvancedVrfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwAclIpv6AdvancedVrfName_Type.__name__ = "OctetString"
_HwAclIpv6AdvancedVrfName_Object = MibTableColumn
hwAclIpv6AdvancedVrfName = _HwAclIpv6AdvancedVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 26),
    _HwAclIpv6AdvancedVrfName_Type()
)
hwAclIpv6AdvancedVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedVrfName.setStatus("current")
_HwAclIpv6AdvancedRowStatus_Type = RowStatus
_HwAclIpv6AdvancedRowStatus_Object = MibTableColumn
hwAclIpv6AdvancedRowStatus = _HwAclIpv6AdvancedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 27),
    _HwAclIpv6AdvancedRowStatus_Type()
)
hwAclIpv6AdvancedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedRowStatus.setStatus("current")


class _HwAclIpv6AdvancedDescription_Type(OctetString):
    """Custom type hwAclIpv6AdvancedDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HwAclIpv6AdvancedDescription_Type.__name__ = "OctetString"
_HwAclIpv6AdvancedDescription_Object = MibTableColumn
hwAclIpv6AdvancedDescription = _HwAclIpv6AdvancedDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 28),
    _HwAclIpv6AdvancedDescription_Type()
)
hwAclIpv6AdvancedDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedDescription.setStatus("current")
_HwAclIpv6AdvancedSrcMask_Type = Ipv6Address
_HwAclIpv6AdvancedSrcMask_Object = MibTableColumn
hwAclIpv6AdvancedSrcMask = _HwAclIpv6AdvancedSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 29),
    _HwAclIpv6AdvancedSrcMask_Type()
)
hwAclIpv6AdvancedSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedSrcMask.setStatus("current")
_HwAclIpv6AdvancedDestMask_Type = Ipv6Address
_HwAclIpv6AdvancedDestMask_Object = MibTableColumn
hwAclIpv6AdvancedDestMask = _HwAclIpv6AdvancedDestMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 30),
    _HwAclIpv6AdvancedDestMask_Type()
)
hwAclIpv6AdvancedDestMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedDestMask.setStatus("current")


class _HwAclIpv6AdvancedProtocolNew_Type(Integer32):
    """Custom type hwAclIpv6AdvancedProtocolNew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HwAclIpv6AdvancedProtocolNew_Type.__name__ = "Integer32"
_HwAclIpv6AdvancedProtocolNew_Object = MibTableColumn
hwAclIpv6AdvancedProtocolNew = _HwAclIpv6AdvancedProtocolNew_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 13, 1, 31),
    _HwAclIpv6AdvancedProtocolNew_Type()
)
hwAclIpv6AdvancedProtocolNew.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6AdvancedProtocolNew.setStatus("current")
_HwAclEthernetFrameRuleTable_Object = MibTable
hwAclEthernetFrameRuleTable = _HwAclEthernetFrameRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 14)
)
if mibBuilder.loadTexts:
    hwAclEthernetFrameRuleTable.setStatus("current")
_HwAclEthernetFrameRuleEntry_Object = MibTableRow
hwAclEthernetFrameRuleEntry = _HwAclEthernetFrameRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 14, 1)
)
hwAclEthernetFrameRuleEntry.setIndexNames(
    (0, "HUAWEI-ACL-MIB", "hwAclEthernetFrameAclNum"),
    (0, "HUAWEI-ACL-MIB", "hwAclEthernetFrameSubitem"),
)
if mibBuilder.loadTexts:
    hwAclEthernetFrameRuleEntry.setStatus("current")
_HwAclEthernetFrameAclNum_Type = Integer32
_HwAclEthernetFrameAclNum_Object = MibTableColumn
hwAclEthernetFrameAclNum = _HwAclEthernetFrameAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 14, 1, 1),
    _HwAclEthernetFrameAclNum_Type()
)
hwAclEthernetFrameAclNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclEthernetFrameAclNum.setStatus("current")
_HwAclEthernetFrameSubitem_Type = Unsigned32
_HwAclEthernetFrameSubitem_Object = MibTableColumn
hwAclEthernetFrameSubitem = _HwAclEthernetFrameSubitem_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 14, 1, 2),
    _HwAclEthernetFrameSubitem_Type()
)
hwAclEthernetFrameSubitem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclEthernetFrameSubitem.setStatus("current")


class _HwAclEthernetFrameAct_Type(Integer32):
    """Custom type hwAclEthernetFrameAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_HwAclEthernetFrameAct_Type.__name__ = "Integer32"
_HwAclEthernetFrameAct_Object = MibTableColumn
hwAclEthernetFrameAct = _HwAclEthernetFrameAct_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 14, 1, 3),
    _HwAclEthernetFrameAct_Type()
)
hwAclEthernetFrameAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclEthernetFrameAct.setStatus("current")
_HwAclEthernetFrameType_Type = Integer32
_HwAclEthernetFrameType_Object = MibTableColumn
hwAclEthernetFrameType = _HwAclEthernetFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 14, 1, 4),
    _HwAclEthernetFrameType_Type()
)
hwAclEthernetFrameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclEthernetFrameType.setStatus("current")
_HwAclEthernetFrameTypeMask_Type = Integer32
_HwAclEthernetFrameTypeMask_Object = MibTableColumn
hwAclEthernetFrameTypeMask = _HwAclEthernetFrameTypeMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 14, 1, 5),
    _HwAclEthernetFrameTypeMask_Type()
)
hwAclEthernetFrameTypeMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclEthernetFrameTypeMask.setStatus("current")
_HwAclEthernetFrameSrcMac_Type = MacAddress
_HwAclEthernetFrameSrcMac_Object = MibTableColumn
hwAclEthernetFrameSrcMac = _HwAclEthernetFrameSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 14, 1, 6),
    _HwAclEthernetFrameSrcMac_Type()
)
hwAclEthernetFrameSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclEthernetFrameSrcMac.setStatus("current")
_HwAclEthernetFrameSrcMacMask_Type = MacAddress
_HwAclEthernetFrameSrcMacMask_Object = MibTableColumn
hwAclEthernetFrameSrcMacMask = _HwAclEthernetFrameSrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 14, 1, 7),
    _HwAclEthernetFrameSrcMacMask_Type()
)
hwAclEthernetFrameSrcMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclEthernetFrameSrcMacMask.setStatus("current")
_HwAclEthernetFrameDstMac_Type = MacAddress
_HwAclEthernetFrameDstMac_Object = MibTableColumn
hwAclEthernetFrameDstMac = _HwAclEthernetFrameDstMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 14, 1, 8),
    _HwAclEthernetFrameDstMac_Type()
)
hwAclEthernetFrameDstMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclEthernetFrameDstMac.setStatus("current")
_HwAclEthernetFrameDstMacMask_Type = MacAddress
_HwAclEthernetFrameDstMacMask_Object = MibTableColumn
hwAclEthernetFrameDstMacMask = _HwAclEthernetFrameDstMacMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 14, 1, 9),
    _HwAclEthernetFrameDstMacMask_Type()
)
hwAclEthernetFrameDstMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclEthernetFrameDstMacMask.setStatus("current")


class _HwAclEthernetFrameTimeRangeIndex_Type(Integer32):
    """Custom type hwAclEthernetFrameTimeRangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_HwAclEthernetFrameTimeRangeIndex_Type.__name__ = "Integer32"
_HwAclEthernetFrameTimeRangeIndex_Object = MibTableColumn
hwAclEthernetFrameTimeRangeIndex = _HwAclEthernetFrameTimeRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 14, 1, 10),
    _HwAclEthernetFrameTimeRangeIndex_Type()
)
hwAclEthernetFrameTimeRangeIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclEthernetFrameTimeRangeIndex.setStatus("current")
_HwAclEthernetFrameLog_Type = TruthValue
_HwAclEthernetFrameLog_Object = MibTableColumn
hwAclEthernetFrameLog = _HwAclEthernetFrameLog_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 14, 1, 11),
    _HwAclEthernetFrameLog_Type()
)
hwAclEthernetFrameLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclEthernetFrameLog.setStatus("current")
_HwAclEthernetFrameEnable_Type = EnabledStatus
_HwAclEthernetFrameEnable_Object = MibTableColumn
hwAclEthernetFrameEnable = _HwAclEthernetFrameEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 14, 1, 12),
    _HwAclEthernetFrameEnable_Type()
)
hwAclEthernetFrameEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclEthernetFrameEnable.setStatus("current")
_HwAclEthernetFrameCount_Type = Counter64
_HwAclEthernetFrameCount_Object = MibTableColumn
hwAclEthernetFrameCount = _HwAclEthernetFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 14, 1, 13),
    _HwAclEthernetFrameCount_Type()
)
hwAclEthernetFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclEthernetFrameCount.setStatus("current")
_HwAclEthernetFrameRowStatus_Type = RowStatus
_HwAclEthernetFrameRowStatus_Object = MibTableColumn
hwAclEthernetFrameRowStatus = _HwAclEthernetFrameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 14, 1, 14),
    _HwAclEthernetFrameRowStatus_Type()
)
hwAclEthernetFrameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclEthernetFrameRowStatus.setStatus("current")


class _HwAclEthernetFrameEncapType_Type(Integer32):
    """Custom type hwAclEthernetFrameEncapType based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ether2", 1),
          ("ieee802dot3", 2),
          ("none", 255),
          ("snap", 3))
    )


_HwAclEthernetFrameEncapType_Type.__name__ = "Integer32"
_HwAclEthernetFrameEncapType_Object = MibTableColumn
hwAclEthernetFrameEncapType = _HwAclEthernetFrameEncapType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 14, 1, 15),
    _HwAclEthernetFrameEncapType_Type()
)
hwAclEthernetFrameEncapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclEthernetFrameEncapType.setStatus("current")


class _HwAclEthernetFrameDoubleTag_Type(TruthValue):
    """Custom type hwAclEthernetFrameDoubleTag based on TruthValue"""


_HwAclEthernetFrameDoubleTag_Object = MibTableColumn
hwAclEthernetFrameDoubleTag = _HwAclEthernetFrameDoubleTag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 14, 1, 16),
    _HwAclEthernetFrameDoubleTag_Type()
)
hwAclEthernetFrameDoubleTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclEthernetFrameDoubleTag.setStatus("current")


class _HwAclEthernetFrameVlanId_Type(Integer32):
    """Custom type hwAclEthernetFrameVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwAclEthernetFrameVlanId_Type.__name__ = "Integer32"
_HwAclEthernetFrameVlanId_Object = MibTableColumn
hwAclEthernetFrameVlanId = _HwAclEthernetFrameVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 14, 1, 17),
    _HwAclEthernetFrameVlanId_Type()
)
hwAclEthernetFrameVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclEthernetFrameVlanId.setStatus("current")


class _HwAclEthernetFrameVlanIdMask_Type(Integer32):
    """Custom type hwAclEthernetFrameVlanIdMask based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HwAclEthernetFrameVlanIdMask_Type.__name__ = "Integer32"
_HwAclEthernetFrameVlanIdMask_Object = MibTableColumn
hwAclEthernetFrameVlanIdMask = _HwAclEthernetFrameVlanIdMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 14, 1, 18),
    _HwAclEthernetFrameVlanIdMask_Type()
)
hwAclEthernetFrameVlanIdMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclEthernetFrameVlanIdMask.setStatus("current")


class _HwAclEthernetFrameCVlanId_Type(Integer32):
    """Custom type hwAclEthernetFrameCVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwAclEthernetFrameCVlanId_Type.__name__ = "Integer32"
_HwAclEthernetFrameCVlanId_Object = MibTableColumn
hwAclEthernetFrameCVlanId = _HwAclEthernetFrameCVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 14, 1, 19),
    _HwAclEthernetFrameCVlanId_Type()
)
hwAclEthernetFrameCVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclEthernetFrameCVlanId.setStatus("current")


class _HwAclEthernetFrameCVlanIdMask_Type(Integer32):
    """Custom type hwAclEthernetFrameCVlanIdMask based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HwAclEthernetFrameCVlanIdMask_Type.__name__ = "Integer32"
_HwAclEthernetFrameCVlanIdMask_Object = MibTableColumn
hwAclEthernetFrameCVlanIdMask = _HwAclEthernetFrameCVlanIdMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 14, 1, 20),
    _HwAclEthernetFrameCVlanIdMask_Type()
)
hwAclEthernetFrameCVlanIdMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclEthernetFrameCVlanIdMask.setStatus("current")


class _HwAclEthernetFrameRule8021p_Type(Integer32):
    """Custom type hwAclEthernetFrameRule8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwAclEthernetFrameRule8021p_Type.__name__ = "Integer32"
_HwAclEthernetFrameRule8021p_Object = MibTableColumn
hwAclEthernetFrameRule8021p = _HwAclEthernetFrameRule8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 14, 1, 21),
    _HwAclEthernetFrameRule8021p_Type()
)
hwAclEthernetFrameRule8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclEthernetFrameRule8021p.setStatus("current")


class _HwAclEthernetFrameRuleCVlan8021p_Type(Integer32):
    """Custom type hwAclEthernetFrameRuleCVlan8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwAclEthernetFrameRuleCVlan8021p_Type.__name__ = "Integer32"
_HwAclEthernetFrameRuleCVlan8021p_Object = MibTableColumn
hwAclEthernetFrameRuleCVlan8021p = _HwAclEthernetFrameRuleCVlan8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 14, 1, 22),
    _HwAclEthernetFrameRuleCVlan8021p_Type()
)
hwAclEthernetFrameRuleCVlan8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclEthernetFrameRuleCVlan8021p.setStatus("current")


class _HwAclEthernetFrameDescription_Type(OctetString):
    """Custom type hwAclEthernetFrameDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HwAclEthernetFrameDescription_Type.__name__ = "OctetString"
_HwAclEthernetFrameDescription_Object = MibTableColumn
hwAclEthernetFrameDescription = _HwAclEthernetFrameDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 14, 1, 23),
    _HwAclEthernetFrameDescription_Type()
)
hwAclEthernetFrameDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclEthernetFrameDescription.setStatus("current")
_HwAclAppliedTable_Object = MibTable
hwAclAppliedTable = _HwAclAppliedTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15)
)
if mibBuilder.loadTexts:
    hwAclAppliedTable.setStatus("current")
_HwAclAppliedEntry_Object = MibTableRow
hwAclAppliedEntry = _HwAclAppliedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1)
)
hwAclAppliedEntry.setIndexNames(
    (0, "HUAWEI-ACL-MIB", "hwAclAppliedOperation"),
    (0, "HUAWEI-ACL-MIB", "hwAclAppliedScopeType"),
    (0, "HUAWEI-ACL-MIB", "hwAclAppliedScopeIndex"),
    (0, "HUAWEI-ACL-MIB", "hwAclAppliedDirection"),
    (0, "HUAWEI-ACL-MIB", "hwAclAppliedAclNum"),
    (0, "HUAWEI-ACL-MIB", "hwAclAppliedSubitem"),
    (0, "HUAWEI-ACL-MIB", "hwAclAppliedAclNum2"),
    (0, "HUAWEI-ACL-MIB", "hwAclAppliedSubitem2"),
    (0, "HUAWEI-ACL-MIB", "hwAclAppliedIsIPv6Acl"),
)
if mibBuilder.loadTexts:
    hwAclAppliedEntry.setStatus("current")


class _HwAclAppliedOperation_Type(Integer32):
    """Custom type hwAclAppliedOperation based on Integer32"""
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
        *(("filter", 1),
          ("limit", 2),
          ("mirror", 3),
          ("redirectCpu", 4),
          ("redirectInterface", 5),
          ("redirectIpNextHop", 6),
          ("redirectIpv6NextHop", 7),
          ("remark8021p", 8),
          ("remarkCVlanId", 13),
          ("remarkDestMac", 14),
          ("remarkDscp", 9),
          ("remarkIpPrecedence", 10),
          ("remarkLocalPrecedence", 11),
          ("remarkVlanId", 12),
          ("statistic", 15))
    )


_HwAclAppliedOperation_Type.__name__ = "Integer32"
_HwAclAppliedOperation_Object = MibTableColumn
hwAclAppliedOperation = _HwAclAppliedOperation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 1),
    _HwAclAppliedOperation_Type()
)
hwAclAppliedOperation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAclAppliedOperation.setStatus("current")


class _HwAclAppliedScopeType_Type(Integer32):
    """Custom type hwAclAppliedScopeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("global", 1),
          ("interface", 3),
          ("vlan", 2))
    )


_HwAclAppliedScopeType_Type.__name__ = "Integer32"
_HwAclAppliedScopeType_Object = MibTableColumn
hwAclAppliedScopeType = _HwAclAppliedScopeType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 2),
    _HwAclAppliedScopeType_Type()
)
hwAclAppliedScopeType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAclAppliedScopeType.setStatus("current")
_HwAclAppliedScopeIndex_Type = Integer32
_HwAclAppliedScopeIndex_Object = MibTableColumn
hwAclAppliedScopeIndex = _HwAclAppliedScopeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 3),
    _HwAclAppliedScopeIndex_Type()
)
hwAclAppliedScopeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAclAppliedScopeIndex.setStatus("current")


class _HwAclAppliedDirection_Type(Integer32):
    """Custom type hwAclAppliedDirection based on Integer32"""
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


_HwAclAppliedDirection_Type.__name__ = "Integer32"
_HwAclAppliedDirection_Object = MibTableColumn
hwAclAppliedDirection = _HwAclAppliedDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 4),
    _HwAclAppliedDirection_Type()
)
hwAclAppliedDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAclAppliedDirection.setStatus("current")


class _HwAclAppliedAclNum_Type(Integer32):
    """Custom type hwAclAppliedAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 4999),
    )


_HwAclAppliedAclNum_Type.__name__ = "Integer32"
_HwAclAppliedAclNum_Object = MibTableColumn
hwAclAppliedAclNum = _HwAclAppliedAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 5),
    _HwAclAppliedAclNum_Type()
)
hwAclAppliedAclNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAclAppliedAclNum.setStatus("current")
_HwAclAppliedSubitem_Type = Integer32
_HwAclAppliedSubitem_Object = MibTableColumn
hwAclAppliedSubitem = _HwAclAppliedSubitem_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 6),
    _HwAclAppliedSubitem_Type()
)
hwAclAppliedSubitem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAclAppliedSubitem.setStatus("current")


class _HwAclAppliedAclNum2_Type(Integer32):
    """Custom type hwAclAppliedAclNum2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(65535, 65535),
    )


_HwAclAppliedAclNum2_Type.__name__ = "Integer32"
_HwAclAppliedAclNum2_Object = MibTableColumn
hwAclAppliedAclNum2 = _HwAclAppliedAclNum2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 7),
    _HwAclAppliedAclNum2_Type()
)
hwAclAppliedAclNum2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAclAppliedAclNum2.setStatus("current")
_HwAclAppliedSubitem2_Type = Integer32
_HwAclAppliedSubitem2_Object = MibTableColumn
hwAclAppliedSubitem2 = _HwAclAppliedSubitem2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 8),
    _HwAclAppliedSubitem2_Type()
)
hwAclAppliedSubitem2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAclAppliedSubitem2.setStatus("current")


class _HwAclAppliedStatMode_Type(Integer32):
    """Custom type hwAclAppliedStatMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("byBytes", 2),
          ("byPackets", 1))
    )


_HwAclAppliedStatMode_Type.__name__ = "Integer32"
_HwAclAppliedStatMode_Object = MibTableColumn
hwAclAppliedStatMode = _HwAclAppliedStatMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 9),
    _HwAclAppliedStatMode_Type()
)
hwAclAppliedStatMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAppliedStatMode.setStatus("current")
_HwAclAppliedStatCount_Type = Counter64
_HwAclAppliedStatCount_Object = MibTableColumn
hwAclAppliedStatCount = _HwAclAppliedStatCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 10),
    _HwAclAppliedStatCount_Type()
)
hwAclAppliedStatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclAppliedStatCount.setStatus("current")


class _HwAclAppliedLimitCir_Type(Integer32):
    """Custom type hwAclAppliedLimitCir based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 10000000),
    )


_HwAclAppliedLimitCir_Type.__name__ = "Integer32"
_HwAclAppliedLimitCir_Object = MibTableColumn
hwAclAppliedLimitCir = _HwAclAppliedLimitCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 11),
    _HwAclAppliedLimitCir_Type()
)
hwAclAppliedLimitCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAppliedLimitCir.setStatus("current")


class _HwAclAppliedLimitPir_Type(Integer32):
    """Custom type hwAclAppliedLimitPir based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 10000000),
    )


_HwAclAppliedLimitPir_Type.__name__ = "Integer32"
_HwAclAppliedLimitPir_Object = MibTableColumn
hwAclAppliedLimitPir = _HwAclAppliedLimitPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 12),
    _HwAclAppliedLimitPir_Type()
)
hwAclAppliedLimitPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAppliedLimitPir.setStatus("current")


class _HwAclAppliedLimitCbs_Type(Integer32):
    """Custom type hwAclAppliedLimitCbs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4096, 16773120),
    )


_HwAclAppliedLimitCbs_Type.__name__ = "Integer32"
_HwAclAppliedLimitCbs_Object = MibTableColumn
hwAclAppliedLimitCbs = _HwAclAppliedLimitCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 13),
    _HwAclAppliedLimitCbs_Type()
)
hwAclAppliedLimitCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAppliedLimitCbs.setStatus("current")


class _HwAclAppliedLimitPbs_Type(Integer32):
    """Custom type hwAclAppliedLimitPbs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4096, 16773120),
    )


_HwAclAppliedLimitPbs_Type.__name__ = "Integer32"
_HwAclAppliedLimitPbs_Object = MibTableColumn
hwAclAppliedLimitPbs = _HwAclAppliedLimitPbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 14),
    _HwAclAppliedLimitPbs_Type()
)
hwAclAppliedLimitPbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAppliedLimitPbs.setStatus("current")


class _HwAclAppliedLimitGreenAction_Type(Integer32):
    """Custom type hwAclAppliedLimitGreenAction based on Integer32"""
    defaultValue = 1

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
        *(("drop", 2),
          ("pass", 1),
          ("passRemark8021p", 4),
          ("passRemarkDscp", 3))
    )


_HwAclAppliedLimitGreenAction_Type.__name__ = "Integer32"
_HwAclAppliedLimitGreenAction_Object = MibTableColumn
hwAclAppliedLimitGreenAction = _HwAclAppliedLimitGreenAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 15),
    _HwAclAppliedLimitGreenAction_Type()
)
hwAclAppliedLimitGreenAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAppliedLimitGreenAction.setStatus("current")


class _HwAclAppliedLimitGreenValue_Type(Integer32):
    """Custom type hwAclAppliedLimitGreenValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwAclAppliedLimitGreenValue_Type.__name__ = "Integer32"
_HwAclAppliedLimitGreenValue_Object = MibTableColumn
hwAclAppliedLimitGreenValue = _HwAclAppliedLimitGreenValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 16),
    _HwAclAppliedLimitGreenValue_Type()
)
hwAclAppliedLimitGreenValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAppliedLimitGreenValue.setStatus("current")


class _HwAclAppliedLimitYellowAction_Type(Integer32):
    """Custom type hwAclAppliedLimitYellowAction based on Integer32"""
    defaultValue = 1

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
        *(("drop", 2),
          ("pass", 1),
          ("passRemark8021p", 4),
          ("passRemarkDscp", 3))
    )


_HwAclAppliedLimitYellowAction_Type.__name__ = "Integer32"
_HwAclAppliedLimitYellowAction_Object = MibTableColumn
hwAclAppliedLimitYellowAction = _HwAclAppliedLimitYellowAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 17),
    _HwAclAppliedLimitYellowAction_Type()
)
hwAclAppliedLimitYellowAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAppliedLimitYellowAction.setStatus("current")


class _HwAclAppliedLimitYellowValue_Type(Integer32):
    """Custom type hwAclAppliedLimitYellowValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwAclAppliedLimitYellowValue_Type.__name__ = "Integer32"
_HwAclAppliedLimitYellowValue_Object = MibTableColumn
hwAclAppliedLimitYellowValue = _HwAclAppliedLimitYellowValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 18),
    _HwAclAppliedLimitYellowValue_Type()
)
hwAclAppliedLimitYellowValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAppliedLimitYellowValue.setStatus("current")


class _HwAclAppliedLimitRedAction_Type(Integer32):
    """Custom type hwAclAppliedLimitRedAction based on Integer32"""
    defaultValue = 2

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
        *(("drop", 2),
          ("pass", 1),
          ("passRemark8021p", 4),
          ("passRemarkDscp", 3))
    )


_HwAclAppliedLimitRedAction_Type.__name__ = "Integer32"
_HwAclAppliedLimitRedAction_Object = MibTableColumn
hwAclAppliedLimitRedAction = _HwAclAppliedLimitRedAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 19),
    _HwAclAppliedLimitRedAction_Type()
)
hwAclAppliedLimitRedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAppliedLimitRedAction.setStatus("current")


class _HwAclAppliedLimitRedValue_Type(Integer32):
    """Custom type hwAclAppliedLimitRedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwAclAppliedLimitRedValue_Type.__name__ = "Integer32"
_HwAclAppliedLimitRedValue_Object = MibTableColumn
hwAclAppliedLimitRedValue = _HwAclAppliedLimitRedValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 20),
    _HwAclAppliedLimitRedValue_Type()
)
hwAclAppliedLimitRedValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAppliedLimitRedValue.setStatus("current")
_HwAclAppliedMirrObservedPort_Type = Integer32
_HwAclAppliedMirrObservedPort_Object = MibTableColumn
hwAclAppliedMirrObservedPort = _HwAclAppliedMirrObservedPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 21),
    _HwAclAppliedMirrObservedPort_Type()
)
hwAclAppliedMirrObservedPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAppliedMirrObservedPort.setStatus("current")


class _HwAclAppliedMirrRspanVlan_Type(Integer32):
    """Custom type hwAclAppliedMirrRspanVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwAclAppliedMirrRspanVlan_Type.__name__ = "Integer32"
_HwAclAppliedMirrRspanVlan_Object = MibTableColumn
hwAclAppliedMirrRspanVlan = _HwAclAppliedMirrRspanVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 22),
    _HwAclAppliedMirrRspanVlan_Type()
)
hwAclAppliedMirrRspanVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAppliedMirrRspanVlan.setStatus("current")
_HwAclAppliedRedirectIfIndex_Type = Integer32
_HwAclAppliedRedirectIfIndex_Object = MibTableColumn
hwAclAppliedRedirectIfIndex = _HwAclAppliedRedirectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 23),
    _HwAclAppliedRedirectIfIndex_Type()
)
hwAclAppliedRedirectIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAppliedRedirectIfIndex.setStatus("current")
_HwAclAppliedRedirectIpAddr_Type = IpAddress
_HwAclAppliedRedirectIpAddr_Object = MibTableColumn
hwAclAppliedRedirectIpAddr = _HwAclAppliedRedirectIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 24),
    _HwAclAppliedRedirectIpAddr_Type()
)
hwAclAppliedRedirectIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAppliedRedirectIpAddr.setStatus("current")
_HwAclAppliedRedirectIpv6Addr_Type = Ipv6Address
_HwAclAppliedRedirectIpv6Addr_Object = MibTableColumn
hwAclAppliedRedirectIpv6Addr = _HwAclAppliedRedirectIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 25),
    _HwAclAppliedRedirectIpv6Addr_Type()
)
hwAclAppliedRedirectIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAppliedRedirectIpv6Addr.setStatus("current")


class _HwAclAppliedRemarkVlan_Type(Integer32):
    """Custom type hwAclAppliedRemarkVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwAclAppliedRemarkVlan_Type.__name__ = "Integer32"
_HwAclAppliedRemarkVlan_Object = MibTableColumn
hwAclAppliedRemarkVlan = _HwAclAppliedRemarkVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 26),
    _HwAclAppliedRemarkVlan_Type()
)
hwAclAppliedRemarkVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAppliedRemarkVlan.setStatus("current")


class _HwAclAppliedRemarkCVlan_Type(Integer32):
    """Custom type hwAclAppliedRemarkCVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwAclAppliedRemarkCVlan_Type.__name__ = "Integer32"
_HwAclAppliedRemarkCVlan_Object = MibTableColumn
hwAclAppliedRemarkCVlan = _HwAclAppliedRemarkCVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 27),
    _HwAclAppliedRemarkCVlan_Type()
)
hwAclAppliedRemarkCVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAppliedRemarkCVlan.setStatus("current")


class _HwAclAppliedRemark8021p_Type(Integer32):
    """Custom type hwAclAppliedRemark8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwAclAppliedRemark8021p_Type.__name__ = "Integer32"
_HwAclAppliedRemark8021p_Object = MibTableColumn
hwAclAppliedRemark8021p = _HwAclAppliedRemark8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 28),
    _HwAclAppliedRemark8021p_Type()
)
hwAclAppliedRemark8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAppliedRemark8021p.setStatus("current")


class _HwAclAppliedRemarkDscp_Type(Integer32):
    """Custom type hwAclAppliedRemarkDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwAclAppliedRemarkDscp_Type.__name__ = "Integer32"
_HwAclAppliedRemarkDscp_Object = MibTableColumn
hwAclAppliedRemarkDscp = _HwAclAppliedRemarkDscp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 29),
    _HwAclAppliedRemarkDscp_Type()
)
hwAclAppliedRemarkDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAppliedRemarkDscp.setStatus("current")


class _HwAclAppliedRemarkIpPre_Type(Integer32):
    """Custom type hwAclAppliedRemarkIpPre based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwAclAppliedRemarkIpPre_Type.__name__ = "Integer32"
_HwAclAppliedRemarkIpPre_Object = MibTableColumn
hwAclAppliedRemarkIpPre = _HwAclAppliedRemarkIpPre_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 30),
    _HwAclAppliedRemarkIpPre_Type()
)
hwAclAppliedRemarkIpPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAppliedRemarkIpPre.setStatus("current")


class _HwAclAppliedRemarkLocalPre_Type(Integer32):
    """Custom type hwAclAppliedRemarkLocalPre based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwAclAppliedRemarkLocalPre_Type.__name__ = "Integer32"
_HwAclAppliedRemarkLocalPre_Object = MibTableColumn
hwAclAppliedRemarkLocalPre = _HwAclAppliedRemarkLocalPre_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 31),
    _HwAclAppliedRemarkLocalPre_Type()
)
hwAclAppliedRemarkLocalPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAppliedRemarkLocalPre.setStatus("current")
_HwAclAppliedRemarkMacAddr_Type = MacAddress
_HwAclAppliedRemarkMacAddr_Object = MibTableColumn
hwAclAppliedRemarkMacAddr = _HwAclAppliedRemarkMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 32),
    _HwAclAppliedRemarkMacAddr_Type()
)
hwAclAppliedRemarkMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAppliedRemarkMacAddr.setStatus("current")
_HwAclAppliedIsIPv6Acl_Type = TruthValue
_HwAclAppliedIsIPv6Acl_Object = MibTableColumn
hwAclAppliedIsIPv6Acl = _HwAclAppliedIsIPv6Acl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 33),
    _HwAclAppliedIsIPv6Acl_Type()
)
hwAclAppliedIsIPv6Acl.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAclAppliedIsIPv6Acl.setStatus("current")
_HwAclAppliedRowStatus_Type = RowStatus
_HwAclAppliedRowStatus_Object = MibTableColumn
hwAclAppliedRowStatus = _HwAclAppliedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 15, 1, 51),
    _HwAclAppliedRowStatus_Type()
)
hwAclAppliedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclAppliedRowStatus.setStatus("current")
_HwAclIpv6NumGroupTable_Object = MibTable
hwAclIpv6NumGroupTable = _HwAclIpv6NumGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 16)
)
if mibBuilder.loadTexts:
    hwAclIpv6NumGroupTable.setStatus("current")
_HwAclIpv6NumGroupEntry_Object = MibTableRow
hwAclIpv6NumGroupEntry = _HwAclIpv6NumGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 16, 1)
)
hwAclIpv6NumGroupEntry.setIndexNames(
    (0, "HUAWEI-ACL-MIB", "hwAclIpv6NumGroupAclNum"),
)
if mibBuilder.loadTexts:
    hwAclIpv6NumGroupEntry.setStatus("current")
_HwAclIpv6NumGroupAclNum_Type = Integer32
_HwAclIpv6NumGroupAclNum_Object = MibTableColumn
hwAclIpv6NumGroupAclNum = _HwAclIpv6NumGroupAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 16, 1, 1),
    _HwAclIpv6NumGroupAclNum_Type()
)
hwAclIpv6NumGroupAclNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclIpv6NumGroupAclNum.setStatus("current")


class _HwAclIpv6NumGroupMatchOrder_Type(Integer32):
    """Custom type hwAclIpv6NumGroupMatchOrder based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("config", 1),
          ("default", 3))
    )


_HwAclIpv6NumGroupMatchOrder_Type.__name__ = "Integer32"
_HwAclIpv6NumGroupMatchOrder_Object = MibTableColumn
hwAclIpv6NumGroupMatchOrder = _HwAclIpv6NumGroupMatchOrder_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 16, 1, 2),
    _HwAclIpv6NumGroupMatchOrder_Type()
)
hwAclIpv6NumGroupMatchOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6NumGroupMatchOrder.setStatus("current")
_HwAclIpv6NumGroupSubitemNum_Type = Counter32
_HwAclIpv6NumGroupSubitemNum_Object = MibTableColumn
hwAclIpv6NumGroupSubitemNum = _HwAclIpv6NumGroupSubitemNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 16, 1, 3),
    _HwAclIpv6NumGroupSubitemNum_Type()
)
hwAclIpv6NumGroupSubitemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclIpv6NumGroupSubitemNum.setStatus("current")


class _HwAclIpv6NumGroupCountClear_Type(Integer32):
    """Custom type hwAclIpv6NumGroupCountClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("notUsed", 2))
    )


_HwAclIpv6NumGroupCountClear_Type.__name__ = "Integer32"
_HwAclIpv6NumGroupCountClear_Object = MibTableColumn
hwAclIpv6NumGroupCountClear = _HwAclIpv6NumGroupCountClear_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 16, 1, 4),
    _HwAclIpv6NumGroupCountClear_Type()
)
hwAclIpv6NumGroupCountClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6NumGroupCountClear.setStatus("current")


class _HwAclIpv6NumGroupAclName_Type(OctetString):
    """Custom type hwAclIpv6NumGroupAclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwAclIpv6NumGroupAclName_Type.__name__ = "OctetString"
_HwAclIpv6NumGroupAclName_Object = MibTableColumn
hwAclIpv6NumGroupAclName = _HwAclIpv6NumGroupAclName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 16, 1, 5),
    _HwAclIpv6NumGroupAclName_Type()
)
hwAclIpv6NumGroupAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6NumGroupAclName.setStatus("current")


class _HwAclIpv6NumGroupDescription_Type(OctetString):
    """Custom type hwAclIpv6NumGroupDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HwAclIpv6NumGroupDescription_Type.__name__ = "OctetString"
_HwAclIpv6NumGroupDescription_Object = MibTableColumn
hwAclIpv6NumGroupDescription = _HwAclIpv6NumGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 16, 1, 6),
    _HwAclIpv6NumGroupDescription_Type()
)
hwAclIpv6NumGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6NumGroupDescription.setStatus("current")


class _HwAclIpv6NumGroupAclType_Type(Integer32):
    """Custom type hwAclIpv6NumGroupAclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advanced", 2),
          ("basic", 1))
    )


_HwAclIpv6NumGroupAclType_Type.__name__ = "Integer32"
_HwAclIpv6NumGroupAclType_Object = MibTableColumn
hwAclIpv6NumGroupAclType = _HwAclIpv6NumGroupAclType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 16, 1, 7),
    _HwAclIpv6NumGroupAclType_Type()
)
hwAclIpv6NumGroupAclType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6NumGroupAclType.setStatus("current")
_HwAclIpv6NumGroupRowStatus_Type = RowStatus
_HwAclIpv6NumGroupRowStatus_Object = MibTableColumn
hwAclIpv6NumGroupRowStatus = _HwAclIpv6NumGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 16, 1, 51),
    _HwAclIpv6NumGroupRowStatus_Type()
)
hwAclIpv6NumGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6NumGroupRowStatus.setStatus("current")


class _HwAclIpv6NumGroupStep_Type(Integer32):
    """Custom type hwAclIpv6NumGroupStep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_HwAclIpv6NumGroupStep_Type.__name__ = "Integer32"
_HwAclIpv6NumGroupStep_Object = MibTableColumn
hwAclIpv6NumGroupStep = _HwAclIpv6NumGroupStep_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 16, 1, 52),
    _HwAclIpv6NumGroupStep_Type()
)
hwAclIpv6NumGroupStep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6NumGroupStep.setStatus("current")
_HwAclIpv6IfRuleTable_Object = MibTable
hwAclIpv6IfRuleTable = _HwAclIpv6IfRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 17)
)
if mibBuilder.loadTexts:
    hwAclIpv6IfRuleTable.setStatus("current")
_HwAclIpv6IfRuleEntry_Object = MibTableRow
hwAclIpv6IfRuleEntry = _HwAclIpv6IfRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 17, 1)
)
hwAclIpv6IfRuleEntry.setIndexNames(
    (0, "HUAWEI-ACL-MIB", "hwAclIpv6IfAclNum"),
    (0, "HUAWEI-ACL-MIB", "hwAclIpv6IfSubitem"),
)
if mibBuilder.loadTexts:
    hwAclIpv6IfRuleEntry.setStatus("current")
_HwAclIpv6IfAclNum_Type = Integer32
_HwAclIpv6IfAclNum_Object = MibTableColumn
hwAclIpv6IfAclNum = _HwAclIpv6IfAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 17, 1, 1),
    _HwAclIpv6IfAclNum_Type()
)
hwAclIpv6IfAclNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclIpv6IfAclNum.setStatus("current")
_HwAclIpv6IfSubitem_Type = Unsigned32
_HwAclIpv6IfSubitem_Object = MibTableColumn
hwAclIpv6IfSubitem = _HwAclIpv6IfSubitem_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 17, 1, 2),
    _HwAclIpv6IfSubitem_Type()
)
hwAclIpv6IfSubitem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclIpv6IfSubitem.setStatus("current")


class _HwAclIpv6IfAct_Type(Integer32):
    """Custom type hwAclIpv6IfAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_HwAclIpv6IfAct_Type.__name__ = "Integer32"
_HwAclIpv6IfAct_Object = MibTableColumn
hwAclIpv6IfAct = _HwAclIpv6IfAct_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 17, 1, 3),
    _HwAclIpv6IfAct_Type()
)
hwAclIpv6IfAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6IfAct.setStatus("current")
_HwAclIpv6IfIndex_Type = Integer32
_HwAclIpv6IfIndex_Object = MibTableColumn
hwAclIpv6IfIndex = _HwAclIpv6IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 17, 1, 4),
    _HwAclIpv6IfIndex_Type()
)
hwAclIpv6IfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6IfIndex.setStatus("current")
_HwAclIpv6IfAny_Type = TruthValue
_HwAclIpv6IfAny_Object = MibTableColumn
hwAclIpv6IfAny = _HwAclIpv6IfAny_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 17, 1, 5),
    _HwAclIpv6IfAny_Type()
)
hwAclIpv6IfAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6IfAny.setStatus("current")


class _HwAclIpv6IfTimeRangeIndex_Type(Integer32):
    """Custom type hwAclIpv6IfTimeRangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_HwAclIpv6IfTimeRangeIndex_Type.__name__ = "Integer32"
_HwAclIpv6IfTimeRangeIndex_Object = MibTableColumn
hwAclIpv6IfTimeRangeIndex = _HwAclIpv6IfTimeRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 17, 1, 6),
    _HwAclIpv6IfTimeRangeIndex_Type()
)
hwAclIpv6IfTimeRangeIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6IfTimeRangeIndex.setStatus("current")
_HwAclIpv6IfLog_Type = TruthValue
_HwAclIpv6IfLog_Object = MibTableColumn
hwAclIpv6IfLog = _HwAclIpv6IfLog_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 17, 1, 7),
    _HwAclIpv6IfLog_Type()
)
hwAclIpv6IfLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6IfLog.setStatus("current")
_HwAclIpv6IfEnable_Type = TruthValue
_HwAclIpv6IfEnable_Object = MibTableColumn
hwAclIpv6IfEnable = _HwAclIpv6IfEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 17, 1, 8),
    _HwAclIpv6IfEnable_Type()
)
hwAclIpv6IfEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclIpv6IfEnable.setStatus("current")
_HwAclIpv6IfCount_Type = Counter64
_HwAclIpv6IfCount_Object = MibTableColumn
hwAclIpv6IfCount = _HwAclIpv6IfCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 17, 1, 9),
    _HwAclIpv6IfCount_Type()
)
hwAclIpv6IfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclIpv6IfCount.setStatus("current")
_HwAclIpv6IfRowStatus_Type = RowStatus
_HwAclIpv6IfRowStatus_Object = MibTableColumn
hwAclIpv6IfRowStatus = _HwAclIpv6IfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 17, 1, 11),
    _HwAclIpv6IfRowStatus_Type()
)
hwAclIpv6IfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclIpv6IfRowStatus.setStatus("current")
_HwAclMplsRuleTable_Object = MibTable
hwAclMplsRuleTable = _HwAclMplsRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 18)
)
if mibBuilder.loadTexts:
    hwAclMplsRuleTable.setStatus("current")
_HwAclMplsRuleEntry_Object = MibTableRow
hwAclMplsRuleEntry = _HwAclMplsRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 18, 1)
)
hwAclMplsRuleEntry.setIndexNames(
    (0, "HUAWEI-ACL-MIB", "hwAclMplsAclNum"),
    (0, "HUAWEI-ACL-MIB", "hwAclMplsSubitem"),
)
if mibBuilder.loadTexts:
    hwAclMplsRuleEntry.setStatus("current")
_HwAclMplsAclNum_Type = Integer32
_HwAclMplsAclNum_Object = MibTableColumn
hwAclMplsAclNum = _HwAclMplsAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 18, 1, 1),
    _HwAclMplsAclNum_Type()
)
hwAclMplsAclNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclMplsAclNum.setStatus("current")
_HwAclMplsSubitem_Type = Unsigned32
_HwAclMplsSubitem_Object = MibTableColumn
hwAclMplsSubitem = _HwAclMplsSubitem_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 18, 1, 2),
    _HwAclMplsSubitem_Type()
)
hwAclMplsSubitem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclMplsSubitem.setStatus("current")


class _HwAclMplsAct_Type(Integer32):
    """Custom type hwAclMplsAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_HwAclMplsAct_Type.__name__ = "Integer32"
_HwAclMplsAct_Object = MibTableColumn
hwAclMplsAct = _HwAclMplsAct_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 18, 1, 3),
    _HwAclMplsAct_Type()
)
hwAclMplsAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclMplsAct.setStatus("current")


class _HwAclMplsExp1_Type(Integer32):
    """Custom type hwAclMplsExp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwAclMplsExp1_Type.__name__ = "Integer32"
_HwAclMplsExp1_Object = MibTableColumn
hwAclMplsExp1 = _HwAclMplsExp1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 18, 1, 4),
    _HwAclMplsExp1_Type()
)
hwAclMplsExp1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclMplsExp1.setStatus("current")


class _HwAclMplsExp2_Type(Integer32):
    """Custom type hwAclMplsExp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwAclMplsExp2_Type.__name__ = "Integer32"
_HwAclMplsExp2_Object = MibTableColumn
hwAclMplsExp2 = _HwAclMplsExp2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 18, 1, 5),
    _HwAclMplsExp2_Type()
)
hwAclMplsExp2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclMplsExp2.setStatus("current")


class _HwAclMplsExp3_Type(Integer32):
    """Custom type hwAclMplsExp3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwAclMplsExp3_Type.__name__ = "Integer32"
_HwAclMplsExp3_Object = MibTableColumn
hwAclMplsExp3 = _HwAclMplsExp3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 18, 1, 6),
    _HwAclMplsExp3_Type()
)
hwAclMplsExp3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclMplsExp3.setStatus("current")


class _HwAclMplsExp4_Type(Integer32):
    """Custom type hwAclMplsExp4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwAclMplsExp4_Type.__name__ = "Integer32"
_HwAclMplsExp4_Object = MibTableColumn
hwAclMplsExp4 = _HwAclMplsExp4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 18, 1, 7),
    _HwAclMplsExp4_Type()
)
hwAclMplsExp4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclMplsExp4.setStatus("current")


class _HwAclMplsLabel1_Type(Integer32):
    """Custom type hwAclMplsLabel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1048575),
    )


_HwAclMplsLabel1_Type.__name__ = "Integer32"
_HwAclMplsLabel1_Object = MibTableColumn
hwAclMplsLabel1 = _HwAclMplsLabel1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 18, 1, 8),
    _HwAclMplsLabel1_Type()
)
hwAclMplsLabel1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclMplsLabel1.setStatus("current")


class _HwAclMplsLabel2_Type(Integer32):
    """Custom type hwAclMplsLabel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1048575),
    )


_HwAclMplsLabel2_Type.__name__ = "Integer32"
_HwAclMplsLabel2_Object = MibTableColumn
hwAclMplsLabel2 = _HwAclMplsLabel2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 18, 1, 9),
    _HwAclMplsLabel2_Type()
)
hwAclMplsLabel2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclMplsLabel2.setStatus("current")


class _HwAclMplsLabel3_Type(Integer32):
    """Custom type hwAclMplsLabel3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1048575),
    )


_HwAclMplsLabel3_Type.__name__ = "Integer32"
_HwAclMplsLabel3_Object = MibTableColumn
hwAclMplsLabel3 = _HwAclMplsLabel3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 18, 1, 10),
    _HwAclMplsLabel3_Type()
)
hwAclMplsLabel3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclMplsLabel3.setStatus("current")


class _HwAclMplsLabel4_Type(Integer32):
    """Custom type hwAclMplsLabel4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1048575),
    )


_HwAclMplsLabel4_Type.__name__ = "Integer32"
_HwAclMplsLabel4_Object = MibTableColumn
hwAclMplsLabel4 = _HwAclMplsLabel4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 18, 1, 11),
    _HwAclMplsLabel4_Type()
)
hwAclMplsLabel4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclMplsLabel4.setStatus("current")


class _HwAclMplsTTLOP1_Type(Integer32):
    """Custom type hwAclMplsTTLOP1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("any", 255),
          ("eq", 2),
          ("gt", 3),
          ("invalid", 0),
          ("lt", 1),
          ("range", 5))
    )


_HwAclMplsTTLOP1_Type.__name__ = "Integer32"
_HwAclMplsTTLOP1_Object = MibTableColumn
hwAclMplsTTLOP1 = _HwAclMplsTTLOP1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 18, 1, 12),
    _HwAclMplsTTLOP1_Type()
)
hwAclMplsTTLOP1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclMplsTTLOP1.setStatus("current")


class _HwAclMplsTTL1Begin_Type(Integer32):
    """Custom type hwAclMplsTTL1Begin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwAclMplsTTL1Begin_Type.__name__ = "Integer32"
_HwAclMplsTTL1Begin_Object = MibTableColumn
hwAclMplsTTL1Begin = _HwAclMplsTTL1Begin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 18, 1, 13),
    _HwAclMplsTTL1Begin_Type()
)
hwAclMplsTTL1Begin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclMplsTTL1Begin.setStatus("current")


class _HwAclMplsTTL1End_Type(Integer32):
    """Custom type hwAclMplsTTL1End based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwAclMplsTTL1End_Type.__name__ = "Integer32"
_HwAclMplsTTL1End_Object = MibTableColumn
hwAclMplsTTL1End = _HwAclMplsTTL1End_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 18, 1, 14),
    _HwAclMplsTTL1End_Type()
)
hwAclMplsTTL1End.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclMplsTTL1End.setStatus("current")


class _HwAclMplsTTLOP2_Type(Integer32):
    """Custom type hwAclMplsTTLOP2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("any", 255),
          ("eq", 2),
          ("gt", 3),
          ("invalid", 0),
          ("lt", 1),
          ("range", 5))
    )


_HwAclMplsTTLOP2_Type.__name__ = "Integer32"
_HwAclMplsTTLOP2_Object = MibTableColumn
hwAclMplsTTLOP2 = _HwAclMplsTTLOP2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 18, 1, 15),
    _HwAclMplsTTLOP2_Type()
)
hwAclMplsTTLOP2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclMplsTTLOP2.setStatus("current")


class _HwAclMplsTTL2Begin_Type(Integer32):
    """Custom type hwAclMplsTTL2Begin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwAclMplsTTL2Begin_Type.__name__ = "Integer32"
_HwAclMplsTTL2Begin_Object = MibTableColumn
hwAclMplsTTL2Begin = _HwAclMplsTTL2Begin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 18, 1, 16),
    _HwAclMplsTTL2Begin_Type()
)
hwAclMplsTTL2Begin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclMplsTTL2Begin.setStatus("current")


class _HwAclMplsTTL2End_Type(Integer32):
    """Custom type hwAclMplsTTL2End based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwAclMplsTTL2End_Type.__name__ = "Integer32"
_HwAclMplsTTL2End_Object = MibTableColumn
hwAclMplsTTL2End = _HwAclMplsTTL2End_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 18, 1, 17),
    _HwAclMplsTTL2End_Type()
)
hwAclMplsTTL2End.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclMplsTTL2End.setStatus("current")


class _HwAclMplsTTLOP3_Type(Integer32):
    """Custom type hwAclMplsTTLOP3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("any", 255),
          ("eq", 2),
          ("gt", 3),
          ("invalid", 0),
          ("lt", 1),
          ("range", 5))
    )


_HwAclMplsTTLOP3_Type.__name__ = "Integer32"
_HwAclMplsTTLOP3_Object = MibTableColumn
hwAclMplsTTLOP3 = _HwAclMplsTTLOP3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 18, 1, 18),
    _HwAclMplsTTLOP3_Type()
)
hwAclMplsTTLOP3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclMplsTTLOP3.setStatus("current")


class _HwAclMplsTTL3Begin_Type(Integer32):
    """Custom type hwAclMplsTTL3Begin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwAclMplsTTL3Begin_Type.__name__ = "Integer32"
_HwAclMplsTTL3Begin_Object = MibTableColumn
hwAclMplsTTL3Begin = _HwAclMplsTTL3Begin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 18, 1, 19),
    _HwAclMplsTTL3Begin_Type()
)
hwAclMplsTTL3Begin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclMplsTTL3Begin.setStatus("current")


class _HwAclMplsTTL3End_Type(Integer32):
    """Custom type hwAclMplsTTL3End based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwAclMplsTTL3End_Type.__name__ = "Integer32"
_HwAclMplsTTL3End_Object = MibTableColumn
hwAclMplsTTL3End = _HwAclMplsTTL3End_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 18, 1, 20),
    _HwAclMplsTTL3End_Type()
)
hwAclMplsTTL3End.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclMplsTTL3End.setStatus("current")
_HwAclMplsRowStatus_Type = RowStatus
_HwAclMplsRowStatus_Object = MibTableColumn
hwAclMplsRowStatus = _HwAclMplsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 18, 1, 21),
    _HwAclMplsRowStatus_Type()
)
hwAclMplsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclMplsRowStatus.setStatus("current")
_HwAclMplsCount_Type = Counter64
_HwAclMplsCount_Object = MibTableColumn
hwAclMplsCount = _HwAclMplsCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 18, 1, 22),
    _HwAclMplsCount_Type()
)
hwAclMplsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAclMplsCount.setStatus("current")
_HwAclDomainNameConfigTable_Object = MibTable
hwAclDomainNameConfigTable = _HwAclDomainNameConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 19)
)
if mibBuilder.loadTexts:
    hwAclDomainNameConfigTable.setStatus("current")
_HwAclDomainNameConfigEntry_Object = MibTableRow
hwAclDomainNameConfigEntry = _HwAclDomainNameConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 19, 1)
)
hwAclDomainNameConfigEntry.setIndexNames(
    (0, "HUAWEI-ACL-MIB", "hwAclDomainID"),
)
if mibBuilder.loadTexts:
    hwAclDomainNameConfigEntry.setStatus("current")
_HwAclDomainID_Type = Integer32
_HwAclDomainID_Object = MibTableColumn
hwAclDomainID = _HwAclDomainID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 19, 1, 1),
    _HwAclDomainID_Type()
)
hwAclDomainID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAclDomainID.setStatus("current")


class _HwAclDomainName_Type(OctetString):
    """Custom type hwAclDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 127),
    )


_HwAclDomainName_Type.__name__ = "OctetString"
_HwAclDomainName_Object = MibTableColumn
hwAclDomainName = _HwAclDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 19, 1, 2),
    _HwAclDomainName_Type()
)
hwAclDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAclDomainName.setStatus("current")
_HwAclDomainNameConfigRowStatus_Type = RowStatus
_HwAclDomainNameConfigRowStatus_Object = MibTableColumn
hwAclDomainNameConfigRowStatus = _HwAclDomainNameConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 1, 19, 1, 3),
    _HwAclDomainNameConfigRowStatus_Type()
)
hwAclDomainNameConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAclDomainNameConfigRowStatus.setStatus("current")
_HwAclMibTrap_ObjectIdentity = ObjectIdentity
hwAclMibTrap = _HwAclMibTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 2)
)
_HwAclTrapOid_ObjectIdentity = ObjectIdentity
hwAclTrapOid = _HwAclTrapOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 2, 1)
)
_HwAclTrapsDefine_ObjectIdentity = ObjectIdentity
hwAclTrapsDefine = _HwAclTrapsDefine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 2, 2)
)
_HwAclTraps_ObjectIdentity = ObjectIdentity
hwAclTraps = _HwAclTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 2, 2, 1)
)
_HwAclResourceTrapsTable_ObjectIdentity = ObjectIdentity
hwAclResourceTrapsTable = _HwAclResourceTrapsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 2, 2, 1, 1)
)
_HwAclResSlotStr_Type = OctetString
_HwAclResSlotStr_Object = MibScalar
hwAclResSlotStr = _HwAclResSlotStr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 2, 2, 1, 1, 1),
    _HwAclResSlotStr_Type()
)
hwAclResSlotStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAclResSlotStr.setStatus("current")
_HwAclResStage_Type = OctetString
_HwAclResStage_Object = MibScalar
hwAclResStage = _HwAclResStage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 2, 2, 1, 1, 2),
    _HwAclResStage_Type()
)
hwAclResStage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAclResStage.setStatus("current")
_HwAclResLimit_Type = Integer32
_HwAclResLimit_Object = MibScalar
hwAclResLimit = _HwAclResLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 2, 2, 1, 1, 3),
    _HwAclResLimit_Type()
)
hwAclResLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAclResLimit.setStatus("current")
_HwAclResourceTrapsEntry_ObjectIdentity = ObjectIdentity
hwAclResourceTrapsEntry = _HwAclResourceTrapsEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 2, 2, 1, 1, 4)
)
_HwAclResourceTrapsGroups_ObjectIdentity = ObjectIdentity
hwAclResourceTrapsGroups = _HwAclResourceTrapsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 2, 2, 1, 1, 5)
)
_HwAclMibConformance_ObjectIdentity = ObjectIdentity
hwAclMibConformance = _HwAclMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 3)
)
_HwAclMibCompliances_ObjectIdentity = ObjectIdentity
hwAclMibCompliances = _HwAclMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 3, 1)
)
_HwAclMibGroups_ObjectIdentity = ObjectIdentity
hwAclMibGroups = _HwAclMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 3, 2)
)
hwAclNumGroupEntry.registerAugmentions(
    ("HUAWEI-ACL-MIB",
     "hwAclCompileNumGroupEntry")
)
hwAclCompileNumGroupEntry.setIndexNames(*hwAclNumGroupEntry.getIndexNames())

# Managed Objects groups

hwAclGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 3, 2, 1)
)
hwAclGroup.setObjects(
      *(("HUAWEI-ACL-MIB", "hwAclNumGroupMatchOrder"),
        ("HUAWEI-ACL-MIB", "hwAclNumGroupSubitemNum"),
        ("HUAWEI-ACL-MIB", "hwAclNumGroupAclName"),
        ("HUAWEI-ACL-MIB", "hwAclBasicAct"),
        ("HUAWEI-ACL-MIB", "hwAclBasicSrcIp"),
        ("HUAWEI-ACL-MIB", "hwAclBasicSrcWild"),
        ("HUAWEI-ACL-MIB", "hwAclBasicTimeRangeIndex"),
        ("HUAWEI-ACL-MIB", "hwAclBasicFragments"),
        ("HUAWEI-ACL-MIB", "hwAclBasicLog"),
        ("HUAWEI-ACL-MIB", "hwAclBasicEnable"),
        ("HUAWEI-ACL-MIB", "hwAclBasicCount"),
        ("HUAWEI-ACL-MIB", "hwAclBasicRowStatus"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedAct"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedProtocol"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedSrcIp"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedSrcWild"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedSrcOp"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedSrcPort1"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedSrcPort2"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedDestIp"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedDestWild"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedDestOp"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedDestPort1"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedDestPort2"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedPrecedence"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedTos"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedDscp"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedEstablish"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedTimeRangeIndex"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedIcmpType"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedIcmpCode"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedFragments"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedLog"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedEnable"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedCount"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedRowStatus"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedTcpSyncFlag"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedSrcPoolName"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedDestPoolName"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedProtocolNew"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedVni"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedIgmpType"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedTtlOp"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedTtlExpire"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedTtlExpireEnd"),
        ("HUAWEI-ACL-MIB", "hwAclIfAct"),
        ("HUAWEI-ACL-MIB", "hwAclIfIndex"),
        ("HUAWEI-ACL-MIB", "hwAclIfAny"),
        ("HUAWEI-ACL-MIB", "hwAclIfTimeRangeIndex"),
        ("HUAWEI-ACL-MIB", "hwAclIfLog"),
        ("HUAWEI-ACL-MIB", "hwAclIfEnable"),
        ("HUAWEI-ACL-MIB", "hwAclIfCount"),
        ("HUAWEI-ACL-MIB", "hwAclIfRowStatus"),
        ("HUAWEI-ACL-MIB", "hwAclUserAct"),
        ("HUAWEI-ACL-MIB", "hwAclUserProtocol"),
        ("HUAWEI-ACL-MIB", "hwAclUserSrcIp"),
        ("HUAWEI-ACL-MIB", "hwAclUserSrcWild"),
        ("HUAWEI-ACL-MIB", "hwAclUserSrcOp"),
        ("HUAWEI-ACL-MIB", "hwAclUserSrcPort1"),
        ("HUAWEI-ACL-MIB", "hwAclUserSrcPort2"),
        ("HUAWEI-ACL-MIB", "hwAclUserDestIp"),
        ("HUAWEI-ACL-MIB", "hwAclUserDestWild"),
        ("HUAWEI-ACL-MIB", "hwAclUserDestOp"),
        ("HUAWEI-ACL-MIB", "hwAclUserDestPort1"),
        ("HUAWEI-ACL-MIB", "hwAclUserDestPort2"),
        ("HUAWEI-ACL-MIB", "hwAclUserPrecedence"),
        ("HUAWEI-ACL-MIB", "hwAclUserTos"),
        ("HUAWEI-ACL-MIB", "hwAclUserDscp"),
        ("HUAWEI-ACL-MIB", "hwAclUserEstablish"),
        ("HUAWEI-ACL-MIB", "hwAclUserTimeRangeIndex"),
        ("HUAWEI-ACL-MIB", "hwAclUserIcmpType"),
        ("HUAWEI-ACL-MIB", "hwAclUserIcmpCode"),
        ("HUAWEI-ACL-MIB", "hwAclUserFragments"),
        ("HUAWEI-ACL-MIB", "hwAclUserLog"),
        ("HUAWEI-ACL-MIB", "hwAclUserEnable"),
        ("HUAWEI-ACL-MIB", "hwAclUserCount"),
        ("HUAWEI-ACL-MIB", "hwAclUserSrcUserGroupName"),
        ("HUAWEI-ACL-MIB", "hwAclUserDestUserGroupName"),
        ("HUAWEI-ACL-MIB", "hwAclUserSrcModeType"),
        ("HUAWEI-ACL-MIB", "hwAclUserDestModeType"),
        ("HUAWEI-ACL-MIB", "hwAclUserRowStatus"),
        ("HUAWEI-ACL-MIB", "hwAclCompileEnableFlag"),
        ("HUAWEI-ACL-MIB", "hwAclNumGroupAclNum"),
        ("HUAWEI-ACL-MIB", "hwAclBasicAclNum"),
        ("HUAWEI-ACL-MIB", "hwAclBasicSubitem"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedAclNum"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedSubitem"),
        ("HUAWEI-ACL-MIB", "hwAclIfAclNum"),
        ("HUAWEI-ACL-MIB", "hwAclIfSubitem"),
        ("HUAWEI-ACL-MIB", "hwAclUserAclNum"),
        ("HUAWEI-ACL-MIB", "hwAclUserSubitem"),
        ("HUAWEI-ACL-MIB", "hwAclUserVrfName"),
        ("HUAWEI-ACL-MIB", "hwAclUserTcpSyncFlag"),
        ("HUAWEI-ACL-MIB", "hwAclEthernetFrameEncapType"),
        ("HUAWEI-ACL-MIB", "hwAclEthernetFrameDoubleTag"),
        ("HUAWEI-ACL-MIB", "hwAclEthernetFrameVlanId"),
        ("HUAWEI-ACL-MIB", "hwAclEthernetFrameVlanIdMask"),
        ("HUAWEI-ACL-MIB", "hwAclEthernetFrameCVlanId"),
        ("HUAWEI-ACL-MIB", "hwAclEthernetFrameCVlanIdMask"),
        ("HUAWEI-ACL-MIB", "hwAclAppliedStatMode"),
        ("HUAWEI-ACL-MIB", "hwAclAppliedStatCount"),
        ("HUAWEI-ACL-MIB", "hwAclAppliedLimitCir"),
        ("HUAWEI-ACL-MIB", "hwAclAppliedLimitPir"),
        ("HUAWEI-ACL-MIB", "hwAclAppliedLimitCbs"),
        ("HUAWEI-ACL-MIB", "hwAclAppliedLimitPbs"),
        ("HUAWEI-ACL-MIB", "hwAclAppliedLimitGreenAction"),
        ("HUAWEI-ACL-MIB", "hwAclAppliedLimitGreenValue"),
        ("HUAWEI-ACL-MIB", "hwAclAppliedLimitYellowAction"),
        ("HUAWEI-ACL-MIB", "hwAclAppliedLimitYellowValue"),
        ("HUAWEI-ACL-MIB", "hwAclAppliedLimitRedAction"),
        ("HUAWEI-ACL-MIB", "hwAclAppliedLimitRedValue"),
        ("HUAWEI-ACL-MIB", "hwAclAppliedMirrObservedPort"),
        ("HUAWEI-ACL-MIB", "hwAclAppliedMirrRspanVlan"),
        ("HUAWEI-ACL-MIB", "hwAclAppliedRedirectIfIndex"),
        ("HUAWEI-ACL-MIB", "hwAclAppliedRedirectIpAddr"),
        ("HUAWEI-ACL-MIB", "hwAclAppliedRedirectIpv6Addr"),
        ("HUAWEI-ACL-MIB", "hwAclAppliedRemarkVlan"),
        ("HUAWEI-ACL-MIB", "hwAclAppliedRemarkCVlan"),
        ("HUAWEI-ACL-MIB", "hwAclAppliedRemark8021p"),
        ("HUAWEI-ACL-MIB", "hwAclAppliedRemarkDscp"),
        ("HUAWEI-ACL-MIB", "hwAclAppliedRemarkIpPre"),
        ("HUAWEI-ACL-MIB", "hwAclAppliedRemarkLocalPre"),
        ("HUAWEI-ACL-MIB", "hwAclAppliedRemarkMacAddr"),
        ("HUAWEI-ACL-MIB", "hwAclAppliedRowStatus"),
        ("HUAWEI-ACL-MIB", "hwAclCompileNumGroupStatus"),
        ("HUAWEI-ACL-MIB", "hwAclNumGroupStep"),
        ("HUAWEI-ACL-MIB", "hwAclNumGroupDescription"),
        ("HUAWEI-ACL-MIB", "hwAclNumGroupCountClear"),
        ("HUAWEI-ACL-MIB", "hwAclNumGroupRowStatus"),
        ("HUAWEI-ACL-MIB", "hwAclBasicVrfName"),
        ("HUAWEI-ACL-MIB", "hwAclAdvancedVrfName"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6BasicAct"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6BasicSrcIp"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6BasicSrcPrefix"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6BasicTimeRangeIndex"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6BasicFragment"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6BasicLog"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6BasicEnable"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6BasicCount"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6BasicVrfName"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6BasicRowStatus"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedAct"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedProtocol"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedSrcIp"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedSrcPrefix"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedSrcOp"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedSrcPort1"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedSrcPort2"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedDestIp"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedDestPrefix"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedDestOp"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedDestPort1"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedDestPort2"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedPrecedence"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedTos"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedDscp"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedEstablish"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedTimeRangeIndex"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedIcmpType"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedIcmpCode"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedFragment"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedLog"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedEnable"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedCount"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedVrfName"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedRowStatus"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedProtocolNew"),
        ("HUAWEI-ACL-MIB", "hwAclEthernetFrameAct"),
        ("HUAWEI-ACL-MIB", "hwAclEthernetFrameType"),
        ("HUAWEI-ACL-MIB", "hwAclEthernetFrameTypeMask"),
        ("HUAWEI-ACL-MIB", "hwAclEthernetFrameSrcMac"),
        ("HUAWEI-ACL-MIB", "hwAclEthernetFrameSrcMacMask"),
        ("HUAWEI-ACL-MIB", "hwAclEthernetFrameDstMac"),
        ("HUAWEI-ACL-MIB", "hwAclEthernetFrameDstMacMask"),
        ("HUAWEI-ACL-MIB", "hwAclEthernetFrameTimeRangeIndex"),
        ("HUAWEI-ACL-MIB", "hwAclEthernetFrameLog"),
        ("HUAWEI-ACL-MIB", "hwAclEthernetFrameEnable"),
        ("HUAWEI-ACL-MIB", "hwAclEthernetFrameCount"),
        ("HUAWEI-ACL-MIB", "hwAclEthernetFrameRowStatus"),
        ("HUAWEI-ACL-MIB", "hwAclEthernetFrameRule8021p"),
        ("HUAWEI-ACL-MIB", "hwAclEthernetFrameRuleCVlan8021p"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6NumGroupMatchOrder"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6NumGroupSubitemNum"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6NumGroupCountClear"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6NumGroupRowStatus"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6NumGroupAclName"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6IfAct"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6IfIndex"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6IfAny"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6IfTimeRangeIndex"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6IfLog"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6IfEnable"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6IfCount"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6IfRowStatus"),
        ("HUAWEI-ACL-MIB", "hwAclMplsAct"),
        ("HUAWEI-ACL-MIB", "hwAclMplsExp1"),
        ("HUAWEI-ACL-MIB", "hwAclMplsExp2"),
        ("HUAWEI-ACL-MIB", "hwAclMplsExp3"),
        ("HUAWEI-ACL-MIB", "hwAclMplsExp4"),
        ("HUAWEI-ACL-MIB", "hwAclMplsLabel1"),
        ("HUAWEI-ACL-MIB", "hwAclMplsLabel2"),
        ("HUAWEI-ACL-MIB", "hwAclMplsLabel3"),
        ("HUAWEI-ACL-MIB", "hwAclMplsLabel4"),
        ("HUAWEI-ACL-MIB", "hwAclMplsTTLOP1"),
        ("HUAWEI-ACL-MIB", "hwAclMplsTTL1Begin"),
        ("HUAWEI-ACL-MIB", "hwAclMplsTTL1End"),
        ("HUAWEI-ACL-MIB", "hwAclMplsTTLOP2"),
        ("HUAWEI-ACL-MIB", "hwAclMplsTTL2Begin"),
        ("HUAWEI-ACL-MIB", "hwAclMplsTTL2End"),
        ("HUAWEI-ACL-MIB", "hwAclMplsTTLOP3"),
        ("HUAWEI-ACL-MIB", "hwAclMplsTTL3Begin"),
        ("HUAWEI-ACL-MIB", "hwAclMplsTTL3End"),
        ("HUAWEI-ACL-MIB", "hwAclMplsRowStatus"),
        ("HUAWEI-ACL-MIB", "hwAclMplsCount"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6BasicSrcMask"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedSrcMask"),
        ("HUAWEI-ACL-MIB", "hwAclIpv6AdvancedDestMask"))
)
if mibBuilder.loadTexts:
    hwAclGroup.setStatus("current")


# Notification objects

hwAclResThresholdExceedClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 2, 2, 1, 1, 4, 1)
)
hwAclResThresholdExceedClearTrap.setObjects(
      *(("HUAWEI-ACL-MIB", "hwAclResLimit"),
        ("HUAWEI-ACL-MIB", "hwAclResSlotStr"),
        ("HUAWEI-ACL-MIB", "hwAclResStage"))
)
if mibBuilder.loadTexts:
    hwAclResThresholdExceedClearTrap.setStatus(
        "current"
    )

hwAclResThresholdExceedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 2, 2, 1, 1, 4, 2)
)
hwAclResThresholdExceedTrap.setObjects(
      *(("HUAWEI-ACL-MIB", "hwAclResLimit"),
        ("HUAWEI-ACL-MIB", "hwAclResSlotStr"),
        ("HUAWEI-ACL-MIB", "hwAclResStage"))
)
if mibBuilder.loadTexts:
    hwAclResThresholdExceedTrap.setStatus(
        "current"
    )

hwAclResTotalCountExceedClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 2, 2, 1, 1, 4, 3)
)
hwAclResTotalCountExceedClearTrap.setObjects(
      *(("HUAWEI-ACL-MIB", "hwAclResLimit"),
        ("HUAWEI-ACL-MIB", "hwAclResSlotStr"),
        ("HUAWEI-ACL-MIB", "hwAclResStage"))
)
if mibBuilder.loadTexts:
    hwAclResTotalCountExceedClearTrap.setStatus(
        "current"
    )

hwAclResTotalCountExceedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 2, 2, 1, 1, 4, 4)
)
hwAclResTotalCountExceedTrap.setObjects(
      *(("HUAWEI-ACL-MIB", "hwAclResLimit"),
        ("HUAWEI-ACL-MIB", "hwAclResSlotStr"),
        ("HUAWEI-ACL-MIB", "hwAclResStage"))
)
if mibBuilder.loadTexts:
    hwAclResTotalCountExceedTrap.setStatus(
        "current"
    )


# Notifications groups

hwAclResourceTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 2, 2, 1, 1, 5, 1)
)
hwAclResourceTrapsGroup.setObjects(
      *(("HUAWEI-ACL-MIB", "hwAclResThresholdExceedClearTrap"),
        ("HUAWEI-ACL-MIB", "hwAclResThresholdExceedTrap"),
        ("HUAWEI-ACL-MIB", "hwAclResTotalCountExceedClearTrap"),
        ("HUAWEI-ACL-MIB", "hwAclResTotalCountExceedTrap"))
)
if mibBuilder.loadTexts:
    hwAclResourceTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwAclMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwAclMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-ACL-MIB",
    **{"hwAcl": hwAcl,
       "hwAclMibObjects": hwAclMibObjects,
       "hwAclNumGroupTable": hwAclNumGroupTable,
       "hwAclNumGroupEntry": hwAclNumGroupEntry,
       "hwAclNumGroupAclNum": hwAclNumGroupAclNum,
       "hwAclNumGroupMatchOrder": hwAclNumGroupMatchOrder,
       "hwAclNumGroupSubitemNum": hwAclNumGroupSubitemNum,
       "hwAclNumGroupStep": hwAclNumGroupStep,
       "hwAclNumGroupDescription": hwAclNumGroupDescription,
       "hwAclNumGroupCountClear": hwAclNumGroupCountClear,
       "hwAclNumGroupRowStatus": hwAclNumGroupRowStatus,
       "hwAclNumGroupAclName": hwAclNumGroupAclName,
       "hwAclNumGroupAclType": hwAclNumGroupAclType,
       "hwAclBasicRuleTable": hwAclBasicRuleTable,
       "hwAclBasicRuleEntry": hwAclBasicRuleEntry,
       "hwAclBasicAclNum": hwAclBasicAclNum,
       "hwAclBasicSubitem": hwAclBasicSubitem,
       "hwAclBasicAct": hwAclBasicAct,
       "hwAclBasicSrcIp": hwAclBasicSrcIp,
       "hwAclBasicSrcWild": hwAclBasicSrcWild,
       "hwAclBasicTimeRangeIndex": hwAclBasicTimeRangeIndex,
       "hwAclBasicFragments": hwAclBasicFragments,
       "hwAclBasicLog": hwAclBasicLog,
       "hwAclBasicEnable": hwAclBasicEnable,
       "hwAclBasicCount": hwAclBasicCount,
       "hwAclBasicVrfName": hwAclBasicVrfName,
       "hwAclBasicRowStatus": hwAclBasicRowStatus,
       "hwAclBasicDescription": hwAclBasicDescription,
       "hwAclAdvancedRuleTable": hwAclAdvancedRuleTable,
       "hwAclAdvancedRuleEntry": hwAclAdvancedRuleEntry,
       "hwAclAdvancedAclNum": hwAclAdvancedAclNum,
       "hwAclAdvancedSubitem": hwAclAdvancedSubitem,
       "hwAclAdvancedAct": hwAclAdvancedAct,
       "hwAclAdvancedProtocol": hwAclAdvancedProtocol,
       "hwAclAdvancedSrcIp": hwAclAdvancedSrcIp,
       "hwAclAdvancedSrcWild": hwAclAdvancedSrcWild,
       "hwAclAdvancedSrcOp": hwAclAdvancedSrcOp,
       "hwAclAdvancedSrcPort1": hwAclAdvancedSrcPort1,
       "hwAclAdvancedSrcPort2": hwAclAdvancedSrcPort2,
       "hwAclAdvancedDestIp": hwAclAdvancedDestIp,
       "hwAclAdvancedDestWild": hwAclAdvancedDestWild,
       "hwAclAdvancedDestOp": hwAclAdvancedDestOp,
       "hwAclAdvancedDestPort1": hwAclAdvancedDestPort1,
       "hwAclAdvancedDestPort2": hwAclAdvancedDestPort2,
       "hwAclAdvancedPrecedence": hwAclAdvancedPrecedence,
       "hwAclAdvancedTos": hwAclAdvancedTos,
       "hwAclAdvancedDscp": hwAclAdvancedDscp,
       "hwAclAdvancedEstablish": hwAclAdvancedEstablish,
       "hwAclAdvancedTimeRangeIndex": hwAclAdvancedTimeRangeIndex,
       "hwAclAdvancedIcmpType": hwAclAdvancedIcmpType,
       "hwAclAdvancedIcmpCode": hwAclAdvancedIcmpCode,
       "hwAclAdvancedFragments": hwAclAdvancedFragments,
       "hwAclAdvancedLog": hwAclAdvancedLog,
       "hwAclAdvancedEnable": hwAclAdvancedEnable,
       "hwAclAdvancedCount": hwAclAdvancedCount,
       "hwAclAdvancedVrfName": hwAclAdvancedVrfName,
       "hwAclAdvancedRowStatus": hwAclAdvancedRowStatus,
       "hwAclAdvancedTcpSyncFlag": hwAclAdvancedTcpSyncFlag,
       "hwAclAdvancedDescription": hwAclAdvancedDescription,
       "hwAclAdvancedSrcPoolName": hwAclAdvancedSrcPoolName,
       "hwAclAdvancedDestPoolName": hwAclAdvancedDestPoolName,
       "hwAclAdvancedProtocolNew": hwAclAdvancedProtocolNew,
       "hwAclAdvancedVni": hwAclAdvancedVni,
       "hwAclAdvancedIgmpType": hwAclAdvancedIgmpType,
       "hwAclAdvancedTtlOp": hwAclAdvancedTtlOp,
       "hwAclAdvancedTtlExpire": hwAclAdvancedTtlExpire,
       "hwAclAdvancedTtlExpireEnd": hwAclAdvancedTtlExpireEnd,
       "hwAclAdvancedPktLenOp": hwAclAdvancedPktLenOp,
       "hwAclAdvancedPktLenBegin": hwAclAdvancedPktLenBegin,
       "hwAclAdvancedPktLenEnd": hwAclAdvancedPktLenEnd,
       "hwAclAdvancedTcpFlagMask": hwAclAdvancedTcpFlagMask,
       "hwAclIfRuleTable": hwAclIfRuleTable,
       "hwAclIfRuleEntry": hwAclIfRuleEntry,
       "hwAclIfAclNum": hwAclIfAclNum,
       "hwAclIfSubitem": hwAclIfSubitem,
       "hwAclIfAct": hwAclIfAct,
       "hwAclIfIndex": hwAclIfIndex,
       "hwAclIfAny": hwAclIfAny,
       "hwAclIfTimeRangeIndex": hwAclIfTimeRangeIndex,
       "hwAclIfLog": hwAclIfLog,
       "hwAclIfEnable": hwAclIfEnable,
       "hwAclIfCount": hwAclIfCount,
       "hwAclIfRowStatus": hwAclIfRowStatus,
       "hwAclUserRuleTable": hwAclUserRuleTable,
       "hwAclUserRuleEntry": hwAclUserRuleEntry,
       "hwAclUserAclNum": hwAclUserAclNum,
       "hwAclUserSubitem": hwAclUserSubitem,
       "hwAclUserAct": hwAclUserAct,
       "hwAclUserProtocol": hwAclUserProtocol,
       "hwAclUserSrcIp": hwAclUserSrcIp,
       "hwAclUserSrcWild": hwAclUserSrcWild,
       "hwAclUserSrcOp": hwAclUserSrcOp,
       "hwAclUserSrcPort1": hwAclUserSrcPort1,
       "hwAclUserSrcPort2": hwAclUserSrcPort2,
       "hwAclUserDestIp": hwAclUserDestIp,
       "hwAclUserDestWild": hwAclUserDestWild,
       "hwAclUserDestOp": hwAclUserDestOp,
       "hwAclUserDestPort1": hwAclUserDestPort1,
       "hwAclUserDestPort2": hwAclUserDestPort2,
       "hwAclUserPrecedence": hwAclUserPrecedence,
       "hwAclUserTos": hwAclUserTos,
       "hwAclUserDscp": hwAclUserDscp,
       "hwAclUserEstablish": hwAclUserEstablish,
       "hwAclUserTimeRangeIndex": hwAclUserTimeRangeIndex,
       "hwAclUserIcmpType": hwAclUserIcmpType,
       "hwAclUserIcmpCode": hwAclUserIcmpCode,
       "hwAclUserFragments": hwAclUserFragments,
       "hwAclUserLog": hwAclUserLog,
       "hwAclUserEnable": hwAclUserEnable,
       "hwAclUserCount": hwAclUserCount,
       "hwAclUserVrfName": hwAclUserVrfName,
       "hwAclUserSrcUserGroupName": hwAclUserSrcUserGroupName,
       "hwAclUserDestUserGroupName": hwAclUserDestUserGroupName,
       "hwAclUserSrcModeType": hwAclUserSrcModeType,
       "hwAclUserDestModeType": hwAclUserDestModeType,
       "hwAclUserRowStatus": hwAclUserRowStatus,
       "hwAclUserTcpSyncFlag": hwAclUserTcpSyncFlag,
       "hwAclUserSrcUserGroupNum": hwAclUserSrcUserGroupNum,
       "hwAclUserDestUserGroupNum": hwAclUserDestUserGroupNum,
       "hwAclUserDestDomainName": hwAclUserDestDomainName,
       "hwAclCompileEnableFlag": hwAclCompileEnableFlag,
       "hwAclCompileNumGroupTable": hwAclCompileNumGroupTable,
       "hwAclCompileNumGroupEntry": hwAclCompileNumGroupEntry,
       "hwAclCompileNumGroupStatus": hwAclCompileNumGroupStatus,
       "hwAclIpv6BasicRuleTable": hwAclIpv6BasicRuleTable,
       "hwAclIpv6BasicRuleEntry": hwAclIpv6BasicRuleEntry,
       "hwAclIpv6BasicAclNum": hwAclIpv6BasicAclNum,
       "hwAclIpv6BasicSubitem": hwAclIpv6BasicSubitem,
       "hwAclIpv6BasicAct": hwAclIpv6BasicAct,
       "hwAclIpv6BasicSrcIp": hwAclIpv6BasicSrcIp,
       "hwAclIpv6BasicSrcPrefix": hwAclIpv6BasicSrcPrefix,
       "hwAclIpv6BasicTimeRangeIndex": hwAclIpv6BasicTimeRangeIndex,
       "hwAclIpv6BasicFragment": hwAclIpv6BasicFragment,
       "hwAclIpv6BasicLog": hwAclIpv6BasicLog,
       "hwAclIpv6BasicEnable": hwAclIpv6BasicEnable,
       "hwAclIpv6BasicCount": hwAclIpv6BasicCount,
       "hwAclIpv6BasicVrfName": hwAclIpv6BasicVrfName,
       "hwAclIpv6BasicRowStatus": hwAclIpv6BasicRowStatus,
       "hwAclIpv6BasicDescription": hwAclIpv6BasicDescription,
       "hwAclIpv6BasicSrcMask": hwAclIpv6BasicSrcMask,
       "hwAclIpv6AdvancedRuleTable": hwAclIpv6AdvancedRuleTable,
       "hwAclIpv6AdvancedRuleEntry": hwAclIpv6AdvancedRuleEntry,
       "hwAclIpv6AdvancedAclNum": hwAclIpv6AdvancedAclNum,
       "hwAclIpv6AdvancedSubitem": hwAclIpv6AdvancedSubitem,
       "hwAclIpv6AdvancedAct": hwAclIpv6AdvancedAct,
       "hwAclIpv6AdvancedProtocol": hwAclIpv6AdvancedProtocol,
       "hwAclIpv6AdvancedSrcIp": hwAclIpv6AdvancedSrcIp,
       "hwAclIpv6AdvancedSrcPrefix": hwAclIpv6AdvancedSrcPrefix,
       "hwAclIpv6AdvancedSrcOp": hwAclIpv6AdvancedSrcOp,
       "hwAclIpv6AdvancedSrcPort1": hwAclIpv6AdvancedSrcPort1,
       "hwAclIpv6AdvancedSrcPort2": hwAclIpv6AdvancedSrcPort2,
       "hwAclIpv6AdvancedDestIp": hwAclIpv6AdvancedDestIp,
       "hwAclIpv6AdvancedDestPrefix": hwAclIpv6AdvancedDestPrefix,
       "hwAclIpv6AdvancedDestOp": hwAclIpv6AdvancedDestOp,
       "hwAclIpv6AdvancedDestPort1": hwAclIpv6AdvancedDestPort1,
       "hwAclIpv6AdvancedDestPort2": hwAclIpv6AdvancedDestPort2,
       "hwAclIpv6AdvancedPrecedence": hwAclIpv6AdvancedPrecedence,
       "hwAclIpv6AdvancedTos": hwAclIpv6AdvancedTos,
       "hwAclIpv6AdvancedDscp": hwAclIpv6AdvancedDscp,
       "hwAclIpv6AdvancedEstablish": hwAclIpv6AdvancedEstablish,
       "hwAclIpv6AdvancedTimeRangeIndex": hwAclIpv6AdvancedTimeRangeIndex,
       "hwAclIpv6AdvancedIcmpType": hwAclIpv6AdvancedIcmpType,
       "hwAclIpv6AdvancedIcmpCode": hwAclIpv6AdvancedIcmpCode,
       "hwAclIpv6AdvancedFragment": hwAclIpv6AdvancedFragment,
       "hwAclIpv6AdvancedLog": hwAclIpv6AdvancedLog,
       "hwAclIpv6AdvancedEnable": hwAclIpv6AdvancedEnable,
       "hwAclIpv6AdvancedCount": hwAclIpv6AdvancedCount,
       "hwAclIpv6AdvancedVrfName": hwAclIpv6AdvancedVrfName,
       "hwAclIpv6AdvancedRowStatus": hwAclIpv6AdvancedRowStatus,
       "hwAclIpv6AdvancedDescription": hwAclIpv6AdvancedDescription,
       "hwAclIpv6AdvancedSrcMask": hwAclIpv6AdvancedSrcMask,
       "hwAclIpv6AdvancedDestMask": hwAclIpv6AdvancedDestMask,
       "hwAclIpv6AdvancedProtocolNew": hwAclIpv6AdvancedProtocolNew,
       "hwAclEthernetFrameRuleTable": hwAclEthernetFrameRuleTable,
       "hwAclEthernetFrameRuleEntry": hwAclEthernetFrameRuleEntry,
       "hwAclEthernetFrameAclNum": hwAclEthernetFrameAclNum,
       "hwAclEthernetFrameSubitem": hwAclEthernetFrameSubitem,
       "hwAclEthernetFrameAct": hwAclEthernetFrameAct,
       "hwAclEthernetFrameType": hwAclEthernetFrameType,
       "hwAclEthernetFrameTypeMask": hwAclEthernetFrameTypeMask,
       "hwAclEthernetFrameSrcMac": hwAclEthernetFrameSrcMac,
       "hwAclEthernetFrameSrcMacMask": hwAclEthernetFrameSrcMacMask,
       "hwAclEthernetFrameDstMac": hwAclEthernetFrameDstMac,
       "hwAclEthernetFrameDstMacMask": hwAclEthernetFrameDstMacMask,
       "hwAclEthernetFrameTimeRangeIndex": hwAclEthernetFrameTimeRangeIndex,
       "hwAclEthernetFrameLog": hwAclEthernetFrameLog,
       "hwAclEthernetFrameEnable": hwAclEthernetFrameEnable,
       "hwAclEthernetFrameCount": hwAclEthernetFrameCount,
       "hwAclEthernetFrameRowStatus": hwAclEthernetFrameRowStatus,
       "hwAclEthernetFrameEncapType": hwAclEthernetFrameEncapType,
       "hwAclEthernetFrameDoubleTag": hwAclEthernetFrameDoubleTag,
       "hwAclEthernetFrameVlanId": hwAclEthernetFrameVlanId,
       "hwAclEthernetFrameVlanIdMask": hwAclEthernetFrameVlanIdMask,
       "hwAclEthernetFrameCVlanId": hwAclEthernetFrameCVlanId,
       "hwAclEthernetFrameCVlanIdMask": hwAclEthernetFrameCVlanIdMask,
       "hwAclEthernetFrameRule8021p": hwAclEthernetFrameRule8021p,
       "hwAclEthernetFrameRuleCVlan8021p": hwAclEthernetFrameRuleCVlan8021p,
       "hwAclEthernetFrameDescription": hwAclEthernetFrameDescription,
       "hwAclAppliedTable": hwAclAppliedTable,
       "hwAclAppliedEntry": hwAclAppliedEntry,
       "hwAclAppliedOperation": hwAclAppliedOperation,
       "hwAclAppliedScopeType": hwAclAppliedScopeType,
       "hwAclAppliedScopeIndex": hwAclAppliedScopeIndex,
       "hwAclAppliedDirection": hwAclAppliedDirection,
       "hwAclAppliedAclNum": hwAclAppliedAclNum,
       "hwAclAppliedSubitem": hwAclAppliedSubitem,
       "hwAclAppliedAclNum2": hwAclAppliedAclNum2,
       "hwAclAppliedSubitem2": hwAclAppliedSubitem2,
       "hwAclAppliedStatMode": hwAclAppliedStatMode,
       "hwAclAppliedStatCount": hwAclAppliedStatCount,
       "hwAclAppliedLimitCir": hwAclAppliedLimitCir,
       "hwAclAppliedLimitPir": hwAclAppliedLimitPir,
       "hwAclAppliedLimitCbs": hwAclAppliedLimitCbs,
       "hwAclAppliedLimitPbs": hwAclAppliedLimitPbs,
       "hwAclAppliedLimitGreenAction": hwAclAppliedLimitGreenAction,
       "hwAclAppliedLimitGreenValue": hwAclAppliedLimitGreenValue,
       "hwAclAppliedLimitYellowAction": hwAclAppliedLimitYellowAction,
       "hwAclAppliedLimitYellowValue": hwAclAppliedLimitYellowValue,
       "hwAclAppliedLimitRedAction": hwAclAppliedLimitRedAction,
       "hwAclAppliedLimitRedValue": hwAclAppliedLimitRedValue,
       "hwAclAppliedMirrObservedPort": hwAclAppliedMirrObservedPort,
       "hwAclAppliedMirrRspanVlan": hwAclAppliedMirrRspanVlan,
       "hwAclAppliedRedirectIfIndex": hwAclAppliedRedirectIfIndex,
       "hwAclAppliedRedirectIpAddr": hwAclAppliedRedirectIpAddr,
       "hwAclAppliedRedirectIpv6Addr": hwAclAppliedRedirectIpv6Addr,
       "hwAclAppliedRemarkVlan": hwAclAppliedRemarkVlan,
       "hwAclAppliedRemarkCVlan": hwAclAppliedRemarkCVlan,
       "hwAclAppliedRemark8021p": hwAclAppliedRemark8021p,
       "hwAclAppliedRemarkDscp": hwAclAppliedRemarkDscp,
       "hwAclAppliedRemarkIpPre": hwAclAppliedRemarkIpPre,
       "hwAclAppliedRemarkLocalPre": hwAclAppliedRemarkLocalPre,
       "hwAclAppliedRemarkMacAddr": hwAclAppliedRemarkMacAddr,
       "hwAclAppliedIsIPv6Acl": hwAclAppliedIsIPv6Acl,
       "hwAclAppliedRowStatus": hwAclAppliedRowStatus,
       "hwAclIpv6NumGroupTable": hwAclIpv6NumGroupTable,
       "hwAclIpv6NumGroupEntry": hwAclIpv6NumGroupEntry,
       "hwAclIpv6NumGroupAclNum": hwAclIpv6NumGroupAclNum,
       "hwAclIpv6NumGroupMatchOrder": hwAclIpv6NumGroupMatchOrder,
       "hwAclIpv6NumGroupSubitemNum": hwAclIpv6NumGroupSubitemNum,
       "hwAclIpv6NumGroupCountClear": hwAclIpv6NumGroupCountClear,
       "hwAclIpv6NumGroupAclName": hwAclIpv6NumGroupAclName,
       "hwAclIpv6NumGroupDescription": hwAclIpv6NumGroupDescription,
       "hwAclIpv6NumGroupAclType": hwAclIpv6NumGroupAclType,
       "hwAclIpv6NumGroupRowStatus": hwAclIpv6NumGroupRowStatus,
       "hwAclIpv6NumGroupStep": hwAclIpv6NumGroupStep,
       "hwAclIpv6IfRuleTable": hwAclIpv6IfRuleTable,
       "hwAclIpv6IfRuleEntry": hwAclIpv6IfRuleEntry,
       "hwAclIpv6IfAclNum": hwAclIpv6IfAclNum,
       "hwAclIpv6IfSubitem": hwAclIpv6IfSubitem,
       "hwAclIpv6IfAct": hwAclIpv6IfAct,
       "hwAclIpv6IfIndex": hwAclIpv6IfIndex,
       "hwAclIpv6IfAny": hwAclIpv6IfAny,
       "hwAclIpv6IfTimeRangeIndex": hwAclIpv6IfTimeRangeIndex,
       "hwAclIpv6IfLog": hwAclIpv6IfLog,
       "hwAclIpv6IfEnable": hwAclIpv6IfEnable,
       "hwAclIpv6IfCount": hwAclIpv6IfCount,
       "hwAclIpv6IfRowStatus": hwAclIpv6IfRowStatus,
       "hwAclMplsRuleTable": hwAclMplsRuleTable,
       "hwAclMplsRuleEntry": hwAclMplsRuleEntry,
       "hwAclMplsAclNum": hwAclMplsAclNum,
       "hwAclMplsSubitem": hwAclMplsSubitem,
       "hwAclMplsAct": hwAclMplsAct,
       "hwAclMplsExp1": hwAclMplsExp1,
       "hwAclMplsExp2": hwAclMplsExp2,
       "hwAclMplsExp3": hwAclMplsExp3,
       "hwAclMplsExp4": hwAclMplsExp4,
       "hwAclMplsLabel1": hwAclMplsLabel1,
       "hwAclMplsLabel2": hwAclMplsLabel2,
       "hwAclMplsLabel3": hwAclMplsLabel3,
       "hwAclMplsLabel4": hwAclMplsLabel4,
       "hwAclMplsTTLOP1": hwAclMplsTTLOP1,
       "hwAclMplsTTL1Begin": hwAclMplsTTL1Begin,
       "hwAclMplsTTL1End": hwAclMplsTTL1End,
       "hwAclMplsTTLOP2": hwAclMplsTTLOP2,
       "hwAclMplsTTL2Begin": hwAclMplsTTL2Begin,
       "hwAclMplsTTL2End": hwAclMplsTTL2End,
       "hwAclMplsTTLOP3": hwAclMplsTTLOP3,
       "hwAclMplsTTL3Begin": hwAclMplsTTL3Begin,
       "hwAclMplsTTL3End": hwAclMplsTTL3End,
       "hwAclMplsRowStatus": hwAclMplsRowStatus,
       "hwAclMplsCount": hwAclMplsCount,
       "hwAclDomainNameConfigTable": hwAclDomainNameConfigTable,
       "hwAclDomainNameConfigEntry": hwAclDomainNameConfigEntry,
       "hwAclDomainID": hwAclDomainID,
       "hwAclDomainName": hwAclDomainName,
       "hwAclDomainNameConfigRowStatus": hwAclDomainNameConfigRowStatus,
       "hwAclMibTrap": hwAclMibTrap,
       "hwAclTrapOid": hwAclTrapOid,
       "hwAclTrapsDefine": hwAclTrapsDefine,
       "hwAclTraps": hwAclTraps,
       "hwAclResourceTrapsTable": hwAclResourceTrapsTable,
       "hwAclResSlotStr": hwAclResSlotStr,
       "hwAclResStage": hwAclResStage,
       "hwAclResLimit": hwAclResLimit,
       "hwAclResourceTrapsEntry": hwAclResourceTrapsEntry,
       "hwAclResThresholdExceedClearTrap": hwAclResThresholdExceedClearTrap,
       "hwAclResThresholdExceedTrap": hwAclResThresholdExceedTrap,
       "hwAclResTotalCountExceedClearTrap": hwAclResTotalCountExceedClearTrap,
       "hwAclResTotalCountExceedTrap": hwAclResTotalCountExceedTrap,
       "hwAclResourceTrapsGroups": hwAclResourceTrapsGroups,
       "hwAclResourceTrapsGroup": hwAclResourceTrapsGroup,
       "hwAclMibConformance": hwAclMibConformance,
       "hwAclMibCompliances": hwAclMibCompliances,
       "hwAclMibCompliance": hwAclMibCompliance,
       "hwAclMibGroups": hwAclMibGroups,
       "hwAclGroup": hwAclGroup}
)
