# SNMP MIB module (Nortel-Magellan-Passport-IpCosMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-IpCosMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:57 2024
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

(vrIp,
 vrIpIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-IpMIB",
    "vrIp",
    "vrIpIndex")

(DisplayString,
 Integer32,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiStringIndex,
 Hex,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiStringIndex",
    "Hex",
    "Link",
    "NonReplicated")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "passportMIBs")

(vrIndex,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-VirtualRouterMIB",
    "vrIndex")

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

_VrIpPg_ObjectIdentity = ObjectIdentity
vrIpPg = _VrIpPg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20)
)
_VrIpPgRowStatusTable_Object = MibTable
vrIpPgRowStatusTable = _VrIpPgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 1)
)
if mibBuilder.loadTexts:
    vrIpPgRowStatusTable.setStatus("mandatory")
_VrIpPgRowStatusEntry_Object = MibTableRow
vrIpPgRowStatusEntry = _VrIpPgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 1, 1)
)
vrIpPgRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgIndex"),
)
if mibBuilder.loadTexts:
    vrIpPgRowStatusEntry.setStatus("mandatory")
_VrIpPgRowStatus_Type = RowStatus
_VrIpPgRowStatus_Object = MibTableColumn
vrIpPgRowStatus = _VrIpPgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 1, 1, 1),
    _VrIpPgRowStatus_Type()
)
vrIpPgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpPgRowStatus.setStatus("mandatory")
_VrIpPgComponentName_Type = DisplayString
_VrIpPgComponentName_Object = MibTableColumn
vrIpPgComponentName = _VrIpPgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 1, 1, 2),
    _VrIpPgComponentName_Type()
)
vrIpPgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpPgComponentName.setStatus("mandatory")
_VrIpPgStorageType_Type = StorageType
_VrIpPgStorageType_Object = MibTableColumn
vrIpPgStorageType = _VrIpPgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 1, 1, 4),
    _VrIpPgStorageType_Type()
)
vrIpPgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpPgStorageType.setStatus("mandatory")


class _VrIpPgIndex_Type(AsciiStringIndex):
    """Custom type vrIpPgIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_VrIpPgIndex_Type.__name__ = "AsciiStringIndex"
_VrIpPgIndex_Object = MibTableColumn
vrIpPgIndex = _VrIpPgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 1, 1, 10),
    _VrIpPgIndex_Type()
)
vrIpPgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpPgIndex.setStatus("mandatory")
_VrIpPgPolicy_ObjectIdentity = ObjectIdentity
vrIpPgPolicy = _VrIpPgPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2)
)
_VrIpPgPolicyRowStatusTable_Object = MibTable
vrIpPgPolicyRowStatusTable = _VrIpPgPolicyRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpPgPolicyRowStatusTable.setStatus("mandatory")
_VrIpPgPolicyRowStatusEntry_Object = MibTableRow
vrIpPgPolicyRowStatusEntry = _VrIpPgPolicyRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 1, 1)
)
vrIpPgPolicyRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgPolicyIndex"),
)
if mibBuilder.loadTexts:
    vrIpPgPolicyRowStatusEntry.setStatus("mandatory")
_VrIpPgPolicyRowStatus_Type = RowStatus
_VrIpPgPolicyRowStatus_Object = MibTableColumn
vrIpPgPolicyRowStatus = _VrIpPgPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 1, 1, 1),
    _VrIpPgPolicyRowStatus_Type()
)
vrIpPgPolicyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpPgPolicyRowStatus.setStatus("mandatory")
_VrIpPgPolicyComponentName_Type = DisplayString
_VrIpPgPolicyComponentName_Object = MibTableColumn
vrIpPgPolicyComponentName = _VrIpPgPolicyComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 1, 1, 2),
    _VrIpPgPolicyComponentName_Type()
)
vrIpPgPolicyComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpPgPolicyComponentName.setStatus("mandatory")
_VrIpPgPolicyStorageType_Type = StorageType
_VrIpPgPolicyStorageType_Object = MibTableColumn
vrIpPgPolicyStorageType = _VrIpPgPolicyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 1, 1, 4),
    _VrIpPgPolicyStorageType_Type()
)
vrIpPgPolicyStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpPgPolicyStorageType.setStatus("mandatory")


class _VrIpPgPolicyIndex_Type(AsciiStringIndex):
    """Custom type vrIpPgPolicyIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_VrIpPgPolicyIndex_Type.__name__ = "AsciiStringIndex"
_VrIpPgPolicyIndex_Object = MibTableColumn
vrIpPgPolicyIndex = _VrIpPgPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 1, 1, 10),
    _VrIpPgPolicyIndex_Type()
)
vrIpPgPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpPgPolicyIndex.setStatus("mandatory")
_VrIpPgPolicyTosMap_ObjectIdentity = ObjectIdentity
vrIpPgPolicyTosMap = _VrIpPgPolicyTosMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 2)
)
_VrIpPgPolicyTosMapRowStatusTable_Object = MibTable
vrIpPgPolicyTosMapRowStatusTable = _VrIpPgPolicyTosMapRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpPgPolicyTosMapRowStatusTable.setStatus("mandatory")
_VrIpPgPolicyTosMapRowStatusEntry_Object = MibTableRow
vrIpPgPolicyTosMapRowStatusEntry = _VrIpPgPolicyTosMapRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 2, 1, 1)
)
vrIpPgPolicyTosMapRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgPolicyIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgPolicyTosMapIndex"),
)
if mibBuilder.loadTexts:
    vrIpPgPolicyTosMapRowStatusEntry.setStatus("mandatory")
