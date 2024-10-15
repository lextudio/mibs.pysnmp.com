# SNMP MIB module (Nortel-MsCarrier-MscPassport-IpCosMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-IpCosMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:38 2024
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

(mscVrIp,
 mscVrIpIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-IpMIB",
    "mscVrIp",
    "mscVrIpIndex")

(DisplayString,
 Integer32,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiStringIndex,
 Hex,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiStringIndex",
    "Hex",
    "Link",
    "NonReplicated")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscPassportMIBs")

(mscVrIndex,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-VirtualRouterMIB",
    "mscVrIndex")

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

_MscVrIpPg_ObjectIdentity = ObjectIdentity
mscVrIpPg = _MscVrIpPg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20)
)
_MscVrIpPgRowStatusTable_Object = MibTable
mscVrIpPgRowStatusTable = _MscVrIpPgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 1)
)
if mibBuilder.loadTexts:
    mscVrIpPgRowStatusTable.setStatus("mandatory")
_MscVrIpPgRowStatusEntry_Object = MibTableRow
mscVrIpPgRowStatusEntry = _MscVrIpPgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 1, 1)
)
mscVrIpPgRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpPgRowStatusEntry.setStatus("mandatory")
_MscVrIpPgRowStatus_Type = RowStatus
_MscVrIpPgRowStatus_Object = MibTableColumn
mscVrIpPgRowStatus = _MscVrIpPgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 1, 1, 1),
    _MscVrIpPgRowStatus_Type()
)
mscVrIpPgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpPgRowStatus.setStatus("mandatory")
_MscVrIpPgComponentName_Type = DisplayString
_MscVrIpPgComponentName_Object = MibTableColumn
mscVrIpPgComponentName = _MscVrIpPgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 1, 1, 2),
    _MscVrIpPgComponentName_Type()
)
mscVrIpPgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpPgComponentName.setStatus("mandatory")
_MscVrIpPgStorageType_Type = StorageType
_MscVrIpPgStorageType_Object = MibTableColumn
mscVrIpPgStorageType = _MscVrIpPgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 1, 1, 4),
    _MscVrIpPgStorageType_Type()
)
mscVrIpPgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpPgStorageType.setStatus("mandatory")


class _MscVrIpPgIndex_Type(AsciiStringIndex):
    """Custom type mscVrIpPgIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_MscVrIpPgIndex_Type.__name__ = "AsciiStringIndex"
_MscVrIpPgIndex_Object = MibTableColumn
mscVrIpPgIndex = _MscVrIpPgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 1, 1, 10),
    _MscVrIpPgIndex_Type()
)
mscVrIpPgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpPgIndex.setStatus("mandatory")
_MscVrIpPgPolicy_ObjectIdentity = ObjectIdentity
mscVrIpPgPolicy = _MscVrIpPgPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2)
)
_MscVrIpPgPolicyRowStatusTable_Object = MibTable
mscVrIpPgPolicyRowStatusTable = _MscVrIpPgPolicyRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpPgPolicyRowStatusTable.setStatus("mandatory")
_MscVrIpPgPolicyRowStatusEntry_Object = MibTableRow
mscVrIpPgPolicyRowStatusEntry = _MscVrIpPgPolicyRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 1, 1)
)
mscVrIpPgPolicyRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgPolicyIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpPgPolicyRowStatusEntry.setStatus("mandatory")
_MscVrIpPgPolicyRowStatus_Type = RowStatus
_MscVrIpPgPolicyRowStatus_Object = MibTableColumn
mscVrIpPgPolicyRowStatus = _MscVrIpPgPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 1, 1, 1),
    _MscVrIpPgPolicyRowStatus_Type()
)
mscVrIpPgPolicyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpPgPolicyRowStatus.setStatus("mandatory")
_MscVrIpPgPolicyComponentName_Type = DisplayString
_MscVrIpPgPolicyComponentName_Object = MibTableColumn
mscVrIpPgPolicyComponentName = _MscVrIpPgPolicyComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 1, 1, 2),
    _MscVrIpPgPolicyComponentName_Type()
)
mscVrIpPgPolicyComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpPgPolicyComponentName.setStatus("mandatory")
_MscVrIpPgPolicyStorageType_Type = StorageType
_MscVrIpPgPolicyStorageType_Object = MibTableColumn
mscVrIpPgPolicyStorageType = _MscVrIpPgPolicyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 1, 1, 4),
    _MscVrIpPgPolicyStorageType_Type()
)
mscVrIpPgPolicyStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpPgPolicyStorageType.setStatus("mandatory")


class _MscVrIpPgPolicyIndex_Type(AsciiStringIndex):
    """Custom type mscVrIpPgPolicyIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_MscVrIpPgPolicyIndex_Type.__name__ = "AsciiStringIndex"
