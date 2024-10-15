# SNMP MIB module (CISCO-SLB-HEALTH-MON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SLB-HEALTH-MON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:26 2024
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

(SlbFunctionNameString,
 SlbUrlString,
 cslbxServerProbes) = mibBuilder.importSymbols(
    "CISCO-SLB-EXT-MIB",
    "SlbFunctionNameString",
    "SlbUrlString",
    "cslbxServerProbes")

(SlbServerString,
 slbEntity,
 slbServerFarmName) = mibBuilder.importSymbols(
    "CISCO-SLB-MIB",
    "SlbServerString",
    "slbEntity",
    "slbServerFarmName")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoPort,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoPort")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

ciscoSlbHealthMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 508)
)
ciscoSlbHealthMonMIB.setRevisions(
        ("2008-06-26 00:00",
         "2008-03-11 00:00",
         "2006-11-14 00:00",
         "2006-01-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SlbProbeType(Integer32, TextualConvention):
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("dnsProbe", 3),
          ("echoProbe", 20),
          ("fingerProbe", 19),
          ("ftpProbe", 5),
          ("httpProbe", 4),
          ("httpsProbe", 11),
          ("icmpProbe", 1),
          ("imapProbe", 14),
          ("ldapProbe", 12),
          ("popProbe", 13),
          ("radiusProbe", 15),
          ("rtspProbe", 21),
          ("scriptedProbe", 8),
          ("sipProbe", 17),
          ("smtpProbe", 7),
          ("snmpProbe", 22),
          ("tacacsProbe", 16),
          ("tcpProbe", 2),
          ("telnetProbe", 6),
          ("tftpProbe", 18),
          ("udpProbe", 10),
          ("undefined", 9))
    )



class CiscoProbeHealthMonState(Integer32, TextualConvention):
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
        *(("active", 4),
          ("disabled", 6),
          ("failed", 5),
          ("init", 3),
          ("invalid", 2),
          ("other", 1))
    )



class CiscoProbeInheritedPortType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("default", 5),
          ("other", 1),
          ("probe", 2),
          ("real", 3),
          ("vip", 4))
    )



# MIB Managed Objects in the order of their OIDs

_CslbxProbeCfgTable_Object = MibTable
cslbxProbeCfgTable = _CslbxProbeCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cslbxProbeCfgTable.setStatus("current")
_CslbxProbeCfgEntry_Object = MibTableRow
cslbxProbeCfgEntry = _CslbxProbeCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1)
)
cslbxProbeCfgEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeName"),
)
if mibBuilder.loadTexts:
    cslbxProbeCfgEntry.setStatus("current")
_CslbxProbeName_Type = SlbServerString
_CslbxProbeName_Object = MibTableColumn
cslbxProbeName = _CslbxProbeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 1),
    _CslbxProbeName_Type()
)
cslbxProbeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxProbeName.setStatus("current")
_CslbxProbeType_Type = SlbProbeType
_CslbxProbeType_Object = MibTableColumn
cslbxProbeType = _CslbxProbeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 2),
    _CslbxProbeType_Type()
)
cslbxProbeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbeType.setStatus("current")


class _CslbxProbeInterval_Type(TimeInterval):
    """Custom type cslbxProbeInterval based on TimeInterval"""
    defaultValue = 12000


_CslbxProbeInterval_Object = MibTableColumn
cslbxProbeInterval = _CslbxProbeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 3),
    _CslbxProbeInterval_Type()
)
cslbxProbeInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbeInterval.setStatus("current")
if mibBuilder.loadTexts:
    cslbxProbeInterval.setUnits("seconds")


class _CslbxProbeRetries_Type(Unsigned32):
    """Custom type cslbxProbeRetries based on Unsigned32"""
    defaultValue = 3


_CslbxProbeRetries_Object = MibTableColumn
cslbxProbeRetries = _CslbxProbeRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 4),
    _CslbxProbeRetries_Type()
)
cslbxProbeRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbeRetries.setStatus("current")


class _CslbxProbeFailedInterval_Type(TimeInterval):
    """Custom type cslbxProbeFailedInterval based on TimeInterval"""
    defaultValue = 30000


_CslbxProbeFailedInterval_Object = MibTableColumn
cslbxProbeFailedInterval = _CslbxProbeFailedInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 5),
    _CslbxProbeFailedInterval_Type()
)
cslbxProbeFailedInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbeFailedInterval.setStatus("current")
if mibBuilder.loadTexts:
    cslbxProbeFailedInterval.setUnits("seconds")


class _CslbxProbeReceiveTimeout_Type(TimeInterval):
    """Custom type cslbxProbeReceiveTimeout based on TimeInterval"""
    defaultValue = 1000


_CslbxProbeReceiveTimeout_Object = MibTableColumn
cslbxProbeReceiveTimeout = _CslbxProbeReceiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 6),
    _CslbxProbeReceiveTimeout_Type()
)
cslbxProbeReceiveTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbeReceiveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cslbxProbeReceiveTimeout.setUnits("seconds")


class _CslbxProbeTcpOpenTimeout_Type(TimeInterval):
    """Custom type cslbxProbeTcpOpenTimeout based on TimeInterval"""
    defaultValue = 1000


_CslbxProbeTcpOpenTimeout_Object = MibTableColumn
cslbxProbeTcpOpenTimeout = _CslbxProbeTcpOpenTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 7),
    _CslbxProbeTcpOpenTimeout_Type()
)
cslbxProbeTcpOpenTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbeTcpOpenTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cslbxProbeTcpOpenTimeout.setUnits("seconds")


class _CslbxProbeAlternateDestAddrType_Type(InetAddressType):
    """Custom type cslbxProbeAlternateDestAddrType based on InetAddressType"""


_CslbxProbeAlternateDestAddrType_Object = MibTableColumn
cslbxProbeAlternateDestAddrType = _CslbxProbeAlternateDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 8),
    _CslbxProbeAlternateDestAddrType_Type()
)
cslbxProbeAlternateDestAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbeAlternateDestAddrType.setStatus("current")


class _CslbxProbeAlternateDestAddr_Type(InetAddress):
    """Custom type cslbxProbeAlternateDestAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CslbxProbeAlternateDestAddr_Type.__name__ = "InetAddress"
_CslbxProbeAlternateDestAddr_Object = MibTableColumn
cslbxProbeAlternateDestAddr = _CslbxProbeAlternateDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 9),
    _CslbxProbeAlternateDestAddr_Type()
)
cslbxProbeAlternateDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbeAlternateDestAddr.setStatus("current")
_CslbxProbeDnsDomainName_Type = SnmpAdminString
_CslbxProbeDnsDomainName_Object = MibTableColumn
cslbxProbeDnsDomainName = _CslbxProbeDnsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 10),
    _CslbxProbeDnsDomainName_Type()
)
cslbxProbeDnsDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbeDnsDomainName.setStatus("current")


class _CslbxProbeHttpRequestMethod_Type(SnmpAdminString):
    """Custom type cslbxProbeHttpRequestMethod based on SnmpAdminString"""
    defaultValue = OctetString("get")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CslbxProbeHttpRequestMethod_Type.__name__ = "SnmpAdminString"
_CslbxProbeHttpRequestMethod_Object = MibTableColumn
cslbxProbeHttpRequestMethod = _CslbxProbeHttpRequestMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 11),
    _CslbxProbeHttpRequestMethod_Type()
)
cslbxProbeHttpRequestMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbeHttpRequestMethod.setStatus("current")
_CslbxProbeHttpRequestUrl_Type = SlbUrlString
_CslbxProbeHttpRequestUrl_Object = MibTableColumn
cslbxProbeHttpRequestUrl = _CslbxProbeHttpRequestUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 12),
    _CslbxProbeHttpRequestUrl_Type()
)
cslbxProbeHttpRequestUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbeHttpRequestUrl.setStatus("current")
_CslbxProbeRowStatus_Type = RowStatus
_CslbxProbeRowStatus_Object = MibTableColumn
cslbxProbeRowStatus = _CslbxProbeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 13),
    _CslbxProbeRowStatus_Type()
)
cslbxProbeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbeRowStatus.setStatus("current")


class _CslbxProbeScriptName_Type(SlbFunctionNameString):
    """Custom type cslbxProbeScriptName based on SlbFunctionNameString"""
    defaultHexValue = ""


_CslbxProbeScriptName_Object = MibTableColumn
cslbxProbeScriptName = _CslbxProbeScriptName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 14),
    _CslbxProbeScriptName_Type()
)
cslbxProbeScriptName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbeScriptName.setStatus("current")


class _CslbxProbeScriptArguments_Type(SnmpAdminString):
    """Custom type cslbxProbeScriptArguments based on SnmpAdminString"""
    defaultHexValue = ""


_CslbxProbeScriptArguments_Object = MibTableColumn
cslbxProbeScriptArguments = _CslbxProbeScriptArguments_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 15),
    _CslbxProbeScriptArguments_Type()
)
cslbxProbeScriptArguments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbeScriptArguments.setStatus("current")


class _CslbxProbePort_Type(CiscoPort):
    """Custom type cslbxProbePort based on CiscoPort"""
    defaultValue = 0


_CslbxProbePort_Object = MibTableColumn
cslbxProbePort = _CslbxProbePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 16),
    _CslbxProbePort_Type()
)
cslbxProbePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbePort.setStatus("current")
_CslbxProbeDescription_Type = SnmpAdminString
_CslbxProbeDescription_Object = MibTableColumn
cslbxProbeDescription = _CslbxProbeDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 17),
    _CslbxProbeDescription_Type()
)
cslbxProbeDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbeDescription.setStatus("current")


class _CslbxProbeRouteMethod_Type(Integer32):
    """Custom type cslbxProbeRouteMethod based on Integer32"""
    defaultValue = 2

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
          ("routingTable", 3),
          ("transparent", 2))
    )


_CslbxProbeRouteMethod_Type.__name__ = "Integer32"
_CslbxProbeRouteMethod_Object = MibTableColumn
cslbxProbeRouteMethod = _CslbxProbeRouteMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 18),
    _CslbxProbeRouteMethod_Type()
)
cslbxProbeRouteMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbeRouteMethod.setStatus("current")


class _CslbxProbeProtocolType_Type(Integer32):
    """Custom type cslbxProbeProtocolType based on Integer32"""
    defaultValue = 2

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
          ("tcp", 2),
          ("udp", 3))
    )


_CslbxProbeProtocolType_Type.__name__ = "Integer32"
_CslbxProbeProtocolType_Object = MibTableColumn
cslbxProbeProtocolType = _CslbxProbeProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 19),
    _CslbxProbeProtocolType_Type()
)
cslbxProbeProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbeProtocolType.setStatus("current")
_CslbxProbePassCount_Type = Unsigned32
_CslbxProbePassCount_Object = MibTableColumn
cslbxProbePassCount = _CslbxProbePassCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 20),
    _CslbxProbePassCount_Type()
)
cslbxProbePassCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbePassCount.setStatus("current")


class _CslbxProbePriority_Type(Unsigned32):
    """Custom type cslbxProbePriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CslbxProbePriority_Type.__name__ = "Unsigned32"