_VrIpPgPolicyTosMapRowStatus_Type = RowStatus
_VrIpPgPolicyTosMapRowStatus_Object = MibTableColumn
vrIpPgPolicyTosMapRowStatus = _VrIpPgPolicyTosMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 2, 1, 1, 1),
    _VrIpPgPolicyTosMapRowStatus_Type()
)
vrIpPgPolicyTosMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpPgPolicyTosMapRowStatus.setStatus("mandatory")
_VrIpPgPolicyTosMapComponentName_Type = DisplayString
_VrIpPgPolicyTosMapComponentName_Object = MibTableColumn
vrIpPgPolicyTosMapComponentName = _VrIpPgPolicyTosMapComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 2, 1, 1, 2),
    _VrIpPgPolicyTosMapComponentName_Type()
)
vrIpPgPolicyTosMapComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpPgPolicyTosMapComponentName.setStatus("mandatory")
_VrIpPgPolicyTosMapStorageType_Type = StorageType
_VrIpPgPolicyTosMapStorageType_Object = MibTableColumn
vrIpPgPolicyTosMapStorageType = _VrIpPgPolicyTosMapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 2, 1, 1, 4),
    _VrIpPgPolicyTosMapStorageType_Type()
)
vrIpPgPolicyTosMapStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpPgPolicyTosMapStorageType.setStatus("mandatory")
_VrIpPgPolicyTosMapIndex_Type = NonReplicated
_VrIpPgPolicyTosMapIndex_Object = MibTableColumn
vrIpPgPolicyTosMapIndex = _VrIpPgPolicyTosMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 2, 1, 1, 10),
    _VrIpPgPolicyTosMapIndex_Type()
)
vrIpPgPolicyTosMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpPgPolicyTosMapIndex.setStatus("mandatory")
_VrIpPgPolicyTosMapOperTable_Object = MibTable
vrIpPgPolicyTosMapOperTable = _VrIpPgPolicyTosMapOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 2, 11)
)
if mibBuilder.loadTexts:
    vrIpPgPolicyTosMapOperTable.setStatus("mandatory")
_VrIpPgPolicyTosMapOperEntry_Object = MibTableRow
vrIpPgPolicyTosMapOperEntry = _VrIpPgPolicyTosMapOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 2, 11, 1)
)
vrIpPgPolicyTosMapOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgPolicyIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgPolicyTosMapIndex"),
)
if mibBuilder.loadTexts:
    vrIpPgPolicyTosMapOperEntry.setStatus("mandatory")


class _VrIpPgPolicyTosMapCos_Type(Unsigned32):
    """Custom type vrIpPgPolicyTosMapCos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_VrIpPgPolicyTosMapCos_Type.__name__ = "Unsigned32"
_VrIpPgPolicyTosMapCos_Object = MibTableColumn
vrIpPgPolicyTosMapCos = _VrIpPgPolicyTosMapCos_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 2, 11, 1, 1),
    _VrIpPgPolicyTosMapCos_Type()
)
vrIpPgPolicyTosMapCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpPgPolicyTosMapCos.setStatus("mandatory")
_VrIpPgPolicyTosMapTosTable_Object = MibTable
vrIpPgPolicyTosMapTosTable = _VrIpPgPolicyTosMapTosTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 2, 434)
)
if mibBuilder.loadTexts:
    vrIpPgPolicyTosMapTosTable.setStatus("mandatory")
_VrIpPgPolicyTosMapTosEntry_Object = MibTableRow
vrIpPgPolicyTosMapTosEntry = _VrIpPgPolicyTosMapTosEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 2, 434, 1)
)
vrIpPgPolicyTosMapTosEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgPolicyIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgPolicyTosMapIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgPolicyTosMapTosValue"),
)
if mibBuilder.loadTexts:
    vrIpPgPolicyTosMapTosEntry.setStatus("mandatory")


class _VrIpPgPolicyTosMapTosValue_Type(Integer32):
    """Custom type vrIpPgPolicyTosMapTosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrIpPgPolicyTosMapTosValue_Type.__name__ = "Integer32"
_VrIpPgPolicyTosMapTosValue_Object = MibTableColumn
vrIpPgPolicyTosMapTosValue = _VrIpPgPolicyTosMapTosValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 2, 434, 1, 1),
    _VrIpPgPolicyTosMapTosValue_Type()
)
vrIpPgPolicyTosMapTosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpPgPolicyTosMapTosValue.setStatus("mandatory")
_VrIpPgPolicyTosMapTosRowStatus_Type = RowStatus
_VrIpPgPolicyTosMapTosRowStatus_Object = MibTableColumn
vrIpPgPolicyTosMapTosRowStatus = _VrIpPgPolicyTosMapTosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 2, 434, 1, 2),
    _VrIpPgPolicyTosMapTosRowStatus_Type()
)
vrIpPgPolicyTosMapTosRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vrIpPgPolicyTosMapTosRowStatus.setStatus("mandatory")
_VrIpPgPolicyIpAddrLayer4Flow_ObjectIdentity = ObjectIdentity
vrIpPgPolicyIpAddrLayer4Flow = _VrIpPgPolicyIpAddrLayer4Flow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 3)
)
_VrIpPgPolicyIpAddrLayer4FlowRowStatusTable_Object = MibTable
vrIpPgPolicyIpAddrLayer4FlowRowStatusTable = _VrIpPgPolicyIpAddrLayer4FlowRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 3, 1)
)
if mibBuilder.loadTexts:
    vrIpPgPolicyIpAddrLayer4FlowRowStatusTable.setStatus("mandatory")
