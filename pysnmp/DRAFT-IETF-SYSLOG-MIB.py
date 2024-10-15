# SNMP MIB module (DRAFT-IETF-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DRAFT-IETF-SYSLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:28 2024
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
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

syslogMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 999999)
)
syslogMIB.setRevisions(
        ("2002-12-25 23:43",
         "2002-06-06 18:41")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SyslogFacility(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              12,
              13,
              14,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              99)
        )
    )
    namedValues = NamedValues(
        *(("auth", 4),
          ("authPriv", 10),
          ("console", 14),
          ("cron", 9),
          ("daemon", 3),
          ("ftp", 11),
          ("kernel", 0),
          ("local0", 16),
          ("local1", 17),
          ("local2", 18),
          ("local3", 19),
          ("local4", 20),
          ("local5", 21),
          ("local6", 22),
          ("local7", 23),
          ("lpr", 6),
          ("mail", 2),
          ("news", 7),
          ("noMap", 99),
          ("ntp", 12),
          ("security", 13),
          ("syslog", 5),
          ("user", 1),
          ("uucp", 8))
    )



class SyslogSeverity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              99)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("info", 6),
          ("notice", 5),
          ("other", 99),
          ("warning", 4))
    )



class SyslogSeverityCompOP(Integer32, TextualConvention):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("equal", 10),
          ("greaterThan", 4),
          ("greaterThanOrEqual", 2),
          ("lessThan", 5),
          ("lessThanOrEqual", 3),
          ("none", 1),
          ("notEqual", 11),
          ("notGreaterThan", 8),
          ("notGreaterThanOrEqual", 6),
          ("notLessThan", 9),
          ("notLessThanOrEqual", 7))
    )



class SyslogTransport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("tcp", 3),
          ("udp", 2))
    )



class SyslogService(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_SyslogSystem_ObjectIdentity = ObjectIdentity
syslogSystem = _SyslogSystem_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999999, 1)
)


class _SyslogDefaultTransport_Type(SyslogTransport):
    """Custom type syslogDefaultTransport based on SyslogTransport"""


_SyslogDefaultTransport_Object = MibScalar
syslogDefaultTransport = _SyslogDefaultTransport_Object(
    (1, 3, 6, 1, 2, 1, 999999, 1, 1),
    _SyslogDefaultTransport_Type()
)
syslogDefaultTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogDefaultTransport.setStatus("current")


class _SyslogDefaultService_Type(SyslogService):
    """Custom type syslogDefaultService based on SyslogService"""
    defaultValue = OctetString("514")


_SyslogDefaultService_Object = MibScalar
syslogDefaultService = _SyslogDefaultService_Object(
    (1, 3, 6, 1, 2, 1, 999999, 1, 2),
    _SyslogDefaultService_Type()
)
syslogDefaultService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogDefaultService.setStatus("current")
_SyslogDefaultFacility_Type = SyslogFacility
_SyslogDefaultFacility_Object = MibScalar
syslogDefaultFacility = _SyslogDefaultFacility_Object(
    (1, 3, 6, 1, 2, 1, 999999, 1, 3),
    _SyslogDefaultFacility_Type()
)
syslogDefaultFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogDefaultFacility.setStatus("current")
_SyslogDefaultSeverity_Type = SyslogSeverity
_SyslogDefaultSeverity_Object = MibScalar
syslogDefaultSeverity = _SyslogDefaultSeverity_Object(
    (1, 3, 6, 1, 2, 1, 999999, 1, 4),
    _SyslogDefaultSeverity_Type()
)
syslogDefaultSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogDefaultSeverity.setStatus("current")


class _SyslogMaxMessageSize_Type(Unsigned32):
    """Custom type syslogMaxMessageSize based on Unsigned32"""
    defaultValue = 1024


_SyslogMaxMessageSize_Object = MibScalar
syslogMaxMessageSize = _SyslogMaxMessageSize_Object(
    (1, 3, 6, 1, 2, 1, 999999, 1, 5),
    _SyslogMaxMessageSize_Type()
)
syslogMaxMessageSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogMaxMessageSize.setStatus("current")
_SyslogProc_ObjectIdentity = ObjectIdentity
syslogProc = _SyslogProc_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999999, 2)
)
_SyslogProcTable_Object = MibTable
syslogProcTable = _SyslogProcTable_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 1)
)
if mibBuilder.loadTexts:
    syslogProcTable.setStatus("current")
_SyslogProcEntry_Object = MibTableRow
syslogProcEntry = _SyslogProcEntry_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 1, 1)
)
syslogProcEntry.setIndexNames(
    (0, "DRAFT-IETF-SYSLOG-MIB", "syslogProcIndex"),
)
if mibBuilder.loadTexts:
    syslogProcEntry.setStatus("current")


