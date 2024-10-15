# SNMP MIB module (T11-FC-FSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/T11-FC-FSPF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:30 2024
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

(FcDomainIdOrZero,
 fcmInstanceIndex,
 fcmSwitchIndex) = mibBuilder.importSymbols(
    "FC-MGMT-MIB",
    "FcDomainIdOrZero",
    "fcmInstanceIndex",
    "fcmSwitchIndex")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

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

(t11FamConfigDomainId,) = mibBuilder.importSymbols(
    "T11-FC-FABRIC-ADDR-MGR-MIB",
    "t11FamConfigDomainId")

(T11FabricIndex,) = mibBuilder.importSymbols(
    "T11-TC-MIB",
    "T11FabricIndex")


# MODULE-IDENTITY

t11FcFspfMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 143)
)
t11FcFspfMIB.setRevisions(
        ("2006-08-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class T11FspfLsrType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class T11FspfLinkType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class T11FspfInterfaceState(Integer32, TextualConvention):
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
        *(("dbAckwait", 4),
          ("dbExchange", 3),
          ("dbWait", 5),
          ("down", 1),
          ("full", 6),
          ("init", 2))
    )



class T11FspfLastCreationTime(TimeTicks, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_T11FspfNotifications_ObjectIdentity = ObjectIdentity
t11FspfNotifications = _T11FspfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 143, 0)
)
_T11FspfObjects_ObjectIdentity = ObjectIdentity
t11FspfObjects = _T11FspfObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 143, 1)
)
_T11FspfConfiguration_ObjectIdentity = ObjectIdentity
t11FspfConfiguration = _T11FspfConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 143, 1, 1)
)
_T11FspfTable_Object = MibTable
t11FspfTable = _T11FspfTable_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 1)
)
if mibBuilder.loadTexts:
    t11FspfTable.setStatus("current")
_T11FspfEntry_Object = MibTableRow
t11FspfEntry = _T11FspfEntry_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1)
)
t11FspfEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-FSPF-MIB", "t11FspfFabricIndex"),
)
if mibBuilder.loadTexts:
    t11FspfEntry.setStatus("current")
_T11FspfFabricIndex_Type = T11FabricIndex
_T11FspfFabricIndex_Object = MibTableColumn
t11FspfFabricIndex = _T11FspfFabricIndex_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 1),
    _T11FspfFabricIndex_Type()
)
t11FspfFabricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FspfFabricIndex.setStatus("current")


class _T11FspfMinLsArrival_Type(Unsigned32):
    """Custom type t11FspfMinLsArrival based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_T11FspfMinLsArrival_Type.__name__ = "Unsigned32"
_T11FspfMinLsArrival_Object = MibTableColumn
t11FspfMinLsArrival = _T11FspfMinLsArrival_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 2),
    _T11FspfMinLsArrival_Type()
)
t11FspfMinLsArrival.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FspfMinLsArrival.setStatus("current")
if mibBuilder.loadTexts:
    t11FspfMinLsArrival.setUnits("milliSeconds")


class _T11FspfMinLsInterval_Type(Unsigned32):
    """Custom type t11FspfMinLsInterval based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_T11FspfMinLsInterval_Type.__name__ = "Unsigned32"
_T11FspfMinLsInterval_Object = MibTableColumn
t11FspfMinLsInterval = _T11FspfMinLsInterval_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 3),
    _T11FspfMinLsInterval_Type()
)
t11FspfMinLsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FspfMinLsInterval.setStatus("current")
if mibBuilder.loadTexts:
    t11FspfMinLsInterval.setUnits("milliSeconds")


class _T11FspfLsRefreshTime_Type(Unsigned32):
    """Custom type t11FspfLsRefreshTime based on Unsigned32"""
    defaultValue = 30


_T11FspfLsRefreshTime_Object = MibTableColumn
t11FspfLsRefreshTime = _T11FspfLsRefreshTime_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 4),
    _T11FspfLsRefreshTime_Type()
)
t11FspfLsRefreshTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfLsRefreshTime.setStatus("current")
if mibBuilder.loadTexts:
    t11FspfLsRefreshTime.setUnits("Minutes")


class _T11FspfMaxAge_Type(Unsigned32):
    """Custom type t11FspfMaxAge based on Unsigned32"""
    defaultValue = 60


