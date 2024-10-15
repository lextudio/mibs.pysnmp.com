# SNMP MIB module (HM2-LOGGING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-LOGGING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:05 2024
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

(Hm2TlsCipherSuites,
 Hm2TlsVersions) = mibBuilder.importSymbols(
    "HM2-MGMTACCESS-MIB",
    "Hm2TlsCipherSuites",
    "Hm2TlsVersions")

(HmEnabledStatus,
 HmTimeSeconds1970,
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "HmTimeSeconds1970",
    "hm2ConfigurationMibs")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hm2LoggingMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 23)
)
hm2LoggingMib.setRevisions(
        ("2012-08-08 00:00",
         "2011-03-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HmAgentLogSeverity(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("informational", 6),
          ("notice", 5),
          ("warning", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Hm2LoggingMibNotifications_ObjectIdentity = ObjectIdentity
hm2LoggingMibNotifications = _Hm2LoggingMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 0)
)
_Hm2LoggingMibObjects_ObjectIdentity = ObjectIdentity
hm2LoggingMibObjects = _Hm2LoggingMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1)
)
_Hm2LogSnmpLoggingGroup_ObjectIdentity = ObjectIdentity
hm2LogSnmpLoggingGroup = _Hm2LogSnmpLoggingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 1)
)


class _Hm2LogSnmpLogGetRequest_Type(HmEnabledStatus):
    """Custom type hm2LogSnmpLogGetRequest based on HmEnabledStatus"""


_Hm2LogSnmpLogGetRequest_Object = MibScalar
hm2LogSnmpLogGetRequest = _Hm2LogSnmpLogGetRequest_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 1, 1),
    _Hm2LogSnmpLogGetRequest_Type()
)
hm2LogSnmpLogGetRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LogSnmpLogGetRequest.setStatus("current")


class _Hm2LogSnmpLogSetRequest_Type(HmEnabledStatus):
    """Custom type hm2LogSnmpLogSetRequest based on HmEnabledStatus"""


_Hm2LogSnmpLogSetRequest_Object = MibScalar
hm2LogSnmpLogSetRequest = _Hm2LogSnmpLogSetRequest_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 1, 2),
    _Hm2LogSnmpLogSetRequest_Type()
)
hm2LogSnmpLogSetRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LogSnmpLogSetRequest.setStatus("current")


class _Hm2LogSnmpLogGetSeverity_Type(HmAgentLogSeverity):
    """Custom type hm2LogSnmpLogGetSeverity based on HmAgentLogSeverity"""


_Hm2LogSnmpLogGetSeverity_Object = MibScalar
hm2LogSnmpLogGetSeverity = _Hm2LogSnmpLogGetSeverity_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 1, 3),
    _Hm2LogSnmpLogGetSeverity_Type()
)
hm2LogSnmpLogGetSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LogSnmpLogGetSeverity.setStatus("current")


class _Hm2LogSnmpLogSetSeverity_Type(HmAgentLogSeverity):
    """Custom type hm2LogSnmpLogSetSeverity based on HmAgentLogSeverity"""


_Hm2LogSnmpLogSetSeverity_Object = MibScalar
hm2LogSnmpLogSetSeverity = _Hm2LogSnmpLogSetSeverity_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 1, 4),
    _Hm2LogSnmpLogSetSeverity_Type()
)
hm2LogSnmpLogSetSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LogSnmpLogSetSeverity.setStatus("current")
_Hm2LogCliCommandsLoggingGroup_ObjectIdentity = ObjectIdentity
hm2LogCliCommandsLoggingGroup = _Hm2LogCliCommandsLoggingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 2)
)


class _Hm2LogCliCommandsAdminStatus_Type(HmEnabledStatus):
    """Custom type hm2LogCliCommandsAdminStatus based on HmEnabledStatus"""


_Hm2LogCliCommandsAdminStatus_Object = MibScalar
hm2LogCliCommandsAdminStatus = _Hm2LogCliCommandsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 2, 1),
    _Hm2LogCliCommandsAdminStatus_Type()
)
hm2LogCliCommandsAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LogCliCommandsAdminStatus.setStatus("current")
_Hm2LogConsoleLoggingGroup_ObjectIdentity = ObjectIdentity
hm2LogConsoleLoggingGroup = _Hm2LogConsoleLoggingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 3)
)


class _Hm2LogConsoleAdminStatus_Type(HmEnabledStatus):
    """Custom type hm2LogConsoleAdminStatus based on HmEnabledStatus"""


_Hm2LogConsoleAdminStatus_Object = MibScalar
hm2LogConsoleAdminStatus = _Hm2LogConsoleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 3, 1),
    _Hm2LogConsoleAdminStatus_Type()
)
hm2LogConsoleAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LogConsoleAdminStatus.setStatus("current")


class _Hm2LogConsoleSeverityFilter_Type(HmAgentLogSeverity):
    """Custom type hm2LogConsoleSeverityFilter based on HmAgentLogSeverity"""


_Hm2LogConsoleSeverityFilter_Object = MibScalar
hm2LogConsoleSeverityFilter = _Hm2LogConsoleSeverityFilter_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 3, 2),
    _Hm2LogConsoleSeverityFilter_Type()
)
hm2LogConsoleSeverityFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LogConsoleSeverityFilter.setStatus("current")
_Hm2LogBufferedLoggingGroup_ObjectIdentity = ObjectIdentity
hm2LogBufferedLoggingGroup = _Hm2LogBufferedLoggingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 4)
)


class _Hm2LogBufferdLogLevelThreshold_Type(HmAgentLogSeverity):
    """Custom type hm2LogBufferdLogLevelThreshold based on HmAgentLogSeverity"""


_Hm2LogBufferdLogLevelThreshold_Object = MibScalar
hm2LogBufferdLogLevelThreshold = _Hm2LogBufferdLogLevelThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 4, 1),
    _Hm2LogBufferdLogLevelThreshold_Type()
)
hm2LogBufferdLogLevelThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LogBufferdLogLevelThreshold.setStatus("current")
_Hm2LogSyslogGroup_ObjectIdentity = ObjectIdentity
hm2LogSyslogGroup = _Hm2LogSyslogGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5)
)


class _Hm2LogSyslogAdminStatus_Type(HmEnabledStatus):
    """Custom type hm2LogSyslogAdminStatus based on HmEnabledStatus"""