class _SyslogProcIndex_Type(Integer32):
    """Custom type syslogProcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SyslogProcIndex_Type.__name__ = "Integer32"
_SyslogProcIndex_Object = MibTableColumn
syslogProcIndex = _SyslogProcIndex_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 1, 1, 1),
    _SyslogProcIndex_Type()
)
syslogProcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    syslogProcIndex.setStatus("current")
_SyslogProcMsgsReceived_Type = Counter32
_SyslogProcMsgsReceived_Object = MibTableColumn
syslogProcMsgsReceived = _SyslogProcMsgsReceived_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 1, 1, 2),
    _SyslogProcMsgsReceived_Type()
)
syslogProcMsgsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogProcMsgsReceived.setStatus("current")
_SyslogProcMsgsRelayed_Type = Counter32
_SyslogProcMsgsRelayed_Object = MibTableColumn
syslogProcMsgsRelayed = _SyslogProcMsgsRelayed_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 1, 1, 3),
    _SyslogProcMsgsRelayed_Type()
)
syslogProcMsgsRelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogProcMsgsRelayed.setStatus("current")
_SyslogProcMsgsDropped_Type = Counter32
_SyslogProcMsgsDropped_Object = MibTableColumn
syslogProcMsgsDropped = _SyslogProcMsgsDropped_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 1, 1, 4),
    _SyslogProcMsgsDropped_Type()
)
syslogProcMsgsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogProcMsgsDropped.setStatus("current")
_SyslogProcMsgsIgnored_Type = Counter32
_SyslogProcMsgsIgnored_Object = MibTableColumn
syslogProcMsgsIgnored = _SyslogProcMsgsIgnored_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 1, 1, 5),
    _SyslogProcMsgsIgnored_Type()
)
syslogProcMsgsIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogProcMsgsIgnored.setStatus("current")
_SyslogProcMsgsRejected_Type = Counter32
_SyslogProcMsgsRejected_Object = MibTableColumn
syslogProcMsgsRejected = _SyslogProcMsgsRejected_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 1, 1, 6),
    _SyslogProcMsgsRejected_Type()
)
syslogProcMsgsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogProcMsgsRejected.setStatus("current")
_SyslogProcLastMsgRecdTime_Type = TimeStamp
_SyslogProcLastMsgRecdTime_Object = MibTableColumn
syslogProcLastMsgRecdTime = _SyslogProcLastMsgRecdTime_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 1, 1, 7),
    _SyslogProcLastMsgRecdTime_Type()
)
syslogProcLastMsgRecdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogProcLastMsgRecdTime.setStatus("current")
_SyslogProcLastMsgDeliveredTime_Type = TimeStamp
_SyslogProcLastMsgDeliveredTime_Object = MibTableColumn
syslogProcLastMsgDeliveredTime = _SyslogProcLastMsgDeliveredTime_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 1, 1, 8),
    _SyslogProcLastMsgDeliveredTime_Type()
)
syslogProcLastMsgDeliveredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogProcLastMsgDeliveredTime.setStatus("current")
_SyslogParamsTable_Object = MibTable
syslogParamsTable = _SyslogParamsTable_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 2)
)
if mibBuilder.loadTexts:
    syslogParamsTable.setStatus("current")
_SyslogParamsEntry_Object = MibTableRow
syslogParamsEntry = _SyslogParamsEntry_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 2, 1)
)
syslogParamsEntry.setIndexNames(
    (0, "DRAFT-IETF-SYSLOG-MIB", "syslogProcIndex"),
)
if mibBuilder.loadTexts:
    syslogParamsEntry.setStatus("current")
_SyslogParamsProcDescr_Type = SnmpAdminString
_SyslogParamsProcDescr_Object = MibTableColumn
syslogParamsProcDescr = _SyslogParamsProcDescr_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 2, 1, 1),
    _SyslogParamsProcDescr_Type()
)
syslogParamsProcDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogParamsProcDescr.setStatus("current")
_SyslogParamsBindAddrType_Type = InetAddressType
_SyslogParamsBindAddrType_Object = MibTableColumn
syslogParamsBindAddrType = _SyslogParamsBindAddrType_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 2, 1, 2),
    _SyslogParamsBindAddrType_Type()
)
syslogParamsBindAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogParamsBindAddrType.setStatus("current")
_SyslogParamsBindAddr_Type = InetAddress
_SyslogParamsBindAddr_Object = MibTableColumn
syslogParamsBindAddr = _SyslogParamsBindAddr_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 2, 1, 3),
    _SyslogParamsBindAddr_Type()
)
syslogParamsBindAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogParamsBindAddr.setStatus("current")


class _SyslogParamsSendToAllAddresses_Type(Integer32):
    """Custom type syslogParamsSendToAllAddresses based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SyslogParamsSendToAllAddresses_Type.__name__ = "Integer32"
_SyslogParamsSendToAllAddresses_Object = MibTableColumn
syslogParamsSendToAllAddresses = _SyslogParamsSendToAllAddresses_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 2, 1, 4),
    _SyslogParamsSendToAllAddresses_Type()
)
syslogParamsSendToAllAddresses.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogParamsSendToAllAddresses.setStatus("current")


class _SyslogParamsCompression_Type(Integer32):
    """Custom type syslogParamsCompression based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("offIfPipe", 2),
          ("on", 3))
    )


_SyslogParamsCompression_Type.__name__ = "Integer32"
_SyslogParamsCompression_Object = MibTableColumn
syslogParamsCompression = _SyslogParamsCompression_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 2, 1, 5),
    _SyslogParamsCompression_Type()
)
syslogParamsCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogParamsCompression.setStatus("current")


class _SyslogParamsConfFileName_Type(SnmpAdminString):
    """Custom type syslogParamsConfFileName based on SnmpAdminString"""
    defaultValue = OctetString("/etc/syslog.conf")


_SyslogParamsConfFileName_Object = MibTableColumn
syslogParamsConfFileName = _SyslogParamsConfFileName_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 2, 1, 6),
    _SyslogParamsConfFileName_Type()
)
syslogParamsConfFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogParamsConfFileName.setStatus("current")


class _SyslogParamsFacilityTranslation_Type(Integer32):
    """Custom type syslogParamsFacilityTranslation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SyslogParamsFacilityTranslation_Type.__name__ = "Integer32"
_SyslogParamsFacilityTranslation_Object = MibTableColumn
syslogParamsFacilityTranslation = _SyslogParamsFacilityTranslation_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 2, 1, 7),
    _SyslogParamsFacilityTranslation_Type()
)
syslogParamsFacilityTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogParamsFacilityTranslation.setStatus("current")


