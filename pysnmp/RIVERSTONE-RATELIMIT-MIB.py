# SNMP MIB module (RIVERSTONE-RATELIMIT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RIVERSTONE-RATELIMIT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:51 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(riverstoneMibs,) = mibBuilder.importSymbols(
    "RIVERSTONE-SMI-MIB",
    "riverstoneMibs")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rsRateLimitMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25)
)
rsRateLimitMIB.setRevisions(
        ("2002-10-10 00:00",
         "2001-07-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RsRateLimit(Unsigned32, TextualConvention):
    status = "current"


class RsBurst(Unsigned32, TextualConvention):
    status = "current"


class RsAdminStatus(Integer32, TextualConvention):
    status = "current"
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



class RsDistAmong(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )



class RsMeterType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("burstsafe", 5),
          ("hardwareFlowAggregate", 3),
          ("l2", 6),
          ("perFlow", 1),
          ("perPort", 4),
          ("softwareFlowAggregate", 2))
    )



class RsMeterInterval(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )



class RsLabel(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )



class RsTOS(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class RsIfDirection(Integer32, TextualConvention):
    status = "current"
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
        *(("both", 3),
          ("inbound", 1),
          ("outbound", 2),
          ("unknown", 4))
    )



class RsAction(Integer32, TextualConvention):
    status = "current"
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
        *(("dropPackets", 2),
          ("lowerPriority", 6),
          ("lowerPriorityExceptControl", 7),
          ("markPackets", 12),
          ("noAction", 1),
          ("setPriorityHigh", 5),
          ("setPriorityLow", 3),
          ("setPriorityMedium", 4),
          ("tosPrecedenceRewrite", 10),
          ("tosPrecedenceRewriteAndLowerPriority", 11),
          ("tosRewrite", 8),
          ("tosRewriteAndLowerPriority", 9))
    )



# MIB Managed Objects in the order of their OIDs

_RsRateLimitNotifications_ObjectIdentity = ObjectIdentity
rsRateLimitNotifications = _RsRateLimitNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 0)
)
if mibBuilder.loadTexts:
    rsRateLimitNotifications.setStatus("current")
_RsTBMeter_ObjectIdentity = ObjectIdentity
rsTBMeter = _RsTBMeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 5)
)
if mibBuilder.loadTexts:
    rsTBMeter.setStatus("current")
_RsTBMeterLastChanged_Type = TimeTicks
_RsTBMeterLastChanged_Object = MibScalar
rsTBMeterLastChanged = _RsTBMeterLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 5, 1),
    _RsTBMeterLastChanged_Type()
)
rsTBMeterLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsTBMeterLastChanged.setStatus("current")
_RsTBMeterCount_Type = Unsigned32
_RsTBMeterCount_Object = MibScalar
rsTBMeterCount = _RsTBMeterCount_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 5, 2),
    _RsTBMeterCount_Type()
)
rsTBMeterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsTBMeterCount.setStatus("current")
_RsTBMeterErrorMessage_Type = SnmpAdminString
_RsTBMeterErrorMessage_Object = MibScalar
rsTBMeterErrorMessage = _RsTBMeterErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 5, 3),
    _RsTBMeterErrorMessage_Type()
)
rsTBMeterErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsTBMeterErrorMessage.setStatus("current")
_RsTBMeterTable_Object = MibTable
rsTBMeterTable = _RsTBMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 5, 4)
)
if mibBuilder.loadTexts:
    rsTBMeterTable.setStatus("current")
_RsTBMeterEntry_Object = MibTableRow
rsTBMeterEntry = _RsTBMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 5, 4, 1)
)
rsTBMeterEntry.setIndexNames(
    (0, "RIVERSTONE-RATELIMIT-MIB", "rsTBMeterId"),
)
if mibBuilder.loadTexts:
    rsTBMeterEntry.setStatus("current")
_RsTBMeterId_Type = RsLabel
_RsTBMeterId_Object = MibTableColumn
rsTBMeterId = _RsTBMeterId_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 5, 4, 1, 1),
    _RsTBMeterId_Type()
)
rsTBMeterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsTBMeterId.setStatus("current")


class _RsTBMeterType_Type(RsMeterType):
    """Custom type rsTBMeterType based on RsMeterType"""


_RsTBMeterType_Object = MibTableColumn
rsTBMeterType = _RsTBMeterType_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 5, 4, 1, 2),
    _RsTBMeterType_Type()
)
rsTBMeterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsTBMeterType.setStatus("current")


class _RsTBMeterRate_Type(RsRateLimit):
    """Custom type rsTBMeterRate based on RsRateLimit"""
    defaultValue = 3000


_RsTBMeterRate_Object = MibTableColumn
rsTBMeterRate = _RsTBMeterRate_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 5, 4, 1, 3),
    _RsTBMeterRate_Type()
)
rsTBMeterRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsTBMeterRate.setStatus("current")
if mibBuilder.loadTexts:
    rsTBMeterRate.setUnits("bps")


class _RsTBMeterBurst_Type(RsBurst):
    """Custom type rsTBMeterBurst based on RsBurst"""
    defaultValue = 10000


_RsTBMeterBurst_Object = MibTableColumn
rsTBMeterBurst = _RsTBMeterBurst_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 5, 4, 1, 4),
    _RsTBMeterBurst_Type()
)
rsTBMeterBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsTBMeterBurst.setStatus("current")
if mibBuilder.loadTexts:
    rsTBMeterBurst.setUnits("bps")
_RsTBMeterInterval_Type = RsMeterInterval
_RsTBMeterInterval_Object = MibTableColumn
rsTBMeterInterval = _RsTBMeterInterval_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 5, 4, 1, 5),
    _RsTBMeterInterval_Type()
)
rsTBMeterInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsTBMeterInterval.setStatus("deprecated")
_RsTBMeterFailAction_Type = RsAction
_RsTBMeterFailAction_Object = MibTableColumn
rsTBMeterFailAction = _RsTBMeterFailAction_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 5, 4, 1, 6),
    _RsTBMeterFailAction_Type()
)
rsTBMeterFailAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsTBMeterFailAction.setStatus("current")


class _RsTBMeterFailActionRewrite_Type(RsTOS):
    """Custom type rsTBMeterFailActionRewrite based on RsTOS"""
    defaultValue = 0


_RsTBMeterFailActionRewrite_Object = MibTableColumn
rsTBMeterFailActionRewrite = _RsTBMeterFailActionRewrite_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 5, 4, 1, 7),
    _RsTBMeterFailActionRewrite_Type()
)
rsTBMeterFailActionRewrite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsTBMeterFailActionRewrite.setStatus("current")
_RsTBMeterBurstFailAction_Type = RsAction
_RsTBMeterBurstFailAction_Object = MibTableColumn
rsTBMeterBurstFailAction = _RsTBMeterBurstFailAction_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 5, 4, 1, 8),
    _RsTBMeterBurstFailAction_Type()
)
rsTBMeterBurstFailAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsTBMeterBurstFailAction.setStatus("current")


class _RsTBMeterBurstFailActionRewrite_Type(RsTOS):
    """Custom type rsTBMeterBurstFailActionRewrite based on RsTOS"""
    defaultValue = 0


