# SNMP MIB module (CISCO-CDSTV-ISA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CDSTV-ISA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:19 2024
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

(TimeIntervalSec,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "TimeIntervalSec")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoCdstvIsaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 755)
)
ciscoCdstvIsaMIB.setRevisions(
        ("2012-03-13 00:00",
         "2010-08-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoCdstvIsaMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCdstvIsaMIBNotifs = _CiscoCdstvIsaMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 0)
)
_CiscoCdstvIsaMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCdstvIsaMIBObjects = _CiscoCdstvIsaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1)
)
_CdstvISAConfigGeneral_ObjectIdentity = ObjectIdentity
cdstvISAConfigGeneral = _CdstvISAConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 1)
)
_CdstvISAConfigFileName_Type = SnmpAdminString
_CdstvISAConfigFileName_Object = MibScalar
cdstvISAConfigFileName = _CdstvISAConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 1, 1),
    _CdstvISAConfigFileName_Type()
)
cdstvISAConfigFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigFileName.setStatus("current")
_CdstvISAConfigWebServicePort_Type = InetPortNumber
_CdstvISAConfigWebServicePort_Object = MibScalar
cdstvISAConfigWebServicePort = _CdstvISAConfigWebServicePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 1, 2),
    _CdstvISAConfigWebServicePort_Type()
)
cdstvISAConfigWebServicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigWebServicePort.setStatus("current")
_CdstvISAConfigMSAEnabled_Type = TruthValue
_CdstvISAConfigMSAEnabled_Object = MibScalar
cdstvISAConfigMSAEnabled = _CdstvISAConfigMSAEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 1, 3),
    _CdstvISAConfigMSAEnabled_Type()
)
cdstvISAConfigMSAEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigMSAEnabled.setStatus("current")
_CdstvISAConfigTmeEnabled_Type = TruthValue
_CdstvISAConfigTmeEnabled_Object = MibScalar
cdstvISAConfigTmeEnabled = _CdstvISAConfigTmeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 1, 4),
    _CdstvISAConfigTmeEnabled_Type()
)
cdstvISAConfigTmeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigTmeEnabled.setStatus("deprecated")
_CdstvISAConfigLoadQueryInterval_Type = TimeIntervalSec
_CdstvISAConfigLoadQueryInterval_Object = MibScalar
cdstvISAConfigLoadQueryInterval = _CdstvISAConfigLoadQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 1, 5),
    _CdstvISAConfigLoadQueryInterval_Type()
)
cdstvISAConfigLoadQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigLoadQueryInterval.setStatus("current")
_CdstvISAConfigPlayNumThreads_Type = Unsigned32
_CdstvISAConfigPlayNumThreads_Object = MibScalar
cdstvISAConfigPlayNumThreads = _CdstvISAConfigPlayNumThreads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 1, 6),
    _CdstvISAConfigPlayNumThreads_Type()
)
cdstvISAConfigPlayNumThreads.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigPlayNumThreads.setStatus("current")
_CdstvISAConfigResourceMgrServiceName_Type = SnmpAdminString
_CdstvISAConfigResourceMgrServiceName_Object = MibScalar
cdstvISAConfigResourceMgrServiceName = _CdstvISAConfigResourceMgrServiceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 1, 7),
    _CdstvISAConfigResourceMgrServiceName_Type()
)
cdstvISAConfigResourceMgrServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigResourceMgrServiceName.setStatus("current")
_CdstvISAConfigServicePollTime_Type = TimeIntervalSec
_CdstvISAConfigServicePollTime_Object = MibScalar
cdstvISAConfigServicePollTime = _CdstvISAConfigServicePollTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 1, 8),
    _CdstvISAConfigServicePollTime_Type()
)
cdstvISAConfigServicePollTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigServicePollTime.setStatus("current")
_CdstvISAConfigPreEncryptionEnabled_Type = TruthValue
_CdstvISAConfigPreEncryptionEnabled_Object = MibScalar
cdstvISAConfigPreEncryptionEnabled = _CdstvISAConfigPreEncryptionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 1, 9),
    _CdstvISAConfigPreEncryptionEnabled_Type()
)
cdstvISAConfigPreEncryptionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigPreEncryptionEnabled.setStatus("current")
_CdstvISAConfigSessionGatewayTable_Object = MibTable
cdstvISAConfigSessionGatewayTable = _CdstvISAConfigSessionGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 1, 10)
)
if mibBuilder.loadTexts:
    cdstvISAConfigSessionGatewayTable.setStatus("current")
_CdstvISAConfigSessionGatewayEntry_Object = MibTableRow
cdstvISAConfigSessionGatewayEntry = _CdstvISAConfigSessionGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 1, 10, 1)
)
cdstvISAConfigSessionGatewayEntry.setIndexNames(
    (0, "CISCO-CDSTV-ISA-MIB", "cdstvISAConfigSessionGatewayIndex"),
)
if mibBuilder.loadTexts:
    cdstvISAConfigSessionGatewayEntry.setStatus("current")