_MscVrIpPgPolicyIndex_Object = MibTableColumn
mscVrIpPgPolicyIndex = _MscVrIpPgPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 1, 1, 10),
    _MscVrIpPgPolicyIndex_Type()
)
mscVrIpPgPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpPgPolicyIndex.setStatus("mandatory")
_MscVrIpPgPolicyTosMap_ObjectIdentity = ObjectIdentity
mscVrIpPgPolicyTosMap = _MscVrIpPgPolicyTosMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 2)
)
_MscVrIpPgPolicyTosMapRowStatusTable_Object = MibTable
mscVrIpPgPolicyTosMapRowStatusTable = _MscVrIpPgPolicyTosMapRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpPgPolicyTosMapRowStatusTable.setStatus("mandatory")
_MscVrIpPgPolicyTosMapRowStatusEntry_Object = MibTableRow
mscVrIpPgPolicyTosMapRowStatusEntry = _MscVrIpPgPolicyTosMapRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 2, 1, 1)
)
mscVrIpPgPolicyTosMapRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgPolicyIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgPolicyTosMapIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpPgPolicyTosMapRowStatusEntry.setStatus("mandatory")
_MscVrIpPgPolicyTosMapRowStatus_Type = RowStatus
_MscVrIpPgPolicyTosMapRowStatus_Object = MibTableColumn
mscVrIpPgPolicyTosMapRowStatus = _MscVrIpPgPolicyTosMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 2, 1, 1, 1),
    _MscVrIpPgPolicyTosMapRowStatus_Type()
)
mscVrIpPgPolicyTosMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpPgPolicyTosMapRowStatus.setStatus("mandatory")
_MscVrIpPgPolicyTosMapComponentName_Type = DisplayString
_MscVrIpPgPolicyTosMapComponentName_Object = MibTableColumn
mscVrIpPgPolicyTosMapComponentName = _MscVrIpPgPolicyTosMapComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 2, 1, 1, 2),
    _MscVrIpPgPolicyTosMapComponentName_Type()
)
mscVrIpPgPolicyTosMapComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpPgPolicyTosMapComponentName.setStatus("mandatory")
_MscVrIpPgPolicyTosMapStorageType_Type = StorageType
_MscVrIpPgPolicyTosMapStorageType_Object = MibTableColumn
mscVrIpPgPolicyTosMapStorageType = _MscVrIpPgPolicyTosMapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 2, 1, 1, 4),
    _MscVrIpPgPolicyTosMapStorageType_Type()
)
mscVrIpPgPolicyTosMapStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpPgPolicyTosMapStorageType.setStatus("mandatory")
_MscVrIpPgPolicyTosMapIndex_Type = NonReplicated
_MscVrIpPgPolicyTosMapIndex_Object = MibTableColumn
mscVrIpPgPolicyTosMapIndex = _MscVrIpPgPolicyTosMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 2, 1, 1, 10),
    _MscVrIpPgPolicyTosMapIndex_Type()
)
mscVrIpPgPolicyTosMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpPgPolicyTosMapIndex.setStatus("mandatory")
_MscVrIpPgPolicyTosMapOperTable_Object = MibTable
mscVrIpPgPolicyTosMapOperTable = _MscVrIpPgPolicyTosMapOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 2, 11)
)
if mibBuilder.loadTexts:
    mscVrIpPgPolicyTosMapOperTable.setStatus("mandatory")
_MscVrIpPgPolicyTosMapOperEntry_Object = MibTableRow
mscVrIpPgPolicyTosMapOperEntry = _MscVrIpPgPolicyTosMapOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 2, 11, 1)
)
mscVrIpPgPolicyTosMapOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgPolicyIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgPolicyTosMapIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpPgPolicyTosMapOperEntry.setStatus("mandatory")


class _MscVrIpPgPolicyTosMapCos_Type(Unsigned32):
    """Custom type mscVrIpPgPolicyTosMapCos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscVrIpPgPolicyTosMapCos_Type.__name__ = "Unsigned32"
_MscVrIpPgPolicyTosMapCos_Object = MibTableColumn
mscVrIpPgPolicyTosMapCos = _MscVrIpPgPolicyTosMapCos_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 2, 11, 1, 1),
    _MscVrIpPgPolicyTosMapCos_Type()
)
mscVrIpPgPolicyTosMapCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpPgPolicyTosMapCos.setStatus("mandatory")
_MscVrIpPgPolicyTosMapTosTable_Object = MibTable
mscVrIpPgPolicyTosMapTosTable = _MscVrIpPgPolicyTosMapTosTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 2, 434)
)
if mibBuilder.loadTexts:
    mscVrIpPgPolicyTosMapTosTable.setStatus("mandatory")
_MscVrIpPgPolicyTosMapTosEntry_Object = MibTableRow
mscVrIpPgPolicyTosMapTosEntry = _MscVrIpPgPolicyTosMapTosEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 2, 434, 1)
)
mscVrIpPgPolicyTosMapTosEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgPolicyIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgPolicyTosMapIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgPolicyTosMapTosValue"),
)
if mibBuilder.loadTexts:
    mscVrIpPgPolicyTosMapTosEntry.setStatus("mandatory")


class _MscVrIpPgPolicyTosMapTosValue_Type(Integer32):
    """Custom type mscVrIpPgPolicyTosMapTosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrIpPgPolicyTosMapTosValue_Type.__name__ = "Integer32"
