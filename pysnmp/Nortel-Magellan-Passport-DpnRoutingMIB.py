# SNMP MIB module (Nortel-Magellan-Passport-DpnRoutingMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-DpnRoutingMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:38 2024
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

(rtg,
 rtgIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-BaseRoutingMIB",
    "rtg",
    "rtgIndex")

(DisplayString,
 Integer32,
 PassportCounter64,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "PassportCounter64",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiStringIndex,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiStringIndex",
    "NonReplicated")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "passportMIBs")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RtgDpn_ObjectIdentity = ObjectIdentity
rtgDpn = _RtgDpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4)
)
_RtgDpnRowStatusTable_Object = MibTable
rtgDpnRowStatusTable = _RtgDpnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 1)
)
if mibBuilder.loadTexts:
    rtgDpnRowStatusTable.setStatus("mandatory")
_RtgDpnRowStatusEntry_Object = MibTableRow
rtgDpnRowStatusEntry = _RtgDpnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 1, 1)
)
rtgDpnRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnRowStatusEntry.setStatus("mandatory")
_RtgDpnRowStatus_Type = RowStatus
_RtgDpnRowStatus_Object = MibTableColumn
rtgDpnRowStatus = _RtgDpnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 1, 1, 1),
    _RtgDpnRowStatus_Type()
)
rtgDpnRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnRowStatus.setStatus("mandatory")
_RtgDpnComponentName_Type = DisplayString
_RtgDpnComponentName_Object = MibTableColumn
rtgDpnComponentName = _RtgDpnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 1, 1, 2),
    _RtgDpnComponentName_Type()
)
rtgDpnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnComponentName.setStatus("mandatory")
_RtgDpnStorageType_Type = StorageType
_RtgDpnStorageType_Object = MibTableColumn
rtgDpnStorageType = _RtgDpnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 1, 1, 4),
    _RtgDpnStorageType_Type()
)
rtgDpnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnStorageType.setStatus("mandatory")
_RtgDpnIndex_Type = NonReplicated
_RtgDpnIndex_Object = MibTableColumn
rtgDpnIndex = _RtgDpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 1, 1, 10),
    _RtgDpnIndex_Type()
)
rtgDpnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnIndex.setStatus("mandatory")
_RtgDpnRid_ObjectIdentity = ObjectIdentity
rtgDpnRid = _RtgDpnRid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2)
)
_RtgDpnRidRowStatusTable_Object = MibTable
rtgDpnRidRowStatusTable = _RtgDpnRidRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 1)
)
if mibBuilder.loadTexts:
    rtgDpnRidRowStatusTable.setStatus("mandatory")
_RtgDpnRidRowStatusEntry_Object = MibTableRow
rtgDpnRidRowStatusEntry = _RtgDpnRidRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 1, 1)
)
rtgDpnRidRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnRidIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnRidRowStatusEntry.setStatus("mandatory")
_RtgDpnRidRowStatus_Type = RowStatus
_RtgDpnRidRowStatus_Object = MibTableColumn
rtgDpnRidRowStatus = _RtgDpnRidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 1, 1, 1),
    _RtgDpnRidRowStatus_Type()
)
rtgDpnRidRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnRidRowStatus.setStatus("mandatory")
_RtgDpnRidComponentName_Type = DisplayString
_RtgDpnRidComponentName_Object = MibTableColumn
rtgDpnRidComponentName = _RtgDpnRidComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 1, 1, 2),
    _RtgDpnRidComponentName_Type()
)
rtgDpnRidComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnRidComponentName.setStatus("mandatory")
_RtgDpnRidStorageType_Type = StorageType
_RtgDpnRidStorageType_Object = MibTableColumn
rtgDpnRidStorageType = _RtgDpnRidStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 1, 1, 4),
    _RtgDpnRidStorageType_Type()
)
rtgDpnRidStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnRidStorageType.setStatus("mandatory")


class _RtgDpnRidIndex_Type(Integer32):
    """Custom type rtgDpnRidIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_RtgDpnRidIndex_Type.__name__ = "Integer32"
_RtgDpnRidIndex_Object = MibTableColumn
rtgDpnRidIndex = _RtgDpnRidIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 1, 1, 10),
    _RtgDpnRidIndex_Type()
)
rtgDpnRidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnRidIndex.setStatus("mandatory")
_RtgDpnRidMid_ObjectIdentity = ObjectIdentity
rtgDpnRidMid = _RtgDpnRidMid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 2)
)
_RtgDpnRidMidRowStatusTable_Object = MibTable
rtgDpnRidMidRowStatusTable = _RtgDpnRidMidRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rtgDpnRidMidRowStatusTable.setStatus("mandatory")
_RtgDpnRidMidRowStatusEntry_Object = MibTableRow
rtgDpnRidMidRowStatusEntry = _RtgDpnRidMidRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 2, 1, 1)
)
rtgDpnRidMidRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnRidIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnRidMidIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnRidMidRowStatusEntry.setStatus("mandatory")
_RtgDpnRidMidRowStatus_Type = RowStatus
_RtgDpnRidMidRowStatus_Object = MibTableColumn
rtgDpnRidMidRowStatus = _RtgDpnRidMidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 2, 1, 1, 1),
    _RtgDpnRidMidRowStatus_Type()
)
rtgDpnRidMidRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnRidMidRowStatus.setStatus("mandatory")
_RtgDpnRidMidComponentName_Type = DisplayString
_RtgDpnRidMidComponentName_Object = MibTableColumn
rtgDpnRidMidComponentName = _RtgDpnRidMidComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 2, 1, 1, 2),
    _RtgDpnRidMidComponentName_Type()
)
rtgDpnRidMidComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnRidMidComponentName.setStatus("mandatory")
_RtgDpnRidMidStorageType_Type = StorageType
_RtgDpnRidMidStorageType_Object = MibTableColumn
rtgDpnRidMidStorageType = _RtgDpnRidMidStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 2, 1, 1, 4),
    _RtgDpnRidMidStorageType_Type()
)
rtgDpnRidMidStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnRidMidStorageType.setStatus("mandatory")


class _RtgDpnRidMidIndex_Type(Integer32):
    """Custom type rtgDpnRidMidIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2046),
    )


_RtgDpnRidMidIndex_Type.__name__ = "Integer32"
_RtgDpnRidMidIndex_Object = MibTableColumn
rtgDpnRidMidIndex = _RtgDpnRidMidIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 2, 1, 1, 10),
    _RtgDpnRidMidIndex_Type()
)
rtgDpnRidMidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnRidMidIndex.setStatus("mandatory")
_RtgDpnRidOperTable_Object = MibTable
rtgDpnRidOperTable = _RtgDpnRidOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 10)
)
if mibBuilder.loadTexts:
    rtgDpnRidOperTable.setStatus("mandatory")
_RtgDpnRidOperEntry_Object = MibTableRow
rtgDpnRidOperEntry = _RtgDpnRidOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 10, 1)
)
rtgDpnRidOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnRidIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnRidOperEntry.setStatus("mandatory")


class _RtgDpnRidDpnDelayMetric_Type(Unsigned32):
    """Custom type rtgDpnRidDpnDelayMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RtgDpnRidDpnDelayMetric_Type.__name__ = "Unsigned32"
_RtgDpnRidDpnDelayMetric_Object = MibTableColumn
rtgDpnRidDpnDelayMetric = _RtgDpnRidDpnDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 10, 1, 1),
    _RtgDpnRidDpnDelayMetric_Type()
)
rtgDpnRidDpnDelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnRidDpnDelayMetric.setStatus("mandatory")


class _RtgDpnRidDpnTputMetric_Type(Unsigned32):
    """Custom type rtgDpnRidDpnTputMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RtgDpnRidDpnTputMetric_Type.__name__ = "Unsigned32"
_RtgDpnRidDpnTputMetric_Object = MibTableColumn
rtgDpnRidDpnTputMetric = _RtgDpnRidDpnTputMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 10, 1, 2),
    _RtgDpnRidDpnTputMetric_Type()
)
rtgDpnRidDpnTputMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnRidDpnTputMetric.setStatus("mandatory")
_RtgDpnRidDelayNextHopLinkGroupsTable_Object = MibTable
rtgDpnRidDelayNextHopLinkGroupsTable = _RtgDpnRidDelayNextHopLinkGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 226)
)
if mibBuilder.loadTexts:
    rtgDpnRidDelayNextHopLinkGroupsTable.setStatus("mandatory")
_RtgDpnRidDelayNextHopLinkGroupsEntry_Object = MibTableRow
rtgDpnRidDelayNextHopLinkGroupsEntry = _RtgDpnRidDelayNextHopLinkGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 226, 1)
)
rtgDpnRidDelayNextHopLinkGroupsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnRidIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnRidDelayNextHopLinkGroupsIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnRidDelayNextHopLinkGroupsEntry.setStatus("mandatory")


class _RtgDpnRidDelayNextHopLinkGroupsIndex_Type(Integer32):
    """Custom type rtgDpnRidDelayNextHopLinkGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RtgDpnRidDelayNextHopLinkGroupsIndex_Type.__name__ = "Integer32"
_RtgDpnRidDelayNextHopLinkGroupsIndex_Object = MibTableColumn
rtgDpnRidDelayNextHopLinkGroupsIndex = _RtgDpnRidDelayNextHopLinkGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 226, 1, 1),
    _RtgDpnRidDelayNextHopLinkGroupsIndex_Type()
)
rtgDpnRidDelayNextHopLinkGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnRidDelayNextHopLinkGroupsIndex.setStatus("mandatory")
_RtgDpnRidDelayNextHopLinkGroupsValue_Type = RowPointer
_RtgDpnRidDelayNextHopLinkGroupsValue_Object = MibTableColumn
rtgDpnRidDelayNextHopLinkGroupsValue = _RtgDpnRidDelayNextHopLinkGroupsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 226, 1, 2),
    _RtgDpnRidDelayNextHopLinkGroupsValue_Type()
)
rtgDpnRidDelayNextHopLinkGroupsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnRidDelayNextHopLinkGroupsValue.setStatus("mandatory")
_RtgDpnRidTputNextHopLinkGroupsTable_Object = MibTable
rtgDpnRidTputNextHopLinkGroupsTable = _RtgDpnRidTputNextHopLinkGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 227)
)
if mibBuilder.loadTexts:
    rtgDpnRidTputNextHopLinkGroupsTable.setStatus("mandatory")
_RtgDpnRidTputNextHopLinkGroupsEntry_Object = MibTableRow
rtgDpnRidTputNextHopLinkGroupsEntry = _RtgDpnRidTputNextHopLinkGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 227, 1)
)
rtgDpnRidTputNextHopLinkGroupsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnRidIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnRidTputNextHopLinkGroupsIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnRidTputNextHopLinkGroupsEntry.setStatus("mandatory")


class _RtgDpnRidTputNextHopLinkGroupsIndex_Type(Integer32):
    """Custom type rtgDpnRidTputNextHopLinkGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RtgDpnRidTputNextHopLinkGroupsIndex_Type.__name__ = "Integer32"
_RtgDpnRidTputNextHopLinkGroupsIndex_Object = MibTableColumn
rtgDpnRidTputNextHopLinkGroupsIndex = _RtgDpnRidTputNextHopLinkGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 227, 1, 1),
    _RtgDpnRidTputNextHopLinkGroupsIndex_Type()
)
rtgDpnRidTputNextHopLinkGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnRidTputNextHopLinkGroupsIndex.setStatus("mandatory")
_RtgDpnRidTputNextHopLinkGroupsValue_Type = RowPointer
_RtgDpnRidTputNextHopLinkGroupsValue_Object = MibTableColumn
rtgDpnRidTputNextHopLinkGroupsValue = _RtgDpnRidTputNextHopLinkGroupsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 227, 1, 2),
    _RtgDpnRidTputNextHopLinkGroupsValue_Type()
)
rtgDpnRidTputNextHopLinkGroupsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnRidTputNextHopLinkGroupsValue.setStatus("mandatory")
_RtgDpnRidDelayPathTrafficProportionsTable_Object = MibTable
rtgDpnRidDelayPathTrafficProportionsTable = _RtgDpnRidDelayPathTrafficProportionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 328)
)
if mibBuilder.loadTexts:
    rtgDpnRidDelayPathTrafficProportionsTable.setStatus("mandatory")
_RtgDpnRidDelayPathTrafficProportionsEntry_Object = MibTableRow
rtgDpnRidDelayPathTrafficProportionsEntry = _RtgDpnRidDelayPathTrafficProportionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 328, 1)
)
rtgDpnRidDelayPathTrafficProportionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnRidIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnRidDelayPathTrafficProportionsIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnRidDelayPathTrafficProportionsEntry.setStatus("mandatory")