_VrIpPgPolicyIpAddrLayer4FlowRowStatusEntry_Object = MibTableRow
vrIpPgPolicyIpAddrLayer4FlowRowStatusEntry = _VrIpPgPolicyIpAddrLayer4FlowRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 3, 1, 1)
)
vrIpPgPolicyIpAddrLayer4FlowRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgPolicyIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgPolicyIpAddrLayer4FlowIndex"),
)
if mibBuilder.loadTexts:
    vrIpPgPolicyIpAddrLayer4FlowRowStatusEntry.setStatus("mandatory")
_VrIpPgPolicyIpAddrLayer4FlowRowStatus_Type = RowStatus
_VrIpPgPolicyIpAddrLayer4FlowRowStatus_Object = MibTableColumn
vrIpPgPolicyIpAddrLayer4FlowRowStatus = _VrIpPgPolicyIpAddrLayer4FlowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 3, 1, 1, 1),
    _VrIpPgPolicyIpAddrLayer4FlowRowStatus_Type()
)
vrIpPgPolicyIpAddrLayer4FlowRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpPgPolicyIpAddrLayer4FlowRowStatus.setStatus("mandatory")
_VrIpPgPolicyIpAddrLayer4FlowComponentName_Type = DisplayString
_VrIpPgPolicyIpAddrLayer4FlowComponentName_Object = MibTableColumn
vrIpPgPolicyIpAddrLayer4FlowComponentName = _VrIpPgPolicyIpAddrLayer4FlowComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 3, 1, 1, 2),
    _VrIpPgPolicyIpAddrLayer4FlowComponentName_Type()
)
vrIpPgPolicyIpAddrLayer4FlowComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpPgPolicyIpAddrLayer4FlowComponentName.setStatus("mandatory")
_VrIpPgPolicyIpAddrLayer4FlowStorageType_Type = StorageType
_VrIpPgPolicyIpAddrLayer4FlowStorageType_Object = MibTableColumn
vrIpPgPolicyIpAddrLayer4FlowStorageType = _VrIpPgPolicyIpAddrLayer4FlowStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 3, 1, 1, 4),
    _VrIpPgPolicyIpAddrLayer4FlowStorageType_Type()
)
vrIpPgPolicyIpAddrLayer4FlowStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpPgPolicyIpAddrLayer4FlowStorageType.setStatus("mandatory")


class _VrIpPgPolicyIpAddrLayer4FlowIndex_Type(Integer32):
    """Custom type vrIpPgPolicyIpAddrLayer4FlowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_VrIpPgPolicyIpAddrLayer4FlowIndex_Type.__name__ = "Integer32"
_VrIpPgPolicyIpAddrLayer4FlowIndex_Object = MibTableColumn
vrIpPgPolicyIpAddrLayer4FlowIndex = _VrIpPgPolicyIpAddrLayer4FlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 3, 1, 1, 10),
    _VrIpPgPolicyIpAddrLayer4FlowIndex_Type()
)
vrIpPgPolicyIpAddrLayer4FlowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpPgPolicyIpAddrLayer4FlowIndex.setStatus("mandatory")
_VrIpPgPolicyIpAddrLayer4FlowProvTable_Object = MibTable
vrIpPgPolicyIpAddrLayer4FlowProvTable = _VrIpPgPolicyIpAddrLayer4FlowProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 3, 10)
)
if mibBuilder.loadTexts:
    vrIpPgPolicyIpAddrLayer4FlowProvTable.setStatus("mandatory")
_VrIpPgPolicyIpAddrLayer4FlowProvEntry_Object = MibTableRow
vrIpPgPolicyIpAddrLayer4FlowProvEntry = _VrIpPgPolicyIpAddrLayer4FlowProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 3, 10, 1)
)
vrIpPgPolicyIpAddrLayer4FlowProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgPolicyIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgPolicyIpAddrLayer4FlowIndex"),
)
if mibBuilder.loadTexts:
    vrIpPgPolicyIpAddrLayer4FlowProvEntry.setStatus("mandatory")


class _VrIpPgPolicyIpAddrLayer4FlowPrefix_Type(IpAddress):
    """Custom type vrIpPgPolicyIpAddrLayer4FlowPrefix based on IpAddress"""
    defaultHexValue = "00000000"


_VrIpPgPolicyIpAddrLayer4FlowPrefix_Object = MibTableColumn
vrIpPgPolicyIpAddrLayer4FlowPrefix = _VrIpPgPolicyIpAddrLayer4FlowPrefix_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 3, 10, 1, 1),
    _VrIpPgPolicyIpAddrLayer4FlowPrefix_Type()
)
vrIpPgPolicyIpAddrLayer4FlowPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpPgPolicyIpAddrLayer4FlowPrefix.setStatus("mandatory")


class _VrIpPgPolicyIpAddrLayer4FlowPrefixLength_Type(Unsigned32):
    """Custom type vrIpPgPolicyIpAddrLayer4FlowPrefixLength based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_VrIpPgPolicyIpAddrLayer4FlowPrefixLength_Type.__name__ = "Unsigned32"