_CdstvISAConfigSessionGatewayIndex_Type = Unsigned32
_CdstvISAConfigSessionGatewayIndex_Object = MibTableColumn
cdstvISAConfigSessionGatewayIndex = _CdstvISAConfigSessionGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 1, 10, 1, 1),
    _CdstvISAConfigSessionGatewayIndex_Type()
)
cdstvISAConfigSessionGatewayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdstvISAConfigSessionGatewayIndex.setStatus("current")
_CdstvISAConfigSessionGatewayID_Type = SnmpAdminString
_CdstvISAConfigSessionGatewayID_Object = MibTableColumn
cdstvISAConfigSessionGatewayID = _CdstvISAConfigSessionGatewayID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 1, 10, 1, 2),
    _CdstvISAConfigSessionGatewayID_Type()
)
cdstvISAConfigSessionGatewayID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigSessionGatewayID.setStatus("current")


class _CdstvISAConfigTmeStatus_Type(Integer32):
    """Custom type cdstvISAConfigTmeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enableForMystroMDN", 2),
          ("enableForOpenStream", 1))
    )


_CdstvISAConfigTmeStatus_Type.__name__ = "Integer32"
_CdstvISAConfigTmeStatus_Object = MibScalar
cdstvISAConfigTmeStatus = _CdstvISAConfigTmeStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 1, 11),
    _CdstvISAConfigTmeStatus_Type()
)
cdstvISAConfigTmeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigTmeStatus.setStatus("current")
_CdstvISAConfigContentService_ObjectIdentity = ObjectIdentity
cdstvISAConfigContentService = _CdstvISAConfigContentService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 2)
)
_CdstvISAConfigContentServiceMasterIpType_Type = InetAddressType
_CdstvISAConfigContentServiceMasterIpType_Object = MibScalar
cdstvISAConfigContentServiceMasterIpType = _CdstvISAConfigContentServiceMasterIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 2, 1),
    _CdstvISAConfigContentServiceMasterIpType_Type()
)
cdstvISAConfigContentServiceMasterIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigContentServiceMasterIpType.setStatus("current")
_CdstvISAConfigContentServiceMasterIp_Type = InetAddress
_CdstvISAConfigContentServiceMasterIp_Object = MibScalar
cdstvISAConfigContentServiceMasterIp = _CdstvISAConfigContentServiceMasterIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 2, 2),
    _CdstvISAConfigContentServiceMasterIp_Type()
)
cdstvISAConfigContentServiceMasterIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigContentServiceMasterIp.setStatus("current")
_CdstvISAConfigContentServiceMasterPort_Type = InetPortNumber
_CdstvISAConfigContentServiceMasterPort_Object = MibScalar
cdstvISAConfigContentServiceMasterPort = _CdstvISAConfigContentServiceMasterPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 2, 3),
    _CdstvISAConfigContentServiceMasterPort_Type()
)
cdstvISAConfigContentServiceMasterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigContentServiceMasterPort.setStatus("current")
_CdstvISAConfigStreamService_ObjectIdentity = ObjectIdentity
cdstvISAConfigStreamService = _CdstvISAConfigStreamService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 3)
)
_CdstvISAConfigStreamServiceMasterIpType_Type = InetAddressType
_CdstvISAConfigStreamServiceMasterIpType_Object = MibScalar
cdstvISAConfigStreamServiceMasterIpType = _CdstvISAConfigStreamServiceMasterIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 3, 1),
    _CdstvISAConfigStreamServiceMasterIpType_Type()
)
cdstvISAConfigStreamServiceMasterIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigStreamServiceMasterIpType.setStatus("current")
_CdstvISAConfigStreamServiceMasterIp_Type = InetAddress
_CdstvISAConfigStreamServiceMasterIp_Object = MibScalar
cdstvISAConfigStreamServiceMasterIp = _CdstvISAConfigStreamServiceMasterIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 3, 2),
    _CdstvISAConfigStreamServiceMasterIp_Type()
)
cdstvISAConfigStreamServiceMasterIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigStreamServiceMasterIp.setStatus("current")
_CdstvISAConfigStreamServiceMasterPort_Type = InetPortNumber
_CdstvISAConfigStreamServiceMasterPort_Object = MibScalar
cdstvISAConfigStreamServiceMasterPort = _CdstvISAConfigStreamServiceMasterPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 3, 3),
    _CdstvISAConfigStreamServiceMasterPort_Type()
)
cdstvISAConfigStreamServiceMasterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigStreamServiceMasterPort.setStatus("current")
_CdstvISAConfigStreamServiceId_Type = SnmpAdminString
_CdstvISAConfigStreamServiceId_Object = MibScalar
cdstvISAConfigStreamServiceId = _CdstvISAConfigStreamServiceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 3, 4),
    _CdstvISAConfigStreamServiceId_Type()
)
cdstvISAConfigStreamServiceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigStreamServiceId.setStatus("current")
_CdstvISAConfigStreamServiceKind_Type = SnmpAdminString
_CdstvISAConfigStreamServiceKind_Object = MibScalar
cdstvISAConfigStreamServiceKind = _CdstvISAConfigStreamServiceKind_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 3, 5),
    _CdstvISAConfigStreamServiceKind_Type()
)
cdstvISAConfigStreamServiceKind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigStreamServiceKind.setStatus("current")
_CdstvISAConfigMasterNumThreads_Type = Unsigned32
_CdstvISAConfigMasterNumThreads_Object = MibScalar
cdstvISAConfigMasterNumThreads = _CdstvISAConfigMasterNumThreads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 3, 6),
    _CdstvISAConfigMasterNumThreads_Type()
)
cdstvISAConfigMasterNumThreads.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigMasterNumThreads.setStatus("current")


class _CdstvISAConfigStreamSourceIPConfig_Type(Integer32):
    """Custom type cdstvISAConfigStreamSourceIPConfig based on Integer32"""
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
        *(("controlIp", 2),
          ("defaultStreamSourceIp", 3),
          ("none", 1),
          ("streamInterfaceIp", 4))
    )


_CdstvISAConfigStreamSourceIPConfig_Type.__name__ = "Integer32"
_CdstvISAConfigStreamSourceIPConfig_Object = MibScalar
cdstvISAConfigStreamSourceIPConfig = _CdstvISAConfigStreamSourceIPConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 3, 7),
    _CdstvISAConfigStreamSourceIPConfig_Type()
)
cdstvISAConfigStreamSourceIPConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigStreamSourceIPConfig.setStatus("current")
_CdstvISAConfigStreamSourcePort_Type = InetPortNumber
_CdstvISAConfigStreamSourcePort_Object = MibScalar
cdstvISAConfigStreamSourcePort = _CdstvISAConfigStreamSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 3, 8),
    _CdstvISAConfigStreamSourcePort_Type()
)
cdstvISAConfigStreamSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigStreamSourcePort.setStatus("current")


class _CdstvISAConfigStreamingMode_Type(Integer32):
    """Custom type cdstvISAConfigStreamingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asi", 1),
          ("gige", 2))
    )