_T11FspfMaxAge_Object = MibTableColumn
t11FspfMaxAge = _T11FspfMaxAge_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 5),
    _T11FspfMaxAge_Type()
)
t11FspfMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    t11FspfMaxAge.setUnits("Minutes")
_T11FspfMaxAgeDiscards_Type = Counter32
_T11FspfMaxAgeDiscards_Object = MibTableColumn
t11FspfMaxAgeDiscards = _T11FspfMaxAgeDiscards_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 6),
    _T11FspfMaxAgeDiscards_Type()
)
t11FspfMaxAgeDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfMaxAgeDiscards.setStatus("current")
_T11FspfPathComputations_Type = Counter32
_T11FspfPathComputations_Object = MibTableColumn
t11FspfPathComputations = _T11FspfPathComputations_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 7),
    _T11FspfPathComputations_Type()
)
t11FspfPathComputations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfPathComputations.setStatus("current")
_T11FspfChecksumErrors_Type = Counter32
_T11FspfChecksumErrors_Object = MibTableColumn
t11FspfChecksumErrors = _T11FspfChecksumErrors_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 8),
    _T11FspfChecksumErrors_Type()
)
t11FspfChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfChecksumErrors.setStatus("current")
_T11FspfLsrs_Type = Gauge32
_T11FspfLsrs_Object = MibTableColumn
t11FspfLsrs = _T11FspfLsrs_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 9),
    _T11FspfLsrs_Type()
)
t11FspfLsrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfLsrs.setStatus("current")
_T11FspfCreateTime_Type = T11FspfLastCreationTime
_T11FspfCreateTime_Object = MibTableColumn
t11FspfCreateTime = _T11FspfCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 10),
    _T11FspfCreateTime_Type()
)
t11FspfCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfCreateTime.setStatus("current")


class _T11FspfAdminStatus_Type(Integer32):
    """Custom type t11FspfAdminStatus based on Integer32"""
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


_T11FspfAdminStatus_Type.__name__ = "Integer32"
_T11FspfAdminStatus_Object = MibTableColumn
t11FspfAdminStatus = _T11FspfAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 11),
    _T11FspfAdminStatus_Type()
)
t11FspfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FspfAdminStatus.setStatus("current")


class _T11FspfOperStatus_Type(Integer32):
    """Custom type t11FspfOperStatus based on Integer32"""
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


_T11FspfOperStatus_Type.__name__ = "Integer32"
_T11FspfOperStatus_Object = MibTableColumn
t11FspfOperStatus = _T11FspfOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 12),
    _T11FspfOperStatus_Type()
)
t11FspfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfOperStatus.setStatus("current")


class _T11FspfNbrStateChangNotifyEnable_Type(TruthValue):
    """Custom type t11FspfNbrStateChangNotifyEnable based on TruthValue"""


_T11FspfNbrStateChangNotifyEnable_Object = MibTableColumn
t11FspfNbrStateChangNotifyEnable = _T11FspfNbrStateChangNotifyEnable_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 13),
    _T11FspfNbrStateChangNotifyEnable_Type()
)
t11FspfNbrStateChangNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FspfNbrStateChangNotifyEnable.setStatus("current")


class _T11FspfSetToDefault_Type(Integer32):
    """Custom type t11FspfSetToDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("noOp", 2))
    )


_T11FspfSetToDefault_Type.__name__ = "Integer32"
_T11FspfSetToDefault_Object = MibTableColumn
t11FspfSetToDefault = _T11FspfSetToDefault_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 14),
    _T11FspfSetToDefault_Type()
)
t11FspfSetToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FspfSetToDefault.setStatus("current")


class _T11FspfStorageType_Type(StorageType):
    """Custom type t11FspfStorageType based on StorageType"""


_T11FspfStorageType_Object = MibTableColumn
t11FspfStorageType = _T11FspfStorageType_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 15),
    _T11FspfStorageType_Type()
)
t11FspfStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FspfStorageType.setStatus("current")
_T11FspfIfTable_Object = MibTable
t11FspfIfTable = _T11FspfIfTable_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 2)
)
if mibBuilder.loadTexts:
    t11FspfIfTable.setStatus("current")
_T11FspfIfEntry_Object = MibTableRow
t11FspfIfEntry = _T11FspfIfEntry_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1)
)
t11FspfIfEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-FSPF-MIB", "t11FspfFabricIndex"),
    (0, "T11-FC-FSPF-MIB", "t11FspfIfIndex"),
)
if mibBuilder.loadTexts:
    t11FspfIfEntry.setStatus("current")
_T11FspfIfIndex_Type = InterfaceIndex
_T11FspfIfIndex_Object = MibTableColumn
t11FspfIfIndex = _T11FspfIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 1),
    _T11FspfIfIndex_Type()
)
t11FspfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FspfIfIndex.setStatus("current")


class _T11FspfIfHelloInterval_Type(Unsigned32):
    """Custom type t11FspfIfHelloInterval based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_T11FspfIfHelloInterval_Type.__name__ = "Unsigned32"
