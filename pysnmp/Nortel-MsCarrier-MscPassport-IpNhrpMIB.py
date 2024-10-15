# SNMP MIB module (Nortel-MsCarrier-MscPassport-IpNhrpMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-IpNhrpMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:40 2024
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
 mscVrIpIndex,
 mscVrPpIpPortIndex,
 mscVrPpIpPortLogicalIf,
 mscVrPpIpPortLogicalIfAddressIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-IpMIB",
    "mscVrIp",
    "mscVrIpIndex",
    "mscVrPpIpPortIndex",
    "mscVrPpIpPortLogicalIf",
    "mscVrPpIpPortLogicalIfAddressIndex")

(Counter32,
 DisplayString,
 Integer32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(HexString,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "HexString",
    "NonReplicated")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscPassportMIBs")

(mscVrIndex,
 mscVrPpIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-VirtualRouterMIB",
    "mscVrIndex",
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

_MscVrPpIpPortLogicalIfNhrpIf_ObjectIdentity = ObjectIdentity
mscVrPpIpPortLogicalIfNhrpIf = _MscVrPpIpPortLogicalIfNhrpIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 4)
)
_MscVrPpIpPortLogicalIfNhrpIfRowStatusTable_Object = MibTable
mscVrPpIpPortLogicalIfNhrpIfRowStatusTable = _MscVrPpIpPortLogicalIfNhrpIfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 4, 1)
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfNhrpIfRowStatusTable.setStatus("mandatory")
_MscVrPpIpPortLogicalIfNhrpIfRowStatusEntry_Object = MibTableRow
mscVrPpIpPortLogicalIfNhrpIfRowStatusEntry = _MscVrPpIpPortLogicalIfNhrpIfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 4, 1, 1)
)
mscVrPpIpPortLogicalIfNhrpIfRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrPpIpPortLogicalIfNhrpIfIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfNhrpIfRowStatusEntry.setStatus("mandatory")
_MscVrPpIpPortLogicalIfNhrpIfRowStatus_Type = RowStatus
_MscVrPpIpPortLogicalIfNhrpIfRowStatus_Object = MibTableColumn
mscVrPpIpPortLogicalIfNhrpIfRowStatus = _MscVrPpIpPortLogicalIfNhrpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 4, 1, 1, 1),
    _MscVrPpIpPortLogicalIfNhrpIfRowStatus_Type()
)
mscVrPpIpPortLogicalIfNhrpIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfNhrpIfRowStatus.setStatus("mandatory")
_MscVrPpIpPortLogicalIfNhrpIfComponentName_Type = DisplayString
_MscVrPpIpPortLogicalIfNhrpIfComponentName_Object = MibTableColumn
mscVrPpIpPortLogicalIfNhrpIfComponentName = _MscVrPpIpPortLogicalIfNhrpIfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 4, 1, 1, 2),
    _MscVrPpIpPortLogicalIfNhrpIfComponentName_Type()
)
mscVrPpIpPortLogicalIfNhrpIfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfNhrpIfComponentName.setStatus("mandatory")
_MscVrPpIpPortLogicalIfNhrpIfStorageType_Type = StorageType
_MscVrPpIpPortLogicalIfNhrpIfStorageType_Object = MibTableColumn
mscVrPpIpPortLogicalIfNhrpIfStorageType = _MscVrPpIpPortLogicalIfNhrpIfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 4, 1, 1, 4),
    _MscVrPpIpPortLogicalIfNhrpIfStorageType_Type()
)
mscVrPpIpPortLogicalIfNhrpIfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfNhrpIfStorageType.setStatus("mandatory")
_MscVrPpIpPortLogicalIfNhrpIfIndex_Type = NonReplicated
_MscVrPpIpPortLogicalIfNhrpIfIndex_Object = MibTableColumn
mscVrPpIpPortLogicalIfNhrpIfIndex = _MscVrPpIpPortLogicalIfNhrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 5, 2, 4, 1, 1, 10),
    _MscVrPpIpPortLogicalIfNhrpIfIndex_Type()
)
mscVrPpIpPortLogicalIfNhrpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpIpPortLogicalIfNhrpIfIndex.setStatus("mandatory")
_MscVrIpNhrp_ObjectIdentity = ObjectIdentity
mscVrIpNhrp = _MscVrIpNhrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19)
)
_MscVrIpNhrpRowStatusTable_Object = MibTable
mscVrIpNhrpRowStatusTable = _MscVrIpNhrpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 1)
)
if mibBuilder.loadTexts:
    mscVrIpNhrpRowStatusTable.setStatus("mandatory")
_MscVrIpNhrpRowStatusEntry_Object = MibTableRow
mscVrIpNhrpRowStatusEntry = _MscVrIpNhrpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 1, 1)
)
mscVrIpNhrpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpNhrpRowStatusEntry.setStatus("mandatory")
_MscVrIpNhrpRowStatus_Type = RowStatus
_MscVrIpNhrpRowStatus_Object = MibTableColumn
mscVrIpNhrpRowStatus = _MscVrIpNhrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 1, 1, 1),
    _MscVrIpNhrpRowStatus_Type()
)
mscVrIpNhrpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNhrpRowStatus.setStatus("mandatory")
_MscVrIpNhrpComponentName_Type = DisplayString
_MscVrIpNhrpComponentName_Object = MibTableColumn
mscVrIpNhrpComponentName = _MscVrIpNhrpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 1, 1, 2),
    _MscVrIpNhrpComponentName_Type()
)
mscVrIpNhrpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpComponentName.setStatus("mandatory")
_MscVrIpNhrpStorageType_Type = StorageType
_MscVrIpNhrpStorageType_Object = MibTableColumn
mscVrIpNhrpStorageType = _MscVrIpNhrpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 1, 1, 4),
    _MscVrIpNhrpStorageType_Type()
)
mscVrIpNhrpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpStorageType.setStatus("mandatory")
_MscVrIpNhrpIndex_Type = NonReplicated
_MscVrIpNhrpIndex_Object = MibTableColumn
mscVrIpNhrpIndex = _MscVrIpNhrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 1, 1, 10),
    _MscVrIpNhrpIndex_Type()
)
mscVrIpNhrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpNhrpIndex.setStatus("mandatory")
_MscVrIpNhrpNhs_ObjectIdentity = ObjectIdentity
mscVrIpNhrpNhs = _MscVrIpNhrpNhs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2)
)
_MscVrIpNhrpNhsRowStatusTable_Object = MibTable
mscVrIpNhrpNhsRowStatusTable = _MscVrIpNhrpNhsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsRowStatusTable.setStatus("mandatory")
_MscVrIpNhrpNhsRowStatusEntry_Object = MibTableRow
mscVrIpNhrpNhsRowStatusEntry = _MscVrIpNhrpNhsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 1, 1)
)
mscVrIpNhrpNhsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpNhsIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsRowStatusEntry.setStatus("mandatory")
_MscVrIpNhrpNhsRowStatus_Type = RowStatus
_MscVrIpNhrpNhsRowStatus_Object = MibTableColumn
mscVrIpNhrpNhsRowStatus = _MscVrIpNhrpNhsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 1, 1, 1),
    _MscVrIpNhrpNhsRowStatus_Type()
)
mscVrIpNhrpNhsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsRowStatus.setStatus("mandatory")
_MscVrIpNhrpNhsComponentName_Type = DisplayString
_MscVrIpNhrpNhsComponentName_Object = MibTableColumn
mscVrIpNhrpNhsComponentName = _MscVrIpNhrpNhsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 1, 1, 2),
    _MscVrIpNhrpNhsComponentName_Type()
)
mscVrIpNhrpNhsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsComponentName.setStatus("mandatory")
_MscVrIpNhrpNhsStorageType_Type = StorageType
_MscVrIpNhrpNhsStorageType_Object = MibTableColumn
mscVrIpNhrpNhsStorageType = _MscVrIpNhrpNhsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 1, 1, 4),
    _MscVrIpNhrpNhsStorageType_Type()
)
mscVrIpNhrpNhsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsStorageType.setStatus("mandatory")
_MscVrIpNhrpNhsIndex_Type = NonReplicated
_MscVrIpNhrpNhsIndex_Object = MibTableColumn
mscVrIpNhrpNhsIndex = _MscVrIpNhrpNhsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 1, 1, 10),
    _MscVrIpNhrpNhsIndex_Type()
)
mscVrIpNhrpNhsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsIndex.setStatus("mandatory")
_MscVrIpNhrpNhsEp_ObjectIdentity = ObjectIdentity
mscVrIpNhrpNhsEp = _MscVrIpNhrpNhsEp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 2)
)
_MscVrIpNhrpNhsEpRowStatusTable_Object = MibTable
mscVrIpNhrpNhsEpRowStatusTable = _MscVrIpNhrpNhsEpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsEpRowStatusTable.setStatus("mandatory")
_MscVrIpNhrpNhsEpRowStatusEntry_Object = MibTableRow
mscVrIpNhrpNhsEpRowStatusEntry = _MscVrIpNhrpNhsEpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 2, 1, 1)
)
mscVrIpNhrpNhsEpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpNhsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpNhsEpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsEpRowStatusEntry.setStatus("mandatory")
_MscVrIpNhrpNhsEpRowStatus_Type = RowStatus
_MscVrIpNhrpNhsEpRowStatus_Object = MibTableColumn
mscVrIpNhrpNhsEpRowStatus = _MscVrIpNhrpNhsEpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 2, 1, 1, 1),
    _MscVrIpNhrpNhsEpRowStatus_Type()
)
mscVrIpNhrpNhsEpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsEpRowStatus.setStatus("mandatory")
_MscVrIpNhrpNhsEpComponentName_Type = DisplayString
_MscVrIpNhrpNhsEpComponentName_Object = MibTableColumn
mscVrIpNhrpNhsEpComponentName = _MscVrIpNhrpNhsEpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 2, 1, 1, 2),
    _MscVrIpNhrpNhsEpComponentName_Type()
)
mscVrIpNhrpNhsEpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsEpComponentName.setStatus("mandatory")
_MscVrIpNhrpNhsEpStorageType_Type = StorageType
_MscVrIpNhrpNhsEpStorageType_Object = MibTableColumn
mscVrIpNhrpNhsEpStorageType = _MscVrIpNhrpNhsEpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 2, 1, 1, 4),
    _MscVrIpNhrpNhsEpStorageType_Type()
)
mscVrIpNhrpNhsEpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsEpStorageType.setStatus("mandatory")


