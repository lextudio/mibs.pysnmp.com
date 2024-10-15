# SNMP MIB module (CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:51 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoL4L7moduleResourceLimitMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 480)
)
ciscoL4L7moduleResourceLimitMIB.setRevisions(
        ("2013-02-20 00:00",
         "2012-09-20 00:00",
         "2011-06-10 00:00",
         "2011-04-15 00:00",
         "2010-12-06 00:00",
         "2008-03-07 00:00",
         "2008-02-07 00:00",
         "2006-06-19 00:00",
         "2005-08-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoResourceClass(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class CiscoResourceLimitType(Integer32, TextualConvention):
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("aclMemory", 10),
          ("all", 1),
          ("asdmSessions", 17),
          ("concurrentConns", 3),
          ("cpu", 20),
          ("hosts", 15),
          ("ipReassemBuffer", 12),
          ("ipsecSessions", 16),
          ("macAddresses", 2),
          ("memory", 21),
          ("mgmtConnections", 4),
          ("natTranslations", 8),
          ("probes", 6),
          ("proxyConns", 5),
          ("regexState", 9),
          ("sshSessions", 18),
          ("sslConnections", 14),
          ("stickyEntries", 7),
          ("syslogBuffer", 11),
          ("tcpOOOBuffer", 13),
          ("telnetSessions", 19))
    )



class CiscoRateLimitResourceType(Integer32, TextualConvention):
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
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("appInspections", 6),
          ("arpRequestsXmt", 2),
          ("arpResponses", 3),
          ("bandwidth", 4),
          ("connections", 5),
          ("httpCompression", 13),
          ("mgmtBandwidth", 10),
          ("missedMac", 12),
          ("sslBandwidth", 8),
          ("sslConnections", 9),
          ("syslog", 7),
          ("throughput", 11))
    )



class CiscoResourceType(Integer32, TextualConvention):
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30)
        )
    )
    namedValues = NamedValues(
        *(("lAclMemory", 9),
          ("lAsdmSessions", 16),
          ("lConcurrentConns", 2),
          ("lHosts", 14),
          ("lIpReassemBuffer", 10),
          ("lIpsecSessions", 15),
          ("lMacAddresses", 1),
          ("lMgmtConnections", 3),
          ("lNatTranslations", 7),
          ("lProbes", 5),
          ("lProxyConns", 4),
          ("lRegexState", 8),
          ("lSshSessions", 17),
          ("lSslConnections", 13),
          ("lStickyEntries", 6),
          ("lSyslogBuffer", 11),
          ("lTcpOOOBuffer", 12),
          ("lTelnetSessions", 18),
          ("rlAppInspections", 23),
          ("rlArpRequestsXmt", 19),
          ("rlArpResponses", 20),
          ("rlBandwidth", 21),
          ("rlConnections", 22),
          ("rlHttpCompression", 30),
          ("rlMgmtBandwidth", 27),
          ("rlMissedMac", 29),
          ("rlSslBandwidth", 25),
          ("rlSslConnections", 26),
          ("rlSyslog", 24),
          ("rlThroughput", 28))
    )



class CiscoBufferUtilPercentage(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoL4L7ResourceLimitNotifs_ObjectIdentity = ObjectIdentity
ciscoL4L7ResourceLimitNotifs = _CiscoL4L7ResourceLimitNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 0)
)
_CiscoL4L7ResourceLimitMIBObjects_ObjectIdentity = ObjectIdentity
ciscoL4L7ResourceLimitMIBObjects = _CiscoL4L7ResourceLimitMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1)
)
_CrlResource_ObjectIdentity = ObjectIdentity
crlResource = _CrlResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1)
)
_CiscoL4L7ResourceClassTable_Object = MibTable
ciscoL4L7ResourceClassTable = _CiscoL4L7ResourceClassTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceClassTable.setStatus("current")
_CiscoL4L7ResourceClassEntry_Object = MibTableRow
ciscoL4L7ResourceClassEntry = _CiscoL4L7ResourceClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 1, 1)
)
ciscoL4L7ResourceClassEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceClassName"),
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceClassEntry.setStatus("current")
_CrlResourceClassName_Type = CiscoResourceClass
_CrlResourceClassName_Object = MibTableColumn
crlResourceClassName = _CrlResourceClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 1, 1, 1),
    _CrlResourceClassName_Type()
)
crlResourceClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crlResourceClassName.setStatus("current")


class _CrlResourceClassStorageType_Type(StorageType):
    """Custom type crlResourceClassStorageType based on StorageType"""


_CrlResourceClassStorageType_Object = MibTableColumn
crlResourceClassStorageType = _CrlResourceClassStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 1, 1, 2),
    _CrlResourceClassStorageType_Type()
)
crlResourceClassStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crlResourceClassStorageType.setStatus("current")
_CrlResourceClassRowStatus_Type = RowStatus
_CrlResourceClassRowStatus_Object = MibTableColumn
crlResourceClassRowStatus = _CrlResourceClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 1, 1, 3),
    _CrlResourceClassRowStatus_Type()
)
crlResourceClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crlResourceClassRowStatus.setStatus("current")
_CiscoL4L7ResourceLimitTable_Object = MibTable
ciscoL4L7ResourceLimitTable = _CiscoL4L7ResourceLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceLimitTable.setStatus("current")
_CiscoL4L7ResourceLimitEntry_Object = MibTableRow
ciscoL4L7ResourceLimitEntry = _CiscoL4L7ResourceLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 2, 1)
)
ciscoL4L7ResourceLimitEntry.setIndexNames(
    (0, "CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceClassName"),
    (0, "CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitType"),
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceLimitEntry.setStatus("current")
_CrlResourceLimitType_Type = CiscoResourceLimitType
_CrlResourceLimitType_Object = MibTableColumn
crlResourceLimitType = _CrlResourceLimitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 2, 1, 2),
    _CrlResourceLimitType_Type()
)
crlResourceLimitType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crlResourceLimitType.setStatus("current")


