# SNMP MIB module (Nortel-MsCarrier-MscPassport-BaseRoutingMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-BaseRoutingMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:57 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
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
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiStringIndex",
    "DigitString",
    "FixedPoint1",
    "NonReplicated")

(mscComponents,
 mscPassportMIBs) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscComponents",
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

_MscRtg_ObjectIdentity = ObjectIdentity
mscRtg = _MscRtg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40)
)
_MscRtgRowStatusTable_Object = MibTable
mscRtgRowStatusTable = _MscRtgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 1)
)
if mibBuilder.loadTexts:
    mscRtgRowStatusTable.setStatus("mandatory")
_MscRtgRowStatusEntry_Object = MibTableRow
mscRtgRowStatusEntry = _MscRtgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 1, 1)
)
mscRtgRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
)
if mibBuilder.loadTexts:
    mscRtgRowStatusEntry.setStatus("mandatory")
_MscRtgRowStatus_Type = RowStatus
_MscRtgRowStatus_Object = MibTableColumn
mscRtgRowStatus = _MscRtgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 1, 1, 1),
    _MscRtgRowStatus_Type()
)
mscRtgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgRowStatus.setStatus("mandatory")
_MscRtgComponentName_Type = DisplayString
_MscRtgComponentName_Object = MibTableColumn
mscRtgComponentName = _MscRtgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 1, 1, 2),
    _MscRtgComponentName_Type()
)
mscRtgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgComponentName.setStatus("mandatory")
_MscRtgStorageType_Type = StorageType
_MscRtgStorageType_Object = MibTableColumn
mscRtgStorageType = _MscRtgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 1, 1, 4),
    _MscRtgStorageType_Type()
)
mscRtgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgStorageType.setStatus("mandatory")
_MscRtgIndex_Type = NonReplicated
_MscRtgIndex_Object = MibTableColumn
mscRtgIndex = _MscRtgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 1, 1, 10),
    _MscRtgIndex_Type()
)
mscRtgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgIndex.setStatus("mandatory")
_MscRtgTop_ObjectIdentity = ObjectIdentity
mscRtgTop = _MscRtgTop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5)
)
_MscRtgTopRowStatusTable_Object = MibTable
mscRtgTopRowStatusTable = _MscRtgTopRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 1)
)
if mibBuilder.loadTexts:
    mscRtgTopRowStatusTable.setStatus("mandatory")
_MscRtgTopRowStatusEntry_Object = MibTableRow
mscRtgTopRowStatusEntry = _MscRtgTopRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 1, 1)
)
mscRtgTopRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopIndex"),
)
if mibBuilder.loadTexts:
    mscRtgTopRowStatusEntry.setStatus("mandatory")
_MscRtgTopRowStatus_Type = RowStatus
_MscRtgTopRowStatus_Object = MibTableColumn
mscRtgTopRowStatus = _MscRtgTopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 1, 1, 1),
    _MscRtgTopRowStatus_Type()
)
mscRtgTopRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopRowStatus.setStatus("mandatory")
_MscRtgTopComponentName_Type = DisplayString
_MscRtgTopComponentName_Object = MibTableColumn
mscRtgTopComponentName = _MscRtgTopComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 1, 1, 2),
    _MscRtgTopComponentName_Type()
)
mscRtgTopComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopComponentName.setStatus("mandatory")
_MscRtgTopStorageType_Type = StorageType
_MscRtgTopStorageType_Object = MibTableColumn
mscRtgTopStorageType = _MscRtgTopStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 1, 1, 4),
    _MscRtgTopStorageType_Type()
)
mscRtgTopStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopStorageType.setStatus("mandatory")
_MscRtgTopIndex_Type = NonReplicated
_MscRtgTopIndex_Object = MibTableColumn
mscRtgTopIndex = _MscRtgTopIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 1, 1, 10),
    _MscRtgTopIndex_Type()
)
mscRtgTopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgTopIndex.setStatus("mandatory")
_MscRtgTopNode_ObjectIdentity = ObjectIdentity
mscRtgTopNode = _MscRtgTopNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2)
)
_MscRtgTopNodeRowStatusTable_Object = MibTable
mscRtgTopNodeRowStatusTable = _MscRtgTopNodeRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mscRtgTopNodeRowStatusTable.setStatus("mandatory")
_MscRtgTopNodeRowStatusEntry_Object = MibTableRow
mscRtgTopNodeRowStatusEntry = _MscRtgTopNodeRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 1, 1)
)
mscRtgTopNodeRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopNodeIndex"),
)
if mibBuilder.loadTexts:
    mscRtgTopNodeRowStatusEntry.setStatus("mandatory")
_MscRtgTopNodeRowStatus_Type = RowStatus
_MscRtgTopNodeRowStatus_Object = MibTableColumn
mscRtgTopNodeRowStatus = _MscRtgTopNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 1, 1, 1),
    _MscRtgTopNodeRowStatus_Type()
)
mscRtgTopNodeRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopNodeRowStatus.setStatus("mandatory")
_MscRtgTopNodeComponentName_Type = DisplayString
_MscRtgTopNodeComponentName_Object = MibTableColumn
mscRtgTopNodeComponentName = _MscRtgTopNodeComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 1, 1, 2),
    _MscRtgTopNodeComponentName_Type()
)
mscRtgTopNodeComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopNodeComponentName.setStatus("mandatory")
_MscRtgTopNodeStorageType_Type = StorageType
_MscRtgTopNodeStorageType_Object = MibTableColumn
mscRtgTopNodeStorageType = _MscRtgTopNodeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 1, 1, 4),
    _MscRtgTopNodeStorageType_Type()
)
mscRtgTopNodeStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopNodeStorageType.setStatus("mandatory")


class _MscRtgTopNodeIndex_Type(AsciiStringIndex):
    """Custom type mscRtgTopNodeIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_MscRtgTopNodeIndex_Type.__name__ = "AsciiStringIndex"
_MscRtgTopNodeIndex_Object = MibTableColumn
mscRtgTopNodeIndex = _MscRtgTopNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 1, 1, 10),
    _MscRtgTopNodeIndex_Type()
)
mscRtgTopNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgTopNodeIndex.setStatus("mandatory")
_MscRtgTopNodeLg_ObjectIdentity = ObjectIdentity
mscRtgTopNodeLg = _MscRtgTopNodeLg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2)
)
_MscRtgTopNodeLgRowStatusTable_Object = MibTable
mscRtgTopNodeLgRowStatusTable = _MscRtgTopNodeLgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscRtgTopNodeLgRowStatusTable.setStatus("mandatory")
_MscRtgTopNodeLgRowStatusEntry_Object = MibTableRow
mscRtgTopNodeLgRowStatusEntry = _MscRtgTopNodeLgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 1, 1)
)
mscRtgTopNodeLgRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopNodeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopNodeLgIndex"),
)
if mibBuilder.loadTexts:
    mscRtgTopNodeLgRowStatusEntry.setStatus("mandatory")
_MscRtgTopNodeLgRowStatus_Type = RowStatus
_MscRtgTopNodeLgRowStatus_Object = MibTableColumn
mscRtgTopNodeLgRowStatus = _MscRtgTopNodeLgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 1, 1, 1),
    _MscRtgTopNodeLgRowStatus_Type()
)
mscRtgTopNodeLgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopNodeLgRowStatus.setStatus("mandatory")
_MscRtgTopNodeLgComponentName_Type = DisplayString
_MscRtgTopNodeLgComponentName_Object = MibTableColumn
mscRtgTopNodeLgComponentName = _MscRtgTopNodeLgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 1, 1, 2),
    _MscRtgTopNodeLgComponentName_Type()
)
mscRtgTopNodeLgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopNodeLgComponentName.setStatus("mandatory")
_MscRtgTopNodeLgStorageType_Type = StorageType
_MscRtgTopNodeLgStorageType_Object = MibTableColumn
mscRtgTopNodeLgStorageType = _MscRtgTopNodeLgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 1, 1, 4),
    _MscRtgTopNodeLgStorageType_Type()
)
mscRtgTopNodeLgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopNodeLgStorageType.setStatus("mandatory")


class _MscRtgTopNodeLgIndex_Type(AsciiStringIndex):
    """Custom type mscRtgTopNodeLgIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_MscRtgTopNodeLgIndex_Type.__name__ = "AsciiStringIndex"
_MscRtgTopNodeLgIndex_Object = MibTableColumn
mscRtgTopNodeLgIndex = _MscRtgTopNodeLgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 1, 1, 10),
    _MscRtgTopNodeLgIndex_Type()
)
mscRtgTopNodeLgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgTopNodeLgIndex.setStatus("mandatory")
_MscRtgTopNodeLgTrkObj_ObjectIdentity = ObjectIdentity
mscRtgTopNodeLgTrkObj = _MscRtgTopNodeLgTrkObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 2)
)
_MscRtgTopNodeLgTrkObjRowStatusTable_Object = MibTable
mscRtgTopNodeLgTrkObjRowStatusTable = _MscRtgTopNodeLgTrkObjRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscRtgTopNodeLgTrkObjRowStatusTable.setStatus("mandatory")
_MscRtgTopNodeLgTrkObjRowStatusEntry_Object = MibTableRow
mscRtgTopNodeLgTrkObjRowStatusEntry = _MscRtgTopNodeLgTrkObjRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 2, 1, 1)
)
mscRtgTopNodeLgTrkObjRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopNodeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopNodeLgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopNodeLgTrkObjIndex"),
)
if mibBuilder.loadTexts:
    mscRtgTopNodeLgTrkObjRowStatusEntry.setStatus("mandatory")