_Hm2LogSyslogAdminStatus_Object = MibScalar
hm2LogSyslogAdminStatus = _Hm2LogSyslogAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5, 1),
    _Hm2LogSyslogAdminStatus_Type()
)
hm2LogSyslogAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LogSyslogAdminStatus.setStatus("current")


class _Hm2LogSyslogClientTlsVersions_Type(Hm2TlsVersions):
    """Custom type hm2LogSyslogClientTlsVersions based on Hm2TlsVersions"""
    defaultBinValue = "001"


_Hm2LogSyslogClientTlsVersions_Object = MibScalar
hm2LogSyslogClientTlsVersions = _Hm2LogSyslogClientTlsVersions_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5, 2),
    _Hm2LogSyslogClientTlsVersions_Type()
)
hm2LogSyslogClientTlsVersions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LogSyslogClientTlsVersions.setStatus("current")


class _Hm2LogSyslogClientTlsCipherSuites_Type(Hm2TlsCipherSuites):
    """Custom type hm2LogSyslogClientTlsCipherSuites based on Hm2TlsCipherSuites"""
    defaultBinValue = "0110101"


_Hm2LogSyslogClientTlsCipherSuites_Object = MibScalar
hm2LogSyslogClientTlsCipherSuites = _Hm2LogSyslogClientTlsCipherSuites_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5, 3),
    _Hm2LogSyslogClientTlsCipherSuites_Type()
)
hm2LogSyslogClientTlsCipherSuites.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LogSyslogClientTlsCipherSuites.setStatus("current")
_Hm2LogSyslogServerTable_Object = MibTable
hm2LogSyslogServerTable = _Hm2LogSyslogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5, 10)
)
if mibBuilder.loadTexts:
    hm2LogSyslogServerTable.setStatus("current")
_Hm2LogSyslogServerEntry_Object = MibTableRow
hm2LogSyslogServerEntry = _Hm2LogSyslogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5, 10, 1)
)
hm2LogSyslogServerEntry.setIndexNames(
    (0, "HM2-LOGGING-MIB", "hm2LogSyslogServerIndex"),
)
if mibBuilder.loadTexts:
    hm2LogSyslogServerEntry.setStatus("current")


class _Hm2LogSyslogServerIndex_Type(Integer32):
    """Custom type hm2LogSyslogServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Hm2LogSyslogServerIndex_Type.__name__ = "Integer32"
_Hm2LogSyslogServerIndex_Object = MibTableColumn
hm2LogSyslogServerIndex = _Hm2LogSyslogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5, 10, 1, 1),
    _Hm2LogSyslogServerIndex_Type()
)
hm2LogSyslogServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LogSyslogServerIndex.setStatus("current")


class _Hm2LogSyslogServerIPAddrType_Type(InetAddressType):
    """Custom type hm2LogSyslogServerIPAddrType based on InetAddressType"""


_Hm2LogSyslogServerIPAddrType_Object = MibTableColumn
hm2LogSyslogServerIPAddrType = _Hm2LogSyslogServerIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5, 10, 1, 2),
    _Hm2LogSyslogServerIPAddrType_Type()
)
hm2LogSyslogServerIPAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LogSyslogServerIPAddrType.setStatus("current")


class _Hm2LogSyslogServerIPAddr_Type(InetAddress):
    """Custom type hm2LogSyslogServerIPAddr based on InetAddress"""
    defaultHexValue = "00000000"


_Hm2LogSyslogServerIPAddr_Object = MibTableColumn
hm2LogSyslogServerIPAddr = _Hm2LogSyslogServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5, 10, 1, 3),
    _Hm2LogSyslogServerIPAddr_Type()
)
hm2LogSyslogServerIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LogSyslogServerIPAddr.setStatus("current")


class _Hm2LogSyslogServerUdpPort_Type(InetPortNumber):
    """Custom type hm2LogSyslogServerUdpPort based on InetPortNumber"""
    defaultValue = 514


_Hm2LogSyslogServerUdpPort_Object = MibTableColumn
hm2LogSyslogServerUdpPort = _Hm2LogSyslogServerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5, 10, 1, 4),
    _Hm2LogSyslogServerUdpPort_Type()
)
hm2LogSyslogServerUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LogSyslogServerUdpPort.setStatus("current")


class _Hm2LogSyslogServerLevelUpto_Type(HmAgentLogSeverity):
    """Custom type hm2LogSyslogServerLevelUpto based on HmAgentLogSeverity"""


_Hm2LogSyslogServerLevelUpto_Object = MibTableColumn
hm2LogSyslogServerLevelUpto = _Hm2LogSyslogServerLevelUpto_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5, 10, 1, 5),
    _Hm2LogSyslogServerLevelUpto_Type()
)
hm2LogSyslogServerLevelUpto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LogSyslogServerLevelUpto.setStatus("current")


class _Hm2LogSyslogServerLogType_Type(Integer32):
    """Custom type hm2LogSyslogServerLogType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("audittrail", 2),
          ("systemlog", 1))
    )


_Hm2LogSyslogServerLogType_Type.__name__ = "Integer32"
_Hm2LogSyslogServerLogType_Object = MibTableColumn
hm2LogSyslogServerLogType = _Hm2LogSyslogServerLogType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5, 10, 1, 6),
    _Hm2LogSyslogServerLogType_Type()
)
hm2LogSyslogServerLogType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LogSyslogServerLogType.setStatus("current")
_Hm2LogSyslogServerRowStatus_Type = RowStatus
_Hm2LogSyslogServerRowStatus_Object = MibTableColumn
hm2LogSyslogServerRowStatus = _Hm2LogSyslogServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5, 10, 1, 7),
    _Hm2LogSyslogServerRowStatus_Type()
)
hm2LogSyslogServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LogSyslogServerRowStatus.setStatus("current")