class _CrlResourceLimitValueType_Type(Integer32):
    """Custom type crlResourceLimitValueType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("percentage", 2))
    )


_CrlResourceLimitValueType_Type.__name__ = "Integer32"
_CrlResourceLimitValueType_Object = MibTableColumn
crlResourceLimitValueType = _CrlResourceLimitValueType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 2, 1, 3),
    _CrlResourceLimitValueType_Type()
)
crlResourceLimitValueType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crlResourceLimitValueType.setStatus("current")


class _CrlResourceLimitMin_Type(Unsigned32):
    """Custom type crlResourceLimitMin based on Unsigned32"""
    defaultValue = 0


_CrlResourceLimitMin_Object = MibTableColumn
crlResourceLimitMin = _CrlResourceLimitMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 2, 1, 4),
    _CrlResourceLimitMin_Type()
)
crlResourceLimitMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crlResourceLimitMin.setStatus("current")


class _CrlResourceLimitMax_Type(Unsigned32):
    """Custom type crlResourceLimitMax based on Unsigned32"""
    defaultValue = 0


_CrlResourceLimitMax_Object = MibTableColumn
crlResourceLimitMax = _CrlResourceLimitMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 2, 1, 5),
    _CrlResourceLimitMax_Type()
)
crlResourceLimitMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crlResourceLimitMax.setStatus("current")


class _CrlResourceLimitStorageType_Type(StorageType):
    """Custom type crlResourceLimitStorageType based on StorageType"""


_CrlResourceLimitStorageType_Object = MibTableColumn
crlResourceLimitStorageType = _CrlResourceLimitStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 2, 1, 6),
    _CrlResourceLimitStorageType_Type()
)
crlResourceLimitStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crlResourceLimitStorageType.setStatus("current")
_CrlResourceLimitRowStatus_Type = RowStatus
_CrlResourceLimitRowStatus_Object = MibTableColumn
crlResourceLimitRowStatus = _CrlResourceLimitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 2, 1, 7),
    _CrlResourceLimitRowStatus_Type()
)
crlResourceLimitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crlResourceLimitRowStatus.setStatus("current")
_CrlResourceLimitCurrentUsage_Type = Gauge32
_CrlResourceLimitCurrentUsage_Object = MibTableColumn
crlResourceLimitCurrentUsage = _CrlResourceLimitCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 2, 1, 8),
    _CrlResourceLimitCurrentUsage_Type()
)
crlResourceLimitCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crlResourceLimitCurrentUsage.setStatus("current")
_CrlResourceLimitPeakUsage_Type = Gauge32
_CrlResourceLimitPeakUsage_Object = MibTableColumn
crlResourceLimitPeakUsage = _CrlResourceLimitPeakUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 2, 1, 9),
    _CrlResourceLimitPeakUsage_Type()
)
crlResourceLimitPeakUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crlResourceLimitPeakUsage.setStatus("current")
_CrlResourceLimitReqsDeniedCount_Type = Counter32
_CrlResourceLimitReqsDeniedCount_Object = MibTableColumn
crlResourceLimitReqsDeniedCount = _CrlResourceLimitReqsDeniedCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 2, 1, 10),
    _CrlResourceLimitReqsDeniedCount_Type()
)
crlResourceLimitReqsDeniedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crlResourceLimitReqsDeniedCount.setStatus("current")
_CiscoL4L7ResourceRateLimitTable_Object = MibTable
ciscoL4L7ResourceRateLimitTable = _CiscoL4L7ResourceRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceRateLimitTable.setStatus("current")
_CiscoL4L7ResourceRateLimitEntry_Object = MibTableRow
ciscoL4L7ResourceRateLimitEntry = _CiscoL4L7ResourceRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 4, 1)
)
ciscoL4L7ResourceRateLimitEntry.setIndexNames(
    (0, "CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceClassName"),
    (0, "CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceType"),
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceRateLimitEntry.setStatus("current")
_CrlRateLimitResourceType_Type = CiscoRateLimitResourceType
_CrlRateLimitResourceType_Object = MibTableColumn
crlRateLimitResourceType = _CrlRateLimitResourceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 4, 1, 1),
    _CrlRateLimitResourceType_Type()
)
crlRateLimitResourceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crlRateLimitResourceType.setStatus("current")


class _CrlRateLimitResourceMin_Type(Unsigned32):
    """Custom type crlRateLimitResourceMin based on Unsigned32"""
    defaultValue = 0


_CrlRateLimitResourceMin_Object = MibTableColumn
crlRateLimitResourceMin = _CrlRateLimitResourceMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 4, 1, 2),
    _CrlRateLimitResourceMin_Type()
)
crlRateLimitResourceMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crlRateLimitResourceMin.setStatus("current")


class _CrlRateLimitResourceMax_Type(Unsigned32):
    """Custom type crlRateLimitResourceMax based on Unsigned32"""
    defaultValue = 0


_CrlRateLimitResourceMax_Object = MibTableColumn
crlRateLimitResourceMax = _CrlRateLimitResourceMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 4, 1, 3),
    _CrlRateLimitResourceMax_Type()
)
crlRateLimitResourceMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crlRateLimitResourceMax.setStatus("current")


class _CrlRateLimitResourceStorageType_Type(StorageType):
    """Custom type crlRateLimitResourceStorageType based on StorageType"""


_CrlRateLimitResourceStorageType_Object = MibTableColumn
crlRateLimitResourceStorageType = _CrlRateLimitResourceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 4, 1, 4),
    _CrlRateLimitResourceStorageType_Type()
)
crlRateLimitResourceStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crlRateLimitResourceStorageType.setStatus("current")
_CrlRateLimitResourceRowStatus_Type = RowStatus
_CrlRateLimitResourceRowStatus_Object = MibTableColumn
crlRateLimitResourceRowStatus = _CrlRateLimitResourceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 4, 1, 5),
    _CrlRateLimitResourceRowStatus_Type()
)
crlRateLimitResourceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crlRateLimitResourceRowStatus.setStatus("current")
_CrlRateLimitResourceCurrentUsage_Type = Gauge32
_CrlRateLimitResourceCurrentUsage_Object = MibTableColumn
crlRateLimitResourceCurrentUsage = _CrlRateLimitResourceCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 4, 1, 6),
    _CrlRateLimitResourceCurrentUsage_Type()
)
crlRateLimitResourceCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crlRateLimitResourceCurrentUsage.setStatus("current")
_CrlRateLimitResourcePeakUsage_Type = Gauge32
_CrlRateLimitResourcePeakUsage_Object = MibTableColumn
crlRateLimitResourcePeakUsage = _CrlRateLimitResourcePeakUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 4, 1, 7),
    _CrlRateLimitResourcePeakUsage_Type()
)
crlRateLimitResourcePeakUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crlRateLimitResourcePeakUsage.setStatus("current")
_CrlRateLimitResourceReqsDeniedCount_Type = Counter32
_CrlRateLimitResourceReqsDeniedCount_Object = MibTableColumn
crlRateLimitResourceReqsDeniedCount = _CrlRateLimitResourceReqsDeniedCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 4, 1, 8),
    _CrlRateLimitResourceReqsDeniedCount_Type()
)
crlRateLimitResourceReqsDeniedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crlRateLimitResourceReqsDeniedCount.setStatus("current")
_CiscoL4L7ResourceUsageSummaryTable_Object = MibTable
ciscoL4L7ResourceUsageSummaryTable = _CiscoL4L7ResourceUsageSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceUsageSummaryTable.setStatus("current")
_CiscoL4L7ResourceUsageSummaryEntry_Object = MibTableRow
ciscoL4L7ResourceUsageSummaryEntry = _CiscoL4L7ResourceUsageSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 5, 1)
)
ciscoL4L7ResourceUsageSummaryEntry.setIndexNames(
    (0, "CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceSummaryType"),
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceUsageSummaryEntry.setStatus("current")
_CrlResourceSummaryType_Type = CiscoResourceType
_CrlResourceSummaryType_Object = MibTableColumn
crlResourceSummaryType = _CrlResourceSummaryType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 5, 1, 1),
    _CrlResourceSummaryType_Type()
)
crlResourceSummaryType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crlResourceSummaryType.setStatus("current")
_CrlResourceSummaryCurrentUsage_Type = Gauge32
_CrlResourceSummaryCurrentUsage_Object = MibTableColumn
crlResourceSummaryCurrentUsage = _CrlResourceSummaryCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 5, 1, 2),
    _CrlResourceSummaryCurrentUsage_Type()
)
crlResourceSummaryCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crlResourceSummaryCurrentUsage.setStatus("current")
_CrlResourceSummaryPeakUsage_Type = Gauge32
_CrlResourceSummaryPeakUsage_Object = MibTableColumn
crlResourceSummaryPeakUsage = _CrlResourceSummaryPeakUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 5, 1, 3),
    _CrlResourceSummaryPeakUsage_Type()
)
crlResourceSummaryPeakUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crlResourceSummaryPeakUsage.setStatus("current")
_CrlResourceSummaryReqsDeniedCount_Type = Counter64
_CrlResourceSummaryReqsDeniedCount_Object = MibTableColumn
crlResourceSummaryReqsDeniedCount = _CrlResourceSummaryReqsDeniedCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 5, 1, 4),
    _CrlResourceSummaryReqsDeniedCount_Type()
)
crlResourceSummaryReqsDeniedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crlResourceSummaryReqsDeniedCount.setStatus("current")
_CrlResourceSummaryLastClearedTime_Type = TimeStamp
_CrlResourceSummaryLastClearedTime_Object = MibTableColumn
crlResourceSummaryLastClearedTime = _CrlResourceSummaryLastClearedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 5, 1, 5),
    _CrlResourceSummaryLastClearedTime_Type()
)
crlResourceSummaryLastClearedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crlResourceSummaryLastClearedTime.setStatus("current")


class _CrlResourceSummaryStorageType_Type(StorageType):
    """Custom type crlResourceSummaryStorageType based on StorageType"""


_CrlResourceSummaryStorageType_Object = MibTableColumn
crlResourceSummaryStorageType = _CrlResourceSummaryStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 5, 1, 6),
    _CrlResourceSummaryStorageType_Type()
)
crlResourceSummaryStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crlResourceSummaryStorageType.setStatus("current")
_CrlResourceSummaryRowStatus_Type = RowStatus
_CrlResourceSummaryRowStatus_Object = MibTableColumn
crlResourceSummaryRowStatus = _CrlResourceSummaryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 5, 1, 7),
    _CrlResourceSummaryRowStatus_Type()
)
crlResourceSummaryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crlResourceSummaryRowStatus.setStatus("current")
_CiscoL4L7BufferUtilizationTable_Object = MibTable
ciscoL4L7BufferUtilizationTable = _CiscoL4L7BufferUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoL4L7BufferUtilizationTable.setStatus("current")
_CiscoL4L7BufferUtilizationEntry_Object = MibTableRow
ciscoL4L7BufferUtilizationEntry = _CiscoL4L7BufferUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 6, 1)
)
ciscoL4L7BufferUtilizationEntry.setIndexNames(
    (0, "CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "clrNetworkProcessor"),
)
if mibBuilder.loadTexts:
    ciscoL4L7BufferUtilizationEntry.setStatus("current")
_ClrNetworkProcessor_Type = Unsigned32
_ClrNetworkProcessor_Object = MibTableColumn
clrNetworkProcessor = _ClrNetworkProcessor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 6, 1, 1),
    _ClrNetworkProcessor_Type()
)
clrNetworkProcessor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clrNetworkProcessor.setStatus("current")
_CrlBufferUsageValue_Type = Gauge32
_CrlBufferUsageValue_Object = MibTableColumn
crlBufferUsageValue = _CrlBufferUsageValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 6, 1, 2),
    _CrlBufferUsageValue_Type()
)
crlBufferUsageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crlBufferUsageValue.setStatus("current")
if mibBuilder.loadTexts:
    crlBufferUsageValue.setUnits("buffers")
_CrlPercentageBufferUsage_Type = CiscoBufferUtilPercentage
_CrlPercentageBufferUsage_Object = MibTableColumn
crlPercentageBufferUsage = _CrlPercentageBufferUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 6, 1, 3),
    _CrlPercentageBufferUsage_Type()
)
crlPercentageBufferUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crlPercentageBufferUsage.setStatus("current")
if mibBuilder.loadTexts:
    crlPercentageBufferUsage.setUnits("percentage")
_CrlPercentageBufferUsageDisplay_Type = SnmpAdminString
_CrlPercentageBufferUsageDisplay_Object = MibTableColumn
crlPercentageBufferUsageDisplay = _CrlPercentageBufferUsageDisplay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 6, 1, 4),
    _CrlPercentageBufferUsageDisplay_Type()
)
crlPercentageBufferUsageDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crlPercentageBufferUsageDisplay.setStatus("current")
if mibBuilder.loadTexts:
    crlPercentageBufferUsageDisplay.setUnits("percentage")
_CrlExternalBufferUsageValue_Type = Gauge32
_CrlExternalBufferUsageValue_Object = MibTableColumn
crlExternalBufferUsageValue = _CrlExternalBufferUsageValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 6, 1, 5),
    _CrlExternalBufferUsageValue_Type()
)
crlExternalBufferUsageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crlExternalBufferUsageValue.setStatus("current")
if mibBuilder.loadTexts:
    crlExternalBufferUsageValue.setUnits("buffers")
_CrlExternalPercentageBufferUsage_Type = CiscoBufferUtilPercentage
_CrlExternalPercentageBufferUsage_Object = MibTableColumn
crlExternalPercentageBufferUsage = _CrlExternalPercentageBufferUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 6, 1, 6),
    _CrlExternalPercentageBufferUsage_Type()
)
crlExternalPercentageBufferUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crlExternalPercentageBufferUsage.setStatus("current")
if mibBuilder.loadTexts:
    crlExternalPercentageBufferUsage.setUnits("percentage")
_CrlExternalPercentageBufferUsageDisplay_Type = SnmpAdminString
_CrlExternalPercentageBufferUsageDisplay_Object = MibTableColumn
crlExternalPercentageBufferUsageDisplay = _CrlExternalPercentageBufferUsageDisplay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 6, 1, 7),
    _CrlExternalPercentageBufferUsageDisplay_Type()
)
crlExternalPercentageBufferUsageDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crlExternalPercentageBufferUsageDisplay.setStatus("current")
if mibBuilder.loadTexts:
    crlExternalPercentageBufferUsageDisplay.setUnits("percentage")
_CiscoL4L7NpCpuUtilTable_Object = MibTable
ciscoL4L7NpCpuUtilTable = _CiscoL4L7NpCpuUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 7)
)
if mibBuilder.loadTexts:
    ciscoL4L7NpCpuUtilTable.setStatus("current")
_CiscoL4L7NpCpuUtilEntry_Object = MibTableRow
ciscoL4L7NpCpuUtilEntry = _CiscoL4L7NpCpuUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 7, 1)
)
ciscoL4L7NpCpuUtilEntry.setIndexNames(
    (0, "CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "clrNetworkProcessor"),
)
if mibBuilder.loadTexts:
    ciscoL4L7NpCpuUtilEntry.setStatus("current")
_ClrNpCpuUtilizationAverage_Type = Gauge32
_ClrNpCpuUtilizationAverage_Object = MibTableColumn
clrNpCpuUtilizationAverage = _ClrNpCpuUtilizationAverage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 1, 7, 1, 1),
    _ClrNpCpuUtilizationAverage_Type()
)
clrNpCpuUtilizationAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrNpCpuUtilizationAverage.setStatus("current")
_CrlNotificationObjects_ObjectIdentity = ObjectIdentity
crlNotificationObjects = _CrlNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 2)
)


class _ClrResourceLimitReachedNotifEnabled_Type(TruthValue):
    """Custom type clrResourceLimitReachedNotifEnabled based on TruthValue"""


_ClrResourceLimitReachedNotifEnabled_Object = MibScalar
clrResourceLimitReachedNotifEnabled = _ClrResourceLimitReachedNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 2, 1),
    _ClrResourceLimitReachedNotifEnabled_Type()
)
clrResourceLimitReachedNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrResourceLimitReachedNotifEnabled.setStatus("current")


class _ClrResourceRateLimitReachedNotifEnabled_Type(TruthValue):
    """Custom type clrResourceRateLimitReachedNotifEnabled based on TruthValue"""


_ClrResourceRateLimitReachedNotifEnabled_Object = MibScalar
clrResourceRateLimitReachedNotifEnabled = _ClrResourceRateLimitReachedNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 2, 2),
    _ClrResourceRateLimitReachedNotifEnabled_Type()
)
clrResourceRateLimitReachedNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrResourceRateLimitReachedNotifEnabled.setStatus("current")
_CrlNotificationOnlyObjects_ObjectIdentity = ObjectIdentity
crlNotificationOnlyObjects = _CrlNotificationOnlyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 3)
)


class _CrlNotifType_Type(Integer32):
    """Custom type crlNotifType based on Integer32"""
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
        *(("fallingMinThresh", 2),
          ("fallingWatermarkThresh", 3),
          ("risingHighThresh", 1),
          ("risingWatermarkThresh", 4))
    )


_CrlNotifType_Type.__name__ = "Integer32"
_CrlNotifType_Object = MibScalar
crlNotifType = _CrlNotifType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 3, 1),
    _CrlNotifType_Type()
)
crlNotifType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    crlNotifType.setStatus("current")


class _CrlNotifContextOrSystem_Type(Integer32):
    """Custom type crlNotifContextOrSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("context", 2),
          ("system", 1))
    )


