# SNMP MIB module (Nortel-Magellan-Passport-VirtualRouterMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-VirtualRouterMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:25 2024
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
 InterfaceIndex,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "InterfaceIndex",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 AsciiStringIndex,
 HexString,
 IntegerSequence,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
    "HexString",
    "IntegerSequence",
    "Link",
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

_Vr_ObjectIdentity = ObjectIdentity
vr = _Vr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100)
)
_VrRowStatusTable_Object = MibTable
vrRowStatusTable = _VrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 1)
)
if mibBuilder.loadTexts:
    vrRowStatusTable.setStatus("mandatory")
_VrRowStatusEntry_Object = MibTableRow
vrRowStatusEntry = _VrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 1, 1)
)
vrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
)
if mibBuilder.loadTexts:
    vrRowStatusEntry.setStatus("mandatory")
_VrRowStatus_Type = RowStatus
_VrRowStatus_Object = MibTableColumn
vrRowStatus = _VrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 1, 1, 1),
    _VrRowStatus_Type()
)
vrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrRowStatus.setStatus("mandatory")
_VrComponentName_Type = DisplayString
_VrComponentName_Object = MibTableColumn
vrComponentName = _VrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 1, 1, 2),
    _VrComponentName_Type()
)
vrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrComponentName.setStatus("mandatory")
_VrStorageType_Type = StorageType
_VrStorageType_Object = MibTableColumn
vrStorageType = _VrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 1, 1, 4),
    _VrStorageType_Type()
)
vrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrStorageType.setStatus("mandatory")


class _VrIndex_Type(AsciiStringIndex):
    """Custom type vrIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_VrIndex_Type.__name__ = "AsciiStringIndex"
_VrIndex_Object = MibTableColumn
vrIndex = _VrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 1, 1, 10),
    _VrIndex_Type()
)
vrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIndex.setStatus("mandatory")
_VrMm_ObjectIdentity = ObjectIdentity
vrMm = _VrMm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2)
)
_VrMmRowStatusTable_Object = MibTable
vrMmRowStatusTable = _VrMmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 1)
)
if mibBuilder.loadTexts:
    vrMmRowStatusTable.setStatus("mandatory")
_VrMmRowStatusEntry_Object = MibTableRow
vrMmRowStatusEntry = _VrMmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 1, 1)
)
vrMmRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrMmIndex"),
)
if mibBuilder.loadTexts:
    vrMmRowStatusEntry.setStatus("mandatory")
_VrMmRowStatus_Type = RowStatus
_VrMmRowStatus_Object = MibTableColumn
vrMmRowStatus = _VrMmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 1, 1, 1),
    _VrMmRowStatus_Type()
)
vrMmRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrMmRowStatus.setStatus("mandatory")
_VrMmComponentName_Type = DisplayString
_VrMmComponentName_Object = MibTableColumn
vrMmComponentName = _VrMmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 1, 1, 2),
    _VrMmComponentName_Type()
)
vrMmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrMmComponentName.setStatus("mandatory")
_VrMmStorageType_Type = StorageType
_VrMmStorageType_Object = MibTableColumn
vrMmStorageType = _VrMmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 1, 1, 4),
    _VrMmStorageType_Type()
)
vrMmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrMmStorageType.setStatus("mandatory")
_VrMmIndex_Type = NonReplicated
_VrMmIndex_Object = MibTableColumn
vrMmIndex = _VrMmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 1, 1, 10),
    _VrMmIndex_Type()
)
vrMmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrMmIndex.setStatus("mandatory")
_VrMmProvTable_Object = MibTable
vrMmProvTable = _VrMmProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 10)
)
if mibBuilder.loadTexts:
    vrMmProvTable.setStatus("mandatory")
_VrMmProvEntry_Object = MibTableRow
vrMmProvEntry = _VrMmProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 10, 1)
)
vrMmProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrMmIndex"),
)
if mibBuilder.loadTexts:
    vrMmProvEntry.setStatus("mandatory")


class _VrMmVrMaxHeapSpace_Type(Unsigned32):
    """Custom type vrMmVrMaxHeapSpace based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrMmVrMaxHeapSpace_Type.__name__ = "Unsigned32"
_VrMmVrMaxHeapSpace_Object = MibTableColumn
vrMmVrMaxHeapSpace = _VrMmVrMaxHeapSpace_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 10, 1, 1),
    _VrMmVrMaxHeapSpace_Type()
)
vrMmVrMaxHeapSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrMmVrMaxHeapSpace.setStatus("mandatory")


class _VrMmIpMaxHeapSpace_Type(Unsigned32):
    """Custom type vrMmIpMaxHeapSpace based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrMmIpMaxHeapSpace_Type.__name__ = "Unsigned32"
_VrMmIpMaxHeapSpace_Object = MibTableColumn
vrMmIpMaxHeapSpace = _VrMmIpMaxHeapSpace_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 10, 1, 2),
    _VrMmIpMaxHeapSpace_Type()
)
vrMmIpMaxHeapSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrMmIpMaxHeapSpace.setStatus("mandatory")


class _VrMmIpxMaxHeapSpace_Type(Unsigned32):
    """Custom type vrMmIpxMaxHeapSpace based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrMmIpxMaxHeapSpace_Type.__name__ = "Unsigned32"
_VrMmIpxMaxHeapSpace_Object = MibTableColumn
vrMmIpxMaxHeapSpace = _VrMmIpxMaxHeapSpace_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 10, 1, 3),
    _VrMmIpxMaxHeapSpace_Type()
)
vrMmIpxMaxHeapSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrMmIpxMaxHeapSpace.setStatus("mandatory")


class _VrMmBridgingMaxHeapSpace_Type(Unsigned32):
    """Custom type vrMmBridgingMaxHeapSpace based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrMmBridgingMaxHeapSpace_Type.__name__ = "Unsigned32"
_VrMmBridgingMaxHeapSpace_Object = MibTableColumn
vrMmBridgingMaxHeapSpace = _VrMmBridgingMaxHeapSpace_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 10, 1, 6),
    _VrMmBridgingMaxHeapSpace_Type()
)
vrMmBridgingMaxHeapSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrMmBridgingMaxHeapSpace.setStatus("mandatory")


class _VrMmNetSentryMaxHeapSpace_Type(Unsigned32):
    """Custom type vrMmNetSentryMaxHeapSpace based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrMmNetSentryMaxHeapSpace_Type.__name__ = "Unsigned32"
_VrMmNetSentryMaxHeapSpace_Object = MibTableColumn
vrMmNetSentryMaxHeapSpace = _VrMmNetSentryMaxHeapSpace_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 10, 1, 7),
    _VrMmNetSentryMaxHeapSpace_Type()
)
vrMmNetSentryMaxHeapSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrMmNetSentryMaxHeapSpace.setStatus("mandatory")