class _Hm2LogSyslogServerTransportType_Type(Integer32):
    """Custom type hm2LogSyslogServerTransportType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tls", 2),
          ("udp", 1))
    )


_Hm2LogSyslogServerTransportType_Type.__name__ = "Integer32"
_Hm2LogSyslogServerTransportType_Object = MibTableColumn
hm2LogSyslogServerTransportType = _Hm2LogSyslogServerTransportType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5, 10, 1, 8),
    _Hm2LogSyslogServerTransportType_Type()
)
hm2LogSyslogServerTransportType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LogSyslogServerTransportType.setStatus("current")
_Hm2LogPersistentGroup_ObjectIdentity = ObjectIdentity
hm2LogPersistentGroup = _Hm2LogPersistentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 6)
)


class _Hm2LogPersistAdminStatus_Type(HmEnabledStatus):
    """Custom type hm2LogPersistAdminStatus based on HmEnabledStatus"""


_Hm2LogPersistAdminStatus_Object = MibScalar
hm2LogPersistAdminStatus = _Hm2LogPersistAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 6, 1),
    _Hm2LogPersistAdminStatus_Type()
)
hm2LogPersistAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LogPersistAdminStatus.setStatus("current")


class _Hm2LogPersistMaxFileSize_Type(Integer32):
    """Custom type hm2LogPersistMaxFileSize based on Integer32"""
    defaultValue = 1024


_Hm2LogPersistMaxFileSize_Object = MibScalar
hm2LogPersistMaxFileSize = _Hm2LogPersistMaxFileSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 6, 2),
    _Hm2LogPersistMaxFileSize_Type()
)
hm2LogPersistMaxFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LogPersistMaxFileSize.setStatus("current")


class _Hm2LogPersistFilesMax_Type(Integer32):
    """Custom type hm2LogPersistFilesMax based on Integer32"""
    defaultValue = 4


_Hm2LogPersistFilesMax_Object = MibScalar
hm2LogPersistFilesMax = _Hm2LogPersistFilesMax_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 6, 3),
    _Hm2LogPersistFilesMax_Type()
)
hm2LogPersistFilesMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LogPersistFilesMax.setStatus("current")


class _Hm2LogPersistLevelUpto_Type(HmAgentLogSeverity):
    """Custom type hm2LogPersistLevelUpto based on HmAgentLogSeverity"""


_Hm2LogPersistLevelUpto_Object = MibScalar
hm2LogPersistLevelUpto = _Hm2LogPersistLevelUpto_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 6, 4),
    _Hm2LogPersistLevelUpto_Type()
)
hm2LogPersistLevelUpto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LogPersistLevelUpto.setStatus("current")
_Hm2LogPersistentFileTable_Object = MibTable
hm2LogPersistentFileTable = _Hm2LogPersistentFileTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 6, 5)
)
if mibBuilder.loadTexts:
    hm2LogPersistentFileTable.setStatus("current")
_Hm2LogPersistentFileEntry_Object = MibTableRow
hm2LogPersistentFileEntry = _Hm2LogPersistentFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 6, 5, 1)
)
hm2LogPersistentFileEntry.setIndexNames(
    (0, "HM2-LOGGING-MIB", "hm2LogPersistentFileIndex"),
)
if mibBuilder.loadTexts:
    hm2LogPersistentFileEntry.setStatus("current")
_Hm2LogPersistentFileIndex_Type = Integer32
_Hm2LogPersistentFileIndex_Object = MibTableColumn
hm2LogPersistentFileIndex = _Hm2LogPersistentFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 6, 5, 1, 1),
    _Hm2LogPersistentFileIndex_Type()
)
hm2LogPersistentFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2LogPersistentFileIndex.setStatus("current")
_Hm2LogPersistentFileName_Type = DisplayString
_Hm2LogPersistentFileName_Object = MibTableColumn
hm2LogPersistentFileName = _Hm2LogPersistentFileName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 6, 5, 1, 2),
    _Hm2LogPersistentFileName_Type()
)
hm2LogPersistentFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LogPersistentFileName.setStatus("current")
_Hm2LogPersistentFileSize_Type = Integer32
_Hm2LogPersistentFileSize_Object = MibTableColumn
hm2LogPersistentFileSize = _Hm2LogPersistentFileSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 6, 5, 1, 3),
    _Hm2LogPersistentFileSize_Type()
)
hm2LogPersistentFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LogPersistentFileSize.setStatus("current")
_Hm2LogCounterGroup_ObjectIdentity = ObjectIdentity
hm2LogCounterGroup = _Hm2LogCounterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 7)
)
_Hm2LogCounterOperatingHours_Type = Integer32
_Hm2LogCounterOperatingHours_Object = MibScalar
hm2LogCounterOperatingHours = _Hm2LogCounterOperatingHours_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 7, 1),
    _Hm2LogCounterOperatingHours_Type()
)
hm2LogCounterOperatingHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LogCounterOperatingHours.setStatus("current")
_Hm2LogCounterFlashTable_Object = MibTable
hm2LogCounterFlashTable = _Hm2LogCounterFlashTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 7, 10)
)
if mibBuilder.loadTexts:
    hm2LogCounterFlashTable.setStatus("current")
_Hm2LogCounterFlashEntry_Object = MibTableRow
hm2LogCounterFlashEntry = _Hm2LogCounterFlashEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 7, 10, 1)
)
hm2LogCounterFlashEntry.setIndexNames(
    (0, "HM2-LOGGING-MIB", "hm2LogCounterFlashBlock"),
)
if mibBuilder.loadTexts:
    hm2LogCounterFlashEntry.setStatus("current")


class _Hm2LogCounterFlashBlock_Type(Integer32):
    """Custom type hm2LogCounterFlashBlock based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("bootBlock", 1),
          ("dhcpBindings", 7),
          ("fileSystem", 2),
          ("formatFs", 5),
          ("imageStorage", 3),
          ("parameters", 4),
          ("persistentLog", 8),
          ("userFormatFs", 6))
    )