class _SyslogParamsPIDFileName_Type(SnmpAdminString):
    """Custom type syslogParamsPIDFileName based on SnmpAdminString"""
    defaultValue = OctetString("/etc/syslog.conf")


_SyslogParamsPIDFileName_Object = MibTableColumn
syslogParamsPIDFileName = _SyslogParamsPIDFileName_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 2, 1, 8),
    _SyslogParamsPIDFileName_Type()
)
syslogParamsPIDFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogParamsPIDFileName.setStatus("current")


class _SyslogParamsDNSLookup_Type(Integer32):
    """Custom type syslogParamsDNSLookup based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNotUseLocalCache", 2),
          ("useLocalCache", 1))
    )


_SyslogParamsDNSLookup_Type.__name__ = "Integer32"
_SyslogParamsDNSLookup_Object = MibTableColumn
syslogParamsDNSLookup = _SyslogParamsDNSLookup_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 2, 1, 9),
    _SyslogParamsDNSLookup_Type()
)
syslogParamsDNSLookup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogParamsDNSLookup.setStatus("current")


class _SyslogParamsSeverityCompOP_Type(SyslogSeverityCompOP):
    """Custom type syslogParamsSeverityCompOP based on SyslogSeverityCompOP"""


_SyslogParamsSeverityCompOP_Object = MibTableColumn
syslogParamsSeverityCompOP = _SyslogParamsSeverityCompOP_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 2, 1, 10),
    _SyslogParamsSeverityCompOP_Type()
)
syslogParamsSeverityCompOP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogParamsSeverityCompOP.setStatus("current")


class _SyslogParamsSecuritySpecs_Type(Integer32):
    """Custom type syslogParamsSecuritySpecs based on Integer32"""
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
        *(("doNotOpenNetworkSockets", 2),
          ("doNotRecvFromRemoteHosts", 1),
          ("none", 0))
    )


_SyslogParamsSecuritySpecs_Type.__name__ = "Integer32"
_SyslogParamsSecuritySpecs_Object = MibTableColumn
syslogParamsSecuritySpecs = _SyslogParamsSecuritySpecs_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 2, 1, 11),
    _SyslogParamsSecuritySpecs_Type()
)
syslogParamsSecuritySpecs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogParamsSecuritySpecs.setStatus("current")


class _SyslogParamsProcessStatus_Type(Integer32):
    """Custom type syslogParamsProcessStatus based on Integer32"""
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
        *(("started", 1),
          ("stopped", 2),
          ("unknown", 0))
    )


_SyslogParamsProcessStatus_Type.__name__ = "Integer32"
_SyslogParamsProcessStatus_Object = MibTableColumn
syslogParamsProcessStatus = _SyslogParamsProcessStatus_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 2, 1, 12),
    _SyslogParamsProcessStatus_Type()
)
syslogParamsProcessStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogParamsProcessStatus.setStatus("current")
_SyslogParamsRowStatus_Type = RowStatus
_SyslogParamsRowStatus_Object = MibTableColumn
syslogParamsRowStatus = _SyslogParamsRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 2, 1, 13),
    _SyslogParamsRowStatus_Type()
)
syslogParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogParamsRowStatus.setStatus("current")
_SyslogAllowedHostsTable_Object = MibTable
syslogAllowedHostsTable = _SyslogAllowedHostsTable_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 3)
)
if mibBuilder.loadTexts:
    syslogAllowedHostsTable.setStatus("current")
_SyslogAllowedHostsEntry_Object = MibTableRow
syslogAllowedHostsEntry = _SyslogAllowedHostsEntry_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 3, 1)
)
syslogAllowedHostsEntry.setIndexNames(
    (0, "DRAFT-IETF-SYSLOG-MIB", "syslogProcIndex"),
)
if mibBuilder.loadTexts:
    syslogAllowedHostsEntry.setStatus("current")
_SyslogAllowedHostsAddressType_Type = InetAddressType
_SyslogAllowedHostsAddressType_Object = MibTableColumn
syslogAllowedHostsAddressType = _SyslogAllowedHostsAddressType_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 3, 1, 1),
    _SyslogAllowedHostsAddressType_Type()
)
syslogAllowedHostsAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogAllowedHostsAddressType.setStatus("current")
_SyslogAllowedHostsAddress_Type = InetAddress
_SyslogAllowedHostsAddress_Object = MibTableColumn
syslogAllowedHostsAddress = _SyslogAllowedHostsAddress_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 3, 1, 2),
    _SyslogAllowedHostsAddress_Type()
)
syslogAllowedHostsAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogAllowedHostsAddress.setStatus("current")
_SyslogAllowedHostsMaskLen_Type = Integer32
_SyslogAllowedHostsMaskLen_Object = MibTableColumn
syslogAllowedHostsMaskLen = _SyslogAllowedHostsMaskLen_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 3, 1, 3),
    _SyslogAllowedHostsMaskLen_Type()
)
syslogAllowedHostsMaskLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogAllowedHostsMaskLen.setStatus("current")


class _SyslogAllowedHostsTransport_Type(SyslogTransport):
    """Custom type syslogAllowedHostsTransport based on SyslogTransport"""


_SyslogAllowedHostsTransport_Object = MibTableColumn
syslogAllowedHostsTransport = _SyslogAllowedHostsTransport_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 3, 1, 4),
    _SyslogAllowedHostsTransport_Type()
)
syslogAllowedHostsTransport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogAllowedHostsTransport.setStatus("current")


class _SyslogAllowedHostsPort_Type(SyslogService):
    """Custom type syslogAllowedHostsPort based on SyslogService"""
    defaultValue = OctetString("any")


_SyslogAllowedHostsPort_Object = MibTableColumn
syslogAllowedHostsPort = _SyslogAllowedHostsPort_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 3, 1, 5),
    _SyslogAllowedHostsPort_Type()
)
syslogAllowedHostsPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogAllowedHostsPort.setStatus("current")
_SyslogAllowedHostsRowStatus_Type = RowStatus
_SyslogAllowedHostsRowStatus_Object = MibTableColumn
syslogAllowedHostsRowStatus = _SyslogAllowedHostsRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 999999, 2, 3, 1, 6),
    _SyslogAllowedHostsRowStatus_Type()
)
syslogAllowedHostsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogAllowedHostsRowStatus.setStatus("current")
_SyslogControl_ObjectIdentity = ObjectIdentity
syslogControl = _SyslogControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999999, 3)
)
_SyslogCtlSelectionTable_Object = MibTable
syslogCtlSelectionTable = _SyslogCtlSelectionTable_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 1)
)
if mibBuilder.loadTexts:
    syslogCtlSelectionTable.setStatus("current")
_SyslogCtlSelectionEntry_Object = MibTableRow
syslogCtlSelectionEntry = _SyslogCtlSelectionEntry_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 1, 1)
)
syslogCtlSelectionEntry.setIndexNames(
    (0, "DRAFT-IETF-SYSLOG-MIB", "syslogProcIndex"),
    (0, "DRAFT-IETF-SYSLOG-MIB", "syslogCtlActionIndex"),
    (0, "DRAFT-IETF-SYSLOG-MIB", "syslogCtlSelectionIndex"),
)
if mibBuilder.loadTexts:
    syslogCtlSelectionEntry.setStatus("current")


class _SyslogCtlActionIndex_Type(Integer32):
    """Custom type syslogCtlActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SyslogCtlActionIndex_Type.__name__ = "Integer32"
