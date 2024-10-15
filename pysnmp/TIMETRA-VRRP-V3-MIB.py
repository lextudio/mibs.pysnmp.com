# SNMP MIB module (TIMETRA-VRRP-V3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-VRRP-V3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:11 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules")

(VrId,
 vrrpMIBCompliances,
 vrrpMIBGroups,
 vrrpNotifications,
 vrrpOperations,
 vrrpStatistics) = mibBuilder.importSymbols(
    "VRRP-MIB",
    "VrId",
    "vrrpMIBCompliances",
    "vrrpMIBGroups",
    "vrrpNotifications",
    "vrrpOperations",
    "vrrpStatistics")


# MODULE-IDENTITY

timetraVrrpV3MibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 57)
)
timetraVrrpV3MibModule.setRevisions(
        ("1909-02-28 00:00",
         "2008-04-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VrrpOperationsTable_Object = MibTable
vrrpOperationsTable = _VrrpOperationsTable_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7)
)
if mibBuilder.loadTexts:
    vrrpOperationsTable.setStatus("current")
_VrrpOperationsEntry_Object = MibTableRow
vrrpOperationsEntry = _VrrpOperationsEntry_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1)
)
vrrpOperationsEntry.setIndexNames(
    (0, "TIMETRA-VRRP-V3-MIB", "vrrpOperationsInetAddrType"),
    (0, "TIMETRA-VRRP-V3-MIB", "vrrpOperationsVrId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vrrpOperationsEntry.setStatus("current")
_VrrpOperationsInetAddrType_Type = InetAddressType
_VrrpOperationsInetAddrType_Object = MibTableColumn
vrrpOperationsInetAddrType = _VrrpOperationsInetAddrType_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 1),
    _VrrpOperationsInetAddrType_Type()
)
vrrpOperationsInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrrpOperationsInetAddrType.setStatus("current")
_VrrpOperationsVrId_Type = VrId
_VrrpOperationsVrId_Object = MibTableColumn
vrrpOperationsVrId = _VrrpOperationsVrId_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 2),
    _VrrpOperationsVrId_Type()
)
vrrpOperationsVrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrrpOperationsVrId.setStatus("current")
_VrrpOperationsVirtualMacAddr_Type = MacAddress
_VrrpOperationsVirtualMacAddr_Object = MibTableColumn
vrrpOperationsVirtualMacAddr = _VrrpOperationsVirtualMacAddr_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 3),
    _VrrpOperationsVirtualMacAddr_Type()
)
vrrpOperationsVirtualMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpOperationsVirtualMacAddr.setStatus("current")


class _VrrpOperationsState_Type(Integer32):
    """Custom type vrrpOperationsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("initialize", 1),
          ("master", 3))
    )


_VrrpOperationsState_Type.__name__ = "Integer32"
_VrrpOperationsState_Object = MibTableColumn
vrrpOperationsState = _VrrpOperationsState_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 4),
    _VrrpOperationsState_Type()
)
vrrpOperationsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpOperationsState.setStatus("current")


class _VrrpOperationsPriority_Type(Unsigned32):
    """Custom type vrrpOperationsPriority based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrrpOperationsPriority_Type.__name__ = "Unsigned32"
_VrrpOperationsPriority_Object = MibTableColumn
vrrpOperationsPriority = _VrrpOperationsPriority_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 5),
    _VrrpOperationsPriority_Type()
)
vrrpOperationsPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperationsPriority.setStatus("current")


