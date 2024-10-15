# SNMP MIB module (HUAWEI-L2TP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-L2TP-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:22 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwL2TPExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 137)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwL2TPStatistic_ObjectIdentity = ObjectIdentity
hwL2TPStatistic = _HwL2TPStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 137, 1)
)
_HwL2TPSessionStatTable_Object = MibTable
hwL2TPSessionStatTable = _HwL2TPSessionStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 137, 1, 1)
)
if mibBuilder.loadTexts:
    hwL2TPSessionStatTable.setStatus("current")
_HwL2TPSessionStatEntry_Object = MibTableRow
hwL2TPSessionStatEntry = _HwL2TPSessionStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 137, 1, 1, 1)
)
hwL2TPSessionStatEntry.setIndexNames(
    (0, "HUAWEI-L2TP-EXT-MIB", "hwL2TPSessionIndex"),
)
if mibBuilder.loadTexts:
    hwL2TPSessionStatEntry.setStatus("current")


class _HwL2TPSessionIndex_Type(Integer32):
    """Custom type hwL2TPSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwL2TPSessionIndex_Type.__name__ = "Integer32"
_HwL2TPSessionIndex_Object = MibTableColumn
hwL2TPSessionIndex = _HwL2TPSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 137, 1, 1, 1, 1),
    _HwL2TPSessionIndex_Type()
)
hwL2TPSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2TPSessionIndex.setStatus("current")
_HwL2TPSessionStatUpPkts_Type = Counter64
_HwL2TPSessionStatUpPkts_Object = MibTableColumn
hwL2TPSessionStatUpPkts = _HwL2TPSessionStatUpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 137, 1, 1, 1, 2),
    _HwL2TPSessionStatUpPkts_Type()
)
hwL2TPSessionStatUpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2TPSessionStatUpPkts.setStatus("current")
_HwL2TPSessionStatUpBytes_Type = Counter64
_HwL2TPSessionStatUpBytes_Object = MibTableColumn
hwL2TPSessionStatUpBytes = _HwL2TPSessionStatUpBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 137, 1, 1, 1, 3),
    _HwL2TPSessionStatUpBytes_Type()
)
hwL2TPSessionStatUpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2TPSessionStatUpBytes.setStatus("current")
_HwL2TPSessionStatDownPkts_Type = Counter64
_HwL2TPSessionStatDownPkts_Object = MibTableColumn
hwL2TPSessionStatDownPkts = _HwL2TPSessionStatDownPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 137, 1, 1, 1, 4),
    _HwL2TPSessionStatDownPkts_Type()
)
hwL2TPSessionStatDownPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2TPSessionStatDownPkts.setStatus("current")
_HwL2TPSessionStatDownBytes_Type = Counter64
_HwL2TPSessionStatDownBytes_Object = MibTableColumn
hwL2TPSessionStatDownBytes = _HwL2TPSessionStatDownBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 137, 1, 1, 1, 5),
    _HwL2TPSessionStatDownBytes_Type()
)
hwL2TPSessionStatDownBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2TPSessionStatDownBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-L2TP-EXT-MIB",
    **{"hwL2TPExt": hwL2TPExt,
       "hwL2TPStatistic": hwL2TPStatistic,
       "hwL2TPSessionStatTable": hwL2TPSessionStatTable,
       "hwL2TPSessionStatEntry": hwL2TPSessionStatEntry,
       "hwL2TPSessionIndex": hwL2TPSessionIndex,
       "hwL2TPSessionStatUpPkts": hwL2TPSessionStatUpPkts,
       "hwL2TPSessionStatUpBytes": hwL2TPSessionStatUpBytes,
       "hwL2TPSessionStatDownPkts": hwL2TPSessionStatDownPkts,
       "hwL2TPSessionStatDownBytes": hwL2TPSessionStatDownBytes}
)
