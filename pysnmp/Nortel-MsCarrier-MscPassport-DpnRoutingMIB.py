# SNMP MIB module (Nortel-MsCarrier-MscPassport-DpnRoutingMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-DpnRoutingMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:15 2024
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

(mscRtg,
 mscRtgIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-BaseRoutingMIB",
    "mscRtg",
    "mscRtgIndex")

(DisplayString,
 Integer32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 AsciiStringIndex,
 NonReplicated,
 PassportCounter64) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
    "NonReplicated",
    "PassportCounter64")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscPassportMIBs")

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

_MscRtgDpn_ObjectIdentity = ObjectIdentity
mscRtgDpn = _MscRtgDpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4)
)
_MscRtgDpnRowStatusTable_Object = MibTable
mscRtgDpnRowStatusTable = _MscRtgDpnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 1)
)
if mibBuilder.loadTexts:
    mscRtgDpnRowStatusTable.setStatus("mandatory")
_MscRtgDpnRowStatusEntry_Object = MibTableRow
mscRtgDpnRowStatusEntry = _MscRtgDpnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 1, 1)
)
mscRtgDpnRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnRowStatusEntry.setStatus("mandatory")
_MscRtgDpnRowStatus_Type = RowStatus
_MscRtgDpnRowStatus_Object = MibTableColumn
mscRtgDpnRowStatus = _MscRtgDpnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 1, 1, 1),
    _MscRtgDpnRowStatus_Type()
)
mscRtgDpnRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnRowStatus.setStatus("mandatory")
_MscRtgDpnComponentName_Type = DisplayString
_MscRtgDpnComponentName_Object = MibTableColumn
mscRtgDpnComponentName = _MscRtgDpnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 1, 1, 2),
    _MscRtgDpnComponentName_Type()
)
mscRtgDpnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnComponentName.setStatus("mandatory")
_MscRtgDpnStorageType_Type = StorageType
_MscRtgDpnStorageType_Object = MibTableColumn
mscRtgDpnStorageType = _MscRtgDpnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 1, 1, 4),
    _MscRtgDpnStorageType_Type()
)
mscRtgDpnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnStorageType.setStatus("mandatory")
_MscRtgDpnIndex_Type = NonReplicated
_MscRtgDpnIndex_Object = MibTableColumn
mscRtgDpnIndex = _MscRtgDpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 1, 1, 10),
    _MscRtgDpnIndex_Type()
)
mscRtgDpnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnIndex.setStatus("mandatory")
_MscRtgDpnRid_ObjectIdentity = ObjectIdentity
mscRtgDpnRid = _MscRtgDpnRid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2)
)
_MscRtgDpnRidRowStatusTable_Object = MibTable
mscRtgDpnRidRowStatusTable = _MscRtgDpnRidRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscRtgDpnRidRowStatusTable.setStatus("mandatory")
_MscRtgDpnRidRowStatusEntry_Object = MibTableRow
mscRtgDpnRidRowStatusEntry = _MscRtgDpnRidRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 1, 1)
)
mscRtgDpnRidRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnRidIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnRidRowStatusEntry.setStatus("mandatory")
_MscRtgDpnRidRowStatus_Type = RowStatus
_MscRtgDpnRidRowStatus_Object = MibTableColumn
mscRtgDpnRidRowStatus = _MscRtgDpnRidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 1, 1, 1),
    _MscRtgDpnRidRowStatus_Type()
)
mscRtgDpnRidRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnRidRowStatus.setStatus("mandatory")
_MscRtgDpnRidComponentName_Type = DisplayString
_MscRtgDpnRidComponentName_Object = MibTableColumn
mscRtgDpnRidComponentName = _MscRtgDpnRidComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 1, 1, 2),
    _MscRtgDpnRidComponentName_Type()
)
mscRtgDpnRidComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnRidComponentName.setStatus("mandatory")
_MscRtgDpnRidStorageType_Type = StorageType
_MscRtgDpnRidStorageType_Object = MibTableColumn
mscRtgDpnRidStorageType = _MscRtgDpnRidStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 1, 1, 4),
    _MscRtgDpnRidStorageType_Type()
)
mscRtgDpnRidStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnRidStorageType.setStatus("mandatory")


class _MscRtgDpnRidIndex_Type(Integer32):
    """Custom type mscRtgDpnRidIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MscRtgDpnRidIndex_Type.__name__ = "Integer32"
_MscRtgDpnRidIndex_Object = MibTableColumn
mscRtgDpnRidIndex = _MscRtgDpnRidIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 1, 1, 10),
    _MscRtgDpnRidIndex_Type()
)
mscRtgDpnRidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnRidIndex.setStatus("mandatory")
_MscRtgDpnRidMid_ObjectIdentity = ObjectIdentity
mscRtgDpnRidMid = _MscRtgDpnRidMid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 2)
)
_MscRtgDpnRidMidRowStatusTable_Object = MibTable
mscRtgDpnRidMidRowStatusTable = _MscRtgDpnRidMidRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscRtgDpnRidMidRowStatusTable.setStatus("mandatory")
_MscRtgDpnRidMidRowStatusEntry_Object = MibTableRow
mscRtgDpnRidMidRowStatusEntry = _MscRtgDpnRidMidRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 2, 1, 1)
)
mscRtgDpnRidMidRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnRidIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnRidMidIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnRidMidRowStatusEntry.setStatus("mandatory")
_MscRtgDpnRidMidRowStatus_Type = RowStatus
_MscRtgDpnRidMidRowStatus_Object = MibTableColumn
mscRtgDpnRidMidRowStatus = _MscRtgDpnRidMidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 2, 1, 1, 1),
    _MscRtgDpnRidMidRowStatus_Type()
)
mscRtgDpnRidMidRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnRidMidRowStatus.setStatus("mandatory")
_MscRtgDpnRidMidComponentName_Type = DisplayString
_MscRtgDpnRidMidComponentName_Object = MibTableColumn
mscRtgDpnRidMidComponentName = _MscRtgDpnRidMidComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 2, 1, 1, 2),
    _MscRtgDpnRidMidComponentName_Type()
)
mscRtgDpnRidMidComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnRidMidComponentName.setStatus("mandatory")
_MscRtgDpnRidMidStorageType_Type = StorageType
_MscRtgDpnRidMidStorageType_Object = MibTableColumn
mscRtgDpnRidMidStorageType = _MscRtgDpnRidMidStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 2, 1, 1, 4),
    _MscRtgDpnRidMidStorageType_Type()
)
mscRtgDpnRidMidStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnRidMidStorageType.setStatus("mandatory")


class _MscRtgDpnRidMidIndex_Type(Integer32):
    """Custom type mscRtgDpnRidMidIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2046),
    )


_MscRtgDpnRidMidIndex_Type.__name__ = "Integer32"
_MscRtgDpnRidMidIndex_Object = MibTableColumn
mscRtgDpnRidMidIndex = _MscRtgDpnRidMidIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 2, 1, 1, 10),
    _MscRtgDpnRidMidIndex_Type()
)
mscRtgDpnRidMidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnRidMidIndex.setStatus("mandatory")
_MscRtgDpnRidOperTable_Object = MibTable
mscRtgDpnRidOperTable = _MscRtgDpnRidOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 10)
)
if mibBuilder.loadTexts:
    mscRtgDpnRidOperTable.setStatus("mandatory")
_MscRtgDpnRidOperEntry_Object = MibTableRow
mscRtgDpnRidOperEntry = _MscRtgDpnRidOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 10, 1)
)
mscRtgDpnRidOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnRidIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnRidOperEntry.setStatus("mandatory")


class _MscRtgDpnRidDpnDelayMetric_Type(Unsigned32):
    """Custom type mscRtgDpnRidDpnDelayMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscRtgDpnRidDpnDelayMetric_Type.__name__ = "Unsigned32"
_MscRtgDpnRidDpnDelayMetric_Object = MibTableColumn
mscRtgDpnRidDpnDelayMetric = _MscRtgDpnRidDpnDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 10, 1, 1),
    _MscRtgDpnRidDpnDelayMetric_Type()
)
mscRtgDpnRidDpnDelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnRidDpnDelayMetric.setStatus("mandatory")


class _MscRtgDpnRidDpnTputMetric_Type(Unsigned32):
    """Custom type mscRtgDpnRidDpnTputMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscRtgDpnRidDpnTputMetric_Type.__name__ = "Unsigned32"
_MscRtgDpnRidDpnTputMetric_Object = MibTableColumn
mscRtgDpnRidDpnTputMetric = _MscRtgDpnRidDpnTputMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 10, 1, 2),
    _MscRtgDpnRidDpnTputMetric_Type()
)
mscRtgDpnRidDpnTputMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnRidDpnTputMetric.setStatus("mandatory")
_MscRtgDpnRidDelayNextHopLinkGroupsTable_Object = MibTable
mscRtgDpnRidDelayNextHopLinkGroupsTable = _MscRtgDpnRidDelayNextHopLinkGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 226)
)
if mibBuilder.loadTexts:
    mscRtgDpnRidDelayNextHopLinkGroupsTable.setStatus("mandatory")
_MscRtgDpnRidDelayNextHopLinkGroupsEntry_Object = MibTableRow
mscRtgDpnRidDelayNextHopLinkGroupsEntry = _MscRtgDpnRidDelayNextHopLinkGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 226, 1)
)
mscRtgDpnRidDelayNextHopLinkGroupsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnRidIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnRidDelayNextHopLinkGroupsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnRidDelayNextHopLinkGroupsEntry.setStatus("mandatory")


class _MscRtgDpnRidDelayNextHopLinkGroupsIndex_Type(Integer32):
    """Custom type mscRtgDpnRidDelayNextHopLinkGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscRtgDpnRidDelayNextHopLinkGroupsIndex_Type.__name__ = "Integer32"
_MscRtgDpnRidDelayNextHopLinkGroupsIndex_Object = MibTableColumn
mscRtgDpnRidDelayNextHopLinkGroupsIndex = _MscRtgDpnRidDelayNextHopLinkGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 226, 1, 1),
    _MscRtgDpnRidDelayNextHopLinkGroupsIndex_Type()
)
mscRtgDpnRidDelayNextHopLinkGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnRidDelayNextHopLinkGroupsIndex.setStatus("mandatory")
_MscRtgDpnRidDelayNextHopLinkGroupsValue_Type = RowPointer
_MscRtgDpnRidDelayNextHopLinkGroupsValue_Object = MibTableColumn
mscRtgDpnRidDelayNextHopLinkGroupsValue = _MscRtgDpnRidDelayNextHopLinkGroupsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 226, 1, 2),
    _MscRtgDpnRidDelayNextHopLinkGroupsValue_Type()
)
mscRtgDpnRidDelayNextHopLinkGroupsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnRidDelayNextHopLinkGroupsValue.setStatus("mandatory")
_MscRtgDpnRidTputNextHopLinkGroupsTable_Object = MibTable
mscRtgDpnRidTputNextHopLinkGroupsTable = _MscRtgDpnRidTputNextHopLinkGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 227)
)
if mibBuilder.loadTexts:
    mscRtgDpnRidTputNextHopLinkGroupsTable.setStatus("mandatory")
_MscRtgDpnRidTputNextHopLinkGroupsEntry_Object = MibTableRow
mscRtgDpnRidTputNextHopLinkGroupsEntry = _MscRtgDpnRidTputNextHopLinkGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 227, 1)
)
mscRtgDpnRidTputNextHopLinkGroupsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnRidIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnRidTputNextHopLinkGroupsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnRidTputNextHopLinkGroupsEntry.setStatus("mandatory")


class _MscRtgDpnRidTputNextHopLinkGroupsIndex_Type(Integer32):
    """Custom type mscRtgDpnRidTputNextHopLinkGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscRtgDpnRidTputNextHopLinkGroupsIndex_Type.__name__ = "Integer32"
_MscRtgDpnRidTputNextHopLinkGroupsIndex_Object = MibTableColumn
mscRtgDpnRidTputNextHopLinkGroupsIndex = _MscRtgDpnRidTputNextHopLinkGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 227, 1, 1),
    _MscRtgDpnRidTputNextHopLinkGroupsIndex_Type()
)
mscRtgDpnRidTputNextHopLinkGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnRidTputNextHopLinkGroupsIndex.setStatus("mandatory")
_MscRtgDpnRidTputNextHopLinkGroupsValue_Type = RowPointer
_MscRtgDpnRidTputNextHopLinkGroupsValue_Object = MibTableColumn
mscRtgDpnRidTputNextHopLinkGroupsValue = _MscRtgDpnRidTputNextHopLinkGroupsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 227, 1, 2),
    _MscRtgDpnRidTputNextHopLinkGroupsValue_Type()
)
mscRtgDpnRidTputNextHopLinkGroupsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnRidTputNextHopLinkGroupsValue.setStatus("mandatory")
_MscRtgDpnRidDelayPathTrafficProportionsTable_Object = MibTable
mscRtgDpnRidDelayPathTrafficProportionsTable = _MscRtgDpnRidDelayPathTrafficProportionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 328)
)
if mibBuilder.loadTexts:
    mscRtgDpnRidDelayPathTrafficProportionsTable.setStatus("mandatory")
_MscRtgDpnRidDelayPathTrafficProportionsEntry_Object = MibTableRow
mscRtgDpnRidDelayPathTrafficProportionsEntry = _MscRtgDpnRidDelayPathTrafficProportionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 328, 1)
)
mscRtgDpnRidDelayPathTrafficProportionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnRidIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnRidDelayPathTrafficProportionsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnRidDelayPathTrafficProportionsEntry.setStatus("mandatory")


class _MscRtgDpnRidDelayPathTrafficProportionsIndex_Type(Integer32):
    """Custom type mscRtgDpnRidDelayPathTrafficProportionsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscRtgDpnRidDelayPathTrafficProportionsIndex_Type.__name__ = "Integer32"
_MscRtgDpnRidDelayPathTrafficProportionsIndex_Object = MibTableColumn
mscRtgDpnRidDelayPathTrafficProportionsIndex = _MscRtgDpnRidDelayPathTrafficProportionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 328, 1, 1),
    _MscRtgDpnRidDelayPathTrafficProportionsIndex_Type()
)
mscRtgDpnRidDelayPathTrafficProportionsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnRidDelayPathTrafficProportionsIndex.setStatus("mandatory")


class _MscRtgDpnRidDelayPathTrafficProportionsValue_Type(Unsigned32):
    """Custom type mscRtgDpnRidDelayPathTrafficProportionsValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscRtgDpnRidDelayPathTrafficProportionsValue_Type.__name__ = "Unsigned32"
_MscRtgDpnRidDelayPathTrafficProportionsValue_Object = MibTableColumn
mscRtgDpnRidDelayPathTrafficProportionsValue = _MscRtgDpnRidDelayPathTrafficProportionsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 328, 1, 2),
    _MscRtgDpnRidDelayPathTrafficProportionsValue_Type()
)
mscRtgDpnRidDelayPathTrafficProportionsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnRidDelayPathTrafficProportionsValue.setStatus("mandatory")
_MscRtgDpnRidTputPathTrafficProportionsTable_Object = MibTable
mscRtgDpnRidTputPathTrafficProportionsTable = _MscRtgDpnRidTputPathTrafficProportionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 329)
)
if mibBuilder.loadTexts:
    mscRtgDpnRidTputPathTrafficProportionsTable.setStatus("mandatory")
_MscRtgDpnRidTputPathTrafficProportionsEntry_Object = MibTableRow
mscRtgDpnRidTputPathTrafficProportionsEntry = _MscRtgDpnRidTputPathTrafficProportionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 329, 1)
)
mscRtgDpnRidTputPathTrafficProportionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnRidIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnRidTputPathTrafficProportionsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnRidTputPathTrafficProportionsEntry.setStatus("mandatory")


class _MscRtgDpnRidTputPathTrafficProportionsIndex_Type(Integer32):
    """Custom type mscRtgDpnRidTputPathTrafficProportionsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscRtgDpnRidTputPathTrafficProportionsIndex_Type.__name__ = "Integer32"
_MscRtgDpnRidTputPathTrafficProportionsIndex_Object = MibTableColumn
mscRtgDpnRidTputPathTrafficProportionsIndex = _MscRtgDpnRidTputPathTrafficProportionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 329, 1, 1),
    _MscRtgDpnRidTputPathTrafficProportionsIndex_Type()
)
mscRtgDpnRidTputPathTrafficProportionsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnRidTputPathTrafficProportionsIndex.setStatus("mandatory")


class _MscRtgDpnRidTputPathTrafficProportionsValue_Type(Unsigned32):
    """Custom type mscRtgDpnRidTputPathTrafficProportionsValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscRtgDpnRidTputPathTrafficProportionsValue_Type.__name__ = "Unsigned32"