class _VrMmSresMaxHeapSpace_Type(Unsigned32):
    """Custom type vrMmSresMaxHeapSpace based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrMmSresMaxHeapSpace_Type.__name__ = "Unsigned32"
_VrMmSresMaxHeapSpace_Object = MibTableColumn
vrMmSresMaxHeapSpace = _VrMmSresMaxHeapSpace_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 10, 1, 8),
    _VrMmSresMaxHeapSpace_Type()
)
vrMmSresMaxHeapSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrMmSresMaxHeapSpace.setStatus("mandatory")


class _VrMmSnaMaxHeapSpace_Type(Unsigned32):
    """Custom type vrMmSnaMaxHeapSpace based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrMmSnaMaxHeapSpace_Type.__name__ = "Unsigned32"
_VrMmSnaMaxHeapSpace_Object = MibTableColumn
vrMmSnaMaxHeapSpace = _VrMmSnaMaxHeapSpace_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 10, 1, 9),
    _VrMmSnaMaxHeapSpace_Type()
)
vrMmSnaMaxHeapSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrMmSnaMaxHeapSpace.setStatus("mandatory")
_VrMmOperTable_Object = MibTable
vrMmOperTable = _VrMmOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 11)
)
if mibBuilder.loadTexts:
    vrMmOperTable.setStatus("mandatory")
_VrMmOperEntry_Object = MibTableRow
vrMmOperEntry = _VrMmOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 11, 1)
)
vrMmOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrMmIndex"),
)
if mibBuilder.loadTexts:
    vrMmOperEntry.setStatus("mandatory")


class _VrMmVrHeapSpaceBytesAllocated_Type(Unsigned32):
    """Custom type vrMmVrHeapSpaceBytesAllocated based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrMmVrHeapSpaceBytesAllocated_Type.__name__ = "Unsigned32"
_VrMmVrHeapSpaceBytesAllocated_Object = MibTableColumn
vrMmVrHeapSpaceBytesAllocated = _VrMmVrHeapSpaceBytesAllocated_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 11, 1, 1),
    _VrMmVrHeapSpaceBytesAllocated_Type()
)
vrMmVrHeapSpaceBytesAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrMmVrHeapSpaceBytesAllocated.setStatus("mandatory")


class _VrMmVrHeapSpaceAllocated_Type(Unsigned32):
    """Custom type vrMmVrHeapSpaceAllocated based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrMmVrHeapSpaceAllocated_Type.__name__ = "Unsigned32"
_VrMmVrHeapSpaceAllocated_Object = MibTableColumn
vrMmVrHeapSpaceAllocated = _VrMmVrHeapSpaceAllocated_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 11, 1, 2),
    _VrMmVrHeapSpaceAllocated_Type()
)
vrMmVrHeapSpaceAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrMmVrHeapSpaceAllocated.setStatus("mandatory")


class _VrMmIpHeapSpaceAllocated_Type(Unsigned32):
    """Custom type vrMmIpHeapSpaceAllocated based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrMmIpHeapSpaceAllocated_Type.__name__ = "Unsigned32"
_VrMmIpHeapSpaceAllocated_Object = MibTableColumn
vrMmIpHeapSpaceAllocated = _VrMmIpHeapSpaceAllocated_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 11, 1, 3),
    _VrMmIpHeapSpaceAllocated_Type()
)
vrMmIpHeapSpaceAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrMmIpHeapSpaceAllocated.setStatus("mandatory")


class _VrMmIpxHeapSpaceAllocated_Type(Unsigned32):
    """Custom type vrMmIpxHeapSpaceAllocated based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrMmIpxHeapSpaceAllocated_Type.__name__ = "Unsigned32"
_VrMmIpxHeapSpaceAllocated_Object = MibTableColumn
vrMmIpxHeapSpaceAllocated = _VrMmIpxHeapSpaceAllocated_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 11, 1, 4),
    _VrMmIpxHeapSpaceAllocated_Type()
)
vrMmIpxHeapSpaceAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrMmIpxHeapSpaceAllocated.setStatus("mandatory")


class _VrMmBridgingHeapSpaceAllocated_Type(Unsigned32):
    """Custom type vrMmBridgingHeapSpaceAllocated based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrMmBridgingHeapSpaceAllocated_Type.__name__ = "Unsigned32"
_VrMmBridgingHeapSpaceAllocated_Object = MibTableColumn
vrMmBridgingHeapSpaceAllocated = _VrMmBridgingHeapSpaceAllocated_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 11, 1, 7),
    _VrMmBridgingHeapSpaceAllocated_Type()
)
vrMmBridgingHeapSpaceAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrMmBridgingHeapSpaceAllocated.setStatus("mandatory")


class _VrMmNetSentryHeapSpaceAllocated_Type(Unsigned32):
    """Custom type vrMmNetSentryHeapSpaceAllocated based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrMmNetSentryHeapSpaceAllocated_Type.__name__ = "Unsigned32"
_VrMmNetSentryHeapSpaceAllocated_Object = MibTableColumn
vrMmNetSentryHeapSpaceAllocated = _VrMmNetSentryHeapSpaceAllocated_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 11, 1, 8),
    _VrMmNetSentryHeapSpaceAllocated_Type()
)
vrMmNetSentryHeapSpaceAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrMmNetSentryHeapSpaceAllocated.setStatus("mandatory")


class _VrMmSresHeapSpaceAllocated_Type(Unsigned32):
    """Custom type vrMmSresHeapSpaceAllocated based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrMmSresHeapSpaceAllocated_Type.__name__ = "Unsigned32"
_VrMmSresHeapSpaceAllocated_Object = MibTableColumn
vrMmSresHeapSpaceAllocated = _VrMmSresHeapSpaceAllocated_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 11, 1, 9),
    _VrMmSresHeapSpaceAllocated_Type()
)
vrMmSresHeapSpaceAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrMmSresHeapSpaceAllocated.setStatus("mandatory")


class _VrMmSnaHeapSpaceAllocated_Type(Unsigned32):
    """Custom type vrMmSnaHeapSpaceAllocated based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VrMmSnaHeapSpaceAllocated_Type.__name__ = "Unsigned32"
_VrMmSnaHeapSpaceAllocated_Object = MibTableColumn
vrMmSnaHeapSpaceAllocated = _VrMmSnaHeapSpaceAllocated_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 11, 1, 10),
    _VrMmSnaHeapSpaceAllocated_Type()
)
vrMmSnaHeapSpaceAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrMmSnaHeapSpaceAllocated.setStatus("mandatory")
_VrPp_ObjectIdentity = ObjectIdentity
vrPp = _VrPp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3)
)
_VrPpRowStatusTable_Object = MibTable
vrPpRowStatusTable = _VrPpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 1)
)
if mibBuilder.loadTexts:
    vrPpRowStatusTable.setStatus("mandatory")
_VrPpRowStatusEntry_Object = MibTableRow
vrPpRowStatusEntry = _VrPpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 1, 1)
)
vrPpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
)
if mibBuilder.loadTexts:
    vrPpRowStatusEntry.setStatus("mandatory")
