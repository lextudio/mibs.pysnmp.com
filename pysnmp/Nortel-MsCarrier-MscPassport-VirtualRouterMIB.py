# SNMP MIB module (Nortel-MsCarrier-MscPassport-VirtualRouterMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-VirtualRouterMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:59 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
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
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
    "HexString",
    "IntegerSequence",
    "Link",
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

_MscVr_ObjectIdentity = ObjectIdentity
mscVr = _MscVr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100)
)
_MscVrRowStatusTable_Object = MibTable
mscVrRowStatusTable = _MscVrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 1)
)
if mibBuilder.loadTexts:
    mscVrRowStatusTable.setStatus("mandatory")
_MscVrRowStatusEntry_Object = MibTableRow
mscVrRowStatusEntry = _MscVrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 1, 1)
)
mscVrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
)
if mibBuilder.loadTexts:
    mscVrRowStatusEntry.setStatus("mandatory")
_MscVrRowStatus_Type = RowStatus
_MscVrRowStatus_Object = MibTableColumn
mscVrRowStatus = _MscVrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 1, 1, 1),
    _MscVrRowStatus_Type()
)
mscVrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrRowStatus.setStatus("mandatory")
_MscVrComponentName_Type = DisplayString
_MscVrComponentName_Object = MibTableColumn
mscVrComponentName = _MscVrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 1, 1, 2),
    _MscVrComponentName_Type()
)
mscVrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrComponentName.setStatus("mandatory")
_MscVrStorageType_Type = StorageType
_MscVrStorageType_Object = MibTableColumn
mscVrStorageType = _MscVrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 1, 1, 4),
    _MscVrStorageType_Type()
)
mscVrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrStorageType.setStatus("mandatory")


class _MscVrIndex_Type(AsciiStringIndex):
    """Custom type mscVrIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscVrIndex_Type.__name__ = "AsciiStringIndex"
_MscVrIndex_Object = MibTableColumn
mscVrIndex = _MscVrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 1, 1, 10),
    _MscVrIndex_Type()
)
mscVrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIndex.setStatus("mandatory")
_MscVrMm_ObjectIdentity = ObjectIdentity
mscVrMm = _MscVrMm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2)
)
_MscVrMmRowStatusTable_Object = MibTable
mscVrMmRowStatusTable = _MscVrMmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrMmRowStatusTable.setStatus("mandatory")
_MscVrMmRowStatusEntry_Object = MibTableRow
mscVrMmRowStatusEntry = _MscVrMmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 1, 1)
)
mscVrMmRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrMmIndex"),
)
if mibBuilder.loadTexts:
    mscVrMmRowStatusEntry.setStatus("mandatory")
_MscVrMmRowStatus_Type = RowStatus
_MscVrMmRowStatus_Object = MibTableColumn
mscVrMmRowStatus = _MscVrMmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 1, 1, 1),
    _MscVrMmRowStatus_Type()
)
mscVrMmRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrMmRowStatus.setStatus("mandatory")
_MscVrMmComponentName_Type = DisplayString
_MscVrMmComponentName_Object = MibTableColumn
mscVrMmComponentName = _MscVrMmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 1, 1, 2),
    _MscVrMmComponentName_Type()
)
mscVrMmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrMmComponentName.setStatus("mandatory")
_MscVrMmStorageType_Type = StorageType
_MscVrMmStorageType_Object = MibTableColumn
mscVrMmStorageType = _MscVrMmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 1, 1, 4),
    _MscVrMmStorageType_Type()
)
mscVrMmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrMmStorageType.setStatus("mandatory")
_MscVrMmIndex_Type = NonReplicated
_MscVrMmIndex_Object = MibTableColumn
mscVrMmIndex = _MscVrMmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 1, 1, 10),
    _MscVrMmIndex_Type()
)
mscVrMmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrMmIndex.setStatus("mandatory")
_MscVrMmProvTable_Object = MibTable
mscVrMmProvTable = _MscVrMmProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrMmProvTable.setStatus("mandatory")
_MscVrMmProvEntry_Object = MibTableRow
mscVrMmProvEntry = _MscVrMmProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 10, 1)
)
mscVrMmProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrMmIndex"),
)
if mibBuilder.loadTexts:
    mscVrMmProvEntry.setStatus("mandatory")


class _MscVrMmVrMaxHeapSpace_Type(Unsigned32):
    """Custom type mscVrMmVrMaxHeapSpace based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscVrMmVrMaxHeapSpace_Type.__name__ = "Unsigned32"
_MscVrMmVrMaxHeapSpace_Object = MibTableColumn
mscVrMmVrMaxHeapSpace = _MscVrMmVrMaxHeapSpace_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 10, 1, 1),
    _MscVrMmVrMaxHeapSpace_Type()
)
mscVrMmVrMaxHeapSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrMmVrMaxHeapSpace.setStatus("mandatory")


class _MscVrMmIpMaxHeapSpace_Type(Unsigned32):
    """Custom type mscVrMmIpMaxHeapSpace based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscVrMmIpMaxHeapSpace_Type.__name__ = "Unsigned32"
_MscVrMmIpMaxHeapSpace_Object = MibTableColumn
mscVrMmIpMaxHeapSpace = _MscVrMmIpMaxHeapSpace_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 10, 1, 2),
    _MscVrMmIpMaxHeapSpace_Type()
)
mscVrMmIpMaxHeapSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrMmIpMaxHeapSpace.setStatus("mandatory")


class _MscVrMmIpxMaxHeapSpace_Type(Unsigned32):
    """Custom type mscVrMmIpxMaxHeapSpace based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscVrMmIpxMaxHeapSpace_Type.__name__ = "Unsigned32"
_MscVrMmIpxMaxHeapSpace_Object = MibTableColumn
mscVrMmIpxMaxHeapSpace = _MscVrMmIpxMaxHeapSpace_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 10, 1, 3),
    _MscVrMmIpxMaxHeapSpace_Type()
)
mscVrMmIpxMaxHeapSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrMmIpxMaxHeapSpace.setStatus("mandatory")


class _MscVrMmBridgingMaxHeapSpace_Type(Unsigned32):
    """Custom type mscVrMmBridgingMaxHeapSpace based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscVrMmBridgingMaxHeapSpace_Type.__name__ = "Unsigned32"
_MscVrMmBridgingMaxHeapSpace_Object = MibTableColumn
mscVrMmBridgingMaxHeapSpace = _MscVrMmBridgingMaxHeapSpace_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 10, 1, 6),
    _MscVrMmBridgingMaxHeapSpace_Type()
)
mscVrMmBridgingMaxHeapSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrMmBridgingMaxHeapSpace.setStatus("mandatory")


class _MscVrMmNetSentryMaxHeapSpace_Type(Unsigned32):
    """Custom type mscVrMmNetSentryMaxHeapSpace based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscVrMmNetSentryMaxHeapSpace_Type.__name__ = "Unsigned32"
_MscVrMmNetSentryMaxHeapSpace_Object = MibTableColumn
mscVrMmNetSentryMaxHeapSpace = _MscVrMmNetSentryMaxHeapSpace_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 10, 1, 7),
    _MscVrMmNetSentryMaxHeapSpace_Type()
)
mscVrMmNetSentryMaxHeapSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrMmNetSentryMaxHeapSpace.setStatus("mandatory")


