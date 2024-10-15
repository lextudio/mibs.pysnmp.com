# SNMP MIB module (EQLSTORAGEPOOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQLSTORAGEPOOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:58 2024
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

(UTFString,
 eqlGroupId,
 eqlLdapLoginAccessName,
 eqlLdapLoginAccessType,
 eqlStorageGroupAdminAccountIndex,
 eqlStorageGroupAdminAccountName) = mibBuilder.importSymbols(
    "EQLGROUP-MIB",
    "UTFString",
    "eqlGroupId",
    "eqlLdapLoginAccessName",
    "eqlLdapLoginAccessType",
    "eqlStorageGroupAdminAccountIndex",
    "eqlStorageGroupAdminAccountName")

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

eqlStoragePoolModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 16)
)
eqlStoragePoolModule.setRevisions(
        ("2005-03-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SiteIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class SiteIndexOrZero(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class Unsigned64(Counter64, TextualConvention):
    status = "current"


class PoolQuotaType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("size", 1))
    )



class StatusEnabledDefault(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )



# MIB Managed Objects in the order of their OIDs

_EqlStoragePoolObjects_ObjectIdentity = ObjectIdentity
eqlStoragePoolObjects = _EqlStoragePoolObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1)
)
_EqlStoragePoolTable_Object = MibTable
eqlStoragePoolTable = _EqlStoragePoolTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 1)
)
if mibBuilder.loadTexts:
    eqlStoragePoolTable.setStatus("current")
_EqlStoragePoolEntry_Object = MibTableRow
eqlStoragePoolEntry = _EqlStoragePoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1)
)
eqlStoragePoolEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex"),
)
if mibBuilder.loadTexts:
    eqlStoragePoolEntry.setStatus("current")
_EqlStoragePoolIndex_Type = Unsigned32
_EqlStoragePoolIndex_Object = MibTableColumn
eqlStoragePoolIndex = _EqlStoragePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 1),
    _EqlStoragePoolIndex_Type()
)
eqlStoragePoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlStoragePoolIndex.setStatus("current")
_EqlStoragePoolRowStatus_Type = RowStatus
_EqlStoragePoolRowStatus_Object = MibTableColumn
eqlStoragePoolRowStatus = _EqlStoragePoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 2),
    _EqlStoragePoolRowStatus_Type()
)
eqlStoragePoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStoragePoolRowStatus.setStatus("current")


class _EqlStoragePoolName_Type(UTFString):
    """Custom type eqlStoragePoolName based on UTFString"""
    defaultValue = OctetString("default")

    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlStoragePoolName_Type.__name__ = "UTFString"
_EqlStoragePoolName_Object = MibTableColumn
eqlStoragePoolName = _EqlStoragePoolName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 3),
    _EqlStoragePoolName_Type()
)
eqlStoragePoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStoragePoolName.setStatus("current")


class _EqlStoragePoolDefaultFlag_Type(TruthValue):
    """Custom type eqlStoragePoolDefaultFlag based on TruthValue"""


_EqlStoragePoolDefaultFlag_Object = MibTableColumn
eqlStoragePoolDefaultFlag = _EqlStoragePoolDefaultFlag_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 4),
    _EqlStoragePoolDefaultFlag_Type()
)
eqlStoragePoolDefaultFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStoragePoolDefaultFlag.setStatus("current")


class _EqlStoragePoolRAIDConfigWaitFlag_Type(TruthValue):
    """Custom type eqlStoragePoolRAIDConfigWaitFlag based on TruthValue"""


_EqlStoragePoolRAIDConfigWaitFlag_Object = MibTableColumn
eqlStoragePoolRAIDConfigWaitFlag = _EqlStoragePoolRAIDConfigWaitFlag_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 5),
    _EqlStoragePoolRAIDConfigWaitFlag_Type()
)
eqlStoragePoolRAIDConfigWaitFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlStoragePoolRAIDConfigWaitFlag.setStatus("current")
_EqlStoragePoolShouldEvalMask_Type = Unsigned32
_EqlStoragePoolShouldEvalMask_Object = MibTableColumn
eqlStoragePoolShouldEvalMask = _EqlStoragePoolShouldEvalMask_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 6),
    _EqlStoragePoolShouldEvalMask_Type()
)
eqlStoragePoolShouldEvalMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolShouldEvalMask.setStatus("current")
_EqlStoragePoolLastBalance_Type = Unsigned32
_EqlStoragePoolLastBalance_Object = MibTableColumn
eqlStoragePoolLastBalance = _EqlStoragePoolLastBalance_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 7),
    _EqlStoragePoolLastBalance_Type()
)
eqlStoragePoolLastBalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolLastBalance.setStatus("current")


class _EqlStoragePoolDescription_Type(DisplayString):
    """Custom type eqlStoragePoolDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EqlStoragePoolDescription_Type.__name__ = "DisplayString"
_EqlStoragePoolDescription_Object = MibTableColumn
eqlStoragePoolDescription = _EqlStoragePoolDescription_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 8),
    _EqlStoragePoolDescription_Type()
)
eqlStoragePoolDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlStoragePoolDescription.setStatus("current")
_EqlStoragePoolLeadMemberId_Type = Unsigned32
_EqlStoragePoolLeadMemberId_Object = MibTableColumn
eqlStoragePoolLeadMemberId = _EqlStoragePoolLeadMemberId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 9),
    _EqlStoragePoolLeadMemberId_Type()
)
eqlStoragePoolLeadMemberId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlStoragePoolLeadMemberId.setStatus("deprecated")


class _EqlStoragePoolUUID_Type(OctetString):
    """Custom type eqlStoragePoolUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlStoragePoolUUID_Type.__name__ = "OctetString"
_EqlStoragePoolUUID_Object = MibTableColumn
eqlStoragePoolUUID = _EqlStoragePoolUUID_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 10),
    _EqlStoragePoolUUID_Type()
)
eqlStoragePoolUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolUUID.setStatus("current")
_EqlStoragePoolExecMergeTo_Type = Unsigned32
_EqlStoragePoolExecMergeTo_Object = MibTableColumn
eqlStoragePoolExecMergeTo = _EqlStoragePoolExecMergeTo_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 11),
    _EqlStoragePoolExecMergeTo_Type()
)
eqlStoragePoolExecMergeTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlStoragePoolExecMergeTo.setStatus("current")


class _EqlStoragePoolBorrow_Type(StatusEnabledDefault):
    """Custom type eqlStoragePoolBorrow based on StatusEnabledDefault"""


_EqlStoragePoolBorrow_Object = MibTableColumn
eqlStoragePoolBorrow = _EqlStoragePoolBorrow_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 12),
    _EqlStoragePoolBorrow_Type()
)
eqlStoragePoolBorrow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlStoragePoolBorrow.setStatus("current")