class _MscVrIpNhrpNhsEpIndex_Type(Integer32):
    """Custom type mscVrIpNhrpNhsEpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpNhrpNhsEpIndex_Type.__name__ = "Integer32"
_MscVrIpNhrpNhsEpIndex_Object = MibTableColumn
mscVrIpNhrpNhsEpIndex = _MscVrIpNhrpNhsEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 2, 1, 1, 10),
    _MscVrIpNhrpNhsEpIndex_Type()
)
mscVrIpNhrpNhsEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsEpIndex.setStatus("mandatory")
_MscVrIpNhrpNhsEpNetAddr_ObjectIdentity = ObjectIdentity
mscVrIpNhrpNhsEpNetAddr = _MscVrIpNhrpNhsEpNetAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 2, 2)
)
_MscVrIpNhrpNhsEpNetAddrRowStatusTable_Object = MibTable
mscVrIpNhrpNhsEpNetAddrRowStatusTable = _MscVrIpNhrpNhsEpNetAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsEpNetAddrRowStatusTable.setStatus("mandatory")
_MscVrIpNhrpNhsEpNetAddrRowStatusEntry_Object = MibTableRow
mscVrIpNhrpNhsEpNetAddrRowStatusEntry = _MscVrIpNhrpNhsEpNetAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 2, 2, 1, 1)
)
mscVrIpNhrpNhsEpNetAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpNhsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpNhsEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpNhsEpNetAddrIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsEpNetAddrRowStatusEntry.setStatus("mandatory")
_MscVrIpNhrpNhsEpNetAddrRowStatus_Type = RowStatus
_MscVrIpNhrpNhsEpNetAddrRowStatus_Object = MibTableColumn
mscVrIpNhrpNhsEpNetAddrRowStatus = _MscVrIpNhrpNhsEpNetAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 2, 2, 1, 1, 1),
    _MscVrIpNhrpNhsEpNetAddrRowStatus_Type()
)
mscVrIpNhrpNhsEpNetAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsEpNetAddrRowStatus.setStatus("mandatory")
_MscVrIpNhrpNhsEpNetAddrComponentName_Type = DisplayString
_MscVrIpNhrpNhsEpNetAddrComponentName_Object = MibTableColumn
mscVrIpNhrpNhsEpNetAddrComponentName = _MscVrIpNhrpNhsEpNetAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 2, 2, 1, 1, 2),
    _MscVrIpNhrpNhsEpNetAddrComponentName_Type()
)
mscVrIpNhrpNhsEpNetAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsEpNetAddrComponentName.setStatus("mandatory")
_MscVrIpNhrpNhsEpNetAddrStorageType_Type = StorageType
_MscVrIpNhrpNhsEpNetAddrStorageType_Object = MibTableColumn
mscVrIpNhrpNhsEpNetAddrStorageType = _MscVrIpNhrpNhsEpNetAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 2, 2, 1, 1, 4),
    _MscVrIpNhrpNhsEpNetAddrStorageType_Type()
)
mscVrIpNhrpNhsEpNetAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsEpNetAddrStorageType.setStatus("mandatory")


class _MscVrIpNhrpNhsEpNetAddrIndex_Type(Integer32):
    """Custom type mscVrIpNhrpNhsEpNetAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpNhrpNhsEpNetAddrIndex_Type.__name__ = "Integer32"
_MscVrIpNhrpNhsEpNetAddrIndex_Object = MibTableColumn
mscVrIpNhrpNhsEpNetAddrIndex = _MscVrIpNhrpNhsEpNetAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 2, 2, 1, 1, 10),
    _MscVrIpNhrpNhsEpNetAddrIndex_Type()
)
mscVrIpNhrpNhsEpNetAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsEpNetAddrIndex.setStatus("mandatory")
_MscVrIpNhrpNhsEpNetAddrProvTable_Object = MibTable
mscVrIpNhrpNhsEpNetAddrProvTable = _MscVrIpNhrpNhsEpNetAddrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsEpNetAddrProvTable.setStatus("mandatory")
_MscVrIpNhrpNhsEpNetAddrProvEntry_Object = MibTableRow
mscVrIpNhrpNhsEpNetAddrProvEntry = _MscVrIpNhrpNhsEpNetAddrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 2, 2, 10, 1)
)
mscVrIpNhrpNhsEpNetAddrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpNhsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpNhsEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpNhsEpNetAddrIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsEpNetAddrProvEntry.setStatus("mandatory")


class _MscVrIpNhrpNhsEpNetAddrSourceAddress_Type(IpAddress):
    """Custom type mscVrIpNhrpNhsEpNetAddrSourceAddress based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrIpNhrpNhsEpNetAddrSourceAddress_Object = MibTableColumn
mscVrIpNhrpNhsEpNetAddrSourceAddress = _MscVrIpNhrpNhsEpNetAddrSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 2, 2, 10, 1, 1),
    _MscVrIpNhrpNhsEpNetAddrSourceAddress_Type()
)
mscVrIpNhrpNhsEpNetAddrSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsEpNetAddrSourceAddress.setStatus("mandatory")


class _MscVrIpNhrpNhsEpNetAddrSourceMask_Type(IpAddress):
    """Custom type mscVrIpNhrpNhsEpNetAddrSourceMask based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrIpNhrpNhsEpNetAddrSourceMask_Object = MibTableColumn
mscVrIpNhrpNhsEpNetAddrSourceMask = _MscVrIpNhrpNhsEpNetAddrSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 2, 2, 10, 1, 2),
    _MscVrIpNhrpNhsEpNetAddrSourceMask_Type()
)
mscVrIpNhrpNhsEpNetAddrSourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsEpNetAddrSourceMask.setStatus("mandatory")


class _MscVrIpNhrpNhsEpNetAddrDestinationAddress_Type(IpAddress):
    """Custom type mscVrIpNhrpNhsEpNetAddrDestinationAddress based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrIpNhrpNhsEpNetAddrDestinationAddress_Object = MibTableColumn
mscVrIpNhrpNhsEpNetAddrDestinationAddress = _MscVrIpNhrpNhsEpNetAddrDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 2, 2, 10, 1, 3),
    _MscVrIpNhrpNhsEpNetAddrDestinationAddress_Type()
)
mscVrIpNhrpNhsEpNetAddrDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsEpNetAddrDestinationAddress.setStatus("mandatory")


class _MscVrIpNhrpNhsEpNetAddrDestinationMask_Type(IpAddress):
    """Custom type mscVrIpNhrpNhsEpNetAddrDestinationMask based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrIpNhrpNhsEpNetAddrDestinationMask_Object = MibTableColumn
mscVrIpNhrpNhsEpNetAddrDestinationMask = _MscVrIpNhrpNhsEpNetAddrDestinationMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 2, 2, 10, 1, 4),
    _MscVrIpNhrpNhsEpNetAddrDestinationMask_Type()
)
mscVrIpNhrpNhsEpNetAddrDestinationMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsEpNetAddrDestinationMask.setStatus("mandatory")
_MscVrIpNhrpNhsEpProvTable_Object = MibTable
mscVrIpNhrpNhsEpProvTable = _MscVrIpNhrpNhsEpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsEpProvTable.setStatus("mandatory")
_MscVrIpNhrpNhsEpProvEntry_Object = MibTableRow
mscVrIpNhrpNhsEpProvEntry = _MscVrIpNhrpNhsEpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 2, 10, 1)
)
mscVrIpNhrpNhsEpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpNhsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpNhsEpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsEpProvEntry.setStatus("mandatory")


class _MscVrIpNhrpNhsEpAction_Type(Integer32):
    """Custom type mscVrIpNhrpNhsEpAction based on Integer32"""
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


_MscVrIpNhrpNhsEpAction_Type.__name__ = "Integer32"
_MscVrIpNhrpNhsEpAction_Object = MibTableColumn
mscVrIpNhrpNhsEpAction = _MscVrIpNhrpNhsEpAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 2, 10, 1, 1),
    _MscVrIpNhrpNhsEpAction_Type()
)
mscVrIpNhrpNhsEpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsEpAction.setStatus("mandatory")


class _MscVrIpNhrpNhsEpProtocol_Type(Integer32):
    """Custom type mscVrIpNhrpNhsEpProtocol based on Integer32"""
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


