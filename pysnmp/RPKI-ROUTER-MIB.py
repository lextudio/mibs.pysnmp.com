# SNMP MIB module (RPKI-ROUTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RPKI-ROUTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:21 2024
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetAutonomousSystemNumber,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetAutonomousSystemNumber",
    "InetPortNumber")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")

(LongUtf8String,) = mibBuilder.importSymbols(
    "SYSAPPL-MIB",
    "LongUtf8String")


# MODULE-IDENTITY

rpkiRtrMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 218)
)
rpkiRtrMIB.setRevisions(
        ("2013-05-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RpkiRtrConnectionType(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("ipsec", 6),
          ("other", 7),
          ("ssh", 1),
          ("tcp", 5),
          ("tcpAO", 4),
          ("tcpMD5", 3),
          ("tls", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RpkiRtrNotifications_ObjectIdentity = ObjectIdentity
rpkiRtrNotifications = _RpkiRtrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 218, 0)
)
_RpkiRtrObjects_ObjectIdentity = ObjectIdentity
rpkiRtrObjects = _RpkiRtrObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 218, 1)
)
_RpkiRtrDiscontinuityTimer_Type = TimeStamp
_RpkiRtrDiscontinuityTimer_Object = MibScalar
rpkiRtrDiscontinuityTimer = _RpkiRtrDiscontinuityTimer_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 1),
    _RpkiRtrDiscontinuityTimer_Type()
)
rpkiRtrDiscontinuityTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrDiscontinuityTimer.setStatus("current")
_RpkiRtrCacheServerTable_Object = MibTable
rpkiRtrCacheServerTable = _RpkiRtrCacheServerTable_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 2)
)
if mibBuilder.loadTexts:
    rpkiRtrCacheServerTable.setStatus("current")
_RpkiRtrCacheServerTableEntry_Object = MibTableRow
rpkiRtrCacheServerTableEntry = _RpkiRtrCacheServerTableEntry_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 2, 1)
)
rpkiRtrCacheServerTableEntry.setIndexNames(
    (0, "RPKI-ROUTER-MIB", "rpkiRtrCacheServerRemoteAddressType"),
    (0, "RPKI-ROUTER-MIB", "rpkiRtrCacheServerRemoteAddress"),
    (0, "RPKI-ROUTER-MIB", "rpkiRtrCacheServerRemotePort"),
)
if mibBuilder.loadTexts:
    rpkiRtrCacheServerTableEntry.setStatus("current")
_RpkiRtrCacheServerRemoteAddressType_Type = InetAddressType
_RpkiRtrCacheServerRemoteAddressType_Object = MibTableColumn
rpkiRtrCacheServerRemoteAddressType = _RpkiRtrCacheServerRemoteAddressType_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 2, 1, 1),
    _RpkiRtrCacheServerRemoteAddressType_Type()
)
rpkiRtrCacheServerRemoteAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerRemoteAddressType.setStatus("current")
_RpkiRtrCacheServerRemoteAddress_Type = InetAddress
_RpkiRtrCacheServerRemoteAddress_Object = MibTableColumn
rpkiRtrCacheServerRemoteAddress = _RpkiRtrCacheServerRemoteAddress_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 2, 1, 2),
    _RpkiRtrCacheServerRemoteAddress_Type()
)
rpkiRtrCacheServerRemoteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerRemoteAddress.setStatus("current")