_MscRtgTopNodeLgTrkObjRowStatus_Type = RowStatus
_MscRtgTopNodeLgTrkObjRowStatus_Object = MibTableColumn
mscRtgTopNodeLgTrkObjRowStatus = _MscRtgTopNodeLgTrkObjRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 2, 1, 1, 1),
    _MscRtgTopNodeLgTrkObjRowStatus_Type()
)
mscRtgTopNodeLgTrkObjRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopNodeLgTrkObjRowStatus.setStatus("mandatory")
_MscRtgTopNodeLgTrkObjComponentName_Type = DisplayString
_MscRtgTopNodeLgTrkObjComponentName_Object = MibTableColumn
mscRtgTopNodeLgTrkObjComponentName = _MscRtgTopNodeLgTrkObjComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 2, 1, 1, 2),
    _MscRtgTopNodeLgTrkObjComponentName_Type()
)
mscRtgTopNodeLgTrkObjComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopNodeLgTrkObjComponentName.setStatus("mandatory")
_MscRtgTopNodeLgTrkObjStorageType_Type = StorageType
_MscRtgTopNodeLgTrkObjStorageType_Object = MibTableColumn
mscRtgTopNodeLgTrkObjStorageType = _MscRtgTopNodeLgTrkObjStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 2, 1, 1, 4),
    _MscRtgTopNodeLgTrkObjStorageType_Type()
)
mscRtgTopNodeLgTrkObjStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopNodeLgTrkObjStorageType.setStatus("mandatory")


class _MscRtgTopNodeLgTrkObjIndex_Type(Integer32):
    """Custom type mscRtgTopNodeLgTrkObjIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_MscRtgTopNodeLgTrkObjIndex_Type.__name__ = "Integer32"
_MscRtgTopNodeLgTrkObjIndex_Object = MibTableColumn
mscRtgTopNodeLgTrkObjIndex = _MscRtgTopNodeLgTrkObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 2, 1, 1, 10),
    _MscRtgTopNodeLgTrkObjIndex_Type()
)
mscRtgTopNodeLgTrkObjIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgTopNodeLgTrkObjIndex.setStatus("mandatory")
_MscRtgTopNodeLgTrkObjOperTable_Object = MibTable
mscRtgTopNodeLgTrkObjOperTable = _MscRtgTopNodeLgTrkObjOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscRtgTopNodeLgTrkObjOperTable.setStatus("mandatory")
_MscRtgTopNodeLgTrkObjOperEntry_Object = MibTableRow
mscRtgTopNodeLgTrkObjOperEntry = _MscRtgTopNodeLgTrkObjOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 2, 10, 1)
)
mscRtgTopNodeLgTrkObjOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopNodeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopNodeLgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopNodeLgTrkObjIndex"),
)
if mibBuilder.loadTexts:
    mscRtgTopNodeLgTrkObjOperEntry.setStatus("mandatory")


class _MscRtgTopNodeLgTrkObjMaxReservableBwOut_Type(Gauge32):
    """Custom type mscRtgTopNodeLgTrkObjMaxReservableBwOut based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscRtgTopNodeLgTrkObjMaxReservableBwOut_Type.__name__ = "Gauge32"
_MscRtgTopNodeLgTrkObjMaxReservableBwOut_Object = MibTableColumn
mscRtgTopNodeLgTrkObjMaxReservableBwOut = _MscRtgTopNodeLgTrkObjMaxReservableBwOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 2, 10, 1, 1),
    _MscRtgTopNodeLgTrkObjMaxReservableBwOut_Type()
)
mscRtgTopNodeLgTrkObjMaxReservableBwOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopNodeLgTrkObjMaxReservableBwOut.setStatus("mandatory")


class _MscRtgTopNodeLgTrkObjTrunkCost_Type(Unsigned32):
    """Custom type mscRtgTopNodeLgTrkObjTrunkCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscRtgTopNodeLgTrkObjTrunkCost_Type.__name__ = "Unsigned32"
_MscRtgTopNodeLgTrkObjTrunkCost_Object = MibTableColumn
mscRtgTopNodeLgTrkObjTrunkCost = _MscRtgTopNodeLgTrkObjTrunkCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 2, 10, 1, 2),
    _MscRtgTopNodeLgTrkObjTrunkCost_Type()
)
mscRtgTopNodeLgTrkObjTrunkCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopNodeLgTrkObjTrunkCost.setStatus("mandatory")


class _MscRtgTopNodeLgTrkObjTrunkDelay_Type(Unsigned32):
    """Custom type mscRtgTopNodeLgTrkObjTrunkDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscRtgTopNodeLgTrkObjTrunkDelay_Type.__name__ = "Unsigned32"
_MscRtgTopNodeLgTrkObjTrunkDelay_Object = MibTableColumn
mscRtgTopNodeLgTrkObjTrunkDelay = _MscRtgTopNodeLgTrkObjTrunkDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 2, 10, 1, 3),
    _MscRtgTopNodeLgTrkObjTrunkDelay_Type()
)
mscRtgTopNodeLgTrkObjTrunkDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopNodeLgTrkObjTrunkDelay.setStatus("mandatory")


class _MscRtgTopNodeLgTrkObjTrunkSecurity_Type(Unsigned32):
    """Custom type mscRtgTopNodeLgTrkObjTrunkSecurity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscRtgTopNodeLgTrkObjTrunkSecurity_Type.__name__ = "Unsigned32"
_MscRtgTopNodeLgTrkObjTrunkSecurity_Object = MibTableColumn
mscRtgTopNodeLgTrkObjTrunkSecurity = _MscRtgTopNodeLgTrkObjTrunkSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 2, 10, 1, 4),
    _MscRtgTopNodeLgTrkObjTrunkSecurity_Type()
)
mscRtgTopNodeLgTrkObjTrunkSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopNodeLgTrkObjTrunkSecurity.setStatus("mandatory")


class _MscRtgTopNodeLgTrkObjSupportedTrafficTypes_Type(OctetString):
    """Custom type mscRtgTopNodeLgTrkObjSupportedTrafficTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscRtgTopNodeLgTrkObjSupportedTrafficTypes_Type.__name__ = "OctetString"
_MscRtgTopNodeLgTrkObjSupportedTrafficTypes_Object = MibTableColumn
mscRtgTopNodeLgTrkObjSupportedTrafficTypes = _MscRtgTopNodeLgTrkObjSupportedTrafficTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 2, 10, 1, 5),
    _MscRtgTopNodeLgTrkObjSupportedTrafficTypes_Type()
)
mscRtgTopNodeLgTrkObjSupportedTrafficTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopNodeLgTrkObjSupportedTrafficTypes.setStatus("mandatory")


class _MscRtgTopNodeLgTrkObjTrunkType_Type(Integer32):
    """Custom type mscRtgTopNodeLgTrkObjTrunkType based on Integer32"""
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


_MscRtgTopNodeLgTrkObjTrunkType_Type.__name__ = "Integer32"
_MscRtgTopNodeLgTrkObjTrunkType_Object = MibTableColumn
mscRtgTopNodeLgTrkObjTrunkType = _MscRtgTopNodeLgTrkObjTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 2, 10, 1, 6),
    _MscRtgTopNodeLgTrkObjTrunkType_Type()
)
mscRtgTopNodeLgTrkObjTrunkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopNodeLgTrkObjTrunkType.setStatus("mandatory")


class _MscRtgTopNodeLgTrkObjCustomerParameter_Type(Unsigned32):
    """Custom type mscRtgTopNodeLgTrkObjCustomerParameter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscRtgTopNodeLgTrkObjCustomerParameter_Type.__name__ = "Unsigned32"
_MscRtgTopNodeLgTrkObjCustomerParameter_Object = MibTableColumn
mscRtgTopNodeLgTrkObjCustomerParameter = _MscRtgTopNodeLgTrkObjCustomerParameter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 2, 10, 1, 7),
    _MscRtgTopNodeLgTrkObjCustomerParameter_Type()
)
mscRtgTopNodeLgTrkObjCustomerParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopNodeLgTrkObjCustomerParameter.setStatus("mandatory")


class _MscRtgTopNodeLgTrkObjFarEndTrmLkInstance_Type(Unsigned32):
    """Custom type mscRtgTopNodeLgTrkObjFarEndTrmLkInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_MscRtgTopNodeLgTrkObjFarEndTrmLkInstance_Type.__name__ = "Unsigned32"
_MscRtgTopNodeLgTrkObjFarEndTrmLkInstance_Object = MibTableColumn
mscRtgTopNodeLgTrkObjFarEndTrmLkInstance = _MscRtgTopNodeLgTrkObjFarEndTrmLkInstance_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 2, 10, 1, 8),
    _MscRtgTopNodeLgTrkObjFarEndTrmLkInstance_Type()
)
mscRtgTopNodeLgTrkObjFarEndTrmLkInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopNodeLgTrkObjFarEndTrmLkInstance.setStatus("mandatory")
_MscRtgTopNodeLgTrkObjUnresTable_Object = MibTable
mscRtgTopNodeLgTrkObjUnresTable = _MscRtgTopNodeLgTrkObjUnresTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 2, 234)
)
if mibBuilder.loadTexts:
    mscRtgTopNodeLgTrkObjUnresTable.setStatus("mandatory")
_MscRtgTopNodeLgTrkObjUnresEntry_Object = MibTableRow
mscRtgTopNodeLgTrkObjUnresEntry = _MscRtgTopNodeLgTrkObjUnresEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 2, 234, 1)
)
mscRtgTopNodeLgTrkObjUnresEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopNodeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopNodeLgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopNodeLgTrkObjIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopNodeLgTrkObjUnresSetupPriorityIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopNodeLgTrkObjUnresUnreservedBwPartsIndex"),
)
if mibBuilder.loadTexts:
    mscRtgTopNodeLgTrkObjUnresEntry.setStatus("mandatory")