class _EqlStoragePoolSnapTrimThreshold_Type(Unsigned32):
    """Custom type eqlStoragePoolSnapTrimThreshold based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EqlStoragePoolSnapTrimThreshold_Type.__name__ = "Unsigned32"
_EqlStoragePoolSnapTrimThreshold_Object = MibTableColumn
eqlStoragePoolSnapTrimThreshold = _EqlStoragePoolSnapTrimThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 13),
    _EqlStoragePoolSnapTrimThreshold_Type()
)
eqlStoragePoolSnapTrimThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlStoragePoolSnapTrimThreshold.setStatus("current")
if mibBuilder.loadTexts:
    eqlStoragePoolSnapTrimThreshold.setUnits("%")


class _EqlStoragePoolSnapTrimBuffer_Type(Counter64):
    """Custom type eqlStoragePoolSnapTrimBuffer based on Counter64"""
    defaultValue = 600


_EqlStoragePoolSnapTrimBuffer_Object = MibTableColumn
eqlStoragePoolSnapTrimBuffer = _EqlStoragePoolSnapTrimBuffer_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 14),
    _EqlStoragePoolSnapTrimBuffer_Type()
)
eqlStoragePoolSnapTrimBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlStoragePoolSnapTrimBuffer.setStatus("current")
if mibBuilder.loadTexts:
    eqlStoragePoolSnapTrimBuffer.setUnits("MB")


class _EqlStoragePoolSnapTrimmerHWMLifeTime_Type(Integer32):
    """Custom type eqlStoragePoolSnapTrimmerHWMLifeTime based on Integer32"""
    defaultValue = 864000


_EqlStoragePoolSnapTrimmerHWMLifeTime_Object = MibTableColumn
eqlStoragePoolSnapTrimmerHWMLifeTime = _EqlStoragePoolSnapTrimmerHWMLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 15),
    _EqlStoragePoolSnapTrimmerHWMLifeTime_Type()
)
eqlStoragePoolSnapTrimmerHWMLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlStoragePoolSnapTrimmerHWMLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    eqlStoragePoolSnapTrimmerHWMLifeTime.setUnits("secs")


class _EqlStoragePoolSnapTrimmerBorrowInfoRefreshInterval_Type(Integer32):
    """Custom type eqlStoragePoolSnapTrimmerBorrowInfoRefreshInterval based on Integer32"""
    defaultValue = 60


_EqlStoragePoolSnapTrimmerBorrowInfoRefreshInterval_Object = MibTableColumn
eqlStoragePoolSnapTrimmerBorrowInfoRefreshInterval = _EqlStoragePoolSnapTrimmerBorrowInfoRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 16),
    _EqlStoragePoolSnapTrimmerBorrowInfoRefreshInterval_Type()
)
eqlStoragePoolSnapTrimmerBorrowInfoRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlStoragePoolSnapTrimmerBorrowInfoRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    eqlStoragePoolSnapTrimmerBorrowInfoRefreshInterval.setUnits("secs")


class _EqlStoragePoolDefaultCompressionStrategy_Type(Integer32):
    """Custom type eqlStoragePoolDefaultCompressionStrategy based on Integer32"""
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
        *(("always", 1),
          ("automatic", 0),
          ("never", 2))
    )


_EqlStoragePoolDefaultCompressionStrategy_Type.__name__ = "Integer32"
_EqlStoragePoolDefaultCompressionStrategy_Object = MibTableColumn
eqlStoragePoolDefaultCompressionStrategy = _EqlStoragePoolDefaultCompressionStrategy_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 17),
    _EqlStoragePoolDefaultCompressionStrategy_Type()
)
eqlStoragePoolDefaultCompressionStrategy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStoragePoolDefaultCompressionStrategy.setStatus("current")


class _EqlStoragePoolDefaultCompressionMinSnapDelay_Type(Integer32):
    """Custom type eqlStoragePoolDefaultCompressionMinSnapDelay based on Integer32"""
    defaultValue = 10


_EqlStoragePoolDefaultCompressionMinSnapDelay_Object = MibTableColumn
eqlStoragePoolDefaultCompressionMinSnapDelay = _EqlStoragePoolDefaultCompressionMinSnapDelay_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 18),
    _EqlStoragePoolDefaultCompressionMinSnapDelay_Type()
)
eqlStoragePoolDefaultCompressionMinSnapDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStoragePoolDefaultCompressionMinSnapDelay.setStatus("current")
if mibBuilder.loadTexts:
    eqlStoragePoolDefaultCompressionMinSnapDelay.setUnits("minutes")


class _EqlStoragePoolDefaultCompressionMinSnapAge_Type(Integer32):
    """Custom type eqlStoragePoolDefaultCompressionMinSnapAge based on Integer32"""
    defaultValue = 1380


_EqlStoragePoolDefaultCompressionMinSnapAge_Object = MibTableColumn
eqlStoragePoolDefaultCompressionMinSnapAge = _EqlStoragePoolDefaultCompressionMinSnapAge_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 19),
    _EqlStoragePoolDefaultCompressionMinSnapAge_Type()
)
eqlStoragePoolDefaultCompressionMinSnapAge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStoragePoolDefaultCompressionMinSnapAge.setStatus("current")
if mibBuilder.loadTexts:
    eqlStoragePoolDefaultCompressionMinSnapAge.setUnits("minutes")


class _EqlStoragePoolSnapMemberTrimThresholdAmount_Type(Counter64):
    """Custom type eqlStoragePoolSnapMemberTrimThresholdAmount based on Counter64"""
    defaultValue = 204800


_EqlStoragePoolSnapMemberTrimThresholdAmount_Object = MibTableColumn
eqlStoragePoolSnapMemberTrimThresholdAmount = _EqlStoragePoolSnapMemberTrimThresholdAmount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 20),
    _EqlStoragePoolSnapMemberTrimThresholdAmount_Type()
)
eqlStoragePoolSnapMemberTrimThresholdAmount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlStoragePoolSnapMemberTrimThresholdAmount.setStatus("current")
if mibBuilder.loadTexts:
    eqlStoragePoolSnapMemberTrimThresholdAmount.setUnits("MB")


class _EqlStoragePoolSnapTrimRecheckTimer_Type(Unsigned32):
    """Custom type eqlStoragePoolSnapTrimRecheckTimer based on Unsigned32"""
    defaultValue = 20


_EqlStoragePoolSnapTrimRecheckTimer_Object = MibTableColumn
eqlStoragePoolSnapTrimRecheckTimer = _EqlStoragePoolSnapTrimRecheckTimer_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 1, 1, 21),
    _EqlStoragePoolSnapTrimRecheckTimer_Type()
)
eqlStoragePoolSnapTrimRecheckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlStoragePoolSnapTrimRecheckTimer.setStatus("current")
if mibBuilder.loadTexts:
    eqlStoragePoolSnapTrimRecheckTimer.setUnits("secs")
_EqlStoragePoolStatsTable_Object = MibTable
eqlStoragePoolStatsTable = _EqlStoragePoolStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2)
)
if mibBuilder.loadTexts:
    eqlStoragePoolStatsTable.setStatus("current")
_EqlStoragePoolStatsEntry_Object = MibTableRow
eqlStoragePoolStatsEntry = _EqlStoragePoolStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eqlStoragePoolStatsEntry.setStatus("current")
_EqlStoragePoolStatsSpace_Type = Counter64
_EqlStoragePoolStatsSpace_Object = MibTableColumn
eqlStoragePoolStatsSpace = _EqlStoragePoolStatsSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 1),
    _EqlStoragePoolStatsSpace_Type()
)
eqlStoragePoolStatsSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsSpace.setStatus("current")
_EqlStoragePoolStatsSpaceUsed_Type = Counter64
_EqlStoragePoolStatsSpaceUsed_Object = MibTableColumn
eqlStoragePoolStatsSpaceUsed = _EqlStoragePoolStatsSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 2),
    _EqlStoragePoolStatsSpaceUsed_Type()
)
eqlStoragePoolStatsSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsSpaceUsed.setStatus("current")
_EqlStoragePoolStatsFreeSpace_Type = Counter64
_EqlStoragePoolStatsFreeSpace_Object = MibTableColumn
eqlStoragePoolStatsFreeSpace = _EqlStoragePoolStatsFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 3),
    _EqlStoragePoolStatsFreeSpace_Type()
)
eqlStoragePoolStatsFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsFreeSpace.setStatus("current")
_EqlStoragePoolStatsReplicationSpace_Type = Counter64
_EqlStoragePoolStatsReplicationSpace_Object = MibTableColumn
eqlStoragePoolStatsReplicationSpace = _EqlStoragePoolStatsReplicationSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 4),
    _EqlStoragePoolStatsReplicationSpace_Type()
)
eqlStoragePoolStatsReplicationSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsReplicationSpace.setStatus("current")
_EqlStoragePoolStatsReplicationSpaceUsed_Type = Counter64
_EqlStoragePoolStatsReplicationSpaceUsed_Object = MibTableColumn
eqlStoragePoolStatsReplicationSpaceUsed = _EqlStoragePoolStatsReplicationSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 5),
    _EqlStoragePoolStatsReplicationSpaceUsed_Type()
)
eqlStoragePoolStatsReplicationSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsReplicationSpaceUsed.setStatus("current")
_EqlStoragePoolStatsReplicationFreeSpace_Type = Counter64
_EqlStoragePoolStatsReplicationFreeSpace_Object = MibTableColumn
eqlStoragePoolStatsReplicationFreeSpace = _EqlStoragePoolStatsReplicationFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 6),
    _EqlStoragePoolStatsReplicationFreeSpace_Type()
)
eqlStoragePoolStatsReplicationFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsReplicationFreeSpace.setStatus("current")
_EqlStoragePoolStatsMemberNumOnline_Type = Integer32
_EqlStoragePoolStatsMemberNumOnline_Object = MibTableColumn
eqlStoragePoolStatsMemberNumOnline = _EqlStoragePoolStatsMemberNumOnline_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 7),
    _EqlStoragePoolStatsMemberNumOnline_Type()
)
eqlStoragePoolStatsMemberNumOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsMemberNumOnline.setStatus("current")
_EqlStoragePoolStatsMemberCount_Type = Integer32
_EqlStoragePoolStatsMemberCount_Object = MibTableColumn
eqlStoragePoolStatsMemberCount = _EqlStoragePoolStatsMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 8),
    _EqlStoragePoolStatsMemberCount_Type()
)
eqlStoragePoolStatsMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsMemberCount.setStatus("current")
_EqlStoragePoolStatsSnapshotReserved_Type = Counter64
_EqlStoragePoolStatsSnapshotReserved_Object = MibTableColumn
eqlStoragePoolStatsSnapshotReserved = _EqlStoragePoolStatsSnapshotReserved_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 9),
    _EqlStoragePoolStatsSnapshotReserved_Type()
)
eqlStoragePoolStatsSnapshotReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsSnapshotReserved.setStatus("current")
_EqlStoragePoolStatsSnapshotUsed_Type = Counter64
_EqlStoragePoolStatsSnapshotUsed_Object = MibTableColumn
eqlStoragePoolStatsSnapshotUsed = _EqlStoragePoolStatsSnapshotUsed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 10),
    _EqlStoragePoolStatsSnapshotUsed_Type()
)
eqlStoragePoolStatsSnapshotUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsSnapshotUsed.setStatus("current")
_EqlStoragePoolStatsSnapshotNumInUse_Type = Integer32
_EqlStoragePoolStatsSnapshotNumInUse_Object = MibTableColumn
eqlStoragePoolStatsSnapshotNumInUse = _EqlStoragePoolStatsSnapshotNumInUse_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 11),
    _EqlStoragePoolStatsSnapshotNumInUse_Type()
)
eqlStoragePoolStatsSnapshotNumInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsSnapshotNumInUse.setStatus("current")
_EqlStoragePoolStatsSnapshotNumOnline_Type = Integer32
_EqlStoragePoolStatsSnapshotNumOnline_Object = MibTableColumn
eqlStoragePoolStatsSnapshotNumOnline = _EqlStoragePoolStatsSnapshotNumOnline_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 12),
    _EqlStoragePoolStatsSnapshotNumOnline_Type()
)
eqlStoragePoolStatsSnapshotNumOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsSnapshotNumOnline.setStatus("current")
_EqlStoragePoolStatsSnapshotCount_Type = Integer32
_EqlStoragePoolStatsSnapshotCount_Object = MibTableColumn
eqlStoragePoolStatsSnapshotCount = _EqlStoragePoolStatsSnapshotCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 13),
    _EqlStoragePoolStatsSnapshotCount_Type()
)
eqlStoragePoolStatsSnapshotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsSnapshotCount.setStatus("current")
_EqlStoragePoolStatsVolumeNumInUse_Type = Integer32
_EqlStoragePoolStatsVolumeNumInUse_Object = MibTableColumn
eqlStoragePoolStatsVolumeNumInUse = _EqlStoragePoolStatsVolumeNumInUse_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 14),
    _EqlStoragePoolStatsVolumeNumInUse_Type()
)
eqlStoragePoolStatsVolumeNumInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsVolumeNumInUse.setStatus("current")
_EqlStoragePoolStatsVolumeNumOnline_Type = Integer32
_EqlStoragePoolStatsVolumeNumOnline_Object = MibTableColumn
eqlStoragePoolStatsVolumeNumOnline = _EqlStoragePoolStatsVolumeNumOnline_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 15),
    _EqlStoragePoolStatsVolumeNumOnline_Type()
)
eqlStoragePoolStatsVolumeNumOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsVolumeNumOnline.setStatus("current")
_EqlStoragePoolStatsVolumeCount_Type = Integer32
_EqlStoragePoolStatsVolumeCount_Object = MibTableColumn
eqlStoragePoolStatsVolumeCount = _EqlStoragePoolStatsVolumeCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 16),
    _EqlStoragePoolStatsVolumeCount_Type()
)
eqlStoragePoolStatsVolumeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsVolumeCount.setStatus("current")
_EqlStoragePoolStatsDelegatedSpace_Type = Counter64
_EqlStoragePoolStatsDelegatedSpace_Object = MibTableColumn
eqlStoragePoolStatsDelegatedSpace = _EqlStoragePoolStatsDelegatedSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 17),
    _EqlStoragePoolStatsDelegatedSpace_Type()
)
eqlStoragePoolStatsDelegatedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsDelegatedSpace.setStatus("current")
_EqlStoragePoolStatsDelegatedSpaceUsed_Type = Counter64
_EqlStoragePoolStatsDelegatedSpaceUsed_Object = MibTableColumn
eqlStoragePoolStatsDelegatedSpaceUsed = _EqlStoragePoolStatsDelegatedSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 18),
    _EqlStoragePoolStatsDelegatedSpaceUsed_Type()
)
eqlStoragePoolStatsDelegatedSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsDelegatedSpaceUsed.setStatus("current")
_EqlStoragePoolStatsMembersInUse_Type = Integer32
_EqlStoragePoolStatsMembersInUse_Object = MibTableColumn
eqlStoragePoolStatsMembersInUse = _EqlStoragePoolStatsMembersInUse_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 19),
    _EqlStoragePoolStatsMembersInUse_Type()
)
eqlStoragePoolStatsMembersInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsMembersInUse.setStatus("current")
_EqlStoragePoolStatsVolumeSubscribed_Type = Counter64
_EqlStoragePoolStatsVolumeSubscribed_Object = MibTableColumn
eqlStoragePoolStatsVolumeSubscribed = _EqlStoragePoolStatsVolumeSubscribed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 20),
    _EqlStoragePoolStatsVolumeSubscribed_Type()
)
eqlStoragePoolStatsVolumeSubscribed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsVolumeSubscribed.setStatus("current")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsVolumeSubscribed.setUnits("MB")
_EqlStoragePoolStatsVolumeSpaceAllocated_Type = Counter64
_EqlStoragePoolStatsVolumeSpaceAllocated_Object = MibTableColumn
eqlStoragePoolStatsVolumeSpaceAllocated = _EqlStoragePoolStatsVolumeSpaceAllocated_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 21),
    _EqlStoragePoolStatsVolumeSpaceAllocated_Type()
)
eqlStoragePoolStatsVolumeSpaceAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsVolumeSpaceAllocated.setStatus("current")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsVolumeSpaceAllocated.setUnits("MB")
_EqlStoragePoolStatsFailbackSpace_Type = Counter64
_EqlStoragePoolStatsFailbackSpace_Object = MibTableColumn
eqlStoragePoolStatsFailbackSpace = _EqlStoragePoolStatsFailbackSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 22),
    _EqlStoragePoolStatsFailbackSpace_Type()
)
eqlStoragePoolStatsFailbackSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsFailbackSpace.setStatus("current")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsFailbackSpace.setUnits("MB")
_EqlStoragePoolStatsThinProvFreeSpace_Type = Counter64
_EqlStoragePoolStatsThinProvFreeSpace_Object = MibTableColumn
eqlStoragePoolStatsThinProvFreeSpace = _EqlStoragePoolStatsThinProvFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 23),
    _EqlStoragePoolStatsThinProvFreeSpace_Type()
)
eqlStoragePoolStatsThinProvFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsThinProvFreeSpace.setStatus("current")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsThinProvFreeSpace.setUnits("MB")
_EqlStoragePoolStatsConnectionCount_Type = Integer32
_EqlStoragePoolStatsConnectionCount_Object = MibTableColumn
eqlStoragePoolStatsConnectionCount = _EqlStoragePoolStatsConnectionCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 24),
    _EqlStoragePoolStatsConnectionCount_Type()
)
eqlStoragePoolStatsConnectionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsConnectionCount.setStatus("current")
_EqlStoragePoolStatsSnapshotResvFreeSpace_Type = Counter64
_EqlStoragePoolStatsSnapshotResvFreeSpace_Object = MibTableColumn
eqlStoragePoolStatsSnapshotResvFreeSpace = _EqlStoragePoolStatsSnapshotResvFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 25),
    _EqlStoragePoolStatsSnapshotResvFreeSpace_Type()
)
eqlStoragePoolStatsSnapshotResvFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsSnapshotResvFreeSpace.setStatus("current")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsSnapshotResvFreeSpace.setUnits("MB")
_EqlStoragePoolStatsVirtualVolumeNumInUse_Type = Integer32
_EqlStoragePoolStatsVirtualVolumeNumInUse_Object = MibTableColumn
eqlStoragePoolStatsVirtualVolumeNumInUse = _EqlStoragePoolStatsVirtualVolumeNumInUse_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 26),
    _EqlStoragePoolStatsVirtualVolumeNumInUse_Type()
)
eqlStoragePoolStatsVirtualVolumeNumInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsVirtualVolumeNumInUse.setStatus("current")
_EqlStoragePoolStatsVirtualVolumeNumOnline_Type = Integer32
_EqlStoragePoolStatsVirtualVolumeNumOnline_Object = MibTableColumn
eqlStoragePoolStatsVirtualVolumeNumOnline = _EqlStoragePoolStatsVirtualVolumeNumOnline_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 27),
    _EqlStoragePoolStatsVirtualVolumeNumOnline_Type()
)
eqlStoragePoolStatsVirtualVolumeNumOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsVirtualVolumeNumOnline.setStatus("current")
_EqlStoragePoolStatsSnapshotResvBorrowing_Type = Counter64
_EqlStoragePoolStatsSnapshotResvBorrowing_Object = MibTableColumn
eqlStoragePoolStatsSnapshotResvBorrowing = _EqlStoragePoolStatsSnapshotResvBorrowing_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 28),
    _EqlStoragePoolStatsSnapshotResvBorrowing_Type()
)
eqlStoragePoolStatsSnapshotResvBorrowing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsSnapshotResvBorrowing.setStatus("current")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsSnapshotResvBorrowing.setUnits("MB")
_EqlStoragePoolStatsFreeSpaceBorrowing_Type = Counter64
_EqlStoragePoolStatsFreeSpaceBorrowing_Object = MibTableColumn
eqlStoragePoolStatsFreeSpaceBorrowing = _EqlStoragePoolStatsFreeSpaceBorrowing_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 29),
    _EqlStoragePoolStatsFreeSpaceBorrowing_Type()
)
eqlStoragePoolStatsFreeSpaceBorrowing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsFreeSpaceBorrowing.setStatus("current")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsFreeSpaceBorrowing.setUnits("MB")
_EqlStoragePoolStatsAvailableForBorrowing_Type = Counter64
_EqlStoragePoolStatsAvailableForBorrowing_Object = MibTableColumn
eqlStoragePoolStatsAvailableForBorrowing = _EqlStoragePoolStatsAvailableForBorrowing_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 30),
    _EqlStoragePoolStatsAvailableForBorrowing_Type()
)
eqlStoragePoolStatsAvailableForBorrowing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsAvailableForBorrowing.setStatus("current")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsAvailableForBorrowing.setUnits("MB")
_EqlStoragePoolStatsRecoverableVolBorrowing_Type = Counter64
_EqlStoragePoolStatsRecoverableVolBorrowing_Object = MibTableColumn
eqlStoragePoolStatsRecoverableVolBorrowing = _EqlStoragePoolStatsRecoverableVolBorrowing_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 31),
    _EqlStoragePoolStatsRecoverableVolBorrowing_Type()
)
eqlStoragePoolStatsRecoverableVolBorrowing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsRecoverableVolBorrowing.setStatus("current")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsRecoverableVolBorrowing.setUnits("MB")
_EqlStoragePoolStatsActualFreeSpace_Type = Counter64
_EqlStoragePoolStatsActualFreeSpace_Object = MibTableColumn
eqlStoragePoolStatsActualFreeSpace = _EqlStoragePoolStatsActualFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 32),
    _EqlStoragePoolStatsActualFreeSpace_Type()
)
eqlStoragePoolStatsActualFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsActualFreeSpace.setStatus("current")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsActualFreeSpace.setUnits("MB")
_EqlStoragePoolStatsTotalSpaceBorrowing_Type = Counter64
_EqlStoragePoolStatsTotalSpaceBorrowing_Object = MibTableColumn
eqlStoragePoolStatsTotalSpaceBorrowing = _EqlStoragePoolStatsTotalSpaceBorrowing_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 33),
    _EqlStoragePoolStatsTotalSpaceBorrowing_Type()
)
eqlStoragePoolStatsTotalSpaceBorrowing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsTotalSpaceBorrowing.setStatus("current")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsTotalSpaceBorrowing.setUnits("MB")
_EqlStoragePoolStatsSnapShotBorrowing_Type = Counter64
_EqlStoragePoolStatsSnapShotBorrowing_Object = MibTableColumn
eqlStoragePoolStatsSnapShotBorrowing = _EqlStoragePoolStatsSnapShotBorrowing_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 34),
    _EqlStoragePoolStatsSnapShotBorrowing_Type()
)
eqlStoragePoolStatsSnapShotBorrowing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsSnapShotBorrowing.setStatus("current")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsSnapShotBorrowing.setUnits("MB")
_EqlStoragePoolStatsStorageContainerCount_Type = Integer32
_EqlStoragePoolStatsStorageContainerCount_Object = MibTableColumn
eqlStoragePoolStatsStorageContainerCount = _EqlStoragePoolStatsStorageContainerCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 35),
    _EqlStoragePoolStatsStorageContainerCount_Type()
)
eqlStoragePoolStatsStorageContainerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsStorageContainerCount.setStatus("current")
_EqlStoragePoolStatsStorageContainerSpaceReserved_Type = Counter64
_EqlStoragePoolStatsStorageContainerSpaceReserved_Object = MibTableColumn
eqlStoragePoolStatsStorageContainerSpaceReserved = _EqlStoragePoolStatsStorageContainerSpaceReserved_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 36),
    _EqlStoragePoolStatsStorageContainerSpaceReserved_Type()
)
eqlStoragePoolStatsStorageContainerSpaceReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsStorageContainerSpaceReserved.setStatus("current")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsStorageContainerSpaceReserved.setUnits("MB")
_EqlStoragePoolStatsCompressedSpaceUsed_Type = Counter64
_EqlStoragePoolStatsCompressedSpaceUsed_Object = MibTableColumn
eqlStoragePoolStatsCompressedSpaceUsed = _EqlStoragePoolStatsCompressedSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 37),
    _EqlStoragePoolStatsCompressedSpaceUsed_Type()
)
eqlStoragePoolStatsCompressedSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsCompressedSpaceUsed.setStatus("current")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsCompressedSpaceUsed.setUnits("MB")
_EqlStoragePoolStatsVirtualSpaceSize_Type = Counter64
_EqlStoragePoolStatsVirtualSpaceSize_Object = MibTableColumn
eqlStoragePoolStatsVirtualSpaceSize = _EqlStoragePoolStatsVirtualSpaceSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 38),
    _EqlStoragePoolStatsVirtualSpaceSize_Type()
)
eqlStoragePoolStatsVirtualSpaceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsVirtualSpaceSize.setStatus("current")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsVirtualSpaceSize.setUnits("MB")
_EqlStoragePoolStatsStorageContainerVolumeCount_Type = Integer32
_EqlStoragePoolStatsStorageContainerVolumeCount_Object = MibTableColumn
eqlStoragePoolStatsStorageContainerVolumeCount = _EqlStoragePoolStatsStorageContainerVolumeCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 39),
    _EqlStoragePoolStatsStorageContainerVolumeCount_Type()
)
eqlStoragePoolStatsStorageContainerVolumeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsStorageContainerVolumeCount.setStatus("current")
_EqlStoragePoolStatsStorageContainerSnapCount_Type = Integer32
_EqlStoragePoolStatsStorageContainerSnapCount_Object = MibTableColumn
eqlStoragePoolStatsStorageContainerSnapCount = _EqlStoragePoolStatsStorageContainerSnapCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 40),
    _EqlStoragePoolStatsStorageContainerSnapCount_Type()
)
eqlStoragePoolStatsStorageContainerSnapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsStorageContainerSnapCount.setStatus("current")
_EqlStoragePoolStatsStorageContainerVolumesOnline_Type = Integer32
_EqlStoragePoolStatsStorageContainerVolumesOnline_Object = MibTableColumn
eqlStoragePoolStatsStorageContainerVolumesOnline = _EqlStoragePoolStatsStorageContainerVolumesOnline_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 2, 1, 41),
    _EqlStoragePoolStatsStorageContainerVolumesOnline_Type()
)
eqlStoragePoolStatsStorageContainerVolumesOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolStatsStorageContainerVolumesOnline.setStatus("current")
_EqlStoragePoolAdminAccountTable_Object = MibTable
eqlStoragePoolAdminAccountTable = _EqlStoragePoolAdminAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 3)
)
if mibBuilder.loadTexts:
    eqlStoragePoolAdminAccountTable.setStatus("current")
_EqlStoragePoolAdminAccountEntry_Object = MibTableRow
eqlStoragePoolAdminAccountEntry = _EqlStoragePoolAdminAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 3, 1)
)
eqlStoragePoolAdminAccountEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex"),
    (0, "EQLGROUP-MIB", "eqlStorageGroupAdminAccountIndex"),
)
if mibBuilder.loadTexts:
    eqlStoragePoolAdminAccountEntry.setStatus("current")
_EqlStoragePoolAdminAccountRowStatus_Type = RowStatus
_EqlStoragePoolAdminAccountRowStatus_Object = MibTableColumn
eqlStoragePoolAdminAccountRowStatus = _EqlStoragePoolAdminAccountRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 3, 1, 1),
    _EqlStoragePoolAdminAccountRowStatus_Type()
)
eqlStoragePoolAdminAccountRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStoragePoolAdminAccountRowStatus.setStatus("current")
_EqlStoragePoolAdminAccountQuotaType_Type = PoolQuotaType
_EqlStoragePoolAdminAccountQuotaType_Object = MibTableColumn
eqlStoragePoolAdminAccountQuotaType = _EqlStoragePoolAdminAccountQuotaType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 3, 1, 2),
    _EqlStoragePoolAdminAccountQuotaType_Type()
)
eqlStoragePoolAdminAccountQuotaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStoragePoolAdminAccountQuotaType.setStatus("current")
_EqlStoragePoolAdminAccountQuota_Type = Unsigned32
_EqlStoragePoolAdminAccountQuota_Object = MibTableColumn
eqlStoragePoolAdminAccountQuota = _EqlStoragePoolAdminAccountQuota_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 3, 1, 3),
    _EqlStoragePoolAdminAccountQuota_Type()
)
eqlStoragePoolAdminAccountQuota.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStoragePoolAdminAccountQuota.setStatus("current")
_EqlAdminAccountStoragePoolTable_Object = MibTable
eqlAdminAccountStoragePoolTable = _EqlAdminAccountStoragePoolTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 4)
)
if mibBuilder.loadTexts:
    eqlAdminAccountStoragePoolTable.setStatus("current")
_EqlAdminAccountStoragePoolEntry_Object = MibTableRow
eqlAdminAccountStoragePoolEntry = _EqlAdminAccountStoragePoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 4, 1)
)
eqlAdminAccountStoragePoolEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlStorageGroupAdminAccountIndex"),
    (0, "EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex"),
)
if mibBuilder.loadTexts:
    eqlAdminAccountStoragePoolEntry.setStatus("current")


class _EqlAdminAccountStoragePoolAccess_Type(Integer32):
    """Custom type eqlAdminAccountStoragePoolAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read-only", 1),
          ("read-write", 2))
    )