_VrPpRowStatus_Type = RowStatus
_VrPpRowStatus_Object = MibTableColumn
vrPpRowStatus = _VrPpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 1, 1, 1),
    _VrPpRowStatus_Type()
)
vrPpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpRowStatus.setStatus("mandatory")
_VrPpComponentName_Type = DisplayString
_VrPpComponentName_Object = MibTableColumn
vrPpComponentName = _VrPpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 1, 1, 2),
    _VrPpComponentName_Type()
)
vrPpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpComponentName.setStatus("mandatory")
_VrPpStorageType_Type = StorageType
_VrPpStorageType_Object = MibTableColumn
vrPpStorageType = _VrPpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 1, 1, 4),
    _VrPpStorageType_Type()
)
vrPpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpStorageType.setStatus("mandatory")


class _VrPpIndex_Type(AsciiStringIndex):
    """Custom type vrPpIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_VrPpIndex_Type.__name__ = "AsciiStringIndex"
_VrPpIndex_Object = MibTableColumn
vrPpIndex = _VrPpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 1, 1, 10),
    _VrPpIndex_Type()
)
vrPpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpIndex.setStatus("mandatory")
_VrPpAdminControlTable_Object = MibTable
vrPpAdminControlTable = _VrPpAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 100)
)
if mibBuilder.loadTexts:
    vrPpAdminControlTable.setStatus("mandatory")
_VrPpAdminControlEntry_Object = MibTableRow
vrPpAdminControlEntry = _VrPpAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 100, 1)
)
vrPpAdminControlEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
)
if mibBuilder.loadTexts:
    vrPpAdminControlEntry.setStatus("mandatory")


class _VrPpSnmpAdminStatus_Type(Integer32):
    """Custom type vrPpSnmpAdminStatus based on Integer32"""
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


_VrPpSnmpAdminStatus_Type.__name__ = "Integer32"
_VrPpSnmpAdminStatus_Object = MibTableColumn
vrPpSnmpAdminStatus = _VrPpSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 100, 1, 1),
    _VrPpSnmpAdminStatus_Type()
)
vrPpSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpSnmpAdminStatus.setStatus("mandatory")
_VrPpProvTable_Object = MibTable
vrPpProvTable = _VrPpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 101)
)
if mibBuilder.loadTexts:
    vrPpProvTable.setStatus("mandatory")
_VrPpProvEntry_Object = MibTableRow
vrPpProvEntry = _VrPpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 101, 1)
)
vrPpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
)
if mibBuilder.loadTexts:
    vrPpProvEntry.setStatus("mandatory")
_VrPpLinkToMedia_Type = Link
_VrPpLinkToMedia_Object = MibTableColumn
vrPpLinkToMedia = _VrPpLinkToMedia_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 101, 1, 1),
    _VrPpLinkToMedia_Type()
)
vrPpLinkToMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpLinkToMedia.setStatus("mandatory")
_VrPpOperStatusTable_Object = MibTable
vrPpOperStatusTable = _VrPpOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 102)
)
if mibBuilder.loadTexts:
    vrPpOperStatusTable.setStatus("mandatory")
_VrPpOperStatusEntry_Object = MibTableRow
vrPpOperStatusEntry = _VrPpOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 102, 1)
)
vrPpOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
)
if mibBuilder.loadTexts:
    vrPpOperStatusEntry.setStatus("mandatory")


class _VrPpSnmpOperStatus_Type(Integer32):
    """Custom type vrPpSnmpOperStatus based on Integer32"""
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


_VrPpSnmpOperStatus_Type.__name__ = "Integer32"
_VrPpSnmpOperStatus_Object = MibTableColumn
vrPpSnmpOperStatus = _VrPpSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 102, 1, 1),
    _VrPpSnmpOperStatus_Type()
)
vrPpSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpSnmpOperStatus.setStatus("mandatory")
_VrPpStateTable_Object = MibTable
vrPpStateTable = _VrPpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 103)
)
if mibBuilder.loadTexts:
    vrPpStateTable.setStatus("mandatory")
_VrPpStateEntry_Object = MibTableRow
vrPpStateEntry = _VrPpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 103, 1)
)
vrPpStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
)
if mibBuilder.loadTexts:
    vrPpStateEntry.setStatus("mandatory")


class _VrPpAdminState_Type(Integer32):
    """Custom type vrPpAdminState based on Integer32"""
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


_VrPpAdminState_Type.__name__ = "Integer32"
_VrPpAdminState_Object = MibTableColumn
vrPpAdminState = _VrPpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 103, 1, 1),
    _VrPpAdminState_Type()
)
vrPpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpAdminState.setStatus("mandatory")


class _VrPpOperationalState_Type(Integer32):
    """Custom type vrPpOperationalState based on Integer32"""
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


_VrPpOperationalState_Type.__name__ = "Integer32"
_VrPpOperationalState_Object = MibTableColumn
vrPpOperationalState = _VrPpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 103, 1, 2),
    _VrPpOperationalState_Type()
)
vrPpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpOperationalState.setStatus("mandatory")


class _VrPpUsageState_Type(Integer32):
    """Custom type vrPpUsageState based on Integer32"""
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


_VrPpUsageState_Type.__name__ = "Integer32"
_VrPpUsageState_Object = MibTableColumn
vrPpUsageState = _VrPpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 103, 1, 3),
    _VrPpUsageState_Type()
)
vrPpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpUsageState.setStatus("mandatory")
_VrPpOperTable_Object = MibTable
vrPpOperTable = _VrPpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 104)
)
if mibBuilder.loadTexts:
    vrPpOperTable.setStatus("mandatory")
_VrPpOperEntry_Object = MibTableRow
vrPpOperEntry = _VrPpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 104, 1)
)
vrPpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
)
if mibBuilder.loadTexts:
    vrPpOperEntry.setStatus("mandatory")


class _VrPpIfIndex_Type(InterfaceIndex):
    """Custom type vrPpIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrPpIfIndex_Type.__name__ = "InterfaceIndex"
_VrPpIfIndex_Object = MibTableColumn
vrPpIfIndex = _VrPpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 104, 1, 1),
    _VrPpIfIndex_Type()
)
vrPpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIfIndex.setStatus("mandatory")
_VrPpNbmaAddressTable_Object = MibTable
vrPpNbmaAddressTable = _VrPpNbmaAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 105)
)
if mibBuilder.loadTexts:
    vrPpNbmaAddressTable.setStatus("mandatory")
_VrPpNbmaAddressEntry_Object = MibTableRow
vrPpNbmaAddressEntry = _VrPpNbmaAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 105, 1)
)
vrPpNbmaAddressEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
)
if mibBuilder.loadTexts:
    vrPpNbmaAddressEntry.setStatus("mandatory")