_RsTBMeterBurstFailActionRewrite_Object = MibTableColumn
rsTBMeterBurstFailActionRewrite = _RsTBMeterBurstFailActionRewrite_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 5, 4, 1, 9),
    _RsTBMeterBurstFailActionRewrite_Type()
)
rsTBMeterBurstFailActionRewrite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsTBMeterBurstFailActionRewrite.setStatus("current")


class _RsTBMeterMinimumBandwidth_Type(RsRateLimit):
    """Custom type rsTBMeterMinimumBandwidth based on RsRateLimit"""
    defaultValue = 3000


_RsTBMeterMinimumBandwidth_Object = MibTableColumn
rsTBMeterMinimumBandwidth = _RsTBMeterMinimumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 5, 4, 1, 10),
    _RsTBMeterMinimumBandwidth_Type()
)
rsTBMeterMinimumBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsTBMeterMinimumBandwidth.setStatus("deprecated")
if mibBuilder.loadTexts:
    rsTBMeterMinimumBandwidth.setUnits("bps")


class _RsTBMeterDistributeAmong_Type(RsDistAmong):
    """Custom type rsTBMeterDistributeAmong based on RsDistAmong"""
    defaultValue = 1


_RsTBMeterDistributeAmong_Object = MibTableColumn
rsTBMeterDistributeAmong = _RsTBMeterDistributeAmong_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 5, 4, 1, 11),
    _RsTBMeterDistributeAmong_Type()
)
rsTBMeterDistributeAmong.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsTBMeterDistributeAmong.setStatus("deprecated")


class _RsTBMeterStorageType_Type(StorageType):
    """Custom type rsTBMeterStorageType based on StorageType"""
    defaultValue = 2

    subtypeSpec = StorageType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonVolatile", 3),
          ("volatile", 2))
    )


_RsTBMeterStorageType_Type.__name__ = "StorageType"
_RsTBMeterStorageType_Object = MibTableColumn
rsTBMeterStorageType = _RsTBMeterStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 5, 4, 1, 12),
    _RsTBMeterStorageType_Type()
)
rsTBMeterStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsTBMeterStorageType.setStatus("current")
_RsTBMeterStatus_Type = RowStatus
_RsTBMeterStatus_Object = MibTableColumn
rsTBMeterStatus = _RsTBMeterStatus_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 5, 4, 1, 13),
    _RsTBMeterStatus_Type()
)
rsTBMeterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsTBMeterStatus.setStatus("current")
_RsTBMeterApply_ObjectIdentity = ObjectIdentity
rsTBMeterApply = _RsTBMeterApply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 10)
)
if mibBuilder.loadTexts:
    rsTBMeterApply.setStatus("current")
_RsTBMeterApplyLastChanged_Type = TimeTicks
_RsTBMeterApplyLastChanged_Object = MibScalar
rsTBMeterApplyLastChanged = _RsTBMeterApplyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 10, 1),
    _RsTBMeterApplyLastChanged_Type()
)
rsTBMeterApplyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsTBMeterApplyLastChanged.setStatus("current")
_RsTBMeterApplyCount_Type = Unsigned32
_RsTBMeterApplyCount_Object = MibScalar
rsTBMeterApplyCount = _RsTBMeterApplyCount_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 10, 2),
    _RsTBMeterApplyCount_Type()
)
rsTBMeterApplyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsTBMeterApplyCount.setStatus("current")
_RsTBMeterApplyErrorMessage_Type = SnmpAdminString
_RsTBMeterApplyErrorMessage_Object = MibScalar
rsTBMeterApplyErrorMessage = _RsTBMeterApplyErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 10, 3),
    _RsTBMeterApplyErrorMessage_Type()
)
rsTBMeterApplyErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsTBMeterApplyErrorMessage.setStatus("current")


class _RsTBMeterApplyMasterAdminStatus_Type(RsAdminStatus):
    """Custom type rsTBMeterApplyMasterAdminStatus based on RsAdminStatus"""


_RsTBMeterApplyMasterAdminStatus_Object = MibScalar
rsTBMeterApplyMasterAdminStatus = _RsTBMeterApplyMasterAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 10, 4),
    _RsTBMeterApplyMasterAdminStatus_Type()
)
rsTBMeterApplyMasterAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTBMeterApplyMasterAdminStatus.setStatus("current")
_RsTBMeterApplyTable_Object = MibTable
rsTBMeterApplyTable = _RsTBMeterApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 10, 5)
)
if mibBuilder.loadTexts:
    rsTBMeterApplyTable.setStatus("current")
_RsTBMeterApplyEntry_Object = MibTableRow
rsTBMeterApplyEntry = _RsTBMeterApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 10, 5, 1)
)
rsTBMeterApplyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RIVERSTONE-RATELIMIT-MIB", "rsTBMeterApplyDirection"),
    (0, "RIVERSTONE-RATELIMIT-MIB", "rsTBMeterApplyAclName"),
    (0, "RIVERSTONE-RATELIMIT-MIB", "rsTBMeterId2"),
)
if mibBuilder.loadTexts:
    rsTBMeterApplyEntry.setStatus("current")


class _RsTBMeterApplyDirection_Type(RsIfDirection):
    """Custom type rsTBMeterApplyDirection based on RsIfDirection"""
    subtypeSpec = RsIfDirection.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_RsTBMeterApplyDirection_Type.__name__ = "RsIfDirection"
_RsTBMeterApplyDirection_Object = MibTableColumn
rsTBMeterApplyDirection = _RsTBMeterApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 10, 5, 1, 1),
    _RsTBMeterApplyDirection_Type()
)
rsTBMeterApplyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsTBMeterApplyDirection.setStatus("current")
_RsTBMeterApplyAclName_Type = RsLabel
_RsTBMeterApplyAclName_Object = MibTableColumn
rsTBMeterApplyAclName = _RsTBMeterApplyAclName_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 10, 5, 1, 2),
    _RsTBMeterApplyAclName_Type()
)
rsTBMeterApplyAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsTBMeterApplyAclName.setStatus("current")
_RsTBMeterId2_Type = RsLabel
_RsTBMeterId2_Object = MibTableColumn
rsTBMeterId2 = _RsTBMeterId2_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 10, 5, 1, 3),
    _RsTBMeterId2_Type()
)
rsTBMeterId2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsTBMeterId2.setStatus("current")


