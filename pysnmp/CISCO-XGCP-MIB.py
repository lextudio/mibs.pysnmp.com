# SNMP MIB module (CISCO-XGCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-XGCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:48 2024
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

(CCallControlProfileIndexOrZero,
 cmgwIndex) = mibBuilder.importSymbols(
    "CISCO-MEDIA-GATEWAY-MIB",
    "CCallControlProfileIndexOrZero",
    "cmgwIndex")

(CMgcGroupIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-MGC-MIB",
    "CMgcGroupIndexOrZero")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoPort,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoPort")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoXgcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 318)
)
ciscoXgcpMIB.setRevisions(
        ("2006-02-21 00:00",
         "2005-12-21 00:00",
         "2005-08-24 00:00",
         "2005-08-09 00:00",
         "2005-03-07 00:00",
         "2004-11-15 00:00",
         "2004-08-30 00:00",
         "2004-05-14 00:00",
         "2003-02-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CXgcpRetryMethod(Integer32, TextualConvention):
    status = "current"
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
        *(("neverResetTimer", 1),
          ("resetTimerForEndpoint", 4),
          ("resetTimerForNewAddr", 3),
          ("resetTimerForNewMgc", 2))
    )



class CXgcpCallEvent(Integer32, TextualConvention):
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
        *(("ack", 0),
          ("alert", 5),
          ("assocConf", 16),
          ("babblerAuditResp", 21),
          ("callConnect", 6),
          ("callDisconnect", 9),
          ("callHandoff", 20),
          ("callProceed", 10),
          ("confDestroy", 8),
          ("confReady", 7),
          ("createConn", 1),
          ("deleteConn", 2),
          ("dissocConf", 15),
          ("intEven", 14),
          ("mediaEvent", 13),
          ("modifyConn", 3),
          ("modifyDone", 17),
          ("notifyReq", 4),
          ("nse", 19),
          ("offHook", 11),
          ("onHook", 12),
          ("voiceModeDone", 18))
    )



# MIB Managed Objects in the order of their OIDs

_CXgcpNotifications_ObjectIdentity = ObjectIdentity
cXgcpNotifications = _CXgcpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 0)
)
_CXgcpObjects_ObjectIdentity = ObjectIdentity
cXgcpObjects = _CXgcpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1)
)
_CXgcpMgcCfg_ObjectIdentity = ObjectIdentity
cXgcpMgcCfg = _CXgcpMgcCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 1)
)
_CXgcpMgcConfigTable_Object = MibTable
cXgcpMgcConfigTable = _CXgcpMgcConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cXgcpMgcConfigTable.setStatus("current")
_CXgcpMgcConfigEntry_Object = MibTableRow
cXgcpMgcConfigEntry = _CXgcpMgcConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 1, 1, 1)
)
cXgcpMgcConfigEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
)
if mibBuilder.loadTexts:
    cXgcpMgcConfigEntry.setStatus("current")


class _CXgcpMgcConfigMgcGrpNum_Type(CMgcGroupIndexOrZero):
    """Custom type cXgcpMgcConfigMgcGrpNum based on CMgcGroupIndexOrZero"""
    defaultValue = 0


_CXgcpMgcConfigMgcGrpNum_Object = MibTableColumn
cXgcpMgcConfigMgcGrpNum = _CXgcpMgcConfigMgcGrpNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 1, 1, 1, 1),
    _CXgcpMgcConfigMgcGrpNum_Type()
)
cXgcpMgcConfigMgcGrpNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXgcpMgcConfigMgcGrpNum.setStatus("current")


class _CXgcpMgcConfigAddrType_Type(InetAddressType):
    """Custom type cXgcpMgcConfigAddrType based on InetAddressType"""


_CXgcpMgcConfigAddrType_Object = MibTableColumn
cXgcpMgcConfigAddrType = _CXgcpMgcConfigAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 1, 1, 1, 2),
    _CXgcpMgcConfigAddrType_Type()
)
cXgcpMgcConfigAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXgcpMgcConfigAddrType.setStatus("current")


class _CXgcpMgcConfigAddress_Type(InetAddress):
    """Custom type cXgcpMgcConfigAddress based on InetAddress"""
    defaultHexValue = "00000000"


_CXgcpMgcConfigAddress_Object = MibTableColumn
cXgcpMgcConfigAddress = _CXgcpMgcConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 1, 1, 1, 3),
    _CXgcpMgcConfigAddress_Type()
)
cXgcpMgcConfigAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXgcpMgcConfigAddress.setStatus("current")


class _CXgcpMgcConfigProtocolIndex_Type(Integer32):
    """Custom type cXgcpMgcConfigProtocolIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CXgcpMgcConfigProtocolIndex_Type.__name__ = "Integer32"
_CXgcpMgcConfigProtocolIndex_Object = MibTableColumn
cXgcpMgcConfigProtocolIndex = _CXgcpMgcConfigProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 1, 1, 1, 4),
    _CXgcpMgcConfigProtocolIndex_Type()
)
cXgcpMgcConfigProtocolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXgcpMgcConfigProtocolIndex.setStatus("current")


class _CXgcpMgcConfigGatewayUdpPort_Type(CiscoPort):
    """Custom type cXgcpMgcConfigGatewayUdpPort based on CiscoPort"""
    defaultValue = 2427


_CXgcpMgcConfigGatewayUdpPort_Object = MibTableColumn
cXgcpMgcConfigGatewayUdpPort = _CXgcpMgcConfigGatewayUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 1, 1, 1, 5),
    _CXgcpMgcConfigGatewayUdpPort_Type()
)
cXgcpMgcConfigGatewayUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpMgcConfigGatewayUdpPort.setStatus("current")
_CXgcpMediaGw_ObjectIdentity = ObjectIdentity
cXgcpMediaGw = _CXgcpMediaGw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2)
)
_CXgcpMediaGwTable_Object = MibTable
cXgcpMediaGwTable = _CXgcpMediaGwTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cXgcpMediaGwTable.setStatus("current")
_CXgcpMediaGwEntry_Object = MibTableRow
cXgcpMediaGwEntry = _CXgcpMediaGwEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1, 1)
)
cXgcpMediaGwEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
)
if mibBuilder.loadTexts:
    cXgcpMediaGwEntry.setStatus("current")


class _CXgcpMediaGwRequestTimeOut_Type(Integer32):
    """Custom type cXgcpMediaGwRequestTimeOut based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CXgcpMediaGwRequestTimeOut_Type.__name__ = "Integer32"
_CXgcpMediaGwRequestTimeOut_Object = MibTableColumn
cXgcpMediaGwRequestTimeOut = _CXgcpMediaGwRequestTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1, 1, 1),
    _CXgcpMediaGwRequestTimeOut_Type()
)
cXgcpMediaGwRequestTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXgcpMediaGwRequestTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    cXgcpMediaGwRequestTimeOut.setUnits("milliseconds")


class _CXgcpMediaGwRequestRetries_Type(Integer32):
    """Custom type cXgcpMediaGwRequestRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CXgcpMediaGwRequestRetries_Type.__name__ = "Integer32"
_CXgcpMediaGwRequestRetries_Object = MibTableColumn
cXgcpMediaGwRequestRetries = _CXgcpMediaGwRequestRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1, 1, 2),
    _CXgcpMediaGwRequestRetries_Type()
)
cXgcpMediaGwRequestRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXgcpMediaGwRequestRetries.setStatus("current")
if mibBuilder.loadTexts:
    cXgcpMediaGwRequestRetries.setUnits("times")
_CXgcpMediaGwRequestRetryMethod_Type = CXgcpRetryMethod
_CXgcpMediaGwRequestRetryMethod_Object = MibTableColumn
cXgcpMediaGwRequestRetryMethod = _CXgcpMediaGwRequestRetryMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1, 1, 3),
    _CXgcpMediaGwRequestRetryMethod_Type()
)
cXgcpMediaGwRequestRetryMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXgcpMediaGwRequestRetryMethod.setStatus("current")


class _CXgcpMediaGwMaxExpTimeout_Type(Integer32):
    """Custom type cXgcpMediaGwMaxExpTimeout based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_CXgcpMediaGwMaxExpTimeout_Type.__name__ = "Integer32"
_CXgcpMediaGwMaxExpTimeout_Object = MibTableColumn
cXgcpMediaGwMaxExpTimeout = _CXgcpMediaGwMaxExpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1, 1, 4),
    _CXgcpMediaGwMaxExpTimeout_Type()
)
cXgcpMediaGwMaxExpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXgcpMediaGwMaxExpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cXgcpMediaGwMaxExpTimeout.setUnits("milliseconds")


class _CXgcpMediaGwRestartMwd_Type(Integer32):
    """Custom type cXgcpMediaGwRestartMwd based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_CXgcpMediaGwRestartMwd_Type.__name__ = "Integer32"
_CXgcpMediaGwRestartMwd_Object = MibTableColumn
cXgcpMediaGwRestartMwd = _CXgcpMediaGwRestartMwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1, 1, 5),
    _CXgcpMediaGwRestartMwd_Type()
)
cXgcpMediaGwRestartMwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXgcpMediaGwRestartMwd.setStatus("current")
if mibBuilder.loadTexts:
    cXgcpMediaGwRestartMwd.setUnits("milliseconds")


class _CXgcpMediaGwRestartDelay_Type(Integer32):
    """Custom type cXgcpMediaGwRestartDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_CXgcpMediaGwRestartDelay_Type.__name__ = "Integer32"