_CrlNotifContextOrSystem_Type.__name__ = "Integer32"
_CrlNotifContextOrSystem_Object = MibScalar
crlNotifContextOrSystem = _CrlNotifContextOrSystem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 3, 2),
    _CrlNotifContextOrSystem_Type()
)
crlNotifContextOrSystem.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    crlNotifContextOrSystem.setStatus("current")
_CrlNotifContextName_Type = SnmpAdminString
_CrlNotifContextName_Object = MibScalar
crlNotifContextName = _CrlNotifContextName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 3, 3),
    _CrlNotifContextName_Type()
)
crlNotifContextName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    crlNotifContextName.setStatus("current")
_CrlNotifCurrentUsagePcnt_Type = Unsigned32
_CrlNotifCurrentUsagePcnt_Object = MibScalar
crlNotifCurrentUsagePcnt = _CrlNotifCurrentUsagePcnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 3, 4),
    _CrlNotifCurrentUsagePcnt_Type()
)
crlNotifCurrentUsagePcnt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    crlNotifCurrentUsagePcnt.setStatus("current")
if mibBuilder.loadTexts:
    crlNotifCurrentUsagePcnt.setUnits("percent")


class _CrlNotifMaxThresholdPcnt_Type(Unsigned32):
    """Custom type crlNotifMaxThresholdPcnt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CrlNotifMaxThresholdPcnt_Type.__name__ = "Unsigned32"
_CrlNotifMaxThresholdPcnt_Object = MibScalar
crlNotifMaxThresholdPcnt = _CrlNotifMaxThresholdPcnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 3, 5),
    _CrlNotifMaxThresholdPcnt_Type()
)
crlNotifMaxThresholdPcnt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    crlNotifMaxThresholdPcnt.setStatus("current")
if mibBuilder.loadTexts:
    crlNotifMaxThresholdPcnt.setUnits("percent")


class _CrlNotifWatermarkPcnt_Type(Unsigned32):
    """Custom type crlNotifWatermarkPcnt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CrlNotifWatermarkPcnt_Type.__name__ = "Unsigned32"