_T11FspfIfHelloInterval_Object = MibTableColumn
t11FspfIfHelloInterval = _T11FspfIfHelloInterval_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 2),
    _T11FspfIfHelloInterval_Type()
)
t11FspfIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FspfIfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    t11FspfIfHelloInterval.setUnits("Seconds")


class _T11FspfIfDeadInterval_Type(Unsigned32):
    """Custom type t11FspfIfDeadInterval based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65535),
    )


_T11FspfIfDeadInterval_Type.__name__ = "Unsigned32"
_T11FspfIfDeadInterval_Object = MibTableColumn
t11FspfIfDeadInterval = _T11FspfIfDeadInterval_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 3),
    _T11FspfIfDeadInterval_Type()
)
t11FspfIfDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FspfIfDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    t11FspfIfDeadInterval.setUnits("Seconds")


class _T11FspfIfRetransmitInterval_Type(Unsigned32):
    """Custom type t11FspfIfRetransmitInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_T11FspfIfRetransmitInterval_Type.__name__ = "Unsigned32"
_T11FspfIfRetransmitInterval_Object = MibTableColumn
t11FspfIfRetransmitInterval = _T11FspfIfRetransmitInterval_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 4),
    _T11FspfIfRetransmitInterval_Type()
)
t11FspfIfRetransmitInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FspfIfRetransmitInterval.setStatus("current")
if mibBuilder.loadTexts:
    t11FspfIfRetransmitInterval.setUnits("Seconds")
_T11FspfIfInLsuPkts_Type = Counter32
_T11FspfIfInLsuPkts_Object = MibTableColumn
t11FspfIfInLsuPkts = _T11FspfIfInLsuPkts_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 5),
    _T11FspfIfInLsuPkts_Type()
)
t11FspfIfInLsuPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfIfInLsuPkts.setStatus("current")
_T11FspfIfInLsaPkts_Type = Counter32
_T11FspfIfInLsaPkts_Object = MibTableColumn
t11FspfIfInLsaPkts = _T11FspfIfInLsaPkts_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 6),
    _T11FspfIfInLsaPkts_Type()
)
t11FspfIfInLsaPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfIfInLsaPkts.setStatus("current")
_T11FspfIfOutLsuPkts_Type = Counter32
_T11FspfIfOutLsuPkts_Object = MibTableColumn
t11FspfIfOutLsuPkts = _T11FspfIfOutLsuPkts_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 7),
    _T11FspfIfOutLsuPkts_Type()
)
t11FspfIfOutLsuPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfIfOutLsuPkts.setStatus("current")
_T11FspfIfOutLsaPkts_Type = Counter32
_T11FspfIfOutLsaPkts_Object = MibTableColumn
t11FspfIfOutLsaPkts = _T11FspfIfOutLsaPkts_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 8),
    _T11FspfIfOutLsaPkts_Type()
)
t11FspfIfOutLsaPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfIfOutLsaPkts.setStatus("current")
_T11FspfIfOutHelloPkts_Type = Counter32
_T11FspfIfOutHelloPkts_Object = MibTableColumn
t11FspfIfOutHelloPkts = _T11FspfIfOutHelloPkts_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 9),
    _T11FspfIfOutHelloPkts_Type()
)
t11FspfIfOutHelloPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfIfOutHelloPkts.setStatus("current")
_T11FspfIfInHelloPkts_Type = Counter32
_T11FspfIfInHelloPkts_Object = MibTableColumn
t11FspfIfInHelloPkts = _T11FspfIfInHelloPkts_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 10),
    _T11FspfIfInHelloPkts_Type()
)
t11FspfIfInHelloPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfIfInHelloPkts.setStatus("current")
_T11FspfIfRetransmittedLsuPkts_Type = Counter32
_T11FspfIfRetransmittedLsuPkts_Object = MibTableColumn
t11FspfIfRetransmittedLsuPkts = _T11FspfIfRetransmittedLsuPkts_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 11),
    _T11FspfIfRetransmittedLsuPkts_Type()
)
t11FspfIfRetransmittedLsuPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfIfRetransmittedLsuPkts.setStatus("current")
_T11FspfIfInErrorPkts_Type = Counter32
_T11FspfIfInErrorPkts_Object = MibTableColumn
t11FspfIfInErrorPkts = _T11FspfIfInErrorPkts_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 12),
    _T11FspfIfInErrorPkts_Type()
)
t11FspfIfInErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfIfInErrorPkts.setStatus("current")
_T11FspfIfNbrState_Type = T11FspfInterfaceState
_T11FspfIfNbrState_Object = MibTableColumn
t11FspfIfNbrState = _T11FspfIfNbrState_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 13),
    _T11FspfIfNbrState_Type()
)
t11FspfIfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfIfNbrState.setStatus("current")
_T11FspfIfNbrDomainId_Type = FcDomainIdOrZero
_T11FspfIfNbrDomainId_Object = MibTableColumn
t11FspfIfNbrDomainId = _T11FspfIfNbrDomainId_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 14),
    _T11FspfIfNbrDomainId_Type()
)
t11FspfIfNbrDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfIfNbrDomainId.setStatus("current")


