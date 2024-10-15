# SNMP MIB module (Nortel-Magellan-Passport-BaseRoutingMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-BaseRoutingMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:24 2024
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

(Counter32,
 DisplayString,
 Gauge32,
 Integer32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiStringIndex,
 DigitString,
 FixedPoint1,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiStringIndex",
    "DigitString",
    "FixedPoint1",
    "NonReplicated")

(components,
 passportMIBs) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "components",
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

_Rtg_ObjectIdentity = ObjectIdentity
rtg = _Rtg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40)
)
_RtgRowStatusTable_Object = MibTable
rtgRowStatusTable = _RtgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 1)
)
if mibBuilder.loadTexts:
    rtgRowStatusTable.setStatus("mandatory")
_RtgRowStatusEntry_Object = MibTableRow
rtgRowStatusEntry = _RtgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 1, 1)
)
rtgRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
)
if mibBuilder.loadTexts:
    rtgRowStatusEntry.setStatus("mandatory")
_RtgRowStatus_Type = RowStatus
_RtgRowStatus_Object = MibTableColumn
rtgRowStatus = _RtgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 1, 1, 1),
    _RtgRowStatus_Type()
)
rtgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgRowStatus.setStatus("mandatory")
_RtgComponentName_Type = DisplayString
_RtgComponentName_Object = MibTableColumn
rtgComponentName = _RtgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 1, 1, 2),
    _RtgComponentName_Type()
)
rtgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgComponentName.setStatus("mandatory")
_RtgStorageType_Type = StorageType
_RtgStorageType_Object = MibTableColumn
rtgStorageType = _RtgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 1, 1, 4),
    _RtgStorageType_Type()
)
rtgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgStorageType.setStatus("mandatory")
_RtgIndex_Type = NonReplicated
_RtgIndex_Object = MibTableColumn
rtgIndex = _RtgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 1, 1, 10),
    _RtgIndex_Type()
)
rtgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgIndex.setStatus("mandatory")
_RtgTop_ObjectIdentity = ObjectIdentity
rtgTop = _RtgTop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5)
)
_RtgTopRowStatusTable_Object = MibTable
rtgTopRowStatusTable = _RtgTopRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 1)
)
if mibBuilder.loadTexts:
    rtgTopRowStatusTable.setStatus("mandatory")
_RtgTopRowStatusEntry_Object = MibTableRow
rtgTopRowStatusEntry = _RtgTopRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 1, 1)
)
rtgTopRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopIndex"),
)
if mibBuilder.loadTexts:
    rtgTopRowStatusEntry.setStatus("mandatory")
_RtgTopRowStatus_Type = RowStatus
_RtgTopRowStatus_Object = MibTableColumn
rtgTopRowStatus = _RtgTopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 1, 1, 1),
    _RtgTopRowStatus_Type()
)
rtgTopRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopRowStatus.setStatus("mandatory")
_RtgTopComponentName_Type = DisplayString
_RtgTopComponentName_Object = MibTableColumn
rtgTopComponentName = _RtgTopComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 1, 1, 2),
    _RtgTopComponentName_Type()
)
rtgTopComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopComponentName.setStatus("mandatory")
_RtgTopStorageType_Type = StorageType
_RtgTopStorageType_Object = MibTableColumn
rtgTopStorageType = _RtgTopStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 1, 1, 4),
    _RtgTopStorageType_Type()
)
rtgTopStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopStorageType.setStatus("mandatory")
_RtgTopIndex_Type = NonReplicated
_RtgTopIndex_Object = MibTableColumn
rtgTopIndex = _RtgTopIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 1, 1, 10),
    _RtgTopIndex_Type()
)
rtgTopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgTopIndex.setStatus("mandatory")
_RtgTopNode_ObjectIdentity = ObjectIdentity
rtgTopNode = _RtgTopNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2)
)
_RtgTopNodeRowStatusTable_Object = MibTable
rtgTopNodeRowStatusTable = _RtgTopNodeRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 1)
)
if mibBuilder.loadTexts:
    rtgTopNodeRowStatusTable.setStatus("mandatory")
_RtgTopNodeRowStatusEntry_Object = MibTableRow
rtgTopNodeRowStatusEntry = _RtgTopNodeRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 1, 1)
)
rtgTopNodeRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopNodeIndex"),
)
if mibBuilder.loadTexts:
    rtgTopNodeRowStatusEntry.setStatus("mandatory")
_RtgTopNodeRowStatus_Type = RowStatus
_RtgTopNodeRowStatus_Object = MibTableColumn
rtgTopNodeRowStatus = _RtgTopNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 1, 1, 1),
    _RtgTopNodeRowStatus_Type()
)
rtgTopNodeRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopNodeRowStatus.setStatus("mandatory")
_RtgTopNodeComponentName_Type = DisplayString
_RtgTopNodeComponentName_Object = MibTableColumn
rtgTopNodeComponentName = _RtgTopNodeComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 1, 1, 2),
    _RtgTopNodeComponentName_Type()
)
rtgTopNodeComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopNodeComponentName.setStatus("mandatory")
_RtgTopNodeStorageType_Type = StorageType
_RtgTopNodeStorageType_Object = MibTableColumn
rtgTopNodeStorageType = _RtgTopNodeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 1, 1, 4),
    _RtgTopNodeStorageType_Type()
)
rtgTopNodeStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopNodeStorageType.setStatus("mandatory")


class _RtgTopNodeIndex_Type(AsciiStringIndex):
    """Custom type rtgTopNodeIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_RtgTopNodeIndex_Type.__name__ = "AsciiStringIndex"
_RtgTopNodeIndex_Object = MibTableColumn
rtgTopNodeIndex = _RtgTopNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 1, 1, 10),
    _RtgTopNodeIndex_Type()
)
rtgTopNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgTopNodeIndex.setStatus("mandatory")
_RtgTopNodeLg_ObjectIdentity = ObjectIdentity
rtgTopNodeLg = _RtgTopNodeLg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2)
)
_RtgTopNodeLgRowStatusTable_Object = MibTable
rtgTopNodeLgRowStatusTable = _RtgTopNodeLgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rtgTopNodeLgRowStatusTable.setStatus("mandatory")
_RtgTopNodeLgRowStatusEntry_Object = MibTableRow
rtgTopNodeLgRowStatusEntry = _RtgTopNodeLgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 1, 1)
)
rtgTopNodeLgRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopNodeIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopNodeLgIndex"),
)
if mibBuilder.loadTexts:
    rtgTopNodeLgRowStatusEntry.setStatus("mandatory")
_RtgTopNodeLgRowStatus_Type = RowStatus
_RtgTopNodeLgRowStatus_Object = MibTableColumn
rtgTopNodeLgRowStatus = _RtgTopNodeLgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 1, 1, 1),
    _RtgTopNodeLgRowStatus_Type()
)
rtgTopNodeLgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopNodeLgRowStatus.setStatus("mandatory")
_RtgTopNodeLgComponentName_Type = DisplayString
_RtgTopNodeLgComponentName_Object = MibTableColumn
rtgTopNodeLgComponentName = _RtgTopNodeLgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 1, 1, 2),
    _RtgTopNodeLgComponentName_Type()
)
rtgTopNodeLgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopNodeLgComponentName.setStatus("mandatory")
_RtgTopNodeLgStorageType_Type = StorageType
_RtgTopNodeLgStorageType_Object = MibTableColumn
rtgTopNodeLgStorageType = _RtgTopNodeLgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 1, 1, 4),
    _RtgTopNodeLgStorageType_Type()
)
rtgTopNodeLgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopNodeLgStorageType.setStatus("mandatory")


class _RtgTopNodeLgIndex_Type(AsciiStringIndex):
    """Custom type rtgTopNodeLgIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_RtgTopNodeLgIndex_Type.__name__ = "AsciiStringIndex"
_RtgTopNodeLgIndex_Object = MibTableColumn
rtgTopNodeLgIndex = _RtgTopNodeLgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 1, 1, 10),
    _RtgTopNodeLgIndex_Type()
)
rtgTopNodeLgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgTopNodeLgIndex.setStatus("mandatory")
_RtgTopNodeLgTrkObj_ObjectIdentity = ObjectIdentity
rtgTopNodeLgTrkObj = _RtgTopNodeLgTrkObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 2)
)
_RtgTopNodeLgTrkObjRowStatusTable_Object = MibTable
rtgTopNodeLgTrkObjRowStatusTable = _RtgTopNodeLgTrkObjRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rtgTopNodeLgTrkObjRowStatusTable.setStatus("mandatory")
_RtgTopNodeLgTrkObjRowStatusEntry_Object = MibTableRow
rtgTopNodeLgTrkObjRowStatusEntry = _RtgTopNodeLgTrkObjRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 2, 1, 1)
)
rtgTopNodeLgTrkObjRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopNodeIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopNodeLgIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopNodeLgTrkObjIndex"),
)
if mibBuilder.loadTexts:
    rtgTopNodeLgTrkObjRowStatusEntry.setStatus("mandatory")
