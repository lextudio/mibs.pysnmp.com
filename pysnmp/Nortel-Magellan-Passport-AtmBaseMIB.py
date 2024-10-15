# SNMP MIB module (Nortel-Magellan-Passport-AtmBaseMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-AtmBaseMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:15 2024
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

(lp,
 lpEng,
 lpEngIndex,
 lpIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-LogicalProcessorMIB",
    "lp",
    "lpEng",
    "lpEngIndex",
    "lpIndex")

(DisplayString,
 Gauge32,
 Integer32,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(FixedPoint1,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "FixedPoint1",
    "NonReplicated")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
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

_LpArc_ObjectIdentity = ObjectIdentity
lpArc = _LpArc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 19)
)
_LpArcRowStatusTable_Object = MibTable
lpArcRowStatusTable = _LpArcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 19, 1)
)
if mibBuilder.loadTexts:
    lpArcRowStatusTable.setStatus("obsolete")
_LpArcRowStatusEntry_Object = MibTableRow
lpArcRowStatusEntry = _LpArcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 19, 1, 1)
)
lpArcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpArcIndex"),
)
if mibBuilder.loadTexts:
    lpArcRowStatusEntry.setStatus("obsolete")
_LpArcRowStatus_Type = RowStatus
_LpArcRowStatus_Object = MibTableColumn
lpArcRowStatus = _LpArcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 19, 1, 1, 1),
    _LpArcRowStatus_Type()
)
lpArcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpArcRowStatus.setStatus("obsolete")
_LpArcComponentName_Type = DisplayString
_LpArcComponentName_Object = MibTableColumn
lpArcComponentName = _LpArcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 19, 1, 1, 2),
    _LpArcComponentName_Type()
)
lpArcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpArcComponentName.setStatus("obsolete")
_LpArcStorageType_Type = StorageType
_LpArcStorageType_Object = MibTableColumn
lpArcStorageType = _LpArcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 19, 1, 1, 4),
    _LpArcStorageType_Type()
)
lpArcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpArcStorageType.setStatus("obsolete")
_LpArcIndex_Type = NonReplicated
_LpArcIndex_Object = MibTableColumn
lpArcIndex = _LpArcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 19, 1, 1, 10),
    _LpArcIndex_Type()
)
lpArcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpArcIndex.setStatus("obsolete")
_LpArcProvTable_Object = MibTable
lpArcProvTable = _LpArcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 19, 100)
)
if mibBuilder.loadTexts:
    lpArcProvTable.setStatus("obsolete")
_LpArcProvEntry_Object = MibTableRow
lpArcProvEntry = _LpArcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 19, 100, 1)
)
lpArcProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpArcIndex"),
)
if mibBuilder.loadTexts:
    lpArcProvEntry.setStatus("obsolete")


class _LpArcTotalConnectionPoolCapacity_Type(Unsigned32):
    """Custom type lpArcTotalConnectionPoolCapacity based on Unsigned32"""
    defaultValue = 3072

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10752),
    )


_LpArcTotalConnectionPoolCapacity_Type.__name__ = "Unsigned32"
_LpArcTotalConnectionPoolCapacity_Object = MibTableColumn
lpArcTotalConnectionPoolCapacity = _LpArcTotalConnectionPoolCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 19, 100, 1, 5),
    _LpArcTotalConnectionPoolCapacity_Type()
)
lpArcTotalConnectionPoolCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpArcTotalConnectionPoolCapacity.setStatus("obsolete")


class _LpArcMulticastBranchesCapacity_Type(Unsigned32):
    """Custom type lpArcMulticastBranchesCapacity based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10752),
    )


_LpArcMulticastBranchesCapacity_Type.__name__ = "Unsigned32"
_LpArcMulticastBranchesCapacity_Object = MibTableColumn
lpArcMulticastBranchesCapacity = _LpArcMulticastBranchesCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 19, 100, 1, 6),
    _LpArcMulticastBranchesCapacity_Type()
)
lpArcMulticastBranchesCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpArcMulticastBranchesCapacity.setStatus("obsolete")


class _LpArcTxFrameMemoryAllocation_Type(Unsigned32):
    """Custom type lpArcTxFrameMemoryAllocation based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpArcTxFrameMemoryAllocation_Type.__name__ = "Unsigned32"
_LpArcTxFrameMemoryAllocation_Object = MibTableColumn
lpArcTxFrameMemoryAllocation = _LpArcTxFrameMemoryAllocation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 19, 100, 1, 10),
    _LpArcTxFrameMemoryAllocation_Type()
)
lpArcTxFrameMemoryAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpArcTxFrameMemoryAllocation.setStatus("obsolete")


class _LpArcRxFrameMemoryAllocation_Type(Unsigned32):
    """Custom type lpArcRxFrameMemoryAllocation based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpArcRxFrameMemoryAllocation_Type.__name__ = "Unsigned32"
_LpArcRxFrameMemoryAllocation_Object = MibTableColumn
lpArcRxFrameMemoryAllocation = _LpArcRxFrameMemoryAllocation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 19, 100, 1, 20),
    _LpArcRxFrameMemoryAllocation_Type()
)
lpArcRxFrameMemoryAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpArcRxFrameMemoryAllocation.setStatus("obsolete")


class _LpArcPerVcQueueInterfaces_Type(Unsigned32):
    """Custom type lpArcPerVcQueueInterfaces based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_LpArcPerVcQueueInterfaces_Type.__name__ = "Unsigned32"
_LpArcPerVcQueueInterfaces_Object = MibTableColumn
lpArcPerVcQueueInterfaces = _LpArcPerVcQueueInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 19, 100, 1, 25),
    _LpArcPerVcQueueInterfaces_Type()
)
lpArcPerVcQueueInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpArcPerVcQueueInterfaces.setStatus("obsolete")


class _LpArcShapingStackAllocation_Type(OctetString):
    """Custom type lpArcShapingStackAllocation based on OctetString"""
    defaultHexValue = "80"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpArcShapingStackAllocation_Type.__name__ = "OctetString"
_LpArcShapingStackAllocation_Object = MibTableColumn
lpArcShapingStackAllocation = _LpArcShapingStackAllocation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 19, 100, 1, 30),
    _LpArcShapingStackAllocation_Type()
)
lpArcShapingStackAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpArcShapingStackAllocation.setStatus("obsolete")


class _LpArcShapingScalingFactor_Type(FixedPoint1):
    """Custom type lpArcShapingScalingFactor based on FixedPoint1"""
    defaultValue = 10

    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(14, 14),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(28, 28),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(56, 56),
    )


_LpArcShapingScalingFactor_Type.__name__ = "FixedPoint1"
_LpArcShapingScalingFactor_Object = MibTableColumn
lpArcShapingScalingFactor = _LpArcShapingScalingFactor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 19, 100, 1, 40),
    _LpArcShapingScalingFactor_Type()
)
lpArcShapingScalingFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpArcShapingScalingFactor.setStatus("obsolete")


class _LpArcCdvAttenuation_Type(Integer32):
    """Custom type lpArcCdvAttenuation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LpArcCdvAttenuation_Type.__name__ = "Integer32"
_LpArcCdvAttenuation_Object = MibTableColumn
lpArcCdvAttenuation = _LpArcCdvAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 19, 100, 1, 41),
    _LpArcCdvAttenuation_Type()
)
lpArcCdvAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpArcCdvAttenuation.setStatus("obsolete")


class _LpArcPortAggregation_Type(Integer32):
    """Custom type lpArcPortAggregation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_LpArcPortAggregation_Type.__name__ = "Integer32"
_LpArcPortAggregation_Object = MibTableColumn
lpArcPortAggregation = _LpArcPortAggregation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 19, 100, 1, 42),
    _LpArcPortAggregation_Type()
)
lpArcPortAggregation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpArcPortAggregation.setStatus("obsolete")


class _LpArcSubConnectionPoolCapacity_Type(Unsigned32):
    """Custom type lpArcSubConnectionPoolCapacity based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_LpArcSubConnectionPoolCapacity_Type.__name__ = "Unsigned32"
_LpArcSubConnectionPoolCapacity_Object = MibTableColumn
lpArcSubConnectionPoolCapacity = _LpArcSubConnectionPoolCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 19, 100, 1, 43),
    _LpArcSubConnectionPoolCapacity_Type()
)
lpArcSubConnectionPoolCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpArcSubConnectionPoolCapacity.setStatus("obsolete")


class _LpArcLnnConnectionPoolCapacity_Type(Unsigned32):
    """Custom type lpArcLnnConnectionPoolCapacity based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_LpArcLnnConnectionPoolCapacity_Type.__name__ = "Unsigned32"
_LpArcLnnConnectionPoolCapacity_Object = MibTableColumn
lpArcLnnConnectionPoolCapacity = _LpArcLnnConnectionPoolCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 19, 100, 1, 44),
    _LpArcLnnConnectionPoolCapacity_Type()
)
lpArcLnnConnectionPoolCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpArcLnnConnectionPoolCapacity.setStatus("obsolete")
_LpArcConnCapTable_Object = MibTable
lpArcConnCapTable = _LpArcConnCapTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 19, 291)
)
if mibBuilder.loadTexts:
    lpArcConnCapTable.setStatus("obsolete")
_LpArcConnCapEntry_Object = MibTableRow
lpArcConnCapEntry = _LpArcConnCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 19, 291, 1)
)
lpArcConnCapEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpArcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpArcConnCapIndex"),
)
if mibBuilder.loadTexts:
    lpArcConnCapEntry.setStatus("obsolete")


class _LpArcConnCapIndex_Type(Integer32):
    """Custom type lpArcConnCapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_LpArcConnCapIndex_Type.__name__ = "Integer32"
_LpArcConnCapIndex_Object = MibTableColumn
lpArcConnCapIndex = _LpArcConnCapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 19, 291, 1, 1),
    _LpArcConnCapIndex_Type()
)
lpArcConnCapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpArcConnCapIndex.setStatus("obsolete")


class _LpArcConnCapValue_Type(Unsigned32):
    """Custom type lpArcConnCapValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 4096),
    )


_LpArcConnCapValue_Type.__name__ = "Unsigned32"
_LpArcConnCapValue_Object = MibTableColumn
lpArcConnCapValue = _LpArcConnCapValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 19, 291, 1, 2),
    _LpArcConnCapValue_Type()
)
lpArcConnCapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpArcConnCapValue.setStatus("obsolete")
_LpAru_ObjectIdentity = ObjectIdentity
lpAru = _LpAru_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20)
)
_LpAruRowStatusTable_Object = MibTable
lpAruRowStatusTable = _LpAruRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 1)
)
if mibBuilder.loadTexts:
    lpAruRowStatusTable.setStatus("obsolete")
_LpAruRowStatusEntry_Object = MibTableRow
lpAruRowStatusEntry = _LpAruRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 1, 1)
)
lpAruRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpAruIndex"),
)
if mibBuilder.loadTexts:
    lpAruRowStatusEntry.setStatus("obsolete")
_LpAruRowStatus_Type = RowStatus
_LpAruRowStatus_Object = MibTableColumn
lpAruRowStatus = _LpAruRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 1, 1, 1),
    _LpAruRowStatus_Type()
)
lpAruRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruRowStatus.setStatus("obsolete")
_LpAruComponentName_Type = DisplayString
_LpAruComponentName_Object = MibTableColumn
lpAruComponentName = _LpAruComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 1, 1, 2),
    _LpAruComponentName_Type()
)
lpAruComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruComponentName.setStatus("obsolete")
_LpAruStorageType_Type = StorageType
_LpAruStorageType_Object = MibTableColumn
lpAruStorageType = _LpAruStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 1, 1, 4),
    _LpAruStorageType_Type()
)
lpAruStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruStorageType.setStatus("obsolete")
_LpAruIndex_Type = NonReplicated
_LpAruIndex_Object = MibTableColumn
lpAruIndex = _LpAruIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 1, 1, 10),
    _LpAruIndex_Type()
)
lpAruIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpAruIndex.setStatus("obsolete")
_LpAruOperTable_Object = MibTable
lpAruOperTable = _LpAruOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 100)
)
if mibBuilder.loadTexts:
    lpAruOperTable.setStatus("obsolete")
_LpAruOperEntry_Object = MibTableRow
lpAruOperEntry = _LpAruOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 100, 1)
)
lpAruOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpAruIndex"),
)
if mibBuilder.loadTexts:
    lpAruOperEntry.setStatus("obsolete")


class _LpAruTotalConnectionPoolUsage_Type(Unsigned32):
    """Custom type lpAruTotalConnectionPoolUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10752),
    )


_LpAruTotalConnectionPoolUsage_Type.__name__ = "Unsigned32"
_LpAruTotalConnectionPoolUsage_Object = MibTableColumn
lpAruTotalConnectionPoolUsage = _LpAruTotalConnectionPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 100, 1, 5),
    _LpAruTotalConnectionPoolUsage_Type()
)
lpAruTotalConnectionPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruTotalConnectionPoolUsage.setStatus("obsolete")


class _LpAruMulticastBranchesUsage_Type(Unsigned32):
    """Custom type lpAruMulticastBranchesUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10752),
    )


_LpAruMulticastBranchesUsage_Type.__name__ = "Unsigned32"
_LpAruMulticastBranchesUsage_Object = MibTableColumn
lpAruMulticastBranchesUsage = _LpAruMulticastBranchesUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 100, 1, 6),
    _LpAruMulticastBranchesUsage_Type()
)
lpAruMulticastBranchesUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruMulticastBranchesUsage.setStatus("obsolete")


class _LpAruTxCellBlockCapacity_Type(Unsigned32):
    """Custom type lpAruTxCellBlockCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_LpAruTxCellBlockCapacity_Type.__name__ = "Unsigned32"
_LpAruTxCellBlockCapacity_Object = MibTableColumn
lpAruTxCellBlockCapacity = _LpAruTxCellBlockCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 100, 1, 10),
    _LpAruTxCellBlockCapacity_Type()
)
lpAruTxCellBlockCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruTxCellBlockCapacity.setStatus("obsolete")


class _LpAruTxCellBlockUsage_Type(Gauge32):
    """Custom type lpAruTxCellBlockUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_LpAruTxCellBlockUsage_Type.__name__ = "Gauge32"
_LpAruTxCellBlockUsage_Object = MibTableColumn
lpAruTxCellBlockUsage = _LpAruTxCellBlockUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 100, 1, 20),
    _LpAruTxCellBlockUsage_Type()
)
lpAruTxCellBlockUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruTxCellBlockUsage.setStatus("obsolete")


class _LpAruTxCellFreeListSize_Type(Unsigned32):
    """Custom type lpAruTxCellFreeListSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_LpAruTxCellFreeListSize_Type.__name__ = "Unsigned32"
_LpAruTxCellFreeListSize_Object = MibTableColumn
lpAruTxCellFreeListSize = _LpAruTxCellFreeListSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 100, 1, 23),
    _LpAruTxCellFreeListSize_Type()
)
lpAruTxCellFreeListSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruTxCellFreeListSize.setStatus("obsolete")


class _LpAruTxCellFreeListCongestionState_Type(Integer32):
    """Custom type lpAruTxCellFreeListCongestionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_LpAruTxCellFreeListCongestionState_Type.__name__ = "Integer32"
_LpAruTxCellFreeListCongestionState_Object = MibTableColumn
lpAruTxCellFreeListCongestionState = _LpAruTxCellFreeListCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 100, 1, 26),
    _LpAruTxCellFreeListCongestionState_Type()
)
lpAruTxCellFreeListCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruTxCellFreeListCongestionState.setStatus("obsolete")


class _LpAruTxFrameMemoryAllocation_Type(Unsigned32):
    """Custom type lpAruTxFrameMemoryAllocation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpAruTxFrameMemoryAllocation_Type.__name__ = "Unsigned32"
_LpAruTxFrameMemoryAllocation_Object = MibTableColumn
lpAruTxFrameMemoryAllocation = _LpAruTxFrameMemoryAllocation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 100, 1, 30),
    _LpAruTxFrameMemoryAllocation_Type()
)
lpAruTxFrameMemoryAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruTxFrameMemoryAllocation.setStatus("obsolete")


class _LpAruTxFrameBlockCapacity_Type(Unsigned32):
    """Custom type lpAruTxFrameBlockCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_LpAruTxFrameBlockCapacity_Type.__name__ = "Unsigned32"
_LpAruTxFrameBlockCapacity_Object = MibTableColumn
lpAruTxFrameBlockCapacity = _LpAruTxFrameBlockCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 100, 1, 40),
    _LpAruTxFrameBlockCapacity_Type()
)
lpAruTxFrameBlockCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruTxFrameBlockCapacity.setStatus("obsolete")


class _LpAruTxFrameBlockUsage_Type(Gauge32):
    """Custom type lpAruTxFrameBlockUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_LpAruTxFrameBlockUsage_Type.__name__ = "Gauge32"
_LpAruTxFrameBlockUsage_Object = MibTableColumn
lpAruTxFrameBlockUsage = _LpAruTxFrameBlockUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 100, 1, 50),
    _LpAruTxFrameBlockUsage_Type()
)
lpAruTxFrameBlockUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruTxFrameBlockUsage.setStatus("obsolete")


class _LpAruTxFrameFreeListSize_Type(Unsigned32):
    """Custom type lpAruTxFrameFreeListSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_LpAruTxFrameFreeListSize_Type.__name__ = "Unsigned32"