class _MscVrMmSresMaxHeapSpace_Type(Unsigned32):
    """Custom type mscVrMmSresMaxHeapSpace based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscVrMmSresMaxHeapSpace_Type.__name__ = "Unsigned32"
_MscVrMmSresMaxHeapSpace_Object = MibTableColumn
mscVrMmSresMaxHeapSpace = _MscVrMmSresMaxHeapSpace_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 10, 1, 8),
    _MscVrMmSresMaxHeapSpace_Type()
)
mscVrMmSresMaxHeapSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrMmSresMaxHeapSpace.setStatus("mandatory")


class _MscVrMmSnaMaxHeapSpace_Type(Unsigned32):
    """Custom type mscVrMmSnaMaxHeapSpace based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscVrMmSnaMaxHeapSpace_Type.__name__ = "Unsigned32"
_MscVrMmSnaMaxHeapSpace_Object = MibTableColumn
mscVrMmSnaMaxHeapSpace = _MscVrMmSnaMaxHeapSpace_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 10, 1, 9),
    _MscVrMmSnaMaxHeapSpace_Type()
)
mscVrMmSnaMaxHeapSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrMmSnaMaxHeapSpace.setStatus("mandatory")
_MscVrMmOperTable_Object = MibTable
mscVrMmOperTable = _MscVrMmOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 11)
)
if mibBuilder.loadTexts:
    mscVrMmOperTable.setStatus("mandatory")
_MscVrMmOperEntry_Object = MibTableRow
mscVrMmOperEntry = _MscVrMmOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 11, 1)
)
mscVrMmOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrMmIndex"),
)
if mibBuilder.loadTexts:
    mscVrMmOperEntry.setStatus("mandatory")


class _MscVrMmVrHeapSpaceBytesAllocated_Type(Unsigned32):
    """Custom type mscVrMmVrHeapSpaceBytesAllocated based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrMmVrHeapSpaceBytesAllocated_Type.__name__ = "Unsigned32"
_MscVrMmVrHeapSpaceBytesAllocated_Object = MibTableColumn
mscVrMmVrHeapSpaceBytesAllocated = _MscVrMmVrHeapSpaceBytesAllocated_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 11, 1, 1),
    _MscVrMmVrHeapSpaceBytesAllocated_Type()
)
mscVrMmVrHeapSpaceBytesAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrMmVrHeapSpaceBytesAllocated.setStatus("mandatory")


class _MscVrMmVrHeapSpaceAllocated_Type(Unsigned32):
    """Custom type mscVrMmVrHeapSpaceAllocated based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscVrMmVrHeapSpaceAllocated_Type.__name__ = "Unsigned32"
_MscVrMmVrHeapSpaceAllocated_Object = MibTableColumn
mscVrMmVrHeapSpaceAllocated = _MscVrMmVrHeapSpaceAllocated_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 11, 1, 2),
    _MscVrMmVrHeapSpaceAllocated_Type()
)
mscVrMmVrHeapSpaceAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrMmVrHeapSpaceAllocated.setStatus("mandatory")


class _MscVrMmIpHeapSpaceAllocated_Type(Unsigned32):
    """Custom type mscVrMmIpHeapSpaceAllocated based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscVrMmIpHeapSpaceAllocated_Type.__name__ = "Unsigned32"
_MscVrMmIpHeapSpaceAllocated_Object = MibTableColumn
mscVrMmIpHeapSpaceAllocated = _MscVrMmIpHeapSpaceAllocated_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 11, 1, 3),
    _MscVrMmIpHeapSpaceAllocated_Type()
)
mscVrMmIpHeapSpaceAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrMmIpHeapSpaceAllocated.setStatus("mandatory")


class _MscVrMmIpxHeapSpaceAllocated_Type(Unsigned32):
    """Custom type mscVrMmIpxHeapSpaceAllocated based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscVrMmIpxHeapSpaceAllocated_Type.__name__ = "Unsigned32"
_MscVrMmIpxHeapSpaceAllocated_Object = MibTableColumn
mscVrMmIpxHeapSpaceAllocated = _MscVrMmIpxHeapSpaceAllocated_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 11, 1, 4),
    _MscVrMmIpxHeapSpaceAllocated_Type()
)
mscVrMmIpxHeapSpaceAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrMmIpxHeapSpaceAllocated.setStatus("mandatory")


class _MscVrMmBridgingHeapSpaceAllocated_Type(Unsigned32):
    """Custom type mscVrMmBridgingHeapSpaceAllocated based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscVrMmBridgingHeapSpaceAllocated_Type.__name__ = "Unsigned32"
_MscVrMmBridgingHeapSpaceAllocated_Object = MibTableColumn
mscVrMmBridgingHeapSpaceAllocated = _MscVrMmBridgingHeapSpaceAllocated_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 11, 1, 7),
    _MscVrMmBridgingHeapSpaceAllocated_Type()
)
mscVrMmBridgingHeapSpaceAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrMmBridgingHeapSpaceAllocated.setStatus("mandatory")


class _MscVrMmNetSentryHeapSpaceAllocated_Type(Unsigned32):
    """Custom type mscVrMmNetSentryHeapSpaceAllocated based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscVrMmNetSentryHeapSpaceAllocated_Type.__name__ = "Unsigned32"
_MscVrMmNetSentryHeapSpaceAllocated_Object = MibTableColumn
mscVrMmNetSentryHeapSpaceAllocated = _MscVrMmNetSentryHeapSpaceAllocated_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 11, 1, 8),
    _MscVrMmNetSentryHeapSpaceAllocated_Type()
)
mscVrMmNetSentryHeapSpaceAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrMmNetSentryHeapSpaceAllocated.setStatus("mandatory")


class _MscVrMmSresHeapSpaceAllocated_Type(Unsigned32):
    """Custom type mscVrMmSresHeapSpaceAllocated based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscVrMmSresHeapSpaceAllocated_Type.__name__ = "Unsigned32"
_MscVrMmSresHeapSpaceAllocated_Object = MibTableColumn
mscVrMmSresHeapSpaceAllocated = _MscVrMmSresHeapSpaceAllocated_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 11, 1, 9),
    _MscVrMmSresHeapSpaceAllocated_Type()
)
mscVrMmSresHeapSpaceAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrMmSresHeapSpaceAllocated.setStatus("mandatory")


class _MscVrMmSnaHeapSpaceAllocated_Type(Unsigned32):
    """Custom type mscVrMmSnaHeapSpaceAllocated based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscVrMmSnaHeapSpaceAllocated_Type.__name__ = "Unsigned32"
_MscVrMmSnaHeapSpaceAllocated_Object = MibTableColumn
mscVrMmSnaHeapSpaceAllocated = _MscVrMmSnaHeapSpaceAllocated_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 2, 11, 1, 10),
    _MscVrMmSnaHeapSpaceAllocated_Type()
)
mscVrMmSnaHeapSpaceAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrMmSnaHeapSpaceAllocated.setStatus("mandatory")
_MscVrPp_ObjectIdentity = ObjectIdentity
mscVrPp = _MscVrPp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3)
)
_MscVrPpRowStatusTable_Object = MibTable
mscVrPpRowStatusTable = _MscVrPpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 1)
)
if mibBuilder.loadTexts:
    mscVrPpRowStatusTable.setStatus("mandatory")