_MscVrIpNhrpNhsEpProtocol_Type.__name__ = "Integer32"
_MscVrIpNhrpNhsEpProtocol_Object = MibTableColumn
mscVrIpNhrpNhsEpProtocol = _MscVrIpNhrpNhsEpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 2, 10, 1, 2),
    _MscVrIpNhrpNhsEpProtocol_Type()
)
mscVrIpNhrpNhsEpProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsEpProtocol.setStatus("mandatory")
_MscVrIpNhrpNhsStatsTable_Object = MibTable
mscVrIpNhrpNhsStatsTable = _MscVrIpNhrpNhsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsStatsTable.setStatus("mandatory")
_MscVrIpNhrpNhsStatsEntry_Object = MibTableRow
mscVrIpNhrpNhsStatsEntry = _MscVrIpNhrpNhsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1)
)
mscVrIpNhrpNhsStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpNhsIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsStatsEntry.setStatus("mandatory")
_MscVrIpNhrpNhsRxResolveReq_Type = Counter32
_MscVrIpNhrpNhsRxResolveReq_Object = MibTableColumn
mscVrIpNhrpNhsRxResolveReq = _MscVrIpNhrpNhsRxResolveReq_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 1),
    _MscVrIpNhrpNhsRxResolveReq_Type()
)
mscVrIpNhrpNhsRxResolveReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsRxResolveReq.setStatus("mandatory")
_MscVrIpNhrpNhsTxResolveReplyAck_Type = Counter32
_MscVrIpNhrpNhsTxResolveReplyAck_Object = MibTableColumn
mscVrIpNhrpNhsTxResolveReplyAck = _MscVrIpNhrpNhsTxResolveReplyAck_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 2),
    _MscVrIpNhrpNhsTxResolveReplyAck_Type()
)
mscVrIpNhrpNhsTxResolveReplyAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsTxResolveReplyAck.setStatus("mandatory")
_MscVrIpNhrpNhsTxResolveReplyNakProhibited_Type = Counter32
_MscVrIpNhrpNhsTxResolveReplyNakProhibited_Object = MibTableColumn
mscVrIpNhrpNhsTxResolveReplyNakProhibited = _MscVrIpNhrpNhsTxResolveReplyNakProhibited_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 3),
    _MscVrIpNhrpNhsTxResolveReplyNakProhibited_Type()
)
mscVrIpNhrpNhsTxResolveReplyNakProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsTxResolveReplyNakProhibited.setStatus("mandatory")
_MscVrIpNhrpNhsTxResolveReplyNakInsufResources_Type = Counter32
_MscVrIpNhrpNhsTxResolveReplyNakInsufResources_Object = MibTableColumn
mscVrIpNhrpNhsTxResolveReplyNakInsufResources = _MscVrIpNhrpNhsTxResolveReplyNakInsufResources_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 4),
    _MscVrIpNhrpNhsTxResolveReplyNakInsufResources_Type()
)
mscVrIpNhrpNhsTxResolveReplyNakInsufResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsTxResolveReplyNakInsufResources.setStatus("mandatory")
_MscVrIpNhrpNhsTxResolveReplyNakNoBinding_Type = Counter32
_MscVrIpNhrpNhsTxResolveReplyNakNoBinding_Object = MibTableColumn
mscVrIpNhrpNhsTxResolveReplyNakNoBinding = _MscVrIpNhrpNhsTxResolveReplyNakNoBinding_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 5),
    _MscVrIpNhrpNhsTxResolveReplyNakNoBinding_Type()
)
mscVrIpNhrpNhsTxResolveReplyNakNoBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsTxResolveReplyNakNoBinding.setStatus("mandatory")
_MscVrIpNhrpNhsTxResolveReplyNakNotUnique_Type = Counter32
_MscVrIpNhrpNhsTxResolveReplyNakNotUnique_Object = MibTableColumn
mscVrIpNhrpNhsTxResolveReplyNakNotUnique = _MscVrIpNhrpNhsTxResolveReplyNakNotUnique_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 6),
    _MscVrIpNhrpNhsTxResolveReplyNakNotUnique_Type()
)
mscVrIpNhrpNhsTxResolveReplyNakNotUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsTxResolveReplyNakNotUnique.setStatus("mandatory")
_MscVrIpNhrpNhsRxRegisterReq_Type = Counter32
_MscVrIpNhrpNhsRxRegisterReq_Object = MibTableColumn
mscVrIpNhrpNhsRxRegisterReq = _MscVrIpNhrpNhsRxRegisterReq_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 7),
    _MscVrIpNhrpNhsRxRegisterReq_Type()
)
mscVrIpNhrpNhsRxRegisterReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsRxRegisterReq.setStatus("mandatory")
_MscVrIpNhrpNhsRxPurgeReq_Type = Counter32
_MscVrIpNhrpNhsRxPurgeReq_Object = MibTableColumn
mscVrIpNhrpNhsRxPurgeReq = _MscVrIpNhrpNhsRxPurgeReq_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 12),
    _MscVrIpNhrpNhsRxPurgeReq_Type()
)
mscVrIpNhrpNhsRxPurgeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsRxPurgeReq.setStatus("mandatory")
_MscVrIpNhrpNhsTxPurgeReq_Type = Counter32
_MscVrIpNhrpNhsTxPurgeReq_Object = MibTableColumn
mscVrIpNhrpNhsTxPurgeReq = _MscVrIpNhrpNhsTxPurgeReq_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 13),
    _MscVrIpNhrpNhsTxPurgeReq_Type()
)
mscVrIpNhrpNhsTxPurgeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsTxPurgeReq.setStatus("mandatory")
_MscVrIpNhrpNhsRxPurgeReply_Type = Counter32
_MscVrIpNhrpNhsRxPurgeReply_Object = MibTableColumn
mscVrIpNhrpNhsRxPurgeReply = _MscVrIpNhrpNhsRxPurgeReply_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 14),
    _MscVrIpNhrpNhsRxPurgeReply_Type()
)
mscVrIpNhrpNhsRxPurgeReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsRxPurgeReply.setStatus("mandatory")
_MscVrIpNhrpNhsTxPurgeReply_Type = Counter32
_MscVrIpNhrpNhsTxPurgeReply_Object = MibTableColumn
mscVrIpNhrpNhsTxPurgeReply = _MscVrIpNhrpNhsTxPurgeReply_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 15),
    _MscVrIpNhrpNhsTxPurgeReply_Type()
)
mscVrIpNhrpNhsTxPurgeReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsTxPurgeReply.setStatus("mandatory")
_MscVrIpNhrpNhsRxErrUnrecognizedExtension_Type = Counter32
_MscVrIpNhrpNhsRxErrUnrecognizedExtension_Object = MibTableColumn
mscVrIpNhrpNhsRxErrUnrecognizedExtension = _MscVrIpNhrpNhsRxErrUnrecognizedExtension_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 16),
    _MscVrIpNhrpNhsRxErrUnrecognizedExtension_Type()
)
mscVrIpNhrpNhsRxErrUnrecognizedExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsRxErrUnrecognizedExtension.setStatus("mandatory")
_MscVrIpNhrpNhsRxErrLoopDetected_Type = Counter32
_MscVrIpNhrpNhsRxErrLoopDetected_Object = MibTableColumn
mscVrIpNhrpNhsRxErrLoopDetected = _MscVrIpNhrpNhsRxErrLoopDetected_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 17),
    _MscVrIpNhrpNhsRxErrLoopDetected_Type()
)
mscVrIpNhrpNhsRxErrLoopDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsRxErrLoopDetected.setStatus("mandatory")
_MscVrIpNhrpNhsRxErrProtoAddrUnreachable_Type = Counter32
_MscVrIpNhrpNhsRxErrProtoAddrUnreachable_Object = MibTableColumn
mscVrIpNhrpNhsRxErrProtoAddrUnreachable = _MscVrIpNhrpNhsRxErrProtoAddrUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 18),
    _MscVrIpNhrpNhsRxErrProtoAddrUnreachable_Type()
)
mscVrIpNhrpNhsRxErrProtoAddrUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsRxErrProtoAddrUnreachable.setStatus("mandatory")
_MscVrIpNhrpNhsRxErrProtoError_Type = Counter32
_MscVrIpNhrpNhsRxErrProtoError_Object = MibTableColumn
mscVrIpNhrpNhsRxErrProtoError = _MscVrIpNhrpNhsRxErrProtoError_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 19),
    _MscVrIpNhrpNhsRxErrProtoError_Type()
)
mscVrIpNhrpNhsRxErrProtoError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsRxErrProtoError.setStatus("mandatory")
_MscVrIpNhrpNhsRxErrSduSizeExceeded_Type = Counter32
_MscVrIpNhrpNhsRxErrSduSizeExceeded_Object = MibTableColumn
mscVrIpNhrpNhsRxErrSduSizeExceeded = _MscVrIpNhrpNhsRxErrSduSizeExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 20),
    _MscVrIpNhrpNhsRxErrSduSizeExceeded_Type()
)
mscVrIpNhrpNhsRxErrSduSizeExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsRxErrSduSizeExceeded.setStatus("mandatory")
_MscVrIpNhrpNhsRxErrInvalidExtension_Type = Counter32
_MscVrIpNhrpNhsRxErrInvalidExtension_Object = MibTableColumn
mscVrIpNhrpNhsRxErrInvalidExtension = _MscVrIpNhrpNhsRxErrInvalidExtension_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 21),
    _MscVrIpNhrpNhsRxErrInvalidExtension_Type()
)
mscVrIpNhrpNhsRxErrInvalidExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsRxErrInvalidExtension.setStatus("mandatory")
_MscVrIpNhrpNhsRxErrInvalidResReplyReceived_Type = Counter32
_MscVrIpNhrpNhsRxErrInvalidResReplyReceived_Object = MibTableColumn
mscVrIpNhrpNhsRxErrInvalidResReplyReceived = _MscVrIpNhrpNhsRxErrInvalidResReplyReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 22),
    _MscVrIpNhrpNhsRxErrInvalidResReplyReceived_Type()
)
mscVrIpNhrpNhsRxErrInvalidResReplyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsRxErrInvalidResReplyReceived.setStatus("mandatory")
_MscVrIpNhrpNhsRxErrAuthenticationFailure_Type = Counter32
_MscVrIpNhrpNhsRxErrAuthenticationFailure_Object = MibTableColumn
mscVrIpNhrpNhsRxErrAuthenticationFailure = _MscVrIpNhrpNhsRxErrAuthenticationFailure_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 23),
    _MscVrIpNhrpNhsRxErrAuthenticationFailure_Type()
)
mscVrIpNhrpNhsRxErrAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsRxErrAuthenticationFailure.setStatus("mandatory")
_MscVrIpNhrpNhsRxErrHopCountExceeded_Type = Counter32
_MscVrIpNhrpNhsRxErrHopCountExceeded_Object = MibTableColumn
mscVrIpNhrpNhsRxErrHopCountExceeded = _MscVrIpNhrpNhsRxErrHopCountExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 24),
    _MscVrIpNhrpNhsRxErrHopCountExceeded_Type()
)
mscVrIpNhrpNhsRxErrHopCountExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsRxErrHopCountExceeded.setStatus("mandatory")
_MscVrIpNhrpNhsTxErrUnrecognizedExtension_Type = Counter32
_MscVrIpNhrpNhsTxErrUnrecognizedExtension_Object = MibTableColumn
mscVrIpNhrpNhsTxErrUnrecognizedExtension = _MscVrIpNhrpNhsTxErrUnrecognizedExtension_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 25),
    _MscVrIpNhrpNhsTxErrUnrecognizedExtension_Type()
)
mscVrIpNhrpNhsTxErrUnrecognizedExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsTxErrUnrecognizedExtension.setStatus("mandatory")
_MscVrIpNhrpNhsTxErrLoopDetected_Type = Counter32
_MscVrIpNhrpNhsTxErrLoopDetected_Object = MibTableColumn
mscVrIpNhrpNhsTxErrLoopDetected = _MscVrIpNhrpNhsTxErrLoopDetected_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 26),
    _MscVrIpNhrpNhsTxErrLoopDetected_Type()
)
mscVrIpNhrpNhsTxErrLoopDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsTxErrLoopDetected.setStatus("mandatory")
_MscVrIpNhrpNhsTxErrProtoAddrUnreachable_Type = Counter32
_MscVrIpNhrpNhsTxErrProtoAddrUnreachable_Object = MibTableColumn
mscVrIpNhrpNhsTxErrProtoAddrUnreachable = _MscVrIpNhrpNhsTxErrProtoAddrUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 27),
    _MscVrIpNhrpNhsTxErrProtoAddrUnreachable_Type()
)
mscVrIpNhrpNhsTxErrProtoAddrUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsTxErrProtoAddrUnreachable.setStatus("mandatory")
_MscVrIpNhrpNhsTxErrProtoError_Type = Counter32
_MscVrIpNhrpNhsTxErrProtoError_Object = MibTableColumn
mscVrIpNhrpNhsTxErrProtoError = _MscVrIpNhrpNhsTxErrProtoError_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 28),
    _MscVrIpNhrpNhsTxErrProtoError_Type()
)
mscVrIpNhrpNhsTxErrProtoError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsTxErrProtoError.setStatus("mandatory")
_MscVrIpNhrpNhsTxErrSduSizeExceeded_Type = Counter32
_MscVrIpNhrpNhsTxErrSduSizeExceeded_Object = MibTableColumn
mscVrIpNhrpNhsTxErrSduSizeExceeded = _MscVrIpNhrpNhsTxErrSduSizeExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 29),
    _MscVrIpNhrpNhsTxErrSduSizeExceeded_Type()
)
mscVrIpNhrpNhsTxErrSduSizeExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsTxErrSduSizeExceeded.setStatus("mandatory")
_MscVrIpNhrpNhsTxErrInvalidExtension_Type = Counter32
_MscVrIpNhrpNhsTxErrInvalidExtension_Object = MibTableColumn
mscVrIpNhrpNhsTxErrInvalidExtension = _MscVrIpNhrpNhsTxErrInvalidExtension_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 30),
    _MscVrIpNhrpNhsTxErrInvalidExtension_Type()
)
mscVrIpNhrpNhsTxErrInvalidExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsTxErrInvalidExtension.setStatus("mandatory")
_MscVrIpNhrpNhsTxErrAuthenticationFailure_Type = Counter32
_MscVrIpNhrpNhsTxErrAuthenticationFailure_Object = MibTableColumn
mscVrIpNhrpNhsTxErrAuthenticationFailure = _MscVrIpNhrpNhsTxErrAuthenticationFailure_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 31),
    _MscVrIpNhrpNhsTxErrAuthenticationFailure_Type()
)
mscVrIpNhrpNhsTxErrAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsTxErrAuthenticationFailure.setStatus("mandatory")
_MscVrIpNhrpNhsTxErrHopCountExceeded_Type = Counter32
_MscVrIpNhrpNhsTxErrHopCountExceeded_Object = MibTableColumn
mscVrIpNhrpNhsTxErrHopCountExceeded = _MscVrIpNhrpNhsTxErrHopCountExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 32),
    _MscVrIpNhrpNhsTxErrHopCountExceeded_Type()
)
mscVrIpNhrpNhsTxErrHopCountExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsTxErrHopCountExceeded.setStatus("mandatory")
_MscVrIpNhrpNhsFwdResolveReq_Type = Counter32
_MscVrIpNhrpNhsFwdResolveReq_Object = MibTableColumn
mscVrIpNhrpNhsFwdResolveReq = _MscVrIpNhrpNhsFwdResolveReq_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 33),
    _MscVrIpNhrpNhsFwdResolveReq_Type()
)
mscVrIpNhrpNhsFwdResolveReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsFwdResolveReq.setStatus("mandatory")
_MscVrIpNhrpNhsFwdResolveReply_Type = Counter32
_MscVrIpNhrpNhsFwdResolveReply_Object = MibTableColumn
mscVrIpNhrpNhsFwdResolveReply = _MscVrIpNhrpNhsFwdResolveReply_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 34),
    _MscVrIpNhrpNhsFwdResolveReply_Type()
)
mscVrIpNhrpNhsFwdResolveReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsFwdResolveReply.setStatus("mandatory")
_MscVrIpNhrpNhsFwdRegisterReq_Type = Counter32
_MscVrIpNhrpNhsFwdRegisterReq_Object = MibTableColumn
mscVrIpNhrpNhsFwdRegisterReq = _MscVrIpNhrpNhsFwdRegisterReq_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 35),
    _MscVrIpNhrpNhsFwdRegisterReq_Type()
)
mscVrIpNhrpNhsFwdRegisterReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsFwdRegisterReq.setStatus("mandatory")
_MscVrIpNhrpNhsFwdRegisterReply_Type = Counter32
_MscVrIpNhrpNhsFwdRegisterReply_Object = MibTableColumn
mscVrIpNhrpNhsFwdRegisterReply = _MscVrIpNhrpNhsFwdRegisterReply_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 36),
    _MscVrIpNhrpNhsFwdRegisterReply_Type()
)
mscVrIpNhrpNhsFwdRegisterReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsFwdRegisterReply.setStatus("mandatory")
_MscVrIpNhrpNhsFwdPurgeReq_Type = Counter32
_MscVrIpNhrpNhsFwdPurgeReq_Object = MibTableColumn
mscVrIpNhrpNhsFwdPurgeReq = _MscVrIpNhrpNhsFwdPurgeReq_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 37),
    _MscVrIpNhrpNhsFwdPurgeReq_Type()
)
mscVrIpNhrpNhsFwdPurgeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsFwdPurgeReq.setStatus("mandatory")
_MscVrIpNhrpNhsFwdPurgeReply_Type = Counter32
_MscVrIpNhrpNhsFwdPurgeReply_Object = MibTableColumn
mscVrIpNhrpNhsFwdPurgeReply = _MscVrIpNhrpNhsFwdPurgeReply_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 38),
    _MscVrIpNhrpNhsFwdPurgeReply_Type()
)
mscVrIpNhrpNhsFwdPurgeReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsFwdPurgeReply.setStatus("mandatory")
_MscVrIpNhrpNhsFwdErrorIndication_Type = Counter32
_MscVrIpNhrpNhsFwdErrorIndication_Object = MibTableColumn
mscVrIpNhrpNhsFwdErrorIndication = _MscVrIpNhrpNhsFwdErrorIndication_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 2, 10, 1, 39),
    _MscVrIpNhrpNhsFwdErrorIndication_Type()
)
mscVrIpNhrpNhsFwdErrorIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhsFwdErrorIndication.setStatus("mandatory")
_MscVrIpNhrpNhc_ObjectIdentity = ObjectIdentity
mscVrIpNhrpNhc = _MscVrIpNhrpNhc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3)
)
_MscVrIpNhrpNhcRowStatusTable_Object = MibTable
mscVrIpNhrpNhcRowStatusTable = _MscVrIpNhrpNhcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 1)
)
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcRowStatusTable.setStatus("mandatory")
_MscVrIpNhrpNhcRowStatusEntry_Object = MibTableRow
mscVrIpNhrpNhcRowStatusEntry = _MscVrIpNhrpNhcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 1, 1)
)
mscVrIpNhrpNhcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpNhcIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcRowStatusEntry.setStatus("mandatory")
_MscVrIpNhrpNhcRowStatus_Type = RowStatus
_MscVrIpNhrpNhcRowStatus_Object = MibTableColumn
mscVrIpNhrpNhcRowStatus = _MscVrIpNhrpNhcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 1, 1, 1),
    _MscVrIpNhrpNhcRowStatus_Type()
)
mscVrIpNhrpNhcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcRowStatus.setStatus("mandatory")
_MscVrIpNhrpNhcComponentName_Type = DisplayString
_MscVrIpNhrpNhcComponentName_Object = MibTableColumn
mscVrIpNhrpNhcComponentName = _MscVrIpNhrpNhcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 1, 1, 2),
    _MscVrIpNhrpNhcComponentName_Type()
)
mscVrIpNhrpNhcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcComponentName.setStatus("mandatory")
_MscVrIpNhrpNhcStorageType_Type = StorageType
_MscVrIpNhrpNhcStorageType_Object = MibTableColumn
mscVrIpNhrpNhcStorageType = _MscVrIpNhrpNhcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 1, 1, 4),
    _MscVrIpNhrpNhcStorageType_Type()
)
mscVrIpNhrpNhcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcStorageType.setStatus("mandatory")
_MscVrIpNhrpNhcIndex_Type = NonReplicated
_MscVrIpNhrpNhcIndex_Object = MibTableColumn
mscVrIpNhrpNhcIndex = _MscVrIpNhrpNhcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 1, 1, 10),
    _MscVrIpNhrpNhcIndex_Type()
)
mscVrIpNhrpNhcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcIndex.setStatus("mandatory")
_MscVrIpNhrpNhcProvTable_Object = MibTable
mscVrIpNhrpNhcProvTable = _MscVrIpNhrpNhcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 10)
)
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcProvTable.setStatus("mandatory")
_MscVrIpNhrpNhcProvEntry_Object = MibTableRow
mscVrIpNhrpNhcProvEntry = _MscVrIpNhrpNhcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 10, 1)
)
mscVrIpNhrpNhcProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpNhcIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcProvEntry.setStatus("mandatory")