_MscVrIpPgPolicyTosMapTosValue_Object = MibTableColumn
mscVrIpPgPolicyTosMapTosValue = _MscVrIpPgPolicyTosMapTosValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 2, 434, 1, 1),
    _MscVrIpPgPolicyTosMapTosValue_Type()
)
mscVrIpPgPolicyTosMapTosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpPgPolicyTosMapTosValue.setStatus("mandatory")
_MscVrIpPgPolicyTosMapTosRowStatus_Type = RowStatus
_MscVrIpPgPolicyTosMapTosRowStatus_Object = MibTableColumn
mscVrIpPgPolicyTosMapTosRowStatus = _MscVrIpPgPolicyTosMapTosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 2, 434, 1, 2),
    _MscVrIpPgPolicyTosMapTosRowStatus_Type()
)
mscVrIpPgPolicyTosMapTosRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscVrIpPgPolicyTosMapTosRowStatus.setStatus("mandatory")
_MscVrIpPgPolicyIpAddrLayer4Flow_ObjectIdentity = ObjectIdentity
mscVrIpPgPolicyIpAddrLayer4Flow = _MscVrIpPgPolicyIpAddrLayer4Flow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 3)
)
_MscVrIpPgPolicyIpAddrLayer4FlowRowStatusTable_Object = MibTable
mscVrIpPgPolicyIpAddrLayer4FlowRowStatusTable = _MscVrIpPgPolicyIpAddrLayer4FlowRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mscVrIpPgPolicyIpAddrLayer4FlowRowStatusTable.setStatus("mandatory")
_MscVrIpPgPolicyIpAddrLayer4FlowRowStatusEntry_Object = MibTableRow
mscVrIpPgPolicyIpAddrLayer4FlowRowStatusEntry = _MscVrIpPgPolicyIpAddrLayer4FlowRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 3, 1, 1)
)
mscVrIpPgPolicyIpAddrLayer4FlowRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgPolicyIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgPolicyIpAddrLayer4FlowIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpPgPolicyIpAddrLayer4FlowRowStatusEntry.setStatus("mandatory")
_MscVrIpPgPolicyIpAddrLayer4FlowRowStatus_Type = RowStatus
_MscVrIpPgPolicyIpAddrLayer4FlowRowStatus_Object = MibTableColumn
mscVrIpPgPolicyIpAddrLayer4FlowRowStatus = _MscVrIpPgPolicyIpAddrLayer4FlowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 3, 1, 1, 1),
    _MscVrIpPgPolicyIpAddrLayer4FlowRowStatus_Type()
)
mscVrIpPgPolicyIpAddrLayer4FlowRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpPgPolicyIpAddrLayer4FlowRowStatus.setStatus("mandatory")
_MscVrIpPgPolicyIpAddrLayer4FlowComponentName_Type = DisplayString
_MscVrIpPgPolicyIpAddrLayer4FlowComponentName_Object = MibTableColumn
mscVrIpPgPolicyIpAddrLayer4FlowComponentName = _MscVrIpPgPolicyIpAddrLayer4FlowComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 3, 1, 1, 2),
    _MscVrIpPgPolicyIpAddrLayer4FlowComponentName_Type()
)
mscVrIpPgPolicyIpAddrLayer4FlowComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpPgPolicyIpAddrLayer4FlowComponentName.setStatus("mandatory")
_MscVrIpPgPolicyIpAddrLayer4FlowStorageType_Type = StorageType
_MscVrIpPgPolicyIpAddrLayer4FlowStorageType_Object = MibTableColumn
mscVrIpPgPolicyIpAddrLayer4FlowStorageType = _MscVrIpPgPolicyIpAddrLayer4FlowStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 3, 1, 1, 4),
    _MscVrIpPgPolicyIpAddrLayer4FlowStorageType_Type()
)
mscVrIpPgPolicyIpAddrLayer4FlowStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpPgPolicyIpAddrLayer4FlowStorageType.setStatus("mandatory")


class _MscVrIpPgPolicyIpAddrLayer4FlowIndex_Type(Integer32):
    """Custom type mscVrIpPgPolicyIpAddrLayer4FlowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_MscVrIpPgPolicyIpAddrLayer4FlowIndex_Type.__name__ = "Integer32"
_MscVrIpPgPolicyIpAddrLayer4FlowIndex_Object = MibTableColumn
mscVrIpPgPolicyIpAddrLayer4FlowIndex = _MscVrIpPgPolicyIpAddrLayer4FlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 3, 1, 1, 10),
    _MscVrIpPgPolicyIpAddrLayer4FlowIndex_Type()
)
mscVrIpPgPolicyIpAddrLayer4FlowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpPgPolicyIpAddrLayer4FlowIndex.setStatus("mandatory")
_MscVrIpPgPolicyIpAddrLayer4FlowProvTable_Object = MibTable
mscVrIpPgPolicyIpAddrLayer4FlowProvTable = _MscVrIpPgPolicyIpAddrLayer4FlowProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 3, 10)
)
if mibBuilder.loadTexts:
    mscVrIpPgPolicyIpAddrLayer4FlowProvTable.setStatus("mandatory")
_MscVrIpPgPolicyIpAddrLayer4FlowProvEntry_Object = MibTableRow
mscVrIpPgPolicyIpAddrLayer4FlowProvEntry = _MscVrIpPgPolicyIpAddrLayer4FlowProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 3, 10, 1)
)
mscVrIpPgPolicyIpAddrLayer4FlowProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgPolicyIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgPolicyIpAddrLayer4FlowIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpPgPolicyIpAddrLayer4FlowProvEntry.setStatus("mandatory")


class _MscVrIpPgPolicyIpAddrLayer4FlowPrefix_Type(IpAddress):
    """Custom type mscVrIpPgPolicyIpAddrLayer4FlowPrefix based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrIpPgPolicyIpAddrLayer4FlowPrefix_Object = MibTableColumn