_CXgcpMediaGwRestartDelay_Object = MibTableColumn
cXgcpMediaGwRestartDelay = _CXgcpMediaGwRestartDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1, 1, 6),
    _CXgcpMediaGwRestartDelay_Type()
)
cXgcpMediaGwRestartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXgcpMediaGwRestartDelay.setStatus("current")
if mibBuilder.loadTexts:
    cXgcpMediaGwRestartDelay.setUnits("seconds")


class _CXgcpMediaGwDefaultPackage_Type(Integer32):
    """Custom type cXgcpMediaGwDefaultPackage based on Integer32"""
    defaultValue = 2

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
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("packageA", 10),
          ("packageATM", 12),
          ("packageB", 20),
          ("packageBA", 24),
          ("packageD", 3),
          ("packageDC", 1),
          ("packageDT", 14),
          ("packageFM", 31),
          ("packageFXR", 23),
          ("packageG", 2),
          ("packageH", 7),
          ("packageIT", 18),
          ("packageL", 6),
          ("packageLCS", 29),
          ("packageM", 4),
          ("packageMD", 25),
          ("packageMDR", 22),
          ("packageMDSTE", 27),
          ("packageMO", 15),
          ("packageMS", 13),
          ("packageMT", 19),
          ("packageN", 9),
          ("packageNAS", 26),
          ("packagePRE", 28),
          ("packageR", 8),
          ("packageRES", 16),
          ("packageS", 11),
          ("packageSASDI", 17),
          ("packageSRTP", 30),
          ("packageSST", 21),
          ("packageT", 5))
    )


_CXgcpMediaGwDefaultPackage_Type.__name__ = "Integer32"
_CXgcpMediaGwDefaultPackage_Object = MibTableColumn
cXgcpMediaGwDefaultPackage = _CXgcpMediaGwDefaultPackage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1, 1, 7),
    _CXgcpMediaGwDefaultPackage_Type()
)
cXgcpMediaGwDefaultPackage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXgcpMediaGwDefaultPackage.setStatus("current")


class _CXgcpMediaGwSupportedPackages_Type(Bits):
    """Custom type cXgcpMediaGwSupportedPackages based on Bits"""
    namedValues = NamedValues(
        *(("notFound", 0),
          ("packageA", 10),
          ("packageATM", 12),
          ("packageB", 20),
          ("packageBA", 24),
          ("packageD", 3),
          ("packageDC", 1),
          ("packageDT", 14),
          ("packageFM", 31),
          ("packageFXR", 23),
          ("packageG", 2),
          ("packageH", 7),
          ("packageIT", 18),
          ("packageL", 6),
          ("packageLCS", 29),
          ("packageM", 4),
          ("packageMD", 25),
          ("packageMDR", 22),
          ("packageMDSTE", 27),
          ("packageMO", 15),
          ("packageMS", 13),
          ("packageMT", 19),
          ("packageN", 9),
          ("packageNAS", 26),
          ("packagePRE", 28),
          ("packageR", 8),
          ("packageRES", 16),
          ("packageS", 11),
          ("packageSASDI", 17),
          ("packageSRTP", 30),
          ("packageSST", 21),
          ("packageT", 5))
    )

_CXgcpMediaGwSupportedPackages_Type.__name__ = "Bits"
_CXgcpMediaGwSupportedPackages_Object = MibTableColumn
cXgcpMediaGwSupportedPackages = _CXgcpMediaGwSupportedPackages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1, 1, 8),
    _CXgcpMediaGwSupportedPackages_Type()
)
cXgcpMediaGwSupportedPackages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpMediaGwSupportedPackages.setStatus("current")


class _CXgcpMediaGwSimpleSdpEnabled_Type(TruthValue):
    """Custom type cXgcpMediaGwSimpleSdpEnabled based on TruthValue"""


_CXgcpMediaGwSimpleSdpEnabled_Object = MibTableColumn
cXgcpMediaGwSimpleSdpEnabled = _CXgcpMediaGwSimpleSdpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1, 1, 9),
    _CXgcpMediaGwSimpleSdpEnabled_Type()
)
cXgcpMediaGwSimpleSdpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXgcpMediaGwSimpleSdpEnabled.setStatus("current")


class _CXgcpMediaGwAckSdpEnabled_Type(TruthValue):
    """Custom type cXgcpMediaGwAckSdpEnabled based on TruthValue"""


_CXgcpMediaGwAckSdpEnabled_Object = MibTableColumn
cXgcpMediaGwAckSdpEnabled = _CXgcpMediaGwAckSdpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1, 1, 10),
    _CXgcpMediaGwAckSdpEnabled_Type()
)
cXgcpMediaGwAckSdpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXgcpMediaGwAckSdpEnabled.setStatus("current")


class _CXgcpMediaGwUndottedNotation_Type(TruthValue):
    """Custom type cXgcpMediaGwUndottedNotation based on TruthValue"""


_CXgcpMediaGwUndottedNotation_Object = MibTableColumn
cXgcpMediaGwUndottedNotation = _CXgcpMediaGwUndottedNotation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1, 1, 11),
    _CXgcpMediaGwUndottedNotation_Type()
)
cXgcpMediaGwUndottedNotation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXgcpMediaGwUndottedNotation.setStatus("current")


class _CXgcpMediaGwQuarantineProcess_Type(TruthValue):
    """Custom type cXgcpMediaGwQuarantineProcess based on TruthValue"""


_CXgcpMediaGwQuarantineProcess_Object = MibTableColumn
cXgcpMediaGwQuarantineProcess = _CXgcpMediaGwQuarantineProcess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1, 1, 12),
    _CXgcpMediaGwQuarantineProcess_Type()
)
cXgcpMediaGwQuarantineProcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXgcpMediaGwQuarantineProcess.setStatus("current")


class _CXgcpMediaGwQuarantineLoop_Type(TruthValue):
    """Custom type cXgcpMediaGwQuarantineLoop based on TruthValue"""


_CXgcpMediaGwQuarantineLoop_Object = MibTableColumn
cXgcpMediaGwQuarantineLoop = _CXgcpMediaGwQuarantineLoop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1, 1, 13),
    _CXgcpMediaGwQuarantineLoop_Type()
)
cXgcpMediaGwQuarantineLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXgcpMediaGwQuarantineLoop.setStatus("current")


class _CXgcpMediaGwQuarantinePersist_Type(TruthValue):
    """Custom type cXgcpMediaGwQuarantinePersist based on TruthValue"""


_CXgcpMediaGwQuarantinePersist_Object = MibTableColumn
cXgcpMediaGwQuarantinePersist = _CXgcpMediaGwQuarantinePersist_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1, 1, 14),
    _CXgcpMediaGwQuarantinePersist_Type()
)
cXgcpMediaGwQuarantinePersist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXgcpMediaGwQuarantinePersist.setStatus("current")


class _CXgcpMediaGwPiggybackMsg_Type(TruthValue):
    """Custom type cXgcpMediaGwPiggybackMsg based on TruthValue"""


_CXgcpMediaGwPiggybackMsg_Object = MibTableColumn
cXgcpMediaGwPiggybackMsg = _CXgcpMediaGwPiggybackMsg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1, 1, 15),
    _CXgcpMediaGwPiggybackMsg_Type()
)
cXgcpMediaGwPiggybackMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXgcpMediaGwPiggybackMsg.setStatus("current")


class _CXgcpMediaGwMaxMsgSize_Type(Integer32):
    """Custom type cXgcpMediaGwMaxMsgSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CXgcpMediaGwMaxMsgSize_Type.__name__ = "Integer32"
_CXgcpMediaGwMaxMsgSize_Object = MibTableColumn
cXgcpMediaGwMaxMsgSize = _CXgcpMediaGwMaxMsgSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1, 1, 16),
    _CXgcpMediaGwMaxMsgSize_Type()
)
cXgcpMediaGwMaxMsgSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXgcpMediaGwMaxMsgSize.setStatus("current")
if mibBuilder.loadTexts:
    cXgcpMediaGwMaxMsgSize.setUnits("bytes")
_CXgcpMediaGwLastFailMgcAddrType_Type = InetAddressType
_CXgcpMediaGwLastFailMgcAddrType_Object = MibTableColumn
cXgcpMediaGwLastFailMgcAddrType = _CXgcpMediaGwLastFailMgcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1, 1, 17),
    _CXgcpMediaGwLastFailMgcAddrType_Type()
)
cXgcpMediaGwLastFailMgcAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpMediaGwLastFailMgcAddrType.setStatus("current")
_CXgcpMediaGwLastFailMgcAddr_Type = InetAddress
_CXgcpMediaGwLastFailMgcAddr_Object = MibTableColumn
cXgcpMediaGwLastFailMgcAddr = _CXgcpMediaGwLastFailMgcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1, 1, 18),
    _CXgcpMediaGwLastFailMgcAddr_Type()
)
cXgcpMediaGwLastFailMgcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpMediaGwLastFailMgcAddr.setStatus("current")
_CXgcpMediaGwDtmfRelay_Type = TruthValue
_CXgcpMediaGwDtmfRelay_Object = MibTableColumn
cXgcpMediaGwDtmfRelay = _CXgcpMediaGwDtmfRelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1, 1, 19),
    _CXgcpMediaGwDtmfRelay_Type()
)
cXgcpMediaGwDtmfRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXgcpMediaGwDtmfRelay.setStatus("current")


class _CXgcpMediaGwCaleaEnabled_Type(TruthValue):
    """Custom type cXgcpMediaGwCaleaEnabled based on TruthValue"""


_CXgcpMediaGwCaleaEnabled_Object = MibTableColumn
cXgcpMediaGwCaleaEnabled = _CXgcpMediaGwCaleaEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1, 1, 20),
    _CXgcpMediaGwCaleaEnabled_Type()
)
cXgcpMediaGwCaleaEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXgcpMediaGwCaleaEnabled.setStatus("current")


class _CXgcpMediaGwConfiguredPackages_Type(Bits):
    """Custom type cXgcpMediaGwConfiguredPackages based on Bits"""
    namedValues = NamedValues(
        *(("notFound", 0),
          ("packageA", 10),
          ("packageATM", 12),
          ("packageB", 20),
          ("packageBA", 24),
          ("packageD", 3),
          ("packageDC", 1),
          ("packageDT", 14),
          ("packageFM", 31),
          ("packageFXR", 23),
          ("packageG", 2),
          ("packageH", 7),
          ("packageIT", 18),
          ("packageL", 6),
          ("packageLCS", 29),
          ("packageM", 4),
          ("packageMD", 25),
          ("packageMDR", 22),
          ("packageMDSTE", 27),
          ("packageMO", 15),
          ("packageMS", 13),
          ("packageMT", 19),
          ("packageN", 9),
          ("packageNAS", 26),
          ("packagePRE", 28),
          ("packageR", 8),
          ("packageRES", 16),
          ("packageS", 11),
          ("packageSASDI", 17),
          ("packageSRTP", 30),
          ("packageSST", 21),
          ("packageT", 5))
    )

_CXgcpMediaGwConfiguredPackages_Type.__name__ = "Bits"
_CXgcpMediaGwConfiguredPackages_Object = MibTableColumn
cXgcpMediaGwConfiguredPackages = _CXgcpMediaGwConfiguredPackages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1, 1, 21),
    _CXgcpMediaGwConfiguredPackages_Type()
)
cXgcpMediaGwConfiguredPackages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXgcpMediaGwConfiguredPackages.setStatus("current")


class _CXgcpMediaGwConnOosRsipBehavior_Type(Integer32):
    """Custom type cXgcpMediaGwConnOosRsipBehavior based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rsipOnly", 2),
          ("sendDlcx", 1))
    )