_CdstvISAConfigStreamingMode_Type.__name__ = "Integer32"
_CdstvISAConfigStreamingMode_Object = MibScalar
cdstvISAConfigStreamingMode = _CdstvISAConfigStreamingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 3, 9),
    _CdstvISAConfigStreamingMode_Type()
)
cdstvISAConfigStreamingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigStreamingMode.setStatus("current")
_CdstvISAConfigStreamHeadendIdType_Type = InetAddressType
_CdstvISAConfigStreamHeadendIdType_Object = MibScalar
cdstvISAConfigStreamHeadendIdType = _CdstvISAConfigStreamHeadendIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 3, 10),
    _CdstvISAConfigStreamHeadendIdType_Type()
)
cdstvISAConfigStreamHeadendIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigStreamHeadendIdType.setStatus("current")
_CdstvISAConfigStreamHeadendId_Type = InetAddress
_CdstvISAConfigStreamHeadendId_Object = MibScalar
cdstvISAConfigStreamHeadendId = _CdstvISAConfigStreamHeadendId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 3, 11),
    _CdstvISAConfigStreamHeadendId_Type()
)
cdstvISAConfigStreamHeadendId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigStreamHeadendId.setStatus("current")
_CdstvISAConfigStreamTimeout_Type = TimeIntervalSec
_CdstvISAConfigStreamTimeout_Object = MibScalar
cdstvISAConfigStreamTimeout = _CdstvISAConfigStreamTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 3, 12),
    _CdstvISAConfigStreamTimeout_Type()
)
cdstvISAConfigStreamTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigStreamTimeout.setStatus("current")
_CdstvISAConfigNamingService_ObjectIdentity = ObjectIdentity
cdstvISAConfigNamingService = _CdstvISAConfigNamingService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 4)
)
_CdstvISAConfigNamingServiceIpType_Type = InetAddressType
_CdstvISAConfigNamingServiceIpType_Object = MibScalar
cdstvISAConfigNamingServiceIpType = _CdstvISAConfigNamingServiceIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 4, 1),
    _CdstvISAConfigNamingServiceIpType_Type()
)
cdstvISAConfigNamingServiceIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigNamingServiceIpType.setStatus("current")
_CdstvISAConfigNamingServiceIp_Type = InetAddress
_CdstvISAConfigNamingServiceIp_Object = MibScalar
cdstvISAConfigNamingServiceIp = _CdstvISAConfigNamingServiceIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 4, 2),
    _CdstvISAConfigNamingServiceIp_Type()
)
cdstvISAConfigNamingServiceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigNamingServiceIp.setStatus("current")
_CdstvISAConfigNamingServicePort_Type = InetPortNumber
_CdstvISAConfigNamingServicePort_Object = MibScalar
cdstvISAConfigNamingServicePort = _CdstvISAConfigNamingServicePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 4, 3),
    _CdstvISAConfigNamingServicePort_Type()
)
cdstvISAConfigNamingServicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigNamingServicePort.setStatus("current")
_CdstvISAConfigNotifyService_ObjectIdentity = ObjectIdentity
cdstvISAConfigNotifyService = _CdstvISAConfigNotifyService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 5)
)
_CdstvISAConfigNotifyServiceIpType_Type = InetAddressType
_CdstvISAConfigNotifyServiceIpType_Object = MibScalar
cdstvISAConfigNotifyServiceIpType = _CdstvISAConfigNotifyServiceIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 5, 1),
    _CdstvISAConfigNotifyServiceIpType_Type()
)
cdstvISAConfigNotifyServiceIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigNotifyServiceIpType.setStatus("current")
_CdstvISAConfigNotifyServiceIp_Type = InetAddress
_CdstvISAConfigNotifyServiceIp_Object = MibScalar
cdstvISAConfigNotifyServiceIp = _CdstvISAConfigNotifyServiceIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 5, 2),
    _CdstvISAConfigNotifyServiceIp_Type()
)
cdstvISAConfigNotifyServiceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigNotifyServiceIp.setStatus("current")
_CdstvISAConfigNotifyServicePort_Type = InetPortNumber
_CdstvISAConfigNotifyServicePort_Object = MibScalar
cdstvISAConfigNotifyServicePort = _CdstvISAConfigNotifyServicePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 5, 3),
    _CdstvISAConfigNotifyServicePort_Type()
)
cdstvISAConfigNotifyServicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigNotifyServicePort.setStatus("current")
_CdstvISAConfigNotifyServiceFactory_Type = SnmpAdminString
_CdstvISAConfigNotifyServiceFactory_Object = MibScalar
cdstvISAConfigNotifyServiceFactory = _CdstvISAConfigNotifyServiceFactory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 5, 4),
    _CdstvISAConfigNotifyServiceFactory_Type()
)
cdstvISAConfigNotifyServiceFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigNotifyServiceFactory.setStatus("current")
_CdstvISAConfigContentStore_ObjectIdentity = ObjectIdentity
cdstvISAConfigContentStore = _CdstvISAConfigContentStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 6)
)
_CdstvISAConfigContentStoreName_Type = SnmpAdminString
_CdstvISAConfigContentStoreName_Object = MibScalar
cdstvISAConfigContentStoreName = _CdstvISAConfigContentStoreName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 6, 1),
    _CdstvISAConfigContentStoreName_Type()
)
cdstvISAConfigContentStoreName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigContentStoreName.setStatus("current")
_CdstvISAConfigContentStoreKind_Type = SnmpAdminString
_CdstvISAConfigContentStoreKind_Object = MibScalar
cdstvISAConfigContentStoreKind = _CdstvISAConfigContentStoreKind_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 6, 2),
    _CdstvISAConfigContentStoreKind_Type()
)
cdstvISAConfigContentStoreKind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigContentStoreKind.setStatus("current")
_CdstvISAConfigContentNumThreads_Type = Unsigned32
_CdstvISAConfigContentNumThreads_Object = MibScalar
cdstvISAConfigContentNumThreads = _CdstvISAConfigContentNumThreads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 6, 3),
    _CdstvISAConfigContentNumThreads_Type()
)
cdstvISAConfigContentNumThreads.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigContentNumThreads.setStatus("current")
_CdstvISAConfigFactory_ObjectIdentity = ObjectIdentity
cdstvISAConfigFactory = _CdstvISAConfigFactory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 7)
)
_CdstvISAConfigFactoryId_Type = SnmpAdminString
_CdstvISAConfigFactoryId_Object = MibScalar
cdstvISAConfigFactoryId = _CdstvISAConfigFactoryId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 7, 1),
    _CdstvISAConfigFactoryId_Type()
)
cdstvISAConfigFactoryId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigFactoryId.setStatus("current")
_CdstvISAConfigFactoryKind_Type = SnmpAdminString
_CdstvISAConfigFactoryKind_Object = MibScalar
cdstvISAConfigFactoryKind = _CdstvISAConfigFactoryKind_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 7, 2),
    _CdstvISAConfigFactoryKind_Type()
)
cdstvISAConfigFactoryKind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigFactoryKind.setStatus("current")
_CdstvISAConfigContentFactory_ObjectIdentity = ObjectIdentity
cdstvISAConfigContentFactory = _CdstvISAConfigContentFactory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 8)
)
_CdstvISAConfigContentFactoryId_Type = SnmpAdminString
_CdstvISAConfigContentFactoryId_Object = MibScalar
cdstvISAConfigContentFactoryId = _CdstvISAConfigContentFactoryId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 8, 1),
    _CdstvISAConfigContentFactoryId_Type()
)
cdstvISAConfigContentFactoryId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigContentFactoryId.setStatus("current")
_CdstvISAConfigContentFactoryKind_Type = SnmpAdminString
_CdstvISAConfigContentFactoryKind_Object = MibScalar
cdstvISAConfigContentFactoryKind = _CdstvISAConfigContentFactoryKind_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 8, 2),
    _CdstvISAConfigContentFactoryKind_Type()
)
cdstvISAConfigContentFactoryKind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigContentFactoryKind.setStatus("current")
_CdstvISAConfigContentChannel_ObjectIdentity = ObjectIdentity
cdstvISAConfigContentChannel = _CdstvISAConfigContentChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 9)
)
_CdstvISAConfigContentChannelId_Type = SnmpAdminString
_CdstvISAConfigContentChannelId_Object = MibScalar
cdstvISAConfigContentChannelId = _CdstvISAConfigContentChannelId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 9, 1),
    _CdstvISAConfigContentChannelId_Type()
)
cdstvISAConfigContentChannelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigContentChannelId.setStatus("current")
_CdstvISAConfigContentChannelKind_Type = SnmpAdminString
_CdstvISAConfigContentChannelKind_Object = MibScalar
cdstvISAConfigContentChannelKind = _CdstvISAConfigContentChannelKind_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 9, 2),
    _CdstvISAConfigContentChannelKind_Type()
)
cdstvISAConfigContentChannelKind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigContentChannelKind.setStatus("current")
_CdstvISAConfigStreamChannel_ObjectIdentity = ObjectIdentity
cdstvISAConfigStreamChannel = _CdstvISAConfigStreamChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 10)
)
_CdstvISAConfigStreamChannelId_Type = SnmpAdminString
_CdstvISAConfigStreamChannelId_Object = MibScalar
cdstvISAConfigStreamChannelId = _CdstvISAConfigStreamChannelId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 10, 1),
    _CdstvISAConfigStreamChannelId_Type()
)
cdstvISAConfigStreamChannelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigStreamChannelId.setStatus("current")
_CdstvISAConfigStreamChannelKind_Type = SnmpAdminString
_CdstvISAConfigStreamChannelKind_Object = MibScalar
cdstvISAConfigStreamChannelKind = _CdstvISAConfigStreamChannelKind_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 10, 2),
    _CdstvISAConfigStreamChannelKind_Type()
)
cdstvISAConfigStreamChannelKind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigStreamChannelKind.setStatus("current")
_CdstvISAConfigEventChannel_ObjectIdentity = ObjectIdentity
cdstvISAConfigEventChannel = _CdstvISAConfigEventChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 11)
)
_CdstvISAConfigEventChannelId_Type = SnmpAdminString
_CdstvISAConfigEventChannelId_Object = MibScalar
cdstvISAConfigEventChannelId = _CdstvISAConfigEventChannelId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 11, 1),
    _CdstvISAConfigEventChannelId_Type()
)
cdstvISAConfigEventChannelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigEventChannelId.setStatus("current")
_CdstvISAConfigEventChannelKind_Type = SnmpAdminString
_CdstvISAConfigEventChannelKind_Object = MibScalar
cdstvISAConfigEventChannelKind = _CdstvISAConfigEventChannelKind_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 11, 2),
    _CdstvISAConfigEventChannelKind_Type()
)
cdstvISAConfigEventChannelKind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigEventChannelKind.setStatus("current")
_CdstvISAConfigEventChannelFactory_Type = SnmpAdminString
_CdstvISAConfigEventChannelFactory_Object = MibScalar
cdstvISAConfigEventChannelFactory = _CdstvISAConfigEventChannelFactory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 11, 3),
    _CdstvISAConfigEventChannelFactory_Type()
)
cdstvISAConfigEventChannelFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigEventChannelFactory.setStatus("current")
_CdstvISAConfigFTP_ObjectIdentity = ObjectIdentity
cdstvISAConfigFTP = _CdstvISAConfigFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 12)
)
_CdstvISAConfigFTPClientPort_Type = InetPortNumber
_CdstvISAConfigFTPClientPort_Object = MibScalar
cdstvISAConfigFTPClientPort = _CdstvISAConfigFTPClientPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 12, 1),
    _CdstvISAConfigFTPClientPort_Type()
)
cdstvISAConfigFTPClientPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigFTPClientPort.setStatus("current")
_CdstvISAConfigFTPServerPort_Type = InetPortNumber
_CdstvISAConfigFTPServerPort_Object = MibScalar
cdstvISAConfigFTPServerPort = _CdstvISAConfigFTPServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 12, 2),
    _CdstvISAConfigFTPServerPort_Type()
)
cdstvISAConfigFTPServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigFTPServerPort.setStatus("current")
_CdstvISAConfigFTPServerOutPort_Type = InetPortNumber
_CdstvISAConfigFTPServerOutPort_Object = MibScalar
cdstvISAConfigFTPServerOutPort = _CdstvISAConfigFTPServerOutPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 12, 3),
    _CdstvISAConfigFTPServerOutPort_Type()
)
cdstvISAConfigFTPServerOutPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigFTPServerOutPort.setStatus("current")
_CdstvISAConfigFTPClientNumAttempts_Type = Unsigned32
_CdstvISAConfigFTPClientNumAttempts_Object = MibScalar
cdstvISAConfigFTPClientNumAttempts = _CdstvISAConfigFTPClientNumAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 12, 4),
    _CdstvISAConfigFTPClientNumAttempts_Type()
)
cdstvISAConfigFTPClientNumAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigFTPClientNumAttempts.setStatus("current")
_CdstvISAConfigFTPPollTimeout_Type = TimeIntervalSec
_CdstvISAConfigFTPPollTimeout_Object = MibScalar
cdstvISAConfigFTPPollTimeout = _CdstvISAConfigFTPPollTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 12, 5),
    _CdstvISAConfigFTPPollTimeout_Type()
)
cdstvISAConfigFTPPollTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigFTPPollTimeout.setStatus("current")
_CdstvISAConfigLSCP_ObjectIdentity = ObjectIdentity
cdstvISAConfigLSCP = _CdstvISAConfigLSCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 13)
)
_CdstvISAConfigLscpServerPort_Type = InetPortNumber
_CdstvISAConfigLscpServerPort_Object = MibScalar
cdstvISAConfigLscpServerPort = _CdstvISAConfigLscpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 13, 1),
    _CdstvISAConfigLscpServerPort_Type()
)
cdstvISAConfigLscpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigLscpServerPort.setStatus("current")
_CdstvISAConfigLscpResponsePadding_Type = TruthValue
_CdstvISAConfigLscpResponsePadding_Object = MibScalar
cdstvISAConfigLscpResponsePadding = _CdstvISAConfigLscpResponsePadding_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 13, 2),
    _CdstvISAConfigLscpResponsePadding_Type()
)
cdstvISAConfigLscpResponsePadding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigLscpResponsePadding.setStatus("current")