_MscRtgDpnRidTputPathTrafficProportionsValue_Object = MibTableColumn
mscRtgDpnRidTputPathTrafficProportionsValue = _MscRtgDpnRidTputPathTrafficProportionsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 329, 1, 2),
    _MscRtgDpnRidTputPathTrafficProportionsValue_Type()
)
mscRtgDpnRidTputPathTrafficProportionsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnRidTputPathTrafficProportionsValue.setStatus("mandatory")
_MscRtgDpnRidDelayMetricTable_Object = MibTable
mscRtgDpnRidDelayMetricTable = _MscRtgDpnRidDelayMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 339)
)
if mibBuilder.loadTexts:
    mscRtgDpnRidDelayMetricTable.setStatus("mandatory")
_MscRtgDpnRidDelayMetricEntry_Object = MibTableRow
mscRtgDpnRidDelayMetricEntry = _MscRtgDpnRidDelayMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 339, 1)
)
mscRtgDpnRidDelayMetricEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnRidIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnRidDelayMetricIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnRidDelayMetricEntry.setStatus("mandatory")


class _MscRtgDpnRidDelayMetricIndex_Type(Integer32):
    """Custom type mscRtgDpnRidDelayMetricIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscRtgDpnRidDelayMetricIndex_Type.__name__ = "Integer32"
_MscRtgDpnRidDelayMetricIndex_Object = MibTableColumn
mscRtgDpnRidDelayMetricIndex = _MscRtgDpnRidDelayMetricIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 339, 1, 1),
    _MscRtgDpnRidDelayMetricIndex_Type()
)
mscRtgDpnRidDelayMetricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnRidDelayMetricIndex.setStatus("mandatory")


class _MscRtgDpnRidDelayMetricValue_Type(Unsigned32):
    """Custom type mscRtgDpnRidDelayMetricValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscRtgDpnRidDelayMetricValue_Type.__name__ = "Unsigned32"
_MscRtgDpnRidDelayMetricValue_Object = MibTableColumn
mscRtgDpnRidDelayMetricValue = _MscRtgDpnRidDelayMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 339, 1, 2),
    _MscRtgDpnRidDelayMetricValue_Type()
)
mscRtgDpnRidDelayMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnRidDelayMetricValue.setStatus("mandatory")
_MscRtgDpnRidTputMetricTable_Object = MibTable
mscRtgDpnRidTputMetricTable = _MscRtgDpnRidTputMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 340)
)
if mibBuilder.loadTexts:
    mscRtgDpnRidTputMetricTable.setStatus("mandatory")
_MscRtgDpnRidTputMetricEntry_Object = MibTableRow
mscRtgDpnRidTputMetricEntry = _MscRtgDpnRidTputMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 340, 1)
)
mscRtgDpnRidTputMetricEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnRidIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnRidTputMetricIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnRidTputMetricEntry.setStatus("mandatory")


class _MscRtgDpnRidTputMetricIndex_Type(Integer32):
    """Custom type mscRtgDpnRidTputMetricIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscRtgDpnRidTputMetricIndex_Type.__name__ = "Integer32"
_MscRtgDpnRidTputMetricIndex_Object = MibTableColumn
mscRtgDpnRidTputMetricIndex = _MscRtgDpnRidTputMetricIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 340, 1, 1),
    _MscRtgDpnRidTputMetricIndex_Type()
)
mscRtgDpnRidTputMetricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnRidTputMetricIndex.setStatus("mandatory")


class _MscRtgDpnRidTputMetricValue_Type(Unsigned32):
    """Custom type mscRtgDpnRidTputMetricValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscRtgDpnRidTputMetricValue_Type.__name__ = "Unsigned32"
_MscRtgDpnRidTputMetricValue_Object = MibTableColumn
mscRtgDpnRidTputMetricValue = _MscRtgDpnRidTputMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 2, 340, 1, 2),
    _MscRtgDpnRidTputMetricValue_Type()
)
mscRtgDpnRidTputMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnRidTputMetricValue.setStatus("mandatory")
_MscRtgDpnMid_ObjectIdentity = ObjectIdentity
mscRtgDpnMid = _MscRtgDpnMid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3)
)
_MscRtgDpnMidRowStatusTable_Object = MibTable
mscRtgDpnMidRowStatusTable = _MscRtgDpnMidRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 1)
)
if mibBuilder.loadTexts:
    mscRtgDpnMidRowStatusTable.setStatus("mandatory")
_MscRtgDpnMidRowStatusEntry_Object = MibTableRow
mscRtgDpnMidRowStatusEntry = _MscRtgDpnMidRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 1, 1)
)
mscRtgDpnMidRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnMidIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnMidRowStatusEntry.setStatus("mandatory")
_MscRtgDpnMidRowStatus_Type = RowStatus
_MscRtgDpnMidRowStatus_Object = MibTableColumn
mscRtgDpnMidRowStatus = _MscRtgDpnMidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 1, 1, 1),
    _MscRtgDpnMidRowStatus_Type()
)
mscRtgDpnMidRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnMidRowStatus.setStatus("mandatory")
_MscRtgDpnMidComponentName_Type = DisplayString
_MscRtgDpnMidComponentName_Object = MibTableColumn
mscRtgDpnMidComponentName = _MscRtgDpnMidComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 1, 1, 2),
    _MscRtgDpnMidComponentName_Type()
)
mscRtgDpnMidComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnMidComponentName.setStatus("mandatory")
_MscRtgDpnMidStorageType_Type = StorageType
_MscRtgDpnMidStorageType_Object = MibTableColumn
mscRtgDpnMidStorageType = _MscRtgDpnMidStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 1, 1, 4),
    _MscRtgDpnMidStorageType_Type()
)
mscRtgDpnMidStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnMidStorageType.setStatus("mandatory")


class _MscRtgDpnMidIndex_Type(Integer32):
    """Custom type mscRtgDpnMidIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2046),
    )


_MscRtgDpnMidIndex_Type.__name__ = "Integer32"
_MscRtgDpnMidIndex_Object = MibTableColumn
mscRtgDpnMidIndex = _MscRtgDpnMidIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 1, 1, 10),
    _MscRtgDpnMidIndex_Type()
)
mscRtgDpnMidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnMidIndex.setStatus("mandatory")
_MscRtgDpnMidOperTable_Object = MibTable
mscRtgDpnMidOperTable = _MscRtgDpnMidOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 10)
)
if mibBuilder.loadTexts:
    mscRtgDpnMidOperTable.setStatus("mandatory")
_MscRtgDpnMidOperEntry_Object = MibTableRow
mscRtgDpnMidOperEntry = _MscRtgDpnMidOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 10, 1)
)
mscRtgDpnMidOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnMidIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnMidOperEntry.setStatus("mandatory")


class _MscRtgDpnMidSubstituteRid_Type(Unsigned32):
    """Custom type mscRtgDpnMidSubstituteRid based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_MscRtgDpnMidSubstituteRid_Type.__name__ = "Unsigned32"
_MscRtgDpnMidSubstituteRid_Object = MibTableColumn
mscRtgDpnMidSubstituteRid = _MscRtgDpnMidSubstituteRid_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 10, 1, 3),
    _MscRtgDpnMidSubstituteRid_Type()
)
mscRtgDpnMidSubstituteRid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnMidSubstituteRid.setStatus("mandatory")
_MscRtgDpnMidDelayNextHopLinkGroupsTable_Object = MibTable
mscRtgDpnMidDelayNextHopLinkGroupsTable = _MscRtgDpnMidDelayNextHopLinkGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 228)
)
if mibBuilder.loadTexts:
    mscRtgDpnMidDelayNextHopLinkGroupsTable.setStatus("mandatory")
_MscRtgDpnMidDelayNextHopLinkGroupsEntry_Object = MibTableRow
mscRtgDpnMidDelayNextHopLinkGroupsEntry = _MscRtgDpnMidDelayNextHopLinkGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 228, 1)
)
mscRtgDpnMidDelayNextHopLinkGroupsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnMidIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnMidDelayNextHopLinkGroupsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnMidDelayNextHopLinkGroupsEntry.setStatus("mandatory")


class _MscRtgDpnMidDelayNextHopLinkGroupsIndex_Type(Integer32):
    """Custom type mscRtgDpnMidDelayNextHopLinkGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscRtgDpnMidDelayNextHopLinkGroupsIndex_Type.__name__ = "Integer32"
_MscRtgDpnMidDelayNextHopLinkGroupsIndex_Object = MibTableColumn
mscRtgDpnMidDelayNextHopLinkGroupsIndex = _MscRtgDpnMidDelayNextHopLinkGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 228, 1, 1),
    _MscRtgDpnMidDelayNextHopLinkGroupsIndex_Type()
)
mscRtgDpnMidDelayNextHopLinkGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnMidDelayNextHopLinkGroupsIndex.setStatus("mandatory")
_MscRtgDpnMidDelayNextHopLinkGroupsValue_Type = RowPointer
_MscRtgDpnMidDelayNextHopLinkGroupsValue_Object = MibTableColumn
mscRtgDpnMidDelayNextHopLinkGroupsValue = _MscRtgDpnMidDelayNextHopLinkGroupsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 228, 1, 2),
    _MscRtgDpnMidDelayNextHopLinkGroupsValue_Type()
)
mscRtgDpnMidDelayNextHopLinkGroupsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnMidDelayNextHopLinkGroupsValue.setStatus("mandatory")
_MscRtgDpnMidTputNextHopLinkGroupsTable_Object = MibTable
mscRtgDpnMidTputNextHopLinkGroupsTable = _MscRtgDpnMidTputNextHopLinkGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 229)
)
if mibBuilder.loadTexts:
    mscRtgDpnMidTputNextHopLinkGroupsTable.setStatus("mandatory")
_MscRtgDpnMidTputNextHopLinkGroupsEntry_Object = MibTableRow
mscRtgDpnMidTputNextHopLinkGroupsEntry = _MscRtgDpnMidTputNextHopLinkGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 229, 1)
)
mscRtgDpnMidTputNextHopLinkGroupsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnMidIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnMidTputNextHopLinkGroupsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnMidTputNextHopLinkGroupsEntry.setStatus("mandatory")


class _MscRtgDpnMidTputNextHopLinkGroupsIndex_Type(Integer32):
    """Custom type mscRtgDpnMidTputNextHopLinkGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscRtgDpnMidTputNextHopLinkGroupsIndex_Type.__name__ = "Integer32"
_MscRtgDpnMidTputNextHopLinkGroupsIndex_Object = MibTableColumn
mscRtgDpnMidTputNextHopLinkGroupsIndex = _MscRtgDpnMidTputNextHopLinkGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 229, 1, 1),
    _MscRtgDpnMidTputNextHopLinkGroupsIndex_Type()
)
mscRtgDpnMidTputNextHopLinkGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnMidTputNextHopLinkGroupsIndex.setStatus("mandatory")
_MscRtgDpnMidTputNextHopLinkGroupsValue_Type = RowPointer
_MscRtgDpnMidTputNextHopLinkGroupsValue_Object = MibTableColumn
mscRtgDpnMidTputNextHopLinkGroupsValue = _MscRtgDpnMidTputNextHopLinkGroupsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 229, 1, 2),
    _MscRtgDpnMidTputNextHopLinkGroupsValue_Type()
)
mscRtgDpnMidTputNextHopLinkGroupsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnMidTputNextHopLinkGroupsValue.setStatus("mandatory")
_MscRtgDpnMidDelayMetricTable_Object = MibTable
mscRtgDpnMidDelayMetricTable = _MscRtgDpnMidDelayMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 330)
)
if mibBuilder.loadTexts:
    mscRtgDpnMidDelayMetricTable.setStatus("mandatory")
_MscRtgDpnMidDelayMetricEntry_Object = MibTableRow
mscRtgDpnMidDelayMetricEntry = _MscRtgDpnMidDelayMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 330, 1)
)
mscRtgDpnMidDelayMetricEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnMidIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnMidDelayMetricIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnMidDelayMetricEntry.setStatus("mandatory")


class _MscRtgDpnMidDelayMetricIndex_Type(Integer32):
    """Custom type mscRtgDpnMidDelayMetricIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscRtgDpnMidDelayMetricIndex_Type.__name__ = "Integer32"
_MscRtgDpnMidDelayMetricIndex_Object = MibTableColumn
mscRtgDpnMidDelayMetricIndex = _MscRtgDpnMidDelayMetricIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 330, 1, 1),
    _MscRtgDpnMidDelayMetricIndex_Type()
)
mscRtgDpnMidDelayMetricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnMidDelayMetricIndex.setStatus("mandatory")


class _MscRtgDpnMidDelayMetricValue_Type(Unsigned32):
    """Custom type mscRtgDpnMidDelayMetricValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscRtgDpnMidDelayMetricValue_Type.__name__ = "Unsigned32"
_MscRtgDpnMidDelayMetricValue_Object = MibTableColumn
mscRtgDpnMidDelayMetricValue = _MscRtgDpnMidDelayMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 330, 1, 2),
    _MscRtgDpnMidDelayMetricValue_Type()
)
mscRtgDpnMidDelayMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnMidDelayMetricValue.setStatus("mandatory")
_MscRtgDpnMidTputMetricTable_Object = MibTable
mscRtgDpnMidTputMetricTable = _MscRtgDpnMidTputMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 331)
)
if mibBuilder.loadTexts:
    mscRtgDpnMidTputMetricTable.setStatus("mandatory")
_MscRtgDpnMidTputMetricEntry_Object = MibTableRow
mscRtgDpnMidTputMetricEntry = _MscRtgDpnMidTputMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 331, 1)
)
mscRtgDpnMidTputMetricEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnMidIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnMidTputMetricIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnMidTputMetricEntry.setStatus("mandatory")


class _MscRtgDpnMidTputMetricIndex_Type(Integer32):
    """Custom type mscRtgDpnMidTputMetricIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscRtgDpnMidTputMetricIndex_Type.__name__ = "Integer32"
_MscRtgDpnMidTputMetricIndex_Object = MibTableColumn
mscRtgDpnMidTputMetricIndex = _MscRtgDpnMidTputMetricIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 331, 1, 1),
    _MscRtgDpnMidTputMetricIndex_Type()
)
mscRtgDpnMidTputMetricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnMidTputMetricIndex.setStatus("mandatory")


class _MscRtgDpnMidTputMetricValue_Type(Unsigned32):
    """Custom type mscRtgDpnMidTputMetricValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscRtgDpnMidTputMetricValue_Type.__name__ = "Unsigned32"
_MscRtgDpnMidTputMetricValue_Object = MibTableColumn
mscRtgDpnMidTputMetricValue = _MscRtgDpnMidTputMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 331, 1, 2),
    _MscRtgDpnMidTputMetricValue_Type()
)
mscRtgDpnMidTputMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnMidTputMetricValue.setStatus("mandatory")
_MscRtgDpnMidDelayPathTrafficProportionsTable_Object = MibTable
mscRtgDpnMidDelayPathTrafficProportionsTable = _MscRtgDpnMidDelayPathTrafficProportionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 332)
)
if mibBuilder.loadTexts:
    mscRtgDpnMidDelayPathTrafficProportionsTable.setStatus("mandatory")
_MscRtgDpnMidDelayPathTrafficProportionsEntry_Object = MibTableRow
mscRtgDpnMidDelayPathTrafficProportionsEntry = _MscRtgDpnMidDelayPathTrafficProportionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 332, 1)
)
mscRtgDpnMidDelayPathTrafficProportionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnMidIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnMidDelayPathTrafficProportionsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnMidDelayPathTrafficProportionsEntry.setStatus("mandatory")


class _MscRtgDpnMidDelayPathTrafficProportionsIndex_Type(Integer32):
    """Custom type mscRtgDpnMidDelayPathTrafficProportionsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscRtgDpnMidDelayPathTrafficProportionsIndex_Type.__name__ = "Integer32"
_MscRtgDpnMidDelayPathTrafficProportionsIndex_Object = MibTableColumn
mscRtgDpnMidDelayPathTrafficProportionsIndex = _MscRtgDpnMidDelayPathTrafficProportionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 332, 1, 1),
    _MscRtgDpnMidDelayPathTrafficProportionsIndex_Type()
)
mscRtgDpnMidDelayPathTrafficProportionsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnMidDelayPathTrafficProportionsIndex.setStatus("mandatory")


class _MscRtgDpnMidDelayPathTrafficProportionsValue_Type(Unsigned32):
    """Custom type mscRtgDpnMidDelayPathTrafficProportionsValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscRtgDpnMidDelayPathTrafficProportionsValue_Type.__name__ = "Unsigned32"
_MscRtgDpnMidDelayPathTrafficProportionsValue_Object = MibTableColumn
mscRtgDpnMidDelayPathTrafficProportionsValue = _MscRtgDpnMidDelayPathTrafficProportionsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 332, 1, 2),
    _MscRtgDpnMidDelayPathTrafficProportionsValue_Type()
)
mscRtgDpnMidDelayPathTrafficProportionsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnMidDelayPathTrafficProportionsValue.setStatus("mandatory")
_MscRtgDpnMidTputPathTrafficProportionsTable_Object = MibTable
mscRtgDpnMidTputPathTrafficProportionsTable = _MscRtgDpnMidTputPathTrafficProportionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 333)
)
if mibBuilder.loadTexts:
    mscRtgDpnMidTputPathTrafficProportionsTable.setStatus("mandatory")
