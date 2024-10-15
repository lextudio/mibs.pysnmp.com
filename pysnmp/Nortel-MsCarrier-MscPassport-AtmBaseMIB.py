# SNMP MIB module (Nortel-MsCarrier-MscPassport-AtmBaseMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-AtmBaseMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:47 2024
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

(mscLp,
 mscLpEng,
 mscLpEngIndex,
 mscLpIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB",
    "mscLp",
    "mscLpEng",
    "mscLpEngIndex",
    "mscLpIndex")

(DisplayString,
 Gauge32,
 Integer32,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(FixedPoint1,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "FixedPoint1",
    "NonReplicated")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
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

_MscLpArc_ObjectIdentity = ObjectIdentity
mscLpArc = _MscLpArc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 19)
)
_MscLpArcRowStatusTable_Object = MibTable
mscLpArcRowStatusTable = _MscLpArcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 19, 1)
)
if mibBuilder.loadTexts:
    mscLpArcRowStatusTable.setStatus("obsolete")
_MscLpArcRowStatusEntry_Object = MibTableRow
mscLpArcRowStatusEntry = _MscLpArcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 19, 1, 1)
)
mscLpArcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpArcIndex"),
)
if mibBuilder.loadTexts:
    mscLpArcRowStatusEntry.setStatus("obsolete")
_MscLpArcRowStatus_Type = RowStatus
_MscLpArcRowStatus_Object = MibTableColumn
mscLpArcRowStatus = _MscLpArcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 19, 1, 1, 1),
    _MscLpArcRowStatus_Type()
)
mscLpArcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpArcRowStatus.setStatus("obsolete")
_MscLpArcComponentName_Type = DisplayString
_MscLpArcComponentName_Object = MibTableColumn
mscLpArcComponentName = _MscLpArcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 19, 1, 1, 2),
    _MscLpArcComponentName_Type()
)
mscLpArcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpArcComponentName.setStatus("obsolete")
_MscLpArcStorageType_Type = StorageType
_MscLpArcStorageType_Object = MibTableColumn
mscLpArcStorageType = _MscLpArcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 19, 1, 1, 4),
    _MscLpArcStorageType_Type()
)
mscLpArcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpArcStorageType.setStatus("obsolete")
_MscLpArcIndex_Type = NonReplicated
_MscLpArcIndex_Object = MibTableColumn
mscLpArcIndex = _MscLpArcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 19, 1, 1, 10),
    _MscLpArcIndex_Type()
)
mscLpArcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpArcIndex.setStatus("obsolete")
_MscLpArcProvTable_Object = MibTable
mscLpArcProvTable = _MscLpArcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 19, 100)
)
if mibBuilder.loadTexts:
    mscLpArcProvTable.setStatus("obsolete")
_MscLpArcProvEntry_Object = MibTableRow
mscLpArcProvEntry = _MscLpArcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 19, 100, 1)
)
mscLpArcProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpArcIndex"),
)
if mibBuilder.loadTexts:
    mscLpArcProvEntry.setStatus("obsolete")


class _MscLpArcTotalConnectionPoolCapacity_Type(Unsigned32):
    """Custom type mscLpArcTotalConnectionPoolCapacity based on Unsigned32"""
    defaultValue = 3072

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10752),
    )


_MscLpArcTotalConnectionPoolCapacity_Type.__name__ = "Unsigned32"
_MscLpArcTotalConnectionPoolCapacity_Object = MibTableColumn
mscLpArcTotalConnectionPoolCapacity = _MscLpArcTotalConnectionPoolCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 19, 100, 1, 5),
    _MscLpArcTotalConnectionPoolCapacity_Type()
)
mscLpArcTotalConnectionPoolCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpArcTotalConnectionPoolCapacity.setStatus("obsolete")


class _MscLpArcMulticastBranchesCapacity_Type(Unsigned32):
    """Custom type mscLpArcMulticastBranchesCapacity based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10752),
    )


_MscLpArcMulticastBranchesCapacity_Type.__name__ = "Unsigned32"
_MscLpArcMulticastBranchesCapacity_Object = MibTableColumn
mscLpArcMulticastBranchesCapacity = _MscLpArcMulticastBranchesCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 19, 100, 1, 6),
    _MscLpArcMulticastBranchesCapacity_Type()
)
mscLpArcMulticastBranchesCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpArcMulticastBranchesCapacity.setStatus("obsolete")


class _MscLpArcTxFrameMemoryAllocation_Type(Unsigned32):
    """Custom type mscLpArcTxFrameMemoryAllocation based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscLpArcTxFrameMemoryAllocation_Type.__name__ = "Unsigned32"
_MscLpArcTxFrameMemoryAllocation_Object = MibTableColumn
mscLpArcTxFrameMemoryAllocation = _MscLpArcTxFrameMemoryAllocation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 19, 100, 1, 10),
    _MscLpArcTxFrameMemoryAllocation_Type()
)
mscLpArcTxFrameMemoryAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpArcTxFrameMemoryAllocation.setStatus("obsolete")


class _MscLpArcRxFrameMemoryAllocation_Type(Unsigned32):
    """Custom type mscLpArcRxFrameMemoryAllocation based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscLpArcRxFrameMemoryAllocation_Type.__name__ = "Unsigned32"
_MscLpArcRxFrameMemoryAllocation_Object = MibTableColumn
mscLpArcRxFrameMemoryAllocation = _MscLpArcRxFrameMemoryAllocation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 19, 100, 1, 20),
    _MscLpArcRxFrameMemoryAllocation_Type()
)
mscLpArcRxFrameMemoryAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpArcRxFrameMemoryAllocation.setStatus("obsolete")


class _MscLpArcPerVcQueueInterfaces_Type(Unsigned32):
    """Custom type mscLpArcPerVcQueueInterfaces based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscLpArcPerVcQueueInterfaces_Type.__name__ = "Unsigned32"
_MscLpArcPerVcQueueInterfaces_Object = MibTableColumn
mscLpArcPerVcQueueInterfaces = _MscLpArcPerVcQueueInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 19, 100, 1, 25),
    _MscLpArcPerVcQueueInterfaces_Type()
)
mscLpArcPerVcQueueInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpArcPerVcQueueInterfaces.setStatus("obsolete")


class _MscLpArcShapingStackAllocation_Type(OctetString):
    """Custom type mscLpArcShapingStackAllocation based on OctetString"""
    defaultHexValue = "80"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscLpArcShapingStackAllocation_Type.__name__ = "OctetString"
_MscLpArcShapingStackAllocation_Object = MibTableColumn
mscLpArcShapingStackAllocation = _MscLpArcShapingStackAllocation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 19, 100, 1, 30),
    _MscLpArcShapingStackAllocation_Type()
)
mscLpArcShapingStackAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpArcShapingStackAllocation.setStatus("obsolete")


class _MscLpArcShapingScalingFactor_Type(FixedPoint1):
    """Custom type mscLpArcShapingScalingFactor based on FixedPoint1"""
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


_MscLpArcShapingScalingFactor_Type.__name__ = "FixedPoint1"
_MscLpArcShapingScalingFactor_Object = MibTableColumn
mscLpArcShapingScalingFactor = _MscLpArcShapingScalingFactor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 19, 100, 1, 40),
    _MscLpArcShapingScalingFactor_Type()
)
mscLpArcShapingScalingFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpArcShapingScalingFactor.setStatus("obsolete")


class _MscLpArcCdvAttenuation_Type(Integer32):
    """Custom type mscLpArcCdvAttenuation based on Integer32"""
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


_MscLpArcCdvAttenuation_Type.__name__ = "Integer32"
_MscLpArcCdvAttenuation_Object = MibTableColumn
mscLpArcCdvAttenuation = _MscLpArcCdvAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 19, 100, 1, 41),
    _MscLpArcCdvAttenuation_Type()
)
mscLpArcCdvAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpArcCdvAttenuation.setStatus("obsolete")


class _MscLpArcPortAggregation_Type(Integer32):
    """Custom type mscLpArcPortAggregation based on Integer32"""
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


_MscLpArcPortAggregation_Type.__name__ = "Integer32"
_MscLpArcPortAggregation_Object = MibTableColumn
mscLpArcPortAggregation = _MscLpArcPortAggregation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 19, 100, 1, 42),
    _MscLpArcPortAggregation_Type()
)
mscLpArcPortAggregation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpArcPortAggregation.setStatus("obsolete")


class _MscLpArcSubConnectionPoolCapacity_Type(Unsigned32):
    """Custom type mscLpArcSubConnectionPoolCapacity based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_MscLpArcSubConnectionPoolCapacity_Type.__name__ = "Unsigned32"
_MscLpArcSubConnectionPoolCapacity_Object = MibTableColumn
mscLpArcSubConnectionPoolCapacity = _MscLpArcSubConnectionPoolCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 19, 100, 1, 43),
    _MscLpArcSubConnectionPoolCapacity_Type()
)
mscLpArcSubConnectionPoolCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpArcSubConnectionPoolCapacity.setStatus("obsolete")


class _MscLpArcLnnConnectionPoolCapacity_Type(Unsigned32):
    """Custom type mscLpArcLnnConnectionPoolCapacity based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_MscLpArcLnnConnectionPoolCapacity_Type.__name__ = "Unsigned32"
_MscLpArcLnnConnectionPoolCapacity_Object = MibTableColumn
mscLpArcLnnConnectionPoolCapacity = _MscLpArcLnnConnectionPoolCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 19, 100, 1, 44),
    _MscLpArcLnnConnectionPoolCapacity_Type()
)
mscLpArcLnnConnectionPoolCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpArcLnnConnectionPoolCapacity.setStatus("obsolete")
_MscLpArcConnCapTable_Object = MibTable
mscLpArcConnCapTable = _MscLpArcConnCapTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 19, 291)
)
if mibBuilder.loadTexts:
    mscLpArcConnCapTable.setStatus("obsolete")
_MscLpArcConnCapEntry_Object = MibTableRow
mscLpArcConnCapEntry = _MscLpArcConnCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 19, 291, 1)
)
mscLpArcConnCapEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpArcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpArcConnCapIndex"),
)
if mibBuilder.loadTexts:
    mscLpArcConnCapEntry.setStatus("obsolete")


class _MscLpArcConnCapIndex_Type(Integer32):
    """Custom type mscLpArcConnCapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscLpArcConnCapIndex_Type.__name__ = "Integer32"
_MscLpArcConnCapIndex_Object = MibTableColumn
mscLpArcConnCapIndex = _MscLpArcConnCapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 19, 291, 1, 1),
    _MscLpArcConnCapIndex_Type()
)
mscLpArcConnCapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpArcConnCapIndex.setStatus("obsolete")


class _MscLpArcConnCapValue_Type(Unsigned32):
    """Custom type mscLpArcConnCapValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 4096),
    )


_MscLpArcConnCapValue_Type.__name__ = "Unsigned32"
_MscLpArcConnCapValue_Object = MibTableColumn
mscLpArcConnCapValue = _MscLpArcConnCapValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 19, 291, 1, 2),
    _MscLpArcConnCapValue_Type()
)
mscLpArcConnCapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpArcConnCapValue.setStatus("obsolete")
_MscLpAru_ObjectIdentity = ObjectIdentity
mscLpAru = _MscLpAru_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20)
)
_MscLpAruRowStatusTable_Object = MibTable
mscLpAruRowStatusTable = _MscLpAruRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 1)
)
if mibBuilder.loadTexts:
    mscLpAruRowStatusTable.setStatus("obsolete")
_MscLpAruRowStatusEntry_Object = MibTableRow
mscLpAruRowStatusEntry = _MscLpAruRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 1, 1)
)
mscLpAruRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpAruIndex"),
)
if mibBuilder.loadTexts:
    mscLpAruRowStatusEntry.setStatus("obsolete")
_MscLpAruRowStatus_Type = RowStatus
_MscLpAruRowStatus_Object = MibTableColumn
mscLpAruRowStatus = _MscLpAruRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 1, 1, 1),
    _MscLpAruRowStatus_Type()
)
mscLpAruRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruRowStatus.setStatus("obsolete")
_MscLpAruComponentName_Type = DisplayString
_MscLpAruComponentName_Object = MibTableColumn
mscLpAruComponentName = _MscLpAruComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 1, 1, 2),
    _MscLpAruComponentName_Type()
)
mscLpAruComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruComponentName.setStatus("obsolete")
_MscLpAruStorageType_Type = StorageType
_MscLpAruStorageType_Object = MibTableColumn
mscLpAruStorageType = _MscLpAruStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 1, 1, 4),
    _MscLpAruStorageType_Type()
)
mscLpAruStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruStorageType.setStatus("obsolete")
_MscLpAruIndex_Type = NonReplicated
_MscLpAruIndex_Object = MibTableColumn
mscLpAruIndex = _MscLpAruIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 1, 1, 10),
    _MscLpAruIndex_Type()
)
mscLpAruIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpAruIndex.setStatus("obsolete")
_MscLpAruOperTable_Object = MibTable
mscLpAruOperTable = _MscLpAruOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 100)
)
if mibBuilder.loadTexts:
    mscLpAruOperTable.setStatus("obsolete")
_MscLpAruOperEntry_Object = MibTableRow
mscLpAruOperEntry = _MscLpAruOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 100, 1)
)
mscLpAruOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpAruIndex"),
)
if mibBuilder.loadTexts:
    mscLpAruOperEntry.setStatus("obsolete")


class _MscLpAruTotalConnectionPoolUsage_Type(Unsigned32):
    """Custom type mscLpAruTotalConnectionPoolUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10752),
    )


_MscLpAruTotalConnectionPoolUsage_Type.__name__ = "Unsigned32"
_MscLpAruTotalConnectionPoolUsage_Object = MibTableColumn
mscLpAruTotalConnectionPoolUsage = _MscLpAruTotalConnectionPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 100, 1, 5),
    _MscLpAruTotalConnectionPoolUsage_Type()
)
mscLpAruTotalConnectionPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruTotalConnectionPoolUsage.setStatus("obsolete")


class _MscLpAruMulticastBranchesUsage_Type(Unsigned32):
    """Custom type mscLpAruMulticastBranchesUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10752),
    )


_MscLpAruMulticastBranchesUsage_Type.__name__ = "Unsigned32"
_MscLpAruMulticastBranchesUsage_Object = MibTableColumn
mscLpAruMulticastBranchesUsage = _MscLpAruMulticastBranchesUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 100, 1, 6),
    _MscLpAruMulticastBranchesUsage_Type()
)
mscLpAruMulticastBranchesUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruMulticastBranchesUsage.setStatus("obsolete")


class _MscLpAruTxCellBlockCapacity_Type(Unsigned32):
    """Custom type mscLpAruTxCellBlockCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_MscLpAruTxCellBlockCapacity_Type.__name__ = "Unsigned32"
_MscLpAruTxCellBlockCapacity_Object = MibTableColumn
mscLpAruTxCellBlockCapacity = _MscLpAruTxCellBlockCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 100, 1, 10),
    _MscLpAruTxCellBlockCapacity_Type()
)
mscLpAruTxCellBlockCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruTxCellBlockCapacity.setStatus("obsolete")


class _MscLpAruTxCellBlockUsage_Type(Gauge32):
    """Custom type mscLpAruTxCellBlockUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_MscLpAruTxCellBlockUsage_Type.__name__ = "Gauge32"
_MscLpAruTxCellBlockUsage_Object = MibTableColumn
mscLpAruTxCellBlockUsage = _MscLpAruTxCellBlockUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 100, 1, 20),
    _MscLpAruTxCellBlockUsage_Type()
)
mscLpAruTxCellBlockUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruTxCellBlockUsage.setStatus("obsolete")


class _MscLpAruTxCellFreeListSize_Type(Unsigned32):
    """Custom type mscLpAruTxCellFreeListSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_MscLpAruTxCellFreeListSize_Type.__name__ = "Unsigned32"
_MscLpAruTxCellFreeListSize_Object = MibTableColumn
mscLpAruTxCellFreeListSize = _MscLpAruTxCellFreeListSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 100, 1, 23),
    _MscLpAruTxCellFreeListSize_Type()
)
mscLpAruTxCellFreeListSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruTxCellFreeListSize.setStatus("obsolete")


class _MscLpAruTxCellFreeListCongestionState_Type(Integer32):
    """Custom type mscLpAruTxCellFreeListCongestionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscLpAruTxCellFreeListCongestionState_Type.__name__ = "Integer32"