_CrlNotifWatermarkPcnt_Object = MibScalar
crlNotifWatermarkPcnt = _CrlNotifWatermarkPcnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 3, 6),
    _CrlNotifWatermarkPcnt_Type()
)
crlNotifWatermarkPcnt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    crlNotifWatermarkPcnt.setStatus("current")
if mibBuilder.loadTexts:
    crlNotifWatermarkPcnt.setUnits("percent")


class _CrlNotifMinThresholdPcnt_Type(Unsigned32):
    """Custom type crlNotifMinThresholdPcnt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CrlNotifMinThresholdPcnt_Type.__name__ = "Unsigned32"
_CrlNotifMinThresholdPcnt_Object = MibScalar
crlNotifMinThresholdPcnt = _CrlNotifMinThresholdPcnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 3, 7),
    _CrlNotifMinThresholdPcnt_Type()
)
crlNotifMinThresholdPcnt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    crlNotifMinThresholdPcnt.setStatus("current")
if mibBuilder.loadTexts:
    crlNotifMinThresholdPcnt.setUnits("percent")


class _CrlNotifSourceType_Type(Integer32):
    """Custom type crlNotifSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("realServer", 2),
          ("virtualIP", 1))
    )


_CrlNotifSourceType_Type.__name__ = "Integer32"
_CrlNotifSourceType_Object = MibScalar
crlNotifSourceType = _CrlNotifSourceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 3, 8),
    _CrlNotifSourceType_Type()
)
crlNotifSourceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    crlNotifSourceType.setStatus("current")
_CrlNotifRealServerName_Type = SnmpAdminString
_CrlNotifRealServerName_Object = MibScalar
crlNotifRealServerName = _CrlNotifRealServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 3, 9),
    _CrlNotifRealServerName_Type()
)
crlNotifRealServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    crlNotifRealServerName.setStatus("current")
_CrlNotifVirtualIPAddrType_Type = InetAddressType
_CrlNotifVirtualIPAddrType_Object = MibScalar
crlNotifVirtualIPAddrType = _CrlNotifVirtualIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 3, 10),
    _CrlNotifVirtualIPAddrType_Type()
)
crlNotifVirtualIPAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    crlNotifVirtualIPAddrType.setStatus("current")
_CrlNotifVirtualIPAddress_Type = InetAddress
_CrlNotifVirtualIPAddress_Object = MibScalar
crlNotifVirtualIPAddress = _CrlNotifVirtualIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 1, 3, 11),
    _CrlNotifVirtualIPAddress_Type()
)
crlNotifVirtualIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    crlNotifVirtualIPAddress.setStatus("current")
_CiscoResourceLimitMIBConform_ObjectIdentity = ObjectIdentity
ciscoResourceLimitMIBConform = _CiscoResourceLimitMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 2)
)
_CiscoL4L7ResourceLimitConformance_ObjectIdentity = ObjectIdentity
ciscoL4L7ResourceLimitConformance = _CiscoL4L7ResourceLimitConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 3)
)
_CiscoL4L7ResourceLimitCompliances_ObjectIdentity = ObjectIdentity
ciscoL4L7ResourceLimitCompliances = _CiscoL4L7ResourceLimitCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 1)
)
_CiscoL4L7ResourceLimitGroups_ObjectIdentity = ObjectIdentity
ciscoL4L7ResourceLimitGroups = _CiscoL4L7ResourceLimitGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2)
)

