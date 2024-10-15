# SNMP MIB module (CISCO-IETF-VRRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-VRRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:07 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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

ciscoVrrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999)
)
ciscoVrrpMIB.setRevisions(
        ("2005-11-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CVrId(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_CVrrpNotifications_ObjectIdentity = ObjectIdentity
cVrrpNotifications = _CVrrpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 0)
)
_CVrrpOperations_ObjectIdentity = ObjectIdentity
cVrrpOperations = _CVrrpOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1)
)


class _CVrrpNotificationCntl_Type(Integer32):
    """Custom type cVrrpNotificationCntl based on Integer32"""
    defaultValue = 1

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


_CVrrpNotificationCntl_Type.__name__ = "Integer32"
_CVrrpNotificationCntl_Object = MibScalar
cVrrpNotificationCntl = _CVrrpNotificationCntl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 2),
    _CVrrpNotificationCntl_Type()
)
cVrrpNotificationCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cVrrpNotificationCntl.setStatus("current")
_CVrrpOperationsTable_Object = MibTable
cVrrpOperationsTable = _CVrrpOperationsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7)
)
if mibBuilder.loadTexts:
    cVrrpOperationsTable.setStatus("current")
_CVrrpOperationsEntry_Object = MibTableRow
cVrrpOperationsEntry = _CVrrpOperationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1)
)
cVrrpOperationsEntry.setIndexNames(
    (0, "CISCO-IETF-VRRP-MIB", "cVrrpOperationsInetAddrType"),
    (0, "CISCO-IETF-VRRP-MIB", "cVrrpOperationsVrId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cVrrpOperationsEntry.setStatus("current")
_CVrrpOperationsInetAddrType_Type = InetAddressType
_CVrrpOperationsInetAddrType_Object = MibTableColumn
cVrrpOperationsInetAddrType = _CVrrpOperationsInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 1),
    _CVrrpOperationsInetAddrType_Type()
)
cVrrpOperationsInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cVrrpOperationsInetAddrType.setStatus("current")
_CVrrpOperationsVrId_Type = CVrId
_CVrrpOperationsVrId_Object = MibTableColumn
cVrrpOperationsVrId = _CVrrpOperationsVrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 2),
    _CVrrpOperationsVrId_Type()
)
cVrrpOperationsVrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cVrrpOperationsVrId.setStatus("current")
_CVrrpOperationsVirtualMacAddr_Type = MacAddress
_CVrrpOperationsVirtualMacAddr_Object = MibTableColumn
cVrrpOperationsVirtualMacAddr = _CVrrpOperationsVirtualMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 3),
    _CVrrpOperationsVirtualMacAddr_Type()
)
cVrrpOperationsVirtualMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVrrpOperationsVirtualMacAddr.setStatus("current")


class _CVrrpOperationsState_Type(Integer32):
    """Custom type cVrrpOperationsState based on Integer32"""
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


_CVrrpOperationsState_Type.__name__ = "Integer32"
_CVrrpOperationsState_Object = MibTableColumn
cVrrpOperationsState = _CVrrpOperationsState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 4),
    _CVrrpOperationsState_Type()
)
cVrrpOperationsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVrrpOperationsState.setStatus("current")


class _CVrrpOperationsPriority_Type(Integer32):
    """Custom type cVrrpOperationsPriority based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CVrrpOperationsPriority_Type.__name__ = "Integer32"
_CVrrpOperationsPriority_Object = MibTableColumn
cVrrpOperationsPriority = _CVrrpOperationsPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 5),
    _CVrrpOperationsPriority_Type()
)
cVrrpOperationsPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cVrrpOperationsPriority.setStatus("current")


class _CVrrpOperationsVersion_Type(Integer32):
    """Custom type cVrrpOperationsVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vrrpv2", 1),
          ("vrrpv3", 2))
    )