class _VrPpAtmAddress_Type(HexString):
    """Custom type vrPpAtmAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_VrPpAtmAddress_Type.__name__ = "HexString"
_VrPpAtmAddress_Object = MibTableColumn
vrPpAtmAddress = _VrPpAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 105, 1, 1),
    _VrPpAtmAddress_Type()
)
vrPpAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpAtmAddress.setStatus("mandatory")
_VrIfTableEntry_ObjectIdentity = ObjectIdentity
vrIfTableEntry = _VrIfTableEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10)
)
_VrIfTableEntryRowStatusTable_Object = MibTable
vrIfTableEntryRowStatusTable = _VrIfTableEntryRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 1)
)
if mibBuilder.loadTexts:
    vrIfTableEntryRowStatusTable.setStatus("mandatory")
_VrIfTableEntryRowStatusEntry_Object = MibTableRow
vrIfTableEntryRowStatusEntry = _VrIfTableEntryRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 1, 1)
)
vrIfTableEntryRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIfTableEntryIndex"),
)
if mibBuilder.loadTexts:
    vrIfTableEntryRowStatusEntry.setStatus("mandatory")
_VrIfTableEntryRowStatus_Type = RowStatus
_VrIfTableEntryRowStatus_Object = MibTableColumn
vrIfTableEntryRowStatus = _VrIfTableEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 1, 1, 1),
    _VrIfTableEntryRowStatus_Type()
)
vrIfTableEntryRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIfTableEntryRowStatus.setStatus("mandatory")
_VrIfTableEntryComponentName_Type = DisplayString
_VrIfTableEntryComponentName_Object = MibTableColumn
vrIfTableEntryComponentName = _VrIfTableEntryComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 1, 1, 2),
    _VrIfTableEntryComponentName_Type()
)
vrIfTableEntryComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIfTableEntryComponentName.setStatus("mandatory")
_VrIfTableEntryStorageType_Type = StorageType
_VrIfTableEntryStorageType_Object = MibTableColumn
vrIfTableEntryStorageType = _VrIfTableEntryStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 1, 1, 4),
    _VrIfTableEntryStorageType_Type()
)
vrIfTableEntryStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIfTableEntryStorageType.setStatus("mandatory")


class _VrIfTableEntryIndex_Type(Integer32):
    """Custom type vrIfTableEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrIfTableEntryIndex_Type.__name__ = "Integer32"
_VrIfTableEntryIndex_Object = MibTableColumn
vrIfTableEntryIndex = _VrIfTableEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 1, 1, 10),
    _VrIfTableEntryIndex_Type()
)
vrIfTableEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIfTableEntryIndex.setStatus("mandatory")
_VrIfTableEntryIftTable_Object = MibTable
vrIfTableEntryIftTable = _VrIfTableEntryIftTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10)
)
if mibBuilder.loadTexts:
    vrIfTableEntryIftTable.setStatus("mandatory")
_VrIfTableEntryIftEntry_Object = MibTableRow
vrIfTableEntryIftEntry = _VrIfTableEntryIftEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1)
)
vrIfTableEntryIftEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIfTableEntryIndex"),
)
if mibBuilder.loadTexts:
    vrIfTableEntryIftEntry.setStatus("mandatory")


class _VrIfTableEntryIfAdminStatus_Type(Integer32):
    """Custom type vrIfTableEntryIfAdminStatus based on Integer32"""
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


_VrIfTableEntryIfAdminStatus_Type.__name__ = "Integer32"
_VrIfTableEntryIfAdminStatus_Object = MibTableColumn
vrIfTableEntryIfAdminStatus = _VrIfTableEntryIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 2),
    _VrIfTableEntryIfAdminStatus_Type()
)
vrIfTableEntryIfAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIfTableEntryIfAdminStatus.setStatus("mandatory")


class _VrIfTableEntryIfOperStatus_Type(Integer32):
    """Custom type vrIfTableEntryIfOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_VrIfTableEntryIfOperStatus_Type.__name__ = "Integer32"
_VrIfTableEntryIfOperStatus_Object = MibTableColumn
vrIfTableEntryIfOperStatus = _VrIfTableEntryIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 3),
    _VrIfTableEntryIfOperStatus_Type()
)
vrIfTableEntryIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIfTableEntryIfOperStatus.setStatus("mandatory")


class _VrIfTableEntryIfLastChange_Type(Unsigned32):
    """Custom type vrIfTableEntryIfLastChange based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIfTableEntryIfLastChange_Type.__name__ = "Unsigned32"
_VrIfTableEntryIfLastChange_Object = MibTableColumn
vrIfTableEntryIfLastChange = _VrIfTableEntryIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 4),
    _VrIfTableEntryIfLastChange_Type()
)
vrIfTableEntryIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIfTableEntryIfLastChange.setStatus("mandatory")
_VrIfTableEntryIfInOctets_Type = Counter32
_VrIfTableEntryIfInOctets_Object = MibTableColumn
vrIfTableEntryIfInOctets = _VrIfTableEntryIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 5),
    _VrIfTableEntryIfInOctets_Type()
)
vrIfTableEntryIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIfTableEntryIfInOctets.setStatus("mandatory")
_VrIfTableEntryIfOutOctets_Type = Counter32
_VrIfTableEntryIfOutOctets_Object = MibTableColumn
vrIfTableEntryIfOutOctets = _VrIfTableEntryIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 6),
    _VrIfTableEntryIfOutOctets_Type()
)
vrIfTableEntryIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIfTableEntryIfOutOctets.setStatus("mandatory")
_VrIfTableEntryIfInDiscards_Type = Counter32
_VrIfTableEntryIfInDiscards_Object = MibTableColumn
vrIfTableEntryIfInDiscards = _VrIfTableEntryIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 7),
    _VrIfTableEntryIfInDiscards_Type()
)
vrIfTableEntryIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIfTableEntryIfInDiscards.setStatus("mandatory")
_VrIfTableEntryIfOutDiscards_Type = Counter32
_VrIfTableEntryIfOutDiscards_Object = MibTableColumn
vrIfTableEntryIfOutDiscards = _VrIfTableEntryIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 8),
    _VrIfTableEntryIfOutDiscards_Type()
)
vrIfTableEntryIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIfTableEntryIfOutDiscards.setStatus("mandatory")
_VrIfTableEntryIfInErrors_Type = Counter32
_VrIfTableEntryIfInErrors_Object = MibTableColumn
vrIfTableEntryIfInErrors = _VrIfTableEntryIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 9),
    _VrIfTableEntryIfInErrors_Type()
)
vrIfTableEntryIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIfTableEntryIfInErrors.setStatus("mandatory")
_VrIfTableEntryIfOutErrors_Type = Counter32
_VrIfTableEntryIfOutErrors_Object = MibTableColumn
vrIfTableEntryIfOutErrors = _VrIfTableEntryIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 10),
    _VrIfTableEntryIfOutErrors_Type()
)
vrIfTableEntryIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIfTableEntryIfOutErrors.setStatus("mandatory")
_VrIfTableEntryIfInUcastPkts_Type = Counter32
_VrIfTableEntryIfInUcastPkts_Object = MibTableColumn
vrIfTableEntryIfInUcastPkts = _VrIfTableEntryIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 11),
    _VrIfTableEntryIfInUcastPkts_Type()
)
vrIfTableEntryIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIfTableEntryIfInUcastPkts.setStatus("mandatory")
_VrIfTableEntryIfOutUcastPkts_Type = Counter32
_VrIfTableEntryIfOutUcastPkts_Object = MibTableColumn
vrIfTableEntryIfOutUcastPkts = _VrIfTableEntryIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 12),
    _VrIfTableEntryIfOutUcastPkts_Type()
)
vrIfTableEntryIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIfTableEntryIfOutUcastPkts.setStatus("mandatory")
_VrIfTableEntryIfInNuCastPkts_Type = Counter32
_VrIfTableEntryIfInNuCastPkts_Object = MibTableColumn
vrIfTableEntryIfInNuCastPkts = _VrIfTableEntryIfInNuCastPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 13),
    _VrIfTableEntryIfInNuCastPkts_Type()
)
vrIfTableEntryIfInNuCastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIfTableEntryIfInNuCastPkts.setStatus("mandatory")
_VrIfTableEntryIfOutNuCastPkts_Type = Counter32
_VrIfTableEntryIfOutNuCastPkts_Object = MibTableColumn
vrIfTableEntryIfOutNuCastPkts = _VrIfTableEntryIfOutNuCastPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 14),
    _VrIfTableEntryIfOutNuCastPkts_Type()
)
vrIfTableEntryIfOutNuCastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIfTableEntryIfOutNuCastPkts.setStatus("mandatory")
_VrIfTableEntryIfInUnknownProtos_Type = Counter32
_VrIfTableEntryIfInUnknownProtos_Object = MibTableColumn
vrIfTableEntryIfInUnknownProtos = _VrIfTableEntryIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 15),
    _VrIfTableEntryIfInUnknownProtos_Type()
)
vrIfTableEntryIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIfTableEntryIfInUnknownProtos.setStatus("mandatory")