_VrIpPgPolicyIpAddrLayer4FlowPrefixLength_Object = MibTableColumn
vrIpPgPolicyIpAddrLayer4FlowPrefixLength = _VrIpPgPolicyIpAddrLayer4FlowPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 3, 10, 1, 2),
    _VrIpPgPolicyIpAddrLayer4FlowPrefixLength_Type()
)
vrIpPgPolicyIpAddrLayer4FlowPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpPgPolicyIpAddrLayer4FlowPrefixLength.setStatus("mandatory")
_VrIpPgPolicyIpAddrLayer4FlowProtoProvisionedTable_Object = MibTable
vrIpPgPolicyIpAddrLayer4FlowProtoProvisionedTable = _VrIpPgPolicyIpAddrLayer4FlowProtoProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 3, 11)
)
if mibBuilder.loadTexts:
    vrIpPgPolicyIpAddrLayer4FlowProtoProvisionedTable.setStatus("mandatory")
_VrIpPgPolicyIpAddrLayer4FlowProtoProvisionedEntry_Object = MibTableRow
vrIpPgPolicyIpAddrLayer4FlowProtoProvisionedEntry = _VrIpPgPolicyIpAddrLayer4FlowProtoProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 3, 11, 1)
)
vrIpPgPolicyIpAddrLayer4FlowProtoProvisionedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgPolicyIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgPolicyIpAddrLayer4FlowIndex"),
)
if mibBuilder.loadTexts:
    vrIpPgPolicyIpAddrLayer4FlowProtoProvisionedEntry.setStatus("mandatory")


class _VrIpPgPolicyIpAddrLayer4FlowProtocol_Type(Integer32):
    """Custom type vrIpPgPolicyIpAddrLayer4FlowProtocol based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("tcp", 6),
          ("udp", 17))
    )


_VrIpPgPolicyIpAddrLayer4FlowProtocol_Type.__name__ = "Integer32"
_VrIpPgPolicyIpAddrLayer4FlowProtocol_Object = MibTableColumn
vrIpPgPolicyIpAddrLayer4FlowProtocol = _VrIpPgPolicyIpAddrLayer4FlowProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 3, 11, 1, 1),
    _VrIpPgPolicyIpAddrLayer4FlowProtocol_Type()
)
vrIpPgPolicyIpAddrLayer4FlowProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpPgPolicyIpAddrLayer4FlowProtocol.setStatus("mandatory")
_VrIpPgPolicyIpAddrLayer4FlowOperTable_Object = MibTable
vrIpPgPolicyIpAddrLayer4FlowOperTable = _VrIpPgPolicyIpAddrLayer4FlowOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 3, 12)
)
if mibBuilder.loadTexts:
    vrIpPgPolicyIpAddrLayer4FlowOperTable.setStatus("mandatory")
_VrIpPgPolicyIpAddrLayer4FlowOperEntry_Object = MibTableRow
vrIpPgPolicyIpAddrLayer4FlowOperEntry = _VrIpPgPolicyIpAddrLayer4FlowOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 3, 12, 1)
)
vrIpPgPolicyIpAddrLayer4FlowOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgPolicyIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgPolicyIpAddrLayer4FlowIndex"),
)
if mibBuilder.loadTexts:
    vrIpPgPolicyIpAddrLayer4FlowOperEntry.setStatus("mandatory")


class _VrIpPgPolicyIpAddrLayer4FlowCos_Type(Unsigned32):
    """Custom type vrIpPgPolicyIpAddrLayer4FlowCos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_VrIpPgPolicyIpAddrLayer4FlowCos_Type.__name__ = "Unsigned32"
_VrIpPgPolicyIpAddrLayer4FlowCos_Object = MibTableColumn
vrIpPgPolicyIpAddrLayer4FlowCos = _VrIpPgPolicyIpAddrLayer4FlowCos_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 3, 12, 1, 1),
    _VrIpPgPolicyIpAddrLayer4FlowCos_Type()
)
vrIpPgPolicyIpAddrLayer4FlowCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpPgPolicyIpAddrLayer4FlowCos.setStatus("mandatory")
_VrIpPgPolicyIpAddrLayer4FlowPortNumberRangeTable_Object = MibTable
vrIpPgPolicyIpAddrLayer4FlowPortNumberRangeTable = _VrIpPgPolicyIpAddrLayer4FlowPortNumberRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 3, 435)
)
if mibBuilder.loadTexts:
    vrIpPgPolicyIpAddrLayer4FlowPortNumberRangeTable.setStatus("mandatory")
_VrIpPgPolicyIpAddrLayer4FlowPortNumberRangeEntry_Object = MibTableRow
vrIpPgPolicyIpAddrLayer4FlowPortNumberRangeEntry = _VrIpPgPolicyIpAddrLayer4FlowPortNumberRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 3, 435, 1)
)
vrIpPgPolicyIpAddrLayer4FlowPortNumberRangeEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgPolicyIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgPolicyIpAddrLayer4FlowIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgPolicyIpAddrLayer4FlowPortNumberRangeValue"),
)
if mibBuilder.loadTexts:
    vrIpPgPolicyIpAddrLayer4FlowPortNumberRangeEntry.setStatus("mandatory")