_MscVrPpRowStatusEntry_Object = MibTableRow
mscVrPpRowStatusEntry = _MscVrPpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 1, 1)
)
mscVrPpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpRowStatusEntry.setStatus("mandatory")
_MscVrPpRowStatus_Type = RowStatus
_MscVrPpRowStatus_Object = MibTableColumn
mscVrPpRowStatus = _MscVrPpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 1, 1, 1),
    _MscVrPpRowStatus_Type()
)
mscVrPpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpRowStatus.setStatus("mandatory")
_MscVrPpComponentName_Type = DisplayString
_MscVrPpComponentName_Object = MibTableColumn
mscVrPpComponentName = _MscVrPpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 1, 1, 2),
    _MscVrPpComponentName_Type()
)
mscVrPpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpComponentName.setStatus("mandatory")
_MscVrPpStorageType_Type = StorageType
_MscVrPpStorageType_Object = MibTableColumn
mscVrPpStorageType = _MscVrPpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 1, 1, 4),
    _MscVrPpStorageType_Type()
)
mscVrPpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpStorageType.setStatus("mandatory")


class _MscVrPpIndex_Type(AsciiStringIndex):
    """Custom type mscVrPpIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_MscVrPpIndex_Type.__name__ = "AsciiStringIndex"
_MscVrPpIndex_Object = MibTableColumn
mscVrPpIndex = _MscVrPpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 1, 1, 10),
    _MscVrPpIndex_Type()
)
mscVrPpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpIndex.setStatus("mandatory")
_MscVrPpAdminControlTable_Object = MibTable
mscVrPpAdminControlTable = _MscVrPpAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 100)
)
if mibBuilder.loadTexts:
    mscVrPpAdminControlTable.setStatus("mandatory")
_MscVrPpAdminControlEntry_Object = MibTableRow
mscVrPpAdminControlEntry = _MscVrPpAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 100, 1)
)
mscVrPpAdminControlEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpAdminControlEntry.setStatus("mandatory")


class _MscVrPpSnmpAdminStatus_Type(Integer32):
    """Custom type mscVrPpSnmpAdminStatus based on Integer32"""
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


_MscVrPpSnmpAdminStatus_Type.__name__ = "Integer32"
_MscVrPpSnmpAdminStatus_Object = MibTableColumn
mscVrPpSnmpAdminStatus = _MscVrPpSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 100, 1, 1),
    _MscVrPpSnmpAdminStatus_Type()
)
mscVrPpSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpSnmpAdminStatus.setStatus("mandatory")
_MscVrPpProvTable_Object = MibTable
mscVrPpProvTable = _MscVrPpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 101)
)
if mibBuilder.loadTexts:
    mscVrPpProvTable.setStatus("mandatory")
_MscVrPpProvEntry_Object = MibTableRow
mscVrPpProvEntry = _MscVrPpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 101, 1)
)
mscVrPpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpProvEntry.setStatus("mandatory")
_MscVrPpLinkToMedia_Type = Link
_MscVrPpLinkToMedia_Object = MibTableColumn
mscVrPpLinkToMedia = _MscVrPpLinkToMedia_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 101, 1, 1),
    _MscVrPpLinkToMedia_Type()
)
mscVrPpLinkToMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpLinkToMedia.setStatus("mandatory")
_MscVrPpOperStatusTable_Object = MibTable
mscVrPpOperStatusTable = _MscVrPpOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 102)
)
if mibBuilder.loadTexts:
    mscVrPpOperStatusTable.setStatus("mandatory")
_MscVrPpOperStatusEntry_Object = MibTableRow
mscVrPpOperStatusEntry = _MscVrPpOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 102, 1)
)
mscVrPpOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpOperStatusEntry.setStatus("mandatory")


class _MscVrPpSnmpOperStatus_Type(Integer32):
    """Custom type mscVrPpSnmpOperStatus based on Integer32"""
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


_MscVrPpSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrPpSnmpOperStatus_Object = MibTableColumn
mscVrPpSnmpOperStatus = _MscVrPpSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 102, 1, 1),
    _MscVrPpSnmpOperStatus_Type()
)
mscVrPpSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpSnmpOperStatus.setStatus("mandatory")
_MscVrPpStateTable_Object = MibTable
mscVrPpStateTable = _MscVrPpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 103)
)
if mibBuilder.loadTexts:
    mscVrPpStateTable.setStatus("mandatory")
_MscVrPpStateEntry_Object = MibTableRow
mscVrPpStateEntry = _MscVrPpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 103, 1)
)
mscVrPpStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpStateEntry.setStatus("mandatory")


class _MscVrPpAdminState_Type(Integer32):
    """Custom type mscVrPpAdminState based on Integer32"""
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


_MscVrPpAdminState_Type.__name__ = "Integer32"
_MscVrPpAdminState_Object = MibTableColumn
mscVrPpAdminState = _MscVrPpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 103, 1, 1),
    _MscVrPpAdminState_Type()
)
mscVrPpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpAdminState.setStatus("mandatory")


class _MscVrPpOperationalState_Type(Integer32):
    """Custom type mscVrPpOperationalState based on Integer32"""
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


_MscVrPpOperationalState_Type.__name__ = "Integer32"
_MscVrPpOperationalState_Object = MibTableColumn
mscVrPpOperationalState = _MscVrPpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 103, 1, 2),
    _MscVrPpOperationalState_Type()
)
mscVrPpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpOperationalState.setStatus("mandatory")


class _MscVrPpUsageState_Type(Integer32):
    """Custom type mscVrPpUsageState based on Integer32"""
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


_MscVrPpUsageState_Type.__name__ = "Integer32"
_MscVrPpUsageState_Object = MibTableColumn
mscVrPpUsageState = _MscVrPpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 103, 1, 3),
    _MscVrPpUsageState_Type()
)
mscVrPpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpUsageState.setStatus("mandatory")
_MscVrPpOperTable_Object = MibTable
mscVrPpOperTable = _MscVrPpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 104)
)
if mibBuilder.loadTexts:
    mscVrPpOperTable.setStatus("mandatory")
_MscVrPpOperEntry_Object = MibTableRow
mscVrPpOperEntry = _MscVrPpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 104, 1)
)
mscVrPpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpOperEntry.setStatus("mandatory")


class _MscVrPpIfIndex_Type(InterfaceIndex):
    """Custom type mscVrPpIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrPpIfIndex_Type.__name__ = "InterfaceIndex"
_MscVrPpIfIndex_Object = MibTableColumn
mscVrPpIfIndex = _MscVrPpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 104, 1, 1),
    _MscVrPpIfIndex_Type()
)
mscVrPpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIfIndex.setStatus("mandatory")
_MscVrPpNbmaAddressTable_Object = MibTable
mscVrPpNbmaAddressTable = _MscVrPpNbmaAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 105)
)
if mibBuilder.loadTexts:
    mscVrPpNbmaAddressTable.setStatus("mandatory")
_MscVrPpNbmaAddressEntry_Object = MibTableRow
mscVrPpNbmaAddressEntry = _MscVrPpNbmaAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 105, 1)
)
mscVrPpNbmaAddressEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpNbmaAddressEntry.setStatus("mandatory")


