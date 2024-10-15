# SNMP MIB module (Nortel-Magellan-Passport-IpNhrpMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-IpNhrpMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:59 2024
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
 vrIpIndex,
 vrPpIpPortIndex,
 vrPpIpPortLogicalIf,
 vrPpIpPortLogicalIfAddressIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-IpMIB",
    "vrIp",
    "vrIpIndex",
    "vrPpIpPortIndex",
    "vrPpIpPortLogicalIf",
    "vrPpIpPortLogicalIfAddressIndex")

(Counter32,
 DisplayString,
 Integer32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(HexString,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "HexString",
    "NonReplicated")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "passportMIBs")

(vrIndex,
 vrPpIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-VirtualRouterMIB",
    "vrIndex",
    "vrPpIndex")

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

_VrPpIpPortLogicalIfNhrpIf_ObjectIdentity = ObjectIdentity
vrPpIpPortLogicalIfNhrpIf = _VrPpIpPortLogicalIfNhrpIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 4)
)
_VrPpIpPortLogicalIfNhrpIfRowStatusTable_Object = MibTable
vrPpIpPortLogicalIfNhrpIfRowStatusTable = _VrPpIpPortLogicalIfNhrpIfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 4, 1)
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfNhrpIfRowStatusTable.setStatus("mandatory")
_VrPpIpPortLogicalIfNhrpIfRowStatusEntry_Object = MibTableRow
vrPpIpPortLogicalIfNhrpIfRowStatusEntry = _VrPpIpPortLogicalIfNhrpIfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 4, 1, 1)
)
vrPpIpPortLogicalIfNhrpIfRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrPpIpPortLogicalIfNhrpIfIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfNhrpIfRowStatusEntry.setStatus("mandatory")
_VrPpIpPortLogicalIfNhrpIfRowStatus_Type = RowStatus
_VrPpIpPortLogicalIfNhrpIfRowStatus_Object = MibTableColumn
vrPpIpPortLogicalIfNhrpIfRowStatus = _VrPpIpPortLogicalIfNhrpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 4, 1, 1, 1),
    _VrPpIpPortLogicalIfNhrpIfRowStatus_Type()
)
vrPpIpPortLogicalIfNhrpIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfNhrpIfRowStatus.setStatus("mandatory")
_VrPpIpPortLogicalIfNhrpIfComponentName_Type = DisplayString
_VrPpIpPortLogicalIfNhrpIfComponentName_Object = MibTableColumn
vrPpIpPortLogicalIfNhrpIfComponentName = _VrPpIpPortLogicalIfNhrpIfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 4, 1, 1, 2),
    _VrPpIpPortLogicalIfNhrpIfComponentName_Type()
)
vrPpIpPortLogicalIfNhrpIfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfNhrpIfComponentName.setStatus("mandatory")
_VrPpIpPortLogicalIfNhrpIfStorageType_Type = StorageType
_VrPpIpPortLogicalIfNhrpIfStorageType_Object = MibTableColumn
vrPpIpPortLogicalIfNhrpIfStorageType = _VrPpIpPortLogicalIfNhrpIfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 4, 1, 1, 4),
    _VrPpIpPortLogicalIfNhrpIfStorageType_Type()
)
vrPpIpPortLogicalIfNhrpIfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfNhrpIfStorageType.setStatus("mandatory")
_VrPpIpPortLogicalIfNhrpIfIndex_Type = NonReplicated
_VrPpIpPortLogicalIfNhrpIfIndex_Object = MibTableColumn
vrPpIpPortLogicalIfNhrpIfIndex = _VrPpIpPortLogicalIfNhrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 4, 1, 1, 10),
    _VrPpIpPortLogicalIfNhrpIfIndex_Type()
)
vrPpIpPortLogicalIfNhrpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfNhrpIfIndex.setStatus("mandatory")
_VrIpNhrp_ObjectIdentity = ObjectIdentity
vrIpNhrp = _VrIpNhrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19)
)
_VrIpNhrpRowStatusTable_Object = MibTable
vrIpNhrpRowStatusTable = _VrIpNhrpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 1)
)
if mibBuilder.loadTexts:
    vrIpNhrpRowStatusTable.setStatus("mandatory")
_VrIpNhrpRowStatusEntry_Object = MibTableRow
vrIpNhrpRowStatusEntry = _VrIpNhrpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 1, 1)
)
vrIpNhrpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpIndex"),
)
if mibBuilder.loadTexts:
    vrIpNhrpRowStatusEntry.setStatus("mandatory")
_VrIpNhrpRowStatus_Type = RowStatus
_VrIpNhrpRowStatus_Object = MibTableColumn
vrIpNhrpRowStatus = _VrIpNhrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 1, 1, 1),
    _VrIpNhrpRowStatus_Type()
)
vrIpNhrpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNhrpRowStatus.setStatus("mandatory")
_VrIpNhrpComponentName_Type = DisplayString
_VrIpNhrpComponentName_Object = MibTableColumn
vrIpNhrpComponentName = _VrIpNhrpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 1, 1, 2),
    _VrIpNhrpComponentName_Type()
)
vrIpNhrpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpComponentName.setStatus("mandatory")
_VrIpNhrpStorageType_Type = StorageType
_VrIpNhrpStorageType_Object = MibTableColumn
vrIpNhrpStorageType = _VrIpNhrpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 1, 1, 4),
    _VrIpNhrpStorageType_Type()
)
vrIpNhrpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpStorageType.setStatus("mandatory")
_VrIpNhrpIndex_Type = NonReplicated
_VrIpNhrpIndex_Object = MibTableColumn
vrIpNhrpIndex = _VrIpNhrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 1, 1, 10),
    _VrIpNhrpIndex_Type()
)
vrIpNhrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpNhrpIndex.setStatus("mandatory")
_VrIpNhrpNhs_ObjectIdentity = ObjectIdentity
vrIpNhrpNhs = _VrIpNhrpNhs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2)
)
_VrIpNhrpNhsRowStatusTable_Object = MibTable
vrIpNhrpNhsRowStatusTable = _VrIpNhrpNhsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpNhrpNhsRowStatusTable.setStatus("mandatory")
_VrIpNhrpNhsRowStatusEntry_Object = MibTableRow
vrIpNhrpNhsRowStatusEntry = _VrIpNhrpNhsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 1, 1)
)
vrIpNhrpNhsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpNhsIndex"),
)
if mibBuilder.loadTexts:
    vrIpNhrpNhsRowStatusEntry.setStatus("mandatory")
_VrIpNhrpNhsRowStatus_Type = RowStatus
_VrIpNhrpNhsRowStatus_Object = MibTableColumn
vrIpNhrpNhsRowStatus = _VrIpNhrpNhsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 1, 1, 1),
    _VrIpNhrpNhsRowStatus_Type()
)
vrIpNhrpNhsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsRowStatus.setStatus("mandatory")
_VrIpNhrpNhsComponentName_Type = DisplayString
_VrIpNhrpNhsComponentName_Object = MibTableColumn
vrIpNhrpNhsComponentName = _VrIpNhrpNhsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 1, 1, 2),
    _VrIpNhrpNhsComponentName_Type()
)
vrIpNhrpNhsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsComponentName.setStatus("mandatory")
_VrIpNhrpNhsStorageType_Type = StorageType
_VrIpNhrpNhsStorageType_Object = MibTableColumn
vrIpNhrpNhsStorageType = _VrIpNhrpNhsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 1, 1, 4),
    _VrIpNhrpNhsStorageType_Type()
)
vrIpNhrpNhsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsStorageType.setStatus("mandatory")
_VrIpNhrpNhsIndex_Type = NonReplicated
_VrIpNhrpNhsIndex_Object = MibTableColumn
vrIpNhrpNhsIndex = _VrIpNhrpNhsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 1, 1, 10),
    _VrIpNhrpNhsIndex_Type()
)
vrIpNhrpNhsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpNhrpNhsIndex.setStatus("mandatory")
_VrIpNhrpNhsEp_ObjectIdentity = ObjectIdentity
vrIpNhrpNhsEp = _VrIpNhrpNhsEp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 2)
)
_VrIpNhrpNhsEpRowStatusTable_Object = MibTable
vrIpNhrpNhsEpRowStatusTable = _VrIpNhrpNhsEpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpNhrpNhsEpRowStatusTable.setStatus("mandatory")
_VrIpNhrpNhsEpRowStatusEntry_Object = MibTableRow
vrIpNhrpNhsEpRowStatusEntry = _VrIpNhrpNhsEpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 2, 1, 1)
)
vrIpNhrpNhsEpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpNhsIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpNhsEpIndex"),
)
if mibBuilder.loadTexts:
    vrIpNhrpNhsEpRowStatusEntry.setStatus("mandatory")
_VrIpNhrpNhsEpRowStatus_Type = RowStatus
_VrIpNhrpNhsEpRowStatus_Object = MibTableColumn
vrIpNhrpNhsEpRowStatus = _VrIpNhrpNhsEpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 2, 1, 1, 1),
    _VrIpNhrpNhsEpRowStatus_Type()
)
vrIpNhrpNhsEpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNhrpNhsEpRowStatus.setStatus("mandatory")
_VrIpNhrpNhsEpComponentName_Type = DisplayString
_VrIpNhrpNhsEpComponentName_Object = MibTableColumn
vrIpNhrpNhsEpComponentName = _VrIpNhrpNhsEpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 2, 1, 1, 2),
    _VrIpNhrpNhsEpComponentName_Type()
)
vrIpNhrpNhsEpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsEpComponentName.setStatus("mandatory")
_VrIpNhrpNhsEpStorageType_Type = StorageType
_VrIpNhrpNhsEpStorageType_Object = MibTableColumn
vrIpNhrpNhsEpStorageType = _VrIpNhrpNhsEpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 2, 1, 1, 4),
    _VrIpNhrpNhsEpStorageType_Type()
)
vrIpNhrpNhsEpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsEpStorageType.setStatus("mandatory")