class _MscVrIpNhrpNhcFlowDetectPacketCount_Type(Unsigned32):
    """Custom type mscVrIpNhrpNhcFlowDetectPacketCount based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4292967295),
    )


_MscVrIpNhrpNhcFlowDetectPacketCount_Type.__name__ = "Unsigned32"
_MscVrIpNhrpNhcFlowDetectPacketCount_Object = MibTableColumn
mscVrIpNhrpNhcFlowDetectPacketCount = _MscVrIpNhrpNhcFlowDetectPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 10, 1, 1),
    _MscVrIpNhrpNhcFlowDetectPacketCount_Type()
)
mscVrIpNhrpNhcFlowDetectPacketCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcFlowDetectPacketCount.setStatus("mandatory")


class _MscVrIpNhrpNhcFlowDetectTimePeriod_Type(Integer32):
    """Custom type mscVrIpNhrpNhcFlowDetectTimePeriod based on Integer32"""
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


_MscVrIpNhrpNhcFlowDetectTimePeriod_Type.__name__ = "Integer32"
_MscVrIpNhrpNhcFlowDetectTimePeriod_Object = MibTableColumn
mscVrIpNhrpNhcFlowDetectTimePeriod = _MscVrIpNhrpNhcFlowDetectTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 10, 1, 2),
    _MscVrIpNhrpNhcFlowDetectTimePeriod_Type()
)
mscVrIpNhrpNhcFlowDetectTimePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcFlowDetectTimePeriod.setStatus("mandatory")


class _MscVrIpNhrpNhcIdleDetectPacketCount_Type(Unsigned32):
    """Custom type mscVrIpNhrpNhcIdleDetectPacketCount based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4292967295),
    )


_MscVrIpNhrpNhcIdleDetectPacketCount_Type.__name__ = "Unsigned32"
_MscVrIpNhrpNhcIdleDetectPacketCount_Object = MibTableColumn
mscVrIpNhrpNhcIdleDetectPacketCount = _MscVrIpNhrpNhcIdleDetectPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 10, 1, 3),
    _MscVrIpNhrpNhcIdleDetectPacketCount_Type()
)
mscVrIpNhrpNhcIdleDetectPacketCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcIdleDetectPacketCount.setStatus("mandatory")