_MscLpAruTxCellFreeListCongestionState_Object = MibTableColumn
mscLpAruTxCellFreeListCongestionState = _MscLpAruTxCellFreeListCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 100, 1, 26),
    _MscLpAruTxCellFreeListCongestionState_Type()
)
mscLpAruTxCellFreeListCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruTxCellFreeListCongestionState.setStatus("obsolete")


class _MscLpAruTxFrameMemoryAllocation_Type(Unsigned32):
    """Custom type mscLpAruTxFrameMemoryAllocation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscLpAruTxFrameMemoryAllocation_Type.__name__ = "Unsigned32"
_MscLpAruTxFrameMemoryAllocation_Object = MibTableColumn
mscLpAruTxFrameMemoryAllocation = _MscLpAruTxFrameMemoryAllocation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 100, 1, 30),
    _MscLpAruTxFrameMemoryAllocation_Type()
)
mscLpAruTxFrameMemoryAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruTxFrameMemoryAllocation.setStatus("obsolete")


class _MscLpAruTxFrameBlockCapacity_Type(Unsigned32):
    """Custom type mscLpAruTxFrameBlockCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_MscLpAruTxFrameBlockCapacity_Type.__name__ = "Unsigned32"
_MscLpAruTxFrameBlockCapacity_Object = MibTableColumn
mscLpAruTxFrameBlockCapacity = _MscLpAruTxFrameBlockCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 100, 1, 40),
    _MscLpAruTxFrameBlockCapacity_Type()
)
mscLpAruTxFrameBlockCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruTxFrameBlockCapacity.setStatus("obsolete")


class _MscLpAruTxFrameBlockUsage_Type(Gauge32):
    """Custom type mscLpAruTxFrameBlockUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_MscLpAruTxFrameBlockUsage_Type.__name__ = "Gauge32"
_MscLpAruTxFrameBlockUsage_Object = MibTableColumn
mscLpAruTxFrameBlockUsage = _MscLpAruTxFrameBlockUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 100, 1, 50),
    _MscLpAruTxFrameBlockUsage_Type()
)
mscLpAruTxFrameBlockUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruTxFrameBlockUsage.setStatus("obsolete")


class _MscLpAruTxFrameFreeListSize_Type(Unsigned32):
    """Custom type mscLpAruTxFrameFreeListSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_MscLpAruTxFrameFreeListSize_Type.__name__ = "Unsigned32"
_MscLpAruTxFrameFreeListSize_Object = MibTableColumn
mscLpAruTxFrameFreeListSize = _MscLpAruTxFrameFreeListSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 100, 1, 53),
    _MscLpAruTxFrameFreeListSize_Type()
)
mscLpAruTxFrameFreeListSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruTxFrameFreeListSize.setStatus("obsolete")


class _MscLpAruTxFrameFreeListCongestionState_Type(Integer32):
    """Custom type mscLpAruTxFrameFreeListCongestionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscLpAruTxFrameFreeListCongestionState_Type.__name__ = "Integer32"
_MscLpAruTxFrameFreeListCongestionState_Object = MibTableColumn
mscLpAruTxFrameFreeListCongestionState = _MscLpAruTxFrameFreeListCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 100, 1, 56),
    _MscLpAruTxFrameFreeListCongestionState_Type()
)
mscLpAruTxFrameFreeListCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruTxFrameFreeListCongestionState.setStatus("obsolete")


class _MscLpAruRxCellBlockCapacity_Type(Unsigned32):
    """Custom type mscLpAruRxCellBlockCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_MscLpAruRxCellBlockCapacity_Type.__name__ = "Unsigned32"
_MscLpAruRxCellBlockCapacity_Object = MibTableColumn
mscLpAruRxCellBlockCapacity = _MscLpAruRxCellBlockCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 100, 1, 60),
    _MscLpAruRxCellBlockCapacity_Type()
)
mscLpAruRxCellBlockCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruRxCellBlockCapacity.setStatus("obsolete")


class _MscLpAruRxCellBlockUsage_Type(Gauge32):
    """Custom type mscLpAruRxCellBlockUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_MscLpAruRxCellBlockUsage_Type.__name__ = "Gauge32"
_MscLpAruRxCellBlockUsage_Object = MibTableColumn
mscLpAruRxCellBlockUsage = _MscLpAruRxCellBlockUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 100, 1, 70),
    _MscLpAruRxCellBlockUsage_Type()
)
mscLpAruRxCellBlockUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruRxCellBlockUsage.setStatus("obsolete")


class _MscLpAruRxCellFreeListSize_Type(Unsigned32):
    """Custom type mscLpAruRxCellFreeListSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_MscLpAruRxCellFreeListSize_Type.__name__ = "Unsigned32"
_MscLpAruRxCellFreeListSize_Object = MibTableColumn
mscLpAruRxCellFreeListSize = _MscLpAruRxCellFreeListSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 100, 1, 73),
    _MscLpAruRxCellFreeListSize_Type()
)
mscLpAruRxCellFreeListSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruRxCellFreeListSize.setStatus("obsolete")


class _MscLpAruRxCellFreeListCongestionState_Type(Integer32):
    """Custom type mscLpAruRxCellFreeListCongestionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscLpAruRxCellFreeListCongestionState_Type.__name__ = "Integer32"
_MscLpAruRxCellFreeListCongestionState_Object = MibTableColumn
mscLpAruRxCellFreeListCongestionState = _MscLpAruRxCellFreeListCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 100, 1, 76),
    _MscLpAruRxCellFreeListCongestionState_Type()
)
mscLpAruRxCellFreeListCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruRxCellFreeListCongestionState.setStatus("obsolete")


class _MscLpAruRxFrameMemoryAllocation_Type(Unsigned32):
    """Custom type mscLpAruRxFrameMemoryAllocation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscLpAruRxFrameMemoryAllocation_Type.__name__ = "Unsigned32"
_MscLpAruRxFrameMemoryAllocation_Object = MibTableColumn
mscLpAruRxFrameMemoryAllocation = _MscLpAruRxFrameMemoryAllocation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 100, 1, 80),
    _MscLpAruRxFrameMemoryAllocation_Type()
)
mscLpAruRxFrameMemoryAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruRxFrameMemoryAllocation.setStatus("obsolete")


class _MscLpAruRxFrameBlockCapacity_Type(Unsigned32):
    """Custom type mscLpAruRxFrameBlockCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_MscLpAruRxFrameBlockCapacity_Type.__name__ = "Unsigned32"
_MscLpAruRxFrameBlockCapacity_Object = MibTableColumn
mscLpAruRxFrameBlockCapacity = _MscLpAruRxFrameBlockCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 100, 1, 90),
    _MscLpAruRxFrameBlockCapacity_Type()
)
mscLpAruRxFrameBlockCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruRxFrameBlockCapacity.setStatus("obsolete")


class _MscLpAruRxFrameBlockUsage_Type(Gauge32):
    """Custom type mscLpAruRxFrameBlockUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_MscLpAruRxFrameBlockUsage_Type.__name__ = "Gauge32"
_MscLpAruRxFrameBlockUsage_Object = MibTableColumn
mscLpAruRxFrameBlockUsage = _MscLpAruRxFrameBlockUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 100, 1, 100),
    _MscLpAruRxFrameBlockUsage_Type()
)
mscLpAruRxFrameBlockUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruRxFrameBlockUsage.setStatus("obsolete")


class _MscLpAruRxFrameFreeListSize_Type(Unsigned32):
    """Custom type mscLpAruRxFrameFreeListSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_MscLpAruRxFrameFreeListSize_Type.__name__ = "Unsigned32"
_MscLpAruRxFrameFreeListSize_Object = MibTableColumn
mscLpAruRxFrameFreeListSize = _MscLpAruRxFrameFreeListSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 100, 1, 103),
    _MscLpAruRxFrameFreeListSize_Type()
)
mscLpAruRxFrameFreeListSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruRxFrameFreeListSize.setStatus("obsolete")


class _MscLpAruRxFrameFreeListCongestionState_Type(Integer32):
    """Custom type mscLpAruRxFrameFreeListCongestionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscLpAruRxFrameFreeListCongestionState_Type.__name__ = "Integer32"
_MscLpAruRxFrameFreeListCongestionState_Object = MibTableColumn
mscLpAruRxFrameFreeListCongestionState = _MscLpAruRxFrameFreeListCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 100, 1, 106),
    _MscLpAruRxFrameFreeListCongestionState_Type()
)
mscLpAruRxFrameFreeListCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruRxFrameFreeListCongestionState.setStatus("obsolete")


class _MscLpAruSubConnectionPoolAvailable_Type(Unsigned32):
    """Custom type mscLpAruSubConnectionPoolAvailable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_MscLpAruSubConnectionPoolAvailable_Type.__name__ = "Unsigned32"
_MscLpAruSubConnectionPoolAvailable_Object = MibTableColumn
mscLpAruSubConnectionPoolAvailable = _MscLpAruSubConnectionPoolAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 100, 1, 107),
    _MscLpAruSubConnectionPoolAvailable_Type()
)
mscLpAruSubConnectionPoolAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruSubConnectionPoolAvailable.setStatus("obsolete")


class _MscLpAruSubConnectionPoolUsage_Type(Unsigned32):
    """Custom type mscLpAruSubConnectionPoolUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_MscLpAruSubConnectionPoolUsage_Type.__name__ = "Unsigned32"
_MscLpAruSubConnectionPoolUsage_Object = MibTableColumn
mscLpAruSubConnectionPoolUsage = _MscLpAruSubConnectionPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 100, 1, 108),
    _MscLpAruSubConnectionPoolUsage_Type()
)
mscLpAruSubConnectionPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruSubConnectionPoolUsage.setStatus("obsolete")


class _MscLpAruLnnConnectionPoolAvailable_Type(Unsigned32):
    """Custom type mscLpAruLnnConnectionPoolAvailable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_MscLpAruLnnConnectionPoolAvailable_Type.__name__ = "Unsigned32"
_MscLpAruLnnConnectionPoolAvailable_Object = MibTableColumn
mscLpAruLnnConnectionPoolAvailable = _MscLpAruLnnConnectionPoolAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 100, 1, 109),
    _MscLpAruLnnConnectionPoolAvailable_Type()
)
mscLpAruLnnConnectionPoolAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruLnnConnectionPoolAvailable.setStatus("obsolete")


class _MscLpAruLnnConnectionPoolUsage_Type(Unsigned32):
    """Custom type mscLpAruLnnConnectionPoolUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_MscLpAruLnnConnectionPoolUsage_Type.__name__ = "Unsigned32"
_MscLpAruLnnConnectionPoolUsage_Object = MibTableColumn
mscLpAruLnnConnectionPoolUsage = _MscLpAruLnnConnectionPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 100, 1, 110),
    _MscLpAruLnnConnectionPoolUsage_Type()
)
mscLpAruLnnConnectionPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruLnnConnectionPoolUsage.setStatus("obsolete")
_MscLpAruConnUsageTable_Object = MibTable
mscLpAruConnUsageTable = _MscLpAruConnUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 292)
)
if mibBuilder.loadTexts:
    mscLpAruConnUsageTable.setStatus("obsolete")
_MscLpAruConnUsageEntry_Object = MibTableRow
mscLpAruConnUsageEntry = _MscLpAruConnUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 292, 1)
)
mscLpAruConnUsageEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpAruIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpAruConnUsageIndex"),
)
if mibBuilder.loadTexts:
    mscLpAruConnUsageEntry.setStatus("obsolete")


class _MscLpAruConnUsageIndex_Type(Integer32):
    """Custom type mscLpAruConnUsageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscLpAruConnUsageIndex_Type.__name__ = "Integer32"
_MscLpAruConnUsageIndex_Object = MibTableColumn
mscLpAruConnUsageIndex = _MscLpAruConnUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 292, 1, 1),
    _MscLpAruConnUsageIndex_Type()
)
mscLpAruConnUsageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpAruConnUsageIndex.setStatus("obsolete")


class _MscLpAruConnUsageValue_Type(Unsigned32):
    """Custom type mscLpAruConnUsageValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000),
    )


_MscLpAruConnUsageValue_Type.__name__ = "Unsigned32"
_MscLpAruConnUsageValue_Object = MibTableColumn
mscLpAruConnUsageValue = _MscLpAruConnUsageValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 292, 1, 2),
    _MscLpAruConnUsageValue_Type()
)
mscLpAruConnUsageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruConnUsageValue.setStatus("obsolete")
_MscLpAruTxCflThreshTable_Object = MibTable
mscLpAruTxCflThreshTable = _MscLpAruTxCflThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 353)
)
if mibBuilder.loadTexts:
    mscLpAruTxCflThreshTable.setStatus("obsolete")
_MscLpAruTxCflThreshEntry_Object = MibTableRow
mscLpAruTxCflThreshEntry = _MscLpAruTxCflThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 353, 1)
)
mscLpAruTxCflThreshEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpAruIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpAruTxCflThreshIndex"),
)
if mibBuilder.loadTexts:
    mscLpAruTxCflThreshEntry.setStatus("obsolete")


class _MscLpAruTxCflThreshIndex_Type(Integer32):
    """Custom type mscLpAruTxCflThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscLpAruTxCflThreshIndex_Type.__name__ = "Integer32"
_MscLpAruTxCflThreshIndex_Object = MibTableColumn
mscLpAruTxCflThreshIndex = _MscLpAruTxCflThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 353, 1, 1),
    _MscLpAruTxCflThreshIndex_Type()
)
mscLpAruTxCflThreshIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpAruTxCflThreshIndex.setStatus("obsolete")


class _MscLpAruTxCflThreshValue_Type(Unsigned32):
    """Custom type mscLpAruTxCflThreshValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_MscLpAruTxCflThreshValue_Type.__name__ = "Unsigned32"
_MscLpAruTxCflThreshValue_Object = MibTableColumn
mscLpAruTxCflThreshValue = _MscLpAruTxCflThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 353, 1, 2),
    _MscLpAruTxCflThreshValue_Type()
)
mscLpAruTxCflThreshValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruTxCflThreshValue.setStatus("obsolete")
_MscLpAruTxFflThreshTable_Object = MibTable
mscLpAruTxFflThreshTable = _MscLpAruTxFflThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 354)
)
if mibBuilder.loadTexts:
    mscLpAruTxFflThreshTable.setStatus("obsolete")
_MscLpAruTxFflThreshEntry_Object = MibTableRow
mscLpAruTxFflThreshEntry = _MscLpAruTxFflThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 354, 1)
)
mscLpAruTxFflThreshEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpAruIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpAruTxFflThreshIndex"),
)
if mibBuilder.loadTexts:
    mscLpAruTxFflThreshEntry.setStatus("obsolete")


class _MscLpAruTxFflThreshIndex_Type(Integer32):
    """Custom type mscLpAruTxFflThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscLpAruTxFflThreshIndex_Type.__name__ = "Integer32"
_MscLpAruTxFflThreshIndex_Object = MibTableColumn
mscLpAruTxFflThreshIndex = _MscLpAruTxFflThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 354, 1, 1),
    _MscLpAruTxFflThreshIndex_Type()
)
mscLpAruTxFflThreshIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpAruTxFflThreshIndex.setStatus("obsolete")


class _MscLpAruTxFflThreshValue_Type(Unsigned32):
    """Custom type mscLpAruTxFflThreshValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_MscLpAruTxFflThreshValue_Type.__name__ = "Unsigned32"
_MscLpAruTxFflThreshValue_Object = MibTableColumn
mscLpAruTxFflThreshValue = _MscLpAruTxFflThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 354, 1, 2),
    _MscLpAruTxFflThreshValue_Type()
)
mscLpAruTxFflThreshValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruTxFflThreshValue.setStatus("obsolete")
_MscLpAruRxCflThreshTable_Object = MibTable
mscLpAruRxCflThreshTable = _MscLpAruRxCflThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 355)
)
if mibBuilder.loadTexts:
    mscLpAruRxCflThreshTable.setStatus("obsolete")
_MscLpAruRxCflThreshEntry_Object = MibTableRow
mscLpAruRxCflThreshEntry = _MscLpAruRxCflThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 355, 1)
)
mscLpAruRxCflThreshEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpAruIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpAruRxCflThreshIndex"),
)
if mibBuilder.loadTexts:
    mscLpAruRxCflThreshEntry.setStatus("obsolete")