class _RpkiRtrCacheServerRemotePort_Type(InetPortNumber):
    """Custom type rpkiRtrCacheServerRemotePort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RpkiRtrCacheServerRemotePort_Type.__name__ = "InetPortNumber"
_RpkiRtrCacheServerRemotePort_Object = MibTableColumn
rpkiRtrCacheServerRemotePort = _RpkiRtrCacheServerRemotePort_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 2, 1, 3),
    _RpkiRtrCacheServerRemotePort_Type()
)
rpkiRtrCacheServerRemotePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerRemotePort.setStatus("current")
_RpkiRtrCacheServerLocalAddressType_Type = InetAddressType
_RpkiRtrCacheServerLocalAddressType_Object = MibTableColumn
rpkiRtrCacheServerLocalAddressType = _RpkiRtrCacheServerLocalAddressType_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 2, 1, 4),
    _RpkiRtrCacheServerLocalAddressType_Type()
)
rpkiRtrCacheServerLocalAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerLocalAddressType.setStatus("current")
_RpkiRtrCacheServerLocalAddress_Type = InetAddress
_RpkiRtrCacheServerLocalAddress_Object = MibTableColumn
rpkiRtrCacheServerLocalAddress = _RpkiRtrCacheServerLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 2, 1, 5),
    _RpkiRtrCacheServerLocalAddress_Type()
)
rpkiRtrCacheServerLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerLocalAddress.setStatus("current")


class _RpkiRtrCacheServerLocalPort_Type(InetPortNumber):
    """Custom type rpkiRtrCacheServerLocalPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RpkiRtrCacheServerLocalPort_Type.__name__ = "InetPortNumber"
_RpkiRtrCacheServerLocalPort_Object = MibTableColumn
rpkiRtrCacheServerLocalPort = _RpkiRtrCacheServerLocalPort_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 2, 1, 6),
    _RpkiRtrCacheServerLocalPort_Type()
)
rpkiRtrCacheServerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerLocalPort.setStatus("current")


class _RpkiRtrCacheServerPreference_Type(Unsigned32):
    """Custom type rpkiRtrCacheServerPreference based on Unsigned32"""
    defaultValue = 4294967295


_RpkiRtrCacheServerPreference_Object = MibTableColumn
rpkiRtrCacheServerPreference = _RpkiRtrCacheServerPreference_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 2, 1, 7),
    _RpkiRtrCacheServerPreference_Type()
)
rpkiRtrCacheServerPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerPreference.setStatus("current")
_RpkiRtrCacheServerConnectionType_Type = RpkiRtrConnectionType
_RpkiRtrCacheServerConnectionType_Object = MibTableColumn
rpkiRtrCacheServerConnectionType = _RpkiRtrCacheServerConnectionType_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 2, 1, 8),
    _RpkiRtrCacheServerConnectionType_Type()
)
rpkiRtrCacheServerConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerConnectionType.setStatus("current")


class _RpkiRtrCacheServerConnectionStatus_Type(Integer32):
    """Custom type rpkiRtrCacheServerConnectionStatus based on Integer32"""
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