_RtgTopNodeLgTrkObjRowStatus_Type = RowStatus
_RtgTopNodeLgTrkObjRowStatus_Object = MibTableColumn
rtgTopNodeLgTrkObjRowStatus = _RtgTopNodeLgTrkObjRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 2, 1, 1, 1),
    _RtgTopNodeLgTrkObjRowStatus_Type()
)
rtgTopNodeLgTrkObjRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopNodeLgTrkObjRowStatus.setStatus("mandatory")
_RtgTopNodeLgTrkObjComponentName_Type = DisplayString
_RtgTopNodeLgTrkObjComponentName_Object = MibTableColumn
rtgTopNodeLgTrkObjComponentName = _RtgTopNodeLgTrkObjComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 2, 1, 1, 2),
    _RtgTopNodeLgTrkObjComponentName_Type()
)
rtgTopNodeLgTrkObjComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopNodeLgTrkObjComponentName.setStatus("mandatory")
_RtgTopNodeLgTrkObjStorageType_Type = StorageType
_RtgTopNodeLgTrkObjStorageType_Object = MibTableColumn
rtgTopNodeLgTrkObjStorageType = _RtgTopNodeLgTrkObjStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 2, 1, 1, 4),
    _RtgTopNodeLgTrkObjStorageType_Type()
)
rtgTopNodeLgTrkObjStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopNodeLgTrkObjStorageType.setStatus("mandatory")


class _RtgTopNodeLgTrkObjIndex_Type(Integer32):
    """Custom type rtgTopNodeLgTrkObjIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_RtgTopNodeLgTrkObjIndex_Type.__name__ = "Integer32"
_RtgTopNodeLgTrkObjIndex_Object = MibTableColumn
rtgTopNodeLgTrkObjIndex = _RtgTopNodeLgTrkObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 2, 1, 1, 10),
    _RtgTopNodeLgTrkObjIndex_Type()
)
rtgTopNodeLgTrkObjIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgTopNodeLgTrkObjIndex.setStatus("mandatory")
_RtgTopNodeLgTrkObjOperTable_Object = MibTable
rtgTopNodeLgTrkObjOperTable = _RtgTopNodeLgTrkObjOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 2, 10)
)
if mibBuilder.loadTexts:
    rtgTopNodeLgTrkObjOperTable.setStatus("mandatory")
_RtgTopNodeLgTrkObjOperEntry_Object = MibTableRow
rtgTopNodeLgTrkObjOperEntry = _RtgTopNodeLgTrkObjOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 2, 10, 1)
)
rtgTopNodeLgTrkObjOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopNodeIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopNodeLgIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopNodeLgTrkObjIndex"),
)
if mibBuilder.loadTexts:
    rtgTopNodeLgTrkObjOperEntry.setStatus("mandatory")


class _RtgTopNodeLgTrkObjMaxReservableBwOut_Type(Gauge32):
    """Custom type rtgTopNodeLgTrkObjMaxReservableBwOut based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RtgTopNodeLgTrkObjMaxReservableBwOut_Type.__name__ = "Gauge32"
_RtgTopNodeLgTrkObjMaxReservableBwOut_Object = MibTableColumn
rtgTopNodeLgTrkObjMaxReservableBwOut = _RtgTopNodeLgTrkObjMaxReservableBwOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 2, 10, 1, 1),
    _RtgTopNodeLgTrkObjMaxReservableBwOut_Type()
)
rtgTopNodeLgTrkObjMaxReservableBwOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopNodeLgTrkObjMaxReservableBwOut.setStatus("mandatory")


class _RtgTopNodeLgTrkObjTrunkCost_Type(Unsigned32):
    """Custom type rtgTopNodeLgTrkObjTrunkCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RtgTopNodeLgTrkObjTrunkCost_Type.__name__ = "Unsigned32"
_RtgTopNodeLgTrkObjTrunkCost_Object = MibTableColumn
rtgTopNodeLgTrkObjTrunkCost = _RtgTopNodeLgTrkObjTrunkCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 2, 10, 1, 2),
    _RtgTopNodeLgTrkObjTrunkCost_Type()
)
rtgTopNodeLgTrkObjTrunkCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopNodeLgTrkObjTrunkCost.setStatus("mandatory")


class _RtgTopNodeLgTrkObjTrunkDelay_Type(Unsigned32):
    """Custom type rtgTopNodeLgTrkObjTrunkDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RtgTopNodeLgTrkObjTrunkDelay_Type.__name__ = "Unsigned32"
_RtgTopNodeLgTrkObjTrunkDelay_Object = MibTableColumn
rtgTopNodeLgTrkObjTrunkDelay = _RtgTopNodeLgTrkObjTrunkDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 2, 10, 1, 3),
    _RtgTopNodeLgTrkObjTrunkDelay_Type()
)
rtgTopNodeLgTrkObjTrunkDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopNodeLgTrkObjTrunkDelay.setStatus("mandatory")


class _RtgTopNodeLgTrkObjTrunkSecurity_Type(Unsigned32):
    """Custom type rtgTopNodeLgTrkObjTrunkSecurity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RtgTopNodeLgTrkObjTrunkSecurity_Type.__name__ = "Unsigned32"
_RtgTopNodeLgTrkObjTrunkSecurity_Object = MibTableColumn
rtgTopNodeLgTrkObjTrunkSecurity = _RtgTopNodeLgTrkObjTrunkSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 2, 10, 1, 4),
    _RtgTopNodeLgTrkObjTrunkSecurity_Type()
)
rtgTopNodeLgTrkObjTrunkSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopNodeLgTrkObjTrunkSecurity.setStatus("mandatory")


class _RtgTopNodeLgTrkObjSupportedTrafficTypes_Type(OctetString):
    """Custom type rtgTopNodeLgTrkObjSupportedTrafficTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RtgTopNodeLgTrkObjSupportedTrafficTypes_Type.__name__ = "OctetString"
_RtgTopNodeLgTrkObjSupportedTrafficTypes_Object = MibTableColumn
rtgTopNodeLgTrkObjSupportedTrafficTypes = _RtgTopNodeLgTrkObjSupportedTrafficTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 2, 10, 1, 5),
    _RtgTopNodeLgTrkObjSupportedTrafficTypes_Type()
)
rtgTopNodeLgTrkObjSupportedTrafficTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopNodeLgTrkObjSupportedTrafficTypes.setStatus("mandatory")


class _RtgTopNodeLgTrkObjTrunkType_Type(Integer32):
    """Custom type rtgTopNodeLgTrkObjTrunkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("satellite", 1),
          ("terrestrial", 0),
          ("trunkType1", 2),
          ("trunkType2", 3),
          ("trunkType3", 4),
          ("trunkType4", 5),
          ("trunkType5", 6),
          ("trunkType6", 7))
    )


_RtgTopNodeLgTrkObjTrunkType_Type.__name__ = "Integer32"
_RtgTopNodeLgTrkObjTrunkType_Object = MibTableColumn
rtgTopNodeLgTrkObjTrunkType = _RtgTopNodeLgTrkObjTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 2, 10, 1, 6),
    _RtgTopNodeLgTrkObjTrunkType_Type()
)
rtgTopNodeLgTrkObjTrunkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopNodeLgTrkObjTrunkType.setStatus("mandatory")


class _RtgTopNodeLgTrkObjCustomerParameter_Type(Unsigned32):
    """Custom type rtgTopNodeLgTrkObjCustomerParameter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RtgTopNodeLgTrkObjCustomerParameter_Type.__name__ = "Unsigned32"
_RtgTopNodeLgTrkObjCustomerParameter_Object = MibTableColumn
rtgTopNodeLgTrkObjCustomerParameter = _RtgTopNodeLgTrkObjCustomerParameter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 2, 10, 1, 7),
    _RtgTopNodeLgTrkObjCustomerParameter_Type()
)
rtgTopNodeLgTrkObjCustomerParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopNodeLgTrkObjCustomerParameter.setStatus("mandatory")


class _RtgTopNodeLgTrkObjFarEndTrmLkInstance_Type(Unsigned32):
    """Custom type rtgTopNodeLgTrkObjFarEndTrmLkInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_RtgTopNodeLgTrkObjFarEndTrmLkInstance_Type.__name__ = "Unsigned32"
_RtgTopNodeLgTrkObjFarEndTrmLkInstance_Object = MibTableColumn
rtgTopNodeLgTrkObjFarEndTrmLkInstance = _RtgTopNodeLgTrkObjFarEndTrmLkInstance_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 2, 10, 1, 8),
    _RtgTopNodeLgTrkObjFarEndTrmLkInstance_Type()
)
rtgTopNodeLgTrkObjFarEndTrmLkInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopNodeLgTrkObjFarEndTrmLkInstance.setStatus("mandatory")
_RtgTopNodeLgTrkObjUnresTable_Object = MibTable
rtgTopNodeLgTrkObjUnresTable = _RtgTopNodeLgTrkObjUnresTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 2, 234)
)
if mibBuilder.loadTexts:
    rtgTopNodeLgTrkObjUnresTable.setStatus("mandatory")
_RtgTopNodeLgTrkObjUnresEntry_Object = MibTableRow
rtgTopNodeLgTrkObjUnresEntry = _RtgTopNodeLgTrkObjUnresEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 2, 234, 1)
)
rtgTopNodeLgTrkObjUnresEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopNodeIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopNodeLgIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopNodeLgTrkObjIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopNodeLgTrkObjUnresSetupPriorityIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopNodeLgTrkObjUnresUnreservedBwPartsIndex"),
)
if mibBuilder.loadTexts:
    rtgTopNodeLgTrkObjUnresEntry.setStatus("mandatory")


class _RtgTopNodeLgTrkObjUnresSetupPriorityIndex_Type(Integer32):
    """Custom type rtgTopNodeLgTrkObjUnresSetupPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("bwPartOver255", 0)
    )


