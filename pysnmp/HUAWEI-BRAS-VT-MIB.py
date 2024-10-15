# SNMP MIB module (HUAWEI-BRAS-VT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-BRAS-VT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:15 2024
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

hwIFVT = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwhwIFVTMibObjects_ObjectIdentity = ObjectIdentity
hwhwIFVTMibObjects = _HwhwIFVTMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 10, 1)
)
_HwIFVTTable_Object = MibTable
hwIFVTTable = _HwIFVTTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 10, 1, 1)
)
if mibBuilder.loadTexts:
    hwIFVTTable.setStatus("current")
_HwIFVTEntry_Object = MibTableRow
hwIFVTEntry = _HwIFVTEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 10, 1, 1, 1)
)
hwIFVTEntry.setIndexNames(
    (0, "HUAWEI-BRAS-VT-MIB", "hwifVTNo"),
)
if mibBuilder.loadTexts:
    hwIFVTEntry.setStatus("current")


class _HwifVTNo_Type(Integer32):
    """Custom type hwifVTNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_HwifVTNo_Type.__name__ = "Integer32"
_HwifVTNo_Object = MibTableColumn
hwifVTNo = _HwifVTNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 10, 1, 1, 1, 1),
    _HwifVTNo_Type()
)
hwifVTNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifVTNo.setStatus("current")


class _HwifVTDescr_Type(OctetString):
    """Custom type hwifVTDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HwifVTDescr_Type.__name__ = "OctetString"
_HwifVTDescr_Object = MibTableColumn
hwifVTDescr = _HwifVTDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 10, 1, 1, 1, 2),
    _HwifVTDescr_Type()
)
hwifVTDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifVTDescr.setStatus("current")


class _HwifVTMtu_Type(Integer32):
    """Custom type hwifVTMtu based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 1500),
    )


_HwifVTMtu_Type.__name__ = "Integer32"
_HwifVTMtu_Object = MibTableColumn
hwifVTMtu = _HwifVTMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 10, 1, 1, 1, 3),
    _HwifVTMtu_Type()
)
hwifVTMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifVTMtu.setStatus("current")
_HwifVTRowStatus_Type = RowStatus
_HwifVTRowStatus_Object = MibTableColumn
hwifVTRowStatus = _HwifVTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 10, 1, 1, 1, 4),
    _HwifVTRowStatus_Type()
)
hwifVTRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifVTRowStatus.setStatus("current")
_HwIfVtConformance_ObjectIdentity = ObjectIdentity
hwIfVtConformance = _HwIfVtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 10, 2)
)
_HwIfVtCompliances_ObjectIdentity = ObjectIdentity
hwIfVtCompliances = _HwIfVtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 10, 2, 1)
)
_HwIfVtObjectGroups_ObjectIdentity = ObjectIdentity
hwIfVtObjectGroups = _HwIfVtObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 10, 2, 2)
)

# Managed Objects groups

hwIfVtTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 10, 2, 2, 1)
)
hwIfVtTableGroup.setObjects(
      *(("HUAWEI-BRAS-VT-MIB", "hwifVTNo"),
        ("HUAWEI-BRAS-VT-MIB", "hwifVTDescr"),
        ("HUAWEI-BRAS-VT-MIB", "hwifVTMtu"),
        ("HUAWEI-BRAS-VT-MIB", "hwifVTRowStatus"))
)
if mibBuilder.loadTexts:
    hwIfVtTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwIfVtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 10, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwIfVtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-BRAS-VT-MIB",
    **{"hwIFVT": hwIFVT,
       "hwhwIFVTMibObjects": hwhwIFVTMibObjects,
       "hwIFVTTable": hwIFVTTable,
       "hwIFVTEntry": hwIFVTEntry,
       "hwifVTNo": hwifVTNo,
       "hwifVTDescr": hwifVTDescr,
       "hwifVTMtu": hwifVTMtu,
       "hwifVTRowStatus": hwifVTRowStatus,
       "hwIfVtConformance": hwIfVtConformance,
       "hwIfVtCompliances": hwIfVtCompliances,
       "hwIfVtCompliance": hwIfVtCompliance,
       "hwIfVtObjectGroups": hwIfVtObjectGroups,
       "hwIfVtTableGroup": hwIfVtTableGroup}
)