class _MscVrPpAtmAddress_Type(HexString):
    """Custom type mscVrPpAtmAddress based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MscVrPpAtmAddress_Type.__name__ = "HexString"
_MscVrPpAtmAddress_Object = MibTableColumn
mscVrPpAtmAddress = _MscVrPpAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 105, 1, 1),
    _MscVrPpAtmAddress_Type()
)
mscVrPpAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpAtmAddress.setStatus("mandatory")
_MscVrIfTableEntry_ObjectIdentity = ObjectIdentity
mscVrIfTableEntry = _MscVrIfTableEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10)
)
_MscVrIfTableEntryRowStatusTable_Object = MibTable
mscVrIfTableEntryRowStatusTable = _MscVrIfTableEntryRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 1)
)
if mibBuilder.loadTexts:
    mscVrIfTableEntryRowStatusTable.setStatus("mandatory")
_MscVrIfTableEntryRowStatusEntry_Object = MibTableRow
mscVrIfTableEntryRowStatusEntry = _MscVrIfTableEntryRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 1, 1)
)
mscVrIfTableEntryRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIfTableEntryIndex"),
)
if mibBuilder.loadTexts:
    mscVrIfTableEntryRowStatusEntry.setStatus("mandatory")
_MscVrIfTableEntryRowStatus_Type = RowStatus
_MscVrIfTableEntryRowStatus_Object = MibTableColumn
mscVrIfTableEntryRowStatus = _MscVrIfTableEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 1, 1, 1),
    _MscVrIfTableEntryRowStatus_Type()
)
mscVrIfTableEntryRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIfTableEntryRowStatus.setStatus("mandatory")
_MscVrIfTableEntryComponentName_Type = DisplayString
_MscVrIfTableEntryComponentName_Object = MibTableColumn
mscVrIfTableEntryComponentName = _MscVrIfTableEntryComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 1, 1, 2),
    _MscVrIfTableEntryComponentName_Type()
)
mscVrIfTableEntryComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIfTableEntryComponentName.setStatus("mandatory")
_MscVrIfTableEntryStorageType_Type = StorageType
_MscVrIfTableEntryStorageType_Object = MibTableColumn
mscVrIfTableEntryStorageType = _MscVrIfTableEntryStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 1, 1, 4),
    _MscVrIfTableEntryStorageType_Type()
)
mscVrIfTableEntryStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIfTableEntryStorageType.setStatus("mandatory")


class _MscVrIfTableEntryIndex_Type(Integer32):
    """Custom type mscVrIfTableEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrIfTableEntryIndex_Type.__name__ = "Integer32"
_MscVrIfTableEntryIndex_Object = MibTableColumn
mscVrIfTableEntryIndex = _MscVrIfTableEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 1, 1, 10),
    _MscVrIfTableEntryIndex_Type()
)
mscVrIfTableEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIfTableEntryIndex.setStatus("mandatory")
_MscVrIfTableEntryIftTable_Object = MibTable
mscVrIfTableEntryIftTable = _MscVrIfTableEntryIftTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10)
)
if mibBuilder.loadTexts:
    mscVrIfTableEntryIftTable.setStatus("mandatory")
_MscVrIfTableEntryIftEntry_Object = MibTableRow
mscVrIfTableEntryIftEntry = _MscVrIfTableEntryIftEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1)
)
mscVrIfTableEntryIftEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIfTableEntryIndex"),
)
if mibBuilder.loadTexts:
    mscVrIfTableEntryIftEntry.setStatus("mandatory")


class _MscVrIfTableEntryIfAdminStatus_Type(Integer32):
    """Custom type mscVrIfTableEntryIfAdminStatus based on Integer32"""
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


_MscVrIfTableEntryIfAdminStatus_Type.__name__ = "Integer32"
_MscVrIfTableEntryIfAdminStatus_Object = MibTableColumn
mscVrIfTableEntryIfAdminStatus = _MscVrIfTableEntryIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 2),
    _MscVrIfTableEntryIfAdminStatus_Type()
)
mscVrIfTableEntryIfAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIfTableEntryIfAdminStatus.setStatus("mandatory")


class _MscVrIfTableEntryIfOperStatus_Type(Integer32):
    """Custom type mscVrIfTableEntryIfOperStatus based on Integer32"""
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


_MscVrIfTableEntryIfOperStatus_Type.__name__ = "Integer32"
_MscVrIfTableEntryIfOperStatus_Object = MibTableColumn
mscVrIfTableEntryIfOperStatus = _MscVrIfTableEntryIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 3),
    _MscVrIfTableEntryIfOperStatus_Type()
)
mscVrIfTableEntryIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIfTableEntryIfOperStatus.setStatus("mandatory")


class _MscVrIfTableEntryIfLastChange_Type(Unsigned32):
    """Custom type mscVrIfTableEntryIfLastChange based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIfTableEntryIfLastChange_Type.__name__ = "Unsigned32"
_MscVrIfTableEntryIfLastChange_Object = MibTableColumn
mscVrIfTableEntryIfLastChange = _MscVrIfTableEntryIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 4),
    _MscVrIfTableEntryIfLastChange_Type()
)
mscVrIfTableEntryIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIfTableEntryIfLastChange.setStatus("mandatory")
_MscVrIfTableEntryIfInOctets_Type = Counter32
_MscVrIfTableEntryIfInOctets_Object = MibTableColumn
mscVrIfTableEntryIfInOctets = _MscVrIfTableEntryIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 5),
    _MscVrIfTableEntryIfInOctets_Type()
)
mscVrIfTableEntryIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIfTableEntryIfInOctets.setStatus("mandatory")
_MscVrIfTableEntryIfOutOctets_Type = Counter32
_MscVrIfTableEntryIfOutOctets_Object = MibTableColumn
mscVrIfTableEntryIfOutOctets = _MscVrIfTableEntryIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 6),
    _MscVrIfTableEntryIfOutOctets_Type()
)
mscVrIfTableEntryIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIfTableEntryIfOutOctets.setStatus("mandatory")
_MscVrIfTableEntryIfInDiscards_Type = Counter32
_MscVrIfTableEntryIfInDiscards_Object = MibTableColumn
mscVrIfTableEntryIfInDiscards = _MscVrIfTableEntryIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 7),
    _MscVrIfTableEntryIfInDiscards_Type()
)
mscVrIfTableEntryIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIfTableEntryIfInDiscards.setStatus("mandatory")
_MscVrIfTableEntryIfOutDiscards_Type = Counter32
_MscVrIfTableEntryIfOutDiscards_Object = MibTableColumn
mscVrIfTableEntryIfOutDiscards = _MscVrIfTableEntryIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 8),
    _MscVrIfTableEntryIfOutDiscards_Type()
)
mscVrIfTableEntryIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIfTableEntryIfOutDiscards.setStatus("mandatory")
_MscVrIfTableEntryIfInErrors_Type = Counter32
_MscVrIfTableEntryIfInErrors_Object = MibTableColumn
mscVrIfTableEntryIfInErrors = _MscVrIfTableEntryIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 9),
    _MscVrIfTableEntryIfInErrors_Type()
)
mscVrIfTableEntryIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIfTableEntryIfInErrors.setStatus("mandatory")
_MscVrIfTableEntryIfOutErrors_Type = Counter32
_MscVrIfTableEntryIfOutErrors_Object = MibTableColumn
mscVrIfTableEntryIfOutErrors = _MscVrIfTableEntryIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 10),
    _MscVrIfTableEntryIfOutErrors_Type()
)
mscVrIfTableEntryIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIfTableEntryIfOutErrors.setStatus("mandatory")
_MscVrIfTableEntryIfInUcastPkts_Type = Counter32
_MscVrIfTableEntryIfInUcastPkts_Object = MibTableColumn
mscVrIfTableEntryIfInUcastPkts = _MscVrIfTableEntryIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 11),
    _MscVrIfTableEntryIfInUcastPkts_Type()
)
mscVrIfTableEntryIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIfTableEntryIfInUcastPkts.setStatus("mandatory")
_MscVrIfTableEntryIfOutUcastPkts_Type = Counter32
_MscVrIfTableEntryIfOutUcastPkts_Object = MibTableColumn
mscVrIfTableEntryIfOutUcastPkts = _MscVrIfTableEntryIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 12),
    _MscVrIfTableEntryIfOutUcastPkts_Type()
)
mscVrIfTableEntryIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIfTableEntryIfOutUcastPkts.setStatus("mandatory")
_MscVrIfTableEntryIfInNuCastPkts_Type = Counter32
_MscVrIfTableEntryIfInNuCastPkts_Object = MibTableColumn
mscVrIfTableEntryIfInNuCastPkts = _MscVrIfTableEntryIfInNuCastPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 13),
    _MscVrIfTableEntryIfInNuCastPkts_Type()
)
mscVrIfTableEntryIfInNuCastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIfTableEntryIfInNuCastPkts.setStatus("mandatory")
_MscVrIfTableEntryIfOutNuCastPkts_Type = Counter32
_MscVrIfTableEntryIfOutNuCastPkts_Object = MibTableColumn
mscVrIfTableEntryIfOutNuCastPkts = _MscVrIfTableEntryIfOutNuCastPkts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 14),
    _MscVrIfTableEntryIfOutNuCastPkts_Type()
)
mscVrIfTableEntryIfOutNuCastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIfTableEntryIfOutNuCastPkts.setStatus("mandatory")
_MscVrIfTableEntryIfInUnknownProtos_Type = Counter32
_MscVrIfTableEntryIfInUnknownProtos_Object = MibTableColumn
mscVrIfTableEntryIfInUnknownProtos = _MscVrIfTableEntryIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 15),
    _MscVrIfTableEntryIfInUnknownProtos_Type()
)
mscVrIfTableEntryIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIfTableEntryIfInUnknownProtos.setStatus("mandatory")


class _MscVrIfTableEntryIfOutQlength_Type(Gauge32):
    """Custom type mscVrIfTableEntryIfOutQlength based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIfTableEntryIfOutQlength_Type.__name__ = "Gauge32"