_CslbxProbePriority_Object = MibTableColumn
cslbxProbePriority = _CslbxProbePriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 21),
    _CslbxProbePriority_Type()
)
cslbxProbePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbePriority.setStatus("current")
_CslbxProbeUserName_Type = SnmpAdminString
_CslbxProbeUserName_Object = MibTableColumn
cslbxProbeUserName = _CslbxProbeUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 22),
    _CslbxProbeUserName_Type()
)
cslbxProbeUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbeUserName.setStatus("current")
_CslbxProbePassword_Type = SnmpAdminString
_CslbxProbePassword_Object = MibTableColumn
cslbxProbePassword = _CslbxProbePassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 23),
    _CslbxProbePassword_Type()
)
cslbxProbePassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbePassword.setStatus("current")


class _CslbxProbeConnTermination_Type(Integer32):
    """Custom type cslbxProbeConnTermination based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forced", 2),
          ("graceful", 1))
    )


_CslbxProbeConnTermination_Type.__name__ = "Integer32"
_CslbxProbeConnTermination_Object = MibTableColumn
cslbxProbeConnTermination = _CslbxProbeConnTermination_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 24),
    _CslbxProbeConnTermination_Type()
)
cslbxProbeConnTermination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbeConnTermination.setStatus("current")
_CslbxProbeSocketReuse_Type = TruthValue
_CslbxProbeSocketReuse_Object = MibTableColumn
cslbxProbeSocketReuse = _CslbxProbeSocketReuse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 25),
    _CslbxProbeSocketReuse_Type()
)
cslbxProbeSocketReuse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbeSocketReuse.setStatus("current")


class _CslbxProbeSendDataType_Type(Integer32):
    """Custom type cslbxProbeSendDataType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("binary", 2))
    )


_CslbxProbeSendDataType_Type.__name__ = "Integer32"
_CslbxProbeSendDataType_Object = MibTableColumn
cslbxProbeSendDataType = _CslbxProbeSendDataType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 26),
    _CslbxProbeSendDataType_Type()
)
cslbxProbeSendDataType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbeSendDataType.setStatus("current")
_CslbxProbeSendData_Type = SnmpAdminString
_CslbxProbeSendData_Object = MibTableColumn
cslbxProbeSendData = _CslbxProbeSendData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 27),
    _CslbxProbeSendData_Type()
)
cslbxProbeSendData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbeSendData.setStatus("current")


class _CslbxProbeState_Type(TruthValue):
    """Custom type cslbxProbeState based on TruthValue"""


_CslbxProbeState_Object = MibTableColumn
cslbxProbeState = _CslbxProbeState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 1, 1, 28),
    _CslbxProbeState_Type()
)
cslbxProbeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxProbeState.setStatus("current")
_CslbxDnsProbeIpTable_Object = MibTable
cslbxDnsProbeIpTable = _CslbxDnsProbeIpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 2)
)
if mibBuilder.loadTexts:
    cslbxDnsProbeIpTable.setStatus("current")
_CslbxDnsProbeIpEntry_Object = MibTableRow
cslbxDnsProbeIpEntry = _CslbxDnsProbeIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 2, 1)
)
cslbxDnsProbeIpEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-HEALTH-MON-MIB", "cslbxDnsProbeIpProbeName"),
    (0, "CISCO-SLB-HEALTH-MON-MIB", "cslbxDnsProbeIpAddressType"),
    (0, "CISCO-SLB-HEALTH-MON-MIB", "cslbxDnsProbeIpAddress"),
)
if mibBuilder.loadTexts:
    cslbxDnsProbeIpEntry.setStatus("current")
_CslbxDnsProbeIpProbeName_Type = SlbServerString
_CslbxDnsProbeIpProbeName_Object = MibTableColumn
cslbxDnsProbeIpProbeName = _CslbxDnsProbeIpProbeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 2, 1, 1),
    _CslbxDnsProbeIpProbeName_Type()
)
cslbxDnsProbeIpProbeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxDnsProbeIpProbeName.setStatus("current")
_CslbxDnsProbeIpAddressType_Type = InetAddressType
_CslbxDnsProbeIpAddressType_Object = MibTableColumn
cslbxDnsProbeIpAddressType = _CslbxDnsProbeIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 2, 1, 2),
    _CslbxDnsProbeIpAddressType_Type()
)
cslbxDnsProbeIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxDnsProbeIpAddressType.setStatus("current")


class _CslbxDnsProbeIpAddress_Type(InetAddress):
    """Custom type cslbxDnsProbeIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CslbxDnsProbeIpAddress_Type.__name__ = "InetAddress"
_CslbxDnsProbeIpAddress_Object = MibTableColumn
cslbxDnsProbeIpAddress = _CslbxDnsProbeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 2, 1, 3),
    _CslbxDnsProbeIpAddress_Type()
)
cslbxDnsProbeIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxDnsProbeIpAddress.setStatus("current")
_CslbxDnsProbeIpRowStatus_Type = RowStatus
_CslbxDnsProbeIpRowStatus_Object = MibTableColumn
cslbxDnsProbeIpRowStatus = _CslbxDnsProbeIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 2, 1, 4),
    _CslbxDnsProbeIpRowStatus_Type()
)
cslbxDnsProbeIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxDnsProbeIpRowStatus.setStatus("current")
_CslbxProbeHeaderCfgTable_Object = MibTable
cslbxProbeHeaderCfgTable = _CslbxProbeHeaderCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 3)
)
if mibBuilder.loadTexts:
    cslbxProbeHeaderCfgTable.setStatus("current")
_CslbxProbeHeaderCfgEntry_Object = MibTableRow
cslbxProbeHeaderCfgEntry = _CslbxProbeHeaderCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 3, 1)
)
cslbxProbeHeaderCfgEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeHeaderProbeName"),
    (0, "CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeHeaderFieldName"),
)
if mibBuilder.loadTexts:
    cslbxProbeHeaderCfgEntry.setStatus("current")
_CslbxProbeHeaderProbeName_Type = SlbServerString
_CslbxProbeHeaderProbeName_Object = MibTableColumn
cslbxProbeHeaderProbeName = _CslbxProbeHeaderProbeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 3, 1, 1),
    _CslbxProbeHeaderProbeName_Type()
)
cslbxProbeHeaderProbeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxProbeHeaderProbeName.setStatus("current")


class _CslbxProbeHeaderFieldName_Type(SnmpAdminString):
    """Custom type cslbxProbeHeaderFieldName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CslbxProbeHeaderFieldName_Type.__name__ = "SnmpAdminString"