class _VrIpPgPolicyIpAddrLayer4FlowPortNumberRangeValue_Type(Integer32):
    """Custom type vrIpPgPolicyIpAddrLayer4FlowPortNumberRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpPgPolicyIpAddrLayer4FlowPortNumberRangeValue_Type.__name__ = "Integer32"
_VrIpPgPolicyIpAddrLayer4FlowPortNumberRangeValue_Object = MibTableColumn
vrIpPgPolicyIpAddrLayer4FlowPortNumberRangeValue = _VrIpPgPolicyIpAddrLayer4FlowPortNumberRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 3, 435, 1, 1),
    _VrIpPgPolicyIpAddrLayer4FlowPortNumberRangeValue_Type()
)
vrIpPgPolicyIpAddrLayer4FlowPortNumberRangeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpPgPolicyIpAddrLayer4FlowPortNumberRangeValue.setStatus("mandatory")
_VrIpPgPolicyIpAddrLayer4FlowPortNumberRangeRowStatus_Type = RowStatus
_VrIpPgPolicyIpAddrLayer4FlowPortNumberRangeRowStatus_Object = MibTableColumn
vrIpPgPolicyIpAddrLayer4FlowPortNumberRangeRowStatus = _VrIpPgPolicyIpAddrLayer4FlowPortNumberRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 3, 435, 1, 2),
    _VrIpPgPolicyIpAddrLayer4FlowPortNumberRangeRowStatus_Type()
)
vrIpPgPolicyIpAddrLayer4FlowPortNumberRangeRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vrIpPgPolicyIpAddrLayer4FlowPortNumberRangeRowStatus.setStatus("mandatory")
_VrIpPgPolicyProvTable_Object = MibTable
vrIpPgPolicyProvTable = _VrIpPgPolicyProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpPgPolicyProvTable.setStatus("mandatory")
_VrIpPgPolicyProvEntry_Object = MibTableRow
vrIpPgPolicyProvEntry = _VrIpPgPolicyProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 10, 1)
)
vrIpPgPolicyProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgPolicyIndex"),
)
if mibBuilder.loadTexts:
    vrIpPgPolicyProvEntry.setStatus("mandatory")


class _VrIpPgPolicyCosTreatmentIndex_Type(Unsigned32):
    """Custom type vrIpPgPolicyCosTreatmentIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_VrIpPgPolicyCosTreatmentIndex_Type.__name__ = "Unsigned32"
_VrIpPgPolicyCosTreatmentIndex_Object = MibTableColumn
vrIpPgPolicyCosTreatmentIndex = _VrIpPgPolicyCosTreatmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 2, 10, 1, 1),
    _VrIpPgPolicyCosTreatmentIndex_Type()
)
vrIpPgPolicyCosTreatmentIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpPgPolicyCosTreatmentIndex.setStatus("mandatory")
_VrIpPgCosTreatment_ObjectIdentity = ObjectIdentity
vrIpPgCosTreatment = _VrIpPgCosTreatment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 3)
)
_VrIpPgCosTreatmentRowStatusTable_Object = MibTable
vrIpPgCosTreatmentRowStatusTable = _VrIpPgCosTreatmentRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 3, 1)
)
if mibBuilder.loadTexts:
    vrIpPgCosTreatmentRowStatusTable.setStatus("mandatory")
_VrIpPgCosTreatmentRowStatusEntry_Object = MibTableRow
vrIpPgCosTreatmentRowStatusEntry = _VrIpPgCosTreatmentRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 3, 1, 1)
)
vrIpPgCosTreatmentRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgCosTreatmentIndex"),
)
if mibBuilder.loadTexts:
    vrIpPgCosTreatmentRowStatusEntry.setStatus("mandatory")
_VrIpPgCosTreatmentRowStatus_Type = RowStatus
_VrIpPgCosTreatmentRowStatus_Object = MibTableColumn
vrIpPgCosTreatmentRowStatus = _VrIpPgCosTreatmentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 3, 1, 1, 1),
    _VrIpPgCosTreatmentRowStatus_Type()
)
vrIpPgCosTreatmentRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpPgCosTreatmentRowStatus.setStatus("mandatory")
_VrIpPgCosTreatmentComponentName_Type = DisplayString
_VrIpPgCosTreatmentComponentName_Object = MibTableColumn
vrIpPgCosTreatmentComponentName = _VrIpPgCosTreatmentComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 3, 1, 1, 2),
    _VrIpPgCosTreatmentComponentName_Type()
)
vrIpPgCosTreatmentComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpPgCosTreatmentComponentName.setStatus("mandatory")
_VrIpPgCosTreatmentStorageType_Type = StorageType
_VrIpPgCosTreatmentStorageType_Object = MibTableColumn
vrIpPgCosTreatmentStorageType = _VrIpPgCosTreatmentStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 3, 1, 1, 4),
    _VrIpPgCosTreatmentStorageType_Type()
)
vrIpPgCosTreatmentStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpPgCosTreatmentStorageType.setStatus("mandatory")