class _RsTBMeterApplyOwner_Type(SnmpAdminString):
    """Custom type rsTBMeterApplyOwner based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RsTBMeterApplyOwner_Type.__name__ = "SnmpAdminString"
_RsTBMeterApplyOwner_Object = MibTableColumn
rsTBMeterApplyOwner = _RsTBMeterApplyOwner_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 10, 5, 1, 4),
    _RsTBMeterApplyOwner_Type()
)
rsTBMeterApplyOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsTBMeterApplyOwner.setStatus("current")


class _RsTBMeterApplyAdminStatus_Type(RsAdminStatus):
    """Custom type rsTBMeterApplyAdminStatus based on RsAdminStatus"""


_RsTBMeterApplyAdminStatus_Object = MibTableColumn
rsTBMeterApplyAdminStatus = _RsTBMeterApplyAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 10, 5, 1, 5),
    _RsTBMeterApplyAdminStatus_Type()
)
rsTBMeterApplyAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsTBMeterApplyAdminStatus.setStatus("current")


class _RsTBMeterApplyStorageType_Type(StorageType):
    """Custom type rsTBMeterApplyStorageType based on StorageType"""
    defaultValue = 2

    subtypeSpec = StorageType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonVolatile", 3),
          ("volatile", 2))
    )


_RsTBMeterApplyStorageType_Type.__name__ = "StorageType"
_RsTBMeterApplyStorageType_Object = MibTableColumn
rsTBMeterApplyStorageType = _RsTBMeterApplyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 10, 5, 1, 6),
    _RsTBMeterApplyStorageType_Type()
)
rsTBMeterApplyStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsTBMeterApplyStorageType.setStatus("current")
_RsTBMeterApplyStatus_Type = RowStatus
_RsTBMeterApplyStatus_Object = MibTableColumn
rsTBMeterApplyStatus = _RsTBMeterApplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 10, 5, 1, 7),
    _RsTBMeterApplyStatus_Type()
)
rsTBMeterApplyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsTBMeterApplyStatus.setStatus("current")
_RsTBMeterApplyMonitor_ObjectIdentity = ObjectIdentity
rsTBMeterApplyMonitor = _RsTBMeterApplyMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 15)
)
if mibBuilder.loadTexts:
    rsTBMeterApplyMonitor.setStatus("current")
_RsTBMeterMonitorTable_Object = MibTable
rsTBMeterMonitorTable = _RsTBMeterMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 15, 1)
)
if mibBuilder.loadTexts:
    rsTBMeterMonitorTable.setStatus("current")
_RsTBMeterMonitorEntry_Object = MibTableRow
rsTBMeterMonitorEntry = _RsTBMeterMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 15, 1, 1)
)
if mibBuilder.loadTexts:
    rsTBMeterMonitorEntry.setStatus("current")
_RsTBMeterExceedByteCount_Type = Counter32
_RsTBMeterExceedByteCount_Object = MibTableColumn
rsTBMeterExceedByteCount = _RsTBMeterExceedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 15, 1, 1, 1),
    _RsTBMeterExceedByteCount_Type()
)
rsTBMeterExceedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsTBMeterExceedByteCount.setStatus("current")
_RsTBMeterCounterDiscontinuityTime_Type = TimeTicks
_RsTBMeterCounterDiscontinuityTime_Object = MibTableColumn
rsTBMeterCounterDiscontinuityTime = _RsTBMeterCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 15, 1, 1, 2),
    _RsTBMeterCounterDiscontinuityTime_Type()
)
rsTBMeterCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsTBMeterCounterDiscontinuityTime.setStatus("current")
_RsTBMeterExceedPacketCount_Type = Counter32
_RsTBMeterExceedPacketCount_Object = MibTableColumn
rsTBMeterExceedPacketCount = _RsTBMeterExceedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 15, 1, 1, 3),
    _RsTBMeterExceedPacketCount_Type()
)
rsTBMeterExceedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsTBMeterExceedPacketCount.setStatus("current")
_RsTBMeterExceedBurstPacketCount_Type = Counter32
_RsTBMeterExceedBurstPacketCount_Object = MibTableColumn
rsTBMeterExceedBurstPacketCount = _RsTBMeterExceedBurstPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 15, 1, 1, 4),
    _RsTBMeterExceedBurstPacketCount_Type()
)
rsTBMeterExceedBurstPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsTBMeterExceedBurstPacketCount.setStatus("current")
_RsPortRateLimit_ObjectIdentity = ObjectIdentity
rsPortRateLimit = _RsPortRateLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 20)
)
if mibBuilder.loadTexts:
    rsPortRateLimit.setStatus("current")
_RsPortRLLastChanged_Type = TimeTicks
_RsPortRLLastChanged_Object = MibScalar
rsPortRLLastChanged = _RsPortRLLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 20, 1),
    _RsPortRLLastChanged_Type()
)
rsPortRLLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortRLLastChanged.setStatus("current")
_RsPortRLCount_Type = Unsigned32
_RsPortRLCount_Object = MibScalar
rsPortRLCount = _RsPortRLCount_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 20, 2),
    _RsPortRLCount_Type()
)
rsPortRLCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortRLCount.setStatus("current")
_RsPortRLErrorMessage_Type = SnmpAdminString
_RsPortRLErrorMessage_Object = MibScalar
rsPortRLErrorMessage = _RsPortRLErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 20, 3),
    _RsPortRLErrorMessage_Type()
)
rsPortRLErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortRLErrorMessage.setStatus("current")


class _RsPortRLMasterAdminStatus_Type(RsAdminStatus):
    """Custom type rsPortRLMasterAdminStatus based on RsAdminStatus"""


_RsPortRLMasterAdminStatus_Object = MibScalar
rsPortRLMasterAdminStatus = _RsPortRLMasterAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 20, 4),
    _RsPortRLMasterAdminStatus_Type()
)
rsPortRLMasterAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPortRLMasterAdminStatus.setStatus("current")
_RsPortRLTable_Object = MibTable
rsPortRLTable = _RsPortRLTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 20, 5)
)
if mibBuilder.loadTexts:
    rsPortRLTable.setStatus("current")
_RsPortRLEntry_Object = MibTableRow
rsPortRLEntry = _RsPortRLEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 20, 5, 1)
)
rsPortRLEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RIVERSTONE-RATELIMIT-MIB", "rsPortRLDirection"),
    (0, "RIVERSTONE-RATELIMIT-MIB", "rsPortRLMeterId"),
)
if mibBuilder.loadTexts:
    rsPortRLEntry.setStatus("current")


class _RsPortRLDirection_Type(RsIfDirection):
    """Custom type rsPortRLDirection based on RsIfDirection"""
    subtypeSpec = RsIfDirection.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_RsPortRLDirection_Type.__name__ = "RsIfDirection"
_RsPortRLDirection_Object = MibTableColumn
rsPortRLDirection = _RsPortRLDirection_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 20, 5, 1, 1),
    _RsPortRLDirection_Type()
)
rsPortRLDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsPortRLDirection.setStatus("current")
_RsPortRLMeterId_Type = RsLabel
_RsPortRLMeterId_Object = MibTableColumn
rsPortRLMeterId = _RsPortRLMeterId_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 20, 5, 1, 2),
    _RsPortRLMeterId_Type()
)
rsPortRLMeterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsPortRLMeterId.setStatus("current")


class _RsPortRLOwner_Type(SnmpAdminString):
    """Custom type rsPortRLOwner based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RsPortRLOwner_Type.__name__ = "SnmpAdminString"
_RsPortRLOwner_Object = MibTableColumn
rsPortRLOwner = _RsPortRLOwner_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 20, 5, 1, 3),
    _RsPortRLOwner_Type()
)
rsPortRLOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsPortRLOwner.setStatus("current")


class _RsPortRLRate_Type(RsRateLimit):
    """Custom type rsPortRLRate based on RsRateLimit"""
    defaultValue = 3000


_RsPortRLRate_Object = MibTableColumn
rsPortRLRate = _RsPortRLRate_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 20, 5, 1, 4),
    _RsPortRLRate_Type()
)
rsPortRLRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsPortRLRate.setStatus("current")
if mibBuilder.loadTexts:
    rsPortRLRate.setUnits("bps")