_RtgTopNodeLgTrkObjUnresSetupPriorityIndex_Type.__name__ = "Integer32"
_RtgTopNodeLgTrkObjUnresSetupPriorityIndex_Object = MibTableColumn
rtgTopNodeLgTrkObjUnresSetupPriorityIndex = _RtgTopNodeLgTrkObjUnresSetupPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 2, 234, 1, 1),
    _RtgTopNodeLgTrkObjUnresSetupPriorityIndex_Type()
)
rtgTopNodeLgTrkObjUnresSetupPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgTopNodeLgTrkObjUnresSetupPriorityIndex.setStatus("mandatory")


class _RtgTopNodeLgTrkObjUnresUnreservedBwPartsIndex_Type(Integer32):
    """Custom type rtgTopNodeLgTrkObjUnresUnreservedBwPartsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_RtgTopNodeLgTrkObjUnresUnreservedBwPartsIndex_Type.__name__ = "Integer32"
_RtgTopNodeLgTrkObjUnresUnreservedBwPartsIndex_Object = MibTableColumn
rtgTopNodeLgTrkObjUnresUnreservedBwPartsIndex = _RtgTopNodeLgTrkObjUnresUnreservedBwPartsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 2, 234, 1, 2),
    _RtgTopNodeLgTrkObjUnresUnreservedBwPartsIndex_Type()
)
rtgTopNodeLgTrkObjUnresUnreservedBwPartsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtgTopNodeLgTrkObjUnresUnreservedBwPartsIndex.setStatus("mandatory")


class _RtgTopNodeLgTrkObjUnresValue_Type(Unsigned32):
    """Custom type rtgTopNodeLgTrkObjUnresValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RtgTopNodeLgTrkObjUnresValue_Type.__name__ = "Unsigned32"
_RtgTopNodeLgTrkObjUnresValue_Object = MibTableColumn
rtgTopNodeLgTrkObjUnresValue = _RtgTopNodeLgTrkObjUnresValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 2, 234, 1, 3),
    _RtgTopNodeLgTrkObjUnresValue_Type()
)
rtgTopNodeLgTrkObjUnresValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopNodeLgTrkObjUnresValue.setStatus("mandatory")
_RtgTopNodeLgOperTable_Object = MibTable
rtgTopNodeLgOperTable = _RtgTopNodeLgOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 10)
)
if mibBuilder.loadTexts:
    rtgTopNodeLgOperTable.setStatus("mandatory")
_RtgTopNodeLgOperEntry_Object = MibTableRow
rtgTopNodeLgOperEntry = _RtgTopNodeLgOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 10, 1)
)
rtgTopNodeLgOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopNodeIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopNodeLgIndex"),
)
if mibBuilder.loadTexts:
    rtgTopNodeLgOperEntry.setStatus("mandatory")


class _RtgTopNodeLgDelayMetric_Type(Unsigned32):
    """Custom type rtgTopNodeLgDelayMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RtgTopNodeLgDelayMetric_Type.__name__ = "Unsigned32"
_RtgTopNodeLgDelayMetric_Object = MibTableColumn
rtgTopNodeLgDelayMetric = _RtgTopNodeLgDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 10, 1, 1),
    _RtgTopNodeLgDelayMetric_Type()
)
rtgTopNodeLgDelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopNodeLgDelayMetric.setStatus("mandatory")


class _RtgTopNodeLgTputMetric_Type(Unsigned32):
    """Custom type rtgTopNodeLgTputMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RtgTopNodeLgTputMetric_Type.__name__ = "Unsigned32"
_RtgTopNodeLgTputMetric_Object = MibTableColumn
rtgTopNodeLgTputMetric = _RtgTopNodeLgTputMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 10, 1, 2),
    _RtgTopNodeLgTputMetric_Type()
)
rtgTopNodeLgTputMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopNodeLgTputMetric.setStatus("mandatory")
_RtgTopNodeLgLnnTable_Object = MibTable
rtgTopNodeLgLnnTable = _RtgTopNodeLgLnnTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 235)
)
if mibBuilder.loadTexts:
    rtgTopNodeLgLnnTable.setStatus("mandatory")
_RtgTopNodeLgLnnEntry_Object = MibTableRow
rtgTopNodeLgLnnEntry = _RtgTopNodeLgLnnEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 235, 1)
)
rtgTopNodeLgLnnEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopNodeIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopNodeLgIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopNodeLgLnnValue"),
)
if mibBuilder.loadTexts:
    rtgTopNodeLgLnnEntry.setStatus("mandatory")


class _RtgTopNodeLgLnnValue_Type(Integer32):
    """Custom type rtgTopNodeLgLnnValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_RtgTopNodeLgLnnValue_Type.__name__ = "Integer32"
_RtgTopNodeLgLnnValue_Object = MibTableColumn
rtgTopNodeLgLnnValue = _RtgTopNodeLgLnnValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 2, 235, 1, 1),
    _RtgTopNodeLgLnnValue_Type()
)
rtgTopNodeLgLnnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopNodeLgLnnValue.setStatus("mandatory")
_RtgTopNodeOperTable_Object = MibTable
rtgTopNodeOperTable = _RtgTopNodeOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 10)
)
if mibBuilder.loadTexts:
    rtgTopNodeOperTable.setStatus("mandatory")
_RtgTopNodeOperEntry_Object = MibTableRow
rtgTopNodeOperEntry = _RtgTopNodeOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 10, 1)
)
rtgTopNodeOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopNodeIndex"),
)
if mibBuilder.loadTexts:
    rtgTopNodeOperEntry.setStatus("mandatory")


class _RtgTopNodeNodeId_Type(Unsigned32):
    """Custom type rtgTopNodeNodeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_RtgTopNodeNodeId_Type.__name__ = "Unsigned32"
_RtgTopNodeNodeId_Object = MibTableColumn
rtgTopNodeNodeId = _RtgTopNodeNodeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 2, 10, 1, 1),
    _RtgTopNodeNodeId_Type()
)
rtgTopNodeNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopNodeNodeId.setStatus("mandatory")
_RtgTopStatsTable_Object = MibTable
rtgTopStatsTable = _RtgTopStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 11)
)
if mibBuilder.loadTexts:
    rtgTopStatsTable.setStatus("mandatory")
_RtgTopStatsEntry_Object = MibTableRow
rtgTopStatsEntry = _RtgTopStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 11, 1)
)
rtgTopStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgTopIndex"),
)
if mibBuilder.loadTexts:
    rtgTopStatsEntry.setStatus("mandatory")
_RtgTopControlPktRx_Type = Counter32
_RtgTopControlPktRx_Object = MibTableColumn
rtgTopControlPktRx = _RtgTopControlPktRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 11, 1, 1),
    _RtgTopControlPktRx_Type()
)
rtgTopControlPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopControlPktRx.setStatus("mandatory")
_RtgTopControlBytesRx_Type = Counter32
_RtgTopControlBytesRx_Object = MibTableColumn
rtgTopControlBytesRx = _RtgTopControlBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 11, 1, 2),
    _RtgTopControlBytesRx_Type()
)
rtgTopControlBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopControlBytesRx.setStatus("mandatory")
_RtgTopControlPktTx_Type = Counter32
_RtgTopControlPktTx_Object = MibTableColumn
rtgTopControlPktTx = _RtgTopControlPktTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 11, 1, 3),
    _RtgTopControlPktTx_Type()
)
rtgTopControlPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopControlPktTx.setStatus("mandatory")
_RtgTopControlBytesTx_Type = Counter32
_RtgTopControlBytesTx_Object = MibTableColumn
rtgTopControlBytesTx = _RtgTopControlBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 5, 11, 1, 4),
    _RtgTopControlBytesTx_Type()
)
rtgTopControlBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtgTopControlBytesTx.setStatus("mandatory")
_RtgProvTable_Object = MibTable
rtgProvTable = _RtgProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 12)
)
if mibBuilder.loadTexts:
    rtgProvTable.setStatus("mandatory")
_RtgProvEntry_Object = MibTableRow
rtgProvEntry = _RtgProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 12, 1)
)
rtgProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
)
if mibBuilder.loadTexts:
    rtgProvEntry.setStatus("mandatory")