mscVrIpPgPolicyIpAddrLayer4FlowPrefix = _MscVrIpPgPolicyIpAddrLayer4FlowPrefix_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 3, 10, 1, 1),
    _MscVrIpPgPolicyIpAddrLayer4FlowPrefix_Type()
)
mscVrIpPgPolicyIpAddrLayer4FlowPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpPgPolicyIpAddrLayer4FlowPrefix.setStatus("mandatory")


class _MscVrIpPgPolicyIpAddrLayer4FlowPrefixLength_Type(Unsigned32):
    """Custom type mscVrIpPgPolicyIpAddrLayer4FlowPrefixLength based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_MscVrIpPgPolicyIpAddrLayer4FlowPrefixLength_Type.__name__ = "Unsigned32"
_MscVrIpPgPolicyIpAddrLayer4FlowPrefixLength_Object = MibTableColumn
mscVrIpPgPolicyIpAddrLayer4FlowPrefixLength = _MscVrIpPgPolicyIpAddrLayer4FlowPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 3, 10, 1, 2),
    _MscVrIpPgPolicyIpAddrLayer4FlowPrefixLength_Type()
)
mscVrIpPgPolicyIpAddrLayer4FlowPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpPgPolicyIpAddrLayer4FlowPrefixLength.setStatus("mandatory")
_MscVrIpPgPolicyIpAddrLayer4FlowProtoProvisionedTable_Object = MibTable
mscVrIpPgPolicyIpAddrLayer4FlowProtoProvisionedTable = _MscVrIpPgPolicyIpAddrLayer4FlowProtoProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 3, 11)
)
if mibBuilder.loadTexts:
    mscVrIpPgPolicyIpAddrLayer4FlowProtoProvisionedTable.setStatus("mandatory")
_MscVrIpPgPolicyIpAddrLayer4FlowProtoProvisionedEntry_Object = MibTableRow
mscVrIpPgPolicyIpAddrLayer4FlowProtoProvisionedEntry = _MscVrIpPgPolicyIpAddrLayer4FlowProtoProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 3, 11, 1)
)
mscVrIpPgPolicyIpAddrLayer4FlowProtoProvisionedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgPolicyIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgPolicyIpAddrLayer4FlowIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpPgPolicyIpAddrLayer4FlowProtoProvisionedEntry.setStatus("mandatory")


class _MscVrIpPgPolicyIpAddrLayer4FlowProtocol_Type(Integer32):
    """Custom type mscVrIpPgPolicyIpAddrLayer4FlowProtocol based on Integer32"""
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


_MscVrIpPgPolicyIpAddrLayer4FlowProtocol_Type.__name__ = "Integer32"
_MscVrIpPgPolicyIpAddrLayer4FlowProtocol_Object = MibTableColumn
mscVrIpPgPolicyIpAddrLayer4FlowProtocol = _MscVrIpPgPolicyIpAddrLayer4FlowProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 3, 11, 1, 1),
    _MscVrIpPgPolicyIpAddrLayer4FlowProtocol_Type()
)
mscVrIpPgPolicyIpAddrLayer4FlowProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpPgPolicyIpAddrLayer4FlowProtocol.setStatus("mandatory")
_MscVrIpPgPolicyIpAddrLayer4FlowOperTable_Object = MibTable
mscVrIpPgPolicyIpAddrLayer4FlowOperTable = _MscVrIpPgPolicyIpAddrLayer4FlowOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 3, 12)
)
if mibBuilder.loadTexts:
    mscVrIpPgPolicyIpAddrLayer4FlowOperTable.setStatus("mandatory")
_MscVrIpPgPolicyIpAddrLayer4FlowOperEntry_Object = MibTableRow
mscVrIpPgPolicyIpAddrLayer4FlowOperEntry = _MscVrIpPgPolicyIpAddrLayer4FlowOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 3, 12, 1)
)
mscVrIpPgPolicyIpAddrLayer4FlowOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgPolicyIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgPolicyIpAddrLayer4FlowIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpPgPolicyIpAddrLayer4FlowOperEntry.setStatus("mandatory")


class _MscVrIpPgPolicyIpAddrLayer4FlowCos_Type(Unsigned32):
    """Custom type mscVrIpPgPolicyIpAddrLayer4FlowCos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscVrIpPgPolicyIpAddrLayer4FlowCos_Type.__name__ = "Unsigned32"