_MscRtgDpnMidTputPathTrafficProportionsEntry_Object = MibTableRow
mscRtgDpnMidTputPathTrafficProportionsEntry = _MscRtgDpnMidTputPathTrafficProportionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 333, 1)
)
mscRtgDpnMidTputPathTrafficProportionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnMidIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnMidTputPathTrafficProportionsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnMidTputPathTrafficProportionsEntry.setStatus("mandatory")


class _MscRtgDpnMidTputPathTrafficProportionsIndex_Type(Integer32):
    """Custom type mscRtgDpnMidTputPathTrafficProportionsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscRtgDpnMidTputPathTrafficProportionsIndex_Type.__name__ = "Integer32"
_MscRtgDpnMidTputPathTrafficProportionsIndex_Object = MibTableColumn
mscRtgDpnMidTputPathTrafficProportionsIndex = _MscRtgDpnMidTputPathTrafficProportionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 333, 1, 1),
    _MscRtgDpnMidTputPathTrafficProportionsIndex_Type()
)
mscRtgDpnMidTputPathTrafficProportionsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnMidTputPathTrafficProportionsIndex.setStatus("mandatory")


class _MscRtgDpnMidTputPathTrafficProportionsValue_Type(Unsigned32):
    """Custom type mscRtgDpnMidTputPathTrafficProportionsValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscRtgDpnMidTputPathTrafficProportionsValue_Type.__name__ = "Unsigned32"
_MscRtgDpnMidTputPathTrafficProportionsValue_Object = MibTableColumn
mscRtgDpnMidTputPathTrafficProportionsValue = _MscRtgDpnMidTputPathTrafficProportionsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 3, 333, 1, 2),
    _MscRtgDpnMidTputPathTrafficProportionsValue_Type()
)
mscRtgDpnMidTputPathTrafficProportionsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnMidTputPathTrafficProportionsValue.setStatus("mandatory")
_MscRtgDpnCs_ObjectIdentity = ObjectIdentity
mscRtgDpnCs = _MscRtgDpnCs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4)
)
_MscRtgDpnCsRowStatusTable_Object = MibTable
mscRtgDpnCsRowStatusTable = _MscRtgDpnCsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 1)
)
if mibBuilder.loadTexts:
    mscRtgDpnCsRowStatusTable.setStatus("mandatory")
_MscRtgDpnCsRowStatusEntry_Object = MibTableRow
mscRtgDpnCsRowStatusEntry = _MscRtgDpnCsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 1, 1)
)
mscRtgDpnCsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnCsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnCsRowStatusEntry.setStatus("mandatory")
_MscRtgDpnCsRowStatus_Type = RowStatus
_MscRtgDpnCsRowStatus_Object = MibTableColumn
mscRtgDpnCsRowStatus = _MscRtgDpnCsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 1, 1, 1),
    _MscRtgDpnCsRowStatus_Type()
)
mscRtgDpnCsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnCsRowStatus.setStatus("mandatory")
_MscRtgDpnCsComponentName_Type = DisplayString
_MscRtgDpnCsComponentName_Object = MibTableColumn
mscRtgDpnCsComponentName = _MscRtgDpnCsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 1, 1, 2),
    _MscRtgDpnCsComponentName_Type()
)
mscRtgDpnCsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnCsComponentName.setStatus("mandatory")
_MscRtgDpnCsStorageType_Type = StorageType
_MscRtgDpnCsStorageType_Object = MibTableColumn
mscRtgDpnCsStorageType = _MscRtgDpnCsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 1, 1, 4),
    _MscRtgDpnCsStorageType_Type()
)
mscRtgDpnCsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnCsStorageType.setStatus("mandatory")


class _MscRtgDpnCsIndex_Type(Integer32):
    """Custom type mscRtgDpnCsIndex based on Integer32"""
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


_MscRtgDpnCsIndex_Type.__name__ = "Integer32"
_MscRtgDpnCsIndex_Object = MibTableColumn
mscRtgDpnCsIndex = _MscRtgDpnCsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 1, 1, 10),
    _MscRtgDpnCsIndex_Type()
)
mscRtgDpnCsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnCsIndex.setStatus("mandatory")
_MscRtgDpnCsDelayNextHopLinkGroupsTable_Object = MibTable
mscRtgDpnCsDelayNextHopLinkGroupsTable = _MscRtgDpnCsDelayNextHopLinkGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 230)
)
if mibBuilder.loadTexts:
    mscRtgDpnCsDelayNextHopLinkGroupsTable.setStatus("mandatory")
_MscRtgDpnCsDelayNextHopLinkGroupsEntry_Object = MibTableRow
mscRtgDpnCsDelayNextHopLinkGroupsEntry = _MscRtgDpnCsDelayNextHopLinkGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 230, 1)
)
mscRtgDpnCsDelayNextHopLinkGroupsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnCsDelayNextHopLinkGroupsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnCsDelayNextHopLinkGroupsEntry.setStatus("mandatory")


class _MscRtgDpnCsDelayNextHopLinkGroupsIndex_Type(Integer32):
    """Custom type mscRtgDpnCsDelayNextHopLinkGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscRtgDpnCsDelayNextHopLinkGroupsIndex_Type.__name__ = "Integer32"
_MscRtgDpnCsDelayNextHopLinkGroupsIndex_Object = MibTableColumn
mscRtgDpnCsDelayNextHopLinkGroupsIndex = _MscRtgDpnCsDelayNextHopLinkGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 230, 1, 1),
    _MscRtgDpnCsDelayNextHopLinkGroupsIndex_Type()
)
mscRtgDpnCsDelayNextHopLinkGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnCsDelayNextHopLinkGroupsIndex.setStatus("mandatory")
_MscRtgDpnCsDelayNextHopLinkGroupsValue_Type = RowPointer
_MscRtgDpnCsDelayNextHopLinkGroupsValue_Object = MibTableColumn
mscRtgDpnCsDelayNextHopLinkGroupsValue = _MscRtgDpnCsDelayNextHopLinkGroupsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 230, 1, 2),
    _MscRtgDpnCsDelayNextHopLinkGroupsValue_Type()
)
mscRtgDpnCsDelayNextHopLinkGroupsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnCsDelayNextHopLinkGroupsValue.setStatus("mandatory")
_MscRtgDpnCsTputNextHopLinkGroupsTable_Object = MibTable
mscRtgDpnCsTputNextHopLinkGroupsTable = _MscRtgDpnCsTputNextHopLinkGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 231)
)
if mibBuilder.loadTexts:
    mscRtgDpnCsTputNextHopLinkGroupsTable.setStatus("mandatory")
_MscRtgDpnCsTputNextHopLinkGroupsEntry_Object = MibTableRow
mscRtgDpnCsTputNextHopLinkGroupsEntry = _MscRtgDpnCsTputNextHopLinkGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 231, 1)
)
mscRtgDpnCsTputNextHopLinkGroupsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnCsTputNextHopLinkGroupsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnCsTputNextHopLinkGroupsEntry.setStatus("mandatory")


class _MscRtgDpnCsTputNextHopLinkGroupsIndex_Type(Integer32):
    """Custom type mscRtgDpnCsTputNextHopLinkGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscRtgDpnCsTputNextHopLinkGroupsIndex_Type.__name__ = "Integer32"
_MscRtgDpnCsTputNextHopLinkGroupsIndex_Object = MibTableColumn
mscRtgDpnCsTputNextHopLinkGroupsIndex = _MscRtgDpnCsTputNextHopLinkGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 231, 1, 1),
    _MscRtgDpnCsTputNextHopLinkGroupsIndex_Type()
)
mscRtgDpnCsTputNextHopLinkGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnCsTputNextHopLinkGroupsIndex.setStatus("mandatory")
_MscRtgDpnCsTputNextHopLinkGroupsValue_Type = RowPointer
_MscRtgDpnCsTputNextHopLinkGroupsValue_Object = MibTableColumn
mscRtgDpnCsTputNextHopLinkGroupsValue = _MscRtgDpnCsTputNextHopLinkGroupsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 231, 1, 2),
    _MscRtgDpnCsTputNextHopLinkGroupsValue_Type()
)
mscRtgDpnCsTputNextHopLinkGroupsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnCsTputNextHopLinkGroupsValue.setStatus("mandatory")
_MscRtgDpnCsDelayMetricTable_Object = MibTable
mscRtgDpnCsDelayMetricTable = _MscRtgDpnCsDelayMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 334)
)
if mibBuilder.loadTexts:
    mscRtgDpnCsDelayMetricTable.setStatus("mandatory")
_MscRtgDpnCsDelayMetricEntry_Object = MibTableRow
mscRtgDpnCsDelayMetricEntry = _MscRtgDpnCsDelayMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 334, 1)
)
mscRtgDpnCsDelayMetricEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnCsDelayMetricIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnCsDelayMetricEntry.setStatus("mandatory")


class _MscRtgDpnCsDelayMetricIndex_Type(Integer32):
    """Custom type mscRtgDpnCsDelayMetricIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscRtgDpnCsDelayMetricIndex_Type.__name__ = "Integer32"
_MscRtgDpnCsDelayMetricIndex_Object = MibTableColumn
mscRtgDpnCsDelayMetricIndex = _MscRtgDpnCsDelayMetricIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 334, 1, 1),
    _MscRtgDpnCsDelayMetricIndex_Type()
)
mscRtgDpnCsDelayMetricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnCsDelayMetricIndex.setStatus("mandatory")


class _MscRtgDpnCsDelayMetricValue_Type(Unsigned32):
    """Custom type mscRtgDpnCsDelayMetricValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscRtgDpnCsDelayMetricValue_Type.__name__ = "Unsigned32"
_MscRtgDpnCsDelayMetricValue_Object = MibTableColumn
mscRtgDpnCsDelayMetricValue = _MscRtgDpnCsDelayMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 334, 1, 2),
    _MscRtgDpnCsDelayMetricValue_Type()
)
mscRtgDpnCsDelayMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnCsDelayMetricValue.setStatus("mandatory")
_MscRtgDpnCsTputMetricTable_Object = MibTable
mscRtgDpnCsTputMetricTable = _MscRtgDpnCsTputMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 335)
)
if mibBuilder.loadTexts:
    mscRtgDpnCsTputMetricTable.setStatus("mandatory")
_MscRtgDpnCsTputMetricEntry_Object = MibTableRow
mscRtgDpnCsTputMetricEntry = _MscRtgDpnCsTputMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 335, 1)
)
mscRtgDpnCsTputMetricEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnCsTputMetricIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnCsTputMetricEntry.setStatus("mandatory")


class _MscRtgDpnCsTputMetricIndex_Type(Integer32):
    """Custom type mscRtgDpnCsTputMetricIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscRtgDpnCsTputMetricIndex_Type.__name__ = "Integer32"
_MscRtgDpnCsTputMetricIndex_Object = MibTableColumn
mscRtgDpnCsTputMetricIndex = _MscRtgDpnCsTputMetricIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 335, 1, 1),
    _MscRtgDpnCsTputMetricIndex_Type()
)
mscRtgDpnCsTputMetricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnCsTputMetricIndex.setStatus("mandatory")


class _MscRtgDpnCsTputMetricValue_Type(Unsigned32):
    """Custom type mscRtgDpnCsTputMetricValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscRtgDpnCsTputMetricValue_Type.__name__ = "Unsigned32"
_MscRtgDpnCsTputMetricValue_Object = MibTableColumn
mscRtgDpnCsTputMetricValue = _MscRtgDpnCsTputMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 335, 1, 2),
    _MscRtgDpnCsTputMetricValue_Type()
)
mscRtgDpnCsTputMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnCsTputMetricValue.setStatus("mandatory")
_MscRtgDpnCsDelayPathTrafficProportionsTable_Object = MibTable
mscRtgDpnCsDelayPathTrafficProportionsTable = _MscRtgDpnCsDelayPathTrafficProportionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 336)
)
if mibBuilder.loadTexts:
    mscRtgDpnCsDelayPathTrafficProportionsTable.setStatus("mandatory")
_MscRtgDpnCsDelayPathTrafficProportionsEntry_Object = MibTableRow
mscRtgDpnCsDelayPathTrafficProportionsEntry = _MscRtgDpnCsDelayPathTrafficProportionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 336, 1)
)
mscRtgDpnCsDelayPathTrafficProportionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnCsDelayPathTrafficProportionsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnCsDelayPathTrafficProportionsEntry.setStatus("mandatory")


class _MscRtgDpnCsDelayPathTrafficProportionsIndex_Type(Integer32):
    """Custom type mscRtgDpnCsDelayPathTrafficProportionsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscRtgDpnCsDelayPathTrafficProportionsIndex_Type.__name__ = "Integer32"
_MscRtgDpnCsDelayPathTrafficProportionsIndex_Object = MibTableColumn
mscRtgDpnCsDelayPathTrafficProportionsIndex = _MscRtgDpnCsDelayPathTrafficProportionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 336, 1, 1),
    _MscRtgDpnCsDelayPathTrafficProportionsIndex_Type()
)
mscRtgDpnCsDelayPathTrafficProportionsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnCsDelayPathTrafficProportionsIndex.setStatus("mandatory")


class _MscRtgDpnCsDelayPathTrafficProportionsValue_Type(Unsigned32):
    """Custom type mscRtgDpnCsDelayPathTrafficProportionsValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscRtgDpnCsDelayPathTrafficProportionsValue_Type.__name__ = "Unsigned32"
_MscRtgDpnCsDelayPathTrafficProportionsValue_Object = MibTableColumn
mscRtgDpnCsDelayPathTrafficProportionsValue = _MscRtgDpnCsDelayPathTrafficProportionsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 336, 1, 2),
    _MscRtgDpnCsDelayPathTrafficProportionsValue_Type()
)
mscRtgDpnCsDelayPathTrafficProportionsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnCsDelayPathTrafficProportionsValue.setStatus("mandatory")
_MscRtgDpnCsTputPathTrafficProportionsTable_Object = MibTable
mscRtgDpnCsTputPathTrafficProportionsTable = _MscRtgDpnCsTputPathTrafficProportionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 337)
)
if mibBuilder.loadTexts:
    mscRtgDpnCsTputPathTrafficProportionsTable.setStatus("mandatory")
_MscRtgDpnCsTputPathTrafficProportionsEntry_Object = MibTableRow
mscRtgDpnCsTputPathTrafficProportionsEntry = _MscRtgDpnCsTputPathTrafficProportionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 337, 1)
)
mscRtgDpnCsTputPathTrafficProportionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnCsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnCsTputPathTrafficProportionsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnCsTputPathTrafficProportionsEntry.setStatus("mandatory")


class _MscRtgDpnCsTputPathTrafficProportionsIndex_Type(Integer32):
    """Custom type mscRtgDpnCsTputPathTrafficProportionsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscRtgDpnCsTputPathTrafficProportionsIndex_Type.__name__ = "Integer32"
_MscRtgDpnCsTputPathTrafficProportionsIndex_Object = MibTableColumn
mscRtgDpnCsTputPathTrafficProportionsIndex = _MscRtgDpnCsTputPathTrafficProportionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 337, 1, 1),
    _MscRtgDpnCsTputPathTrafficProportionsIndex_Type()
)
mscRtgDpnCsTputPathTrafficProportionsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnCsTputPathTrafficProportionsIndex.setStatus("mandatory")


class _MscRtgDpnCsTputPathTrafficProportionsValue_Type(Unsigned32):
    """Custom type mscRtgDpnCsTputPathTrafficProportionsValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscRtgDpnCsTputPathTrafficProportionsValue_Type.__name__ = "Unsigned32"
_MscRtgDpnCsTputPathTrafficProportionsValue_Object = MibTableColumn
mscRtgDpnCsTputPathTrafficProportionsValue = _MscRtgDpnCsTputPathTrafficProportionsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 4, 337, 1, 2),
    _MscRtgDpnCsTputPathTrafficProportionsValue_Type()
)
mscRtgDpnCsTputPathTrafficProportionsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnCsTputPathTrafficProportionsValue.setStatus("mandatory")
_MscRtgDpnLg_ObjectIdentity = ObjectIdentity
mscRtgDpnLg = _MscRtgDpnLg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 5)
)
_MscRtgDpnLgRowStatusTable_Object = MibTable
mscRtgDpnLgRowStatusTable = _MscRtgDpnLgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 5, 1)
)
if mibBuilder.loadTexts:
    mscRtgDpnLgRowStatusTable.setStatus("mandatory")