_CVrrpOperationsVersion_Type.__name__ = "Integer32"
_CVrrpOperationsVersion_Object = MibTableColumn
cVrrpOperationsVersion = _CVrrpOperationsVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 6),
    _CVrrpOperationsVersion_Type()
)
cVrrpOperationsVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cVrrpOperationsVersion.setStatus("current")


class _CVrrpOperationsAddrCount_Type(Integer32):
    """Custom type cVrrpOperationsAddrCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CVrrpOperationsAddrCount_Type.__name__ = "Integer32"
_CVrrpOperationsAddrCount_Object = MibTableColumn
cVrrpOperationsAddrCount = _CVrrpOperationsAddrCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 7),
    _CVrrpOperationsAddrCount_Type()
)
cVrrpOperationsAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVrrpOperationsAddrCount.setStatus("current")
_CVrrpOperationsMasterIpAddr_Type = InetAddress
_CVrrpOperationsMasterIpAddr_Object = MibTableColumn
cVrrpOperationsMasterIpAddr = _CVrrpOperationsMasterIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 9),
    _CVrrpOperationsMasterIpAddr_Type()
)
cVrrpOperationsMasterIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVrrpOperationsMasterIpAddr.setStatus("current")
_CVrrpOperationsPrimaryIpAddr_Type = InetAddress
_CVrrpOperationsPrimaryIpAddr_Object = MibTableColumn
cVrrpOperationsPrimaryIpAddr = _CVrrpOperationsPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 10),
    _CVrrpOperationsPrimaryIpAddr_Type()
)
cVrrpOperationsPrimaryIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cVrrpOperationsPrimaryIpAddr.setStatus("current")


class _CVrrpOperationsAdvInterval_Type(TimeInterval):
    """Custom type cVrrpOperationsAdvInterval based on TimeInterval"""
    defaultValue = 100

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_CVrrpOperationsAdvInterval_Type.__name__ = "TimeInterval"
_CVrrpOperationsAdvInterval_Object = MibTableColumn
cVrrpOperationsAdvInterval = _CVrrpOperationsAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 11),
    _CVrrpOperationsAdvInterval_Type()
)
cVrrpOperationsAdvInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cVrrpOperationsAdvInterval.setStatus("current")
if mibBuilder.loadTexts:
    cVrrpOperationsAdvInterval.setUnits("centiseconds")


class _CVrrpOperationsPreemptMode_Type(TruthValue):
    """Custom type cVrrpOperationsPreemptMode based on TruthValue"""


_CVrrpOperationsPreemptMode_Object = MibTableColumn
cVrrpOperationsPreemptMode = _CVrrpOperationsPreemptMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 12),
    _CVrrpOperationsPreemptMode_Type()
)
cVrrpOperationsPreemptMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cVrrpOperationsPreemptMode.setStatus("current")


class _CVrrpOperationsAcceptMode_Type(TruthValue):
    """Custom type cVrrpOperationsAcceptMode based on TruthValue"""


_CVrrpOperationsAcceptMode_Object = MibTableColumn
cVrrpOperationsAcceptMode = _CVrrpOperationsAcceptMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 13),
    _CVrrpOperationsAcceptMode_Type()
)
cVrrpOperationsAcceptMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cVrrpOperationsAcceptMode.setStatus("current")
_CVrrpOperationsUpTime_Type = TimeStamp
_CVrrpOperationsUpTime_Object = MibTableColumn
cVrrpOperationsUpTime = _CVrrpOperationsUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 14),
    _CVrrpOperationsUpTime_Type()
)
cVrrpOperationsUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVrrpOperationsUpTime.setStatus("current")
_CVrrpOperationsRowStatus_Type = RowStatus
_CVrrpOperationsRowStatus_Object = MibTableColumn
cVrrpOperationsRowStatus = _CVrrpOperationsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 15),
    _CVrrpOperationsRowStatus_Type()
)
cVrrpOperationsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cVrrpOperationsRowStatus.setStatus("current")
_CVrrpAssociatedIpAddrTable_Object = MibTable
cVrrpAssociatedIpAddrTable = _CVrrpAssociatedIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 8)
)
if mibBuilder.loadTexts:
    cVrrpAssociatedIpAddrTable.setStatus("current")
_CVrrpAssociatedIpAddrEntry_Object = MibTableRow
cVrrpAssociatedIpAddrEntry = _CVrrpAssociatedIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 8, 1)
)
cVrrpAssociatedIpAddrEntry.setIndexNames(
    (0, "CISCO-IETF-VRRP-MIB", "cVrrpAssociatedInetAddrType"),
    (0, "CISCO-IETF-VRRP-MIB", "cVrrpOperationsVrId"),
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IETF-VRRP-MIB", "cVrrpAssociatedIpAddr"),
)
if mibBuilder.loadTexts:
    cVrrpAssociatedIpAddrEntry.setStatus("current")
_CVrrpAssociatedInetAddrType_Type = InetAddressType
_CVrrpAssociatedInetAddrType_Object = MibTableColumn
cVrrpAssociatedInetAddrType = _CVrrpAssociatedInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 8, 1, 2),
    _CVrrpAssociatedInetAddrType_Type()
)
cVrrpAssociatedInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cVrrpAssociatedInetAddrType.setStatus("current")


class _CVrrpAssociatedIpAddr_Type(InetAddress):
    """Custom type cVrrpAssociatedIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_CVrrpAssociatedIpAddr_Type.__name__ = "InetAddress"