_LpAruTxFrameFreeListSize_Object = MibTableColumn
lpAruTxFrameFreeListSize = _LpAruTxFrameFreeListSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 100, 1, 53),
    _LpAruTxFrameFreeListSize_Type()
)
lpAruTxFrameFreeListSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruTxFrameFreeListSize.setStatus("obsolete")


class _LpAruTxFrameFreeListCongestionState_Type(Integer32):
    """Custom type lpAruTxFrameFreeListCongestionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_LpAruTxFrameFreeListCongestionState_Type.__name__ = "Integer32"
_LpAruTxFrameFreeListCongestionState_Object = MibTableColumn
lpAruTxFrameFreeListCongestionState = _LpAruTxFrameFreeListCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 100, 1, 56),
    _LpAruTxFrameFreeListCongestionState_Type()
)
lpAruTxFrameFreeListCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruTxFrameFreeListCongestionState.setStatus("obsolete")


class _LpAruRxCellBlockCapacity_Type(Unsigned32):
    """Custom type lpAruRxCellBlockCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_LpAruRxCellBlockCapacity_Type.__name__ = "Unsigned32"
_LpAruRxCellBlockCapacity_Object = MibTableColumn
lpAruRxCellBlockCapacity = _LpAruRxCellBlockCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 100, 1, 60),
    _LpAruRxCellBlockCapacity_Type()
)
lpAruRxCellBlockCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruRxCellBlockCapacity.setStatus("obsolete")


class _LpAruRxCellBlockUsage_Type(Gauge32):
    """Custom type lpAruRxCellBlockUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_LpAruRxCellBlockUsage_Type.__name__ = "Gauge32"
_LpAruRxCellBlockUsage_Object = MibTableColumn
lpAruRxCellBlockUsage = _LpAruRxCellBlockUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 100, 1, 70),
    _LpAruRxCellBlockUsage_Type()
)
lpAruRxCellBlockUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruRxCellBlockUsage.setStatus("obsolete")


class _LpAruRxCellFreeListSize_Type(Unsigned32):
    """Custom type lpAruRxCellFreeListSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_LpAruRxCellFreeListSize_Type.__name__ = "Unsigned32"
_LpAruRxCellFreeListSize_Object = MibTableColumn
lpAruRxCellFreeListSize = _LpAruRxCellFreeListSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 100, 1, 73),
    _LpAruRxCellFreeListSize_Type()
)
lpAruRxCellFreeListSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruRxCellFreeListSize.setStatus("obsolete")


class _LpAruRxCellFreeListCongestionState_Type(Integer32):
    """Custom type lpAruRxCellFreeListCongestionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_LpAruRxCellFreeListCongestionState_Type.__name__ = "Integer32"
_LpAruRxCellFreeListCongestionState_Object = MibTableColumn
lpAruRxCellFreeListCongestionState = _LpAruRxCellFreeListCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 100, 1, 76),
    _LpAruRxCellFreeListCongestionState_Type()
)
lpAruRxCellFreeListCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruRxCellFreeListCongestionState.setStatus("obsolete")


class _LpAruRxFrameMemoryAllocation_Type(Unsigned32):
    """Custom type lpAruRxFrameMemoryAllocation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpAruRxFrameMemoryAllocation_Type.__name__ = "Unsigned32"
_LpAruRxFrameMemoryAllocation_Object = MibTableColumn
lpAruRxFrameMemoryAllocation = _LpAruRxFrameMemoryAllocation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 100, 1, 80),
    _LpAruRxFrameMemoryAllocation_Type()
)
lpAruRxFrameMemoryAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruRxFrameMemoryAllocation.setStatus("obsolete")


class _LpAruRxFrameBlockCapacity_Type(Unsigned32):
    """Custom type lpAruRxFrameBlockCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_LpAruRxFrameBlockCapacity_Type.__name__ = "Unsigned32"
_LpAruRxFrameBlockCapacity_Object = MibTableColumn
lpAruRxFrameBlockCapacity = _LpAruRxFrameBlockCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 100, 1, 90),
    _LpAruRxFrameBlockCapacity_Type()
)
lpAruRxFrameBlockCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruRxFrameBlockCapacity.setStatus("obsolete")


class _LpAruRxFrameBlockUsage_Type(Gauge32):
    """Custom type lpAruRxFrameBlockUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_LpAruRxFrameBlockUsage_Type.__name__ = "Gauge32"
_LpAruRxFrameBlockUsage_Object = MibTableColumn
lpAruRxFrameBlockUsage = _LpAruRxFrameBlockUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 100, 1, 100),
    _LpAruRxFrameBlockUsage_Type()
)
lpAruRxFrameBlockUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruRxFrameBlockUsage.setStatus("obsolete")


class _LpAruRxFrameFreeListSize_Type(Unsigned32):
    """Custom type lpAruRxFrameFreeListSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_LpAruRxFrameFreeListSize_Type.__name__ = "Unsigned32"
_LpAruRxFrameFreeListSize_Object = MibTableColumn
lpAruRxFrameFreeListSize = _LpAruRxFrameFreeListSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 100, 1, 103),
    _LpAruRxFrameFreeListSize_Type()
)
lpAruRxFrameFreeListSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruRxFrameFreeListSize.setStatus("obsolete")


class _LpAruRxFrameFreeListCongestionState_Type(Integer32):
    """Custom type lpAruRxFrameFreeListCongestionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_LpAruRxFrameFreeListCongestionState_Type.__name__ = "Integer32"
_LpAruRxFrameFreeListCongestionState_Object = MibTableColumn
lpAruRxFrameFreeListCongestionState = _LpAruRxFrameFreeListCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 100, 1, 106),
    _LpAruRxFrameFreeListCongestionState_Type()
)
lpAruRxFrameFreeListCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruRxFrameFreeListCongestionState.setStatus("obsolete")


class _LpAruSubConnectionPoolAvailable_Type(Unsigned32):
    """Custom type lpAruSubConnectionPoolAvailable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_LpAruSubConnectionPoolAvailable_Type.__name__ = "Unsigned32"
_LpAruSubConnectionPoolAvailable_Object = MibTableColumn
lpAruSubConnectionPoolAvailable = _LpAruSubConnectionPoolAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 100, 1, 107),
    _LpAruSubConnectionPoolAvailable_Type()
)
lpAruSubConnectionPoolAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruSubConnectionPoolAvailable.setStatus("obsolete")


class _LpAruSubConnectionPoolUsage_Type(Unsigned32):
    """Custom type lpAruSubConnectionPoolUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_LpAruSubConnectionPoolUsage_Type.__name__ = "Unsigned32"
_LpAruSubConnectionPoolUsage_Object = MibTableColumn
lpAruSubConnectionPoolUsage = _LpAruSubConnectionPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 100, 1, 108),
    _LpAruSubConnectionPoolUsage_Type()
)
lpAruSubConnectionPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruSubConnectionPoolUsage.setStatus("obsolete")


class _LpAruLnnConnectionPoolAvailable_Type(Unsigned32):
    """Custom type lpAruLnnConnectionPoolAvailable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_LpAruLnnConnectionPoolAvailable_Type.__name__ = "Unsigned32"
_LpAruLnnConnectionPoolAvailable_Object = MibTableColumn
lpAruLnnConnectionPoolAvailable = _LpAruLnnConnectionPoolAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 100, 1, 109),
    _LpAruLnnConnectionPoolAvailable_Type()
)
lpAruLnnConnectionPoolAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruLnnConnectionPoolAvailable.setStatus("obsolete")


class _LpAruLnnConnectionPoolUsage_Type(Unsigned32):
    """Custom type lpAruLnnConnectionPoolUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_LpAruLnnConnectionPoolUsage_Type.__name__ = "Unsigned32"
_LpAruLnnConnectionPoolUsage_Object = MibTableColumn
lpAruLnnConnectionPoolUsage = _LpAruLnnConnectionPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 100, 1, 110),
    _LpAruLnnConnectionPoolUsage_Type()
)
lpAruLnnConnectionPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruLnnConnectionPoolUsage.setStatus("obsolete")
_LpAruConnUsageTable_Object = MibTable
lpAruConnUsageTable = _LpAruConnUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 292)
)
if mibBuilder.loadTexts:
    lpAruConnUsageTable.setStatus("obsolete")
_LpAruConnUsageEntry_Object = MibTableRow
lpAruConnUsageEntry = _LpAruConnUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 292, 1)
)
lpAruConnUsageEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpAruIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpAruConnUsageIndex"),
)
if mibBuilder.loadTexts:
    lpAruConnUsageEntry.setStatus("obsolete")


class _LpAruConnUsageIndex_Type(Integer32):
    """Custom type lpAruConnUsageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_LpAruConnUsageIndex_Type.__name__ = "Integer32"
_LpAruConnUsageIndex_Object = MibTableColumn
lpAruConnUsageIndex = _LpAruConnUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 292, 1, 1),
    _LpAruConnUsageIndex_Type()
)
lpAruConnUsageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpAruConnUsageIndex.setStatus("obsolete")


class _LpAruConnUsageValue_Type(Unsigned32):
    """Custom type lpAruConnUsageValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000),
    )


_LpAruConnUsageValue_Type.__name__ = "Unsigned32"
_LpAruConnUsageValue_Object = MibTableColumn
lpAruConnUsageValue = _LpAruConnUsageValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 292, 1, 2),
    _LpAruConnUsageValue_Type()
)
lpAruConnUsageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruConnUsageValue.setStatus("obsolete")
_LpAruTxCflThreshTable_Object = MibTable
lpAruTxCflThreshTable = _LpAruTxCflThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 353)
)
if mibBuilder.loadTexts:
    lpAruTxCflThreshTable.setStatus("obsolete")
_LpAruTxCflThreshEntry_Object = MibTableRow
lpAruTxCflThreshEntry = _LpAruTxCflThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 353, 1)
)
lpAruTxCflThreshEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpAruIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpAruTxCflThreshIndex"),
)
if mibBuilder.loadTexts:
    lpAruTxCflThreshEntry.setStatus("obsolete")


class _LpAruTxCflThreshIndex_Type(Integer32):
    """Custom type lpAruTxCflThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_LpAruTxCflThreshIndex_Type.__name__ = "Integer32"
_LpAruTxCflThreshIndex_Object = MibTableColumn
lpAruTxCflThreshIndex = _LpAruTxCflThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 353, 1, 1),
    _LpAruTxCflThreshIndex_Type()
)
lpAruTxCflThreshIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpAruTxCflThreshIndex.setStatus("obsolete")


class _LpAruTxCflThreshValue_Type(Unsigned32):
    """Custom type lpAruTxCflThreshValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_LpAruTxCflThreshValue_Type.__name__ = "Unsigned32"
_LpAruTxCflThreshValue_Object = MibTableColumn
lpAruTxCflThreshValue = _LpAruTxCflThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 353, 1, 2),
    _LpAruTxCflThreshValue_Type()
)
lpAruTxCflThreshValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruTxCflThreshValue.setStatus("obsolete")
_LpAruTxFflThreshTable_Object = MibTable
lpAruTxFflThreshTable = _LpAruTxFflThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 354)
)
if mibBuilder.loadTexts:
    lpAruTxFflThreshTable.setStatus("obsolete")
_LpAruTxFflThreshEntry_Object = MibTableRow
lpAruTxFflThreshEntry = _LpAruTxFflThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 354, 1)
)
lpAruTxFflThreshEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpAruIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpAruTxFflThreshIndex"),
)
if mibBuilder.loadTexts:
    lpAruTxFflThreshEntry.setStatus("obsolete")


class _LpAruTxFflThreshIndex_Type(Integer32):
    """Custom type lpAruTxFflThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_LpAruTxFflThreshIndex_Type.__name__ = "Integer32"
_LpAruTxFflThreshIndex_Object = MibTableColumn
lpAruTxFflThreshIndex = _LpAruTxFflThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 354, 1, 1),
    _LpAruTxFflThreshIndex_Type()
)
lpAruTxFflThreshIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpAruTxFflThreshIndex.setStatus("obsolete")


class _LpAruTxFflThreshValue_Type(Unsigned32):
    """Custom type lpAruTxFflThreshValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_LpAruTxFflThreshValue_Type.__name__ = "Unsigned32"
_LpAruTxFflThreshValue_Object = MibTableColumn
lpAruTxFflThreshValue = _LpAruTxFflThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 354, 1, 2),
    _LpAruTxFflThreshValue_Type()
)
lpAruTxFflThreshValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruTxFflThreshValue.setStatus("obsolete")
_LpAruRxCflThreshTable_Object = MibTable
lpAruRxCflThreshTable = _LpAruRxCflThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 355)
)
if mibBuilder.loadTexts:
    lpAruRxCflThreshTable.setStatus("obsolete")
_LpAruRxCflThreshEntry_Object = MibTableRow
lpAruRxCflThreshEntry = _LpAruRxCflThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 355, 1)
)
lpAruRxCflThreshEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpAruIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpAruRxCflThreshIndex"),
)
if mibBuilder.loadTexts:
    lpAruRxCflThreshEntry.setStatus("obsolete")


class _LpAruRxCflThreshIndex_Type(Integer32):
    """Custom type lpAruRxCflThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_LpAruRxCflThreshIndex_Type.__name__ = "Integer32"
_LpAruRxCflThreshIndex_Object = MibTableColumn
lpAruRxCflThreshIndex = _LpAruRxCflThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 355, 1, 1),
    _LpAruRxCflThreshIndex_Type()
)
lpAruRxCflThreshIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpAruRxCflThreshIndex.setStatus("obsolete")


class _LpAruRxCflThreshValue_Type(Unsigned32):
    """Custom type lpAruRxCflThreshValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_LpAruRxCflThreshValue_Type.__name__ = "Unsigned32"
_LpAruRxCflThreshValue_Object = MibTableColumn
lpAruRxCflThreshValue = _LpAruRxCflThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 355, 1, 2),
    _LpAruRxCflThreshValue_Type()
)
lpAruRxCflThreshValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruRxCflThreshValue.setStatus("obsolete")
_LpAruRxFflThreshTable_Object = MibTable
lpAruRxFflThreshTable = _LpAruRxFflThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 356)
)
if mibBuilder.loadTexts:
    lpAruRxFflThreshTable.setStatus("obsolete")
_LpAruRxFflThreshEntry_Object = MibTableRow
lpAruRxFflThreshEntry = _LpAruRxFflThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 356, 1)
)
lpAruRxFflThreshEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpAruIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpAruRxFflThreshIndex"),
)
if mibBuilder.loadTexts:
    lpAruRxFflThreshEntry.setStatus("obsolete")


class _LpAruRxFflThreshIndex_Type(Integer32):
    """Custom type lpAruRxFflThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_LpAruRxFflThreshIndex_Type.__name__ = "Integer32"
_LpAruRxFflThreshIndex_Object = MibTableColumn
lpAruRxFflThreshIndex = _LpAruRxFflThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 356, 1, 1),
    _LpAruRxFflThreshIndex_Type()
)
lpAruRxFflThreshIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpAruRxFflThreshIndex.setStatus("obsolete")


class _LpAruRxFflThreshValue_Type(Unsigned32):
    """Custom type lpAruRxFflThreshValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_LpAruRxFflThreshValue_Type.__name__ = "Unsigned32"
_LpAruRxFflThreshValue_Object = MibTableColumn
lpAruRxFflThreshValue = _LpAruRxFflThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 20, 356, 1, 2),
    _LpAruRxFflThreshValue_Type()
)
lpAruRxFflThreshValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAruRxFflThreshValue.setStatus("obsolete")
_LpEngArc_ObjectIdentity = ObjectIdentity
lpEngArc = _LpEngArc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5)
)
_LpEngArcRowStatusTable_Object = MibTable
lpEngArcRowStatusTable = _LpEngArcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 1)
)
if mibBuilder.loadTexts:
    lpEngArcRowStatusTable.setStatus("mandatory")
_LpEngArcRowStatusEntry_Object = MibTableRow
lpEngArcRowStatusEntry = _LpEngArcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 1, 1)
)
lpEngArcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcIndex"),
)
if mibBuilder.loadTexts:
    lpEngArcRowStatusEntry.setStatus("mandatory")