_CslbxProbeHeaderFieldName_Object = MibTableColumn
cslbxProbeHeaderFieldName = _CslbxProbeHeaderFieldName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 3, 1, 2),
    _CslbxProbeHeaderFieldName_Type()
)
cslbxProbeHeaderFieldName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxProbeHeaderFieldName.setStatus("current")
_CslbxProbeHeaderFieldValue_Type = SnmpAdminString
_CslbxProbeHeaderFieldValue_Object = MibTableColumn
cslbxProbeHeaderFieldValue = _CslbxProbeHeaderFieldValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 3, 1, 3),
    _CslbxProbeHeaderFieldValue_Type()
)
cslbxProbeHeaderFieldValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbeHeaderFieldValue.setStatus("current")
_CslbxProbeHeaderRowStatus_Type = RowStatus
_CslbxProbeHeaderRowStatus_Object = MibTableColumn
cslbxProbeHeaderRowStatus = _CslbxProbeHeaderRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 3, 1, 4),
    _CslbxProbeHeaderRowStatus_Type()
)
cslbxProbeHeaderRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbeHeaderRowStatus.setStatus("current")
_CslbxProbeExpectStatusCfgTable_Object = MibTable
cslbxProbeExpectStatusCfgTable = _CslbxProbeExpectStatusCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 4)
)
if mibBuilder.loadTexts:
    cslbxProbeExpectStatusCfgTable.setStatus("current")
_CslbxProbeExpectStatusCfgEntry_Object = MibTableRow
cslbxProbeExpectStatusCfgEntry = _CslbxProbeExpectStatusCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 4, 1)
)
cslbxProbeExpectStatusCfgEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeExpectStatusProbeName"),
    (0, "CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeExpectStatusMinValue"),
)
if mibBuilder.loadTexts:
    cslbxProbeExpectStatusCfgEntry.setStatus("current")
_CslbxProbeExpectStatusProbeName_Type = SlbServerString
_CslbxProbeExpectStatusProbeName_Object = MibTableColumn
cslbxProbeExpectStatusProbeName = _CslbxProbeExpectStatusProbeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 4, 1, 1),
    _CslbxProbeExpectStatusProbeName_Type()
)
cslbxProbeExpectStatusProbeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxProbeExpectStatusProbeName.setStatus("current")
_CslbxProbeExpectStatusMinValue_Type = Unsigned32
_CslbxProbeExpectStatusMinValue_Object = MibTableColumn
cslbxProbeExpectStatusMinValue = _CslbxProbeExpectStatusMinValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 4, 1, 2),
    _CslbxProbeExpectStatusMinValue_Type()
)
cslbxProbeExpectStatusMinValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxProbeExpectStatusMinValue.setStatus("current")
_CslbxProbeExpectStatusMaxValue_Type = Unsigned32
_CslbxProbeExpectStatusMaxValue_Object = MibTableColumn
cslbxProbeExpectStatusMaxValue = _CslbxProbeExpectStatusMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 4, 1, 3),
    _CslbxProbeExpectStatusMaxValue_Type()
)
cslbxProbeExpectStatusMaxValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbeExpectStatusMaxValue.setStatus("current")
_CslbxProbeExpectStatusRowStatus_Type = RowStatus
_CslbxProbeExpectStatusRowStatus_Object = MibTableColumn
cslbxProbeExpectStatusRowStatus = _CslbxProbeExpectStatusRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 4, 1, 4),
    _CslbxProbeExpectStatusRowStatus_Type()
)
cslbxProbeExpectStatusRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxProbeExpectStatusRowStatus.setStatus("current")
_CslbxProbeHTTPCfgTable_Object = MibTable
cslbxProbeHTTPCfgTable = _CslbxProbeHTTPCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 5)
)
if mibBuilder.loadTexts:
    cslbxProbeHTTPCfgTable.setStatus("current")
_CslbxProbeHTTPCfgEntry_Object = MibTableRow
cslbxProbeHTTPCfgEntry = _CslbxProbeHTTPCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 5, 1)
)
cslbxProbeHTTPCfgEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeName"),
)
if mibBuilder.loadTexts:
    cslbxProbeHTTPCfgEntry.setStatus("current")


class _CslbxProbeHTTPCfgVersion_Type(Integer32):
    """Custom type cslbxProbeHTTPCfgVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("httpOneDotOne", 2),
          ("httpOneDotZero", 1))
    )


_CslbxProbeHTTPCfgVersion_Type.__name__ = "Integer32"
_CslbxProbeHTTPCfgVersion_Object = MibTableColumn
cslbxProbeHTTPCfgVersion = _CslbxProbeHTTPCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 5, 1, 1),
    _CslbxProbeHTTPCfgVersion_Type()
)
cslbxProbeHTTPCfgVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cslbxProbeHTTPCfgVersion.setStatus("current")


class _CslbxProbeHTTPCfgPersistence_Type(TruthValue):
    """Custom type cslbxProbeHTTPCfgPersistence based on TruthValue"""


_CslbxProbeHTTPCfgPersistence_Object = MibTableColumn
cslbxProbeHTTPCfgPersistence = _CslbxProbeHTTPCfgPersistence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 5, 1, 2),
    _CslbxProbeHTTPCfgPersistence_Type()
)
cslbxProbeHTTPCfgPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cslbxProbeHTTPCfgPersistence.setStatus("current")


class _CslbxProbeHTTPCfgHashValid_Type(TruthValue):
    """Custom type cslbxProbeHTTPCfgHashValid based on TruthValue"""


_CslbxProbeHTTPCfgHashValid_Object = MibTableColumn
cslbxProbeHTTPCfgHashValid = _CslbxProbeHTTPCfgHashValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 5, 1, 3),
    _CslbxProbeHTTPCfgHashValid_Type()
)
cslbxProbeHTTPCfgHashValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cslbxProbeHTTPCfgHashValid.setStatus("current")
_CslbxProbeHTTPCfgHashName_Type = SnmpAdminString
_CslbxProbeHTTPCfgHashName_Object = MibTableColumn
cslbxProbeHTTPCfgHashName = _CslbxProbeHTTPCfgHashName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 5, 1, 4),
    _CslbxProbeHTTPCfgHashName_Type()
)
cslbxProbeHTTPCfgHashName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cslbxProbeHTTPCfgHashName.setStatus("current")


class _CslbxProbeHTTPCfgCipherSuite_Type(Integer32):
    """Custom type cslbxProbeHTTPCfgCipherSuite based on Integer32"""
    defaultValue = 1

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
        *(("rsaAny", 2),
          ("rsaExport1024WithDesCbcSha", 10),
          ("rsaExport1024WithRc456Md5", 9),
          ("rsaExport1024WithRc456Sha", 11),
          ("rsaExportWithDes40CbcSha", 8),
          ("rsaExportWithRc440Md5", 7),
          ("rsaOther", 1),
          ("rsaWith3desEdeCbcSha", 6),
          ("rsaWithAes128CbcSha", 12),
          ("rsaWithAes256cbcSha", 13),
          ("rsaWithRc4128Md5", 3),
          ("rsaWithRc4128Sha", 4),
          ("rsaWithdesCbcSha", 5))
    )


_CslbxProbeHTTPCfgCipherSuite_Type.__name__ = "Integer32"
_CslbxProbeHTTPCfgCipherSuite_Object = MibTableColumn
cslbxProbeHTTPCfgCipherSuite = _CslbxProbeHTTPCfgCipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 5, 1, 5),
    _CslbxProbeHTTPCfgCipherSuite_Type()
)
cslbxProbeHTTPCfgCipherSuite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cslbxProbeHTTPCfgCipherSuite.setStatus("current")


class _CslbxProbeHTTPCfgSslTlsVersion_Type(Integer32):
    """Custom type cslbxProbeHTTPCfgSslTlsVersion based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("all", 5),
          ("other", 1),
          ("sslv2", 2),
          ("sslv3", 3),
          ("tlsv1", 4))
    )


_CslbxProbeHTTPCfgSslTlsVersion_Type.__name__ = "Integer32"
_CslbxProbeHTTPCfgSslTlsVersion_Object = MibTableColumn
cslbxProbeHTTPCfgSslTlsVersion = _CslbxProbeHTTPCfgSslTlsVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 5, 1, 6),
    _CslbxProbeHTTPCfgSslTlsVersion_Type()
)
cslbxProbeHTTPCfgSslTlsVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cslbxProbeHTTPCfgSslTlsVersion.setStatus("current")
_CslbxProbeHTTPCfgSslSessionReuse_Type = TruthValue
_CslbxProbeHTTPCfgSslSessionReuse_Object = MibTableColumn
cslbxProbeHTTPCfgSslSessionReuse = _CslbxProbeHTTPCfgSslSessionReuse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 5, 1, 7),
    _CslbxProbeHTTPCfgSslSessionReuse_Type()
)
cslbxProbeHTTPCfgSslSessionReuse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cslbxProbeHTTPCfgSslSessionReuse.setStatus("current")