class _VrIfTableEntryIfOutQlength_Type(Gauge32):
    """Custom type vrIfTableEntryIfOutQlength based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIfTableEntryIfOutQlength_Type.__name__ = "Gauge32"
_VrIfTableEntryIfOutQlength_Object = MibTableColumn
vrIfTableEntryIfOutQlength = _VrIfTableEntryIfOutQlength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 16),
    _VrIfTableEntryIfOutQlength_Type()
)
vrIfTableEntryIfOutQlength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIfTableEntryIfOutQlength.setStatus("mandatory")


class _VrIfTableEntryIfDescription_Type(AsciiString):
    """Custom type vrIfTableEntryIfDescription based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VrIfTableEntryIfDescription_Type.__name__ = "AsciiString"
_VrIfTableEntryIfDescription_Object = MibTableColumn
vrIfTableEntryIfDescription = _VrIfTableEntryIfDescription_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 17),
    _VrIfTableEntryIfDescription_Type()
)
vrIfTableEntryIfDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIfTableEntryIfDescription.setStatus("mandatory")


class _VrIfTableEntryIfType_Type(Integer32):
    """Custom type vrIfTableEntryIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              30,
              31,
              32,
              44,
              45,
              46,
              59,
              60,
              64,
              1039,
              1040,
              1041,
              1042,
              1043)
        )
    )
    namedValues = NamedValues(
        *(("aflane8023", 59),
          ("aflane8025", 60),
          ("atmMpeLlcEncap", 1040),
          ("atmMpeVcEncap", 1039),
          ("basicIsdn", 20),
          ("ddnX25", 4),
          ("ds1", 18),
          ("ds3", 30),
          ("e1", 19),
          ("ethernet8023", 7),
          ("ethernetCsmacd", 6),
          ("fddi", 15),
          ("frameRelay", 32),
          ("frameRelayService", 44),
          ("hssi", 46),
          ("hyperChannel", 14),
          ("ilsForwarder", 1041),
          ("ipTunnel", 1042),
          ("lapb", 16),
          ("man802", 10),
          ("other", 1),
          ("ppp", 23),
          ("primaryIsdn", 21),
          ("propPointToPointSerial", 22),
          ("rfc877x25", 5),
          ("sdlc", 17),
          ("smds", 31),
          ("starLan", 11),
          ("tokenBus8024", 8),
          ("tokenring8025", 9),
          ("v11", 64),
          ("v35", 45),
          ("virtualMedia", 1043))
    )


_VrIfTableEntryIfType_Type.__name__ = "Integer32"
_VrIfTableEntryIfType_Object = MibTableColumn
vrIfTableEntryIfType = _VrIfTableEntryIfType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 18),
    _VrIfTableEntryIfType_Type()
)
vrIfTableEntryIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIfTableEntryIfType.setStatus("mandatory")


class _VrIfTableEntryIfMtu_Type(Unsigned32):
    """Custom type vrIfTableEntryIfMtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIfTableEntryIfMtu_Type.__name__ = "Unsigned32"
_VrIfTableEntryIfMtu_Object = MibTableColumn
vrIfTableEntryIfMtu = _VrIfTableEntryIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 19),
    _VrIfTableEntryIfMtu_Type()
)
vrIfTableEntryIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIfTableEntryIfMtu.setStatus("mandatory")


class _VrIfTableEntryIfSpeed_Type(Unsigned32):
    """Custom type vrIfTableEntryIfSpeed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIfTableEntryIfSpeed_Type.__name__ = "Unsigned32"
_VrIfTableEntryIfSpeed_Object = MibTableColumn
vrIfTableEntryIfSpeed = _VrIfTableEntryIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 20),
    _VrIfTableEntryIfSpeed_Type()
)
vrIfTableEntryIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIfTableEntryIfSpeed.setStatus("mandatory")


class _VrIfTableEntryIfPhysicalAddress_Type(AsciiString):
    """Custom type vrIfTableEntryIfPhysicalAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_VrIfTableEntryIfPhysicalAddress_Type.__name__ = "AsciiString"
_VrIfTableEntryIfPhysicalAddress_Object = MibTableColumn
vrIfTableEntryIfPhysicalAddress = _VrIfTableEntryIfPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 21),
    _VrIfTableEntryIfPhysicalAddress_Type()
)
vrIfTableEntryIfPhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIfTableEntryIfPhysicalAddress.setStatus("mandatory")
_VrIfTableEntryIfSpecific_Type = IntegerSequence
_VrIfTableEntryIfSpecific_Object = MibTableColumn
vrIfTableEntryIfSpecific = _VrIfTableEntryIfSpecific_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 22),
    _VrIfTableEntryIfSpecific_Type()
)
vrIfTableEntryIfSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIfTableEntryIfSpecific.setStatus("mandatory")
_VrIfTableEntryAdditionalInfoTable_Object = MibTable
vrIfTableEntryAdditionalInfoTable = _VrIfTableEntryAdditionalInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 11)
)
if mibBuilder.loadTexts:
    vrIfTableEntryAdditionalInfoTable.setStatus("mandatory")
_VrIfTableEntryAdditionalInfoEntry_Object = MibTableRow
vrIfTableEntryAdditionalInfoEntry = _VrIfTableEntryAdditionalInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 11, 1)
)
vrIfTableEntryAdditionalInfoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIfTableEntryIndex"),
)
if mibBuilder.loadTexts:
    vrIfTableEntryAdditionalInfoEntry.setStatus("mandatory")