class _MscRtgTopNodeLgTrkObjUnresSetupPriorityIndex_Type(Integer32):
    """Custom type mscRtgTopNodeLgTrkObjUnresSetupPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("bwPartOver255", 0)
    )


_MscRtgTopNodeLgTrkObjUnresSetupPriorityIndex_Type.__name__ = "Integer32"
_MscRtgTopNodeLgTrkObjUnresSetupPriorityIndex_Object = MibTableColumn
mscRtgTopNodeLgTrkObjUnresSetupPriorityIndex = _MscRtgTopNodeLgTrkObjUnresSetupPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 2, 234, 1, 1),
    _MscRtgTopNodeLgTrkObjUnresSetupPriorityIndex_Type()
)
mscRtgTopNodeLgTrkObjUnresSetupPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgTopNodeLgTrkObjUnresSetupPriorityIndex.setStatus("mandatory")


class _MscRtgTopNodeLgTrkObjUnresUnreservedBwPartsIndex_Type(Integer32):
    """Custom type mscRtgTopNodeLgTrkObjUnresUnreservedBwPartsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscRtgTopNodeLgTrkObjUnresUnreservedBwPartsIndex_Type.__name__ = "Integer32"
_MscRtgTopNodeLgTrkObjUnresUnreservedBwPartsIndex_Object = MibTableColumn
mscRtgTopNodeLgTrkObjUnresUnreservedBwPartsIndex = _MscRtgTopNodeLgTrkObjUnresUnreservedBwPartsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 2, 234, 1, 2),
    _MscRtgTopNodeLgTrkObjUnresUnreservedBwPartsIndex_Type()
)
mscRtgTopNodeLgTrkObjUnresUnreservedBwPartsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscRtgTopNodeLgTrkObjUnresUnreservedBwPartsIndex.setStatus("mandatory")


class _MscRtgTopNodeLgTrkObjUnresValue_Type(Unsigned32):
    """Custom type mscRtgTopNodeLgTrkObjUnresValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscRtgTopNodeLgTrkObjUnresValue_Type.__name__ = "Unsigned32"
_MscRtgTopNodeLgTrkObjUnresValue_Object = MibTableColumn
mscRtgTopNodeLgTrkObjUnresValue = _MscRtgTopNodeLgTrkObjUnresValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 2, 234, 1, 3),
    _MscRtgTopNodeLgTrkObjUnresValue_Type()
)
mscRtgTopNodeLgTrkObjUnresValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopNodeLgTrkObjUnresValue.setStatus("mandatory")
_MscRtgTopNodeLgOperTable_Object = MibTable
mscRtgTopNodeLgOperTable = _MscRtgTopNodeLgOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscRtgTopNodeLgOperTable.setStatus("mandatory")
_MscRtgTopNodeLgOperEntry_Object = MibTableRow
mscRtgTopNodeLgOperEntry = _MscRtgTopNodeLgOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 10, 1)
)
mscRtgTopNodeLgOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopNodeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopNodeLgIndex"),
)
if mibBuilder.loadTexts:
    mscRtgTopNodeLgOperEntry.setStatus("mandatory")


class _MscRtgTopNodeLgDelayMetric_Type(Unsigned32):
    """Custom type mscRtgTopNodeLgDelayMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MscRtgTopNodeLgDelayMetric_Type.__name__ = "Unsigned32"
_MscRtgTopNodeLgDelayMetric_Object = MibTableColumn
mscRtgTopNodeLgDelayMetric = _MscRtgTopNodeLgDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 10, 1, 1),
    _MscRtgTopNodeLgDelayMetric_Type()
)
mscRtgTopNodeLgDelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopNodeLgDelayMetric.setStatus("mandatory")


class _MscRtgTopNodeLgTputMetric_Type(Unsigned32):
    """Custom type mscRtgTopNodeLgTputMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MscRtgTopNodeLgTputMetric_Type.__name__ = "Unsigned32"
_MscRtgTopNodeLgTputMetric_Object = MibTableColumn
mscRtgTopNodeLgTputMetric = _MscRtgTopNodeLgTputMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 10, 1, 2),
    _MscRtgTopNodeLgTputMetric_Type()
)
mscRtgTopNodeLgTputMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopNodeLgTputMetric.setStatus("mandatory")
_MscRtgTopNodeLgLnnTable_Object = MibTable
mscRtgTopNodeLgLnnTable = _MscRtgTopNodeLgLnnTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 235)
)
if mibBuilder.loadTexts:
    mscRtgTopNodeLgLnnTable.setStatus("mandatory")
_MscRtgTopNodeLgLnnEntry_Object = MibTableRow
mscRtgTopNodeLgLnnEntry = _MscRtgTopNodeLgLnnEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 235, 1)
)
mscRtgTopNodeLgLnnEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopNodeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopNodeLgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopNodeLgLnnValue"),
)
if mibBuilder.loadTexts:
    mscRtgTopNodeLgLnnEntry.setStatus("mandatory")


class _MscRtgTopNodeLgLnnValue_Type(Integer32):
    """Custom type mscRtgTopNodeLgLnnValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_MscRtgTopNodeLgLnnValue_Type.__name__ = "Integer32"
_MscRtgTopNodeLgLnnValue_Object = MibTableColumn
mscRtgTopNodeLgLnnValue = _MscRtgTopNodeLgLnnValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 2, 235, 1, 1),
    _MscRtgTopNodeLgLnnValue_Type()
)
mscRtgTopNodeLgLnnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopNodeLgLnnValue.setStatus("mandatory")
_MscRtgTopNodeOperTable_Object = MibTable
mscRtgTopNodeOperTable = _MscRtgTopNodeOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 10)
)
if mibBuilder.loadTexts:
    mscRtgTopNodeOperTable.setStatus("mandatory")
_MscRtgTopNodeOperEntry_Object = MibTableRow
mscRtgTopNodeOperEntry = _MscRtgTopNodeOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 10, 1)
)
mscRtgTopNodeOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopNodeIndex"),
)
if mibBuilder.loadTexts:
    mscRtgTopNodeOperEntry.setStatus("mandatory")


class _MscRtgTopNodeNodeId_Type(Unsigned32):
    """Custom type mscRtgTopNodeNodeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_MscRtgTopNodeNodeId_Type.__name__ = "Unsigned32"
_MscRtgTopNodeNodeId_Object = MibTableColumn
mscRtgTopNodeNodeId = _MscRtgTopNodeNodeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 2, 10, 1, 1),
    _MscRtgTopNodeNodeId_Type()
)
mscRtgTopNodeNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopNodeNodeId.setStatus("mandatory")
_MscRtgTopStatsTable_Object = MibTable
mscRtgTopStatsTable = _MscRtgTopStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 11)
)
if mibBuilder.loadTexts:
    mscRtgTopStatsTable.setStatus("mandatory")
_MscRtgTopStatsEntry_Object = MibTableRow
mscRtgTopStatsEntry = _MscRtgTopStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 11, 1)
)
mscRtgTopStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgTopIndex"),
)
if mibBuilder.loadTexts:
    mscRtgTopStatsEntry.setStatus("mandatory")
_MscRtgTopControlPktRx_Type = Counter32
_MscRtgTopControlPktRx_Object = MibTableColumn
mscRtgTopControlPktRx = _MscRtgTopControlPktRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 11, 1, 1),
    _MscRtgTopControlPktRx_Type()
)
mscRtgTopControlPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopControlPktRx.setStatus("mandatory")
_MscRtgTopControlBytesRx_Type = Counter32
_MscRtgTopControlBytesRx_Object = MibTableColumn
mscRtgTopControlBytesRx = _MscRtgTopControlBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 11, 1, 2),
    _MscRtgTopControlBytesRx_Type()
)
mscRtgTopControlBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopControlBytesRx.setStatus("mandatory")
_MscRtgTopControlPktTx_Type = Counter32
_MscRtgTopControlPktTx_Object = MibTableColumn
mscRtgTopControlPktTx = _MscRtgTopControlPktTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 11, 1, 3),
    _MscRtgTopControlPktTx_Type()
)
mscRtgTopControlPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopControlPktTx.setStatus("mandatory")
_MscRtgTopControlBytesTx_Type = Counter32
_MscRtgTopControlBytesTx_Object = MibTableColumn
mscRtgTopControlBytesTx = _MscRtgTopControlBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 5, 11, 1, 4),
    _MscRtgTopControlBytesTx_Type()
)
mscRtgTopControlBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscRtgTopControlBytesTx.setStatus("mandatory")
_MscRtgProvTable_Object = MibTable
mscRtgProvTable = _MscRtgProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 12)
)
if mibBuilder.loadTexts:
    mscRtgProvTable.setStatus("mandatory")
_MscRtgProvEntry_Object = MibTableRow
mscRtgProvEntry = _MscRtgProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 12, 1)
)
mscRtgProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
)
if mibBuilder.loadTexts:
    mscRtgProvEntry.setStatus("mandatory")


class _MscRtgTandemTraffic_Type(Integer32):
    """Custom type mscRtgTandemTraffic based on Integer32"""
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


_MscRtgTandemTraffic_Type.__name__ = "Integer32"
_MscRtgTandemTraffic_Object = MibTableColumn
mscRtgTandemTraffic = _MscRtgTandemTraffic_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 12, 1, 1),
    _MscRtgTandemTraffic_Type()
)
mscRtgTandemTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgTandemTraffic.setStatus("mandatory")
_MscRtgSplittingRegionIdsTable_Object = MibTable
mscRtgSplittingRegionIdsTable = _MscRtgSplittingRegionIdsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 407)
)
if mibBuilder.loadTexts:
    mscRtgSplittingRegionIdsTable.setStatus("mandatory")
_MscRtgSplittingRegionIdsEntry_Object = MibTableRow
mscRtgSplittingRegionIdsEntry = _MscRtgSplittingRegionIdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 407, 1)
)
mscRtgSplittingRegionIdsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgSplittingRegionIdsValue"),
)
if mibBuilder.loadTexts:
    mscRtgSplittingRegionIdsEntry.setStatus("mandatory")


class _MscRtgSplittingRegionIdsValue_Type(Integer32):
    """Custom type mscRtgSplittingRegionIdsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 126),
    )