class _RtgDpnRidDelayPathTrafficProportionsIndex_Type(Integer32):
    """Custom type rtgDpnRidDelayPathTrafficProportionsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RtgDpnRidDelayPathTrafficProportionsIndex_Type.__name__ = "Integer32"
_RtgDpnRidDelayPathTrafficProportionsIndex_Object = MibTableColumn
rtgDpnRidDelayPathTrafficProportionsIndex = _RtgDpnRidDelayPathTrafficProportionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 328, 1, 1),
    _RtgDpnRidDelayPathTrafficProportionsIndex_Type()
)
rtgDpnRidDelayPathTrafficProportionsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnRidDelayPathTrafficProportionsIndex.setStatus("mandatory")


class _RtgDpnRidDelayPathTrafficProportionsValue_Type(Unsigned32):
    """Custom type rtgDpnRidDelayPathTrafficProportionsValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RtgDpnRidDelayPathTrafficProportionsValue_Type.__name__ = "Unsigned32"
_RtgDpnRidDelayPathTrafficProportionsValue_Object = MibTableColumn
rtgDpnRidDelayPathTrafficProportionsValue = _RtgDpnRidDelayPathTrafficProportionsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 328, 1, 2),
    _RtgDpnRidDelayPathTrafficProportionsValue_Type()
)
rtgDpnRidDelayPathTrafficProportionsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnRidDelayPathTrafficProportionsValue.setStatus("mandatory")
_RtgDpnRidTputPathTrafficProportionsTable_Object = MibTable
rtgDpnRidTputPathTrafficProportionsTable = _RtgDpnRidTputPathTrafficProportionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 329)
)
if mibBuilder.loadTexts:
    rtgDpnRidTputPathTrafficProportionsTable.setStatus("mandatory")
_RtgDpnRidTputPathTrafficProportionsEntry_Object = MibTableRow
rtgDpnRidTputPathTrafficProportionsEntry = _RtgDpnRidTputPathTrafficProportionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 329, 1)
)
rtgDpnRidTputPathTrafficProportionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnRidIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnRidTputPathTrafficProportionsIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnRidTputPathTrafficProportionsEntry.setStatus("mandatory")


class _RtgDpnRidTputPathTrafficProportionsIndex_Type(Integer32):
    """Custom type rtgDpnRidTputPathTrafficProportionsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RtgDpnRidTputPathTrafficProportionsIndex_Type.__name__ = "Integer32"
_RtgDpnRidTputPathTrafficProportionsIndex_Object = MibTableColumn
rtgDpnRidTputPathTrafficProportionsIndex = _RtgDpnRidTputPathTrafficProportionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 329, 1, 1),
    _RtgDpnRidTputPathTrafficProportionsIndex_Type()
)
rtgDpnRidTputPathTrafficProportionsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnRidTputPathTrafficProportionsIndex.setStatus("mandatory")


class _RtgDpnRidTputPathTrafficProportionsValue_Type(Unsigned32):
    """Custom type rtgDpnRidTputPathTrafficProportionsValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RtgDpnRidTputPathTrafficProportionsValue_Type.__name__ = "Unsigned32"
_RtgDpnRidTputPathTrafficProportionsValue_Object = MibTableColumn
rtgDpnRidTputPathTrafficProportionsValue = _RtgDpnRidTputPathTrafficProportionsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 329, 1, 2),
    _RtgDpnRidTputPathTrafficProportionsValue_Type()
)
rtgDpnRidTputPathTrafficProportionsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnRidTputPathTrafficProportionsValue.setStatus("mandatory")
_RtgDpnRidDelayMetricTable_Object = MibTable
rtgDpnRidDelayMetricTable = _RtgDpnRidDelayMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 339)
)
if mibBuilder.loadTexts:
    rtgDpnRidDelayMetricTable.setStatus("mandatory")
_RtgDpnRidDelayMetricEntry_Object = MibTableRow
rtgDpnRidDelayMetricEntry = _RtgDpnRidDelayMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 339, 1)
)
rtgDpnRidDelayMetricEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnRidIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnRidDelayMetricIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnRidDelayMetricEntry.setStatus("mandatory")


class _RtgDpnRidDelayMetricIndex_Type(Integer32):
    """Custom type rtgDpnRidDelayMetricIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RtgDpnRidDelayMetricIndex_Type.__name__ = "Integer32"
_RtgDpnRidDelayMetricIndex_Object = MibTableColumn
rtgDpnRidDelayMetricIndex = _RtgDpnRidDelayMetricIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 339, 1, 1),
    _RtgDpnRidDelayMetricIndex_Type()
)
rtgDpnRidDelayMetricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnRidDelayMetricIndex.setStatus("mandatory")


class _RtgDpnRidDelayMetricValue_Type(Unsigned32):
    """Custom type rtgDpnRidDelayMetricValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RtgDpnRidDelayMetricValue_Type.__name__ = "Unsigned32"
_RtgDpnRidDelayMetricValue_Object = MibTableColumn
rtgDpnRidDelayMetricValue = _RtgDpnRidDelayMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 339, 1, 2),
    _RtgDpnRidDelayMetricValue_Type()
)
rtgDpnRidDelayMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnRidDelayMetricValue.setStatus("mandatory")
_RtgDpnRidTputMetricTable_Object = MibTable
rtgDpnRidTputMetricTable = _RtgDpnRidTputMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 340)
)
if mibBuilder.loadTexts:
    rtgDpnRidTputMetricTable.setStatus("mandatory")
_RtgDpnRidTputMetricEntry_Object = MibTableRow
rtgDpnRidTputMetricEntry = _RtgDpnRidTputMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 340, 1)
)
rtgDpnRidTputMetricEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnRidIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnRidTputMetricIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnRidTputMetricEntry.setStatus("mandatory")


class _RtgDpnRidTputMetricIndex_Type(Integer32):
    """Custom type rtgDpnRidTputMetricIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RtgDpnRidTputMetricIndex_Type.__name__ = "Integer32"
_RtgDpnRidTputMetricIndex_Object = MibTableColumn
rtgDpnRidTputMetricIndex = _RtgDpnRidTputMetricIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 340, 1, 1),
    _RtgDpnRidTputMetricIndex_Type()
)
rtgDpnRidTputMetricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnRidTputMetricIndex.setStatus("mandatory")


class _RtgDpnRidTputMetricValue_Type(Unsigned32):
    """Custom type rtgDpnRidTputMetricValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RtgDpnRidTputMetricValue_Type.__name__ = "Unsigned32"
_RtgDpnRidTputMetricValue_Object = MibTableColumn
rtgDpnRidTputMetricValue = _RtgDpnRidTputMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 2, 340, 1, 2),
    _RtgDpnRidTputMetricValue_Type()
)
rtgDpnRidTputMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnRidTputMetricValue.setStatus("mandatory")
_RtgDpnMid_ObjectIdentity = ObjectIdentity
rtgDpnMid = _RtgDpnMid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3)
)
_RtgDpnMidRowStatusTable_Object = MibTable
rtgDpnMidRowStatusTable = _RtgDpnMidRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 1)
)
if mibBuilder.loadTexts:
    rtgDpnMidRowStatusTable.setStatus("mandatory")
_RtgDpnMidRowStatusEntry_Object = MibTableRow
rtgDpnMidRowStatusEntry = _RtgDpnMidRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 1, 1)
)
rtgDpnMidRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnMidIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnMidRowStatusEntry.setStatus("mandatory")
_RtgDpnMidRowStatus_Type = RowStatus
_RtgDpnMidRowStatus_Object = MibTableColumn
rtgDpnMidRowStatus = _RtgDpnMidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 1, 1, 1),
    _RtgDpnMidRowStatus_Type()
)
rtgDpnMidRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnMidRowStatus.setStatus("mandatory")
_RtgDpnMidComponentName_Type = DisplayString
_RtgDpnMidComponentName_Object = MibTableColumn
rtgDpnMidComponentName = _RtgDpnMidComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 1, 1, 2),
    _RtgDpnMidComponentName_Type()
)
rtgDpnMidComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnMidComponentName.setStatus("mandatory")
_RtgDpnMidStorageType_Type = StorageType
_RtgDpnMidStorageType_Object = MibTableColumn
rtgDpnMidStorageType = _RtgDpnMidStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 1, 1, 4),
    _RtgDpnMidStorageType_Type()
)
rtgDpnMidStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnMidStorageType.setStatus("mandatory")


class _RtgDpnMidIndex_Type(Integer32):
    """Custom type rtgDpnMidIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2046),
    )


_RtgDpnMidIndex_Type.__name__ = "Integer32"
_RtgDpnMidIndex_Object = MibTableColumn
rtgDpnMidIndex = _RtgDpnMidIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 1, 1, 10),
    _RtgDpnMidIndex_Type()
)
rtgDpnMidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnMidIndex.setStatus("mandatory")
_RtgDpnMidOperTable_Object = MibTable
rtgDpnMidOperTable = _RtgDpnMidOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 10)
)
if mibBuilder.loadTexts:
    rtgDpnMidOperTable.setStatus("mandatory")
_RtgDpnMidOperEntry_Object = MibTableRow
rtgDpnMidOperEntry = _RtgDpnMidOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 10, 1)
)
rtgDpnMidOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnMidIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnMidOperEntry.setStatus("mandatory")


class _RtgDpnMidSubstituteRid_Type(Unsigned32):
    """Custom type rtgDpnMidSubstituteRid based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_RtgDpnMidSubstituteRid_Type.__name__ = "Unsigned32"
_RtgDpnMidSubstituteRid_Object = MibTableColumn
rtgDpnMidSubstituteRid = _RtgDpnMidSubstituteRid_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 10, 1, 3),
    _RtgDpnMidSubstituteRid_Type()
)
rtgDpnMidSubstituteRid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnMidSubstituteRid.setStatus("mandatory")
_RtgDpnMidDelayNextHopLinkGroupsTable_Object = MibTable
rtgDpnMidDelayNextHopLinkGroupsTable = _RtgDpnMidDelayNextHopLinkGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 228)
)
if mibBuilder.loadTexts:
    rtgDpnMidDelayNextHopLinkGroupsTable.setStatus("mandatory")
_RtgDpnMidDelayNextHopLinkGroupsEntry_Object = MibTableRow
rtgDpnMidDelayNextHopLinkGroupsEntry = _RtgDpnMidDelayNextHopLinkGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 228, 1)
)
rtgDpnMidDelayNextHopLinkGroupsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnMidIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnMidDelayNextHopLinkGroupsIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnMidDelayNextHopLinkGroupsEntry.setStatus("mandatory")


class _RtgDpnMidDelayNextHopLinkGroupsIndex_Type(Integer32):
    """Custom type rtgDpnMidDelayNextHopLinkGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RtgDpnMidDelayNextHopLinkGroupsIndex_Type.__name__ = "Integer32"
_RtgDpnMidDelayNextHopLinkGroupsIndex_Object = MibTableColumn
rtgDpnMidDelayNextHopLinkGroupsIndex = _RtgDpnMidDelayNextHopLinkGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 228, 1, 1),
    _RtgDpnMidDelayNextHopLinkGroupsIndex_Type()
)
rtgDpnMidDelayNextHopLinkGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnMidDelayNextHopLinkGroupsIndex.setStatus("mandatory")
_RtgDpnMidDelayNextHopLinkGroupsValue_Type = RowPointer
_RtgDpnMidDelayNextHopLinkGroupsValue_Object = MibTableColumn
rtgDpnMidDelayNextHopLinkGroupsValue = _RtgDpnMidDelayNextHopLinkGroupsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 228, 1, 2),
    _RtgDpnMidDelayNextHopLinkGroupsValue_Type()
)
rtgDpnMidDelayNextHopLinkGroupsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnMidDelayNextHopLinkGroupsValue.setStatus("mandatory")
_RtgDpnMidTputNextHopLinkGroupsTable_Object = MibTable
rtgDpnMidTputNextHopLinkGroupsTable = _RtgDpnMidTputNextHopLinkGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 229)
)
if mibBuilder.loadTexts:
    rtgDpnMidTputNextHopLinkGroupsTable.setStatus("mandatory")
_RtgDpnMidTputNextHopLinkGroupsEntry_Object = MibTableRow
rtgDpnMidTputNextHopLinkGroupsEntry = _RtgDpnMidTputNextHopLinkGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 229, 1)
)
rtgDpnMidTputNextHopLinkGroupsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnMidIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnMidTputNextHopLinkGroupsIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnMidTputNextHopLinkGroupsEntry.setStatus("mandatory")


class _RtgDpnMidTputNextHopLinkGroupsIndex_Type(Integer32):
    """Custom type rtgDpnMidTputNextHopLinkGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RtgDpnMidTputNextHopLinkGroupsIndex_Type.__name__ = "Integer32"
