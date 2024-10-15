# SNMP MIB module (EQLSTORAGECONTAINER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQLSTORAGECONTAINER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:11 2024
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

(UTFString,) = mibBuilder.importSymbols(
    "EQLGROUP-MIB",
    "UTFString")

(eqlStoragePoolIndex,) = mibBuilder.importSymbols(
    "EQLSTORAGEPOOL-MIB",
    "eqlStoragePoolIndex")

(EQL2PartRowPointerStr,
 eqliscsiLocalMemberId) = mibBuilder.importSymbols(
    "EQLVOLUME-MIB",
    "EQL2PartRowPointerStr",
    "eqliscsiLocalMemberId")

(equalLogic,) = mibBuilder.importSymbols(
    "EQUALLOGIC-SMI",
    "equalLogic")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eqlStorageContainerModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 25)
)
eqlStorageContainerModule.setRevisions(
        ("2012-06-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Unsigned64(Counter64, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_EqlStorageContainerObjects_ObjectIdentity = ObjectIdentity
eqlStorageContainerObjects = _EqlStorageContainerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1)
)
_EqlStorageContainerTable_Object = MibTable
eqlStorageContainerTable = _EqlStorageContainerTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 1)
)
if mibBuilder.loadTexts:
    eqlStorageContainerTable.setStatus("current")
_EqlStorageContainerEntry_Object = MibTableRow
eqlStorageContainerEntry = _EqlStorageContainerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 1, 1)
)
eqlStorageContainerEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLSTORAGECONTAINER-MIB", "eqlStorageContainerIndex"),
)
if mibBuilder.loadTexts:
    eqlStorageContainerEntry.setStatus("current")
_EqlStorageContainerIndex_Type = Unsigned32
_EqlStorageContainerIndex_Object = MibTableColumn
eqlStorageContainerIndex = _EqlStorageContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 1, 1, 1),
    _EqlStorageContainerIndex_Type()
)
eqlStorageContainerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlStorageContainerIndex.setStatus("current")
_EqlStorageContainerRowStatus_Type = RowStatus
_EqlStorageContainerRowStatus_Object = MibTableColumn
eqlStorageContainerRowStatus = _EqlStorageContainerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 1, 1, 2),
    _EqlStorageContainerRowStatus_Type()
)
eqlStorageContainerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageContainerRowStatus.setStatus("current")


class _EqlStorageContainerUuid_Type(OctetString):
    """Custom type eqlStorageContainerUuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlStorageContainerUuid_Type.__name__ = "OctetString"
_EqlStorageContainerUuid_Object = MibTableColumn
eqlStorageContainerUuid = _EqlStorageContainerUuid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 1, 1, 3),
    _EqlStorageContainerUuid_Type()
)
eqlStorageContainerUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageContainerUuid.setStatus("current")


class _EqlStorageContainerName_Type(UTFString):
    """Custom type eqlStorageContainerName based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlStorageContainerName_Type.__name__ = "UTFString"
_EqlStorageContainerName_Object = MibTableColumn
eqlStorageContainerName = _EqlStorageContainerName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 1, 1, 4),
    _EqlStorageContainerName_Type()
)
eqlStorageContainerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageContainerName.setStatus("current")


class _EqlStorageContainerLookupName_Type(UTFString):
    """Custom type eqlStorageContainerLookupName based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlStorageContainerLookupName_Type.__name__ = "UTFString"
_EqlStorageContainerLookupName_Object = MibTableColumn
eqlStorageContainerLookupName = _EqlStorageContainerLookupName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 1, 1, 5),
    _EqlStorageContainerLookupName_Type()
)
eqlStorageContainerLookupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageContainerLookupName.setStatus("current")


class _EqlStorageContainerDescription_Type(UTFString):
    """Custom type eqlStorageContainerDescription based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EqlStorageContainerDescription_Type.__name__ = "UTFString"
_EqlStorageContainerDescription_Object = MibTableColumn
eqlStorageContainerDescription = _EqlStorageContainerDescription_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 1, 1, 6),
    _EqlStorageContainerDescription_Type()
)
eqlStorageContainerDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageContainerDescription.setStatus("current")