_LpEngArcRowStatus_Type = RowStatus
_LpEngArcRowStatus_Object = MibTableColumn
lpEngArcRowStatus = _LpEngArcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 1, 1, 1),
    _LpEngArcRowStatus_Type()
)
lpEngArcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngArcRowStatus.setStatus("mandatory")
_LpEngArcComponentName_Type = DisplayString
_LpEngArcComponentName_Object = MibTableColumn
lpEngArcComponentName = _LpEngArcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 1, 1, 2),
    _LpEngArcComponentName_Type()
)
lpEngArcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcComponentName.setStatus("mandatory")
_LpEngArcStorageType_Type = StorageType
_LpEngArcStorageType_Object = MibTableColumn
lpEngArcStorageType = _LpEngArcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 1, 1, 4),
    _LpEngArcStorageType_Type()
)
lpEngArcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcStorageType.setStatus("mandatory")
_LpEngArcIndex_Type = NonReplicated
_LpEngArcIndex_Object = MibTableColumn
lpEngArcIndex = _LpEngArcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 1, 1, 10),
    _LpEngArcIndex_Type()
)
lpEngArcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEngArcIndex.setStatus("mandatory")
_LpEngArcOv_ObjectIdentity = ObjectIdentity
lpEngArcOv = _LpEngArcOv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 2)
)
_LpEngArcOvRowStatusTable_Object = MibTable
lpEngArcOvRowStatusTable = _LpEngArcOvRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 2, 1)
)
if mibBuilder.loadTexts:
    lpEngArcOvRowStatusTable.setStatus("mandatory")
_LpEngArcOvRowStatusEntry_Object = MibTableRow
lpEngArcOvRowStatusEntry = _LpEngArcOvRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 2, 1, 1)
)
lpEngArcOvRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcOvIndex"),
)
if mibBuilder.loadTexts:
    lpEngArcOvRowStatusEntry.setStatus("mandatory")
_LpEngArcOvRowStatus_Type = RowStatus
_LpEngArcOvRowStatus_Object = MibTableColumn
lpEngArcOvRowStatus = _LpEngArcOvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 2, 1, 1, 1),
    _LpEngArcOvRowStatus_Type()
)
lpEngArcOvRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngArcOvRowStatus.setStatus("mandatory")
_LpEngArcOvComponentName_Type = DisplayString
_LpEngArcOvComponentName_Object = MibTableColumn
lpEngArcOvComponentName = _LpEngArcOvComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 2, 1, 1, 2),
    _LpEngArcOvComponentName_Type()
)
lpEngArcOvComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcOvComponentName.setStatus("mandatory")
_LpEngArcOvStorageType_Type = StorageType
_LpEngArcOvStorageType_Object = MibTableColumn
lpEngArcOvStorageType = _LpEngArcOvStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 2, 1, 1, 4),
    _LpEngArcOvStorageType_Type()
)
lpEngArcOvStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcOvStorageType.setStatus("mandatory")
_LpEngArcOvIndex_Type = NonReplicated
_LpEngArcOvIndex_Object = MibTableColumn
lpEngArcOvIndex = _LpEngArcOvIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 2, 1, 1, 10),
    _LpEngArcOvIndex_Type()
)
lpEngArcOvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEngArcOvIndex.setStatus("mandatory")
_LpEngArcOvProvTable_Object = MibTable
lpEngArcOvProvTable = _LpEngArcOvProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 2, 10)
)
if mibBuilder.loadTexts:
    lpEngArcOvProvTable.setStatus("mandatory")
_LpEngArcOvProvEntry_Object = MibTableRow
lpEngArcOvProvEntry = _LpEngArcOvProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 2, 10, 1)
)
lpEngArcOvProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcOvIndex"),
)
if mibBuilder.loadTexts:
    lpEngArcOvProvEntry.setStatus("mandatory")


class _LpEngArcOvTotalConnectionPoolCapacity_Type(Unsigned32):
    """Custom type lpEngArcOvTotalConnectionPoolCapacity based on Unsigned32"""
    defaultValue = 3072

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_LpEngArcOvTotalConnectionPoolCapacity_Type.__name__ = "Unsigned32"
_LpEngArcOvTotalConnectionPoolCapacity_Object = MibTableColumn
lpEngArcOvTotalConnectionPoolCapacity = _LpEngArcOvTotalConnectionPoolCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 2, 10, 1, 1),
    _LpEngArcOvTotalConnectionPoolCapacity_Type()
)
lpEngArcOvTotalConnectionPoolCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngArcOvTotalConnectionPoolCapacity.setStatus("mandatory")


class _LpEngArcOvMulticastBranchesCapacity_Type(Unsigned32):
    """Custom type lpEngArcOvMulticastBranchesCapacity based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_LpEngArcOvMulticastBranchesCapacity_Type.__name__ = "Unsigned32"
_LpEngArcOvMulticastBranchesCapacity_Object = MibTableColumn
lpEngArcOvMulticastBranchesCapacity = _LpEngArcOvMulticastBranchesCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 2, 10, 1, 2),
    _LpEngArcOvMulticastBranchesCapacity_Type()
)
lpEngArcOvMulticastBranchesCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngArcOvMulticastBranchesCapacity.setStatus("mandatory")


class _LpEngArcOvTxCellMemoryAllocation_Type(Unsigned32):
    """Custom type lpEngArcOvTxCellMemoryAllocation based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_LpEngArcOvTxCellMemoryAllocation_Type.__name__ = "Unsigned32"
_LpEngArcOvTxCellMemoryAllocation_Object = MibTableColumn
lpEngArcOvTxCellMemoryAllocation = _LpEngArcOvTxCellMemoryAllocation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 2, 10, 1, 3),
    _LpEngArcOvTxCellMemoryAllocation_Type()
)
lpEngArcOvTxCellMemoryAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngArcOvTxCellMemoryAllocation.setStatus("mandatory")


class _LpEngArcOvRxCellMemoryAllocation_Type(Unsigned32):
    """Custom type lpEngArcOvRxCellMemoryAllocation based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_LpEngArcOvRxCellMemoryAllocation_Type.__name__ = "Unsigned32"
_LpEngArcOvRxCellMemoryAllocation_Object = MibTableColumn
lpEngArcOvRxCellMemoryAllocation = _LpEngArcOvRxCellMemoryAllocation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 2, 10, 1, 4),
    _LpEngArcOvRxCellMemoryAllocation_Type()
)
lpEngArcOvRxCellMemoryAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngArcOvRxCellMemoryAllocation.setStatus("mandatory")
_LpEngArcCqc_ObjectIdentity = ObjectIdentity
lpEngArcCqc = _LpEngArcCqc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3)
)
_LpEngArcCqcRowStatusTable_Object = MibTable
lpEngArcCqcRowStatusTable = _LpEngArcCqcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3, 1)
)
if mibBuilder.loadTexts:
    lpEngArcCqcRowStatusTable.setStatus("mandatory")
_LpEngArcCqcRowStatusEntry_Object = MibTableRow
lpEngArcCqcRowStatusEntry = _LpEngArcCqcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3, 1, 1)
)
lpEngArcCqcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcCqcIndex"),
)
if mibBuilder.loadTexts:
    lpEngArcCqcRowStatusEntry.setStatus("mandatory")
_LpEngArcCqcRowStatus_Type = RowStatus
_LpEngArcCqcRowStatus_Object = MibTableColumn
lpEngArcCqcRowStatus = _LpEngArcCqcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3, 1, 1, 1),
    _LpEngArcCqcRowStatus_Type()
)
lpEngArcCqcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngArcCqcRowStatus.setStatus("mandatory")
_LpEngArcCqcComponentName_Type = DisplayString
_LpEngArcCqcComponentName_Object = MibTableColumn
lpEngArcCqcComponentName = _LpEngArcCqcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3, 1, 1, 2),
    _LpEngArcCqcComponentName_Type()
)
lpEngArcCqcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcCqcComponentName.setStatus("mandatory")
_LpEngArcCqcStorageType_Type = StorageType
_LpEngArcCqcStorageType_Object = MibTableColumn
lpEngArcCqcStorageType = _LpEngArcCqcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3, 1, 1, 4),
    _LpEngArcCqcStorageType_Type()
)
lpEngArcCqcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcCqcStorageType.setStatus("mandatory")
_LpEngArcCqcIndex_Type = NonReplicated
_LpEngArcCqcIndex_Object = MibTableColumn
lpEngArcCqcIndex = _LpEngArcCqcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3, 1, 1, 10),
    _LpEngArcCqcIndex_Type()
)
lpEngArcCqcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEngArcCqcIndex.setStatus("mandatory")
_LpEngArcCqcOv_ObjectIdentity = ObjectIdentity
lpEngArcCqcOv = _LpEngArcCqcOv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3, 2)
)
_LpEngArcCqcOvRowStatusTable_Object = MibTable
lpEngArcCqcOvRowStatusTable = _LpEngArcCqcOvRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3, 2, 1)
)
if mibBuilder.loadTexts:
    lpEngArcCqcOvRowStatusTable.setStatus("mandatory")
_LpEngArcCqcOvRowStatusEntry_Object = MibTableRow
lpEngArcCqcOvRowStatusEntry = _LpEngArcCqcOvRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3, 2, 1, 1)
)
lpEngArcCqcOvRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcCqcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcCqcOvIndex"),
)
if mibBuilder.loadTexts:
    lpEngArcCqcOvRowStatusEntry.setStatus("mandatory")
_LpEngArcCqcOvRowStatus_Type = RowStatus
_LpEngArcCqcOvRowStatus_Object = MibTableColumn
lpEngArcCqcOvRowStatus = _LpEngArcCqcOvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3, 2, 1, 1, 1),
    _LpEngArcCqcOvRowStatus_Type()
)
lpEngArcCqcOvRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcCqcOvRowStatus.setStatus("mandatory")
_LpEngArcCqcOvComponentName_Type = DisplayString
_LpEngArcCqcOvComponentName_Object = MibTableColumn
lpEngArcCqcOvComponentName = _LpEngArcCqcOvComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3, 2, 1, 1, 2),
    _LpEngArcCqcOvComponentName_Type()
)
lpEngArcCqcOvComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcCqcOvComponentName.setStatus("mandatory")
_LpEngArcCqcOvStorageType_Type = StorageType
_LpEngArcCqcOvStorageType_Object = MibTableColumn
lpEngArcCqcOvStorageType = _LpEngArcCqcOvStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3, 2, 1, 1, 4),
    _LpEngArcCqcOvStorageType_Type()
)
lpEngArcCqcOvStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcCqcOvStorageType.setStatus("mandatory")
_LpEngArcCqcOvIndex_Type = NonReplicated
_LpEngArcCqcOvIndex_Object = MibTableColumn
lpEngArcCqcOvIndex = _LpEngArcCqcOvIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3, 2, 1, 1, 10),
    _LpEngArcCqcOvIndex_Type()
)
lpEngArcCqcOvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEngArcCqcOvIndex.setStatus("mandatory")
_LpEngArcCqcOvProvTable_Object = MibTable
lpEngArcCqcOvProvTable = _LpEngArcCqcOvProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3, 2, 10)
)
if mibBuilder.loadTexts:
    lpEngArcCqcOvProvTable.setStatus("mandatory")
_LpEngArcCqcOvProvEntry_Object = MibTableRow
lpEngArcCqcOvProvEntry = _LpEngArcCqcOvProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3, 2, 10, 1)
)
lpEngArcCqcOvProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcCqcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcCqcOvIndex"),
)
if mibBuilder.loadTexts:
    lpEngArcCqcOvProvEntry.setStatus("mandatory")


class _LpEngArcCqcOvPerVcQueueInterfaces_Type(Unsigned32):
    """Custom type lpEngArcCqcOvPerVcQueueInterfaces based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_LpEngArcCqcOvPerVcQueueInterfaces_Type.__name__ = "Unsigned32"
_LpEngArcCqcOvPerVcQueueInterfaces_Object = MibTableColumn
lpEngArcCqcOvPerVcQueueInterfaces = _LpEngArcCqcOvPerVcQueueInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3, 2, 10, 1, 1),
    _LpEngArcCqcOvPerVcQueueInterfaces_Type()
)
lpEngArcCqcOvPerVcQueueInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngArcCqcOvPerVcQueueInterfaces.setStatus("mandatory")


class _LpEngArcCqcOvShapingScalingFactor_Type(FixedPoint1):
    """Custom type lpEngArcCqcOvShapingScalingFactor based on FixedPoint1"""
    defaultValue = 10

    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(14, 14),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(28, 28),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(56, 56),
    )


_LpEngArcCqcOvShapingScalingFactor_Type.__name__ = "FixedPoint1"
_LpEngArcCqcOvShapingScalingFactor_Object = MibTableColumn
lpEngArcCqcOvShapingScalingFactor = _LpEngArcCqcOvShapingScalingFactor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3, 2, 10, 1, 2),
    _LpEngArcCqcOvShapingScalingFactor_Type()
)
lpEngArcCqcOvShapingScalingFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngArcCqcOvShapingScalingFactor.setStatus("mandatory")


class _LpEngArcCqcOvCdvReduction_Type(Integer32):
    """Custom type lpEngArcCqcOvCdvReduction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cardDependent", 2),
          ("disabled", 0),
          ("enabled", 1))
    )


_LpEngArcCqcOvCdvReduction_Type.__name__ = "Integer32"
_LpEngArcCqcOvCdvReduction_Object = MibTableColumn
lpEngArcCqcOvCdvReduction = _LpEngArcCqcOvCdvReduction_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3, 2, 10, 1, 3),
    _LpEngArcCqcOvCdvReduction_Type()
)
lpEngArcCqcOvCdvReduction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngArcCqcOvCdvReduction.setStatus("mandatory")


class _LpEngArcCqcOvPortCongestionPolicy_Type(Integer32):
    """Custom type lpEngArcCqcOvPortCongestionPolicy based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aggregate", 0),
          ("individualQueue", 1))
    )


_LpEngArcCqcOvPortCongestionPolicy_Type.__name__ = "Integer32"
_LpEngArcCqcOvPortCongestionPolicy_Object = MibTableColumn
lpEngArcCqcOvPortCongestionPolicy = _LpEngArcCqcOvPortCongestionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3, 2, 10, 1, 4),
    _LpEngArcCqcOvPortCongestionPolicy_Type()
)
lpEngArcCqcOvPortCongestionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngArcCqcOvPortCongestionPolicy.setStatus("mandatory")
_LpEngArcCqcOvConnCapTable_Object = MibTable
lpEngArcCqcOvConnCapTable = _LpEngArcCqcOvConnCapTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3, 2, 450)
)
if mibBuilder.loadTexts:
    lpEngArcCqcOvConnCapTable.setStatus("mandatory")
_LpEngArcCqcOvConnCapEntry_Object = MibTableRow
lpEngArcCqcOvConnCapEntry = _LpEngArcCqcOvConnCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3, 2, 450, 1)
)
lpEngArcCqcOvConnCapEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcCqcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcCqcOvIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcCqcOvConnCapIndex"),
)
if mibBuilder.loadTexts:
    lpEngArcCqcOvConnCapEntry.setStatus("mandatory")


class _LpEngArcCqcOvConnCapIndex_Type(Integer32):
    """Custom type lpEngArcCqcOvConnCapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_LpEngArcCqcOvConnCapIndex_Type.__name__ = "Integer32"
_LpEngArcCqcOvConnCapIndex_Object = MibTableColumn
lpEngArcCqcOvConnCapIndex = _LpEngArcCqcOvConnCapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3, 2, 450, 1, 1),
    _LpEngArcCqcOvConnCapIndex_Type()
)
lpEngArcCqcOvConnCapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEngArcCqcOvConnCapIndex.setStatus("mandatory")


class _LpEngArcCqcOvConnCapValue_Type(Unsigned32):
    """Custom type lpEngArcCqcOvConnCapValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 4096),
    )


_LpEngArcCqcOvConnCapValue_Type.__name__ = "Unsigned32"
_LpEngArcCqcOvConnCapValue_Object = MibTableColumn
lpEngArcCqcOvConnCapValue = _LpEngArcCqcOvConnCapValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3, 2, 450, 1, 2),
    _LpEngArcCqcOvConnCapValue_Type()
)
lpEngArcCqcOvConnCapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngArcCqcOvConnCapValue.setStatus("mandatory")
_LpEngArcCqcOperTable_Object = MibTable
lpEngArcCqcOperTable = _LpEngArcCqcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3, 10)
)
if mibBuilder.loadTexts:
    lpEngArcCqcOperTable.setStatus("mandatory")
_LpEngArcCqcOperEntry_Object = MibTableRow
lpEngArcCqcOperEntry = _LpEngArcCqcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3, 10, 1)
)
lpEngArcCqcOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcCqcIndex"),
)
if mibBuilder.loadTexts:
    lpEngArcCqcOperEntry.setStatus("mandatory")