class _RtgTandemTraffic_Type(Integer32):
    """Custom type rtgTandemTraffic based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 0),
          ("denied", 1))
    )


_RtgTandemTraffic_Type.__name__ = "Integer32"
_RtgTandemTraffic_Object = MibTableColumn
rtgTandemTraffic = _RtgTandemTraffic_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 12, 1, 1),
    _RtgTandemTraffic_Type()
)
rtgTandemTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgTandemTraffic.setStatus("mandatory")
_RtgSplittingRegionIdsTable_Object = MibTable
rtgSplittingRegionIdsTable = _RtgSplittingRegionIdsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 407)
)
if mibBuilder.loadTexts:
    rtgSplittingRegionIdsTable.setStatus("mandatory")
_RtgSplittingRegionIdsEntry_Object = MibTableRow
rtgSplittingRegionIdsEntry = _RtgSplittingRegionIdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 407, 1)
)
rtgSplittingRegionIdsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "rtgSplittingRegionIdsValue"),
)
if mibBuilder.loadTexts:
    rtgSplittingRegionIdsEntry.setStatus("mandatory")


class _RtgSplittingRegionIdsValue_Type(Integer32):
    """Custom type rtgSplittingRegionIdsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 126),
    )


_RtgSplittingRegionIdsValue_Type.__name__ = "Integer32"
_RtgSplittingRegionIdsValue_Object = MibTableColumn
rtgSplittingRegionIdsValue = _RtgSplittingRegionIdsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 407, 1, 1),
    _RtgSplittingRegionIdsValue_Type()
)
rtgSplittingRegionIdsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtgSplittingRegionIdsValue.setStatus("mandatory")
_RtgSplittingRegionIdsRowStatus_Type = RowStatus
_RtgSplittingRegionIdsRowStatus_Object = MibTableColumn
rtgSplittingRegionIdsRowStatus = _RtgSplittingRegionIdsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 40, 407, 1, 2),
    _RtgSplittingRegionIdsRowStatus_Type()
)
rtgSplittingRegionIdsRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    rtgSplittingRegionIdsRowStatus.setStatus("mandatory")
_Trm_ObjectIdentity = ObjectIdentity
trm = _Trm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41)
)
_TrmRowStatusTable_Object = MibTable
trmRowStatusTable = _TrmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 1)
)
if mibBuilder.loadTexts:
    trmRowStatusTable.setStatus("mandatory")
_TrmRowStatusEntry_Object = MibTableRow
trmRowStatusEntry = _TrmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 1, 1)
)
trmRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmIndex"),
)
if mibBuilder.loadTexts:
    trmRowStatusEntry.setStatus("mandatory")
_TrmRowStatus_Type = RowStatus
_TrmRowStatus_Object = MibTableColumn
trmRowStatus = _TrmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 1, 1, 1),
    _TrmRowStatus_Type()
)
trmRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmRowStatus.setStatus("mandatory")
_TrmComponentName_Type = DisplayString
_TrmComponentName_Object = MibTableColumn
trmComponentName = _TrmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 1, 1, 2),
    _TrmComponentName_Type()
)
trmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmComponentName.setStatus("mandatory")
_TrmStorageType_Type = StorageType
_TrmStorageType_Object = MibTableColumn
trmStorageType = _TrmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 1, 1, 4),
    _TrmStorageType_Type()
)
trmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmStorageType.setStatus("mandatory")
_TrmIndex_Type = NonReplicated
_TrmIndex_Object = MibTableColumn
trmIndex = _TrmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 1, 1, 10),
    _TrmIndex_Type()
)
trmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trmIndex.setStatus("mandatory")
_TrmLk_ObjectIdentity = ObjectIdentity
trmLk = _TrmLk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 2)
)
_TrmLkRowStatusTable_Object = MibTable
trmLkRowStatusTable = _TrmLkRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 2, 1)
)
if mibBuilder.loadTexts:
    trmLkRowStatusTable.setStatus("mandatory")
_TrmLkRowStatusEntry_Object = MibTableRow
trmLkRowStatusEntry = _TrmLkRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 2, 1, 1)
)
trmLkRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmLkIndex"),
)
if mibBuilder.loadTexts:
    trmLkRowStatusEntry.setStatus("mandatory")
_TrmLkRowStatus_Type = RowStatus
_TrmLkRowStatus_Object = MibTableColumn
trmLkRowStatus = _TrmLkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 2, 1, 1, 1),
    _TrmLkRowStatus_Type()
)
trmLkRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLkRowStatus.setStatus("mandatory")
_TrmLkComponentName_Type = DisplayString
_TrmLkComponentName_Object = MibTableColumn
trmLkComponentName = _TrmLkComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 2, 1, 1, 2),
    _TrmLkComponentName_Type()
)
trmLkComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLkComponentName.setStatus("mandatory")
_TrmLkStorageType_Type = StorageType
_TrmLkStorageType_Object = MibTableColumn
trmLkStorageType = _TrmLkStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 2, 1, 1, 4),
    _TrmLkStorageType_Type()
)
trmLkStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLkStorageType.setStatus("mandatory")


class _TrmLkIndex_Type(Integer32):
    """Custom type trmLkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_TrmLkIndex_Type.__name__ = "Integer32"
_TrmLkIndex_Object = MibTableColumn
trmLkIndex = _TrmLkIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 2, 1, 1, 10),
    _TrmLkIndex_Type()
)
trmLkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trmLkIndex.setStatus("mandatory")
_TrmLkOperTable_Object = MibTable
trmLkOperTable = _TrmLkOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 2, 10)
)
if mibBuilder.loadTexts:
    trmLkOperTable.setStatus("mandatory")
_TrmLkOperEntry_Object = MibTableRow
trmLkOperEntry = _TrmLkOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 2, 10, 1)
)
trmLkOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmLkIndex"),
)
if mibBuilder.loadTexts:
    trmLkOperEntry.setStatus("mandatory")


class _TrmLkStatus_Type(Integer32):
    """Custom type trmLkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("joining", 2),
          ("online", 3))
    )


_TrmLkStatus_Type.__name__ = "Integer32"
_TrmLkStatus_Object = MibTableColumn
trmLkStatus = _TrmLkStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 2, 10, 1, 1),
    _TrmLkStatus_Type()
)
trmLkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLkStatus.setStatus("mandatory")


class _TrmLkThroughput_Type(Gauge32):
    """Custom type trmLkThroughput based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 640000000),
    )


_TrmLkThroughput_Type.__name__ = "Gauge32"
_TrmLkThroughput_Object = MibTableColumn
trmLkThroughput = _TrmLkThroughput_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 2, 10, 1, 2),
    _TrmLkThroughput_Type()
)
trmLkThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLkThroughput.setStatus("mandatory")


class _TrmLkDelay_Type(Gauge32):
    """Custom type trmLkDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1500),
    )


_TrmLkDelay_Type.__name__ = "Gauge32"
_TrmLkDelay_Object = MibTableColumn
trmLkDelay = _TrmLkDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 2, 10, 1, 3),
    _TrmLkDelay_Type()
)
trmLkDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLkDelay.setStatus("obsolete")


class _TrmLkMaxTxUnit_Type(Unsigned32):
    """Custom type trmLkMaxTxUnit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TrmLkMaxTxUnit_Type.__name__ = "Unsigned32"
_TrmLkMaxTxUnit_Object = MibTableColumn
trmLkMaxTxUnit = _TrmLkMaxTxUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 2, 10, 1, 4),
    _TrmLkMaxTxUnit_Type()
)
trmLkMaxTxUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLkMaxTxUnit.setStatus("mandatory")
_TrmLkLinkComponentName_Type = RowPointer
_TrmLkLinkComponentName_Object = MibTableColumn
trmLkLinkComponentName = _TrmLkLinkComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 2, 10, 1, 5),
    _TrmLkLinkComponentName_Type()
)
trmLkLinkComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLkLinkComponentName.setStatus("mandatory")


class _TrmLkDelayUsec_Type(FixedPoint1):
    """Custom type trmLkDelayUsec based on FixedPoint1"""
    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 15000),
    )


_TrmLkDelayUsec_Type.__name__ = "FixedPoint1"
_TrmLkDelayUsec_Object = MibTableColumn
trmLkDelayUsec = _TrmLkDelayUsec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 2, 10, 1, 6),
    _TrmLkDelayUsec_Type()
)
trmLkDelayUsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLkDelayUsec.setStatus("mandatory")
_TrmLkFwdStatsTable_Object = MibTable
trmLkFwdStatsTable = _TrmLkFwdStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 2, 11)
)
if mibBuilder.loadTexts:
    trmLkFwdStatsTable.setStatus("mandatory")
_TrmLkFwdStatsEntry_Object = MibTableRow
trmLkFwdStatsEntry = _TrmLkFwdStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 2, 11, 1)
)
trmLkFwdStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmLkIndex"),
)
if mibBuilder.loadTexts:
    trmLkFwdStatsEntry.setStatus("mandatory")
_TrmLkFciSet_Type = Counter32
_TrmLkFciSet_Object = MibTableColumn
trmLkFciSet = _TrmLkFciSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 2, 11, 1, 1),
    _TrmLkFciSet_Type()
)
trmLkFciSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLkFciSet.setStatus("mandatory")
_TrmLkOverflowAttempts_Type = Counter32
_TrmLkOverflowAttempts_Object = MibTableColumn
trmLkOverflowAttempts = _TrmLkOverflowAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 2, 11, 1, 2),
    _TrmLkOverflowAttempts_Type()
)
trmLkOverflowAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLkOverflowAttempts.setStatus("mandatory")
_TrmLkPathOverflowAttempts_Type = Counter32
_TrmLkPathOverflowAttempts_Object = MibTableColumn
trmLkPathOverflowAttempts = _TrmLkPathOverflowAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 2, 11, 1, 3),
    _TrmLkPathOverflowAttempts_Type()
)
trmLkPathOverflowAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLkPathOverflowAttempts.setStatus("mandatory")
_TrmLkDiscardCongestedTable_Object = MibTable
trmLkDiscardCongestedTable = _TrmLkDiscardCongestedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 2, 280)
)
if mibBuilder.loadTexts:
    trmLkDiscardCongestedTable.setStatus("mandatory")
_TrmLkDiscardCongestedEntry_Object = MibTableRow
trmLkDiscardCongestedEntry = _TrmLkDiscardCongestedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 2, 280, 1)
)
trmLkDiscardCongestedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmLkIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmLkDiscardCongestedIndex"),
)
if mibBuilder.loadTexts:
    trmLkDiscardCongestedEntry.setStatus("mandatory")


class _TrmLkDiscardCongestedIndex_Type(Integer32):
    """Custom type trmLkDiscardCongestedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discardPriority1", 0),
          ("discardPriority2", 1),
          ("discardPriority3", 2))
    )