_EqlAdminAccountStoragePoolAccess_Type.__name__ = "Integer32"
_EqlAdminAccountStoragePoolAccess_Object = MibTableColumn
eqlAdminAccountStoragePoolAccess = _EqlAdminAccountStoragePoolAccess_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 4, 1, 1),
    _EqlAdminAccountStoragePoolAccess_Type()
)
eqlAdminAccountStoragePoolAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlAdminAccountStoragePoolAccess.setStatus("current")
_EqlStoragePoolOpsTable_Object = MibTable
eqlStoragePoolOpsTable = _EqlStoragePoolOpsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 5)
)
if mibBuilder.loadTexts:
    eqlStoragePoolOpsTable.setStatus("current")
_EqlStoragePoolOpsEntry_Object = MibTableRow
eqlStoragePoolOpsEntry = _EqlStoragePoolOpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 5, 1)
)
eqlStoragePoolOpsEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex"),
    (0, "EQLSTORAGEPOOL-MIB", "eqlStoragePoolOpsIndex"),
)
if mibBuilder.loadTexts:
    eqlStoragePoolOpsEntry.setStatus("current")
_EqlStoragePoolOpsIndex_Type = Unsigned32
_EqlStoragePoolOpsIndex_Object = MibTableColumn
eqlStoragePoolOpsIndex = _EqlStoragePoolOpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 5, 1, 1),
    _EqlStoragePoolOpsIndex_Type()
)
eqlStoragePoolOpsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlStoragePoolOpsIndex.setStatus("current")
_EqlStoragePoolOpsRowStatus_Type = RowStatus
_EqlStoragePoolOpsRowStatus_Object = MibTableColumn
eqlStoragePoolOpsRowStatus = _EqlStoragePoolOpsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 5, 1, 2),
    _EqlStoragePoolOpsRowStatus_Type()
)
eqlStoragePoolOpsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStoragePoolOpsRowStatus.setStatus("current")