_VrIfTableEntryStdComponentName_Type = RowPointer
_VrIfTableEntryStdComponentName_Object = MibTableColumn
vrIfTableEntryStdComponentName = _VrIfTableEntryStdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 11, 1, 1),
    _VrIfTableEntryStdComponentName_Type()
)
vrIfTableEntryStdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIfTableEntryStdComponentName.setStatus("mandatory")
_VrQosP_ObjectIdentity = ObjectIdentity
vrQosP = _VrQosP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 15)
)
_VrQosPRowStatusTable_Object = MibTable
vrQosPRowStatusTable = _VrQosPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 15, 1)
)
if mibBuilder.loadTexts:
    vrQosPRowStatusTable.setStatus("mandatory")
_VrQosPRowStatusEntry_Object = MibTableRow
vrQosPRowStatusEntry = _VrQosPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 15, 1, 1)
)
vrQosPRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrQosPIndex"),
)
if mibBuilder.loadTexts:
    vrQosPRowStatusEntry.setStatus("mandatory")
_VrQosPRowStatus_Type = RowStatus
_VrQosPRowStatus_Object = MibTableColumn
vrQosPRowStatus = _VrQosPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 15, 1, 1, 1),
    _VrQosPRowStatus_Type()
)
vrQosPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrQosPRowStatus.setStatus("mandatory")
_VrQosPComponentName_Type = DisplayString
_VrQosPComponentName_Object = MibTableColumn
vrQosPComponentName = _VrQosPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 15, 1, 1, 2),
    _VrQosPComponentName_Type()
)
vrQosPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrQosPComponentName.setStatus("mandatory")
_VrQosPStorageType_Type = StorageType
_VrQosPStorageType_Object = MibTableColumn
vrQosPStorageType = _VrQosPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 15, 1, 1, 4),
    _VrQosPStorageType_Type()
)
vrQosPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrQosPStorageType.setStatus("mandatory")


class _VrQosPIndex_Type(Integer32):
    """Custom type vrQosPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_VrQosPIndex_Type.__name__ = "Integer32"
_VrQosPIndex_Object = MibTableColumn
vrQosPIndex = _VrQosPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 15, 1, 1, 10),
    _VrQosPIndex_Type()
)
vrQosPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrQosPIndex.setStatus("mandatory")
_VrQosPProvTable_Object = MibTable
vrQosPProvTable = _VrQosPProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 15, 10)
)
if mibBuilder.loadTexts:
    vrQosPProvTable.setStatus("mandatory")
_VrQosPProvEntry_Object = MibTableRow
vrQosPProvEntry = _VrQosPProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 15, 10, 1)
)
vrQosPProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrQosPIndex"),
)
if mibBuilder.loadTexts:
    vrQosPProvEntry.setStatus("mandatory")


class _VrQosPVnsDiscardPriority_Type(Unsigned32):
    """Custom type vrQosPVnsDiscardPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_VrQosPVnsDiscardPriority_Type.__name__ = "Unsigned32"
_VrQosPVnsDiscardPriority_Object = MibTableColumn
vrQosPVnsDiscardPriority = _VrQosPVnsDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 15, 10, 1, 1),
    _VrQosPVnsDiscardPriority_Type()
)
vrQosPVnsDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrQosPVnsDiscardPriority.setStatus("mandatory")


class _VrQosPVnsEmissionPriority_Type(Unsigned32):
    """Custom type vrQosPVnsEmissionPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_VrQosPVnsEmissionPriority_Type.__name__ = "Unsigned32"
_VrQosPVnsEmissionPriority_Object = MibTableColumn
vrQosPVnsEmissionPriority = _VrQosPVnsEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 15, 10, 1, 2),
    _VrQosPVnsEmissionPriority_Type()
)
vrQosPVnsEmissionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrQosPVnsEmissionPriority.setStatus("mandatory")


class _VrQosPWanEmissionPriority_Type(Unsigned32):
    """Custom type vrQosPWanEmissionPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_VrQosPWanEmissionPriority_Type.__name__ = "Unsigned32"
_VrQosPWanEmissionPriority_Object = MibTableColumn
vrQosPWanEmissionPriority = _VrQosPWanEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 15, 10, 1, 3),
    _VrQosPWanEmissionPriority_Type()
)
vrQosPWanEmissionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrQosPWanEmissionPriority.setStatus("obsolete")
_VrAdminContorlTable_Object = MibTable
vrAdminContorlTable = _VrAdminContorlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 100)
)
if mibBuilder.loadTexts:
    vrAdminContorlTable.setStatus("mandatory")
_VrAdminContorlEntry_Object = MibTableRow
vrAdminContorlEntry = _VrAdminContorlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 100, 1)
)
vrAdminContorlEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
)
if mibBuilder.loadTexts:
    vrAdminContorlEntry.setStatus("mandatory")


class _VrSnmpAdminStatus_Type(Integer32):
    """Custom type vrSnmpAdminStatus based on Integer32"""
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


_VrSnmpAdminStatus_Type.__name__ = "Integer32"
_VrSnmpAdminStatus_Object = MibTableColumn
vrSnmpAdminStatus = _VrSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 100, 1, 1),
    _VrSnmpAdminStatus_Type()
)
vrSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSnmpAdminStatus.setStatus("mandatory")


class _VrManagementAccess_Type(Integer32):
    """Custom type vrManagementAccess based on Integer32"""
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


_VrManagementAccess_Type.__name__ = "Integer32"
_VrManagementAccess_Object = MibTableColumn
vrManagementAccess = _VrManagementAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 100, 1, 2),
    _VrManagementAccess_Type()
)
vrManagementAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrManagementAccess.setStatus("mandatory")


class _VrVirtualPrivateIntranetIdentifier_Type(Integer32):
    """Custom type vrVirtualPrivateIntranetIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrVirtualPrivateIntranetIdentifier_Type.__name__ = "Integer32"
_VrVirtualPrivateIntranetIdentifier_Object = MibTableColumn
vrVirtualPrivateIntranetIdentifier = _VrVirtualPrivateIntranetIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 100, 1, 3),
    _VrVirtualPrivateIntranetIdentifier_Type()
)
vrVirtualPrivateIntranetIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrVirtualPrivateIntranetIdentifier.setStatus("mandatory")
_VrCidDataTable_Object = MibTable
vrCidDataTable = _VrCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 101)
)
if mibBuilder.loadTexts:
    vrCidDataTable.setStatus("mandatory")
_VrCidDataEntry_Object = MibTableRow
vrCidDataEntry = _VrCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 101, 1)
)
vrCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
)
if mibBuilder.loadTexts:
    vrCidDataEntry.setStatus("mandatory")


class _VrCustomerIdentifier_Type(Unsigned32):
    """Custom type vrCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_VrCustomerIdentifier_Type.__name__ = "Unsigned32"
_VrCustomerIdentifier_Object = MibTableColumn
vrCustomerIdentifier = _VrCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 101, 1, 1),
    _VrCustomerIdentifier_Type()
)
vrCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrCustomerIdentifier.setStatus("mandatory")
_VrOperStatusTable_Object = MibTable
vrOperStatusTable = _VrOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 103)
)
if mibBuilder.loadTexts:
    vrOperStatusTable.setStatus("mandatory")