class _EqlStorageContainerLogicalLimit_Type(Unsigned64):
    """Custom type eqlStorageContainerLogicalLimit based on Unsigned64"""
    defaultValue = 8589934592


_EqlStorageContainerLogicalLimit_Object = MibTableColumn
eqlStorageContainerLogicalLimit = _EqlStorageContainerLogicalLimit_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 1, 1, 7),
    _EqlStorageContainerLogicalLimit_Type()
)
eqlStorageContainerLogicalLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageContainerLogicalLimit.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageContainerLogicalLimit.setUnits("MB")
_EqlStorageContainerStatisticsTable_Object = MibTable
eqlStorageContainerStatisticsTable = _EqlStorageContainerStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 2)
)
if mibBuilder.loadTexts:
    eqlStorageContainerStatisticsTable.setStatus("current")
_EqlStorageContainerStatisticsEntry_Object = MibTableRow
eqlStorageContainerStatisticsEntry = _EqlStorageContainerStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eqlStorageContainerStatisticsEntry.setStatus("current")
_EqlStorageContainerStatisticsLogicalUsed_Type = Unsigned64
_EqlStorageContainerStatisticsLogicalUsed_Object = MibTableColumn
eqlStorageContainerStatisticsLogicalUsed = _EqlStorageContainerStatisticsLogicalUsed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 2, 1, 1),
    _EqlStorageContainerStatisticsLogicalUsed_Type()
)
eqlStorageContainerStatisticsLogicalUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageContainerStatisticsLogicalUsed.setStatus("current")
_EqlStorageContainerStatisticsLogicalFree_Type = Unsigned64
_EqlStorageContainerStatisticsLogicalFree_Object = MibTableColumn
eqlStorageContainerStatisticsLogicalFree = _EqlStorageContainerStatisticsLogicalFree_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 2, 1, 2),
    _EqlStorageContainerStatisticsLogicalFree_Type()
)
eqlStorageContainerStatisticsLogicalFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageContainerStatisticsLogicalFree.setStatus("current")
_EqlStorageContainerStatisticsPhysicalUsed_Type = Unsigned64
_EqlStorageContainerStatisticsPhysicalUsed_Object = MibTableColumn
eqlStorageContainerStatisticsPhysicalUsed = _EqlStorageContainerStatisticsPhysicalUsed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 2, 1, 3),
    _EqlStorageContainerStatisticsPhysicalUsed_Type()
)
eqlStorageContainerStatisticsPhysicalUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageContainerStatisticsPhysicalUsed.setStatus("current")
_EqlStorageContainerStatisticsPhysicalFree_Type = Unsigned64
_EqlStorageContainerStatisticsPhysicalFree_Object = MibTableColumn
eqlStorageContainerStatisticsPhysicalFree = _EqlStorageContainerStatisticsPhysicalFree_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 2, 1, 4),
    _EqlStorageContainerStatisticsPhysicalFree_Type()
)
eqlStorageContainerStatisticsPhysicalFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageContainerStatisticsPhysicalFree.setStatus("current")
_EqlStorageContainerStatisticsThinProvFree_Type = Unsigned64
_EqlStorageContainerStatisticsThinProvFree_Object = MibTableColumn
eqlStorageContainerStatisticsThinProvFree = _EqlStorageContainerStatisticsThinProvFree_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 2, 1, 5),
    _EqlStorageContainerStatisticsThinProvFree_Type()
)
eqlStorageContainerStatisticsThinProvFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageContainerStatisticsThinProvFree.setStatus("current")
_EqlStorageContainerStatisticsVvolsBound_Type = Counter32
_EqlStorageContainerStatisticsVvolsBound_Object = MibTableColumn
eqlStorageContainerStatisticsVvolsBound = _EqlStorageContainerStatisticsVvolsBound_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 2, 1, 6),
    _EqlStorageContainerStatisticsVvolsBound_Type()
)
eqlStorageContainerStatisticsVvolsBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageContainerStatisticsVvolsBound.setStatus("current")
_EqlStorageContainerStatisticsSVCount_Type = Counter32
_EqlStorageContainerStatisticsSVCount_Object = MibTableColumn
eqlStorageContainerStatisticsSVCount = _EqlStorageContainerStatisticsSVCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 2, 1, 7),
    _EqlStorageContainerStatisticsSVCount_Type()
)
eqlStorageContainerStatisticsSVCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageContainerStatisticsSVCount.setStatus("current")
_EqlStorageContainerStatisticsSVSCount_Type = Counter32
_EqlStorageContainerStatisticsSVSCount_Object = MibTableColumn
eqlStorageContainerStatisticsSVSCount = _EqlStorageContainerStatisticsSVSCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 2, 1, 8),
    _EqlStorageContainerStatisticsSVSCount_Type()
)
eqlStorageContainerStatisticsSVSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageContainerStatisticsSVSCount.setStatus("current")
_EqlStorageContainerStatisticsThinProvisioned_Type = TruthValue
_EqlStorageContainerStatisticsThinProvisioned_Object = MibTableColumn
eqlStorageContainerStatisticsThinProvisioned = _EqlStorageContainerStatisticsThinProvisioned_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 2, 1, 9),
    _EqlStorageContainerStatisticsThinProvisioned_Type()
)
eqlStorageContainerStatisticsThinProvisioned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageContainerStatisticsThinProvisioned.setStatus("current")
_EqlStorageContainerStatisticsVvolsOnline_Type = Counter32
_EqlStorageContainerStatisticsVvolsOnline_Object = MibTableColumn
eqlStorageContainerStatisticsVvolsOnline = _EqlStorageContainerStatisticsVvolsOnline_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 2, 1, 10),
    _EqlStorageContainerStatisticsVvolsOnline_Type()
)
eqlStorageContainerStatisticsVvolsOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageContainerStatisticsVvolsOnline.setStatus("current")
_EqlStorageBucketTable_Object = MibTable
eqlStorageBucketTable = _EqlStorageBucketTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 3)
)
if mibBuilder.loadTexts:
    eqlStorageBucketTable.setStatus("current")
