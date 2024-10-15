# SNMP MIB module (VRRPV3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VRRPV3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:10 2024
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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

vrrpv3MIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 207)
)
vrrpv3MIB.setRevisions(
        ("2012-02-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Vrrpv3VrIdTC(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_Vrrpv3Notifications_ObjectIdentity = ObjectIdentity
vrrpv3Notifications = _Vrrpv3Notifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 207, 0)
)
_Vrrpv3Objects_ObjectIdentity = ObjectIdentity
vrrpv3Objects = _Vrrpv3Objects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 207, 1)
)
_Vrrpv3Operations_ObjectIdentity = ObjectIdentity
vrrpv3Operations = _Vrrpv3Operations_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 207, 1, 1)
)
_Vrrpv3OperationsTable_Object = MibTable
vrrpv3OperationsTable = _Vrrpv3OperationsTable_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 1, 1)
)
if mibBuilder.loadTexts:
    vrrpv3OperationsTable.setStatus("current")
_Vrrpv3OperationsEntry_Object = MibTableRow
vrrpv3OperationsEntry = _Vrrpv3OperationsEntry_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1)
)
vrrpv3OperationsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRPV3-MIB", "vrrpv3OperationsVrId"),
    (0, "VRRPV3-MIB", "vrrpv3OperationsInetAddrType"),
)
if mibBuilder.loadTexts:
    vrrpv3OperationsEntry.setStatus("current")
_Vrrpv3OperationsVrId_Type = Vrrpv3VrIdTC
_Vrrpv3OperationsVrId_Object = MibTableColumn
vrrpv3OperationsVrId = _Vrrpv3OperationsVrId_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 1),
    _Vrrpv3OperationsVrId_Type()
)
vrrpv3OperationsVrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrrpv3OperationsVrId.setStatus("current")
_Vrrpv3OperationsInetAddrType_Type = InetAddressType
_Vrrpv3OperationsInetAddrType_Object = MibTableColumn
vrrpv3OperationsInetAddrType = _Vrrpv3OperationsInetAddrType_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 2),
    _Vrrpv3OperationsInetAddrType_Type()
)
vrrpv3OperationsInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrrpv3OperationsInetAddrType.setStatus("current")
_Vrrpv3OperationsMasterIpAddr_Type = InetAddress
_Vrrpv3OperationsMasterIpAddr_Object = MibTableColumn
vrrpv3OperationsMasterIpAddr = _Vrrpv3OperationsMasterIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 3),
    _Vrrpv3OperationsMasterIpAddr_Type()
)
vrrpv3OperationsMasterIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpv3OperationsMasterIpAddr.setStatus("current")
_Vrrpv3OperationsPrimaryIpAddr_Type = InetAddress
_Vrrpv3OperationsPrimaryIpAddr_Object = MibTableColumn
vrrpv3OperationsPrimaryIpAddr = _Vrrpv3OperationsPrimaryIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 4),
    _Vrrpv3OperationsPrimaryIpAddr_Type()
)
vrrpv3OperationsPrimaryIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpv3OperationsPrimaryIpAddr.setStatus("current")
_Vrrpv3OperationsVirtualMacAddr_Type = MacAddress
_Vrrpv3OperationsVirtualMacAddr_Object = MibTableColumn
vrrpv3OperationsVirtualMacAddr = _Vrrpv3OperationsVirtualMacAddr_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 5),
    _Vrrpv3OperationsVirtualMacAddr_Type()
)
vrrpv3OperationsVirtualMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpv3OperationsVirtualMacAddr.setStatus("current")


class _Vrrpv3OperationsStatus_Type(Integer32):
    """Custom type vrrpv3OperationsStatus based on Integer32"""
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


_Vrrpv3OperationsStatus_Type.__name__ = "Integer32"
_Vrrpv3OperationsStatus_Object = MibTableColumn
vrrpv3OperationsStatus = _Vrrpv3OperationsStatus_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 6),
    _Vrrpv3OperationsStatus_Type()
)
vrrpv3OperationsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpv3OperationsStatus.setStatus("current")