class _LpEngArcCqcCdvReduction_Type(Integer32):
    """Custom type lpEngArcCqcCdvReduction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cardDependent", 2),
          ("disabled", 0),
          ("enabled", 1))
    )


_LpEngArcCqcCdvReduction_Type.__name__ = "Integer32"
_LpEngArcCqcCdvReduction_Object = MibTableColumn
lpEngArcCqcCdvReduction = _LpEngArcCqcCdvReduction_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 3, 10, 1, 1),
    _LpEngArcCqcCdvReduction_Type()
)
lpEngArcCqcCdvReduction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcCqcCdvReduction.setStatus("mandatory")
_LpEngArcAqm_ObjectIdentity = ObjectIdentity
lpEngArcAqm = _LpEngArcAqm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4)
)
_LpEngArcAqmRowStatusTable_Object = MibTable
lpEngArcAqmRowStatusTable = _LpEngArcAqmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 1)
)
if mibBuilder.loadTexts:
    lpEngArcAqmRowStatusTable.setStatus("mandatory")
_LpEngArcAqmRowStatusEntry_Object = MibTableRow
lpEngArcAqmRowStatusEntry = _LpEngArcAqmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 1, 1)
)
lpEngArcAqmRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcAqmIndex"),
)
if mibBuilder.loadTexts:
    lpEngArcAqmRowStatusEntry.setStatus("mandatory")
_LpEngArcAqmRowStatus_Type = RowStatus
_LpEngArcAqmRowStatus_Object = MibTableColumn
lpEngArcAqmRowStatus = _LpEngArcAqmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 1, 1, 1),
    _LpEngArcAqmRowStatus_Type()
)
lpEngArcAqmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngArcAqmRowStatus.setStatus("mandatory")
_LpEngArcAqmComponentName_Type = DisplayString
_LpEngArcAqmComponentName_Object = MibTableColumn
lpEngArcAqmComponentName = _LpEngArcAqmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 1, 1, 2),
    _LpEngArcAqmComponentName_Type()
)
lpEngArcAqmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcAqmComponentName.setStatus("mandatory")
_LpEngArcAqmStorageType_Type = StorageType
_LpEngArcAqmStorageType_Object = MibTableColumn
lpEngArcAqmStorageType = _LpEngArcAqmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 1, 1, 4),
    _LpEngArcAqmStorageType_Type()
)
lpEngArcAqmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcAqmStorageType.setStatus("mandatory")


class _LpEngArcAqmIndex_Type(Integer32):
    """Custom type lpEngArcAqmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_LpEngArcAqmIndex_Type.__name__ = "Integer32"
_LpEngArcAqmIndex_Object = MibTableColumn
lpEngArcAqmIndex = _LpEngArcAqmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 1, 1, 10),
    _LpEngArcAqmIndex_Type()
)
lpEngArcAqmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEngArcAqmIndex.setStatus("mandatory")
_LpEngArcAqmOv_ObjectIdentity = ObjectIdentity
lpEngArcAqmOv = _LpEngArcAqmOv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 2)
)
_LpEngArcAqmOvRowStatusTable_Object = MibTable
lpEngArcAqmOvRowStatusTable = _LpEngArcAqmOvRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 2, 1)
)
if mibBuilder.loadTexts:
    lpEngArcAqmOvRowStatusTable.setStatus("mandatory")
_LpEngArcAqmOvRowStatusEntry_Object = MibTableRow
lpEngArcAqmOvRowStatusEntry = _LpEngArcAqmOvRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 2, 1, 1)
)
lpEngArcAqmOvRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcAqmIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcAqmOvIndex"),
)
if mibBuilder.loadTexts:
    lpEngArcAqmOvRowStatusEntry.setStatus("mandatory")
_LpEngArcAqmOvRowStatus_Type = RowStatus
_LpEngArcAqmOvRowStatus_Object = MibTableColumn
lpEngArcAqmOvRowStatus = _LpEngArcAqmOvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 2, 1, 1, 1),
    _LpEngArcAqmOvRowStatus_Type()
)
lpEngArcAqmOvRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcAqmOvRowStatus.setStatus("mandatory")
_LpEngArcAqmOvComponentName_Type = DisplayString
_LpEngArcAqmOvComponentName_Object = MibTableColumn
lpEngArcAqmOvComponentName = _LpEngArcAqmOvComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 2, 1, 1, 2),
    _LpEngArcAqmOvComponentName_Type()
)
lpEngArcAqmOvComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcAqmOvComponentName.setStatus("mandatory")
_LpEngArcAqmOvStorageType_Type = StorageType
_LpEngArcAqmOvStorageType_Object = MibTableColumn
lpEngArcAqmOvStorageType = _LpEngArcAqmOvStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 2, 1, 1, 4),
    _LpEngArcAqmOvStorageType_Type()
)
lpEngArcAqmOvStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcAqmOvStorageType.setStatus("mandatory")
_LpEngArcAqmOvIndex_Type = NonReplicated
_LpEngArcAqmOvIndex_Object = MibTableColumn
lpEngArcAqmOvIndex = _LpEngArcAqmOvIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 2, 1, 1, 10),
    _LpEngArcAqmOvIndex_Type()
)
lpEngArcAqmOvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEngArcAqmOvIndex.setStatus("mandatory")
_LpEngArcAqmOvProvTable_Object = MibTable
lpEngArcAqmOvProvTable = _LpEngArcAqmOvProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 2, 10)
)
if mibBuilder.loadTexts:
    lpEngArcAqmOvProvTable.setStatus("mandatory")
_LpEngArcAqmOvProvEntry_Object = MibTableRow
lpEngArcAqmOvProvEntry = _LpEngArcAqmOvProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 2, 10, 1)
)
lpEngArcAqmOvProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcAqmIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcAqmOvIndex"),
)
if mibBuilder.loadTexts:
    lpEngArcAqmOvProvEntry.setStatus("mandatory")


class _LpEngArcAqmOvConnectionPoolCapacity_Type(Unsigned32):
    """Custom type lpEngArcAqmOvConnectionPoolCapacity based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16000),
    )


_LpEngArcAqmOvConnectionPoolCapacity_Type.__name__ = "Unsigned32"
_LpEngArcAqmOvConnectionPoolCapacity_Object = MibTableColumn
lpEngArcAqmOvConnectionPoolCapacity = _LpEngArcAqmOvConnectionPoolCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 2, 10, 1, 1),
    _LpEngArcAqmOvConnectionPoolCapacity_Type()
)
lpEngArcAqmOvConnectionPoolCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngArcAqmOvConnectionPoolCapacity.setStatus("mandatory")


class _LpEngArcAqmOvHighPriorityEpdOffset_Type(Unsigned32):
    """Custom type lpEngArcAqmOvHighPriorityEpdOffset based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1024),
    )


_LpEngArcAqmOvHighPriorityEpdOffset_Type.__name__ = "Unsigned32"
_LpEngArcAqmOvHighPriorityEpdOffset_Object = MibTableColumn
lpEngArcAqmOvHighPriorityEpdOffset = _LpEngArcAqmOvHighPriorityEpdOffset_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 2, 10, 1, 2),
    _LpEngArcAqmOvHighPriorityEpdOffset_Type()
)
lpEngArcAqmOvHighPriorityEpdOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngArcAqmOvHighPriorityEpdOffset.setStatus("mandatory")


class _LpEngArcAqmOvLowPriorityEpdOffset_Type(Unsigned32):
    """Custom type lpEngArcAqmOvLowPriorityEpdOffset based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1024),
    )


_LpEngArcAqmOvLowPriorityEpdOffset_Type.__name__ = "Unsigned32"
_LpEngArcAqmOvLowPriorityEpdOffset_Object = MibTableColumn
lpEngArcAqmOvLowPriorityEpdOffset = _LpEngArcAqmOvLowPriorityEpdOffset_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 2, 10, 1, 3),
    _LpEngArcAqmOvLowPriorityEpdOffset_Type()
)
lpEngArcAqmOvLowPriorityEpdOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngArcAqmOvLowPriorityEpdOffset.setStatus("mandatory")


class _LpEngArcAqmOvPortCongestionPolicy_Type(Integer32):
    """Custom type lpEngArcAqmOvPortCongestionPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aggregate", 0),
          ("individualQueue", 1))
    )


_LpEngArcAqmOvPortCongestionPolicy_Type.__name__ = "Integer32"
_LpEngArcAqmOvPortCongestionPolicy_Object = MibTableColumn
lpEngArcAqmOvPortCongestionPolicy = _LpEngArcAqmOvPortCongestionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 2, 10, 1, 4),
    _LpEngArcAqmOvPortCongestionPolicy_Type()
)
lpEngArcAqmOvPortCongestionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngArcAqmOvPortCongestionPolicy.setStatus("mandatory")


class _LpEngArcAqmOvMaxVirtualLinks_Type(Unsigned32):
    """Custom type lpEngArcAqmOvMaxVirtualLinks based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(6, 6),
        ValueRangeConstraint(14, 14),
        ValueRangeConstraint(29, 29),
    )


_LpEngArcAqmOvMaxVirtualLinks_Type.__name__ = "Unsigned32"
_LpEngArcAqmOvMaxVirtualLinks_Object = MibTableColumn
lpEngArcAqmOvMaxVirtualLinks = _LpEngArcAqmOvMaxVirtualLinks_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 2, 10, 1, 5),
    _LpEngArcAqmOvMaxVirtualLinks_Type()
)
lpEngArcAqmOvMaxVirtualLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngArcAqmOvMaxVirtualLinks.setStatus("mandatory")


class _LpEngArcAqmOvVirtualLinkGranularity_Type(Integer32):
    """Custom type lpEngArcAqmOvVirtualLinkGranularity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ds1", 1),
          ("e1", 2),
          ("jt2", 3),
          ("minimum", 0))
    )


_LpEngArcAqmOvVirtualLinkGranularity_Type.__name__ = "Integer32"
_LpEngArcAqmOvVirtualLinkGranularity_Object = MibTableColumn
lpEngArcAqmOvVirtualLinkGranularity = _LpEngArcAqmOvVirtualLinkGranularity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 2, 10, 1, 6),
    _LpEngArcAqmOvVirtualLinkGranularity_Type()
)
lpEngArcAqmOvVirtualLinkGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngArcAqmOvVirtualLinkGranularity.setStatus("mandatory")
_LpEngArcAqmOperTable_Object = MibTable
lpEngArcAqmOperTable = _LpEngArcAqmOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 10)
)
if mibBuilder.loadTexts:
    lpEngArcAqmOperTable.setStatus("mandatory")
_LpEngArcAqmOperEntry_Object = MibTableRow
lpEngArcAqmOperEntry = _LpEngArcAqmOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 10, 1)
)
lpEngArcAqmOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcAqmIndex"),
)
if mibBuilder.loadTexts:
    lpEngArcAqmOperEntry.setStatus("mandatory")


class _LpEngArcAqmConnectionPoolAvailable_Type(Unsigned32):
    """Custom type lpEngArcAqmConnectionPoolAvailable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000),
    )


_LpEngArcAqmConnectionPoolAvailable_Type.__name__ = "Unsigned32"
_LpEngArcAqmConnectionPoolAvailable_Object = MibTableColumn
lpEngArcAqmConnectionPoolAvailable = _LpEngArcAqmConnectionPoolAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 10, 1, 1),
    _LpEngArcAqmConnectionPoolAvailable_Type()
)
lpEngArcAqmConnectionPoolAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcAqmConnectionPoolAvailable.setStatus("mandatory")


class _LpEngArcAqmConnectionPoolUsage_Type(Unsigned32):
    """Custom type lpEngArcAqmConnectionPoolUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000),
    )


_LpEngArcAqmConnectionPoolUsage_Type.__name__ = "Unsigned32"
_LpEngArcAqmConnectionPoolUsage_Object = MibTableColumn
lpEngArcAqmConnectionPoolUsage = _LpEngArcAqmConnectionPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 10, 1, 2),
    _LpEngArcAqmConnectionPoolUsage_Type()
)
lpEngArcAqmConnectionPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcAqmConnectionPoolUsage.setStatus("mandatory")


class _LpEngArcAqmTxCellMemoryAvailable_Type(Gauge32):
    """Custom type lpEngArcAqmTxCellMemoryAvailable based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 163839),
    )


_LpEngArcAqmTxCellMemoryAvailable_Type.__name__ = "Gauge32"
_LpEngArcAqmTxCellMemoryAvailable_Object = MibTableColumn
lpEngArcAqmTxCellMemoryAvailable = _LpEngArcAqmTxCellMemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 10, 1, 5),
    _LpEngArcAqmTxCellMemoryAvailable_Type()
)
lpEngArcAqmTxCellMemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcAqmTxCellMemoryAvailable.setStatus("obsolete")


class _LpEngArcAqmTxCellMemoryMinAvailable_Type(Gauge32):
    """Custom type lpEngArcAqmTxCellMemoryMinAvailable based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 163839),
    )


_LpEngArcAqmTxCellMemoryMinAvailable_Type.__name__ = "Gauge32"
_LpEngArcAqmTxCellMemoryMinAvailable_Object = MibTableColumn
lpEngArcAqmTxCellMemoryMinAvailable = _LpEngArcAqmTxCellMemoryMinAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 10, 1, 6),
    _LpEngArcAqmTxCellMemoryMinAvailable_Type()
)
lpEngArcAqmTxCellMemoryMinAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcAqmTxCellMemoryMinAvailable.setStatus("obsolete")


class _LpEngArcAqmTxCellMemoryCongestionState_Type(Gauge32):
    """Custom type lpEngArcAqmTxCellMemoryCongestionState based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_LpEngArcAqmTxCellMemoryCongestionState_Type.__name__ = "Gauge32"
_LpEngArcAqmTxCellMemoryCongestionState_Object = MibTableColumn
lpEngArcAqmTxCellMemoryCongestionState = _LpEngArcAqmTxCellMemoryCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 10, 1, 7),
    _LpEngArcAqmTxCellMemoryCongestionState_Type()
)
lpEngArcAqmTxCellMemoryCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcAqmTxCellMemoryCongestionState.setStatus("mandatory")


class _LpEngArcAqmTxCellMemoryMaxUsage_Type(Gauge32):
    """Custom type lpEngArcAqmTxCellMemoryMaxUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 163839),
    )


_LpEngArcAqmTxCellMemoryMaxUsage_Type.__name__ = "Gauge32"
_LpEngArcAqmTxCellMemoryMaxUsage_Object = MibTableColumn
lpEngArcAqmTxCellMemoryMaxUsage = _LpEngArcAqmTxCellMemoryMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 10, 1, 8),
    _LpEngArcAqmTxCellMemoryMaxUsage_Type()
)
lpEngArcAqmTxCellMemoryMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcAqmTxCellMemoryMaxUsage.setStatus("mandatory")


class _LpEngArcAqmTxCellMemoryUsage_Type(Gauge32):
    """Custom type lpEngArcAqmTxCellMemoryUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 163839),
    )


_LpEngArcAqmTxCellMemoryUsage_Type.__name__ = "Gauge32"
_LpEngArcAqmTxCellMemoryUsage_Object = MibTableColumn
lpEngArcAqmTxCellMemoryUsage = _LpEngArcAqmTxCellMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 10, 1, 9),
    _LpEngArcAqmTxCellMemoryUsage_Type()
)
lpEngArcAqmTxCellMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcAqmTxCellMemoryUsage.setStatus("mandatory")


class _LpEngArcAqmMaxVirtualLinks_Type(Unsigned32):
    """Custom type lpEngArcAqmMaxVirtualLinks based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(6, 6),
        ValueRangeConstraint(14, 14),
        ValueRangeConstraint(29, 29),
    )


_LpEngArcAqmMaxVirtualLinks_Type.__name__ = "Unsigned32"
_LpEngArcAqmMaxVirtualLinks_Object = MibTableColumn
lpEngArcAqmMaxVirtualLinks = _LpEngArcAqmMaxVirtualLinks_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 10, 1, 10),
    _LpEngArcAqmMaxVirtualLinks_Type()
)
lpEngArcAqmMaxVirtualLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcAqmMaxVirtualLinks.setStatus("mandatory")


class _LpEngArcAqmVirtualLinkUsage_Type(Unsigned32):
    """Custom type lpEngArcAqmVirtualLinkUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_LpEngArcAqmVirtualLinkUsage_Type.__name__ = "Unsigned32"
_LpEngArcAqmVirtualLinkUsage_Object = MibTableColumn
lpEngArcAqmVirtualLinkUsage = _LpEngArcAqmVirtualLinkUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 10, 1, 11),
    _LpEngArcAqmVirtualLinkUsage_Type()
)
lpEngArcAqmVirtualLinkUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcAqmVirtualLinkUsage.setStatus("mandatory")


class _LpEngArcAqmVirtualLinkGranularity_Type(Unsigned32):
    """Custom type lpEngArcAqmVirtualLinkGranularity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpEngArcAqmVirtualLinkGranularity_Type.__name__ = "Unsigned32"
_LpEngArcAqmVirtualLinkGranularity_Object = MibTableColumn
lpEngArcAqmVirtualLinkGranularity = _LpEngArcAqmVirtualLinkGranularity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 10, 1, 12),
    _LpEngArcAqmVirtualLinkGranularity_Type()
)
lpEngArcAqmVirtualLinkGranularity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcAqmVirtualLinkGranularity.setStatus("mandatory")
_LpEngArcAqmTxCellThreshTable_Object = MibTable
lpEngArcAqmTxCellThreshTable = _LpEngArcAqmTxCellThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 448)
)
if mibBuilder.loadTexts:
    lpEngArcAqmTxCellThreshTable.setStatus("mandatory")
