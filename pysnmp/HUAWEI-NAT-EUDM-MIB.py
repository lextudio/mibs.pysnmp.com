# SNMP MIB module (HUAWEI-NAT-EUDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-NAT-EUDM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:20 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwNATEudm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NatType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("easyIP", 3),
          ("nat", 2),
          ("pat", 1))
    )



# MIB Managed Objects in the order of their OIDs

_HwNAT_ObjectIdentity = ObjectIdentity
hwNAT = _HwNAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7)
)
_HwNatEudmMibObjects_ObjectIdentity = ObjectIdentity
hwNatEudmMibObjects = _HwNatEudmMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 2, 1)
)
_HwNatEudmOutboundTable_Object = MibTable
hwNatEudmOutboundTable = _HwNatEudmOutboundTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwNatEudmOutboundTable.setStatus("current")
_HwNatEudmOutboundEntry_Object = MibTableRow
hwNatEudmOutboundEntry = _HwNatEudmOutboundEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 2, 1, 1, 1)
)
hwNatEudmOutboundEntry.setIndexNames(
    (0, "HUAWEI-NAT-EUDM-MIB", "hwNatEudmOutboundNatID"),
)
if mibBuilder.loadTexts:
    hwNatEudmOutboundEntry.setStatus("current")


class _HwNatEudmOutboundNatID_Type(Integer32):
    """Custom type hwNatEudmOutboundNatID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwNatEudmOutboundNatID_Type.__name__ = "Integer32"
_HwNatEudmOutboundNatID_Object = MibTableColumn
hwNatEudmOutboundNatID = _HwNatEudmOutboundNatID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 2, 1, 1, 1, 1),
    _HwNatEudmOutboundNatID_Type()
)
hwNatEudmOutboundNatID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNatEudmOutboundNatID.setStatus("current")
_HwNatEudmOutboundType_Type = NatType
_HwNatEudmOutboundType_Object = MibTableColumn
hwNatEudmOutboundType = _HwNatEudmOutboundType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 2, 1, 1, 1, 2),
    _HwNatEudmOutboundType_Type()
)
hwNatEudmOutboundType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNatEudmOutboundType.setStatus("current")


class _HwNatEudmOutboundAclNumber_Type(Integer32):
    """Custom type hwNatEudmOutboundAclNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_HwNatEudmOutboundAclNumber_Type.__name__ = "Integer32"
_HwNatEudmOutboundAclNumber_Object = MibTableColumn
hwNatEudmOutboundAclNumber = _HwNatEudmOutboundAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 2, 1, 1, 1, 3),
    _HwNatEudmOutboundAclNumber_Type()
)
hwNatEudmOutboundAclNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNatEudmOutboundAclNumber.setStatus("current")


class _HwNatEudmOutboundPoolIndex_Type(Integer32):
    """Custom type hwNatEudmOutboundPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwNatEudmOutboundPoolIndex_Type.__name__ = "Integer32"
_HwNatEudmOutboundPoolIndex_Object = MibTableColumn
hwNatEudmOutboundPoolIndex = _HwNatEudmOutboundPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 2, 1, 1, 1, 4),
    _HwNatEudmOutboundPoolIndex_Type()
)
hwNatEudmOutboundPoolIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNatEudmOutboundPoolIndex.setStatus("current")
_HwNatEudmOutboundEasyIpIfIndex_Type = Gauge32
_HwNatEudmOutboundEasyIpIfIndex_Object = MibTableColumn
hwNatEudmOutboundEasyIpIfIndex = _HwNatEudmOutboundEasyIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 2, 1, 1, 1, 5),
    _HwNatEudmOutboundEasyIpIfIndex_Type()
)
hwNatEudmOutboundEasyIpIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNatEudmOutboundEasyIpIfIndex.setStatus("current")
_HwNatEudmOutboundRefCount_Type = Integer32
_HwNatEudmOutboundRefCount_Object = MibTableColumn
hwNatEudmOutboundRefCount = _HwNatEudmOutboundRefCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 2, 1, 1, 1, 6),
    _HwNatEudmOutboundRefCount_Type()
)
hwNatEudmOutboundRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatEudmOutboundRefCount.setStatus("current")
_HwNatEudmOutboundRowstatus_Type = RowStatus
_HwNatEudmOutboundRowstatus_Object = MibTableColumn
hwNatEudmOutboundRowstatus = _HwNatEudmOutboundRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 2, 1, 1, 1, 7),
    _HwNatEudmOutboundRowstatus_Type()
)
hwNatEudmOutboundRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNatEudmOutboundRowstatus.setStatus("current")
_HwNatEudmZoneApplyTable_Object = MibTable
hwNatEudmZoneApplyTable = _HwNatEudmZoneApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hwNatEudmZoneApplyTable.setStatus("current")
_HwNatEudmZoneApplyEntry_Object = MibTableRow
hwNatEudmZoneApplyEntry = _HwNatEudmZoneApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 2, 1, 2, 1)
)
hwNatEudmZoneApplyEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "HUAWEI-NAT-EUDM-MIB", "hwNatEudmZoneApplyZoneID1"),
    (0, "HUAWEI-NAT-EUDM-MIB", "hwNatEudmZoneApplyZoneID2"),
    (0, "HUAWEI-NAT-EUDM-MIB", "hwNatEudmZoneApplyNatID"),
)
if mibBuilder.loadTexts:
    hwNatEudmZoneApplyEntry.setStatus("current")


class _HwNatEudmZoneApplyZoneID1_Type(Integer32):
    """Custom type hwNatEudmZoneApplyZoneID1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwNatEudmZoneApplyZoneID1_Type.__name__ = "Integer32"