_MscRtgDpnLgRowStatusEntry_Object = MibTableRow
mscRtgDpnLgRowStatusEntry = _MscRtgDpnLgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 5, 1, 1)
)
mscRtgDpnLgRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnLgIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnLgRowStatusEntry.setStatus("mandatory")
_MscRtgDpnLgRowStatus_Type = RowStatus
_MscRtgDpnLgRowStatus_Object = MibTableColumn
mscRtgDpnLgRowStatus = _MscRtgDpnLgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 5, 1, 1, 1),
    _MscRtgDpnLgRowStatus_Type()
)
mscRtgDpnLgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnLgRowStatus.setStatus("mandatory")
_MscRtgDpnLgComponentName_Type = DisplayString
_MscRtgDpnLgComponentName_Object = MibTableColumn
mscRtgDpnLgComponentName = _MscRtgDpnLgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 5, 1, 1, 2),
    _MscRtgDpnLgComponentName_Type()
)
mscRtgDpnLgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnLgComponentName.setStatus("mandatory")
_MscRtgDpnLgStorageType_Type = StorageType
_MscRtgDpnLgStorageType_Object = MibTableColumn
mscRtgDpnLgStorageType = _MscRtgDpnLgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 5, 1, 1, 4),
    _MscRtgDpnLgStorageType_Type()
)
mscRtgDpnLgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnLgStorageType.setStatus("mandatory")


class _MscRtgDpnLgIndex_Type(AsciiStringIndex):
    """Custom type mscRtgDpnLgIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_MscRtgDpnLgIndex_Type.__name__ = "AsciiStringIndex"
_MscRtgDpnLgIndex_Object = MibTableColumn
mscRtgDpnLgIndex = _MscRtgDpnLgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 5, 1, 1, 10),
    _MscRtgDpnLgIndex_Type()
)
mscRtgDpnLgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnLgIndex.setStatus("mandatory")
_MscRtgDpnLgOperTable_Object = MibTable
mscRtgDpnLgOperTable = _MscRtgDpnLgOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 5, 3)
)
if mibBuilder.loadTexts:
    mscRtgDpnLgOperTable.setStatus("mandatory")
_MscRtgDpnLgOperEntry_Object = MibTableRow
mscRtgDpnLgOperEntry = _MscRtgDpnLgOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 5, 3, 1)
)
mscRtgDpnLgOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnLgIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnLgOperEntry.setStatus("mandatory")


class _MscRtgDpnLgFarEndType_Type(Integer32):
    """Custom type mscRtgDpnLgFarEndType based on Integer32"""
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


_MscRtgDpnLgFarEndType_Type.__name__ = "Integer32"
_MscRtgDpnLgFarEndType_Object = MibTableColumn
mscRtgDpnLgFarEndType = _MscRtgDpnLgFarEndType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 5, 3, 1, 1),
    _MscRtgDpnLgFarEndType_Type()
)
mscRtgDpnLgFarEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnLgFarEndType.setStatus("mandatory")


class _MscRtgDpnLgFarEndRid_Type(Unsigned32):
    """Custom type mscRtgDpnLgFarEndRid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 126),
    )


_MscRtgDpnLgFarEndRid_Type.__name__ = "Unsigned32"
_MscRtgDpnLgFarEndRid_Object = MibTableColumn
mscRtgDpnLgFarEndRid = _MscRtgDpnLgFarEndRid_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 5, 3, 1, 2),
    _MscRtgDpnLgFarEndRid_Type()
)
mscRtgDpnLgFarEndRid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnLgFarEndRid.setStatus("mandatory")


class _MscRtgDpnLgFarEndMid_Type(Unsigned32):
    """Custom type mscRtgDpnLgFarEndMid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1910),
    )


_MscRtgDpnLgFarEndMid_Type.__name__ = "Unsigned32"
_MscRtgDpnLgFarEndMid_Object = MibTableColumn
mscRtgDpnLgFarEndMid = _MscRtgDpnLgFarEndMid_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 5, 3, 1, 3),
    _MscRtgDpnLgFarEndMid_Type()
)
mscRtgDpnLgFarEndMid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnLgFarEndMid.setStatus("mandatory")


class _MscRtgDpnLgDelayMetric_Type(Unsigned32):
    """Custom type mscRtgDpnLgDelayMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MscRtgDpnLgDelayMetric_Type.__name__ = "Unsigned32"
_MscRtgDpnLgDelayMetric_Object = MibTableColumn
mscRtgDpnLgDelayMetric = _MscRtgDpnLgDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 5, 3, 1, 4),
    _MscRtgDpnLgDelayMetric_Type()
)
mscRtgDpnLgDelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnLgDelayMetric.setStatus("mandatory")


class _MscRtgDpnLgTputMetric_Type(Unsigned32):
    """Custom type mscRtgDpnLgTputMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MscRtgDpnLgTputMetric_Type.__name__ = "Unsigned32"
_MscRtgDpnLgTputMetric_Object = MibTableColumn
mscRtgDpnLgTputMetric = _MscRtgDpnLgTputMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 5, 3, 1, 5),
    _MscRtgDpnLgTputMetric_Type()
)
mscRtgDpnLgTputMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnLgTputMetric.setStatus("mandatory")
_MscRtgDpnLpStats_ObjectIdentity = ObjectIdentity
mscRtgDpnLpStats = _MscRtgDpnLpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 6)
)
_MscRtgDpnLpStatsRowStatusTable_Object = MibTable
mscRtgDpnLpStatsRowStatusTable = _MscRtgDpnLpStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 6, 1)
)
if mibBuilder.loadTexts:
    mscRtgDpnLpStatsRowStatusTable.setStatus("mandatory")
_MscRtgDpnLpStatsRowStatusEntry_Object = MibTableRow
mscRtgDpnLpStatsRowStatusEntry = _MscRtgDpnLpStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 6, 1, 1)
)
mscRtgDpnLpStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnLpStatsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnLpStatsRowStatusEntry.setStatus("mandatory")
_MscRtgDpnLpStatsRowStatus_Type = RowStatus
_MscRtgDpnLpStatsRowStatus_Object = MibTableColumn
mscRtgDpnLpStatsRowStatus = _MscRtgDpnLpStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 6, 1, 1, 1),
    _MscRtgDpnLpStatsRowStatus_Type()
)
mscRtgDpnLpStatsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnLpStatsRowStatus.setStatus("mandatory")
_MscRtgDpnLpStatsComponentName_Type = DisplayString
_MscRtgDpnLpStatsComponentName_Object = MibTableColumn
mscRtgDpnLpStatsComponentName = _MscRtgDpnLpStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 6, 1, 1, 2),
    _MscRtgDpnLpStatsComponentName_Type()
)
mscRtgDpnLpStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnLpStatsComponentName.setStatus("mandatory")
_MscRtgDpnLpStatsStorageType_Type = StorageType
_MscRtgDpnLpStatsStorageType_Object = MibTableColumn
mscRtgDpnLpStatsStorageType = _MscRtgDpnLpStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 6, 1, 1, 4),
    _MscRtgDpnLpStatsStorageType_Type()
)
mscRtgDpnLpStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnLpStatsStorageType.setStatus("mandatory")


class _MscRtgDpnLpStatsIndex_Type(Integer32):
    """Custom type mscRtgDpnLpStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscRtgDpnLpStatsIndex_Type.__name__ = "Integer32"
_MscRtgDpnLpStatsIndex_Object = MibTableColumn
mscRtgDpnLpStatsIndex = _MscRtgDpnLpStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 6, 1, 1, 10),
    _MscRtgDpnLpStatsIndex_Type()
)
mscRtgDpnLpStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnLpStatsIndex.setStatus("mandatory")
_MscRtgDpnLpStatsFwdStatsTable_Object = MibTable
mscRtgDpnLpStatsFwdStatsTable = _MscRtgDpnLpStatsFwdStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 6, 10)
)
if mibBuilder.loadTexts:
    mscRtgDpnLpStatsFwdStatsTable.setStatus("mandatory")
_MscRtgDpnLpStatsFwdStatsEntry_Object = MibTableRow
mscRtgDpnLpStatsFwdStatsEntry = _MscRtgDpnLpStatsFwdStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 6, 10, 1)
)
mscRtgDpnLpStatsFwdStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnLpStatsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnLpStatsFwdStatsEntry.setStatus("mandatory")
_MscRtgDpnLpStatsTotalPackets_Type = PassportCounter64
_MscRtgDpnLpStatsTotalPackets_Object = MibTableColumn
mscRtgDpnLpStatsTotalPackets = _MscRtgDpnLpStatsTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 6, 10, 1, 1),
    _MscRtgDpnLpStatsTotalPackets_Type()
)
mscRtgDpnLpStatsTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnLpStatsTotalPackets.setStatus("mandatory")
_MscRtgDpnLpStatsThroughputPackets_Type = PassportCounter64
_MscRtgDpnLpStatsThroughputPackets_Object = MibTableColumn
mscRtgDpnLpStatsThroughputPackets = _MscRtgDpnLpStatsThroughputPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 6, 10, 1, 2),
    _MscRtgDpnLpStatsThroughputPackets_Type()
)
mscRtgDpnLpStatsThroughputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnLpStatsThroughputPackets.setStatus("mandatory")
_MscRtgDpnLpStatsDelayPackets_Type = PassportCounter64
_MscRtgDpnLpStatsDelayPackets_Object = MibTableColumn
mscRtgDpnLpStatsDelayPackets = _MscRtgDpnLpStatsDelayPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 6, 10, 1, 3),
    _MscRtgDpnLpStatsDelayPackets_Type()
)
mscRtgDpnLpStatsDelayPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnLpStatsDelayPackets.setStatus("mandatory")
_MscRtgDpnLpStatsNormalReliabilityPackets_Type = PassportCounter64
_MscRtgDpnLpStatsNormalReliabilityPackets_Object = MibTableColumn
mscRtgDpnLpStatsNormalReliabilityPackets = _MscRtgDpnLpStatsNormalReliabilityPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 6, 10, 1, 4),
    _MscRtgDpnLpStatsNormalReliabilityPackets_Type()
)
mscRtgDpnLpStatsNormalReliabilityPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnLpStatsNormalReliabilityPackets.setStatus("mandatory")
_MscRtgDpnLpStatsHighReliabilityPackets_Type = PassportCounter64
_MscRtgDpnLpStatsHighReliabilityPackets_Object = MibTableColumn
mscRtgDpnLpStatsHighReliabilityPackets = _MscRtgDpnLpStatsHighReliabilityPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 6, 10, 1, 5),
    _MscRtgDpnLpStatsHighReliabilityPackets_Type()
)
mscRtgDpnLpStatsHighReliabilityPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnLpStatsHighReliabilityPackets.setStatus("mandatory")
_MscRtgDpnLpStatsDiscardNoRoute_Type = PassportCounter64
_MscRtgDpnLpStatsDiscardNoRoute_Object = MibTableColumn
mscRtgDpnLpStatsDiscardNoRoute = _MscRtgDpnLpStatsDiscardNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 6, 10, 1, 6),
    _MscRtgDpnLpStatsDiscardNoRoute_Type()
)
mscRtgDpnLpStatsDiscardNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnLpStatsDiscardNoRoute.setStatus("mandatory")
_MscRtgDpnLpStatsInterruptingPackets_Type = PassportCounter64
_MscRtgDpnLpStatsInterruptingPackets_Object = MibTableColumn
mscRtgDpnLpStatsInterruptingPackets = _MscRtgDpnLpStatsInterruptingPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 6, 10, 1, 7),
    _MscRtgDpnLpStatsInterruptingPackets_Type()
)
mscRtgDpnLpStatsInterruptingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnLpStatsInterruptingPackets.setStatus("mandatory")
_MscRtgDpnLpStatsDiscardLpCongested_Type = PassportCounter64
_MscRtgDpnLpStatsDiscardLpCongested_Object = MibTableColumn
mscRtgDpnLpStatsDiscardLpCongested = _MscRtgDpnLpStatsDiscardLpCongested_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 6, 10, 1, 8),
    _MscRtgDpnLpStatsDiscardLpCongested_Type()
)
mscRtgDpnLpStatsDiscardLpCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnLpStatsDiscardLpCongested.setStatus("mandatory")
_MscRtgDpnRidFilter_ObjectIdentity = ObjectIdentity
mscRtgDpnRidFilter = _MscRtgDpnRidFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 7)
)
_MscRtgDpnRidFilterRowStatusTable_Object = MibTable
mscRtgDpnRidFilterRowStatusTable = _MscRtgDpnRidFilterRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 7, 1)
)
if mibBuilder.loadTexts:
    mscRtgDpnRidFilterRowStatusTable.setStatus("mandatory")
_MscRtgDpnRidFilterRowStatusEntry_Object = MibTableRow
mscRtgDpnRidFilterRowStatusEntry = _MscRtgDpnRidFilterRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 7, 1, 1)
)
mscRtgDpnRidFilterRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnRidFilterIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnRidFilterRowStatusEntry.setStatus("mandatory")
_MscRtgDpnRidFilterRowStatus_Type = RowStatus
_MscRtgDpnRidFilterRowStatus_Object = MibTableColumn
mscRtgDpnRidFilterRowStatus = _MscRtgDpnRidFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 7, 1, 1, 1),
    _MscRtgDpnRidFilterRowStatus_Type()
)
mscRtgDpnRidFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgDpnRidFilterRowStatus.setStatus("mandatory")
_MscRtgDpnRidFilterComponentName_Type = DisplayString
_MscRtgDpnRidFilterComponentName_Object = MibTableColumn
mscRtgDpnRidFilterComponentName = _MscRtgDpnRidFilterComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 7, 1, 1, 2),
    _MscRtgDpnRidFilterComponentName_Type()
)
mscRtgDpnRidFilterComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnRidFilterComponentName.setStatus("mandatory")
_MscRtgDpnRidFilterStorageType_Type = StorageType
_MscRtgDpnRidFilterStorageType_Object = MibTableColumn
mscRtgDpnRidFilterStorageType = _MscRtgDpnRidFilterStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 7, 1, 1, 4),
    _MscRtgDpnRidFilterStorageType_Type()
)
mscRtgDpnRidFilterStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnRidFilterStorageType.setStatus("mandatory")


class _MscRtgDpnRidFilterIndex_Type(Integer32):
    """Custom type mscRtgDpnRidFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 126),
    )


_MscRtgDpnRidFilterIndex_Type.__name__ = "Integer32"
_MscRtgDpnRidFilterIndex_Object = MibTableColumn
mscRtgDpnRidFilterIndex = _MscRtgDpnRidFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 7, 1, 1, 10),
    _MscRtgDpnRidFilterIndex_Type()
)
mscRtgDpnRidFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnRidFilterIndex.setStatus("mandatory")
_MscRtgDpnRidFilterImportRidListTable_Object = MibTable
mscRtgDpnRidFilterImportRidListTable = _MscRtgDpnRidFilterImportRidListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 7, 303)
)
if mibBuilder.loadTexts:
    mscRtgDpnRidFilterImportRidListTable.setStatus("mandatory")
_MscRtgDpnRidFilterImportRidListEntry_Object = MibTableRow
mscRtgDpnRidFilterImportRidListEntry = _MscRtgDpnRidFilterImportRidListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 7, 303, 1)
)
mscRtgDpnRidFilterImportRidListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnRidFilterIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnRidFilterImportRidListValue"),
)
if mibBuilder.loadTexts:
    mscRtgDpnRidFilterImportRidListEntry.setStatus("mandatory")


class _MscRtgDpnRidFilterImportRidListValue_Type(Integer32):
    """Custom type mscRtgDpnRidFilterImportRidListValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MscRtgDpnRidFilterImportRidListValue_Type.__name__ = "Integer32"
_MscRtgDpnRidFilterImportRidListValue_Object = MibTableColumn
mscRtgDpnRidFilterImportRidListValue = _MscRtgDpnRidFilterImportRidListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 7, 303, 1, 1),
    _MscRtgDpnRidFilterImportRidListValue_Type()
)
mscRtgDpnRidFilterImportRidListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgDpnRidFilterImportRidListValue.setStatus("mandatory")
_MscRtgDpnRidFilterImportRidListRowStatus_Type = RowStatus
_MscRtgDpnRidFilterImportRidListRowStatus_Object = MibTableColumn
mscRtgDpnRidFilterImportRidListRowStatus = _MscRtgDpnRidFilterImportRidListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 7, 303, 1, 2),
    _MscRtgDpnRidFilterImportRidListRowStatus_Type()
)
mscRtgDpnRidFilterImportRidListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscRtgDpnRidFilterImportRidListRowStatus.setStatus("mandatory")
_MscRtgDpnRidFilterExportRidListTable_Object = MibTable
mscRtgDpnRidFilterExportRidListTable = _MscRtgDpnRidFilterExportRidListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 7, 304)
)
if mibBuilder.loadTexts:
    mscRtgDpnRidFilterExportRidListTable.setStatus("mandatory")
_MscRtgDpnRidFilterExportRidListEntry_Object = MibTableRow
mscRtgDpnRidFilterExportRidListEntry = _MscRtgDpnRidFilterExportRidListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 7, 304, 1)
)
mscRtgDpnRidFilterExportRidListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnRidFilterIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnRidFilterExportRidListValue"),
)
if mibBuilder.loadTexts:
    mscRtgDpnRidFilterExportRidListEntry.setStatus("mandatory")