_MscRtgSplittingRegionIdsValue_Type.__name__ = "Integer32"
_MscRtgSplittingRegionIdsValue_Object = MibTableColumn
mscRtgSplittingRegionIdsValue = _MscRtgSplittingRegionIdsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 407, 1, 1),
    _MscRtgSplittingRegionIdsValue_Type()
)
mscRtgSplittingRegionIdsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscRtgSplittingRegionIdsValue.setStatus("mandatory")
_MscRtgSplittingRegionIdsRowStatus_Type = RowStatus
_MscRtgSplittingRegionIdsRowStatus_Object = MibTableColumn
mscRtgSplittingRegionIdsRowStatus = _MscRtgSplittingRegionIdsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 407, 1, 2),
    _MscRtgSplittingRegionIdsRowStatus_Type()
)
mscRtgSplittingRegionIdsRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscRtgSplittingRegionIdsRowStatus.setStatus("mandatory")
_MscTrm_ObjectIdentity = ObjectIdentity
mscTrm = _MscTrm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41)
)
_MscTrmRowStatusTable_Object = MibTable
mscTrmRowStatusTable = _MscTrmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 1)
)
if mibBuilder.loadTexts:
    mscTrmRowStatusTable.setStatus("mandatory")
_MscTrmRowStatusEntry_Object = MibTableRow
mscTrmRowStatusEntry = _MscTrmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 1, 1)
)
mscTrmRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmIndex"),
)
if mibBuilder.loadTexts:
    mscTrmRowStatusEntry.setStatus("mandatory")
_MscTrmRowStatus_Type = RowStatus
_MscTrmRowStatus_Object = MibTableColumn
mscTrmRowStatus = _MscTrmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 1, 1, 1),
    _MscTrmRowStatus_Type()
)
mscTrmRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmRowStatus.setStatus("mandatory")
_MscTrmComponentName_Type = DisplayString
_MscTrmComponentName_Object = MibTableColumn
mscTrmComponentName = _MscTrmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 1, 1, 2),
    _MscTrmComponentName_Type()
)
mscTrmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmComponentName.setStatus("mandatory")
_MscTrmStorageType_Type = StorageType
_MscTrmStorageType_Object = MibTableColumn
mscTrmStorageType = _MscTrmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 1, 1, 4),
    _MscTrmStorageType_Type()
)
mscTrmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmStorageType.setStatus("mandatory")
_MscTrmIndex_Type = NonReplicated
_MscTrmIndex_Object = MibTableColumn
mscTrmIndex = _MscTrmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 1, 1, 10),
    _MscTrmIndex_Type()
)
mscTrmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrmIndex.setStatus("mandatory")
_MscTrmLk_ObjectIdentity = ObjectIdentity
mscTrmLk = _MscTrmLk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 2)
)
_MscTrmLkRowStatusTable_Object = MibTable
mscTrmLkRowStatusTable = _MscTrmLkRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 2, 1)
)
if mibBuilder.loadTexts:
    mscTrmLkRowStatusTable.setStatus("mandatory")
_MscTrmLkRowStatusEntry_Object = MibTableRow
mscTrmLkRowStatusEntry = _MscTrmLkRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 2, 1, 1)
)
mscTrmLkRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmLkIndex"),
)
if mibBuilder.loadTexts:
    mscTrmLkRowStatusEntry.setStatus("mandatory")
_MscTrmLkRowStatus_Type = RowStatus
_MscTrmLkRowStatus_Object = MibTableColumn
mscTrmLkRowStatus = _MscTrmLkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 2, 1, 1, 1),
    _MscTrmLkRowStatus_Type()
)
mscTrmLkRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLkRowStatus.setStatus("mandatory")
_MscTrmLkComponentName_Type = DisplayString
_MscTrmLkComponentName_Object = MibTableColumn
mscTrmLkComponentName = _MscTrmLkComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 2, 1, 1, 2),
    _MscTrmLkComponentName_Type()
)
mscTrmLkComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLkComponentName.setStatus("mandatory")
_MscTrmLkStorageType_Type = StorageType
_MscTrmLkStorageType_Object = MibTableColumn
mscTrmLkStorageType = _MscTrmLkStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 2, 1, 1, 4),
    _MscTrmLkStorageType_Type()
)
mscTrmLkStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLkStorageType.setStatus("mandatory")


class _MscTrmLkIndex_Type(Integer32):
    """Custom type mscTrmLkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_MscTrmLkIndex_Type.__name__ = "Integer32"
_MscTrmLkIndex_Object = MibTableColumn
mscTrmLkIndex = _MscTrmLkIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 2, 1, 1, 10),
    _MscTrmLkIndex_Type()
)
mscTrmLkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrmLkIndex.setStatus("mandatory")
_MscTrmLkOperTable_Object = MibTable
mscTrmLkOperTable = _MscTrmLkOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 2, 10)
)
if mibBuilder.loadTexts:
    mscTrmLkOperTable.setStatus("mandatory")
_MscTrmLkOperEntry_Object = MibTableRow
mscTrmLkOperEntry = _MscTrmLkOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 2, 10, 1)
)
mscTrmLkOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmLkIndex"),
)
if mibBuilder.loadTexts:
    mscTrmLkOperEntry.setStatus("mandatory")


class _MscTrmLkStatus_Type(Integer32):
    """Custom type mscTrmLkStatus based on Integer32"""
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


_MscTrmLkStatus_Type.__name__ = "Integer32"
_MscTrmLkStatus_Object = MibTableColumn
mscTrmLkStatus = _MscTrmLkStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 2, 10, 1, 1),
    _MscTrmLkStatus_Type()
)
mscTrmLkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLkStatus.setStatus("mandatory")


class _MscTrmLkThroughput_Type(Gauge32):
    """Custom type mscTrmLkThroughput based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 640000000),
    )


_MscTrmLkThroughput_Type.__name__ = "Gauge32"
_MscTrmLkThroughput_Object = MibTableColumn
mscTrmLkThroughput = _MscTrmLkThroughput_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 2, 10, 1, 2),
    _MscTrmLkThroughput_Type()
)
mscTrmLkThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLkThroughput.setStatus("mandatory")


class _MscTrmLkDelay_Type(Gauge32):
    """Custom type mscTrmLkDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1500),
    )


_MscTrmLkDelay_Type.__name__ = "Gauge32"
_MscTrmLkDelay_Object = MibTableColumn
mscTrmLkDelay = _MscTrmLkDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 2, 10, 1, 3),
    _MscTrmLkDelay_Type()
)
mscTrmLkDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLkDelay.setStatus("obsolete")


class _MscTrmLkMaxTxUnit_Type(Unsigned32):
    """Custom type mscTrmLkMaxTxUnit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscTrmLkMaxTxUnit_Type.__name__ = "Unsigned32"
_MscTrmLkMaxTxUnit_Object = MibTableColumn
mscTrmLkMaxTxUnit = _MscTrmLkMaxTxUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 2, 10, 1, 4),
    _MscTrmLkMaxTxUnit_Type()
)
mscTrmLkMaxTxUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLkMaxTxUnit.setStatus("mandatory")
_MscTrmLkLinkComponentName_Type = RowPointer
_MscTrmLkLinkComponentName_Object = MibTableColumn
mscTrmLkLinkComponentName = _MscTrmLkLinkComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 2, 10, 1, 5),
    _MscTrmLkLinkComponentName_Type()
)
mscTrmLkLinkComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLkLinkComponentName.setStatus("mandatory")


class _MscTrmLkDelayUsec_Type(FixedPoint1):
    """Custom type mscTrmLkDelayUsec based on FixedPoint1"""
    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 15000),
    )


_MscTrmLkDelayUsec_Type.__name__ = "FixedPoint1"
_MscTrmLkDelayUsec_Object = MibTableColumn
mscTrmLkDelayUsec = _MscTrmLkDelayUsec_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 2, 10, 1, 6),
    _MscTrmLkDelayUsec_Type()
)
mscTrmLkDelayUsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLkDelayUsec.setStatus("mandatory")
_MscTrmLkFwdStatsTable_Object = MibTable
mscTrmLkFwdStatsTable = _MscTrmLkFwdStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 2, 11)
)
if mibBuilder.loadTexts:
    mscTrmLkFwdStatsTable.setStatus("mandatory")
_MscTrmLkFwdStatsEntry_Object = MibTableRow
mscTrmLkFwdStatsEntry = _MscTrmLkFwdStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 2, 11, 1)
)
mscTrmLkFwdStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmLkIndex"),
)
if mibBuilder.loadTexts:
    mscTrmLkFwdStatsEntry.setStatus("mandatory")
_MscTrmLkFciSet_Type = Counter32
_MscTrmLkFciSet_Object = MibTableColumn
mscTrmLkFciSet = _MscTrmLkFciSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 2, 11, 1, 1),
    _MscTrmLkFciSet_Type()
)
mscTrmLkFciSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLkFciSet.setStatus("mandatory")
_MscTrmLkOverflowAttempts_Type = Counter32
_MscTrmLkOverflowAttempts_Object = MibTableColumn
mscTrmLkOverflowAttempts = _MscTrmLkOverflowAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 2, 11, 1, 2),
    _MscTrmLkOverflowAttempts_Type()
)
mscTrmLkOverflowAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLkOverflowAttempts.setStatus("mandatory")
_MscTrmLkPathOverflowAttempts_Type = Counter32
_MscTrmLkPathOverflowAttempts_Object = MibTableColumn
mscTrmLkPathOverflowAttempts = _MscTrmLkPathOverflowAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 2, 11, 1, 3),
    _MscTrmLkPathOverflowAttempts_Type()
)
mscTrmLkPathOverflowAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLkPathOverflowAttempts.setStatus("mandatory")
_MscTrmLkDiscardCongestedTable_Object = MibTable
mscTrmLkDiscardCongestedTable = _MscTrmLkDiscardCongestedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 2, 280)
)
if mibBuilder.loadTexts:
    mscTrmLkDiscardCongestedTable.setStatus("mandatory")