_Hm2LogCounterFlashBlock_Type.__name__ = "Integer32"
_Hm2LogCounterFlashBlock_Object = MibTableColumn
hm2LogCounterFlashBlock = _Hm2LogCounterFlashBlock_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 7, 10, 1, 1),
    _Hm2LogCounterFlashBlock_Type()
)
hm2LogCounterFlashBlock.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2LogCounterFlashBlock.setStatus("current")
_Hm2LogCounterFlashDescription_Type = DisplayString
_Hm2LogCounterFlashDescription_Object = MibTableColumn
hm2LogCounterFlashDescription = _Hm2LogCounterFlashDescription_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 7, 10, 1, 2),
    _Hm2LogCounterFlashDescription_Type()
)
hm2LogCounterFlashDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LogCounterFlashDescription.setStatus("current")
_Hm2LogCounterFlashCount_Type = Integer32
_Hm2LogCounterFlashCount_Object = MibTableColumn
hm2LogCounterFlashCount = _Hm2LogCounterFlashCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 7, 10, 1, 3),
    _Hm2LogCounterFlashCount_Type()
)
hm2LogCounterFlashCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LogCounterFlashCount.setStatus("current")
_Hm2LogCounterFlashValue_Type = Integer32
_Hm2LogCounterFlashValue_Object = MibTableColumn
hm2LogCounterFlashValue = _Hm2LogCounterFlashValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 7, 10, 1, 4),
    _Hm2LogCounterFlashValue_Type()
)
hm2LogCounterFlashValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LogCounterFlashValue.setStatus("current")
_Hm2LogTemperatureGroup_ObjectIdentity = ObjectIdentity
hm2LogTemperatureGroup = _Hm2LogTemperatureGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 8)
)
_Hm2LogTempMinimum_Type = Integer32
_Hm2LogTempMinimum_Object = MibScalar
hm2LogTempMinimum = _Hm2LogTempMinimum_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 8, 1),
    _Hm2LogTempMinimum_Type()
)
hm2LogTempMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LogTempMinimum.setStatus("current")
_Hm2LogTempMaximum_Type = Integer32
_Hm2LogTempMaximum_Object = MibScalar
hm2LogTempMaximum = _Hm2LogTempMaximum_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 8, 2),
    _Hm2LogTempMaximum_Type()
)
hm2LogTempMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LogTempMaximum.setStatus("current")
_Hm2LogTempVariationCount_Type = Integer32
_Hm2LogTempVariationCount_Object = MibScalar
hm2LogTempVariationCount = _Hm2LogTempVariationCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 8, 3),
    _Hm2LogTempVariationCount_Type()
)
hm2LogTempVariationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LogTempVariationCount.setStatus("current")
_Hm2LogTempHistTable_Object = MibTable
hm2LogTempHistTable = _Hm2LogTempHistTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 8, 10)
)
if mibBuilder.loadTexts:
    hm2LogTempHistTable.setStatus("current")
_Hm2LogTempHistEntry_Object = MibTableRow
hm2LogTempHistEntry = _Hm2LogTempHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 8, 10, 1)
)
hm2LogTempHistEntry.setIndexNames(
    (0, "HM2-LOGGING-MIB", "hm2LogTempHistIndex"),
)
if mibBuilder.loadTexts:
    hm2LogTempHistEntry.setStatus("current")
_Hm2LogTempHistIndex_Type = Integer32
_Hm2LogTempHistIndex_Object = MibTableColumn
hm2LogTempHistIndex = _Hm2LogTempHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 8, 10, 1, 1),
    _Hm2LogTempHistIndex_Type()
)
hm2LogTempHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2LogTempHistIndex.setStatus("current")
_Hm2LogTempHistRangeMin_Type = Integer32
_Hm2LogTempHistRangeMin_Object = MibTableColumn
hm2LogTempHistRangeMin = _Hm2LogTempHistRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 8, 10, 1, 2),
    _Hm2LogTempHistRangeMin_Type()
)
hm2LogTempHistRangeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LogTempHistRangeMin.setStatus("current")
_Hm2LogTempHistRangeMax_Type = Integer32
_Hm2LogTempHistRangeMax_Object = MibTableColumn
hm2LogTempHistRangeMax = _Hm2LogTempHistRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 8, 10, 1, 3),
    _Hm2LogTempHistRangeMax_Type()
)
hm2LogTempHistRangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LogTempHistRangeMax.setStatus("current")
_Hm2LogTempHistTime_Type = Integer32
_Hm2LogTempHistTime_Object = MibTableColumn
hm2LogTempHistTime = _Hm2LogTempHistTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 8, 10, 1, 4),
    _Hm2LogTempHistTime_Type()
)
hm2LogTempHistTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LogTempHistTime.setStatus("current")
_Hm2LogAuditGroup_ObjectIdentity = ObjectIdentity
hm2LogAuditGroup = _Hm2LogAuditGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 9)
)


class _Hm2LogAuditTrailComment_Type(DisplayString):
    """Custom type hm2LogAuditTrailComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 80),
    )


_Hm2LogAuditTrailComment_Type.__name__ = "DisplayString"
_Hm2LogAuditTrailComment_Object = MibScalar
hm2LogAuditTrailComment = _Hm2LogAuditTrailComment_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 9, 1),
    _Hm2LogAuditTrailComment_Type()
)
hm2LogAuditTrailComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LogAuditTrailComment.setStatus("current")
_Hm2LogEmailAlertGroup_ObjectIdentity = ObjectIdentity
hm2LogEmailAlertGroup = _Hm2LogEmailAlertGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10)
)


class _Hm2LogEmailAdminStatus_Type(HmEnabledStatus):
    """Custom type hm2LogEmailAdminStatus based on HmEnabledStatus"""


_Hm2LogEmailAdminStatus_Object = MibScalar
hm2LogEmailAdminStatus = _Hm2LogEmailAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 1),
    _Hm2LogEmailAdminStatus_Type()
)
hm2LogEmailAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LogEmailAdminStatus.setStatus("current")


class _Hm2LogEmailFromAddress_Type(SnmpAdminString):
    """Custom type hm2LogEmailFromAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hm2LogEmailFromAddress_Type.__name__ = "SnmpAdminString"
_Hm2LogEmailFromAddress_Object = MibScalar
hm2LogEmailFromAddress = _Hm2LogEmailFromAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 2),
    _Hm2LogEmailFromAddress_Type()
)
hm2LogEmailFromAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LogEmailFromAddress.setStatus("current")