class _VrrpOperationsAddrCount_Type(Integer32):
    """Custom type vrrpOperationsAddrCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrrpOperationsAddrCount_Type.__name__ = "Integer32"
_VrrpOperationsAddrCount_Object = MibTableColumn
vrrpOperationsAddrCount = _VrrpOperationsAddrCount_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 6),
    _VrrpOperationsAddrCount_Type()
)
vrrpOperationsAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpOperationsAddrCount.setStatus("current")
_VrrpOperationsMasterIpAddr_Type = InetAddress
_VrrpOperationsMasterIpAddr_Object = MibTableColumn
vrrpOperationsMasterIpAddr = _VrrpOperationsMasterIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 7),
    _VrrpOperationsMasterIpAddr_Type()
)
vrrpOperationsMasterIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpOperationsMasterIpAddr.setStatus("current")
_VrrpOperationsPrimaryIpAddr_Type = InetAddress
_VrrpOperationsPrimaryIpAddr_Object = MibTableColumn
vrrpOperationsPrimaryIpAddr = _VrrpOperationsPrimaryIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 8),
    _VrrpOperationsPrimaryIpAddr_Type()
)
vrrpOperationsPrimaryIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperationsPrimaryIpAddr.setStatus("current")


class _VrrpOperationsAdvInterval_Type(TimeInterval):
    """Custom type vrrpOperationsAdvInterval based on TimeInterval"""
    defaultValue = 100

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_VrrpOperationsAdvInterval_Type.__name__ = "TimeInterval"
_VrrpOperationsAdvInterval_Object = MibTableColumn
vrrpOperationsAdvInterval = _VrrpOperationsAdvInterval_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 9),
    _VrrpOperationsAdvInterval_Type()
)
vrrpOperationsAdvInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperationsAdvInterval.setStatus("current")
if mibBuilder.loadTexts:
    vrrpOperationsAdvInterval.setUnits("centiseconds")


class _VrrpOperationsPreemptMode_Type(TruthValue):
    """Custom type vrrpOperationsPreemptMode based on TruthValue"""


_VrrpOperationsPreemptMode_Object = MibTableColumn
vrrpOperationsPreemptMode = _VrrpOperationsPreemptMode_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 10),
    _VrrpOperationsPreemptMode_Type()
)
vrrpOperationsPreemptMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperationsPreemptMode.setStatus("current")


class _VrrpOperationsAcceptMode_Type(TruthValue):
    """Custom type vrrpOperationsAcceptMode based on TruthValue"""


_VrrpOperationsAcceptMode_Object = MibTableColumn
vrrpOperationsAcceptMode = _VrrpOperationsAcceptMode_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 11),
    _VrrpOperationsAcceptMode_Type()
)
vrrpOperationsAcceptMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperationsAcceptMode.setStatus("current")
_VrrpOperationsUpTime_Type = TimeStamp
_VrrpOperationsUpTime_Object = MibTableColumn
vrrpOperationsUpTime = _VrrpOperationsUpTime_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 12),
    _VrrpOperationsUpTime_Type()
)
vrrpOperationsUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpOperationsUpTime.setStatus("current")


class _VrrpOperationsStorageType_Type(StorageType):
    """Custom type vrrpOperationsStorageType based on StorageType"""


_VrrpOperationsStorageType_Object = MibTableColumn
vrrpOperationsStorageType = _VrrpOperationsStorageType_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 13),
    _VrrpOperationsStorageType_Type()
)
vrrpOperationsStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperationsStorageType.setStatus("current")
_VrrpOperationsRowStatus_Type = RowStatus
_VrrpOperationsRowStatus_Object = MibTableColumn
vrrpOperationsRowStatus = _VrrpOperationsRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 14),
    _VrrpOperationsRowStatus_Type()
)
vrrpOperationsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperationsRowStatus.setStatus("current")
_VrrpAssociatedIpAddrTable_Object = MibTable
vrrpAssociatedIpAddrTable = _VrrpAssociatedIpAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 8)
)
if mibBuilder.loadTexts:
    vrrpAssociatedIpAddrTable.setStatus("current")
_VrrpAssociatedIpAddrEntry_Object = MibTableRow
vrrpAssociatedIpAddrEntry = _VrrpAssociatedIpAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 8, 1)
)
vrrpAssociatedIpAddrEntry.setIndexNames(
    (0, "TIMETRA-VRRP-V3-MIB", "vrrpOperationsInetAddrType"),
    (0, "TIMETRA-VRRP-V3-MIB", "vrrpOperationsVrId"),
    (0, "IF-MIB", "ifIndex"),
    (0, "TIMETRA-VRRP-V3-MIB", "vrrpAssociatedIpAddr"),
)
if mibBuilder.loadTexts:
    vrrpAssociatedIpAddrEntry.setStatus("current")


class _VrrpAssociatedIpAddr_Type(InetAddress):
    """Custom type vrrpAssociatedIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VrrpAssociatedIpAddr_Type.__name__ = "InetAddress"