_SyslogCtlActionIndex_Object = MibTableColumn
syslogCtlActionIndex = _SyslogCtlActionIndex_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 1, 1, 1),
    _SyslogCtlActionIndex_Type()
)
syslogCtlActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    syslogCtlActionIndex.setStatus("current")


class _SyslogCtlSelectionIndex_Type(Integer32):
    """Custom type syslogCtlSelectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SyslogCtlSelectionIndex_Type.__name__ = "Integer32"
_SyslogCtlSelectionIndex_Object = MibTableColumn
syslogCtlSelectionIndex = _SyslogCtlSelectionIndex_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 1, 1, 2),
    _SyslogCtlSelectionIndex_Type()
)
syslogCtlSelectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    syslogCtlSelectionIndex.setStatus("current")
_SyslogCtlSelectionDescr_Type = SnmpAdminString
_SyslogCtlSelectionDescr_Object = MibTableColumn
syslogCtlSelectionDescr = _SyslogCtlSelectionDescr_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 1, 1, 3),
    _SyslogCtlSelectionDescr_Type()
)
syslogCtlSelectionDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogCtlSelectionDescr.setStatus("current")


class _SyslogCtlSelectionHostNameIncl_Type(Integer32):
    """Custom type syslogCtlSelectionHostNameIncl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("excluded", 2),
          ("included", 1))
    )


_SyslogCtlSelectionHostNameIncl_Type.__name__ = "Integer32"
_SyslogCtlSelectionHostNameIncl_Object = MibTableColumn
syslogCtlSelectionHostNameIncl = _SyslogCtlSelectionHostNameIncl_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 1, 1, 4),
    _SyslogCtlSelectionHostNameIncl_Type()
)
syslogCtlSelectionHostNameIncl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogCtlSelectionHostNameIncl.setStatus("current")


class _SyslogCtlSelectionHostname_Type(SnmpAdminString):
    """Custom type syslogCtlSelectionHostname based on SnmpAdminString"""
    defaultValue = OctetString("*")


_SyslogCtlSelectionHostname_Object = MibTableColumn
syslogCtlSelectionHostname = _SyslogCtlSelectionHostname_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 1, 1, 5),
    _SyslogCtlSelectionHostname_Type()
)
syslogCtlSelectionHostname.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogCtlSelectionHostname.setStatus("current")


class _SyslogCtlSelectionProgNameIncl_Type(Integer32):
    """Custom type syslogCtlSelectionProgNameIncl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("excluded", 2),
          ("included", 1))
    )


_SyslogCtlSelectionProgNameIncl_Type.__name__ = "Integer32"
_SyslogCtlSelectionProgNameIncl_Object = MibTableColumn
syslogCtlSelectionProgNameIncl = _SyslogCtlSelectionProgNameIncl_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 1, 1, 6),
    _SyslogCtlSelectionProgNameIncl_Type()
)
syslogCtlSelectionProgNameIncl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogCtlSelectionProgNameIncl.setStatus("current")


class _SyslogCtlSelectionProgName_Type(SnmpAdminString):
    """Custom type syslogCtlSelectionProgName based on SnmpAdminString"""
    defaultValue = OctetString("*")


_SyslogCtlSelectionProgName_Object = MibTableColumn
syslogCtlSelectionProgName = _SyslogCtlSelectionProgName_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 1, 1, 7),
    _SyslogCtlSelectionProgName_Type()
)
syslogCtlSelectionProgName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogCtlSelectionProgName.setStatus("current")


class _SyslogCtlSelectionPriorityIncl_Type(Integer32):
    """Custom type syslogCtlSelectionPriorityIncl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("excluded", 2),
          ("included", 1))
    )


