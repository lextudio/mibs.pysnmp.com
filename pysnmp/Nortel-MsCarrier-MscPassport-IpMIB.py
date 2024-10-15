# SNMP MIB module (Nortel-MsCarrier-MscPassport-IpMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-IpMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:00 2024
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

(AreaID,
 Counter32,
 DisplayString,
 Gauge32,
 Integer32,
 InterfaceIndex,
 PhysAddress,
 RouterID,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "AreaID",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "InterfaceIndex",
    "PhysAddress",
    "RouterID",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 AsciiStringIndex,
 DashedHexString,
 HexString,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
    "DashedHexString",
    "HexString",
    "Link",
    "NonReplicated")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscPassportMIBs")

(mscVr,
 mscVrIndex,
 mscVrPp,
 mscVrPpIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-VirtualRouterMIB",
    "mscVr",
    "mscVrIndex",
    "mscVrPp",
    "mscVrPpIndex")

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

_MscVrPpIpPort_ObjectIdentity = ObjectIdentity
mscVrPpIpPort = _MscVrPpIpPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5)
)
_MscVrPpIpPortRowStatusTable_Object = MibTable
mscVrPpIpPortRowStatusTable = _MscVrPpIpPortRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 1)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortRowStatusTable.setStatus("mandatory")
_MscVrPpIpPortRowStatusEntry_Object = MibTableRow
mscVrPpIpPortRowStatusEntry = _MscVrPpIpPortRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 1, 1)
)
mscVrPpIpPortRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortRowStatusEntry.setStatus("mandatory")
_MscVrPpIpPortRowStatus_Type = RowStatus
_MscVrPpIpPortRowStatus_Object = MibTableColumn
mscVrPpIpPortRowStatus = _MscVrPpIpPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 1, 1, 1),
    _MscVrPpIpPortRowStatus_Type()
)
mscVrPpIpPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortRowStatus.setStatus("mandatory")
_MscVrPpIpPortComponentName_Type = DisplayString
_MscVrPpIpPortComponentName_Object = MibTableColumn
mscVrPpIpPortComponentName = _MscVrPpIpPortComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 1, 1, 2),
    _MscVrPpIpPortComponentName_Type()
)
mscVrPpIpPortComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortComponentName.setStatus("mandatory")
_MscVrPpIpPortStorageType_Type = StorageType
_MscVrPpIpPortStorageType_Object = MibTableColumn
mscVrPpIpPortStorageType = _MscVrPpIpPortStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 1, 1, 4),
    _MscVrPpIpPortStorageType_Type()
)
mscVrPpIpPortStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortStorageType.setStatus("mandatory")
_MscVrPpIpPortIndex_Type = NonReplicated
_MscVrPpIpPortIndex_Object = MibTableColumn
mscVrPpIpPortIndex = _MscVrPpIpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 1, 1, 10),
    _MscVrPpIpPortIndex_Type()
)
mscVrPpIpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpIpPortIndex.setStatus("mandatory")
_MscVrPpIpPortLogicalIf_ObjectIdentity = ObjectIdentity
mscVrPpIpPortLogicalIf = _MscVrPpIpPortLogicalIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2)
)
_MscVrPpIpPortLogicalIfRowStatusTable_Object = MibTable
mscVrPpIpPortLogicalIfRowStatusTable = _MscVrPpIpPortLogicalIfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRowStatusTable.setStatus("mandatory")
_MscVrPpIpPortLogicalIfRowStatusEntry_Object = MibTableRow
mscVrPpIpPortLogicalIfRowStatusEntry = _MscVrPpIpPortLogicalIfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 1, 1)
)
mscVrPpIpPortLogicalIfRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRowStatusEntry.setStatus("mandatory")
_MscVrPpIpPortLogicalIfRowStatus_Type = RowStatus
_MscVrPpIpPortLogicalIfRowStatus_Object = MibTableColumn
mscVrPpIpPortLogicalIfRowStatus = _MscVrPpIpPortLogicalIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 1, 1, 1),
    _MscVrPpIpPortLogicalIfRowStatus_Type()
)
mscVrPpIpPortLogicalIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRowStatus.setStatus("mandatory")
_MscVrPpIpPortLogicalIfComponentName_Type = DisplayString
_MscVrPpIpPortLogicalIfComponentName_Object = MibTableColumn
mscVrPpIpPortLogicalIfComponentName = _MscVrPpIpPortLogicalIfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 1, 1, 2),
    _MscVrPpIpPortLogicalIfComponentName_Type()
)
mscVrPpIpPortLogicalIfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfComponentName.setStatus("mandatory")
_MscVrPpIpPortLogicalIfStorageType_Type = StorageType
_MscVrPpIpPortLogicalIfStorageType_Object = MibTableColumn
mscVrPpIpPortLogicalIfStorageType = _MscVrPpIpPortLogicalIfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 1, 1, 4),
    _MscVrPpIpPortLogicalIfStorageType_Type()
)
mscVrPpIpPortLogicalIfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfStorageType.setStatus("mandatory")
_MscVrPpIpPortLogicalIfAddressIndex_Type = IpAddress
_MscVrPpIpPortLogicalIfAddressIndex_Object = MibTableColumn
mscVrPpIpPortLogicalIfAddressIndex = _MscVrPpIpPortLogicalIfAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 1, 1, 10),
    _MscVrPpIpPortLogicalIfAddressIndex_Type()
)
mscVrPpIpPortLogicalIfAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfAddressIndex.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIf_ObjectIdentity = ObjectIdentity
mscVrPpIpPortLogicalIfOspfIf = _MscVrPpIpPortLogicalIfOspfIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2)
)
_MscVrPpIpPortLogicalIfOspfIfRowStatusTable_Object = MibTable
mscVrPpIpPortLogicalIfOspfIfRowStatusTable = _MscVrPpIpPortLogicalIfOspfIfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfRowStatusTable.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfRowStatusEntry_Object = MibTableRow
mscVrPpIpPortLogicalIfOspfIfRowStatusEntry = _MscVrPpIpPortLogicalIfOspfIfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 1, 1)
)
mscVrPpIpPortLogicalIfOspfIfRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfOspfIfIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfRowStatusEntry.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfRowStatus_Type = RowStatus
_MscVrPpIpPortLogicalIfOspfIfRowStatus_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfRowStatus = _MscVrPpIpPortLogicalIfOspfIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 1, 1, 1),
    _MscVrPpIpPortLogicalIfOspfIfRowStatus_Type()
)
mscVrPpIpPortLogicalIfOspfIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfRowStatus.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfComponentName_Type = DisplayString
_MscVrPpIpPortLogicalIfOspfIfComponentName_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfComponentName = _MscVrPpIpPortLogicalIfOspfIfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 1, 1, 2),
    _MscVrPpIpPortLogicalIfOspfIfComponentName_Type()
)
mscVrPpIpPortLogicalIfOspfIfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfComponentName.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfStorageType_Type = StorageType
_MscVrPpIpPortLogicalIfOspfIfStorageType_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfStorageType = _MscVrPpIpPortLogicalIfOspfIfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 1, 1, 4),
    _MscVrPpIpPortLogicalIfOspfIfStorageType_Type()
)
mscVrPpIpPortLogicalIfOspfIfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfStorageType.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfIndex_Type = NonReplicated
_MscVrPpIpPortLogicalIfOspfIfIndex_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfIndex = _MscVrPpIpPortLogicalIfOspfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 1, 1, 10),
    _MscVrPpIpPortLogicalIfOspfIfIndex_Type()
)
mscVrPpIpPortLogicalIfOspfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfIndex.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfTOS_ObjectIdentity = ObjectIdentity
mscVrPpIpPortLogicalIfOspfIfTOS = _MscVrPpIpPortLogicalIfOspfIfTOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 2)
)
_MscVrPpIpPortLogicalIfOspfIfTOSRowStatusTable_Object = MibTable
mscVrPpIpPortLogicalIfOspfIfTOSRowStatusTable = _MscVrPpIpPortLogicalIfOspfIfTOSRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfTOSRowStatusTable.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfTOSRowStatusEntry_Object = MibTableRow
mscVrPpIpPortLogicalIfOspfIfTOSRowStatusEntry = _MscVrPpIpPortLogicalIfOspfIfTOSRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 2, 1, 1)
)
mscVrPpIpPortLogicalIfOspfIfTOSRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfOspfIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfOspfIfTOSMetricTosIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfTOSRowStatusEntry.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfTOSRowStatus_Type = RowStatus
_MscVrPpIpPortLogicalIfOspfIfTOSRowStatus_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfTOSRowStatus = _MscVrPpIpPortLogicalIfOspfIfTOSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 2, 1, 1, 1),
    _MscVrPpIpPortLogicalIfOspfIfTOSRowStatus_Type()
)
mscVrPpIpPortLogicalIfOspfIfTOSRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfTOSRowStatus.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfTOSComponentName_Type = DisplayString
_MscVrPpIpPortLogicalIfOspfIfTOSComponentName_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfTOSComponentName = _MscVrPpIpPortLogicalIfOspfIfTOSComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 2, 1, 1, 2),
    _MscVrPpIpPortLogicalIfOspfIfTOSComponentName_Type()
)
mscVrPpIpPortLogicalIfOspfIfTOSComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfTOSComponentName.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfTOSStorageType_Type = StorageType
_MscVrPpIpPortLogicalIfOspfIfTOSStorageType_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfTOSStorageType = _MscVrPpIpPortLogicalIfOspfIfTOSStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 2, 1, 1, 4),
    _MscVrPpIpPortLogicalIfOspfIfTOSStorageType_Type()
)
mscVrPpIpPortLogicalIfOspfIfTOSStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfTOSStorageType.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfOspfIfTOSMetricTosIndex_Type(Integer32):
    """Custom type mscVrPpIpPortLogicalIfOspfIfTOSMetricTosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_MscVrPpIpPortLogicalIfOspfIfTOSMetricTosIndex_Type.__name__ = "Integer32"
_MscVrPpIpPortLogicalIfOspfIfTOSMetricTosIndex_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfTOSMetricTosIndex = _MscVrPpIpPortLogicalIfOspfIfTOSMetricTosIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 2, 1, 1, 10),
    _MscVrPpIpPortLogicalIfOspfIfTOSMetricTosIndex_Type()
)
mscVrPpIpPortLogicalIfOspfIfTOSMetricTosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfTOSMetricTosIndex.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfTOSProvTable_Object = MibTable
mscVrPpIpPortLogicalIfOspfIfTOSProvTable = _MscVrPpIpPortLogicalIfOspfIfTOSProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfTOSProvTable.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfTOSProvEntry_Object = MibTableRow
mscVrPpIpPortLogicalIfOspfIfTOSProvEntry = _MscVrPpIpPortLogicalIfOspfIfTOSProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 2, 10, 1)
)
mscVrPpIpPortLogicalIfOspfIfTOSProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfOspfIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfOspfIfTOSMetricTosIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfTOSProvEntry.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfOspfIfTOSTosMetric_Type(Unsigned32):
    """Custom type mscVrPpIpPortLogicalIfOspfIfTOSTosMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrPpIpPortLogicalIfOspfIfTOSTosMetric_Type.__name__ = "Unsigned32"
_MscVrPpIpPortLogicalIfOspfIfTOSTosMetric_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfTOSTosMetric = _MscVrPpIpPortLogicalIfOspfIfTOSTosMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 2, 10, 1, 1),
    _MscVrPpIpPortLogicalIfOspfIfTOSTosMetric_Type()
)
mscVrPpIpPortLogicalIfOspfIfTOSTosMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfTOSTosMetric.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfNbr_ObjectIdentity = ObjectIdentity
mscVrPpIpPortLogicalIfOspfIfNbr = _MscVrPpIpPortLogicalIfOspfIfNbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 3)
)
_MscVrPpIpPortLogicalIfOspfIfNbrRowStatusTable_Object = MibTable
mscVrPpIpPortLogicalIfOspfIfNbrRowStatusTable = _MscVrPpIpPortLogicalIfOspfIfNbrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfNbrRowStatusTable.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfNbrRowStatusEntry_Object = MibTableRow
mscVrPpIpPortLogicalIfOspfIfNbrRowStatusEntry = _MscVrPpIpPortLogicalIfOspfIfNbrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 3, 1, 1)
)
mscVrPpIpPortLogicalIfOspfIfNbrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfOspfIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfOspfIfNbrAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfNbrRowStatusEntry.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfNbrRowStatus_Type = RowStatus
_MscVrPpIpPortLogicalIfOspfIfNbrRowStatus_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfNbrRowStatus = _MscVrPpIpPortLogicalIfOspfIfNbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 3, 1, 1, 1),
    _MscVrPpIpPortLogicalIfOspfIfNbrRowStatus_Type()
)
mscVrPpIpPortLogicalIfOspfIfNbrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfNbrRowStatus.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfNbrComponentName_Type = DisplayString
_MscVrPpIpPortLogicalIfOspfIfNbrComponentName_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfNbrComponentName = _MscVrPpIpPortLogicalIfOspfIfNbrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 3, 1, 1, 2),
    _MscVrPpIpPortLogicalIfOspfIfNbrComponentName_Type()
)
mscVrPpIpPortLogicalIfOspfIfNbrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfNbrComponentName.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfNbrStorageType_Type = StorageType
_MscVrPpIpPortLogicalIfOspfIfNbrStorageType_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfNbrStorageType = _MscVrPpIpPortLogicalIfOspfIfNbrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 3, 1, 1, 4),
    _MscVrPpIpPortLogicalIfOspfIfNbrStorageType_Type()
)
mscVrPpIpPortLogicalIfOspfIfNbrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfNbrStorageType.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfNbrAddressIndex_Type = IpAddress
_MscVrPpIpPortLogicalIfOspfIfNbrAddressIndex_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfNbrAddressIndex = _MscVrPpIpPortLogicalIfOspfIfNbrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 3, 1, 1, 10),
    _MscVrPpIpPortLogicalIfOspfIfNbrAddressIndex_Type()
)
mscVrPpIpPortLogicalIfOspfIfNbrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfNbrAddressIndex.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfNbrProvTable_Object = MibTable
mscVrPpIpPortLogicalIfOspfIfNbrProvTable = _MscVrPpIpPortLogicalIfOspfIfNbrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 3, 10)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfNbrProvTable.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfNbrProvEntry_Object = MibTableRow
mscVrPpIpPortLogicalIfOspfIfNbrProvEntry = _MscVrPpIpPortLogicalIfOspfIfNbrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 3, 10, 1)
)
mscVrPpIpPortLogicalIfOspfIfNbrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfOspfIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfOspfIfNbrAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfNbrProvEntry.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfOspfIfNbrPriority_Type(Unsigned32):
    """Custom type mscVrPpIpPortLogicalIfOspfIfNbrPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrPpIpPortLogicalIfOspfIfNbrPriority_Type.__name__ = "Unsigned32"
_MscVrPpIpPortLogicalIfOspfIfNbrPriority_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfNbrPriority = _MscVrPpIpPortLogicalIfOspfIfNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 3, 10, 1, 1),
    _MscVrPpIpPortLogicalIfOspfIfNbrPriority_Type()
)
mscVrPpIpPortLogicalIfOspfIfNbrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfNbrPriority.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfNbrOperTable_Object = MibTable
mscVrPpIpPortLogicalIfOspfIfNbrOperTable = _MscVrPpIpPortLogicalIfOspfIfNbrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 3, 11)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfNbrOperTable.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfNbrOperEntry_Object = MibTableRow
mscVrPpIpPortLogicalIfOspfIfNbrOperEntry = _MscVrPpIpPortLogicalIfOspfIfNbrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 3, 11, 1)
)
mscVrPpIpPortLogicalIfOspfIfNbrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfOspfIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfOspfIfNbrAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfNbrOperEntry.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfNbrRtrId_Type = RouterID
_MscVrPpIpPortLogicalIfOspfIfNbrRtrId_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfNbrRtrId = _MscVrPpIpPortLogicalIfOspfIfNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 3, 11, 1, 1),
    _MscVrPpIpPortLogicalIfOspfIfNbrRtrId_Type()
)
mscVrPpIpPortLogicalIfOspfIfNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfNbrRtrId.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfOspfIfNbrOptions_Type(Unsigned32):
    """Custom type mscVrPpIpPortLogicalIfOspfIfNbrOptions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscVrPpIpPortLogicalIfOspfIfNbrOptions_Type.__name__ = "Unsigned32"
_MscVrPpIpPortLogicalIfOspfIfNbrOptions_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfNbrOptions = _MscVrPpIpPortLogicalIfOspfIfNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 3, 11, 1, 2),
    _MscVrPpIpPortLogicalIfOspfIfNbrOptions_Type()
)
mscVrPpIpPortLogicalIfOspfIfNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfNbrOptions.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfOspfIfNbrState_Type(Integer32):
    """Custom type mscVrPpIpPortLogicalIfOspfIfNbrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("attempt", 2),
          ("down", 1),
          ("exchange", 6),
          ("exchangeStart", 5),
          ("full", 8),
          ("init", 3),
          ("loading", 7),
          ("twoWay", 4))
    )


_MscVrPpIpPortLogicalIfOspfIfNbrState_Type.__name__ = "Integer32"
_MscVrPpIpPortLogicalIfOspfIfNbrState_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfNbrState = _MscVrPpIpPortLogicalIfOspfIfNbrState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 3, 11, 1, 3),
    _MscVrPpIpPortLogicalIfOspfIfNbrState_Type()
)
mscVrPpIpPortLogicalIfOspfIfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfNbrState.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfNbrEvents_Type = Counter32
_MscVrPpIpPortLogicalIfOspfIfNbrEvents_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfNbrEvents = _MscVrPpIpPortLogicalIfOspfIfNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 3, 11, 1, 4),
    _MscVrPpIpPortLogicalIfOspfIfNbrEvents_Type()
)
mscVrPpIpPortLogicalIfOspfIfNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfNbrEvents.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfOspfIfNbrLsRetransQlen_Type(Gauge32):
    """Custom type mscVrPpIpPortLogicalIfOspfIfNbrLsRetransQlen based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpIpPortLogicalIfOspfIfNbrLsRetransQlen_Type.__name__ = "Gauge32"
_MscVrPpIpPortLogicalIfOspfIfNbrLsRetransQlen_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfNbrLsRetransQlen = _MscVrPpIpPortLogicalIfOspfIfNbrLsRetransQlen_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 3, 11, 1, 5),
    _MscVrPpIpPortLogicalIfOspfIfNbrLsRetransQlen_Type()
)
mscVrPpIpPortLogicalIfOspfIfNbrLsRetransQlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfNbrLsRetransQlen.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfOspfIfNbrExchangeStatus_Type(Integer32):
    """Custom type mscVrPpIpPortLogicalIfOspfIfNbrExchangeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_MscVrPpIpPortLogicalIfOspfIfNbrExchangeStatus_Type.__name__ = "Integer32"
_MscVrPpIpPortLogicalIfOspfIfNbrExchangeStatus_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfNbrExchangeStatus = _MscVrPpIpPortLogicalIfOspfIfNbrExchangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 3, 11, 1, 6),
    _MscVrPpIpPortLogicalIfOspfIfNbrExchangeStatus_Type()
)
mscVrPpIpPortLogicalIfOspfIfNbrExchangeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfNbrExchangeStatus.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfOspfIfNbrPermanance_Type(Integer32):
    """Custom type mscVrPpIpPortLogicalIfOspfIfNbrPermanance based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("permanent", 1))
    )


_MscVrPpIpPortLogicalIfOspfIfNbrPermanance_Type.__name__ = "Integer32"
_MscVrPpIpPortLogicalIfOspfIfNbrPermanance_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfNbrPermanance = _MscVrPpIpPortLogicalIfOspfIfNbrPermanance_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 3, 11, 1, 9),
    _MscVrPpIpPortLogicalIfOspfIfNbrPermanance_Type()
)
mscVrPpIpPortLogicalIfOspfIfNbrPermanance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfNbrPermanance.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfProvTable_Object = MibTable
mscVrPpIpPortLogicalIfOspfIfProvTable = _MscVrPpIpPortLogicalIfOspfIfProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfProvTable.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfProvEntry_Object = MibTableRow
mscVrPpIpPortLogicalIfOspfIfProvEntry = _MscVrPpIpPortLogicalIfOspfIfProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 10, 1)
)
mscVrPpIpPortLogicalIfOspfIfProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfOspfIfIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfProvEntry.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfOspfIfAreaId_Type(AreaID):
    """Custom type mscVrPpIpPortLogicalIfOspfIfAreaId based on AreaID"""
    defaultHexValue = "00000000"


_MscVrPpIpPortLogicalIfOspfIfAreaId_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfAreaId = _MscVrPpIpPortLogicalIfOspfIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 10, 1, 1),
    _MscVrPpIpPortLogicalIfOspfIfAreaId_Type()
)
mscVrPpIpPortLogicalIfOspfIfAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfAreaId.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfOspfIfIfType_Type(Integer32):
    """Custom type mscVrPpIpPortLogicalIfOspfIfIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("nbma", 2),
          ("pointToPoint", 3))
    )


_MscVrPpIpPortLogicalIfOspfIfIfType_Type.__name__ = "Integer32"
_MscVrPpIpPortLogicalIfOspfIfIfType_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfIfType = _MscVrPpIpPortLogicalIfOspfIfIfType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 10, 1, 2),
    _MscVrPpIpPortLogicalIfOspfIfIfType_Type()
)
mscVrPpIpPortLogicalIfOspfIfIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfIfType.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfOspfIfSnmpAdminStatus_Type(Integer32):
    """Custom type mscVrPpIpPortLogicalIfOspfIfSnmpAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MscVrPpIpPortLogicalIfOspfIfSnmpAdminStatus_Type.__name__ = "Integer32"
_MscVrPpIpPortLogicalIfOspfIfSnmpAdminStatus_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfSnmpAdminStatus = _MscVrPpIpPortLogicalIfOspfIfSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 10, 1, 3),
    _MscVrPpIpPortLogicalIfOspfIfSnmpAdminStatus_Type()
)
mscVrPpIpPortLogicalIfOspfIfSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfSnmpAdminStatus.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfOspfIfRtrPriority_Type(Unsigned32):
    """Custom type mscVrPpIpPortLogicalIfOspfIfRtrPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrPpIpPortLogicalIfOspfIfRtrPriority_Type.__name__ = "Unsigned32"
_MscVrPpIpPortLogicalIfOspfIfRtrPriority_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfRtrPriority = _MscVrPpIpPortLogicalIfOspfIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 10, 1, 4),
    _MscVrPpIpPortLogicalIfOspfIfRtrPriority_Type()
)
mscVrPpIpPortLogicalIfOspfIfRtrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfRtrPriority.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfOspfIfTransitDelay_Type(Unsigned32):
    """Custom type mscVrPpIpPortLogicalIfOspfIfTransitDelay based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_MscVrPpIpPortLogicalIfOspfIfTransitDelay_Type.__name__ = "Unsigned32"
_MscVrPpIpPortLogicalIfOspfIfTransitDelay_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfTransitDelay = _MscVrPpIpPortLogicalIfOspfIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 10, 1, 5),
    _MscVrPpIpPortLogicalIfOspfIfTransitDelay_Type()
)
mscVrPpIpPortLogicalIfOspfIfTransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfTransitDelay.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfOspfIfRetransInterval_Type(Unsigned32):
    """Custom type mscVrPpIpPortLogicalIfOspfIfRetransInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_MscVrPpIpPortLogicalIfOspfIfRetransInterval_Type.__name__ = "Unsigned32"
_MscVrPpIpPortLogicalIfOspfIfRetransInterval_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfRetransInterval = _MscVrPpIpPortLogicalIfOspfIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 10, 1, 6),
    _MscVrPpIpPortLogicalIfOspfIfRetransInterval_Type()
)
mscVrPpIpPortLogicalIfOspfIfRetransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfRetransInterval.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfOspfIfHelloInterval_Type(Unsigned32):
    """Custom type mscVrPpIpPortLogicalIfOspfIfHelloInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_MscVrPpIpPortLogicalIfOspfIfHelloInterval_Type.__name__ = "Unsigned32"
_MscVrPpIpPortLogicalIfOspfIfHelloInterval_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfHelloInterval = _MscVrPpIpPortLogicalIfOspfIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 10, 1, 7),
    _MscVrPpIpPortLogicalIfOspfIfHelloInterval_Type()
)
mscVrPpIpPortLogicalIfOspfIfHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfHelloInterval.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfOspfIfRtrDeadInterval_Type(Unsigned32):
    """Custom type mscVrPpIpPortLogicalIfOspfIfRtrDeadInterval based on Unsigned32"""
    defaultValue = 40

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_MscVrPpIpPortLogicalIfOspfIfRtrDeadInterval_Type.__name__ = "Unsigned32"
_MscVrPpIpPortLogicalIfOspfIfRtrDeadInterval_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfRtrDeadInterval = _MscVrPpIpPortLogicalIfOspfIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 10, 1, 8),
    _MscVrPpIpPortLogicalIfOspfIfRtrDeadInterval_Type()
)
mscVrPpIpPortLogicalIfOspfIfRtrDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfRtrDeadInterval.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfOspfIfPollInterval_Type(Unsigned32):
    """Custom type mscVrPpIpPortLogicalIfOspfIfPollInterval based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_MscVrPpIpPortLogicalIfOspfIfPollInterval_Type.__name__ = "Unsigned32"
_MscVrPpIpPortLogicalIfOspfIfPollInterval_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfPollInterval = _MscVrPpIpPortLogicalIfOspfIfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 10, 1, 9),
    _MscVrPpIpPortLogicalIfOspfIfPollInterval_Type()
)
mscVrPpIpPortLogicalIfOspfIfPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfPollInterval.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfOspfIfAuthKey_Type(HexString):
    """Custom type mscVrPpIpPortLogicalIfOspfIfAuthKey based on HexString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscVrPpIpPortLogicalIfOspfIfAuthKey_Type.__name__ = "HexString"
_MscVrPpIpPortLogicalIfOspfIfAuthKey_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfAuthKey = _MscVrPpIpPortLogicalIfOspfIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 10, 1, 10),
    _MscVrPpIpPortLogicalIfOspfIfAuthKey_Type()
)
mscVrPpIpPortLogicalIfOspfIfAuthKey.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfAuthKey.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfOspfIfMulticastForwarding_Type(Integer32):
    """Custom type mscVrPpIpPortLogicalIfOspfIfMulticastForwarding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("blocked", 1)
    )


_MscVrPpIpPortLogicalIfOspfIfMulticastForwarding_Type.__name__ = "Integer32"
_MscVrPpIpPortLogicalIfOspfIfMulticastForwarding_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfMulticastForwarding = _MscVrPpIpPortLogicalIfOspfIfMulticastForwarding_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 10, 1, 12),
    _MscVrPpIpPortLogicalIfOspfIfMulticastForwarding_Type()
)
mscVrPpIpPortLogicalIfOspfIfMulticastForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfMulticastForwarding.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfOperTable_Object = MibTable
mscVrPpIpPortLogicalIfOspfIfOperTable = _MscVrPpIpPortLogicalIfOspfIfOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 11)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfOperTable.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfOperEntry_Object = MibTableRow
mscVrPpIpPortLogicalIfOspfIfOperEntry = _MscVrPpIpPortLogicalIfOspfIfOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 11, 1)
)
mscVrPpIpPortLogicalIfOspfIfOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfOspfIfIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfOperEntry.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfOspfIfState_Type(Integer32):
    """Custom type mscVrPpIpPortLogicalIfOspfIfState based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("backupDesignatedRouter", 6),
          ("designatedRouter", 5),
          ("down", 1),
          ("loopback", 2),
          ("otherDesignatedRouter", 7),
          ("pointToPoint", 4),
          ("waiting", 3))
    )


_MscVrPpIpPortLogicalIfOspfIfState_Type.__name__ = "Integer32"
_MscVrPpIpPortLogicalIfOspfIfState_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfState = _MscVrPpIpPortLogicalIfOspfIfState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 11, 1, 1),
    _MscVrPpIpPortLogicalIfOspfIfState_Type()
)
mscVrPpIpPortLogicalIfOspfIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfState.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfDesignatedRouter_Type = IpAddress
_MscVrPpIpPortLogicalIfOspfIfDesignatedRouter_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfDesignatedRouter = _MscVrPpIpPortLogicalIfOspfIfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 11, 1, 2),
    _MscVrPpIpPortLogicalIfOspfIfDesignatedRouter_Type()
)
mscVrPpIpPortLogicalIfOspfIfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfDesignatedRouter.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfBackupDesignatedRouter_Type = IpAddress
_MscVrPpIpPortLogicalIfOspfIfBackupDesignatedRouter_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfBackupDesignatedRouter = _MscVrPpIpPortLogicalIfOspfIfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 11, 1, 3),
    _MscVrPpIpPortLogicalIfOspfIfBackupDesignatedRouter_Type()
)
mscVrPpIpPortLogicalIfOspfIfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfBackupDesignatedRouter.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfEvents_Type = Counter32
_MscVrPpIpPortLogicalIfOspfIfEvents_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfEvents = _MscVrPpIpPortLogicalIfOspfIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 11, 1, 4),
    _MscVrPpIpPortLogicalIfOspfIfEvents_Type()
)
mscVrPpIpPortLogicalIfOspfIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfEvents.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfMetricTable_Object = MibTable
mscVrPpIpPortLogicalIfOspfIfMetricTable = _MscVrPpIpPortLogicalIfOspfIfMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 12)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfMetricTable.setStatus("mandatory")
_MscVrPpIpPortLogicalIfOspfIfMetricEntry_Object = MibTableRow
mscVrPpIpPortLogicalIfOspfIfMetricEntry = _MscVrPpIpPortLogicalIfOspfIfMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 12, 1)
)
mscVrPpIpPortLogicalIfOspfIfMetricEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfOspfIfIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfMetricEntry.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfOspfIfMetric_Type(Unsigned32):
    """Custom type mscVrPpIpPortLogicalIfOspfIfMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpIpPortLogicalIfOspfIfMetric_Type.__name__ = "Unsigned32"
_MscVrPpIpPortLogicalIfOspfIfMetric_Object = MibTableColumn
mscVrPpIpPortLogicalIfOspfIfMetric = _MscVrPpIpPortLogicalIfOspfIfMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 2, 12, 1, 1),
    _MscVrPpIpPortLogicalIfOspfIfMetric_Type()
)
mscVrPpIpPortLogicalIfOspfIfMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfOspfIfMetric.setStatus("mandatory")
_MscVrPpIpPortLogicalIfRipIf_ObjectIdentity = ObjectIdentity
mscVrPpIpPortLogicalIfRipIf = _MscVrPpIpPortLogicalIfRipIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3)
)
_MscVrPpIpPortLogicalIfRipIfRowStatusTable_Object = MibTable
mscVrPpIpPortLogicalIfRipIfRowStatusTable = _MscVrPpIpPortLogicalIfRipIfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfRowStatusTable.setStatus("mandatory")
_MscVrPpIpPortLogicalIfRipIfRowStatusEntry_Object = MibTableRow
mscVrPpIpPortLogicalIfRipIfRowStatusEntry = _MscVrPpIpPortLogicalIfRipIfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 1, 1)
)
mscVrPpIpPortLogicalIfRipIfRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfRipIfIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfRowStatusEntry.setStatus("mandatory")
_MscVrPpIpPortLogicalIfRipIfRowStatus_Type = RowStatus
_MscVrPpIpPortLogicalIfRipIfRowStatus_Object = MibTableColumn
mscVrPpIpPortLogicalIfRipIfRowStatus = _MscVrPpIpPortLogicalIfRipIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 1, 1, 1),
    _MscVrPpIpPortLogicalIfRipIfRowStatus_Type()
)
mscVrPpIpPortLogicalIfRipIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfRowStatus.setStatus("mandatory")
_MscVrPpIpPortLogicalIfRipIfComponentName_Type = DisplayString
_MscVrPpIpPortLogicalIfRipIfComponentName_Object = MibTableColumn
mscVrPpIpPortLogicalIfRipIfComponentName = _MscVrPpIpPortLogicalIfRipIfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 1, 1, 2),
    _MscVrPpIpPortLogicalIfRipIfComponentName_Type()
)
mscVrPpIpPortLogicalIfRipIfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfComponentName.setStatus("mandatory")
_MscVrPpIpPortLogicalIfRipIfStorageType_Type = StorageType
_MscVrPpIpPortLogicalIfRipIfStorageType_Object = MibTableColumn
mscVrPpIpPortLogicalIfRipIfStorageType = _MscVrPpIpPortLogicalIfRipIfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 1, 1, 4),
    _MscVrPpIpPortLogicalIfRipIfStorageType_Type()
)
mscVrPpIpPortLogicalIfRipIfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfStorageType.setStatus("mandatory")
_MscVrPpIpPortLogicalIfRipIfIndex_Type = NonReplicated
_MscVrPpIpPortLogicalIfRipIfIndex_Object = MibTableColumn
mscVrPpIpPortLogicalIfRipIfIndex = _MscVrPpIpPortLogicalIfRipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 1, 1, 10),
    _MscVrPpIpPortLogicalIfRipIfIndex_Type()
)
mscVrPpIpPortLogicalIfRipIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfIndex.setStatus("mandatory")
_MscVrPpIpPortLogicalIfRipIfNbr_ObjectIdentity = ObjectIdentity
mscVrPpIpPortLogicalIfRipIfNbr = _MscVrPpIpPortLogicalIfRipIfNbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 2)
)
_MscVrPpIpPortLogicalIfRipIfNbrRowStatusTable_Object = MibTable
mscVrPpIpPortLogicalIfRipIfNbrRowStatusTable = _MscVrPpIpPortLogicalIfRipIfNbrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfNbrRowStatusTable.setStatus("mandatory")
_MscVrPpIpPortLogicalIfRipIfNbrRowStatusEntry_Object = MibTableRow
mscVrPpIpPortLogicalIfRipIfNbrRowStatusEntry = _MscVrPpIpPortLogicalIfRipIfNbrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 2, 1, 1)
)
mscVrPpIpPortLogicalIfRipIfNbrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfRipIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfRipIfNbrIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfNbrRowStatusEntry.setStatus("mandatory")
_MscVrPpIpPortLogicalIfRipIfNbrRowStatus_Type = RowStatus
_MscVrPpIpPortLogicalIfRipIfNbrRowStatus_Object = MibTableColumn
mscVrPpIpPortLogicalIfRipIfNbrRowStatus = _MscVrPpIpPortLogicalIfRipIfNbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 2, 1, 1, 1),
    _MscVrPpIpPortLogicalIfRipIfNbrRowStatus_Type()
)
mscVrPpIpPortLogicalIfRipIfNbrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfNbrRowStatus.setStatus("mandatory")
_MscVrPpIpPortLogicalIfRipIfNbrComponentName_Type = DisplayString
_MscVrPpIpPortLogicalIfRipIfNbrComponentName_Object = MibTableColumn
mscVrPpIpPortLogicalIfRipIfNbrComponentName = _MscVrPpIpPortLogicalIfRipIfNbrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 2, 1, 1, 2),
    _MscVrPpIpPortLogicalIfRipIfNbrComponentName_Type()
)
mscVrPpIpPortLogicalIfRipIfNbrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfNbrComponentName.setStatus("mandatory")
_MscVrPpIpPortLogicalIfRipIfNbrStorageType_Type = StorageType
_MscVrPpIpPortLogicalIfRipIfNbrStorageType_Object = MibTableColumn
mscVrPpIpPortLogicalIfRipIfNbrStorageType = _MscVrPpIpPortLogicalIfRipIfNbrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 2, 1, 1, 4),
    _MscVrPpIpPortLogicalIfRipIfNbrStorageType_Type()
)
mscVrPpIpPortLogicalIfRipIfNbrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfNbrStorageType.setStatus("mandatory")
_MscVrPpIpPortLogicalIfRipIfNbrIndex_Type = IpAddress
_MscVrPpIpPortLogicalIfRipIfNbrIndex_Object = MibTableColumn
mscVrPpIpPortLogicalIfRipIfNbrIndex = _MscVrPpIpPortLogicalIfRipIfNbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 2, 1, 1, 10),
    _MscVrPpIpPortLogicalIfRipIfNbrIndex_Type()
)
mscVrPpIpPortLogicalIfRipIfNbrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfNbrIndex.setStatus("mandatory")
_MscVrPpIpPortLogicalIfRipIfProvTable_Object = MibTable
mscVrPpIpPortLogicalIfRipIfProvTable = _MscVrPpIpPortLogicalIfRipIfProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 10)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfProvTable.setStatus("mandatory")
_MscVrPpIpPortLogicalIfRipIfProvEntry_Object = MibTableRow
mscVrPpIpPortLogicalIfRipIfProvEntry = _MscVrPpIpPortLogicalIfRipIfProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 10, 1)
)
mscVrPpIpPortLogicalIfRipIfProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfRipIfIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfProvEntry.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfRipIfSnmpAdminStatus_Type(Integer32):
    """Custom type mscVrPpIpPortLogicalIfRipIfSnmpAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MscVrPpIpPortLogicalIfRipIfSnmpAdminStatus_Type.__name__ = "Integer32"
_MscVrPpIpPortLogicalIfRipIfSnmpAdminStatus_Object = MibTableColumn
mscVrPpIpPortLogicalIfRipIfSnmpAdminStatus = _MscVrPpIpPortLogicalIfRipIfSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 10, 1, 1),
    _MscVrPpIpPortLogicalIfRipIfSnmpAdminStatus_Type()
)
mscVrPpIpPortLogicalIfRipIfSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfSnmpAdminStatus.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfRipIfMetric_Type(Unsigned32):
    """Custom type mscVrPpIpPortLogicalIfRipIfMetric based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscVrPpIpPortLogicalIfRipIfMetric_Type.__name__ = "Unsigned32"
_MscVrPpIpPortLogicalIfRipIfMetric_Object = MibTableColumn
mscVrPpIpPortLogicalIfRipIfMetric = _MscVrPpIpPortLogicalIfRipIfMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 10, 1, 2),
    _MscVrPpIpPortLogicalIfRipIfMetric_Type()
)
mscVrPpIpPortLogicalIfRipIfMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfMetric.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfRipIfSilentFlag_Type(Integer32):
    """Custom type mscVrPpIpPortLogicalIfRipIfSilentFlag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_MscVrPpIpPortLogicalIfRipIfSilentFlag_Type.__name__ = "Integer32"
_MscVrPpIpPortLogicalIfRipIfSilentFlag_Object = MibTableColumn
mscVrPpIpPortLogicalIfRipIfSilentFlag = _MscVrPpIpPortLogicalIfRipIfSilentFlag_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 10, 1, 3),
    _MscVrPpIpPortLogicalIfRipIfSilentFlag_Type()
)
mscVrPpIpPortLogicalIfRipIfSilentFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfSilentFlag.setStatus("obsolete")


class _MscVrPpIpPortLogicalIfRipIfPoisonReverseFlag_Type(Integer32):
    """Custom type mscVrPpIpPortLogicalIfRipIfPoisonReverseFlag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_MscVrPpIpPortLogicalIfRipIfPoisonReverseFlag_Type.__name__ = "Integer32"
_MscVrPpIpPortLogicalIfRipIfPoisonReverseFlag_Object = MibTableColumn
mscVrPpIpPortLogicalIfRipIfPoisonReverseFlag = _MscVrPpIpPortLogicalIfRipIfPoisonReverseFlag_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 10, 1, 4),
    _MscVrPpIpPortLogicalIfRipIfPoisonReverseFlag_Type()
)
mscVrPpIpPortLogicalIfRipIfPoisonReverseFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfPoisonReverseFlag.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfRipIfFlashUpdateFlag_Type(Integer32):
    """Custom type mscVrPpIpPortLogicalIfRipIfFlashUpdateFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_MscVrPpIpPortLogicalIfRipIfFlashUpdateFlag_Type.__name__ = "Integer32"
_MscVrPpIpPortLogicalIfRipIfFlashUpdateFlag_Object = MibTableColumn
mscVrPpIpPortLogicalIfRipIfFlashUpdateFlag = _MscVrPpIpPortLogicalIfRipIfFlashUpdateFlag_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 10, 1, 5),
    _MscVrPpIpPortLogicalIfRipIfFlashUpdateFlag_Type()
)
mscVrPpIpPortLogicalIfRipIfFlashUpdateFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfFlashUpdateFlag.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfRipIfNetworkRouteStatus_Type(Integer32):
    """Custom type mscVrPpIpPortLogicalIfRipIfNetworkRouteStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("defaultRouteOnly", 3),
          ("naturalNetWithDefaultRoute", 2),
          ("naturalNetWithOutDefaultRoute", 1),
          ("subnetsOnly", 4))
    )


_MscVrPpIpPortLogicalIfRipIfNetworkRouteStatus_Type.__name__ = "Integer32"
_MscVrPpIpPortLogicalIfRipIfNetworkRouteStatus_Object = MibTableColumn
mscVrPpIpPortLogicalIfRipIfNetworkRouteStatus = _MscVrPpIpPortLogicalIfRipIfNetworkRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 10, 1, 6),
    _MscVrPpIpPortLogicalIfRipIfNetworkRouteStatus_Type()
)
mscVrPpIpPortLogicalIfRipIfNetworkRouteStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfNetworkRouteStatus.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfRipIfDefaultRouteMetric_Type(Unsigned32):
    """Custom type mscVrPpIpPortLogicalIfRipIfDefaultRouteMetric based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscVrPpIpPortLogicalIfRipIfDefaultRouteMetric_Type.__name__ = "Unsigned32"
_MscVrPpIpPortLogicalIfRipIfDefaultRouteMetric_Object = MibTableColumn
mscVrPpIpPortLogicalIfRipIfDefaultRouteMetric = _MscVrPpIpPortLogicalIfRipIfDefaultRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 10, 1, 7),
    _MscVrPpIpPortLogicalIfRipIfDefaultRouteMetric_Type()
)
mscVrPpIpPortLogicalIfRipIfDefaultRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfDefaultRouteMetric.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfRipIfAcceptDefault_Type(Integer32):
    """Custom type mscVrPpIpPortLogicalIfRipIfAcceptDefault based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_MscVrPpIpPortLogicalIfRipIfAcceptDefault_Type.__name__ = "Integer32"
_MscVrPpIpPortLogicalIfRipIfAcceptDefault_Object = MibTableColumn
mscVrPpIpPortLogicalIfRipIfAcceptDefault = _MscVrPpIpPortLogicalIfRipIfAcceptDefault_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 10, 1, 8),
    _MscVrPpIpPortLogicalIfRipIfAcceptDefault_Type()
)
mscVrPpIpPortLogicalIfRipIfAcceptDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfAcceptDefault.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfRipIfIfConfSend_Type(Integer32):
    """Custom type mscVrPpIpPortLogicalIfRipIfIfConfSend based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("doNotSend", 1),
          ("rip1Compatible", 3),
          ("ripVersion1", 2),
          ("ripVersion2", 4))
    )


_MscVrPpIpPortLogicalIfRipIfIfConfSend_Type.__name__ = "Integer32"
_MscVrPpIpPortLogicalIfRipIfIfConfSend_Object = MibTableColumn
mscVrPpIpPortLogicalIfRipIfIfConfSend = _MscVrPpIpPortLogicalIfRipIfIfConfSend_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 10, 1, 12),
    _MscVrPpIpPortLogicalIfRipIfIfConfSend_Type()
)
mscVrPpIpPortLogicalIfRipIfIfConfSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfIfConfSend.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfRipIfIfConfReceive_Type(Integer32):
    """Custom type mscVrPpIpPortLogicalIfRipIfIfConfReceive based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("doNotReceive", 4),
          ("rip1", 1),
          ("rip1OrRip2", 3),
          ("rip2", 2))
    )


_MscVrPpIpPortLogicalIfRipIfIfConfReceive_Type.__name__ = "Integer32"
_MscVrPpIpPortLogicalIfRipIfIfConfReceive_Object = MibTableColumn
mscVrPpIpPortLogicalIfRipIfIfConfReceive = _MscVrPpIpPortLogicalIfRipIfIfConfReceive_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 10, 1, 13),
    _MscVrPpIpPortLogicalIfRipIfIfConfReceive_Type()
)
mscVrPpIpPortLogicalIfRipIfIfConfReceive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfIfConfReceive.setStatus("mandatory")
_MscVrPpIpPortLogicalIfRipIfStatTable_Object = MibTable
mscVrPpIpPortLogicalIfRipIfStatTable = _MscVrPpIpPortLogicalIfRipIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 11)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfStatTable.setStatus("mandatory")
_MscVrPpIpPortLogicalIfRipIfStatEntry_Object = MibTableRow
mscVrPpIpPortLogicalIfRipIfStatEntry = _MscVrPpIpPortLogicalIfRipIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 11, 1)
)
mscVrPpIpPortLogicalIfRipIfStatEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfRipIfIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfStatEntry.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfRipIfIfBadPacketRcv_Type(Unsigned32):
    """Custom type mscVrPpIpPortLogicalIfRipIfIfBadPacketRcv based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpIpPortLogicalIfRipIfIfBadPacketRcv_Type.__name__ = "Unsigned32"
_MscVrPpIpPortLogicalIfRipIfIfBadPacketRcv_Object = MibTableColumn
mscVrPpIpPortLogicalIfRipIfIfBadPacketRcv = _MscVrPpIpPortLogicalIfRipIfIfBadPacketRcv_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 11, 1, 1),
    _MscVrPpIpPortLogicalIfRipIfIfBadPacketRcv_Type()
)
mscVrPpIpPortLogicalIfRipIfIfBadPacketRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfIfBadPacketRcv.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfRipIfIfBadRouteRcv_Type(Unsigned32):
    """Custom type mscVrPpIpPortLogicalIfRipIfIfBadRouteRcv based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpIpPortLogicalIfRipIfIfBadRouteRcv_Type.__name__ = "Unsigned32"
_MscVrPpIpPortLogicalIfRipIfIfBadRouteRcv_Object = MibTableColumn
mscVrPpIpPortLogicalIfRipIfIfBadRouteRcv = _MscVrPpIpPortLogicalIfRipIfIfBadRouteRcv_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 11, 1, 2),
    _MscVrPpIpPortLogicalIfRipIfIfBadRouteRcv_Type()
)
mscVrPpIpPortLogicalIfRipIfIfBadRouteRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfIfBadRouteRcv.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfRipIfIfTriggeredUpdates_Type(Unsigned32):
    """Custom type mscVrPpIpPortLogicalIfRipIfIfTriggeredUpdates based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrPpIpPortLogicalIfRipIfIfTriggeredUpdates_Type.__name__ = "Unsigned32"
_MscVrPpIpPortLogicalIfRipIfIfTriggeredUpdates_Object = MibTableColumn
mscVrPpIpPortLogicalIfRipIfIfTriggeredUpdates = _MscVrPpIpPortLogicalIfRipIfIfTriggeredUpdates_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 3, 11, 1, 3),
    _MscVrPpIpPortLogicalIfRipIfIfTriggeredUpdates_Type()
)
mscVrPpIpPortLogicalIfRipIfIfTriggeredUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfRipIfIfTriggeredUpdates.setStatus("mandatory")
_MscVrPpIpPortLogicalIfProvTable_Object = MibTable
mscVrPpIpPortLogicalIfProvTable = _MscVrPpIpPortLogicalIfProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfProvTable.setStatus("mandatory")
_MscVrPpIpPortLogicalIfProvEntry_Object = MibTableRow
mscVrPpIpPortLogicalIfProvEntry = _MscVrPpIpPortLogicalIfProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 10, 1)
)
mscVrPpIpPortLogicalIfProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfProvEntry.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfNetMask_Type(IpAddress):
    """Custom type mscVrPpIpPortLogicalIfNetMask based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrPpIpPortLogicalIfNetMask_Object = MibTableColumn
mscVrPpIpPortLogicalIfNetMask = _MscVrPpIpPortLogicalIfNetMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 10, 1, 1),
    _MscVrPpIpPortLogicalIfNetMask_Type()
)
mscVrPpIpPortLogicalIfNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfNetMask.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfBroadcastAddress_Type(IpAddress):
    """Custom type mscVrPpIpPortLogicalIfBroadcastAddress based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrPpIpPortLogicalIfBroadcastAddress_Object = MibTableColumn
mscVrPpIpPortLogicalIfBroadcastAddress = _MscVrPpIpPortLogicalIfBroadcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 10, 1, 2),
    _MscVrPpIpPortLogicalIfBroadcastAddress_Type()
)
mscVrPpIpPortLogicalIfBroadcastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfBroadcastAddress.setStatus("mandatory")


class _MscVrPpIpPortLogicalIfLinkDestinationAddress_Type(IpAddress):
    """Custom type mscVrPpIpPortLogicalIfLinkDestinationAddress based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrPpIpPortLogicalIfLinkDestinationAddress_Object = MibTableColumn
mscVrPpIpPortLogicalIfLinkDestinationAddress = _MscVrPpIpPortLogicalIfLinkDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 10, 1, 3),
    _MscVrPpIpPortLogicalIfLinkDestinationAddress_Type()
)
mscVrPpIpPortLogicalIfLinkDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfLinkDestinationAddress.setStatus("mandatory")
_MscVrPpIpPortNs_ObjectIdentity = ObjectIdentity
mscVrPpIpPortNs = _MscVrPpIpPortNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 3)
)
_MscVrPpIpPortNsRowStatusTable_Object = MibTable
mscVrPpIpPortNsRowStatusTable = _MscVrPpIpPortNsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 3, 1)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortNsRowStatusTable.setStatus("mandatory")
_MscVrPpIpPortNsRowStatusEntry_Object = MibTableRow
mscVrPpIpPortNsRowStatusEntry = _MscVrPpIpPortNsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 3, 1, 1)
)
mscVrPpIpPortNsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortNsIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortNsRowStatusEntry.setStatus("mandatory")
_MscVrPpIpPortNsRowStatus_Type = RowStatus
_MscVrPpIpPortNsRowStatus_Object = MibTableColumn
mscVrPpIpPortNsRowStatus = _MscVrPpIpPortNsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 3, 1, 1, 1),
    _MscVrPpIpPortNsRowStatus_Type()
)
mscVrPpIpPortNsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortNsRowStatus.setStatus("mandatory")
_MscVrPpIpPortNsComponentName_Type = DisplayString
_MscVrPpIpPortNsComponentName_Object = MibTableColumn
mscVrPpIpPortNsComponentName = _MscVrPpIpPortNsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 3, 1, 1, 2),
    _MscVrPpIpPortNsComponentName_Type()
)
mscVrPpIpPortNsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortNsComponentName.setStatus("mandatory")
_MscVrPpIpPortNsStorageType_Type = StorageType
_MscVrPpIpPortNsStorageType_Object = MibTableColumn
mscVrPpIpPortNsStorageType = _MscVrPpIpPortNsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 3, 1, 1, 4),
    _MscVrPpIpPortNsStorageType_Type()
)
mscVrPpIpPortNsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortNsStorageType.setStatus("mandatory")
_MscVrPpIpPortNsIndex_Type = NonReplicated
_MscVrPpIpPortNsIndex_Object = MibTableColumn
mscVrPpIpPortNsIndex = _MscVrPpIpPortNsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 3, 1, 1, 10),
    _MscVrPpIpPortNsIndex_Type()
)
mscVrPpIpPortNsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpIpPortNsIndex.setStatus("mandatory")
_MscVrPpIpPortNsProvTable_Object = MibTable
mscVrPpIpPortNsProvTable = _MscVrPpIpPortNsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 3, 10)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortNsProvTable.setStatus("mandatory")
_MscVrPpIpPortNsProvEntry_Object = MibTableRow
mscVrPpIpPortNsProvEntry = _MscVrPpIpPortNsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 3, 10, 1)
)
mscVrPpIpPortNsProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortNsIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortNsProvEntry.setStatus("mandatory")


class _MscVrPpIpPortNsIncomingFilter_Type(AsciiString):
    """Custom type mscVrPpIpPortNsIncomingFilter based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrPpIpPortNsIncomingFilter_Type.__name__ = "AsciiString"
_MscVrPpIpPortNsIncomingFilter_Object = MibTableColumn
mscVrPpIpPortNsIncomingFilter = _MscVrPpIpPortNsIncomingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 3, 10, 1, 1),
    _MscVrPpIpPortNsIncomingFilter_Type()
)
mscVrPpIpPortNsIncomingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortNsIncomingFilter.setStatus("mandatory")


class _MscVrPpIpPortNsOutgoingFilter_Type(AsciiString):
    """Custom type mscVrPpIpPortNsOutgoingFilter based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrPpIpPortNsOutgoingFilter_Type.__name__ = "AsciiString"
_MscVrPpIpPortNsOutgoingFilter_Object = MibTableColumn
mscVrPpIpPortNsOutgoingFilter = _MscVrPpIpPortNsOutgoingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 3, 10, 1, 2),
    _MscVrPpIpPortNsOutgoingFilter_Type()
)
mscVrPpIpPortNsOutgoingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortNsOutgoingFilter.setStatus("mandatory")
_MscVrPpIpPortBootpP_ObjectIdentity = ObjectIdentity
mscVrPpIpPortBootpP = _MscVrPpIpPortBootpP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4)
)
_MscVrPpIpPortBootpPRowStatusTable_Object = MibTable
mscVrPpIpPortBootpPRowStatusTable = _MscVrPpIpPortBootpPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 1)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPRowStatusTable.setStatus("mandatory")
_MscVrPpIpPortBootpPRowStatusEntry_Object = MibTableRow
mscVrPpIpPortBootpPRowStatusEntry = _MscVrPpIpPortBootpPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 1, 1)
)
mscVrPpIpPortBootpPRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortBootpPIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPRowStatusEntry.setStatus("mandatory")
_MscVrPpIpPortBootpPRowStatus_Type = RowStatus
_MscVrPpIpPortBootpPRowStatus_Object = MibTableColumn
mscVrPpIpPortBootpPRowStatus = _MscVrPpIpPortBootpPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 1, 1, 1),
    _MscVrPpIpPortBootpPRowStatus_Type()
)
mscVrPpIpPortBootpPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPRowStatus.setStatus("mandatory")
_MscVrPpIpPortBootpPComponentName_Type = DisplayString
_MscVrPpIpPortBootpPComponentName_Object = MibTableColumn
mscVrPpIpPortBootpPComponentName = _MscVrPpIpPortBootpPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 1, 1, 2),
    _MscVrPpIpPortBootpPComponentName_Type()
)
mscVrPpIpPortBootpPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPComponentName.setStatus("mandatory")
_MscVrPpIpPortBootpPStorageType_Type = StorageType
_MscVrPpIpPortBootpPStorageType_Object = MibTableColumn
mscVrPpIpPortBootpPStorageType = _MscVrPpIpPortBootpPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 1, 1, 4),
    _MscVrPpIpPortBootpPStorageType_Type()
)
mscVrPpIpPortBootpPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPStorageType.setStatus("mandatory")
_MscVrPpIpPortBootpPIndex_Type = NonReplicated
_MscVrPpIpPortBootpPIndex_Object = MibTableColumn
mscVrPpIpPortBootpPIndex = _MscVrPpIpPortBootpPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 1, 1, 10),
    _MscVrPpIpPortBootpPIndex_Type()
)
mscVrPpIpPortBootpPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPIndex.setStatus("mandatory")
_MscVrPpIpPortBootpPProvTable_Object = MibTable
mscVrPpIpPortBootpPProvTable = _MscVrPpIpPortBootpPProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 10)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPProvTable.setStatus("mandatory")
_MscVrPpIpPortBootpPProvEntry_Object = MibTableRow
mscVrPpIpPortBootpPProvEntry = _MscVrPpIpPortBootpPProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 10, 1)
)
mscVrPpIpPortBootpPProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortBootpPIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPProvEntry.setStatus("mandatory")


class _MscVrPpIpPortBootpPRelayForwardStatus_Type(Integer32):
    """Custom type mscVrPpIpPortBootpPRelayForwardStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_MscVrPpIpPortBootpPRelayForwardStatus_Type.__name__ = "Integer32"
_MscVrPpIpPortBootpPRelayForwardStatus_Object = MibTableColumn
mscVrPpIpPortBootpPRelayForwardStatus = _MscVrPpIpPortBootpPRelayForwardStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 10, 1, 2),
    _MscVrPpIpPortBootpPRelayForwardStatus_Type()
)
mscVrPpIpPortBootpPRelayForwardStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPRelayForwardStatus.setStatus("mandatory")


class _MscVrPpIpPortBootpPBootpLogicalInterface_Type(IpAddress):
    """Custom type mscVrPpIpPortBootpPBootpLogicalInterface based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrPpIpPortBootpPBootpLogicalInterface_Object = MibTableColumn
mscVrPpIpPortBootpPBootpLogicalInterface = _MscVrPpIpPortBootpPBootpLogicalInterface_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 10, 1, 3),
    _MscVrPpIpPortBootpPBootpLogicalInterface_Type()
)
mscVrPpIpPortBootpPBootpLogicalInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPBootpLogicalInterface.setStatus("mandatory")
_MscVrPpIpPortBootpPAdminControlTable_Object = MibTable
mscVrPpIpPortBootpPAdminControlTable = _MscVrPpIpPortBootpPAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 11)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPAdminControlTable.setStatus("mandatory")
_MscVrPpIpPortBootpPAdminControlEntry_Object = MibTableRow
mscVrPpIpPortBootpPAdminControlEntry = _MscVrPpIpPortBootpPAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 11, 1)
)
mscVrPpIpPortBootpPAdminControlEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortBootpPIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPAdminControlEntry.setStatus("mandatory")


class _MscVrPpIpPortBootpPSnmpAdminStatus_Type(Integer32):
    """Custom type mscVrPpIpPortBootpPSnmpAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscVrPpIpPortBootpPSnmpAdminStatus_Type.__name__ = "Integer32"
_MscVrPpIpPortBootpPSnmpAdminStatus_Object = MibTableColumn
mscVrPpIpPortBootpPSnmpAdminStatus = _MscVrPpIpPortBootpPSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 11, 1, 1),
    _MscVrPpIpPortBootpPSnmpAdminStatus_Type()
)
mscVrPpIpPortBootpPSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPSnmpAdminStatus.setStatus("mandatory")
_MscVrPpIpPortBootpPOperStatusTable_Object = MibTable
mscVrPpIpPortBootpPOperStatusTable = _MscVrPpIpPortBootpPOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 12)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPOperStatusTable.setStatus("mandatory")
_MscVrPpIpPortBootpPOperStatusEntry_Object = MibTableRow
mscVrPpIpPortBootpPOperStatusEntry = _MscVrPpIpPortBootpPOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 12, 1)
)
mscVrPpIpPortBootpPOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortBootpPIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPOperStatusEntry.setStatus("mandatory")


class _MscVrPpIpPortBootpPSnmpOperStatus_Type(Integer32):
    """Custom type mscVrPpIpPortBootpPSnmpOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscVrPpIpPortBootpPSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrPpIpPortBootpPSnmpOperStatus_Object = MibTableColumn
mscVrPpIpPortBootpPSnmpOperStatus = _MscVrPpIpPortBootpPSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 12, 1, 1),
    _MscVrPpIpPortBootpPSnmpOperStatus_Type()
)
mscVrPpIpPortBootpPSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPSnmpOperStatus.setStatus("mandatory")
_MscVrPpIpPortBootpPStateTable_Object = MibTable
mscVrPpIpPortBootpPStateTable = _MscVrPpIpPortBootpPStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 13)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPStateTable.setStatus("mandatory")
_MscVrPpIpPortBootpPStateEntry_Object = MibTableRow
mscVrPpIpPortBootpPStateEntry = _MscVrPpIpPortBootpPStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 13, 1)
)
mscVrPpIpPortBootpPStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortBootpPIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPStateEntry.setStatus("mandatory")


class _MscVrPpIpPortBootpPAdminState_Type(Integer32):
    """Custom type mscVrPpIpPortBootpPAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_MscVrPpIpPortBootpPAdminState_Type.__name__ = "Integer32"
_MscVrPpIpPortBootpPAdminState_Object = MibTableColumn
mscVrPpIpPortBootpPAdminState = _MscVrPpIpPortBootpPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 13, 1, 1),
    _MscVrPpIpPortBootpPAdminState_Type()
)
mscVrPpIpPortBootpPAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPAdminState.setStatus("mandatory")


class _MscVrPpIpPortBootpPOperationalState_Type(Integer32):
    """Custom type mscVrPpIpPortBootpPOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MscVrPpIpPortBootpPOperationalState_Type.__name__ = "Integer32"
_MscVrPpIpPortBootpPOperationalState_Object = MibTableColumn
mscVrPpIpPortBootpPOperationalState = _MscVrPpIpPortBootpPOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 13, 1, 2),
    _MscVrPpIpPortBootpPOperationalState_Type()
)
mscVrPpIpPortBootpPOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPOperationalState.setStatus("mandatory")


class _MscVrPpIpPortBootpPUsageState_Type(Integer32):
    """Custom type mscVrPpIpPortBootpPUsageState based on Integer32"""
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
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_MscVrPpIpPortBootpPUsageState_Type.__name__ = "Integer32"
_MscVrPpIpPortBootpPUsageState_Object = MibTableColumn
mscVrPpIpPortBootpPUsageState = _MscVrPpIpPortBootpPUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 13, 1, 3),
    _MscVrPpIpPortBootpPUsageState_Type()
)
mscVrPpIpPortBootpPUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPUsageState.setStatus("mandatory")
_MscVrPpIpPortBootpPStatsTable_Object = MibTable
mscVrPpIpPortBootpPStatsTable = _MscVrPpIpPortBootpPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 14)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPStatsTable.setStatus("mandatory")
_MscVrPpIpPortBootpPStatsEntry_Object = MibTableRow
mscVrPpIpPortBootpPStatsEntry = _MscVrPpIpPortBootpPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 14, 1)
)
mscVrPpIpPortBootpPStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortBootpPIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPStatsEntry.setStatus("mandatory")
_MscVrPpIpPortBootpPInRequests_Type = Counter32
_MscVrPpIpPortBootpPInRequests_Object = MibTableColumn
mscVrPpIpPortBootpPInRequests = _MscVrPpIpPortBootpPInRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 14, 1, 1),
    _MscVrPpIpPortBootpPInRequests_Type()
)
mscVrPpIpPortBootpPInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPInRequests.setStatus("mandatory")
_MscVrPpIpPortBootpPInReplies_Type = Counter32
_MscVrPpIpPortBootpPInReplies_Object = MibTableColumn
mscVrPpIpPortBootpPInReplies = _MscVrPpIpPortBootpPInReplies_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 14, 1, 2),
    _MscVrPpIpPortBootpPInReplies_Type()
)
mscVrPpIpPortBootpPInReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPInReplies.setStatus("mandatory")
_MscVrPpIpPortBootpPOutRequests_Type = Counter32
_MscVrPpIpPortBootpPOutRequests_Object = MibTableColumn
mscVrPpIpPortBootpPOutRequests = _MscVrPpIpPortBootpPOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 14, 1, 3),
    _MscVrPpIpPortBootpPOutRequests_Type()
)
mscVrPpIpPortBootpPOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPOutRequests.setStatus("mandatory")
_MscVrPpIpPortBootpPOutReplies_Type = Counter32
_MscVrPpIpPortBootpPOutReplies_Object = MibTableColumn
mscVrPpIpPortBootpPOutReplies = _MscVrPpIpPortBootpPOutReplies_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 14, 1, 4),
    _MscVrPpIpPortBootpPOutReplies_Type()
)
mscVrPpIpPortBootpPOutReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPOutReplies.setStatus("mandatory")
_MscVrPpIpPortBootpPInRequestErrors_Type = Counter32
_MscVrPpIpPortBootpPInRequestErrors_Object = MibTableColumn
mscVrPpIpPortBootpPInRequestErrors = _MscVrPpIpPortBootpPInRequestErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 14, 1, 5),
    _MscVrPpIpPortBootpPInRequestErrors_Type()
)
mscVrPpIpPortBootpPInRequestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPInRequestErrors.setStatus("mandatory")
_MscVrPpIpPortBootpPInReplyErrors_Type = Counter32
_MscVrPpIpPortBootpPInReplyErrors_Object = MibTableColumn
mscVrPpIpPortBootpPInReplyErrors = _MscVrPpIpPortBootpPInReplyErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 14, 1, 6),
    _MscVrPpIpPortBootpPInReplyErrors_Type()
)
mscVrPpIpPortBootpPInReplyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPInReplyErrors.setStatus("mandatory")
_MscVrPpIpPortBootpPAddrTable_Object = MibTable
mscVrPpIpPortBootpPAddrTable = _MscVrPpIpPortBootpPAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 290)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPAddrTable.setStatus("mandatory")
_MscVrPpIpPortBootpPAddrEntry_Object = MibTableRow
mscVrPpIpPortBootpPAddrEntry = _MscVrPpIpPortBootpPAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 290, 1)
)
mscVrPpIpPortBootpPAddrEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortBootpPIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortBootpPAddrValue"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPAddrEntry.setStatus("mandatory")
_MscVrPpIpPortBootpPAddrValue_Type = IpAddress
_MscVrPpIpPortBootpPAddrValue_Object = MibTableColumn
mscVrPpIpPortBootpPAddrValue = _MscVrPpIpPortBootpPAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 290, 1, 1),
    _MscVrPpIpPortBootpPAddrValue_Type()
)
mscVrPpIpPortBootpPAddrValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPAddrValue.setStatus("mandatory")
_MscVrPpIpPortBootpPAddrRowStatus_Type = RowStatus
_MscVrPpIpPortBootpPAddrRowStatus_Object = MibTableColumn
mscVrPpIpPortBootpPAddrRowStatus = _MscVrPpIpPortBootpPAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 4, 290, 1, 2),
    _MscVrPpIpPortBootpPAddrRowStatus_Type()
)
mscVrPpIpPortBootpPAddrRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortBootpPAddrRowStatus.setStatus("mandatory")
_MscVrPpIpPortProvTable_Object = MibTable
mscVrPpIpPortProvTable = _MscVrPpIpPortProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 10)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortProvTable.setStatus("mandatory")
_MscVrPpIpPortProvEntry_Object = MibTableRow
mscVrPpIpPortProvEntry = _MscVrPpIpPortProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 10, 1)
)
mscVrPpIpPortProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortProvEntry.setStatus("mandatory")


class _MscVrPpIpPortMaxTxUnit_Type(Unsigned32):
    """Custom type mscVrPpIpPortMaxTxUnit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 18944),
    )


_MscVrPpIpPortMaxTxUnit_Type.__name__ = "Unsigned32"
_MscVrPpIpPortMaxTxUnit_Object = MibTableColumn
mscVrPpIpPortMaxTxUnit = _MscVrPpIpPortMaxTxUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 10, 1, 2),
    _MscVrPpIpPortMaxTxUnit_Type()
)
mscVrPpIpPortMaxTxUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortMaxTxUnit.setStatus("mandatory")


class _MscVrPpIpPortArpStatus_Type(Integer32):
    """Custom type mscVrPpIpPortArpStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_MscVrPpIpPortArpStatus_Type.__name__ = "Integer32"
_MscVrPpIpPortArpStatus_Object = MibTableColumn
mscVrPpIpPortArpStatus = _MscVrPpIpPortArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 10, 1, 3),
    _MscVrPpIpPortArpStatus_Type()
)
mscVrPpIpPortArpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortArpStatus.setStatus("mandatory")


class _MscVrPpIpPortProxyArpStatus_Type(Integer32):
    """Custom type mscVrPpIpPortProxyArpStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MscVrPpIpPortProxyArpStatus_Type.__name__ = "Integer32"
_MscVrPpIpPortProxyArpStatus_Object = MibTableColumn
mscVrPpIpPortProxyArpStatus = _MscVrPpIpPortProxyArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 10, 1, 4),
    _MscVrPpIpPortProxyArpStatus_Type()
)
mscVrPpIpPortProxyArpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortProxyArpStatus.setStatus("mandatory")


class _MscVrPpIpPortArpNoLearn_Type(Integer32):
    """Custom type mscVrPpIpPortArpNoLearn based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MscVrPpIpPortArpNoLearn_Type.__name__ = "Integer32"
_MscVrPpIpPortArpNoLearn_Object = MibTableColumn
mscVrPpIpPortArpNoLearn = _MscVrPpIpPortArpNoLearn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 10, 1, 5),
    _MscVrPpIpPortArpNoLearn_Type()
)
mscVrPpIpPortArpNoLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortArpNoLearn.setStatus("mandatory")


class _MscVrPpIpPortSendRedirect_Type(Integer32):
    """Custom type mscVrPpIpPortSendRedirect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MscVrPpIpPortSendRedirect_Type.__name__ = "Integer32"
_MscVrPpIpPortSendRedirect_Object = MibTableColumn
mscVrPpIpPortSendRedirect = _MscVrPpIpPortSendRedirect_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 10, 1, 6),
    _MscVrPpIpPortSendRedirect_Type()
)
mscVrPpIpPortSendRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortSendRedirect.setStatus("mandatory")


class _MscVrPpIpPortMulticastStatus_Type(Integer32):
    """Custom type mscVrPpIpPortMulticastStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_MscVrPpIpPortMulticastStatus_Type.__name__ = "Integer32"
_MscVrPpIpPortMulticastStatus_Object = MibTableColumn
mscVrPpIpPortMulticastStatus = _MscVrPpIpPortMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 10, 1, 7),
    _MscVrPpIpPortMulticastStatus_Type()
)
mscVrPpIpPortMulticastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortMulticastStatus.setStatus("mandatory")


class _MscVrPpIpPortRelayAddress_Type(IpAddress):
    """Custom type mscVrPpIpPortRelayAddress based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrPpIpPortRelayAddress_Object = MibTableColumn
mscVrPpIpPortRelayAddress = _MscVrPpIpPortRelayAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 10, 1, 8),
    _MscVrPpIpPortRelayAddress_Type()
)
mscVrPpIpPortRelayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortRelayAddress.setStatus("mandatory")


class _MscVrPpIpPortRelayBroadcast_Type(Integer32):
    """Custom type mscVrPpIpPortRelayBroadcast based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_MscVrPpIpPortRelayBroadcast_Type.__name__ = "Integer32"
_MscVrPpIpPortRelayBroadcast_Object = MibTableColumn
mscVrPpIpPortRelayBroadcast = _MscVrPpIpPortRelayBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 10, 1, 9),
    _MscVrPpIpPortRelayBroadcast_Type()
)
mscVrPpIpPortRelayBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortRelayBroadcast.setStatus("mandatory")


class _MscVrPpIpPortLinkModel_Type(Integer32):
    """Custom type mscVrPpIpPortLinkModel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localAreaNetwork", 1),
          ("pointToPoint", 2))
    )


_MscVrPpIpPortLinkModel_Type.__name__ = "Integer32"
_MscVrPpIpPortLinkModel_Object = MibTableColumn
mscVrPpIpPortLinkModel = _MscVrPpIpPortLinkModel_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 10, 1, 10),
    _MscVrPpIpPortLinkModel_Type()
)
mscVrPpIpPortLinkModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLinkModel.setStatus("mandatory")


class _MscVrPpIpPortLanModel_Type(Integer32):
    """Custom type mscVrPpIpPortLanModel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localAreaNetwork", 1),
          ("nonBroadcastMultipleAccess", 2))
    )


_MscVrPpIpPortLanModel_Type.__name__ = "Integer32"
_MscVrPpIpPortLanModel_Object = MibTableColumn
mscVrPpIpPortLanModel = _MscVrPpIpPortLanModel_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 10, 1, 11),
    _MscVrPpIpPortLanModel_Type()
)
mscVrPpIpPortLanModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLanModel.setStatus("mandatory")


class _MscVrPpIpPortEncap_Type(Integer32):
    """Custom type mscVrPpIpPortEncap based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("ethernet", 2),
          ("ieee8023", 1))
    )


_MscVrPpIpPortEncap_Type.__name__ = "Integer32"
_MscVrPpIpPortEncap_Object = MibTableColumn
mscVrPpIpPortEncap = _MscVrPpIpPortEncap_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 10, 1, 12),
    _MscVrPpIpPortEncap_Type()
)
mscVrPpIpPortEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortEncap.setStatus("mandatory")


class _MscVrPpIpPortIcmpMaskReply_Type(Integer32):
    """Custom type mscVrPpIpPortIcmpMaskReply based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MscVrPpIpPortIcmpMaskReply_Type.__name__ = "Integer32"
_MscVrPpIpPortIcmpMaskReply_Object = MibTableColumn
mscVrPpIpPortIcmpMaskReply = _MscVrPpIpPortIcmpMaskReply_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 10, 1, 13),
    _MscVrPpIpPortIcmpMaskReply_Type()
)
mscVrPpIpPortIcmpMaskReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortIcmpMaskReply.setStatus("mandatory")


class _MscVrPpIpPortDirectedBroadcast_Type(Integer32):
    """Custom type mscVrPpIpPortDirectedBroadcast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MscVrPpIpPortDirectedBroadcast_Type.__name__ = "Integer32"
_MscVrPpIpPortDirectedBroadcast_Object = MibTableColumn
mscVrPpIpPortDirectedBroadcast = _MscVrPpIpPortDirectedBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 10, 1, 14),
    _MscVrPpIpPortDirectedBroadcast_Type()
)
mscVrPpIpPortDirectedBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortDirectedBroadcast.setStatus("mandatory")


class _MscVrPpIpPortAssignedQos_Type(Unsigned32):
    """Custom type mscVrPpIpPortAssignedQos based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscVrPpIpPortAssignedQos_Type.__name__ = "Unsigned32"
_MscVrPpIpPortAssignedQos_Object = MibTableColumn
mscVrPpIpPortAssignedQos = _MscVrPpIpPortAssignedQos_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 10, 1, 15),
    _MscVrPpIpPortAssignedQos_Type()
)
mscVrPpIpPortAssignedQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortAssignedQos.setStatus("mandatory")


class _MscVrPpIpPortAllowMcastMacDest_Type(Integer32):
    """Custom type mscVrPpIpPortAllowMcastMacDest based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MscVrPpIpPortAllowMcastMacDest_Type.__name__ = "Integer32"
_MscVrPpIpPortAllowMcastMacDest_Object = MibTableColumn
mscVrPpIpPortAllowMcastMacDest = _MscVrPpIpPortAllowMcastMacDest_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 10, 1, 16),
    _MscVrPpIpPortAllowMcastMacDest_Type()
)
mscVrPpIpPortAllowMcastMacDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortAllowMcastMacDest.setStatus("mandatory")
_MscVrPpIpPortCosPolicyAssignment_Type = Link
_MscVrPpIpPortCosPolicyAssignment_Object = MibTableColumn
mscVrPpIpPortCosPolicyAssignment = _MscVrPpIpPortCosPolicyAssignment_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 10, 1, 17),
    _MscVrPpIpPortCosPolicyAssignment_Type()
)
mscVrPpIpPortCosPolicyAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortCosPolicyAssignment.setStatus("mandatory")
_MscVrPpIpPortSresProvTable_Object = MibTable
mscVrPpIpPortSresProvTable = _MscVrPpIpPortSresProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 11)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortSresProvTable.setStatus("mandatory")
_MscVrPpIpPortSresProvEntry_Object = MibTableRow
mscVrPpIpPortSresProvEntry = _MscVrPpIpPortSresProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 11, 1)
)
mscVrPpIpPortSresProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortSresProvEntry.setStatus("mandatory")


class _MscVrPpIpPortSourceRouteEndStationSupport_Type(Integer32):
    """Custom type mscVrPpIpPortSourceRouteEndStationSupport based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MscVrPpIpPortSourceRouteEndStationSupport_Type.__name__ = "Integer32"
_MscVrPpIpPortSourceRouteEndStationSupport_Object = MibTableColumn
mscVrPpIpPortSourceRouteEndStationSupport = _MscVrPpIpPortSourceRouteEndStationSupport_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 11, 1, 1),
    _MscVrPpIpPortSourceRouteEndStationSupport_Type()
)
mscVrPpIpPortSourceRouteEndStationSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortSourceRouteEndStationSupport.setStatus("mandatory")
_MscVrPpIpPortAdminControlTable_Object = MibTable
mscVrPpIpPortAdminControlTable = _MscVrPpIpPortAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 12)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortAdminControlTable.setStatus("mandatory")
_MscVrPpIpPortAdminControlEntry_Object = MibTableRow
mscVrPpIpPortAdminControlEntry = _MscVrPpIpPortAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 12, 1)
)
mscVrPpIpPortAdminControlEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortAdminControlEntry.setStatus("mandatory")


class _MscVrPpIpPortSnmpAdminStatus_Type(Integer32):
    """Custom type mscVrPpIpPortSnmpAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscVrPpIpPortSnmpAdminStatus_Type.__name__ = "Integer32"
_MscVrPpIpPortSnmpAdminStatus_Object = MibTableColumn
mscVrPpIpPortSnmpAdminStatus = _MscVrPpIpPortSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 12, 1, 1),
    _MscVrPpIpPortSnmpAdminStatus_Type()
)
mscVrPpIpPortSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortSnmpAdminStatus.setStatus("mandatory")
_MscVrPpIpPortOperTable_Object = MibTable
mscVrPpIpPortOperTable = _MscVrPpIpPortOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 13)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortOperTable.setStatus("mandatory")
_MscVrPpIpPortOperEntry_Object = MibTableRow
mscVrPpIpPortOperEntry = _MscVrPpIpPortOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 13, 1)
)
mscVrPpIpPortOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortOperEntry.setStatus("mandatory")


class _MscVrPpIpPortMediaType_Type(Integer32):
    """Custom type mscVrPpIpPortMediaType based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("atmMpeLlcEncap", 14),
          ("atmMpeVcEncap", 13),
          ("clusterBridge", 10),
          ("ethernet", 1),
          ("fddi", 2),
          ("frameRelay", 9),
          ("invalid", 12),
          ("lecEther", 15),
          ("lecToken", 16),
          ("ppp", 4),
          ("smds", 11),
          ("tokenRing", 3),
          ("tunnel", 17),
          ("vcpEther", 5),
          ("vcpToken", 6),
          ("virtual", 18),
          ("vns", 7),
          ("x25", 8))
    )


_MscVrPpIpPortMediaType_Type.__name__ = "Integer32"
_MscVrPpIpPortMediaType_Object = MibTableColumn
mscVrPpIpPortMediaType = _MscVrPpIpPortMediaType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 13, 1, 1),
    _MscVrPpIpPortMediaType_Type()
)
mscVrPpIpPortMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortMediaType.setStatus("mandatory")


class _MscVrPpIpPortOperMtu_Type(Unsigned32):
    """Custom type mscVrPpIpPortOperMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 18944),
    )


_MscVrPpIpPortOperMtu_Type.__name__ = "Unsigned32"
_MscVrPpIpPortOperMtu_Object = MibTableColumn
mscVrPpIpPortOperMtu = _MscVrPpIpPortOperMtu_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 13, 1, 2),
    _MscVrPpIpPortOperMtu_Type()
)
mscVrPpIpPortOperMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortOperMtu.setStatus("mandatory")


class _MscVrPpIpPortOperArpStatus_Type(Integer32):
    """Custom type mscVrPpIpPortOperArpStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MscVrPpIpPortOperArpStatus_Type.__name__ = "Integer32"
_MscVrPpIpPortOperArpStatus_Object = MibTableColumn
mscVrPpIpPortOperArpStatus = _MscVrPpIpPortOperArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 13, 1, 3),
    _MscVrPpIpPortOperArpStatus_Type()
)
mscVrPpIpPortOperArpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortOperArpStatus.setStatus("mandatory")


class _MscVrPpIpPortOperMulticastStatus_Type(Integer32):
    """Custom type mscVrPpIpPortOperMulticastStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MscVrPpIpPortOperMulticastStatus_Type.__name__ = "Integer32"
_MscVrPpIpPortOperMulticastStatus_Object = MibTableColumn
mscVrPpIpPortOperMulticastStatus = _MscVrPpIpPortOperMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 13, 1, 4),
    _MscVrPpIpPortOperMulticastStatus_Type()
)
mscVrPpIpPortOperMulticastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortOperMulticastStatus.setStatus("mandatory")


class _MscVrPpIpPortOperEncap_Type(Integer32):
    """Custom type mscVrPpIpPortOperEncap based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("ieee8023", 1),
          ("notApplicable", 3))
    )


_MscVrPpIpPortOperEncap_Type.__name__ = "Integer32"
_MscVrPpIpPortOperEncap_Object = MibTableColumn
mscVrPpIpPortOperEncap = _MscVrPpIpPortOperEncap_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 13, 1, 5),
    _MscVrPpIpPortOperEncap_Type()
)
mscVrPpIpPortOperEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortOperEncap.setStatus("mandatory")
_MscVrPpIpPortOperCosPolicyAssignment_Type = RowPointer
_MscVrPpIpPortOperCosPolicyAssignment_Object = MibTableColumn
mscVrPpIpPortOperCosPolicyAssignment = _MscVrPpIpPortOperCosPolicyAssignment_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 13, 1, 433),
    _MscVrPpIpPortOperCosPolicyAssignment_Type()
)
mscVrPpIpPortOperCosPolicyAssignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortOperCosPolicyAssignment.setStatus("mandatory")
_MscVrPpIpPortRelayBcOperTable_Object = MibTable
mscVrPpIpPortRelayBcOperTable = _MscVrPpIpPortRelayBcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 14)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortRelayBcOperTable.setStatus("mandatory")
_MscVrPpIpPortRelayBcOperEntry_Object = MibTableRow
mscVrPpIpPortRelayBcOperEntry = _MscVrPpIpPortRelayBcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 14, 1)
)
mscVrPpIpPortRelayBcOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortRelayBcOperEntry.setStatus("mandatory")
_MscVrPpIpPortRelayAddressCount_Type = Counter32
_MscVrPpIpPortRelayAddressCount_Object = MibTableColumn
mscVrPpIpPortRelayAddressCount = _MscVrPpIpPortRelayAddressCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 14, 1, 1),
    _MscVrPpIpPortRelayAddressCount_Type()
)
mscVrPpIpPortRelayAddressCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortRelayAddressCount.setStatus("mandatory")
_MscVrPpIpPortRelayBcCount_Type = Counter32
_MscVrPpIpPortRelayBcCount_Object = MibTableColumn
mscVrPpIpPortRelayBcCount = _MscVrPpIpPortRelayBcCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 14, 1, 2),
    _MscVrPpIpPortRelayBcCount_Type()
)
mscVrPpIpPortRelayBcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortRelayBcCount.setStatus("mandatory")
_MscVrPpIpPortStateTable_Object = MibTable
mscVrPpIpPortStateTable = _MscVrPpIpPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 15)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortStateTable.setStatus("mandatory")
_MscVrPpIpPortStateEntry_Object = MibTableRow
mscVrPpIpPortStateEntry = _MscVrPpIpPortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 15, 1)
)
mscVrPpIpPortStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortStateEntry.setStatus("mandatory")


class _MscVrPpIpPortAdminState_Type(Integer32):
    """Custom type mscVrPpIpPortAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_MscVrPpIpPortAdminState_Type.__name__ = "Integer32"
_MscVrPpIpPortAdminState_Object = MibTableColumn
mscVrPpIpPortAdminState = _MscVrPpIpPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 15, 1, 1),
    _MscVrPpIpPortAdminState_Type()
)
mscVrPpIpPortAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortAdminState.setStatus("mandatory")


class _MscVrPpIpPortOperationalState_Type(Integer32):
    """Custom type mscVrPpIpPortOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MscVrPpIpPortOperationalState_Type.__name__ = "Integer32"
_MscVrPpIpPortOperationalState_Object = MibTableColumn
mscVrPpIpPortOperationalState = _MscVrPpIpPortOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 15, 1, 2),
    _MscVrPpIpPortOperationalState_Type()
)
mscVrPpIpPortOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortOperationalState.setStatus("mandatory")


class _MscVrPpIpPortUsageState_Type(Integer32):
    """Custom type mscVrPpIpPortUsageState based on Integer32"""
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
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_MscVrPpIpPortUsageState_Type.__name__ = "Integer32"
_MscVrPpIpPortUsageState_Object = MibTableColumn
mscVrPpIpPortUsageState = _MscVrPpIpPortUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 15, 1, 3),
    _MscVrPpIpPortUsageState_Type()
)
mscVrPpIpPortUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortUsageState.setStatus("mandatory")
_MscVrPpIpPortOperStatusTable_Object = MibTable
mscVrPpIpPortOperStatusTable = _MscVrPpIpPortOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 16)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortOperStatusTable.setStatus("mandatory")
_MscVrPpIpPortOperStatusEntry_Object = MibTableRow
mscVrPpIpPortOperStatusEntry = _MscVrPpIpPortOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 16, 1)
)
mscVrPpIpPortOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortOperStatusEntry.setStatus("mandatory")


class _MscVrPpIpPortSnmpOperStatus_Type(Integer32):
    """Custom type mscVrPpIpPortSnmpOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscVrPpIpPortSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrPpIpPortSnmpOperStatus_Object = MibTableColumn
mscVrPpIpPortSnmpOperStatus = _MscVrPpIpPortSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 16, 1, 1),
    _MscVrPpIpPortSnmpOperStatus_Type()
)
mscVrPpIpPortSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortSnmpOperStatus.setStatus("mandatory")
_MscVrIp_ObjectIdentity = ObjectIdentity
mscVrIp = _MscVrIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6)
)
_MscVrIpRowStatusTable_Object = MibTable
mscVrIpRowStatusTable = _MscVrIpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 1)
)
if mibBuilder.loadTexts:
    mscVrIpRowStatusTable.setStatus("mandatory")
_MscVrIpRowStatusEntry_Object = MibTableRow
mscVrIpRowStatusEntry = _MscVrIpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 1, 1)
)
mscVrIpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpRowStatusEntry.setStatus("mandatory")
_MscVrIpRowStatus_Type = RowStatus
_MscVrIpRowStatus_Object = MibTableColumn
mscVrIpRowStatus = _MscVrIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 1, 1, 1),
    _MscVrIpRowStatus_Type()
)
mscVrIpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRowStatus.setStatus("mandatory")
_MscVrIpComponentName_Type = DisplayString
_MscVrIpComponentName_Object = MibTableColumn
mscVrIpComponentName = _MscVrIpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 1, 1, 2),
    _MscVrIpComponentName_Type()
)
mscVrIpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpComponentName.setStatus("mandatory")
_MscVrIpStorageType_Type = StorageType
_MscVrIpStorageType_Object = MibTableColumn
mscVrIpStorageType = _MscVrIpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 1, 1, 4),
    _MscVrIpStorageType_Type()
)
mscVrIpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpStorageType.setStatus("mandatory")
_MscVrIpIndex_Type = NonReplicated
_MscVrIpIndex_Object = MibTableColumn
mscVrIpIndex = _MscVrIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 1, 1, 10),
    _MscVrIpIndex_Type()
)
mscVrIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpIndex.setStatus("mandatory")
_MscVrIpFwd_ObjectIdentity = ObjectIdentity
mscVrIpFwd = _MscVrIpFwd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 3)
)
_MscVrIpFwdRowStatusTable_Object = MibTable
mscVrIpFwdRowStatusTable = _MscVrIpFwdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 3, 1)
)
if mibBuilder.loadTexts:
    mscVrIpFwdRowStatusTable.setStatus("mandatory")
_MscVrIpFwdRowStatusEntry_Object = MibTableRow
mscVrIpFwdRowStatusEntry = _MscVrIpFwdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 3, 1, 1)
)
mscVrIpFwdRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpFwdDestAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpFwdDestMaskIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpFwdTypeOfServiceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpFwdGatewayIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpFwdRowStatusEntry.setStatus("mandatory")
_MscVrIpFwdRowStatus_Type = RowStatus
_MscVrIpFwdRowStatus_Object = MibTableColumn
mscVrIpFwdRowStatus = _MscVrIpFwdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 3, 1, 1, 1),
    _MscVrIpFwdRowStatus_Type()
)
mscVrIpFwdRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpFwdRowStatus.setStatus("mandatory")
_MscVrIpFwdComponentName_Type = DisplayString
_MscVrIpFwdComponentName_Object = MibTableColumn
mscVrIpFwdComponentName = _MscVrIpFwdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 3, 1, 1, 2),
    _MscVrIpFwdComponentName_Type()
)
mscVrIpFwdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpFwdComponentName.setStatus("mandatory")
_MscVrIpFwdStorageType_Type = StorageType
_MscVrIpFwdStorageType_Object = MibTableColumn
mscVrIpFwdStorageType = _MscVrIpFwdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 3, 1, 1, 4),
    _MscVrIpFwdStorageType_Type()
)
mscVrIpFwdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpFwdStorageType.setStatus("mandatory")
_MscVrIpFwdDestAddressIndex_Type = IpAddress
_MscVrIpFwdDestAddressIndex_Object = MibTableColumn
mscVrIpFwdDestAddressIndex = _MscVrIpFwdDestAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 3, 1, 1, 10),
    _MscVrIpFwdDestAddressIndex_Type()
)
mscVrIpFwdDestAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpFwdDestAddressIndex.setStatus("mandatory")
_MscVrIpFwdDestMaskIndex_Type = IpAddress
_MscVrIpFwdDestMaskIndex_Object = MibTableColumn
mscVrIpFwdDestMaskIndex = _MscVrIpFwdDestMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 3, 1, 1, 11),
    _MscVrIpFwdDestMaskIndex_Type()
)
mscVrIpFwdDestMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpFwdDestMaskIndex.setStatus("mandatory")


class _MscVrIpFwdTypeOfServiceIndex_Type(Integer32):
    """Custom type mscVrIpFwdTypeOfServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_MscVrIpFwdTypeOfServiceIndex_Type.__name__ = "Integer32"
_MscVrIpFwdTypeOfServiceIndex_Object = MibTableColumn
mscVrIpFwdTypeOfServiceIndex = _MscVrIpFwdTypeOfServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 3, 1, 1, 12),
    _MscVrIpFwdTypeOfServiceIndex_Type()
)
mscVrIpFwdTypeOfServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpFwdTypeOfServiceIndex.setStatus("mandatory")
_MscVrIpFwdGatewayIndex_Type = IpAddress
_MscVrIpFwdGatewayIndex_Object = MibTableColumn
mscVrIpFwdGatewayIndex = _MscVrIpFwdGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 3, 1, 1, 13),
    _MscVrIpFwdGatewayIndex_Type()
)
mscVrIpFwdGatewayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpFwdGatewayIndex.setStatus("mandatory")
_MscVrIpFwdOperTable_Object = MibTable
mscVrIpFwdOperTable = _MscVrIpFwdOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 3, 10)
)
if mibBuilder.loadTexts:
    mscVrIpFwdOperTable.setStatus("mandatory")
_MscVrIpFwdOperEntry_Object = MibTableRow
mscVrIpFwdOperEntry = _MscVrIpFwdOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 3, 10, 1)
)
mscVrIpFwdOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpFwdDestAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpFwdDestMaskIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpFwdTypeOfServiceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpFwdGatewayIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpFwdOperEntry.setStatus("mandatory")


class _MscVrIpFwdIfIndex_Type(InterfaceIndex):
    """Custom type mscVrIpFwdIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrIpFwdIfIndex_Type.__name__ = "InterfaceIndex"
_MscVrIpFwdIfIndex_Object = MibTableColumn
mscVrIpFwdIfIndex = _MscVrIpFwdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 3, 10, 1, 1),
    _MscVrIpFwdIfIndex_Type()
)
mscVrIpFwdIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpFwdIfIndex.setStatus("mandatory")


class _MscVrIpFwdType_Type(Integer32):
    """Custom type mscVrIpFwdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("localInterface", 3),
          ("notDefined", 1),
          ("remoteDestination", 4))
    )


_MscVrIpFwdType_Type.__name__ = "Integer32"
_MscVrIpFwdType_Object = MibTableColumn
mscVrIpFwdType = _MscVrIpFwdType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 3, 10, 1, 2),
    _MscVrIpFwdType_Type()
)
mscVrIpFwdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpFwdType.setStatus("mandatory")


class _MscVrIpFwdProtocol_Type(Integer32):
    """Custom type mscVrIpFwdProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("bbnSpfIgp", 12),
          ("bgp", 14),
          ("ciscoIgrp", 11),
          ("egp", 5),
          ("esIs", 10),
          ("ggp", 6),
          ("hello", 7),
          ("icmp", 4),
          ("idpr", 15),
          ("isIs", 9),
          ("local", 2),
          ("mpls", 16),
          ("netmgmt", 3),
          ("ospf", 13),
          ("other", 1),
          ("rip", 8))
    )


_MscVrIpFwdProtocol_Type.__name__ = "Integer32"
_MscVrIpFwdProtocol_Object = MibTableColumn
mscVrIpFwdProtocol = _MscVrIpFwdProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 3, 10, 1, 3),
    _MscVrIpFwdProtocol_Type()
)
mscVrIpFwdProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpFwdProtocol.setStatus("mandatory")


class _MscVrIpFwdAge_Type(Gauge32):
    """Custom type mscVrIpFwdAge based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpFwdAge_Type.__name__ = "Gauge32"
_MscVrIpFwdAge_Object = MibTableColumn
mscVrIpFwdAge = _MscVrIpFwdAge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 3, 10, 1, 4),
    _MscVrIpFwdAge_Type()
)
mscVrIpFwdAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpFwdAge.setStatus("mandatory")
_MscVrIpFwdProtocolPortName_Type = RowPointer
_MscVrIpFwdProtocolPortName_Object = MibTableColumn
mscVrIpFwdProtocolPortName = _MscVrIpFwdProtocolPortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 3, 10, 1, 5),
    _MscVrIpFwdProtocolPortName_Type()
)
mscVrIpFwdProtocolPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpFwdProtocolPortName.setStatus("mandatory")


class _MscVrIpFwdNextHopAs_Type(Unsigned32):
    """Custom type mscVrIpFwdNextHopAs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429467295),
    )


_MscVrIpFwdNextHopAs_Type.__name__ = "Unsigned32"
_MscVrIpFwdNextHopAs_Object = MibTableColumn
mscVrIpFwdNextHopAs = _MscVrIpFwdNextHopAs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 3, 10, 1, 7),
    _MscVrIpFwdNextHopAs_Type()
)
mscVrIpFwdNextHopAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpFwdNextHopAs.setStatus("mandatory")


class _MscVrIpFwdMetric_Type(Integer32):
    """Custom type mscVrIpFwdMetric based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MscVrIpFwdMetric_Type.__name__ = "Integer32"
_MscVrIpFwdMetric_Object = MibTableColumn
mscVrIpFwdMetric = _MscVrIpFwdMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 3, 10, 1, 8),
    _MscVrIpFwdMetric_Type()
)
mscVrIpFwdMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpFwdMetric.setStatus("mandatory")
_MscVrIpRdb_ObjectIdentity = ObjectIdentity
mscVrIpRdb = _MscVrIpRdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 4)
)
_MscVrIpRdbRowStatusTable_Object = MibTable
mscVrIpRdbRowStatusTable = _MscVrIpRdbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 4, 1)
)
if mibBuilder.loadTexts:
    mscVrIpRdbRowStatusTable.setStatus("mandatory")
_MscVrIpRdbRowStatusEntry_Object = MibTableRow
mscVrIpRdbRowStatusEntry = _MscVrIpRdbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 4, 1, 1)
)
mscVrIpRdbRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRdbDestAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRdbDestMaskIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRdbProtocolIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRdbGatewayIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpRdbRowStatusEntry.setStatus("mandatory")
_MscVrIpRdbRowStatus_Type = RowStatus
_MscVrIpRdbRowStatus_Object = MibTableColumn
mscVrIpRdbRowStatus = _MscVrIpRdbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 4, 1, 1, 1),
    _MscVrIpRdbRowStatus_Type()
)
mscVrIpRdbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRdbRowStatus.setStatus("mandatory")
_MscVrIpRdbComponentName_Type = DisplayString
_MscVrIpRdbComponentName_Object = MibTableColumn
mscVrIpRdbComponentName = _MscVrIpRdbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 4, 1, 1, 2),
    _MscVrIpRdbComponentName_Type()
)
mscVrIpRdbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRdbComponentName.setStatus("mandatory")
_MscVrIpRdbStorageType_Type = StorageType
_MscVrIpRdbStorageType_Object = MibTableColumn
mscVrIpRdbStorageType = _MscVrIpRdbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 4, 1, 1, 4),
    _MscVrIpRdbStorageType_Type()
)
mscVrIpRdbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRdbStorageType.setStatus("mandatory")
_MscVrIpRdbDestAddressIndex_Type = IpAddress
_MscVrIpRdbDestAddressIndex_Object = MibTableColumn
mscVrIpRdbDestAddressIndex = _MscVrIpRdbDestAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 4, 1, 1, 10),
    _MscVrIpRdbDestAddressIndex_Type()
)
mscVrIpRdbDestAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpRdbDestAddressIndex.setStatus("mandatory")
_MscVrIpRdbDestMaskIndex_Type = IpAddress
_MscVrIpRdbDestMaskIndex_Object = MibTableColumn
mscVrIpRdbDestMaskIndex = _MscVrIpRdbDestMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 4, 1, 1, 11),
    _MscVrIpRdbDestMaskIndex_Type()
)
mscVrIpRdbDestMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpRdbDestMaskIndex.setStatus("mandatory")


class _MscVrIpRdbProtocolIndex_Type(Integer32):
    """Custom type mscVrIpRdbProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("bgpAggrDiscard", 14),
          ("bgpExternal", 12),
          ("bgpInternal", 13),
          ("bogus", 1),
          ("egp", 11),
          ("local", 2),
          ("mpls", 16),
          ("ospf", 5),
          ("ospfExternal", 6),
          ("ospfType3Discard", 7),
          ("ospfType7Discard", 8),
          ("redistrib", 15),
          ("remote", 3),
          ("rip", 9),
          ("ripDiscard", 10),
          ("special", 4))
    )


_MscVrIpRdbProtocolIndex_Type.__name__ = "Integer32"
_MscVrIpRdbProtocolIndex_Object = MibTableColumn
mscVrIpRdbProtocolIndex = _MscVrIpRdbProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 4, 1, 1, 12),
    _MscVrIpRdbProtocolIndex_Type()
)
mscVrIpRdbProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpRdbProtocolIndex.setStatus("mandatory")
_MscVrIpRdbGatewayIndex_Type = IpAddress
_MscVrIpRdbGatewayIndex_Object = MibTableColumn
mscVrIpRdbGatewayIndex = _MscVrIpRdbGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 4, 1, 1, 13),
    _MscVrIpRdbGatewayIndex_Type()
)
mscVrIpRdbGatewayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpRdbGatewayIndex.setStatus("mandatory")
_MscVrIpRdbOperTable_Object = MibTable
mscVrIpRdbOperTable = _MscVrIpRdbOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 4, 10)
)
if mibBuilder.loadTexts:
    mscVrIpRdbOperTable.setStatus("mandatory")
_MscVrIpRdbOperEntry_Object = MibTableRow
mscVrIpRdbOperEntry = _MscVrIpRdbOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 4, 10, 1)
)
mscVrIpRdbOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRdbDestAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRdbDestMaskIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRdbProtocolIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRdbGatewayIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpRdbOperEntry.setStatus("mandatory")


class _MscVrIpRdbMetric_Type(Integer32):
    """Custom type mscVrIpRdbMetric based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MscVrIpRdbMetric_Type.__name__ = "Integer32"
_MscVrIpRdbMetric_Object = MibTableColumn
mscVrIpRdbMetric = _MscVrIpRdbMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 4, 10, 1, 1),
    _MscVrIpRdbMetric_Type()
)
mscVrIpRdbMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRdbMetric.setStatus("mandatory")


class _MscVrIpRdbPreference_Type(Unsigned32):
    """Custom type mscVrIpRdbPreference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrIpRdbPreference_Type.__name__ = "Unsigned32"
_MscVrIpRdbPreference_Object = MibTableColumn
mscVrIpRdbPreference = _MscVrIpRdbPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 4, 10, 1, 2),
    _MscVrIpRdbPreference_Type()
)
mscVrIpRdbPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRdbPreference.setStatus("mandatory")


class _MscVrIpRdbAge_Type(Gauge32):
    """Custom type mscVrIpRdbAge based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpRdbAge_Type.__name__ = "Gauge32"
_MscVrIpRdbAge_Object = MibTableColumn
mscVrIpRdbAge = _MscVrIpRdbAge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 4, 10, 1, 3),
    _MscVrIpRdbAge_Type()
)
mscVrIpRdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRdbAge.setStatus("mandatory")
_MscVrIpIf_ObjectIdentity = ObjectIdentity
mscVrIpIf = _MscVrIpIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 5)
)
_MscVrIpIfRowStatusTable_Object = MibTable
mscVrIpIfRowStatusTable = _MscVrIpIfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 5, 1)
)
if mibBuilder.loadTexts:
    mscVrIpIfRowStatusTable.setStatus("mandatory")
_MscVrIpIfRowStatusEntry_Object = MibTableRow
mscVrIpIfRowStatusEntry = _MscVrIpIfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 5, 1, 1)
)
mscVrIpIfRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIfInterfaceAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpIfRowStatusEntry.setStatus("mandatory")
_MscVrIpIfRowStatus_Type = RowStatus
_MscVrIpIfRowStatus_Object = MibTableColumn
mscVrIpIfRowStatus = _MscVrIpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 5, 1, 1, 1),
    _MscVrIpIfRowStatus_Type()
)
mscVrIpIfRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIfRowStatus.setStatus("mandatory")
_MscVrIpIfComponentName_Type = DisplayString
_MscVrIpIfComponentName_Object = MibTableColumn
mscVrIpIfComponentName = _MscVrIpIfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 5, 1, 1, 2),
    _MscVrIpIfComponentName_Type()
)
mscVrIpIfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIfComponentName.setStatus("mandatory")
_MscVrIpIfStorageType_Type = StorageType
_MscVrIpIfStorageType_Object = MibTableColumn
mscVrIpIfStorageType = _MscVrIpIfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 5, 1, 1, 4),
    _MscVrIpIfStorageType_Type()
)
mscVrIpIfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIfStorageType.setStatus("mandatory")
_MscVrIpIfInterfaceAddressIndex_Type = IpAddress
_MscVrIpIfInterfaceAddressIndex_Object = MibTableColumn
mscVrIpIfInterfaceAddressIndex = _MscVrIpIfInterfaceAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 5, 1, 1, 10),
    _MscVrIpIfInterfaceAddressIndex_Type()
)
mscVrIpIfInterfaceAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpIfInterfaceAddressIndex.setStatus("mandatory")
_MscVrIpIfOperTable_Object = MibTable
mscVrIpIfOperTable = _MscVrIpIfOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 5, 10)
)
if mibBuilder.loadTexts:
    mscVrIpIfOperTable.setStatus("mandatory")
_MscVrIpIfOperEntry_Object = MibTableRow
mscVrIpIfOperEntry = _MscVrIpIfOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 5, 10, 1)
)
mscVrIpIfOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIfInterfaceAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpIfOperEntry.setStatus("mandatory")
_MscVrIpIfInterfaceMask_Type = IpAddress
_MscVrIpIfInterfaceMask_Object = MibTableColumn
mscVrIpIfInterfaceMask = _MscVrIpIfInterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 5, 10, 1, 1),
    _MscVrIpIfInterfaceMask_Type()
)
mscVrIpIfInterfaceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIfInterfaceMask.setStatus("mandatory")


class _MscVrIpIfStatus_Type(Integer32):
    """Custom type mscVrIpIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("down", 2),
          ("up", 1))
    )


_MscVrIpIfStatus_Type.__name__ = "Integer32"
_MscVrIpIfStatus_Object = MibTableColumn
mscVrIpIfStatus = _MscVrIpIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 5, 10, 1, 2),
    _MscVrIpIfStatus_Type()
)
mscVrIpIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIfStatus.setStatus("mandatory")


class _MscVrIpIfPPName_Type(AsciiString):
    """Custom type mscVrIpIfPPName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 23),
    )


_MscVrIpIfPPName_Type.__name__ = "AsciiString"
_MscVrIpIfPPName_Object = MibTableColumn
mscVrIpIfPPName = _MscVrIpIfPPName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 5, 10, 1, 3),
    _MscVrIpIfPPName_Type()
)
mscVrIpIfPPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIfPPName.setStatus("mandatory")


class _MscVrIpIfMediaType_Type(Integer32):
    """Custom type mscVrIpIfMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("atmMpeLlcEncap", 15),
          ("atmMpeVcEncap", 14),
          ("clusterBridge", 8),
          ("ethernet", 3),
          ("fddi", 4),
          ("frameRelay", 6),
          ("lecEther", 16),
          ("lecToken", 17),
          ("none", 1),
          ("ppp", 7),
          ("smds", 13),
          ("tokenRing", 2),
          ("tunnel", 18),
          ("vcpEther", 10),
          ("vcpToken", 11),
          ("virtual", 19),
          ("virtualLink", 9),
          ("vns", 12),
          ("x25", 5))
    )


_MscVrIpIfMediaType_Type.__name__ = "Integer32"
_MscVrIpIfMediaType_Object = MibTableColumn
mscVrIpIfMediaType = _MscVrIpIfMediaType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 5, 10, 1, 4),
    _MscVrIpIfMediaType_Type()
)
mscVrIpIfMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIfMediaType.setStatus("mandatory")


class _MscVrIpIfHardwareAddress_Type(DashedHexString):
    """Custom type mscVrIpIfHardwareAddress based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MscVrIpIfHardwareAddress_Type.__name__ = "DashedHexString"
_MscVrIpIfHardwareAddress_Object = MibTableColumn
mscVrIpIfHardwareAddress = _MscVrIpIfHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 5, 10, 1, 5),
    _MscVrIpIfHardwareAddress_Type()
)
mscVrIpIfHardwareAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIfHardwareAddress.setStatus("mandatory")


class _MscVrIpIfMtu_Type(Unsigned32):
    """Custom type mscVrIpIfMtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 18944),
    )


_MscVrIpIfMtu_Type.__name__ = "Unsigned32"
_MscVrIpIfMtu_Object = MibTableColumn
mscVrIpIfMtu = _MscVrIpIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 5, 10, 1, 6),
    _MscVrIpIfMtu_Type()
)
mscVrIpIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIfMtu.setStatus("mandatory")
_MscVrIpIfBroadcastAddress_Type = IpAddress
_MscVrIpIfBroadcastAddress_Object = MibTableColumn
mscVrIpIfBroadcastAddress = _MscVrIpIfBroadcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 5, 10, 1, 7),
    _MscVrIpIfBroadcastAddress_Type()
)
mscVrIpIfBroadcastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIfBroadcastAddress.setStatus("mandatory")


class _MscVrIpIfNcHardwareAddress_Type(DashedHexString):
    """Custom type mscVrIpIfNcHardwareAddress based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MscVrIpIfNcHardwareAddress_Type.__name__ = "DashedHexString"
_MscVrIpIfNcHardwareAddress_Object = MibTableColumn
mscVrIpIfNcHardwareAddress = _MscVrIpIfNcHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 5, 10, 1, 8),
    _MscVrIpIfNcHardwareAddress_Type()
)
mscVrIpIfNcHardwareAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIfNcHardwareAddress.setStatus("mandatory")
_MscVrIpEgp_ObjectIdentity = ObjectIdentity
mscVrIpEgp = _MscVrIpEgp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6)
)
_MscVrIpEgpRowStatusTable_Object = MibTable
mscVrIpEgpRowStatusTable = _MscVrIpEgpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 1)
)
if mibBuilder.loadTexts:
    mscVrIpEgpRowStatusTable.setStatus("mandatory")
_MscVrIpEgpRowStatusEntry_Object = MibTableRow
mscVrIpEgpRowStatusEntry = _MscVrIpEgpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 1, 1)
)
mscVrIpEgpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpEgpRowStatusEntry.setStatus("mandatory")
_MscVrIpEgpRowStatus_Type = RowStatus
_MscVrIpEgpRowStatus_Object = MibTableColumn
mscVrIpEgpRowStatus = _MscVrIpEgpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 1, 1, 1),
    _MscVrIpEgpRowStatus_Type()
)
mscVrIpEgpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpRowStatus.setStatus("mandatory")
_MscVrIpEgpComponentName_Type = DisplayString
_MscVrIpEgpComponentName_Object = MibTableColumn
mscVrIpEgpComponentName = _MscVrIpEgpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 1, 1, 2),
    _MscVrIpEgpComponentName_Type()
)
mscVrIpEgpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpComponentName.setStatus("mandatory")
_MscVrIpEgpStorageType_Type = StorageType
_MscVrIpEgpStorageType_Object = MibTableColumn
mscVrIpEgpStorageType = _MscVrIpEgpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 1, 1, 4),
    _MscVrIpEgpStorageType_Type()
)
mscVrIpEgpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpStorageType.setStatus("mandatory")
_MscVrIpEgpIndex_Type = NonReplicated
_MscVrIpEgpIndex_Object = MibTableColumn
mscVrIpEgpIndex = _MscVrIpEgpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 1, 1, 10),
    _MscVrIpEgpIndex_Type()
)
mscVrIpEgpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpEgpIndex.setStatus("mandatory")
_MscVrIpEgpNbr_ObjectIdentity = ObjectIdentity
mscVrIpEgpNbr = _MscVrIpEgpNbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2)
)
_MscVrIpEgpNbrRowStatusTable_Object = MibTable
mscVrIpEgpNbrRowStatusTable = _MscVrIpEgpNbrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpEgpNbrRowStatusTable.setStatus("mandatory")
_MscVrIpEgpNbrRowStatusEntry_Object = MibTableRow
mscVrIpEgpNbrRowStatusEntry = _MscVrIpEgpNbrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 1, 1)
)
mscVrIpEgpNbrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpNbrNeighborAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpEgpNbrRowStatusEntry.setStatus("mandatory")
_MscVrIpEgpNbrRowStatus_Type = RowStatus
_MscVrIpEgpNbrRowStatus_Object = MibTableColumn
mscVrIpEgpNbrRowStatus = _MscVrIpEgpNbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 1, 1, 1),
    _MscVrIpEgpNbrRowStatus_Type()
)
mscVrIpEgpNbrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpNbrRowStatus.setStatus("mandatory")
_MscVrIpEgpNbrComponentName_Type = DisplayString
_MscVrIpEgpNbrComponentName_Object = MibTableColumn
mscVrIpEgpNbrComponentName = _MscVrIpEgpNbrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 1, 1, 2),
    _MscVrIpEgpNbrComponentName_Type()
)
mscVrIpEgpNbrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpNbrComponentName.setStatus("mandatory")
_MscVrIpEgpNbrStorageType_Type = StorageType
_MscVrIpEgpNbrStorageType_Object = MibTableColumn
mscVrIpEgpNbrStorageType = _MscVrIpEgpNbrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 1, 1, 4),
    _MscVrIpEgpNbrStorageType_Type()
)
mscVrIpEgpNbrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpNbrStorageType.setStatus("mandatory")
_MscVrIpEgpNbrNeighborAddressIndex_Type = IpAddress
_MscVrIpEgpNbrNeighborAddressIndex_Object = MibTableColumn
mscVrIpEgpNbrNeighborAddressIndex = _MscVrIpEgpNbrNeighborAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 1, 1, 10),
    _MscVrIpEgpNbrNeighborAddressIndex_Type()
)
mscVrIpEgpNbrNeighborAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpEgpNbrNeighborAddressIndex.setStatus("mandatory")
_MscVrIpEgpNbrProvTable_Object = MibTable
mscVrIpEgpNbrProvTable = _MscVrIpEgpNbrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpEgpNbrProvTable.setStatus("mandatory")
_MscVrIpEgpNbrProvEntry_Object = MibTableRow
mscVrIpEgpNbrProvEntry = _MscVrIpEgpNbrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 10, 1)
)
mscVrIpEgpNbrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpNbrNeighborAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpEgpNbrProvEntry.setStatus("mandatory")


class _MscVrIpEgpNbrAsId_Type(Unsigned32):
    """Custom type mscVrIpEgpNbrAsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrIpEgpNbrAsId_Type.__name__ = "Unsigned32"
_MscVrIpEgpNbrAsId_Object = MibTableColumn
mscVrIpEgpNbrAsId = _MscVrIpEgpNbrAsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 10, 1, 1),
    _MscVrIpEgpNbrAsId_Type()
)
mscVrIpEgpNbrAsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpNbrAsId.setStatus("mandatory")


class _MscVrIpEgpNbrMode_Type(Integer32):
    """Custom type mscVrIpEgpNbrMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_MscVrIpEgpNbrMode_Type.__name__ = "Integer32"
_MscVrIpEgpNbrMode_Object = MibTableColumn
mscVrIpEgpNbrMode = _MscVrIpEgpNbrMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 10, 1, 2),
    _MscVrIpEgpNbrMode_Type()
)
mscVrIpEgpNbrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpNbrMode.setStatus("mandatory")


class _MscVrIpEgpNbrGenerateDefaultRoute_Type(Integer32):
    """Custom type mscVrIpEgpNbrGenerateDefaultRoute based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MscVrIpEgpNbrGenerateDefaultRoute_Type.__name__ = "Integer32"
_MscVrIpEgpNbrGenerateDefaultRoute_Object = MibTableColumn
mscVrIpEgpNbrGenerateDefaultRoute = _MscVrIpEgpNbrGenerateDefaultRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 10, 1, 3),
    _MscVrIpEgpNbrGenerateDefaultRoute_Type()
)
mscVrIpEgpNbrGenerateDefaultRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpNbrGenerateDefaultRoute.setStatus("mandatory")


class _MscVrIpEgpNbrDefaultRouteMetric_Type(Unsigned32):
    """Custom type mscVrIpEgpNbrDefaultRouteMetric based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrIpEgpNbrDefaultRouteMetric_Type.__name__ = "Unsigned32"
_MscVrIpEgpNbrDefaultRouteMetric_Object = MibTableColumn
mscVrIpEgpNbrDefaultRouteMetric = _MscVrIpEgpNbrDefaultRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 10, 1, 4),
    _MscVrIpEgpNbrDefaultRouteMetric_Type()
)
mscVrIpEgpNbrDefaultRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpNbrDefaultRouteMetric.setStatus("mandatory")


class _MscVrIpEgpNbrDefaultMetric_Type(Unsigned32):
    """Custom type mscVrIpEgpNbrDefaultMetric based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrIpEgpNbrDefaultMetric_Type.__name__ = "Unsigned32"
_MscVrIpEgpNbrDefaultMetric_Object = MibTableColumn
mscVrIpEgpNbrDefaultMetric = _MscVrIpEgpNbrDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 10, 1, 5),
    _MscVrIpEgpNbrDefaultMetric_Type()
)
mscVrIpEgpNbrDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpNbrDefaultMetric.setStatus("mandatory")


class _MscVrIpEgpNbrHelloInterval_Type(Unsigned32):
    """Custom type mscVrIpEgpNbrHelloInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 120),
    )


_MscVrIpEgpNbrHelloInterval_Type.__name__ = "Unsigned32"
_MscVrIpEgpNbrHelloInterval_Object = MibTableColumn
mscVrIpEgpNbrHelloInterval = _MscVrIpEgpNbrHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 10, 1, 6),
    _MscVrIpEgpNbrHelloInterval_Type()
)
mscVrIpEgpNbrHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpNbrHelloInterval.setStatus("mandatory")


class _MscVrIpEgpNbrPollInterval_Type(Unsigned32):
    """Custom type mscVrIpEgpNbrPollInterval based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 480),
    )


_MscVrIpEgpNbrPollInterval_Type.__name__ = "Unsigned32"
_MscVrIpEgpNbrPollInterval_Object = MibTableColumn
mscVrIpEgpNbrPollInterval = _MscVrIpEgpNbrPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 10, 1, 7),
    _MscVrIpEgpNbrPollInterval_Type()
)
mscVrIpEgpNbrPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpNbrPollInterval.setStatus("mandatory")
_MscVrIpEgpNbrOperTable_Object = MibTable
mscVrIpEgpNbrOperTable = _MscVrIpEgpNbrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 11)
)
if mibBuilder.loadTexts:
    mscVrIpEgpNbrOperTable.setStatus("mandatory")
_MscVrIpEgpNbrOperEntry_Object = MibTableRow
mscVrIpEgpNbrOperEntry = _MscVrIpEgpNbrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 11, 1)
)
mscVrIpEgpNbrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpNbrNeighborAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpEgpNbrOperEntry.setStatus("mandatory")


class _MscVrIpEgpNbrState_Type(Integer32):
    """Custom type mscVrIpEgpNbrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("acquisition", 2),
          ("cease", 5),
          ("down", 3),
          ("idle", 1),
          ("up", 4))
    )


_MscVrIpEgpNbrState_Type.__name__ = "Integer32"
_MscVrIpEgpNbrState_Object = MibTableColumn
mscVrIpEgpNbrState = _MscVrIpEgpNbrState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 11, 1, 1),
    _MscVrIpEgpNbrState_Type()
)
mscVrIpEgpNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpNbrState.setStatus("mandatory")
_MscVrIpEgpNbrInMsgs_Type = Counter32
_MscVrIpEgpNbrInMsgs_Object = MibTableColumn
mscVrIpEgpNbrInMsgs = _MscVrIpEgpNbrInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 11, 1, 2),
    _MscVrIpEgpNbrInMsgs_Type()
)
mscVrIpEgpNbrInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpNbrInMsgs.setStatus("mandatory")
_MscVrIpEgpNbrInErrors_Type = Counter32
_MscVrIpEgpNbrInErrors_Object = MibTableColumn
mscVrIpEgpNbrInErrors = _MscVrIpEgpNbrInErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 11, 1, 3),
    _MscVrIpEgpNbrInErrors_Type()
)
mscVrIpEgpNbrInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpNbrInErrors.setStatus("mandatory")
_MscVrIpEgpNbrOutMsgs_Type = Counter32
_MscVrIpEgpNbrOutMsgs_Object = MibTableColumn
mscVrIpEgpNbrOutMsgs = _MscVrIpEgpNbrOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 11, 1, 4),
    _MscVrIpEgpNbrOutMsgs_Type()
)
mscVrIpEgpNbrOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpNbrOutMsgs.setStatus("mandatory")
_MscVrIpEgpNbrOutErrors_Type = Counter32
_MscVrIpEgpNbrOutErrors_Object = MibTableColumn
mscVrIpEgpNbrOutErrors = _MscVrIpEgpNbrOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 11, 1, 5),
    _MscVrIpEgpNbrOutErrors_Type()
)
mscVrIpEgpNbrOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpNbrOutErrors.setStatus("mandatory")
_MscVrIpEgpNbrInErrorMsgs_Type = Counter32
_MscVrIpEgpNbrInErrorMsgs_Object = MibTableColumn
mscVrIpEgpNbrInErrorMsgs = _MscVrIpEgpNbrInErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 11, 1, 6),
    _MscVrIpEgpNbrInErrorMsgs_Type()
)
mscVrIpEgpNbrInErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpNbrInErrorMsgs.setStatus("mandatory")
_MscVrIpEgpNbrOutErrorMsgs_Type = Counter32
_MscVrIpEgpNbrOutErrorMsgs_Object = MibTableColumn
mscVrIpEgpNbrOutErrorMsgs = _MscVrIpEgpNbrOutErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 11, 1, 7),
    _MscVrIpEgpNbrOutErrorMsgs_Type()
)
mscVrIpEgpNbrOutErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpNbrOutErrorMsgs.setStatus("mandatory")
_MscVrIpEgpNbrStateUps_Type = Counter32
_MscVrIpEgpNbrStateUps_Object = MibTableColumn
mscVrIpEgpNbrStateUps = _MscVrIpEgpNbrStateUps_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 11, 1, 8),
    _MscVrIpEgpNbrStateUps_Type()
)
mscVrIpEgpNbrStateUps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpNbrStateUps.setStatus("mandatory")
_MscVrIpEgpNbrStateDowns_Type = Counter32
_MscVrIpEgpNbrStateDowns_Object = MibTableColumn
mscVrIpEgpNbrStateDowns = _MscVrIpEgpNbrStateDowns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 11, 1, 9),
    _MscVrIpEgpNbrStateDowns_Type()
)
mscVrIpEgpNbrStateDowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpNbrStateDowns.setStatus("mandatory")


class _MscVrIpEgpNbrEventTrigger_Type(Integer32):
    """Custom type mscVrIpEgpNbrEventTrigger based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_MscVrIpEgpNbrEventTrigger_Type.__name__ = "Integer32"
_MscVrIpEgpNbrEventTrigger_Object = MibTableColumn
mscVrIpEgpNbrEventTrigger = _MscVrIpEgpNbrEventTrigger_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 2, 11, 1, 10),
    _MscVrIpEgpNbrEventTrigger_Type()
)
mscVrIpEgpNbrEventTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpNbrEventTrigger.setStatus("mandatory")
_MscVrIpEgpImport_ObjectIdentity = ObjectIdentity
mscVrIpEgpImport = _MscVrIpEgpImport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 3)
)
_MscVrIpEgpImportRowStatusTable_Object = MibTable
mscVrIpEgpImportRowStatusTable = _MscVrIpEgpImportRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 3, 1)
)
if mibBuilder.loadTexts:
    mscVrIpEgpImportRowStatusTable.setStatus("mandatory")
_MscVrIpEgpImportRowStatusEntry_Object = MibTableRow
mscVrIpEgpImportRowStatusEntry = _MscVrIpEgpImportRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 3, 1, 1)
)
mscVrIpEgpImportRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpImportIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpEgpImportRowStatusEntry.setStatus("mandatory")
_MscVrIpEgpImportRowStatus_Type = RowStatus
_MscVrIpEgpImportRowStatus_Object = MibTableColumn
mscVrIpEgpImportRowStatus = _MscVrIpEgpImportRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 3, 1, 1, 1),
    _MscVrIpEgpImportRowStatus_Type()
)
mscVrIpEgpImportRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpImportRowStatus.setStatus("mandatory")
_MscVrIpEgpImportComponentName_Type = DisplayString
_MscVrIpEgpImportComponentName_Object = MibTableColumn
mscVrIpEgpImportComponentName = _MscVrIpEgpImportComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 3, 1, 1, 2),
    _MscVrIpEgpImportComponentName_Type()
)
mscVrIpEgpImportComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpImportComponentName.setStatus("mandatory")
_MscVrIpEgpImportStorageType_Type = StorageType
_MscVrIpEgpImportStorageType_Object = MibTableColumn
mscVrIpEgpImportStorageType = _MscVrIpEgpImportStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 3, 1, 1, 4),
    _MscVrIpEgpImportStorageType_Type()
)
mscVrIpEgpImportStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpImportStorageType.setStatus("mandatory")


class _MscVrIpEgpImportIndex_Type(Integer32):
    """Custom type mscVrIpEgpImportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpEgpImportIndex_Type.__name__ = "Integer32"
_MscVrIpEgpImportIndex_Object = MibTableColumn
mscVrIpEgpImportIndex = _MscVrIpEgpImportIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 3, 1, 1, 10),
    _MscVrIpEgpImportIndex_Type()
)
mscVrIpEgpImportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpEgpImportIndex.setStatus("mandatory")
_MscVrIpEgpImportNet_ObjectIdentity = ObjectIdentity
mscVrIpEgpImportNet = _MscVrIpEgpImportNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 3, 2)
)
_MscVrIpEgpImportNetRowStatusTable_Object = MibTable
mscVrIpEgpImportNetRowStatusTable = _MscVrIpEgpImportNetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpEgpImportNetRowStatusTable.setStatus("mandatory")
_MscVrIpEgpImportNetRowStatusEntry_Object = MibTableRow
mscVrIpEgpImportNetRowStatusEntry = _MscVrIpEgpImportNetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 3, 2, 1, 1)
)
mscVrIpEgpImportNetRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpImportIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpImportNetIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpEgpImportNetRowStatusEntry.setStatus("mandatory")
_MscVrIpEgpImportNetRowStatus_Type = RowStatus
_MscVrIpEgpImportNetRowStatus_Object = MibTableColumn
mscVrIpEgpImportNetRowStatus = _MscVrIpEgpImportNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 3, 2, 1, 1, 1),
    _MscVrIpEgpImportNetRowStatus_Type()
)
mscVrIpEgpImportNetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpImportNetRowStatus.setStatus("mandatory")
_MscVrIpEgpImportNetComponentName_Type = DisplayString
_MscVrIpEgpImportNetComponentName_Object = MibTableColumn
mscVrIpEgpImportNetComponentName = _MscVrIpEgpImportNetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 3, 2, 1, 1, 2),
    _MscVrIpEgpImportNetComponentName_Type()
)
mscVrIpEgpImportNetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpImportNetComponentName.setStatus("mandatory")
_MscVrIpEgpImportNetStorageType_Type = StorageType
_MscVrIpEgpImportNetStorageType_Object = MibTableColumn
mscVrIpEgpImportNetStorageType = _MscVrIpEgpImportNetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 3, 2, 1, 1, 4),
    _MscVrIpEgpImportNetStorageType_Type()
)
mscVrIpEgpImportNetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpImportNetStorageType.setStatus("mandatory")


class _MscVrIpEgpImportNetIndex_Type(Integer32):
    """Custom type mscVrIpEgpImportNetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpEgpImportNetIndex_Type.__name__ = "Integer32"
_MscVrIpEgpImportNetIndex_Object = MibTableColumn
mscVrIpEgpImportNetIndex = _MscVrIpEgpImportNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 3, 2, 1, 1, 10),
    _MscVrIpEgpImportNetIndex_Type()
)
mscVrIpEgpImportNetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpEgpImportNetIndex.setStatus("mandatory")
_MscVrIpEgpImportNetProvTable_Object = MibTable
mscVrIpEgpImportNetProvTable = _MscVrIpEgpImportNetProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpEgpImportNetProvTable.setStatus("mandatory")
_MscVrIpEgpImportNetProvEntry_Object = MibTableRow
mscVrIpEgpImportNetProvEntry = _MscVrIpEgpImportNetProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 3, 2, 10, 1)
)
mscVrIpEgpImportNetProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpImportIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpImportNetIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpEgpImportNetProvEntry.setStatus("mandatory")
_MscVrIpEgpImportNetIpAddress_Type = IpAddress
_MscVrIpEgpImportNetIpAddress_Object = MibTableColumn
mscVrIpEgpImportNetIpAddress = _MscVrIpEgpImportNetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 3, 2, 10, 1, 1),
    _MscVrIpEgpImportNetIpAddress_Type()
)
mscVrIpEgpImportNetIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpImportNetIpAddress.setStatus("mandatory")
_MscVrIpEgpImportProvTable_Object = MibTable
mscVrIpEgpImportProvTable = _MscVrIpEgpImportProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 3, 10)
)
if mibBuilder.loadTexts:
    mscVrIpEgpImportProvTable.setStatus("mandatory")
_MscVrIpEgpImportProvEntry_Object = MibTableRow
mscVrIpEgpImportProvEntry = _MscVrIpEgpImportProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 3, 10, 1)
)
mscVrIpEgpImportProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpImportIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpEgpImportProvEntry.setStatus("mandatory")


class _MscVrIpEgpImportUsageFlag_Type(Integer32):
    """Custom type mscVrIpEgpImportUsageFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 2),
          ("use", 1))
    )


_MscVrIpEgpImportUsageFlag_Type.__name__ = "Integer32"
_MscVrIpEgpImportUsageFlag_Object = MibTableColumn
mscVrIpEgpImportUsageFlag = _MscVrIpEgpImportUsageFlag_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 3, 10, 1, 1),
    _MscVrIpEgpImportUsageFlag_Type()
)
mscVrIpEgpImportUsageFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpImportUsageFlag.setStatus("mandatory")


class _MscVrIpEgpImportImportMetric_Type(Unsigned32):
    """Custom type mscVrIpEgpImportImportMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrIpEgpImportImportMetric_Type.__name__ = "Unsigned32"
_MscVrIpEgpImportImportMetric_Object = MibTableColumn
mscVrIpEgpImportImportMetric = _MscVrIpEgpImportImportMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 3, 10, 1, 2),
    _MscVrIpEgpImportImportMetric_Type()
)
mscVrIpEgpImportImportMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpImportImportMetric.setStatus("mandatory")


class _MscVrIpEgpImportNbrAsId_Type(Unsigned32):
    """Custom type mscVrIpEgpImportNbrAsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpEgpImportNbrAsId_Type.__name__ = "Unsigned32"
_MscVrIpEgpImportNbrAsId_Object = MibTableColumn
mscVrIpEgpImportNbrAsId = _MscVrIpEgpImportNbrAsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 3, 10, 1, 3),
    _MscVrIpEgpImportNbrAsId_Type()
)
mscVrIpEgpImportNbrAsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpImportNbrAsId.setStatus("mandatory")
_MscVrIpEgpExport_ObjectIdentity = ObjectIdentity
mscVrIpEgpExport = _MscVrIpEgpExport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4)
)
_MscVrIpEgpExportRowStatusTable_Object = MibTable
mscVrIpEgpExportRowStatusTable = _MscVrIpEgpExportRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4, 1)
)
if mibBuilder.loadTexts:
    mscVrIpEgpExportRowStatusTable.setStatus("mandatory")
_MscVrIpEgpExportRowStatusEntry_Object = MibTableRow
mscVrIpEgpExportRowStatusEntry = _MscVrIpEgpExportRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4, 1, 1)
)
mscVrIpEgpExportRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpExportIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpEgpExportRowStatusEntry.setStatus("mandatory")
_MscVrIpEgpExportRowStatus_Type = RowStatus
_MscVrIpEgpExportRowStatus_Object = MibTableColumn
mscVrIpEgpExportRowStatus = _MscVrIpEgpExportRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4, 1, 1, 1),
    _MscVrIpEgpExportRowStatus_Type()
)
mscVrIpEgpExportRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpExportRowStatus.setStatus("mandatory")
_MscVrIpEgpExportComponentName_Type = DisplayString
_MscVrIpEgpExportComponentName_Object = MibTableColumn
mscVrIpEgpExportComponentName = _MscVrIpEgpExportComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4, 1, 1, 2),
    _MscVrIpEgpExportComponentName_Type()
)
mscVrIpEgpExportComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpExportComponentName.setStatus("mandatory")
_MscVrIpEgpExportStorageType_Type = StorageType
_MscVrIpEgpExportStorageType_Object = MibTableColumn
mscVrIpEgpExportStorageType = _MscVrIpEgpExportStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4, 1, 1, 4),
    _MscVrIpEgpExportStorageType_Type()
)
mscVrIpEgpExportStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpExportStorageType.setStatus("mandatory")


class _MscVrIpEgpExportIndex_Type(Integer32):
    """Custom type mscVrIpEgpExportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpEgpExportIndex_Type.__name__ = "Integer32"
_MscVrIpEgpExportIndex_Object = MibTableColumn
mscVrIpEgpExportIndex = _MscVrIpEgpExportIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4, 1, 1, 10),
    _MscVrIpEgpExportIndex_Type()
)
mscVrIpEgpExportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpEgpExportIndex.setStatus("mandatory")
_MscVrIpEgpExportNet_ObjectIdentity = ObjectIdentity
mscVrIpEgpExportNet = _MscVrIpEgpExportNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4, 2)
)
_MscVrIpEgpExportNetRowStatusTable_Object = MibTable
mscVrIpEgpExportNetRowStatusTable = _MscVrIpEgpExportNetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpEgpExportNetRowStatusTable.setStatus("mandatory")
_MscVrIpEgpExportNetRowStatusEntry_Object = MibTableRow
mscVrIpEgpExportNetRowStatusEntry = _MscVrIpEgpExportNetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4, 2, 1, 1)
)
mscVrIpEgpExportNetRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpExportIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpExportNetIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpEgpExportNetRowStatusEntry.setStatus("mandatory")
_MscVrIpEgpExportNetRowStatus_Type = RowStatus
_MscVrIpEgpExportNetRowStatus_Object = MibTableColumn
mscVrIpEgpExportNetRowStatus = _MscVrIpEgpExportNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4, 2, 1, 1, 1),
    _MscVrIpEgpExportNetRowStatus_Type()
)
mscVrIpEgpExportNetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpExportNetRowStatus.setStatus("mandatory")
_MscVrIpEgpExportNetComponentName_Type = DisplayString
_MscVrIpEgpExportNetComponentName_Object = MibTableColumn
mscVrIpEgpExportNetComponentName = _MscVrIpEgpExportNetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4, 2, 1, 1, 2),
    _MscVrIpEgpExportNetComponentName_Type()
)
mscVrIpEgpExportNetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpExportNetComponentName.setStatus("mandatory")
_MscVrIpEgpExportNetStorageType_Type = StorageType
_MscVrIpEgpExportNetStorageType_Object = MibTableColumn
mscVrIpEgpExportNetStorageType = _MscVrIpEgpExportNetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4, 2, 1, 1, 4),
    _MscVrIpEgpExportNetStorageType_Type()
)
mscVrIpEgpExportNetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpExportNetStorageType.setStatus("mandatory")


class _MscVrIpEgpExportNetIndex_Type(Integer32):
    """Custom type mscVrIpEgpExportNetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpEgpExportNetIndex_Type.__name__ = "Integer32"
_MscVrIpEgpExportNetIndex_Object = MibTableColumn
mscVrIpEgpExportNetIndex = _MscVrIpEgpExportNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4, 2, 1, 1, 10),
    _MscVrIpEgpExportNetIndex_Type()
)
mscVrIpEgpExportNetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpEgpExportNetIndex.setStatus("mandatory")
_MscVrIpEgpExportNetProvTable_Object = MibTable
mscVrIpEgpExportNetProvTable = _MscVrIpEgpExportNetProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpEgpExportNetProvTable.setStatus("mandatory")
_MscVrIpEgpExportNetProvEntry_Object = MibTableRow
mscVrIpEgpExportNetProvEntry = _MscVrIpEgpExportNetProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4, 2, 10, 1)
)
mscVrIpEgpExportNetProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpExportIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpExportNetIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpEgpExportNetProvEntry.setStatus("mandatory")
_MscVrIpEgpExportNetIpAddress_Type = IpAddress
_MscVrIpEgpExportNetIpAddress_Object = MibTableColumn
mscVrIpEgpExportNetIpAddress = _MscVrIpEgpExportNetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4, 2, 10, 1, 1),
    _MscVrIpEgpExportNetIpAddress_Type()
)
mscVrIpEgpExportNetIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpExportNetIpAddress.setStatus("mandatory")
_MscVrIpEgpExportProvTable_Object = MibTable
mscVrIpEgpExportProvTable = _MscVrIpEgpExportProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4, 10)
)
if mibBuilder.loadTexts:
    mscVrIpEgpExportProvTable.setStatus("mandatory")
_MscVrIpEgpExportProvEntry_Object = MibTableRow
mscVrIpEgpExportProvEntry = _MscVrIpEgpExportProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4, 10, 1)
)
mscVrIpEgpExportProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpExportIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpEgpExportProvEntry.setStatus("mandatory")


class _MscVrIpEgpExportAdvertiseStatus_Type(Integer32):
    """Custom type mscVrIpEgpExportAdvertiseStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("send", 1))
    )


_MscVrIpEgpExportAdvertiseStatus_Type.__name__ = "Integer32"
_MscVrIpEgpExportAdvertiseStatus_Object = MibTableColumn
mscVrIpEgpExportAdvertiseStatus = _MscVrIpEgpExportAdvertiseStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4, 10, 1, 1),
    _MscVrIpEgpExportAdvertiseStatus_Type()
)
mscVrIpEgpExportAdvertiseStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpExportAdvertiseStatus.setStatus("mandatory")


class _MscVrIpEgpExportExportMetric_Type(Unsigned32):
    """Custom type mscVrIpEgpExportExportMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrIpEgpExportExportMetric_Type.__name__ = "Unsigned32"
_MscVrIpEgpExportExportMetric_Object = MibTableColumn
mscVrIpEgpExportExportMetric = _MscVrIpEgpExportExportMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4, 10, 1, 2),
    _MscVrIpEgpExportExportMetric_Type()
)
mscVrIpEgpExportExportMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpExportExportMetric.setStatus("mandatory")


class _MscVrIpEgpExportProtocol_Type(Integer32):
    """Custom type mscVrIpEgpExportProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("egp", 2),
          ("ospfExternal", 5),
          ("ospfInternal", 4),
          ("rip", 3),
          ("staticLocal", 6),
          ("staticRemote", 7))
    )


_MscVrIpEgpExportProtocol_Type.__name__ = "Integer32"
_MscVrIpEgpExportProtocol_Object = MibTableColumn
mscVrIpEgpExportProtocol = _MscVrIpEgpExportProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4, 10, 1, 3),
    _MscVrIpEgpExportProtocol_Type()
)
mscVrIpEgpExportProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpExportProtocol.setStatus("mandatory")


class _MscVrIpEgpExportRipInterface_Type(IpAddress):
    """Custom type mscVrIpEgpExportRipInterface based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrIpEgpExportRipInterface_Object = MibTableColumn
mscVrIpEgpExportRipInterface = _MscVrIpEgpExportRipInterface_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4, 10, 1, 4),
    _MscVrIpEgpExportRipInterface_Type()
)
mscVrIpEgpExportRipInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpExportRipInterface.setStatus("mandatory")


class _MscVrIpEgpExportRipNeighbor_Type(IpAddress):
    """Custom type mscVrIpEgpExportRipNeighbor based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrIpEgpExportRipNeighbor_Object = MibTableColumn
mscVrIpEgpExportRipNeighbor = _MscVrIpEgpExportRipNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4, 10, 1, 5),
    _MscVrIpEgpExportRipNeighbor_Type()
)
mscVrIpEgpExportRipNeighbor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpExportRipNeighbor.setStatus("mandatory")


class _MscVrIpEgpExportInEgpAsId_Type(Unsigned32):
    """Custom type mscVrIpEgpExportInEgpAsId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpEgpExportInEgpAsId_Type.__name__ = "Unsigned32"
_MscVrIpEgpExportInEgpAsId_Object = MibTableColumn
mscVrIpEgpExportInEgpAsId = _MscVrIpEgpExportInEgpAsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4, 10, 1, 6),
    _MscVrIpEgpExportInEgpAsId_Type()
)
mscVrIpEgpExportInEgpAsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpExportInEgpAsId.setStatus("mandatory")


class _MscVrIpEgpExportOspfTag_Type(Unsigned32):
    """Custom type mscVrIpEgpExportOspfTag based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpEgpExportOspfTag_Type.__name__ = "Unsigned32"
_MscVrIpEgpExportOspfTag_Object = MibTableColumn
mscVrIpEgpExportOspfTag = _MscVrIpEgpExportOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4, 10, 1, 7),
    _MscVrIpEgpExportOspfTag_Type()
)
mscVrIpEgpExportOspfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpExportOspfTag.setStatus("mandatory")


class _MscVrIpEgpExportOutAutonomousSystem_Type(Unsigned32):
    """Custom type mscVrIpEgpExportOutAutonomousSystem based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpEgpExportOutAutonomousSystem_Type.__name__ = "Unsigned32"
_MscVrIpEgpExportOutAutonomousSystem_Object = MibTableColumn
mscVrIpEgpExportOutAutonomousSystem = _MscVrIpEgpExportOutAutonomousSystem_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 4, 10, 1, 8),
    _MscVrIpEgpExportOutAutonomousSystem_Type()
)
mscVrIpEgpExportOutAutonomousSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpExportOutAutonomousSystem.setStatus("mandatory")
_MscVrIpEgpProvTable_Object = MibTable
mscVrIpEgpProvTable = _MscVrIpEgpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 10)
)
if mibBuilder.loadTexts:
    mscVrIpEgpProvTable.setStatus("mandatory")
_MscVrIpEgpProvEntry_Object = MibTableRow
mscVrIpEgpProvEntry = _MscVrIpEgpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 10, 1)
)
mscVrIpEgpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpEgpProvEntry.setStatus("mandatory")


class _MscVrIpEgpAsId_Type(Unsigned32):
    """Custom type mscVrIpEgpAsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrIpEgpAsId_Type.__name__ = "Unsigned32"
_MscVrIpEgpAsId_Object = MibTableColumn
mscVrIpEgpAsId = _MscVrIpEgpAsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 10, 1, 2),
    _MscVrIpEgpAsId_Type()
)
mscVrIpEgpAsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpAsId.setStatus("mandatory")


class _MscVrIpEgpDefaultHelloInterval_Type(Unsigned32):
    """Custom type mscVrIpEgpDefaultHelloInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 900),
    )


_MscVrIpEgpDefaultHelloInterval_Type.__name__ = "Unsigned32"
_MscVrIpEgpDefaultHelloInterval_Object = MibTableColumn
mscVrIpEgpDefaultHelloInterval = _MscVrIpEgpDefaultHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 10, 1, 3),
    _MscVrIpEgpDefaultHelloInterval_Type()
)
mscVrIpEgpDefaultHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpDefaultHelloInterval.setStatus("mandatory")


class _MscVrIpEgpDefaultPollInterval_Type(Unsigned32):
    """Custom type mscVrIpEgpDefaultPollInterval based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 3600),
    )


_MscVrIpEgpDefaultPollInterval_Type.__name__ = "Unsigned32"
_MscVrIpEgpDefaultPollInterval_Object = MibTableColumn
mscVrIpEgpDefaultPollInterval = _MscVrIpEgpDefaultPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 10, 1, 4),
    _MscVrIpEgpDefaultPollInterval_Type()
)
mscVrIpEgpDefaultPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpDefaultPollInterval.setStatus("mandatory")


class _MscVrIpEgpMaxNatNets_Type(Unsigned32):
    """Custom type mscVrIpEgpMaxNatNets based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrIpEgpMaxNatNets_Type.__name__ = "Unsigned32"
_MscVrIpEgpMaxNatNets_Object = MibTableColumn
mscVrIpEgpMaxNatNets = _MscVrIpEgpMaxNatNets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 10, 1, 5),
    _MscVrIpEgpMaxNatNets_Type()
)
mscVrIpEgpMaxNatNets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpMaxNatNets.setStatus("mandatory")


class _MscVrIpEgpMaxBufferSize_Type(Unsigned32):
    """Custom type mscVrIpEgpMaxBufferSize based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 16),
    )


_MscVrIpEgpMaxBufferSize_Type.__name__ = "Unsigned32"
_MscVrIpEgpMaxBufferSize_Object = MibTableColumn
mscVrIpEgpMaxBufferSize = _MscVrIpEgpMaxBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 10, 1, 6),
    _MscVrIpEgpMaxBufferSize_Type()
)
mscVrIpEgpMaxBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpMaxBufferSize.setStatus("mandatory")
_MscVrIpEgpStatsTable_Object = MibTable
mscVrIpEgpStatsTable = _MscVrIpEgpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 11)
)
if mibBuilder.loadTexts:
    mscVrIpEgpStatsTable.setStatus("mandatory")
_MscVrIpEgpStatsEntry_Object = MibTableRow
mscVrIpEgpStatsEntry = _MscVrIpEgpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 11, 1)
)
mscVrIpEgpStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpEgpStatsEntry.setStatus("mandatory")
_MscVrIpEgpInMsgs_Type = Counter32
_MscVrIpEgpInMsgs_Object = MibTableColumn
mscVrIpEgpInMsgs = _MscVrIpEgpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 11, 1, 1),
    _MscVrIpEgpInMsgs_Type()
)
mscVrIpEgpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpInMsgs.setStatus("mandatory")
_MscVrIpEgpInErrorMsgs_Type = Counter32
_MscVrIpEgpInErrorMsgs_Object = MibTableColumn
mscVrIpEgpInErrorMsgs = _MscVrIpEgpInErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 11, 1, 2),
    _MscVrIpEgpInErrorMsgs_Type()
)
mscVrIpEgpInErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpInErrorMsgs.setStatus("mandatory")
_MscVrIpEgpOutErrorMsgs_Type = Counter32
_MscVrIpEgpOutErrorMsgs_Object = MibTableColumn
mscVrIpEgpOutErrorMsgs = _MscVrIpEgpOutErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 11, 1, 3),
    _MscVrIpEgpOutErrorMsgs_Type()
)
mscVrIpEgpOutErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpOutErrorMsgs.setStatus("mandatory")
_MscVrIpEgpInErrors_Type = Counter32
_MscVrIpEgpInErrors_Object = MibTableColumn
mscVrIpEgpInErrors = _MscVrIpEgpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 11, 1, 4),
    _MscVrIpEgpInErrors_Type()
)
mscVrIpEgpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpInErrors.setStatus("mandatory")
_MscVrIpEgpOutMsgs_Type = Counter32
_MscVrIpEgpOutMsgs_Object = MibTableColumn
mscVrIpEgpOutMsgs = _MscVrIpEgpOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 11, 1, 5),
    _MscVrIpEgpOutMsgs_Type()
)
mscVrIpEgpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpOutMsgs.setStatus("mandatory")
_MscVrIpEgpOutErrors_Type = Counter32
_MscVrIpEgpOutErrors_Object = MibTableColumn
mscVrIpEgpOutErrors = _MscVrIpEgpOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 11, 1, 6),
    _MscVrIpEgpOutErrors_Type()
)
mscVrIpEgpOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpOutErrors.setStatus("mandatory")
_MscVrIpEgpStateTable_Object = MibTable
mscVrIpEgpStateTable = _MscVrIpEgpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 12)
)
if mibBuilder.loadTexts:
    mscVrIpEgpStateTable.setStatus("mandatory")
_MscVrIpEgpStateEntry_Object = MibTableRow
mscVrIpEgpStateEntry = _MscVrIpEgpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 12, 1)
)
mscVrIpEgpStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpEgpStateEntry.setStatus("mandatory")


class _MscVrIpEgpAdminState_Type(Integer32):
    """Custom type mscVrIpEgpAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_MscVrIpEgpAdminState_Type.__name__ = "Integer32"
_MscVrIpEgpAdminState_Object = MibTableColumn
mscVrIpEgpAdminState = _MscVrIpEgpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 12, 1, 1),
    _MscVrIpEgpAdminState_Type()
)
mscVrIpEgpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpAdminState.setStatus("mandatory")


class _MscVrIpEgpOperationalState_Type(Integer32):
    """Custom type mscVrIpEgpOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MscVrIpEgpOperationalState_Type.__name__ = "Integer32"
_MscVrIpEgpOperationalState_Object = MibTableColumn
mscVrIpEgpOperationalState = _MscVrIpEgpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 12, 1, 2),
    _MscVrIpEgpOperationalState_Type()
)
mscVrIpEgpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpOperationalState.setStatus("mandatory")


class _MscVrIpEgpUsageState_Type(Integer32):
    """Custom type mscVrIpEgpUsageState based on Integer32"""
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
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_MscVrIpEgpUsageState_Type.__name__ = "Integer32"
_MscVrIpEgpUsageState_Object = MibTableColumn
mscVrIpEgpUsageState = _MscVrIpEgpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 12, 1, 3),
    _MscVrIpEgpUsageState_Type()
)
mscVrIpEgpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpUsageState.setStatus("mandatory")
_MscVrIpEgpAdminControlTable_Object = MibTable
mscVrIpEgpAdminControlTable = _MscVrIpEgpAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 13)
)
if mibBuilder.loadTexts:
    mscVrIpEgpAdminControlTable.setStatus("mandatory")
_MscVrIpEgpAdminControlEntry_Object = MibTableRow
mscVrIpEgpAdminControlEntry = _MscVrIpEgpAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 13, 1)
)
mscVrIpEgpAdminControlEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpEgpAdminControlEntry.setStatus("mandatory")


class _MscVrIpEgpSnmpAdminStatus_Type(Integer32):
    """Custom type mscVrIpEgpSnmpAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscVrIpEgpSnmpAdminStatus_Type.__name__ = "Integer32"
_MscVrIpEgpSnmpAdminStatus_Object = MibTableColumn
mscVrIpEgpSnmpAdminStatus = _MscVrIpEgpSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 13, 1, 1),
    _MscVrIpEgpSnmpAdminStatus_Type()
)
mscVrIpEgpSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpEgpSnmpAdminStatus.setStatus("mandatory")
_MscVrIpEgpOperStatusTable_Object = MibTable
mscVrIpEgpOperStatusTable = _MscVrIpEgpOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 16)
)
if mibBuilder.loadTexts:
    mscVrIpEgpOperStatusTable.setStatus("mandatory")
_MscVrIpEgpOperStatusEntry_Object = MibTableRow
mscVrIpEgpOperStatusEntry = _MscVrIpEgpOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 16, 1)
)
mscVrIpEgpOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpEgpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpEgpOperStatusEntry.setStatus("mandatory")


class _MscVrIpEgpSnmpOperStatus_Type(Integer32):
    """Custom type mscVrIpEgpSnmpOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscVrIpEgpSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrIpEgpSnmpOperStatus_Object = MibTableColumn
mscVrIpEgpSnmpOperStatus = _MscVrIpEgpSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 6, 16, 1, 1),
    _MscVrIpEgpSnmpOperStatus_Type()
)
mscVrIpEgpSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpEgpSnmpOperStatus.setStatus("mandatory")
_MscVrIpOspf_ObjectIdentity = ObjectIdentity
mscVrIpOspf = _MscVrIpOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7)
)
_MscVrIpOspfRowStatusTable_Object = MibTable
mscVrIpOspfRowStatusTable = _MscVrIpOspfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 1)
)
if mibBuilder.loadTexts:
    mscVrIpOspfRowStatusTable.setStatus("mandatory")
_MscVrIpOspfRowStatusEntry_Object = MibTableRow
mscVrIpOspfRowStatusEntry = _MscVrIpOspfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 1, 1)
)
mscVrIpOspfRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfRowStatusEntry.setStatus("mandatory")
_MscVrIpOspfRowStatus_Type = RowStatus
_MscVrIpOspfRowStatus_Object = MibTableColumn
mscVrIpOspfRowStatus = _MscVrIpOspfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 1, 1, 1),
    _MscVrIpOspfRowStatus_Type()
)
mscVrIpOspfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfRowStatus.setStatus("mandatory")
_MscVrIpOspfComponentName_Type = DisplayString
_MscVrIpOspfComponentName_Object = MibTableColumn
mscVrIpOspfComponentName = _MscVrIpOspfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 1, 1, 2),
    _MscVrIpOspfComponentName_Type()
)
mscVrIpOspfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfComponentName.setStatus("mandatory")
_MscVrIpOspfStorageType_Type = StorageType
_MscVrIpOspfStorageType_Object = MibTableColumn
mscVrIpOspfStorageType = _MscVrIpOspfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 1, 1, 4),
    _MscVrIpOspfStorageType_Type()
)
mscVrIpOspfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfStorageType.setStatus("mandatory")
_MscVrIpOspfIndex_Type = NonReplicated
_MscVrIpOspfIndex_Object = MibTableColumn
mscVrIpOspfIndex = _MscVrIpOspfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 1, 1, 10),
    _MscVrIpOspfIndex_Type()
)
mscVrIpOspfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpOspfIndex.setStatus("mandatory")
_MscVrIpOspfArea_ObjectIdentity = ObjectIdentity
mscVrIpOspfArea = _MscVrIpOspfArea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 2)
)
_MscVrIpOspfAreaRowStatusTable_Object = MibTable
mscVrIpOspfAreaRowStatusTable = _MscVrIpOspfAreaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpOspfAreaRowStatusTable.setStatus("mandatory")
_MscVrIpOspfAreaRowStatusEntry_Object = MibTableRow
mscVrIpOspfAreaRowStatusEntry = _MscVrIpOspfAreaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 2, 1, 1)
)
mscVrIpOspfAreaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfAreaAreaIdIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfAreaRowStatusEntry.setStatus("mandatory")
_MscVrIpOspfAreaRowStatus_Type = RowStatus
_MscVrIpOspfAreaRowStatus_Object = MibTableColumn
mscVrIpOspfAreaRowStatus = _MscVrIpOspfAreaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 2, 1, 1, 1),
    _MscVrIpOspfAreaRowStatus_Type()
)
mscVrIpOspfAreaRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfAreaRowStatus.setStatus("mandatory")
_MscVrIpOspfAreaComponentName_Type = DisplayString
_MscVrIpOspfAreaComponentName_Object = MibTableColumn
mscVrIpOspfAreaComponentName = _MscVrIpOspfAreaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 2, 1, 1, 2),
    _MscVrIpOspfAreaComponentName_Type()
)
mscVrIpOspfAreaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfAreaComponentName.setStatus("mandatory")
_MscVrIpOspfAreaStorageType_Type = StorageType
_MscVrIpOspfAreaStorageType_Object = MibTableColumn
mscVrIpOspfAreaStorageType = _MscVrIpOspfAreaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 2, 1, 1, 4),
    _MscVrIpOspfAreaStorageType_Type()
)
mscVrIpOspfAreaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfAreaStorageType.setStatus("mandatory")
_MscVrIpOspfAreaAreaIdIndex_Type = IpAddress
_MscVrIpOspfAreaAreaIdIndex_Object = MibTableColumn
mscVrIpOspfAreaAreaIdIndex = _MscVrIpOspfAreaAreaIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 2, 1, 1, 10),
    _MscVrIpOspfAreaAreaIdIndex_Type()
)
mscVrIpOspfAreaAreaIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpOspfAreaAreaIdIndex.setStatus("mandatory")
_MscVrIpOspfAreaProvTable_Object = MibTable
mscVrIpOspfAreaProvTable = _MscVrIpOspfAreaProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpOspfAreaProvTable.setStatus("mandatory")
_MscVrIpOspfAreaProvEntry_Object = MibTableRow
mscVrIpOspfAreaProvEntry = _MscVrIpOspfAreaProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 2, 10, 1)
)
mscVrIpOspfAreaProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfAreaAreaIdIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfAreaProvEntry.setStatus("mandatory")


class _MscVrIpOspfAreaAuthType_Type(Integer32):
    """Custom type mscVrIpOspfAreaAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("simplePassword", 1))
    )


_MscVrIpOspfAreaAuthType_Type.__name__ = "Integer32"
_MscVrIpOspfAreaAuthType_Object = MibTableColumn
mscVrIpOspfAreaAuthType = _MscVrIpOspfAreaAuthType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 2, 10, 1, 1),
    _MscVrIpOspfAreaAuthType_Type()
)
mscVrIpOspfAreaAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfAreaAuthType.setStatus("mandatory")


class _MscVrIpOspfAreaImportAsExtern_Type(Integer32):
    """Custom type mscVrIpOspfAreaImportAsExtern based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("importExternal", 1),
          ("importNoExternal", 2),
          ("importNssa", 3))
    )


_MscVrIpOspfAreaImportAsExtern_Type.__name__ = "Integer32"
_MscVrIpOspfAreaImportAsExtern_Object = MibTableColumn
mscVrIpOspfAreaImportAsExtern = _MscVrIpOspfAreaImportAsExtern_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 2, 10, 1, 2),
    _MscVrIpOspfAreaImportAsExtern_Type()
)
mscVrIpOspfAreaImportAsExtern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfAreaImportAsExtern.setStatus("mandatory")


class _MscVrIpOspfAreaAreaSummary_Type(Integer32):
    """Custom type mscVrIpOspfAreaAreaSummary based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAreaSummary", 1),
          ("sendAreaSummary", 2))
    )


_MscVrIpOspfAreaAreaSummary_Type.__name__ = "Integer32"
_MscVrIpOspfAreaAreaSummary_Object = MibTableColumn
mscVrIpOspfAreaAreaSummary = _MscVrIpOspfAreaAreaSummary_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 2, 10, 1, 3),
    _MscVrIpOspfAreaAreaSummary_Type()
)
mscVrIpOspfAreaAreaSummary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfAreaAreaSummary.setStatus("mandatory")
_MscVrIpOspfAreaOperTable_Object = MibTable
mscVrIpOspfAreaOperTable = _MscVrIpOspfAreaOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 2, 11)
)
if mibBuilder.loadTexts:
    mscVrIpOspfAreaOperTable.setStatus("mandatory")
_MscVrIpOspfAreaOperEntry_Object = MibTableRow
mscVrIpOspfAreaOperEntry = _MscVrIpOspfAreaOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 2, 11, 1)
)
mscVrIpOspfAreaOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfAreaAreaIdIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfAreaOperEntry.setStatus("mandatory")
_MscVrIpOspfAreaSpfRuns_Type = Counter32
_MscVrIpOspfAreaSpfRuns_Object = MibTableColumn
mscVrIpOspfAreaSpfRuns = _MscVrIpOspfAreaSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 2, 11, 1, 1),
    _MscVrIpOspfAreaSpfRuns_Type()
)
mscVrIpOspfAreaSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfAreaSpfRuns.setStatus("mandatory")


class _MscVrIpOspfAreaAreaBdrRtrCount_Type(Gauge32):
    """Custom type mscVrIpOspfAreaAreaBdrRtrCount based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpOspfAreaAreaBdrRtrCount_Type.__name__ = "Gauge32"
_MscVrIpOspfAreaAreaBdrRtrCount_Object = MibTableColumn
mscVrIpOspfAreaAreaBdrRtrCount = _MscVrIpOspfAreaAreaBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 2, 11, 1, 2),
    _MscVrIpOspfAreaAreaBdrRtrCount_Type()
)
mscVrIpOspfAreaAreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfAreaAreaBdrRtrCount.setStatus("mandatory")


class _MscVrIpOspfAreaAsBdrRtrCount_Type(Gauge32):
    """Custom type mscVrIpOspfAreaAsBdrRtrCount based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpOspfAreaAsBdrRtrCount_Type.__name__ = "Gauge32"
_MscVrIpOspfAreaAsBdrRtrCount_Object = MibTableColumn
mscVrIpOspfAreaAsBdrRtrCount = _MscVrIpOspfAreaAsBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 2, 11, 1, 3),
    _MscVrIpOspfAreaAsBdrRtrCount_Type()
)
mscVrIpOspfAreaAsBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfAreaAsBdrRtrCount.setStatus("mandatory")


class _MscVrIpOspfAreaLsaCount_Type(Gauge32):
    """Custom type mscVrIpOspfAreaLsaCount based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpOspfAreaLsaCount_Type.__name__ = "Gauge32"
_MscVrIpOspfAreaLsaCount_Object = MibTableColumn
mscVrIpOspfAreaLsaCount = _MscVrIpOspfAreaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 2, 11, 1, 4),
    _MscVrIpOspfAreaLsaCount_Type()
)
mscVrIpOspfAreaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfAreaLsaCount.setStatus("mandatory")


class _MscVrIpOspfAreaAreaLsaCksumSum_Type(Unsigned32):
    """Custom type mscVrIpOspfAreaAreaLsaCksumSum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpOspfAreaAreaLsaCksumSum_Type.__name__ = "Unsigned32"
_MscVrIpOspfAreaAreaLsaCksumSum_Object = MibTableColumn
mscVrIpOspfAreaAreaLsaCksumSum = _MscVrIpOspfAreaAreaLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 2, 11, 1, 5),
    _MscVrIpOspfAreaAreaLsaCksumSum_Type()
)
mscVrIpOspfAreaAreaLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfAreaAreaLsaCksumSum.setStatus("mandatory")
_MscVrIpOspfStub_ObjectIdentity = ObjectIdentity
mscVrIpOspfStub = _MscVrIpOspfStub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 3)
)
_MscVrIpOspfStubRowStatusTable_Object = MibTable
mscVrIpOspfStubRowStatusTable = _MscVrIpOspfStubRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 3, 1)
)
if mibBuilder.loadTexts:
    mscVrIpOspfStubRowStatusTable.setStatus("mandatory")
_MscVrIpOspfStubRowStatusEntry_Object = MibTableRow
mscVrIpOspfStubRowStatusEntry = _MscVrIpOspfStubRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 3, 1, 1)
)
mscVrIpOspfStubRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfStubAreaIdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfStubTosIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfStubRowStatusEntry.setStatus("mandatory")
_MscVrIpOspfStubRowStatus_Type = RowStatus
_MscVrIpOspfStubRowStatus_Object = MibTableColumn
mscVrIpOspfStubRowStatus = _MscVrIpOspfStubRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 3, 1, 1, 1),
    _MscVrIpOspfStubRowStatus_Type()
)
mscVrIpOspfStubRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfStubRowStatus.setStatus("mandatory")
_MscVrIpOspfStubComponentName_Type = DisplayString
_MscVrIpOspfStubComponentName_Object = MibTableColumn
mscVrIpOspfStubComponentName = _MscVrIpOspfStubComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 3, 1, 1, 2),
    _MscVrIpOspfStubComponentName_Type()
)
mscVrIpOspfStubComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfStubComponentName.setStatus("mandatory")
_MscVrIpOspfStubStorageType_Type = StorageType
_MscVrIpOspfStubStorageType_Object = MibTableColumn
mscVrIpOspfStubStorageType = _MscVrIpOspfStubStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 3, 1, 1, 4),
    _MscVrIpOspfStubStorageType_Type()
)
mscVrIpOspfStubStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfStubStorageType.setStatus("mandatory")
_MscVrIpOspfStubAreaIdIndex_Type = IpAddress
_MscVrIpOspfStubAreaIdIndex_Object = MibTableColumn
mscVrIpOspfStubAreaIdIndex = _MscVrIpOspfStubAreaIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 3, 1, 1, 10),
    _MscVrIpOspfStubAreaIdIndex_Type()
)
mscVrIpOspfStubAreaIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpOspfStubAreaIdIndex.setStatus("mandatory")


class _MscVrIpOspfStubTosIndex_Type(Integer32):
    """Custom type mscVrIpOspfStubTosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_MscVrIpOspfStubTosIndex_Type.__name__ = "Integer32"
_MscVrIpOspfStubTosIndex_Object = MibTableColumn
mscVrIpOspfStubTosIndex = _MscVrIpOspfStubTosIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 3, 1, 1, 11),
    _MscVrIpOspfStubTosIndex_Type()
)
mscVrIpOspfStubTosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpOspfStubTosIndex.setStatus("mandatory")
_MscVrIpOspfStubProvTable_Object = MibTable
mscVrIpOspfStubProvTable = _MscVrIpOspfStubProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 3, 10)
)
if mibBuilder.loadTexts:
    mscVrIpOspfStubProvTable.setStatus("mandatory")
_MscVrIpOspfStubProvEntry_Object = MibTableRow
mscVrIpOspfStubProvEntry = _MscVrIpOspfStubProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 3, 10, 1)
)
mscVrIpOspfStubProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfStubAreaIdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfStubTosIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfStubProvEntry.setStatus("mandatory")


class _MscVrIpOspfStubMetric_Type(Unsigned32):
    """Custom type mscVrIpOspfStubMetric based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MscVrIpOspfStubMetric_Type.__name__ = "Unsigned32"
_MscVrIpOspfStubMetric_Object = MibTableColumn
mscVrIpOspfStubMetric = _MscVrIpOspfStubMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 3, 10, 1, 1),
    _MscVrIpOspfStubMetric_Type()
)
mscVrIpOspfStubMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfStubMetric.setStatus("mandatory")


class _MscVrIpOspfStubMetricType_Type(Integer32):
    """Custom type mscVrIpOspfStubMetricType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("comparableCost", 2),
          ("nonComparable", 3),
          ("ospfMetric", 1))
    )


_MscVrIpOspfStubMetricType_Type.__name__ = "Integer32"
_MscVrIpOspfStubMetricType_Object = MibTableColumn
mscVrIpOspfStubMetricType = _MscVrIpOspfStubMetricType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 3, 10, 1, 2),
    _MscVrIpOspfStubMetricType_Type()
)
mscVrIpOspfStubMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfStubMetricType.setStatus("mandatory")


class _MscVrIpOspfStubAdvertiseDefault_Type(Integer32):
    """Custom type mscVrIpOspfStubAdvertiseDefault based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MscVrIpOspfStubAdvertiseDefault_Type.__name__ = "Integer32"
_MscVrIpOspfStubAdvertiseDefault_Object = MibTableColumn
mscVrIpOspfStubAdvertiseDefault = _MscVrIpOspfStubAdvertiseDefault_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 3, 10, 1, 3),
    _MscVrIpOspfStubAdvertiseDefault_Type()
)
mscVrIpOspfStubAdvertiseDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfStubAdvertiseDefault.setStatus("mandatory")
_MscVrIpOspfAggregate_ObjectIdentity = ObjectIdentity
mscVrIpOspfAggregate = _MscVrIpOspfAggregate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 5)
)
_MscVrIpOspfAggregateRowStatusTable_Object = MibTable
mscVrIpOspfAggregateRowStatusTable = _MscVrIpOspfAggregateRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 5, 1)
)
if mibBuilder.loadTexts:
    mscVrIpOspfAggregateRowStatusTable.setStatus("mandatory")
_MscVrIpOspfAggregateRowStatusEntry_Object = MibTableRow
mscVrIpOspfAggregateRowStatusEntry = _MscVrIpOspfAggregateRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 5, 1, 1)
)
mscVrIpOspfAggregateRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfAggregateAreaIdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfAggregateLsdbTypeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfAggregateAggregateNetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfAggregateAggregateMaskIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfAggregateRowStatusEntry.setStatus("mandatory")
_MscVrIpOspfAggregateRowStatus_Type = RowStatus
_MscVrIpOspfAggregateRowStatus_Object = MibTableColumn
mscVrIpOspfAggregateRowStatus = _MscVrIpOspfAggregateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 5, 1, 1, 1),
    _MscVrIpOspfAggregateRowStatus_Type()
)
mscVrIpOspfAggregateRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfAggregateRowStatus.setStatus("mandatory")
_MscVrIpOspfAggregateComponentName_Type = DisplayString
_MscVrIpOspfAggregateComponentName_Object = MibTableColumn
mscVrIpOspfAggregateComponentName = _MscVrIpOspfAggregateComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 5, 1, 1, 2),
    _MscVrIpOspfAggregateComponentName_Type()
)
mscVrIpOspfAggregateComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfAggregateComponentName.setStatus("mandatory")
_MscVrIpOspfAggregateStorageType_Type = StorageType
_MscVrIpOspfAggregateStorageType_Object = MibTableColumn
mscVrIpOspfAggregateStorageType = _MscVrIpOspfAggregateStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 5, 1, 1, 4),
    _MscVrIpOspfAggregateStorageType_Type()
)
mscVrIpOspfAggregateStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfAggregateStorageType.setStatus("mandatory")
_MscVrIpOspfAggregateAreaIdIndex_Type = IpAddress
_MscVrIpOspfAggregateAreaIdIndex_Object = MibTableColumn
mscVrIpOspfAggregateAreaIdIndex = _MscVrIpOspfAggregateAreaIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 5, 1, 1, 10),
    _MscVrIpOspfAggregateAreaIdIndex_Type()
)
mscVrIpOspfAggregateAreaIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpOspfAggregateAreaIdIndex.setStatus("mandatory")


class _MscVrIpOspfAggregateLsdbTypeIndex_Type(Integer32):
    """Custom type mscVrIpOspfAggregateLsdbTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("nssaExternalLink", 7),
          ("summaryLink", 3))
    )


_MscVrIpOspfAggregateLsdbTypeIndex_Type.__name__ = "Integer32"
_MscVrIpOspfAggregateLsdbTypeIndex_Object = MibTableColumn
mscVrIpOspfAggregateLsdbTypeIndex = _MscVrIpOspfAggregateLsdbTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 5, 1, 1, 11),
    _MscVrIpOspfAggregateLsdbTypeIndex_Type()
)
mscVrIpOspfAggregateLsdbTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpOspfAggregateLsdbTypeIndex.setStatus("mandatory")
_MscVrIpOspfAggregateAggregateNetIndex_Type = IpAddress
_MscVrIpOspfAggregateAggregateNetIndex_Object = MibTableColumn
mscVrIpOspfAggregateAggregateNetIndex = _MscVrIpOspfAggregateAggregateNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 5, 1, 1, 12),
    _MscVrIpOspfAggregateAggregateNetIndex_Type()
)
mscVrIpOspfAggregateAggregateNetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpOspfAggregateAggregateNetIndex.setStatus("mandatory")
_MscVrIpOspfAggregateAggregateMaskIndex_Type = IpAddress
_MscVrIpOspfAggregateAggregateMaskIndex_Object = MibTableColumn
mscVrIpOspfAggregateAggregateMaskIndex = _MscVrIpOspfAggregateAggregateMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 5, 1, 1, 13),
    _MscVrIpOspfAggregateAggregateMaskIndex_Type()
)
mscVrIpOspfAggregateAggregateMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpOspfAggregateAggregateMaskIndex.setStatus("mandatory")
_MscVrIpOspfAggregateProvTable_Object = MibTable
mscVrIpOspfAggregateProvTable = _MscVrIpOspfAggregateProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 5, 10)
)
if mibBuilder.loadTexts:
    mscVrIpOspfAggregateProvTable.setStatus("mandatory")
_MscVrIpOspfAggregateProvEntry_Object = MibTableRow
mscVrIpOspfAggregateProvEntry = _MscVrIpOspfAggregateProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 5, 10, 1)
)
mscVrIpOspfAggregateProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfAggregateAreaIdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfAggregateLsdbTypeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfAggregateAggregateNetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfAggregateAggregateMaskIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfAggregateProvEntry.setStatus("mandatory")


class _MscVrIpOspfAggregateEffect_Type(Integer32):
    """Custom type mscVrIpOspfAggregateEffect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("advertiseMatching", 1),
          ("doNotAdvertiseMatching", 2),
          ("invalid", 3))
    )


_MscVrIpOspfAggregateEffect_Type.__name__ = "Integer32"
_MscVrIpOspfAggregateEffect_Object = MibTableColumn
mscVrIpOspfAggregateEffect = _MscVrIpOspfAggregateEffect_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 5, 10, 1, 1),
    _MscVrIpOspfAggregateEffect_Type()
)
mscVrIpOspfAggregateEffect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfAggregateEffect.setStatus("mandatory")
_MscVrIpOspfHost_ObjectIdentity = ObjectIdentity
mscVrIpOspfHost = _MscVrIpOspfHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 6)
)
_MscVrIpOspfHostRowStatusTable_Object = MibTable
mscVrIpOspfHostRowStatusTable = _MscVrIpOspfHostRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 6, 1)
)
if mibBuilder.loadTexts:
    mscVrIpOspfHostRowStatusTable.setStatus("mandatory")
_MscVrIpOspfHostRowStatusEntry_Object = MibTableRow
mscVrIpOspfHostRowStatusEntry = _MscVrIpOspfHostRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 6, 1, 1)
)
mscVrIpOspfHostRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfHostAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfHostTosIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfHostRowStatusEntry.setStatus("mandatory")
_MscVrIpOspfHostRowStatus_Type = RowStatus
_MscVrIpOspfHostRowStatus_Object = MibTableColumn
mscVrIpOspfHostRowStatus = _MscVrIpOspfHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 6, 1, 1, 1),
    _MscVrIpOspfHostRowStatus_Type()
)
mscVrIpOspfHostRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfHostRowStatus.setStatus("mandatory")
_MscVrIpOspfHostComponentName_Type = DisplayString
_MscVrIpOspfHostComponentName_Object = MibTableColumn
mscVrIpOspfHostComponentName = _MscVrIpOspfHostComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 6, 1, 1, 2),
    _MscVrIpOspfHostComponentName_Type()
)
mscVrIpOspfHostComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfHostComponentName.setStatus("mandatory")
_MscVrIpOspfHostStorageType_Type = StorageType
_MscVrIpOspfHostStorageType_Object = MibTableColumn
mscVrIpOspfHostStorageType = _MscVrIpOspfHostStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 6, 1, 1, 4),
    _MscVrIpOspfHostStorageType_Type()
)
mscVrIpOspfHostStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfHostStorageType.setStatus("mandatory")
_MscVrIpOspfHostAddressIndex_Type = IpAddress
_MscVrIpOspfHostAddressIndex_Object = MibTableColumn
mscVrIpOspfHostAddressIndex = _MscVrIpOspfHostAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 6, 1, 1, 10),
    _MscVrIpOspfHostAddressIndex_Type()
)
mscVrIpOspfHostAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpOspfHostAddressIndex.setStatus("mandatory")


class _MscVrIpOspfHostTosIndex_Type(Integer32):
    """Custom type mscVrIpOspfHostTosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_MscVrIpOspfHostTosIndex_Type.__name__ = "Integer32"
_MscVrIpOspfHostTosIndex_Object = MibTableColumn
mscVrIpOspfHostTosIndex = _MscVrIpOspfHostTosIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 6, 1, 1, 11),
    _MscVrIpOspfHostTosIndex_Type()
)
mscVrIpOspfHostTosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpOspfHostTosIndex.setStatus("mandatory")
_MscVrIpOspfHostProvTable_Object = MibTable
mscVrIpOspfHostProvTable = _MscVrIpOspfHostProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 6, 10)
)
if mibBuilder.loadTexts:
    mscVrIpOspfHostProvTable.setStatus("mandatory")
_MscVrIpOspfHostProvEntry_Object = MibTableRow
mscVrIpOspfHostProvEntry = _MscVrIpOspfHostProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 6, 10, 1)
)
mscVrIpOspfHostProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfHostAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfHostTosIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfHostProvEntry.setStatus("mandatory")
_MscVrIpOspfHostAreaId_Type = AreaID
_MscVrIpOspfHostAreaId_Object = MibTableColumn
mscVrIpOspfHostAreaId = _MscVrIpOspfHostAreaId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 6, 10, 1, 1),
    _MscVrIpOspfHostAreaId_Type()
)
mscVrIpOspfHostAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfHostAreaId.setStatus("mandatory")


class _MscVrIpOspfHostMetric_Type(Unsigned32):
    """Custom type mscVrIpOspfHostMetric based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrIpOspfHostMetric_Type.__name__ = "Unsigned32"
_MscVrIpOspfHostMetric_Object = MibTableColumn
mscVrIpOspfHostMetric = _MscVrIpOspfHostMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 6, 10, 1, 2),
    _MscVrIpOspfHostMetric_Type()
)
mscVrIpOspfHostMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfHostMetric.setStatus("mandatory")
_MscVrIpOspfVirtIf_ObjectIdentity = ObjectIdentity
mscVrIpOspfVirtIf = _MscVrIpOspfVirtIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 7)
)
_MscVrIpOspfVirtIfRowStatusTable_Object = MibTable
mscVrIpOspfVirtIfRowStatusTable = _MscVrIpOspfVirtIfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 7, 1)
)
if mibBuilder.loadTexts:
    mscVrIpOspfVirtIfRowStatusTable.setStatus("mandatory")
_MscVrIpOspfVirtIfRowStatusEntry_Object = MibTableRow
mscVrIpOspfVirtIfRowStatusEntry = _MscVrIpOspfVirtIfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 7, 1, 1)
)
mscVrIpOspfVirtIfRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfVirtIfAreaIdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfVirtIfNbrRouterIdIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfVirtIfRowStatusEntry.setStatus("mandatory")
_MscVrIpOspfVirtIfRowStatus_Type = RowStatus
_MscVrIpOspfVirtIfRowStatus_Object = MibTableColumn
mscVrIpOspfVirtIfRowStatus = _MscVrIpOspfVirtIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 7, 1, 1, 1),
    _MscVrIpOspfVirtIfRowStatus_Type()
)
mscVrIpOspfVirtIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfVirtIfRowStatus.setStatus("mandatory")
_MscVrIpOspfVirtIfComponentName_Type = DisplayString
_MscVrIpOspfVirtIfComponentName_Object = MibTableColumn
mscVrIpOspfVirtIfComponentName = _MscVrIpOspfVirtIfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 7, 1, 1, 2),
    _MscVrIpOspfVirtIfComponentName_Type()
)
mscVrIpOspfVirtIfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfVirtIfComponentName.setStatus("mandatory")
_MscVrIpOspfVirtIfStorageType_Type = StorageType
_MscVrIpOspfVirtIfStorageType_Object = MibTableColumn
mscVrIpOspfVirtIfStorageType = _MscVrIpOspfVirtIfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 7, 1, 1, 4),
    _MscVrIpOspfVirtIfStorageType_Type()
)
mscVrIpOspfVirtIfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfVirtIfStorageType.setStatus("mandatory")
_MscVrIpOspfVirtIfAreaIdIndex_Type = IpAddress
_MscVrIpOspfVirtIfAreaIdIndex_Object = MibTableColumn
mscVrIpOspfVirtIfAreaIdIndex = _MscVrIpOspfVirtIfAreaIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 7, 1, 1, 10),
    _MscVrIpOspfVirtIfAreaIdIndex_Type()
)
mscVrIpOspfVirtIfAreaIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpOspfVirtIfAreaIdIndex.setStatus("mandatory")
_MscVrIpOspfVirtIfNbrRouterIdIndex_Type = IpAddress
_MscVrIpOspfVirtIfNbrRouterIdIndex_Object = MibTableColumn
mscVrIpOspfVirtIfNbrRouterIdIndex = _MscVrIpOspfVirtIfNbrRouterIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 7, 1, 1, 11),
    _MscVrIpOspfVirtIfNbrRouterIdIndex_Type()
)
mscVrIpOspfVirtIfNbrRouterIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpOspfVirtIfNbrRouterIdIndex.setStatus("mandatory")
_MscVrIpOspfVirtIfProvTable_Object = MibTable
mscVrIpOspfVirtIfProvTable = _MscVrIpOspfVirtIfProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 7, 10)
)
if mibBuilder.loadTexts:
    mscVrIpOspfVirtIfProvTable.setStatus("mandatory")
_MscVrIpOspfVirtIfProvEntry_Object = MibTableRow
mscVrIpOspfVirtIfProvEntry = _MscVrIpOspfVirtIfProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 7, 10, 1)
)
mscVrIpOspfVirtIfProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfVirtIfAreaIdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfVirtIfNbrRouterIdIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfVirtIfProvEntry.setStatus("mandatory")


class _MscVrIpOspfVirtIfTransitDelay_Type(Unsigned32):
    """Custom type mscVrIpOspfVirtIfTransitDelay based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_MscVrIpOspfVirtIfTransitDelay_Type.__name__ = "Unsigned32"
_MscVrIpOspfVirtIfTransitDelay_Object = MibTableColumn
mscVrIpOspfVirtIfTransitDelay = _MscVrIpOspfVirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 7, 10, 1, 1),
    _MscVrIpOspfVirtIfTransitDelay_Type()
)
mscVrIpOspfVirtIfTransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfVirtIfTransitDelay.setStatus("mandatory")


class _MscVrIpOspfVirtIfRetransInterval_Type(Unsigned32):
    """Custom type mscVrIpOspfVirtIfRetransInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_MscVrIpOspfVirtIfRetransInterval_Type.__name__ = "Unsigned32"
_MscVrIpOspfVirtIfRetransInterval_Object = MibTableColumn
mscVrIpOspfVirtIfRetransInterval = _MscVrIpOspfVirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 7, 10, 1, 2),
    _MscVrIpOspfVirtIfRetransInterval_Type()
)
mscVrIpOspfVirtIfRetransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfVirtIfRetransInterval.setStatus("mandatory")


class _MscVrIpOspfVirtIfHelloInterval_Type(Unsigned32):
    """Custom type mscVrIpOspfVirtIfHelloInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_MscVrIpOspfVirtIfHelloInterval_Type.__name__ = "Unsigned32"
_MscVrIpOspfVirtIfHelloInterval_Object = MibTableColumn
mscVrIpOspfVirtIfHelloInterval = _MscVrIpOspfVirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 7, 10, 1, 3),
    _MscVrIpOspfVirtIfHelloInterval_Type()
)
mscVrIpOspfVirtIfHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfVirtIfHelloInterval.setStatus("mandatory")


class _MscVrIpOspfVirtIfRtrDeadInterval_Type(Unsigned32):
    """Custom type mscVrIpOspfVirtIfRtrDeadInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_MscVrIpOspfVirtIfRtrDeadInterval_Type.__name__ = "Unsigned32"
_MscVrIpOspfVirtIfRtrDeadInterval_Object = MibTableColumn
mscVrIpOspfVirtIfRtrDeadInterval = _MscVrIpOspfVirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 7, 10, 1, 4),
    _MscVrIpOspfVirtIfRtrDeadInterval_Type()
)
mscVrIpOspfVirtIfRtrDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfVirtIfRtrDeadInterval.setStatus("mandatory")


class _MscVrIpOspfVirtIfAuthKey_Type(HexString):
    """Custom type mscVrIpOspfVirtIfAuthKey based on HexString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscVrIpOspfVirtIfAuthKey_Type.__name__ = "HexString"
_MscVrIpOspfVirtIfAuthKey_Object = MibTableColumn
mscVrIpOspfVirtIfAuthKey = _MscVrIpOspfVirtIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 7, 10, 1, 5),
    _MscVrIpOspfVirtIfAuthKey_Type()
)
mscVrIpOspfVirtIfAuthKey.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscVrIpOspfVirtIfAuthKey.setStatus("mandatory")
_MscVrIpOspfVirtIfOperTable_Object = MibTable
mscVrIpOspfVirtIfOperTable = _MscVrIpOspfVirtIfOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 7, 11)
)
if mibBuilder.loadTexts:
    mscVrIpOspfVirtIfOperTable.setStatus("mandatory")
_MscVrIpOspfVirtIfOperEntry_Object = MibTableRow
mscVrIpOspfVirtIfOperEntry = _MscVrIpOspfVirtIfOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 7, 11, 1)
)
mscVrIpOspfVirtIfOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfVirtIfAreaIdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfVirtIfNbrRouterIdIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfVirtIfOperEntry.setStatus("mandatory")


class _MscVrIpOspfVirtIfState_Type(Integer32):
    """Custom type mscVrIpOspfVirtIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("pointToPoint", 4))
    )


_MscVrIpOspfVirtIfState_Type.__name__ = "Integer32"
_MscVrIpOspfVirtIfState_Object = MibTableColumn
mscVrIpOspfVirtIfState = _MscVrIpOspfVirtIfState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 7, 11, 1, 1),
    _MscVrIpOspfVirtIfState_Type()
)
mscVrIpOspfVirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfVirtIfState.setStatus("mandatory")
_MscVrIpOspfVirtIfEvents_Type = Counter32
_MscVrIpOspfVirtIfEvents_Object = MibTableColumn
mscVrIpOspfVirtIfEvents = _MscVrIpOspfVirtIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 7, 11, 1, 2),
    _MscVrIpOspfVirtIfEvents_Type()
)
mscVrIpOspfVirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfVirtIfEvents.setStatus("mandatory")
_MscVrIpOspfExport_ObjectIdentity = ObjectIdentity
mscVrIpOspfExport = _MscVrIpOspfExport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8)
)
_MscVrIpOspfExportRowStatusTable_Object = MibTable
mscVrIpOspfExportRowStatusTable = _MscVrIpOspfExportRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 1)
)
if mibBuilder.loadTexts:
    mscVrIpOspfExportRowStatusTable.setStatus("mandatory")
_MscVrIpOspfExportRowStatusEntry_Object = MibTableRow
mscVrIpOspfExportRowStatusEntry = _MscVrIpOspfExportRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 1, 1)
)
mscVrIpOspfExportRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfExportIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfExportRowStatusEntry.setStatus("mandatory")
_MscVrIpOspfExportRowStatus_Type = RowStatus
_MscVrIpOspfExportRowStatus_Object = MibTableColumn
mscVrIpOspfExportRowStatus = _MscVrIpOspfExportRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 1, 1, 1),
    _MscVrIpOspfExportRowStatus_Type()
)
mscVrIpOspfExportRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfExportRowStatus.setStatus("mandatory")
_MscVrIpOspfExportComponentName_Type = DisplayString
_MscVrIpOspfExportComponentName_Object = MibTableColumn
mscVrIpOspfExportComponentName = _MscVrIpOspfExportComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 1, 1, 2),
    _MscVrIpOspfExportComponentName_Type()
)
mscVrIpOspfExportComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfExportComponentName.setStatus("mandatory")
_MscVrIpOspfExportStorageType_Type = StorageType
_MscVrIpOspfExportStorageType_Object = MibTableColumn
mscVrIpOspfExportStorageType = _MscVrIpOspfExportStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 1, 1, 4),
    _MscVrIpOspfExportStorageType_Type()
)
mscVrIpOspfExportStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfExportStorageType.setStatus("mandatory")


class _MscVrIpOspfExportIndex_Type(Integer32):
    """Custom type mscVrIpOspfExportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpOspfExportIndex_Type.__name__ = "Integer32"
_MscVrIpOspfExportIndex_Object = MibTableColumn
mscVrIpOspfExportIndex = _MscVrIpOspfExportIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 1, 1, 10),
    _MscVrIpOspfExportIndex_Type()
)
mscVrIpOspfExportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpOspfExportIndex.setStatus("mandatory")
_MscVrIpOspfExportNetList_ObjectIdentity = ObjectIdentity
mscVrIpOspfExportNetList = _MscVrIpOspfExportNetList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 2)
)
_MscVrIpOspfExportNetListRowStatusTable_Object = MibTable
mscVrIpOspfExportNetListRowStatusTable = _MscVrIpOspfExportNetListRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpOspfExportNetListRowStatusTable.setStatus("mandatory")
_MscVrIpOspfExportNetListRowStatusEntry_Object = MibTableRow
mscVrIpOspfExportNetListRowStatusEntry = _MscVrIpOspfExportNetListRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 2, 1, 1)
)
mscVrIpOspfExportNetListRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfExportIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfExportNetListIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfExportNetListRowStatusEntry.setStatus("mandatory")
_MscVrIpOspfExportNetListRowStatus_Type = RowStatus
_MscVrIpOspfExportNetListRowStatus_Object = MibTableColumn
mscVrIpOspfExportNetListRowStatus = _MscVrIpOspfExportNetListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 2, 1, 1, 1),
    _MscVrIpOspfExportNetListRowStatus_Type()
)
mscVrIpOspfExportNetListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfExportNetListRowStatus.setStatus("mandatory")
_MscVrIpOspfExportNetListComponentName_Type = DisplayString
_MscVrIpOspfExportNetListComponentName_Object = MibTableColumn
mscVrIpOspfExportNetListComponentName = _MscVrIpOspfExportNetListComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 2, 1, 1, 2),
    _MscVrIpOspfExportNetListComponentName_Type()
)
mscVrIpOspfExportNetListComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfExportNetListComponentName.setStatus("mandatory")
_MscVrIpOspfExportNetListStorageType_Type = StorageType
_MscVrIpOspfExportNetListStorageType_Object = MibTableColumn
mscVrIpOspfExportNetListStorageType = _MscVrIpOspfExportNetListStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 2, 1, 1, 4),
    _MscVrIpOspfExportNetListStorageType_Type()
)
mscVrIpOspfExportNetListStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfExportNetListStorageType.setStatus("mandatory")


class _MscVrIpOspfExportNetListIndex_Type(Integer32):
    """Custom type mscVrIpOspfExportNetListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpOspfExportNetListIndex_Type.__name__ = "Integer32"
_MscVrIpOspfExportNetListIndex_Object = MibTableColumn
mscVrIpOspfExportNetListIndex = _MscVrIpOspfExportNetListIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 2, 1, 1, 10),
    _MscVrIpOspfExportNetListIndex_Type()
)
mscVrIpOspfExportNetListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpOspfExportNetListIndex.setStatus("mandatory")
_MscVrIpOspfExportNetListProvTable_Object = MibTable
mscVrIpOspfExportNetListProvTable = _MscVrIpOspfExportNetListProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpOspfExportNetListProvTable.setStatus("mandatory")
_MscVrIpOspfExportNetListProvEntry_Object = MibTableRow
mscVrIpOspfExportNetListProvEntry = _MscVrIpOspfExportNetListProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 2, 10, 1)
)
mscVrIpOspfExportNetListProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfExportIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfExportNetListIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfExportNetListProvEntry.setStatus("mandatory")
_MscVrIpOspfExportNetListIpAddress_Type = IpAddress
_MscVrIpOspfExportNetListIpAddress_Object = MibTableColumn
mscVrIpOspfExportNetListIpAddress = _MscVrIpOspfExportNetListIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 2, 10, 1, 1),
    _MscVrIpOspfExportNetListIpAddress_Type()
)
mscVrIpOspfExportNetListIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfExportNetListIpAddress.setStatus("mandatory")
_MscVrIpOspfExportNetListIpMask_Type = IpAddress
_MscVrIpOspfExportNetListIpMask_Object = MibTableColumn
mscVrIpOspfExportNetListIpMask = _MscVrIpOspfExportNetListIpMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 2, 10, 1, 2),
    _MscVrIpOspfExportNetListIpMask_Type()
)
mscVrIpOspfExportNetListIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfExportNetListIpMask.setStatus("mandatory")
_MscVrIpOspfExportProvTable_Object = MibTable
mscVrIpOspfExportProvTable = _MscVrIpOspfExportProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 10)
)
if mibBuilder.loadTexts:
    mscVrIpOspfExportProvTable.setStatus("mandatory")
_MscVrIpOspfExportProvEntry_Object = MibTableRow
mscVrIpOspfExportProvEntry = _MscVrIpOspfExportProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 10, 1)
)
mscVrIpOspfExportProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfExportIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfExportProvEntry.setStatus("mandatory")


class _MscVrIpOspfExportAdvertiseStatus_Type(Integer32):
    """Custom type mscVrIpOspfExportAdvertiseStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("send", 1))
    )


_MscVrIpOspfExportAdvertiseStatus_Type.__name__ = "Integer32"
_MscVrIpOspfExportAdvertiseStatus_Object = MibTableColumn
mscVrIpOspfExportAdvertiseStatus = _MscVrIpOspfExportAdvertiseStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 10, 1, 1),
    _MscVrIpOspfExportAdvertiseStatus_Type()
)
mscVrIpOspfExportAdvertiseStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfExportAdvertiseStatus.setStatus("mandatory")


class _MscVrIpOspfExportMetric_Type(Integer32):
    """Custom type mscVrIpOspfExportMetric based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 16777215),
    )


_MscVrIpOspfExportMetric_Type.__name__ = "Integer32"
_MscVrIpOspfExportMetric_Object = MibTableColumn
mscVrIpOspfExportMetric = _MscVrIpOspfExportMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 10, 1, 2),
    _MscVrIpOspfExportMetric_Type()
)
mscVrIpOspfExportMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfExportMetric.setStatus("mandatory")


class _MscVrIpOspfExportProtocol_Type(Integer32):
    """Custom type mscVrIpOspfExportProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("bgpExternal", 9),
          ("bgpInternal", 8),
          ("egp", 2),
          ("rip", 3),
          ("staticLocal", 6),
          ("staticRemote", 7))
    )


_MscVrIpOspfExportProtocol_Type.__name__ = "Integer32"
_MscVrIpOspfExportProtocol_Object = MibTableColumn
mscVrIpOspfExportProtocol = _MscVrIpOspfExportProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 10, 1, 3),
    _MscVrIpOspfExportProtocol_Type()
)
mscVrIpOspfExportProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfExportProtocol.setStatus("mandatory")


class _MscVrIpOspfExportRipInterface_Type(IpAddress):
    """Custom type mscVrIpOspfExportRipInterface based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrIpOspfExportRipInterface_Object = MibTableColumn
mscVrIpOspfExportRipInterface = _MscVrIpOspfExportRipInterface_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 10, 1, 4),
    _MscVrIpOspfExportRipInterface_Type()
)
mscVrIpOspfExportRipInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfExportRipInterface.setStatus("mandatory")


class _MscVrIpOspfExportRipNeighbor_Type(IpAddress):
    """Custom type mscVrIpOspfExportRipNeighbor based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrIpOspfExportRipNeighbor_Object = MibTableColumn
mscVrIpOspfExportRipNeighbor = _MscVrIpOspfExportRipNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 10, 1, 5),
    _MscVrIpOspfExportRipNeighbor_Type()
)
mscVrIpOspfExportRipNeighbor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfExportRipNeighbor.setStatus("mandatory")


class _MscVrIpOspfExportEgpAsId_Type(Unsigned32):
    """Custom type mscVrIpOspfExportEgpAsId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpOspfExportEgpAsId_Type.__name__ = "Unsigned32"
_MscVrIpOspfExportEgpAsId_Object = MibTableColumn
mscVrIpOspfExportEgpAsId = _MscVrIpOspfExportEgpAsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 10, 1, 6),
    _MscVrIpOspfExportEgpAsId_Type()
)
mscVrIpOspfExportEgpAsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfExportEgpAsId.setStatus("mandatory")


class _MscVrIpOspfExportTag_Type(Unsigned32):
    """Custom type mscVrIpOspfExportTag based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpOspfExportTag_Type.__name__ = "Unsigned32"
_MscVrIpOspfExportTag_Object = MibTableColumn
mscVrIpOspfExportTag = _MscVrIpOspfExportTag_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 10, 1, 7),
    _MscVrIpOspfExportTag_Type()
)
mscVrIpOspfExportTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfExportTag.setStatus("mandatory")


class _MscVrIpOspfExportExtLsaMetricType_Type(Integer32):
    """Custom type mscVrIpOspfExportExtLsaMetricType based on Integer32"""
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
        *(("type1", 1),
          ("type2", 2),
          ("useProtocolDefault", 0))
    )


_MscVrIpOspfExportExtLsaMetricType_Type.__name__ = "Integer32"
_MscVrIpOspfExportExtLsaMetricType_Object = MibTableColumn
mscVrIpOspfExportExtLsaMetricType = _MscVrIpOspfExportExtLsaMetricType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 10, 1, 8),
    _MscVrIpOspfExportExtLsaMetricType_Type()
)
mscVrIpOspfExportExtLsaMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfExportExtLsaMetricType.setStatus("mandatory")


class _MscVrIpOspfExportBgpAsId_Type(Unsigned32):
    """Custom type mscVrIpOspfExportBgpAsId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpOspfExportBgpAsId_Type.__name__ = "Unsigned32"
_MscVrIpOspfExportBgpAsId_Object = MibTableColumn
mscVrIpOspfExportBgpAsId = _MscVrIpOspfExportBgpAsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 10, 1, 9),
    _MscVrIpOspfExportBgpAsId_Type()
)
mscVrIpOspfExportBgpAsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfExportBgpAsId.setStatus("mandatory")


class _MscVrIpOspfExportBgpPeerIp_Type(IpAddress):
    """Custom type mscVrIpOspfExportBgpPeerIp based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrIpOspfExportBgpPeerIp_Object = MibTableColumn
mscVrIpOspfExportBgpPeerIp = _MscVrIpOspfExportBgpPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 8, 10, 1, 10),
    _MscVrIpOspfExportBgpPeerIp_Type()
)
mscVrIpOspfExportBgpPeerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfExportBgpPeerIp.setStatus("mandatory")
_MscVrIpOspfVirtNbr_ObjectIdentity = ObjectIdentity
mscVrIpOspfVirtNbr = _MscVrIpOspfVirtNbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 9)
)
_MscVrIpOspfVirtNbrRowStatusTable_Object = MibTable
mscVrIpOspfVirtNbrRowStatusTable = _MscVrIpOspfVirtNbrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 9, 1)
)
if mibBuilder.loadTexts:
    mscVrIpOspfVirtNbrRowStatusTable.setStatus("mandatory")
_MscVrIpOspfVirtNbrRowStatusEntry_Object = MibTableRow
mscVrIpOspfVirtNbrRowStatusEntry = _MscVrIpOspfVirtNbrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 9, 1, 1)
)
mscVrIpOspfVirtNbrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfVirtNbrAreaIdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfVirtNbrNbrRouterIdIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfVirtNbrRowStatusEntry.setStatus("mandatory")
_MscVrIpOspfVirtNbrRowStatus_Type = RowStatus
_MscVrIpOspfVirtNbrRowStatus_Object = MibTableColumn
mscVrIpOspfVirtNbrRowStatus = _MscVrIpOspfVirtNbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 9, 1, 1, 1),
    _MscVrIpOspfVirtNbrRowStatus_Type()
)
mscVrIpOspfVirtNbrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfVirtNbrRowStatus.setStatus("mandatory")
_MscVrIpOspfVirtNbrComponentName_Type = DisplayString
_MscVrIpOspfVirtNbrComponentName_Object = MibTableColumn
mscVrIpOspfVirtNbrComponentName = _MscVrIpOspfVirtNbrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 9, 1, 1, 2),
    _MscVrIpOspfVirtNbrComponentName_Type()
)
mscVrIpOspfVirtNbrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfVirtNbrComponentName.setStatus("mandatory")
_MscVrIpOspfVirtNbrStorageType_Type = StorageType
_MscVrIpOspfVirtNbrStorageType_Object = MibTableColumn
mscVrIpOspfVirtNbrStorageType = _MscVrIpOspfVirtNbrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 9, 1, 1, 4),
    _MscVrIpOspfVirtNbrStorageType_Type()
)
mscVrIpOspfVirtNbrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfVirtNbrStorageType.setStatus("mandatory")
_MscVrIpOspfVirtNbrAreaIdIndex_Type = IpAddress
_MscVrIpOspfVirtNbrAreaIdIndex_Object = MibTableColumn
mscVrIpOspfVirtNbrAreaIdIndex = _MscVrIpOspfVirtNbrAreaIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 9, 1, 1, 10),
    _MscVrIpOspfVirtNbrAreaIdIndex_Type()
)
mscVrIpOspfVirtNbrAreaIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpOspfVirtNbrAreaIdIndex.setStatus("mandatory")
_MscVrIpOspfVirtNbrNbrRouterIdIndex_Type = IpAddress
_MscVrIpOspfVirtNbrNbrRouterIdIndex_Object = MibTableColumn
mscVrIpOspfVirtNbrNbrRouterIdIndex = _MscVrIpOspfVirtNbrNbrRouterIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 9, 1, 1, 11),
    _MscVrIpOspfVirtNbrNbrRouterIdIndex_Type()
)
mscVrIpOspfVirtNbrNbrRouterIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpOspfVirtNbrNbrRouterIdIndex.setStatus("mandatory")
_MscVrIpOspfVirtNbrOperTable_Object = MibTable
mscVrIpOspfVirtNbrOperTable = _MscVrIpOspfVirtNbrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 9, 10)
)
if mibBuilder.loadTexts:
    mscVrIpOspfVirtNbrOperTable.setStatus("mandatory")
_MscVrIpOspfVirtNbrOperEntry_Object = MibTableRow
mscVrIpOspfVirtNbrOperEntry = _MscVrIpOspfVirtNbrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 9, 10, 1)
)
mscVrIpOspfVirtNbrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfVirtNbrAreaIdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfVirtNbrNbrRouterIdIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfVirtNbrOperEntry.setStatus("mandatory")
_MscVrIpOspfVirtNbrNbrIpAddress_Type = IpAddress
_MscVrIpOspfVirtNbrNbrIpAddress_Object = MibTableColumn
mscVrIpOspfVirtNbrNbrIpAddress = _MscVrIpOspfVirtNbrNbrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 9, 10, 1, 1),
    _MscVrIpOspfVirtNbrNbrIpAddress_Type()
)
mscVrIpOspfVirtNbrNbrIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfVirtNbrNbrIpAddress.setStatus("mandatory")


class _MscVrIpOspfVirtNbrOptions_Type(Unsigned32):
    """Custom type mscVrIpOspfVirtNbrOptions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscVrIpOspfVirtNbrOptions_Type.__name__ = "Unsigned32"
_MscVrIpOspfVirtNbrOptions_Object = MibTableColumn
mscVrIpOspfVirtNbrOptions = _MscVrIpOspfVirtNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 9, 10, 1, 2),
    _MscVrIpOspfVirtNbrOptions_Type()
)
mscVrIpOspfVirtNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfVirtNbrOptions.setStatus("mandatory")


class _MscVrIpOspfVirtNbrState_Type(Integer32):
    """Custom type mscVrIpOspfVirtNbrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("attempt", 2),
          ("down", 1),
          ("exchange", 5),
          ("exchangeStatrt", 6),
          ("full", 8),
          ("init", 3),
          ("loading", 7),
          ("twoWay", 4))
    )


_MscVrIpOspfVirtNbrState_Type.__name__ = "Integer32"
_MscVrIpOspfVirtNbrState_Object = MibTableColumn
mscVrIpOspfVirtNbrState = _MscVrIpOspfVirtNbrState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 9, 10, 1, 3),
    _MscVrIpOspfVirtNbrState_Type()
)
mscVrIpOspfVirtNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfVirtNbrState.setStatus("mandatory")
_MscVrIpOspfVirtNbrEvents_Type = Counter32
_MscVrIpOspfVirtNbrEvents_Object = MibTableColumn
mscVrIpOspfVirtNbrEvents = _MscVrIpOspfVirtNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 9, 10, 1, 4),
    _MscVrIpOspfVirtNbrEvents_Type()
)
mscVrIpOspfVirtNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfVirtNbrEvents.setStatus("mandatory")


class _MscVrIpOspfVirtNbrLsRetransQlen_Type(Gauge32):
    """Custom type mscVrIpOspfVirtNbrLsRetransQlen based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpOspfVirtNbrLsRetransQlen_Type.__name__ = "Gauge32"
_MscVrIpOspfVirtNbrLsRetransQlen_Object = MibTableColumn
mscVrIpOspfVirtNbrLsRetransQlen = _MscVrIpOspfVirtNbrLsRetransQlen_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 9, 10, 1, 5),
    _MscVrIpOspfVirtNbrLsRetransQlen_Type()
)
mscVrIpOspfVirtNbrLsRetransQlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfVirtNbrLsRetransQlen.setStatus("mandatory")


class _MscVrIpOspfVirtNbrExchangeStatus_Type(Integer32):
    """Custom type mscVrIpOspfVirtNbrExchangeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_MscVrIpOspfVirtNbrExchangeStatus_Type.__name__ = "Integer32"
_MscVrIpOspfVirtNbrExchangeStatus_Object = MibTableColumn
mscVrIpOspfVirtNbrExchangeStatus = _MscVrIpOspfVirtNbrExchangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 9, 10, 1, 6),
    _MscVrIpOspfVirtNbrExchangeStatus_Type()
)
mscVrIpOspfVirtNbrExchangeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfVirtNbrExchangeStatus.setStatus("mandatory")
_MscVrIpOspfNbr_ObjectIdentity = ObjectIdentity
mscVrIpOspfNbr = _MscVrIpOspfNbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 10)
)
_MscVrIpOspfNbrRowStatusTable_Object = MibTable
mscVrIpOspfNbrRowStatusTable = _MscVrIpOspfNbrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 10, 1)
)
if mibBuilder.loadTexts:
    mscVrIpOspfNbrRowStatusTable.setStatus("mandatory")
_MscVrIpOspfNbrRowStatusEntry_Object = MibTableRow
mscVrIpOspfNbrRowStatusEntry = _MscVrIpOspfNbrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 10, 1, 1)
)
mscVrIpOspfNbrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfNbrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfNbrRowStatusEntry.setStatus("mandatory")
_MscVrIpOspfNbrRowStatus_Type = RowStatus
_MscVrIpOspfNbrRowStatus_Object = MibTableColumn
mscVrIpOspfNbrRowStatus = _MscVrIpOspfNbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 10, 1, 1, 1),
    _MscVrIpOspfNbrRowStatus_Type()
)
mscVrIpOspfNbrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfNbrRowStatus.setStatus("mandatory")
_MscVrIpOspfNbrComponentName_Type = DisplayString
_MscVrIpOspfNbrComponentName_Object = MibTableColumn
mscVrIpOspfNbrComponentName = _MscVrIpOspfNbrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 10, 1, 1, 2),
    _MscVrIpOspfNbrComponentName_Type()
)
mscVrIpOspfNbrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfNbrComponentName.setStatus("mandatory")
_MscVrIpOspfNbrStorageType_Type = StorageType
_MscVrIpOspfNbrStorageType_Object = MibTableColumn
mscVrIpOspfNbrStorageType = _MscVrIpOspfNbrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 10, 1, 1, 4),
    _MscVrIpOspfNbrStorageType_Type()
)
mscVrIpOspfNbrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfNbrStorageType.setStatus("mandatory")
_MscVrIpOspfNbrAddressIndex_Type = IpAddress
_MscVrIpOspfNbrAddressIndex_Object = MibTableColumn
mscVrIpOspfNbrAddressIndex = _MscVrIpOspfNbrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 10, 1, 1, 10),
    _MscVrIpOspfNbrAddressIndex_Type()
)
mscVrIpOspfNbrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpOspfNbrAddressIndex.setStatus("mandatory")


class _MscVrIpOspfNbrAddressLessIndex_Type(Integer32):
    """Custom type mscVrIpOspfNbrAddressLessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_MscVrIpOspfNbrAddressLessIndex_Type.__name__ = "Integer32"
_MscVrIpOspfNbrAddressLessIndex_Object = MibTableColumn
mscVrIpOspfNbrAddressLessIndex = _MscVrIpOspfNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 10, 1, 1, 11),
    _MscVrIpOspfNbrAddressLessIndex_Type()
)
mscVrIpOspfNbrAddressLessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpOspfNbrAddressLessIndex.setStatus("mandatory")
_MscVrIpOspfNbrOperTable_Object = MibTable
mscVrIpOspfNbrOperTable = _MscVrIpOspfNbrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 10, 10)
)
if mibBuilder.loadTexts:
    mscVrIpOspfNbrOperTable.setStatus("mandatory")
_MscVrIpOspfNbrOperEntry_Object = MibTableRow
mscVrIpOspfNbrOperEntry = _MscVrIpOspfNbrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 10, 10, 1)
)
mscVrIpOspfNbrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfNbrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfNbrOperEntry.setStatus("mandatory")
_MscVrIpOspfNbrRtrId_Type = IpAddress
_MscVrIpOspfNbrRtrId_Object = MibTableColumn
mscVrIpOspfNbrRtrId = _MscVrIpOspfNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 10, 10, 1, 1),
    _MscVrIpOspfNbrRtrId_Type()
)
mscVrIpOspfNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfNbrRtrId.setStatus("mandatory")


class _MscVrIpOspfNbrOptions_Type(Unsigned32):
    """Custom type mscVrIpOspfNbrOptions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscVrIpOspfNbrOptions_Type.__name__ = "Unsigned32"
_MscVrIpOspfNbrOptions_Object = MibTableColumn
mscVrIpOspfNbrOptions = _MscVrIpOspfNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 10, 10, 1, 2),
    _MscVrIpOspfNbrOptions_Type()
)
mscVrIpOspfNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfNbrOptions.setStatus("mandatory")


class _MscVrIpOspfNbrPriority_Type(Unsigned32):
    """Custom type mscVrIpOspfNbrPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrIpOspfNbrPriority_Type.__name__ = "Unsigned32"
_MscVrIpOspfNbrPriority_Object = MibTableColumn
mscVrIpOspfNbrPriority = _MscVrIpOspfNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 10, 10, 1, 3),
    _MscVrIpOspfNbrPriority_Type()
)
mscVrIpOspfNbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfNbrPriority.setStatus("mandatory")


class _MscVrIpOspfNbrState_Type(Integer32):
    """Custom type mscVrIpOspfNbrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("attempt", 2),
          ("down", 1),
          ("exchange", 6),
          ("exchangeStart", 5),
          ("full", 8),
          ("init", 3),
          ("loading", 7),
          ("twoWay", 4))
    )


_MscVrIpOspfNbrState_Type.__name__ = "Integer32"
_MscVrIpOspfNbrState_Object = MibTableColumn
mscVrIpOspfNbrState = _MscVrIpOspfNbrState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 10, 10, 1, 4),
    _MscVrIpOspfNbrState_Type()
)
mscVrIpOspfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfNbrState.setStatus("mandatory")
_MscVrIpOspfNbrEvents_Type = Counter32
_MscVrIpOspfNbrEvents_Object = MibTableColumn
mscVrIpOspfNbrEvents = _MscVrIpOspfNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 10, 10, 1, 5),
    _MscVrIpOspfNbrEvents_Type()
)
mscVrIpOspfNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfNbrEvents.setStatus("mandatory")


class _MscVrIpOspfNbrLsRetransQlen_Type(Gauge32):
    """Custom type mscVrIpOspfNbrLsRetransQlen based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpOspfNbrLsRetransQlen_Type.__name__ = "Gauge32"
_MscVrIpOspfNbrLsRetransQlen_Object = MibTableColumn
mscVrIpOspfNbrLsRetransQlen = _MscVrIpOspfNbrLsRetransQlen_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 10, 10, 1, 6),
    _MscVrIpOspfNbrLsRetransQlen_Type()
)
mscVrIpOspfNbrLsRetransQlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfNbrLsRetransQlen.setStatus("mandatory")


class _MscVrIpOspfNbrNbmaNbrStatus_Type(Integer32):
    """Custom type mscVrIpOspfNbrNbmaNbrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_MscVrIpOspfNbrNbmaNbrStatus_Type.__name__ = "Integer32"
_MscVrIpOspfNbrNbmaNbrStatus_Object = MibTableColumn
mscVrIpOspfNbrNbmaNbrStatus = _MscVrIpOspfNbrNbmaNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 10, 10, 1, 7),
    _MscVrIpOspfNbrNbmaNbrStatus_Type()
)
mscVrIpOspfNbrNbmaNbrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfNbrNbmaNbrStatus.setStatus("mandatory")


class _MscVrIpOspfNbrExchangeStatus_Type(Integer32):
    """Custom type mscVrIpOspfNbrExchangeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_MscVrIpOspfNbrExchangeStatus_Type.__name__ = "Integer32"
_MscVrIpOspfNbrExchangeStatus_Object = MibTableColumn
mscVrIpOspfNbrExchangeStatus = _MscVrIpOspfNbrExchangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 10, 10, 1, 8),
    _MscVrIpOspfNbrExchangeStatus_Type()
)
mscVrIpOspfNbrExchangeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfNbrExchangeStatus.setStatus("mandatory")


class _MscVrIpOspfNbrPermanence_Type(Integer32):
    """Custom type mscVrIpOspfNbrPermanence based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("permanent", 2))
    )


_MscVrIpOspfNbrPermanence_Type.__name__ = "Integer32"
_MscVrIpOspfNbrPermanence_Object = MibTableColumn
mscVrIpOspfNbrPermanence = _MscVrIpOspfNbrPermanence_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 10, 10, 1, 11),
    _MscVrIpOspfNbrPermanence_Type()
)
mscVrIpOspfNbrPermanence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfNbrPermanence.setStatus("mandatory")
_MscVrIpOspfLsdb_ObjectIdentity = ObjectIdentity
mscVrIpOspfLsdb = _MscVrIpOspfLsdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 11)
)
_MscVrIpOspfLsdbRowStatusTable_Object = MibTable
mscVrIpOspfLsdbRowStatusTable = _MscVrIpOspfLsdbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 11, 1)
)
if mibBuilder.loadTexts:
    mscVrIpOspfLsdbRowStatusTable.setStatus("mandatory")
_MscVrIpOspfLsdbRowStatusEntry_Object = MibTableRow
mscVrIpOspfLsdbRowStatusEntry = _MscVrIpOspfLsdbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 11, 1, 1)
)
mscVrIpOspfLsdbRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfLsdbAreaIdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfLsdbLsdbTypeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfLsdbLsIdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfLsdbRouterIdIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfLsdbRowStatusEntry.setStatus("mandatory")
_MscVrIpOspfLsdbRowStatus_Type = RowStatus
_MscVrIpOspfLsdbRowStatus_Object = MibTableColumn
mscVrIpOspfLsdbRowStatus = _MscVrIpOspfLsdbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 11, 1, 1, 1),
    _MscVrIpOspfLsdbRowStatus_Type()
)
mscVrIpOspfLsdbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfLsdbRowStatus.setStatus("mandatory")
_MscVrIpOspfLsdbComponentName_Type = DisplayString
_MscVrIpOspfLsdbComponentName_Object = MibTableColumn
mscVrIpOspfLsdbComponentName = _MscVrIpOspfLsdbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 11, 1, 1, 2),
    _MscVrIpOspfLsdbComponentName_Type()
)
mscVrIpOspfLsdbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfLsdbComponentName.setStatus("mandatory")
_MscVrIpOspfLsdbStorageType_Type = StorageType
_MscVrIpOspfLsdbStorageType_Object = MibTableColumn
mscVrIpOspfLsdbStorageType = _MscVrIpOspfLsdbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 11, 1, 1, 4),
    _MscVrIpOspfLsdbStorageType_Type()
)
mscVrIpOspfLsdbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfLsdbStorageType.setStatus("mandatory")
_MscVrIpOspfLsdbAreaIdIndex_Type = IpAddress
_MscVrIpOspfLsdbAreaIdIndex_Object = MibTableColumn
mscVrIpOspfLsdbAreaIdIndex = _MscVrIpOspfLsdbAreaIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 11, 1, 1, 10),
    _MscVrIpOspfLsdbAreaIdIndex_Type()
)
mscVrIpOspfLsdbAreaIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpOspfLsdbAreaIdIndex.setStatus("mandatory")


class _MscVrIpOspfLsdbLsdbTypeIndex_Type(Integer32):
    """Custom type mscVrIpOspfLsdbLsdbTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_MscVrIpOspfLsdbLsdbTypeIndex_Type.__name__ = "Integer32"
_MscVrIpOspfLsdbLsdbTypeIndex_Object = MibTableColumn
mscVrIpOspfLsdbLsdbTypeIndex = _MscVrIpOspfLsdbLsdbTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 11, 1, 1, 11),
    _MscVrIpOspfLsdbLsdbTypeIndex_Type()
)
mscVrIpOspfLsdbLsdbTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpOspfLsdbLsdbTypeIndex.setStatus("mandatory")
_MscVrIpOspfLsdbLsIdIndex_Type = IpAddress
_MscVrIpOspfLsdbLsIdIndex_Object = MibTableColumn
mscVrIpOspfLsdbLsIdIndex = _MscVrIpOspfLsdbLsIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 11, 1, 1, 12),
    _MscVrIpOspfLsdbLsIdIndex_Type()
)
mscVrIpOspfLsdbLsIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpOspfLsdbLsIdIndex.setStatus("mandatory")
_MscVrIpOspfLsdbRouterIdIndex_Type = IpAddress
_MscVrIpOspfLsdbRouterIdIndex_Object = MibTableColumn
mscVrIpOspfLsdbRouterIdIndex = _MscVrIpOspfLsdbRouterIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 11, 1, 1, 13),
    _MscVrIpOspfLsdbRouterIdIndex_Type()
)
mscVrIpOspfLsdbRouterIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpOspfLsdbRouterIdIndex.setStatus("mandatory")
_MscVrIpOspfLsdbOperTable_Object = MibTable
mscVrIpOspfLsdbOperTable = _MscVrIpOspfLsdbOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 11, 10)
)
if mibBuilder.loadTexts:
    mscVrIpOspfLsdbOperTable.setStatus("mandatory")
_MscVrIpOspfLsdbOperEntry_Object = MibTableRow
mscVrIpOspfLsdbOperEntry = _MscVrIpOspfLsdbOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 11, 10, 1)
)
mscVrIpOspfLsdbOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfLsdbAreaIdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfLsdbLsdbTypeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfLsdbLsIdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfLsdbRouterIdIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfLsdbOperEntry.setStatus("mandatory")


class _MscVrIpOspfLsdbSequence_Type(Unsigned32):
    """Custom type mscVrIpOspfLsdbSequence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpOspfLsdbSequence_Type.__name__ = "Unsigned32"
_MscVrIpOspfLsdbSequence_Object = MibTableColumn
mscVrIpOspfLsdbSequence = _MscVrIpOspfLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 11, 10, 1, 1),
    _MscVrIpOspfLsdbSequence_Type()
)
mscVrIpOspfLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfLsdbSequence.setStatus("mandatory")


class _MscVrIpOspfLsdbAge_Type(Gauge32):
    """Custom type mscVrIpOspfLsdbAge based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_MscVrIpOspfLsdbAge_Type.__name__ = "Gauge32"
_MscVrIpOspfLsdbAge_Object = MibTableColumn
mscVrIpOspfLsdbAge = _MscVrIpOspfLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 11, 10, 1, 2),
    _MscVrIpOspfLsdbAge_Type()
)
mscVrIpOspfLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfLsdbAge.setStatus("mandatory")


class _MscVrIpOspfLsdbChecksum_Type(Unsigned32):
    """Custom type mscVrIpOspfLsdbChecksum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpOspfLsdbChecksum_Type.__name__ = "Unsigned32"
_MscVrIpOspfLsdbChecksum_Object = MibTableColumn
mscVrIpOspfLsdbChecksum = _MscVrIpOspfLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 11, 10, 1, 3),
    _MscVrIpOspfLsdbChecksum_Type()
)
mscVrIpOspfLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfLsdbChecksum.setStatus("mandatory")


class _MscVrIpOspfLsdbAdvertisement_Type(HexString):
    """Custom type mscVrIpOspfLsdbAdvertisement based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_MscVrIpOspfLsdbAdvertisement_Type.__name__ = "HexString"
_MscVrIpOspfLsdbAdvertisement_Object = MibTableColumn
mscVrIpOspfLsdbAdvertisement = _MscVrIpOspfLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 11, 10, 1, 4),
    _MscVrIpOspfLsdbAdvertisement_Type()
)
mscVrIpOspfLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfLsdbAdvertisement.setStatus("mandatory")
_MscVrIpOspfExtLsdb_ObjectIdentity = ObjectIdentity
mscVrIpOspfExtLsdb = _MscVrIpOspfExtLsdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 12)
)
_MscVrIpOspfExtLsdbRowStatusTable_Object = MibTable
mscVrIpOspfExtLsdbRowStatusTable = _MscVrIpOspfExtLsdbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 12, 1)
)
if mibBuilder.loadTexts:
    mscVrIpOspfExtLsdbRowStatusTable.setStatus("mandatory")
_MscVrIpOspfExtLsdbRowStatusEntry_Object = MibTableRow
mscVrIpOspfExtLsdbRowStatusEntry = _MscVrIpOspfExtLsdbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 12, 1, 1)
)
mscVrIpOspfExtLsdbRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfExtLsdbLsdbTypeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfExtLsdbLsIdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfExtLsdbRouterIdIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfExtLsdbRowStatusEntry.setStatus("mandatory")
_MscVrIpOspfExtLsdbRowStatus_Type = RowStatus
_MscVrIpOspfExtLsdbRowStatus_Object = MibTableColumn
mscVrIpOspfExtLsdbRowStatus = _MscVrIpOspfExtLsdbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 12, 1, 1, 1),
    _MscVrIpOspfExtLsdbRowStatus_Type()
)
mscVrIpOspfExtLsdbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfExtLsdbRowStatus.setStatus("mandatory")
_MscVrIpOspfExtLsdbComponentName_Type = DisplayString
_MscVrIpOspfExtLsdbComponentName_Object = MibTableColumn
mscVrIpOspfExtLsdbComponentName = _MscVrIpOspfExtLsdbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 12, 1, 1, 2),
    _MscVrIpOspfExtLsdbComponentName_Type()
)
mscVrIpOspfExtLsdbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfExtLsdbComponentName.setStatus("mandatory")
_MscVrIpOspfExtLsdbStorageType_Type = StorageType
_MscVrIpOspfExtLsdbStorageType_Object = MibTableColumn
mscVrIpOspfExtLsdbStorageType = _MscVrIpOspfExtLsdbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 12, 1, 1, 4),
    _MscVrIpOspfExtLsdbStorageType_Type()
)
mscVrIpOspfExtLsdbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfExtLsdbStorageType.setStatus("mandatory")


class _MscVrIpOspfExtLsdbLsdbTypeIndex_Type(Integer32):
    """Custom type mscVrIpOspfExtLsdbLsdbTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_MscVrIpOspfExtLsdbLsdbTypeIndex_Type.__name__ = "Integer32"
_MscVrIpOspfExtLsdbLsdbTypeIndex_Object = MibTableColumn
mscVrIpOspfExtLsdbLsdbTypeIndex = _MscVrIpOspfExtLsdbLsdbTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 12, 1, 1, 10),
    _MscVrIpOspfExtLsdbLsdbTypeIndex_Type()
)
mscVrIpOspfExtLsdbLsdbTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpOspfExtLsdbLsdbTypeIndex.setStatus("mandatory")
_MscVrIpOspfExtLsdbLsIdIndex_Type = IpAddress
_MscVrIpOspfExtLsdbLsIdIndex_Object = MibTableColumn
mscVrIpOspfExtLsdbLsIdIndex = _MscVrIpOspfExtLsdbLsIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 12, 1, 1, 11),
    _MscVrIpOspfExtLsdbLsIdIndex_Type()
)
mscVrIpOspfExtLsdbLsIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpOspfExtLsdbLsIdIndex.setStatus("mandatory")
_MscVrIpOspfExtLsdbRouterIdIndex_Type = IpAddress
_MscVrIpOspfExtLsdbRouterIdIndex_Object = MibTableColumn
mscVrIpOspfExtLsdbRouterIdIndex = _MscVrIpOspfExtLsdbRouterIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 12, 1, 1, 12),
    _MscVrIpOspfExtLsdbRouterIdIndex_Type()
)
mscVrIpOspfExtLsdbRouterIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpOspfExtLsdbRouterIdIndex.setStatus("mandatory")
_MscVrIpOspfExtLsdbOperTable_Object = MibTable
mscVrIpOspfExtLsdbOperTable = _MscVrIpOspfExtLsdbOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 12, 10)
)
if mibBuilder.loadTexts:
    mscVrIpOspfExtLsdbOperTable.setStatus("mandatory")
_MscVrIpOspfExtLsdbOperEntry_Object = MibTableRow
mscVrIpOspfExtLsdbOperEntry = _MscVrIpOspfExtLsdbOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 12, 10, 1)
)
mscVrIpOspfExtLsdbOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfExtLsdbLsdbTypeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfExtLsdbLsIdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfExtLsdbRouterIdIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfExtLsdbOperEntry.setStatus("mandatory")


class _MscVrIpOspfExtLsdbSequence_Type(Unsigned32):
    """Custom type mscVrIpOspfExtLsdbSequence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpOspfExtLsdbSequence_Type.__name__ = "Unsigned32"
_MscVrIpOspfExtLsdbSequence_Object = MibTableColumn
mscVrIpOspfExtLsdbSequence = _MscVrIpOspfExtLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 12, 10, 1, 1),
    _MscVrIpOspfExtLsdbSequence_Type()
)
mscVrIpOspfExtLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfExtLsdbSequence.setStatus("mandatory")


class _MscVrIpOspfExtLsdbAge_Type(Gauge32):
    """Custom type mscVrIpOspfExtLsdbAge based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_MscVrIpOspfExtLsdbAge_Type.__name__ = "Gauge32"
_MscVrIpOspfExtLsdbAge_Object = MibTableColumn
mscVrIpOspfExtLsdbAge = _MscVrIpOspfExtLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 12, 10, 1, 2),
    _MscVrIpOspfExtLsdbAge_Type()
)
mscVrIpOspfExtLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfExtLsdbAge.setStatus("mandatory")


class _MscVrIpOspfExtLsdbChecksum_Type(Unsigned32):
    """Custom type mscVrIpOspfExtLsdbChecksum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpOspfExtLsdbChecksum_Type.__name__ = "Unsigned32"
_MscVrIpOspfExtLsdbChecksum_Object = MibTableColumn
mscVrIpOspfExtLsdbChecksum = _MscVrIpOspfExtLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 12, 10, 1, 3),
    _MscVrIpOspfExtLsdbChecksum_Type()
)
mscVrIpOspfExtLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfExtLsdbChecksum.setStatus("mandatory")


class _MscVrIpOspfExtLsdbAdvertisement_Type(HexString):
    """Custom type mscVrIpOspfExtLsdbAdvertisement based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_MscVrIpOspfExtLsdbAdvertisement_Type.__name__ = "HexString"
_MscVrIpOspfExtLsdbAdvertisement_Object = MibTableColumn
mscVrIpOspfExtLsdbAdvertisement = _MscVrIpOspfExtLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 12, 10, 1, 4),
    _MscVrIpOspfExtLsdbAdvertisement_Type()
)
mscVrIpOspfExtLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfExtLsdbAdvertisement.setStatus("mandatory")
_MscVrIpOspfProvTable_Object = MibTable
mscVrIpOspfProvTable = _MscVrIpOspfProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 100)
)
if mibBuilder.loadTexts:
    mscVrIpOspfProvTable.setStatus("mandatory")
_MscVrIpOspfProvEntry_Object = MibTableRow
mscVrIpOspfProvEntry = _MscVrIpOspfProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 100, 1)
)
mscVrIpOspfProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfProvEntry.setStatus("mandatory")
_MscVrIpOspfRouterId_Type = RouterID
_MscVrIpOspfRouterId_Object = MibTableColumn
mscVrIpOspfRouterId = _MscVrIpOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 100, 1, 1),
    _MscVrIpOspfRouterId_Type()
)
mscVrIpOspfRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfRouterId.setStatus("mandatory")


class _MscVrIpOspfSnmpAdminStatus_Type(Integer32):
    """Custom type mscVrIpOspfSnmpAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscVrIpOspfSnmpAdminStatus_Type.__name__ = "Integer32"
_MscVrIpOspfSnmpAdminStatus_Object = MibTableColumn
mscVrIpOspfSnmpAdminStatus = _MscVrIpOspfSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 100, 1, 2),
    _MscVrIpOspfSnmpAdminStatus_Type()
)
mscVrIpOspfSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfSnmpAdminStatus.setStatus("mandatory")


class _MscVrIpOspfAsBdrRtrStatus_Type(Integer32):
    """Custom type mscVrIpOspfAsBdrRtrStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_MscVrIpOspfAsBdrRtrStatus_Type.__name__ = "Integer32"
_MscVrIpOspfAsBdrRtrStatus_Object = MibTableColumn
mscVrIpOspfAsBdrRtrStatus = _MscVrIpOspfAsBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 100, 1, 3),
    _MscVrIpOspfAsBdrRtrStatus_Type()
)
mscVrIpOspfAsBdrRtrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfAsBdrRtrStatus.setStatus("mandatory")


class _MscVrIpOspfTosSupport_Type(Integer32):
    """Custom type mscVrIpOspfTosSupport based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("false", 2)
    )


_MscVrIpOspfTosSupport_Type.__name__ = "Integer32"
_MscVrIpOspfTosSupport_Object = MibTableColumn
mscVrIpOspfTosSupport = _MscVrIpOspfTosSupport_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 100, 1, 4),
    _MscVrIpOspfTosSupport_Type()
)
mscVrIpOspfTosSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfTosSupport.setStatus("mandatory")


class _MscVrIpOspfExtLsdbLimit_Type(Integer32):
    """Custom type mscVrIpOspfExtLsdbLimit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_MscVrIpOspfExtLsdbLimit_Type.__name__ = "Integer32"
_MscVrIpOspfExtLsdbLimit_Object = MibTableColumn
mscVrIpOspfExtLsdbLimit = _MscVrIpOspfExtLsdbLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 100, 1, 5),
    _MscVrIpOspfExtLsdbLimit_Type()
)
mscVrIpOspfExtLsdbLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfExtLsdbLimit.setStatus("mandatory")


class _MscVrIpOspfMulticastForward_Type(Unsigned32):
    """Custom type mscVrIpOspfMulticastForward based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_MscVrIpOspfMulticastForward_Type.__name__ = "Unsigned32"
_MscVrIpOspfMulticastForward_Object = MibTableColumn
mscVrIpOspfMulticastForward = _MscVrIpOspfMulticastForward_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 100, 1, 6),
    _MscVrIpOspfMulticastForward_Type()
)
mscVrIpOspfMulticastForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfMulticastForward.setStatus("mandatory")


class _MscVrIpOspfMigrateRip_Type(Integer32):
    """Custom type mscVrIpOspfMigrateRip based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MscVrIpOspfMigrateRip_Type.__name__ = "Integer32"
_MscVrIpOspfMigrateRip_Object = MibTableColumn
mscVrIpOspfMigrateRip = _MscVrIpOspfMigrateRip_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 100, 1, 7),
    _MscVrIpOspfMigrateRip_Type()
)
mscVrIpOspfMigrateRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfMigrateRip.setStatus("mandatory")


class _MscVrIpOspfGenerateDefaultRouteMetric_Type(Integer32):
    """Custom type mscVrIpOspfGenerateDefaultRouteMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MscVrIpOspfGenerateDefaultRouteMetric_Type.__name__ = "Integer32"
_MscVrIpOspfGenerateDefaultRouteMetric_Object = MibTableColumn
mscVrIpOspfGenerateDefaultRouteMetric = _MscVrIpOspfGenerateDefaultRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 100, 1, 8),
    _MscVrIpOspfGenerateDefaultRouteMetric_Type()
)
mscVrIpOspfGenerateDefaultRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfGenerateDefaultRouteMetric.setStatus("mandatory")


class _MscVrIpOspfRedistributeIbgp_Type(Integer32):
    """Custom type mscVrIpOspfRedistributeIbgp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_MscVrIpOspfRedistributeIbgp_Type.__name__ = "Integer32"
_MscVrIpOspfRedistributeIbgp_Object = MibTableColumn
mscVrIpOspfRedistributeIbgp = _MscVrIpOspfRedistributeIbgp_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 100, 1, 9),
    _MscVrIpOspfRedistributeIbgp_Type()
)
mscVrIpOspfRedistributeIbgp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpOspfRedistributeIbgp.setStatus("mandatory")
_MscVrIpOspfOperTable_Object = MibTable
mscVrIpOspfOperTable = _MscVrIpOspfOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 101)
)
if mibBuilder.loadTexts:
    mscVrIpOspfOperTable.setStatus("mandatory")
_MscVrIpOspfOperEntry_Object = MibTableRow
mscVrIpOspfOperEntry = _MscVrIpOspfOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 101, 1)
)
mscVrIpOspfOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfOperEntry.setStatus("mandatory")


class _MscVrIpOspfVersionNumber_Type(Unsigned32):
    """Custom type mscVrIpOspfVersionNumber based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_MscVrIpOspfVersionNumber_Type.__name__ = "Unsigned32"
_MscVrIpOspfVersionNumber_Object = MibTableColumn
mscVrIpOspfVersionNumber = _MscVrIpOspfVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 101, 1, 1),
    _MscVrIpOspfVersionNumber_Type()
)
mscVrIpOspfVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfVersionNumber.setStatus("mandatory")


class _MscVrIpOspfAreaBdrRtrStatus_Type(Integer32):
    """Custom type mscVrIpOspfAreaBdrRtrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_MscVrIpOspfAreaBdrRtrStatus_Type.__name__ = "Integer32"
_MscVrIpOspfAreaBdrRtrStatus_Object = MibTableColumn
mscVrIpOspfAreaBdrRtrStatus = _MscVrIpOspfAreaBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 101, 1, 2),
    _MscVrIpOspfAreaBdrRtrStatus_Type()
)
mscVrIpOspfAreaBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfAreaBdrRtrStatus.setStatus("mandatory")


class _MscVrIpOspfExternLsaCount_Type(Gauge32):
    """Custom type mscVrIpOspfExternLsaCount based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpOspfExternLsaCount_Type.__name__ = "Gauge32"
_MscVrIpOspfExternLsaCount_Object = MibTableColumn
mscVrIpOspfExternLsaCount = _MscVrIpOspfExternLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 101, 1, 3),
    _MscVrIpOspfExternLsaCount_Type()
)
mscVrIpOspfExternLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfExternLsaCount.setStatus("mandatory")


class _MscVrIpOspfExternLsaChecksumSum_Type(Unsigned32):
    """Custom type mscVrIpOspfExternLsaChecksumSum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpOspfExternLsaChecksumSum_Type.__name__ = "Unsigned32"
_MscVrIpOspfExternLsaChecksumSum_Object = MibTableColumn
mscVrIpOspfExternLsaChecksumSum = _MscVrIpOspfExternLsaChecksumSum_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 101, 1, 4),
    _MscVrIpOspfExternLsaChecksumSum_Type()
)
mscVrIpOspfExternLsaChecksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfExternLsaChecksumSum.setStatus("mandatory")
_MscVrIpOspfOriginateNewLsas_Type = Counter32
_MscVrIpOspfOriginateNewLsas_Object = MibTableColumn
mscVrIpOspfOriginateNewLsas = _MscVrIpOspfOriginateNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 101, 1, 5),
    _MscVrIpOspfOriginateNewLsas_Type()
)
mscVrIpOspfOriginateNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfOriginateNewLsas.setStatus("mandatory")
_MscVrIpOspfRxNewLsas_Type = Counter32
_MscVrIpOspfRxNewLsas_Object = MibTableColumn
mscVrIpOspfRxNewLsas = _MscVrIpOspfRxNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 101, 1, 6),
    _MscVrIpOspfRxNewLsas_Type()
)
mscVrIpOspfRxNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfRxNewLsas.setStatus("mandatory")
_MscVrIpOspfStateTable_Object = MibTable
mscVrIpOspfStateTable = _MscVrIpOspfStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 102)
)
if mibBuilder.loadTexts:
    mscVrIpOspfStateTable.setStatus("mandatory")
_MscVrIpOspfStateEntry_Object = MibTableRow
mscVrIpOspfStateEntry = _MscVrIpOspfStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 102, 1)
)
mscVrIpOspfStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfStateEntry.setStatus("mandatory")


class _MscVrIpOspfAdminState_Type(Integer32):
    """Custom type mscVrIpOspfAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_MscVrIpOspfAdminState_Type.__name__ = "Integer32"
_MscVrIpOspfAdminState_Object = MibTableColumn
mscVrIpOspfAdminState = _MscVrIpOspfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 102, 1, 1),
    _MscVrIpOspfAdminState_Type()
)
mscVrIpOspfAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfAdminState.setStatus("mandatory")


class _MscVrIpOspfOperationalState_Type(Integer32):
    """Custom type mscVrIpOspfOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MscVrIpOspfOperationalState_Type.__name__ = "Integer32"
_MscVrIpOspfOperationalState_Object = MibTableColumn
mscVrIpOspfOperationalState = _MscVrIpOspfOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 102, 1, 2),
    _MscVrIpOspfOperationalState_Type()
)
mscVrIpOspfOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfOperationalState.setStatus("mandatory")


class _MscVrIpOspfUsageState_Type(Integer32):
    """Custom type mscVrIpOspfUsageState based on Integer32"""
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
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_MscVrIpOspfUsageState_Type.__name__ = "Integer32"
_MscVrIpOspfUsageState_Object = MibTableColumn
mscVrIpOspfUsageState = _MscVrIpOspfUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 102, 1, 3),
    _MscVrIpOspfUsageState_Type()
)
mscVrIpOspfUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfUsageState.setStatus("mandatory")
_MscVrIpOspfOperStatusTable_Object = MibTable
mscVrIpOspfOperStatusTable = _MscVrIpOspfOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 105)
)
if mibBuilder.loadTexts:
    mscVrIpOspfOperStatusTable.setStatus("mandatory")
_MscVrIpOspfOperStatusEntry_Object = MibTableRow
mscVrIpOspfOperStatusEntry = _MscVrIpOspfOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 105, 1)
)
mscVrIpOspfOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpOspfIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOspfOperStatusEntry.setStatus("mandatory")


class _MscVrIpOspfSnmpOperStatus_Type(Integer32):
    """Custom type mscVrIpOspfSnmpOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscVrIpOspfSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrIpOspfSnmpOperStatus_Object = MibTableColumn
mscVrIpOspfSnmpOperStatus = _MscVrIpOspfSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 7, 105, 1, 1),
    _MscVrIpOspfSnmpOperStatus_Type()
)
mscVrIpOspfSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOspfSnmpOperStatus.setStatus("mandatory")
_MscVrIpRip_ObjectIdentity = ObjectIdentity
mscVrIpRip = _MscVrIpRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8)
)
_MscVrIpRipRowStatusTable_Object = MibTable
mscVrIpRipRowStatusTable = _MscVrIpRipRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 1)
)
if mibBuilder.loadTexts:
    mscVrIpRipRowStatusTable.setStatus("mandatory")
_MscVrIpRipRowStatusEntry_Object = MibTableRow
mscVrIpRipRowStatusEntry = _MscVrIpRipRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 1, 1)
)
mscVrIpRipRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRipIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpRipRowStatusEntry.setStatus("mandatory")
_MscVrIpRipRowStatus_Type = RowStatus
_MscVrIpRipRowStatus_Object = MibTableColumn
mscVrIpRipRowStatus = _MscVrIpRipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 1, 1, 1),
    _MscVrIpRipRowStatus_Type()
)
mscVrIpRipRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRipRowStatus.setStatus("mandatory")
_MscVrIpRipComponentName_Type = DisplayString
_MscVrIpRipComponentName_Object = MibTableColumn
mscVrIpRipComponentName = _MscVrIpRipComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 1, 1, 2),
    _MscVrIpRipComponentName_Type()
)
mscVrIpRipComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRipComponentName.setStatus("mandatory")
_MscVrIpRipStorageType_Type = StorageType
_MscVrIpRipStorageType_Object = MibTableColumn
mscVrIpRipStorageType = _MscVrIpRipStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 1, 1, 4),
    _MscVrIpRipStorageType_Type()
)
mscVrIpRipStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRipStorageType.setStatus("mandatory")
_MscVrIpRipIndex_Type = NonReplicated
_MscVrIpRipIndex_Object = MibTableColumn
mscVrIpRipIndex = _MscVrIpRipIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 1, 1, 10),
    _MscVrIpRipIndex_Type()
)
mscVrIpRipIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpRipIndex.setStatus("mandatory")
_MscVrIpRipImport_ObjectIdentity = ObjectIdentity
mscVrIpRipImport = _MscVrIpRipImport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 2)
)
_MscVrIpRipImportRowStatusTable_Object = MibTable
mscVrIpRipImportRowStatusTable = _MscVrIpRipImportRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpRipImportRowStatusTable.setStatus("mandatory")
_MscVrIpRipImportRowStatusEntry_Object = MibTableRow
mscVrIpRipImportRowStatusEntry = _MscVrIpRipImportRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 2, 1, 1)
)
mscVrIpRipImportRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRipIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRipImportIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpRipImportRowStatusEntry.setStatus("mandatory")
_MscVrIpRipImportRowStatus_Type = RowStatus
_MscVrIpRipImportRowStatus_Object = MibTableColumn
mscVrIpRipImportRowStatus = _MscVrIpRipImportRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 2, 1, 1, 1),
    _MscVrIpRipImportRowStatus_Type()
)
mscVrIpRipImportRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRipImportRowStatus.setStatus("mandatory")
_MscVrIpRipImportComponentName_Type = DisplayString
_MscVrIpRipImportComponentName_Object = MibTableColumn
mscVrIpRipImportComponentName = _MscVrIpRipImportComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 2, 1, 1, 2),
    _MscVrIpRipImportComponentName_Type()
)
mscVrIpRipImportComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRipImportComponentName.setStatus("mandatory")
_MscVrIpRipImportStorageType_Type = StorageType
_MscVrIpRipImportStorageType_Object = MibTableColumn
mscVrIpRipImportStorageType = _MscVrIpRipImportStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 2, 1, 1, 4),
    _MscVrIpRipImportStorageType_Type()
)
mscVrIpRipImportStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRipImportStorageType.setStatus("mandatory")


class _MscVrIpRipImportIndex_Type(Integer32):
    """Custom type mscVrIpRipImportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpRipImportIndex_Type.__name__ = "Integer32"
_MscVrIpRipImportIndex_Object = MibTableColumn
mscVrIpRipImportIndex = _MscVrIpRipImportIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 2, 1, 1, 10),
    _MscVrIpRipImportIndex_Type()
)
mscVrIpRipImportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpRipImportIndex.setStatus("mandatory")
_MscVrIpRipImportNet_ObjectIdentity = ObjectIdentity
mscVrIpRipImportNet = _MscVrIpRipImportNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 2, 2)
)
_MscVrIpRipImportNetRowStatusTable_Object = MibTable
mscVrIpRipImportNetRowStatusTable = _MscVrIpRipImportNetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpRipImportNetRowStatusTable.setStatus("mandatory")
_MscVrIpRipImportNetRowStatusEntry_Object = MibTableRow
mscVrIpRipImportNetRowStatusEntry = _MscVrIpRipImportNetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 2, 2, 1, 1)
)
mscVrIpRipImportNetRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRipIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRipImportIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRipImportNetIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpRipImportNetRowStatusEntry.setStatus("mandatory")
_MscVrIpRipImportNetRowStatus_Type = RowStatus
_MscVrIpRipImportNetRowStatus_Object = MibTableColumn
mscVrIpRipImportNetRowStatus = _MscVrIpRipImportNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 2, 2, 1, 1, 1),
    _MscVrIpRipImportNetRowStatus_Type()
)
mscVrIpRipImportNetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRipImportNetRowStatus.setStatus("mandatory")
_MscVrIpRipImportNetComponentName_Type = DisplayString
_MscVrIpRipImportNetComponentName_Object = MibTableColumn
mscVrIpRipImportNetComponentName = _MscVrIpRipImportNetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 2, 2, 1, 1, 2),
    _MscVrIpRipImportNetComponentName_Type()
)
mscVrIpRipImportNetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRipImportNetComponentName.setStatus("mandatory")
_MscVrIpRipImportNetStorageType_Type = StorageType
_MscVrIpRipImportNetStorageType_Object = MibTableColumn
mscVrIpRipImportNetStorageType = _MscVrIpRipImportNetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 2, 2, 1, 1, 4),
    _MscVrIpRipImportNetStorageType_Type()
)
mscVrIpRipImportNetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRipImportNetStorageType.setStatus("mandatory")


class _MscVrIpRipImportNetIndex_Type(Integer32):
    """Custom type mscVrIpRipImportNetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpRipImportNetIndex_Type.__name__ = "Integer32"
_MscVrIpRipImportNetIndex_Object = MibTableColumn
mscVrIpRipImportNetIndex = _MscVrIpRipImportNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 2, 2, 1, 1, 10),
    _MscVrIpRipImportNetIndex_Type()
)
mscVrIpRipImportNetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpRipImportNetIndex.setStatus("mandatory")
_MscVrIpRipImportNetProvTable_Object = MibTable
mscVrIpRipImportNetProvTable = _MscVrIpRipImportNetProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpRipImportNetProvTable.setStatus("mandatory")
_MscVrIpRipImportNetProvEntry_Object = MibTableRow
mscVrIpRipImportNetProvEntry = _MscVrIpRipImportNetProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 2, 2, 10, 1)
)
mscVrIpRipImportNetProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRipIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRipImportIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRipImportNetIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpRipImportNetProvEntry.setStatus("mandatory")
_MscVrIpRipImportNetIpAddress_Type = IpAddress
_MscVrIpRipImportNetIpAddress_Object = MibTableColumn
mscVrIpRipImportNetIpAddress = _MscVrIpRipImportNetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 2, 2, 10, 1, 1),
    _MscVrIpRipImportNetIpAddress_Type()
)
mscVrIpRipImportNetIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRipImportNetIpAddress.setStatus("mandatory")
_MscVrIpRipImportNetIpMask_Type = IpAddress
_MscVrIpRipImportNetIpMask_Object = MibTableColumn
mscVrIpRipImportNetIpMask = _MscVrIpRipImportNetIpMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 2, 2, 10, 1, 2),
    _MscVrIpRipImportNetIpMask_Type()
)
mscVrIpRipImportNetIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRipImportNetIpMask.setStatus("mandatory")
_MscVrIpRipImportProvTable_Object = MibTable
mscVrIpRipImportProvTable = _MscVrIpRipImportProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpRipImportProvTable.setStatus("mandatory")
_MscVrIpRipImportProvEntry_Object = MibTableRow
mscVrIpRipImportProvEntry = _MscVrIpRipImportProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 2, 10, 1)
)
mscVrIpRipImportProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRipIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRipImportIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpRipImportProvEntry.setStatus("mandatory")


class _MscVrIpRipImportUsageFlag_Type(Integer32):
    """Custom type mscVrIpRipImportUsageFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 2),
          ("use", 1))
    )


_MscVrIpRipImportUsageFlag_Type.__name__ = "Integer32"
_MscVrIpRipImportUsageFlag_Object = MibTableColumn
mscVrIpRipImportUsageFlag = _MscVrIpRipImportUsageFlag_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 2, 10, 1, 1),
    _MscVrIpRipImportUsageFlag_Type()
)
mscVrIpRipImportUsageFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRipImportUsageFlag.setStatus("mandatory")


class _MscVrIpRipImportImportMetric_Type(Unsigned32):
    """Custom type mscVrIpRipImportImportMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MscVrIpRipImportImportMetric_Type.__name__ = "Unsigned32"
_MscVrIpRipImportImportMetric_Object = MibTableColumn
mscVrIpRipImportImportMetric = _MscVrIpRipImportImportMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 2, 10, 1, 2),
    _MscVrIpRipImportImportMetric_Type()
)
mscVrIpRipImportImportMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRipImportImportMetric.setStatus("mandatory")


class _MscVrIpRipImportNeighbor_Type(IpAddress):
    """Custom type mscVrIpRipImportNeighbor based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrIpRipImportNeighbor_Object = MibTableColumn
mscVrIpRipImportNeighbor = _MscVrIpRipImportNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 2, 10, 1, 3),
    _MscVrIpRipImportNeighbor_Type()
)
mscVrIpRipImportNeighbor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRipImportNeighbor.setStatus("mandatory")


class _MscVrIpRipImportInterface_Type(IpAddress):
    """Custom type mscVrIpRipImportInterface based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrIpRipImportInterface_Object = MibTableColumn
mscVrIpRipImportInterface = _MscVrIpRipImportInterface_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 2, 10, 1, 4),
    _MscVrIpRipImportInterface_Type()
)
mscVrIpRipImportInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRipImportInterface.setStatus("mandatory")
_MscVrIpRipExport_ObjectIdentity = ObjectIdentity
mscVrIpRipExport = _MscVrIpRipExport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3)
)
_MscVrIpRipExportRowStatusTable_Object = MibTable
mscVrIpRipExportRowStatusTable = _MscVrIpRipExportRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 1)
)
if mibBuilder.loadTexts:
    mscVrIpRipExportRowStatusTable.setStatus("mandatory")
_MscVrIpRipExportRowStatusEntry_Object = MibTableRow
mscVrIpRipExportRowStatusEntry = _MscVrIpRipExportRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 1, 1)
)
mscVrIpRipExportRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRipIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRipExportIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpRipExportRowStatusEntry.setStatus("mandatory")
_MscVrIpRipExportRowStatus_Type = RowStatus
_MscVrIpRipExportRowStatus_Object = MibTableColumn
mscVrIpRipExportRowStatus = _MscVrIpRipExportRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 1, 1, 1),
    _MscVrIpRipExportRowStatus_Type()
)
mscVrIpRipExportRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRipExportRowStatus.setStatus("mandatory")
_MscVrIpRipExportComponentName_Type = DisplayString
_MscVrIpRipExportComponentName_Object = MibTableColumn
mscVrIpRipExportComponentName = _MscVrIpRipExportComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 1, 1, 2),
    _MscVrIpRipExportComponentName_Type()
)
mscVrIpRipExportComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRipExportComponentName.setStatus("mandatory")
_MscVrIpRipExportStorageType_Type = StorageType
_MscVrIpRipExportStorageType_Object = MibTableColumn
mscVrIpRipExportStorageType = _MscVrIpRipExportStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 1, 1, 4),
    _MscVrIpRipExportStorageType_Type()
)
mscVrIpRipExportStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRipExportStorageType.setStatus("mandatory")


class _MscVrIpRipExportIndex_Type(Integer32):
    """Custom type mscVrIpRipExportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpRipExportIndex_Type.__name__ = "Integer32"
_MscVrIpRipExportIndex_Object = MibTableColumn
mscVrIpRipExportIndex = _MscVrIpRipExportIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 1, 1, 10),
    _MscVrIpRipExportIndex_Type()
)
mscVrIpRipExportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpRipExportIndex.setStatus("mandatory")
_MscVrIpRipExportNet_ObjectIdentity = ObjectIdentity
mscVrIpRipExportNet = _MscVrIpRipExportNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 2)
)
_MscVrIpRipExportNetRowStatusTable_Object = MibTable
mscVrIpRipExportNetRowStatusTable = _MscVrIpRipExportNetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpRipExportNetRowStatusTable.setStatus("mandatory")
_MscVrIpRipExportNetRowStatusEntry_Object = MibTableRow
mscVrIpRipExportNetRowStatusEntry = _MscVrIpRipExportNetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 2, 1, 1)
)
mscVrIpRipExportNetRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRipIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRipExportIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRipExportNetIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpRipExportNetRowStatusEntry.setStatus("mandatory")
_MscVrIpRipExportNetRowStatus_Type = RowStatus
_MscVrIpRipExportNetRowStatus_Object = MibTableColumn
mscVrIpRipExportNetRowStatus = _MscVrIpRipExportNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 2, 1, 1, 1),
    _MscVrIpRipExportNetRowStatus_Type()
)
mscVrIpRipExportNetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRipExportNetRowStatus.setStatus("mandatory")
_MscVrIpRipExportNetComponentName_Type = DisplayString
_MscVrIpRipExportNetComponentName_Object = MibTableColumn
mscVrIpRipExportNetComponentName = _MscVrIpRipExportNetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 2, 1, 1, 2),
    _MscVrIpRipExportNetComponentName_Type()
)
mscVrIpRipExportNetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRipExportNetComponentName.setStatus("mandatory")
_MscVrIpRipExportNetStorageType_Type = StorageType
_MscVrIpRipExportNetStorageType_Object = MibTableColumn
mscVrIpRipExportNetStorageType = _MscVrIpRipExportNetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 2, 1, 1, 4),
    _MscVrIpRipExportNetStorageType_Type()
)
mscVrIpRipExportNetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRipExportNetStorageType.setStatus("mandatory")


class _MscVrIpRipExportNetIndex_Type(Integer32):
    """Custom type mscVrIpRipExportNetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpRipExportNetIndex_Type.__name__ = "Integer32"
_MscVrIpRipExportNetIndex_Object = MibTableColumn
mscVrIpRipExportNetIndex = _MscVrIpRipExportNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 2, 1, 1, 10),
    _MscVrIpRipExportNetIndex_Type()
)
mscVrIpRipExportNetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpRipExportNetIndex.setStatus("mandatory")
_MscVrIpRipExportNetProvTable_Object = MibTable
mscVrIpRipExportNetProvTable = _MscVrIpRipExportNetProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpRipExportNetProvTable.setStatus("mandatory")
_MscVrIpRipExportNetProvEntry_Object = MibTableRow
mscVrIpRipExportNetProvEntry = _MscVrIpRipExportNetProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 2, 10, 1)
)
mscVrIpRipExportNetProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRipIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRipExportIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRipExportNetIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpRipExportNetProvEntry.setStatus("mandatory")
_MscVrIpRipExportNetIpAddress_Type = IpAddress
_MscVrIpRipExportNetIpAddress_Object = MibTableColumn
mscVrIpRipExportNetIpAddress = _MscVrIpRipExportNetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 2, 10, 1, 1),
    _MscVrIpRipExportNetIpAddress_Type()
)
mscVrIpRipExportNetIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRipExportNetIpAddress.setStatus("mandatory")
_MscVrIpRipExportNetIpMask_Type = IpAddress
_MscVrIpRipExportNetIpMask_Object = MibTableColumn
mscVrIpRipExportNetIpMask = _MscVrIpRipExportNetIpMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 2, 10, 1, 2),
    _MscVrIpRipExportNetIpMask_Type()
)
mscVrIpRipExportNetIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRipExportNetIpMask.setStatus("mandatory")
_MscVrIpRipExportProvTable_Object = MibTable
mscVrIpRipExportProvTable = _MscVrIpRipExportProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 10)
)
if mibBuilder.loadTexts:
    mscVrIpRipExportProvTable.setStatus("mandatory")
_MscVrIpRipExportProvEntry_Object = MibTableRow
mscVrIpRipExportProvEntry = _MscVrIpRipExportProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 10, 1)
)
mscVrIpRipExportProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRipIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRipExportIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpRipExportProvEntry.setStatus("mandatory")


class _MscVrIpRipExportAdvertiseStatus_Type(Integer32):
    """Custom type mscVrIpRipExportAdvertiseStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("send", 1))
    )


_MscVrIpRipExportAdvertiseStatus_Type.__name__ = "Integer32"
_MscVrIpRipExportAdvertiseStatus_Object = MibTableColumn
mscVrIpRipExportAdvertiseStatus = _MscVrIpRipExportAdvertiseStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 10, 1, 1),
    _MscVrIpRipExportAdvertiseStatus_Type()
)
mscVrIpRipExportAdvertiseStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRipExportAdvertiseStatus.setStatus("mandatory")


class _MscVrIpRipExportExportMetric_Type(Unsigned32):
    """Custom type mscVrIpRipExportExportMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MscVrIpRipExportExportMetric_Type.__name__ = "Unsigned32"
_MscVrIpRipExportExportMetric_Object = MibTableColumn
mscVrIpRipExportExportMetric = _MscVrIpRipExportExportMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 10, 1, 2),
    _MscVrIpRipExportExportMetric_Type()
)
mscVrIpRipExportExportMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRipExportExportMetric.setStatus("mandatory")


class _MscVrIpRipExportProtocol_Type(Integer32):
    """Custom type mscVrIpRipExportProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("bgpExternal", 9),
          ("bgpInternal", 8),
          ("egp", 2),
          ("ospfExternal", 5),
          ("ospfInternal", 4),
          ("rip", 3),
          ("staticLocal", 6),
          ("staticRemote", 7))
    )


_MscVrIpRipExportProtocol_Type.__name__ = "Integer32"
_MscVrIpRipExportProtocol_Object = MibTableColumn
mscVrIpRipExportProtocol = _MscVrIpRipExportProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 10, 1, 3),
    _MscVrIpRipExportProtocol_Type()
)
mscVrIpRipExportProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRipExportProtocol.setStatus("mandatory")


class _MscVrIpRipExportRipInterface_Type(IpAddress):
    """Custom type mscVrIpRipExportRipInterface based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrIpRipExportRipInterface_Object = MibTableColumn
mscVrIpRipExportRipInterface = _MscVrIpRipExportRipInterface_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 10, 1, 4),
    _MscVrIpRipExportRipInterface_Type()
)
mscVrIpRipExportRipInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRipExportRipInterface.setStatus("mandatory")


class _MscVrIpRipExportEgpAsId_Type(Unsigned32):
    """Custom type mscVrIpRipExportEgpAsId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_MscVrIpRipExportEgpAsId_Type.__name__ = "Unsigned32"
_MscVrIpRipExportEgpAsId_Object = MibTableColumn
mscVrIpRipExportEgpAsId = _MscVrIpRipExportEgpAsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 10, 1, 5),
    _MscVrIpRipExportEgpAsId_Type()
)
mscVrIpRipExportEgpAsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRipExportEgpAsId.setStatus("mandatory")


class _MscVrIpRipExportOspfTag_Type(Unsigned32):
    """Custom type mscVrIpRipExportOspfTag based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpRipExportOspfTag_Type.__name__ = "Unsigned32"
_MscVrIpRipExportOspfTag_Object = MibTableColumn
mscVrIpRipExportOspfTag = _MscVrIpRipExportOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 10, 1, 6),
    _MscVrIpRipExportOspfTag_Type()
)
mscVrIpRipExportOspfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRipExportOspfTag.setStatus("mandatory")


class _MscVrIpRipExportOutInterface_Type(IpAddress):
    """Custom type mscVrIpRipExportOutInterface based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrIpRipExportOutInterface_Object = MibTableColumn
mscVrIpRipExportOutInterface = _MscVrIpRipExportOutInterface_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 10, 1, 7),
    _MscVrIpRipExportOutInterface_Type()
)
mscVrIpRipExportOutInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRipExportOutInterface.setStatus("mandatory")


class _MscVrIpRipExportBgpAsId_Type(Unsigned32):
    """Custom type mscVrIpRipExportBgpAsId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpRipExportBgpAsId_Type.__name__ = "Unsigned32"
_MscVrIpRipExportBgpAsId_Object = MibTableColumn
mscVrIpRipExportBgpAsId = _MscVrIpRipExportBgpAsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 3, 10, 1, 8),
    _MscVrIpRipExportBgpAsId_Type()
)
mscVrIpRipExportBgpAsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRipExportBgpAsId.setStatus("mandatory")
_MscVrIpRipProvTable_Object = MibTable
mscVrIpRipProvTable = _MscVrIpRipProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 10)
)
if mibBuilder.loadTexts:
    mscVrIpRipProvTable.setStatus("mandatory")
_MscVrIpRipProvEntry_Object = MibTableRow
mscVrIpRipProvEntry = _MscVrIpRipProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 10, 1)
)
mscVrIpRipProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRipIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpRipProvEntry.setStatus("mandatory")


class _MscVrIpRipMigrateRip_Type(Integer32):
    """Custom type mscVrIpRipMigrateRip based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MscVrIpRipMigrateRip_Type.__name__ = "Integer32"
_MscVrIpRipMigrateRip_Object = MibTableColumn
mscVrIpRipMigrateRip = _MscVrIpRipMigrateRip_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 10, 1, 2),
    _MscVrIpRipMigrateRip_Type()
)
mscVrIpRipMigrateRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRipMigrateRip.setStatus("mandatory")


class _MscVrIpRipRfc1058MetricUsage_Type(Integer32):
    """Custom type mscVrIpRipRfc1058MetricUsage based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MscVrIpRipRfc1058MetricUsage_Type.__name__ = "Integer32"
_MscVrIpRipRfc1058MetricUsage_Object = MibTableColumn
mscVrIpRipRfc1058MetricUsage = _MscVrIpRipRfc1058MetricUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 10, 1, 3),
    _MscVrIpRipRfc1058MetricUsage_Type()
)
mscVrIpRipRfc1058MetricUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRipRfc1058MetricUsage.setStatus("mandatory")


class _MscVrIpRipGenerateDiscardRoute_Type(Integer32):
    """Custom type mscVrIpRipGenerateDiscardRoute based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MscVrIpRipGenerateDiscardRoute_Type.__name__ = "Integer32"
_MscVrIpRipGenerateDiscardRoute_Object = MibTableColumn
mscVrIpRipGenerateDiscardRoute = _MscVrIpRipGenerateDiscardRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 10, 1, 4),
    _MscVrIpRipGenerateDiscardRoute_Type()
)
mscVrIpRipGenerateDiscardRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRipGenerateDiscardRoute.setStatus("mandatory")


class _MscVrIpRipRedistributeIbgp_Type(Integer32):
    """Custom type mscVrIpRipRedistributeIbgp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_MscVrIpRipRedistributeIbgp_Type.__name__ = "Integer32"
_MscVrIpRipRedistributeIbgp_Object = MibTableColumn
mscVrIpRipRedistributeIbgp = _MscVrIpRipRedistributeIbgp_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 10, 1, 5),
    _MscVrIpRipRedistributeIbgp_Type()
)
mscVrIpRipRedistributeIbgp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRipRedistributeIbgp.setStatus("mandatory")
_MscVrIpRipStateTable_Object = MibTable
mscVrIpRipStateTable = _MscVrIpRipStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 11)
)
if mibBuilder.loadTexts:
    mscVrIpRipStateTable.setStatus("mandatory")
_MscVrIpRipStateEntry_Object = MibTableRow
mscVrIpRipStateEntry = _MscVrIpRipStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 11, 1)
)
mscVrIpRipStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRipIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpRipStateEntry.setStatus("mandatory")


class _MscVrIpRipAdminState_Type(Integer32):
    """Custom type mscVrIpRipAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_MscVrIpRipAdminState_Type.__name__ = "Integer32"
_MscVrIpRipAdminState_Object = MibTableColumn
mscVrIpRipAdminState = _MscVrIpRipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 11, 1, 1),
    _MscVrIpRipAdminState_Type()
)
mscVrIpRipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRipAdminState.setStatus("mandatory")


class _MscVrIpRipOperationalState_Type(Integer32):
    """Custom type mscVrIpRipOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MscVrIpRipOperationalState_Type.__name__ = "Integer32"
_MscVrIpRipOperationalState_Object = MibTableColumn
mscVrIpRipOperationalState = _MscVrIpRipOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 11, 1, 2),
    _MscVrIpRipOperationalState_Type()
)
mscVrIpRipOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRipOperationalState.setStatus("mandatory")


class _MscVrIpRipUsageState_Type(Integer32):
    """Custom type mscVrIpRipUsageState based on Integer32"""
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
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_MscVrIpRipUsageState_Type.__name__ = "Integer32"
_MscVrIpRipUsageState_Object = MibTableColumn
mscVrIpRipUsageState = _MscVrIpRipUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 11, 1, 3),
    _MscVrIpRipUsageState_Type()
)
mscVrIpRipUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRipUsageState.setStatus("mandatory")
_MscVrIpRipAdminControlTable_Object = MibTable
mscVrIpRipAdminControlTable = _MscVrIpRipAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 12)
)
if mibBuilder.loadTexts:
    mscVrIpRipAdminControlTable.setStatus("mandatory")
_MscVrIpRipAdminControlEntry_Object = MibTableRow
mscVrIpRipAdminControlEntry = _MscVrIpRipAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 12, 1)
)
mscVrIpRipAdminControlEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRipIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpRipAdminControlEntry.setStatus("mandatory")


class _MscVrIpRipSnmpAdminStatus_Type(Integer32):
    """Custom type mscVrIpRipSnmpAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscVrIpRipSnmpAdminStatus_Type.__name__ = "Integer32"
_MscVrIpRipSnmpAdminStatus_Object = MibTableColumn
mscVrIpRipSnmpAdminStatus = _MscVrIpRipSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 12, 1, 1),
    _MscVrIpRipSnmpAdminStatus_Type()
)
mscVrIpRipSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRipSnmpAdminStatus.setStatus("mandatory")
_MscVrIpRipOperStatusTable_Object = MibTable
mscVrIpRipOperStatusTable = _MscVrIpRipOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 15)
)
if mibBuilder.loadTexts:
    mscVrIpRipOperStatusTable.setStatus("mandatory")
_MscVrIpRipOperStatusEntry_Object = MibTableRow
mscVrIpRipOperStatusEntry = _MscVrIpRipOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 15, 1)
)
mscVrIpRipOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRipIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpRipOperStatusEntry.setStatus("mandatory")


class _MscVrIpRipSnmpOperStatus_Type(Integer32):
    """Custom type mscVrIpRipSnmpOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscVrIpRipSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrIpRipSnmpOperStatus_Object = MibTableColumn
mscVrIpRipSnmpOperStatus = _MscVrIpRipSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 15, 1, 1),
    _MscVrIpRipSnmpOperStatus_Type()
)
mscVrIpRipSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRipSnmpOperStatus.setStatus("mandatory")
_MscVrIpRipOperTable_Object = MibTable
mscVrIpRipOperTable = _MscVrIpRipOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 16)
)
if mibBuilder.loadTexts:
    mscVrIpRipOperTable.setStatus("mandatory")
_MscVrIpRipOperEntry_Object = MibTableRow
mscVrIpRipOperEntry = _MscVrIpRipOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 16, 1)
)
mscVrIpRipOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRipIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpRipOperEntry.setStatus("mandatory")
_MscVrIpRipRouteChangesMade_Type = Counter32
_MscVrIpRipRouteChangesMade_Object = MibTableColumn
mscVrIpRipRouteChangesMade = _MscVrIpRipRouteChangesMade_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 16, 1, 1),
    _MscVrIpRipRouteChangesMade_Type()
)
mscVrIpRipRouteChangesMade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRipRouteChangesMade.setStatus("mandatory")
_MscVrIpRipQueryResponses_Type = Counter32
_MscVrIpRipQueryResponses_Object = MibTableColumn
mscVrIpRipQueryResponses = _MscVrIpRipQueryResponses_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 8, 16, 1, 2),
    _MscVrIpRipQueryResponses_Type()
)
mscVrIpRipQueryResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRipQueryResponses.setStatus("mandatory")
_MscVrIpStatic_ObjectIdentity = ObjectIdentity
mscVrIpStatic = _MscVrIpStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9)
)
_MscVrIpStaticRowStatusTable_Object = MibTable
mscVrIpStaticRowStatusTable = _MscVrIpStaticRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 1)
)
if mibBuilder.loadTexts:
    mscVrIpStaticRowStatusTable.setStatus("mandatory")
_MscVrIpStaticRowStatusEntry_Object = MibTableRow
mscVrIpStaticRowStatusEntry = _MscVrIpStaticRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 1, 1)
)
mscVrIpStaticRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpStaticIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpStaticRowStatusEntry.setStatus("mandatory")
_MscVrIpStaticRowStatus_Type = RowStatus
_MscVrIpStaticRowStatus_Object = MibTableColumn
mscVrIpStaticRowStatus = _MscVrIpStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 1, 1, 1),
    _MscVrIpStaticRowStatus_Type()
)
mscVrIpStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpStaticRowStatus.setStatus("mandatory")
_MscVrIpStaticComponentName_Type = DisplayString
_MscVrIpStaticComponentName_Object = MibTableColumn
mscVrIpStaticComponentName = _MscVrIpStaticComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 1, 1, 2),
    _MscVrIpStaticComponentName_Type()
)
mscVrIpStaticComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpStaticComponentName.setStatus("mandatory")
_MscVrIpStaticStorageType_Type = StorageType
_MscVrIpStaticStorageType_Object = MibTableColumn
mscVrIpStaticStorageType = _MscVrIpStaticStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 1, 1, 4),
    _MscVrIpStaticStorageType_Type()
)
mscVrIpStaticStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpStaticStorageType.setStatus("mandatory")
_MscVrIpStaticIndex_Type = NonReplicated
_MscVrIpStaticIndex_Object = MibTableColumn
mscVrIpStaticIndex = _MscVrIpStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 1, 1, 10),
    _MscVrIpStaticIndex_Type()
)
mscVrIpStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpStaticIndex.setStatus("mandatory")
_MscVrIpStaticRoute_ObjectIdentity = ObjectIdentity
mscVrIpStaticRoute = _MscVrIpStaticRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 2)
)
_MscVrIpStaticRouteRowStatusTable_Object = MibTable
mscVrIpStaticRouteRowStatusTable = _MscVrIpStaticRouteRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpStaticRouteRowStatusTable.setStatus("mandatory")
_MscVrIpStaticRouteRowStatusEntry_Object = MibTableRow
mscVrIpStaticRouteRowStatusEntry = _MscVrIpStaticRouteRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 2, 1, 1)
)
mscVrIpStaticRouteRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpStaticIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpStaticRouteDestAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpStaticRouteDestMaskIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpStaticRouteTypeOfServiceIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpStaticRouteRowStatusEntry.setStatus("mandatory")
_MscVrIpStaticRouteRowStatus_Type = RowStatus
_MscVrIpStaticRouteRowStatus_Object = MibTableColumn
mscVrIpStaticRouteRowStatus = _MscVrIpStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 2, 1, 1, 1),
    _MscVrIpStaticRouteRowStatus_Type()
)
mscVrIpStaticRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpStaticRouteRowStatus.setStatus("mandatory")
_MscVrIpStaticRouteComponentName_Type = DisplayString
_MscVrIpStaticRouteComponentName_Object = MibTableColumn
mscVrIpStaticRouteComponentName = _MscVrIpStaticRouteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 2, 1, 1, 2),
    _MscVrIpStaticRouteComponentName_Type()
)
mscVrIpStaticRouteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpStaticRouteComponentName.setStatus("mandatory")
_MscVrIpStaticRouteStorageType_Type = StorageType
_MscVrIpStaticRouteStorageType_Object = MibTableColumn
mscVrIpStaticRouteStorageType = _MscVrIpStaticRouteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 2, 1, 1, 4),
    _MscVrIpStaticRouteStorageType_Type()
)
mscVrIpStaticRouteStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpStaticRouteStorageType.setStatus("mandatory")
_MscVrIpStaticRouteDestAddressIndex_Type = IpAddress
_MscVrIpStaticRouteDestAddressIndex_Object = MibTableColumn
mscVrIpStaticRouteDestAddressIndex = _MscVrIpStaticRouteDestAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 2, 1, 1, 10),
    _MscVrIpStaticRouteDestAddressIndex_Type()
)
mscVrIpStaticRouteDestAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpStaticRouteDestAddressIndex.setStatus("mandatory")
_MscVrIpStaticRouteDestMaskIndex_Type = IpAddress
_MscVrIpStaticRouteDestMaskIndex_Object = MibTableColumn
mscVrIpStaticRouteDestMaskIndex = _MscVrIpStaticRouteDestMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 2, 1, 1, 11),
    _MscVrIpStaticRouteDestMaskIndex_Type()
)
mscVrIpStaticRouteDestMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpStaticRouteDestMaskIndex.setStatus("mandatory")


class _MscVrIpStaticRouteTypeOfServiceIndex_Type(Integer32):
    """Custom type mscVrIpStaticRouteTypeOfServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_MscVrIpStaticRouteTypeOfServiceIndex_Type.__name__ = "Integer32"
_MscVrIpStaticRouteTypeOfServiceIndex_Object = MibTableColumn
mscVrIpStaticRouteTypeOfServiceIndex = _MscVrIpStaticRouteTypeOfServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 2, 1, 1, 12),
    _MscVrIpStaticRouteTypeOfServiceIndex_Type()
)
mscVrIpStaticRouteTypeOfServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpStaticRouteTypeOfServiceIndex.setStatus("mandatory")
_MscVrIpStaticRouteNh_ObjectIdentity = ObjectIdentity
mscVrIpStaticRouteNh = _MscVrIpStaticRouteNh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 2, 2)
)
_MscVrIpStaticRouteNhRowStatusTable_Object = MibTable
mscVrIpStaticRouteNhRowStatusTable = _MscVrIpStaticRouteNhRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpStaticRouteNhRowStatusTable.setStatus("mandatory")
_MscVrIpStaticRouteNhRowStatusEntry_Object = MibTableRow
mscVrIpStaticRouteNhRowStatusEntry = _MscVrIpStaticRouteNhRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 2, 2, 1, 1)
)
mscVrIpStaticRouteNhRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpStaticIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpStaticRouteDestAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpStaticRouteDestMaskIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpStaticRouteTypeOfServiceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpStaticRouteNhIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpStaticRouteNhRowStatusEntry.setStatus("mandatory")
_MscVrIpStaticRouteNhRowStatus_Type = RowStatus
_MscVrIpStaticRouteNhRowStatus_Object = MibTableColumn
mscVrIpStaticRouteNhRowStatus = _MscVrIpStaticRouteNhRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 2, 2, 1, 1, 1),
    _MscVrIpStaticRouteNhRowStatus_Type()
)
mscVrIpStaticRouteNhRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpStaticRouteNhRowStatus.setStatus("mandatory")
_MscVrIpStaticRouteNhComponentName_Type = DisplayString
_MscVrIpStaticRouteNhComponentName_Object = MibTableColumn
mscVrIpStaticRouteNhComponentName = _MscVrIpStaticRouteNhComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 2, 2, 1, 1, 2),
    _MscVrIpStaticRouteNhComponentName_Type()
)
mscVrIpStaticRouteNhComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpStaticRouteNhComponentName.setStatus("mandatory")
_MscVrIpStaticRouteNhStorageType_Type = StorageType
_MscVrIpStaticRouteNhStorageType_Object = MibTableColumn
mscVrIpStaticRouteNhStorageType = _MscVrIpStaticRouteNhStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 2, 2, 1, 1, 4),
    _MscVrIpStaticRouteNhStorageType_Type()
)
mscVrIpStaticRouteNhStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpStaticRouteNhStorageType.setStatus("mandatory")
_MscVrIpStaticRouteNhIndex_Type = IpAddress
_MscVrIpStaticRouteNhIndex_Object = MibTableColumn
mscVrIpStaticRouteNhIndex = _MscVrIpStaticRouteNhIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 2, 2, 1, 1, 10),
    _MscVrIpStaticRouteNhIndex_Type()
)
mscVrIpStaticRouteNhIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpStaticRouteNhIndex.setStatus("mandatory")
_MscVrIpStaticRouteNhProvTable_Object = MibTable
mscVrIpStaticRouteNhProvTable = _MscVrIpStaticRouteNhProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpStaticRouteNhProvTable.setStatus("mandatory")
_MscVrIpStaticRouteNhProvEntry_Object = MibTableRow
mscVrIpStaticRouteNhProvEntry = _MscVrIpStaticRouteNhProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 2, 2, 10, 1)
)
mscVrIpStaticRouteNhProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpStaticIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpStaticRouteDestAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpStaticRouteDestMaskIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpStaticRouteTypeOfServiceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpStaticRouteNhIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpStaticRouteNhProvEntry.setStatus("mandatory")


class _MscVrIpStaticRouteNhMetric_Type(Integer32):
    """Custom type mscVrIpStaticRouteNhMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MscVrIpStaticRouteNhMetric_Type.__name__ = "Integer32"
_MscVrIpStaticRouteNhMetric_Object = MibTableColumn
mscVrIpStaticRouteNhMetric = _MscVrIpStaticRouteNhMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 2, 2, 10, 1, 1),
    _MscVrIpStaticRouteNhMetric_Type()
)
mscVrIpStaticRouteNhMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpStaticRouteNhMetric.setStatus("mandatory")
_MscVrIpStaticRouteProvTable_Object = MibTable
mscVrIpStaticRouteProvTable = _MscVrIpStaticRouteProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpStaticRouteProvTable.setStatus("mandatory")
_MscVrIpStaticRouteProvEntry_Object = MibTableRow
mscVrIpStaticRouteProvEntry = _MscVrIpStaticRouteProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 2, 10, 1)
)
mscVrIpStaticRouteProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpStaticIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpStaticRouteDestAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpStaticRouteDestMaskIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpStaticRouteTypeOfServiceIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpStaticRouteProvEntry.setStatus("mandatory")


class _MscVrIpStaticRoutePreferredOver_Type(Integer32):
    """Custom type mscVrIpStaticRoutePreferredOver based on Integer32"""
    defaultValue = 72

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              72)
        )
    )
    namedValues = NamedValues(
        *(("extOspf", 72),
          ("intOspf", 5))
    )


_MscVrIpStaticRoutePreferredOver_Type.__name__ = "Integer32"
_MscVrIpStaticRoutePreferredOver_Object = MibTableColumn
mscVrIpStaticRoutePreferredOver = _MscVrIpStaticRoutePreferredOver_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 2, 10, 1, 12),
    _MscVrIpStaticRoutePreferredOver_Type()
)
mscVrIpStaticRoutePreferredOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpStaticRoutePreferredOver.setStatus("mandatory")
_MscVrIpStaticDiscard_ObjectIdentity = ObjectIdentity
mscVrIpStaticDiscard = _MscVrIpStaticDiscard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 3)
)
_MscVrIpStaticDiscardRowStatusTable_Object = MibTable
mscVrIpStaticDiscardRowStatusTable = _MscVrIpStaticDiscardRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 3, 1)
)
if mibBuilder.loadTexts:
    mscVrIpStaticDiscardRowStatusTable.setStatus("mandatory")
_MscVrIpStaticDiscardRowStatusEntry_Object = MibTableRow
mscVrIpStaticDiscardRowStatusEntry = _MscVrIpStaticDiscardRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 3, 1, 1)
)
mscVrIpStaticDiscardRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpStaticIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpStaticDiscardDestAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpStaticDiscardDestMaskIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpStaticDiscardRowStatusEntry.setStatus("mandatory")
_MscVrIpStaticDiscardRowStatus_Type = RowStatus
_MscVrIpStaticDiscardRowStatus_Object = MibTableColumn
mscVrIpStaticDiscardRowStatus = _MscVrIpStaticDiscardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 3, 1, 1, 1),
    _MscVrIpStaticDiscardRowStatus_Type()
)
mscVrIpStaticDiscardRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpStaticDiscardRowStatus.setStatus("mandatory")
_MscVrIpStaticDiscardComponentName_Type = DisplayString
_MscVrIpStaticDiscardComponentName_Object = MibTableColumn
mscVrIpStaticDiscardComponentName = _MscVrIpStaticDiscardComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 3, 1, 1, 2),
    _MscVrIpStaticDiscardComponentName_Type()
)
mscVrIpStaticDiscardComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpStaticDiscardComponentName.setStatus("mandatory")
_MscVrIpStaticDiscardStorageType_Type = StorageType
_MscVrIpStaticDiscardStorageType_Object = MibTableColumn
mscVrIpStaticDiscardStorageType = _MscVrIpStaticDiscardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 3, 1, 1, 4),
    _MscVrIpStaticDiscardStorageType_Type()
)
mscVrIpStaticDiscardStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpStaticDiscardStorageType.setStatus("mandatory")
_MscVrIpStaticDiscardDestAddressIndex_Type = IpAddress
_MscVrIpStaticDiscardDestAddressIndex_Object = MibTableColumn
mscVrIpStaticDiscardDestAddressIndex = _MscVrIpStaticDiscardDestAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 3, 1, 1, 10),
    _MscVrIpStaticDiscardDestAddressIndex_Type()
)
mscVrIpStaticDiscardDestAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpStaticDiscardDestAddressIndex.setStatus("mandatory")
_MscVrIpStaticDiscardDestMaskIndex_Type = IpAddress
_MscVrIpStaticDiscardDestMaskIndex_Object = MibTableColumn
mscVrIpStaticDiscardDestMaskIndex = _MscVrIpStaticDiscardDestMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 3, 1, 1, 11),
    _MscVrIpStaticDiscardDestMaskIndex_Type()
)
mscVrIpStaticDiscardDestMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpStaticDiscardDestMaskIndex.setStatus("mandatory")
_MscVrIpStaticStateTable_Object = MibTable
mscVrIpStaticStateTable = _MscVrIpStaticStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 10)
)
if mibBuilder.loadTexts:
    mscVrIpStaticStateTable.setStatus("mandatory")
_MscVrIpStaticStateEntry_Object = MibTableRow
mscVrIpStaticStateEntry = _MscVrIpStaticStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 10, 1)
)
mscVrIpStaticStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpStaticIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpStaticStateEntry.setStatus("mandatory")


class _MscVrIpStaticAdminState_Type(Integer32):
    """Custom type mscVrIpStaticAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_MscVrIpStaticAdminState_Type.__name__ = "Integer32"
_MscVrIpStaticAdminState_Object = MibTableColumn
mscVrIpStaticAdminState = _MscVrIpStaticAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 10, 1, 1),
    _MscVrIpStaticAdminState_Type()
)
mscVrIpStaticAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpStaticAdminState.setStatus("mandatory")


class _MscVrIpStaticOperationalState_Type(Integer32):
    """Custom type mscVrIpStaticOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MscVrIpStaticOperationalState_Type.__name__ = "Integer32"
_MscVrIpStaticOperationalState_Object = MibTableColumn
mscVrIpStaticOperationalState = _MscVrIpStaticOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 10, 1, 2),
    _MscVrIpStaticOperationalState_Type()
)
mscVrIpStaticOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpStaticOperationalState.setStatus("mandatory")


class _MscVrIpStaticUsageState_Type(Integer32):
    """Custom type mscVrIpStaticUsageState based on Integer32"""
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
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_MscVrIpStaticUsageState_Type.__name__ = "Integer32"
_MscVrIpStaticUsageState_Object = MibTableColumn
mscVrIpStaticUsageState = _MscVrIpStaticUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 9, 10, 1, 3),
    _MscVrIpStaticUsageState_Type()
)
mscVrIpStaticUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpStaticUsageState.setStatus("mandatory")
_MscVrIpNs_ObjectIdentity = ObjectIdentity
mscVrIpNs = _MscVrIpNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10)
)
_MscVrIpNsRowStatusTable_Object = MibTable
mscVrIpNsRowStatusTable = _MscVrIpNsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 1)
)
if mibBuilder.loadTexts:
    mscVrIpNsRowStatusTable.setStatus("mandatory")
_MscVrIpNsRowStatusEntry_Object = MibTableRow
mscVrIpNsRowStatusEntry = _MscVrIpNsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 1, 1)
)
mscVrIpNsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpNsIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpNsRowStatusEntry.setStatus("mandatory")
_MscVrIpNsRowStatus_Type = RowStatus
_MscVrIpNsRowStatus_Object = MibTableColumn
mscVrIpNsRowStatus = _MscVrIpNsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 1, 1, 1),
    _MscVrIpNsRowStatus_Type()
)
mscVrIpNsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNsRowStatus.setStatus("mandatory")
_MscVrIpNsComponentName_Type = DisplayString
_MscVrIpNsComponentName_Object = MibTableColumn
mscVrIpNsComponentName = _MscVrIpNsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 1, 1, 2),
    _MscVrIpNsComponentName_Type()
)
mscVrIpNsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNsComponentName.setStatus("mandatory")
_MscVrIpNsStorageType_Type = StorageType
_MscVrIpNsStorageType_Object = MibTableColumn
mscVrIpNsStorageType = _MscVrIpNsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 1, 1, 4),
    _MscVrIpNsStorageType_Type()
)
mscVrIpNsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNsStorageType.setStatus("mandatory")
_MscVrIpNsIndex_Type = NonReplicated
_MscVrIpNsIndex_Object = MibTableColumn
mscVrIpNsIndex = _MscVrIpNsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 1, 1, 10),
    _MscVrIpNsIndex_Type()
)
mscVrIpNsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpNsIndex.setStatus("mandatory")
_MscVrIpNsApply_ObjectIdentity = ObjectIdentity
mscVrIpNsApply = _MscVrIpNsApply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 2)
)
_MscVrIpNsApplyRowStatusTable_Object = MibTable
mscVrIpNsApplyRowStatusTable = _MscVrIpNsApplyRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpNsApplyRowStatusTable.setStatus("mandatory")
_MscVrIpNsApplyRowStatusEntry_Object = MibTableRow
mscVrIpNsApplyRowStatusEntry = _MscVrIpNsApplyRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 2, 1, 1)
)
mscVrIpNsApplyRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpNsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpNsApplyIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpNsApplyRowStatusEntry.setStatus("mandatory")
_MscVrIpNsApplyRowStatus_Type = RowStatus
_MscVrIpNsApplyRowStatus_Object = MibTableColumn
mscVrIpNsApplyRowStatus = _MscVrIpNsApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 2, 1, 1, 1),
    _MscVrIpNsApplyRowStatus_Type()
)
mscVrIpNsApplyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNsApplyRowStatus.setStatus("mandatory")
_MscVrIpNsApplyComponentName_Type = DisplayString
_MscVrIpNsApplyComponentName_Object = MibTableColumn
mscVrIpNsApplyComponentName = _MscVrIpNsApplyComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 2, 1, 1, 2),
    _MscVrIpNsApplyComponentName_Type()
)
mscVrIpNsApplyComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNsApplyComponentName.setStatus("mandatory")
_MscVrIpNsApplyStorageType_Type = StorageType
_MscVrIpNsApplyStorageType_Object = MibTableColumn
mscVrIpNsApplyStorageType = _MscVrIpNsApplyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 2, 1, 1, 4),
    _MscVrIpNsApplyStorageType_Type()
)
mscVrIpNsApplyStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNsApplyStorageType.setStatus("mandatory")


class _MscVrIpNsApplyIndex_Type(Integer32):
    """Custom type mscVrIpNsApplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrIpNsApplyIndex_Type.__name__ = "Integer32"
_MscVrIpNsApplyIndex_Object = MibTableColumn
mscVrIpNsApplyIndex = _MscVrIpNsApplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 2, 1, 1, 10),
    _MscVrIpNsApplyIndex_Type()
)
mscVrIpNsApplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpNsApplyIndex.setStatus("mandatory")
_MscVrIpNsApplyProvisionedTable_Object = MibTable
mscVrIpNsApplyProvisionedTable = _MscVrIpNsApplyProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpNsApplyProvisionedTable.setStatus("mandatory")
_MscVrIpNsApplyProvisionedEntry_Object = MibTableRow
mscVrIpNsApplyProvisionedEntry = _MscVrIpNsApplyProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 2, 10, 1)
)
mscVrIpNsApplyProvisionedEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpNsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpNsApplyIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpNsApplyProvisionedEntry.setStatus("mandatory")


class _MscVrIpNsApplyFilter_Type(AsciiString):
    """Custom type mscVrIpNsApplyFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrIpNsApplyFilter_Type.__name__ = "AsciiString"
_MscVrIpNsApplyFilter_Object = MibTableColumn
mscVrIpNsApplyFilter = _MscVrIpNsApplyFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 2, 10, 1, 1),
    _MscVrIpNsApplyFilter_Type()
)
mscVrIpNsApplyFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNsApplyFilter.setStatus("mandatory")
_MscVrIpNsApplyIpAddress1_Type = IpAddress
_MscVrIpNsApplyIpAddress1_Object = MibTableColumn
mscVrIpNsApplyIpAddress1 = _MscVrIpNsApplyIpAddress1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 2, 10, 1, 2),
    _MscVrIpNsApplyIpAddress1_Type()
)
mscVrIpNsApplyIpAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNsApplyIpAddress1.setStatus("mandatory")
_MscVrIpNsApplyIpMask1_Type = IpAddress
_MscVrIpNsApplyIpMask1_Object = MibTableColumn
mscVrIpNsApplyIpMask1 = _MscVrIpNsApplyIpMask1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 2, 10, 1, 3),
    _MscVrIpNsApplyIpMask1_Type()
)
mscVrIpNsApplyIpMask1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNsApplyIpMask1.setStatus("mandatory")
_MscVrIpNsApplyIpAddress2_Type = IpAddress
_MscVrIpNsApplyIpAddress2_Object = MibTableColumn
mscVrIpNsApplyIpAddress2 = _MscVrIpNsApplyIpAddress2_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 2, 10, 1, 4),
    _MscVrIpNsApplyIpAddress2_Type()
)
mscVrIpNsApplyIpAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNsApplyIpAddress2.setStatus("mandatory")
_MscVrIpNsApplyIpMask2_Type = IpAddress
_MscVrIpNsApplyIpMask2_Object = MibTableColumn
mscVrIpNsApplyIpMask2 = _MscVrIpNsApplyIpMask2_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 2, 10, 1, 5),
    _MscVrIpNsApplyIpMask2_Type()
)
mscVrIpNsApplyIpMask2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNsApplyIpMask2.setStatus("mandatory")


class _MscVrIpNsApplyDirection_Type(Integer32):
    """Custom type mscVrIpNsApplyDirection based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("from", 2),
          ("to", 1),
          ("tofrom", 3))
    )


_MscVrIpNsApplyDirection_Type.__name__ = "Integer32"
_MscVrIpNsApplyDirection_Object = MibTableColumn
mscVrIpNsApplyDirection = _MscVrIpNsApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 2, 10, 1, 6),
    _MscVrIpNsApplyDirection_Type()
)
mscVrIpNsApplyDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNsApplyDirection.setStatus("mandatory")
_MscVrIpNsProvTable_Object = MibTable
mscVrIpNsProvTable = _MscVrIpNsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 10)
)
if mibBuilder.loadTexts:
    mscVrIpNsProvTable.setStatus("mandatory")
_MscVrIpNsProvEntry_Object = MibTableRow
mscVrIpNsProvEntry = _MscVrIpNsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 10, 1)
)
mscVrIpNsProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpNsIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpNsProvEntry.setStatus("mandatory")


class _MscVrIpNsFirstFilter_Type(AsciiString):
    """Custom type mscVrIpNsFirstFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrIpNsFirstFilter_Type.__name__ = "AsciiString"
_MscVrIpNsFirstFilter_Object = MibTableColumn
mscVrIpNsFirstFilter = _MscVrIpNsFirstFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 10, 1, 1),
    _MscVrIpNsFirstFilter_Type()
)
mscVrIpNsFirstFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNsFirstFilter.setStatus("mandatory")


class _MscVrIpNsLocalInFilter_Type(AsciiString):
    """Custom type mscVrIpNsLocalInFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrIpNsLocalInFilter_Type.__name__ = "AsciiString"
_MscVrIpNsLocalInFilter_Object = MibTableColumn
mscVrIpNsLocalInFilter = _MscVrIpNsLocalInFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 10, 1, 2),
    _MscVrIpNsLocalInFilter_Type()
)
mscVrIpNsLocalInFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNsLocalInFilter.setStatus("mandatory")


class _MscVrIpNsLocalOutFilter_Type(AsciiString):
    """Custom type mscVrIpNsLocalOutFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrIpNsLocalOutFilter_Type.__name__ = "AsciiString"
_MscVrIpNsLocalOutFilter_Object = MibTableColumn
mscVrIpNsLocalOutFilter = _MscVrIpNsLocalOutFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 10, 1, 3),
    _MscVrIpNsLocalOutFilter_Type()
)
mscVrIpNsLocalOutFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNsLocalOutFilter.setStatus("mandatory")


class _MscVrIpNsLastFilter_Type(AsciiString):
    """Custom type mscVrIpNsLastFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrIpNsLastFilter_Type.__name__ = "AsciiString"
_MscVrIpNsLastFilter_Object = MibTableColumn
mscVrIpNsLastFilter = _MscVrIpNsLastFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 10, 10, 1, 4),
    _MscVrIpNsLastFilter_Type()
)
mscVrIpNsLastFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNsLastFilter.setStatus("mandatory")
_MscVrIpArp_ObjectIdentity = ObjectIdentity
mscVrIpArp = _MscVrIpArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11)
)
_MscVrIpArpRowStatusTable_Object = MibTable
mscVrIpArpRowStatusTable = _MscVrIpArpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 1)
)
if mibBuilder.loadTexts:
    mscVrIpArpRowStatusTable.setStatus("mandatory")
_MscVrIpArpRowStatusEntry_Object = MibTableRow
mscVrIpArpRowStatusEntry = _MscVrIpArpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 1, 1)
)
mscVrIpArpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpArpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpArpRowStatusEntry.setStatus("mandatory")
_MscVrIpArpRowStatus_Type = RowStatus
_MscVrIpArpRowStatus_Object = MibTableColumn
mscVrIpArpRowStatus = _MscVrIpArpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 1, 1, 1),
    _MscVrIpArpRowStatus_Type()
)
mscVrIpArpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpArpRowStatus.setStatus("mandatory")
_MscVrIpArpComponentName_Type = DisplayString
_MscVrIpArpComponentName_Object = MibTableColumn
mscVrIpArpComponentName = _MscVrIpArpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 1, 1, 2),
    _MscVrIpArpComponentName_Type()
)
mscVrIpArpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpArpComponentName.setStatus("mandatory")
_MscVrIpArpStorageType_Type = StorageType
_MscVrIpArpStorageType_Object = MibTableColumn
mscVrIpArpStorageType = _MscVrIpArpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 1, 1, 4),
    _MscVrIpArpStorageType_Type()
)
mscVrIpArpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpArpStorageType.setStatus("mandatory")
_MscVrIpArpIndex_Type = NonReplicated
_MscVrIpArpIndex_Object = MibTableColumn
mscVrIpArpIndex = _MscVrIpArpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 1, 1, 10),
    _MscVrIpArpIndex_Type()
)
mscVrIpArpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpArpIndex.setStatus("mandatory")
_MscVrIpArpHost_ObjectIdentity = ObjectIdentity
mscVrIpArpHost = _MscVrIpArpHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 2)
)
_MscVrIpArpHostRowStatusTable_Object = MibTable
mscVrIpArpHostRowStatusTable = _MscVrIpArpHostRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpArpHostRowStatusTable.setStatus("mandatory")
_MscVrIpArpHostRowStatusEntry_Object = MibTableRow
mscVrIpArpHostRowStatusEntry = _MscVrIpArpHostRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 2, 1, 1)
)
mscVrIpArpHostRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpArpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpArpHostHostAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpArpHostRowStatusEntry.setStatus("mandatory")
_MscVrIpArpHostRowStatus_Type = RowStatus
_MscVrIpArpHostRowStatus_Object = MibTableColumn
mscVrIpArpHostRowStatus = _MscVrIpArpHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 2, 1, 1, 1),
    _MscVrIpArpHostRowStatus_Type()
)
mscVrIpArpHostRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpArpHostRowStatus.setStatus("mandatory")
_MscVrIpArpHostComponentName_Type = DisplayString
_MscVrIpArpHostComponentName_Object = MibTableColumn
mscVrIpArpHostComponentName = _MscVrIpArpHostComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 2, 1, 1, 2),
    _MscVrIpArpHostComponentName_Type()
)
mscVrIpArpHostComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpArpHostComponentName.setStatus("mandatory")
_MscVrIpArpHostStorageType_Type = StorageType
_MscVrIpArpHostStorageType_Object = MibTableColumn
mscVrIpArpHostStorageType = _MscVrIpArpHostStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 2, 1, 1, 4),
    _MscVrIpArpHostStorageType_Type()
)
mscVrIpArpHostStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpArpHostStorageType.setStatus("mandatory")
_MscVrIpArpHostHostAddressIndex_Type = IpAddress
_MscVrIpArpHostHostAddressIndex_Object = MibTableColumn
mscVrIpArpHostHostAddressIndex = _MscVrIpArpHostHostAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 2, 1, 1, 10),
    _MscVrIpArpHostHostAddressIndex_Type()
)
mscVrIpArpHostHostAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpArpHostHostAddressIndex.setStatus("mandatory")
_MscVrIpArpHostProvTable_Object = MibTable
mscVrIpArpHostProvTable = _MscVrIpArpHostProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpArpHostProvTable.setStatus("mandatory")
_MscVrIpArpHostProvEntry_Object = MibTableRow
mscVrIpArpHostProvEntry = _MscVrIpArpHostProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 2, 10, 1)
)
mscVrIpArpHostProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpArpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpArpHostHostAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpArpHostProvEntry.setStatus("mandatory")


class _MscVrIpArpHostPhysAddress_Type(PhysAddress):
    """Custom type mscVrIpArpHostPhysAddress based on PhysAddress"""
    defaultHexValue = "000000000000"

    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MscVrIpArpHostPhysAddress_Type.__name__ = "PhysAddress"
_MscVrIpArpHostPhysAddress_Object = MibTableColumn
mscVrIpArpHostPhysAddress = _MscVrIpArpHostPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 2, 10, 1, 1),
    _MscVrIpArpHostPhysAddress_Type()
)
mscVrIpArpHostPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpArpHostPhysAddress.setStatus("mandatory")


class _MscVrIpArpHostMaxTxUnit_Type(Unsigned32):
    """Custom type mscVrIpArpHostMaxTxUnit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 18944),
    )


_MscVrIpArpHostMaxTxUnit_Type.__name__ = "Unsigned32"
_MscVrIpArpHostMaxTxUnit_Object = MibTableColumn
mscVrIpArpHostMaxTxUnit = _MscVrIpArpHostMaxTxUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 2, 10, 1, 2),
    _MscVrIpArpHostMaxTxUnit_Type()
)
mscVrIpArpHostMaxTxUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpArpHostMaxTxUnit.setStatus("mandatory")


class _MscVrIpArpHostPermanentVirtualCircuitNumber_Type(Unsigned32):
    """Custom type mscVrIpArpHostPermanentVirtualCircuitNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MscVrIpArpHostPermanentVirtualCircuitNumber_Type.__name__ = "Unsigned32"
_MscVrIpArpHostPermanentVirtualCircuitNumber_Object = MibTableColumn
mscVrIpArpHostPermanentVirtualCircuitNumber = _MscVrIpArpHostPermanentVirtualCircuitNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 2, 10, 1, 3),
    _MscVrIpArpHostPermanentVirtualCircuitNumber_Type()
)
mscVrIpArpHostPermanentVirtualCircuitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpArpHostPermanentVirtualCircuitNumber.setStatus("mandatory")


class _MscVrIpArpHostTunnelDestinationAddress_Type(IpAddress):
    """Custom type mscVrIpArpHostTunnelDestinationAddress based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrIpArpHostTunnelDestinationAddress_Object = MibTableColumn
mscVrIpArpHostTunnelDestinationAddress = _MscVrIpArpHostTunnelDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 2, 10, 1, 4),
    _MscVrIpArpHostTunnelDestinationAddress_Type()
)
mscVrIpArpHostTunnelDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpArpHostTunnelDestinationAddress.setStatus("mandatory")


class _MscVrIpArpHostEncap_Type(Integer32):
    """Custom type mscVrIpArpHostEncap based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("ethernet", 2),
          ("ieee8023", 1))
    )


_MscVrIpArpHostEncap_Type.__name__ = "Integer32"
_MscVrIpArpHostEncap_Object = MibTableColumn
mscVrIpArpHostEncap = _MscVrIpArpHostEncap_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 2, 10, 1, 5),
    _MscVrIpArpHostEncap_Type()
)
mscVrIpArpHostEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpArpHostEncap.setStatus("mandatory")
_MscVrIpArpHostOperTable_Object = MibTable
mscVrIpArpHostOperTable = _MscVrIpArpHostOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 2, 11)
)
if mibBuilder.loadTexts:
    mscVrIpArpHostOperTable.setStatus("mandatory")
_MscVrIpArpHostOperEntry_Object = MibTableRow
mscVrIpArpHostOperEntry = _MscVrIpArpHostOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 2, 11, 1)
)
mscVrIpArpHostOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpArpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpArpHostHostAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpArpHostOperEntry.setStatus("mandatory")


class _MscVrIpArpHostOperMaxTxUnit_Type(Unsigned32):
    """Custom type mscVrIpArpHostOperMaxTxUnit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 18944),
    )


_MscVrIpArpHostOperMaxTxUnit_Type.__name__ = "Unsigned32"
_MscVrIpArpHostOperMaxTxUnit_Object = MibTableColumn
mscVrIpArpHostOperMaxTxUnit = _MscVrIpArpHostOperMaxTxUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 2, 11, 1, 4),
    _MscVrIpArpHostOperMaxTxUnit_Type()
)
mscVrIpArpHostOperMaxTxUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpArpHostOperMaxTxUnit.setStatus("mandatory")


class _MscVrIpArpHostOperEncap_Type(Integer32):
    """Custom type mscVrIpArpHostOperEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("ieee8023", 1),
          ("notApplicable", 3))
    )


_MscVrIpArpHostOperEncap_Type.__name__ = "Integer32"
_MscVrIpArpHostOperEncap_Object = MibTableColumn
mscVrIpArpHostOperEncap = _MscVrIpArpHostOperEncap_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 2, 11, 1, 5),
    _MscVrIpArpHostOperEncap_Type()
)
mscVrIpArpHostOperEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpArpHostOperEncap.setStatus("mandatory")
_MscVrIpArpDynHost_ObjectIdentity = ObjectIdentity
mscVrIpArpDynHost = _MscVrIpArpDynHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 3)
)
_MscVrIpArpDynHostRowStatusTable_Object = MibTable
mscVrIpArpDynHostRowStatusTable = _MscVrIpArpDynHostRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 3, 1)
)
if mibBuilder.loadTexts:
    mscVrIpArpDynHostRowStatusTable.setStatus("mandatory")
_MscVrIpArpDynHostRowStatusEntry_Object = MibTableRow
mscVrIpArpDynHostRowStatusEntry = _MscVrIpArpDynHostRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 3, 1, 1)
)
mscVrIpArpDynHostRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpArpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpArpDynHostHostAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpArpDynHostCosIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpArpDynHostRowStatusEntry.setStatus("mandatory")
_MscVrIpArpDynHostRowStatus_Type = RowStatus
_MscVrIpArpDynHostRowStatus_Object = MibTableColumn
mscVrIpArpDynHostRowStatus = _MscVrIpArpDynHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 3, 1, 1, 1),
    _MscVrIpArpDynHostRowStatus_Type()
)
mscVrIpArpDynHostRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpArpDynHostRowStatus.setStatus("mandatory")
_MscVrIpArpDynHostComponentName_Type = DisplayString
_MscVrIpArpDynHostComponentName_Object = MibTableColumn
mscVrIpArpDynHostComponentName = _MscVrIpArpDynHostComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 3, 1, 1, 2),
    _MscVrIpArpDynHostComponentName_Type()
)
mscVrIpArpDynHostComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpArpDynHostComponentName.setStatus("mandatory")
_MscVrIpArpDynHostStorageType_Type = StorageType
_MscVrIpArpDynHostStorageType_Object = MibTableColumn
mscVrIpArpDynHostStorageType = _MscVrIpArpDynHostStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 3, 1, 1, 4),
    _MscVrIpArpDynHostStorageType_Type()
)
mscVrIpArpDynHostStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpArpDynHostStorageType.setStatus("mandatory")
_MscVrIpArpDynHostHostAddressIndex_Type = IpAddress
_MscVrIpArpDynHostHostAddressIndex_Object = MibTableColumn
mscVrIpArpDynHostHostAddressIndex = _MscVrIpArpDynHostHostAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 3, 1, 1, 10),
    _MscVrIpArpDynHostHostAddressIndex_Type()
)
mscVrIpArpDynHostHostAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpArpDynHostHostAddressIndex.setStatus("mandatory")


class _MscVrIpArpDynHostCosIndex_Type(Integer32):
    """Custom type mscVrIpArpDynHostCosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n2", 2),
          ("n3", 3),
          ("notApplicable", 4))
    )


_MscVrIpArpDynHostCosIndex_Type.__name__ = "Integer32"
_MscVrIpArpDynHostCosIndex_Object = MibTableColumn
mscVrIpArpDynHostCosIndex = _MscVrIpArpDynHostCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 3, 1, 1, 11),
    _MscVrIpArpDynHostCosIndex_Type()
)
mscVrIpArpDynHostCosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpArpDynHostCosIndex.setStatus("mandatory")
_MscVrIpArpDynHostOperTable_Object = MibTable
mscVrIpArpDynHostOperTable = _MscVrIpArpDynHostOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 3, 10)
)
if mibBuilder.loadTexts:
    mscVrIpArpDynHostOperTable.setStatus("mandatory")
_MscVrIpArpDynHostOperEntry_Object = MibTableRow
mscVrIpArpDynHostOperEntry = _MscVrIpArpDynHostOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 3, 10, 1)
)
mscVrIpArpDynHostOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpArpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpArpDynHostHostAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpArpDynHostCosIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpArpDynHostOperEntry.setStatus("mandatory")


class _MscVrIpArpDynHostPhysAddress_Type(PhysAddress):
    """Custom type mscVrIpArpDynHostPhysAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MscVrIpArpDynHostPhysAddress_Type.__name__ = "PhysAddress"
_MscVrIpArpDynHostPhysAddress_Object = MibTableColumn
mscVrIpArpDynHostPhysAddress = _MscVrIpArpDynHostPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 3, 10, 1, 1),
    _MscVrIpArpDynHostPhysAddress_Type()
)
mscVrIpArpDynHostPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpArpDynHostPhysAddress.setStatus("mandatory")


class _MscVrIpArpDynHostMaxTxUnit_Type(Unsigned32):
    """Custom type mscVrIpArpDynHostMaxTxUnit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 18944),
    )


_MscVrIpArpDynHostMaxTxUnit_Type.__name__ = "Unsigned32"
_MscVrIpArpDynHostMaxTxUnit_Object = MibTableColumn
mscVrIpArpDynHostMaxTxUnit = _MscVrIpArpDynHostMaxTxUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 3, 10, 1, 3),
    _MscVrIpArpDynHostMaxTxUnit_Type()
)
mscVrIpArpDynHostMaxTxUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpArpDynHostMaxTxUnit.setStatus("mandatory")


class _MscVrIpArpDynHostEncapsulationType_Type(Integer32):
    """Custom type mscVrIpArpDynHostEncapsulationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("ieee8023", 1),
          ("notApplicable", 3))
    )


_MscVrIpArpDynHostEncapsulationType_Type.__name__ = "Integer32"
_MscVrIpArpDynHostEncapsulationType_Object = MibTableColumn
mscVrIpArpDynHostEncapsulationType = _MscVrIpArpDynHostEncapsulationType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 3, 10, 1, 4),
    _MscVrIpArpDynHostEncapsulationType_Type()
)
mscVrIpArpDynHostEncapsulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpArpDynHostEncapsulationType.setStatus("mandatory")


class _MscVrIpArpDynHostPermanentVirtualCircuitNumber_Type(Unsigned32):
    """Custom type mscVrIpArpDynHostPermanentVirtualCircuitNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MscVrIpArpDynHostPermanentVirtualCircuitNumber_Type.__name__ = "Unsigned32"
_MscVrIpArpDynHostPermanentVirtualCircuitNumber_Object = MibTableColumn
mscVrIpArpDynHostPermanentVirtualCircuitNumber = _MscVrIpArpDynHostPermanentVirtualCircuitNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 3, 10, 1, 5),
    _MscVrIpArpDynHostPermanentVirtualCircuitNumber_Type()
)
mscVrIpArpDynHostPermanentVirtualCircuitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpArpDynHostPermanentVirtualCircuitNumber.setStatus("mandatory")


class _MscVrIpArpDynHostIfIndex_Type(InterfaceIndex):
    """Custom type mscVrIpArpDynHostIfIndex based on InterfaceIndex"""
    defaultValue = 1

    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrIpArpDynHostIfIndex_Type.__name__ = "InterfaceIndex"
_MscVrIpArpDynHostIfIndex_Object = MibTableColumn
mscVrIpArpDynHostIfIndex = _MscVrIpArpDynHostIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 3, 10, 1, 6),
    _MscVrIpArpDynHostIfIndex_Type()
)
mscVrIpArpDynHostIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpArpDynHostIfIndex.setStatus("mandatory")


class _MscVrIpArpDynHostType_Type(Integer32):
    """Custom type mscVrIpArpDynHostType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 3),
          ("invalid", 2),
          ("pending", 1),
          ("static", 4))
    )


_MscVrIpArpDynHostType_Type.__name__ = "Integer32"
_MscVrIpArpDynHostType_Object = MibTableColumn
mscVrIpArpDynHostType = _MscVrIpArpDynHostType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 3, 10, 1, 7),
    _MscVrIpArpDynHostType_Type()
)
mscVrIpArpDynHostType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpArpDynHostType.setStatus("mandatory")


class _MscVrIpArpDynHostNcPhysAddress_Type(PhysAddress):
    """Custom type mscVrIpArpDynHostNcPhysAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MscVrIpArpDynHostNcPhysAddress_Type.__name__ = "PhysAddress"
_MscVrIpArpDynHostNcPhysAddress_Object = MibTableColumn
mscVrIpArpDynHostNcPhysAddress = _MscVrIpArpDynHostNcPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 3, 10, 1, 8),
    _MscVrIpArpDynHostNcPhysAddress_Type()
)
mscVrIpArpDynHostNcPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpArpDynHostNcPhysAddress.setStatus("mandatory")


class _MscVrIpArpDynHostTunnelDestinationAddress_Type(IpAddress):
    """Custom type mscVrIpArpDynHostTunnelDestinationAddress based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrIpArpDynHostTunnelDestinationAddress_Object = MibTableColumn
mscVrIpArpDynHostTunnelDestinationAddress = _MscVrIpArpDynHostTunnelDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 3, 10, 1, 9),
    _MscVrIpArpDynHostTunnelDestinationAddress_Type()
)
mscVrIpArpDynHostTunnelDestinationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpArpDynHostTunnelDestinationAddress.setStatus("mandatory")
_MscVrIpArpProvTable_Object = MibTable
mscVrIpArpProvTable = _MscVrIpArpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 10)
)
if mibBuilder.loadTexts:
    mscVrIpArpProvTable.setStatus("mandatory")
_MscVrIpArpProvEntry_Object = MibTableRow
mscVrIpArpProvEntry = _MscVrIpArpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 10, 1)
)
mscVrIpArpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpArpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpArpProvEntry.setStatus("mandatory")


class _MscVrIpArpAutoRefresh_Type(Integer32):
    """Custom type mscVrIpArpAutoRefresh based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MscVrIpArpAutoRefresh_Type.__name__ = "Integer32"
_MscVrIpArpAutoRefresh_Object = MibTableColumn
mscVrIpArpAutoRefresh = _MscVrIpArpAutoRefresh_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 10, 1, 1),
    _MscVrIpArpAutoRefresh_Type()
)
mscVrIpArpAutoRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpArpAutoRefresh.setStatus("mandatory")


class _MscVrIpArpAutoRefreshTimeout_Type(Unsigned32):
    """Custom type mscVrIpArpAutoRefreshTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_MscVrIpArpAutoRefreshTimeout_Type.__name__ = "Unsigned32"
_MscVrIpArpAutoRefreshTimeout_Object = MibTableColumn
mscVrIpArpAutoRefreshTimeout = _MscVrIpArpAutoRefreshTimeout_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 11, 10, 1, 2),
    _MscVrIpArpAutoRefreshTimeout_Type()
)
mscVrIpArpAutoRefreshTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpArpAutoRefreshTimeout.setStatus("mandatory")
_MscVrIpIcmp_ObjectIdentity = ObjectIdentity
mscVrIpIcmp = _MscVrIpIcmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12)
)
_MscVrIpIcmpRowStatusTable_Object = MibTable
mscVrIpIcmpRowStatusTable = _MscVrIpIcmpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 1)
)
if mibBuilder.loadTexts:
    mscVrIpIcmpRowStatusTable.setStatus("mandatory")
_MscVrIpIcmpRowStatusEntry_Object = MibTableRow
mscVrIpIcmpRowStatusEntry = _MscVrIpIcmpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 1, 1)
)
mscVrIpIcmpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIcmpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpIcmpRowStatusEntry.setStatus("mandatory")
_MscVrIpIcmpRowStatus_Type = RowStatus
_MscVrIpIcmpRowStatus_Object = MibTableColumn
mscVrIpIcmpRowStatus = _MscVrIpIcmpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 1, 1, 1),
    _MscVrIpIcmpRowStatus_Type()
)
mscVrIpIcmpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpRowStatus.setStatus("mandatory")
_MscVrIpIcmpComponentName_Type = DisplayString
_MscVrIpIcmpComponentName_Object = MibTableColumn
mscVrIpIcmpComponentName = _MscVrIpIcmpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 1, 1, 2),
    _MscVrIpIcmpComponentName_Type()
)
mscVrIpIcmpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpComponentName.setStatus("mandatory")
_MscVrIpIcmpStorageType_Type = StorageType
_MscVrIpIcmpStorageType_Object = MibTableColumn
mscVrIpIcmpStorageType = _MscVrIpIcmpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 1, 1, 4),
    _MscVrIpIcmpStorageType_Type()
)
mscVrIpIcmpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpStorageType.setStatus("mandatory")
_MscVrIpIcmpIndex_Type = NonReplicated
_MscVrIpIcmpIndex_Object = MibTableColumn
mscVrIpIcmpIndex = _MscVrIpIcmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 1, 1, 10),
    _MscVrIpIcmpIndex_Type()
)
mscVrIpIcmpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpIcmpIndex.setStatus("mandatory")
_MscVrIpIcmpProvTable_Object = MibTable
mscVrIpIcmpProvTable = _MscVrIpIcmpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 10)
)
if mibBuilder.loadTexts:
    mscVrIpIcmpProvTable.setStatus("mandatory")
_MscVrIpIcmpProvEntry_Object = MibTableRow
mscVrIpIcmpProvEntry = _MscVrIpIcmpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 10, 1)
)
mscVrIpIcmpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIcmpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpIcmpProvEntry.setStatus("mandatory")


class _MscVrIpIcmpSendRedirect_Type(Integer32):
    """Custom type mscVrIpIcmpSendRedirect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MscVrIpIcmpSendRedirect_Type.__name__ = "Integer32"
_MscVrIpIcmpSendRedirect_Object = MibTableColumn
mscVrIpIcmpSendRedirect = _MscVrIpIcmpSendRedirect_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 10, 1, 1),
    _MscVrIpIcmpSendRedirect_Type()
)
mscVrIpIcmpSendRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpIcmpSendRedirect.setStatus("obsolete")


class _MscVrIpIcmpSendHostUnreachable_Type(Integer32):
    """Custom type mscVrIpIcmpSendHostUnreachable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MscVrIpIcmpSendHostUnreachable_Type.__name__ = "Integer32"
_MscVrIpIcmpSendHostUnreachable_Object = MibTableColumn
mscVrIpIcmpSendHostUnreachable = _MscVrIpIcmpSendHostUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 10, 1, 2),
    _MscVrIpIcmpSendHostUnreachable_Type()
)
mscVrIpIcmpSendHostUnreachable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpIcmpSendHostUnreachable.setStatus("obsolete")
_MscVrIpIcmpStatsTable_Object = MibTable
mscVrIpIcmpStatsTable = _MscVrIpIcmpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11)
)
if mibBuilder.loadTexts:
    mscVrIpIcmpStatsTable.setStatus("mandatory")
_MscVrIpIcmpStatsEntry_Object = MibTableRow
mscVrIpIcmpStatsEntry = _MscVrIpIcmpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1)
)
mscVrIpIcmpStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIcmpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpIcmpStatsEntry.setStatus("mandatory")
_MscVrIpIcmpInMsgs_Type = Counter32
_MscVrIpIcmpInMsgs_Object = MibTableColumn
mscVrIpIcmpInMsgs = _MscVrIpIcmpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 1),
    _MscVrIpIcmpInMsgs_Type()
)
mscVrIpIcmpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpInMsgs.setStatus("mandatory")
_MscVrIpIcmpInErrors_Type = Counter32
_MscVrIpIcmpInErrors_Object = MibTableColumn
mscVrIpIcmpInErrors = _MscVrIpIcmpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 2),
    _MscVrIpIcmpInErrors_Type()
)
mscVrIpIcmpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpInErrors.setStatus("mandatory")
_MscVrIpIcmpInDestUnreachs_Type = Counter32
_MscVrIpIcmpInDestUnreachs_Object = MibTableColumn
mscVrIpIcmpInDestUnreachs = _MscVrIpIcmpInDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 3),
    _MscVrIpIcmpInDestUnreachs_Type()
)
mscVrIpIcmpInDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpInDestUnreachs.setStatus("mandatory")
_MscVrIpIcmpInTimeExcds_Type = Counter32
_MscVrIpIcmpInTimeExcds_Object = MibTableColumn
mscVrIpIcmpInTimeExcds = _MscVrIpIcmpInTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 4),
    _MscVrIpIcmpInTimeExcds_Type()
)
mscVrIpIcmpInTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpInTimeExcds.setStatus("mandatory")
_MscVrIpIcmpInParmProbs_Type = Counter32
_MscVrIpIcmpInParmProbs_Object = MibTableColumn
mscVrIpIcmpInParmProbs = _MscVrIpIcmpInParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 5),
    _MscVrIpIcmpInParmProbs_Type()
)
mscVrIpIcmpInParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpInParmProbs.setStatus("mandatory")
_MscVrIpIcmpInSrcQuenchs_Type = Counter32
_MscVrIpIcmpInSrcQuenchs_Object = MibTableColumn
mscVrIpIcmpInSrcQuenchs = _MscVrIpIcmpInSrcQuenchs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 6),
    _MscVrIpIcmpInSrcQuenchs_Type()
)
mscVrIpIcmpInSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpInSrcQuenchs.setStatus("mandatory")
_MscVrIpIcmpInRedirects_Type = Counter32
_MscVrIpIcmpInRedirects_Object = MibTableColumn
mscVrIpIcmpInRedirects = _MscVrIpIcmpInRedirects_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 7),
    _MscVrIpIcmpInRedirects_Type()
)
mscVrIpIcmpInRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpInRedirects.setStatus("mandatory")
_MscVrIpIcmpInEchos_Type = Counter32
_MscVrIpIcmpInEchos_Object = MibTableColumn
mscVrIpIcmpInEchos = _MscVrIpIcmpInEchos_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 8),
    _MscVrIpIcmpInEchos_Type()
)
mscVrIpIcmpInEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpInEchos.setStatus("mandatory")
_MscVrIpIcmpInEchoReps_Type = Counter32
_MscVrIpIcmpInEchoReps_Object = MibTableColumn
mscVrIpIcmpInEchoReps = _MscVrIpIcmpInEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 9),
    _MscVrIpIcmpInEchoReps_Type()
)
mscVrIpIcmpInEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpInEchoReps.setStatus("mandatory")
_MscVrIpIcmpInTimestamps_Type = Counter32
_MscVrIpIcmpInTimestamps_Object = MibTableColumn
mscVrIpIcmpInTimestamps = _MscVrIpIcmpInTimestamps_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 10),
    _MscVrIpIcmpInTimestamps_Type()
)
mscVrIpIcmpInTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpInTimestamps.setStatus("mandatory")
_MscVrIpIcmpInTimestampReps_Type = Counter32
_MscVrIpIcmpInTimestampReps_Object = MibTableColumn
mscVrIpIcmpInTimestampReps = _MscVrIpIcmpInTimestampReps_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 11),
    _MscVrIpIcmpInTimestampReps_Type()
)
mscVrIpIcmpInTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpInTimestampReps.setStatus("mandatory")
_MscVrIpIcmpInAddrMasks_Type = Counter32
_MscVrIpIcmpInAddrMasks_Object = MibTableColumn
mscVrIpIcmpInAddrMasks = _MscVrIpIcmpInAddrMasks_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 12),
    _MscVrIpIcmpInAddrMasks_Type()
)
mscVrIpIcmpInAddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpInAddrMasks.setStatus("mandatory")
_MscVrIpIcmpInAddrMaskReps_Type = Counter32
_MscVrIpIcmpInAddrMaskReps_Object = MibTableColumn
mscVrIpIcmpInAddrMaskReps = _MscVrIpIcmpInAddrMaskReps_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 13),
    _MscVrIpIcmpInAddrMaskReps_Type()
)
mscVrIpIcmpInAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpInAddrMaskReps.setStatus("mandatory")
_MscVrIpIcmpOutMsgs_Type = Counter32
_MscVrIpIcmpOutMsgs_Object = MibTableColumn
mscVrIpIcmpOutMsgs = _MscVrIpIcmpOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 14),
    _MscVrIpIcmpOutMsgs_Type()
)
mscVrIpIcmpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpOutMsgs.setStatus("mandatory")
_MscVrIpIcmpOutErrors_Type = Counter32
_MscVrIpIcmpOutErrors_Object = MibTableColumn
mscVrIpIcmpOutErrors = _MscVrIpIcmpOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 15),
    _MscVrIpIcmpOutErrors_Type()
)
mscVrIpIcmpOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpOutErrors.setStatus("mandatory")
_MscVrIpIcmpOutDestUnreachs_Type = Counter32
_MscVrIpIcmpOutDestUnreachs_Object = MibTableColumn
mscVrIpIcmpOutDestUnreachs = _MscVrIpIcmpOutDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 16),
    _MscVrIpIcmpOutDestUnreachs_Type()
)
mscVrIpIcmpOutDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpOutDestUnreachs.setStatus("mandatory")
_MscVrIpIcmpOutTimeExcds_Type = Counter32
_MscVrIpIcmpOutTimeExcds_Object = MibTableColumn
mscVrIpIcmpOutTimeExcds = _MscVrIpIcmpOutTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 17),
    _MscVrIpIcmpOutTimeExcds_Type()
)
mscVrIpIcmpOutTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpOutTimeExcds.setStatus("mandatory")
_MscVrIpIcmpOutParmProbs_Type = Counter32
_MscVrIpIcmpOutParmProbs_Object = MibTableColumn
mscVrIpIcmpOutParmProbs = _MscVrIpIcmpOutParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 18),
    _MscVrIpIcmpOutParmProbs_Type()
)
mscVrIpIcmpOutParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpOutParmProbs.setStatus("mandatory")
_MscVrIpIcmpOutSrcQuenchs_Type = Counter32
_MscVrIpIcmpOutSrcQuenchs_Object = MibTableColumn
mscVrIpIcmpOutSrcQuenchs = _MscVrIpIcmpOutSrcQuenchs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 19),
    _MscVrIpIcmpOutSrcQuenchs_Type()
)
mscVrIpIcmpOutSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpOutSrcQuenchs.setStatus("mandatory")
_MscVrIpIcmpOutRedirects_Type = Counter32
_MscVrIpIcmpOutRedirects_Object = MibTableColumn
mscVrIpIcmpOutRedirects = _MscVrIpIcmpOutRedirects_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 20),
    _MscVrIpIcmpOutRedirects_Type()
)
mscVrIpIcmpOutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpOutRedirects.setStatus("mandatory")
_MscVrIpIcmpOutEchos_Type = Counter32
_MscVrIpIcmpOutEchos_Object = MibTableColumn
mscVrIpIcmpOutEchos = _MscVrIpIcmpOutEchos_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 21),
    _MscVrIpIcmpOutEchos_Type()
)
mscVrIpIcmpOutEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpOutEchos.setStatus("mandatory")
_MscVrIpIcmpOutEchoReps_Type = Counter32
_MscVrIpIcmpOutEchoReps_Object = MibTableColumn
mscVrIpIcmpOutEchoReps = _MscVrIpIcmpOutEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 22),
    _MscVrIpIcmpOutEchoReps_Type()
)
mscVrIpIcmpOutEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpOutEchoReps.setStatus("mandatory")
_MscVrIpIcmpOutTimestamps_Type = Counter32
_MscVrIpIcmpOutTimestamps_Object = MibTableColumn
mscVrIpIcmpOutTimestamps = _MscVrIpIcmpOutTimestamps_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 23),
    _MscVrIpIcmpOutTimestamps_Type()
)
mscVrIpIcmpOutTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpOutTimestamps.setStatus("mandatory")
_MscVrIpIcmpOutTimestampReps_Type = Counter32
_MscVrIpIcmpOutTimestampReps_Object = MibTableColumn
mscVrIpIcmpOutTimestampReps = _MscVrIpIcmpOutTimestampReps_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 24),
    _MscVrIpIcmpOutTimestampReps_Type()
)
mscVrIpIcmpOutTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpOutTimestampReps.setStatus("mandatory")
_MscVrIpIcmpOutAddrMasks_Type = Counter32
_MscVrIpIcmpOutAddrMasks_Object = MibTableColumn
mscVrIpIcmpOutAddrMasks = _MscVrIpIcmpOutAddrMasks_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 25),
    _MscVrIpIcmpOutAddrMasks_Type()
)
mscVrIpIcmpOutAddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpOutAddrMasks.setStatus("mandatory")
_MscVrIpIcmpOutAddrMaskReps_Type = Counter32
_MscVrIpIcmpOutAddrMaskReps_Object = MibTableColumn
mscVrIpIcmpOutAddrMaskReps = _MscVrIpIcmpOutAddrMaskReps_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 26),
    _MscVrIpIcmpOutAddrMaskReps_Type()
)
mscVrIpIcmpOutAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpOutAddrMaskReps.setStatus("mandatory")
_MscVrIpIcmpInRtrAdvs_Type = Counter32
_MscVrIpIcmpInRtrAdvs_Object = MibTableColumn
mscVrIpIcmpInRtrAdvs = _MscVrIpIcmpInRtrAdvs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 27),
    _MscVrIpIcmpInRtrAdvs_Type()
)
mscVrIpIcmpInRtrAdvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpInRtrAdvs.setStatus("mandatory")
_MscVrIpIcmpInRtrSolicits_Type = Counter32
_MscVrIpIcmpInRtrSolicits_Object = MibTableColumn
mscVrIpIcmpInRtrSolicits = _MscVrIpIcmpInRtrSolicits_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 28),
    _MscVrIpIcmpInRtrSolicits_Type()
)
mscVrIpIcmpInRtrSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpInRtrSolicits.setStatus("mandatory")
_MscVrIpIcmpOutRtrAdvs_Type = Counter32
_MscVrIpIcmpOutRtrAdvs_Object = MibTableColumn
mscVrIpIcmpOutRtrAdvs = _MscVrIpIcmpOutRtrAdvs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 29),
    _MscVrIpIcmpOutRtrAdvs_Type()
)
mscVrIpIcmpOutRtrAdvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpOutRtrAdvs.setStatus("mandatory")
_MscVrIpIcmpOutRtrSolicits_Type = Counter32
_MscVrIpIcmpOutRtrSolicits_Object = MibTableColumn
mscVrIpIcmpOutRtrSolicits = _MscVrIpIcmpOutRtrSolicits_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 12, 11, 1, 30),
    _MscVrIpIcmpOutRtrSolicits_Type()
)
mscVrIpIcmpOutRtrSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpIcmpOutRtrSolicits.setStatus("mandatory")
_MscVrIpRelayBC_ObjectIdentity = ObjectIdentity
mscVrIpRelayBC = _MscVrIpRelayBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 13)
)
_MscVrIpRelayBCRowStatusTable_Object = MibTable
mscVrIpRelayBCRowStatusTable = _MscVrIpRelayBCRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 13, 1)
)
if mibBuilder.loadTexts:
    mscVrIpRelayBCRowStatusTable.setStatus("mandatory")
_MscVrIpRelayBCRowStatusEntry_Object = MibTableRow
mscVrIpRelayBCRowStatusEntry = _MscVrIpRelayBCRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 13, 1, 1)
)
mscVrIpRelayBCRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRelayBCIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpRelayBCRowStatusEntry.setStatus("mandatory")
_MscVrIpRelayBCRowStatus_Type = RowStatus
_MscVrIpRelayBCRowStatus_Object = MibTableColumn
mscVrIpRelayBCRowStatus = _MscVrIpRelayBCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 13, 1, 1, 1),
    _MscVrIpRelayBCRowStatus_Type()
)
mscVrIpRelayBCRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRelayBCRowStatus.setStatus("mandatory")
_MscVrIpRelayBCComponentName_Type = DisplayString
_MscVrIpRelayBCComponentName_Object = MibTableColumn
mscVrIpRelayBCComponentName = _MscVrIpRelayBCComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 13, 1, 1, 2),
    _MscVrIpRelayBCComponentName_Type()
)
mscVrIpRelayBCComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRelayBCComponentName.setStatus("mandatory")
_MscVrIpRelayBCStorageType_Type = StorageType
_MscVrIpRelayBCStorageType_Object = MibTableColumn
mscVrIpRelayBCStorageType = _MscVrIpRelayBCStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 13, 1, 1, 4),
    _MscVrIpRelayBCStorageType_Type()
)
mscVrIpRelayBCStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRelayBCStorageType.setStatus("mandatory")
_MscVrIpRelayBCIndex_Type = NonReplicated
_MscVrIpRelayBCIndex_Object = MibTableColumn
mscVrIpRelayBCIndex = _MscVrIpRelayBCIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 13, 1, 1, 10),
    _MscVrIpRelayBCIndex_Type()
)
mscVrIpRelayBCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpRelayBCIndex.setStatus("mandatory")
_MscVrIpRelayBCPort_ObjectIdentity = ObjectIdentity
mscVrIpRelayBCPort = _MscVrIpRelayBCPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 13, 2)
)
_MscVrIpRelayBCPortRowStatusTable_Object = MibTable
mscVrIpRelayBCPortRowStatusTable = _MscVrIpRelayBCPortRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 13, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpRelayBCPortRowStatusTable.setStatus("mandatory")
_MscVrIpRelayBCPortRowStatusEntry_Object = MibTableRow
mscVrIpRelayBCPortRowStatusEntry = _MscVrIpRelayBCPortRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 13, 2, 1, 1)
)
mscVrIpRelayBCPortRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRelayBCIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRelayBCPortPortNumIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpRelayBCPortRowStatusEntry.setStatus("mandatory")
_MscVrIpRelayBCPortRowStatus_Type = RowStatus
_MscVrIpRelayBCPortRowStatus_Object = MibTableColumn
mscVrIpRelayBCPortRowStatus = _MscVrIpRelayBCPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 13, 2, 1, 1, 1),
    _MscVrIpRelayBCPortRowStatus_Type()
)
mscVrIpRelayBCPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRelayBCPortRowStatus.setStatus("mandatory")
_MscVrIpRelayBCPortComponentName_Type = DisplayString
_MscVrIpRelayBCPortComponentName_Object = MibTableColumn
mscVrIpRelayBCPortComponentName = _MscVrIpRelayBCPortComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 13, 2, 1, 1, 2),
    _MscVrIpRelayBCPortComponentName_Type()
)
mscVrIpRelayBCPortComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRelayBCPortComponentName.setStatus("mandatory")
_MscVrIpRelayBCPortStorageType_Type = StorageType
_MscVrIpRelayBCPortStorageType_Object = MibTableColumn
mscVrIpRelayBCPortStorageType = _MscVrIpRelayBCPortStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 13, 2, 1, 1, 4),
    _MscVrIpRelayBCPortStorageType_Type()
)
mscVrIpRelayBCPortStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRelayBCPortStorageType.setStatus("mandatory")


class _MscVrIpRelayBCPortPortNumIndex_Type(Integer32):
    """Custom type mscVrIpRelayBCPortPortNumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_MscVrIpRelayBCPortPortNumIndex_Type.__name__ = "Integer32"
_MscVrIpRelayBCPortPortNumIndex_Object = MibTableColumn
mscVrIpRelayBCPortPortNumIndex = _MscVrIpRelayBCPortPortNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 13, 2, 1, 1, 10),
    _MscVrIpRelayBCPortPortNumIndex_Type()
)
mscVrIpRelayBCPortPortNumIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpRelayBCPortPortNumIndex.setStatus("mandatory")
_MscVrIpRelayBCPortOperTable_Object = MibTable
mscVrIpRelayBCPortOperTable = _MscVrIpRelayBCPortOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 13, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpRelayBCPortOperTable.setStatus("mandatory")
_MscVrIpRelayBCPortOperEntry_Object = MibTableRow
mscVrIpRelayBCPortOperEntry = _MscVrIpRelayBCPortOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 13, 2, 10, 1)
)
mscVrIpRelayBCPortOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRelayBCIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRelayBCPortPortNumIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpRelayBCPortOperEntry.setStatus("mandatory")
_MscVrIpRelayBCPortRelayBcUdpCount_Type = Counter32
_MscVrIpRelayBCPortRelayBcUdpCount_Object = MibTableColumn
mscVrIpRelayBCPortRelayBcUdpCount = _MscVrIpRelayBCPortRelayBcUdpCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 13, 2, 10, 1, 1),
    _MscVrIpRelayBCPortRelayBcUdpCount_Type()
)
mscVrIpRelayBCPortRelayBcUdpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRelayBCPortRelayBcUdpCount.setStatus("mandatory")
_MscVrIpRelayBCProvTable_Object = MibTable
mscVrIpRelayBCProvTable = _MscVrIpRelayBCProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 13, 10)
)
if mibBuilder.loadTexts:
    mscVrIpRelayBCProvTable.setStatus("mandatory")
_MscVrIpRelayBCProvEntry_Object = MibTableRow
mscVrIpRelayBCProvEntry = _MscVrIpRelayBCProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 13, 10, 1)
)
mscVrIpRelayBCProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRelayBCIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpRelayBCProvEntry.setStatus("mandatory")


class _MscVrIpRelayBCRelayStatus_Type(Integer32):
    """Custom type mscVrIpRelayBCRelayStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MscVrIpRelayBCRelayStatus_Type.__name__ = "Integer32"
_MscVrIpRelayBCRelayStatus_Object = MibTableColumn
mscVrIpRelayBCRelayStatus = _MscVrIpRelayBCRelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 13, 10, 1, 1),
    _MscVrIpRelayBCRelayStatus_Type()
)
mscVrIpRelayBCRelayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRelayBCRelayStatus.setStatus("mandatory")


class _MscVrIpRelayBCRelayNdStatus_Type(Integer32):
    """Custom type mscVrIpRelayBCRelayNdStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MscVrIpRelayBCRelayNdStatus_Type.__name__ = "Integer32"
_MscVrIpRelayBCRelayNdStatus_Object = MibTableColumn
mscVrIpRelayBCRelayNdStatus = _MscVrIpRelayBCRelayNdStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 13, 10, 1, 2),
    _MscVrIpRelayBCRelayNdStatus_Type()
)
mscVrIpRelayBCRelayNdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpRelayBCRelayNdStatus.setStatus("mandatory")
_MscVrIpRelayBCOperTable_Object = MibTable
mscVrIpRelayBCOperTable = _MscVrIpRelayBCOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 13, 11)
)
if mibBuilder.loadTexts:
    mscVrIpRelayBCOperTable.setStatus("mandatory")
_MscVrIpRelayBCOperEntry_Object = MibTableRow
mscVrIpRelayBCOperEntry = _MscVrIpRelayBCOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 13, 11, 1)
)
mscVrIpRelayBCOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpRelayBCIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpRelayBCOperEntry.setStatus("mandatory")
_MscVrIpRelayBCRelayNdCount_Type = Counter32
_MscVrIpRelayBCRelayNdCount_Object = MibTableColumn
mscVrIpRelayBCRelayNdCount = _MscVrIpRelayBCRelayNdCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 13, 11, 1, 1),
    _MscVrIpRelayBCRelayNdCount_Type()
)
mscVrIpRelayBCRelayNdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRelayBCRelayNdCount.setStatus("mandatory")
_MscVrIpUdp_ObjectIdentity = ObjectIdentity
mscVrIpUdp = _MscVrIpUdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 14)
)
_MscVrIpUdpRowStatusTable_Object = MibTable
mscVrIpUdpRowStatusTable = _MscVrIpUdpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 14, 1)
)
if mibBuilder.loadTexts:
    mscVrIpUdpRowStatusTable.setStatus("mandatory")
_MscVrIpUdpRowStatusEntry_Object = MibTableRow
mscVrIpUdpRowStatusEntry = _MscVrIpUdpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 14, 1, 1)
)
mscVrIpUdpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpUdpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpUdpRowStatusEntry.setStatus("mandatory")
_MscVrIpUdpRowStatus_Type = RowStatus
_MscVrIpUdpRowStatus_Object = MibTableColumn
mscVrIpUdpRowStatus = _MscVrIpUdpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 14, 1, 1, 1),
    _MscVrIpUdpRowStatus_Type()
)
mscVrIpUdpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpUdpRowStatus.setStatus("mandatory")
_MscVrIpUdpComponentName_Type = DisplayString
_MscVrIpUdpComponentName_Object = MibTableColumn
mscVrIpUdpComponentName = _MscVrIpUdpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 14, 1, 1, 2),
    _MscVrIpUdpComponentName_Type()
)
mscVrIpUdpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpUdpComponentName.setStatus("mandatory")
_MscVrIpUdpStorageType_Type = StorageType
_MscVrIpUdpStorageType_Object = MibTableColumn
mscVrIpUdpStorageType = _MscVrIpUdpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 14, 1, 1, 4),
    _MscVrIpUdpStorageType_Type()
)
mscVrIpUdpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpUdpStorageType.setStatus("mandatory")
_MscVrIpUdpIndex_Type = NonReplicated
_MscVrIpUdpIndex_Object = MibTableColumn
mscVrIpUdpIndex = _MscVrIpUdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 14, 1, 1, 10),
    _MscVrIpUdpIndex_Type()
)
mscVrIpUdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpUdpIndex.setStatus("mandatory")
_MscVrIpUdpListenEntry_ObjectIdentity = ObjectIdentity
mscVrIpUdpListenEntry = _MscVrIpUdpListenEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 14, 2)
)
_MscVrIpUdpListenEntryRowStatusTable_Object = MibTable
mscVrIpUdpListenEntryRowStatusTable = _MscVrIpUdpListenEntryRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 14, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpUdpListenEntryRowStatusTable.setStatus("mandatory")
_MscVrIpUdpListenEntryRowStatusEntry_Object = MibTableRow
mscVrIpUdpListenEntryRowStatusEntry = _MscVrIpUdpListenEntryRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 14, 2, 1, 1)
)
mscVrIpUdpListenEntryRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpUdpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpUdpListenEntryLocalAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpUdpListenEntryLocalPortIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpUdpListenEntryRowStatusEntry.setStatus("mandatory")
_MscVrIpUdpListenEntryRowStatus_Type = RowStatus
_MscVrIpUdpListenEntryRowStatus_Object = MibTableColumn
mscVrIpUdpListenEntryRowStatus = _MscVrIpUdpListenEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 14, 2, 1, 1, 1),
    _MscVrIpUdpListenEntryRowStatus_Type()
)
mscVrIpUdpListenEntryRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpUdpListenEntryRowStatus.setStatus("mandatory")
_MscVrIpUdpListenEntryComponentName_Type = DisplayString
_MscVrIpUdpListenEntryComponentName_Object = MibTableColumn
mscVrIpUdpListenEntryComponentName = _MscVrIpUdpListenEntryComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 14, 2, 1, 1, 2),
    _MscVrIpUdpListenEntryComponentName_Type()
)
mscVrIpUdpListenEntryComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpUdpListenEntryComponentName.setStatus("mandatory")
_MscVrIpUdpListenEntryStorageType_Type = StorageType
_MscVrIpUdpListenEntryStorageType_Object = MibTableColumn
mscVrIpUdpListenEntryStorageType = _MscVrIpUdpListenEntryStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 14, 2, 1, 1, 4),
    _MscVrIpUdpListenEntryStorageType_Type()
)
mscVrIpUdpListenEntryStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpUdpListenEntryStorageType.setStatus("mandatory")
_MscVrIpUdpListenEntryLocalAddressIndex_Type = IpAddress
_MscVrIpUdpListenEntryLocalAddressIndex_Object = MibTableColumn
mscVrIpUdpListenEntryLocalAddressIndex = _MscVrIpUdpListenEntryLocalAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 14, 2, 1, 1, 10),
    _MscVrIpUdpListenEntryLocalAddressIndex_Type()
)
mscVrIpUdpListenEntryLocalAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpUdpListenEntryLocalAddressIndex.setStatus("mandatory")


class _MscVrIpUdpListenEntryLocalPortIndex_Type(Integer32):
    """Custom type mscVrIpUdpListenEntryLocalPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpUdpListenEntryLocalPortIndex_Type.__name__ = "Integer32"
_MscVrIpUdpListenEntryLocalPortIndex_Object = MibTableColumn
mscVrIpUdpListenEntryLocalPortIndex = _MscVrIpUdpListenEntryLocalPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 14, 2, 1, 1, 11),
    _MscVrIpUdpListenEntryLocalPortIndex_Type()
)
mscVrIpUdpListenEntryLocalPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpUdpListenEntryLocalPortIndex.setStatus("mandatory")
_MscVrIpUdpStatsTable_Object = MibTable
mscVrIpUdpStatsTable = _MscVrIpUdpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 14, 10)
)
if mibBuilder.loadTexts:
    mscVrIpUdpStatsTable.setStatus("mandatory")
_MscVrIpUdpStatsEntry_Object = MibTableRow
mscVrIpUdpStatsEntry = _MscVrIpUdpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 14, 10, 1)
)
mscVrIpUdpStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpUdpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpUdpStatsEntry.setStatus("mandatory")
_MscVrIpUdpInDatagrams_Type = Counter32
_MscVrIpUdpInDatagrams_Object = MibTableColumn
mscVrIpUdpInDatagrams = _MscVrIpUdpInDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 14, 10, 1, 1),
    _MscVrIpUdpInDatagrams_Type()
)
mscVrIpUdpInDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpUdpInDatagrams.setStatus("mandatory")
_MscVrIpUdpNoPorts_Type = Counter32
_MscVrIpUdpNoPorts_Object = MibTableColumn
mscVrIpUdpNoPorts = _MscVrIpUdpNoPorts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 14, 10, 1, 2),
    _MscVrIpUdpNoPorts_Type()
)
mscVrIpUdpNoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpUdpNoPorts.setStatus("mandatory")
_MscVrIpUdpInErrors_Type = Counter32
_MscVrIpUdpInErrors_Object = MibTableColumn
mscVrIpUdpInErrors = _MscVrIpUdpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 14, 10, 1, 3),
    _MscVrIpUdpInErrors_Type()
)
mscVrIpUdpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpUdpInErrors.setStatus("mandatory")
_MscVrIpUdpOutDatagrams_Type = Counter32
_MscVrIpUdpOutDatagrams_Object = MibTableColumn
mscVrIpUdpOutDatagrams = _MscVrIpUdpOutDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 14, 10, 1, 4),
    _MscVrIpUdpOutDatagrams_Type()
)
mscVrIpUdpOutDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpUdpOutDatagrams.setStatus("mandatory")
_MscVrIpTcp_ObjectIdentity = ObjectIdentity
mscVrIpTcp = _MscVrIpTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15)
)
_MscVrIpTcpRowStatusTable_Object = MibTable
mscVrIpTcpRowStatusTable = _MscVrIpTcpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 1)
)
if mibBuilder.loadTexts:
    mscVrIpTcpRowStatusTable.setStatus("mandatory")
_MscVrIpTcpRowStatusEntry_Object = MibTableRow
mscVrIpTcpRowStatusEntry = _MscVrIpTcpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 1, 1)
)
mscVrIpTcpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTcpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpTcpRowStatusEntry.setStatus("mandatory")
_MscVrIpTcpRowStatus_Type = RowStatus
_MscVrIpTcpRowStatus_Object = MibTableColumn
mscVrIpTcpRowStatus = _MscVrIpTcpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 1, 1, 1),
    _MscVrIpTcpRowStatus_Type()
)
mscVrIpTcpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTcpRowStatus.setStatus("mandatory")
_MscVrIpTcpComponentName_Type = DisplayString
_MscVrIpTcpComponentName_Object = MibTableColumn
mscVrIpTcpComponentName = _MscVrIpTcpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 1, 1, 2),
    _MscVrIpTcpComponentName_Type()
)
mscVrIpTcpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTcpComponentName.setStatus("mandatory")
_MscVrIpTcpStorageType_Type = StorageType
_MscVrIpTcpStorageType_Object = MibTableColumn
mscVrIpTcpStorageType = _MscVrIpTcpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 1, 1, 4),
    _MscVrIpTcpStorageType_Type()
)
mscVrIpTcpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTcpStorageType.setStatus("mandatory")
_MscVrIpTcpIndex_Type = NonReplicated
_MscVrIpTcpIndex_Object = MibTableColumn
mscVrIpTcpIndex = _MscVrIpTcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 1, 1, 10),
    _MscVrIpTcpIndex_Type()
)
mscVrIpTcpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpTcpIndex.setStatus("mandatory")
_MscVrIpTcpTcpEntry_ObjectIdentity = ObjectIdentity
mscVrIpTcpTcpEntry = _MscVrIpTcpTcpEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 2)
)
_MscVrIpTcpTcpEntryRowStatusTable_Object = MibTable
mscVrIpTcpTcpEntryRowStatusTable = _MscVrIpTcpTcpEntryRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpTcpTcpEntryRowStatusTable.setStatus("mandatory")
_MscVrIpTcpTcpEntryRowStatusEntry_Object = MibTableRow
mscVrIpTcpTcpEntryRowStatusEntry = _MscVrIpTcpTcpEntryRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 2, 1, 1)
)
mscVrIpTcpTcpEntryRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTcpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTcpTcpEntryLocalAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTcpTcpEntryLocalPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTcpTcpEntryRemoteAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTcpTcpEntryRemotePortIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpTcpTcpEntryRowStatusEntry.setStatus("mandatory")
_MscVrIpTcpTcpEntryRowStatus_Type = RowStatus
_MscVrIpTcpTcpEntryRowStatus_Object = MibTableColumn
mscVrIpTcpTcpEntryRowStatus = _MscVrIpTcpTcpEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 2, 1, 1, 1),
    _MscVrIpTcpTcpEntryRowStatus_Type()
)
mscVrIpTcpTcpEntryRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTcpTcpEntryRowStatus.setStatus("mandatory")
_MscVrIpTcpTcpEntryComponentName_Type = DisplayString
_MscVrIpTcpTcpEntryComponentName_Object = MibTableColumn
mscVrIpTcpTcpEntryComponentName = _MscVrIpTcpTcpEntryComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 2, 1, 1, 2),
    _MscVrIpTcpTcpEntryComponentName_Type()
)
mscVrIpTcpTcpEntryComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTcpTcpEntryComponentName.setStatus("mandatory")
_MscVrIpTcpTcpEntryStorageType_Type = StorageType
_MscVrIpTcpTcpEntryStorageType_Object = MibTableColumn
mscVrIpTcpTcpEntryStorageType = _MscVrIpTcpTcpEntryStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 2, 1, 1, 4),
    _MscVrIpTcpTcpEntryStorageType_Type()
)
mscVrIpTcpTcpEntryStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTcpTcpEntryStorageType.setStatus("mandatory")
_MscVrIpTcpTcpEntryLocalAddressIndex_Type = IpAddress
_MscVrIpTcpTcpEntryLocalAddressIndex_Object = MibTableColumn
mscVrIpTcpTcpEntryLocalAddressIndex = _MscVrIpTcpTcpEntryLocalAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 2, 1, 1, 10),
    _MscVrIpTcpTcpEntryLocalAddressIndex_Type()
)
mscVrIpTcpTcpEntryLocalAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpTcpTcpEntryLocalAddressIndex.setStatus("mandatory")


class _MscVrIpTcpTcpEntryLocalPortIndex_Type(Integer32):
    """Custom type mscVrIpTcpTcpEntryLocalPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpTcpTcpEntryLocalPortIndex_Type.__name__ = "Integer32"
_MscVrIpTcpTcpEntryLocalPortIndex_Object = MibTableColumn
mscVrIpTcpTcpEntryLocalPortIndex = _MscVrIpTcpTcpEntryLocalPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 2, 1, 1, 11),
    _MscVrIpTcpTcpEntryLocalPortIndex_Type()
)
mscVrIpTcpTcpEntryLocalPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpTcpTcpEntryLocalPortIndex.setStatus("mandatory")
_MscVrIpTcpTcpEntryRemoteAddressIndex_Type = IpAddress
_MscVrIpTcpTcpEntryRemoteAddressIndex_Object = MibTableColumn
mscVrIpTcpTcpEntryRemoteAddressIndex = _MscVrIpTcpTcpEntryRemoteAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 2, 1, 1, 12),
    _MscVrIpTcpTcpEntryRemoteAddressIndex_Type()
)
mscVrIpTcpTcpEntryRemoteAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpTcpTcpEntryRemoteAddressIndex.setStatus("mandatory")


class _MscVrIpTcpTcpEntryRemotePortIndex_Type(Integer32):
    """Custom type mscVrIpTcpTcpEntryRemotePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpTcpTcpEntryRemotePortIndex_Type.__name__ = "Integer32"
_MscVrIpTcpTcpEntryRemotePortIndex_Object = MibTableColumn
mscVrIpTcpTcpEntryRemotePortIndex = _MscVrIpTcpTcpEntryRemotePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 2, 1, 1, 13),
    _MscVrIpTcpTcpEntryRemotePortIndex_Type()
)
mscVrIpTcpTcpEntryRemotePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpTcpTcpEntryRemotePortIndex.setStatus("mandatory")
_MscVrIpTcpTcpEntryOperTable_Object = MibTable
mscVrIpTcpTcpEntryOperTable = _MscVrIpTcpTcpEntryOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpTcpTcpEntryOperTable.setStatus("mandatory")
_MscVrIpTcpTcpEntryOperEntry_Object = MibTableRow
mscVrIpTcpTcpEntryOperEntry = _MscVrIpTcpTcpEntryOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 2, 10, 1)
)
mscVrIpTcpTcpEntryOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTcpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTcpTcpEntryLocalAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTcpTcpEntryLocalPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTcpTcpEntryRemoteAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTcpTcpEntryRemotePortIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpTcpTcpEntryOperEntry.setStatus("mandatory")


class _MscVrIpTcpTcpEntryState_Type(Integer32):
    """Custom type mscVrIpTcpTcpEntryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("closeWait", 6),
          ("closed", 1),
          ("closing", 8),
          ("delete", 12),
          ("established", 5),
          ("finWait1", 7),
          ("finWait2", 10),
          ("lastAck", 9),
          ("listen", 2),
          ("synReceived", 4),
          ("synSent", 3),
          ("timeWait", 11))
    )


_MscVrIpTcpTcpEntryState_Type.__name__ = "Integer32"
_MscVrIpTcpTcpEntryState_Object = MibTableColumn
mscVrIpTcpTcpEntryState = _MscVrIpTcpTcpEntryState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 2, 10, 1, 1),
    _MscVrIpTcpTcpEntryState_Type()
)
mscVrIpTcpTcpEntryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpTcpTcpEntryState.setStatus("mandatory")
_MscVrIpTcpStatsTable_Object = MibTable
mscVrIpTcpStatsTable = _MscVrIpTcpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 10)
)
if mibBuilder.loadTexts:
    mscVrIpTcpStatsTable.setStatus("mandatory")
_MscVrIpTcpStatsEntry_Object = MibTableRow
mscVrIpTcpStatsEntry = _MscVrIpTcpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 10, 1)
)
mscVrIpTcpStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTcpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpTcpStatsEntry.setStatus("mandatory")


class _MscVrIpTcpRToAlgorithm_Type(Integer32):
    """Custom type mscVrIpTcpRToAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("constant", 2),
          ("other", 1),
          ("rsre", 3),
          ("vanJacobson", 4))
    )


_MscVrIpTcpRToAlgorithm_Type.__name__ = "Integer32"
_MscVrIpTcpRToAlgorithm_Object = MibTableColumn
mscVrIpTcpRToAlgorithm = _MscVrIpTcpRToAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 10, 1, 1),
    _MscVrIpTcpRToAlgorithm_Type()
)
mscVrIpTcpRToAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTcpRToAlgorithm.setStatus("mandatory")


class _MscVrIpTcpRToMin_Type(Unsigned32):
    """Custom type mscVrIpTcpRToMin based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpTcpRToMin_Type.__name__ = "Unsigned32"
_MscVrIpTcpRToMin_Object = MibTableColumn
mscVrIpTcpRToMin = _MscVrIpTcpRToMin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 10, 1, 2),
    _MscVrIpTcpRToMin_Type()
)
mscVrIpTcpRToMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTcpRToMin.setStatus("mandatory")


class _MscVrIpTcpRToMax_Type(Unsigned32):
    """Custom type mscVrIpTcpRToMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpTcpRToMax_Type.__name__ = "Unsigned32"
_MscVrIpTcpRToMax_Object = MibTableColumn
mscVrIpTcpRToMax = _MscVrIpTcpRToMax_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 10, 1, 3),
    _MscVrIpTcpRToMax_Type()
)
mscVrIpTcpRToMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTcpRToMax.setStatus("mandatory")


class _MscVrIpTcpMaxConn_Type(Integer32):
    """Custom type mscVrIpTcpMaxConn based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
    )


_MscVrIpTcpMaxConn_Type.__name__ = "Integer32"
_MscVrIpTcpMaxConn_Object = MibTableColumn
mscVrIpTcpMaxConn = _MscVrIpTcpMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 10, 1, 4),
    _MscVrIpTcpMaxConn_Type()
)
mscVrIpTcpMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTcpMaxConn.setStatus("mandatory")
_MscVrIpTcpActiveOpens_Type = Counter32
_MscVrIpTcpActiveOpens_Object = MibTableColumn
mscVrIpTcpActiveOpens = _MscVrIpTcpActiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 10, 1, 5),
    _MscVrIpTcpActiveOpens_Type()
)
mscVrIpTcpActiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTcpActiveOpens.setStatus("mandatory")
_MscVrIpTcpPassiveOpens_Type = Counter32
_MscVrIpTcpPassiveOpens_Object = MibTableColumn
mscVrIpTcpPassiveOpens = _MscVrIpTcpPassiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 10, 1, 6),
    _MscVrIpTcpPassiveOpens_Type()
)
mscVrIpTcpPassiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTcpPassiveOpens.setStatus("mandatory")
_MscVrIpTcpAttemptFails_Type = Counter32
_MscVrIpTcpAttemptFails_Object = MibTableColumn
mscVrIpTcpAttemptFails = _MscVrIpTcpAttemptFails_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 10, 1, 7),
    _MscVrIpTcpAttemptFails_Type()
)
mscVrIpTcpAttemptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTcpAttemptFails.setStatus("mandatory")
_MscVrIpTcpEstabResets_Type = Counter32
_MscVrIpTcpEstabResets_Object = MibTableColumn
mscVrIpTcpEstabResets = _MscVrIpTcpEstabResets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 10, 1, 8),
    _MscVrIpTcpEstabResets_Type()
)
mscVrIpTcpEstabResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTcpEstabResets.setStatus("mandatory")


class _MscVrIpTcpCurrEstab_Type(Gauge32):
    """Custom type mscVrIpTcpCurrEstab based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpTcpCurrEstab_Type.__name__ = "Gauge32"
_MscVrIpTcpCurrEstab_Object = MibTableColumn
mscVrIpTcpCurrEstab = _MscVrIpTcpCurrEstab_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 10, 1, 9),
    _MscVrIpTcpCurrEstab_Type()
)
mscVrIpTcpCurrEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTcpCurrEstab.setStatus("mandatory")
_MscVrIpTcpInSegs_Type = Counter32
_MscVrIpTcpInSegs_Object = MibTableColumn
mscVrIpTcpInSegs = _MscVrIpTcpInSegs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 10, 1, 10),
    _MscVrIpTcpInSegs_Type()
)
mscVrIpTcpInSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTcpInSegs.setStatus("mandatory")
_MscVrIpTcpOutSegs_Type = Counter32
_MscVrIpTcpOutSegs_Object = MibTableColumn
mscVrIpTcpOutSegs = _MscVrIpTcpOutSegs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 10, 1, 11),
    _MscVrIpTcpOutSegs_Type()
)
mscVrIpTcpOutSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTcpOutSegs.setStatus("mandatory")
_MscVrIpTcpRetransSegs_Type = Counter32
_MscVrIpTcpRetransSegs_Object = MibTableColumn
mscVrIpTcpRetransSegs = _MscVrIpTcpRetransSegs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 10, 1, 12),
    _MscVrIpTcpRetransSegs_Type()
)
mscVrIpTcpRetransSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTcpRetransSegs.setStatus("mandatory")
_MscVrIpTcpInErrs_Type = Counter32
_MscVrIpTcpInErrs_Object = MibTableColumn
mscVrIpTcpInErrs = _MscVrIpTcpInErrs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 10, 1, 13),
    _MscVrIpTcpInErrs_Type()
)
mscVrIpTcpInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTcpInErrs.setStatus("mandatory")
_MscVrIpTcpOutRsts_Type = Counter32
_MscVrIpTcpOutRsts_Object = MibTableColumn
mscVrIpTcpOutRsts = _MscVrIpTcpOutRsts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 15, 10, 1, 14),
    _MscVrIpTcpOutRsts_Type()
)
mscVrIpTcpOutRsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTcpOutRsts.setStatus("mandatory")
_MscVrIpBootp_ObjectIdentity = ObjectIdentity
mscVrIpBootp = _MscVrIpBootp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16)
)
_MscVrIpBootpRowStatusTable_Object = MibTable
mscVrIpBootpRowStatusTable = _MscVrIpBootpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 1)
)
if mibBuilder.loadTexts:
    mscVrIpBootpRowStatusTable.setStatus("mandatory")
_MscVrIpBootpRowStatusEntry_Object = MibTableRow
mscVrIpBootpRowStatusEntry = _MscVrIpBootpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 1, 1)
)
mscVrIpBootpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpBootpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBootpRowStatusEntry.setStatus("mandatory")
_MscVrIpBootpRowStatus_Type = RowStatus
_MscVrIpBootpRowStatus_Object = MibTableColumn
mscVrIpBootpRowStatus = _MscVrIpBootpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 1, 1, 1),
    _MscVrIpBootpRowStatus_Type()
)
mscVrIpBootpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBootpRowStatus.setStatus("mandatory")
_MscVrIpBootpComponentName_Type = DisplayString
_MscVrIpBootpComponentName_Object = MibTableColumn
mscVrIpBootpComponentName = _MscVrIpBootpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 1, 1, 2),
    _MscVrIpBootpComponentName_Type()
)
mscVrIpBootpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBootpComponentName.setStatus("mandatory")
_MscVrIpBootpStorageType_Type = StorageType
_MscVrIpBootpStorageType_Object = MibTableColumn
mscVrIpBootpStorageType = _MscVrIpBootpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 1, 1, 4),
    _MscVrIpBootpStorageType_Type()
)
mscVrIpBootpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBootpStorageType.setStatus("mandatory")
_MscVrIpBootpIndex_Type = NonReplicated
_MscVrIpBootpIndex_Object = MibTableColumn
mscVrIpBootpIndex = _MscVrIpBootpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 1, 1, 10),
    _MscVrIpBootpIndex_Type()
)
mscVrIpBootpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpBootpIndex.setStatus("mandatory")
_MscVrIpBootpPpE_ObjectIdentity = ObjectIdentity
mscVrIpBootpPpE = _MscVrIpBootpPpE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 2)
)
_MscVrIpBootpPpERowStatusTable_Object = MibTable
mscVrIpBootpPpERowStatusTable = _MscVrIpBootpPpERowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpBootpPpERowStatusTable.setStatus("mandatory")
_MscVrIpBootpPpERowStatusEntry_Object = MibTableRow
mscVrIpBootpPpERowStatusEntry = _MscVrIpBootpPpERowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 2, 1, 1)
)
mscVrIpBootpPpERowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpBootpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpBootpPpEIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBootpPpERowStatusEntry.setStatus("mandatory")
_MscVrIpBootpPpERowStatus_Type = RowStatus
_MscVrIpBootpPpERowStatus_Object = MibTableColumn
mscVrIpBootpPpERowStatus = _MscVrIpBootpPpERowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 2, 1, 1, 1),
    _MscVrIpBootpPpERowStatus_Type()
)
mscVrIpBootpPpERowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBootpPpERowStatus.setStatus("mandatory")
_MscVrIpBootpPpEComponentName_Type = DisplayString
_MscVrIpBootpPpEComponentName_Object = MibTableColumn
mscVrIpBootpPpEComponentName = _MscVrIpBootpPpEComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 2, 1, 1, 2),
    _MscVrIpBootpPpEComponentName_Type()
)
mscVrIpBootpPpEComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBootpPpEComponentName.setStatus("mandatory")
_MscVrIpBootpPpEStorageType_Type = StorageType
_MscVrIpBootpPpEStorageType_Object = MibTableColumn
mscVrIpBootpPpEStorageType = _MscVrIpBootpPpEStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 2, 1, 1, 4),
    _MscVrIpBootpPpEStorageType_Type()
)
mscVrIpBootpPpEStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBootpPpEStorageType.setStatus("mandatory")


class _MscVrIpBootpPpEIndex_Type(AsciiStringIndex):
    """Custom type mscVrIpBootpPpEIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_MscVrIpBootpPpEIndex_Type.__name__ = "AsciiStringIndex"
_MscVrIpBootpPpEIndex_Object = MibTableColumn
mscVrIpBootpPpEIndex = _MscVrIpBootpPpEIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 2, 1, 1, 10),
    _MscVrIpBootpPpEIndex_Type()
)
mscVrIpBootpPpEIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpBootpPpEIndex.setStatus("mandatory")
_MscVrIpBootpPpEOperTable_Object = MibTable
mscVrIpBootpPpEOperTable = _MscVrIpBootpPpEOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpBootpPpEOperTable.setStatus("mandatory")
_MscVrIpBootpPpEOperEntry_Object = MibTableRow
mscVrIpBootpPpEOperEntry = _MscVrIpBootpPpEOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 2, 10, 1)
)
mscVrIpBootpPpEOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpBootpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpBootpPpEIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBootpPpEOperEntry.setStatus("mandatory")


class _MscVrIpBootpPpEStatus_Type(Integer32):
    """Custom type mscVrIpBootpPpEStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("down", 2),
          ("up", 1))
    )


_MscVrIpBootpPpEStatus_Type.__name__ = "Integer32"
_MscVrIpBootpPpEStatus_Object = MibTableColumn
mscVrIpBootpPpEStatus = _MscVrIpBootpPpEStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 2, 10, 1, 1),
    _MscVrIpBootpPpEStatus_Type()
)
mscVrIpBootpPpEStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBootpPpEStatus.setStatus("mandatory")
_MscVrIpBootpPpEStatsTable_Object = MibTable
mscVrIpBootpPpEStatsTable = _MscVrIpBootpPpEStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 2, 11)
)
if mibBuilder.loadTexts:
    mscVrIpBootpPpEStatsTable.setStatus("mandatory")
_MscVrIpBootpPpEStatsEntry_Object = MibTableRow
mscVrIpBootpPpEStatsEntry = _MscVrIpBootpPpEStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 2, 11, 1)
)
mscVrIpBootpPpEStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpBootpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpBootpPpEIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBootpPpEStatsEntry.setStatus("mandatory")
_MscVrIpBootpPpEInRequests_Type = Counter32
_MscVrIpBootpPpEInRequests_Object = MibTableColumn
mscVrIpBootpPpEInRequests = _MscVrIpBootpPpEInRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 2, 11, 1, 1),
    _MscVrIpBootpPpEInRequests_Type()
)
mscVrIpBootpPpEInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBootpPpEInRequests.setStatus("mandatory")
_MscVrIpBootpPpEInReplies_Type = Counter32
_MscVrIpBootpPpEInReplies_Object = MibTableColumn
mscVrIpBootpPpEInReplies = _MscVrIpBootpPpEInReplies_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 2, 11, 1, 2),
    _MscVrIpBootpPpEInReplies_Type()
)
mscVrIpBootpPpEInReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBootpPpEInReplies.setStatus("mandatory")
_MscVrIpBootpPpEOutRequests_Type = Counter32
_MscVrIpBootpPpEOutRequests_Object = MibTableColumn
mscVrIpBootpPpEOutRequests = _MscVrIpBootpPpEOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 2, 11, 1, 3),
    _MscVrIpBootpPpEOutRequests_Type()
)
mscVrIpBootpPpEOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBootpPpEOutRequests.setStatus("mandatory")
_MscVrIpBootpPpEOutReplies_Type = Counter32
_MscVrIpBootpPpEOutReplies_Object = MibTableColumn
mscVrIpBootpPpEOutReplies = _MscVrIpBootpPpEOutReplies_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 2, 11, 1, 4),
    _MscVrIpBootpPpEOutReplies_Type()
)
mscVrIpBootpPpEOutReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBootpPpEOutReplies.setStatus("mandatory")
_MscVrIpBootpPpEInRequestErrors_Type = Counter32
_MscVrIpBootpPpEInRequestErrors_Object = MibTableColumn
mscVrIpBootpPpEInRequestErrors = _MscVrIpBootpPpEInRequestErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 2, 11, 1, 5),
    _MscVrIpBootpPpEInRequestErrors_Type()
)
mscVrIpBootpPpEInRequestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBootpPpEInRequestErrors.setStatus("mandatory")
_MscVrIpBootpPpEInReplyErrors_Type = Counter32
_MscVrIpBootpPpEInReplyErrors_Object = MibTableColumn
mscVrIpBootpPpEInReplyErrors = _MscVrIpBootpPpEInReplyErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 2, 11, 1, 6),
    _MscVrIpBootpPpEInReplyErrors_Type()
)
mscVrIpBootpPpEInReplyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBootpPpEInReplyErrors.setStatus("mandatory")
_MscVrIpBootpAdminControlTable_Object = MibTable
mscVrIpBootpAdminControlTable = _MscVrIpBootpAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 10)
)
if mibBuilder.loadTexts:
    mscVrIpBootpAdminControlTable.setStatus("mandatory")
_MscVrIpBootpAdminControlEntry_Object = MibTableRow
mscVrIpBootpAdminControlEntry = _MscVrIpBootpAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 10, 1)
)
mscVrIpBootpAdminControlEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpBootpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBootpAdminControlEntry.setStatus("mandatory")


class _MscVrIpBootpSnmpAdminStatus_Type(Integer32):
    """Custom type mscVrIpBootpSnmpAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscVrIpBootpSnmpAdminStatus_Type.__name__ = "Integer32"
_MscVrIpBootpSnmpAdminStatus_Object = MibTableColumn
mscVrIpBootpSnmpAdminStatus = _MscVrIpBootpSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 10, 1, 1),
    _MscVrIpBootpSnmpAdminStatus_Type()
)
mscVrIpBootpSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBootpSnmpAdminStatus.setStatus("mandatory")
_MscVrIpBootpProvTable_Object = MibTable
mscVrIpBootpProvTable = _MscVrIpBootpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 11)
)
if mibBuilder.loadTexts:
    mscVrIpBootpProvTable.setStatus("mandatory")
_MscVrIpBootpProvEntry_Object = MibTableRow
mscVrIpBootpProvEntry = _MscVrIpBootpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 11, 1)
)
mscVrIpBootpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpBootpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBootpProvEntry.setStatus("mandatory")


class _MscVrIpBootpHopDiscardThreshold_Type(Unsigned32):
    """Custom type mscVrIpBootpHopDiscardThreshold based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 16),
    )


_MscVrIpBootpHopDiscardThreshold_Type.__name__ = "Unsigned32"
_MscVrIpBootpHopDiscardThreshold_Object = MibTableColumn
mscVrIpBootpHopDiscardThreshold = _MscVrIpBootpHopDiscardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 11, 1, 1),
    _MscVrIpBootpHopDiscardThreshold_Type()
)
mscVrIpBootpHopDiscardThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBootpHopDiscardThreshold.setStatus("mandatory")
_MscVrIpBootpStateTable_Object = MibTable
mscVrIpBootpStateTable = _MscVrIpBootpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 12)
)
if mibBuilder.loadTexts:
    mscVrIpBootpStateTable.setStatus("mandatory")
_MscVrIpBootpStateEntry_Object = MibTableRow
mscVrIpBootpStateEntry = _MscVrIpBootpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 12, 1)
)
mscVrIpBootpStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpBootpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBootpStateEntry.setStatus("mandatory")


class _MscVrIpBootpAdminState_Type(Integer32):
    """Custom type mscVrIpBootpAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_MscVrIpBootpAdminState_Type.__name__ = "Integer32"
_MscVrIpBootpAdminState_Object = MibTableColumn
mscVrIpBootpAdminState = _MscVrIpBootpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 12, 1, 1),
    _MscVrIpBootpAdminState_Type()
)
mscVrIpBootpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBootpAdminState.setStatus("mandatory")


class _MscVrIpBootpOperationalState_Type(Integer32):
    """Custom type mscVrIpBootpOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MscVrIpBootpOperationalState_Type.__name__ = "Integer32"
_MscVrIpBootpOperationalState_Object = MibTableColumn
mscVrIpBootpOperationalState = _MscVrIpBootpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 12, 1, 2),
    _MscVrIpBootpOperationalState_Type()
)
mscVrIpBootpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBootpOperationalState.setStatus("mandatory")


class _MscVrIpBootpUsageState_Type(Integer32):
    """Custom type mscVrIpBootpUsageState based on Integer32"""
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
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_MscVrIpBootpUsageState_Type.__name__ = "Integer32"
_MscVrIpBootpUsageState_Object = MibTableColumn
mscVrIpBootpUsageState = _MscVrIpBootpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 12, 1, 3),
    _MscVrIpBootpUsageState_Type()
)
mscVrIpBootpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBootpUsageState.setStatus("mandatory")
_MscVrIpBootpOperStatusTable_Object = MibTable
mscVrIpBootpOperStatusTable = _MscVrIpBootpOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 13)
)
if mibBuilder.loadTexts:
    mscVrIpBootpOperStatusTable.setStatus("mandatory")
_MscVrIpBootpOperStatusEntry_Object = MibTableRow
mscVrIpBootpOperStatusEntry = _MscVrIpBootpOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 13, 1)
)
mscVrIpBootpOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpBootpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBootpOperStatusEntry.setStatus("mandatory")


class _MscVrIpBootpSnmpOperStatus_Type(Integer32):
    """Custom type mscVrIpBootpSnmpOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscVrIpBootpSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrIpBootpSnmpOperStatus_Object = MibTableColumn
mscVrIpBootpSnmpOperStatus = _MscVrIpBootpSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 16, 13, 1, 1),
    _MscVrIpBootpSnmpOperStatus_Type()
)
mscVrIpBootpSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBootpSnmpOperStatus.setStatus("mandatory")
_MscVrIpCache_ObjectIdentity = ObjectIdentity
mscVrIpCache = _MscVrIpCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 17)
)
_MscVrIpCacheRowStatusTable_Object = MibTable
mscVrIpCacheRowStatusTable = _MscVrIpCacheRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 17, 1)
)
if mibBuilder.loadTexts:
    mscVrIpCacheRowStatusTable.setStatus("mandatory")
_MscVrIpCacheRowStatusEntry_Object = MibTableRow
mscVrIpCacheRowStatusEntry = _MscVrIpCacheRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 17, 1, 1)
)
mscVrIpCacheRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpCacheIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpCacheRowStatusEntry.setStatus("mandatory")
_MscVrIpCacheRowStatus_Type = RowStatus
_MscVrIpCacheRowStatus_Object = MibTableColumn
mscVrIpCacheRowStatus = _MscVrIpCacheRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 17, 1, 1, 1),
    _MscVrIpCacheRowStatus_Type()
)
mscVrIpCacheRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpCacheRowStatus.setStatus("mandatory")
_MscVrIpCacheComponentName_Type = DisplayString
_MscVrIpCacheComponentName_Object = MibTableColumn
mscVrIpCacheComponentName = _MscVrIpCacheComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 17, 1, 1, 2),
    _MscVrIpCacheComponentName_Type()
)
mscVrIpCacheComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpCacheComponentName.setStatus("mandatory")
_MscVrIpCacheStorageType_Type = StorageType
_MscVrIpCacheStorageType_Object = MibTableColumn
mscVrIpCacheStorageType = _MscVrIpCacheStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 17, 1, 1, 4),
    _MscVrIpCacheStorageType_Type()
)
mscVrIpCacheStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpCacheStorageType.setStatus("mandatory")


class _MscVrIpCacheIndex_Type(Integer32):
    """Custom type mscVrIpCacheIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscVrIpCacheIndex_Type.__name__ = "Integer32"
_MscVrIpCacheIndex_Object = MibTableColumn
mscVrIpCacheIndex = _MscVrIpCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 17, 1, 1, 10),
    _MscVrIpCacheIndex_Type()
)
mscVrIpCacheIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpCacheIndex.setStatus("mandatory")
_MscVrIpCacheStateTable_Object = MibTable
mscVrIpCacheStateTable = _MscVrIpCacheStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 17, 10)
)
if mibBuilder.loadTexts:
    mscVrIpCacheStateTable.setStatus("mandatory")
_MscVrIpCacheStateEntry_Object = MibTableRow
mscVrIpCacheStateEntry = _MscVrIpCacheStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 17, 10, 1)
)
mscVrIpCacheStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpCacheIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpCacheStateEntry.setStatus("mandatory")


class _MscVrIpCacheAdminState_Type(Integer32):
    """Custom type mscVrIpCacheAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_MscVrIpCacheAdminState_Type.__name__ = "Integer32"
_MscVrIpCacheAdminState_Object = MibTableColumn
mscVrIpCacheAdminState = _MscVrIpCacheAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 17, 10, 1, 1),
    _MscVrIpCacheAdminState_Type()
)
mscVrIpCacheAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpCacheAdminState.setStatus("mandatory")


class _MscVrIpCacheOperationalState_Type(Integer32):
    """Custom type mscVrIpCacheOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MscVrIpCacheOperationalState_Type.__name__ = "Integer32"
_MscVrIpCacheOperationalState_Object = MibTableColumn
mscVrIpCacheOperationalState = _MscVrIpCacheOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 17, 10, 1, 2),
    _MscVrIpCacheOperationalState_Type()
)
mscVrIpCacheOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpCacheOperationalState.setStatus("mandatory")


class _MscVrIpCacheUsageState_Type(Integer32):
    """Custom type mscVrIpCacheUsageState based on Integer32"""
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
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_MscVrIpCacheUsageState_Type.__name__ = "Integer32"
_MscVrIpCacheUsageState_Object = MibTableColumn
mscVrIpCacheUsageState = _MscVrIpCacheUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 17, 10, 1, 3),
    _MscVrIpCacheUsageState_Type()
)
mscVrIpCacheUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpCacheUsageState.setStatus("mandatory")
_MscVrIpCacheOperTable_Object = MibTable
mscVrIpCacheOperTable = _MscVrIpCacheOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 17, 11)
)
if mibBuilder.loadTexts:
    mscVrIpCacheOperTable.setStatus("mandatory")
_MscVrIpCacheOperEntry_Object = MibTableRow
mscVrIpCacheOperEntry = _MscVrIpCacheOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 17, 11, 1)
)
mscVrIpCacheOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpCacheIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpCacheOperEntry.setStatus("mandatory")


class _MscVrIpCacheEntriesFree_Type(Unsigned32):
    """Custom type mscVrIpCacheEntriesFree based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_MscVrIpCacheEntriesFree_Type.__name__ = "Unsigned32"
_MscVrIpCacheEntriesFree_Object = MibTableColumn
mscVrIpCacheEntriesFree = _MscVrIpCacheEntriesFree_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 17, 11, 1, 3),
    _MscVrIpCacheEntriesFree_Type()
)
mscVrIpCacheEntriesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpCacheEntriesFree.setStatus("mandatory")


class _MscVrIpCacheTotalLookups_Type(Unsigned32):
    """Custom type mscVrIpCacheTotalLookups based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpCacheTotalLookups_Type.__name__ = "Unsigned32"
_MscVrIpCacheTotalLookups_Object = MibTableColumn
mscVrIpCacheTotalLookups = _MscVrIpCacheTotalLookups_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 17, 11, 1, 4),
    _MscVrIpCacheTotalLookups_Type()
)
mscVrIpCacheTotalLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpCacheTotalLookups.setStatus("mandatory")
_MscVrIpCacheLookupMisses_Type = Counter32
_MscVrIpCacheLookupMisses_Object = MibTableColumn
mscVrIpCacheLookupMisses = _MscVrIpCacheLookupMisses_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 17, 11, 1, 5),
    _MscVrIpCacheLookupMisses_Type()
)
mscVrIpCacheLookupMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpCacheLookupMisses.setStatus("mandatory")


class _MscVrIpCacheCacheTableMaxEntries_Type(Unsigned32):
    """Custom type mscVrIpCacheCacheTableMaxEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_MscVrIpCacheCacheTableMaxEntries_Type.__name__ = "Unsigned32"
_MscVrIpCacheCacheTableMaxEntries_Object = MibTableColumn
mscVrIpCacheCacheTableMaxEntries = _MscVrIpCacheCacheTableMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 17, 11, 1, 395),
    _MscVrIpCacheCacheTableMaxEntries_Type()
)
mscVrIpCacheCacheTableMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpCacheCacheTableMaxEntries.setStatus("mandatory")
_MscVrIpTunnel_ObjectIdentity = ObjectIdentity
mscVrIpTunnel = _MscVrIpTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18)
)
_MscVrIpTunnelRowStatusTable_Object = MibTable
mscVrIpTunnelRowStatusTable = _MscVrIpTunnelRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 1)
)
if mibBuilder.loadTexts:
    mscVrIpTunnelRowStatusTable.setStatus("mandatory")
_MscVrIpTunnelRowStatusEntry_Object = MibTableRow
mscVrIpTunnelRowStatusEntry = _MscVrIpTunnelRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 1, 1)
)
mscVrIpTunnelRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTunnelIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpTunnelRowStatusEntry.setStatus("mandatory")
_MscVrIpTunnelRowStatus_Type = RowStatus
_MscVrIpTunnelRowStatus_Object = MibTableColumn
mscVrIpTunnelRowStatus = _MscVrIpTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 1, 1, 1),
    _MscVrIpTunnelRowStatus_Type()
)
mscVrIpTunnelRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpTunnelRowStatus.setStatus("mandatory")
_MscVrIpTunnelComponentName_Type = DisplayString
_MscVrIpTunnelComponentName_Object = MibTableColumn
mscVrIpTunnelComponentName = _MscVrIpTunnelComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 1, 1, 2),
    _MscVrIpTunnelComponentName_Type()
)
mscVrIpTunnelComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTunnelComponentName.setStatus("mandatory")
_MscVrIpTunnelStorageType_Type = StorageType
_MscVrIpTunnelStorageType_Object = MibTableColumn
mscVrIpTunnelStorageType = _MscVrIpTunnelStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 1, 1, 4),
    _MscVrIpTunnelStorageType_Type()
)
mscVrIpTunnelStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTunnelStorageType.setStatus("mandatory")
_MscVrIpTunnelIndex_Type = NonReplicated
_MscVrIpTunnelIndex_Object = MibTableColumn
mscVrIpTunnelIndex = _MscVrIpTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 1, 1, 10),
    _MscVrIpTunnelIndex_Type()
)
mscVrIpTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpTunnelIndex.setStatus("mandatory")
_MscVrIpTunnelSep_ObjectIdentity = ObjectIdentity
mscVrIpTunnelSep = _MscVrIpTunnelSep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 10)
)
_MscVrIpTunnelSepRowStatusTable_Object = MibTable
mscVrIpTunnelSepRowStatusTable = _MscVrIpTunnelSepRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 10, 1)
)
if mibBuilder.loadTexts:
    mscVrIpTunnelSepRowStatusTable.setStatus("mandatory")
_MscVrIpTunnelSepRowStatusEntry_Object = MibTableRow
mscVrIpTunnelSepRowStatusEntry = _MscVrIpTunnelSepRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 10, 1, 1)
)
mscVrIpTunnelSepRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTunnelIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTunnelSepIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpTunnelSepRowStatusEntry.setStatus("mandatory")
_MscVrIpTunnelSepRowStatus_Type = RowStatus
_MscVrIpTunnelSepRowStatus_Object = MibTableColumn
mscVrIpTunnelSepRowStatus = _MscVrIpTunnelSepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 10, 1, 1, 1),
    _MscVrIpTunnelSepRowStatus_Type()
)
mscVrIpTunnelSepRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpTunnelSepRowStatus.setStatus("mandatory")
_MscVrIpTunnelSepComponentName_Type = DisplayString
_MscVrIpTunnelSepComponentName_Object = MibTableColumn
mscVrIpTunnelSepComponentName = _MscVrIpTunnelSepComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 10, 1, 1, 2),
    _MscVrIpTunnelSepComponentName_Type()
)
mscVrIpTunnelSepComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTunnelSepComponentName.setStatus("mandatory")
_MscVrIpTunnelSepStorageType_Type = StorageType
_MscVrIpTunnelSepStorageType_Object = MibTableColumn
mscVrIpTunnelSepStorageType = _MscVrIpTunnelSepStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 10, 1, 1, 4),
    _MscVrIpTunnelSepStorageType_Type()
)
mscVrIpTunnelSepStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTunnelSepStorageType.setStatus("mandatory")


class _MscVrIpTunnelSepIndex_Type(Integer32):
    """Custom type mscVrIpTunnelSepIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_MscVrIpTunnelSepIndex_Type.__name__ = "Integer32"
_MscVrIpTunnelSepIndex_Object = MibTableColumn
mscVrIpTunnelSepIndex = _MscVrIpTunnelSepIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 10, 1, 1, 10),
    _MscVrIpTunnelSepIndex_Type()
)
mscVrIpTunnelSepIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpTunnelSepIndex.setStatus("mandatory")
_MscVrIpTunnelSepIfEntryTable_Object = MibTable
mscVrIpTunnelSepIfEntryTable = _MscVrIpTunnelSepIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 10, 10)
)
if mibBuilder.loadTexts:
    mscVrIpTunnelSepIfEntryTable.setStatus("mandatory")
_MscVrIpTunnelSepIfEntryEntry_Object = MibTableRow
mscVrIpTunnelSepIfEntryEntry = _MscVrIpTunnelSepIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 10, 10, 1)
)
mscVrIpTunnelSepIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTunnelIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTunnelSepIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpTunnelSepIfEntryEntry.setStatus("mandatory")


class _MscVrIpTunnelSepIfAdminStatus_Type(Integer32):
    """Custom type mscVrIpTunnelSepIfAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscVrIpTunnelSepIfAdminStatus_Type.__name__ = "Integer32"
_MscVrIpTunnelSepIfAdminStatus_Object = MibTableColumn
mscVrIpTunnelSepIfAdminStatus = _MscVrIpTunnelSepIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 10, 10, 1, 1),
    _MscVrIpTunnelSepIfAdminStatus_Type()
)
mscVrIpTunnelSepIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpTunnelSepIfAdminStatus.setStatus("mandatory")


class _MscVrIpTunnelSepIfIndex_Type(InterfaceIndex):
    """Custom type mscVrIpTunnelSepIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrIpTunnelSepIfIndex_Type.__name__ = "InterfaceIndex"
_MscVrIpTunnelSepIfIndex_Object = MibTableColumn
mscVrIpTunnelSepIfIndex = _MscVrIpTunnelSepIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 10, 10, 1, 2),
    _MscVrIpTunnelSepIfIndex_Type()
)
mscVrIpTunnelSepIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTunnelSepIfIndex.setStatus("mandatory")
_MscVrIpTunnelSepMpTable_Object = MibTable
mscVrIpTunnelSepMpTable = _MscVrIpTunnelSepMpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 10, 11)
)
if mibBuilder.loadTexts:
    mscVrIpTunnelSepMpTable.setStatus("mandatory")
_MscVrIpTunnelSepMpEntry_Object = MibTableRow
mscVrIpTunnelSepMpEntry = _MscVrIpTunnelSepMpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 10, 11, 1)
)
mscVrIpTunnelSepMpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTunnelIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTunnelSepIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpTunnelSepMpEntry.setStatus("mandatory")
_MscVrIpTunnelSepLinkToProtocolPort_Type = Link
_MscVrIpTunnelSepLinkToProtocolPort_Object = MibTableColumn
mscVrIpTunnelSepLinkToProtocolPort = _MscVrIpTunnelSepLinkToProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 10, 11, 1, 1),
    _MscVrIpTunnelSepLinkToProtocolPort_Type()
)
mscVrIpTunnelSepLinkToProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpTunnelSepLinkToProtocolPort.setStatus("mandatory")
_MscVrIpTunnelSepProvTable_Object = MibTable
mscVrIpTunnelSepProvTable = _MscVrIpTunnelSepProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 10, 12)
)
if mibBuilder.loadTexts:
    mscVrIpTunnelSepProvTable.setStatus("mandatory")
_MscVrIpTunnelSepProvEntry_Object = MibTableRow
mscVrIpTunnelSepProvEntry = _MscVrIpTunnelSepProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 10, 12, 1)
)
mscVrIpTunnelSepProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTunnelIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTunnelSepIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpTunnelSepProvEntry.setStatus("mandatory")


class _MscVrIpTunnelSepEncapType_Type(Integer32):
    """Custom type mscVrIpTunnelSepEncapType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("greIp", 1),
          ("ipInIp", 0))
    )


_MscVrIpTunnelSepEncapType_Type.__name__ = "Integer32"
_MscVrIpTunnelSepEncapType_Object = MibTableColumn
mscVrIpTunnelSepEncapType = _MscVrIpTunnelSepEncapType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 10, 12, 1, 1),
    _MscVrIpTunnelSepEncapType_Type()
)
mscVrIpTunnelSepEncapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpTunnelSepEncapType.setStatus("mandatory")


class _MscVrIpTunnelSepSourceAddress_Type(IpAddress):
    """Custom type mscVrIpTunnelSepSourceAddress based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrIpTunnelSepSourceAddress_Object = MibTableColumn
mscVrIpTunnelSepSourceAddress = _MscVrIpTunnelSepSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 10, 12, 1, 2),
    _MscVrIpTunnelSepSourceAddress_Type()
)
mscVrIpTunnelSepSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpTunnelSepSourceAddress.setStatus("mandatory")


class _MscVrIpTunnelSepDestinationAddress_Type(IpAddress):
    """Custom type mscVrIpTunnelSepDestinationAddress based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrIpTunnelSepDestinationAddress_Object = MibTableColumn
mscVrIpTunnelSepDestinationAddress = _MscVrIpTunnelSepDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 10, 12, 1, 3),
    _MscVrIpTunnelSepDestinationAddress_Type()
)
mscVrIpTunnelSepDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpTunnelSepDestinationAddress.setStatus("mandatory")
_MscVrIpTunnelSepOperTable_Object = MibTable
mscVrIpTunnelSepOperTable = _MscVrIpTunnelSepOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 10, 14)
)
if mibBuilder.loadTexts:
    mscVrIpTunnelSepOperTable.setStatus("mandatory")
_MscVrIpTunnelSepOperEntry_Object = MibTableRow
mscVrIpTunnelSepOperEntry = _MscVrIpTunnelSepOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 10, 14, 1)
)
mscVrIpTunnelSepOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTunnelIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTunnelSepIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpTunnelSepOperEntry.setStatus("mandatory")


class _MscVrIpTunnelSepDiscoveredPathMtu_Type(Unsigned32):
    """Custom type mscVrIpTunnelSepDiscoveredPathMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 18944),
    )


_MscVrIpTunnelSepDiscoveredPathMtu_Type.__name__ = "Unsigned32"
_MscVrIpTunnelSepDiscoveredPathMtu_Object = MibTableColumn
mscVrIpTunnelSepDiscoveredPathMtu = _MscVrIpTunnelSepDiscoveredPathMtu_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 10, 14, 1, 1),
    _MscVrIpTunnelSepDiscoveredPathMtu_Type()
)
mscVrIpTunnelSepDiscoveredPathMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTunnelSepDiscoveredPathMtu.setStatus("mandatory")
_MscVrIpTunnelMsep_ObjectIdentity = ObjectIdentity
mscVrIpTunnelMsep = _MscVrIpTunnelMsep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 11)
)
_MscVrIpTunnelMsepRowStatusTable_Object = MibTable
mscVrIpTunnelMsepRowStatusTable = _MscVrIpTunnelMsepRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 11, 1)
)
if mibBuilder.loadTexts:
    mscVrIpTunnelMsepRowStatusTable.setStatus("mandatory")
_MscVrIpTunnelMsepRowStatusEntry_Object = MibTableRow
mscVrIpTunnelMsepRowStatusEntry = _MscVrIpTunnelMsepRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 11, 1, 1)
)
mscVrIpTunnelMsepRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTunnelIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTunnelMsepIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpTunnelMsepRowStatusEntry.setStatus("mandatory")
_MscVrIpTunnelMsepRowStatus_Type = RowStatus
_MscVrIpTunnelMsepRowStatus_Object = MibTableColumn
mscVrIpTunnelMsepRowStatus = _MscVrIpTunnelMsepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 11, 1, 1, 1),
    _MscVrIpTunnelMsepRowStatus_Type()
)
mscVrIpTunnelMsepRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpTunnelMsepRowStatus.setStatus("mandatory")
_MscVrIpTunnelMsepComponentName_Type = DisplayString
_MscVrIpTunnelMsepComponentName_Object = MibTableColumn
mscVrIpTunnelMsepComponentName = _MscVrIpTunnelMsepComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 11, 1, 1, 2),
    _MscVrIpTunnelMsepComponentName_Type()
)
mscVrIpTunnelMsepComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTunnelMsepComponentName.setStatus("mandatory")
_MscVrIpTunnelMsepStorageType_Type = StorageType
_MscVrIpTunnelMsepStorageType_Object = MibTableColumn
mscVrIpTunnelMsepStorageType = _MscVrIpTunnelMsepStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 11, 1, 1, 4),
    _MscVrIpTunnelMsepStorageType_Type()
)
mscVrIpTunnelMsepStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTunnelMsepStorageType.setStatus("mandatory")


class _MscVrIpTunnelMsepIndex_Type(Integer32):
    """Custom type mscVrIpTunnelMsepIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_MscVrIpTunnelMsepIndex_Type.__name__ = "Integer32"
_MscVrIpTunnelMsepIndex_Object = MibTableColumn
mscVrIpTunnelMsepIndex = _MscVrIpTunnelMsepIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 11, 1, 1, 10),
    _MscVrIpTunnelMsepIndex_Type()
)
mscVrIpTunnelMsepIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpTunnelMsepIndex.setStatus("mandatory")
_MscVrIpTunnelMsepIfEntryTable_Object = MibTable
mscVrIpTunnelMsepIfEntryTable = _MscVrIpTunnelMsepIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 11, 10)
)
if mibBuilder.loadTexts:
    mscVrIpTunnelMsepIfEntryTable.setStatus("mandatory")
_MscVrIpTunnelMsepIfEntryEntry_Object = MibTableRow
mscVrIpTunnelMsepIfEntryEntry = _MscVrIpTunnelMsepIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 11, 10, 1)
)
mscVrIpTunnelMsepIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTunnelIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTunnelMsepIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpTunnelMsepIfEntryEntry.setStatus("mandatory")


class _MscVrIpTunnelMsepIfAdminStatus_Type(Integer32):
    """Custom type mscVrIpTunnelMsepIfAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscVrIpTunnelMsepIfAdminStatus_Type.__name__ = "Integer32"
_MscVrIpTunnelMsepIfAdminStatus_Object = MibTableColumn
mscVrIpTunnelMsepIfAdminStatus = _MscVrIpTunnelMsepIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 11, 10, 1, 1),
    _MscVrIpTunnelMsepIfAdminStatus_Type()
)
mscVrIpTunnelMsepIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpTunnelMsepIfAdminStatus.setStatus("mandatory")


class _MscVrIpTunnelMsepIfIndex_Type(InterfaceIndex):
    """Custom type mscVrIpTunnelMsepIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrIpTunnelMsepIfIndex_Type.__name__ = "InterfaceIndex"
_MscVrIpTunnelMsepIfIndex_Object = MibTableColumn
mscVrIpTunnelMsepIfIndex = _MscVrIpTunnelMsepIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 11, 10, 1, 2),
    _MscVrIpTunnelMsepIfIndex_Type()
)
mscVrIpTunnelMsepIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTunnelMsepIfIndex.setStatus("mandatory")
_MscVrIpTunnelMsepMpTable_Object = MibTable
mscVrIpTunnelMsepMpTable = _MscVrIpTunnelMsepMpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 11, 11)
)
if mibBuilder.loadTexts:
    mscVrIpTunnelMsepMpTable.setStatus("mandatory")
_MscVrIpTunnelMsepMpEntry_Object = MibTableRow
mscVrIpTunnelMsepMpEntry = _MscVrIpTunnelMsepMpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 11, 11, 1)
)
mscVrIpTunnelMsepMpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTunnelIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTunnelMsepIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpTunnelMsepMpEntry.setStatus("mandatory")
_MscVrIpTunnelMsepLinkToProtocolPort_Type = Link
_MscVrIpTunnelMsepLinkToProtocolPort_Object = MibTableColumn
mscVrIpTunnelMsepLinkToProtocolPort = _MscVrIpTunnelMsepLinkToProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 11, 11, 1, 1),
    _MscVrIpTunnelMsepLinkToProtocolPort_Type()
)
mscVrIpTunnelMsepLinkToProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpTunnelMsepLinkToProtocolPort.setStatus("mandatory")
_MscVrIpTunnelMsepProvTable_Object = MibTable
mscVrIpTunnelMsepProvTable = _MscVrIpTunnelMsepProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 11, 12)
)
if mibBuilder.loadTexts:
    mscVrIpTunnelMsepProvTable.setStatus("mandatory")
_MscVrIpTunnelMsepProvEntry_Object = MibTableRow
mscVrIpTunnelMsepProvEntry = _MscVrIpTunnelMsepProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 11, 12, 1)
)
mscVrIpTunnelMsepProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTunnelIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTunnelMsepIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpTunnelMsepProvEntry.setStatus("mandatory")


class _MscVrIpTunnelMsepPathMtu_Type(Unsigned32):
    """Custom type mscVrIpTunnelMsepPathMtu based on Unsigned32"""
    defaultValue = 1604

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(576, 18944),
    )


_MscVrIpTunnelMsepPathMtu_Type.__name__ = "Unsigned32"
_MscVrIpTunnelMsepPathMtu_Object = MibTableColumn
mscVrIpTunnelMsepPathMtu = _MscVrIpTunnelMsepPathMtu_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 11, 12, 1, 1),
    _MscVrIpTunnelMsepPathMtu_Type()
)
mscVrIpTunnelMsepPathMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpTunnelMsepPathMtu.setStatus("mandatory")


class _MscVrIpTunnelMsepEncapType_Type(Integer32):
    """Custom type mscVrIpTunnelMsepEncapType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("ipInIp", 0)
    )


_MscVrIpTunnelMsepEncapType_Type.__name__ = "Integer32"
_MscVrIpTunnelMsepEncapType_Object = MibTableColumn
mscVrIpTunnelMsepEncapType = _MscVrIpTunnelMsepEncapType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 11, 12, 1, 2),
    _MscVrIpTunnelMsepEncapType_Type()
)
mscVrIpTunnelMsepEncapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpTunnelMsepEncapType.setStatus("mandatory")
_MscVrIpTunnelMsepSharedDomainVirtualRouter_Type = RowPointer
_MscVrIpTunnelMsepSharedDomainVirtualRouter_Object = MibTableColumn
mscVrIpTunnelMsepSharedDomainVirtualRouter = _MscVrIpTunnelMsepSharedDomainVirtualRouter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 11, 12, 1, 3),
    _MscVrIpTunnelMsepSharedDomainVirtualRouter_Type()
)
mscVrIpTunnelMsepSharedDomainVirtualRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpTunnelMsepSharedDomainVirtualRouter.setStatus("mandatory")


class _MscVrIpTunnelMsepSourceAddress_Type(IpAddress):
    """Custom type mscVrIpTunnelMsepSourceAddress based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrIpTunnelMsepSourceAddress_Object = MibTableColumn
mscVrIpTunnelMsepSourceAddress = _MscVrIpTunnelMsepSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 11, 12, 1, 4),
    _MscVrIpTunnelMsepSourceAddress_Type()
)
mscVrIpTunnelMsepSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpTunnelMsepSourceAddress.setStatus("mandatory")
_MscVrIpTunnelMsepDstTable_Object = MibTable
mscVrIpTunnelMsepDstTable = _MscVrIpTunnelMsepDstTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 11, 834)
)
if mibBuilder.loadTexts:
    mscVrIpTunnelMsepDstTable.setStatus("mandatory")
_MscVrIpTunnelMsepDstEntry_Object = MibTableRow
mscVrIpTunnelMsepDstEntry = _MscVrIpTunnelMsepDstEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 11, 834, 1)
)
mscVrIpTunnelMsepDstEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTunnelIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTunnelMsepIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTunnelMsepDstValue"),
)
if mibBuilder.loadTexts:
    mscVrIpTunnelMsepDstEntry.setStatus("mandatory")
_MscVrIpTunnelMsepDstValue_Type = IpAddress
_MscVrIpTunnelMsepDstValue_Object = MibTableColumn
mscVrIpTunnelMsepDstValue = _MscVrIpTunnelMsepDstValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 11, 834, 1, 1),
    _MscVrIpTunnelMsepDstValue_Type()
)
mscVrIpTunnelMsepDstValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpTunnelMsepDstValue.setStatus("mandatory")
_MscVrIpTunnelMsepDstRowStatus_Type = RowStatus
_MscVrIpTunnelMsepDstRowStatus_Object = MibTableColumn
mscVrIpTunnelMsepDstRowStatus = _MscVrIpTunnelMsepDstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 11, 834, 1, 2),
    _MscVrIpTunnelMsepDstRowStatus_Type()
)
mscVrIpTunnelMsepDstRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscVrIpTunnelMsepDstRowStatus.setStatus("mandatory")
_MscVrIpTunnelStateTable_Object = MibTable
mscVrIpTunnelStateTable = _MscVrIpTunnelStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 12)
)
if mibBuilder.loadTexts:
    mscVrIpTunnelStateTable.setStatus("mandatory")
_MscVrIpTunnelStateEntry_Object = MibTableRow
mscVrIpTunnelStateEntry = _MscVrIpTunnelStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 12, 1)
)
mscVrIpTunnelStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpTunnelIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpTunnelStateEntry.setStatus("mandatory")


class _MscVrIpTunnelAdminState_Type(Integer32):
    """Custom type mscVrIpTunnelAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_MscVrIpTunnelAdminState_Type.__name__ = "Integer32"
_MscVrIpTunnelAdminState_Object = MibTableColumn
mscVrIpTunnelAdminState = _MscVrIpTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 12, 1, 1),
    _MscVrIpTunnelAdminState_Type()
)
mscVrIpTunnelAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTunnelAdminState.setStatus("mandatory")


class _MscVrIpTunnelOperationalState_Type(Integer32):
    """Custom type mscVrIpTunnelOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MscVrIpTunnelOperationalState_Type.__name__ = "Integer32"
_MscVrIpTunnelOperationalState_Object = MibTableColumn
mscVrIpTunnelOperationalState = _MscVrIpTunnelOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 12, 1, 2),
    _MscVrIpTunnelOperationalState_Type()
)
mscVrIpTunnelOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTunnelOperationalState.setStatus("mandatory")


class _MscVrIpTunnelUsageState_Type(Integer32):
    """Custom type mscVrIpTunnelUsageState based on Integer32"""
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
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_MscVrIpTunnelUsageState_Type.__name__ = "Integer32"
_MscVrIpTunnelUsageState_Object = MibTableColumn
mscVrIpTunnelUsageState = _MscVrIpTunnelUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 18, 12, 1, 3),
    _MscVrIpTunnelUsageState_Type()
)
mscVrIpTunnelUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpTunnelUsageState.setStatus("mandatory")
_MscVrIpProvTable_Object = MibTable
mscVrIpProvTable = _MscVrIpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 100)
)
if mibBuilder.loadTexts:
    mscVrIpProvTable.setStatus("mandatory")
_MscVrIpProvEntry_Object = MibTableRow
mscVrIpProvEntry = _MscVrIpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 100, 1)
)
mscVrIpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpProvEntry.setStatus("mandatory")


class _MscVrIpForwarding_Type(Integer32):
    """Custom type mscVrIpForwarding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("gateway", 1)
    )


_MscVrIpForwarding_Type.__name__ = "Integer32"
_MscVrIpForwarding_Object = MibTableColumn
mscVrIpForwarding = _MscVrIpForwarding_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 100, 1, 2),
    _MscVrIpForwarding_Type()
)
mscVrIpForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpForwarding.setStatus("mandatory")


class _MscVrIpDefaultTtl_Type(Unsigned32):
    """Custom type mscVrIpDefaultTtl based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(255, 255),
    )


_MscVrIpDefaultTtl_Type.__name__ = "Unsigned32"
_MscVrIpDefaultTtl_Object = MibTableColumn
mscVrIpDefaultTtl = _MscVrIpDefaultTtl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 100, 1, 3),
    _MscVrIpDefaultTtl_Type()
)
mscVrIpDefaultTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpDefaultTtl.setStatus("mandatory")
_MscVrIpCosPolicyAssignment_Type = Link
_MscVrIpCosPolicyAssignment_Object = MibTableColumn
mscVrIpCosPolicyAssignment = _MscVrIpCosPolicyAssignment_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 100, 1, 4),
    _MscVrIpCosPolicyAssignment_Type()
)
mscVrIpCosPolicyAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpCosPolicyAssignment.setStatus("mandatory")
_MscVrIpStatsTable_Object = MibTable
mscVrIpStatsTable = _MscVrIpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 101)
)
if mibBuilder.loadTexts:
    mscVrIpStatsTable.setStatus("mandatory")
_MscVrIpStatsEntry_Object = MibTableRow
mscVrIpStatsEntry = _MscVrIpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 101, 1)
)
mscVrIpStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpStatsEntry.setStatus("mandatory")
_MscVrIpInReceives_Type = Counter32
_MscVrIpInReceives_Object = MibTableColumn
mscVrIpInReceives = _MscVrIpInReceives_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 101, 1, 1),
    _MscVrIpInReceives_Type()
)
mscVrIpInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpInReceives.setStatus("mandatory")
_MscVrIpInHdrErrors_Type = Counter32
_MscVrIpInHdrErrors_Object = MibTableColumn
mscVrIpInHdrErrors = _MscVrIpInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 101, 1, 2),
    _MscVrIpInHdrErrors_Type()
)
mscVrIpInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpInHdrErrors.setStatus("mandatory")
_MscVrIpInAddrErrors_Type = Counter32
_MscVrIpInAddrErrors_Object = MibTableColumn
mscVrIpInAddrErrors = _MscVrIpInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 101, 1, 3),
    _MscVrIpInAddrErrors_Type()
)
mscVrIpInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpInAddrErrors.setStatus("mandatory")
_MscVrIpForwDatagrams_Type = Counter32
_MscVrIpForwDatagrams_Object = MibTableColumn
mscVrIpForwDatagrams = _MscVrIpForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 101, 1, 4),
    _MscVrIpForwDatagrams_Type()
)
mscVrIpForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpForwDatagrams.setStatus("mandatory")
_MscVrIpInUnknownProtos_Type = Counter32
_MscVrIpInUnknownProtos_Object = MibTableColumn
mscVrIpInUnknownProtos = _MscVrIpInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 101, 1, 5),
    _MscVrIpInUnknownProtos_Type()
)
mscVrIpInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpInUnknownProtos.setStatus("mandatory")
_MscVrIpInDiscards_Type = Counter32
_MscVrIpInDiscards_Object = MibTableColumn
mscVrIpInDiscards = _MscVrIpInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 101, 1, 6),
    _MscVrIpInDiscards_Type()
)
mscVrIpInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpInDiscards.setStatus("mandatory")
_MscVrIpInDelivers_Type = Counter32
_MscVrIpInDelivers_Object = MibTableColumn
mscVrIpInDelivers = _MscVrIpInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 101, 1, 7),
    _MscVrIpInDelivers_Type()
)
mscVrIpInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpInDelivers.setStatus("mandatory")
_MscVrIpOutRequests_Type = Counter32
_MscVrIpOutRequests_Object = MibTableColumn
mscVrIpOutRequests = _MscVrIpOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 101, 1, 8),
    _MscVrIpOutRequests_Type()
)
mscVrIpOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOutRequests.setStatus("mandatory")
_MscVrIpOutDiscards_Type = Counter32
_MscVrIpOutDiscards_Object = MibTableColumn
mscVrIpOutDiscards = _MscVrIpOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 101, 1, 9),
    _MscVrIpOutDiscards_Type()
)
mscVrIpOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOutDiscards.setStatus("mandatory")
_MscVrIpOutNoRoutes_Type = Counter32
_MscVrIpOutNoRoutes_Object = MibTableColumn
mscVrIpOutNoRoutes = _MscVrIpOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 101, 1, 10),
    _MscVrIpOutNoRoutes_Type()
)
mscVrIpOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOutNoRoutes.setStatus("mandatory")


class _MscVrIpReasmTimeOut_Type(Unsigned32):
    """Custom type mscVrIpReasmTimeOut based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_MscVrIpReasmTimeOut_Type.__name__ = "Unsigned32"
_MscVrIpReasmTimeOut_Object = MibTableColumn
mscVrIpReasmTimeOut = _MscVrIpReasmTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 101, 1, 11),
    _MscVrIpReasmTimeOut_Type()
)
mscVrIpReasmTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpReasmTimeOut.setStatus("mandatory")
_MscVrIpReasmReqds_Type = Counter32
_MscVrIpReasmReqds_Object = MibTableColumn
mscVrIpReasmReqds = _MscVrIpReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 101, 1, 12),
    _MscVrIpReasmReqds_Type()
)
mscVrIpReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpReasmReqds.setStatus("mandatory")
_MscVrIpReasmOks_Type = Counter32
_MscVrIpReasmOks_Object = MibTableColumn
mscVrIpReasmOks = _MscVrIpReasmOks_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 101, 1, 13),
    _MscVrIpReasmOks_Type()
)
mscVrIpReasmOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpReasmOks.setStatus("mandatory")
_MscVrIpReasmFails_Type = Counter32
_MscVrIpReasmFails_Object = MibTableColumn
mscVrIpReasmFails = _MscVrIpReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 101, 1, 14),
    _MscVrIpReasmFails_Type()
)
mscVrIpReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpReasmFails.setStatus("mandatory")
_MscVrIpFragOks_Type = Counter32
_MscVrIpFragOks_Object = MibTableColumn
mscVrIpFragOks = _MscVrIpFragOks_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 101, 1, 15),
    _MscVrIpFragOks_Type()
)
mscVrIpFragOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpFragOks.setStatus("mandatory")
_MscVrIpFragFails_Type = Counter32
_MscVrIpFragFails_Object = MibTableColumn
mscVrIpFragFails = _MscVrIpFragFails_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 101, 1, 16),
    _MscVrIpFragFails_Type()
)
mscVrIpFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpFragFails.setStatus("mandatory")
_MscVrIpFragCreates_Type = Counter32
_MscVrIpFragCreates_Object = MibTableColumn
mscVrIpFragCreates = _MscVrIpFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 101, 1, 17),
    _MscVrIpFragCreates_Type()
)
mscVrIpFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpFragCreates.setStatus("mandatory")
_MscVrIpRoutingDiscards_Type = Counter32
_MscVrIpRoutingDiscards_Object = MibTableColumn
mscVrIpRoutingDiscards = _MscVrIpRoutingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 101, 1, 18),
    _MscVrIpRoutingDiscards_Type()
)
mscVrIpRoutingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpRoutingDiscards.setStatus("mandatory")
_MscVrIpAdminControlTable_Object = MibTable
mscVrIpAdminControlTable = _MscVrIpAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 102)
)
if mibBuilder.loadTexts:
    mscVrIpAdminControlTable.setStatus("mandatory")
_MscVrIpAdminControlEntry_Object = MibTableRow
mscVrIpAdminControlEntry = _MscVrIpAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 102, 1)
)
mscVrIpAdminControlEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpAdminControlEntry.setStatus("mandatory")


class _MscVrIpSnmpAdminStatus_Type(Integer32):
    """Custom type mscVrIpSnmpAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscVrIpSnmpAdminStatus_Type.__name__ = "Integer32"
_MscVrIpSnmpAdminStatus_Object = MibTableColumn
mscVrIpSnmpAdminStatus = _MscVrIpSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 102, 1, 1),
    _MscVrIpSnmpAdminStatus_Type()
)
mscVrIpSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpSnmpAdminStatus.setStatus("mandatory")
_MscVrIpStateTable_Object = MibTable
mscVrIpStateTable = _MscVrIpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 104)
)
if mibBuilder.loadTexts:
    mscVrIpStateTable.setStatus("mandatory")
_MscVrIpStateEntry_Object = MibTableRow
mscVrIpStateEntry = _MscVrIpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 104, 1)
)
mscVrIpStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpStateEntry.setStatus("mandatory")


class _MscVrIpAdminState_Type(Integer32):
    """Custom type mscVrIpAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_MscVrIpAdminState_Type.__name__ = "Integer32"
_MscVrIpAdminState_Object = MibTableColumn
mscVrIpAdminState = _MscVrIpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 104, 1, 1),
    _MscVrIpAdminState_Type()
)
mscVrIpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpAdminState.setStatus("mandatory")


class _MscVrIpOperationalState_Type(Integer32):
    """Custom type mscVrIpOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MscVrIpOperationalState_Type.__name__ = "Integer32"
_MscVrIpOperationalState_Object = MibTableColumn
mscVrIpOperationalState = _MscVrIpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 104, 1, 2),
    _MscVrIpOperationalState_Type()
)
mscVrIpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpOperationalState.setStatus("mandatory")


class _MscVrIpUsageState_Type(Integer32):
    """Custom type mscVrIpUsageState based on Integer32"""
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
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_MscVrIpUsageState_Type.__name__ = "Integer32"
_MscVrIpUsageState_Object = MibTableColumn
mscVrIpUsageState = _MscVrIpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 104, 1, 3),
    _MscVrIpUsageState_Type()
)
mscVrIpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpUsageState.setStatus("mandatory")
_MscVrIpOperStatusTable_Object = MibTable
mscVrIpOperStatusTable = _MscVrIpOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 107)
)
if mibBuilder.loadTexts:
    mscVrIpOperStatusTable.setStatus("mandatory")
_MscVrIpOperStatusEntry_Object = MibTableRow
mscVrIpOperStatusEntry = _MscVrIpOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 107, 1)
)
mscVrIpOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpOperStatusEntry.setStatus("mandatory")


class _MscVrIpSnmpOperStatus_Type(Integer32):
    """Custom type mscVrIpSnmpOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscVrIpSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrIpSnmpOperStatus_Object = MibTableColumn
mscVrIpSnmpOperStatus = _MscVrIpSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 107, 1, 1),
    _MscVrIpSnmpOperStatus_Type()
)
mscVrIpSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpSnmpOperStatus.setStatus("mandatory")
_MscVrIpCtsTable_Object = MibTable
mscVrIpCtsTable = _MscVrIpCtsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 394)
)
if mibBuilder.loadTexts:
    mscVrIpCtsTable.setStatus("mandatory")
_MscVrIpCtsEntry_Object = MibTableRow
mscVrIpCtsEntry = _MscVrIpCtsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 394, 1)
)
mscVrIpCtsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpCtsIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpCtsEntry.setStatus("mandatory")


class _MscVrIpCtsIndex_Type(Integer32):
    """Custom type mscVrIpCtsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscVrIpCtsIndex_Type.__name__ = "Integer32"
_MscVrIpCtsIndex_Object = MibTableColumn
mscVrIpCtsIndex = _MscVrIpCtsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 394, 1, 1),
    _MscVrIpCtsIndex_Type()
)
mscVrIpCtsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpCtsIndex.setStatus("mandatory")


class _MscVrIpCtsValue_Type(Unsigned32):
    """Custom type mscVrIpCtsValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 8000),
    )


_MscVrIpCtsValue_Type.__name__ = "Unsigned32"
_MscVrIpCtsValue_Object = MibTableColumn
mscVrIpCtsValue = _MscVrIpCtsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 394, 1, 2),
    _MscVrIpCtsValue_Type()
)
mscVrIpCtsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpCtsValue.setStatus("mandatory")
_IpMIB_ObjectIdentity = ObjectIdentity
ipMIB = _IpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 27)
)
_IpGroup_ObjectIdentity = ObjectIdentity
ipGroup = _IpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 27, 1)
)
_IpGroupCA_ObjectIdentity = ObjectIdentity
ipGroupCA = _IpGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 27, 1, 1)
)
_IpGroupCA02_ObjectIdentity = ObjectIdentity
ipGroupCA02 = _IpGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 27, 1, 1, 3)
)
_IpGroupCA02A_ObjectIdentity = ObjectIdentity
ipGroupCA02A = _IpGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 27, 1, 1, 3, 2)
)
_IpCapabilities_ObjectIdentity = ObjectIdentity
ipCapabilities = _IpCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 27, 3)
)
_IpCapabilitiesCA_ObjectIdentity = ObjectIdentity
ipCapabilitiesCA = _IpCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 27, 3, 1)
)
_IpCapabilitiesCA02_ObjectIdentity = ObjectIdentity
ipCapabilitiesCA02 = _IpCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 27, 3, 1, 3)
)
_IpCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
ipCapabilitiesCA02A = _IpCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 27, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-IpMIB",
    **{"mscVrPpIpPort": mscVrPpIpPort,
       "mscVrPpIpPortRowStatusTable": mscVrPpIpPortRowStatusTable,
       "mscVrPpIpPortRowStatusEntry": mscVrPpIpPortRowStatusEntry,
       "mscVrPpIpPortRowStatus": mscVrPpIpPortRowStatus,
       "mscVrPpIpPortComponentName": mscVrPpIpPortComponentName,
       "mscVrPpIpPortStorageType": mscVrPpIpPortStorageType,
       "mscVrPpIpPortIndex": mscVrPpIpPortIndex,
       "mscVrPpIpPortLogicalIf": mscVrPpIpPortLogicalIf,
       "mscVrPpIpPortLogicalIfRowStatusTable": mscVrPpIpPortLogicalIfRowStatusTable,
       "mscVrPpIpPortLogicalIfRowStatusEntry": mscVrPpIpPortLogicalIfRowStatusEntry,
       "mscVrPpIpPortLogicalIfRowStatus": mscVrPpIpPortLogicalIfRowStatus,
       "mscVrPpIpPortLogicalIfComponentName": mscVrPpIpPortLogicalIfComponentName,
       "mscVrPpIpPortLogicalIfStorageType": mscVrPpIpPortLogicalIfStorageType,
       "mscVrPpIpPortLogicalIfAddressIndex": mscVrPpIpPortLogicalIfAddressIndex,
       "mscVrPpIpPortLogicalIfOspfIf": mscVrPpIpPortLogicalIfOspfIf,
       "mscVrPpIpPortLogicalIfOspfIfRowStatusTable": mscVrPpIpPortLogicalIfOspfIfRowStatusTable,
       "mscVrPpIpPortLogicalIfOspfIfRowStatusEntry": mscVrPpIpPortLogicalIfOspfIfRowStatusEntry,
       "mscVrPpIpPortLogicalIfOspfIfRowStatus": mscVrPpIpPortLogicalIfOspfIfRowStatus,
       "mscVrPpIpPortLogicalIfOspfIfComponentName": mscVrPpIpPortLogicalIfOspfIfComponentName,
       "mscVrPpIpPortLogicalIfOspfIfStorageType": mscVrPpIpPortLogicalIfOspfIfStorageType,
       "mscVrPpIpPortLogicalIfOspfIfIndex": mscVrPpIpPortLogicalIfOspfIfIndex,
       "mscVrPpIpPortLogicalIfOspfIfTOS": mscVrPpIpPortLogicalIfOspfIfTOS,
       "mscVrPpIpPortLogicalIfOspfIfTOSRowStatusTable": mscVrPpIpPortLogicalIfOspfIfTOSRowStatusTable,
       "mscVrPpIpPortLogicalIfOspfIfTOSRowStatusEntry": mscVrPpIpPortLogicalIfOspfIfTOSRowStatusEntry,
       "mscVrPpIpPortLogicalIfOspfIfTOSRowStatus": mscVrPpIpPortLogicalIfOspfIfTOSRowStatus,
       "mscVrPpIpPortLogicalIfOspfIfTOSComponentName": mscVrPpIpPortLogicalIfOspfIfTOSComponentName,
       "mscVrPpIpPortLogicalIfOspfIfTOSStorageType": mscVrPpIpPortLogicalIfOspfIfTOSStorageType,
       "mscVrPpIpPortLogicalIfOspfIfTOSMetricTosIndex": mscVrPpIpPortLogicalIfOspfIfTOSMetricTosIndex,
       "mscVrPpIpPortLogicalIfOspfIfTOSProvTable": mscVrPpIpPortLogicalIfOspfIfTOSProvTable,
       "mscVrPpIpPortLogicalIfOspfIfTOSProvEntry": mscVrPpIpPortLogicalIfOspfIfTOSProvEntry,
       "mscVrPpIpPortLogicalIfOspfIfTOSTosMetric": mscVrPpIpPortLogicalIfOspfIfTOSTosMetric,
       "mscVrPpIpPortLogicalIfOspfIfNbr": mscVrPpIpPortLogicalIfOspfIfNbr,
       "mscVrPpIpPortLogicalIfOspfIfNbrRowStatusTable": mscVrPpIpPortLogicalIfOspfIfNbrRowStatusTable,
       "mscVrPpIpPortLogicalIfOspfIfNbrRowStatusEntry": mscVrPpIpPortLogicalIfOspfIfNbrRowStatusEntry,
       "mscVrPpIpPortLogicalIfOspfIfNbrRowStatus": mscVrPpIpPortLogicalIfOspfIfNbrRowStatus,
       "mscVrPpIpPortLogicalIfOspfIfNbrComponentName": mscVrPpIpPortLogicalIfOspfIfNbrComponentName,
       "mscVrPpIpPortLogicalIfOspfIfNbrStorageType": mscVrPpIpPortLogicalIfOspfIfNbrStorageType,
       "mscVrPpIpPortLogicalIfOspfIfNbrAddressIndex": mscVrPpIpPortLogicalIfOspfIfNbrAddressIndex,
       "mscVrPpIpPortLogicalIfOspfIfNbrProvTable": mscVrPpIpPortLogicalIfOspfIfNbrProvTable,
       "mscVrPpIpPortLogicalIfOspfIfNbrProvEntry": mscVrPpIpPortLogicalIfOspfIfNbrProvEntry,
       "mscVrPpIpPortLogicalIfOspfIfNbrPriority": mscVrPpIpPortLogicalIfOspfIfNbrPriority,
       "mscVrPpIpPortLogicalIfOspfIfNbrOperTable": mscVrPpIpPortLogicalIfOspfIfNbrOperTable,
       "mscVrPpIpPortLogicalIfOspfIfNbrOperEntry": mscVrPpIpPortLogicalIfOspfIfNbrOperEntry,
       "mscVrPpIpPortLogicalIfOspfIfNbrRtrId": mscVrPpIpPortLogicalIfOspfIfNbrRtrId,
       "mscVrPpIpPortLogicalIfOspfIfNbrOptions": mscVrPpIpPortLogicalIfOspfIfNbrOptions,
       "mscVrPpIpPortLogicalIfOspfIfNbrState": mscVrPpIpPortLogicalIfOspfIfNbrState,
       "mscVrPpIpPortLogicalIfOspfIfNbrEvents": mscVrPpIpPortLogicalIfOspfIfNbrEvents,
       "mscVrPpIpPortLogicalIfOspfIfNbrLsRetransQlen": mscVrPpIpPortLogicalIfOspfIfNbrLsRetransQlen,
       "mscVrPpIpPortLogicalIfOspfIfNbrExchangeStatus": mscVrPpIpPortLogicalIfOspfIfNbrExchangeStatus,
       "mscVrPpIpPortLogicalIfOspfIfNbrPermanance": mscVrPpIpPortLogicalIfOspfIfNbrPermanance,
       "mscVrPpIpPortLogicalIfOspfIfProvTable": mscVrPpIpPortLogicalIfOspfIfProvTable,
       "mscVrPpIpPortLogicalIfOspfIfProvEntry": mscVrPpIpPortLogicalIfOspfIfProvEntry,
       "mscVrPpIpPortLogicalIfOspfIfAreaId": mscVrPpIpPortLogicalIfOspfIfAreaId,
       "mscVrPpIpPortLogicalIfOspfIfIfType": mscVrPpIpPortLogicalIfOspfIfIfType,
       "mscVrPpIpPortLogicalIfOspfIfSnmpAdminStatus": mscVrPpIpPortLogicalIfOspfIfSnmpAdminStatus,
       "mscVrPpIpPortLogicalIfOspfIfRtrPriority": mscVrPpIpPortLogicalIfOspfIfRtrPriority,
       "mscVrPpIpPortLogicalIfOspfIfTransitDelay": mscVrPpIpPortLogicalIfOspfIfTransitDelay,
       "mscVrPpIpPortLogicalIfOspfIfRetransInterval": mscVrPpIpPortLogicalIfOspfIfRetransInterval,
       "mscVrPpIpPortLogicalIfOspfIfHelloInterval": mscVrPpIpPortLogicalIfOspfIfHelloInterval,
       "mscVrPpIpPortLogicalIfOspfIfRtrDeadInterval": mscVrPpIpPortLogicalIfOspfIfRtrDeadInterval,
       "mscVrPpIpPortLogicalIfOspfIfPollInterval": mscVrPpIpPortLogicalIfOspfIfPollInterval,
       "mscVrPpIpPortLogicalIfOspfIfAuthKey": mscVrPpIpPortLogicalIfOspfIfAuthKey,
       "mscVrPpIpPortLogicalIfOspfIfMulticastForwarding": mscVrPpIpPortLogicalIfOspfIfMulticastForwarding,
       "mscVrPpIpPortLogicalIfOspfIfOperTable": mscVrPpIpPortLogicalIfOspfIfOperTable,
       "mscVrPpIpPortLogicalIfOspfIfOperEntry": mscVrPpIpPortLogicalIfOspfIfOperEntry,
       "mscVrPpIpPortLogicalIfOspfIfState": mscVrPpIpPortLogicalIfOspfIfState,
       "mscVrPpIpPortLogicalIfOspfIfDesignatedRouter": mscVrPpIpPortLogicalIfOspfIfDesignatedRouter,
       "mscVrPpIpPortLogicalIfOspfIfBackupDesignatedRouter": mscVrPpIpPortLogicalIfOspfIfBackupDesignatedRouter,
       "mscVrPpIpPortLogicalIfOspfIfEvents": mscVrPpIpPortLogicalIfOspfIfEvents,
       "mscVrPpIpPortLogicalIfOspfIfMetricTable": mscVrPpIpPortLogicalIfOspfIfMetricTable,
       "mscVrPpIpPortLogicalIfOspfIfMetricEntry": mscVrPpIpPortLogicalIfOspfIfMetricEntry,
       "mscVrPpIpPortLogicalIfOspfIfMetric": mscVrPpIpPortLogicalIfOspfIfMetric,
       "mscVrPpIpPortLogicalIfRipIf": mscVrPpIpPortLogicalIfRipIf,
       "mscVrPpIpPortLogicalIfRipIfRowStatusTable": mscVrPpIpPortLogicalIfRipIfRowStatusTable,
       "mscVrPpIpPortLogicalIfRipIfRowStatusEntry": mscVrPpIpPortLogicalIfRipIfRowStatusEntry,
       "mscVrPpIpPortLogicalIfRipIfRowStatus": mscVrPpIpPortLogicalIfRipIfRowStatus,
       "mscVrPpIpPortLogicalIfRipIfComponentName": mscVrPpIpPortLogicalIfRipIfComponentName,
       "mscVrPpIpPortLogicalIfRipIfStorageType": mscVrPpIpPortLogicalIfRipIfStorageType,
       "mscVrPpIpPortLogicalIfRipIfIndex": mscVrPpIpPortLogicalIfRipIfIndex,
       "mscVrPpIpPortLogicalIfRipIfNbr": mscVrPpIpPortLogicalIfRipIfNbr,
       "mscVrPpIpPortLogicalIfRipIfNbrRowStatusTable": mscVrPpIpPortLogicalIfRipIfNbrRowStatusTable,
       "mscVrPpIpPortLogicalIfRipIfNbrRowStatusEntry": mscVrPpIpPortLogicalIfRipIfNbrRowStatusEntry,
       "mscVrPpIpPortLogicalIfRipIfNbrRowStatus": mscVrPpIpPortLogicalIfRipIfNbrRowStatus,
       "mscVrPpIpPortLogicalIfRipIfNbrComponentName": mscVrPpIpPortLogicalIfRipIfNbrComponentName,
       "mscVrPpIpPortLogicalIfRipIfNbrStorageType": mscVrPpIpPortLogicalIfRipIfNbrStorageType,
       "mscVrPpIpPortLogicalIfRipIfNbrIndex": mscVrPpIpPortLogicalIfRipIfNbrIndex,
       "mscVrPpIpPortLogicalIfRipIfProvTable": mscVrPpIpPortLogicalIfRipIfProvTable,
       "mscVrPpIpPortLogicalIfRipIfProvEntry": mscVrPpIpPortLogicalIfRipIfProvEntry,
       "mscVrPpIpPortLogicalIfRipIfSnmpAdminStatus": mscVrPpIpPortLogicalIfRipIfSnmpAdminStatus,
       "mscVrPpIpPortLogicalIfRipIfMetric": mscVrPpIpPortLogicalIfRipIfMetric,
       "mscVrPpIpPortLogicalIfRipIfSilentFlag": mscVrPpIpPortLogicalIfRipIfSilentFlag,
       "mscVrPpIpPortLogicalIfRipIfPoisonReverseFlag": mscVrPpIpPortLogicalIfRipIfPoisonReverseFlag,
       "mscVrPpIpPortLogicalIfRipIfFlashUpdateFlag": mscVrPpIpPortLogicalIfRipIfFlashUpdateFlag,
       "mscVrPpIpPortLogicalIfRipIfNetworkRouteStatus": mscVrPpIpPortLogicalIfRipIfNetworkRouteStatus,
       "mscVrPpIpPortLogicalIfRipIfDefaultRouteMetric": mscVrPpIpPortLogicalIfRipIfDefaultRouteMetric,
       "mscVrPpIpPortLogicalIfRipIfAcceptDefault": mscVrPpIpPortLogicalIfRipIfAcceptDefault,
       "mscVrPpIpPortLogicalIfRipIfIfConfSend": mscVrPpIpPortLogicalIfRipIfIfConfSend,
       "mscVrPpIpPortLogicalIfRipIfIfConfReceive": mscVrPpIpPortLogicalIfRipIfIfConfReceive,
       "mscVrPpIpPortLogicalIfRipIfStatTable": mscVrPpIpPortLogicalIfRipIfStatTable,
       "mscVrPpIpPortLogicalIfRipIfStatEntry": mscVrPpIpPortLogicalIfRipIfStatEntry,
       "mscVrPpIpPortLogicalIfRipIfIfBadPacketRcv": mscVrPpIpPortLogicalIfRipIfIfBadPacketRcv,
       "mscVrPpIpPortLogicalIfRipIfIfBadRouteRcv": mscVrPpIpPortLogicalIfRipIfIfBadRouteRcv,
       "mscVrPpIpPortLogicalIfRipIfIfTriggeredUpdates": mscVrPpIpPortLogicalIfRipIfIfTriggeredUpdates,
       "mscVrPpIpPortLogicalIfProvTable": mscVrPpIpPortLogicalIfProvTable,
       "mscVrPpIpPortLogicalIfProvEntry": mscVrPpIpPortLogicalIfProvEntry,
       "mscVrPpIpPortLogicalIfNetMask": mscVrPpIpPortLogicalIfNetMask,
       "mscVrPpIpPortLogicalIfBroadcastAddress": mscVrPpIpPortLogicalIfBroadcastAddress,
       "mscVrPpIpPortLogicalIfLinkDestinationAddress": mscVrPpIpPortLogicalIfLinkDestinationAddress,
       "mscVrPpIpPortNs": mscVrPpIpPortNs,
       "mscVrPpIpPortNsRowStatusTable": mscVrPpIpPortNsRowStatusTable,
       "mscVrPpIpPortNsRowStatusEntry": mscVrPpIpPortNsRowStatusEntry,
       "mscVrPpIpPortNsRowStatus": mscVrPpIpPortNsRowStatus,
       "mscVrPpIpPortNsComponentName": mscVrPpIpPortNsComponentName,
       "mscVrPpIpPortNsStorageType": mscVrPpIpPortNsStorageType,
       "mscVrPpIpPortNsIndex": mscVrPpIpPortNsIndex,
       "mscVrPpIpPortNsProvTable": mscVrPpIpPortNsProvTable,
       "mscVrPpIpPortNsProvEntry": mscVrPpIpPortNsProvEntry,
       "mscVrPpIpPortNsIncomingFilter": mscVrPpIpPortNsIncomingFilter,
       "mscVrPpIpPortNsOutgoingFilter": mscVrPpIpPortNsOutgoingFilter,
       "mscVrPpIpPortBootpP": mscVrPpIpPortBootpP,
       "mscVrPpIpPortBootpPRowStatusTable": mscVrPpIpPortBootpPRowStatusTable,
       "mscVrPpIpPortBootpPRowStatusEntry": mscVrPpIpPortBootpPRowStatusEntry,
       "mscVrPpIpPortBootpPRowStatus": mscVrPpIpPortBootpPRowStatus,
       "mscVrPpIpPortBootpPComponentName": mscVrPpIpPortBootpPComponentName,
       "mscVrPpIpPortBootpPStorageType": mscVrPpIpPortBootpPStorageType,
       "mscVrPpIpPortBootpPIndex": mscVrPpIpPortBootpPIndex,
       "mscVrPpIpPortBootpPProvTable": mscVrPpIpPortBootpPProvTable,
       "mscVrPpIpPortBootpPProvEntry": mscVrPpIpPortBootpPProvEntry,
       "mscVrPpIpPortBootpPRelayForwardStatus": mscVrPpIpPortBootpPRelayForwardStatus,
       "mscVrPpIpPortBootpPBootpLogicalInterface": mscVrPpIpPortBootpPBootpLogicalInterface,
       "mscVrPpIpPortBootpPAdminControlTable": mscVrPpIpPortBootpPAdminControlTable,
       "mscVrPpIpPortBootpPAdminControlEntry": mscVrPpIpPortBootpPAdminControlEntry,
       "mscVrPpIpPortBootpPSnmpAdminStatus": mscVrPpIpPortBootpPSnmpAdminStatus,
       "mscVrPpIpPortBootpPOperStatusTable": mscVrPpIpPortBootpPOperStatusTable,
       "mscVrPpIpPortBootpPOperStatusEntry": mscVrPpIpPortBootpPOperStatusEntry,
       "mscVrPpIpPortBootpPSnmpOperStatus": mscVrPpIpPortBootpPSnmpOperStatus,
       "mscVrPpIpPortBootpPStateTable": mscVrPpIpPortBootpPStateTable,
       "mscVrPpIpPortBootpPStateEntry": mscVrPpIpPortBootpPStateEntry,
       "mscVrPpIpPortBootpPAdminState": mscVrPpIpPortBootpPAdminState,
       "mscVrPpIpPortBootpPOperationalState": mscVrPpIpPortBootpPOperationalState,
       "mscVrPpIpPortBootpPUsageState": mscVrPpIpPortBootpPUsageState,
       "mscVrPpIpPortBootpPStatsTable": mscVrPpIpPortBootpPStatsTable,
       "mscVrPpIpPortBootpPStatsEntry": mscVrPpIpPortBootpPStatsEntry,
       "mscVrPpIpPortBootpPInRequests": mscVrPpIpPortBootpPInRequests,
       "mscVrPpIpPortBootpPInReplies": mscVrPpIpPortBootpPInReplies,
       "mscVrPpIpPortBootpPOutRequests": mscVrPpIpPortBootpPOutRequests,
       "mscVrPpIpPortBootpPOutReplies": mscVrPpIpPortBootpPOutReplies,
       "mscVrPpIpPortBootpPInRequestErrors": mscVrPpIpPortBootpPInRequestErrors,
       "mscVrPpIpPortBootpPInReplyErrors": mscVrPpIpPortBootpPInReplyErrors,
       "mscVrPpIpPortBootpPAddrTable": mscVrPpIpPortBootpPAddrTable,
       "mscVrPpIpPortBootpPAddrEntry": mscVrPpIpPortBootpPAddrEntry,
       "mscVrPpIpPortBootpPAddrValue": mscVrPpIpPortBootpPAddrValue,
       "mscVrPpIpPortBootpPAddrRowStatus": mscVrPpIpPortBootpPAddrRowStatus,
       "mscVrPpIpPortProvTable": mscVrPpIpPortProvTable,
       "mscVrPpIpPortProvEntry": mscVrPpIpPortProvEntry,
       "mscVrPpIpPortMaxTxUnit": mscVrPpIpPortMaxTxUnit,
       "mscVrPpIpPortArpStatus": mscVrPpIpPortArpStatus,
       "mscVrPpIpPortProxyArpStatus": mscVrPpIpPortProxyArpStatus,
       "mscVrPpIpPortArpNoLearn": mscVrPpIpPortArpNoLearn,
       "mscVrPpIpPortSendRedirect": mscVrPpIpPortSendRedirect,
       "mscVrPpIpPortMulticastStatus": mscVrPpIpPortMulticastStatus,
       "mscVrPpIpPortRelayAddress": mscVrPpIpPortRelayAddress,
       "mscVrPpIpPortRelayBroadcast": mscVrPpIpPortRelayBroadcast,
       "mscVrPpIpPortLinkModel": mscVrPpIpPortLinkModel,
       "mscVrPpIpPortLanModel": mscVrPpIpPortLanModel,
       "mscVrPpIpPortEncap": mscVrPpIpPortEncap,
       "mscVrPpIpPortIcmpMaskReply": mscVrPpIpPortIcmpMaskReply,
       "mscVrPpIpPortDirectedBroadcast": mscVrPpIpPortDirectedBroadcast,
       "mscVrPpIpPortAssignedQos": mscVrPpIpPortAssignedQos,
       "mscVrPpIpPortAllowMcastMacDest": mscVrPpIpPortAllowMcastMacDest,
       "mscVrPpIpPortCosPolicyAssignment": mscVrPpIpPortCosPolicyAssignment,
       "mscVrPpIpPortSresProvTable": mscVrPpIpPortSresProvTable,
       "mscVrPpIpPortSresProvEntry": mscVrPpIpPortSresProvEntry,
       "mscVrPpIpPortSourceRouteEndStationSupport": mscVrPpIpPortSourceRouteEndStationSupport,
       "mscVrPpIpPortAdminControlTable": mscVrPpIpPortAdminControlTable,
       "mscVrPpIpPortAdminControlEntry": mscVrPpIpPortAdminControlEntry,
       "mscVrPpIpPortSnmpAdminStatus": mscVrPpIpPortSnmpAdminStatus,
       "mscVrPpIpPortOperTable": mscVrPpIpPortOperTable,
       "mscVrPpIpPortOperEntry": mscVrPpIpPortOperEntry,
       "mscVrPpIpPortMediaType": mscVrPpIpPortMediaType,
       "mscVrPpIpPortOperMtu": mscVrPpIpPortOperMtu,
       "mscVrPpIpPortOperArpStatus": mscVrPpIpPortOperArpStatus,
       "mscVrPpIpPortOperMulticastStatus": mscVrPpIpPortOperMulticastStatus,
       "mscVrPpIpPortOperEncap": mscVrPpIpPortOperEncap,
       "mscVrPpIpPortOperCosPolicyAssignment": mscVrPpIpPortOperCosPolicyAssignment,
       "mscVrPpIpPortRelayBcOperTable": mscVrPpIpPortRelayBcOperTable,
       "mscVrPpIpPortRelayBcOperEntry": mscVrPpIpPortRelayBcOperEntry,
       "mscVrPpIpPortRelayAddressCount": mscVrPpIpPortRelayAddressCount,
       "mscVrPpIpPortRelayBcCount": mscVrPpIpPortRelayBcCount,
       "mscVrPpIpPortStateTable": mscVrPpIpPortStateTable,
       "mscVrPpIpPortStateEntry": mscVrPpIpPortStateEntry,
       "mscVrPpIpPortAdminState": mscVrPpIpPortAdminState,
       "mscVrPpIpPortOperationalState": mscVrPpIpPortOperationalState,
       "mscVrPpIpPortUsageState": mscVrPpIpPortUsageState,
       "mscVrPpIpPortOperStatusTable": mscVrPpIpPortOperStatusTable,
       "mscVrPpIpPortOperStatusEntry": mscVrPpIpPortOperStatusEntry,
       "mscVrPpIpPortSnmpOperStatus": mscVrPpIpPortSnmpOperStatus,
       "mscVrIp": mscVrIp,
       "mscVrIpRowStatusTable": mscVrIpRowStatusTable,
       "mscVrIpRowStatusEntry": mscVrIpRowStatusEntry,
       "mscVrIpRowStatus": mscVrIpRowStatus,
       "mscVrIpComponentName": mscVrIpComponentName,
       "mscVrIpStorageType": mscVrIpStorageType,
       "mscVrIpIndex": mscVrIpIndex,
       "mscVrIpFwd": mscVrIpFwd,
       "mscVrIpFwdRowStatusTable": mscVrIpFwdRowStatusTable,
       "mscVrIpFwdRowStatusEntry": mscVrIpFwdRowStatusEntry,
       "mscVrIpFwdRowStatus": mscVrIpFwdRowStatus,
       "mscVrIpFwdComponentName": mscVrIpFwdComponentName,
       "mscVrIpFwdStorageType": mscVrIpFwdStorageType,
       "mscVrIpFwdDestAddressIndex": mscVrIpFwdDestAddressIndex,
       "mscVrIpFwdDestMaskIndex": mscVrIpFwdDestMaskIndex,
       "mscVrIpFwdTypeOfServiceIndex": mscVrIpFwdTypeOfServiceIndex,
       "mscVrIpFwdGatewayIndex": mscVrIpFwdGatewayIndex,
       "mscVrIpFwdOperTable": mscVrIpFwdOperTable,
       "mscVrIpFwdOperEntry": mscVrIpFwdOperEntry,
       "mscVrIpFwdIfIndex": mscVrIpFwdIfIndex,
       "mscVrIpFwdType": mscVrIpFwdType,
       "mscVrIpFwdProtocol": mscVrIpFwdProtocol,
       "mscVrIpFwdAge": mscVrIpFwdAge,
       "mscVrIpFwdProtocolPortName": mscVrIpFwdProtocolPortName,
       "mscVrIpFwdNextHopAs": mscVrIpFwdNextHopAs,
       "mscVrIpFwdMetric": mscVrIpFwdMetric,
       "mscVrIpRdb": mscVrIpRdb,
       "mscVrIpRdbRowStatusTable": mscVrIpRdbRowStatusTable,
       "mscVrIpRdbRowStatusEntry": mscVrIpRdbRowStatusEntry,
       "mscVrIpRdbRowStatus": mscVrIpRdbRowStatus,
       "mscVrIpRdbComponentName": mscVrIpRdbComponentName,
       "mscVrIpRdbStorageType": mscVrIpRdbStorageType,
       "mscVrIpRdbDestAddressIndex": mscVrIpRdbDestAddressIndex,
       "mscVrIpRdbDestMaskIndex": mscVrIpRdbDestMaskIndex,
       "mscVrIpRdbProtocolIndex": mscVrIpRdbProtocolIndex,
       "mscVrIpRdbGatewayIndex": mscVrIpRdbGatewayIndex,
       "mscVrIpRdbOperTable": mscVrIpRdbOperTable,
       "mscVrIpRdbOperEntry": mscVrIpRdbOperEntry,
       "mscVrIpRdbMetric": mscVrIpRdbMetric,
       "mscVrIpRdbPreference": mscVrIpRdbPreference,
       "mscVrIpRdbAge": mscVrIpRdbAge,
       "mscVrIpIf": mscVrIpIf,
       "mscVrIpIfRowStatusTable": mscVrIpIfRowStatusTable,
       "mscVrIpIfRowStatusEntry": mscVrIpIfRowStatusEntry,
       "mscVrIpIfRowStatus": mscVrIpIfRowStatus,
       "mscVrIpIfComponentName": mscVrIpIfComponentName,
       "mscVrIpIfStorageType": mscVrIpIfStorageType,
       "mscVrIpIfInterfaceAddressIndex": mscVrIpIfInterfaceAddressIndex,
       "mscVrIpIfOperTable": mscVrIpIfOperTable,
       "mscVrIpIfOperEntry": mscVrIpIfOperEntry,
       "mscVrIpIfInterfaceMask": mscVrIpIfInterfaceMask,
       "mscVrIpIfStatus": mscVrIpIfStatus,
       "mscVrIpIfPPName": mscVrIpIfPPName,
       "mscVrIpIfMediaType": mscVrIpIfMediaType,
       "mscVrIpIfHardwareAddress": mscVrIpIfHardwareAddress,
       "mscVrIpIfMtu": mscVrIpIfMtu,
       "mscVrIpIfBroadcastAddress": mscVrIpIfBroadcastAddress,
       "mscVrIpIfNcHardwareAddress": mscVrIpIfNcHardwareAddress,
       "mscVrIpEgp": mscVrIpEgp,
       "mscVrIpEgpRowStatusTable": mscVrIpEgpRowStatusTable,
       "mscVrIpEgpRowStatusEntry": mscVrIpEgpRowStatusEntry,
       "mscVrIpEgpRowStatus": mscVrIpEgpRowStatus,
       "mscVrIpEgpComponentName": mscVrIpEgpComponentName,
       "mscVrIpEgpStorageType": mscVrIpEgpStorageType,
       "mscVrIpEgpIndex": mscVrIpEgpIndex,
       "mscVrIpEgpNbr": mscVrIpEgpNbr,
       "mscVrIpEgpNbrRowStatusTable": mscVrIpEgpNbrRowStatusTable,
       "mscVrIpEgpNbrRowStatusEntry": mscVrIpEgpNbrRowStatusEntry,
       "mscVrIpEgpNbrRowStatus": mscVrIpEgpNbrRowStatus,
       "mscVrIpEgpNbrComponentName": mscVrIpEgpNbrComponentName,
       "mscVrIpEgpNbrStorageType": mscVrIpEgpNbrStorageType,
       "mscVrIpEgpNbrNeighborAddressIndex": mscVrIpEgpNbrNeighborAddressIndex,
       "mscVrIpEgpNbrProvTable": mscVrIpEgpNbrProvTable,
       "mscVrIpEgpNbrProvEntry": mscVrIpEgpNbrProvEntry,
       "mscVrIpEgpNbrAsId": mscVrIpEgpNbrAsId,
       "mscVrIpEgpNbrMode": mscVrIpEgpNbrMode,
       "mscVrIpEgpNbrGenerateDefaultRoute": mscVrIpEgpNbrGenerateDefaultRoute,
       "mscVrIpEgpNbrDefaultRouteMetric": mscVrIpEgpNbrDefaultRouteMetric,
       "mscVrIpEgpNbrDefaultMetric": mscVrIpEgpNbrDefaultMetric,
       "mscVrIpEgpNbrHelloInterval": mscVrIpEgpNbrHelloInterval,
       "mscVrIpEgpNbrPollInterval": mscVrIpEgpNbrPollInterval,
       "mscVrIpEgpNbrOperTable": mscVrIpEgpNbrOperTable,
       "mscVrIpEgpNbrOperEntry": mscVrIpEgpNbrOperEntry,
       "mscVrIpEgpNbrState": mscVrIpEgpNbrState,
       "mscVrIpEgpNbrInMsgs": mscVrIpEgpNbrInMsgs,
       "mscVrIpEgpNbrInErrors": mscVrIpEgpNbrInErrors,
       "mscVrIpEgpNbrOutMsgs": mscVrIpEgpNbrOutMsgs,
       "mscVrIpEgpNbrOutErrors": mscVrIpEgpNbrOutErrors,
       "mscVrIpEgpNbrInErrorMsgs": mscVrIpEgpNbrInErrorMsgs,
       "mscVrIpEgpNbrOutErrorMsgs": mscVrIpEgpNbrOutErrorMsgs,
       "mscVrIpEgpNbrStateUps": mscVrIpEgpNbrStateUps,
       "mscVrIpEgpNbrStateDowns": mscVrIpEgpNbrStateDowns,
       "mscVrIpEgpNbrEventTrigger": mscVrIpEgpNbrEventTrigger,
       "mscVrIpEgpImport": mscVrIpEgpImport,
       "mscVrIpEgpImportRowStatusTable": mscVrIpEgpImportRowStatusTable,
       "mscVrIpEgpImportRowStatusEntry": mscVrIpEgpImportRowStatusEntry,
       "mscVrIpEgpImportRowStatus": mscVrIpEgpImportRowStatus,
       "mscVrIpEgpImportComponentName": mscVrIpEgpImportComponentName,
       "mscVrIpEgpImportStorageType": mscVrIpEgpImportStorageType,
       "mscVrIpEgpImportIndex": mscVrIpEgpImportIndex,
       "mscVrIpEgpImportNet": mscVrIpEgpImportNet,
       "mscVrIpEgpImportNetRowStatusTable": mscVrIpEgpImportNetRowStatusTable,
       "mscVrIpEgpImportNetRowStatusEntry": mscVrIpEgpImportNetRowStatusEntry,
       "mscVrIpEgpImportNetRowStatus": mscVrIpEgpImportNetRowStatus,
       "mscVrIpEgpImportNetComponentName": mscVrIpEgpImportNetComponentName,
       "mscVrIpEgpImportNetStorageType": mscVrIpEgpImportNetStorageType,
       "mscVrIpEgpImportNetIndex": mscVrIpEgpImportNetIndex,
       "mscVrIpEgpImportNetProvTable": mscVrIpEgpImportNetProvTable,
       "mscVrIpEgpImportNetProvEntry": mscVrIpEgpImportNetProvEntry,
       "mscVrIpEgpImportNetIpAddress": mscVrIpEgpImportNetIpAddress,
       "mscVrIpEgpImportProvTable": mscVrIpEgpImportProvTable,
       "mscVrIpEgpImportProvEntry": mscVrIpEgpImportProvEntry,
       "mscVrIpEgpImportUsageFlag": mscVrIpEgpImportUsageFlag,
       "mscVrIpEgpImportImportMetric": mscVrIpEgpImportImportMetric,
       "mscVrIpEgpImportNbrAsId": mscVrIpEgpImportNbrAsId,
       "mscVrIpEgpExport": mscVrIpEgpExport,
       "mscVrIpEgpExportRowStatusTable": mscVrIpEgpExportRowStatusTable,
       "mscVrIpEgpExportRowStatusEntry": mscVrIpEgpExportRowStatusEntry,
       "mscVrIpEgpExportRowStatus": mscVrIpEgpExportRowStatus,
       "mscVrIpEgpExportComponentName": mscVrIpEgpExportComponentName,
       "mscVrIpEgpExportStorageType": mscVrIpEgpExportStorageType,
       "mscVrIpEgpExportIndex": mscVrIpEgpExportIndex,
       "mscVrIpEgpExportNet": mscVrIpEgpExportNet,
       "mscVrIpEgpExportNetRowStatusTable": mscVrIpEgpExportNetRowStatusTable,
       "mscVrIpEgpExportNetRowStatusEntry": mscVrIpEgpExportNetRowStatusEntry,
       "mscVrIpEgpExportNetRowStatus": mscVrIpEgpExportNetRowStatus,
       "mscVrIpEgpExportNetComponentName": mscVrIpEgpExportNetComponentName,
       "mscVrIpEgpExportNetStorageType": mscVrIpEgpExportNetStorageType,
       "mscVrIpEgpExportNetIndex": mscVrIpEgpExportNetIndex,
       "mscVrIpEgpExportNetProvTable": mscVrIpEgpExportNetProvTable,
       "mscVrIpEgpExportNetProvEntry": mscVrIpEgpExportNetProvEntry,
       "mscVrIpEgpExportNetIpAddress": mscVrIpEgpExportNetIpAddress,
       "mscVrIpEgpExportProvTable": mscVrIpEgpExportProvTable,
       "mscVrIpEgpExportProvEntry": mscVrIpEgpExportProvEntry,
       "mscVrIpEgpExportAdvertiseStatus": mscVrIpEgpExportAdvertiseStatus,
       "mscVrIpEgpExportExportMetric": mscVrIpEgpExportExportMetric,
       "mscVrIpEgpExportProtocol": mscVrIpEgpExportProtocol,
       "mscVrIpEgpExportRipInterface": mscVrIpEgpExportRipInterface,
       "mscVrIpEgpExportRipNeighbor": mscVrIpEgpExportRipNeighbor,
       "mscVrIpEgpExportInEgpAsId": mscVrIpEgpExportInEgpAsId,
       "mscVrIpEgpExportOspfTag": mscVrIpEgpExportOspfTag,
       "mscVrIpEgpExportOutAutonomousSystem": mscVrIpEgpExportOutAutonomousSystem,
       "mscVrIpEgpProvTable": mscVrIpEgpProvTable,
       "mscVrIpEgpProvEntry": mscVrIpEgpProvEntry,
       "mscVrIpEgpAsId": mscVrIpEgpAsId,
       "mscVrIpEgpDefaultHelloInterval": mscVrIpEgpDefaultHelloInterval,
       "mscVrIpEgpDefaultPollInterval": mscVrIpEgpDefaultPollInterval,
       "mscVrIpEgpMaxNatNets": mscVrIpEgpMaxNatNets,
       "mscVrIpEgpMaxBufferSize": mscVrIpEgpMaxBufferSize,
       "mscVrIpEgpStatsTable": mscVrIpEgpStatsTable,
       "mscVrIpEgpStatsEntry": mscVrIpEgpStatsEntry,
       "mscVrIpEgpInMsgs": mscVrIpEgpInMsgs,
       "mscVrIpEgpInErrorMsgs": mscVrIpEgpInErrorMsgs,
       "mscVrIpEgpOutErrorMsgs": mscVrIpEgpOutErrorMsgs,
       "mscVrIpEgpInErrors": mscVrIpEgpInErrors,
       "mscVrIpEgpOutMsgs": mscVrIpEgpOutMsgs,
       "mscVrIpEgpOutErrors": mscVrIpEgpOutErrors,
       "mscVrIpEgpStateTable": mscVrIpEgpStateTable,
       "mscVrIpEgpStateEntry": mscVrIpEgpStateEntry,
       "mscVrIpEgpAdminState": mscVrIpEgpAdminState,
       "mscVrIpEgpOperationalState": mscVrIpEgpOperationalState,
       "mscVrIpEgpUsageState": mscVrIpEgpUsageState,
       "mscVrIpEgpAdminControlTable": mscVrIpEgpAdminControlTable,
       "mscVrIpEgpAdminControlEntry": mscVrIpEgpAdminControlEntry,
       "mscVrIpEgpSnmpAdminStatus": mscVrIpEgpSnmpAdminStatus,
       "mscVrIpEgpOperStatusTable": mscVrIpEgpOperStatusTable,
       "mscVrIpEgpOperStatusEntry": mscVrIpEgpOperStatusEntry,
       "mscVrIpEgpSnmpOperStatus": mscVrIpEgpSnmpOperStatus,
       "mscVrIpOspf": mscVrIpOspf,
       "mscVrIpOspfRowStatusTable": mscVrIpOspfRowStatusTable,
       "mscVrIpOspfRowStatusEntry": mscVrIpOspfRowStatusEntry,
       "mscVrIpOspfRowStatus": mscVrIpOspfRowStatus,
       "mscVrIpOspfComponentName": mscVrIpOspfComponentName,
       "mscVrIpOspfStorageType": mscVrIpOspfStorageType,
       "mscVrIpOspfIndex": mscVrIpOspfIndex,
       "mscVrIpOspfArea": mscVrIpOspfArea,
       "mscVrIpOspfAreaRowStatusTable": mscVrIpOspfAreaRowStatusTable,
       "mscVrIpOspfAreaRowStatusEntry": mscVrIpOspfAreaRowStatusEntry,
       "mscVrIpOspfAreaRowStatus": mscVrIpOspfAreaRowStatus,
       "mscVrIpOspfAreaComponentName": mscVrIpOspfAreaComponentName,
       "mscVrIpOspfAreaStorageType": mscVrIpOspfAreaStorageType,
       "mscVrIpOspfAreaAreaIdIndex": mscVrIpOspfAreaAreaIdIndex,
       "mscVrIpOspfAreaProvTable": mscVrIpOspfAreaProvTable,
       "mscVrIpOspfAreaProvEntry": mscVrIpOspfAreaProvEntry,
       "mscVrIpOspfAreaAuthType": mscVrIpOspfAreaAuthType,
       "mscVrIpOspfAreaImportAsExtern": mscVrIpOspfAreaImportAsExtern,
       "mscVrIpOspfAreaAreaSummary": mscVrIpOspfAreaAreaSummary,
       "mscVrIpOspfAreaOperTable": mscVrIpOspfAreaOperTable,
       "mscVrIpOspfAreaOperEntry": mscVrIpOspfAreaOperEntry,
       "mscVrIpOspfAreaSpfRuns": mscVrIpOspfAreaSpfRuns,
       "mscVrIpOspfAreaAreaBdrRtrCount": mscVrIpOspfAreaAreaBdrRtrCount,
       "mscVrIpOspfAreaAsBdrRtrCount": mscVrIpOspfAreaAsBdrRtrCount,
       "mscVrIpOspfAreaLsaCount": mscVrIpOspfAreaLsaCount,
       "mscVrIpOspfAreaAreaLsaCksumSum": mscVrIpOspfAreaAreaLsaCksumSum,
       "mscVrIpOspfStub": mscVrIpOspfStub,
       "mscVrIpOspfStubRowStatusTable": mscVrIpOspfStubRowStatusTable,
       "mscVrIpOspfStubRowStatusEntry": mscVrIpOspfStubRowStatusEntry,
       "mscVrIpOspfStubRowStatus": mscVrIpOspfStubRowStatus,
       "mscVrIpOspfStubComponentName": mscVrIpOspfStubComponentName,
       "mscVrIpOspfStubStorageType": mscVrIpOspfStubStorageType,
       "mscVrIpOspfStubAreaIdIndex": mscVrIpOspfStubAreaIdIndex,
       "mscVrIpOspfStubTosIndex": mscVrIpOspfStubTosIndex,
       "mscVrIpOspfStubProvTable": mscVrIpOspfStubProvTable,
       "mscVrIpOspfStubProvEntry": mscVrIpOspfStubProvEntry,
       "mscVrIpOspfStubMetric": mscVrIpOspfStubMetric,
       "mscVrIpOspfStubMetricType": mscVrIpOspfStubMetricType,
       "mscVrIpOspfStubAdvertiseDefault": mscVrIpOspfStubAdvertiseDefault,
       "mscVrIpOspfAggregate": mscVrIpOspfAggregate,
       "mscVrIpOspfAggregateRowStatusTable": mscVrIpOspfAggregateRowStatusTable,
       "mscVrIpOspfAggregateRowStatusEntry": mscVrIpOspfAggregateRowStatusEntry,
       "mscVrIpOspfAggregateRowStatus": mscVrIpOspfAggregateRowStatus,
       "mscVrIpOspfAggregateComponentName": mscVrIpOspfAggregateComponentName,
       "mscVrIpOspfAggregateStorageType": mscVrIpOspfAggregateStorageType,
       "mscVrIpOspfAggregateAreaIdIndex": mscVrIpOspfAggregateAreaIdIndex,
       "mscVrIpOspfAggregateLsdbTypeIndex": mscVrIpOspfAggregateLsdbTypeIndex,
       "mscVrIpOspfAggregateAggregateNetIndex": mscVrIpOspfAggregateAggregateNetIndex,
       "mscVrIpOspfAggregateAggregateMaskIndex": mscVrIpOspfAggregateAggregateMaskIndex,
       "mscVrIpOspfAggregateProvTable": mscVrIpOspfAggregateProvTable,
       "mscVrIpOspfAggregateProvEntry": mscVrIpOspfAggregateProvEntry,
       "mscVrIpOspfAggregateEffect": mscVrIpOspfAggregateEffect,
       "mscVrIpOspfHost": mscVrIpOspfHost,
       "mscVrIpOspfHostRowStatusTable": mscVrIpOspfHostRowStatusTable,
       "mscVrIpOspfHostRowStatusEntry": mscVrIpOspfHostRowStatusEntry,
       "mscVrIpOspfHostRowStatus": mscVrIpOspfHostRowStatus,
       "mscVrIpOspfHostComponentName": mscVrIpOspfHostComponentName,
       "mscVrIpOspfHostStorageType": mscVrIpOspfHostStorageType,
       "mscVrIpOspfHostAddressIndex": mscVrIpOspfHostAddressIndex,
       "mscVrIpOspfHostTosIndex": mscVrIpOspfHostTosIndex,
       "mscVrIpOspfHostProvTable": mscVrIpOspfHostProvTable,
       "mscVrIpOspfHostProvEntry": mscVrIpOspfHostProvEntry,
       "mscVrIpOspfHostAreaId": mscVrIpOspfHostAreaId,
       "mscVrIpOspfHostMetric": mscVrIpOspfHostMetric,
       "mscVrIpOspfVirtIf": mscVrIpOspfVirtIf,
       "mscVrIpOspfVirtIfRowStatusTable": mscVrIpOspfVirtIfRowStatusTable,
       "mscVrIpOspfVirtIfRowStatusEntry": mscVrIpOspfVirtIfRowStatusEntry,
       "mscVrIpOspfVirtIfRowStatus": mscVrIpOspfVirtIfRowStatus,
       "mscVrIpOspfVirtIfComponentName": mscVrIpOspfVirtIfComponentName,
       "mscVrIpOspfVirtIfStorageType": mscVrIpOspfVirtIfStorageType,
       "mscVrIpOspfVirtIfAreaIdIndex": mscVrIpOspfVirtIfAreaIdIndex,
       "mscVrIpOspfVirtIfNbrRouterIdIndex": mscVrIpOspfVirtIfNbrRouterIdIndex,
       "mscVrIpOspfVirtIfProvTable": mscVrIpOspfVirtIfProvTable,
       "mscVrIpOspfVirtIfProvEntry": mscVrIpOspfVirtIfProvEntry,
       "mscVrIpOspfVirtIfTransitDelay": mscVrIpOspfVirtIfTransitDelay,
       "mscVrIpOspfVirtIfRetransInterval": mscVrIpOspfVirtIfRetransInterval,
       "mscVrIpOspfVirtIfHelloInterval": mscVrIpOspfVirtIfHelloInterval,
       "mscVrIpOspfVirtIfRtrDeadInterval": mscVrIpOspfVirtIfRtrDeadInterval,
       "mscVrIpOspfVirtIfAuthKey": mscVrIpOspfVirtIfAuthKey,
       "mscVrIpOspfVirtIfOperTable": mscVrIpOspfVirtIfOperTable,
       "mscVrIpOspfVirtIfOperEntry": mscVrIpOspfVirtIfOperEntry,
       "mscVrIpOspfVirtIfState": mscVrIpOspfVirtIfState,
       "mscVrIpOspfVirtIfEvents": mscVrIpOspfVirtIfEvents,
       "mscVrIpOspfExport": mscVrIpOspfExport,
       "mscVrIpOspfExportRowStatusTable": mscVrIpOspfExportRowStatusTable,
       "mscVrIpOspfExportRowStatusEntry": mscVrIpOspfExportRowStatusEntry,
       "mscVrIpOspfExportRowStatus": mscVrIpOspfExportRowStatus,
       "mscVrIpOspfExportComponentName": mscVrIpOspfExportComponentName,
       "mscVrIpOspfExportStorageType": mscVrIpOspfExportStorageType,
       "mscVrIpOspfExportIndex": mscVrIpOspfExportIndex,
       "mscVrIpOspfExportNetList": mscVrIpOspfExportNetList,
       "mscVrIpOspfExportNetListRowStatusTable": mscVrIpOspfExportNetListRowStatusTable,
       "mscVrIpOspfExportNetListRowStatusEntry": mscVrIpOspfExportNetListRowStatusEntry,
       "mscVrIpOspfExportNetListRowStatus": mscVrIpOspfExportNetListRowStatus,
       "mscVrIpOspfExportNetListComponentName": mscVrIpOspfExportNetListComponentName,
       "mscVrIpOspfExportNetListStorageType": mscVrIpOspfExportNetListStorageType,
       "mscVrIpOspfExportNetListIndex": mscVrIpOspfExportNetListIndex,
       "mscVrIpOspfExportNetListProvTable": mscVrIpOspfExportNetListProvTable,
       "mscVrIpOspfExportNetListProvEntry": mscVrIpOspfExportNetListProvEntry,
       "mscVrIpOspfExportNetListIpAddress": mscVrIpOspfExportNetListIpAddress,
       "mscVrIpOspfExportNetListIpMask": mscVrIpOspfExportNetListIpMask,
       "mscVrIpOspfExportProvTable": mscVrIpOspfExportProvTable,
       "mscVrIpOspfExportProvEntry": mscVrIpOspfExportProvEntry,
       "mscVrIpOspfExportAdvertiseStatus": mscVrIpOspfExportAdvertiseStatus,
       "mscVrIpOspfExportMetric": mscVrIpOspfExportMetric,
       "mscVrIpOspfExportProtocol": mscVrIpOspfExportProtocol,
       "mscVrIpOspfExportRipInterface": mscVrIpOspfExportRipInterface,
       "mscVrIpOspfExportRipNeighbor": mscVrIpOspfExportRipNeighbor,
       "mscVrIpOspfExportEgpAsId": mscVrIpOspfExportEgpAsId,
       "mscVrIpOspfExportTag": mscVrIpOspfExportTag,
       "mscVrIpOspfExportExtLsaMetricType": mscVrIpOspfExportExtLsaMetricType,
       "mscVrIpOspfExportBgpAsId": mscVrIpOspfExportBgpAsId,
       "mscVrIpOspfExportBgpPeerIp": mscVrIpOspfExportBgpPeerIp,
       "mscVrIpOspfVirtNbr": mscVrIpOspfVirtNbr,
       "mscVrIpOspfVirtNbrRowStatusTable": mscVrIpOspfVirtNbrRowStatusTable,
       "mscVrIpOspfVirtNbrRowStatusEntry": mscVrIpOspfVirtNbrRowStatusEntry,
       "mscVrIpOspfVirtNbrRowStatus": mscVrIpOspfVirtNbrRowStatus,
       "mscVrIpOspfVirtNbrComponentName": mscVrIpOspfVirtNbrComponentName,
       "mscVrIpOspfVirtNbrStorageType": mscVrIpOspfVirtNbrStorageType,
       "mscVrIpOspfVirtNbrAreaIdIndex": mscVrIpOspfVirtNbrAreaIdIndex,
       "mscVrIpOspfVirtNbrNbrRouterIdIndex": mscVrIpOspfVirtNbrNbrRouterIdIndex,
       "mscVrIpOspfVirtNbrOperTable": mscVrIpOspfVirtNbrOperTable,
       "mscVrIpOspfVirtNbrOperEntry": mscVrIpOspfVirtNbrOperEntry,
       "mscVrIpOspfVirtNbrNbrIpAddress": mscVrIpOspfVirtNbrNbrIpAddress,
       "mscVrIpOspfVirtNbrOptions": mscVrIpOspfVirtNbrOptions,
       "mscVrIpOspfVirtNbrState": mscVrIpOspfVirtNbrState,
       "mscVrIpOspfVirtNbrEvents": mscVrIpOspfVirtNbrEvents,
       "mscVrIpOspfVirtNbrLsRetransQlen": mscVrIpOspfVirtNbrLsRetransQlen,
       "mscVrIpOspfVirtNbrExchangeStatus": mscVrIpOspfVirtNbrExchangeStatus,
       "mscVrIpOspfNbr": mscVrIpOspfNbr,
       "mscVrIpOspfNbrRowStatusTable": mscVrIpOspfNbrRowStatusTable,
       "mscVrIpOspfNbrRowStatusEntry": mscVrIpOspfNbrRowStatusEntry,
       "mscVrIpOspfNbrRowStatus": mscVrIpOspfNbrRowStatus,
       "mscVrIpOspfNbrComponentName": mscVrIpOspfNbrComponentName,
       "mscVrIpOspfNbrStorageType": mscVrIpOspfNbrStorageType,
       "mscVrIpOspfNbrAddressIndex": mscVrIpOspfNbrAddressIndex,
       "mscVrIpOspfNbrAddressLessIndex": mscVrIpOspfNbrAddressLessIndex,
       "mscVrIpOspfNbrOperTable": mscVrIpOspfNbrOperTable,
       "mscVrIpOspfNbrOperEntry": mscVrIpOspfNbrOperEntry,
       "mscVrIpOspfNbrRtrId": mscVrIpOspfNbrRtrId,
       "mscVrIpOspfNbrOptions": mscVrIpOspfNbrOptions,
       "mscVrIpOspfNbrPriority": mscVrIpOspfNbrPriority,
       "mscVrIpOspfNbrState": mscVrIpOspfNbrState,
       "mscVrIpOspfNbrEvents": mscVrIpOspfNbrEvents,
       "mscVrIpOspfNbrLsRetransQlen": mscVrIpOspfNbrLsRetransQlen,
       "mscVrIpOspfNbrNbmaNbrStatus": mscVrIpOspfNbrNbmaNbrStatus,
       "mscVrIpOspfNbrExchangeStatus": mscVrIpOspfNbrExchangeStatus,
       "mscVrIpOspfNbrPermanence": mscVrIpOspfNbrPermanence,
       "mscVrIpOspfLsdb": mscVrIpOspfLsdb,
       "mscVrIpOspfLsdbRowStatusTable": mscVrIpOspfLsdbRowStatusTable,
       "mscVrIpOspfLsdbRowStatusEntry": mscVrIpOspfLsdbRowStatusEntry,
       "mscVrIpOspfLsdbRowStatus": mscVrIpOspfLsdbRowStatus,
       "mscVrIpOspfLsdbComponentName": mscVrIpOspfLsdbComponentName,
       "mscVrIpOspfLsdbStorageType": mscVrIpOspfLsdbStorageType,
       "mscVrIpOspfLsdbAreaIdIndex": mscVrIpOspfLsdbAreaIdIndex,
       "mscVrIpOspfLsdbLsdbTypeIndex": mscVrIpOspfLsdbLsdbTypeIndex,
       "mscVrIpOspfLsdbLsIdIndex": mscVrIpOspfLsdbLsIdIndex,
       "mscVrIpOspfLsdbRouterIdIndex": mscVrIpOspfLsdbRouterIdIndex,
       "mscVrIpOspfLsdbOperTable": mscVrIpOspfLsdbOperTable,
       "mscVrIpOspfLsdbOperEntry": mscVrIpOspfLsdbOperEntry,
       "mscVrIpOspfLsdbSequence": mscVrIpOspfLsdbSequence,
       "mscVrIpOspfLsdbAge": mscVrIpOspfLsdbAge,
       "mscVrIpOspfLsdbChecksum": mscVrIpOspfLsdbChecksum,
       "mscVrIpOspfLsdbAdvertisement": mscVrIpOspfLsdbAdvertisement,
       "mscVrIpOspfExtLsdb": mscVrIpOspfExtLsdb,
       "mscVrIpOspfExtLsdbRowStatusTable": mscVrIpOspfExtLsdbRowStatusTable,
       "mscVrIpOspfExtLsdbRowStatusEntry": mscVrIpOspfExtLsdbRowStatusEntry,
       "mscVrIpOspfExtLsdbRowStatus": mscVrIpOspfExtLsdbRowStatus,
       "mscVrIpOspfExtLsdbComponentName": mscVrIpOspfExtLsdbComponentName,
       "mscVrIpOspfExtLsdbStorageType": mscVrIpOspfExtLsdbStorageType,
       "mscVrIpOspfExtLsdbLsdbTypeIndex": mscVrIpOspfExtLsdbLsdbTypeIndex,
       "mscVrIpOspfExtLsdbLsIdIndex": mscVrIpOspfExtLsdbLsIdIndex,
       "mscVrIpOspfExtLsdbRouterIdIndex": mscVrIpOspfExtLsdbRouterIdIndex,
       "mscVrIpOspfExtLsdbOperTable": mscVrIpOspfExtLsdbOperTable,
       "mscVrIpOspfExtLsdbOperEntry": mscVrIpOspfExtLsdbOperEntry,
       "mscVrIpOspfExtLsdbSequence": mscVrIpOspfExtLsdbSequence,
       "mscVrIpOspfExtLsdbAge": mscVrIpOspfExtLsdbAge,
       "mscVrIpOspfExtLsdbChecksum": mscVrIpOspfExtLsdbChecksum,
       "mscVrIpOspfExtLsdbAdvertisement": mscVrIpOspfExtLsdbAdvertisement,
       "mscVrIpOspfProvTable": mscVrIpOspfProvTable,
       "mscVrIpOspfProvEntry": mscVrIpOspfProvEntry,
       "mscVrIpOspfRouterId": mscVrIpOspfRouterId,
       "mscVrIpOspfSnmpAdminStatus": mscVrIpOspfSnmpAdminStatus,
       "mscVrIpOspfAsBdrRtrStatus": mscVrIpOspfAsBdrRtrStatus,
       "mscVrIpOspfTosSupport": mscVrIpOspfTosSupport,
       "mscVrIpOspfExtLsdbLimit": mscVrIpOspfExtLsdbLimit,
       "mscVrIpOspfMulticastForward": mscVrIpOspfMulticastForward,
       "mscVrIpOspfMigrateRip": mscVrIpOspfMigrateRip,
       "mscVrIpOspfGenerateDefaultRouteMetric": mscVrIpOspfGenerateDefaultRouteMetric,
       "mscVrIpOspfRedistributeIbgp": mscVrIpOspfRedistributeIbgp,
       "mscVrIpOspfOperTable": mscVrIpOspfOperTable,
       "mscVrIpOspfOperEntry": mscVrIpOspfOperEntry,
       "mscVrIpOspfVersionNumber": mscVrIpOspfVersionNumber,
       "mscVrIpOspfAreaBdrRtrStatus": mscVrIpOspfAreaBdrRtrStatus,
       "mscVrIpOspfExternLsaCount": mscVrIpOspfExternLsaCount,
       "mscVrIpOspfExternLsaChecksumSum": mscVrIpOspfExternLsaChecksumSum,
       "mscVrIpOspfOriginateNewLsas": mscVrIpOspfOriginateNewLsas,
       "mscVrIpOspfRxNewLsas": mscVrIpOspfRxNewLsas,
       "mscVrIpOspfStateTable": mscVrIpOspfStateTable,
       "mscVrIpOspfStateEntry": mscVrIpOspfStateEntry,
       "mscVrIpOspfAdminState": mscVrIpOspfAdminState,
       "mscVrIpOspfOperationalState": mscVrIpOspfOperationalState,
       "mscVrIpOspfUsageState": mscVrIpOspfUsageState,
       "mscVrIpOspfOperStatusTable": mscVrIpOspfOperStatusTable,
       "mscVrIpOspfOperStatusEntry": mscVrIpOspfOperStatusEntry,
       "mscVrIpOspfSnmpOperStatus": mscVrIpOspfSnmpOperStatus,
       "mscVrIpRip": mscVrIpRip,
       "mscVrIpRipRowStatusTable": mscVrIpRipRowStatusTable,
       "mscVrIpRipRowStatusEntry": mscVrIpRipRowStatusEntry,
       "mscVrIpRipRowStatus": mscVrIpRipRowStatus,
       "mscVrIpRipComponentName": mscVrIpRipComponentName,
       "mscVrIpRipStorageType": mscVrIpRipStorageType,
       "mscVrIpRipIndex": mscVrIpRipIndex,
       "mscVrIpRipImport": mscVrIpRipImport,
       "mscVrIpRipImportRowStatusTable": mscVrIpRipImportRowStatusTable,
       "mscVrIpRipImportRowStatusEntry": mscVrIpRipImportRowStatusEntry,
       "mscVrIpRipImportRowStatus": mscVrIpRipImportRowStatus,
       "mscVrIpRipImportComponentName": mscVrIpRipImportComponentName,
       "mscVrIpRipImportStorageType": mscVrIpRipImportStorageType,
       "mscVrIpRipImportIndex": mscVrIpRipImportIndex,
       "mscVrIpRipImportNet": mscVrIpRipImportNet,
       "mscVrIpRipImportNetRowStatusTable": mscVrIpRipImportNetRowStatusTable,
       "mscVrIpRipImportNetRowStatusEntry": mscVrIpRipImportNetRowStatusEntry,
       "mscVrIpRipImportNetRowStatus": mscVrIpRipImportNetRowStatus,
       "mscVrIpRipImportNetComponentName": mscVrIpRipImportNetComponentName,
       "mscVrIpRipImportNetStorageType": mscVrIpRipImportNetStorageType,
       "mscVrIpRipImportNetIndex": mscVrIpRipImportNetIndex,
       "mscVrIpRipImportNetProvTable": mscVrIpRipImportNetProvTable,
       "mscVrIpRipImportNetProvEntry": mscVrIpRipImportNetProvEntry,
       "mscVrIpRipImportNetIpAddress": mscVrIpRipImportNetIpAddress,
       "mscVrIpRipImportNetIpMask": mscVrIpRipImportNetIpMask,
       "mscVrIpRipImportProvTable": mscVrIpRipImportProvTable,
       "mscVrIpRipImportProvEntry": mscVrIpRipImportProvEntry,
       "mscVrIpRipImportUsageFlag": mscVrIpRipImportUsageFlag,
       "mscVrIpRipImportImportMetric": mscVrIpRipImportImportMetric,
       "mscVrIpRipImportNeighbor": mscVrIpRipImportNeighbor,
       "mscVrIpRipImportInterface": mscVrIpRipImportInterface,
       "mscVrIpRipExport": mscVrIpRipExport,
       "mscVrIpRipExportRowStatusTable": mscVrIpRipExportRowStatusTable,
       "mscVrIpRipExportRowStatusEntry": mscVrIpRipExportRowStatusEntry,
       "mscVrIpRipExportRowStatus": mscVrIpRipExportRowStatus,
       "mscVrIpRipExportComponentName": mscVrIpRipExportComponentName,
       "mscVrIpRipExportStorageType": mscVrIpRipExportStorageType,
       "mscVrIpRipExportIndex": mscVrIpRipExportIndex,
       "mscVrIpRipExportNet": mscVrIpRipExportNet,
       "mscVrIpRipExportNetRowStatusTable": mscVrIpRipExportNetRowStatusTable,
       "mscVrIpRipExportNetRowStatusEntry": mscVrIpRipExportNetRowStatusEntry,
       "mscVrIpRipExportNetRowStatus": mscVrIpRipExportNetRowStatus,
       "mscVrIpRipExportNetComponentName": mscVrIpRipExportNetComponentName,
       "mscVrIpRipExportNetStorageType": mscVrIpRipExportNetStorageType,
       "mscVrIpRipExportNetIndex": mscVrIpRipExportNetIndex,
       "mscVrIpRipExportNetProvTable": mscVrIpRipExportNetProvTable,
       "mscVrIpRipExportNetProvEntry": mscVrIpRipExportNetProvEntry,
       "mscVrIpRipExportNetIpAddress": mscVrIpRipExportNetIpAddress,
       "mscVrIpRipExportNetIpMask": mscVrIpRipExportNetIpMask,
       "mscVrIpRipExportProvTable": mscVrIpRipExportProvTable,
       "mscVrIpRipExportProvEntry": mscVrIpRipExportProvEntry,
       "mscVrIpRipExportAdvertiseStatus": mscVrIpRipExportAdvertiseStatus,
       "mscVrIpRipExportExportMetric": mscVrIpRipExportExportMetric,
       "mscVrIpRipExportProtocol": mscVrIpRipExportProtocol,
       "mscVrIpRipExportRipInterface": mscVrIpRipExportRipInterface,
       "mscVrIpRipExportEgpAsId": mscVrIpRipExportEgpAsId,
       "mscVrIpRipExportOspfTag": mscVrIpRipExportOspfTag,
       "mscVrIpRipExportOutInterface": mscVrIpRipExportOutInterface,
       "mscVrIpRipExportBgpAsId": mscVrIpRipExportBgpAsId,
       "mscVrIpRipProvTable": mscVrIpRipProvTable,
       "mscVrIpRipProvEntry": mscVrIpRipProvEntry,
       "mscVrIpRipMigrateRip": mscVrIpRipMigrateRip,
       "mscVrIpRipRfc1058MetricUsage": mscVrIpRipRfc1058MetricUsage,
       "mscVrIpRipGenerateDiscardRoute": mscVrIpRipGenerateDiscardRoute,
       "mscVrIpRipRedistributeIbgp": mscVrIpRipRedistributeIbgp,
       "mscVrIpRipStateTable": mscVrIpRipStateTable,
       "mscVrIpRipStateEntry": mscVrIpRipStateEntry,
       "mscVrIpRipAdminState": mscVrIpRipAdminState,
       "mscVrIpRipOperationalState": mscVrIpRipOperationalState,
       "mscVrIpRipUsageState": mscVrIpRipUsageState,
       "mscVrIpRipAdminControlTable": mscVrIpRipAdminControlTable,
       "mscVrIpRipAdminControlEntry": mscVrIpRipAdminControlEntry,
       "mscVrIpRipSnmpAdminStatus": mscVrIpRipSnmpAdminStatus,
       "mscVrIpRipOperStatusTable": mscVrIpRipOperStatusTable,
       "mscVrIpRipOperStatusEntry": mscVrIpRipOperStatusEntry,
       "mscVrIpRipSnmpOperStatus": mscVrIpRipSnmpOperStatus,
       "mscVrIpRipOperTable": mscVrIpRipOperTable,
       "mscVrIpRipOperEntry": mscVrIpRipOperEntry,
       "mscVrIpRipRouteChangesMade": mscVrIpRipRouteChangesMade,
       "mscVrIpRipQueryResponses": mscVrIpRipQueryResponses,
       "mscVrIpStatic": mscVrIpStatic,
       "mscVrIpStaticRowStatusTable": mscVrIpStaticRowStatusTable,
       "mscVrIpStaticRowStatusEntry": mscVrIpStaticRowStatusEntry,
       "mscVrIpStaticRowStatus": mscVrIpStaticRowStatus,
       "mscVrIpStaticComponentName": mscVrIpStaticComponentName,
       "mscVrIpStaticStorageType": mscVrIpStaticStorageType,
       "mscVrIpStaticIndex": mscVrIpStaticIndex,
       "mscVrIpStaticRoute": mscVrIpStaticRoute,
       "mscVrIpStaticRouteRowStatusTable": mscVrIpStaticRouteRowStatusTable,
       "mscVrIpStaticRouteRowStatusEntry": mscVrIpStaticRouteRowStatusEntry,
       "mscVrIpStaticRouteRowStatus": mscVrIpStaticRouteRowStatus,
       "mscVrIpStaticRouteComponentName": mscVrIpStaticRouteComponentName,
       "mscVrIpStaticRouteStorageType": mscVrIpStaticRouteStorageType,
       "mscVrIpStaticRouteDestAddressIndex": mscVrIpStaticRouteDestAddressIndex,
       "mscVrIpStaticRouteDestMaskIndex": mscVrIpStaticRouteDestMaskIndex,
       "mscVrIpStaticRouteTypeOfServiceIndex": mscVrIpStaticRouteTypeOfServiceIndex,
       "mscVrIpStaticRouteNh": mscVrIpStaticRouteNh,
       "mscVrIpStaticRouteNhRowStatusTable": mscVrIpStaticRouteNhRowStatusTable,
       "mscVrIpStaticRouteNhRowStatusEntry": mscVrIpStaticRouteNhRowStatusEntry,
       "mscVrIpStaticRouteNhRowStatus": mscVrIpStaticRouteNhRowStatus,
       "mscVrIpStaticRouteNhComponentName": mscVrIpStaticRouteNhComponentName,
       "mscVrIpStaticRouteNhStorageType": mscVrIpStaticRouteNhStorageType,
       "mscVrIpStaticRouteNhIndex": mscVrIpStaticRouteNhIndex,
       "mscVrIpStaticRouteNhProvTable": mscVrIpStaticRouteNhProvTable,
       "mscVrIpStaticRouteNhProvEntry": mscVrIpStaticRouteNhProvEntry,
       "mscVrIpStaticRouteNhMetric": mscVrIpStaticRouteNhMetric,
       "mscVrIpStaticRouteProvTable": mscVrIpStaticRouteProvTable,
       "mscVrIpStaticRouteProvEntry": mscVrIpStaticRouteProvEntry,
       "mscVrIpStaticRoutePreferredOver": mscVrIpStaticRoutePreferredOver,
       "mscVrIpStaticDiscard": mscVrIpStaticDiscard,
       "mscVrIpStaticDiscardRowStatusTable": mscVrIpStaticDiscardRowStatusTable,
       "mscVrIpStaticDiscardRowStatusEntry": mscVrIpStaticDiscardRowStatusEntry,
       "mscVrIpStaticDiscardRowStatus": mscVrIpStaticDiscardRowStatus,
       "mscVrIpStaticDiscardComponentName": mscVrIpStaticDiscardComponentName,
       "mscVrIpStaticDiscardStorageType": mscVrIpStaticDiscardStorageType,
       "mscVrIpStaticDiscardDestAddressIndex": mscVrIpStaticDiscardDestAddressIndex,
       "mscVrIpStaticDiscardDestMaskIndex": mscVrIpStaticDiscardDestMaskIndex,
       "mscVrIpStaticStateTable": mscVrIpStaticStateTable,
       "mscVrIpStaticStateEntry": mscVrIpStaticStateEntry,
       "mscVrIpStaticAdminState": mscVrIpStaticAdminState,
       "mscVrIpStaticOperationalState": mscVrIpStaticOperationalState,
       "mscVrIpStaticUsageState": mscVrIpStaticUsageState,
       "mscVrIpNs": mscVrIpNs,
       "mscVrIpNsRowStatusTable": mscVrIpNsRowStatusTable,
       "mscVrIpNsRowStatusEntry": mscVrIpNsRowStatusEntry,
       "mscVrIpNsRowStatus": mscVrIpNsRowStatus,
       "mscVrIpNsComponentName": mscVrIpNsComponentName,
       "mscVrIpNsStorageType": mscVrIpNsStorageType,
       "mscVrIpNsIndex": mscVrIpNsIndex,
       "mscVrIpNsApply": mscVrIpNsApply,
       "mscVrIpNsApplyRowStatusTable": mscVrIpNsApplyRowStatusTable,
       "mscVrIpNsApplyRowStatusEntry": mscVrIpNsApplyRowStatusEntry,
       "mscVrIpNsApplyRowStatus": mscVrIpNsApplyRowStatus,
       "mscVrIpNsApplyComponentName": mscVrIpNsApplyComponentName,
       "mscVrIpNsApplyStorageType": mscVrIpNsApplyStorageType,
       "mscVrIpNsApplyIndex": mscVrIpNsApplyIndex,
       "mscVrIpNsApplyProvisionedTable": mscVrIpNsApplyProvisionedTable,
       "mscVrIpNsApplyProvisionedEntry": mscVrIpNsApplyProvisionedEntry,
       "mscVrIpNsApplyFilter": mscVrIpNsApplyFilter,
       "mscVrIpNsApplyIpAddress1": mscVrIpNsApplyIpAddress1,
       "mscVrIpNsApplyIpMask1": mscVrIpNsApplyIpMask1,
       "mscVrIpNsApplyIpAddress2": mscVrIpNsApplyIpAddress2,
       "mscVrIpNsApplyIpMask2": mscVrIpNsApplyIpMask2,
       "mscVrIpNsApplyDirection": mscVrIpNsApplyDirection,
       "mscVrIpNsProvTable": mscVrIpNsProvTable,
       "mscVrIpNsProvEntry": mscVrIpNsProvEntry,
       "mscVrIpNsFirstFilter": mscVrIpNsFirstFilter,
       "mscVrIpNsLocalInFilter": mscVrIpNsLocalInFilter,
       "mscVrIpNsLocalOutFilter": mscVrIpNsLocalOutFilter,
       "mscVrIpNsLastFilter": mscVrIpNsLastFilter,
       "mscVrIpArp": mscVrIpArp,
       "mscVrIpArpRowStatusTable": mscVrIpArpRowStatusTable,
       "mscVrIpArpRowStatusEntry": mscVrIpArpRowStatusEntry,
       "mscVrIpArpRowStatus": mscVrIpArpRowStatus,
       "mscVrIpArpComponentName": mscVrIpArpComponentName,
       "mscVrIpArpStorageType": mscVrIpArpStorageType,
       "mscVrIpArpIndex": mscVrIpArpIndex,
       "mscVrIpArpHost": mscVrIpArpHost,
       "mscVrIpArpHostRowStatusTable": mscVrIpArpHostRowStatusTable,
       "mscVrIpArpHostRowStatusEntry": mscVrIpArpHostRowStatusEntry,
       "mscVrIpArpHostRowStatus": mscVrIpArpHostRowStatus,
       "mscVrIpArpHostComponentName": mscVrIpArpHostComponentName,
       "mscVrIpArpHostStorageType": mscVrIpArpHostStorageType,
       "mscVrIpArpHostHostAddressIndex": mscVrIpArpHostHostAddressIndex,
       "mscVrIpArpHostProvTable": mscVrIpArpHostProvTable,
       "mscVrIpArpHostProvEntry": mscVrIpArpHostProvEntry,
       "mscVrIpArpHostPhysAddress": mscVrIpArpHostPhysAddress,
       "mscVrIpArpHostMaxTxUnit": mscVrIpArpHostMaxTxUnit,
       "mscVrIpArpHostPermanentVirtualCircuitNumber": mscVrIpArpHostPermanentVirtualCircuitNumber,
       "mscVrIpArpHostTunnelDestinationAddress": mscVrIpArpHostTunnelDestinationAddress,
       "mscVrIpArpHostEncap": mscVrIpArpHostEncap,
       "mscVrIpArpHostOperTable": mscVrIpArpHostOperTable,
       "mscVrIpArpHostOperEntry": mscVrIpArpHostOperEntry,
       "mscVrIpArpHostOperMaxTxUnit": mscVrIpArpHostOperMaxTxUnit,
       "mscVrIpArpHostOperEncap": mscVrIpArpHostOperEncap,
       "mscVrIpArpDynHost": mscVrIpArpDynHost,
       "mscVrIpArpDynHostRowStatusTable": mscVrIpArpDynHostRowStatusTable,
       "mscVrIpArpDynHostRowStatusEntry": mscVrIpArpDynHostRowStatusEntry,
       "mscVrIpArpDynHostRowStatus": mscVrIpArpDynHostRowStatus,
       "mscVrIpArpDynHostComponentName": mscVrIpArpDynHostComponentName,
       "mscVrIpArpDynHostStorageType": mscVrIpArpDynHostStorageType,
       "mscVrIpArpDynHostHostAddressIndex": mscVrIpArpDynHostHostAddressIndex,
       "mscVrIpArpDynHostCosIndex": mscVrIpArpDynHostCosIndex,
       "mscVrIpArpDynHostOperTable": mscVrIpArpDynHostOperTable,
       "mscVrIpArpDynHostOperEntry": mscVrIpArpDynHostOperEntry,
       "mscVrIpArpDynHostPhysAddress": mscVrIpArpDynHostPhysAddress,
       "mscVrIpArpDynHostMaxTxUnit": mscVrIpArpDynHostMaxTxUnit,
       "mscVrIpArpDynHostEncapsulationType": mscVrIpArpDynHostEncapsulationType,
       "mscVrIpArpDynHostPermanentVirtualCircuitNumber": mscVrIpArpDynHostPermanentVirtualCircuitNumber,
       "mscVrIpArpDynHostIfIndex": mscVrIpArpDynHostIfIndex,
       "mscVrIpArpDynHostType": mscVrIpArpDynHostType,
       "mscVrIpArpDynHostNcPhysAddress": mscVrIpArpDynHostNcPhysAddress,
       "mscVrIpArpDynHostTunnelDestinationAddress": mscVrIpArpDynHostTunnelDestinationAddress,
       "mscVrIpArpProvTable": mscVrIpArpProvTable,
       "mscVrIpArpProvEntry": mscVrIpArpProvEntry,
       "mscVrIpArpAutoRefresh": mscVrIpArpAutoRefresh,
       "mscVrIpArpAutoRefreshTimeout": mscVrIpArpAutoRefreshTimeout,
       "mscVrIpIcmp": mscVrIpIcmp,
       "mscVrIpIcmpRowStatusTable": mscVrIpIcmpRowStatusTable,
       "mscVrIpIcmpRowStatusEntry": mscVrIpIcmpRowStatusEntry,
       "mscVrIpIcmpRowStatus": mscVrIpIcmpRowStatus,
       "mscVrIpIcmpComponentName": mscVrIpIcmpComponentName,
       "mscVrIpIcmpStorageType": mscVrIpIcmpStorageType,
       "mscVrIpIcmpIndex": mscVrIpIcmpIndex,
       "mscVrIpIcmpProvTable": mscVrIpIcmpProvTable,
       "mscVrIpIcmpProvEntry": mscVrIpIcmpProvEntry,
       "mscVrIpIcmpSendRedirect": mscVrIpIcmpSendRedirect,
       "mscVrIpIcmpSendHostUnreachable": mscVrIpIcmpSendHostUnreachable,
       "mscVrIpIcmpStatsTable": mscVrIpIcmpStatsTable,
       "mscVrIpIcmpStatsEntry": mscVrIpIcmpStatsEntry,
       "mscVrIpIcmpInMsgs": mscVrIpIcmpInMsgs,
       "mscVrIpIcmpInErrors": mscVrIpIcmpInErrors,
       "mscVrIpIcmpInDestUnreachs": mscVrIpIcmpInDestUnreachs,
       "mscVrIpIcmpInTimeExcds": mscVrIpIcmpInTimeExcds,
       "mscVrIpIcmpInParmProbs": mscVrIpIcmpInParmProbs,
       "mscVrIpIcmpInSrcQuenchs": mscVrIpIcmpInSrcQuenchs,
       "mscVrIpIcmpInRedirects": mscVrIpIcmpInRedirects,
       "mscVrIpIcmpInEchos": mscVrIpIcmpInEchos,
       "mscVrIpIcmpInEchoReps": mscVrIpIcmpInEchoReps,
       "mscVrIpIcmpInTimestamps": mscVrIpIcmpInTimestamps,
       "mscVrIpIcmpInTimestampReps": mscVrIpIcmpInTimestampReps,
       "mscVrIpIcmpInAddrMasks": mscVrIpIcmpInAddrMasks,
       "mscVrIpIcmpInAddrMaskReps": mscVrIpIcmpInAddrMaskReps,
       "mscVrIpIcmpOutMsgs": mscVrIpIcmpOutMsgs,
       "mscVrIpIcmpOutErrors": mscVrIpIcmpOutErrors,
       "mscVrIpIcmpOutDestUnreachs": mscVrIpIcmpOutDestUnreachs,
       "mscVrIpIcmpOutTimeExcds": mscVrIpIcmpOutTimeExcds,
       "mscVrIpIcmpOutParmProbs": mscVrIpIcmpOutParmProbs,
       "mscVrIpIcmpOutSrcQuenchs": mscVrIpIcmpOutSrcQuenchs,
       "mscVrIpIcmpOutRedirects": mscVrIpIcmpOutRedirects,
       "mscVrIpIcmpOutEchos": mscVrIpIcmpOutEchos,
       "mscVrIpIcmpOutEchoReps": mscVrIpIcmpOutEchoReps,
       "mscVrIpIcmpOutTimestamps": mscVrIpIcmpOutTimestamps,
       "mscVrIpIcmpOutTimestampReps": mscVrIpIcmpOutTimestampReps,
       "mscVrIpIcmpOutAddrMasks": mscVrIpIcmpOutAddrMasks,
       "mscVrIpIcmpOutAddrMaskReps": mscVrIpIcmpOutAddrMaskReps,
       "mscVrIpIcmpInRtrAdvs": mscVrIpIcmpInRtrAdvs,
       "mscVrIpIcmpInRtrSolicits": mscVrIpIcmpInRtrSolicits,
       "mscVrIpIcmpOutRtrAdvs": mscVrIpIcmpOutRtrAdvs,
       "mscVrIpIcmpOutRtrSolicits": mscVrIpIcmpOutRtrSolicits,
       "mscVrIpRelayBC": mscVrIpRelayBC,
       "mscVrIpRelayBCRowStatusTable": mscVrIpRelayBCRowStatusTable,
       "mscVrIpRelayBCRowStatusEntry": mscVrIpRelayBCRowStatusEntry,
       "mscVrIpRelayBCRowStatus": mscVrIpRelayBCRowStatus,
       "mscVrIpRelayBCComponentName": mscVrIpRelayBCComponentName,
       "mscVrIpRelayBCStorageType": mscVrIpRelayBCStorageType,
       "mscVrIpRelayBCIndex": mscVrIpRelayBCIndex,
       "mscVrIpRelayBCPort": mscVrIpRelayBCPort,
       "mscVrIpRelayBCPortRowStatusTable": mscVrIpRelayBCPortRowStatusTable,
       "mscVrIpRelayBCPortRowStatusEntry": mscVrIpRelayBCPortRowStatusEntry,
       "mscVrIpRelayBCPortRowStatus": mscVrIpRelayBCPortRowStatus,
       "mscVrIpRelayBCPortComponentName": mscVrIpRelayBCPortComponentName,
       "mscVrIpRelayBCPortStorageType": mscVrIpRelayBCPortStorageType,
       "mscVrIpRelayBCPortPortNumIndex": mscVrIpRelayBCPortPortNumIndex,
       "mscVrIpRelayBCPortOperTable": mscVrIpRelayBCPortOperTable,
       "mscVrIpRelayBCPortOperEntry": mscVrIpRelayBCPortOperEntry,
       "mscVrIpRelayBCPortRelayBcUdpCount": mscVrIpRelayBCPortRelayBcUdpCount,
       "mscVrIpRelayBCProvTable": mscVrIpRelayBCProvTable,
       "mscVrIpRelayBCProvEntry": mscVrIpRelayBCProvEntry,
       "mscVrIpRelayBCRelayStatus": mscVrIpRelayBCRelayStatus,
       "mscVrIpRelayBCRelayNdStatus": mscVrIpRelayBCRelayNdStatus,
       "mscVrIpRelayBCOperTable": mscVrIpRelayBCOperTable,
       "mscVrIpRelayBCOperEntry": mscVrIpRelayBCOperEntry,
       "mscVrIpRelayBCRelayNdCount": mscVrIpRelayBCRelayNdCount,
       "mscVrIpUdp": mscVrIpUdp,
       "mscVrIpUdpRowStatusTable": mscVrIpUdpRowStatusTable,
       "mscVrIpUdpRowStatusEntry": mscVrIpUdpRowStatusEntry,
       "mscVrIpUdpRowStatus": mscVrIpUdpRowStatus,
       "mscVrIpUdpComponentName": mscVrIpUdpComponentName,
       "mscVrIpUdpStorageType": mscVrIpUdpStorageType,
       "mscVrIpUdpIndex": mscVrIpUdpIndex,
       "mscVrIpUdpListenEntry": mscVrIpUdpListenEntry,
       "mscVrIpUdpListenEntryRowStatusTable": mscVrIpUdpListenEntryRowStatusTable,
       "mscVrIpUdpListenEntryRowStatusEntry": mscVrIpUdpListenEntryRowStatusEntry,
       "mscVrIpUdpListenEntryRowStatus": mscVrIpUdpListenEntryRowStatus,
       "mscVrIpUdpListenEntryComponentName": mscVrIpUdpListenEntryComponentName,
       "mscVrIpUdpListenEntryStorageType": mscVrIpUdpListenEntryStorageType,
       "mscVrIpUdpListenEntryLocalAddressIndex": mscVrIpUdpListenEntryLocalAddressIndex,
       "mscVrIpUdpListenEntryLocalPortIndex": mscVrIpUdpListenEntryLocalPortIndex,
       "mscVrIpUdpStatsTable": mscVrIpUdpStatsTable,
       "mscVrIpUdpStatsEntry": mscVrIpUdpStatsEntry,
       "mscVrIpUdpInDatagrams": mscVrIpUdpInDatagrams,
       "mscVrIpUdpNoPorts": mscVrIpUdpNoPorts,
       "mscVrIpUdpInErrors": mscVrIpUdpInErrors,
       "mscVrIpUdpOutDatagrams": mscVrIpUdpOutDatagrams,
       "mscVrIpTcp": mscVrIpTcp,
       "mscVrIpTcpRowStatusTable": mscVrIpTcpRowStatusTable,
       "mscVrIpTcpRowStatusEntry": mscVrIpTcpRowStatusEntry,
       "mscVrIpTcpRowStatus": mscVrIpTcpRowStatus,
       "mscVrIpTcpComponentName": mscVrIpTcpComponentName,
       "mscVrIpTcpStorageType": mscVrIpTcpStorageType,
       "mscVrIpTcpIndex": mscVrIpTcpIndex,
       "mscVrIpTcpTcpEntry": mscVrIpTcpTcpEntry,
       "mscVrIpTcpTcpEntryRowStatusTable": mscVrIpTcpTcpEntryRowStatusTable,
       "mscVrIpTcpTcpEntryRowStatusEntry": mscVrIpTcpTcpEntryRowStatusEntry,
       "mscVrIpTcpTcpEntryRowStatus": mscVrIpTcpTcpEntryRowStatus,
       "mscVrIpTcpTcpEntryComponentName": mscVrIpTcpTcpEntryComponentName,
       "mscVrIpTcpTcpEntryStorageType": mscVrIpTcpTcpEntryStorageType,
       "mscVrIpTcpTcpEntryLocalAddressIndex": mscVrIpTcpTcpEntryLocalAddressIndex,
       "mscVrIpTcpTcpEntryLocalPortIndex": mscVrIpTcpTcpEntryLocalPortIndex,
       "mscVrIpTcpTcpEntryRemoteAddressIndex": mscVrIpTcpTcpEntryRemoteAddressIndex,
       "mscVrIpTcpTcpEntryRemotePortIndex": mscVrIpTcpTcpEntryRemotePortIndex,
       "mscVrIpTcpTcpEntryOperTable": mscVrIpTcpTcpEntryOperTable,
       "mscVrIpTcpTcpEntryOperEntry": mscVrIpTcpTcpEntryOperEntry,
       "mscVrIpTcpTcpEntryState": mscVrIpTcpTcpEntryState,
       "mscVrIpTcpStatsTable": mscVrIpTcpStatsTable,
       "mscVrIpTcpStatsEntry": mscVrIpTcpStatsEntry,
       "mscVrIpTcpRToAlgorithm": mscVrIpTcpRToAlgorithm,
       "mscVrIpTcpRToMin": mscVrIpTcpRToMin,
       "mscVrIpTcpRToMax": mscVrIpTcpRToMax,
       "mscVrIpTcpMaxConn": mscVrIpTcpMaxConn,
       "mscVrIpTcpActiveOpens": mscVrIpTcpActiveOpens,
       "mscVrIpTcpPassiveOpens": mscVrIpTcpPassiveOpens,
       "mscVrIpTcpAttemptFails": mscVrIpTcpAttemptFails,
       "mscVrIpTcpEstabResets": mscVrIpTcpEstabResets,
       "mscVrIpTcpCurrEstab": mscVrIpTcpCurrEstab,
       "mscVrIpTcpInSegs": mscVrIpTcpInSegs,
       "mscVrIpTcpOutSegs": mscVrIpTcpOutSegs,
       "mscVrIpTcpRetransSegs": mscVrIpTcpRetransSegs,
       "mscVrIpTcpInErrs": mscVrIpTcpInErrs,
       "mscVrIpTcpOutRsts": mscVrIpTcpOutRsts,
       "mscVrIpBootp": mscVrIpBootp,
       "mscVrIpBootpRowStatusTable": mscVrIpBootpRowStatusTable,
       "mscVrIpBootpRowStatusEntry": mscVrIpBootpRowStatusEntry,
       "mscVrIpBootpRowStatus": mscVrIpBootpRowStatus,
       "mscVrIpBootpComponentName": mscVrIpBootpComponentName,
       "mscVrIpBootpStorageType": mscVrIpBootpStorageType,
       "mscVrIpBootpIndex": mscVrIpBootpIndex,
       "mscVrIpBootpPpE": mscVrIpBootpPpE,
       "mscVrIpBootpPpERowStatusTable": mscVrIpBootpPpERowStatusTable,
       "mscVrIpBootpPpERowStatusEntry": mscVrIpBootpPpERowStatusEntry,
       "mscVrIpBootpPpERowStatus": mscVrIpBootpPpERowStatus,
       "mscVrIpBootpPpEComponentName": mscVrIpBootpPpEComponentName,
       "mscVrIpBootpPpEStorageType": mscVrIpBootpPpEStorageType,
       "mscVrIpBootpPpEIndex": mscVrIpBootpPpEIndex,
       "mscVrIpBootpPpEOperTable": mscVrIpBootpPpEOperTable,
       "mscVrIpBootpPpEOperEntry": mscVrIpBootpPpEOperEntry,
       "mscVrIpBootpPpEStatus": mscVrIpBootpPpEStatus,
       "mscVrIpBootpPpEStatsTable": mscVrIpBootpPpEStatsTable,
       "mscVrIpBootpPpEStatsEntry": mscVrIpBootpPpEStatsEntry,
       "mscVrIpBootpPpEInRequests": mscVrIpBootpPpEInRequests,
       "mscVrIpBootpPpEInReplies": mscVrIpBootpPpEInReplies,
       "mscVrIpBootpPpEOutRequests": mscVrIpBootpPpEOutRequests,
       "mscVrIpBootpPpEOutReplies": mscVrIpBootpPpEOutReplies,
       "mscVrIpBootpPpEInRequestErrors": mscVrIpBootpPpEInRequestErrors,
       "mscVrIpBootpPpEInReplyErrors": mscVrIpBootpPpEInReplyErrors,
       "mscVrIpBootpAdminControlTable": mscVrIpBootpAdminControlTable,
       "mscVrIpBootpAdminControlEntry": mscVrIpBootpAdminControlEntry,
       "mscVrIpBootpSnmpAdminStatus": mscVrIpBootpSnmpAdminStatus,
       "mscVrIpBootpProvTable": mscVrIpBootpProvTable,
       "mscVrIpBootpProvEntry": mscVrIpBootpProvEntry,
       "mscVrIpBootpHopDiscardThreshold": mscVrIpBootpHopDiscardThreshold,
       "mscVrIpBootpStateTable": mscVrIpBootpStateTable,
       "mscVrIpBootpStateEntry": mscVrIpBootpStateEntry,
       "mscVrIpBootpAdminState": mscVrIpBootpAdminState,
       "mscVrIpBootpOperationalState": mscVrIpBootpOperationalState,
       "mscVrIpBootpUsageState": mscVrIpBootpUsageState,
       "mscVrIpBootpOperStatusTable": mscVrIpBootpOperStatusTable,
       "mscVrIpBootpOperStatusEntry": mscVrIpBootpOperStatusEntry,
       "mscVrIpBootpSnmpOperStatus": mscVrIpBootpSnmpOperStatus,
       "mscVrIpCache": mscVrIpCache,
       "mscVrIpCacheRowStatusTable": mscVrIpCacheRowStatusTable,
       "mscVrIpCacheRowStatusEntry": mscVrIpCacheRowStatusEntry,
       "mscVrIpCacheRowStatus": mscVrIpCacheRowStatus,
       "mscVrIpCacheComponentName": mscVrIpCacheComponentName,
       "mscVrIpCacheStorageType": mscVrIpCacheStorageType,
       "mscVrIpCacheIndex": mscVrIpCacheIndex,
       "mscVrIpCacheStateTable": mscVrIpCacheStateTable,
       "mscVrIpCacheStateEntry": mscVrIpCacheStateEntry,
       "mscVrIpCacheAdminState": mscVrIpCacheAdminState,
       "mscVrIpCacheOperationalState": mscVrIpCacheOperationalState,
       "mscVrIpCacheUsageState": mscVrIpCacheUsageState,
       "mscVrIpCacheOperTable": mscVrIpCacheOperTable,
       "mscVrIpCacheOperEntry": mscVrIpCacheOperEntry,
       "mscVrIpCacheEntriesFree": mscVrIpCacheEntriesFree,
       "mscVrIpCacheTotalLookups": mscVrIpCacheTotalLookups,
       "mscVrIpCacheLookupMisses": mscVrIpCacheLookupMisses,
       "mscVrIpCacheCacheTableMaxEntries": mscVrIpCacheCacheTableMaxEntries,
       "mscVrIpTunnel": mscVrIpTunnel,
       "mscVrIpTunnelRowStatusTable": mscVrIpTunnelRowStatusTable,
       "mscVrIpTunnelRowStatusEntry": mscVrIpTunnelRowStatusEntry,
       "mscVrIpTunnelRowStatus": mscVrIpTunnelRowStatus,
       "mscVrIpTunnelComponentName": mscVrIpTunnelComponentName,
       "mscVrIpTunnelStorageType": mscVrIpTunnelStorageType,
       "mscVrIpTunnelIndex": mscVrIpTunnelIndex,
       "mscVrIpTunnelSep": mscVrIpTunnelSep,
       "mscVrIpTunnelSepRowStatusTable": mscVrIpTunnelSepRowStatusTable,
       "mscVrIpTunnelSepRowStatusEntry": mscVrIpTunnelSepRowStatusEntry,
       "mscVrIpTunnelSepRowStatus": mscVrIpTunnelSepRowStatus,
       "mscVrIpTunnelSepComponentName": mscVrIpTunnelSepComponentName,
       "mscVrIpTunnelSepStorageType": mscVrIpTunnelSepStorageType,
       "mscVrIpTunnelSepIndex": mscVrIpTunnelSepIndex,
       "mscVrIpTunnelSepIfEntryTable": mscVrIpTunnelSepIfEntryTable,
       "mscVrIpTunnelSepIfEntryEntry": mscVrIpTunnelSepIfEntryEntry,
       "mscVrIpTunnelSepIfAdminStatus": mscVrIpTunnelSepIfAdminStatus,
       "mscVrIpTunnelSepIfIndex": mscVrIpTunnelSepIfIndex,
       "mscVrIpTunnelSepMpTable": mscVrIpTunnelSepMpTable,
       "mscVrIpTunnelSepMpEntry": mscVrIpTunnelSepMpEntry,
       "mscVrIpTunnelSepLinkToProtocolPort": mscVrIpTunnelSepLinkToProtocolPort,
       "mscVrIpTunnelSepProvTable": mscVrIpTunnelSepProvTable,
       "mscVrIpTunnelSepProvEntry": mscVrIpTunnelSepProvEntry,
       "mscVrIpTunnelSepEncapType": mscVrIpTunnelSepEncapType,
       "mscVrIpTunnelSepSourceAddress": mscVrIpTunnelSepSourceAddress,
       "mscVrIpTunnelSepDestinationAddress": mscVrIpTunnelSepDestinationAddress,
       "mscVrIpTunnelSepOperTable": mscVrIpTunnelSepOperTable,
       "mscVrIpTunnelSepOperEntry": mscVrIpTunnelSepOperEntry,
       "mscVrIpTunnelSepDiscoveredPathMtu": mscVrIpTunnelSepDiscoveredPathMtu,
       "mscVrIpTunnelMsep": mscVrIpTunnelMsep,
       "mscVrIpTunnelMsepRowStatusTable": mscVrIpTunnelMsepRowStatusTable,
       "mscVrIpTunnelMsepRowStatusEntry": mscVrIpTunnelMsepRowStatusEntry,
       "mscVrIpTunnelMsepRowStatus": mscVrIpTunnelMsepRowStatus,
       "mscVrIpTunnelMsepComponentName": mscVrIpTunnelMsepComponentName,
       "mscVrIpTunnelMsepStorageType": mscVrIpTunnelMsepStorageType,
       "mscVrIpTunnelMsepIndex": mscVrIpTunnelMsepIndex,
       "mscVrIpTunnelMsepIfEntryTable": mscVrIpTunnelMsepIfEntryTable,
       "mscVrIpTunnelMsepIfEntryEntry": mscVrIpTunnelMsepIfEntryEntry,
       "mscVrIpTunnelMsepIfAdminStatus": mscVrIpTunnelMsepIfAdminStatus,
       "mscVrIpTunnelMsepIfIndex": mscVrIpTunnelMsepIfIndex,
       "mscVrIpTunnelMsepMpTable": mscVrIpTunnelMsepMpTable,
       "mscVrIpTunnelMsepMpEntry": mscVrIpTunnelMsepMpEntry,
       "mscVrIpTunnelMsepLinkToProtocolPort": mscVrIpTunnelMsepLinkToProtocolPort,
       "mscVrIpTunnelMsepProvTable": mscVrIpTunnelMsepProvTable,
       "mscVrIpTunnelMsepProvEntry": mscVrIpTunnelMsepProvEntry,
       "mscVrIpTunnelMsepPathMtu": mscVrIpTunnelMsepPathMtu,
       "mscVrIpTunnelMsepEncapType": mscVrIpTunnelMsepEncapType,
       "mscVrIpTunnelMsepSharedDomainVirtualRouter": mscVrIpTunnelMsepSharedDomainVirtualRouter,
       "mscVrIpTunnelMsepSourceAddress": mscVrIpTunnelMsepSourceAddress,
       "mscVrIpTunnelMsepDstTable": mscVrIpTunnelMsepDstTable,
       "mscVrIpTunnelMsepDstEntry": mscVrIpTunnelMsepDstEntry,
       "mscVrIpTunnelMsepDstValue": mscVrIpTunnelMsepDstValue,
       "mscVrIpTunnelMsepDstRowStatus": mscVrIpTunnelMsepDstRowStatus,
       "mscVrIpTunnelStateTable": mscVrIpTunnelStateTable,
       "mscVrIpTunnelStateEntry": mscVrIpTunnelStateEntry,
       "mscVrIpTunnelAdminState": mscVrIpTunnelAdminState,
       "mscVrIpTunnelOperationalState": mscVrIpTunnelOperationalState,
       "mscVrIpTunnelUsageState": mscVrIpTunnelUsageState,
       "mscVrIpProvTable": mscVrIpProvTable,
       "mscVrIpProvEntry": mscVrIpProvEntry,
       "mscVrIpForwarding": mscVrIpForwarding,
       "mscVrIpDefaultTtl": mscVrIpDefaultTtl,
       "mscVrIpCosPolicyAssignment": mscVrIpCosPolicyAssignment,
       "mscVrIpStatsTable": mscVrIpStatsTable,
       "mscVrIpStatsEntry": mscVrIpStatsEntry,
       "mscVrIpInReceives": mscVrIpInReceives,
       "mscVrIpInHdrErrors": mscVrIpInHdrErrors,
       "mscVrIpInAddrErrors": mscVrIpInAddrErrors,
       "mscVrIpForwDatagrams": mscVrIpForwDatagrams,
       "mscVrIpInUnknownProtos": mscVrIpInUnknownProtos,
       "mscVrIpInDiscards": mscVrIpInDiscards,
       "mscVrIpInDelivers": mscVrIpInDelivers,
       "mscVrIpOutRequests": mscVrIpOutRequests,
       "mscVrIpOutDiscards": mscVrIpOutDiscards,
       "mscVrIpOutNoRoutes": mscVrIpOutNoRoutes,
       "mscVrIpReasmTimeOut": mscVrIpReasmTimeOut,
       "mscVrIpReasmReqds": mscVrIpReasmReqds,
       "mscVrIpReasmOks": mscVrIpReasmOks,
       "mscVrIpReasmFails": mscVrIpReasmFails,
       "mscVrIpFragOks": mscVrIpFragOks,
       "mscVrIpFragFails": mscVrIpFragFails,
       "mscVrIpFragCreates": mscVrIpFragCreates,
       "mscVrIpRoutingDiscards": mscVrIpRoutingDiscards,
       "mscVrIpAdminControlTable": mscVrIpAdminControlTable,
       "mscVrIpAdminControlEntry": mscVrIpAdminControlEntry,
       "mscVrIpSnmpAdminStatus": mscVrIpSnmpAdminStatus,
       "mscVrIpStateTable": mscVrIpStateTable,
       "mscVrIpStateEntry": mscVrIpStateEntry,
       "mscVrIpAdminState": mscVrIpAdminState,
       "mscVrIpOperationalState": mscVrIpOperationalState,
       "mscVrIpUsageState": mscVrIpUsageState,
       "mscVrIpOperStatusTable": mscVrIpOperStatusTable,
       "mscVrIpOperStatusEntry": mscVrIpOperStatusEntry,
       "mscVrIpSnmpOperStatus": mscVrIpSnmpOperStatus,
       "mscVrIpCtsTable": mscVrIpCtsTable,
       "mscVrIpCtsEntry": mscVrIpCtsEntry,
       "mscVrIpCtsIndex": mscVrIpCtsIndex,
       "mscVrIpCtsValue": mscVrIpCtsValue,
       "ipMIB": ipMIB,
       "ipGroup": ipGroup,
       "ipGroupCA": ipGroupCA,
       "ipGroupCA02": ipGroupCA02,
       "ipGroupCA02A": ipGroupCA02A,
       "ipCapabilities": ipCapabilities,
       "ipCapabilitiesCA": ipCapabilitiesCA,
       "ipCapabilitiesCA02": ipCapabilitiesCA02,
       "ipCapabilitiesCA02A": ipCapabilitiesCA02A}
)