class _MscVrIpNhrpNhcIdleDetectTimePeriod_Type(Unsigned32):
    """Custom type mscVrIpNhrpNhcIdleDetectTimePeriod based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_MscVrIpNhrpNhcIdleDetectTimePeriod_Type.__name__ = "Unsigned32"
_MscVrIpNhrpNhcIdleDetectTimePeriod_Object = MibTableColumn
mscVrIpNhrpNhcIdleDetectTimePeriod = _MscVrIpNhrpNhcIdleDetectTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 10, 1, 4),
    _MscVrIpNhrpNhcIdleDetectTimePeriod_Type()
)
mscVrIpNhrpNhcIdleDetectTimePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcIdleDetectTimePeriod.setStatus("mandatory")


class _MscVrIpNhrpNhcAtmFlowDetection_Type(Integer32):
    """Custom type mscVrIpNhrpNhcAtmFlowDetection based on Integer32"""
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


_MscVrIpNhrpNhcAtmFlowDetection_Type.__name__ = "Integer32"
_MscVrIpNhrpNhcAtmFlowDetection_Object = MibTableColumn
mscVrIpNhrpNhcAtmFlowDetection = _MscVrIpNhrpNhcAtmFlowDetection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 10, 1, 5),
    _MscVrIpNhrpNhcAtmFlowDetection_Type()
)
mscVrIpNhrpNhcAtmFlowDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcAtmFlowDetection.setStatus("mandatory")
_MscVrIpNhrpNhcStatsTable_Object = MibTable
mscVrIpNhrpNhcStatsTable = _MscVrIpNhrpNhcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 11)
)
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcStatsTable.setStatus("mandatory")
_MscVrIpNhrpNhcStatsEntry_Object = MibTableRow
mscVrIpNhrpNhcStatsEntry = _MscVrIpNhrpNhcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 11, 1)
)
mscVrIpNhrpNhcStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpNhcIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcStatsEntry.setStatus("mandatory")
_MscVrIpNhrpNhcTxResolveReq_Type = Counter32
_MscVrIpNhrpNhcTxResolveReq_Object = MibTableColumn
mscVrIpNhrpNhcTxResolveReq = _MscVrIpNhrpNhcTxResolveReq_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 11, 1, 1),
    _MscVrIpNhrpNhcTxResolveReq_Type()
)
mscVrIpNhrpNhcTxResolveReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcTxResolveReq.setStatus("mandatory")
_MscVrIpNhrpNhcRxResolveReplyAck_Type = Counter32
_MscVrIpNhrpNhcRxResolveReplyAck_Object = MibTableColumn
mscVrIpNhrpNhcRxResolveReplyAck = _MscVrIpNhrpNhcRxResolveReplyAck_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 11, 1, 2),
    _MscVrIpNhrpNhcRxResolveReplyAck_Type()
)
mscVrIpNhrpNhcRxResolveReplyAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcRxResolveReplyAck.setStatus("mandatory")
_MscVrIpNhrpNhcRxResolveReplyNakProhibited_Type = Counter32
_MscVrIpNhrpNhcRxResolveReplyNakProhibited_Object = MibTableColumn
mscVrIpNhrpNhcRxResolveReplyNakProhibited = _MscVrIpNhrpNhcRxResolveReplyNakProhibited_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 11, 1, 3),
    _MscVrIpNhrpNhcRxResolveReplyNakProhibited_Type()
)
mscVrIpNhrpNhcRxResolveReplyNakProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcRxResolveReplyNakProhibited.setStatus("mandatory")
_MscVrIpNhrpNhcRxResolveReplyNakInsufResources_Type = Counter32
_MscVrIpNhrpNhcRxResolveReplyNakInsufResources_Object = MibTableColumn
mscVrIpNhrpNhcRxResolveReplyNakInsufResources = _MscVrIpNhrpNhcRxResolveReplyNakInsufResources_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 11, 1, 4),
    _MscVrIpNhrpNhcRxResolveReplyNakInsufResources_Type()
)
mscVrIpNhrpNhcRxResolveReplyNakInsufResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcRxResolveReplyNakInsufResources.setStatus("mandatory")
_MscVrIpNhrpNhcRxResolveReplyNakNoBinding_Type = Counter32
_MscVrIpNhrpNhcRxResolveReplyNakNoBinding_Object = MibTableColumn
mscVrIpNhrpNhcRxResolveReplyNakNoBinding = _MscVrIpNhrpNhcRxResolveReplyNakNoBinding_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 11, 1, 5),
    _MscVrIpNhrpNhcRxResolveReplyNakNoBinding_Type()
)
mscVrIpNhrpNhcRxResolveReplyNakNoBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcRxResolveReplyNakNoBinding.setStatus("mandatory")
_MscVrIpNhrpNhcRxResolveReplyNakNotUnique_Type = Counter32
_MscVrIpNhrpNhcRxResolveReplyNakNotUnique_Object = MibTableColumn
mscVrIpNhrpNhcRxResolveReplyNakNotUnique = _MscVrIpNhrpNhcRxResolveReplyNakNotUnique_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 11, 1, 6),
    _MscVrIpNhrpNhcRxResolveReplyNakNotUnique_Type()
)
mscVrIpNhrpNhcRxResolveReplyNakNotUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcRxResolveReplyNakNotUnique.setStatus("mandatory")
_MscVrIpNhrpNhcRxPurgeReq_Type = Counter32
_MscVrIpNhrpNhcRxPurgeReq_Object = MibTableColumn
mscVrIpNhrpNhcRxPurgeReq = _MscVrIpNhrpNhcRxPurgeReq_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 11, 1, 12),
    _MscVrIpNhrpNhcRxPurgeReq_Type()
)
mscVrIpNhrpNhcRxPurgeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcRxPurgeReq.setStatus("mandatory")
_MscVrIpNhrpNhcTxPurgeReq_Type = Counter32
_MscVrIpNhrpNhcTxPurgeReq_Object = MibTableColumn
mscVrIpNhrpNhcTxPurgeReq = _MscVrIpNhrpNhcTxPurgeReq_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 11, 1, 13),
    _MscVrIpNhrpNhcTxPurgeReq_Type()
)
mscVrIpNhrpNhcTxPurgeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcTxPurgeReq.setStatus("mandatory")
_MscVrIpNhrpNhcRxPurgeReply_Type = Counter32
_MscVrIpNhrpNhcRxPurgeReply_Object = MibTableColumn
mscVrIpNhrpNhcRxPurgeReply = _MscVrIpNhrpNhcRxPurgeReply_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 11, 1, 14),
    _MscVrIpNhrpNhcRxPurgeReply_Type()
)
mscVrIpNhrpNhcRxPurgeReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcRxPurgeReply.setStatus("mandatory")
_MscVrIpNhrpNhcTxPurgeReply_Type = Counter32
_MscVrIpNhrpNhcTxPurgeReply_Object = MibTableColumn
mscVrIpNhrpNhcTxPurgeReply = _MscVrIpNhrpNhcTxPurgeReply_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 11, 1, 15),
    _MscVrIpNhrpNhcTxPurgeReply_Type()
)
mscVrIpNhrpNhcTxPurgeReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcTxPurgeReply.setStatus("mandatory")
_MscVrIpNhrpNhcTxErrIndication_Type = Counter32
_MscVrIpNhrpNhcTxErrIndication_Object = MibTableColumn
mscVrIpNhrpNhcTxErrIndication = _MscVrIpNhrpNhcTxErrIndication_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 11, 1, 16),
    _MscVrIpNhrpNhcTxErrIndication_Type()
)
mscVrIpNhrpNhcTxErrIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcTxErrIndication.setStatus("mandatory")
_MscVrIpNhrpNhcRxErrUnrecognizedExtension_Type = Counter32
_MscVrIpNhrpNhcRxErrUnrecognizedExtension_Object = MibTableColumn
mscVrIpNhrpNhcRxErrUnrecognizedExtension = _MscVrIpNhrpNhcRxErrUnrecognizedExtension_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 11, 1, 17),
    _MscVrIpNhrpNhcRxErrUnrecognizedExtension_Type()
)
mscVrIpNhrpNhcRxErrUnrecognizedExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcRxErrUnrecognizedExtension.setStatus("mandatory")
_MscVrIpNhrpNhcRxErrLoopDetected_Type = Counter32
_MscVrIpNhrpNhcRxErrLoopDetected_Object = MibTableColumn
mscVrIpNhrpNhcRxErrLoopDetected = _MscVrIpNhrpNhcRxErrLoopDetected_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 11, 1, 18),
    _MscVrIpNhrpNhcRxErrLoopDetected_Type()
)
mscVrIpNhrpNhcRxErrLoopDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcRxErrLoopDetected.setStatus("mandatory")
_MscVrIpNhrpNhcRxErrProtoAddrUnreachable_Type = Counter32
_MscVrIpNhrpNhcRxErrProtoAddrUnreachable_Object = MibTableColumn
mscVrIpNhrpNhcRxErrProtoAddrUnreachable = _MscVrIpNhrpNhcRxErrProtoAddrUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 11, 1, 19),
    _MscVrIpNhrpNhcRxErrProtoAddrUnreachable_Type()
)
mscVrIpNhrpNhcRxErrProtoAddrUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcRxErrProtoAddrUnreachable.setStatus("mandatory")
_MscVrIpNhrpNhcRxErrProtoError_Type = Counter32
_MscVrIpNhrpNhcRxErrProtoError_Object = MibTableColumn
mscVrIpNhrpNhcRxErrProtoError = _MscVrIpNhrpNhcRxErrProtoError_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 11, 1, 20),
    _MscVrIpNhrpNhcRxErrProtoError_Type()
)
mscVrIpNhrpNhcRxErrProtoError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcRxErrProtoError.setStatus("mandatory")
_MscVrIpNhrpNhcRxErrSduSizeExceeded_Type = Counter32
_MscVrIpNhrpNhcRxErrSduSizeExceeded_Object = MibTableColumn
mscVrIpNhrpNhcRxErrSduSizeExceeded = _MscVrIpNhrpNhcRxErrSduSizeExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 11, 1, 21),
    _MscVrIpNhrpNhcRxErrSduSizeExceeded_Type()
)
mscVrIpNhrpNhcRxErrSduSizeExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcRxErrSduSizeExceeded.setStatus("mandatory")
_MscVrIpNhrpNhcRxErrInvalidExtension_Type = Counter32
_MscVrIpNhrpNhcRxErrInvalidExtension_Object = MibTableColumn
mscVrIpNhrpNhcRxErrInvalidExtension = _MscVrIpNhrpNhcRxErrInvalidExtension_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 11, 1, 22),
    _MscVrIpNhrpNhcRxErrInvalidExtension_Type()
)
mscVrIpNhrpNhcRxErrInvalidExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcRxErrInvalidExtension.setStatus("mandatory")
_MscVrIpNhrpNhcRxErrAuthenticationFailure_Type = Counter32
_MscVrIpNhrpNhcRxErrAuthenticationFailure_Object = MibTableColumn
mscVrIpNhrpNhcRxErrAuthenticationFailure = _MscVrIpNhrpNhcRxErrAuthenticationFailure_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 11, 1, 23),
    _MscVrIpNhrpNhcRxErrAuthenticationFailure_Type()
)
mscVrIpNhrpNhcRxErrAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcRxErrAuthenticationFailure.setStatus("mandatory")
_MscVrIpNhrpNhcRxErrHopCountExceeded_Type = Counter32
_MscVrIpNhrpNhcRxErrHopCountExceeded_Object = MibTableColumn
mscVrIpNhrpNhcRxErrHopCountExceeded = _MscVrIpNhrpNhcRxErrHopCountExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 3, 11, 1, 24),
    _MscVrIpNhrpNhcRxErrHopCountExceeded_Type()
)
mscVrIpNhrpNhcRxErrHopCountExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpNhcRxErrHopCountExceeded.setStatus("mandatory")
_MscVrIpNhrpRce_ObjectIdentity = ObjectIdentity
mscVrIpNhrpRce = _MscVrIpNhrpRce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 4)
)
_MscVrIpNhrpRceRowStatusTable_Object = MibTable
mscVrIpNhrpRceRowStatusTable = _MscVrIpNhrpRceRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 4, 1)
)
if mibBuilder.loadTexts:
    mscVrIpNhrpRceRowStatusTable.setStatus("mandatory")
_MscVrIpNhrpRceRowStatusEntry_Object = MibTableRow
mscVrIpNhrpRceRowStatusEntry = _MscVrIpNhrpRceRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 4, 1, 1)
)
mscVrIpNhrpRceRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpRceDestAddrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpRceDestMaskIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpNhrpRceRowStatusEntry.setStatus("mandatory")
_MscVrIpNhrpRceRowStatus_Type = RowStatus
_MscVrIpNhrpRceRowStatus_Object = MibTableColumn
mscVrIpNhrpRceRowStatus = _MscVrIpNhrpRceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 4, 1, 1, 1),
    _MscVrIpNhrpRceRowStatus_Type()
)
mscVrIpNhrpRceRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpRceRowStatus.setStatus("mandatory")
_MscVrIpNhrpRceComponentName_Type = DisplayString
_MscVrIpNhrpRceComponentName_Object = MibTableColumn
mscVrIpNhrpRceComponentName = _MscVrIpNhrpRceComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 4, 1, 1, 2),
    _MscVrIpNhrpRceComponentName_Type()
)
mscVrIpNhrpRceComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpRceComponentName.setStatus("mandatory")
_MscVrIpNhrpRceStorageType_Type = StorageType
_MscVrIpNhrpRceStorageType_Object = MibTableColumn
mscVrIpNhrpRceStorageType = _MscVrIpNhrpRceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 4, 1, 1, 4),
    _MscVrIpNhrpRceStorageType_Type()
)
mscVrIpNhrpRceStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpRceStorageType.setStatus("mandatory")
_MscVrIpNhrpRceDestAddrIndex_Type = IpAddress
_MscVrIpNhrpRceDestAddrIndex_Object = MibTableColumn
mscVrIpNhrpRceDestAddrIndex = _MscVrIpNhrpRceDestAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 4, 1, 1, 10),
    _MscVrIpNhrpRceDestAddrIndex_Type()
)
mscVrIpNhrpRceDestAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpNhrpRceDestAddrIndex.setStatus("mandatory")
_MscVrIpNhrpRceDestMaskIndex_Type = IpAddress
_MscVrIpNhrpRceDestMaskIndex_Object = MibTableColumn
mscVrIpNhrpRceDestMaskIndex = _MscVrIpNhrpRceDestMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 4, 1, 1, 11),
    _MscVrIpNhrpRceDestMaskIndex_Type()
)
mscVrIpNhrpRceDestMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpNhrpRceDestMaskIndex.setStatus("mandatory")
_MscVrIpNhrpRceOperTable_Object = MibTable
mscVrIpNhrpRceOperTable = _MscVrIpNhrpRceOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 4, 10)
)
if mibBuilder.loadTexts:
    mscVrIpNhrpRceOperTable.setStatus("mandatory")
_MscVrIpNhrpRceOperEntry_Object = MibTableRow
mscVrIpNhrpRceOperEntry = _MscVrIpNhrpRceOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 4, 10, 1)
)
mscVrIpNhrpRceOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpRceDestAddrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpRceDestMaskIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpNhrpRceOperEntry.setStatus("mandatory")


class _MscVrIpNhrpRceNbmaAddress_Type(HexString):
    """Custom type mscVrIpNhrpRceNbmaAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MscVrIpNhrpRceNbmaAddress_Type.__name__ = "HexString"