class _T11FspfIfNbrPortIndex_Type(Unsigned32):
    """Custom type t11FspfIfNbrPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_T11FspfIfNbrPortIndex_Type.__name__ = "Unsigned32"
_T11FspfIfNbrPortIndex_Object = MibTableColumn
t11FspfIfNbrPortIndex = _T11FspfIfNbrPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 15),
    _T11FspfIfNbrPortIndex_Type()
)
t11FspfIfNbrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfIfNbrPortIndex.setStatus("current")


class _T11FspfIfAdminStatus_Type(Integer32):
    """Custom type t11FspfIfAdminStatus based on Integer32"""
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


_T11FspfIfAdminStatus_Type.__name__ = "Integer32"
_T11FspfIfAdminStatus_Object = MibTableColumn
t11FspfIfAdminStatus = _T11FspfIfAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 16),
    _T11FspfIfAdminStatus_Type()
)
t11FspfIfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FspfIfAdminStatus.setStatus("current")
_T11FspfIfCreateTime_Type = T11FspfLastCreationTime
_T11FspfIfCreateTime_Object = MibTableColumn
t11FspfIfCreateTime = _T11FspfIfCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 17),
    _T11FspfIfCreateTime_Type()
)
t11FspfIfCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfIfCreateTime.setStatus("current")


class _T11FspfIfSetToDefault_Type(Integer32):
    """Custom type t11FspfIfSetToDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("noOp", 2))
    )


_T11FspfIfSetToDefault_Type.__name__ = "Integer32"
_T11FspfIfSetToDefault_Object = MibTableColumn
t11FspfIfSetToDefault = _T11FspfIfSetToDefault_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 18),
    _T11FspfIfSetToDefault_Type()
)
t11FspfIfSetToDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FspfIfSetToDefault.setStatus("current")


class _T11FspfIfLinkCostFactor_Type(Unsigned32):
    """Custom type t11FspfIfLinkCostFactor based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_T11FspfIfLinkCostFactor_Type.__name__ = "Unsigned32"
_T11FspfIfLinkCostFactor_Object = MibTableColumn
t11FspfIfLinkCostFactor = _T11FspfIfLinkCostFactor_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 19),
    _T11FspfIfLinkCostFactor_Type()
)
t11FspfIfLinkCostFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FspfIfLinkCostFactor.setStatus("current")


class _T11FspfIfStorageType_Type(StorageType):
    """Custom type t11FspfIfStorageType based on StorageType"""


_T11FspfIfStorageType_Object = MibTableColumn
t11FspfIfStorageType = _T11FspfIfStorageType_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 20),
    _T11FspfIfStorageType_Type()
)
t11FspfIfStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FspfIfStorageType.setStatus("current")
_T11FspfIfRowStatus_Type = RowStatus
_T11FspfIfRowStatus_Object = MibTableColumn
t11FspfIfRowStatus = _T11FspfIfRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 21),
    _T11FspfIfRowStatus_Type()
)
t11FspfIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FspfIfRowStatus.setStatus("current")
_T11FspfIfPrevNbrState_Type = T11FspfInterfaceState
_T11FspfIfPrevNbrState_Object = MibScalar
t11FspfIfPrevNbrState = _T11FspfIfPrevNbrState_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 1, 3),
    _T11FspfIfPrevNbrState_Type()
)
t11FspfIfPrevNbrState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    t11FspfIfPrevNbrState.setStatus("current")
_T11FspfDatabase_ObjectIdentity = ObjectIdentity
t11FspfDatabase = _T11FspfDatabase_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 143, 1, 2)
)
_T11FspfLsrTable_Object = MibTable
t11FspfLsrTable = _T11FspfLsrTable_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 2, 1)
)
if mibBuilder.loadTexts:
    t11FspfLsrTable.setStatus("current")
_T11FspfLsrEntry_Object = MibTableRow
t11FspfLsrEntry = _T11FspfLsrEntry_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 2, 1, 1)
)
t11FspfLsrEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-FSPF-MIB", "t11FspfFabricIndex"),
    (0, "T11-FC-FSPF-MIB", "t11FspfLsrDomainId"),
    (0, "T11-FC-FSPF-MIB", "t11FspfLsrType"),
)
if mibBuilder.loadTexts:
    t11FspfLsrEntry.setStatus("current")
_T11FspfLsrDomainId_Type = FcDomainIdOrZero
_T11FspfLsrDomainId_Object = MibTableColumn
t11FspfLsrDomainId = _T11FspfLsrDomainId_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 2, 1, 1, 1),
    _T11FspfLsrDomainId_Type()
)
t11FspfLsrDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FspfLsrDomainId.setStatus("current")
_T11FspfLsrType_Type = T11FspfLsrType
_T11FspfLsrType_Object = MibTableColumn
t11FspfLsrType = _T11FspfLsrType_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 2, 1, 1, 2),
    _T11FspfLsrType_Type()
)
t11FspfLsrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FspfLsrType.setStatus("current")
_T11FspfLsrAdvDomainId_Type = FcDomainIdOrZero
_T11FspfLsrAdvDomainId_Object = MibTableColumn
t11FspfLsrAdvDomainId = _T11FspfLsrAdvDomainId_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 2, 1, 1, 3),
    _T11FspfLsrAdvDomainId_Type()
)
t11FspfLsrAdvDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfLsrAdvDomainId.setStatus("current")


class _T11FspfLsrAge_Type(Unsigned32):
    """Custom type t11FspfLsrAge based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_T11FspfLsrAge_Type.__name__ = "Unsigned32"