class _VrIpNhrpNhsEpIndex_Type(Integer32):
    """Custom type vrIpNhrpNhsEpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpNhrpNhsEpIndex_Type.__name__ = "Integer32"
_VrIpNhrpNhsEpIndex_Object = MibTableColumn
vrIpNhrpNhsEpIndex = _VrIpNhrpNhsEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 2, 1, 1, 10),
    _VrIpNhrpNhsEpIndex_Type()
)
vrIpNhrpNhsEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpNhrpNhsEpIndex.setStatus("mandatory")
_VrIpNhrpNhsEpNetAddr_ObjectIdentity = ObjectIdentity
vrIpNhrpNhsEpNetAddr = _VrIpNhrpNhsEpNetAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 2, 2)
)
_VrIpNhrpNhsEpNetAddrRowStatusTable_Object = MibTable
vrIpNhrpNhsEpNetAddrRowStatusTable = _VrIpNhrpNhsEpNetAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpNhrpNhsEpNetAddrRowStatusTable.setStatus("mandatory")
_VrIpNhrpNhsEpNetAddrRowStatusEntry_Object = MibTableRow
vrIpNhrpNhsEpNetAddrRowStatusEntry = _VrIpNhrpNhsEpNetAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 2, 2, 1, 1)
)
vrIpNhrpNhsEpNetAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpNhsIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpNhsEpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpNhsEpNetAddrIndex"),
)
if mibBuilder.loadTexts:
    vrIpNhrpNhsEpNetAddrRowStatusEntry.setStatus("mandatory")
_VrIpNhrpNhsEpNetAddrRowStatus_Type = RowStatus
_VrIpNhrpNhsEpNetAddrRowStatus_Object = MibTableColumn
vrIpNhrpNhsEpNetAddrRowStatus = _VrIpNhrpNhsEpNetAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 2, 2, 1, 1, 1),
    _VrIpNhrpNhsEpNetAddrRowStatus_Type()
)
vrIpNhrpNhsEpNetAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNhrpNhsEpNetAddrRowStatus.setStatus("mandatory")
_VrIpNhrpNhsEpNetAddrComponentName_Type = DisplayString
_VrIpNhrpNhsEpNetAddrComponentName_Object = MibTableColumn
vrIpNhrpNhsEpNetAddrComponentName = _VrIpNhrpNhsEpNetAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 2, 2, 1, 1, 2),
    _VrIpNhrpNhsEpNetAddrComponentName_Type()
)
vrIpNhrpNhsEpNetAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsEpNetAddrComponentName.setStatus("mandatory")
_VrIpNhrpNhsEpNetAddrStorageType_Type = StorageType
_VrIpNhrpNhsEpNetAddrStorageType_Object = MibTableColumn
vrIpNhrpNhsEpNetAddrStorageType = _VrIpNhrpNhsEpNetAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 2, 2, 1, 1, 4),
    _VrIpNhrpNhsEpNetAddrStorageType_Type()
)
vrIpNhrpNhsEpNetAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsEpNetAddrStorageType.setStatus("mandatory")


class _VrIpNhrpNhsEpNetAddrIndex_Type(Integer32):
    """Custom type vrIpNhrpNhsEpNetAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpNhrpNhsEpNetAddrIndex_Type.__name__ = "Integer32"
_VrIpNhrpNhsEpNetAddrIndex_Object = MibTableColumn
vrIpNhrpNhsEpNetAddrIndex = _VrIpNhrpNhsEpNetAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 2, 2, 1, 1, 10),
    _VrIpNhrpNhsEpNetAddrIndex_Type()
)
vrIpNhrpNhsEpNetAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpNhrpNhsEpNetAddrIndex.setStatus("mandatory")
_VrIpNhrpNhsEpNetAddrProvTable_Object = MibTable
vrIpNhrpNhsEpNetAddrProvTable = _VrIpNhrpNhsEpNetAddrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 2, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpNhrpNhsEpNetAddrProvTable.setStatus("mandatory")
_VrIpNhrpNhsEpNetAddrProvEntry_Object = MibTableRow
vrIpNhrpNhsEpNetAddrProvEntry = _VrIpNhrpNhsEpNetAddrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 2, 2, 10, 1)
)
vrIpNhrpNhsEpNetAddrProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpNhsIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpNhsEpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpNhsEpNetAddrIndex"),
)
if mibBuilder.loadTexts:
    vrIpNhrpNhsEpNetAddrProvEntry.setStatus("mandatory")


class _VrIpNhrpNhsEpNetAddrSourceAddress_Type(IpAddress):
    """Custom type vrIpNhrpNhsEpNetAddrSourceAddress based on IpAddress"""
    defaultHexValue = "00000000"


_VrIpNhrpNhsEpNetAddrSourceAddress_Object = MibTableColumn
vrIpNhrpNhsEpNetAddrSourceAddress = _VrIpNhrpNhsEpNetAddrSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 2, 2, 10, 1, 1),
    _VrIpNhrpNhsEpNetAddrSourceAddress_Type()
)
vrIpNhrpNhsEpNetAddrSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNhrpNhsEpNetAddrSourceAddress.setStatus("mandatory")


class _VrIpNhrpNhsEpNetAddrSourceMask_Type(IpAddress):
    """Custom type vrIpNhrpNhsEpNetAddrSourceMask based on IpAddress"""
    defaultHexValue = "00000000"


_VrIpNhrpNhsEpNetAddrSourceMask_Object = MibTableColumn
vrIpNhrpNhsEpNetAddrSourceMask = _VrIpNhrpNhsEpNetAddrSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 2, 2, 10, 1, 2),
    _VrIpNhrpNhsEpNetAddrSourceMask_Type()
)
vrIpNhrpNhsEpNetAddrSourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNhrpNhsEpNetAddrSourceMask.setStatus("mandatory")


class _VrIpNhrpNhsEpNetAddrDestinationAddress_Type(IpAddress):
    """Custom type vrIpNhrpNhsEpNetAddrDestinationAddress based on IpAddress"""
    defaultHexValue = "00000000"


_VrIpNhrpNhsEpNetAddrDestinationAddress_Object = MibTableColumn
vrIpNhrpNhsEpNetAddrDestinationAddress = _VrIpNhrpNhsEpNetAddrDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 2, 2, 10, 1, 3),
    _VrIpNhrpNhsEpNetAddrDestinationAddress_Type()
)
vrIpNhrpNhsEpNetAddrDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNhrpNhsEpNetAddrDestinationAddress.setStatus("mandatory")


class _VrIpNhrpNhsEpNetAddrDestinationMask_Type(IpAddress):
    """Custom type vrIpNhrpNhsEpNetAddrDestinationMask based on IpAddress"""
    defaultHexValue = "00000000"


_VrIpNhrpNhsEpNetAddrDestinationMask_Object = MibTableColumn
vrIpNhrpNhsEpNetAddrDestinationMask = _VrIpNhrpNhsEpNetAddrDestinationMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 2, 2, 10, 1, 4),
    _VrIpNhrpNhsEpNetAddrDestinationMask_Type()
)
vrIpNhrpNhsEpNetAddrDestinationMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNhrpNhsEpNetAddrDestinationMask.setStatus("mandatory")
_VrIpNhrpNhsEpProvTable_Object = MibTable
vrIpNhrpNhsEpProvTable = _VrIpNhrpNhsEpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpNhrpNhsEpProvTable.setStatus("mandatory")
_VrIpNhrpNhsEpProvEntry_Object = MibTableRow
vrIpNhrpNhsEpProvEntry = _VrIpNhrpNhsEpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 2, 10, 1)
)
vrIpNhrpNhsEpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpNhsIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpNhsEpIndex"),
)
if mibBuilder.loadTexts:
    vrIpNhrpNhsEpProvEntry.setStatus("mandatory")


class _VrIpNhrpNhsEpAction_Type(Integer32):
    """Custom type vrIpNhrpNhsEpAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("nak", 2))
    )


_VrIpNhrpNhsEpAction_Type.__name__ = "Integer32"
_VrIpNhrpNhsEpAction_Object = MibTableColumn
vrIpNhrpNhsEpAction = _VrIpNhrpNhsEpAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 2, 10, 1, 1),
    _VrIpNhrpNhsEpAction_Type()
)
vrIpNhrpNhsEpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNhrpNhsEpAction.setStatus("mandatory")


class _VrIpNhrpNhsEpProtocol_Type(Integer32):
    """Custom type vrIpNhrpNhsEpProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("staticLocal", 1))
    )


_VrIpNhrpNhsEpProtocol_Type.__name__ = "Integer32"
_VrIpNhrpNhsEpProtocol_Object = MibTableColumn
vrIpNhrpNhsEpProtocol = _VrIpNhrpNhsEpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 2, 10, 1, 2),
    _VrIpNhrpNhsEpProtocol_Type()
)
vrIpNhrpNhsEpProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNhrpNhsEpProtocol.setStatus("mandatory")
_VrIpNhrpNhsStatsTable_Object = MibTable
vrIpNhrpNhsStatsTable = _VrIpNhrpNhsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpNhrpNhsStatsTable.setStatus("mandatory")
_VrIpNhrpNhsStatsEntry_Object = MibTableRow
vrIpNhrpNhsStatsEntry = _VrIpNhrpNhsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1)
)
vrIpNhrpNhsStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpNhsIndex"),
)
if mibBuilder.loadTexts:
    vrIpNhrpNhsStatsEntry.setStatus("mandatory")