_RsPortRLFailAction_Type = RsAction
_RsPortRLFailAction_Object = MibTableColumn
rsPortRLFailAction = _RsPortRLFailAction_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 20, 5, 1, 5),
    _RsPortRLFailAction_Type()
)
rsPortRLFailAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsPortRLFailAction.setStatus("current")
_RsPortRLFailActionRewrite_Type = RsTOS
_RsPortRLFailActionRewrite_Object = MibTableColumn
rsPortRLFailActionRewrite = _RsPortRLFailActionRewrite_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 20, 5, 1, 6),
    _RsPortRLFailActionRewrite_Type()
)
rsPortRLFailActionRewrite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsPortRLFailActionRewrite.setStatus("current")
_RsPortRLInterval_Type = RsMeterInterval
_RsPortRLInterval_Object = MibTableColumn
rsPortRLInterval = _RsPortRLInterval_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 20, 5, 1, 7),
    _RsPortRLInterval_Type()
)
rsPortRLInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsPortRLInterval.setStatus("deprecated")


class _RsPortRLAdminStatus_Type(RsAdminStatus):
    """Custom type rsPortRLAdminStatus based on RsAdminStatus"""


_RsPortRLAdminStatus_Object = MibTableColumn
rsPortRLAdminStatus = _RsPortRLAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 20, 5, 1, 8),
    _RsPortRLAdminStatus_Type()
)
rsPortRLAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsPortRLAdminStatus.setStatus("current")


class _RsPortRLStorageType_Type(StorageType):
    """Custom type rsPortRLStorageType based on StorageType"""
    defaultValue = 2

    subtypeSpec = StorageType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonVolatile", 3),
          ("volatile", 2))
    )


_RsPortRLStorageType_Type.__name__ = "StorageType"
_RsPortRLStorageType_Object = MibTableColumn
rsPortRLStorageType = _RsPortRLStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 20, 5, 1, 9),
    _RsPortRLStorageType_Type()
)
rsPortRLStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsPortRLStorageType.setStatus("current")
_RsPortRLStatus_Type = RowStatus
_RsPortRLStatus_Object = MibTableColumn
rsPortRLStatus = _RsPortRLStatus_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 20, 5, 1, 10),
    _RsPortRLStatus_Type()
)
rsPortRLStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsPortRLStatus.setStatus("current")
_RsPortRLMonitor_ObjectIdentity = ObjectIdentity
rsPortRLMonitor = _RsPortRLMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 25)
)
if mibBuilder.loadTexts:
    rsPortRLMonitor.setStatus("current")
_RsPortRLMonitorTable_Object = MibTable
rsPortRLMonitorTable = _RsPortRLMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 25, 1)
)
if mibBuilder.loadTexts:
    rsPortRLMonitorTable.setStatus("current")
_RsPortRLMonitorEntry_Object = MibTableRow
rsPortRLMonitorEntry = _RsPortRLMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 25, 1, 1)
)
if mibBuilder.loadTexts:
    rsPortRLMonitorEntry.setStatus("current")
_RsPortRLExceedByteCount_Type = Counter32
_RsPortRLExceedByteCount_Object = MibTableColumn
rsPortRLExceedByteCount = _RsPortRLExceedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 25, 1, 1, 1),
    _RsPortRLExceedByteCount_Type()
)
rsPortRLExceedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortRLExceedByteCount.setStatus("current")
_RsPortRLCounterDiscontinuityTime_Type = TimeTicks
_RsPortRLCounterDiscontinuityTime_Object = MibTableColumn
rsPortRLCounterDiscontinuityTime = _RsPortRLCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 25, 1, 1, 2),
    _RsPortRLCounterDiscontinuityTime_Type()
)
rsPortRLCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortRLCounterDiscontinuityTime.setStatus("current")
_RsPortRLExceedPacketCount_Type = Counter32
_RsPortRLExceedPacketCount_Object = MibTableColumn
rsPortRLExceedPacketCount = _RsPortRLExceedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 25, 1, 1, 3),
    _RsPortRLExceedPacketCount_Type()
)
rsPortRLExceedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortRLExceedPacketCount.setStatus("current")
_RsL2RateLimit_ObjectIdentity = ObjectIdentity
rsL2RateLimit = _RsL2RateLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 26)
)
if mibBuilder.loadTexts:
    rsL2RateLimit.setStatus("current")
_RsL2RLApplyLastChanged_Type = TimeTicks
_RsL2RLApplyLastChanged_Object = MibScalar
rsL2RLApplyLastChanged = _RsL2RLApplyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 26, 1),
    _RsL2RLApplyLastChanged_Type()
)
rsL2RLApplyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsL2RLApplyLastChanged.setStatus("current")
_RsL2RLApplyCount_Type = Unsigned32
_RsL2RLApplyCount_Object = MibScalar
rsL2RLApplyCount = _RsL2RLApplyCount_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 26, 2),
    _RsL2RLApplyCount_Type()
)
rsL2RLApplyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsL2RLApplyCount.setStatus("current")
_RsL2RLApplyErrorMessage_Type = SnmpAdminString
_RsL2RLApplyErrorMessage_Object = MibScalar
rsL2RLApplyErrorMessage = _RsL2RLApplyErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 26, 3),
    _RsL2RLApplyErrorMessage_Type()
)
rsL2RLApplyErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsL2RLApplyErrorMessage.setStatus("current")


class _RsL2RLApplyMasterAdminStatus_Type(RsAdminStatus):
    """Custom type rsL2RLApplyMasterAdminStatus based on RsAdminStatus"""


_RsL2RLApplyMasterAdminStatus_Object = MibScalar
rsL2RLApplyMasterAdminStatus = _RsL2RLApplyMasterAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 26, 4),
    _RsL2RLApplyMasterAdminStatus_Type()
)
rsL2RLApplyMasterAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsL2RLApplyMasterAdminStatus.setStatus("current")
_RsL2RLApplyTable_Object = MibTable
rsL2RLApplyTable = _RsL2RLApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 26, 5)
)
if mibBuilder.loadTexts:
    rsL2RLApplyTable.setStatus("current")
_RsL2RLApplyEntry_Object = MibTableRow
rsL2RLApplyEntry = _RsL2RLApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 26, 5, 1)
)
rsL2RLApplyEntry.setIndexNames(
    (0, "RIVERSTONE-RATELIMIT-MIB", "rsTBMeterId"),
    (0, "RIVERSTONE-RATELIMIT-MIB", "rsL2RLApplyDirection"),
    (0, "RIVERSTONE-RATELIMIT-MIB", "rsL2RLApplyIfIndex"),
    (0, "RIVERSTONE-RATELIMIT-MIB", "rsL2RLApplyPortGroupName"),
    (0, "RIVERSTONE-RATELIMIT-MIB", "rsL2RLApplyFilterName"),
)
if mibBuilder.loadTexts:
    rsL2RLApplyEntry.setStatus("current")


class _RsL2RLApplyDirection_Type(RsIfDirection):
    """Custom type rsL2RLApplyDirection based on RsIfDirection"""
    subtypeSpec = RsIfDirection.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_RsL2RLApplyDirection_Type.__name__ = "RsIfDirection"