class _CdstvISAConfigfMsaLscpClientProto_Type(Integer32):
    """Custom type cdstvISAConfigfMsaLscpClientProto based on Integer32"""
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
        *(("cisco", 5),
          ("cv", 4),
          ("lscppauseateos", 7),
          ("rti", 2),
          ("ttv", 6),
          ("tvguide", 1),
          ("vodlink", 3))
    )


_CdstvISAConfigfMsaLscpClientProto_Type.__name__ = "Integer32"
_CdstvISAConfigfMsaLscpClientProto_Object = MibScalar
cdstvISAConfigfMsaLscpClientProto = _CdstvISAConfigfMsaLscpClientProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 1, 13, 3),
    _CdstvISAConfigfMsaLscpClientProto_Type()
)
cdstvISAConfigfMsaLscpClientProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvISAConfigfMsaLscpClientProto.setStatus("current")
_CiscoCdstvIsaMIBConform_ObjectIdentity = ObjectIdentity
ciscoCdstvIsaMIBConform = _CiscoCdstvIsaMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 2)
)
_CiscoCdstvIsaMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCdstvIsaMIBCompliances = _CiscoCdstvIsaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 2, 1)
)
_CiscoCdstvIsaMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCdstvIsaMIBGroups = _CiscoCdstvIsaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 2, 2)
)