_VrIpNhrpNhsRxResolveReq_Type = Counter32
_VrIpNhrpNhsRxResolveReq_Object = MibTableColumn
vrIpNhrpNhsRxResolveReq = _VrIpNhrpNhsRxResolveReq_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 1),
    _VrIpNhrpNhsRxResolveReq_Type()
)
vrIpNhrpNhsRxResolveReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsRxResolveReq.setStatus("mandatory")
_VrIpNhrpNhsTxResolveReplyAck_Type = Counter32
_VrIpNhrpNhsTxResolveReplyAck_Object = MibTableColumn
vrIpNhrpNhsTxResolveReplyAck = _VrIpNhrpNhsTxResolveReplyAck_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 2),
    _VrIpNhrpNhsTxResolveReplyAck_Type()
)
vrIpNhrpNhsTxResolveReplyAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsTxResolveReplyAck.setStatus("mandatory")
_VrIpNhrpNhsTxResolveReplyNakProhibited_Type = Counter32
_VrIpNhrpNhsTxResolveReplyNakProhibited_Object = MibTableColumn
vrIpNhrpNhsTxResolveReplyNakProhibited = _VrIpNhrpNhsTxResolveReplyNakProhibited_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 3),
    _VrIpNhrpNhsTxResolveReplyNakProhibited_Type()
)
vrIpNhrpNhsTxResolveReplyNakProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsTxResolveReplyNakProhibited.setStatus("mandatory")
_VrIpNhrpNhsTxResolveReplyNakInsufResources_Type = Counter32
_VrIpNhrpNhsTxResolveReplyNakInsufResources_Object = MibTableColumn
vrIpNhrpNhsTxResolveReplyNakInsufResources = _VrIpNhrpNhsTxResolveReplyNakInsufResources_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 4),
    _VrIpNhrpNhsTxResolveReplyNakInsufResources_Type()
)
vrIpNhrpNhsTxResolveReplyNakInsufResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsTxResolveReplyNakInsufResources.setStatus("mandatory")
_VrIpNhrpNhsTxResolveReplyNakNoBinding_Type = Counter32
_VrIpNhrpNhsTxResolveReplyNakNoBinding_Object = MibTableColumn
vrIpNhrpNhsTxResolveReplyNakNoBinding = _VrIpNhrpNhsTxResolveReplyNakNoBinding_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 5),
    _VrIpNhrpNhsTxResolveReplyNakNoBinding_Type()
)
vrIpNhrpNhsTxResolveReplyNakNoBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsTxResolveReplyNakNoBinding.setStatus("mandatory")
_VrIpNhrpNhsTxResolveReplyNakNotUnique_Type = Counter32
_VrIpNhrpNhsTxResolveReplyNakNotUnique_Object = MibTableColumn
vrIpNhrpNhsTxResolveReplyNakNotUnique = _VrIpNhrpNhsTxResolveReplyNakNotUnique_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 6),
    _VrIpNhrpNhsTxResolveReplyNakNotUnique_Type()
)
vrIpNhrpNhsTxResolveReplyNakNotUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsTxResolveReplyNakNotUnique.setStatus("mandatory")
_VrIpNhrpNhsRxRegisterReq_Type = Counter32
_VrIpNhrpNhsRxRegisterReq_Object = MibTableColumn
vrIpNhrpNhsRxRegisterReq = _VrIpNhrpNhsRxRegisterReq_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 7),
    _VrIpNhrpNhsRxRegisterReq_Type()
)
vrIpNhrpNhsRxRegisterReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsRxRegisterReq.setStatus("mandatory")
_VrIpNhrpNhsRxPurgeReq_Type = Counter32
_VrIpNhrpNhsRxPurgeReq_Object = MibTableColumn
vrIpNhrpNhsRxPurgeReq = _VrIpNhrpNhsRxPurgeReq_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 12),
    _VrIpNhrpNhsRxPurgeReq_Type()
)
vrIpNhrpNhsRxPurgeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsRxPurgeReq.setStatus("mandatory")
_VrIpNhrpNhsTxPurgeReq_Type = Counter32
_VrIpNhrpNhsTxPurgeReq_Object = MibTableColumn
vrIpNhrpNhsTxPurgeReq = _VrIpNhrpNhsTxPurgeReq_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 13),
    _VrIpNhrpNhsTxPurgeReq_Type()
)
vrIpNhrpNhsTxPurgeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsTxPurgeReq.setStatus("mandatory")
_VrIpNhrpNhsRxPurgeReply_Type = Counter32
_VrIpNhrpNhsRxPurgeReply_Object = MibTableColumn
vrIpNhrpNhsRxPurgeReply = _VrIpNhrpNhsRxPurgeReply_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 14),
    _VrIpNhrpNhsRxPurgeReply_Type()
)
vrIpNhrpNhsRxPurgeReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsRxPurgeReply.setStatus("mandatory")
_VrIpNhrpNhsTxPurgeReply_Type = Counter32
_VrIpNhrpNhsTxPurgeReply_Object = MibTableColumn
vrIpNhrpNhsTxPurgeReply = _VrIpNhrpNhsTxPurgeReply_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 15),
    _VrIpNhrpNhsTxPurgeReply_Type()
)
vrIpNhrpNhsTxPurgeReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsTxPurgeReply.setStatus("mandatory")
_VrIpNhrpNhsRxErrUnrecognizedExtension_Type = Counter32
_VrIpNhrpNhsRxErrUnrecognizedExtension_Object = MibTableColumn
vrIpNhrpNhsRxErrUnrecognizedExtension = _VrIpNhrpNhsRxErrUnrecognizedExtension_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 16),
    _VrIpNhrpNhsRxErrUnrecognizedExtension_Type()
)
vrIpNhrpNhsRxErrUnrecognizedExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsRxErrUnrecognizedExtension.setStatus("mandatory")
_VrIpNhrpNhsRxErrLoopDetected_Type = Counter32
_VrIpNhrpNhsRxErrLoopDetected_Object = MibTableColumn
vrIpNhrpNhsRxErrLoopDetected = _VrIpNhrpNhsRxErrLoopDetected_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 17),
    _VrIpNhrpNhsRxErrLoopDetected_Type()
)
vrIpNhrpNhsRxErrLoopDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsRxErrLoopDetected.setStatus("mandatory")
_VrIpNhrpNhsRxErrProtoAddrUnreachable_Type = Counter32
_VrIpNhrpNhsRxErrProtoAddrUnreachable_Object = MibTableColumn
vrIpNhrpNhsRxErrProtoAddrUnreachable = _VrIpNhrpNhsRxErrProtoAddrUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 18),
    _VrIpNhrpNhsRxErrProtoAddrUnreachable_Type()
)
vrIpNhrpNhsRxErrProtoAddrUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsRxErrProtoAddrUnreachable.setStatus("mandatory")
_VrIpNhrpNhsRxErrProtoError_Type = Counter32
_VrIpNhrpNhsRxErrProtoError_Object = MibTableColumn
vrIpNhrpNhsRxErrProtoError = _VrIpNhrpNhsRxErrProtoError_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 19),
    _VrIpNhrpNhsRxErrProtoError_Type()
)
vrIpNhrpNhsRxErrProtoError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsRxErrProtoError.setStatus("mandatory")
_VrIpNhrpNhsRxErrSduSizeExceeded_Type = Counter32
_VrIpNhrpNhsRxErrSduSizeExceeded_Object = MibTableColumn
vrIpNhrpNhsRxErrSduSizeExceeded = _VrIpNhrpNhsRxErrSduSizeExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 20),
    _VrIpNhrpNhsRxErrSduSizeExceeded_Type()
)
vrIpNhrpNhsRxErrSduSizeExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsRxErrSduSizeExceeded.setStatus("mandatory")
_VrIpNhrpNhsRxErrInvalidExtension_Type = Counter32
_VrIpNhrpNhsRxErrInvalidExtension_Object = MibTableColumn
vrIpNhrpNhsRxErrInvalidExtension = _VrIpNhrpNhsRxErrInvalidExtension_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 21),
    _VrIpNhrpNhsRxErrInvalidExtension_Type()
)
vrIpNhrpNhsRxErrInvalidExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsRxErrInvalidExtension.setStatus("mandatory")
_VrIpNhrpNhsRxErrInvalidResReplyReceived_Type = Counter32
_VrIpNhrpNhsRxErrInvalidResReplyReceived_Object = MibTableColumn
vrIpNhrpNhsRxErrInvalidResReplyReceived = _VrIpNhrpNhsRxErrInvalidResReplyReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 22),
    _VrIpNhrpNhsRxErrInvalidResReplyReceived_Type()
)
vrIpNhrpNhsRxErrInvalidResReplyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsRxErrInvalidResReplyReceived.setStatus("mandatory")
_VrIpNhrpNhsRxErrAuthenticationFailure_Type = Counter32
_VrIpNhrpNhsRxErrAuthenticationFailure_Object = MibTableColumn
vrIpNhrpNhsRxErrAuthenticationFailure = _VrIpNhrpNhsRxErrAuthenticationFailure_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 23),
    _VrIpNhrpNhsRxErrAuthenticationFailure_Type()
)
vrIpNhrpNhsRxErrAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsRxErrAuthenticationFailure.setStatus("mandatory")
_VrIpNhrpNhsRxErrHopCountExceeded_Type = Counter32
_VrIpNhrpNhsRxErrHopCountExceeded_Object = MibTableColumn
vrIpNhrpNhsRxErrHopCountExceeded = _VrIpNhrpNhsRxErrHopCountExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 24),
    _VrIpNhrpNhsRxErrHopCountExceeded_Type()
)
vrIpNhrpNhsRxErrHopCountExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsRxErrHopCountExceeded.setStatus("mandatory")
_VrIpNhrpNhsTxErrUnrecognizedExtension_Type = Counter32
_VrIpNhrpNhsTxErrUnrecognizedExtension_Object = MibTableColumn
vrIpNhrpNhsTxErrUnrecognizedExtension = _VrIpNhrpNhsTxErrUnrecognizedExtension_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 25),
    _VrIpNhrpNhsTxErrUnrecognizedExtension_Type()
)
vrIpNhrpNhsTxErrUnrecognizedExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsTxErrUnrecognizedExtension.setStatus("mandatory")
_VrIpNhrpNhsTxErrLoopDetected_Type = Counter32
_VrIpNhrpNhsTxErrLoopDetected_Object = MibTableColumn
vrIpNhrpNhsTxErrLoopDetected = _VrIpNhrpNhsTxErrLoopDetected_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 26),
    _VrIpNhrpNhsTxErrLoopDetected_Type()
)
vrIpNhrpNhsTxErrLoopDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsTxErrLoopDetected.setStatus("mandatory")
_VrIpNhrpNhsTxErrProtoAddrUnreachable_Type = Counter32
_VrIpNhrpNhsTxErrProtoAddrUnreachable_Object = MibTableColumn
vrIpNhrpNhsTxErrProtoAddrUnreachable = _VrIpNhrpNhsTxErrProtoAddrUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 27),
    _VrIpNhrpNhsTxErrProtoAddrUnreachable_Type()
)
vrIpNhrpNhsTxErrProtoAddrUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsTxErrProtoAddrUnreachable.setStatus("mandatory")
_VrIpNhrpNhsTxErrProtoError_Type = Counter32
_VrIpNhrpNhsTxErrProtoError_Object = MibTableColumn
vrIpNhrpNhsTxErrProtoError = _VrIpNhrpNhsTxErrProtoError_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 28),
    _VrIpNhrpNhsTxErrProtoError_Type()
)
vrIpNhrpNhsTxErrProtoError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsTxErrProtoError.setStatus("mandatory")
_VrIpNhrpNhsTxErrSduSizeExceeded_Type = Counter32
_VrIpNhrpNhsTxErrSduSizeExceeded_Object = MibTableColumn
vrIpNhrpNhsTxErrSduSizeExceeded = _VrIpNhrpNhsTxErrSduSizeExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 29),
    _VrIpNhrpNhsTxErrSduSizeExceeded_Type()
)
vrIpNhrpNhsTxErrSduSizeExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsTxErrSduSizeExceeded.setStatus("mandatory")
_VrIpNhrpNhsTxErrInvalidExtension_Type = Counter32
_VrIpNhrpNhsTxErrInvalidExtension_Object = MibTableColumn
vrIpNhrpNhsTxErrInvalidExtension = _VrIpNhrpNhsTxErrInvalidExtension_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 30),
    _VrIpNhrpNhsTxErrInvalidExtension_Type()
)
vrIpNhrpNhsTxErrInvalidExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsTxErrInvalidExtension.setStatus("mandatory")
_VrIpNhrpNhsTxErrAuthenticationFailure_Type = Counter32
_VrIpNhrpNhsTxErrAuthenticationFailure_Object = MibTableColumn
vrIpNhrpNhsTxErrAuthenticationFailure = _VrIpNhrpNhsTxErrAuthenticationFailure_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 31),
    _VrIpNhrpNhsTxErrAuthenticationFailure_Type()
)
vrIpNhrpNhsTxErrAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsTxErrAuthenticationFailure.setStatus("mandatory")
_VrIpNhrpNhsTxErrHopCountExceeded_Type = Counter32
_VrIpNhrpNhsTxErrHopCountExceeded_Object = MibTableColumn
vrIpNhrpNhsTxErrHopCountExceeded = _VrIpNhrpNhsTxErrHopCountExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 32),
    _VrIpNhrpNhsTxErrHopCountExceeded_Type()
)
vrIpNhrpNhsTxErrHopCountExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsTxErrHopCountExceeded.setStatus("mandatory")
_VrIpNhrpNhsFwdResolveReq_Type = Counter32
_VrIpNhrpNhsFwdResolveReq_Object = MibTableColumn
vrIpNhrpNhsFwdResolveReq = _VrIpNhrpNhsFwdResolveReq_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 33),
    _VrIpNhrpNhsFwdResolveReq_Type()
)
vrIpNhrpNhsFwdResolveReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsFwdResolveReq.setStatus("mandatory")
_VrIpNhrpNhsFwdResolveReply_Type = Counter32
_VrIpNhrpNhsFwdResolveReply_Object = MibTableColumn
vrIpNhrpNhsFwdResolveReply = _VrIpNhrpNhsFwdResolveReply_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 34),
    _VrIpNhrpNhsFwdResolveReply_Type()
)
vrIpNhrpNhsFwdResolveReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsFwdResolveReply.setStatus("mandatory")
_VrIpNhrpNhsFwdRegisterReq_Type = Counter32
_VrIpNhrpNhsFwdRegisterReq_Object = MibTableColumn
vrIpNhrpNhsFwdRegisterReq = _VrIpNhrpNhsFwdRegisterReq_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 35),
    _VrIpNhrpNhsFwdRegisterReq_Type()
)
vrIpNhrpNhsFwdRegisterReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsFwdRegisterReq.setStatus("mandatory")
_VrIpNhrpNhsFwdRegisterReply_Type = Counter32
_VrIpNhrpNhsFwdRegisterReply_Object = MibTableColumn
vrIpNhrpNhsFwdRegisterReply = _VrIpNhrpNhsFwdRegisterReply_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 36),
    _VrIpNhrpNhsFwdRegisterReply_Type()
)
vrIpNhrpNhsFwdRegisterReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsFwdRegisterReply.setStatus("mandatory")
_VrIpNhrpNhsFwdPurgeReq_Type = Counter32
_VrIpNhrpNhsFwdPurgeReq_Object = MibTableColumn
vrIpNhrpNhsFwdPurgeReq = _VrIpNhrpNhsFwdPurgeReq_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 37),
    _VrIpNhrpNhsFwdPurgeReq_Type()
)
vrIpNhrpNhsFwdPurgeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsFwdPurgeReq.setStatus("mandatory")
_VrIpNhrpNhsFwdPurgeReply_Type = Counter32
_VrIpNhrpNhsFwdPurgeReply_Object = MibTableColumn
vrIpNhrpNhsFwdPurgeReply = _VrIpNhrpNhsFwdPurgeReply_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 38),
    _VrIpNhrpNhsFwdPurgeReply_Type()
)
vrIpNhrpNhsFwdPurgeReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsFwdPurgeReply.setStatus("mandatory")
_VrIpNhrpNhsFwdErrorIndication_Type = Counter32
_VrIpNhrpNhsFwdErrorIndication_Object = MibTableColumn
vrIpNhrpNhsFwdErrorIndication = _VrIpNhrpNhsFwdErrorIndication_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 2, 10, 1, 39),
    _VrIpNhrpNhsFwdErrorIndication_Type()
)
vrIpNhrpNhsFwdErrorIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhsFwdErrorIndication.setStatus("mandatory")
_VrIpNhrpNhc_ObjectIdentity = ObjectIdentity
vrIpNhrpNhc = _VrIpNhrpNhc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3)
)
_VrIpNhrpNhcRowStatusTable_Object = MibTable
vrIpNhrpNhcRowStatusTable = _VrIpNhrpNhcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 1)
)
if mibBuilder.loadTexts:
    vrIpNhrpNhcRowStatusTable.setStatus("mandatory")
