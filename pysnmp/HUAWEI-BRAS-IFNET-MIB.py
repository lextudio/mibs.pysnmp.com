# SNMP MIB module (HUAWEI-BRAS-IFNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-BRAS-IFNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:59 2024
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

(hwBRASMib,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwBRASMib")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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

hwSUBINT = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwhwSUBINTMibObjects_ObjectIdentity = ObjectIdentity
hwhwSUBINTMibObjects = _HwhwSUBINTMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 11, 1)
)
_HwSubIntTable_Object = MibTable
hwSubIntTable = _HwSubIntTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 11, 1, 1)
)
if mibBuilder.loadTexts:
    hwSubIntTable.setStatus("current")
_HwSubIntEntry_Object = MibTableRow
hwSubIntEntry = _HwSubIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 11, 1, 1, 1)
)
hwSubIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-BRAS-IFNET-MIB", "hwSubInterfaceNo"),
)
if mibBuilder.loadTexts:
    hwSubIntEntry.setStatus("current")


class _HwSubInterfaceNo_Type(Integer32):
    """Custom type hwSubInterfaceNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_HwSubInterfaceNo_Type.__name__ = "Integer32"
_HwSubInterfaceNo_Object = MibTableColumn
hwSubInterfaceNo = _HwSubInterfaceNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 11, 1, 1, 1, 1),
    _HwSubInterfaceNo_Type()
)
hwSubInterfaceNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSubInterfaceNo.setStatus("current")
_HwSubIntRowStatus_Type = RowStatus
_HwSubIntRowStatus_Object = MibTableColumn
hwSubIntRowStatus = _HwSubIntRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 11, 1, 1, 1, 2),
    _HwSubIntRowStatus_Type()
)
hwSubIntRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSubIntRowStatus.setStatus("current")
_HwSubIfIndex_Type = InterfaceIndex
_HwSubIfIndex_Object = MibTableColumn
hwSubIfIndex = _HwSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 11, 1, 1, 1, 3),
    _HwSubIfIndex_Type()
)
hwSubIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSubIfIndex.setStatus("current")


class _HwSubIfDescr_Type(DisplayString):
    """Custom type hwSubIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwSubIfDescr_Type.__name__ = "DisplayString"
_HwSubIfDescr_Object = MibTableColumn
hwSubIfDescr = _HwSubIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 11, 1, 1, 1, 4),
    _HwSubIfDescr_Type()
)
hwSubIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSubIfDescr.setStatus("current")
_HwSubIntConformance_ObjectIdentity = ObjectIdentity
hwSubIntConformance = _HwSubIntConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 11, 2)
)
_HwSubIntCompliances_ObjectIdentity = ObjectIdentity
hwSubIntCompliances = _HwSubIntCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 11, 2, 1)
)
_HwSubIntTableGroups_ObjectIdentity = ObjectIdentity
hwSubIntTableGroups = _HwSubIntTableGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 11, 2, 2)
)

# Managed Objects groups

hwSubIntTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 11, 2, 2, 1)
)
hwSubIntTableGroup.setObjects(
      *(("HUAWEI-BRAS-IFNET-MIB", "hwSubInterfaceNo"),
        ("HUAWEI-BRAS-IFNET-MIB", "hwSubIntRowStatus"),
        ("HUAWEI-BRAS-IFNET-MIB", "hwSubIfIndex"),
        ("HUAWEI-BRAS-IFNET-MIB", "hwSubIfDescr"))
)
if mibBuilder.loadTexts:
    hwSubIntTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwSubIntCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 11, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwSubIntCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-BRAS-IFNET-MIB",
    **{"hwSUBINT": hwSUBINT,
       "hwhwSUBINTMibObjects": hwhwSUBINTMibObjects,
       "hwSubIntTable": hwSubIntTable,
       "hwSubIntEntry": hwSubIntEntry,
       "hwSubInterfaceNo": hwSubInterfaceNo,
       "hwSubIntRowStatus": hwSubIntRowStatus,
       "hwSubIfIndex": hwSubIfIndex,
       "hwSubIfDescr": hwSubIfDescr,
       "hwSubIntConformance": hwSubIntConformance,
       "hwSubIntCompliances": hwSubIntCompliances,
       "hwSubIntCompliance": hwSubIntCompliance,
       "hwSubIntTableGroups": hwSubIntTableGroups,
       "hwSubIntTableGroup": hwSubIntTableGroup}
)