_MscVrIfTableEntryIfOutQlength_Object = MibTableColumn
mscVrIfTableEntryIfOutQlength = _MscVrIfTableEntryIfOutQlength_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 16),
    _MscVrIfTableEntryIfOutQlength_Type()
)
mscVrIfTableEntryIfOutQlength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIfTableEntryIfOutQlength.setStatus("mandatory")


class _MscVrIfTableEntryIfDescription_Type(AsciiString):
    """Custom type mscVrIfTableEntryIfDescription based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscVrIfTableEntryIfDescription_Type.__name__ = "AsciiString"
_MscVrIfTableEntryIfDescription_Object = MibTableColumn
mscVrIfTableEntryIfDescription = _MscVrIfTableEntryIfDescription_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 17),
    _MscVrIfTableEntryIfDescription_Type()
)
mscVrIfTableEntryIfDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIfTableEntryIfDescription.setStatus("mandatory")


class _MscVrIfTableEntryIfType_Type(Integer32):
    """Custom type mscVrIfTableEntryIfType based on Integer32"""
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


_MscVrIfTableEntryIfType_Type.__name__ = "Integer32"
_MscVrIfTableEntryIfType_Object = MibTableColumn
mscVrIfTableEntryIfType = _MscVrIfTableEntryIfType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 18),
    _MscVrIfTableEntryIfType_Type()
)
mscVrIfTableEntryIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIfTableEntryIfType.setStatus("mandatory")


class _MscVrIfTableEntryIfMtu_Type(Unsigned32):
    """Custom type mscVrIfTableEntryIfMtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIfTableEntryIfMtu_Type.__name__ = "Unsigned32"
_MscVrIfTableEntryIfMtu_Object = MibTableColumn
mscVrIfTableEntryIfMtu = _MscVrIfTableEntryIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 19),
    _MscVrIfTableEntryIfMtu_Type()
)
mscVrIfTableEntryIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIfTableEntryIfMtu.setStatus("mandatory")


class _MscVrIfTableEntryIfSpeed_Type(Unsigned32):
    """Custom type mscVrIfTableEntryIfSpeed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIfTableEntryIfSpeed_Type.__name__ = "Unsigned32"
_MscVrIfTableEntryIfSpeed_Object = MibTableColumn
mscVrIfTableEntryIfSpeed = _MscVrIfTableEntryIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 20),
    _MscVrIfTableEntryIfSpeed_Type()
)
mscVrIfTableEntryIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIfTableEntryIfSpeed.setStatus("mandatory")


class _MscVrIfTableEntryIfPhysicalAddress_Type(AsciiString):
    """Custom type mscVrIfTableEntryIfPhysicalAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_MscVrIfTableEntryIfPhysicalAddress_Type.__name__ = "AsciiString"
_MscVrIfTableEntryIfPhysicalAddress_Object = MibTableColumn
mscVrIfTableEntryIfPhysicalAddress = _MscVrIfTableEntryIfPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 21),
    _MscVrIfTableEntryIfPhysicalAddress_Type()
)
mscVrIfTableEntryIfPhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIfTableEntryIfPhysicalAddress.setStatus("mandatory")
_MscVrIfTableEntryIfSpecific_Type = IntegerSequence
_MscVrIfTableEntryIfSpecific_Object = MibTableColumn
mscVrIfTableEntryIfSpecific = _MscVrIfTableEntryIfSpecific_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 10, 1, 22),
    _MscVrIfTableEntryIfSpecific_Type()
)
mscVrIfTableEntryIfSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIfTableEntryIfSpecific.setStatus("mandatory")
_MscVrIfTableEntryAdditionalInfoTable_Object = MibTable
mscVrIfTableEntryAdditionalInfoTable = _MscVrIfTableEntryAdditionalInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 11)
)
if mibBuilder.loadTexts:
    mscVrIfTableEntryAdditionalInfoTable.setStatus("mandatory")
_MscVrIfTableEntryAdditionalInfoEntry_Object = MibTableRow
mscVrIfTableEntryAdditionalInfoEntry = _MscVrIfTableEntryAdditionalInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 11, 1)
)
mscVrIfTableEntryAdditionalInfoEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIfTableEntryIndex"),
)
if mibBuilder.loadTexts:
    mscVrIfTableEntryAdditionalInfoEntry.setStatus("mandatory")
_MscVrIfTableEntryStdComponentName_Type = RowPointer
_MscVrIfTableEntryStdComponentName_Object = MibTableColumn
mscVrIfTableEntryStdComponentName = _MscVrIfTableEntryStdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 10, 11, 1, 1),
    _MscVrIfTableEntryStdComponentName_Type()
)
mscVrIfTableEntryStdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIfTableEntryStdComponentName.setStatus("mandatory")
_MscVrQosP_ObjectIdentity = ObjectIdentity
mscVrQosP = _MscVrQosP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 15)
)
_MscVrQosPRowStatusTable_Object = MibTable
mscVrQosPRowStatusTable = _MscVrQosPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 15, 1)
)
if mibBuilder.loadTexts:
    mscVrQosPRowStatusTable.setStatus("mandatory")
_MscVrQosPRowStatusEntry_Object = MibTableRow
mscVrQosPRowStatusEntry = _MscVrQosPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 15, 1, 1)
)
mscVrQosPRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrQosPIndex"),
)
if mibBuilder.loadTexts:
    mscVrQosPRowStatusEntry.setStatus("mandatory")