_EqlStorageBucketEntry_Object = MibTableRow
eqlStorageBucketEntry = _EqlStorageBucketEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 3, 1)
)
eqlStorageBucketEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLSTORAGECONTAINER-MIB", "eqlStorageBucketIndex"),
)
if mibBuilder.loadTexts:
    eqlStorageBucketEntry.setStatus("current")
_EqlStorageBucketIndex_Type = Unsigned32
_EqlStorageBucketIndex_Object = MibTableColumn
eqlStorageBucketIndex = _EqlStorageBucketIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 3, 1, 1),
    _EqlStorageBucketIndex_Type()
)
eqlStorageBucketIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlStorageBucketIndex.setStatus("current")
_EqlStorageBucketRowStatus_Type = RowStatus
_EqlStorageBucketRowStatus_Object = MibTableColumn
eqlStorageBucketRowStatus = _EqlStorageBucketRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 3, 1, 2),
    _EqlStorageBucketRowStatus_Type()
)
eqlStorageBucketRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageBucketRowStatus.setStatus("current")


class _EqlStorageBucketName_Type(UTFString):
    """Custom type eqlStorageBucketName based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlStorageBucketName_Type.__name__ = "UTFString"
_EqlStorageBucketName_Object = MibTableColumn
eqlStorageBucketName = _EqlStorageBucketName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 3, 1, 3),
    _EqlStorageBucketName_Type()
)
eqlStorageBucketName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageBucketName.setStatus("current")


class _EqlStorageBucketLookupName_Type(UTFString):
    """Custom type eqlStorageBucketLookupName based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlStorageBucketLookupName_Type.__name__ = "UTFString"
_EqlStorageBucketLookupName_Object = MibTableColumn
eqlStorageBucketLookupName = _EqlStorageBucketLookupName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 3, 1, 4),
    _EqlStorageBucketLookupName_Type()
)
eqlStorageBucketLookupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageBucketLookupName.setStatus("current")