_RpkiRtrCacheServerConnectionStatus_Type.__name__ = "Integer32"
_RpkiRtrCacheServerConnectionStatus_Object = MibTableColumn
rpkiRtrCacheServerConnectionStatus = _RpkiRtrCacheServerConnectionStatus_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 2, 1, 9),
    _RpkiRtrCacheServerConnectionStatus_Type()
)
rpkiRtrCacheServerConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerConnectionStatus.setStatus("current")
_RpkiRtrCacheServerDescription_Type = LongUtf8String
_RpkiRtrCacheServerDescription_Object = MibTableColumn
rpkiRtrCacheServerDescription = _RpkiRtrCacheServerDescription_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 2, 1, 10),
    _RpkiRtrCacheServerDescription_Type()
)
rpkiRtrCacheServerDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerDescription.setStatus("current")
_RpkiRtrCacheServerMsgsReceived_Type = Counter32
_RpkiRtrCacheServerMsgsReceived_Object = MibTableColumn
rpkiRtrCacheServerMsgsReceived = _RpkiRtrCacheServerMsgsReceived_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 2, 1, 11),
    _RpkiRtrCacheServerMsgsReceived_Type()
)
rpkiRtrCacheServerMsgsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerMsgsReceived.setStatus("current")
_RpkiRtrCacheServerMsgsSent_Type = Counter32
_RpkiRtrCacheServerMsgsSent_Object = MibTableColumn
rpkiRtrCacheServerMsgsSent = _RpkiRtrCacheServerMsgsSent_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 2, 1, 12),
    _RpkiRtrCacheServerMsgsSent_Type()
)
rpkiRtrCacheServerMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerMsgsSent.setStatus("current")
_RpkiRtrCacheServerV4ActiveRecords_Type = Gauge32
_RpkiRtrCacheServerV4ActiveRecords_Object = MibTableColumn
rpkiRtrCacheServerV4ActiveRecords = _RpkiRtrCacheServerV4ActiveRecords_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 2, 1, 13),
    _RpkiRtrCacheServerV4ActiveRecords_Type()
)
rpkiRtrCacheServerV4ActiveRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerV4ActiveRecords.setStatus("current")
_RpkiRtrCacheServerV4Announcements_Type = Counter32
_RpkiRtrCacheServerV4Announcements_Object = MibTableColumn
rpkiRtrCacheServerV4Announcements = _RpkiRtrCacheServerV4Announcements_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 2, 1, 14),
    _RpkiRtrCacheServerV4Announcements_Type()
)
rpkiRtrCacheServerV4Announcements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerV4Announcements.setStatus("current")
_RpkiRtrCacheServerV4Withdrawals_Type = Counter32
_RpkiRtrCacheServerV4Withdrawals_Object = MibTableColumn
rpkiRtrCacheServerV4Withdrawals = _RpkiRtrCacheServerV4Withdrawals_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 2, 1, 15),
    _RpkiRtrCacheServerV4Withdrawals_Type()
)
rpkiRtrCacheServerV4Withdrawals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerV4Withdrawals.setStatus("current")
_RpkiRtrCacheServerV6ActiveRecords_Type = Gauge32
_RpkiRtrCacheServerV6ActiveRecords_Object = MibTableColumn
rpkiRtrCacheServerV6ActiveRecords = _RpkiRtrCacheServerV6ActiveRecords_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 2, 1, 16),
    _RpkiRtrCacheServerV6ActiveRecords_Type()
)
rpkiRtrCacheServerV6ActiveRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerV6ActiveRecords.setStatus("current")
_RpkiRtrCacheServerV6Announcements_Type = Counter32
_RpkiRtrCacheServerV6Announcements_Object = MibTableColumn
rpkiRtrCacheServerV6Announcements = _RpkiRtrCacheServerV6Announcements_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 2, 1, 17),
    _RpkiRtrCacheServerV6Announcements_Type()
)
rpkiRtrCacheServerV6Announcements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerV6Announcements.setStatus("current")
_RpkiRtrCacheServerV6Withdrawals_Type = Counter32
_RpkiRtrCacheServerV6Withdrawals_Object = MibTableColumn
rpkiRtrCacheServerV6Withdrawals = _RpkiRtrCacheServerV6Withdrawals_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 2, 1, 18),
    _RpkiRtrCacheServerV6Withdrawals_Type()
)
rpkiRtrCacheServerV6Withdrawals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerV6Withdrawals.setStatus("current")
_RpkiRtrCacheServerLatestSerial_Type = Unsigned32
_RpkiRtrCacheServerLatestSerial_Object = MibTableColumn
rpkiRtrCacheServerLatestSerial = _RpkiRtrCacheServerLatestSerial_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 2, 1, 19),
    _RpkiRtrCacheServerLatestSerial_Type()
)
rpkiRtrCacheServerLatestSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerLatestSerial.setStatus("current")


class _RpkiRtrCacheServerSessionID_Type(Unsigned32):
    """Custom type rpkiRtrCacheServerSessionID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RpkiRtrCacheServerSessionID_Type.__name__ = "Unsigned32"
_RpkiRtrCacheServerSessionID_Object = MibTableColumn
rpkiRtrCacheServerSessionID = _RpkiRtrCacheServerSessionID_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 2, 1, 20),
    _RpkiRtrCacheServerSessionID_Type()
)
rpkiRtrCacheServerSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerSessionID.setStatus("current")


class _RpkiRtrCacheServerRefreshTimer_Type(Unsigned32):
    """Custom type rpkiRtrCacheServerRefreshTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 7200),
    )