_CVrrpAssociatedIpAddr_Object = MibTableColumn
cVrrpAssociatedIpAddr = _CVrrpAssociatedIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 8, 1, 3),
    _CVrrpAssociatedIpAddr_Type()
)
cVrrpAssociatedIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cVrrpAssociatedIpAddr.setStatus("current")
_CVrrpAssociatedIpAddrRowStatus_Type = RowStatus
_CVrrpAssociatedIpAddrRowStatus_Object = MibTableColumn
cVrrpAssociatedIpAddrRowStatus = _CVrrpAssociatedIpAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 8, 1, 4),
    _CVrrpAssociatedIpAddrRowStatus_Type()
)
cVrrpAssociatedIpAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cVrrpAssociatedIpAddrRowStatus.setStatus("current")


class _CVrrpNotificationNewMasterReason_Type(Integer32):
    """Custom type cVrrpNotificationNewMasterReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("masterNoResponse", 2),
          ("preempted", 1),
          ("priority", 0))
    )


_CVrrpNotificationNewMasterReason_Type.__name__ = "Integer32"
_CVrrpNotificationNewMasterReason_Object = MibScalar
cVrrpNotificationNewMasterReason = _CVrrpNotificationNewMasterReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 9),
    _CVrrpNotificationNewMasterReason_Type()
)
cVrrpNotificationNewMasterReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cVrrpNotificationNewMasterReason.setStatus("current")


class _CVrrpNotificationProtoErrReason_Type(Integer32):
    """Custom type cVrrpNotificationProtoErrReason based on Integer32"""
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


_CVrrpNotificationProtoErrReason_Type.__name__ = "Integer32"
_CVrrpNotificationProtoErrReason_Object = MibScalar
cVrrpNotificationProtoErrReason = _CVrrpNotificationProtoErrReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 10),
    _CVrrpNotificationProtoErrReason_Type()
)
cVrrpNotificationProtoErrReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cVrrpNotificationProtoErrReason.setStatus("current")
_CVrrpStatistics_ObjectIdentity = ObjectIdentity
cVrrpStatistics = _CVrrpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2)
)
_CVrrpRouterChecksumErrors_Type = Counter32
_CVrrpRouterChecksumErrors_Object = MibScalar
cVrrpRouterChecksumErrors = _CVrrpRouterChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 1),
    _CVrrpRouterChecksumErrors_Type()
)
cVrrpRouterChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVrrpRouterChecksumErrors.setStatus("current")
_CVrrpRouterVersionErrors_Type = Counter32
_CVrrpRouterVersionErrors_Object = MibScalar
cVrrpRouterVersionErrors = _CVrrpRouterVersionErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 2),
    _CVrrpRouterVersionErrors_Type()
)
cVrrpRouterVersionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVrrpRouterVersionErrors.setStatus("current")
_CVrrpRouterVrIdErrors_Type = Counter32
_CVrrpRouterVrIdErrors_Object = MibScalar
cVrrpRouterVrIdErrors = _CVrrpRouterVrIdErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 3),
    _CVrrpRouterVrIdErrors_Type()
)
cVrrpRouterVrIdErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVrrpRouterVrIdErrors.setStatus("current")
_CVrrpRouterStatisticsTable_Object = MibTable
cVrrpRouterStatisticsTable = _CVrrpRouterStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5)
)
if mibBuilder.loadTexts:
    cVrrpRouterStatisticsTable.setStatus("current")
_CVrrpRouterStatisticsEntry_Object = MibTableRow
cVrrpRouterStatisticsEntry = _CVrrpRouterStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5, 1)
)
cVrrpRouterStatisticsEntry.setIndexNames(
    (0, "CISCO-IETF-VRRP-MIB", "cVrrpOperationsInetAddrType"),
    (0, "CISCO-IETF-VRRP-MIB", "cVrrpOperationsVrId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cVrrpRouterStatisticsEntry.setStatus("current")
_CVrrpStatisticsBecomeMaster_Type = Counter32
_CVrrpStatisticsBecomeMaster_Object = MibTableColumn
cVrrpStatisticsBecomeMaster = _CVrrpStatisticsBecomeMaster_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5, 1, 1),
    _CVrrpStatisticsBecomeMaster_Type()
)
cVrrpStatisticsBecomeMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVrrpStatisticsBecomeMaster.setStatus("current")
_CVrrpStatisticsAdvertiseRcvd_Type = Counter32
_CVrrpStatisticsAdvertiseRcvd_Object = MibTableColumn
cVrrpStatisticsAdvertiseRcvd = _CVrrpStatisticsAdvertiseRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5, 1, 2),
    _CVrrpStatisticsAdvertiseRcvd_Type()
)
cVrrpStatisticsAdvertiseRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVrrpStatisticsAdvertiseRcvd.setStatus("current")
_CVrrpStatisticsAdvIntervalErrors_Type = Counter32
_CVrrpStatisticsAdvIntervalErrors_Object = MibTableColumn
cVrrpStatisticsAdvIntervalErrors = _CVrrpStatisticsAdvIntervalErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5, 1, 3),
    _CVrrpStatisticsAdvIntervalErrors_Type()
)
cVrrpStatisticsAdvIntervalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVrrpStatisticsAdvIntervalErrors.setStatus("current")
_CVrrpStatisticsIpTtlErrors_Type = Counter32
_CVrrpStatisticsIpTtlErrors_Object = MibTableColumn
cVrrpStatisticsIpTtlErrors = _CVrrpStatisticsIpTtlErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5, 1, 4),
    _CVrrpStatisticsIpTtlErrors_Type()
)
cVrrpStatisticsIpTtlErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVrrpStatisticsIpTtlErrors.setStatus("current")
_CVrrpStatisticsPriZeroPktsRcvd_Type = Counter32
_CVrrpStatisticsPriZeroPktsRcvd_Object = MibTableColumn
cVrrpStatisticsPriZeroPktsRcvd = _CVrrpStatisticsPriZeroPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5, 1, 5),
    _CVrrpStatisticsPriZeroPktsRcvd_Type()
)
cVrrpStatisticsPriZeroPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVrrpStatisticsPriZeroPktsRcvd.setStatus("current")
_CVrrpStatisticsPriZeroPktsSent_Type = Counter32
_CVrrpStatisticsPriZeroPktsSent_Object = MibTableColumn
cVrrpStatisticsPriZeroPktsSent = _CVrrpStatisticsPriZeroPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5, 1, 6),
    _CVrrpStatisticsPriZeroPktsSent_Type()
)
cVrrpStatisticsPriZeroPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVrrpStatisticsPriZeroPktsSent.setStatus("current")
_CVrrpStatisticsInvldTypePktsRcvd_Type = Counter32
_CVrrpStatisticsInvldTypePktsRcvd_Object = MibTableColumn
cVrrpStatisticsInvldTypePktsRcvd = _CVrrpStatisticsInvldTypePktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5, 1, 7),
    _CVrrpStatisticsInvldTypePktsRcvd_Type()
)
cVrrpStatisticsInvldTypePktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVrrpStatisticsInvldTypePktsRcvd.setStatus("current")
_CVrrpStatisticsAddressListErrors_Type = Counter32
_CVrrpStatisticsAddressListErrors_Object = MibTableColumn
cVrrpStatisticsAddressListErrors = _CVrrpStatisticsAddressListErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5, 1, 8),
    _CVrrpStatisticsAddressListErrors_Type()
)
cVrrpStatisticsAddressListErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVrrpStatisticsAddressListErrors.setStatus("current")
_CVrrpStatisticsPacketLengthErrors_Type = Counter32
_CVrrpStatisticsPacketLengthErrors_Object = MibTableColumn
cVrrpStatisticsPacketLengthErrors = _CVrrpStatisticsPacketLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5, 1, 11),
    _CVrrpStatisticsPacketLengthErrors_Type()
)
cVrrpStatisticsPacketLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVrrpStatisticsPacketLengthErrors.setStatus("current")
_CVrrpStatisticsDiscontinuityTime_Type = TimeStamp
_CVrrpStatisticsDiscontinuityTime_Object = MibTableColumn
cVrrpStatisticsDiscontinuityTime = _CVrrpStatisticsDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5, 1, 12),
    _CVrrpStatisticsDiscontinuityTime_Type()
)
cVrrpStatisticsDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVrrpStatisticsDiscontinuityTime.setStatus("current")
_CVrrpStatisticsRefreshRate_Type = Unsigned32
_CVrrpStatisticsRefreshRate_Object = MibTableColumn
cVrrpStatisticsRefreshRate = _CVrrpStatisticsRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5, 1, 13),
    _CVrrpStatisticsRefreshRate_Type()
)
cVrrpStatisticsRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVrrpStatisticsRefreshRate.setStatus("current")
if mibBuilder.loadTexts:
    cVrrpStatisticsRefreshRate.setUnits("milli-seconds")
_CVrrpStatisticsInvalidAuthType_Type = Counter32
_CVrrpStatisticsInvalidAuthType_Object = MibTableColumn
cVrrpStatisticsInvalidAuthType = _CVrrpStatisticsInvalidAuthType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5, 1, 14),
    _CVrrpStatisticsInvalidAuthType_Type()
)
cVrrpStatisticsInvalidAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVrrpStatisticsInvalidAuthType.setStatus("current")
_CVrrpConformance_ObjectIdentity = ObjectIdentity
cVrrpConformance = _CVrrpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 3)
)
_CVrrpMIBCompliances_ObjectIdentity = ObjectIdentity
cVrrpMIBCompliances = _CVrrpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 3, 1)
)
_CVrrpMIBGroups_ObjectIdentity = ObjectIdentity
cVrrpMIBGroups = _CVrrpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 3, 2)
)

# Managed Objects groups

cVrrpOperationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 3, 2, 5)
)
cVrrpOperationsGroup.setObjects(
      *(("CISCO-IETF-VRRP-MIB", "cVrrpNotificationCntl"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpOperationsVirtualMacAddr"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpOperationsState"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpOperationsPriority"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpOperationsMasterIpAddr"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpOperationsVersion"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpOperationsAdvInterval"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpOperationsPreemptMode"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpOperationsAcceptMode"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpOperationsUpTime"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpOperationsRowStatus"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpOperationsAddrCount"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpOperationsPrimaryIpAddr"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpAssociatedIpAddrRowStatus"))
)
if mibBuilder.loadTexts:
    cVrrpOperationsGroup.setStatus("current")

cVrrpStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 3, 2, 6)
)
cVrrpStatisticsGroup.setObjects(
      *(("CISCO-IETF-VRRP-MIB", "cVrrpRouterChecksumErrors"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpRouterVersionErrors"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpRouterVrIdErrors"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpStatisticsBecomeMaster"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpStatisticsAdvertiseRcvd"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpStatisticsAdvIntervalErrors"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpStatisticsPriZeroPktsRcvd"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpStatisticsPriZeroPktsSent"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpStatisticsInvldTypePktsRcvd"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpStatisticsIpTtlErrors"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpStatisticsAddressListErrors"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpStatisticsPacketLengthErrors"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpStatisticsDiscontinuityTime"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpStatisticsRefreshRate"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpStatisticsInvalidAuthType"))
)
if mibBuilder.loadTexts:
    cVrrpStatisticsGroup.setStatus("current")

cVrrpNotificationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 3, 2, 8)
)
cVrrpNotificationInfoGroup.setObjects(
      *(("CISCO-IETF-VRRP-MIB", "cVrrpNotificationNewMasterReason"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpNotificationProtoErrReason"))
)
if mibBuilder.loadTexts:
    cVrrpNotificationInfoGroup.setStatus("current")


# Notification objects

cVrrpNotificationNewMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 0, 1)
)
cVrrpNotificationNewMaster.setObjects(
      *(("CISCO-IETF-VRRP-MIB", "cVrrpOperationsMasterIpAddr"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpNotificationNewMasterReason"))
)
if mibBuilder.loadTexts:
    cVrrpNotificationNewMaster.setStatus(
        "current"
    )

cVrrpNotificationProtoError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 0, 3)
)
cVrrpNotificationProtoError.setObjects(
    ("CISCO-IETF-VRRP-MIB", "cVrrpNotificationProtoErrReason")
)
if mibBuilder.loadTexts:
    cVrrpNotificationProtoError.setStatus(
        "current"
    )


# Notifications groups

cVrrpNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 3, 2, 9)
)
cVrrpNotificationsGroup.setObjects(
      *(("CISCO-IETF-VRRP-MIB", "cVrrpNotificationNewMaster"),
        ("CISCO-IETF-VRRP-MIB", "cVrrpNotificationProtoError"))
)
if mibBuilder.loadTexts:
    cVrrpNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cVrrpMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cVrrpMIBCompliance2.setStatus(
        "current"
    )

cVrrpMIBReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cVrrpMIBReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-VRRP-MIB",
    **{"CVrId": CVrId,
       "ciscoVrrpMIB": ciscoVrrpMIB,
       "cVrrpNotifications": cVrrpNotifications,
       "cVrrpNotificationNewMaster": cVrrpNotificationNewMaster,
       "cVrrpNotificationProtoError": cVrrpNotificationProtoError,
       "cVrrpOperations": cVrrpOperations,
       "cVrrpNotificationCntl": cVrrpNotificationCntl,
       "cVrrpOperationsTable": cVrrpOperationsTable,
       "cVrrpOperationsEntry": cVrrpOperationsEntry,
       "cVrrpOperationsInetAddrType": cVrrpOperationsInetAddrType,
       "cVrrpOperationsVrId": cVrrpOperationsVrId,
       "cVrrpOperationsVirtualMacAddr": cVrrpOperationsVirtualMacAddr,
       "cVrrpOperationsState": cVrrpOperationsState,
       "cVrrpOperationsPriority": cVrrpOperationsPriority,
       "cVrrpOperationsVersion": cVrrpOperationsVersion,
       "cVrrpOperationsAddrCount": cVrrpOperationsAddrCount,
       "cVrrpOperationsMasterIpAddr": cVrrpOperationsMasterIpAddr,
       "cVrrpOperationsPrimaryIpAddr": cVrrpOperationsPrimaryIpAddr,
       "cVrrpOperationsAdvInterval": cVrrpOperationsAdvInterval,
       "cVrrpOperationsPreemptMode": cVrrpOperationsPreemptMode,
       "cVrrpOperationsAcceptMode": cVrrpOperationsAcceptMode,
       "cVrrpOperationsUpTime": cVrrpOperationsUpTime,
       "cVrrpOperationsRowStatus": cVrrpOperationsRowStatus,
       "cVrrpAssociatedIpAddrTable": cVrrpAssociatedIpAddrTable,
       "cVrrpAssociatedIpAddrEntry": cVrrpAssociatedIpAddrEntry,
       "cVrrpAssociatedInetAddrType": cVrrpAssociatedInetAddrType,
       "cVrrpAssociatedIpAddr": cVrrpAssociatedIpAddr,
       "cVrrpAssociatedIpAddrRowStatus": cVrrpAssociatedIpAddrRowStatus,
       "cVrrpNotificationNewMasterReason": cVrrpNotificationNewMasterReason,
       "cVrrpNotificationProtoErrReason": cVrrpNotificationProtoErrReason,
       "cVrrpStatistics": cVrrpStatistics,
       "cVrrpRouterChecksumErrors": cVrrpRouterChecksumErrors,
       "cVrrpRouterVersionErrors": cVrrpRouterVersionErrors,
       "cVrrpRouterVrIdErrors": cVrrpRouterVrIdErrors,
       "cVrrpRouterStatisticsTable": cVrrpRouterStatisticsTable,
       "cVrrpRouterStatisticsEntry": cVrrpRouterStatisticsEntry,
       "cVrrpStatisticsBecomeMaster": cVrrpStatisticsBecomeMaster,
       "cVrrpStatisticsAdvertiseRcvd": cVrrpStatisticsAdvertiseRcvd,
       "cVrrpStatisticsAdvIntervalErrors": cVrrpStatisticsAdvIntervalErrors,
       "cVrrpStatisticsIpTtlErrors": cVrrpStatisticsIpTtlErrors,
       "cVrrpStatisticsPriZeroPktsRcvd": cVrrpStatisticsPriZeroPktsRcvd,
       "cVrrpStatisticsPriZeroPktsSent": cVrrpStatisticsPriZeroPktsSent,
       "cVrrpStatisticsInvldTypePktsRcvd": cVrrpStatisticsInvldTypePktsRcvd,
       "cVrrpStatisticsAddressListErrors": cVrrpStatisticsAddressListErrors,
       "cVrrpStatisticsPacketLengthErrors": cVrrpStatisticsPacketLengthErrors,
       "cVrrpStatisticsDiscontinuityTime": cVrrpStatisticsDiscontinuityTime,
       "cVrrpStatisticsRefreshRate": cVrrpStatisticsRefreshRate,
       "cVrrpStatisticsInvalidAuthType": cVrrpStatisticsInvalidAuthType,
       "cVrrpConformance": cVrrpConformance,
       "cVrrpMIBCompliances": cVrrpMIBCompliances,
       "cVrrpMIBCompliance2": cVrrpMIBCompliance2,
       "cVrrpMIBReadOnlyCompliance": cVrrpMIBReadOnlyCompliance,
       "cVrrpMIBGroups": cVrrpMIBGroups,
       "cVrrpOperationsGroup": cVrrpOperationsGroup,
       "cVrrpStatisticsGroup": cVrrpStatisticsGroup,
       "cVrrpNotificationInfoGroup": cVrrpNotificationInfoGroup,
       "cVrrpNotificationsGroup": cVrrpNotificationsGroup}
)