class _EqlStoragePoolOpsOperation_Type(Integer32):
    """Custom type eqlStoragePoolOpsOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("none", 0))
    )


_EqlStoragePoolOpsOperation_Type.__name__ = "Integer32"
_EqlStoragePoolOpsOperation_Object = MibTableColumn
eqlStoragePoolOpsOperation = _EqlStoragePoolOpsOperation_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 5, 1, 3),
    _EqlStoragePoolOpsOperation_Type()
)
eqlStoragePoolOpsOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlStoragePoolOpsOperation.setStatus("current")


class _EqlStoragePoolOpsStoragePoolDestinationIndex_Type(Unsigned32):
    """Custom type eqlStoragePoolOpsStoragePoolDestinationIndex based on Unsigned32"""
    defaultValue = 1


_EqlStoragePoolOpsStoragePoolDestinationIndex_Object = MibTableColumn
eqlStoragePoolOpsStoragePoolDestinationIndex = _EqlStoragePoolOpsStoragePoolDestinationIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 5, 1, 4),
    _EqlStoragePoolOpsStoragePoolDestinationIndex_Type()
)
eqlStoragePoolOpsStoragePoolDestinationIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlStoragePoolOpsStoragePoolDestinationIndex.setStatus("current")
_EqlStoragePoolAdminAccountStatsTable_Object = MibTable
eqlStoragePoolAdminAccountStatsTable = _EqlStoragePoolAdminAccountStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 6)
)
if mibBuilder.loadTexts:
    eqlStoragePoolAdminAccountStatsTable.setStatus("current")
_EqlStoragePoolAdminAccountStatsEntry_Object = MibTableRow
eqlStoragePoolAdminAccountStatsEntry = _EqlStoragePoolAdminAccountStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1)
)
if mibBuilder.loadTexts:
    eqlStoragePoolAdminAccountStatsEntry.setStatus("current")
_EqlStorageAdminAccountPoolStatsQuota_Type = Unsigned64
_EqlStorageAdminAccountPoolStatsQuota_Object = MibTableColumn
eqlStorageAdminAccountPoolStatsQuota = _EqlStorageAdminAccountPoolStatsQuota_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 1),
    _EqlStorageAdminAccountPoolStatsQuota_Type()
)
eqlStorageAdminAccountPoolStatsQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsQuota.setStatus("current")
_EqlStorageAdminAccountPoolStatsQuotaUsed_Type = Unsigned64
_EqlStorageAdminAccountPoolStatsQuotaUsed_Object = MibTableColumn
eqlStorageAdminAccountPoolStatsQuotaUsed = _EqlStorageAdminAccountPoolStatsQuotaUsed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 2),
    _EqlStorageAdminAccountPoolStatsQuotaUsed_Type()
)
eqlStorageAdminAccountPoolStatsQuotaUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsQuotaUsed.setStatus("current")
_EqlStorageAdminAccountPoolStatsQuotaAvailable_Type = Unsigned64
_EqlStorageAdminAccountPoolStatsQuotaAvailable_Object = MibTableColumn
eqlStorageAdminAccountPoolStatsQuotaAvailable = _EqlStorageAdminAccountPoolStatsQuotaAvailable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 3),
    _EqlStorageAdminAccountPoolStatsQuotaAvailable_Type()
)
eqlStorageAdminAccountPoolStatsQuotaAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsQuotaAvailable.setStatus("current")
_EqlStorageAdminAccountPoolStatsSnapshotReserved_Type = Unsigned64
_EqlStorageAdminAccountPoolStatsSnapshotReserved_Object = MibTableColumn
eqlStorageAdminAccountPoolStatsSnapshotReserved = _EqlStorageAdminAccountPoolStatsSnapshotReserved_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 4),
    _EqlStorageAdminAccountPoolStatsSnapshotReserved_Type()
)
eqlStorageAdminAccountPoolStatsSnapshotReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsSnapshotReserved.setStatus("current")
_EqlStorageAdminAccountPoolStatsSnapshotUsed_Type = Unsigned64
_EqlStorageAdminAccountPoolStatsSnapshotUsed_Object = MibTableColumn
eqlStorageAdminAccountPoolStatsSnapshotUsed = _EqlStorageAdminAccountPoolStatsSnapshotUsed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 5),
    _EqlStorageAdminAccountPoolStatsSnapshotUsed_Type()
)
eqlStorageAdminAccountPoolStatsSnapshotUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsSnapshotUsed.setStatus("current")
_EqlStorageAdminAccountPoolStatsSnapshotSubscribed_Type = Unsigned64
_EqlStorageAdminAccountPoolStatsSnapshotSubscribed_Object = MibTableColumn
eqlStorageAdminAccountPoolStatsSnapshotSubscribed = _EqlStorageAdminAccountPoolStatsSnapshotSubscribed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 6),
    _EqlStorageAdminAccountPoolStatsSnapshotSubscribed_Type()
)
eqlStorageAdminAccountPoolStatsSnapshotSubscribed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsSnapshotSubscribed.setStatus("current")
_EqlStorageAdminAccountPoolStatsSnapshotNumInUse_Type = Integer32
_EqlStorageAdminAccountPoolStatsSnapshotNumInUse_Object = MibTableColumn
eqlStorageAdminAccountPoolStatsSnapshotNumInUse = _EqlStorageAdminAccountPoolStatsSnapshotNumInUse_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 7),
    _EqlStorageAdminAccountPoolStatsSnapshotNumInUse_Type()
)
eqlStorageAdminAccountPoolStatsSnapshotNumInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsSnapshotNumInUse.setStatus("current")
_EqlStorageAdminAccountPoolStatsSnapshotNumOnline_Type = Integer32
_EqlStorageAdminAccountPoolStatsSnapshotNumOnline_Object = MibTableColumn
eqlStorageAdminAccountPoolStatsSnapshotNumOnline = _EqlStorageAdminAccountPoolStatsSnapshotNumOnline_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 8),
    _EqlStorageAdminAccountPoolStatsSnapshotNumOnline_Type()
)
eqlStorageAdminAccountPoolStatsSnapshotNumOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsSnapshotNumOnline.setStatus("current")
_EqlStorageAdminAccountPoolStatsSnapshotCount_Type = Integer32
_EqlStorageAdminAccountPoolStatsSnapshotCount_Object = MibTableColumn
eqlStorageAdminAccountPoolStatsSnapshotCount = _EqlStorageAdminAccountPoolStatsSnapshotCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 9),
    _EqlStorageAdminAccountPoolStatsSnapshotCount_Type()
)
eqlStorageAdminAccountPoolStatsSnapshotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsSnapshotCount.setStatus("current")
_EqlStorageAdminAccountPoolStatsVolumeNumInUse_Type = Integer32
_EqlStorageAdminAccountPoolStatsVolumeNumInUse_Object = MibTableColumn
eqlStorageAdminAccountPoolStatsVolumeNumInUse = _EqlStorageAdminAccountPoolStatsVolumeNumInUse_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 10),
    _EqlStorageAdminAccountPoolStatsVolumeNumInUse_Type()
)
eqlStorageAdminAccountPoolStatsVolumeNumInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsVolumeNumInUse.setStatus("current")
_EqlStorageAdminAccountPoolStatsVolumeNumOnline_Type = Integer32
_EqlStorageAdminAccountPoolStatsVolumeNumOnline_Object = MibTableColumn
eqlStorageAdminAccountPoolStatsVolumeNumOnline = _EqlStorageAdminAccountPoolStatsVolumeNumOnline_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 11),
    _EqlStorageAdminAccountPoolStatsVolumeNumOnline_Type()
)
eqlStorageAdminAccountPoolStatsVolumeNumOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsVolumeNumOnline.setStatus("current")
_EqlStorageAdminAccountPoolStatsVolumeCount_Type = Integer32
_EqlStorageAdminAccountPoolStatsVolumeCount_Object = MibTableColumn
eqlStorageAdminAccountPoolStatsVolumeCount = _EqlStorageAdminAccountPoolStatsVolumeCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 12),
    _EqlStorageAdminAccountPoolStatsVolumeCount_Type()
)
eqlStorageAdminAccountPoolStatsVolumeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsVolumeCount.setStatus("current")
_EqlStorageAdminAccountPoolStatsVolumeSubscribed_Type = Unsigned64
_EqlStorageAdminAccountPoolStatsVolumeSubscribed_Object = MibTableColumn
eqlStorageAdminAccountPoolStatsVolumeSubscribed = _EqlStorageAdminAccountPoolStatsVolumeSubscribed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 13),
    _EqlStorageAdminAccountPoolStatsVolumeSubscribed_Type()
)
eqlStorageAdminAccountPoolStatsVolumeSubscribed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsVolumeSubscribed.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsVolumeSubscribed.setUnits("MB")
_EqlStorageAdminAccountPoolStatsVolumeQuotaUsage_Type = Unsigned64
_EqlStorageAdminAccountPoolStatsVolumeQuotaUsage_Object = MibTableColumn
eqlStorageAdminAccountPoolStatsVolumeQuotaUsage = _EqlStorageAdminAccountPoolStatsVolumeQuotaUsage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 14),
    _EqlStorageAdminAccountPoolStatsVolumeQuotaUsage_Type()
)
eqlStorageAdminAccountPoolStatsVolumeQuotaUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsVolumeQuotaUsage.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsVolumeQuotaUsage.setUnits("MB")
_EqlStorageAdminAccountPoolStatsVolumeSpaceAllocated_Type = Unsigned64
_EqlStorageAdminAccountPoolStatsVolumeSpaceAllocated_Object = MibTableColumn
eqlStorageAdminAccountPoolStatsVolumeSpaceAllocated = _EqlStorageAdminAccountPoolStatsVolumeSpaceAllocated_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 15),
    _EqlStorageAdminAccountPoolStatsVolumeSpaceAllocated_Type()
)
eqlStorageAdminAccountPoolStatsVolumeSpaceAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsVolumeSpaceAllocated.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsVolumeSpaceAllocated.setUnits("MB")
_EqlStorageAdminAccountPoolStatsFailbackSpace_Type = Unsigned64
_EqlStorageAdminAccountPoolStatsFailbackSpace_Object = MibTableColumn
eqlStorageAdminAccountPoolStatsFailbackSpace = _EqlStorageAdminAccountPoolStatsFailbackSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 16),
    _EqlStorageAdminAccountPoolStatsFailbackSpace_Type()
)
eqlStorageAdminAccountPoolStatsFailbackSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsFailbackSpace.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsFailbackSpace.setUnits("MB")
_EqlStorageAdminAccountPoolStatsFailbackSubscribed_Type = Unsigned64
_EqlStorageAdminAccountPoolStatsFailbackSubscribed_Object = MibTableColumn
eqlStorageAdminAccountPoolStatsFailbackSubscribed = _EqlStorageAdminAccountPoolStatsFailbackSubscribed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 17),
    _EqlStorageAdminAccountPoolStatsFailbackSubscribed_Type()
)
eqlStorageAdminAccountPoolStatsFailbackSubscribed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsFailbackSubscribed.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsFailbackSubscribed.setUnits("MB")
_EqlStorageAdminAccountPoolStatsThinProvFreeSpace_Type = Unsigned64
_EqlStorageAdminAccountPoolStatsThinProvFreeSpace_Object = MibTableColumn
eqlStorageAdminAccountPoolStatsThinProvFreeSpace = _EqlStorageAdminAccountPoolStatsThinProvFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 18),
    _EqlStorageAdminAccountPoolStatsThinProvFreeSpace_Type()
)
eqlStorageAdminAccountPoolStatsThinProvFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsThinProvFreeSpace.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsThinProvFreeSpace.setUnits("MB")
_EqlStorageAdminAccountPoolStatsConnectionCount_Type = Integer32
_EqlStorageAdminAccountPoolStatsConnectionCount_Object = MibTableColumn
eqlStorageAdminAccountPoolStatsConnectionCount = _EqlStorageAdminAccountPoolStatsConnectionCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 19),
    _EqlStorageAdminAccountPoolStatsConnectionCount_Type()
)
eqlStorageAdminAccountPoolStatsConnectionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsConnectionCount.setStatus("current")
_EqlStorageAdminAccountPoolStatsSnapshotResvFreeSpace_Type = Unsigned64
_EqlStorageAdminAccountPoolStatsSnapshotResvFreeSpace_Object = MibTableColumn
eqlStorageAdminAccountPoolStatsSnapshotResvFreeSpace = _EqlStorageAdminAccountPoolStatsSnapshotResvFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 20),
    _EqlStorageAdminAccountPoolStatsSnapshotResvFreeSpace_Type()
)
eqlStorageAdminAccountPoolStatsSnapshotResvFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsSnapshotResvFreeSpace.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsSnapshotResvFreeSpace.setUnits("MB")
_EqlStorageAdminAccountPoolStatsSpaceUsed_Type = Unsigned64
_EqlStorageAdminAccountPoolStatsSpaceUsed_Object = MibTableColumn
eqlStorageAdminAccountPoolStatsSpaceUsed = _EqlStorageAdminAccountPoolStatsSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 6, 1, 21),
    _EqlStorageAdminAccountPoolStatsSpaceUsed_Type()
)
eqlStorageAdminAccountPoolStatsSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsSpaceUsed.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageAdminAccountPoolStatsSpaceUsed.setUnits("MB")
_EqlLdapLoginAccessPoolTable_Object = MibTable
eqlLdapLoginAccessPoolTable = _EqlLdapLoginAccessPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 7)
)
if mibBuilder.loadTexts:
    eqlLdapLoginAccessPoolTable.setStatus("current")
_EqlLdapLoginAccessPoolEntry_Object = MibTableRow
eqlLdapLoginAccessPoolEntry = _EqlLdapLoginAccessPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 7, 1)
)
eqlLdapLoginAccessPoolEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlLdapLoginAccessType"),
    (0, "EQLGROUP-MIB", "eqlLdapLoginAccessName"),
    (0, "EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex"),
)
if mibBuilder.loadTexts:
    eqlLdapLoginAccessPoolEntry.setStatus("current")
_EqlLdapLoginAccessPoolQuotaType_Type = PoolQuotaType
_EqlLdapLoginAccessPoolQuotaType_Object = MibTableColumn
eqlLdapLoginAccessPoolQuotaType = _EqlLdapLoginAccessPoolQuotaType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 7, 1, 1),
    _EqlLdapLoginAccessPoolQuotaType_Type()
)
eqlLdapLoginAccessPoolQuotaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlLdapLoginAccessPoolQuotaType.setStatus("current")
_EqlLdapLoginAccessPoolQuota_Type = Unsigned32
_EqlLdapLoginAccessPoolQuota_Object = MibTableColumn
eqlLdapLoginAccessPoolQuota = _EqlLdapLoginAccessPoolQuota_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 7, 1, 2),
    _EqlLdapLoginAccessPoolQuota_Type()
)
eqlLdapLoginAccessPoolQuota.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlLdapLoginAccessPoolQuota.setStatus("current")
_EqlLdapLoginAccessPoolQuotaRowStatus_Type = RowStatus
_EqlLdapLoginAccessPoolQuotaRowStatus_Object = MibTableColumn
eqlLdapLoginAccessPoolQuotaRowStatus = _EqlLdapLoginAccessPoolQuotaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 7, 1, 3),
    _EqlLdapLoginAccessPoolQuotaRowStatus_Type()
)
eqlLdapLoginAccessPoolQuotaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlLdapLoginAccessPoolQuotaRowStatus.setStatus("current")
_EqlStoragePoolOperStatusTable_Object = MibTable
eqlStoragePoolOperStatusTable = _EqlStoragePoolOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 8)
)
if mibBuilder.loadTexts:
    eqlStoragePoolOperStatusTable.setStatus("current")
_EqlStoragePoolOperStatusEntry_Object = MibTableRow
eqlStoragePoolOperStatusEntry = _EqlStoragePoolOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 8, 1)
)
if mibBuilder.loadTexts:
    eqlStoragePoolOperStatusEntry.setStatus("current")


class _EqlStoragePoolOperStatusCompression_Type(Integer32):
    """Custom type eqlStoragePoolOperStatusCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("no-capable-hardware", 3),
          ("no-capable-raid", 4),
          ("paused", 2),
          ("unknown", 5))
    )