_RsL2RLApplyDirection_Object = MibTableColumn
rsL2RLApplyDirection = _RsL2RLApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 26, 5, 1, 1),
    _RsL2RLApplyDirection_Type()
)
rsL2RLApplyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsL2RLApplyDirection.setStatus("current")
_RsL2RLApplyIfIndex_Type = InterfaceIndexOrZero
_RsL2RLApplyIfIndex_Object = MibTableColumn
rsL2RLApplyIfIndex = _RsL2RLApplyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 26, 5, 1, 2),
    _RsL2RLApplyIfIndex_Type()
)
rsL2RLApplyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsL2RLApplyIfIndex.setStatus("current")
_RsL2RLApplyPortGroupName_Type = RsLabel
_RsL2RLApplyPortGroupName_Object = MibTableColumn
rsL2RLApplyPortGroupName = _RsL2RLApplyPortGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 26, 5, 1, 3),
    _RsL2RLApplyPortGroupName_Type()
)
rsL2RLApplyPortGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsL2RLApplyPortGroupName.setStatus("current")
_RsL2RLApplyFilterName_Type = RsLabel
_RsL2RLApplyFilterName_Object = MibTableColumn
rsL2RLApplyFilterName = _RsL2RLApplyFilterName_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 26, 5, 1, 4),
    _RsL2RLApplyFilterName_Type()
)
rsL2RLApplyFilterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsL2RLApplyFilterName.setStatus("current")
_RsL2RLIsFilterGroup_Type = TruthValue
_RsL2RLIsFilterGroup_Object = MibTableColumn
rsL2RLIsFilterGroup = _RsL2RLIsFilterGroup_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 26, 5, 1, 5),
    _RsL2RLIsFilterGroup_Type()
)
rsL2RLIsFilterGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsL2RLIsFilterGroup.setStatus("current")


class _RsL2RLApplyOnePGrouping_Type(Integer32):
    """Custom type rsL2RLApplyOnePGrouping based on Integer32"""
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
        *(("group1", 2),
          ("group2", 3),
          ("group3", 4),
          ("group4", 5),
          ("none", 0),
          ("other", 1))
    )


_RsL2RLApplyOnePGrouping_Type.__name__ = "Integer32"
_RsL2RLApplyOnePGrouping_Object = MibTableColumn
rsL2RLApplyOnePGrouping = _RsL2RLApplyOnePGrouping_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 26, 5, 1, 6),
    _RsL2RLApplyOnePGrouping_Type()
)
rsL2RLApplyOnePGrouping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsL2RLApplyOnePGrouping.setStatus("current")


class _RsL2RLApplyOwner_Type(SnmpAdminString):
    """Custom type rsL2RLApplyOwner based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RsL2RLApplyOwner_Type.__name__ = "SnmpAdminString"
_RsL2RLApplyOwner_Object = MibTableColumn
rsL2RLApplyOwner = _RsL2RLApplyOwner_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 26, 5, 1, 7),
    _RsL2RLApplyOwner_Type()
)
rsL2RLApplyOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsL2RLApplyOwner.setStatus("current")


class _RsL2RLApplyAdminStatus_Type(RsAdminStatus):
    """Custom type rsL2RLApplyAdminStatus based on RsAdminStatus"""


_RsL2RLApplyAdminStatus_Object = MibTableColumn
rsL2RLApplyAdminStatus = _RsL2RLApplyAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 26, 5, 1, 8),
    _RsL2RLApplyAdminStatus_Type()
)
rsL2RLApplyAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsL2RLApplyAdminStatus.setStatus("current")


class _RsL2RLApplyStorageType_Type(StorageType):
    """Custom type rsL2RLApplyStorageType based on StorageType"""
    defaultValue = 2

    subtypeSpec = StorageType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonVolatile", 3),
          ("volatile", 2))
    )


_RsL2RLApplyStorageType_Type.__name__ = "StorageType"
_RsL2RLApplyStorageType_Object = MibTableColumn
rsL2RLApplyStorageType = _RsL2RLApplyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 26, 5, 1, 9),
    _RsL2RLApplyStorageType_Type()
)
rsL2RLApplyStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsL2RLApplyStorageType.setStatus("current")
_RsL2RLApplyStatus_Type = RowStatus
_RsL2RLApplyStatus_Object = MibTableColumn
rsL2RLApplyStatus = _RsL2RLApplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 26, 5, 1, 10),
    _RsL2RLApplyStatus_Type()
)
rsL2RLApplyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsL2RLApplyStatus.setStatus("current")
_RsL2RLMonitor_ObjectIdentity = ObjectIdentity
rsL2RLMonitor = _RsL2RLMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 29)
)
if mibBuilder.loadTexts:
    rsL2RLMonitor.setStatus("current")
_RsL2RLMonitorTable_Object = MibTable
rsL2RLMonitorTable = _RsL2RLMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 29, 1)
)
if mibBuilder.loadTexts:
    rsL2RLMonitorTable.setStatus("current")
_RsL2RLMonitorEntry_Object = MibTableRow
rsL2RLMonitorEntry = _RsL2RLMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 29, 1, 1)
)
if mibBuilder.loadTexts:
    rsL2RLMonitorEntry.setStatus("current")
_RsL2RLExceedByteCount_Type = Counter32
_RsL2RLExceedByteCount_Object = MibTableColumn
rsL2RLExceedByteCount = _RsL2RLExceedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 29, 1, 1, 1),
    _RsL2RLExceedByteCount_Type()
)
rsL2RLExceedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsL2RLExceedByteCount.setStatus("current")
_RsL2RLExceedPacketCount_Type = Counter32
_RsL2RLExceedPacketCount_Object = MibTableColumn
rsL2RLExceedPacketCount = _RsL2RLExceedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 29, 1, 1, 2),
    _RsL2RLExceedPacketCount_Type()
)
rsL2RLExceedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsL2RLExceedPacketCount.setStatus("current")
_RsL2RLCounterDiscontinuityTime_Type = TimeTicks
_RsL2RLCounterDiscontinuityTime_Object = MibTableColumn
rsL2RLCounterDiscontinuityTime = _RsL2RLCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 29, 1, 1, 3),
    _RsL2RLCounterDiscontinuityTime_Type()
)
rsL2RLCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsL2RLCounterDiscontinuityTime.setStatus("current")
_RsRateLimitModes_ObjectIdentity = ObjectIdentity
rsRateLimitModes = _RsRateLimitModes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 30)
)
if mibBuilder.loadTexts:
    rsRateLimitModes.setStatus("current")
_RsRLModeLastChanged_Type = TimeTicks
_RsRLModeLastChanged_Object = MibScalar
rsRLModeLastChanged = _RsRLModeLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 30, 1),
    _RsRLModeLastChanged_Type()
)
rsRLModeLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRLModeLastChanged.setStatus("current")
_RsRLModeTable_Object = MibTable
rsRLModeTable = _RsRLModeTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 30, 2)
)
if mibBuilder.loadTexts:
    rsRLModeTable.setStatus("current")
_RsRLModeEntry_Object = MibTableRow
rsRLModeEntry = _RsRLModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 30, 2, 1)
)
rsRLModeEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    rsRLModeEntry.setStatus("current")


class _RsRLModeType_Type(Integer32):
    """Custom type rsRLModeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggregateMode", 2),
          ("flowMode", 1))
    )


_RsRLModeType_Type.__name__ = "Integer32"
_RsRLModeType_Object = MibTableColumn
rsRLModeType = _RsRLModeType_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 30, 2, 1, 1),
    _RsRLModeType_Type()
)
rsRLModeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRLModeType.setStatus("current")
_RsRLModeInputPortStatus_Type = RsAdminStatus
_RsRLModeInputPortStatus_Object = MibTableColumn
rsRLModeInputPortStatus = _RsRLModeInputPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 30, 2, 1, 2),
    _RsRLModeInputPortStatus_Type()
)
rsRLModeInputPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRLModeInputPortStatus.setStatus("current")