_MscVrIpPgPolicyIpAddrLayer4FlowCos_Object = MibTableColumn
mscVrIpPgPolicyIpAddrLayer4FlowCos = _MscVrIpPgPolicyIpAddrLayer4FlowCos_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 3, 12, 1, 1),
    _MscVrIpPgPolicyIpAddrLayer4FlowCos_Type()
)
mscVrIpPgPolicyIpAddrLayer4FlowCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpPgPolicyIpAddrLayer4FlowCos.setStatus("mandatory")
_MscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeTable_Object = MibTable
mscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeTable = _MscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 3, 435)
)
if mibBuilder.loadTexts:
    mscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeTable.setStatus("mandatory")
_MscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeEntry_Object = MibTableRow
mscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeEntry = _MscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 3, 435, 1)
)
mscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgPolicyIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgPolicyIpAddrLayer4FlowIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeValue"),
)
if mibBuilder.loadTexts:
    mscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeEntry.setStatus("mandatory")


class _MscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeValue_Type(Integer32):
    """Custom type mscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeValue_Type.__name__ = "Integer32"
_MscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeValue_Object = MibTableColumn
mscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeValue = _MscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 3, 435, 1, 1),
    _MscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeValue_Type()
)
mscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeValue.setStatus("mandatory")
_MscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeRowStatus_Type = RowStatus
_MscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeRowStatus_Object = MibTableColumn
mscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeRowStatus = _MscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 3, 435, 1, 2),
    _MscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeRowStatus_Type()
)
mscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeRowStatus.setStatus("mandatory")
_MscVrIpPgPolicyProvTable_Object = MibTable
mscVrIpPgPolicyProvTable = _MscVrIpPgPolicyProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpPgPolicyProvTable.setStatus("mandatory")
_MscVrIpPgPolicyProvEntry_Object = MibTableRow
mscVrIpPgPolicyProvEntry = _MscVrIpPgPolicyProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 10, 1)
)
mscVrIpPgPolicyProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgPolicyIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpPgPolicyProvEntry.setStatus("mandatory")


class _MscVrIpPgPolicyCosTreatmentIndex_Type(Unsigned32):
    """Custom type mscVrIpPgPolicyCosTreatmentIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscVrIpPgPolicyCosTreatmentIndex_Type.__name__ = "Unsigned32"
_MscVrIpPgPolicyCosTreatmentIndex_Object = MibTableColumn
mscVrIpPgPolicyCosTreatmentIndex = _MscVrIpPgPolicyCosTreatmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 2, 10, 1, 1),
    _MscVrIpPgPolicyCosTreatmentIndex_Type()
)
mscVrIpPgPolicyCosTreatmentIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpPgPolicyCosTreatmentIndex.setStatus("mandatory")
_MscVrIpPgCosTreatment_ObjectIdentity = ObjectIdentity
mscVrIpPgCosTreatment = _MscVrIpPgCosTreatment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 3)
)
_MscVrIpPgCosTreatmentRowStatusTable_Object = MibTable
mscVrIpPgCosTreatmentRowStatusTable = _MscVrIpPgCosTreatmentRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 3, 1)
)
if mibBuilder.loadTexts:
    mscVrIpPgCosTreatmentRowStatusTable.setStatus("mandatory")
_MscVrIpPgCosTreatmentRowStatusEntry_Object = MibTableRow
mscVrIpPgCosTreatmentRowStatusEntry = _MscVrIpPgCosTreatmentRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 3, 1, 1)
)
mscVrIpPgCosTreatmentRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgCosTreatmentIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpPgCosTreatmentRowStatusEntry.setStatus("mandatory")
_MscVrIpPgCosTreatmentRowStatus_Type = RowStatus
_MscVrIpPgCosTreatmentRowStatus_Object = MibTableColumn
mscVrIpPgCosTreatmentRowStatus = _MscVrIpPgCosTreatmentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 3, 1, 1, 1),
    _MscVrIpPgCosTreatmentRowStatus_Type()
)
mscVrIpPgCosTreatmentRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpPgCosTreatmentRowStatus.setStatus("mandatory")
_MscVrIpPgCosTreatmentComponentName_Type = DisplayString
_MscVrIpPgCosTreatmentComponentName_Object = MibTableColumn
mscVrIpPgCosTreatmentComponentName = _MscVrIpPgCosTreatmentComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 3, 1, 1, 2),
    _MscVrIpPgCosTreatmentComponentName_Type()
)
mscVrIpPgCosTreatmentComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpPgCosTreatmentComponentName.setStatus("mandatory")
_MscVrIpPgCosTreatmentStorageType_Type = StorageType
_MscVrIpPgCosTreatmentStorageType_Object = MibTableColumn
mscVrIpPgCosTreatmentStorageType = _MscVrIpPgCosTreatmentStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 3, 1, 1, 4),
    _MscVrIpPgCosTreatmentStorageType_Type()
)
mscVrIpPgCosTreatmentStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpPgCosTreatmentStorageType.setStatus("mandatory")