class _MscLpAruRxCflThreshIndex_Type(Integer32):
    """Custom type mscLpAruRxCflThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscLpAruRxCflThreshIndex_Type.__name__ = "Integer32"
_MscLpAruRxCflThreshIndex_Object = MibTableColumn
mscLpAruRxCflThreshIndex = _MscLpAruRxCflThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 355, 1, 1),
    _MscLpAruRxCflThreshIndex_Type()
)
mscLpAruRxCflThreshIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpAruRxCflThreshIndex.setStatus("obsolete")


class _MscLpAruRxCflThreshValue_Type(Unsigned32):
    """Custom type mscLpAruRxCflThreshValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_MscLpAruRxCflThreshValue_Type.__name__ = "Unsigned32"
_MscLpAruRxCflThreshValue_Object = MibTableColumn
mscLpAruRxCflThreshValue = _MscLpAruRxCflThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 355, 1, 2),
    _MscLpAruRxCflThreshValue_Type()
)
mscLpAruRxCflThreshValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruRxCflThreshValue.setStatus("obsolete")
_MscLpAruRxFflThreshTable_Object = MibTable
mscLpAruRxFflThreshTable = _MscLpAruRxFflThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 356)
)
if mibBuilder.loadTexts:
    mscLpAruRxFflThreshTable.setStatus("obsolete")
_MscLpAruRxFflThreshEntry_Object = MibTableRow
mscLpAruRxFflThreshEntry = _MscLpAruRxFflThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 356, 1)
)
mscLpAruRxFflThreshEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpAruIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpAruRxFflThreshIndex"),
)
if mibBuilder.loadTexts:
    mscLpAruRxFflThreshEntry.setStatus("obsolete")


class _MscLpAruRxFflThreshIndex_Type(Integer32):
    """Custom type mscLpAruRxFflThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscLpAruRxFflThreshIndex_Type.__name__ = "Integer32"
_MscLpAruRxFflThreshIndex_Object = MibTableColumn
mscLpAruRxFflThreshIndex = _MscLpAruRxFflThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 356, 1, 1),
    _MscLpAruRxFflThreshIndex_Type()
)
mscLpAruRxFflThreshIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpAruRxFflThreshIndex.setStatus("obsolete")


class _MscLpAruRxFflThreshValue_Type(Unsigned32):
    """Custom type mscLpAruRxFflThreshValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_MscLpAruRxFflThreshValue_Type.__name__ = "Unsigned32"
_MscLpAruRxFflThreshValue_Object = MibTableColumn
mscLpAruRxFflThreshValue = _MscLpAruRxFflThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 20, 356, 1, 2),
    _MscLpAruRxFflThreshValue_Type()
)
mscLpAruRxFflThreshValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpAruRxFflThreshValue.setStatus("obsolete")
_MscLpEngArc_ObjectIdentity = ObjectIdentity
mscLpEngArc = _MscLpEngArc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5)
)
_MscLpEngArcRowStatusTable_Object = MibTable
mscLpEngArcRowStatusTable = _MscLpEngArcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 1)
)
if mibBuilder.loadTexts:
    mscLpEngArcRowStatusTable.setStatus("mandatory")
_MscLpEngArcRowStatusEntry_Object = MibTableRow
mscLpEngArcRowStatusEntry = _MscLpEngArcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 1, 1)
)
mscLpEngArcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngArcRowStatusEntry.setStatus("mandatory")
_MscLpEngArcRowStatus_Type = RowStatus
_MscLpEngArcRowStatus_Object = MibTableColumn
mscLpEngArcRowStatus = _MscLpEngArcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 1, 1, 1),
    _MscLpEngArcRowStatus_Type()
)
mscLpEngArcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngArcRowStatus.setStatus("mandatory")
_MscLpEngArcComponentName_Type = DisplayString
_MscLpEngArcComponentName_Object = MibTableColumn
mscLpEngArcComponentName = _MscLpEngArcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 1, 1, 2),
    _MscLpEngArcComponentName_Type()
)
mscLpEngArcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcComponentName.setStatus("mandatory")
_MscLpEngArcStorageType_Type = StorageType
_MscLpEngArcStorageType_Object = MibTableColumn
mscLpEngArcStorageType = _MscLpEngArcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 1, 1, 4),
    _MscLpEngArcStorageType_Type()
)
mscLpEngArcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcStorageType.setStatus("mandatory")
_MscLpEngArcIndex_Type = NonReplicated
_MscLpEngArcIndex_Object = MibTableColumn
mscLpEngArcIndex = _MscLpEngArcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 1, 1, 10),
    _MscLpEngArcIndex_Type()
)
mscLpEngArcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEngArcIndex.setStatus("mandatory")
_MscLpEngArcOv_ObjectIdentity = ObjectIdentity
mscLpEngArcOv = _MscLpEngArcOv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 2)
)
_MscLpEngArcOvRowStatusTable_Object = MibTable
mscLpEngArcOvRowStatusTable = _MscLpEngArcOvRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mscLpEngArcOvRowStatusTable.setStatus("mandatory")
_MscLpEngArcOvRowStatusEntry_Object = MibTableRow
mscLpEngArcOvRowStatusEntry = _MscLpEngArcOvRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 2, 1, 1)
)
mscLpEngArcOvRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcOvIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngArcOvRowStatusEntry.setStatus("mandatory")
_MscLpEngArcOvRowStatus_Type = RowStatus
_MscLpEngArcOvRowStatus_Object = MibTableColumn
mscLpEngArcOvRowStatus = _MscLpEngArcOvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 2, 1, 1, 1),
    _MscLpEngArcOvRowStatus_Type()
)
mscLpEngArcOvRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngArcOvRowStatus.setStatus("mandatory")
_MscLpEngArcOvComponentName_Type = DisplayString
_MscLpEngArcOvComponentName_Object = MibTableColumn
mscLpEngArcOvComponentName = _MscLpEngArcOvComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 2, 1, 1, 2),
    _MscLpEngArcOvComponentName_Type()
)
mscLpEngArcOvComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcOvComponentName.setStatus("mandatory")
_MscLpEngArcOvStorageType_Type = StorageType
_MscLpEngArcOvStorageType_Object = MibTableColumn
mscLpEngArcOvStorageType = _MscLpEngArcOvStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 2, 1, 1, 4),
    _MscLpEngArcOvStorageType_Type()
)
mscLpEngArcOvStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcOvStorageType.setStatus("mandatory")
_MscLpEngArcOvIndex_Type = NonReplicated
_MscLpEngArcOvIndex_Object = MibTableColumn
mscLpEngArcOvIndex = _MscLpEngArcOvIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 2, 1, 1, 10),
    _MscLpEngArcOvIndex_Type()
)
mscLpEngArcOvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEngArcOvIndex.setStatus("mandatory")
_MscLpEngArcOvProvTable_Object = MibTable
mscLpEngArcOvProvTable = _MscLpEngArcOvProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 2, 10)
)
if mibBuilder.loadTexts:
    mscLpEngArcOvProvTable.setStatus("mandatory")
_MscLpEngArcOvProvEntry_Object = MibTableRow
mscLpEngArcOvProvEntry = _MscLpEngArcOvProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 2, 10, 1)
)
mscLpEngArcOvProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcOvIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngArcOvProvEntry.setStatus("mandatory")


class _MscLpEngArcOvTotalConnectionPoolCapacity_Type(Unsigned32):
    """Custom type mscLpEngArcOvTotalConnectionPoolCapacity based on Unsigned32"""
    defaultValue = 3072

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_MscLpEngArcOvTotalConnectionPoolCapacity_Type.__name__ = "Unsigned32"
_MscLpEngArcOvTotalConnectionPoolCapacity_Object = MibTableColumn
mscLpEngArcOvTotalConnectionPoolCapacity = _MscLpEngArcOvTotalConnectionPoolCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 2, 10, 1, 1),
    _MscLpEngArcOvTotalConnectionPoolCapacity_Type()
)
mscLpEngArcOvTotalConnectionPoolCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngArcOvTotalConnectionPoolCapacity.setStatus("mandatory")


class _MscLpEngArcOvMulticastBranchesCapacity_Type(Unsigned32):
    """Custom type mscLpEngArcOvMulticastBranchesCapacity based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_MscLpEngArcOvMulticastBranchesCapacity_Type.__name__ = "Unsigned32"
_MscLpEngArcOvMulticastBranchesCapacity_Object = MibTableColumn
mscLpEngArcOvMulticastBranchesCapacity = _MscLpEngArcOvMulticastBranchesCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 2, 10, 1, 2),
    _MscLpEngArcOvMulticastBranchesCapacity_Type()
)
mscLpEngArcOvMulticastBranchesCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngArcOvMulticastBranchesCapacity.setStatus("mandatory")


class _MscLpEngArcOvTxCellMemoryAllocation_Type(Unsigned32):
    """Custom type mscLpEngArcOvTxCellMemoryAllocation based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_MscLpEngArcOvTxCellMemoryAllocation_Type.__name__ = "Unsigned32"
_MscLpEngArcOvTxCellMemoryAllocation_Object = MibTableColumn
mscLpEngArcOvTxCellMemoryAllocation = _MscLpEngArcOvTxCellMemoryAllocation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 2, 10, 1, 3),
    _MscLpEngArcOvTxCellMemoryAllocation_Type()
)
mscLpEngArcOvTxCellMemoryAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngArcOvTxCellMemoryAllocation.setStatus("mandatory")


class _MscLpEngArcOvRxCellMemoryAllocation_Type(Unsigned32):
    """Custom type mscLpEngArcOvRxCellMemoryAllocation based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_MscLpEngArcOvRxCellMemoryAllocation_Type.__name__ = "Unsigned32"
_MscLpEngArcOvRxCellMemoryAllocation_Object = MibTableColumn
mscLpEngArcOvRxCellMemoryAllocation = _MscLpEngArcOvRxCellMemoryAllocation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 2, 10, 1, 4),
    _MscLpEngArcOvRxCellMemoryAllocation_Type()
)
mscLpEngArcOvRxCellMemoryAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngArcOvRxCellMemoryAllocation.setStatus("mandatory")
_MscLpEngArcCqc_ObjectIdentity = ObjectIdentity
mscLpEngArcCqc = _MscLpEngArcCqc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3)
)
_MscLpEngArcCqcRowStatusTable_Object = MibTable
mscLpEngArcCqcRowStatusTable = _MscLpEngArcCqcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3, 1)
)
if mibBuilder.loadTexts:
    mscLpEngArcCqcRowStatusTable.setStatus("mandatory")
_MscLpEngArcCqcRowStatusEntry_Object = MibTableRow
mscLpEngArcCqcRowStatusEntry = _MscLpEngArcCqcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3, 1, 1)
)
mscLpEngArcCqcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcCqcIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngArcCqcRowStatusEntry.setStatus("mandatory")
_MscLpEngArcCqcRowStatus_Type = RowStatus
_MscLpEngArcCqcRowStatus_Object = MibTableColumn
mscLpEngArcCqcRowStatus = _MscLpEngArcCqcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3, 1, 1, 1),
    _MscLpEngArcCqcRowStatus_Type()
)
mscLpEngArcCqcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngArcCqcRowStatus.setStatus("mandatory")
_MscLpEngArcCqcComponentName_Type = DisplayString
_MscLpEngArcCqcComponentName_Object = MibTableColumn
mscLpEngArcCqcComponentName = _MscLpEngArcCqcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3, 1, 1, 2),
    _MscLpEngArcCqcComponentName_Type()
)
mscLpEngArcCqcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcCqcComponentName.setStatus("mandatory")
_MscLpEngArcCqcStorageType_Type = StorageType
_MscLpEngArcCqcStorageType_Object = MibTableColumn
mscLpEngArcCqcStorageType = _MscLpEngArcCqcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3, 1, 1, 4),
    _MscLpEngArcCqcStorageType_Type()
)
mscLpEngArcCqcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcCqcStorageType.setStatus("mandatory")
_MscLpEngArcCqcIndex_Type = NonReplicated
_MscLpEngArcCqcIndex_Object = MibTableColumn
mscLpEngArcCqcIndex = _MscLpEngArcCqcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3, 1, 1, 10),
    _MscLpEngArcCqcIndex_Type()
)
mscLpEngArcCqcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEngArcCqcIndex.setStatus("mandatory")
_MscLpEngArcCqcOv_ObjectIdentity = ObjectIdentity
mscLpEngArcCqcOv = _MscLpEngArcCqcOv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3, 2)
)
_MscLpEngArcCqcOvRowStatusTable_Object = MibTable
mscLpEngArcCqcOvRowStatusTable = _MscLpEngArcCqcOvRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscLpEngArcCqcOvRowStatusTable.setStatus("mandatory")
_MscLpEngArcCqcOvRowStatusEntry_Object = MibTableRow
mscLpEngArcCqcOvRowStatusEntry = _MscLpEngArcCqcOvRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3, 2, 1, 1)
)
mscLpEngArcCqcOvRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcCqcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcCqcOvIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngArcCqcOvRowStatusEntry.setStatus("mandatory")
_MscLpEngArcCqcOvRowStatus_Type = RowStatus
_MscLpEngArcCqcOvRowStatus_Object = MibTableColumn
mscLpEngArcCqcOvRowStatus = _MscLpEngArcCqcOvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3, 2, 1, 1, 1),
    _MscLpEngArcCqcOvRowStatus_Type()
)
mscLpEngArcCqcOvRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcCqcOvRowStatus.setStatus("mandatory")
_MscLpEngArcCqcOvComponentName_Type = DisplayString
_MscLpEngArcCqcOvComponentName_Object = MibTableColumn
mscLpEngArcCqcOvComponentName = _MscLpEngArcCqcOvComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3, 2, 1, 1, 2),
    _MscLpEngArcCqcOvComponentName_Type()
)
mscLpEngArcCqcOvComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcCqcOvComponentName.setStatus("mandatory")
_MscLpEngArcCqcOvStorageType_Type = StorageType
_MscLpEngArcCqcOvStorageType_Object = MibTableColumn
mscLpEngArcCqcOvStorageType = _MscLpEngArcCqcOvStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3, 2, 1, 1, 4),
    _MscLpEngArcCqcOvStorageType_Type()
)
mscLpEngArcCqcOvStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcCqcOvStorageType.setStatus("mandatory")
_MscLpEngArcCqcOvIndex_Type = NonReplicated
_MscLpEngArcCqcOvIndex_Object = MibTableColumn
mscLpEngArcCqcOvIndex = _MscLpEngArcCqcOvIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3, 2, 1, 1, 10),
    _MscLpEngArcCqcOvIndex_Type()
)
mscLpEngArcCqcOvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEngArcCqcOvIndex.setStatus("mandatory")
_MscLpEngArcCqcOvProvTable_Object = MibTable
mscLpEngArcCqcOvProvTable = _MscLpEngArcCqcOvProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscLpEngArcCqcOvProvTable.setStatus("mandatory")
_MscLpEngArcCqcOvProvEntry_Object = MibTableRow
mscLpEngArcCqcOvProvEntry = _MscLpEngArcCqcOvProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3, 2, 10, 1)
)
mscLpEngArcCqcOvProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcCqcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcCqcOvIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngArcCqcOvProvEntry.setStatus("mandatory")


class _MscLpEngArcCqcOvPerVcQueueInterfaces_Type(Unsigned32):
    """Custom type mscLpEngArcCqcOvPerVcQueueInterfaces based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscLpEngArcCqcOvPerVcQueueInterfaces_Type.__name__ = "Unsigned32"
_MscLpEngArcCqcOvPerVcQueueInterfaces_Object = MibTableColumn
mscLpEngArcCqcOvPerVcQueueInterfaces = _MscLpEngArcCqcOvPerVcQueueInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3, 2, 10, 1, 1),
    _MscLpEngArcCqcOvPerVcQueueInterfaces_Type()
)
mscLpEngArcCqcOvPerVcQueueInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngArcCqcOvPerVcQueueInterfaces.setStatus("mandatory")


class _MscLpEngArcCqcOvShapingScalingFactor_Type(FixedPoint1):
    """Custom type mscLpEngArcCqcOvShapingScalingFactor based on FixedPoint1"""
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


_MscLpEngArcCqcOvShapingScalingFactor_Type.__name__ = "FixedPoint1"
_MscLpEngArcCqcOvShapingScalingFactor_Object = MibTableColumn
mscLpEngArcCqcOvShapingScalingFactor = _MscLpEngArcCqcOvShapingScalingFactor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3, 2, 10, 1, 2),
    _MscLpEngArcCqcOvShapingScalingFactor_Type()
)
mscLpEngArcCqcOvShapingScalingFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngArcCqcOvShapingScalingFactor.setStatus("mandatory")


class _MscLpEngArcCqcOvCdvReduction_Type(Integer32):
    """Custom type mscLpEngArcCqcOvCdvReduction based on Integer32"""
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