_LpEngArcAqmTxCellThreshEntry_Object = MibTableRow
lpEngArcAqmTxCellThreshEntry = _LpEngArcAqmTxCellThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 448, 1)
)
lpEngArcAqmTxCellThreshEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcAqmIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcAqmTxCellThreshIndex"),
)
if mibBuilder.loadTexts:
    lpEngArcAqmTxCellThreshEntry.setStatus("mandatory")


class _LpEngArcAqmTxCellThreshIndex_Type(Integer32):
    """Custom type lpEngArcAqmTxCellThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_LpEngArcAqmTxCellThreshIndex_Type.__name__ = "Integer32"
_LpEngArcAqmTxCellThreshIndex_Object = MibTableColumn
lpEngArcAqmTxCellThreshIndex = _LpEngArcAqmTxCellThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 448, 1, 1),
    _LpEngArcAqmTxCellThreshIndex_Type()
)
lpEngArcAqmTxCellThreshIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEngArcAqmTxCellThreshIndex.setStatus("mandatory")


class _LpEngArcAqmTxCellThreshValue_Type(Unsigned32):
    """Custom type lpEngArcAqmTxCellThreshValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 163839),
    )


_LpEngArcAqmTxCellThreshValue_Type.__name__ = "Unsigned32"
_LpEngArcAqmTxCellThreshValue_Object = MibTableColumn
lpEngArcAqmTxCellThreshValue = _LpEngArcAqmTxCellThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 4, 448, 1, 2),
    _LpEngArcAqmTxCellThreshValue_Type()
)
lpEngArcAqmTxCellThreshValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcAqmTxCellThreshValue.setStatus("mandatory")
_LpEngArcOperTable_Object = MibTable
lpEngArcOperTable = _LpEngArcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 10)
)
if mibBuilder.loadTexts:
    lpEngArcOperTable.setStatus("mandatory")
_LpEngArcOperEntry_Object = MibTableRow
lpEngArcOperEntry = _LpEngArcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 10, 1)
)
lpEngArcOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcIndex"),
)
if mibBuilder.loadTexts:
    lpEngArcOperEntry.setStatus("mandatory")


class _LpEngArcTotalConnectionPoolAvailable_Type(Unsigned32):
    """Custom type lpEngArcTotalConnectionPoolAvailable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_LpEngArcTotalConnectionPoolAvailable_Type.__name__ = "Unsigned32"
_LpEngArcTotalConnectionPoolAvailable_Object = MibTableColumn
lpEngArcTotalConnectionPoolAvailable = _LpEngArcTotalConnectionPoolAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 10, 1, 1),
    _LpEngArcTotalConnectionPoolAvailable_Type()
)
lpEngArcTotalConnectionPoolAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcTotalConnectionPoolAvailable.setStatus("mandatory")


class _LpEngArcTotalConnectionPoolUsage_Type(Unsigned32):
    """Custom type lpEngArcTotalConnectionPoolUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_LpEngArcTotalConnectionPoolUsage_Type.__name__ = "Unsigned32"
_LpEngArcTotalConnectionPoolUsage_Object = MibTableColumn
lpEngArcTotalConnectionPoolUsage = _LpEngArcTotalConnectionPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 10, 1, 2),
    _LpEngArcTotalConnectionPoolUsage_Type()
)
lpEngArcTotalConnectionPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcTotalConnectionPoolUsage.setStatus("mandatory")


class _LpEngArcMulticastBranchesAvailable_Type(Unsigned32):
    """Custom type lpEngArcMulticastBranchesAvailable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_LpEngArcMulticastBranchesAvailable_Type.__name__ = "Unsigned32"
_LpEngArcMulticastBranchesAvailable_Object = MibTableColumn
lpEngArcMulticastBranchesAvailable = _LpEngArcMulticastBranchesAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 10, 1, 3),
    _LpEngArcMulticastBranchesAvailable_Type()
)
lpEngArcMulticastBranchesAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcMulticastBranchesAvailable.setStatus("mandatory")


class _LpEngArcMulticastBranchesUsage_Type(Unsigned32):
    """Custom type lpEngArcMulticastBranchesUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_LpEngArcMulticastBranchesUsage_Type.__name__ = "Unsigned32"
_LpEngArcMulticastBranchesUsage_Object = MibTableColumn
lpEngArcMulticastBranchesUsage = _LpEngArcMulticastBranchesUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 10, 1, 4),
    _LpEngArcMulticastBranchesUsage_Type()
)
lpEngArcMulticastBranchesUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcMulticastBranchesUsage.setStatus("mandatory")


class _LpEngArcTxCellMemoryAllocation_Type(Unsigned32):
    """Custom type lpEngArcTxCellMemoryAllocation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_LpEngArcTxCellMemoryAllocation_Type.__name__ = "Unsigned32"
_LpEngArcTxCellMemoryAllocation_Object = MibTableColumn
lpEngArcTxCellMemoryAllocation = _LpEngArcTxCellMemoryAllocation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 10, 1, 5),
    _LpEngArcTxCellMemoryAllocation_Type()
)
lpEngArcTxCellMemoryAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcTxCellMemoryAllocation.setStatus("mandatory")


class _LpEngArcTxCellMemoryAvailable_Type(Gauge32):
    """Custom type lpEngArcTxCellMemoryAvailable based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 163839),
    )


_LpEngArcTxCellMemoryAvailable_Type.__name__ = "Gauge32"
_LpEngArcTxCellMemoryAvailable_Object = MibTableColumn
lpEngArcTxCellMemoryAvailable = _LpEngArcTxCellMemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 10, 1, 6),
    _LpEngArcTxCellMemoryAvailable_Type()
)
lpEngArcTxCellMemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcTxCellMemoryAvailable.setStatus("obsolete")


class _LpEngArcTxCellMemoryMinAvailable_Type(Gauge32):
    """Custom type lpEngArcTxCellMemoryMinAvailable based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 163839),
    )


_LpEngArcTxCellMemoryMinAvailable_Type.__name__ = "Gauge32"
_LpEngArcTxCellMemoryMinAvailable_Object = MibTableColumn
lpEngArcTxCellMemoryMinAvailable = _LpEngArcTxCellMemoryMinAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 10, 1, 7),
    _LpEngArcTxCellMemoryMinAvailable_Type()
)
lpEngArcTxCellMemoryMinAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcTxCellMemoryMinAvailable.setStatus("obsolete")


class _LpEngArcTxCellMemoryCongestionState_Type(Gauge32):
    """Custom type lpEngArcTxCellMemoryCongestionState based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_LpEngArcTxCellMemoryCongestionState_Type.__name__ = "Gauge32"
_LpEngArcTxCellMemoryCongestionState_Object = MibTableColumn
lpEngArcTxCellMemoryCongestionState = _LpEngArcTxCellMemoryCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 10, 1, 8),
    _LpEngArcTxCellMemoryCongestionState_Type()
)
lpEngArcTxCellMemoryCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcTxCellMemoryCongestionState.setStatus("mandatory")


class _LpEngArcRxCellMemoryAllocation_Type(Unsigned32):
    """Custom type lpEngArcRxCellMemoryAllocation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_LpEngArcRxCellMemoryAllocation_Type.__name__ = "Unsigned32"
_LpEngArcRxCellMemoryAllocation_Object = MibTableColumn
lpEngArcRxCellMemoryAllocation = _LpEngArcRxCellMemoryAllocation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 10, 1, 9),
    _LpEngArcRxCellMemoryAllocation_Type()
)
lpEngArcRxCellMemoryAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcRxCellMemoryAllocation.setStatus("mandatory")


class _LpEngArcRxCellMemoryAvailable_Type(Gauge32):
    """Custom type lpEngArcRxCellMemoryAvailable based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 163839),
    )


_LpEngArcRxCellMemoryAvailable_Type.__name__ = "Gauge32"
_LpEngArcRxCellMemoryAvailable_Object = MibTableColumn
lpEngArcRxCellMemoryAvailable = _LpEngArcRxCellMemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 10, 1, 10),
    _LpEngArcRxCellMemoryAvailable_Type()
)
lpEngArcRxCellMemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcRxCellMemoryAvailable.setStatus("obsolete")


class _LpEngArcRxCellMemoryMinAvailable_Type(Gauge32):
    """Custom type lpEngArcRxCellMemoryMinAvailable based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_LpEngArcRxCellMemoryMinAvailable_Type.__name__ = "Gauge32"
_LpEngArcRxCellMemoryMinAvailable_Object = MibTableColumn
lpEngArcRxCellMemoryMinAvailable = _LpEngArcRxCellMemoryMinAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 10, 1, 11),
    _LpEngArcRxCellMemoryMinAvailable_Type()
)
lpEngArcRxCellMemoryMinAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcRxCellMemoryMinAvailable.setStatus("obsolete")


class _LpEngArcRxCellMemoryCongestionState_Type(Gauge32):
    """Custom type lpEngArcRxCellMemoryCongestionState based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_LpEngArcRxCellMemoryCongestionState_Type.__name__ = "Gauge32"
_LpEngArcRxCellMemoryCongestionState_Object = MibTableColumn
lpEngArcRxCellMemoryCongestionState = _LpEngArcRxCellMemoryCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 10, 1, 12),
    _LpEngArcRxCellMemoryCongestionState_Type()
)
lpEngArcRxCellMemoryCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcRxCellMemoryCongestionState.setStatus("mandatory")


class _LpEngArcTxCellMemoryMaxUsage_Type(Gauge32):
    """Custom type lpEngArcTxCellMemoryMaxUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 163839),
    )


_LpEngArcTxCellMemoryMaxUsage_Type.__name__ = "Gauge32"
_LpEngArcTxCellMemoryMaxUsage_Object = MibTableColumn
lpEngArcTxCellMemoryMaxUsage = _LpEngArcTxCellMemoryMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 10, 1, 13),
    _LpEngArcTxCellMemoryMaxUsage_Type()
)
lpEngArcTxCellMemoryMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcTxCellMemoryMaxUsage.setStatus("mandatory")


class _LpEngArcTxCellMemoryUsage_Type(Gauge32):
    """Custom type lpEngArcTxCellMemoryUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 163839),
    )


_LpEngArcTxCellMemoryUsage_Type.__name__ = "Gauge32"
_LpEngArcTxCellMemoryUsage_Object = MibTableColumn
lpEngArcTxCellMemoryUsage = _LpEngArcTxCellMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 10, 1, 14),
    _LpEngArcTxCellMemoryUsage_Type()
)
lpEngArcTxCellMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcTxCellMemoryUsage.setStatus("mandatory")


class _LpEngArcRxCellMemoryMaxUsage_Type(Gauge32):
    """Custom type lpEngArcRxCellMemoryMaxUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 163839),
    )


_LpEngArcRxCellMemoryMaxUsage_Type.__name__ = "Gauge32"
_LpEngArcRxCellMemoryMaxUsage_Object = MibTableColumn
lpEngArcRxCellMemoryMaxUsage = _LpEngArcRxCellMemoryMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 10, 1, 15),
    _LpEngArcRxCellMemoryMaxUsage_Type()
)
lpEngArcRxCellMemoryMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcRxCellMemoryMaxUsage.setStatus("mandatory")


class _LpEngArcRxCellMemoryUsage_Type(Gauge32):
    """Custom type lpEngArcRxCellMemoryUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 163839),
    )


_LpEngArcRxCellMemoryUsage_Type.__name__ = "Gauge32"
_LpEngArcRxCellMemoryUsage_Object = MibTableColumn
lpEngArcRxCellMemoryUsage = _LpEngArcRxCellMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 10, 1, 16),
    _LpEngArcRxCellMemoryUsage_Type()
)
lpEngArcRxCellMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcRxCellMemoryUsage.setStatus("mandatory")
_LpEngArcTxCellThreshTable_Object = MibTable
lpEngArcTxCellThreshTable = _LpEngArcTxCellThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 440)
)
if mibBuilder.loadTexts:
    lpEngArcTxCellThreshTable.setStatus("mandatory")
_LpEngArcTxCellThreshEntry_Object = MibTableRow
lpEngArcTxCellThreshEntry = _LpEngArcTxCellThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 440, 1)
)
lpEngArcTxCellThreshEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcTxCellThreshIndex"),
)
if mibBuilder.loadTexts:
    lpEngArcTxCellThreshEntry.setStatus("mandatory")


class _LpEngArcTxCellThreshIndex_Type(Integer32):
    """Custom type lpEngArcTxCellThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_LpEngArcTxCellThreshIndex_Type.__name__ = "Integer32"
_LpEngArcTxCellThreshIndex_Object = MibTableColumn
lpEngArcTxCellThreshIndex = _LpEngArcTxCellThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 440, 1, 1),
    _LpEngArcTxCellThreshIndex_Type()
)
lpEngArcTxCellThreshIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEngArcTxCellThreshIndex.setStatus("mandatory")


class _LpEngArcTxCellThreshValue_Type(Unsigned32):
    """Custom type lpEngArcTxCellThreshValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 163839),
    )


_LpEngArcTxCellThreshValue_Type.__name__ = "Unsigned32"
_LpEngArcTxCellThreshValue_Object = MibTableColumn
lpEngArcTxCellThreshValue = _LpEngArcTxCellThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 440, 1, 2),
    _LpEngArcTxCellThreshValue_Type()
)
lpEngArcTxCellThreshValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcTxCellThreshValue.setStatus("mandatory")
_LpEngArcRxCellThreshTable_Object = MibTable
lpEngArcRxCellThreshTable = _LpEngArcRxCellThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 444)
)
if mibBuilder.loadTexts:
    lpEngArcRxCellThreshTable.setStatus("mandatory")
_LpEngArcRxCellThreshEntry_Object = MibTableRow
lpEngArcRxCellThreshEntry = _LpEngArcRxCellThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 444, 1)
)
lpEngArcRxCellThreshEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngArcRxCellThreshIndex"),
)
if mibBuilder.loadTexts:
    lpEngArcRxCellThreshEntry.setStatus("mandatory")


class _LpEngArcRxCellThreshIndex_Type(Integer32):
    """Custom type lpEngArcRxCellThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_LpEngArcRxCellThreshIndex_Type.__name__ = "Integer32"
_LpEngArcRxCellThreshIndex_Object = MibTableColumn
lpEngArcRxCellThreshIndex = _LpEngArcRxCellThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 444, 1, 1),
    _LpEngArcRxCellThreshIndex_Type()
)
lpEngArcRxCellThreshIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEngArcRxCellThreshIndex.setStatus("mandatory")


class _LpEngArcRxCellThreshValue_Type(Unsigned32):
    """Custom type lpEngArcRxCellThreshValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 163839),
    )


_LpEngArcRxCellThreshValue_Type.__name__ = "Unsigned32"
_LpEngArcRxCellThreshValue_Object = MibTableColumn
lpEngArcRxCellThreshValue = _LpEngArcRxCellThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 5, 444, 1, 2),
    _LpEngArcRxCellThreshValue_Type()
)
lpEngArcRxCellThreshValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngArcRxCellThreshValue.setStatus("mandatory")
_LpEngFcrc_ObjectIdentity = ObjectIdentity
lpEngFcrc = _LpEngFcrc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6)
)
_LpEngFcrcRowStatusTable_Object = MibTable
lpEngFcrcRowStatusTable = _LpEngFcrcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 1)
)
if mibBuilder.loadTexts:
    lpEngFcrcRowStatusTable.setStatus("mandatory")
_LpEngFcrcRowStatusEntry_Object = MibTableRow
lpEngFcrcRowStatusEntry = _LpEngFcrcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 1, 1)
)
lpEngFcrcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngFcrcIndex"),
)
if mibBuilder.loadTexts:
    lpEngFcrcRowStatusEntry.setStatus("mandatory")
_LpEngFcrcRowStatus_Type = RowStatus
_LpEngFcrcRowStatus_Object = MibTableColumn
lpEngFcrcRowStatus = _LpEngFcrcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 1, 1, 1),
    _LpEngFcrcRowStatus_Type()
)
lpEngFcrcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngFcrcRowStatus.setStatus("mandatory")
_LpEngFcrcComponentName_Type = DisplayString
_LpEngFcrcComponentName_Object = MibTableColumn
lpEngFcrcComponentName = _LpEngFcrcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 1, 1, 2),
    _LpEngFcrcComponentName_Type()
)
lpEngFcrcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcComponentName.setStatus("mandatory")
_LpEngFcrcStorageType_Type = StorageType
_LpEngFcrcStorageType_Object = MibTableColumn
lpEngFcrcStorageType = _LpEngFcrcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 1, 1, 4),
    _LpEngFcrcStorageType_Type()
)
lpEngFcrcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcStorageType.setStatus("mandatory")
_LpEngFcrcIndex_Type = NonReplicated
_LpEngFcrcIndex_Object = MibTableColumn
lpEngFcrcIndex = _LpEngFcrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 1, 1, 10),
    _LpEngFcrcIndex_Type()
)
lpEngFcrcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEngFcrcIndex.setStatus("mandatory")
_LpEngFcrcOv_ObjectIdentity = ObjectIdentity
lpEngFcrcOv = _LpEngFcrcOv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 2)
)
_LpEngFcrcOvRowStatusTable_Object = MibTable
lpEngFcrcOvRowStatusTable = _LpEngFcrcOvRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 2, 1)
)
if mibBuilder.loadTexts:
    lpEngFcrcOvRowStatusTable.setStatus("mandatory")
