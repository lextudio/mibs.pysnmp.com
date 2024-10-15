# SNMP MIB module (HUAWEI-ISOLATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-ISOLATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:15 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

hwIsolateMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 247)
)
hwIsolateMIB.setRevisions(
        ("2014-03-12 15:28",
         "2010-08-11 16:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwIsolateObjects_ObjectIdentity = ObjectIdentity
hwIsolateObjects = _HwIsolateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1)
)
_HwIsolateTable_ObjectIdentity = ObjectIdentity
hwIsolateTable = _HwIsolateTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1, 2)
)
_HwPortIsolateMode_Type = Integer32
_HwPortIsolateMode_Object = MibScalar
hwPortIsolateMode = _HwPortIsolateMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1, 2, 1),
    _HwPortIsolateMode_Type()
)
hwPortIsolateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortIsolateMode.setStatus("current")
_HwPortIsolateTable_Object = MibTable
hwPortIsolateTable = _HwPortIsolateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hwPortIsolateTable.setStatus("current")
_HwPortIsolateEntry_Object = MibTableRow
hwPortIsolateEntry = _HwPortIsolateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1, 2, 2, 1)
)
hwPortIsolateEntry.setIndexNames(
    (0, "HUAWEI-ISOLATE-MIB", "hwPortIsolateIfIndex"),
    (0, "HUAWEI-ISOLATE-MIB", "hwPortIsolateGroupId"),
)
if mibBuilder.loadTexts:
    hwPortIsolateEntry.setStatus("current")


class _HwPortIsolateGroupId_Type(Integer32):
    """Custom type hwPortIsolateGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwPortIsolateGroupId_Type.__name__ = "Integer32"
_HwPortIsolateGroupId_Object = MibTableColumn
hwPortIsolateGroupId = _HwPortIsolateGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1, 2, 2, 1, 1),
    _HwPortIsolateGroupId_Type()
)
hwPortIsolateGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortIsolateGroupId.setStatus("current")
_HwPortIsolateIfIndex_Type = InterfaceIndex
_HwPortIsolateIfIndex_Object = MibTableColumn
hwPortIsolateIfIndex = _HwPortIsolateIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1, 2, 2, 1, 2),
    _HwPortIsolateIfIndex_Type()
)
hwPortIsolateIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortIsolateIfIndex.setStatus("current")
_HwPortIsolateRowStatus_Type = RowStatus
_HwPortIsolateRowStatus_Object = MibTableColumn
hwPortIsolateRowStatus = _HwPortIsolateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1, 2, 2, 1, 3),
    _HwPortIsolateRowStatus_Type()
)
hwPortIsolateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortIsolateRowStatus.setStatus("current")
_HwAmIsolateTable_Object = MibTable
hwAmIsolateTable = _HwAmIsolateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hwAmIsolateTable.setStatus("current")
_HwAmIsolateEntry_Object = MibTableRow
hwAmIsolateEntry = _HwAmIsolateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1, 2, 3, 1)
)
hwAmIsolateEntry.setIndexNames(
    (0, "HUAWEI-ISOLATE-MIB", "hwAmIsolateSrcIfIndex"),
    (0, "HUAWEI-ISOLATE-MIB", "hwAmIsolateDstIfIndex"),
)
if mibBuilder.loadTexts:
    hwAmIsolateEntry.setStatus("current")
_HwAmIsolateSrcIfIndex_Type = InterfaceIndex
_HwAmIsolateSrcIfIndex_Object = MibTableColumn
hwAmIsolateSrcIfIndex = _HwAmIsolateSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1, 2, 3, 1, 1),
    _HwAmIsolateSrcIfIndex_Type()
)
hwAmIsolateSrcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAmIsolateSrcIfIndex.setStatus("current")
_HwAmIsolateDstIfIndex_Type = InterfaceIndex
_HwAmIsolateDstIfIndex_Object = MibTableColumn
hwAmIsolateDstIfIndex = _HwAmIsolateDstIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1, 2, 3, 1, 2),
    _HwAmIsolateDstIfIndex_Type()
)
hwAmIsolateDstIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAmIsolateDstIfIndex.setStatus("current")
_HwAmIsolateRowStatus_Type = RowStatus
_HwAmIsolateRowStatus_Object = MibTableColumn
hwAmIsolateRowStatus = _HwAmIsolateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1, 2, 3, 1, 3),
    _HwAmIsolateRowStatus_Type()
)
hwAmIsolateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAmIsolateRowStatus.setStatus("current")

# Managed Objects groups

hwIsolateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1, 2, 4)
)
hwIsolateGroup.setObjects(
      *(("HUAWEI-ISOLATE-MIB", "hwPortIsolateMode"),
        ("HUAWEI-ISOLATE-MIB", "hwPortIsolateRowStatus"),
        ("HUAWEI-ISOLATE-MIB", "hwAmIsolateRowStatus"))
)
if mibBuilder.loadTexts:
    hwIsolateGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwIsolateComformance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 3)
)
if mibBuilder.loadTexts:
    hwIsolateComformance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-ISOLATE-MIB",
    **{"hwIsolateMIB": hwIsolateMIB,
       "hwIsolateObjects": hwIsolateObjects,
       "hwIsolateTable": hwIsolateTable,
       "hwPortIsolateMode": hwPortIsolateMode,
       "hwPortIsolateTable": hwPortIsolateTable,
       "hwPortIsolateEntry": hwPortIsolateEntry,
       "hwPortIsolateGroupId": hwPortIsolateGroupId,
       "hwPortIsolateIfIndex": hwPortIsolateIfIndex,
       "hwPortIsolateRowStatus": hwPortIsolateRowStatus,
       "hwAmIsolateTable": hwAmIsolateTable,
       "hwAmIsolateEntry": hwAmIsolateEntry,
       "hwAmIsolateSrcIfIndex": hwAmIsolateSrcIfIndex,
       "hwAmIsolateDstIfIndex": hwAmIsolateDstIfIndex,
       "hwAmIsolateRowStatus": hwAmIsolateRowStatus,
       "hwIsolateGroup": hwIsolateGroup,
       "hwIsolateComformance": hwIsolateComformance}
)