_RpkiRtrCacheServerRefreshTimer_Type.__name__ = "Unsigned32"
_RpkiRtrCacheServerRefreshTimer_Object = MibTableColumn
rpkiRtrCacheServerRefreshTimer = _RpkiRtrCacheServerRefreshTimer_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 2, 1, 21),
    _RpkiRtrCacheServerRefreshTimer_Type()
)
rpkiRtrCacheServerRefreshTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerRefreshTimer.setStatus("current")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerRefreshTimer.setUnits("seconds")
_RpkiRtrCacheServerTimeToRefresh_Type = Integer32
_RpkiRtrCacheServerTimeToRefresh_Object = MibTableColumn
rpkiRtrCacheServerTimeToRefresh = _RpkiRtrCacheServerTimeToRefresh_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 2, 1, 22),
    _RpkiRtrCacheServerTimeToRefresh_Type()
)
rpkiRtrCacheServerTimeToRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerTimeToRefresh.setStatus("current")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerTimeToRefresh.setUnits("seconds")


class _RpkiRtrCacheServerId_Type(Unsigned32):
    """Custom type rpkiRtrCacheServerId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RpkiRtrCacheServerId_Type.__name__ = "Unsigned32"
_RpkiRtrCacheServerId_Object = MibTableColumn
rpkiRtrCacheServerId = _RpkiRtrCacheServerId_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 2, 1, 23),
    _RpkiRtrCacheServerId_Type()
)
rpkiRtrCacheServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerId.setStatus("current")
_RpkiRtrCacheServerErrorsTable_Object = MibTable
rpkiRtrCacheServerErrorsTable = _RpkiRtrCacheServerErrorsTable_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 3)
)
if mibBuilder.loadTexts:
    rpkiRtrCacheServerErrorsTable.setStatus("current")
_RpkiRtrCacheServerErrorsTableEntry_Object = MibTableRow
rpkiRtrCacheServerErrorsTableEntry = _RpkiRtrCacheServerErrorsTableEntry_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rpkiRtrCacheServerErrorsTableEntry.setStatus("current")
_RpkiRtrCacheServerErrorsCorruptData_Type = Counter32
_RpkiRtrCacheServerErrorsCorruptData_Object = MibTableColumn
rpkiRtrCacheServerErrorsCorruptData = _RpkiRtrCacheServerErrorsCorruptData_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 3, 1, 1),
    _RpkiRtrCacheServerErrorsCorruptData_Type()
)
rpkiRtrCacheServerErrorsCorruptData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerErrorsCorruptData.setStatus("current")
_RpkiRtrCacheServerErrorsInternalError_Type = Counter32
_RpkiRtrCacheServerErrorsInternalError_Object = MibTableColumn
rpkiRtrCacheServerErrorsInternalError = _RpkiRtrCacheServerErrorsInternalError_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 3, 1, 2),
    _RpkiRtrCacheServerErrorsInternalError_Type()
)
rpkiRtrCacheServerErrorsInternalError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerErrorsInternalError.setStatus("current")
_RpkiRtrCacheServerErrorsNoData_Type = Counter32
_RpkiRtrCacheServerErrorsNoData_Object = MibTableColumn
rpkiRtrCacheServerErrorsNoData = _RpkiRtrCacheServerErrorsNoData_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 3, 1, 3),
    _RpkiRtrCacheServerErrorsNoData_Type()
)
rpkiRtrCacheServerErrorsNoData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerErrorsNoData.setStatus("current")
_RpkiRtrCacheServerErrorsInvalidRequest_Type = Counter32
_RpkiRtrCacheServerErrorsInvalidRequest_Object = MibTableColumn
rpkiRtrCacheServerErrorsInvalidRequest = _RpkiRtrCacheServerErrorsInvalidRequest_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 3, 1, 4),
    _RpkiRtrCacheServerErrorsInvalidRequest_Type()
)
rpkiRtrCacheServerErrorsInvalidRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerErrorsInvalidRequest.setStatus("current")
_RpkiRtrCacheServerErrorsUnsupportedVersion_Type = Counter32
_RpkiRtrCacheServerErrorsUnsupportedVersion_Object = MibTableColumn
rpkiRtrCacheServerErrorsUnsupportedVersion = _RpkiRtrCacheServerErrorsUnsupportedVersion_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 3, 1, 5),
    _RpkiRtrCacheServerErrorsUnsupportedVersion_Type()
)
rpkiRtrCacheServerErrorsUnsupportedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerErrorsUnsupportedVersion.setStatus("current")
_RpkiRtrCacheServerErrorsUnsupportedPdu_Type = Counter32
_RpkiRtrCacheServerErrorsUnsupportedPdu_Object = MibTableColumn
rpkiRtrCacheServerErrorsUnsupportedPdu = _RpkiRtrCacheServerErrorsUnsupportedPdu_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 3, 1, 6),
    _RpkiRtrCacheServerErrorsUnsupportedPdu_Type()
)
rpkiRtrCacheServerErrorsUnsupportedPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerErrorsUnsupportedPdu.setStatus("current")
_RpkiRtrCacheServerErrorsWithdrawalUnknown_Type = Counter32
_RpkiRtrCacheServerErrorsWithdrawalUnknown_Object = MibTableColumn
rpkiRtrCacheServerErrorsWithdrawalUnknown = _RpkiRtrCacheServerErrorsWithdrawalUnknown_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 3, 1, 7),
    _RpkiRtrCacheServerErrorsWithdrawalUnknown_Type()
)
rpkiRtrCacheServerErrorsWithdrawalUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerErrorsWithdrawalUnknown.setStatus("current")
_RpkiRtrCacheServerErrorsDuplicateAnnounce_Type = Counter32
_RpkiRtrCacheServerErrorsDuplicateAnnounce_Object = MibTableColumn
rpkiRtrCacheServerErrorsDuplicateAnnounce = _RpkiRtrCacheServerErrorsDuplicateAnnounce_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 3, 1, 8),
    _RpkiRtrCacheServerErrorsDuplicateAnnounce_Type()
)
rpkiRtrCacheServerErrorsDuplicateAnnounce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrCacheServerErrorsDuplicateAnnounce.setStatus("current")
_RpkiRtrPrefixOriginTable_Object = MibTable
rpkiRtrPrefixOriginTable = _RpkiRtrPrefixOriginTable_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 4)
)
if mibBuilder.loadTexts:
    rpkiRtrPrefixOriginTable.setStatus("current")
_RpkiRtrPrefixOriginTableEntry_Object = MibTableRow
rpkiRtrPrefixOriginTableEntry = _RpkiRtrPrefixOriginTableEntry_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 4, 1)
)
rpkiRtrPrefixOriginTableEntry.setIndexNames(
    (0, "RPKI-ROUTER-MIB", "rpkiRtrPrefixOriginAddressType"),
    (0, "RPKI-ROUTER-MIB", "rpkiRtrPrefixOriginAddress"),
    (0, "RPKI-ROUTER-MIB", "rpkiRtrPrefixOriginMinLength"),
    (0, "RPKI-ROUTER-MIB", "rpkiRtrPrefixOriginMaxLength"),
    (0, "RPKI-ROUTER-MIB", "rpkiRtrPrefixOriginASN"),
    (0, "RPKI-ROUTER-MIB", "rpkiRtrPrefixOriginCacheServerId"),
)
if mibBuilder.loadTexts:
    rpkiRtrPrefixOriginTableEntry.setStatus("current")
_RpkiRtrPrefixOriginAddressType_Type = InetAddressType
_RpkiRtrPrefixOriginAddressType_Object = MibTableColumn
rpkiRtrPrefixOriginAddressType = _RpkiRtrPrefixOriginAddressType_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 4, 1, 1),
    _RpkiRtrPrefixOriginAddressType_Type()
)
rpkiRtrPrefixOriginAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rpkiRtrPrefixOriginAddressType.setStatus("current")
_RpkiRtrPrefixOriginAddress_Type = InetAddress
_RpkiRtrPrefixOriginAddress_Object = MibTableColumn
rpkiRtrPrefixOriginAddress = _RpkiRtrPrefixOriginAddress_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 4, 1, 2),
    _RpkiRtrPrefixOriginAddress_Type()
)
rpkiRtrPrefixOriginAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rpkiRtrPrefixOriginAddress.setStatus("current")
_RpkiRtrPrefixOriginMinLength_Type = InetAddressPrefixLength
_RpkiRtrPrefixOriginMinLength_Object = MibTableColumn
rpkiRtrPrefixOriginMinLength = _RpkiRtrPrefixOriginMinLength_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 4, 1, 3),
    _RpkiRtrPrefixOriginMinLength_Type()
)
rpkiRtrPrefixOriginMinLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rpkiRtrPrefixOriginMinLength.setStatus("current")
_RpkiRtrPrefixOriginMaxLength_Type = InetAddressPrefixLength
_RpkiRtrPrefixOriginMaxLength_Object = MibTableColumn
rpkiRtrPrefixOriginMaxLength = _RpkiRtrPrefixOriginMaxLength_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 4, 1, 4),
    _RpkiRtrPrefixOriginMaxLength_Type()
)
rpkiRtrPrefixOriginMaxLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rpkiRtrPrefixOriginMaxLength.setStatus("current")


class _RpkiRtrPrefixOriginASN_Type(InetAutonomousSystemNumber):
    """Custom type rpkiRtrPrefixOriginASN based on InetAutonomousSystemNumber"""
    subtypeSpec = InetAutonomousSystemNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RpkiRtrPrefixOriginASN_Type.__name__ = "InetAutonomousSystemNumber"
_RpkiRtrPrefixOriginASN_Object = MibTableColumn
rpkiRtrPrefixOriginASN = _RpkiRtrPrefixOriginASN_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 4, 1, 5),
    _RpkiRtrPrefixOriginASN_Type()
)
rpkiRtrPrefixOriginASN.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rpkiRtrPrefixOriginASN.setStatus("current")


class _RpkiRtrPrefixOriginCacheServerId_Type(Unsigned32):
    """Custom type rpkiRtrPrefixOriginCacheServerId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RpkiRtrPrefixOriginCacheServerId_Type.__name__ = "Unsigned32"