_MscLpEngArcCqcOvCdvReduction_Type.__name__ = "Integer32"
_MscLpEngArcCqcOvCdvReduction_Object = MibTableColumn
mscLpEngArcCqcOvCdvReduction = _MscLpEngArcCqcOvCdvReduction_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3, 2, 10, 1, 3),
    _MscLpEngArcCqcOvCdvReduction_Type()
)
mscLpEngArcCqcOvCdvReduction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngArcCqcOvCdvReduction.setStatus("mandatory")


class _MscLpEngArcCqcOvPortCongestionPolicy_Type(Integer32):
    """Custom type mscLpEngArcCqcOvPortCongestionPolicy based on Integer32"""
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


_MscLpEngArcCqcOvPortCongestionPolicy_Type.__name__ = "Integer32"
_MscLpEngArcCqcOvPortCongestionPolicy_Object = MibTableColumn
mscLpEngArcCqcOvPortCongestionPolicy = _MscLpEngArcCqcOvPortCongestionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3, 2, 10, 1, 4),
    _MscLpEngArcCqcOvPortCongestionPolicy_Type()
)
mscLpEngArcCqcOvPortCongestionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngArcCqcOvPortCongestionPolicy.setStatus("mandatory")
_MscLpEngArcCqcOvConnCapTable_Object = MibTable
mscLpEngArcCqcOvConnCapTable = _MscLpEngArcCqcOvConnCapTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3, 2, 450)
)
if mibBuilder.loadTexts:
    mscLpEngArcCqcOvConnCapTable.setStatus("mandatory")
_MscLpEngArcCqcOvConnCapEntry_Object = MibTableRow
mscLpEngArcCqcOvConnCapEntry = _MscLpEngArcCqcOvConnCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3, 2, 450, 1)
)
mscLpEngArcCqcOvConnCapEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcCqcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcCqcOvIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcCqcOvConnCapIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngArcCqcOvConnCapEntry.setStatus("mandatory")


class _MscLpEngArcCqcOvConnCapIndex_Type(Integer32):
    """Custom type mscLpEngArcCqcOvConnCapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscLpEngArcCqcOvConnCapIndex_Type.__name__ = "Integer32"
_MscLpEngArcCqcOvConnCapIndex_Object = MibTableColumn
mscLpEngArcCqcOvConnCapIndex = _MscLpEngArcCqcOvConnCapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3, 2, 450, 1, 1),
    _MscLpEngArcCqcOvConnCapIndex_Type()
)
mscLpEngArcCqcOvConnCapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEngArcCqcOvConnCapIndex.setStatus("mandatory")


class _MscLpEngArcCqcOvConnCapValue_Type(Unsigned32):
    """Custom type mscLpEngArcCqcOvConnCapValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 4096),
    )


_MscLpEngArcCqcOvConnCapValue_Type.__name__ = "Unsigned32"
_MscLpEngArcCqcOvConnCapValue_Object = MibTableColumn
mscLpEngArcCqcOvConnCapValue = _MscLpEngArcCqcOvConnCapValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3, 2, 450, 1, 2),
    _MscLpEngArcCqcOvConnCapValue_Type()
)
mscLpEngArcCqcOvConnCapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngArcCqcOvConnCapValue.setStatus("mandatory")
_MscLpEngArcCqcOperTable_Object = MibTable
mscLpEngArcCqcOperTable = _MscLpEngArcCqcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3, 10)
)
if mibBuilder.loadTexts:
    mscLpEngArcCqcOperTable.setStatus("mandatory")
_MscLpEngArcCqcOperEntry_Object = MibTableRow
mscLpEngArcCqcOperEntry = _MscLpEngArcCqcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3, 10, 1)
)
mscLpEngArcCqcOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcCqcIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngArcCqcOperEntry.setStatus("mandatory")


class _MscLpEngArcCqcCdvReduction_Type(Integer32):
    """Custom type mscLpEngArcCqcCdvReduction based on Integer32"""
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


_MscLpEngArcCqcCdvReduction_Type.__name__ = "Integer32"
_MscLpEngArcCqcCdvReduction_Object = MibTableColumn
mscLpEngArcCqcCdvReduction = _MscLpEngArcCqcCdvReduction_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 3, 10, 1, 1),
    _MscLpEngArcCqcCdvReduction_Type()
)
mscLpEngArcCqcCdvReduction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcCqcCdvReduction.setStatus("mandatory")
_MscLpEngArcAqm_ObjectIdentity = ObjectIdentity
mscLpEngArcAqm = _MscLpEngArcAqm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4)
)
_MscLpEngArcAqmRowStatusTable_Object = MibTable
mscLpEngArcAqmRowStatusTable = _MscLpEngArcAqmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 1)
)
if mibBuilder.loadTexts:
    mscLpEngArcAqmRowStatusTable.setStatus("mandatory")
_MscLpEngArcAqmRowStatusEntry_Object = MibTableRow
mscLpEngArcAqmRowStatusEntry = _MscLpEngArcAqmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 1, 1)
)
mscLpEngArcAqmRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcAqmIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngArcAqmRowStatusEntry.setStatus("mandatory")
_MscLpEngArcAqmRowStatus_Type = RowStatus
_MscLpEngArcAqmRowStatus_Object = MibTableColumn
mscLpEngArcAqmRowStatus = _MscLpEngArcAqmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 1, 1, 1),
    _MscLpEngArcAqmRowStatus_Type()
)
mscLpEngArcAqmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngArcAqmRowStatus.setStatus("mandatory")
_MscLpEngArcAqmComponentName_Type = DisplayString
_MscLpEngArcAqmComponentName_Object = MibTableColumn
mscLpEngArcAqmComponentName = _MscLpEngArcAqmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 1, 1, 2),
    _MscLpEngArcAqmComponentName_Type()
)
mscLpEngArcAqmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcAqmComponentName.setStatus("mandatory")
_MscLpEngArcAqmStorageType_Type = StorageType
_MscLpEngArcAqmStorageType_Object = MibTableColumn
mscLpEngArcAqmStorageType = _MscLpEngArcAqmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 1, 1, 4),
    _MscLpEngArcAqmStorageType_Type()
)
mscLpEngArcAqmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcAqmStorageType.setStatus("mandatory")


class _MscLpEngArcAqmIndex_Type(Integer32):
    """Custom type mscLpEngArcAqmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscLpEngArcAqmIndex_Type.__name__ = "Integer32"
_MscLpEngArcAqmIndex_Object = MibTableColumn
mscLpEngArcAqmIndex = _MscLpEngArcAqmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 1, 1, 10),
    _MscLpEngArcAqmIndex_Type()
)
mscLpEngArcAqmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEngArcAqmIndex.setStatus("mandatory")
_MscLpEngArcAqmOv_ObjectIdentity = ObjectIdentity
mscLpEngArcAqmOv = _MscLpEngArcAqmOv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 2)
)
_MscLpEngArcAqmOvRowStatusTable_Object = MibTable
mscLpEngArcAqmOvRowStatusTable = _MscLpEngArcAqmOvRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscLpEngArcAqmOvRowStatusTable.setStatus("mandatory")
_MscLpEngArcAqmOvRowStatusEntry_Object = MibTableRow
mscLpEngArcAqmOvRowStatusEntry = _MscLpEngArcAqmOvRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 2, 1, 1)
)
mscLpEngArcAqmOvRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcAqmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcAqmOvIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngArcAqmOvRowStatusEntry.setStatus("mandatory")
_MscLpEngArcAqmOvRowStatus_Type = RowStatus
_MscLpEngArcAqmOvRowStatus_Object = MibTableColumn
mscLpEngArcAqmOvRowStatus = _MscLpEngArcAqmOvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 2, 1, 1, 1),
    _MscLpEngArcAqmOvRowStatus_Type()
)
mscLpEngArcAqmOvRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcAqmOvRowStatus.setStatus("mandatory")
_MscLpEngArcAqmOvComponentName_Type = DisplayString
_MscLpEngArcAqmOvComponentName_Object = MibTableColumn
mscLpEngArcAqmOvComponentName = _MscLpEngArcAqmOvComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 2, 1, 1, 2),
    _MscLpEngArcAqmOvComponentName_Type()
)
mscLpEngArcAqmOvComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcAqmOvComponentName.setStatus("mandatory")
_MscLpEngArcAqmOvStorageType_Type = StorageType
_MscLpEngArcAqmOvStorageType_Object = MibTableColumn
mscLpEngArcAqmOvStorageType = _MscLpEngArcAqmOvStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 2, 1, 1, 4),
    _MscLpEngArcAqmOvStorageType_Type()
)
mscLpEngArcAqmOvStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcAqmOvStorageType.setStatus("mandatory")
_MscLpEngArcAqmOvIndex_Type = NonReplicated
_MscLpEngArcAqmOvIndex_Object = MibTableColumn
mscLpEngArcAqmOvIndex = _MscLpEngArcAqmOvIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 2, 1, 1, 10),
    _MscLpEngArcAqmOvIndex_Type()
)
mscLpEngArcAqmOvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEngArcAqmOvIndex.setStatus("mandatory")
_MscLpEngArcAqmOvProvTable_Object = MibTable
mscLpEngArcAqmOvProvTable = _MscLpEngArcAqmOvProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 2, 10)
)
if mibBuilder.loadTexts:
    mscLpEngArcAqmOvProvTable.setStatus("mandatory")
_MscLpEngArcAqmOvProvEntry_Object = MibTableRow
mscLpEngArcAqmOvProvEntry = _MscLpEngArcAqmOvProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 2, 10, 1)
)
mscLpEngArcAqmOvProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcAqmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcAqmOvIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngArcAqmOvProvEntry.setStatus("mandatory")


class _MscLpEngArcAqmOvConnectionPoolCapacity_Type(Unsigned32):
    """Custom type mscLpEngArcAqmOvConnectionPoolCapacity based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16000),
    )


_MscLpEngArcAqmOvConnectionPoolCapacity_Type.__name__ = "Unsigned32"
_MscLpEngArcAqmOvConnectionPoolCapacity_Object = MibTableColumn
mscLpEngArcAqmOvConnectionPoolCapacity = _MscLpEngArcAqmOvConnectionPoolCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 2, 10, 1, 1),
    _MscLpEngArcAqmOvConnectionPoolCapacity_Type()
)
mscLpEngArcAqmOvConnectionPoolCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngArcAqmOvConnectionPoolCapacity.setStatus("mandatory")


class _MscLpEngArcAqmOvHighPriorityEpdOffset_Type(Unsigned32):
    """Custom type mscLpEngArcAqmOvHighPriorityEpdOffset based on Unsigned32"""
    defaultValue = 28

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1024),
    )


_MscLpEngArcAqmOvHighPriorityEpdOffset_Type.__name__ = "Unsigned32"
_MscLpEngArcAqmOvHighPriorityEpdOffset_Object = MibTableColumn
mscLpEngArcAqmOvHighPriorityEpdOffset = _MscLpEngArcAqmOvHighPriorityEpdOffset_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 2, 10, 1, 2),
    _MscLpEngArcAqmOvHighPriorityEpdOffset_Type()
)
mscLpEngArcAqmOvHighPriorityEpdOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngArcAqmOvHighPriorityEpdOffset.setStatus("mandatory")


class _MscLpEngArcAqmOvLowPriorityEpdOffset_Type(Unsigned32):
    """Custom type mscLpEngArcAqmOvLowPriorityEpdOffset based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1024),
    )


_MscLpEngArcAqmOvLowPriorityEpdOffset_Type.__name__ = "Unsigned32"
_MscLpEngArcAqmOvLowPriorityEpdOffset_Object = MibTableColumn
mscLpEngArcAqmOvLowPriorityEpdOffset = _MscLpEngArcAqmOvLowPriorityEpdOffset_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 2, 10, 1, 3),
    _MscLpEngArcAqmOvLowPriorityEpdOffset_Type()
)
mscLpEngArcAqmOvLowPriorityEpdOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngArcAqmOvLowPriorityEpdOffset.setStatus("mandatory")


class _MscLpEngArcAqmOvPortCongestionPolicy_Type(Integer32):
    """Custom type mscLpEngArcAqmOvPortCongestionPolicy based on Integer32"""
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


_MscLpEngArcAqmOvPortCongestionPolicy_Type.__name__ = "Integer32"
_MscLpEngArcAqmOvPortCongestionPolicy_Object = MibTableColumn
mscLpEngArcAqmOvPortCongestionPolicy = _MscLpEngArcAqmOvPortCongestionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 2, 10, 1, 4),
    _MscLpEngArcAqmOvPortCongestionPolicy_Type()
)
mscLpEngArcAqmOvPortCongestionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngArcAqmOvPortCongestionPolicy.setStatus("mandatory")
_MscLpEngArcAqmOperTable_Object = MibTable
mscLpEngArcAqmOperTable = _MscLpEngArcAqmOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 10)
)
if mibBuilder.loadTexts:
    mscLpEngArcAqmOperTable.setStatus("mandatory")
_MscLpEngArcAqmOperEntry_Object = MibTableRow
mscLpEngArcAqmOperEntry = _MscLpEngArcAqmOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 10, 1)
)
mscLpEngArcAqmOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcAqmIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngArcAqmOperEntry.setStatus("mandatory")


class _MscLpEngArcAqmConnectionPoolAvailable_Type(Unsigned32):
    """Custom type mscLpEngArcAqmConnectionPoolAvailable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000),
    )


_MscLpEngArcAqmConnectionPoolAvailable_Type.__name__ = "Unsigned32"
_MscLpEngArcAqmConnectionPoolAvailable_Object = MibTableColumn
mscLpEngArcAqmConnectionPoolAvailable = _MscLpEngArcAqmConnectionPoolAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 10, 1, 1),
    _MscLpEngArcAqmConnectionPoolAvailable_Type()
)
mscLpEngArcAqmConnectionPoolAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcAqmConnectionPoolAvailable.setStatus("mandatory")


class _MscLpEngArcAqmConnectionPoolUsage_Type(Unsigned32):
    """Custom type mscLpEngArcAqmConnectionPoolUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000),
    )


_MscLpEngArcAqmConnectionPoolUsage_Type.__name__ = "Unsigned32"
_MscLpEngArcAqmConnectionPoolUsage_Object = MibTableColumn
mscLpEngArcAqmConnectionPoolUsage = _MscLpEngArcAqmConnectionPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 10, 1, 2),
    _MscLpEngArcAqmConnectionPoolUsage_Type()
)
mscLpEngArcAqmConnectionPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcAqmConnectionPoolUsage.setStatus("mandatory")


class _MscLpEngArcAqmTxCellMemoryAvailable_Type(Gauge32):
    """Custom type mscLpEngArcAqmTxCellMemoryAvailable based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 163839),
    )


_MscLpEngArcAqmTxCellMemoryAvailable_Type.__name__ = "Gauge32"
_MscLpEngArcAqmTxCellMemoryAvailable_Object = MibTableColumn
mscLpEngArcAqmTxCellMemoryAvailable = _MscLpEngArcAqmTxCellMemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 10, 1, 5),
    _MscLpEngArcAqmTxCellMemoryAvailable_Type()
)
mscLpEngArcAqmTxCellMemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcAqmTxCellMemoryAvailable.setStatus("mandatory")


class _MscLpEngArcAqmTxCellMemoryMinAvailable_Type(Gauge32):
    """Custom type mscLpEngArcAqmTxCellMemoryMinAvailable based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 163839),
    )


_MscLpEngArcAqmTxCellMemoryMinAvailable_Type.__name__ = "Gauge32"
_MscLpEngArcAqmTxCellMemoryMinAvailable_Object = MibTableColumn
mscLpEngArcAqmTxCellMemoryMinAvailable = _MscLpEngArcAqmTxCellMemoryMinAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 10, 1, 6),
    _MscLpEngArcAqmTxCellMemoryMinAvailable_Type()
)
mscLpEngArcAqmTxCellMemoryMinAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcAqmTxCellMemoryMinAvailable.setStatus("mandatory")


class _MscLpEngArcAqmTxCellMemoryCongestionState_Type(Gauge32):
    """Custom type mscLpEngArcAqmTxCellMemoryCongestionState based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscLpEngArcAqmTxCellMemoryCongestionState_Type.__name__ = "Gauge32"