class _CslbxProbeHTTPSslTlsVersionSupported_Type(Bits):
    """Custom type cslbxProbeHTTPSslTlsVersionSupported based on Bits"""
    namedValues = NamedValues(
        *(("sslv3", 0),
          ("tlsv1", 1))
    )

_CslbxProbeHTTPSslTlsVersionSupported_Type.__name__ = "Bits"
_CslbxProbeHTTPSslTlsVersionSupported_Object = MibTableColumn
cslbxProbeHTTPSslTlsVersionSupported = _CslbxProbeHTTPSslTlsVersionSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 5, 1, 8),
    _CslbxProbeHTTPSslTlsVersionSupported_Type()
)
cslbxProbeHTTPSslTlsVersionSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxProbeHTTPSslTlsVersionSupported.setStatus("current")
_CslbxProbeSIPCfgTable_Object = MibTable
cslbxProbeSIPCfgTable = _CslbxProbeSIPCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 6)
)
if mibBuilder.loadTexts:
    cslbxProbeSIPCfgTable.setStatus("current")
_CslbxProbeSIPCfgEntry_Object = MibTableRow
cslbxProbeSIPCfgEntry = _CslbxProbeSIPCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 6, 1)
)
cslbxProbeSIPCfgEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeName"),
)
if mibBuilder.loadTexts:
    cslbxProbeSIPCfgEntry.setStatus("current")


class _CslbxProbeSIPRegAddress_Type(SnmpAdminString):
    """Custom type cslbxProbeSIPRegAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CslbxProbeSIPRegAddress_Type.__name__ = "SnmpAdminString"
_CslbxProbeSIPRegAddress_Object = MibTableColumn
cslbxProbeSIPRegAddress = _CslbxProbeSIPRegAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 6, 1, 1),
    _CslbxProbeSIPRegAddress_Type()
)
cslbxProbeSIPRegAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cslbxProbeSIPRegAddress.setStatus("current")
_CslbxProbeFTPCfgTable_Object = MibTable
cslbxProbeFTPCfgTable = _CslbxProbeFTPCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 7)
)
if mibBuilder.loadTexts:
    cslbxProbeFTPCfgTable.setStatus("current")
_CslbxProbeFTPCfgEntry_Object = MibTableRow
cslbxProbeFTPCfgEntry = _CslbxProbeFTPCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 7, 1)
)
cslbxProbeFTPCfgEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeName"),
)
if mibBuilder.loadTexts:
    cslbxProbeFTPCfgEntry.setStatus("current")


class _CslbxProbeFtpRequestMethod_Type(Integer32):
    """Custom type cslbxProbeFtpRequestMethod based on Integer32"""
    defaultValue = 3

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
        *(("get", 3),
          ("ls", 2),
          ("other", 1),
          ("put", 4))
    )


_CslbxProbeFtpRequestMethod_Type.__name__ = "Integer32"
_CslbxProbeFtpRequestMethod_Object = MibTableColumn
cslbxProbeFtpRequestMethod = _CslbxProbeFtpRequestMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 7, 1, 1),
    _CslbxProbeFtpRequestMethod_Type()
)
cslbxProbeFtpRequestMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cslbxProbeFtpRequestMethod.setStatus("current")
_CslbxProbeFtpRequestFileName_Type = SlbUrlString
_CslbxProbeFtpRequestFileName_Object = MibTableColumn
cslbxProbeFtpRequestFileName = _CslbxProbeFtpRequestFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 7, 1, 2),
    _CslbxProbeFtpRequestFileName_Type()
)
cslbxProbeFtpRequestFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cslbxProbeFtpRequestFileName.setStatus("current")


class _CslbxProbeFtpRequestFileType_Type(Integer32):
    """Custom type cslbxProbeFtpRequestFileType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("binary", 2))
    )


_CslbxProbeFtpRequestFileType_Type.__name__ = "Integer32"
_CslbxProbeFtpRequestFileType_Object = MibTableColumn
cslbxProbeFtpRequestFileType = _CslbxProbeFtpRequestFileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 7, 1, 3),
    _CslbxProbeFtpRequestFileType_Type()
)
cslbxProbeFtpRequestFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cslbxProbeFtpRequestFileType.setStatus("current")
_CslbxProbeTFTPCfgTable_Object = MibTable
cslbxProbeTFTPCfgTable = _CslbxProbeTFTPCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 8)
)
if mibBuilder.loadTexts:
    cslbxProbeTFTPCfgTable.setStatus("current")
_CslbxProbeTFTPCfgEntry_Object = MibTableRow
cslbxProbeTFTPCfgEntry = _CslbxProbeTFTPCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 8, 1)
)
cslbxProbeTFTPCfgEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeName"),
)
if mibBuilder.loadTexts:
    cslbxProbeTFTPCfgEntry.setStatus("current")


class _CslbxProbeTftpRequestMethod_Type(Integer32):
    """Custom type cslbxProbeTftpRequestMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("get", 1),
          ("put", 2))
    )


_CslbxProbeTftpRequestMethod_Type.__name__ = "Integer32"
_CslbxProbeTftpRequestMethod_Object = MibTableColumn
cslbxProbeTftpRequestMethod = _CslbxProbeTftpRequestMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 8, 1, 1),
    _CslbxProbeTftpRequestMethod_Type()
)
cslbxProbeTftpRequestMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cslbxProbeTftpRequestMethod.setStatus("current")
_CslbxProbeTftpRequestFileName_Type = SlbUrlString
_CslbxProbeTftpRequestFileName_Object = MibTableColumn
cslbxProbeTftpRequestFileName = _CslbxProbeTftpRequestFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 8, 1, 2),
    _CslbxProbeTftpRequestFileName_Type()
)
cslbxProbeTftpRequestFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cslbxProbeTftpRequestFileName.setStatus("current")


class _CslbxProbeTftpRequestFileType_Type(Integer32):
    """Custom type cslbxProbeTftpRequestFileType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("binary", 2))
    )


_CslbxProbeTftpRequestFileType_Type.__name__ = "Integer32"
_CslbxProbeTftpRequestFileType_Object = MibTableColumn
cslbxProbeTftpRequestFileType = _CslbxProbeTftpRequestFileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 8, 1, 3),
    _CslbxProbeTftpRequestFileType_Type()
)
cslbxProbeTftpRequestFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cslbxProbeTftpRequestFileType.setStatus("current")
_CslbxProbeIMAPCfgTable_Object = MibTable
cslbxProbeIMAPCfgTable = _CslbxProbeIMAPCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 9)
)
if mibBuilder.loadTexts:
    cslbxProbeIMAPCfgTable.setStatus("current")
_CslbxProbeIMAPCfgEntry_Object = MibTableRow
cslbxProbeIMAPCfgEntry = _CslbxProbeIMAPCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 9, 1)
)
cslbxProbeIMAPCfgEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeName"),
)
if mibBuilder.loadTexts:
    cslbxProbeIMAPCfgEntry.setStatus("current")
_CslbxProbeIMAPMailBox_Type = SnmpAdminString
_CslbxProbeIMAPMailBox_Object = MibTableColumn
cslbxProbeIMAPMailBox = _CslbxProbeIMAPMailBox_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 9, 1, 1),
    _CslbxProbeIMAPMailBox_Type()
)
cslbxProbeIMAPMailBox.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cslbxProbeIMAPMailBox.setStatus("current")
_CslbxProbeIMAPMethodName_Type = SnmpAdminString
_CslbxProbeIMAPMethodName_Object = MibTableColumn
cslbxProbeIMAPMethodName = _CslbxProbeIMAPMethodName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6, 9, 1, 2),
    _CslbxProbeIMAPMethodName_Type()
)
cslbxProbeIMAPMethodName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cslbxProbeIMAPMethodName.setStatus("current")
_CiscoSlbHealthMonMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSlbHealthMonMIBNotifs = _CiscoSlbHealthMonMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 0)
)
_CiscoSlbHealthMonMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSlbHealthMonMIBObjects = _CiscoSlbHealthMonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1)
)
_CshMonSfarmProbes_ObjectIdentity = ObjectIdentity
cshMonSfarmProbes = _CshMonSfarmProbes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1)
)
_CshMonSfarmRealProbeStatsTable_Object = MibTable
cshMonSfarmRealProbeStatsTable = _CshMonSfarmRealProbeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cshMonSfarmRealProbeStatsTable.setStatus("deprecated")
_CshMonSfarmRealProbeStatsEntry_Object = MibTableRow
cshMonSfarmRealProbeStatsEntry = _CshMonSfarmRealProbeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 1, 1)
)
cshMonSfarmRealProbeStatsEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeName"),
    (0, "CISCO-SLB-MIB", "slbServerFarmName"),
    (0, "CISCO-SLB-HEALTH-MON-MIB", "cshMonSfarmRealServerName"),
    (0, "CISCO-SLB-HEALTH-MON-MIB", "cshMonSfarmRealServerPort"),
)
if mibBuilder.loadTexts:
    cshMonSfarmRealProbeStatsEntry.setStatus("deprecated")


