# SNMP MIB module (HUAWEI-PFLT-EUDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-PFLT-EUDM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:29 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(mplsVpnVrfName,) = mibBuilder.importSymbols(
    "MPLS-VPN-MIB",
    "mplsVpnVrfName")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwPFLTEudm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 12, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AclAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aclDeny", 2),
          ("aclPermit", 1))
    )



class AclType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aclTypeName", 2),
          ("aclTypeNum", 1))
    )



# MIB Managed Objects in the order of their OIDs

_HwPFLT_ObjectIdentity = ObjectIdentity
hwPFLT = _HwPFLT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 12)
)
_HwPFltEudmCfgMibObjects_ObjectIdentity = ObjectIdentity
hwPFltEudmCfgMibObjects = _HwPFltEudmCfgMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 12, 2, 1)
)
_HwPFltEudmDefaultActionTable_Object = MibTable
hwPFltEudmDefaultActionTable = _HwPFltEudmDefaultActionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 12, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwPFltEudmDefaultActionTable.setStatus("current")
_HwPFltEudmDefaultActionEntry_Object = MibTableRow
hwPFltEudmDefaultActionEntry = _HwPFltEudmDefaultActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 12, 2, 1, 1, 1)
)
hwPFltEudmDefaultActionEntry.setIndexNames(
    (0, "HUAWEI-PFLT-EUDM-MIB", "hwPFltEudmDefaultActZoneID1"),
    (0, "HUAWEI-PFLT-EUDM-MIB", "hwPFltEudmDefaultActZoneID2"),
)
if mibBuilder.loadTexts:
    hwPFltEudmDefaultActionEntry.setStatus("current")


class _HwPFltEudmDefaultActZoneID1_Type(Integer32):
    """Custom type hwPFltEudmDefaultActZoneID1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwPFltEudmDefaultActZoneID1_Type.__name__ = "Integer32"
_HwPFltEudmDefaultActZoneID1_Object = MibTableColumn
hwPFltEudmDefaultActZoneID1 = _HwPFltEudmDefaultActZoneID1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 12, 2, 1, 1, 1, 1),
    _HwPFltEudmDefaultActZoneID1_Type()
)
hwPFltEudmDefaultActZoneID1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPFltEudmDefaultActZoneID1.setStatus("current")


class _HwPFltEudmDefaultActZoneID2_Type(Integer32):
    """Custom type hwPFltEudmDefaultActZoneID2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwPFltEudmDefaultActZoneID2_Type.__name__ = "Integer32"
_HwPFltEudmDefaultActZoneID2_Object = MibTableColumn
hwPFltEudmDefaultActZoneID2 = _HwPFltEudmDefaultActZoneID2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 12, 2, 1, 1, 1, 2),
    _HwPFltEudmDefaultActZoneID2_Type()
)
hwPFltEudmDefaultActZoneID2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPFltEudmDefaultActZoneID2.setStatus("current")


class _HwPFltEudmDeaultActInbound_Type(AclAction):
    """Custom type hwPFltEudmDeaultActInbound based on AclAction"""


_HwPFltEudmDeaultActInbound_Object = MibTableColumn
hwPFltEudmDeaultActInbound = _HwPFltEudmDeaultActInbound_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 12, 2, 1, 1, 1, 3),
    _HwPFltEudmDeaultActInbound_Type()
)
hwPFltEudmDeaultActInbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPFltEudmDeaultActInbound.setStatus("current")


class _HwPFltEudmDeaultActOutbound_Type(AclAction):
    """Custom type hwPFltEudmDeaultActOutbound based on AclAction"""


_HwPFltEudmDeaultActOutbound_Object = MibTableColumn
hwPFltEudmDeaultActOutbound = _HwPFltEudmDeaultActOutbound_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 12, 2, 1, 1, 1, 4),
    _HwPFltEudmDeaultActOutbound_Type()
)
hwPFltEudmDeaultActOutbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPFltEudmDeaultActOutbound.setStatus("current")
_HwPFltEudmPolicyApplyTable_Object = MibTable
hwPFltEudmPolicyApplyTable = _HwPFltEudmPolicyApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 12, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hwPFltEudmPolicyApplyTable.setStatus("current")
_HwPFltEudmPolicyApplyEntry_Object = MibTableRow
hwPFltEudmPolicyApplyEntry = _HwPFltEudmPolicyApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 12, 2, 1, 2, 1)
)
hwPFltEudmPolicyApplyEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "HUAWEI-PFLT-EUDM-MIB", "hwPFltEudmPolicyZoneID1"),
    (0, "HUAWEI-PFLT-EUDM-MIB", "hwPFltEudmPolicyZoneID2"),
)
if mibBuilder.loadTexts:
    hwPFltEudmPolicyApplyEntry.setStatus("current")