class _VrIpPgCosTreatmentIndex_Type(Integer32):
    """Custom type vrIpPgCosTreatmentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_VrIpPgCosTreatmentIndex_Type.__name__ = "Integer32"
_VrIpPgCosTreatmentIndex_Object = MibTableColumn
vrIpPgCosTreatmentIndex = _VrIpPgCosTreatmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 3, 1, 1, 10),
    _VrIpPgCosTreatmentIndex_Type()
)
vrIpPgCosTreatmentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpPgCosTreatmentIndex.setStatus("mandatory")
_VrIpPgCosTreatmentProvTable_Object = MibTable
vrIpPgCosTreatmentProvTable = _VrIpPgCosTreatmentProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 3, 10)
)
if mibBuilder.loadTexts:
    vrIpPgCosTreatmentProvTable.setStatus("mandatory")
_VrIpPgCosTreatmentProvEntry_Object = MibTableRow
vrIpPgCosTreatmentProvEntry = _VrIpPgCosTreatmentProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 3, 10, 1)
)
vrIpPgCosTreatmentProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgCosTreatmentIndex"),
)
if mibBuilder.loadTexts:
    vrIpPgCosTreatmentProvEntry.setStatus("mandatory")


class _VrIpPgCosTreatmentCos_Type(Unsigned32):
    """Custom type vrIpPgCosTreatmentCos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_VrIpPgCosTreatmentCos_Type.__name__ = "Unsigned32"
_VrIpPgCosTreatmentCos_Object = MibTableColumn
vrIpPgCosTreatmentCos = _VrIpPgCosTreatmentCos_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 3, 10, 1, 1),
    _VrIpPgCosTreatmentCos_Type()
)
vrIpPgCosTreatmentCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpPgCosTreatmentCos.setStatus("mandatory")


class _VrIpPgCosTreatmentSetTosByte_Type(Integer32):
    """Custom type vrIpPgCosTreatmentSetTosByte based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_VrIpPgCosTreatmentSetTosByte_Type.__name__ = "Integer32"
_VrIpPgCosTreatmentSetTosByte_Object = MibTableColumn
vrIpPgCosTreatmentSetTosByte = _VrIpPgCosTreatmentSetTosByte_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 3, 10, 1, 3),
    _VrIpPgCosTreatmentSetTosByte_Type()
)
vrIpPgCosTreatmentSetTosByte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpPgCosTreatmentSetTosByte.setStatus("mandatory")


class _VrIpPgCosTreatmentTos_Type(Hex):
    """Custom type vrIpPgCosTreatmentTos based on Hex"""
    defaultValue = 0

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrIpPgCosTreatmentTos_Type.__name__ = "Hex"
_VrIpPgCosTreatmentTos_Object = MibTableColumn
vrIpPgCosTreatmentTos = _VrIpPgCosTreatmentTos_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 3, 10, 1, 4),
    _VrIpPgCosTreatmentTos_Type()
)
vrIpPgCosTreatmentTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpPgCosTreatmentTos.setStatus("mandatory")


class _VrIpPgCosTreatmentTosMask_Type(Hex):
    """Custom type vrIpPgCosTreatmentTosMask based on Hex"""
    defaultValue = 252

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrIpPgCosTreatmentTosMask_Type.__name__ = "Hex"
_VrIpPgCosTreatmentTosMask_Object = MibTableColumn
vrIpPgCosTreatmentTosMask = _VrIpPgCosTreatmentTosMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 3, 10, 1, 5),
    _VrIpPgCosTreatmentTosMask_Type()
)
vrIpPgCosTreatmentTosMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpPgCosTreatmentTosMask.setStatus("mandatory")


class _VrIpPgCosTreatmentEmissionPriority_Type(Unsigned32):
    """Custom type vrIpPgCosTreatmentEmissionPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_VrIpPgCosTreatmentEmissionPriority_Type.__name__ = "Unsigned32"
_VrIpPgCosTreatmentEmissionPriority_Object = MibTableColumn
vrIpPgCosTreatmentEmissionPriority = _VrIpPgCosTreatmentEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 3, 10, 1, 6),
    _VrIpPgCosTreatmentEmissionPriority_Type()
)
vrIpPgCosTreatmentEmissionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpPgCosTreatmentEmissionPriority.setStatus("mandatory")