class _Hm2LogEmailLogDuration_Type(Integer32):
    """Custom type hm2LogEmailLogDuration based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1440),
    )


_Hm2LogEmailLogDuration_Type.__name__ = "Integer32"
_Hm2LogEmailLogDuration_Object = MibScalar
hm2LogEmailLogDuration = _Hm2LogEmailLogDuration_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 3),
    _Hm2LogEmailLogDuration_Type()
)
hm2LogEmailLogDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LogEmailLogDuration.setStatus("current")


class _Hm2LogEmailUrgentSeverity_Type(HmAgentLogSeverity):
    """Custom type hm2LogEmailUrgentSeverity based on HmAgentLogSeverity"""


_Hm2LogEmailUrgentSeverity_Object = MibScalar
hm2LogEmailUrgentSeverity = _Hm2LogEmailUrgentSeverity_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 4),
    _Hm2LogEmailUrgentSeverity_Type()
)
hm2LogEmailUrgentSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LogEmailUrgentSeverity.setStatus("current")


class _Hm2LogEmailNonUrgentSeverity_Type(HmAgentLogSeverity):
    """Custom type hm2LogEmailNonUrgentSeverity based on HmAgentLogSeverity"""


_Hm2LogEmailNonUrgentSeverity_Object = MibScalar
hm2LogEmailNonUrgentSeverity = _Hm2LogEmailNonUrgentSeverity_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 5),
    _Hm2LogEmailNonUrgentSeverity_Type()
)
hm2LogEmailNonUrgentSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LogEmailNonUrgentSeverity.setStatus("current")
_Hm2LogEmailNumEmailsSent_Type = Counter32
_Hm2LogEmailNumEmailsSent_Object = MibScalar
hm2LogEmailNumEmailsSent = _Hm2LogEmailNumEmailsSent_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 6),
    _Hm2LogEmailNumEmailsSent_Type()
)
hm2LogEmailNumEmailsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LogEmailNumEmailsSent.setStatus("current")
_Hm2LogEmailNumEmailFailures_Type = Counter32
_Hm2LogEmailNumEmailFailures_Object = MibScalar
hm2LogEmailNumEmailFailures = _Hm2LogEmailNumEmailFailures_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 7),
    _Hm2LogEmailNumEmailFailures_Type()
)
hm2LogEmailNumEmailFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LogEmailNumEmailFailures.setStatus("current")
_Hm2LogEmailTimeOfLastMailSent_Type = HmTimeSeconds1970
_Hm2LogEmailTimeOfLastMailSent_Object = MibScalar
hm2LogEmailTimeOfLastMailSent = _Hm2LogEmailTimeOfLastMailSent_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 8),
    _Hm2LogEmailTimeOfLastMailSent_Type()
)
hm2LogEmailTimeOfLastMailSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LogEmailTimeOfLastMailSent.setStatus("current")


class _Hm2LogEmailAction_Type(Integer32):
    """Custom type hm2LogEmailAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("non-urgent", 3),
          ("other", 1),
          ("test", 2))
    )


_Hm2LogEmailAction_Type.__name__ = "Integer32"
_Hm2LogEmailAction_Object = MibScalar
hm2LogEmailAction = _Hm2LogEmailAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 9),
    _Hm2LogEmailAction_Type()
)
hm2LogEmailAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LogEmailAction.setStatus("current")


class _Hm2LogEmailTestMessageType_Type(Integer32):
    """Custom type hm2LogEmailTestMessageType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-urgent", 2),
          ("urgent", 1))
    )


_Hm2LogEmailTestMessageType_Type.__name__ = "Integer32"
_Hm2LogEmailTestMessageType_Object = MibScalar
hm2LogEmailTestMessageType = _Hm2LogEmailTestMessageType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 10),
    _Hm2LogEmailTestMessageType_Type()
)
hm2LogEmailTestMessageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LogEmailTestMessageType.setStatus("current")


class _Hm2LogEmailTestMessageBody_Type(SnmpAdminString):
    """Custom type hm2LogEmailTestMessageBody based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hm2LogEmailTestMessageBody_Type.__name__ = "SnmpAdminString"
_Hm2LogEmailTestMessageBody_Object = MibScalar
hm2LogEmailTestMessageBody = _Hm2LogEmailTestMessageBody_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 11),
    _Hm2LogEmailTestMessageBody_Type()
)
hm2LogEmailTestMessageBody.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LogEmailTestMessageBody.setStatus("current")
_Hm2LogEmailToAddressTable_Object = MibTable
hm2LogEmailToAddressTable = _Hm2LogEmailToAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 15)
)
if mibBuilder.loadTexts:
    hm2LogEmailToAddressTable.setStatus("current")
_Hm2LogEmailToAddressEntry_Object = MibTableRow
hm2LogEmailToAddressEntry = _Hm2LogEmailToAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 15, 1)
)
hm2LogEmailToAddressEntry.setIndexNames(
    (0, "HM2-LOGGING-MIB", "hm2LogEmailToAddrMessageIndex"),
)
if mibBuilder.loadTexts:
    hm2LogEmailToAddressEntry.setStatus("current")


class _Hm2LogEmailToAddrMessageIndex_Type(Integer32):
    """Custom type hm2LogEmailToAddrMessageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Hm2LogEmailToAddrMessageIndex_Type.__name__ = "Integer32"
_Hm2LogEmailToAddrMessageIndex_Object = MibTableColumn
hm2LogEmailToAddrMessageIndex = _Hm2LogEmailToAddrMessageIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 15, 1, 1),
    _Hm2LogEmailToAddrMessageIndex_Type()
)
hm2LogEmailToAddrMessageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2LogEmailToAddrMessageIndex.setStatus("current")


class _Hm2LogEmailToAddrMessageType_Type(Integer32):
    """Custom type hm2LogEmailToAddrMessageType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-urgent", 2),
          ("urgent", 1))
    )


_Hm2LogEmailToAddrMessageType_Type.__name__ = "Integer32"
_Hm2LogEmailToAddrMessageType_Object = MibTableColumn
hm2LogEmailToAddrMessageType = _Hm2LogEmailToAddrMessageType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 15, 1, 2),
    _Hm2LogEmailToAddrMessageType_Type()
)
hm2LogEmailToAddrMessageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LogEmailToAddrMessageType.setStatus("current")