# Managed Objects groups

ciscoCdstvIsaGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 2, 2, 1)
)
ciscoCdstvIsaGeneralGroup.setObjects(
      *(("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigFileName"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigWebServicePort"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigMSAEnabled"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigTmeEnabled"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigLoadQueryInterval"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigPlayNumThreads"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigResourceMgrServiceName"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigServicePollTime"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigPreEncryptionEnabled"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigSessionGatewayID"))
)
if mibBuilder.loadTexts:
    ciscoCdstvIsaGeneralGroup.setStatus("deprecated")

ciscoCdstvIsaContentServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 2, 2, 2)
)
ciscoCdstvIsaContentServiceGroup.setObjects(
      *(("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigContentServiceMasterIpType"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigContentServiceMasterIp"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigContentServiceMasterPort"))
)
if mibBuilder.loadTexts:
    ciscoCdstvIsaContentServiceGroup.setStatus("current")

ciscoCdstvIsaStreamServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 2, 2, 3)
)
ciscoCdstvIsaStreamServiceGroup.setObjects(
      *(("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigStreamServiceMasterIpType"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigStreamServiceMasterIp"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigStreamServiceMasterPort"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigStreamServiceId"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigStreamServiceKind"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigMasterNumThreads"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigStreamSourceIPConfig"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigStreamSourcePort"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigStreamingMode"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigStreamHeadendIdType"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigStreamHeadendId"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigStreamTimeout"))
)
if mibBuilder.loadTexts:
    ciscoCdstvIsaStreamServiceGroup.setStatus("current")

ciscoCdstvIsaNamingServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 2, 2, 4)
)
ciscoCdstvIsaNamingServiceGroup.setObjects(
      *(("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigNamingServiceIpType"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigNamingServiceIp"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigNamingServicePort"))
)
if mibBuilder.loadTexts:
    ciscoCdstvIsaNamingServiceGroup.setStatus("current")

ciscoCdstvIsaNotifyServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 2, 2, 5)
)
ciscoCdstvIsaNotifyServiceGroup.setObjects(
      *(("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigNotifyServiceIpType"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigNotifyServiceIp"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigNotifyServicePort"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigNotifyServiceFactory"))
)
if mibBuilder.loadTexts:
    ciscoCdstvIsaNotifyServiceGroup.setStatus("current")

ciscoCdstvIsaContentStoreGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 2, 2, 6)
)
ciscoCdstvIsaContentStoreGroup.setObjects(
      *(("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigContentStoreName"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigContentStoreKind"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigContentNumThreads"))
)
if mibBuilder.loadTexts:
    ciscoCdstvIsaContentStoreGroup.setStatus("current")

ciscoCdstvIsaFactoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 2, 2, 7)
)
ciscoCdstvIsaFactoryGroup.setObjects(
      *(("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigFactoryId"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigFactoryKind"))
)
if mibBuilder.loadTexts:
    ciscoCdstvIsaFactoryGroup.setStatus("current")

ciscoCdstvIsaContentFactoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 2, 2, 8)
)
ciscoCdstvIsaContentFactoryGroup.setObjects(
      *(("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigContentFactoryId"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigContentFactoryKind"))
)
if mibBuilder.loadTexts:
    ciscoCdstvIsaContentFactoryGroup.setStatus("current")

ciscoCdstvIsaContentChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 2, 2, 9)
)
ciscoCdstvIsaContentChannelGroup.setObjects(
      *(("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigContentChannelId"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigContentChannelKind"))
)
if mibBuilder.loadTexts:
    ciscoCdstvIsaContentChannelGroup.setStatus("current")

ciscoCdstvIsaStreamChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 2, 2, 10)
)
ciscoCdstvIsaStreamChannelGroup.setObjects(
      *(("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigStreamChannelId"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigStreamChannelKind"))
)
if mibBuilder.loadTexts:
    ciscoCdstvIsaStreamChannelGroup.setStatus("current")

ciscoCdstvIsaEventChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 2, 2, 11)
)
ciscoCdstvIsaEventChannelGroup.setObjects(
      *(("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigEventChannelId"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigEventChannelKind"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigEventChannelFactory"))
)
if mibBuilder.loadTexts:
    ciscoCdstvIsaEventChannelGroup.setStatus("current")

ciscoCdstvIsaFtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 2, 2, 12)
)
ciscoCdstvIsaFtpGroup.setObjects(
      *(("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigFTPClientPort"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigFTPServerPort"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigFTPServerOutPort"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigFTPClientNumAttempts"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigFTPPollTimeout"))
)
if mibBuilder.loadTexts:
    ciscoCdstvIsaFtpGroup.setStatus("current")

ciscoCdstvIsaLscpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 2, 2, 13)
)
ciscoCdstvIsaLscpGroup.setObjects(
      *(("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigLscpServerPort"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigLscpResponsePadding"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigfMsaLscpClientProto"))
)
if mibBuilder.loadTexts:
    ciscoCdstvIsaLscpGroup.setStatus("current")

ciscoCdstvIsaGeneralGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 2, 2, 14)
)
ciscoCdstvIsaGeneralGroup2.setObjects(
      *(("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigFileName"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigWebServicePort"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigMSAEnabled"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigLoadQueryInterval"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigPlayNumThreads"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigResourceMgrServiceName"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigServicePollTime"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigPreEncryptionEnabled"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigSessionGatewayID"),
        ("CISCO-CDSTV-ISA-MIB", "cdstvISAConfigTmeStatus"))
)
if mibBuilder.loadTexts:
    ciscoCdstvIsaGeneralGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCdstvIsaMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCdstvIsaMIBCompliance.setStatus(
        "deprecated"
    )

ciscoCdstvIsaMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 755, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoCdstvIsaMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CDSTV-ISA-MIB",
    **{"ciscoCdstvIsaMIB": ciscoCdstvIsaMIB,
       "ciscoCdstvIsaMIBNotifs": ciscoCdstvIsaMIBNotifs,
       "ciscoCdstvIsaMIBObjects": ciscoCdstvIsaMIBObjects,
       "cdstvISAConfigGeneral": cdstvISAConfigGeneral,
       "cdstvISAConfigFileName": cdstvISAConfigFileName,
       "cdstvISAConfigWebServicePort": cdstvISAConfigWebServicePort,
       "cdstvISAConfigMSAEnabled": cdstvISAConfigMSAEnabled,
       "cdstvISAConfigTmeEnabled": cdstvISAConfigTmeEnabled,
       "cdstvISAConfigLoadQueryInterval": cdstvISAConfigLoadQueryInterval,
       "cdstvISAConfigPlayNumThreads": cdstvISAConfigPlayNumThreads,
       "cdstvISAConfigResourceMgrServiceName": cdstvISAConfigResourceMgrServiceName,
       "cdstvISAConfigServicePollTime": cdstvISAConfigServicePollTime,
       "cdstvISAConfigPreEncryptionEnabled": cdstvISAConfigPreEncryptionEnabled,
       "cdstvISAConfigSessionGatewayTable": cdstvISAConfigSessionGatewayTable,
       "cdstvISAConfigSessionGatewayEntry": cdstvISAConfigSessionGatewayEntry,
       "cdstvISAConfigSessionGatewayIndex": cdstvISAConfigSessionGatewayIndex,
       "cdstvISAConfigSessionGatewayID": cdstvISAConfigSessionGatewayID,
       "cdstvISAConfigTmeStatus": cdstvISAConfigTmeStatus,
       "cdstvISAConfigContentService": cdstvISAConfigContentService,
       "cdstvISAConfigContentServiceMasterIpType": cdstvISAConfigContentServiceMasterIpType,
       "cdstvISAConfigContentServiceMasterIp": cdstvISAConfigContentServiceMasterIp,
       "cdstvISAConfigContentServiceMasterPort": cdstvISAConfigContentServiceMasterPort,
       "cdstvISAConfigStreamService": cdstvISAConfigStreamService,
       "cdstvISAConfigStreamServiceMasterIpType": cdstvISAConfigStreamServiceMasterIpType,
       "cdstvISAConfigStreamServiceMasterIp": cdstvISAConfigStreamServiceMasterIp,
       "cdstvISAConfigStreamServiceMasterPort": cdstvISAConfigStreamServiceMasterPort,
       "cdstvISAConfigStreamServiceId": cdstvISAConfigStreamServiceId,
       "cdstvISAConfigStreamServiceKind": cdstvISAConfigStreamServiceKind,
       "cdstvISAConfigMasterNumThreads": cdstvISAConfigMasterNumThreads,
       "cdstvISAConfigStreamSourceIPConfig": cdstvISAConfigStreamSourceIPConfig,
       "cdstvISAConfigStreamSourcePort": cdstvISAConfigStreamSourcePort,
       "cdstvISAConfigStreamingMode": cdstvISAConfigStreamingMode,
       "cdstvISAConfigStreamHeadendIdType": cdstvISAConfigStreamHeadendIdType,
       "cdstvISAConfigStreamHeadendId": cdstvISAConfigStreamHeadendId,
       "cdstvISAConfigStreamTimeout": cdstvISAConfigStreamTimeout,
       "cdstvISAConfigNamingService": cdstvISAConfigNamingService,
       "cdstvISAConfigNamingServiceIpType": cdstvISAConfigNamingServiceIpType,
       "cdstvISAConfigNamingServiceIp": cdstvISAConfigNamingServiceIp,
       "cdstvISAConfigNamingServicePort": cdstvISAConfigNamingServicePort,
       "cdstvISAConfigNotifyService": cdstvISAConfigNotifyService,
       "cdstvISAConfigNotifyServiceIpType": cdstvISAConfigNotifyServiceIpType,
       "cdstvISAConfigNotifyServiceIp": cdstvISAConfigNotifyServiceIp,
       "cdstvISAConfigNotifyServicePort": cdstvISAConfigNotifyServicePort,
       "cdstvISAConfigNotifyServiceFactory": cdstvISAConfigNotifyServiceFactory,
       "cdstvISAConfigContentStore": cdstvISAConfigContentStore,
       "cdstvISAConfigContentStoreName": cdstvISAConfigContentStoreName,
       "cdstvISAConfigContentStoreKind": cdstvISAConfigContentStoreKind,
       "cdstvISAConfigContentNumThreads": cdstvISAConfigContentNumThreads,
       "cdstvISAConfigFactory": cdstvISAConfigFactory,
       "cdstvISAConfigFactoryId": cdstvISAConfigFactoryId,
       "cdstvISAConfigFactoryKind": cdstvISAConfigFactoryKind,
       "cdstvISAConfigContentFactory": cdstvISAConfigContentFactory,
       "cdstvISAConfigContentFactoryId": cdstvISAConfigContentFactoryId,
       "cdstvISAConfigContentFactoryKind": cdstvISAConfigContentFactoryKind,
       "cdstvISAConfigContentChannel": cdstvISAConfigContentChannel,
       "cdstvISAConfigContentChannelId": cdstvISAConfigContentChannelId,
       "cdstvISAConfigContentChannelKind": cdstvISAConfigContentChannelKind,
       "cdstvISAConfigStreamChannel": cdstvISAConfigStreamChannel,
       "cdstvISAConfigStreamChannelId": cdstvISAConfigStreamChannelId,
       "cdstvISAConfigStreamChannelKind": cdstvISAConfigStreamChannelKind,
       "cdstvISAConfigEventChannel": cdstvISAConfigEventChannel,
       "cdstvISAConfigEventChannelId": cdstvISAConfigEventChannelId,
       "cdstvISAConfigEventChannelKind": cdstvISAConfigEventChannelKind,
       "cdstvISAConfigEventChannelFactory": cdstvISAConfigEventChannelFactory,
       "cdstvISAConfigFTP": cdstvISAConfigFTP,
       "cdstvISAConfigFTPClientPort": cdstvISAConfigFTPClientPort,
       "cdstvISAConfigFTPServerPort": cdstvISAConfigFTPServerPort,
       "cdstvISAConfigFTPServerOutPort": cdstvISAConfigFTPServerOutPort,
       "cdstvISAConfigFTPClientNumAttempts": cdstvISAConfigFTPClientNumAttempts,
       "cdstvISAConfigFTPPollTimeout": cdstvISAConfigFTPPollTimeout,
       "cdstvISAConfigLSCP": cdstvISAConfigLSCP,
       "cdstvISAConfigLscpServerPort": cdstvISAConfigLscpServerPort,
       "cdstvISAConfigLscpResponsePadding": cdstvISAConfigLscpResponsePadding,
       "cdstvISAConfigfMsaLscpClientProto": cdstvISAConfigfMsaLscpClientProto,
       "ciscoCdstvIsaMIBConform": ciscoCdstvIsaMIBConform,
       "ciscoCdstvIsaMIBCompliances": ciscoCdstvIsaMIBCompliances,
       "ciscoCdstvIsaMIBCompliance": ciscoCdstvIsaMIBCompliance,
       "ciscoCdstvIsaMIBCompliance2": ciscoCdstvIsaMIBCompliance2,
       "ciscoCdstvIsaMIBGroups": ciscoCdstvIsaMIBGroups,
       "ciscoCdstvIsaGeneralGroup": ciscoCdstvIsaGeneralGroup,
       "ciscoCdstvIsaContentServiceGroup": ciscoCdstvIsaContentServiceGroup,
       "ciscoCdstvIsaStreamServiceGroup": ciscoCdstvIsaStreamServiceGroup,
       "ciscoCdstvIsaNamingServiceGroup": ciscoCdstvIsaNamingServiceGroup,
       "ciscoCdstvIsaNotifyServiceGroup": ciscoCdstvIsaNotifyServiceGroup,
       "ciscoCdstvIsaContentStoreGroup": ciscoCdstvIsaContentStoreGroup,
       "ciscoCdstvIsaFactoryGroup": ciscoCdstvIsaFactoryGroup,
       "ciscoCdstvIsaContentFactoryGroup": ciscoCdstvIsaContentFactoryGroup,
       "ciscoCdstvIsaContentChannelGroup": ciscoCdstvIsaContentChannelGroup,
       "ciscoCdstvIsaStreamChannelGroup": ciscoCdstvIsaStreamChannelGroup,
       "ciscoCdstvIsaEventChannelGroup": ciscoCdstvIsaEventChannelGroup,
       "ciscoCdstvIsaFtpGroup": ciscoCdstvIsaFtpGroup,
       "ciscoCdstvIsaLscpGroup": ciscoCdstvIsaLscpGroup,
       "ciscoCdstvIsaGeneralGroup2": ciscoCdstvIsaGeneralGroup2}
)