class _EqlStorageBucketUuid_Type(OctetString):
    """Custom type eqlStorageBucketUuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlStorageBucketUuid_Type.__name__ = "OctetString"
_EqlStorageBucketUuid_Object = MibTableColumn
eqlStorageBucketUuid = _EqlStorageBucketUuid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 3, 1, 5),
    _EqlStorageBucketUuid_Type()
)
eqlStorageBucketUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageBucketUuid.setStatus("current")
_EqlStorageBucketPhysicalSize_Type = Unsigned64
_EqlStorageBucketPhysicalSize_Object = MibTableColumn
eqlStorageBucketPhysicalSize = _EqlStorageBucketPhysicalSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 3, 1, 6),
    _EqlStorageBucketPhysicalSize_Type()
)
eqlStorageBucketPhysicalSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageBucketPhysicalSize.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageBucketPhysicalSize.setUnits("MB")


class _EqlStorageBucketThinProvision_Type(TruthValue):
    """Custom type eqlStorageBucketThinProvision based on TruthValue"""


_EqlStorageBucketThinProvision_Object = MibTableColumn
eqlStorageBucketThinProvision = _EqlStorageBucketThinProvision_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 3, 1, 7),
    _EqlStorageBucketThinProvision_Type()
)
eqlStorageBucketThinProvision.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageBucketThinProvision.setStatus("current")


class _EqlStorageBucketThinMinReserve_Type(Unsigned32):
    """Custom type eqlStorageBucketThinMinReserve based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EqlStorageBucketThinMinReserve_Type.__name__ = "Unsigned32"
_EqlStorageBucketThinMinReserve_Object = MibTableColumn
eqlStorageBucketThinMinReserve = _EqlStorageBucketThinMinReserve_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 3, 1, 8),
    _EqlStorageBucketThinMinReserve_Type()
)
eqlStorageBucketThinMinReserve.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageBucketThinMinReserve.setStatus("current")


class _EqlStorageBucketThinMaxGrow_Type(Unsigned32):
    """Custom type eqlStorageBucketThinMaxGrow based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_EqlStorageBucketThinMaxGrow_Type.__name__ = "Unsigned32"
_EqlStorageBucketThinMaxGrow_Object = MibTableColumn
eqlStorageBucketThinMaxGrow = _EqlStorageBucketThinMaxGrow_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 3, 1, 9),
    _EqlStorageBucketThinMaxGrow_Type()
)
eqlStorageBucketThinMaxGrow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageBucketThinMaxGrow.setStatus("current")


class _EqlStorageBucketFreeWarnPercentage_Type(Unsigned32):
    """Custom type eqlStorageBucketFreeWarnPercentage based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_EqlStorageBucketFreeWarnPercentage_Type.__name__ = "Unsigned32"
_EqlStorageBucketFreeWarnPercentage_Object = MibTableColumn
eqlStorageBucketFreeWarnPercentage = _EqlStorageBucketFreeWarnPercentage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 3, 1, 10),
    _EqlStorageBucketFreeWarnPercentage_Type()
)
eqlStorageBucketFreeWarnPercentage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageBucketFreeWarnPercentage.setStatus("current")
_EqlParentStorageContainerPointer_Type = EQL2PartRowPointerStr
_EqlParentStorageContainerPointer_Object = MibTableColumn
eqlParentStorageContainerPointer = _EqlParentStorageContainerPointer_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 3, 1, 11),
    _EqlParentStorageContainerPointer_Type()
)
eqlParentStorageContainerPointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlParentStorageContainerPointer.setStatus("current")
_EqlParentStoragePoolIndex_Type = Unsigned32
_EqlParentStoragePoolIndex_Object = MibTableColumn
eqlParentStoragePoolIndex = _EqlParentStoragePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 3, 1, 12),
    _EqlParentStoragePoolIndex_Type()
)
eqlParentStoragePoolIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlParentStoragePoolIndex.setStatus("current")
_EqlStorageBucketDynamicConfigTable_Object = MibTable
eqlStorageBucketDynamicConfigTable = _EqlStorageBucketDynamicConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 4)
)
if mibBuilder.loadTexts:
    eqlStorageBucketDynamicConfigTable.setStatus("current")