class _RsRLModeCapabilityBits_Type(Bits):
    """Custom type rsRLModeCapabilityBits based on Bits"""
    namedValues = NamedValues(
        *(("rlInputPortRateLimit", 1),
          ("rlMode", 0))
    )

_RsRLModeCapabilityBits_Type.__name__ = "Bits"
_RsRLModeCapabilityBits_Object = MibTableColumn
rsRLModeCapabilityBits = _RsRLModeCapabilityBits_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 30, 2, 1, 3),
    _RsRLModeCapabilityBits_Type()
)
rsRLModeCapabilityBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRLModeCapabilityBits.setStatus("current")
_RsRLModeEntryLastChanged_Type = TimeTicks
_RsRLModeEntryLastChanged_Object = MibTableColumn
rsRLModeEntryLastChanged = _RsRLModeEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 30, 2, 1, 4),
    _RsRLModeEntryLastChanged_Type()
)
rsRLModeEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRLModeEntryLastChanged.setStatus("current")


class _RsRLModeStorageType_Type(StorageType):
    """Custom type rsRLModeStorageType based on StorageType"""
    defaultValue = 2

    subtypeSpec = StorageType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonVolatile", 3),
          ("volatile", 2))
    )


_RsRLModeStorageType_Type.__name__ = "StorageType"
_RsRLModeStorageType_Object = MibTableColumn
rsRLModeStorageType = _RsRLModeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 30, 2, 1, 5),
    _RsRLModeStorageType_Type()
)
rsRLModeStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRLModeStorageType.setStatus("current")
_RsRateLimitGroups_ObjectIdentity = ObjectIdentity
rsRateLimitGroups = _RsRateLimitGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 33)
)
if mibBuilder.loadTexts:
    rsRateLimitGroups.setStatus("current")
_RsRLPortGroupLastChanged_Type = TimeTicks
_RsRLPortGroupLastChanged_Object = MibScalar
rsRLPortGroupLastChanged = _RsRLPortGroupLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 33, 1),
    _RsRLPortGroupLastChanged_Type()
)
rsRLPortGroupLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRLPortGroupLastChanged.setStatus("current")
_RsRLPortGroupTable_Object = MibTable
rsRLPortGroupTable = _RsRLPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 33, 2)
)
if mibBuilder.loadTexts:
    rsRLPortGroupTable.setStatus("current")
_RsRLPortGroupEntry_Object = MibTableRow
rsRLPortGroupEntry = _RsRLPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 33, 2, 1)
)
rsRLPortGroupEntry.setIndexNames(
    (0, "RIVERSTONE-RATELIMIT-MIB", "rsRLPortGroupName"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rsRLPortGroupEntry.setStatus("current")
_RsRLPortGroupName_Type = RsLabel
_RsRLPortGroupName_Object = MibTableColumn
rsRLPortGroupName = _RsRLPortGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 33, 2, 1, 1),
    _RsRLPortGroupName_Type()
)
rsRLPortGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsRLPortGroupName.setStatus("current")


class _RsRLPortGroupStorageType_Type(StorageType):
    """Custom type rsRLPortGroupStorageType based on StorageType"""
    subtypeSpec = StorageType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonVolatile", 3),
          ("volatile", 2))
    )


_RsRLPortGroupStorageType_Type.__name__ = "StorageType"
_RsRLPortGroupStorageType_Object = MibTableColumn
rsRLPortGroupStorageType = _RsRLPortGroupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 33, 2, 1, 2),
    _RsRLPortGroupStorageType_Type()
)
rsRLPortGroupStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRLPortGroupStorageType.setStatus("current")
_RsRLPortGroupStatus_Type = RowStatus
_RsRLPortGroupStatus_Object = MibTableColumn
rsRLPortGroupStatus = _RsRLPortGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 33, 2, 1, 3),
    _RsRLPortGroupStatus_Type()
)
rsRLPortGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsRLPortGroupStatus.setStatus("current")
_RsRLFilterGroupLastChanged_Type = TimeTicks
_RsRLFilterGroupLastChanged_Object = MibScalar
rsRLFilterGroupLastChanged = _RsRLFilterGroupLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 33, 3),
    _RsRLFilterGroupLastChanged_Type()
)
rsRLFilterGroupLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRLFilterGroupLastChanged.setStatus("current")
_RsRLFilterGroupTable_Object = MibTable
rsRLFilterGroupTable = _RsRLFilterGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 33, 4)
)
if mibBuilder.loadTexts:
    rsRLFilterGroupTable.setStatus("current")
_RsRLFilterGroupEntry_Object = MibTableRow
rsRLFilterGroupEntry = _RsRLFilterGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 33, 4, 1)
)
rsRLFilterGroupEntry.setIndexNames(
    (0, "RIVERSTONE-RATELIMIT-MIB", "rsRLFilterGroupName"),
    (0, "RIVERSTONE-RATELIMIT-MIB", "rsRLFilterName"),
)
if mibBuilder.loadTexts:
    rsRLFilterGroupEntry.setStatus("current")
_RsRLFilterGroupName_Type = RsLabel
_RsRLFilterGroupName_Object = MibTableColumn
rsRLFilterGroupName = _RsRLFilterGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 33, 4, 1, 1),
    _RsRLFilterGroupName_Type()
)
rsRLFilterGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsRLFilterGroupName.setStatus("current")
_RsRLFilterName_Type = RsLabel
_RsRLFilterName_Object = MibTableColumn
rsRLFilterName = _RsRLFilterName_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 33, 4, 1, 2),
    _RsRLFilterName_Type()
)
rsRLFilterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsRLFilterName.setStatus("current")


class _RsRLFilterGroupStorageType_Type(StorageType):
    """Custom type rsRLFilterGroupStorageType based on StorageType"""
    subtypeSpec = StorageType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonVolatile", 3),
          ("volatile", 2))
    )


_RsRLFilterGroupStorageType_Type.__name__ = "StorageType"
_RsRLFilterGroupStorageType_Object = MibTableColumn
rsRLFilterGroupStorageType = _RsRLFilterGroupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 33, 4, 1, 3),
    _RsRLFilterGroupStorageType_Type()
)
rsRLFilterGroupStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRLFilterGroupStorageType.setStatus("current")
_RsRLFilterGroupStatus_Type = RowStatus
_RsRLFilterGroupStatus_Object = MibTableColumn
rsRLFilterGroupStatus = _RsRLFilterGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 33, 4, 1, 4),
    _RsRLFilterGroupStatus_Type()
)
rsRLFilterGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsRLFilterGroupStatus.setStatus("current")
_RsRateLimitConformance_ObjectIdentity = ObjectIdentity
rsRateLimitConformance = _RsRateLimitConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 35)
)
if mibBuilder.loadTexts:
    rsRateLimitConformance.setStatus("current")
