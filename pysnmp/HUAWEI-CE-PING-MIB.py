# SNMP MIB module (HUAWEI-CE-PING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-CE-PING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:20 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwCePing = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 175)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwCePingTable_Object = MibTable
hwCePingTable = _HwCePingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 1)
)
if mibBuilder.loadTexts:
    hwCePingTable.setStatus("current")
_HwCePingEntry_Object = MibTableRow
hwCePingEntry = _HwCePingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 1, 1)
)
hwCePingEntry.setIndexNames(
    (0, "HUAWEI-CE-PING-MIB", "hwCePingIndex"),
)
if mibBuilder.loadTexts:
    hwCePingEntry.setStatus("current")


class _HwCePingIndex_Type(Integer32):
    """Custom type hwCePingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwCePingIndex_Type.__name__ = "Integer32"
_HwCePingIndex_Object = MibTableColumn
hwCePingIndex = _HwCePingIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 1, 1, 1),
    _HwCePingIndex_Type()
)
hwCePingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCePingIndex.setStatus("current")
_HwCePingTargetAddress_Type = IpAddress
_HwCePingTargetAddress_Object = MibTableColumn
hwCePingTargetAddress = _HwCePingTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 1, 1, 2),
    _HwCePingTargetAddress_Type()
)
hwCePingTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCePingTargetAddress.setStatus("current")
_HwCePingSourceAddress_Type = IpAddress
_HwCePingSourceAddress_Object = MibTableColumn
hwCePingSourceAddress = _HwCePingSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 1, 1, 3),
    _HwCePingSourceAddress_Type()
)
hwCePingSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCePingSourceAddress.setStatus("current")


class _HwCePingVsiName_Type(OctetString):
    """Custom type hwCePingVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwCePingVsiName_Type.__name__ = "OctetString"
_HwCePingVsiName_Object = MibTableColumn
hwCePingVsiName = _HwCePingVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 1, 1, 4),
    _HwCePingVsiName_Type()
)
hwCePingVsiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCePingVsiName.setStatus("current")


class _HwCePingInterval_Type(Integer32):
    """Custom type hwCePingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwCePingInterval_Type.__name__ = "Integer32"
_HwCePingInterval_Object = MibTableColumn
hwCePingInterval = _HwCePingInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 1, 1, 5),
    _HwCePingInterval_Type()
)
hwCePingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCePingInterval.setStatus("current")


class _HwCePingCount_Type(Integer32):
    """Custom type hwCePingCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwCePingCount_Type.__name__ = "Integer32"
_HwCePingCount_Object = MibTableColumn
hwCePingCount = _HwCePingCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 1, 1, 6),
    _HwCePingCount_Type()
)
hwCePingCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCePingCount.setStatus("current")
_HwCePingRowStatus_Type = RowStatus
_HwCePingRowStatus_Object = MibTableColumn
hwCePingRowStatus = _HwCePingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 1, 1, 51),
    _HwCePingRowStatus_Type()
)
hwCePingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCePingRowStatus.setStatus("current")
_HwCePingResultTable_Object = MibTable
hwCePingResultTable = _HwCePingResultTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 2)
)
if mibBuilder.loadTexts:
    hwCePingResultTable.setStatus("current")
_HwCePingResultEntry_Object = MibTableRow
hwCePingResultEntry = _HwCePingResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 2, 1)
)
hwCePingResultEntry.setIndexNames(
    (0, "HUAWEI-CE-PING-MIB", "hwCePingIndex"),
)
if mibBuilder.loadTexts:
    hwCePingResultEntry.setStatus("current")


class _HwCePingResultOperStatus_Type(Integer32):
    """Custom type hwCePingResultOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inProcess", 2),
          ("sucessful", 1),
          ("timeout", 3))
    )


_HwCePingResultOperStatus_Type.__name__ = "Integer32"
_HwCePingResultOperStatus_Object = MibTableColumn
hwCePingResultOperStatus = _HwCePingResultOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 2, 1, 1),
    _HwCePingResultOperStatus_Type()
)
hwCePingResultOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCePingResultOperStatus.setStatus("current")
_HwCePingResultMac_Type = MacAddress
_HwCePingResultMac_Object = MibTableColumn
hwCePingResultMac = _HwCePingResultMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 2, 1, 2),
    _HwCePingResultMac_Type()
)
hwCePingResultMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCePingResultMac.setStatus("current")
_HwCePingGroup_ObjectIdentity = ObjectIdentity
hwCePingGroup = _HwCePingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 3)
)

# Managed Objects groups

hwCePingCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 3, 1)
)
hwCePingCtrlGroup.setObjects(
      *(("HUAWEI-CE-PING-MIB", "hwCePingTargetAddress"),
        ("HUAWEI-CE-PING-MIB", "hwCePingSourceAddress"),
        ("HUAWEI-CE-PING-MIB", "hwCePingVsiName"),
        ("HUAWEI-CE-PING-MIB", "hwCePingInterval"),
        ("HUAWEI-CE-PING-MIB", "hwCePingCount"),
        ("HUAWEI-CE-PING-MIB", "hwCePingRowStatus"))
)
if mibBuilder.loadTexts:
    hwCePingCtrlGroup.setStatus("current")

hwCePingResultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 3, 2)
)
hwCePingResultGroup.setObjects(
      *(("HUAWEI-CE-PING-MIB", "hwCePingResultOperStatus"),
        ("HUAWEI-CE-PING-MIB", "hwCePingResultMac"))
)
if mibBuilder.loadTexts:
    hwCePingResultGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-CE-PING-MIB",
    **{"hwCePing": hwCePing,
       "hwCePingTable": hwCePingTable,
       "hwCePingEntry": hwCePingEntry,
       "hwCePingIndex": hwCePingIndex,
       "hwCePingTargetAddress": hwCePingTargetAddress,
       "hwCePingSourceAddress": hwCePingSourceAddress,
       "hwCePingVsiName": hwCePingVsiName,
       "hwCePingInterval": hwCePingInterval,
       "hwCePingCount": hwCePingCount,
       "hwCePingRowStatus": hwCePingRowStatus,
       "hwCePingResultTable": hwCePingResultTable,
       "hwCePingResultEntry": hwCePingResultEntry,
       "hwCePingResultOperStatus": hwCePingResultOperStatus,
       "hwCePingResultMac": hwCePingResultMac,
       "hwCePingGroup": hwCePingGroup,
       "hwCePingCtrlGroup": hwCePingCtrlGroup,
       "hwCePingResultGroup": hwCePingResultGroup}
)