_TrmLkDiscardCongestedIndex_Type.__name__ = "Integer32"
_TrmLkDiscardCongestedIndex_Object = MibTableColumn
trmLkDiscardCongestedIndex = _TrmLkDiscardCongestedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 2, 280, 1, 1),
    _TrmLkDiscardCongestedIndex_Type()
)
trmLkDiscardCongestedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trmLkDiscardCongestedIndex.setStatus("mandatory")
_TrmLkDiscardCongestedValue_Type = Counter32
_TrmLkDiscardCongestedValue_Object = MibTableColumn
trmLkDiscardCongestedValue = _TrmLkDiscardCongestedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 2, 280, 1, 2),
    _TrmLkDiscardCongestedValue_Type()
)
trmLkDiscardCongestedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLkDiscardCongestedValue.setStatus("mandatory")
_TrmLg_ObjectIdentity = ObjectIdentity
trmLg = _TrmLg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3)
)
_TrmLgRowStatusTable_Object = MibTable
trmLgRowStatusTable = _TrmLgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 1)
)
if mibBuilder.loadTexts:
    trmLgRowStatusTable.setStatus("mandatory")
_TrmLgRowStatusEntry_Object = MibTableRow
trmLgRowStatusEntry = _TrmLgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 1, 1)
)
trmLgRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmLgIndex"),
)
if mibBuilder.loadTexts:
    trmLgRowStatusEntry.setStatus("mandatory")
_TrmLgRowStatus_Type = RowStatus
_TrmLgRowStatus_Object = MibTableColumn
trmLgRowStatus = _TrmLgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 1, 1, 1),
    _TrmLgRowStatus_Type()
)
trmLgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLgRowStatus.setStatus("mandatory")
_TrmLgComponentName_Type = DisplayString
_TrmLgComponentName_Object = MibTableColumn
trmLgComponentName = _TrmLgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 1, 1, 2),
    _TrmLgComponentName_Type()
)
trmLgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLgComponentName.setStatus("mandatory")
_TrmLgStorageType_Type = StorageType
_TrmLgStorageType_Object = MibTableColumn
trmLgStorageType = _TrmLgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 1, 1, 4),
    _TrmLgStorageType_Type()
)
trmLgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLgStorageType.setStatus("mandatory")


class _TrmLgIndex_Type(AsciiStringIndex):
    """Custom type trmLgIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_TrmLgIndex_Type.__name__ = "AsciiStringIndex"
_TrmLgIndex_Object = MibTableColumn
trmLgIndex = _TrmLgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 1, 1, 10),
    _TrmLgIndex_Type()
)
trmLgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trmLgIndex.setStatus("mandatory")
_TrmLgLk_ObjectIdentity = ObjectIdentity
trmLgLk = _TrmLgLk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 2)
)
_TrmLgLkRowStatusTable_Object = MibTable
trmLgLkRowStatusTable = _TrmLgLkRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 2, 1)
)
if mibBuilder.loadTexts:
    trmLgLkRowStatusTable.setStatus("mandatory")
_TrmLgLkRowStatusEntry_Object = MibTableRow
trmLgLkRowStatusEntry = _TrmLgLkRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 2, 1, 1)
)
trmLgLkRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmLgIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmLgLkIndex"),
)
if mibBuilder.loadTexts:
    trmLgLkRowStatusEntry.setStatus("mandatory")
_TrmLgLkRowStatus_Type = RowStatus
_TrmLgLkRowStatus_Object = MibTableColumn
trmLgLkRowStatus = _TrmLgLkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 2, 1, 1, 1),
    _TrmLgLkRowStatus_Type()
)
trmLgLkRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLgLkRowStatus.setStatus("mandatory")
_TrmLgLkComponentName_Type = DisplayString
_TrmLgLkComponentName_Object = MibTableColumn
trmLgLkComponentName = _TrmLgLkComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 2, 1, 1, 2),
    _TrmLgLkComponentName_Type()
)
trmLgLkComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLgLkComponentName.setStatus("mandatory")
_TrmLgLkStorageType_Type = StorageType
_TrmLgLkStorageType_Object = MibTableColumn
trmLgLkStorageType = _TrmLgLkStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 2, 1, 1, 4),
    _TrmLgLkStorageType_Type()
)
trmLgLkStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLgLkStorageType.setStatus("mandatory")


class _TrmLgLkIndex_Type(Integer32):
    """Custom type trmLgLkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_TrmLgLkIndex_Type.__name__ = "Integer32"
_TrmLgLkIndex_Object = MibTableColumn
trmLgLkIndex = _TrmLgLkIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 2, 1, 1, 10),
    _TrmLgLkIndex_Type()
)
trmLgLkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trmLgLkIndex.setStatus("mandatory")
_TrmLgLkOperTable_Object = MibTable
trmLgLkOperTable = _TrmLgLkOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 2, 10)
)
if mibBuilder.loadTexts:
    trmLgLkOperTable.setStatus("mandatory")
_TrmLgLkOperEntry_Object = MibTableRow
trmLgLkOperEntry = _TrmLgLkOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 2, 10, 1)
)
trmLgLkOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmLgIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmLgLkIndex"),
)
if mibBuilder.loadTexts:
    trmLgLkOperEntry.setStatus("mandatory")


class _TrmLgLkStatus_Type(Integer32):
    """Custom type trmLgLkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("joining", 2),
          ("online", 3))
    )


_TrmLgLkStatus_Type.__name__ = "Integer32"
_TrmLgLkStatus_Object = MibTableColumn
trmLgLkStatus = _TrmLgLkStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 2, 10, 1, 1),
    _TrmLgLkStatus_Type()
)
trmLgLkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLgLkStatus.setStatus("mandatory")


class _TrmLgLkThroughput_Type(Gauge32):
    """Custom type trmLgLkThroughput based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 640000000),
    )


_TrmLgLkThroughput_Type.__name__ = "Gauge32"
_TrmLgLkThroughput_Object = MibTableColumn
trmLgLkThroughput = _TrmLgLkThroughput_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 2, 10, 1, 2),
    _TrmLgLkThroughput_Type()
)
trmLgLkThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLgLkThroughput.setStatus("mandatory")


class _TrmLgLkDelay_Type(Gauge32):
    """Custom type trmLgLkDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1500),
    )


_TrmLgLkDelay_Type.__name__ = "Gauge32"
_TrmLgLkDelay_Object = MibTableColumn
trmLgLkDelay = _TrmLgLkDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 2, 10, 1, 3),
    _TrmLgLkDelay_Type()
)
trmLgLkDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLgLkDelay.setStatus("obsolete")


class _TrmLgLkMaxTxUnit_Type(Unsigned32):
    """Custom type trmLgLkMaxTxUnit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TrmLgLkMaxTxUnit_Type.__name__ = "Unsigned32"
_TrmLgLkMaxTxUnit_Object = MibTableColumn
trmLgLkMaxTxUnit = _TrmLgLkMaxTxUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 2, 10, 1, 4),
    _TrmLgLkMaxTxUnit_Type()
)
trmLgLkMaxTxUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLgLkMaxTxUnit.setStatus("mandatory")
_TrmLgLkLinkComponentName_Type = RowPointer
_TrmLgLkLinkComponentName_Object = MibTableColumn
trmLgLkLinkComponentName = _TrmLgLkLinkComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 2, 10, 1, 5),
    _TrmLgLkLinkComponentName_Type()
)
trmLgLkLinkComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLgLkLinkComponentName.setStatus("mandatory")


class _TrmLgLkDelayUsec_Type(FixedPoint1):
    """Custom type trmLgLkDelayUsec based on FixedPoint1"""
    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 15000),
    )