_LpEngFcrcOvRowStatusEntry_Object = MibTableRow
lpEngFcrcOvRowStatusEntry = _LpEngFcrcOvRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 2, 1, 1)
)
lpEngFcrcOvRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngFcrcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngFcrcOvIndex"),
)
if mibBuilder.loadTexts:
    lpEngFcrcOvRowStatusEntry.setStatus("mandatory")
_LpEngFcrcOvRowStatus_Type = RowStatus
_LpEngFcrcOvRowStatus_Object = MibTableColumn
lpEngFcrcOvRowStatus = _LpEngFcrcOvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 2, 1, 1, 1),
    _LpEngFcrcOvRowStatus_Type()
)
lpEngFcrcOvRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngFcrcOvRowStatus.setStatus("mandatory")
_LpEngFcrcOvComponentName_Type = DisplayString
_LpEngFcrcOvComponentName_Object = MibTableColumn
lpEngFcrcOvComponentName = _LpEngFcrcOvComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 2, 1, 1, 2),
    _LpEngFcrcOvComponentName_Type()
)
lpEngFcrcOvComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcOvComponentName.setStatus("mandatory")
_LpEngFcrcOvStorageType_Type = StorageType
_LpEngFcrcOvStorageType_Object = MibTableColumn
lpEngFcrcOvStorageType = _LpEngFcrcOvStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 2, 1, 1, 4),
    _LpEngFcrcOvStorageType_Type()
)
lpEngFcrcOvStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcOvStorageType.setStatus("mandatory")
_LpEngFcrcOvIndex_Type = NonReplicated
_LpEngFcrcOvIndex_Object = MibTableColumn
lpEngFcrcOvIndex = _LpEngFcrcOvIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 2, 1, 1, 10),
    _LpEngFcrcOvIndex_Type()
)
lpEngFcrcOvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEngFcrcOvIndex.setStatus("mandatory")
_LpEngFcrcOvProvTable_Object = MibTable
lpEngFcrcOvProvTable = _LpEngFcrcOvProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 2, 10)
)
if mibBuilder.loadTexts:
    lpEngFcrcOvProvTable.setStatus("mandatory")
_LpEngFcrcOvProvEntry_Object = MibTableRow
lpEngFcrcOvProvEntry = _LpEngFcrcOvProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 2, 10, 1)
)
lpEngFcrcOvProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngFcrcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngFcrcOvIndex"),
)
if mibBuilder.loadTexts:
    lpEngFcrcOvProvEntry.setStatus("mandatory")


class _LpEngFcrcOvSubConnectionPoolCapacity_Type(Unsigned32):
    """Custom type lpEngFcrcOvSubConnectionPoolCapacity based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49152),
        ValueRangeConstraint(65535, 65535),
    )


_LpEngFcrcOvSubConnectionPoolCapacity_Type.__name__ = "Unsigned32"
_LpEngFcrcOvSubConnectionPoolCapacity_Object = MibTableColumn
lpEngFcrcOvSubConnectionPoolCapacity = _LpEngFcrcOvSubConnectionPoolCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 2, 10, 1, 1),
    _LpEngFcrcOvSubConnectionPoolCapacity_Type()
)
lpEngFcrcOvSubConnectionPoolCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngFcrcOvSubConnectionPoolCapacity.setStatus("mandatory")


class _LpEngFcrcOvLnnConnectionPoolCapacity_Type(Unsigned32):
    """Custom type lpEngFcrcOvLnnConnectionPoolCapacity based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2048),
    )


_LpEngFcrcOvLnnConnectionPoolCapacity_Type.__name__ = "Unsigned32"
_LpEngFcrcOvLnnConnectionPoolCapacity_Object = MibTableColumn
lpEngFcrcOvLnnConnectionPoolCapacity = _LpEngFcrcOvLnnConnectionPoolCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 2, 10, 1, 2),
    _LpEngFcrcOvLnnConnectionPoolCapacity_Type()
)
lpEngFcrcOvLnnConnectionPoolCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngFcrcOvLnnConnectionPoolCapacity.setStatus("mandatory")
_LpEngFcrcPqc_ObjectIdentity = ObjectIdentity
lpEngFcrcPqc = _LpEngFcrcPqc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 3)
)
_LpEngFcrcPqcRowStatusTable_Object = MibTable
lpEngFcrcPqcRowStatusTable = _LpEngFcrcPqcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 3, 1)
)
if mibBuilder.loadTexts:
    lpEngFcrcPqcRowStatusTable.setStatus("mandatory")
_LpEngFcrcPqcRowStatusEntry_Object = MibTableRow
lpEngFcrcPqcRowStatusEntry = _LpEngFcrcPqcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 3, 1, 1)
)
lpEngFcrcPqcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngFcrcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngFcrcPqcIndex"),
)
if mibBuilder.loadTexts:
    lpEngFcrcPqcRowStatusEntry.setStatus("mandatory")
_LpEngFcrcPqcRowStatus_Type = RowStatus
_LpEngFcrcPqcRowStatus_Object = MibTableColumn
lpEngFcrcPqcRowStatus = _LpEngFcrcPqcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 3, 1, 1, 1),
    _LpEngFcrcPqcRowStatus_Type()
)
lpEngFcrcPqcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngFcrcPqcRowStatus.setStatus("mandatory")
_LpEngFcrcPqcComponentName_Type = DisplayString
_LpEngFcrcPqcComponentName_Object = MibTableColumn
lpEngFcrcPqcComponentName = _LpEngFcrcPqcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 3, 1, 1, 2),
    _LpEngFcrcPqcComponentName_Type()
)
lpEngFcrcPqcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcPqcComponentName.setStatus("mandatory")
_LpEngFcrcPqcStorageType_Type = StorageType
_LpEngFcrcPqcStorageType_Object = MibTableColumn
lpEngFcrcPqcStorageType = _LpEngFcrcPqcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 3, 1, 1, 4),
    _LpEngFcrcPqcStorageType_Type()
)
lpEngFcrcPqcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcPqcStorageType.setStatus("mandatory")
_LpEngFcrcPqcIndex_Type = NonReplicated
_LpEngFcrcPqcIndex_Object = MibTableColumn
lpEngFcrcPqcIndex = _LpEngFcrcPqcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 3, 1, 1, 10),
    _LpEngFcrcPqcIndex_Type()
)
lpEngFcrcPqcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEngFcrcPqcIndex.setStatus("mandatory")
_LpEngFcrcPqcOv_ObjectIdentity = ObjectIdentity
lpEngFcrcPqcOv = _LpEngFcrcPqcOv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 3, 2)
)
_LpEngFcrcPqcOvRowStatusTable_Object = MibTable
lpEngFcrcPqcOvRowStatusTable = _LpEngFcrcPqcOvRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 3, 2, 1)
)
if mibBuilder.loadTexts:
    lpEngFcrcPqcOvRowStatusTable.setStatus("mandatory")
_LpEngFcrcPqcOvRowStatusEntry_Object = MibTableRow
lpEngFcrcPqcOvRowStatusEntry = _LpEngFcrcPqcOvRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 3, 2, 1, 1)
)
lpEngFcrcPqcOvRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngFcrcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngFcrcPqcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngFcrcPqcOvIndex"),
)
if mibBuilder.loadTexts:
    lpEngFcrcPqcOvRowStatusEntry.setStatus("mandatory")
_LpEngFcrcPqcOvRowStatus_Type = RowStatus
_LpEngFcrcPqcOvRowStatus_Object = MibTableColumn
lpEngFcrcPqcOvRowStatus = _LpEngFcrcPqcOvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 3, 2, 1, 1, 1),
    _LpEngFcrcPqcOvRowStatus_Type()
)
lpEngFcrcPqcOvRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcPqcOvRowStatus.setStatus("mandatory")
_LpEngFcrcPqcOvComponentName_Type = DisplayString
_LpEngFcrcPqcOvComponentName_Object = MibTableColumn
lpEngFcrcPqcOvComponentName = _LpEngFcrcPqcOvComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 3, 2, 1, 1, 2),
    _LpEngFcrcPqcOvComponentName_Type()
)
lpEngFcrcPqcOvComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcPqcOvComponentName.setStatus("mandatory")
_LpEngFcrcPqcOvStorageType_Type = StorageType
_LpEngFcrcPqcOvStorageType_Object = MibTableColumn
lpEngFcrcPqcOvStorageType = _LpEngFcrcPqcOvStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 3, 2, 1, 1, 4),
    _LpEngFcrcPqcOvStorageType_Type()
)
lpEngFcrcPqcOvStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcPqcOvStorageType.setStatus("mandatory")
_LpEngFcrcPqcOvIndex_Type = NonReplicated
_LpEngFcrcPqcOvIndex_Object = MibTableColumn
lpEngFcrcPqcOvIndex = _LpEngFcrcPqcOvIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 3, 2, 1, 1, 10),
    _LpEngFcrcPqcOvIndex_Type()
)
lpEngFcrcPqcOvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEngFcrcPqcOvIndex.setStatus("mandatory")
_LpEngFcrcPqcOvProvTable_Object = MibTable
lpEngFcrcPqcOvProvTable = _LpEngFcrcPqcOvProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 3, 2, 10)
)
if mibBuilder.loadTexts:
    lpEngFcrcPqcOvProvTable.setStatus("mandatory")
_LpEngFcrcPqcOvProvEntry_Object = MibTableRow
lpEngFcrcPqcOvProvEntry = _LpEngFcrcPqcOvProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 3, 2, 10, 1)
)
lpEngFcrcPqcOvProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngFcrcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngFcrcPqcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngFcrcPqcOvIndex"),
)
if mibBuilder.loadTexts:
    lpEngFcrcPqcOvProvEntry.setStatus("mandatory")


class _LpEngFcrcPqcOvIpRoutesPoolCapacity_Type(Unsigned32):
    """Custom type lpEngFcrcPqcOvIpRoutesPoolCapacity based on Unsigned32"""
    defaultValue = 4096

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_LpEngFcrcPqcOvIpRoutesPoolCapacity_Type.__name__ = "Unsigned32"
_LpEngFcrcPqcOvIpRoutesPoolCapacity_Object = MibTableColumn
lpEngFcrcPqcOvIpRoutesPoolCapacity = _LpEngFcrcPqcOvIpRoutesPoolCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 3, 2, 10, 1, 1),
    _LpEngFcrcPqcOvIpRoutesPoolCapacity_Type()
)
lpEngFcrcPqcOvIpRoutesPoolCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngFcrcPqcOvIpRoutesPoolCapacity.setStatus("mandatory")
_LpEngFcrcPqcOperTable_Object = MibTable
lpEngFcrcPqcOperTable = _LpEngFcrcPqcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 3, 10)
)
if mibBuilder.loadTexts:
    lpEngFcrcPqcOperTable.setStatus("mandatory")
_LpEngFcrcPqcOperEntry_Object = MibTableRow
lpEngFcrcPqcOperEntry = _LpEngFcrcPqcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 3, 10, 1)
)
lpEngFcrcPqcOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngFcrcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngFcrcPqcIndex"),
)
if mibBuilder.loadTexts:
    lpEngFcrcPqcOperEntry.setStatus("mandatory")


class _LpEngFcrcPqcIpRoutesPoolSize_Type(Gauge32):
    """Custom type lpEngFcrcPqcIpRoutesPoolSize based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_LpEngFcrcPqcIpRoutesPoolSize_Type.__name__ = "Gauge32"
_LpEngFcrcPqcIpRoutesPoolSize_Object = MibTableColumn
lpEngFcrcPqcIpRoutesPoolSize = _LpEngFcrcPqcIpRoutesPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 3, 10, 1, 1),
    _LpEngFcrcPqcIpRoutesPoolSize_Type()
)
lpEngFcrcPqcIpRoutesPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcPqcIpRoutesPoolSize.setStatus("mandatory")


class _LpEngFcrcPqcIpRoutesPoolUsage_Type(Gauge32):
    """Custom type lpEngFcrcPqcIpRoutesPoolUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_LpEngFcrcPqcIpRoutesPoolUsage_Type.__name__ = "Gauge32"
_LpEngFcrcPqcIpRoutesPoolUsage_Object = MibTableColumn
lpEngFcrcPqcIpRoutesPoolUsage = _LpEngFcrcPqcIpRoutesPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 3, 10, 1, 2),
    _LpEngFcrcPqcIpRoutesPoolUsage_Type()
)
lpEngFcrcPqcIpRoutesPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcPqcIpRoutesPoolUsage.setStatus("mandatory")


class _LpEngFcrcPqcIpRoutesPoolAvailableEst_Type(Gauge32):
    """Custom type lpEngFcrcPqcIpRoutesPoolAvailableEst based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_LpEngFcrcPqcIpRoutesPoolAvailableEst_Type.__name__ = "Gauge32"
_LpEngFcrcPqcIpRoutesPoolAvailableEst_Object = MibTableColumn
lpEngFcrcPqcIpRoutesPoolAvailableEst = _LpEngFcrcPqcIpRoutesPoolAvailableEst_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 3, 10, 1, 3),
    _LpEngFcrcPqcIpRoutesPoolAvailableEst_Type()
)
lpEngFcrcPqcIpRoutesPoolAvailableEst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcPqcIpRoutesPoolAvailableEst.setStatus("mandatory")
_LpEngFcrcOperTable_Object = MibTable
lpEngFcrcOperTable = _LpEngFcrcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 10)
)
if mibBuilder.loadTexts:
    lpEngFcrcOperTable.setStatus("mandatory")
_LpEngFcrcOperEntry_Object = MibTableRow
lpEngFcrcOperEntry = _LpEngFcrcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 10, 1)
)
lpEngFcrcOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngFcrcIndex"),
)
if mibBuilder.loadTexts:
    lpEngFcrcOperEntry.setStatus("mandatory")


class _LpEngFcrcSubConnectionPoolAvailable_Type(Unsigned32):
    """Custom type lpEngFcrcSubConnectionPoolAvailable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49152),
    )


_LpEngFcrcSubConnectionPoolAvailable_Type.__name__ = "Unsigned32"
_LpEngFcrcSubConnectionPoolAvailable_Object = MibTableColumn
lpEngFcrcSubConnectionPoolAvailable = _LpEngFcrcSubConnectionPoolAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 10, 1, 1),
    _LpEngFcrcSubConnectionPoolAvailable_Type()
)
lpEngFcrcSubConnectionPoolAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcSubConnectionPoolAvailable.setStatus("mandatory")


class _LpEngFcrcSubConnectionPoolUsage_Type(Unsigned32):
    """Custom type lpEngFcrcSubConnectionPoolUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49152),
    )


_LpEngFcrcSubConnectionPoolUsage_Type.__name__ = "Unsigned32"
_LpEngFcrcSubConnectionPoolUsage_Object = MibTableColumn
lpEngFcrcSubConnectionPoolUsage = _LpEngFcrcSubConnectionPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 10, 1, 2),
    _LpEngFcrcSubConnectionPoolUsage_Type()
)
lpEngFcrcSubConnectionPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcSubConnectionPoolUsage.setStatus("mandatory")


class _LpEngFcrcLnnConnectionPoolAvailable_Type(Unsigned32):
    """Custom type lpEngFcrcLnnConnectionPoolAvailable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_LpEngFcrcLnnConnectionPoolAvailable_Type.__name__ = "Unsigned32"
_LpEngFcrcLnnConnectionPoolAvailable_Object = MibTableColumn
lpEngFcrcLnnConnectionPoolAvailable = _LpEngFcrcLnnConnectionPoolAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 10, 1, 3),
    _LpEngFcrcLnnConnectionPoolAvailable_Type()
)
lpEngFcrcLnnConnectionPoolAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcLnnConnectionPoolAvailable.setStatus("mandatory")


class _LpEngFcrcLnnConnectionPoolUsage_Type(Unsigned32):
    """Custom type lpEngFcrcLnnConnectionPoolUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_LpEngFcrcLnnConnectionPoolUsage_Type.__name__ = "Unsigned32"
_LpEngFcrcLnnConnectionPoolUsage_Object = MibTableColumn
lpEngFcrcLnnConnectionPoolUsage = _LpEngFcrcLnnConnectionPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 10, 1, 4),
    _LpEngFcrcLnnConnectionPoolUsage_Type()
)
lpEngFcrcLnnConnectionPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcLnnConnectionPoolUsage.setStatus("mandatory")


class _LpEngFcrcTxFrameMemoryAvailable_Type(Gauge32):
    """Custom type lpEngFcrcTxFrameMemoryAvailable based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_LpEngFcrcTxFrameMemoryAvailable_Type.__name__ = "Gauge32"
_LpEngFcrcTxFrameMemoryAvailable_Object = MibTableColumn
lpEngFcrcTxFrameMemoryAvailable = _LpEngFcrcTxFrameMemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 10, 1, 5),
    _LpEngFcrcTxFrameMemoryAvailable_Type()
)
lpEngFcrcTxFrameMemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcTxFrameMemoryAvailable.setStatus("obsolete")