_MscLpEngArcAqmTxCellMemoryCongestionState_Object = MibTableColumn
mscLpEngArcAqmTxCellMemoryCongestionState = _MscLpEngArcAqmTxCellMemoryCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 10, 1, 7),
    _MscLpEngArcAqmTxCellMemoryCongestionState_Type()
)
mscLpEngArcAqmTxCellMemoryCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcAqmTxCellMemoryCongestionState.setStatus("mandatory")
_MscLpEngArcAqmTxCellThreshTable_Object = MibTable
mscLpEngArcAqmTxCellThreshTable = _MscLpEngArcAqmTxCellThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 448)
)
if mibBuilder.loadTexts:
    mscLpEngArcAqmTxCellThreshTable.setStatus("mandatory")
_MscLpEngArcAqmTxCellThreshEntry_Object = MibTableRow
mscLpEngArcAqmTxCellThreshEntry = _MscLpEngArcAqmTxCellThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 448, 1)
)
mscLpEngArcAqmTxCellThreshEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcAqmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcAqmTxCellThreshIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngArcAqmTxCellThreshEntry.setStatus("mandatory")


class _MscLpEngArcAqmTxCellThreshIndex_Type(Integer32):
    """Custom type mscLpEngArcAqmTxCellThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscLpEngArcAqmTxCellThreshIndex_Type.__name__ = "Integer32"
_MscLpEngArcAqmTxCellThreshIndex_Object = MibTableColumn
mscLpEngArcAqmTxCellThreshIndex = _MscLpEngArcAqmTxCellThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 448, 1, 1),
    _MscLpEngArcAqmTxCellThreshIndex_Type()
)
mscLpEngArcAqmTxCellThreshIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEngArcAqmTxCellThreshIndex.setStatus("mandatory")


class _MscLpEngArcAqmTxCellThreshValue_Type(Unsigned32):
    """Custom type mscLpEngArcAqmTxCellThreshValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 163839),
    )


_MscLpEngArcAqmTxCellThreshValue_Type.__name__ = "Unsigned32"
_MscLpEngArcAqmTxCellThreshValue_Object = MibTableColumn
mscLpEngArcAqmTxCellThreshValue = _MscLpEngArcAqmTxCellThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 4, 448, 1, 2),
    _MscLpEngArcAqmTxCellThreshValue_Type()
)
mscLpEngArcAqmTxCellThreshValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcAqmTxCellThreshValue.setStatus("mandatory")
_MscLpEngArcOperTable_Object = MibTable
mscLpEngArcOperTable = _MscLpEngArcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 10)
)
if mibBuilder.loadTexts:
    mscLpEngArcOperTable.setStatus("mandatory")
_MscLpEngArcOperEntry_Object = MibTableRow
mscLpEngArcOperEntry = _MscLpEngArcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 10, 1)
)
mscLpEngArcOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngArcOperEntry.setStatus("mandatory")


class _MscLpEngArcTotalConnectionPoolAvailable_Type(Unsigned32):
    """Custom type mscLpEngArcTotalConnectionPoolAvailable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_MscLpEngArcTotalConnectionPoolAvailable_Type.__name__ = "Unsigned32"
_MscLpEngArcTotalConnectionPoolAvailable_Object = MibTableColumn
mscLpEngArcTotalConnectionPoolAvailable = _MscLpEngArcTotalConnectionPoolAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 10, 1, 1),
    _MscLpEngArcTotalConnectionPoolAvailable_Type()
)
mscLpEngArcTotalConnectionPoolAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcTotalConnectionPoolAvailable.setStatus("mandatory")


class _MscLpEngArcTotalConnectionPoolUsage_Type(Unsigned32):
    """Custom type mscLpEngArcTotalConnectionPoolUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_MscLpEngArcTotalConnectionPoolUsage_Type.__name__ = "Unsigned32"
_MscLpEngArcTotalConnectionPoolUsage_Object = MibTableColumn
mscLpEngArcTotalConnectionPoolUsage = _MscLpEngArcTotalConnectionPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 10, 1, 2),
    _MscLpEngArcTotalConnectionPoolUsage_Type()
)
mscLpEngArcTotalConnectionPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcTotalConnectionPoolUsage.setStatus("mandatory")


class _MscLpEngArcMulticastBranchesAvailable_Type(Unsigned32):
    """Custom type mscLpEngArcMulticastBranchesAvailable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_MscLpEngArcMulticastBranchesAvailable_Type.__name__ = "Unsigned32"
_MscLpEngArcMulticastBranchesAvailable_Object = MibTableColumn
mscLpEngArcMulticastBranchesAvailable = _MscLpEngArcMulticastBranchesAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 10, 1, 3),
    _MscLpEngArcMulticastBranchesAvailable_Type()
)
mscLpEngArcMulticastBranchesAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcMulticastBranchesAvailable.setStatus("mandatory")


class _MscLpEngArcMulticastBranchesUsage_Type(Unsigned32):
    """Custom type mscLpEngArcMulticastBranchesUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_MscLpEngArcMulticastBranchesUsage_Type.__name__ = "Unsigned32"
_MscLpEngArcMulticastBranchesUsage_Object = MibTableColumn
mscLpEngArcMulticastBranchesUsage = _MscLpEngArcMulticastBranchesUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 10, 1, 4),
    _MscLpEngArcMulticastBranchesUsage_Type()
)
mscLpEngArcMulticastBranchesUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcMulticastBranchesUsage.setStatus("mandatory")


class _MscLpEngArcTxCellMemoryAllocation_Type(Unsigned32):
    """Custom type mscLpEngArcTxCellMemoryAllocation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_MscLpEngArcTxCellMemoryAllocation_Type.__name__ = "Unsigned32"
_MscLpEngArcTxCellMemoryAllocation_Object = MibTableColumn
mscLpEngArcTxCellMemoryAllocation = _MscLpEngArcTxCellMemoryAllocation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 10, 1, 5),
    _MscLpEngArcTxCellMemoryAllocation_Type()
)
mscLpEngArcTxCellMemoryAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcTxCellMemoryAllocation.setStatus("mandatory")


class _MscLpEngArcTxCellMemoryAvailable_Type(Gauge32):
    """Custom type mscLpEngArcTxCellMemoryAvailable based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 163839),
    )


_MscLpEngArcTxCellMemoryAvailable_Type.__name__ = "Gauge32"
_MscLpEngArcTxCellMemoryAvailable_Object = MibTableColumn
mscLpEngArcTxCellMemoryAvailable = _MscLpEngArcTxCellMemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 10, 1, 6),
    _MscLpEngArcTxCellMemoryAvailable_Type()
)
mscLpEngArcTxCellMemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcTxCellMemoryAvailable.setStatus("mandatory")


class _MscLpEngArcTxCellMemoryMinAvailable_Type(Gauge32):
    """Custom type mscLpEngArcTxCellMemoryMinAvailable based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 163839),
    )


_MscLpEngArcTxCellMemoryMinAvailable_Type.__name__ = "Gauge32"
_MscLpEngArcTxCellMemoryMinAvailable_Object = MibTableColumn
mscLpEngArcTxCellMemoryMinAvailable = _MscLpEngArcTxCellMemoryMinAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 10, 1, 7),
    _MscLpEngArcTxCellMemoryMinAvailable_Type()
)
mscLpEngArcTxCellMemoryMinAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcTxCellMemoryMinAvailable.setStatus("mandatory")


class _MscLpEngArcTxCellMemoryCongestionState_Type(Gauge32):
    """Custom type mscLpEngArcTxCellMemoryCongestionState based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscLpEngArcTxCellMemoryCongestionState_Type.__name__ = "Gauge32"
_MscLpEngArcTxCellMemoryCongestionState_Object = MibTableColumn
mscLpEngArcTxCellMemoryCongestionState = _MscLpEngArcTxCellMemoryCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 10, 1, 8),
    _MscLpEngArcTxCellMemoryCongestionState_Type()
)
mscLpEngArcTxCellMemoryCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcTxCellMemoryCongestionState.setStatus("mandatory")


class _MscLpEngArcRxCellMemoryAllocation_Type(Unsigned32):
    """Custom type mscLpEngArcRxCellMemoryAllocation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_MscLpEngArcRxCellMemoryAllocation_Type.__name__ = "Unsigned32"
_MscLpEngArcRxCellMemoryAllocation_Object = MibTableColumn
mscLpEngArcRxCellMemoryAllocation = _MscLpEngArcRxCellMemoryAllocation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 10, 1, 9),
    _MscLpEngArcRxCellMemoryAllocation_Type()
)
mscLpEngArcRxCellMemoryAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcRxCellMemoryAllocation.setStatus("mandatory")


class _MscLpEngArcRxCellMemoryAvailable_Type(Gauge32):
    """Custom type mscLpEngArcRxCellMemoryAvailable based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 163839),
    )


_MscLpEngArcRxCellMemoryAvailable_Type.__name__ = "Gauge32"
_MscLpEngArcRxCellMemoryAvailable_Object = MibTableColumn
mscLpEngArcRxCellMemoryAvailable = _MscLpEngArcRxCellMemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 10, 1, 10),
    _MscLpEngArcRxCellMemoryAvailable_Type()
)
mscLpEngArcRxCellMemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcRxCellMemoryAvailable.setStatus("mandatory")


class _MscLpEngArcRxCellMemoryMinAvailable_Type(Gauge32):
    """Custom type mscLpEngArcRxCellMemoryMinAvailable based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 163839),
    )


_MscLpEngArcRxCellMemoryMinAvailable_Type.__name__ = "Gauge32"
_MscLpEngArcRxCellMemoryMinAvailable_Object = MibTableColumn
mscLpEngArcRxCellMemoryMinAvailable = _MscLpEngArcRxCellMemoryMinAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 10, 1, 11),
    _MscLpEngArcRxCellMemoryMinAvailable_Type()
)
mscLpEngArcRxCellMemoryMinAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcRxCellMemoryMinAvailable.setStatus("mandatory")


class _MscLpEngArcRxCellMemoryCongestionState_Type(Gauge32):
    """Custom type mscLpEngArcRxCellMemoryCongestionState based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscLpEngArcRxCellMemoryCongestionState_Type.__name__ = "Gauge32"
_MscLpEngArcRxCellMemoryCongestionState_Object = MibTableColumn
mscLpEngArcRxCellMemoryCongestionState = _MscLpEngArcRxCellMemoryCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 10, 1, 12),
    _MscLpEngArcRxCellMemoryCongestionState_Type()
)
mscLpEngArcRxCellMemoryCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcRxCellMemoryCongestionState.setStatus("mandatory")
_MscLpEngArcTxCellThreshTable_Object = MibTable
mscLpEngArcTxCellThreshTable = _MscLpEngArcTxCellThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 440)
)
if mibBuilder.loadTexts:
    mscLpEngArcTxCellThreshTable.setStatus("mandatory")
_MscLpEngArcTxCellThreshEntry_Object = MibTableRow
mscLpEngArcTxCellThreshEntry = _MscLpEngArcTxCellThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 440, 1)
)
mscLpEngArcTxCellThreshEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcTxCellThreshIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngArcTxCellThreshEntry.setStatus("mandatory")


class _MscLpEngArcTxCellThreshIndex_Type(Integer32):
    """Custom type mscLpEngArcTxCellThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscLpEngArcTxCellThreshIndex_Type.__name__ = "Integer32"
_MscLpEngArcTxCellThreshIndex_Object = MibTableColumn
mscLpEngArcTxCellThreshIndex = _MscLpEngArcTxCellThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 440, 1, 1),
    _MscLpEngArcTxCellThreshIndex_Type()
)
mscLpEngArcTxCellThreshIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEngArcTxCellThreshIndex.setStatus("mandatory")


class _MscLpEngArcTxCellThreshValue_Type(Unsigned32):
    """Custom type mscLpEngArcTxCellThreshValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 163839),
    )


_MscLpEngArcTxCellThreshValue_Type.__name__ = "Unsigned32"
_MscLpEngArcTxCellThreshValue_Object = MibTableColumn
mscLpEngArcTxCellThreshValue = _MscLpEngArcTxCellThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 440, 1, 2),
    _MscLpEngArcTxCellThreshValue_Type()
)
mscLpEngArcTxCellThreshValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcTxCellThreshValue.setStatus("mandatory")
_MscLpEngArcRxCellThreshTable_Object = MibTable
mscLpEngArcRxCellThreshTable = _MscLpEngArcRxCellThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 444)
)
if mibBuilder.loadTexts:
    mscLpEngArcRxCellThreshTable.setStatus("mandatory")
_MscLpEngArcRxCellThreshEntry_Object = MibTableRow
mscLpEngArcRxCellThreshEntry = _MscLpEngArcRxCellThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 444, 1)
)
mscLpEngArcRxCellThreshEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngArcRxCellThreshIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngArcRxCellThreshEntry.setStatus("mandatory")


class _MscLpEngArcRxCellThreshIndex_Type(Integer32):
    """Custom type mscLpEngArcRxCellThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscLpEngArcRxCellThreshIndex_Type.__name__ = "Integer32"
_MscLpEngArcRxCellThreshIndex_Object = MibTableColumn
mscLpEngArcRxCellThreshIndex = _MscLpEngArcRxCellThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 444, 1, 1),
    _MscLpEngArcRxCellThreshIndex_Type()
)
mscLpEngArcRxCellThreshIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEngArcRxCellThreshIndex.setStatus("mandatory")


class _MscLpEngArcRxCellThreshValue_Type(Unsigned32):
    """Custom type mscLpEngArcRxCellThreshValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 163839),
    )


_MscLpEngArcRxCellThreshValue_Type.__name__ = "Unsigned32"
_MscLpEngArcRxCellThreshValue_Object = MibTableColumn
mscLpEngArcRxCellThreshValue = _MscLpEngArcRxCellThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 5, 444, 1, 2),
    _MscLpEngArcRxCellThreshValue_Type()
)
mscLpEngArcRxCellThreshValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngArcRxCellThreshValue.setStatus("mandatory")
_MscLpEngFcrc_ObjectIdentity = ObjectIdentity
mscLpEngFcrc = _MscLpEngFcrc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6)
)
_MscLpEngFcrcRowStatusTable_Object = MibTable
mscLpEngFcrcRowStatusTable = _MscLpEngFcrcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 1)
)
if mibBuilder.loadTexts:
    mscLpEngFcrcRowStatusTable.setStatus("mandatory")
_MscLpEngFcrcRowStatusEntry_Object = MibTableRow
mscLpEngFcrcRowStatusEntry = _MscLpEngFcrcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 1, 1)
)
mscLpEngFcrcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngFcrcIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngFcrcRowStatusEntry.setStatus("mandatory")
_MscLpEngFcrcRowStatus_Type = RowStatus
_MscLpEngFcrcRowStatus_Object = MibTableColumn
mscLpEngFcrcRowStatus = _MscLpEngFcrcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 1, 1, 1),
    _MscLpEngFcrcRowStatus_Type()
)
mscLpEngFcrcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngFcrcRowStatus.setStatus("mandatory")
_MscLpEngFcrcComponentName_Type = DisplayString
_MscLpEngFcrcComponentName_Object = MibTableColumn
mscLpEngFcrcComponentName = _MscLpEngFcrcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 1, 1, 2),
    _MscLpEngFcrcComponentName_Type()
)
mscLpEngFcrcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFcrcComponentName.setStatus("mandatory")
_MscLpEngFcrcStorageType_Type = StorageType
_MscLpEngFcrcStorageType_Object = MibTableColumn
mscLpEngFcrcStorageType = _MscLpEngFcrcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 1, 1, 4),
    _MscLpEngFcrcStorageType_Type()
)
mscLpEngFcrcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFcrcStorageType.setStatus("mandatory")
_MscLpEngFcrcIndex_Type = NonReplicated
_MscLpEngFcrcIndex_Object = MibTableColumn
mscLpEngFcrcIndex = _MscLpEngFcrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 1, 1, 10),
    _MscLpEngFcrcIndex_Type()
)
mscLpEngFcrcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEngFcrcIndex.setStatus("mandatory")
_MscLpEngFcrcOv_ObjectIdentity = ObjectIdentity
mscLpEngFcrcOv = _MscLpEngFcrcOv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 2)
)
_MscLpEngFcrcOvRowStatusTable_Object = MibTable
mscLpEngFcrcOvRowStatusTable = _MscLpEngFcrcOvRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 2, 1)
)
if mibBuilder.loadTexts:
    mscLpEngFcrcOvRowStatusTable.setStatus("mandatory")