class _CshMonSfarmRealServerName_Type(SnmpAdminString):
    """Custom type cshMonSfarmRealServerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CshMonSfarmRealServerName_Type.__name__ = "SnmpAdminString"
_CshMonSfarmRealServerName_Object = MibTableColumn
cshMonSfarmRealServerName = _CshMonSfarmRealServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 1, 1, 1),
    _CshMonSfarmRealServerName_Type()
)
cshMonSfarmRealServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cshMonSfarmRealServerName.setStatus("deprecated")
_CshMonSfarmRealServerPort_Type = InetPortNumber
_CshMonSfarmRealServerPort_Object = MibTableColumn
cshMonSfarmRealServerPort = _CshMonSfarmRealServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 1, 1, 2),
    _CshMonSfarmRealServerPort_Type()
)
cshMonSfarmRealServerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cshMonSfarmRealServerPort.setStatus("deprecated")
_CshMonSfarmRealProbesPassed_Type = Counter32
_CshMonSfarmRealProbesPassed_Object = MibTableColumn
cshMonSfarmRealProbesPassed = _CshMonSfarmRealProbesPassed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 1, 1, 3),
    _CshMonSfarmRealProbesPassed_Type()
)
cshMonSfarmRealProbesPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshMonSfarmRealProbesPassed.setStatus("deprecated")
_CshMonSfarmRealProbesFailed_Type = Counter32
_CshMonSfarmRealProbesFailed_Object = MibTableColumn
cshMonSfarmRealProbesFailed = _CshMonSfarmRealProbesFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 1, 1, 4),
    _CshMonSfarmRealProbesFailed_Type()
)
cshMonSfarmRealProbesFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshMonSfarmRealProbesFailed.setStatus("deprecated")


class _CshMonSfarmRealProbeHealthMonState_Type(CiscoProbeHealthMonState):
    """Custom type cshMonSfarmRealProbeHealthMonState based on CiscoProbeHealthMonState"""


_CshMonSfarmRealProbeHealthMonState_Object = MibTableColumn
cshMonSfarmRealProbeHealthMonState = _CshMonSfarmRealProbeHealthMonState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 1, 1, 5),
    _CshMonSfarmRealProbeHealthMonState_Type()
)
cshMonSfarmRealProbeHealthMonState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshMonSfarmRealProbeHealthMonState.setStatus("deprecated")
_CshMonProbeTypeStatsTable_Object = MibTable
cshMonProbeTypeStatsTable = _CshMonProbeTypeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cshMonProbeTypeStatsTable.setStatus("current")
_CshMonProbeTypeStatsEntry_Object = MibTableRow
cshMonProbeTypeStatsEntry = _CshMonProbeTypeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 2, 1)
)
cshMonProbeTypeStatsEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeType"),
)
if mibBuilder.loadTexts:
    cshMonProbeTypeStatsEntry.setStatus("current")
_CshMonProbeTotalSentProbes_Type = Counter32
_CshMonProbeTotalSentProbes_Object = MibTableColumn
cshMonProbeTotalSentProbes = _CshMonProbeTotalSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 2, 1, 1),
    _CshMonProbeTotalSentProbes_Type()
)
cshMonProbeTotalSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshMonProbeTotalSentProbes.setStatus("current")
_CshMonProbeTotalPassedProbes_Type = Counter32
_CshMonProbeTotalPassedProbes_Object = MibTableColumn
cshMonProbeTotalPassedProbes = _CshMonProbeTotalPassedProbes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 2, 1, 2),
    _CshMonProbeTotalPassedProbes_Type()
)
cshMonProbeTotalPassedProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshMonProbeTotalPassedProbes.setStatus("current")
_CshMonProbeTotalConnectionErrors_Type = Counter32
_CshMonProbeTotalConnectionErrors_Object = MibTableColumn
cshMonProbeTotalConnectionErrors = _CshMonProbeTotalConnectionErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 2, 1, 3),
    _CshMonProbeTotalConnectionErrors_Type()
)
cshMonProbeTotalConnectionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshMonProbeTotalConnectionErrors.setStatus("current")
_CshMonProbeTotalReceivedRSTs_Type = Counter32
_CshMonProbeTotalReceivedRSTs_Object = MibTableColumn
cshMonProbeTotalReceivedRSTs = _CshMonProbeTotalReceivedRSTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 2, 1, 4),
    _CshMonProbeTotalReceivedRSTs_Type()
)
cshMonProbeTotalReceivedRSTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshMonProbeTotalReceivedRSTs.setStatus("current")
_CshMonProbeTotalReceiveTimeouts_Type = Counter32
_CshMonProbeTotalReceiveTimeouts_Object = MibTableColumn
cshMonProbeTotalReceiveTimeouts = _CshMonProbeTotalReceiveTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 2, 1, 5),
    _CshMonProbeTotalReceiveTimeouts_Type()
)
cshMonProbeTotalReceiveTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshMonProbeTotalReceiveTimeouts.setStatus("current")
_CshMonProbeTotalSendFailures_Type = Counter32
_CshMonProbeTotalSendFailures_Object = MibTableColumn
cshMonProbeTotalSendFailures = _CshMonProbeTotalSendFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 2, 1, 6),
    _CshMonProbeTotalSendFailures_Type()
)
cshMonProbeTotalSendFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshMonProbeTotalSendFailures.setStatus("current")
_CshMonProbeTotalFailedProbes_Type = Counter32
_CshMonProbeTotalFailedProbes_Object = MibTableColumn
cshMonProbeTotalFailedProbes = _CshMonProbeTotalFailedProbes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 2, 1, 7),
    _CshMonProbeTotalFailedProbes_Type()
)
cshMonProbeTotalFailedProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshMonProbeTotalFailedProbes.setStatus("current")
_CshMonProbeTotalRefusedConns_Type = Counter32
_CshMonProbeTotalRefusedConns_Object = MibTableColumn
cshMonProbeTotalRefusedConns = _CshMonProbeTotalRefusedConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 2, 1, 8),
    _CshMonProbeTotalRefusedConns_Type()
)
cshMonProbeTotalRefusedConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshMonProbeTotalRefusedConns.setStatus("current")
_CshMonProbeTotalOpenTimeouts_Type = Counter32
_CshMonProbeTotalOpenTimeouts_Object = MibTableColumn
cshMonProbeTotalOpenTimeouts = _CshMonProbeTotalOpenTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 2, 1, 9),
    _CshMonProbeTotalOpenTimeouts_Type()
)
cshMonProbeTotalOpenTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshMonProbeTotalOpenTimeouts.setStatus("current")
_CshMonProbeTotalActiveSockets_Type = Counter32
_CshMonProbeTotalActiveSockets_Object = MibTableColumn
cshMonProbeTotalActiveSockets = _CshMonProbeTotalActiveSockets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 2, 1, 10),
    _CshMonProbeTotalActiveSockets_Type()
)
cshMonProbeTotalActiveSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshMonProbeTotalActiveSockets.setStatus("current")
_CshMonServerfarmRealProbeStatsTable_Object = MibTable
cshMonServerfarmRealProbeStatsTable = _CshMonServerfarmRealProbeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cshMonServerfarmRealProbeStatsTable.setStatus("current")
_CshMonServerfarmRealProbeStatsEntry_Object = MibTableRow
cshMonServerfarmRealProbeStatsEntry = _CshMonServerfarmRealProbeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 3, 1)
)
cshMonServerfarmRealProbeStatsEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeName"),
    (0, "CISCO-SLB-MIB", "slbServerFarmName"),
    (0, "CISCO-SLB-HEALTH-MON-MIB", "cshMonServerfarmRealServerName"),
    (0, "CISCO-SLB-HEALTH-MON-MIB", "cshMonServerfarmRealServerPort"),
    (0, "CISCO-SLB-HEALTH-MON-MIB", "cshMonProbeInheritedPort"),
)
if mibBuilder.loadTexts:
    cshMonServerfarmRealProbeStatsEntry.setStatus("current")


class _CshMonServerfarmRealServerName_Type(SnmpAdminString):
    """Custom type cshMonServerfarmRealServerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CshMonServerfarmRealServerName_Type.__name__ = "SnmpAdminString"