_RtgDpnMidTputNextHopLinkGroupsIndex_Object = MibTableColumn
rtgDpnMidTputNextHopLinkGroupsIndex = _RtgDpnMidTputNextHopLinkGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 229, 1, 1),
    _RtgDpnMidTputNextHopLinkGroupsIndex_Type()
)
rtgDpnMidTputNextHopLinkGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnMidTputNextHopLinkGroupsIndex.setStatus("mandatory")
_RtgDpnMidTputNextHopLinkGroupsValue_Type = RowPointer
_RtgDpnMidTputNextHopLinkGroupsValue_Object = MibTableColumn
rtgDpnMidTputNextHopLinkGroupsValue = _RtgDpnMidTputNextHopLinkGroupsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 229, 1, 2),
    _RtgDpnMidTputNextHopLinkGroupsValue_Type()
)
rtgDpnMidTputNextHopLinkGroupsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnMidTputNextHopLinkGroupsValue.setStatus("mandatory")
_RtgDpnMidDelayMetricTable_Object = MibTable
rtgDpnMidDelayMetricTable = _RtgDpnMidDelayMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 330)
)
if mibBuilder.loadTexts:
    rtgDpnMidDelayMetricTable.setStatus("mandatory")
_RtgDpnMidDelayMetricEntry_Object = MibTableRow
rtgDpnMidDelayMetricEntry = _RtgDpnMidDelayMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 330, 1)
)
rtgDpnMidDelayMetricEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnMidIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnMidDelayMetricIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnMidDelayMetricEntry.setStatus("mandatory")


class _RtgDpnMidDelayMetricIndex_Type(Integer32):
    """Custom type rtgDpnMidDelayMetricIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RtgDpnMidDelayMetricIndex_Type.__name__ = "Integer32"
_RtgDpnMidDelayMetricIndex_Object = MibTableColumn
rtgDpnMidDelayMetricIndex = _RtgDpnMidDelayMetricIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 330, 1, 1),
    _RtgDpnMidDelayMetricIndex_Type()
)
rtgDpnMidDelayMetricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnMidDelayMetricIndex.setStatus("mandatory")


class _RtgDpnMidDelayMetricValue_Type(Unsigned32):
    """Custom type rtgDpnMidDelayMetricValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RtgDpnMidDelayMetricValue_Type.__name__ = "Unsigned32"
_RtgDpnMidDelayMetricValue_Object = MibTableColumn
rtgDpnMidDelayMetricValue = _RtgDpnMidDelayMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 330, 1, 2),
    _RtgDpnMidDelayMetricValue_Type()
)
rtgDpnMidDelayMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnMidDelayMetricValue.setStatus("mandatory")
_RtgDpnMidTputMetricTable_Object = MibTable
rtgDpnMidTputMetricTable = _RtgDpnMidTputMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 331)
)
if mibBuilder.loadTexts:
    rtgDpnMidTputMetricTable.setStatus("mandatory")
_RtgDpnMidTputMetricEntry_Object = MibTableRow
rtgDpnMidTputMetricEntry = _RtgDpnMidTputMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 331, 1)
)
rtgDpnMidTputMetricEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnMidIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnMidTputMetricIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnMidTputMetricEntry.setStatus("mandatory")


class _RtgDpnMidTputMetricIndex_Type(Integer32):
    """Custom type rtgDpnMidTputMetricIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RtgDpnMidTputMetricIndex_Type.__name__ = "Integer32"
_RtgDpnMidTputMetricIndex_Object = MibTableColumn
rtgDpnMidTputMetricIndex = _RtgDpnMidTputMetricIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 331, 1, 1),
    _RtgDpnMidTputMetricIndex_Type()
)
rtgDpnMidTputMetricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnMidTputMetricIndex.setStatus("mandatory")


class _RtgDpnMidTputMetricValue_Type(Unsigned32):
    """Custom type rtgDpnMidTputMetricValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RtgDpnMidTputMetricValue_Type.__name__ = "Unsigned32"
_RtgDpnMidTputMetricValue_Object = MibTableColumn
rtgDpnMidTputMetricValue = _RtgDpnMidTputMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 331, 1, 2),
    _RtgDpnMidTputMetricValue_Type()
)
rtgDpnMidTputMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnMidTputMetricValue.setStatus("mandatory")
_RtgDpnMidDelayPathTrafficProportionsTable_Object = MibTable
rtgDpnMidDelayPathTrafficProportionsTable = _RtgDpnMidDelayPathTrafficProportionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 332)
)
if mibBuilder.loadTexts:
    rtgDpnMidDelayPathTrafficProportionsTable.setStatus("mandatory")
_RtgDpnMidDelayPathTrafficProportionsEntry_Object = MibTableRow
rtgDpnMidDelayPathTrafficProportionsEntry = _RtgDpnMidDelayPathTrafficProportionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 332, 1)
)
rtgDpnMidDelayPathTrafficProportionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnMidIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnMidDelayPathTrafficProportionsIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnMidDelayPathTrafficProportionsEntry.setStatus("mandatory")


class _RtgDpnMidDelayPathTrafficProportionsIndex_Type(Integer32):
    """Custom type rtgDpnMidDelayPathTrafficProportionsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RtgDpnMidDelayPathTrafficProportionsIndex_Type.__name__ = "Integer32"
_RtgDpnMidDelayPathTrafficProportionsIndex_Object = MibTableColumn
rtgDpnMidDelayPathTrafficProportionsIndex = _RtgDpnMidDelayPathTrafficProportionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 332, 1, 1),
    _RtgDpnMidDelayPathTrafficProportionsIndex_Type()
)
rtgDpnMidDelayPathTrafficProportionsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnMidDelayPathTrafficProportionsIndex.setStatus("mandatory")


class _RtgDpnMidDelayPathTrafficProportionsValue_Type(Unsigned32):
    """Custom type rtgDpnMidDelayPathTrafficProportionsValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RtgDpnMidDelayPathTrafficProportionsValue_Type.__name__ = "Unsigned32"
_RtgDpnMidDelayPathTrafficProportionsValue_Object = MibTableColumn
rtgDpnMidDelayPathTrafficProportionsValue = _RtgDpnMidDelayPathTrafficProportionsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 332, 1, 2),
    _RtgDpnMidDelayPathTrafficProportionsValue_Type()
)
rtgDpnMidDelayPathTrafficProportionsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnMidDelayPathTrafficProportionsValue.setStatus("mandatory")
_RtgDpnMidTputPathTrafficProportionsTable_Object = MibTable
rtgDpnMidTputPathTrafficProportionsTable = _RtgDpnMidTputPathTrafficProportionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 333)
)
if mibBuilder.loadTexts:
    rtgDpnMidTputPathTrafficProportionsTable.setStatus("mandatory")
_RtgDpnMidTputPathTrafficProportionsEntry_Object = MibTableRow
rtgDpnMidTputPathTrafficProportionsEntry = _RtgDpnMidTputPathTrafficProportionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 333, 1)
)
rtgDpnMidTputPathTrafficProportionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnMidIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnMidTputPathTrafficProportionsIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnMidTputPathTrafficProportionsEntry.setStatus("mandatory")


class _RtgDpnMidTputPathTrafficProportionsIndex_Type(Integer32):
    """Custom type rtgDpnMidTputPathTrafficProportionsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RtgDpnMidTputPathTrafficProportionsIndex_Type.__name__ = "Integer32"
_RtgDpnMidTputPathTrafficProportionsIndex_Object = MibTableColumn
rtgDpnMidTputPathTrafficProportionsIndex = _RtgDpnMidTputPathTrafficProportionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 333, 1, 1),
    _RtgDpnMidTputPathTrafficProportionsIndex_Type()
)
rtgDpnMidTputPathTrafficProportionsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnMidTputPathTrafficProportionsIndex.setStatus("mandatory")


class _RtgDpnMidTputPathTrafficProportionsValue_Type(Unsigned32):
    """Custom type rtgDpnMidTputPathTrafficProportionsValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RtgDpnMidTputPathTrafficProportionsValue_Type.__name__ = "Unsigned32"
_RtgDpnMidTputPathTrafficProportionsValue_Object = MibTableColumn
rtgDpnMidTputPathTrafficProportionsValue = _RtgDpnMidTputPathTrafficProportionsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 3, 333, 1, 2),
    _RtgDpnMidTputPathTrafficProportionsValue_Type()
)
rtgDpnMidTputPathTrafficProportionsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnMidTputPathTrafficProportionsValue.setStatus("mandatory")
_RtgDpnCs_ObjectIdentity = ObjectIdentity
rtgDpnCs = _RtgDpnCs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4)
)
_RtgDpnCsRowStatusTable_Object = MibTable
rtgDpnCsRowStatusTable = _RtgDpnCsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 1)
)
if mibBuilder.loadTexts:
    rtgDpnCsRowStatusTable.setStatus("mandatory")
_RtgDpnCsRowStatusEntry_Object = MibTableRow
rtgDpnCsRowStatusEntry = _RtgDpnCsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 1, 1)
)
rtgDpnCsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnCsIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnCsRowStatusEntry.setStatus("mandatory")
_RtgDpnCsRowStatus_Type = RowStatus
_RtgDpnCsRowStatus_Object = MibTableColumn
rtgDpnCsRowStatus = _RtgDpnCsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 1, 1, 1),
    _RtgDpnCsRowStatus_Type()
)
rtgDpnCsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnCsRowStatus.setStatus("mandatory")
_RtgDpnCsComponentName_Type = DisplayString
_RtgDpnCsComponentName_Object = MibTableColumn
rtgDpnCsComponentName = _RtgDpnCsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 1, 1, 2),
    _RtgDpnCsComponentName_Type()
)
rtgDpnCsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnCsComponentName.setStatus("mandatory")
_RtgDpnCsStorageType_Type = StorageType
_RtgDpnCsStorageType_Object = MibTableColumn
rtgDpnCsStorageType = _RtgDpnCsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 1, 1, 4),
    _RtgDpnCsStorageType_Type()
)
rtgDpnCsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnCsStorageType.setStatus("mandatory")


class _RtgDpnCsIndex_Type(Integer32):
    """Custom type rtgDpnCsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              6,
              7,
              8,
              10,
              11,
              12,
              14)
        )
    )
    namedValues = NamedValues(
        *(("crd", 5),
          ("dcr", 1),
          ("gdcr", 12),
          ("grman", 10),
          ("gscr", 11),
          ("lcr", 14),
          ("lnui", 6),
          ("npm", 8),
          ("nui", 4),
          ("scr", 7))
    )


_RtgDpnCsIndex_Type.__name__ = "Integer32"
_RtgDpnCsIndex_Object = MibTableColumn
rtgDpnCsIndex = _RtgDpnCsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 1, 1, 10),
    _RtgDpnCsIndex_Type()
)
rtgDpnCsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnCsIndex.setStatus("mandatory")
_RtgDpnCsDelayNextHopLinkGroupsTable_Object = MibTable
rtgDpnCsDelayNextHopLinkGroupsTable = _RtgDpnCsDelayNextHopLinkGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 230)
)
if mibBuilder.loadTexts:
    rtgDpnCsDelayNextHopLinkGroupsTable.setStatus("mandatory")
_RtgDpnCsDelayNextHopLinkGroupsEntry_Object = MibTableRow
rtgDpnCsDelayNextHopLinkGroupsEntry = _RtgDpnCsDelayNextHopLinkGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 230, 1)
)
rtgDpnCsDelayNextHopLinkGroupsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnCsIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnCsDelayNextHopLinkGroupsIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnCsDelayNextHopLinkGroupsEntry.setStatus("mandatory")


class _RtgDpnCsDelayNextHopLinkGroupsIndex_Type(Integer32):
    """Custom type rtgDpnCsDelayNextHopLinkGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RtgDpnCsDelayNextHopLinkGroupsIndex_Type.__name__ = "Integer32"
_RtgDpnCsDelayNextHopLinkGroupsIndex_Object = MibTableColumn
rtgDpnCsDelayNextHopLinkGroupsIndex = _RtgDpnCsDelayNextHopLinkGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 230, 1, 1),
    _RtgDpnCsDelayNextHopLinkGroupsIndex_Type()
)
rtgDpnCsDelayNextHopLinkGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnCsDelayNextHopLinkGroupsIndex.setStatus("mandatory")
_RtgDpnCsDelayNextHopLinkGroupsValue_Type = RowPointer
_RtgDpnCsDelayNextHopLinkGroupsValue_Object = MibTableColumn
rtgDpnCsDelayNextHopLinkGroupsValue = _RtgDpnCsDelayNextHopLinkGroupsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 230, 1, 2),
    _RtgDpnCsDelayNextHopLinkGroupsValue_Type()
)
rtgDpnCsDelayNextHopLinkGroupsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnCsDelayNextHopLinkGroupsValue.setStatus("mandatory")
_RtgDpnCsTputNextHopLinkGroupsTable_Object = MibTable
rtgDpnCsTputNextHopLinkGroupsTable = _RtgDpnCsTputNextHopLinkGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 231)
)
if mibBuilder.loadTexts:
    rtgDpnCsTputNextHopLinkGroupsTable.setStatus("mandatory")