class _Hm2LogEmailToAddrAddress_Type(SnmpAdminString):
    """Custom type hm2LogEmailToAddrAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hm2LogEmailToAddrAddress_Type.__name__ = "SnmpAdminString"
_Hm2LogEmailToAddrAddress_Object = MibTableColumn
hm2LogEmailToAddrAddress = _Hm2LogEmailToAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 15, 1, 3),
    _Hm2LogEmailToAddrAddress_Type()
)
hm2LogEmailToAddrAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LogEmailToAddrAddress.setStatus("current")
_Hm2LogEmailToAddrEntryStatus_Type = RowStatus
_Hm2LogEmailToAddrEntryStatus_Object = MibTableColumn
hm2LogEmailToAddrEntryStatus = _Hm2LogEmailToAddrEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 15, 1, 4),
    _Hm2LogEmailToAddrEntryStatus_Type()
)
hm2LogEmailToAddrEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LogEmailToAddrEntryStatus.setStatus("current")
_Hm2LogEmailSubjectTable_Object = MibTable
hm2LogEmailSubjectTable = _Hm2LogEmailSubjectTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 16)
)
if mibBuilder.loadTexts:
    hm2LogEmailSubjectTable.setStatus("current")
_Hm2LogEmailSubjectEntry_Object = MibTableRow
hm2LogEmailSubjectEntry = _Hm2LogEmailSubjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 16, 1)
)
hm2LogEmailSubjectEntry.setIndexNames(
    (0, "HM2-LOGGING-MIB", "hm2LogEmailSubjectMessageType"),
)
if mibBuilder.loadTexts:
    hm2LogEmailSubjectEntry.setStatus("current")


class _Hm2LogEmailSubjectMessageType_Type(Integer32):
    """Custom type hm2LogEmailSubjectMessageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-urgent", 2),
          ("urgent", 1))
    )


_Hm2LogEmailSubjectMessageType_Type.__name__ = "Integer32"
_Hm2LogEmailSubjectMessageType_Object = MibTableColumn
hm2LogEmailSubjectMessageType = _Hm2LogEmailSubjectMessageType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 16, 1, 1),
    _Hm2LogEmailSubjectMessageType_Type()
)
hm2LogEmailSubjectMessageType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2LogEmailSubjectMessageType.setStatus("current")


class _Hm2LogEmailSubject_Type(SnmpAdminString):
    """Custom type hm2LogEmailSubject based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hm2LogEmailSubject_Type.__name__ = "SnmpAdminString"
_Hm2LogEmailSubject_Object = MibTableColumn
hm2LogEmailSubject = _Hm2LogEmailSubject_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 16, 1, 2),
    _Hm2LogEmailSubject_Type()
)
hm2LogEmailSubject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LogEmailSubject.setStatus("current")
_Hm2LogEmailSubjectEntryStatus_Type = RowStatus
_Hm2LogEmailSubjectEntryStatus_Object = MibTableColumn
hm2LogEmailSubjectEntryStatus = _Hm2LogEmailSubjectEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 16, 1, 3),
    _Hm2LogEmailSubjectEntryStatus_Type()
)
hm2LogEmailSubjectEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LogEmailSubjectEntryStatus.setStatus("current")
_Hm2LogEmailMailServerTable_Object = MibTable
hm2LogEmailMailServerTable = _Hm2LogEmailMailServerTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 17)
)
if mibBuilder.loadTexts:
    hm2LogEmailMailServerTable.setStatus("current")
_Hm2LogEmailMailServerEntry_Object = MibTableRow
hm2LogEmailMailServerEntry = _Hm2LogEmailMailServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 17, 1)
)
hm2LogEmailMailServerEntry.setIndexNames(
    (0, "HM2-LOGGING-MIB", "hm2LogEmailSmtpAddrIndex"),
)
if mibBuilder.loadTexts:
    hm2LogEmailMailServerEntry.setStatus("current")


class _Hm2LogEmailSmtpAddrIndex_Type(Integer32):
    """Custom type hm2LogEmailSmtpAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Hm2LogEmailSmtpAddrIndex_Type.__name__ = "Integer32"
_Hm2LogEmailSmtpAddrIndex_Object = MibTableColumn
hm2LogEmailSmtpAddrIndex = _Hm2LogEmailSmtpAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 17, 1, 1),
    _Hm2LogEmailSmtpAddrIndex_Type()
)
hm2LogEmailSmtpAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2LogEmailSmtpAddrIndex.setStatus("current")


class _Hm2LogEmailSmtpAddrDescr_Type(SnmpAdminString):
    """Custom type hm2LogEmailSmtpAddrDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hm2LogEmailSmtpAddrDescr_Type.__name__ = "SnmpAdminString"
_Hm2LogEmailSmtpAddrDescr_Object = MibTableColumn
hm2LogEmailSmtpAddrDescr = _Hm2LogEmailSmtpAddrDescr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 17, 1, 2),
    _Hm2LogEmailSmtpAddrDescr_Type()
)
hm2LogEmailSmtpAddrDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LogEmailSmtpAddrDescr.setStatus("current")


class _Hm2LogEmailSmtpAddrType_Type(InetAddressType):
    """Custom type hm2LogEmailSmtpAddrType based on InetAddressType"""


_Hm2LogEmailSmtpAddrType_Object = MibTableColumn
hm2LogEmailSmtpAddrType = _Hm2LogEmailSmtpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 17, 1, 3),
    _Hm2LogEmailSmtpAddrType_Type()
)
hm2LogEmailSmtpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LogEmailSmtpAddrType.setStatus("current")


class _Hm2LogEmailSmtpAddr_Type(InetAddress):
    """Custom type hm2LogEmailSmtpAddr based on InetAddress"""
    defaultHexValue = "00000000"


_Hm2LogEmailSmtpAddr_Object = MibTableColumn
hm2LogEmailSmtpAddr = _Hm2LogEmailSmtpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 17, 1, 4),
    _Hm2LogEmailSmtpAddr_Type()
)
hm2LogEmailSmtpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LogEmailSmtpAddr.setStatus("current")


class _Hm2LogEmailSmtpPort_Type(InetPortNumber):
    """Custom type hm2LogEmailSmtpPort based on InetPortNumber"""
    defaultValue = 25


_Hm2LogEmailSmtpPort_Object = MibTableColumn
hm2LogEmailSmtpPort = _Hm2LogEmailSmtpPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 17, 1, 5),
    _Hm2LogEmailSmtpPort_Type()
)
hm2LogEmailSmtpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LogEmailSmtpPort.setStatus("current")


class _Hm2LogEmailSmtpSecurity_Type(Integer32):
    """Custom type hm2LogEmailSmtpSecurity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("tlsv1", 2))
    )