_SyslogCtlSelectionPriorityIncl_Type.__name__ = "Integer32"
_SyslogCtlSelectionPriorityIncl_Object = MibTableColumn
syslogCtlSelectionPriorityIncl = _SyslogCtlSelectionPriorityIncl_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 1, 1, 8),
    _SyslogCtlSelectionPriorityIncl_Type()
)
syslogCtlSelectionPriorityIncl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogCtlSelectionPriorityIncl.setStatus("current")
_SyslogCtlSelectionFacility_Type = SyslogFacility
_SyslogCtlSelectionFacility_Object = MibTableColumn
syslogCtlSelectionFacility = _SyslogCtlSelectionFacility_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 1, 1, 9),
    _SyslogCtlSelectionFacility_Type()
)
syslogCtlSelectionFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogCtlSelectionFacility.setStatus("current")


class _SyslogCtlSelectionSeverityCompOP_Type(SyslogSeverityCompOP):
    """Custom type syslogCtlSelectionSeverityCompOP based on SyslogSeverityCompOP"""


_SyslogCtlSelectionSeverityCompOP_Object = MibTableColumn
syslogCtlSelectionSeverityCompOP = _SyslogCtlSelectionSeverityCompOP_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 1, 1, 10),
    _SyslogCtlSelectionSeverityCompOP_Type()
)
syslogCtlSelectionSeverityCompOP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogCtlSelectionSeverityCompOP.setStatus("current")
_SyslogCtlSelectionSeverity_Type = SyslogSeverity
_SyslogCtlSelectionSeverity_Object = MibTableColumn
syslogCtlSelectionSeverity = _SyslogCtlSelectionSeverity_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 1, 1, 11),
    _SyslogCtlSelectionSeverity_Type()
)
syslogCtlSelectionSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogCtlSelectionSeverity.setStatus("current")
_SyslogCtlSelectionRowStatus_Type = RowStatus
_SyslogCtlSelectionRowStatus_Object = MibTableColumn
syslogCtlSelectionRowStatus = _SyslogCtlSelectionRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 1, 1, 12),
    _SyslogCtlSelectionRowStatus_Type()
)
syslogCtlSelectionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogCtlSelectionRowStatus.setStatus("current")
_SyslogCtlLogActionTable_Object = MibTable
syslogCtlLogActionTable = _SyslogCtlLogActionTable_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 2)
)
if mibBuilder.loadTexts:
    syslogCtlLogActionTable.setStatus("current")
_SyslogCtlLogActionEntry_Object = MibTableRow
syslogCtlLogActionEntry = _SyslogCtlLogActionEntry_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 2, 1)
)
syslogCtlLogActionEntry.setIndexNames(
    (0, "DRAFT-IETF-SYSLOG-MIB", "syslogProcIndex"),
    (0, "DRAFT-IETF-SYSLOG-MIB", "syslogCtlActionIndex"),
)
if mibBuilder.loadTexts:
    syslogCtlLogActionEntry.setStatus("current")
_SyslogCtlLogActionFileName_Type = SnmpAdminString
_SyslogCtlLogActionFileName_Object = MibTableColumn
syslogCtlLogActionFileName = _SyslogCtlLogActionFileName_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 2, 1, 1),
    _SyslogCtlLogActionFileName_Type()
)
syslogCtlLogActionFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogCtlLogActionFileName.setStatus("current")
_SyslogCtlLogActionRowStatus_Type = RowStatus
_SyslogCtlLogActionRowStatus_Object = MibTableColumn
syslogCtlLogActionRowStatus = _SyslogCtlLogActionRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 2, 1, 2),
    _SyslogCtlLogActionRowStatus_Type()
)
syslogCtlLogActionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogCtlLogActionRowStatus.setStatus("current")
_SyslogCtlUserActionTable_Object = MibTable
syslogCtlUserActionTable = _SyslogCtlUserActionTable_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 3)
)
if mibBuilder.loadTexts:
    syslogCtlUserActionTable.setStatus("current")
_SyslogCtlUserActionEntry_Object = MibTableRow
syslogCtlUserActionEntry = _SyslogCtlUserActionEntry_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 3, 1)
)
syslogCtlUserActionEntry.setIndexNames(
    (0, "DRAFT-IETF-SYSLOG-MIB", "syslogProcIndex"),
    (0, "DRAFT-IETF-SYSLOG-MIB", "syslogCtlActionIndex"),
    (0, "DRAFT-IETF-SYSLOG-MIB", "syslogCtlUserActionIndex"),
)
if mibBuilder.loadTexts:
    syslogCtlUserActionEntry.setStatus("current")
_SyslogCtlUserActionIndex_Type = Unsigned32
_SyslogCtlUserActionIndex_Object = MibTableColumn
syslogCtlUserActionIndex = _SyslogCtlUserActionIndex_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 3, 1, 1),
    _SyslogCtlUserActionIndex_Type()
)
syslogCtlUserActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    syslogCtlUserActionIndex.setStatus("current")
_SyslogCtlUserActionUserID_Type = SnmpAdminString
_SyslogCtlUserActionUserID_Object = MibTableColumn
syslogCtlUserActionUserID = _SyslogCtlUserActionUserID_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 3, 1, 2),
    _SyslogCtlUserActionUserID_Type()
)
syslogCtlUserActionUserID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogCtlUserActionUserID.setStatus("current")
_SyslogCtlUserActionRowStatus_Type = RowStatus
_SyslogCtlUserActionRowStatus_Object = MibTableColumn
syslogCtlUserActionRowStatus = _SyslogCtlUserActionRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 3, 1, 3),
    _SyslogCtlUserActionRowStatus_Type()
)
syslogCtlUserActionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogCtlUserActionRowStatus.setStatus("current")
_SyslogCtlForwardActionTable_Object = MibTable
syslogCtlForwardActionTable = _SyslogCtlForwardActionTable_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 4)
)
if mibBuilder.loadTexts:
    syslogCtlForwardActionTable.setStatus("current")