class _MscRtgDpnRidFilterExportRidListValue_Type(Integer32):
    """Custom type mscRtgDpnRidFilterExportRidListValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MscRtgDpnRidFilterExportRidListValue_Type.__name__ = "Integer32"
_MscRtgDpnRidFilterExportRidListValue_Object = MibTableColumn
mscRtgDpnRidFilterExportRidListValue = _MscRtgDpnRidFilterExportRidListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 7, 304, 1, 1),
    _MscRtgDpnRidFilterExportRidListValue_Type()
)
mscRtgDpnRidFilterExportRidListValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgDpnRidFilterExportRidListValue.setStatus("mandatory")
_MscRtgDpnRidFilterExportRidListRowStatus_Type = RowStatus
_MscRtgDpnRidFilterExportRidListRowStatus_Object = MibTableColumn
mscRtgDpnRidFilterExportRidListRowStatus = _MscRtgDpnRidFilterExportRidListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 7, 304, 1, 2),
    _MscRtgDpnRidFilterExportRidListRowStatus_Type()
)
mscRtgDpnRidFilterExportRidListRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscRtgDpnRidFilterExportRidListRowStatus.setStatus("mandatory")
_MscRtgDpnArt_ObjectIdentity = ObjectIdentity
mscRtgDpnArt = _MscRtgDpnArt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9)
)
_MscRtgDpnArtRowStatusTable_Object = MibTable
mscRtgDpnArtRowStatusTable = _MscRtgDpnArtRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 1)
)
if mibBuilder.loadTexts:
    mscRtgDpnArtRowStatusTable.setStatus("mandatory")
_MscRtgDpnArtRowStatusEntry_Object = MibTableRow
mscRtgDpnArtRowStatusEntry = _MscRtgDpnArtRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 1, 1)
)
mscRtgDpnArtRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnArtIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnArtRowStatusEntry.setStatus("mandatory")
_MscRtgDpnArtRowStatus_Type = RowStatus
_MscRtgDpnArtRowStatus_Object = MibTableColumn
mscRtgDpnArtRowStatus = _MscRtgDpnArtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 1, 1, 1),
    _MscRtgDpnArtRowStatus_Type()
)
mscRtgDpnArtRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnArtRowStatus.setStatus("mandatory")
_MscRtgDpnArtComponentName_Type = DisplayString
_MscRtgDpnArtComponentName_Object = MibTableColumn
mscRtgDpnArtComponentName = _MscRtgDpnArtComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 1, 1, 2),
    _MscRtgDpnArtComponentName_Type()
)
mscRtgDpnArtComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnArtComponentName.setStatus("mandatory")
_MscRtgDpnArtStorageType_Type = StorageType
_MscRtgDpnArtStorageType_Object = MibTableColumn
mscRtgDpnArtStorageType = _MscRtgDpnArtStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 1, 1, 4),
    _MscRtgDpnArtStorageType_Type()
)
mscRtgDpnArtStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnArtStorageType.setStatus("mandatory")
_MscRtgDpnArtIndex_Type = NonReplicated
_MscRtgDpnArtIndex_Object = MibTableColumn
mscRtgDpnArtIndex = _MscRtgDpnArtIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 1, 1, 10),
    _MscRtgDpnArtIndex_Type()
)
mscRtgDpnArtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnArtIndex.setStatus("mandatory")
_MscRtgDpnArtErrRid_ObjectIdentity = ObjectIdentity
mscRtgDpnArtErrRid = _MscRtgDpnArtErrRid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 2)
)
_MscRtgDpnArtErrRidRowStatusTable_Object = MibTable
mscRtgDpnArtErrRidRowStatusTable = _MscRtgDpnArtErrRidRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 2, 1)
)
if mibBuilder.loadTexts:
    mscRtgDpnArtErrRidRowStatusTable.setStatus("mandatory")
_MscRtgDpnArtErrRidRowStatusEntry_Object = MibTableRow
mscRtgDpnArtErrRidRowStatusEntry = _MscRtgDpnArtErrRidRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 2, 1, 1)
)
mscRtgDpnArtErrRidRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnArtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnArtErrRidIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnArtErrRidRowStatusEntry.setStatus("mandatory")
_MscRtgDpnArtErrRidRowStatus_Type = RowStatus
_MscRtgDpnArtErrRidRowStatus_Object = MibTableColumn
mscRtgDpnArtErrRidRowStatus = _MscRtgDpnArtErrRidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 2, 1, 1, 1),
    _MscRtgDpnArtErrRidRowStatus_Type()
)
mscRtgDpnArtErrRidRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnArtErrRidRowStatus.setStatus("mandatory")
_MscRtgDpnArtErrRidComponentName_Type = DisplayString
_MscRtgDpnArtErrRidComponentName_Object = MibTableColumn
mscRtgDpnArtErrRidComponentName = _MscRtgDpnArtErrRidComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 2, 1, 1, 2),
    _MscRtgDpnArtErrRidComponentName_Type()
)
mscRtgDpnArtErrRidComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnArtErrRidComponentName.setStatus("mandatory")
_MscRtgDpnArtErrRidStorageType_Type = StorageType
_MscRtgDpnArtErrRidStorageType_Object = MibTableColumn
mscRtgDpnArtErrRidStorageType = _MscRtgDpnArtErrRidStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 2, 1, 1, 4),
    _MscRtgDpnArtErrRidStorageType_Type()
)
mscRtgDpnArtErrRidStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnArtErrRidStorageType.setStatus("mandatory")


class _MscRtgDpnArtErrRidIndex_Type(Integer32):
    """Custom type mscRtgDpnArtErrRidIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MscRtgDpnArtErrRidIndex_Type.__name__ = "Integer32"
_MscRtgDpnArtErrRidIndex_Object = MibTableColumn
mscRtgDpnArtErrRidIndex = _MscRtgDpnArtErrRidIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 2, 1, 1, 10),
    _MscRtgDpnArtErrRidIndex_Type()
)
mscRtgDpnArtErrRidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnArtErrRidIndex.setStatus("mandatory")
_MscRtgDpnArtErrRidOperTable_Object = MibTable
mscRtgDpnArtErrRidOperTable = _MscRtgDpnArtErrRidOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 2, 10)
)
if mibBuilder.loadTexts:
    mscRtgDpnArtErrRidOperTable.setStatus("mandatory")
_MscRtgDpnArtErrRidOperEntry_Object = MibTableRow
mscRtgDpnArtErrRidOperEntry = _MscRtgDpnArtErrRidOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 2, 10, 1)
)
mscRtgDpnArtErrRidOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnArtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnArtErrRidIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnArtErrRidOperEntry.setStatus("mandatory")


class _MscRtgDpnArtErrRidDelayCosErrType_Type(Integer32):
    """Custom type mscRtgDpnArtErrRidDelayCosErrType based on Integer32"""
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
        *(("loop", 2),
          ("noError", 0),
          ("timeout", 1))
    )


_MscRtgDpnArtErrRidDelayCosErrType_Type.__name__ = "Integer32"
_MscRtgDpnArtErrRidDelayCosErrType_Object = MibTableColumn
mscRtgDpnArtErrRidDelayCosErrType = _MscRtgDpnArtErrRidDelayCosErrType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 2, 10, 1, 1),
    _MscRtgDpnArtErrRidDelayCosErrType_Type()
)
mscRtgDpnArtErrRidDelayCosErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnArtErrRidDelayCosErrType.setStatus("mandatory")


class _MscRtgDpnArtErrRidThroughputCosErrType_Type(Integer32):
    """Custom type mscRtgDpnArtErrRidThroughputCosErrType based on Integer32"""
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
        *(("loop", 2),
          ("noError", 0),
          ("timeout", 1))
    )


_MscRtgDpnArtErrRidThroughputCosErrType_Type.__name__ = "Integer32"
_MscRtgDpnArtErrRidThroughputCosErrType_Object = MibTableColumn
mscRtgDpnArtErrRidThroughputCosErrType = _MscRtgDpnArtErrRidThroughputCosErrType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 2, 10, 1, 2),
    _MscRtgDpnArtErrRidThroughputCosErrType_Type()
)
mscRtgDpnArtErrRidThroughputCosErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnArtErrRidThroughputCosErrType.setStatus("mandatory")
_MscRtgDpnArtErrRidDelayErrPathTable_Object = MibTable
mscRtgDpnArtErrRidDelayErrPathTable = _MscRtgDpnArtErrRidDelayErrPathTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 2, 688)
)
if mibBuilder.loadTexts:
    mscRtgDpnArtErrRidDelayErrPathTable.setStatus("mandatory")
_MscRtgDpnArtErrRidDelayErrPathEntry_Object = MibTableRow
mscRtgDpnArtErrRidDelayErrPathEntry = _MscRtgDpnArtErrRidDelayErrPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 2, 688, 1)
)
mscRtgDpnArtErrRidDelayErrPathEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnArtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnArtErrRidIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnArtErrRidDelayErrPathValue"),
)
if mibBuilder.loadTexts:
    mscRtgDpnArtErrRidDelayErrPathEntry.setStatus("mandatory")


class _MscRtgDpnArtErrRidDelayErrPathValue_Type(AsciiString):
    """Custom type mscRtgDpnArtErrRidDelayErrPathValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscRtgDpnArtErrRidDelayErrPathValue_Type.__name__ = "AsciiString"
_MscRtgDpnArtErrRidDelayErrPathValue_Object = MibTableColumn
mscRtgDpnArtErrRidDelayErrPathValue = _MscRtgDpnArtErrRidDelayErrPathValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 2, 688, 1, 1),
    _MscRtgDpnArtErrRidDelayErrPathValue_Type()
)
mscRtgDpnArtErrRidDelayErrPathValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnArtErrRidDelayErrPathValue.setStatus("mandatory")
_MscRtgDpnArtErrRidTputErrPathTable_Object = MibTable
mscRtgDpnArtErrRidTputErrPathTable = _MscRtgDpnArtErrRidTputErrPathTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 2, 689)
)
if mibBuilder.loadTexts:
    mscRtgDpnArtErrRidTputErrPathTable.setStatus("mandatory")
_MscRtgDpnArtErrRidTputErrPathEntry_Object = MibTableRow
mscRtgDpnArtErrRidTputErrPathEntry = _MscRtgDpnArtErrRidTputErrPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 2, 689, 1)
)
mscRtgDpnArtErrRidTputErrPathEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnArtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnArtErrRidIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnArtErrRidTputErrPathValue"),
)
if mibBuilder.loadTexts:
    mscRtgDpnArtErrRidTputErrPathEntry.setStatus("mandatory")


class _MscRtgDpnArtErrRidTputErrPathValue_Type(AsciiString):
    """Custom type mscRtgDpnArtErrRidTputErrPathValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscRtgDpnArtErrRidTputErrPathValue_Type.__name__ = "AsciiString"
_MscRtgDpnArtErrRidTputErrPathValue_Object = MibTableColumn
mscRtgDpnArtErrRidTputErrPathValue = _MscRtgDpnArtErrRidTputErrPathValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 2, 689, 1, 1),
    _MscRtgDpnArtErrRidTputErrPathValue_Type()
)
mscRtgDpnArtErrRidTputErrPathValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnArtErrRidTputErrPathValue.setStatus("mandatory")
_MscRtgDpnArtErrMid_ObjectIdentity = ObjectIdentity
mscRtgDpnArtErrMid = _MscRtgDpnArtErrMid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 3)
)
_MscRtgDpnArtErrMidRowStatusTable_Object = MibTable
mscRtgDpnArtErrMidRowStatusTable = _MscRtgDpnArtErrMidRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 3, 1)
)
if mibBuilder.loadTexts:
    mscRtgDpnArtErrMidRowStatusTable.setStatus("mandatory")
_MscRtgDpnArtErrMidRowStatusEntry_Object = MibTableRow
mscRtgDpnArtErrMidRowStatusEntry = _MscRtgDpnArtErrMidRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 3, 1, 1)
)
mscRtgDpnArtErrMidRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnArtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnArtErrMidIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnArtErrMidRowStatusEntry.setStatus("mandatory")
_MscRtgDpnArtErrMidRowStatus_Type = RowStatus
_MscRtgDpnArtErrMidRowStatus_Object = MibTableColumn
mscRtgDpnArtErrMidRowStatus = _MscRtgDpnArtErrMidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 3, 1, 1, 1),
    _MscRtgDpnArtErrMidRowStatus_Type()
)
mscRtgDpnArtErrMidRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnArtErrMidRowStatus.setStatus("mandatory")
_MscRtgDpnArtErrMidComponentName_Type = DisplayString
_MscRtgDpnArtErrMidComponentName_Object = MibTableColumn
mscRtgDpnArtErrMidComponentName = _MscRtgDpnArtErrMidComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 3, 1, 1, 2),
    _MscRtgDpnArtErrMidComponentName_Type()
)
mscRtgDpnArtErrMidComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnArtErrMidComponentName.setStatus("mandatory")
_MscRtgDpnArtErrMidStorageType_Type = StorageType
_MscRtgDpnArtErrMidStorageType_Object = MibTableColumn
mscRtgDpnArtErrMidStorageType = _MscRtgDpnArtErrMidStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 3, 1, 1, 4),
    _MscRtgDpnArtErrMidStorageType_Type()
)
mscRtgDpnArtErrMidStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnArtErrMidStorageType.setStatus("mandatory")


class _MscRtgDpnArtErrMidIndex_Type(Integer32):
    """Custom type mscRtgDpnArtErrMidIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2046),
    )


_MscRtgDpnArtErrMidIndex_Type.__name__ = "Integer32"
_MscRtgDpnArtErrMidIndex_Object = MibTableColumn
mscRtgDpnArtErrMidIndex = _MscRtgDpnArtErrMidIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 3, 1, 1, 10),
    _MscRtgDpnArtErrMidIndex_Type()
)
mscRtgDpnArtErrMidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnArtErrMidIndex.setStatus("mandatory")
_MscRtgDpnArtErrMidOperTable_Object = MibTable
mscRtgDpnArtErrMidOperTable = _MscRtgDpnArtErrMidOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 3, 10)
)
if mibBuilder.loadTexts:
    mscRtgDpnArtErrMidOperTable.setStatus("mandatory")
_MscRtgDpnArtErrMidOperEntry_Object = MibTableRow
mscRtgDpnArtErrMidOperEntry = _MscRtgDpnArtErrMidOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 3, 10, 1)
)
mscRtgDpnArtErrMidOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnArtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnArtErrMidIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnArtErrMidOperEntry.setStatus("mandatory")


class _MscRtgDpnArtErrMidDelayCosErrType_Type(Integer32):
    """Custom type mscRtgDpnArtErrMidDelayCosErrType based on Integer32"""
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
        *(("loop", 2),
          ("noError", 0),
          ("timeout", 1))
    )


_MscRtgDpnArtErrMidDelayCosErrType_Type.__name__ = "Integer32"
_MscRtgDpnArtErrMidDelayCosErrType_Object = MibTableColumn
mscRtgDpnArtErrMidDelayCosErrType = _MscRtgDpnArtErrMidDelayCosErrType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 3, 10, 1, 1),
    _MscRtgDpnArtErrMidDelayCosErrType_Type()
)
mscRtgDpnArtErrMidDelayCosErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnArtErrMidDelayCosErrType.setStatus("mandatory")


class _MscRtgDpnArtErrMidThroughputCosErrType_Type(Integer32):
    """Custom type mscRtgDpnArtErrMidThroughputCosErrType based on Integer32"""
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
        *(("loop", 2),
          ("noError", 0),
          ("timeout", 1))
    )


_MscRtgDpnArtErrMidThroughputCosErrType_Type.__name__ = "Integer32"
_MscRtgDpnArtErrMidThroughputCosErrType_Object = MibTableColumn
mscRtgDpnArtErrMidThroughputCosErrType = _MscRtgDpnArtErrMidThroughputCosErrType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 3, 10, 1, 2),
    _MscRtgDpnArtErrMidThroughputCosErrType_Type()
)
mscRtgDpnArtErrMidThroughputCosErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnArtErrMidThroughputCosErrType.setStatus("mandatory")
_MscRtgDpnArtErrMidDelayErrPathTable_Object = MibTable
mscRtgDpnArtErrMidDelayErrPathTable = _MscRtgDpnArtErrMidDelayErrPathTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 3, 688)
)
if mibBuilder.loadTexts:
    mscRtgDpnArtErrMidDelayErrPathTable.setStatus("mandatory")
_MscRtgDpnArtErrMidDelayErrPathEntry_Object = MibTableRow
mscRtgDpnArtErrMidDelayErrPathEntry = _MscRtgDpnArtErrMidDelayErrPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 3, 688, 1)
)
mscRtgDpnArtErrMidDelayErrPathEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnArtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnArtErrMidIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnArtErrMidDelayErrPathValue"),
)
if mibBuilder.loadTexts:
    mscRtgDpnArtErrMidDelayErrPathEntry.setStatus("mandatory")


class _MscRtgDpnArtErrMidDelayErrPathValue_Type(AsciiString):
    """Custom type mscRtgDpnArtErrMidDelayErrPathValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscRtgDpnArtErrMidDelayErrPathValue_Type.__name__ = "AsciiString"