_MscLpEngFcrcOvRowStatusEntry_Object = MibTableRow
mscLpEngFcrcOvRowStatusEntry = _MscLpEngFcrcOvRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 2, 1, 1)
)
mscLpEngFcrcOvRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngFcrcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngFcrcOvIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngFcrcOvRowStatusEntry.setStatus("mandatory")
_MscLpEngFcrcOvRowStatus_Type = RowStatus
_MscLpEngFcrcOvRowStatus_Object = MibTableColumn
mscLpEngFcrcOvRowStatus = _MscLpEngFcrcOvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 2, 1, 1, 1),
    _MscLpEngFcrcOvRowStatus_Type()
)
mscLpEngFcrcOvRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngFcrcOvRowStatus.setStatus("mandatory")
_MscLpEngFcrcOvComponentName_Type = DisplayString
_MscLpEngFcrcOvComponentName_Object = MibTableColumn
mscLpEngFcrcOvComponentName = _MscLpEngFcrcOvComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 2, 1, 1, 2),
    _MscLpEngFcrcOvComponentName_Type()
)
mscLpEngFcrcOvComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFcrcOvComponentName.setStatus("mandatory")
_MscLpEngFcrcOvStorageType_Type = StorageType
_MscLpEngFcrcOvStorageType_Object = MibTableColumn
mscLpEngFcrcOvStorageType = _MscLpEngFcrcOvStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 2, 1, 1, 4),
    _MscLpEngFcrcOvStorageType_Type()
)
mscLpEngFcrcOvStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFcrcOvStorageType.setStatus("mandatory")
_MscLpEngFcrcOvIndex_Type = NonReplicated
_MscLpEngFcrcOvIndex_Object = MibTableColumn
mscLpEngFcrcOvIndex = _MscLpEngFcrcOvIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 2, 1, 1, 10),
    _MscLpEngFcrcOvIndex_Type()
)
mscLpEngFcrcOvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEngFcrcOvIndex.setStatus("mandatory")
_MscLpEngFcrcOvProvTable_Object = MibTable
mscLpEngFcrcOvProvTable = _MscLpEngFcrcOvProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 2, 10)
)
if mibBuilder.loadTexts:
    mscLpEngFcrcOvProvTable.setStatus("mandatory")
_MscLpEngFcrcOvProvEntry_Object = MibTableRow
mscLpEngFcrcOvProvEntry = _MscLpEngFcrcOvProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 2, 10, 1)
)
mscLpEngFcrcOvProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngFcrcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngFcrcOvIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngFcrcOvProvEntry.setStatus("mandatory")


class _MscLpEngFcrcOvSubConnectionPoolCapacity_Type(Unsigned32):
    """Custom type mscLpEngFcrcOvSubConnectionPoolCapacity based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49152),
        ValueRangeConstraint(65535, 65535),
    )


_MscLpEngFcrcOvSubConnectionPoolCapacity_Type.__name__ = "Unsigned32"
_MscLpEngFcrcOvSubConnectionPoolCapacity_Object = MibTableColumn
mscLpEngFcrcOvSubConnectionPoolCapacity = _MscLpEngFcrcOvSubConnectionPoolCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 2, 10, 1, 1),
    _MscLpEngFcrcOvSubConnectionPoolCapacity_Type()
)
mscLpEngFcrcOvSubConnectionPoolCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngFcrcOvSubConnectionPoolCapacity.setStatus("mandatory")


class _MscLpEngFcrcOvLnnConnectionPoolCapacity_Type(Unsigned32):
    """Custom type mscLpEngFcrcOvLnnConnectionPoolCapacity based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2048),
    )


_MscLpEngFcrcOvLnnConnectionPoolCapacity_Type.__name__ = "Unsigned32"
_MscLpEngFcrcOvLnnConnectionPoolCapacity_Object = MibTableColumn
mscLpEngFcrcOvLnnConnectionPoolCapacity = _MscLpEngFcrcOvLnnConnectionPoolCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 2, 10, 1, 2),
    _MscLpEngFcrcOvLnnConnectionPoolCapacity_Type()
)
mscLpEngFcrcOvLnnConnectionPoolCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngFcrcOvLnnConnectionPoolCapacity.setStatus("mandatory")
_MscLpEngFcrcPqc_ObjectIdentity = ObjectIdentity
mscLpEngFcrcPqc = _MscLpEngFcrcPqc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 3)
)
_MscLpEngFcrcPqcRowStatusTable_Object = MibTable
mscLpEngFcrcPqcRowStatusTable = _MscLpEngFcrcPqcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 3, 1)
)
if mibBuilder.loadTexts:
    mscLpEngFcrcPqcRowStatusTable.setStatus("mandatory")
_MscLpEngFcrcPqcRowStatusEntry_Object = MibTableRow
mscLpEngFcrcPqcRowStatusEntry = _MscLpEngFcrcPqcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 3, 1, 1)
)
mscLpEngFcrcPqcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngFcrcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngFcrcPqcIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngFcrcPqcRowStatusEntry.setStatus("mandatory")
_MscLpEngFcrcPqcRowStatus_Type = RowStatus
_MscLpEngFcrcPqcRowStatus_Object = MibTableColumn
mscLpEngFcrcPqcRowStatus = _MscLpEngFcrcPqcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 3, 1, 1, 1),
    _MscLpEngFcrcPqcRowStatus_Type()
)
mscLpEngFcrcPqcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngFcrcPqcRowStatus.setStatus("mandatory")
_MscLpEngFcrcPqcComponentName_Type = DisplayString
_MscLpEngFcrcPqcComponentName_Object = MibTableColumn
mscLpEngFcrcPqcComponentName = _MscLpEngFcrcPqcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 3, 1, 1, 2),
    _MscLpEngFcrcPqcComponentName_Type()
)
mscLpEngFcrcPqcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFcrcPqcComponentName.setStatus("mandatory")
_MscLpEngFcrcPqcStorageType_Type = StorageType
_MscLpEngFcrcPqcStorageType_Object = MibTableColumn
mscLpEngFcrcPqcStorageType = _MscLpEngFcrcPqcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 3, 1, 1, 4),
    _MscLpEngFcrcPqcStorageType_Type()
)
mscLpEngFcrcPqcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFcrcPqcStorageType.setStatus("mandatory")
_MscLpEngFcrcPqcIndex_Type = NonReplicated
_MscLpEngFcrcPqcIndex_Object = MibTableColumn
mscLpEngFcrcPqcIndex = _MscLpEngFcrcPqcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 3, 1, 1, 10),
    _MscLpEngFcrcPqcIndex_Type()
)
mscLpEngFcrcPqcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEngFcrcPqcIndex.setStatus("mandatory")
_MscLpEngFcrcPqcOv_ObjectIdentity = ObjectIdentity
mscLpEngFcrcPqcOv = _MscLpEngFcrcPqcOv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 3, 2)
)
_MscLpEngFcrcPqcOvRowStatusTable_Object = MibTable
mscLpEngFcrcPqcOvRowStatusTable = _MscLpEngFcrcPqcOvRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscLpEngFcrcPqcOvRowStatusTable.setStatus("mandatory")
_MscLpEngFcrcPqcOvRowStatusEntry_Object = MibTableRow
mscLpEngFcrcPqcOvRowStatusEntry = _MscLpEngFcrcPqcOvRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 3, 2, 1, 1)
)
mscLpEngFcrcPqcOvRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngFcrcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngFcrcPqcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngFcrcPqcOvIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngFcrcPqcOvRowStatusEntry.setStatus("mandatory")
_MscLpEngFcrcPqcOvRowStatus_Type = RowStatus
_MscLpEngFcrcPqcOvRowStatus_Object = MibTableColumn
mscLpEngFcrcPqcOvRowStatus = _MscLpEngFcrcPqcOvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 3, 2, 1, 1, 1),
    _MscLpEngFcrcPqcOvRowStatus_Type()
)
mscLpEngFcrcPqcOvRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFcrcPqcOvRowStatus.setStatus("mandatory")
_MscLpEngFcrcPqcOvComponentName_Type = DisplayString
_MscLpEngFcrcPqcOvComponentName_Object = MibTableColumn
mscLpEngFcrcPqcOvComponentName = _MscLpEngFcrcPqcOvComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 3, 2, 1, 1, 2),
    _MscLpEngFcrcPqcOvComponentName_Type()
)
mscLpEngFcrcPqcOvComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFcrcPqcOvComponentName.setStatus("mandatory")
_MscLpEngFcrcPqcOvStorageType_Type = StorageType
_MscLpEngFcrcPqcOvStorageType_Object = MibTableColumn
mscLpEngFcrcPqcOvStorageType = _MscLpEngFcrcPqcOvStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 3, 2, 1, 1, 4),
    _MscLpEngFcrcPqcOvStorageType_Type()
)
mscLpEngFcrcPqcOvStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFcrcPqcOvStorageType.setStatus("mandatory")
_MscLpEngFcrcPqcOvIndex_Type = NonReplicated
_MscLpEngFcrcPqcOvIndex_Object = MibTableColumn
mscLpEngFcrcPqcOvIndex = _MscLpEngFcrcPqcOvIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 3, 2, 1, 1, 10),
    _MscLpEngFcrcPqcOvIndex_Type()
)
mscLpEngFcrcPqcOvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEngFcrcPqcOvIndex.setStatus("mandatory")
_MscLpEngFcrcPqcOvProvTable_Object = MibTable
mscLpEngFcrcPqcOvProvTable = _MscLpEngFcrcPqcOvProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscLpEngFcrcPqcOvProvTable.setStatus("mandatory")
_MscLpEngFcrcPqcOvProvEntry_Object = MibTableRow
mscLpEngFcrcPqcOvProvEntry = _MscLpEngFcrcPqcOvProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 3, 2, 10, 1)
)
mscLpEngFcrcPqcOvProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngFcrcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngFcrcPqcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngFcrcPqcOvIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngFcrcPqcOvProvEntry.setStatus("mandatory")


class _MscLpEngFcrcPqcOvIpRoutesPoolCapacity_Type(Unsigned32):
    """Custom type mscLpEngFcrcPqcOvIpRoutesPoolCapacity based on Unsigned32"""
    defaultValue = 4096

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MscLpEngFcrcPqcOvIpRoutesPoolCapacity_Type.__name__ = "Unsigned32"
_MscLpEngFcrcPqcOvIpRoutesPoolCapacity_Object = MibTableColumn
mscLpEngFcrcPqcOvIpRoutesPoolCapacity = _MscLpEngFcrcPqcOvIpRoutesPoolCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 3, 2, 10, 1, 1),
    _MscLpEngFcrcPqcOvIpRoutesPoolCapacity_Type()
)
mscLpEngFcrcPqcOvIpRoutesPoolCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEngFcrcPqcOvIpRoutesPoolCapacity.setStatus("mandatory")
_MscLpEngFcrcPqcOperTable_Object = MibTable
mscLpEngFcrcPqcOperTable = _MscLpEngFcrcPqcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 3, 10)
)
if mibBuilder.loadTexts:
    mscLpEngFcrcPqcOperTable.setStatus("mandatory")
_MscLpEngFcrcPqcOperEntry_Object = MibTableRow
mscLpEngFcrcPqcOperEntry = _MscLpEngFcrcPqcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 3, 10, 1)
)
mscLpEngFcrcPqcOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngFcrcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngFcrcPqcIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngFcrcPqcOperEntry.setStatus("mandatory")


class _MscLpEngFcrcPqcIpRoutesPoolSize_Type(Gauge32):
    """Custom type mscLpEngFcrcPqcIpRoutesPoolSize based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MscLpEngFcrcPqcIpRoutesPoolSize_Type.__name__ = "Gauge32"
_MscLpEngFcrcPqcIpRoutesPoolSize_Object = MibTableColumn
mscLpEngFcrcPqcIpRoutesPoolSize = _MscLpEngFcrcPqcIpRoutesPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 3, 10, 1, 1),
    _MscLpEngFcrcPqcIpRoutesPoolSize_Type()
)
mscLpEngFcrcPqcIpRoutesPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFcrcPqcIpRoutesPoolSize.setStatus("mandatory")


class _MscLpEngFcrcPqcIpRoutesPoolUsage_Type(Gauge32):
    """Custom type mscLpEngFcrcPqcIpRoutesPoolUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MscLpEngFcrcPqcIpRoutesPoolUsage_Type.__name__ = "Gauge32"
_MscLpEngFcrcPqcIpRoutesPoolUsage_Object = MibTableColumn
mscLpEngFcrcPqcIpRoutesPoolUsage = _MscLpEngFcrcPqcIpRoutesPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 3, 10, 1, 2),
    _MscLpEngFcrcPqcIpRoutesPoolUsage_Type()
)
mscLpEngFcrcPqcIpRoutesPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFcrcPqcIpRoutesPoolUsage.setStatus("mandatory")


class _MscLpEngFcrcPqcIpRoutesPoolAvailableEst_Type(Gauge32):
    """Custom type mscLpEngFcrcPqcIpRoutesPoolAvailableEst based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MscLpEngFcrcPqcIpRoutesPoolAvailableEst_Type.__name__ = "Gauge32"
_MscLpEngFcrcPqcIpRoutesPoolAvailableEst_Object = MibTableColumn
mscLpEngFcrcPqcIpRoutesPoolAvailableEst = _MscLpEngFcrcPqcIpRoutesPoolAvailableEst_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 3, 10, 1, 3),
    _MscLpEngFcrcPqcIpRoutesPoolAvailableEst_Type()
)
mscLpEngFcrcPqcIpRoutesPoolAvailableEst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFcrcPqcIpRoutesPoolAvailableEst.setStatus("mandatory")
_MscLpEngFcrcOperTable_Object = MibTable
mscLpEngFcrcOperTable = _MscLpEngFcrcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 10)
)
if mibBuilder.loadTexts:
    mscLpEngFcrcOperTable.setStatus("mandatory")
_MscLpEngFcrcOperEntry_Object = MibTableRow
mscLpEngFcrcOperEntry = _MscLpEngFcrcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 10, 1)
)
mscLpEngFcrcOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngFcrcIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngFcrcOperEntry.setStatus("mandatory")


class _MscLpEngFcrcSubConnectionPoolAvailable_Type(Unsigned32):
    """Custom type mscLpEngFcrcSubConnectionPoolAvailable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49152),
    )


_MscLpEngFcrcSubConnectionPoolAvailable_Type.__name__ = "Unsigned32"
_MscLpEngFcrcSubConnectionPoolAvailable_Object = MibTableColumn
mscLpEngFcrcSubConnectionPoolAvailable = _MscLpEngFcrcSubConnectionPoolAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 10, 1, 1),
    _MscLpEngFcrcSubConnectionPoolAvailable_Type()
)
mscLpEngFcrcSubConnectionPoolAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFcrcSubConnectionPoolAvailable.setStatus("mandatory")


class _MscLpEngFcrcSubConnectionPoolUsage_Type(Unsigned32):
    """Custom type mscLpEngFcrcSubConnectionPoolUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49152),
    )


_MscLpEngFcrcSubConnectionPoolUsage_Type.__name__ = "Unsigned32"
_MscLpEngFcrcSubConnectionPoolUsage_Object = MibTableColumn
mscLpEngFcrcSubConnectionPoolUsage = _MscLpEngFcrcSubConnectionPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 10, 1, 2),
    _MscLpEngFcrcSubConnectionPoolUsage_Type()
)
mscLpEngFcrcSubConnectionPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFcrcSubConnectionPoolUsage.setStatus("mandatory")


class _MscLpEngFcrcLnnConnectionPoolAvailable_Type(Unsigned32):
    """Custom type mscLpEngFcrcLnnConnectionPoolAvailable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_MscLpEngFcrcLnnConnectionPoolAvailable_Type.__name__ = "Unsigned32"
_MscLpEngFcrcLnnConnectionPoolAvailable_Object = MibTableColumn
mscLpEngFcrcLnnConnectionPoolAvailable = _MscLpEngFcrcLnnConnectionPoolAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 10, 1, 3),
    _MscLpEngFcrcLnnConnectionPoolAvailable_Type()
)
mscLpEngFcrcLnnConnectionPoolAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFcrcLnnConnectionPoolAvailable.setStatus("mandatory")


class _MscLpEngFcrcLnnConnectionPoolUsage_Type(Unsigned32):
    """Custom type mscLpEngFcrcLnnConnectionPoolUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_MscLpEngFcrcLnnConnectionPoolUsage_Type.__name__ = "Unsigned32"
_MscLpEngFcrcLnnConnectionPoolUsage_Object = MibTableColumn
mscLpEngFcrcLnnConnectionPoolUsage = _MscLpEngFcrcLnnConnectionPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 10, 1, 4),
    _MscLpEngFcrcLnnConnectionPoolUsage_Type()
)
mscLpEngFcrcLnnConnectionPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFcrcLnnConnectionPoolUsage.setStatus("mandatory")


class _MscLpEngFcrcTxFrameMemoryAvailable_Type(Gauge32):
    """Custom type mscLpEngFcrcTxFrameMemoryAvailable based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscLpEngFcrcTxFrameMemoryAvailable_Type.__name__ = "Gauge32"