# Managed Objects groups

ciscoL4L7ResourceClassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 1)
)
ciscoL4L7ResourceClassGroup.setObjects(
      *(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceClassStorageType"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceClassRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceClassGroup.setStatus("current")

ciscoL4L7ResourceLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 2)
)
ciscoL4L7ResourceLimitGroup.setObjects(
      *(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitValueType"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitMin"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitMax"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitStorageType"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceLimitGroup.setStatus("current")

ciscoL4L7ResourceRateLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 3)
)
ciscoL4L7ResourceRateLimitGroup.setObjects(
      *(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceMin"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceMax"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceStorageType"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceRateLimitGroup.setStatus("current")

ciscoL4L7ResourceLimitUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 4)
)
ciscoL4L7ResourceLimitUsageGroup.setObjects(
      *(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitCurrentUsage"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitPeakUsage"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitReqsDeniedCount"))
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceLimitUsageGroup.setStatus("current")

ciscoL4L7ResourceRateLimitUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 5)
)
ciscoL4L7ResourceRateLimitUsageGroup.setObjects(
      *(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceCurrentUsage"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourcePeakUsage"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceReqsDeniedCount"))
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceRateLimitUsageGroup.setStatus("current")

ciscoL4L7ResourceNotifEnabledGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 6)
)
ciscoL4L7ResourceNotifEnabledGroup.setObjects(
      *(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "clrResourceLimitReachedNotifEnabled"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "clrResourceRateLimitReachedNotifEnabled"))
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceNotifEnabledGroup.setStatus("current")