_MscVrIpNhrpRceNbmaAddress_Object = MibTableColumn
mscVrIpNhrpRceNbmaAddress = _MscVrIpNhrpRceNbmaAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 4, 10, 1, 3),
    _MscVrIpNhrpRceNbmaAddress_Type()
)
mscVrIpNhrpRceNbmaAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpRceNbmaAddress.setStatus("mandatory")


class _MscVrIpNhrpRceEntryState_Type(Integer32):
    """Custom type mscVrIpNhrpRceEntryState based on Integer32"""
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


_MscVrIpNhrpRceEntryState_Type.__name__ = "Integer32"
_MscVrIpNhrpRceEntryState_Object = MibTableColumn
mscVrIpNhrpRceEntryState = _MscVrIpNhrpRceEntryState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 4, 10, 1, 6),
    _MscVrIpNhrpRceEntryState_Type()
)
mscVrIpNhrpRceEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpRceEntryState.setStatus("mandatory")


class _MscVrIpNhrpRceHoldingTime_Type(Unsigned32):
    """Custom type mscVrIpNhrpRceHoldingTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpNhrpRceHoldingTime_Type.__name__ = "Unsigned32"
_MscVrIpNhrpRceHoldingTime_Object = MibTableColumn
mscVrIpNhrpRceHoldingTime = _MscVrIpNhrpRceHoldingTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 4, 10, 1, 7),
    _MscVrIpNhrpRceHoldingTime_Type()
)
mscVrIpNhrpRceHoldingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpRceHoldingTime.setStatus("mandatory")
_MscVrIpNhrpRceShortcut_Type = RowPointer
_MscVrIpNhrpRceShortcut_Object = MibTableColumn
mscVrIpNhrpRceShortcut = _MscVrIpNhrpRceShortcut_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 4, 10, 1, 8),
    _MscVrIpNhrpRceShortcut_Type()
)
mscVrIpNhrpRceShortcut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpRceShortcut.setStatus("mandatory")
_MscVrIpNhrpAdminControlTable_Object = MibTable
mscVrIpNhrpAdminControlTable = _MscVrIpNhrpAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 10)
)
if mibBuilder.loadTexts:
    mscVrIpNhrpAdminControlTable.setStatus("mandatory")
_MscVrIpNhrpAdminControlEntry_Object = MibTableRow
mscVrIpNhrpAdminControlEntry = _MscVrIpNhrpAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 10, 1)
)
mscVrIpNhrpAdminControlEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpNhrpAdminControlEntry.setStatus("mandatory")


class _MscVrIpNhrpSnmpAdminStatus_Type(Integer32):
    """Custom type mscVrIpNhrpSnmpAdminStatus based on Integer32"""
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


_MscVrIpNhrpSnmpAdminStatus_Type.__name__ = "Integer32"
_MscVrIpNhrpSnmpAdminStatus_Object = MibTableColumn
mscVrIpNhrpSnmpAdminStatus = _MscVrIpNhrpSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 10, 1, 1),
    _MscVrIpNhrpSnmpAdminStatus_Type()
)
mscVrIpNhrpSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNhrpSnmpAdminStatus.setStatus("mandatory")
_MscVrIpNhrpProvTable_Object = MibTable
mscVrIpNhrpProvTable = _MscVrIpNhrpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 11)
)
if mibBuilder.loadTexts:
    mscVrIpNhrpProvTable.setStatus("mandatory")
_MscVrIpNhrpProvEntry_Object = MibTableRow
mscVrIpNhrpProvEntry = _MscVrIpNhrpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 11, 1)
)
mscVrIpNhrpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpNhrpProvEntry.setStatus("mandatory")


class _MscVrIpNhrpMaxResCacheEntries_Type(Unsigned32):
    """Custom type mscVrIpNhrpMaxResCacheEntries based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 1024),
    )


_MscVrIpNhrpMaxResCacheEntries_Type.__name__ = "Unsigned32"
_MscVrIpNhrpMaxResCacheEntries_Object = MibTableColumn
mscVrIpNhrpMaxResCacheEntries = _MscVrIpNhrpMaxResCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 11, 1, 1),
    _MscVrIpNhrpMaxResCacheEntries_Type()
)
mscVrIpNhrpMaxResCacheEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNhrpMaxResCacheEntries.setStatus("mandatory")


class _MscVrIpNhrpFwdTransitRecord_Type(Integer32):
    """Custom type mscVrIpNhrpFwdTransitRecord based on Integer32"""
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


_MscVrIpNhrpFwdTransitRecord_Type.__name__ = "Integer32"
_MscVrIpNhrpFwdTransitRecord_Object = MibTableColumn
mscVrIpNhrpFwdTransitRecord = _MscVrIpNhrpFwdTransitRecord_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 11, 1, 2),
    _MscVrIpNhrpFwdTransitRecord_Type()
)
mscVrIpNhrpFwdTransitRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNhrpFwdTransitRecord.setStatus("mandatory")


class _MscVrIpNhrpRevTransitRecord_Type(Integer32):
    """Custom type mscVrIpNhrpRevTransitRecord based on Integer32"""
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


_MscVrIpNhrpRevTransitRecord_Type.__name__ = "Integer32"
_MscVrIpNhrpRevTransitRecord_Object = MibTableColumn
mscVrIpNhrpRevTransitRecord = _MscVrIpNhrpRevTransitRecord_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 11, 1, 3),
    _MscVrIpNhrpRevTransitRecord_Type()
)
mscVrIpNhrpRevTransitRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpNhrpRevTransitRecord.setStatus("mandatory")
_MscVrIpNhrpStateTable_Object = MibTable
mscVrIpNhrpStateTable = _MscVrIpNhrpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 13)
)
if mibBuilder.loadTexts:
    mscVrIpNhrpStateTable.setStatus("mandatory")
_MscVrIpNhrpStateEntry_Object = MibTableRow
mscVrIpNhrpStateEntry = _MscVrIpNhrpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 13, 1)
)
mscVrIpNhrpStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpNhrpStateEntry.setStatus("mandatory")


class _MscVrIpNhrpAdminState_Type(Integer32):
    """Custom type mscVrIpNhrpAdminState based on Integer32"""
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


_MscVrIpNhrpAdminState_Type.__name__ = "Integer32"
_MscVrIpNhrpAdminState_Object = MibTableColumn
mscVrIpNhrpAdminState = _MscVrIpNhrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 13, 1, 1),
    _MscVrIpNhrpAdminState_Type()
)
mscVrIpNhrpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpAdminState.setStatus("mandatory")


class _MscVrIpNhrpOperationalState_Type(Integer32):
    """Custom type mscVrIpNhrpOperationalState based on Integer32"""
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


_MscVrIpNhrpOperationalState_Type.__name__ = "Integer32"
_MscVrIpNhrpOperationalState_Object = MibTableColumn
mscVrIpNhrpOperationalState = _MscVrIpNhrpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 13, 1, 2),
    _MscVrIpNhrpOperationalState_Type()
)
mscVrIpNhrpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpOperationalState.setStatus("mandatory")


class _MscVrIpNhrpUsageState_Type(Integer32):
    """Custom type mscVrIpNhrpUsageState based on Integer32"""
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


_MscVrIpNhrpUsageState_Type.__name__ = "Integer32"
_MscVrIpNhrpUsageState_Object = MibTableColumn
mscVrIpNhrpUsageState = _MscVrIpNhrpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 13, 1, 3),
    _MscVrIpNhrpUsageState_Type()
)
mscVrIpNhrpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpUsageState.setStatus("mandatory")
_MscVrIpNhrpOperStatusTable_Object = MibTable
mscVrIpNhrpOperStatusTable = _MscVrIpNhrpOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 14)
)
if mibBuilder.loadTexts:
    mscVrIpNhrpOperStatusTable.setStatus("mandatory")
_MscVrIpNhrpOperStatusEntry_Object = MibTableRow
mscVrIpNhrpOperStatusEntry = _MscVrIpNhrpOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 14, 1)
)
mscVrIpNhrpOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpNhrpOperStatusEntry.setStatus("mandatory")