_EqlStoragePoolOperStatusCompression_Type.__name__ = "Integer32"
_EqlStoragePoolOperStatusCompression_Object = MibTableColumn
eqlStoragePoolOperStatusCompression = _EqlStoragePoolOperStatusCompression_Object(
    (1, 3, 6, 1, 4, 1, 12740, 16, 1, 8, 1, 1),
    _EqlStoragePoolOperStatusCompression_Type()
)
eqlStoragePoolOperStatusCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolOperStatusCompression.setStatus("current")
_EqlStoragePoolNotifications_ObjectIdentity = ObjectIdentity
eqlStoragePoolNotifications = _EqlStoragePoolNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 16, 2)
)
_EqlStoragePoolConformance_ObjectIdentity = ObjectIdentity
eqlStoragePoolConformance = _EqlStoragePoolConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 16, 3)
)
eqlStoragePoolEntry.registerAugmentions(
    ("EQLSTORAGEPOOL-MIB",
     "eqlStoragePoolStatsEntry")
)
eqlStoragePoolStatsEntry.setIndexNames(*eqlStoragePoolEntry.getIndexNames())
eqlStoragePoolAdminAccountEntry.registerAugmentions(
    ("EQLSTORAGEPOOL-MIB",
     "eqlStoragePoolAdminAccountStatsEntry")
)
eqlStoragePoolAdminAccountStatsEntry.setIndexNames(*eqlStoragePoolAdminAccountEntry.getIndexNames())
eqlStoragePoolEntry.registerAugmentions(
    ("EQLSTORAGEPOOL-MIB",
     "eqlStoragePoolOperStatusEntry")
)
eqlStoragePoolOperStatusEntry.setIndexNames(*eqlStoragePoolEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQLSTORAGEPOOL-MIB",
    **{"SiteIndex": SiteIndex,
       "SiteIndexOrZero": SiteIndexOrZero,
       "Unsigned64": Unsigned64,
       "PoolQuotaType": PoolQuotaType,
       "StatusEnabledDefault": StatusEnabledDefault,
       "eqlStoragePoolModule": eqlStoragePoolModule,
       "eqlStoragePoolObjects": eqlStoragePoolObjects,
       "eqlStoragePoolTable": eqlStoragePoolTable,
       "eqlStoragePoolEntry": eqlStoragePoolEntry,
       "eqlStoragePoolIndex": eqlStoragePoolIndex,
       "eqlStoragePoolRowStatus": eqlStoragePoolRowStatus,
       "eqlStoragePoolName": eqlStoragePoolName,
       "eqlStoragePoolDefaultFlag": eqlStoragePoolDefaultFlag,
       "eqlStoragePoolRAIDConfigWaitFlag": eqlStoragePoolRAIDConfigWaitFlag,
       "eqlStoragePoolShouldEvalMask": eqlStoragePoolShouldEvalMask,
       "eqlStoragePoolLastBalance": eqlStoragePoolLastBalance,
       "eqlStoragePoolDescription": eqlStoragePoolDescription,
       "eqlStoragePoolLeadMemberId": eqlStoragePoolLeadMemberId,
       "eqlStoragePoolUUID": eqlStoragePoolUUID,
       "eqlStoragePoolExecMergeTo": eqlStoragePoolExecMergeTo,
       "eqlStoragePoolBorrow": eqlStoragePoolBorrow,
       "eqlStoragePoolSnapTrimThreshold": eqlStoragePoolSnapTrimThreshold,
       "eqlStoragePoolSnapTrimBuffer": eqlStoragePoolSnapTrimBuffer,
       "eqlStoragePoolSnapTrimmerHWMLifeTime": eqlStoragePoolSnapTrimmerHWMLifeTime,
       "eqlStoragePoolSnapTrimmerBorrowInfoRefreshInterval": eqlStoragePoolSnapTrimmerBorrowInfoRefreshInterval,
       "eqlStoragePoolDefaultCompressionStrategy": eqlStoragePoolDefaultCompressionStrategy,
       "eqlStoragePoolDefaultCompressionMinSnapDelay": eqlStoragePoolDefaultCompressionMinSnapDelay,
       "eqlStoragePoolDefaultCompressionMinSnapAge": eqlStoragePoolDefaultCompressionMinSnapAge,
       "eqlStoragePoolSnapMemberTrimThresholdAmount": eqlStoragePoolSnapMemberTrimThresholdAmount,
       "eqlStoragePoolSnapTrimRecheckTimer": eqlStoragePoolSnapTrimRecheckTimer,
       "eqlStoragePoolStatsTable": eqlStoragePoolStatsTable,
       "eqlStoragePoolStatsEntry": eqlStoragePoolStatsEntry,
       "eqlStoragePoolStatsSpace": eqlStoragePoolStatsSpace,
       "eqlStoragePoolStatsSpaceUsed": eqlStoragePoolStatsSpaceUsed,
       "eqlStoragePoolStatsFreeSpace": eqlStoragePoolStatsFreeSpace,
       "eqlStoragePoolStatsReplicationSpace": eqlStoragePoolStatsReplicationSpace,
       "eqlStoragePoolStatsReplicationSpaceUsed": eqlStoragePoolStatsReplicationSpaceUsed,
       "eqlStoragePoolStatsReplicationFreeSpace": eqlStoragePoolStatsReplicationFreeSpace,
       "eqlStoragePoolStatsMemberNumOnline": eqlStoragePoolStatsMemberNumOnline,
       "eqlStoragePoolStatsMemberCount": eqlStoragePoolStatsMemberCount,
       "eqlStoragePoolStatsSnapshotReserved": eqlStoragePoolStatsSnapshotReserved,
       "eqlStoragePoolStatsSnapshotUsed": eqlStoragePoolStatsSnapshotUsed,
       "eqlStoragePoolStatsSnapshotNumInUse": eqlStoragePoolStatsSnapshotNumInUse,
       "eqlStoragePoolStatsSnapshotNumOnline": eqlStoragePoolStatsSnapshotNumOnline,
       "eqlStoragePoolStatsSnapshotCount": eqlStoragePoolStatsSnapshotCount,
       "eqlStoragePoolStatsVolumeNumInUse": eqlStoragePoolStatsVolumeNumInUse,
       "eqlStoragePoolStatsVolumeNumOnline": eqlStoragePoolStatsVolumeNumOnline,
       "eqlStoragePoolStatsVolumeCount": eqlStoragePoolStatsVolumeCount,
       "eqlStoragePoolStatsDelegatedSpace": eqlStoragePoolStatsDelegatedSpace,
       "eqlStoragePoolStatsDelegatedSpaceUsed": eqlStoragePoolStatsDelegatedSpaceUsed,
       "eqlStoragePoolStatsMembersInUse": eqlStoragePoolStatsMembersInUse,
       "eqlStoragePoolStatsVolumeSubscribed": eqlStoragePoolStatsVolumeSubscribed,
       "eqlStoragePoolStatsVolumeSpaceAllocated": eqlStoragePoolStatsVolumeSpaceAllocated,
       "eqlStoragePoolStatsFailbackSpace": eqlStoragePoolStatsFailbackSpace,
       "eqlStoragePoolStatsThinProvFreeSpace": eqlStoragePoolStatsThinProvFreeSpace,
       "eqlStoragePoolStatsConnectionCount": eqlStoragePoolStatsConnectionCount,
       "eqlStoragePoolStatsSnapshotResvFreeSpace": eqlStoragePoolStatsSnapshotResvFreeSpace,
       "eqlStoragePoolStatsVirtualVolumeNumInUse": eqlStoragePoolStatsVirtualVolumeNumInUse,
       "eqlStoragePoolStatsVirtualVolumeNumOnline": eqlStoragePoolStatsVirtualVolumeNumOnline,
       "eqlStoragePoolStatsSnapshotResvBorrowing": eqlStoragePoolStatsSnapshotResvBorrowing,
       "eqlStoragePoolStatsFreeSpaceBorrowing": eqlStoragePoolStatsFreeSpaceBorrowing,
       "eqlStoragePoolStatsAvailableForBorrowing": eqlStoragePoolStatsAvailableForBorrowing,
       "eqlStoragePoolStatsRecoverableVolBorrowing": eqlStoragePoolStatsRecoverableVolBorrowing,
       "eqlStoragePoolStatsActualFreeSpace": eqlStoragePoolStatsActualFreeSpace,
       "eqlStoragePoolStatsTotalSpaceBorrowing": eqlStoragePoolStatsTotalSpaceBorrowing,
       "eqlStoragePoolStatsSnapShotBorrowing": eqlStoragePoolStatsSnapShotBorrowing,
       "eqlStoragePoolStatsStorageContainerCount": eqlStoragePoolStatsStorageContainerCount,
       "eqlStoragePoolStatsStorageContainerSpaceReserved": eqlStoragePoolStatsStorageContainerSpaceReserved,
       "eqlStoragePoolStatsCompressedSpaceUsed": eqlStoragePoolStatsCompressedSpaceUsed,
       "eqlStoragePoolStatsVirtualSpaceSize": eqlStoragePoolStatsVirtualSpaceSize,
       "eqlStoragePoolStatsStorageContainerVolumeCount": eqlStoragePoolStatsStorageContainerVolumeCount,
       "eqlStoragePoolStatsStorageContainerSnapCount": eqlStoragePoolStatsStorageContainerSnapCount,
       "eqlStoragePoolStatsStorageContainerVolumesOnline": eqlStoragePoolStatsStorageContainerVolumesOnline,
       "eqlStoragePoolAdminAccountTable": eqlStoragePoolAdminAccountTable,
       "eqlStoragePoolAdminAccountEntry": eqlStoragePoolAdminAccountEntry,
       "eqlStoragePoolAdminAccountRowStatus": eqlStoragePoolAdminAccountRowStatus,
       "eqlStoragePoolAdminAccountQuotaType": eqlStoragePoolAdminAccountQuotaType,
       "eqlStoragePoolAdminAccountQuota": eqlStoragePoolAdminAccountQuota,
       "eqlAdminAccountStoragePoolTable": eqlAdminAccountStoragePoolTable,
       "eqlAdminAccountStoragePoolEntry": eqlAdminAccountStoragePoolEntry,
       "eqlAdminAccountStoragePoolAccess": eqlAdminAccountStoragePoolAccess,
       "eqlStoragePoolOpsTable": eqlStoragePoolOpsTable,
       "eqlStoragePoolOpsEntry": eqlStoragePoolOpsEntry,
       "eqlStoragePoolOpsIndex": eqlStoragePoolOpsIndex,
       "eqlStoragePoolOpsRowStatus": eqlStoragePoolOpsRowStatus,
       "eqlStoragePoolOpsOperation": eqlStoragePoolOpsOperation,
       "eqlStoragePoolOpsStoragePoolDestinationIndex": eqlStoragePoolOpsStoragePoolDestinationIndex,
       "eqlStoragePoolAdminAccountStatsTable": eqlStoragePoolAdminAccountStatsTable,
       "eqlStoragePoolAdminAccountStatsEntry": eqlStoragePoolAdminAccountStatsEntry,
       "eqlStorageAdminAccountPoolStatsQuota": eqlStorageAdminAccountPoolStatsQuota,
       "eqlStorageAdminAccountPoolStatsQuotaUsed": eqlStorageAdminAccountPoolStatsQuotaUsed,
       "eqlStorageAdminAccountPoolStatsQuotaAvailable": eqlStorageAdminAccountPoolStatsQuotaAvailable,
       "eqlStorageAdminAccountPoolStatsSnapshotReserved": eqlStorageAdminAccountPoolStatsSnapshotReserved,
       "eqlStorageAdminAccountPoolStatsSnapshotUsed": eqlStorageAdminAccountPoolStatsSnapshotUsed,
       "eqlStorageAdminAccountPoolStatsSnapshotSubscribed": eqlStorageAdminAccountPoolStatsSnapshotSubscribed,
       "eqlStorageAdminAccountPoolStatsSnapshotNumInUse": eqlStorageAdminAccountPoolStatsSnapshotNumInUse,
       "eqlStorageAdminAccountPoolStatsSnapshotNumOnline": eqlStorageAdminAccountPoolStatsSnapshotNumOnline,
       "eqlStorageAdminAccountPoolStatsSnapshotCount": eqlStorageAdminAccountPoolStatsSnapshotCount,
       "eqlStorageAdminAccountPoolStatsVolumeNumInUse": eqlStorageAdminAccountPoolStatsVolumeNumInUse,
       "eqlStorageAdminAccountPoolStatsVolumeNumOnline": eqlStorageAdminAccountPoolStatsVolumeNumOnline,
       "eqlStorageAdminAccountPoolStatsVolumeCount": eqlStorageAdminAccountPoolStatsVolumeCount,
       "eqlStorageAdminAccountPoolStatsVolumeSubscribed": eqlStorageAdminAccountPoolStatsVolumeSubscribed,
       "eqlStorageAdminAccountPoolStatsVolumeQuotaUsage": eqlStorageAdminAccountPoolStatsVolumeQuotaUsage,
       "eqlStorageAdminAccountPoolStatsVolumeSpaceAllocated": eqlStorageAdminAccountPoolStatsVolumeSpaceAllocated,
       "eqlStorageAdminAccountPoolStatsFailbackSpace": eqlStorageAdminAccountPoolStatsFailbackSpace,
       "eqlStorageAdminAccountPoolStatsFailbackSubscribed": eqlStorageAdminAccountPoolStatsFailbackSubscribed,
       "eqlStorageAdminAccountPoolStatsThinProvFreeSpace": eqlStorageAdminAccountPoolStatsThinProvFreeSpace,
       "eqlStorageAdminAccountPoolStatsConnectionCount": eqlStorageAdminAccountPoolStatsConnectionCount,
       "eqlStorageAdminAccountPoolStatsSnapshotResvFreeSpace": eqlStorageAdminAccountPoolStatsSnapshotResvFreeSpace,
       "eqlStorageAdminAccountPoolStatsSpaceUsed": eqlStorageAdminAccountPoolStatsSpaceUsed,
       "eqlLdapLoginAccessPoolTable": eqlLdapLoginAccessPoolTable,
       "eqlLdapLoginAccessPoolEntry": eqlLdapLoginAccessPoolEntry,
       "eqlLdapLoginAccessPoolQuotaType": eqlLdapLoginAccessPoolQuotaType,
       "eqlLdapLoginAccessPoolQuota": eqlLdapLoginAccessPoolQuota,
       "eqlLdapLoginAccessPoolQuotaRowStatus": eqlLdapLoginAccessPoolQuotaRowStatus,
       "eqlStoragePoolOperStatusTable": eqlStoragePoolOperStatusTable,
       "eqlStoragePoolOperStatusEntry": eqlStoragePoolOperStatusEntry,
       "eqlStoragePoolOperStatusCompression": eqlStoragePoolOperStatusCompression,
       "eqlStoragePoolNotifications": eqlStoragePoolNotifications,
       "eqlStoragePoolConformance": eqlStoragePoolConformance}
)