_RtgDpnCsTputNextHopLinkGroupsEntry_Object = MibTableRow
rtgDpnCsTputNextHopLinkGroupsEntry = _RtgDpnCsTputNextHopLinkGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 231, 1)
)
rtgDpnCsTputNextHopLinkGroupsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnCsIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnCsTputNextHopLinkGroupsIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnCsTputNextHopLinkGroupsEntry.setStatus("mandatory")


class _RtgDpnCsTputNextHopLinkGroupsIndex_Type(Integer32):
    """Custom type rtgDpnCsTputNextHopLinkGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RtgDpnCsTputNextHopLinkGroupsIndex_Type.__name__ = "Integer32"
_RtgDpnCsTputNextHopLinkGroupsIndex_Object = MibTableColumn
rtgDpnCsTputNextHopLinkGroupsIndex = _RtgDpnCsTputNextHopLinkGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 231, 1, 1),
    _RtgDpnCsTputNextHopLinkGroupsIndex_Type()
)
rtgDpnCsTputNextHopLinkGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnCsTputNextHopLinkGroupsIndex.setStatus("mandatory")
_RtgDpnCsTputNextHopLinkGroupsValue_Type = RowPointer
_RtgDpnCsTputNextHopLinkGroupsValue_Object = MibTableColumn
rtgDpnCsTputNextHopLinkGroupsValue = _RtgDpnCsTputNextHopLinkGroupsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 231, 1, 2),
    _RtgDpnCsTputNextHopLinkGroupsValue_Type()
)
rtgDpnCsTputNextHopLinkGroupsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnCsTputNextHopLinkGroupsValue.setStatus("mandatory")
_RtgDpnCsDelayMetricTable_Object = MibTable
rtgDpnCsDelayMetricTable = _RtgDpnCsDelayMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 334)
)
if mibBuilder.loadTexts:
    rtgDpnCsDelayMetricTable.setStatus("mandatory")
_RtgDpnCsDelayMetricEntry_Object = MibTableRow
rtgDpnCsDelayMetricEntry = _RtgDpnCsDelayMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 334, 1)
)
rtgDpnCsDelayMetricEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnCsIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnCsDelayMetricIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnCsDelayMetricEntry.setStatus("mandatory")


class _RtgDpnCsDelayMetricIndex_Type(Integer32):
    """Custom type rtgDpnCsDelayMetricIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RtgDpnCsDelayMetricIndex_Type.__name__ = "Integer32"
_RtgDpnCsDelayMetricIndex_Object = MibTableColumn
rtgDpnCsDelayMetricIndex = _RtgDpnCsDelayMetricIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 334, 1, 1),
    _RtgDpnCsDelayMetricIndex_Type()
)
rtgDpnCsDelayMetricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnCsDelayMetricIndex.setStatus("mandatory")


class _RtgDpnCsDelayMetricValue_Type(Unsigned32):
    """Custom type rtgDpnCsDelayMetricValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RtgDpnCsDelayMetricValue_Type.__name__ = "Unsigned32"
_RtgDpnCsDelayMetricValue_Object = MibTableColumn
rtgDpnCsDelayMetricValue = _RtgDpnCsDelayMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 334, 1, 2),
    _RtgDpnCsDelayMetricValue_Type()
)
rtgDpnCsDelayMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnCsDelayMetricValue.setStatus("mandatory")
_RtgDpnCsTputMetricTable_Object = MibTable
rtgDpnCsTputMetricTable = _RtgDpnCsTputMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 335)
)
if mibBuilder.loadTexts:
    rtgDpnCsTputMetricTable.setStatus("mandatory")
_RtgDpnCsTputMetricEntry_Object = MibTableRow
rtgDpnCsTputMetricEntry = _RtgDpnCsTputMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 335, 1)
)
rtgDpnCsTputMetricEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnCsIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnCsTputMetricIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnCsTputMetricEntry.setStatus("mandatory")


class _RtgDpnCsTputMetricIndex_Type(Integer32):
    """Custom type rtgDpnCsTputMetricIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RtgDpnCsTputMetricIndex_Type.__name__ = "Integer32"
_RtgDpnCsTputMetricIndex_Object = MibTableColumn
rtgDpnCsTputMetricIndex = _RtgDpnCsTputMetricIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 335, 1, 1),
    _RtgDpnCsTputMetricIndex_Type()
)
rtgDpnCsTputMetricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnCsTputMetricIndex.setStatus("mandatory")


class _RtgDpnCsTputMetricValue_Type(Unsigned32):
    """Custom type rtgDpnCsTputMetricValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RtgDpnCsTputMetricValue_Type.__name__ = "Unsigned32"
_RtgDpnCsTputMetricValue_Object = MibTableColumn
rtgDpnCsTputMetricValue = _RtgDpnCsTputMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 335, 1, 2),
    _RtgDpnCsTputMetricValue_Type()
)
rtgDpnCsTputMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnCsTputMetricValue.setStatus("mandatory")
_RtgDpnCsDelayPathTrafficProportionsTable_Object = MibTable
rtgDpnCsDelayPathTrafficProportionsTable = _RtgDpnCsDelayPathTrafficProportionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 336)
)
if mibBuilder.loadTexts:
    rtgDpnCsDelayPathTrafficProportionsTable.setStatus("mandatory")
_RtgDpnCsDelayPathTrafficProportionsEntry_Object = MibTableRow
rtgDpnCsDelayPathTrafficProportionsEntry = _RtgDpnCsDelayPathTrafficProportionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 336, 1)
)
rtgDpnCsDelayPathTrafficProportionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnCsIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnCsDelayPathTrafficProportionsIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnCsDelayPathTrafficProportionsEntry.setStatus("mandatory")


class _RtgDpnCsDelayPathTrafficProportionsIndex_Type(Integer32):
    """Custom type rtgDpnCsDelayPathTrafficProportionsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RtgDpnCsDelayPathTrafficProportionsIndex_Type.__name__ = "Integer32"
_RtgDpnCsDelayPathTrafficProportionsIndex_Object = MibTableColumn
rtgDpnCsDelayPathTrafficProportionsIndex = _RtgDpnCsDelayPathTrafficProportionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 336, 1, 1),
    _RtgDpnCsDelayPathTrafficProportionsIndex_Type()
)
rtgDpnCsDelayPathTrafficProportionsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnCsDelayPathTrafficProportionsIndex.setStatus("mandatory")


class _RtgDpnCsDelayPathTrafficProportionsValue_Type(Unsigned32):
    """Custom type rtgDpnCsDelayPathTrafficProportionsValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RtgDpnCsDelayPathTrafficProportionsValue_Type.__name__ = "Unsigned32"
_RtgDpnCsDelayPathTrafficProportionsValue_Object = MibTableColumn
rtgDpnCsDelayPathTrafficProportionsValue = _RtgDpnCsDelayPathTrafficProportionsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 336, 1, 2),
    _RtgDpnCsDelayPathTrafficProportionsValue_Type()
)
rtgDpnCsDelayPathTrafficProportionsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnCsDelayPathTrafficProportionsValue.setStatus("mandatory")
_RtgDpnCsTputPathTrafficProportionsTable_Object = MibTable
rtgDpnCsTputPathTrafficProportionsTable = _RtgDpnCsTputPathTrafficProportionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 337)
)
if mibBuilder.loadTexts:
    rtgDpnCsTputPathTrafficProportionsTable.setStatus("mandatory")
_RtgDpnCsTputPathTrafficProportionsEntry_Object = MibTableRow
rtgDpnCsTputPathTrafficProportionsEntry = _RtgDpnCsTputPathTrafficProportionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 337, 1)
)
rtgDpnCsTputPathTrafficProportionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnCsIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnCsTputPathTrafficProportionsIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnCsTputPathTrafficProportionsEntry.setStatus("mandatory")


class _RtgDpnCsTputPathTrafficProportionsIndex_Type(Integer32):
    """Custom type rtgDpnCsTputPathTrafficProportionsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RtgDpnCsTputPathTrafficProportionsIndex_Type.__name__ = "Integer32"
_RtgDpnCsTputPathTrafficProportionsIndex_Object = MibTableColumn
rtgDpnCsTputPathTrafficProportionsIndex = _RtgDpnCsTputPathTrafficProportionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 337, 1, 1),
    _RtgDpnCsTputPathTrafficProportionsIndex_Type()
)
rtgDpnCsTputPathTrafficProportionsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnCsTputPathTrafficProportionsIndex.setStatus("mandatory")


class _RtgDpnCsTputPathTrafficProportionsValue_Type(Unsigned32):
    """Custom type rtgDpnCsTputPathTrafficProportionsValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RtgDpnCsTputPathTrafficProportionsValue_Type.__name__ = "Unsigned32"
_RtgDpnCsTputPathTrafficProportionsValue_Object = MibTableColumn
rtgDpnCsTputPathTrafficProportionsValue = _RtgDpnCsTputPathTrafficProportionsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 4, 337, 1, 2),
    _RtgDpnCsTputPathTrafficProportionsValue_Type()
)
rtgDpnCsTputPathTrafficProportionsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnCsTputPathTrafficProportionsValue.setStatus("mandatory")
_RtgDpnLg_ObjectIdentity = ObjectIdentity
rtgDpnLg = _RtgDpnLg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 5)
)
_RtgDpnLgRowStatusTable_Object = MibTable
rtgDpnLgRowStatusTable = _RtgDpnLgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 5, 1)
)
if mibBuilder.loadTexts:
    rtgDpnLgRowStatusTable.setStatus("mandatory")
_RtgDpnLgRowStatusEntry_Object = MibTableRow
rtgDpnLgRowStatusEntry = _RtgDpnLgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 5, 1, 1)
)
rtgDpnLgRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnLgIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnLgRowStatusEntry.setStatus("mandatory")
_RtgDpnLgRowStatus_Type = RowStatus
_RtgDpnLgRowStatus_Object = MibTableColumn
rtgDpnLgRowStatus = _RtgDpnLgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 5, 1, 1, 1),
    _RtgDpnLgRowStatus_Type()
)
rtgDpnLgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnLgRowStatus.setStatus("mandatory")
_RtgDpnLgComponentName_Type = DisplayString
_RtgDpnLgComponentName_Object = MibTableColumn
rtgDpnLgComponentName = _RtgDpnLgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 5, 1, 1, 2),
    _RtgDpnLgComponentName_Type()
)
rtgDpnLgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnLgComponentName.setStatus("mandatory")
_RtgDpnLgStorageType_Type = StorageType
_RtgDpnLgStorageType_Object = MibTableColumn
rtgDpnLgStorageType = _RtgDpnLgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 5, 1, 1, 4),
    _RtgDpnLgStorageType_Type()
)
rtgDpnLgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnLgStorageType.setStatus("mandatory")


class _RtgDpnLgIndex_Type(AsciiStringIndex):
    """Custom type rtgDpnLgIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_RtgDpnLgIndex_Type.__name__ = "AsciiStringIndex"
_RtgDpnLgIndex_Object = MibTableColumn
rtgDpnLgIndex = _RtgDpnLgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 5, 1, 1, 10),
    _RtgDpnLgIndex_Type()
)
rtgDpnLgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnLgIndex.setStatus("mandatory")
_RtgDpnLgOperTable_Object = MibTable
rtgDpnLgOperTable = _RtgDpnLgOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 5, 3)
)
if mibBuilder.loadTexts:
    rtgDpnLgOperTable.setStatus("mandatory")
_RtgDpnLgOperEntry_Object = MibTableRow
rtgDpnLgOperEntry = _RtgDpnLgOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 5, 3, 1)
)
rtgDpnLgOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnLgIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnLgOperEntry.setStatus("mandatory")


class _RtgDpnLgFarEndType_Type(Integer32):
    """Custom type rtgDpnLgFarEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("am", 2),
          ("em", 0),
          ("rm", 1))
    )


_RtgDpnLgFarEndType_Type.__name__ = "Integer32"
_RtgDpnLgFarEndType_Object = MibTableColumn
rtgDpnLgFarEndType = _RtgDpnLgFarEndType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 5, 3, 1, 1),
    _RtgDpnLgFarEndType_Type()
)
rtgDpnLgFarEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnLgFarEndType.setStatus("mandatory")


class _RtgDpnLgFarEndRid_Type(Unsigned32):
    """Custom type rtgDpnLgFarEndRid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 126),
    )


_RtgDpnLgFarEndRid_Type.__name__ = "Unsigned32"
_RtgDpnLgFarEndRid_Object = MibTableColumn
rtgDpnLgFarEndRid = _RtgDpnLgFarEndRid_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 5, 3, 1, 2),
    _RtgDpnLgFarEndRid_Type()
)
rtgDpnLgFarEndRid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnLgFarEndRid.setStatus("mandatory")