_VrrpAssociatedIpAddr_Object = MibTableColumn
vrrpAssociatedIpAddr = _VrrpAssociatedIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 8, 1, 1),
    _VrrpAssociatedIpAddr_Type()
)
vrrpAssociatedIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrrpAssociatedIpAddr.setStatus("current")


class _VrrpAssociatedStorageType_Type(StorageType):
    """Custom type vrrpAssociatedStorageType based on StorageType"""


_VrrpAssociatedStorageType_Object = MibTableColumn
vrrpAssociatedStorageType = _VrrpAssociatedStorageType_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 8, 1, 2),
    _VrrpAssociatedStorageType_Type()
)
vrrpAssociatedStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpAssociatedStorageType.setStatus("current")
_VrrpAssociatedIpAddrRowStatus_Type = RowStatus
_VrrpAssociatedIpAddrRowStatus_Object = MibTableColumn
vrrpAssociatedIpAddrRowStatus = _VrrpAssociatedIpAddrRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 8, 1, 3),
    _VrrpAssociatedIpAddrRowStatus_Type()
)
vrrpAssociatedIpAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpAssociatedIpAddrRowStatus.setStatus("current")


class _VrrpNewMasterReason_Type(Integer32):
    """Custom type vrrpNewMasterReason based on Integer32"""
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
        *(("masterNoResponse", 3),
          ("notmaster", 0),
          ("preempted", 2),
          ("priority", 1))
    )


_VrrpNewMasterReason_Type.__name__ = "Integer32"
_VrrpNewMasterReason_Object = MibScalar
vrrpNewMasterReason = _VrrpNewMasterReason_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 9),
    _VrrpNewMasterReason_Type()
)
vrrpNewMasterReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpNewMasterReason.setStatus("current")


class _VrrpTrapProtoErrReason_Type(Integer32):
    """Custom type vrrpTrapProtoErrReason based on Integer32"""
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
        *(("checksumError", 2),
          ("hopLimitError", 0),
          ("versionError", 1),
          ("vridError", 3))
    )


_VrrpTrapProtoErrReason_Type.__name__ = "Integer32"
_VrrpTrapProtoErrReason_Object = MibScalar
vrrpTrapProtoErrReason = _VrrpTrapProtoErrReason_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 10),
    _VrrpTrapProtoErrReason_Type()
)
vrrpTrapProtoErrReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vrrpTrapProtoErrReason.setStatus("current")
_VrrpRouterStatisticsTable_Object = MibTable
vrrpRouterStatisticsTable = _VrrpRouterStatisticsTable_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5)
)
if mibBuilder.loadTexts:
    vrrpRouterStatisticsTable.setStatus("current")
_VrrpRouterStatisticsEntry_Object = MibTableRow
vrrpRouterStatisticsEntry = _VrrpRouterStatisticsEntry_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5, 1)
)
if mibBuilder.loadTexts:
    vrrpRouterStatisticsEntry.setStatus("current")