class _LpEngFcrcTxFrameMemoryMinAvailable_Type(Gauge32):
    """Custom type lpEngFcrcTxFrameMemoryMinAvailable based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_LpEngFcrcTxFrameMemoryMinAvailable_Type.__name__ = "Gauge32"
_LpEngFcrcTxFrameMemoryMinAvailable_Object = MibTableColumn
lpEngFcrcTxFrameMemoryMinAvailable = _LpEngFcrcTxFrameMemoryMinAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 10, 1, 6),
    _LpEngFcrcTxFrameMemoryMinAvailable_Type()
)
lpEngFcrcTxFrameMemoryMinAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcTxFrameMemoryMinAvailable.setStatus("obsolete")


class _LpEngFcrcTxFrameMemoryCongestionState_Type(Gauge32):
    """Custom type lpEngFcrcTxFrameMemoryCongestionState based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_LpEngFcrcTxFrameMemoryCongestionState_Type.__name__ = "Gauge32"
_LpEngFcrcTxFrameMemoryCongestionState_Object = MibTableColumn
lpEngFcrcTxFrameMemoryCongestionState = _LpEngFcrcTxFrameMemoryCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 10, 1, 7),
    _LpEngFcrcTxFrameMemoryCongestionState_Type()
)
lpEngFcrcTxFrameMemoryCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcTxFrameMemoryCongestionState.setStatus("mandatory")


class _LpEngFcrcRxFrameMemoryAvailable_Type(Gauge32):
    """Custom type lpEngFcrcRxFrameMemoryAvailable based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_LpEngFcrcRxFrameMemoryAvailable_Type.__name__ = "Gauge32"
_LpEngFcrcRxFrameMemoryAvailable_Object = MibTableColumn
lpEngFcrcRxFrameMemoryAvailable = _LpEngFcrcRxFrameMemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 10, 1, 8),
    _LpEngFcrcRxFrameMemoryAvailable_Type()
)
lpEngFcrcRxFrameMemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcRxFrameMemoryAvailable.setStatus("obsolete")


class _LpEngFcrcRxFrameMemoryMinAvailable_Type(Gauge32):
    """Custom type lpEngFcrcRxFrameMemoryMinAvailable based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_LpEngFcrcRxFrameMemoryMinAvailable_Type.__name__ = "Gauge32"
_LpEngFcrcRxFrameMemoryMinAvailable_Object = MibTableColumn
lpEngFcrcRxFrameMemoryMinAvailable = _LpEngFcrcRxFrameMemoryMinAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 10, 1, 9),
    _LpEngFcrcRxFrameMemoryMinAvailable_Type()
)
lpEngFcrcRxFrameMemoryMinAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcRxFrameMemoryMinAvailable.setStatus("obsolete")


class _LpEngFcrcRxFrameMemoryCongestionState_Type(Gauge32):
    """Custom type lpEngFcrcRxFrameMemoryCongestionState based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_LpEngFcrcRxFrameMemoryCongestionState_Type.__name__ = "Gauge32"
_LpEngFcrcRxFrameMemoryCongestionState_Object = MibTableColumn
lpEngFcrcRxFrameMemoryCongestionState = _LpEngFcrcRxFrameMemoryCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 10, 1, 10),
    _LpEngFcrcRxFrameMemoryCongestionState_Type()
)
lpEngFcrcRxFrameMemoryCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcRxFrameMemoryCongestionState.setStatus("mandatory")


class _LpEngFcrcTxFrameMemoryMaxUsage_Type(Gauge32):
    """Custom type lpEngFcrcTxFrameMemoryMaxUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_LpEngFcrcTxFrameMemoryMaxUsage_Type.__name__ = "Gauge32"
_LpEngFcrcTxFrameMemoryMaxUsage_Object = MibTableColumn
lpEngFcrcTxFrameMemoryMaxUsage = _LpEngFcrcTxFrameMemoryMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 10, 1, 11),
    _LpEngFcrcTxFrameMemoryMaxUsage_Type()
)
lpEngFcrcTxFrameMemoryMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcTxFrameMemoryMaxUsage.setStatus("mandatory")


class _LpEngFcrcTxFrameMemoryUsage_Type(Gauge32):
    """Custom type lpEngFcrcTxFrameMemoryUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_LpEngFcrcTxFrameMemoryUsage_Type.__name__ = "Gauge32"
_LpEngFcrcTxFrameMemoryUsage_Object = MibTableColumn
lpEngFcrcTxFrameMemoryUsage = _LpEngFcrcTxFrameMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 10, 1, 12),
    _LpEngFcrcTxFrameMemoryUsage_Type()
)
lpEngFcrcTxFrameMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcTxFrameMemoryUsage.setStatus("mandatory")


class _LpEngFcrcRxFrameMemoryMaxUsage_Type(Gauge32):
    """Custom type lpEngFcrcRxFrameMemoryMaxUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_LpEngFcrcRxFrameMemoryMaxUsage_Type.__name__ = "Gauge32"
_LpEngFcrcRxFrameMemoryMaxUsage_Object = MibTableColumn
lpEngFcrcRxFrameMemoryMaxUsage = _LpEngFcrcRxFrameMemoryMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 10, 1, 13),
    _LpEngFcrcRxFrameMemoryMaxUsage_Type()
)
lpEngFcrcRxFrameMemoryMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcRxFrameMemoryMaxUsage.setStatus("mandatory")


class _LpEngFcrcRxFrameMemoryUsage_Type(Gauge32):
    """Custom type lpEngFcrcRxFrameMemoryUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_LpEngFcrcRxFrameMemoryUsage_Type.__name__ = "Gauge32"
_LpEngFcrcRxFrameMemoryUsage_Object = MibTableColumn
lpEngFcrcRxFrameMemoryUsage = _LpEngFcrcRxFrameMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 10, 1, 14),
    _LpEngFcrcRxFrameMemoryUsage_Type()
)
lpEngFcrcRxFrameMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcRxFrameMemoryUsage.setStatus("mandatory")
_LpEngFcrcTxFrThreshTable_Object = MibTable
lpEngFcrcTxFrThreshTable = _LpEngFcrcTxFrThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 442)
)
if mibBuilder.loadTexts:
    lpEngFcrcTxFrThreshTable.setStatus("mandatory")
_LpEngFcrcTxFrThreshEntry_Object = MibTableRow
lpEngFcrcTxFrThreshEntry = _LpEngFcrcTxFrThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 442, 1)
)
lpEngFcrcTxFrThreshEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngFcrcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngFcrcTxFrThreshIndex"),
)
if mibBuilder.loadTexts:
    lpEngFcrcTxFrThreshEntry.setStatus("mandatory")


class _LpEngFcrcTxFrThreshIndex_Type(Integer32):
    """Custom type lpEngFcrcTxFrThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_LpEngFcrcTxFrThreshIndex_Type.__name__ = "Integer32"
_LpEngFcrcTxFrThreshIndex_Object = MibTableColumn
lpEngFcrcTxFrThreshIndex = _LpEngFcrcTxFrThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 442, 1, 1),
    _LpEngFcrcTxFrThreshIndex_Type()
)
lpEngFcrcTxFrThreshIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEngFcrcTxFrThreshIndex.setStatus("mandatory")


class _LpEngFcrcTxFrThreshValue_Type(Unsigned32):
    """Custom type lpEngFcrcTxFrThreshValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_LpEngFcrcTxFrThreshValue_Type.__name__ = "Unsigned32"
_LpEngFcrcTxFrThreshValue_Object = MibTableColumn
lpEngFcrcTxFrThreshValue = _LpEngFcrcTxFrThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 442, 1, 2),
    _LpEngFcrcTxFrThreshValue_Type()
)
lpEngFcrcTxFrThreshValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcTxFrThreshValue.setStatus("mandatory")
_LpEngFcrcRxFrThreshTable_Object = MibTable
lpEngFcrcRxFrThreshTable = _LpEngFcrcRxFrThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 446)
)
if mibBuilder.loadTexts:
    lpEngFcrcRxFrThreshTable.setStatus("mandatory")
_LpEngFcrcRxFrThreshEntry_Object = MibTableRow
lpEngFcrcRxFrThreshEntry = _LpEngFcrcRxFrThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 446, 1)
)
lpEngFcrcRxFrThreshEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngFcrcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBaseMIB", "lpEngFcrcRxFrThreshIndex"),
)
if mibBuilder.loadTexts:
    lpEngFcrcRxFrThreshEntry.setStatus("mandatory")


class _LpEngFcrcRxFrThreshIndex_Type(Integer32):
    """Custom type lpEngFcrcRxFrThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_LpEngFcrcRxFrThreshIndex_Type.__name__ = "Integer32"
_LpEngFcrcRxFrThreshIndex_Object = MibTableColumn
lpEngFcrcRxFrThreshIndex = _LpEngFcrcRxFrThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 446, 1, 1),
    _LpEngFcrcRxFrThreshIndex_Type()
)
lpEngFcrcRxFrThreshIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEngFcrcRxFrThreshIndex.setStatus("mandatory")