ciscoL4L7ResourceUsageSummaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 8)
)
ciscoL4L7ResourceUsageSummaryGroup.setObjects(
      *(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceSummaryCurrentUsage"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceSummaryPeakUsage"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceSummaryReqsDeniedCount"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceSummaryLastClearedTime"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceSummaryStorageType"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceSummaryRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceUsageSummaryGroup.setStatus("current")

ciscoL4L7BufferUtilizationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 9)
)
ciscoL4L7BufferUtilizationGroup.setObjects(
      *(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlBufferUsageValue"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlPercentageBufferUsage"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlPercentageBufferUsageDisplay"))
)
if mibBuilder.loadTexts:
    ciscoL4L7BufferUtilizationGroup.setStatus("deprecated")

ciscoL4L7NpCpuUtilizationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 10)
)
ciscoL4L7NpCpuUtilizationGroup.setObjects(
    ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "clrNpCpuUtilizationAverage")
)
if mibBuilder.loadTexts:
    ciscoL4L7NpCpuUtilizationGroup.setStatus("current")

ciscoL4L7BufferUtilizationGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 11)
)
ciscoL4L7BufferUtilizationGroupRev1.setObjects(
      *(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlBufferUsageValue"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlPercentageBufferUsage"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlPercentageBufferUsageDisplay"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlExternalBufferUsageValue"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlExternalPercentageBufferUsage"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlExternalPercentageBufferUsageDisplay"))
)
if mibBuilder.loadTexts:
    ciscoL4L7BufferUtilizationGroupRev1.setStatus("current")

ciscoL4L7ResourceNotifOnlyObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 13)
)
ciscoL4L7ResourceNotifOnlyObjectsGroup.setObjects(
      *(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifType"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifCurrentUsagePcnt"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifMaxThresholdPcnt"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifWatermarkPcnt"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifMinThresholdPcnt"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifContextOrSystem"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifContextName"))
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceNotifOnlyObjectsGroup.setStatus("current")

ciscoL4L7ResourceNotifOnlyObjectsGroupExt = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 15)
)
ciscoL4L7ResourceNotifOnlyObjectsGroupExt.setObjects(
      *(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifSourceType"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifRealServerName"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifVirtualIPAddrType"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifVirtualIPAddress"))
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceNotifOnlyObjectsGroupExt.setStatus("current")


# Notification objects

clrResourceLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 0, 1)
)
clrResourceLimitReached.setObjects(
      *(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitValueType"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitMax"))
)
if mibBuilder.loadTexts:
    clrResourceLimitReached.setStatus(
        "deprecated"
    )

clrResourceRateLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 0, 2)
)
clrResourceRateLimitReached.setObjects(
    ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceMax")
)
if mibBuilder.loadTexts:
    clrResourceRateLimitReached.setStatus(
        "deprecated"
    )

clrResourceLimitReachedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 0, 3)
)
clrResourceLimitReachedNotif.setObjects(
      *(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifType"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitCurrentUsage"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitMax"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitMin"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifCurrentUsagePcnt"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifMaxThresholdPcnt"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifWatermarkPcnt"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifMinThresholdPcnt"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifContextOrSystem"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifContextName"))
)
if mibBuilder.loadTexts:
    clrResourceLimitReachedNotif.setStatus(
        "deprecated"
    )

clrResourceRateLimitReachedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 0, 4)
)
clrResourceRateLimitReachedNotif.setObjects(
      *(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifType"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceCurrentUsage"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceMax"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceMin"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifCurrentUsagePcnt"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifMaxThresholdPcnt"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifWatermarkPcnt"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifMinThresholdPcnt"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifContextOrSystem"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifContextName"))
)
if mibBuilder.loadTexts:
    clrResourceRateLimitReachedNotif.setStatus(
        "deprecated"
    )

clrResourceRateLimitReachedNotifRev1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 0, 5)
)
clrResourceRateLimitReachedNotifRev1.setObjects(
      *(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifType"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceCurrentUsage"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceMax"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlRateLimitResourceMin"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifCurrentUsagePcnt"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifMaxThresholdPcnt"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifWatermarkPcnt"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifMinThresholdPcnt"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifContextOrSystem"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifContextName"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifSourceType"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifRealServerName"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifVirtualIPAddrType"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifVirtualIPAddress"))
)
if mibBuilder.loadTexts:
    clrResourceRateLimitReachedNotifRev1.setStatus(
        "current"
    )