_MscRtgDpnArtErrMidDelayErrPathValue_Object = MibTableColumn
mscRtgDpnArtErrMidDelayErrPathValue = _MscRtgDpnArtErrMidDelayErrPathValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 3, 688, 1, 1),
    _MscRtgDpnArtErrMidDelayErrPathValue_Type()
)
mscRtgDpnArtErrMidDelayErrPathValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnArtErrMidDelayErrPathValue.setStatus("mandatory")
_MscRtgDpnArtErrMidTputErrPathTable_Object = MibTable
mscRtgDpnArtErrMidTputErrPathTable = _MscRtgDpnArtErrMidTputErrPathTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 3, 689)
)
if mibBuilder.loadTexts:
    mscRtgDpnArtErrMidTputErrPathTable.setStatus("mandatory")
_MscRtgDpnArtErrMidTputErrPathEntry_Object = MibTableRow
mscRtgDpnArtErrMidTputErrPathEntry = _MscRtgDpnArtErrMidTputErrPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 3, 689, 1)
)
mscRtgDpnArtErrMidTputErrPathEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnArtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnArtErrMidIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnArtErrMidTputErrPathValue"),
)
if mibBuilder.loadTexts:
    mscRtgDpnArtErrMidTputErrPathEntry.setStatus("mandatory")


class _MscRtgDpnArtErrMidTputErrPathValue_Type(AsciiString):
    """Custom type mscRtgDpnArtErrMidTputErrPathValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscRtgDpnArtErrMidTputErrPathValue_Type.__name__ = "AsciiString"
_MscRtgDpnArtErrMidTputErrPathValue_Object = MibTableColumn
mscRtgDpnArtErrMidTputErrPathValue = _MscRtgDpnArtErrMidTputErrPathValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 3, 689, 1, 1),
    _MscRtgDpnArtErrMidTputErrPathValue_Type()
)
mscRtgDpnArtErrMidTputErrPathValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnArtErrMidTputErrPathValue.setStatus("mandatory")
_MscRtgDpnArtProvTable_Object = MibTable
mscRtgDpnArtProvTable = _MscRtgDpnArtProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 10)
)
if mibBuilder.loadTexts:
    mscRtgDpnArtProvTable.setStatus("mandatory")
_MscRtgDpnArtProvEntry_Object = MibTableRow
mscRtgDpnArtProvEntry = _MscRtgDpnArtProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 10, 1)
)
mscRtgDpnArtProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnArtIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnArtProvEntry.setStatus("mandatory")


class _MscRtgDpnArtCosUnderTest_Type(Integer32):
    """Custom type mscRtgDpnArtCosUnderTest based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delayAndTputCos", 3),
          ("delayCosOnly", 1),
          ("none", 0),
          ("tputCosOnly", 2))
    )


_MscRtgDpnArtCosUnderTest_Type.__name__ = "Integer32"
_MscRtgDpnArtCosUnderTest_Object = MibTableColumn
mscRtgDpnArtCosUnderTest = _MscRtgDpnArtCosUnderTest_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 10, 1, 1),
    _MscRtgDpnArtCosUnderTest_Type()
)
mscRtgDpnArtCosUnderTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgDpnArtCosUnderTest.setStatus("mandatory")


class _MscRtgDpnArtTestInterval_Type(Unsigned32):
    """Custom type mscRtgDpnArtTestInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 900),
    )


_MscRtgDpnArtTestInterval_Type.__name__ = "Unsigned32"
_MscRtgDpnArtTestInterval_Object = MibTableColumn
mscRtgDpnArtTestInterval = _MscRtgDpnArtTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 10, 1, 2),
    _MscRtgDpnArtTestInterval_Type()
)
mscRtgDpnArtTestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgDpnArtTestInterval.setStatus("mandatory")
_MscRtgDpnArtOperTable_Object = MibTable
mscRtgDpnArtOperTable = _MscRtgDpnArtOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 11)
)
if mibBuilder.loadTexts:
    mscRtgDpnArtOperTable.setStatus("mandatory")
_MscRtgDpnArtOperEntry_Object = MibTableRow
mscRtgDpnArtOperEntry = _MscRtgDpnArtOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 11, 1)
)
mscRtgDpnArtOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnArtIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnArtOperEntry.setStatus("mandatory")


class _MscRtgDpnArtNumOfLoopDests_Type(Unsigned32):
    """Custom type mscRtgDpnArtNumOfLoopDests based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_MscRtgDpnArtNumOfLoopDests_Type.__name__ = "Unsigned32"
_MscRtgDpnArtNumOfLoopDests_Object = MibTableColumn
mscRtgDpnArtNumOfLoopDests = _MscRtgDpnArtNumOfLoopDests_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 11, 1, 1),
    _MscRtgDpnArtNumOfLoopDests_Type()
)
mscRtgDpnArtNumOfLoopDests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnArtNumOfLoopDests.setStatus("mandatory")


class _MscRtgDpnArtNumOfTimeoutDests_Type(Unsigned32):
    """Custom type mscRtgDpnArtNumOfTimeoutDests based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_MscRtgDpnArtNumOfTimeoutDests_Type.__name__ = "Unsigned32"
_MscRtgDpnArtNumOfTimeoutDests_Object = MibTableColumn
mscRtgDpnArtNumOfTimeoutDests = _MscRtgDpnArtNumOfTimeoutDests_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 9, 11, 1, 2),
    _MscRtgDpnArtNumOfTimeoutDests_Type()
)
mscRtgDpnArtNumOfTimeoutDests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnArtNumOfTimeoutDests.setStatus("mandatory")
_MscRtgDpnProvTable_Object = MibTable
mscRtgDpnProvTable = _MscRtgDpnProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 11)
)
if mibBuilder.loadTexts:
    mscRtgDpnProvTable.setStatus("mandatory")
_MscRtgDpnProvEntry_Object = MibTableRow
mscRtgDpnProvEntry = _MscRtgDpnProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 11, 1)
)
mscRtgDpnProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnProvEntry.setStatus("mandatory")


class _MscRtgDpnLogicalNetworkNumber_Type(Unsigned32):
    """Custom type mscRtgDpnLogicalNetworkNumber based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MscRtgDpnLogicalNetworkNumber_Type.__name__ = "Unsigned32"
_MscRtgDpnLogicalNetworkNumber_Object = MibTableColumn
mscRtgDpnLogicalNetworkNumber = _MscRtgDpnLogicalNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 11, 1, 1),
    _MscRtgDpnLogicalNetworkNumber_Type()
)
mscRtgDpnLogicalNetworkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnLogicalNetworkNumber.setStatus("mandatory")


class _MscRtgDpnRoutingId_Type(Unsigned32):
    """Custom type mscRtgDpnRoutingId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 126),
    )


_MscRtgDpnRoutingId_Type.__name__ = "Unsigned32"
_MscRtgDpnRoutingId_Object = MibTableColumn
mscRtgDpnRoutingId = _MscRtgDpnRoutingId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 11, 1, 2),
    _MscRtgDpnRoutingId_Type()
)
mscRtgDpnRoutingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgDpnRoutingId.setStatus("mandatory")


class _MscRtgDpnModuleId_Type(Unsigned32):
    """Custom type mscRtgDpnModuleId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1909),
    )


_MscRtgDpnModuleId_Type.__name__ = "Unsigned32"
_MscRtgDpnModuleId_Object = MibTableColumn
mscRtgDpnModuleId = _MscRtgDpnModuleId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 11, 1, 3),
    _MscRtgDpnModuleId_Type()
)
mscRtgDpnModuleId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgDpnModuleId.setStatus("mandatory")


class _MscRtgDpnDelayMetricCutOff_Type(Unsigned32):
    """Custom type mscRtgDpnDelayMetricCutOff based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 250),
    )


_MscRtgDpnDelayMetricCutOff_Type.__name__ = "Unsigned32"
_MscRtgDpnDelayMetricCutOff_Object = MibTableColumn
mscRtgDpnDelayMetricCutOff = _MscRtgDpnDelayMetricCutOff_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 11, 1, 4),
    _MscRtgDpnDelayMetricCutOff_Type()
)
mscRtgDpnDelayMetricCutOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgDpnDelayMetricCutOff.setStatus("mandatory")


class _MscRtgDpnThroughputMetricCutOff_Type(Unsigned32):
    """Custom type mscRtgDpnThroughputMetricCutOff based on Unsigned32"""
    defaultValue = 245

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 245),
    )


_MscRtgDpnThroughputMetricCutOff_Type.__name__ = "Unsigned32"
_MscRtgDpnThroughputMetricCutOff_Object = MibTableColumn
mscRtgDpnThroughputMetricCutOff = _MscRtgDpnThroughputMetricCutOff_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 11, 1, 5),
    _MscRtgDpnThroughputMetricCutOff_Type()
)
mscRtgDpnThroughputMetricCutOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgDpnThroughputMetricCutOff.setStatus("mandatory")


class _MscRtgDpnForwardingPolicy_Type(Integer32):
    """Custom type mscRtgDpnForwardingPolicy based on Integer32"""
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


_MscRtgDpnForwardingPolicy_Type.__name__ = "Integer32"
_MscRtgDpnForwardingPolicy_Object = MibTableColumn
mscRtgDpnForwardingPolicy = _MscRtgDpnForwardingPolicy_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 11, 1, 6),
    _MscRtgDpnForwardingPolicy_Type()
)
mscRtgDpnForwardingPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgDpnForwardingPolicy.setStatus("mandatory")


class _MscRtgDpnDelayMetricRangeBoundary_Type(Unsigned32):
    """Custom type mscRtgDpnDelayMetricRangeBoundary based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscRtgDpnDelayMetricRangeBoundary_Type.__name__ = "Unsigned32"
_MscRtgDpnDelayMetricRangeBoundary_Object = MibTableColumn
mscRtgDpnDelayMetricRangeBoundary = _MscRtgDpnDelayMetricRangeBoundary_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 11, 1, 7),
    _MscRtgDpnDelayMetricRangeBoundary_Type()
)
mscRtgDpnDelayMetricRangeBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgDpnDelayMetricRangeBoundary.setStatus("mandatory")


class _MscRtgDpnTputMetricRangeBoundary_Type(Unsigned32):
    """Custom type mscRtgDpnTputMetricRangeBoundary based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscRtgDpnTputMetricRangeBoundary_Type.__name__ = "Unsigned32"
_MscRtgDpnTputMetricRangeBoundary_Object = MibTableColumn
mscRtgDpnTputMetricRangeBoundary = _MscRtgDpnTputMetricRangeBoundary_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 11, 1, 8),
    _MscRtgDpnTputMetricRangeBoundary_Type()
)
mscRtgDpnTputMetricRangeBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgDpnTputMetricRangeBoundary.setStatus("mandatory")
_MscRtgDpnConStatsTable_Object = MibTable
mscRtgDpnConStatsTable = _MscRtgDpnConStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 13)
)
if mibBuilder.loadTexts:
    mscRtgDpnConStatsTable.setStatus("mandatory")
_MscRtgDpnConStatsEntry_Object = MibTableRow
mscRtgDpnConStatsEntry = _MscRtgDpnConStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 13, 1)
)
mscRtgDpnConStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnConStatsEntry.setStatus("mandatory")


class _MscRtgDpnControlPktTx_Type(Unsigned32):
    """Custom type mscRtgDpnControlPktTx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscRtgDpnControlPktTx_Type.__name__ = "Unsigned32"
_MscRtgDpnControlPktTx_Object = MibTableColumn
mscRtgDpnControlPktTx = _MscRtgDpnControlPktTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 13, 1, 1),
    _MscRtgDpnControlPktTx_Type()
)
mscRtgDpnControlPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnControlPktTx.setStatus("mandatory")


class _MscRtgDpnControlPktRx_Type(Unsigned32):
    """Custom type mscRtgDpnControlPktRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscRtgDpnControlPktRx_Type.__name__ = "Unsigned32"
_MscRtgDpnControlPktRx_Object = MibTableColumn
mscRtgDpnControlPktRx = _MscRtgDpnControlPktRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 13, 1, 2),
    _MscRtgDpnControlPktRx_Type()
)
mscRtgDpnControlPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnControlPktRx.setStatus("mandatory")


class _MscRtgDpnControlBytesTx_Type(Unsigned32):
    """Custom type mscRtgDpnControlBytesTx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscRtgDpnControlBytesTx_Type.__name__ = "Unsigned32"
_MscRtgDpnControlBytesTx_Object = MibTableColumn
mscRtgDpnControlBytesTx = _MscRtgDpnControlBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 13, 1, 3),
    _MscRtgDpnControlBytesTx_Type()
)
mscRtgDpnControlBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnControlBytesTx.setStatus("mandatory")


class _MscRtgDpnControlBytesRx_Type(Unsigned32):
    """Custom type mscRtgDpnControlBytesRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscRtgDpnControlBytesRx_Type.__name__ = "Unsigned32"
_MscRtgDpnControlBytesRx_Object = MibTableColumn
mscRtgDpnControlBytesRx = _MscRtgDpnControlBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 13, 1, 4),
    _MscRtgDpnControlBytesRx_Type()
)
mscRtgDpnControlBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnControlBytesRx.setStatus("mandatory")


class _MscRtgDpnOutOfSequencePkt_Type(Unsigned32):
    """Custom type mscRtgDpnOutOfSequencePkt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscRtgDpnOutOfSequencePkt_Type.__name__ = "Unsigned32"
_MscRtgDpnOutOfSequencePkt_Object = MibTableColumn
mscRtgDpnOutOfSequencePkt = _MscRtgDpnOutOfSequencePkt_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 13, 1, 5),
    _MscRtgDpnOutOfSequencePkt_Type()
)
mscRtgDpnOutOfSequencePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnOutOfSequencePkt.setStatus("mandatory")
_MscRtgDpnFwdStatsTable_Object = MibTable
mscRtgDpnFwdStatsTable = _MscRtgDpnFwdStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 14)
)
if mibBuilder.loadTexts:
    mscRtgDpnFwdStatsTable.setStatus("mandatory")
_MscRtgDpnFwdStatsEntry_Object = MibTableRow
mscRtgDpnFwdStatsEntry = _MscRtgDpnFwdStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 14, 1)
)
mscRtgDpnFwdStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnFwdStatsEntry.setStatus("mandatory")
_MscRtgDpnTotalPackets_Type = PassportCounter64
_MscRtgDpnTotalPackets_Object = MibTableColumn
mscRtgDpnTotalPackets = _MscRtgDpnTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 14, 1, 1),
    _MscRtgDpnTotalPackets_Type()
)
mscRtgDpnTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnTotalPackets.setStatus("mandatory")
_MscRtgDpnThroughputPackets_Type = PassportCounter64
_MscRtgDpnThroughputPackets_Object = MibTableColumn
mscRtgDpnThroughputPackets = _MscRtgDpnThroughputPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 14, 1, 2),
    _MscRtgDpnThroughputPackets_Type()
)
mscRtgDpnThroughputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnThroughputPackets.setStatus("mandatory")
_MscRtgDpnDelayPackets_Type = PassportCounter64
_MscRtgDpnDelayPackets_Object = MibTableColumn
mscRtgDpnDelayPackets = _MscRtgDpnDelayPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 14, 1, 3),
    _MscRtgDpnDelayPackets_Type()
)
mscRtgDpnDelayPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnDelayPackets.setStatus("mandatory")
_MscRtgDpnNormalReliabilityPackets_Type = PassportCounter64
_MscRtgDpnNormalReliabilityPackets_Object = MibTableColumn
mscRtgDpnNormalReliabilityPackets = _MscRtgDpnNormalReliabilityPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 14, 1, 4),
    _MscRtgDpnNormalReliabilityPackets_Type()
)
mscRtgDpnNormalReliabilityPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnNormalReliabilityPackets.setStatus("mandatory")
_MscRtgDpnHighReliabilityPackets_Type = PassportCounter64
_MscRtgDpnHighReliabilityPackets_Object = MibTableColumn
mscRtgDpnHighReliabilityPackets = _MscRtgDpnHighReliabilityPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 14, 1, 5),
    _MscRtgDpnHighReliabilityPackets_Type()
)
mscRtgDpnHighReliabilityPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnHighReliabilityPackets.setStatus("mandatory")
_MscRtgDpnDiscardNoRoute_Type = PassportCounter64
_MscRtgDpnDiscardNoRoute_Object = MibTableColumn
mscRtgDpnDiscardNoRoute = _MscRtgDpnDiscardNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 14, 1, 6),
    _MscRtgDpnDiscardNoRoute_Type()
)
mscRtgDpnDiscardNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnDiscardNoRoute.setStatus("mandatory")
_MscRtgDpnInterruptingPackets_Type = PassportCounter64
_MscRtgDpnInterruptingPackets_Object = MibTableColumn
mscRtgDpnInterruptingPackets = _MscRtgDpnInterruptingPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 14, 1, 7),
    _MscRtgDpnInterruptingPackets_Type()
)
mscRtgDpnInterruptingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnInterruptingPackets.setStatus("mandatory")
_MscRtgDpnDiscardLpCongested_Type = PassportCounter64
_MscRtgDpnDiscardLpCongested_Object = MibTableColumn
mscRtgDpnDiscardLpCongested = _MscRtgDpnDiscardLpCongested_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 14, 1, 8),
    _MscRtgDpnDiscardLpCongested_Type()
)
mscRtgDpnDiscardLpCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnDiscardLpCongested.setStatus("mandatory")
_MscRtgDpnCallServerModuleRidsTable_Object = MibTable
mscRtgDpnCallServerModuleRidsTable = _MscRtgDpnCallServerModuleRidsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 232)
)
if mibBuilder.loadTexts:
    mscRtgDpnCallServerModuleRidsTable.setStatus("mandatory")