_VrIpNhrpNhcRowStatusEntry_Object = MibTableRow
vrIpNhrpNhcRowStatusEntry = _VrIpNhrpNhcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 1, 1)
)
vrIpNhrpNhcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpNhcIndex"),
)
if mibBuilder.loadTexts:
    vrIpNhrpNhcRowStatusEntry.setStatus("mandatory")
_VrIpNhrpNhcRowStatus_Type = RowStatus
_VrIpNhrpNhcRowStatus_Object = MibTableColumn
vrIpNhrpNhcRowStatus = _VrIpNhrpNhcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 1, 1, 1),
    _VrIpNhrpNhcRowStatus_Type()
)
vrIpNhrpNhcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhcRowStatus.setStatus("mandatory")
_VrIpNhrpNhcComponentName_Type = DisplayString
_VrIpNhrpNhcComponentName_Object = MibTableColumn
vrIpNhrpNhcComponentName = _VrIpNhrpNhcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 1, 1, 2),
    _VrIpNhrpNhcComponentName_Type()
)
vrIpNhrpNhcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhcComponentName.setStatus("mandatory")
_VrIpNhrpNhcStorageType_Type = StorageType
_VrIpNhrpNhcStorageType_Object = MibTableColumn
vrIpNhrpNhcStorageType = _VrIpNhrpNhcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 1, 1, 4),
    _VrIpNhrpNhcStorageType_Type()
)
vrIpNhrpNhcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhcStorageType.setStatus("mandatory")
_VrIpNhrpNhcIndex_Type = NonReplicated
_VrIpNhrpNhcIndex_Object = MibTableColumn
vrIpNhrpNhcIndex = _VrIpNhrpNhcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 1, 1, 10),
    _VrIpNhrpNhcIndex_Type()
)
vrIpNhrpNhcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpNhrpNhcIndex.setStatus("mandatory")
_VrIpNhrpNhcProvTable_Object = MibTable
vrIpNhrpNhcProvTable = _VrIpNhrpNhcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 10)
)
if mibBuilder.loadTexts:
    vrIpNhrpNhcProvTable.setStatus("mandatory")
_VrIpNhrpNhcProvEntry_Object = MibTableRow
vrIpNhrpNhcProvEntry = _VrIpNhrpNhcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 10, 1)
)
vrIpNhrpNhcProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpNhcIndex"),
)
if mibBuilder.loadTexts:
    vrIpNhrpNhcProvEntry.setStatus("mandatory")


class _VrIpNhrpNhcFlowDetectPacketCount_Type(Unsigned32):
    """Custom type vrIpNhrpNhcFlowDetectPacketCount based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4292967295),
    )


_VrIpNhrpNhcFlowDetectPacketCount_Type.__name__ = "Unsigned32"
_VrIpNhrpNhcFlowDetectPacketCount_Object = MibTableColumn
vrIpNhrpNhcFlowDetectPacketCount = _VrIpNhrpNhcFlowDetectPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 10, 1, 1),
    _VrIpNhrpNhcFlowDetectPacketCount_Type()
)
vrIpNhrpNhcFlowDetectPacketCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNhrpNhcFlowDetectPacketCount.setStatus("mandatory")


class _VrIpNhrpNhcFlowDetectTimePeriod_Type(Integer32):
    """Custom type vrIpNhrpNhcFlowDetectTimePeriod based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(60, 60),
    )


_VrIpNhrpNhcFlowDetectTimePeriod_Type.__name__ = "Integer32"
_VrIpNhrpNhcFlowDetectTimePeriod_Object = MibTableColumn
vrIpNhrpNhcFlowDetectTimePeriod = _VrIpNhrpNhcFlowDetectTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 10, 1, 2),
    _VrIpNhrpNhcFlowDetectTimePeriod_Type()
)
vrIpNhrpNhcFlowDetectTimePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNhrpNhcFlowDetectTimePeriod.setStatus("mandatory")


class _VrIpNhrpNhcIdleDetectPacketCount_Type(Unsigned32):
    """Custom type vrIpNhrpNhcIdleDetectPacketCount based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4292967295),
    )


_VrIpNhrpNhcIdleDetectPacketCount_Type.__name__ = "Unsigned32"
_VrIpNhrpNhcIdleDetectPacketCount_Object = MibTableColumn
vrIpNhrpNhcIdleDetectPacketCount = _VrIpNhrpNhcIdleDetectPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 10, 1, 3),
    _VrIpNhrpNhcIdleDetectPacketCount_Type()
)
vrIpNhrpNhcIdleDetectPacketCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNhrpNhcIdleDetectPacketCount.setStatus("mandatory")


class _VrIpNhrpNhcIdleDetectTimePeriod_Type(Unsigned32):
    """Custom type vrIpNhrpNhcIdleDetectTimePeriod based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_VrIpNhrpNhcIdleDetectTimePeriod_Type.__name__ = "Unsigned32"
_VrIpNhrpNhcIdleDetectTimePeriod_Object = MibTableColumn
vrIpNhrpNhcIdleDetectTimePeriod = _VrIpNhrpNhcIdleDetectTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 10, 1, 4),
    _VrIpNhrpNhcIdleDetectTimePeriod_Type()
)
vrIpNhrpNhcIdleDetectTimePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNhrpNhcIdleDetectTimePeriod.setStatus("mandatory")


class _VrIpNhrpNhcAtmFlowDetection_Type(Integer32):
    """Custom type vrIpNhrpNhcAtmFlowDetection based on Integer32"""
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