_TrmLgLkDelayUsec_Type.__name__ = "FixedPoint1"
_TrmLgLkDelayUsec_Object = MibTableColumn
trmLgLkDelayUsec = _TrmLgLkDelayUsec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 2, 10, 1, 6),
    _TrmLgLkDelayUsec_Type()
)
trmLgLkDelayUsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLgLkDelayUsec.setStatus("mandatory")
_TrmLgLkFwdStatsTable_Object = MibTable
trmLgLkFwdStatsTable = _TrmLgLkFwdStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 2, 11)
)
if mibBuilder.loadTexts:
    trmLgLkFwdStatsTable.setStatus("mandatory")
_TrmLgLkFwdStatsEntry_Object = MibTableRow
trmLgLkFwdStatsEntry = _TrmLgLkFwdStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 2, 11, 1)
)
trmLgLkFwdStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmLgIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmLgLkIndex"),
)
if mibBuilder.loadTexts:
    trmLgLkFwdStatsEntry.setStatus("mandatory")
_TrmLgLkFciSet_Type = Counter32
_TrmLgLkFciSet_Object = MibTableColumn
trmLgLkFciSet = _TrmLgLkFciSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 2, 11, 1, 1),
    _TrmLgLkFciSet_Type()
)
trmLgLkFciSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLgLkFciSet.setStatus("mandatory")
_TrmLgLkOverflowAttempts_Type = Counter32
_TrmLgLkOverflowAttempts_Object = MibTableColumn
trmLgLkOverflowAttempts = _TrmLgLkOverflowAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 2, 11, 1, 2),
    _TrmLgLkOverflowAttempts_Type()
)
trmLgLkOverflowAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLgLkOverflowAttempts.setStatus("mandatory")
_TrmLgLkPathOverflowAttempts_Type = Counter32
_TrmLgLkPathOverflowAttempts_Object = MibTableColumn
trmLgLkPathOverflowAttempts = _TrmLgLkPathOverflowAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 2, 11, 1, 3),
    _TrmLgLkPathOverflowAttempts_Type()
)
trmLgLkPathOverflowAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLgLkPathOverflowAttempts.setStatus("mandatory")
_TrmLgLkDiscardCongestedTable_Object = MibTable
trmLgLkDiscardCongestedTable = _TrmLgLkDiscardCongestedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 2, 280)
)
if mibBuilder.loadTexts:
    trmLgLkDiscardCongestedTable.setStatus("mandatory")
_TrmLgLkDiscardCongestedEntry_Object = MibTableRow
trmLgLkDiscardCongestedEntry = _TrmLgLkDiscardCongestedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 2, 280, 1)
)
trmLgLkDiscardCongestedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmLgIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmLgLkIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmLgLkDiscardCongestedIndex"),
)
if mibBuilder.loadTexts:
    trmLgLkDiscardCongestedEntry.setStatus("mandatory")


class _TrmLgLkDiscardCongestedIndex_Type(Integer32):
    """Custom type trmLgLkDiscardCongestedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discardPriority1", 0),
          ("discardPriority2", 1),
          ("discardPriority3", 2))
    )


_TrmLgLkDiscardCongestedIndex_Type.__name__ = "Integer32"
_TrmLgLkDiscardCongestedIndex_Object = MibTableColumn
trmLgLkDiscardCongestedIndex = _TrmLgLkDiscardCongestedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 2, 280, 1, 1),
    _TrmLgLkDiscardCongestedIndex_Type()
)
trmLgLkDiscardCongestedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trmLgLkDiscardCongestedIndex.setStatus("mandatory")
_TrmLgLkDiscardCongestedValue_Type = Counter32
_TrmLgLkDiscardCongestedValue_Object = MibTableColumn
trmLgLkDiscardCongestedValue = _TrmLgLkDiscardCongestedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 2, 280, 1, 2),
    _TrmLgLkDiscardCongestedValue_Type()
)
trmLgLkDiscardCongestedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLgLkDiscardCongestedValue.setStatus("mandatory")
_TrmLgLNN_ObjectIdentity = ObjectIdentity
trmLgLNN = _TrmLgLNN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 3)
)
_TrmLgLNNRowStatusTable_Object = MibTable
trmLgLNNRowStatusTable = _TrmLgLNNRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 3, 1)
)
if mibBuilder.loadTexts:
    trmLgLNNRowStatusTable.setStatus("mandatory")
_TrmLgLNNRowStatusEntry_Object = MibTableRow
trmLgLNNRowStatusEntry = _TrmLgLNNRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 3, 1, 1)
)
trmLgLNNRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmLgIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmLgLNNIndex"),
)
if mibBuilder.loadTexts:
    trmLgLNNRowStatusEntry.setStatus("mandatory")
_TrmLgLNNRowStatus_Type = RowStatus
_TrmLgLNNRowStatus_Object = MibTableColumn
trmLgLNNRowStatus = _TrmLgLNNRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 3, 1, 1, 1),
    _TrmLgLNNRowStatus_Type()
)
trmLgLNNRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLgLNNRowStatus.setStatus("mandatory")
_TrmLgLNNComponentName_Type = DisplayString
_TrmLgLNNComponentName_Object = MibTableColumn
trmLgLNNComponentName = _TrmLgLNNComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 3, 1, 1, 2),
    _TrmLgLNNComponentName_Type()
)
trmLgLNNComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLgLNNComponentName.setStatus("mandatory")
_TrmLgLNNStorageType_Type = StorageType
_TrmLgLNNStorageType_Object = MibTableColumn
trmLgLNNStorageType = _TrmLgLNNStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 3, 1, 1, 4),
    _TrmLgLNNStorageType_Type()
)
trmLgLNNStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLgLNNStorageType.setStatus("mandatory")


class _TrmLgLNNIndex_Type(Integer32):
    """Custom type trmLgLNNIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_TrmLgLNNIndex_Type.__name__ = "Integer32"
_TrmLgLNNIndex_Object = MibTableColumn
trmLgLNNIndex = _TrmLgLNNIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 3, 1, 1, 10),
    _TrmLgLNNIndex_Type()
)
trmLgLNNIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trmLgLNNIndex.setStatus("mandatory")
_TrmLgLNNOperTable_Object = MibTable
trmLgLNNOperTable = _TrmLgLNNOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 3, 10)
)
if mibBuilder.loadTexts:
    trmLgLNNOperTable.setStatus("mandatory")
_TrmLgLNNOperEntry_Object = MibTableRow
trmLgLNNOperEntry = _TrmLgLNNOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 3, 10, 1)
)
trmLgLNNOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmLgIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "trmLgLNNIndex"),
)
if mibBuilder.loadTexts:
    trmLgLNNOperEntry.setStatus("mandatory")


class _TrmLgLNNLinkType_Type(Integer32):
    """Custom type trmLgLNNLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalGateway", 2),
          ("internalGateway", 1),
          ("trunk", 0))
    )


_TrmLgLNNLinkType_Type.__name__ = "Integer32"
_TrmLgLNNLinkType_Object = MibTableColumn
trmLgLNNLinkType = _TrmLgLNNLinkType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 3, 10, 1, 1),
    _TrmLgLNNLinkType_Type()
)
trmLgLNNLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLgLNNLinkType.setStatus("mandatory")
_TrmLgLNNAddressPlanComponentName_Type = RowPointer
_TrmLgLNNAddressPlanComponentName_Object = MibTableColumn
trmLgLNNAddressPlanComponentName = _TrmLgLNNAddressPlanComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 41, 3, 3, 10, 1, 2),
    _TrmLgLNNAddressPlanComponentName_Type()
)
trmLgLNNAddressPlanComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmLgLNNAddressPlanComponentName.setStatus("mandatory")
_Npi_ObjectIdentity = ObjectIdentity
npi = _Npi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 43)
)
_NpiRowStatusTable_Object = MibTable
npiRowStatusTable = _NpiRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 43, 1)
)
if mibBuilder.loadTexts:
    npiRowStatusTable.setStatus("mandatory")
_NpiRowStatusEntry_Object = MibTableRow
npiRowStatusEntry = _NpiRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 43, 1, 1)
)
npiRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "npiIndex"),
)
if mibBuilder.loadTexts:
    npiRowStatusEntry.setStatus("mandatory")
_NpiRowStatus_Type = RowStatus
_NpiRowStatus_Object = MibTableColumn
npiRowStatus = _NpiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 43, 1, 1, 1),
    _NpiRowStatus_Type()
)
npiRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npiRowStatus.setStatus("mandatory")
_NpiComponentName_Type = DisplayString
_NpiComponentName_Object = MibTableColumn
npiComponentName = _NpiComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 43, 1, 1, 2),
    _NpiComponentName_Type()
)
npiComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npiComponentName.setStatus("mandatory")
_NpiStorageType_Type = StorageType
_NpiStorageType_Object = MibTableColumn
npiStorageType = _NpiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 43, 1, 1, 4),
    _NpiStorageType_Type()
)
npiStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npiStorageType.setStatus("mandatory")


class _NpiIndex_Type(Integer32):
    """Custom type npiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_NpiIndex_Type.__name__ = "Integer32"