_RsRateLimitCompliances_ObjectIdentity = ObjectIdentity
rsRateLimitCompliances = _RsRateLimitCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 35, 1)
)
_RsRateLimitGroup_ObjectIdentity = ObjectIdentity
rsRateLimitGroup = _RsRateLimitGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 35, 2)
)
rsTBMeterApplyEntry.registerAugmentions(
    ("RIVERSTONE-RATELIMIT-MIB",
     "rsTBMeterMonitorEntry")
)
rsTBMeterMonitorEntry.setIndexNames(*rsTBMeterApplyEntry.getIndexNames())
rsPortRLEntry.registerAugmentions(
    ("RIVERSTONE-RATELIMIT-MIB",
     "rsPortRLMonitorEntry")
)
rsPortRLMonitorEntry.setIndexNames(*rsPortRLEntry.getIndexNames())
rsL2RLApplyEntry.registerAugmentions(
    ("RIVERSTONE-RATELIMIT-MIB",
     "rsL2RLMonitorEntry")
)
rsL2RLMonitorEntry.setIndexNames(*rsL2RLApplyEntry.getIndexNames())

# Managed Objects groups

rsRateLimitGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 35, 2, 1)
)
rsRateLimitGroup1.setObjects(
      *(("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterLastChanged"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterCount"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterErrorMessage"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterType"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterRate"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterBurst"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterFailAction"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterFailActionRewrite"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterBurstFailActionRewrite"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterStorageType"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterStatus"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterApplyLastChanged"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterApplyCount"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterApplyErrorMessage"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterApplyMasterAdminStatus"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterApplyOwner"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterApplyAdminStatus"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterApplyStorageType"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterApplyStatus"))
)
if mibBuilder.loadTexts:
    rsRateLimitGroup1.setStatus("current")

rsRateLimitGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 35, 2, 2)
)
rsRateLimitGroup2.setObjects(
      *(("RIVERSTONE-RATELIMIT-MIB", "rsPortRLLastChanged"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsPortRLCount"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsPortRLErrorMessage"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsPortRLMasterAdminStatus"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsPortRLOwner"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsPortRLRate"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsPortRLFailAction"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsPortRLFailActionRewrite"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsPortRLAdminStatus"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsPortRLStorageType"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsPortRLStatus"))
)
if mibBuilder.loadTexts:
    rsRateLimitGroup2.setStatus("current")

rsRateLimitGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 35, 2, 3)
)
rsRateLimitGroup3.setObjects(
      *(("RIVERSTONE-RATELIMIT-MIB", "rsRLModeLastChanged"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsRLModeType"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsRLModeCapabilityBits"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsRLModeInputPortStatus"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsRLModeEntryLastChanged"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsRLModeStorageType"))
)
if mibBuilder.loadTexts:
    rsRateLimitGroup3.setStatus("current")

rsRateLimitGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 35, 2, 4)
)
rsRateLimitGroup4.setObjects(
      *(("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterBurstFailAction"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterMinimumBandwidth"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterDistributeAmong"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterInterval"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsPortRLInterval"))
)
if mibBuilder.loadTexts:
    rsRateLimitGroup4.setStatus("deprecated")

rsRateLimitGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 35, 2, 5)
)
rsRateLimitGroup5.setObjects(
      *(("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterExceedByteCount"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterCounterDiscontinuityTime"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsPortRLExceedByteCount"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsPortRLCounterDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    rsRateLimitGroup5.setStatus("deprecated")

rsRateLimitGroup4V2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 35, 2, 6)
)
rsRateLimitGroup4V2.setObjects(
    ("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterBurstFailAction")
)
if mibBuilder.loadTexts:
    rsRateLimitGroup4V2.setStatus("current")

rsRateLimitGroup5V2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 35, 2, 7)
)
rsRateLimitGroup5V2.setObjects(
      *(("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterExceedByteCount"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterExceedPacketCount"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterCounterDiscontinuityTime"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsTBMeterExceedBurstPacketCount"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsPortRLExceedByteCount"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsPortRLExceedPacketCount"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsPortRLCounterDiscontinuityTime"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsL2RLExceedByteCount"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsL2RLExceedPacketCount"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsL2RLCounterDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    rsRateLimitGroup5V2.setStatus("current")

rsRateLimitGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 35, 2, 8)
)
rsRateLimitGroup6.setObjects(
      *(("RIVERSTONE-RATELIMIT-MIB", "rsL2RLApplyLastChanged"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsL2RLApplyCount"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsL2RLApplyErrorMessage"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsL2RLApplyMasterAdminStatus"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsL2RLIsFilterGroup"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsL2RLApplyOnePGrouping"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsL2RLApplyOwner"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsL2RLApplyAdminStatus"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsL2RLApplyStorageType"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsL2RLApplyStatus"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsRLFilterGroupLastChanged"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsRLPortGroupStorageType"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsRLPortGroupStatus"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsRLPortGroupLastChanged"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsRLFilterGroupStorageType"),
        ("RIVERSTONE-RATELIMIT-MIB", "rsRLFilterGroupStatus"))
)
if mibBuilder.loadTexts:
    rsRateLimitGroup6.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsRateLimitCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 35, 1, 1)
)
if mibBuilder.loadTexts:
    rsRateLimitCompliance.setStatus(
        "deprecated"
    )