_MscVrQosPRowStatus_Type = RowStatus
_MscVrQosPRowStatus_Object = MibTableColumn
mscVrQosPRowStatus = _MscVrQosPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 15, 1, 1, 1),
    _MscVrQosPRowStatus_Type()
)
mscVrQosPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrQosPRowStatus.setStatus("mandatory")
_MscVrQosPComponentName_Type = DisplayString
_MscVrQosPComponentName_Object = MibTableColumn
mscVrQosPComponentName = _MscVrQosPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 15, 1, 1, 2),
    _MscVrQosPComponentName_Type()
)
mscVrQosPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrQosPComponentName.setStatus("mandatory")
_MscVrQosPStorageType_Type = StorageType
_MscVrQosPStorageType_Object = MibTableColumn
mscVrQosPStorageType = _MscVrQosPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 15, 1, 1, 4),
    _MscVrQosPStorageType_Type()
)
mscVrQosPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrQosPStorageType.setStatus("mandatory")


class _MscVrQosPIndex_Type(Integer32):
    """Custom type mscVrQosPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscVrQosPIndex_Type.__name__ = "Integer32"
_MscVrQosPIndex_Object = MibTableColumn
mscVrQosPIndex = _MscVrQosPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 15, 1, 1, 10),
    _MscVrQosPIndex_Type()
)
mscVrQosPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrQosPIndex.setStatus("mandatory")
_MscVrQosPProvTable_Object = MibTable
mscVrQosPProvTable = _MscVrQosPProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 15, 10)
)
if mibBuilder.loadTexts:
    mscVrQosPProvTable.setStatus("mandatory")
_MscVrQosPProvEntry_Object = MibTableRow
mscVrQosPProvEntry = _MscVrQosPProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 15, 10, 1)
)
mscVrQosPProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrQosPIndex"),
)
if mibBuilder.loadTexts:
    mscVrQosPProvEntry.setStatus("mandatory")


class _MscVrQosPVnsDiscardPriority_Type(Unsigned32):
    """Custom type mscVrQosPVnsDiscardPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MscVrQosPVnsDiscardPriority_Type.__name__ = "Unsigned32"
_MscVrQosPVnsDiscardPriority_Object = MibTableColumn
mscVrQosPVnsDiscardPriority = _MscVrQosPVnsDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 15, 10, 1, 1),
    _MscVrQosPVnsDiscardPriority_Type()
)
mscVrQosPVnsDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrQosPVnsDiscardPriority.setStatus("mandatory")


class _MscVrQosPVnsEmissionPriority_Type(Unsigned32):
    """Custom type mscVrQosPVnsEmissionPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_MscVrQosPVnsEmissionPriority_Type.__name__ = "Unsigned32"
_MscVrQosPVnsEmissionPriority_Object = MibTableColumn
mscVrQosPVnsEmissionPriority = _MscVrQosPVnsEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 15, 10, 1, 2),
    _MscVrQosPVnsEmissionPriority_Type()
)
mscVrQosPVnsEmissionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrQosPVnsEmissionPriority.setStatus("mandatory")


class _MscVrQosPWanEmissionPriority_Type(Unsigned32):
    """Custom type mscVrQosPWanEmissionPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_MscVrQosPWanEmissionPriority_Type.__name__ = "Unsigned32"
_MscVrQosPWanEmissionPriority_Object = MibTableColumn
mscVrQosPWanEmissionPriority = _MscVrQosPWanEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 15, 10, 1, 3),
    _MscVrQosPWanEmissionPriority_Type()
)
mscVrQosPWanEmissionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrQosPWanEmissionPriority.setStatus("mandatory")
_MscVrAdminContorlTable_Object = MibTable
mscVrAdminContorlTable = _MscVrAdminContorlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 100)
)
if mibBuilder.loadTexts:
    mscVrAdminContorlTable.setStatus("mandatory")
_MscVrAdminContorlEntry_Object = MibTableRow
mscVrAdminContorlEntry = _MscVrAdminContorlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 100, 1)
)
mscVrAdminContorlEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
)
if mibBuilder.loadTexts:
    mscVrAdminContorlEntry.setStatus("mandatory")


class _MscVrSnmpAdminStatus_Type(Integer32):
    """Custom type mscVrSnmpAdminStatus based on Integer32"""
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


_MscVrSnmpAdminStatus_Type.__name__ = "Integer32"
_MscVrSnmpAdminStatus_Object = MibTableColumn
mscVrSnmpAdminStatus = _MscVrSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 100, 1, 1),
    _MscVrSnmpAdminStatus_Type()
)
mscVrSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSnmpAdminStatus.setStatus("mandatory")


class _MscVrManagementAccess_Type(Integer32):
    """Custom type mscVrManagementAccess based on Integer32"""
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


_MscVrManagementAccess_Type.__name__ = "Integer32"
_MscVrManagementAccess_Object = MibTableColumn
mscVrManagementAccess = _MscVrManagementAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 100, 1, 2),
    _MscVrManagementAccess_Type()
)
mscVrManagementAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrManagementAccess.setStatus("mandatory")


class _MscVrVirtualPrivateIntranetIdentifier_Type(Integer32):
    """Custom type mscVrVirtualPrivateIntranetIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscVrVirtualPrivateIntranetIdentifier_Type.__name__ = "Integer32"
_MscVrVirtualPrivateIntranetIdentifier_Object = MibTableColumn
mscVrVirtualPrivateIntranetIdentifier = _MscVrVirtualPrivateIntranetIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 100, 1, 3),
    _MscVrVirtualPrivateIntranetIdentifier_Type()
)
mscVrVirtualPrivateIntranetIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrVirtualPrivateIntranetIdentifier.setStatus("mandatory")


class _MscVrVpnMode_Type(Integer32):
    """Custom type mscVrVpnMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("carrier", 1),
          ("customer", 0))
    )


_MscVrVpnMode_Type.__name__ = "Integer32"
_MscVrVpnMode_Object = MibTableColumn
mscVrVpnMode = _MscVrVpnMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 100, 1, 4),
    _MscVrVpnMode_Type()
)
mscVrVpnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrVpnMode.setStatus("mandatory")
_MscVrCidDataTable_Object = MibTable
mscVrCidDataTable = _MscVrCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 101)
)
if mibBuilder.loadTexts:
    mscVrCidDataTable.setStatus("mandatory")
_MscVrCidDataEntry_Object = MibTableRow
mscVrCidDataEntry = _MscVrCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 101, 1)
)
mscVrCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
)
if mibBuilder.loadTexts:
    mscVrCidDataEntry.setStatus("mandatory")