_RpkiRtrPrefixOriginCacheServerId_Object = MibTableColumn
rpkiRtrPrefixOriginCacheServerId = _RpkiRtrPrefixOriginCacheServerId_Object(
    (1, 3, 6, 1, 2, 1, 218, 1, 4, 1, 6),
    _RpkiRtrPrefixOriginCacheServerId_Type()
)
rpkiRtrPrefixOriginCacheServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpkiRtrPrefixOriginCacheServerId.setStatus("current")
_RpkiRtrConformance_ObjectIdentity = ObjectIdentity
rpkiRtrConformance = _RpkiRtrConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 218, 2)
)
_RpkiRtrCompliances_ObjectIdentity = ObjectIdentity
rpkiRtrCompliances = _RpkiRtrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 218, 2, 1)
)
_RpkiRtrGroups_ObjectIdentity = ObjectIdentity
rpkiRtrGroups = _RpkiRtrGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 218, 2, 2)
)
rpkiRtrCacheServerTableEntry.registerAugmentions(
    ("RPKI-ROUTER-MIB",
     "rpkiRtrCacheServerErrorsTableEntry")
)
rpkiRtrCacheServerErrorsTableEntry.setIndexNames(*rpkiRtrCacheServerTableEntry.getIndexNames())

# Managed Objects groups

rpkiRtrCacheServerGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 218, 2, 2, 1)
)
rpkiRtrCacheServerGroup.setObjects(
      *(("RPKI-ROUTER-MIB", "rpkiRtrDiscontinuityTimer"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerLocalAddressType"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerLocalAddress"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerLocalPort"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerPreference"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerConnectionType"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerConnectionStatus"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerDescription"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerMsgsReceived"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerMsgsSent"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerV4ActiveRecords"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerV4Announcements"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerV4Withdrawals"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerV6ActiveRecords"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerV6Announcements"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerV6Withdrawals"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerLatestSerial"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerSessionID"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerRefreshTimer"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerTimeToRefresh"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerId"))
)
if mibBuilder.loadTexts:
    rpkiRtrCacheServerGroup.setStatus("current")

rpkiRtrCacheServerErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 218, 2, 2, 2)
)
rpkiRtrCacheServerErrorsGroup.setObjects(
      *(("RPKI-ROUTER-MIB", "rpkiRtrCacheServerErrorsCorruptData"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerErrorsInternalError"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerErrorsNoData"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerErrorsInvalidRequest"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerErrorsUnsupportedVersion"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerErrorsUnsupportedPdu"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerErrorsWithdrawalUnknown"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerErrorsDuplicateAnnounce"))
)
if mibBuilder.loadTexts:
    rpkiRtrCacheServerErrorsGroup.setStatus("current")

rpkiRtrPrefixOriginGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 218, 2, 2, 3)
)
rpkiRtrPrefixOriginGroup.setObjects(
    ("RPKI-ROUTER-MIB", "rpkiRtrPrefixOriginCacheServerId")
)
if mibBuilder.loadTexts:
    rpkiRtrPrefixOriginGroup.setStatus("current")