_MscRtgDpnCallServerModuleRidsEntry_Object = MibTableRow
mscRtgDpnCallServerModuleRidsEntry = _MscRtgDpnCallServerModuleRidsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 232, 1)
)
mscRtgDpnCallServerModuleRidsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnCallServerModuleRidsValue"),
)
if mibBuilder.loadTexts:
    mscRtgDpnCallServerModuleRidsEntry.setStatus("mandatory")


class _MscRtgDpnCallServerModuleRidsValue_Type(Integer32):
    """Custom type mscRtgDpnCallServerModuleRidsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 126),
    )


_MscRtgDpnCallServerModuleRidsValue_Type.__name__ = "Integer32"
_MscRtgDpnCallServerModuleRidsValue_Object = MibTableColumn
mscRtgDpnCallServerModuleRidsValue = _MscRtgDpnCallServerModuleRidsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 232, 1, 1),
    _MscRtgDpnCallServerModuleRidsValue_Type()
)
mscRtgDpnCallServerModuleRidsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnCallServerModuleRidsValue.setStatus("mandatory")
_MscRtgDpnSubnetMidsTable_Object = MibTable
mscRtgDpnSubnetMidsTable = _MscRtgDpnSubnetMidsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 233)
)
if mibBuilder.loadTexts:
    mscRtgDpnSubnetMidsTable.setStatus("mandatory")
_MscRtgDpnSubnetMidsEntry_Object = MibTableRow
mscRtgDpnSubnetMidsEntry = _MscRtgDpnSubnetMidsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 233, 1)
)
mscRtgDpnSubnetMidsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnSubnetMidsValue"),
)
if mibBuilder.loadTexts:
    mscRtgDpnSubnetMidsEntry.setStatus("mandatory")
_MscRtgDpnSubnetMidsValue_Type = RowPointer
_MscRtgDpnSubnetMidsValue_Object = MibTableColumn
mscRtgDpnSubnetMidsValue = _MscRtgDpnSubnetMidsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 233, 1, 1),
    _MscRtgDpnSubnetMidsValue_Type()
)
mscRtgDpnSubnetMidsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgDpnSubnetMidsValue.setStatus("mandatory")
_MscRtgDpnVarianceTable_Object = MibTable
mscRtgDpnVarianceTable = _MscRtgDpnVarianceTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 343)
)
if mibBuilder.loadTexts:
    mscRtgDpnVarianceTable.setStatus("mandatory")
_MscRtgDpnVarianceEntry_Object = MibTableRow
mscRtgDpnVarianceEntry = _MscRtgDpnVarianceEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 343, 1)
)
mscRtgDpnVarianceEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnVarianceCosIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DpnRoutingMIB", "mscRtgDpnVarianceMetricRangeIndex"),
)
if mibBuilder.loadTexts:
    mscRtgDpnVarianceEntry.setStatus("mandatory")


class _MscRtgDpnVarianceCosIndex_Type(Integer32):
    """Custom type mscRtgDpnVarianceCosIndex based on Integer32"""
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


_MscRtgDpnVarianceCosIndex_Type.__name__ = "Integer32"
_MscRtgDpnVarianceCosIndex_Object = MibTableColumn
mscRtgDpnVarianceCosIndex = _MscRtgDpnVarianceCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 343, 1, 1),
    _MscRtgDpnVarianceCosIndex_Type()
)
mscRtgDpnVarianceCosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnVarianceCosIndex.setStatus("mandatory")


class _MscRtgDpnVarianceMetricRangeIndex_Type(Integer32):
    """Custom type mscRtgDpnVarianceMetricRangeIndex based on Integer32"""
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


_MscRtgDpnVarianceMetricRangeIndex_Type.__name__ = "Integer32"
_MscRtgDpnVarianceMetricRangeIndex_Object = MibTableColumn
mscRtgDpnVarianceMetricRangeIndex = _MscRtgDpnVarianceMetricRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 343, 1, 2),
    _MscRtgDpnVarianceMetricRangeIndex_Type()
)
mscRtgDpnVarianceMetricRangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgDpnVarianceMetricRangeIndex.setStatus("mandatory")


class _MscRtgDpnVarianceValue_Type(Unsigned32):
    """Custom type mscRtgDpnVarianceValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
        ValueRangeConstraint(9999, 9999),
    )