_MscLpEngFcrcTxFrameMemoryAvailable_Object = MibTableColumn
mscLpEngFcrcTxFrameMemoryAvailable = _MscLpEngFcrcTxFrameMemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 10, 1, 5),
    _MscLpEngFcrcTxFrameMemoryAvailable_Type()
)
mscLpEngFcrcTxFrameMemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFcrcTxFrameMemoryAvailable.setStatus("mandatory")


class _MscLpEngFcrcTxFrameMemoryMinAvailable_Type(Gauge32):
    """Custom type mscLpEngFcrcTxFrameMemoryMinAvailable based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscLpEngFcrcTxFrameMemoryMinAvailable_Type.__name__ = "Gauge32"
_MscLpEngFcrcTxFrameMemoryMinAvailable_Object = MibTableColumn
mscLpEngFcrcTxFrameMemoryMinAvailable = _MscLpEngFcrcTxFrameMemoryMinAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 10, 1, 6),
    _MscLpEngFcrcTxFrameMemoryMinAvailable_Type()
)
mscLpEngFcrcTxFrameMemoryMinAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFcrcTxFrameMemoryMinAvailable.setStatus("mandatory")


class _MscLpEngFcrcTxFrameMemoryCongestionState_Type(Gauge32):
    """Custom type mscLpEngFcrcTxFrameMemoryCongestionState based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscLpEngFcrcTxFrameMemoryCongestionState_Type.__name__ = "Gauge32"
_MscLpEngFcrcTxFrameMemoryCongestionState_Object = MibTableColumn
mscLpEngFcrcTxFrameMemoryCongestionState = _MscLpEngFcrcTxFrameMemoryCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 10, 1, 7),
    _MscLpEngFcrcTxFrameMemoryCongestionState_Type()
)
mscLpEngFcrcTxFrameMemoryCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFcrcTxFrameMemoryCongestionState.setStatus("mandatory")


class _MscLpEngFcrcRxFrameMemoryAvailable_Type(Gauge32):
    """Custom type mscLpEngFcrcRxFrameMemoryAvailable based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscLpEngFcrcRxFrameMemoryAvailable_Type.__name__ = "Gauge32"
_MscLpEngFcrcRxFrameMemoryAvailable_Object = MibTableColumn
mscLpEngFcrcRxFrameMemoryAvailable = _MscLpEngFcrcRxFrameMemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 10, 1, 8),
    _MscLpEngFcrcRxFrameMemoryAvailable_Type()
)
mscLpEngFcrcRxFrameMemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFcrcRxFrameMemoryAvailable.setStatus("mandatory")


class _MscLpEngFcrcRxFrameMemoryMinAvailable_Type(Gauge32):
    """Custom type mscLpEngFcrcRxFrameMemoryMinAvailable based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscLpEngFcrcRxFrameMemoryMinAvailable_Type.__name__ = "Gauge32"
_MscLpEngFcrcRxFrameMemoryMinAvailable_Object = MibTableColumn
mscLpEngFcrcRxFrameMemoryMinAvailable = _MscLpEngFcrcRxFrameMemoryMinAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 10, 1, 9),
    _MscLpEngFcrcRxFrameMemoryMinAvailable_Type()
)
mscLpEngFcrcRxFrameMemoryMinAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFcrcRxFrameMemoryMinAvailable.setStatus("mandatory")


class _MscLpEngFcrcRxFrameMemoryCongestionState_Type(Gauge32):
    """Custom type mscLpEngFcrcRxFrameMemoryCongestionState based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscLpEngFcrcRxFrameMemoryCongestionState_Type.__name__ = "Gauge32"
_MscLpEngFcrcRxFrameMemoryCongestionState_Object = MibTableColumn
mscLpEngFcrcRxFrameMemoryCongestionState = _MscLpEngFcrcRxFrameMemoryCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 10, 1, 10),
    _MscLpEngFcrcRxFrameMemoryCongestionState_Type()
)
mscLpEngFcrcRxFrameMemoryCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFcrcRxFrameMemoryCongestionState.setStatus("mandatory")
_MscLpEngFcrcTxFrThreshTable_Object = MibTable
mscLpEngFcrcTxFrThreshTable = _MscLpEngFcrcTxFrThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 442)
)
if mibBuilder.loadTexts:
    mscLpEngFcrcTxFrThreshTable.setStatus("mandatory")
_MscLpEngFcrcTxFrThreshEntry_Object = MibTableRow
mscLpEngFcrcTxFrThreshEntry = _MscLpEngFcrcTxFrThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 442, 1)
)
mscLpEngFcrcTxFrThreshEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngFcrcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngFcrcTxFrThreshIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngFcrcTxFrThreshEntry.setStatus("mandatory")


class _MscLpEngFcrcTxFrThreshIndex_Type(Integer32):
    """Custom type mscLpEngFcrcTxFrThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscLpEngFcrcTxFrThreshIndex_Type.__name__ = "Integer32"
_MscLpEngFcrcTxFrThreshIndex_Object = MibTableColumn
mscLpEngFcrcTxFrThreshIndex = _MscLpEngFcrcTxFrThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 442, 1, 1),
    _MscLpEngFcrcTxFrThreshIndex_Type()
)
mscLpEngFcrcTxFrThreshIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEngFcrcTxFrThreshIndex.setStatus("mandatory")


class _MscLpEngFcrcTxFrThreshValue_Type(Unsigned32):
    """Custom type mscLpEngFcrcTxFrThreshValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscLpEngFcrcTxFrThreshValue_Type.__name__ = "Unsigned32"
_MscLpEngFcrcTxFrThreshValue_Object = MibTableColumn
mscLpEngFcrcTxFrThreshValue = _MscLpEngFcrcTxFrThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 442, 1, 2),
    _MscLpEngFcrcTxFrThreshValue_Type()
)
mscLpEngFcrcTxFrThreshValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFcrcTxFrThreshValue.setStatus("mandatory")
_MscLpEngFcrcRxFrThreshTable_Object = MibTable
mscLpEngFcrcRxFrThreshTable = _MscLpEngFcrcRxFrThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 446)
)
if mibBuilder.loadTexts:
    mscLpEngFcrcRxFrThreshTable.setStatus("mandatory")
_MscLpEngFcrcRxFrThreshEntry_Object = MibTableRow
mscLpEngFcrcRxFrThreshEntry = _MscLpEngFcrcRxFrThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 446, 1)
)
mscLpEngFcrcRxFrThreshEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngFcrcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBaseMIB", "mscLpEngFcrcRxFrThreshIndex"),
)
if mibBuilder.loadTexts:
    mscLpEngFcrcRxFrThreshEntry.setStatus("mandatory")


class _MscLpEngFcrcRxFrThreshIndex_Type(Integer32):
    """Custom type mscLpEngFcrcRxFrThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscLpEngFcrcRxFrThreshIndex_Type.__name__ = "Integer32"
_MscLpEngFcrcRxFrThreshIndex_Object = MibTableColumn
mscLpEngFcrcRxFrThreshIndex = _MscLpEngFcrcRxFrThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 446, 1, 1),
    _MscLpEngFcrcRxFrThreshIndex_Type()
)
mscLpEngFcrcRxFrThreshIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEngFcrcRxFrThreshIndex.setStatus("mandatory")