_EqlStorageBucketDynamicConfigEntry_Object = MibTableRow
eqlStorageBucketDynamicConfigEntry = _EqlStorageBucketDynamicConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 4, 1)
)
eqlStorageBucketDynamicConfigEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLSTORAGECONTAINER-MIB", "eqlStorageBucketIndex"),
)
if mibBuilder.loadTexts:
    eqlStorageBucketDynamicConfigEntry.setStatus("current")
_EqlStorageBucketDynamicReservePages_Type = Counter64
_EqlStorageBucketDynamicReservePages_Object = MibTableColumn
eqlStorageBucketDynamicReservePages = _EqlStorageBucketDynamicReservePages_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 4, 1, 1),
    _EqlStorageBucketDynamicReservePages_Type()
)
eqlStorageBucketDynamicReservePages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageBucketDynamicReservePages.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageBucketDynamicReservePages.setUnits("pages")
_EqlStorageBucketFreeWarnInUsePageCount_Type = Counter64
_EqlStorageBucketFreeWarnInUsePageCount_Object = MibTableColumn
eqlStorageBucketFreeWarnInUsePageCount = _EqlStorageBucketFreeWarnInUsePageCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 4, 1, 2),
    _EqlStorageBucketFreeWarnInUsePageCount_Type()
)
eqlStorageBucketFreeWarnInUsePageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageBucketFreeWarnInUsePageCount.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageBucketFreeWarnInUsePageCount.setUnits("pages")
_EqlStorageBucketMaxResvInUsePageCount_Type = Counter64
_EqlStorageBucketMaxResvInUsePageCount_Object = MibTableColumn
eqlStorageBucketMaxResvInUsePageCount = _EqlStorageBucketMaxResvInUsePageCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 4, 1, 3),
    _EqlStorageBucketMaxResvInUsePageCount_Type()
)
eqlStorageBucketMaxResvInUsePageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageBucketMaxResvInUsePageCount.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageBucketMaxResvInUsePageCount.setUnits("pages")
_EqlStorageBucketFreeWarnThresholdPageCount_Type = Counter64
_EqlStorageBucketFreeWarnThresholdPageCount_Object = MibTableColumn
eqlStorageBucketFreeWarnThresholdPageCount = _EqlStorageBucketFreeWarnThresholdPageCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 4, 1, 4),
    _EqlStorageBucketFreeWarnThresholdPageCount_Type()
)
eqlStorageBucketFreeWarnThresholdPageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageBucketFreeWarnThresholdPageCount.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageBucketFreeWarnThresholdPageCount.setUnits("pages")
_EqlStorageBucketStatisticsTable_Object = MibTable
eqlStorageBucketStatisticsTable = _EqlStorageBucketStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 5)
)
if mibBuilder.loadTexts:
    eqlStorageBucketStatisticsTable.setStatus("current")
_EqlStorageBucketStatisticsEntry_Object = MibTableRow
eqlStorageBucketStatisticsEntry = _EqlStorageBucketStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 5, 1)
)
if mibBuilder.loadTexts:
    eqlStorageBucketStatisticsEntry.setStatus("current")