class _Vrrpv3OperationsPriority_Type(Unsigned32):
    """Custom type vrrpv3OperationsPriority based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Vrrpv3OperationsPriority_Type.__name__ = "Unsigned32"
_Vrrpv3OperationsPriority_Object = MibTableColumn
vrrpv3OperationsPriority = _Vrrpv3OperationsPriority_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 7),
    _Vrrpv3OperationsPriority_Type()
)
vrrpv3OperationsPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpv3OperationsPriority.setStatus("current")


class _Vrrpv3OperationsAddrCount_Type(Integer32):
    """Custom type vrrpv3OperationsAddrCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Vrrpv3OperationsAddrCount_Type.__name__ = "Integer32"
_Vrrpv3OperationsAddrCount_Object = MibTableColumn
vrrpv3OperationsAddrCount = _Vrrpv3OperationsAddrCount_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 8),
    _Vrrpv3OperationsAddrCount_Type()
)
vrrpv3OperationsAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpv3OperationsAddrCount.setStatus("current")


class _Vrrpv3OperationsAdvInterval_Type(TimeInterval):
    """Custom type vrrpv3OperationsAdvInterval based on TimeInterval"""
    defaultValue = 100

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Vrrpv3OperationsAdvInterval_Type.__name__ = "TimeInterval"
_Vrrpv3OperationsAdvInterval_Object = MibTableColumn
vrrpv3OperationsAdvInterval = _Vrrpv3OperationsAdvInterval_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 9),
    _Vrrpv3OperationsAdvInterval_Type()
)
vrrpv3OperationsAdvInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpv3OperationsAdvInterval.setStatus("current")
if mibBuilder.loadTexts:
    vrrpv3OperationsAdvInterval.setUnits("centiseconds")


class _Vrrpv3OperationsPreemptMode_Type(TruthValue):
    """Custom type vrrpv3OperationsPreemptMode based on TruthValue"""


_Vrrpv3OperationsPreemptMode_Object = MibTableColumn
vrrpv3OperationsPreemptMode = _Vrrpv3OperationsPreemptMode_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 10),
    _Vrrpv3OperationsPreemptMode_Type()
)
vrrpv3OperationsPreemptMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpv3OperationsPreemptMode.setStatus("current")


class _Vrrpv3OperationsAcceptMode_Type(TruthValue):
    """Custom type vrrpv3OperationsAcceptMode based on TruthValue"""


_Vrrpv3OperationsAcceptMode_Object = MibTableColumn
vrrpv3OperationsAcceptMode = _Vrrpv3OperationsAcceptMode_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 11),
    _Vrrpv3OperationsAcceptMode_Type()
)
vrrpv3OperationsAcceptMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpv3OperationsAcceptMode.setStatus("current")
_Vrrpv3OperationsUpTime_Type = TimeTicks
_Vrrpv3OperationsUpTime_Object = MibTableColumn
vrrpv3OperationsUpTime = _Vrrpv3OperationsUpTime_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 12),
    _Vrrpv3OperationsUpTime_Type()
)
vrrpv3OperationsUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpv3OperationsUpTime.setStatus("current")
_Vrrpv3OperationsRowStatus_Type = RowStatus
_Vrrpv3OperationsRowStatus_Object = MibTableColumn
vrrpv3OperationsRowStatus = _Vrrpv3OperationsRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 13),
    _Vrrpv3OperationsRowStatus_Type()
)
vrrpv3OperationsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpv3OperationsRowStatus.setStatus("current")
_Vrrpv3AssociatedIpAddrTable_Object = MibTable
vrrpv3AssociatedIpAddrTable = _Vrrpv3AssociatedIpAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 1, 2)
)
if mibBuilder.loadTexts:
    vrrpv3AssociatedIpAddrTable.setStatus("current")
_Vrrpv3AssociatedIpAddrEntry_Object = MibTableRow
vrrpv3AssociatedIpAddrEntry = _Vrrpv3AssociatedIpAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 1, 2, 1)
)
vrrpv3AssociatedIpAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRPV3-MIB", "vrrpv3OperationsVrId"),
    (0, "VRRPV3-MIB", "vrrpv3OperationsInetAddrType"),
    (0, "VRRPV3-MIB", "vrrpv3AssociatedIpAddrAddress"),
)
if mibBuilder.loadTexts:
    vrrpv3AssociatedIpAddrEntry.setStatus("current")