_Hm2LogEmailSmtpSecurity_Type.__name__ = "Integer32"
_Hm2LogEmailSmtpSecurity_Object = MibTableColumn
hm2LogEmailSmtpSecurity = _Hm2LogEmailSmtpSecurity_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 17, 1, 6),
    _Hm2LogEmailSmtpSecurity_Type()
)
hm2LogEmailSmtpSecurity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LogEmailSmtpSecurity.setStatus("current")


class _Hm2LogEmailSmtpLoginID_Type(SnmpAdminString):
    """Custom type hm2LogEmailSmtpLoginID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hm2LogEmailSmtpLoginID_Type.__name__ = "SnmpAdminString"
_Hm2LogEmailSmtpLoginID_Object = MibTableColumn
hm2LogEmailSmtpLoginID = _Hm2LogEmailSmtpLoginID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 17, 1, 7),
    _Hm2LogEmailSmtpLoginID_Type()
)
hm2LogEmailSmtpLoginID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LogEmailSmtpLoginID.setStatus("current")


class _Hm2LogEmailSmtpPassword_Type(SnmpAdminString):
    """Custom type hm2LogEmailSmtpPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hm2LogEmailSmtpPassword_Type.__name__ = "SnmpAdminString"
_Hm2LogEmailSmtpPassword_Object = MibTableColumn
hm2LogEmailSmtpPassword = _Hm2LogEmailSmtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 17, 1, 8),
    _Hm2LogEmailSmtpPassword_Type()
)
hm2LogEmailSmtpPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LogEmailSmtpPassword.setStatus("current")
_Hm2LogEmailSmtpEntryStatus_Type = RowStatus
_Hm2LogEmailSmtpEntryStatus_Object = MibTableColumn
hm2LogEmailSmtpEntryStatus = _Hm2LogEmailSmtpEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 17, 1, 9),
    _Hm2LogEmailSmtpEntryStatus_Type()
)
hm2LogEmailSmtpEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LogEmailSmtpEntryStatus.setStatus("current")


