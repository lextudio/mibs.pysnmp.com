# SNMP MIB module (Nortel-Magellan-Passport-IpMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-IpMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:26 2024
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
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
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
 EnterpriseDateAndTime,
 HexString,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
    "DashedHexString",
    "EnterpriseDateAndTime",
    "HexString",
    "Link",
    "NonReplicated")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "passportMIBs")

(vr,
 vrIndex,
 vrPp,
 vrPpIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-VirtualRouterMIB",
    "vr",
    "vrIndex",
    "vrPp",
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

_VrPpIpPort_ObjectIdentity = ObjectIdentity
vrPpIpPort = _VrPpIpPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5)
)
_VrPpIpPortRowStatusTable_Object = MibTable
vrPpIpPortRowStatusTable = _VrPpIpPortRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 1)
)
if mibBuilder.loadTexts:
    vrPpIpPortRowStatusTable.setStatus("mandatory")
_VrPpIpPortRowStatusEntry_Object = MibTableRow
vrPpIpPortRowStatusEntry = _VrPpIpPortRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 1, 1)
)
vrPpIpPortRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortRowStatusEntry.setStatus("mandatory")
_VrPpIpPortRowStatus_Type = RowStatus
_VrPpIpPortRowStatus_Object = MibTableColumn
vrPpIpPortRowStatus = _VrPpIpPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 1, 1, 1),
    _VrPpIpPortRowStatus_Type()
)
vrPpIpPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortRowStatus.setStatus("mandatory")
_VrPpIpPortComponentName_Type = DisplayString
_VrPpIpPortComponentName_Object = MibTableColumn
vrPpIpPortComponentName = _VrPpIpPortComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 1, 1, 2),
    _VrPpIpPortComponentName_Type()
)
vrPpIpPortComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortComponentName.setStatus("mandatory")
_VrPpIpPortStorageType_Type = StorageType
_VrPpIpPortStorageType_Object = MibTableColumn
vrPpIpPortStorageType = _VrPpIpPortStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 1, 1, 4),
    _VrPpIpPortStorageType_Type()
)
vrPpIpPortStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortStorageType.setStatus("mandatory")
_VrPpIpPortIndex_Type = NonReplicated
_VrPpIpPortIndex_Object = MibTableColumn
vrPpIpPortIndex = _VrPpIpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 1, 1, 10),
    _VrPpIpPortIndex_Type()
)
vrPpIpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpIpPortIndex.setStatus("mandatory")
_VrPpIpPortLogicalIf_ObjectIdentity = ObjectIdentity
vrPpIpPortLogicalIf = _VrPpIpPortLogicalIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2)
)
_VrPpIpPortLogicalIfRowStatusTable_Object = MibTable
vrPpIpPortLogicalIfRowStatusTable = _VrPpIpPortLogicalIfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 1)
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRowStatusTable.setStatus("mandatory")
_VrPpIpPortLogicalIfRowStatusEntry_Object = MibTableRow
vrPpIpPortLogicalIfRowStatusEntry = _VrPpIpPortLogicalIfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 1, 1)
)
vrPpIpPortLogicalIfRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfAddressIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRowStatusEntry.setStatus("mandatory")
_VrPpIpPortLogicalIfRowStatus_Type = RowStatus
_VrPpIpPortLogicalIfRowStatus_Object = MibTableColumn
vrPpIpPortLogicalIfRowStatus = _VrPpIpPortLogicalIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 1, 1, 1),
    _VrPpIpPortLogicalIfRowStatus_Type()
)
vrPpIpPortLogicalIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRowStatus.setStatus("mandatory")
_VrPpIpPortLogicalIfComponentName_Type = DisplayString
_VrPpIpPortLogicalIfComponentName_Object = MibTableColumn
vrPpIpPortLogicalIfComponentName = _VrPpIpPortLogicalIfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 1, 1, 2),
    _VrPpIpPortLogicalIfComponentName_Type()
)
vrPpIpPortLogicalIfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfComponentName.setStatus("mandatory")
_VrPpIpPortLogicalIfStorageType_Type = StorageType
_VrPpIpPortLogicalIfStorageType_Object = MibTableColumn
vrPpIpPortLogicalIfStorageType = _VrPpIpPortLogicalIfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 1, 1, 4),
    _VrPpIpPortLogicalIfStorageType_Type()
)
vrPpIpPortLogicalIfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfStorageType.setStatus("mandatory")
_VrPpIpPortLogicalIfAddressIndex_Type = IpAddress
_VrPpIpPortLogicalIfAddressIndex_Object = MibTableColumn
vrPpIpPortLogicalIfAddressIndex = _VrPpIpPortLogicalIfAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 1, 1, 10),
    _VrPpIpPortLogicalIfAddressIndex_Type()
)
vrPpIpPortLogicalIfAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfAddressIndex.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIf_ObjectIdentity = ObjectIdentity
vrPpIpPortLogicalIfOspfIf = _VrPpIpPortLogicalIfOspfIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2)
)
_VrPpIpPortLogicalIfOspfIfRowStatusTable_Object = MibTable
vrPpIpPortLogicalIfOspfIfRowStatusTable = _VrPpIpPortLogicalIfOspfIfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfRowStatusTable.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfRowStatusEntry_Object = MibTableRow
vrPpIpPortLogicalIfOspfIfRowStatusEntry = _VrPpIpPortLogicalIfOspfIfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 1, 1)
)
vrPpIpPortLogicalIfOspfIfRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfOspfIfIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfRowStatusEntry.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfRowStatus_Type = RowStatus
_VrPpIpPortLogicalIfOspfIfRowStatus_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfRowStatus = _VrPpIpPortLogicalIfOspfIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 1, 1, 1),
    _VrPpIpPortLogicalIfOspfIfRowStatus_Type()
)
vrPpIpPortLogicalIfOspfIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfRowStatus.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfComponentName_Type = DisplayString
_VrPpIpPortLogicalIfOspfIfComponentName_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfComponentName = _VrPpIpPortLogicalIfOspfIfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 1, 1, 2),
    _VrPpIpPortLogicalIfOspfIfComponentName_Type()
)
vrPpIpPortLogicalIfOspfIfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfComponentName.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfStorageType_Type = StorageType
_VrPpIpPortLogicalIfOspfIfStorageType_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfStorageType = _VrPpIpPortLogicalIfOspfIfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 1, 1, 4),
    _VrPpIpPortLogicalIfOspfIfStorageType_Type()
)
vrPpIpPortLogicalIfOspfIfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfStorageType.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfIndex_Type = NonReplicated
_VrPpIpPortLogicalIfOspfIfIndex_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfIndex = _VrPpIpPortLogicalIfOspfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 1, 1, 10),
    _VrPpIpPortLogicalIfOspfIfIndex_Type()
)
vrPpIpPortLogicalIfOspfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfIndex.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfTOS_ObjectIdentity = ObjectIdentity
vrPpIpPortLogicalIfOspfIfTOS = _VrPpIpPortLogicalIfOspfIfTOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 2)
)
_VrPpIpPortLogicalIfOspfIfTOSRowStatusTable_Object = MibTable
vrPpIpPortLogicalIfOspfIfTOSRowStatusTable = _VrPpIpPortLogicalIfOspfIfTOSRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfTOSRowStatusTable.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfTOSRowStatusEntry_Object = MibTableRow
vrPpIpPortLogicalIfOspfIfTOSRowStatusEntry = _VrPpIpPortLogicalIfOspfIfTOSRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 2, 1, 1)
)
vrPpIpPortLogicalIfOspfIfTOSRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfOspfIfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfOspfIfTOSMetricTosIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfTOSRowStatusEntry.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfTOSRowStatus_Type = RowStatus
_VrPpIpPortLogicalIfOspfIfTOSRowStatus_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfTOSRowStatus = _VrPpIpPortLogicalIfOspfIfTOSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 2, 1, 1, 1),
    _VrPpIpPortLogicalIfOspfIfTOSRowStatus_Type()
)
vrPpIpPortLogicalIfOspfIfTOSRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfTOSRowStatus.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfTOSComponentName_Type = DisplayString
_VrPpIpPortLogicalIfOspfIfTOSComponentName_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfTOSComponentName = _VrPpIpPortLogicalIfOspfIfTOSComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 2, 1, 1, 2),
    _VrPpIpPortLogicalIfOspfIfTOSComponentName_Type()
)
vrPpIpPortLogicalIfOspfIfTOSComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfTOSComponentName.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfTOSStorageType_Type = StorageType
_VrPpIpPortLogicalIfOspfIfTOSStorageType_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfTOSStorageType = _VrPpIpPortLogicalIfOspfIfTOSStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 2, 1, 1, 4),
    _VrPpIpPortLogicalIfOspfIfTOSStorageType_Type()
)
vrPpIpPortLogicalIfOspfIfTOSStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfTOSStorageType.setStatus("mandatory")


class _VrPpIpPortLogicalIfOspfIfTOSMetricTosIndex_Type(Integer32):
    """Custom type vrPpIpPortLogicalIfOspfIfTOSMetricTosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_VrPpIpPortLogicalIfOspfIfTOSMetricTosIndex_Type.__name__ = "Integer32"
_VrPpIpPortLogicalIfOspfIfTOSMetricTosIndex_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfTOSMetricTosIndex = _VrPpIpPortLogicalIfOspfIfTOSMetricTosIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 2, 1, 1, 10),
    _VrPpIpPortLogicalIfOspfIfTOSMetricTosIndex_Type()
)
vrPpIpPortLogicalIfOspfIfTOSMetricTosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfTOSMetricTosIndex.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfTOSProvTable_Object = MibTable
vrPpIpPortLogicalIfOspfIfTOSProvTable = _VrPpIpPortLogicalIfOspfIfTOSProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 2, 10)
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfTOSProvTable.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfTOSProvEntry_Object = MibTableRow
vrPpIpPortLogicalIfOspfIfTOSProvEntry = _VrPpIpPortLogicalIfOspfIfTOSProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 2, 10, 1)
)
vrPpIpPortLogicalIfOspfIfTOSProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfOspfIfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfOspfIfTOSMetricTosIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfTOSProvEntry.setStatus("mandatory")


class _VrPpIpPortLogicalIfOspfIfTOSTosMetric_Type(Unsigned32):
    """Custom type vrPpIpPortLogicalIfOspfIfTOSTosMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrPpIpPortLogicalIfOspfIfTOSTosMetric_Type.__name__ = "Unsigned32"
_VrPpIpPortLogicalIfOspfIfTOSTosMetric_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfTOSTosMetric = _VrPpIpPortLogicalIfOspfIfTOSTosMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 2, 10, 1, 1),
    _VrPpIpPortLogicalIfOspfIfTOSTosMetric_Type()
)
vrPpIpPortLogicalIfOspfIfTOSTosMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfTOSTosMetric.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfNbr_ObjectIdentity = ObjectIdentity
vrPpIpPortLogicalIfOspfIfNbr = _VrPpIpPortLogicalIfOspfIfNbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 3)
)
_VrPpIpPortLogicalIfOspfIfNbrRowStatusTable_Object = MibTable
vrPpIpPortLogicalIfOspfIfNbrRowStatusTable = _VrPpIpPortLogicalIfOspfIfNbrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfNbrRowStatusTable.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfNbrRowStatusEntry_Object = MibTableRow
vrPpIpPortLogicalIfOspfIfNbrRowStatusEntry = _VrPpIpPortLogicalIfOspfIfNbrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 3, 1, 1)
)
vrPpIpPortLogicalIfOspfIfNbrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfOspfIfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfOspfIfNbrAddressIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfNbrRowStatusEntry.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfNbrRowStatus_Type = RowStatus
_VrPpIpPortLogicalIfOspfIfNbrRowStatus_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfNbrRowStatus = _VrPpIpPortLogicalIfOspfIfNbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 3, 1, 1, 1),
    _VrPpIpPortLogicalIfOspfIfNbrRowStatus_Type()
)
vrPpIpPortLogicalIfOspfIfNbrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfNbrRowStatus.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfNbrComponentName_Type = DisplayString
_VrPpIpPortLogicalIfOspfIfNbrComponentName_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfNbrComponentName = _VrPpIpPortLogicalIfOspfIfNbrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 3, 1, 1, 2),
    _VrPpIpPortLogicalIfOspfIfNbrComponentName_Type()
)
vrPpIpPortLogicalIfOspfIfNbrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfNbrComponentName.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfNbrStorageType_Type = StorageType
_VrPpIpPortLogicalIfOspfIfNbrStorageType_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfNbrStorageType = _VrPpIpPortLogicalIfOspfIfNbrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 3, 1, 1, 4),
    _VrPpIpPortLogicalIfOspfIfNbrStorageType_Type()
)
vrPpIpPortLogicalIfOspfIfNbrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfNbrStorageType.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfNbrAddressIndex_Type = IpAddress
_VrPpIpPortLogicalIfOspfIfNbrAddressIndex_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfNbrAddressIndex = _VrPpIpPortLogicalIfOspfIfNbrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 3, 1, 1, 10),
    _VrPpIpPortLogicalIfOspfIfNbrAddressIndex_Type()
)
vrPpIpPortLogicalIfOspfIfNbrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfNbrAddressIndex.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfNbrProvTable_Object = MibTable
vrPpIpPortLogicalIfOspfIfNbrProvTable = _VrPpIpPortLogicalIfOspfIfNbrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 3, 10)
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfNbrProvTable.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfNbrProvEntry_Object = MibTableRow
vrPpIpPortLogicalIfOspfIfNbrProvEntry = _VrPpIpPortLogicalIfOspfIfNbrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 3, 10, 1)
)
vrPpIpPortLogicalIfOspfIfNbrProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfOspfIfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfOspfIfNbrAddressIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfNbrProvEntry.setStatus("mandatory")


class _VrPpIpPortLogicalIfOspfIfNbrPriority_Type(Unsigned32):
    """Custom type vrPpIpPortLogicalIfOspfIfNbrPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrPpIpPortLogicalIfOspfIfNbrPriority_Type.__name__ = "Unsigned32"
_VrPpIpPortLogicalIfOspfIfNbrPriority_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfNbrPriority = _VrPpIpPortLogicalIfOspfIfNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 3, 10, 1, 1),
    _VrPpIpPortLogicalIfOspfIfNbrPriority_Type()
)
vrPpIpPortLogicalIfOspfIfNbrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfNbrPriority.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfNbrOperTable_Object = MibTable
vrPpIpPortLogicalIfOspfIfNbrOperTable = _VrPpIpPortLogicalIfOspfIfNbrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 3, 11)
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfNbrOperTable.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfNbrOperEntry_Object = MibTableRow
vrPpIpPortLogicalIfOspfIfNbrOperEntry = _VrPpIpPortLogicalIfOspfIfNbrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 3, 11, 1)
)
vrPpIpPortLogicalIfOspfIfNbrOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfOspfIfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfOspfIfNbrAddressIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfNbrOperEntry.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfNbrRtrId_Type = RouterID
_VrPpIpPortLogicalIfOspfIfNbrRtrId_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfNbrRtrId = _VrPpIpPortLogicalIfOspfIfNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 3, 11, 1, 1),
    _VrPpIpPortLogicalIfOspfIfNbrRtrId_Type()
)
vrPpIpPortLogicalIfOspfIfNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfNbrRtrId.setStatus("mandatory")


class _VrPpIpPortLogicalIfOspfIfNbrOptions_Type(Unsigned32):
    """Custom type vrPpIpPortLogicalIfOspfIfNbrOptions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_VrPpIpPortLogicalIfOspfIfNbrOptions_Type.__name__ = "Unsigned32"
_VrPpIpPortLogicalIfOspfIfNbrOptions_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfNbrOptions = _VrPpIpPortLogicalIfOspfIfNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 3, 11, 1, 2),
    _VrPpIpPortLogicalIfOspfIfNbrOptions_Type()
)
vrPpIpPortLogicalIfOspfIfNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfNbrOptions.setStatus("mandatory")


class _VrPpIpPortLogicalIfOspfIfNbrState_Type(Integer32):
    """Custom type vrPpIpPortLogicalIfOspfIfNbrState based on Integer32"""
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


_VrPpIpPortLogicalIfOspfIfNbrState_Type.__name__ = "Integer32"
_VrPpIpPortLogicalIfOspfIfNbrState_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfNbrState = _VrPpIpPortLogicalIfOspfIfNbrState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 3, 11, 1, 3),
    _VrPpIpPortLogicalIfOspfIfNbrState_Type()
)
vrPpIpPortLogicalIfOspfIfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfNbrState.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfNbrEvents_Type = Counter32
_VrPpIpPortLogicalIfOspfIfNbrEvents_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfNbrEvents = _VrPpIpPortLogicalIfOspfIfNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 3, 11, 1, 4),
    _VrPpIpPortLogicalIfOspfIfNbrEvents_Type()
)
vrPpIpPortLogicalIfOspfIfNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfNbrEvents.setStatus("mandatory")


class _VrPpIpPortLogicalIfOspfIfNbrLsRetransQlen_Type(Gauge32):
    """Custom type vrPpIpPortLogicalIfOspfIfNbrLsRetransQlen based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpIpPortLogicalIfOspfIfNbrLsRetransQlen_Type.__name__ = "Gauge32"
_VrPpIpPortLogicalIfOspfIfNbrLsRetransQlen_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfNbrLsRetransQlen = _VrPpIpPortLogicalIfOspfIfNbrLsRetransQlen_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 3, 11, 1, 5),
    _VrPpIpPortLogicalIfOspfIfNbrLsRetransQlen_Type()
)
vrPpIpPortLogicalIfOspfIfNbrLsRetransQlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfNbrLsRetransQlen.setStatus("mandatory")


class _VrPpIpPortLogicalIfOspfIfNbrExchangeStatus_Type(Integer32):
    """Custom type vrPpIpPortLogicalIfOspfIfNbrExchangeStatus based on Integer32"""
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


_VrPpIpPortLogicalIfOspfIfNbrExchangeStatus_Type.__name__ = "Integer32"
_VrPpIpPortLogicalIfOspfIfNbrExchangeStatus_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfNbrExchangeStatus = _VrPpIpPortLogicalIfOspfIfNbrExchangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 3, 11, 1, 6),
    _VrPpIpPortLogicalIfOspfIfNbrExchangeStatus_Type()
)
vrPpIpPortLogicalIfOspfIfNbrExchangeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfNbrExchangeStatus.setStatus("mandatory")


class _VrPpIpPortLogicalIfOspfIfNbrPermanance_Type(Integer32):
    """Custom type vrPpIpPortLogicalIfOspfIfNbrPermanance based on Integer32"""
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


_VrPpIpPortLogicalIfOspfIfNbrPermanance_Type.__name__ = "Integer32"
_VrPpIpPortLogicalIfOspfIfNbrPermanance_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfNbrPermanance = _VrPpIpPortLogicalIfOspfIfNbrPermanance_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 3, 11, 1, 9),
    _VrPpIpPortLogicalIfOspfIfNbrPermanance_Type()
)
vrPpIpPortLogicalIfOspfIfNbrPermanance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfNbrPermanance.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfProvTable_Object = MibTable
vrPpIpPortLogicalIfOspfIfProvTable = _VrPpIpPortLogicalIfOspfIfProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 10)
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfProvTable.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfProvEntry_Object = MibTableRow
vrPpIpPortLogicalIfOspfIfProvEntry = _VrPpIpPortLogicalIfOspfIfProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 10, 1)
)
vrPpIpPortLogicalIfOspfIfProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfOspfIfIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfProvEntry.setStatus("mandatory")


class _VrPpIpPortLogicalIfOspfIfAreaId_Type(AreaID):
    """Custom type vrPpIpPortLogicalIfOspfIfAreaId based on AreaID"""
    defaultHexValue = "00000000"


_VrPpIpPortLogicalIfOspfIfAreaId_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfAreaId = _VrPpIpPortLogicalIfOspfIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 10, 1, 1),
    _VrPpIpPortLogicalIfOspfIfAreaId_Type()
)
vrPpIpPortLogicalIfOspfIfAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfAreaId.setStatus("mandatory")


class _VrPpIpPortLogicalIfOspfIfIfType_Type(Integer32):
    """Custom type vrPpIpPortLogicalIfOspfIfIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("loopback", 5),
          ("nbma", 2),
          ("pointToPoint", 3))
    )


_VrPpIpPortLogicalIfOspfIfIfType_Type.__name__ = "Integer32"
_VrPpIpPortLogicalIfOspfIfIfType_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfIfType = _VrPpIpPortLogicalIfOspfIfIfType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 10, 1, 2),
    _VrPpIpPortLogicalIfOspfIfIfType_Type()
)
vrPpIpPortLogicalIfOspfIfIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfIfType.setStatus("mandatory")


class _VrPpIpPortLogicalIfOspfIfSnmpAdminStatus_Type(Integer32):
    """Custom type vrPpIpPortLogicalIfOspfIfSnmpAdminStatus based on Integer32"""
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


_VrPpIpPortLogicalIfOspfIfSnmpAdminStatus_Type.__name__ = "Integer32"
_VrPpIpPortLogicalIfOspfIfSnmpAdminStatus_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfSnmpAdminStatus = _VrPpIpPortLogicalIfOspfIfSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 10, 1, 3),
    _VrPpIpPortLogicalIfOspfIfSnmpAdminStatus_Type()
)
vrPpIpPortLogicalIfOspfIfSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfSnmpAdminStatus.setStatus("mandatory")


class _VrPpIpPortLogicalIfOspfIfRtrPriority_Type(Unsigned32):
    """Custom type vrPpIpPortLogicalIfOspfIfRtrPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrPpIpPortLogicalIfOspfIfRtrPriority_Type.__name__ = "Unsigned32"
_VrPpIpPortLogicalIfOspfIfRtrPriority_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfRtrPriority = _VrPpIpPortLogicalIfOspfIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 10, 1, 4),
    _VrPpIpPortLogicalIfOspfIfRtrPriority_Type()
)
vrPpIpPortLogicalIfOspfIfRtrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfRtrPriority.setStatus("mandatory")


class _VrPpIpPortLogicalIfOspfIfTransitDelay_Type(Unsigned32):
    """Custom type vrPpIpPortLogicalIfOspfIfTransitDelay based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_VrPpIpPortLogicalIfOspfIfTransitDelay_Type.__name__ = "Unsigned32"
_VrPpIpPortLogicalIfOspfIfTransitDelay_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfTransitDelay = _VrPpIpPortLogicalIfOspfIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 10, 1, 5),
    _VrPpIpPortLogicalIfOspfIfTransitDelay_Type()
)
vrPpIpPortLogicalIfOspfIfTransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfTransitDelay.setStatus("mandatory")


class _VrPpIpPortLogicalIfOspfIfRetransInterval_Type(Unsigned32):
    """Custom type vrPpIpPortLogicalIfOspfIfRetransInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_VrPpIpPortLogicalIfOspfIfRetransInterval_Type.__name__ = "Unsigned32"
_VrPpIpPortLogicalIfOspfIfRetransInterval_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfRetransInterval = _VrPpIpPortLogicalIfOspfIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 10, 1, 6),
    _VrPpIpPortLogicalIfOspfIfRetransInterval_Type()
)
vrPpIpPortLogicalIfOspfIfRetransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfRetransInterval.setStatus("mandatory")


class _VrPpIpPortLogicalIfOspfIfHelloInterval_Type(Unsigned32):
    """Custom type vrPpIpPortLogicalIfOspfIfHelloInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_VrPpIpPortLogicalIfOspfIfHelloInterval_Type.__name__ = "Unsigned32"
_VrPpIpPortLogicalIfOspfIfHelloInterval_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfHelloInterval = _VrPpIpPortLogicalIfOspfIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 10, 1, 7),
    _VrPpIpPortLogicalIfOspfIfHelloInterval_Type()
)
vrPpIpPortLogicalIfOspfIfHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfHelloInterval.setStatus("mandatory")


class _VrPpIpPortLogicalIfOspfIfRtrDeadInterval_Type(Unsigned32):
    """Custom type vrPpIpPortLogicalIfOspfIfRtrDeadInterval based on Unsigned32"""
    defaultValue = 40

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_VrPpIpPortLogicalIfOspfIfRtrDeadInterval_Type.__name__ = "Unsigned32"
_VrPpIpPortLogicalIfOspfIfRtrDeadInterval_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfRtrDeadInterval = _VrPpIpPortLogicalIfOspfIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 10, 1, 8),
    _VrPpIpPortLogicalIfOspfIfRtrDeadInterval_Type()
)
vrPpIpPortLogicalIfOspfIfRtrDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfRtrDeadInterval.setStatus("mandatory")


class _VrPpIpPortLogicalIfOspfIfPollInterval_Type(Unsigned32):
    """Custom type vrPpIpPortLogicalIfOspfIfPollInterval based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_VrPpIpPortLogicalIfOspfIfPollInterval_Type.__name__ = "Unsigned32"
_VrPpIpPortLogicalIfOspfIfPollInterval_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfPollInterval = _VrPpIpPortLogicalIfOspfIfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 10, 1, 9),
    _VrPpIpPortLogicalIfOspfIfPollInterval_Type()
)
vrPpIpPortLogicalIfOspfIfPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfPollInterval.setStatus("mandatory")


class _VrPpIpPortLogicalIfOspfIfAuthKey_Type(HexString):
    """Custom type vrPpIpPortLogicalIfOspfIfAuthKey based on HexString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_VrPpIpPortLogicalIfOspfIfAuthKey_Type.__name__ = "HexString"
_VrPpIpPortLogicalIfOspfIfAuthKey_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfAuthKey = _VrPpIpPortLogicalIfOspfIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 10, 1, 10),
    _VrPpIpPortLogicalIfOspfIfAuthKey_Type()
)
vrPpIpPortLogicalIfOspfIfAuthKey.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfAuthKey.setStatus("mandatory")


class _VrPpIpPortLogicalIfOspfIfMulticastForwarding_Type(Integer32):
    """Custom type vrPpIpPortLogicalIfOspfIfMulticastForwarding based on Integer32"""
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


_VrPpIpPortLogicalIfOspfIfMulticastForwarding_Type.__name__ = "Integer32"
_VrPpIpPortLogicalIfOspfIfMulticastForwarding_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfMulticastForwarding = _VrPpIpPortLogicalIfOspfIfMulticastForwarding_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 10, 1, 12),
    _VrPpIpPortLogicalIfOspfIfMulticastForwarding_Type()
)
vrPpIpPortLogicalIfOspfIfMulticastForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfMulticastForwarding.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfOperTable_Object = MibTable
vrPpIpPortLogicalIfOspfIfOperTable = _VrPpIpPortLogicalIfOspfIfOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 11)
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfOperTable.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfOperEntry_Object = MibTableRow
vrPpIpPortLogicalIfOspfIfOperEntry = _VrPpIpPortLogicalIfOspfIfOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 11, 1)
)
vrPpIpPortLogicalIfOspfIfOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfOspfIfIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfOperEntry.setStatus("mandatory")


class _VrPpIpPortLogicalIfOspfIfState_Type(Integer32):
    """Custom type vrPpIpPortLogicalIfOspfIfState based on Integer32"""
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


_VrPpIpPortLogicalIfOspfIfState_Type.__name__ = "Integer32"
_VrPpIpPortLogicalIfOspfIfState_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfState = _VrPpIpPortLogicalIfOspfIfState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 11, 1, 1),
    _VrPpIpPortLogicalIfOspfIfState_Type()
)
vrPpIpPortLogicalIfOspfIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfState.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfDesignatedRouter_Type = IpAddress
_VrPpIpPortLogicalIfOspfIfDesignatedRouter_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfDesignatedRouter = _VrPpIpPortLogicalIfOspfIfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 11, 1, 2),
    _VrPpIpPortLogicalIfOspfIfDesignatedRouter_Type()
)
vrPpIpPortLogicalIfOspfIfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfDesignatedRouter.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfBackupDesignatedRouter_Type = IpAddress
_VrPpIpPortLogicalIfOspfIfBackupDesignatedRouter_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfBackupDesignatedRouter = _VrPpIpPortLogicalIfOspfIfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 11, 1, 3),
    _VrPpIpPortLogicalIfOspfIfBackupDesignatedRouter_Type()
)
vrPpIpPortLogicalIfOspfIfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfBackupDesignatedRouter.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfEvents_Type = Counter32
_VrPpIpPortLogicalIfOspfIfEvents_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfEvents = _VrPpIpPortLogicalIfOspfIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 11, 1, 4),
    _VrPpIpPortLogicalIfOspfIfEvents_Type()
)
vrPpIpPortLogicalIfOspfIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfEvents.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfMetricTable_Object = MibTable
vrPpIpPortLogicalIfOspfIfMetricTable = _VrPpIpPortLogicalIfOspfIfMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 12)
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfMetricTable.setStatus("mandatory")
_VrPpIpPortLogicalIfOspfIfMetricEntry_Object = MibTableRow
vrPpIpPortLogicalIfOspfIfMetricEntry = _VrPpIpPortLogicalIfOspfIfMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 12, 1)
)
vrPpIpPortLogicalIfOspfIfMetricEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfOspfIfIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfMetricEntry.setStatus("mandatory")


class _VrPpIpPortLogicalIfOspfIfMetric_Type(Unsigned32):
    """Custom type vrPpIpPortLogicalIfOspfIfMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpIpPortLogicalIfOspfIfMetric_Type.__name__ = "Unsigned32"
_VrPpIpPortLogicalIfOspfIfMetric_Object = MibTableColumn
vrPpIpPortLogicalIfOspfIfMetric = _VrPpIpPortLogicalIfOspfIfMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 2, 12, 1, 1),
    _VrPpIpPortLogicalIfOspfIfMetric_Type()
)
vrPpIpPortLogicalIfOspfIfMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfOspfIfMetric.setStatus("mandatory")
_VrPpIpPortLogicalIfRipIf_ObjectIdentity = ObjectIdentity
vrPpIpPortLogicalIfRipIf = _VrPpIpPortLogicalIfRipIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3)
)
_VrPpIpPortLogicalIfRipIfRowStatusTable_Object = MibTable
vrPpIpPortLogicalIfRipIfRowStatusTable = _VrPpIpPortLogicalIfRipIfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 1)
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfRowStatusTable.setStatus("mandatory")
_VrPpIpPortLogicalIfRipIfRowStatusEntry_Object = MibTableRow
vrPpIpPortLogicalIfRipIfRowStatusEntry = _VrPpIpPortLogicalIfRipIfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 1, 1)
)
vrPpIpPortLogicalIfRipIfRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfRipIfIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfRowStatusEntry.setStatus("mandatory")
_VrPpIpPortLogicalIfRipIfRowStatus_Type = RowStatus
_VrPpIpPortLogicalIfRipIfRowStatus_Object = MibTableColumn
vrPpIpPortLogicalIfRipIfRowStatus = _VrPpIpPortLogicalIfRipIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 1, 1, 1),
    _VrPpIpPortLogicalIfRipIfRowStatus_Type()
)
vrPpIpPortLogicalIfRipIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfRowStatus.setStatus("mandatory")
_VrPpIpPortLogicalIfRipIfComponentName_Type = DisplayString
_VrPpIpPortLogicalIfRipIfComponentName_Object = MibTableColumn
vrPpIpPortLogicalIfRipIfComponentName = _VrPpIpPortLogicalIfRipIfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 1, 1, 2),
    _VrPpIpPortLogicalIfRipIfComponentName_Type()
)
vrPpIpPortLogicalIfRipIfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfComponentName.setStatus("mandatory")
_VrPpIpPortLogicalIfRipIfStorageType_Type = StorageType
_VrPpIpPortLogicalIfRipIfStorageType_Object = MibTableColumn
vrPpIpPortLogicalIfRipIfStorageType = _VrPpIpPortLogicalIfRipIfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 1, 1, 4),
    _VrPpIpPortLogicalIfRipIfStorageType_Type()
)
vrPpIpPortLogicalIfRipIfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfStorageType.setStatus("mandatory")
_VrPpIpPortLogicalIfRipIfIndex_Type = NonReplicated
_VrPpIpPortLogicalIfRipIfIndex_Object = MibTableColumn
vrPpIpPortLogicalIfRipIfIndex = _VrPpIpPortLogicalIfRipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 1, 1, 10),
    _VrPpIpPortLogicalIfRipIfIndex_Type()
)
vrPpIpPortLogicalIfRipIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfIndex.setStatus("mandatory")
_VrPpIpPortLogicalIfRipIfNbr_ObjectIdentity = ObjectIdentity
vrPpIpPortLogicalIfRipIfNbr = _VrPpIpPortLogicalIfRipIfNbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 2)
)
_VrPpIpPortLogicalIfRipIfNbrRowStatusTable_Object = MibTable
vrPpIpPortLogicalIfRipIfNbrRowStatusTable = _VrPpIpPortLogicalIfRipIfNbrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfNbrRowStatusTable.setStatus("mandatory")
_VrPpIpPortLogicalIfRipIfNbrRowStatusEntry_Object = MibTableRow
vrPpIpPortLogicalIfRipIfNbrRowStatusEntry = _VrPpIpPortLogicalIfRipIfNbrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 2, 1, 1)
)
vrPpIpPortLogicalIfRipIfNbrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfRipIfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfRipIfNbrIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfNbrRowStatusEntry.setStatus("mandatory")
_VrPpIpPortLogicalIfRipIfNbrRowStatus_Type = RowStatus
_VrPpIpPortLogicalIfRipIfNbrRowStatus_Object = MibTableColumn
vrPpIpPortLogicalIfRipIfNbrRowStatus = _VrPpIpPortLogicalIfRipIfNbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 2, 1, 1, 1),
    _VrPpIpPortLogicalIfRipIfNbrRowStatus_Type()
)
vrPpIpPortLogicalIfRipIfNbrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfNbrRowStatus.setStatus("mandatory")
_VrPpIpPortLogicalIfRipIfNbrComponentName_Type = DisplayString
_VrPpIpPortLogicalIfRipIfNbrComponentName_Object = MibTableColumn
vrPpIpPortLogicalIfRipIfNbrComponentName = _VrPpIpPortLogicalIfRipIfNbrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 2, 1, 1, 2),
    _VrPpIpPortLogicalIfRipIfNbrComponentName_Type()
)
vrPpIpPortLogicalIfRipIfNbrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfNbrComponentName.setStatus("mandatory")
_VrPpIpPortLogicalIfRipIfNbrStorageType_Type = StorageType
_VrPpIpPortLogicalIfRipIfNbrStorageType_Object = MibTableColumn
vrPpIpPortLogicalIfRipIfNbrStorageType = _VrPpIpPortLogicalIfRipIfNbrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 2, 1, 1, 4),
    _VrPpIpPortLogicalIfRipIfNbrStorageType_Type()
)
vrPpIpPortLogicalIfRipIfNbrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfNbrStorageType.setStatus("mandatory")
_VrPpIpPortLogicalIfRipIfNbrIndex_Type = IpAddress
_VrPpIpPortLogicalIfRipIfNbrIndex_Object = MibTableColumn
vrPpIpPortLogicalIfRipIfNbrIndex = _VrPpIpPortLogicalIfRipIfNbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 2, 1, 1, 10),
    _VrPpIpPortLogicalIfRipIfNbrIndex_Type()
)
vrPpIpPortLogicalIfRipIfNbrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfNbrIndex.setStatus("mandatory")
_VrPpIpPortLogicalIfRipIfProvTable_Object = MibTable
vrPpIpPortLogicalIfRipIfProvTable = _VrPpIpPortLogicalIfRipIfProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 10)
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfProvTable.setStatus("mandatory")
_VrPpIpPortLogicalIfRipIfProvEntry_Object = MibTableRow
vrPpIpPortLogicalIfRipIfProvEntry = _VrPpIpPortLogicalIfRipIfProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 10, 1)
)
vrPpIpPortLogicalIfRipIfProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfRipIfIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfProvEntry.setStatus("mandatory")


class _VrPpIpPortLogicalIfRipIfSnmpAdminStatus_Type(Integer32):
    """Custom type vrPpIpPortLogicalIfRipIfSnmpAdminStatus based on Integer32"""
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


_VrPpIpPortLogicalIfRipIfSnmpAdminStatus_Type.__name__ = "Integer32"
_VrPpIpPortLogicalIfRipIfSnmpAdminStatus_Object = MibTableColumn
vrPpIpPortLogicalIfRipIfSnmpAdminStatus = _VrPpIpPortLogicalIfRipIfSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 10, 1, 1),
    _VrPpIpPortLogicalIfRipIfSnmpAdminStatus_Type()
)
vrPpIpPortLogicalIfRipIfSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfSnmpAdminStatus.setStatus("mandatory")


class _VrPpIpPortLogicalIfRipIfMetric_Type(Unsigned32):
    """Custom type vrPpIpPortLogicalIfRipIfMetric based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VrPpIpPortLogicalIfRipIfMetric_Type.__name__ = "Unsigned32"
_VrPpIpPortLogicalIfRipIfMetric_Object = MibTableColumn
vrPpIpPortLogicalIfRipIfMetric = _VrPpIpPortLogicalIfRipIfMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 10, 1, 2),
    _VrPpIpPortLogicalIfRipIfMetric_Type()
)
vrPpIpPortLogicalIfRipIfMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfMetric.setStatus("mandatory")


class _VrPpIpPortLogicalIfRipIfSilentFlag_Type(Integer32):
    """Custom type vrPpIpPortLogicalIfRipIfSilentFlag based on Integer32"""
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


_VrPpIpPortLogicalIfRipIfSilentFlag_Type.__name__ = "Integer32"
_VrPpIpPortLogicalIfRipIfSilentFlag_Object = MibTableColumn
vrPpIpPortLogicalIfRipIfSilentFlag = _VrPpIpPortLogicalIfRipIfSilentFlag_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 10, 1, 3),
    _VrPpIpPortLogicalIfRipIfSilentFlag_Type()
)
vrPpIpPortLogicalIfRipIfSilentFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfSilentFlag.setStatus("obsolete")


class _VrPpIpPortLogicalIfRipIfPoisonReverseFlag_Type(Integer32):
    """Custom type vrPpIpPortLogicalIfRipIfPoisonReverseFlag based on Integer32"""
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


_VrPpIpPortLogicalIfRipIfPoisonReverseFlag_Type.__name__ = "Integer32"
_VrPpIpPortLogicalIfRipIfPoisonReverseFlag_Object = MibTableColumn
vrPpIpPortLogicalIfRipIfPoisonReverseFlag = _VrPpIpPortLogicalIfRipIfPoisonReverseFlag_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 10, 1, 4),
    _VrPpIpPortLogicalIfRipIfPoisonReverseFlag_Type()
)
vrPpIpPortLogicalIfRipIfPoisonReverseFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfPoisonReverseFlag.setStatus("mandatory")


class _VrPpIpPortLogicalIfRipIfFlashUpdateFlag_Type(Integer32):
    """Custom type vrPpIpPortLogicalIfRipIfFlashUpdateFlag based on Integer32"""
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


_VrPpIpPortLogicalIfRipIfFlashUpdateFlag_Type.__name__ = "Integer32"
_VrPpIpPortLogicalIfRipIfFlashUpdateFlag_Object = MibTableColumn
vrPpIpPortLogicalIfRipIfFlashUpdateFlag = _VrPpIpPortLogicalIfRipIfFlashUpdateFlag_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 10, 1, 5),
    _VrPpIpPortLogicalIfRipIfFlashUpdateFlag_Type()
)
vrPpIpPortLogicalIfRipIfFlashUpdateFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfFlashUpdateFlag.setStatus("mandatory")


class _VrPpIpPortLogicalIfRipIfNetworkRouteStatus_Type(Integer32):
    """Custom type vrPpIpPortLogicalIfRipIfNetworkRouteStatus based on Integer32"""
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


_VrPpIpPortLogicalIfRipIfNetworkRouteStatus_Type.__name__ = "Integer32"
_VrPpIpPortLogicalIfRipIfNetworkRouteStatus_Object = MibTableColumn
vrPpIpPortLogicalIfRipIfNetworkRouteStatus = _VrPpIpPortLogicalIfRipIfNetworkRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 10, 1, 6),
    _VrPpIpPortLogicalIfRipIfNetworkRouteStatus_Type()
)
vrPpIpPortLogicalIfRipIfNetworkRouteStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfNetworkRouteStatus.setStatus("mandatory")


class _VrPpIpPortLogicalIfRipIfDefaultRouteMetric_Type(Unsigned32):
    """Custom type vrPpIpPortLogicalIfRipIfDefaultRouteMetric based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VrPpIpPortLogicalIfRipIfDefaultRouteMetric_Type.__name__ = "Unsigned32"
_VrPpIpPortLogicalIfRipIfDefaultRouteMetric_Object = MibTableColumn
vrPpIpPortLogicalIfRipIfDefaultRouteMetric = _VrPpIpPortLogicalIfRipIfDefaultRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 10, 1, 7),
    _VrPpIpPortLogicalIfRipIfDefaultRouteMetric_Type()
)
vrPpIpPortLogicalIfRipIfDefaultRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfDefaultRouteMetric.setStatus("mandatory")


class _VrPpIpPortLogicalIfRipIfAcceptDefault_Type(Integer32):
    """Custom type vrPpIpPortLogicalIfRipIfAcceptDefault based on Integer32"""
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


_VrPpIpPortLogicalIfRipIfAcceptDefault_Type.__name__ = "Integer32"
_VrPpIpPortLogicalIfRipIfAcceptDefault_Object = MibTableColumn
vrPpIpPortLogicalIfRipIfAcceptDefault = _VrPpIpPortLogicalIfRipIfAcceptDefault_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 10, 1, 8),
    _VrPpIpPortLogicalIfRipIfAcceptDefault_Type()
)
vrPpIpPortLogicalIfRipIfAcceptDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfAcceptDefault.setStatus("mandatory")


class _VrPpIpPortLogicalIfRipIfIfConfSend_Type(Integer32):
    """Custom type vrPpIpPortLogicalIfRipIfIfConfSend based on Integer32"""
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


_VrPpIpPortLogicalIfRipIfIfConfSend_Type.__name__ = "Integer32"
_VrPpIpPortLogicalIfRipIfIfConfSend_Object = MibTableColumn
vrPpIpPortLogicalIfRipIfIfConfSend = _VrPpIpPortLogicalIfRipIfIfConfSend_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 10, 1, 12),
    _VrPpIpPortLogicalIfRipIfIfConfSend_Type()
)
vrPpIpPortLogicalIfRipIfIfConfSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfIfConfSend.setStatus("mandatory")


class _VrPpIpPortLogicalIfRipIfIfConfReceive_Type(Integer32):
    """Custom type vrPpIpPortLogicalIfRipIfIfConfReceive based on Integer32"""
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


_VrPpIpPortLogicalIfRipIfIfConfReceive_Type.__name__ = "Integer32"
_VrPpIpPortLogicalIfRipIfIfConfReceive_Object = MibTableColumn
vrPpIpPortLogicalIfRipIfIfConfReceive = _VrPpIpPortLogicalIfRipIfIfConfReceive_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 10, 1, 13),
    _VrPpIpPortLogicalIfRipIfIfConfReceive_Type()
)
vrPpIpPortLogicalIfRipIfIfConfReceive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfIfConfReceive.setStatus("mandatory")
_VrPpIpPortLogicalIfRipIfStatTable_Object = MibTable
vrPpIpPortLogicalIfRipIfStatTable = _VrPpIpPortLogicalIfRipIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 11)
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfStatTable.setStatus("mandatory")
_VrPpIpPortLogicalIfRipIfStatEntry_Object = MibTableRow
vrPpIpPortLogicalIfRipIfStatEntry = _VrPpIpPortLogicalIfRipIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 11, 1)
)
vrPpIpPortLogicalIfRipIfStatEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfRipIfIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfStatEntry.setStatus("mandatory")


class _VrPpIpPortLogicalIfRipIfIfBadPacketRcv_Type(Unsigned32):
    """Custom type vrPpIpPortLogicalIfRipIfIfBadPacketRcv based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpIpPortLogicalIfRipIfIfBadPacketRcv_Type.__name__ = "Unsigned32"
_VrPpIpPortLogicalIfRipIfIfBadPacketRcv_Object = MibTableColumn
vrPpIpPortLogicalIfRipIfIfBadPacketRcv = _VrPpIpPortLogicalIfRipIfIfBadPacketRcv_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 11, 1, 1),
    _VrPpIpPortLogicalIfRipIfIfBadPacketRcv_Type()
)
vrPpIpPortLogicalIfRipIfIfBadPacketRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfIfBadPacketRcv.setStatus("mandatory")


class _VrPpIpPortLogicalIfRipIfIfBadRouteRcv_Type(Unsigned32):
    """Custom type vrPpIpPortLogicalIfRipIfIfBadRouteRcv based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpIpPortLogicalIfRipIfIfBadRouteRcv_Type.__name__ = "Unsigned32"
_VrPpIpPortLogicalIfRipIfIfBadRouteRcv_Object = MibTableColumn
vrPpIpPortLogicalIfRipIfIfBadRouteRcv = _VrPpIpPortLogicalIfRipIfIfBadRouteRcv_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 11, 1, 2),
    _VrPpIpPortLogicalIfRipIfIfBadRouteRcv_Type()
)
vrPpIpPortLogicalIfRipIfIfBadRouteRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfIfBadRouteRcv.setStatus("mandatory")


class _VrPpIpPortLogicalIfRipIfIfTriggeredUpdates_Type(Unsigned32):
    """Custom type vrPpIpPortLogicalIfRipIfIfTriggeredUpdates based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrPpIpPortLogicalIfRipIfIfTriggeredUpdates_Type.__name__ = "Unsigned32"
_VrPpIpPortLogicalIfRipIfIfTriggeredUpdates_Object = MibTableColumn
vrPpIpPortLogicalIfRipIfIfTriggeredUpdates = _VrPpIpPortLogicalIfRipIfIfTriggeredUpdates_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 3, 11, 1, 3),
    _VrPpIpPortLogicalIfRipIfIfTriggeredUpdates_Type()
)
vrPpIpPortLogicalIfRipIfIfTriggeredUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfRipIfIfTriggeredUpdates.setStatus("mandatory")
_VrPpIpPortLogicalIfIgmpIf_ObjectIdentity = ObjectIdentity
vrPpIpPortLogicalIfIgmpIf = _VrPpIpPortLogicalIfIgmpIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 5)
)
_VrPpIpPortLogicalIfIgmpIfRowStatusTable_Object = MibTable
vrPpIpPortLogicalIfIgmpIfRowStatusTable = _VrPpIpPortLogicalIfIgmpIfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 5, 1)
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfIgmpIfRowStatusTable.setStatus("mandatory")
_VrPpIpPortLogicalIfIgmpIfRowStatusEntry_Object = MibTableRow
vrPpIpPortLogicalIfIgmpIfRowStatusEntry = _VrPpIpPortLogicalIfIgmpIfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 5, 1, 1)
)
vrPpIpPortLogicalIfIgmpIfRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfIgmpIfIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfIgmpIfRowStatusEntry.setStatus("mandatory")
_VrPpIpPortLogicalIfIgmpIfRowStatus_Type = RowStatus
_VrPpIpPortLogicalIfIgmpIfRowStatus_Object = MibTableColumn
vrPpIpPortLogicalIfIgmpIfRowStatus = _VrPpIpPortLogicalIfIgmpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 5, 1, 1, 1),
    _VrPpIpPortLogicalIfIgmpIfRowStatus_Type()
)
vrPpIpPortLogicalIfIgmpIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfIgmpIfRowStatus.setStatus("mandatory")
_VrPpIpPortLogicalIfIgmpIfComponentName_Type = DisplayString
_VrPpIpPortLogicalIfIgmpIfComponentName_Object = MibTableColumn
vrPpIpPortLogicalIfIgmpIfComponentName = _VrPpIpPortLogicalIfIgmpIfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 5, 1, 1, 2),
    _VrPpIpPortLogicalIfIgmpIfComponentName_Type()
)
vrPpIpPortLogicalIfIgmpIfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfIgmpIfComponentName.setStatus("mandatory")
_VrPpIpPortLogicalIfIgmpIfStorageType_Type = StorageType
_VrPpIpPortLogicalIfIgmpIfStorageType_Object = MibTableColumn
vrPpIpPortLogicalIfIgmpIfStorageType = _VrPpIpPortLogicalIfIgmpIfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 5, 1, 1, 4),
    _VrPpIpPortLogicalIfIgmpIfStorageType_Type()
)
vrPpIpPortLogicalIfIgmpIfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfIgmpIfStorageType.setStatus("mandatory")
_VrPpIpPortLogicalIfIgmpIfIndex_Type = NonReplicated
_VrPpIpPortLogicalIfIgmpIfIndex_Object = MibTableColumn
vrPpIpPortLogicalIfIgmpIfIndex = _VrPpIpPortLogicalIfIgmpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 5, 1, 1, 10),
    _VrPpIpPortLogicalIfIgmpIfIndex_Type()
)
vrPpIpPortLogicalIfIgmpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfIgmpIfIndex.setStatus("mandatory")
_VrPpIpPortLogicalIfIgmpIfProvTable_Object = MibTable
vrPpIpPortLogicalIfIgmpIfProvTable = _VrPpIpPortLogicalIfIgmpIfProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 5, 10)
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfIgmpIfProvTable.setStatus("mandatory")
_VrPpIpPortLogicalIfIgmpIfProvEntry_Object = MibTableRow
vrPpIpPortLogicalIfIgmpIfProvEntry = _VrPpIpPortLogicalIfIgmpIfProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 5, 10, 1)
)
vrPpIpPortLogicalIfIgmpIfProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfIgmpIfIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfIgmpIfProvEntry.setStatus("mandatory")


class _VrPpIpPortLogicalIfIgmpIfVersion_Type(Integer32):
    """Custom type vrPpIpPortLogicalIfIgmpIfVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("v2", 2)
    )


_VrPpIpPortLogicalIfIgmpIfVersion_Type.__name__ = "Integer32"
_VrPpIpPortLogicalIfIgmpIfVersion_Object = MibTableColumn
vrPpIpPortLogicalIfIgmpIfVersion = _VrPpIpPortLogicalIfIgmpIfVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 5, 10, 1, 1),
    _VrPpIpPortLogicalIfIgmpIfVersion_Type()
)
vrPpIpPortLogicalIfIgmpIfVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfIgmpIfVersion.setStatus("mandatory")


class _VrPpIpPortLogicalIfIgmpIfQueryInterval_Type(Unsigned32):
    """Custom type vrPpIpPortLogicalIfIgmpIfQueryInterval based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_VrPpIpPortLogicalIfIgmpIfQueryInterval_Type.__name__ = "Unsigned32"
_VrPpIpPortLogicalIfIgmpIfQueryInterval_Object = MibTableColumn
vrPpIpPortLogicalIfIgmpIfQueryInterval = _VrPpIpPortLogicalIfIgmpIfQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 5, 10, 1, 2),
    _VrPpIpPortLogicalIfIgmpIfQueryInterval_Type()
)
vrPpIpPortLogicalIfIgmpIfQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfIgmpIfQueryInterval.setStatus("mandatory")


class _VrPpIpPortLogicalIfIgmpIfQueryMaxRespTime_Type(Unsigned32):
    """Custom type vrPpIpPortLogicalIfIgmpIfQueryMaxRespTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_VrPpIpPortLogicalIfIgmpIfQueryMaxRespTime_Type.__name__ = "Unsigned32"
_VrPpIpPortLogicalIfIgmpIfQueryMaxRespTime_Object = MibTableColumn
vrPpIpPortLogicalIfIgmpIfQueryMaxRespTime = _VrPpIpPortLogicalIfIgmpIfQueryMaxRespTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 5, 10, 1, 3),
    _VrPpIpPortLogicalIfIgmpIfQueryMaxRespTime_Type()
)
vrPpIpPortLogicalIfIgmpIfQueryMaxRespTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfIgmpIfQueryMaxRespTime.setStatus("mandatory")
_VrPpIpPortLogicalIfIgmpIfOperTable_Object = MibTable
vrPpIpPortLogicalIfIgmpIfOperTable = _VrPpIpPortLogicalIfIgmpIfOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 5, 11)
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfIgmpIfOperTable.setStatus("mandatory")
_VrPpIpPortLogicalIfIgmpIfOperEntry_Object = MibTableRow
vrPpIpPortLogicalIfIgmpIfOperEntry = _VrPpIpPortLogicalIfIgmpIfOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 5, 11, 1)
)
vrPpIpPortLogicalIfIgmpIfOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfIgmpIfIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfIgmpIfOperEntry.setStatus("mandatory")


class _VrPpIpPortLogicalIfIgmpIfQuerier_Type(IpAddress):
    """Custom type vrPpIpPortLogicalIfIgmpIfQuerier based on IpAddress"""
    defaultHexValue = "00000000"


_VrPpIpPortLogicalIfIgmpIfQuerier_Object = MibTableColumn
vrPpIpPortLogicalIfIgmpIfQuerier = _VrPpIpPortLogicalIfIgmpIfQuerier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 5, 11, 1, 2),
    _VrPpIpPortLogicalIfIgmpIfQuerier_Type()
)
vrPpIpPortLogicalIfIgmpIfQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfIgmpIfQuerier.setStatus("mandatory")
_VrPpIpPortLogicalIfIgmpIfWrongVersionQuery_Type = Counter32
_VrPpIpPortLogicalIfIgmpIfWrongVersionQuery_Object = MibTableColumn
vrPpIpPortLogicalIfIgmpIfWrongVersionQuery = _VrPpIpPortLogicalIfIgmpIfWrongVersionQuery_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 5, 11, 1, 3),
    _VrPpIpPortLogicalIfIgmpIfWrongVersionQuery_Type()
)
vrPpIpPortLogicalIfIgmpIfWrongVersionQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfIgmpIfWrongVersionQuery.setStatus("mandatory")
_VrPpIpPortLogicalIfIgmpIfJoins_Type = Counter32
_VrPpIpPortLogicalIfIgmpIfJoins_Object = MibTableColumn
vrPpIpPortLogicalIfIgmpIfJoins = _VrPpIpPortLogicalIfIgmpIfJoins_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 5, 11, 1, 4),
    _VrPpIpPortLogicalIfIgmpIfJoins_Type()
)
vrPpIpPortLogicalIfIgmpIfJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfIgmpIfJoins.setStatus("mandatory")


class _VrPpIpPortLogicalIfIgmpIfGroups_Type(Gauge32):
    """Custom type vrPpIpPortLogicalIfIgmpIfGroups based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4292967295),
    )


_VrPpIpPortLogicalIfIgmpIfGroups_Type.__name__ = "Gauge32"
_VrPpIpPortLogicalIfIgmpIfGroups_Object = MibTableColumn
vrPpIpPortLogicalIfIgmpIfGroups = _VrPpIpPortLogicalIfIgmpIfGroups_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 5, 11, 1, 5),
    _VrPpIpPortLogicalIfIgmpIfGroups_Type()
)
vrPpIpPortLogicalIfIgmpIfGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfIgmpIfGroups.setStatus("mandatory")


class _VrPpIpPortLogicalIfIgmpIfQuerierExpiryTime_Type(Unsigned32):
    """Custom type vrPpIpPortLogicalIfIgmpIfQuerierExpiryTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_VrPpIpPortLogicalIfIgmpIfQuerierExpiryTime_Type.__name__ = "Unsigned32"
_VrPpIpPortLogicalIfIgmpIfQuerierExpiryTime_Object = MibTableColumn
vrPpIpPortLogicalIfIgmpIfQuerierExpiryTime = _VrPpIpPortLogicalIfIgmpIfQuerierExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 5, 11, 1, 6),
    _VrPpIpPortLogicalIfIgmpIfQuerierExpiryTime_Type()
)
vrPpIpPortLogicalIfIgmpIfQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfIgmpIfQuerierExpiryTime.setStatus("mandatory")
_VrPpIpPortLogicalIfPimSmIf_ObjectIdentity = ObjectIdentity
vrPpIpPortLogicalIfPimSmIf = _VrPpIpPortLogicalIfPimSmIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 6)
)
_VrPpIpPortLogicalIfPimSmIfRowStatusTable_Object = MibTable
vrPpIpPortLogicalIfPimSmIfRowStatusTable = _VrPpIpPortLogicalIfPimSmIfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 6, 1)
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfPimSmIfRowStatusTable.setStatus("mandatory")
_VrPpIpPortLogicalIfPimSmIfRowStatusEntry_Object = MibTableRow
vrPpIpPortLogicalIfPimSmIfRowStatusEntry = _VrPpIpPortLogicalIfPimSmIfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 6, 1, 1)
)
vrPpIpPortLogicalIfPimSmIfRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfPimSmIfIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfPimSmIfRowStatusEntry.setStatus("mandatory")
_VrPpIpPortLogicalIfPimSmIfRowStatus_Type = RowStatus
_VrPpIpPortLogicalIfPimSmIfRowStatus_Object = MibTableColumn
vrPpIpPortLogicalIfPimSmIfRowStatus = _VrPpIpPortLogicalIfPimSmIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 6, 1, 1, 1),
    _VrPpIpPortLogicalIfPimSmIfRowStatus_Type()
)
vrPpIpPortLogicalIfPimSmIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfPimSmIfRowStatus.setStatus("mandatory")
_VrPpIpPortLogicalIfPimSmIfComponentName_Type = DisplayString
_VrPpIpPortLogicalIfPimSmIfComponentName_Object = MibTableColumn
vrPpIpPortLogicalIfPimSmIfComponentName = _VrPpIpPortLogicalIfPimSmIfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 6, 1, 1, 2),
    _VrPpIpPortLogicalIfPimSmIfComponentName_Type()
)
vrPpIpPortLogicalIfPimSmIfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfPimSmIfComponentName.setStatus("mandatory")
_VrPpIpPortLogicalIfPimSmIfStorageType_Type = StorageType
_VrPpIpPortLogicalIfPimSmIfStorageType_Object = MibTableColumn
vrPpIpPortLogicalIfPimSmIfStorageType = _VrPpIpPortLogicalIfPimSmIfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 6, 1, 1, 4),
    _VrPpIpPortLogicalIfPimSmIfStorageType_Type()
)
vrPpIpPortLogicalIfPimSmIfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfPimSmIfStorageType.setStatus("mandatory")
_VrPpIpPortLogicalIfPimSmIfIndex_Type = NonReplicated
_VrPpIpPortLogicalIfPimSmIfIndex_Object = MibTableColumn
vrPpIpPortLogicalIfPimSmIfIndex = _VrPpIpPortLogicalIfPimSmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 6, 1, 1, 10),
    _VrPpIpPortLogicalIfPimSmIfIndex_Type()
)
vrPpIpPortLogicalIfPimSmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfPimSmIfIndex.setStatus("mandatory")
_VrPpIpPortLogicalIfPimSmIfProvTable_Object = MibTable
vrPpIpPortLogicalIfPimSmIfProvTable = _VrPpIpPortLogicalIfPimSmIfProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 6, 10)
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfPimSmIfProvTable.setStatus("mandatory")
_VrPpIpPortLogicalIfPimSmIfProvEntry_Object = MibTableRow
vrPpIpPortLogicalIfPimSmIfProvEntry = _VrPpIpPortLogicalIfPimSmIfProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 6, 10, 1)
)
vrPpIpPortLogicalIfPimSmIfProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfPimSmIfIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfPimSmIfProvEntry.setStatus("mandatory")


class _VrPpIpPortLogicalIfPimSmIfHelloInterval_Type(Unsigned32):
    """Custom type vrPpIpPortLogicalIfPimSmIfHelloInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_VrPpIpPortLogicalIfPimSmIfHelloInterval_Type.__name__ = "Unsigned32"
_VrPpIpPortLogicalIfPimSmIfHelloInterval_Object = MibTableColumn
vrPpIpPortLogicalIfPimSmIfHelloInterval = _VrPpIpPortLogicalIfPimSmIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 6, 10, 1, 1),
    _VrPpIpPortLogicalIfPimSmIfHelloInterval_Type()
)
vrPpIpPortLogicalIfPimSmIfHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfPimSmIfHelloInterval.setStatus("mandatory")
_VrPpIpPortLogicalIfPimSmIfOperTable_Object = MibTable
vrPpIpPortLogicalIfPimSmIfOperTable = _VrPpIpPortLogicalIfPimSmIfOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 6, 11)
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfPimSmIfOperTable.setStatus("mandatory")
_VrPpIpPortLogicalIfPimSmIfOperEntry_Object = MibTableRow
vrPpIpPortLogicalIfPimSmIfOperEntry = _VrPpIpPortLogicalIfPimSmIfOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 6, 11, 1)
)
vrPpIpPortLogicalIfPimSmIfOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfPimSmIfIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfPimSmIfOperEntry.setStatus("mandatory")
_VrPpIpPortLogicalIfPimSmIfDesignatedRouter_Type = IpAddress
_VrPpIpPortLogicalIfPimSmIfDesignatedRouter_Object = MibTableColumn
vrPpIpPortLogicalIfPimSmIfDesignatedRouter = _VrPpIpPortLogicalIfPimSmIfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 6, 11, 1, 1),
    _VrPpIpPortLogicalIfPimSmIfDesignatedRouter_Type()
)
vrPpIpPortLogicalIfPimSmIfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfPimSmIfDesignatedRouter.setStatus("mandatory")
_VrPpIpPortLogicalIfProvTable_Object = MibTable
vrPpIpPortLogicalIfProvTable = _VrPpIpPortLogicalIfProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 10)
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfProvTable.setStatus("mandatory")
_VrPpIpPortLogicalIfProvEntry_Object = MibTableRow
vrPpIpPortLogicalIfProvEntry = _VrPpIpPortLogicalIfProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 10, 1)
)
vrPpIpPortLogicalIfProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfAddressIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfProvEntry.setStatus("mandatory")


class _VrPpIpPortLogicalIfNetMask_Type(IpAddress):
    """Custom type vrPpIpPortLogicalIfNetMask based on IpAddress"""
    defaultHexValue = "00000000"


_VrPpIpPortLogicalIfNetMask_Object = MibTableColumn
vrPpIpPortLogicalIfNetMask = _VrPpIpPortLogicalIfNetMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 10, 1, 1),
    _VrPpIpPortLogicalIfNetMask_Type()
)
vrPpIpPortLogicalIfNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfNetMask.setStatus("mandatory")


class _VrPpIpPortLogicalIfBroadcastAddress_Type(IpAddress):
    """Custom type vrPpIpPortLogicalIfBroadcastAddress based on IpAddress"""
    defaultHexValue = "00000000"


_VrPpIpPortLogicalIfBroadcastAddress_Object = MibTableColumn
vrPpIpPortLogicalIfBroadcastAddress = _VrPpIpPortLogicalIfBroadcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 10, 1, 2),
    _VrPpIpPortLogicalIfBroadcastAddress_Type()
)
vrPpIpPortLogicalIfBroadcastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfBroadcastAddress.setStatus("mandatory")


class _VrPpIpPortLogicalIfLinkDestinationAddress_Type(IpAddress):
    """Custom type vrPpIpPortLogicalIfLinkDestinationAddress based on IpAddress"""
    defaultHexValue = "00000000"


_VrPpIpPortLogicalIfLinkDestinationAddress_Object = MibTableColumn
vrPpIpPortLogicalIfLinkDestinationAddress = _VrPpIpPortLogicalIfLinkDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 10, 1, 3),
    _VrPpIpPortLogicalIfLinkDestinationAddress_Type()
)
vrPpIpPortLogicalIfLinkDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfLinkDestinationAddress.setStatus("mandatory")
_VrPpIpPortLogicalIfLinkToPimSmCandidateRp_Type = Link
_VrPpIpPortLogicalIfLinkToPimSmCandidateRp_Object = MibTableColumn
vrPpIpPortLogicalIfLinkToPimSmCandidateRp = _VrPpIpPortLogicalIfLinkToPimSmCandidateRp_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 10, 1, 4),
    _VrPpIpPortLogicalIfLinkToPimSmCandidateRp_Type()
)
vrPpIpPortLogicalIfLinkToPimSmCandidateRp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfLinkToPimSmCandidateRp.setStatus("mandatory")
_VrPpIpPortLogicalIfLinkToPimSmCandidateBsr_Type = Link
_VrPpIpPortLogicalIfLinkToPimSmCandidateBsr_Object = MibTableColumn
vrPpIpPortLogicalIfLinkToPimSmCandidateBsr = _VrPpIpPortLogicalIfLinkToPimSmCandidateBsr_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 10, 1, 5),
    _VrPpIpPortLogicalIfLinkToPimSmCandidateBsr_Type()
)
vrPpIpPortLogicalIfLinkToPimSmCandidateBsr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfLinkToPimSmCandidateBsr.setStatus("mandatory")
_VrPpIpPortLogicalIfLinkToMulStaticGpTable_Object = MibTable
vrPpIpPortLogicalIfLinkToMulStaticGpTable = _VrPpIpPortLogicalIfLinkToMulStaticGpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 706)
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfLinkToMulStaticGpTable.setStatus("mandatory")
_VrPpIpPortLogicalIfLinkToMulStaticGpEntry_Object = MibTableRow
vrPpIpPortLogicalIfLinkToMulStaticGpEntry = _VrPpIpPortLogicalIfLinkToMulStaticGpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 706, 1)
)
vrPpIpPortLogicalIfLinkToMulStaticGpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortLogicalIfLinkToMulStaticGpValue"),
)
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfLinkToMulStaticGpEntry.setStatus("mandatory")
_VrPpIpPortLogicalIfLinkToMulStaticGpValue_Type = Link
_VrPpIpPortLogicalIfLinkToMulStaticGpValue_Object = MibTableColumn
vrPpIpPortLogicalIfLinkToMulStaticGpValue = _VrPpIpPortLogicalIfLinkToMulStaticGpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 706, 1, 1),
    _VrPpIpPortLogicalIfLinkToMulStaticGpValue_Type()
)
vrPpIpPortLogicalIfLinkToMulStaticGpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfLinkToMulStaticGpValue.setStatus("mandatory")
_VrPpIpPortLogicalIfLinkToMulStaticGpRowStatus_Type = RowStatus
_VrPpIpPortLogicalIfLinkToMulStaticGpRowStatus_Object = MibTableColumn
vrPpIpPortLogicalIfLinkToMulStaticGpRowStatus = _VrPpIpPortLogicalIfLinkToMulStaticGpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 2, 706, 1, 2),
    _VrPpIpPortLogicalIfLinkToMulStaticGpRowStatus_Type()
)
vrPpIpPortLogicalIfLinkToMulStaticGpRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vrPpIpPortLogicalIfLinkToMulStaticGpRowStatus.setStatus("mandatory")
_VrPpIpPortNs_ObjectIdentity = ObjectIdentity
vrPpIpPortNs = _VrPpIpPortNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 3)
)
_VrPpIpPortNsRowStatusTable_Object = MibTable
vrPpIpPortNsRowStatusTable = _VrPpIpPortNsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 3, 1)
)
if mibBuilder.loadTexts:
    vrPpIpPortNsRowStatusTable.setStatus("mandatory")
_VrPpIpPortNsRowStatusEntry_Object = MibTableRow
vrPpIpPortNsRowStatusEntry = _VrPpIpPortNsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 3, 1, 1)
)
vrPpIpPortNsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortNsIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortNsRowStatusEntry.setStatus("mandatory")
_VrPpIpPortNsRowStatus_Type = RowStatus
_VrPpIpPortNsRowStatus_Object = MibTableColumn
vrPpIpPortNsRowStatus = _VrPpIpPortNsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 3, 1, 1, 1),
    _VrPpIpPortNsRowStatus_Type()
)
vrPpIpPortNsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortNsRowStatus.setStatus("mandatory")
_VrPpIpPortNsComponentName_Type = DisplayString
_VrPpIpPortNsComponentName_Object = MibTableColumn
vrPpIpPortNsComponentName = _VrPpIpPortNsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 3, 1, 1, 2),
    _VrPpIpPortNsComponentName_Type()
)
vrPpIpPortNsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortNsComponentName.setStatus("mandatory")
_VrPpIpPortNsStorageType_Type = StorageType
_VrPpIpPortNsStorageType_Object = MibTableColumn
vrPpIpPortNsStorageType = _VrPpIpPortNsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 3, 1, 1, 4),
    _VrPpIpPortNsStorageType_Type()
)
vrPpIpPortNsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortNsStorageType.setStatus("mandatory")
_VrPpIpPortNsIndex_Type = NonReplicated
_VrPpIpPortNsIndex_Object = MibTableColumn
vrPpIpPortNsIndex = _VrPpIpPortNsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 3, 1, 1, 10),
    _VrPpIpPortNsIndex_Type()
)
vrPpIpPortNsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpIpPortNsIndex.setStatus("mandatory")
_VrPpIpPortNsProvTable_Object = MibTable
vrPpIpPortNsProvTable = _VrPpIpPortNsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 3, 10)
)
if mibBuilder.loadTexts:
    vrPpIpPortNsProvTable.setStatus("mandatory")
_VrPpIpPortNsProvEntry_Object = MibTableRow
vrPpIpPortNsProvEntry = _VrPpIpPortNsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 3, 10, 1)
)
vrPpIpPortNsProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortNsIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortNsProvEntry.setStatus("mandatory")


class _VrPpIpPortNsIncomingFilter_Type(AsciiString):
    """Custom type vrPpIpPortNsIncomingFilter based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrPpIpPortNsIncomingFilter_Type.__name__ = "AsciiString"
_VrPpIpPortNsIncomingFilter_Object = MibTableColumn
vrPpIpPortNsIncomingFilter = _VrPpIpPortNsIncomingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 3, 10, 1, 1),
    _VrPpIpPortNsIncomingFilter_Type()
)
vrPpIpPortNsIncomingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortNsIncomingFilter.setStatus("mandatory")


class _VrPpIpPortNsOutgoingFilter_Type(AsciiString):
    """Custom type vrPpIpPortNsOutgoingFilter based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrPpIpPortNsOutgoingFilter_Type.__name__ = "AsciiString"
_VrPpIpPortNsOutgoingFilter_Object = MibTableColumn
vrPpIpPortNsOutgoingFilter = _VrPpIpPortNsOutgoingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 3, 10, 1, 2),
    _VrPpIpPortNsOutgoingFilter_Type()
)
vrPpIpPortNsOutgoingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortNsOutgoingFilter.setStatus("mandatory")
_VrPpIpPortBootpP_ObjectIdentity = ObjectIdentity
vrPpIpPortBootpP = _VrPpIpPortBootpP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4)
)
_VrPpIpPortBootpPRowStatusTable_Object = MibTable
vrPpIpPortBootpPRowStatusTable = _VrPpIpPortBootpPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 1)
)
if mibBuilder.loadTexts:
    vrPpIpPortBootpPRowStatusTable.setStatus("mandatory")
_VrPpIpPortBootpPRowStatusEntry_Object = MibTableRow
vrPpIpPortBootpPRowStatusEntry = _VrPpIpPortBootpPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 1, 1)
)
vrPpIpPortBootpPRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortBootpPIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortBootpPRowStatusEntry.setStatus("mandatory")
_VrPpIpPortBootpPRowStatus_Type = RowStatus
_VrPpIpPortBootpPRowStatus_Object = MibTableColumn
vrPpIpPortBootpPRowStatus = _VrPpIpPortBootpPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 1, 1, 1),
    _VrPpIpPortBootpPRowStatus_Type()
)
vrPpIpPortBootpPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortBootpPRowStatus.setStatus("mandatory")
_VrPpIpPortBootpPComponentName_Type = DisplayString
_VrPpIpPortBootpPComponentName_Object = MibTableColumn
vrPpIpPortBootpPComponentName = _VrPpIpPortBootpPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 1, 1, 2),
    _VrPpIpPortBootpPComponentName_Type()
)
vrPpIpPortBootpPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortBootpPComponentName.setStatus("mandatory")
_VrPpIpPortBootpPStorageType_Type = StorageType
_VrPpIpPortBootpPStorageType_Object = MibTableColumn
vrPpIpPortBootpPStorageType = _VrPpIpPortBootpPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 1, 1, 4),
    _VrPpIpPortBootpPStorageType_Type()
)
vrPpIpPortBootpPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortBootpPStorageType.setStatus("mandatory")
_VrPpIpPortBootpPIndex_Type = NonReplicated
_VrPpIpPortBootpPIndex_Object = MibTableColumn
vrPpIpPortBootpPIndex = _VrPpIpPortBootpPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 1, 1, 10),
    _VrPpIpPortBootpPIndex_Type()
)
vrPpIpPortBootpPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpIpPortBootpPIndex.setStatus("mandatory")
_VrPpIpPortBootpPProvTable_Object = MibTable
vrPpIpPortBootpPProvTable = _VrPpIpPortBootpPProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 10)
)
if mibBuilder.loadTexts:
    vrPpIpPortBootpPProvTable.setStatus("mandatory")
_VrPpIpPortBootpPProvEntry_Object = MibTableRow
vrPpIpPortBootpPProvEntry = _VrPpIpPortBootpPProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 10, 1)
)
vrPpIpPortBootpPProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortBootpPIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortBootpPProvEntry.setStatus("mandatory")


class _VrPpIpPortBootpPRelayForwardStatus_Type(Integer32):
    """Custom type vrPpIpPortBootpPRelayForwardStatus based on Integer32"""
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


_VrPpIpPortBootpPRelayForwardStatus_Type.__name__ = "Integer32"
_VrPpIpPortBootpPRelayForwardStatus_Object = MibTableColumn
vrPpIpPortBootpPRelayForwardStatus = _VrPpIpPortBootpPRelayForwardStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 10, 1, 2),
    _VrPpIpPortBootpPRelayForwardStatus_Type()
)
vrPpIpPortBootpPRelayForwardStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortBootpPRelayForwardStatus.setStatus("mandatory")


class _VrPpIpPortBootpPBootpLogicalInterface_Type(IpAddress):
    """Custom type vrPpIpPortBootpPBootpLogicalInterface based on IpAddress"""
    defaultHexValue = "00000000"


_VrPpIpPortBootpPBootpLogicalInterface_Object = MibTableColumn
vrPpIpPortBootpPBootpLogicalInterface = _VrPpIpPortBootpPBootpLogicalInterface_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 10, 1, 3),
    _VrPpIpPortBootpPBootpLogicalInterface_Type()
)
vrPpIpPortBootpPBootpLogicalInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortBootpPBootpLogicalInterface.setStatus("mandatory")
_VrPpIpPortBootpPAdminControlTable_Object = MibTable
vrPpIpPortBootpPAdminControlTable = _VrPpIpPortBootpPAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 11)
)
if mibBuilder.loadTexts:
    vrPpIpPortBootpPAdminControlTable.setStatus("mandatory")
_VrPpIpPortBootpPAdminControlEntry_Object = MibTableRow
vrPpIpPortBootpPAdminControlEntry = _VrPpIpPortBootpPAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 11, 1)
)
vrPpIpPortBootpPAdminControlEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortBootpPIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortBootpPAdminControlEntry.setStatus("mandatory")


class _VrPpIpPortBootpPSnmpAdminStatus_Type(Integer32):
    """Custom type vrPpIpPortBootpPSnmpAdminStatus based on Integer32"""
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


_VrPpIpPortBootpPSnmpAdminStatus_Type.__name__ = "Integer32"
_VrPpIpPortBootpPSnmpAdminStatus_Object = MibTableColumn
vrPpIpPortBootpPSnmpAdminStatus = _VrPpIpPortBootpPSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 11, 1, 1),
    _VrPpIpPortBootpPSnmpAdminStatus_Type()
)
vrPpIpPortBootpPSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortBootpPSnmpAdminStatus.setStatus("mandatory")
_VrPpIpPortBootpPOperStatusTable_Object = MibTable
vrPpIpPortBootpPOperStatusTable = _VrPpIpPortBootpPOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 12)
)
if mibBuilder.loadTexts:
    vrPpIpPortBootpPOperStatusTable.setStatus("mandatory")
_VrPpIpPortBootpPOperStatusEntry_Object = MibTableRow
vrPpIpPortBootpPOperStatusEntry = _VrPpIpPortBootpPOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 12, 1)
)
vrPpIpPortBootpPOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortBootpPIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortBootpPOperStatusEntry.setStatus("mandatory")


class _VrPpIpPortBootpPSnmpOperStatus_Type(Integer32):
    """Custom type vrPpIpPortBootpPSnmpOperStatus based on Integer32"""
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


_VrPpIpPortBootpPSnmpOperStatus_Type.__name__ = "Integer32"
_VrPpIpPortBootpPSnmpOperStatus_Object = MibTableColumn
vrPpIpPortBootpPSnmpOperStatus = _VrPpIpPortBootpPSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 12, 1, 1),
    _VrPpIpPortBootpPSnmpOperStatus_Type()
)
vrPpIpPortBootpPSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortBootpPSnmpOperStatus.setStatus("mandatory")
_VrPpIpPortBootpPStateTable_Object = MibTable
vrPpIpPortBootpPStateTable = _VrPpIpPortBootpPStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 13)
)
if mibBuilder.loadTexts:
    vrPpIpPortBootpPStateTable.setStatus("mandatory")
_VrPpIpPortBootpPStateEntry_Object = MibTableRow
vrPpIpPortBootpPStateEntry = _VrPpIpPortBootpPStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 13, 1)
)
vrPpIpPortBootpPStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortBootpPIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortBootpPStateEntry.setStatus("mandatory")


class _VrPpIpPortBootpPAdminState_Type(Integer32):
    """Custom type vrPpIpPortBootpPAdminState based on Integer32"""
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


_VrPpIpPortBootpPAdminState_Type.__name__ = "Integer32"
_VrPpIpPortBootpPAdminState_Object = MibTableColumn
vrPpIpPortBootpPAdminState = _VrPpIpPortBootpPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 13, 1, 1),
    _VrPpIpPortBootpPAdminState_Type()
)
vrPpIpPortBootpPAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortBootpPAdminState.setStatus("mandatory")


class _VrPpIpPortBootpPOperationalState_Type(Integer32):
    """Custom type vrPpIpPortBootpPOperationalState based on Integer32"""
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


_VrPpIpPortBootpPOperationalState_Type.__name__ = "Integer32"
_VrPpIpPortBootpPOperationalState_Object = MibTableColumn
vrPpIpPortBootpPOperationalState = _VrPpIpPortBootpPOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 13, 1, 2),
    _VrPpIpPortBootpPOperationalState_Type()
)
vrPpIpPortBootpPOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortBootpPOperationalState.setStatus("mandatory")


class _VrPpIpPortBootpPUsageState_Type(Integer32):
    """Custom type vrPpIpPortBootpPUsageState based on Integer32"""
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


_VrPpIpPortBootpPUsageState_Type.__name__ = "Integer32"
_VrPpIpPortBootpPUsageState_Object = MibTableColumn
vrPpIpPortBootpPUsageState = _VrPpIpPortBootpPUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 13, 1, 3),
    _VrPpIpPortBootpPUsageState_Type()
)
vrPpIpPortBootpPUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortBootpPUsageState.setStatus("mandatory")
_VrPpIpPortBootpPStatsTable_Object = MibTable
vrPpIpPortBootpPStatsTable = _VrPpIpPortBootpPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 14)
)
if mibBuilder.loadTexts:
    vrPpIpPortBootpPStatsTable.setStatus("mandatory")
_VrPpIpPortBootpPStatsEntry_Object = MibTableRow
vrPpIpPortBootpPStatsEntry = _VrPpIpPortBootpPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 14, 1)
)
vrPpIpPortBootpPStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortBootpPIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortBootpPStatsEntry.setStatus("mandatory")
_VrPpIpPortBootpPInRequests_Type = Counter32
_VrPpIpPortBootpPInRequests_Object = MibTableColumn
vrPpIpPortBootpPInRequests = _VrPpIpPortBootpPInRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 14, 1, 1),
    _VrPpIpPortBootpPInRequests_Type()
)
vrPpIpPortBootpPInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortBootpPInRequests.setStatus("mandatory")
_VrPpIpPortBootpPInReplies_Type = Counter32
_VrPpIpPortBootpPInReplies_Object = MibTableColumn
vrPpIpPortBootpPInReplies = _VrPpIpPortBootpPInReplies_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 14, 1, 2),
    _VrPpIpPortBootpPInReplies_Type()
)
vrPpIpPortBootpPInReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortBootpPInReplies.setStatus("mandatory")
_VrPpIpPortBootpPOutRequests_Type = Counter32
_VrPpIpPortBootpPOutRequests_Object = MibTableColumn
vrPpIpPortBootpPOutRequests = _VrPpIpPortBootpPOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 14, 1, 3),
    _VrPpIpPortBootpPOutRequests_Type()
)
vrPpIpPortBootpPOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortBootpPOutRequests.setStatus("mandatory")
_VrPpIpPortBootpPOutReplies_Type = Counter32
_VrPpIpPortBootpPOutReplies_Object = MibTableColumn
vrPpIpPortBootpPOutReplies = _VrPpIpPortBootpPOutReplies_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 14, 1, 4),
    _VrPpIpPortBootpPOutReplies_Type()
)
vrPpIpPortBootpPOutReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortBootpPOutReplies.setStatus("mandatory")
_VrPpIpPortBootpPInRequestErrors_Type = Counter32
_VrPpIpPortBootpPInRequestErrors_Object = MibTableColumn
vrPpIpPortBootpPInRequestErrors = _VrPpIpPortBootpPInRequestErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 14, 1, 5),
    _VrPpIpPortBootpPInRequestErrors_Type()
)
vrPpIpPortBootpPInRequestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortBootpPInRequestErrors.setStatus("mandatory")
_VrPpIpPortBootpPInReplyErrors_Type = Counter32
_VrPpIpPortBootpPInReplyErrors_Object = MibTableColumn
vrPpIpPortBootpPInReplyErrors = _VrPpIpPortBootpPInReplyErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 14, 1, 6),
    _VrPpIpPortBootpPInReplyErrors_Type()
)
vrPpIpPortBootpPInReplyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortBootpPInReplyErrors.setStatus("mandatory")
_VrPpIpPortBootpPAddrTable_Object = MibTable
vrPpIpPortBootpPAddrTable = _VrPpIpPortBootpPAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 290)
)
if mibBuilder.loadTexts:
    vrPpIpPortBootpPAddrTable.setStatus("mandatory")
_VrPpIpPortBootpPAddrEntry_Object = MibTableRow
vrPpIpPortBootpPAddrEntry = _VrPpIpPortBootpPAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 290, 1)
)
vrPpIpPortBootpPAddrEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortBootpPIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortBootpPAddrValue"),
)
if mibBuilder.loadTexts:
    vrPpIpPortBootpPAddrEntry.setStatus("mandatory")
_VrPpIpPortBootpPAddrValue_Type = IpAddress
_VrPpIpPortBootpPAddrValue_Object = MibTableColumn
vrPpIpPortBootpPAddrValue = _VrPpIpPortBootpPAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 290, 1, 1),
    _VrPpIpPortBootpPAddrValue_Type()
)
vrPpIpPortBootpPAddrValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortBootpPAddrValue.setStatus("mandatory")
_VrPpIpPortBootpPAddrRowStatus_Type = RowStatus
_VrPpIpPortBootpPAddrRowStatus_Object = MibTableColumn
vrPpIpPortBootpPAddrRowStatus = _VrPpIpPortBootpPAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 4, 290, 1, 2),
    _VrPpIpPortBootpPAddrRowStatus_Type()
)
vrPpIpPortBootpPAddrRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vrPpIpPortBootpPAddrRowStatus.setStatus("mandatory")
_VrPpIpPortProvTable_Object = MibTable
vrPpIpPortProvTable = _VrPpIpPortProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 10)
)
if mibBuilder.loadTexts:
    vrPpIpPortProvTable.setStatus("mandatory")
_VrPpIpPortProvEntry_Object = MibTableRow
vrPpIpPortProvEntry = _VrPpIpPortProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 10, 1)
)
vrPpIpPortProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortProvEntry.setStatus("mandatory")


class _VrPpIpPortMaxTxUnit_Type(Unsigned32):
    """Custom type vrPpIpPortMaxTxUnit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 18944),
    )


_VrPpIpPortMaxTxUnit_Type.__name__ = "Unsigned32"
_VrPpIpPortMaxTxUnit_Object = MibTableColumn
vrPpIpPortMaxTxUnit = _VrPpIpPortMaxTxUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 10, 1, 2),
    _VrPpIpPortMaxTxUnit_Type()
)
vrPpIpPortMaxTxUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortMaxTxUnit.setStatus("mandatory")


class _VrPpIpPortArpStatus_Type(Integer32):
    """Custom type vrPpIpPortArpStatus based on Integer32"""
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


_VrPpIpPortArpStatus_Type.__name__ = "Integer32"
_VrPpIpPortArpStatus_Object = MibTableColumn
vrPpIpPortArpStatus = _VrPpIpPortArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 10, 1, 3),
    _VrPpIpPortArpStatus_Type()
)
vrPpIpPortArpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortArpStatus.setStatus("mandatory")


class _VrPpIpPortProxyArpStatus_Type(Integer32):
    """Custom type vrPpIpPortProxyArpStatus based on Integer32"""
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


_VrPpIpPortProxyArpStatus_Type.__name__ = "Integer32"
_VrPpIpPortProxyArpStatus_Object = MibTableColumn
vrPpIpPortProxyArpStatus = _VrPpIpPortProxyArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 10, 1, 4),
    _VrPpIpPortProxyArpStatus_Type()
)
vrPpIpPortProxyArpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortProxyArpStatus.setStatus("mandatory")


class _VrPpIpPortArpNoLearn_Type(Integer32):
    """Custom type vrPpIpPortArpNoLearn based on Integer32"""
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


_VrPpIpPortArpNoLearn_Type.__name__ = "Integer32"
_VrPpIpPortArpNoLearn_Object = MibTableColumn
vrPpIpPortArpNoLearn = _VrPpIpPortArpNoLearn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 10, 1, 5),
    _VrPpIpPortArpNoLearn_Type()
)
vrPpIpPortArpNoLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortArpNoLearn.setStatus("mandatory")


class _VrPpIpPortSendRedirect_Type(Integer32):
    """Custom type vrPpIpPortSendRedirect based on Integer32"""
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


_VrPpIpPortSendRedirect_Type.__name__ = "Integer32"
_VrPpIpPortSendRedirect_Object = MibTableColumn
vrPpIpPortSendRedirect = _VrPpIpPortSendRedirect_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 10, 1, 6),
    _VrPpIpPortSendRedirect_Type()
)
vrPpIpPortSendRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortSendRedirect.setStatus("mandatory")


class _VrPpIpPortMulticastStatus_Type(Integer32):
    """Custom type vrPpIpPortMulticastStatus based on Integer32"""
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


_VrPpIpPortMulticastStatus_Type.__name__ = "Integer32"
_VrPpIpPortMulticastStatus_Object = MibTableColumn
vrPpIpPortMulticastStatus = _VrPpIpPortMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 10, 1, 7),
    _VrPpIpPortMulticastStatus_Type()
)
vrPpIpPortMulticastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortMulticastStatus.setStatus("mandatory")


class _VrPpIpPortRelayAddress_Type(IpAddress):
    """Custom type vrPpIpPortRelayAddress based on IpAddress"""
    defaultHexValue = "00000000"


_VrPpIpPortRelayAddress_Object = MibTableColumn
vrPpIpPortRelayAddress = _VrPpIpPortRelayAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 10, 1, 8),
    _VrPpIpPortRelayAddress_Type()
)
vrPpIpPortRelayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortRelayAddress.setStatus("mandatory")


class _VrPpIpPortRelayBroadcast_Type(Integer32):
    """Custom type vrPpIpPortRelayBroadcast based on Integer32"""
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


_VrPpIpPortRelayBroadcast_Type.__name__ = "Integer32"
_VrPpIpPortRelayBroadcast_Object = MibTableColumn
vrPpIpPortRelayBroadcast = _VrPpIpPortRelayBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 10, 1, 9),
    _VrPpIpPortRelayBroadcast_Type()
)
vrPpIpPortRelayBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortRelayBroadcast.setStatus("mandatory")


class _VrPpIpPortLinkModel_Type(Integer32):
    """Custom type vrPpIpPortLinkModel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("localAreaNetwork", 1),
          ("loopback", 5),
          ("pointToPoint", 2))
    )


_VrPpIpPortLinkModel_Type.__name__ = "Integer32"
_VrPpIpPortLinkModel_Object = MibTableColumn
vrPpIpPortLinkModel = _VrPpIpPortLinkModel_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 10, 1, 10),
    _VrPpIpPortLinkModel_Type()
)
vrPpIpPortLinkModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLinkModel.setStatus("mandatory")


class _VrPpIpPortLanModel_Type(Integer32):
    """Custom type vrPpIpPortLanModel based on Integer32"""
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


_VrPpIpPortLanModel_Type.__name__ = "Integer32"
_VrPpIpPortLanModel_Object = MibTableColumn
vrPpIpPortLanModel = _VrPpIpPortLanModel_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 10, 1, 11),
    _VrPpIpPortLanModel_Type()
)
vrPpIpPortLanModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortLanModel.setStatus("mandatory")


class _VrPpIpPortEncap_Type(Integer32):
    """Custom type vrPpIpPortEncap based on Integer32"""
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


_VrPpIpPortEncap_Type.__name__ = "Integer32"
_VrPpIpPortEncap_Object = MibTableColumn
vrPpIpPortEncap = _VrPpIpPortEncap_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 10, 1, 12),
    _VrPpIpPortEncap_Type()
)
vrPpIpPortEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortEncap.setStatus("mandatory")


class _VrPpIpPortIcmpMaskReply_Type(Integer32):
    """Custom type vrPpIpPortIcmpMaskReply based on Integer32"""
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


_VrPpIpPortIcmpMaskReply_Type.__name__ = "Integer32"
_VrPpIpPortIcmpMaskReply_Object = MibTableColumn
vrPpIpPortIcmpMaskReply = _VrPpIpPortIcmpMaskReply_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 10, 1, 13),
    _VrPpIpPortIcmpMaskReply_Type()
)
vrPpIpPortIcmpMaskReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortIcmpMaskReply.setStatus("mandatory")


class _VrPpIpPortDirectedBroadcast_Type(Integer32):
    """Custom type vrPpIpPortDirectedBroadcast based on Integer32"""
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


_VrPpIpPortDirectedBroadcast_Type.__name__ = "Integer32"
_VrPpIpPortDirectedBroadcast_Object = MibTableColumn
vrPpIpPortDirectedBroadcast = _VrPpIpPortDirectedBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 10, 1, 14),
    _VrPpIpPortDirectedBroadcast_Type()
)
vrPpIpPortDirectedBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortDirectedBroadcast.setStatus("mandatory")


class _VrPpIpPortAssignedQos_Type(Unsigned32):
    """Custom type vrPpIpPortAssignedQos based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_VrPpIpPortAssignedQos_Type.__name__ = "Unsigned32"
_VrPpIpPortAssignedQos_Object = MibTableColumn
vrPpIpPortAssignedQos = _VrPpIpPortAssignedQos_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 10, 1, 15),
    _VrPpIpPortAssignedQos_Type()
)
vrPpIpPortAssignedQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortAssignedQos.setStatus("mandatory")


class _VrPpIpPortAllowMcastMacDest_Type(Integer32):
    """Custom type vrPpIpPortAllowMcastMacDest based on Integer32"""
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


_VrPpIpPortAllowMcastMacDest_Type.__name__ = "Integer32"
_VrPpIpPortAllowMcastMacDest_Object = MibTableColumn
vrPpIpPortAllowMcastMacDest = _VrPpIpPortAllowMcastMacDest_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 10, 1, 16),
    _VrPpIpPortAllowMcastMacDest_Type()
)
vrPpIpPortAllowMcastMacDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortAllowMcastMacDest.setStatus("mandatory")
_VrPpIpPortCosPolicyAssignment_Type = Link
_VrPpIpPortCosPolicyAssignment_Object = MibTableColumn
vrPpIpPortCosPolicyAssignment = _VrPpIpPortCosPolicyAssignment_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 10, 1, 17),
    _VrPpIpPortCosPolicyAssignment_Type()
)
vrPpIpPortCosPolicyAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortCosPolicyAssignment.setStatus("mandatory")


class _VrPpIpPortMcastDomain_Type(Unsigned32):
    """Custom type vrPpIpPortMcastDomain based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_VrPpIpPortMcastDomain_Type.__name__ = "Unsigned32"
_VrPpIpPortMcastDomain_Object = MibTableColumn
vrPpIpPortMcastDomain = _VrPpIpPortMcastDomain_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 10, 1, 18),
    _VrPpIpPortMcastDomain_Type()
)
vrPpIpPortMcastDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortMcastDomain.setStatus("mandatory")
_VrPpIpPortMcastPolicyAssignment_Type = Link
_VrPpIpPortMcastPolicyAssignment_Object = MibTableColumn
vrPpIpPortMcastPolicyAssignment = _VrPpIpPortMcastPolicyAssignment_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 10, 1, 19),
    _VrPpIpPortMcastPolicyAssignment_Type()
)
vrPpIpPortMcastPolicyAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortMcastPolicyAssignment.setStatus("mandatory")
_VrPpIpPortSresProvTable_Object = MibTable
vrPpIpPortSresProvTable = _VrPpIpPortSresProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 11)
)
if mibBuilder.loadTexts:
    vrPpIpPortSresProvTable.setStatus("mandatory")
_VrPpIpPortSresProvEntry_Object = MibTableRow
vrPpIpPortSresProvEntry = _VrPpIpPortSresProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 11, 1)
)
vrPpIpPortSresProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortSresProvEntry.setStatus("mandatory")


class _VrPpIpPortSourceRouteEndStationSupport_Type(Integer32):
    """Custom type vrPpIpPortSourceRouteEndStationSupport based on Integer32"""
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


_VrPpIpPortSourceRouteEndStationSupport_Type.__name__ = "Integer32"
_VrPpIpPortSourceRouteEndStationSupport_Object = MibTableColumn
vrPpIpPortSourceRouteEndStationSupport = _VrPpIpPortSourceRouteEndStationSupport_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 11, 1, 1),
    _VrPpIpPortSourceRouteEndStationSupport_Type()
)
vrPpIpPortSourceRouteEndStationSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortSourceRouteEndStationSupport.setStatus("mandatory")
_VrPpIpPortAdminControlTable_Object = MibTable
vrPpIpPortAdminControlTable = _VrPpIpPortAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 12)
)
if mibBuilder.loadTexts:
    vrPpIpPortAdminControlTable.setStatus("mandatory")
_VrPpIpPortAdminControlEntry_Object = MibTableRow
vrPpIpPortAdminControlEntry = _VrPpIpPortAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 12, 1)
)
vrPpIpPortAdminControlEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortAdminControlEntry.setStatus("mandatory")


class _VrPpIpPortSnmpAdminStatus_Type(Integer32):
    """Custom type vrPpIpPortSnmpAdminStatus based on Integer32"""
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


_VrPpIpPortSnmpAdminStatus_Type.__name__ = "Integer32"
_VrPpIpPortSnmpAdminStatus_Object = MibTableColumn
vrPpIpPortSnmpAdminStatus = _VrPpIpPortSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 12, 1, 1),
    _VrPpIpPortSnmpAdminStatus_Type()
)
vrPpIpPortSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpPortSnmpAdminStatus.setStatus("mandatory")
_VrPpIpPortOperTable_Object = MibTable
vrPpIpPortOperTable = _VrPpIpPortOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 13)
)
if mibBuilder.loadTexts:
    vrPpIpPortOperTable.setStatus("mandatory")
_VrPpIpPortOperEntry_Object = MibTableRow
vrPpIpPortOperEntry = _VrPpIpPortOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 13, 1)
)
vrPpIpPortOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortOperEntry.setStatus("mandatory")


class _VrPpIpPortMediaType_Type(Integer32):
    """Custom type vrPpIpPortMediaType based on Integer32"""
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


_VrPpIpPortMediaType_Type.__name__ = "Integer32"
_VrPpIpPortMediaType_Object = MibTableColumn
vrPpIpPortMediaType = _VrPpIpPortMediaType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 13, 1, 1),
    _VrPpIpPortMediaType_Type()
)
vrPpIpPortMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortMediaType.setStatus("mandatory")


class _VrPpIpPortOperMtu_Type(Unsigned32):
    """Custom type vrPpIpPortOperMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 18944),
    )


_VrPpIpPortOperMtu_Type.__name__ = "Unsigned32"
_VrPpIpPortOperMtu_Object = MibTableColumn
vrPpIpPortOperMtu = _VrPpIpPortOperMtu_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 13, 1, 2),
    _VrPpIpPortOperMtu_Type()
)
vrPpIpPortOperMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortOperMtu.setStatus("mandatory")


class _VrPpIpPortOperArpStatus_Type(Integer32):
    """Custom type vrPpIpPortOperArpStatus based on Integer32"""
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


_VrPpIpPortOperArpStatus_Type.__name__ = "Integer32"
_VrPpIpPortOperArpStatus_Object = MibTableColumn
vrPpIpPortOperArpStatus = _VrPpIpPortOperArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 13, 1, 3),
    _VrPpIpPortOperArpStatus_Type()
)
vrPpIpPortOperArpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortOperArpStatus.setStatus("mandatory")


class _VrPpIpPortOperMulticastStatus_Type(Integer32):
    """Custom type vrPpIpPortOperMulticastStatus based on Integer32"""
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


_VrPpIpPortOperMulticastStatus_Type.__name__ = "Integer32"
_VrPpIpPortOperMulticastStatus_Object = MibTableColumn
vrPpIpPortOperMulticastStatus = _VrPpIpPortOperMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 13, 1, 4),
    _VrPpIpPortOperMulticastStatus_Type()
)
vrPpIpPortOperMulticastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortOperMulticastStatus.setStatus("mandatory")


class _VrPpIpPortOperEncap_Type(Integer32):
    """Custom type vrPpIpPortOperEncap based on Integer32"""
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


_VrPpIpPortOperEncap_Type.__name__ = "Integer32"
_VrPpIpPortOperEncap_Object = MibTableColumn
vrPpIpPortOperEncap = _VrPpIpPortOperEncap_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 13, 1, 5),
    _VrPpIpPortOperEncap_Type()
)
vrPpIpPortOperEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortOperEncap.setStatus("mandatory")
_VrPpIpPortOperCosPolicyAssignment_Type = RowPointer
_VrPpIpPortOperCosPolicyAssignment_Object = MibTableColumn
vrPpIpPortOperCosPolicyAssignment = _VrPpIpPortOperCosPolicyAssignment_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 13, 1, 433),
    _VrPpIpPortOperCosPolicyAssignment_Type()
)
vrPpIpPortOperCosPolicyAssignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortOperCosPolicyAssignment.setStatus("mandatory")
_VrPpIpPortRelayBcOperTable_Object = MibTable
vrPpIpPortRelayBcOperTable = _VrPpIpPortRelayBcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 14)
)
if mibBuilder.loadTexts:
    vrPpIpPortRelayBcOperTable.setStatus("mandatory")
_VrPpIpPortRelayBcOperEntry_Object = MibTableRow
vrPpIpPortRelayBcOperEntry = _VrPpIpPortRelayBcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 14, 1)
)
vrPpIpPortRelayBcOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortRelayBcOperEntry.setStatus("mandatory")
_VrPpIpPortRelayAddressCount_Type = Counter32
_VrPpIpPortRelayAddressCount_Object = MibTableColumn
vrPpIpPortRelayAddressCount = _VrPpIpPortRelayAddressCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 14, 1, 1),
    _VrPpIpPortRelayAddressCount_Type()
)
vrPpIpPortRelayAddressCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortRelayAddressCount.setStatus("mandatory")
_VrPpIpPortRelayBcCount_Type = Counter32
_VrPpIpPortRelayBcCount_Object = MibTableColumn
vrPpIpPortRelayBcCount = _VrPpIpPortRelayBcCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 14, 1, 2),
    _VrPpIpPortRelayBcCount_Type()
)
vrPpIpPortRelayBcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortRelayBcCount.setStatus("mandatory")
_VrPpIpPortStateTable_Object = MibTable
vrPpIpPortStateTable = _VrPpIpPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 15)
)
if mibBuilder.loadTexts:
    vrPpIpPortStateTable.setStatus("mandatory")
_VrPpIpPortStateEntry_Object = MibTableRow
vrPpIpPortStateEntry = _VrPpIpPortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 15, 1)
)
vrPpIpPortStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortStateEntry.setStatus("mandatory")


class _VrPpIpPortAdminState_Type(Integer32):
    """Custom type vrPpIpPortAdminState based on Integer32"""
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


_VrPpIpPortAdminState_Type.__name__ = "Integer32"
_VrPpIpPortAdminState_Object = MibTableColumn
vrPpIpPortAdminState = _VrPpIpPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 15, 1, 1),
    _VrPpIpPortAdminState_Type()
)
vrPpIpPortAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortAdminState.setStatus("mandatory")


class _VrPpIpPortOperationalState_Type(Integer32):
    """Custom type vrPpIpPortOperationalState based on Integer32"""
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


_VrPpIpPortOperationalState_Type.__name__ = "Integer32"
_VrPpIpPortOperationalState_Object = MibTableColumn
vrPpIpPortOperationalState = _VrPpIpPortOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 15, 1, 2),
    _VrPpIpPortOperationalState_Type()
)
vrPpIpPortOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortOperationalState.setStatus("mandatory")


class _VrPpIpPortUsageState_Type(Integer32):
    """Custom type vrPpIpPortUsageState based on Integer32"""
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


_VrPpIpPortUsageState_Type.__name__ = "Integer32"
_VrPpIpPortUsageState_Object = MibTableColumn
vrPpIpPortUsageState = _VrPpIpPortUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 15, 1, 3),
    _VrPpIpPortUsageState_Type()
)
vrPpIpPortUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortUsageState.setStatus("mandatory")
_VrPpIpPortOperStatusTable_Object = MibTable
vrPpIpPortOperStatusTable = _VrPpIpPortOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 16)
)
if mibBuilder.loadTexts:
    vrPpIpPortOperStatusTable.setStatus("mandatory")
_VrPpIpPortOperStatusEntry_Object = MibTableRow
vrPpIpPortOperStatusEntry = _VrPpIpPortOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 16, 1)
)
vrPpIpPortOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrPpIpPortIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpPortOperStatusEntry.setStatus("mandatory")


class _VrPpIpPortSnmpOperStatus_Type(Integer32):
    """Custom type vrPpIpPortSnmpOperStatus based on Integer32"""
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


_VrPpIpPortSnmpOperStatus_Type.__name__ = "Integer32"
_VrPpIpPortSnmpOperStatus_Object = MibTableColumn
vrPpIpPortSnmpOperStatus = _VrPpIpPortSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 5, 16, 1, 1),
    _VrPpIpPortSnmpOperStatus_Type()
)
vrPpIpPortSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpPortSnmpOperStatus.setStatus("mandatory")
_VrIp_ObjectIdentity = ObjectIdentity
vrIp = _VrIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6)
)
_VrIpRowStatusTable_Object = MibTable
vrIpRowStatusTable = _VrIpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 1)
)
if mibBuilder.loadTexts:
    vrIpRowStatusTable.setStatus("mandatory")
_VrIpRowStatusEntry_Object = MibTableRow
vrIpRowStatusEntry = _VrIpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 1, 1)
)
vrIpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
)
if mibBuilder.loadTexts:
    vrIpRowStatusEntry.setStatus("mandatory")
_VrIpRowStatus_Type = RowStatus
_VrIpRowStatus_Object = MibTableColumn
vrIpRowStatus = _VrIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 1, 1, 1),
    _VrIpRowStatus_Type()
)
vrIpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRowStatus.setStatus("mandatory")
_VrIpComponentName_Type = DisplayString
_VrIpComponentName_Object = MibTableColumn
vrIpComponentName = _VrIpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 1, 1, 2),
    _VrIpComponentName_Type()
)
vrIpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpComponentName.setStatus("mandatory")
_VrIpStorageType_Type = StorageType
_VrIpStorageType_Object = MibTableColumn
vrIpStorageType = _VrIpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 1, 1, 4),
    _VrIpStorageType_Type()
)
vrIpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpStorageType.setStatus("mandatory")
_VrIpIndex_Type = NonReplicated
_VrIpIndex_Object = MibTableColumn
vrIpIndex = _VrIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 1, 1, 10),
    _VrIpIndex_Type()
)
vrIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpIndex.setStatus("mandatory")
_VrIpFwd_ObjectIdentity = ObjectIdentity
vrIpFwd = _VrIpFwd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 3)
)
_VrIpFwdRowStatusTable_Object = MibTable
vrIpFwdRowStatusTable = _VrIpFwdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 3, 1)
)
if mibBuilder.loadTexts:
    vrIpFwdRowStatusTable.setStatus("mandatory")
_VrIpFwdRowStatusEntry_Object = MibTableRow
vrIpFwdRowStatusEntry = _VrIpFwdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 3, 1, 1)
)
vrIpFwdRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpFwdDestAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpFwdDestMaskIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpFwdTypeOfServiceIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpFwdGatewayIndex"),
)
if mibBuilder.loadTexts:
    vrIpFwdRowStatusEntry.setStatus("mandatory")
_VrIpFwdRowStatus_Type = RowStatus
_VrIpFwdRowStatus_Object = MibTableColumn
vrIpFwdRowStatus = _VrIpFwdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 3, 1, 1, 1),
    _VrIpFwdRowStatus_Type()
)
vrIpFwdRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpFwdRowStatus.setStatus("mandatory")
_VrIpFwdComponentName_Type = DisplayString
_VrIpFwdComponentName_Object = MibTableColumn
vrIpFwdComponentName = _VrIpFwdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 3, 1, 1, 2),
    _VrIpFwdComponentName_Type()
)
vrIpFwdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpFwdComponentName.setStatus("mandatory")
_VrIpFwdStorageType_Type = StorageType
_VrIpFwdStorageType_Object = MibTableColumn
vrIpFwdStorageType = _VrIpFwdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 3, 1, 1, 4),
    _VrIpFwdStorageType_Type()
)
vrIpFwdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpFwdStorageType.setStatus("mandatory")
_VrIpFwdDestAddressIndex_Type = IpAddress
_VrIpFwdDestAddressIndex_Object = MibTableColumn
vrIpFwdDestAddressIndex = _VrIpFwdDestAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 3, 1, 1, 10),
    _VrIpFwdDestAddressIndex_Type()
)
vrIpFwdDestAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpFwdDestAddressIndex.setStatus("mandatory")
_VrIpFwdDestMaskIndex_Type = IpAddress
_VrIpFwdDestMaskIndex_Object = MibTableColumn
vrIpFwdDestMaskIndex = _VrIpFwdDestMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 3, 1, 1, 11),
    _VrIpFwdDestMaskIndex_Type()
)
vrIpFwdDestMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpFwdDestMaskIndex.setStatus("mandatory")


class _VrIpFwdTypeOfServiceIndex_Type(Integer32):
    """Custom type vrIpFwdTypeOfServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_VrIpFwdTypeOfServiceIndex_Type.__name__ = "Integer32"
_VrIpFwdTypeOfServiceIndex_Object = MibTableColumn
vrIpFwdTypeOfServiceIndex = _VrIpFwdTypeOfServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 3, 1, 1, 12),
    _VrIpFwdTypeOfServiceIndex_Type()
)
vrIpFwdTypeOfServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpFwdTypeOfServiceIndex.setStatus("mandatory")
_VrIpFwdGatewayIndex_Type = IpAddress
_VrIpFwdGatewayIndex_Object = MibTableColumn
vrIpFwdGatewayIndex = _VrIpFwdGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 3, 1, 1, 13),
    _VrIpFwdGatewayIndex_Type()
)
vrIpFwdGatewayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpFwdGatewayIndex.setStatus("mandatory")
_VrIpFwdOperTable_Object = MibTable
vrIpFwdOperTable = _VrIpFwdOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 3, 10)
)
if mibBuilder.loadTexts:
    vrIpFwdOperTable.setStatus("mandatory")
_VrIpFwdOperEntry_Object = MibTableRow
vrIpFwdOperEntry = _VrIpFwdOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 3, 10, 1)
)
vrIpFwdOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpFwdDestAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpFwdDestMaskIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpFwdTypeOfServiceIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpFwdGatewayIndex"),
)
if mibBuilder.loadTexts:
    vrIpFwdOperEntry.setStatus("mandatory")


class _VrIpFwdIfIndex_Type(InterfaceIndex):
    """Custom type vrIpFwdIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrIpFwdIfIndex_Type.__name__ = "InterfaceIndex"
_VrIpFwdIfIndex_Object = MibTableColumn
vrIpFwdIfIndex = _VrIpFwdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 3, 10, 1, 1),
    _VrIpFwdIfIndex_Type()
)
vrIpFwdIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpFwdIfIndex.setStatus("mandatory")


class _VrIpFwdType_Type(Integer32):
    """Custom type vrIpFwdType based on Integer32"""
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


_VrIpFwdType_Type.__name__ = "Integer32"
_VrIpFwdType_Object = MibTableColumn
vrIpFwdType = _VrIpFwdType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 3, 10, 1, 2),
    _VrIpFwdType_Type()
)
vrIpFwdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpFwdType.setStatus("mandatory")


class _VrIpFwdProtocol_Type(Integer32):
    """Custom type vrIpFwdProtocol based on Integer32"""
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
              15)
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
          ("netmgmt", 3),
          ("ospf", 13),
          ("other", 1),
          ("rip", 8))
    )


_VrIpFwdProtocol_Type.__name__ = "Integer32"
_VrIpFwdProtocol_Object = MibTableColumn
vrIpFwdProtocol = _VrIpFwdProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 3, 10, 1, 3),
    _VrIpFwdProtocol_Type()
)
vrIpFwdProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpFwdProtocol.setStatus("mandatory")


class _VrIpFwdAge_Type(Gauge32):
    """Custom type vrIpFwdAge based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpFwdAge_Type.__name__ = "Gauge32"
_VrIpFwdAge_Object = MibTableColumn
vrIpFwdAge = _VrIpFwdAge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 3, 10, 1, 4),
    _VrIpFwdAge_Type()
)
vrIpFwdAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpFwdAge.setStatus("mandatory")
_VrIpFwdProtocolPortName_Type = RowPointer
_VrIpFwdProtocolPortName_Object = MibTableColumn
vrIpFwdProtocolPortName = _VrIpFwdProtocolPortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 3, 10, 1, 5),
    _VrIpFwdProtocolPortName_Type()
)
vrIpFwdProtocolPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpFwdProtocolPortName.setStatus("mandatory")


class _VrIpFwdNextHopAs_Type(Unsigned32):
    """Custom type vrIpFwdNextHopAs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429467295),
    )


_VrIpFwdNextHopAs_Type.__name__ = "Unsigned32"
_VrIpFwdNextHopAs_Object = MibTableColumn
vrIpFwdNextHopAs = _VrIpFwdNextHopAs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 3, 10, 1, 7),
    _VrIpFwdNextHopAs_Type()
)
vrIpFwdNextHopAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpFwdNextHopAs.setStatus("mandatory")


class _VrIpFwdMetric_Type(Integer32):
    """Custom type vrIpFwdMetric based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_VrIpFwdMetric_Type.__name__ = "Integer32"
_VrIpFwdMetric_Object = MibTableColumn
vrIpFwdMetric = _VrIpFwdMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 3, 10, 1, 8),
    _VrIpFwdMetric_Type()
)
vrIpFwdMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpFwdMetric.setStatus("mandatory")
_VrIpRdb_ObjectIdentity = ObjectIdentity
vrIpRdb = _VrIpRdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 4)
)
_VrIpRdbRowStatusTable_Object = MibTable
vrIpRdbRowStatusTable = _VrIpRdbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 4, 1)
)
if mibBuilder.loadTexts:
    vrIpRdbRowStatusTable.setStatus("mandatory")
_VrIpRdbRowStatusEntry_Object = MibTableRow
vrIpRdbRowStatusEntry = _VrIpRdbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 4, 1, 1)
)
vrIpRdbRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRdbDestAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRdbDestMaskIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRdbProtocolIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRdbGatewayIndex"),
)
if mibBuilder.loadTexts:
    vrIpRdbRowStatusEntry.setStatus("mandatory")
_VrIpRdbRowStatus_Type = RowStatus
_VrIpRdbRowStatus_Object = MibTableColumn
vrIpRdbRowStatus = _VrIpRdbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 4, 1, 1, 1),
    _VrIpRdbRowStatus_Type()
)
vrIpRdbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRdbRowStatus.setStatus("mandatory")
_VrIpRdbComponentName_Type = DisplayString
_VrIpRdbComponentName_Object = MibTableColumn
vrIpRdbComponentName = _VrIpRdbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 4, 1, 1, 2),
    _VrIpRdbComponentName_Type()
)
vrIpRdbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRdbComponentName.setStatus("mandatory")
_VrIpRdbStorageType_Type = StorageType
_VrIpRdbStorageType_Object = MibTableColumn
vrIpRdbStorageType = _VrIpRdbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 4, 1, 1, 4),
    _VrIpRdbStorageType_Type()
)
vrIpRdbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRdbStorageType.setStatus("mandatory")
_VrIpRdbDestAddressIndex_Type = IpAddress
_VrIpRdbDestAddressIndex_Object = MibTableColumn
vrIpRdbDestAddressIndex = _VrIpRdbDestAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 4, 1, 1, 10),
    _VrIpRdbDestAddressIndex_Type()
)
vrIpRdbDestAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpRdbDestAddressIndex.setStatus("mandatory")
_VrIpRdbDestMaskIndex_Type = IpAddress
_VrIpRdbDestMaskIndex_Object = MibTableColumn
vrIpRdbDestMaskIndex = _VrIpRdbDestMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 4, 1, 1, 11),
    _VrIpRdbDestMaskIndex_Type()
)
vrIpRdbDestMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpRdbDestMaskIndex.setStatus("mandatory")


class _VrIpRdbProtocolIndex_Type(Integer32):
    """Custom type vrIpRdbProtocolIndex based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("bgpAggrDiscard", 14),
          ("bgpExternal", 12),
          ("bgpInternal", 13),
          ("bogus", 1),
          ("egp", 11),
          ("local", 2),
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


_VrIpRdbProtocolIndex_Type.__name__ = "Integer32"
_VrIpRdbProtocolIndex_Object = MibTableColumn
vrIpRdbProtocolIndex = _VrIpRdbProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 4, 1, 1, 12),
    _VrIpRdbProtocolIndex_Type()
)
vrIpRdbProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpRdbProtocolIndex.setStatus("mandatory")
_VrIpRdbGatewayIndex_Type = IpAddress
_VrIpRdbGatewayIndex_Object = MibTableColumn
vrIpRdbGatewayIndex = _VrIpRdbGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 4, 1, 1, 13),
    _VrIpRdbGatewayIndex_Type()
)
vrIpRdbGatewayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpRdbGatewayIndex.setStatus("mandatory")
_VrIpRdbOperTable_Object = MibTable
vrIpRdbOperTable = _VrIpRdbOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 4, 10)
)
if mibBuilder.loadTexts:
    vrIpRdbOperTable.setStatus("mandatory")
_VrIpRdbOperEntry_Object = MibTableRow
vrIpRdbOperEntry = _VrIpRdbOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 4, 10, 1)
)
vrIpRdbOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRdbDestAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRdbDestMaskIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRdbProtocolIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRdbGatewayIndex"),
)
if mibBuilder.loadTexts:
    vrIpRdbOperEntry.setStatus("mandatory")


class _VrIpRdbMetric_Type(Integer32):
    """Custom type vrIpRdbMetric based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_VrIpRdbMetric_Type.__name__ = "Integer32"
_VrIpRdbMetric_Object = MibTableColumn
vrIpRdbMetric = _VrIpRdbMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 4, 10, 1, 1),
    _VrIpRdbMetric_Type()
)
vrIpRdbMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRdbMetric.setStatus("mandatory")


class _VrIpRdbPreference_Type(Unsigned32):
    """Custom type vrIpRdbPreference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrIpRdbPreference_Type.__name__ = "Unsigned32"
_VrIpRdbPreference_Object = MibTableColumn
vrIpRdbPreference = _VrIpRdbPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 4, 10, 1, 2),
    _VrIpRdbPreference_Type()
)
vrIpRdbPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRdbPreference.setStatus("mandatory")


class _VrIpRdbAge_Type(Gauge32):
    """Custom type vrIpRdbAge based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpRdbAge_Type.__name__ = "Gauge32"
_VrIpRdbAge_Object = MibTableColumn
vrIpRdbAge = _VrIpRdbAge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 4, 10, 1, 3),
    _VrIpRdbAge_Type()
)
vrIpRdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRdbAge.setStatus("mandatory")
_VrIpIf_ObjectIdentity = ObjectIdentity
vrIpIf = _VrIpIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 5)
)
_VrIpIfRowStatusTable_Object = MibTable
vrIpIfRowStatusTable = _VrIpIfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 5, 1)
)
if mibBuilder.loadTexts:
    vrIpIfRowStatusTable.setStatus("mandatory")
_VrIpIfRowStatusEntry_Object = MibTableRow
vrIpIfRowStatusEntry = _VrIpIfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 5, 1, 1)
)
vrIpIfRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIfInterfaceAddressIndex"),
)
if mibBuilder.loadTexts:
    vrIpIfRowStatusEntry.setStatus("mandatory")
_VrIpIfRowStatus_Type = RowStatus
_VrIpIfRowStatus_Object = MibTableColumn
vrIpIfRowStatus = _VrIpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 5, 1, 1, 1),
    _VrIpIfRowStatus_Type()
)
vrIpIfRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIfRowStatus.setStatus("mandatory")
_VrIpIfComponentName_Type = DisplayString
_VrIpIfComponentName_Object = MibTableColumn
vrIpIfComponentName = _VrIpIfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 5, 1, 1, 2),
    _VrIpIfComponentName_Type()
)
vrIpIfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIfComponentName.setStatus("mandatory")
_VrIpIfStorageType_Type = StorageType
_VrIpIfStorageType_Object = MibTableColumn
vrIpIfStorageType = _VrIpIfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 5, 1, 1, 4),
    _VrIpIfStorageType_Type()
)
vrIpIfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIfStorageType.setStatus("mandatory")
_VrIpIfInterfaceAddressIndex_Type = IpAddress
_VrIpIfInterfaceAddressIndex_Object = MibTableColumn
vrIpIfInterfaceAddressIndex = _VrIpIfInterfaceAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 5, 1, 1, 10),
    _VrIpIfInterfaceAddressIndex_Type()
)
vrIpIfInterfaceAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpIfInterfaceAddressIndex.setStatus("mandatory")
_VrIpIfOperTable_Object = MibTable
vrIpIfOperTable = _VrIpIfOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 5, 10)
)
if mibBuilder.loadTexts:
    vrIpIfOperTable.setStatus("mandatory")
_VrIpIfOperEntry_Object = MibTableRow
vrIpIfOperEntry = _VrIpIfOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 5, 10, 1)
)
vrIpIfOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIfInterfaceAddressIndex"),
)
if mibBuilder.loadTexts:
    vrIpIfOperEntry.setStatus("mandatory")
_VrIpIfInterfaceMask_Type = IpAddress
_VrIpIfInterfaceMask_Object = MibTableColumn
vrIpIfInterfaceMask = _VrIpIfInterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 5, 10, 1, 1),
    _VrIpIfInterfaceMask_Type()
)
vrIpIfInterfaceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIfInterfaceMask.setStatus("mandatory")


class _VrIpIfStatus_Type(Integer32):
    """Custom type vrIpIfStatus based on Integer32"""
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


_VrIpIfStatus_Type.__name__ = "Integer32"
_VrIpIfStatus_Object = MibTableColumn
vrIpIfStatus = _VrIpIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 5, 10, 1, 2),
    _VrIpIfStatus_Type()
)
vrIpIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIfStatus.setStatus("mandatory")


class _VrIpIfPPName_Type(AsciiString):
    """Custom type vrIpIfPPName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 23),
    )


_VrIpIfPPName_Type.__name__ = "AsciiString"
_VrIpIfPPName_Object = MibTableColumn
vrIpIfPPName = _VrIpIfPPName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 5, 10, 1, 3),
    _VrIpIfPPName_Type()
)
vrIpIfPPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIfPPName.setStatus("mandatory")


class _VrIpIfMediaType_Type(Integer32):
    """Custom type vrIpIfMediaType based on Integer32"""
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


_VrIpIfMediaType_Type.__name__ = "Integer32"
_VrIpIfMediaType_Object = MibTableColumn
vrIpIfMediaType = _VrIpIfMediaType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 5, 10, 1, 4),
    _VrIpIfMediaType_Type()
)
vrIpIfMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIfMediaType.setStatus("mandatory")


class _VrIpIfHardwareAddress_Type(DashedHexString):
    """Custom type vrIpIfHardwareAddress based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_VrIpIfHardwareAddress_Type.__name__ = "DashedHexString"
_VrIpIfHardwareAddress_Object = MibTableColumn
vrIpIfHardwareAddress = _VrIpIfHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 5, 10, 1, 5),
    _VrIpIfHardwareAddress_Type()
)
vrIpIfHardwareAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIfHardwareAddress.setStatus("mandatory")


class _VrIpIfMtu_Type(Unsigned32):
    """Custom type vrIpIfMtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 18944),
    )


_VrIpIfMtu_Type.__name__ = "Unsigned32"
_VrIpIfMtu_Object = MibTableColumn
vrIpIfMtu = _VrIpIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 5, 10, 1, 6),
    _VrIpIfMtu_Type()
)
vrIpIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIfMtu.setStatus("mandatory")
_VrIpIfBroadcastAddress_Type = IpAddress
_VrIpIfBroadcastAddress_Object = MibTableColumn
vrIpIfBroadcastAddress = _VrIpIfBroadcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 5, 10, 1, 7),
    _VrIpIfBroadcastAddress_Type()
)
vrIpIfBroadcastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIfBroadcastAddress.setStatus("mandatory")


class _VrIpIfNcHardwareAddress_Type(DashedHexString):
    """Custom type vrIpIfNcHardwareAddress based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_VrIpIfNcHardwareAddress_Type.__name__ = "DashedHexString"
_VrIpIfNcHardwareAddress_Object = MibTableColumn
vrIpIfNcHardwareAddress = _VrIpIfNcHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 5, 10, 1, 8),
    _VrIpIfNcHardwareAddress_Type()
)
vrIpIfNcHardwareAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIfNcHardwareAddress.setStatus("mandatory")
_VrIpEgp_ObjectIdentity = ObjectIdentity
vrIpEgp = _VrIpEgp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6)
)
_VrIpEgpRowStatusTable_Object = MibTable
vrIpEgpRowStatusTable = _VrIpEgpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 1)
)
if mibBuilder.loadTexts:
    vrIpEgpRowStatusTable.setStatus("mandatory")
_VrIpEgpRowStatusEntry_Object = MibTableRow
vrIpEgpRowStatusEntry = _VrIpEgpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 1, 1)
)
vrIpEgpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpIndex"),
)
if mibBuilder.loadTexts:
    vrIpEgpRowStatusEntry.setStatus("mandatory")
_VrIpEgpRowStatus_Type = RowStatus
_VrIpEgpRowStatus_Object = MibTableColumn
vrIpEgpRowStatus = _VrIpEgpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 1, 1, 1),
    _VrIpEgpRowStatus_Type()
)
vrIpEgpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpRowStatus.setStatus("mandatory")
_VrIpEgpComponentName_Type = DisplayString
_VrIpEgpComponentName_Object = MibTableColumn
vrIpEgpComponentName = _VrIpEgpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 1, 1, 2),
    _VrIpEgpComponentName_Type()
)
vrIpEgpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpComponentName.setStatus("mandatory")
_VrIpEgpStorageType_Type = StorageType
_VrIpEgpStorageType_Object = MibTableColumn
vrIpEgpStorageType = _VrIpEgpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 1, 1, 4),
    _VrIpEgpStorageType_Type()
)
vrIpEgpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpStorageType.setStatus("mandatory")
_VrIpEgpIndex_Type = NonReplicated
_VrIpEgpIndex_Object = MibTableColumn
vrIpEgpIndex = _VrIpEgpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 1, 1, 10),
    _VrIpEgpIndex_Type()
)
vrIpEgpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpEgpIndex.setStatus("mandatory")
_VrIpEgpNbr_ObjectIdentity = ObjectIdentity
vrIpEgpNbr = _VrIpEgpNbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2)
)
_VrIpEgpNbrRowStatusTable_Object = MibTable
vrIpEgpNbrRowStatusTable = _VrIpEgpNbrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpEgpNbrRowStatusTable.setStatus("mandatory")
_VrIpEgpNbrRowStatusEntry_Object = MibTableRow
vrIpEgpNbrRowStatusEntry = _VrIpEgpNbrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 1, 1)
)
vrIpEgpNbrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpNbrNeighborAddressIndex"),
)
if mibBuilder.loadTexts:
    vrIpEgpNbrRowStatusEntry.setStatus("mandatory")
_VrIpEgpNbrRowStatus_Type = RowStatus
_VrIpEgpNbrRowStatus_Object = MibTableColumn
vrIpEgpNbrRowStatus = _VrIpEgpNbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 1, 1, 1),
    _VrIpEgpNbrRowStatus_Type()
)
vrIpEgpNbrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpNbrRowStatus.setStatus("mandatory")
_VrIpEgpNbrComponentName_Type = DisplayString
_VrIpEgpNbrComponentName_Object = MibTableColumn
vrIpEgpNbrComponentName = _VrIpEgpNbrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 1, 1, 2),
    _VrIpEgpNbrComponentName_Type()
)
vrIpEgpNbrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpNbrComponentName.setStatus("mandatory")
_VrIpEgpNbrStorageType_Type = StorageType
_VrIpEgpNbrStorageType_Object = MibTableColumn
vrIpEgpNbrStorageType = _VrIpEgpNbrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 1, 1, 4),
    _VrIpEgpNbrStorageType_Type()
)
vrIpEgpNbrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpNbrStorageType.setStatus("mandatory")
_VrIpEgpNbrNeighborAddressIndex_Type = IpAddress
_VrIpEgpNbrNeighborAddressIndex_Object = MibTableColumn
vrIpEgpNbrNeighborAddressIndex = _VrIpEgpNbrNeighborAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 1, 1, 10),
    _VrIpEgpNbrNeighborAddressIndex_Type()
)
vrIpEgpNbrNeighborAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpEgpNbrNeighborAddressIndex.setStatus("mandatory")
_VrIpEgpNbrProvTable_Object = MibTable
vrIpEgpNbrProvTable = _VrIpEgpNbrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpEgpNbrProvTable.setStatus("mandatory")
_VrIpEgpNbrProvEntry_Object = MibTableRow
vrIpEgpNbrProvEntry = _VrIpEgpNbrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 10, 1)
)
vrIpEgpNbrProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpNbrNeighborAddressIndex"),
)
if mibBuilder.loadTexts:
    vrIpEgpNbrProvEntry.setStatus("mandatory")


class _VrIpEgpNbrAsId_Type(Unsigned32):
    """Custom type vrIpEgpNbrAsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrIpEgpNbrAsId_Type.__name__ = "Unsigned32"
_VrIpEgpNbrAsId_Object = MibTableColumn
vrIpEgpNbrAsId = _VrIpEgpNbrAsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 10, 1, 1),
    _VrIpEgpNbrAsId_Type()
)
vrIpEgpNbrAsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpNbrAsId.setStatus("mandatory")


class _VrIpEgpNbrMode_Type(Integer32):
    """Custom type vrIpEgpNbrMode based on Integer32"""
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


_VrIpEgpNbrMode_Type.__name__ = "Integer32"
_VrIpEgpNbrMode_Object = MibTableColumn
vrIpEgpNbrMode = _VrIpEgpNbrMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 10, 1, 2),
    _VrIpEgpNbrMode_Type()
)
vrIpEgpNbrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpNbrMode.setStatus("mandatory")


class _VrIpEgpNbrGenerateDefaultRoute_Type(Integer32):
    """Custom type vrIpEgpNbrGenerateDefaultRoute based on Integer32"""
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


_VrIpEgpNbrGenerateDefaultRoute_Type.__name__ = "Integer32"
_VrIpEgpNbrGenerateDefaultRoute_Object = MibTableColumn
vrIpEgpNbrGenerateDefaultRoute = _VrIpEgpNbrGenerateDefaultRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 10, 1, 3),
    _VrIpEgpNbrGenerateDefaultRoute_Type()
)
vrIpEgpNbrGenerateDefaultRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpNbrGenerateDefaultRoute.setStatus("mandatory")


class _VrIpEgpNbrDefaultRouteMetric_Type(Unsigned32):
    """Custom type vrIpEgpNbrDefaultRouteMetric based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrIpEgpNbrDefaultRouteMetric_Type.__name__ = "Unsigned32"
_VrIpEgpNbrDefaultRouteMetric_Object = MibTableColumn
vrIpEgpNbrDefaultRouteMetric = _VrIpEgpNbrDefaultRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 10, 1, 4),
    _VrIpEgpNbrDefaultRouteMetric_Type()
)
vrIpEgpNbrDefaultRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpNbrDefaultRouteMetric.setStatus("mandatory")


class _VrIpEgpNbrDefaultMetric_Type(Unsigned32):
    """Custom type vrIpEgpNbrDefaultMetric based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrIpEgpNbrDefaultMetric_Type.__name__ = "Unsigned32"
_VrIpEgpNbrDefaultMetric_Object = MibTableColumn
vrIpEgpNbrDefaultMetric = _VrIpEgpNbrDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 10, 1, 5),
    _VrIpEgpNbrDefaultMetric_Type()
)
vrIpEgpNbrDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpNbrDefaultMetric.setStatus("mandatory")


class _VrIpEgpNbrHelloInterval_Type(Unsigned32):
    """Custom type vrIpEgpNbrHelloInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 120),
    )


_VrIpEgpNbrHelloInterval_Type.__name__ = "Unsigned32"
_VrIpEgpNbrHelloInterval_Object = MibTableColumn
vrIpEgpNbrHelloInterval = _VrIpEgpNbrHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 10, 1, 6),
    _VrIpEgpNbrHelloInterval_Type()
)
vrIpEgpNbrHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpNbrHelloInterval.setStatus("mandatory")


class _VrIpEgpNbrPollInterval_Type(Unsigned32):
    """Custom type vrIpEgpNbrPollInterval based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 480),
    )


_VrIpEgpNbrPollInterval_Type.__name__ = "Unsigned32"
_VrIpEgpNbrPollInterval_Object = MibTableColumn
vrIpEgpNbrPollInterval = _VrIpEgpNbrPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 10, 1, 7),
    _VrIpEgpNbrPollInterval_Type()
)
vrIpEgpNbrPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpNbrPollInterval.setStatus("mandatory")
_VrIpEgpNbrOperTable_Object = MibTable
vrIpEgpNbrOperTable = _VrIpEgpNbrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 11)
)
if mibBuilder.loadTexts:
    vrIpEgpNbrOperTable.setStatus("mandatory")
_VrIpEgpNbrOperEntry_Object = MibTableRow
vrIpEgpNbrOperEntry = _VrIpEgpNbrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 11, 1)
)
vrIpEgpNbrOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpNbrNeighborAddressIndex"),
)
if mibBuilder.loadTexts:
    vrIpEgpNbrOperEntry.setStatus("mandatory")


class _VrIpEgpNbrState_Type(Integer32):
    """Custom type vrIpEgpNbrState based on Integer32"""
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


_VrIpEgpNbrState_Type.__name__ = "Integer32"
_VrIpEgpNbrState_Object = MibTableColumn
vrIpEgpNbrState = _VrIpEgpNbrState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 11, 1, 1),
    _VrIpEgpNbrState_Type()
)
vrIpEgpNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpNbrState.setStatus("mandatory")
_VrIpEgpNbrInMsgs_Type = Counter32
_VrIpEgpNbrInMsgs_Object = MibTableColumn
vrIpEgpNbrInMsgs = _VrIpEgpNbrInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 11, 1, 2),
    _VrIpEgpNbrInMsgs_Type()
)
vrIpEgpNbrInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpNbrInMsgs.setStatus("mandatory")
_VrIpEgpNbrInErrors_Type = Counter32
_VrIpEgpNbrInErrors_Object = MibTableColumn
vrIpEgpNbrInErrors = _VrIpEgpNbrInErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 11, 1, 3),
    _VrIpEgpNbrInErrors_Type()
)
vrIpEgpNbrInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpNbrInErrors.setStatus("mandatory")
_VrIpEgpNbrOutMsgs_Type = Counter32
_VrIpEgpNbrOutMsgs_Object = MibTableColumn
vrIpEgpNbrOutMsgs = _VrIpEgpNbrOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 11, 1, 4),
    _VrIpEgpNbrOutMsgs_Type()
)
vrIpEgpNbrOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpNbrOutMsgs.setStatus("mandatory")
_VrIpEgpNbrOutErrors_Type = Counter32
_VrIpEgpNbrOutErrors_Object = MibTableColumn
vrIpEgpNbrOutErrors = _VrIpEgpNbrOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 11, 1, 5),
    _VrIpEgpNbrOutErrors_Type()
)
vrIpEgpNbrOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpNbrOutErrors.setStatus("mandatory")
_VrIpEgpNbrInErrorMsgs_Type = Counter32
_VrIpEgpNbrInErrorMsgs_Object = MibTableColumn
vrIpEgpNbrInErrorMsgs = _VrIpEgpNbrInErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 11, 1, 6),
    _VrIpEgpNbrInErrorMsgs_Type()
)
vrIpEgpNbrInErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpNbrInErrorMsgs.setStatus("mandatory")
_VrIpEgpNbrOutErrorMsgs_Type = Counter32
_VrIpEgpNbrOutErrorMsgs_Object = MibTableColumn
vrIpEgpNbrOutErrorMsgs = _VrIpEgpNbrOutErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 11, 1, 7),
    _VrIpEgpNbrOutErrorMsgs_Type()
)
vrIpEgpNbrOutErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpNbrOutErrorMsgs.setStatus("mandatory")
_VrIpEgpNbrStateUps_Type = Counter32
_VrIpEgpNbrStateUps_Object = MibTableColumn
vrIpEgpNbrStateUps = _VrIpEgpNbrStateUps_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 11, 1, 8),
    _VrIpEgpNbrStateUps_Type()
)
vrIpEgpNbrStateUps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpNbrStateUps.setStatus("mandatory")
_VrIpEgpNbrStateDowns_Type = Counter32
_VrIpEgpNbrStateDowns_Object = MibTableColumn
vrIpEgpNbrStateDowns = _VrIpEgpNbrStateDowns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 11, 1, 9),
    _VrIpEgpNbrStateDowns_Type()
)
vrIpEgpNbrStateDowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpNbrStateDowns.setStatus("mandatory")


class _VrIpEgpNbrEventTrigger_Type(Integer32):
    """Custom type vrIpEgpNbrEventTrigger based on Integer32"""
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


_VrIpEgpNbrEventTrigger_Type.__name__ = "Integer32"
_VrIpEgpNbrEventTrigger_Object = MibTableColumn
vrIpEgpNbrEventTrigger = _VrIpEgpNbrEventTrigger_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 2, 11, 1, 10),
    _VrIpEgpNbrEventTrigger_Type()
)
vrIpEgpNbrEventTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpNbrEventTrigger.setStatus("mandatory")
_VrIpEgpImport_ObjectIdentity = ObjectIdentity
vrIpEgpImport = _VrIpEgpImport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 3)
)
_VrIpEgpImportRowStatusTable_Object = MibTable
vrIpEgpImportRowStatusTable = _VrIpEgpImportRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 3, 1)
)
if mibBuilder.loadTexts:
    vrIpEgpImportRowStatusTable.setStatus("mandatory")
_VrIpEgpImportRowStatusEntry_Object = MibTableRow
vrIpEgpImportRowStatusEntry = _VrIpEgpImportRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 3, 1, 1)
)
vrIpEgpImportRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpImportIndex"),
)
if mibBuilder.loadTexts:
    vrIpEgpImportRowStatusEntry.setStatus("mandatory")
_VrIpEgpImportRowStatus_Type = RowStatus
_VrIpEgpImportRowStatus_Object = MibTableColumn
vrIpEgpImportRowStatus = _VrIpEgpImportRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 3, 1, 1, 1),
    _VrIpEgpImportRowStatus_Type()
)
vrIpEgpImportRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpImportRowStatus.setStatus("mandatory")
_VrIpEgpImportComponentName_Type = DisplayString
_VrIpEgpImportComponentName_Object = MibTableColumn
vrIpEgpImportComponentName = _VrIpEgpImportComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 3, 1, 1, 2),
    _VrIpEgpImportComponentName_Type()
)
vrIpEgpImportComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpImportComponentName.setStatus("mandatory")
_VrIpEgpImportStorageType_Type = StorageType
_VrIpEgpImportStorageType_Object = MibTableColumn
vrIpEgpImportStorageType = _VrIpEgpImportStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 3, 1, 1, 4),
    _VrIpEgpImportStorageType_Type()
)
vrIpEgpImportStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpImportStorageType.setStatus("mandatory")


class _VrIpEgpImportIndex_Type(Integer32):
    """Custom type vrIpEgpImportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpEgpImportIndex_Type.__name__ = "Integer32"
_VrIpEgpImportIndex_Object = MibTableColumn
vrIpEgpImportIndex = _VrIpEgpImportIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 3, 1, 1, 10),
    _VrIpEgpImportIndex_Type()
)
vrIpEgpImportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpEgpImportIndex.setStatus("mandatory")
_VrIpEgpImportNet_ObjectIdentity = ObjectIdentity
vrIpEgpImportNet = _VrIpEgpImportNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 3, 2)
)
_VrIpEgpImportNetRowStatusTable_Object = MibTable
vrIpEgpImportNetRowStatusTable = _VrIpEgpImportNetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 3, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpEgpImportNetRowStatusTable.setStatus("mandatory")
_VrIpEgpImportNetRowStatusEntry_Object = MibTableRow
vrIpEgpImportNetRowStatusEntry = _VrIpEgpImportNetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 3, 2, 1, 1)
)
vrIpEgpImportNetRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpImportIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpImportNetIndex"),
)
if mibBuilder.loadTexts:
    vrIpEgpImportNetRowStatusEntry.setStatus("mandatory")
_VrIpEgpImportNetRowStatus_Type = RowStatus
_VrIpEgpImportNetRowStatus_Object = MibTableColumn
vrIpEgpImportNetRowStatus = _VrIpEgpImportNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 3, 2, 1, 1, 1),
    _VrIpEgpImportNetRowStatus_Type()
)
vrIpEgpImportNetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpImportNetRowStatus.setStatus("mandatory")
_VrIpEgpImportNetComponentName_Type = DisplayString
_VrIpEgpImportNetComponentName_Object = MibTableColumn
vrIpEgpImportNetComponentName = _VrIpEgpImportNetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 3, 2, 1, 1, 2),
    _VrIpEgpImportNetComponentName_Type()
)
vrIpEgpImportNetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpImportNetComponentName.setStatus("mandatory")
_VrIpEgpImportNetStorageType_Type = StorageType
_VrIpEgpImportNetStorageType_Object = MibTableColumn
vrIpEgpImportNetStorageType = _VrIpEgpImportNetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 3, 2, 1, 1, 4),
    _VrIpEgpImportNetStorageType_Type()
)
vrIpEgpImportNetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpImportNetStorageType.setStatus("mandatory")


class _VrIpEgpImportNetIndex_Type(Integer32):
    """Custom type vrIpEgpImportNetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpEgpImportNetIndex_Type.__name__ = "Integer32"
_VrIpEgpImportNetIndex_Object = MibTableColumn
vrIpEgpImportNetIndex = _VrIpEgpImportNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 3, 2, 1, 1, 10),
    _VrIpEgpImportNetIndex_Type()
)
vrIpEgpImportNetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpEgpImportNetIndex.setStatus("mandatory")
_VrIpEgpImportNetProvTable_Object = MibTable
vrIpEgpImportNetProvTable = _VrIpEgpImportNetProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 3, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpEgpImportNetProvTable.setStatus("mandatory")
_VrIpEgpImportNetProvEntry_Object = MibTableRow
vrIpEgpImportNetProvEntry = _VrIpEgpImportNetProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 3, 2, 10, 1)
)
vrIpEgpImportNetProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpImportIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpImportNetIndex"),
)
if mibBuilder.loadTexts:
    vrIpEgpImportNetProvEntry.setStatus("mandatory")
_VrIpEgpImportNetIpAddress_Type = IpAddress
_VrIpEgpImportNetIpAddress_Object = MibTableColumn
vrIpEgpImportNetIpAddress = _VrIpEgpImportNetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 3, 2, 10, 1, 1),
    _VrIpEgpImportNetIpAddress_Type()
)
vrIpEgpImportNetIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpImportNetIpAddress.setStatus("mandatory")
_VrIpEgpImportProvTable_Object = MibTable
vrIpEgpImportProvTable = _VrIpEgpImportProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 3, 10)
)
if mibBuilder.loadTexts:
    vrIpEgpImportProvTable.setStatus("mandatory")
_VrIpEgpImportProvEntry_Object = MibTableRow
vrIpEgpImportProvEntry = _VrIpEgpImportProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 3, 10, 1)
)
vrIpEgpImportProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpImportIndex"),
)
if mibBuilder.loadTexts:
    vrIpEgpImportProvEntry.setStatus("mandatory")


class _VrIpEgpImportUsageFlag_Type(Integer32):
    """Custom type vrIpEgpImportUsageFlag based on Integer32"""
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


_VrIpEgpImportUsageFlag_Type.__name__ = "Integer32"
_VrIpEgpImportUsageFlag_Object = MibTableColumn
vrIpEgpImportUsageFlag = _VrIpEgpImportUsageFlag_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 3, 10, 1, 1),
    _VrIpEgpImportUsageFlag_Type()
)
vrIpEgpImportUsageFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpImportUsageFlag.setStatus("mandatory")


class _VrIpEgpImportImportMetric_Type(Unsigned32):
    """Custom type vrIpEgpImportImportMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrIpEgpImportImportMetric_Type.__name__ = "Unsigned32"
_VrIpEgpImportImportMetric_Object = MibTableColumn
vrIpEgpImportImportMetric = _VrIpEgpImportImportMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 3, 10, 1, 2),
    _VrIpEgpImportImportMetric_Type()
)
vrIpEgpImportImportMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpImportImportMetric.setStatus("mandatory")


class _VrIpEgpImportNbrAsId_Type(Unsigned32):
    """Custom type vrIpEgpImportNbrAsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpEgpImportNbrAsId_Type.__name__ = "Unsigned32"
_VrIpEgpImportNbrAsId_Object = MibTableColumn
vrIpEgpImportNbrAsId = _VrIpEgpImportNbrAsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 3, 10, 1, 3),
    _VrIpEgpImportNbrAsId_Type()
)
vrIpEgpImportNbrAsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpImportNbrAsId.setStatus("mandatory")
_VrIpEgpExport_ObjectIdentity = ObjectIdentity
vrIpEgpExport = _VrIpEgpExport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4)
)
_VrIpEgpExportRowStatusTable_Object = MibTable
vrIpEgpExportRowStatusTable = _VrIpEgpExportRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4, 1)
)
if mibBuilder.loadTexts:
    vrIpEgpExportRowStatusTable.setStatus("mandatory")
_VrIpEgpExportRowStatusEntry_Object = MibTableRow
vrIpEgpExportRowStatusEntry = _VrIpEgpExportRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4, 1, 1)
)
vrIpEgpExportRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpExportIndex"),
)
if mibBuilder.loadTexts:
    vrIpEgpExportRowStatusEntry.setStatus("mandatory")
_VrIpEgpExportRowStatus_Type = RowStatus
_VrIpEgpExportRowStatus_Object = MibTableColumn
vrIpEgpExportRowStatus = _VrIpEgpExportRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4, 1, 1, 1),
    _VrIpEgpExportRowStatus_Type()
)
vrIpEgpExportRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpExportRowStatus.setStatus("mandatory")
_VrIpEgpExportComponentName_Type = DisplayString
_VrIpEgpExportComponentName_Object = MibTableColumn
vrIpEgpExportComponentName = _VrIpEgpExportComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4, 1, 1, 2),
    _VrIpEgpExportComponentName_Type()
)
vrIpEgpExportComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpExportComponentName.setStatus("mandatory")
_VrIpEgpExportStorageType_Type = StorageType
_VrIpEgpExportStorageType_Object = MibTableColumn
vrIpEgpExportStorageType = _VrIpEgpExportStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4, 1, 1, 4),
    _VrIpEgpExportStorageType_Type()
)
vrIpEgpExportStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpExportStorageType.setStatus("mandatory")


class _VrIpEgpExportIndex_Type(Integer32):
    """Custom type vrIpEgpExportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpEgpExportIndex_Type.__name__ = "Integer32"
_VrIpEgpExportIndex_Object = MibTableColumn
vrIpEgpExportIndex = _VrIpEgpExportIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4, 1, 1, 10),
    _VrIpEgpExportIndex_Type()
)
vrIpEgpExportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpEgpExportIndex.setStatus("mandatory")
_VrIpEgpExportNet_ObjectIdentity = ObjectIdentity
vrIpEgpExportNet = _VrIpEgpExportNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4, 2)
)
_VrIpEgpExportNetRowStatusTable_Object = MibTable
vrIpEgpExportNetRowStatusTable = _VrIpEgpExportNetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpEgpExportNetRowStatusTable.setStatus("mandatory")
_VrIpEgpExportNetRowStatusEntry_Object = MibTableRow
vrIpEgpExportNetRowStatusEntry = _VrIpEgpExportNetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4, 2, 1, 1)
)
vrIpEgpExportNetRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpExportIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpExportNetIndex"),
)
if mibBuilder.loadTexts:
    vrIpEgpExportNetRowStatusEntry.setStatus("mandatory")
_VrIpEgpExportNetRowStatus_Type = RowStatus
_VrIpEgpExportNetRowStatus_Object = MibTableColumn
vrIpEgpExportNetRowStatus = _VrIpEgpExportNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4, 2, 1, 1, 1),
    _VrIpEgpExportNetRowStatus_Type()
)
vrIpEgpExportNetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpExportNetRowStatus.setStatus("mandatory")
_VrIpEgpExportNetComponentName_Type = DisplayString
_VrIpEgpExportNetComponentName_Object = MibTableColumn
vrIpEgpExportNetComponentName = _VrIpEgpExportNetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4, 2, 1, 1, 2),
    _VrIpEgpExportNetComponentName_Type()
)
vrIpEgpExportNetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpExportNetComponentName.setStatus("mandatory")
_VrIpEgpExportNetStorageType_Type = StorageType
_VrIpEgpExportNetStorageType_Object = MibTableColumn
vrIpEgpExportNetStorageType = _VrIpEgpExportNetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4, 2, 1, 1, 4),
    _VrIpEgpExportNetStorageType_Type()
)
vrIpEgpExportNetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpExportNetStorageType.setStatus("mandatory")


class _VrIpEgpExportNetIndex_Type(Integer32):
    """Custom type vrIpEgpExportNetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpEgpExportNetIndex_Type.__name__ = "Integer32"
_VrIpEgpExportNetIndex_Object = MibTableColumn
vrIpEgpExportNetIndex = _VrIpEgpExportNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4, 2, 1, 1, 10),
    _VrIpEgpExportNetIndex_Type()
)
vrIpEgpExportNetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpEgpExportNetIndex.setStatus("mandatory")
_VrIpEgpExportNetProvTable_Object = MibTable
vrIpEgpExportNetProvTable = _VrIpEgpExportNetProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpEgpExportNetProvTable.setStatus("mandatory")
_VrIpEgpExportNetProvEntry_Object = MibTableRow
vrIpEgpExportNetProvEntry = _VrIpEgpExportNetProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4, 2, 10, 1)
)
vrIpEgpExportNetProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpExportIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpExportNetIndex"),
)
if mibBuilder.loadTexts:
    vrIpEgpExportNetProvEntry.setStatus("mandatory")
_VrIpEgpExportNetIpAddress_Type = IpAddress
_VrIpEgpExportNetIpAddress_Object = MibTableColumn
vrIpEgpExportNetIpAddress = _VrIpEgpExportNetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4, 2, 10, 1, 1),
    _VrIpEgpExportNetIpAddress_Type()
)
vrIpEgpExportNetIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpExportNetIpAddress.setStatus("mandatory")
_VrIpEgpExportProvTable_Object = MibTable
vrIpEgpExportProvTable = _VrIpEgpExportProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4, 10)
)
if mibBuilder.loadTexts:
    vrIpEgpExportProvTable.setStatus("mandatory")
_VrIpEgpExportProvEntry_Object = MibTableRow
vrIpEgpExportProvEntry = _VrIpEgpExportProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4, 10, 1)
)
vrIpEgpExportProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpExportIndex"),
)
if mibBuilder.loadTexts:
    vrIpEgpExportProvEntry.setStatus("mandatory")


class _VrIpEgpExportAdvertiseStatus_Type(Integer32):
    """Custom type vrIpEgpExportAdvertiseStatus based on Integer32"""
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


_VrIpEgpExportAdvertiseStatus_Type.__name__ = "Integer32"
_VrIpEgpExportAdvertiseStatus_Object = MibTableColumn
vrIpEgpExportAdvertiseStatus = _VrIpEgpExportAdvertiseStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4, 10, 1, 1),
    _VrIpEgpExportAdvertiseStatus_Type()
)
vrIpEgpExportAdvertiseStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpExportAdvertiseStatus.setStatus("mandatory")


class _VrIpEgpExportExportMetric_Type(Unsigned32):
    """Custom type vrIpEgpExportExportMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrIpEgpExportExportMetric_Type.__name__ = "Unsigned32"
_VrIpEgpExportExportMetric_Object = MibTableColumn
vrIpEgpExportExportMetric = _VrIpEgpExportExportMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4, 10, 1, 2),
    _VrIpEgpExportExportMetric_Type()
)
vrIpEgpExportExportMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpExportExportMetric.setStatus("mandatory")


class _VrIpEgpExportProtocol_Type(Integer32):
    """Custom type vrIpEgpExportProtocol based on Integer32"""
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


_VrIpEgpExportProtocol_Type.__name__ = "Integer32"
_VrIpEgpExportProtocol_Object = MibTableColumn
vrIpEgpExportProtocol = _VrIpEgpExportProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4, 10, 1, 3),
    _VrIpEgpExportProtocol_Type()
)
vrIpEgpExportProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpExportProtocol.setStatus("mandatory")


class _VrIpEgpExportRipInterface_Type(IpAddress):
    """Custom type vrIpEgpExportRipInterface based on IpAddress"""
    defaultHexValue = "00000000"


_VrIpEgpExportRipInterface_Object = MibTableColumn
vrIpEgpExportRipInterface = _VrIpEgpExportRipInterface_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4, 10, 1, 4),
    _VrIpEgpExportRipInterface_Type()
)
vrIpEgpExportRipInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpExportRipInterface.setStatus("mandatory")


class _VrIpEgpExportRipNeighbor_Type(IpAddress):
    """Custom type vrIpEgpExportRipNeighbor based on IpAddress"""
    defaultHexValue = "00000000"


_VrIpEgpExportRipNeighbor_Object = MibTableColumn
vrIpEgpExportRipNeighbor = _VrIpEgpExportRipNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4, 10, 1, 5),
    _VrIpEgpExportRipNeighbor_Type()
)
vrIpEgpExportRipNeighbor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpExportRipNeighbor.setStatus("mandatory")


class _VrIpEgpExportInEgpAsId_Type(Unsigned32):
    """Custom type vrIpEgpExportInEgpAsId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpEgpExportInEgpAsId_Type.__name__ = "Unsigned32"
_VrIpEgpExportInEgpAsId_Object = MibTableColumn
vrIpEgpExportInEgpAsId = _VrIpEgpExportInEgpAsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4, 10, 1, 6),
    _VrIpEgpExportInEgpAsId_Type()
)
vrIpEgpExportInEgpAsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpExportInEgpAsId.setStatus("mandatory")


class _VrIpEgpExportOspfTag_Type(Unsigned32):
    """Custom type vrIpEgpExportOspfTag based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpEgpExportOspfTag_Type.__name__ = "Unsigned32"
_VrIpEgpExportOspfTag_Object = MibTableColumn
vrIpEgpExportOspfTag = _VrIpEgpExportOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4, 10, 1, 7),
    _VrIpEgpExportOspfTag_Type()
)
vrIpEgpExportOspfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpExportOspfTag.setStatus("mandatory")


class _VrIpEgpExportOutAutonomousSystem_Type(Unsigned32):
    """Custom type vrIpEgpExportOutAutonomousSystem based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpEgpExportOutAutonomousSystem_Type.__name__ = "Unsigned32"
_VrIpEgpExportOutAutonomousSystem_Object = MibTableColumn
vrIpEgpExportOutAutonomousSystem = _VrIpEgpExportOutAutonomousSystem_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 4, 10, 1, 8),
    _VrIpEgpExportOutAutonomousSystem_Type()
)
vrIpEgpExportOutAutonomousSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpExportOutAutonomousSystem.setStatus("mandatory")
_VrIpEgpProvTable_Object = MibTable
vrIpEgpProvTable = _VrIpEgpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 10)
)
if mibBuilder.loadTexts:
    vrIpEgpProvTable.setStatus("mandatory")
_VrIpEgpProvEntry_Object = MibTableRow
vrIpEgpProvEntry = _VrIpEgpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 10, 1)
)
vrIpEgpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpIndex"),
)
if mibBuilder.loadTexts:
    vrIpEgpProvEntry.setStatus("mandatory")


class _VrIpEgpAsId_Type(Unsigned32):
    """Custom type vrIpEgpAsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrIpEgpAsId_Type.__name__ = "Unsigned32"
_VrIpEgpAsId_Object = MibTableColumn
vrIpEgpAsId = _VrIpEgpAsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 10, 1, 2),
    _VrIpEgpAsId_Type()
)
vrIpEgpAsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpAsId.setStatus("mandatory")


class _VrIpEgpDefaultHelloInterval_Type(Unsigned32):
    """Custom type vrIpEgpDefaultHelloInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 900),
    )


_VrIpEgpDefaultHelloInterval_Type.__name__ = "Unsigned32"
_VrIpEgpDefaultHelloInterval_Object = MibTableColumn
vrIpEgpDefaultHelloInterval = _VrIpEgpDefaultHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 10, 1, 3),
    _VrIpEgpDefaultHelloInterval_Type()
)
vrIpEgpDefaultHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpDefaultHelloInterval.setStatus("mandatory")


class _VrIpEgpDefaultPollInterval_Type(Unsigned32):
    """Custom type vrIpEgpDefaultPollInterval based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 3600),
    )


_VrIpEgpDefaultPollInterval_Type.__name__ = "Unsigned32"
_VrIpEgpDefaultPollInterval_Object = MibTableColumn
vrIpEgpDefaultPollInterval = _VrIpEgpDefaultPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 10, 1, 4),
    _VrIpEgpDefaultPollInterval_Type()
)
vrIpEgpDefaultPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpDefaultPollInterval.setStatus("mandatory")


class _VrIpEgpMaxNatNets_Type(Unsigned32):
    """Custom type vrIpEgpMaxNatNets based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrIpEgpMaxNatNets_Type.__name__ = "Unsigned32"
_VrIpEgpMaxNatNets_Object = MibTableColumn
vrIpEgpMaxNatNets = _VrIpEgpMaxNatNets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 10, 1, 5),
    _VrIpEgpMaxNatNets_Type()
)
vrIpEgpMaxNatNets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpMaxNatNets.setStatus("mandatory")


class _VrIpEgpMaxBufferSize_Type(Unsigned32):
    """Custom type vrIpEgpMaxBufferSize based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 16),
    )


_VrIpEgpMaxBufferSize_Type.__name__ = "Unsigned32"
_VrIpEgpMaxBufferSize_Object = MibTableColumn
vrIpEgpMaxBufferSize = _VrIpEgpMaxBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 10, 1, 6),
    _VrIpEgpMaxBufferSize_Type()
)
vrIpEgpMaxBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpMaxBufferSize.setStatus("mandatory")
_VrIpEgpStatsTable_Object = MibTable
vrIpEgpStatsTable = _VrIpEgpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 11)
)
if mibBuilder.loadTexts:
    vrIpEgpStatsTable.setStatus("mandatory")
_VrIpEgpStatsEntry_Object = MibTableRow
vrIpEgpStatsEntry = _VrIpEgpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 11, 1)
)
vrIpEgpStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpIndex"),
)
if mibBuilder.loadTexts:
    vrIpEgpStatsEntry.setStatus("mandatory")
_VrIpEgpInMsgs_Type = Counter32
_VrIpEgpInMsgs_Object = MibTableColumn
vrIpEgpInMsgs = _VrIpEgpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 11, 1, 1),
    _VrIpEgpInMsgs_Type()
)
vrIpEgpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpInMsgs.setStatus("mandatory")
_VrIpEgpInErrorMsgs_Type = Counter32
_VrIpEgpInErrorMsgs_Object = MibTableColumn
vrIpEgpInErrorMsgs = _VrIpEgpInErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 11, 1, 2),
    _VrIpEgpInErrorMsgs_Type()
)
vrIpEgpInErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpInErrorMsgs.setStatus("mandatory")
_VrIpEgpOutErrorMsgs_Type = Counter32
_VrIpEgpOutErrorMsgs_Object = MibTableColumn
vrIpEgpOutErrorMsgs = _VrIpEgpOutErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 11, 1, 3),
    _VrIpEgpOutErrorMsgs_Type()
)
vrIpEgpOutErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpOutErrorMsgs.setStatus("mandatory")
_VrIpEgpInErrors_Type = Counter32
_VrIpEgpInErrors_Object = MibTableColumn
vrIpEgpInErrors = _VrIpEgpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 11, 1, 4),
    _VrIpEgpInErrors_Type()
)
vrIpEgpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpInErrors.setStatus("mandatory")
_VrIpEgpOutMsgs_Type = Counter32
_VrIpEgpOutMsgs_Object = MibTableColumn
vrIpEgpOutMsgs = _VrIpEgpOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 11, 1, 5),
    _VrIpEgpOutMsgs_Type()
)
vrIpEgpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpOutMsgs.setStatus("mandatory")
_VrIpEgpOutErrors_Type = Counter32
_VrIpEgpOutErrors_Object = MibTableColumn
vrIpEgpOutErrors = _VrIpEgpOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 11, 1, 6),
    _VrIpEgpOutErrors_Type()
)
vrIpEgpOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpOutErrors.setStatus("mandatory")
_VrIpEgpStateTable_Object = MibTable
vrIpEgpStateTable = _VrIpEgpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 12)
)
if mibBuilder.loadTexts:
    vrIpEgpStateTable.setStatus("mandatory")
_VrIpEgpStateEntry_Object = MibTableRow
vrIpEgpStateEntry = _VrIpEgpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 12, 1)
)
vrIpEgpStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpIndex"),
)
if mibBuilder.loadTexts:
    vrIpEgpStateEntry.setStatus("mandatory")


class _VrIpEgpAdminState_Type(Integer32):
    """Custom type vrIpEgpAdminState based on Integer32"""
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


_VrIpEgpAdminState_Type.__name__ = "Integer32"
_VrIpEgpAdminState_Object = MibTableColumn
vrIpEgpAdminState = _VrIpEgpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 12, 1, 1),
    _VrIpEgpAdminState_Type()
)
vrIpEgpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpAdminState.setStatus("mandatory")


class _VrIpEgpOperationalState_Type(Integer32):
    """Custom type vrIpEgpOperationalState based on Integer32"""
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


_VrIpEgpOperationalState_Type.__name__ = "Integer32"
_VrIpEgpOperationalState_Object = MibTableColumn
vrIpEgpOperationalState = _VrIpEgpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 12, 1, 2),
    _VrIpEgpOperationalState_Type()
)
vrIpEgpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpOperationalState.setStatus("mandatory")


class _VrIpEgpUsageState_Type(Integer32):
    """Custom type vrIpEgpUsageState based on Integer32"""
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


_VrIpEgpUsageState_Type.__name__ = "Integer32"
_VrIpEgpUsageState_Object = MibTableColumn
vrIpEgpUsageState = _VrIpEgpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 12, 1, 3),
    _VrIpEgpUsageState_Type()
)
vrIpEgpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpUsageState.setStatus("mandatory")
_VrIpEgpAdminControlTable_Object = MibTable
vrIpEgpAdminControlTable = _VrIpEgpAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 13)
)
if mibBuilder.loadTexts:
    vrIpEgpAdminControlTable.setStatus("mandatory")
_VrIpEgpAdminControlEntry_Object = MibTableRow
vrIpEgpAdminControlEntry = _VrIpEgpAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 13, 1)
)
vrIpEgpAdminControlEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpIndex"),
)
if mibBuilder.loadTexts:
    vrIpEgpAdminControlEntry.setStatus("mandatory")


class _VrIpEgpSnmpAdminStatus_Type(Integer32):
    """Custom type vrIpEgpSnmpAdminStatus based on Integer32"""
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


_VrIpEgpSnmpAdminStatus_Type.__name__ = "Integer32"
_VrIpEgpSnmpAdminStatus_Object = MibTableColumn
vrIpEgpSnmpAdminStatus = _VrIpEgpSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 13, 1, 1),
    _VrIpEgpSnmpAdminStatus_Type()
)
vrIpEgpSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpEgpSnmpAdminStatus.setStatus("mandatory")
_VrIpEgpOperStatusTable_Object = MibTable
vrIpEgpOperStatusTable = _VrIpEgpOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 16)
)
if mibBuilder.loadTexts:
    vrIpEgpOperStatusTable.setStatus("mandatory")
_VrIpEgpOperStatusEntry_Object = MibTableRow
vrIpEgpOperStatusEntry = _VrIpEgpOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 16, 1)
)
vrIpEgpOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpEgpIndex"),
)
if mibBuilder.loadTexts:
    vrIpEgpOperStatusEntry.setStatus("mandatory")


class _VrIpEgpSnmpOperStatus_Type(Integer32):
    """Custom type vrIpEgpSnmpOperStatus based on Integer32"""
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


_VrIpEgpSnmpOperStatus_Type.__name__ = "Integer32"
_VrIpEgpSnmpOperStatus_Object = MibTableColumn
vrIpEgpSnmpOperStatus = _VrIpEgpSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 6, 16, 1, 1),
    _VrIpEgpSnmpOperStatus_Type()
)
vrIpEgpSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpEgpSnmpOperStatus.setStatus("mandatory")
_VrIpOspf_ObjectIdentity = ObjectIdentity
vrIpOspf = _VrIpOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7)
)
_VrIpOspfRowStatusTable_Object = MibTable
vrIpOspfRowStatusTable = _VrIpOspfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 1)
)
if mibBuilder.loadTexts:
    vrIpOspfRowStatusTable.setStatus("mandatory")
_VrIpOspfRowStatusEntry_Object = MibTableRow
vrIpOspfRowStatusEntry = _VrIpOspfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 1, 1)
)
vrIpOspfRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfRowStatusEntry.setStatus("mandatory")
_VrIpOspfRowStatus_Type = RowStatus
_VrIpOspfRowStatus_Object = MibTableColumn
vrIpOspfRowStatus = _VrIpOspfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 1, 1, 1),
    _VrIpOspfRowStatus_Type()
)
vrIpOspfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfRowStatus.setStatus("mandatory")
_VrIpOspfComponentName_Type = DisplayString
_VrIpOspfComponentName_Object = MibTableColumn
vrIpOspfComponentName = _VrIpOspfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 1, 1, 2),
    _VrIpOspfComponentName_Type()
)
vrIpOspfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfComponentName.setStatus("mandatory")
_VrIpOspfStorageType_Type = StorageType
_VrIpOspfStorageType_Object = MibTableColumn
vrIpOspfStorageType = _VrIpOspfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 1, 1, 4),
    _VrIpOspfStorageType_Type()
)
vrIpOspfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfStorageType.setStatus("mandatory")
_VrIpOspfIndex_Type = NonReplicated
_VrIpOspfIndex_Object = MibTableColumn
vrIpOspfIndex = _VrIpOspfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 1, 1, 10),
    _VrIpOspfIndex_Type()
)
vrIpOspfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpOspfIndex.setStatus("mandatory")
_VrIpOspfArea_ObjectIdentity = ObjectIdentity
vrIpOspfArea = _VrIpOspfArea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 2)
)
_VrIpOspfAreaRowStatusTable_Object = MibTable
vrIpOspfAreaRowStatusTable = _VrIpOspfAreaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpOspfAreaRowStatusTable.setStatus("mandatory")
_VrIpOspfAreaRowStatusEntry_Object = MibTableRow
vrIpOspfAreaRowStatusEntry = _VrIpOspfAreaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 2, 1, 1)
)
vrIpOspfAreaRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfAreaAreaIdIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfAreaRowStatusEntry.setStatus("mandatory")
_VrIpOspfAreaRowStatus_Type = RowStatus
_VrIpOspfAreaRowStatus_Object = MibTableColumn
vrIpOspfAreaRowStatus = _VrIpOspfAreaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 2, 1, 1, 1),
    _VrIpOspfAreaRowStatus_Type()
)
vrIpOspfAreaRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfAreaRowStatus.setStatus("mandatory")
_VrIpOspfAreaComponentName_Type = DisplayString
_VrIpOspfAreaComponentName_Object = MibTableColumn
vrIpOspfAreaComponentName = _VrIpOspfAreaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 2, 1, 1, 2),
    _VrIpOspfAreaComponentName_Type()
)
vrIpOspfAreaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfAreaComponentName.setStatus("mandatory")
_VrIpOspfAreaStorageType_Type = StorageType
_VrIpOspfAreaStorageType_Object = MibTableColumn
vrIpOspfAreaStorageType = _VrIpOspfAreaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 2, 1, 1, 4),
    _VrIpOspfAreaStorageType_Type()
)
vrIpOspfAreaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfAreaStorageType.setStatus("mandatory")
_VrIpOspfAreaAreaIdIndex_Type = IpAddress
_VrIpOspfAreaAreaIdIndex_Object = MibTableColumn
vrIpOspfAreaAreaIdIndex = _VrIpOspfAreaAreaIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 2, 1, 1, 10),
    _VrIpOspfAreaAreaIdIndex_Type()
)
vrIpOspfAreaAreaIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpOspfAreaAreaIdIndex.setStatus("mandatory")
_VrIpOspfAreaProvTable_Object = MibTable
vrIpOspfAreaProvTable = _VrIpOspfAreaProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpOspfAreaProvTable.setStatus("mandatory")
_VrIpOspfAreaProvEntry_Object = MibTableRow
vrIpOspfAreaProvEntry = _VrIpOspfAreaProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 2, 10, 1)
)
vrIpOspfAreaProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfAreaAreaIdIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfAreaProvEntry.setStatus("mandatory")


class _VrIpOspfAreaAuthType_Type(Integer32):
    """Custom type vrIpOspfAreaAuthType based on Integer32"""
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


_VrIpOspfAreaAuthType_Type.__name__ = "Integer32"
_VrIpOspfAreaAuthType_Object = MibTableColumn
vrIpOspfAreaAuthType = _VrIpOspfAreaAuthType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 2, 10, 1, 1),
    _VrIpOspfAreaAuthType_Type()
)
vrIpOspfAreaAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfAreaAuthType.setStatus("mandatory")


class _VrIpOspfAreaImportAsExtern_Type(Integer32):
    """Custom type vrIpOspfAreaImportAsExtern based on Integer32"""
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


_VrIpOspfAreaImportAsExtern_Type.__name__ = "Integer32"
_VrIpOspfAreaImportAsExtern_Object = MibTableColumn
vrIpOspfAreaImportAsExtern = _VrIpOspfAreaImportAsExtern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 2, 10, 1, 2),
    _VrIpOspfAreaImportAsExtern_Type()
)
vrIpOspfAreaImportAsExtern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfAreaImportAsExtern.setStatus("mandatory")


class _VrIpOspfAreaAreaSummary_Type(Integer32):
    """Custom type vrIpOspfAreaAreaSummary based on Integer32"""
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


_VrIpOspfAreaAreaSummary_Type.__name__ = "Integer32"
_VrIpOspfAreaAreaSummary_Object = MibTableColumn
vrIpOspfAreaAreaSummary = _VrIpOspfAreaAreaSummary_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 2, 10, 1, 3),
    _VrIpOspfAreaAreaSummary_Type()
)
vrIpOspfAreaAreaSummary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfAreaAreaSummary.setStatus("mandatory")
_VrIpOspfAreaOperTable_Object = MibTable
vrIpOspfAreaOperTable = _VrIpOspfAreaOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 2, 11)
)
if mibBuilder.loadTexts:
    vrIpOspfAreaOperTable.setStatus("mandatory")
_VrIpOspfAreaOperEntry_Object = MibTableRow
vrIpOspfAreaOperEntry = _VrIpOspfAreaOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 2, 11, 1)
)
vrIpOspfAreaOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfAreaAreaIdIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfAreaOperEntry.setStatus("mandatory")
_VrIpOspfAreaSpfRuns_Type = Counter32
_VrIpOspfAreaSpfRuns_Object = MibTableColumn
vrIpOspfAreaSpfRuns = _VrIpOspfAreaSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 2, 11, 1, 1),
    _VrIpOspfAreaSpfRuns_Type()
)
vrIpOspfAreaSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfAreaSpfRuns.setStatus("mandatory")


class _VrIpOspfAreaAreaBdrRtrCount_Type(Gauge32):
    """Custom type vrIpOspfAreaAreaBdrRtrCount based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpOspfAreaAreaBdrRtrCount_Type.__name__ = "Gauge32"
_VrIpOspfAreaAreaBdrRtrCount_Object = MibTableColumn
vrIpOspfAreaAreaBdrRtrCount = _VrIpOspfAreaAreaBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 2, 11, 1, 2),
    _VrIpOspfAreaAreaBdrRtrCount_Type()
)
vrIpOspfAreaAreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfAreaAreaBdrRtrCount.setStatus("mandatory")


class _VrIpOspfAreaAsBdrRtrCount_Type(Gauge32):
    """Custom type vrIpOspfAreaAsBdrRtrCount based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpOspfAreaAsBdrRtrCount_Type.__name__ = "Gauge32"
_VrIpOspfAreaAsBdrRtrCount_Object = MibTableColumn
vrIpOspfAreaAsBdrRtrCount = _VrIpOspfAreaAsBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 2, 11, 1, 3),
    _VrIpOspfAreaAsBdrRtrCount_Type()
)
vrIpOspfAreaAsBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfAreaAsBdrRtrCount.setStatus("mandatory")


class _VrIpOspfAreaLsaCount_Type(Gauge32):
    """Custom type vrIpOspfAreaLsaCount based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpOspfAreaLsaCount_Type.__name__ = "Gauge32"
_VrIpOspfAreaLsaCount_Object = MibTableColumn
vrIpOspfAreaLsaCount = _VrIpOspfAreaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 2, 11, 1, 4),
    _VrIpOspfAreaLsaCount_Type()
)
vrIpOspfAreaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfAreaLsaCount.setStatus("mandatory")


class _VrIpOspfAreaAreaLsaCksumSum_Type(Unsigned32):
    """Custom type vrIpOspfAreaAreaLsaCksumSum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpOspfAreaAreaLsaCksumSum_Type.__name__ = "Unsigned32"
_VrIpOspfAreaAreaLsaCksumSum_Object = MibTableColumn
vrIpOspfAreaAreaLsaCksumSum = _VrIpOspfAreaAreaLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 2, 11, 1, 5),
    _VrIpOspfAreaAreaLsaCksumSum_Type()
)
vrIpOspfAreaAreaLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfAreaAreaLsaCksumSum.setStatus("mandatory")
_VrIpOspfStub_ObjectIdentity = ObjectIdentity
vrIpOspfStub = _VrIpOspfStub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 3)
)
_VrIpOspfStubRowStatusTable_Object = MibTable
vrIpOspfStubRowStatusTable = _VrIpOspfStubRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 3, 1)
)
if mibBuilder.loadTexts:
    vrIpOspfStubRowStatusTable.setStatus("mandatory")
_VrIpOspfStubRowStatusEntry_Object = MibTableRow
vrIpOspfStubRowStatusEntry = _VrIpOspfStubRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 3, 1, 1)
)
vrIpOspfStubRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfStubAreaIdIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfStubTosIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfStubRowStatusEntry.setStatus("mandatory")
_VrIpOspfStubRowStatus_Type = RowStatus
_VrIpOspfStubRowStatus_Object = MibTableColumn
vrIpOspfStubRowStatus = _VrIpOspfStubRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 3, 1, 1, 1),
    _VrIpOspfStubRowStatus_Type()
)
vrIpOspfStubRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfStubRowStatus.setStatus("mandatory")
_VrIpOspfStubComponentName_Type = DisplayString
_VrIpOspfStubComponentName_Object = MibTableColumn
vrIpOspfStubComponentName = _VrIpOspfStubComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 3, 1, 1, 2),
    _VrIpOspfStubComponentName_Type()
)
vrIpOspfStubComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfStubComponentName.setStatus("mandatory")
_VrIpOspfStubStorageType_Type = StorageType
_VrIpOspfStubStorageType_Object = MibTableColumn
vrIpOspfStubStorageType = _VrIpOspfStubStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 3, 1, 1, 4),
    _VrIpOspfStubStorageType_Type()
)
vrIpOspfStubStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfStubStorageType.setStatus("mandatory")
_VrIpOspfStubAreaIdIndex_Type = IpAddress
_VrIpOspfStubAreaIdIndex_Object = MibTableColumn
vrIpOspfStubAreaIdIndex = _VrIpOspfStubAreaIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 3, 1, 1, 10),
    _VrIpOspfStubAreaIdIndex_Type()
)
vrIpOspfStubAreaIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpOspfStubAreaIdIndex.setStatus("mandatory")


class _VrIpOspfStubTosIndex_Type(Integer32):
    """Custom type vrIpOspfStubTosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_VrIpOspfStubTosIndex_Type.__name__ = "Integer32"
_VrIpOspfStubTosIndex_Object = MibTableColumn
vrIpOspfStubTosIndex = _VrIpOspfStubTosIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 3, 1, 1, 11),
    _VrIpOspfStubTosIndex_Type()
)
vrIpOspfStubTosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpOspfStubTosIndex.setStatus("mandatory")
_VrIpOspfStubProvTable_Object = MibTable
vrIpOspfStubProvTable = _VrIpOspfStubProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 3, 10)
)
if mibBuilder.loadTexts:
    vrIpOspfStubProvTable.setStatus("mandatory")
_VrIpOspfStubProvEntry_Object = MibTableRow
vrIpOspfStubProvEntry = _VrIpOspfStubProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 3, 10, 1)
)
vrIpOspfStubProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfStubAreaIdIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfStubTosIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfStubProvEntry.setStatus("mandatory")


class _VrIpOspfStubMetric_Type(Unsigned32):
    """Custom type vrIpOspfStubMetric based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VrIpOspfStubMetric_Type.__name__ = "Unsigned32"
_VrIpOspfStubMetric_Object = MibTableColumn
vrIpOspfStubMetric = _VrIpOspfStubMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 3, 10, 1, 1),
    _VrIpOspfStubMetric_Type()
)
vrIpOspfStubMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfStubMetric.setStatus("mandatory")


class _VrIpOspfStubMetricType_Type(Integer32):
    """Custom type vrIpOspfStubMetricType based on Integer32"""
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


_VrIpOspfStubMetricType_Type.__name__ = "Integer32"
_VrIpOspfStubMetricType_Object = MibTableColumn
vrIpOspfStubMetricType = _VrIpOspfStubMetricType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 3, 10, 1, 2),
    _VrIpOspfStubMetricType_Type()
)
vrIpOspfStubMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfStubMetricType.setStatus("mandatory")


class _VrIpOspfStubAdvertiseDefault_Type(Integer32):
    """Custom type vrIpOspfStubAdvertiseDefault based on Integer32"""
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


_VrIpOspfStubAdvertiseDefault_Type.__name__ = "Integer32"
_VrIpOspfStubAdvertiseDefault_Object = MibTableColumn
vrIpOspfStubAdvertiseDefault = _VrIpOspfStubAdvertiseDefault_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 3, 10, 1, 3),
    _VrIpOspfStubAdvertiseDefault_Type()
)
vrIpOspfStubAdvertiseDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfStubAdvertiseDefault.setStatus("mandatory")
_VrIpOspfAggregate_ObjectIdentity = ObjectIdentity
vrIpOspfAggregate = _VrIpOspfAggregate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 5)
)
_VrIpOspfAggregateRowStatusTable_Object = MibTable
vrIpOspfAggregateRowStatusTable = _VrIpOspfAggregateRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 5, 1)
)
if mibBuilder.loadTexts:
    vrIpOspfAggregateRowStatusTable.setStatus("mandatory")
_VrIpOspfAggregateRowStatusEntry_Object = MibTableRow
vrIpOspfAggregateRowStatusEntry = _VrIpOspfAggregateRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 5, 1, 1)
)
vrIpOspfAggregateRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfAggregateAreaIdIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfAggregateLsdbTypeIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfAggregateAggregateNetIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfAggregateAggregateMaskIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfAggregateRowStatusEntry.setStatus("mandatory")
_VrIpOspfAggregateRowStatus_Type = RowStatus
_VrIpOspfAggregateRowStatus_Object = MibTableColumn
vrIpOspfAggregateRowStatus = _VrIpOspfAggregateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 5, 1, 1, 1),
    _VrIpOspfAggregateRowStatus_Type()
)
vrIpOspfAggregateRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfAggregateRowStatus.setStatus("mandatory")
_VrIpOspfAggregateComponentName_Type = DisplayString
_VrIpOspfAggregateComponentName_Object = MibTableColumn
vrIpOspfAggregateComponentName = _VrIpOspfAggregateComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 5, 1, 1, 2),
    _VrIpOspfAggregateComponentName_Type()
)
vrIpOspfAggregateComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfAggregateComponentName.setStatus("mandatory")
_VrIpOspfAggregateStorageType_Type = StorageType
_VrIpOspfAggregateStorageType_Object = MibTableColumn
vrIpOspfAggregateStorageType = _VrIpOspfAggregateStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 5, 1, 1, 4),
    _VrIpOspfAggregateStorageType_Type()
)
vrIpOspfAggregateStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfAggregateStorageType.setStatus("mandatory")
_VrIpOspfAggregateAreaIdIndex_Type = IpAddress
_VrIpOspfAggregateAreaIdIndex_Object = MibTableColumn
vrIpOspfAggregateAreaIdIndex = _VrIpOspfAggregateAreaIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 5, 1, 1, 10),
    _VrIpOspfAggregateAreaIdIndex_Type()
)
vrIpOspfAggregateAreaIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpOspfAggregateAreaIdIndex.setStatus("mandatory")


class _VrIpOspfAggregateLsdbTypeIndex_Type(Integer32):
    """Custom type vrIpOspfAggregateLsdbTypeIndex based on Integer32"""
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


_VrIpOspfAggregateLsdbTypeIndex_Type.__name__ = "Integer32"
_VrIpOspfAggregateLsdbTypeIndex_Object = MibTableColumn
vrIpOspfAggregateLsdbTypeIndex = _VrIpOspfAggregateLsdbTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 5, 1, 1, 11),
    _VrIpOspfAggregateLsdbTypeIndex_Type()
)
vrIpOspfAggregateLsdbTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpOspfAggregateLsdbTypeIndex.setStatus("mandatory")
_VrIpOspfAggregateAggregateNetIndex_Type = IpAddress
_VrIpOspfAggregateAggregateNetIndex_Object = MibTableColumn
vrIpOspfAggregateAggregateNetIndex = _VrIpOspfAggregateAggregateNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 5, 1, 1, 12),
    _VrIpOspfAggregateAggregateNetIndex_Type()
)
vrIpOspfAggregateAggregateNetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpOspfAggregateAggregateNetIndex.setStatus("mandatory")
_VrIpOspfAggregateAggregateMaskIndex_Type = IpAddress
_VrIpOspfAggregateAggregateMaskIndex_Object = MibTableColumn
vrIpOspfAggregateAggregateMaskIndex = _VrIpOspfAggregateAggregateMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 5, 1, 1, 13),
    _VrIpOspfAggregateAggregateMaskIndex_Type()
)
vrIpOspfAggregateAggregateMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpOspfAggregateAggregateMaskIndex.setStatus("mandatory")
_VrIpOspfAggregateProvTable_Object = MibTable
vrIpOspfAggregateProvTable = _VrIpOspfAggregateProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 5, 10)
)
if mibBuilder.loadTexts:
    vrIpOspfAggregateProvTable.setStatus("mandatory")
_VrIpOspfAggregateProvEntry_Object = MibTableRow
vrIpOspfAggregateProvEntry = _VrIpOspfAggregateProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 5, 10, 1)
)
vrIpOspfAggregateProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfAggregateAreaIdIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfAggregateLsdbTypeIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfAggregateAggregateNetIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfAggregateAggregateMaskIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfAggregateProvEntry.setStatus("mandatory")


class _VrIpOspfAggregateEffect_Type(Integer32):
    """Custom type vrIpOspfAggregateEffect based on Integer32"""
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


_VrIpOspfAggregateEffect_Type.__name__ = "Integer32"
_VrIpOspfAggregateEffect_Object = MibTableColumn
vrIpOspfAggregateEffect = _VrIpOspfAggregateEffect_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 5, 10, 1, 1),
    _VrIpOspfAggregateEffect_Type()
)
vrIpOspfAggregateEffect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfAggregateEffect.setStatus("mandatory")
_VrIpOspfHost_ObjectIdentity = ObjectIdentity
vrIpOspfHost = _VrIpOspfHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 6)
)
_VrIpOspfHostRowStatusTable_Object = MibTable
vrIpOspfHostRowStatusTable = _VrIpOspfHostRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 6, 1)
)
if mibBuilder.loadTexts:
    vrIpOspfHostRowStatusTable.setStatus("mandatory")
_VrIpOspfHostRowStatusEntry_Object = MibTableRow
vrIpOspfHostRowStatusEntry = _VrIpOspfHostRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 6, 1, 1)
)
vrIpOspfHostRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfHostAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfHostTosIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfHostRowStatusEntry.setStatus("mandatory")
_VrIpOspfHostRowStatus_Type = RowStatus
_VrIpOspfHostRowStatus_Object = MibTableColumn
vrIpOspfHostRowStatus = _VrIpOspfHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 6, 1, 1, 1),
    _VrIpOspfHostRowStatus_Type()
)
vrIpOspfHostRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfHostRowStatus.setStatus("mandatory")
_VrIpOspfHostComponentName_Type = DisplayString
_VrIpOspfHostComponentName_Object = MibTableColumn
vrIpOspfHostComponentName = _VrIpOspfHostComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 6, 1, 1, 2),
    _VrIpOspfHostComponentName_Type()
)
vrIpOspfHostComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfHostComponentName.setStatus("mandatory")
_VrIpOspfHostStorageType_Type = StorageType
_VrIpOspfHostStorageType_Object = MibTableColumn
vrIpOspfHostStorageType = _VrIpOspfHostStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 6, 1, 1, 4),
    _VrIpOspfHostStorageType_Type()
)
vrIpOspfHostStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfHostStorageType.setStatus("mandatory")
_VrIpOspfHostAddressIndex_Type = IpAddress
_VrIpOspfHostAddressIndex_Object = MibTableColumn
vrIpOspfHostAddressIndex = _VrIpOspfHostAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 6, 1, 1, 10),
    _VrIpOspfHostAddressIndex_Type()
)
vrIpOspfHostAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpOspfHostAddressIndex.setStatus("mandatory")


class _VrIpOspfHostTosIndex_Type(Integer32):
    """Custom type vrIpOspfHostTosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_VrIpOspfHostTosIndex_Type.__name__ = "Integer32"
_VrIpOspfHostTosIndex_Object = MibTableColumn
vrIpOspfHostTosIndex = _VrIpOspfHostTosIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 6, 1, 1, 11),
    _VrIpOspfHostTosIndex_Type()
)
vrIpOspfHostTosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpOspfHostTosIndex.setStatus("mandatory")
_VrIpOspfHostProvTable_Object = MibTable
vrIpOspfHostProvTable = _VrIpOspfHostProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 6, 10)
)
if mibBuilder.loadTexts:
    vrIpOspfHostProvTable.setStatus("mandatory")
_VrIpOspfHostProvEntry_Object = MibTableRow
vrIpOspfHostProvEntry = _VrIpOspfHostProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 6, 10, 1)
)
vrIpOspfHostProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfHostAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfHostTosIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfHostProvEntry.setStatus("mandatory")
_VrIpOspfHostAreaId_Type = AreaID
_VrIpOspfHostAreaId_Object = MibTableColumn
vrIpOspfHostAreaId = _VrIpOspfHostAreaId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 6, 10, 1, 1),
    _VrIpOspfHostAreaId_Type()
)
vrIpOspfHostAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfHostAreaId.setStatus("mandatory")


class _VrIpOspfHostMetric_Type(Unsigned32):
    """Custom type vrIpOspfHostMetric based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrIpOspfHostMetric_Type.__name__ = "Unsigned32"
_VrIpOspfHostMetric_Object = MibTableColumn
vrIpOspfHostMetric = _VrIpOspfHostMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 6, 10, 1, 2),
    _VrIpOspfHostMetric_Type()
)
vrIpOspfHostMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfHostMetric.setStatus("mandatory")
_VrIpOspfVirtIf_ObjectIdentity = ObjectIdentity
vrIpOspfVirtIf = _VrIpOspfVirtIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 7)
)
_VrIpOspfVirtIfRowStatusTable_Object = MibTable
vrIpOspfVirtIfRowStatusTable = _VrIpOspfVirtIfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 7, 1)
)
if mibBuilder.loadTexts:
    vrIpOspfVirtIfRowStatusTable.setStatus("mandatory")
_VrIpOspfVirtIfRowStatusEntry_Object = MibTableRow
vrIpOspfVirtIfRowStatusEntry = _VrIpOspfVirtIfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 7, 1, 1)
)
vrIpOspfVirtIfRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfVirtIfAreaIdIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfVirtIfNbrRouterIdIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfVirtIfRowStatusEntry.setStatus("mandatory")
_VrIpOspfVirtIfRowStatus_Type = RowStatus
_VrIpOspfVirtIfRowStatus_Object = MibTableColumn
vrIpOspfVirtIfRowStatus = _VrIpOspfVirtIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 7, 1, 1, 1),
    _VrIpOspfVirtIfRowStatus_Type()
)
vrIpOspfVirtIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfVirtIfRowStatus.setStatus("mandatory")
_VrIpOspfVirtIfComponentName_Type = DisplayString
_VrIpOspfVirtIfComponentName_Object = MibTableColumn
vrIpOspfVirtIfComponentName = _VrIpOspfVirtIfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 7, 1, 1, 2),
    _VrIpOspfVirtIfComponentName_Type()
)
vrIpOspfVirtIfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfVirtIfComponentName.setStatus("mandatory")
_VrIpOspfVirtIfStorageType_Type = StorageType
_VrIpOspfVirtIfStorageType_Object = MibTableColumn
vrIpOspfVirtIfStorageType = _VrIpOspfVirtIfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 7, 1, 1, 4),
    _VrIpOspfVirtIfStorageType_Type()
)
vrIpOspfVirtIfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfVirtIfStorageType.setStatus("mandatory")
_VrIpOspfVirtIfAreaIdIndex_Type = IpAddress
_VrIpOspfVirtIfAreaIdIndex_Object = MibTableColumn
vrIpOspfVirtIfAreaIdIndex = _VrIpOspfVirtIfAreaIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 7, 1, 1, 10),
    _VrIpOspfVirtIfAreaIdIndex_Type()
)
vrIpOspfVirtIfAreaIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpOspfVirtIfAreaIdIndex.setStatus("mandatory")
_VrIpOspfVirtIfNbrRouterIdIndex_Type = IpAddress
_VrIpOspfVirtIfNbrRouterIdIndex_Object = MibTableColumn
vrIpOspfVirtIfNbrRouterIdIndex = _VrIpOspfVirtIfNbrRouterIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 7, 1, 1, 11),
    _VrIpOspfVirtIfNbrRouterIdIndex_Type()
)
vrIpOspfVirtIfNbrRouterIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpOspfVirtIfNbrRouterIdIndex.setStatus("mandatory")
_VrIpOspfVirtIfProvTable_Object = MibTable
vrIpOspfVirtIfProvTable = _VrIpOspfVirtIfProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 7, 10)
)
if mibBuilder.loadTexts:
    vrIpOspfVirtIfProvTable.setStatus("mandatory")
_VrIpOspfVirtIfProvEntry_Object = MibTableRow
vrIpOspfVirtIfProvEntry = _VrIpOspfVirtIfProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 7, 10, 1)
)
vrIpOspfVirtIfProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfVirtIfAreaIdIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfVirtIfNbrRouterIdIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfVirtIfProvEntry.setStatus("mandatory")


class _VrIpOspfVirtIfTransitDelay_Type(Unsigned32):
    """Custom type vrIpOspfVirtIfTransitDelay based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_VrIpOspfVirtIfTransitDelay_Type.__name__ = "Unsigned32"
_VrIpOspfVirtIfTransitDelay_Object = MibTableColumn
vrIpOspfVirtIfTransitDelay = _VrIpOspfVirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 7, 10, 1, 1),
    _VrIpOspfVirtIfTransitDelay_Type()
)
vrIpOspfVirtIfTransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfVirtIfTransitDelay.setStatus("mandatory")


class _VrIpOspfVirtIfRetransInterval_Type(Unsigned32):
    """Custom type vrIpOspfVirtIfRetransInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_VrIpOspfVirtIfRetransInterval_Type.__name__ = "Unsigned32"
_VrIpOspfVirtIfRetransInterval_Object = MibTableColumn
vrIpOspfVirtIfRetransInterval = _VrIpOspfVirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 7, 10, 1, 2),
    _VrIpOspfVirtIfRetransInterval_Type()
)
vrIpOspfVirtIfRetransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfVirtIfRetransInterval.setStatus("mandatory")


class _VrIpOspfVirtIfHelloInterval_Type(Unsigned32):
    """Custom type vrIpOspfVirtIfHelloInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_VrIpOspfVirtIfHelloInterval_Type.__name__ = "Unsigned32"
_VrIpOspfVirtIfHelloInterval_Object = MibTableColumn
vrIpOspfVirtIfHelloInterval = _VrIpOspfVirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 7, 10, 1, 3),
    _VrIpOspfVirtIfHelloInterval_Type()
)
vrIpOspfVirtIfHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfVirtIfHelloInterval.setStatus("mandatory")


class _VrIpOspfVirtIfRtrDeadInterval_Type(Unsigned32):
    """Custom type vrIpOspfVirtIfRtrDeadInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_VrIpOspfVirtIfRtrDeadInterval_Type.__name__ = "Unsigned32"
_VrIpOspfVirtIfRtrDeadInterval_Object = MibTableColumn
vrIpOspfVirtIfRtrDeadInterval = _VrIpOspfVirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 7, 10, 1, 4),
    _VrIpOspfVirtIfRtrDeadInterval_Type()
)
vrIpOspfVirtIfRtrDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfVirtIfRtrDeadInterval.setStatus("mandatory")


class _VrIpOspfVirtIfAuthKey_Type(HexString):
    """Custom type vrIpOspfVirtIfAuthKey based on HexString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_VrIpOspfVirtIfAuthKey_Type.__name__ = "HexString"
_VrIpOspfVirtIfAuthKey_Object = MibTableColumn
vrIpOspfVirtIfAuthKey = _VrIpOspfVirtIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 7, 10, 1, 5),
    _VrIpOspfVirtIfAuthKey_Type()
)
vrIpOspfVirtIfAuthKey.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vrIpOspfVirtIfAuthKey.setStatus("mandatory")
_VrIpOspfVirtIfOperTable_Object = MibTable
vrIpOspfVirtIfOperTable = _VrIpOspfVirtIfOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 7, 11)
)
if mibBuilder.loadTexts:
    vrIpOspfVirtIfOperTable.setStatus("mandatory")
_VrIpOspfVirtIfOperEntry_Object = MibTableRow
vrIpOspfVirtIfOperEntry = _VrIpOspfVirtIfOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 7, 11, 1)
)
vrIpOspfVirtIfOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfVirtIfAreaIdIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfVirtIfNbrRouterIdIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfVirtIfOperEntry.setStatus("mandatory")


class _VrIpOspfVirtIfState_Type(Integer32):
    """Custom type vrIpOspfVirtIfState based on Integer32"""
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


_VrIpOspfVirtIfState_Type.__name__ = "Integer32"
_VrIpOspfVirtIfState_Object = MibTableColumn
vrIpOspfVirtIfState = _VrIpOspfVirtIfState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 7, 11, 1, 1),
    _VrIpOspfVirtIfState_Type()
)
vrIpOspfVirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfVirtIfState.setStatus("mandatory")
_VrIpOspfVirtIfEvents_Type = Counter32
_VrIpOspfVirtIfEvents_Object = MibTableColumn
vrIpOspfVirtIfEvents = _VrIpOspfVirtIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 7, 11, 1, 2),
    _VrIpOspfVirtIfEvents_Type()
)
vrIpOspfVirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfVirtIfEvents.setStatus("mandatory")
_VrIpOspfExport_ObjectIdentity = ObjectIdentity
vrIpOspfExport = _VrIpOspfExport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8)
)
_VrIpOspfExportRowStatusTable_Object = MibTable
vrIpOspfExportRowStatusTable = _VrIpOspfExportRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 1)
)
if mibBuilder.loadTexts:
    vrIpOspfExportRowStatusTable.setStatus("mandatory")
_VrIpOspfExportRowStatusEntry_Object = MibTableRow
vrIpOspfExportRowStatusEntry = _VrIpOspfExportRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 1, 1)
)
vrIpOspfExportRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfExportIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfExportRowStatusEntry.setStatus("mandatory")
_VrIpOspfExportRowStatus_Type = RowStatus
_VrIpOspfExportRowStatus_Object = MibTableColumn
vrIpOspfExportRowStatus = _VrIpOspfExportRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 1, 1, 1),
    _VrIpOspfExportRowStatus_Type()
)
vrIpOspfExportRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfExportRowStatus.setStatus("mandatory")
_VrIpOspfExportComponentName_Type = DisplayString
_VrIpOspfExportComponentName_Object = MibTableColumn
vrIpOspfExportComponentName = _VrIpOspfExportComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 1, 1, 2),
    _VrIpOspfExportComponentName_Type()
)
vrIpOspfExportComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfExportComponentName.setStatus("mandatory")
_VrIpOspfExportStorageType_Type = StorageType
_VrIpOspfExportStorageType_Object = MibTableColumn
vrIpOspfExportStorageType = _VrIpOspfExportStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 1, 1, 4),
    _VrIpOspfExportStorageType_Type()
)
vrIpOspfExportStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfExportStorageType.setStatus("mandatory")


class _VrIpOspfExportIndex_Type(Integer32):
    """Custom type vrIpOspfExportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpOspfExportIndex_Type.__name__ = "Integer32"
_VrIpOspfExportIndex_Object = MibTableColumn
vrIpOspfExportIndex = _VrIpOspfExportIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 1, 1, 10),
    _VrIpOspfExportIndex_Type()
)
vrIpOspfExportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpOspfExportIndex.setStatus("mandatory")
_VrIpOspfExportNetList_ObjectIdentity = ObjectIdentity
vrIpOspfExportNetList = _VrIpOspfExportNetList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 2)
)
_VrIpOspfExportNetListRowStatusTable_Object = MibTable
vrIpOspfExportNetListRowStatusTable = _VrIpOspfExportNetListRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpOspfExportNetListRowStatusTable.setStatus("mandatory")
_VrIpOspfExportNetListRowStatusEntry_Object = MibTableRow
vrIpOspfExportNetListRowStatusEntry = _VrIpOspfExportNetListRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 2, 1, 1)
)
vrIpOspfExportNetListRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfExportIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfExportNetListIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfExportNetListRowStatusEntry.setStatus("mandatory")
_VrIpOspfExportNetListRowStatus_Type = RowStatus
_VrIpOspfExportNetListRowStatus_Object = MibTableColumn
vrIpOspfExportNetListRowStatus = _VrIpOspfExportNetListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 2, 1, 1, 1),
    _VrIpOspfExportNetListRowStatus_Type()
)
vrIpOspfExportNetListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfExportNetListRowStatus.setStatus("mandatory")
_VrIpOspfExportNetListComponentName_Type = DisplayString
_VrIpOspfExportNetListComponentName_Object = MibTableColumn
vrIpOspfExportNetListComponentName = _VrIpOspfExportNetListComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 2, 1, 1, 2),
    _VrIpOspfExportNetListComponentName_Type()
)
vrIpOspfExportNetListComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfExportNetListComponentName.setStatus("mandatory")
_VrIpOspfExportNetListStorageType_Type = StorageType
_VrIpOspfExportNetListStorageType_Object = MibTableColumn
vrIpOspfExportNetListStorageType = _VrIpOspfExportNetListStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 2, 1, 1, 4),
    _VrIpOspfExportNetListStorageType_Type()
)
vrIpOspfExportNetListStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfExportNetListStorageType.setStatus("mandatory")


class _VrIpOspfExportNetListIndex_Type(Integer32):
    """Custom type vrIpOspfExportNetListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpOspfExportNetListIndex_Type.__name__ = "Integer32"
_VrIpOspfExportNetListIndex_Object = MibTableColumn
vrIpOspfExportNetListIndex = _VrIpOspfExportNetListIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 2, 1, 1, 10),
    _VrIpOspfExportNetListIndex_Type()
)
vrIpOspfExportNetListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpOspfExportNetListIndex.setStatus("mandatory")
_VrIpOspfExportNetListProvTable_Object = MibTable
vrIpOspfExportNetListProvTable = _VrIpOspfExportNetListProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpOspfExportNetListProvTable.setStatus("mandatory")
_VrIpOspfExportNetListProvEntry_Object = MibTableRow
vrIpOspfExportNetListProvEntry = _VrIpOspfExportNetListProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 2, 10, 1)
)
vrIpOspfExportNetListProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfExportIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfExportNetListIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfExportNetListProvEntry.setStatus("mandatory")
_VrIpOspfExportNetListIpAddress_Type = IpAddress
_VrIpOspfExportNetListIpAddress_Object = MibTableColumn
vrIpOspfExportNetListIpAddress = _VrIpOspfExportNetListIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 2, 10, 1, 1),
    _VrIpOspfExportNetListIpAddress_Type()
)
vrIpOspfExportNetListIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfExportNetListIpAddress.setStatus("mandatory")
_VrIpOspfExportNetListIpMask_Type = IpAddress
_VrIpOspfExportNetListIpMask_Object = MibTableColumn
vrIpOspfExportNetListIpMask = _VrIpOspfExportNetListIpMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 2, 10, 1, 2),
    _VrIpOspfExportNetListIpMask_Type()
)
vrIpOspfExportNetListIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfExportNetListIpMask.setStatus("mandatory")
_VrIpOspfExportProvTable_Object = MibTable
vrIpOspfExportProvTable = _VrIpOspfExportProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 10)
)
if mibBuilder.loadTexts:
    vrIpOspfExportProvTable.setStatus("mandatory")
_VrIpOspfExportProvEntry_Object = MibTableRow
vrIpOspfExportProvEntry = _VrIpOspfExportProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 10, 1)
)
vrIpOspfExportProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfExportIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfExportProvEntry.setStatus("mandatory")


class _VrIpOspfExportAdvertiseStatus_Type(Integer32):
    """Custom type vrIpOspfExportAdvertiseStatus based on Integer32"""
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


_VrIpOspfExportAdvertiseStatus_Type.__name__ = "Integer32"
_VrIpOspfExportAdvertiseStatus_Object = MibTableColumn
vrIpOspfExportAdvertiseStatus = _VrIpOspfExportAdvertiseStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 10, 1, 1),
    _VrIpOspfExportAdvertiseStatus_Type()
)
vrIpOspfExportAdvertiseStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfExportAdvertiseStatus.setStatus("mandatory")


class _VrIpOspfExportMetric_Type(Integer32):
    """Custom type vrIpOspfExportMetric based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 16777215),
    )


_VrIpOspfExportMetric_Type.__name__ = "Integer32"
_VrIpOspfExportMetric_Object = MibTableColumn
vrIpOspfExportMetric = _VrIpOspfExportMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 10, 1, 2),
    _VrIpOspfExportMetric_Type()
)
vrIpOspfExportMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfExportMetric.setStatus("mandatory")


class _VrIpOspfExportProtocol_Type(Integer32):
    """Custom type vrIpOspfExportProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("bgpExternal", 9),
          ("egp", 2),
          ("rip", 3),
          ("staticLocal", 6),
          ("staticRemote", 7))
    )


_VrIpOspfExportProtocol_Type.__name__ = "Integer32"
_VrIpOspfExportProtocol_Object = MibTableColumn
vrIpOspfExportProtocol = _VrIpOspfExportProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 10, 1, 3),
    _VrIpOspfExportProtocol_Type()
)
vrIpOspfExportProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfExportProtocol.setStatus("mandatory")


class _VrIpOspfExportRipInterface_Type(IpAddress):
    """Custom type vrIpOspfExportRipInterface based on IpAddress"""
    defaultHexValue = "00000000"


_VrIpOspfExportRipInterface_Object = MibTableColumn
vrIpOspfExportRipInterface = _VrIpOspfExportRipInterface_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 10, 1, 4),
    _VrIpOspfExportRipInterface_Type()
)
vrIpOspfExportRipInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfExportRipInterface.setStatus("mandatory")


class _VrIpOspfExportRipNeighbor_Type(IpAddress):
    """Custom type vrIpOspfExportRipNeighbor based on IpAddress"""
    defaultHexValue = "00000000"


_VrIpOspfExportRipNeighbor_Object = MibTableColumn
vrIpOspfExportRipNeighbor = _VrIpOspfExportRipNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 10, 1, 5),
    _VrIpOspfExportRipNeighbor_Type()
)
vrIpOspfExportRipNeighbor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfExportRipNeighbor.setStatus("mandatory")


class _VrIpOspfExportEgpAsId_Type(Unsigned32):
    """Custom type vrIpOspfExportEgpAsId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpOspfExportEgpAsId_Type.__name__ = "Unsigned32"
_VrIpOspfExportEgpAsId_Object = MibTableColumn
vrIpOspfExportEgpAsId = _VrIpOspfExportEgpAsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 10, 1, 6),
    _VrIpOspfExportEgpAsId_Type()
)
vrIpOspfExportEgpAsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfExportEgpAsId.setStatus("mandatory")


class _VrIpOspfExportTag_Type(Unsigned32):
    """Custom type vrIpOspfExportTag based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpOspfExportTag_Type.__name__ = "Unsigned32"
_VrIpOspfExportTag_Object = MibTableColumn
vrIpOspfExportTag = _VrIpOspfExportTag_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 10, 1, 7),
    _VrIpOspfExportTag_Type()
)
vrIpOspfExportTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfExportTag.setStatus("mandatory")


class _VrIpOspfExportExtLsaMetricType_Type(Integer32):
    """Custom type vrIpOspfExportExtLsaMetricType based on Integer32"""
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


_VrIpOspfExportExtLsaMetricType_Type.__name__ = "Integer32"
_VrIpOspfExportExtLsaMetricType_Object = MibTableColumn
vrIpOspfExportExtLsaMetricType = _VrIpOspfExportExtLsaMetricType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 10, 1, 8),
    _VrIpOspfExportExtLsaMetricType_Type()
)
vrIpOspfExportExtLsaMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfExportExtLsaMetricType.setStatus("mandatory")


class _VrIpOspfExportBgpAsId_Type(Unsigned32):
    """Custom type vrIpOspfExportBgpAsId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpOspfExportBgpAsId_Type.__name__ = "Unsigned32"
_VrIpOspfExportBgpAsId_Object = MibTableColumn
vrIpOspfExportBgpAsId = _VrIpOspfExportBgpAsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 10, 1, 9),
    _VrIpOspfExportBgpAsId_Type()
)
vrIpOspfExportBgpAsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfExportBgpAsId.setStatus("mandatory")


class _VrIpOspfExportBgpPeerIp_Type(IpAddress):
    """Custom type vrIpOspfExportBgpPeerIp based on IpAddress"""
    defaultHexValue = "00000000"


_VrIpOspfExportBgpPeerIp_Object = MibTableColumn
vrIpOspfExportBgpPeerIp = _VrIpOspfExportBgpPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 8, 10, 1, 10),
    _VrIpOspfExportBgpPeerIp_Type()
)
vrIpOspfExportBgpPeerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfExportBgpPeerIp.setStatus("mandatory")
_VrIpOspfVirtNbr_ObjectIdentity = ObjectIdentity
vrIpOspfVirtNbr = _VrIpOspfVirtNbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 9)
)
_VrIpOspfVirtNbrRowStatusTable_Object = MibTable
vrIpOspfVirtNbrRowStatusTable = _VrIpOspfVirtNbrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 9, 1)
)
if mibBuilder.loadTexts:
    vrIpOspfVirtNbrRowStatusTable.setStatus("mandatory")
_VrIpOspfVirtNbrRowStatusEntry_Object = MibTableRow
vrIpOspfVirtNbrRowStatusEntry = _VrIpOspfVirtNbrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 9, 1, 1)
)
vrIpOspfVirtNbrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfVirtNbrAreaIdIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfVirtNbrNbrRouterIdIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfVirtNbrRowStatusEntry.setStatus("mandatory")
_VrIpOspfVirtNbrRowStatus_Type = RowStatus
_VrIpOspfVirtNbrRowStatus_Object = MibTableColumn
vrIpOspfVirtNbrRowStatus = _VrIpOspfVirtNbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 9, 1, 1, 1),
    _VrIpOspfVirtNbrRowStatus_Type()
)
vrIpOspfVirtNbrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfVirtNbrRowStatus.setStatus("mandatory")
_VrIpOspfVirtNbrComponentName_Type = DisplayString
_VrIpOspfVirtNbrComponentName_Object = MibTableColumn
vrIpOspfVirtNbrComponentName = _VrIpOspfVirtNbrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 9, 1, 1, 2),
    _VrIpOspfVirtNbrComponentName_Type()
)
vrIpOspfVirtNbrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfVirtNbrComponentName.setStatus("mandatory")
_VrIpOspfVirtNbrStorageType_Type = StorageType
_VrIpOspfVirtNbrStorageType_Object = MibTableColumn
vrIpOspfVirtNbrStorageType = _VrIpOspfVirtNbrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 9, 1, 1, 4),
    _VrIpOspfVirtNbrStorageType_Type()
)
vrIpOspfVirtNbrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfVirtNbrStorageType.setStatus("mandatory")
_VrIpOspfVirtNbrAreaIdIndex_Type = IpAddress
_VrIpOspfVirtNbrAreaIdIndex_Object = MibTableColumn
vrIpOspfVirtNbrAreaIdIndex = _VrIpOspfVirtNbrAreaIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 9, 1, 1, 10),
    _VrIpOspfVirtNbrAreaIdIndex_Type()
)
vrIpOspfVirtNbrAreaIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpOspfVirtNbrAreaIdIndex.setStatus("mandatory")
_VrIpOspfVirtNbrNbrRouterIdIndex_Type = IpAddress
_VrIpOspfVirtNbrNbrRouterIdIndex_Object = MibTableColumn
vrIpOspfVirtNbrNbrRouterIdIndex = _VrIpOspfVirtNbrNbrRouterIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 9, 1, 1, 11),
    _VrIpOspfVirtNbrNbrRouterIdIndex_Type()
)
vrIpOspfVirtNbrNbrRouterIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpOspfVirtNbrNbrRouterIdIndex.setStatus("mandatory")
_VrIpOspfVirtNbrOperTable_Object = MibTable
vrIpOspfVirtNbrOperTable = _VrIpOspfVirtNbrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 9, 10)
)
if mibBuilder.loadTexts:
    vrIpOspfVirtNbrOperTable.setStatus("mandatory")
_VrIpOspfVirtNbrOperEntry_Object = MibTableRow
vrIpOspfVirtNbrOperEntry = _VrIpOspfVirtNbrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 9, 10, 1)
)
vrIpOspfVirtNbrOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfVirtNbrAreaIdIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfVirtNbrNbrRouterIdIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfVirtNbrOperEntry.setStatus("mandatory")
_VrIpOspfVirtNbrNbrIpAddress_Type = IpAddress
_VrIpOspfVirtNbrNbrIpAddress_Object = MibTableColumn
vrIpOspfVirtNbrNbrIpAddress = _VrIpOspfVirtNbrNbrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 9, 10, 1, 1),
    _VrIpOspfVirtNbrNbrIpAddress_Type()
)
vrIpOspfVirtNbrNbrIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfVirtNbrNbrIpAddress.setStatus("mandatory")


class _VrIpOspfVirtNbrOptions_Type(Unsigned32):
    """Custom type vrIpOspfVirtNbrOptions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VrIpOspfVirtNbrOptions_Type.__name__ = "Unsigned32"
_VrIpOspfVirtNbrOptions_Object = MibTableColumn
vrIpOspfVirtNbrOptions = _VrIpOspfVirtNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 9, 10, 1, 2),
    _VrIpOspfVirtNbrOptions_Type()
)
vrIpOspfVirtNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfVirtNbrOptions.setStatus("mandatory")


class _VrIpOspfVirtNbrState_Type(Integer32):
    """Custom type vrIpOspfVirtNbrState based on Integer32"""
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


_VrIpOspfVirtNbrState_Type.__name__ = "Integer32"
_VrIpOspfVirtNbrState_Object = MibTableColumn
vrIpOspfVirtNbrState = _VrIpOspfVirtNbrState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 9, 10, 1, 3),
    _VrIpOspfVirtNbrState_Type()
)
vrIpOspfVirtNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfVirtNbrState.setStatus("mandatory")
_VrIpOspfVirtNbrEvents_Type = Counter32
_VrIpOspfVirtNbrEvents_Object = MibTableColumn
vrIpOspfVirtNbrEvents = _VrIpOspfVirtNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 9, 10, 1, 4),
    _VrIpOspfVirtNbrEvents_Type()
)
vrIpOspfVirtNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfVirtNbrEvents.setStatus("mandatory")


class _VrIpOspfVirtNbrLsRetransQlen_Type(Gauge32):
    """Custom type vrIpOspfVirtNbrLsRetransQlen based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpOspfVirtNbrLsRetransQlen_Type.__name__ = "Gauge32"
_VrIpOspfVirtNbrLsRetransQlen_Object = MibTableColumn
vrIpOspfVirtNbrLsRetransQlen = _VrIpOspfVirtNbrLsRetransQlen_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 9, 10, 1, 5),
    _VrIpOspfVirtNbrLsRetransQlen_Type()
)
vrIpOspfVirtNbrLsRetransQlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfVirtNbrLsRetransQlen.setStatus("mandatory")


class _VrIpOspfVirtNbrExchangeStatus_Type(Integer32):
    """Custom type vrIpOspfVirtNbrExchangeStatus based on Integer32"""
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


_VrIpOspfVirtNbrExchangeStatus_Type.__name__ = "Integer32"
_VrIpOspfVirtNbrExchangeStatus_Object = MibTableColumn
vrIpOspfVirtNbrExchangeStatus = _VrIpOspfVirtNbrExchangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 9, 10, 1, 6),
    _VrIpOspfVirtNbrExchangeStatus_Type()
)
vrIpOspfVirtNbrExchangeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfVirtNbrExchangeStatus.setStatus("mandatory")
_VrIpOspfNbr_ObjectIdentity = ObjectIdentity
vrIpOspfNbr = _VrIpOspfNbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 10)
)
_VrIpOspfNbrRowStatusTable_Object = MibTable
vrIpOspfNbrRowStatusTable = _VrIpOspfNbrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 10, 1)
)
if mibBuilder.loadTexts:
    vrIpOspfNbrRowStatusTable.setStatus("mandatory")
_VrIpOspfNbrRowStatusEntry_Object = MibTableRow
vrIpOspfNbrRowStatusEntry = _VrIpOspfNbrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 10, 1, 1)
)
vrIpOspfNbrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfNbrAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfNbrRowStatusEntry.setStatus("mandatory")
_VrIpOspfNbrRowStatus_Type = RowStatus
_VrIpOspfNbrRowStatus_Object = MibTableColumn
vrIpOspfNbrRowStatus = _VrIpOspfNbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 10, 1, 1, 1),
    _VrIpOspfNbrRowStatus_Type()
)
vrIpOspfNbrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfNbrRowStatus.setStatus("mandatory")
_VrIpOspfNbrComponentName_Type = DisplayString
_VrIpOspfNbrComponentName_Object = MibTableColumn
vrIpOspfNbrComponentName = _VrIpOspfNbrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 10, 1, 1, 2),
    _VrIpOspfNbrComponentName_Type()
)
vrIpOspfNbrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfNbrComponentName.setStatus("mandatory")
_VrIpOspfNbrStorageType_Type = StorageType
_VrIpOspfNbrStorageType_Object = MibTableColumn
vrIpOspfNbrStorageType = _VrIpOspfNbrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 10, 1, 1, 4),
    _VrIpOspfNbrStorageType_Type()
)
vrIpOspfNbrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfNbrStorageType.setStatus("mandatory")
_VrIpOspfNbrAddressIndex_Type = IpAddress
_VrIpOspfNbrAddressIndex_Object = MibTableColumn
vrIpOspfNbrAddressIndex = _VrIpOspfNbrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 10, 1, 1, 10),
    _VrIpOspfNbrAddressIndex_Type()
)
vrIpOspfNbrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpOspfNbrAddressIndex.setStatus("mandatory")


class _VrIpOspfNbrAddressLessIndex_Type(Integer32):
    """Custom type vrIpOspfNbrAddressLessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_VrIpOspfNbrAddressLessIndex_Type.__name__ = "Integer32"
_VrIpOspfNbrAddressLessIndex_Object = MibTableColumn
vrIpOspfNbrAddressLessIndex = _VrIpOspfNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 10, 1, 1, 11),
    _VrIpOspfNbrAddressLessIndex_Type()
)
vrIpOspfNbrAddressLessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpOspfNbrAddressLessIndex.setStatus("mandatory")
_VrIpOspfNbrOperTable_Object = MibTable
vrIpOspfNbrOperTable = _VrIpOspfNbrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 10, 10)
)
if mibBuilder.loadTexts:
    vrIpOspfNbrOperTable.setStatus("mandatory")
_VrIpOspfNbrOperEntry_Object = MibTableRow
vrIpOspfNbrOperEntry = _VrIpOspfNbrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 10, 10, 1)
)
vrIpOspfNbrOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfNbrAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfNbrOperEntry.setStatus("mandatory")
_VrIpOspfNbrRtrId_Type = IpAddress
_VrIpOspfNbrRtrId_Object = MibTableColumn
vrIpOspfNbrRtrId = _VrIpOspfNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 10, 10, 1, 1),
    _VrIpOspfNbrRtrId_Type()
)
vrIpOspfNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfNbrRtrId.setStatus("mandatory")


class _VrIpOspfNbrOptions_Type(Unsigned32):
    """Custom type vrIpOspfNbrOptions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VrIpOspfNbrOptions_Type.__name__ = "Unsigned32"
_VrIpOspfNbrOptions_Object = MibTableColumn
vrIpOspfNbrOptions = _VrIpOspfNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 10, 10, 1, 2),
    _VrIpOspfNbrOptions_Type()
)
vrIpOspfNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfNbrOptions.setStatus("mandatory")


class _VrIpOspfNbrPriority_Type(Unsigned32):
    """Custom type vrIpOspfNbrPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrIpOspfNbrPriority_Type.__name__ = "Unsigned32"
_VrIpOspfNbrPriority_Object = MibTableColumn
vrIpOspfNbrPriority = _VrIpOspfNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 10, 10, 1, 3),
    _VrIpOspfNbrPriority_Type()
)
vrIpOspfNbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfNbrPriority.setStatus("mandatory")


class _VrIpOspfNbrState_Type(Integer32):
    """Custom type vrIpOspfNbrState based on Integer32"""
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


_VrIpOspfNbrState_Type.__name__ = "Integer32"
_VrIpOspfNbrState_Object = MibTableColumn
vrIpOspfNbrState = _VrIpOspfNbrState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 10, 10, 1, 4),
    _VrIpOspfNbrState_Type()
)
vrIpOspfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfNbrState.setStatus("mandatory")
_VrIpOspfNbrEvents_Type = Counter32
_VrIpOspfNbrEvents_Object = MibTableColumn
vrIpOspfNbrEvents = _VrIpOspfNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 10, 10, 1, 5),
    _VrIpOspfNbrEvents_Type()
)
vrIpOspfNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfNbrEvents.setStatus("mandatory")


class _VrIpOspfNbrLsRetransQlen_Type(Gauge32):
    """Custom type vrIpOspfNbrLsRetransQlen based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpOspfNbrLsRetransQlen_Type.__name__ = "Gauge32"
_VrIpOspfNbrLsRetransQlen_Object = MibTableColumn
vrIpOspfNbrLsRetransQlen = _VrIpOspfNbrLsRetransQlen_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 10, 10, 1, 6),
    _VrIpOspfNbrLsRetransQlen_Type()
)
vrIpOspfNbrLsRetransQlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfNbrLsRetransQlen.setStatus("mandatory")


class _VrIpOspfNbrNbmaNbrStatus_Type(Integer32):
    """Custom type vrIpOspfNbrNbmaNbrStatus based on Integer32"""
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


_VrIpOspfNbrNbmaNbrStatus_Type.__name__ = "Integer32"
_VrIpOspfNbrNbmaNbrStatus_Object = MibTableColumn
vrIpOspfNbrNbmaNbrStatus = _VrIpOspfNbrNbmaNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 10, 10, 1, 7),
    _VrIpOspfNbrNbmaNbrStatus_Type()
)
vrIpOspfNbrNbmaNbrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfNbrNbmaNbrStatus.setStatus("mandatory")


class _VrIpOspfNbrExchangeStatus_Type(Integer32):
    """Custom type vrIpOspfNbrExchangeStatus based on Integer32"""
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


_VrIpOspfNbrExchangeStatus_Type.__name__ = "Integer32"
_VrIpOspfNbrExchangeStatus_Object = MibTableColumn
vrIpOspfNbrExchangeStatus = _VrIpOspfNbrExchangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 10, 10, 1, 8),
    _VrIpOspfNbrExchangeStatus_Type()
)
vrIpOspfNbrExchangeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfNbrExchangeStatus.setStatus("mandatory")


class _VrIpOspfNbrPermanence_Type(Integer32):
    """Custom type vrIpOspfNbrPermanence based on Integer32"""
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


_VrIpOspfNbrPermanence_Type.__name__ = "Integer32"
_VrIpOspfNbrPermanence_Object = MibTableColumn
vrIpOspfNbrPermanence = _VrIpOspfNbrPermanence_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 10, 10, 1, 11),
    _VrIpOspfNbrPermanence_Type()
)
vrIpOspfNbrPermanence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfNbrPermanence.setStatus("mandatory")
_VrIpOspfLsdb_ObjectIdentity = ObjectIdentity
vrIpOspfLsdb = _VrIpOspfLsdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 11)
)
_VrIpOspfLsdbRowStatusTable_Object = MibTable
vrIpOspfLsdbRowStatusTable = _VrIpOspfLsdbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 11, 1)
)
if mibBuilder.loadTexts:
    vrIpOspfLsdbRowStatusTable.setStatus("mandatory")
_VrIpOspfLsdbRowStatusEntry_Object = MibTableRow
vrIpOspfLsdbRowStatusEntry = _VrIpOspfLsdbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 11, 1, 1)
)
vrIpOspfLsdbRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfLsdbAreaIdIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfLsdbLsdbTypeIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfLsdbLsIdIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfLsdbRouterIdIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfLsdbRowStatusEntry.setStatus("mandatory")
_VrIpOspfLsdbRowStatus_Type = RowStatus
_VrIpOspfLsdbRowStatus_Object = MibTableColumn
vrIpOspfLsdbRowStatus = _VrIpOspfLsdbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 11, 1, 1, 1),
    _VrIpOspfLsdbRowStatus_Type()
)
vrIpOspfLsdbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfLsdbRowStatus.setStatus("mandatory")
_VrIpOspfLsdbComponentName_Type = DisplayString
_VrIpOspfLsdbComponentName_Object = MibTableColumn
vrIpOspfLsdbComponentName = _VrIpOspfLsdbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 11, 1, 1, 2),
    _VrIpOspfLsdbComponentName_Type()
)
vrIpOspfLsdbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfLsdbComponentName.setStatus("mandatory")
_VrIpOspfLsdbStorageType_Type = StorageType
_VrIpOspfLsdbStorageType_Object = MibTableColumn
vrIpOspfLsdbStorageType = _VrIpOspfLsdbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 11, 1, 1, 4),
    _VrIpOspfLsdbStorageType_Type()
)
vrIpOspfLsdbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfLsdbStorageType.setStatus("mandatory")
_VrIpOspfLsdbAreaIdIndex_Type = IpAddress
_VrIpOspfLsdbAreaIdIndex_Object = MibTableColumn
vrIpOspfLsdbAreaIdIndex = _VrIpOspfLsdbAreaIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 11, 1, 1, 10),
    _VrIpOspfLsdbAreaIdIndex_Type()
)
vrIpOspfLsdbAreaIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpOspfLsdbAreaIdIndex.setStatus("mandatory")


class _VrIpOspfLsdbLsdbTypeIndex_Type(Integer32):
    """Custom type vrIpOspfLsdbLsdbTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_VrIpOspfLsdbLsdbTypeIndex_Type.__name__ = "Integer32"
_VrIpOspfLsdbLsdbTypeIndex_Object = MibTableColumn
vrIpOspfLsdbLsdbTypeIndex = _VrIpOspfLsdbLsdbTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 11, 1, 1, 11),
    _VrIpOspfLsdbLsdbTypeIndex_Type()
)
vrIpOspfLsdbLsdbTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpOspfLsdbLsdbTypeIndex.setStatus("mandatory")
_VrIpOspfLsdbLsIdIndex_Type = IpAddress
_VrIpOspfLsdbLsIdIndex_Object = MibTableColumn
vrIpOspfLsdbLsIdIndex = _VrIpOspfLsdbLsIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 11, 1, 1, 12),
    _VrIpOspfLsdbLsIdIndex_Type()
)
vrIpOspfLsdbLsIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpOspfLsdbLsIdIndex.setStatus("mandatory")
_VrIpOspfLsdbRouterIdIndex_Type = IpAddress
_VrIpOspfLsdbRouterIdIndex_Object = MibTableColumn
vrIpOspfLsdbRouterIdIndex = _VrIpOspfLsdbRouterIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 11, 1, 1, 13),
    _VrIpOspfLsdbRouterIdIndex_Type()
)
vrIpOspfLsdbRouterIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpOspfLsdbRouterIdIndex.setStatus("mandatory")
_VrIpOspfLsdbOperTable_Object = MibTable
vrIpOspfLsdbOperTable = _VrIpOspfLsdbOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 11, 10)
)
if mibBuilder.loadTexts:
    vrIpOspfLsdbOperTable.setStatus("mandatory")
_VrIpOspfLsdbOperEntry_Object = MibTableRow
vrIpOspfLsdbOperEntry = _VrIpOspfLsdbOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 11, 10, 1)
)
vrIpOspfLsdbOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfLsdbAreaIdIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfLsdbLsdbTypeIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfLsdbLsIdIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfLsdbRouterIdIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfLsdbOperEntry.setStatus("mandatory")


class _VrIpOspfLsdbSequence_Type(Unsigned32):
    """Custom type vrIpOspfLsdbSequence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpOspfLsdbSequence_Type.__name__ = "Unsigned32"
_VrIpOspfLsdbSequence_Object = MibTableColumn
vrIpOspfLsdbSequence = _VrIpOspfLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 11, 10, 1, 1),
    _VrIpOspfLsdbSequence_Type()
)
vrIpOspfLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfLsdbSequence.setStatus("mandatory")


class _VrIpOspfLsdbAge_Type(Gauge32):
    """Custom type vrIpOspfLsdbAge based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_VrIpOspfLsdbAge_Type.__name__ = "Gauge32"
_VrIpOspfLsdbAge_Object = MibTableColumn
vrIpOspfLsdbAge = _VrIpOspfLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 11, 10, 1, 2),
    _VrIpOspfLsdbAge_Type()
)
vrIpOspfLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfLsdbAge.setStatus("mandatory")


class _VrIpOspfLsdbChecksum_Type(Unsigned32):
    """Custom type vrIpOspfLsdbChecksum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpOspfLsdbChecksum_Type.__name__ = "Unsigned32"
_VrIpOspfLsdbChecksum_Object = MibTableColumn
vrIpOspfLsdbChecksum = _VrIpOspfLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 11, 10, 1, 3),
    _VrIpOspfLsdbChecksum_Type()
)
vrIpOspfLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfLsdbChecksum.setStatus("mandatory")


class _VrIpOspfLsdbAdvertisement_Type(HexString):
    """Custom type vrIpOspfLsdbAdvertisement based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_VrIpOspfLsdbAdvertisement_Type.__name__ = "HexString"
_VrIpOspfLsdbAdvertisement_Object = MibTableColumn
vrIpOspfLsdbAdvertisement = _VrIpOspfLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 11, 10, 1, 4),
    _VrIpOspfLsdbAdvertisement_Type()
)
vrIpOspfLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfLsdbAdvertisement.setStatus("mandatory")
_VrIpOspfExtLsdb_ObjectIdentity = ObjectIdentity
vrIpOspfExtLsdb = _VrIpOspfExtLsdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 12)
)
_VrIpOspfExtLsdbRowStatusTable_Object = MibTable
vrIpOspfExtLsdbRowStatusTable = _VrIpOspfExtLsdbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 12, 1)
)
if mibBuilder.loadTexts:
    vrIpOspfExtLsdbRowStatusTable.setStatus("mandatory")
_VrIpOspfExtLsdbRowStatusEntry_Object = MibTableRow
vrIpOspfExtLsdbRowStatusEntry = _VrIpOspfExtLsdbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 12, 1, 1)
)
vrIpOspfExtLsdbRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfExtLsdbLsdbTypeIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfExtLsdbLsIdIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfExtLsdbRouterIdIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfExtLsdbRowStatusEntry.setStatus("mandatory")
_VrIpOspfExtLsdbRowStatus_Type = RowStatus
_VrIpOspfExtLsdbRowStatus_Object = MibTableColumn
vrIpOspfExtLsdbRowStatus = _VrIpOspfExtLsdbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 12, 1, 1, 1),
    _VrIpOspfExtLsdbRowStatus_Type()
)
vrIpOspfExtLsdbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfExtLsdbRowStatus.setStatus("mandatory")
_VrIpOspfExtLsdbComponentName_Type = DisplayString
_VrIpOspfExtLsdbComponentName_Object = MibTableColumn
vrIpOspfExtLsdbComponentName = _VrIpOspfExtLsdbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 12, 1, 1, 2),
    _VrIpOspfExtLsdbComponentName_Type()
)
vrIpOspfExtLsdbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfExtLsdbComponentName.setStatus("mandatory")
_VrIpOspfExtLsdbStorageType_Type = StorageType
_VrIpOspfExtLsdbStorageType_Object = MibTableColumn
vrIpOspfExtLsdbStorageType = _VrIpOspfExtLsdbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 12, 1, 1, 4),
    _VrIpOspfExtLsdbStorageType_Type()
)
vrIpOspfExtLsdbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfExtLsdbStorageType.setStatus("mandatory")


class _VrIpOspfExtLsdbLsdbTypeIndex_Type(Integer32):
    """Custom type vrIpOspfExtLsdbLsdbTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_VrIpOspfExtLsdbLsdbTypeIndex_Type.__name__ = "Integer32"
_VrIpOspfExtLsdbLsdbTypeIndex_Object = MibTableColumn
vrIpOspfExtLsdbLsdbTypeIndex = _VrIpOspfExtLsdbLsdbTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 12, 1, 1, 10),
    _VrIpOspfExtLsdbLsdbTypeIndex_Type()
)
vrIpOspfExtLsdbLsdbTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpOspfExtLsdbLsdbTypeIndex.setStatus("mandatory")
_VrIpOspfExtLsdbLsIdIndex_Type = IpAddress
_VrIpOspfExtLsdbLsIdIndex_Object = MibTableColumn
vrIpOspfExtLsdbLsIdIndex = _VrIpOspfExtLsdbLsIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 12, 1, 1, 11),
    _VrIpOspfExtLsdbLsIdIndex_Type()
)
vrIpOspfExtLsdbLsIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpOspfExtLsdbLsIdIndex.setStatus("mandatory")
_VrIpOspfExtLsdbRouterIdIndex_Type = IpAddress
_VrIpOspfExtLsdbRouterIdIndex_Object = MibTableColumn
vrIpOspfExtLsdbRouterIdIndex = _VrIpOspfExtLsdbRouterIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 12, 1, 1, 12),
    _VrIpOspfExtLsdbRouterIdIndex_Type()
)
vrIpOspfExtLsdbRouterIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpOspfExtLsdbRouterIdIndex.setStatus("mandatory")
_VrIpOspfExtLsdbOperTable_Object = MibTable
vrIpOspfExtLsdbOperTable = _VrIpOspfExtLsdbOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 12, 10)
)
if mibBuilder.loadTexts:
    vrIpOspfExtLsdbOperTable.setStatus("mandatory")
_VrIpOspfExtLsdbOperEntry_Object = MibTableRow
vrIpOspfExtLsdbOperEntry = _VrIpOspfExtLsdbOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 12, 10, 1)
)
vrIpOspfExtLsdbOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfExtLsdbLsdbTypeIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfExtLsdbLsIdIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfExtLsdbRouterIdIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfExtLsdbOperEntry.setStatus("mandatory")


class _VrIpOspfExtLsdbSequence_Type(Unsigned32):
    """Custom type vrIpOspfExtLsdbSequence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpOspfExtLsdbSequence_Type.__name__ = "Unsigned32"
_VrIpOspfExtLsdbSequence_Object = MibTableColumn
vrIpOspfExtLsdbSequence = _VrIpOspfExtLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 12, 10, 1, 1),
    _VrIpOspfExtLsdbSequence_Type()
)
vrIpOspfExtLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfExtLsdbSequence.setStatus("mandatory")


class _VrIpOspfExtLsdbAge_Type(Gauge32):
    """Custom type vrIpOspfExtLsdbAge based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_VrIpOspfExtLsdbAge_Type.__name__ = "Gauge32"
_VrIpOspfExtLsdbAge_Object = MibTableColumn
vrIpOspfExtLsdbAge = _VrIpOspfExtLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 12, 10, 1, 2),
    _VrIpOspfExtLsdbAge_Type()
)
vrIpOspfExtLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfExtLsdbAge.setStatus("mandatory")


class _VrIpOspfExtLsdbChecksum_Type(Unsigned32):
    """Custom type vrIpOspfExtLsdbChecksum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpOspfExtLsdbChecksum_Type.__name__ = "Unsigned32"
_VrIpOspfExtLsdbChecksum_Object = MibTableColumn
vrIpOspfExtLsdbChecksum = _VrIpOspfExtLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 12, 10, 1, 3),
    _VrIpOspfExtLsdbChecksum_Type()
)
vrIpOspfExtLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfExtLsdbChecksum.setStatus("mandatory")


class _VrIpOspfExtLsdbAdvertisement_Type(HexString):
    """Custom type vrIpOspfExtLsdbAdvertisement based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_VrIpOspfExtLsdbAdvertisement_Type.__name__ = "HexString"
_VrIpOspfExtLsdbAdvertisement_Object = MibTableColumn
vrIpOspfExtLsdbAdvertisement = _VrIpOspfExtLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 12, 10, 1, 4),
    _VrIpOspfExtLsdbAdvertisement_Type()
)
vrIpOspfExtLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfExtLsdbAdvertisement.setStatus("mandatory")
_VrIpOspfProvTable_Object = MibTable
vrIpOspfProvTable = _VrIpOspfProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 100)
)
if mibBuilder.loadTexts:
    vrIpOspfProvTable.setStatus("mandatory")
_VrIpOspfProvEntry_Object = MibTableRow
vrIpOspfProvEntry = _VrIpOspfProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 100, 1)
)
vrIpOspfProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfProvEntry.setStatus("mandatory")
_VrIpOspfRouterId_Type = RouterID
_VrIpOspfRouterId_Object = MibTableColumn
vrIpOspfRouterId = _VrIpOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 100, 1, 1),
    _VrIpOspfRouterId_Type()
)
vrIpOspfRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfRouterId.setStatus("mandatory")


class _VrIpOspfSnmpAdminStatus_Type(Integer32):
    """Custom type vrIpOspfSnmpAdminStatus based on Integer32"""
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


_VrIpOspfSnmpAdminStatus_Type.__name__ = "Integer32"
_VrIpOspfSnmpAdminStatus_Object = MibTableColumn
vrIpOspfSnmpAdminStatus = _VrIpOspfSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 100, 1, 2),
    _VrIpOspfSnmpAdminStatus_Type()
)
vrIpOspfSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfSnmpAdminStatus.setStatus("mandatory")


class _VrIpOspfAsBdrRtrStatus_Type(Integer32):
    """Custom type vrIpOspfAsBdrRtrStatus based on Integer32"""
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


_VrIpOspfAsBdrRtrStatus_Type.__name__ = "Integer32"
_VrIpOspfAsBdrRtrStatus_Object = MibTableColumn
vrIpOspfAsBdrRtrStatus = _VrIpOspfAsBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 100, 1, 3),
    _VrIpOspfAsBdrRtrStatus_Type()
)
vrIpOspfAsBdrRtrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfAsBdrRtrStatus.setStatus("mandatory")


class _VrIpOspfTosSupport_Type(Integer32):
    """Custom type vrIpOspfTosSupport based on Integer32"""
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


_VrIpOspfTosSupport_Type.__name__ = "Integer32"
_VrIpOspfTosSupport_Object = MibTableColumn
vrIpOspfTosSupport = _VrIpOspfTosSupport_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 100, 1, 4),
    _VrIpOspfTosSupport_Type()
)
vrIpOspfTosSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfTosSupport.setStatus("mandatory")


class _VrIpOspfExtLsdbLimit_Type(Integer32):
    """Custom type vrIpOspfExtLsdbLimit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_VrIpOspfExtLsdbLimit_Type.__name__ = "Integer32"
_VrIpOspfExtLsdbLimit_Object = MibTableColumn
vrIpOspfExtLsdbLimit = _VrIpOspfExtLsdbLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 100, 1, 5),
    _VrIpOspfExtLsdbLimit_Type()
)
vrIpOspfExtLsdbLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfExtLsdbLimit.setStatus("mandatory")


class _VrIpOspfMulticastForward_Type(Unsigned32):
    """Custom type vrIpOspfMulticastForward based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_VrIpOspfMulticastForward_Type.__name__ = "Unsigned32"
_VrIpOspfMulticastForward_Object = MibTableColumn
vrIpOspfMulticastForward = _VrIpOspfMulticastForward_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 100, 1, 6),
    _VrIpOspfMulticastForward_Type()
)
vrIpOspfMulticastForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfMulticastForward.setStatus("mandatory")


class _VrIpOspfMigrateRip_Type(Integer32):
    """Custom type vrIpOspfMigrateRip based on Integer32"""
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


_VrIpOspfMigrateRip_Type.__name__ = "Integer32"
_VrIpOspfMigrateRip_Object = MibTableColumn
vrIpOspfMigrateRip = _VrIpOspfMigrateRip_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 100, 1, 7),
    _VrIpOspfMigrateRip_Type()
)
vrIpOspfMigrateRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfMigrateRip.setStatus("mandatory")


class _VrIpOspfGenerateDefaultRouteMetric_Type(Integer32):
    """Custom type vrIpOspfGenerateDefaultRouteMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_VrIpOspfGenerateDefaultRouteMetric_Type.__name__ = "Integer32"
_VrIpOspfGenerateDefaultRouteMetric_Object = MibTableColumn
vrIpOspfGenerateDefaultRouteMetric = _VrIpOspfGenerateDefaultRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 100, 1, 8),
    _VrIpOspfGenerateDefaultRouteMetric_Type()
)
vrIpOspfGenerateDefaultRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpOspfGenerateDefaultRouteMetric.setStatus("mandatory")
_VrIpOspfOperTable_Object = MibTable
vrIpOspfOperTable = _VrIpOspfOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 101)
)
if mibBuilder.loadTexts:
    vrIpOspfOperTable.setStatus("mandatory")
_VrIpOspfOperEntry_Object = MibTableRow
vrIpOspfOperEntry = _VrIpOspfOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 101, 1)
)
vrIpOspfOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfOperEntry.setStatus("mandatory")


class _VrIpOspfVersionNumber_Type(Unsigned32):
    """Custom type vrIpOspfVersionNumber based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_VrIpOspfVersionNumber_Type.__name__ = "Unsigned32"
_VrIpOspfVersionNumber_Object = MibTableColumn
vrIpOspfVersionNumber = _VrIpOspfVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 101, 1, 1),
    _VrIpOspfVersionNumber_Type()
)
vrIpOspfVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfVersionNumber.setStatus("mandatory")


class _VrIpOspfAreaBdrRtrStatus_Type(Integer32):
    """Custom type vrIpOspfAreaBdrRtrStatus based on Integer32"""
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


_VrIpOspfAreaBdrRtrStatus_Type.__name__ = "Integer32"
_VrIpOspfAreaBdrRtrStatus_Object = MibTableColumn
vrIpOspfAreaBdrRtrStatus = _VrIpOspfAreaBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 101, 1, 2),
    _VrIpOspfAreaBdrRtrStatus_Type()
)
vrIpOspfAreaBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfAreaBdrRtrStatus.setStatus("mandatory")


class _VrIpOspfExternLsaCount_Type(Gauge32):
    """Custom type vrIpOspfExternLsaCount based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpOspfExternLsaCount_Type.__name__ = "Gauge32"
_VrIpOspfExternLsaCount_Object = MibTableColumn
vrIpOspfExternLsaCount = _VrIpOspfExternLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 101, 1, 3),
    _VrIpOspfExternLsaCount_Type()
)
vrIpOspfExternLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfExternLsaCount.setStatus("mandatory")


class _VrIpOspfExternLsaChecksumSum_Type(Unsigned32):
    """Custom type vrIpOspfExternLsaChecksumSum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpOspfExternLsaChecksumSum_Type.__name__ = "Unsigned32"
_VrIpOspfExternLsaChecksumSum_Object = MibTableColumn
vrIpOspfExternLsaChecksumSum = _VrIpOspfExternLsaChecksumSum_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 101, 1, 4),
    _VrIpOspfExternLsaChecksumSum_Type()
)
vrIpOspfExternLsaChecksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfExternLsaChecksumSum.setStatus("mandatory")
_VrIpOspfOriginateNewLsas_Type = Counter32
_VrIpOspfOriginateNewLsas_Object = MibTableColumn
vrIpOspfOriginateNewLsas = _VrIpOspfOriginateNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 101, 1, 5),
    _VrIpOspfOriginateNewLsas_Type()
)
vrIpOspfOriginateNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfOriginateNewLsas.setStatus("mandatory")
_VrIpOspfRxNewLsas_Type = Counter32
_VrIpOspfRxNewLsas_Object = MibTableColumn
vrIpOspfRxNewLsas = _VrIpOspfRxNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 101, 1, 6),
    _VrIpOspfRxNewLsas_Type()
)
vrIpOspfRxNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfRxNewLsas.setStatus("mandatory")
_VrIpOspfStateTable_Object = MibTable
vrIpOspfStateTable = _VrIpOspfStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 102)
)
if mibBuilder.loadTexts:
    vrIpOspfStateTable.setStatus("mandatory")
_VrIpOspfStateEntry_Object = MibTableRow
vrIpOspfStateEntry = _VrIpOspfStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 102, 1)
)
vrIpOspfStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfStateEntry.setStatus("mandatory")


class _VrIpOspfAdminState_Type(Integer32):
    """Custom type vrIpOspfAdminState based on Integer32"""
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


_VrIpOspfAdminState_Type.__name__ = "Integer32"
_VrIpOspfAdminState_Object = MibTableColumn
vrIpOspfAdminState = _VrIpOspfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 102, 1, 1),
    _VrIpOspfAdminState_Type()
)
vrIpOspfAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfAdminState.setStatus("mandatory")


class _VrIpOspfOperationalState_Type(Integer32):
    """Custom type vrIpOspfOperationalState based on Integer32"""
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


_VrIpOspfOperationalState_Type.__name__ = "Integer32"
_VrIpOspfOperationalState_Object = MibTableColumn
vrIpOspfOperationalState = _VrIpOspfOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 102, 1, 2),
    _VrIpOspfOperationalState_Type()
)
vrIpOspfOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfOperationalState.setStatus("mandatory")


class _VrIpOspfUsageState_Type(Integer32):
    """Custom type vrIpOspfUsageState based on Integer32"""
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


_VrIpOspfUsageState_Type.__name__ = "Integer32"
_VrIpOspfUsageState_Object = MibTableColumn
vrIpOspfUsageState = _VrIpOspfUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 102, 1, 3),
    _VrIpOspfUsageState_Type()
)
vrIpOspfUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfUsageState.setStatus("mandatory")
_VrIpOspfOperStatusTable_Object = MibTable
vrIpOspfOperStatusTable = _VrIpOspfOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 105)
)
if mibBuilder.loadTexts:
    vrIpOspfOperStatusTable.setStatus("mandatory")
_VrIpOspfOperStatusEntry_Object = MibTableRow
vrIpOspfOperStatusEntry = _VrIpOspfOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 105, 1)
)
vrIpOspfOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpOspfIndex"),
)
if mibBuilder.loadTexts:
    vrIpOspfOperStatusEntry.setStatus("mandatory")


class _VrIpOspfSnmpOperStatus_Type(Integer32):
    """Custom type vrIpOspfSnmpOperStatus based on Integer32"""
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


_VrIpOspfSnmpOperStatus_Type.__name__ = "Integer32"
_VrIpOspfSnmpOperStatus_Object = MibTableColumn
vrIpOspfSnmpOperStatus = _VrIpOspfSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 7, 105, 1, 1),
    _VrIpOspfSnmpOperStatus_Type()
)
vrIpOspfSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOspfSnmpOperStatus.setStatus("mandatory")
_VrIpRip_ObjectIdentity = ObjectIdentity
vrIpRip = _VrIpRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8)
)
_VrIpRipRowStatusTable_Object = MibTable
vrIpRipRowStatusTable = _VrIpRipRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 1)
)
if mibBuilder.loadTexts:
    vrIpRipRowStatusTable.setStatus("mandatory")
_VrIpRipRowStatusEntry_Object = MibTableRow
vrIpRipRowStatusEntry = _VrIpRipRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 1, 1)
)
vrIpRipRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRipIndex"),
)
if mibBuilder.loadTexts:
    vrIpRipRowStatusEntry.setStatus("mandatory")
_VrIpRipRowStatus_Type = RowStatus
_VrIpRipRowStatus_Object = MibTableColumn
vrIpRipRowStatus = _VrIpRipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 1, 1, 1),
    _VrIpRipRowStatus_Type()
)
vrIpRipRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipRowStatus.setStatus("mandatory")
_VrIpRipComponentName_Type = DisplayString
_VrIpRipComponentName_Object = MibTableColumn
vrIpRipComponentName = _VrIpRipComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 1, 1, 2),
    _VrIpRipComponentName_Type()
)
vrIpRipComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRipComponentName.setStatus("mandatory")
_VrIpRipStorageType_Type = StorageType
_VrIpRipStorageType_Object = MibTableColumn
vrIpRipStorageType = _VrIpRipStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 1, 1, 4),
    _VrIpRipStorageType_Type()
)
vrIpRipStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRipStorageType.setStatus("mandatory")
_VrIpRipIndex_Type = NonReplicated
_VrIpRipIndex_Object = MibTableColumn
vrIpRipIndex = _VrIpRipIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 1, 1, 10),
    _VrIpRipIndex_Type()
)
vrIpRipIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpRipIndex.setStatus("mandatory")
_VrIpRipImport_ObjectIdentity = ObjectIdentity
vrIpRipImport = _VrIpRipImport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 2)
)
_VrIpRipImportRowStatusTable_Object = MibTable
vrIpRipImportRowStatusTable = _VrIpRipImportRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpRipImportRowStatusTable.setStatus("mandatory")
_VrIpRipImportRowStatusEntry_Object = MibTableRow
vrIpRipImportRowStatusEntry = _VrIpRipImportRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 2, 1, 1)
)
vrIpRipImportRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRipIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRipImportIndex"),
)
if mibBuilder.loadTexts:
    vrIpRipImportRowStatusEntry.setStatus("mandatory")
_VrIpRipImportRowStatus_Type = RowStatus
_VrIpRipImportRowStatus_Object = MibTableColumn
vrIpRipImportRowStatus = _VrIpRipImportRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 2, 1, 1, 1),
    _VrIpRipImportRowStatus_Type()
)
vrIpRipImportRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipImportRowStatus.setStatus("mandatory")
_VrIpRipImportComponentName_Type = DisplayString
_VrIpRipImportComponentName_Object = MibTableColumn
vrIpRipImportComponentName = _VrIpRipImportComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 2, 1, 1, 2),
    _VrIpRipImportComponentName_Type()
)
vrIpRipImportComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRipImportComponentName.setStatus("mandatory")
_VrIpRipImportStorageType_Type = StorageType
_VrIpRipImportStorageType_Object = MibTableColumn
vrIpRipImportStorageType = _VrIpRipImportStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 2, 1, 1, 4),
    _VrIpRipImportStorageType_Type()
)
vrIpRipImportStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRipImportStorageType.setStatus("mandatory")


class _VrIpRipImportIndex_Type(Integer32):
    """Custom type vrIpRipImportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpRipImportIndex_Type.__name__ = "Integer32"
_VrIpRipImportIndex_Object = MibTableColumn
vrIpRipImportIndex = _VrIpRipImportIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 2, 1, 1, 10),
    _VrIpRipImportIndex_Type()
)
vrIpRipImportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpRipImportIndex.setStatus("mandatory")
_VrIpRipImportNet_ObjectIdentity = ObjectIdentity
vrIpRipImportNet = _VrIpRipImportNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 2, 2)
)
_VrIpRipImportNetRowStatusTable_Object = MibTable
vrIpRipImportNetRowStatusTable = _VrIpRipImportNetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpRipImportNetRowStatusTable.setStatus("mandatory")
_VrIpRipImportNetRowStatusEntry_Object = MibTableRow
vrIpRipImportNetRowStatusEntry = _VrIpRipImportNetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 2, 2, 1, 1)
)
vrIpRipImportNetRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRipIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRipImportIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRipImportNetIndex"),
)
if mibBuilder.loadTexts:
    vrIpRipImportNetRowStatusEntry.setStatus("mandatory")
_VrIpRipImportNetRowStatus_Type = RowStatus
_VrIpRipImportNetRowStatus_Object = MibTableColumn
vrIpRipImportNetRowStatus = _VrIpRipImportNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 2, 2, 1, 1, 1),
    _VrIpRipImportNetRowStatus_Type()
)
vrIpRipImportNetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipImportNetRowStatus.setStatus("mandatory")
_VrIpRipImportNetComponentName_Type = DisplayString
_VrIpRipImportNetComponentName_Object = MibTableColumn
vrIpRipImportNetComponentName = _VrIpRipImportNetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 2, 2, 1, 1, 2),
    _VrIpRipImportNetComponentName_Type()
)
vrIpRipImportNetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRipImportNetComponentName.setStatus("mandatory")
_VrIpRipImportNetStorageType_Type = StorageType
_VrIpRipImportNetStorageType_Object = MibTableColumn
vrIpRipImportNetStorageType = _VrIpRipImportNetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 2, 2, 1, 1, 4),
    _VrIpRipImportNetStorageType_Type()
)
vrIpRipImportNetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRipImportNetStorageType.setStatus("mandatory")


class _VrIpRipImportNetIndex_Type(Integer32):
    """Custom type vrIpRipImportNetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpRipImportNetIndex_Type.__name__ = "Integer32"
_VrIpRipImportNetIndex_Object = MibTableColumn
vrIpRipImportNetIndex = _VrIpRipImportNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 2, 2, 1, 1, 10),
    _VrIpRipImportNetIndex_Type()
)
vrIpRipImportNetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpRipImportNetIndex.setStatus("mandatory")
_VrIpRipImportNetProvTable_Object = MibTable
vrIpRipImportNetProvTable = _VrIpRipImportNetProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 2, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpRipImportNetProvTable.setStatus("mandatory")
_VrIpRipImportNetProvEntry_Object = MibTableRow
vrIpRipImportNetProvEntry = _VrIpRipImportNetProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 2, 2, 10, 1)
)
vrIpRipImportNetProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRipIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRipImportIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRipImportNetIndex"),
)
if mibBuilder.loadTexts:
    vrIpRipImportNetProvEntry.setStatus("mandatory")
_VrIpRipImportNetIpAddress_Type = IpAddress
_VrIpRipImportNetIpAddress_Object = MibTableColumn
vrIpRipImportNetIpAddress = _VrIpRipImportNetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 2, 2, 10, 1, 1),
    _VrIpRipImportNetIpAddress_Type()
)
vrIpRipImportNetIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipImportNetIpAddress.setStatus("mandatory")
_VrIpRipImportNetIpMask_Type = IpAddress
_VrIpRipImportNetIpMask_Object = MibTableColumn
vrIpRipImportNetIpMask = _VrIpRipImportNetIpMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 2, 2, 10, 1, 2),
    _VrIpRipImportNetIpMask_Type()
)
vrIpRipImportNetIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipImportNetIpMask.setStatus("mandatory")
_VrIpRipImportProvTable_Object = MibTable
vrIpRipImportProvTable = _VrIpRipImportProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpRipImportProvTable.setStatus("mandatory")
_VrIpRipImportProvEntry_Object = MibTableRow
vrIpRipImportProvEntry = _VrIpRipImportProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 2, 10, 1)
)
vrIpRipImportProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRipIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRipImportIndex"),
)
if mibBuilder.loadTexts:
    vrIpRipImportProvEntry.setStatus("mandatory")


class _VrIpRipImportUsageFlag_Type(Integer32):
    """Custom type vrIpRipImportUsageFlag based on Integer32"""
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


_VrIpRipImportUsageFlag_Type.__name__ = "Integer32"
_VrIpRipImportUsageFlag_Object = MibTableColumn
vrIpRipImportUsageFlag = _VrIpRipImportUsageFlag_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 2, 10, 1, 1),
    _VrIpRipImportUsageFlag_Type()
)
vrIpRipImportUsageFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipImportUsageFlag.setStatus("mandatory")


class _VrIpRipImportImportMetric_Type(Unsigned32):
    """Custom type vrIpRipImportImportMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_VrIpRipImportImportMetric_Type.__name__ = "Unsigned32"
_VrIpRipImportImportMetric_Object = MibTableColumn
vrIpRipImportImportMetric = _VrIpRipImportImportMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 2, 10, 1, 2),
    _VrIpRipImportImportMetric_Type()
)
vrIpRipImportImportMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipImportImportMetric.setStatus("mandatory")


class _VrIpRipImportNeighbor_Type(IpAddress):
    """Custom type vrIpRipImportNeighbor based on IpAddress"""
    defaultHexValue = "00000000"


_VrIpRipImportNeighbor_Object = MibTableColumn
vrIpRipImportNeighbor = _VrIpRipImportNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 2, 10, 1, 3),
    _VrIpRipImportNeighbor_Type()
)
vrIpRipImportNeighbor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipImportNeighbor.setStatus("mandatory")


class _VrIpRipImportInterface_Type(IpAddress):
    """Custom type vrIpRipImportInterface based on IpAddress"""
    defaultHexValue = "00000000"


_VrIpRipImportInterface_Object = MibTableColumn
vrIpRipImportInterface = _VrIpRipImportInterface_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 2, 10, 1, 4),
    _VrIpRipImportInterface_Type()
)
vrIpRipImportInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipImportInterface.setStatus("mandatory")
_VrIpRipExport_ObjectIdentity = ObjectIdentity
vrIpRipExport = _VrIpRipExport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3)
)
_VrIpRipExportRowStatusTable_Object = MibTable
vrIpRipExportRowStatusTable = _VrIpRipExportRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 1)
)
if mibBuilder.loadTexts:
    vrIpRipExportRowStatusTable.setStatus("mandatory")
_VrIpRipExportRowStatusEntry_Object = MibTableRow
vrIpRipExportRowStatusEntry = _VrIpRipExportRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 1, 1)
)
vrIpRipExportRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRipIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRipExportIndex"),
)
if mibBuilder.loadTexts:
    vrIpRipExportRowStatusEntry.setStatus("mandatory")
_VrIpRipExportRowStatus_Type = RowStatus
_VrIpRipExportRowStatus_Object = MibTableColumn
vrIpRipExportRowStatus = _VrIpRipExportRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 1, 1, 1),
    _VrIpRipExportRowStatus_Type()
)
vrIpRipExportRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipExportRowStatus.setStatus("mandatory")
_VrIpRipExportComponentName_Type = DisplayString
_VrIpRipExportComponentName_Object = MibTableColumn
vrIpRipExportComponentName = _VrIpRipExportComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 1, 1, 2),
    _VrIpRipExportComponentName_Type()
)
vrIpRipExportComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRipExportComponentName.setStatus("mandatory")
_VrIpRipExportStorageType_Type = StorageType
_VrIpRipExportStorageType_Object = MibTableColumn
vrIpRipExportStorageType = _VrIpRipExportStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 1, 1, 4),
    _VrIpRipExportStorageType_Type()
)
vrIpRipExportStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRipExportStorageType.setStatus("mandatory")


class _VrIpRipExportIndex_Type(Integer32):
    """Custom type vrIpRipExportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpRipExportIndex_Type.__name__ = "Integer32"
_VrIpRipExportIndex_Object = MibTableColumn
vrIpRipExportIndex = _VrIpRipExportIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 1, 1, 10),
    _VrIpRipExportIndex_Type()
)
vrIpRipExportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpRipExportIndex.setStatus("mandatory")
_VrIpRipExportNet_ObjectIdentity = ObjectIdentity
vrIpRipExportNet = _VrIpRipExportNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 2)
)
_VrIpRipExportNetRowStatusTable_Object = MibTable
vrIpRipExportNetRowStatusTable = _VrIpRipExportNetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpRipExportNetRowStatusTable.setStatus("mandatory")
_VrIpRipExportNetRowStatusEntry_Object = MibTableRow
vrIpRipExportNetRowStatusEntry = _VrIpRipExportNetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 2, 1, 1)
)
vrIpRipExportNetRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRipIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRipExportIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRipExportNetIndex"),
)
if mibBuilder.loadTexts:
    vrIpRipExportNetRowStatusEntry.setStatus("mandatory")
_VrIpRipExportNetRowStatus_Type = RowStatus
_VrIpRipExportNetRowStatus_Object = MibTableColumn
vrIpRipExportNetRowStatus = _VrIpRipExportNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 2, 1, 1, 1),
    _VrIpRipExportNetRowStatus_Type()
)
vrIpRipExportNetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipExportNetRowStatus.setStatus("mandatory")
_VrIpRipExportNetComponentName_Type = DisplayString
_VrIpRipExportNetComponentName_Object = MibTableColumn
vrIpRipExportNetComponentName = _VrIpRipExportNetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 2, 1, 1, 2),
    _VrIpRipExportNetComponentName_Type()
)
vrIpRipExportNetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRipExportNetComponentName.setStatus("mandatory")
_VrIpRipExportNetStorageType_Type = StorageType
_VrIpRipExportNetStorageType_Object = MibTableColumn
vrIpRipExportNetStorageType = _VrIpRipExportNetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 2, 1, 1, 4),
    _VrIpRipExportNetStorageType_Type()
)
vrIpRipExportNetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRipExportNetStorageType.setStatus("mandatory")


class _VrIpRipExportNetIndex_Type(Integer32):
    """Custom type vrIpRipExportNetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpRipExportNetIndex_Type.__name__ = "Integer32"
_VrIpRipExportNetIndex_Object = MibTableColumn
vrIpRipExportNetIndex = _VrIpRipExportNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 2, 1, 1, 10),
    _VrIpRipExportNetIndex_Type()
)
vrIpRipExportNetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpRipExportNetIndex.setStatus("mandatory")
_VrIpRipExportNetProvTable_Object = MibTable
vrIpRipExportNetProvTable = _VrIpRipExportNetProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpRipExportNetProvTable.setStatus("mandatory")
_VrIpRipExportNetProvEntry_Object = MibTableRow
vrIpRipExportNetProvEntry = _VrIpRipExportNetProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 2, 10, 1)
)
vrIpRipExportNetProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRipIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRipExportIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRipExportNetIndex"),
)
if mibBuilder.loadTexts:
    vrIpRipExportNetProvEntry.setStatus("mandatory")
_VrIpRipExportNetIpAddress_Type = IpAddress
_VrIpRipExportNetIpAddress_Object = MibTableColumn
vrIpRipExportNetIpAddress = _VrIpRipExportNetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 2, 10, 1, 1),
    _VrIpRipExportNetIpAddress_Type()
)
vrIpRipExportNetIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipExportNetIpAddress.setStatus("mandatory")
_VrIpRipExportNetIpMask_Type = IpAddress
_VrIpRipExportNetIpMask_Object = MibTableColumn
vrIpRipExportNetIpMask = _VrIpRipExportNetIpMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 2, 10, 1, 2),
    _VrIpRipExportNetIpMask_Type()
)
vrIpRipExportNetIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipExportNetIpMask.setStatus("mandatory")
_VrIpRipExportProvTable_Object = MibTable
vrIpRipExportProvTable = _VrIpRipExportProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 10)
)
if mibBuilder.loadTexts:
    vrIpRipExportProvTable.setStatus("mandatory")
_VrIpRipExportProvEntry_Object = MibTableRow
vrIpRipExportProvEntry = _VrIpRipExportProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 10, 1)
)
vrIpRipExportProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRipIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRipExportIndex"),
)
if mibBuilder.loadTexts:
    vrIpRipExportProvEntry.setStatus("mandatory")


class _VrIpRipExportAdvertiseStatus_Type(Integer32):
    """Custom type vrIpRipExportAdvertiseStatus based on Integer32"""
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


_VrIpRipExportAdvertiseStatus_Type.__name__ = "Integer32"
_VrIpRipExportAdvertiseStatus_Object = MibTableColumn
vrIpRipExportAdvertiseStatus = _VrIpRipExportAdvertiseStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 10, 1, 1),
    _VrIpRipExportAdvertiseStatus_Type()
)
vrIpRipExportAdvertiseStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipExportAdvertiseStatus.setStatus("mandatory")


class _VrIpRipExportExportMetric_Type(Unsigned32):
    """Custom type vrIpRipExportExportMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_VrIpRipExportExportMetric_Type.__name__ = "Unsigned32"
_VrIpRipExportExportMetric_Object = MibTableColumn
vrIpRipExportExportMetric = _VrIpRipExportExportMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 10, 1, 2),
    _VrIpRipExportExportMetric_Type()
)
vrIpRipExportExportMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipExportExportMetric.setStatus("mandatory")


class _VrIpRipExportProtocol_Type(Integer32):
    """Custom type vrIpRipExportProtocol based on Integer32"""
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


_VrIpRipExportProtocol_Type.__name__ = "Integer32"
_VrIpRipExportProtocol_Object = MibTableColumn
vrIpRipExportProtocol = _VrIpRipExportProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 10, 1, 3),
    _VrIpRipExportProtocol_Type()
)
vrIpRipExportProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipExportProtocol.setStatus("mandatory")


class _VrIpRipExportRipInterface_Type(IpAddress):
    """Custom type vrIpRipExportRipInterface based on IpAddress"""
    defaultHexValue = "00000000"


_VrIpRipExportRipInterface_Object = MibTableColumn
vrIpRipExportRipInterface = _VrIpRipExportRipInterface_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 10, 1, 4),
    _VrIpRipExportRipInterface_Type()
)
vrIpRipExportRipInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipExportRipInterface.setStatus("mandatory")


class _VrIpRipExportEgpAsId_Type(Unsigned32):
    """Custom type vrIpRipExportEgpAsId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_VrIpRipExportEgpAsId_Type.__name__ = "Unsigned32"
_VrIpRipExportEgpAsId_Object = MibTableColumn
vrIpRipExportEgpAsId = _VrIpRipExportEgpAsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 10, 1, 5),
    _VrIpRipExportEgpAsId_Type()
)
vrIpRipExportEgpAsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipExportEgpAsId.setStatus("mandatory")


class _VrIpRipExportOspfTag_Type(Unsigned32):
    """Custom type vrIpRipExportOspfTag based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpRipExportOspfTag_Type.__name__ = "Unsigned32"
_VrIpRipExportOspfTag_Object = MibTableColumn
vrIpRipExportOspfTag = _VrIpRipExportOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 10, 1, 6),
    _VrIpRipExportOspfTag_Type()
)
vrIpRipExportOspfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipExportOspfTag.setStatus("mandatory")


class _VrIpRipExportOutInterface_Type(IpAddress):
    """Custom type vrIpRipExportOutInterface based on IpAddress"""
    defaultHexValue = "00000000"


_VrIpRipExportOutInterface_Object = MibTableColumn
vrIpRipExportOutInterface = _VrIpRipExportOutInterface_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 10, 1, 7),
    _VrIpRipExportOutInterface_Type()
)
vrIpRipExportOutInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipExportOutInterface.setStatus("mandatory")


class _VrIpRipExportBgpAsId_Type(Unsigned32):
    """Custom type vrIpRipExportBgpAsId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpRipExportBgpAsId_Type.__name__ = "Unsigned32"
_VrIpRipExportBgpAsId_Object = MibTableColumn
vrIpRipExportBgpAsId = _VrIpRipExportBgpAsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 3, 10, 1, 8),
    _VrIpRipExportBgpAsId_Type()
)
vrIpRipExportBgpAsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipExportBgpAsId.setStatus("mandatory")
_VrIpRipProvTable_Object = MibTable
vrIpRipProvTable = _VrIpRipProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 10)
)
if mibBuilder.loadTexts:
    vrIpRipProvTable.setStatus("mandatory")
_VrIpRipProvEntry_Object = MibTableRow
vrIpRipProvEntry = _VrIpRipProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 10, 1)
)
vrIpRipProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRipIndex"),
)
if mibBuilder.loadTexts:
    vrIpRipProvEntry.setStatus("mandatory")


class _VrIpRipMigrateRip_Type(Integer32):
    """Custom type vrIpRipMigrateRip based on Integer32"""
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


_VrIpRipMigrateRip_Type.__name__ = "Integer32"
_VrIpRipMigrateRip_Object = MibTableColumn
vrIpRipMigrateRip = _VrIpRipMigrateRip_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 10, 1, 2),
    _VrIpRipMigrateRip_Type()
)
vrIpRipMigrateRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipMigrateRip.setStatus("mandatory")


class _VrIpRipRfc1058MetricUsage_Type(Integer32):
    """Custom type vrIpRipRfc1058MetricUsage based on Integer32"""
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


_VrIpRipRfc1058MetricUsage_Type.__name__ = "Integer32"
_VrIpRipRfc1058MetricUsage_Object = MibTableColumn
vrIpRipRfc1058MetricUsage = _VrIpRipRfc1058MetricUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 10, 1, 3),
    _VrIpRipRfc1058MetricUsage_Type()
)
vrIpRipRfc1058MetricUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipRfc1058MetricUsage.setStatus("mandatory")


class _VrIpRipGenerateDiscardRoute_Type(Integer32):
    """Custom type vrIpRipGenerateDiscardRoute based on Integer32"""
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


_VrIpRipGenerateDiscardRoute_Type.__name__ = "Integer32"
_VrIpRipGenerateDiscardRoute_Object = MibTableColumn
vrIpRipGenerateDiscardRoute = _VrIpRipGenerateDiscardRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 10, 1, 4),
    _VrIpRipGenerateDiscardRoute_Type()
)
vrIpRipGenerateDiscardRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipGenerateDiscardRoute.setStatus("mandatory")


class _VrIpRipRipUpdate_Type(Integer32):
    """Custom type vrIpRipRipUpdate based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 500),
    )


_VrIpRipRipUpdate_Type.__name__ = "Integer32"
_VrIpRipRipUpdate_Object = MibTableColumn
vrIpRipRipUpdate = _VrIpRipRipUpdate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 10, 1, 5),
    _VrIpRipRipUpdate_Type()
)
vrIpRipRipUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipRipUpdate.setStatus("mandatory")


class _VrIpRipRipTimeout_Type(Integer32):
    """Custom type vrIpRipRipTimeout based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 500),
    )


_VrIpRipRipTimeout_Type.__name__ = "Integer32"
_VrIpRipRipTimeout_Object = MibTableColumn
vrIpRipRipTimeout = _VrIpRipRipTimeout_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 10, 1, 6),
    _VrIpRipRipTimeout_Type()
)
vrIpRipRipTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipRipTimeout.setStatus("mandatory")


class _VrIpRipGarbageCollectTimer_Type(Integer32):
    """Custom type vrIpRipGarbageCollectTimer based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 500),
    )


_VrIpRipGarbageCollectTimer_Type.__name__ = "Integer32"
_VrIpRipGarbageCollectTimer_Object = MibTableColumn
vrIpRipGarbageCollectTimer = _VrIpRipGarbageCollectTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 10, 1, 7),
    _VrIpRipGarbageCollectTimer_Type()
)
vrIpRipGarbageCollectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipGarbageCollectTimer.setStatus("mandatory")
_VrIpRipStateTable_Object = MibTable
vrIpRipStateTable = _VrIpRipStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 11)
)
if mibBuilder.loadTexts:
    vrIpRipStateTable.setStatus("mandatory")
_VrIpRipStateEntry_Object = MibTableRow
vrIpRipStateEntry = _VrIpRipStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 11, 1)
)
vrIpRipStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRipIndex"),
)
if mibBuilder.loadTexts:
    vrIpRipStateEntry.setStatus("mandatory")


class _VrIpRipAdminState_Type(Integer32):
    """Custom type vrIpRipAdminState based on Integer32"""
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


_VrIpRipAdminState_Type.__name__ = "Integer32"
_VrIpRipAdminState_Object = MibTableColumn
vrIpRipAdminState = _VrIpRipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 11, 1, 1),
    _VrIpRipAdminState_Type()
)
vrIpRipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRipAdminState.setStatus("mandatory")


class _VrIpRipOperationalState_Type(Integer32):
    """Custom type vrIpRipOperationalState based on Integer32"""
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


_VrIpRipOperationalState_Type.__name__ = "Integer32"
_VrIpRipOperationalState_Object = MibTableColumn
vrIpRipOperationalState = _VrIpRipOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 11, 1, 2),
    _VrIpRipOperationalState_Type()
)
vrIpRipOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRipOperationalState.setStatus("mandatory")


class _VrIpRipUsageState_Type(Integer32):
    """Custom type vrIpRipUsageState based on Integer32"""
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


_VrIpRipUsageState_Type.__name__ = "Integer32"
_VrIpRipUsageState_Object = MibTableColumn
vrIpRipUsageState = _VrIpRipUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 11, 1, 3),
    _VrIpRipUsageState_Type()
)
vrIpRipUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRipUsageState.setStatus("mandatory")
_VrIpRipAdminControlTable_Object = MibTable
vrIpRipAdminControlTable = _VrIpRipAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 12)
)
if mibBuilder.loadTexts:
    vrIpRipAdminControlTable.setStatus("mandatory")
_VrIpRipAdminControlEntry_Object = MibTableRow
vrIpRipAdminControlEntry = _VrIpRipAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 12, 1)
)
vrIpRipAdminControlEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRipIndex"),
)
if mibBuilder.loadTexts:
    vrIpRipAdminControlEntry.setStatus("mandatory")


class _VrIpRipSnmpAdminStatus_Type(Integer32):
    """Custom type vrIpRipSnmpAdminStatus based on Integer32"""
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


_VrIpRipSnmpAdminStatus_Type.__name__ = "Integer32"
_VrIpRipSnmpAdminStatus_Object = MibTableColumn
vrIpRipSnmpAdminStatus = _VrIpRipSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 12, 1, 1),
    _VrIpRipSnmpAdminStatus_Type()
)
vrIpRipSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRipSnmpAdminStatus.setStatus("mandatory")
_VrIpRipOperStatusTable_Object = MibTable
vrIpRipOperStatusTable = _VrIpRipOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 15)
)
if mibBuilder.loadTexts:
    vrIpRipOperStatusTable.setStatus("mandatory")
_VrIpRipOperStatusEntry_Object = MibTableRow
vrIpRipOperStatusEntry = _VrIpRipOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 15, 1)
)
vrIpRipOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRipIndex"),
)
if mibBuilder.loadTexts:
    vrIpRipOperStatusEntry.setStatus("mandatory")


class _VrIpRipSnmpOperStatus_Type(Integer32):
    """Custom type vrIpRipSnmpOperStatus based on Integer32"""
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


_VrIpRipSnmpOperStatus_Type.__name__ = "Integer32"
_VrIpRipSnmpOperStatus_Object = MibTableColumn
vrIpRipSnmpOperStatus = _VrIpRipSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 15, 1, 1),
    _VrIpRipSnmpOperStatus_Type()
)
vrIpRipSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRipSnmpOperStatus.setStatus("mandatory")
_VrIpRipOperTable_Object = MibTable
vrIpRipOperTable = _VrIpRipOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 16)
)
if mibBuilder.loadTexts:
    vrIpRipOperTable.setStatus("mandatory")
_VrIpRipOperEntry_Object = MibTableRow
vrIpRipOperEntry = _VrIpRipOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 16, 1)
)
vrIpRipOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRipIndex"),
)
if mibBuilder.loadTexts:
    vrIpRipOperEntry.setStatus("mandatory")
_VrIpRipRouteChangesMade_Type = Counter32
_VrIpRipRouteChangesMade_Object = MibTableColumn
vrIpRipRouteChangesMade = _VrIpRipRouteChangesMade_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 16, 1, 1),
    _VrIpRipRouteChangesMade_Type()
)
vrIpRipRouteChangesMade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRipRouteChangesMade.setStatus("mandatory")
_VrIpRipQueryResponses_Type = Counter32
_VrIpRipQueryResponses_Object = MibTableColumn
vrIpRipQueryResponses = _VrIpRipQueryResponses_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 8, 16, 1, 2),
    _VrIpRipQueryResponses_Type()
)
vrIpRipQueryResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRipQueryResponses.setStatus("mandatory")
_VrIpStatic_ObjectIdentity = ObjectIdentity
vrIpStatic = _VrIpStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9)
)
_VrIpStaticRowStatusTable_Object = MibTable
vrIpStaticRowStatusTable = _VrIpStaticRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 1)
)
if mibBuilder.loadTexts:
    vrIpStaticRowStatusTable.setStatus("mandatory")
_VrIpStaticRowStatusEntry_Object = MibTableRow
vrIpStaticRowStatusEntry = _VrIpStaticRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 1, 1)
)
vrIpStaticRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpStaticIndex"),
)
if mibBuilder.loadTexts:
    vrIpStaticRowStatusEntry.setStatus("mandatory")
_VrIpStaticRowStatus_Type = RowStatus
_VrIpStaticRowStatus_Object = MibTableColumn
vrIpStaticRowStatus = _VrIpStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 1, 1, 1),
    _VrIpStaticRowStatus_Type()
)
vrIpStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpStaticRowStatus.setStatus("mandatory")
_VrIpStaticComponentName_Type = DisplayString
_VrIpStaticComponentName_Object = MibTableColumn
vrIpStaticComponentName = _VrIpStaticComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 1, 1, 2),
    _VrIpStaticComponentName_Type()
)
vrIpStaticComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpStaticComponentName.setStatus("mandatory")
_VrIpStaticStorageType_Type = StorageType
_VrIpStaticStorageType_Object = MibTableColumn
vrIpStaticStorageType = _VrIpStaticStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 1, 1, 4),
    _VrIpStaticStorageType_Type()
)
vrIpStaticStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpStaticStorageType.setStatus("mandatory")
_VrIpStaticIndex_Type = NonReplicated
_VrIpStaticIndex_Object = MibTableColumn
vrIpStaticIndex = _VrIpStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 1, 1, 10),
    _VrIpStaticIndex_Type()
)
vrIpStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpStaticIndex.setStatus("mandatory")
_VrIpStaticRoute_ObjectIdentity = ObjectIdentity
vrIpStaticRoute = _VrIpStaticRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 2)
)
_VrIpStaticRouteRowStatusTable_Object = MibTable
vrIpStaticRouteRowStatusTable = _VrIpStaticRouteRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpStaticRouteRowStatusTable.setStatus("mandatory")
_VrIpStaticRouteRowStatusEntry_Object = MibTableRow
vrIpStaticRouteRowStatusEntry = _VrIpStaticRouteRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 2, 1, 1)
)
vrIpStaticRouteRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpStaticIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpStaticRouteDestAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpStaticRouteDestMaskIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpStaticRouteTypeOfServiceIndex"),
)
if mibBuilder.loadTexts:
    vrIpStaticRouteRowStatusEntry.setStatus("mandatory")
_VrIpStaticRouteRowStatus_Type = RowStatus
_VrIpStaticRouteRowStatus_Object = MibTableColumn
vrIpStaticRouteRowStatus = _VrIpStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 2, 1, 1, 1),
    _VrIpStaticRouteRowStatus_Type()
)
vrIpStaticRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpStaticRouteRowStatus.setStatus("mandatory")
_VrIpStaticRouteComponentName_Type = DisplayString
_VrIpStaticRouteComponentName_Object = MibTableColumn
vrIpStaticRouteComponentName = _VrIpStaticRouteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 2, 1, 1, 2),
    _VrIpStaticRouteComponentName_Type()
)
vrIpStaticRouteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpStaticRouteComponentName.setStatus("mandatory")
_VrIpStaticRouteStorageType_Type = StorageType
_VrIpStaticRouteStorageType_Object = MibTableColumn
vrIpStaticRouteStorageType = _VrIpStaticRouteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 2, 1, 1, 4),
    _VrIpStaticRouteStorageType_Type()
)
vrIpStaticRouteStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpStaticRouteStorageType.setStatus("mandatory")
_VrIpStaticRouteDestAddressIndex_Type = IpAddress
_VrIpStaticRouteDestAddressIndex_Object = MibTableColumn
vrIpStaticRouteDestAddressIndex = _VrIpStaticRouteDestAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 2, 1, 1, 10),
    _VrIpStaticRouteDestAddressIndex_Type()
)
vrIpStaticRouteDestAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpStaticRouteDestAddressIndex.setStatus("mandatory")
_VrIpStaticRouteDestMaskIndex_Type = IpAddress
_VrIpStaticRouteDestMaskIndex_Object = MibTableColumn
vrIpStaticRouteDestMaskIndex = _VrIpStaticRouteDestMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 2, 1, 1, 11),
    _VrIpStaticRouteDestMaskIndex_Type()
)
vrIpStaticRouteDestMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpStaticRouteDestMaskIndex.setStatus("mandatory")


class _VrIpStaticRouteTypeOfServiceIndex_Type(Integer32):
    """Custom type vrIpStaticRouteTypeOfServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_VrIpStaticRouteTypeOfServiceIndex_Type.__name__ = "Integer32"
_VrIpStaticRouteTypeOfServiceIndex_Object = MibTableColumn
vrIpStaticRouteTypeOfServiceIndex = _VrIpStaticRouteTypeOfServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 2, 1, 1, 12),
    _VrIpStaticRouteTypeOfServiceIndex_Type()
)
vrIpStaticRouteTypeOfServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpStaticRouteTypeOfServiceIndex.setStatus("mandatory")
_VrIpStaticRouteNh_ObjectIdentity = ObjectIdentity
vrIpStaticRouteNh = _VrIpStaticRouteNh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 2, 2)
)
_VrIpStaticRouteNhRowStatusTable_Object = MibTable
vrIpStaticRouteNhRowStatusTable = _VrIpStaticRouteNhRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpStaticRouteNhRowStatusTable.setStatus("mandatory")
_VrIpStaticRouteNhRowStatusEntry_Object = MibTableRow
vrIpStaticRouteNhRowStatusEntry = _VrIpStaticRouteNhRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 2, 2, 1, 1)
)
vrIpStaticRouteNhRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpStaticIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpStaticRouteDestAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpStaticRouteDestMaskIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpStaticRouteTypeOfServiceIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpStaticRouteNhIndex"),
)
if mibBuilder.loadTexts:
    vrIpStaticRouteNhRowStatusEntry.setStatus("mandatory")
_VrIpStaticRouteNhRowStatus_Type = RowStatus
_VrIpStaticRouteNhRowStatus_Object = MibTableColumn
vrIpStaticRouteNhRowStatus = _VrIpStaticRouteNhRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 2, 2, 1, 1, 1),
    _VrIpStaticRouteNhRowStatus_Type()
)
vrIpStaticRouteNhRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpStaticRouteNhRowStatus.setStatus("mandatory")
_VrIpStaticRouteNhComponentName_Type = DisplayString
_VrIpStaticRouteNhComponentName_Object = MibTableColumn
vrIpStaticRouteNhComponentName = _VrIpStaticRouteNhComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 2, 2, 1, 1, 2),
    _VrIpStaticRouteNhComponentName_Type()
)
vrIpStaticRouteNhComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpStaticRouteNhComponentName.setStatus("mandatory")
_VrIpStaticRouteNhStorageType_Type = StorageType
_VrIpStaticRouteNhStorageType_Object = MibTableColumn
vrIpStaticRouteNhStorageType = _VrIpStaticRouteNhStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 2, 2, 1, 1, 4),
    _VrIpStaticRouteNhStorageType_Type()
)
vrIpStaticRouteNhStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpStaticRouteNhStorageType.setStatus("mandatory")
_VrIpStaticRouteNhIndex_Type = IpAddress
_VrIpStaticRouteNhIndex_Object = MibTableColumn
vrIpStaticRouteNhIndex = _VrIpStaticRouteNhIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 2, 2, 1, 1, 10),
    _VrIpStaticRouteNhIndex_Type()
)
vrIpStaticRouteNhIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpStaticRouteNhIndex.setStatus("mandatory")
_VrIpStaticRouteNhProvTable_Object = MibTable
vrIpStaticRouteNhProvTable = _VrIpStaticRouteNhProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 2, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpStaticRouteNhProvTable.setStatus("mandatory")
_VrIpStaticRouteNhProvEntry_Object = MibTableRow
vrIpStaticRouteNhProvEntry = _VrIpStaticRouteNhProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 2, 2, 10, 1)
)
vrIpStaticRouteNhProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpStaticIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpStaticRouteDestAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpStaticRouteDestMaskIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpStaticRouteTypeOfServiceIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpStaticRouteNhIndex"),
)
if mibBuilder.loadTexts:
    vrIpStaticRouteNhProvEntry.setStatus("mandatory")


class _VrIpStaticRouteNhMetric_Type(Integer32):
    """Custom type vrIpStaticRouteNhMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_VrIpStaticRouteNhMetric_Type.__name__ = "Integer32"
_VrIpStaticRouteNhMetric_Object = MibTableColumn
vrIpStaticRouteNhMetric = _VrIpStaticRouteNhMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 2, 2, 10, 1, 1),
    _VrIpStaticRouteNhMetric_Type()
)
vrIpStaticRouteNhMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpStaticRouteNhMetric.setStatus("mandatory")
_VrIpStaticRouteProvTable_Object = MibTable
vrIpStaticRouteProvTable = _VrIpStaticRouteProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpStaticRouteProvTable.setStatus("mandatory")
_VrIpStaticRouteProvEntry_Object = MibTableRow
vrIpStaticRouteProvEntry = _VrIpStaticRouteProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 2, 10, 1)
)
vrIpStaticRouteProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpStaticIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpStaticRouteDestAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpStaticRouteDestMaskIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpStaticRouteTypeOfServiceIndex"),
)
if mibBuilder.loadTexts:
    vrIpStaticRouteProvEntry.setStatus("mandatory")


class _VrIpStaticRoutePreferredOver_Type(Integer32):
    """Custom type vrIpStaticRoutePreferredOver based on Integer32"""
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


_VrIpStaticRoutePreferredOver_Type.__name__ = "Integer32"
_VrIpStaticRoutePreferredOver_Object = MibTableColumn
vrIpStaticRoutePreferredOver = _VrIpStaticRoutePreferredOver_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 2, 10, 1, 12),
    _VrIpStaticRoutePreferredOver_Type()
)
vrIpStaticRoutePreferredOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpStaticRoutePreferredOver.setStatus("mandatory")
_VrIpStaticDiscard_ObjectIdentity = ObjectIdentity
vrIpStaticDiscard = _VrIpStaticDiscard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 3)
)
_VrIpStaticDiscardRowStatusTable_Object = MibTable
vrIpStaticDiscardRowStatusTable = _VrIpStaticDiscardRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 3, 1)
)
if mibBuilder.loadTexts:
    vrIpStaticDiscardRowStatusTable.setStatus("mandatory")
_VrIpStaticDiscardRowStatusEntry_Object = MibTableRow
vrIpStaticDiscardRowStatusEntry = _VrIpStaticDiscardRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 3, 1, 1)
)
vrIpStaticDiscardRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpStaticIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpStaticDiscardDestAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpStaticDiscardDestMaskIndex"),
)
if mibBuilder.loadTexts:
    vrIpStaticDiscardRowStatusEntry.setStatus("mandatory")
_VrIpStaticDiscardRowStatus_Type = RowStatus
_VrIpStaticDiscardRowStatus_Object = MibTableColumn
vrIpStaticDiscardRowStatus = _VrIpStaticDiscardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 3, 1, 1, 1),
    _VrIpStaticDiscardRowStatus_Type()
)
vrIpStaticDiscardRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpStaticDiscardRowStatus.setStatus("mandatory")
_VrIpStaticDiscardComponentName_Type = DisplayString
_VrIpStaticDiscardComponentName_Object = MibTableColumn
vrIpStaticDiscardComponentName = _VrIpStaticDiscardComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 3, 1, 1, 2),
    _VrIpStaticDiscardComponentName_Type()
)
vrIpStaticDiscardComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpStaticDiscardComponentName.setStatus("mandatory")
_VrIpStaticDiscardStorageType_Type = StorageType
_VrIpStaticDiscardStorageType_Object = MibTableColumn
vrIpStaticDiscardStorageType = _VrIpStaticDiscardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 3, 1, 1, 4),
    _VrIpStaticDiscardStorageType_Type()
)
vrIpStaticDiscardStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpStaticDiscardStorageType.setStatus("mandatory")
_VrIpStaticDiscardDestAddressIndex_Type = IpAddress
_VrIpStaticDiscardDestAddressIndex_Object = MibTableColumn
vrIpStaticDiscardDestAddressIndex = _VrIpStaticDiscardDestAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 3, 1, 1, 10),
    _VrIpStaticDiscardDestAddressIndex_Type()
)
vrIpStaticDiscardDestAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpStaticDiscardDestAddressIndex.setStatus("mandatory")
_VrIpStaticDiscardDestMaskIndex_Type = IpAddress
_VrIpStaticDiscardDestMaskIndex_Object = MibTableColumn
vrIpStaticDiscardDestMaskIndex = _VrIpStaticDiscardDestMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 3, 1, 1, 11),
    _VrIpStaticDiscardDestMaskIndex_Type()
)
vrIpStaticDiscardDestMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpStaticDiscardDestMaskIndex.setStatus("mandatory")
_VrIpStaticStateTable_Object = MibTable
vrIpStaticStateTable = _VrIpStaticStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 10)
)
if mibBuilder.loadTexts:
    vrIpStaticStateTable.setStatus("mandatory")
_VrIpStaticStateEntry_Object = MibTableRow
vrIpStaticStateEntry = _VrIpStaticStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 10, 1)
)
vrIpStaticStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpStaticIndex"),
)
if mibBuilder.loadTexts:
    vrIpStaticStateEntry.setStatus("mandatory")


class _VrIpStaticAdminState_Type(Integer32):
    """Custom type vrIpStaticAdminState based on Integer32"""
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


_VrIpStaticAdminState_Type.__name__ = "Integer32"
_VrIpStaticAdminState_Object = MibTableColumn
vrIpStaticAdminState = _VrIpStaticAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 10, 1, 1),
    _VrIpStaticAdminState_Type()
)
vrIpStaticAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpStaticAdminState.setStatus("mandatory")


class _VrIpStaticOperationalState_Type(Integer32):
    """Custom type vrIpStaticOperationalState based on Integer32"""
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


_VrIpStaticOperationalState_Type.__name__ = "Integer32"
_VrIpStaticOperationalState_Object = MibTableColumn
vrIpStaticOperationalState = _VrIpStaticOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 10, 1, 2),
    _VrIpStaticOperationalState_Type()
)
vrIpStaticOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpStaticOperationalState.setStatus("mandatory")


class _VrIpStaticUsageState_Type(Integer32):
    """Custom type vrIpStaticUsageState based on Integer32"""
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


_VrIpStaticUsageState_Type.__name__ = "Integer32"
_VrIpStaticUsageState_Object = MibTableColumn
vrIpStaticUsageState = _VrIpStaticUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 9, 10, 1, 3),
    _VrIpStaticUsageState_Type()
)
vrIpStaticUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpStaticUsageState.setStatus("mandatory")
_VrIpNs_ObjectIdentity = ObjectIdentity
vrIpNs = _VrIpNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10)
)
_VrIpNsRowStatusTable_Object = MibTable
vrIpNsRowStatusTable = _VrIpNsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 1)
)
if mibBuilder.loadTexts:
    vrIpNsRowStatusTable.setStatus("mandatory")
_VrIpNsRowStatusEntry_Object = MibTableRow
vrIpNsRowStatusEntry = _VrIpNsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 1, 1)
)
vrIpNsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpNsIndex"),
)
if mibBuilder.loadTexts:
    vrIpNsRowStatusEntry.setStatus("mandatory")
_VrIpNsRowStatus_Type = RowStatus
_VrIpNsRowStatus_Object = MibTableColumn
vrIpNsRowStatus = _VrIpNsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 1, 1, 1),
    _VrIpNsRowStatus_Type()
)
vrIpNsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNsRowStatus.setStatus("mandatory")
_VrIpNsComponentName_Type = DisplayString
_VrIpNsComponentName_Object = MibTableColumn
vrIpNsComponentName = _VrIpNsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 1, 1, 2),
    _VrIpNsComponentName_Type()
)
vrIpNsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNsComponentName.setStatus("mandatory")
_VrIpNsStorageType_Type = StorageType
_VrIpNsStorageType_Object = MibTableColumn
vrIpNsStorageType = _VrIpNsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 1, 1, 4),
    _VrIpNsStorageType_Type()
)
vrIpNsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNsStorageType.setStatus("mandatory")
_VrIpNsIndex_Type = NonReplicated
_VrIpNsIndex_Object = MibTableColumn
vrIpNsIndex = _VrIpNsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 1, 1, 10),
    _VrIpNsIndex_Type()
)
vrIpNsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpNsIndex.setStatus("mandatory")
_VrIpNsApply_ObjectIdentity = ObjectIdentity
vrIpNsApply = _VrIpNsApply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 2)
)
_VrIpNsApplyRowStatusTable_Object = MibTable
vrIpNsApplyRowStatusTable = _VrIpNsApplyRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpNsApplyRowStatusTable.setStatus("mandatory")
_VrIpNsApplyRowStatusEntry_Object = MibTableRow
vrIpNsApplyRowStatusEntry = _VrIpNsApplyRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 2, 1, 1)
)
vrIpNsApplyRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpNsIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpNsApplyIndex"),
)
if mibBuilder.loadTexts:
    vrIpNsApplyRowStatusEntry.setStatus("mandatory")
_VrIpNsApplyRowStatus_Type = RowStatus
_VrIpNsApplyRowStatus_Object = MibTableColumn
vrIpNsApplyRowStatus = _VrIpNsApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 2, 1, 1, 1),
    _VrIpNsApplyRowStatus_Type()
)
vrIpNsApplyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNsApplyRowStatus.setStatus("mandatory")
_VrIpNsApplyComponentName_Type = DisplayString
_VrIpNsApplyComponentName_Object = MibTableColumn
vrIpNsApplyComponentName = _VrIpNsApplyComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 2, 1, 1, 2),
    _VrIpNsApplyComponentName_Type()
)
vrIpNsApplyComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNsApplyComponentName.setStatus("mandatory")
_VrIpNsApplyStorageType_Type = StorageType
_VrIpNsApplyStorageType_Object = MibTableColumn
vrIpNsApplyStorageType = _VrIpNsApplyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 2, 1, 1, 4),
    _VrIpNsApplyStorageType_Type()
)
vrIpNsApplyStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpNsApplyStorageType.setStatus("mandatory")


class _VrIpNsApplyIndex_Type(Integer32):
    """Custom type vrIpNsApplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrIpNsApplyIndex_Type.__name__ = "Integer32"
_VrIpNsApplyIndex_Object = MibTableColumn
vrIpNsApplyIndex = _VrIpNsApplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 2, 1, 1, 10),
    _VrIpNsApplyIndex_Type()
)
vrIpNsApplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpNsApplyIndex.setStatus("mandatory")
_VrIpNsApplyProvisionedTable_Object = MibTable
vrIpNsApplyProvisionedTable = _VrIpNsApplyProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpNsApplyProvisionedTable.setStatus("mandatory")
_VrIpNsApplyProvisionedEntry_Object = MibTableRow
vrIpNsApplyProvisionedEntry = _VrIpNsApplyProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 2, 10, 1)
)
vrIpNsApplyProvisionedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpNsIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpNsApplyIndex"),
)
if mibBuilder.loadTexts:
    vrIpNsApplyProvisionedEntry.setStatus("mandatory")


class _VrIpNsApplyFilter_Type(AsciiString):
    """Custom type vrIpNsApplyFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrIpNsApplyFilter_Type.__name__ = "AsciiString"
_VrIpNsApplyFilter_Object = MibTableColumn
vrIpNsApplyFilter = _VrIpNsApplyFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 2, 10, 1, 1),
    _VrIpNsApplyFilter_Type()
)
vrIpNsApplyFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNsApplyFilter.setStatus("mandatory")
_VrIpNsApplyIpAddress1_Type = IpAddress
_VrIpNsApplyIpAddress1_Object = MibTableColumn
vrIpNsApplyIpAddress1 = _VrIpNsApplyIpAddress1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 2, 10, 1, 2),
    _VrIpNsApplyIpAddress1_Type()
)
vrIpNsApplyIpAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNsApplyIpAddress1.setStatus("mandatory")
_VrIpNsApplyIpMask1_Type = IpAddress
_VrIpNsApplyIpMask1_Object = MibTableColumn
vrIpNsApplyIpMask1 = _VrIpNsApplyIpMask1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 2, 10, 1, 3),
    _VrIpNsApplyIpMask1_Type()
)
vrIpNsApplyIpMask1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNsApplyIpMask1.setStatus("mandatory")
_VrIpNsApplyIpAddress2_Type = IpAddress
_VrIpNsApplyIpAddress2_Object = MibTableColumn
vrIpNsApplyIpAddress2 = _VrIpNsApplyIpAddress2_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 2, 10, 1, 4),
    _VrIpNsApplyIpAddress2_Type()
)
vrIpNsApplyIpAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNsApplyIpAddress2.setStatus("mandatory")
_VrIpNsApplyIpMask2_Type = IpAddress
_VrIpNsApplyIpMask2_Object = MibTableColumn
vrIpNsApplyIpMask2 = _VrIpNsApplyIpMask2_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 2, 10, 1, 5),
    _VrIpNsApplyIpMask2_Type()
)
vrIpNsApplyIpMask2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNsApplyIpMask2.setStatus("mandatory")


class _VrIpNsApplyDirection_Type(Integer32):
    """Custom type vrIpNsApplyDirection based on Integer32"""
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


_VrIpNsApplyDirection_Type.__name__ = "Integer32"
_VrIpNsApplyDirection_Object = MibTableColumn
vrIpNsApplyDirection = _VrIpNsApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 2, 10, 1, 6),
    _VrIpNsApplyDirection_Type()
)
vrIpNsApplyDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNsApplyDirection.setStatus("mandatory")
_VrIpNsProvTable_Object = MibTable
vrIpNsProvTable = _VrIpNsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 10)
)
if mibBuilder.loadTexts:
    vrIpNsProvTable.setStatus("mandatory")
_VrIpNsProvEntry_Object = MibTableRow
vrIpNsProvEntry = _VrIpNsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 10, 1)
)
vrIpNsProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpNsIndex"),
)
if mibBuilder.loadTexts:
    vrIpNsProvEntry.setStatus("mandatory")


class _VrIpNsFirstFilter_Type(AsciiString):
    """Custom type vrIpNsFirstFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrIpNsFirstFilter_Type.__name__ = "AsciiString"
_VrIpNsFirstFilter_Object = MibTableColumn
vrIpNsFirstFilter = _VrIpNsFirstFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 10, 1, 1),
    _VrIpNsFirstFilter_Type()
)
vrIpNsFirstFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNsFirstFilter.setStatus("mandatory")


class _VrIpNsLocalInFilter_Type(AsciiString):
    """Custom type vrIpNsLocalInFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrIpNsLocalInFilter_Type.__name__ = "AsciiString"
_VrIpNsLocalInFilter_Object = MibTableColumn
vrIpNsLocalInFilter = _VrIpNsLocalInFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 10, 1, 2),
    _VrIpNsLocalInFilter_Type()
)
vrIpNsLocalInFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNsLocalInFilter.setStatus("mandatory")


class _VrIpNsLocalOutFilter_Type(AsciiString):
    """Custom type vrIpNsLocalOutFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrIpNsLocalOutFilter_Type.__name__ = "AsciiString"
_VrIpNsLocalOutFilter_Object = MibTableColumn
vrIpNsLocalOutFilter = _VrIpNsLocalOutFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 10, 1, 3),
    _VrIpNsLocalOutFilter_Type()
)
vrIpNsLocalOutFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNsLocalOutFilter.setStatus("mandatory")


class _VrIpNsLastFilter_Type(AsciiString):
    """Custom type vrIpNsLastFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrIpNsLastFilter_Type.__name__ = "AsciiString"
_VrIpNsLastFilter_Object = MibTableColumn
vrIpNsLastFilter = _VrIpNsLastFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 10, 10, 1, 4),
    _VrIpNsLastFilter_Type()
)
vrIpNsLastFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpNsLastFilter.setStatus("mandatory")
_VrIpArp_ObjectIdentity = ObjectIdentity
vrIpArp = _VrIpArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11)
)
_VrIpArpRowStatusTable_Object = MibTable
vrIpArpRowStatusTable = _VrIpArpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 1)
)
if mibBuilder.loadTexts:
    vrIpArpRowStatusTable.setStatus("mandatory")
_VrIpArpRowStatusEntry_Object = MibTableRow
vrIpArpRowStatusEntry = _VrIpArpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 1, 1)
)
vrIpArpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpArpIndex"),
)
if mibBuilder.loadTexts:
    vrIpArpRowStatusEntry.setStatus("mandatory")
_VrIpArpRowStatus_Type = RowStatus
_VrIpArpRowStatus_Object = MibTableColumn
vrIpArpRowStatus = _VrIpArpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 1, 1, 1),
    _VrIpArpRowStatus_Type()
)
vrIpArpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpArpRowStatus.setStatus("mandatory")
_VrIpArpComponentName_Type = DisplayString
_VrIpArpComponentName_Object = MibTableColumn
vrIpArpComponentName = _VrIpArpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 1, 1, 2),
    _VrIpArpComponentName_Type()
)
vrIpArpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpArpComponentName.setStatus("mandatory")
_VrIpArpStorageType_Type = StorageType
_VrIpArpStorageType_Object = MibTableColumn
vrIpArpStorageType = _VrIpArpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 1, 1, 4),
    _VrIpArpStorageType_Type()
)
vrIpArpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpArpStorageType.setStatus("mandatory")
_VrIpArpIndex_Type = NonReplicated
_VrIpArpIndex_Object = MibTableColumn
vrIpArpIndex = _VrIpArpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 1, 1, 10),
    _VrIpArpIndex_Type()
)
vrIpArpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpArpIndex.setStatus("mandatory")
_VrIpArpHost_ObjectIdentity = ObjectIdentity
vrIpArpHost = _VrIpArpHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 2)
)
_VrIpArpHostRowStatusTable_Object = MibTable
vrIpArpHostRowStatusTable = _VrIpArpHostRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpArpHostRowStatusTable.setStatus("mandatory")
_VrIpArpHostRowStatusEntry_Object = MibTableRow
vrIpArpHostRowStatusEntry = _VrIpArpHostRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 2, 1, 1)
)
vrIpArpHostRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpArpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpArpHostHostAddressIndex"),
)
if mibBuilder.loadTexts:
    vrIpArpHostRowStatusEntry.setStatus("mandatory")
_VrIpArpHostRowStatus_Type = RowStatus
_VrIpArpHostRowStatus_Object = MibTableColumn
vrIpArpHostRowStatus = _VrIpArpHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 2, 1, 1, 1),
    _VrIpArpHostRowStatus_Type()
)
vrIpArpHostRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpArpHostRowStatus.setStatus("mandatory")
_VrIpArpHostComponentName_Type = DisplayString
_VrIpArpHostComponentName_Object = MibTableColumn
vrIpArpHostComponentName = _VrIpArpHostComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 2, 1, 1, 2),
    _VrIpArpHostComponentName_Type()
)
vrIpArpHostComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpArpHostComponentName.setStatus("mandatory")
_VrIpArpHostStorageType_Type = StorageType
_VrIpArpHostStorageType_Object = MibTableColumn
vrIpArpHostStorageType = _VrIpArpHostStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 2, 1, 1, 4),
    _VrIpArpHostStorageType_Type()
)
vrIpArpHostStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpArpHostStorageType.setStatus("mandatory")
_VrIpArpHostHostAddressIndex_Type = IpAddress
_VrIpArpHostHostAddressIndex_Object = MibTableColumn
vrIpArpHostHostAddressIndex = _VrIpArpHostHostAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 2, 1, 1, 10),
    _VrIpArpHostHostAddressIndex_Type()
)
vrIpArpHostHostAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpArpHostHostAddressIndex.setStatus("mandatory")
_VrIpArpHostProvTable_Object = MibTable
vrIpArpHostProvTable = _VrIpArpHostProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpArpHostProvTable.setStatus("mandatory")
_VrIpArpHostProvEntry_Object = MibTableRow
vrIpArpHostProvEntry = _VrIpArpHostProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 2, 10, 1)
)
vrIpArpHostProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpArpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpArpHostHostAddressIndex"),
)
if mibBuilder.loadTexts:
    vrIpArpHostProvEntry.setStatus("mandatory")


class _VrIpArpHostPhysAddress_Type(PhysAddress):
    """Custom type vrIpArpHostPhysAddress based on PhysAddress"""
    defaultHexValue = "000000000000"

    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_VrIpArpHostPhysAddress_Type.__name__ = "PhysAddress"
_VrIpArpHostPhysAddress_Object = MibTableColumn
vrIpArpHostPhysAddress = _VrIpArpHostPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 2, 10, 1, 1),
    _VrIpArpHostPhysAddress_Type()
)
vrIpArpHostPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpArpHostPhysAddress.setStatus("mandatory")


class _VrIpArpHostMaxTxUnit_Type(Unsigned32):
    """Custom type vrIpArpHostMaxTxUnit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 18944),
    )


_VrIpArpHostMaxTxUnit_Type.__name__ = "Unsigned32"
_VrIpArpHostMaxTxUnit_Object = MibTableColumn
vrIpArpHostMaxTxUnit = _VrIpArpHostMaxTxUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 2, 10, 1, 2),
    _VrIpArpHostMaxTxUnit_Type()
)
vrIpArpHostMaxTxUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpArpHostMaxTxUnit.setStatus("mandatory")


class _VrIpArpHostPermanentVirtualCircuitNumber_Type(Unsigned32):
    """Custom type vrIpArpHostPermanentVirtualCircuitNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VrIpArpHostPermanentVirtualCircuitNumber_Type.__name__ = "Unsigned32"
_VrIpArpHostPermanentVirtualCircuitNumber_Object = MibTableColumn
vrIpArpHostPermanentVirtualCircuitNumber = _VrIpArpHostPermanentVirtualCircuitNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 2, 10, 1, 3),
    _VrIpArpHostPermanentVirtualCircuitNumber_Type()
)
vrIpArpHostPermanentVirtualCircuitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpArpHostPermanentVirtualCircuitNumber.setStatus("mandatory")


class _VrIpArpHostEncap_Type(Integer32):
    """Custom type vrIpArpHostEncap based on Integer32"""
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


_VrIpArpHostEncap_Type.__name__ = "Integer32"
_VrIpArpHostEncap_Object = MibTableColumn
vrIpArpHostEncap = _VrIpArpHostEncap_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 2, 10, 1, 4),
    _VrIpArpHostEncap_Type()
)
vrIpArpHostEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpArpHostEncap.setStatus("mandatory")
_VrIpArpHostOperTable_Object = MibTable
vrIpArpHostOperTable = _VrIpArpHostOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 2, 11)
)
if mibBuilder.loadTexts:
    vrIpArpHostOperTable.setStatus("mandatory")
_VrIpArpHostOperEntry_Object = MibTableRow
vrIpArpHostOperEntry = _VrIpArpHostOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 2, 11, 1)
)
vrIpArpHostOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpArpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpArpHostHostAddressIndex"),
)
if mibBuilder.loadTexts:
    vrIpArpHostOperEntry.setStatus("mandatory")


class _VrIpArpHostOperMaxTxUnit_Type(Unsigned32):
    """Custom type vrIpArpHostOperMaxTxUnit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 18944),
    )


_VrIpArpHostOperMaxTxUnit_Type.__name__ = "Unsigned32"
_VrIpArpHostOperMaxTxUnit_Object = MibTableColumn
vrIpArpHostOperMaxTxUnit = _VrIpArpHostOperMaxTxUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 2, 11, 1, 4),
    _VrIpArpHostOperMaxTxUnit_Type()
)
vrIpArpHostOperMaxTxUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpArpHostOperMaxTxUnit.setStatus("mandatory")


class _VrIpArpHostOperEncap_Type(Integer32):
    """Custom type vrIpArpHostOperEncap based on Integer32"""
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


_VrIpArpHostOperEncap_Type.__name__ = "Integer32"
_VrIpArpHostOperEncap_Object = MibTableColumn
vrIpArpHostOperEncap = _VrIpArpHostOperEncap_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 2, 11, 1, 5),
    _VrIpArpHostOperEncap_Type()
)
vrIpArpHostOperEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpArpHostOperEncap.setStatus("mandatory")
_VrIpArpDynHost_ObjectIdentity = ObjectIdentity
vrIpArpDynHost = _VrIpArpDynHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 3)
)
_VrIpArpDynHostRowStatusTable_Object = MibTable
vrIpArpDynHostRowStatusTable = _VrIpArpDynHostRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 3, 1)
)
if mibBuilder.loadTexts:
    vrIpArpDynHostRowStatusTable.setStatus("mandatory")
_VrIpArpDynHostRowStatusEntry_Object = MibTableRow
vrIpArpDynHostRowStatusEntry = _VrIpArpDynHostRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 3, 1, 1)
)
vrIpArpDynHostRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpArpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpArpDynHostHostAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpArpDynHostCosIndex"),
)
if mibBuilder.loadTexts:
    vrIpArpDynHostRowStatusEntry.setStatus("mandatory")
_VrIpArpDynHostRowStatus_Type = RowStatus
_VrIpArpDynHostRowStatus_Object = MibTableColumn
vrIpArpDynHostRowStatus = _VrIpArpDynHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 3, 1, 1, 1),
    _VrIpArpDynHostRowStatus_Type()
)
vrIpArpDynHostRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpArpDynHostRowStatus.setStatus("mandatory")
_VrIpArpDynHostComponentName_Type = DisplayString
_VrIpArpDynHostComponentName_Object = MibTableColumn
vrIpArpDynHostComponentName = _VrIpArpDynHostComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 3, 1, 1, 2),
    _VrIpArpDynHostComponentName_Type()
)
vrIpArpDynHostComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpArpDynHostComponentName.setStatus("mandatory")
_VrIpArpDynHostStorageType_Type = StorageType
_VrIpArpDynHostStorageType_Object = MibTableColumn
vrIpArpDynHostStorageType = _VrIpArpDynHostStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 3, 1, 1, 4),
    _VrIpArpDynHostStorageType_Type()
)
vrIpArpDynHostStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpArpDynHostStorageType.setStatus("mandatory")
_VrIpArpDynHostHostAddressIndex_Type = IpAddress
_VrIpArpDynHostHostAddressIndex_Object = MibTableColumn
vrIpArpDynHostHostAddressIndex = _VrIpArpDynHostHostAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 3, 1, 1, 10),
    _VrIpArpDynHostHostAddressIndex_Type()
)
vrIpArpDynHostHostAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpArpDynHostHostAddressIndex.setStatus("mandatory")


class _VrIpArpDynHostCosIndex_Type(Integer32):
    """Custom type vrIpArpDynHostCosIndex based on Integer32"""
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


_VrIpArpDynHostCosIndex_Type.__name__ = "Integer32"
_VrIpArpDynHostCosIndex_Object = MibTableColumn
vrIpArpDynHostCosIndex = _VrIpArpDynHostCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 3, 1, 1, 11),
    _VrIpArpDynHostCosIndex_Type()
)
vrIpArpDynHostCosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpArpDynHostCosIndex.setStatus("mandatory")
_VrIpArpDynHostOperTable_Object = MibTable
vrIpArpDynHostOperTable = _VrIpArpDynHostOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 3, 10)
)
if mibBuilder.loadTexts:
    vrIpArpDynHostOperTable.setStatus("mandatory")
_VrIpArpDynHostOperEntry_Object = MibTableRow
vrIpArpDynHostOperEntry = _VrIpArpDynHostOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 3, 10, 1)
)
vrIpArpDynHostOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpArpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpArpDynHostHostAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpArpDynHostCosIndex"),
)
if mibBuilder.loadTexts:
    vrIpArpDynHostOperEntry.setStatus("mandatory")


class _VrIpArpDynHostPhysAddress_Type(PhysAddress):
    """Custom type vrIpArpDynHostPhysAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_VrIpArpDynHostPhysAddress_Type.__name__ = "PhysAddress"
_VrIpArpDynHostPhysAddress_Object = MibTableColumn
vrIpArpDynHostPhysAddress = _VrIpArpDynHostPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 3, 10, 1, 1),
    _VrIpArpDynHostPhysAddress_Type()
)
vrIpArpDynHostPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpArpDynHostPhysAddress.setStatus("mandatory")


class _VrIpArpDynHostMaxTxUnit_Type(Unsigned32):
    """Custom type vrIpArpDynHostMaxTxUnit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 18944),
    )


_VrIpArpDynHostMaxTxUnit_Type.__name__ = "Unsigned32"
_VrIpArpDynHostMaxTxUnit_Object = MibTableColumn
vrIpArpDynHostMaxTxUnit = _VrIpArpDynHostMaxTxUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 3, 10, 1, 3),
    _VrIpArpDynHostMaxTxUnit_Type()
)
vrIpArpDynHostMaxTxUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpArpDynHostMaxTxUnit.setStatus("mandatory")


class _VrIpArpDynHostEncapsulationType_Type(Integer32):
    """Custom type vrIpArpDynHostEncapsulationType based on Integer32"""
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


_VrIpArpDynHostEncapsulationType_Type.__name__ = "Integer32"
_VrIpArpDynHostEncapsulationType_Object = MibTableColumn
vrIpArpDynHostEncapsulationType = _VrIpArpDynHostEncapsulationType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 3, 10, 1, 4),
    _VrIpArpDynHostEncapsulationType_Type()
)
vrIpArpDynHostEncapsulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpArpDynHostEncapsulationType.setStatus("mandatory")


class _VrIpArpDynHostPermanentVirtualCircuitNumber_Type(Unsigned32):
    """Custom type vrIpArpDynHostPermanentVirtualCircuitNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VrIpArpDynHostPermanentVirtualCircuitNumber_Type.__name__ = "Unsigned32"
_VrIpArpDynHostPermanentVirtualCircuitNumber_Object = MibTableColumn
vrIpArpDynHostPermanentVirtualCircuitNumber = _VrIpArpDynHostPermanentVirtualCircuitNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 3, 10, 1, 5),
    _VrIpArpDynHostPermanentVirtualCircuitNumber_Type()
)
vrIpArpDynHostPermanentVirtualCircuitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpArpDynHostPermanentVirtualCircuitNumber.setStatus("mandatory")


class _VrIpArpDynHostIfIndex_Type(InterfaceIndex):
    """Custom type vrIpArpDynHostIfIndex based on InterfaceIndex"""
    defaultValue = 1

    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrIpArpDynHostIfIndex_Type.__name__ = "InterfaceIndex"
_VrIpArpDynHostIfIndex_Object = MibTableColumn
vrIpArpDynHostIfIndex = _VrIpArpDynHostIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 3, 10, 1, 6),
    _VrIpArpDynHostIfIndex_Type()
)
vrIpArpDynHostIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpArpDynHostIfIndex.setStatus("mandatory")


class _VrIpArpDynHostType_Type(Integer32):
    """Custom type vrIpArpDynHostType based on Integer32"""
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


_VrIpArpDynHostType_Type.__name__ = "Integer32"
_VrIpArpDynHostType_Object = MibTableColumn
vrIpArpDynHostType = _VrIpArpDynHostType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 3, 10, 1, 7),
    _VrIpArpDynHostType_Type()
)
vrIpArpDynHostType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpArpDynHostType.setStatus("mandatory")


class _VrIpArpDynHostNcPhysAddress_Type(PhysAddress):
    """Custom type vrIpArpDynHostNcPhysAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_VrIpArpDynHostNcPhysAddress_Type.__name__ = "PhysAddress"
_VrIpArpDynHostNcPhysAddress_Object = MibTableColumn
vrIpArpDynHostNcPhysAddress = _VrIpArpDynHostNcPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 3, 10, 1, 8),
    _VrIpArpDynHostNcPhysAddress_Type()
)
vrIpArpDynHostNcPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpArpDynHostNcPhysAddress.setStatus("mandatory")
_VrIpArpProvTable_Object = MibTable
vrIpArpProvTable = _VrIpArpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 10)
)
if mibBuilder.loadTexts:
    vrIpArpProvTable.setStatus("mandatory")
_VrIpArpProvEntry_Object = MibTableRow
vrIpArpProvEntry = _VrIpArpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 10, 1)
)
vrIpArpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpArpIndex"),
)
if mibBuilder.loadTexts:
    vrIpArpProvEntry.setStatus("mandatory")


class _VrIpArpAutoRefresh_Type(Integer32):
    """Custom type vrIpArpAutoRefresh based on Integer32"""
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


_VrIpArpAutoRefresh_Type.__name__ = "Integer32"
_VrIpArpAutoRefresh_Object = MibTableColumn
vrIpArpAutoRefresh = _VrIpArpAutoRefresh_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 10, 1, 1),
    _VrIpArpAutoRefresh_Type()
)
vrIpArpAutoRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpArpAutoRefresh.setStatus("mandatory")


class _VrIpArpAutoRefreshTimeout_Type(Unsigned32):
    """Custom type vrIpArpAutoRefreshTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_VrIpArpAutoRefreshTimeout_Type.__name__ = "Unsigned32"
_VrIpArpAutoRefreshTimeout_Object = MibTableColumn
vrIpArpAutoRefreshTimeout = _VrIpArpAutoRefreshTimeout_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 11, 10, 1, 2),
    _VrIpArpAutoRefreshTimeout_Type()
)
vrIpArpAutoRefreshTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpArpAutoRefreshTimeout.setStatus("mandatory")
_VrIpIcmp_ObjectIdentity = ObjectIdentity
vrIpIcmp = _VrIpIcmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12)
)
_VrIpIcmpRowStatusTable_Object = MibTable
vrIpIcmpRowStatusTable = _VrIpIcmpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 1)
)
if mibBuilder.loadTexts:
    vrIpIcmpRowStatusTable.setStatus("mandatory")
_VrIpIcmpRowStatusEntry_Object = MibTableRow
vrIpIcmpRowStatusEntry = _VrIpIcmpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 1, 1)
)
vrIpIcmpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIcmpIndex"),
)
if mibBuilder.loadTexts:
    vrIpIcmpRowStatusEntry.setStatus("mandatory")
_VrIpIcmpRowStatus_Type = RowStatus
_VrIpIcmpRowStatus_Object = MibTableColumn
vrIpIcmpRowStatus = _VrIpIcmpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 1, 1, 1),
    _VrIpIcmpRowStatus_Type()
)
vrIpIcmpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpRowStatus.setStatus("mandatory")
_VrIpIcmpComponentName_Type = DisplayString
_VrIpIcmpComponentName_Object = MibTableColumn
vrIpIcmpComponentName = _VrIpIcmpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 1, 1, 2),
    _VrIpIcmpComponentName_Type()
)
vrIpIcmpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpComponentName.setStatus("mandatory")
_VrIpIcmpStorageType_Type = StorageType
_VrIpIcmpStorageType_Object = MibTableColumn
vrIpIcmpStorageType = _VrIpIcmpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 1, 1, 4),
    _VrIpIcmpStorageType_Type()
)
vrIpIcmpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpStorageType.setStatus("mandatory")
_VrIpIcmpIndex_Type = NonReplicated
_VrIpIcmpIndex_Object = MibTableColumn
vrIpIcmpIndex = _VrIpIcmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 1, 1, 10),
    _VrIpIcmpIndex_Type()
)
vrIpIcmpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpIcmpIndex.setStatus("mandatory")
_VrIpIcmpProvTable_Object = MibTable
vrIpIcmpProvTable = _VrIpIcmpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 10)
)
if mibBuilder.loadTexts:
    vrIpIcmpProvTable.setStatus("mandatory")
_VrIpIcmpProvEntry_Object = MibTableRow
vrIpIcmpProvEntry = _VrIpIcmpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 10, 1)
)
vrIpIcmpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIcmpIndex"),
)
if mibBuilder.loadTexts:
    vrIpIcmpProvEntry.setStatus("mandatory")


class _VrIpIcmpSendRedirect_Type(Integer32):
    """Custom type vrIpIcmpSendRedirect based on Integer32"""
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


_VrIpIcmpSendRedirect_Type.__name__ = "Integer32"
_VrIpIcmpSendRedirect_Object = MibTableColumn
vrIpIcmpSendRedirect = _VrIpIcmpSendRedirect_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 10, 1, 1),
    _VrIpIcmpSendRedirect_Type()
)
vrIpIcmpSendRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpIcmpSendRedirect.setStatus("obsolete")


class _VrIpIcmpSendHostUnreachable_Type(Integer32):
    """Custom type vrIpIcmpSendHostUnreachable based on Integer32"""
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


_VrIpIcmpSendHostUnreachable_Type.__name__ = "Integer32"
_VrIpIcmpSendHostUnreachable_Object = MibTableColumn
vrIpIcmpSendHostUnreachable = _VrIpIcmpSendHostUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 10, 1, 2),
    _VrIpIcmpSendHostUnreachable_Type()
)
vrIpIcmpSendHostUnreachable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpIcmpSendHostUnreachable.setStatus("obsolete")
_VrIpIcmpStatsTable_Object = MibTable
vrIpIcmpStatsTable = _VrIpIcmpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11)
)
if mibBuilder.loadTexts:
    vrIpIcmpStatsTable.setStatus("mandatory")
_VrIpIcmpStatsEntry_Object = MibTableRow
vrIpIcmpStatsEntry = _VrIpIcmpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1)
)
vrIpIcmpStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIcmpIndex"),
)
if mibBuilder.loadTexts:
    vrIpIcmpStatsEntry.setStatus("mandatory")
_VrIpIcmpInMsgs_Type = Counter32
_VrIpIcmpInMsgs_Object = MibTableColumn
vrIpIcmpInMsgs = _VrIpIcmpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 1),
    _VrIpIcmpInMsgs_Type()
)
vrIpIcmpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpInMsgs.setStatus("mandatory")
_VrIpIcmpInErrors_Type = Counter32
_VrIpIcmpInErrors_Object = MibTableColumn
vrIpIcmpInErrors = _VrIpIcmpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 2),
    _VrIpIcmpInErrors_Type()
)
vrIpIcmpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpInErrors.setStatus("mandatory")
_VrIpIcmpInDestUnreachs_Type = Counter32
_VrIpIcmpInDestUnreachs_Object = MibTableColumn
vrIpIcmpInDestUnreachs = _VrIpIcmpInDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 3),
    _VrIpIcmpInDestUnreachs_Type()
)
vrIpIcmpInDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpInDestUnreachs.setStatus("mandatory")
_VrIpIcmpInTimeExcds_Type = Counter32
_VrIpIcmpInTimeExcds_Object = MibTableColumn
vrIpIcmpInTimeExcds = _VrIpIcmpInTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 4),
    _VrIpIcmpInTimeExcds_Type()
)
vrIpIcmpInTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpInTimeExcds.setStatus("mandatory")
_VrIpIcmpInParmProbs_Type = Counter32
_VrIpIcmpInParmProbs_Object = MibTableColumn
vrIpIcmpInParmProbs = _VrIpIcmpInParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 5),
    _VrIpIcmpInParmProbs_Type()
)
vrIpIcmpInParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpInParmProbs.setStatus("mandatory")
_VrIpIcmpInSrcQuenchs_Type = Counter32
_VrIpIcmpInSrcQuenchs_Object = MibTableColumn
vrIpIcmpInSrcQuenchs = _VrIpIcmpInSrcQuenchs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 6),
    _VrIpIcmpInSrcQuenchs_Type()
)
vrIpIcmpInSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpInSrcQuenchs.setStatus("mandatory")
_VrIpIcmpInRedirects_Type = Counter32
_VrIpIcmpInRedirects_Object = MibTableColumn
vrIpIcmpInRedirects = _VrIpIcmpInRedirects_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 7),
    _VrIpIcmpInRedirects_Type()
)
vrIpIcmpInRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpInRedirects.setStatus("mandatory")
_VrIpIcmpInEchos_Type = Counter32
_VrIpIcmpInEchos_Object = MibTableColumn
vrIpIcmpInEchos = _VrIpIcmpInEchos_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 8),
    _VrIpIcmpInEchos_Type()
)
vrIpIcmpInEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpInEchos.setStatus("mandatory")
_VrIpIcmpInEchoReps_Type = Counter32
_VrIpIcmpInEchoReps_Object = MibTableColumn
vrIpIcmpInEchoReps = _VrIpIcmpInEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 9),
    _VrIpIcmpInEchoReps_Type()
)
vrIpIcmpInEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpInEchoReps.setStatus("mandatory")
_VrIpIcmpInTimestamps_Type = Counter32
_VrIpIcmpInTimestamps_Object = MibTableColumn
vrIpIcmpInTimestamps = _VrIpIcmpInTimestamps_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 10),
    _VrIpIcmpInTimestamps_Type()
)
vrIpIcmpInTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpInTimestamps.setStatus("mandatory")
_VrIpIcmpInTimestampReps_Type = Counter32
_VrIpIcmpInTimestampReps_Object = MibTableColumn
vrIpIcmpInTimestampReps = _VrIpIcmpInTimestampReps_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 11),
    _VrIpIcmpInTimestampReps_Type()
)
vrIpIcmpInTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpInTimestampReps.setStatus("mandatory")
_VrIpIcmpInAddrMasks_Type = Counter32
_VrIpIcmpInAddrMasks_Object = MibTableColumn
vrIpIcmpInAddrMasks = _VrIpIcmpInAddrMasks_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 12),
    _VrIpIcmpInAddrMasks_Type()
)
vrIpIcmpInAddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpInAddrMasks.setStatus("mandatory")
_VrIpIcmpInAddrMaskReps_Type = Counter32
_VrIpIcmpInAddrMaskReps_Object = MibTableColumn
vrIpIcmpInAddrMaskReps = _VrIpIcmpInAddrMaskReps_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 13),
    _VrIpIcmpInAddrMaskReps_Type()
)
vrIpIcmpInAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpInAddrMaskReps.setStatus("mandatory")
_VrIpIcmpOutMsgs_Type = Counter32
_VrIpIcmpOutMsgs_Object = MibTableColumn
vrIpIcmpOutMsgs = _VrIpIcmpOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 14),
    _VrIpIcmpOutMsgs_Type()
)
vrIpIcmpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpOutMsgs.setStatus("mandatory")
_VrIpIcmpOutErrors_Type = Counter32
_VrIpIcmpOutErrors_Object = MibTableColumn
vrIpIcmpOutErrors = _VrIpIcmpOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 15),
    _VrIpIcmpOutErrors_Type()
)
vrIpIcmpOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpOutErrors.setStatus("mandatory")
_VrIpIcmpOutDestUnreachs_Type = Counter32
_VrIpIcmpOutDestUnreachs_Object = MibTableColumn
vrIpIcmpOutDestUnreachs = _VrIpIcmpOutDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 16),
    _VrIpIcmpOutDestUnreachs_Type()
)
vrIpIcmpOutDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpOutDestUnreachs.setStatus("mandatory")
_VrIpIcmpOutTimeExcds_Type = Counter32
_VrIpIcmpOutTimeExcds_Object = MibTableColumn
vrIpIcmpOutTimeExcds = _VrIpIcmpOutTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 17),
    _VrIpIcmpOutTimeExcds_Type()
)
vrIpIcmpOutTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpOutTimeExcds.setStatus("mandatory")
_VrIpIcmpOutParmProbs_Type = Counter32
_VrIpIcmpOutParmProbs_Object = MibTableColumn
vrIpIcmpOutParmProbs = _VrIpIcmpOutParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 18),
    _VrIpIcmpOutParmProbs_Type()
)
vrIpIcmpOutParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpOutParmProbs.setStatus("mandatory")
_VrIpIcmpOutSrcQuenchs_Type = Counter32
_VrIpIcmpOutSrcQuenchs_Object = MibTableColumn
vrIpIcmpOutSrcQuenchs = _VrIpIcmpOutSrcQuenchs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 19),
    _VrIpIcmpOutSrcQuenchs_Type()
)
vrIpIcmpOutSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpOutSrcQuenchs.setStatus("mandatory")
_VrIpIcmpOutRedirects_Type = Counter32
_VrIpIcmpOutRedirects_Object = MibTableColumn
vrIpIcmpOutRedirects = _VrIpIcmpOutRedirects_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 20),
    _VrIpIcmpOutRedirects_Type()
)
vrIpIcmpOutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpOutRedirects.setStatus("mandatory")
_VrIpIcmpOutEchos_Type = Counter32
_VrIpIcmpOutEchos_Object = MibTableColumn
vrIpIcmpOutEchos = _VrIpIcmpOutEchos_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 21),
    _VrIpIcmpOutEchos_Type()
)
vrIpIcmpOutEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpOutEchos.setStatus("mandatory")
_VrIpIcmpOutEchoReps_Type = Counter32
_VrIpIcmpOutEchoReps_Object = MibTableColumn
vrIpIcmpOutEchoReps = _VrIpIcmpOutEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 22),
    _VrIpIcmpOutEchoReps_Type()
)
vrIpIcmpOutEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpOutEchoReps.setStatus("mandatory")
_VrIpIcmpOutTimestamps_Type = Counter32
_VrIpIcmpOutTimestamps_Object = MibTableColumn
vrIpIcmpOutTimestamps = _VrIpIcmpOutTimestamps_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 23),
    _VrIpIcmpOutTimestamps_Type()
)
vrIpIcmpOutTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpOutTimestamps.setStatus("mandatory")
_VrIpIcmpOutTimestampReps_Type = Counter32
_VrIpIcmpOutTimestampReps_Object = MibTableColumn
vrIpIcmpOutTimestampReps = _VrIpIcmpOutTimestampReps_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 24),
    _VrIpIcmpOutTimestampReps_Type()
)
vrIpIcmpOutTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpOutTimestampReps.setStatus("mandatory")
_VrIpIcmpOutAddrMasks_Type = Counter32
_VrIpIcmpOutAddrMasks_Object = MibTableColumn
vrIpIcmpOutAddrMasks = _VrIpIcmpOutAddrMasks_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 25),
    _VrIpIcmpOutAddrMasks_Type()
)
vrIpIcmpOutAddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpOutAddrMasks.setStatus("mandatory")
_VrIpIcmpOutAddrMaskReps_Type = Counter32
_VrIpIcmpOutAddrMaskReps_Object = MibTableColumn
vrIpIcmpOutAddrMaskReps = _VrIpIcmpOutAddrMaskReps_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 26),
    _VrIpIcmpOutAddrMaskReps_Type()
)
vrIpIcmpOutAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpOutAddrMaskReps.setStatus("mandatory")
_VrIpIcmpInRtrAdvs_Type = Counter32
_VrIpIcmpInRtrAdvs_Object = MibTableColumn
vrIpIcmpInRtrAdvs = _VrIpIcmpInRtrAdvs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 27),
    _VrIpIcmpInRtrAdvs_Type()
)
vrIpIcmpInRtrAdvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpInRtrAdvs.setStatus("mandatory")
_VrIpIcmpInRtrSolicits_Type = Counter32
_VrIpIcmpInRtrSolicits_Object = MibTableColumn
vrIpIcmpInRtrSolicits = _VrIpIcmpInRtrSolicits_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 28),
    _VrIpIcmpInRtrSolicits_Type()
)
vrIpIcmpInRtrSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpInRtrSolicits.setStatus("mandatory")
_VrIpIcmpOutRtrAdvs_Type = Counter32
_VrIpIcmpOutRtrAdvs_Object = MibTableColumn
vrIpIcmpOutRtrAdvs = _VrIpIcmpOutRtrAdvs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 29),
    _VrIpIcmpOutRtrAdvs_Type()
)
vrIpIcmpOutRtrAdvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpOutRtrAdvs.setStatus("mandatory")
_VrIpIcmpOutRtrSolicits_Type = Counter32
_VrIpIcmpOutRtrSolicits_Object = MibTableColumn
vrIpIcmpOutRtrSolicits = _VrIpIcmpOutRtrSolicits_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 12, 11, 1, 30),
    _VrIpIcmpOutRtrSolicits_Type()
)
vrIpIcmpOutRtrSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpIcmpOutRtrSolicits.setStatus("mandatory")
_VrIpRelayBC_ObjectIdentity = ObjectIdentity
vrIpRelayBC = _VrIpRelayBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 13)
)
_VrIpRelayBCRowStatusTable_Object = MibTable
vrIpRelayBCRowStatusTable = _VrIpRelayBCRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 13, 1)
)
if mibBuilder.loadTexts:
    vrIpRelayBCRowStatusTable.setStatus("mandatory")
_VrIpRelayBCRowStatusEntry_Object = MibTableRow
vrIpRelayBCRowStatusEntry = _VrIpRelayBCRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 13, 1, 1)
)
vrIpRelayBCRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRelayBCIndex"),
)
if mibBuilder.loadTexts:
    vrIpRelayBCRowStatusEntry.setStatus("mandatory")
_VrIpRelayBCRowStatus_Type = RowStatus
_VrIpRelayBCRowStatus_Object = MibTableColumn
vrIpRelayBCRowStatus = _VrIpRelayBCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 13, 1, 1, 1),
    _VrIpRelayBCRowStatus_Type()
)
vrIpRelayBCRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRelayBCRowStatus.setStatus("mandatory")
_VrIpRelayBCComponentName_Type = DisplayString
_VrIpRelayBCComponentName_Object = MibTableColumn
vrIpRelayBCComponentName = _VrIpRelayBCComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 13, 1, 1, 2),
    _VrIpRelayBCComponentName_Type()
)
vrIpRelayBCComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRelayBCComponentName.setStatus("mandatory")
_VrIpRelayBCStorageType_Type = StorageType
_VrIpRelayBCStorageType_Object = MibTableColumn
vrIpRelayBCStorageType = _VrIpRelayBCStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 13, 1, 1, 4),
    _VrIpRelayBCStorageType_Type()
)
vrIpRelayBCStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRelayBCStorageType.setStatus("mandatory")
_VrIpRelayBCIndex_Type = NonReplicated
_VrIpRelayBCIndex_Object = MibTableColumn
vrIpRelayBCIndex = _VrIpRelayBCIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 13, 1, 1, 10),
    _VrIpRelayBCIndex_Type()
)
vrIpRelayBCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpRelayBCIndex.setStatus("mandatory")
_VrIpRelayBCPort_ObjectIdentity = ObjectIdentity
vrIpRelayBCPort = _VrIpRelayBCPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 13, 2)
)
_VrIpRelayBCPortRowStatusTable_Object = MibTable
vrIpRelayBCPortRowStatusTable = _VrIpRelayBCPortRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 13, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpRelayBCPortRowStatusTable.setStatus("mandatory")
_VrIpRelayBCPortRowStatusEntry_Object = MibTableRow
vrIpRelayBCPortRowStatusEntry = _VrIpRelayBCPortRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 13, 2, 1, 1)
)
vrIpRelayBCPortRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRelayBCIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRelayBCPortPortNumIndex"),
)
if mibBuilder.loadTexts:
    vrIpRelayBCPortRowStatusEntry.setStatus("mandatory")
_VrIpRelayBCPortRowStatus_Type = RowStatus
_VrIpRelayBCPortRowStatus_Object = MibTableColumn
vrIpRelayBCPortRowStatus = _VrIpRelayBCPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 13, 2, 1, 1, 1),
    _VrIpRelayBCPortRowStatus_Type()
)
vrIpRelayBCPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRelayBCPortRowStatus.setStatus("mandatory")
_VrIpRelayBCPortComponentName_Type = DisplayString
_VrIpRelayBCPortComponentName_Object = MibTableColumn
vrIpRelayBCPortComponentName = _VrIpRelayBCPortComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 13, 2, 1, 1, 2),
    _VrIpRelayBCPortComponentName_Type()
)
vrIpRelayBCPortComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRelayBCPortComponentName.setStatus("mandatory")
_VrIpRelayBCPortStorageType_Type = StorageType
_VrIpRelayBCPortStorageType_Object = MibTableColumn
vrIpRelayBCPortStorageType = _VrIpRelayBCPortStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 13, 2, 1, 1, 4),
    _VrIpRelayBCPortStorageType_Type()
)
vrIpRelayBCPortStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRelayBCPortStorageType.setStatus("mandatory")


class _VrIpRelayBCPortPortNumIndex_Type(Integer32):
    """Custom type vrIpRelayBCPortPortNumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_VrIpRelayBCPortPortNumIndex_Type.__name__ = "Integer32"
_VrIpRelayBCPortPortNumIndex_Object = MibTableColumn
vrIpRelayBCPortPortNumIndex = _VrIpRelayBCPortPortNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 13, 2, 1, 1, 10),
    _VrIpRelayBCPortPortNumIndex_Type()
)
vrIpRelayBCPortPortNumIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpRelayBCPortPortNumIndex.setStatus("mandatory")
_VrIpRelayBCPortOperTable_Object = MibTable
vrIpRelayBCPortOperTable = _VrIpRelayBCPortOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 13, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpRelayBCPortOperTable.setStatus("mandatory")
_VrIpRelayBCPortOperEntry_Object = MibTableRow
vrIpRelayBCPortOperEntry = _VrIpRelayBCPortOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 13, 2, 10, 1)
)
vrIpRelayBCPortOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRelayBCIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRelayBCPortPortNumIndex"),
)
if mibBuilder.loadTexts:
    vrIpRelayBCPortOperEntry.setStatus("mandatory")
_VrIpRelayBCPortRelayBcUdpCount_Type = Counter32
_VrIpRelayBCPortRelayBcUdpCount_Object = MibTableColumn
vrIpRelayBCPortRelayBcUdpCount = _VrIpRelayBCPortRelayBcUdpCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 13, 2, 10, 1, 1),
    _VrIpRelayBCPortRelayBcUdpCount_Type()
)
vrIpRelayBCPortRelayBcUdpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRelayBCPortRelayBcUdpCount.setStatus("mandatory")
_VrIpRelayBCProvTable_Object = MibTable
vrIpRelayBCProvTable = _VrIpRelayBCProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 13, 10)
)
if mibBuilder.loadTexts:
    vrIpRelayBCProvTable.setStatus("mandatory")
_VrIpRelayBCProvEntry_Object = MibTableRow
vrIpRelayBCProvEntry = _VrIpRelayBCProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 13, 10, 1)
)
vrIpRelayBCProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRelayBCIndex"),
)
if mibBuilder.loadTexts:
    vrIpRelayBCProvEntry.setStatus("mandatory")


class _VrIpRelayBCRelayStatus_Type(Integer32):
    """Custom type vrIpRelayBCRelayStatus based on Integer32"""
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


_VrIpRelayBCRelayStatus_Type.__name__ = "Integer32"
_VrIpRelayBCRelayStatus_Object = MibTableColumn
vrIpRelayBCRelayStatus = _VrIpRelayBCRelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 13, 10, 1, 1),
    _VrIpRelayBCRelayStatus_Type()
)
vrIpRelayBCRelayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRelayBCRelayStatus.setStatus("mandatory")


class _VrIpRelayBCRelayNdStatus_Type(Integer32):
    """Custom type vrIpRelayBCRelayNdStatus based on Integer32"""
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


_VrIpRelayBCRelayNdStatus_Type.__name__ = "Integer32"
_VrIpRelayBCRelayNdStatus_Object = MibTableColumn
vrIpRelayBCRelayNdStatus = _VrIpRelayBCRelayNdStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 13, 10, 1, 2),
    _VrIpRelayBCRelayNdStatus_Type()
)
vrIpRelayBCRelayNdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpRelayBCRelayNdStatus.setStatus("mandatory")
_VrIpRelayBCOperTable_Object = MibTable
vrIpRelayBCOperTable = _VrIpRelayBCOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 13, 11)
)
if mibBuilder.loadTexts:
    vrIpRelayBCOperTable.setStatus("mandatory")
_VrIpRelayBCOperEntry_Object = MibTableRow
vrIpRelayBCOperEntry = _VrIpRelayBCOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 13, 11, 1)
)
vrIpRelayBCOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpRelayBCIndex"),
)
if mibBuilder.loadTexts:
    vrIpRelayBCOperEntry.setStatus("mandatory")
_VrIpRelayBCRelayNdCount_Type = Counter32
_VrIpRelayBCRelayNdCount_Object = MibTableColumn
vrIpRelayBCRelayNdCount = _VrIpRelayBCRelayNdCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 13, 11, 1, 1),
    _VrIpRelayBCRelayNdCount_Type()
)
vrIpRelayBCRelayNdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRelayBCRelayNdCount.setStatus("mandatory")
_VrIpUdp_ObjectIdentity = ObjectIdentity
vrIpUdp = _VrIpUdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 14)
)
_VrIpUdpRowStatusTable_Object = MibTable
vrIpUdpRowStatusTable = _VrIpUdpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 14, 1)
)
if mibBuilder.loadTexts:
    vrIpUdpRowStatusTable.setStatus("mandatory")
_VrIpUdpRowStatusEntry_Object = MibTableRow
vrIpUdpRowStatusEntry = _VrIpUdpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 14, 1, 1)
)
vrIpUdpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpUdpIndex"),
)
if mibBuilder.loadTexts:
    vrIpUdpRowStatusEntry.setStatus("mandatory")
_VrIpUdpRowStatus_Type = RowStatus
_VrIpUdpRowStatus_Object = MibTableColumn
vrIpUdpRowStatus = _VrIpUdpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 14, 1, 1, 1),
    _VrIpUdpRowStatus_Type()
)
vrIpUdpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpUdpRowStatus.setStatus("mandatory")
_VrIpUdpComponentName_Type = DisplayString
_VrIpUdpComponentName_Object = MibTableColumn
vrIpUdpComponentName = _VrIpUdpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 14, 1, 1, 2),
    _VrIpUdpComponentName_Type()
)
vrIpUdpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpUdpComponentName.setStatus("mandatory")
_VrIpUdpStorageType_Type = StorageType
_VrIpUdpStorageType_Object = MibTableColumn
vrIpUdpStorageType = _VrIpUdpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 14, 1, 1, 4),
    _VrIpUdpStorageType_Type()
)
vrIpUdpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpUdpStorageType.setStatus("mandatory")
_VrIpUdpIndex_Type = NonReplicated
_VrIpUdpIndex_Object = MibTableColumn
vrIpUdpIndex = _VrIpUdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 14, 1, 1, 10),
    _VrIpUdpIndex_Type()
)
vrIpUdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpUdpIndex.setStatus("mandatory")
_VrIpUdpListenEntry_ObjectIdentity = ObjectIdentity
vrIpUdpListenEntry = _VrIpUdpListenEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 14, 2)
)
_VrIpUdpListenEntryRowStatusTable_Object = MibTable
vrIpUdpListenEntryRowStatusTable = _VrIpUdpListenEntryRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 14, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpUdpListenEntryRowStatusTable.setStatus("mandatory")
_VrIpUdpListenEntryRowStatusEntry_Object = MibTableRow
vrIpUdpListenEntryRowStatusEntry = _VrIpUdpListenEntryRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 14, 2, 1, 1)
)
vrIpUdpListenEntryRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpUdpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpUdpListenEntryLocalAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpUdpListenEntryLocalPortIndex"),
)
if mibBuilder.loadTexts:
    vrIpUdpListenEntryRowStatusEntry.setStatus("mandatory")
_VrIpUdpListenEntryRowStatus_Type = RowStatus
_VrIpUdpListenEntryRowStatus_Object = MibTableColumn
vrIpUdpListenEntryRowStatus = _VrIpUdpListenEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 14, 2, 1, 1, 1),
    _VrIpUdpListenEntryRowStatus_Type()
)
vrIpUdpListenEntryRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpUdpListenEntryRowStatus.setStatus("mandatory")
_VrIpUdpListenEntryComponentName_Type = DisplayString
_VrIpUdpListenEntryComponentName_Object = MibTableColumn
vrIpUdpListenEntryComponentName = _VrIpUdpListenEntryComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 14, 2, 1, 1, 2),
    _VrIpUdpListenEntryComponentName_Type()
)
vrIpUdpListenEntryComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpUdpListenEntryComponentName.setStatus("mandatory")
_VrIpUdpListenEntryStorageType_Type = StorageType
_VrIpUdpListenEntryStorageType_Object = MibTableColumn
vrIpUdpListenEntryStorageType = _VrIpUdpListenEntryStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 14, 2, 1, 1, 4),
    _VrIpUdpListenEntryStorageType_Type()
)
vrIpUdpListenEntryStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpUdpListenEntryStorageType.setStatus("mandatory")
_VrIpUdpListenEntryLocalAddressIndex_Type = IpAddress
_VrIpUdpListenEntryLocalAddressIndex_Object = MibTableColumn
vrIpUdpListenEntryLocalAddressIndex = _VrIpUdpListenEntryLocalAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 14, 2, 1, 1, 10),
    _VrIpUdpListenEntryLocalAddressIndex_Type()
)
vrIpUdpListenEntryLocalAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpUdpListenEntryLocalAddressIndex.setStatus("mandatory")


class _VrIpUdpListenEntryLocalPortIndex_Type(Integer32):
    """Custom type vrIpUdpListenEntryLocalPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpUdpListenEntryLocalPortIndex_Type.__name__ = "Integer32"
_VrIpUdpListenEntryLocalPortIndex_Object = MibTableColumn
vrIpUdpListenEntryLocalPortIndex = _VrIpUdpListenEntryLocalPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 14, 2, 1, 1, 11),
    _VrIpUdpListenEntryLocalPortIndex_Type()
)
vrIpUdpListenEntryLocalPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpUdpListenEntryLocalPortIndex.setStatus("mandatory")
_VrIpUdpStatsTable_Object = MibTable
vrIpUdpStatsTable = _VrIpUdpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 14, 10)
)
if mibBuilder.loadTexts:
    vrIpUdpStatsTable.setStatus("mandatory")
_VrIpUdpStatsEntry_Object = MibTableRow
vrIpUdpStatsEntry = _VrIpUdpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 14, 10, 1)
)
vrIpUdpStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpUdpIndex"),
)
if mibBuilder.loadTexts:
    vrIpUdpStatsEntry.setStatus("mandatory")
_VrIpUdpInDatagrams_Type = Counter32
_VrIpUdpInDatagrams_Object = MibTableColumn
vrIpUdpInDatagrams = _VrIpUdpInDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 14, 10, 1, 1),
    _VrIpUdpInDatagrams_Type()
)
vrIpUdpInDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpUdpInDatagrams.setStatus("mandatory")
_VrIpUdpNoPorts_Type = Counter32
_VrIpUdpNoPorts_Object = MibTableColumn
vrIpUdpNoPorts = _VrIpUdpNoPorts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 14, 10, 1, 2),
    _VrIpUdpNoPorts_Type()
)
vrIpUdpNoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpUdpNoPorts.setStatus("mandatory")
_VrIpUdpInErrors_Type = Counter32
_VrIpUdpInErrors_Object = MibTableColumn
vrIpUdpInErrors = _VrIpUdpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 14, 10, 1, 3),
    _VrIpUdpInErrors_Type()
)
vrIpUdpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpUdpInErrors.setStatus("mandatory")
_VrIpUdpOutDatagrams_Type = Counter32
_VrIpUdpOutDatagrams_Object = MibTableColumn
vrIpUdpOutDatagrams = _VrIpUdpOutDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 14, 10, 1, 4),
    _VrIpUdpOutDatagrams_Type()
)
vrIpUdpOutDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpUdpOutDatagrams.setStatus("mandatory")
_VrIpTcp_ObjectIdentity = ObjectIdentity
vrIpTcp = _VrIpTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15)
)
_VrIpTcpRowStatusTable_Object = MibTable
vrIpTcpRowStatusTable = _VrIpTcpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 1)
)
if mibBuilder.loadTexts:
    vrIpTcpRowStatusTable.setStatus("mandatory")
_VrIpTcpRowStatusEntry_Object = MibTableRow
vrIpTcpRowStatusEntry = _VrIpTcpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 1, 1)
)
vrIpTcpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpTcpIndex"),
)
if mibBuilder.loadTexts:
    vrIpTcpRowStatusEntry.setStatus("mandatory")
_VrIpTcpRowStatus_Type = RowStatus
_VrIpTcpRowStatus_Object = MibTableColumn
vrIpTcpRowStatus = _VrIpTcpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 1, 1, 1),
    _VrIpTcpRowStatus_Type()
)
vrIpTcpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTcpRowStatus.setStatus("mandatory")
_VrIpTcpComponentName_Type = DisplayString
_VrIpTcpComponentName_Object = MibTableColumn
vrIpTcpComponentName = _VrIpTcpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 1, 1, 2),
    _VrIpTcpComponentName_Type()
)
vrIpTcpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTcpComponentName.setStatus("mandatory")
_VrIpTcpStorageType_Type = StorageType
_VrIpTcpStorageType_Object = MibTableColumn
vrIpTcpStorageType = _VrIpTcpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 1, 1, 4),
    _VrIpTcpStorageType_Type()
)
vrIpTcpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTcpStorageType.setStatus("mandatory")
_VrIpTcpIndex_Type = NonReplicated
_VrIpTcpIndex_Object = MibTableColumn
vrIpTcpIndex = _VrIpTcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 1, 1, 10),
    _VrIpTcpIndex_Type()
)
vrIpTcpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpTcpIndex.setStatus("mandatory")
_VrIpTcpTcpEntry_ObjectIdentity = ObjectIdentity
vrIpTcpTcpEntry = _VrIpTcpTcpEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 2)
)
_VrIpTcpTcpEntryRowStatusTable_Object = MibTable
vrIpTcpTcpEntryRowStatusTable = _VrIpTcpTcpEntryRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpTcpTcpEntryRowStatusTable.setStatus("mandatory")
_VrIpTcpTcpEntryRowStatusEntry_Object = MibTableRow
vrIpTcpTcpEntryRowStatusEntry = _VrIpTcpTcpEntryRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 2, 1, 1)
)
vrIpTcpTcpEntryRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpTcpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpTcpTcpEntryLocalAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpTcpTcpEntryLocalPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpTcpTcpEntryRemoteAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpTcpTcpEntryRemotePortIndex"),
)
if mibBuilder.loadTexts:
    vrIpTcpTcpEntryRowStatusEntry.setStatus("mandatory")
_VrIpTcpTcpEntryRowStatus_Type = RowStatus
_VrIpTcpTcpEntryRowStatus_Object = MibTableColumn
vrIpTcpTcpEntryRowStatus = _VrIpTcpTcpEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 2, 1, 1, 1),
    _VrIpTcpTcpEntryRowStatus_Type()
)
vrIpTcpTcpEntryRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTcpTcpEntryRowStatus.setStatus("mandatory")
_VrIpTcpTcpEntryComponentName_Type = DisplayString
_VrIpTcpTcpEntryComponentName_Object = MibTableColumn
vrIpTcpTcpEntryComponentName = _VrIpTcpTcpEntryComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 2, 1, 1, 2),
    _VrIpTcpTcpEntryComponentName_Type()
)
vrIpTcpTcpEntryComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTcpTcpEntryComponentName.setStatus("mandatory")
_VrIpTcpTcpEntryStorageType_Type = StorageType
_VrIpTcpTcpEntryStorageType_Object = MibTableColumn
vrIpTcpTcpEntryStorageType = _VrIpTcpTcpEntryStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 2, 1, 1, 4),
    _VrIpTcpTcpEntryStorageType_Type()
)
vrIpTcpTcpEntryStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTcpTcpEntryStorageType.setStatus("mandatory")
_VrIpTcpTcpEntryLocalAddressIndex_Type = IpAddress
_VrIpTcpTcpEntryLocalAddressIndex_Object = MibTableColumn
vrIpTcpTcpEntryLocalAddressIndex = _VrIpTcpTcpEntryLocalAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 2, 1, 1, 10),
    _VrIpTcpTcpEntryLocalAddressIndex_Type()
)
vrIpTcpTcpEntryLocalAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpTcpTcpEntryLocalAddressIndex.setStatus("mandatory")


class _VrIpTcpTcpEntryLocalPortIndex_Type(Integer32):
    """Custom type vrIpTcpTcpEntryLocalPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpTcpTcpEntryLocalPortIndex_Type.__name__ = "Integer32"
_VrIpTcpTcpEntryLocalPortIndex_Object = MibTableColumn
vrIpTcpTcpEntryLocalPortIndex = _VrIpTcpTcpEntryLocalPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 2, 1, 1, 11),
    _VrIpTcpTcpEntryLocalPortIndex_Type()
)
vrIpTcpTcpEntryLocalPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpTcpTcpEntryLocalPortIndex.setStatus("mandatory")
_VrIpTcpTcpEntryRemoteAddressIndex_Type = IpAddress
_VrIpTcpTcpEntryRemoteAddressIndex_Object = MibTableColumn
vrIpTcpTcpEntryRemoteAddressIndex = _VrIpTcpTcpEntryRemoteAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 2, 1, 1, 12),
    _VrIpTcpTcpEntryRemoteAddressIndex_Type()
)
vrIpTcpTcpEntryRemoteAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpTcpTcpEntryRemoteAddressIndex.setStatus("mandatory")


class _VrIpTcpTcpEntryRemotePortIndex_Type(Integer32):
    """Custom type vrIpTcpTcpEntryRemotePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpTcpTcpEntryRemotePortIndex_Type.__name__ = "Integer32"
_VrIpTcpTcpEntryRemotePortIndex_Object = MibTableColumn
vrIpTcpTcpEntryRemotePortIndex = _VrIpTcpTcpEntryRemotePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 2, 1, 1, 13),
    _VrIpTcpTcpEntryRemotePortIndex_Type()
)
vrIpTcpTcpEntryRemotePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpTcpTcpEntryRemotePortIndex.setStatus("mandatory")
_VrIpTcpTcpEntryOperTable_Object = MibTable
vrIpTcpTcpEntryOperTable = _VrIpTcpTcpEntryOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpTcpTcpEntryOperTable.setStatus("mandatory")
_VrIpTcpTcpEntryOperEntry_Object = MibTableRow
vrIpTcpTcpEntryOperEntry = _VrIpTcpTcpEntryOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 2, 10, 1)
)
vrIpTcpTcpEntryOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpTcpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpTcpTcpEntryLocalAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpTcpTcpEntryLocalPortIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpTcpTcpEntryRemoteAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpTcpTcpEntryRemotePortIndex"),
)
if mibBuilder.loadTexts:
    vrIpTcpTcpEntryOperEntry.setStatus("mandatory")


class _VrIpTcpTcpEntryState_Type(Integer32):
    """Custom type vrIpTcpTcpEntryState based on Integer32"""
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


_VrIpTcpTcpEntryState_Type.__name__ = "Integer32"
_VrIpTcpTcpEntryState_Object = MibTableColumn
vrIpTcpTcpEntryState = _VrIpTcpTcpEntryState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 2, 10, 1, 1),
    _VrIpTcpTcpEntryState_Type()
)
vrIpTcpTcpEntryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpTcpTcpEntryState.setStatus("mandatory")
_VrIpTcpStatsTable_Object = MibTable
vrIpTcpStatsTable = _VrIpTcpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 10)
)
if mibBuilder.loadTexts:
    vrIpTcpStatsTable.setStatus("mandatory")
_VrIpTcpStatsEntry_Object = MibTableRow
vrIpTcpStatsEntry = _VrIpTcpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 10, 1)
)
vrIpTcpStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpTcpIndex"),
)
if mibBuilder.loadTexts:
    vrIpTcpStatsEntry.setStatus("mandatory")


class _VrIpTcpRToAlgorithm_Type(Integer32):
    """Custom type vrIpTcpRToAlgorithm based on Integer32"""
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


_VrIpTcpRToAlgorithm_Type.__name__ = "Integer32"
_VrIpTcpRToAlgorithm_Object = MibTableColumn
vrIpTcpRToAlgorithm = _VrIpTcpRToAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 10, 1, 1),
    _VrIpTcpRToAlgorithm_Type()
)
vrIpTcpRToAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTcpRToAlgorithm.setStatus("mandatory")


class _VrIpTcpRToMin_Type(Unsigned32):
    """Custom type vrIpTcpRToMin based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpTcpRToMin_Type.__name__ = "Unsigned32"
_VrIpTcpRToMin_Object = MibTableColumn
vrIpTcpRToMin = _VrIpTcpRToMin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 10, 1, 2),
    _VrIpTcpRToMin_Type()
)
vrIpTcpRToMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTcpRToMin.setStatus("mandatory")


class _VrIpTcpRToMax_Type(Unsigned32):
    """Custom type vrIpTcpRToMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpTcpRToMax_Type.__name__ = "Unsigned32"
_VrIpTcpRToMax_Object = MibTableColumn
vrIpTcpRToMax = _VrIpTcpRToMax_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 10, 1, 3),
    _VrIpTcpRToMax_Type()
)
vrIpTcpRToMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTcpRToMax.setStatus("mandatory")


class _VrIpTcpMaxConn_Type(Integer32):
    """Custom type vrIpTcpMaxConn based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
    )


_VrIpTcpMaxConn_Type.__name__ = "Integer32"
_VrIpTcpMaxConn_Object = MibTableColumn
vrIpTcpMaxConn = _VrIpTcpMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 10, 1, 4),
    _VrIpTcpMaxConn_Type()
)
vrIpTcpMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTcpMaxConn.setStatus("mandatory")
_VrIpTcpActiveOpens_Type = Counter32
_VrIpTcpActiveOpens_Object = MibTableColumn
vrIpTcpActiveOpens = _VrIpTcpActiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 10, 1, 5),
    _VrIpTcpActiveOpens_Type()
)
vrIpTcpActiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTcpActiveOpens.setStatus("mandatory")
_VrIpTcpPassiveOpens_Type = Counter32
_VrIpTcpPassiveOpens_Object = MibTableColumn
vrIpTcpPassiveOpens = _VrIpTcpPassiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 10, 1, 6),
    _VrIpTcpPassiveOpens_Type()
)
vrIpTcpPassiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTcpPassiveOpens.setStatus("mandatory")
_VrIpTcpAttemptFails_Type = Counter32
_VrIpTcpAttemptFails_Object = MibTableColumn
vrIpTcpAttemptFails = _VrIpTcpAttemptFails_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 10, 1, 7),
    _VrIpTcpAttemptFails_Type()
)
vrIpTcpAttemptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTcpAttemptFails.setStatus("mandatory")
_VrIpTcpEstabResets_Type = Counter32
_VrIpTcpEstabResets_Object = MibTableColumn
vrIpTcpEstabResets = _VrIpTcpEstabResets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 10, 1, 8),
    _VrIpTcpEstabResets_Type()
)
vrIpTcpEstabResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTcpEstabResets.setStatus("mandatory")


class _VrIpTcpCurrEstab_Type(Gauge32):
    """Custom type vrIpTcpCurrEstab based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpTcpCurrEstab_Type.__name__ = "Gauge32"
_VrIpTcpCurrEstab_Object = MibTableColumn
vrIpTcpCurrEstab = _VrIpTcpCurrEstab_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 10, 1, 9),
    _VrIpTcpCurrEstab_Type()
)
vrIpTcpCurrEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTcpCurrEstab.setStatus("mandatory")
_VrIpTcpInSegs_Type = Counter32
_VrIpTcpInSegs_Object = MibTableColumn
vrIpTcpInSegs = _VrIpTcpInSegs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 10, 1, 10),
    _VrIpTcpInSegs_Type()
)
vrIpTcpInSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTcpInSegs.setStatus("mandatory")
_VrIpTcpOutSegs_Type = Counter32
_VrIpTcpOutSegs_Object = MibTableColumn
vrIpTcpOutSegs = _VrIpTcpOutSegs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 10, 1, 11),
    _VrIpTcpOutSegs_Type()
)
vrIpTcpOutSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTcpOutSegs.setStatus("mandatory")
_VrIpTcpRetransSegs_Type = Counter32
_VrIpTcpRetransSegs_Object = MibTableColumn
vrIpTcpRetransSegs = _VrIpTcpRetransSegs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 10, 1, 12),
    _VrIpTcpRetransSegs_Type()
)
vrIpTcpRetransSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTcpRetransSegs.setStatus("mandatory")
_VrIpTcpInErrs_Type = Counter32
_VrIpTcpInErrs_Object = MibTableColumn
vrIpTcpInErrs = _VrIpTcpInErrs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 10, 1, 13),
    _VrIpTcpInErrs_Type()
)
vrIpTcpInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTcpInErrs.setStatus("mandatory")
_VrIpTcpOutRsts_Type = Counter32
_VrIpTcpOutRsts_Object = MibTableColumn
vrIpTcpOutRsts = _VrIpTcpOutRsts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 15, 10, 1, 14),
    _VrIpTcpOutRsts_Type()
)
vrIpTcpOutRsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTcpOutRsts.setStatus("mandatory")
_VrIpBootp_ObjectIdentity = ObjectIdentity
vrIpBootp = _VrIpBootp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16)
)
_VrIpBootpRowStatusTable_Object = MibTable
vrIpBootpRowStatusTable = _VrIpBootpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 1)
)
if mibBuilder.loadTexts:
    vrIpBootpRowStatusTable.setStatus("mandatory")
_VrIpBootpRowStatusEntry_Object = MibTableRow
vrIpBootpRowStatusEntry = _VrIpBootpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 1, 1)
)
vrIpBootpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpBootpIndex"),
)
if mibBuilder.loadTexts:
    vrIpBootpRowStatusEntry.setStatus("mandatory")
_VrIpBootpRowStatus_Type = RowStatus
_VrIpBootpRowStatus_Object = MibTableColumn
vrIpBootpRowStatus = _VrIpBootpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 1, 1, 1),
    _VrIpBootpRowStatus_Type()
)
vrIpBootpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBootpRowStatus.setStatus("mandatory")
_VrIpBootpComponentName_Type = DisplayString
_VrIpBootpComponentName_Object = MibTableColumn
vrIpBootpComponentName = _VrIpBootpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 1, 1, 2),
    _VrIpBootpComponentName_Type()
)
vrIpBootpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBootpComponentName.setStatus("mandatory")
_VrIpBootpStorageType_Type = StorageType
_VrIpBootpStorageType_Object = MibTableColumn
vrIpBootpStorageType = _VrIpBootpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 1, 1, 4),
    _VrIpBootpStorageType_Type()
)
vrIpBootpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBootpStorageType.setStatus("mandatory")
_VrIpBootpIndex_Type = NonReplicated
_VrIpBootpIndex_Object = MibTableColumn
vrIpBootpIndex = _VrIpBootpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 1, 1, 10),
    _VrIpBootpIndex_Type()
)
vrIpBootpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpBootpIndex.setStatus("mandatory")
_VrIpBootpPpE_ObjectIdentity = ObjectIdentity
vrIpBootpPpE = _VrIpBootpPpE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 2)
)
_VrIpBootpPpERowStatusTable_Object = MibTable
vrIpBootpPpERowStatusTable = _VrIpBootpPpERowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpBootpPpERowStatusTable.setStatus("mandatory")
_VrIpBootpPpERowStatusEntry_Object = MibTableRow
vrIpBootpPpERowStatusEntry = _VrIpBootpPpERowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 2, 1, 1)
)
vrIpBootpPpERowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpBootpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpBootpPpEIndex"),
)
if mibBuilder.loadTexts:
    vrIpBootpPpERowStatusEntry.setStatus("mandatory")
_VrIpBootpPpERowStatus_Type = RowStatus
_VrIpBootpPpERowStatus_Object = MibTableColumn
vrIpBootpPpERowStatus = _VrIpBootpPpERowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 2, 1, 1, 1),
    _VrIpBootpPpERowStatus_Type()
)
vrIpBootpPpERowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBootpPpERowStatus.setStatus("mandatory")
_VrIpBootpPpEComponentName_Type = DisplayString
_VrIpBootpPpEComponentName_Object = MibTableColumn
vrIpBootpPpEComponentName = _VrIpBootpPpEComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 2, 1, 1, 2),
    _VrIpBootpPpEComponentName_Type()
)
vrIpBootpPpEComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBootpPpEComponentName.setStatus("mandatory")
_VrIpBootpPpEStorageType_Type = StorageType
_VrIpBootpPpEStorageType_Object = MibTableColumn
vrIpBootpPpEStorageType = _VrIpBootpPpEStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 2, 1, 1, 4),
    _VrIpBootpPpEStorageType_Type()
)
vrIpBootpPpEStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBootpPpEStorageType.setStatus("mandatory")


class _VrIpBootpPpEIndex_Type(AsciiStringIndex):
    """Custom type vrIpBootpPpEIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_VrIpBootpPpEIndex_Type.__name__ = "AsciiStringIndex"
_VrIpBootpPpEIndex_Object = MibTableColumn
vrIpBootpPpEIndex = _VrIpBootpPpEIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 2, 1, 1, 10),
    _VrIpBootpPpEIndex_Type()
)
vrIpBootpPpEIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpBootpPpEIndex.setStatus("mandatory")
_VrIpBootpPpEOperTable_Object = MibTable
vrIpBootpPpEOperTable = _VrIpBootpPpEOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpBootpPpEOperTable.setStatus("mandatory")
_VrIpBootpPpEOperEntry_Object = MibTableRow
vrIpBootpPpEOperEntry = _VrIpBootpPpEOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 2, 10, 1)
)
vrIpBootpPpEOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpBootpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpBootpPpEIndex"),
)
if mibBuilder.loadTexts:
    vrIpBootpPpEOperEntry.setStatus("mandatory")


class _VrIpBootpPpEStatus_Type(Integer32):
    """Custom type vrIpBootpPpEStatus based on Integer32"""
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


_VrIpBootpPpEStatus_Type.__name__ = "Integer32"
_VrIpBootpPpEStatus_Object = MibTableColumn
vrIpBootpPpEStatus = _VrIpBootpPpEStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 2, 10, 1, 1),
    _VrIpBootpPpEStatus_Type()
)
vrIpBootpPpEStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBootpPpEStatus.setStatus("mandatory")
_VrIpBootpPpEStatsTable_Object = MibTable
vrIpBootpPpEStatsTable = _VrIpBootpPpEStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 2, 11)
)
if mibBuilder.loadTexts:
    vrIpBootpPpEStatsTable.setStatus("mandatory")
_VrIpBootpPpEStatsEntry_Object = MibTableRow
vrIpBootpPpEStatsEntry = _VrIpBootpPpEStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 2, 11, 1)
)
vrIpBootpPpEStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpBootpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpBootpPpEIndex"),
)
if mibBuilder.loadTexts:
    vrIpBootpPpEStatsEntry.setStatus("mandatory")
_VrIpBootpPpEInRequests_Type = Counter32
_VrIpBootpPpEInRequests_Object = MibTableColumn
vrIpBootpPpEInRequests = _VrIpBootpPpEInRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 2, 11, 1, 1),
    _VrIpBootpPpEInRequests_Type()
)
vrIpBootpPpEInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBootpPpEInRequests.setStatus("mandatory")
_VrIpBootpPpEInReplies_Type = Counter32
_VrIpBootpPpEInReplies_Object = MibTableColumn
vrIpBootpPpEInReplies = _VrIpBootpPpEInReplies_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 2, 11, 1, 2),
    _VrIpBootpPpEInReplies_Type()
)
vrIpBootpPpEInReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBootpPpEInReplies.setStatus("mandatory")
_VrIpBootpPpEOutRequests_Type = Counter32
_VrIpBootpPpEOutRequests_Object = MibTableColumn
vrIpBootpPpEOutRequests = _VrIpBootpPpEOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 2, 11, 1, 3),
    _VrIpBootpPpEOutRequests_Type()
)
vrIpBootpPpEOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBootpPpEOutRequests.setStatus("mandatory")
_VrIpBootpPpEOutReplies_Type = Counter32
_VrIpBootpPpEOutReplies_Object = MibTableColumn
vrIpBootpPpEOutReplies = _VrIpBootpPpEOutReplies_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 2, 11, 1, 4),
    _VrIpBootpPpEOutReplies_Type()
)
vrIpBootpPpEOutReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBootpPpEOutReplies.setStatus("mandatory")
_VrIpBootpPpEInRequestErrors_Type = Counter32
_VrIpBootpPpEInRequestErrors_Object = MibTableColumn
vrIpBootpPpEInRequestErrors = _VrIpBootpPpEInRequestErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 2, 11, 1, 5),
    _VrIpBootpPpEInRequestErrors_Type()
)
vrIpBootpPpEInRequestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBootpPpEInRequestErrors.setStatus("mandatory")
_VrIpBootpPpEInReplyErrors_Type = Counter32
_VrIpBootpPpEInReplyErrors_Object = MibTableColumn
vrIpBootpPpEInReplyErrors = _VrIpBootpPpEInReplyErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 2, 11, 1, 6),
    _VrIpBootpPpEInReplyErrors_Type()
)
vrIpBootpPpEInReplyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBootpPpEInReplyErrors.setStatus("mandatory")
_VrIpBootpAdminControlTable_Object = MibTable
vrIpBootpAdminControlTable = _VrIpBootpAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 10)
)
if mibBuilder.loadTexts:
    vrIpBootpAdminControlTable.setStatus("mandatory")
_VrIpBootpAdminControlEntry_Object = MibTableRow
vrIpBootpAdminControlEntry = _VrIpBootpAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 10, 1)
)
vrIpBootpAdminControlEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpBootpIndex"),
)
if mibBuilder.loadTexts:
    vrIpBootpAdminControlEntry.setStatus("mandatory")


class _VrIpBootpSnmpAdminStatus_Type(Integer32):
    """Custom type vrIpBootpSnmpAdminStatus based on Integer32"""
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


_VrIpBootpSnmpAdminStatus_Type.__name__ = "Integer32"
_VrIpBootpSnmpAdminStatus_Object = MibTableColumn
vrIpBootpSnmpAdminStatus = _VrIpBootpSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 10, 1, 1),
    _VrIpBootpSnmpAdminStatus_Type()
)
vrIpBootpSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBootpSnmpAdminStatus.setStatus("mandatory")
_VrIpBootpProvTable_Object = MibTable
vrIpBootpProvTable = _VrIpBootpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 11)
)
if mibBuilder.loadTexts:
    vrIpBootpProvTable.setStatus("mandatory")
_VrIpBootpProvEntry_Object = MibTableRow
vrIpBootpProvEntry = _VrIpBootpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 11, 1)
)
vrIpBootpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpBootpIndex"),
)
if mibBuilder.loadTexts:
    vrIpBootpProvEntry.setStatus("mandatory")


class _VrIpBootpHopDiscardThreshold_Type(Unsigned32):
    """Custom type vrIpBootpHopDiscardThreshold based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 16),
    )


_VrIpBootpHopDiscardThreshold_Type.__name__ = "Unsigned32"
_VrIpBootpHopDiscardThreshold_Object = MibTableColumn
vrIpBootpHopDiscardThreshold = _VrIpBootpHopDiscardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 11, 1, 1),
    _VrIpBootpHopDiscardThreshold_Type()
)
vrIpBootpHopDiscardThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBootpHopDiscardThreshold.setStatus("mandatory")
_VrIpBootpStateTable_Object = MibTable
vrIpBootpStateTable = _VrIpBootpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 12)
)
if mibBuilder.loadTexts:
    vrIpBootpStateTable.setStatus("mandatory")
_VrIpBootpStateEntry_Object = MibTableRow
vrIpBootpStateEntry = _VrIpBootpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 12, 1)
)
vrIpBootpStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpBootpIndex"),
)
if mibBuilder.loadTexts:
    vrIpBootpStateEntry.setStatus("mandatory")


class _VrIpBootpAdminState_Type(Integer32):
    """Custom type vrIpBootpAdminState based on Integer32"""
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


_VrIpBootpAdminState_Type.__name__ = "Integer32"
_VrIpBootpAdminState_Object = MibTableColumn
vrIpBootpAdminState = _VrIpBootpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 12, 1, 1),
    _VrIpBootpAdminState_Type()
)
vrIpBootpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBootpAdminState.setStatus("mandatory")


class _VrIpBootpOperationalState_Type(Integer32):
    """Custom type vrIpBootpOperationalState based on Integer32"""
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


_VrIpBootpOperationalState_Type.__name__ = "Integer32"
_VrIpBootpOperationalState_Object = MibTableColumn
vrIpBootpOperationalState = _VrIpBootpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 12, 1, 2),
    _VrIpBootpOperationalState_Type()
)
vrIpBootpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBootpOperationalState.setStatus("mandatory")


class _VrIpBootpUsageState_Type(Integer32):
    """Custom type vrIpBootpUsageState based on Integer32"""
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


_VrIpBootpUsageState_Type.__name__ = "Integer32"
_VrIpBootpUsageState_Object = MibTableColumn
vrIpBootpUsageState = _VrIpBootpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 12, 1, 3),
    _VrIpBootpUsageState_Type()
)
vrIpBootpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBootpUsageState.setStatus("mandatory")
_VrIpBootpOperStatusTable_Object = MibTable
vrIpBootpOperStatusTable = _VrIpBootpOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 13)
)
if mibBuilder.loadTexts:
    vrIpBootpOperStatusTable.setStatus("mandatory")
_VrIpBootpOperStatusEntry_Object = MibTableRow
vrIpBootpOperStatusEntry = _VrIpBootpOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 13, 1)
)
vrIpBootpOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpBootpIndex"),
)
if mibBuilder.loadTexts:
    vrIpBootpOperStatusEntry.setStatus("mandatory")


class _VrIpBootpSnmpOperStatus_Type(Integer32):
    """Custom type vrIpBootpSnmpOperStatus based on Integer32"""
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


_VrIpBootpSnmpOperStatus_Type.__name__ = "Integer32"
_VrIpBootpSnmpOperStatus_Object = MibTableColumn
vrIpBootpSnmpOperStatus = _VrIpBootpSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 16, 13, 1, 1),
    _VrIpBootpSnmpOperStatus_Type()
)
vrIpBootpSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBootpSnmpOperStatus.setStatus("mandatory")
_VrIpCache_ObjectIdentity = ObjectIdentity
vrIpCache = _VrIpCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 17)
)
_VrIpCacheRowStatusTable_Object = MibTable
vrIpCacheRowStatusTable = _VrIpCacheRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 17, 1)
)
if mibBuilder.loadTexts:
    vrIpCacheRowStatusTable.setStatus("mandatory")
_VrIpCacheRowStatusEntry_Object = MibTableRow
vrIpCacheRowStatusEntry = _VrIpCacheRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 17, 1, 1)
)
vrIpCacheRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpCacheIndex"),
)
if mibBuilder.loadTexts:
    vrIpCacheRowStatusEntry.setStatus("mandatory")
_VrIpCacheRowStatus_Type = RowStatus
_VrIpCacheRowStatus_Object = MibTableColumn
vrIpCacheRowStatus = _VrIpCacheRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 17, 1, 1, 1),
    _VrIpCacheRowStatus_Type()
)
vrIpCacheRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpCacheRowStatus.setStatus("mandatory")
_VrIpCacheComponentName_Type = DisplayString
_VrIpCacheComponentName_Object = MibTableColumn
vrIpCacheComponentName = _VrIpCacheComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 17, 1, 1, 2),
    _VrIpCacheComponentName_Type()
)
vrIpCacheComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpCacheComponentName.setStatus("mandatory")
_VrIpCacheStorageType_Type = StorageType
_VrIpCacheStorageType_Object = MibTableColumn
vrIpCacheStorageType = _VrIpCacheStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 17, 1, 1, 4),
    _VrIpCacheStorageType_Type()
)
vrIpCacheStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpCacheStorageType.setStatus("mandatory")


class _VrIpCacheIndex_Type(Integer32):
    """Custom type vrIpCacheIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_VrIpCacheIndex_Type.__name__ = "Integer32"
_VrIpCacheIndex_Object = MibTableColumn
vrIpCacheIndex = _VrIpCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 17, 1, 1, 10),
    _VrIpCacheIndex_Type()
)
vrIpCacheIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpCacheIndex.setStatus("mandatory")
_VrIpCacheStateTable_Object = MibTable
vrIpCacheStateTable = _VrIpCacheStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 17, 10)
)
if mibBuilder.loadTexts:
    vrIpCacheStateTable.setStatus("mandatory")
_VrIpCacheStateEntry_Object = MibTableRow
vrIpCacheStateEntry = _VrIpCacheStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 17, 10, 1)
)
vrIpCacheStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpCacheIndex"),
)
if mibBuilder.loadTexts:
    vrIpCacheStateEntry.setStatus("mandatory")


class _VrIpCacheAdminState_Type(Integer32):
    """Custom type vrIpCacheAdminState based on Integer32"""
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


_VrIpCacheAdminState_Type.__name__ = "Integer32"
_VrIpCacheAdminState_Object = MibTableColumn
vrIpCacheAdminState = _VrIpCacheAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 17, 10, 1, 1),
    _VrIpCacheAdminState_Type()
)
vrIpCacheAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpCacheAdminState.setStatus("mandatory")


class _VrIpCacheOperationalState_Type(Integer32):
    """Custom type vrIpCacheOperationalState based on Integer32"""
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


_VrIpCacheOperationalState_Type.__name__ = "Integer32"
_VrIpCacheOperationalState_Object = MibTableColumn
vrIpCacheOperationalState = _VrIpCacheOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 17, 10, 1, 2),
    _VrIpCacheOperationalState_Type()
)
vrIpCacheOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpCacheOperationalState.setStatus("mandatory")


class _VrIpCacheUsageState_Type(Integer32):
    """Custom type vrIpCacheUsageState based on Integer32"""
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


_VrIpCacheUsageState_Type.__name__ = "Integer32"
_VrIpCacheUsageState_Object = MibTableColumn
vrIpCacheUsageState = _VrIpCacheUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 17, 10, 1, 3),
    _VrIpCacheUsageState_Type()
)
vrIpCacheUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpCacheUsageState.setStatus("mandatory")
_VrIpCacheOperTable_Object = MibTable
vrIpCacheOperTable = _VrIpCacheOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 17, 11)
)
if mibBuilder.loadTexts:
    vrIpCacheOperTable.setStatus("mandatory")
_VrIpCacheOperEntry_Object = MibTableRow
vrIpCacheOperEntry = _VrIpCacheOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 17, 11, 1)
)
vrIpCacheOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpCacheIndex"),
)
if mibBuilder.loadTexts:
    vrIpCacheOperEntry.setStatus("mandatory")


class _VrIpCacheEntriesFree_Type(Unsigned32):
    """Custom type vrIpCacheEntriesFree based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_VrIpCacheEntriesFree_Type.__name__ = "Unsigned32"
_VrIpCacheEntriesFree_Object = MibTableColumn
vrIpCacheEntriesFree = _VrIpCacheEntriesFree_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 17, 11, 1, 3),
    _VrIpCacheEntriesFree_Type()
)
vrIpCacheEntriesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpCacheEntriesFree.setStatus("mandatory")


class _VrIpCacheTotalLookups_Type(Unsigned32):
    """Custom type vrIpCacheTotalLookups based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpCacheTotalLookups_Type.__name__ = "Unsigned32"
_VrIpCacheTotalLookups_Object = MibTableColumn
vrIpCacheTotalLookups = _VrIpCacheTotalLookups_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 17, 11, 1, 4),
    _VrIpCacheTotalLookups_Type()
)
vrIpCacheTotalLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpCacheTotalLookups.setStatus("mandatory")
_VrIpCacheLookupMisses_Type = Counter32
_VrIpCacheLookupMisses_Object = MibTableColumn
vrIpCacheLookupMisses = _VrIpCacheLookupMisses_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 17, 11, 1, 5),
    _VrIpCacheLookupMisses_Type()
)
vrIpCacheLookupMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpCacheLookupMisses.setStatus("mandatory")


class _VrIpCacheCacheTableMaxEntries_Type(Unsigned32):
    """Custom type vrIpCacheCacheTableMaxEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_VrIpCacheCacheTableMaxEntries_Type.__name__ = "Unsigned32"
_VrIpCacheCacheTableMaxEntries_Object = MibTableColumn
vrIpCacheCacheTableMaxEntries = _VrIpCacheCacheTableMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 17, 11, 1, 395),
    _VrIpCacheCacheTableMaxEntries_Type()
)
vrIpCacheCacheTableMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpCacheCacheTableMaxEntries.setStatus("mandatory")
_VrIpTunnel_ObjectIdentity = ObjectIdentity
vrIpTunnel = _VrIpTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18)
)
_VrIpTunnelRowStatusTable_Object = MibTable
vrIpTunnelRowStatusTable = _VrIpTunnelRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 1)
)
if mibBuilder.loadTexts:
    vrIpTunnelRowStatusTable.setStatus("mandatory")
_VrIpTunnelRowStatusEntry_Object = MibTableRow
vrIpTunnelRowStatusEntry = _VrIpTunnelRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 1, 1)
)
vrIpTunnelRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpTunnelIndex"),
)
if mibBuilder.loadTexts:
    vrIpTunnelRowStatusEntry.setStatus("mandatory")
_VrIpTunnelRowStatus_Type = RowStatus
_VrIpTunnelRowStatus_Object = MibTableColumn
vrIpTunnelRowStatus = _VrIpTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 1, 1, 1),
    _VrIpTunnelRowStatus_Type()
)
vrIpTunnelRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpTunnelRowStatus.setStatus("mandatory")
_VrIpTunnelComponentName_Type = DisplayString
_VrIpTunnelComponentName_Object = MibTableColumn
vrIpTunnelComponentName = _VrIpTunnelComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 1, 1, 2),
    _VrIpTunnelComponentName_Type()
)
vrIpTunnelComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTunnelComponentName.setStatus("mandatory")
_VrIpTunnelStorageType_Type = StorageType
_VrIpTunnelStorageType_Object = MibTableColumn
vrIpTunnelStorageType = _VrIpTunnelStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 1, 1, 4),
    _VrIpTunnelStorageType_Type()
)
vrIpTunnelStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTunnelStorageType.setStatus("mandatory")
_VrIpTunnelIndex_Type = NonReplicated
_VrIpTunnelIndex_Object = MibTableColumn
vrIpTunnelIndex = _VrIpTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 1, 1, 10),
    _VrIpTunnelIndex_Type()
)
vrIpTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpTunnelIndex.setStatus("mandatory")
_VrIpTunnelSep_ObjectIdentity = ObjectIdentity
vrIpTunnelSep = _VrIpTunnelSep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 2)
)
_VrIpTunnelSepRowStatusTable_Object = MibTable
vrIpTunnelSepRowStatusTable = _VrIpTunnelSepRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpTunnelSepRowStatusTable.setStatus("mandatory")
_VrIpTunnelSepRowStatusEntry_Object = MibTableRow
vrIpTunnelSepRowStatusEntry = _VrIpTunnelSepRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 2, 1, 1)
)
vrIpTunnelSepRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpTunnelIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpTunnelSepIndex"),
)
if mibBuilder.loadTexts:
    vrIpTunnelSepRowStatusEntry.setStatus("mandatory")
_VrIpTunnelSepRowStatus_Type = RowStatus
_VrIpTunnelSepRowStatus_Object = MibTableColumn
vrIpTunnelSepRowStatus = _VrIpTunnelSepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 2, 1, 1, 1),
    _VrIpTunnelSepRowStatus_Type()
)
vrIpTunnelSepRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpTunnelSepRowStatus.setStatus("mandatory")
_VrIpTunnelSepComponentName_Type = DisplayString
_VrIpTunnelSepComponentName_Object = MibTableColumn
vrIpTunnelSepComponentName = _VrIpTunnelSepComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 2, 1, 1, 2),
    _VrIpTunnelSepComponentName_Type()
)
vrIpTunnelSepComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTunnelSepComponentName.setStatus("mandatory")
_VrIpTunnelSepStorageType_Type = StorageType
_VrIpTunnelSepStorageType_Object = MibTableColumn
vrIpTunnelSepStorageType = _VrIpTunnelSepStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 2, 1, 1, 4),
    _VrIpTunnelSepStorageType_Type()
)
vrIpTunnelSepStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTunnelSepStorageType.setStatus("mandatory")


class _VrIpTunnelSepIndex_Type(Integer32):
    """Custom type vrIpTunnelSepIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_VrIpTunnelSepIndex_Type.__name__ = "Integer32"
_VrIpTunnelSepIndex_Object = MibTableColumn
vrIpTunnelSepIndex = _VrIpTunnelSepIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 2, 1, 1, 10),
    _VrIpTunnelSepIndex_Type()
)
vrIpTunnelSepIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpTunnelSepIndex.setStatus("mandatory")
_VrIpTunnelSepIfEntryTable_Object = MibTable
vrIpTunnelSepIfEntryTable = _VrIpTunnelSepIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpTunnelSepIfEntryTable.setStatus("mandatory")
_VrIpTunnelSepIfEntryEntry_Object = MibTableRow
vrIpTunnelSepIfEntryEntry = _VrIpTunnelSepIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 2, 10, 1)
)
vrIpTunnelSepIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpTunnelIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpTunnelSepIndex"),
)
if mibBuilder.loadTexts:
    vrIpTunnelSepIfEntryEntry.setStatus("mandatory")


class _VrIpTunnelSepIfAdminStatus_Type(Integer32):
    """Custom type vrIpTunnelSepIfAdminStatus based on Integer32"""
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


_VrIpTunnelSepIfAdminStatus_Type.__name__ = "Integer32"
_VrIpTunnelSepIfAdminStatus_Object = MibTableColumn
vrIpTunnelSepIfAdminStatus = _VrIpTunnelSepIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 2, 10, 1, 1),
    _VrIpTunnelSepIfAdminStatus_Type()
)
vrIpTunnelSepIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpTunnelSepIfAdminStatus.setStatus("mandatory")


class _VrIpTunnelSepIfIndex_Type(InterfaceIndex):
    """Custom type vrIpTunnelSepIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrIpTunnelSepIfIndex_Type.__name__ = "InterfaceIndex"
_VrIpTunnelSepIfIndex_Object = MibTableColumn
vrIpTunnelSepIfIndex = _VrIpTunnelSepIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 2, 10, 1, 2),
    _VrIpTunnelSepIfIndex_Type()
)
vrIpTunnelSepIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTunnelSepIfIndex.setStatus("mandatory")
_VrIpTunnelSepMpTable_Object = MibTable
vrIpTunnelSepMpTable = _VrIpTunnelSepMpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 2, 11)
)
if mibBuilder.loadTexts:
    vrIpTunnelSepMpTable.setStatus("mandatory")
_VrIpTunnelSepMpEntry_Object = MibTableRow
vrIpTunnelSepMpEntry = _VrIpTunnelSepMpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 2, 11, 1)
)
vrIpTunnelSepMpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpTunnelIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpTunnelSepIndex"),
)
if mibBuilder.loadTexts:
    vrIpTunnelSepMpEntry.setStatus("mandatory")
_VrIpTunnelSepLinkToProtocolPort_Type = Link
_VrIpTunnelSepLinkToProtocolPort_Object = MibTableColumn
vrIpTunnelSepLinkToProtocolPort = _VrIpTunnelSepLinkToProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 2, 11, 1, 1),
    _VrIpTunnelSepLinkToProtocolPort_Type()
)
vrIpTunnelSepLinkToProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpTunnelSepLinkToProtocolPort.setStatus("mandatory")
_VrIpTunnelSepProvTable_Object = MibTable
vrIpTunnelSepProvTable = _VrIpTunnelSepProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 2, 12)
)
if mibBuilder.loadTexts:
    vrIpTunnelSepProvTable.setStatus("mandatory")
_VrIpTunnelSepProvEntry_Object = MibTableRow
vrIpTunnelSepProvEntry = _VrIpTunnelSepProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 2, 12, 1)
)
vrIpTunnelSepProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpTunnelIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpTunnelSepIndex"),
)
if mibBuilder.loadTexts:
    vrIpTunnelSepProvEntry.setStatus("mandatory")


class _VrIpTunnelSepEncapType_Type(Integer32):
    """Custom type vrIpTunnelSepEncapType based on Integer32"""
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


_VrIpTunnelSepEncapType_Type.__name__ = "Integer32"
_VrIpTunnelSepEncapType_Object = MibTableColumn
vrIpTunnelSepEncapType = _VrIpTunnelSepEncapType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 2, 12, 1, 1),
    _VrIpTunnelSepEncapType_Type()
)
vrIpTunnelSepEncapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpTunnelSepEncapType.setStatus("mandatory")


class _VrIpTunnelSepSourceAddress_Type(IpAddress):
    """Custom type vrIpTunnelSepSourceAddress based on IpAddress"""
    defaultHexValue = "00000000"


_VrIpTunnelSepSourceAddress_Object = MibTableColumn
vrIpTunnelSepSourceAddress = _VrIpTunnelSepSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 2, 12, 1, 2),
    _VrIpTunnelSepSourceAddress_Type()
)
vrIpTunnelSepSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpTunnelSepSourceAddress.setStatus("mandatory")


class _VrIpTunnelSepDestinationAddress_Type(IpAddress):
    """Custom type vrIpTunnelSepDestinationAddress based on IpAddress"""
    defaultHexValue = "00000000"


_VrIpTunnelSepDestinationAddress_Object = MibTableColumn
vrIpTunnelSepDestinationAddress = _VrIpTunnelSepDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 2, 12, 1, 3),
    _VrIpTunnelSepDestinationAddress_Type()
)
vrIpTunnelSepDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpTunnelSepDestinationAddress.setStatus("mandatory")
_VrIpTunnelSepOperTable_Object = MibTable
vrIpTunnelSepOperTable = _VrIpTunnelSepOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 2, 14)
)
if mibBuilder.loadTexts:
    vrIpTunnelSepOperTable.setStatus("mandatory")
_VrIpTunnelSepOperEntry_Object = MibTableRow
vrIpTunnelSepOperEntry = _VrIpTunnelSepOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 2, 14, 1)
)
vrIpTunnelSepOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpTunnelIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpTunnelSepIndex"),
)
if mibBuilder.loadTexts:
    vrIpTunnelSepOperEntry.setStatus("mandatory")


class _VrIpTunnelSepPathMtu_Type(Unsigned32):
    """Custom type vrIpTunnelSepPathMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 18944),
    )


_VrIpTunnelSepPathMtu_Type.__name__ = "Unsigned32"
_VrIpTunnelSepPathMtu_Object = MibTableColumn
vrIpTunnelSepPathMtu = _VrIpTunnelSepPathMtu_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 2, 14, 1, 1),
    _VrIpTunnelSepPathMtu_Type()
)
vrIpTunnelSepPathMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTunnelSepPathMtu.setStatus("mandatory")
_VrIpTunnelStateTable_Object = MibTable
vrIpTunnelStateTable = _VrIpTunnelStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 10)
)
if mibBuilder.loadTexts:
    vrIpTunnelStateTable.setStatus("mandatory")
_VrIpTunnelStateEntry_Object = MibTableRow
vrIpTunnelStateEntry = _VrIpTunnelStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 10, 1)
)
vrIpTunnelStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpTunnelIndex"),
)
if mibBuilder.loadTexts:
    vrIpTunnelStateEntry.setStatus("mandatory")


class _VrIpTunnelAdminState_Type(Integer32):
    """Custom type vrIpTunnelAdminState based on Integer32"""
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


_VrIpTunnelAdminState_Type.__name__ = "Integer32"
_VrIpTunnelAdminState_Object = MibTableColumn
vrIpTunnelAdminState = _VrIpTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 10, 1, 1),
    _VrIpTunnelAdminState_Type()
)
vrIpTunnelAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTunnelAdminState.setStatus("mandatory")


class _VrIpTunnelOperationalState_Type(Integer32):
    """Custom type vrIpTunnelOperationalState based on Integer32"""
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


_VrIpTunnelOperationalState_Type.__name__ = "Integer32"
_VrIpTunnelOperationalState_Object = MibTableColumn
vrIpTunnelOperationalState = _VrIpTunnelOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 10, 1, 2),
    _VrIpTunnelOperationalState_Type()
)
vrIpTunnelOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTunnelOperationalState.setStatus("mandatory")


class _VrIpTunnelUsageState_Type(Integer32):
    """Custom type vrIpTunnelUsageState based on Integer32"""
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


_VrIpTunnelUsageState_Type.__name__ = "Integer32"
_VrIpTunnelUsageState_Object = MibTableColumn
vrIpTunnelUsageState = _VrIpTunnelUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 18, 10, 1, 3),
    _VrIpTunnelUsageState_Type()
)
vrIpTunnelUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpTunnelUsageState.setStatus("mandatory")
_VrIpMcast_ObjectIdentity = ObjectIdentity
vrIpMcast = _VrIpMcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26)
)
_VrIpMcastRowStatusTable_Object = MibTable
vrIpMcastRowStatusTable = _VrIpMcastRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 1)
)
if mibBuilder.loadTexts:
    vrIpMcastRowStatusTable.setStatus("mandatory")
_VrIpMcastRowStatusEntry_Object = MibTableRow
vrIpMcastRowStatusEntry = _VrIpMcastRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 1, 1)
)
vrIpMcastRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastRowStatusEntry.setStatus("mandatory")
_VrIpMcastRowStatus_Type = RowStatus
_VrIpMcastRowStatus_Object = MibTableColumn
vrIpMcastRowStatus = _VrIpMcastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 1, 1, 1),
    _VrIpMcastRowStatus_Type()
)
vrIpMcastRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpMcastRowStatus.setStatus("mandatory")
_VrIpMcastComponentName_Type = DisplayString
_VrIpMcastComponentName_Object = MibTableColumn
vrIpMcastComponentName = _VrIpMcastComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 1, 1, 2),
    _VrIpMcastComponentName_Type()
)
vrIpMcastComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastComponentName.setStatus("mandatory")
_VrIpMcastStorageType_Type = StorageType
_VrIpMcastStorageType_Object = MibTableColumn
vrIpMcastStorageType = _VrIpMcastStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 1, 1, 4),
    _VrIpMcastStorageType_Type()
)
vrIpMcastStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastStorageType.setStatus("mandatory")
_VrIpMcastIndex_Type = NonReplicated
_VrIpMcastIndex_Object = MibTableColumn
vrIpMcastIndex = _VrIpMcastIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 1, 1, 10),
    _VrIpMcastIndex_Type()
)
vrIpMcastIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastIndex.setStatus("mandatory")
_VrIpMcastIgmp_ObjectIdentity = ObjectIdentity
vrIpMcastIgmp = _VrIpMcastIgmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2)
)
_VrIpMcastIgmpRowStatusTable_Object = MibTable
vrIpMcastIgmpRowStatusTable = _VrIpMcastIgmpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpMcastIgmpRowStatusTable.setStatus("mandatory")
_VrIpMcastIgmpRowStatusEntry_Object = MibTableRow
vrIpMcastIgmpRowStatusEntry = _VrIpMcastIgmpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 1, 1)
)
vrIpMcastIgmpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIgmpIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastIgmpRowStatusEntry.setStatus("mandatory")
_VrIpMcastIgmpRowStatus_Type = RowStatus
_VrIpMcastIgmpRowStatus_Object = MibTableColumn
vrIpMcastIgmpRowStatus = _VrIpMcastIgmpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 1, 1, 1),
    _VrIpMcastIgmpRowStatus_Type()
)
vrIpMcastIgmpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpMcastIgmpRowStatus.setStatus("mandatory")
_VrIpMcastIgmpComponentName_Type = DisplayString
_VrIpMcastIgmpComponentName_Object = MibTableColumn
vrIpMcastIgmpComponentName = _VrIpMcastIgmpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 1, 1, 2),
    _VrIpMcastIgmpComponentName_Type()
)
vrIpMcastIgmpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastIgmpComponentName.setStatus("mandatory")
_VrIpMcastIgmpStorageType_Type = StorageType
_VrIpMcastIgmpStorageType_Object = MibTableColumn
vrIpMcastIgmpStorageType = _VrIpMcastIgmpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 1, 1, 4),
    _VrIpMcastIgmpStorageType_Type()
)
vrIpMcastIgmpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastIgmpStorageType.setStatus("mandatory")
_VrIpMcastIgmpIndex_Type = NonReplicated
_VrIpMcastIgmpIndex_Object = MibTableColumn
vrIpMcastIgmpIndex = _VrIpMcastIgmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 1, 1, 10),
    _VrIpMcastIgmpIndex_Type()
)
vrIpMcastIgmpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastIgmpIndex.setStatus("mandatory")
_VrIpMcastIgmpGc_ObjectIdentity = ObjectIdentity
vrIpMcastIgmpGc = _VrIpMcastIgmpGc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 2)
)
_VrIpMcastIgmpGcRowStatusTable_Object = MibTable
vrIpMcastIgmpGcRowStatusTable = _VrIpMcastIgmpGcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpMcastIgmpGcRowStatusTable.setStatus("mandatory")
_VrIpMcastIgmpGcRowStatusEntry_Object = MibTableRow
vrIpMcastIgmpGcRowStatusEntry = _VrIpMcastIgmpGcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 2, 1, 1)
)
vrIpMcastIgmpGcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIgmpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIgmpGcGAddrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIgmpGcDomainIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIgmpGcProtocolportStringIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastIgmpGcRowStatusEntry.setStatus("mandatory")
_VrIpMcastIgmpGcRowStatus_Type = RowStatus
_VrIpMcastIgmpGcRowStatus_Object = MibTableColumn
vrIpMcastIgmpGcRowStatus = _VrIpMcastIgmpGcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 2, 1, 1, 1),
    _VrIpMcastIgmpGcRowStatus_Type()
)
vrIpMcastIgmpGcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastIgmpGcRowStatus.setStatus("mandatory")
_VrIpMcastIgmpGcComponentName_Type = DisplayString
_VrIpMcastIgmpGcComponentName_Object = MibTableColumn
vrIpMcastIgmpGcComponentName = _VrIpMcastIgmpGcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 2, 1, 1, 2),
    _VrIpMcastIgmpGcComponentName_Type()
)
vrIpMcastIgmpGcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastIgmpGcComponentName.setStatus("mandatory")
_VrIpMcastIgmpGcStorageType_Type = StorageType
_VrIpMcastIgmpGcStorageType_Object = MibTableColumn
vrIpMcastIgmpGcStorageType = _VrIpMcastIgmpGcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 2, 1, 1, 4),
    _VrIpMcastIgmpGcStorageType_Type()
)
vrIpMcastIgmpGcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastIgmpGcStorageType.setStatus("mandatory")
_VrIpMcastIgmpGcGAddrIndex_Type = IpAddress
_VrIpMcastIgmpGcGAddrIndex_Object = MibTableColumn
vrIpMcastIgmpGcGAddrIndex = _VrIpMcastIgmpGcGAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 2, 1, 1, 10),
    _VrIpMcastIgmpGcGAddrIndex_Type()
)
vrIpMcastIgmpGcGAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastIgmpGcGAddrIndex.setStatus("mandatory")


class _VrIpMcastIgmpGcDomainIndex_Type(Integer32):
    """Custom type vrIpMcastIgmpGcDomainIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_VrIpMcastIgmpGcDomainIndex_Type.__name__ = "Integer32"
_VrIpMcastIgmpGcDomainIndex_Object = MibTableColumn
vrIpMcastIgmpGcDomainIndex = _VrIpMcastIgmpGcDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 2, 1, 1, 11),
    _VrIpMcastIgmpGcDomainIndex_Type()
)
vrIpMcastIgmpGcDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastIgmpGcDomainIndex.setStatus("mandatory")


class _VrIpMcastIgmpGcProtocolportStringIndex_Type(AsciiStringIndex):
    """Custom type vrIpMcastIgmpGcProtocolportStringIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_VrIpMcastIgmpGcProtocolportStringIndex_Type.__name__ = "AsciiStringIndex"
_VrIpMcastIgmpGcProtocolportStringIndex_Object = MibTableColumn
vrIpMcastIgmpGcProtocolportStringIndex = _VrIpMcastIgmpGcProtocolportStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 2, 1, 1, 12),
    _VrIpMcastIgmpGcProtocolportStringIndex_Type()
)
vrIpMcastIgmpGcProtocolportStringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastIgmpGcProtocolportStringIndex.setStatus("mandatory")
_VrIpMcastIgmpGcOperTable_Object = MibTable
vrIpMcastIgmpGcOperTable = _VrIpMcastIgmpGcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 2, 11)
)
if mibBuilder.loadTexts:
    vrIpMcastIgmpGcOperTable.setStatus("mandatory")
_VrIpMcastIgmpGcOperEntry_Object = MibTableRow
vrIpMcastIgmpGcOperEntry = _VrIpMcastIgmpGcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 2, 11, 1)
)
vrIpMcastIgmpGcOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIgmpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIgmpGcGAddrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIgmpGcDomainIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIgmpGcProtocolportStringIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastIgmpGcOperEntry.setStatus("mandatory")


class _VrIpMcastIgmpGcUpTime_Type(EnterpriseDateAndTime):
    """Custom type vrIpMcastIgmpGcUpTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_VrIpMcastIgmpGcUpTime_Type.__name__ = "EnterpriseDateAndTime"
_VrIpMcastIgmpGcUpTime_Object = MibTableColumn
vrIpMcastIgmpGcUpTime = _VrIpMcastIgmpGcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 2, 11, 1, 1),
    _VrIpMcastIgmpGcUpTime_Type()
)
vrIpMcastIgmpGcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastIgmpGcUpTime.setStatus("mandatory")


class _VrIpMcastIgmpGcExpiryTime_Type(EnterpriseDateAndTime):
    """Custom type vrIpMcastIgmpGcExpiryTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_VrIpMcastIgmpGcExpiryTime_Type.__name__ = "EnterpriseDateAndTime"
_VrIpMcastIgmpGcExpiryTime_Object = MibTableColumn
vrIpMcastIgmpGcExpiryTime = _VrIpMcastIgmpGcExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 2, 11, 1, 2),
    _VrIpMcastIgmpGcExpiryTime_Type()
)
vrIpMcastIgmpGcExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastIgmpGcExpiryTime.setStatus("mandatory")


class _VrIpMcastIgmpGcLastReporter_Type(IpAddress):
    """Custom type vrIpMcastIgmpGcLastReporter based on IpAddress"""
    defaultHexValue = "00000000"


_VrIpMcastIgmpGcLastReporter_Object = MibTableColumn
vrIpMcastIgmpGcLastReporter = _VrIpMcastIgmpGcLastReporter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 2, 11, 1, 3),
    _VrIpMcastIgmpGcLastReporter_Type()
)
vrIpMcastIgmpGcLastReporter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastIgmpGcLastReporter.setStatus("mandatory")


class _VrIpMcastIgmpGcVersion1HostTimer_Type(Unsigned32):
    """Custom type vrIpMcastIgmpGcVersion1HostTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpMcastIgmpGcVersion1HostTimer_Type.__name__ = "Unsigned32"
_VrIpMcastIgmpGcVersion1HostTimer_Object = MibTableColumn
vrIpMcastIgmpGcVersion1HostTimer = _VrIpMcastIgmpGcVersion1HostTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 2, 11, 1, 4),
    _VrIpMcastIgmpGcVersion1HostTimer_Type()
)
vrIpMcastIgmpGcVersion1HostTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastIgmpGcVersion1HostTimer.setStatus("mandatory")
_VrIpMcastIgmpAdminControlTable_Object = MibTable
vrIpMcastIgmpAdminControlTable = _VrIpMcastIgmpAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpMcastIgmpAdminControlTable.setStatus("mandatory")
_VrIpMcastIgmpAdminControlEntry_Object = MibTableRow
vrIpMcastIgmpAdminControlEntry = _VrIpMcastIgmpAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 10, 1)
)
vrIpMcastIgmpAdminControlEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIgmpIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastIgmpAdminControlEntry.setStatus("mandatory")


class _VrIpMcastIgmpSnmpAdminStatus_Type(Integer32):
    """Custom type vrIpMcastIgmpSnmpAdminStatus based on Integer32"""
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


_VrIpMcastIgmpSnmpAdminStatus_Type.__name__ = "Integer32"
_VrIpMcastIgmpSnmpAdminStatus_Object = MibTableColumn
vrIpMcastIgmpSnmpAdminStatus = _VrIpMcastIgmpSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 10, 1, 1),
    _VrIpMcastIgmpSnmpAdminStatus_Type()
)
vrIpMcastIgmpSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpMcastIgmpSnmpAdminStatus.setStatus("mandatory")
_VrIpMcastIgmpStateTable_Object = MibTable
vrIpMcastIgmpStateTable = _VrIpMcastIgmpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 12)
)
if mibBuilder.loadTexts:
    vrIpMcastIgmpStateTable.setStatus("mandatory")
_VrIpMcastIgmpStateEntry_Object = MibTableRow
vrIpMcastIgmpStateEntry = _VrIpMcastIgmpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 12, 1)
)
vrIpMcastIgmpStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIgmpIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastIgmpStateEntry.setStatus("mandatory")


class _VrIpMcastIgmpAdminState_Type(Integer32):
    """Custom type vrIpMcastIgmpAdminState based on Integer32"""
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


_VrIpMcastIgmpAdminState_Type.__name__ = "Integer32"
_VrIpMcastIgmpAdminState_Object = MibTableColumn
vrIpMcastIgmpAdminState = _VrIpMcastIgmpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 12, 1, 1),
    _VrIpMcastIgmpAdminState_Type()
)
vrIpMcastIgmpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastIgmpAdminState.setStatus("mandatory")


class _VrIpMcastIgmpOperationalState_Type(Integer32):
    """Custom type vrIpMcastIgmpOperationalState based on Integer32"""
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


_VrIpMcastIgmpOperationalState_Type.__name__ = "Integer32"
_VrIpMcastIgmpOperationalState_Object = MibTableColumn
vrIpMcastIgmpOperationalState = _VrIpMcastIgmpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 12, 1, 2),
    _VrIpMcastIgmpOperationalState_Type()
)
vrIpMcastIgmpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastIgmpOperationalState.setStatus("mandatory")


class _VrIpMcastIgmpUsageState_Type(Integer32):
    """Custom type vrIpMcastIgmpUsageState based on Integer32"""
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


_VrIpMcastIgmpUsageState_Type.__name__ = "Integer32"
_VrIpMcastIgmpUsageState_Object = MibTableColumn
vrIpMcastIgmpUsageState = _VrIpMcastIgmpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 12, 1, 3),
    _VrIpMcastIgmpUsageState_Type()
)
vrIpMcastIgmpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastIgmpUsageState.setStatus("mandatory")
_VrIpMcastIgmpOperStatusTable_Object = MibTable
vrIpMcastIgmpOperStatusTable = _VrIpMcastIgmpOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 13)
)
if mibBuilder.loadTexts:
    vrIpMcastIgmpOperStatusTable.setStatus("mandatory")
_VrIpMcastIgmpOperStatusEntry_Object = MibTableRow
vrIpMcastIgmpOperStatusEntry = _VrIpMcastIgmpOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 13, 1)
)
vrIpMcastIgmpOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIgmpIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastIgmpOperStatusEntry.setStatus("mandatory")


class _VrIpMcastIgmpSnmpOperStatus_Type(Integer32):
    """Custom type vrIpMcastIgmpSnmpOperStatus based on Integer32"""
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


_VrIpMcastIgmpSnmpOperStatus_Type.__name__ = "Integer32"
_VrIpMcastIgmpSnmpOperStatus_Object = MibTableColumn
vrIpMcastIgmpSnmpOperStatus = _VrIpMcastIgmpSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 2, 13, 1, 1),
    _VrIpMcastIgmpSnmpOperStatus_Type()
)
vrIpMcastIgmpSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastIgmpSnmpOperStatus.setStatus("mandatory")
_VrIpMcastStatic_ObjectIdentity = ObjectIdentity
vrIpMcastStatic = _VrIpMcastStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 3)
)
_VrIpMcastStaticRowStatusTable_Object = MibTable
vrIpMcastStaticRowStatusTable = _VrIpMcastStaticRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 3, 1)
)
if mibBuilder.loadTexts:
    vrIpMcastStaticRowStatusTable.setStatus("mandatory")
_VrIpMcastStaticRowStatusEntry_Object = MibTableRow
vrIpMcastStaticRowStatusEntry = _VrIpMcastStaticRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 3, 1, 1)
)
vrIpMcastStaticRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastStaticIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastStaticRowStatusEntry.setStatus("mandatory")
_VrIpMcastStaticRowStatus_Type = RowStatus
_VrIpMcastStaticRowStatus_Object = MibTableColumn
vrIpMcastStaticRowStatus = _VrIpMcastStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 3, 1, 1, 1),
    _VrIpMcastStaticRowStatus_Type()
)
vrIpMcastStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpMcastStaticRowStatus.setStatus("mandatory")
_VrIpMcastStaticComponentName_Type = DisplayString
_VrIpMcastStaticComponentName_Object = MibTableColumn
vrIpMcastStaticComponentName = _VrIpMcastStaticComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 3, 1, 1, 2),
    _VrIpMcastStaticComponentName_Type()
)
vrIpMcastStaticComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastStaticComponentName.setStatus("mandatory")
_VrIpMcastStaticStorageType_Type = StorageType
_VrIpMcastStaticStorageType_Object = MibTableColumn
vrIpMcastStaticStorageType = _VrIpMcastStaticStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 3, 1, 1, 4),
    _VrIpMcastStaticStorageType_Type()
)
vrIpMcastStaticStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastStaticStorageType.setStatus("mandatory")
_VrIpMcastStaticIndex_Type = NonReplicated
_VrIpMcastStaticIndex_Object = MibTableColumn
vrIpMcastStaticIndex = _VrIpMcastStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 3, 1, 1, 10),
    _VrIpMcastStaticIndex_Type()
)
vrIpMcastStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastStaticIndex.setStatus("mandatory")
_VrIpMcastStaticRoute_ObjectIdentity = ObjectIdentity
vrIpMcastStaticRoute = _VrIpMcastStaticRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 3, 2)
)
_VrIpMcastStaticRouteRowStatusTable_Object = MibTable
vrIpMcastStaticRouteRowStatusTable = _VrIpMcastStaticRouteRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 3, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpMcastStaticRouteRowStatusTable.setStatus("mandatory")
_VrIpMcastStaticRouteRowStatusEntry_Object = MibTableRow
vrIpMcastStaticRouteRowStatusEntry = _VrIpMcastStaticRouteRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 3, 2, 1, 1)
)
vrIpMcastStaticRouteRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastStaticIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastStaticRouteGAddrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastStaticRouteDomainIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastStaticRouteRowStatusEntry.setStatus("mandatory")
_VrIpMcastStaticRouteRowStatus_Type = RowStatus
_VrIpMcastStaticRouteRowStatus_Object = MibTableColumn
vrIpMcastStaticRouteRowStatus = _VrIpMcastStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 3, 2, 1, 1, 1),
    _VrIpMcastStaticRouteRowStatus_Type()
)
vrIpMcastStaticRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpMcastStaticRouteRowStatus.setStatus("mandatory")
_VrIpMcastStaticRouteComponentName_Type = DisplayString
_VrIpMcastStaticRouteComponentName_Object = MibTableColumn
vrIpMcastStaticRouteComponentName = _VrIpMcastStaticRouteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 3, 2, 1, 1, 2),
    _VrIpMcastStaticRouteComponentName_Type()
)
vrIpMcastStaticRouteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastStaticRouteComponentName.setStatus("mandatory")
_VrIpMcastStaticRouteStorageType_Type = StorageType
_VrIpMcastStaticRouteStorageType_Object = MibTableColumn
vrIpMcastStaticRouteStorageType = _VrIpMcastStaticRouteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 3, 2, 1, 1, 4),
    _VrIpMcastStaticRouteStorageType_Type()
)
vrIpMcastStaticRouteStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastStaticRouteStorageType.setStatus("mandatory")
_VrIpMcastStaticRouteGAddrIndex_Type = IpAddress
_VrIpMcastStaticRouteGAddrIndex_Object = MibTableColumn
vrIpMcastStaticRouteGAddrIndex = _VrIpMcastStaticRouteGAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 3, 2, 1, 1, 10),
    _VrIpMcastStaticRouteGAddrIndex_Type()
)
vrIpMcastStaticRouteGAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastStaticRouteGAddrIndex.setStatus("mandatory")


class _VrIpMcastStaticRouteDomainIndex_Type(Integer32):
    """Custom type vrIpMcastStaticRouteDomainIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_VrIpMcastStaticRouteDomainIndex_Type.__name__ = "Integer32"
_VrIpMcastStaticRouteDomainIndex_Object = MibTableColumn
vrIpMcastStaticRouteDomainIndex = _VrIpMcastStaticRouteDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 3, 2, 1, 1, 11),
    _VrIpMcastStaticRouteDomainIndex_Type()
)
vrIpMcastStaticRouteDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastStaticRouteDomainIndex.setStatus("mandatory")
_VrIpMcastStaticRouteOifsTable_Object = MibTable
vrIpMcastStaticRouteOifsTable = _VrIpMcastStaticRouteOifsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 3, 2, 705)
)
if mibBuilder.loadTexts:
    vrIpMcastStaticRouteOifsTable.setStatus("mandatory")
_VrIpMcastStaticRouteOifsEntry_Object = MibTableRow
vrIpMcastStaticRouteOifsEntry = _VrIpMcastStaticRouteOifsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 3, 2, 705, 1)
)
vrIpMcastStaticRouteOifsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastStaticIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastStaticRouteGAddrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastStaticRouteDomainIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastStaticRouteOifsValue"),
)
if mibBuilder.loadTexts:
    vrIpMcastStaticRouteOifsEntry.setStatus("mandatory")
_VrIpMcastStaticRouteOifsValue_Type = Link
_VrIpMcastStaticRouteOifsValue_Object = MibTableColumn
vrIpMcastStaticRouteOifsValue = _VrIpMcastStaticRouteOifsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 3, 2, 705, 1, 1),
    _VrIpMcastStaticRouteOifsValue_Type()
)
vrIpMcastStaticRouteOifsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpMcastStaticRouteOifsValue.setStatus("mandatory")
_VrIpMcastStaticRouteOifsRowStatus_Type = RowStatus
_VrIpMcastStaticRouteOifsRowStatus_Object = MibTableColumn
vrIpMcastStaticRouteOifsRowStatus = _VrIpMcastStaticRouteOifsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 3, 2, 705, 1, 2),
    _VrIpMcastStaticRouteOifsRowStatus_Type()
)
vrIpMcastStaticRouteOifsRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vrIpMcastStaticRouteOifsRowStatus.setStatus("mandatory")
_VrIpMcastStaticStateTable_Object = MibTable
vrIpMcastStaticStateTable = _VrIpMcastStaticStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 3, 10)
)
if mibBuilder.loadTexts:
    vrIpMcastStaticStateTable.setStatus("mandatory")
_VrIpMcastStaticStateEntry_Object = MibTableRow
vrIpMcastStaticStateEntry = _VrIpMcastStaticStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 3, 10, 1)
)
vrIpMcastStaticStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastStaticIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastStaticStateEntry.setStatus("mandatory")


class _VrIpMcastStaticAdminState_Type(Integer32):
    """Custom type vrIpMcastStaticAdminState based on Integer32"""
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


_VrIpMcastStaticAdminState_Type.__name__ = "Integer32"
_VrIpMcastStaticAdminState_Object = MibTableColumn
vrIpMcastStaticAdminState = _VrIpMcastStaticAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 3, 10, 1, 1),
    _VrIpMcastStaticAdminState_Type()
)
vrIpMcastStaticAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastStaticAdminState.setStatus("mandatory")


class _VrIpMcastStaticOperationalState_Type(Integer32):
    """Custom type vrIpMcastStaticOperationalState based on Integer32"""
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


_VrIpMcastStaticOperationalState_Type.__name__ = "Integer32"
_VrIpMcastStaticOperationalState_Object = MibTableColumn
vrIpMcastStaticOperationalState = _VrIpMcastStaticOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 3, 10, 1, 2),
    _VrIpMcastStaticOperationalState_Type()
)
vrIpMcastStaticOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastStaticOperationalState.setStatus("mandatory")


class _VrIpMcastStaticUsageState_Type(Integer32):
    """Custom type vrIpMcastStaticUsageState based on Integer32"""
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


_VrIpMcastStaticUsageState_Type.__name__ = "Integer32"
_VrIpMcastStaticUsageState_Object = MibTableColumn
vrIpMcastStaticUsageState = _VrIpMcastStaticUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 3, 10, 1, 3),
    _VrIpMcastStaticUsageState_Type()
)
vrIpMcastStaticUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastStaticUsageState.setStatus("mandatory")
_VrIpMcastPg_ObjectIdentity = ObjectIdentity
vrIpMcastPg = _VrIpMcastPg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 4)
)
_VrIpMcastPgRowStatusTable_Object = MibTable
vrIpMcastPgRowStatusTable = _VrIpMcastPgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 4, 1)
)
if mibBuilder.loadTexts:
    vrIpMcastPgRowStatusTable.setStatus("mandatory")
_VrIpMcastPgRowStatusEntry_Object = MibTableRow
vrIpMcastPgRowStatusEntry = _VrIpMcastPgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 4, 1, 1)
)
vrIpMcastPgRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPgIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastPgRowStatusEntry.setStatus("mandatory")
_VrIpMcastPgRowStatus_Type = RowStatus
_VrIpMcastPgRowStatus_Object = MibTableColumn
vrIpMcastPgRowStatus = _VrIpMcastPgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 4, 1, 1, 1),
    _VrIpMcastPgRowStatus_Type()
)
vrIpMcastPgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpMcastPgRowStatus.setStatus("mandatory")
_VrIpMcastPgComponentName_Type = DisplayString
_VrIpMcastPgComponentName_Object = MibTableColumn
vrIpMcastPgComponentName = _VrIpMcastPgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 4, 1, 1, 2),
    _VrIpMcastPgComponentName_Type()
)
vrIpMcastPgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPgComponentName.setStatus("mandatory")
_VrIpMcastPgStorageType_Type = StorageType
_VrIpMcastPgStorageType_Object = MibTableColumn
vrIpMcastPgStorageType = _VrIpMcastPgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 4, 1, 1, 4),
    _VrIpMcastPgStorageType_Type()
)
vrIpMcastPgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPgStorageType.setStatus("mandatory")


class _VrIpMcastPgIndex_Type(AsciiStringIndex):
    """Custom type vrIpMcastPgIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_VrIpMcastPgIndex_Type.__name__ = "AsciiStringIndex"
_VrIpMcastPgIndex_Object = MibTableColumn
vrIpMcastPgIndex = _VrIpMcastPgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 4, 1, 1, 10),
    _VrIpMcastPgIndex_Type()
)
vrIpMcastPgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastPgIndex.setStatus("mandatory")
_VrIpMcastPgGrp_ObjectIdentity = ObjectIdentity
vrIpMcastPgGrp = _VrIpMcastPgGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 4, 2)
)
_VrIpMcastPgGrpRowStatusTable_Object = MibTable
vrIpMcastPgGrpRowStatusTable = _VrIpMcastPgGrpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 4, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpMcastPgGrpRowStatusTable.setStatus("mandatory")
_VrIpMcastPgGrpRowStatusEntry_Object = MibTableRow
vrIpMcastPgGrpRowStatusEntry = _VrIpMcastPgGrpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 4, 2, 1, 1)
)
vrIpMcastPgGrpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPgIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPgGrpGAddrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPgGrpGMaskIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastPgGrpRowStatusEntry.setStatus("mandatory")
_VrIpMcastPgGrpRowStatus_Type = RowStatus
_VrIpMcastPgGrpRowStatus_Object = MibTableColumn
vrIpMcastPgGrpRowStatus = _VrIpMcastPgGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 4, 2, 1, 1, 1),
    _VrIpMcastPgGrpRowStatus_Type()
)
vrIpMcastPgGrpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpMcastPgGrpRowStatus.setStatus("mandatory")
_VrIpMcastPgGrpComponentName_Type = DisplayString
_VrIpMcastPgGrpComponentName_Object = MibTableColumn
vrIpMcastPgGrpComponentName = _VrIpMcastPgGrpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 4, 2, 1, 1, 2),
    _VrIpMcastPgGrpComponentName_Type()
)
vrIpMcastPgGrpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPgGrpComponentName.setStatus("mandatory")
_VrIpMcastPgGrpStorageType_Type = StorageType
_VrIpMcastPgGrpStorageType_Object = MibTableColumn
vrIpMcastPgGrpStorageType = _VrIpMcastPgGrpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 4, 2, 1, 1, 4),
    _VrIpMcastPgGrpStorageType_Type()
)
vrIpMcastPgGrpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPgGrpStorageType.setStatus("mandatory")
_VrIpMcastPgGrpGAddrIndex_Type = IpAddress
_VrIpMcastPgGrpGAddrIndex_Object = MibTableColumn
vrIpMcastPgGrpGAddrIndex = _VrIpMcastPgGrpGAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 4, 2, 1, 1, 10),
    _VrIpMcastPgGrpGAddrIndex_Type()
)
vrIpMcastPgGrpGAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastPgGrpGAddrIndex.setStatus("mandatory")
_VrIpMcastPgGrpGMaskIndex_Type = IpAddress
_VrIpMcastPgGrpGMaskIndex_Object = MibTableColumn
vrIpMcastPgGrpGMaskIndex = _VrIpMcastPgGrpGMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 4, 2, 1, 1, 11),
    _VrIpMcastPgGrpGMaskIndex_Type()
)
vrIpMcastPgGrpGMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastPgGrpGMaskIndex.setStatus("mandatory")
_VrIpMcastPgProvTable_Object = MibTable
vrIpMcastPgProvTable = _VrIpMcastPgProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 4, 10)
)
if mibBuilder.loadTexts:
    vrIpMcastPgProvTable.setStatus("mandatory")
_VrIpMcastPgProvEntry_Object = MibTableRow
vrIpMcastPgProvEntry = _VrIpMcastPgProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 4, 10, 1)
)
vrIpMcastPgProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPgIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastPgProvEntry.setStatus("mandatory")


class _VrIpMcastPgAction_Type(Integer32):
    """Custom type vrIpMcastPgAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 2),
          ("deny", 1))
    )


_VrIpMcastPgAction_Type.__name__ = "Integer32"
_VrIpMcastPgAction_Object = MibTableColumn
vrIpMcastPgAction = _VrIpMcastPgAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 4, 10, 1, 1),
    _VrIpMcastPgAction_Type()
)
vrIpMcastPgAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpMcastPgAction.setStatus("mandatory")
_VrIpMcastPgLinkToPolicyUserTable_Object = MibTable
vrIpMcastPgLinkToPolicyUserTable = _VrIpMcastPgLinkToPolicyUserTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 4, 704)
)
if mibBuilder.loadTexts:
    vrIpMcastPgLinkToPolicyUserTable.setStatus("mandatory")
_VrIpMcastPgLinkToPolicyUserEntry_Object = MibTableRow
vrIpMcastPgLinkToPolicyUserEntry = _VrIpMcastPgLinkToPolicyUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 4, 704, 1)
)
vrIpMcastPgLinkToPolicyUserEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPgIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPgLinkToPolicyUserValue"),
)
if mibBuilder.loadTexts:
    vrIpMcastPgLinkToPolicyUserEntry.setStatus("mandatory")
_VrIpMcastPgLinkToPolicyUserValue_Type = Link
_VrIpMcastPgLinkToPolicyUserValue_Object = MibTableColumn
vrIpMcastPgLinkToPolicyUserValue = _VrIpMcastPgLinkToPolicyUserValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 4, 704, 1, 1),
    _VrIpMcastPgLinkToPolicyUserValue_Type()
)
vrIpMcastPgLinkToPolicyUserValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpMcastPgLinkToPolicyUserValue.setStatus("mandatory")
_VrIpMcastPgLinkToPolicyUserRowStatus_Type = RowStatus
_VrIpMcastPgLinkToPolicyUserRowStatus_Object = MibTableColumn
vrIpMcastPgLinkToPolicyUserRowStatus = _VrIpMcastPgLinkToPolicyUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 4, 704, 1, 2),
    _VrIpMcastPgLinkToPolicyUserRowStatus_Type()
)
vrIpMcastPgLinkToPolicyUserRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vrIpMcastPgLinkToPolicyUserRowStatus.setStatus("mandatory")
_VrIpMcastDomain_ObjectIdentity = ObjectIdentity
vrIpMcastDomain = _VrIpMcastDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 5)
)
_VrIpMcastDomainRowStatusTable_Object = MibTable
vrIpMcastDomainRowStatusTable = _VrIpMcastDomainRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 5, 1)
)
if mibBuilder.loadTexts:
    vrIpMcastDomainRowStatusTable.setStatus("mandatory")
_VrIpMcastDomainRowStatusEntry_Object = MibTableRow
vrIpMcastDomainRowStatusEntry = _VrIpMcastDomainRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 5, 1, 1)
)
vrIpMcastDomainRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastDomainIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastDomainRowStatusEntry.setStatus("mandatory")
_VrIpMcastDomainRowStatus_Type = RowStatus
_VrIpMcastDomainRowStatus_Object = MibTableColumn
vrIpMcastDomainRowStatus = _VrIpMcastDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 5, 1, 1, 1),
    _VrIpMcastDomainRowStatus_Type()
)
vrIpMcastDomainRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpMcastDomainRowStatus.setStatus("mandatory")
_VrIpMcastDomainComponentName_Type = DisplayString
_VrIpMcastDomainComponentName_Object = MibTableColumn
vrIpMcastDomainComponentName = _VrIpMcastDomainComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 5, 1, 1, 2),
    _VrIpMcastDomainComponentName_Type()
)
vrIpMcastDomainComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastDomainComponentName.setStatus("mandatory")
_VrIpMcastDomainStorageType_Type = StorageType
_VrIpMcastDomainStorageType_Object = MibTableColumn
vrIpMcastDomainStorageType = _VrIpMcastDomainStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 5, 1, 1, 4),
    _VrIpMcastDomainStorageType_Type()
)
vrIpMcastDomainStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastDomainStorageType.setStatus("mandatory")


class _VrIpMcastDomainIndex_Type(Integer32):
    """Custom type vrIpMcastDomainIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_VrIpMcastDomainIndex_Type.__name__ = "Integer32"
_VrIpMcastDomainIndex_Object = MibTableColumn
vrIpMcastDomainIndex = _VrIpMcastDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 5, 1, 1, 10),
    _VrIpMcastDomainIndex_Type()
)
vrIpMcastDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastDomainIndex.setStatus("mandatory")
_VrIpMcastDomainOperTable_Object = MibTable
vrIpMcastDomainOperTable = _VrIpMcastDomainOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 5, 11)
)
if mibBuilder.loadTexts:
    vrIpMcastDomainOperTable.setStatus("mandatory")
_VrIpMcastDomainOperEntry_Object = MibTableRow
vrIpMcastDomainOperEntry = _VrIpMcastDomainOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 5, 11, 1)
)
vrIpMcastDomainOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastDomainIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastDomainOperEntry.setStatus("mandatory")


class _VrIpMcastDomainProtocolActive_Type(Integer32):
    """Custom type vrIpMcastDomainProtocolActive based on Integer32"""
    defaultValue = 0

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
        *(("dvmrp", 4),
          ("local", 3),
          ("none", 0),
          ("pimDm", 2),
          ("pimSm", 1))
    )


_VrIpMcastDomainProtocolActive_Type.__name__ = "Integer32"
_VrIpMcastDomainProtocolActive_Object = MibTableColumn
vrIpMcastDomainProtocolActive = _VrIpMcastDomainProtocolActive_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 5, 11, 1, 1),
    _VrIpMcastDomainProtocolActive_Type()
)
vrIpMcastDomainProtocolActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastDomainProtocolActive.setStatus("mandatory")
_VrIpMcastFwd_ObjectIdentity = ObjectIdentity
vrIpMcastFwd = _VrIpMcastFwd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6)
)
_VrIpMcastFwdRowStatusTable_Object = MibTable
vrIpMcastFwdRowStatusTable = _VrIpMcastFwdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 1)
)
if mibBuilder.loadTexts:
    vrIpMcastFwdRowStatusTable.setStatus("mandatory")
_VrIpMcastFwdRowStatusEntry_Object = MibTableRow
vrIpMcastFwdRowStatusEntry = _VrIpMcastFwdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 1, 1)
)
vrIpMcastFwdRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastFwdGAddrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastFwdDomainIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastFwdSrcAddrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastFwdSrcMaskIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastFwdRowStatusEntry.setStatus("mandatory")
_VrIpMcastFwdRowStatus_Type = RowStatus
_VrIpMcastFwdRowStatus_Object = MibTableColumn
vrIpMcastFwdRowStatus = _VrIpMcastFwdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 1, 1, 1),
    _VrIpMcastFwdRowStatus_Type()
)
vrIpMcastFwdRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastFwdRowStatus.setStatus("mandatory")
_VrIpMcastFwdComponentName_Type = DisplayString
_VrIpMcastFwdComponentName_Object = MibTableColumn
vrIpMcastFwdComponentName = _VrIpMcastFwdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 1, 1, 2),
    _VrIpMcastFwdComponentName_Type()
)
vrIpMcastFwdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastFwdComponentName.setStatus("mandatory")
_VrIpMcastFwdStorageType_Type = StorageType
_VrIpMcastFwdStorageType_Object = MibTableColumn
vrIpMcastFwdStorageType = _VrIpMcastFwdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 1, 1, 4),
    _VrIpMcastFwdStorageType_Type()
)
vrIpMcastFwdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastFwdStorageType.setStatus("mandatory")
_VrIpMcastFwdGAddrIndex_Type = IpAddress
_VrIpMcastFwdGAddrIndex_Object = MibTableColumn
vrIpMcastFwdGAddrIndex = _VrIpMcastFwdGAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 1, 1, 10),
    _VrIpMcastFwdGAddrIndex_Type()
)
vrIpMcastFwdGAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastFwdGAddrIndex.setStatus("mandatory")


class _VrIpMcastFwdDomainIndex_Type(Integer32):
    """Custom type vrIpMcastFwdDomainIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_VrIpMcastFwdDomainIndex_Type.__name__ = "Integer32"
_VrIpMcastFwdDomainIndex_Object = MibTableColumn
vrIpMcastFwdDomainIndex = _VrIpMcastFwdDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 1, 1, 11),
    _VrIpMcastFwdDomainIndex_Type()
)
vrIpMcastFwdDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastFwdDomainIndex.setStatus("mandatory")
_VrIpMcastFwdSrcAddrIndex_Type = IpAddress
_VrIpMcastFwdSrcAddrIndex_Object = MibTableColumn
vrIpMcastFwdSrcAddrIndex = _VrIpMcastFwdSrcAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 1, 1, 12),
    _VrIpMcastFwdSrcAddrIndex_Type()
)
vrIpMcastFwdSrcAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastFwdSrcAddrIndex.setStatus("mandatory")
_VrIpMcastFwdSrcMaskIndex_Type = IpAddress
_VrIpMcastFwdSrcMaskIndex_Object = MibTableColumn
vrIpMcastFwdSrcMaskIndex = _VrIpMcastFwdSrcMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 1, 1, 13),
    _VrIpMcastFwdSrcMaskIndex_Type()
)
vrIpMcastFwdSrcMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastFwdSrcMaskIndex.setStatus("mandatory")
_VrIpMcastFwdOif_ObjectIdentity = ObjectIdentity
vrIpMcastFwdOif = _VrIpMcastFwdOif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 2)
)
_VrIpMcastFwdOifRowStatusTable_Object = MibTable
vrIpMcastFwdOifRowStatusTable = _VrIpMcastFwdOifRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpMcastFwdOifRowStatusTable.setStatus("mandatory")
_VrIpMcastFwdOifRowStatusEntry_Object = MibTableRow
vrIpMcastFwdOifRowStatusEntry = _VrIpMcastFwdOifRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 2, 1, 1)
)
vrIpMcastFwdOifRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastFwdGAddrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastFwdDomainIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastFwdSrcAddrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastFwdSrcMaskIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastFwdOifOutIfAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastFwdOifConnectionIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastFwdOifRowStatusEntry.setStatus("mandatory")
_VrIpMcastFwdOifRowStatus_Type = RowStatus
_VrIpMcastFwdOifRowStatus_Object = MibTableColumn
vrIpMcastFwdOifRowStatus = _VrIpMcastFwdOifRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 2, 1, 1, 1),
    _VrIpMcastFwdOifRowStatus_Type()
)
vrIpMcastFwdOifRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastFwdOifRowStatus.setStatus("mandatory")
_VrIpMcastFwdOifComponentName_Type = DisplayString
_VrIpMcastFwdOifComponentName_Object = MibTableColumn
vrIpMcastFwdOifComponentName = _VrIpMcastFwdOifComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 2, 1, 1, 2),
    _VrIpMcastFwdOifComponentName_Type()
)
vrIpMcastFwdOifComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastFwdOifComponentName.setStatus("mandatory")
_VrIpMcastFwdOifStorageType_Type = StorageType
_VrIpMcastFwdOifStorageType_Object = MibTableColumn
vrIpMcastFwdOifStorageType = _VrIpMcastFwdOifStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 2, 1, 1, 4),
    _VrIpMcastFwdOifStorageType_Type()
)
vrIpMcastFwdOifStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastFwdOifStorageType.setStatus("mandatory")
_VrIpMcastFwdOifOutIfAddressIndex_Type = IpAddress
_VrIpMcastFwdOifOutIfAddressIndex_Object = MibTableColumn
vrIpMcastFwdOifOutIfAddressIndex = _VrIpMcastFwdOifOutIfAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 2, 1, 1, 10),
    _VrIpMcastFwdOifOutIfAddressIndex_Type()
)
vrIpMcastFwdOifOutIfAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastFwdOifOutIfAddressIndex.setStatus("mandatory")


class _VrIpMcastFwdOifConnectionIndex_Type(Integer32):
    """Custom type vrIpMcastFwdOifConnectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpMcastFwdOifConnectionIndex_Type.__name__ = "Integer32"
_VrIpMcastFwdOifConnectionIndex_Object = MibTableColumn
vrIpMcastFwdOifConnectionIndex = _VrIpMcastFwdOifConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 2, 1, 1, 11),
    _VrIpMcastFwdOifConnectionIndex_Type()
)
vrIpMcastFwdOifConnectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastFwdOifConnectionIndex.setStatus("mandatory")
_VrIpMcastFwdOifOperTable_Object = MibTable
vrIpMcastFwdOifOperTable = _VrIpMcastFwdOifOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpMcastFwdOifOperTable.setStatus("mandatory")
_VrIpMcastFwdOifOperEntry_Object = MibTableRow
vrIpMcastFwdOifOperEntry = _VrIpMcastFwdOifOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 2, 10, 1)
)
vrIpMcastFwdOifOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastFwdGAddrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastFwdDomainIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastFwdSrcAddrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastFwdSrcMaskIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastFwdOifOutIfAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastFwdOifConnectionIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastFwdOifOperEntry.setStatus("mandatory")


class _VrIpMcastFwdOifIfIndex_Type(InterfaceIndex):
    """Custom type vrIpMcastFwdOifIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrIpMcastFwdOifIfIndex_Type.__name__ = "InterfaceIndex"
_VrIpMcastFwdOifIfIndex_Object = MibTableColumn
vrIpMcastFwdOifIfIndex = _VrIpMcastFwdOifIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 2, 10, 1, 2),
    _VrIpMcastFwdOifIfIndex_Type()
)
vrIpMcastFwdOifIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastFwdOifIfIndex.setStatus("mandatory")


class _VrIpMcastFwdOifProtocol_Type(Integer32):
    """Custom type vrIpMcastFwdOifProtocol based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("cbt", 7),
          ("dvmrp", 4),
          ("igmponly", 10),
          ("local", 2),
          ("mospf", 5),
          ("netmgmt", 3),
          ("other", 1),
          ("pimDense", 9),
          ("pimSparse", 8),
          ("pimSparseDense", 6))
    )


_VrIpMcastFwdOifProtocol_Type.__name__ = "Integer32"
_VrIpMcastFwdOifProtocol_Object = MibTableColumn
vrIpMcastFwdOifProtocol = _VrIpMcastFwdOifProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 2, 10, 1, 3),
    _VrIpMcastFwdOifProtocol_Type()
)
vrIpMcastFwdOifProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastFwdOifProtocol.setStatus("mandatory")


class _VrIpMcastFwdOifAge_Type(Unsigned32):
    """Custom type vrIpMcastFwdOifAge based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpMcastFwdOifAge_Type.__name__ = "Unsigned32"
_VrIpMcastFwdOifAge_Object = MibTableColumn
vrIpMcastFwdOifAge = _VrIpMcastFwdOifAge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 2, 10, 1, 4),
    _VrIpMcastFwdOifAge_Type()
)
vrIpMcastFwdOifAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastFwdOifAge.setStatus("mandatory")
_VrIpMcastFwdOifOutProtocolPortName_Type = RowPointer
_VrIpMcastFwdOifOutProtocolPortName_Object = MibTableColumn
vrIpMcastFwdOifOutProtocolPortName = _VrIpMcastFwdOifOutProtocolPortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 2, 10, 1, 702),
    _VrIpMcastFwdOifOutProtocolPortName_Type()
)
vrIpMcastFwdOifOutProtocolPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastFwdOifOutProtocolPortName.setStatus("mandatory")
_VrIpMcastFwdOperTable_Object = MibTable
vrIpMcastFwdOperTable = _VrIpMcastFwdOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 10)
)
if mibBuilder.loadTexts:
    vrIpMcastFwdOperTable.setStatus("mandatory")
_VrIpMcastFwdOperEntry_Object = MibTableRow
vrIpMcastFwdOperEntry = _VrIpMcastFwdOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 10, 1)
)
vrIpMcastFwdOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastFwdGAddrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastFwdDomainIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastFwdSrcAddrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastFwdSrcMaskIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastFwdOperEntry.setStatus("mandatory")


class _VrIpMcastFwdAge_Type(Unsigned32):
    """Custom type vrIpMcastFwdAge based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpMcastFwdAge_Type.__name__ = "Unsigned32"
_VrIpMcastFwdAge_Object = MibTableColumn
vrIpMcastFwdAge = _VrIpMcastFwdAge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 10, 1, 2),
    _VrIpMcastFwdAge_Type()
)
vrIpMcastFwdAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastFwdAge.setStatus("mandatory")
_VrIpMcastFwdInProtocolPortName_Type = RowPointer
_VrIpMcastFwdInProtocolPortName_Object = MibTableColumn
vrIpMcastFwdInProtocolPortName = _VrIpMcastFwdInProtocolPortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 10, 1, 3),
    _VrIpMcastFwdInProtocolPortName_Type()
)
vrIpMcastFwdInProtocolPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastFwdInProtocolPortName.setStatus("mandatory")


class _VrIpMcastFwdProtocol_Type(Integer32):
    """Custom type vrIpMcastFwdProtocol based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("cbt", 7),
          ("dvmrp", 4),
          ("igmponly", 10),
          ("local", 2),
          ("mospf", 5),
          ("netmgmt", 3),
          ("other", 1),
          ("pimDense", 9),
          ("pimSparse", 8),
          ("pimSparseDense", 6))
    )


_VrIpMcastFwdProtocol_Type.__name__ = "Integer32"
_VrIpMcastFwdProtocol_Object = MibTableColumn
vrIpMcastFwdProtocol = _VrIpMcastFwdProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 10, 1, 4),
    _VrIpMcastFwdProtocol_Type()
)
vrIpMcastFwdProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastFwdProtocol.setStatus("mandatory")
_VrIpMcastFwdReversePathForwardingNeighbor_Type = IpAddress
_VrIpMcastFwdReversePathForwardingNeighbor_Object = MibTableColumn
vrIpMcastFwdReversePathForwardingNeighbor = _VrIpMcastFwdReversePathForwardingNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 10, 1, 5),
    _VrIpMcastFwdReversePathForwardingNeighbor_Type()
)
vrIpMcastFwdReversePathForwardingNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastFwdReversePathForwardingNeighbor.setStatus("mandatory")


class _VrIpMcastFwdFlags_Type(AsciiString):
    """Custom type vrIpMcastFwdFlags based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 20),
    )


_VrIpMcastFwdFlags_Type.__name__ = "AsciiString"
_VrIpMcastFwdFlags_Object = MibTableColumn
vrIpMcastFwdFlags = _VrIpMcastFwdFlags_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 6, 10, 1, 703),
    _VrIpMcastFwdFlags_Type()
)
vrIpMcastFwdFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastFwdFlags.setStatus("mandatory")
_VrIpMcastCacheStats_ObjectIdentity = ObjectIdentity
vrIpMcastCacheStats = _VrIpMcastCacheStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 8)
)
_VrIpMcastCacheStatsRowStatusTable_Object = MibTable
vrIpMcastCacheStatsRowStatusTable = _VrIpMcastCacheStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 8, 1)
)
if mibBuilder.loadTexts:
    vrIpMcastCacheStatsRowStatusTable.setStatus("mandatory")
_VrIpMcastCacheStatsRowStatusEntry_Object = MibTableRow
vrIpMcastCacheStatsRowStatusEntry = _VrIpMcastCacheStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 8, 1, 1)
)
vrIpMcastCacheStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastCacheStatsIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastCacheStatsRowStatusEntry.setStatus("mandatory")
_VrIpMcastCacheStatsRowStatus_Type = RowStatus
_VrIpMcastCacheStatsRowStatus_Object = MibTableColumn
vrIpMcastCacheStatsRowStatus = _VrIpMcastCacheStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 8, 1, 1, 1),
    _VrIpMcastCacheStatsRowStatus_Type()
)
vrIpMcastCacheStatsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastCacheStatsRowStatus.setStatus("mandatory")
_VrIpMcastCacheStatsComponentName_Type = DisplayString
_VrIpMcastCacheStatsComponentName_Object = MibTableColumn
vrIpMcastCacheStatsComponentName = _VrIpMcastCacheStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 8, 1, 1, 2),
    _VrIpMcastCacheStatsComponentName_Type()
)
vrIpMcastCacheStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastCacheStatsComponentName.setStatus("mandatory")
_VrIpMcastCacheStatsStorageType_Type = StorageType
_VrIpMcastCacheStatsStorageType_Object = MibTableColumn
vrIpMcastCacheStatsStorageType = _VrIpMcastCacheStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 8, 1, 1, 4),
    _VrIpMcastCacheStatsStorageType_Type()
)
vrIpMcastCacheStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastCacheStatsStorageType.setStatus("mandatory")


class _VrIpMcastCacheStatsIndex_Type(Integer32):
    """Custom type vrIpMcastCacheStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_VrIpMcastCacheStatsIndex_Type.__name__ = "Integer32"
_VrIpMcastCacheStatsIndex_Object = MibTableColumn
vrIpMcastCacheStatsIndex = _VrIpMcastCacheStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 8, 1, 1, 10),
    _VrIpMcastCacheStatsIndex_Type()
)
vrIpMcastCacheStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastCacheStatsIndex.setStatus("mandatory")
_VrIpMcastCacheStatsStateTable_Object = MibTable
vrIpMcastCacheStatsStateTable = _VrIpMcastCacheStatsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 8, 10)
)
if mibBuilder.loadTexts:
    vrIpMcastCacheStatsStateTable.setStatus("mandatory")
_VrIpMcastCacheStatsStateEntry_Object = MibTableRow
vrIpMcastCacheStatsStateEntry = _VrIpMcastCacheStatsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 8, 10, 1)
)
vrIpMcastCacheStatsStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastCacheStatsIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastCacheStatsStateEntry.setStatus("mandatory")


class _VrIpMcastCacheStatsAdminState_Type(Integer32):
    """Custom type vrIpMcastCacheStatsAdminState based on Integer32"""
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


_VrIpMcastCacheStatsAdminState_Type.__name__ = "Integer32"
_VrIpMcastCacheStatsAdminState_Object = MibTableColumn
vrIpMcastCacheStatsAdminState = _VrIpMcastCacheStatsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 8, 10, 1, 1),
    _VrIpMcastCacheStatsAdminState_Type()
)
vrIpMcastCacheStatsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastCacheStatsAdminState.setStatus("mandatory")


class _VrIpMcastCacheStatsOperationalState_Type(Integer32):
    """Custom type vrIpMcastCacheStatsOperationalState based on Integer32"""
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


_VrIpMcastCacheStatsOperationalState_Type.__name__ = "Integer32"
_VrIpMcastCacheStatsOperationalState_Object = MibTableColumn
vrIpMcastCacheStatsOperationalState = _VrIpMcastCacheStatsOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 8, 10, 1, 2),
    _VrIpMcastCacheStatsOperationalState_Type()
)
vrIpMcastCacheStatsOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastCacheStatsOperationalState.setStatus("mandatory")


class _VrIpMcastCacheStatsUsageState_Type(Integer32):
    """Custom type vrIpMcastCacheStatsUsageState based on Integer32"""
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


_VrIpMcastCacheStatsUsageState_Type.__name__ = "Integer32"
_VrIpMcastCacheStatsUsageState_Object = MibTableColumn
vrIpMcastCacheStatsUsageState = _VrIpMcastCacheStatsUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 8, 10, 1, 3),
    _VrIpMcastCacheStatsUsageState_Type()
)
vrIpMcastCacheStatsUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastCacheStatsUsageState.setStatus("mandatory")
_VrIpMcastCacheStatsOperTable_Object = MibTable
vrIpMcastCacheStatsOperTable = _VrIpMcastCacheStatsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 8, 11)
)
if mibBuilder.loadTexts:
    vrIpMcastCacheStatsOperTable.setStatus("mandatory")
_VrIpMcastCacheStatsOperEntry_Object = MibTableRow
vrIpMcastCacheStatsOperEntry = _VrIpMcastCacheStatsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 8, 11, 1)
)
vrIpMcastCacheStatsOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastCacheStatsIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastCacheStatsOperEntry.setStatus("mandatory")


class _VrIpMcastCacheStatsEntriesFree_Type(Unsigned32):
    """Custom type vrIpMcastCacheStatsEntriesFree based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_VrIpMcastCacheStatsEntriesFree_Type.__name__ = "Unsigned32"
_VrIpMcastCacheStatsEntriesFree_Object = MibTableColumn
vrIpMcastCacheStatsEntriesFree = _VrIpMcastCacheStatsEntriesFree_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 8, 11, 1, 3),
    _VrIpMcastCacheStatsEntriesFree_Type()
)
vrIpMcastCacheStatsEntriesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastCacheStatsEntriesFree.setStatus("mandatory")


class _VrIpMcastCacheStatsTotalLookups_Type(Unsigned32):
    """Custom type vrIpMcastCacheStatsTotalLookups based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpMcastCacheStatsTotalLookups_Type.__name__ = "Unsigned32"
_VrIpMcastCacheStatsTotalLookups_Object = MibTableColumn
vrIpMcastCacheStatsTotalLookups = _VrIpMcastCacheStatsTotalLookups_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 8, 11, 1, 4),
    _VrIpMcastCacheStatsTotalLookups_Type()
)
vrIpMcastCacheStatsTotalLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastCacheStatsTotalLookups.setStatus("mandatory")
_VrIpMcastCacheStatsLookupMisses_Type = Counter32
_VrIpMcastCacheStatsLookupMisses_Object = MibTableColumn
vrIpMcastCacheStatsLookupMisses = _VrIpMcastCacheStatsLookupMisses_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 8, 11, 1, 5),
    _VrIpMcastCacheStatsLookupMisses_Type()
)
vrIpMcastCacheStatsLookupMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastCacheStatsLookupMisses.setStatus("mandatory")


class _VrIpMcastCacheStatsCacheTableMaxEntries_Type(Unsigned32):
    """Custom type vrIpMcastCacheStatsCacheTableMaxEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_VrIpMcastCacheStatsCacheTableMaxEntries_Type.__name__ = "Unsigned32"
_VrIpMcastCacheStatsCacheTableMaxEntries_Object = MibTableColumn
vrIpMcastCacheStatsCacheTableMaxEntries = _VrIpMcastCacheStatsCacheTableMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 8, 11, 1, 395),
    _VrIpMcastCacheStatsCacheTableMaxEntries_Type()
)
vrIpMcastCacheStatsCacheTableMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastCacheStatsCacheTableMaxEntries.setStatus("mandatory")
_VrIpMcastPimSm_ObjectIdentity = ObjectIdentity
vrIpMcastPimSm = _VrIpMcastPimSm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9)
)
_VrIpMcastPimSmRowStatusTable_Object = MibTable
vrIpMcastPimSmRowStatusTable = _VrIpMcastPimSmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 1)
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmRowStatusTable.setStatus("mandatory")
_VrIpMcastPimSmRowStatusEntry_Object = MibTableRow
vrIpMcastPimSmRowStatusEntry = _VrIpMcastPimSmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 1, 1)
)
vrIpMcastPimSmRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmRowStatusEntry.setStatus("mandatory")
_VrIpMcastPimSmRowStatus_Type = RowStatus
_VrIpMcastPimSmRowStatus_Object = MibTableColumn
vrIpMcastPimSmRowStatus = _VrIpMcastPimSmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 1, 1, 1),
    _VrIpMcastPimSmRowStatus_Type()
)
vrIpMcastPimSmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpMcastPimSmRowStatus.setStatus("mandatory")
_VrIpMcastPimSmComponentName_Type = DisplayString
_VrIpMcastPimSmComponentName_Object = MibTableColumn
vrIpMcastPimSmComponentName = _VrIpMcastPimSmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 1, 1, 2),
    _VrIpMcastPimSmComponentName_Type()
)
vrIpMcastPimSmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmComponentName.setStatus("mandatory")
_VrIpMcastPimSmStorageType_Type = StorageType
_VrIpMcastPimSmStorageType_Object = MibTableColumn
vrIpMcastPimSmStorageType = _VrIpMcastPimSmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 1, 1, 4),
    _VrIpMcastPimSmStorageType_Type()
)
vrIpMcastPimSmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmStorageType.setStatus("mandatory")
_VrIpMcastPimSmIndex_Type = NonReplicated
_VrIpMcastPimSmIndex_Object = MibTableColumn
vrIpMcastPimSmIndex = _VrIpMcastPimSmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 1, 1, 10),
    _VrIpMcastPimSmIndex_Type()
)
vrIpMcastPimSmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastPimSmIndex.setStatus("mandatory")
_VrIpMcastPimSmDomain_ObjectIdentity = ObjectIdentity
vrIpMcastPimSmDomain = _VrIpMcastPimSmDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2)
)
_VrIpMcastPimSmDomainRowStatusTable_Object = MibTable
vrIpMcastPimSmDomainRowStatusTable = _VrIpMcastPimSmDomainRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainRowStatusTable.setStatus("mandatory")
_VrIpMcastPimSmDomainRowStatusEntry_Object = MibTableRow
vrIpMcastPimSmDomainRowStatusEntry = _VrIpMcastPimSmDomainRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 1, 1)
)
vrIpMcastPimSmDomainRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmDomainIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainRowStatusEntry.setStatus("mandatory")
_VrIpMcastPimSmDomainRowStatus_Type = RowStatus
_VrIpMcastPimSmDomainRowStatus_Object = MibTableColumn
vrIpMcastPimSmDomainRowStatus = _VrIpMcastPimSmDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 1, 1, 1),
    _VrIpMcastPimSmDomainRowStatus_Type()
)
vrIpMcastPimSmDomainRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainRowStatus.setStatus("mandatory")
_VrIpMcastPimSmDomainComponentName_Type = DisplayString
_VrIpMcastPimSmDomainComponentName_Object = MibTableColumn
vrIpMcastPimSmDomainComponentName = _VrIpMcastPimSmDomainComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 1, 1, 2),
    _VrIpMcastPimSmDomainComponentName_Type()
)
vrIpMcastPimSmDomainComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainComponentName.setStatus("mandatory")
_VrIpMcastPimSmDomainStorageType_Type = StorageType
_VrIpMcastPimSmDomainStorageType_Object = MibTableColumn
vrIpMcastPimSmDomainStorageType = _VrIpMcastPimSmDomainStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 1, 1, 4),
    _VrIpMcastPimSmDomainStorageType_Type()
)
vrIpMcastPimSmDomainStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainStorageType.setStatus("mandatory")


class _VrIpMcastPimSmDomainIndex_Type(Integer32):
    """Custom type vrIpMcastPimSmDomainIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_VrIpMcastPimSmDomainIndex_Type.__name__ = "Integer32"
_VrIpMcastPimSmDomainIndex_Object = MibTableColumn
vrIpMcastPimSmDomainIndex = _VrIpMcastPimSmDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 1, 1, 10),
    _VrIpMcastPimSmDomainIndex_Type()
)
vrIpMcastPimSmDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainIndex.setStatus("mandatory")
_VrIpMcastPimSmDomainCRp_ObjectIdentity = ObjectIdentity
vrIpMcastPimSmDomainCRp = _VrIpMcastPimSmDomainCRp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 2)
)
_VrIpMcastPimSmDomainCRpRowStatusTable_Object = MibTable
vrIpMcastPimSmDomainCRpRowStatusTable = _VrIpMcastPimSmDomainCRpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCRpRowStatusTable.setStatus("mandatory")
_VrIpMcastPimSmDomainCRpRowStatusEntry_Object = MibTableRow
vrIpMcastPimSmDomainCRpRowStatusEntry = _VrIpMcastPimSmDomainCRpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 2, 1, 1)
)
vrIpMcastPimSmDomainCRpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmDomainIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmDomainCRpIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCRpRowStatusEntry.setStatus("mandatory")
_VrIpMcastPimSmDomainCRpRowStatus_Type = RowStatus
_VrIpMcastPimSmDomainCRpRowStatus_Object = MibTableColumn
vrIpMcastPimSmDomainCRpRowStatus = _VrIpMcastPimSmDomainCRpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 2, 1, 1, 1),
    _VrIpMcastPimSmDomainCRpRowStatus_Type()
)
vrIpMcastPimSmDomainCRpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCRpRowStatus.setStatus("mandatory")
_VrIpMcastPimSmDomainCRpComponentName_Type = DisplayString
_VrIpMcastPimSmDomainCRpComponentName_Object = MibTableColumn
vrIpMcastPimSmDomainCRpComponentName = _VrIpMcastPimSmDomainCRpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 2, 1, 1, 2),
    _VrIpMcastPimSmDomainCRpComponentName_Type()
)
vrIpMcastPimSmDomainCRpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCRpComponentName.setStatus("mandatory")
_VrIpMcastPimSmDomainCRpStorageType_Type = StorageType
_VrIpMcastPimSmDomainCRpStorageType_Object = MibTableColumn
vrIpMcastPimSmDomainCRpStorageType = _VrIpMcastPimSmDomainCRpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 2, 1, 1, 4),
    _VrIpMcastPimSmDomainCRpStorageType_Type()
)
vrIpMcastPimSmDomainCRpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCRpStorageType.setStatus("mandatory")
_VrIpMcastPimSmDomainCRpIndex_Type = NonReplicated
_VrIpMcastPimSmDomainCRpIndex_Object = MibTableColumn
vrIpMcastPimSmDomainCRpIndex = _VrIpMcastPimSmDomainCRpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 2, 1, 1, 10),
    _VrIpMcastPimSmDomainCRpIndex_Type()
)
vrIpMcastPimSmDomainCRpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCRpIndex.setStatus("mandatory")
_VrIpMcastPimSmDomainCRpGrp_ObjectIdentity = ObjectIdentity
vrIpMcastPimSmDomainCRpGrp = _VrIpMcastPimSmDomainCRpGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 2, 2)
)
_VrIpMcastPimSmDomainCRpGrpRowStatusTable_Object = MibTable
vrIpMcastPimSmDomainCRpGrpRowStatusTable = _VrIpMcastPimSmDomainCRpGrpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCRpGrpRowStatusTable.setStatus("mandatory")
_VrIpMcastPimSmDomainCRpGrpRowStatusEntry_Object = MibTableRow
vrIpMcastPimSmDomainCRpGrpRowStatusEntry = _VrIpMcastPimSmDomainCRpGrpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 2, 2, 1, 1)
)
vrIpMcastPimSmDomainCRpGrpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmDomainIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmDomainCRpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmDomainCRpGrpGrpAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmDomainCRpGrpGrpMaskIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCRpGrpRowStatusEntry.setStatus("mandatory")
_VrIpMcastPimSmDomainCRpGrpRowStatus_Type = RowStatus
_VrIpMcastPimSmDomainCRpGrpRowStatus_Object = MibTableColumn
vrIpMcastPimSmDomainCRpGrpRowStatus = _VrIpMcastPimSmDomainCRpGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 2, 2, 1, 1, 1),
    _VrIpMcastPimSmDomainCRpGrpRowStatus_Type()
)
vrIpMcastPimSmDomainCRpGrpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCRpGrpRowStatus.setStatus("mandatory")
_VrIpMcastPimSmDomainCRpGrpComponentName_Type = DisplayString
_VrIpMcastPimSmDomainCRpGrpComponentName_Object = MibTableColumn
vrIpMcastPimSmDomainCRpGrpComponentName = _VrIpMcastPimSmDomainCRpGrpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 2, 2, 1, 1, 2),
    _VrIpMcastPimSmDomainCRpGrpComponentName_Type()
)
vrIpMcastPimSmDomainCRpGrpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCRpGrpComponentName.setStatus("mandatory")
_VrIpMcastPimSmDomainCRpGrpStorageType_Type = StorageType
_VrIpMcastPimSmDomainCRpGrpStorageType_Object = MibTableColumn
vrIpMcastPimSmDomainCRpGrpStorageType = _VrIpMcastPimSmDomainCRpGrpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 2, 2, 1, 1, 4),
    _VrIpMcastPimSmDomainCRpGrpStorageType_Type()
)
vrIpMcastPimSmDomainCRpGrpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCRpGrpStorageType.setStatus("mandatory")
_VrIpMcastPimSmDomainCRpGrpGrpAddressIndex_Type = IpAddress
_VrIpMcastPimSmDomainCRpGrpGrpAddressIndex_Object = MibTableColumn
vrIpMcastPimSmDomainCRpGrpGrpAddressIndex = _VrIpMcastPimSmDomainCRpGrpGrpAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 2, 2, 1, 1, 10),
    _VrIpMcastPimSmDomainCRpGrpGrpAddressIndex_Type()
)
vrIpMcastPimSmDomainCRpGrpGrpAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCRpGrpGrpAddressIndex.setStatus("mandatory")
_VrIpMcastPimSmDomainCRpGrpGrpMaskIndex_Type = IpAddress
_VrIpMcastPimSmDomainCRpGrpGrpMaskIndex_Object = MibTableColumn
vrIpMcastPimSmDomainCRpGrpGrpMaskIndex = _VrIpMcastPimSmDomainCRpGrpGrpMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 2, 2, 1, 1, 11),
    _VrIpMcastPimSmDomainCRpGrpGrpMaskIndex_Type()
)
vrIpMcastPimSmDomainCRpGrpGrpMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCRpGrpGrpMaskIndex.setStatus("mandatory")
_VrIpMcastPimSmDomainCRpProvTable_Object = MibTable
vrIpMcastPimSmDomainCRpProvTable = _VrIpMcastPimSmDomainCRpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCRpProvTable.setStatus("mandatory")
_VrIpMcastPimSmDomainCRpProvEntry_Object = MibTableRow
vrIpMcastPimSmDomainCRpProvEntry = _VrIpMcastPimSmDomainCRpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 2, 10, 1)
)
vrIpMcastPimSmDomainCRpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmDomainIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmDomainCRpIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCRpProvEntry.setStatus("mandatory")
_VrIpMcastPimSmDomainCRpCandidateRpAddress_Type = Link
_VrIpMcastPimSmDomainCRpCandidateRpAddress_Object = MibTableColumn
vrIpMcastPimSmDomainCRpCandidateRpAddress = _VrIpMcastPimSmDomainCRpCandidateRpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 2, 10, 1, 1),
    _VrIpMcastPimSmDomainCRpCandidateRpAddress_Type()
)
vrIpMcastPimSmDomainCRpCandidateRpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCRpCandidateRpAddress.setStatus("mandatory")


class _VrIpMcastPimSmDomainCRpCandidateRpPreference_Type(Integer32):
    """Custom type vrIpMcastPimSmDomainCRpCandidateRpPreference based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrIpMcastPimSmDomainCRpCandidateRpPreference_Type.__name__ = "Integer32"
_VrIpMcastPimSmDomainCRpCandidateRpPreference_Object = MibTableColumn
vrIpMcastPimSmDomainCRpCandidateRpPreference = _VrIpMcastPimSmDomainCRpCandidateRpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 2, 10, 1, 2),
    _VrIpMcastPimSmDomainCRpCandidateRpPreference_Type()
)
vrIpMcastPimSmDomainCRpCandidateRpPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCRpCandidateRpPreference.setStatus("mandatory")
_VrIpMcastPimSmDomainRpSet_ObjectIdentity = ObjectIdentity
vrIpMcastPimSmDomainRpSet = _VrIpMcastPimSmDomainRpSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 3)
)
_VrIpMcastPimSmDomainRpSetRowStatusTable_Object = MibTable
vrIpMcastPimSmDomainRpSetRowStatusTable = _VrIpMcastPimSmDomainRpSetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 3, 1)
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainRpSetRowStatusTable.setStatus("mandatory")
_VrIpMcastPimSmDomainRpSetRowStatusEntry_Object = MibTableRow
vrIpMcastPimSmDomainRpSetRowStatusEntry = _VrIpMcastPimSmDomainRpSetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 3, 1, 1)
)
vrIpMcastPimSmDomainRpSetRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmDomainIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmDomainRpSetGrpAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmDomainRpSetGrpMaskIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmDomainRpSetRpAddressIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainRpSetRowStatusEntry.setStatus("mandatory")
_VrIpMcastPimSmDomainRpSetRowStatus_Type = RowStatus
_VrIpMcastPimSmDomainRpSetRowStatus_Object = MibTableColumn
vrIpMcastPimSmDomainRpSetRowStatus = _VrIpMcastPimSmDomainRpSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 3, 1, 1, 1),
    _VrIpMcastPimSmDomainRpSetRowStatus_Type()
)
vrIpMcastPimSmDomainRpSetRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainRpSetRowStatus.setStatus("mandatory")
_VrIpMcastPimSmDomainRpSetComponentName_Type = DisplayString
_VrIpMcastPimSmDomainRpSetComponentName_Object = MibTableColumn
vrIpMcastPimSmDomainRpSetComponentName = _VrIpMcastPimSmDomainRpSetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 3, 1, 1, 2),
    _VrIpMcastPimSmDomainRpSetComponentName_Type()
)
vrIpMcastPimSmDomainRpSetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainRpSetComponentName.setStatus("mandatory")
_VrIpMcastPimSmDomainRpSetStorageType_Type = StorageType
_VrIpMcastPimSmDomainRpSetStorageType_Object = MibTableColumn
vrIpMcastPimSmDomainRpSetStorageType = _VrIpMcastPimSmDomainRpSetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 3, 1, 1, 4),
    _VrIpMcastPimSmDomainRpSetStorageType_Type()
)
vrIpMcastPimSmDomainRpSetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainRpSetStorageType.setStatus("mandatory")
_VrIpMcastPimSmDomainRpSetGrpAddressIndex_Type = IpAddress
_VrIpMcastPimSmDomainRpSetGrpAddressIndex_Object = MibTableColumn
vrIpMcastPimSmDomainRpSetGrpAddressIndex = _VrIpMcastPimSmDomainRpSetGrpAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 3, 1, 1, 10),
    _VrIpMcastPimSmDomainRpSetGrpAddressIndex_Type()
)
vrIpMcastPimSmDomainRpSetGrpAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainRpSetGrpAddressIndex.setStatus("mandatory")
_VrIpMcastPimSmDomainRpSetGrpMaskIndex_Type = IpAddress
_VrIpMcastPimSmDomainRpSetGrpMaskIndex_Object = MibTableColumn
vrIpMcastPimSmDomainRpSetGrpMaskIndex = _VrIpMcastPimSmDomainRpSetGrpMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 3, 1, 1, 11),
    _VrIpMcastPimSmDomainRpSetGrpMaskIndex_Type()
)
vrIpMcastPimSmDomainRpSetGrpMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainRpSetGrpMaskIndex.setStatus("mandatory")
_VrIpMcastPimSmDomainRpSetRpAddressIndex_Type = IpAddress
_VrIpMcastPimSmDomainRpSetRpAddressIndex_Object = MibTableColumn
vrIpMcastPimSmDomainRpSetRpAddressIndex = _VrIpMcastPimSmDomainRpSetRpAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 3, 1, 1, 12),
    _VrIpMcastPimSmDomainRpSetRpAddressIndex_Type()
)
vrIpMcastPimSmDomainRpSetRpAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainRpSetRpAddressIndex.setStatus("mandatory")
_VrIpMcastPimSmDomainRpSetOperTable_Object = MibTable
vrIpMcastPimSmDomainRpSetOperTable = _VrIpMcastPimSmDomainRpSetOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 3, 11)
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainRpSetOperTable.setStatus("mandatory")
_VrIpMcastPimSmDomainRpSetOperEntry_Object = MibTableRow
vrIpMcastPimSmDomainRpSetOperEntry = _VrIpMcastPimSmDomainRpSetOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 3, 11, 1)
)
vrIpMcastPimSmDomainRpSetOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmDomainIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmDomainRpSetGrpAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmDomainRpSetGrpMaskIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmDomainRpSetRpAddressIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainRpSetOperEntry.setStatus("mandatory")


class _VrIpMcastPimSmDomainRpSetRpSetHoldTime_Type(Unsigned32):
    """Custom type vrIpMcastPimSmDomainRpSetRpSetHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrIpMcastPimSmDomainRpSetRpSetHoldTime_Type.__name__ = "Unsigned32"
_VrIpMcastPimSmDomainRpSetRpSetHoldTime_Object = MibTableColumn
vrIpMcastPimSmDomainRpSetRpSetHoldTime = _VrIpMcastPimSmDomainRpSetRpSetHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 3, 11, 1, 1),
    _VrIpMcastPimSmDomainRpSetRpSetHoldTime_Type()
)
vrIpMcastPimSmDomainRpSetRpSetHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainRpSetRpSetHoldTime.setStatus("mandatory")
_VrIpMcastPimSmDomainRpSetRpSetExpiryTime_Type = TimeTicks
_VrIpMcastPimSmDomainRpSetRpSetExpiryTime_Object = MibTableColumn
vrIpMcastPimSmDomainRpSetRpSetExpiryTime = _VrIpMcastPimSmDomainRpSetRpSetExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 3, 11, 1, 2),
    _VrIpMcastPimSmDomainRpSetRpSetExpiryTime_Type()
)
vrIpMcastPimSmDomainRpSetRpSetExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainRpSetRpSetExpiryTime.setStatus("mandatory")


class _VrIpMcastPimSmDomainRpSetRpSetPriority_Type(Integer32):
    """Custom type vrIpMcastPimSmDomainRpSetRpSetPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrIpMcastPimSmDomainRpSetRpSetPriority_Type.__name__ = "Integer32"
_VrIpMcastPimSmDomainRpSetRpSetPriority_Object = MibTableColumn
vrIpMcastPimSmDomainRpSetRpSetPriority = _VrIpMcastPimSmDomainRpSetRpSetPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 3, 11, 1, 3),
    _VrIpMcastPimSmDomainRpSetRpSetPriority_Type()
)
vrIpMcastPimSmDomainRpSetRpSetPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainRpSetRpSetPriority.setStatus("mandatory")
_VrIpMcastPimSmDomainCBsr_ObjectIdentity = ObjectIdentity
vrIpMcastPimSmDomainCBsr = _VrIpMcastPimSmDomainCBsr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 4)
)
_VrIpMcastPimSmDomainCBsrRowStatusTable_Object = MibTable
vrIpMcastPimSmDomainCBsrRowStatusTable = _VrIpMcastPimSmDomainCBsrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 4, 1)
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCBsrRowStatusTable.setStatus("mandatory")
_VrIpMcastPimSmDomainCBsrRowStatusEntry_Object = MibTableRow
vrIpMcastPimSmDomainCBsrRowStatusEntry = _VrIpMcastPimSmDomainCBsrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 4, 1, 1)
)
vrIpMcastPimSmDomainCBsrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmDomainIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmDomainCBsrIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCBsrRowStatusEntry.setStatus("mandatory")
_VrIpMcastPimSmDomainCBsrRowStatus_Type = RowStatus
_VrIpMcastPimSmDomainCBsrRowStatus_Object = MibTableColumn
vrIpMcastPimSmDomainCBsrRowStatus = _VrIpMcastPimSmDomainCBsrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 4, 1, 1, 1),
    _VrIpMcastPimSmDomainCBsrRowStatus_Type()
)
vrIpMcastPimSmDomainCBsrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCBsrRowStatus.setStatus("mandatory")
_VrIpMcastPimSmDomainCBsrComponentName_Type = DisplayString
_VrIpMcastPimSmDomainCBsrComponentName_Object = MibTableColumn
vrIpMcastPimSmDomainCBsrComponentName = _VrIpMcastPimSmDomainCBsrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 4, 1, 1, 2),
    _VrIpMcastPimSmDomainCBsrComponentName_Type()
)
vrIpMcastPimSmDomainCBsrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCBsrComponentName.setStatus("mandatory")
_VrIpMcastPimSmDomainCBsrStorageType_Type = StorageType
_VrIpMcastPimSmDomainCBsrStorageType_Object = MibTableColumn
vrIpMcastPimSmDomainCBsrStorageType = _VrIpMcastPimSmDomainCBsrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 4, 1, 1, 4),
    _VrIpMcastPimSmDomainCBsrStorageType_Type()
)
vrIpMcastPimSmDomainCBsrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCBsrStorageType.setStatus("mandatory")
_VrIpMcastPimSmDomainCBsrIndex_Type = NonReplicated
_VrIpMcastPimSmDomainCBsrIndex_Object = MibTableColumn
vrIpMcastPimSmDomainCBsrIndex = _VrIpMcastPimSmDomainCBsrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 4, 1, 1, 10),
    _VrIpMcastPimSmDomainCBsrIndex_Type()
)
vrIpMcastPimSmDomainCBsrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCBsrIndex.setStatus("mandatory")
_VrIpMcastPimSmDomainCBsrProvTable_Object = MibTable
vrIpMcastPimSmDomainCBsrProvTable = _VrIpMcastPimSmDomainCBsrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 4, 10)
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCBsrProvTable.setStatus("mandatory")
_VrIpMcastPimSmDomainCBsrProvEntry_Object = MibTableRow
vrIpMcastPimSmDomainCBsrProvEntry = _VrIpMcastPimSmDomainCBsrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 4, 10, 1)
)
vrIpMcastPimSmDomainCBsrProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmDomainIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmDomainCBsrIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCBsrProvEntry.setStatus("mandatory")
_VrIpMcastPimSmDomainCBsrCandidateBsrAddress_Type = Link
_VrIpMcastPimSmDomainCBsrCandidateBsrAddress_Object = MibTableColumn
vrIpMcastPimSmDomainCBsrCandidateBsrAddress = _VrIpMcastPimSmDomainCBsrCandidateBsrAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 4, 10, 1, 1),
    _VrIpMcastPimSmDomainCBsrCandidateBsrAddress_Type()
)
vrIpMcastPimSmDomainCBsrCandidateBsrAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCBsrCandidateBsrAddress.setStatus("mandatory")


class _VrIpMcastPimSmDomainCBsrCandidateBsrPreference_Type(Integer32):
    """Custom type vrIpMcastPimSmDomainCBsrCandidateBsrPreference based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrIpMcastPimSmDomainCBsrCandidateBsrPreference_Type.__name__ = "Integer32"
_VrIpMcastPimSmDomainCBsrCandidateBsrPreference_Object = MibTableColumn
vrIpMcastPimSmDomainCBsrCandidateBsrPreference = _VrIpMcastPimSmDomainCBsrCandidateBsrPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 4, 10, 1, 2),
    _VrIpMcastPimSmDomainCBsrCandidateBsrPreference_Type()
)
vrIpMcastPimSmDomainCBsrCandidateBsrPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainCBsrCandidateBsrPreference.setStatus("mandatory")
_VrIpMcastPimSmDomainProvTable_Object = MibTable
vrIpMcastPimSmDomainProvTable = _VrIpMcastPimSmDomainProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainProvTable.setStatus("mandatory")
_VrIpMcastPimSmDomainProvEntry_Object = MibTableRow
vrIpMcastPimSmDomainProvEntry = _VrIpMcastPimSmDomainProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 10, 1)
)
vrIpMcastPimSmDomainProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmDomainIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainProvEntry.setStatus("mandatory")


class _VrIpMcastPimSmDomainJoinPruneInterval_Type(Unsigned32):
    """Custom type vrIpMcastPimSmDomainJoinPruneInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 4292967295),
    )


_VrIpMcastPimSmDomainJoinPruneInterval_Type.__name__ = "Unsigned32"
_VrIpMcastPimSmDomainJoinPruneInterval_Object = MibTableColumn
vrIpMcastPimSmDomainJoinPruneInterval = _VrIpMcastPimSmDomainJoinPruneInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 10, 1, 1),
    _VrIpMcastPimSmDomainJoinPruneInterval_Type()
)
vrIpMcastPimSmDomainJoinPruneInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainJoinPruneInterval.setStatus("mandatory")


class _VrIpMcastPimSmDomainSptJoinThreshold_Type(Unsigned32):
    """Custom type vrIpMcastPimSmDomainSptJoinThreshold based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_VrIpMcastPimSmDomainSptJoinThreshold_Type.__name__ = "Unsigned32"
_VrIpMcastPimSmDomainSptJoinThreshold_Object = MibTableColumn
vrIpMcastPimSmDomainSptJoinThreshold = _VrIpMcastPimSmDomainSptJoinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 10, 1, 2),
    _VrIpMcastPimSmDomainSptJoinThreshold_Type()
)
vrIpMcastPimSmDomainSptJoinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainSptJoinThreshold.setStatus("mandatory")
_VrIpMcastPimSmDomainOperTable_Object = MibTable
vrIpMcastPimSmDomainOperTable = _VrIpMcastPimSmDomainOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 11)
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainOperTable.setStatus("mandatory")
_VrIpMcastPimSmDomainOperEntry_Object = MibTableRow
vrIpMcastPimSmDomainOperEntry = _VrIpMcastPimSmDomainOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 11, 1)
)
vrIpMcastPimSmDomainOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmDomainIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainOperEntry.setStatus("mandatory")
_VrIpMcastPimSmDomainBsrAddress_Type = IpAddress
_VrIpMcastPimSmDomainBsrAddress_Object = MibTableColumn
vrIpMcastPimSmDomainBsrAddress = _VrIpMcastPimSmDomainBsrAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 11, 1, 1),
    _VrIpMcastPimSmDomainBsrAddress_Type()
)
vrIpMcastPimSmDomainBsrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainBsrAddress.setStatus("mandatory")
_VrIpMcastPimSmDomainBsrExpiryTimer_Type = TimeTicks
_VrIpMcastPimSmDomainBsrExpiryTimer_Object = MibTableColumn
vrIpMcastPimSmDomainBsrExpiryTimer = _VrIpMcastPimSmDomainBsrExpiryTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 11, 1, 2),
    _VrIpMcastPimSmDomainBsrExpiryTimer_Type()
)
vrIpMcastPimSmDomainBsrExpiryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainBsrExpiryTimer.setStatus("mandatory")
_VrIpMcastPimSmDomainStatsTable_Object = MibTable
vrIpMcastPimSmDomainStatsTable = _VrIpMcastPimSmDomainStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 12)
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainStatsTable.setStatus("mandatory")
_VrIpMcastPimSmDomainStatsEntry_Object = MibTableRow
vrIpMcastPimSmDomainStatsEntry = _VrIpMcastPimSmDomainStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 12, 1)
)
vrIpMcastPimSmDomainStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmDomainIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainStatsEntry.setStatus("mandatory")
_VrIpMcastPimSmDomainTxBsrMsg_Type = Counter32
_VrIpMcastPimSmDomainTxBsrMsg_Object = MibTableColumn
vrIpMcastPimSmDomainTxBsrMsg = _VrIpMcastPimSmDomainTxBsrMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 12, 1, 1),
    _VrIpMcastPimSmDomainTxBsrMsg_Type()
)
vrIpMcastPimSmDomainTxBsrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainTxBsrMsg.setStatus("mandatory")
_VrIpMcastPimSmDomainRxBsrMsg_Type = Counter32
_VrIpMcastPimSmDomainRxBsrMsg_Object = MibTableColumn
vrIpMcastPimSmDomainRxBsrMsg = _VrIpMcastPimSmDomainRxBsrMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 12, 1, 2),
    _VrIpMcastPimSmDomainRxBsrMsg_Type()
)
vrIpMcastPimSmDomainRxBsrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainRxBsrMsg.setStatus("mandatory")
_VrIpMcastPimSmDomainTxCRpAdvMsg_Type = Counter32
_VrIpMcastPimSmDomainTxCRpAdvMsg_Object = MibTableColumn
vrIpMcastPimSmDomainTxCRpAdvMsg = _VrIpMcastPimSmDomainTxCRpAdvMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 12, 1, 3),
    _VrIpMcastPimSmDomainTxCRpAdvMsg_Type()
)
vrIpMcastPimSmDomainTxCRpAdvMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainTxCRpAdvMsg.setStatus("mandatory")
_VrIpMcastPimSmDomainRxCRpAdvMsg_Type = Counter32
_VrIpMcastPimSmDomainRxCRpAdvMsg_Object = MibTableColumn
vrIpMcastPimSmDomainRxCRpAdvMsg = _VrIpMcastPimSmDomainRxCRpAdvMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 12, 1, 4),
    _VrIpMcastPimSmDomainRxCRpAdvMsg_Type()
)
vrIpMcastPimSmDomainRxCRpAdvMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainRxCRpAdvMsg.setStatus("mandatory")
_VrIpMcastPimSmDomainTxHelloMsg_Type = Counter32
_VrIpMcastPimSmDomainTxHelloMsg_Object = MibTableColumn
vrIpMcastPimSmDomainTxHelloMsg = _VrIpMcastPimSmDomainTxHelloMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 12, 1, 5),
    _VrIpMcastPimSmDomainTxHelloMsg_Type()
)
vrIpMcastPimSmDomainTxHelloMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainTxHelloMsg.setStatus("mandatory")
_VrIpMcastPimSmDomainRxHelloMsg_Type = Counter32
_VrIpMcastPimSmDomainRxHelloMsg_Object = MibTableColumn
vrIpMcastPimSmDomainRxHelloMsg = _VrIpMcastPimSmDomainRxHelloMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 12, 1, 6),
    _VrIpMcastPimSmDomainRxHelloMsg_Type()
)
vrIpMcastPimSmDomainRxHelloMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainRxHelloMsg.setStatus("mandatory")
_VrIpMcastPimSmDomainTxRegisterMsg_Type = Counter32
_VrIpMcastPimSmDomainTxRegisterMsg_Object = MibTableColumn
vrIpMcastPimSmDomainTxRegisterMsg = _VrIpMcastPimSmDomainTxRegisterMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 12, 1, 7),
    _VrIpMcastPimSmDomainTxRegisterMsg_Type()
)
vrIpMcastPimSmDomainTxRegisterMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainTxRegisterMsg.setStatus("mandatory")
_VrIpMcastPimSmDomainRxRegisterMsg_Type = Counter32
_VrIpMcastPimSmDomainRxRegisterMsg_Object = MibTableColumn
vrIpMcastPimSmDomainRxRegisterMsg = _VrIpMcastPimSmDomainRxRegisterMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 12, 1, 8),
    _VrIpMcastPimSmDomainRxRegisterMsg_Type()
)
vrIpMcastPimSmDomainRxRegisterMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainRxRegisterMsg.setStatus("mandatory")
_VrIpMcastPimSmDomainTxRegisterStopMsg_Type = Counter32
_VrIpMcastPimSmDomainTxRegisterStopMsg_Object = MibTableColumn
vrIpMcastPimSmDomainTxRegisterStopMsg = _VrIpMcastPimSmDomainTxRegisterStopMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 12, 1, 9),
    _VrIpMcastPimSmDomainTxRegisterStopMsg_Type()
)
vrIpMcastPimSmDomainTxRegisterStopMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainTxRegisterStopMsg.setStatus("mandatory")
_VrIpMcastPimSmDomainRxRegisterStopMsg_Type = Counter32
_VrIpMcastPimSmDomainRxRegisterStopMsg_Object = MibTableColumn
vrIpMcastPimSmDomainRxRegisterStopMsg = _VrIpMcastPimSmDomainRxRegisterStopMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 12, 1, 10),
    _VrIpMcastPimSmDomainRxRegisterStopMsg_Type()
)
vrIpMcastPimSmDomainRxRegisterStopMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainRxRegisterStopMsg.setStatus("mandatory")
_VrIpMcastPimSmDomainTxAssertMsg_Type = Counter32
_VrIpMcastPimSmDomainTxAssertMsg_Object = MibTableColumn
vrIpMcastPimSmDomainTxAssertMsg = _VrIpMcastPimSmDomainTxAssertMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 12, 1, 11),
    _VrIpMcastPimSmDomainTxAssertMsg_Type()
)
vrIpMcastPimSmDomainTxAssertMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainTxAssertMsg.setStatus("mandatory")
_VrIpMcastPimSmDomainRxAssertMsg_Type = Counter32
_VrIpMcastPimSmDomainRxAssertMsg_Object = MibTableColumn
vrIpMcastPimSmDomainRxAssertMsg = _VrIpMcastPimSmDomainRxAssertMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 12, 1, 12),
    _VrIpMcastPimSmDomainRxAssertMsg_Type()
)
vrIpMcastPimSmDomainRxAssertMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainRxAssertMsg.setStatus("mandatory")
_VrIpMcastPimSmDomainTxJPMsg_Type = Counter32
_VrIpMcastPimSmDomainTxJPMsg_Object = MibTableColumn
vrIpMcastPimSmDomainTxJPMsg = _VrIpMcastPimSmDomainTxJPMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 12, 1, 13),
    _VrIpMcastPimSmDomainTxJPMsg_Type()
)
vrIpMcastPimSmDomainTxJPMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainTxJPMsg.setStatus("mandatory")
_VrIpMcastPimSmDomainRxJPMsg_Type = Counter32
_VrIpMcastPimSmDomainRxJPMsg_Object = MibTableColumn
vrIpMcastPimSmDomainRxJPMsg = _VrIpMcastPimSmDomainRxJPMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 12, 1, 14),
    _VrIpMcastPimSmDomainRxJPMsg_Type()
)
vrIpMcastPimSmDomainRxJPMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainRxJPMsg.setStatus("mandatory")
_VrIpMcastPimSmDomainDiscardBsrMsg_Type = Counter32
_VrIpMcastPimSmDomainDiscardBsrMsg_Object = MibTableColumn
vrIpMcastPimSmDomainDiscardBsrMsg = _VrIpMcastPimSmDomainDiscardBsrMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 12, 1, 17),
    _VrIpMcastPimSmDomainDiscardBsrMsg_Type()
)
vrIpMcastPimSmDomainDiscardBsrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainDiscardBsrMsg.setStatus("mandatory")
_VrIpMcastPimSmDomainDiscardCRpAdvMsg_Type = Counter32
_VrIpMcastPimSmDomainDiscardCRpAdvMsg_Object = MibTableColumn
vrIpMcastPimSmDomainDiscardCRpAdvMsg = _VrIpMcastPimSmDomainDiscardCRpAdvMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 12, 1, 18),
    _VrIpMcastPimSmDomainDiscardCRpAdvMsg_Type()
)
vrIpMcastPimSmDomainDiscardCRpAdvMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainDiscardCRpAdvMsg.setStatus("mandatory")
_VrIpMcastPimSmDomainDiscardHelloMsg_Type = Counter32
_VrIpMcastPimSmDomainDiscardHelloMsg_Object = MibTableColumn
vrIpMcastPimSmDomainDiscardHelloMsg = _VrIpMcastPimSmDomainDiscardHelloMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 12, 1, 19),
    _VrIpMcastPimSmDomainDiscardHelloMsg_Type()
)
vrIpMcastPimSmDomainDiscardHelloMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainDiscardHelloMsg.setStatus("mandatory")
_VrIpMcastPimSmDomainDiscardRegisterMsg_Type = Counter32
_VrIpMcastPimSmDomainDiscardRegisterMsg_Object = MibTableColumn
vrIpMcastPimSmDomainDiscardRegisterMsg = _VrIpMcastPimSmDomainDiscardRegisterMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 12, 1, 20),
    _VrIpMcastPimSmDomainDiscardRegisterMsg_Type()
)
vrIpMcastPimSmDomainDiscardRegisterMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainDiscardRegisterMsg.setStatus("mandatory")
_VrIpMcastPimSmDomainDiscardRegisterStopMsg_Type = Counter32
_VrIpMcastPimSmDomainDiscardRegisterStopMsg_Object = MibTableColumn
vrIpMcastPimSmDomainDiscardRegisterStopMsg = _VrIpMcastPimSmDomainDiscardRegisterStopMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 12, 1, 21),
    _VrIpMcastPimSmDomainDiscardRegisterStopMsg_Type()
)
vrIpMcastPimSmDomainDiscardRegisterStopMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainDiscardRegisterStopMsg.setStatus("mandatory")
_VrIpMcastPimSmDomainDiscardAssertMsg_Type = Counter32
_VrIpMcastPimSmDomainDiscardAssertMsg_Object = MibTableColumn
vrIpMcastPimSmDomainDiscardAssertMsg = _VrIpMcastPimSmDomainDiscardAssertMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 12, 1, 22),
    _VrIpMcastPimSmDomainDiscardAssertMsg_Type()
)
vrIpMcastPimSmDomainDiscardAssertMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainDiscardAssertMsg.setStatus("mandatory")
_VrIpMcastPimSmDomainDiscardJPMsg_Type = Counter32
_VrIpMcastPimSmDomainDiscardJPMsg_Object = MibTableColumn
vrIpMcastPimSmDomainDiscardJPMsg = _VrIpMcastPimSmDomainDiscardJPMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 2, 12, 1, 23),
    _VrIpMcastPimSmDomainDiscardJPMsg_Type()
)
vrIpMcastPimSmDomainDiscardJPMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmDomainDiscardJPMsg.setStatus("mandatory")
_VrIpMcastPimSmAdminControlTable_Object = MibTable
vrIpMcastPimSmAdminControlTable = _VrIpMcastPimSmAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 10)
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmAdminControlTable.setStatus("mandatory")
_VrIpMcastPimSmAdminControlEntry_Object = MibTableRow
vrIpMcastPimSmAdminControlEntry = _VrIpMcastPimSmAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 10, 1)
)
vrIpMcastPimSmAdminControlEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmAdminControlEntry.setStatus("mandatory")


class _VrIpMcastPimSmSnmpAdminStatus_Type(Integer32):
    """Custom type vrIpMcastPimSmSnmpAdminStatus based on Integer32"""
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


_VrIpMcastPimSmSnmpAdminStatus_Type.__name__ = "Integer32"
_VrIpMcastPimSmSnmpAdminStatus_Object = MibTableColumn
vrIpMcastPimSmSnmpAdminStatus = _VrIpMcastPimSmSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 10, 1, 1),
    _VrIpMcastPimSmSnmpAdminStatus_Type()
)
vrIpMcastPimSmSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpMcastPimSmSnmpAdminStatus.setStatus("mandatory")
_VrIpMcastPimSmStateTable_Object = MibTable
vrIpMcastPimSmStateTable = _VrIpMcastPimSmStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 13)
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmStateTable.setStatus("mandatory")
_VrIpMcastPimSmStateEntry_Object = MibTableRow
vrIpMcastPimSmStateEntry = _VrIpMcastPimSmStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 13, 1)
)
vrIpMcastPimSmStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmStateEntry.setStatus("mandatory")


class _VrIpMcastPimSmAdminState_Type(Integer32):
    """Custom type vrIpMcastPimSmAdminState based on Integer32"""
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


_VrIpMcastPimSmAdminState_Type.__name__ = "Integer32"
_VrIpMcastPimSmAdminState_Object = MibTableColumn
vrIpMcastPimSmAdminState = _VrIpMcastPimSmAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 13, 1, 1),
    _VrIpMcastPimSmAdminState_Type()
)
vrIpMcastPimSmAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmAdminState.setStatus("mandatory")


class _VrIpMcastPimSmOperationalState_Type(Integer32):
    """Custom type vrIpMcastPimSmOperationalState based on Integer32"""
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


_VrIpMcastPimSmOperationalState_Type.__name__ = "Integer32"
_VrIpMcastPimSmOperationalState_Object = MibTableColumn
vrIpMcastPimSmOperationalState = _VrIpMcastPimSmOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 13, 1, 2),
    _VrIpMcastPimSmOperationalState_Type()
)
vrIpMcastPimSmOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmOperationalState.setStatus("mandatory")


class _VrIpMcastPimSmUsageState_Type(Integer32):
    """Custom type vrIpMcastPimSmUsageState based on Integer32"""
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


_VrIpMcastPimSmUsageState_Type.__name__ = "Integer32"
_VrIpMcastPimSmUsageState_Object = MibTableColumn
vrIpMcastPimSmUsageState = _VrIpMcastPimSmUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 13, 1, 3),
    _VrIpMcastPimSmUsageState_Type()
)
vrIpMcastPimSmUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmUsageState.setStatus("mandatory")
_VrIpMcastPimSmOperStatusTable_Object = MibTable
vrIpMcastPimSmOperStatusTable = _VrIpMcastPimSmOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 14)
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmOperStatusTable.setStatus("mandatory")
_VrIpMcastPimSmOperStatusEntry_Object = MibTableRow
vrIpMcastPimSmOperStatusEntry = _VrIpMcastPimSmOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 14, 1)
)
vrIpMcastPimSmOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimSmIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastPimSmOperStatusEntry.setStatus("mandatory")


class _VrIpMcastPimSmSnmpOperStatus_Type(Integer32):
    """Custom type vrIpMcastPimSmSnmpOperStatus based on Integer32"""
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


_VrIpMcastPimSmSnmpOperStatus_Type.__name__ = "Integer32"
_VrIpMcastPimSmSnmpOperStatus_Object = MibTableColumn
vrIpMcastPimSmSnmpOperStatus = _VrIpMcastPimSmSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 9, 14, 1, 1),
    _VrIpMcastPimSmSnmpOperStatus_Type()
)
vrIpMcastPimSmSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimSmSnmpOperStatus.setStatus("mandatory")
_VrIpMcastPimNbr_ObjectIdentity = ObjectIdentity
vrIpMcastPimNbr = _VrIpMcastPimNbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 10)
)
_VrIpMcastPimNbrRowStatusTable_Object = MibTable
vrIpMcastPimNbrRowStatusTable = _VrIpMcastPimNbrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 10, 1)
)
if mibBuilder.loadTexts:
    vrIpMcastPimNbrRowStatusTable.setStatus("mandatory")
_VrIpMcastPimNbrRowStatusEntry_Object = MibTableRow
vrIpMcastPimNbrRowStatusEntry = _VrIpMcastPimNbrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 10, 1, 1)
)
vrIpMcastPimNbrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimNbrNbrAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimNbrDomainIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastPimNbrRowStatusEntry.setStatus("mandatory")
_VrIpMcastPimNbrRowStatus_Type = RowStatus
_VrIpMcastPimNbrRowStatus_Object = MibTableColumn
vrIpMcastPimNbrRowStatus = _VrIpMcastPimNbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 10, 1, 1, 1),
    _VrIpMcastPimNbrRowStatus_Type()
)
vrIpMcastPimNbrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimNbrRowStatus.setStatus("mandatory")
_VrIpMcastPimNbrComponentName_Type = DisplayString
_VrIpMcastPimNbrComponentName_Object = MibTableColumn
vrIpMcastPimNbrComponentName = _VrIpMcastPimNbrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 10, 1, 1, 2),
    _VrIpMcastPimNbrComponentName_Type()
)
vrIpMcastPimNbrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimNbrComponentName.setStatus("mandatory")
_VrIpMcastPimNbrStorageType_Type = StorageType
_VrIpMcastPimNbrStorageType_Object = MibTableColumn
vrIpMcastPimNbrStorageType = _VrIpMcastPimNbrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 10, 1, 1, 4),
    _VrIpMcastPimNbrStorageType_Type()
)
vrIpMcastPimNbrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimNbrStorageType.setStatus("mandatory")
_VrIpMcastPimNbrNbrAddressIndex_Type = IpAddress
_VrIpMcastPimNbrNbrAddressIndex_Object = MibTableColumn
vrIpMcastPimNbrNbrAddressIndex = _VrIpMcastPimNbrNbrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 10, 1, 1, 10),
    _VrIpMcastPimNbrNbrAddressIndex_Type()
)
vrIpMcastPimNbrNbrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastPimNbrNbrAddressIndex.setStatus("mandatory")


class _VrIpMcastPimNbrDomainIndex_Type(Integer32):
    """Custom type vrIpMcastPimNbrDomainIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_VrIpMcastPimNbrDomainIndex_Type.__name__ = "Integer32"
_VrIpMcastPimNbrDomainIndex_Object = MibTableColumn
vrIpMcastPimNbrDomainIndex = _VrIpMcastPimNbrDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 10, 1, 1, 11),
    _VrIpMcastPimNbrDomainIndex_Type()
)
vrIpMcastPimNbrDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastPimNbrDomainIndex.setStatus("mandatory")
_VrIpMcastPimNbrOperTable_Object = MibTable
vrIpMcastPimNbrOperTable = _VrIpMcastPimNbrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 10, 10)
)
if mibBuilder.loadTexts:
    vrIpMcastPimNbrOperTable.setStatus("mandatory")
_VrIpMcastPimNbrOperEntry_Object = MibTableRow
vrIpMcastPimNbrOperEntry = _VrIpMcastPimNbrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 10, 10, 1)
)
vrIpMcastPimNbrOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimNbrNbrAddressIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastPimNbrDomainIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastPimNbrOperEntry.setStatus("mandatory")


class _VrIpMcastPimNbrIfIndex_Type(InterfaceIndex):
    """Custom type vrIpMcastPimNbrIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrIpMcastPimNbrIfIndex_Type.__name__ = "InterfaceIndex"
_VrIpMcastPimNbrIfIndex_Object = MibTableColumn
vrIpMcastPimNbrIfIndex = _VrIpMcastPimNbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 10, 10, 1, 1),
    _VrIpMcastPimNbrIfIndex_Type()
)
vrIpMcastPimNbrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimNbrIfIndex.setStatus("mandatory")
_VrIpMcastPimNbrUpTime_Type = TimeTicks
_VrIpMcastPimNbrUpTime_Object = MibTableColumn
vrIpMcastPimNbrUpTime = _VrIpMcastPimNbrUpTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 10, 10, 1, 2),
    _VrIpMcastPimNbrUpTime_Type()
)
vrIpMcastPimNbrUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimNbrUpTime.setStatus("mandatory")
_VrIpMcastPimNbrExpiryTimer_Type = TimeTicks
_VrIpMcastPimNbrExpiryTimer_Object = MibTableColumn
vrIpMcastPimNbrExpiryTimer = _VrIpMcastPimNbrExpiryTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 10, 10, 1, 3),
    _VrIpMcastPimNbrExpiryTimer_Type()
)
vrIpMcastPimNbrExpiryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastPimNbrExpiryTimer.setStatus("mandatory")
_VrIpMcastAdminControlTable_Object = MibTable
vrIpMcastAdminControlTable = _VrIpMcastAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 100)
)
if mibBuilder.loadTexts:
    vrIpMcastAdminControlTable.setStatus("mandatory")
_VrIpMcastAdminControlEntry_Object = MibTableRow
vrIpMcastAdminControlEntry = _VrIpMcastAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 100, 1)
)
vrIpMcastAdminControlEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastAdminControlEntry.setStatus("mandatory")


class _VrIpMcastSnmpAdminStatus_Type(Integer32):
    """Custom type vrIpMcastSnmpAdminStatus based on Integer32"""
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


_VrIpMcastSnmpAdminStatus_Type.__name__ = "Integer32"
_VrIpMcastSnmpAdminStatus_Object = MibTableColumn
vrIpMcastSnmpAdminStatus = _VrIpMcastSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 100, 1, 1),
    _VrIpMcastSnmpAdminStatus_Type()
)
vrIpMcastSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpMcastSnmpAdminStatus.setStatus("mandatory")
_VrIpMcastStateTable_Object = MibTable
vrIpMcastStateTable = _VrIpMcastStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 103)
)
if mibBuilder.loadTexts:
    vrIpMcastStateTable.setStatus("mandatory")
_VrIpMcastStateEntry_Object = MibTableRow
vrIpMcastStateEntry = _VrIpMcastStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 103, 1)
)
vrIpMcastStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastStateEntry.setStatus("mandatory")


class _VrIpMcastAdminState_Type(Integer32):
    """Custom type vrIpMcastAdminState based on Integer32"""
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


_VrIpMcastAdminState_Type.__name__ = "Integer32"
_VrIpMcastAdminState_Object = MibTableColumn
vrIpMcastAdminState = _VrIpMcastAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 103, 1, 1),
    _VrIpMcastAdminState_Type()
)
vrIpMcastAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastAdminState.setStatus("mandatory")


class _VrIpMcastOperationalState_Type(Integer32):
    """Custom type vrIpMcastOperationalState based on Integer32"""
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


_VrIpMcastOperationalState_Type.__name__ = "Integer32"
_VrIpMcastOperationalState_Object = MibTableColumn
vrIpMcastOperationalState = _VrIpMcastOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 103, 1, 2),
    _VrIpMcastOperationalState_Type()
)
vrIpMcastOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastOperationalState.setStatus("mandatory")


class _VrIpMcastUsageState_Type(Integer32):
    """Custom type vrIpMcastUsageState based on Integer32"""
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


_VrIpMcastUsageState_Type.__name__ = "Integer32"
_VrIpMcastUsageState_Object = MibTableColumn
vrIpMcastUsageState = _VrIpMcastUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 103, 1, 3),
    _VrIpMcastUsageState_Type()
)
vrIpMcastUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastUsageState.setStatus("mandatory")
_VrIpMcastOperStatusTable_Object = MibTable
vrIpMcastOperStatusTable = _VrIpMcastOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 104)
)
if mibBuilder.loadTexts:
    vrIpMcastOperStatusTable.setStatus("mandatory")
_VrIpMcastOperStatusEntry_Object = MibTableRow
vrIpMcastOperStatusEntry = _VrIpMcastOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 104, 1)
)
vrIpMcastOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastOperStatusEntry.setStatus("mandatory")


class _VrIpMcastSnmpOperStatus_Type(Integer32):
    """Custom type vrIpMcastSnmpOperStatus based on Integer32"""
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


_VrIpMcastSnmpOperStatus_Type.__name__ = "Integer32"
_VrIpMcastSnmpOperStatus_Object = MibTableColumn
vrIpMcastSnmpOperStatus = _VrIpMcastSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 104, 1, 1),
    _VrIpMcastSnmpOperStatus_Type()
)
vrIpMcastSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpMcastSnmpOperStatus.setStatus("mandatory")
_VrIpMcastCtsTable_Object = MibTable
vrIpMcastCtsTable = _VrIpMcastCtsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 701)
)
if mibBuilder.loadTexts:
    vrIpMcastCtsTable.setStatus("mandatory")
_VrIpMcastCtsEntry_Object = MibTableRow
vrIpMcastCtsEntry = _VrIpMcastCtsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 701, 1)
)
vrIpMcastCtsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpMcastCtsIndex"),
)
if mibBuilder.loadTexts:
    vrIpMcastCtsEntry.setStatus("mandatory")


class _VrIpMcastCtsIndex_Type(Integer32):
    """Custom type vrIpMcastCtsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_VrIpMcastCtsIndex_Type.__name__ = "Integer32"
_VrIpMcastCtsIndex_Object = MibTableColumn
vrIpMcastCtsIndex = _VrIpMcastCtsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 701, 1, 1),
    _VrIpMcastCtsIndex_Type()
)
vrIpMcastCtsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpMcastCtsIndex.setStatus("mandatory")


class _VrIpMcastCtsValue_Type(Unsigned32):
    """Custom type vrIpMcastCtsValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 500),
    )


_VrIpMcastCtsValue_Type.__name__ = "Unsigned32"
_VrIpMcastCtsValue_Object = MibTableColumn
vrIpMcastCtsValue = _VrIpMcastCtsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 26, 701, 1, 2),
    _VrIpMcastCtsValue_Type()
)
vrIpMcastCtsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpMcastCtsValue.setStatus("mandatory")
_VrIpProvTable_Object = MibTable
vrIpProvTable = _VrIpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 100)
)
if mibBuilder.loadTexts:
    vrIpProvTable.setStatus("mandatory")
_VrIpProvEntry_Object = MibTableRow
vrIpProvEntry = _VrIpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 100, 1)
)
vrIpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
)
if mibBuilder.loadTexts:
    vrIpProvEntry.setStatus("mandatory")


class _VrIpForwarding_Type(Integer32):
    """Custom type vrIpForwarding based on Integer32"""
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


_VrIpForwarding_Type.__name__ = "Integer32"
_VrIpForwarding_Object = MibTableColumn
vrIpForwarding = _VrIpForwarding_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 100, 1, 2),
    _VrIpForwarding_Type()
)
vrIpForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpForwarding.setStatus("mandatory")


class _VrIpDefaultTtl_Type(Unsigned32):
    """Custom type vrIpDefaultTtl based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(255, 255),
    )


_VrIpDefaultTtl_Type.__name__ = "Unsigned32"
_VrIpDefaultTtl_Object = MibTableColumn
vrIpDefaultTtl = _VrIpDefaultTtl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 100, 1, 3),
    _VrIpDefaultTtl_Type()
)
vrIpDefaultTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpDefaultTtl.setStatus("mandatory")
_VrIpCosPolicyAssignment_Type = Link
_VrIpCosPolicyAssignment_Object = MibTableColumn
vrIpCosPolicyAssignment = _VrIpCosPolicyAssignment_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 100, 1, 4),
    _VrIpCosPolicyAssignment_Type()
)
vrIpCosPolicyAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpCosPolicyAssignment.setStatus("mandatory")
_VrIpStatsTable_Object = MibTable
vrIpStatsTable = _VrIpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 101)
)
if mibBuilder.loadTexts:
    vrIpStatsTable.setStatus("mandatory")
_VrIpStatsEntry_Object = MibTableRow
vrIpStatsEntry = _VrIpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 101, 1)
)
vrIpStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
)
if mibBuilder.loadTexts:
    vrIpStatsEntry.setStatus("mandatory")
_VrIpInReceives_Type = Counter32
_VrIpInReceives_Object = MibTableColumn
vrIpInReceives = _VrIpInReceives_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 101, 1, 1),
    _VrIpInReceives_Type()
)
vrIpInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpInReceives.setStatus("mandatory")
_VrIpInHdrErrors_Type = Counter32
_VrIpInHdrErrors_Object = MibTableColumn
vrIpInHdrErrors = _VrIpInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 101, 1, 2),
    _VrIpInHdrErrors_Type()
)
vrIpInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpInHdrErrors.setStatus("mandatory")
_VrIpInAddrErrors_Type = Counter32
_VrIpInAddrErrors_Object = MibTableColumn
vrIpInAddrErrors = _VrIpInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 101, 1, 3),
    _VrIpInAddrErrors_Type()
)
vrIpInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpInAddrErrors.setStatus("mandatory")
_VrIpForwDatagrams_Type = Counter32
_VrIpForwDatagrams_Object = MibTableColumn
vrIpForwDatagrams = _VrIpForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 101, 1, 4),
    _VrIpForwDatagrams_Type()
)
vrIpForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpForwDatagrams.setStatus("mandatory")
_VrIpInUnknownProtos_Type = Counter32
_VrIpInUnknownProtos_Object = MibTableColumn
vrIpInUnknownProtos = _VrIpInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 101, 1, 5),
    _VrIpInUnknownProtos_Type()
)
vrIpInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpInUnknownProtos.setStatus("mandatory")
_VrIpInDiscards_Type = Counter32
_VrIpInDiscards_Object = MibTableColumn
vrIpInDiscards = _VrIpInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 101, 1, 6),
    _VrIpInDiscards_Type()
)
vrIpInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpInDiscards.setStatus("mandatory")
_VrIpInDelivers_Type = Counter32
_VrIpInDelivers_Object = MibTableColumn
vrIpInDelivers = _VrIpInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 101, 1, 7),
    _VrIpInDelivers_Type()
)
vrIpInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpInDelivers.setStatus("mandatory")
_VrIpOutRequests_Type = Counter32
_VrIpOutRequests_Object = MibTableColumn
vrIpOutRequests = _VrIpOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 101, 1, 8),
    _VrIpOutRequests_Type()
)
vrIpOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOutRequests.setStatus("mandatory")
_VrIpOutDiscards_Type = Counter32
_VrIpOutDiscards_Object = MibTableColumn
vrIpOutDiscards = _VrIpOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 101, 1, 9),
    _VrIpOutDiscards_Type()
)
vrIpOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOutDiscards.setStatus("mandatory")
_VrIpOutNoRoutes_Type = Counter32
_VrIpOutNoRoutes_Object = MibTableColumn
vrIpOutNoRoutes = _VrIpOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 101, 1, 10),
    _VrIpOutNoRoutes_Type()
)
vrIpOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOutNoRoutes.setStatus("mandatory")


class _VrIpReasmTimeOut_Type(Unsigned32):
    """Custom type vrIpReasmTimeOut based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_VrIpReasmTimeOut_Type.__name__ = "Unsigned32"
_VrIpReasmTimeOut_Object = MibTableColumn
vrIpReasmTimeOut = _VrIpReasmTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 101, 1, 11),
    _VrIpReasmTimeOut_Type()
)
vrIpReasmTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpReasmTimeOut.setStatus("mandatory")
_VrIpReasmReqds_Type = Counter32
_VrIpReasmReqds_Object = MibTableColumn
vrIpReasmReqds = _VrIpReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 101, 1, 12),
    _VrIpReasmReqds_Type()
)
vrIpReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpReasmReqds.setStatus("mandatory")
_VrIpReasmOks_Type = Counter32
_VrIpReasmOks_Object = MibTableColumn
vrIpReasmOks = _VrIpReasmOks_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 101, 1, 13),
    _VrIpReasmOks_Type()
)
vrIpReasmOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpReasmOks.setStatus("mandatory")
_VrIpReasmFails_Type = Counter32
_VrIpReasmFails_Object = MibTableColumn
vrIpReasmFails = _VrIpReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 101, 1, 14),
    _VrIpReasmFails_Type()
)
vrIpReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpReasmFails.setStatus("mandatory")
_VrIpFragOks_Type = Counter32
_VrIpFragOks_Object = MibTableColumn
vrIpFragOks = _VrIpFragOks_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 101, 1, 15),
    _VrIpFragOks_Type()
)
vrIpFragOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpFragOks.setStatus("mandatory")
_VrIpFragFails_Type = Counter32
_VrIpFragFails_Object = MibTableColumn
vrIpFragFails = _VrIpFragFails_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 101, 1, 16),
    _VrIpFragFails_Type()
)
vrIpFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpFragFails.setStatus("mandatory")
_VrIpFragCreates_Type = Counter32
_VrIpFragCreates_Object = MibTableColumn
vrIpFragCreates = _VrIpFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 101, 1, 17),
    _VrIpFragCreates_Type()
)
vrIpFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpFragCreates.setStatus("mandatory")
_VrIpRoutingDiscards_Type = Counter32
_VrIpRoutingDiscards_Object = MibTableColumn
vrIpRoutingDiscards = _VrIpRoutingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 101, 1, 18),
    _VrIpRoutingDiscards_Type()
)
vrIpRoutingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpRoutingDiscards.setStatus("mandatory")
_VrIpAdminControlTable_Object = MibTable
vrIpAdminControlTable = _VrIpAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 102)
)
if mibBuilder.loadTexts:
    vrIpAdminControlTable.setStatus("mandatory")
_VrIpAdminControlEntry_Object = MibTableRow
vrIpAdminControlEntry = _VrIpAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 102, 1)
)
vrIpAdminControlEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
)
if mibBuilder.loadTexts:
    vrIpAdminControlEntry.setStatus("mandatory")


class _VrIpSnmpAdminStatus_Type(Integer32):
    """Custom type vrIpSnmpAdminStatus based on Integer32"""
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


_VrIpSnmpAdminStatus_Type.__name__ = "Integer32"
_VrIpSnmpAdminStatus_Object = MibTableColumn
vrIpSnmpAdminStatus = _VrIpSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 102, 1, 1),
    _VrIpSnmpAdminStatus_Type()
)
vrIpSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpSnmpAdminStatus.setStatus("mandatory")
_VrIpStateTable_Object = MibTable
vrIpStateTable = _VrIpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 104)
)
if mibBuilder.loadTexts:
    vrIpStateTable.setStatus("mandatory")
_VrIpStateEntry_Object = MibTableRow
vrIpStateEntry = _VrIpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 104, 1)
)
vrIpStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
)
if mibBuilder.loadTexts:
    vrIpStateEntry.setStatus("mandatory")


class _VrIpAdminState_Type(Integer32):
    """Custom type vrIpAdminState based on Integer32"""
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


_VrIpAdminState_Type.__name__ = "Integer32"
_VrIpAdminState_Object = MibTableColumn
vrIpAdminState = _VrIpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 104, 1, 1),
    _VrIpAdminState_Type()
)
vrIpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpAdminState.setStatus("mandatory")


class _VrIpOperationalState_Type(Integer32):
    """Custom type vrIpOperationalState based on Integer32"""
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


_VrIpOperationalState_Type.__name__ = "Integer32"
_VrIpOperationalState_Object = MibTableColumn
vrIpOperationalState = _VrIpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 104, 1, 2),
    _VrIpOperationalState_Type()
)
vrIpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpOperationalState.setStatus("mandatory")


class _VrIpUsageState_Type(Integer32):
    """Custom type vrIpUsageState based on Integer32"""
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


_VrIpUsageState_Type.__name__ = "Integer32"
_VrIpUsageState_Object = MibTableColumn
vrIpUsageState = _VrIpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 104, 1, 3),
    _VrIpUsageState_Type()
)
vrIpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpUsageState.setStatus("mandatory")
_VrIpOperStatusTable_Object = MibTable
vrIpOperStatusTable = _VrIpOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 107)
)
if mibBuilder.loadTexts:
    vrIpOperStatusTable.setStatus("mandatory")
_VrIpOperStatusEntry_Object = MibTableRow
vrIpOperStatusEntry = _VrIpOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 107, 1)
)
vrIpOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
)
if mibBuilder.loadTexts:
    vrIpOperStatusEntry.setStatus("mandatory")


class _VrIpSnmpOperStatus_Type(Integer32):
    """Custom type vrIpSnmpOperStatus based on Integer32"""
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


_VrIpSnmpOperStatus_Type.__name__ = "Integer32"
_VrIpSnmpOperStatus_Object = MibTableColumn
vrIpSnmpOperStatus = _VrIpSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 107, 1, 1),
    _VrIpSnmpOperStatus_Type()
)
vrIpSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpSnmpOperStatus.setStatus("mandatory")
_VrIpCtsTable_Object = MibTable
vrIpCtsTable = _VrIpCtsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 394)
)
if mibBuilder.loadTexts:
    vrIpCtsTable.setStatus("mandatory")
_VrIpCtsEntry_Object = MibTableRow
vrIpCtsEntry = _VrIpCtsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 394, 1)
)
vrIpCtsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpCtsIndex"),
)
if mibBuilder.loadTexts:
    vrIpCtsEntry.setStatus("mandatory")


class _VrIpCtsIndex_Type(Integer32):
    """Custom type vrIpCtsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_VrIpCtsIndex_Type.__name__ = "Integer32"
_VrIpCtsIndex_Object = MibTableColumn
vrIpCtsIndex = _VrIpCtsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 394, 1, 1),
    _VrIpCtsIndex_Type()
)
vrIpCtsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpCtsIndex.setStatus("mandatory")


class _VrIpCtsValue_Type(Unsigned32):
    """Custom type vrIpCtsValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 8000),
    )


_VrIpCtsValue_Type.__name__ = "Unsigned32"
_VrIpCtsValue_Object = MibTableColumn
vrIpCtsValue = _VrIpCtsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 394, 1, 2),
    _VrIpCtsValue_Type()
)
vrIpCtsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpCtsValue.setStatus("mandatory")
_IpMIB_ObjectIdentity = ObjectIdentity
ipMIB = _IpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 27)
)
_IpGroup_ObjectIdentity = ObjectIdentity
ipGroup = _IpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 27, 1)
)
_IpGroupBE_ObjectIdentity = ObjectIdentity
ipGroupBE = _IpGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 27, 1, 5)
)
_IpGroupBE01_ObjectIdentity = ObjectIdentity
ipGroupBE01 = _IpGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 27, 1, 5, 2)
)
_IpGroupBE01A_ObjectIdentity = ObjectIdentity
ipGroupBE01A = _IpGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 27, 1, 5, 2, 2)
)
_IpCapabilities_ObjectIdentity = ObjectIdentity
ipCapabilities = _IpCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 27, 3)
)
_IpCapabilitiesBE_ObjectIdentity = ObjectIdentity
ipCapabilitiesBE = _IpCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 27, 3, 5)
)
_IpCapabilitiesBE01_ObjectIdentity = ObjectIdentity
ipCapabilitiesBE01 = _IpCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 27, 3, 5, 2)
)
_IpCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
ipCapabilitiesBE01A = _IpCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 27, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-IpMIB",
    **{"vrPpIpPort": vrPpIpPort,
       "vrPpIpPortRowStatusTable": vrPpIpPortRowStatusTable,
       "vrPpIpPortRowStatusEntry": vrPpIpPortRowStatusEntry,
       "vrPpIpPortRowStatus": vrPpIpPortRowStatus,
       "vrPpIpPortComponentName": vrPpIpPortComponentName,
       "vrPpIpPortStorageType": vrPpIpPortStorageType,
       "vrPpIpPortIndex": vrPpIpPortIndex,
       "vrPpIpPortLogicalIf": vrPpIpPortLogicalIf,
       "vrPpIpPortLogicalIfRowStatusTable": vrPpIpPortLogicalIfRowStatusTable,
       "vrPpIpPortLogicalIfRowStatusEntry": vrPpIpPortLogicalIfRowStatusEntry,
       "vrPpIpPortLogicalIfRowStatus": vrPpIpPortLogicalIfRowStatus,
       "vrPpIpPortLogicalIfComponentName": vrPpIpPortLogicalIfComponentName,
       "vrPpIpPortLogicalIfStorageType": vrPpIpPortLogicalIfStorageType,
       "vrPpIpPortLogicalIfAddressIndex": vrPpIpPortLogicalIfAddressIndex,
       "vrPpIpPortLogicalIfOspfIf": vrPpIpPortLogicalIfOspfIf,
       "vrPpIpPortLogicalIfOspfIfRowStatusTable": vrPpIpPortLogicalIfOspfIfRowStatusTable,
       "vrPpIpPortLogicalIfOspfIfRowStatusEntry": vrPpIpPortLogicalIfOspfIfRowStatusEntry,
       "vrPpIpPortLogicalIfOspfIfRowStatus": vrPpIpPortLogicalIfOspfIfRowStatus,
       "vrPpIpPortLogicalIfOspfIfComponentName": vrPpIpPortLogicalIfOspfIfComponentName,
       "vrPpIpPortLogicalIfOspfIfStorageType": vrPpIpPortLogicalIfOspfIfStorageType,
       "vrPpIpPortLogicalIfOspfIfIndex": vrPpIpPortLogicalIfOspfIfIndex,
       "vrPpIpPortLogicalIfOspfIfTOS": vrPpIpPortLogicalIfOspfIfTOS,
       "vrPpIpPortLogicalIfOspfIfTOSRowStatusTable": vrPpIpPortLogicalIfOspfIfTOSRowStatusTable,
       "vrPpIpPortLogicalIfOspfIfTOSRowStatusEntry": vrPpIpPortLogicalIfOspfIfTOSRowStatusEntry,
       "vrPpIpPortLogicalIfOspfIfTOSRowStatus": vrPpIpPortLogicalIfOspfIfTOSRowStatus,
       "vrPpIpPortLogicalIfOspfIfTOSComponentName": vrPpIpPortLogicalIfOspfIfTOSComponentName,
       "vrPpIpPortLogicalIfOspfIfTOSStorageType": vrPpIpPortLogicalIfOspfIfTOSStorageType,
       "vrPpIpPortLogicalIfOspfIfTOSMetricTosIndex": vrPpIpPortLogicalIfOspfIfTOSMetricTosIndex,
       "vrPpIpPortLogicalIfOspfIfTOSProvTable": vrPpIpPortLogicalIfOspfIfTOSProvTable,
       "vrPpIpPortLogicalIfOspfIfTOSProvEntry": vrPpIpPortLogicalIfOspfIfTOSProvEntry,
       "vrPpIpPortLogicalIfOspfIfTOSTosMetric": vrPpIpPortLogicalIfOspfIfTOSTosMetric,
       "vrPpIpPortLogicalIfOspfIfNbr": vrPpIpPortLogicalIfOspfIfNbr,
       "vrPpIpPortLogicalIfOspfIfNbrRowStatusTable": vrPpIpPortLogicalIfOspfIfNbrRowStatusTable,
       "vrPpIpPortLogicalIfOspfIfNbrRowStatusEntry": vrPpIpPortLogicalIfOspfIfNbrRowStatusEntry,
       "vrPpIpPortLogicalIfOspfIfNbrRowStatus": vrPpIpPortLogicalIfOspfIfNbrRowStatus,
       "vrPpIpPortLogicalIfOspfIfNbrComponentName": vrPpIpPortLogicalIfOspfIfNbrComponentName,
       "vrPpIpPortLogicalIfOspfIfNbrStorageType": vrPpIpPortLogicalIfOspfIfNbrStorageType,
       "vrPpIpPortLogicalIfOspfIfNbrAddressIndex": vrPpIpPortLogicalIfOspfIfNbrAddressIndex,
       "vrPpIpPortLogicalIfOspfIfNbrProvTable": vrPpIpPortLogicalIfOspfIfNbrProvTable,
       "vrPpIpPortLogicalIfOspfIfNbrProvEntry": vrPpIpPortLogicalIfOspfIfNbrProvEntry,
       "vrPpIpPortLogicalIfOspfIfNbrPriority": vrPpIpPortLogicalIfOspfIfNbrPriority,
       "vrPpIpPortLogicalIfOspfIfNbrOperTable": vrPpIpPortLogicalIfOspfIfNbrOperTable,
       "vrPpIpPortLogicalIfOspfIfNbrOperEntry": vrPpIpPortLogicalIfOspfIfNbrOperEntry,
       "vrPpIpPortLogicalIfOspfIfNbrRtrId": vrPpIpPortLogicalIfOspfIfNbrRtrId,
       "vrPpIpPortLogicalIfOspfIfNbrOptions": vrPpIpPortLogicalIfOspfIfNbrOptions,
       "vrPpIpPortLogicalIfOspfIfNbrState": vrPpIpPortLogicalIfOspfIfNbrState,
       "vrPpIpPortLogicalIfOspfIfNbrEvents": vrPpIpPortLogicalIfOspfIfNbrEvents,
       "vrPpIpPortLogicalIfOspfIfNbrLsRetransQlen": vrPpIpPortLogicalIfOspfIfNbrLsRetransQlen,
       "vrPpIpPortLogicalIfOspfIfNbrExchangeStatus": vrPpIpPortLogicalIfOspfIfNbrExchangeStatus,
       "vrPpIpPortLogicalIfOspfIfNbrPermanance": vrPpIpPortLogicalIfOspfIfNbrPermanance,
       "vrPpIpPortLogicalIfOspfIfProvTable": vrPpIpPortLogicalIfOspfIfProvTable,
       "vrPpIpPortLogicalIfOspfIfProvEntry": vrPpIpPortLogicalIfOspfIfProvEntry,
       "vrPpIpPortLogicalIfOspfIfAreaId": vrPpIpPortLogicalIfOspfIfAreaId,
       "vrPpIpPortLogicalIfOspfIfIfType": vrPpIpPortLogicalIfOspfIfIfType,
       "vrPpIpPortLogicalIfOspfIfSnmpAdminStatus": vrPpIpPortLogicalIfOspfIfSnmpAdminStatus,
       "vrPpIpPortLogicalIfOspfIfRtrPriority": vrPpIpPortLogicalIfOspfIfRtrPriority,
       "vrPpIpPortLogicalIfOspfIfTransitDelay": vrPpIpPortLogicalIfOspfIfTransitDelay,
       "vrPpIpPortLogicalIfOspfIfRetransInterval": vrPpIpPortLogicalIfOspfIfRetransInterval,
       "vrPpIpPortLogicalIfOspfIfHelloInterval": vrPpIpPortLogicalIfOspfIfHelloInterval,
       "vrPpIpPortLogicalIfOspfIfRtrDeadInterval": vrPpIpPortLogicalIfOspfIfRtrDeadInterval,
       "vrPpIpPortLogicalIfOspfIfPollInterval": vrPpIpPortLogicalIfOspfIfPollInterval,
       "vrPpIpPortLogicalIfOspfIfAuthKey": vrPpIpPortLogicalIfOspfIfAuthKey,
       "vrPpIpPortLogicalIfOspfIfMulticastForwarding": vrPpIpPortLogicalIfOspfIfMulticastForwarding,
       "vrPpIpPortLogicalIfOspfIfOperTable": vrPpIpPortLogicalIfOspfIfOperTable,
       "vrPpIpPortLogicalIfOspfIfOperEntry": vrPpIpPortLogicalIfOspfIfOperEntry,
       "vrPpIpPortLogicalIfOspfIfState": vrPpIpPortLogicalIfOspfIfState,
       "vrPpIpPortLogicalIfOspfIfDesignatedRouter": vrPpIpPortLogicalIfOspfIfDesignatedRouter,
       "vrPpIpPortLogicalIfOspfIfBackupDesignatedRouter": vrPpIpPortLogicalIfOspfIfBackupDesignatedRouter,
       "vrPpIpPortLogicalIfOspfIfEvents": vrPpIpPortLogicalIfOspfIfEvents,
       "vrPpIpPortLogicalIfOspfIfMetricTable": vrPpIpPortLogicalIfOspfIfMetricTable,
       "vrPpIpPortLogicalIfOspfIfMetricEntry": vrPpIpPortLogicalIfOspfIfMetricEntry,
       "vrPpIpPortLogicalIfOspfIfMetric": vrPpIpPortLogicalIfOspfIfMetric,
       "vrPpIpPortLogicalIfRipIf": vrPpIpPortLogicalIfRipIf,
       "vrPpIpPortLogicalIfRipIfRowStatusTable": vrPpIpPortLogicalIfRipIfRowStatusTable,
       "vrPpIpPortLogicalIfRipIfRowStatusEntry": vrPpIpPortLogicalIfRipIfRowStatusEntry,
       "vrPpIpPortLogicalIfRipIfRowStatus": vrPpIpPortLogicalIfRipIfRowStatus,
       "vrPpIpPortLogicalIfRipIfComponentName": vrPpIpPortLogicalIfRipIfComponentName,
       "vrPpIpPortLogicalIfRipIfStorageType": vrPpIpPortLogicalIfRipIfStorageType,
       "vrPpIpPortLogicalIfRipIfIndex": vrPpIpPortLogicalIfRipIfIndex,
       "vrPpIpPortLogicalIfRipIfNbr": vrPpIpPortLogicalIfRipIfNbr,
       "vrPpIpPortLogicalIfRipIfNbrRowStatusTable": vrPpIpPortLogicalIfRipIfNbrRowStatusTable,
       "vrPpIpPortLogicalIfRipIfNbrRowStatusEntry": vrPpIpPortLogicalIfRipIfNbrRowStatusEntry,
       "vrPpIpPortLogicalIfRipIfNbrRowStatus": vrPpIpPortLogicalIfRipIfNbrRowStatus,
       "vrPpIpPortLogicalIfRipIfNbrComponentName": vrPpIpPortLogicalIfRipIfNbrComponentName,
       "vrPpIpPortLogicalIfRipIfNbrStorageType": vrPpIpPortLogicalIfRipIfNbrStorageType,
       "vrPpIpPortLogicalIfRipIfNbrIndex": vrPpIpPortLogicalIfRipIfNbrIndex,
       "vrPpIpPortLogicalIfRipIfProvTable": vrPpIpPortLogicalIfRipIfProvTable,
       "vrPpIpPortLogicalIfRipIfProvEntry": vrPpIpPortLogicalIfRipIfProvEntry,
       "vrPpIpPortLogicalIfRipIfSnmpAdminStatus": vrPpIpPortLogicalIfRipIfSnmpAdminStatus,
       "vrPpIpPortLogicalIfRipIfMetric": vrPpIpPortLogicalIfRipIfMetric,
       "vrPpIpPortLogicalIfRipIfSilentFlag": vrPpIpPortLogicalIfRipIfSilentFlag,
       "vrPpIpPortLogicalIfRipIfPoisonReverseFlag": vrPpIpPortLogicalIfRipIfPoisonReverseFlag,
       "vrPpIpPortLogicalIfRipIfFlashUpdateFlag": vrPpIpPortLogicalIfRipIfFlashUpdateFlag,
       "vrPpIpPortLogicalIfRipIfNetworkRouteStatus": vrPpIpPortLogicalIfRipIfNetworkRouteStatus,
       "vrPpIpPortLogicalIfRipIfDefaultRouteMetric": vrPpIpPortLogicalIfRipIfDefaultRouteMetric,
       "vrPpIpPortLogicalIfRipIfAcceptDefault": vrPpIpPortLogicalIfRipIfAcceptDefault,
       "vrPpIpPortLogicalIfRipIfIfConfSend": vrPpIpPortLogicalIfRipIfIfConfSend,
       "vrPpIpPortLogicalIfRipIfIfConfReceive": vrPpIpPortLogicalIfRipIfIfConfReceive,
       "vrPpIpPortLogicalIfRipIfStatTable": vrPpIpPortLogicalIfRipIfStatTable,
       "vrPpIpPortLogicalIfRipIfStatEntry": vrPpIpPortLogicalIfRipIfStatEntry,
       "vrPpIpPortLogicalIfRipIfIfBadPacketRcv": vrPpIpPortLogicalIfRipIfIfBadPacketRcv,
       "vrPpIpPortLogicalIfRipIfIfBadRouteRcv": vrPpIpPortLogicalIfRipIfIfBadRouteRcv,
       "vrPpIpPortLogicalIfRipIfIfTriggeredUpdates": vrPpIpPortLogicalIfRipIfIfTriggeredUpdates,
       "vrPpIpPortLogicalIfIgmpIf": vrPpIpPortLogicalIfIgmpIf,
       "vrPpIpPortLogicalIfIgmpIfRowStatusTable": vrPpIpPortLogicalIfIgmpIfRowStatusTable,
       "vrPpIpPortLogicalIfIgmpIfRowStatusEntry": vrPpIpPortLogicalIfIgmpIfRowStatusEntry,
       "vrPpIpPortLogicalIfIgmpIfRowStatus": vrPpIpPortLogicalIfIgmpIfRowStatus,
       "vrPpIpPortLogicalIfIgmpIfComponentName": vrPpIpPortLogicalIfIgmpIfComponentName,
       "vrPpIpPortLogicalIfIgmpIfStorageType": vrPpIpPortLogicalIfIgmpIfStorageType,
       "vrPpIpPortLogicalIfIgmpIfIndex": vrPpIpPortLogicalIfIgmpIfIndex,
       "vrPpIpPortLogicalIfIgmpIfProvTable": vrPpIpPortLogicalIfIgmpIfProvTable,
       "vrPpIpPortLogicalIfIgmpIfProvEntry": vrPpIpPortLogicalIfIgmpIfProvEntry,
       "vrPpIpPortLogicalIfIgmpIfVersion": vrPpIpPortLogicalIfIgmpIfVersion,
       "vrPpIpPortLogicalIfIgmpIfQueryInterval": vrPpIpPortLogicalIfIgmpIfQueryInterval,
       "vrPpIpPortLogicalIfIgmpIfQueryMaxRespTime": vrPpIpPortLogicalIfIgmpIfQueryMaxRespTime,
       "vrPpIpPortLogicalIfIgmpIfOperTable": vrPpIpPortLogicalIfIgmpIfOperTable,
       "vrPpIpPortLogicalIfIgmpIfOperEntry": vrPpIpPortLogicalIfIgmpIfOperEntry,
       "vrPpIpPortLogicalIfIgmpIfQuerier": vrPpIpPortLogicalIfIgmpIfQuerier,
       "vrPpIpPortLogicalIfIgmpIfWrongVersionQuery": vrPpIpPortLogicalIfIgmpIfWrongVersionQuery,
       "vrPpIpPortLogicalIfIgmpIfJoins": vrPpIpPortLogicalIfIgmpIfJoins,
       "vrPpIpPortLogicalIfIgmpIfGroups": vrPpIpPortLogicalIfIgmpIfGroups,
       "vrPpIpPortLogicalIfIgmpIfQuerierExpiryTime": vrPpIpPortLogicalIfIgmpIfQuerierExpiryTime,
       "vrPpIpPortLogicalIfPimSmIf": vrPpIpPortLogicalIfPimSmIf,
       "vrPpIpPortLogicalIfPimSmIfRowStatusTable": vrPpIpPortLogicalIfPimSmIfRowStatusTable,
       "vrPpIpPortLogicalIfPimSmIfRowStatusEntry": vrPpIpPortLogicalIfPimSmIfRowStatusEntry,
       "vrPpIpPortLogicalIfPimSmIfRowStatus": vrPpIpPortLogicalIfPimSmIfRowStatus,
       "vrPpIpPortLogicalIfPimSmIfComponentName": vrPpIpPortLogicalIfPimSmIfComponentName,
       "vrPpIpPortLogicalIfPimSmIfStorageType": vrPpIpPortLogicalIfPimSmIfStorageType,
       "vrPpIpPortLogicalIfPimSmIfIndex": vrPpIpPortLogicalIfPimSmIfIndex,
       "vrPpIpPortLogicalIfPimSmIfProvTable": vrPpIpPortLogicalIfPimSmIfProvTable,
       "vrPpIpPortLogicalIfPimSmIfProvEntry": vrPpIpPortLogicalIfPimSmIfProvEntry,
       "vrPpIpPortLogicalIfPimSmIfHelloInterval": vrPpIpPortLogicalIfPimSmIfHelloInterval,
       "vrPpIpPortLogicalIfPimSmIfOperTable": vrPpIpPortLogicalIfPimSmIfOperTable,
       "vrPpIpPortLogicalIfPimSmIfOperEntry": vrPpIpPortLogicalIfPimSmIfOperEntry,
       "vrPpIpPortLogicalIfPimSmIfDesignatedRouter": vrPpIpPortLogicalIfPimSmIfDesignatedRouter,
       "vrPpIpPortLogicalIfProvTable": vrPpIpPortLogicalIfProvTable,
       "vrPpIpPortLogicalIfProvEntry": vrPpIpPortLogicalIfProvEntry,
       "vrPpIpPortLogicalIfNetMask": vrPpIpPortLogicalIfNetMask,
       "vrPpIpPortLogicalIfBroadcastAddress": vrPpIpPortLogicalIfBroadcastAddress,
       "vrPpIpPortLogicalIfLinkDestinationAddress": vrPpIpPortLogicalIfLinkDestinationAddress,
       "vrPpIpPortLogicalIfLinkToPimSmCandidateRp": vrPpIpPortLogicalIfLinkToPimSmCandidateRp,
       "vrPpIpPortLogicalIfLinkToPimSmCandidateBsr": vrPpIpPortLogicalIfLinkToPimSmCandidateBsr,
       "vrPpIpPortLogicalIfLinkToMulStaticGpTable": vrPpIpPortLogicalIfLinkToMulStaticGpTable,
       "vrPpIpPortLogicalIfLinkToMulStaticGpEntry": vrPpIpPortLogicalIfLinkToMulStaticGpEntry,
       "vrPpIpPortLogicalIfLinkToMulStaticGpValue": vrPpIpPortLogicalIfLinkToMulStaticGpValue,
       "vrPpIpPortLogicalIfLinkToMulStaticGpRowStatus": vrPpIpPortLogicalIfLinkToMulStaticGpRowStatus,
       "vrPpIpPortNs": vrPpIpPortNs,
       "vrPpIpPortNsRowStatusTable": vrPpIpPortNsRowStatusTable,
       "vrPpIpPortNsRowStatusEntry": vrPpIpPortNsRowStatusEntry,
       "vrPpIpPortNsRowStatus": vrPpIpPortNsRowStatus,
       "vrPpIpPortNsComponentName": vrPpIpPortNsComponentName,
       "vrPpIpPortNsStorageType": vrPpIpPortNsStorageType,
       "vrPpIpPortNsIndex": vrPpIpPortNsIndex,
       "vrPpIpPortNsProvTable": vrPpIpPortNsProvTable,
       "vrPpIpPortNsProvEntry": vrPpIpPortNsProvEntry,
       "vrPpIpPortNsIncomingFilter": vrPpIpPortNsIncomingFilter,
       "vrPpIpPortNsOutgoingFilter": vrPpIpPortNsOutgoingFilter,
       "vrPpIpPortBootpP": vrPpIpPortBootpP,
       "vrPpIpPortBootpPRowStatusTable": vrPpIpPortBootpPRowStatusTable,
       "vrPpIpPortBootpPRowStatusEntry": vrPpIpPortBootpPRowStatusEntry,
       "vrPpIpPortBootpPRowStatus": vrPpIpPortBootpPRowStatus,
       "vrPpIpPortBootpPComponentName": vrPpIpPortBootpPComponentName,
       "vrPpIpPortBootpPStorageType": vrPpIpPortBootpPStorageType,
       "vrPpIpPortBootpPIndex": vrPpIpPortBootpPIndex,
       "vrPpIpPortBootpPProvTable": vrPpIpPortBootpPProvTable,
       "vrPpIpPortBootpPProvEntry": vrPpIpPortBootpPProvEntry,
       "vrPpIpPortBootpPRelayForwardStatus": vrPpIpPortBootpPRelayForwardStatus,
       "vrPpIpPortBootpPBootpLogicalInterface": vrPpIpPortBootpPBootpLogicalInterface,
       "vrPpIpPortBootpPAdminControlTable": vrPpIpPortBootpPAdminControlTable,
       "vrPpIpPortBootpPAdminControlEntry": vrPpIpPortBootpPAdminControlEntry,
       "vrPpIpPortBootpPSnmpAdminStatus": vrPpIpPortBootpPSnmpAdminStatus,
       "vrPpIpPortBootpPOperStatusTable": vrPpIpPortBootpPOperStatusTable,
       "vrPpIpPortBootpPOperStatusEntry": vrPpIpPortBootpPOperStatusEntry,
       "vrPpIpPortBootpPSnmpOperStatus": vrPpIpPortBootpPSnmpOperStatus,
       "vrPpIpPortBootpPStateTable": vrPpIpPortBootpPStateTable,
       "vrPpIpPortBootpPStateEntry": vrPpIpPortBootpPStateEntry,
       "vrPpIpPortBootpPAdminState": vrPpIpPortBootpPAdminState,
       "vrPpIpPortBootpPOperationalState": vrPpIpPortBootpPOperationalState,
       "vrPpIpPortBootpPUsageState": vrPpIpPortBootpPUsageState,
       "vrPpIpPortBootpPStatsTable": vrPpIpPortBootpPStatsTable,
       "vrPpIpPortBootpPStatsEntry": vrPpIpPortBootpPStatsEntry,
       "vrPpIpPortBootpPInRequests": vrPpIpPortBootpPInRequests,
       "vrPpIpPortBootpPInReplies": vrPpIpPortBootpPInReplies,
       "vrPpIpPortBootpPOutRequests": vrPpIpPortBootpPOutRequests,
       "vrPpIpPortBootpPOutReplies": vrPpIpPortBootpPOutReplies,
       "vrPpIpPortBootpPInRequestErrors": vrPpIpPortBootpPInRequestErrors,
       "vrPpIpPortBootpPInReplyErrors": vrPpIpPortBootpPInReplyErrors,
       "vrPpIpPortBootpPAddrTable": vrPpIpPortBootpPAddrTable,
       "vrPpIpPortBootpPAddrEntry": vrPpIpPortBootpPAddrEntry,
       "vrPpIpPortBootpPAddrValue": vrPpIpPortBootpPAddrValue,
       "vrPpIpPortBootpPAddrRowStatus": vrPpIpPortBootpPAddrRowStatus,
       "vrPpIpPortProvTable": vrPpIpPortProvTable,
       "vrPpIpPortProvEntry": vrPpIpPortProvEntry,
       "vrPpIpPortMaxTxUnit": vrPpIpPortMaxTxUnit,
       "vrPpIpPortArpStatus": vrPpIpPortArpStatus,
       "vrPpIpPortProxyArpStatus": vrPpIpPortProxyArpStatus,
       "vrPpIpPortArpNoLearn": vrPpIpPortArpNoLearn,
       "vrPpIpPortSendRedirect": vrPpIpPortSendRedirect,
       "vrPpIpPortMulticastStatus": vrPpIpPortMulticastStatus,
       "vrPpIpPortRelayAddress": vrPpIpPortRelayAddress,
       "vrPpIpPortRelayBroadcast": vrPpIpPortRelayBroadcast,
       "vrPpIpPortLinkModel": vrPpIpPortLinkModel,
       "vrPpIpPortLanModel": vrPpIpPortLanModel,
       "vrPpIpPortEncap": vrPpIpPortEncap,
       "vrPpIpPortIcmpMaskReply": vrPpIpPortIcmpMaskReply,
       "vrPpIpPortDirectedBroadcast": vrPpIpPortDirectedBroadcast,
       "vrPpIpPortAssignedQos": vrPpIpPortAssignedQos,
       "vrPpIpPortAllowMcastMacDest": vrPpIpPortAllowMcastMacDest,
       "vrPpIpPortCosPolicyAssignment": vrPpIpPortCosPolicyAssignment,
       "vrPpIpPortMcastDomain": vrPpIpPortMcastDomain,
       "vrPpIpPortMcastPolicyAssignment": vrPpIpPortMcastPolicyAssignment,
       "vrPpIpPortSresProvTable": vrPpIpPortSresProvTable,
       "vrPpIpPortSresProvEntry": vrPpIpPortSresProvEntry,
       "vrPpIpPortSourceRouteEndStationSupport": vrPpIpPortSourceRouteEndStationSupport,
       "vrPpIpPortAdminControlTable": vrPpIpPortAdminControlTable,
       "vrPpIpPortAdminControlEntry": vrPpIpPortAdminControlEntry,
       "vrPpIpPortSnmpAdminStatus": vrPpIpPortSnmpAdminStatus,
       "vrPpIpPortOperTable": vrPpIpPortOperTable,
       "vrPpIpPortOperEntry": vrPpIpPortOperEntry,
       "vrPpIpPortMediaType": vrPpIpPortMediaType,
       "vrPpIpPortOperMtu": vrPpIpPortOperMtu,
       "vrPpIpPortOperArpStatus": vrPpIpPortOperArpStatus,
       "vrPpIpPortOperMulticastStatus": vrPpIpPortOperMulticastStatus,
       "vrPpIpPortOperEncap": vrPpIpPortOperEncap,
       "vrPpIpPortOperCosPolicyAssignment": vrPpIpPortOperCosPolicyAssignment,
       "vrPpIpPortRelayBcOperTable": vrPpIpPortRelayBcOperTable,
       "vrPpIpPortRelayBcOperEntry": vrPpIpPortRelayBcOperEntry,
       "vrPpIpPortRelayAddressCount": vrPpIpPortRelayAddressCount,
       "vrPpIpPortRelayBcCount": vrPpIpPortRelayBcCount,
       "vrPpIpPortStateTable": vrPpIpPortStateTable,
       "vrPpIpPortStateEntry": vrPpIpPortStateEntry,
       "vrPpIpPortAdminState": vrPpIpPortAdminState,
       "vrPpIpPortOperationalState": vrPpIpPortOperationalState,
       "vrPpIpPortUsageState": vrPpIpPortUsageState,
       "vrPpIpPortOperStatusTable": vrPpIpPortOperStatusTable,
       "vrPpIpPortOperStatusEntry": vrPpIpPortOperStatusEntry,
       "vrPpIpPortSnmpOperStatus": vrPpIpPortSnmpOperStatus,
       "vrIp": vrIp,
       "vrIpRowStatusTable": vrIpRowStatusTable,
       "vrIpRowStatusEntry": vrIpRowStatusEntry,
       "vrIpRowStatus": vrIpRowStatus,
       "vrIpComponentName": vrIpComponentName,
       "vrIpStorageType": vrIpStorageType,
       "vrIpIndex": vrIpIndex,
       "vrIpFwd": vrIpFwd,
       "vrIpFwdRowStatusTable": vrIpFwdRowStatusTable,
       "vrIpFwdRowStatusEntry": vrIpFwdRowStatusEntry,
       "vrIpFwdRowStatus": vrIpFwdRowStatus,
       "vrIpFwdComponentName": vrIpFwdComponentName,
       "vrIpFwdStorageType": vrIpFwdStorageType,
       "vrIpFwdDestAddressIndex": vrIpFwdDestAddressIndex,
       "vrIpFwdDestMaskIndex": vrIpFwdDestMaskIndex,
       "vrIpFwdTypeOfServiceIndex": vrIpFwdTypeOfServiceIndex,
       "vrIpFwdGatewayIndex": vrIpFwdGatewayIndex,
       "vrIpFwdOperTable": vrIpFwdOperTable,
       "vrIpFwdOperEntry": vrIpFwdOperEntry,
       "vrIpFwdIfIndex": vrIpFwdIfIndex,
       "vrIpFwdType": vrIpFwdType,
       "vrIpFwdProtocol": vrIpFwdProtocol,
       "vrIpFwdAge": vrIpFwdAge,
       "vrIpFwdProtocolPortName": vrIpFwdProtocolPortName,
       "vrIpFwdNextHopAs": vrIpFwdNextHopAs,
       "vrIpFwdMetric": vrIpFwdMetric,
       "vrIpRdb": vrIpRdb,
       "vrIpRdbRowStatusTable": vrIpRdbRowStatusTable,
       "vrIpRdbRowStatusEntry": vrIpRdbRowStatusEntry,
       "vrIpRdbRowStatus": vrIpRdbRowStatus,
       "vrIpRdbComponentName": vrIpRdbComponentName,
       "vrIpRdbStorageType": vrIpRdbStorageType,
       "vrIpRdbDestAddressIndex": vrIpRdbDestAddressIndex,
       "vrIpRdbDestMaskIndex": vrIpRdbDestMaskIndex,
       "vrIpRdbProtocolIndex": vrIpRdbProtocolIndex,
       "vrIpRdbGatewayIndex": vrIpRdbGatewayIndex,
       "vrIpRdbOperTable": vrIpRdbOperTable,
       "vrIpRdbOperEntry": vrIpRdbOperEntry,
       "vrIpRdbMetric": vrIpRdbMetric,
       "vrIpRdbPreference": vrIpRdbPreference,
       "vrIpRdbAge": vrIpRdbAge,
       "vrIpIf": vrIpIf,
       "vrIpIfRowStatusTable": vrIpIfRowStatusTable,
       "vrIpIfRowStatusEntry": vrIpIfRowStatusEntry,
       "vrIpIfRowStatus": vrIpIfRowStatus,
       "vrIpIfComponentName": vrIpIfComponentName,
       "vrIpIfStorageType": vrIpIfStorageType,
       "vrIpIfInterfaceAddressIndex": vrIpIfInterfaceAddressIndex,
       "vrIpIfOperTable": vrIpIfOperTable,
       "vrIpIfOperEntry": vrIpIfOperEntry,
       "vrIpIfInterfaceMask": vrIpIfInterfaceMask,
       "vrIpIfStatus": vrIpIfStatus,
       "vrIpIfPPName": vrIpIfPPName,
       "vrIpIfMediaType": vrIpIfMediaType,
       "vrIpIfHardwareAddress": vrIpIfHardwareAddress,
       "vrIpIfMtu": vrIpIfMtu,
       "vrIpIfBroadcastAddress": vrIpIfBroadcastAddress,
       "vrIpIfNcHardwareAddress": vrIpIfNcHardwareAddress,
       "vrIpEgp": vrIpEgp,
       "vrIpEgpRowStatusTable": vrIpEgpRowStatusTable,
       "vrIpEgpRowStatusEntry": vrIpEgpRowStatusEntry,
       "vrIpEgpRowStatus": vrIpEgpRowStatus,
       "vrIpEgpComponentName": vrIpEgpComponentName,
       "vrIpEgpStorageType": vrIpEgpStorageType,
       "vrIpEgpIndex": vrIpEgpIndex,
       "vrIpEgpNbr": vrIpEgpNbr,
       "vrIpEgpNbrRowStatusTable": vrIpEgpNbrRowStatusTable,
       "vrIpEgpNbrRowStatusEntry": vrIpEgpNbrRowStatusEntry,
       "vrIpEgpNbrRowStatus": vrIpEgpNbrRowStatus,
       "vrIpEgpNbrComponentName": vrIpEgpNbrComponentName,
       "vrIpEgpNbrStorageType": vrIpEgpNbrStorageType,
       "vrIpEgpNbrNeighborAddressIndex": vrIpEgpNbrNeighborAddressIndex,
       "vrIpEgpNbrProvTable": vrIpEgpNbrProvTable,
       "vrIpEgpNbrProvEntry": vrIpEgpNbrProvEntry,
       "vrIpEgpNbrAsId": vrIpEgpNbrAsId,
       "vrIpEgpNbrMode": vrIpEgpNbrMode,
       "vrIpEgpNbrGenerateDefaultRoute": vrIpEgpNbrGenerateDefaultRoute,
       "vrIpEgpNbrDefaultRouteMetric": vrIpEgpNbrDefaultRouteMetric,
       "vrIpEgpNbrDefaultMetric": vrIpEgpNbrDefaultMetric,
       "vrIpEgpNbrHelloInterval": vrIpEgpNbrHelloInterval,
       "vrIpEgpNbrPollInterval": vrIpEgpNbrPollInterval,
       "vrIpEgpNbrOperTable": vrIpEgpNbrOperTable,
       "vrIpEgpNbrOperEntry": vrIpEgpNbrOperEntry,
       "vrIpEgpNbrState": vrIpEgpNbrState,
       "vrIpEgpNbrInMsgs": vrIpEgpNbrInMsgs,
       "vrIpEgpNbrInErrors": vrIpEgpNbrInErrors,
       "vrIpEgpNbrOutMsgs": vrIpEgpNbrOutMsgs,
       "vrIpEgpNbrOutErrors": vrIpEgpNbrOutErrors,
       "vrIpEgpNbrInErrorMsgs": vrIpEgpNbrInErrorMsgs,
       "vrIpEgpNbrOutErrorMsgs": vrIpEgpNbrOutErrorMsgs,
       "vrIpEgpNbrStateUps": vrIpEgpNbrStateUps,
       "vrIpEgpNbrStateDowns": vrIpEgpNbrStateDowns,
       "vrIpEgpNbrEventTrigger": vrIpEgpNbrEventTrigger,
       "vrIpEgpImport": vrIpEgpImport,
       "vrIpEgpImportRowStatusTable": vrIpEgpImportRowStatusTable,
       "vrIpEgpImportRowStatusEntry": vrIpEgpImportRowStatusEntry,
       "vrIpEgpImportRowStatus": vrIpEgpImportRowStatus,
       "vrIpEgpImportComponentName": vrIpEgpImportComponentName,
       "vrIpEgpImportStorageType": vrIpEgpImportStorageType,
       "vrIpEgpImportIndex": vrIpEgpImportIndex,
       "vrIpEgpImportNet": vrIpEgpImportNet,
       "vrIpEgpImportNetRowStatusTable": vrIpEgpImportNetRowStatusTable,
       "vrIpEgpImportNetRowStatusEntry": vrIpEgpImportNetRowStatusEntry,
       "vrIpEgpImportNetRowStatus": vrIpEgpImportNetRowStatus,
       "vrIpEgpImportNetComponentName": vrIpEgpImportNetComponentName,
       "vrIpEgpImportNetStorageType": vrIpEgpImportNetStorageType,
       "vrIpEgpImportNetIndex": vrIpEgpImportNetIndex,
       "vrIpEgpImportNetProvTable": vrIpEgpImportNetProvTable,
       "vrIpEgpImportNetProvEntry": vrIpEgpImportNetProvEntry,
       "vrIpEgpImportNetIpAddress": vrIpEgpImportNetIpAddress,
       "vrIpEgpImportProvTable": vrIpEgpImportProvTable,
       "vrIpEgpImportProvEntry": vrIpEgpImportProvEntry,
       "vrIpEgpImportUsageFlag": vrIpEgpImportUsageFlag,
       "vrIpEgpImportImportMetric": vrIpEgpImportImportMetric,
       "vrIpEgpImportNbrAsId": vrIpEgpImportNbrAsId,
       "vrIpEgpExport": vrIpEgpExport,
       "vrIpEgpExportRowStatusTable": vrIpEgpExportRowStatusTable,
       "vrIpEgpExportRowStatusEntry": vrIpEgpExportRowStatusEntry,
       "vrIpEgpExportRowStatus": vrIpEgpExportRowStatus,
       "vrIpEgpExportComponentName": vrIpEgpExportComponentName,
       "vrIpEgpExportStorageType": vrIpEgpExportStorageType,
       "vrIpEgpExportIndex": vrIpEgpExportIndex,
       "vrIpEgpExportNet": vrIpEgpExportNet,
       "vrIpEgpExportNetRowStatusTable": vrIpEgpExportNetRowStatusTable,
       "vrIpEgpExportNetRowStatusEntry": vrIpEgpExportNetRowStatusEntry,
       "vrIpEgpExportNetRowStatus": vrIpEgpExportNetRowStatus,
       "vrIpEgpExportNetComponentName": vrIpEgpExportNetComponentName,
       "vrIpEgpExportNetStorageType": vrIpEgpExportNetStorageType,
       "vrIpEgpExportNetIndex": vrIpEgpExportNetIndex,
       "vrIpEgpExportNetProvTable": vrIpEgpExportNetProvTable,
       "vrIpEgpExportNetProvEntry": vrIpEgpExportNetProvEntry,
       "vrIpEgpExportNetIpAddress": vrIpEgpExportNetIpAddress,
       "vrIpEgpExportProvTable": vrIpEgpExportProvTable,
       "vrIpEgpExportProvEntry": vrIpEgpExportProvEntry,
       "vrIpEgpExportAdvertiseStatus": vrIpEgpExportAdvertiseStatus,
       "vrIpEgpExportExportMetric": vrIpEgpExportExportMetric,
       "vrIpEgpExportProtocol": vrIpEgpExportProtocol,
       "vrIpEgpExportRipInterface": vrIpEgpExportRipInterface,
       "vrIpEgpExportRipNeighbor": vrIpEgpExportRipNeighbor,
       "vrIpEgpExportInEgpAsId": vrIpEgpExportInEgpAsId,
       "vrIpEgpExportOspfTag": vrIpEgpExportOspfTag,
       "vrIpEgpExportOutAutonomousSystem": vrIpEgpExportOutAutonomousSystem,
       "vrIpEgpProvTable": vrIpEgpProvTable,
       "vrIpEgpProvEntry": vrIpEgpProvEntry,
       "vrIpEgpAsId": vrIpEgpAsId,
       "vrIpEgpDefaultHelloInterval": vrIpEgpDefaultHelloInterval,
       "vrIpEgpDefaultPollInterval": vrIpEgpDefaultPollInterval,
       "vrIpEgpMaxNatNets": vrIpEgpMaxNatNets,
       "vrIpEgpMaxBufferSize": vrIpEgpMaxBufferSize,
       "vrIpEgpStatsTable": vrIpEgpStatsTable,
       "vrIpEgpStatsEntry": vrIpEgpStatsEntry,
       "vrIpEgpInMsgs": vrIpEgpInMsgs,
       "vrIpEgpInErrorMsgs": vrIpEgpInErrorMsgs,
       "vrIpEgpOutErrorMsgs": vrIpEgpOutErrorMsgs,
       "vrIpEgpInErrors": vrIpEgpInErrors,
       "vrIpEgpOutMsgs": vrIpEgpOutMsgs,
       "vrIpEgpOutErrors": vrIpEgpOutErrors,
       "vrIpEgpStateTable": vrIpEgpStateTable,
       "vrIpEgpStateEntry": vrIpEgpStateEntry,
       "vrIpEgpAdminState": vrIpEgpAdminState,
       "vrIpEgpOperationalState": vrIpEgpOperationalState,
       "vrIpEgpUsageState": vrIpEgpUsageState,
       "vrIpEgpAdminControlTable": vrIpEgpAdminControlTable,
       "vrIpEgpAdminControlEntry": vrIpEgpAdminControlEntry,
       "vrIpEgpSnmpAdminStatus": vrIpEgpSnmpAdminStatus,
       "vrIpEgpOperStatusTable": vrIpEgpOperStatusTable,
       "vrIpEgpOperStatusEntry": vrIpEgpOperStatusEntry,
       "vrIpEgpSnmpOperStatus": vrIpEgpSnmpOperStatus,
       "vrIpOspf": vrIpOspf,
       "vrIpOspfRowStatusTable": vrIpOspfRowStatusTable,
       "vrIpOspfRowStatusEntry": vrIpOspfRowStatusEntry,
       "vrIpOspfRowStatus": vrIpOspfRowStatus,
       "vrIpOspfComponentName": vrIpOspfComponentName,
       "vrIpOspfStorageType": vrIpOspfStorageType,
       "vrIpOspfIndex": vrIpOspfIndex,
       "vrIpOspfArea": vrIpOspfArea,
       "vrIpOspfAreaRowStatusTable": vrIpOspfAreaRowStatusTable,
       "vrIpOspfAreaRowStatusEntry": vrIpOspfAreaRowStatusEntry,
       "vrIpOspfAreaRowStatus": vrIpOspfAreaRowStatus,
       "vrIpOspfAreaComponentName": vrIpOspfAreaComponentName,
       "vrIpOspfAreaStorageType": vrIpOspfAreaStorageType,
       "vrIpOspfAreaAreaIdIndex": vrIpOspfAreaAreaIdIndex,
       "vrIpOspfAreaProvTable": vrIpOspfAreaProvTable,
       "vrIpOspfAreaProvEntry": vrIpOspfAreaProvEntry,
       "vrIpOspfAreaAuthType": vrIpOspfAreaAuthType,
       "vrIpOspfAreaImportAsExtern": vrIpOspfAreaImportAsExtern,
       "vrIpOspfAreaAreaSummary": vrIpOspfAreaAreaSummary,
       "vrIpOspfAreaOperTable": vrIpOspfAreaOperTable,
       "vrIpOspfAreaOperEntry": vrIpOspfAreaOperEntry,
       "vrIpOspfAreaSpfRuns": vrIpOspfAreaSpfRuns,
       "vrIpOspfAreaAreaBdrRtrCount": vrIpOspfAreaAreaBdrRtrCount,
       "vrIpOspfAreaAsBdrRtrCount": vrIpOspfAreaAsBdrRtrCount,
       "vrIpOspfAreaLsaCount": vrIpOspfAreaLsaCount,
       "vrIpOspfAreaAreaLsaCksumSum": vrIpOspfAreaAreaLsaCksumSum,
       "vrIpOspfStub": vrIpOspfStub,
       "vrIpOspfStubRowStatusTable": vrIpOspfStubRowStatusTable,
       "vrIpOspfStubRowStatusEntry": vrIpOspfStubRowStatusEntry,
       "vrIpOspfStubRowStatus": vrIpOspfStubRowStatus,
       "vrIpOspfStubComponentName": vrIpOspfStubComponentName,
       "vrIpOspfStubStorageType": vrIpOspfStubStorageType,
       "vrIpOspfStubAreaIdIndex": vrIpOspfStubAreaIdIndex,
       "vrIpOspfStubTosIndex": vrIpOspfStubTosIndex,
       "vrIpOspfStubProvTable": vrIpOspfStubProvTable,
       "vrIpOspfStubProvEntry": vrIpOspfStubProvEntry,
       "vrIpOspfStubMetric": vrIpOspfStubMetric,
       "vrIpOspfStubMetricType": vrIpOspfStubMetricType,
       "vrIpOspfStubAdvertiseDefault": vrIpOspfStubAdvertiseDefault,
       "vrIpOspfAggregate": vrIpOspfAggregate,
       "vrIpOspfAggregateRowStatusTable": vrIpOspfAggregateRowStatusTable,
       "vrIpOspfAggregateRowStatusEntry": vrIpOspfAggregateRowStatusEntry,
       "vrIpOspfAggregateRowStatus": vrIpOspfAggregateRowStatus,
       "vrIpOspfAggregateComponentName": vrIpOspfAggregateComponentName,
       "vrIpOspfAggregateStorageType": vrIpOspfAggregateStorageType,
       "vrIpOspfAggregateAreaIdIndex": vrIpOspfAggregateAreaIdIndex,
       "vrIpOspfAggregateLsdbTypeIndex": vrIpOspfAggregateLsdbTypeIndex,
       "vrIpOspfAggregateAggregateNetIndex": vrIpOspfAggregateAggregateNetIndex,
       "vrIpOspfAggregateAggregateMaskIndex": vrIpOspfAggregateAggregateMaskIndex,
       "vrIpOspfAggregateProvTable": vrIpOspfAggregateProvTable,
       "vrIpOspfAggregateProvEntry": vrIpOspfAggregateProvEntry,
       "vrIpOspfAggregateEffect": vrIpOspfAggregateEffect,
       "vrIpOspfHost": vrIpOspfHost,
       "vrIpOspfHostRowStatusTable": vrIpOspfHostRowStatusTable,
       "vrIpOspfHostRowStatusEntry": vrIpOspfHostRowStatusEntry,
       "vrIpOspfHostRowStatus": vrIpOspfHostRowStatus,
       "vrIpOspfHostComponentName": vrIpOspfHostComponentName,
       "vrIpOspfHostStorageType": vrIpOspfHostStorageType,
       "vrIpOspfHostAddressIndex": vrIpOspfHostAddressIndex,
       "vrIpOspfHostTosIndex": vrIpOspfHostTosIndex,
       "vrIpOspfHostProvTable": vrIpOspfHostProvTable,
       "vrIpOspfHostProvEntry": vrIpOspfHostProvEntry,
       "vrIpOspfHostAreaId": vrIpOspfHostAreaId,
       "vrIpOspfHostMetric": vrIpOspfHostMetric,
       "vrIpOspfVirtIf": vrIpOspfVirtIf,
       "vrIpOspfVirtIfRowStatusTable": vrIpOspfVirtIfRowStatusTable,
       "vrIpOspfVirtIfRowStatusEntry": vrIpOspfVirtIfRowStatusEntry,
       "vrIpOspfVirtIfRowStatus": vrIpOspfVirtIfRowStatus,
       "vrIpOspfVirtIfComponentName": vrIpOspfVirtIfComponentName,
       "vrIpOspfVirtIfStorageType": vrIpOspfVirtIfStorageType,
       "vrIpOspfVirtIfAreaIdIndex": vrIpOspfVirtIfAreaIdIndex,
       "vrIpOspfVirtIfNbrRouterIdIndex": vrIpOspfVirtIfNbrRouterIdIndex,
       "vrIpOspfVirtIfProvTable": vrIpOspfVirtIfProvTable,
       "vrIpOspfVirtIfProvEntry": vrIpOspfVirtIfProvEntry,
       "vrIpOspfVirtIfTransitDelay": vrIpOspfVirtIfTransitDelay,
       "vrIpOspfVirtIfRetransInterval": vrIpOspfVirtIfRetransInterval,
       "vrIpOspfVirtIfHelloInterval": vrIpOspfVirtIfHelloInterval,
       "vrIpOspfVirtIfRtrDeadInterval": vrIpOspfVirtIfRtrDeadInterval,
       "vrIpOspfVirtIfAuthKey": vrIpOspfVirtIfAuthKey,
       "vrIpOspfVirtIfOperTable": vrIpOspfVirtIfOperTable,
       "vrIpOspfVirtIfOperEntry": vrIpOspfVirtIfOperEntry,
       "vrIpOspfVirtIfState": vrIpOspfVirtIfState,
       "vrIpOspfVirtIfEvents": vrIpOspfVirtIfEvents,
       "vrIpOspfExport": vrIpOspfExport,
       "vrIpOspfExportRowStatusTable": vrIpOspfExportRowStatusTable,
       "vrIpOspfExportRowStatusEntry": vrIpOspfExportRowStatusEntry,
       "vrIpOspfExportRowStatus": vrIpOspfExportRowStatus,
       "vrIpOspfExportComponentName": vrIpOspfExportComponentName,
       "vrIpOspfExportStorageType": vrIpOspfExportStorageType,
       "vrIpOspfExportIndex": vrIpOspfExportIndex,
       "vrIpOspfExportNetList": vrIpOspfExportNetList,
       "vrIpOspfExportNetListRowStatusTable": vrIpOspfExportNetListRowStatusTable,
       "vrIpOspfExportNetListRowStatusEntry": vrIpOspfExportNetListRowStatusEntry,
       "vrIpOspfExportNetListRowStatus": vrIpOspfExportNetListRowStatus,
       "vrIpOspfExportNetListComponentName": vrIpOspfExportNetListComponentName,
       "vrIpOspfExportNetListStorageType": vrIpOspfExportNetListStorageType,
       "vrIpOspfExportNetListIndex": vrIpOspfExportNetListIndex,
       "vrIpOspfExportNetListProvTable": vrIpOspfExportNetListProvTable,
       "vrIpOspfExportNetListProvEntry": vrIpOspfExportNetListProvEntry,
       "vrIpOspfExportNetListIpAddress": vrIpOspfExportNetListIpAddress,
       "vrIpOspfExportNetListIpMask": vrIpOspfExportNetListIpMask,
       "vrIpOspfExportProvTable": vrIpOspfExportProvTable,
       "vrIpOspfExportProvEntry": vrIpOspfExportProvEntry,
       "vrIpOspfExportAdvertiseStatus": vrIpOspfExportAdvertiseStatus,
       "vrIpOspfExportMetric": vrIpOspfExportMetric,
       "vrIpOspfExportProtocol": vrIpOspfExportProtocol,
       "vrIpOspfExportRipInterface": vrIpOspfExportRipInterface,
       "vrIpOspfExportRipNeighbor": vrIpOspfExportRipNeighbor,
       "vrIpOspfExportEgpAsId": vrIpOspfExportEgpAsId,
       "vrIpOspfExportTag": vrIpOspfExportTag,
       "vrIpOspfExportExtLsaMetricType": vrIpOspfExportExtLsaMetricType,
       "vrIpOspfExportBgpAsId": vrIpOspfExportBgpAsId,
       "vrIpOspfExportBgpPeerIp": vrIpOspfExportBgpPeerIp,
       "vrIpOspfVirtNbr": vrIpOspfVirtNbr,
       "vrIpOspfVirtNbrRowStatusTable": vrIpOspfVirtNbrRowStatusTable,
       "vrIpOspfVirtNbrRowStatusEntry": vrIpOspfVirtNbrRowStatusEntry,
       "vrIpOspfVirtNbrRowStatus": vrIpOspfVirtNbrRowStatus,
       "vrIpOspfVirtNbrComponentName": vrIpOspfVirtNbrComponentName,
       "vrIpOspfVirtNbrStorageType": vrIpOspfVirtNbrStorageType,
       "vrIpOspfVirtNbrAreaIdIndex": vrIpOspfVirtNbrAreaIdIndex,
       "vrIpOspfVirtNbrNbrRouterIdIndex": vrIpOspfVirtNbrNbrRouterIdIndex,
       "vrIpOspfVirtNbrOperTable": vrIpOspfVirtNbrOperTable,
       "vrIpOspfVirtNbrOperEntry": vrIpOspfVirtNbrOperEntry,
       "vrIpOspfVirtNbrNbrIpAddress": vrIpOspfVirtNbrNbrIpAddress,
       "vrIpOspfVirtNbrOptions": vrIpOspfVirtNbrOptions,
       "vrIpOspfVirtNbrState": vrIpOspfVirtNbrState,
       "vrIpOspfVirtNbrEvents": vrIpOspfVirtNbrEvents,
       "vrIpOspfVirtNbrLsRetransQlen": vrIpOspfVirtNbrLsRetransQlen,
       "vrIpOspfVirtNbrExchangeStatus": vrIpOspfVirtNbrExchangeStatus,
       "vrIpOspfNbr": vrIpOspfNbr,
       "vrIpOspfNbrRowStatusTable": vrIpOspfNbrRowStatusTable,
       "vrIpOspfNbrRowStatusEntry": vrIpOspfNbrRowStatusEntry,
       "vrIpOspfNbrRowStatus": vrIpOspfNbrRowStatus,
       "vrIpOspfNbrComponentName": vrIpOspfNbrComponentName,
       "vrIpOspfNbrStorageType": vrIpOspfNbrStorageType,
       "vrIpOspfNbrAddressIndex": vrIpOspfNbrAddressIndex,
       "vrIpOspfNbrAddressLessIndex": vrIpOspfNbrAddressLessIndex,
       "vrIpOspfNbrOperTable": vrIpOspfNbrOperTable,
       "vrIpOspfNbrOperEntry": vrIpOspfNbrOperEntry,
       "vrIpOspfNbrRtrId": vrIpOspfNbrRtrId,
       "vrIpOspfNbrOptions": vrIpOspfNbrOptions,
       "vrIpOspfNbrPriority": vrIpOspfNbrPriority,
       "vrIpOspfNbrState": vrIpOspfNbrState,
       "vrIpOspfNbrEvents": vrIpOspfNbrEvents,
       "vrIpOspfNbrLsRetransQlen": vrIpOspfNbrLsRetransQlen,
       "vrIpOspfNbrNbmaNbrStatus": vrIpOspfNbrNbmaNbrStatus,
       "vrIpOspfNbrExchangeStatus": vrIpOspfNbrExchangeStatus,
       "vrIpOspfNbrPermanence": vrIpOspfNbrPermanence,
       "vrIpOspfLsdb": vrIpOspfLsdb,
       "vrIpOspfLsdbRowStatusTable": vrIpOspfLsdbRowStatusTable,
       "vrIpOspfLsdbRowStatusEntry": vrIpOspfLsdbRowStatusEntry,
       "vrIpOspfLsdbRowStatus": vrIpOspfLsdbRowStatus,
       "vrIpOspfLsdbComponentName": vrIpOspfLsdbComponentName,
       "vrIpOspfLsdbStorageType": vrIpOspfLsdbStorageType,
       "vrIpOspfLsdbAreaIdIndex": vrIpOspfLsdbAreaIdIndex,
       "vrIpOspfLsdbLsdbTypeIndex": vrIpOspfLsdbLsdbTypeIndex,
       "vrIpOspfLsdbLsIdIndex": vrIpOspfLsdbLsIdIndex,
       "vrIpOspfLsdbRouterIdIndex": vrIpOspfLsdbRouterIdIndex,
       "vrIpOspfLsdbOperTable": vrIpOspfLsdbOperTable,
       "vrIpOspfLsdbOperEntry": vrIpOspfLsdbOperEntry,
       "vrIpOspfLsdbSequence": vrIpOspfLsdbSequence,
       "vrIpOspfLsdbAge": vrIpOspfLsdbAge,
       "vrIpOspfLsdbChecksum": vrIpOspfLsdbChecksum,
       "vrIpOspfLsdbAdvertisement": vrIpOspfLsdbAdvertisement,
       "vrIpOspfExtLsdb": vrIpOspfExtLsdb,
       "vrIpOspfExtLsdbRowStatusTable": vrIpOspfExtLsdbRowStatusTable,
       "vrIpOspfExtLsdbRowStatusEntry": vrIpOspfExtLsdbRowStatusEntry,
       "vrIpOspfExtLsdbRowStatus": vrIpOspfExtLsdbRowStatus,
       "vrIpOspfExtLsdbComponentName": vrIpOspfExtLsdbComponentName,
       "vrIpOspfExtLsdbStorageType": vrIpOspfExtLsdbStorageType,
       "vrIpOspfExtLsdbLsdbTypeIndex": vrIpOspfExtLsdbLsdbTypeIndex,
       "vrIpOspfExtLsdbLsIdIndex": vrIpOspfExtLsdbLsIdIndex,
       "vrIpOspfExtLsdbRouterIdIndex": vrIpOspfExtLsdbRouterIdIndex,
       "vrIpOspfExtLsdbOperTable": vrIpOspfExtLsdbOperTable,
       "vrIpOspfExtLsdbOperEntry": vrIpOspfExtLsdbOperEntry,
       "vrIpOspfExtLsdbSequence": vrIpOspfExtLsdbSequence,
       "vrIpOspfExtLsdbAge": vrIpOspfExtLsdbAge,
       "vrIpOspfExtLsdbChecksum": vrIpOspfExtLsdbChecksum,
       "vrIpOspfExtLsdbAdvertisement": vrIpOspfExtLsdbAdvertisement,
       "vrIpOspfProvTable": vrIpOspfProvTable,
       "vrIpOspfProvEntry": vrIpOspfProvEntry,
       "vrIpOspfRouterId": vrIpOspfRouterId,
       "vrIpOspfSnmpAdminStatus": vrIpOspfSnmpAdminStatus,
       "vrIpOspfAsBdrRtrStatus": vrIpOspfAsBdrRtrStatus,
       "vrIpOspfTosSupport": vrIpOspfTosSupport,
       "vrIpOspfExtLsdbLimit": vrIpOspfExtLsdbLimit,
       "vrIpOspfMulticastForward": vrIpOspfMulticastForward,
       "vrIpOspfMigrateRip": vrIpOspfMigrateRip,
       "vrIpOspfGenerateDefaultRouteMetric": vrIpOspfGenerateDefaultRouteMetric,
       "vrIpOspfOperTable": vrIpOspfOperTable,
       "vrIpOspfOperEntry": vrIpOspfOperEntry,
       "vrIpOspfVersionNumber": vrIpOspfVersionNumber,
       "vrIpOspfAreaBdrRtrStatus": vrIpOspfAreaBdrRtrStatus,
       "vrIpOspfExternLsaCount": vrIpOspfExternLsaCount,
       "vrIpOspfExternLsaChecksumSum": vrIpOspfExternLsaChecksumSum,
       "vrIpOspfOriginateNewLsas": vrIpOspfOriginateNewLsas,
       "vrIpOspfRxNewLsas": vrIpOspfRxNewLsas,
       "vrIpOspfStateTable": vrIpOspfStateTable,
       "vrIpOspfStateEntry": vrIpOspfStateEntry,
       "vrIpOspfAdminState": vrIpOspfAdminState,
       "vrIpOspfOperationalState": vrIpOspfOperationalState,
       "vrIpOspfUsageState": vrIpOspfUsageState,
       "vrIpOspfOperStatusTable": vrIpOspfOperStatusTable,
       "vrIpOspfOperStatusEntry": vrIpOspfOperStatusEntry,
       "vrIpOspfSnmpOperStatus": vrIpOspfSnmpOperStatus,
       "vrIpRip": vrIpRip,
       "vrIpRipRowStatusTable": vrIpRipRowStatusTable,
       "vrIpRipRowStatusEntry": vrIpRipRowStatusEntry,
       "vrIpRipRowStatus": vrIpRipRowStatus,
       "vrIpRipComponentName": vrIpRipComponentName,
       "vrIpRipStorageType": vrIpRipStorageType,
       "vrIpRipIndex": vrIpRipIndex,
       "vrIpRipImport": vrIpRipImport,
       "vrIpRipImportRowStatusTable": vrIpRipImportRowStatusTable,
       "vrIpRipImportRowStatusEntry": vrIpRipImportRowStatusEntry,
       "vrIpRipImportRowStatus": vrIpRipImportRowStatus,
       "vrIpRipImportComponentName": vrIpRipImportComponentName,
       "vrIpRipImportStorageType": vrIpRipImportStorageType,
       "vrIpRipImportIndex": vrIpRipImportIndex,
       "vrIpRipImportNet": vrIpRipImportNet,
       "vrIpRipImportNetRowStatusTable": vrIpRipImportNetRowStatusTable,
       "vrIpRipImportNetRowStatusEntry": vrIpRipImportNetRowStatusEntry,
       "vrIpRipImportNetRowStatus": vrIpRipImportNetRowStatus,
       "vrIpRipImportNetComponentName": vrIpRipImportNetComponentName,
       "vrIpRipImportNetStorageType": vrIpRipImportNetStorageType,
       "vrIpRipImportNetIndex": vrIpRipImportNetIndex,
       "vrIpRipImportNetProvTable": vrIpRipImportNetProvTable,
       "vrIpRipImportNetProvEntry": vrIpRipImportNetProvEntry,
       "vrIpRipImportNetIpAddress": vrIpRipImportNetIpAddress,
       "vrIpRipImportNetIpMask": vrIpRipImportNetIpMask,
       "vrIpRipImportProvTable": vrIpRipImportProvTable,
       "vrIpRipImportProvEntry": vrIpRipImportProvEntry,
       "vrIpRipImportUsageFlag": vrIpRipImportUsageFlag,
       "vrIpRipImportImportMetric": vrIpRipImportImportMetric,
       "vrIpRipImportNeighbor": vrIpRipImportNeighbor,
       "vrIpRipImportInterface": vrIpRipImportInterface,
       "vrIpRipExport": vrIpRipExport,
       "vrIpRipExportRowStatusTable": vrIpRipExportRowStatusTable,
       "vrIpRipExportRowStatusEntry": vrIpRipExportRowStatusEntry,
       "vrIpRipExportRowStatus": vrIpRipExportRowStatus,
       "vrIpRipExportComponentName": vrIpRipExportComponentName,
       "vrIpRipExportStorageType": vrIpRipExportStorageType,
       "vrIpRipExportIndex": vrIpRipExportIndex,
       "vrIpRipExportNet": vrIpRipExportNet,
       "vrIpRipExportNetRowStatusTable": vrIpRipExportNetRowStatusTable,
       "vrIpRipExportNetRowStatusEntry": vrIpRipExportNetRowStatusEntry,
       "vrIpRipExportNetRowStatus": vrIpRipExportNetRowStatus,
       "vrIpRipExportNetComponentName": vrIpRipExportNetComponentName,
       "vrIpRipExportNetStorageType": vrIpRipExportNetStorageType,
       "vrIpRipExportNetIndex": vrIpRipExportNetIndex,
       "vrIpRipExportNetProvTable": vrIpRipExportNetProvTable,
       "vrIpRipExportNetProvEntry": vrIpRipExportNetProvEntry,
       "vrIpRipExportNetIpAddress": vrIpRipExportNetIpAddress,
       "vrIpRipExportNetIpMask": vrIpRipExportNetIpMask,
       "vrIpRipExportProvTable": vrIpRipExportProvTable,
       "vrIpRipExportProvEntry": vrIpRipExportProvEntry,
       "vrIpRipExportAdvertiseStatus": vrIpRipExportAdvertiseStatus,
       "vrIpRipExportExportMetric": vrIpRipExportExportMetric,
       "vrIpRipExportProtocol": vrIpRipExportProtocol,
       "vrIpRipExportRipInterface": vrIpRipExportRipInterface,
       "vrIpRipExportEgpAsId": vrIpRipExportEgpAsId,
       "vrIpRipExportOspfTag": vrIpRipExportOspfTag,
       "vrIpRipExportOutInterface": vrIpRipExportOutInterface,
       "vrIpRipExportBgpAsId": vrIpRipExportBgpAsId,
       "vrIpRipProvTable": vrIpRipProvTable,
       "vrIpRipProvEntry": vrIpRipProvEntry,
       "vrIpRipMigrateRip": vrIpRipMigrateRip,
       "vrIpRipRfc1058MetricUsage": vrIpRipRfc1058MetricUsage,
       "vrIpRipGenerateDiscardRoute": vrIpRipGenerateDiscardRoute,
       "vrIpRipRipUpdate": vrIpRipRipUpdate,
       "vrIpRipRipTimeout": vrIpRipRipTimeout,
       "vrIpRipGarbageCollectTimer": vrIpRipGarbageCollectTimer,
       "vrIpRipStateTable": vrIpRipStateTable,
       "vrIpRipStateEntry": vrIpRipStateEntry,
       "vrIpRipAdminState": vrIpRipAdminState,
       "vrIpRipOperationalState": vrIpRipOperationalState,
       "vrIpRipUsageState": vrIpRipUsageState,
       "vrIpRipAdminControlTable": vrIpRipAdminControlTable,
       "vrIpRipAdminControlEntry": vrIpRipAdminControlEntry,
       "vrIpRipSnmpAdminStatus": vrIpRipSnmpAdminStatus,
       "vrIpRipOperStatusTable": vrIpRipOperStatusTable,
       "vrIpRipOperStatusEntry": vrIpRipOperStatusEntry,
       "vrIpRipSnmpOperStatus": vrIpRipSnmpOperStatus,
       "vrIpRipOperTable": vrIpRipOperTable,
       "vrIpRipOperEntry": vrIpRipOperEntry,
       "vrIpRipRouteChangesMade": vrIpRipRouteChangesMade,
       "vrIpRipQueryResponses": vrIpRipQueryResponses,
       "vrIpStatic": vrIpStatic,
       "vrIpStaticRowStatusTable": vrIpStaticRowStatusTable,
       "vrIpStaticRowStatusEntry": vrIpStaticRowStatusEntry,
       "vrIpStaticRowStatus": vrIpStaticRowStatus,
       "vrIpStaticComponentName": vrIpStaticComponentName,
       "vrIpStaticStorageType": vrIpStaticStorageType,
       "vrIpStaticIndex": vrIpStaticIndex,
       "vrIpStaticRoute": vrIpStaticRoute,
       "vrIpStaticRouteRowStatusTable": vrIpStaticRouteRowStatusTable,
       "vrIpStaticRouteRowStatusEntry": vrIpStaticRouteRowStatusEntry,
       "vrIpStaticRouteRowStatus": vrIpStaticRouteRowStatus,
       "vrIpStaticRouteComponentName": vrIpStaticRouteComponentName,
       "vrIpStaticRouteStorageType": vrIpStaticRouteStorageType,
       "vrIpStaticRouteDestAddressIndex": vrIpStaticRouteDestAddressIndex,
       "vrIpStaticRouteDestMaskIndex": vrIpStaticRouteDestMaskIndex,
       "vrIpStaticRouteTypeOfServiceIndex": vrIpStaticRouteTypeOfServiceIndex,
       "vrIpStaticRouteNh": vrIpStaticRouteNh,
       "vrIpStaticRouteNhRowStatusTable": vrIpStaticRouteNhRowStatusTable,
       "vrIpStaticRouteNhRowStatusEntry": vrIpStaticRouteNhRowStatusEntry,
       "vrIpStaticRouteNhRowStatus": vrIpStaticRouteNhRowStatus,
       "vrIpStaticRouteNhComponentName": vrIpStaticRouteNhComponentName,
       "vrIpStaticRouteNhStorageType": vrIpStaticRouteNhStorageType,
       "vrIpStaticRouteNhIndex": vrIpStaticRouteNhIndex,
       "vrIpStaticRouteNhProvTable": vrIpStaticRouteNhProvTable,
       "vrIpStaticRouteNhProvEntry": vrIpStaticRouteNhProvEntry,
       "vrIpStaticRouteNhMetric": vrIpStaticRouteNhMetric,
       "vrIpStaticRouteProvTable": vrIpStaticRouteProvTable,
       "vrIpStaticRouteProvEntry": vrIpStaticRouteProvEntry,
       "vrIpStaticRoutePreferredOver": vrIpStaticRoutePreferredOver,
       "vrIpStaticDiscard": vrIpStaticDiscard,
       "vrIpStaticDiscardRowStatusTable": vrIpStaticDiscardRowStatusTable,
       "vrIpStaticDiscardRowStatusEntry": vrIpStaticDiscardRowStatusEntry,
       "vrIpStaticDiscardRowStatus": vrIpStaticDiscardRowStatus,
       "vrIpStaticDiscardComponentName": vrIpStaticDiscardComponentName,
       "vrIpStaticDiscardStorageType": vrIpStaticDiscardStorageType,
       "vrIpStaticDiscardDestAddressIndex": vrIpStaticDiscardDestAddressIndex,
       "vrIpStaticDiscardDestMaskIndex": vrIpStaticDiscardDestMaskIndex,
       "vrIpStaticStateTable": vrIpStaticStateTable,
       "vrIpStaticStateEntry": vrIpStaticStateEntry,
       "vrIpStaticAdminState": vrIpStaticAdminState,
       "vrIpStaticOperationalState": vrIpStaticOperationalState,
       "vrIpStaticUsageState": vrIpStaticUsageState,
       "vrIpNs": vrIpNs,
       "vrIpNsRowStatusTable": vrIpNsRowStatusTable,
       "vrIpNsRowStatusEntry": vrIpNsRowStatusEntry,
       "vrIpNsRowStatus": vrIpNsRowStatus,
       "vrIpNsComponentName": vrIpNsComponentName,
       "vrIpNsStorageType": vrIpNsStorageType,
       "vrIpNsIndex": vrIpNsIndex,
       "vrIpNsApply": vrIpNsApply,
       "vrIpNsApplyRowStatusTable": vrIpNsApplyRowStatusTable,
       "vrIpNsApplyRowStatusEntry": vrIpNsApplyRowStatusEntry,
       "vrIpNsApplyRowStatus": vrIpNsApplyRowStatus,
       "vrIpNsApplyComponentName": vrIpNsApplyComponentName,
       "vrIpNsApplyStorageType": vrIpNsApplyStorageType,
       "vrIpNsApplyIndex": vrIpNsApplyIndex,
       "vrIpNsApplyProvisionedTable": vrIpNsApplyProvisionedTable,
       "vrIpNsApplyProvisionedEntry": vrIpNsApplyProvisionedEntry,
       "vrIpNsApplyFilter": vrIpNsApplyFilter,
       "vrIpNsApplyIpAddress1": vrIpNsApplyIpAddress1,
       "vrIpNsApplyIpMask1": vrIpNsApplyIpMask1,
       "vrIpNsApplyIpAddress2": vrIpNsApplyIpAddress2,
       "vrIpNsApplyIpMask2": vrIpNsApplyIpMask2,
       "vrIpNsApplyDirection": vrIpNsApplyDirection,
       "vrIpNsProvTable": vrIpNsProvTable,
       "vrIpNsProvEntry": vrIpNsProvEntry,
       "vrIpNsFirstFilter": vrIpNsFirstFilter,
       "vrIpNsLocalInFilter": vrIpNsLocalInFilter,
       "vrIpNsLocalOutFilter": vrIpNsLocalOutFilter,
       "vrIpNsLastFilter": vrIpNsLastFilter,
       "vrIpArp": vrIpArp,
       "vrIpArpRowStatusTable": vrIpArpRowStatusTable,
       "vrIpArpRowStatusEntry": vrIpArpRowStatusEntry,
       "vrIpArpRowStatus": vrIpArpRowStatus,
       "vrIpArpComponentName": vrIpArpComponentName,
       "vrIpArpStorageType": vrIpArpStorageType,
       "vrIpArpIndex": vrIpArpIndex,
       "vrIpArpHost": vrIpArpHost,
       "vrIpArpHostRowStatusTable": vrIpArpHostRowStatusTable,
       "vrIpArpHostRowStatusEntry": vrIpArpHostRowStatusEntry,
       "vrIpArpHostRowStatus": vrIpArpHostRowStatus,
       "vrIpArpHostComponentName": vrIpArpHostComponentName,
       "vrIpArpHostStorageType": vrIpArpHostStorageType,
       "vrIpArpHostHostAddressIndex": vrIpArpHostHostAddressIndex,
       "vrIpArpHostProvTable": vrIpArpHostProvTable,
       "vrIpArpHostProvEntry": vrIpArpHostProvEntry,
       "vrIpArpHostPhysAddress": vrIpArpHostPhysAddress,
       "vrIpArpHostMaxTxUnit": vrIpArpHostMaxTxUnit,
       "vrIpArpHostPermanentVirtualCircuitNumber": vrIpArpHostPermanentVirtualCircuitNumber,
       "vrIpArpHostEncap": vrIpArpHostEncap,
       "vrIpArpHostOperTable": vrIpArpHostOperTable,
       "vrIpArpHostOperEntry": vrIpArpHostOperEntry,
       "vrIpArpHostOperMaxTxUnit": vrIpArpHostOperMaxTxUnit,
       "vrIpArpHostOperEncap": vrIpArpHostOperEncap,
       "vrIpArpDynHost": vrIpArpDynHost,
       "vrIpArpDynHostRowStatusTable": vrIpArpDynHostRowStatusTable,
       "vrIpArpDynHostRowStatusEntry": vrIpArpDynHostRowStatusEntry,
       "vrIpArpDynHostRowStatus": vrIpArpDynHostRowStatus,
       "vrIpArpDynHostComponentName": vrIpArpDynHostComponentName,
       "vrIpArpDynHostStorageType": vrIpArpDynHostStorageType,
       "vrIpArpDynHostHostAddressIndex": vrIpArpDynHostHostAddressIndex,
       "vrIpArpDynHostCosIndex": vrIpArpDynHostCosIndex,
       "vrIpArpDynHostOperTable": vrIpArpDynHostOperTable,
       "vrIpArpDynHostOperEntry": vrIpArpDynHostOperEntry,
       "vrIpArpDynHostPhysAddress": vrIpArpDynHostPhysAddress,
       "vrIpArpDynHostMaxTxUnit": vrIpArpDynHostMaxTxUnit,
       "vrIpArpDynHostEncapsulationType": vrIpArpDynHostEncapsulationType,
       "vrIpArpDynHostPermanentVirtualCircuitNumber": vrIpArpDynHostPermanentVirtualCircuitNumber,
       "vrIpArpDynHostIfIndex": vrIpArpDynHostIfIndex,
       "vrIpArpDynHostType": vrIpArpDynHostType,
       "vrIpArpDynHostNcPhysAddress": vrIpArpDynHostNcPhysAddress,
       "vrIpArpProvTable": vrIpArpProvTable,
       "vrIpArpProvEntry": vrIpArpProvEntry,
       "vrIpArpAutoRefresh": vrIpArpAutoRefresh,
       "vrIpArpAutoRefreshTimeout": vrIpArpAutoRefreshTimeout,
       "vrIpIcmp": vrIpIcmp,
       "vrIpIcmpRowStatusTable": vrIpIcmpRowStatusTable,
       "vrIpIcmpRowStatusEntry": vrIpIcmpRowStatusEntry,
       "vrIpIcmpRowStatus": vrIpIcmpRowStatus,
       "vrIpIcmpComponentName": vrIpIcmpComponentName,
       "vrIpIcmpStorageType": vrIpIcmpStorageType,
       "vrIpIcmpIndex": vrIpIcmpIndex,
       "vrIpIcmpProvTable": vrIpIcmpProvTable,
       "vrIpIcmpProvEntry": vrIpIcmpProvEntry,
       "vrIpIcmpSendRedirect": vrIpIcmpSendRedirect,
       "vrIpIcmpSendHostUnreachable": vrIpIcmpSendHostUnreachable,
       "vrIpIcmpStatsTable": vrIpIcmpStatsTable,
       "vrIpIcmpStatsEntry": vrIpIcmpStatsEntry,
       "vrIpIcmpInMsgs": vrIpIcmpInMsgs,
       "vrIpIcmpInErrors": vrIpIcmpInErrors,
       "vrIpIcmpInDestUnreachs": vrIpIcmpInDestUnreachs,
       "vrIpIcmpInTimeExcds": vrIpIcmpInTimeExcds,
       "vrIpIcmpInParmProbs": vrIpIcmpInParmProbs,
       "vrIpIcmpInSrcQuenchs": vrIpIcmpInSrcQuenchs,
       "vrIpIcmpInRedirects": vrIpIcmpInRedirects,
       "vrIpIcmpInEchos": vrIpIcmpInEchos,
       "vrIpIcmpInEchoReps": vrIpIcmpInEchoReps,
       "vrIpIcmpInTimestamps": vrIpIcmpInTimestamps,
       "vrIpIcmpInTimestampReps": vrIpIcmpInTimestampReps,
       "vrIpIcmpInAddrMasks": vrIpIcmpInAddrMasks,
       "vrIpIcmpInAddrMaskReps": vrIpIcmpInAddrMaskReps,
       "vrIpIcmpOutMsgs": vrIpIcmpOutMsgs,
       "vrIpIcmpOutErrors": vrIpIcmpOutErrors,
       "vrIpIcmpOutDestUnreachs": vrIpIcmpOutDestUnreachs,
       "vrIpIcmpOutTimeExcds": vrIpIcmpOutTimeExcds,
       "vrIpIcmpOutParmProbs": vrIpIcmpOutParmProbs,
       "vrIpIcmpOutSrcQuenchs": vrIpIcmpOutSrcQuenchs,
       "vrIpIcmpOutRedirects": vrIpIcmpOutRedirects,
       "vrIpIcmpOutEchos": vrIpIcmpOutEchos,
       "vrIpIcmpOutEchoReps": vrIpIcmpOutEchoReps,
       "vrIpIcmpOutTimestamps": vrIpIcmpOutTimestamps,
       "vrIpIcmpOutTimestampReps": vrIpIcmpOutTimestampReps,
       "vrIpIcmpOutAddrMasks": vrIpIcmpOutAddrMasks,
       "vrIpIcmpOutAddrMaskReps": vrIpIcmpOutAddrMaskReps,
       "vrIpIcmpInRtrAdvs": vrIpIcmpInRtrAdvs,
       "vrIpIcmpInRtrSolicits": vrIpIcmpInRtrSolicits,
       "vrIpIcmpOutRtrAdvs": vrIpIcmpOutRtrAdvs,
       "vrIpIcmpOutRtrSolicits": vrIpIcmpOutRtrSolicits,
       "vrIpRelayBC": vrIpRelayBC,
       "vrIpRelayBCRowStatusTable": vrIpRelayBCRowStatusTable,
       "vrIpRelayBCRowStatusEntry": vrIpRelayBCRowStatusEntry,
       "vrIpRelayBCRowStatus": vrIpRelayBCRowStatus,
       "vrIpRelayBCComponentName": vrIpRelayBCComponentName,
       "vrIpRelayBCStorageType": vrIpRelayBCStorageType,
       "vrIpRelayBCIndex": vrIpRelayBCIndex,
       "vrIpRelayBCPort": vrIpRelayBCPort,
       "vrIpRelayBCPortRowStatusTable": vrIpRelayBCPortRowStatusTable,
       "vrIpRelayBCPortRowStatusEntry": vrIpRelayBCPortRowStatusEntry,
       "vrIpRelayBCPortRowStatus": vrIpRelayBCPortRowStatus,
       "vrIpRelayBCPortComponentName": vrIpRelayBCPortComponentName,
       "vrIpRelayBCPortStorageType": vrIpRelayBCPortStorageType,
       "vrIpRelayBCPortPortNumIndex": vrIpRelayBCPortPortNumIndex,
       "vrIpRelayBCPortOperTable": vrIpRelayBCPortOperTable,
       "vrIpRelayBCPortOperEntry": vrIpRelayBCPortOperEntry,
       "vrIpRelayBCPortRelayBcUdpCount": vrIpRelayBCPortRelayBcUdpCount,
       "vrIpRelayBCProvTable": vrIpRelayBCProvTable,
       "vrIpRelayBCProvEntry": vrIpRelayBCProvEntry,
       "vrIpRelayBCRelayStatus": vrIpRelayBCRelayStatus,
       "vrIpRelayBCRelayNdStatus": vrIpRelayBCRelayNdStatus,
       "vrIpRelayBCOperTable": vrIpRelayBCOperTable,
       "vrIpRelayBCOperEntry": vrIpRelayBCOperEntry,
       "vrIpRelayBCRelayNdCount": vrIpRelayBCRelayNdCount,
       "vrIpUdp": vrIpUdp,
       "vrIpUdpRowStatusTable": vrIpUdpRowStatusTable,
       "vrIpUdpRowStatusEntry": vrIpUdpRowStatusEntry,
       "vrIpUdpRowStatus": vrIpUdpRowStatus,
       "vrIpUdpComponentName": vrIpUdpComponentName,
       "vrIpUdpStorageType": vrIpUdpStorageType,
       "vrIpUdpIndex": vrIpUdpIndex,
       "vrIpUdpListenEntry": vrIpUdpListenEntry,
       "vrIpUdpListenEntryRowStatusTable": vrIpUdpListenEntryRowStatusTable,
       "vrIpUdpListenEntryRowStatusEntry": vrIpUdpListenEntryRowStatusEntry,
       "vrIpUdpListenEntryRowStatus": vrIpUdpListenEntryRowStatus,
       "vrIpUdpListenEntryComponentName": vrIpUdpListenEntryComponentName,
       "vrIpUdpListenEntryStorageType": vrIpUdpListenEntryStorageType,
       "vrIpUdpListenEntryLocalAddressIndex": vrIpUdpListenEntryLocalAddressIndex,
       "vrIpUdpListenEntryLocalPortIndex": vrIpUdpListenEntryLocalPortIndex,
       "vrIpUdpStatsTable": vrIpUdpStatsTable,
       "vrIpUdpStatsEntry": vrIpUdpStatsEntry,
       "vrIpUdpInDatagrams": vrIpUdpInDatagrams,
       "vrIpUdpNoPorts": vrIpUdpNoPorts,
       "vrIpUdpInErrors": vrIpUdpInErrors,
       "vrIpUdpOutDatagrams": vrIpUdpOutDatagrams,
       "vrIpTcp": vrIpTcp,
       "vrIpTcpRowStatusTable": vrIpTcpRowStatusTable,
       "vrIpTcpRowStatusEntry": vrIpTcpRowStatusEntry,
       "vrIpTcpRowStatus": vrIpTcpRowStatus,
       "vrIpTcpComponentName": vrIpTcpComponentName,
       "vrIpTcpStorageType": vrIpTcpStorageType,
       "vrIpTcpIndex": vrIpTcpIndex,
       "vrIpTcpTcpEntry": vrIpTcpTcpEntry,
       "vrIpTcpTcpEntryRowStatusTable": vrIpTcpTcpEntryRowStatusTable,
       "vrIpTcpTcpEntryRowStatusEntry": vrIpTcpTcpEntryRowStatusEntry,
       "vrIpTcpTcpEntryRowStatus": vrIpTcpTcpEntryRowStatus,
       "vrIpTcpTcpEntryComponentName": vrIpTcpTcpEntryComponentName,
       "vrIpTcpTcpEntryStorageType": vrIpTcpTcpEntryStorageType,
       "vrIpTcpTcpEntryLocalAddressIndex": vrIpTcpTcpEntryLocalAddressIndex,
       "vrIpTcpTcpEntryLocalPortIndex": vrIpTcpTcpEntryLocalPortIndex,
       "vrIpTcpTcpEntryRemoteAddressIndex": vrIpTcpTcpEntryRemoteAddressIndex,
       "vrIpTcpTcpEntryRemotePortIndex": vrIpTcpTcpEntryRemotePortIndex,
       "vrIpTcpTcpEntryOperTable": vrIpTcpTcpEntryOperTable,
       "vrIpTcpTcpEntryOperEntry": vrIpTcpTcpEntryOperEntry,
       "vrIpTcpTcpEntryState": vrIpTcpTcpEntryState,
       "vrIpTcpStatsTable": vrIpTcpStatsTable,
       "vrIpTcpStatsEntry": vrIpTcpStatsEntry,
       "vrIpTcpRToAlgorithm": vrIpTcpRToAlgorithm,
       "vrIpTcpRToMin": vrIpTcpRToMin,
       "vrIpTcpRToMax": vrIpTcpRToMax,
       "vrIpTcpMaxConn": vrIpTcpMaxConn,
       "vrIpTcpActiveOpens": vrIpTcpActiveOpens,
       "vrIpTcpPassiveOpens": vrIpTcpPassiveOpens,
       "vrIpTcpAttemptFails": vrIpTcpAttemptFails,
       "vrIpTcpEstabResets": vrIpTcpEstabResets,
       "vrIpTcpCurrEstab": vrIpTcpCurrEstab,
       "vrIpTcpInSegs": vrIpTcpInSegs,
       "vrIpTcpOutSegs": vrIpTcpOutSegs,
       "vrIpTcpRetransSegs": vrIpTcpRetransSegs,
       "vrIpTcpInErrs": vrIpTcpInErrs,
       "vrIpTcpOutRsts": vrIpTcpOutRsts,
       "vrIpBootp": vrIpBootp,
       "vrIpBootpRowStatusTable": vrIpBootpRowStatusTable,
       "vrIpBootpRowStatusEntry": vrIpBootpRowStatusEntry,
       "vrIpBootpRowStatus": vrIpBootpRowStatus,
       "vrIpBootpComponentName": vrIpBootpComponentName,
       "vrIpBootpStorageType": vrIpBootpStorageType,
       "vrIpBootpIndex": vrIpBootpIndex,
       "vrIpBootpPpE": vrIpBootpPpE,
       "vrIpBootpPpERowStatusTable": vrIpBootpPpERowStatusTable,
       "vrIpBootpPpERowStatusEntry": vrIpBootpPpERowStatusEntry,
       "vrIpBootpPpERowStatus": vrIpBootpPpERowStatus,
       "vrIpBootpPpEComponentName": vrIpBootpPpEComponentName,
       "vrIpBootpPpEStorageType": vrIpBootpPpEStorageType,
       "vrIpBootpPpEIndex": vrIpBootpPpEIndex,
       "vrIpBootpPpEOperTable": vrIpBootpPpEOperTable,
       "vrIpBootpPpEOperEntry": vrIpBootpPpEOperEntry,
       "vrIpBootpPpEStatus": vrIpBootpPpEStatus,
       "vrIpBootpPpEStatsTable": vrIpBootpPpEStatsTable,
       "vrIpBootpPpEStatsEntry": vrIpBootpPpEStatsEntry,
       "vrIpBootpPpEInRequests": vrIpBootpPpEInRequests,
       "vrIpBootpPpEInReplies": vrIpBootpPpEInReplies,
       "vrIpBootpPpEOutRequests": vrIpBootpPpEOutRequests,
       "vrIpBootpPpEOutReplies": vrIpBootpPpEOutReplies,
       "vrIpBootpPpEInRequestErrors": vrIpBootpPpEInRequestErrors,
       "vrIpBootpPpEInReplyErrors": vrIpBootpPpEInReplyErrors,
       "vrIpBootpAdminControlTable": vrIpBootpAdminControlTable,
       "vrIpBootpAdminControlEntry": vrIpBootpAdminControlEntry,
       "vrIpBootpSnmpAdminStatus": vrIpBootpSnmpAdminStatus,
       "vrIpBootpProvTable": vrIpBootpProvTable,
       "vrIpBootpProvEntry": vrIpBootpProvEntry,
       "vrIpBootpHopDiscardThreshold": vrIpBootpHopDiscardThreshold,
       "vrIpBootpStateTable": vrIpBootpStateTable,
       "vrIpBootpStateEntry": vrIpBootpStateEntry,
       "vrIpBootpAdminState": vrIpBootpAdminState,
       "vrIpBootpOperationalState": vrIpBootpOperationalState,
       "vrIpBootpUsageState": vrIpBootpUsageState,
       "vrIpBootpOperStatusTable": vrIpBootpOperStatusTable,
       "vrIpBootpOperStatusEntry": vrIpBootpOperStatusEntry,
       "vrIpBootpSnmpOperStatus": vrIpBootpSnmpOperStatus,
       "vrIpCache": vrIpCache,
       "vrIpCacheRowStatusTable": vrIpCacheRowStatusTable,
       "vrIpCacheRowStatusEntry": vrIpCacheRowStatusEntry,
       "vrIpCacheRowStatus": vrIpCacheRowStatus,
       "vrIpCacheComponentName": vrIpCacheComponentName,
       "vrIpCacheStorageType": vrIpCacheStorageType,
       "vrIpCacheIndex": vrIpCacheIndex,
       "vrIpCacheStateTable": vrIpCacheStateTable,
       "vrIpCacheStateEntry": vrIpCacheStateEntry,
       "vrIpCacheAdminState": vrIpCacheAdminState,
       "vrIpCacheOperationalState": vrIpCacheOperationalState,
       "vrIpCacheUsageState": vrIpCacheUsageState,
       "vrIpCacheOperTable": vrIpCacheOperTable,
       "vrIpCacheOperEntry": vrIpCacheOperEntry,
       "vrIpCacheEntriesFree": vrIpCacheEntriesFree,
       "vrIpCacheTotalLookups": vrIpCacheTotalLookups,
       "vrIpCacheLookupMisses": vrIpCacheLookupMisses,
       "vrIpCacheCacheTableMaxEntries": vrIpCacheCacheTableMaxEntries,
       "vrIpTunnel": vrIpTunnel,
       "vrIpTunnelRowStatusTable": vrIpTunnelRowStatusTable,
       "vrIpTunnelRowStatusEntry": vrIpTunnelRowStatusEntry,
       "vrIpTunnelRowStatus": vrIpTunnelRowStatus,
       "vrIpTunnelComponentName": vrIpTunnelComponentName,
       "vrIpTunnelStorageType": vrIpTunnelStorageType,
       "vrIpTunnelIndex": vrIpTunnelIndex,
       "vrIpTunnelSep": vrIpTunnelSep,
       "vrIpTunnelSepRowStatusTable": vrIpTunnelSepRowStatusTable,
       "vrIpTunnelSepRowStatusEntry": vrIpTunnelSepRowStatusEntry,
       "vrIpTunnelSepRowStatus": vrIpTunnelSepRowStatus,
       "vrIpTunnelSepComponentName": vrIpTunnelSepComponentName,
       "vrIpTunnelSepStorageType": vrIpTunnelSepStorageType,
       "vrIpTunnelSepIndex": vrIpTunnelSepIndex,
       "vrIpTunnelSepIfEntryTable": vrIpTunnelSepIfEntryTable,
       "vrIpTunnelSepIfEntryEntry": vrIpTunnelSepIfEntryEntry,
       "vrIpTunnelSepIfAdminStatus": vrIpTunnelSepIfAdminStatus,
       "vrIpTunnelSepIfIndex": vrIpTunnelSepIfIndex,
       "vrIpTunnelSepMpTable": vrIpTunnelSepMpTable,
       "vrIpTunnelSepMpEntry": vrIpTunnelSepMpEntry,
       "vrIpTunnelSepLinkToProtocolPort": vrIpTunnelSepLinkToProtocolPort,
       "vrIpTunnelSepProvTable": vrIpTunnelSepProvTable,
       "vrIpTunnelSepProvEntry": vrIpTunnelSepProvEntry,
       "vrIpTunnelSepEncapType": vrIpTunnelSepEncapType,
       "vrIpTunnelSepSourceAddress": vrIpTunnelSepSourceAddress,
       "vrIpTunnelSepDestinationAddress": vrIpTunnelSepDestinationAddress,
       "vrIpTunnelSepOperTable": vrIpTunnelSepOperTable,
       "vrIpTunnelSepOperEntry": vrIpTunnelSepOperEntry,
       "vrIpTunnelSepPathMtu": vrIpTunnelSepPathMtu,
       "vrIpTunnelStateTable": vrIpTunnelStateTable,
       "vrIpTunnelStateEntry": vrIpTunnelStateEntry,
       "vrIpTunnelAdminState": vrIpTunnelAdminState,
       "vrIpTunnelOperationalState": vrIpTunnelOperationalState,
       "vrIpTunnelUsageState": vrIpTunnelUsageState,
       "vrIpMcast": vrIpMcast,
       "vrIpMcastRowStatusTable": vrIpMcastRowStatusTable,
       "vrIpMcastRowStatusEntry": vrIpMcastRowStatusEntry,
       "vrIpMcastRowStatus": vrIpMcastRowStatus,
       "vrIpMcastComponentName": vrIpMcastComponentName,
       "vrIpMcastStorageType": vrIpMcastStorageType,
       "vrIpMcastIndex": vrIpMcastIndex,
       "vrIpMcastIgmp": vrIpMcastIgmp,
       "vrIpMcastIgmpRowStatusTable": vrIpMcastIgmpRowStatusTable,
       "vrIpMcastIgmpRowStatusEntry": vrIpMcastIgmpRowStatusEntry,
       "vrIpMcastIgmpRowStatus": vrIpMcastIgmpRowStatus,
       "vrIpMcastIgmpComponentName": vrIpMcastIgmpComponentName,
       "vrIpMcastIgmpStorageType": vrIpMcastIgmpStorageType,
       "vrIpMcastIgmpIndex": vrIpMcastIgmpIndex,
       "vrIpMcastIgmpGc": vrIpMcastIgmpGc,
       "vrIpMcastIgmpGcRowStatusTable": vrIpMcastIgmpGcRowStatusTable,
       "vrIpMcastIgmpGcRowStatusEntry": vrIpMcastIgmpGcRowStatusEntry,
       "vrIpMcastIgmpGcRowStatus": vrIpMcastIgmpGcRowStatus,
       "vrIpMcastIgmpGcComponentName": vrIpMcastIgmpGcComponentName,
       "vrIpMcastIgmpGcStorageType": vrIpMcastIgmpGcStorageType,
       "vrIpMcastIgmpGcGAddrIndex": vrIpMcastIgmpGcGAddrIndex,
       "vrIpMcastIgmpGcDomainIndex": vrIpMcastIgmpGcDomainIndex,
       "vrIpMcastIgmpGcProtocolportStringIndex": vrIpMcastIgmpGcProtocolportStringIndex,
       "vrIpMcastIgmpGcOperTable": vrIpMcastIgmpGcOperTable,
       "vrIpMcastIgmpGcOperEntry": vrIpMcastIgmpGcOperEntry,
       "vrIpMcastIgmpGcUpTime": vrIpMcastIgmpGcUpTime,
       "vrIpMcastIgmpGcExpiryTime": vrIpMcastIgmpGcExpiryTime,
       "vrIpMcastIgmpGcLastReporter": vrIpMcastIgmpGcLastReporter,
       "vrIpMcastIgmpGcVersion1HostTimer": vrIpMcastIgmpGcVersion1HostTimer,
       "vrIpMcastIgmpAdminControlTable": vrIpMcastIgmpAdminControlTable,
       "vrIpMcastIgmpAdminControlEntry": vrIpMcastIgmpAdminControlEntry,
       "vrIpMcastIgmpSnmpAdminStatus": vrIpMcastIgmpSnmpAdminStatus,
       "vrIpMcastIgmpStateTable": vrIpMcastIgmpStateTable,
       "vrIpMcastIgmpStateEntry": vrIpMcastIgmpStateEntry,
       "vrIpMcastIgmpAdminState": vrIpMcastIgmpAdminState,
       "vrIpMcastIgmpOperationalState": vrIpMcastIgmpOperationalState,
       "vrIpMcastIgmpUsageState": vrIpMcastIgmpUsageState,
       "vrIpMcastIgmpOperStatusTable": vrIpMcastIgmpOperStatusTable,
       "vrIpMcastIgmpOperStatusEntry": vrIpMcastIgmpOperStatusEntry,
       "vrIpMcastIgmpSnmpOperStatus": vrIpMcastIgmpSnmpOperStatus,
       "vrIpMcastStatic": vrIpMcastStatic,
       "vrIpMcastStaticRowStatusTable": vrIpMcastStaticRowStatusTable,
       "vrIpMcastStaticRowStatusEntry": vrIpMcastStaticRowStatusEntry,
       "vrIpMcastStaticRowStatus": vrIpMcastStaticRowStatus,
       "vrIpMcastStaticComponentName": vrIpMcastStaticComponentName,
       "vrIpMcastStaticStorageType": vrIpMcastStaticStorageType,
       "vrIpMcastStaticIndex": vrIpMcastStaticIndex,
       "vrIpMcastStaticRoute": vrIpMcastStaticRoute,
       "vrIpMcastStaticRouteRowStatusTable": vrIpMcastStaticRouteRowStatusTable,
       "vrIpMcastStaticRouteRowStatusEntry": vrIpMcastStaticRouteRowStatusEntry,
       "vrIpMcastStaticRouteRowStatus": vrIpMcastStaticRouteRowStatus,
       "vrIpMcastStaticRouteComponentName": vrIpMcastStaticRouteComponentName,
       "vrIpMcastStaticRouteStorageType": vrIpMcastStaticRouteStorageType,
       "vrIpMcastStaticRouteGAddrIndex": vrIpMcastStaticRouteGAddrIndex,
       "vrIpMcastStaticRouteDomainIndex": vrIpMcastStaticRouteDomainIndex,
       "vrIpMcastStaticRouteOifsTable": vrIpMcastStaticRouteOifsTable,
       "vrIpMcastStaticRouteOifsEntry": vrIpMcastStaticRouteOifsEntry,
       "vrIpMcastStaticRouteOifsValue": vrIpMcastStaticRouteOifsValue,
       "vrIpMcastStaticRouteOifsRowStatus": vrIpMcastStaticRouteOifsRowStatus,
       "vrIpMcastStaticStateTable": vrIpMcastStaticStateTable,
       "vrIpMcastStaticStateEntry": vrIpMcastStaticStateEntry,
       "vrIpMcastStaticAdminState": vrIpMcastStaticAdminState,
       "vrIpMcastStaticOperationalState": vrIpMcastStaticOperationalState,
       "vrIpMcastStaticUsageState": vrIpMcastStaticUsageState,
       "vrIpMcastPg": vrIpMcastPg,
       "vrIpMcastPgRowStatusTable": vrIpMcastPgRowStatusTable,
       "vrIpMcastPgRowStatusEntry": vrIpMcastPgRowStatusEntry,
       "vrIpMcastPgRowStatus": vrIpMcastPgRowStatus,
       "vrIpMcastPgComponentName": vrIpMcastPgComponentName,
       "vrIpMcastPgStorageType": vrIpMcastPgStorageType,
       "vrIpMcastPgIndex": vrIpMcastPgIndex,
       "vrIpMcastPgGrp": vrIpMcastPgGrp,
       "vrIpMcastPgGrpRowStatusTable": vrIpMcastPgGrpRowStatusTable,
       "vrIpMcastPgGrpRowStatusEntry": vrIpMcastPgGrpRowStatusEntry,
       "vrIpMcastPgGrpRowStatus": vrIpMcastPgGrpRowStatus,
       "vrIpMcastPgGrpComponentName": vrIpMcastPgGrpComponentName,
       "vrIpMcastPgGrpStorageType": vrIpMcastPgGrpStorageType,
       "vrIpMcastPgGrpGAddrIndex": vrIpMcastPgGrpGAddrIndex,
       "vrIpMcastPgGrpGMaskIndex": vrIpMcastPgGrpGMaskIndex,
       "vrIpMcastPgProvTable": vrIpMcastPgProvTable,
       "vrIpMcastPgProvEntry": vrIpMcastPgProvEntry,
       "vrIpMcastPgAction": vrIpMcastPgAction,
       "vrIpMcastPgLinkToPolicyUserTable": vrIpMcastPgLinkToPolicyUserTable,
       "vrIpMcastPgLinkToPolicyUserEntry": vrIpMcastPgLinkToPolicyUserEntry,
       "vrIpMcastPgLinkToPolicyUserValue": vrIpMcastPgLinkToPolicyUserValue,
       "vrIpMcastPgLinkToPolicyUserRowStatus": vrIpMcastPgLinkToPolicyUserRowStatus,
       "vrIpMcastDomain": vrIpMcastDomain,
       "vrIpMcastDomainRowStatusTable": vrIpMcastDomainRowStatusTable,
       "vrIpMcastDomainRowStatusEntry": vrIpMcastDomainRowStatusEntry,
       "vrIpMcastDomainRowStatus": vrIpMcastDomainRowStatus,
       "vrIpMcastDomainComponentName": vrIpMcastDomainComponentName,
       "vrIpMcastDomainStorageType": vrIpMcastDomainStorageType,
       "vrIpMcastDomainIndex": vrIpMcastDomainIndex,
       "vrIpMcastDomainOperTable": vrIpMcastDomainOperTable,
       "vrIpMcastDomainOperEntry": vrIpMcastDomainOperEntry,
       "vrIpMcastDomainProtocolActive": vrIpMcastDomainProtocolActive,
       "vrIpMcastFwd": vrIpMcastFwd,
       "vrIpMcastFwdRowStatusTable": vrIpMcastFwdRowStatusTable,
       "vrIpMcastFwdRowStatusEntry": vrIpMcastFwdRowStatusEntry,
       "vrIpMcastFwdRowStatus": vrIpMcastFwdRowStatus,
       "vrIpMcastFwdComponentName": vrIpMcastFwdComponentName,
       "vrIpMcastFwdStorageType": vrIpMcastFwdStorageType,
       "vrIpMcastFwdGAddrIndex": vrIpMcastFwdGAddrIndex,
       "vrIpMcastFwdDomainIndex": vrIpMcastFwdDomainIndex,
       "vrIpMcastFwdSrcAddrIndex": vrIpMcastFwdSrcAddrIndex,
       "vrIpMcastFwdSrcMaskIndex": vrIpMcastFwdSrcMaskIndex,
       "vrIpMcastFwdOif": vrIpMcastFwdOif,
       "vrIpMcastFwdOifRowStatusTable": vrIpMcastFwdOifRowStatusTable,
       "vrIpMcastFwdOifRowStatusEntry": vrIpMcastFwdOifRowStatusEntry,
       "vrIpMcastFwdOifRowStatus": vrIpMcastFwdOifRowStatus,
       "vrIpMcastFwdOifComponentName": vrIpMcastFwdOifComponentName,
       "vrIpMcastFwdOifStorageType": vrIpMcastFwdOifStorageType,
       "vrIpMcastFwdOifOutIfAddressIndex": vrIpMcastFwdOifOutIfAddressIndex,
       "vrIpMcastFwdOifConnectionIndex": vrIpMcastFwdOifConnectionIndex,
       "vrIpMcastFwdOifOperTable": vrIpMcastFwdOifOperTable,
       "vrIpMcastFwdOifOperEntry": vrIpMcastFwdOifOperEntry,
       "vrIpMcastFwdOifIfIndex": vrIpMcastFwdOifIfIndex,
       "vrIpMcastFwdOifProtocol": vrIpMcastFwdOifProtocol,
       "vrIpMcastFwdOifAge": vrIpMcastFwdOifAge,
       "vrIpMcastFwdOifOutProtocolPortName": vrIpMcastFwdOifOutProtocolPortName,
       "vrIpMcastFwdOperTable": vrIpMcastFwdOperTable,
       "vrIpMcastFwdOperEntry": vrIpMcastFwdOperEntry,
       "vrIpMcastFwdAge": vrIpMcastFwdAge,
       "vrIpMcastFwdInProtocolPortName": vrIpMcastFwdInProtocolPortName,
       "vrIpMcastFwdProtocol": vrIpMcastFwdProtocol,
       "vrIpMcastFwdReversePathForwardingNeighbor": vrIpMcastFwdReversePathForwardingNeighbor,
       "vrIpMcastFwdFlags": vrIpMcastFwdFlags,
       "vrIpMcastCacheStats": vrIpMcastCacheStats,
       "vrIpMcastCacheStatsRowStatusTable": vrIpMcastCacheStatsRowStatusTable,
       "vrIpMcastCacheStatsRowStatusEntry": vrIpMcastCacheStatsRowStatusEntry,
       "vrIpMcastCacheStatsRowStatus": vrIpMcastCacheStatsRowStatus,
       "vrIpMcastCacheStatsComponentName": vrIpMcastCacheStatsComponentName,
       "vrIpMcastCacheStatsStorageType": vrIpMcastCacheStatsStorageType,
       "vrIpMcastCacheStatsIndex": vrIpMcastCacheStatsIndex,
       "vrIpMcastCacheStatsStateTable": vrIpMcastCacheStatsStateTable,
       "vrIpMcastCacheStatsStateEntry": vrIpMcastCacheStatsStateEntry,
       "vrIpMcastCacheStatsAdminState": vrIpMcastCacheStatsAdminState,
       "vrIpMcastCacheStatsOperationalState": vrIpMcastCacheStatsOperationalState,
       "vrIpMcastCacheStatsUsageState": vrIpMcastCacheStatsUsageState,
       "vrIpMcastCacheStatsOperTable": vrIpMcastCacheStatsOperTable,
       "vrIpMcastCacheStatsOperEntry": vrIpMcastCacheStatsOperEntry,
       "vrIpMcastCacheStatsEntriesFree": vrIpMcastCacheStatsEntriesFree,
       "vrIpMcastCacheStatsTotalLookups": vrIpMcastCacheStatsTotalLookups,
       "vrIpMcastCacheStatsLookupMisses": vrIpMcastCacheStatsLookupMisses,
       "vrIpMcastCacheStatsCacheTableMaxEntries": vrIpMcastCacheStatsCacheTableMaxEntries,
       "vrIpMcastPimSm": vrIpMcastPimSm,
       "vrIpMcastPimSmRowStatusTable": vrIpMcastPimSmRowStatusTable,
       "vrIpMcastPimSmRowStatusEntry": vrIpMcastPimSmRowStatusEntry,
       "vrIpMcastPimSmRowStatus": vrIpMcastPimSmRowStatus,
       "vrIpMcastPimSmComponentName": vrIpMcastPimSmComponentName,
       "vrIpMcastPimSmStorageType": vrIpMcastPimSmStorageType,
       "vrIpMcastPimSmIndex": vrIpMcastPimSmIndex,
       "vrIpMcastPimSmDomain": vrIpMcastPimSmDomain,
       "vrIpMcastPimSmDomainRowStatusTable": vrIpMcastPimSmDomainRowStatusTable,
       "vrIpMcastPimSmDomainRowStatusEntry": vrIpMcastPimSmDomainRowStatusEntry,
       "vrIpMcastPimSmDomainRowStatus": vrIpMcastPimSmDomainRowStatus,
       "vrIpMcastPimSmDomainComponentName": vrIpMcastPimSmDomainComponentName,
       "vrIpMcastPimSmDomainStorageType": vrIpMcastPimSmDomainStorageType,
       "vrIpMcastPimSmDomainIndex": vrIpMcastPimSmDomainIndex,
       "vrIpMcastPimSmDomainCRp": vrIpMcastPimSmDomainCRp,
       "vrIpMcastPimSmDomainCRpRowStatusTable": vrIpMcastPimSmDomainCRpRowStatusTable,
       "vrIpMcastPimSmDomainCRpRowStatusEntry": vrIpMcastPimSmDomainCRpRowStatusEntry,
       "vrIpMcastPimSmDomainCRpRowStatus": vrIpMcastPimSmDomainCRpRowStatus,
       "vrIpMcastPimSmDomainCRpComponentName": vrIpMcastPimSmDomainCRpComponentName,
       "vrIpMcastPimSmDomainCRpStorageType": vrIpMcastPimSmDomainCRpStorageType,
       "vrIpMcastPimSmDomainCRpIndex": vrIpMcastPimSmDomainCRpIndex,
       "vrIpMcastPimSmDomainCRpGrp": vrIpMcastPimSmDomainCRpGrp,
       "vrIpMcastPimSmDomainCRpGrpRowStatusTable": vrIpMcastPimSmDomainCRpGrpRowStatusTable,
       "vrIpMcastPimSmDomainCRpGrpRowStatusEntry": vrIpMcastPimSmDomainCRpGrpRowStatusEntry,
       "vrIpMcastPimSmDomainCRpGrpRowStatus": vrIpMcastPimSmDomainCRpGrpRowStatus,
       "vrIpMcastPimSmDomainCRpGrpComponentName": vrIpMcastPimSmDomainCRpGrpComponentName,
       "vrIpMcastPimSmDomainCRpGrpStorageType": vrIpMcastPimSmDomainCRpGrpStorageType,
       "vrIpMcastPimSmDomainCRpGrpGrpAddressIndex": vrIpMcastPimSmDomainCRpGrpGrpAddressIndex,
       "vrIpMcastPimSmDomainCRpGrpGrpMaskIndex": vrIpMcastPimSmDomainCRpGrpGrpMaskIndex,
       "vrIpMcastPimSmDomainCRpProvTable": vrIpMcastPimSmDomainCRpProvTable,
       "vrIpMcastPimSmDomainCRpProvEntry": vrIpMcastPimSmDomainCRpProvEntry,
       "vrIpMcastPimSmDomainCRpCandidateRpAddress": vrIpMcastPimSmDomainCRpCandidateRpAddress,
       "vrIpMcastPimSmDomainCRpCandidateRpPreference": vrIpMcastPimSmDomainCRpCandidateRpPreference,
       "vrIpMcastPimSmDomainRpSet": vrIpMcastPimSmDomainRpSet,
       "vrIpMcastPimSmDomainRpSetRowStatusTable": vrIpMcastPimSmDomainRpSetRowStatusTable,
       "vrIpMcastPimSmDomainRpSetRowStatusEntry": vrIpMcastPimSmDomainRpSetRowStatusEntry,
       "vrIpMcastPimSmDomainRpSetRowStatus": vrIpMcastPimSmDomainRpSetRowStatus,
       "vrIpMcastPimSmDomainRpSetComponentName": vrIpMcastPimSmDomainRpSetComponentName,
       "vrIpMcastPimSmDomainRpSetStorageType": vrIpMcastPimSmDomainRpSetStorageType,
       "vrIpMcastPimSmDomainRpSetGrpAddressIndex": vrIpMcastPimSmDomainRpSetGrpAddressIndex,
       "vrIpMcastPimSmDomainRpSetGrpMaskIndex": vrIpMcastPimSmDomainRpSetGrpMaskIndex,
       "vrIpMcastPimSmDomainRpSetRpAddressIndex": vrIpMcastPimSmDomainRpSetRpAddressIndex,
       "vrIpMcastPimSmDomainRpSetOperTable": vrIpMcastPimSmDomainRpSetOperTable,
       "vrIpMcastPimSmDomainRpSetOperEntry": vrIpMcastPimSmDomainRpSetOperEntry,
       "vrIpMcastPimSmDomainRpSetRpSetHoldTime": vrIpMcastPimSmDomainRpSetRpSetHoldTime,
       "vrIpMcastPimSmDomainRpSetRpSetExpiryTime": vrIpMcastPimSmDomainRpSetRpSetExpiryTime,
       "vrIpMcastPimSmDomainRpSetRpSetPriority": vrIpMcastPimSmDomainRpSetRpSetPriority,
       "vrIpMcastPimSmDomainCBsr": vrIpMcastPimSmDomainCBsr,
       "vrIpMcastPimSmDomainCBsrRowStatusTable": vrIpMcastPimSmDomainCBsrRowStatusTable,
       "vrIpMcastPimSmDomainCBsrRowStatusEntry": vrIpMcastPimSmDomainCBsrRowStatusEntry,
       "vrIpMcastPimSmDomainCBsrRowStatus": vrIpMcastPimSmDomainCBsrRowStatus,
       "vrIpMcastPimSmDomainCBsrComponentName": vrIpMcastPimSmDomainCBsrComponentName,
       "vrIpMcastPimSmDomainCBsrStorageType": vrIpMcastPimSmDomainCBsrStorageType,
       "vrIpMcastPimSmDomainCBsrIndex": vrIpMcastPimSmDomainCBsrIndex,
       "vrIpMcastPimSmDomainCBsrProvTable": vrIpMcastPimSmDomainCBsrProvTable,
       "vrIpMcastPimSmDomainCBsrProvEntry": vrIpMcastPimSmDomainCBsrProvEntry,
       "vrIpMcastPimSmDomainCBsrCandidateBsrAddress": vrIpMcastPimSmDomainCBsrCandidateBsrAddress,
       "vrIpMcastPimSmDomainCBsrCandidateBsrPreference": vrIpMcastPimSmDomainCBsrCandidateBsrPreference,
       "vrIpMcastPimSmDomainProvTable": vrIpMcastPimSmDomainProvTable,
       "vrIpMcastPimSmDomainProvEntry": vrIpMcastPimSmDomainProvEntry,
       "vrIpMcastPimSmDomainJoinPruneInterval": vrIpMcastPimSmDomainJoinPruneInterval,
       "vrIpMcastPimSmDomainSptJoinThreshold": vrIpMcastPimSmDomainSptJoinThreshold,
       "vrIpMcastPimSmDomainOperTable": vrIpMcastPimSmDomainOperTable,
       "vrIpMcastPimSmDomainOperEntry": vrIpMcastPimSmDomainOperEntry,
       "vrIpMcastPimSmDomainBsrAddress": vrIpMcastPimSmDomainBsrAddress,
       "vrIpMcastPimSmDomainBsrExpiryTimer": vrIpMcastPimSmDomainBsrExpiryTimer,
       "vrIpMcastPimSmDomainStatsTable": vrIpMcastPimSmDomainStatsTable,
       "vrIpMcastPimSmDomainStatsEntry": vrIpMcastPimSmDomainStatsEntry,
       "vrIpMcastPimSmDomainTxBsrMsg": vrIpMcastPimSmDomainTxBsrMsg,
       "vrIpMcastPimSmDomainRxBsrMsg": vrIpMcastPimSmDomainRxBsrMsg,
       "vrIpMcastPimSmDomainTxCRpAdvMsg": vrIpMcastPimSmDomainTxCRpAdvMsg,
       "vrIpMcastPimSmDomainRxCRpAdvMsg": vrIpMcastPimSmDomainRxCRpAdvMsg,
       "vrIpMcastPimSmDomainTxHelloMsg": vrIpMcastPimSmDomainTxHelloMsg,
       "vrIpMcastPimSmDomainRxHelloMsg": vrIpMcastPimSmDomainRxHelloMsg,
       "vrIpMcastPimSmDomainTxRegisterMsg": vrIpMcastPimSmDomainTxRegisterMsg,
       "vrIpMcastPimSmDomainRxRegisterMsg": vrIpMcastPimSmDomainRxRegisterMsg,
       "vrIpMcastPimSmDomainTxRegisterStopMsg": vrIpMcastPimSmDomainTxRegisterStopMsg,
       "vrIpMcastPimSmDomainRxRegisterStopMsg": vrIpMcastPimSmDomainRxRegisterStopMsg,
       "vrIpMcastPimSmDomainTxAssertMsg": vrIpMcastPimSmDomainTxAssertMsg,
       "vrIpMcastPimSmDomainRxAssertMsg": vrIpMcastPimSmDomainRxAssertMsg,
       "vrIpMcastPimSmDomainTxJPMsg": vrIpMcastPimSmDomainTxJPMsg,
       "vrIpMcastPimSmDomainRxJPMsg": vrIpMcastPimSmDomainRxJPMsg,
       "vrIpMcastPimSmDomainDiscardBsrMsg": vrIpMcastPimSmDomainDiscardBsrMsg,
       "vrIpMcastPimSmDomainDiscardCRpAdvMsg": vrIpMcastPimSmDomainDiscardCRpAdvMsg,
       "vrIpMcastPimSmDomainDiscardHelloMsg": vrIpMcastPimSmDomainDiscardHelloMsg,
       "vrIpMcastPimSmDomainDiscardRegisterMsg": vrIpMcastPimSmDomainDiscardRegisterMsg,
       "vrIpMcastPimSmDomainDiscardRegisterStopMsg": vrIpMcastPimSmDomainDiscardRegisterStopMsg,
       "vrIpMcastPimSmDomainDiscardAssertMsg": vrIpMcastPimSmDomainDiscardAssertMsg,
       "vrIpMcastPimSmDomainDiscardJPMsg": vrIpMcastPimSmDomainDiscardJPMsg,
       "vrIpMcastPimSmAdminControlTable": vrIpMcastPimSmAdminControlTable,
       "vrIpMcastPimSmAdminControlEntry": vrIpMcastPimSmAdminControlEntry,
       "vrIpMcastPimSmSnmpAdminStatus": vrIpMcastPimSmSnmpAdminStatus,
       "vrIpMcastPimSmStateTable": vrIpMcastPimSmStateTable,
       "vrIpMcastPimSmStateEntry": vrIpMcastPimSmStateEntry,
       "vrIpMcastPimSmAdminState": vrIpMcastPimSmAdminState,
       "vrIpMcastPimSmOperationalState": vrIpMcastPimSmOperationalState,
       "vrIpMcastPimSmUsageState": vrIpMcastPimSmUsageState,
       "vrIpMcastPimSmOperStatusTable": vrIpMcastPimSmOperStatusTable,
       "vrIpMcastPimSmOperStatusEntry": vrIpMcastPimSmOperStatusEntry,
       "vrIpMcastPimSmSnmpOperStatus": vrIpMcastPimSmSnmpOperStatus,
       "vrIpMcastPimNbr": vrIpMcastPimNbr,
       "vrIpMcastPimNbrRowStatusTable": vrIpMcastPimNbrRowStatusTable,
       "vrIpMcastPimNbrRowStatusEntry": vrIpMcastPimNbrRowStatusEntry,
       "vrIpMcastPimNbrRowStatus": vrIpMcastPimNbrRowStatus,
       "vrIpMcastPimNbrComponentName": vrIpMcastPimNbrComponentName,
       "vrIpMcastPimNbrStorageType": vrIpMcastPimNbrStorageType,
       "vrIpMcastPimNbrNbrAddressIndex": vrIpMcastPimNbrNbrAddressIndex,
       "vrIpMcastPimNbrDomainIndex": vrIpMcastPimNbrDomainIndex,
       "vrIpMcastPimNbrOperTable": vrIpMcastPimNbrOperTable,
       "vrIpMcastPimNbrOperEntry": vrIpMcastPimNbrOperEntry,
       "vrIpMcastPimNbrIfIndex": vrIpMcastPimNbrIfIndex,
       "vrIpMcastPimNbrUpTime": vrIpMcastPimNbrUpTime,
       "vrIpMcastPimNbrExpiryTimer": vrIpMcastPimNbrExpiryTimer,
       "vrIpMcastAdminControlTable": vrIpMcastAdminControlTable,
       "vrIpMcastAdminControlEntry": vrIpMcastAdminControlEntry,
       "vrIpMcastSnmpAdminStatus": vrIpMcastSnmpAdminStatus,
       "vrIpMcastStateTable": vrIpMcastStateTable,
       "vrIpMcastStateEntry": vrIpMcastStateEntry,
       "vrIpMcastAdminState": vrIpMcastAdminState,
       "vrIpMcastOperationalState": vrIpMcastOperationalState,
       "vrIpMcastUsageState": vrIpMcastUsageState,
       "vrIpMcastOperStatusTable": vrIpMcastOperStatusTable,
       "vrIpMcastOperStatusEntry": vrIpMcastOperStatusEntry,
       "vrIpMcastSnmpOperStatus": vrIpMcastSnmpOperStatus,
       "vrIpMcastCtsTable": vrIpMcastCtsTable,
       "vrIpMcastCtsEntry": vrIpMcastCtsEntry,
       "vrIpMcastCtsIndex": vrIpMcastCtsIndex,
       "vrIpMcastCtsValue": vrIpMcastCtsValue,
       "vrIpProvTable": vrIpProvTable,
       "vrIpProvEntry": vrIpProvEntry,
       "vrIpForwarding": vrIpForwarding,
       "vrIpDefaultTtl": vrIpDefaultTtl,
       "vrIpCosPolicyAssignment": vrIpCosPolicyAssignment,
       "vrIpStatsTable": vrIpStatsTable,
       "vrIpStatsEntry": vrIpStatsEntry,
       "vrIpInReceives": vrIpInReceives,
       "vrIpInHdrErrors": vrIpInHdrErrors,
       "vrIpInAddrErrors": vrIpInAddrErrors,
       "vrIpForwDatagrams": vrIpForwDatagrams,
       "vrIpInUnknownProtos": vrIpInUnknownProtos,
       "vrIpInDiscards": vrIpInDiscards,
       "vrIpInDelivers": vrIpInDelivers,
       "vrIpOutRequests": vrIpOutRequests,
       "vrIpOutDiscards": vrIpOutDiscards,
       "vrIpOutNoRoutes": vrIpOutNoRoutes,
       "vrIpReasmTimeOut": vrIpReasmTimeOut,
       "vrIpReasmReqds": vrIpReasmReqds,
       "vrIpReasmOks": vrIpReasmOks,
       "vrIpReasmFails": vrIpReasmFails,
       "vrIpFragOks": vrIpFragOks,
       "vrIpFragFails": vrIpFragFails,
       "vrIpFragCreates": vrIpFragCreates,
       "vrIpRoutingDiscards": vrIpRoutingDiscards,
       "vrIpAdminControlTable": vrIpAdminControlTable,
       "vrIpAdminControlEntry": vrIpAdminControlEntry,
       "vrIpSnmpAdminStatus": vrIpSnmpAdminStatus,
       "vrIpStateTable": vrIpStateTable,
       "vrIpStateEntry": vrIpStateEntry,
       "vrIpAdminState": vrIpAdminState,
       "vrIpOperationalState": vrIpOperationalState,
       "vrIpUsageState": vrIpUsageState,
       "vrIpOperStatusTable": vrIpOperStatusTable,
       "vrIpOperStatusEntry": vrIpOperStatusEntry,
       "vrIpSnmpOperStatus": vrIpSnmpOperStatus,
       "vrIpCtsTable": vrIpCtsTable,
       "vrIpCtsEntry": vrIpCtsEntry,
       "vrIpCtsIndex": vrIpCtsIndex,
       "vrIpCtsValue": vrIpCtsValue,
       "ipMIB": ipMIB,
       "ipGroup": ipGroup,
       "ipGroupBE": ipGroupBE,
       "ipGroupBE01": ipGroupBE01,
       "ipGroupBE01A": ipGroupBE01A,
       "ipCapabilities": ipCapabilities,
       "ipCapabilitiesBE": ipCapabilitiesBE,
       "ipCapabilitiesBE01": ipCapabilitiesBE01,
       "ipCapabilitiesBE01A": ipCapabilitiesBE01A}
)