class _MscVrIpNhrpSnmpOperStatus_Type(Integer32):
    """Custom type mscVrIpNhrpSnmpOperStatus based on Integer32"""
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


_MscVrIpNhrpSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrIpNhrpSnmpOperStatus_Object = MibTableColumn
mscVrIpNhrpSnmpOperStatus = _MscVrIpNhrpSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 14, 1, 1),
    _MscVrIpNhrpSnmpOperStatus_Type()
)
mscVrIpNhrpSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpSnmpOperStatus.setStatus("mandatory")
_MscVrIpNhrpOperTable_Object = MibTable
mscVrIpNhrpOperTable = _MscVrIpNhrpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 15)
)
if mibBuilder.loadTexts:
    mscVrIpNhrpOperTable.setStatus("mandatory")
_MscVrIpNhrpOperEntry_Object = MibTableRow
mscVrIpNhrpOperEntry = _MscVrIpNhrpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 15, 1)
)
mscVrIpNhrpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpNhrpMIB", "mscVrIpNhrpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpNhrpOperEntry.setStatus("mandatory")


class _MscVrIpNhrpCurrResCacheEntries_Type(Unsigned32):
    """Custom type mscVrIpNhrpCurrResCacheEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4292967295),
    )


_MscVrIpNhrpCurrResCacheEntries_Type.__name__ = "Unsigned32"
_MscVrIpNhrpCurrResCacheEntries_Object = MibTableColumn
mscVrIpNhrpCurrResCacheEntries = _MscVrIpNhrpCurrResCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 15, 1, 1),
    _MscVrIpNhrpCurrResCacheEntries_Type()
)
mscVrIpNhrpCurrResCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpCurrResCacheEntries.setStatus("mandatory")


class _MscVrIpNhrpPeakResCacheEntries_Type(Unsigned32):
    """Custom type mscVrIpNhrpPeakResCacheEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4292967295),
    )