class _RtgDpnLgFarEndMid_Type(Unsigned32):
    """Custom type rtgDpnLgFarEndMid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1910),
    )


_RtgDpnLgFarEndMid_Type.__name__ = "Unsigned32"
_RtgDpnLgFarEndMid_Object = MibTableColumn
rtgDpnLgFarEndMid = _RtgDpnLgFarEndMid_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 5, 3, 1, 3),
    _RtgDpnLgFarEndMid_Type()
)
rtgDpnLgFarEndMid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnLgFarEndMid.setStatus("mandatory")


class _RtgDpnLgDelayMetric_Type(Unsigned32):
    """Custom type rtgDpnLgDelayMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RtgDpnLgDelayMetric_Type.__name__ = "Unsigned32"
_RtgDpnLgDelayMetric_Object = MibTableColumn
rtgDpnLgDelayMetric = _RtgDpnLgDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 5, 3, 1, 4),
    _RtgDpnLgDelayMetric_Type()
)
rtgDpnLgDelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnLgDelayMetric.setStatus("mandatory")


class _RtgDpnLgTputMetric_Type(Unsigned32):
    """Custom type rtgDpnLgTputMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RtgDpnLgTputMetric_Type.__name__ = "Unsigned32"
_RtgDpnLgTputMetric_Object = MibTableColumn
rtgDpnLgTputMetric = _RtgDpnLgTputMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 5, 3, 1, 5),
    _RtgDpnLgTputMetric_Type()
)
rtgDpnLgTputMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnLgTputMetric.setStatus("mandatory")
_RtgDpnLpStats_ObjectIdentity = ObjectIdentity
rtgDpnLpStats = _RtgDpnLpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 6)
)
_RtgDpnLpStatsRowStatusTable_Object = MibTable
rtgDpnLpStatsRowStatusTable = _RtgDpnLpStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 6, 1)
)
if mibBuilder.loadTexts:
    rtgDpnLpStatsRowStatusTable.setStatus("mandatory")
_RtgDpnLpStatsRowStatusEntry_Object = MibTableRow
rtgDpnLpStatsRowStatusEntry = _RtgDpnLpStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 6, 1, 1)
)
rtgDpnLpStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnLpStatsIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnLpStatsRowStatusEntry.setStatus("mandatory")
_RtgDpnLpStatsRowStatus_Type = RowStatus
_RtgDpnLpStatsRowStatus_Object = MibTableColumn
rtgDpnLpStatsRowStatus = _RtgDpnLpStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 6, 1, 1, 1),
    _RtgDpnLpStatsRowStatus_Type()
)
rtgDpnLpStatsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnLpStatsRowStatus.setStatus("mandatory")
_RtgDpnLpStatsComponentName_Type = DisplayString
_RtgDpnLpStatsComponentName_Object = MibTableColumn
rtgDpnLpStatsComponentName = _RtgDpnLpStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 6, 1, 1, 2),
    _RtgDpnLpStatsComponentName_Type()
)
rtgDpnLpStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnLpStatsComponentName.setStatus("mandatory")
_RtgDpnLpStatsStorageType_Type = StorageType
_RtgDpnLpStatsStorageType_Object = MibTableColumn
rtgDpnLpStatsStorageType = _RtgDpnLpStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 6, 1, 1, 4),
    _RtgDpnLpStatsStorageType_Type()
)
rtgDpnLpStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnLpStatsStorageType.setStatus("mandatory")


class _RtgDpnLpStatsIndex_Type(Integer32):
    """Custom type rtgDpnLpStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RtgDpnLpStatsIndex_Type.__name__ = "Integer32"
_RtgDpnLpStatsIndex_Object = MibTableColumn
rtgDpnLpStatsIndex = _RtgDpnLpStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 6, 1, 1, 10),
    _RtgDpnLpStatsIndex_Type()
)
rtgDpnLpStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnLpStatsIndex.setStatus("mandatory")
_RtgDpnLpStatsFwdStatsTable_Object = MibTable
rtgDpnLpStatsFwdStatsTable = _RtgDpnLpStatsFwdStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 6, 10)
)
if mibBuilder.loadTexts:
    rtgDpnLpStatsFwdStatsTable.setStatus("mandatory")
_RtgDpnLpStatsFwdStatsEntry_Object = MibTableRow
rtgDpnLpStatsFwdStatsEntry = _RtgDpnLpStatsFwdStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 6, 10, 1)
)
rtgDpnLpStatsFwdStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnLpStatsIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnLpStatsFwdStatsEntry.setStatus("mandatory")
_RtgDpnLpStatsTotalPackets_Type = PassportCounter64
_RtgDpnLpStatsTotalPackets_Object = MibTableColumn
rtgDpnLpStatsTotalPackets = _RtgDpnLpStatsTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 6, 10, 1, 1),
    _RtgDpnLpStatsTotalPackets_Type()
)
rtgDpnLpStatsTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnLpStatsTotalPackets.setStatus("mandatory")
_RtgDpnLpStatsThroughputPackets_Type = PassportCounter64
_RtgDpnLpStatsThroughputPackets_Object = MibTableColumn
rtgDpnLpStatsThroughputPackets = _RtgDpnLpStatsThroughputPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 6, 10, 1, 2),
    _RtgDpnLpStatsThroughputPackets_Type()
)
rtgDpnLpStatsThroughputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnLpStatsThroughputPackets.setStatus("mandatory")
_RtgDpnLpStatsDelayPackets_Type = PassportCounter64
_RtgDpnLpStatsDelayPackets_Object = MibTableColumn
rtgDpnLpStatsDelayPackets = _RtgDpnLpStatsDelayPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 6, 10, 1, 3),
    _RtgDpnLpStatsDelayPackets_Type()
)
rtgDpnLpStatsDelayPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnLpStatsDelayPackets.setStatus("mandatory")
_RtgDpnLpStatsNormalReliabilityPackets_Type = PassportCounter64
_RtgDpnLpStatsNormalReliabilityPackets_Object = MibTableColumn
rtgDpnLpStatsNormalReliabilityPackets = _RtgDpnLpStatsNormalReliabilityPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 6, 10, 1, 4),
    _RtgDpnLpStatsNormalReliabilityPackets_Type()
)
rtgDpnLpStatsNormalReliabilityPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnLpStatsNormalReliabilityPackets.setStatus("mandatory")
_RtgDpnLpStatsHighReliabilityPackets_Type = PassportCounter64
_RtgDpnLpStatsHighReliabilityPackets_Object = MibTableColumn
rtgDpnLpStatsHighReliabilityPackets = _RtgDpnLpStatsHighReliabilityPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 6, 10, 1, 5),
    _RtgDpnLpStatsHighReliabilityPackets_Type()
)
rtgDpnLpStatsHighReliabilityPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnLpStatsHighReliabilityPackets.setStatus("mandatory")
_RtgDpnLpStatsDiscardNoRoute_Type = PassportCounter64
_RtgDpnLpStatsDiscardNoRoute_Object = MibTableColumn
rtgDpnLpStatsDiscardNoRoute = _RtgDpnLpStatsDiscardNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 6, 10, 1, 6),
    _RtgDpnLpStatsDiscardNoRoute_Type()
)
rtgDpnLpStatsDiscardNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnLpStatsDiscardNoRoute.setStatus("mandatory")
_RtgDpnLpStatsInterruptingPackets_Type = PassportCounter64
_RtgDpnLpStatsInterruptingPackets_Object = MibTableColumn
rtgDpnLpStatsInterruptingPackets = _RtgDpnLpStatsInterruptingPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 6, 10, 1, 7),
    _RtgDpnLpStatsInterruptingPackets_Type()
)
rtgDpnLpStatsInterruptingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnLpStatsInterruptingPackets.setStatus("mandatory")
_RtgDpnLpStatsDiscardLpCongested_Type = PassportCounter64
_RtgDpnLpStatsDiscardLpCongested_Object = MibTableColumn
rtgDpnLpStatsDiscardLpCongested = _RtgDpnLpStatsDiscardLpCongested_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 6, 10, 1, 8),
    _RtgDpnLpStatsDiscardLpCongested_Type()
)
rtgDpnLpStatsDiscardLpCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnLpStatsDiscardLpCongested.setStatus("mandatory")
_RtgDpnRidFilter_ObjectIdentity = ObjectIdentity
rtgDpnRidFilter = _RtgDpnRidFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 7)
)
_RtgDpnRidFilterRowStatusTable_Object = MibTable
rtgDpnRidFilterRowStatusTable = _RtgDpnRidFilterRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 7, 1)
)
if mibBuilder.loadTexts:
    rtgDpnRidFilterRowStatusTable.setStatus("mandatory")
_RtgDpnRidFilterRowStatusEntry_Object = MibTableRow
rtgDpnRidFilterRowStatusEntry = _RtgDpnRidFilterRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 7, 1, 1)
)
rtgDpnRidFilterRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnRidFilterIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnRidFilterRowStatusEntry.setStatus("mandatory")
_RtgDpnRidFilterRowStatus_Type = RowStatus
_RtgDpnRidFilterRowStatus_Object = MibTableColumn
rtgDpnRidFilterRowStatus = _RtgDpnRidFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 7, 1, 1, 1),
    _RtgDpnRidFilterRowStatus_Type()
)
rtgDpnRidFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgDpnRidFilterRowStatus.setStatus("mandatory")
_RtgDpnRidFilterComponentName_Type = DisplayString
_RtgDpnRidFilterComponentName_Object = MibTableColumn
rtgDpnRidFilterComponentName = _RtgDpnRidFilterComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 7, 1, 1, 2),
    _RtgDpnRidFilterComponentName_Type()
)
rtgDpnRidFilterComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnRidFilterComponentName.setStatus("mandatory")
_RtgDpnRidFilterStorageType_Type = StorageType
_RtgDpnRidFilterStorageType_Object = MibTableColumn
rtgDpnRidFilterStorageType = _RtgDpnRidFilterStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 7, 1, 1, 4),
    _RtgDpnRidFilterStorageType_Type()
)
rtgDpnRidFilterStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnRidFilterStorageType.setStatus("mandatory")


class _RtgDpnRidFilterIndex_Type(Integer32):
    """Custom type rtgDpnRidFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 126),
    )


_RtgDpnRidFilterIndex_Type.__name__ = "Integer32"
_RtgDpnRidFilterIndex_Object = MibTableColumn
rtgDpnRidFilterIndex = _RtgDpnRidFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 7, 1, 1, 10),
    _RtgDpnRidFilterIndex_Type()
)
rtgDpnRidFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnRidFilterIndex.setStatus("mandatory")
_RtgDpnRidFilterImportRidListTable_Object = MibTable
rtgDpnRidFilterImportRidListTable = _RtgDpnRidFilterImportRidListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 7, 303)
)
if mibBuilder.loadTexts:
    rtgDpnRidFilterImportRidListTable.setStatus("mandatory")
_RtgDpnRidFilterImportRidListEntry_Object = MibTableRow
rtgDpnRidFilterImportRidListEntry = _RtgDpnRidFilterImportRidListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 7, 303, 1)
)
rtgDpnRidFilterImportRidListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnRidFilterIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnRidFilterImportRidListValue"),
)
if mibBuilder.loadTexts:
    rtgDpnRidFilterImportRidListEntry.setStatus("mandatory")


class _RtgDpnRidFilterImportRidListValue_Type(Integer32):
    """Custom type rtgDpnRidFilterImportRidListValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_RtgDpnRidFilterImportRidListValue_Type.__name__ = "Integer32"
_RtgDpnRidFilterImportRidListValue_Object = MibTableColumn
rtgDpnRidFilterImportRidListValue = _RtgDpnRidFilterImportRidListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 7, 303, 1, 1),
    _RtgDpnRidFilterImportRidListValue_Type()
)
rtgDpnRidFilterImportRidListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgDpnRidFilterImportRidListValue.setStatus("mandatory")
_RtgDpnRidFilterImportRidListRowStatus_Type = RowStatus
_RtgDpnRidFilterImportRidListRowStatus_Object = MibTableColumn
rtgDpnRidFilterImportRidListRowStatus = _RtgDpnRidFilterImportRidListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 7, 303, 1, 2),
    _RtgDpnRidFilterImportRidListRowStatus_Type()
)
rtgDpnRidFilterImportRidListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    rtgDpnRidFilterImportRidListRowStatus.setStatus("mandatory")
_RtgDpnRidFilterExportRidListTable_Object = MibTable
rtgDpnRidFilterExportRidListTable = _RtgDpnRidFilterExportRidListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 7, 304)
)
if mibBuilder.loadTexts:
    rtgDpnRidFilterExportRidListTable.setStatus("mandatory")