clrResourceLimitReachedNotifRev1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 0, 6)
)
clrResourceLimitReachedNotifRev1.setObjects(
      *(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifType"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitCurrentUsage"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitMax"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlResourceLimitMin"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifCurrentUsagePcnt"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifMaxThresholdPcnt"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifWatermarkPcnt"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifMinThresholdPcnt"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifContextOrSystem"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifContextName"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifSourceType"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifRealServerName"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifVirtualIPAddrType"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "crlNotifVirtualIPAddress"))
)
if mibBuilder.loadTexts:
    clrResourceLimitReachedNotifRev1.setStatus(
        "current"
    )


# Notifications groups

ciscoL4L7ResourceNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 7)
)
ciscoL4L7ResourceNotifGroup.setObjects(
      *(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "clrResourceLimitReached"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "clrResourceRateLimitReached"))
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceNotifGroup.setStatus(
        "deprecated"
    )

ciscoL4L7ResourceNotifGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 12)
)
ciscoL4L7ResourceNotifGroupRev1.setObjects(
      *(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "clrResourceLimitReachedNotif"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "clrResourceRateLimitReachedNotif"))
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceNotifGroupRev1.setStatus(
        "deprecated"
    )

ciscoL4L7ResourceNotifGroupRev2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 2, 14)
)
ciscoL4L7ResourceNotifGroupRev2.setObjects(
      *(("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "clrResourceLimitReachedNotifRev1"),
        ("CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB", "clrResourceRateLimitReachedNotifRev1"))
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceNotifGroupRev2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoL4L7ResourceLimitCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceLimitCompliance.setStatus(
        "deprecated"
    )

ciscoL4L7ResourceLimitComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceLimitComplianceRev1.setStatus(
        "deprecated"
    )

ciscoL4L7ResourceLimitComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceLimitComplianceRev2.setStatus(
        "deprecated"
    )

ciscoL4L7ResourceLimitComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceLimitComplianceRev3.setStatus(
        "deprecated"
    )

ciscoL4L7ResourceLimitComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceLimitComplianceRev4.setStatus(
        "deprecated"
    )

ciscoL4L7ResourceLimitComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceLimitComplianceRev5.setStatus(
        "deprecated"
    )

ciscoL4L7ResourceLimitComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 1, 7)
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceLimitComplianceRev6.setStatus(
        "deprecated"
    )

ciscoL4L7ResourceLimitComplianceRev7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 480, 3, 1, 8)
)
if mibBuilder.loadTexts:
    ciscoL4L7ResourceLimitComplianceRev7.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB",
    **{"CiscoResourceClass": CiscoResourceClass,
       "CiscoResourceLimitType": CiscoResourceLimitType,
       "CiscoRateLimitResourceType": CiscoRateLimitResourceType,
       "CiscoResourceType": CiscoResourceType,
       "CiscoBufferUtilPercentage": CiscoBufferUtilPercentage,
       "ciscoL4L7moduleResourceLimitMIB": ciscoL4L7moduleResourceLimitMIB,
       "ciscoL4L7ResourceLimitNotifs": ciscoL4L7ResourceLimitNotifs,
       "clrResourceLimitReached": clrResourceLimitReached,
       "clrResourceRateLimitReached": clrResourceRateLimitReached,
       "clrResourceLimitReachedNotif": clrResourceLimitReachedNotif,
       "clrResourceRateLimitReachedNotif": clrResourceRateLimitReachedNotif,
       "clrResourceRateLimitReachedNotifRev1": clrResourceRateLimitReachedNotifRev1,
       "clrResourceLimitReachedNotifRev1": clrResourceLimitReachedNotifRev1,
       "ciscoL4L7ResourceLimitMIBObjects": ciscoL4L7ResourceLimitMIBObjects,
       "crlResource": crlResource,
       "ciscoL4L7ResourceClassTable": ciscoL4L7ResourceClassTable,
       "ciscoL4L7ResourceClassEntry": ciscoL4L7ResourceClassEntry,
       "crlResourceClassName": crlResourceClassName,
       "crlResourceClassStorageType": crlResourceClassStorageType,
       "crlResourceClassRowStatus": crlResourceClassRowStatus,
       "ciscoL4L7ResourceLimitTable": ciscoL4L7ResourceLimitTable,
       "ciscoL4L7ResourceLimitEntry": ciscoL4L7ResourceLimitEntry,
       "crlResourceLimitType": crlResourceLimitType,
       "crlResourceLimitValueType": crlResourceLimitValueType,
       "crlResourceLimitMin": crlResourceLimitMin,
       "crlResourceLimitMax": crlResourceLimitMax,
       "crlResourceLimitStorageType": crlResourceLimitStorageType,
       "crlResourceLimitRowStatus": crlResourceLimitRowStatus,
       "crlResourceLimitCurrentUsage": crlResourceLimitCurrentUsage,
       "crlResourceLimitPeakUsage": crlResourceLimitPeakUsage,
       "crlResourceLimitReqsDeniedCount": crlResourceLimitReqsDeniedCount,
       "ciscoL4L7ResourceRateLimitTable": ciscoL4L7ResourceRateLimitTable,
       "ciscoL4L7ResourceRateLimitEntry": ciscoL4L7ResourceRateLimitEntry,
       "crlRateLimitResourceType": crlRateLimitResourceType,
       "crlRateLimitResourceMin": crlRateLimitResourceMin,
       "crlRateLimitResourceMax": crlRateLimitResourceMax,
       "crlRateLimitResourceStorageType": crlRateLimitResourceStorageType,
       "crlRateLimitResourceRowStatus": crlRateLimitResourceRowStatus,
       "crlRateLimitResourceCurrentUsage": crlRateLimitResourceCurrentUsage,
       "crlRateLimitResourcePeakUsage": crlRateLimitResourcePeakUsage,
       "crlRateLimitResourceReqsDeniedCount": crlRateLimitResourceReqsDeniedCount,
       "ciscoL4L7ResourceUsageSummaryTable": ciscoL4L7ResourceUsageSummaryTable,
       "ciscoL4L7ResourceUsageSummaryEntry": ciscoL4L7ResourceUsageSummaryEntry,
       "crlResourceSummaryType": crlResourceSummaryType,
       "crlResourceSummaryCurrentUsage": crlResourceSummaryCurrentUsage,
       "crlResourceSummaryPeakUsage": crlResourceSummaryPeakUsage,
       "crlResourceSummaryReqsDeniedCount": crlResourceSummaryReqsDeniedCount,
       "crlResourceSummaryLastClearedTime": crlResourceSummaryLastClearedTime,
       "crlResourceSummaryStorageType": crlResourceSummaryStorageType,
       "crlResourceSummaryRowStatus": crlResourceSummaryRowStatus,
       "ciscoL4L7BufferUtilizationTable": ciscoL4L7BufferUtilizationTable,
       "ciscoL4L7BufferUtilizationEntry": ciscoL4L7BufferUtilizationEntry,
       "clrNetworkProcessor": clrNetworkProcessor,
       "crlBufferUsageValue": crlBufferUsageValue,
       "crlPercentageBufferUsage": crlPercentageBufferUsage,
       "crlPercentageBufferUsageDisplay": crlPercentageBufferUsageDisplay,
       "crlExternalBufferUsageValue": crlExternalBufferUsageValue,
       "crlExternalPercentageBufferUsage": crlExternalPercentageBufferUsage,
       "crlExternalPercentageBufferUsageDisplay": crlExternalPercentageBufferUsageDisplay,
       "ciscoL4L7NpCpuUtilTable": ciscoL4L7NpCpuUtilTable,
       "ciscoL4L7NpCpuUtilEntry": ciscoL4L7NpCpuUtilEntry,
       "clrNpCpuUtilizationAverage": clrNpCpuUtilizationAverage,
       "crlNotificationObjects": crlNotificationObjects,
       "clrResourceLimitReachedNotifEnabled": clrResourceLimitReachedNotifEnabled,
       "clrResourceRateLimitReachedNotifEnabled": clrResourceRateLimitReachedNotifEnabled,
       "crlNotificationOnlyObjects": crlNotificationOnlyObjects,
       "crlNotifType": crlNotifType,
       "crlNotifContextOrSystem": crlNotifContextOrSystem,
       "crlNotifContextName": crlNotifContextName,
       "crlNotifCurrentUsagePcnt": crlNotifCurrentUsagePcnt,
       "crlNotifMaxThresholdPcnt": crlNotifMaxThresholdPcnt,
       "crlNotifWatermarkPcnt": crlNotifWatermarkPcnt,
       "crlNotifMinThresholdPcnt": crlNotifMinThresholdPcnt,
       "crlNotifSourceType": crlNotifSourceType,
       "crlNotifRealServerName": crlNotifRealServerName,
       "crlNotifVirtualIPAddrType": crlNotifVirtualIPAddrType,
       "crlNotifVirtualIPAddress": crlNotifVirtualIPAddress,
       "ciscoResourceLimitMIBConform": ciscoResourceLimitMIBConform,
       "ciscoL4L7ResourceLimitConformance": ciscoL4L7ResourceLimitConformance,
       "ciscoL4L7ResourceLimitCompliances": ciscoL4L7ResourceLimitCompliances,
       "ciscoL4L7ResourceLimitCompliance": ciscoL4L7ResourceLimitCompliance,
       "ciscoL4L7ResourceLimitComplianceRev1": ciscoL4L7ResourceLimitComplianceRev1,
       "ciscoL4L7ResourceLimitComplianceRev2": ciscoL4L7ResourceLimitComplianceRev2,
       "ciscoL4L7ResourceLimitComplianceRev3": ciscoL4L7ResourceLimitComplianceRev3,
       "ciscoL4L7ResourceLimitComplianceRev4": ciscoL4L7ResourceLimitComplianceRev4,
       "ciscoL4L7ResourceLimitComplianceRev5": ciscoL4L7ResourceLimitComplianceRev5,
       "ciscoL4L7ResourceLimitComplianceRev6": ciscoL4L7ResourceLimitComplianceRev6,
       "ciscoL4L7ResourceLimitComplianceRev7": ciscoL4L7ResourceLimitComplianceRev7,
       "ciscoL4L7ResourceLimitGroups": ciscoL4L7ResourceLimitGroups,
       "ciscoL4L7ResourceClassGroup": ciscoL4L7ResourceClassGroup,
       "ciscoL4L7ResourceLimitGroup": ciscoL4L7ResourceLimitGroup,
       "ciscoL4L7ResourceRateLimitGroup": ciscoL4L7ResourceRateLimitGroup,
       "ciscoL4L7ResourceLimitUsageGroup": ciscoL4L7ResourceLimitUsageGroup,
       "ciscoL4L7ResourceRateLimitUsageGroup": ciscoL4L7ResourceRateLimitUsageGroup,
       "ciscoL4L7ResourceNotifEnabledGroup": ciscoL4L7ResourceNotifEnabledGroup,
       "ciscoL4L7ResourceNotifGroup": ciscoL4L7ResourceNotifGroup,
       "ciscoL4L7ResourceUsageSummaryGroup": ciscoL4L7ResourceUsageSummaryGroup,
       "ciscoL4L7BufferUtilizationGroup": ciscoL4L7BufferUtilizationGroup,
       "ciscoL4L7NpCpuUtilizationGroup": ciscoL4L7NpCpuUtilizationGroup,
       "ciscoL4L7BufferUtilizationGroupRev1": ciscoL4L7BufferUtilizationGroupRev1,
       "ciscoL4L7ResourceNotifGroupRev1": ciscoL4L7ResourceNotifGroupRev1,
       "ciscoL4L7ResourceNotifOnlyObjectsGroup": ciscoL4L7ResourceNotifOnlyObjectsGroup,
       "ciscoL4L7ResourceNotifGroupRev2": ciscoL4L7ResourceNotifGroupRev2,
       "ciscoL4L7ResourceNotifOnlyObjectsGroupExt": ciscoL4L7ResourceNotifOnlyObjectsGroupExt}
)