_MscTrmLkDiscardCongestedEntry_Object = MibTableRow
mscTrmLkDiscardCongestedEntry = _MscTrmLkDiscardCongestedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 2, 280, 1)
)
mscTrmLkDiscardCongestedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmLkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmLkDiscardCongestedIndex"),
)
if mibBuilder.loadTexts:
    mscTrmLkDiscardCongestedEntry.setStatus("mandatory")


class _MscTrmLkDiscardCongestedIndex_Type(Integer32):
    """Custom type mscTrmLkDiscardCongestedIndex based on Integer32"""
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


_MscTrmLkDiscardCongestedIndex_Type.__name__ = "Integer32"
_MscTrmLkDiscardCongestedIndex_Object = MibTableColumn
mscTrmLkDiscardCongestedIndex = _MscTrmLkDiscardCongestedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 2, 280, 1, 1),
    _MscTrmLkDiscardCongestedIndex_Type()
)
mscTrmLkDiscardCongestedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrmLkDiscardCongestedIndex.setStatus("mandatory")
_MscTrmLkDiscardCongestedValue_Type = Counter32
_MscTrmLkDiscardCongestedValue_Object = MibTableColumn
mscTrmLkDiscardCongestedValue = _MscTrmLkDiscardCongestedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 2, 280, 1, 2),
    _MscTrmLkDiscardCongestedValue_Type()
)
mscTrmLkDiscardCongestedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLkDiscardCongestedValue.setStatus("mandatory")
_MscTrmLg_ObjectIdentity = ObjectIdentity
mscTrmLg = _MscTrmLg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3)
)
_MscTrmLgRowStatusTable_Object = MibTable
mscTrmLgRowStatusTable = _MscTrmLgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 1)
)
if mibBuilder.loadTexts:
    mscTrmLgRowStatusTable.setStatus("mandatory")
_MscTrmLgRowStatusEntry_Object = MibTableRow
mscTrmLgRowStatusEntry = _MscTrmLgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 1, 1)
)
mscTrmLgRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmLgIndex"),
)
if mibBuilder.loadTexts:
    mscTrmLgRowStatusEntry.setStatus("mandatory")
_MscTrmLgRowStatus_Type = RowStatus
_MscTrmLgRowStatus_Object = MibTableColumn
mscTrmLgRowStatus = _MscTrmLgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 1, 1, 1),
    _MscTrmLgRowStatus_Type()
)
mscTrmLgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLgRowStatus.setStatus("mandatory")
_MscTrmLgComponentName_Type = DisplayString
_MscTrmLgComponentName_Object = MibTableColumn
mscTrmLgComponentName = _MscTrmLgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 1, 1, 2),
    _MscTrmLgComponentName_Type()
)
mscTrmLgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLgComponentName.setStatus("mandatory")
_MscTrmLgStorageType_Type = StorageType
_MscTrmLgStorageType_Object = MibTableColumn
mscTrmLgStorageType = _MscTrmLgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 1, 1, 4),
    _MscTrmLgStorageType_Type()
)
mscTrmLgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLgStorageType.setStatus("mandatory")


class _MscTrmLgIndex_Type(AsciiStringIndex):
    """Custom type mscTrmLgIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_MscTrmLgIndex_Type.__name__ = "AsciiStringIndex"
_MscTrmLgIndex_Object = MibTableColumn
mscTrmLgIndex = _MscTrmLgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 1, 1, 10),
    _MscTrmLgIndex_Type()
)
mscTrmLgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrmLgIndex.setStatus("mandatory")
_MscTrmLgLk_ObjectIdentity = ObjectIdentity
mscTrmLgLk = _MscTrmLgLk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 2)
)
_MscTrmLgLkRowStatusTable_Object = MibTable
mscTrmLgLkRowStatusTable = _MscTrmLgLkRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscTrmLgLkRowStatusTable.setStatus("mandatory")
_MscTrmLgLkRowStatusEntry_Object = MibTableRow
mscTrmLgLkRowStatusEntry = _MscTrmLgLkRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 2, 1, 1)
)
mscTrmLgLkRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmLgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmLgLkIndex"),
)
if mibBuilder.loadTexts:
    mscTrmLgLkRowStatusEntry.setStatus("mandatory")
_MscTrmLgLkRowStatus_Type = RowStatus
_MscTrmLgLkRowStatus_Object = MibTableColumn
mscTrmLgLkRowStatus = _MscTrmLgLkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 2, 1, 1, 1),
    _MscTrmLgLkRowStatus_Type()
)
mscTrmLgLkRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLgLkRowStatus.setStatus("mandatory")
_MscTrmLgLkComponentName_Type = DisplayString
_MscTrmLgLkComponentName_Object = MibTableColumn
mscTrmLgLkComponentName = _MscTrmLgLkComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 2, 1, 1, 2),
    _MscTrmLgLkComponentName_Type()
)
mscTrmLgLkComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLgLkComponentName.setStatus("mandatory")
_MscTrmLgLkStorageType_Type = StorageType
_MscTrmLgLkStorageType_Object = MibTableColumn
mscTrmLgLkStorageType = _MscTrmLgLkStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 2, 1, 1, 4),
    _MscTrmLgLkStorageType_Type()
)
mscTrmLgLkStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLgLkStorageType.setStatus("mandatory")


class _MscTrmLgLkIndex_Type(Integer32):
    """Custom type mscTrmLgLkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_MscTrmLgLkIndex_Type.__name__ = "Integer32"
_MscTrmLgLkIndex_Object = MibTableColumn
mscTrmLgLkIndex = _MscTrmLgLkIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 2, 1, 1, 10),
    _MscTrmLgLkIndex_Type()
)
mscTrmLgLkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrmLgLkIndex.setStatus("mandatory")
_MscTrmLgLkOperTable_Object = MibTable
mscTrmLgLkOperTable = _MscTrmLgLkOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscTrmLgLkOperTable.setStatus("mandatory")
_MscTrmLgLkOperEntry_Object = MibTableRow
mscTrmLgLkOperEntry = _MscTrmLgLkOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 2, 10, 1)
)
mscTrmLgLkOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmLgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmLgLkIndex"),
)
if mibBuilder.loadTexts:
    mscTrmLgLkOperEntry.setStatus("mandatory")


class _MscTrmLgLkStatus_Type(Integer32):
    """Custom type mscTrmLgLkStatus based on Integer32"""
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


_MscTrmLgLkStatus_Type.__name__ = "Integer32"
_MscTrmLgLkStatus_Object = MibTableColumn
mscTrmLgLkStatus = _MscTrmLgLkStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 2, 10, 1, 1),
    _MscTrmLgLkStatus_Type()
)
mscTrmLgLkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLgLkStatus.setStatus("mandatory")


class _MscTrmLgLkThroughput_Type(Gauge32):
    """Custom type mscTrmLgLkThroughput based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 640000000),
    )


_MscTrmLgLkThroughput_Type.__name__ = "Gauge32"
_MscTrmLgLkThroughput_Object = MibTableColumn
mscTrmLgLkThroughput = _MscTrmLgLkThroughput_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 2, 10, 1, 2),
    _MscTrmLgLkThroughput_Type()
)
mscTrmLgLkThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLgLkThroughput.setStatus("mandatory")


class _MscTrmLgLkDelay_Type(Gauge32):
    """Custom type mscTrmLgLkDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1500),
    )


_MscTrmLgLkDelay_Type.__name__ = "Gauge32"
_MscTrmLgLkDelay_Object = MibTableColumn
mscTrmLgLkDelay = _MscTrmLgLkDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 2, 10, 1, 3),
    _MscTrmLgLkDelay_Type()
)
mscTrmLgLkDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLgLkDelay.setStatus("obsolete")