class _HwPFltEudmPolicyZoneID1_Type(Integer32):
    """Custom type hwPFltEudmPolicyZoneID1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwPFltEudmPolicyZoneID1_Type.__name__ = "Integer32"
_HwPFltEudmPolicyZoneID1_Object = MibTableColumn
hwPFltEudmPolicyZoneID1 = _HwPFltEudmPolicyZoneID1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 12, 2, 1, 2, 1, 1),
    _HwPFltEudmPolicyZoneID1_Type()
)
hwPFltEudmPolicyZoneID1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPFltEudmPolicyZoneID1.setStatus("current")


class _HwPFltEudmPolicyZoneID2_Type(Integer32):
    """Custom type hwPFltEudmPolicyZoneID2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwPFltEudmPolicyZoneID2_Type.__name__ = "Integer32"
_HwPFltEudmPolicyZoneID2_Object = MibTableColumn
hwPFltEudmPolicyZoneID2 = _HwPFltEudmPolicyZoneID2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 12, 2, 1, 2, 1, 2),
    _HwPFltEudmPolicyZoneID2_Type()
)
hwPFltEudmPolicyZoneID2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPFltEudmPolicyZoneID2.setStatus("current")


class _HwPFltEudmPolicyInAclType_Type(AclType):
    """Custom type hwPFltEudmPolicyInAclType based on AclType"""


_HwPFltEudmPolicyInAclType_Object = MibTableColumn
hwPFltEudmPolicyInAclType = _HwPFltEudmPolicyInAclType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 12, 2, 1, 2, 1, 3),
    _HwPFltEudmPolicyInAclType_Type()
)
hwPFltEudmPolicyInAclType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPFltEudmPolicyInAclType.setStatus("current")


class _HwPFltEudmPolicyInAclNum_Type(Integer32):
    """Custom type hwPFltEudmPolicyInAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1000, 3999),
    )


_HwPFltEudmPolicyInAclNum_Type.__name__ = "Integer32"
_HwPFltEudmPolicyInAclNum_Object = MibTableColumn
hwPFltEudmPolicyInAclNum = _HwPFltEudmPolicyInAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 12, 2, 1, 2, 1, 4),
    _HwPFltEudmPolicyInAclNum_Type()
)
hwPFltEudmPolicyInAclNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPFltEudmPolicyInAclNum.setStatus("current")


class _HwPFltEudmPolicyInAclName_Type(OctetString):
    """Custom type hwPFltEudmPolicyInAclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwPFltEudmPolicyInAclName_Type.__name__ = "OctetString"
_HwPFltEudmPolicyInAclName_Object = MibTableColumn
hwPFltEudmPolicyInAclName = _HwPFltEudmPolicyInAclName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 12, 2, 1, 2, 1, 5),
    _HwPFltEudmPolicyInAclName_Type()
)
hwPFltEudmPolicyInAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPFltEudmPolicyInAclName.setStatus("current")


class _HwPFltEudmPolicyOutAclType_Type(AclType):
    """Custom type hwPFltEudmPolicyOutAclType based on AclType"""


_HwPFltEudmPolicyOutAclType_Object = MibTableColumn
hwPFltEudmPolicyOutAclType = _HwPFltEudmPolicyOutAclType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 12, 2, 1, 2, 1, 6),
    _HwPFltEudmPolicyOutAclType_Type()
)
hwPFltEudmPolicyOutAclType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPFltEudmPolicyOutAclType.setStatus("current")


class _HwPFltEudmPolicyOutAclNum_Type(Integer32):
    """Custom type hwPFltEudmPolicyOutAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1000, 3999),
    )


_HwPFltEudmPolicyOutAclNum_Type.__name__ = "Integer32"
_HwPFltEudmPolicyOutAclNum_Object = MibTableColumn
hwPFltEudmPolicyOutAclNum = _HwPFltEudmPolicyOutAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 12, 2, 1, 2, 1, 7),
    _HwPFltEudmPolicyOutAclNum_Type()
)
hwPFltEudmPolicyOutAclNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPFltEudmPolicyOutAclNum.setStatus("current")


class _HwPFltEudmPolicyOutAclName_Type(OctetString):
    """Custom type hwPFltEudmPolicyOutAclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwPFltEudmPolicyOutAclName_Type.__name__ = "OctetString"