_T11FspfLsrAge_Object = MibTableColumn
t11FspfLsrAge = _T11FspfLsrAge_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 2, 1, 1, 4),
    _T11FspfLsrAge_Type()
)
t11FspfLsrAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfLsrAge.setStatus("current")
if mibBuilder.loadTexts:
    t11FspfLsrAge.setUnits("Seconds")


class _T11FspfLsrIncarnationNumber_Type(Unsigned32):
    """Custom type t11FspfLsrIncarnationNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_T11FspfLsrIncarnationNumber_Type.__name__ = "Unsigned32"
_T11FspfLsrIncarnationNumber_Object = MibTableColumn
t11FspfLsrIncarnationNumber = _T11FspfLsrIncarnationNumber_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 2, 1, 1, 5),
    _T11FspfLsrIncarnationNumber_Type()
)
t11FspfLsrIncarnationNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfLsrIncarnationNumber.setStatus("current")


class _T11FspfLsrCheckSum_Type(Unsigned32):
    """Custom type t11FspfLsrCheckSum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_T11FspfLsrCheckSum_Type.__name__ = "Unsigned32"
_T11FspfLsrCheckSum_Object = MibTableColumn
t11FspfLsrCheckSum = _T11FspfLsrCheckSum_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 2, 1, 1, 6),
    _T11FspfLsrCheckSum_Type()
)
t11FspfLsrCheckSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfLsrCheckSum.setStatus("current")


class _T11FspfLsrLinks_Type(Unsigned32):
    """Custom type t11FspfLsrLinks based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65355),
    )


_T11FspfLsrLinks_Type.__name__ = "Unsigned32"
_T11FspfLsrLinks_Object = MibTableColumn
t11FspfLsrLinks = _T11FspfLsrLinks_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 2, 1, 1, 7),
    _T11FspfLsrLinks_Type()
)
t11FspfLsrLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfLsrLinks.setStatus("current")


class _T11FspfLinkNumber_Type(Unsigned32):
    """Custom type t11FspfLinkNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_T11FspfLinkNumber_Type.__name__ = "Unsigned32"
_T11FspfLinkNumber_Object = MibScalar
t11FspfLinkNumber = _T11FspfLinkNumber_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 2, 3),
    _T11FspfLinkNumber_Type()
)
t11FspfLinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfLinkNumber.setStatus("current")
_T11FspfLinkTable_Object = MibTable
t11FspfLinkTable = _T11FspfLinkTable_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 2, 4)
)
if mibBuilder.loadTexts:
    t11FspfLinkTable.setStatus("current")
_T11FspfLinkEntry_Object = MibTableRow
t11FspfLinkEntry = _T11FspfLinkEntry_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 2, 4, 1)
)
t11FspfLinkEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-FSPF-MIB", "t11FspfFabricIndex"),
    (0, "T11-FC-FSPF-MIB", "t11FspfLsrDomainId"),
    (0, "T11-FC-FSPF-MIB", "t11FspfLsrType"),
    (0, "T11-FC-FSPF-MIB", "t11FspfLinkIndex"),
)
if mibBuilder.loadTexts:
    t11FspfLinkEntry.setStatus("current")