_RtgDpnRidFilterExportRidListEntry_Object = MibTableRow
rtgDpnRidFilterExportRidListEntry = _RtgDpnRidFilterExportRidListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 7, 304, 1)
)
rtgDpnRidFilterExportRidListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnRidFilterIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnRidFilterExportRidListValue"),
)
if mibBuilder.loadTexts:
    rtgDpnRidFilterExportRidListEntry.setStatus("mandatory")


class _RtgDpnRidFilterExportRidListValue_Type(Integer32):
    """Custom type rtgDpnRidFilterExportRidListValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_RtgDpnRidFilterExportRidListValue_Type.__name__ = "Integer32"
_RtgDpnRidFilterExportRidListValue_Object = MibTableColumn
rtgDpnRidFilterExportRidListValue = _RtgDpnRidFilterExportRidListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 7, 304, 1, 1),
    _RtgDpnRidFilterExportRidListValue_Type()
)
rtgDpnRidFilterExportRidListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgDpnRidFilterExportRidListValue.setStatus("mandatory")
_RtgDpnRidFilterExportRidListRowStatus_Type = RowStatus
_RtgDpnRidFilterExportRidListRowStatus_Object = MibTableColumn
rtgDpnRidFilterExportRidListRowStatus = _RtgDpnRidFilterExportRidListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 7, 304, 1, 2),
    _RtgDpnRidFilterExportRidListRowStatus_Type()
)
rtgDpnRidFilterExportRidListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    rtgDpnRidFilterExportRidListRowStatus.setStatus("mandatory")
_RtgDpnProvTable_Object = MibTable
rtgDpnProvTable = _RtgDpnProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 11)
)
if mibBuilder.loadTexts:
    rtgDpnProvTable.setStatus("mandatory")
_RtgDpnProvEntry_Object = MibTableRow
rtgDpnProvEntry = _RtgDpnProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 11, 1)
)
rtgDpnProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnProvEntry.setStatus("mandatory")


class _RtgDpnLogicalNetworkNumber_Type(Unsigned32):
    """Custom type rtgDpnLogicalNetworkNumber based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_RtgDpnLogicalNetworkNumber_Type.__name__ = "Unsigned32"
_RtgDpnLogicalNetworkNumber_Object = MibTableColumn
rtgDpnLogicalNetworkNumber = _RtgDpnLogicalNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 11, 1, 1),
    _RtgDpnLogicalNetworkNumber_Type()
)
rtgDpnLogicalNetworkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnLogicalNetworkNumber.setStatus("mandatory")


class _RtgDpnRoutingId_Type(Unsigned32):
    """Custom type rtgDpnRoutingId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 126),
    )


_RtgDpnRoutingId_Type.__name__ = "Unsigned32"
_RtgDpnRoutingId_Object = MibTableColumn
rtgDpnRoutingId = _RtgDpnRoutingId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 11, 1, 2),
    _RtgDpnRoutingId_Type()
)
rtgDpnRoutingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgDpnRoutingId.setStatus("mandatory")


class _RtgDpnModuleId_Type(Unsigned32):
    """Custom type rtgDpnModuleId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1909),
    )


_RtgDpnModuleId_Type.__name__ = "Unsigned32"
_RtgDpnModuleId_Object = MibTableColumn
rtgDpnModuleId = _RtgDpnModuleId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 11, 1, 3),
    _RtgDpnModuleId_Type()
)
rtgDpnModuleId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgDpnModuleId.setStatus("mandatory")


class _RtgDpnDelayMetricCutOff_Type(Unsigned32):
    """Custom type rtgDpnDelayMetricCutOff based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 250),
    )


_RtgDpnDelayMetricCutOff_Type.__name__ = "Unsigned32"
_RtgDpnDelayMetricCutOff_Object = MibTableColumn
rtgDpnDelayMetricCutOff = _RtgDpnDelayMetricCutOff_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 11, 1, 4),
    _RtgDpnDelayMetricCutOff_Type()
)
rtgDpnDelayMetricCutOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgDpnDelayMetricCutOff.setStatus("mandatory")


class _RtgDpnThroughputMetricCutOff_Type(Unsigned32):
    """Custom type rtgDpnThroughputMetricCutOff based on Unsigned32"""
    defaultValue = 245

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 245),
    )


_RtgDpnThroughputMetricCutOff_Type.__name__ = "Unsigned32"
_RtgDpnThroughputMetricCutOff_Object = MibTableColumn
rtgDpnThroughputMetricCutOff = _RtgDpnThroughputMetricCutOff_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 11, 1, 5),
    _RtgDpnThroughputMetricCutOff_Type()
)
rtgDpnThroughputMetricCutOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgDpnThroughputMetricCutOff.setStatus("mandatory")


class _RtgDpnForwardingPolicy_Type(Integer32):
    """Custom type rtgDpnForwardingPolicy based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loadshare", 1),
          ("loadspread", 0),
          ("loadspreadFast", 2))
    )


_RtgDpnForwardingPolicy_Type.__name__ = "Integer32"
_RtgDpnForwardingPolicy_Object = MibTableColumn
rtgDpnForwardingPolicy = _RtgDpnForwardingPolicy_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 11, 1, 6),
    _RtgDpnForwardingPolicy_Type()
)
rtgDpnForwardingPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgDpnForwardingPolicy.setStatus("mandatory")


class _RtgDpnDelayMetricRangeBoundary_Type(Unsigned32):
    """Custom type rtgDpnDelayMetricRangeBoundary based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RtgDpnDelayMetricRangeBoundary_Type.__name__ = "Unsigned32"
_RtgDpnDelayMetricRangeBoundary_Object = MibTableColumn
rtgDpnDelayMetricRangeBoundary = _RtgDpnDelayMetricRangeBoundary_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 11, 1, 7),
    _RtgDpnDelayMetricRangeBoundary_Type()
)
rtgDpnDelayMetricRangeBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgDpnDelayMetricRangeBoundary.setStatus("mandatory")


class _RtgDpnTputMetricRangeBoundary_Type(Unsigned32):
    """Custom type rtgDpnTputMetricRangeBoundary based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RtgDpnTputMetricRangeBoundary_Type.__name__ = "Unsigned32"
_RtgDpnTputMetricRangeBoundary_Object = MibTableColumn
rtgDpnTputMetricRangeBoundary = _RtgDpnTputMetricRangeBoundary_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 11, 1, 8),
    _RtgDpnTputMetricRangeBoundary_Type()
)
rtgDpnTputMetricRangeBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgDpnTputMetricRangeBoundary.setStatus("mandatory")
_RtgDpnConStatsTable_Object = MibTable
rtgDpnConStatsTable = _RtgDpnConStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 13)
)
if mibBuilder.loadTexts:
    rtgDpnConStatsTable.setStatus("mandatory")
_RtgDpnConStatsEntry_Object = MibTableRow
rtgDpnConStatsEntry = _RtgDpnConStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 13, 1)
)
rtgDpnConStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnConStatsEntry.setStatus("mandatory")


class _RtgDpnControlPktTx_Type(Unsigned32):
    """Custom type rtgDpnControlPktTx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RtgDpnControlPktTx_Type.__name__ = "Unsigned32"
_RtgDpnControlPktTx_Object = MibTableColumn
rtgDpnControlPktTx = _RtgDpnControlPktTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 13, 1, 1),
    _RtgDpnControlPktTx_Type()
)
rtgDpnControlPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnControlPktTx.setStatus("mandatory")


class _RtgDpnControlPktRx_Type(Unsigned32):
    """Custom type rtgDpnControlPktRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RtgDpnControlPktRx_Type.__name__ = "Unsigned32"
_RtgDpnControlPktRx_Object = MibTableColumn
rtgDpnControlPktRx = _RtgDpnControlPktRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 13, 1, 2),
    _RtgDpnControlPktRx_Type()
)
rtgDpnControlPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnControlPktRx.setStatus("mandatory")


class _RtgDpnControlBytesTx_Type(Unsigned32):
    """Custom type rtgDpnControlBytesTx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RtgDpnControlBytesTx_Type.__name__ = "Unsigned32"
_RtgDpnControlBytesTx_Object = MibTableColumn
rtgDpnControlBytesTx = _RtgDpnControlBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 13, 1, 3),
    _RtgDpnControlBytesTx_Type()
)
rtgDpnControlBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnControlBytesTx.setStatus("mandatory")


class _RtgDpnControlBytesRx_Type(Unsigned32):
    """Custom type rtgDpnControlBytesRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RtgDpnControlBytesRx_Type.__name__ = "Unsigned32"
_RtgDpnControlBytesRx_Object = MibTableColumn
rtgDpnControlBytesRx = _RtgDpnControlBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 13, 1, 4),
    _RtgDpnControlBytesRx_Type()
)
rtgDpnControlBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnControlBytesRx.setStatus("mandatory")


class _RtgDpnOutOfSequencePkt_Type(Unsigned32):
    """Custom type rtgDpnOutOfSequencePkt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RtgDpnOutOfSequencePkt_Type.__name__ = "Unsigned32"
_RtgDpnOutOfSequencePkt_Object = MibTableColumn
rtgDpnOutOfSequencePkt = _RtgDpnOutOfSequencePkt_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 13, 1, 5),
    _RtgDpnOutOfSequencePkt_Type()
)
rtgDpnOutOfSequencePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnOutOfSequencePkt.setStatus("mandatory")
_RtgDpnFwdStatsTable_Object = MibTable
rtgDpnFwdStatsTable = _RtgDpnFwdStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 14)
)
if mibBuilder.loadTexts:
    rtgDpnFwdStatsTable.setStatus("mandatory")
_RtgDpnFwdStatsEntry_Object = MibTableRow
rtgDpnFwdStatsEntry = _RtgDpnFwdStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 14, 1)
)
rtgDpnFwdStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnFwdStatsEntry.setStatus("mandatory")
_RtgDpnTotalPackets_Type = PassportCounter64
_RtgDpnTotalPackets_Object = MibTableColumn
rtgDpnTotalPackets = _RtgDpnTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 14, 1, 1),
    _RtgDpnTotalPackets_Type()
)
rtgDpnTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnTotalPackets.setStatus("mandatory")
_RtgDpnThroughputPackets_Type = PassportCounter64
_RtgDpnThroughputPackets_Object = MibTableColumn
rtgDpnThroughputPackets = _RtgDpnThroughputPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 14, 1, 2),
    _RtgDpnThroughputPackets_Type()
)
rtgDpnThroughputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnThroughputPackets.setStatus("mandatory")
_RtgDpnDelayPackets_Type = PassportCounter64
_RtgDpnDelayPackets_Object = MibTableColumn
rtgDpnDelayPackets = _RtgDpnDelayPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 14, 1, 3),
    _RtgDpnDelayPackets_Type()
)
rtgDpnDelayPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnDelayPackets.setStatus("mandatory")
_RtgDpnNormalReliabilityPackets_Type = PassportCounter64
_RtgDpnNormalReliabilityPackets_Object = MibTableColumn
rtgDpnNormalReliabilityPackets = _RtgDpnNormalReliabilityPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 14, 1, 4),
    _RtgDpnNormalReliabilityPackets_Type()
)
rtgDpnNormalReliabilityPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnNormalReliabilityPackets.setStatus("mandatory")
_RtgDpnHighReliabilityPackets_Type = PassportCounter64
_RtgDpnHighReliabilityPackets_Object = MibTableColumn
rtgDpnHighReliabilityPackets = _RtgDpnHighReliabilityPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 14, 1, 5),
    _RtgDpnHighReliabilityPackets_Type()
)
rtgDpnHighReliabilityPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnHighReliabilityPackets.setStatus("mandatory")
_RtgDpnDiscardNoRoute_Type = PassportCounter64
_RtgDpnDiscardNoRoute_Object = MibTableColumn
rtgDpnDiscardNoRoute = _RtgDpnDiscardNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 14, 1, 6),
    _RtgDpnDiscardNoRoute_Type()
)
rtgDpnDiscardNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnDiscardNoRoute.setStatus("mandatory")
_RtgDpnInterruptingPackets_Type = PassportCounter64
_RtgDpnInterruptingPackets_Object = MibTableColumn
rtgDpnInterruptingPackets = _RtgDpnInterruptingPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 14, 1, 7),
    _RtgDpnInterruptingPackets_Type()
)
rtgDpnInterruptingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnInterruptingPackets.setStatus("mandatory")
_RtgDpnDiscardLpCongested_Type = PassportCounter64
_RtgDpnDiscardLpCongested_Object = MibTableColumn
rtgDpnDiscardLpCongested = _RtgDpnDiscardLpCongested_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 14, 1, 8),
    _RtgDpnDiscardLpCongested_Type()
)
rtgDpnDiscardLpCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnDiscardLpCongested.setStatus("mandatory")
_RtgDpnCallServerModuleRidsTable_Object = MibTable
rtgDpnCallServerModuleRidsTable = _RtgDpnCallServerModuleRidsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 232)
)
if mibBuilder.loadTexts:
    rtgDpnCallServerModuleRidsTable.setStatus("mandatory")
_RtgDpnCallServerModuleRidsEntry_Object = MibTableRow
rtgDpnCallServerModuleRidsEntry = _RtgDpnCallServerModuleRidsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 232, 1)
)
rtgDpnCallServerModuleRidsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnCallServerModuleRidsValue"),
)
if mibBuilder.loadTexts:
    rtgDpnCallServerModuleRidsEntry.setStatus("mandatory")


class _RtgDpnCallServerModuleRidsValue_Type(Integer32):
    """Custom type rtgDpnCallServerModuleRidsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 126),
    )


