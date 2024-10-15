# SNMP MIB module (HUAWEI-BLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-BLS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:57 2024
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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwBLS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BlsAddReason(Integer32, TextualConvention):
    status = "current"
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
        *(("reasonIPSweep", 3),
          ("reasonManual", 2),
          ("reasonPortScan", 4),
          ("reasonUnknow", 1))
    )



# MIB Managed Objects in the order of their OIDs

_HwBlsMibObjects_ObjectIdentity = ObjectIdentity
hwBlsMibObjects = _HwBlsMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 1)
)


class _HwBlsEnableFlag_Type(TruthValue):
    """Custom type hwBlsEnableFlag based on TruthValue"""


_HwBlsEnableFlag_Object = MibScalar
hwBlsEnableFlag = _HwBlsEnableFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 1, 1),
    _HwBlsEnableFlag_Type()
)
hwBlsEnableFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBlsEnableFlag.setStatus("current")
_HwBlsBlackListTable_Object = MibTable
hwBlsBlackListTable = _HwBlsBlackListTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 1, 2)
)
if mibBuilder.loadTexts:
    hwBlsBlackListTable.setStatus("current")
_HwBlsBlackListEntry_Object = MibTableRow
hwBlsBlackListEntry = _HwBlsBlackListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 1, 2, 1)
)
hwBlsBlackListEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "HUAWEI-BLS-MIB", "hwBlsItemIPAddress"),
)
if mibBuilder.loadTexts:
    hwBlsBlackListEntry.setStatus("current")
_HwBlsItemIPAddress_Type = IpAddress
_HwBlsItemIPAddress_Object = MibTableColumn
hwBlsItemIPAddress = _HwBlsItemIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 1, 2, 1, 1),
    _HwBlsItemIPAddress_Type()
)
hwBlsItemIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBlsItemIPAddress.setStatus("current")


class _HwBlsItemAge_Type(Integer32):
    """Custom type hwBlsItemAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HwBlsItemAge_Type.__name__ = "Integer32"
_HwBlsItemAge_Object = MibTableColumn
hwBlsItemAge = _HwBlsItemAge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 1, 2, 1, 2),
    _HwBlsItemAge_Type()
)
hwBlsItemAge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBlsItemAge.setStatus("current")
_HwBlsItemAddReason_Type = BlsAddReason
_HwBlsItemAddReason_Object = MibTableColumn
hwBlsItemAddReason = _HwBlsItemAddReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 1, 2, 1, 3),
    _HwBlsItemAddReason_Type()
)
hwBlsItemAddReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBlsItemAddReason.setStatus("current")
_HwBlsItemAddTime_Type = DateAndTime
_HwBlsItemAddTime_Object = MibTableColumn
hwBlsItemAddTime = _HwBlsItemAddTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 1, 2, 1, 4),
    _HwBlsItemAddTime_Type()
)
hwBlsItemAddTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBlsItemAddTime.setStatus("current")
_HwBlsRowStatus_Type = RowStatus
_HwBlsRowStatus_Object = MibTableColumn
hwBlsRowStatus = _HwBlsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 1, 2, 1, 5),
    _HwBlsRowStatus_Type()
)
hwBlsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBlsRowStatus.setStatus("current")
_HwBlsFilterTypeSet_ObjectIdentity = ObjectIdentity
hwBlsFilterTypeSet = _HwBlsFilterTypeSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 1, 3)
)


class _HwBlsFilterType_Type(Integer32):
    """Custom type hwBlsFilterType based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwBlsFilterType_Type.__name__ = "Integer32"
_HwBlsFilterType_Object = MibScalar
hwBlsFilterType = _HwBlsFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 1, 3, 1),
    _HwBlsFilterType_Type()
)
hwBlsFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBlsFilterType.setStatus("current")
_HwBlsMibConformance_ObjectIdentity = ObjectIdentity
hwBlsMibConformance = _HwBlsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 2)
)
_HwBlsMibGroup_ObjectIdentity = ObjectIdentity
hwBlsMibGroup = _HwBlsMibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 2, 1)
)

# Managed Objects groups

hwBlsEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 2, 1, 1)
)
hwBlsEnableGroup.setObjects(
    ("HUAWEI-BLS-MIB", "hwBlsEnableFlag")
)
if mibBuilder.loadTexts:
    hwBlsEnableGroup.setStatus("current")

hwBlsBlackListTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 2, 1, 2)
)
hwBlsBlackListTableGroup.setObjects(
      *(("HUAWEI-BLS-MIB", "hwBlsItemIPAddress"),
        ("HUAWEI-BLS-MIB", "hwBlsItemAge"),
        ("HUAWEI-BLS-MIB", "hwBlsItemAddReason"),
        ("HUAWEI-BLS-MIB", "hwBlsItemAddTime"),
        ("HUAWEI-BLS-MIB", "hwBlsRowStatus"))
)
if mibBuilder.loadTexts:
    hwBlsBlackListTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-BLS-MIB",
    **{"BlsAddReason": BlsAddReason,
       "hwBLS": hwBLS,
       "hwBlsMibObjects": hwBlsMibObjects,
       "hwBlsEnableFlag": hwBlsEnableFlag,
       "hwBlsBlackListTable": hwBlsBlackListTable,
       "hwBlsBlackListEntry": hwBlsBlackListEntry,
       "hwBlsItemIPAddress": hwBlsItemIPAddress,
       "hwBlsItemAge": hwBlsItemAge,
       "hwBlsItemAddReason": hwBlsItemAddReason,
       "hwBlsItemAddTime": hwBlsItemAddTime,
       "hwBlsRowStatus": hwBlsRowStatus,
       "hwBlsFilterTypeSet": hwBlsFilterTypeSet,
       "hwBlsFilterType": hwBlsFilterType,
       "hwBlsMibConformance": hwBlsMibConformance,
       "hwBlsMibGroup": hwBlsMibGroup,
       "hwBlsEnableGroup": hwBlsEnableGroup,
       "hwBlsBlackListTableGroup": hwBlsBlackListTableGroup}
)