_SyslogCtlForwardActionEntry_Object = MibTableRow
syslogCtlForwardActionEntry = _SyslogCtlForwardActionEntry_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 4, 1)
)
syslogCtlForwardActionEntry.setIndexNames(
    (0, "DRAFT-IETF-SYSLOG-MIB", "syslogProcIndex"),
    (0, "DRAFT-IETF-SYSLOG-MIB", "syslogCtlActionIndex"),
    (0, "DRAFT-IETF-SYSLOG-MIB", "syslogCtlForwardActionIndex"),
)
if mibBuilder.loadTexts:
    syslogCtlForwardActionEntry.setStatus("current")
_SyslogCtlForwardActionIndex_Type = Unsigned32
_SyslogCtlForwardActionIndex_Object = MibTableColumn
syslogCtlForwardActionIndex = _SyslogCtlForwardActionIndex_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 4, 1, 1),
    _SyslogCtlForwardActionIndex_Type()
)
syslogCtlForwardActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    syslogCtlForwardActionIndex.setStatus("current")


class _SyslogCtlForwardActionDescr_Type(SnmpAdminString):
    """Custom type syslogCtlForwardActionDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SyslogCtlForwardActionDescr_Type.__name__ = "SnmpAdminString"
_SyslogCtlForwardActionDescr_Object = MibTableColumn
syslogCtlForwardActionDescr = _SyslogCtlForwardActionDescr_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 4, 1, 2),
    _SyslogCtlForwardActionDescr_Type()
)
syslogCtlForwardActionDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogCtlForwardActionDescr.setStatus("current")
_SyslogCtlForwardActionAddrType_Type = InetAddressType
_SyslogCtlForwardActionAddrType_Object = MibTableColumn
syslogCtlForwardActionAddrType = _SyslogCtlForwardActionAddrType_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 4, 1, 3),
    _SyslogCtlForwardActionAddrType_Type()
)
syslogCtlForwardActionAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogCtlForwardActionAddrType.setStatus("current")
_SyslogCtlForwardActionAddr_Type = InetAddress
_SyslogCtlForwardActionAddr_Object = MibTableColumn
syslogCtlForwardActionAddr = _SyslogCtlForwardActionAddr_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 4, 1, 4),
    _SyslogCtlForwardActionAddr_Type()
)
syslogCtlForwardActionAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogCtlForwardActionAddr.setStatus("current")


class _SyslogCtlForwardActionTransport_Type(SyslogTransport):
    """Custom type syslogCtlForwardActionTransport based on SyslogTransport"""


_SyslogCtlForwardActionTransport_Object = MibTableColumn
syslogCtlForwardActionTransport = _SyslogCtlForwardActionTransport_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 4, 1, 5),
    _SyslogCtlForwardActionTransport_Type()
)
syslogCtlForwardActionTransport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogCtlForwardActionTransport.setStatus("current")


class _SyslogCtlForwardActionPort_Type(SyslogService):
    """Custom type syslogCtlForwardActionPort based on SyslogService"""
    defaultValue = OctetString("514")


_SyslogCtlForwardActionPort_Object = MibTableColumn
syslogCtlForwardActionPort = _SyslogCtlForwardActionPort_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 4, 1, 6),
    _SyslogCtlForwardActionPort_Type()
)
syslogCtlForwardActionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogCtlForwardActionPort.setStatus("current")
_SyslogCtlForwardActionFacility_Type = SyslogFacility
_SyslogCtlForwardActionFacility_Object = MibTableColumn
syslogCtlForwardActionFacility = _SyslogCtlForwardActionFacility_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 4, 1, 7),
    _SyslogCtlForwardActionFacility_Type()
)
syslogCtlForwardActionFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogCtlForwardActionFacility.setStatus("current")
_SyslogCtlForwardActionSeverity_Type = SyslogSeverity
_SyslogCtlForwardActionSeverity_Object = MibTableColumn
syslogCtlForwardActionSeverity = _SyslogCtlForwardActionSeverity_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 4, 1, 8),
    _SyslogCtlForwardActionSeverity_Type()
)
syslogCtlForwardActionSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogCtlForwardActionSeverity.setStatus("current")
_SyslogCtlForwardActionRowStatus_Type = RowStatus
_SyslogCtlForwardActionRowStatus_Object = MibTableColumn
syslogCtlForwardActionRowStatus = _SyslogCtlForwardActionRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 4, 1, 9),
    _SyslogCtlForwardActionRowStatus_Type()
)
syslogCtlForwardActionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogCtlForwardActionRowStatus.setStatus("current")
_SyslogCtlPipeActionTable_Object = MibTable
syslogCtlPipeActionTable = _SyslogCtlPipeActionTable_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 5)
)
if mibBuilder.loadTexts:
    syslogCtlPipeActionTable.setStatus("current")
_SyslogCtlPipeActionEntry_Object = MibTableRow
syslogCtlPipeActionEntry = _SyslogCtlPipeActionEntry_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 5, 1)
)
syslogCtlPipeActionEntry.setIndexNames(
    (0, "DRAFT-IETF-SYSLOG-MIB", "syslogProcIndex"),
    (0, "DRAFT-IETF-SYSLOG-MIB", "syslogCtlActionIndex"),
)
if mibBuilder.loadTexts:
    syslogCtlPipeActionEntry.setStatus("current")
_SyslogCtlPipeActionCmd_Type = SnmpAdminString
_SyslogCtlPipeActionCmd_Object = MibTableColumn
syslogCtlPipeActionCmd = _SyslogCtlPipeActionCmd_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 5, 1, 1),
    _SyslogCtlPipeActionCmd_Type()
)
syslogCtlPipeActionCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogCtlPipeActionCmd.setStatus("current")
_SyslogCtlPipeActionRowStatus_Type = RowStatus
_SyslogCtlPipeActionRowStatus_Object = MibTableColumn
syslogCtlPipeActionRowStatus = _SyslogCtlPipeActionRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 999999, 3, 5, 1, 2),
    _SyslogCtlPipeActionRowStatus_Type()
)
syslogCtlPipeActionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogCtlPipeActionRowStatus.setStatus("current")
_SyslogConformance_ObjectIdentity = ObjectIdentity
syslogConformance = _SyslogConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999999, 4)
)
_SyslogGroups_ObjectIdentity = ObjectIdentity
syslogGroups = _SyslogGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999999, 4, 1)
)
_SyslogCompliances_ObjectIdentity = ObjectIdentity
syslogCompliances = _SyslogCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999999, 4, 2)
)

# Managed Objects groups

syslogSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999999, 4, 1, 1)
)
syslogSystemGroup.setObjects(
      *(("DRAFT-IETF-SYSLOG-MIB", "syslogDefaultTransport"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogDefaultService"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogDefaultFacility"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogDefaultSeverity"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogMaxMessageSize"))
)
if mibBuilder.loadTexts:
    syslogSystemGroup.setStatus("current")

syslogStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999999, 4, 1, 2)
)
syslogStatsGroup.setObjects(
      *(("DRAFT-IETF-SYSLOG-MIB", "syslogProcMsgsReceived"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogProcMsgsRelayed"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogProcMsgsDropped"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogProcMsgsIgnored"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogProcMsgsRejected"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogProcLastMsgRecdTime"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogProcLastMsgDeliveredTime"))
)
if mibBuilder.loadTexts:
    syslogStatsGroup.setStatus("current")

syslogParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999999, 4, 1, 3)
)
syslogParamsGroup.setObjects(
      *(("DRAFT-IETF-SYSLOG-MIB", "syslogParamsProcDescr"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogParamsBindAddrType"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogParamsBindAddr"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogParamsSendToAllAddresses"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogParamsCompression"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogParamsConfFileName"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogParamsFacilityTranslation"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogParamsPIDFileName"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogParamsDNSLookup"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogParamsSeverityCompOP"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogParamsSecuritySpecs"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogParamsProcessStatus"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogParamsRowStatus"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogAllowedHostsAddressType"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogAllowedHostsAddress"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogAllowedHostsMaskLen"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogAllowedHostsTransport"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogAllowedHostsPort"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogAllowedHostsRowStatus"))
)
if mibBuilder.loadTexts:
    syslogParamsGroup.setStatus("current")

syslogControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999999, 4, 1, 4)
)
syslogControlGroup.setObjects(
      *(("DRAFT-IETF-SYSLOG-MIB", "syslogCtlSelectionDescr"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogCtlSelectionHostNameIncl"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogCtlSelectionHostname"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogCtlSelectionProgNameIncl"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogCtlSelectionProgName"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogCtlSelectionPriorityIncl"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogCtlSelectionFacility"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogCtlSelectionSeverity"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogCtlSelectionSeverityCompOP"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogCtlSelectionRowStatus"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogCtlLogActionFileName"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogCtlLogActionRowStatus"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogCtlUserActionUserID"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogCtlUserActionRowStatus"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogCtlForwardActionDescr"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogCtlForwardActionAddrType"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogCtlForwardActionAddr"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogCtlForwardActionTransport"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogCtlForwardActionPort"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogCtlForwardActionFacility"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogCtlForwardActionSeverity"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogCtlForwardActionRowStatus"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogCtlPipeActionCmd"),
        ("DRAFT-IETF-SYSLOG-MIB", "syslogCtlPipeActionRowStatus"))
)
if mibBuilder.loadTexts:
    syslogControlGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

syslogCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 999999, 4, 2, 1)
)
if mibBuilder.loadTexts:
    syslogCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DRAFT-IETF-SYSLOG-MIB",
    **{"SyslogFacility": SyslogFacility,
       "SyslogSeverity": SyslogSeverity,
       "SyslogSeverityCompOP": SyslogSeverityCompOP,
       "SyslogTransport": SyslogTransport,
       "SyslogService": SyslogService,
       "syslogMIB": syslogMIB,
       "syslogSystem": syslogSystem,
       "syslogDefaultTransport": syslogDefaultTransport,
       "syslogDefaultService": syslogDefaultService,
       "syslogDefaultFacility": syslogDefaultFacility,
       "syslogDefaultSeverity": syslogDefaultSeverity,
       "syslogMaxMessageSize": syslogMaxMessageSize,
       "syslogProc": syslogProc,
       "syslogProcTable": syslogProcTable,
       "syslogProcEntry": syslogProcEntry,
       "syslogProcIndex": syslogProcIndex,
       "syslogProcMsgsReceived": syslogProcMsgsReceived,
       "syslogProcMsgsRelayed": syslogProcMsgsRelayed,
       "syslogProcMsgsDropped": syslogProcMsgsDropped,
       "syslogProcMsgsIgnored": syslogProcMsgsIgnored,
       "syslogProcMsgsRejected": syslogProcMsgsRejected,
       "syslogProcLastMsgRecdTime": syslogProcLastMsgRecdTime,
       "syslogProcLastMsgDeliveredTime": syslogProcLastMsgDeliveredTime,
       "syslogParamsTable": syslogParamsTable,
       "syslogParamsEntry": syslogParamsEntry,
       "syslogParamsProcDescr": syslogParamsProcDescr,
       "syslogParamsBindAddrType": syslogParamsBindAddrType,
       "syslogParamsBindAddr": syslogParamsBindAddr,
       "syslogParamsSendToAllAddresses": syslogParamsSendToAllAddresses,
       "syslogParamsCompression": syslogParamsCompression,
       "syslogParamsConfFileName": syslogParamsConfFileName,
       "syslogParamsFacilityTranslation": syslogParamsFacilityTranslation,
       "syslogParamsPIDFileName": syslogParamsPIDFileName,
       "syslogParamsDNSLookup": syslogParamsDNSLookup,
       "syslogParamsSeverityCompOP": syslogParamsSeverityCompOP,
       "syslogParamsSecuritySpecs": syslogParamsSecuritySpecs,
       "syslogParamsProcessStatus": syslogParamsProcessStatus,
       "syslogParamsRowStatus": syslogParamsRowStatus,
       "syslogAllowedHostsTable": syslogAllowedHostsTable,
       "syslogAllowedHostsEntry": syslogAllowedHostsEntry,
       "syslogAllowedHostsAddressType": syslogAllowedHostsAddressType,
       "syslogAllowedHostsAddress": syslogAllowedHostsAddress,
       "syslogAllowedHostsMaskLen": syslogAllowedHostsMaskLen,
       "syslogAllowedHostsTransport": syslogAllowedHostsTransport,
       "syslogAllowedHostsPort": syslogAllowedHostsPort,
       "syslogAllowedHostsRowStatus": syslogAllowedHostsRowStatus,
       "syslogControl": syslogControl,
       "syslogCtlSelectionTable": syslogCtlSelectionTable,
       "syslogCtlSelectionEntry": syslogCtlSelectionEntry,
       "syslogCtlActionIndex": syslogCtlActionIndex,
       "syslogCtlSelectionIndex": syslogCtlSelectionIndex,
       "syslogCtlSelectionDescr": syslogCtlSelectionDescr,
       "syslogCtlSelectionHostNameIncl": syslogCtlSelectionHostNameIncl,
       "syslogCtlSelectionHostname": syslogCtlSelectionHostname,
       "syslogCtlSelectionProgNameIncl": syslogCtlSelectionProgNameIncl,
       "syslogCtlSelectionProgName": syslogCtlSelectionProgName,
       "syslogCtlSelectionPriorityIncl": syslogCtlSelectionPriorityIncl,
       "syslogCtlSelectionFacility": syslogCtlSelectionFacility,
       "syslogCtlSelectionSeverityCompOP": syslogCtlSelectionSeverityCompOP,
       "syslogCtlSelectionSeverity": syslogCtlSelectionSeverity,
       "syslogCtlSelectionRowStatus": syslogCtlSelectionRowStatus,
       "syslogCtlLogActionTable": syslogCtlLogActionTable,
       "syslogCtlLogActionEntry": syslogCtlLogActionEntry,
       "syslogCtlLogActionFileName": syslogCtlLogActionFileName,
       "syslogCtlLogActionRowStatus": syslogCtlLogActionRowStatus,
       "syslogCtlUserActionTable": syslogCtlUserActionTable,
       "syslogCtlUserActionEntry": syslogCtlUserActionEntry,
       "syslogCtlUserActionIndex": syslogCtlUserActionIndex,
       "syslogCtlUserActionUserID": syslogCtlUserActionUserID,
       "syslogCtlUserActionRowStatus": syslogCtlUserActionRowStatus,
       "syslogCtlForwardActionTable": syslogCtlForwardActionTable,
       "syslogCtlForwardActionEntry": syslogCtlForwardActionEntry,
       "syslogCtlForwardActionIndex": syslogCtlForwardActionIndex,
       "syslogCtlForwardActionDescr": syslogCtlForwardActionDescr,
       "syslogCtlForwardActionAddrType": syslogCtlForwardActionAddrType,
       "syslogCtlForwardActionAddr": syslogCtlForwardActionAddr,
       "syslogCtlForwardActionTransport": syslogCtlForwardActionTransport,
       "syslogCtlForwardActionPort": syslogCtlForwardActionPort,
       "syslogCtlForwardActionFacility": syslogCtlForwardActionFacility,
       "syslogCtlForwardActionSeverity": syslogCtlForwardActionSeverity,
       "syslogCtlForwardActionRowStatus": syslogCtlForwardActionRowStatus,
       "syslogCtlPipeActionTable": syslogCtlPipeActionTable,
       "syslogCtlPipeActionEntry": syslogCtlPipeActionEntry,
       "syslogCtlPipeActionCmd": syslogCtlPipeActionCmd,
       "syslogCtlPipeActionRowStatus": syslogCtlPipeActionRowStatus,
       "syslogConformance": syslogConformance,
       "syslogGroups": syslogGroups,
       "syslogSystemGroup": syslogSystemGroup,
       "syslogStatsGroup": syslogStatsGroup,
       "syslogParamsGroup": syslogParamsGroup,
       "syslogControlGroup": syslogControlGroup,
       "syslogCompliances": syslogCompliances,
       "syslogCompliance": syslogCompliance}
)