_CshMonServerfarmRealServerName_Object = MibTableColumn
cshMonServerfarmRealServerName = _CshMonServerfarmRealServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 3, 1, 1),
    _CshMonServerfarmRealServerName_Type()
)
cshMonServerfarmRealServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cshMonServerfarmRealServerName.setStatus("current")
_CshMonServerfarmRealServerPort_Type = InetPortNumber
_CshMonServerfarmRealServerPort_Object = MibTableColumn
cshMonServerfarmRealServerPort = _CshMonServerfarmRealServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 3, 1, 2),
    _CshMonServerfarmRealServerPort_Type()
)
cshMonServerfarmRealServerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cshMonServerfarmRealServerPort.setStatus("current")
_CshMonProbeInheritedPort_Type = InetPortNumber
_CshMonProbeInheritedPort_Object = MibTableColumn
cshMonProbeInheritedPort = _CshMonProbeInheritedPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 3, 1, 3),
    _CshMonProbeInheritedPort_Type()
)
cshMonProbeInheritedPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cshMonProbeInheritedPort.setStatus("current")
_CshMonServerfarmRealPassedProbes_Type = Counter32
_CshMonServerfarmRealPassedProbes_Object = MibTableColumn
cshMonServerfarmRealPassedProbes = _CshMonServerfarmRealPassedProbes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 3, 1, 4),
    _CshMonServerfarmRealPassedProbes_Type()
)
cshMonServerfarmRealPassedProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshMonServerfarmRealPassedProbes.setStatus("current")
_CshMonServerfarmRealFailedProbes_Type = Counter32
_CshMonServerfarmRealFailedProbes_Object = MibTableColumn
cshMonServerfarmRealFailedProbes = _CshMonServerfarmRealFailedProbes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 3, 1, 5),
    _CshMonServerfarmRealFailedProbes_Type()
)
cshMonServerfarmRealFailedProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshMonServerfarmRealFailedProbes.setStatus("current")


class _CshMonServerfarmRealProbeHealthMonState_Type(CiscoProbeHealthMonState):
    """Custom type cshMonServerfarmRealProbeHealthMonState based on CiscoProbeHealthMonState"""


_CshMonServerfarmRealProbeHealthMonState_Object = MibTableColumn
cshMonServerfarmRealProbeHealthMonState = _CshMonServerfarmRealProbeHealthMonState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 3, 1, 6),
    _CshMonServerfarmRealProbeHealthMonState_Type()
)
cshMonServerfarmRealProbeHealthMonState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshMonServerfarmRealProbeHealthMonState.setStatus("current")
_CshMonServerfarmRealProbeLastProbeTime_Type = DateAndTime
_CshMonServerfarmRealProbeLastProbeTime_Object = MibTableColumn
cshMonServerfarmRealProbeLastProbeTime = _CshMonServerfarmRealProbeLastProbeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 3, 1, 7),
    _CshMonServerfarmRealProbeLastProbeTime_Type()
)
cshMonServerfarmRealProbeLastProbeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshMonServerfarmRealProbeLastProbeTime.setStatus("current")
_CshMonServerfarmRealProbeLastActiveTime_Type = DateAndTime
_CshMonServerfarmRealProbeLastActiveTime_Object = MibTableColumn
cshMonServerfarmRealProbeLastActiveTime = _CshMonServerfarmRealProbeLastActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 3, 1, 8),
    _CshMonServerfarmRealProbeLastActiveTime_Type()
)
cshMonServerfarmRealProbeLastActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshMonServerfarmRealProbeLastActiveTime.setStatus("current")
_CshMonServerfarmRealProbeLastFailedTime_Type = DateAndTime
_CshMonServerfarmRealProbeLastFailedTime_Object = MibTableColumn
cshMonServerfarmRealProbeLastFailedTime = _CshMonServerfarmRealProbeLastFailedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 3, 1, 9),
    _CshMonServerfarmRealProbeLastFailedTime_Type()
)
cshMonServerfarmRealProbeLastFailedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshMonServerfarmRealProbeLastFailedTime.setStatus("current")


class _CshMonProbeInheritedPortType_Type(CiscoProbeInheritedPortType):
    """Custom type cshMonProbeInheritedPortType based on CiscoProbeInheritedPortType"""


_CshMonProbeInheritedPortType_Object = MibTableColumn
cshMonProbeInheritedPortType = _CshMonProbeInheritedPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 1, 3, 1, 10),
    _CshMonProbeInheritedPortType_Type()
)
cshMonProbeInheritedPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cshMonProbeInheritedPortType.setStatus("current")
_CiscoSlbHealthMonNotifObjects_ObjectIdentity = ObjectIdentity
ciscoSlbHealthMonNotifObjects = _CiscoSlbHealthMonNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 2)
)
_CshMonSocketOverusageCount_Type = Gauge32
_CshMonSocketOverusageCount_Object = MibScalar
cshMonSocketOverusageCount = _CshMonSocketOverusageCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 1, 2, 1),
    _CshMonSocketOverusageCount_Type()
)
cshMonSocketOverusageCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cshMonSocketOverusageCount.setStatus("current")
_CiscoSlbHealthMonMIBConformance_ObjectIdentity = ObjectIdentity
ciscoSlbHealthMonMIBConformance = _CiscoSlbHealthMonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 2)
)
_CiscoSlbHealthMonMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSlbHealthMonMIBCompliances = _CiscoSlbHealthMonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 2, 1)
)
_CiscoSlbHealthMonMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSlbHealthMonMIBGroups = _CiscoSlbHealthMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 2, 2)
)

# Managed Objects groups

cslbHealthMonServerProbesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 2, 2, 1)
)
cslbHealthMonServerProbesGroup.setObjects(
      *(("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeType"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeInterval"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeRetries"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeFailedInterval"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeReceiveTimeout"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeTcpOpenTimeout"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeAlternateDestAddrType"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeAlternateDestAddr"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeDnsDomainName"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeRowStatus"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxDnsProbeIpRowStatus"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeExpectStatusMaxValue"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeExpectStatusRowStatus"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbePort"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeDescription"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeProtocolType"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeRouteMethod"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbePriority"))
)
if mibBuilder.loadTexts:
    cslbHealthMonServerProbesGroup.setStatus("deprecated")

cslbHealthMonProbeCfgExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 2, 2, 2)
)
cslbHealthMonProbeCfgExtGroup.setObjects(
      *(("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeUserName"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbePassword"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbePassCount"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeConnTermination"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeSocketReuse"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeSendDataType"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeSendData"))
)
if mibBuilder.loadTexts:
    cslbHealthMonProbeCfgExtGroup.setStatus("current")

cslbHealthMonSIPProbesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 2, 2, 3)
)
cslbHealthMonSIPProbesGroup.setObjects(
    ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeSIPRegAddress")
)
if mibBuilder.loadTexts:
    cslbHealthMonSIPProbesGroup.setStatus("current")

cslbHealthMonFTPProbesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 2, 2, 4)
)
cslbHealthMonFTPProbesGroup.setObjects(
      *(("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeFtpRequestMethod"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeFtpRequestFileName"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeFtpRequestFileType"))
)
if mibBuilder.loadTexts:
    cslbHealthMonFTPProbesGroup.setStatus("current")

cslbHealthMonHTTPProbesCommmonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 2, 2, 5)
)
cslbHealthMonHTTPProbesCommmonGroup.setObjects(
      *(("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeHttpRequestMethod"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeHttpRequestUrl"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeHeaderFieldValue"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeHeaderRowStatus"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeHTTPCfgVersion"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeHTTPCfgPersistence"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeHTTPCfgHashValid"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeHTTPCfgHashName"))
)
if mibBuilder.loadTexts:
    cslbHealthMonHTTPProbesCommmonGroup.setStatus("current")

cslbHealthMonHTTPSProbesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 2, 2, 6)
)
cslbHealthMonHTTPSProbesGroup.setObjects(
      *(("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeHTTPCfgCipherSuite"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeHTTPCfgSslTlsVersion"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeHTTPCfgSslSessionReuse"))
)
if mibBuilder.loadTexts:
    cslbHealthMonHTTPSProbesGroup.setStatus("deprecated")

cslbHealthMonTFTPProbesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 2, 2, 7)
)
cslbHealthMonTFTPProbesGroup.setObjects(
      *(("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeTftpRequestMethod"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeTftpRequestFileName"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeTftpRequestFileType"))
)
if mibBuilder.loadTexts:
    cslbHealthMonTFTPProbesGroup.setStatus("current")

cslbHealthMonIMAPProbesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 2, 2, 8)
)
cslbHealthMonIMAPProbesGroup.setObjects(
      *(("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeIMAPMailBox"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeIMAPMethodName"))
)
if mibBuilder.loadTexts:
    cslbHealthMonIMAPProbesGroup.setStatus("current")

cslbHealthMonProbeScriptGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 2, 2, 9)
)
cslbHealthMonProbeScriptGroup.setObjects(
      *(("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeScriptName"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeScriptArguments"))
)
if mibBuilder.loadTexts:
    cslbHealthMonProbeScriptGroup.setStatus("current")

cslbHealthMonHTTPSProbesGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 2, 2, 10)
)
cslbHealthMonHTTPSProbesGroupRev1.setObjects(
      *(("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeHTTPCfgCipherSuite"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeHTTPCfgSslTlsVersion"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeHTTPCfgSslSessionReuse"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeHTTPSslTlsVersionSupported"))
)
if mibBuilder.loadTexts:
    cslbHealthMonHTTPSProbesGroupRev1.setStatus("current")

cslbHealthMonServerProbesGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 2, 2, 11)
)
cslbHealthMonServerProbesGroupRev1.setObjects(
      *(("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeType"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeInterval"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeRetries"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeFailedInterval"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeReceiveTimeout"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeTcpOpenTimeout"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeAlternateDestAddrType"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeAlternateDestAddr"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeDnsDomainName"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeRowStatus"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxDnsProbeIpRowStatus"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeExpectStatusMaxValue"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeExpectStatusRowStatus"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbePort"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeDescription"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeProtocolType"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeRouteMethod"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbePriority"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeState"))
)
if mibBuilder.loadTexts:
    cslbHealthMonServerProbesGroupRev1.setStatus("current")

cshMonSfarmrealserverProbeStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 2, 2, 12)
)
cshMonSfarmrealserverProbeStatsGroup.setObjects(
      *(("CISCO-SLB-HEALTH-MON-MIB", "cshMonSfarmRealProbesPassed"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cshMonSfarmRealProbesFailed"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cshMonSfarmRealProbeHealthMonState"))
)
if mibBuilder.loadTexts:
    cshMonSfarmrealserverProbeStatsGroup.setStatus("deprecated")

cshMonSfarmrealserverProbeStatsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 2, 2, 13)
)
cshMonSfarmrealserverProbeStatsGroupRev1.setObjects(
      *(("CISCO-SLB-HEALTH-MON-MIB", "cshMonServerfarmRealPassedProbes"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cshMonServerfarmRealFailedProbes"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cshMonServerfarmRealProbeHealthMonState"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cshMonServerfarmRealProbeLastProbeTime"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cshMonServerfarmRealProbeLastActiveTime"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cshMonServerfarmRealProbeLastFailedTime"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cshMonProbeInheritedPortType"))
)
if mibBuilder.loadTexts:
    cshMonSfarmrealserverProbeStatsGroupRev1.setStatus("current")

cshMonProbeTypeStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 2, 2, 14)
)
cshMonProbeTypeStatsGroup.setObjects(
      *(("CISCO-SLB-HEALTH-MON-MIB", "cshMonProbeTotalSentProbes"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cshMonProbeTotalPassedProbes"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cshMonProbeTotalConnectionErrors"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cshMonProbeTotalReceivedRSTs"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cshMonProbeTotalReceiveTimeouts"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cshMonProbeTotalSendFailures"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cshMonProbeTotalFailedProbes"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cshMonProbeTotalRefusedConns"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cshMonProbeTotalOpenTimeouts"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cshMonProbeTotalActiveSockets"))
)
if mibBuilder.loadTexts:
    cshMonProbeTypeStatsGroup.setStatus("current")

cshMonNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 2, 2, 15)
)
cshMonNotifObjectsGroup.setObjects(
    ("CISCO-SLB-HEALTH-MON-MIB", "cshMonSocketOverusageCount")
)
if mibBuilder.loadTexts:
    cshMonNotifObjectsGroup.setStatus("current")


# Notification objects

cshMonSocketOveruse = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 0, 1)
)
cshMonSocketOveruse.setObjects(
    ("CISCO-SLB-HEALTH-MON-MIB", "cshMonSocketOverusageCount")
)
if mibBuilder.loadTexts:
    cshMonSocketOveruse.setStatus(
        "current"
    )

cshMonSocketNormalUse = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 0, 2)
)
cshMonSocketNormalUse.setObjects(
    ("CISCO-SLB-HEALTH-MON-MIB", "cshMonSocketOverusageCount")
)
if mibBuilder.loadTexts:
    cshMonSocketNormalUse.setStatus(
        "current"
    )


# Notifications groups

cshMonNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 2, 2, 16)
)
cshMonNotifGroup.setObjects(
      *(("CISCO-SLB-HEALTH-MON-MIB", "cshMonSocketOveruse"),
        ("CISCO-SLB-HEALTH-MON-MIB", "cshMonSocketNormalUse"))
)
if mibBuilder.loadTexts:
    cshMonNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoSlbHealthMonMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSlbHealthMonMIBCompliance.setStatus(
        "deprecated"
    )

ciscoSlbHealthMonMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoSlbHealthMonMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoSlbHealthMonMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoSlbHealthMonMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoSlbHealthMonMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 508, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoSlbHealthMonMIBComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SLB-HEALTH-MON-MIB",
    **{"SlbProbeType": SlbProbeType,
       "CiscoProbeHealthMonState": CiscoProbeHealthMonState,
       "CiscoProbeInheritedPortType": CiscoProbeInheritedPortType,
       "cslbxProbeCfgTable": cslbxProbeCfgTable,
       "cslbxProbeCfgEntry": cslbxProbeCfgEntry,
       "cslbxProbeName": cslbxProbeName,
       "cslbxProbeType": cslbxProbeType,
       "cslbxProbeInterval": cslbxProbeInterval,
       "cslbxProbeRetries": cslbxProbeRetries,
       "cslbxProbeFailedInterval": cslbxProbeFailedInterval,
       "cslbxProbeReceiveTimeout": cslbxProbeReceiveTimeout,
       "cslbxProbeTcpOpenTimeout": cslbxProbeTcpOpenTimeout,
       "cslbxProbeAlternateDestAddrType": cslbxProbeAlternateDestAddrType,
       "cslbxProbeAlternateDestAddr": cslbxProbeAlternateDestAddr,
       "cslbxProbeDnsDomainName": cslbxProbeDnsDomainName,
       "cslbxProbeHttpRequestMethod": cslbxProbeHttpRequestMethod,
       "cslbxProbeHttpRequestUrl": cslbxProbeHttpRequestUrl,
       "cslbxProbeRowStatus": cslbxProbeRowStatus,
       "cslbxProbeScriptName": cslbxProbeScriptName,
       "cslbxProbeScriptArguments": cslbxProbeScriptArguments,
       "cslbxProbePort": cslbxProbePort,
       "cslbxProbeDescription": cslbxProbeDescription,
       "cslbxProbeRouteMethod": cslbxProbeRouteMethod,
       "cslbxProbeProtocolType": cslbxProbeProtocolType,
       "cslbxProbePassCount": cslbxProbePassCount,
       "cslbxProbePriority": cslbxProbePriority,
       "cslbxProbeUserName": cslbxProbeUserName,
       "cslbxProbePassword": cslbxProbePassword,
       "cslbxProbeConnTermination": cslbxProbeConnTermination,
       "cslbxProbeSocketReuse": cslbxProbeSocketReuse,
       "cslbxProbeSendDataType": cslbxProbeSendDataType,
       "cslbxProbeSendData": cslbxProbeSendData,
       "cslbxProbeState": cslbxProbeState,
       "cslbxDnsProbeIpTable": cslbxDnsProbeIpTable,
       "cslbxDnsProbeIpEntry": cslbxDnsProbeIpEntry,
       "cslbxDnsProbeIpProbeName": cslbxDnsProbeIpProbeName,
       "cslbxDnsProbeIpAddressType": cslbxDnsProbeIpAddressType,
       "cslbxDnsProbeIpAddress": cslbxDnsProbeIpAddress,
       "cslbxDnsProbeIpRowStatus": cslbxDnsProbeIpRowStatus,
       "cslbxProbeHeaderCfgTable": cslbxProbeHeaderCfgTable,
       "cslbxProbeHeaderCfgEntry": cslbxProbeHeaderCfgEntry,
       "cslbxProbeHeaderProbeName": cslbxProbeHeaderProbeName,
       "cslbxProbeHeaderFieldName": cslbxProbeHeaderFieldName,
       "cslbxProbeHeaderFieldValue": cslbxProbeHeaderFieldValue,
       "cslbxProbeHeaderRowStatus": cslbxProbeHeaderRowStatus,
       "cslbxProbeExpectStatusCfgTable": cslbxProbeExpectStatusCfgTable,
       "cslbxProbeExpectStatusCfgEntry": cslbxProbeExpectStatusCfgEntry,
       "cslbxProbeExpectStatusProbeName": cslbxProbeExpectStatusProbeName,
       "cslbxProbeExpectStatusMinValue": cslbxProbeExpectStatusMinValue,
       "cslbxProbeExpectStatusMaxValue": cslbxProbeExpectStatusMaxValue,
       "cslbxProbeExpectStatusRowStatus": cslbxProbeExpectStatusRowStatus,
       "cslbxProbeHTTPCfgTable": cslbxProbeHTTPCfgTable,
       "cslbxProbeHTTPCfgEntry": cslbxProbeHTTPCfgEntry,
       "cslbxProbeHTTPCfgVersion": cslbxProbeHTTPCfgVersion,
       "cslbxProbeHTTPCfgPersistence": cslbxProbeHTTPCfgPersistence,
       "cslbxProbeHTTPCfgHashValid": cslbxProbeHTTPCfgHashValid,
       "cslbxProbeHTTPCfgHashName": cslbxProbeHTTPCfgHashName,
       "cslbxProbeHTTPCfgCipherSuite": cslbxProbeHTTPCfgCipherSuite,
       "cslbxProbeHTTPCfgSslTlsVersion": cslbxProbeHTTPCfgSslTlsVersion,
       "cslbxProbeHTTPCfgSslSessionReuse": cslbxProbeHTTPCfgSslSessionReuse,
       "cslbxProbeHTTPSslTlsVersionSupported": cslbxProbeHTTPSslTlsVersionSupported,
       "cslbxProbeSIPCfgTable": cslbxProbeSIPCfgTable,
       "cslbxProbeSIPCfgEntry": cslbxProbeSIPCfgEntry,
       "cslbxProbeSIPRegAddress": cslbxProbeSIPRegAddress,
       "cslbxProbeFTPCfgTable": cslbxProbeFTPCfgTable,
       "cslbxProbeFTPCfgEntry": cslbxProbeFTPCfgEntry,
       "cslbxProbeFtpRequestMethod": cslbxProbeFtpRequestMethod,
       "cslbxProbeFtpRequestFileName": cslbxProbeFtpRequestFileName,
       "cslbxProbeFtpRequestFileType": cslbxProbeFtpRequestFileType,
       "cslbxProbeTFTPCfgTable": cslbxProbeTFTPCfgTable,
       "cslbxProbeTFTPCfgEntry": cslbxProbeTFTPCfgEntry,
       "cslbxProbeTftpRequestMethod": cslbxProbeTftpRequestMethod,
       "cslbxProbeTftpRequestFileName": cslbxProbeTftpRequestFileName,
       "cslbxProbeTftpRequestFileType": cslbxProbeTftpRequestFileType,
       "cslbxProbeIMAPCfgTable": cslbxProbeIMAPCfgTable,
       "cslbxProbeIMAPCfgEntry": cslbxProbeIMAPCfgEntry,
       "cslbxProbeIMAPMailBox": cslbxProbeIMAPMailBox,
       "cslbxProbeIMAPMethodName": cslbxProbeIMAPMethodName,
       "ciscoSlbHealthMonMIB": ciscoSlbHealthMonMIB,
       "ciscoSlbHealthMonMIBNotifs": ciscoSlbHealthMonMIBNotifs,
       "cshMonSocketOveruse": cshMonSocketOveruse,
       "cshMonSocketNormalUse": cshMonSocketNormalUse,
       "ciscoSlbHealthMonMIBObjects": ciscoSlbHealthMonMIBObjects,
       "cshMonSfarmProbes": cshMonSfarmProbes,
       "cshMonSfarmRealProbeStatsTable": cshMonSfarmRealProbeStatsTable,
       "cshMonSfarmRealProbeStatsEntry": cshMonSfarmRealProbeStatsEntry,
       "cshMonSfarmRealServerName": cshMonSfarmRealServerName,
       "cshMonSfarmRealServerPort": cshMonSfarmRealServerPort,
       "cshMonSfarmRealProbesPassed": cshMonSfarmRealProbesPassed,
       "cshMonSfarmRealProbesFailed": cshMonSfarmRealProbesFailed,
       "cshMonSfarmRealProbeHealthMonState": cshMonSfarmRealProbeHealthMonState,
       "cshMonProbeTypeStatsTable": cshMonProbeTypeStatsTable,
       "cshMonProbeTypeStatsEntry": cshMonProbeTypeStatsEntry,
       "cshMonProbeTotalSentProbes": cshMonProbeTotalSentProbes,
       "cshMonProbeTotalPassedProbes": cshMonProbeTotalPassedProbes,
       "cshMonProbeTotalConnectionErrors": cshMonProbeTotalConnectionErrors,
       "cshMonProbeTotalReceivedRSTs": cshMonProbeTotalReceivedRSTs,
       "cshMonProbeTotalReceiveTimeouts": cshMonProbeTotalReceiveTimeouts,
       "cshMonProbeTotalSendFailures": cshMonProbeTotalSendFailures,
       "cshMonProbeTotalFailedProbes": cshMonProbeTotalFailedProbes,
       "cshMonProbeTotalRefusedConns": cshMonProbeTotalRefusedConns,
       "cshMonProbeTotalOpenTimeouts": cshMonProbeTotalOpenTimeouts,
       "cshMonProbeTotalActiveSockets": cshMonProbeTotalActiveSockets,
       "cshMonServerfarmRealProbeStatsTable": cshMonServerfarmRealProbeStatsTable,
       "cshMonServerfarmRealProbeStatsEntry": cshMonServerfarmRealProbeStatsEntry,
       "cshMonServerfarmRealServerName": cshMonServerfarmRealServerName,
       "cshMonServerfarmRealServerPort": cshMonServerfarmRealServerPort,
       "cshMonProbeInheritedPort": cshMonProbeInheritedPort,
       "cshMonServerfarmRealPassedProbes": cshMonServerfarmRealPassedProbes,
       "cshMonServerfarmRealFailedProbes": cshMonServerfarmRealFailedProbes,
       "cshMonServerfarmRealProbeHealthMonState": cshMonServerfarmRealProbeHealthMonState,
       "cshMonServerfarmRealProbeLastProbeTime": cshMonServerfarmRealProbeLastProbeTime,
       "cshMonServerfarmRealProbeLastActiveTime": cshMonServerfarmRealProbeLastActiveTime,
       "cshMonServerfarmRealProbeLastFailedTime": cshMonServerfarmRealProbeLastFailedTime,
       "cshMonProbeInheritedPortType": cshMonProbeInheritedPortType,
       "ciscoSlbHealthMonNotifObjects": ciscoSlbHealthMonNotifObjects,
       "cshMonSocketOverusageCount": cshMonSocketOverusageCount,
       "ciscoSlbHealthMonMIBConformance": ciscoSlbHealthMonMIBConformance,
       "ciscoSlbHealthMonMIBCompliances": ciscoSlbHealthMonMIBCompliances,
       "ciscoSlbHealthMonMIBCompliance": ciscoSlbHealthMonMIBCompliance,
       "ciscoSlbHealthMonMIBComplianceRev1": ciscoSlbHealthMonMIBComplianceRev1,
       "ciscoSlbHealthMonMIBComplianceRev2": ciscoSlbHealthMonMIBComplianceRev2,
       "ciscoSlbHealthMonMIBComplianceRev3": ciscoSlbHealthMonMIBComplianceRev3,
       "ciscoSlbHealthMonMIBGroups": ciscoSlbHealthMonMIBGroups,
       "cslbHealthMonServerProbesGroup": cslbHealthMonServerProbesGroup,
       "cslbHealthMonProbeCfgExtGroup": cslbHealthMonProbeCfgExtGroup,
       "cslbHealthMonSIPProbesGroup": cslbHealthMonSIPProbesGroup,
       "cslbHealthMonFTPProbesGroup": cslbHealthMonFTPProbesGroup,
       "cslbHealthMonHTTPProbesCommmonGroup": cslbHealthMonHTTPProbesCommmonGroup,
       "cslbHealthMonHTTPSProbesGroup": cslbHealthMonHTTPSProbesGroup,
       "cslbHealthMonTFTPProbesGroup": cslbHealthMonTFTPProbesGroup,
       "cslbHealthMonIMAPProbesGroup": cslbHealthMonIMAPProbesGroup,
       "cslbHealthMonProbeScriptGroup": cslbHealthMonProbeScriptGroup,
       "cslbHealthMonHTTPSProbesGroupRev1": cslbHealthMonHTTPSProbesGroupRev1,
       "cslbHealthMonServerProbesGroupRev1": cslbHealthMonServerProbesGroupRev1,
       "cshMonSfarmrealserverProbeStatsGroup": cshMonSfarmrealserverProbeStatsGroup,
       "cshMonSfarmrealserverProbeStatsGroupRev1": cshMonSfarmrealserverProbeStatsGroupRev1,
       "cshMonProbeTypeStatsGroup": cshMonProbeTypeStatsGroup,
       "cshMonNotifObjectsGroup": cshMonNotifObjectsGroup,
       "cshMonNotifGroup": cshMonNotifGroup}
)