_CXgcpMediaGwConnOosRsipBehavior_Type.__name__ = "Integer32"
_CXgcpMediaGwConnOosRsipBehavior_Object = MibTableColumn
cXgcpMediaGwConnOosRsipBehavior = _CXgcpMediaGwConnOosRsipBehavior_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1, 1, 22),
    _CXgcpMediaGwConnOosRsipBehavior_Type()
)
cXgcpMediaGwConnOosRsipBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXgcpMediaGwConnOosRsipBehavior.setStatus("current")


class _CXgcpMediaGwLongDurTimer_Type(Integer32):
    """Custom type cXgcpMediaGwLongDurTimer based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_CXgcpMediaGwLongDurTimer_Type.__name__ = "Integer32"
_CXgcpMediaGwLongDurTimer_Object = MibTableColumn
cXgcpMediaGwLongDurTimer = _CXgcpMediaGwLongDurTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1, 1, 23),
    _CXgcpMediaGwLongDurTimer_Type()
)
cXgcpMediaGwLongDurTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXgcpMediaGwLongDurTimer.setStatus("current")
if mibBuilder.loadTexts:
    cXgcpMediaGwLongDurTimer.setUnits("seconds")


class _CXgcpMediaGwProfile_Type(CCallControlProfileIndexOrZero):
    """Custom type cXgcpMediaGwProfile based on CCallControlProfileIndexOrZero"""
    defaultValue = 0


_CXgcpMediaGwProfile_Object = MibTableColumn
cXgcpMediaGwProfile = _CXgcpMediaGwProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1, 1, 24),
    _CXgcpMediaGwProfile_Type()
)
cXgcpMediaGwProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXgcpMediaGwProfile.setStatus("current")


class _CXgcpMediaGwAnnexabSdpEnabled_Type(TruthValue):
    """Custom type cXgcpMediaGwAnnexabSdpEnabled based on TruthValue"""


_CXgcpMediaGwAnnexabSdpEnabled_Object = MibTableColumn
cXgcpMediaGwAnnexabSdpEnabled = _CXgcpMediaGwAnnexabSdpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 2, 1, 1, 25),
    _CXgcpMediaGwAnnexabSdpEnabled_Type()
)
cXgcpMediaGwAnnexabSdpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXgcpMediaGwAnnexabSdpEnabled.setStatus("current")
_CXgcpStats_ObjectIdentity = ObjectIdentity
cXgcpStats = _CXgcpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3)
)
_CXgcpMsgStatsTable_Object = MibTable
cXgcpMsgStatsTable = _CXgcpMsgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cXgcpMsgStatsTable.setStatus("current")
_CXgcpMsgStatsEntry_Object = MibTableRow
cXgcpMsgStatsEntry = _CXgcpMsgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 1, 1)
)
cXgcpMsgStatsEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-XGCP-MIB", "cXgcpMsgStatsIndex"),
)
if mibBuilder.loadTexts:
    cXgcpMsgStatsEntry.setStatus("current")


class _CXgcpMsgStatsIndex_Type(Integer32):
    """Custom type cXgcpMsgStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CXgcpMsgStatsIndex_Type.__name__ = "Integer32"
_CXgcpMsgStatsIndex_Object = MibTableColumn
cXgcpMsgStatsIndex = _CXgcpMsgStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 1, 1, 1),
    _CXgcpMsgStatsIndex_Type()
)
cXgcpMsgStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cXgcpMsgStatsIndex.setStatus("current")
_CXgcpMsgStatsMgcIPAddressType_Type = InetAddressType
_CXgcpMsgStatsMgcIPAddressType_Object = MibTableColumn
cXgcpMsgStatsMgcIPAddressType = _CXgcpMsgStatsMgcIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 1, 1, 2),
    _CXgcpMsgStatsMgcIPAddressType_Type()
)
cXgcpMsgStatsMgcIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpMsgStatsMgcIPAddressType.setStatus("current")
_CXgcpMsgStatsMgcIPAddress_Type = InetAddress
_CXgcpMsgStatsMgcIPAddress_Object = MibTableColumn
cXgcpMsgStatsMgcIPAddress = _CXgcpMsgStatsMgcIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 1, 1, 3),
    _CXgcpMsgStatsMgcIPAddress_Type()
)
cXgcpMsgStatsMgcIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpMsgStatsMgcIPAddress.setStatus("current")
_CXgcpMsgStatsSuccessMessages_Type = Counter32
_CXgcpMsgStatsSuccessMessages_Object = MibTableColumn
cXgcpMsgStatsSuccessMessages = _CXgcpMsgStatsSuccessMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 1, 1, 4),
    _CXgcpMsgStatsSuccessMessages_Type()
)
cXgcpMsgStatsSuccessMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpMsgStatsSuccessMessages.setStatus("current")
_CXgcpMsgStatsFailMessages_Type = Counter32
_CXgcpMsgStatsFailMessages_Object = MibTableColumn
cXgcpMsgStatsFailMessages = _CXgcpMsgStatsFailMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 1, 1, 5),
    _CXgcpMsgStatsFailMessages_Type()
)
cXgcpMsgStatsFailMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpMsgStatsFailMessages.setStatus("current")
_CXgcpMsgStatsIncompleteMessages_Type = Counter32
_CXgcpMsgStatsIncompleteMessages_Object = MibTableColumn
cXgcpMsgStatsIncompleteMessages = _CXgcpMsgStatsIncompleteMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 1, 1, 6),
    _CXgcpMsgStatsIncompleteMessages_Type()
)
cXgcpMsgStatsIncompleteMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpMsgStatsIncompleteMessages.setStatus("current")
_CXgcpStatsTable_Object = MibTable
cXgcpStatsTable = _CXgcpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cXgcpStatsTable.setStatus("current")
_CXgcpStatsEntry_Object = MibTableRow
cXgcpStatsEntry = _CXgcpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1)
)
cXgcpStatsEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
)
if mibBuilder.loadTexts:
    cXgcpStatsEntry.setStatus("current")