class _T11FspfLinkIndex_Type(Unsigned32):
    """Custom type t11FspfLinkIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FspfLinkIndex_Type.__name__ = "Unsigned32"
_T11FspfLinkIndex_Object = MibTableColumn
t11FspfLinkIndex = _T11FspfLinkIndex_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 2, 4, 1, 1),
    _T11FspfLinkIndex_Type()
)
t11FspfLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FspfLinkIndex.setStatus("current")
_T11FspfLinkNbrDomainId_Type = FcDomainIdOrZero
_T11FspfLinkNbrDomainId_Object = MibTableColumn
t11FspfLinkNbrDomainId = _T11FspfLinkNbrDomainId_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 2, 4, 1, 2),
    _T11FspfLinkNbrDomainId_Type()
)
t11FspfLinkNbrDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfLinkNbrDomainId.setStatus("current")


class _T11FspfLinkPortIndex_Type(Unsigned32):
    """Custom type t11FspfLinkPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_T11FspfLinkPortIndex_Type.__name__ = "Unsigned32"
_T11FspfLinkPortIndex_Object = MibTableColumn
t11FspfLinkPortIndex = _T11FspfLinkPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 2, 4, 1, 3),
    _T11FspfLinkPortIndex_Type()
)
t11FspfLinkPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfLinkPortIndex.setStatus("current")


class _T11FspfLinkNbrPortIndex_Type(Unsigned32):
    """Custom type t11FspfLinkNbrPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_T11FspfLinkNbrPortIndex_Type.__name__ = "Unsigned32"
_T11FspfLinkNbrPortIndex_Object = MibTableColumn
t11FspfLinkNbrPortIndex = _T11FspfLinkNbrPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 2, 4, 1, 4),
    _T11FspfLinkNbrPortIndex_Type()
)
t11FspfLinkNbrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfLinkNbrPortIndex.setStatus("current")
_T11FspfLinkType_Type = T11FspfLinkType
_T11FspfLinkType_Object = MibTableColumn
t11FspfLinkType = _T11FspfLinkType_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 2, 4, 1, 5),
    _T11FspfLinkType_Type()
)
t11FspfLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfLinkType.setStatus("current")


class _T11FspfLinkCost_Type(Integer32):
    """Custom type t11FspfLinkCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_T11FspfLinkCost_Type.__name__ = "Integer32"
_T11FspfLinkCost_Object = MibTableColumn
t11FspfLinkCost = _T11FspfLinkCost_Object(
    (1, 3, 6, 1, 2, 1, 143, 1, 2, 4, 1, 6),
    _T11FspfLinkCost_Type()
)
t11FspfLinkCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FspfLinkCost.setStatus("current")
_T11FspfConformance_ObjectIdentity = ObjectIdentity
t11FspfConformance = _T11FspfConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 143, 2)
)
_T11FspfMIBCompliances_ObjectIdentity = ObjectIdentity
t11FspfMIBCompliances = _T11FspfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 143, 2, 1)
)
_T11FspfMIBGroups_ObjectIdentity = ObjectIdentity
t11FspfMIBGroups = _T11FspfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 143, 2, 2)
)

# Managed Objects groups

t11FspfGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 143, 2, 2, 1)
)
t11FspfGeneralGroup.setObjects(
      *(("T11-FC-FSPF-MIB", "t11FspfMinLsArrival"),
        ("T11-FC-FSPF-MIB", "t11FspfMinLsInterval"),
        ("T11-FC-FSPF-MIB", "t11FspfLsRefreshTime"),
        ("T11-FC-FSPF-MIB", "t11FspfMaxAge"),
        ("T11-FC-FSPF-MIB", "t11FspfMaxAgeDiscards"),
        ("T11-FC-FSPF-MIB", "t11FspfPathComputations"),
        ("T11-FC-FSPF-MIB", "t11FspfChecksumErrors"),
        ("T11-FC-FSPF-MIB", "t11FspfLsrs"),
        ("T11-FC-FSPF-MIB", "t11FspfCreateTime"),
        ("T11-FC-FSPF-MIB", "t11FspfAdminStatus"),
        ("T11-FC-FSPF-MIB", "t11FspfOperStatus"),
        ("T11-FC-FSPF-MIB", "t11FspfNbrStateChangNotifyEnable"),
        ("T11-FC-FSPF-MIB", "t11FspfSetToDefault"),
        ("T11-FC-FSPF-MIB", "t11FspfStorageType"))
)
if mibBuilder.loadTexts:
    t11FspfGeneralGroup.setStatus("current")

t11FspfIfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 143, 2, 2, 2)
)
t11FspfIfGroup.setObjects(
      *(("T11-FC-FSPF-MIB", "t11FspfIfHelloInterval"),
        ("T11-FC-FSPF-MIB", "t11FspfIfDeadInterval"),
        ("T11-FC-FSPF-MIB", "t11FspfIfRetransmitInterval"),
        ("T11-FC-FSPF-MIB", "t11FspfIfNbrState"),
        ("T11-FC-FSPF-MIB", "t11FspfIfNbrDomainId"),
        ("T11-FC-FSPF-MIB", "t11FspfIfNbrPortIndex"),
        ("T11-FC-FSPF-MIB", "t11FspfIfAdminStatus"),
        ("T11-FC-FSPF-MIB", "t11FspfIfCreateTime"),
        ("T11-FC-FSPF-MIB", "t11FspfIfSetToDefault"),
        ("T11-FC-FSPF-MIB", "t11FspfIfLinkCostFactor"),
        ("T11-FC-FSPF-MIB", "t11FspfIfRowStatus"),
        ("T11-FC-FSPF-MIB", "t11FspfIfStorageType"),
        ("T11-FC-FSPF-MIB", "t11FspfIfPrevNbrState"))
)
if mibBuilder.loadTexts:
    t11FspfIfGroup.setStatus("current")