class _LpEngFcrcRxFrThreshValue_Type(Unsigned32):
    """Custom type lpEngFcrcRxFrThreshValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_LpEngFcrcRxFrThreshValue_Type.__name__ = "Unsigned32"
_LpEngFcrcRxFrThreshValue_Object = MibTableColumn
lpEngFcrcRxFrThreshValue = _LpEngFcrcRxFrThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 6, 446, 1, 2),
    _LpEngFcrcRxFrThreshValue_Type()
)
lpEngFcrcRxFrThreshValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngFcrcRxFrThreshValue.setStatus("mandatory")
_AtmBaseMIB_ObjectIdentity = ObjectIdentity
atmBaseMIB = _AtmBaseMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 63)
)
_AtmBaseGroup_ObjectIdentity = ObjectIdentity
atmBaseGroup = _AtmBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 63, 1)
)
_AtmBaseGroupBE_ObjectIdentity = ObjectIdentity
atmBaseGroupBE = _AtmBaseGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 63, 1, 5)
)
_AtmBaseGroupBE00_ObjectIdentity = ObjectIdentity
atmBaseGroupBE00 = _AtmBaseGroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 63, 1, 5, 1)
)
_AtmBaseGroupBE00A_ObjectIdentity = ObjectIdentity
atmBaseGroupBE00A = _AtmBaseGroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 63, 1, 5, 1, 2)
)
_AtmBaseCapabilities_ObjectIdentity = ObjectIdentity
atmBaseCapabilities = _AtmBaseCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 63, 3)
)
_AtmBaseCapabilitiesBE_ObjectIdentity = ObjectIdentity
atmBaseCapabilitiesBE = _AtmBaseCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 63, 3, 5)
)
_AtmBaseCapabilitiesBE00_ObjectIdentity = ObjectIdentity
atmBaseCapabilitiesBE00 = _AtmBaseCapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 63, 3, 5, 1)
)
_AtmBaseCapabilitiesBE00A_ObjectIdentity = ObjectIdentity
atmBaseCapabilitiesBE00A = _AtmBaseCapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 63, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-AtmBaseMIB",
    **{"lpArc": lpArc,
       "lpArcRowStatusTable": lpArcRowStatusTable,
       "lpArcRowStatusEntry": lpArcRowStatusEntry,
       "lpArcRowStatus": lpArcRowStatus,
       "lpArcComponentName": lpArcComponentName,
       "lpArcStorageType": lpArcStorageType,
       "lpArcIndex": lpArcIndex,
       "lpArcProvTable": lpArcProvTable,
       "lpArcProvEntry": lpArcProvEntry,
       "lpArcTotalConnectionPoolCapacity": lpArcTotalConnectionPoolCapacity,
       "lpArcMulticastBranchesCapacity": lpArcMulticastBranchesCapacity,
       "lpArcTxFrameMemoryAllocation": lpArcTxFrameMemoryAllocation,
       "lpArcRxFrameMemoryAllocation": lpArcRxFrameMemoryAllocation,
       "lpArcPerVcQueueInterfaces": lpArcPerVcQueueInterfaces,
       "lpArcShapingStackAllocation": lpArcShapingStackAllocation,
       "lpArcShapingScalingFactor": lpArcShapingScalingFactor,
       "lpArcCdvAttenuation": lpArcCdvAttenuation,
       "lpArcPortAggregation": lpArcPortAggregation,
       "lpArcSubConnectionPoolCapacity": lpArcSubConnectionPoolCapacity,
       "lpArcLnnConnectionPoolCapacity": lpArcLnnConnectionPoolCapacity,
       "lpArcConnCapTable": lpArcConnCapTable,
       "lpArcConnCapEntry": lpArcConnCapEntry,
       "lpArcConnCapIndex": lpArcConnCapIndex,
       "lpArcConnCapValue": lpArcConnCapValue,
       "lpAru": lpAru,
       "lpAruRowStatusTable": lpAruRowStatusTable,
       "lpAruRowStatusEntry": lpAruRowStatusEntry,
       "lpAruRowStatus": lpAruRowStatus,
       "lpAruComponentName": lpAruComponentName,
       "lpAruStorageType": lpAruStorageType,
       "lpAruIndex": lpAruIndex,
       "lpAruOperTable": lpAruOperTable,
       "lpAruOperEntry": lpAruOperEntry,
       "lpAruTotalConnectionPoolUsage": lpAruTotalConnectionPoolUsage,
       "lpAruMulticastBranchesUsage": lpAruMulticastBranchesUsage,
       "lpAruTxCellBlockCapacity": lpAruTxCellBlockCapacity,
       "lpAruTxCellBlockUsage": lpAruTxCellBlockUsage,
       "lpAruTxCellFreeListSize": lpAruTxCellFreeListSize,
       "lpAruTxCellFreeListCongestionState": lpAruTxCellFreeListCongestionState,
       "lpAruTxFrameMemoryAllocation": lpAruTxFrameMemoryAllocation,
       "lpAruTxFrameBlockCapacity": lpAruTxFrameBlockCapacity,
       "lpAruTxFrameBlockUsage": lpAruTxFrameBlockUsage,
       "lpAruTxFrameFreeListSize": lpAruTxFrameFreeListSize,
       "lpAruTxFrameFreeListCongestionState": lpAruTxFrameFreeListCongestionState,
       "lpAruRxCellBlockCapacity": lpAruRxCellBlockCapacity,
       "lpAruRxCellBlockUsage": lpAruRxCellBlockUsage,
       "lpAruRxCellFreeListSize": lpAruRxCellFreeListSize,
       "lpAruRxCellFreeListCongestionState": lpAruRxCellFreeListCongestionState,
       "lpAruRxFrameMemoryAllocation": lpAruRxFrameMemoryAllocation,
       "lpAruRxFrameBlockCapacity": lpAruRxFrameBlockCapacity,
       "lpAruRxFrameBlockUsage": lpAruRxFrameBlockUsage,
       "lpAruRxFrameFreeListSize": lpAruRxFrameFreeListSize,
       "lpAruRxFrameFreeListCongestionState": lpAruRxFrameFreeListCongestionState,
       "lpAruSubConnectionPoolAvailable": lpAruSubConnectionPoolAvailable,
       "lpAruSubConnectionPoolUsage": lpAruSubConnectionPoolUsage,
       "lpAruLnnConnectionPoolAvailable": lpAruLnnConnectionPoolAvailable,
       "lpAruLnnConnectionPoolUsage": lpAruLnnConnectionPoolUsage,
       "lpAruConnUsageTable": lpAruConnUsageTable,
       "lpAruConnUsageEntry": lpAruConnUsageEntry,
       "lpAruConnUsageIndex": lpAruConnUsageIndex,
       "lpAruConnUsageValue": lpAruConnUsageValue,
       "lpAruTxCflThreshTable": lpAruTxCflThreshTable,
       "lpAruTxCflThreshEntry": lpAruTxCflThreshEntry,
       "lpAruTxCflThreshIndex": lpAruTxCflThreshIndex,
       "lpAruTxCflThreshValue": lpAruTxCflThreshValue,
       "lpAruTxFflThreshTable": lpAruTxFflThreshTable,
       "lpAruTxFflThreshEntry": lpAruTxFflThreshEntry,
       "lpAruTxFflThreshIndex": lpAruTxFflThreshIndex,
       "lpAruTxFflThreshValue": lpAruTxFflThreshValue,
       "lpAruRxCflThreshTable": lpAruRxCflThreshTable,
       "lpAruRxCflThreshEntry": lpAruRxCflThreshEntry,
       "lpAruRxCflThreshIndex": lpAruRxCflThreshIndex,
       "lpAruRxCflThreshValue": lpAruRxCflThreshValue,
       "lpAruRxFflThreshTable": lpAruRxFflThreshTable,
       "lpAruRxFflThreshEntry": lpAruRxFflThreshEntry,
       "lpAruRxFflThreshIndex": lpAruRxFflThreshIndex,
       "lpAruRxFflThreshValue": lpAruRxFflThreshValue,
       "lpEngArc": lpEngArc,
       "lpEngArcRowStatusTable": lpEngArcRowStatusTable,
       "lpEngArcRowStatusEntry": lpEngArcRowStatusEntry,
       "lpEngArcRowStatus": lpEngArcRowStatus,
       "lpEngArcComponentName": lpEngArcComponentName,
       "lpEngArcStorageType": lpEngArcStorageType,
       "lpEngArcIndex": lpEngArcIndex,
       "lpEngArcOv": lpEngArcOv,
       "lpEngArcOvRowStatusTable": lpEngArcOvRowStatusTable,
       "lpEngArcOvRowStatusEntry": lpEngArcOvRowStatusEntry,
       "lpEngArcOvRowStatus": lpEngArcOvRowStatus,
       "lpEngArcOvComponentName": lpEngArcOvComponentName,
       "lpEngArcOvStorageType": lpEngArcOvStorageType,
       "lpEngArcOvIndex": lpEngArcOvIndex,
       "lpEngArcOvProvTable": lpEngArcOvProvTable,
       "lpEngArcOvProvEntry": lpEngArcOvProvEntry,
       "lpEngArcOvTotalConnectionPoolCapacity": lpEngArcOvTotalConnectionPoolCapacity,
       "lpEngArcOvMulticastBranchesCapacity": lpEngArcOvMulticastBranchesCapacity,
       "lpEngArcOvTxCellMemoryAllocation": lpEngArcOvTxCellMemoryAllocation,
       "lpEngArcOvRxCellMemoryAllocation": lpEngArcOvRxCellMemoryAllocation,
       "lpEngArcCqc": lpEngArcCqc,
       "lpEngArcCqcRowStatusTable": lpEngArcCqcRowStatusTable,
       "lpEngArcCqcRowStatusEntry": lpEngArcCqcRowStatusEntry,
       "lpEngArcCqcRowStatus": lpEngArcCqcRowStatus,
       "lpEngArcCqcComponentName": lpEngArcCqcComponentName,
       "lpEngArcCqcStorageType": lpEngArcCqcStorageType,
       "lpEngArcCqcIndex": lpEngArcCqcIndex,
       "lpEngArcCqcOv": lpEngArcCqcOv,
       "lpEngArcCqcOvRowStatusTable": lpEngArcCqcOvRowStatusTable,
       "lpEngArcCqcOvRowStatusEntry": lpEngArcCqcOvRowStatusEntry,
       "lpEngArcCqcOvRowStatus": lpEngArcCqcOvRowStatus,
       "lpEngArcCqcOvComponentName": lpEngArcCqcOvComponentName,
       "lpEngArcCqcOvStorageType": lpEngArcCqcOvStorageType,
       "lpEngArcCqcOvIndex": lpEngArcCqcOvIndex,
       "lpEngArcCqcOvProvTable": lpEngArcCqcOvProvTable,
       "lpEngArcCqcOvProvEntry": lpEngArcCqcOvProvEntry,
       "lpEngArcCqcOvPerVcQueueInterfaces": lpEngArcCqcOvPerVcQueueInterfaces,
       "lpEngArcCqcOvShapingScalingFactor": lpEngArcCqcOvShapingScalingFactor,
       "lpEngArcCqcOvCdvReduction": lpEngArcCqcOvCdvReduction,
       "lpEngArcCqcOvPortCongestionPolicy": lpEngArcCqcOvPortCongestionPolicy,
       "lpEngArcCqcOvConnCapTable": lpEngArcCqcOvConnCapTable,
       "lpEngArcCqcOvConnCapEntry": lpEngArcCqcOvConnCapEntry,
       "lpEngArcCqcOvConnCapIndex": lpEngArcCqcOvConnCapIndex,
       "lpEngArcCqcOvConnCapValue": lpEngArcCqcOvConnCapValue,
       "lpEngArcCqcOperTable": lpEngArcCqcOperTable,
       "lpEngArcCqcOperEntry": lpEngArcCqcOperEntry,
       "lpEngArcCqcCdvReduction": lpEngArcCqcCdvReduction,
       "lpEngArcAqm": lpEngArcAqm,
       "lpEngArcAqmRowStatusTable": lpEngArcAqmRowStatusTable,
       "lpEngArcAqmRowStatusEntry": lpEngArcAqmRowStatusEntry,
       "lpEngArcAqmRowStatus": lpEngArcAqmRowStatus,
       "lpEngArcAqmComponentName": lpEngArcAqmComponentName,
       "lpEngArcAqmStorageType": lpEngArcAqmStorageType,
       "lpEngArcAqmIndex": lpEngArcAqmIndex,
       "lpEngArcAqmOv": lpEngArcAqmOv,
       "lpEngArcAqmOvRowStatusTable": lpEngArcAqmOvRowStatusTable,
       "lpEngArcAqmOvRowStatusEntry": lpEngArcAqmOvRowStatusEntry,
       "lpEngArcAqmOvRowStatus": lpEngArcAqmOvRowStatus,
       "lpEngArcAqmOvComponentName": lpEngArcAqmOvComponentName,
       "lpEngArcAqmOvStorageType": lpEngArcAqmOvStorageType,
       "lpEngArcAqmOvIndex": lpEngArcAqmOvIndex,
       "lpEngArcAqmOvProvTable": lpEngArcAqmOvProvTable,
       "lpEngArcAqmOvProvEntry": lpEngArcAqmOvProvEntry,
       "lpEngArcAqmOvConnectionPoolCapacity": lpEngArcAqmOvConnectionPoolCapacity,
       "lpEngArcAqmOvHighPriorityEpdOffset": lpEngArcAqmOvHighPriorityEpdOffset,
       "lpEngArcAqmOvLowPriorityEpdOffset": lpEngArcAqmOvLowPriorityEpdOffset,
       "lpEngArcAqmOvPortCongestionPolicy": lpEngArcAqmOvPortCongestionPolicy,
       "lpEngArcAqmOvMaxVirtualLinks": lpEngArcAqmOvMaxVirtualLinks,
       "lpEngArcAqmOvVirtualLinkGranularity": lpEngArcAqmOvVirtualLinkGranularity,
       "lpEngArcAqmOperTable": lpEngArcAqmOperTable,
       "lpEngArcAqmOperEntry": lpEngArcAqmOperEntry,
       "lpEngArcAqmConnectionPoolAvailable": lpEngArcAqmConnectionPoolAvailable,
       "lpEngArcAqmConnectionPoolUsage": lpEngArcAqmConnectionPoolUsage,
       "lpEngArcAqmTxCellMemoryAvailable": lpEngArcAqmTxCellMemoryAvailable,
       "lpEngArcAqmTxCellMemoryMinAvailable": lpEngArcAqmTxCellMemoryMinAvailable,
       "lpEngArcAqmTxCellMemoryCongestionState": lpEngArcAqmTxCellMemoryCongestionState,
       "lpEngArcAqmTxCellMemoryMaxUsage": lpEngArcAqmTxCellMemoryMaxUsage,
       "lpEngArcAqmTxCellMemoryUsage": lpEngArcAqmTxCellMemoryUsage,
       "lpEngArcAqmMaxVirtualLinks": lpEngArcAqmMaxVirtualLinks,
       "lpEngArcAqmVirtualLinkUsage": lpEngArcAqmVirtualLinkUsage,
       "lpEngArcAqmVirtualLinkGranularity": lpEngArcAqmVirtualLinkGranularity,
       "lpEngArcAqmTxCellThreshTable": lpEngArcAqmTxCellThreshTable,
       "lpEngArcAqmTxCellThreshEntry": lpEngArcAqmTxCellThreshEntry,
       "lpEngArcAqmTxCellThreshIndex": lpEngArcAqmTxCellThreshIndex,
       "lpEngArcAqmTxCellThreshValue": lpEngArcAqmTxCellThreshValue,
       "lpEngArcOperTable": lpEngArcOperTable,
       "lpEngArcOperEntry": lpEngArcOperEntry,
       "lpEngArcTotalConnectionPoolAvailable": lpEngArcTotalConnectionPoolAvailable,
       "lpEngArcTotalConnectionPoolUsage": lpEngArcTotalConnectionPoolUsage,
       "lpEngArcMulticastBranchesAvailable": lpEngArcMulticastBranchesAvailable,
       "lpEngArcMulticastBranchesUsage": lpEngArcMulticastBranchesUsage,
       "lpEngArcTxCellMemoryAllocation": lpEngArcTxCellMemoryAllocation,
       "lpEngArcTxCellMemoryAvailable": lpEngArcTxCellMemoryAvailable,
       "lpEngArcTxCellMemoryMinAvailable": lpEngArcTxCellMemoryMinAvailable,
       "lpEngArcTxCellMemoryCongestionState": lpEngArcTxCellMemoryCongestionState,
       "lpEngArcRxCellMemoryAllocation": lpEngArcRxCellMemoryAllocation,
       "lpEngArcRxCellMemoryAvailable": lpEngArcRxCellMemoryAvailable,
       "lpEngArcRxCellMemoryMinAvailable": lpEngArcRxCellMemoryMinAvailable,
       "lpEngArcRxCellMemoryCongestionState": lpEngArcRxCellMemoryCongestionState,
       "lpEngArcTxCellMemoryMaxUsage": lpEngArcTxCellMemoryMaxUsage,
       "lpEngArcTxCellMemoryUsage": lpEngArcTxCellMemoryUsage,
       "lpEngArcRxCellMemoryMaxUsage": lpEngArcRxCellMemoryMaxUsage,
       "lpEngArcRxCellMemoryUsage": lpEngArcRxCellMemoryUsage,
       "lpEngArcTxCellThreshTable": lpEngArcTxCellThreshTable,
       "lpEngArcTxCellThreshEntry": lpEngArcTxCellThreshEntry,
       "lpEngArcTxCellThreshIndex": lpEngArcTxCellThreshIndex,
       "lpEngArcTxCellThreshValue": lpEngArcTxCellThreshValue,
       "lpEngArcRxCellThreshTable": lpEngArcRxCellThreshTable,
       "lpEngArcRxCellThreshEntry": lpEngArcRxCellThreshEntry,
       "lpEngArcRxCellThreshIndex": lpEngArcRxCellThreshIndex,
       "lpEngArcRxCellThreshValue": lpEngArcRxCellThreshValue,
       "lpEngFcrc": lpEngFcrc,
       "lpEngFcrcRowStatusTable": lpEngFcrcRowStatusTable,
       "lpEngFcrcRowStatusEntry": lpEngFcrcRowStatusEntry,
       "lpEngFcrcRowStatus": lpEngFcrcRowStatus,
       "lpEngFcrcComponentName": lpEngFcrcComponentName,
       "lpEngFcrcStorageType": lpEngFcrcStorageType,
       "lpEngFcrcIndex": lpEngFcrcIndex,
       "lpEngFcrcOv": lpEngFcrcOv,
       "lpEngFcrcOvRowStatusTable": lpEngFcrcOvRowStatusTable,
       "lpEngFcrcOvRowStatusEntry": lpEngFcrcOvRowStatusEntry,
       "lpEngFcrcOvRowStatus": lpEngFcrcOvRowStatus,
       "lpEngFcrcOvComponentName": lpEngFcrcOvComponentName,
       "lpEngFcrcOvStorageType": lpEngFcrcOvStorageType,
       "lpEngFcrcOvIndex": lpEngFcrcOvIndex,
       "lpEngFcrcOvProvTable": lpEngFcrcOvProvTable,
       "lpEngFcrcOvProvEntry": lpEngFcrcOvProvEntry,
       "lpEngFcrcOvSubConnectionPoolCapacity": lpEngFcrcOvSubConnectionPoolCapacity,
       "lpEngFcrcOvLnnConnectionPoolCapacity": lpEngFcrcOvLnnConnectionPoolCapacity,
       "lpEngFcrcPqc": lpEngFcrcPqc,
       "lpEngFcrcPqcRowStatusTable": lpEngFcrcPqcRowStatusTable,
       "lpEngFcrcPqcRowStatusEntry": lpEngFcrcPqcRowStatusEntry,
       "lpEngFcrcPqcRowStatus": lpEngFcrcPqcRowStatus,
       "lpEngFcrcPqcComponentName": lpEngFcrcPqcComponentName,
       "lpEngFcrcPqcStorageType": lpEngFcrcPqcStorageType,
       "lpEngFcrcPqcIndex": lpEngFcrcPqcIndex,
       "lpEngFcrcPqcOv": lpEngFcrcPqcOv,
       "lpEngFcrcPqcOvRowStatusTable": lpEngFcrcPqcOvRowStatusTable,
       "lpEngFcrcPqcOvRowStatusEntry": lpEngFcrcPqcOvRowStatusEntry,
       "lpEngFcrcPqcOvRowStatus": lpEngFcrcPqcOvRowStatus,
       "lpEngFcrcPqcOvComponentName": lpEngFcrcPqcOvComponentName,
       "lpEngFcrcPqcOvStorageType": lpEngFcrcPqcOvStorageType,
       "lpEngFcrcPqcOvIndex": lpEngFcrcPqcOvIndex,
       "lpEngFcrcPqcOvProvTable": lpEngFcrcPqcOvProvTable,
       "lpEngFcrcPqcOvProvEntry": lpEngFcrcPqcOvProvEntry,
       "lpEngFcrcPqcOvIpRoutesPoolCapacity": lpEngFcrcPqcOvIpRoutesPoolCapacity,
       "lpEngFcrcPqcOperTable": lpEngFcrcPqcOperTable,
       "lpEngFcrcPqcOperEntry": lpEngFcrcPqcOperEntry,
       "lpEngFcrcPqcIpRoutesPoolSize": lpEngFcrcPqcIpRoutesPoolSize,
       "lpEngFcrcPqcIpRoutesPoolUsage": lpEngFcrcPqcIpRoutesPoolUsage,
       "lpEngFcrcPqcIpRoutesPoolAvailableEst": lpEngFcrcPqcIpRoutesPoolAvailableEst,
       "lpEngFcrcOperTable": lpEngFcrcOperTable,
       "lpEngFcrcOperEntry": lpEngFcrcOperEntry,
       "lpEngFcrcSubConnectionPoolAvailable": lpEngFcrcSubConnectionPoolAvailable,
       "lpEngFcrcSubConnectionPoolUsage": lpEngFcrcSubConnectionPoolUsage,
       "lpEngFcrcLnnConnectionPoolAvailable": lpEngFcrcLnnConnectionPoolAvailable,
       "lpEngFcrcLnnConnectionPoolUsage": lpEngFcrcLnnConnectionPoolUsage,
       "lpEngFcrcTxFrameMemoryAvailable": lpEngFcrcTxFrameMemoryAvailable,
       "lpEngFcrcTxFrameMemoryMinAvailable": lpEngFcrcTxFrameMemoryMinAvailable,
       "lpEngFcrcTxFrameMemoryCongestionState": lpEngFcrcTxFrameMemoryCongestionState,
       "lpEngFcrcRxFrameMemoryAvailable": lpEngFcrcRxFrameMemoryAvailable,
       "lpEngFcrcRxFrameMemoryMinAvailable": lpEngFcrcRxFrameMemoryMinAvailable,
       "lpEngFcrcRxFrameMemoryCongestionState": lpEngFcrcRxFrameMemoryCongestionState,
       "lpEngFcrcTxFrameMemoryMaxUsage": lpEngFcrcTxFrameMemoryMaxUsage,
       "lpEngFcrcTxFrameMemoryUsage": lpEngFcrcTxFrameMemoryUsage,
       "lpEngFcrcRxFrameMemoryMaxUsage": lpEngFcrcRxFrameMemoryMaxUsage,
       "lpEngFcrcRxFrameMemoryUsage": lpEngFcrcRxFrameMemoryUsage,
       "lpEngFcrcTxFrThreshTable": lpEngFcrcTxFrThreshTable,
       "lpEngFcrcTxFrThreshEntry": lpEngFcrcTxFrThreshEntry,
       "lpEngFcrcTxFrThreshIndex": lpEngFcrcTxFrThreshIndex,
       "lpEngFcrcTxFrThreshValue": lpEngFcrcTxFrThreshValue,
       "lpEngFcrcRxFrThreshTable": lpEngFcrcRxFrThreshTable,
       "lpEngFcrcRxFrThreshEntry": lpEngFcrcRxFrThreshEntry,
       "lpEngFcrcRxFrThreshIndex": lpEngFcrcRxFrThreshIndex,
       "lpEngFcrcRxFrThreshValue": lpEngFcrcRxFrThreshValue,
       "atmBaseMIB": atmBaseMIB,
       "atmBaseGroup": atmBaseGroup,
       "atmBaseGroupBE": atmBaseGroupBE,
       "atmBaseGroupBE00": atmBaseGroupBE00,
       "atmBaseGroupBE00A": atmBaseGroupBE00A,
       "atmBaseCapabilities": atmBaseCapabilities,
       "atmBaseCapabilitiesBE": atmBaseCapabilitiesBE,
       "atmBaseCapabilitiesBE00": atmBaseCapabilitiesBE00,
       "atmBaseCapabilitiesBE00A": atmBaseCapabilitiesBE00A}
)