_CXgcpStatsUdpRxPkts_Type = Counter32
_CXgcpStatsUdpRxPkts_Object = MibTableColumn
cXgcpStatsUdpRxPkts = _CXgcpStatsUdpRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 1),
    _CXgcpStatsUdpRxPkts_Type()
)
cXgcpStatsUdpRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsUdpRxPkts.setStatus("current")
_CXgcpStatsUdpTxPkts_Type = Counter32
_CXgcpStatsUdpTxPkts_Object = MibTableColumn
cXgcpStatsUdpTxPkts = _CXgcpStatsUdpTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 2),
    _CXgcpStatsUdpTxPkts_Type()
)
cXgcpStatsUdpTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsUdpTxPkts.setStatus("current")
_CXgcpStatsUnRecRxPkts_Type = Counter32
_CXgcpStatsUnRecRxPkts_Object = MibTableColumn
cXgcpStatsUnRecRxPkts = _CXgcpStatsUnRecRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 3),
    _CXgcpStatsUnRecRxPkts_Type()
)
cXgcpStatsUnRecRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsUnRecRxPkts.setStatus("current")
_CXgcpStatsMsgParsingErrors_Type = Counter32
_CXgcpStatsMsgParsingErrors_Object = MibTableColumn
cXgcpStatsMsgParsingErrors = _CXgcpStatsMsgParsingErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 4),
    _CXgcpStatsMsgParsingErrors_Type()
)
cXgcpStatsMsgParsingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsMsgParsingErrors.setStatus("current")
_CXgcpStatsDupAckTxMsgs_Type = Counter32
_CXgcpStatsDupAckTxMsgs_Object = MibTableColumn
cXgcpStatsDupAckTxMsgs = _CXgcpStatsDupAckTxMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 5),
    _CXgcpStatsDupAckTxMsgs_Type()
)
cXgcpStatsDupAckTxMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsDupAckTxMsgs.setStatus("current")
_CXgcpStatsInvalidVerCount_Type = Counter32
_CXgcpStatsInvalidVerCount_Object = MibTableColumn
cXgcpStatsInvalidVerCount = _CXgcpStatsInvalidVerCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 6),
    _CXgcpStatsInvalidVerCount_Type()
)
cXgcpStatsInvalidVerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsInvalidVerCount.setStatus("current")
_CXgcpStatsUnknownMgcRxPkts_Type = Counter32
_CXgcpStatsUnknownMgcRxPkts_Object = MibTableColumn
cXgcpStatsUnknownMgcRxPkts = _CXgcpStatsUnknownMgcRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 7),
    _CXgcpStatsUnknownMgcRxPkts_Type()
)
cXgcpStatsUnknownMgcRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsUnknownMgcRxPkts.setStatus("current")
_CXgcpStatsAckTxMsgs_Type = Counter32
_CXgcpStatsAckTxMsgs_Object = MibTableColumn
cXgcpStatsAckTxMsgs = _CXgcpStatsAckTxMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 8),
    _CXgcpStatsAckTxMsgs_Type()
)
cXgcpStatsAckTxMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsAckTxMsgs.setStatus("current")
_CXgcpStatsNackTxMsgs_Type = Counter32
_CXgcpStatsNackTxMsgs_Object = MibTableColumn
cXgcpStatsNackTxMsgs = _CXgcpStatsNackTxMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 9),
    _CXgcpStatsNackTxMsgs_Type()
)
cXgcpStatsNackTxMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsNackTxMsgs.setStatus("current")
_CXgcpStatsAckRxMsgs_Type = Counter32
_CXgcpStatsAckRxMsgs_Object = MibTableColumn
cXgcpStatsAckRxMsgs = _CXgcpStatsAckRxMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 10),
    _CXgcpStatsAckRxMsgs_Type()
)
cXgcpStatsAckRxMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsAckRxMsgs.setStatus("current")
_CXgcpStatsNackRxMsgs_Type = Counter32
_CXgcpStatsNackRxMsgs_Object = MibTableColumn
cXgcpStatsNackRxMsgs = _CXgcpStatsNackRxMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 11),
    _CXgcpStatsNackRxMsgs_Type()
)
cXgcpStatsNackRxMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsNackRxMsgs.setStatus("current")
_CXgcpStatsRxCrcxs_Type = Counter32
_CXgcpStatsRxCrcxs_Object = MibTableColumn
cXgcpStatsRxCrcxs = _CXgcpStatsRxCrcxs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 12),
    _CXgcpStatsRxCrcxs_Type()
)
cXgcpStatsRxCrcxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsRxCrcxs.setStatus("current")
_CXgcpStatsRxSuccCrcxs_Type = Counter32
_CXgcpStatsRxSuccCrcxs_Object = MibTableColumn
cXgcpStatsRxSuccCrcxs = _CXgcpStatsRxSuccCrcxs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 13),
    _CXgcpStatsRxSuccCrcxs_Type()
)
cXgcpStatsRxSuccCrcxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsRxSuccCrcxs.setStatus("current")
_CXgcpStatsRxFailCrcxs_Type = Counter32
_CXgcpStatsRxFailCrcxs_Object = MibTableColumn
cXgcpStatsRxFailCrcxs = _CXgcpStatsRxFailCrcxs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 14),
    _CXgcpStatsRxFailCrcxs_Type()
)
cXgcpStatsRxFailCrcxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsRxFailCrcxs.setStatus("current")
_CXgcpStatsRxDlcxs_Type = Counter32
_CXgcpStatsRxDlcxs_Object = MibTableColumn
cXgcpStatsRxDlcxs = _CXgcpStatsRxDlcxs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 15),
    _CXgcpStatsRxDlcxs_Type()
)
cXgcpStatsRxDlcxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsRxDlcxs.setStatus("current")
_CXgcpStatsRxSuccDlcxs_Type = Counter32
_CXgcpStatsRxSuccDlcxs_Object = MibTableColumn
cXgcpStatsRxSuccDlcxs = _CXgcpStatsRxSuccDlcxs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 16),
    _CXgcpStatsRxSuccDlcxs_Type()
)
cXgcpStatsRxSuccDlcxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsRxSuccDlcxs.setStatus("current")
_CXgcpStatsRxFailDlcxs_Type = Counter32
_CXgcpStatsRxFailDlcxs_Object = MibTableColumn
cXgcpStatsRxFailDlcxs = _CXgcpStatsRxFailDlcxs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 17),
    _CXgcpStatsRxFailDlcxs_Type()
)
cXgcpStatsRxFailDlcxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsRxFailDlcxs.setStatus("current")
_CXgcpStatsTxDlcxs_Type = Counter32
_CXgcpStatsTxDlcxs_Object = MibTableColumn
cXgcpStatsTxDlcxs = _CXgcpStatsTxDlcxs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 18),
    _CXgcpStatsTxDlcxs_Type()
)
cXgcpStatsTxDlcxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsTxDlcxs.setStatus("current")
_CXgcpStatsTxSuccDlcxs_Type = Counter32
_CXgcpStatsTxSuccDlcxs_Object = MibTableColumn
cXgcpStatsTxSuccDlcxs = _CXgcpStatsTxSuccDlcxs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 19),
    _CXgcpStatsTxSuccDlcxs_Type()
)
cXgcpStatsTxSuccDlcxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsTxSuccDlcxs.setStatus("current")
_CXgcpStatsTxFailDlcxs_Type = Counter32
_CXgcpStatsTxFailDlcxs_Object = MibTableColumn
cXgcpStatsTxFailDlcxs = _CXgcpStatsTxFailDlcxs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 20),
    _CXgcpStatsTxFailDlcxs_Type()
)
cXgcpStatsTxFailDlcxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsTxFailDlcxs.setStatus("current")
_CXgcpStatsRxMdcxs_Type = Counter32
_CXgcpStatsRxMdcxs_Object = MibTableColumn
cXgcpStatsRxMdcxs = _CXgcpStatsRxMdcxs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 21),
    _CXgcpStatsRxMdcxs_Type()
)
cXgcpStatsRxMdcxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsRxMdcxs.setStatus("current")
_CXgcpStatsRxSuccMdcxs_Type = Counter32
_CXgcpStatsRxSuccMdcxs_Object = MibTableColumn
cXgcpStatsRxSuccMdcxs = _CXgcpStatsRxSuccMdcxs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 22),
    _CXgcpStatsRxSuccMdcxs_Type()
)
cXgcpStatsRxSuccMdcxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsRxSuccMdcxs.setStatus("current")
_CXgcpStatsRxFailMdcxs_Type = Counter32
_CXgcpStatsRxFailMdcxs_Object = MibTableColumn
cXgcpStatsRxFailMdcxs = _CXgcpStatsRxFailMdcxs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 23),
    _CXgcpStatsRxFailMdcxs_Type()
)
cXgcpStatsRxFailMdcxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsRxFailMdcxs.setStatus("current")
_CXgcpStatsRxRqnts_Type = Counter32
_CXgcpStatsRxRqnts_Object = MibTableColumn
cXgcpStatsRxRqnts = _CXgcpStatsRxRqnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 24),
    _CXgcpStatsRxRqnts_Type()
)
cXgcpStatsRxRqnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsRxRqnts.setStatus("current")
_CXgcpStatsRxSuccRqnts_Type = Counter32
_CXgcpStatsRxSuccRqnts_Object = MibTableColumn
cXgcpStatsRxSuccRqnts = _CXgcpStatsRxSuccRqnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 25),
    _CXgcpStatsRxSuccRqnts_Type()
)
cXgcpStatsRxSuccRqnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsRxSuccRqnts.setStatus("current")
_CXgcpStatsRxFailRqnts_Type = Counter32
_CXgcpStatsRxFailRqnts_Object = MibTableColumn
cXgcpStatsRxFailRqnts = _CXgcpStatsRxFailRqnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 26),
    _CXgcpStatsRxFailRqnts_Type()
)
cXgcpStatsRxFailRqnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsRxFailRqnts.setStatus("current")
_CXgcpStatsRxAucxs_Type = Counter32
_CXgcpStatsRxAucxs_Object = MibTableColumn
cXgcpStatsRxAucxs = _CXgcpStatsRxAucxs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 27),
    _CXgcpStatsRxAucxs_Type()
)
cXgcpStatsRxAucxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsRxAucxs.setStatus("current")
_CXgcpStatsRxSuccAucxs_Type = Counter32
_CXgcpStatsRxSuccAucxs_Object = MibTableColumn
cXgcpStatsRxSuccAucxs = _CXgcpStatsRxSuccAucxs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 28),
    _CXgcpStatsRxSuccAucxs_Type()
)
cXgcpStatsRxSuccAucxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsRxSuccAucxs.setStatus("current")
_CXgcpStatsRxFailAucxs_Type = Counter32
_CXgcpStatsRxFailAucxs_Object = MibTableColumn
cXgcpStatsRxFailAucxs = _CXgcpStatsRxFailAucxs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 29),
    _CXgcpStatsRxFailAucxs_Type()
)
cXgcpStatsRxFailAucxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsRxFailAucxs.setStatus("current")
_CXgcpStatsRxAueps_Type = Counter32
_CXgcpStatsRxAueps_Object = MibTableColumn
cXgcpStatsRxAueps = _CXgcpStatsRxAueps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 30),
    _CXgcpStatsRxAueps_Type()
)
cXgcpStatsRxAueps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsRxAueps.setStatus("current")
_CXgcpStatsRxSuccAueps_Type = Counter32
_CXgcpStatsRxSuccAueps_Object = MibTableColumn
cXgcpStatsRxSuccAueps = _CXgcpStatsRxSuccAueps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 31),
    _CXgcpStatsRxSuccAueps_Type()
)
cXgcpStatsRxSuccAueps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsRxSuccAueps.setStatus("current")
_CXgcpStatsRxFailAueps_Type = Counter32
_CXgcpStatsRxFailAueps_Object = MibTableColumn
cXgcpStatsRxFailAueps = _CXgcpStatsRxFailAueps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 32),
    _CXgcpStatsRxFailAueps_Type()
)
cXgcpStatsRxFailAueps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsRxFailAueps.setStatus("current")
_CXgcpStatsTxRsips_Type = Counter32
_CXgcpStatsTxRsips_Object = MibTableColumn
cXgcpStatsTxRsips = _CXgcpStatsTxRsips_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 33),
    _CXgcpStatsTxRsips_Type()
)
cXgcpStatsTxRsips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsTxRsips.setStatus("current")
_CXgcpStatsTxSuccRsips_Type = Counter32
_CXgcpStatsTxSuccRsips_Object = MibTableColumn
cXgcpStatsTxSuccRsips = _CXgcpStatsTxSuccRsips_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 34),
    _CXgcpStatsTxSuccRsips_Type()
)
cXgcpStatsTxSuccRsips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsTxSuccRsips.setStatus("current")
_CXgcpStatsTxFailRsips_Type = Counter32
_CXgcpStatsTxFailRsips_Object = MibTableColumn
cXgcpStatsTxFailRsips = _CXgcpStatsTxFailRsips_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 35),
    _CXgcpStatsTxFailRsips_Type()
)
cXgcpStatsTxFailRsips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsTxFailRsips.setStatus("current")
_CXgcpStatsTxNotifies_Type = Counter32
_CXgcpStatsTxNotifies_Object = MibTableColumn
cXgcpStatsTxNotifies = _CXgcpStatsTxNotifies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 36),
    _CXgcpStatsTxNotifies_Type()
)
cXgcpStatsTxNotifies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsTxNotifies.setStatus("current")
_CXgcpStatsTxSuccNotifies_Type = Counter32
_CXgcpStatsTxSuccNotifies_Object = MibTableColumn
cXgcpStatsTxSuccNotifies = _CXgcpStatsTxSuccNotifies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 37),
    _CXgcpStatsTxSuccNotifies_Type()
)
cXgcpStatsTxSuccNotifies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsTxSuccNotifies.setStatus("current")
_CXgcpStatsTxFailNotifies_Type = Counter32
_CXgcpStatsTxFailNotifies_Object = MibTableColumn
cXgcpStatsTxFailNotifies = _CXgcpStatsTxFailNotifies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 3, 2, 1, 38),
    _CXgcpStatsTxFailNotifies_Type()
)
cXgcpStatsTxFailNotifies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpStatsTxFailNotifies.setStatus("current")
_CXgcpConnection_ObjectIdentity = ObjectIdentity
cXgcpConnection = _CXgcpConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 4)
)
_CXgcpConnectionTable_Object = MibTable
cXgcpConnectionTable = _CXgcpConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cXgcpConnectionTable.setStatus("current")
_CXgcpConnectionEntry_Object = MibTableRow
cXgcpConnectionEntry = _CXgcpConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 4, 1, 1)
)
cXgcpConnectionEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-XGCP-MIB", "cXgcpConnId"),
)
if mibBuilder.loadTexts:
    cXgcpConnectionEntry.setStatus("current")