rsRateLimitComplianceV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5567, 2, 25, 35, 1, 2)
)
if mibBuilder.loadTexts:
    rsRateLimitComplianceV2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RIVERSTONE-RATELIMIT-MIB",
    **{"RsRateLimit": RsRateLimit,
       "RsBurst": RsBurst,
       "RsAdminStatus": RsAdminStatus,
       "RsDistAmong": RsDistAmong,
       "RsMeterType": RsMeterType,
       "RsMeterInterval": RsMeterInterval,
       "RsLabel": RsLabel,
       "RsTOS": RsTOS,
       "RsIfDirection": RsIfDirection,
       "RsAction": RsAction,
       "rsRateLimitMIB": rsRateLimitMIB,
       "rsRateLimitNotifications": rsRateLimitNotifications,
       "rsTBMeter": rsTBMeter,
       "rsTBMeterLastChanged": rsTBMeterLastChanged,
       "rsTBMeterCount": rsTBMeterCount,
       "rsTBMeterErrorMessage": rsTBMeterErrorMessage,
       "rsTBMeterTable": rsTBMeterTable,
       "rsTBMeterEntry": rsTBMeterEntry,
       "rsTBMeterId": rsTBMeterId,
       "rsTBMeterType": rsTBMeterType,
       "rsTBMeterRate": rsTBMeterRate,
       "rsTBMeterBurst": rsTBMeterBurst,
       "rsTBMeterInterval": rsTBMeterInterval,
       "rsTBMeterFailAction": rsTBMeterFailAction,
       "rsTBMeterFailActionRewrite": rsTBMeterFailActionRewrite,
       "rsTBMeterBurstFailAction": rsTBMeterBurstFailAction,
       "rsTBMeterBurstFailActionRewrite": rsTBMeterBurstFailActionRewrite,
       "rsTBMeterMinimumBandwidth": rsTBMeterMinimumBandwidth,
       "rsTBMeterDistributeAmong": rsTBMeterDistributeAmong,
       "rsTBMeterStorageType": rsTBMeterStorageType,
       "rsTBMeterStatus": rsTBMeterStatus,
       "rsTBMeterApply": rsTBMeterApply,
       "rsTBMeterApplyLastChanged": rsTBMeterApplyLastChanged,
       "rsTBMeterApplyCount": rsTBMeterApplyCount,
       "rsTBMeterApplyErrorMessage": rsTBMeterApplyErrorMessage,
       "rsTBMeterApplyMasterAdminStatus": rsTBMeterApplyMasterAdminStatus,
       "rsTBMeterApplyTable": rsTBMeterApplyTable,
       "rsTBMeterApplyEntry": rsTBMeterApplyEntry,
       "rsTBMeterApplyDirection": rsTBMeterApplyDirection,
       "rsTBMeterApplyAclName": rsTBMeterApplyAclName,
       "rsTBMeterId2": rsTBMeterId2,
       "rsTBMeterApplyOwner": rsTBMeterApplyOwner,
       "rsTBMeterApplyAdminStatus": rsTBMeterApplyAdminStatus,
       "rsTBMeterApplyStorageType": rsTBMeterApplyStorageType,
       "rsTBMeterApplyStatus": rsTBMeterApplyStatus,
       "rsTBMeterApplyMonitor": rsTBMeterApplyMonitor,
       "rsTBMeterMonitorTable": rsTBMeterMonitorTable,
       "rsTBMeterMonitorEntry": rsTBMeterMonitorEntry,
       "rsTBMeterExceedByteCount": rsTBMeterExceedByteCount,
       "rsTBMeterCounterDiscontinuityTime": rsTBMeterCounterDiscontinuityTime,
       "rsTBMeterExceedPacketCount": rsTBMeterExceedPacketCount,
       "rsTBMeterExceedBurstPacketCount": rsTBMeterExceedBurstPacketCount,
       "rsPortRateLimit": rsPortRateLimit,
       "rsPortRLLastChanged": rsPortRLLastChanged,
       "rsPortRLCount": rsPortRLCount,
       "rsPortRLErrorMessage": rsPortRLErrorMessage,
       "rsPortRLMasterAdminStatus": rsPortRLMasterAdminStatus,
       "rsPortRLTable": rsPortRLTable,
       "rsPortRLEntry": rsPortRLEntry,
       "rsPortRLDirection": rsPortRLDirection,
       "rsPortRLMeterId": rsPortRLMeterId,
       "rsPortRLOwner": rsPortRLOwner,
       "rsPortRLRate": rsPortRLRate,
       "rsPortRLFailAction": rsPortRLFailAction,
       "rsPortRLFailActionRewrite": rsPortRLFailActionRewrite,
       "rsPortRLInterval": rsPortRLInterval,
       "rsPortRLAdminStatus": rsPortRLAdminStatus,
       "rsPortRLStorageType": rsPortRLStorageType,
       "rsPortRLStatus": rsPortRLStatus,
       "rsPortRLMonitor": rsPortRLMonitor,
       "rsPortRLMonitorTable": rsPortRLMonitorTable,
       "rsPortRLMonitorEntry": rsPortRLMonitorEntry,
       "rsPortRLExceedByteCount": rsPortRLExceedByteCount,
       "rsPortRLCounterDiscontinuityTime": rsPortRLCounterDiscontinuityTime,
       "rsPortRLExceedPacketCount": rsPortRLExceedPacketCount,
       "rsL2RateLimit": rsL2RateLimit,
       "rsL2RLApplyLastChanged": rsL2RLApplyLastChanged,
       "rsL2RLApplyCount": rsL2RLApplyCount,
       "rsL2RLApplyErrorMessage": rsL2RLApplyErrorMessage,
       "rsL2RLApplyMasterAdminStatus": rsL2RLApplyMasterAdminStatus,
       "rsL2RLApplyTable": rsL2RLApplyTable,
       "rsL2RLApplyEntry": rsL2RLApplyEntry,
       "rsL2RLApplyDirection": rsL2RLApplyDirection,
       "rsL2RLApplyIfIndex": rsL2RLApplyIfIndex,
       "rsL2RLApplyPortGroupName": rsL2RLApplyPortGroupName,
       "rsL2RLApplyFilterName": rsL2RLApplyFilterName,
       "rsL2RLIsFilterGroup": rsL2RLIsFilterGroup,
       "rsL2RLApplyOnePGrouping": rsL2RLApplyOnePGrouping,
       "rsL2RLApplyOwner": rsL2RLApplyOwner,
       "rsL2RLApplyAdminStatus": rsL2RLApplyAdminStatus,
       "rsL2RLApplyStorageType": rsL2RLApplyStorageType,
       "rsL2RLApplyStatus": rsL2RLApplyStatus,
       "rsL2RLMonitor": rsL2RLMonitor,
       "rsL2RLMonitorTable": rsL2RLMonitorTable,
       "rsL2RLMonitorEntry": rsL2RLMonitorEntry,
       "rsL2RLExceedByteCount": rsL2RLExceedByteCount,
       "rsL2RLExceedPacketCount": rsL2RLExceedPacketCount,
       "rsL2RLCounterDiscontinuityTime": rsL2RLCounterDiscontinuityTime,
       "rsRateLimitModes": rsRateLimitModes,
       "rsRLModeLastChanged": rsRLModeLastChanged,
       "rsRLModeTable": rsRLModeTable,
       "rsRLModeEntry": rsRLModeEntry,
       "rsRLModeType": rsRLModeType,
       "rsRLModeInputPortStatus": rsRLModeInputPortStatus,
       "rsRLModeCapabilityBits": rsRLModeCapabilityBits,
       "rsRLModeEntryLastChanged": rsRLModeEntryLastChanged,
       "rsRLModeStorageType": rsRLModeStorageType,
       "rsRateLimitGroups": rsRateLimitGroups,
       "rsRLPortGroupLastChanged": rsRLPortGroupLastChanged,
       "rsRLPortGroupTable": rsRLPortGroupTable,
       "rsRLPortGroupEntry": rsRLPortGroupEntry,
       "rsRLPortGroupName": rsRLPortGroupName,
       "rsRLPortGroupStorageType": rsRLPortGroupStorageType,
       "rsRLPortGroupStatus": rsRLPortGroupStatus,
       "rsRLFilterGroupLastChanged": rsRLFilterGroupLastChanged,
       "rsRLFilterGroupTable": rsRLFilterGroupTable,
       "rsRLFilterGroupEntry": rsRLFilterGroupEntry,
       "rsRLFilterGroupName": rsRLFilterGroupName,
       "rsRLFilterName": rsRLFilterName,
       "rsRLFilterGroupStorageType": rsRLFilterGroupStorageType,
       "rsRLFilterGroupStatus": rsRLFilterGroupStatus,
       "rsRateLimitConformance": rsRateLimitConformance,
       "rsRateLimitCompliances": rsRateLimitCompliances,
       "rsRateLimitCompliance": rsRateLimitCompliance,
       "rsRateLimitComplianceV2": rsRateLimitComplianceV2,
       "rsRateLimitGroup": rsRateLimitGroup,
       "rsRateLimitGroup1": rsRateLimitGroup1,
       "rsRateLimitGroup2": rsRateLimitGroup2,
       "rsRateLimitGroup3": rsRateLimitGroup3,
       "rsRateLimitGroup4": rsRateLimitGroup4,
       "rsRateLimitGroup5": rsRateLimitGroup5,
       "rsRateLimitGroup4V2": rsRateLimitGroup4V2,
       "rsRateLimitGroup5V2": rsRateLimitGroup5V2,
       "rsRateLimitGroup6": rsRateLimitGroup6}
)