class _MscVrCustomerIdentifier_Type(Unsigned32):
    """Custom type mscVrCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscVrCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscVrCustomerIdentifier_Object = MibTableColumn
mscVrCustomerIdentifier = _MscVrCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 101, 1, 1),
    _MscVrCustomerIdentifier_Type()
)
mscVrCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrCustomerIdentifier.setStatus("mandatory")
_MscVrOperStatusTable_Object = MibTable
mscVrOperStatusTable = _MscVrOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 103)
)
if mibBuilder.loadTexts:
    mscVrOperStatusTable.setStatus("mandatory")
_MscVrOperStatusEntry_Object = MibTableRow
mscVrOperStatusEntry = _MscVrOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 103, 1)
)
mscVrOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
)
if mibBuilder.loadTexts:
    mscVrOperStatusEntry.setStatus("mandatory")


class _MscVrSnmpOperStatus_Type(Integer32):
    """Custom type mscVrSnmpOperStatus based on Integer32"""
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


_MscVrSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrSnmpOperStatus_Object = MibTableColumn
mscVrSnmpOperStatus = _MscVrSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 103, 1, 1),
    _MscVrSnmpOperStatus_Type()
)
mscVrSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSnmpOperStatus.setStatus("mandatory")
_MscVrStateTable_Object = MibTable
mscVrStateTable = _MscVrStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 104)
)
if mibBuilder.loadTexts:
    mscVrStateTable.setStatus("mandatory")
_MscVrStateEntry_Object = MibTableRow
mscVrStateEntry = _MscVrStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 104, 1)
)
mscVrStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
)
if mibBuilder.loadTexts:
    mscVrStateEntry.setStatus("mandatory")


class _MscVrAdminState_Type(Integer32):
    """Custom type mscVrAdminState based on Integer32"""
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


_MscVrAdminState_Type.__name__ = "Integer32"
_MscVrAdminState_Object = MibTableColumn
mscVrAdminState = _MscVrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 104, 1, 1),
    _MscVrAdminState_Type()
)
mscVrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrAdminState.setStatus("mandatory")


class _MscVrOperationalState_Type(Integer32):
    """Custom type mscVrOperationalState based on Integer32"""
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


_MscVrOperationalState_Type.__name__ = "Integer32"
_MscVrOperationalState_Object = MibTableColumn
mscVrOperationalState = _MscVrOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 104, 1, 2),
    _MscVrOperationalState_Type()
)
mscVrOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrOperationalState.setStatus("mandatory")


class _MscVrUsageState_Type(Integer32):
    """Custom type mscVrUsageState based on Integer32"""
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


_MscVrUsageState_Type.__name__ = "Integer32"
_MscVrUsageState_Object = MibTableColumn
mscVrUsageState = _MscVrUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 104, 1, 3),
    _MscVrUsageState_Type()
)
mscVrUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrUsageState.setStatus("mandatory")
_MscVrIfNumberOperTable_Object = MibTable
mscVrIfNumberOperTable = _MscVrIfNumberOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 105)
)
if mibBuilder.loadTexts:
    mscVrIfNumberOperTable.setStatus("mandatory")
_MscVrIfNumberOperEntry_Object = MibTableRow
mscVrIfNumberOperEntry = _MscVrIfNumberOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 105, 1)
)
mscVrIfNumberOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
)
if mibBuilder.loadTexts:
    mscVrIfNumberOperEntry.setStatus("mandatory")


class _MscVrIfNumber_Type(Unsigned32):
    """Custom type mscVrIfNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIfNumber_Type.__name__ = "Unsigned32"