_VrOperStatusEntry_Object = MibTableRow
vrOperStatusEntry = _VrOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 103, 1)
)
vrOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
)
if mibBuilder.loadTexts:
    vrOperStatusEntry.setStatus("mandatory")


class _VrSnmpOperStatus_Type(Integer32):
    """Custom type vrSnmpOperStatus based on Integer32"""
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


_VrSnmpOperStatus_Type.__name__ = "Integer32"
_VrSnmpOperStatus_Object = MibTableColumn
vrSnmpOperStatus = _VrSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 103, 1, 1),
    _VrSnmpOperStatus_Type()
)
vrSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSnmpOperStatus.setStatus("mandatory")
_VrStateTable_Object = MibTable
vrStateTable = _VrStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 104)
)
if mibBuilder.loadTexts:
    vrStateTable.setStatus("mandatory")
_VrStateEntry_Object = MibTableRow
vrStateEntry = _VrStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 104, 1)
)
vrStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
)
if mibBuilder.loadTexts:
    vrStateEntry.setStatus("mandatory")


class _VrAdminState_Type(Integer32):
    """Custom type vrAdminState based on Integer32"""
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


_VrAdminState_Type.__name__ = "Integer32"
_VrAdminState_Object = MibTableColumn
vrAdminState = _VrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 104, 1, 1),
    _VrAdminState_Type()
)
vrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrAdminState.setStatus("mandatory")


class _VrOperationalState_Type(Integer32):
    """Custom type vrOperationalState based on Integer32"""
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


_VrOperationalState_Type.__name__ = "Integer32"
_VrOperationalState_Object = MibTableColumn
vrOperationalState = _VrOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 104, 1, 2),
    _VrOperationalState_Type()
)
vrOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrOperationalState.setStatus("mandatory")


class _VrUsageState_Type(Integer32):
    """Custom type vrUsageState based on Integer32"""
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


_VrUsageState_Type.__name__ = "Integer32"
_VrUsageState_Object = MibTableColumn
vrUsageState = _VrUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 104, 1, 3),
    _VrUsageState_Type()
)
vrUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrUsageState.setStatus("mandatory")
_VrIfNumberOperTable_Object = MibTable
vrIfNumberOperTable = _VrIfNumberOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 105)
)
if mibBuilder.loadTexts:
    vrIfNumberOperTable.setStatus("mandatory")
_VrIfNumberOperEntry_Object = MibTableRow
vrIfNumberOperEntry = _VrIfNumberOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 105, 1)
)
vrIfNumberOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
)
if mibBuilder.loadTexts:
    vrIfNumberOperEntry.setStatus("mandatory")