_VrrpStatisticsMasterTransitions_Type = Counter32
_VrrpStatisticsMasterTransitions_Object = MibTableColumn
vrrpStatisticsMasterTransitions = _VrrpStatisticsMasterTransitions_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 1),
    _VrrpStatisticsMasterTransitions_Type()
)
vrrpStatisticsMasterTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatisticsMasterTransitions.setStatus("current")
_VrrpStatisticsRcvdAdvertisements_Type = Counter32
_VrrpStatisticsRcvdAdvertisements_Object = MibTableColumn
vrrpStatisticsRcvdAdvertisements = _VrrpStatisticsRcvdAdvertisements_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 2),
    _VrrpStatisticsRcvdAdvertisements_Type()
)
vrrpStatisticsRcvdAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatisticsRcvdAdvertisements.setStatus("current")
_VrrpStatisticsAdvIntervalErrors_Type = Counter32
_VrrpStatisticsAdvIntervalErrors_Object = MibTableColumn
vrrpStatisticsAdvIntervalErrors = _VrrpStatisticsAdvIntervalErrors_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 3),
    _VrrpStatisticsAdvIntervalErrors_Type()
)
vrrpStatisticsAdvIntervalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatisticsAdvIntervalErrors.setStatus("current")
_VrrpStatisticsIpTtlErrors_Type = Counter32
_VrrpStatisticsIpTtlErrors_Object = MibTableColumn
vrrpStatisticsIpTtlErrors = _VrrpStatisticsIpTtlErrors_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 4),
    _VrrpStatisticsIpTtlErrors_Type()
)
vrrpStatisticsIpTtlErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatisticsIpTtlErrors.setStatus("current")
_VrrpStatisticsRcvdPriZeroPackets_Type = Counter32
_VrrpStatisticsRcvdPriZeroPackets_Object = MibTableColumn
vrrpStatisticsRcvdPriZeroPackets = _VrrpStatisticsRcvdPriZeroPackets_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 5),
    _VrrpStatisticsRcvdPriZeroPackets_Type()
)
vrrpStatisticsRcvdPriZeroPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatisticsRcvdPriZeroPackets.setStatus("current")
_VrrpStatisticsSentPriZeroPackets_Type = Counter32
_VrrpStatisticsSentPriZeroPackets_Object = MibTableColumn
vrrpStatisticsSentPriZeroPackets = _VrrpStatisticsSentPriZeroPackets_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 6),
    _VrrpStatisticsSentPriZeroPackets_Type()
)
vrrpStatisticsSentPriZeroPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatisticsSentPriZeroPackets.setStatus("current")
_VrrpStatisticsRcvdInvalidTypePkts_Type = Counter32
_VrrpStatisticsRcvdInvalidTypePkts_Object = MibTableColumn
vrrpStatisticsRcvdInvalidTypePkts = _VrrpStatisticsRcvdInvalidTypePkts_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 7),
    _VrrpStatisticsRcvdInvalidTypePkts_Type()
)
vrrpStatisticsRcvdInvalidTypePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatisticsRcvdInvalidTypePkts.setStatus("current")
_VrrpStatisticsAddressListErrors_Type = Counter32
_VrrpStatisticsAddressListErrors_Object = MibTableColumn
vrrpStatisticsAddressListErrors = _VrrpStatisticsAddressListErrors_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 8),
    _VrrpStatisticsAddressListErrors_Type()
)
vrrpStatisticsAddressListErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatisticsAddressListErrors.setStatus("current")
_VrrpStatisticsPacketLengthErrors_Type = Counter32
_VrrpStatisticsPacketLengthErrors_Object = MibTableColumn
vrrpStatisticsPacketLengthErrors = _VrrpStatisticsPacketLengthErrors_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 9),
    _VrrpStatisticsPacketLengthErrors_Type()
)
vrrpStatisticsPacketLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatisticsPacketLengthErrors.setStatus("current")
_VrrpStatisticsRcvdInvalidAuthentications_Type = Counter32
_VrrpStatisticsRcvdInvalidAuthentications_Object = MibTableColumn
vrrpStatisticsRcvdInvalidAuthentications = _VrrpStatisticsRcvdInvalidAuthentications_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 10),
    _VrrpStatisticsRcvdInvalidAuthentications_Type()
)
vrrpStatisticsRcvdInvalidAuthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatisticsRcvdInvalidAuthentications.setStatus("current")
_VrrpStatisticsDiscontinuityTime_Type = TimeStamp
_VrrpStatisticsDiscontinuityTime_Object = MibTableColumn
vrrpStatisticsDiscontinuityTime = _VrrpStatisticsDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 11),
    _VrrpStatisticsDiscontinuityTime_Type()
)
vrrpStatisticsDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatisticsDiscontinuityTime.setStatus("current")
_VrrpStatisticsRefreshRate_Type = Unsigned32
_VrrpStatisticsRefreshRate_Object = MibTableColumn
vrrpStatisticsRefreshRate = _VrrpStatisticsRefreshRate_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 12),
    _VrrpStatisticsRefreshRate_Type()
)
vrrpStatisticsRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatisticsRefreshRate.setStatus("current")
if mibBuilder.loadTexts:
    vrrpStatisticsRefreshRate.setUnits("milli-seconds")
vrrpOperationsEntry.registerAugmentions(
    ("TIMETRA-VRRP-V3-MIB",
     "vrrpRouterStatisticsEntry")
)
vrrpRouterStatisticsEntry.setIndexNames(*vrrpOperationsEntry.getIndexNames())

# Managed Objects groups

vrrpOperationsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 68, 3, 2, 5)
)
vrrpOperationsGroup.setObjects(
      *(("TIMETRA-VRRP-V3-MIB", "vrrpOperationsVirtualMacAddr"),
        ("TIMETRA-VRRP-V3-MIB", "vrrpOperationsState"),
        ("TIMETRA-VRRP-V3-MIB", "vrrpOperationsPriority"),
        ("TIMETRA-VRRP-V3-MIB", "vrrpOperationsMasterIpAddr"),
        ("TIMETRA-VRRP-V3-MIB", "vrrpOperationsAdvInterval"),
        ("TIMETRA-VRRP-V3-MIB", "vrrpOperationsPreemptMode"),
        ("TIMETRA-VRRP-V3-MIB", "vrrpOperationsAcceptMode"),
        ("TIMETRA-VRRP-V3-MIB", "vrrpOperationsUpTime"),
        ("TIMETRA-VRRP-V3-MIB", "vrrpOperationsStorageType"),
        ("TIMETRA-VRRP-V3-MIB", "vrrpOperationsRowStatus"),
        ("TIMETRA-VRRP-V3-MIB", "vrrpOperationsAddrCount"),
        ("TIMETRA-VRRP-V3-MIB", "vrrpOperationsPrimaryIpAddr"),
        ("TIMETRA-VRRP-V3-MIB", "vrrpAssociatedStorageType"),
        ("TIMETRA-VRRP-V3-MIB", "vrrpAssociatedIpAddrRowStatus"))
)
if mibBuilder.loadTexts:
    vrrpOperationsGroup.setStatus("current")

vrrpStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 68, 3, 2, 6)
)
vrrpStatisticsGroup.setObjects(
      *(("TIMETRA-VRRP-V3-MIB", "vrrpStatisticsMasterTransitions"),
        ("TIMETRA-VRRP-V3-MIB", "vrrpStatisticsRcvdAdvertisements"),
        ("TIMETRA-VRRP-V3-MIB", "vrrpStatisticsAdvIntervalErrors"),
        ("TIMETRA-VRRP-V3-MIB", "vrrpStatisticsRcvdPriZeroPackets"),
        ("TIMETRA-VRRP-V3-MIB", "vrrpStatisticsSentPriZeroPackets"),
        ("TIMETRA-VRRP-V3-MIB", "vrrpStatisticsRcvdInvalidTypePkts"),
        ("TIMETRA-VRRP-V3-MIB", "vrrpStatisticsIpTtlErrors"),
        ("TIMETRA-VRRP-V3-MIB", "vrrpStatisticsAddressListErrors"),
        ("TIMETRA-VRRP-V3-MIB", "vrrpStatisticsPacketLengthErrors"),
        ("TIMETRA-VRRP-V3-MIB", "vrrpStatisticsRcvdInvalidAuthentications"),
        ("TIMETRA-VRRP-V3-MIB", "vrrpStatisticsDiscontinuityTime"),
        ("TIMETRA-VRRP-V3-MIB", "vrrpStatisticsRefreshRate"))
)
if mibBuilder.loadTexts:
    vrrpStatisticsGroup.setStatus("current")

vrrpTrapInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 68, 3, 2, 7)
)
vrrpTrapInfoGroup.setObjects(
    ("TIMETRA-VRRP-V3-MIB", "vrrpNewMasterReason")
)
if mibBuilder.loadTexts:
    vrrpTrapInfoGroup.setStatus("current")

vrrpNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 68, 3, 2, 9)
)
vrrpNotifyObjsGroup.setObjects(
    ("TIMETRA-VRRP-V3-MIB", "vrrpTrapProtoErrReason")
)
if mibBuilder.loadTexts:
    vrrpNotifyObjsGroup.setStatus("current")


# Notification objects

vrrpTrapProtoError = NotificationType(
    (1, 3, 6, 1, 2, 1, 68, 0, 3)
)
vrrpTrapProtoError.setObjects(
    ("TIMETRA-VRRP-V3-MIB", "vrrpTrapProtoErrReason")
)
if mibBuilder.loadTexts:
    vrrpTrapProtoError.setStatus(
        "current"
    )


# Notifications groups

vrrpNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 68, 3, 2, 8)
)
vrrpNotificationsGroup.setObjects(
    ("TIMETRA-VRRP-V3-MIB", "vrrpTrapProtoError")
)
if mibBuilder.loadTexts:
    vrrpNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vrrpModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 68, 3, 1, 2)
)
if mibBuilder.loadTexts:
    vrrpModuleFullCompliance.setStatus(
        "current"
    )

vrrpModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 68, 3, 1, 3)
)
if mibBuilder.loadTexts:
    vrrpModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-VRRP-V3-MIB",
    **{"vrrpTrapProtoError": vrrpTrapProtoError,
       "vrrpOperationsTable": vrrpOperationsTable,
       "vrrpOperationsEntry": vrrpOperationsEntry,
       "vrrpOperationsInetAddrType": vrrpOperationsInetAddrType,
       "vrrpOperationsVrId": vrrpOperationsVrId,
       "vrrpOperationsVirtualMacAddr": vrrpOperationsVirtualMacAddr,
       "vrrpOperationsState": vrrpOperationsState,
       "vrrpOperationsPriority": vrrpOperationsPriority,
       "vrrpOperationsAddrCount": vrrpOperationsAddrCount,
       "vrrpOperationsMasterIpAddr": vrrpOperationsMasterIpAddr,
       "vrrpOperationsPrimaryIpAddr": vrrpOperationsPrimaryIpAddr,
       "vrrpOperationsAdvInterval": vrrpOperationsAdvInterval,
       "vrrpOperationsPreemptMode": vrrpOperationsPreemptMode,
       "vrrpOperationsAcceptMode": vrrpOperationsAcceptMode,
       "vrrpOperationsUpTime": vrrpOperationsUpTime,
       "vrrpOperationsStorageType": vrrpOperationsStorageType,
       "vrrpOperationsRowStatus": vrrpOperationsRowStatus,
       "vrrpAssociatedIpAddrTable": vrrpAssociatedIpAddrTable,
       "vrrpAssociatedIpAddrEntry": vrrpAssociatedIpAddrEntry,
       "vrrpAssociatedIpAddr": vrrpAssociatedIpAddr,
       "vrrpAssociatedStorageType": vrrpAssociatedStorageType,
       "vrrpAssociatedIpAddrRowStatus": vrrpAssociatedIpAddrRowStatus,
       "vrrpNewMasterReason": vrrpNewMasterReason,
       "vrrpTrapProtoErrReason": vrrpTrapProtoErrReason,
       "vrrpRouterStatisticsTable": vrrpRouterStatisticsTable,
       "vrrpRouterStatisticsEntry": vrrpRouterStatisticsEntry,
       "vrrpStatisticsMasterTransitions": vrrpStatisticsMasterTransitions,
       "vrrpStatisticsRcvdAdvertisements": vrrpStatisticsRcvdAdvertisements,
       "vrrpStatisticsAdvIntervalErrors": vrrpStatisticsAdvIntervalErrors,
       "vrrpStatisticsIpTtlErrors": vrrpStatisticsIpTtlErrors,
       "vrrpStatisticsRcvdPriZeroPackets": vrrpStatisticsRcvdPriZeroPackets,
       "vrrpStatisticsSentPriZeroPackets": vrrpStatisticsSentPriZeroPackets,
       "vrrpStatisticsRcvdInvalidTypePkts": vrrpStatisticsRcvdInvalidTypePkts,
       "vrrpStatisticsAddressListErrors": vrrpStatisticsAddressListErrors,
       "vrrpStatisticsPacketLengthErrors": vrrpStatisticsPacketLengthErrors,
       "vrrpStatisticsRcvdInvalidAuthentications": vrrpStatisticsRcvdInvalidAuthentications,
       "vrrpStatisticsDiscontinuityTime": vrrpStatisticsDiscontinuityTime,
       "vrrpStatisticsRefreshRate": vrrpStatisticsRefreshRate,
       "vrrpModuleFullCompliance": vrrpModuleFullCompliance,
       "vrrpModuleReadOnlyCompliance": vrrpModuleReadOnlyCompliance,
       "vrrpOperationsGroup": vrrpOperationsGroup,
       "vrrpStatisticsGroup": vrrpStatisticsGroup,
       "vrrpTrapInfoGroup": vrrpTrapInfoGroup,
       "vrrpNotificationsGroup": vrrpNotificationsGroup,
       "vrrpNotifyObjsGroup": vrrpNotifyObjsGroup,
       "timetraVrrpV3MibModule": timetraVrrpV3MibModule}
)