class _Vrrpv3AssociatedIpAddrAddress_Type(InetAddress):
    """Custom type vrrpv3AssociatedIpAddrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_Vrrpv3AssociatedIpAddrAddress_Type.__name__ = "InetAddress"
_Vrrpv3AssociatedIpAddrAddress_Object = MibTableColumn
vrrpv3AssociatedIpAddrAddress = _Vrrpv3AssociatedIpAddrAddress_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 1, 2, 1, 1),
    _Vrrpv3AssociatedIpAddrAddress_Type()
)
vrrpv3AssociatedIpAddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrrpv3AssociatedIpAddrAddress.setStatus("current")
_Vrrpv3AssociatedIpAddrRowStatus_Type = RowStatus
_Vrrpv3AssociatedIpAddrRowStatus_Object = MibTableColumn
vrrpv3AssociatedIpAddrRowStatus = _Vrrpv3AssociatedIpAddrRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 1, 2, 1, 2),
    _Vrrpv3AssociatedIpAddrRowStatus_Type()
)
vrrpv3AssociatedIpAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpv3AssociatedIpAddrRowStatus.setStatus("current")
_Vrrpv3Statistics_ObjectIdentity = ObjectIdentity
vrrpv3Statistics = _Vrrpv3Statistics_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 207, 1, 2)
)
_Vrrpv3RouterChecksumErrors_Type = Counter64
_Vrrpv3RouterChecksumErrors_Object = MibScalar
vrrpv3RouterChecksumErrors = _Vrrpv3RouterChecksumErrors_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 2, 1),
    _Vrrpv3RouterChecksumErrors_Type()
)
vrrpv3RouterChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpv3RouterChecksumErrors.setStatus("current")
_Vrrpv3RouterVersionErrors_Type = Counter64
_Vrrpv3RouterVersionErrors_Object = MibScalar
vrrpv3RouterVersionErrors = _Vrrpv3RouterVersionErrors_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 2, 2),
    _Vrrpv3RouterVersionErrors_Type()
)
vrrpv3RouterVersionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpv3RouterVersionErrors.setStatus("current")
_Vrrpv3RouterVrIdErrors_Type = Counter64
_Vrrpv3RouterVrIdErrors_Object = MibScalar
vrrpv3RouterVrIdErrors = _Vrrpv3RouterVrIdErrors_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 2, 3),
    _Vrrpv3RouterVrIdErrors_Type()
)
vrrpv3RouterVrIdErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpv3RouterVrIdErrors.setStatus("current")
_Vrrpv3GlobalStatisticsDiscontinuityTime_Type = TimeStamp
_Vrrpv3GlobalStatisticsDiscontinuityTime_Object = MibScalar
vrrpv3GlobalStatisticsDiscontinuityTime = _Vrrpv3GlobalStatisticsDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 2, 4),
    _Vrrpv3GlobalStatisticsDiscontinuityTime_Type()
)
vrrpv3GlobalStatisticsDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpv3GlobalStatisticsDiscontinuityTime.setStatus("current")
_Vrrpv3StatisticsTable_Object = MibTable
vrrpv3StatisticsTable = _Vrrpv3StatisticsTable_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 2, 5)
)
if mibBuilder.loadTexts:
    vrrpv3StatisticsTable.setStatus("current")
_Vrrpv3StatisticsEntry_Object = MibTableRow
vrrpv3StatisticsEntry = _Vrrpv3StatisticsEntry_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    vrrpv3StatisticsEntry.setStatus("current")
_Vrrpv3StatisticsMasterTransitions_Type = Counter32
_Vrrpv3StatisticsMasterTransitions_Object = MibTableColumn
vrrpv3StatisticsMasterTransitions = _Vrrpv3StatisticsMasterTransitions_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 1),
    _Vrrpv3StatisticsMasterTransitions_Type()
)
vrrpv3StatisticsMasterTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpv3StatisticsMasterTransitions.setStatus("current")


class _Vrrpv3StatisticsNewMasterReason_Type(Integer32):
    """Custom type vrrpv3StatisticsNewMasterReason based on Integer32"""
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
          ("notMaster", 0),
          ("preempted", 2),
          ("priority", 1))
    )


_Vrrpv3StatisticsNewMasterReason_Type.__name__ = "Integer32"
_Vrrpv3StatisticsNewMasterReason_Object = MibTableColumn
vrrpv3StatisticsNewMasterReason = _Vrrpv3StatisticsNewMasterReason_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 2),
    _Vrrpv3StatisticsNewMasterReason_Type()
)
vrrpv3StatisticsNewMasterReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpv3StatisticsNewMasterReason.setStatus("current")
_Vrrpv3StatisticsRcvdAdvertisements_Type = Counter64
_Vrrpv3StatisticsRcvdAdvertisements_Object = MibTableColumn
vrrpv3StatisticsRcvdAdvertisements = _Vrrpv3StatisticsRcvdAdvertisements_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 3),
    _Vrrpv3StatisticsRcvdAdvertisements_Type()
)
vrrpv3StatisticsRcvdAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpv3StatisticsRcvdAdvertisements.setStatus("current")
_Vrrpv3StatisticsAdvIntervalErrors_Type = Counter64
_Vrrpv3StatisticsAdvIntervalErrors_Object = MibTableColumn
vrrpv3StatisticsAdvIntervalErrors = _Vrrpv3StatisticsAdvIntervalErrors_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 4),
    _Vrrpv3StatisticsAdvIntervalErrors_Type()
)
vrrpv3StatisticsAdvIntervalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpv3StatisticsAdvIntervalErrors.setStatus("current")
_Vrrpv3StatisticsIpTtlErrors_Type = Counter64
_Vrrpv3StatisticsIpTtlErrors_Object = MibTableColumn
vrrpv3StatisticsIpTtlErrors = _Vrrpv3StatisticsIpTtlErrors_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 5),
    _Vrrpv3StatisticsIpTtlErrors_Type()
)
vrrpv3StatisticsIpTtlErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpv3StatisticsIpTtlErrors.setStatus("current")


class _Vrrpv3StatisticsProtoErrReason_Type(Integer32):
    """Custom type vrrpv3StatisticsProtoErrReason based on Integer32"""
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
        *(("checksumError", 3),
          ("ipTtlError", 1),
          ("noError", 0),
          ("versionError", 2),
          ("vrIdError", 4))
    )


_Vrrpv3StatisticsProtoErrReason_Type.__name__ = "Integer32"
_Vrrpv3StatisticsProtoErrReason_Object = MibTableColumn
vrrpv3StatisticsProtoErrReason = _Vrrpv3StatisticsProtoErrReason_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 6),
    _Vrrpv3StatisticsProtoErrReason_Type()
)
vrrpv3StatisticsProtoErrReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpv3StatisticsProtoErrReason.setStatus("current")
_Vrrpv3StatisticsRcvdPriZeroPackets_Type = Counter64
_Vrrpv3StatisticsRcvdPriZeroPackets_Object = MibTableColumn
vrrpv3StatisticsRcvdPriZeroPackets = _Vrrpv3StatisticsRcvdPriZeroPackets_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 7),
    _Vrrpv3StatisticsRcvdPriZeroPackets_Type()
)
vrrpv3StatisticsRcvdPriZeroPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpv3StatisticsRcvdPriZeroPackets.setStatus("current")
_Vrrpv3StatisticsSentPriZeroPackets_Type = Counter64
_Vrrpv3StatisticsSentPriZeroPackets_Object = MibTableColumn
vrrpv3StatisticsSentPriZeroPackets = _Vrrpv3StatisticsSentPriZeroPackets_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 8),
    _Vrrpv3StatisticsSentPriZeroPackets_Type()
)
vrrpv3StatisticsSentPriZeroPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpv3StatisticsSentPriZeroPackets.setStatus("current")
_Vrrpv3StatisticsRcvdInvalidTypePackets_Type = Counter64
_Vrrpv3StatisticsRcvdInvalidTypePackets_Object = MibTableColumn
vrrpv3StatisticsRcvdInvalidTypePackets = _Vrrpv3StatisticsRcvdInvalidTypePackets_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 9),
    _Vrrpv3StatisticsRcvdInvalidTypePackets_Type()
)
vrrpv3StatisticsRcvdInvalidTypePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpv3StatisticsRcvdInvalidTypePackets.setStatus("current")
_Vrrpv3StatisticsAddressListErrors_Type = Counter64
_Vrrpv3StatisticsAddressListErrors_Object = MibTableColumn
vrrpv3StatisticsAddressListErrors = _Vrrpv3StatisticsAddressListErrors_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 10),
    _Vrrpv3StatisticsAddressListErrors_Type()
)
vrrpv3StatisticsAddressListErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpv3StatisticsAddressListErrors.setStatus("current")
_Vrrpv3StatisticsPacketLengthErrors_Type = Counter64
_Vrrpv3StatisticsPacketLengthErrors_Object = MibTableColumn
vrrpv3StatisticsPacketLengthErrors = _Vrrpv3StatisticsPacketLengthErrors_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 11),
    _Vrrpv3StatisticsPacketLengthErrors_Type()
)
vrrpv3StatisticsPacketLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpv3StatisticsPacketLengthErrors.setStatus("current")
_Vrrpv3StatisticsRowDiscontinuityTime_Type = TimeStamp
_Vrrpv3StatisticsRowDiscontinuityTime_Object = MibTableColumn
vrrpv3StatisticsRowDiscontinuityTime = _Vrrpv3StatisticsRowDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 12),
    _Vrrpv3StatisticsRowDiscontinuityTime_Type()
)
vrrpv3StatisticsRowDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpv3StatisticsRowDiscontinuityTime.setStatus("current")
_Vrrpv3StatisticsRefreshRate_Type = Unsigned32
_Vrrpv3StatisticsRefreshRate_Object = MibTableColumn
vrrpv3StatisticsRefreshRate = _Vrrpv3StatisticsRefreshRate_Object(
    (1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 13),
    _Vrrpv3StatisticsRefreshRate_Type()
)
vrrpv3StatisticsRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpv3StatisticsRefreshRate.setStatus("current")
if mibBuilder.loadTexts:
    vrrpv3StatisticsRefreshRate.setUnits("milliseconds")
_Vrrpv3Conformance_ObjectIdentity = ObjectIdentity
vrrpv3Conformance = _Vrrpv3Conformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 207, 2)
)
_Vrrpv3Compliances_ObjectIdentity = ObjectIdentity
vrrpv3Compliances = _Vrrpv3Compliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 207, 2, 1)
)
_Vrrpv3Groups_ObjectIdentity = ObjectIdentity
vrrpv3Groups = _Vrrpv3Groups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 207, 2, 2)
)
vrrpv3OperationsEntry.registerAugmentions(
    ("VRRPV3-MIB",
     "vrrpv3StatisticsEntry")
)
vrrpv3StatisticsEntry.setIndexNames(*vrrpv3OperationsEntry.getIndexNames())

# Managed Objects groups

vrrpv3OperationsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 207, 2, 2, 1)
)
vrrpv3OperationsGroup.setObjects(
      *(("VRRPV3-MIB", "vrrpv3OperationsVirtualMacAddr"),
        ("VRRPV3-MIB", "vrrpv3OperationsStatus"),
        ("VRRPV3-MIB", "vrrpv3OperationsPriority"),
        ("VRRPV3-MIB", "vrrpv3OperationsMasterIpAddr"),
        ("VRRPV3-MIB", "vrrpv3OperationsAdvInterval"),
        ("VRRPV3-MIB", "vrrpv3OperationsPreemptMode"),
        ("VRRPV3-MIB", "vrrpv3OperationsAcceptMode"),
        ("VRRPV3-MIB", "vrrpv3OperationsUpTime"),
        ("VRRPV3-MIB", "vrrpv3OperationsRowStatus"),
        ("VRRPV3-MIB", "vrrpv3OperationsAddrCount"),
        ("VRRPV3-MIB", "vrrpv3OperationsPrimaryIpAddr"),
        ("VRRPV3-MIB", "vrrpv3AssociatedIpAddrRowStatus"))
)
if mibBuilder.loadTexts:
    vrrpv3OperationsGroup.setStatus("current")

vrrpv3StatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 207, 2, 2, 2)
)
vrrpv3StatisticsGroup.setObjects(
      *(("VRRPV3-MIB", "vrrpv3RouterChecksumErrors"),
        ("VRRPV3-MIB", "vrrpv3RouterVersionErrors"),
        ("VRRPV3-MIB", "vrrpv3RouterVrIdErrors"),
        ("VRRPV3-MIB", "vrrpv3StatisticsMasterTransitions"),
        ("VRRPV3-MIB", "vrrpv3StatisticsNewMasterReason"),
        ("VRRPV3-MIB", "vrrpv3StatisticsRcvdAdvertisements"),
        ("VRRPV3-MIB", "vrrpv3StatisticsAdvIntervalErrors"),
        ("VRRPV3-MIB", "vrrpv3StatisticsRcvdPriZeroPackets"),
        ("VRRPV3-MIB", "vrrpv3StatisticsSentPriZeroPackets"),
        ("VRRPV3-MIB", "vrrpv3StatisticsRcvdInvalidTypePackets"),
        ("VRRPV3-MIB", "vrrpv3StatisticsIpTtlErrors"),
        ("VRRPV3-MIB", "vrrpv3StatisticsProtoErrReason"),
        ("VRRPV3-MIB", "vrrpv3StatisticsAddressListErrors"),
        ("VRRPV3-MIB", "vrrpv3StatisticsPacketLengthErrors"),
        ("VRRPV3-MIB", "vrrpv3StatisticsRowDiscontinuityTime"),
        ("VRRPV3-MIB", "vrrpv3StatisticsRefreshRate"))
)
if mibBuilder.loadTexts:
    vrrpv3StatisticsGroup.setStatus("current")

vrrpv3StatisticsDiscontinuityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 207, 2, 2, 3)
)
vrrpv3StatisticsDiscontinuityGroup.setObjects(
    ("VRRPV3-MIB", "vrrpv3GlobalStatisticsDiscontinuityTime")
)
if mibBuilder.loadTexts:
    vrrpv3StatisticsDiscontinuityGroup.setStatus("current")

vrrpv3InfoGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 207, 2, 2, 4)
)
vrrpv3InfoGroup.setObjects(
      *(("VRRPV3-MIB", "vrrpv3StatisticsProtoErrReason"),
        ("VRRPV3-MIB", "vrrpv3StatisticsNewMasterReason"))
)
if mibBuilder.loadTexts:
    vrrpv3InfoGroup.setStatus("current")


# Notification objects

vrrpv3NewMaster = NotificationType(
    (1, 3, 6, 1, 2, 1, 207, 0, 1)
)
vrrpv3NewMaster.setObjects(
      *(("VRRPV3-MIB", "vrrpv3OperationsMasterIpAddr"),
        ("VRRPV3-MIB", "vrrpv3StatisticsNewMasterReason"))
)
if mibBuilder.loadTexts:
    vrrpv3NewMaster.setStatus(
        "current"
    )

vrrpv3ProtoError = NotificationType(
    (1, 3, 6, 1, 2, 1, 207, 0, 2)
)
vrrpv3ProtoError.setObjects(
    ("VRRPV3-MIB", "vrrpv3StatisticsProtoErrReason")
)
if mibBuilder.loadTexts:
    vrrpv3ProtoError.setStatus(
        "current"
    )


# Notifications groups

vrrpv3NotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 207, 2, 2, 5)
)
vrrpv3NotificationsGroup.setObjects(
      *(("VRRPV3-MIB", "vrrpv3NewMaster"),
        ("VRRPV3-MIB", "vrrpv3ProtoError"))
)
if mibBuilder.loadTexts:
    vrrpv3NotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vrrpv3FullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 207, 2, 1, 1)
)
if mibBuilder.loadTexts:
    vrrpv3FullCompliance.setStatus(
        "current"
    )

vrrpv3ReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 207, 2, 1, 2)
)
if mibBuilder.loadTexts:
    vrrpv3ReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VRRPV3-MIB",
    **{"Vrrpv3VrIdTC": Vrrpv3VrIdTC,
       "vrrpv3MIB": vrrpv3MIB,
       "vrrpv3Notifications": vrrpv3Notifications,
       "vrrpv3NewMaster": vrrpv3NewMaster,
       "vrrpv3ProtoError": vrrpv3ProtoError,
       "vrrpv3Objects": vrrpv3Objects,
       "vrrpv3Operations": vrrpv3Operations,
       "vrrpv3OperationsTable": vrrpv3OperationsTable,
       "vrrpv3OperationsEntry": vrrpv3OperationsEntry,
       "vrrpv3OperationsVrId": vrrpv3OperationsVrId,
       "vrrpv3OperationsInetAddrType": vrrpv3OperationsInetAddrType,
       "vrrpv3OperationsMasterIpAddr": vrrpv3OperationsMasterIpAddr,
       "vrrpv3OperationsPrimaryIpAddr": vrrpv3OperationsPrimaryIpAddr,
       "vrrpv3OperationsVirtualMacAddr": vrrpv3OperationsVirtualMacAddr,
       "vrrpv3OperationsStatus": vrrpv3OperationsStatus,
       "vrrpv3OperationsPriority": vrrpv3OperationsPriority,
       "vrrpv3OperationsAddrCount": vrrpv3OperationsAddrCount,
       "vrrpv3OperationsAdvInterval": vrrpv3OperationsAdvInterval,
       "vrrpv3OperationsPreemptMode": vrrpv3OperationsPreemptMode,
       "vrrpv3OperationsAcceptMode": vrrpv3OperationsAcceptMode,
       "vrrpv3OperationsUpTime": vrrpv3OperationsUpTime,
       "vrrpv3OperationsRowStatus": vrrpv3OperationsRowStatus,
       "vrrpv3AssociatedIpAddrTable": vrrpv3AssociatedIpAddrTable,
       "vrrpv3AssociatedIpAddrEntry": vrrpv3AssociatedIpAddrEntry,
       "vrrpv3AssociatedIpAddrAddress": vrrpv3AssociatedIpAddrAddress,
       "vrrpv3AssociatedIpAddrRowStatus": vrrpv3AssociatedIpAddrRowStatus,
       "vrrpv3Statistics": vrrpv3Statistics,
       "vrrpv3RouterChecksumErrors": vrrpv3RouterChecksumErrors,
       "vrrpv3RouterVersionErrors": vrrpv3RouterVersionErrors,
       "vrrpv3RouterVrIdErrors": vrrpv3RouterVrIdErrors,
       "vrrpv3GlobalStatisticsDiscontinuityTime": vrrpv3GlobalStatisticsDiscontinuityTime,
       "vrrpv3StatisticsTable": vrrpv3StatisticsTable,
       "vrrpv3StatisticsEntry": vrrpv3StatisticsEntry,
       "vrrpv3StatisticsMasterTransitions": vrrpv3StatisticsMasterTransitions,
       "vrrpv3StatisticsNewMasterReason": vrrpv3StatisticsNewMasterReason,
       "vrrpv3StatisticsRcvdAdvertisements": vrrpv3StatisticsRcvdAdvertisements,
       "vrrpv3StatisticsAdvIntervalErrors": vrrpv3StatisticsAdvIntervalErrors,
       "vrrpv3StatisticsIpTtlErrors": vrrpv3StatisticsIpTtlErrors,
       "vrrpv3StatisticsProtoErrReason": vrrpv3StatisticsProtoErrReason,
       "vrrpv3StatisticsRcvdPriZeroPackets": vrrpv3StatisticsRcvdPriZeroPackets,
       "vrrpv3StatisticsSentPriZeroPackets": vrrpv3StatisticsSentPriZeroPackets,
       "vrrpv3StatisticsRcvdInvalidTypePackets": vrrpv3StatisticsRcvdInvalidTypePackets,
       "vrrpv3StatisticsAddressListErrors": vrrpv3StatisticsAddressListErrors,
       "vrrpv3StatisticsPacketLengthErrors": vrrpv3StatisticsPacketLengthErrors,
       "vrrpv3StatisticsRowDiscontinuityTime": vrrpv3StatisticsRowDiscontinuityTime,
       "vrrpv3StatisticsRefreshRate": vrrpv3StatisticsRefreshRate,
       "vrrpv3Conformance": vrrpv3Conformance,
       "vrrpv3Compliances": vrrpv3Compliances,
       "vrrpv3FullCompliance": vrrpv3FullCompliance,
       "vrrpv3ReadOnlyCompliance": vrrpv3ReadOnlyCompliance,
       "vrrpv3Groups": vrrpv3Groups,
       "vrrpv3OperationsGroup": vrrpv3OperationsGroup,
       "vrrpv3StatisticsGroup": vrrpv3StatisticsGroup,
       "vrrpv3StatisticsDiscontinuityGroup": vrrpv3StatisticsDiscontinuityGroup,
       "vrrpv3InfoGroup": vrrpv3InfoGroup,
       "vrrpv3NotificationsGroup": vrrpv3NotificationsGroup}
)