class _MscLpEngFcrcRxFrThreshValue_Type(Unsigned32):
    """Custom type mscLpEngFcrcRxFrThreshValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscLpEngFcrcRxFrThreshValue_Type.__name__ = "Unsigned32"
_MscLpEngFcrcRxFrThreshValue_Object = MibTableColumn
mscLpEngFcrcRxFrThreshValue = _MscLpEngFcrcRxFrThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 6, 446, 1, 2),
    _MscLpEngFcrcRxFrThreshValue_Type()
)
mscLpEngFcrcRxFrThreshValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEngFcrcRxFrThreshValue.setStatus("mandatory")
_AtmBaseMIB_ObjectIdentity = ObjectIdentity
atmBaseMIB = _AtmBaseMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 63)
)
_AtmBaseGroup_ObjectIdentity = ObjectIdentity
atmBaseGroup = _AtmBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 63, 1)
)
_AtmBaseGroupCA_ObjectIdentity = ObjectIdentity
atmBaseGroupCA = _AtmBaseGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 63, 1, 1)
)
_AtmBaseGroupCA02_ObjectIdentity = ObjectIdentity
atmBaseGroupCA02 = _AtmBaseGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 63, 1, 1, 3)
)
_AtmBaseGroupCA02A_ObjectIdentity = ObjectIdentity
atmBaseGroupCA02A = _AtmBaseGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 63, 1, 1, 3, 2)
)
_AtmBaseCapabilities_ObjectIdentity = ObjectIdentity
atmBaseCapabilities = _AtmBaseCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 63, 3)
)
_AtmBaseCapabilitiesCA_ObjectIdentity = ObjectIdentity
atmBaseCapabilitiesCA = _AtmBaseCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 63, 3, 1)
)
_AtmBaseCapabilitiesCA02_ObjectIdentity = ObjectIdentity
atmBaseCapabilitiesCA02 = _AtmBaseCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 63, 3, 1, 3)
)
_AtmBaseCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
atmBaseCapabilitiesCA02A = _AtmBaseCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 63, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-AtmBaseMIB",
    **{"mscLpArc": mscLpArc,
       "mscLpArcRowStatusTable": mscLpArcRowStatusTable,
       "mscLpArcRowStatusEntry": mscLpArcRowStatusEntry,
       "mscLpArcRowStatus": mscLpArcRowStatus,
       "mscLpArcComponentName": mscLpArcComponentName,
       "mscLpArcStorageType": mscLpArcStorageType,
       "mscLpArcIndex": mscLpArcIndex,
       "mscLpArcProvTable": mscLpArcProvTable,
       "mscLpArcProvEntry": mscLpArcProvEntry,
       "mscLpArcTotalConnectionPoolCapacity": mscLpArcTotalConnectionPoolCapacity,
       "mscLpArcMulticastBranchesCapacity": mscLpArcMulticastBranchesCapacity,
       "mscLpArcTxFrameMemoryAllocation": mscLpArcTxFrameMemoryAllocation,
       "mscLpArcRxFrameMemoryAllocation": mscLpArcRxFrameMemoryAllocation,
       "mscLpArcPerVcQueueInterfaces": mscLpArcPerVcQueueInterfaces,
       "mscLpArcShapingStackAllocation": mscLpArcShapingStackAllocation,
       "mscLpArcShapingScalingFactor": mscLpArcShapingScalingFactor,
       "mscLpArcCdvAttenuation": mscLpArcCdvAttenuation,
       "mscLpArcPortAggregation": mscLpArcPortAggregation,
       "mscLpArcSubConnectionPoolCapacity": mscLpArcSubConnectionPoolCapacity,
       "mscLpArcLnnConnectionPoolCapacity": mscLpArcLnnConnectionPoolCapacity,
       "mscLpArcConnCapTable": mscLpArcConnCapTable,
       "mscLpArcConnCapEntry": mscLpArcConnCapEntry,
       "mscLpArcConnCapIndex": mscLpArcConnCapIndex,
       "mscLpArcConnCapValue": mscLpArcConnCapValue,
       "mscLpAru": mscLpAru,
       "mscLpAruRowStatusTable": mscLpAruRowStatusTable,
       "mscLpAruRowStatusEntry": mscLpAruRowStatusEntry,
       "mscLpAruRowStatus": mscLpAruRowStatus,
       "mscLpAruComponentName": mscLpAruComponentName,
       "mscLpAruStorageType": mscLpAruStorageType,
       "mscLpAruIndex": mscLpAruIndex,
       "mscLpAruOperTable": mscLpAruOperTable,
       "mscLpAruOperEntry": mscLpAruOperEntry,
       "mscLpAruTotalConnectionPoolUsage": mscLpAruTotalConnectionPoolUsage,
       "mscLpAruMulticastBranchesUsage": mscLpAruMulticastBranchesUsage,
       "mscLpAruTxCellBlockCapacity": mscLpAruTxCellBlockCapacity,
       "mscLpAruTxCellBlockUsage": mscLpAruTxCellBlockUsage,
       "mscLpAruTxCellFreeListSize": mscLpAruTxCellFreeListSize,
       "mscLpAruTxCellFreeListCongestionState": mscLpAruTxCellFreeListCongestionState,
       "mscLpAruTxFrameMemoryAllocation": mscLpAruTxFrameMemoryAllocation,
       "mscLpAruTxFrameBlockCapacity": mscLpAruTxFrameBlockCapacity,
       "mscLpAruTxFrameBlockUsage": mscLpAruTxFrameBlockUsage,
       "mscLpAruTxFrameFreeListSize": mscLpAruTxFrameFreeListSize,
       "mscLpAruTxFrameFreeListCongestionState": mscLpAruTxFrameFreeListCongestionState,
       "mscLpAruRxCellBlockCapacity": mscLpAruRxCellBlockCapacity,
       "mscLpAruRxCellBlockUsage": mscLpAruRxCellBlockUsage,
       "mscLpAruRxCellFreeListSize": mscLpAruRxCellFreeListSize,
       "mscLpAruRxCellFreeListCongestionState": mscLpAruRxCellFreeListCongestionState,
       "mscLpAruRxFrameMemoryAllocation": mscLpAruRxFrameMemoryAllocation,
       "mscLpAruRxFrameBlockCapacity": mscLpAruRxFrameBlockCapacity,
       "mscLpAruRxFrameBlockUsage": mscLpAruRxFrameBlockUsage,
       "mscLpAruRxFrameFreeListSize": mscLpAruRxFrameFreeListSize,
       "mscLpAruRxFrameFreeListCongestionState": mscLpAruRxFrameFreeListCongestionState,
       "mscLpAruSubConnectionPoolAvailable": mscLpAruSubConnectionPoolAvailable,
       "mscLpAruSubConnectionPoolUsage": mscLpAruSubConnectionPoolUsage,
       "mscLpAruLnnConnectionPoolAvailable": mscLpAruLnnConnectionPoolAvailable,
       "mscLpAruLnnConnectionPoolUsage": mscLpAruLnnConnectionPoolUsage,
       "mscLpAruConnUsageTable": mscLpAruConnUsageTable,
       "mscLpAruConnUsageEntry": mscLpAruConnUsageEntry,
       "mscLpAruConnUsageIndex": mscLpAruConnUsageIndex,
       "mscLpAruConnUsageValue": mscLpAruConnUsageValue,
       "mscLpAruTxCflThreshTable": mscLpAruTxCflThreshTable,
       "mscLpAruTxCflThreshEntry": mscLpAruTxCflThreshEntry,
       "mscLpAruTxCflThreshIndex": mscLpAruTxCflThreshIndex,
       "mscLpAruTxCflThreshValue": mscLpAruTxCflThreshValue,
       "mscLpAruTxFflThreshTable": mscLpAruTxFflThreshTable,
       "mscLpAruTxFflThreshEntry": mscLpAruTxFflThreshEntry,
       "mscLpAruTxFflThreshIndex": mscLpAruTxFflThreshIndex,
       "mscLpAruTxFflThreshValue": mscLpAruTxFflThreshValue,
       "mscLpAruRxCflThreshTable": mscLpAruRxCflThreshTable,
       "mscLpAruRxCflThreshEntry": mscLpAruRxCflThreshEntry,
       "mscLpAruRxCflThreshIndex": mscLpAruRxCflThreshIndex,
       "mscLpAruRxCflThreshValue": mscLpAruRxCflThreshValue,
       "mscLpAruRxFflThreshTable": mscLpAruRxFflThreshTable,
       "mscLpAruRxFflThreshEntry": mscLpAruRxFflThreshEntry,
       "mscLpAruRxFflThreshIndex": mscLpAruRxFflThreshIndex,
       "mscLpAruRxFflThreshValue": mscLpAruRxFflThreshValue,
       "mscLpEngArc": mscLpEngArc,
       "mscLpEngArcRowStatusTable": mscLpEngArcRowStatusTable,
       "mscLpEngArcRowStatusEntry": mscLpEngArcRowStatusEntry,
       "mscLpEngArcRowStatus": mscLpEngArcRowStatus,
       "mscLpEngArcComponentName": mscLpEngArcComponentName,
       "mscLpEngArcStorageType": mscLpEngArcStorageType,
       "mscLpEngArcIndex": mscLpEngArcIndex,
       "mscLpEngArcOv": mscLpEngArcOv,
       "mscLpEngArcOvRowStatusTable": mscLpEngArcOvRowStatusTable,
       "mscLpEngArcOvRowStatusEntry": mscLpEngArcOvRowStatusEntry,
       "mscLpEngArcOvRowStatus": mscLpEngArcOvRowStatus,
       "mscLpEngArcOvComponentName": mscLpEngArcOvComponentName,
       "mscLpEngArcOvStorageType": mscLpEngArcOvStorageType,
       "mscLpEngArcOvIndex": mscLpEngArcOvIndex,
       "mscLpEngArcOvProvTable": mscLpEngArcOvProvTable,
       "mscLpEngArcOvProvEntry": mscLpEngArcOvProvEntry,
       "mscLpEngArcOvTotalConnectionPoolCapacity": mscLpEngArcOvTotalConnectionPoolCapacity,
       "mscLpEngArcOvMulticastBranchesCapacity": mscLpEngArcOvMulticastBranchesCapacity,
       "mscLpEngArcOvTxCellMemoryAllocation": mscLpEngArcOvTxCellMemoryAllocation,
       "mscLpEngArcOvRxCellMemoryAllocation": mscLpEngArcOvRxCellMemoryAllocation,
       "mscLpEngArcCqc": mscLpEngArcCqc,
       "mscLpEngArcCqcRowStatusTable": mscLpEngArcCqcRowStatusTable,
       "mscLpEngArcCqcRowStatusEntry": mscLpEngArcCqcRowStatusEntry,
       "mscLpEngArcCqcRowStatus": mscLpEngArcCqcRowStatus,
       "mscLpEngArcCqcComponentName": mscLpEngArcCqcComponentName,
       "mscLpEngArcCqcStorageType": mscLpEngArcCqcStorageType,
       "mscLpEngArcCqcIndex": mscLpEngArcCqcIndex,
       "mscLpEngArcCqcOv": mscLpEngArcCqcOv,
       "mscLpEngArcCqcOvRowStatusTable": mscLpEngArcCqcOvRowStatusTable,
       "mscLpEngArcCqcOvRowStatusEntry": mscLpEngArcCqcOvRowStatusEntry,
       "mscLpEngArcCqcOvRowStatus": mscLpEngArcCqcOvRowStatus,
       "mscLpEngArcCqcOvComponentName": mscLpEngArcCqcOvComponentName,
       "mscLpEngArcCqcOvStorageType": mscLpEngArcCqcOvStorageType,
       "mscLpEngArcCqcOvIndex": mscLpEngArcCqcOvIndex,
       "mscLpEngArcCqcOvProvTable": mscLpEngArcCqcOvProvTable,
       "mscLpEngArcCqcOvProvEntry": mscLpEngArcCqcOvProvEntry,
       "mscLpEngArcCqcOvPerVcQueueInterfaces": mscLpEngArcCqcOvPerVcQueueInterfaces,
       "mscLpEngArcCqcOvShapingScalingFactor": mscLpEngArcCqcOvShapingScalingFactor,
       "mscLpEngArcCqcOvCdvReduction": mscLpEngArcCqcOvCdvReduction,
       "mscLpEngArcCqcOvPortCongestionPolicy": mscLpEngArcCqcOvPortCongestionPolicy,
       "mscLpEngArcCqcOvConnCapTable": mscLpEngArcCqcOvConnCapTable,
       "mscLpEngArcCqcOvConnCapEntry": mscLpEngArcCqcOvConnCapEntry,
       "mscLpEngArcCqcOvConnCapIndex": mscLpEngArcCqcOvConnCapIndex,
       "mscLpEngArcCqcOvConnCapValue": mscLpEngArcCqcOvConnCapValue,
       "mscLpEngArcCqcOperTable": mscLpEngArcCqcOperTable,
       "mscLpEngArcCqcOperEntry": mscLpEngArcCqcOperEntry,
       "mscLpEngArcCqcCdvReduction": mscLpEngArcCqcCdvReduction,
       "mscLpEngArcAqm": mscLpEngArcAqm,
       "mscLpEngArcAqmRowStatusTable": mscLpEngArcAqmRowStatusTable,
       "mscLpEngArcAqmRowStatusEntry": mscLpEngArcAqmRowStatusEntry,
       "mscLpEngArcAqmRowStatus": mscLpEngArcAqmRowStatus,
       "mscLpEngArcAqmComponentName": mscLpEngArcAqmComponentName,
       "mscLpEngArcAqmStorageType": mscLpEngArcAqmStorageType,
       "mscLpEngArcAqmIndex": mscLpEngArcAqmIndex,
       "mscLpEngArcAqmOv": mscLpEngArcAqmOv,
       "mscLpEngArcAqmOvRowStatusTable": mscLpEngArcAqmOvRowStatusTable,
       "mscLpEngArcAqmOvRowStatusEntry": mscLpEngArcAqmOvRowStatusEntry,
       "mscLpEngArcAqmOvRowStatus": mscLpEngArcAqmOvRowStatus,
       "mscLpEngArcAqmOvComponentName": mscLpEngArcAqmOvComponentName,
       "mscLpEngArcAqmOvStorageType": mscLpEngArcAqmOvStorageType,
       "mscLpEngArcAqmOvIndex": mscLpEngArcAqmOvIndex,
       "mscLpEngArcAqmOvProvTable": mscLpEngArcAqmOvProvTable,
       "mscLpEngArcAqmOvProvEntry": mscLpEngArcAqmOvProvEntry,
       "mscLpEngArcAqmOvConnectionPoolCapacity": mscLpEngArcAqmOvConnectionPoolCapacity,
       "mscLpEngArcAqmOvHighPriorityEpdOffset": mscLpEngArcAqmOvHighPriorityEpdOffset,
       "mscLpEngArcAqmOvLowPriorityEpdOffset": mscLpEngArcAqmOvLowPriorityEpdOffset,
       "mscLpEngArcAqmOvPortCongestionPolicy": mscLpEngArcAqmOvPortCongestionPolicy,
       "mscLpEngArcAqmOperTable": mscLpEngArcAqmOperTable,
       "mscLpEngArcAqmOperEntry": mscLpEngArcAqmOperEntry,
       "mscLpEngArcAqmConnectionPoolAvailable": mscLpEngArcAqmConnectionPoolAvailable,
       "mscLpEngArcAqmConnectionPoolUsage": mscLpEngArcAqmConnectionPoolUsage,
       "mscLpEngArcAqmTxCellMemoryAvailable": mscLpEngArcAqmTxCellMemoryAvailable,
       "mscLpEngArcAqmTxCellMemoryMinAvailable": mscLpEngArcAqmTxCellMemoryMinAvailable,
       "mscLpEngArcAqmTxCellMemoryCongestionState": mscLpEngArcAqmTxCellMemoryCongestionState,
       "mscLpEngArcAqmTxCellThreshTable": mscLpEngArcAqmTxCellThreshTable,
       "mscLpEngArcAqmTxCellThreshEntry": mscLpEngArcAqmTxCellThreshEntry,
       "mscLpEngArcAqmTxCellThreshIndex": mscLpEngArcAqmTxCellThreshIndex,
       "mscLpEngArcAqmTxCellThreshValue": mscLpEngArcAqmTxCellThreshValue,
       "mscLpEngArcOperTable": mscLpEngArcOperTable,
       "mscLpEngArcOperEntry": mscLpEngArcOperEntry,
       "mscLpEngArcTotalConnectionPoolAvailable": mscLpEngArcTotalConnectionPoolAvailable,
       "mscLpEngArcTotalConnectionPoolUsage": mscLpEngArcTotalConnectionPoolUsage,
       "mscLpEngArcMulticastBranchesAvailable": mscLpEngArcMulticastBranchesAvailable,
       "mscLpEngArcMulticastBranchesUsage": mscLpEngArcMulticastBranchesUsage,
       "mscLpEngArcTxCellMemoryAllocation": mscLpEngArcTxCellMemoryAllocation,
       "mscLpEngArcTxCellMemoryAvailable": mscLpEngArcTxCellMemoryAvailable,
       "mscLpEngArcTxCellMemoryMinAvailable": mscLpEngArcTxCellMemoryMinAvailable,
       "mscLpEngArcTxCellMemoryCongestionState": mscLpEngArcTxCellMemoryCongestionState,
       "mscLpEngArcRxCellMemoryAllocation": mscLpEngArcRxCellMemoryAllocation,
       "mscLpEngArcRxCellMemoryAvailable": mscLpEngArcRxCellMemoryAvailable,
       "mscLpEngArcRxCellMemoryMinAvailable": mscLpEngArcRxCellMemoryMinAvailable,
       "mscLpEngArcRxCellMemoryCongestionState": mscLpEngArcRxCellMemoryCongestionState,
       "mscLpEngArcTxCellThreshTable": mscLpEngArcTxCellThreshTable,
       "mscLpEngArcTxCellThreshEntry": mscLpEngArcTxCellThreshEntry,
       "mscLpEngArcTxCellThreshIndex": mscLpEngArcTxCellThreshIndex,
       "mscLpEngArcTxCellThreshValue": mscLpEngArcTxCellThreshValue,
       "mscLpEngArcRxCellThreshTable": mscLpEngArcRxCellThreshTable,
       "mscLpEngArcRxCellThreshEntry": mscLpEngArcRxCellThreshEntry,
       "mscLpEngArcRxCellThreshIndex": mscLpEngArcRxCellThreshIndex,
       "mscLpEngArcRxCellThreshValue": mscLpEngArcRxCellThreshValue,
       "mscLpEngFcrc": mscLpEngFcrc,
       "mscLpEngFcrcRowStatusTable": mscLpEngFcrcRowStatusTable,
       "mscLpEngFcrcRowStatusEntry": mscLpEngFcrcRowStatusEntry,
       "mscLpEngFcrcRowStatus": mscLpEngFcrcRowStatus,
       "mscLpEngFcrcComponentName": mscLpEngFcrcComponentName,
       "mscLpEngFcrcStorageType": mscLpEngFcrcStorageType,
       "mscLpEngFcrcIndex": mscLpEngFcrcIndex,
       "mscLpEngFcrcOv": mscLpEngFcrcOv,
       "mscLpEngFcrcOvRowStatusTable": mscLpEngFcrcOvRowStatusTable,
       "mscLpEngFcrcOvRowStatusEntry": mscLpEngFcrcOvRowStatusEntry,
       "mscLpEngFcrcOvRowStatus": mscLpEngFcrcOvRowStatus,
       "mscLpEngFcrcOvComponentName": mscLpEngFcrcOvComponentName,
       "mscLpEngFcrcOvStorageType": mscLpEngFcrcOvStorageType,
       "mscLpEngFcrcOvIndex": mscLpEngFcrcOvIndex,
       "mscLpEngFcrcOvProvTable": mscLpEngFcrcOvProvTable,
       "mscLpEngFcrcOvProvEntry": mscLpEngFcrcOvProvEntry,
       "mscLpEngFcrcOvSubConnectionPoolCapacity": mscLpEngFcrcOvSubConnectionPoolCapacity,
       "mscLpEngFcrcOvLnnConnectionPoolCapacity": mscLpEngFcrcOvLnnConnectionPoolCapacity,
       "mscLpEngFcrcPqc": mscLpEngFcrcPqc,
       "mscLpEngFcrcPqcRowStatusTable": mscLpEngFcrcPqcRowStatusTable,
       "mscLpEngFcrcPqcRowStatusEntry": mscLpEngFcrcPqcRowStatusEntry,
       "mscLpEngFcrcPqcRowStatus": mscLpEngFcrcPqcRowStatus,
       "mscLpEngFcrcPqcComponentName": mscLpEngFcrcPqcComponentName,
       "mscLpEngFcrcPqcStorageType": mscLpEngFcrcPqcStorageType,
       "mscLpEngFcrcPqcIndex": mscLpEngFcrcPqcIndex,
       "mscLpEngFcrcPqcOv": mscLpEngFcrcPqcOv,
       "mscLpEngFcrcPqcOvRowStatusTable": mscLpEngFcrcPqcOvRowStatusTable,
       "mscLpEngFcrcPqcOvRowStatusEntry": mscLpEngFcrcPqcOvRowStatusEntry,
       "mscLpEngFcrcPqcOvRowStatus": mscLpEngFcrcPqcOvRowStatus,
       "mscLpEngFcrcPqcOvComponentName": mscLpEngFcrcPqcOvComponentName,
       "mscLpEngFcrcPqcOvStorageType": mscLpEngFcrcPqcOvStorageType,
       "mscLpEngFcrcPqcOvIndex": mscLpEngFcrcPqcOvIndex,
       "mscLpEngFcrcPqcOvProvTable": mscLpEngFcrcPqcOvProvTable,
       "mscLpEngFcrcPqcOvProvEntry": mscLpEngFcrcPqcOvProvEntry,
       "mscLpEngFcrcPqcOvIpRoutesPoolCapacity": mscLpEngFcrcPqcOvIpRoutesPoolCapacity,
       "mscLpEngFcrcPqcOperTable": mscLpEngFcrcPqcOperTable,
       "mscLpEngFcrcPqcOperEntry": mscLpEngFcrcPqcOperEntry,
       "mscLpEngFcrcPqcIpRoutesPoolSize": mscLpEngFcrcPqcIpRoutesPoolSize,
       "mscLpEngFcrcPqcIpRoutesPoolUsage": mscLpEngFcrcPqcIpRoutesPoolUsage,
       "mscLpEngFcrcPqcIpRoutesPoolAvailableEst": mscLpEngFcrcPqcIpRoutesPoolAvailableEst,
       "mscLpEngFcrcOperTable": mscLpEngFcrcOperTable,
       "mscLpEngFcrcOperEntry": mscLpEngFcrcOperEntry,
       "mscLpEngFcrcSubConnectionPoolAvailable": mscLpEngFcrcSubConnectionPoolAvailable,
       "mscLpEngFcrcSubConnectionPoolUsage": mscLpEngFcrcSubConnectionPoolUsage,
       "mscLpEngFcrcLnnConnectionPoolAvailable": mscLpEngFcrcLnnConnectionPoolAvailable,
       "mscLpEngFcrcLnnConnectionPoolUsage": mscLpEngFcrcLnnConnectionPoolUsage,
       "mscLpEngFcrcTxFrameMemoryAvailable": mscLpEngFcrcTxFrameMemoryAvailable,
       "mscLpEngFcrcTxFrameMemoryMinAvailable": mscLpEngFcrcTxFrameMemoryMinAvailable,
       "mscLpEngFcrcTxFrameMemoryCongestionState": mscLpEngFcrcTxFrameMemoryCongestionState,
       "mscLpEngFcrcRxFrameMemoryAvailable": mscLpEngFcrcRxFrameMemoryAvailable,
       "mscLpEngFcrcRxFrameMemoryMinAvailable": mscLpEngFcrcRxFrameMemoryMinAvailable,
       "mscLpEngFcrcRxFrameMemoryCongestionState": mscLpEngFcrcRxFrameMemoryCongestionState,
       "mscLpEngFcrcTxFrThreshTable": mscLpEngFcrcTxFrThreshTable,
       "mscLpEngFcrcTxFrThreshEntry": mscLpEngFcrcTxFrThreshEntry,
       "mscLpEngFcrcTxFrThreshIndex": mscLpEngFcrcTxFrThreshIndex,
       "mscLpEngFcrcTxFrThreshValue": mscLpEngFcrcTxFrThreshValue,
       "mscLpEngFcrcRxFrThreshTable": mscLpEngFcrcRxFrThreshTable,
       "mscLpEngFcrcRxFrThreshEntry": mscLpEngFcrcRxFrThreshEntry,
       "mscLpEngFcrcRxFrThreshIndex": mscLpEngFcrcRxFrThreshIndex,
       "mscLpEngFcrcRxFrThreshValue": mscLpEngFcrcRxFrThreshValue,
       "atmBaseMIB": atmBaseMIB,
       "atmBaseGroup": atmBaseGroup,
       "atmBaseGroupCA": atmBaseGroupCA,
       "atmBaseGroupCA02": atmBaseGroupCA02,
       "atmBaseGroupCA02A": atmBaseGroupCA02A,
       "atmBaseCapabilities": atmBaseCapabilities,
       "atmBaseCapabilitiesCA": atmBaseCapabilitiesCA,
       "atmBaseCapabilitiesCA02": atmBaseCapabilitiesCA02,
       "atmBaseCapabilitiesCA02A": atmBaseCapabilitiesCA02A}
)