_HwNatEudmZoneApplyZoneID1_Object = MibTableColumn
hwNatEudmZoneApplyZoneID1 = _HwNatEudmZoneApplyZoneID1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 2, 1, 2, 1, 1),
    _HwNatEudmZoneApplyZoneID1_Type()
)
hwNatEudmZoneApplyZoneID1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNatEudmZoneApplyZoneID1.setStatus("current")


class _HwNatEudmZoneApplyZoneID2_Type(Integer32):
    """Custom type hwNatEudmZoneApplyZoneID2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwNatEudmZoneApplyZoneID2_Type.__name__ = "Integer32"
_HwNatEudmZoneApplyZoneID2_Object = MibTableColumn
hwNatEudmZoneApplyZoneID2 = _HwNatEudmZoneApplyZoneID2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 2, 1, 2, 1, 2),
    _HwNatEudmZoneApplyZoneID2_Type()
)
hwNatEudmZoneApplyZoneID2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNatEudmZoneApplyZoneID2.setStatus("current")


class _HwNatEudmZoneApplyNatID_Type(Integer32):
    """Custom type hwNatEudmZoneApplyNatID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwNatEudmZoneApplyNatID_Type.__name__ = "Integer32"
_HwNatEudmZoneApplyNatID_Object = MibTableColumn
hwNatEudmZoneApplyNatID = _HwNatEudmZoneApplyNatID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 2, 1, 2, 1, 3),
    _HwNatEudmZoneApplyNatID_Type()
)
hwNatEudmZoneApplyNatID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNatEudmZoneApplyNatID.setStatus("current")
_HwNatEudmZoneApplyRowstatus_Type = RowStatus
_HwNatEudmZoneApplyRowstatus_Object = MibTableColumn
hwNatEudmZoneApplyRowstatus = _HwNatEudmZoneApplyRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 2, 1, 2, 1, 4),
    _HwNatEudmZoneApplyRowstatus_Type()
)
hwNatEudmZoneApplyRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNatEudmZoneApplyRowstatus.setStatus("current")
_HwNatEudmConformance_ObjectIdentity = ObjectIdentity
hwNatEudmConformance = _HwNatEudmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 2, 2)
)
_HwNatEudmGroups_ObjectIdentity = ObjectIdentity
hwNatEudmGroups = _HwNatEudmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 2, 2, 1)
)

# Managed Objects groups

hwNatEudmCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 7, 2, 2, 1, 1)
)
hwNatEudmCfgGroup.setObjects(
      *(("HUAWEI-NAT-EUDM-MIB", "hwNatEudmOutboundRefCount"),
        ("HUAWEI-NAT-EUDM-MIB", "hwNatEudmZoneApplyRowstatus"),
        ("HUAWEI-NAT-EUDM-MIB", "hwNatEudmOutboundType"),
        ("HUAWEI-NAT-EUDM-MIB", "hwNatEudmOutboundAclNumber"),
        ("HUAWEI-NAT-EUDM-MIB", "hwNatEudmOutboundPoolIndex"),
        ("HUAWEI-NAT-EUDM-MIB", "hwNatEudmOutboundEasyIpIfIndex"),
        ("HUAWEI-NAT-EUDM-MIB", "hwNatEudmOutboundRowstatus"))
)
if mibBuilder.loadTexts:
    hwNatEudmCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-NAT-EUDM-MIB",
    **{"NatType": NatType,
       "hwNAT": hwNAT,
       "hwNATEudm": hwNATEudm,
       "hwNatEudmMibObjects": hwNatEudmMibObjects,
       "hwNatEudmOutboundTable": hwNatEudmOutboundTable,
       "hwNatEudmOutboundEntry": hwNatEudmOutboundEntry,
       "hwNatEudmOutboundNatID": hwNatEudmOutboundNatID,
       "hwNatEudmOutboundType": hwNatEudmOutboundType,
       "hwNatEudmOutboundAclNumber": hwNatEudmOutboundAclNumber,
       "hwNatEudmOutboundPoolIndex": hwNatEudmOutboundPoolIndex,
       "hwNatEudmOutboundEasyIpIfIndex": hwNatEudmOutboundEasyIpIfIndex,
       "hwNatEudmOutboundRefCount": hwNatEudmOutboundRefCount,
       "hwNatEudmOutboundRowstatus": hwNatEudmOutboundRowstatus,
       "hwNatEudmZoneApplyTable": hwNatEudmZoneApplyTable,
       "hwNatEudmZoneApplyEntry": hwNatEudmZoneApplyEntry,
       "hwNatEudmZoneApplyZoneID1": hwNatEudmZoneApplyZoneID1,
       "hwNatEudmZoneApplyZoneID2": hwNatEudmZoneApplyZoneID2,
       "hwNatEudmZoneApplyNatID": hwNatEudmZoneApplyNatID,
       "hwNatEudmZoneApplyRowstatus": hwNatEudmZoneApplyRowstatus,
       "hwNatEudmConformance": hwNatEudmConformance,
       "hwNatEudmGroups": hwNatEudmGroups,
       "hwNatEudmCfgGroup": hwNatEudmCfgGroup}
)