_MscRtgDpnVarianceValue_Type.__name__ = "Unsigned32"
_MscRtgDpnVarianceValue_Object = MibTableColumn
mscRtgDpnVarianceValue = _MscRtgDpnVarianceValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 4, 343, 1, 3),
    _MscRtgDpnVarianceValue_Type()
)
mscRtgDpnVarianceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgDpnVarianceValue.setStatus("mandatory")
_DpnRoutingMIB_ObjectIdentity = ObjectIdentity
dpnRoutingMIB = _DpnRoutingMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 21)
)
_DpnRoutingGroup_ObjectIdentity = ObjectIdentity
dpnRoutingGroup = _DpnRoutingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 21, 1)
)
_DpnRoutingGroupCA_ObjectIdentity = ObjectIdentity
dpnRoutingGroupCA = _DpnRoutingGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 21, 1, 1)
)
_DpnRoutingGroupCA02_ObjectIdentity = ObjectIdentity
dpnRoutingGroupCA02 = _DpnRoutingGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 21, 1, 1, 3)
)
_DpnRoutingGroupCA02A_ObjectIdentity = ObjectIdentity
dpnRoutingGroupCA02A = _DpnRoutingGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 21, 1, 1, 3, 2)
)
_DpnRoutingCapabilities_ObjectIdentity = ObjectIdentity
dpnRoutingCapabilities = _DpnRoutingCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 21, 3)
)
_DpnRoutingCapabilitiesCA_ObjectIdentity = ObjectIdentity
dpnRoutingCapabilitiesCA = _DpnRoutingCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 21, 3, 1)
)
_DpnRoutingCapabilitiesCA02_ObjectIdentity = ObjectIdentity
dpnRoutingCapabilitiesCA02 = _DpnRoutingCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 21, 3, 1, 3)
)
_DpnRoutingCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
dpnRoutingCapabilitiesCA02A = _DpnRoutingCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 21, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-DpnRoutingMIB",
    **{"mscRtgDpn": mscRtgDpn,
       "mscRtgDpnRowStatusTable": mscRtgDpnRowStatusTable,
       "mscRtgDpnRowStatusEntry": mscRtgDpnRowStatusEntry,
       "mscRtgDpnRowStatus": mscRtgDpnRowStatus,
       "mscRtgDpnComponentName": mscRtgDpnComponentName,
       "mscRtgDpnStorageType": mscRtgDpnStorageType,
       "mscRtgDpnIndex": mscRtgDpnIndex,
       "mscRtgDpnRid": mscRtgDpnRid,
       "mscRtgDpnRidRowStatusTable": mscRtgDpnRidRowStatusTable,
       "mscRtgDpnRidRowStatusEntry": mscRtgDpnRidRowStatusEntry,
       "mscRtgDpnRidRowStatus": mscRtgDpnRidRowStatus,
       "mscRtgDpnRidComponentName": mscRtgDpnRidComponentName,
       "mscRtgDpnRidStorageType": mscRtgDpnRidStorageType,
       "mscRtgDpnRidIndex": mscRtgDpnRidIndex,
       "mscRtgDpnRidMid": mscRtgDpnRidMid,
       "mscRtgDpnRidMidRowStatusTable": mscRtgDpnRidMidRowStatusTable,
       "mscRtgDpnRidMidRowStatusEntry": mscRtgDpnRidMidRowStatusEntry,
       "mscRtgDpnRidMidRowStatus": mscRtgDpnRidMidRowStatus,
       "mscRtgDpnRidMidComponentName": mscRtgDpnRidMidComponentName,
       "mscRtgDpnRidMidStorageType": mscRtgDpnRidMidStorageType,
       "mscRtgDpnRidMidIndex": mscRtgDpnRidMidIndex,
       "mscRtgDpnRidOperTable": mscRtgDpnRidOperTable,
       "mscRtgDpnRidOperEntry": mscRtgDpnRidOperEntry,
       "mscRtgDpnRidDpnDelayMetric": mscRtgDpnRidDpnDelayMetric,
       "mscRtgDpnRidDpnTputMetric": mscRtgDpnRidDpnTputMetric,
       "mscRtgDpnRidDelayNextHopLinkGroupsTable": mscRtgDpnRidDelayNextHopLinkGroupsTable,
       "mscRtgDpnRidDelayNextHopLinkGroupsEntry": mscRtgDpnRidDelayNextHopLinkGroupsEntry,
       "mscRtgDpnRidDelayNextHopLinkGroupsIndex": mscRtgDpnRidDelayNextHopLinkGroupsIndex,
       "mscRtgDpnRidDelayNextHopLinkGroupsValue": mscRtgDpnRidDelayNextHopLinkGroupsValue,
       "mscRtgDpnRidTputNextHopLinkGroupsTable": mscRtgDpnRidTputNextHopLinkGroupsTable,
       "mscRtgDpnRidTputNextHopLinkGroupsEntry": mscRtgDpnRidTputNextHopLinkGroupsEntry,
       "mscRtgDpnRidTputNextHopLinkGroupsIndex": mscRtgDpnRidTputNextHopLinkGroupsIndex,
       "mscRtgDpnRidTputNextHopLinkGroupsValue": mscRtgDpnRidTputNextHopLinkGroupsValue,
       "mscRtgDpnRidDelayPathTrafficProportionsTable": mscRtgDpnRidDelayPathTrafficProportionsTable,
       "mscRtgDpnRidDelayPathTrafficProportionsEntry": mscRtgDpnRidDelayPathTrafficProportionsEntry,
       "mscRtgDpnRidDelayPathTrafficProportionsIndex": mscRtgDpnRidDelayPathTrafficProportionsIndex,
       "mscRtgDpnRidDelayPathTrafficProportionsValue": mscRtgDpnRidDelayPathTrafficProportionsValue,
       "mscRtgDpnRidTputPathTrafficProportionsTable": mscRtgDpnRidTputPathTrafficProportionsTable,
       "mscRtgDpnRidTputPathTrafficProportionsEntry": mscRtgDpnRidTputPathTrafficProportionsEntry,
       "mscRtgDpnRidTputPathTrafficProportionsIndex": mscRtgDpnRidTputPathTrafficProportionsIndex,
       "mscRtgDpnRidTputPathTrafficProportionsValue": mscRtgDpnRidTputPathTrafficProportionsValue,
       "mscRtgDpnRidDelayMetricTable": mscRtgDpnRidDelayMetricTable,
       "mscRtgDpnRidDelayMetricEntry": mscRtgDpnRidDelayMetricEntry,
       "mscRtgDpnRidDelayMetricIndex": mscRtgDpnRidDelayMetricIndex,
       "mscRtgDpnRidDelayMetricValue": mscRtgDpnRidDelayMetricValue,
       "mscRtgDpnRidTputMetricTable": mscRtgDpnRidTputMetricTable,
       "mscRtgDpnRidTputMetricEntry": mscRtgDpnRidTputMetricEntry,
       "mscRtgDpnRidTputMetricIndex": mscRtgDpnRidTputMetricIndex,
       "mscRtgDpnRidTputMetricValue": mscRtgDpnRidTputMetricValue,
       "mscRtgDpnMid": mscRtgDpnMid,
       "mscRtgDpnMidRowStatusTable": mscRtgDpnMidRowStatusTable,
       "mscRtgDpnMidRowStatusEntry": mscRtgDpnMidRowStatusEntry,
       "mscRtgDpnMidRowStatus": mscRtgDpnMidRowStatus,
       "mscRtgDpnMidComponentName": mscRtgDpnMidComponentName,
       "mscRtgDpnMidStorageType": mscRtgDpnMidStorageType,
       "mscRtgDpnMidIndex": mscRtgDpnMidIndex,
       "mscRtgDpnMidOperTable": mscRtgDpnMidOperTable,
       "mscRtgDpnMidOperEntry": mscRtgDpnMidOperEntry,
       "mscRtgDpnMidSubstituteRid": mscRtgDpnMidSubstituteRid,
       "mscRtgDpnMidDelayNextHopLinkGroupsTable": mscRtgDpnMidDelayNextHopLinkGroupsTable,
       "mscRtgDpnMidDelayNextHopLinkGroupsEntry": mscRtgDpnMidDelayNextHopLinkGroupsEntry,
       "mscRtgDpnMidDelayNextHopLinkGroupsIndex": mscRtgDpnMidDelayNextHopLinkGroupsIndex,
       "mscRtgDpnMidDelayNextHopLinkGroupsValue": mscRtgDpnMidDelayNextHopLinkGroupsValue,
       "mscRtgDpnMidTputNextHopLinkGroupsTable": mscRtgDpnMidTputNextHopLinkGroupsTable,
       "mscRtgDpnMidTputNextHopLinkGroupsEntry": mscRtgDpnMidTputNextHopLinkGroupsEntry,
       "mscRtgDpnMidTputNextHopLinkGroupsIndex": mscRtgDpnMidTputNextHopLinkGroupsIndex,
       "mscRtgDpnMidTputNextHopLinkGroupsValue": mscRtgDpnMidTputNextHopLinkGroupsValue,
       "mscRtgDpnMidDelayMetricTable": mscRtgDpnMidDelayMetricTable,
       "mscRtgDpnMidDelayMetricEntry": mscRtgDpnMidDelayMetricEntry,
       "mscRtgDpnMidDelayMetricIndex": mscRtgDpnMidDelayMetricIndex,
       "mscRtgDpnMidDelayMetricValue": mscRtgDpnMidDelayMetricValue,
       "mscRtgDpnMidTputMetricTable": mscRtgDpnMidTputMetricTable,
       "mscRtgDpnMidTputMetricEntry": mscRtgDpnMidTputMetricEntry,
       "mscRtgDpnMidTputMetricIndex": mscRtgDpnMidTputMetricIndex,
       "mscRtgDpnMidTputMetricValue": mscRtgDpnMidTputMetricValue,
       "mscRtgDpnMidDelayPathTrafficProportionsTable": mscRtgDpnMidDelayPathTrafficProportionsTable,
       "mscRtgDpnMidDelayPathTrafficProportionsEntry": mscRtgDpnMidDelayPathTrafficProportionsEntry,
       "mscRtgDpnMidDelayPathTrafficProportionsIndex": mscRtgDpnMidDelayPathTrafficProportionsIndex,
       "mscRtgDpnMidDelayPathTrafficProportionsValue": mscRtgDpnMidDelayPathTrafficProportionsValue,
       "mscRtgDpnMidTputPathTrafficProportionsTable": mscRtgDpnMidTputPathTrafficProportionsTable,
       "mscRtgDpnMidTputPathTrafficProportionsEntry": mscRtgDpnMidTputPathTrafficProportionsEntry,
       "mscRtgDpnMidTputPathTrafficProportionsIndex": mscRtgDpnMidTputPathTrafficProportionsIndex,
       "mscRtgDpnMidTputPathTrafficProportionsValue": mscRtgDpnMidTputPathTrafficProportionsValue,
       "mscRtgDpnCs": mscRtgDpnCs,
       "mscRtgDpnCsRowStatusTable": mscRtgDpnCsRowStatusTable,
       "mscRtgDpnCsRowStatusEntry": mscRtgDpnCsRowStatusEntry,
       "mscRtgDpnCsRowStatus": mscRtgDpnCsRowStatus,
       "mscRtgDpnCsComponentName": mscRtgDpnCsComponentName,
       "mscRtgDpnCsStorageType": mscRtgDpnCsStorageType,
       "mscRtgDpnCsIndex": mscRtgDpnCsIndex,
       "mscRtgDpnCsDelayNextHopLinkGroupsTable": mscRtgDpnCsDelayNextHopLinkGroupsTable,
       "mscRtgDpnCsDelayNextHopLinkGroupsEntry": mscRtgDpnCsDelayNextHopLinkGroupsEntry,
       "mscRtgDpnCsDelayNextHopLinkGroupsIndex": mscRtgDpnCsDelayNextHopLinkGroupsIndex,
       "mscRtgDpnCsDelayNextHopLinkGroupsValue": mscRtgDpnCsDelayNextHopLinkGroupsValue,
       "mscRtgDpnCsTputNextHopLinkGroupsTable": mscRtgDpnCsTputNextHopLinkGroupsTable,
       "mscRtgDpnCsTputNextHopLinkGroupsEntry": mscRtgDpnCsTputNextHopLinkGroupsEntry,
       "mscRtgDpnCsTputNextHopLinkGroupsIndex": mscRtgDpnCsTputNextHopLinkGroupsIndex,
       "mscRtgDpnCsTputNextHopLinkGroupsValue": mscRtgDpnCsTputNextHopLinkGroupsValue,
       "mscRtgDpnCsDelayMetricTable": mscRtgDpnCsDelayMetricTable,
       "mscRtgDpnCsDelayMetricEntry": mscRtgDpnCsDelayMetricEntry,
       "mscRtgDpnCsDelayMetricIndex": mscRtgDpnCsDelayMetricIndex,
       "mscRtgDpnCsDelayMetricValue": mscRtgDpnCsDelayMetricValue,
       "mscRtgDpnCsTputMetricTable": mscRtgDpnCsTputMetricTable,
       "mscRtgDpnCsTputMetricEntry": mscRtgDpnCsTputMetricEntry,
       "mscRtgDpnCsTputMetricIndex": mscRtgDpnCsTputMetricIndex,
       "mscRtgDpnCsTputMetricValue": mscRtgDpnCsTputMetricValue,
       "mscRtgDpnCsDelayPathTrafficProportionsTable": mscRtgDpnCsDelayPathTrafficProportionsTable,
       "mscRtgDpnCsDelayPathTrafficProportionsEntry": mscRtgDpnCsDelayPathTrafficProportionsEntry,
       "mscRtgDpnCsDelayPathTrafficProportionsIndex": mscRtgDpnCsDelayPathTrafficProportionsIndex,
       "mscRtgDpnCsDelayPathTrafficProportionsValue": mscRtgDpnCsDelayPathTrafficProportionsValue,
       "mscRtgDpnCsTputPathTrafficProportionsTable": mscRtgDpnCsTputPathTrafficProportionsTable,
       "mscRtgDpnCsTputPathTrafficProportionsEntry": mscRtgDpnCsTputPathTrafficProportionsEntry,
       "mscRtgDpnCsTputPathTrafficProportionsIndex": mscRtgDpnCsTputPathTrafficProportionsIndex,
       "mscRtgDpnCsTputPathTrafficProportionsValue": mscRtgDpnCsTputPathTrafficProportionsValue,
       "mscRtgDpnLg": mscRtgDpnLg,
       "mscRtgDpnLgRowStatusTable": mscRtgDpnLgRowStatusTable,
       "mscRtgDpnLgRowStatusEntry": mscRtgDpnLgRowStatusEntry,
       "mscRtgDpnLgRowStatus": mscRtgDpnLgRowStatus,
       "mscRtgDpnLgComponentName": mscRtgDpnLgComponentName,
       "mscRtgDpnLgStorageType": mscRtgDpnLgStorageType,
       "mscRtgDpnLgIndex": mscRtgDpnLgIndex,
       "mscRtgDpnLgOperTable": mscRtgDpnLgOperTable,
       "mscRtgDpnLgOperEntry": mscRtgDpnLgOperEntry,
       "mscRtgDpnLgFarEndType": mscRtgDpnLgFarEndType,
       "mscRtgDpnLgFarEndRid": mscRtgDpnLgFarEndRid,
       "mscRtgDpnLgFarEndMid": mscRtgDpnLgFarEndMid,
       "mscRtgDpnLgDelayMetric": mscRtgDpnLgDelayMetric,
       "mscRtgDpnLgTputMetric": mscRtgDpnLgTputMetric,
       "mscRtgDpnLpStats": mscRtgDpnLpStats,
       "mscRtgDpnLpStatsRowStatusTable": mscRtgDpnLpStatsRowStatusTable,
       "mscRtgDpnLpStatsRowStatusEntry": mscRtgDpnLpStatsRowStatusEntry,
       "mscRtgDpnLpStatsRowStatus": mscRtgDpnLpStatsRowStatus,
       "mscRtgDpnLpStatsComponentName": mscRtgDpnLpStatsComponentName,
       "mscRtgDpnLpStatsStorageType": mscRtgDpnLpStatsStorageType,
       "mscRtgDpnLpStatsIndex": mscRtgDpnLpStatsIndex,
       "mscRtgDpnLpStatsFwdStatsTable": mscRtgDpnLpStatsFwdStatsTable,
       "mscRtgDpnLpStatsFwdStatsEntry": mscRtgDpnLpStatsFwdStatsEntry,
       "mscRtgDpnLpStatsTotalPackets": mscRtgDpnLpStatsTotalPackets,
       "mscRtgDpnLpStatsThroughputPackets": mscRtgDpnLpStatsThroughputPackets,
       "mscRtgDpnLpStatsDelayPackets": mscRtgDpnLpStatsDelayPackets,
       "mscRtgDpnLpStatsNormalReliabilityPackets": mscRtgDpnLpStatsNormalReliabilityPackets,
       "mscRtgDpnLpStatsHighReliabilityPackets": mscRtgDpnLpStatsHighReliabilityPackets,
       "mscRtgDpnLpStatsDiscardNoRoute": mscRtgDpnLpStatsDiscardNoRoute,
       "mscRtgDpnLpStatsInterruptingPackets": mscRtgDpnLpStatsInterruptingPackets,
       "mscRtgDpnLpStatsDiscardLpCongested": mscRtgDpnLpStatsDiscardLpCongested,
       "mscRtgDpnRidFilter": mscRtgDpnRidFilter,
       "mscRtgDpnRidFilterRowStatusTable": mscRtgDpnRidFilterRowStatusTable,
       "mscRtgDpnRidFilterRowStatusEntry": mscRtgDpnRidFilterRowStatusEntry,
       "mscRtgDpnRidFilterRowStatus": mscRtgDpnRidFilterRowStatus,
       "mscRtgDpnRidFilterComponentName": mscRtgDpnRidFilterComponentName,
       "mscRtgDpnRidFilterStorageType": mscRtgDpnRidFilterStorageType,
       "mscRtgDpnRidFilterIndex": mscRtgDpnRidFilterIndex,
       "mscRtgDpnRidFilterImportRidListTable": mscRtgDpnRidFilterImportRidListTable,
       "mscRtgDpnRidFilterImportRidListEntry": mscRtgDpnRidFilterImportRidListEntry,
       "mscRtgDpnRidFilterImportRidListValue": mscRtgDpnRidFilterImportRidListValue,
       "mscRtgDpnRidFilterImportRidListRowStatus": mscRtgDpnRidFilterImportRidListRowStatus,
       "mscRtgDpnRidFilterExportRidListTable": mscRtgDpnRidFilterExportRidListTable,
       "mscRtgDpnRidFilterExportRidListEntry": mscRtgDpnRidFilterExportRidListEntry,
       "mscRtgDpnRidFilterExportRidListValue": mscRtgDpnRidFilterExportRidListValue,
       "mscRtgDpnRidFilterExportRidListRowStatus": mscRtgDpnRidFilterExportRidListRowStatus,
       "mscRtgDpnArt": mscRtgDpnArt,
       "mscRtgDpnArtRowStatusTable": mscRtgDpnArtRowStatusTable,
       "mscRtgDpnArtRowStatusEntry": mscRtgDpnArtRowStatusEntry,
       "mscRtgDpnArtRowStatus": mscRtgDpnArtRowStatus,
       "mscRtgDpnArtComponentName": mscRtgDpnArtComponentName,
       "mscRtgDpnArtStorageType": mscRtgDpnArtStorageType,
       "mscRtgDpnArtIndex": mscRtgDpnArtIndex,
       "mscRtgDpnArtErrRid": mscRtgDpnArtErrRid,
       "mscRtgDpnArtErrRidRowStatusTable": mscRtgDpnArtErrRidRowStatusTable,
       "mscRtgDpnArtErrRidRowStatusEntry": mscRtgDpnArtErrRidRowStatusEntry,
       "mscRtgDpnArtErrRidRowStatus": mscRtgDpnArtErrRidRowStatus,
       "mscRtgDpnArtErrRidComponentName": mscRtgDpnArtErrRidComponentName,
       "mscRtgDpnArtErrRidStorageType": mscRtgDpnArtErrRidStorageType,
       "mscRtgDpnArtErrRidIndex": mscRtgDpnArtErrRidIndex,
       "mscRtgDpnArtErrRidOperTable": mscRtgDpnArtErrRidOperTable,
       "mscRtgDpnArtErrRidOperEntry": mscRtgDpnArtErrRidOperEntry,
       "mscRtgDpnArtErrRidDelayCosErrType": mscRtgDpnArtErrRidDelayCosErrType,
       "mscRtgDpnArtErrRidThroughputCosErrType": mscRtgDpnArtErrRidThroughputCosErrType,
       "mscRtgDpnArtErrRidDelayErrPathTable": mscRtgDpnArtErrRidDelayErrPathTable,
       "mscRtgDpnArtErrRidDelayErrPathEntry": mscRtgDpnArtErrRidDelayErrPathEntry,
       "mscRtgDpnArtErrRidDelayErrPathValue": mscRtgDpnArtErrRidDelayErrPathValue,
       "mscRtgDpnArtErrRidTputErrPathTable": mscRtgDpnArtErrRidTputErrPathTable,
       "mscRtgDpnArtErrRidTputErrPathEntry": mscRtgDpnArtErrRidTputErrPathEntry,
       "mscRtgDpnArtErrRidTputErrPathValue": mscRtgDpnArtErrRidTputErrPathValue,
       "mscRtgDpnArtErrMid": mscRtgDpnArtErrMid,
       "mscRtgDpnArtErrMidRowStatusTable": mscRtgDpnArtErrMidRowStatusTable,
       "mscRtgDpnArtErrMidRowStatusEntry": mscRtgDpnArtErrMidRowStatusEntry,
       "mscRtgDpnArtErrMidRowStatus": mscRtgDpnArtErrMidRowStatus,
       "mscRtgDpnArtErrMidComponentName": mscRtgDpnArtErrMidComponentName,
       "mscRtgDpnArtErrMidStorageType": mscRtgDpnArtErrMidStorageType,
       "mscRtgDpnArtErrMidIndex": mscRtgDpnArtErrMidIndex,
       "mscRtgDpnArtErrMidOperTable": mscRtgDpnArtErrMidOperTable,
       "mscRtgDpnArtErrMidOperEntry": mscRtgDpnArtErrMidOperEntry,
       "mscRtgDpnArtErrMidDelayCosErrType": mscRtgDpnArtErrMidDelayCosErrType,
       "mscRtgDpnArtErrMidThroughputCosErrType": mscRtgDpnArtErrMidThroughputCosErrType,
       "mscRtgDpnArtErrMidDelayErrPathTable": mscRtgDpnArtErrMidDelayErrPathTable,
       "mscRtgDpnArtErrMidDelayErrPathEntry": mscRtgDpnArtErrMidDelayErrPathEntry,
       "mscRtgDpnArtErrMidDelayErrPathValue": mscRtgDpnArtErrMidDelayErrPathValue,
       "mscRtgDpnArtErrMidTputErrPathTable": mscRtgDpnArtErrMidTputErrPathTable,
       "mscRtgDpnArtErrMidTputErrPathEntry": mscRtgDpnArtErrMidTputErrPathEntry,
       "mscRtgDpnArtErrMidTputErrPathValue": mscRtgDpnArtErrMidTputErrPathValue,
       "mscRtgDpnArtProvTable": mscRtgDpnArtProvTable,
       "mscRtgDpnArtProvEntry": mscRtgDpnArtProvEntry,
       "mscRtgDpnArtCosUnderTest": mscRtgDpnArtCosUnderTest,
       "mscRtgDpnArtTestInterval": mscRtgDpnArtTestInterval,
       "mscRtgDpnArtOperTable": mscRtgDpnArtOperTable,
       "mscRtgDpnArtOperEntry": mscRtgDpnArtOperEntry,
       "mscRtgDpnArtNumOfLoopDests": mscRtgDpnArtNumOfLoopDests,
       "mscRtgDpnArtNumOfTimeoutDests": mscRtgDpnArtNumOfTimeoutDests,
       "mscRtgDpnProvTable": mscRtgDpnProvTable,
       "mscRtgDpnProvEntry": mscRtgDpnProvEntry,
       "mscRtgDpnLogicalNetworkNumber": mscRtgDpnLogicalNetworkNumber,
       "mscRtgDpnRoutingId": mscRtgDpnRoutingId,
       "mscRtgDpnModuleId": mscRtgDpnModuleId,
       "mscRtgDpnDelayMetricCutOff": mscRtgDpnDelayMetricCutOff,
       "mscRtgDpnThroughputMetricCutOff": mscRtgDpnThroughputMetricCutOff,
       "mscRtgDpnForwardingPolicy": mscRtgDpnForwardingPolicy,
       "mscRtgDpnDelayMetricRangeBoundary": mscRtgDpnDelayMetricRangeBoundary,
       "mscRtgDpnTputMetricRangeBoundary": mscRtgDpnTputMetricRangeBoundary,
       "mscRtgDpnConStatsTable": mscRtgDpnConStatsTable,
       "mscRtgDpnConStatsEntry": mscRtgDpnConStatsEntry,
       "mscRtgDpnControlPktTx": mscRtgDpnControlPktTx,
       "mscRtgDpnControlPktRx": mscRtgDpnControlPktRx,
       "mscRtgDpnControlBytesTx": mscRtgDpnControlBytesTx,
       "mscRtgDpnControlBytesRx": mscRtgDpnControlBytesRx,
       "mscRtgDpnOutOfSequencePkt": mscRtgDpnOutOfSequencePkt,
       "mscRtgDpnFwdStatsTable": mscRtgDpnFwdStatsTable,
       "mscRtgDpnFwdStatsEntry": mscRtgDpnFwdStatsEntry,
       "mscRtgDpnTotalPackets": mscRtgDpnTotalPackets,
       "mscRtgDpnThroughputPackets": mscRtgDpnThroughputPackets,
       "mscRtgDpnDelayPackets": mscRtgDpnDelayPackets,
       "mscRtgDpnNormalReliabilityPackets": mscRtgDpnNormalReliabilityPackets,
       "mscRtgDpnHighReliabilityPackets": mscRtgDpnHighReliabilityPackets,
       "mscRtgDpnDiscardNoRoute": mscRtgDpnDiscardNoRoute,
       "mscRtgDpnInterruptingPackets": mscRtgDpnInterruptingPackets,
       "mscRtgDpnDiscardLpCongested": mscRtgDpnDiscardLpCongested,
       "mscRtgDpnCallServerModuleRidsTable": mscRtgDpnCallServerModuleRidsTable,
       "mscRtgDpnCallServerModuleRidsEntry": mscRtgDpnCallServerModuleRidsEntry,
       "mscRtgDpnCallServerModuleRidsValue": mscRtgDpnCallServerModuleRidsValue,
       "mscRtgDpnSubnetMidsTable": mscRtgDpnSubnetMidsTable,
       "mscRtgDpnSubnetMidsEntry": mscRtgDpnSubnetMidsEntry,
       "mscRtgDpnSubnetMidsValue": mscRtgDpnSubnetMidsValue,
       "mscRtgDpnVarianceTable": mscRtgDpnVarianceTable,
       "mscRtgDpnVarianceEntry": mscRtgDpnVarianceEntry,
       "mscRtgDpnVarianceCosIndex": mscRtgDpnVarianceCosIndex,
       "mscRtgDpnVarianceMetricRangeIndex": mscRtgDpnVarianceMetricRangeIndex,
       "mscRtgDpnVarianceValue": mscRtgDpnVarianceValue,
       "dpnRoutingMIB": dpnRoutingMIB,
       "dpnRoutingGroup": dpnRoutingGroup,
       "dpnRoutingGroupCA": dpnRoutingGroupCA,
       "dpnRoutingGroupCA02": dpnRoutingGroupCA02,
       "dpnRoutingGroupCA02A": dpnRoutingGroupCA02A,
       "dpnRoutingCapabilities": dpnRoutingCapabilities,
       "dpnRoutingCapabilitiesCA": dpnRoutingCapabilitiesCA,
       "dpnRoutingCapabilitiesCA02": dpnRoutingCapabilitiesCA02,
       "dpnRoutingCapabilitiesCA02A": dpnRoutingCapabilitiesCA02A}
)