t11FspfIfCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 143, 2, 2, 3)
)
t11FspfIfCounterGroup.setObjects(
      *(("T11-FC-FSPF-MIB", "t11FspfIfInLsuPkts"),
        ("T11-FC-FSPF-MIB", "t11FspfIfInLsaPkts"),
        ("T11-FC-FSPF-MIB", "t11FspfIfOutLsuPkts"),
        ("T11-FC-FSPF-MIB", "t11FspfIfOutLsaPkts"),
        ("T11-FC-FSPF-MIB", "t11FspfIfOutHelloPkts"),
        ("T11-FC-FSPF-MIB", "t11FspfIfInHelloPkts"),
        ("T11-FC-FSPF-MIB", "t11FspfIfRetransmittedLsuPkts"),
        ("T11-FC-FSPF-MIB", "t11FspfIfInErrorPkts"))
)
if mibBuilder.loadTexts:
    t11FspfIfCounterGroup.setStatus("current")

t11FspfDatabaseGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 143, 2, 2, 4)
)
t11FspfDatabaseGroup.setObjects(
      *(("T11-FC-FSPF-MIB", "t11FspfLsrAdvDomainId"),
        ("T11-FC-FSPF-MIB", "t11FspfLsrAge"),
        ("T11-FC-FSPF-MIB", "t11FspfLsrIncarnationNumber"),
        ("T11-FC-FSPF-MIB", "t11FspfLsrCheckSum"),
        ("T11-FC-FSPF-MIB", "t11FspfLsrLinks"),
        ("T11-FC-FSPF-MIB", "t11FspfLinkNbrDomainId"),
        ("T11-FC-FSPF-MIB", "t11FspfLinkPortIndex"),
        ("T11-FC-FSPF-MIB", "t11FspfLinkNbrPortIndex"),
        ("T11-FC-FSPF-MIB", "t11FspfLinkType"),
        ("T11-FC-FSPF-MIB", "t11FspfLinkCost"),
        ("T11-FC-FSPF-MIB", "t11FspfLinkNumber"))
)
if mibBuilder.loadTexts:
    t11FspfDatabaseGroup.setStatus("current")


# Notification objects

t11FspfNbrStateChangNotify = NotificationType(
    (1, 3, 6, 1, 2, 1, 143, 0, 1)
)
t11FspfNbrStateChangNotify.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamConfigDomainId"),
        ("T11-FC-FSPF-MIB", "t11FspfIfNbrDomainId"),
        ("T11-FC-FSPF-MIB", "t11FspfIfNbrState"),
        ("T11-FC-FSPF-MIB", "t11FspfIfPrevNbrState"))
)
if mibBuilder.loadTexts:
    t11FspfNbrStateChangNotify.setStatus(
        "current"
    )


# Notifications groups

t11FspfNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 143, 2, 2, 5)
)
t11FspfNotificationGroup.setObjects(
    ("T11-FC-FSPF-MIB", "t11FspfNbrStateChangNotify")
)
if mibBuilder.loadTexts:
    t11FspfNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