class _MscTrmLgLkMaxTxUnit_Type(Unsigned32):
    """Custom type mscTrmLgLkMaxTxUnit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscTrmLgLkMaxTxUnit_Type.__name__ = "Unsigned32"
_MscTrmLgLkMaxTxUnit_Object = MibTableColumn
mscTrmLgLkMaxTxUnit = _MscTrmLgLkMaxTxUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 2, 10, 1, 4),
    _MscTrmLgLkMaxTxUnit_Type()
)
mscTrmLgLkMaxTxUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLgLkMaxTxUnit.setStatus("mandatory")
_MscTrmLgLkLinkComponentName_Type = RowPointer
_MscTrmLgLkLinkComponentName_Object = MibTableColumn
mscTrmLgLkLinkComponentName = _MscTrmLgLkLinkComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 2, 10, 1, 5),
    _MscTrmLgLkLinkComponentName_Type()
)
mscTrmLgLkLinkComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLgLkLinkComponentName.setStatus("mandatory")


class _MscTrmLgLkDelayUsec_Type(FixedPoint1):
    """Custom type mscTrmLgLkDelayUsec based on FixedPoint1"""
    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 15000),
    )


_MscTrmLgLkDelayUsec_Type.__name__ = "FixedPoint1"
_MscTrmLgLkDelayUsec_Object = MibTableColumn
mscTrmLgLkDelayUsec = _MscTrmLgLkDelayUsec_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 2, 10, 1, 6),
    _MscTrmLgLkDelayUsec_Type()
)
mscTrmLgLkDelayUsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLgLkDelayUsec.setStatus("mandatory")
_MscTrmLgLkFwdStatsTable_Object = MibTable
mscTrmLgLkFwdStatsTable = _MscTrmLgLkFwdStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 2, 11)
)
if mibBuilder.loadTexts:
    mscTrmLgLkFwdStatsTable.setStatus("mandatory")
_MscTrmLgLkFwdStatsEntry_Object = MibTableRow
mscTrmLgLkFwdStatsEntry = _MscTrmLgLkFwdStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 2, 11, 1)
)
mscTrmLgLkFwdStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmLgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmLgLkIndex"),
)
if mibBuilder.loadTexts:
    mscTrmLgLkFwdStatsEntry.setStatus("mandatory")
_MscTrmLgLkFciSet_Type = Counter32
_MscTrmLgLkFciSet_Object = MibTableColumn
mscTrmLgLkFciSet = _MscTrmLgLkFciSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 2, 11, 1, 1),
    _MscTrmLgLkFciSet_Type()
)
mscTrmLgLkFciSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLgLkFciSet.setStatus("mandatory")
_MscTrmLgLkOverflowAttempts_Type = Counter32
_MscTrmLgLkOverflowAttempts_Object = MibTableColumn
mscTrmLgLkOverflowAttempts = _MscTrmLgLkOverflowAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 2, 11, 1, 2),
    _MscTrmLgLkOverflowAttempts_Type()
)
mscTrmLgLkOverflowAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLgLkOverflowAttempts.setStatus("mandatory")
_MscTrmLgLkPathOverflowAttempts_Type = Counter32
_MscTrmLgLkPathOverflowAttempts_Object = MibTableColumn
mscTrmLgLkPathOverflowAttempts = _MscTrmLgLkPathOverflowAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 2, 11, 1, 3),
    _MscTrmLgLkPathOverflowAttempts_Type()
)
mscTrmLgLkPathOverflowAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLgLkPathOverflowAttempts.setStatus("mandatory")
_MscTrmLgLkDiscardCongestedTable_Object = MibTable
mscTrmLgLkDiscardCongestedTable = _MscTrmLgLkDiscardCongestedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 2, 280)
)
if mibBuilder.loadTexts:
    mscTrmLgLkDiscardCongestedTable.setStatus("mandatory")
_MscTrmLgLkDiscardCongestedEntry_Object = MibTableRow
mscTrmLgLkDiscardCongestedEntry = _MscTrmLgLkDiscardCongestedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 2, 280, 1)
)
mscTrmLgLkDiscardCongestedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmLgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmLgLkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmLgLkDiscardCongestedIndex"),
)
if mibBuilder.loadTexts:
    mscTrmLgLkDiscardCongestedEntry.setStatus("mandatory")


class _MscTrmLgLkDiscardCongestedIndex_Type(Integer32):
    """Custom type mscTrmLgLkDiscardCongestedIndex based on Integer32"""
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


_MscTrmLgLkDiscardCongestedIndex_Type.__name__ = "Integer32"
_MscTrmLgLkDiscardCongestedIndex_Object = MibTableColumn
mscTrmLgLkDiscardCongestedIndex = _MscTrmLgLkDiscardCongestedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 2, 280, 1, 1),
    _MscTrmLgLkDiscardCongestedIndex_Type()
)
mscTrmLgLkDiscardCongestedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrmLgLkDiscardCongestedIndex.setStatus("mandatory")
_MscTrmLgLkDiscardCongestedValue_Type = Counter32
_MscTrmLgLkDiscardCongestedValue_Object = MibTableColumn
mscTrmLgLkDiscardCongestedValue = _MscTrmLgLkDiscardCongestedValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 2, 280, 1, 2),
    _MscTrmLgLkDiscardCongestedValue_Type()
)
mscTrmLgLkDiscardCongestedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLgLkDiscardCongestedValue.setStatus("mandatory")
_MscTrmLgLNN_ObjectIdentity = ObjectIdentity
mscTrmLgLNN = _MscTrmLgLNN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 3)
)
_MscTrmLgLNNRowStatusTable_Object = MibTable
mscTrmLgLNNRowStatusTable = _MscTrmLgLNNRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 3, 1)
)
if mibBuilder.loadTexts:
    mscTrmLgLNNRowStatusTable.setStatus("mandatory")
_MscTrmLgLNNRowStatusEntry_Object = MibTableRow
mscTrmLgLNNRowStatusEntry = _MscTrmLgLNNRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 3, 1, 1)
)
mscTrmLgLNNRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmLgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmLgLNNIndex"),
)
if mibBuilder.loadTexts:
    mscTrmLgLNNRowStatusEntry.setStatus("mandatory")
_MscTrmLgLNNRowStatus_Type = RowStatus
_MscTrmLgLNNRowStatus_Object = MibTableColumn
mscTrmLgLNNRowStatus = _MscTrmLgLNNRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 3, 1, 1, 1),
    _MscTrmLgLNNRowStatus_Type()
)
mscTrmLgLNNRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLgLNNRowStatus.setStatus("mandatory")
_MscTrmLgLNNComponentName_Type = DisplayString
_MscTrmLgLNNComponentName_Object = MibTableColumn
mscTrmLgLNNComponentName = _MscTrmLgLNNComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 3, 1, 1, 2),
    _MscTrmLgLNNComponentName_Type()
)
mscTrmLgLNNComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLgLNNComponentName.setStatus("mandatory")
_MscTrmLgLNNStorageType_Type = StorageType
_MscTrmLgLNNStorageType_Object = MibTableColumn
mscTrmLgLNNStorageType = _MscTrmLgLNNStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 3, 1, 1, 4),
    _MscTrmLgLNNStorageType_Type()
)
mscTrmLgLNNStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLgLNNStorageType.setStatus("mandatory")


class _MscTrmLgLNNIndex_Type(Integer32):
    """Custom type mscTrmLgLNNIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_MscTrmLgLNNIndex_Type.__name__ = "Integer32"
_MscTrmLgLNNIndex_Object = MibTableColumn
mscTrmLgLNNIndex = _MscTrmLgLNNIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 3, 1, 1, 10),
    _MscTrmLgLNNIndex_Type()
)
mscTrmLgLNNIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrmLgLNNIndex.setStatus("mandatory")
_MscTrmLgLNNOperTable_Object = MibTable
mscTrmLgLNNOperTable = _MscTrmLgLNNOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 3, 10)
)
if mibBuilder.loadTexts:
    mscTrmLgLNNOperTable.setStatus("mandatory")
_MscTrmLgLNNOperEntry_Object = MibTableRow
mscTrmLgLNNOperEntry = _MscTrmLgLNNOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 3, 10, 1)
)
mscTrmLgLNNOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmLgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscTrmLgLNNIndex"),
)
if mibBuilder.loadTexts:
    mscTrmLgLNNOperEntry.setStatus("mandatory")


class _MscTrmLgLNNLinkType_Type(Integer32):
    """Custom type mscTrmLgLNNLinkType based on Integer32"""
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


_MscTrmLgLNNLinkType_Type.__name__ = "Integer32"
_MscTrmLgLNNLinkType_Object = MibTableColumn
mscTrmLgLNNLinkType = _MscTrmLgLNNLinkType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 3, 10, 1, 1),
    _MscTrmLgLNNLinkType_Type()
)
mscTrmLgLNNLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLgLNNLinkType.setStatus("mandatory")
_MscTrmLgLNNAddressPlanComponentName_Type = RowPointer
_MscTrmLgLNNAddressPlanComponentName_Object = MibTableColumn
mscTrmLgLNNAddressPlanComponentName = _MscTrmLgLNNAddressPlanComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 41, 3, 3, 10, 1, 2),
    _MscTrmLgLNNAddressPlanComponentName_Type()
)
mscTrmLgLNNAddressPlanComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrmLgLNNAddressPlanComponentName.setStatus("mandatory")
_MscNpi_ObjectIdentity = ObjectIdentity
mscNpi = _MscNpi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 43)
)
_MscNpiRowStatusTable_Object = MibTable
mscNpiRowStatusTable = _MscNpiRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 43, 1)
)
if mibBuilder.loadTexts:
    mscNpiRowStatusTable.setStatus("mandatory")
_MscNpiRowStatusEntry_Object = MibTableRow
mscNpiRowStatusEntry = _MscNpiRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 43, 1, 1)
)
mscNpiRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscNpiIndex"),
)
if mibBuilder.loadTexts:
    mscNpiRowStatusEntry.setStatus("mandatory")
_MscNpiRowStatus_Type = RowStatus
_MscNpiRowStatus_Object = MibTableColumn
mscNpiRowStatus = _MscNpiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 43, 1, 1, 1),
    _MscNpiRowStatus_Type()
)
mscNpiRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNpiRowStatus.setStatus("mandatory")
_MscNpiComponentName_Type = DisplayString
_MscNpiComponentName_Object = MibTableColumn
mscNpiComponentName = _MscNpiComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 43, 1, 1, 2),
    _MscNpiComponentName_Type()
)
mscNpiComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNpiComponentName.setStatus("mandatory")
_MscNpiStorageType_Type = StorageType
_MscNpiStorageType_Object = MibTableColumn
mscNpiStorageType = _MscNpiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 43, 1, 1, 4),
    _MscNpiStorageType_Type()
)
mscNpiStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNpiStorageType.setStatus("mandatory")


class _MscNpiIndex_Type(Integer32):
    """Custom type mscNpiIndex based on Integer32"""
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


_MscNpiIndex_Type.__name__ = "Integer32"
_MscNpiIndex_Object = MibTableColumn
mscNpiIndex = _MscNpiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 43, 1, 1, 10),
    _MscNpiIndex_Type()
)
mscNpiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscNpiIndex.setStatus("mandatory")
_MscNpiDna_ObjectIdentity = ObjectIdentity
mscNpiDna = _MscNpiDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 43, 2)
)
_MscNpiDnaRowStatusTable_Object = MibTable
mscNpiDnaRowStatusTable = _MscNpiDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 43, 2, 1)
)
if mibBuilder.loadTexts:
    mscNpiDnaRowStatusTable.setStatus("mandatory")
_MscNpiDnaRowStatusEntry_Object = MibTableRow
mscNpiDnaRowStatusEntry = _MscNpiDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 43, 2, 1, 1)
)
mscNpiDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscNpiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscNpiDnaIndex"),
)
if mibBuilder.loadTexts:
    mscNpiDnaRowStatusEntry.setStatus("mandatory")