_RtgDpnCallServerModuleRidsValue_Type.__name__ = "Integer32"
_RtgDpnCallServerModuleRidsValue_Object = MibTableColumn
rtgDpnCallServerModuleRidsValue = _RtgDpnCallServerModuleRidsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 232, 1, 1),
    _RtgDpnCallServerModuleRidsValue_Type()
)
rtgDpnCallServerModuleRidsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnCallServerModuleRidsValue.setStatus("mandatory")
_RtgDpnSubnetMidsTable_Object = MibTable
rtgDpnSubnetMidsTable = _RtgDpnSubnetMidsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 233)
)
if mibBuilder.loadTexts:
    rtgDpnSubnetMidsTable.setStatus("mandatory")
_RtgDpnSubnetMidsEntry_Object = MibTableRow
rtgDpnSubnetMidsEntry = _RtgDpnSubnetMidsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 233, 1)
)
rtgDpnSubnetMidsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnSubnetMidsValue"),
)
if mibBuilder.loadTexts:
    rtgDpnSubnetMidsEntry.setStatus("mandatory")
_RtgDpnSubnetMidsValue_Type = RowPointer
_RtgDpnSubnetMidsValue_Object = MibTableColumn
rtgDpnSubnetMidsValue = _RtgDpnSubnetMidsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 233, 1, 1),
    _RtgDpnSubnetMidsValue_Type()
)
rtgDpnSubnetMidsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgDpnSubnetMidsValue.setStatus("mandatory")
_RtgDpnVarianceTable_Object = MibTable
rtgDpnVarianceTable = _RtgDpnVarianceTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 343)
)
if mibBuilder.loadTexts:
    rtgDpnVarianceTable.setStatus("mandatory")
_RtgDpnVarianceEntry_Object = MibTableRow
rtgDpnVarianceEntry = _RtgDpnVarianceEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 343, 1)
)
rtgDpnVarianceEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnVarianceCosIndex"),
    (0, "Nortel-Magellan-Passport-DpnRoutingMIB", "rtgDpnVarianceMetricRangeIndex"),
)
if mibBuilder.loadTexts:
    rtgDpnVarianceEntry.setStatus("mandatory")


class _RtgDpnVarianceCosIndex_Type(Integer32):
    """Custom type rtgDpnVarianceCosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("delay", 0),
          ("throughput", 1))
    )


_RtgDpnVarianceCosIndex_Type.__name__ = "Integer32"
_RtgDpnVarianceCosIndex_Object = MibTableColumn
rtgDpnVarianceCosIndex = _RtgDpnVarianceCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 343, 1, 1),
    _RtgDpnVarianceCosIndex_Type()
)
rtgDpnVarianceCosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnVarianceCosIndex.setStatus("mandatory")


class _RtgDpnVarianceMetricRangeIndex_Type(Integer32):
    """Custom type rtgDpnVarianceMetricRangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_RtgDpnVarianceMetricRangeIndex_Type.__name__ = "Integer32"
_RtgDpnVarianceMetricRangeIndex_Object = MibTableColumn
rtgDpnVarianceMetricRangeIndex = _RtgDpnVarianceMetricRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 343, 1, 2),
    _RtgDpnVarianceMetricRangeIndex_Type()
)
rtgDpnVarianceMetricRangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgDpnVarianceMetricRangeIndex.setStatus("mandatory")