_NpiIndex_Object = MibTableColumn
npiIndex = _NpiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 43, 1, 1, 10),
    _NpiIndex_Type()
)
npiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    npiIndex.setStatus("mandatory")
_NpiDna_ObjectIdentity = ObjectIdentity
npiDna = _NpiDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 43, 2)
)
_NpiDnaRowStatusTable_Object = MibTable
npiDnaRowStatusTable = _NpiDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 43, 2, 1)
)
if mibBuilder.loadTexts:
    npiDnaRowStatusTable.setStatus("mandatory")
_NpiDnaRowStatusEntry_Object = MibTableRow
npiDnaRowStatusEntry = _NpiDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 43, 2, 1, 1)
)
npiDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "npiIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "npiDnaIndex"),
)
if mibBuilder.loadTexts:
    npiDnaRowStatusEntry.setStatus("mandatory")
_NpiDnaRowStatus_Type = RowStatus
_NpiDnaRowStatus_Object = MibTableColumn
npiDnaRowStatus = _NpiDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 43, 2, 1, 1, 1),
    _NpiDnaRowStatus_Type()
)
npiDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npiDnaRowStatus.setStatus("mandatory")
_NpiDnaComponentName_Type = DisplayString
_NpiDnaComponentName_Object = MibTableColumn
npiDnaComponentName = _NpiDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 43, 2, 1, 1, 2),
    _NpiDnaComponentName_Type()
)
npiDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npiDnaComponentName.setStatus("mandatory")
_NpiDnaStorageType_Type = StorageType
_NpiDnaStorageType_Object = MibTableColumn
npiDnaStorageType = _NpiDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 43, 2, 1, 1, 4),
    _NpiDnaStorageType_Type()
)
npiDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npiDnaStorageType.setStatus("mandatory")


class _NpiDnaIndex_Type(DigitString):
    """Custom type npiDnaIndex based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_NpiDnaIndex_Type.__name__ = "DigitString"
_NpiDnaIndex_Object = MibTableColumn
npiDnaIndex = _NpiDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 43, 2, 1, 1, 10),
    _NpiDnaIndex_Type()
)
npiDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    npiDnaIndex.setStatus("mandatory")
_NpiDnaInfoTable_Object = MibTable
npiDnaInfoTable = _NpiDnaInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 43, 2, 10)
)
if mibBuilder.loadTexts:
    npiDnaInfoTable.setStatus("mandatory")
_NpiDnaInfoEntry_Object = MibTableRow
npiDnaInfoEntry = _NpiDnaInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 43, 2, 10, 1)
)
npiDnaInfoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "npiIndex"),
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "npiDnaIndex"),
)
if mibBuilder.loadTexts:
    npiDnaInfoEntry.setStatus("mandatory")
_NpiDnaDestinationName_Type = RowPointer
_NpiDnaDestinationName_Object = MibTableColumn
npiDnaDestinationName = _NpiDnaDestinationName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 43, 2, 10, 1, 1),
    _NpiDnaDestinationName_Type()
)
npiDnaDestinationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npiDnaDestinationName.setStatus("mandatory")
_NpiStatsTable_Object = MibTable
npiStatsTable = _NpiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 43, 10)
)
if mibBuilder.loadTexts:
    npiStatsTable.setStatus("mandatory")
_NpiStatsEntry_Object = MibTableRow
npiStatsEntry = _NpiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 43, 10, 1)
)
npiStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BaseRoutingMIB", "npiIndex"),
)
if mibBuilder.loadTexts:
    npiStatsEntry.setStatus("mandatory")


class _NpiTotalDnas_Type(Unsigned32):
    """Custom type npiTotalDnas based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NpiTotalDnas_Type.__name__ = "Unsigned32"