class _CXgcpConnId_Type(Unsigned32):
    """Custom type cXgcpConnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CXgcpConnId_Type.__name__ = "Unsigned32"
_CXgcpConnId_Object = MibTableColumn
cXgcpConnId = _CXgcpConnId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 4, 1, 1, 1),
    _CXgcpConnId_Type()
)
cXgcpConnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cXgcpConnId.setStatus("current")
_CXgcpConnEndPoint_Type = SnmpAdminString
_CXgcpConnEndPoint_Object = MibTableColumn
cXgcpConnEndPoint = _CXgcpConnEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 4, 1, 1, 2),
    _CXgcpConnEndPoint_Type()
)
cXgcpConnEndPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpConnEndPoint.setStatus("current")
_CXgcpConnCallId_Type = SnmpAdminString
_CXgcpConnCallId_Object = MibTableColumn
cXgcpConnCallId = _CXgcpConnCallId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 4, 1, 1, 3),
    _CXgcpConnCallId_Type()
)
cXgcpConnCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpConnCallId.setStatus("current")
_CXgcpConnLocalUdpPort_Type = CiscoPort
_CXgcpConnLocalUdpPort_Object = MibTableColumn
cXgcpConnLocalUdpPort = _CXgcpConnLocalUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 4, 1, 1, 4),
    _CXgcpConnLocalUdpPort_Type()
)
cXgcpConnLocalUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpConnLocalUdpPort.setStatus("current")
_CXgcpConnRemoteUdpPort_Type = CiscoPort
_CXgcpConnRemoteUdpPort_Object = MibTableColumn
cXgcpConnRemoteUdpPort = _CXgcpConnRemoteUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 4, 1, 1, 5),
    _CXgcpConnRemoteUdpPort_Type()
)
cXgcpConnRemoteUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpConnRemoteUdpPort.setStatus("current")


class _CXgcpConnMode_Type(Integer32):
    """Custom type cXgcpConnMode based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("conference", 10),
          ("contTest", 6),
          ("data", 7),
          ("inActive", 4),
          ("invalid", 0),
          ("loopBack", 5),
          ("netwLoop", 8),
          ("netwTest", 9),
          ("recvOnly", 2),
          ("sendOnly", 1),
          ("sendRecv", 3))
    )


_CXgcpConnMode_Type.__name__ = "Integer32"
_CXgcpConnMode_Object = MibTableColumn
cXgcpConnMode = _CXgcpConnMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 4, 1, 1, 6),
    _CXgcpConnMode_Type()
)
cXgcpConnMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpConnMode.setStatus("current")


class _CXgcpConnVccId_Type(Unsigned32):
    """Custom type cXgcpConnVccId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CXgcpConnVccId_Type.__name__ = "Unsigned32"
_CXgcpConnVccId_Object = MibTableColumn
cXgcpConnVccId = _CXgcpConnVccId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 4, 1, 1, 7),
    _CXgcpConnVccId_Type()
)
cXgcpConnVccId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpConnVccId.setStatus("current")


class _CXgcpConnChannelId_Type(Unsigned32):
    """Custom type cXgcpConnChannelId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CXgcpConnChannelId_Type.__name__ = "Unsigned32"
_CXgcpConnChannelId_Object = MibTableColumn
cXgcpConnChannelId = _CXgcpConnChannelId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 4, 1, 1, 8),
    _CXgcpConnChannelId_Type()
)
cXgcpConnChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpConnChannelId.setStatus("current")


class _CXgcpConnCallState_Type(Integer32):
    """Custom type cXgcpConnCallState based on Integer32"""
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
              25)
        )
    )
    namedValues = NamedValues(
        *(("active", 4),
          ("callLegsDissociated", 11),
          ("confDestroying", 5),
          ("confDestroyingInactive", 19),
          ("confDissociating", 10),
          ("confTest", 20),
          ("conferencing", 3),
          ("connecting", 2),
          ("connectingInactive", 18),
          ("disconnecting", 6),
          ("erroState", 17),
          ("handOver", 25),
          ("hpActive", 15),
          ("hpConferencing", 14),
          ("hpConnected", 13),
          ("hpConnecting", 12),
          ("idle", 0),
          ("inactive", 7),
          ("setting", 1),
          ("setupWait", 21),
          ("twcActive", 23),
          ("voiceActive", 9),
          ("voiceConnecting", 8),
          ("voipConfDestroy", 16),
          ("waitNseSent", 22),
          ("waitState", 24))
    )


_CXgcpConnCallState_Type.__name__ = "Integer32"
_CXgcpConnCallState_Object = MibTableColumn
cXgcpConnCallState = _CXgcpConnCallState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 4, 1, 1, 9),
    _CXgcpConnCallState_Type()
)
cXgcpConnCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpConnCallState.setStatus("current")


class _CXgcpConnCodec_Type(Integer32):
    """Custom type cXgcpConnCodec based on Integer32"""
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
              15,
              16,
              17,
              18,
              19,
              20,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              200)
        )
    )
    namedValues = NamedValues(
        *(("clearChannel", 128),
          ("codecUnknown", 200),
          ("g711alaw", 2),
          ("g711ulaw", 1),
          ("g723", 11),
          ("g7231HighRate", 12),
          ("g7231LowRate", 14),
          ("g7231aHighRate", 13),
          ("g7231aLowRate", 15),
          ("g726k16", 5),
          ("g726k24", 4),
          ("g726k32", 3),
          ("g728", 10),
          ("g729", 6),
          ("g729a", 7),
          ("g729ab", 20),
          ("g729b", 8),
          ("g729bLowComp", 9),
          ("gsmEnhancedFullRate", 18),
          ("gsmEnhancedHalfRate", 19),
          ("gsmFullRate", 16),
          ("gsmHalfRate", 17),
          ("mdsteModemRelay", 134),
          ("modemRelay", 133),
          ("notApplicable", 0),
          ("nse", 129),
          ("nte", 131),
          ("sse", 135),
          ("t38", 132),
          ("xnse", 130))
    )