_MscVrIpNhrpPeakResCacheEntries_Type.__name__ = "Unsigned32"
_MscVrIpNhrpPeakResCacheEntries_Object = MibTableColumn
mscVrIpNhrpPeakResCacheEntries = _MscVrIpNhrpPeakResCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 19, 15, 1, 2),
    _MscVrIpNhrpPeakResCacheEntries_Type()
)
mscVrIpNhrpPeakResCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpNhrpPeakResCacheEntries.setStatus("mandatory")
_IpNhrpMIB_ObjectIdentity = ObjectIdentity
ipNhrpMIB = _IpNhrpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 77)
)
_IpNhrpGroup_ObjectIdentity = ObjectIdentity
ipNhrpGroup = _IpNhrpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 77, 1)
)
_IpNhrpGroupCA_ObjectIdentity = ObjectIdentity
ipNhrpGroupCA = _IpNhrpGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 77, 1, 1)
)
_IpNhrpGroupCA02_ObjectIdentity = ObjectIdentity
ipNhrpGroupCA02 = _IpNhrpGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 77, 1, 1, 3)
)
_IpNhrpGroupCA02A_ObjectIdentity = ObjectIdentity
ipNhrpGroupCA02A = _IpNhrpGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 77, 1, 1, 3, 2)
)
_IpNhrpCapabilities_ObjectIdentity = ObjectIdentity
ipNhrpCapabilities = _IpNhrpCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 77, 3)
)
_IpNhrpCapabilitiesCA_ObjectIdentity = ObjectIdentity
ipNhrpCapabilitiesCA = _IpNhrpCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 77, 3, 1)
)
_IpNhrpCapabilitiesCA02_ObjectIdentity = ObjectIdentity
ipNhrpCapabilitiesCA02 = _IpNhrpCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 77, 3, 1, 3)
)
_IpNhrpCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
ipNhrpCapabilitiesCA02A = _IpNhrpCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 77, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-IpNhrpMIB",
    **{"mscVrPpIpPortLogicalIfNhrpIf": mscVrPpIpPortLogicalIfNhrpIf,
       "mscVrPpIpPortLogicalIfNhrpIfRowStatusTable": mscVrPpIpPortLogicalIfNhrpIfRowStatusTable,
       "mscVrPpIpPortLogicalIfNhrpIfRowStatusEntry": mscVrPpIpPortLogicalIfNhrpIfRowStatusEntry,
       "mscVrPpIpPortLogicalIfNhrpIfRowStatus": mscVrPpIpPortLogicalIfNhrpIfRowStatus,
       "mscVrPpIpPortLogicalIfNhrpIfComponentName": mscVrPpIpPortLogicalIfNhrpIfComponentName,
       "mscVrPpIpPortLogicalIfNhrpIfStorageType": mscVrPpIpPortLogicalIfNhrpIfStorageType,
       "mscVrPpIpPortLogicalIfNhrpIfIndex": mscVrPpIpPortLogicalIfNhrpIfIndex,
       "mscVrIpNhrp": mscVrIpNhrp,
       "mscVrIpNhrpRowStatusTable": mscVrIpNhrpRowStatusTable,
       "mscVrIpNhrpRowStatusEntry": mscVrIpNhrpRowStatusEntry,
       "mscVrIpNhrpRowStatus": mscVrIpNhrpRowStatus,
       "mscVrIpNhrpComponentName": mscVrIpNhrpComponentName,
       "mscVrIpNhrpStorageType": mscVrIpNhrpStorageType,
       "mscVrIpNhrpIndex": mscVrIpNhrpIndex,
       "mscVrIpNhrpNhs": mscVrIpNhrpNhs,
       "mscVrIpNhrpNhsRowStatusTable": mscVrIpNhrpNhsRowStatusTable,
       "mscVrIpNhrpNhsRowStatusEntry": mscVrIpNhrpNhsRowStatusEntry,
       "mscVrIpNhrpNhsRowStatus": mscVrIpNhrpNhsRowStatus,
       "mscVrIpNhrpNhsComponentName": mscVrIpNhrpNhsComponentName,
       "mscVrIpNhrpNhsStorageType": mscVrIpNhrpNhsStorageType,
       "mscVrIpNhrpNhsIndex": mscVrIpNhrpNhsIndex,
       "mscVrIpNhrpNhsEp": mscVrIpNhrpNhsEp,
       "mscVrIpNhrpNhsEpRowStatusTable": mscVrIpNhrpNhsEpRowStatusTable,
       "mscVrIpNhrpNhsEpRowStatusEntry": mscVrIpNhrpNhsEpRowStatusEntry,
       "mscVrIpNhrpNhsEpRowStatus": mscVrIpNhrpNhsEpRowStatus,
       "mscVrIpNhrpNhsEpComponentName": mscVrIpNhrpNhsEpComponentName,
       "mscVrIpNhrpNhsEpStorageType": mscVrIpNhrpNhsEpStorageType,
       "mscVrIpNhrpNhsEpIndex": mscVrIpNhrpNhsEpIndex,
       "mscVrIpNhrpNhsEpNetAddr": mscVrIpNhrpNhsEpNetAddr,
       "mscVrIpNhrpNhsEpNetAddrRowStatusTable": mscVrIpNhrpNhsEpNetAddrRowStatusTable,
       "mscVrIpNhrpNhsEpNetAddrRowStatusEntry": mscVrIpNhrpNhsEpNetAddrRowStatusEntry,
       "mscVrIpNhrpNhsEpNetAddrRowStatus": mscVrIpNhrpNhsEpNetAddrRowStatus,
       "mscVrIpNhrpNhsEpNetAddrComponentName": mscVrIpNhrpNhsEpNetAddrComponentName,
       "mscVrIpNhrpNhsEpNetAddrStorageType": mscVrIpNhrpNhsEpNetAddrStorageType,
       "mscVrIpNhrpNhsEpNetAddrIndex": mscVrIpNhrpNhsEpNetAddrIndex,
       "mscVrIpNhrpNhsEpNetAddrProvTable": mscVrIpNhrpNhsEpNetAddrProvTable,
       "mscVrIpNhrpNhsEpNetAddrProvEntry": mscVrIpNhrpNhsEpNetAddrProvEntry,
       "mscVrIpNhrpNhsEpNetAddrSourceAddress": mscVrIpNhrpNhsEpNetAddrSourceAddress,
       "mscVrIpNhrpNhsEpNetAddrSourceMask": mscVrIpNhrpNhsEpNetAddrSourceMask,
       "mscVrIpNhrpNhsEpNetAddrDestinationAddress": mscVrIpNhrpNhsEpNetAddrDestinationAddress,
       "mscVrIpNhrpNhsEpNetAddrDestinationMask": mscVrIpNhrpNhsEpNetAddrDestinationMask,
       "mscVrIpNhrpNhsEpProvTable": mscVrIpNhrpNhsEpProvTable,
       "mscVrIpNhrpNhsEpProvEntry": mscVrIpNhrpNhsEpProvEntry,
       "mscVrIpNhrpNhsEpAction": mscVrIpNhrpNhsEpAction,
       "mscVrIpNhrpNhsEpProtocol": mscVrIpNhrpNhsEpProtocol,
       "mscVrIpNhrpNhsStatsTable": mscVrIpNhrpNhsStatsTable,
       "mscVrIpNhrpNhsStatsEntry": mscVrIpNhrpNhsStatsEntry,
       "mscVrIpNhrpNhsRxResolveReq": mscVrIpNhrpNhsRxResolveReq,
       "mscVrIpNhrpNhsTxResolveReplyAck": mscVrIpNhrpNhsTxResolveReplyAck,
       "mscVrIpNhrpNhsTxResolveReplyNakProhibited": mscVrIpNhrpNhsTxResolveReplyNakProhibited,
       "mscVrIpNhrpNhsTxResolveReplyNakInsufResources": mscVrIpNhrpNhsTxResolveReplyNakInsufResources,
       "mscVrIpNhrpNhsTxResolveReplyNakNoBinding": mscVrIpNhrpNhsTxResolveReplyNakNoBinding,
       "mscVrIpNhrpNhsTxResolveReplyNakNotUnique": mscVrIpNhrpNhsTxResolveReplyNakNotUnique,
       "mscVrIpNhrpNhsRxRegisterReq": mscVrIpNhrpNhsRxRegisterReq,
       "mscVrIpNhrpNhsRxPurgeReq": mscVrIpNhrpNhsRxPurgeReq,
       "mscVrIpNhrpNhsTxPurgeReq": mscVrIpNhrpNhsTxPurgeReq,
       "mscVrIpNhrpNhsRxPurgeReply": mscVrIpNhrpNhsRxPurgeReply,
       "mscVrIpNhrpNhsTxPurgeReply": mscVrIpNhrpNhsTxPurgeReply,
       "mscVrIpNhrpNhsRxErrUnrecognizedExtension": mscVrIpNhrpNhsRxErrUnrecognizedExtension,
       "mscVrIpNhrpNhsRxErrLoopDetected": mscVrIpNhrpNhsRxErrLoopDetected,
       "mscVrIpNhrpNhsRxErrProtoAddrUnreachable": mscVrIpNhrpNhsRxErrProtoAddrUnreachable,
       "mscVrIpNhrpNhsRxErrProtoError": mscVrIpNhrpNhsRxErrProtoError,
       "mscVrIpNhrpNhsRxErrSduSizeExceeded": mscVrIpNhrpNhsRxErrSduSizeExceeded,
       "mscVrIpNhrpNhsRxErrInvalidExtension": mscVrIpNhrpNhsRxErrInvalidExtension,
       "mscVrIpNhrpNhsRxErrInvalidResReplyReceived": mscVrIpNhrpNhsRxErrInvalidResReplyReceived,
       "mscVrIpNhrpNhsRxErrAuthenticationFailure": mscVrIpNhrpNhsRxErrAuthenticationFailure,
       "mscVrIpNhrpNhsRxErrHopCountExceeded": mscVrIpNhrpNhsRxErrHopCountExceeded,
       "mscVrIpNhrpNhsTxErrUnrecognizedExtension": mscVrIpNhrpNhsTxErrUnrecognizedExtension,
       "mscVrIpNhrpNhsTxErrLoopDetected": mscVrIpNhrpNhsTxErrLoopDetected,
       "mscVrIpNhrpNhsTxErrProtoAddrUnreachable": mscVrIpNhrpNhsTxErrProtoAddrUnreachable,
       "mscVrIpNhrpNhsTxErrProtoError": mscVrIpNhrpNhsTxErrProtoError,
       "mscVrIpNhrpNhsTxErrSduSizeExceeded": mscVrIpNhrpNhsTxErrSduSizeExceeded,
       "mscVrIpNhrpNhsTxErrInvalidExtension": mscVrIpNhrpNhsTxErrInvalidExtension,
       "mscVrIpNhrpNhsTxErrAuthenticationFailure": mscVrIpNhrpNhsTxErrAuthenticationFailure,
       "mscVrIpNhrpNhsTxErrHopCountExceeded": mscVrIpNhrpNhsTxErrHopCountExceeded,
       "mscVrIpNhrpNhsFwdResolveReq": mscVrIpNhrpNhsFwdResolveReq,
       "mscVrIpNhrpNhsFwdResolveReply": mscVrIpNhrpNhsFwdResolveReply,
       "mscVrIpNhrpNhsFwdRegisterReq": mscVrIpNhrpNhsFwdRegisterReq,
       "mscVrIpNhrpNhsFwdRegisterReply": mscVrIpNhrpNhsFwdRegisterReply,
       "mscVrIpNhrpNhsFwdPurgeReq": mscVrIpNhrpNhsFwdPurgeReq,
       "mscVrIpNhrpNhsFwdPurgeReply": mscVrIpNhrpNhsFwdPurgeReply,
       "mscVrIpNhrpNhsFwdErrorIndication": mscVrIpNhrpNhsFwdErrorIndication,
       "mscVrIpNhrpNhc": mscVrIpNhrpNhc,
       "mscVrIpNhrpNhcRowStatusTable": mscVrIpNhrpNhcRowStatusTable,
       "mscVrIpNhrpNhcRowStatusEntry": mscVrIpNhrpNhcRowStatusEntry,
       "mscVrIpNhrpNhcRowStatus": mscVrIpNhrpNhcRowStatus,
       "mscVrIpNhrpNhcComponentName": mscVrIpNhrpNhcComponentName,
       "mscVrIpNhrpNhcStorageType": mscVrIpNhrpNhcStorageType,
       "mscVrIpNhrpNhcIndex": mscVrIpNhrpNhcIndex,
       "mscVrIpNhrpNhcProvTable": mscVrIpNhrpNhcProvTable,
       "mscVrIpNhrpNhcProvEntry": mscVrIpNhrpNhcProvEntry,
       "mscVrIpNhrpNhcFlowDetectPacketCount": mscVrIpNhrpNhcFlowDetectPacketCount,
       "mscVrIpNhrpNhcFlowDetectTimePeriod": mscVrIpNhrpNhcFlowDetectTimePeriod,
       "mscVrIpNhrpNhcIdleDetectPacketCount": mscVrIpNhrpNhcIdleDetectPacketCount,
       "mscVrIpNhrpNhcIdleDetectTimePeriod": mscVrIpNhrpNhcIdleDetectTimePeriod,
       "mscVrIpNhrpNhcAtmFlowDetection": mscVrIpNhrpNhcAtmFlowDetection,
       "mscVrIpNhrpNhcStatsTable": mscVrIpNhrpNhcStatsTable,
       "mscVrIpNhrpNhcStatsEntry": mscVrIpNhrpNhcStatsEntry,
       "mscVrIpNhrpNhcTxResolveReq": mscVrIpNhrpNhcTxResolveReq,
       "mscVrIpNhrpNhcRxResolveReplyAck": mscVrIpNhrpNhcRxResolveReplyAck,
       "mscVrIpNhrpNhcRxResolveReplyNakProhibited": mscVrIpNhrpNhcRxResolveReplyNakProhibited,
       "mscVrIpNhrpNhcRxResolveReplyNakInsufResources": mscVrIpNhrpNhcRxResolveReplyNakInsufResources,
       "mscVrIpNhrpNhcRxResolveReplyNakNoBinding": mscVrIpNhrpNhcRxResolveReplyNakNoBinding,
       "mscVrIpNhrpNhcRxResolveReplyNakNotUnique": mscVrIpNhrpNhcRxResolveReplyNakNotUnique,
       "mscVrIpNhrpNhcRxPurgeReq": mscVrIpNhrpNhcRxPurgeReq,
       "mscVrIpNhrpNhcTxPurgeReq": mscVrIpNhrpNhcTxPurgeReq,
       "mscVrIpNhrpNhcRxPurgeReply": mscVrIpNhrpNhcRxPurgeReply,
       "mscVrIpNhrpNhcTxPurgeReply": mscVrIpNhrpNhcTxPurgeReply,
       "mscVrIpNhrpNhcTxErrIndication": mscVrIpNhrpNhcTxErrIndication,
       "mscVrIpNhrpNhcRxErrUnrecognizedExtension": mscVrIpNhrpNhcRxErrUnrecognizedExtension,
       "mscVrIpNhrpNhcRxErrLoopDetected": mscVrIpNhrpNhcRxErrLoopDetected,
       "mscVrIpNhrpNhcRxErrProtoAddrUnreachable": mscVrIpNhrpNhcRxErrProtoAddrUnreachable,
       "mscVrIpNhrpNhcRxErrProtoError": mscVrIpNhrpNhcRxErrProtoError,
       "mscVrIpNhrpNhcRxErrSduSizeExceeded": mscVrIpNhrpNhcRxErrSduSizeExceeded,
       "mscVrIpNhrpNhcRxErrInvalidExtension": mscVrIpNhrpNhcRxErrInvalidExtension,
       "mscVrIpNhrpNhcRxErrAuthenticationFailure": mscVrIpNhrpNhcRxErrAuthenticationFailure,
       "mscVrIpNhrpNhcRxErrHopCountExceeded": mscVrIpNhrpNhcRxErrHopCountExceeded,
       "mscVrIpNhrpRce": mscVrIpNhrpRce,
       "mscVrIpNhrpRceRowStatusTable": mscVrIpNhrpRceRowStatusTable,
       "mscVrIpNhrpRceRowStatusEntry": mscVrIpNhrpRceRowStatusEntry,
       "mscVrIpNhrpRceRowStatus": mscVrIpNhrpRceRowStatus,
       "mscVrIpNhrpRceComponentName": mscVrIpNhrpRceComponentName,
       "mscVrIpNhrpRceStorageType": mscVrIpNhrpRceStorageType,
       "mscVrIpNhrpRceDestAddrIndex": mscVrIpNhrpRceDestAddrIndex,
       "mscVrIpNhrpRceDestMaskIndex": mscVrIpNhrpRceDestMaskIndex,
       "mscVrIpNhrpRceOperTable": mscVrIpNhrpRceOperTable,
       "mscVrIpNhrpRceOperEntry": mscVrIpNhrpRceOperEntry,
       "mscVrIpNhrpRceNbmaAddress": mscVrIpNhrpRceNbmaAddress,
       "mscVrIpNhrpRceEntryState": mscVrIpNhrpRceEntryState,
       "mscVrIpNhrpRceHoldingTime": mscVrIpNhrpRceHoldingTime,
       "mscVrIpNhrpRceShortcut": mscVrIpNhrpRceShortcut,
       "mscVrIpNhrpAdminControlTable": mscVrIpNhrpAdminControlTable,
       "mscVrIpNhrpAdminControlEntry": mscVrIpNhrpAdminControlEntry,
       "mscVrIpNhrpSnmpAdminStatus": mscVrIpNhrpSnmpAdminStatus,
       "mscVrIpNhrpProvTable": mscVrIpNhrpProvTable,
       "mscVrIpNhrpProvEntry": mscVrIpNhrpProvEntry,
       "mscVrIpNhrpMaxResCacheEntries": mscVrIpNhrpMaxResCacheEntries,
       "mscVrIpNhrpFwdTransitRecord": mscVrIpNhrpFwdTransitRecord,
       "mscVrIpNhrpRevTransitRecord": mscVrIpNhrpRevTransitRecord,
       "mscVrIpNhrpStateTable": mscVrIpNhrpStateTable,
       "mscVrIpNhrpStateEntry": mscVrIpNhrpStateEntry,
       "mscVrIpNhrpAdminState": mscVrIpNhrpAdminState,
       "mscVrIpNhrpOperationalState": mscVrIpNhrpOperationalState,
       "mscVrIpNhrpUsageState": mscVrIpNhrpUsageState,
       "mscVrIpNhrpOperStatusTable": mscVrIpNhrpOperStatusTable,
       "mscVrIpNhrpOperStatusEntry": mscVrIpNhrpOperStatusEntry,
       "mscVrIpNhrpSnmpOperStatus": mscVrIpNhrpSnmpOperStatus,
       "mscVrIpNhrpOperTable": mscVrIpNhrpOperTable,
       "mscVrIpNhrpOperEntry": mscVrIpNhrpOperEntry,
       "mscVrIpNhrpCurrResCacheEntries": mscVrIpNhrpCurrResCacheEntries,
       "mscVrIpNhrpPeakResCacheEntries": mscVrIpNhrpPeakResCacheEntries,
       "ipNhrpMIB": ipNhrpMIB,
       "ipNhrpGroup": ipNhrpGroup,
       "ipNhrpGroupCA": ipNhrpGroupCA,
       "ipNhrpGroupCA02": ipNhrpGroupCA02,
       "ipNhrpGroupCA02A": ipNhrpGroupCA02A,
       "ipNhrpCapabilities": ipNhrpCapabilities,
       "ipNhrpCapabilitiesCA": ipNhrpCapabilitiesCA,
       "ipNhrpCapabilitiesCA02": ipNhrpCapabilitiesCA02,
       "ipNhrpCapabilitiesCA02A": ipNhrpCapabilitiesCA02A}
)