class _VrIfNumber_Type(Unsigned32):
    """Custom type vrIfNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIfNumber_Type.__name__ = "Unsigned32"
_VrIfNumber_Object = MibTableColumn
vrIfNumber = _VrIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 105, 1, 1),
    _VrIfNumber_Type()
)
vrIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIfNumber.setStatus("mandatory")
_VirtualRouterMIB_ObjectIdentity = ObjectIdentity
virtualRouterMIB = _VirtualRouterMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 26)
)
_VirtualRouterGroup_ObjectIdentity = ObjectIdentity
virtualRouterGroup = _VirtualRouterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 26, 1)
)
_VirtualRouterGroupBE_ObjectIdentity = ObjectIdentity
virtualRouterGroupBE = _VirtualRouterGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 26, 1, 5)
)
_VirtualRouterGroupBE01_ObjectIdentity = ObjectIdentity
virtualRouterGroupBE01 = _VirtualRouterGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 26, 1, 5, 2)
)
_VirtualRouterGroupBE01A_ObjectIdentity = ObjectIdentity
virtualRouterGroupBE01A = _VirtualRouterGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 26, 1, 5, 2, 2)
)
_VirtualRouterCapabilities_ObjectIdentity = ObjectIdentity
virtualRouterCapabilities = _VirtualRouterCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 26, 3)
)
_VirtualRouterCapabilitiesBE_ObjectIdentity = ObjectIdentity
virtualRouterCapabilitiesBE = _VirtualRouterCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 26, 3, 5)
)
_VirtualRouterCapabilitiesBE01_ObjectIdentity = ObjectIdentity
virtualRouterCapabilitiesBE01 = _VirtualRouterCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 26, 3, 5, 2)
)
_VirtualRouterCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
virtualRouterCapabilitiesBE01A = _VirtualRouterCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 26, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-VirtualRouterMIB",
    **{"vr": vr,
       "vrRowStatusTable": vrRowStatusTable,
       "vrRowStatusEntry": vrRowStatusEntry,
       "vrRowStatus": vrRowStatus,
       "vrComponentName": vrComponentName,
       "vrStorageType": vrStorageType,
       "vrIndex": vrIndex,
       "vrMm": vrMm,
       "vrMmRowStatusTable": vrMmRowStatusTable,
       "vrMmRowStatusEntry": vrMmRowStatusEntry,
       "vrMmRowStatus": vrMmRowStatus,
       "vrMmComponentName": vrMmComponentName,
       "vrMmStorageType": vrMmStorageType,
       "vrMmIndex": vrMmIndex,
       "vrMmProvTable": vrMmProvTable,
       "vrMmProvEntry": vrMmProvEntry,
       "vrMmVrMaxHeapSpace": vrMmVrMaxHeapSpace,
       "vrMmIpMaxHeapSpace": vrMmIpMaxHeapSpace,
       "vrMmIpxMaxHeapSpace": vrMmIpxMaxHeapSpace,
       "vrMmBridgingMaxHeapSpace": vrMmBridgingMaxHeapSpace,
       "vrMmNetSentryMaxHeapSpace": vrMmNetSentryMaxHeapSpace,
       "vrMmSresMaxHeapSpace": vrMmSresMaxHeapSpace,
       "vrMmSnaMaxHeapSpace": vrMmSnaMaxHeapSpace,
       "vrMmOperTable": vrMmOperTable,
       "vrMmOperEntry": vrMmOperEntry,
       "vrMmVrHeapSpaceBytesAllocated": vrMmVrHeapSpaceBytesAllocated,
       "vrMmVrHeapSpaceAllocated": vrMmVrHeapSpaceAllocated,
       "vrMmIpHeapSpaceAllocated": vrMmIpHeapSpaceAllocated,
       "vrMmIpxHeapSpaceAllocated": vrMmIpxHeapSpaceAllocated,
       "vrMmBridgingHeapSpaceAllocated": vrMmBridgingHeapSpaceAllocated,
       "vrMmNetSentryHeapSpaceAllocated": vrMmNetSentryHeapSpaceAllocated,
       "vrMmSresHeapSpaceAllocated": vrMmSresHeapSpaceAllocated,
       "vrMmSnaHeapSpaceAllocated": vrMmSnaHeapSpaceAllocated,
       "vrPp": vrPp,
       "vrPpRowStatusTable": vrPpRowStatusTable,
       "vrPpRowStatusEntry": vrPpRowStatusEntry,
       "vrPpRowStatus": vrPpRowStatus,
       "vrPpComponentName": vrPpComponentName,
       "vrPpStorageType": vrPpStorageType,
       "vrPpIndex": vrPpIndex,
       "vrPpAdminControlTable": vrPpAdminControlTable,
       "vrPpAdminControlEntry": vrPpAdminControlEntry,
       "vrPpSnmpAdminStatus": vrPpSnmpAdminStatus,
       "vrPpProvTable": vrPpProvTable,
       "vrPpProvEntry": vrPpProvEntry,
       "vrPpLinkToMedia": vrPpLinkToMedia,
       "vrPpOperStatusTable": vrPpOperStatusTable,
       "vrPpOperStatusEntry": vrPpOperStatusEntry,
       "vrPpSnmpOperStatus": vrPpSnmpOperStatus,
       "vrPpStateTable": vrPpStateTable,
       "vrPpStateEntry": vrPpStateEntry,
       "vrPpAdminState": vrPpAdminState,
       "vrPpOperationalState": vrPpOperationalState,
       "vrPpUsageState": vrPpUsageState,
       "vrPpOperTable": vrPpOperTable,
       "vrPpOperEntry": vrPpOperEntry,
       "vrPpIfIndex": vrPpIfIndex,
       "vrPpNbmaAddressTable": vrPpNbmaAddressTable,
       "vrPpNbmaAddressEntry": vrPpNbmaAddressEntry,
       "vrPpAtmAddress": vrPpAtmAddress,
       "vrIfTableEntry": vrIfTableEntry,
       "vrIfTableEntryRowStatusTable": vrIfTableEntryRowStatusTable,
       "vrIfTableEntryRowStatusEntry": vrIfTableEntryRowStatusEntry,
       "vrIfTableEntryRowStatus": vrIfTableEntryRowStatus,
       "vrIfTableEntryComponentName": vrIfTableEntryComponentName,
       "vrIfTableEntryStorageType": vrIfTableEntryStorageType,
       "vrIfTableEntryIndex": vrIfTableEntryIndex,
       "vrIfTableEntryIftTable": vrIfTableEntryIftTable,
       "vrIfTableEntryIftEntry": vrIfTableEntryIftEntry,
       "vrIfTableEntryIfAdminStatus": vrIfTableEntryIfAdminStatus,
       "vrIfTableEntryIfOperStatus": vrIfTableEntryIfOperStatus,
       "vrIfTableEntryIfLastChange": vrIfTableEntryIfLastChange,
       "vrIfTableEntryIfInOctets": vrIfTableEntryIfInOctets,
       "vrIfTableEntryIfOutOctets": vrIfTableEntryIfOutOctets,
       "vrIfTableEntryIfInDiscards": vrIfTableEntryIfInDiscards,
       "vrIfTableEntryIfOutDiscards": vrIfTableEntryIfOutDiscards,
       "vrIfTableEntryIfInErrors": vrIfTableEntryIfInErrors,
       "vrIfTableEntryIfOutErrors": vrIfTableEntryIfOutErrors,
       "vrIfTableEntryIfInUcastPkts": vrIfTableEntryIfInUcastPkts,
       "vrIfTableEntryIfOutUcastPkts": vrIfTableEntryIfOutUcastPkts,
       "vrIfTableEntryIfInNuCastPkts": vrIfTableEntryIfInNuCastPkts,
       "vrIfTableEntryIfOutNuCastPkts": vrIfTableEntryIfOutNuCastPkts,
       "vrIfTableEntryIfInUnknownProtos": vrIfTableEntryIfInUnknownProtos,
       "vrIfTableEntryIfOutQlength": vrIfTableEntryIfOutQlength,
       "vrIfTableEntryIfDescription": vrIfTableEntryIfDescription,
       "vrIfTableEntryIfType": vrIfTableEntryIfType,
       "vrIfTableEntryIfMtu": vrIfTableEntryIfMtu,
       "vrIfTableEntryIfSpeed": vrIfTableEntryIfSpeed,
       "vrIfTableEntryIfPhysicalAddress": vrIfTableEntryIfPhysicalAddress,
       "vrIfTableEntryIfSpecific": vrIfTableEntryIfSpecific,
       "vrIfTableEntryAdditionalInfoTable": vrIfTableEntryAdditionalInfoTable,
       "vrIfTableEntryAdditionalInfoEntry": vrIfTableEntryAdditionalInfoEntry,
       "vrIfTableEntryStdComponentName": vrIfTableEntryStdComponentName,
       "vrQosP": vrQosP,
       "vrQosPRowStatusTable": vrQosPRowStatusTable,
       "vrQosPRowStatusEntry": vrQosPRowStatusEntry,
       "vrQosPRowStatus": vrQosPRowStatus,
       "vrQosPComponentName": vrQosPComponentName,
       "vrQosPStorageType": vrQosPStorageType,
       "vrQosPIndex": vrQosPIndex,
       "vrQosPProvTable": vrQosPProvTable,
       "vrQosPProvEntry": vrQosPProvEntry,
       "vrQosPVnsDiscardPriority": vrQosPVnsDiscardPriority,
       "vrQosPVnsEmissionPriority": vrQosPVnsEmissionPriority,
       "vrQosPWanEmissionPriority": vrQosPWanEmissionPriority,
       "vrAdminContorlTable": vrAdminContorlTable,
       "vrAdminContorlEntry": vrAdminContorlEntry,
       "vrSnmpAdminStatus": vrSnmpAdminStatus,
       "vrManagementAccess": vrManagementAccess,
       "vrVirtualPrivateIntranetIdentifier": vrVirtualPrivateIntranetIdentifier,
       "vrCidDataTable": vrCidDataTable,
       "vrCidDataEntry": vrCidDataEntry,
       "vrCustomerIdentifier": vrCustomerIdentifier,
       "vrOperStatusTable": vrOperStatusTable,
       "vrOperStatusEntry": vrOperStatusEntry,
       "vrSnmpOperStatus": vrSnmpOperStatus,
       "vrStateTable": vrStateTable,
       "vrStateEntry": vrStateEntry,
       "vrAdminState": vrAdminState,
       "vrOperationalState": vrOperationalState,
       "vrUsageState": vrUsageState,
       "vrIfNumberOperTable": vrIfNumberOperTable,
       "vrIfNumberOperEntry": vrIfNumberOperEntry,
       "vrIfNumber": vrIfNumber,
       "virtualRouterMIB": virtualRouterMIB,
       "virtualRouterGroup": virtualRouterGroup,
       "virtualRouterGroupBE": virtualRouterGroupBE,
       "virtualRouterGroupBE01": virtualRouterGroupBE01,
       "virtualRouterGroupBE01A": virtualRouterGroupBE01A,
       "virtualRouterCapabilities": virtualRouterCapabilities,
       "virtualRouterCapabilitiesBE": virtualRouterCapabilitiesBE,
       "virtualRouterCapabilitiesBE01": virtualRouterCapabilitiesBE01,
       "virtualRouterCapabilitiesBE01A": virtualRouterCapabilitiesBE01A}
)