_VrIpNhrpNhcAtmFlowDetection_Type.__name__ = "Integer32"
_VrIpNhrpNhcAtmFlowDetection_Object = MibTableColumn
vrIpNhrpNhcAtmFlowDetection = _VrIpNhrpNhcAtmFlowDetection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 10, 1, 5),
    _VrIpNhrpNhcAtmFlowDetection_Type()
)
vrIpNhrpNhcAtmFlowDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNhrpNhcAtmFlowDetection.setStatus("mandatory")
_VrIpNhrpNhcStatsTable_Object = MibTable
vrIpNhrpNhcStatsTable = _VrIpNhrpNhcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 11)
)
if mibBuilder.loadTexts:
    vrIpNhrpNhcStatsTable.setStatus("mandatory")
_VrIpNhrpNhcStatsEntry_Object = MibTableRow
vrIpNhrpNhcStatsEntry = _VrIpNhrpNhcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 11, 1)
)
vrIpNhrpNhcStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpNhcIndex"),
)
if mibBuilder.loadTexts:
    vrIpNhrpNhcStatsEntry.setStatus("mandatory")
_VrIpNhrpNhcTxResolveReq_Type = Counter32
_VrIpNhrpNhcTxResolveReq_Object = MibTableColumn
vrIpNhrpNhcTxResolveReq = _VrIpNhrpNhcTxResolveReq_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 11, 1, 1),
    _VrIpNhrpNhcTxResolveReq_Type()
)
vrIpNhrpNhcTxResolveReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhcTxResolveReq.setStatus("mandatory")
_VrIpNhrpNhcRxResolveReplyAck_Type = Counter32
_VrIpNhrpNhcRxResolveReplyAck_Object = MibTableColumn
vrIpNhrpNhcRxResolveReplyAck = _VrIpNhrpNhcRxResolveReplyAck_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 11, 1, 2),
    _VrIpNhrpNhcRxResolveReplyAck_Type()
)
vrIpNhrpNhcRxResolveReplyAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhcRxResolveReplyAck.setStatus("mandatory")
_VrIpNhrpNhcRxResolveReplyNakProhibited_Type = Counter32
_VrIpNhrpNhcRxResolveReplyNakProhibited_Object = MibTableColumn
vrIpNhrpNhcRxResolveReplyNakProhibited = _VrIpNhrpNhcRxResolveReplyNakProhibited_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 11, 1, 3),
    _VrIpNhrpNhcRxResolveReplyNakProhibited_Type()
)
vrIpNhrpNhcRxResolveReplyNakProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhcRxResolveReplyNakProhibited.setStatus("mandatory")
_VrIpNhrpNhcRxResolveReplyNakInsufResources_Type = Counter32
_VrIpNhrpNhcRxResolveReplyNakInsufResources_Object = MibTableColumn
vrIpNhrpNhcRxResolveReplyNakInsufResources = _VrIpNhrpNhcRxResolveReplyNakInsufResources_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 11, 1, 4),
    _VrIpNhrpNhcRxResolveReplyNakInsufResources_Type()
)
vrIpNhrpNhcRxResolveReplyNakInsufResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhcRxResolveReplyNakInsufResources.setStatus("mandatory")
_VrIpNhrpNhcRxResolveReplyNakNoBinding_Type = Counter32
_VrIpNhrpNhcRxResolveReplyNakNoBinding_Object = MibTableColumn
vrIpNhrpNhcRxResolveReplyNakNoBinding = _VrIpNhrpNhcRxResolveReplyNakNoBinding_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 11, 1, 5),
    _VrIpNhrpNhcRxResolveReplyNakNoBinding_Type()
)
vrIpNhrpNhcRxResolveReplyNakNoBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhcRxResolveReplyNakNoBinding.setStatus("mandatory")
_VrIpNhrpNhcRxResolveReplyNakNotUnique_Type = Counter32
_VrIpNhrpNhcRxResolveReplyNakNotUnique_Object = MibTableColumn
vrIpNhrpNhcRxResolveReplyNakNotUnique = _VrIpNhrpNhcRxResolveReplyNakNotUnique_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 11, 1, 6),
    _VrIpNhrpNhcRxResolveReplyNakNotUnique_Type()
)
vrIpNhrpNhcRxResolveReplyNakNotUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhcRxResolveReplyNakNotUnique.setStatus("mandatory")
_VrIpNhrpNhcRxPurgeReq_Type = Counter32
_VrIpNhrpNhcRxPurgeReq_Object = MibTableColumn
vrIpNhrpNhcRxPurgeReq = _VrIpNhrpNhcRxPurgeReq_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 11, 1, 12),
    _VrIpNhrpNhcRxPurgeReq_Type()
)
vrIpNhrpNhcRxPurgeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhcRxPurgeReq.setStatus("mandatory")
_VrIpNhrpNhcTxPurgeReq_Type = Counter32
_VrIpNhrpNhcTxPurgeReq_Object = MibTableColumn
vrIpNhrpNhcTxPurgeReq = _VrIpNhrpNhcTxPurgeReq_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 11, 1, 13),
    _VrIpNhrpNhcTxPurgeReq_Type()
)
vrIpNhrpNhcTxPurgeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhcTxPurgeReq.setStatus("mandatory")
_VrIpNhrpNhcRxPurgeReply_Type = Counter32
_VrIpNhrpNhcRxPurgeReply_Object = MibTableColumn
vrIpNhrpNhcRxPurgeReply = _VrIpNhrpNhcRxPurgeReply_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 11, 1, 14),
    _VrIpNhrpNhcRxPurgeReply_Type()
)
vrIpNhrpNhcRxPurgeReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhcRxPurgeReply.setStatus("mandatory")
_VrIpNhrpNhcTxPurgeReply_Type = Counter32
_VrIpNhrpNhcTxPurgeReply_Object = MibTableColumn
vrIpNhrpNhcTxPurgeReply = _VrIpNhrpNhcTxPurgeReply_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 11, 1, 15),
    _VrIpNhrpNhcTxPurgeReply_Type()
)
vrIpNhrpNhcTxPurgeReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhcTxPurgeReply.setStatus("mandatory")
_VrIpNhrpNhcTxErrIndication_Type = Counter32
_VrIpNhrpNhcTxErrIndication_Object = MibTableColumn
vrIpNhrpNhcTxErrIndication = _VrIpNhrpNhcTxErrIndication_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 11, 1, 16),
    _VrIpNhrpNhcTxErrIndication_Type()
)
vrIpNhrpNhcTxErrIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhcTxErrIndication.setStatus("mandatory")
_VrIpNhrpNhcRxErrUnrecognizedExtension_Type = Counter32
_VrIpNhrpNhcRxErrUnrecognizedExtension_Object = MibTableColumn
vrIpNhrpNhcRxErrUnrecognizedExtension = _VrIpNhrpNhcRxErrUnrecognizedExtension_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 11, 1, 17),
    _VrIpNhrpNhcRxErrUnrecognizedExtension_Type()
)
vrIpNhrpNhcRxErrUnrecognizedExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhcRxErrUnrecognizedExtension.setStatus("mandatory")
_VrIpNhrpNhcRxErrLoopDetected_Type = Counter32
_VrIpNhrpNhcRxErrLoopDetected_Object = MibTableColumn
vrIpNhrpNhcRxErrLoopDetected = _VrIpNhrpNhcRxErrLoopDetected_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 11, 1, 18),
    _VrIpNhrpNhcRxErrLoopDetected_Type()
)
vrIpNhrpNhcRxErrLoopDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhcRxErrLoopDetected.setStatus("mandatory")
_VrIpNhrpNhcRxErrProtoAddrUnreachable_Type = Counter32
_VrIpNhrpNhcRxErrProtoAddrUnreachable_Object = MibTableColumn
vrIpNhrpNhcRxErrProtoAddrUnreachable = _VrIpNhrpNhcRxErrProtoAddrUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 11, 1, 19),
    _VrIpNhrpNhcRxErrProtoAddrUnreachable_Type()
)
vrIpNhrpNhcRxErrProtoAddrUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhcRxErrProtoAddrUnreachable.setStatus("mandatory")
_VrIpNhrpNhcRxErrProtoError_Type = Counter32
_VrIpNhrpNhcRxErrProtoError_Object = MibTableColumn
vrIpNhrpNhcRxErrProtoError = _VrIpNhrpNhcRxErrProtoError_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 11, 1, 20),
    _VrIpNhrpNhcRxErrProtoError_Type()
)
vrIpNhrpNhcRxErrProtoError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhcRxErrProtoError.setStatus("mandatory")
_VrIpNhrpNhcRxErrSduSizeExceeded_Type = Counter32
_VrIpNhrpNhcRxErrSduSizeExceeded_Object = MibTableColumn
vrIpNhrpNhcRxErrSduSizeExceeded = _VrIpNhrpNhcRxErrSduSizeExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 11, 1, 21),
    _VrIpNhrpNhcRxErrSduSizeExceeded_Type()
)
vrIpNhrpNhcRxErrSduSizeExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhcRxErrSduSizeExceeded.setStatus("mandatory")
_VrIpNhrpNhcRxErrInvalidExtension_Type = Counter32
_VrIpNhrpNhcRxErrInvalidExtension_Object = MibTableColumn
vrIpNhrpNhcRxErrInvalidExtension = _VrIpNhrpNhcRxErrInvalidExtension_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 11, 1, 22),
    _VrIpNhrpNhcRxErrInvalidExtension_Type()
)
vrIpNhrpNhcRxErrInvalidExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhcRxErrInvalidExtension.setStatus("mandatory")
_VrIpNhrpNhcRxErrAuthenticationFailure_Type = Counter32
_VrIpNhrpNhcRxErrAuthenticationFailure_Object = MibTableColumn
vrIpNhrpNhcRxErrAuthenticationFailure = _VrIpNhrpNhcRxErrAuthenticationFailure_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 11, 1, 23),
    _VrIpNhrpNhcRxErrAuthenticationFailure_Type()
)
vrIpNhrpNhcRxErrAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhcRxErrAuthenticationFailure.setStatus("mandatory")
_VrIpNhrpNhcRxErrHopCountExceeded_Type = Counter32
_VrIpNhrpNhcRxErrHopCountExceeded_Object = MibTableColumn
vrIpNhrpNhcRxErrHopCountExceeded = _VrIpNhrpNhcRxErrHopCountExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 3, 11, 1, 24),
    _VrIpNhrpNhcRxErrHopCountExceeded_Type()
)
vrIpNhrpNhcRxErrHopCountExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpNhcRxErrHopCountExceeded.setStatus("mandatory")
_VrIpNhrpRce_ObjectIdentity = ObjectIdentity
vrIpNhrpRce = _VrIpNhrpRce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 4)
)
_VrIpNhrpRceRowStatusTable_Object = MibTable
vrIpNhrpRceRowStatusTable = _VrIpNhrpRceRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 4, 1)
)
if mibBuilder.loadTexts:
    vrIpNhrpRceRowStatusTable.setStatus("mandatory")