class _RtgDpnVarianceValue_Type(Unsigned32):
    """Custom type rtgDpnVarianceValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
        ValueRangeConstraint(9999, 9999),
    )


_RtgDpnVarianceValue_Type.__name__ = "Unsigned32"
_RtgDpnVarianceValue_Object = MibTableColumn
rtgDpnVarianceValue = _RtgDpnVarianceValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 4, 343, 1, 3),
    _RtgDpnVarianceValue_Type()
)
rtgDpnVarianceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgDpnVarianceValue.setStatus("mandatory")
_DpnRoutingMIB_ObjectIdentity = ObjectIdentity
dpnRoutingMIB = _DpnRoutingMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 21)
)
_DpnRoutingGroup_ObjectIdentity = ObjectIdentity
dpnRoutingGroup = _DpnRoutingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 21, 1)
)
_DpnRoutingGroupBE_ObjectIdentity = ObjectIdentity
dpnRoutingGroupBE = _DpnRoutingGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 21, 1, 5)
)
_DpnRoutingGroupBE01_ObjectIdentity = ObjectIdentity
dpnRoutingGroupBE01 = _DpnRoutingGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 21, 1, 5, 2)
)
_DpnRoutingGroupBE01A_ObjectIdentity = ObjectIdentity
dpnRoutingGroupBE01A = _DpnRoutingGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 21, 1, 5, 2, 2)
)
_DpnRoutingCapabilities_ObjectIdentity = ObjectIdentity
dpnRoutingCapabilities = _DpnRoutingCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 21, 3)
)
_DpnRoutingCapabilitiesBE_ObjectIdentity = ObjectIdentity
dpnRoutingCapabilitiesBE = _DpnRoutingCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 21, 3, 5)
)
_DpnRoutingCapabilitiesBE01_ObjectIdentity = ObjectIdentity
dpnRoutingCapabilitiesBE01 = _DpnRoutingCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 21, 3, 5, 2)
)
_DpnRoutingCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
dpnRoutingCapabilitiesBE01A = _DpnRoutingCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 21, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-DpnRoutingMIB",
    **{"rtgDpn": rtgDpn,
       "rtgDpnRowStatusTable": rtgDpnRowStatusTable,
       "rtgDpnRowStatusEntry": rtgDpnRowStatusEntry,
       "rtgDpnRowStatus": rtgDpnRowStatus,
       "rtgDpnComponentName": rtgDpnComponentName,
       "rtgDpnStorageType": rtgDpnStorageType,
       "rtgDpnIndex": rtgDpnIndex,
       "rtgDpnRid": rtgDpnRid,
       "rtgDpnRidRowStatusTable": rtgDpnRidRowStatusTable,
       "rtgDpnRidRowStatusEntry": rtgDpnRidRowStatusEntry,
       "rtgDpnRidRowStatus": rtgDpnRidRowStatus,
       "rtgDpnRidComponentName": rtgDpnRidComponentName,
       "rtgDpnRidStorageType": rtgDpnRidStorageType,
       "rtgDpnRidIndex": rtgDpnRidIndex,
       "rtgDpnRidMid": rtgDpnRidMid,
       "rtgDpnRidMidRowStatusTable": rtgDpnRidMidRowStatusTable,
       "rtgDpnRidMidRowStatusEntry": rtgDpnRidMidRowStatusEntry,
       "rtgDpnRidMidRowStatus": rtgDpnRidMidRowStatus,
       "rtgDpnRidMidComponentName": rtgDpnRidMidComponentName,
       "rtgDpnRidMidStorageType": rtgDpnRidMidStorageType,
       "rtgDpnRidMidIndex": rtgDpnRidMidIndex,
       "rtgDpnRidOperTable": rtgDpnRidOperTable,
       "rtgDpnRidOperEntry": rtgDpnRidOperEntry,
       "rtgDpnRidDpnDelayMetric": rtgDpnRidDpnDelayMetric,
       "rtgDpnRidDpnTputMetric": rtgDpnRidDpnTputMetric,
       "rtgDpnRidDelayNextHopLinkGroupsTable": rtgDpnRidDelayNextHopLinkGroupsTable,
       "rtgDpnRidDelayNextHopLinkGroupsEntry": rtgDpnRidDelayNextHopLinkGroupsEntry,
       "rtgDpnRidDelayNextHopLinkGroupsIndex": rtgDpnRidDelayNextHopLinkGroupsIndex,
       "rtgDpnRidDelayNextHopLinkGroupsValue": rtgDpnRidDelayNextHopLinkGroupsValue,
       "rtgDpnRidTputNextHopLinkGroupsTable": rtgDpnRidTputNextHopLinkGroupsTable,
       "rtgDpnRidTputNextHopLinkGroupsEntry": rtgDpnRidTputNextHopLinkGroupsEntry,
       "rtgDpnRidTputNextHopLinkGroupsIndex": rtgDpnRidTputNextHopLinkGroupsIndex,
       "rtgDpnRidTputNextHopLinkGroupsValue": rtgDpnRidTputNextHopLinkGroupsValue,
       "rtgDpnRidDelayPathTrafficProportionsTable": rtgDpnRidDelayPathTrafficProportionsTable,
       "rtgDpnRidDelayPathTrafficProportionsEntry": rtgDpnRidDelayPathTrafficProportionsEntry,
       "rtgDpnRidDelayPathTrafficProportionsIndex": rtgDpnRidDelayPathTrafficProportionsIndex,
       "rtgDpnRidDelayPathTrafficProportionsValue": rtgDpnRidDelayPathTrafficProportionsValue,
       "rtgDpnRidTputPathTrafficProportionsTable": rtgDpnRidTputPathTrafficProportionsTable,
       "rtgDpnRidTputPathTrafficProportionsEntry": rtgDpnRidTputPathTrafficProportionsEntry,
       "rtgDpnRidTputPathTrafficProportionsIndex": rtgDpnRidTputPathTrafficProportionsIndex,
       "rtgDpnRidTputPathTrafficProportionsValue": rtgDpnRidTputPathTrafficProportionsValue,
       "rtgDpnRidDelayMetricTable": rtgDpnRidDelayMetricTable,
       "rtgDpnRidDelayMetricEntry": rtgDpnRidDelayMetricEntry,
       "rtgDpnRidDelayMetricIndex": rtgDpnRidDelayMetricIndex,
       "rtgDpnRidDelayMetricValue": rtgDpnRidDelayMetricValue,
       "rtgDpnRidTputMetricTable": rtgDpnRidTputMetricTable,
       "rtgDpnRidTputMetricEntry": rtgDpnRidTputMetricEntry,
       "rtgDpnRidTputMetricIndex": rtgDpnRidTputMetricIndex,
       "rtgDpnRidTputMetricValue": rtgDpnRidTputMetricValue,
       "rtgDpnMid": rtgDpnMid,
       "rtgDpnMidRowStatusTable": rtgDpnMidRowStatusTable,
       "rtgDpnMidRowStatusEntry": rtgDpnMidRowStatusEntry,
       "rtgDpnMidRowStatus": rtgDpnMidRowStatus,
       "rtgDpnMidComponentName": rtgDpnMidComponentName,
       "rtgDpnMidStorageType": rtgDpnMidStorageType,
       "rtgDpnMidIndex": rtgDpnMidIndex,
       "rtgDpnMidOperTable": rtgDpnMidOperTable,
       "rtgDpnMidOperEntry": rtgDpnMidOperEntry,
       "rtgDpnMidSubstituteRid": rtgDpnMidSubstituteRid,
       "rtgDpnMidDelayNextHopLinkGroupsTable": rtgDpnMidDelayNextHopLinkGroupsTable,
       "rtgDpnMidDelayNextHopLinkGroupsEntry": rtgDpnMidDelayNextHopLinkGroupsEntry,
       "rtgDpnMidDelayNextHopLinkGroupsIndex": rtgDpnMidDelayNextHopLinkGroupsIndex,
       "rtgDpnMidDelayNextHopLinkGroupsValue": rtgDpnMidDelayNextHopLinkGroupsValue,
       "rtgDpnMidTputNextHopLinkGroupsTable": rtgDpnMidTputNextHopLinkGroupsTable,
       "rtgDpnMidTputNextHopLinkGroupsEntry": rtgDpnMidTputNextHopLinkGroupsEntry,
       "rtgDpnMidTputNextHopLinkGroupsIndex": rtgDpnMidTputNextHopLinkGroupsIndex,
       "rtgDpnMidTputNextHopLinkGroupsValue": rtgDpnMidTputNextHopLinkGroupsValue,
       "rtgDpnMidDelayMetricTable": rtgDpnMidDelayMetricTable,
       "rtgDpnMidDelayMetricEntry": rtgDpnMidDelayMetricEntry,
       "rtgDpnMidDelayMetricIndex": rtgDpnMidDelayMetricIndex,
       "rtgDpnMidDelayMetricValue": rtgDpnMidDelayMetricValue,
       "rtgDpnMidTputMetricTable": rtgDpnMidTputMetricTable,
       "rtgDpnMidTputMetricEntry": rtgDpnMidTputMetricEntry,
       "rtgDpnMidTputMetricIndex": rtgDpnMidTputMetricIndex,
       "rtgDpnMidTputMetricValue": rtgDpnMidTputMetricValue,
       "rtgDpnMidDelayPathTrafficProportionsTable": rtgDpnMidDelayPathTrafficProportionsTable,
       "rtgDpnMidDelayPathTrafficProportionsEntry": rtgDpnMidDelayPathTrafficProportionsEntry,
       "rtgDpnMidDelayPathTrafficProportionsIndex": rtgDpnMidDelayPathTrafficProportionsIndex,
       "rtgDpnMidDelayPathTrafficProportionsValue": rtgDpnMidDelayPathTrafficProportionsValue,
       "rtgDpnMidTputPathTrafficProportionsTable": rtgDpnMidTputPathTrafficProportionsTable,
       "rtgDpnMidTputPathTrafficProportionsEntry": rtgDpnMidTputPathTrafficProportionsEntry,
       "rtgDpnMidTputPathTrafficProportionsIndex": rtgDpnMidTputPathTrafficProportionsIndex,
       "rtgDpnMidTputPathTrafficProportionsValue": rtgDpnMidTputPathTrafficProportionsValue,
       "rtgDpnCs": rtgDpnCs,
       "rtgDpnCsRowStatusTable": rtgDpnCsRowStatusTable,
       "rtgDpnCsRowStatusEntry": rtgDpnCsRowStatusEntry,
       "rtgDpnCsRowStatus": rtgDpnCsRowStatus,
       "rtgDpnCsComponentName": rtgDpnCsComponentName,
       "rtgDpnCsStorageType": rtgDpnCsStorageType,
       "rtgDpnCsIndex": rtgDpnCsIndex,
       "rtgDpnCsDelayNextHopLinkGroupsTable": rtgDpnCsDelayNextHopLinkGroupsTable,
       "rtgDpnCsDelayNextHopLinkGroupsEntry": rtgDpnCsDelayNextHopLinkGroupsEntry,
       "rtgDpnCsDelayNextHopLinkGroupsIndex": rtgDpnCsDelayNextHopLinkGroupsIndex,
       "rtgDpnCsDelayNextHopLinkGroupsValue": rtgDpnCsDelayNextHopLinkGroupsValue,
       "rtgDpnCsTputNextHopLinkGroupsTable": rtgDpnCsTputNextHopLinkGroupsTable,
       "rtgDpnCsTputNextHopLinkGroupsEntry": rtgDpnCsTputNextHopLinkGroupsEntry,
       "rtgDpnCsTputNextHopLinkGroupsIndex": rtgDpnCsTputNextHopLinkGroupsIndex,
       "rtgDpnCsTputNextHopLinkGroupsValue": rtgDpnCsTputNextHopLinkGroupsValue,
       "rtgDpnCsDelayMetricTable": rtgDpnCsDelayMetricTable,
       "rtgDpnCsDelayMetricEntry": rtgDpnCsDelayMetricEntry,
       "rtgDpnCsDelayMetricIndex": rtgDpnCsDelayMetricIndex,
       "rtgDpnCsDelayMetricValue": rtgDpnCsDelayMetricValue,
       "rtgDpnCsTputMetricTable": rtgDpnCsTputMetricTable,
       "rtgDpnCsTputMetricEntry": rtgDpnCsTputMetricEntry,
       "rtgDpnCsTputMetricIndex": rtgDpnCsTputMetricIndex,
       "rtgDpnCsTputMetricValue": rtgDpnCsTputMetricValue,
       "rtgDpnCsDelayPathTrafficProportionsTable": rtgDpnCsDelayPathTrafficProportionsTable,
       "rtgDpnCsDelayPathTrafficProportionsEntry": rtgDpnCsDelayPathTrafficProportionsEntry,
       "rtgDpnCsDelayPathTrafficProportionsIndex": rtgDpnCsDelayPathTrafficProportionsIndex,
       "rtgDpnCsDelayPathTrafficProportionsValue": rtgDpnCsDelayPathTrafficProportionsValue,
       "rtgDpnCsTputPathTrafficProportionsTable": rtgDpnCsTputPathTrafficProportionsTable,
       "rtgDpnCsTputPathTrafficProportionsEntry": rtgDpnCsTputPathTrafficProportionsEntry,
       "rtgDpnCsTputPathTrafficProportionsIndex": rtgDpnCsTputPathTrafficProportionsIndex,
       "rtgDpnCsTputPathTrafficProportionsValue": rtgDpnCsTputPathTrafficProportionsValue,
       "rtgDpnLg": rtgDpnLg,
       "rtgDpnLgRowStatusTable": rtgDpnLgRowStatusTable,
       "rtgDpnLgRowStatusEntry": rtgDpnLgRowStatusEntry,
       "rtgDpnLgRowStatus": rtgDpnLgRowStatus,
       "rtgDpnLgComponentName": rtgDpnLgComponentName,
       "rtgDpnLgStorageType": rtgDpnLgStorageType,
       "rtgDpnLgIndex": rtgDpnLgIndex,
       "rtgDpnLgOperTable": rtgDpnLgOperTable,
       "rtgDpnLgOperEntry": rtgDpnLgOperEntry,
       "rtgDpnLgFarEndType": rtgDpnLgFarEndType,
       "rtgDpnLgFarEndRid": rtgDpnLgFarEndRid,
       "rtgDpnLgFarEndMid": rtgDpnLgFarEndMid,
       "rtgDpnLgDelayMetric": rtgDpnLgDelayMetric,
       "rtgDpnLgTputMetric": rtgDpnLgTputMetric,
       "rtgDpnLpStats": rtgDpnLpStats,
       "rtgDpnLpStatsRowStatusTable": rtgDpnLpStatsRowStatusTable,
       "rtgDpnLpStatsRowStatusEntry": rtgDpnLpStatsRowStatusEntry,
       "rtgDpnLpStatsRowStatus": rtgDpnLpStatsRowStatus,
       "rtgDpnLpStatsComponentName": rtgDpnLpStatsComponentName,
       "rtgDpnLpStatsStorageType": rtgDpnLpStatsStorageType,
       "rtgDpnLpStatsIndex": rtgDpnLpStatsIndex,
       "rtgDpnLpStatsFwdStatsTable": rtgDpnLpStatsFwdStatsTable,
       "rtgDpnLpStatsFwdStatsEntry": rtgDpnLpStatsFwdStatsEntry,
       "rtgDpnLpStatsTotalPackets": rtgDpnLpStatsTotalPackets,
       "rtgDpnLpStatsThroughputPackets": rtgDpnLpStatsThroughputPackets,
       "rtgDpnLpStatsDelayPackets": rtgDpnLpStatsDelayPackets,
       "rtgDpnLpStatsNormalReliabilityPackets": rtgDpnLpStatsNormalReliabilityPackets,
       "rtgDpnLpStatsHighReliabilityPackets": rtgDpnLpStatsHighReliabilityPackets,
       "rtgDpnLpStatsDiscardNoRoute": rtgDpnLpStatsDiscardNoRoute,
       "rtgDpnLpStatsInterruptingPackets": rtgDpnLpStatsInterruptingPackets,
       "rtgDpnLpStatsDiscardLpCongested": rtgDpnLpStatsDiscardLpCongested,
       "rtgDpnRidFilter": rtgDpnRidFilter,
       "rtgDpnRidFilterRowStatusTable": rtgDpnRidFilterRowStatusTable,
       "rtgDpnRidFilterRowStatusEntry": rtgDpnRidFilterRowStatusEntry,
       "rtgDpnRidFilterRowStatus": rtgDpnRidFilterRowStatus,
       "rtgDpnRidFilterComponentName": rtgDpnRidFilterComponentName,
       "rtgDpnRidFilterStorageType": rtgDpnRidFilterStorageType,
       "rtgDpnRidFilterIndex": rtgDpnRidFilterIndex,
       "rtgDpnRidFilterImportRidListTable": rtgDpnRidFilterImportRidListTable,
       "rtgDpnRidFilterImportRidListEntry": rtgDpnRidFilterImportRidListEntry,
       "rtgDpnRidFilterImportRidListValue": rtgDpnRidFilterImportRidListValue,
       "rtgDpnRidFilterImportRidListRowStatus": rtgDpnRidFilterImportRidListRowStatus,
       "rtgDpnRidFilterExportRidListTable": rtgDpnRidFilterExportRidListTable,
       "rtgDpnRidFilterExportRidListEntry": rtgDpnRidFilterExportRidListEntry,
       "rtgDpnRidFilterExportRidListValue": rtgDpnRidFilterExportRidListValue,
       "rtgDpnRidFilterExportRidListRowStatus": rtgDpnRidFilterExportRidListRowStatus,
       "rtgDpnProvTable": rtgDpnProvTable,
       "rtgDpnProvEntry": rtgDpnProvEntry,
       "rtgDpnLogicalNetworkNumber": rtgDpnLogicalNetworkNumber,
       "rtgDpnRoutingId": rtgDpnRoutingId,
       "rtgDpnModuleId": rtgDpnModuleId,
       "rtgDpnDelayMetricCutOff": rtgDpnDelayMetricCutOff,
       "rtgDpnThroughputMetricCutOff": rtgDpnThroughputMetricCutOff,
       "rtgDpnForwardingPolicy": rtgDpnForwardingPolicy,
       "rtgDpnDelayMetricRangeBoundary": rtgDpnDelayMetricRangeBoundary,
       "rtgDpnTputMetricRangeBoundary": rtgDpnTputMetricRangeBoundary,
       "rtgDpnConStatsTable": rtgDpnConStatsTable,
       "rtgDpnConStatsEntry": rtgDpnConStatsEntry,
       "rtgDpnControlPktTx": rtgDpnControlPktTx,
       "rtgDpnControlPktRx": rtgDpnControlPktRx,
       "rtgDpnControlBytesTx": rtgDpnControlBytesTx,
       "rtgDpnControlBytesRx": rtgDpnControlBytesRx,
       "rtgDpnOutOfSequencePkt": rtgDpnOutOfSequencePkt,
       "rtgDpnFwdStatsTable": rtgDpnFwdStatsTable,
       "rtgDpnFwdStatsEntry": rtgDpnFwdStatsEntry,
       "rtgDpnTotalPackets": rtgDpnTotalPackets,
       "rtgDpnThroughputPackets": rtgDpnThroughputPackets,
       "rtgDpnDelayPackets": rtgDpnDelayPackets,
       "rtgDpnNormalReliabilityPackets": rtgDpnNormalReliabilityPackets,
       "rtgDpnHighReliabilityPackets": rtgDpnHighReliabilityPackets,
       "rtgDpnDiscardNoRoute": rtgDpnDiscardNoRoute,
       "rtgDpnInterruptingPackets": rtgDpnInterruptingPackets,
       "rtgDpnDiscardLpCongested": rtgDpnDiscardLpCongested,
       "rtgDpnCallServerModuleRidsTable": rtgDpnCallServerModuleRidsTable,
       "rtgDpnCallServerModuleRidsEntry": rtgDpnCallServerModuleRidsEntry,
       "rtgDpnCallServerModuleRidsValue": rtgDpnCallServerModuleRidsValue,
       "rtgDpnSubnetMidsTable": rtgDpnSubnetMidsTable,
       "rtgDpnSubnetMidsEntry": rtgDpnSubnetMidsEntry,
       "rtgDpnSubnetMidsValue": rtgDpnSubnetMidsValue,
       "rtgDpnVarianceTable": rtgDpnVarianceTable,
       "rtgDpnVarianceEntry": rtgDpnVarianceEntry,
       "rtgDpnVarianceCosIndex": rtgDpnVarianceCosIndex,
       "rtgDpnVarianceMetricRangeIndex": rtgDpnVarianceMetricRangeIndex,
       "rtgDpnVarianceValue": rtgDpnVarianceValue,
       "dpnRoutingMIB": dpnRoutingMIB,
       "dpnRoutingGroup": dpnRoutingGroup,
       "dpnRoutingGroupBE": dpnRoutingGroupBE,
       "dpnRoutingGroupBE01": dpnRoutingGroupBE01,
       "dpnRoutingGroupBE01A": dpnRoutingGroupBE01A,
       "dpnRoutingCapabilities": dpnRoutingCapabilities,
       "dpnRoutingCapabilitiesBE": dpnRoutingCapabilitiesBE,
       "dpnRoutingCapabilitiesBE01": dpnRoutingCapabilitiesBE01,
       "dpnRoutingCapabilitiesBE01A": dpnRoutingCapabilitiesBE01A}
)