t11FspfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 143, 2, 1, 1)
)
if mibBuilder.loadTexts:
    t11FspfMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "T11-FC-FSPF-MIB",
    **{"T11FspfLsrType": T11FspfLsrType,
       "T11FspfLinkType": T11FspfLinkType,
       "T11FspfInterfaceState": T11FspfInterfaceState,
       "T11FspfLastCreationTime": T11FspfLastCreationTime,
       "t11FcFspfMIB": t11FcFspfMIB,
       "t11FspfNotifications": t11FspfNotifications,
       "t11FspfNbrStateChangNotify": t11FspfNbrStateChangNotify,
       "t11FspfObjects": t11FspfObjects,
       "t11FspfConfiguration": t11FspfConfiguration,
       "t11FspfTable": t11FspfTable,
       "t11FspfEntry": t11FspfEntry,
       "t11FspfFabricIndex": t11FspfFabricIndex,
       "t11FspfMinLsArrival": t11FspfMinLsArrival,
       "t11FspfMinLsInterval": t11FspfMinLsInterval,
       "t11FspfLsRefreshTime": t11FspfLsRefreshTime,
       "t11FspfMaxAge": t11FspfMaxAge,
       "t11FspfMaxAgeDiscards": t11FspfMaxAgeDiscards,
       "t11FspfPathComputations": t11FspfPathComputations,
       "t11FspfChecksumErrors": t11FspfChecksumErrors,
       "t11FspfLsrs": t11FspfLsrs,
       "t11FspfCreateTime": t11FspfCreateTime,
       "t11FspfAdminStatus": t11FspfAdminStatus,
       "t11FspfOperStatus": t11FspfOperStatus,
       "t11FspfNbrStateChangNotifyEnable": t11FspfNbrStateChangNotifyEnable,
       "t11FspfSetToDefault": t11FspfSetToDefault,
       "t11FspfStorageType": t11FspfStorageType,
       "t11FspfIfTable": t11FspfIfTable,
       "t11FspfIfEntry": t11FspfIfEntry,
       "t11FspfIfIndex": t11FspfIfIndex,
       "t11FspfIfHelloInterval": t11FspfIfHelloInterval,
       "t11FspfIfDeadInterval": t11FspfIfDeadInterval,
       "t11FspfIfRetransmitInterval": t11FspfIfRetransmitInterval,
       "t11FspfIfInLsuPkts": t11FspfIfInLsuPkts,
       "t11FspfIfInLsaPkts": t11FspfIfInLsaPkts,
       "t11FspfIfOutLsuPkts": t11FspfIfOutLsuPkts,
       "t11FspfIfOutLsaPkts": t11FspfIfOutLsaPkts,
       "t11FspfIfOutHelloPkts": t11FspfIfOutHelloPkts,
       "t11FspfIfInHelloPkts": t11FspfIfInHelloPkts,
       "t11FspfIfRetransmittedLsuPkts": t11FspfIfRetransmittedLsuPkts,
       "t11FspfIfInErrorPkts": t11FspfIfInErrorPkts,
       "t11FspfIfNbrState": t11FspfIfNbrState,
       "t11FspfIfNbrDomainId": t11FspfIfNbrDomainId,
       "t11FspfIfNbrPortIndex": t11FspfIfNbrPortIndex,
       "t11FspfIfAdminStatus": t11FspfIfAdminStatus,
       "t11FspfIfCreateTime": t11FspfIfCreateTime,
       "t11FspfIfSetToDefault": t11FspfIfSetToDefault,
       "t11FspfIfLinkCostFactor": t11FspfIfLinkCostFactor,
       "t11FspfIfStorageType": t11FspfIfStorageType,
       "t11FspfIfRowStatus": t11FspfIfRowStatus,
       "t11FspfIfPrevNbrState": t11FspfIfPrevNbrState,
       "t11FspfDatabase": t11FspfDatabase,
       "t11FspfLsrTable": t11FspfLsrTable,
       "t11FspfLsrEntry": t11FspfLsrEntry,
       "t11FspfLsrDomainId": t11FspfLsrDomainId,
       "t11FspfLsrType": t11FspfLsrType,
       "t11FspfLsrAdvDomainId": t11FspfLsrAdvDomainId,
       "t11FspfLsrAge": t11FspfLsrAge,
       "t11FspfLsrIncarnationNumber": t11FspfLsrIncarnationNumber,
       "t11FspfLsrCheckSum": t11FspfLsrCheckSum,
       "t11FspfLsrLinks": t11FspfLsrLinks,
       "t11FspfLinkNumber": t11FspfLinkNumber,
       "t11FspfLinkTable": t11FspfLinkTable,
       "t11FspfLinkEntry": t11FspfLinkEntry,
       "t11FspfLinkIndex": t11FspfLinkIndex,
       "t11FspfLinkNbrDomainId": t11FspfLinkNbrDomainId,
       "t11FspfLinkPortIndex": t11FspfLinkPortIndex,
       "t11FspfLinkNbrPortIndex": t11FspfLinkNbrPortIndex,
       "t11FspfLinkType": t11FspfLinkType,
       "t11FspfLinkCost": t11FspfLinkCost,
       "t11FspfConformance": t11FspfConformance,
       "t11FspfMIBCompliances": t11FspfMIBCompliances,
       "t11FspfMIBCompliance": t11FspfMIBCompliance,
       "t11FspfMIBGroups": t11FspfMIBGroups,
       "t11FspfGeneralGroup": t11FspfGeneralGroup,
       "t11FspfIfGroup": t11FspfIfGroup,
       "t11FspfIfCounterGroup": t11FspfIfCounterGroup,
       "t11FspfDatabaseGroup": t11FspfDatabaseGroup,
       "t11FspfNotificationGroup": t11FspfNotificationGroup}
)