class _MscVrIpPgCosTreatmentIndex_Type(Integer32):
    """Custom type mscVrIpPgCosTreatmentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscVrIpPgCosTreatmentIndex_Type.__name__ = "Integer32"
_MscVrIpPgCosTreatmentIndex_Object = MibTableColumn
mscVrIpPgCosTreatmentIndex = _MscVrIpPgCosTreatmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 3, 1, 1, 10),
    _MscVrIpPgCosTreatmentIndex_Type()
)
mscVrIpPgCosTreatmentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpPgCosTreatmentIndex.setStatus("mandatory")
_MscVrIpPgCosTreatmentProvTable_Object = MibTable
mscVrIpPgCosTreatmentProvTable = _MscVrIpPgCosTreatmentProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 3, 10)
)
if mibBuilder.loadTexts:
    mscVrIpPgCosTreatmentProvTable.setStatus("mandatory")
_MscVrIpPgCosTreatmentProvEntry_Object = MibTableRow
mscVrIpPgCosTreatmentProvEntry = _MscVrIpPgCosTreatmentProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 3, 10, 1)
)
mscVrIpPgCosTreatmentProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgCosTreatmentIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpPgCosTreatmentProvEntry.setStatus("mandatory")


class _MscVrIpPgCosTreatmentCos_Type(Unsigned32):
    """Custom type mscVrIpPgCosTreatmentCos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscVrIpPgCosTreatmentCos_Type.__name__ = "Unsigned32"
_MscVrIpPgCosTreatmentCos_Object = MibTableColumn
mscVrIpPgCosTreatmentCos = _MscVrIpPgCosTreatmentCos_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 3, 10, 1, 1),
    _MscVrIpPgCosTreatmentCos_Type()
)
mscVrIpPgCosTreatmentCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpPgCosTreatmentCos.setStatus("mandatory")


class _MscVrIpPgCosTreatmentSetTosByte_Type(Integer32):
    """Custom type mscVrIpPgCosTreatmentSetTosByte based on Integer32"""
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


_MscVrIpPgCosTreatmentSetTosByte_Type.__name__ = "Integer32"
_MscVrIpPgCosTreatmentSetTosByte_Object = MibTableColumn
mscVrIpPgCosTreatmentSetTosByte = _MscVrIpPgCosTreatmentSetTosByte_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 3, 10, 1, 3),
    _MscVrIpPgCosTreatmentSetTosByte_Type()
)
mscVrIpPgCosTreatmentSetTosByte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpPgCosTreatmentSetTosByte.setStatus("mandatory")


class _MscVrIpPgCosTreatmentTos_Type(Hex):
    """Custom type mscVrIpPgCosTreatmentTos based on Hex"""
    defaultValue = 0

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrIpPgCosTreatmentTos_Type.__name__ = "Hex"
_MscVrIpPgCosTreatmentTos_Object = MibTableColumn
mscVrIpPgCosTreatmentTos = _MscVrIpPgCosTreatmentTos_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 3, 10, 1, 4),
    _MscVrIpPgCosTreatmentTos_Type()
)
mscVrIpPgCosTreatmentTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpPgCosTreatmentTos.setStatus("mandatory")


class _MscVrIpPgCosTreatmentTosMask_Type(Hex):
    """Custom type mscVrIpPgCosTreatmentTosMask based on Hex"""
    defaultValue = 224

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscVrIpPgCosTreatmentTosMask_Type.__name__ = "Hex"
_MscVrIpPgCosTreatmentTosMask_Object = MibTableColumn
mscVrIpPgCosTreatmentTosMask = _MscVrIpPgCosTreatmentTosMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 3, 10, 1, 5),
    _MscVrIpPgCosTreatmentTosMask_Type()
)
mscVrIpPgCosTreatmentTosMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpPgCosTreatmentTosMask.setStatus("mandatory")
_MscVrIpPgUsersTable_Object = MibTable
mscVrIpPgUsersTable = _MscVrIpPgUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 432)
)
if mibBuilder.loadTexts:
    mscVrIpPgUsersTable.setStatus("mandatory")
_MscVrIpPgUsersEntry_Object = MibTableRow
mscVrIpPgUsersEntry = _MscVrIpPgUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 432, 1)
)
mscVrIpPgUsersEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpCosMIB", "mscVrIpPgUsersValue"),
)
if mibBuilder.loadTexts:
    mscVrIpPgUsersEntry.setStatus("mandatory")