class _VrIpPgCosTreatmentDiscardPriority_Type(Unsigned32):
    """Custom type vrIpPgCosTreatmentDiscardPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 3),
    )


_VrIpPgCosTreatmentDiscardPriority_Type.__name__ = "Unsigned32"
_VrIpPgCosTreatmentDiscardPriority_Object = MibTableColumn
vrIpPgCosTreatmentDiscardPriority = _VrIpPgCosTreatmentDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 3, 10, 1, 7),
    _VrIpPgCosTreatmentDiscardPriority_Type()
)
vrIpPgCosTreatmentDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpPgCosTreatmentDiscardPriority.setStatus("mandatory")
_VrIpPgUsersTable_Object = MibTable
vrIpPgUsersTable = _VrIpPgUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 432)
)
if mibBuilder.loadTexts:
    vrIpPgUsersTable.setStatus("mandatory")
_VrIpPgUsersEntry_Object = MibTableRow
vrIpPgUsersEntry = _VrIpPgUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 432, 1)
)
vrIpPgUsersEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgIndex"),
    (0, "Nortel-Magellan-Passport-IpCosMIB", "vrIpPgUsersValue"),
)
if mibBuilder.loadTexts:
    vrIpPgUsersEntry.setStatus("mandatory")
_VrIpPgUsersValue_Type = Link
_VrIpPgUsersValue_Object = MibTableColumn
vrIpPgUsersValue = _VrIpPgUsersValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 432, 1, 1),
    _VrIpPgUsersValue_Type()
)
vrIpPgUsersValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpPgUsersValue.setStatus("mandatory")
_VrIpPgUsersRowStatus_Type = RowStatus
_VrIpPgUsersRowStatus_Object = MibTableColumn
vrIpPgUsersRowStatus = _VrIpPgUsersRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 20, 432, 1, 2),
    _VrIpPgUsersRowStatus_Type()
)
vrIpPgUsersRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vrIpPgUsersRowStatus.setStatus("mandatory")
_IpCosMIB_ObjectIdentity = ObjectIdentity
ipCosMIB = _IpCosMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 162)
)
_IpCosGroup_ObjectIdentity = ObjectIdentity
ipCosGroup = _IpCosGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 162, 1)
)
_IpCosGroupBG_ObjectIdentity = ObjectIdentity
ipCosGroupBG = _IpCosGroupBG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 162, 1, 7)
)
_IpCosGroupBG00_ObjectIdentity = ObjectIdentity
ipCosGroupBG00 = _IpCosGroupBG00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 162, 1, 7, 1)
)
_IpCosGroupBG00A_ObjectIdentity = ObjectIdentity
ipCosGroupBG00A = _IpCosGroupBG00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 162, 1, 7, 1, 2)
)
_IpCosCapabilities_ObjectIdentity = ObjectIdentity
ipCosCapabilities = _IpCosCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 162, 3)
)
_IpCosCapabilitiesBG_ObjectIdentity = ObjectIdentity
ipCosCapabilitiesBG = _IpCosCapabilitiesBG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 162, 3, 7)
)
_IpCosCapabilitiesBG00_ObjectIdentity = ObjectIdentity
ipCosCapabilitiesBG00 = _IpCosCapabilitiesBG00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 162, 3, 7, 1)
)
_IpCosCapabilitiesBG00A_ObjectIdentity = ObjectIdentity
ipCosCapabilitiesBG00A = _IpCosCapabilitiesBG00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 162, 3, 7, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-IpCosMIB",
    **{"vrIpPg": vrIpPg,
       "vrIpPgRowStatusTable": vrIpPgRowStatusTable,
       "vrIpPgRowStatusEntry": vrIpPgRowStatusEntry,
       "vrIpPgRowStatus": vrIpPgRowStatus,
       "vrIpPgComponentName": vrIpPgComponentName,
       "vrIpPgStorageType": vrIpPgStorageType,
       "vrIpPgIndex": vrIpPgIndex,
       "vrIpPgPolicy": vrIpPgPolicy,
       "vrIpPgPolicyRowStatusTable": vrIpPgPolicyRowStatusTable,
       "vrIpPgPolicyRowStatusEntry": vrIpPgPolicyRowStatusEntry,
       "vrIpPgPolicyRowStatus": vrIpPgPolicyRowStatus,
       "vrIpPgPolicyComponentName": vrIpPgPolicyComponentName,
       "vrIpPgPolicyStorageType": vrIpPgPolicyStorageType,
       "vrIpPgPolicyIndex": vrIpPgPolicyIndex,
       "vrIpPgPolicyTosMap": vrIpPgPolicyTosMap,
       "vrIpPgPolicyTosMapRowStatusTable": vrIpPgPolicyTosMapRowStatusTable,
       "vrIpPgPolicyTosMapRowStatusEntry": vrIpPgPolicyTosMapRowStatusEntry,
       "vrIpPgPolicyTosMapRowStatus": vrIpPgPolicyTosMapRowStatus,
       "vrIpPgPolicyTosMapComponentName": vrIpPgPolicyTosMapComponentName,
       "vrIpPgPolicyTosMapStorageType": vrIpPgPolicyTosMapStorageType,
       "vrIpPgPolicyTosMapIndex": vrIpPgPolicyTosMapIndex,
       "vrIpPgPolicyTosMapOperTable": vrIpPgPolicyTosMapOperTable,
       "vrIpPgPolicyTosMapOperEntry": vrIpPgPolicyTosMapOperEntry,
       "vrIpPgPolicyTosMapCos": vrIpPgPolicyTosMapCos,
       "vrIpPgPolicyTosMapTosTable": vrIpPgPolicyTosMapTosTable,
       "vrIpPgPolicyTosMapTosEntry": vrIpPgPolicyTosMapTosEntry,
       "vrIpPgPolicyTosMapTosValue": vrIpPgPolicyTosMapTosValue,
       "vrIpPgPolicyTosMapTosRowStatus": vrIpPgPolicyTosMapTosRowStatus,
       "vrIpPgPolicyIpAddrLayer4Flow": vrIpPgPolicyIpAddrLayer4Flow,
       "vrIpPgPolicyIpAddrLayer4FlowRowStatusTable": vrIpPgPolicyIpAddrLayer4FlowRowStatusTable,
       "vrIpPgPolicyIpAddrLayer4FlowRowStatusEntry": vrIpPgPolicyIpAddrLayer4FlowRowStatusEntry,
       "vrIpPgPolicyIpAddrLayer4FlowRowStatus": vrIpPgPolicyIpAddrLayer4FlowRowStatus,
       "vrIpPgPolicyIpAddrLayer4FlowComponentName": vrIpPgPolicyIpAddrLayer4FlowComponentName,
       "vrIpPgPolicyIpAddrLayer4FlowStorageType": vrIpPgPolicyIpAddrLayer4FlowStorageType,
       "vrIpPgPolicyIpAddrLayer4FlowIndex": vrIpPgPolicyIpAddrLayer4FlowIndex,
       "vrIpPgPolicyIpAddrLayer4FlowProvTable": vrIpPgPolicyIpAddrLayer4FlowProvTable,
       "vrIpPgPolicyIpAddrLayer4FlowProvEntry": vrIpPgPolicyIpAddrLayer4FlowProvEntry,
       "vrIpPgPolicyIpAddrLayer4FlowPrefix": vrIpPgPolicyIpAddrLayer4FlowPrefix,
       "vrIpPgPolicyIpAddrLayer4FlowPrefixLength": vrIpPgPolicyIpAddrLayer4FlowPrefixLength,
       "vrIpPgPolicyIpAddrLayer4FlowProtoProvisionedTable": vrIpPgPolicyIpAddrLayer4FlowProtoProvisionedTable,
       "vrIpPgPolicyIpAddrLayer4FlowProtoProvisionedEntry": vrIpPgPolicyIpAddrLayer4FlowProtoProvisionedEntry,
       "vrIpPgPolicyIpAddrLayer4FlowProtocol": vrIpPgPolicyIpAddrLayer4FlowProtocol,
       "vrIpPgPolicyIpAddrLayer4FlowOperTable": vrIpPgPolicyIpAddrLayer4FlowOperTable,
       "vrIpPgPolicyIpAddrLayer4FlowOperEntry": vrIpPgPolicyIpAddrLayer4FlowOperEntry,
       "vrIpPgPolicyIpAddrLayer4FlowCos": vrIpPgPolicyIpAddrLayer4FlowCos,
       "vrIpPgPolicyIpAddrLayer4FlowPortNumberRangeTable": vrIpPgPolicyIpAddrLayer4FlowPortNumberRangeTable,
       "vrIpPgPolicyIpAddrLayer4FlowPortNumberRangeEntry": vrIpPgPolicyIpAddrLayer4FlowPortNumberRangeEntry,
       "vrIpPgPolicyIpAddrLayer4FlowPortNumberRangeValue": vrIpPgPolicyIpAddrLayer4FlowPortNumberRangeValue,
       "vrIpPgPolicyIpAddrLayer4FlowPortNumberRangeRowStatus": vrIpPgPolicyIpAddrLayer4FlowPortNumberRangeRowStatus,
       "vrIpPgPolicyProvTable": vrIpPgPolicyProvTable,
       "vrIpPgPolicyProvEntry": vrIpPgPolicyProvEntry,
       "vrIpPgPolicyCosTreatmentIndex": vrIpPgPolicyCosTreatmentIndex,
       "vrIpPgCosTreatment": vrIpPgCosTreatment,
       "vrIpPgCosTreatmentRowStatusTable": vrIpPgCosTreatmentRowStatusTable,
       "vrIpPgCosTreatmentRowStatusEntry": vrIpPgCosTreatmentRowStatusEntry,
       "vrIpPgCosTreatmentRowStatus": vrIpPgCosTreatmentRowStatus,
       "vrIpPgCosTreatmentComponentName": vrIpPgCosTreatmentComponentName,
       "vrIpPgCosTreatmentStorageType": vrIpPgCosTreatmentStorageType,
       "vrIpPgCosTreatmentIndex": vrIpPgCosTreatmentIndex,
       "vrIpPgCosTreatmentProvTable": vrIpPgCosTreatmentProvTable,
       "vrIpPgCosTreatmentProvEntry": vrIpPgCosTreatmentProvEntry,
       "vrIpPgCosTreatmentCos": vrIpPgCosTreatmentCos,
       "vrIpPgCosTreatmentSetTosByte": vrIpPgCosTreatmentSetTosByte,
       "vrIpPgCosTreatmentTos": vrIpPgCosTreatmentTos,
       "vrIpPgCosTreatmentTosMask": vrIpPgCosTreatmentTosMask,
       "vrIpPgCosTreatmentEmissionPriority": vrIpPgCosTreatmentEmissionPriority,
       "vrIpPgCosTreatmentDiscardPriority": vrIpPgCosTreatmentDiscardPriority,
       "vrIpPgUsersTable": vrIpPgUsersTable,
       "vrIpPgUsersEntry": vrIpPgUsersEntry,
       "vrIpPgUsersValue": vrIpPgUsersValue,
       "vrIpPgUsersRowStatus": vrIpPgUsersRowStatus,
       "ipCosMIB": ipCosMIB,
       "ipCosGroup": ipCosGroup,
       "ipCosGroupBG": ipCosGroupBG,
       "ipCosGroupBG00": ipCosGroupBG00,
       "ipCosGroupBG00A": ipCosGroupBG00A,
       "ipCosCapabilities": ipCosCapabilities,
       "ipCosCapabilitiesBG": ipCosCapabilitiesBG,
       "ipCosCapabilitiesBG00": ipCosCapabilitiesBG00,
       "ipCosCapabilitiesBG00A": ipCosCapabilitiesBG00A}
)