_CXgcpConnCodec_Type.__name__ = "Integer32"
_CXgcpConnCodec_Object = MibTableColumn
cXgcpConnCodec = _CXgcpConnCodec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 4, 1, 1, 10),
    _CXgcpConnCodec_Type()
)
cXgcpConnCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpConnCodec.setStatus("current")
_CXgcpConnLastSuccEvent_Type = CXgcpCallEvent
_CXgcpConnLastSuccEvent_Object = MibTableColumn
cXgcpConnLastSuccEvent = _CXgcpConnLastSuccEvent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 4, 1, 1, 11),
    _CXgcpConnLastSuccEvent_Type()
)
cXgcpConnLastSuccEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpConnLastSuccEvent.setStatus("current")
_CXgcpConnLastSuccIntEvent_Type = CXgcpCallEvent
_CXgcpConnLastSuccIntEvent_Object = MibTableColumn
cXgcpConnLastSuccIntEvent = _CXgcpConnLastSuccIntEvent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 4, 1, 1, 12),
    _CXgcpConnLastSuccIntEvent_Type()
)
cXgcpConnLastSuccIntEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpConnLastSuccIntEvent.setStatus("current")
_CXgcpConnLastFailedEvent_Type = CXgcpCallEvent
_CXgcpConnLastFailedEvent_Object = MibTableColumn
cXgcpConnLastFailedEvent = _CXgcpConnLastFailedEvent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 4, 1, 1, 13),
    _CXgcpConnLastFailedEvent_Type()
)
cXgcpConnLastFailedEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpConnLastFailedEvent.setStatus("current")
_CXgcpConnLastReqEvent_Type = CXgcpCallEvent
_CXgcpConnLastReqEvent_Object = MibTableColumn
cXgcpConnLastReqEvent = _CXgcpConnLastReqEvent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 4, 1, 1, 14),
    _CXgcpConnLastReqEvent_Type()
)
cXgcpConnLastReqEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpConnLastReqEvent.setStatus("current")


class _CXgcpConnEventResult_Type(Integer32):
    """Custom type cXgcpConnEventResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
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
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              50,
              51,
              52,
              53,
              54,
              55,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              115,
              120,
              130,
              131,
              132,
              133,
              140,
              141,
              142,
              143,
              144,
              145,
              146)
        )
    )
    namedValues = NamedValues(
        *(("abnormalOnhook", 51),
          ("ackFailure", 13),
          ("callAlertFailure", 68),
          ("callCacFailure", 37),
          ("callContextFailure", 62),
          ("callDeleteFailure", 69),
          ("callDiscFailure", 66),
          ("callModifyFailure", 67),
          ("callPeerFailure", 63),
          ("callRecordReleased", 2),
          ("callSetupIndFailure", 61),
          ("callSetupReqFailure", 60),
          ("callUnknownFeature", 70),
          ("callVdbFailure", 32),
          ("callVoipCallFailure", 65),
          ("callVoxCallFailure", 64),
          ("codecNotMatched", 76),
          ("codecSpecInError", 104),
          ("confCreateFailure", 95),
          ("confDestroyFailure", 96),
          ("confRsrcError", 38),
          ("connRecordMissing", 34),
          ("cotDisableFailure", 55),
          ("cotFailure", 54),
          ("createAckFailure", 15),
          ("createAckMissing", 16),
          ("deferMsg", 112),
          ("deleteAckFailure", 17),
          ("deleteFailure", 14),
          ("digitsNotifyFailure", 75),
          ("digitsOverflow", 74),
          ("discOnWrongLeg", 120),
          ("duplicatedMsg", 12),
          ("embMdcxError", 109),
          ("endPointNotRdy", 35),
          ("glare", 78),
          ("gwRsrcNotAvailable", 39),
          ("ignoreCcapiEvent", 42),
          ("ignoreDigit", 73),
          ("invalidCallId", 10),
          ("invalidCcapiEvent", 41),
          ("invalidConnId", 11),
          ("invalidConnMode", 77),
          ("invalidCot", 53),
          ("invalidEndpoint", 98),
          ("invalidModemRelayParam", 142),
          ("invalidNseEvent", 100),
          ("invalidNsePayload", 107),
          ("invalidNteEvent", 130),
          ("invalidOffhook", 52),
          ("invalidOk", 1),
          ("invalidProtocolVer", 20),
          ("invalidSprtPayload", 145),
          ("invalidSsePayload", 140),
          ("invalidState", 19),
          ("invalidXcapXcpar", 144),
          ("mdcxLeg1Error", 110),
          ("mdcxLeg2Error", 111),
          ("mediaChangeFail", 106),
          ("mediaSpecUpsupported", 105),
          ("memResourceError", 36),
          ("modemRelayNotSupported", 143),
          ("noConferenceId", 94),
          ("noDigitMap", 72),
          ("normalOk", 0),
          ("notEnabledNteEvent", 131),
          ("notifyFailure", 18),
          ("nsePayloadNotAvail", 108),
          ("nseRcvdOnWrongLeg", 101),
          ("nteEventExecuteFail", 132),
          ("peerDisconnectFailure", 93),
          ("peerInWrongState", 92),
          ("peerMissing", 90),
          ("peerNotReady", 91),
          ("playToneFailure", 103),
          ("prevRtpPortLocked", 33),
          ("reqEventFailure", 40),
          ("sendNseFailure", 102),
          ("sendNteFailure", 133),
          ("signalFailure", 50),
          ("sprtPayloadNotAvailable", 146),
          ("ssePayloadNotAvailable", 141),
          ("tgwDown", 30),
          ("tgwNotReady", 31),
          ("transError", 115),
          ("unknownConnType", 97),
          ("upSupportedCodec", 71))
    )


_CXgcpConnEventResult_Type.__name__ = "Integer32"
_CXgcpConnEventResult_Object = MibTableColumn
cXgcpConnEventResult = _CXgcpConnEventResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 4, 1, 1, 15),
    _CXgcpConnEventResult_Type()
)
cXgcpConnEventResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpConnEventResult.setStatus("current")


class _CXgcpConnEncrSuite_Type(Integer32):
    """Custom type cXgcpConnEncrSuite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aes128Cm", 1),
          ("none", 0))
    )


_CXgcpConnEncrSuite_Type.__name__ = "Integer32"
_CXgcpConnEncrSuite_Object = MibTableColumn
cXgcpConnEncrSuite = _CXgcpConnEncrSuite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 1, 4, 1, 1, 16),
    _CXgcpConnEncrSuite_Type()
)
cXgcpConnEncrSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXgcpConnEncrSuite.setStatus("current")
_CXgcpMIBConformance_ObjectIdentity = ObjectIdentity
cXgcpMIBConformance = _CXgcpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 2)
)
_CXgcpMIBCompliances_ObjectIdentity = ObjectIdentity
cXgcpMIBCompliances = _CXgcpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 2, 1)
)
_CXgcpMIBGroups_ObjectIdentity = ObjectIdentity
cXgcpMIBGroups = _CXgcpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 2, 2)
)

# Managed Objects groups

cXgcpMgcConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 2, 2, 1)
)
cXgcpMgcConfigGroup.setObjects(
      *(("CISCO-XGCP-MIB", "cXgcpMgcConfigMgcGrpNum"),
        ("CISCO-XGCP-MIB", "cXgcpMgcConfigAddress"),
        ("CISCO-XGCP-MIB", "cXgcpMgcConfigAddrType"),
        ("CISCO-XGCP-MIB", "cXgcpMgcConfigProtocolIndex"),
        ("CISCO-XGCP-MIB", "cXgcpMgcConfigGatewayUdpPort"))
)
if mibBuilder.loadTexts:
    cXgcpMgcConfigGroup.setStatus("current")

cXgcpMediaGwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 2, 2, 2)
)
cXgcpMediaGwGroup.setObjects(
      *(("CISCO-XGCP-MIB", "cXgcpMediaGwRequestTimeOut"),
        ("CISCO-XGCP-MIB", "cXgcpMediaGwRequestRetries"),
        ("CISCO-XGCP-MIB", "cXgcpMediaGwRequestRetryMethod"),
        ("CISCO-XGCP-MIB", "cXgcpMediaGwMaxExpTimeout"),
        ("CISCO-XGCP-MIB", "cXgcpMediaGwRestartMwd"),
        ("CISCO-XGCP-MIB", "cXgcpMediaGwRestartDelay"),
        ("CISCO-XGCP-MIB", "cXgcpMediaGwDefaultPackage"),
        ("CISCO-XGCP-MIB", "cXgcpMediaGwSupportedPackages"),
        ("CISCO-XGCP-MIB", "cXgcpMediaGwSimpleSdpEnabled"),
        ("CISCO-XGCP-MIB", "cXgcpMediaGwAckSdpEnabled"),
        ("CISCO-XGCP-MIB", "cXgcpMediaGwUndottedNotation"),
        ("CISCO-XGCP-MIB", "cXgcpMediaGwQuarantineProcess"),
        ("CISCO-XGCP-MIB", "cXgcpMediaGwQuarantineLoop"),
        ("CISCO-XGCP-MIB", "cXgcpMediaGwQuarantinePersist"),
        ("CISCO-XGCP-MIB", "cXgcpMediaGwPiggybackMsg"),
        ("CISCO-XGCP-MIB", "cXgcpMediaGwMaxMsgSize"),
        ("CISCO-XGCP-MIB", "cXgcpMediaGwLastFailMgcAddrType"),
        ("CISCO-XGCP-MIB", "cXgcpMediaGwLastFailMgcAddr"),
        ("CISCO-XGCP-MIB", "cXgcpMediaGwDtmfRelay"),
        ("CISCO-XGCP-MIB", "cXgcpMediaGwCaleaEnabled"))
)
if mibBuilder.loadTexts:
    cXgcpMediaGwGroup.setStatus("current")

cXgcpMsgStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 2, 2, 3)
)
cXgcpMsgStatsGroup.setObjects(
      *(("CISCO-XGCP-MIB", "cXgcpMsgStatsMgcIPAddressType"),
        ("CISCO-XGCP-MIB", "cXgcpMsgStatsMgcIPAddress"),
        ("CISCO-XGCP-MIB", "cXgcpMsgStatsSuccessMessages"),
        ("CISCO-XGCP-MIB", "cXgcpMsgStatsFailMessages"),
        ("CISCO-XGCP-MIB", "cXgcpMsgStatsIncompleteMessages"))
)
if mibBuilder.loadTexts:
    cXgcpMsgStatsGroup.setStatus("current")

cXgcpMediaGwGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 2, 2, 4)
)
cXgcpMediaGwGroupSup1.setObjects(
      *(("CISCO-XGCP-MIB", "cXgcpMediaGwConfiguredPackages"),
        ("CISCO-XGCP-MIB", "cXgcpMediaGwConnOosRsipBehavior"),
        ("CISCO-XGCP-MIB", "cXgcpMediaGwLongDurTimer"),
        ("CISCO-XGCP-MIB", "cXgcpMediaGwProfile"))
)
if mibBuilder.loadTexts:
    cXgcpMediaGwGroupSup1.setStatus("deprecated")

cXgcpMediaGwGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 2, 2, 5)
)
cXgcpMediaGwGroupSup2.setObjects(
      *(("CISCO-XGCP-MIB", "cXgcpMediaGwConfiguredPackages"),
        ("CISCO-XGCP-MIB", "cXgcpMediaGwConnOosRsipBehavior"),
        ("CISCO-XGCP-MIB", "cXgcpMediaGwLongDurTimer"),
        ("CISCO-XGCP-MIB", "cXgcpMediaGwProfile"),
        ("CISCO-XGCP-MIB", "cXgcpMediaGwAnnexabSdpEnabled"))
)
if mibBuilder.loadTexts:
    cXgcpMediaGwGroupSup2.setStatus("current")

cXgcpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 2, 2, 6)
)
cXgcpStatsGroup.setObjects(
      *(("CISCO-XGCP-MIB", "cXgcpStatsUdpRxPkts"),
        ("CISCO-XGCP-MIB", "cXgcpStatsUdpTxPkts"),
        ("CISCO-XGCP-MIB", "cXgcpStatsUnRecRxPkts"),
        ("CISCO-XGCP-MIB", "cXgcpStatsMsgParsingErrors"),
        ("CISCO-XGCP-MIB", "cXgcpStatsDupAckTxMsgs"),
        ("CISCO-XGCP-MIB", "cXgcpStatsInvalidVerCount"),
        ("CISCO-XGCP-MIB", "cXgcpStatsUnknownMgcRxPkts"),
        ("CISCO-XGCP-MIB", "cXgcpStatsAckTxMsgs"),
        ("CISCO-XGCP-MIB", "cXgcpStatsNackTxMsgs"),
        ("CISCO-XGCP-MIB", "cXgcpStatsAckRxMsgs"),
        ("CISCO-XGCP-MIB", "cXgcpStatsNackRxMsgs"),
        ("CISCO-XGCP-MIB", "cXgcpStatsRxCrcxs"),
        ("CISCO-XGCP-MIB", "cXgcpStatsRxSuccCrcxs"),
        ("CISCO-XGCP-MIB", "cXgcpStatsRxFailCrcxs"),
        ("CISCO-XGCP-MIB", "cXgcpStatsRxDlcxs"),
        ("CISCO-XGCP-MIB", "cXgcpStatsRxSuccDlcxs"),
        ("CISCO-XGCP-MIB", "cXgcpStatsRxFailDlcxs"),
        ("CISCO-XGCP-MIB", "cXgcpStatsTxDlcxs"),
        ("CISCO-XGCP-MIB", "cXgcpStatsTxSuccDlcxs"),
        ("CISCO-XGCP-MIB", "cXgcpStatsTxFailDlcxs"),
        ("CISCO-XGCP-MIB", "cXgcpStatsRxMdcxs"),
        ("CISCO-XGCP-MIB", "cXgcpStatsRxSuccMdcxs"),
        ("CISCO-XGCP-MIB", "cXgcpStatsRxFailMdcxs"),
        ("CISCO-XGCP-MIB", "cXgcpStatsRxRqnts"),
        ("CISCO-XGCP-MIB", "cXgcpStatsRxSuccRqnts"),
        ("CISCO-XGCP-MIB", "cXgcpStatsRxFailRqnts"),
        ("CISCO-XGCP-MIB", "cXgcpStatsRxAucxs"),
        ("CISCO-XGCP-MIB", "cXgcpStatsRxSuccAucxs"),
        ("CISCO-XGCP-MIB", "cXgcpStatsRxFailAucxs"),
        ("CISCO-XGCP-MIB", "cXgcpStatsRxAueps"),
        ("CISCO-XGCP-MIB", "cXgcpStatsRxSuccAueps"),
        ("CISCO-XGCP-MIB", "cXgcpStatsRxFailAueps"),
        ("CISCO-XGCP-MIB", "cXgcpStatsTxRsips"),
        ("CISCO-XGCP-MIB", "cXgcpStatsTxSuccRsips"),
        ("CISCO-XGCP-MIB", "cXgcpStatsTxFailRsips"),
        ("CISCO-XGCP-MIB", "cXgcpStatsTxNotifies"),
        ("CISCO-XGCP-MIB", "cXgcpStatsTxSuccNotifies"),
        ("CISCO-XGCP-MIB", "cXgcpStatsTxFailNotifies"))
)
if mibBuilder.loadTexts:
    cXgcpStatsGroup.setStatus("current")

cXgcpConnectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 2, 2, 7)
)
cXgcpConnectionGroup.setObjects(
      *(("CISCO-XGCP-MIB", "cXgcpConnEndPoint"),
        ("CISCO-XGCP-MIB", "cXgcpConnCallId"),
        ("CISCO-XGCP-MIB", "cXgcpConnLocalUdpPort"),
        ("CISCO-XGCP-MIB", "cXgcpConnRemoteUdpPort"),
        ("CISCO-XGCP-MIB", "cXgcpConnMode"),
        ("CISCO-XGCP-MIB", "cXgcpConnVccId"),
        ("CISCO-XGCP-MIB", "cXgcpConnChannelId"),
        ("CISCO-XGCP-MIB", "cXgcpConnCallState"),
        ("CISCO-XGCP-MIB", "cXgcpConnCodec"),
        ("CISCO-XGCP-MIB", "cXgcpConnLastSuccEvent"),
        ("CISCO-XGCP-MIB", "cXgcpConnLastSuccIntEvent"),
        ("CISCO-XGCP-MIB", "cXgcpConnLastFailedEvent"),
        ("CISCO-XGCP-MIB", "cXgcpConnLastReqEvent"),
        ("CISCO-XGCP-MIB", "cXgcpConnEventResult"),
        ("CISCO-XGCP-MIB", "cXgcpConnEncrSuite"))
)
if mibBuilder.loadTexts:
    cXgcpConnectionGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoXgcpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoXgcpMIBCompliance.setStatus(
        "deprecated"
    )

ciscoXgcpMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoXgcpMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoXgcpMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoXgcpMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoXgcpMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 318, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoXgcpMIBComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-XGCP-MIB",
    **{"CXgcpRetryMethod": CXgcpRetryMethod,
       "CXgcpCallEvent": CXgcpCallEvent,
       "ciscoXgcpMIB": ciscoXgcpMIB,
       "cXgcpNotifications": cXgcpNotifications,
       "cXgcpObjects": cXgcpObjects,
       "cXgcpMgcCfg": cXgcpMgcCfg,
       "cXgcpMgcConfigTable": cXgcpMgcConfigTable,
       "cXgcpMgcConfigEntry": cXgcpMgcConfigEntry,
       "cXgcpMgcConfigMgcGrpNum": cXgcpMgcConfigMgcGrpNum,
       "cXgcpMgcConfigAddrType": cXgcpMgcConfigAddrType,
       "cXgcpMgcConfigAddress": cXgcpMgcConfigAddress,
       "cXgcpMgcConfigProtocolIndex": cXgcpMgcConfigProtocolIndex,
       "cXgcpMgcConfigGatewayUdpPort": cXgcpMgcConfigGatewayUdpPort,
       "cXgcpMediaGw": cXgcpMediaGw,
       "cXgcpMediaGwTable": cXgcpMediaGwTable,
       "cXgcpMediaGwEntry": cXgcpMediaGwEntry,
       "cXgcpMediaGwRequestTimeOut": cXgcpMediaGwRequestTimeOut,
       "cXgcpMediaGwRequestRetries": cXgcpMediaGwRequestRetries,
       "cXgcpMediaGwRequestRetryMethod": cXgcpMediaGwRequestRetryMethod,
       "cXgcpMediaGwMaxExpTimeout": cXgcpMediaGwMaxExpTimeout,
       "cXgcpMediaGwRestartMwd": cXgcpMediaGwRestartMwd,
       "cXgcpMediaGwRestartDelay": cXgcpMediaGwRestartDelay,
       "cXgcpMediaGwDefaultPackage": cXgcpMediaGwDefaultPackage,
       "cXgcpMediaGwSupportedPackages": cXgcpMediaGwSupportedPackages,
       "cXgcpMediaGwSimpleSdpEnabled": cXgcpMediaGwSimpleSdpEnabled,
       "cXgcpMediaGwAckSdpEnabled": cXgcpMediaGwAckSdpEnabled,
       "cXgcpMediaGwUndottedNotation": cXgcpMediaGwUndottedNotation,
       "cXgcpMediaGwQuarantineProcess": cXgcpMediaGwQuarantineProcess,
       "cXgcpMediaGwQuarantineLoop": cXgcpMediaGwQuarantineLoop,
       "cXgcpMediaGwQuarantinePersist": cXgcpMediaGwQuarantinePersist,
       "cXgcpMediaGwPiggybackMsg": cXgcpMediaGwPiggybackMsg,
       "cXgcpMediaGwMaxMsgSize": cXgcpMediaGwMaxMsgSize,
       "cXgcpMediaGwLastFailMgcAddrType": cXgcpMediaGwLastFailMgcAddrType,
       "cXgcpMediaGwLastFailMgcAddr": cXgcpMediaGwLastFailMgcAddr,
       "cXgcpMediaGwDtmfRelay": cXgcpMediaGwDtmfRelay,
       "cXgcpMediaGwCaleaEnabled": cXgcpMediaGwCaleaEnabled,
       "cXgcpMediaGwConfiguredPackages": cXgcpMediaGwConfiguredPackages,
       "cXgcpMediaGwConnOosRsipBehavior": cXgcpMediaGwConnOosRsipBehavior,
       "cXgcpMediaGwLongDurTimer": cXgcpMediaGwLongDurTimer,
       "cXgcpMediaGwProfile": cXgcpMediaGwProfile,
       "cXgcpMediaGwAnnexabSdpEnabled": cXgcpMediaGwAnnexabSdpEnabled,
       "cXgcpStats": cXgcpStats,
       "cXgcpMsgStatsTable": cXgcpMsgStatsTable,
       "cXgcpMsgStatsEntry": cXgcpMsgStatsEntry,
       "cXgcpMsgStatsIndex": cXgcpMsgStatsIndex,
       "cXgcpMsgStatsMgcIPAddressType": cXgcpMsgStatsMgcIPAddressType,
       "cXgcpMsgStatsMgcIPAddress": cXgcpMsgStatsMgcIPAddress,
       "cXgcpMsgStatsSuccessMessages": cXgcpMsgStatsSuccessMessages,
       "cXgcpMsgStatsFailMessages": cXgcpMsgStatsFailMessages,
       "cXgcpMsgStatsIncompleteMessages": cXgcpMsgStatsIncompleteMessages,
       "cXgcpStatsTable": cXgcpStatsTable,
       "cXgcpStatsEntry": cXgcpStatsEntry,
       "cXgcpStatsUdpRxPkts": cXgcpStatsUdpRxPkts,
       "cXgcpStatsUdpTxPkts": cXgcpStatsUdpTxPkts,
       "cXgcpStatsUnRecRxPkts": cXgcpStatsUnRecRxPkts,
       "cXgcpStatsMsgParsingErrors": cXgcpStatsMsgParsingErrors,
       "cXgcpStatsDupAckTxMsgs": cXgcpStatsDupAckTxMsgs,
       "cXgcpStatsInvalidVerCount": cXgcpStatsInvalidVerCount,
       "cXgcpStatsUnknownMgcRxPkts": cXgcpStatsUnknownMgcRxPkts,
       "cXgcpStatsAckTxMsgs": cXgcpStatsAckTxMsgs,
       "cXgcpStatsNackTxMsgs": cXgcpStatsNackTxMsgs,
       "cXgcpStatsAckRxMsgs": cXgcpStatsAckRxMsgs,
       "cXgcpStatsNackRxMsgs": cXgcpStatsNackRxMsgs,
       "cXgcpStatsRxCrcxs": cXgcpStatsRxCrcxs,
       "cXgcpStatsRxSuccCrcxs": cXgcpStatsRxSuccCrcxs,
       "cXgcpStatsRxFailCrcxs": cXgcpStatsRxFailCrcxs,
       "cXgcpStatsRxDlcxs": cXgcpStatsRxDlcxs,
       "cXgcpStatsRxSuccDlcxs": cXgcpStatsRxSuccDlcxs,
       "cXgcpStatsRxFailDlcxs": cXgcpStatsRxFailDlcxs,
       "cXgcpStatsTxDlcxs": cXgcpStatsTxDlcxs,
       "cXgcpStatsTxSuccDlcxs": cXgcpStatsTxSuccDlcxs,
       "cXgcpStatsTxFailDlcxs": cXgcpStatsTxFailDlcxs,
       "cXgcpStatsRxMdcxs": cXgcpStatsRxMdcxs,
       "cXgcpStatsRxSuccMdcxs": cXgcpStatsRxSuccMdcxs,
       "cXgcpStatsRxFailMdcxs": cXgcpStatsRxFailMdcxs,
       "cXgcpStatsRxRqnts": cXgcpStatsRxRqnts,
       "cXgcpStatsRxSuccRqnts": cXgcpStatsRxSuccRqnts,
       "cXgcpStatsRxFailRqnts": cXgcpStatsRxFailRqnts,
       "cXgcpStatsRxAucxs": cXgcpStatsRxAucxs,
       "cXgcpStatsRxSuccAucxs": cXgcpStatsRxSuccAucxs,
       "cXgcpStatsRxFailAucxs": cXgcpStatsRxFailAucxs,
       "cXgcpStatsRxAueps": cXgcpStatsRxAueps,
       "cXgcpStatsRxSuccAueps": cXgcpStatsRxSuccAueps,
       "cXgcpStatsRxFailAueps": cXgcpStatsRxFailAueps,
       "cXgcpStatsTxRsips": cXgcpStatsTxRsips,
       "cXgcpStatsTxSuccRsips": cXgcpStatsTxSuccRsips,
       "cXgcpStatsTxFailRsips": cXgcpStatsTxFailRsips,
       "cXgcpStatsTxNotifies": cXgcpStatsTxNotifies,
       "cXgcpStatsTxSuccNotifies": cXgcpStatsTxSuccNotifies,
       "cXgcpStatsTxFailNotifies": cXgcpStatsTxFailNotifies,
       "cXgcpConnection": cXgcpConnection,
       "cXgcpConnectionTable": cXgcpConnectionTable,
       "cXgcpConnectionEntry": cXgcpConnectionEntry,
       "cXgcpConnId": cXgcpConnId,
       "cXgcpConnEndPoint": cXgcpConnEndPoint,
       "cXgcpConnCallId": cXgcpConnCallId,
       "cXgcpConnLocalUdpPort": cXgcpConnLocalUdpPort,
       "cXgcpConnRemoteUdpPort": cXgcpConnRemoteUdpPort,
       "cXgcpConnMode": cXgcpConnMode,
       "cXgcpConnVccId": cXgcpConnVccId,
       "cXgcpConnChannelId": cXgcpConnChannelId,
       "cXgcpConnCallState": cXgcpConnCallState,
       "cXgcpConnCodec": cXgcpConnCodec,
       "cXgcpConnLastSuccEvent": cXgcpConnLastSuccEvent,
       "cXgcpConnLastSuccIntEvent": cXgcpConnLastSuccIntEvent,
       "cXgcpConnLastFailedEvent": cXgcpConnLastFailedEvent,
       "cXgcpConnLastReqEvent": cXgcpConnLastReqEvent,
       "cXgcpConnEventResult": cXgcpConnEventResult,
       "cXgcpConnEncrSuite": cXgcpConnEncrSuite,
       "cXgcpMIBConformance": cXgcpMIBConformance,
       "cXgcpMIBCompliances": cXgcpMIBCompliances,
       "ciscoXgcpMIBCompliance": ciscoXgcpMIBCompliance,
       "ciscoXgcpMIBComplianceRev1": ciscoXgcpMIBComplianceRev1,
       "ciscoXgcpMIBComplianceRev2": ciscoXgcpMIBComplianceRev2,
       "ciscoXgcpMIBComplianceRev3": ciscoXgcpMIBComplianceRev3,
       "cXgcpMIBGroups": cXgcpMIBGroups,
       "cXgcpMgcConfigGroup": cXgcpMgcConfigGroup,
       "cXgcpMediaGwGroup": cXgcpMediaGwGroup,
       "cXgcpMsgStatsGroup": cXgcpMsgStatsGroup,
       "cXgcpMediaGwGroupSup1": cXgcpMediaGwGroupSup1,
       "cXgcpMediaGwGroupSup2": cXgcpMediaGwGroupSup2,
       "cXgcpStatsGroup": cXgcpStatsGroup,
       "cXgcpConnectionGroup": cXgcpConnectionGroup}
)