_MscVrIfNumber_Object = MibTableColumn
mscVrIfNumber = _MscVrIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 105, 1, 1),
    _MscVrIfNumber_Type()
)
mscVrIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIfNumber.setStatus("mandatory")
_VirtualRouterMIB_ObjectIdentity = ObjectIdentity
virtualRouterMIB = _VirtualRouterMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 26)
)
_VirtualRouterGroup_ObjectIdentity = ObjectIdentity
virtualRouterGroup = _VirtualRouterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 26, 1)
)
_VirtualRouterGroupCA_ObjectIdentity = ObjectIdentity
virtualRouterGroupCA = _VirtualRouterGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 26, 1, 1)
)
_VirtualRouterGroupCA02_ObjectIdentity = ObjectIdentity
virtualRouterGroupCA02 = _VirtualRouterGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 26, 1, 1, 3)
)
_VirtualRouterGroupCA02A_ObjectIdentity = ObjectIdentity
virtualRouterGroupCA02A = _VirtualRouterGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 26, 1, 1, 3, 2)
)
_VirtualRouterCapabilities_ObjectIdentity = ObjectIdentity
virtualRouterCapabilities = _VirtualRouterCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 26, 3)
)
_VirtualRouterCapabilitiesCA_ObjectIdentity = ObjectIdentity
virtualRouterCapabilitiesCA = _VirtualRouterCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 26, 3, 1)
)
_VirtualRouterCapabilitiesCA02_ObjectIdentity = ObjectIdentity
virtualRouterCapabilitiesCA02 = _VirtualRouterCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 26, 3, 1, 3)
)
_VirtualRouterCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
virtualRouterCapabilitiesCA02A = _VirtualRouterCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 26, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-VirtualRouterMIB",
    **{"mscVr": mscVr,
       "mscVrRowStatusTable": mscVrRowStatusTable,
       "mscVrRowStatusEntry": mscVrRowStatusEntry,
       "mscVrRowStatus": mscVrRowStatus,
       "mscVrComponentName": mscVrComponentName,
       "mscVrStorageType": mscVrStorageType,
       "mscVrIndex": mscVrIndex,
       "mscVrMm": mscVrMm,
       "mscVrMmRowStatusTable": mscVrMmRowStatusTable,
       "mscVrMmRowStatusEntry": mscVrMmRowStatusEntry,
       "mscVrMmRowStatus": mscVrMmRowStatus,
       "mscVrMmComponentName": mscVrMmComponentName,
       "mscVrMmStorageType": mscVrMmStorageType,
       "mscVrMmIndex": mscVrMmIndex,
       "mscVrMmProvTable": mscVrMmProvTable,
       "mscVrMmProvEntry": mscVrMmProvEntry,
       "mscVrMmVrMaxHeapSpace": mscVrMmVrMaxHeapSpace,
       "mscVrMmIpMaxHeapSpace": mscVrMmIpMaxHeapSpace,
       "mscVrMmIpxMaxHeapSpace": mscVrMmIpxMaxHeapSpace,
       "mscVrMmBridgingMaxHeapSpace": mscVrMmBridgingMaxHeapSpace,
       "mscVrMmNetSentryMaxHeapSpace": mscVrMmNetSentryMaxHeapSpace,
       "mscVrMmSresMaxHeapSpace": mscVrMmSresMaxHeapSpace,
       "mscVrMmSnaMaxHeapSpace": mscVrMmSnaMaxHeapSpace,
       "mscVrMmOperTable": mscVrMmOperTable,
       "mscVrMmOperEntry": mscVrMmOperEntry,
       "mscVrMmVrHeapSpaceBytesAllocated": mscVrMmVrHeapSpaceBytesAllocated,
       "mscVrMmVrHeapSpaceAllocated": mscVrMmVrHeapSpaceAllocated,
       "mscVrMmIpHeapSpaceAllocated": mscVrMmIpHeapSpaceAllocated,
       "mscVrMmIpxHeapSpaceAllocated": mscVrMmIpxHeapSpaceAllocated,
       "mscVrMmBridgingHeapSpaceAllocated": mscVrMmBridgingHeapSpaceAllocated,
       "mscVrMmNetSentryHeapSpaceAllocated": mscVrMmNetSentryHeapSpaceAllocated,
       "mscVrMmSresHeapSpaceAllocated": mscVrMmSresHeapSpaceAllocated,
       "mscVrMmSnaHeapSpaceAllocated": mscVrMmSnaHeapSpaceAllocated,
       "mscVrPp": mscVrPp,
       "mscVrPpRowStatusTable": mscVrPpRowStatusTable,
       "mscVrPpRowStatusEntry": mscVrPpRowStatusEntry,
       "mscVrPpRowStatus": mscVrPpRowStatus,
       "mscVrPpComponentName": mscVrPpComponentName,
       "mscVrPpStorageType": mscVrPpStorageType,
       "mscVrPpIndex": mscVrPpIndex,
       "mscVrPpAdminControlTable": mscVrPpAdminControlTable,
       "mscVrPpAdminControlEntry": mscVrPpAdminControlEntry,
       "mscVrPpSnmpAdminStatus": mscVrPpSnmpAdminStatus,
       "mscVrPpProvTable": mscVrPpProvTable,
       "mscVrPpProvEntry": mscVrPpProvEntry,
       "mscVrPpLinkToMedia": mscVrPpLinkToMedia,
       "mscVrPpOperStatusTable": mscVrPpOperStatusTable,
       "mscVrPpOperStatusEntry": mscVrPpOperStatusEntry,
       "mscVrPpSnmpOperStatus": mscVrPpSnmpOperStatus,
       "mscVrPpStateTable": mscVrPpStateTable,
       "mscVrPpStateEntry": mscVrPpStateEntry,
       "mscVrPpAdminState": mscVrPpAdminState,
       "mscVrPpOperationalState": mscVrPpOperationalState,
       "mscVrPpUsageState": mscVrPpUsageState,
       "mscVrPpOperTable": mscVrPpOperTable,
       "mscVrPpOperEntry": mscVrPpOperEntry,
       "mscVrPpIfIndex": mscVrPpIfIndex,
       "mscVrPpNbmaAddressTable": mscVrPpNbmaAddressTable,
       "mscVrPpNbmaAddressEntry": mscVrPpNbmaAddressEntry,
       "mscVrPpAtmAddress": mscVrPpAtmAddress,
       "mscVrIfTableEntry": mscVrIfTableEntry,
       "mscVrIfTableEntryRowStatusTable": mscVrIfTableEntryRowStatusTable,
       "mscVrIfTableEntryRowStatusEntry": mscVrIfTableEntryRowStatusEntry,
       "mscVrIfTableEntryRowStatus": mscVrIfTableEntryRowStatus,
       "mscVrIfTableEntryComponentName": mscVrIfTableEntryComponentName,
       "mscVrIfTableEntryStorageType": mscVrIfTableEntryStorageType,
       "mscVrIfTableEntryIndex": mscVrIfTableEntryIndex,
       "mscVrIfTableEntryIftTable": mscVrIfTableEntryIftTable,
       "mscVrIfTableEntryIftEntry": mscVrIfTableEntryIftEntry,
       "mscVrIfTableEntryIfAdminStatus": mscVrIfTableEntryIfAdminStatus,
       "mscVrIfTableEntryIfOperStatus": mscVrIfTableEntryIfOperStatus,
       "mscVrIfTableEntryIfLastChange": mscVrIfTableEntryIfLastChange,
       "mscVrIfTableEntryIfInOctets": mscVrIfTableEntryIfInOctets,
       "mscVrIfTableEntryIfOutOctets": mscVrIfTableEntryIfOutOctets,
       "mscVrIfTableEntryIfInDiscards": mscVrIfTableEntryIfInDiscards,
       "mscVrIfTableEntryIfOutDiscards": mscVrIfTableEntryIfOutDiscards,
       "mscVrIfTableEntryIfInErrors": mscVrIfTableEntryIfInErrors,
       "mscVrIfTableEntryIfOutErrors": mscVrIfTableEntryIfOutErrors,
       "mscVrIfTableEntryIfInUcastPkts": mscVrIfTableEntryIfInUcastPkts,
       "mscVrIfTableEntryIfOutUcastPkts": mscVrIfTableEntryIfOutUcastPkts,
       "mscVrIfTableEntryIfInNuCastPkts": mscVrIfTableEntryIfInNuCastPkts,
       "mscVrIfTableEntryIfOutNuCastPkts": mscVrIfTableEntryIfOutNuCastPkts,
       "mscVrIfTableEntryIfInUnknownProtos": mscVrIfTableEntryIfInUnknownProtos,
       "mscVrIfTableEntryIfOutQlength": mscVrIfTableEntryIfOutQlength,
       "mscVrIfTableEntryIfDescription": mscVrIfTableEntryIfDescription,
       "mscVrIfTableEntryIfType": mscVrIfTableEntryIfType,
       "mscVrIfTableEntryIfMtu": mscVrIfTableEntryIfMtu,
       "mscVrIfTableEntryIfSpeed": mscVrIfTableEntryIfSpeed,
       "mscVrIfTableEntryIfPhysicalAddress": mscVrIfTableEntryIfPhysicalAddress,
       "mscVrIfTableEntryIfSpecific": mscVrIfTableEntryIfSpecific,
       "mscVrIfTableEntryAdditionalInfoTable": mscVrIfTableEntryAdditionalInfoTable,
       "mscVrIfTableEntryAdditionalInfoEntry": mscVrIfTableEntryAdditionalInfoEntry,
       "mscVrIfTableEntryStdComponentName": mscVrIfTableEntryStdComponentName,
       "mscVrQosP": mscVrQosP,
       "mscVrQosPRowStatusTable": mscVrQosPRowStatusTable,
       "mscVrQosPRowStatusEntry": mscVrQosPRowStatusEntry,
       "mscVrQosPRowStatus": mscVrQosPRowStatus,
       "mscVrQosPComponentName": mscVrQosPComponentName,
       "mscVrQosPStorageType": mscVrQosPStorageType,
       "mscVrQosPIndex": mscVrQosPIndex,
       "mscVrQosPProvTable": mscVrQosPProvTable,
       "mscVrQosPProvEntry": mscVrQosPProvEntry,
       "mscVrQosPVnsDiscardPriority": mscVrQosPVnsDiscardPriority,
       "mscVrQosPVnsEmissionPriority": mscVrQosPVnsEmissionPriority,
       "mscVrQosPWanEmissionPriority": mscVrQosPWanEmissionPriority,
       "mscVrAdminContorlTable": mscVrAdminContorlTable,
       "mscVrAdminContorlEntry": mscVrAdminContorlEntry,
       "mscVrSnmpAdminStatus": mscVrSnmpAdminStatus,
       "mscVrManagementAccess": mscVrManagementAccess,
       "mscVrVirtualPrivateIntranetIdentifier": mscVrVirtualPrivateIntranetIdentifier,
       "mscVrVpnMode": mscVrVpnMode,
       "mscVrCidDataTable": mscVrCidDataTable,
       "mscVrCidDataEntry": mscVrCidDataEntry,
       "mscVrCustomerIdentifier": mscVrCustomerIdentifier,
       "mscVrOperStatusTable": mscVrOperStatusTable,
       "mscVrOperStatusEntry": mscVrOperStatusEntry,
       "mscVrSnmpOperStatus": mscVrSnmpOperStatus,
       "mscVrStateTable": mscVrStateTable,
       "mscVrStateEntry": mscVrStateEntry,
       "mscVrAdminState": mscVrAdminState,
       "mscVrOperationalState": mscVrOperationalState,
       "mscVrUsageState": mscVrUsageState,
       "mscVrIfNumberOperTable": mscVrIfNumberOperTable,
       "mscVrIfNumberOperEntry": mscVrIfNumberOperEntry,
       "mscVrIfNumber": mscVrIfNumber,
       "virtualRouterMIB": virtualRouterMIB,
       "virtualRouterGroup": virtualRouterGroup,
       "virtualRouterGroupCA": virtualRouterGroupCA,
       "virtualRouterGroupCA02": virtualRouterGroupCA02,
       "virtualRouterGroupCA02A": virtualRouterGroupCA02A,
       "virtualRouterCapabilities": virtualRouterCapabilities,
       "virtualRouterCapabilitiesCA": virtualRouterCapabilitiesCA,
       "virtualRouterCapabilitiesCA02": virtualRouterCapabilitiesCA02,
       "virtualRouterCapabilitiesCA02A": virtualRouterCapabilitiesCA02A}
)