class _Hm2LogEmailSmtpTimeout_Type(Unsigned32):
    """Custom type hm2LogEmailSmtpTimeout based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Hm2LogEmailSmtpTimeout_Type.__name__ = "Unsigned32"
_Hm2LogEmailSmtpTimeout_Object = MibTableColumn
hm2LogEmailSmtpTimeout = _Hm2LogEmailSmtpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 17, 1, 10),
    _Hm2LogEmailSmtpTimeout_Type()
)
hm2LogEmailSmtpTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LogEmailSmtpTimeout.setStatus("current")


class _Hm2LogEmailClientTlsVersions_Type(Hm2TlsVersions):
    """Custom type hm2LogEmailClientTlsVersions based on Hm2TlsVersions"""
    defaultBinValue = "101"


_Hm2LogEmailClientTlsVersions_Object = MibScalar
hm2LogEmailClientTlsVersions = _Hm2LogEmailClientTlsVersions_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 18),
    _Hm2LogEmailClientTlsVersions_Type()
)
hm2LogEmailClientTlsVersions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LogEmailClientTlsVersions.setStatus("current")


class _Hm2LogEmailClientTlsCipherSuites_Type(Hm2TlsCipherSuites):
    """Custom type hm2LogEmailClientTlsCipherSuites based on Hm2TlsCipherSuites"""
    defaultBinValue = "0010101"


_Hm2LogEmailClientTlsCipherSuites_Object = MibScalar
hm2LogEmailClientTlsCipherSuites = _Hm2LogEmailClientTlsCipherSuites_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 19),
    _Hm2LogEmailClientTlsCipherSuites_Type()
)
hm2LogEmailClientTlsCipherSuites.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LogEmailClientTlsCipherSuites.setStatus("current")

# Managed Objects groups


# Notification objects

hm2LogAuditStartNextSector = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 0, 1)
)
if mibBuilder.loadTexts:
    hm2LogAuditStartNextSector.setStatus(
        "current"
    )

hm2LogEmailSendFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 23, 0, 2)
)
hm2LogEmailSendFailed.setObjects(
    ("HM2-LOGGING-MIB", "hm2LogEmailNumEmailFailures")
)
if mibBuilder.loadTexts:
    hm2LogEmailSendFailed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-LOGGING-MIB",
    **{"HmAgentLogSeverity": HmAgentLogSeverity,
       "hm2LoggingMib": hm2LoggingMib,
       "hm2LoggingMibNotifications": hm2LoggingMibNotifications,
       "hm2LogAuditStartNextSector": hm2LogAuditStartNextSector,
       "hm2LogEmailSendFailed": hm2LogEmailSendFailed,
       "hm2LoggingMibObjects": hm2LoggingMibObjects,
       "hm2LogSnmpLoggingGroup": hm2LogSnmpLoggingGroup,
       "hm2LogSnmpLogGetRequest": hm2LogSnmpLogGetRequest,
       "hm2LogSnmpLogSetRequest": hm2LogSnmpLogSetRequest,
       "hm2LogSnmpLogGetSeverity": hm2LogSnmpLogGetSeverity,
       "hm2LogSnmpLogSetSeverity": hm2LogSnmpLogSetSeverity,
       "hm2LogCliCommandsLoggingGroup": hm2LogCliCommandsLoggingGroup,
       "hm2LogCliCommandsAdminStatus": hm2LogCliCommandsAdminStatus,
       "hm2LogConsoleLoggingGroup": hm2LogConsoleLoggingGroup,
       "hm2LogConsoleAdminStatus": hm2LogConsoleAdminStatus,
       "hm2LogConsoleSeverityFilter": hm2LogConsoleSeverityFilter,
       "hm2LogBufferedLoggingGroup": hm2LogBufferedLoggingGroup,
       "hm2LogBufferdLogLevelThreshold": hm2LogBufferdLogLevelThreshold,
       "hm2LogSyslogGroup": hm2LogSyslogGroup,
       "hm2LogSyslogAdminStatus": hm2LogSyslogAdminStatus,
       "hm2LogSyslogClientTlsVersions": hm2LogSyslogClientTlsVersions,
       "hm2LogSyslogClientTlsCipherSuites": hm2LogSyslogClientTlsCipherSuites,
       "hm2LogSyslogServerTable": hm2LogSyslogServerTable,
       "hm2LogSyslogServerEntry": hm2LogSyslogServerEntry,
       "hm2LogSyslogServerIndex": hm2LogSyslogServerIndex,
       "hm2LogSyslogServerIPAddrType": hm2LogSyslogServerIPAddrType,
       "hm2LogSyslogServerIPAddr": hm2LogSyslogServerIPAddr,
       "hm2LogSyslogServerUdpPort": hm2LogSyslogServerUdpPort,
       "hm2LogSyslogServerLevelUpto": hm2LogSyslogServerLevelUpto,
       "hm2LogSyslogServerLogType": hm2LogSyslogServerLogType,
       "hm2LogSyslogServerRowStatus": hm2LogSyslogServerRowStatus,
       "hm2LogSyslogServerTransportType": hm2LogSyslogServerTransportType,
       "hm2LogPersistentGroup": hm2LogPersistentGroup,
       "hm2LogPersistAdminStatus": hm2LogPersistAdminStatus,
       "hm2LogPersistMaxFileSize": hm2LogPersistMaxFileSize,
       "hm2LogPersistFilesMax": hm2LogPersistFilesMax,
       "hm2LogPersistLevelUpto": hm2LogPersistLevelUpto,
       "hm2LogPersistentFileTable": hm2LogPersistentFileTable,
       "hm2LogPersistentFileEntry": hm2LogPersistentFileEntry,
       "hm2LogPersistentFileIndex": hm2LogPersistentFileIndex,
       "hm2LogPersistentFileName": hm2LogPersistentFileName,
       "hm2LogPersistentFileSize": hm2LogPersistentFileSize,
       "hm2LogCounterGroup": hm2LogCounterGroup,
       "hm2LogCounterOperatingHours": hm2LogCounterOperatingHours,
       "hm2LogCounterFlashTable": hm2LogCounterFlashTable,
       "hm2LogCounterFlashEntry": hm2LogCounterFlashEntry,
       "hm2LogCounterFlashBlock": hm2LogCounterFlashBlock,
       "hm2LogCounterFlashDescription": hm2LogCounterFlashDescription,
       "hm2LogCounterFlashCount": hm2LogCounterFlashCount,
       "hm2LogCounterFlashValue": hm2LogCounterFlashValue,
       "hm2LogTemperatureGroup": hm2LogTemperatureGroup,
       "hm2LogTempMinimum": hm2LogTempMinimum,
       "hm2LogTempMaximum": hm2LogTempMaximum,
       "hm2LogTempVariationCount": hm2LogTempVariationCount,
       "hm2LogTempHistTable": hm2LogTempHistTable,
       "hm2LogTempHistEntry": hm2LogTempHistEntry,
       "hm2LogTempHistIndex": hm2LogTempHistIndex,
       "hm2LogTempHistRangeMin": hm2LogTempHistRangeMin,
       "hm2LogTempHistRangeMax": hm2LogTempHistRangeMax,
       "hm2LogTempHistTime": hm2LogTempHistTime,
       "hm2LogAuditGroup": hm2LogAuditGroup,
       "hm2LogAuditTrailComment": hm2LogAuditTrailComment,
       "hm2LogEmailAlertGroup": hm2LogEmailAlertGroup,
       "hm2LogEmailAdminStatus": hm2LogEmailAdminStatus,
       "hm2LogEmailFromAddress": hm2LogEmailFromAddress,
       "hm2LogEmailLogDuration": hm2LogEmailLogDuration,
       "hm2LogEmailUrgentSeverity": hm2LogEmailUrgentSeverity,
       "hm2LogEmailNonUrgentSeverity": hm2LogEmailNonUrgentSeverity,
       "hm2LogEmailNumEmailsSent": hm2LogEmailNumEmailsSent,
       "hm2LogEmailNumEmailFailures": hm2LogEmailNumEmailFailures,
       "hm2LogEmailTimeOfLastMailSent": hm2LogEmailTimeOfLastMailSent,
       "hm2LogEmailAction": hm2LogEmailAction,
       "hm2LogEmailTestMessageType": hm2LogEmailTestMessageType,
       "hm2LogEmailTestMessageBody": hm2LogEmailTestMessageBody,
       "hm2LogEmailToAddressTable": hm2LogEmailToAddressTable,
       "hm2LogEmailToAddressEntry": hm2LogEmailToAddressEntry,
       "hm2LogEmailToAddrMessageIndex": hm2LogEmailToAddrMessageIndex,
       "hm2LogEmailToAddrMessageType": hm2LogEmailToAddrMessageType,
       "hm2LogEmailToAddrAddress": hm2LogEmailToAddrAddress,
       "hm2LogEmailToAddrEntryStatus": hm2LogEmailToAddrEntryStatus,
       "hm2LogEmailSubjectTable": hm2LogEmailSubjectTable,
       "hm2LogEmailSubjectEntry": hm2LogEmailSubjectEntry,
       "hm2LogEmailSubjectMessageType": hm2LogEmailSubjectMessageType,
       "hm2LogEmailSubject": hm2LogEmailSubject,
       "hm2LogEmailSubjectEntryStatus": hm2LogEmailSubjectEntryStatus,
       "hm2LogEmailMailServerTable": hm2LogEmailMailServerTable,
       "hm2LogEmailMailServerEntry": hm2LogEmailMailServerEntry,
       "hm2LogEmailSmtpAddrIndex": hm2LogEmailSmtpAddrIndex,
       "hm2LogEmailSmtpAddrDescr": hm2LogEmailSmtpAddrDescr,
       "hm2LogEmailSmtpAddrType": hm2LogEmailSmtpAddrType,
       "hm2LogEmailSmtpAddr": hm2LogEmailSmtpAddr,
       "hm2LogEmailSmtpPort": hm2LogEmailSmtpPort,
       "hm2LogEmailSmtpSecurity": hm2LogEmailSmtpSecurity,
       "hm2LogEmailSmtpLoginID": hm2LogEmailSmtpLoginID,
       "hm2LogEmailSmtpPassword": hm2LogEmailSmtpPassword,
       "hm2LogEmailSmtpEntryStatus": hm2LogEmailSmtpEntryStatus,
       "hm2LogEmailSmtpTimeout": hm2LogEmailSmtpTimeout,
       "hm2LogEmailClientTlsVersions": hm2LogEmailClientTlsVersions,
       "hm2LogEmailClientTlsCipherSuites": hm2LogEmailClientTlsCipherSuites}
)