_MscNpiDnaRowStatus_Type = RowStatus
_MscNpiDnaRowStatus_Object = MibTableColumn
mscNpiDnaRowStatus = _MscNpiDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 43, 2, 1, 1, 1),
    _MscNpiDnaRowStatus_Type()
)
mscNpiDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNpiDnaRowStatus.setStatus("mandatory")
_MscNpiDnaComponentName_Type = DisplayString
_MscNpiDnaComponentName_Object = MibTableColumn
mscNpiDnaComponentName = _MscNpiDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 43, 2, 1, 1, 2),
    _MscNpiDnaComponentName_Type()
)
mscNpiDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNpiDnaComponentName.setStatus("mandatory")
_MscNpiDnaStorageType_Type = StorageType
_MscNpiDnaStorageType_Object = MibTableColumn
mscNpiDnaStorageType = _MscNpiDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 43, 2, 1, 1, 4),
    _MscNpiDnaStorageType_Type()
)
mscNpiDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNpiDnaStorageType.setStatus("mandatory")


class _MscNpiDnaIndex_Type(DigitString):
    """Custom type mscNpiDnaIndex based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscNpiDnaIndex_Type.__name__ = "DigitString"
_MscNpiDnaIndex_Object = MibTableColumn
mscNpiDnaIndex = _MscNpiDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 43, 2, 1, 1, 10),
    _MscNpiDnaIndex_Type()
)
mscNpiDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscNpiDnaIndex.setStatus("mandatory")
_MscNpiDnaInfoTable_Object = MibTable
mscNpiDnaInfoTable = _MscNpiDnaInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 43, 2, 10)
)
if mibBuilder.loadTexts:
    mscNpiDnaInfoTable.setStatus("mandatory")
_MscNpiDnaInfoEntry_Object = MibTableRow
mscNpiDnaInfoEntry = _MscNpiDnaInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 43, 2, 10, 1)
)
mscNpiDnaInfoEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscNpiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscNpiDnaIndex"),
)
if mibBuilder.loadTexts:
    mscNpiDnaInfoEntry.setStatus("mandatory")
_MscNpiDnaDestinationName_Type = RowPointer
_MscNpiDnaDestinationName_Object = MibTableColumn
mscNpiDnaDestinationName = _MscNpiDnaDestinationName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 43, 2, 10, 1, 1),
    _MscNpiDnaDestinationName_Type()
)
mscNpiDnaDestinationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNpiDnaDestinationName.setStatus("mandatory")
_MscNpiStatsTable_Object = MibTable
mscNpiStatsTable = _MscNpiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 43, 10)
)
if mibBuilder.loadTexts:
    mscNpiStatsTable.setStatus("mandatory")
_MscNpiStatsEntry_Object = MibTableRow
mscNpiStatsEntry = _MscNpiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 43, 10, 1)
)
mscNpiStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscNpiIndex"),
)
if mibBuilder.loadTexts:
    mscNpiStatsEntry.setStatus("mandatory")


class _MscNpiTotalDnas_Type(Unsigned32):
    """Custom type mscNpiTotalDnas based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscNpiTotalDnas_Type.__name__ = "Unsigned32"