_MscVrIpPgUsersValue_Type = Link
_MscVrIpPgUsersValue_Object = MibTableColumn
mscVrIpPgUsersValue = _MscVrIpPgUsersValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 432, 1, 1),
    _MscVrIpPgUsersValue_Type()
)
mscVrIpPgUsersValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpPgUsersValue.setStatus("mandatory")
_MscVrIpPgUsersRowStatus_Type = RowStatus
_MscVrIpPgUsersRowStatus_Object = MibTableColumn
mscVrIpPgUsersRowStatus = _MscVrIpPgUsersRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 20, 432, 1, 2),
    _MscVrIpPgUsersRowStatus_Type()
)
mscVrIpPgUsersRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscVrIpPgUsersRowStatus.setStatus("mandatory")
_IpCosMIB_ObjectIdentity = ObjectIdentity
ipCosMIB = _IpCosMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 161)
)
_IpCosGroup_ObjectIdentity = ObjectIdentity
ipCosGroup = _IpCosGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 161, 1)
)
_IpCosGroupCA_ObjectIdentity = ObjectIdentity
ipCosGroupCA = _IpCosGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 161, 1, 1)
)
_IpCosGroupCA02_ObjectIdentity = ObjectIdentity
ipCosGroupCA02 = _IpCosGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 161, 1, 1, 3)
)
_IpCosGroupCA02A_ObjectIdentity = ObjectIdentity
ipCosGroupCA02A = _IpCosGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 161, 1, 1, 3, 2)
)
_IpCosCapabilities_ObjectIdentity = ObjectIdentity
ipCosCapabilities = _IpCosCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 161, 3)
)
_IpCosCapabilitiesCA_ObjectIdentity = ObjectIdentity
ipCosCapabilitiesCA = _IpCosCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 161, 3, 1)
)
_IpCosCapabilitiesCA02_ObjectIdentity = ObjectIdentity
ipCosCapabilitiesCA02 = _IpCosCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 161, 3, 1, 3)
)
_IpCosCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
ipCosCapabilitiesCA02A = _IpCosCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 161, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-IpCosMIB",
    **{"mscVrIpPg": mscVrIpPg,
       "mscVrIpPgRowStatusTable": mscVrIpPgRowStatusTable,
       "mscVrIpPgRowStatusEntry": mscVrIpPgRowStatusEntry,
       "mscVrIpPgRowStatus": mscVrIpPgRowStatus,
       "mscVrIpPgComponentName": mscVrIpPgComponentName,
       "mscVrIpPgStorageType": mscVrIpPgStorageType,
       "mscVrIpPgIndex": mscVrIpPgIndex,
       "mscVrIpPgPolicy": mscVrIpPgPolicy,
       "mscVrIpPgPolicyRowStatusTable": mscVrIpPgPolicyRowStatusTable,
       "mscVrIpPgPolicyRowStatusEntry": mscVrIpPgPolicyRowStatusEntry,
       "mscVrIpPgPolicyRowStatus": mscVrIpPgPolicyRowStatus,
       "mscVrIpPgPolicyComponentName": mscVrIpPgPolicyComponentName,
       "mscVrIpPgPolicyStorageType": mscVrIpPgPolicyStorageType,
       "mscVrIpPgPolicyIndex": mscVrIpPgPolicyIndex,
       "mscVrIpPgPolicyTosMap": mscVrIpPgPolicyTosMap,
       "mscVrIpPgPolicyTosMapRowStatusTable": mscVrIpPgPolicyTosMapRowStatusTable,
       "mscVrIpPgPolicyTosMapRowStatusEntry": mscVrIpPgPolicyTosMapRowStatusEntry,
       "mscVrIpPgPolicyTosMapRowStatus": mscVrIpPgPolicyTosMapRowStatus,
       "mscVrIpPgPolicyTosMapComponentName": mscVrIpPgPolicyTosMapComponentName,
       "mscVrIpPgPolicyTosMapStorageType": mscVrIpPgPolicyTosMapStorageType,
       "mscVrIpPgPolicyTosMapIndex": mscVrIpPgPolicyTosMapIndex,
       "mscVrIpPgPolicyTosMapOperTable": mscVrIpPgPolicyTosMapOperTable,
       "mscVrIpPgPolicyTosMapOperEntry": mscVrIpPgPolicyTosMapOperEntry,
       "mscVrIpPgPolicyTosMapCos": mscVrIpPgPolicyTosMapCos,
       "mscVrIpPgPolicyTosMapTosTable": mscVrIpPgPolicyTosMapTosTable,
       "mscVrIpPgPolicyTosMapTosEntry": mscVrIpPgPolicyTosMapTosEntry,
       "mscVrIpPgPolicyTosMapTosValue": mscVrIpPgPolicyTosMapTosValue,
       "mscVrIpPgPolicyTosMapTosRowStatus": mscVrIpPgPolicyTosMapTosRowStatus,
       "mscVrIpPgPolicyIpAddrLayer4Flow": mscVrIpPgPolicyIpAddrLayer4Flow,
       "mscVrIpPgPolicyIpAddrLayer4FlowRowStatusTable": mscVrIpPgPolicyIpAddrLayer4FlowRowStatusTable,
       "mscVrIpPgPolicyIpAddrLayer4FlowRowStatusEntry": mscVrIpPgPolicyIpAddrLayer4FlowRowStatusEntry,
       "mscVrIpPgPolicyIpAddrLayer4FlowRowStatus": mscVrIpPgPolicyIpAddrLayer4FlowRowStatus,
       "mscVrIpPgPolicyIpAddrLayer4FlowComponentName": mscVrIpPgPolicyIpAddrLayer4FlowComponentName,
       "mscVrIpPgPolicyIpAddrLayer4FlowStorageType": mscVrIpPgPolicyIpAddrLayer4FlowStorageType,
       "mscVrIpPgPolicyIpAddrLayer4FlowIndex": mscVrIpPgPolicyIpAddrLayer4FlowIndex,
       "mscVrIpPgPolicyIpAddrLayer4FlowProvTable": mscVrIpPgPolicyIpAddrLayer4FlowProvTable,
       "mscVrIpPgPolicyIpAddrLayer4FlowProvEntry": mscVrIpPgPolicyIpAddrLayer4FlowProvEntry,
       "mscVrIpPgPolicyIpAddrLayer4FlowPrefix": mscVrIpPgPolicyIpAddrLayer4FlowPrefix,
       "mscVrIpPgPolicyIpAddrLayer4FlowPrefixLength": mscVrIpPgPolicyIpAddrLayer4FlowPrefixLength,
       "mscVrIpPgPolicyIpAddrLayer4FlowProtoProvisionedTable": mscVrIpPgPolicyIpAddrLayer4FlowProtoProvisionedTable,
       "mscVrIpPgPolicyIpAddrLayer4FlowProtoProvisionedEntry": mscVrIpPgPolicyIpAddrLayer4FlowProtoProvisionedEntry,
       "mscVrIpPgPolicyIpAddrLayer4FlowProtocol": mscVrIpPgPolicyIpAddrLayer4FlowProtocol,
       "mscVrIpPgPolicyIpAddrLayer4FlowOperTable": mscVrIpPgPolicyIpAddrLayer4FlowOperTable,
       "mscVrIpPgPolicyIpAddrLayer4FlowOperEntry": mscVrIpPgPolicyIpAddrLayer4FlowOperEntry,
       "mscVrIpPgPolicyIpAddrLayer4FlowCos": mscVrIpPgPolicyIpAddrLayer4FlowCos,
       "mscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeTable": mscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeTable,
       "mscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeEntry": mscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeEntry,
       "mscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeValue": mscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeValue,
       "mscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeRowStatus": mscVrIpPgPolicyIpAddrLayer4FlowPortNumberRangeRowStatus,
       "mscVrIpPgPolicyProvTable": mscVrIpPgPolicyProvTable,
       "mscVrIpPgPolicyProvEntry": mscVrIpPgPolicyProvEntry,
       "mscVrIpPgPolicyCosTreatmentIndex": mscVrIpPgPolicyCosTreatmentIndex,
       "mscVrIpPgCosTreatment": mscVrIpPgCosTreatment,
       "mscVrIpPgCosTreatmentRowStatusTable": mscVrIpPgCosTreatmentRowStatusTable,
       "mscVrIpPgCosTreatmentRowStatusEntry": mscVrIpPgCosTreatmentRowStatusEntry,
       "mscVrIpPgCosTreatmentRowStatus": mscVrIpPgCosTreatmentRowStatus,
       "mscVrIpPgCosTreatmentComponentName": mscVrIpPgCosTreatmentComponentName,
       "mscVrIpPgCosTreatmentStorageType": mscVrIpPgCosTreatmentStorageType,
       "mscVrIpPgCosTreatmentIndex": mscVrIpPgCosTreatmentIndex,
       "mscVrIpPgCosTreatmentProvTable": mscVrIpPgCosTreatmentProvTable,
       "mscVrIpPgCosTreatmentProvEntry": mscVrIpPgCosTreatmentProvEntry,
       "mscVrIpPgCosTreatmentCos": mscVrIpPgCosTreatmentCos,
       "mscVrIpPgCosTreatmentSetTosByte": mscVrIpPgCosTreatmentSetTosByte,
       "mscVrIpPgCosTreatmentTos": mscVrIpPgCosTreatmentTos,
       "mscVrIpPgCosTreatmentTosMask": mscVrIpPgCosTreatmentTosMask,
       "mscVrIpPgUsersTable": mscVrIpPgUsersTable,
       "mscVrIpPgUsersEntry": mscVrIpPgUsersEntry,
       "mscVrIpPgUsersValue": mscVrIpPgUsersValue,
       "mscVrIpPgUsersRowStatus": mscVrIpPgUsersRowStatus,
       "ipCosMIB": ipCosMIB,
       "ipCosGroup": ipCosGroup,
       "ipCosGroupCA": ipCosGroupCA,
       "ipCosGroupCA02": ipCosGroupCA02,
       "ipCosGroupCA02A": ipCosGroupCA02A,
       "ipCosCapabilities": ipCosCapabilities,
       "ipCosCapabilitiesCA": ipCosCapabilitiesCA,
       "ipCosCapabilitiesCA02": ipCosCapabilitiesCA02,
       "ipCosCapabilitiesCA02A": ipCosCapabilitiesCA02A}
)