_VrIpNhrpRceRowStatusEntry_Object = MibTableRow
vrIpNhrpRceRowStatusEntry = _VrIpNhrpRceRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 4, 1, 1)
)
vrIpNhrpRceRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpRceDestAddrIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpRceDestMaskIndex"),
)
if mibBuilder.loadTexts:
    vrIpNhrpRceRowStatusEntry.setStatus("mandatory")
_VrIpNhrpRceRowStatus_Type = RowStatus
_VrIpNhrpRceRowStatus_Object = MibTableColumn
vrIpNhrpRceRowStatus = _VrIpNhrpRceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 4, 1, 1, 1),
    _VrIpNhrpRceRowStatus_Type()
)
vrIpNhrpRceRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpRceRowStatus.setStatus("mandatory")
_VrIpNhrpRceComponentName_Type = DisplayString
_VrIpNhrpRceComponentName_Object = MibTableColumn
vrIpNhrpRceComponentName = _VrIpNhrpRceComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 4, 1, 1, 2),
    _VrIpNhrpRceComponentName_Type()
)
vrIpNhrpRceComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpRceComponentName.setStatus("mandatory")
_VrIpNhrpRceStorageType_Type = StorageType
_VrIpNhrpRceStorageType_Object = MibTableColumn
vrIpNhrpRceStorageType = _VrIpNhrpRceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 4, 1, 1, 4),
    _VrIpNhrpRceStorageType_Type()
)
vrIpNhrpRceStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpRceStorageType.setStatus("mandatory")
_VrIpNhrpRceDestAddrIndex_Type = IpAddress
_VrIpNhrpRceDestAddrIndex_Object = MibTableColumn
vrIpNhrpRceDestAddrIndex = _VrIpNhrpRceDestAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 4, 1, 1, 10),
    _VrIpNhrpRceDestAddrIndex_Type()
)
vrIpNhrpRceDestAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpNhrpRceDestAddrIndex.setStatus("mandatory")
_VrIpNhrpRceDestMaskIndex_Type = IpAddress
_VrIpNhrpRceDestMaskIndex_Object = MibTableColumn
vrIpNhrpRceDestMaskIndex = _VrIpNhrpRceDestMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 4, 1, 1, 11),
    _VrIpNhrpRceDestMaskIndex_Type()
)
vrIpNhrpRceDestMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpNhrpRceDestMaskIndex.setStatus("mandatory")
_VrIpNhrpRceOperTable_Object = MibTable
vrIpNhrpRceOperTable = _VrIpNhrpRceOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 4, 10)
)
if mibBuilder.loadTexts:
    vrIpNhrpRceOperTable.setStatus("mandatory")
_VrIpNhrpRceOperEntry_Object = MibTableRow
vrIpNhrpRceOperEntry = _VrIpNhrpRceOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 4, 10, 1)
)
vrIpNhrpRceOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpRceDestAddrIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpRceDestMaskIndex"),
)
if mibBuilder.loadTexts:
    vrIpNhrpRceOperEntry.setStatus("mandatory")


class _VrIpNhrpRceNbmaAddress_Type(HexString):
    """Custom type vrIpNhrpRceNbmaAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_VrIpNhrpRceNbmaAddress_Type.__name__ = "HexString"
_VrIpNhrpRceNbmaAddress_Object = MibTableColumn
vrIpNhrpRceNbmaAddress = _VrIpNhrpRceNbmaAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 4, 10, 1, 3),
    _VrIpNhrpRceNbmaAddress_Type()
)
vrIpNhrpRceNbmaAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpRceNbmaAddress.setStatus("mandatory")


class _VrIpNhrpRceEntryState_Type(Integer32):
    """Custom type vrIpNhrpRceEntryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("ackReply", 2),
          ("incomplete", 1),
          ("localReply", 11),
          ("nakReply", 3),
          ("noReply", 10))
    )


_VrIpNhrpRceEntryState_Type.__name__ = "Integer32"
_VrIpNhrpRceEntryState_Object = MibTableColumn
vrIpNhrpRceEntryState = _VrIpNhrpRceEntryState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 4, 10, 1, 6),
    _VrIpNhrpRceEntryState_Type()
)
vrIpNhrpRceEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpRceEntryState.setStatus("mandatory")


class _VrIpNhrpRceHoldingTime_Type(Unsigned32):
    """Custom type vrIpNhrpRceHoldingTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpNhrpRceHoldingTime_Type.__name__ = "Unsigned32"
_VrIpNhrpRceHoldingTime_Object = MibTableColumn
vrIpNhrpRceHoldingTime = _VrIpNhrpRceHoldingTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 4, 10, 1, 7),
    _VrIpNhrpRceHoldingTime_Type()
)
vrIpNhrpRceHoldingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpRceHoldingTime.setStatus("mandatory")
_VrIpNhrpRceShortcut_Type = RowPointer
_VrIpNhrpRceShortcut_Object = MibTableColumn
vrIpNhrpRceShortcut = _VrIpNhrpRceShortcut_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 4, 10, 1, 8),
    _VrIpNhrpRceShortcut_Type()
)
vrIpNhrpRceShortcut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpRceShortcut.setStatus("mandatory")
_VrIpNhrpAdminControlTable_Object = MibTable
vrIpNhrpAdminControlTable = _VrIpNhrpAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 10)
)
if mibBuilder.loadTexts:
    vrIpNhrpAdminControlTable.setStatus("mandatory")
_VrIpNhrpAdminControlEntry_Object = MibTableRow
vrIpNhrpAdminControlEntry = _VrIpNhrpAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 10, 1)
)
vrIpNhrpAdminControlEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpIndex"),
)
if mibBuilder.loadTexts:
    vrIpNhrpAdminControlEntry.setStatus("mandatory")


class _VrIpNhrpSnmpAdminStatus_Type(Integer32):
    """Custom type vrIpNhrpSnmpAdminStatus based on Integer32"""
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


_VrIpNhrpSnmpAdminStatus_Type.__name__ = "Integer32"
_VrIpNhrpSnmpAdminStatus_Object = MibTableColumn
vrIpNhrpSnmpAdminStatus = _VrIpNhrpSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 10, 1, 1),
    _VrIpNhrpSnmpAdminStatus_Type()
)
vrIpNhrpSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNhrpSnmpAdminStatus.setStatus("mandatory")
_VrIpNhrpProvTable_Object = MibTable
vrIpNhrpProvTable = _VrIpNhrpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 11)
)
if mibBuilder.loadTexts:
    vrIpNhrpProvTable.setStatus("mandatory")
_VrIpNhrpProvEntry_Object = MibTableRow
vrIpNhrpProvEntry = _VrIpNhrpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 11, 1)
)
vrIpNhrpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpIndex"),
)
if mibBuilder.loadTexts:
    vrIpNhrpProvEntry.setStatus("mandatory")


class _VrIpNhrpMaxResCacheEntries_Type(Unsigned32):
    """Custom type vrIpNhrpMaxResCacheEntries based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 1024),
    )


_VrIpNhrpMaxResCacheEntries_Type.__name__ = "Unsigned32"
_VrIpNhrpMaxResCacheEntries_Object = MibTableColumn
vrIpNhrpMaxResCacheEntries = _VrIpNhrpMaxResCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 11, 1, 1),
    _VrIpNhrpMaxResCacheEntries_Type()
)
vrIpNhrpMaxResCacheEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNhrpMaxResCacheEntries.setStatus("mandatory")


class _VrIpNhrpFwdTransitRecord_Type(Integer32):
    """Custom type vrIpNhrpFwdTransitRecord based on Integer32"""
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


_VrIpNhrpFwdTransitRecord_Type.__name__ = "Integer32"
_VrIpNhrpFwdTransitRecord_Object = MibTableColumn
vrIpNhrpFwdTransitRecord = _VrIpNhrpFwdTransitRecord_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 11, 1, 2),
    _VrIpNhrpFwdTransitRecord_Type()
)
vrIpNhrpFwdTransitRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNhrpFwdTransitRecord.setStatus("mandatory")


class _VrIpNhrpRevTransitRecord_Type(Integer32):
    """Custom type vrIpNhrpRevTransitRecord based on Integer32"""
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


_VrIpNhrpRevTransitRecord_Type.__name__ = "Integer32"
_VrIpNhrpRevTransitRecord_Object = MibTableColumn
vrIpNhrpRevTransitRecord = _VrIpNhrpRevTransitRecord_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 11, 1, 3),
    _VrIpNhrpRevTransitRecord_Type()
)
vrIpNhrpRevTransitRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNhrpRevTransitRecord.setStatus("mandatory")
_VrIpNhrpStateTable_Object = MibTable
vrIpNhrpStateTable = _VrIpNhrpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 13)
)
if mibBuilder.loadTexts:
    vrIpNhrpStateTable.setStatus("mandatory")
_VrIpNhrpStateEntry_Object = MibTableRow
vrIpNhrpStateEntry = _VrIpNhrpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 13, 1)
)
vrIpNhrpStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpIndex"),
)
if mibBuilder.loadTexts:
    vrIpNhrpStateEntry.setStatus("mandatory")


class _VrIpNhrpAdminState_Type(Integer32):
    """Custom type vrIpNhrpAdminState based on Integer32"""
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


_VrIpNhrpAdminState_Type.__name__ = "Integer32"
_VrIpNhrpAdminState_Object = MibTableColumn
vrIpNhrpAdminState = _VrIpNhrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 13, 1, 1),
    _VrIpNhrpAdminState_Type()
)
vrIpNhrpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpAdminState.setStatus("mandatory")


class _VrIpNhrpOperationalState_Type(Integer32):
    """Custom type vrIpNhrpOperationalState based on Integer32"""
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


_VrIpNhrpOperationalState_Type.__name__ = "Integer32"
_VrIpNhrpOperationalState_Object = MibTableColumn
vrIpNhrpOperationalState = _VrIpNhrpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 13, 1, 2),
    _VrIpNhrpOperationalState_Type()
)
vrIpNhrpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpOperationalState.setStatus("mandatory")


class _VrIpNhrpUsageState_Type(Integer32):
    """Custom type vrIpNhrpUsageState based on Integer32"""
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