_MscNpiTotalDnas_Object = MibTableColumn
mscNpiTotalDnas = _MscNpiTotalDnas_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 43, 10, 1, 1),
    _MscNpiTotalDnas_Type()
)
mscNpiTotalDnas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNpiTotalDnas.setStatus("mandatory")
_BaseRoutingMIB_ObjectIdentity = ObjectIdentity
baseRoutingMIB = _BaseRoutingMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 18)
)
_BaseRoutingGroup_ObjectIdentity = ObjectIdentity
baseRoutingGroup = _BaseRoutingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 18, 1)
)
_BaseRoutingGroupCA_ObjectIdentity = ObjectIdentity
baseRoutingGroupCA = _BaseRoutingGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 18, 1, 1)
)
_BaseRoutingGroupCA02_ObjectIdentity = ObjectIdentity
baseRoutingGroupCA02 = _BaseRoutingGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 18, 1, 1, 3)
)
_BaseRoutingGroupCA02A_ObjectIdentity = ObjectIdentity
baseRoutingGroupCA02A = _BaseRoutingGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 18, 1, 1, 3, 2)
)
_BaseRoutingCapabilities_ObjectIdentity = ObjectIdentity
baseRoutingCapabilities = _BaseRoutingCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 18, 3)
)
_BaseRoutingCapabilitiesCA_ObjectIdentity = ObjectIdentity
baseRoutingCapabilitiesCA = _BaseRoutingCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 18, 3, 1)
)
_BaseRoutingCapabilitiesCA02_ObjectIdentity = ObjectIdentity
baseRoutingCapabilitiesCA02 = _BaseRoutingCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 18, 3, 1, 3)
)
_BaseRoutingCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
baseRoutingCapabilitiesCA02A = _BaseRoutingCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 18, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-BaseRoutingMIB",
    **{"mscRtg": mscRtg,
       "mscRtgRowStatusTable": mscRtgRowStatusTable,
       "mscRtgRowStatusEntry": mscRtgRowStatusEntry,
       "mscRtgRowStatus": mscRtgRowStatus,
       "mscRtgComponentName": mscRtgComponentName,
       "mscRtgStorageType": mscRtgStorageType,
       "mscRtgIndex": mscRtgIndex,
       "mscRtgTop": mscRtgTop,
       "mscRtgTopRowStatusTable": mscRtgTopRowStatusTable,
       "mscRtgTopRowStatusEntry": mscRtgTopRowStatusEntry,
       "mscRtgTopRowStatus": mscRtgTopRowStatus,
       "mscRtgTopComponentName": mscRtgTopComponentName,
       "mscRtgTopStorageType": mscRtgTopStorageType,
       "mscRtgTopIndex": mscRtgTopIndex,
       "mscRtgTopNode": mscRtgTopNode,
       "mscRtgTopNodeRowStatusTable": mscRtgTopNodeRowStatusTable,
       "mscRtgTopNodeRowStatusEntry": mscRtgTopNodeRowStatusEntry,
       "mscRtgTopNodeRowStatus": mscRtgTopNodeRowStatus,
       "mscRtgTopNodeComponentName": mscRtgTopNodeComponentName,
       "mscRtgTopNodeStorageType": mscRtgTopNodeStorageType,
       "mscRtgTopNodeIndex": mscRtgTopNodeIndex,
       "mscRtgTopNodeLg": mscRtgTopNodeLg,
       "mscRtgTopNodeLgRowStatusTable": mscRtgTopNodeLgRowStatusTable,
       "mscRtgTopNodeLgRowStatusEntry": mscRtgTopNodeLgRowStatusEntry,
       "mscRtgTopNodeLgRowStatus": mscRtgTopNodeLgRowStatus,
       "mscRtgTopNodeLgComponentName": mscRtgTopNodeLgComponentName,
       "mscRtgTopNodeLgStorageType": mscRtgTopNodeLgStorageType,
       "mscRtgTopNodeLgIndex": mscRtgTopNodeLgIndex,
       "mscRtgTopNodeLgTrkObj": mscRtgTopNodeLgTrkObj,
       "mscRtgTopNodeLgTrkObjRowStatusTable": mscRtgTopNodeLgTrkObjRowStatusTable,
       "mscRtgTopNodeLgTrkObjRowStatusEntry": mscRtgTopNodeLgTrkObjRowStatusEntry,
       "mscRtgTopNodeLgTrkObjRowStatus": mscRtgTopNodeLgTrkObjRowStatus,
       "mscRtgTopNodeLgTrkObjComponentName": mscRtgTopNodeLgTrkObjComponentName,
       "mscRtgTopNodeLgTrkObjStorageType": mscRtgTopNodeLgTrkObjStorageType,
       "mscRtgTopNodeLgTrkObjIndex": mscRtgTopNodeLgTrkObjIndex,
       "mscRtgTopNodeLgTrkObjOperTable": mscRtgTopNodeLgTrkObjOperTable,
       "mscRtgTopNodeLgTrkObjOperEntry": mscRtgTopNodeLgTrkObjOperEntry,
       "mscRtgTopNodeLgTrkObjMaxReservableBwOut": mscRtgTopNodeLgTrkObjMaxReservableBwOut,
       "mscRtgTopNodeLgTrkObjTrunkCost": mscRtgTopNodeLgTrkObjTrunkCost,
       "mscRtgTopNodeLgTrkObjTrunkDelay": mscRtgTopNodeLgTrkObjTrunkDelay,
       "mscRtgTopNodeLgTrkObjTrunkSecurity": mscRtgTopNodeLgTrkObjTrunkSecurity,
       "mscRtgTopNodeLgTrkObjSupportedTrafficTypes": mscRtgTopNodeLgTrkObjSupportedTrafficTypes,
       "mscRtgTopNodeLgTrkObjTrunkType": mscRtgTopNodeLgTrkObjTrunkType,
       "mscRtgTopNodeLgTrkObjCustomerParameter": mscRtgTopNodeLgTrkObjCustomerParameter,
       "mscRtgTopNodeLgTrkObjFarEndTrmLkInstance": mscRtgTopNodeLgTrkObjFarEndTrmLkInstance,
       "mscRtgTopNodeLgTrkObjUnresTable": mscRtgTopNodeLgTrkObjUnresTable,
       "mscRtgTopNodeLgTrkObjUnresEntry": mscRtgTopNodeLgTrkObjUnresEntry,
       "mscRtgTopNodeLgTrkObjUnresSetupPriorityIndex": mscRtgTopNodeLgTrkObjUnresSetupPriorityIndex,
       "mscRtgTopNodeLgTrkObjUnresUnreservedBwPartsIndex": mscRtgTopNodeLgTrkObjUnresUnreservedBwPartsIndex,
       "mscRtgTopNodeLgTrkObjUnresValue": mscRtgTopNodeLgTrkObjUnresValue,
       "mscRtgTopNodeLgOperTable": mscRtgTopNodeLgOperTable,
       "mscRtgTopNodeLgOperEntry": mscRtgTopNodeLgOperEntry,
       "mscRtgTopNodeLgDelayMetric": mscRtgTopNodeLgDelayMetric,
       "mscRtgTopNodeLgTputMetric": mscRtgTopNodeLgTputMetric,
       "mscRtgTopNodeLgLnnTable": mscRtgTopNodeLgLnnTable,
       "mscRtgTopNodeLgLnnEntry": mscRtgTopNodeLgLnnEntry,
       "mscRtgTopNodeLgLnnValue": mscRtgTopNodeLgLnnValue,
       "mscRtgTopNodeOperTable": mscRtgTopNodeOperTable,
       "mscRtgTopNodeOperEntry": mscRtgTopNodeOperEntry,
       "mscRtgTopNodeNodeId": mscRtgTopNodeNodeId,
       "mscRtgTopStatsTable": mscRtgTopStatsTable,
       "mscRtgTopStatsEntry": mscRtgTopStatsEntry,
       "mscRtgTopControlPktRx": mscRtgTopControlPktRx,
       "mscRtgTopControlBytesRx": mscRtgTopControlBytesRx,
       "mscRtgTopControlPktTx": mscRtgTopControlPktTx,
       "mscRtgTopControlBytesTx": mscRtgTopControlBytesTx,
       "mscRtgProvTable": mscRtgProvTable,
       "mscRtgProvEntry": mscRtgProvEntry,
       "mscRtgTandemTraffic": mscRtgTandemTraffic,
       "mscRtgSplittingRegionIdsTable": mscRtgSplittingRegionIdsTable,
       "mscRtgSplittingRegionIdsEntry": mscRtgSplittingRegionIdsEntry,
       "mscRtgSplittingRegionIdsValue": mscRtgSplittingRegionIdsValue,
       "mscRtgSplittingRegionIdsRowStatus": mscRtgSplittingRegionIdsRowStatus,
       "mscTrm": mscTrm,
       "mscTrmRowStatusTable": mscTrmRowStatusTable,
       "mscTrmRowStatusEntry": mscTrmRowStatusEntry,
       "mscTrmRowStatus": mscTrmRowStatus,
       "mscTrmComponentName": mscTrmComponentName,
       "mscTrmStorageType": mscTrmStorageType,
       "mscTrmIndex": mscTrmIndex,
       "mscTrmLk": mscTrmLk,
       "mscTrmLkRowStatusTable": mscTrmLkRowStatusTable,
       "mscTrmLkRowStatusEntry": mscTrmLkRowStatusEntry,
       "mscTrmLkRowStatus": mscTrmLkRowStatus,
       "mscTrmLkComponentName": mscTrmLkComponentName,
       "mscTrmLkStorageType": mscTrmLkStorageType,
       "mscTrmLkIndex": mscTrmLkIndex,
       "mscTrmLkOperTable": mscTrmLkOperTable,
       "mscTrmLkOperEntry": mscTrmLkOperEntry,
       "mscTrmLkStatus": mscTrmLkStatus,
       "mscTrmLkThroughput": mscTrmLkThroughput,
       "mscTrmLkDelay": mscTrmLkDelay,
       "mscTrmLkMaxTxUnit": mscTrmLkMaxTxUnit,
       "mscTrmLkLinkComponentName": mscTrmLkLinkComponentName,
       "mscTrmLkDelayUsec": mscTrmLkDelayUsec,
       "mscTrmLkFwdStatsTable": mscTrmLkFwdStatsTable,
       "mscTrmLkFwdStatsEntry": mscTrmLkFwdStatsEntry,
       "mscTrmLkFciSet": mscTrmLkFciSet,
       "mscTrmLkOverflowAttempts": mscTrmLkOverflowAttempts,
       "mscTrmLkPathOverflowAttempts": mscTrmLkPathOverflowAttempts,
       "mscTrmLkDiscardCongestedTable": mscTrmLkDiscardCongestedTable,
       "mscTrmLkDiscardCongestedEntry": mscTrmLkDiscardCongestedEntry,
       "mscTrmLkDiscardCongestedIndex": mscTrmLkDiscardCongestedIndex,
       "mscTrmLkDiscardCongestedValue": mscTrmLkDiscardCongestedValue,
       "mscTrmLg": mscTrmLg,
       "mscTrmLgRowStatusTable": mscTrmLgRowStatusTable,
       "mscTrmLgRowStatusEntry": mscTrmLgRowStatusEntry,
       "mscTrmLgRowStatus": mscTrmLgRowStatus,
       "mscTrmLgComponentName": mscTrmLgComponentName,
       "mscTrmLgStorageType": mscTrmLgStorageType,
       "mscTrmLgIndex": mscTrmLgIndex,
       "mscTrmLgLk": mscTrmLgLk,
       "mscTrmLgLkRowStatusTable": mscTrmLgLkRowStatusTable,
       "mscTrmLgLkRowStatusEntry": mscTrmLgLkRowStatusEntry,
       "mscTrmLgLkRowStatus": mscTrmLgLkRowStatus,
       "mscTrmLgLkComponentName": mscTrmLgLkComponentName,
       "mscTrmLgLkStorageType": mscTrmLgLkStorageType,
       "mscTrmLgLkIndex": mscTrmLgLkIndex,
       "mscTrmLgLkOperTable": mscTrmLgLkOperTable,
       "mscTrmLgLkOperEntry": mscTrmLgLkOperEntry,
       "mscTrmLgLkStatus": mscTrmLgLkStatus,
       "mscTrmLgLkThroughput": mscTrmLgLkThroughput,
       "mscTrmLgLkDelay": mscTrmLgLkDelay,
       "mscTrmLgLkMaxTxUnit": mscTrmLgLkMaxTxUnit,
       "mscTrmLgLkLinkComponentName": mscTrmLgLkLinkComponentName,
       "mscTrmLgLkDelayUsec": mscTrmLgLkDelayUsec,
       "mscTrmLgLkFwdStatsTable": mscTrmLgLkFwdStatsTable,
       "mscTrmLgLkFwdStatsEntry": mscTrmLgLkFwdStatsEntry,
       "mscTrmLgLkFciSet": mscTrmLgLkFciSet,
       "mscTrmLgLkOverflowAttempts": mscTrmLgLkOverflowAttempts,
       "mscTrmLgLkPathOverflowAttempts": mscTrmLgLkPathOverflowAttempts,
       "mscTrmLgLkDiscardCongestedTable": mscTrmLgLkDiscardCongestedTable,
       "mscTrmLgLkDiscardCongestedEntry": mscTrmLgLkDiscardCongestedEntry,
       "mscTrmLgLkDiscardCongestedIndex": mscTrmLgLkDiscardCongestedIndex,
       "mscTrmLgLkDiscardCongestedValue": mscTrmLgLkDiscardCongestedValue,
       "mscTrmLgLNN": mscTrmLgLNN,
       "mscTrmLgLNNRowStatusTable": mscTrmLgLNNRowStatusTable,
       "mscTrmLgLNNRowStatusEntry": mscTrmLgLNNRowStatusEntry,
       "mscTrmLgLNNRowStatus": mscTrmLgLNNRowStatus,
       "mscTrmLgLNNComponentName": mscTrmLgLNNComponentName,
       "mscTrmLgLNNStorageType": mscTrmLgLNNStorageType,
       "mscTrmLgLNNIndex": mscTrmLgLNNIndex,
       "mscTrmLgLNNOperTable": mscTrmLgLNNOperTable,
       "mscTrmLgLNNOperEntry": mscTrmLgLNNOperEntry,
       "mscTrmLgLNNLinkType": mscTrmLgLNNLinkType,
       "mscTrmLgLNNAddressPlanComponentName": mscTrmLgLNNAddressPlanComponentName,
       "mscNpi": mscNpi,
       "mscNpiRowStatusTable": mscNpiRowStatusTable,
       "mscNpiRowStatusEntry": mscNpiRowStatusEntry,
       "mscNpiRowStatus": mscNpiRowStatus,
       "mscNpiComponentName": mscNpiComponentName,
       "mscNpiStorageType": mscNpiStorageType,
       "mscNpiIndex": mscNpiIndex,
       "mscNpiDna": mscNpiDna,
       "mscNpiDnaRowStatusTable": mscNpiDnaRowStatusTable,
       "mscNpiDnaRowStatusEntry": mscNpiDnaRowStatusEntry,
       "mscNpiDnaRowStatus": mscNpiDnaRowStatus,
       "mscNpiDnaComponentName": mscNpiDnaComponentName,
       "mscNpiDnaStorageType": mscNpiDnaStorageType,
       "mscNpiDnaIndex": mscNpiDnaIndex,
       "mscNpiDnaInfoTable": mscNpiDnaInfoTable,
       "mscNpiDnaInfoEntry": mscNpiDnaInfoEntry,
       "mscNpiDnaDestinationName": mscNpiDnaDestinationName,
       "mscNpiStatsTable": mscNpiStatsTable,
       "mscNpiStatsEntry": mscNpiStatsEntry,
       "mscNpiTotalDnas": mscNpiTotalDnas,
       "baseRoutingMIB": baseRoutingMIB,
       "baseRoutingGroup": baseRoutingGroup,
       "baseRoutingGroupCA": baseRoutingGroupCA,
       "baseRoutingGroupCA02": baseRoutingGroupCA02,
       "baseRoutingGroupCA02A": baseRoutingGroupCA02A,
       "baseRoutingCapabilities": baseRoutingCapabilities,
       "baseRoutingCapabilitiesCA": baseRoutingCapabilitiesCA,
       "baseRoutingCapabilitiesCA02": baseRoutingCapabilitiesCA02,
       "baseRoutingCapabilitiesCA02A": baseRoutingCapabilitiesCA02A}
)