_EqlStorageBucketStatisticsPhysicalUsed_Type = Unsigned64
_EqlStorageBucketStatisticsPhysicalUsed_Object = MibTableColumn
eqlStorageBucketStatisticsPhysicalUsed = _EqlStorageBucketStatisticsPhysicalUsed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 5, 1, 1),
    _EqlStorageBucketStatisticsPhysicalUsed_Type()
)
eqlStorageBucketStatisticsPhysicalUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageBucketStatisticsPhysicalUsed.setStatus("current")
_EqlStorageBucketStatisticsPhysicalFree_Type = Unsigned64
_EqlStorageBucketStatisticsPhysicalFree_Object = MibTableColumn
eqlStorageBucketStatisticsPhysicalFree = _EqlStorageBucketStatisticsPhysicalFree_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 5, 1, 2),
    _EqlStorageBucketStatisticsPhysicalFree_Type()
)
eqlStorageBucketStatisticsPhysicalFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageBucketStatisticsPhysicalFree.setStatus("current")
_EqlStorageBucketStatisticsThinProvFree_Type = Unsigned64
_EqlStorageBucketStatisticsThinProvFree_Object = MibTableColumn
eqlStorageBucketStatisticsThinProvFree = _EqlStorageBucketStatisticsThinProvFree_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 5, 1, 3),
    _EqlStorageBucketStatisticsThinProvFree_Type()
)
eqlStorageBucketStatisticsThinProvFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageBucketStatisticsThinProvFree.setStatus("current")
_EqlStorageBucketStatisticsVvolsBound_Type = Counter32
_EqlStorageBucketStatisticsVvolsBound_Object = MibTableColumn
eqlStorageBucketStatisticsVvolsBound = _EqlStorageBucketStatisticsVvolsBound_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 5, 1, 4),
    _EqlStorageBucketStatisticsVvolsBound_Type()
)
eqlStorageBucketStatisticsVvolsBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageBucketStatisticsVvolsBound.setStatus("current")
_EqlStorageBucketStatisticsSVCount_Type = Counter32
_EqlStorageBucketStatisticsSVCount_Object = MibTableColumn
eqlStorageBucketStatisticsSVCount = _EqlStorageBucketStatisticsSVCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 5, 1, 5),
    _EqlStorageBucketStatisticsSVCount_Type()
)
eqlStorageBucketStatisticsSVCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageBucketStatisticsSVCount.setStatus("current")
_EqlStorageBucketStatisticsSVSCount_Type = Counter32
_EqlStorageBucketStatisticsSVSCount_Object = MibTableColumn
eqlStorageBucketStatisticsSVSCount = _EqlStorageBucketStatisticsSVSCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 5, 1, 6),
    _EqlStorageBucketStatisticsSVSCount_Type()
)
eqlStorageBucketStatisticsSVSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageBucketStatisticsSVSCount.setStatus("current")
_EqlStorageBucketStatisticsVvolsOnline_Type = Counter32
_EqlStorageBucketStatisticsVvolsOnline_Object = MibTableColumn
eqlStorageBucketStatisticsVvolsOnline = _EqlStorageBucketStatisticsVvolsOnline_Object(
    (1, 3, 6, 1, 4, 1, 12740, 25, 1, 5, 1, 7),
    _EqlStorageBucketStatisticsVvolsOnline_Type()
)
eqlStorageBucketStatisticsVvolsOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageBucketStatisticsVvolsOnline.setStatus("current")
_EqlStorageContainerNotifications_ObjectIdentity = ObjectIdentity
eqlStorageContainerNotifications = _EqlStorageContainerNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 25, 2)
)
_EqlStorageContainerConformance_ObjectIdentity = ObjectIdentity
eqlStorageContainerConformance = _EqlStorageContainerConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 25, 3)
)
eqlStorageContainerEntry.registerAugmentions(
    ("EQLSTORAGECONTAINER-MIB",
     "eqlStorageContainerStatisticsEntry")
)
eqlStorageContainerStatisticsEntry.setIndexNames(*eqlStorageContainerEntry.getIndexNames())
eqlStorageBucketEntry.registerAugmentions(
    ("EQLSTORAGECONTAINER-MIB",
     "eqlStorageBucketStatisticsEntry")
)
eqlStorageBucketStatisticsEntry.setIndexNames(*eqlStorageBucketEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQLSTORAGECONTAINER-MIB",
    **{"Unsigned64": Unsigned64,
       "eqlStorageContainerModule": eqlStorageContainerModule,
       "eqlStorageContainerObjects": eqlStorageContainerObjects,
       "eqlStorageContainerTable": eqlStorageContainerTable,
       "eqlStorageContainerEntry": eqlStorageContainerEntry,
       "eqlStorageContainerIndex": eqlStorageContainerIndex,
       "eqlStorageContainerRowStatus": eqlStorageContainerRowStatus,
       "eqlStorageContainerUuid": eqlStorageContainerUuid,
       "eqlStorageContainerName": eqlStorageContainerName,
       "eqlStorageContainerLookupName": eqlStorageContainerLookupName,
       "eqlStorageContainerDescription": eqlStorageContainerDescription,
       "eqlStorageContainerLogicalLimit": eqlStorageContainerLogicalLimit,
       "eqlStorageContainerStatisticsTable": eqlStorageContainerStatisticsTable,
       "eqlStorageContainerStatisticsEntry": eqlStorageContainerStatisticsEntry,
       "eqlStorageContainerStatisticsLogicalUsed": eqlStorageContainerStatisticsLogicalUsed,
       "eqlStorageContainerStatisticsLogicalFree": eqlStorageContainerStatisticsLogicalFree,
       "eqlStorageContainerStatisticsPhysicalUsed": eqlStorageContainerStatisticsPhysicalUsed,
       "eqlStorageContainerStatisticsPhysicalFree": eqlStorageContainerStatisticsPhysicalFree,
       "eqlStorageContainerStatisticsThinProvFree": eqlStorageContainerStatisticsThinProvFree,
       "eqlStorageContainerStatisticsVvolsBound": eqlStorageContainerStatisticsVvolsBound,
       "eqlStorageContainerStatisticsSVCount": eqlStorageContainerStatisticsSVCount,
       "eqlStorageContainerStatisticsSVSCount": eqlStorageContainerStatisticsSVSCount,
       "eqlStorageContainerStatisticsThinProvisioned": eqlStorageContainerStatisticsThinProvisioned,
       "eqlStorageContainerStatisticsVvolsOnline": eqlStorageContainerStatisticsVvolsOnline,
       "eqlStorageBucketTable": eqlStorageBucketTable,
       "eqlStorageBucketEntry": eqlStorageBucketEntry,
       "eqlStorageBucketIndex": eqlStorageBucketIndex,
       "eqlStorageBucketRowStatus": eqlStorageBucketRowStatus,
       "eqlStorageBucketName": eqlStorageBucketName,
       "eqlStorageBucketLookupName": eqlStorageBucketLookupName,
       "eqlStorageBucketUuid": eqlStorageBucketUuid,
       "eqlStorageBucketPhysicalSize": eqlStorageBucketPhysicalSize,
       "eqlStorageBucketThinProvision": eqlStorageBucketThinProvision,
       "eqlStorageBucketThinMinReserve": eqlStorageBucketThinMinReserve,
       "eqlStorageBucketThinMaxGrow": eqlStorageBucketThinMaxGrow,
       "eqlStorageBucketFreeWarnPercentage": eqlStorageBucketFreeWarnPercentage,
       "eqlParentStorageContainerPointer": eqlParentStorageContainerPointer,
       "eqlParentStoragePoolIndex": eqlParentStoragePoolIndex,
       "eqlStorageBucketDynamicConfigTable": eqlStorageBucketDynamicConfigTable,
       "eqlStorageBucketDynamicConfigEntry": eqlStorageBucketDynamicConfigEntry,
       "eqlStorageBucketDynamicReservePages": eqlStorageBucketDynamicReservePages,
       "eqlStorageBucketFreeWarnInUsePageCount": eqlStorageBucketFreeWarnInUsePageCount,
       "eqlStorageBucketMaxResvInUsePageCount": eqlStorageBucketMaxResvInUsePageCount,
       "eqlStorageBucketFreeWarnThresholdPageCount": eqlStorageBucketFreeWarnThresholdPageCount,
       "eqlStorageBucketStatisticsTable": eqlStorageBucketStatisticsTable,
       "eqlStorageBucketStatisticsEntry": eqlStorageBucketStatisticsEntry,
       "eqlStorageBucketStatisticsPhysicalUsed": eqlStorageBucketStatisticsPhysicalUsed,
       "eqlStorageBucketStatisticsPhysicalFree": eqlStorageBucketStatisticsPhysicalFree,
       "eqlStorageBucketStatisticsThinProvFree": eqlStorageBucketStatisticsThinProvFree,
       "eqlStorageBucketStatisticsVvolsBound": eqlStorageBucketStatisticsVvolsBound,
       "eqlStorageBucketStatisticsSVCount": eqlStorageBucketStatisticsSVCount,
       "eqlStorageBucketStatisticsSVSCount": eqlStorageBucketStatisticsSVSCount,
       "eqlStorageBucketStatisticsVvolsOnline": eqlStorageBucketStatisticsVvolsOnline,
       "eqlStorageContainerNotifications": eqlStorageContainerNotifications,
       "eqlStorageContainerConformance": eqlStorageContainerConformance}
)