_VrIpNhrpUsageState_Type.__name__ = "Integer32"
_VrIpNhrpUsageState_Object = MibTableColumn
vrIpNhrpUsageState = _VrIpNhrpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 13, 1, 3),
    _VrIpNhrpUsageState_Type()
)
vrIpNhrpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpUsageState.setStatus("mandatory")
_VrIpNhrpOperStatusTable_Object = MibTable
vrIpNhrpOperStatusTable = _VrIpNhrpOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 14)
)
if mibBuilder.loadTexts:
    vrIpNhrpOperStatusTable.setStatus("mandatory")
_VrIpNhrpOperStatusEntry_Object = MibTableRow
vrIpNhrpOperStatusEntry = _VrIpNhrpOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 14, 1)
)
vrIpNhrpOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpIndex"),
)
if mibBuilder.loadTexts:
    vrIpNhrpOperStatusEntry.setStatus("mandatory")


class _VrIpNhrpSnmpOperStatus_Type(Integer32):
    """Custom type vrIpNhrpSnmpOperStatus based on Integer32"""
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


_VrIpNhrpSnmpOperStatus_Type.__name__ = "Integer32"
_VrIpNhrpSnmpOperStatus_Object = MibTableColumn
vrIpNhrpSnmpOperStatus = _VrIpNhrpSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 14, 1, 1),
    _VrIpNhrpSnmpOperStatus_Type()
)
vrIpNhrpSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpSnmpOperStatus.setStatus("mandatory")
_VrIpNhrpOperTable_Object = MibTable
vrIpNhrpOperTable = _VrIpNhrpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 15)
)
if mibBuilder.loadTexts:
    vrIpNhrpOperTable.setStatus("mandatory")
_VrIpNhrpOperEntry_Object = MibTableRow
vrIpNhrpOperEntry = _VrIpNhrpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 15, 1)
)
vrIpNhrpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpNhrpMIB", "vrIpNhrpIndex"),
)
if mibBuilder.loadTexts:
    vrIpNhrpOperEntry.setStatus("mandatory")


class _VrIpNhrpCurrResCacheEntries_Type(Unsigned32):
    """Custom type vrIpNhrpCurrResCacheEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4292967295),
    )


_VrIpNhrpCurrResCacheEntries_Type.__name__ = "Unsigned32"
_VrIpNhrpCurrResCacheEntries_Object = MibTableColumn
vrIpNhrpCurrResCacheEntries = _VrIpNhrpCurrResCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 15, 1, 1),
    _VrIpNhrpCurrResCacheEntries_Type()
)
vrIpNhrpCurrResCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpCurrResCacheEntries.setStatus("mandatory")


class _VrIpNhrpPeakResCacheEntries_Type(Unsigned32):
    """Custom type vrIpNhrpPeakResCacheEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4292967295),
    )