_HwPFltEudmPolicyOutAclName_Object = MibTableColumn
hwPFltEudmPolicyOutAclName = _HwPFltEudmPolicyOutAclName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 12, 2, 1, 2, 1, 8),
    _HwPFltEudmPolicyOutAclName_Type()
)
hwPFltEudmPolicyOutAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPFltEudmPolicyOutAclName.setStatus("current")
_HwPFltEudmConformance_ObjectIdentity = ObjectIdentity
hwPFltEudmConformance = _HwPFltEudmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 12, 2, 2)
)
_HwPFltEudmCompliance_ObjectIdentity = ObjectIdentity
hwPFltEudmCompliance = _HwPFltEudmCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 12, 2, 2, 1)
)
_HwPFltEudmMibGroups_ObjectIdentity = ObjectIdentity
hwPFltEudmMibGroups = _HwPFltEudmMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 12, 2, 2, 2)
)

# Managed Objects groups

hwPFltEudmDefaultActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 12, 2, 2, 2, 1)
)
hwPFltEudmDefaultActionGroup.setObjects(
      *(("HUAWEI-PFLT-EUDM-MIB", "hwPFltEudmDeaultActInbound"),
        ("HUAWEI-PFLT-EUDM-MIB", "hwPFltEudmDeaultActOutbound"))
)
if mibBuilder.loadTexts:
    hwPFltEudmDefaultActionGroup.setStatus("current")

hwPFltEudmPolicyApplyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 12, 2, 2, 2, 2)
)
hwPFltEudmPolicyApplyGroup.setObjects(
      *(("HUAWEI-PFLT-EUDM-MIB", "hwPFltEudmPolicyInAclType"),
        ("HUAWEI-PFLT-EUDM-MIB", "hwPFltEudmPolicyInAclNum"),
        ("HUAWEI-PFLT-EUDM-MIB", "hwPFltEudmPolicyInAclName"),
        ("HUAWEI-PFLT-EUDM-MIB", "hwPFltEudmPolicyOutAclType"),
        ("HUAWEI-PFLT-EUDM-MIB", "hwPFltEudmPolicyOutAclNum"),
        ("HUAWEI-PFLT-EUDM-MIB", "hwPFltEudmPolicyOutAclName"))
)
if mibBuilder.loadTexts:
    hwPFltEudmPolicyApplyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-PFLT-EUDM-MIB",
    **{"AclAction": AclAction,
       "AclType": AclType,
       "hwPFLT": hwPFLT,
       "hwPFLTEudm": hwPFLTEudm,
       "hwPFltEudmCfgMibObjects": hwPFltEudmCfgMibObjects,
       "hwPFltEudmDefaultActionTable": hwPFltEudmDefaultActionTable,
       "hwPFltEudmDefaultActionEntry": hwPFltEudmDefaultActionEntry,
       "hwPFltEudmDefaultActZoneID1": hwPFltEudmDefaultActZoneID1,
       "hwPFltEudmDefaultActZoneID2": hwPFltEudmDefaultActZoneID2,
       "hwPFltEudmDeaultActInbound": hwPFltEudmDeaultActInbound,
       "hwPFltEudmDeaultActOutbound": hwPFltEudmDeaultActOutbound,
       "hwPFltEudmPolicyApplyTable": hwPFltEudmPolicyApplyTable,
       "hwPFltEudmPolicyApplyEntry": hwPFltEudmPolicyApplyEntry,
       "hwPFltEudmPolicyZoneID1": hwPFltEudmPolicyZoneID1,
       "hwPFltEudmPolicyZoneID2": hwPFltEudmPolicyZoneID2,
       "hwPFltEudmPolicyInAclType": hwPFltEudmPolicyInAclType,
       "hwPFltEudmPolicyInAclNum": hwPFltEudmPolicyInAclNum,
       "hwPFltEudmPolicyInAclName": hwPFltEudmPolicyInAclName,
       "hwPFltEudmPolicyOutAclType": hwPFltEudmPolicyOutAclType,
       "hwPFltEudmPolicyOutAclNum": hwPFltEudmPolicyOutAclNum,
       "hwPFltEudmPolicyOutAclName": hwPFltEudmPolicyOutAclName,
       "hwPFltEudmConformance": hwPFltEudmConformance,
       "hwPFltEudmCompliance": hwPFltEudmCompliance,
       "hwPFltEudmMibGroups": hwPFltEudmMibGroups,
       "hwPFltEudmDefaultActionGroup": hwPFltEudmDefaultActionGroup,
       "hwPFltEudmPolicyApplyGroup": hwPFltEudmPolicyApplyGroup}
)