_NpiTotalDnas_Object = MibTableColumn
npiTotalDnas = _NpiTotalDnas_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 43, 10, 1, 1),
    _NpiTotalDnas_Type()
)
npiTotalDnas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npiTotalDnas.setStatus("mandatory")
_BaseRoutingMIB_ObjectIdentity = ObjectIdentity
baseRoutingMIB = _BaseRoutingMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 18)
)
_BaseRoutingGroup_ObjectIdentity = ObjectIdentity
baseRoutingGroup = _BaseRoutingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 18, 1)
)
_BaseRoutingGroupBE_ObjectIdentity = ObjectIdentity
baseRoutingGroupBE = _BaseRoutingGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 18, 1, 5)
)
_BaseRoutingGroupBE00_ObjectIdentity = ObjectIdentity
baseRoutingGroupBE00 = _BaseRoutingGroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 18, 1, 5, 1)
)
_BaseRoutingGroupBE00A_ObjectIdentity = ObjectIdentity
baseRoutingGroupBE00A = _BaseRoutingGroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 18, 1, 5, 1, 2)
)
_BaseRoutingCapabilities_ObjectIdentity = ObjectIdentity
baseRoutingCapabilities = _BaseRoutingCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 18, 3)
)
_BaseRoutingCapabilitiesBE_ObjectIdentity = ObjectIdentity
baseRoutingCapabilitiesBE = _BaseRoutingCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 18, 3, 5)
)
_BaseRoutingCapabilitiesBE00_ObjectIdentity = ObjectIdentity
baseRoutingCapabilitiesBE00 = _BaseRoutingCapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 18, 3, 5, 1)
)
_BaseRoutingCapabilitiesBE00A_ObjectIdentity = ObjectIdentity
baseRoutingCapabilitiesBE00A = _BaseRoutingCapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 18, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-BaseRoutingMIB",
    **{"rtg": rtg,
       "rtgRowStatusTable": rtgRowStatusTable,
       "rtgRowStatusEntry": rtgRowStatusEntry,
       "rtgRowStatus": rtgRowStatus,
       "rtgComponentName": rtgComponentName,
       "rtgStorageType": rtgStorageType,
       "rtgIndex": rtgIndex,
       "rtgTop": rtgTop,
       "rtgTopRowStatusTable": rtgTopRowStatusTable,
       "rtgTopRowStatusEntry": rtgTopRowStatusEntry,
       "rtgTopRowStatus": rtgTopRowStatus,
       "rtgTopComponentName": rtgTopComponentName,
       "rtgTopStorageType": rtgTopStorageType,
       "rtgTopIndex": rtgTopIndex,
       "rtgTopNode": rtgTopNode,
       "rtgTopNodeRowStatusTable": rtgTopNodeRowStatusTable,
       "rtgTopNodeRowStatusEntry": rtgTopNodeRowStatusEntry,
       "rtgTopNodeRowStatus": rtgTopNodeRowStatus,
       "rtgTopNodeComponentName": rtgTopNodeComponentName,
       "rtgTopNodeStorageType": rtgTopNodeStorageType,
       "rtgTopNodeIndex": rtgTopNodeIndex,
       "rtgTopNodeLg": rtgTopNodeLg,
       "rtgTopNodeLgRowStatusTable": rtgTopNodeLgRowStatusTable,
       "rtgTopNodeLgRowStatusEntry": rtgTopNodeLgRowStatusEntry,
       "rtgTopNodeLgRowStatus": rtgTopNodeLgRowStatus,
       "rtgTopNodeLgComponentName": rtgTopNodeLgComponentName,
       "rtgTopNodeLgStorageType": rtgTopNodeLgStorageType,
       "rtgTopNodeLgIndex": rtgTopNodeLgIndex,
       "rtgTopNodeLgTrkObj": rtgTopNodeLgTrkObj,
       "rtgTopNodeLgTrkObjRowStatusTable": rtgTopNodeLgTrkObjRowStatusTable,
       "rtgTopNodeLgTrkObjRowStatusEntry": rtgTopNodeLgTrkObjRowStatusEntry,
       "rtgTopNodeLgTrkObjRowStatus": rtgTopNodeLgTrkObjRowStatus,
       "rtgTopNodeLgTrkObjComponentName": rtgTopNodeLgTrkObjComponentName,
       "rtgTopNodeLgTrkObjStorageType": rtgTopNodeLgTrkObjStorageType,
       "rtgTopNodeLgTrkObjIndex": rtgTopNodeLgTrkObjIndex,
       "rtgTopNodeLgTrkObjOperTable": rtgTopNodeLgTrkObjOperTable,
       "rtgTopNodeLgTrkObjOperEntry": rtgTopNodeLgTrkObjOperEntry,
       "rtgTopNodeLgTrkObjMaxReservableBwOut": rtgTopNodeLgTrkObjMaxReservableBwOut,
       "rtgTopNodeLgTrkObjTrunkCost": rtgTopNodeLgTrkObjTrunkCost,
       "rtgTopNodeLgTrkObjTrunkDelay": rtgTopNodeLgTrkObjTrunkDelay,
       "rtgTopNodeLgTrkObjTrunkSecurity": rtgTopNodeLgTrkObjTrunkSecurity,
       "rtgTopNodeLgTrkObjSupportedTrafficTypes": rtgTopNodeLgTrkObjSupportedTrafficTypes,
       "rtgTopNodeLgTrkObjTrunkType": rtgTopNodeLgTrkObjTrunkType,
       "rtgTopNodeLgTrkObjCustomerParameter": rtgTopNodeLgTrkObjCustomerParameter,
       "rtgTopNodeLgTrkObjFarEndTrmLkInstance": rtgTopNodeLgTrkObjFarEndTrmLkInstance,
       "rtgTopNodeLgTrkObjUnresTable": rtgTopNodeLgTrkObjUnresTable,
       "rtgTopNodeLgTrkObjUnresEntry": rtgTopNodeLgTrkObjUnresEntry,
       "rtgTopNodeLgTrkObjUnresSetupPriorityIndex": rtgTopNodeLgTrkObjUnresSetupPriorityIndex,
       "rtgTopNodeLgTrkObjUnresUnreservedBwPartsIndex": rtgTopNodeLgTrkObjUnresUnreservedBwPartsIndex,
       "rtgTopNodeLgTrkObjUnresValue": rtgTopNodeLgTrkObjUnresValue,
       "rtgTopNodeLgOperTable": rtgTopNodeLgOperTable,
       "rtgTopNodeLgOperEntry": rtgTopNodeLgOperEntry,
       "rtgTopNodeLgDelayMetric": rtgTopNodeLgDelayMetric,
       "rtgTopNodeLgTputMetric": rtgTopNodeLgTputMetric,
       "rtgTopNodeLgLnnTable": rtgTopNodeLgLnnTable,
       "rtgTopNodeLgLnnEntry": rtgTopNodeLgLnnEntry,
       "rtgTopNodeLgLnnValue": rtgTopNodeLgLnnValue,
       "rtgTopNodeOperTable": rtgTopNodeOperTable,
       "rtgTopNodeOperEntry": rtgTopNodeOperEntry,
       "rtgTopNodeNodeId": rtgTopNodeNodeId,
       "rtgTopStatsTable": rtgTopStatsTable,
       "rtgTopStatsEntry": rtgTopStatsEntry,
       "rtgTopControlPktRx": rtgTopControlPktRx,
       "rtgTopControlBytesRx": rtgTopControlBytesRx,
       "rtgTopControlPktTx": rtgTopControlPktTx,
       "rtgTopControlBytesTx": rtgTopControlBytesTx,
       "rtgProvTable": rtgProvTable,
       "rtgProvEntry": rtgProvEntry,
       "rtgTandemTraffic": rtgTandemTraffic,
       "rtgSplittingRegionIdsTable": rtgSplittingRegionIdsTable,
       "rtgSplittingRegionIdsEntry": rtgSplittingRegionIdsEntry,
       "rtgSplittingRegionIdsValue": rtgSplittingRegionIdsValue,
       "rtgSplittingRegionIdsRowStatus": rtgSplittingRegionIdsRowStatus,
       "trm": trm,
       "trmRowStatusTable": trmRowStatusTable,
       "trmRowStatusEntry": trmRowStatusEntry,
       "trmRowStatus": trmRowStatus,
       "trmComponentName": trmComponentName,
       "trmStorageType": trmStorageType,
       "trmIndex": trmIndex,
       "trmLk": trmLk,
       "trmLkRowStatusTable": trmLkRowStatusTable,
       "trmLkRowStatusEntry": trmLkRowStatusEntry,
       "trmLkRowStatus": trmLkRowStatus,
       "trmLkComponentName": trmLkComponentName,
       "trmLkStorageType": trmLkStorageType,
       "trmLkIndex": trmLkIndex,
       "trmLkOperTable": trmLkOperTable,
       "trmLkOperEntry": trmLkOperEntry,
       "trmLkStatus": trmLkStatus,
       "trmLkThroughput": trmLkThroughput,
       "trmLkDelay": trmLkDelay,
       "trmLkMaxTxUnit": trmLkMaxTxUnit,
       "trmLkLinkComponentName": trmLkLinkComponentName,
       "trmLkDelayUsec": trmLkDelayUsec,
       "trmLkFwdStatsTable": trmLkFwdStatsTable,
       "trmLkFwdStatsEntry": trmLkFwdStatsEntry,
       "trmLkFciSet": trmLkFciSet,
       "trmLkOverflowAttempts": trmLkOverflowAttempts,
       "trmLkPathOverflowAttempts": trmLkPathOverflowAttempts,
       "trmLkDiscardCongestedTable": trmLkDiscardCongestedTable,
       "trmLkDiscardCongestedEntry": trmLkDiscardCongestedEntry,
       "trmLkDiscardCongestedIndex": trmLkDiscardCongestedIndex,
       "trmLkDiscardCongestedValue": trmLkDiscardCongestedValue,
       "trmLg": trmLg,
       "trmLgRowStatusTable": trmLgRowStatusTable,
       "trmLgRowStatusEntry": trmLgRowStatusEntry,
       "trmLgRowStatus": trmLgRowStatus,
       "trmLgComponentName": trmLgComponentName,
       "trmLgStorageType": trmLgStorageType,
       "trmLgIndex": trmLgIndex,
       "trmLgLk": trmLgLk,
       "trmLgLkRowStatusTable": trmLgLkRowStatusTable,
       "trmLgLkRowStatusEntry": trmLgLkRowStatusEntry,
       "trmLgLkRowStatus": trmLgLkRowStatus,
       "trmLgLkComponentName": trmLgLkComponentName,
       "trmLgLkStorageType": trmLgLkStorageType,
       "trmLgLkIndex": trmLgLkIndex,
       "trmLgLkOperTable": trmLgLkOperTable,
       "trmLgLkOperEntry": trmLgLkOperEntry,
       "trmLgLkStatus": trmLgLkStatus,
       "trmLgLkThroughput": trmLgLkThroughput,
       "trmLgLkDelay": trmLgLkDelay,
       "trmLgLkMaxTxUnit": trmLgLkMaxTxUnit,
       "trmLgLkLinkComponentName": trmLgLkLinkComponentName,
       "trmLgLkDelayUsec": trmLgLkDelayUsec,
       "trmLgLkFwdStatsTable": trmLgLkFwdStatsTable,
       "trmLgLkFwdStatsEntry": trmLgLkFwdStatsEntry,
       "trmLgLkFciSet": trmLgLkFciSet,
       "trmLgLkOverflowAttempts": trmLgLkOverflowAttempts,
       "trmLgLkPathOverflowAttempts": trmLgLkPathOverflowAttempts,
       "trmLgLkDiscardCongestedTable": trmLgLkDiscardCongestedTable,
       "trmLgLkDiscardCongestedEntry": trmLgLkDiscardCongestedEntry,
       "trmLgLkDiscardCongestedIndex": trmLgLkDiscardCongestedIndex,
       "trmLgLkDiscardCongestedValue": trmLgLkDiscardCongestedValue,
       "trmLgLNN": trmLgLNN,
       "trmLgLNNRowStatusTable": trmLgLNNRowStatusTable,
       "trmLgLNNRowStatusEntry": trmLgLNNRowStatusEntry,
       "trmLgLNNRowStatus": trmLgLNNRowStatus,
       "trmLgLNNComponentName": trmLgLNNComponentName,
       "trmLgLNNStorageType": trmLgLNNStorageType,
       "trmLgLNNIndex": trmLgLNNIndex,
       "trmLgLNNOperTable": trmLgLNNOperTable,
       "trmLgLNNOperEntry": trmLgLNNOperEntry,
       "trmLgLNNLinkType": trmLgLNNLinkType,
       "trmLgLNNAddressPlanComponentName": trmLgLNNAddressPlanComponentName,
       "npi": npi,
       "npiRowStatusTable": npiRowStatusTable,
       "npiRowStatusEntry": npiRowStatusEntry,
       "npiRowStatus": npiRowStatus,
       "npiComponentName": npiComponentName,
       "npiStorageType": npiStorageType,
       "npiIndex": npiIndex,
       "npiDna": npiDna,
       "npiDnaRowStatusTable": npiDnaRowStatusTable,
       "npiDnaRowStatusEntry": npiDnaRowStatusEntry,
       "npiDnaRowStatus": npiDnaRowStatus,
       "npiDnaComponentName": npiDnaComponentName,
       "npiDnaStorageType": npiDnaStorageType,
       "npiDnaIndex": npiDnaIndex,
       "npiDnaInfoTable": npiDnaInfoTable,
       "npiDnaInfoEntry": npiDnaInfoEntry,
       "npiDnaDestinationName": npiDnaDestinationName,
       "npiStatsTable": npiStatsTable,
       "npiStatsEntry": npiStatsEntry,
       "npiTotalDnas": npiTotalDnas,
       "baseRoutingMIB": baseRoutingMIB,
       "baseRoutingGroup": baseRoutingGroup,
       "baseRoutingGroupBE": baseRoutingGroupBE,
       "baseRoutingGroupBE00": baseRoutingGroupBE00,
       "baseRoutingGroupBE00A": baseRoutingGroupBE00A,
       "baseRoutingCapabilities": baseRoutingCapabilities,
       "baseRoutingCapabilitiesBE": baseRoutingCapabilitiesBE,
       "baseRoutingCapabilitiesBE00": baseRoutingCapabilitiesBE00,
       "baseRoutingCapabilitiesBE00A": baseRoutingCapabilitiesBE00A}
)