_VrIpNhrpPeakResCacheEntries_Type.__name__ = "Unsigned32"
_VrIpNhrpPeakResCacheEntries_Object = MibTableColumn
vrIpNhrpPeakResCacheEntries = _VrIpNhrpPeakResCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 19, 15, 1, 2),
    _VrIpNhrpPeakResCacheEntries_Type()
)
vrIpNhrpPeakResCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNhrpPeakResCacheEntries.setStatus("mandatory")
_IpNhrpMIB_ObjectIdentity = ObjectIdentity
ipNhrpMIB = _IpNhrpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 77)
)
_IpNhrpGroup_ObjectIdentity = ObjectIdentity
ipNhrpGroup = _IpNhrpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 77, 1)
)
_IpNhrpGroupBE_ObjectIdentity = ObjectIdentity
ipNhrpGroupBE = _IpNhrpGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 77, 1, 5)
)
_IpNhrpGroupBE01_ObjectIdentity = ObjectIdentity
ipNhrpGroupBE01 = _IpNhrpGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 77, 1, 5, 2)
)
_IpNhrpGroupBE01A_ObjectIdentity = ObjectIdentity
ipNhrpGroupBE01A = _IpNhrpGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 77, 1, 5, 2, 2)
)
_IpNhrpCapabilities_ObjectIdentity = ObjectIdentity
ipNhrpCapabilities = _IpNhrpCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 77, 3)
)
_IpNhrpCapabilitiesBE_ObjectIdentity = ObjectIdentity
ipNhrpCapabilitiesBE = _IpNhrpCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 77, 3, 5)
)
_IpNhrpCapabilitiesBE01_ObjectIdentity = ObjectIdentity
ipNhrpCapabilitiesBE01 = _IpNhrpCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 77, 3, 5, 2)
)
_IpNhrpCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
ipNhrpCapabilitiesBE01A = _IpNhrpCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 77, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-IpNhrpMIB",
    **{"vrPpIpPortLogicalIfNhrpIf": vrPpIpPortLogicalIfNhrpIf,
       "vrPpIpPortLogicalIfNhrpIfRowStatusTable": vrPpIpPortLogicalIfNhrpIfRowStatusTable,
       "vrPpIpPortLogicalIfNhrpIfRowStatusEntry": vrPpIpPortLogicalIfNhrpIfRowStatusEntry,
       "vrPpIpPortLogicalIfNhrpIfRowStatus": vrPpIpPortLogicalIfNhrpIfRowStatus,
       "vrPpIpPortLogicalIfNhrpIfComponentName": vrPpIpPortLogicalIfNhrpIfComponentName,
       "vrPpIpPortLogicalIfNhrpIfStorageType": vrPpIpPortLogicalIfNhrpIfStorageType,
       "vrPpIpPortLogicalIfNhrpIfIndex": vrPpIpPortLogicalIfNhrpIfIndex,
       "vrIpNhrp": vrIpNhrp,
       "vrIpNhrpRowStatusTable": vrIpNhrpRowStatusTable,
       "vrIpNhrpRowStatusEntry": vrIpNhrpRowStatusEntry,
       "vrIpNhrpRowStatus": vrIpNhrpRowStatus,
       "vrIpNhrpComponentName": vrIpNhrpComponentName,
       "vrIpNhrpStorageType": vrIpNhrpStorageType,
       "vrIpNhrpIndex": vrIpNhrpIndex,
       "vrIpNhrpNhs": vrIpNhrpNhs,
       "vrIpNhrpNhsRowStatusTable": vrIpNhrpNhsRowStatusTable,
       "vrIpNhrpNhsRowStatusEntry": vrIpNhrpNhsRowStatusEntry,
       "vrIpNhrpNhsRowStatus": vrIpNhrpNhsRowStatus,
       "vrIpNhrpNhsComponentName": vrIpNhrpNhsComponentName,
       "vrIpNhrpNhsStorageType": vrIpNhrpNhsStorageType,
       "vrIpNhrpNhsIndex": vrIpNhrpNhsIndex,
       "vrIpNhrpNhsEp": vrIpNhrpNhsEp,
       "vrIpNhrpNhsEpRowStatusTable": vrIpNhrpNhsEpRowStatusTable,
       "vrIpNhrpNhsEpRowStatusEntry": vrIpNhrpNhsEpRowStatusEntry,
       "vrIpNhrpNhsEpRowStatus": vrIpNhrpNhsEpRowStatus,
       "vrIpNhrpNhsEpComponentName": vrIpNhrpNhsEpComponentName,
       "vrIpNhrpNhsEpStorageType": vrIpNhrpNhsEpStorageType,
       "vrIpNhrpNhsEpIndex": vrIpNhrpNhsEpIndex,
       "vrIpNhrpNhsEpNetAddr": vrIpNhrpNhsEpNetAddr,
       "vrIpNhrpNhsEpNetAddrRowStatusTable": vrIpNhrpNhsEpNetAddrRowStatusTable,
       "vrIpNhrpNhsEpNetAddrRowStatusEntry": vrIpNhrpNhsEpNetAddrRowStatusEntry,
       "vrIpNhrpNhsEpNetAddrRowStatus": vrIpNhrpNhsEpNetAddrRowStatus,
       "vrIpNhrpNhsEpNetAddrComponentName": vrIpNhrpNhsEpNetAddrComponentName,
       "vrIpNhrpNhsEpNetAddrStorageType": vrIpNhrpNhsEpNetAddrStorageType,
       "vrIpNhrpNhsEpNetAddrIndex": vrIpNhrpNhsEpNetAddrIndex,
       "vrIpNhrpNhsEpNetAddrProvTable": vrIpNhrpNhsEpNetAddrProvTable,
       "vrIpNhrpNhsEpNetAddrProvEntry": vrIpNhrpNhsEpNetAddrProvEntry,
       "vrIpNhrpNhsEpNetAddrSourceAddress": vrIpNhrpNhsEpNetAddrSourceAddress,
       "vrIpNhrpNhsEpNetAddrSourceMask": vrIpNhrpNhsEpNetAddrSourceMask,
       "vrIpNhrpNhsEpNetAddrDestinationAddress": vrIpNhrpNhsEpNetAddrDestinationAddress,
       "vrIpNhrpNhsEpNetAddrDestinationMask": vrIpNhrpNhsEpNetAddrDestinationMask,
       "vrIpNhrpNhsEpProvTable": vrIpNhrpNhsEpProvTable,
       "vrIpNhrpNhsEpProvEntry": vrIpNhrpNhsEpProvEntry,
       "vrIpNhrpNhsEpAction": vrIpNhrpNhsEpAction,
       "vrIpNhrpNhsEpProtocol": vrIpNhrpNhsEpProtocol,
       "vrIpNhrpNhsStatsTable": vrIpNhrpNhsStatsTable,
       "vrIpNhrpNhsStatsEntry": vrIpNhrpNhsStatsEntry,
       "vrIpNhrpNhsRxResolveReq": vrIpNhrpNhsRxResolveReq,
       "vrIpNhrpNhsTxResolveReplyAck": vrIpNhrpNhsTxResolveReplyAck,
       "vrIpNhrpNhsTxResolveReplyNakProhibited": vrIpNhrpNhsTxResolveReplyNakProhibited,
       "vrIpNhrpNhsTxResolveReplyNakInsufResources": vrIpNhrpNhsTxResolveReplyNakInsufResources,
       "vrIpNhrpNhsTxResolveReplyNakNoBinding": vrIpNhrpNhsTxResolveReplyNakNoBinding,
       "vrIpNhrpNhsTxResolveReplyNakNotUnique": vrIpNhrpNhsTxResolveReplyNakNotUnique,
       "vrIpNhrpNhsRxRegisterReq": vrIpNhrpNhsRxRegisterReq,
       "vrIpNhrpNhsRxPurgeReq": vrIpNhrpNhsRxPurgeReq,
       "vrIpNhrpNhsTxPurgeReq": vrIpNhrpNhsTxPurgeReq,
       "vrIpNhrpNhsRxPurgeReply": vrIpNhrpNhsRxPurgeReply,
       "vrIpNhrpNhsTxPurgeReply": vrIpNhrpNhsTxPurgeReply,
       "vrIpNhrpNhsRxErrUnrecognizedExtension": vrIpNhrpNhsRxErrUnrecognizedExtension,
       "vrIpNhrpNhsRxErrLoopDetected": vrIpNhrpNhsRxErrLoopDetected,
       "vrIpNhrpNhsRxErrProtoAddrUnreachable": vrIpNhrpNhsRxErrProtoAddrUnreachable,
       "vrIpNhrpNhsRxErrProtoError": vrIpNhrpNhsRxErrProtoError,
       "vrIpNhrpNhsRxErrSduSizeExceeded": vrIpNhrpNhsRxErrSduSizeExceeded,
       "vrIpNhrpNhsRxErrInvalidExtension": vrIpNhrpNhsRxErrInvalidExtension,
       "vrIpNhrpNhsRxErrInvalidResReplyReceived": vrIpNhrpNhsRxErrInvalidResReplyReceived,
       "vrIpNhrpNhsRxErrAuthenticationFailure": vrIpNhrpNhsRxErrAuthenticationFailure,
       "vrIpNhrpNhsRxErrHopCountExceeded": vrIpNhrpNhsRxErrHopCountExceeded,
       "vrIpNhrpNhsTxErrUnrecognizedExtension": vrIpNhrpNhsTxErrUnrecognizedExtension,
       "vrIpNhrpNhsTxErrLoopDetected": vrIpNhrpNhsTxErrLoopDetected,
       "vrIpNhrpNhsTxErrProtoAddrUnreachable": vrIpNhrpNhsTxErrProtoAddrUnreachable,
       "vrIpNhrpNhsTxErrProtoError": vrIpNhrpNhsTxErrProtoError,
       "vrIpNhrpNhsTxErrSduSizeExceeded": vrIpNhrpNhsTxErrSduSizeExceeded,
       "vrIpNhrpNhsTxErrInvalidExtension": vrIpNhrpNhsTxErrInvalidExtension,
       "vrIpNhrpNhsTxErrAuthenticationFailure": vrIpNhrpNhsTxErrAuthenticationFailure,
       "vrIpNhrpNhsTxErrHopCountExceeded": vrIpNhrpNhsTxErrHopCountExceeded,
       "vrIpNhrpNhsFwdResolveReq": vrIpNhrpNhsFwdResolveReq,
       "vrIpNhrpNhsFwdResolveReply": vrIpNhrpNhsFwdResolveReply,
       "vrIpNhrpNhsFwdRegisterReq": vrIpNhrpNhsFwdRegisterReq,
       "vrIpNhrpNhsFwdRegisterReply": vrIpNhrpNhsFwdRegisterReply,
       "vrIpNhrpNhsFwdPurgeReq": vrIpNhrpNhsFwdPurgeReq,
       "vrIpNhrpNhsFwdPurgeReply": vrIpNhrpNhsFwdPurgeReply,
       "vrIpNhrpNhsFwdErrorIndication": vrIpNhrpNhsFwdErrorIndication,
       "vrIpNhrpNhc": vrIpNhrpNhc,
       "vrIpNhrpNhcRowStatusTable": vrIpNhrpNhcRowStatusTable,
       "vrIpNhrpNhcRowStatusEntry": vrIpNhrpNhcRowStatusEntry,
       "vrIpNhrpNhcRowStatus": vrIpNhrpNhcRowStatus,
       "vrIpNhrpNhcComponentName": vrIpNhrpNhcComponentName,
       "vrIpNhrpNhcStorageType": vrIpNhrpNhcStorageType,
       "vrIpNhrpNhcIndex": vrIpNhrpNhcIndex,
       "vrIpNhrpNhcProvTable": vrIpNhrpNhcProvTable,
       "vrIpNhrpNhcProvEntry": vrIpNhrpNhcProvEntry,
       "vrIpNhrpNhcFlowDetectPacketCount": vrIpNhrpNhcFlowDetectPacketCount,
       "vrIpNhrpNhcFlowDetectTimePeriod": vrIpNhrpNhcFlowDetectTimePeriod,
       "vrIpNhrpNhcIdleDetectPacketCount": vrIpNhrpNhcIdleDetectPacketCount,
       "vrIpNhrpNhcIdleDetectTimePeriod": vrIpNhrpNhcIdleDetectTimePeriod,
       "vrIpNhrpNhcAtmFlowDetection": vrIpNhrpNhcAtmFlowDetection,
       "vrIpNhrpNhcStatsTable": vrIpNhrpNhcStatsTable,
       "vrIpNhrpNhcStatsEntry": vrIpNhrpNhcStatsEntry,
       "vrIpNhrpNhcTxResolveReq": vrIpNhrpNhcTxResolveReq,
       "vrIpNhrpNhcRxResolveReplyAck": vrIpNhrpNhcRxResolveReplyAck,
       "vrIpNhrpNhcRxResolveReplyNakProhibited": vrIpNhrpNhcRxResolveReplyNakProhibited,
       "vrIpNhrpNhcRxResolveReplyNakInsufResources": vrIpNhrpNhcRxResolveReplyNakInsufResources,
       "vrIpNhrpNhcRxResolveReplyNakNoBinding": vrIpNhrpNhcRxResolveReplyNakNoBinding,
       "vrIpNhrpNhcRxResolveReplyNakNotUnique": vrIpNhrpNhcRxResolveReplyNakNotUnique,
       "vrIpNhrpNhcRxPurgeReq": vrIpNhrpNhcRxPurgeReq,
       "vrIpNhrpNhcTxPurgeReq": vrIpNhrpNhcTxPurgeReq,
       "vrIpNhrpNhcRxPurgeReply": vrIpNhrpNhcRxPurgeReply,
       "vrIpNhrpNhcTxPurgeReply": vrIpNhrpNhcTxPurgeReply,
       "vrIpNhrpNhcTxErrIndication": vrIpNhrpNhcTxErrIndication,
       "vrIpNhrpNhcRxErrUnrecognizedExtension": vrIpNhrpNhcRxErrUnrecognizedExtension,
       "vrIpNhrpNhcRxErrLoopDetected": vrIpNhrpNhcRxErrLoopDetected,
       "vrIpNhrpNhcRxErrProtoAddrUnreachable": vrIpNhrpNhcRxErrProtoAddrUnreachable,
       "vrIpNhrpNhcRxErrProtoError": vrIpNhrpNhcRxErrProtoError,
       "vrIpNhrpNhcRxErrSduSizeExceeded": vrIpNhrpNhcRxErrSduSizeExceeded,
       "vrIpNhrpNhcRxErrInvalidExtension": vrIpNhrpNhcRxErrInvalidExtension,
       "vrIpNhrpNhcRxErrAuthenticationFailure": vrIpNhrpNhcRxErrAuthenticationFailure,
       "vrIpNhrpNhcRxErrHopCountExceeded": vrIpNhrpNhcRxErrHopCountExceeded,
       "vrIpNhrpRce": vrIpNhrpRce,
       "vrIpNhrpRceRowStatusTable": vrIpNhrpRceRowStatusTable,
       "vrIpNhrpRceRowStatusEntry": vrIpNhrpRceRowStatusEntry,
       "vrIpNhrpRceRowStatus": vrIpNhrpRceRowStatus,
       "vrIpNhrpRceComponentName": vrIpNhrpRceComponentName,
       "vrIpNhrpRceStorageType": vrIpNhrpRceStorageType,
       "vrIpNhrpRceDestAddrIndex": vrIpNhrpRceDestAddrIndex,
       "vrIpNhrpRceDestMaskIndex": vrIpNhrpRceDestMaskIndex,
       "vrIpNhrpRceOperTable": vrIpNhrpRceOperTable,
       "vrIpNhrpRceOperEntry": vrIpNhrpRceOperEntry,
       "vrIpNhrpRceNbmaAddress": vrIpNhrpRceNbmaAddress,
       "vrIpNhrpRceEntryState": vrIpNhrpRceEntryState,
       "vrIpNhrpRceHoldingTime": vrIpNhrpRceHoldingTime,
       "vrIpNhrpRceShortcut": vrIpNhrpRceShortcut,
       "vrIpNhrpAdminControlTable": vrIpNhrpAdminControlTable,
       "vrIpNhrpAdminControlEntry": vrIpNhrpAdminControlEntry,
       "vrIpNhrpSnmpAdminStatus": vrIpNhrpSnmpAdminStatus,
       "vrIpNhrpProvTable": vrIpNhrpProvTable,
       "vrIpNhrpProvEntry": vrIpNhrpProvEntry,
       "vrIpNhrpMaxResCacheEntries": vrIpNhrpMaxResCacheEntries,
       "vrIpNhrpFwdTransitRecord": vrIpNhrpFwdTransitRecord,
       "vrIpNhrpRevTransitRecord": vrIpNhrpRevTransitRecord,
       "vrIpNhrpStateTable": vrIpNhrpStateTable,
       "vrIpNhrpStateEntry": vrIpNhrpStateEntry,
       "vrIpNhrpAdminState": vrIpNhrpAdminState,
       "vrIpNhrpOperationalState": vrIpNhrpOperationalState,
       "vrIpNhrpUsageState": vrIpNhrpUsageState,
       "vrIpNhrpOperStatusTable": vrIpNhrpOperStatusTable,
       "vrIpNhrpOperStatusEntry": vrIpNhrpOperStatusEntry,
       "vrIpNhrpSnmpOperStatus": vrIpNhrpSnmpOperStatus,
       "vrIpNhrpOperTable": vrIpNhrpOperTable,
       "vrIpNhrpOperEntry": vrIpNhrpOperEntry,
       "vrIpNhrpCurrResCacheEntries": vrIpNhrpCurrResCacheEntries,
       "vrIpNhrpPeakResCacheEntries": vrIpNhrpPeakResCacheEntries,
       "ipNhrpMIB": ipNhrpMIB,
       "ipNhrpGroup": ipNhrpGroup,
       "ipNhrpGroupBE": ipNhrpGroupBE,
       "ipNhrpGroupBE01": ipNhrpGroupBE01,
       "ipNhrpGroupBE01A": ipNhrpGroupBE01A,
       "ipNhrpCapabilities": ipNhrpCapabilities,
       "ipNhrpCapabilitiesBE": ipNhrpCapabilitiesBE,
       "ipNhrpCapabilitiesBE01": ipNhrpCapabilitiesBE01,
       "ipNhrpCapabilitiesBE01A": ipNhrpCapabilitiesBE01A}
)