# Notification objects

rpkiRtrCacheServerConnectionStateChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 218, 0, 1)
)
rpkiRtrCacheServerConnectionStateChange.setObjects(
      *(("RPKI-ROUTER-MIB", "rpkiRtrCacheServerConnectionStatus"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerLatestSerial"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerSessionID"))
)
if mibBuilder.loadTexts:
    rpkiRtrCacheServerConnectionStateChange.setStatus(
        "current"
    )

rpkiRtrCacheServerConnectionToGoStale = NotificationType(
    (1, 3, 6, 1, 2, 1, 218, 0, 2)
)
rpkiRtrCacheServerConnectionToGoStale.setObjects(
      *(("RPKI-ROUTER-MIB", "rpkiRtrCacheServerV4ActiveRecords"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerV6ActiveRecords"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerLatestSerial"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerSessionID"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerRefreshTimer"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerTimeToRefresh"))
)
if mibBuilder.loadTexts:
    rpkiRtrCacheServerConnectionToGoStale.setStatus(
        "current"
    )


# Notifications groups

rpkiRtrNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 218, 2, 2, 4)
)
rpkiRtrNotificationsGroup.setObjects(
      *(("RPKI-ROUTER-MIB", "rpkiRtrCacheServerConnectionStateChange"),
        ("RPKI-ROUTER-MIB", "rpkiRtrCacheServerConnectionToGoStale"))
)
if mibBuilder.loadTexts:
    rpkiRtrNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rpkiRtrRFC6945ReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 218, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rpkiRtrRFC6945ReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RPKI-ROUTER-MIB",
    **{"RpkiRtrConnectionType": RpkiRtrConnectionType,
       "rpkiRtrMIB": rpkiRtrMIB,
       "rpkiRtrNotifications": rpkiRtrNotifications,
       "rpkiRtrCacheServerConnectionStateChange": rpkiRtrCacheServerConnectionStateChange,
       "rpkiRtrCacheServerConnectionToGoStale": rpkiRtrCacheServerConnectionToGoStale,
       "rpkiRtrObjects": rpkiRtrObjects,
       "rpkiRtrDiscontinuityTimer": rpkiRtrDiscontinuityTimer,
       "rpkiRtrCacheServerTable": rpkiRtrCacheServerTable,
       "rpkiRtrCacheServerTableEntry": rpkiRtrCacheServerTableEntry,
       "rpkiRtrCacheServerRemoteAddressType": rpkiRtrCacheServerRemoteAddressType,
       "rpkiRtrCacheServerRemoteAddress": rpkiRtrCacheServerRemoteAddress,
       "rpkiRtrCacheServerRemotePort": rpkiRtrCacheServerRemotePort,
       "rpkiRtrCacheServerLocalAddressType": rpkiRtrCacheServerLocalAddressType,
       "rpkiRtrCacheServerLocalAddress": rpkiRtrCacheServerLocalAddress,
       "rpkiRtrCacheServerLocalPort": rpkiRtrCacheServerLocalPort,
       "rpkiRtrCacheServerPreference": rpkiRtrCacheServerPreference,
       "rpkiRtrCacheServerConnectionType": rpkiRtrCacheServerConnectionType,
       "rpkiRtrCacheServerConnectionStatus": rpkiRtrCacheServerConnectionStatus,
       "rpkiRtrCacheServerDescription": rpkiRtrCacheServerDescription,
       "rpkiRtrCacheServerMsgsReceived": rpkiRtrCacheServerMsgsReceived,
       "rpkiRtrCacheServerMsgsSent": rpkiRtrCacheServerMsgsSent,
       "rpkiRtrCacheServerV4ActiveRecords": rpkiRtrCacheServerV4ActiveRecords,
       "rpkiRtrCacheServerV4Announcements": rpkiRtrCacheServerV4Announcements,
       "rpkiRtrCacheServerV4Withdrawals": rpkiRtrCacheServerV4Withdrawals,
       "rpkiRtrCacheServerV6ActiveRecords": rpkiRtrCacheServerV6ActiveRecords,
       "rpkiRtrCacheServerV6Announcements": rpkiRtrCacheServerV6Announcements,
       "rpkiRtrCacheServerV6Withdrawals": rpkiRtrCacheServerV6Withdrawals,
       "rpkiRtrCacheServerLatestSerial": rpkiRtrCacheServerLatestSerial,
       "rpkiRtrCacheServerSessionID": rpkiRtrCacheServerSessionID,
       "rpkiRtrCacheServerRefreshTimer": rpkiRtrCacheServerRefreshTimer,
       "rpkiRtrCacheServerTimeToRefresh": rpkiRtrCacheServerTimeToRefresh,
       "rpkiRtrCacheServerId": rpkiRtrCacheServerId,
       "rpkiRtrCacheServerErrorsTable": rpkiRtrCacheServerErrorsTable,
       "rpkiRtrCacheServerErrorsTableEntry": rpkiRtrCacheServerErrorsTableEntry,
       "rpkiRtrCacheServerErrorsCorruptData": rpkiRtrCacheServerErrorsCorruptData,
       "rpkiRtrCacheServerErrorsInternalError": rpkiRtrCacheServerErrorsInternalError,
       "rpkiRtrCacheServerErrorsNoData": rpkiRtrCacheServerErrorsNoData,
       "rpkiRtrCacheServerErrorsInvalidRequest": rpkiRtrCacheServerErrorsInvalidRequest,
       "rpkiRtrCacheServerErrorsUnsupportedVersion": rpkiRtrCacheServerErrorsUnsupportedVersion,
       "rpkiRtrCacheServerErrorsUnsupportedPdu": rpkiRtrCacheServerErrorsUnsupportedPdu,
       "rpkiRtrCacheServerErrorsWithdrawalUnknown": rpkiRtrCacheServerErrorsWithdrawalUnknown,
       "rpkiRtrCacheServerErrorsDuplicateAnnounce": rpkiRtrCacheServerErrorsDuplicateAnnounce,
       "rpkiRtrPrefixOriginTable": rpkiRtrPrefixOriginTable,
       "rpkiRtrPrefixOriginTableEntry": rpkiRtrPrefixOriginTableEntry,
       "rpkiRtrPrefixOriginAddressType": rpkiRtrPrefixOriginAddressType,
       "rpkiRtrPrefixOriginAddress": rpkiRtrPrefixOriginAddress,
       "rpkiRtrPrefixOriginMinLength": rpkiRtrPrefixOriginMinLength,
       "rpkiRtrPrefixOriginMaxLength": rpkiRtrPrefixOriginMaxLength,
       "rpkiRtrPrefixOriginASN": rpkiRtrPrefixOriginASN,
       "rpkiRtrPrefixOriginCacheServerId": rpkiRtrPrefixOriginCacheServerId,
       "rpkiRtrConformance": rpkiRtrConformance,
       "rpkiRtrCompliances": rpkiRtrCompliances,
       "rpkiRtrRFC6945ReadOnlyCompliance": rpkiRtrRFC6945ReadOnlyCompliance,
       "rpkiRtrGroups": rpkiRtrGroups,
       "rpkiRtrCacheServerGroup": rpkiRtrCacheServerGroup,
       "rpkiRtrCacheServerErrorsGroup": rpkiRtrCacheServerErrorsGroup,
       "rpkiRtrPrefixOriginGroup": rpkiRtrPrefixOriginGroup,
       "rpkiRtrNotificationsGroup": rpkiRtrNotificationsGroup}
)
