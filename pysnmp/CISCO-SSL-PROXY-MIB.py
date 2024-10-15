# SNMP MIB module (CISCO-SSL-PROXY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SSL-PROXY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:48 2024
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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoSslProxyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370)
)
ciscoSslProxyMIB.setRevisions(
        ("2012-09-18 00:00",
         "2009-09-22 00:00",
         "2003-10-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CspMIBNotifications_ObjectIdentity = ObjectIdentity
cspMIBNotifications = _CspMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 0)
)
_CspMIBObjects_ObjectIdentity = ObjectIdentity
cspMIBObjects = _CspMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1)
)
_CspGlobalConfig_ObjectIdentity = ObjectIdentity
cspGlobalConfig = _CspGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 1)
)


class _CspGcVersion_Type(SnmpAdminString):
    """Custom type cspGcVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CspGcVersion_Type.__name__ = "SnmpAdminString"
_CspGcVersion_Object = MibScalar
cspGcVersion = _CspGcVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 1, 1),
    _CspGcVersion_Type()
)
cspGcVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspGcVersion.setStatus("current")
_CspGcFIPSMode_Type = TruthValue
_CspGcFIPSMode_Object = MibScalar
cspGcFIPSMode = _CspGcFIPSMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 1, 2),
    _CspGcFIPSMode_Type()
)
cspGcFIPSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cspGcFIPSMode.setStatus("current")
_CspGcRSArc4128md5_Type = TruthValue
_CspGcRSArc4128md5_Object = MibScalar
cspGcRSArc4128md5 = _CspGcRSArc4128md5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 1, 3),
    _CspGcRSArc4128md5_Type()
)
cspGcRSArc4128md5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspGcRSArc4128md5.setStatus("current")
_CspGcRSArc4128sha_Type = TruthValue
_CspGcRSArc4128sha_Object = MibScalar
cspGcRSArc4128sha = _CspGcRSArc4128sha_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 1, 4),
    _CspGcRSArc4128sha_Type()
)
cspGcRSArc4128sha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspGcRSArc4128sha.setStatus("current")
_CspGcRSAdescbcsha_Type = TruthValue
_CspGcRSAdescbcsha_Object = MibScalar
cspGcRSAdescbcsha = _CspGcRSAdescbcsha_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 1, 5),
    _CspGcRSAdescbcsha_Type()
)
cspGcRSAdescbcsha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspGcRSAdescbcsha.setStatus("current")
_CspGcRSA3descbcsha_Type = TruthValue
_CspGcRSA3descbcsha_Object = MibScalar
cspGcRSA3descbcsha = _CspGcRSA3descbcsha_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 1, 6),
    _CspGcRSA3descbcsha_Type()
)
cspGcRSA3descbcsha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspGcRSA3descbcsha.setStatus("current")


class _CspGcNotifyProxyServOperStatus_Type(TruthValue):
    """Custom type cspGcNotifyProxyServOperStatus based on TruthValue"""


_CspGcNotifyProxyServOperStatus_Object = MibScalar
cspGcNotifyProxyServOperStatus = _CspGcNotifyProxyServOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 1, 7),
    _CspGcNotifyProxyServOperStatus_Type()
)
cspGcNotifyProxyServOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cspGcNotifyProxyServOperStatus.setStatus("current")


class _CspGcNotifyPSCertExpiring_Type(TruthValue):
    """Custom type cspGcNotifyPSCertExpiring based on TruthValue"""


_CspGcNotifyPSCertExpiring_Object = MibScalar
cspGcNotifyPSCertExpiring = _CspGcNotifyPSCertExpiring_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 1, 8),
    _CspGcNotifyPSCertExpiring_Type()
)
cspGcNotifyPSCertExpiring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cspGcNotifyPSCertExpiring.setStatus("current")


class _CspGcPSCertExpireInterval_Type(Integer32):
    """Custom type cspGcPSCertExpireInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 720),
    )


_CspGcPSCertExpireInterval_Type.__name__ = "Integer32"
_CspGcPSCertExpireInterval_Object = MibScalar
cspGcPSCertExpireInterval = _CspGcPSCertExpireInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 1, 9),
    _CspGcPSCertExpireInterval_Type()
)
cspGcPSCertExpireInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cspGcPSCertExpireInterval.setStatus("current")
if mibBuilder.loadTexts:
    cspGcPSCertExpireInterval.setUnits("hours")
_CspPsConfig_ObjectIdentity = ObjectIdentity
cspPsConfig = _CspPsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 2)
)
_CspPsTable_Object = MibTable
cspPsTable = _CspPsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cspPsTable.setStatus("current")
_CspPsEntry_Object = MibTableRow
cspPsEntry = _CspPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 2, 1, 1)
)
cspPsEntry.setIndexNames(
    (0, "CISCO-SSL-PROXY-MIB", "cspPsName"),
    (0, "CISCO-SSL-PROXY-MIB", "cspPsListIndex"),
)
if mibBuilder.loadTexts:
    cspPsEntry.setStatus("current")


class _CspPsName_Type(SnmpAdminString):
    """Custom type cspPsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CspPsName_Type.__name__ = "SnmpAdminString"
_CspPsName_Object = MibTableColumn
cspPsName = _CspPsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 2, 1, 1, 1),
    _CspPsName_Type()
)
cspPsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cspPsName.setStatus("current")


class _CspPsListIndex_Type(Integer32):
    """Custom type cspPsListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_CspPsListIndex_Type.__name__ = "Integer32"
_CspPsListIndex_Object = MibTableColumn
cspPsListIndex = _CspPsListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 2, 1, 1, 2),
    _CspPsListIndex_Type()
)
cspPsListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cspPsListIndex.setStatus("current")


class _CspPsServiceType_Type(Integer32):
    """Custom type cspPsServiceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 2),
          ("server", 1))
    )


_CspPsServiceType_Type.__name__ = "Integer32"
_CspPsServiceType_Object = MibTableColumn
cspPsServiceType = _CspPsServiceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 2, 1, 1, 3),
    _CspPsServiceType_Type()
)
cspPsServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspPsServiceType.setStatus("current")


class _CspPsVirtualAddressType_Type(InetAddressType):
    """Custom type cspPsVirtualAddressType based on InetAddressType"""


_CspPsVirtualAddressType_Object = MibTableColumn
cspPsVirtualAddressType = _CspPsVirtualAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 2, 1, 1, 4),
    _CspPsVirtualAddressType_Type()
)
cspPsVirtualAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspPsVirtualAddressType.setStatus("current")
_CspPsVirtualAddress_Type = InetAddress
_CspPsVirtualAddress_Object = MibTableColumn
cspPsVirtualAddress = _CspPsVirtualAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 2, 1, 1, 5),
    _CspPsVirtualAddress_Type()
)
cspPsVirtualAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspPsVirtualAddress.setStatus("current")
_CspPsVirtualPort_Type = CiscoPort
_CspPsVirtualPort_Object = MibTableColumn
cspPsVirtualPort = _CspPsVirtualPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 2, 1, 1, 6),
    _CspPsVirtualPort_Type()
)
cspPsVirtualPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspPsVirtualPort.setStatus("current")


class _CspPsServerAddressType_Type(InetAddressType):
    """Custom type cspPsServerAddressType based on InetAddressType"""


_CspPsServerAddressType_Object = MibTableColumn
cspPsServerAddressType = _CspPsServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 2, 1, 1, 7),
    _CspPsServerAddressType_Type()
)
cspPsServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspPsServerAddressType.setStatus("current")
_CspPsServerAddress_Type = InetAddress
_CspPsServerAddress_Object = MibTableColumn
cspPsServerAddress = _CspPsServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 2, 1, 1, 8),
    _CspPsServerAddress_Type()
)
cspPsServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspPsServerAddress.setStatus("current")
_CspPsServerPort_Type = CiscoPort
_CspPsServerPort_Object = MibTableColumn
cspPsServerPort = _CspPsServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 2, 1, 1, 9),
    _CspPsServerPort_Type()
)
cspPsServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspPsServerPort.setStatus("current")


class _CspPsAdminStatus_Type(Integer32):
    """Custom type cspPsAdminStatus based on Integer32"""
    defaultValue = 2

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


_CspPsAdminStatus_Type.__name__ = "Integer32"
_CspPsAdminStatus_Object = MibTableColumn
cspPsAdminStatus = _CspPsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 2, 1, 1, 10),
    _CspPsAdminStatus_Type()
)
cspPsAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspPsAdminStatus.setStatus("current")


class _CspPsOperStatus_Type(Integer32):
    """Custom type cspPsOperStatus based on Integer32"""
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


_CspPsOperStatus_Type.__name__ = "Integer32"
_CspPsOperStatus_Object = MibTableColumn
cspPsOperStatus = _CspPsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 2, 1, 1, 11),
    _CspPsOperStatus_Type()
)
cspPsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPsOperStatus.setStatus("current")


class _CspPsOperDownReason_Type(Integer32):
    """Custom type cspPsOperDownReason based on Integer32"""
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
        *(("certNotConfigured", 7),
          ("noCert", 6),
          ("noConnectivity", 3),
          ("noServerAddr", 5),
          ("noVirtualAddr", 4),
          ("notApplicable", 2),
          ("other", 1))
    )


_CspPsOperDownReason_Type.__name__ = "Integer32"
_CspPsOperDownReason_Object = MibTableColumn
cspPsOperDownReason = _CspPsOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 2, 1, 1, 12),
    _CspPsOperDownReason_Type()
)
cspPsOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPsOperDownReason.setStatus("current")
_CspPsConfigRowStatus_Type = RowStatus
_CspPsConfigRowStatus_Object = MibTableColumn
cspPsConfigRowStatus = _CspPsConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 2, 1, 1, 13),
    _CspPsConfigRowStatus_Type()
)
cspPsConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspPsConfigRowStatus.setStatus("current")
_CspPsPolicyConfig_ObjectIdentity = ObjectIdentity
cspPsPolicyConfig = _CspPsPolicyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 3)
)
_CspPsPolicyTable_Object = MibTable
cspPsPolicyTable = _CspPsPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cspPsPolicyTable.setStatus("current")
_CspPsPolicyEntry_Object = MibTableRow
cspPsPolicyEntry = _CspPsPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cspPsPolicyEntry.setStatus("current")


class _CspPspVirTcpPolicyName_Type(SnmpAdminString):
    """Custom type cspPspVirTcpPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CspPspVirTcpPolicyName_Type.__name__ = "SnmpAdminString"
_CspPspVirTcpPolicyName_Object = MibTableColumn
cspPspVirTcpPolicyName = _CspPspVirTcpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 3, 1, 1, 1),
    _CspPspVirTcpPolicyName_Type()
)
cspPspVirTcpPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspPspVirTcpPolicyName.setStatus("current")


class _CspPspSerTcpPolicyName_Type(SnmpAdminString):
    """Custom type cspPspSerTcpPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CspPspSerTcpPolicyName_Type.__name__ = "SnmpAdminString"
_CspPspSerTcpPolicyName_Object = MibTableColumn
cspPspSerTcpPolicyName = _CspPspSerTcpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 3, 1, 1, 2),
    _CspPspSerTcpPolicyName_Type()
)
cspPspSerTcpPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspPspSerTcpPolicyName.setStatus("current")


class _CspPspSslPolicyName_Type(SnmpAdminString):
    """Custom type cspPspSslPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CspPspSslPolicyName_Type.__name__ = "SnmpAdminString"
_CspPspSslPolicyName_Object = MibTableColumn
cspPspSslPolicyName = _CspPspSslPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 3, 1, 1, 3),
    _CspPspSslPolicyName_Type()
)
cspPspSslPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspPspSslPolicyName.setStatus("current")


class _CspPspHttpHdrPolicyName_Type(SnmpAdminString):
    """Custom type cspPspHttpHdrPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CspPspHttpHdrPolicyName_Type.__name__ = "SnmpAdminString"
_CspPspHttpHdrPolicyName_Object = MibTableColumn
cspPspHttpHdrPolicyName = _CspPspHttpHdrPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 3, 1, 1, 4),
    _CspPspHttpHdrPolicyName_Type()
)
cspPspHttpHdrPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspPspHttpHdrPolicyName.setStatus("current")


class _CspPspUrlRewritePolicyName_Type(SnmpAdminString):
    """Custom type cspPspUrlRewritePolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CspPspUrlRewritePolicyName_Type.__name__ = "SnmpAdminString"
_CspPspUrlRewritePolicyName_Object = MibTableColumn
cspPspUrlRewritePolicyName = _CspPspUrlRewritePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 3, 1, 1, 5),
    _CspPspUrlRewritePolicyName_Type()
)
cspPspUrlRewritePolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspPspUrlRewritePolicyName.setStatus("current")
_CspPsKeyCertConfig_ObjectIdentity = ObjectIdentity
cspPsKeyCertConfig = _CspPsKeyCertConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 4)
)
_CspPsKeyCertTable_Object = MibTable
cspPsKeyCertTable = _CspPsKeyCertTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cspPsKeyCertTable.setStatus("current")
_CspPsKeyCertEntry_Object = MibTableRow
cspPsKeyCertEntry = _CspPsKeyCertEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 4, 1, 1)
)
cspPsKeyCertEntry.setIndexNames(
    (0, "CISCO-SSL-PROXY-MIB", "cspPsName"),
    (0, "CISCO-SSL-PROXY-MIB", "cspPsListIndex"),
    (0, "CISCO-SSL-PROXY-MIB", "cspPskcKeyUsage"),
)
if mibBuilder.loadTexts:
    cspPsKeyCertEntry.setStatus("current")


class _CspPskcKeyUsage_Type(Integer32):
    """Custom type cspPskcKeyUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rsaEncryption", 2),
          ("rsaGeneralPurpose", 3),
          ("rsaSigning", 1))
    )


_CspPskcKeyUsage_Type.__name__ = "Integer32"
_CspPskcKeyUsage_Object = MibTableColumn
cspPskcKeyUsage = _CspPskcKeyUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 4, 1, 1, 1),
    _CspPskcKeyUsage_Type()
)
cspPskcKeyUsage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cspPskcKeyUsage.setStatus("current")


class _CspPskcTrustPointName_Type(SnmpAdminString):
    """Custom type cspPskcTrustPointName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CspPskcTrustPointName_Type.__name__ = "SnmpAdminString"
_CspPskcTrustPointName_Object = MibTableColumn
cspPskcTrustPointName = _CspPskcTrustPointName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 4, 1, 1, 2),
    _CspPskcTrustPointName_Type()
)
cspPskcTrustPointName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspPskcTrustPointName.setStatus("current")


class _CspPskcCertFileName_Type(SnmpAdminString):
    """Custom type cspPskcCertFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CspPskcCertFileName_Type.__name__ = "SnmpAdminString"
_CspPskcCertFileName_Object = MibTableColumn
cspPskcCertFileName = _CspPskcCertFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 4, 1, 1, 3),
    _CspPskcCertFileName_Type()
)
cspPskcCertFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspPskcCertFileName.setStatus("current")


class _CspPskcKeyName_Type(SnmpAdminString):
    """Custom type cspPskcKeyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CspPskcKeyName_Type.__name__ = "SnmpAdminString"
_CspPskcKeyName_Object = MibTableColumn
cspPskcKeyName = _CspPskcKeyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 4, 1, 1, 4),
    _CspPskcKeyName_Type()
)
cspPskcKeyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspPskcKeyName.setStatus("current")


class _CspPskcKeyFileName_Type(SnmpAdminString):
    """Custom type cspPskcKeyFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CspPskcKeyFileName_Type.__name__ = "SnmpAdminString"
_CspPskcKeyFileName_Object = MibTableColumn
cspPskcKeyFileName = _CspPskcKeyFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 4, 1, 1, 5),
    _CspPskcKeyFileName_Type()
)
cspPskcKeyFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspPskcKeyFileName.setStatus("current")


class _CspPskcKeySize_Type(Integer32):
    """Custom type cspPskcKeySize based on Integer32"""
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
        *(("other", 1),
          ("rsa1024", 4),
          ("rsa1536", 5),
          ("rsa2048", 6),
          ("rsa512", 2),
          ("rsa768", 3))
    )


_CspPskcKeySize_Type.__name__ = "Integer32"
_CspPskcKeySize_Object = MibTableColumn
cspPskcKeySize = _CspPskcKeySize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 4, 1, 1, 6),
    _CspPskcKeySize_Type()
)
cspPskcKeySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPskcKeySize.setStatus("current")


class _CspPskcKeyTime_Type(SnmpAdminString):
    """Custom type cspPskcKeyTime based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CspPskcKeyTime_Type.__name__ = "SnmpAdminString"
_CspPskcKeyTime_Object = MibTableColumn
cspPskcKeyTime = _CspPskcKeyTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 4, 1, 1, 7),
    _CspPskcKeyTime_Type()
)
cspPskcKeyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPskcKeyTime.setStatus("current")


class _CspPskcCertStatus_Type(Integer32):
    """Custom type cspPskcCertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("expired", 2),
          ("rollover", 3),
          ("valid", 1))
    )


_CspPskcCertStatus_Type.__name__ = "Integer32"
_CspPskcCertStatus_Object = MibTableColumn
cspPskcCertStatus = _CspPskcCertStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 4, 1, 1, 8),
    _CspPskcCertStatus_Type()
)
cspPskcCertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPskcCertStatus.setStatus("current")


class _CspPskcCertSubjName_Type(SnmpAdminString):
    """Custom type cspPskcCertSubjName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CspPskcCertSubjName_Type.__name__ = "SnmpAdminString"
_CspPskcCertSubjName_Object = MibTableColumn
cspPskcCertSubjName = _CspPskcCertSubjName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 4, 1, 1, 9),
    _CspPskcCertSubjName_Type()
)
cspPskcCertSubjName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPskcCertSubjName.setStatus("current")


class _CspPskcCertSerialNum_Type(SnmpAdminString):
    """Custom type cspPskcCertSerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CspPskcCertSerialNum_Type.__name__ = "SnmpAdminString"
_CspPskcCertSerialNum_Object = MibTableColumn
cspPskcCertSerialNum = _CspPskcCertSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 4, 1, 1, 10),
    _CspPskcCertSerialNum_Type()
)
cspPskcCertSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPskcCertSerialNum.setStatus("current")


class _CspPskcIssuerName_Type(SnmpAdminString):
    """Custom type cspPskcIssuerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CspPskcIssuerName_Type.__name__ = "SnmpAdminString"
_CspPskcIssuerName_Object = MibTableColumn
cspPskcIssuerName = _CspPskcIssuerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 4, 1, 1, 11),
    _CspPskcIssuerName_Type()
)
cspPskcIssuerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPskcIssuerName.setStatus("current")


class _CspPskcIssuerCertSerialNum_Type(SnmpAdminString):
    """Custom type cspPskcIssuerCertSerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CspPskcIssuerCertSerialNum_Type.__name__ = "SnmpAdminString"
_CspPskcIssuerCertSerialNum_Object = MibTableColumn
cspPskcIssuerCertSerialNum = _CspPskcIssuerCertSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 4, 1, 1, 12),
    _CspPskcIssuerCertSerialNum_Type()
)
cspPskcIssuerCertSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPskcIssuerCertSerialNum.setStatus("current")


class _CspPskcCertStartDate_Type(SnmpAdminString):
    """Custom type cspPskcCertStartDate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CspPskcCertStartDate_Type.__name__ = "SnmpAdminString"
_CspPskcCertStartDate_Object = MibTableColumn
cspPskcCertStartDate = _CspPskcCertStartDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 4, 1, 1, 13),
    _CspPskcCertStartDate_Type()
)
cspPskcCertStartDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPskcCertStartDate.setStatus("current")


class _CspPskcCertEndDate_Type(SnmpAdminString):
    """Custom type cspPskcCertEndDate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CspPskcCertEndDate_Type.__name__ = "SnmpAdminString"
_CspPskcCertEndDate_Object = MibTableColumn
cspPskcCertEndDate = _CspPskcCertEndDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 4, 1, 1, 14),
    _CspPskcCertEndDate_Type()
)
cspPskcCertEndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPskcCertEndDate.setStatus("current")
_CspPskcConfigRowStatus_Type = RowStatus
_CspPskcConfigRowStatus_Object = MibTableColumn
cspPskcConfigRowStatus = _CspPskcConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 4, 1, 1, 15),
    _CspPskcConfigRowStatus_Type()
)
cspPskcConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspPskcConfigRowStatus.setStatus("current")
_CspTcpPolicyConfig_ObjectIdentity = ObjectIdentity
cspTcpPolicyConfig = _CspTcpPolicyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 5)
)
_CspTcpPolicyTable_Object = MibTable
cspTcpPolicyTable = _CspTcpPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cspTcpPolicyTable.setStatus("current")
_CspTcpPolicyEntry_Object = MibTableRow
cspTcpPolicyEntry = _CspTcpPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 5, 1, 1)
)
cspTcpPolicyEntry.setIndexNames(
    (0, "CISCO-SSL-PROXY-MIB", "cspTpPolicyName"),
)
if mibBuilder.loadTexts:
    cspTcpPolicyEntry.setStatus("current")


class _CspTpPolicyName_Type(SnmpAdminString):
    """Custom type cspTpPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CspTpPolicyName_Type.__name__ = "SnmpAdminString"
_CspTpPolicyName_Object = MibTableColumn
cspTpPolicyName = _CspTpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 5, 1, 1, 1),
    _CspTpPolicyName_Type()
)
cspTpPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cspTpPolicyName.setStatus("current")


class _CspTpSynTimeOut_Type(Integer32):
    """Custom type cspTpSynTimeOut based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CspTpSynTimeOut_Type.__name__ = "Integer32"
_CspTpSynTimeOut_Object = MibTableColumn
cspTpSynTimeOut = _CspTpSynTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 5, 1, 1, 2),
    _CspTpSynTimeOut_Type()
)
cspTpSynTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspTpSynTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    cspTpSynTimeOut.setUnits("seconds")


class _CspTpInActivityTimeOut_Type(Integer32):
    """Custom type cspTpInActivityTimeOut based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CspTpInActivityTimeOut_Type.__name__ = "Integer32"
_CspTpInActivityTimeOut_Object = MibTableColumn
cspTpInActivityTimeOut = _CspTpInActivityTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 5, 1, 1, 3),
    _CspTpInActivityTimeOut_Type()
)
cspTpInActivityTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspTpInActivityTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    cspTpInActivityTimeOut.setUnits("seconds")
_CspTpNagleAlgo_Type = TruthValue
_CspTpNagleAlgo_Object = MibTableColumn
cspTpNagleAlgo = _CspTpNagleAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 5, 1, 1, 4),
    _CspTpNagleAlgo_Type()
)
cspTpNagleAlgo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspTpNagleAlgo.setStatus("current")


class _CspTpFinWaitTimeOut_Type(Integer32):
    """Custom type cspTpFinWaitTimeOut based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CspTpFinWaitTimeOut_Type.__name__ = "Integer32"
_CspTpFinWaitTimeOut_Object = MibTableColumn
cspTpFinWaitTimeOut = _CspTpFinWaitTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 5, 1, 1, 5),
    _CspTpFinWaitTimeOut_Type()
)
cspTpFinWaitTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspTpFinWaitTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    cspTpFinWaitTimeOut.setUnits("seconds")


class _CspTpReassemTimeOut_Type(Integer32):
    """Custom type cspTpReassemTimeOut based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CspTpReassemTimeOut_Type.__name__ = "Integer32"
_CspTpReassemTimeOut_Object = MibTableColumn
cspTpReassemTimeOut = _CspTpReassemTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 5, 1, 1, 6),
    _CspTpReassemTimeOut_Type()
)
cspTpReassemTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspTpReassemTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    cspTpReassemTimeOut.setUnits("seconds")


class _CspTpRcvBufShrLim_Type(Integer32):
    """Custom type cspTpRcvBufShrLim based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8192, 262144),
    )


_CspTpRcvBufShrLim_Type.__name__ = "Integer32"
_CspTpRcvBufShrLim_Object = MibTableColumn
cspTpRcvBufShrLim = _CspTpRcvBufShrLim_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 5, 1, 1, 7),
    _CspTpRcvBufShrLim_Type()
)
cspTpRcvBufShrLim.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspTpRcvBufShrLim.setStatus("current")
if mibBuilder.loadTexts:
    cspTpRcvBufShrLim.setUnits("bytes")


class _CspTpTransBufShrLim_Type(Integer32):
    """Custom type cspTpTransBufShrLim based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8192, 262144),
    )


_CspTpTransBufShrLim_Type.__name__ = "Integer32"
_CspTpTransBufShrLim_Object = MibTableColumn
cspTpTransBufShrLim = _CspTpTransBufShrLim_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 5, 1, 1, 8),
    _CspTpTransBufShrLim_Type()
)
cspTpTransBufShrLim.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspTpTransBufShrLim.setStatus("current")
if mibBuilder.loadTexts:
    cspTpTransBufShrLim.setUnits("bytes")


class _CspTpMss_Type(Integer32):
    """Custom type cspTpMss based on Integer32"""
    defaultValue = 1460

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 1460),
    )


_CspTpMss_Type.__name__ = "Integer32"
_CspTpMss_Object = MibTableColumn
cspTpMss = _CspTpMss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 5, 1, 1, 9),
    _CspTpMss_Type()
)
cspTpMss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspTpMss.setStatus("current")
if mibBuilder.loadTexts:
    cspTpMss.setUnits("bytes")
_CspTpPathMtuDisc_Type = TruthValue
_CspTpPathMtuDisc_Object = MibTableColumn
cspTpPathMtuDisc = _CspTpPathMtuDisc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 5, 1, 1, 10),
    _CspTpPathMtuDisc_Type()
)
cspTpPathMtuDisc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspTpPathMtuDisc.setStatus("current")
_CspTpConfigRowStatus_Type = RowStatus
_CspTpConfigRowStatus_Object = MibTableColumn
cspTpConfigRowStatus = _CspTpConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 5, 1, 1, 11),
    _CspTpConfigRowStatus_Type()
)
cspTpConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspTpConfigRowStatus.setStatus("current")
_CspSslPolicyConfig_ObjectIdentity = ObjectIdentity
cspSslPolicyConfig = _CspSslPolicyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 6)
)
_CspSslPolicyTable_Object = MibTable
cspSslPolicyTable = _CspSslPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cspSslPolicyTable.setStatus("current")
_CspSslPolicyEntry_Object = MibTableRow
cspSslPolicyEntry = _CspSslPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 6, 1, 1)
)
cspSslPolicyEntry.setIndexNames(
    (0, "CISCO-SSL-PROXY-MIB", "cspSpPolicyName"),
)
if mibBuilder.loadTexts:
    cspSslPolicyEntry.setStatus("current")


class _CspSpPolicyName_Type(SnmpAdminString):
    """Custom type cspSpPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CspSpPolicyName_Type.__name__ = "SnmpAdminString"
_CspSpPolicyName_Object = MibTableColumn
cspSpPolicyName = _CspSpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 6, 1, 1, 1),
    _CspSpPolicyName_Type()
)
cspSpPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cspSpPolicyName.setStatus("current")
_CspSpRSArc4128md5_Type = TruthValue
_CspSpRSArc4128md5_Object = MibTableColumn
cspSpRSArc4128md5 = _CspSpRSArc4128md5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 6, 1, 1, 2),
    _CspSpRSArc4128md5_Type()
)
cspSpRSArc4128md5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspSpRSArc4128md5.setStatus("current")
_CspSpRSArc4128sha_Type = TruthValue
_CspSpRSArc4128sha_Object = MibTableColumn
cspSpRSArc4128sha = _CspSpRSArc4128sha_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 6, 1, 1, 3),
    _CspSpRSArc4128sha_Type()
)
cspSpRSArc4128sha.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspSpRSArc4128sha.setStatus("current")
_CspSpRSAdescbcsha_Type = TruthValue
_CspSpRSAdescbcsha_Object = MibTableColumn
cspSpRSAdescbcsha = _CspSpRSAdescbcsha_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 6, 1, 1, 4),
    _CspSpRSAdescbcsha_Type()
)
cspSpRSAdescbcsha.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspSpRSAdescbcsha.setStatus("current")
_CspSpRSA3descbcsha_Type = TruthValue
_CspSpRSA3descbcsha_Object = MibTableColumn
cspSpRSA3descbcsha = _CspSpRSA3descbcsha_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 6, 1, 1, 5),
    _CspSpRSA3descbcsha_Type()
)
cspSpRSA3descbcsha.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspSpRSA3descbcsha.setStatus("current")


class _CspSpProtocol_Type(Integer32):
    """Custom type cspSpProtocol based on Integer32"""
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
        *(("other", 1),
          ("ssl3", 2),
          ("ssl3AndTls1", 4),
          ("tls1", 3))
    )


_CspSpProtocol_Type.__name__ = "Integer32"
_CspSpProtocol_Object = MibTableColumn
cspSpProtocol = _CspSpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 6, 1, 1, 6),
    _CspSpProtocol_Type()
)
cspSpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspSpProtocol.setStatus("current")


class _CspSpCloseProtocol_Type(TruthValue):
    """Custom type cspSpCloseProtocol based on TruthValue"""


_CspSpCloseProtocol_Object = MibTableColumn
cspSpCloseProtocol = _CspSpCloseProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 6, 1, 1, 7),
    _CspSpCloseProtocol_Type()
)
cspSpCloseProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspSpCloseProtocol.setStatus("current")


class _CspSpSessionCache_Type(Integer32):
    """Custom type cspSpSessionCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 262143),
    )


_CspSpSessionCache_Type.__name__ = "Integer32"
_CspSpSessionCache_Object = MibTableColumn
cspSpSessionCache = _CspSpSessionCache_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 6, 1, 1, 8),
    _CspSpSessionCache_Type()
)
cspSpSessionCache.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspSpSessionCache.setStatus("current")
if mibBuilder.loadTexts:
    cspSpSessionCache.setUnits("bytes")


class _CspSpSessionTimeOut_Type(Integer32):
    """Custom type cspSpSessionTimeOut based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 72000),
    )


_CspSpSessionTimeOut_Type.__name__ = "Integer32"
_CspSpSessionTimeOut_Object = MibTableColumn
cspSpSessionTimeOut = _CspSpSessionTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 6, 1, 1, 9),
    _CspSpSessionTimeOut_Type()
)
cspSpSessionTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspSpSessionTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    cspSpSessionTimeOut.setUnits("seconds")
_CspSpConfigRowStatus_Type = RowStatus
_CspSpConfigRowStatus_Object = MibTableColumn
cspSpConfigRowStatus = _CspSpConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 6, 1, 1, 10),
    _CspSpConfigRowStatus_Type()
)
cspSpConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspSpConfigRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    cspSpConfigRowStatus.setUnits("seconds")
_CspTcpCountersInfo_ObjectIdentity = ObjectIdentity
cspTcpCountersInfo = _CspTcpCountersInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 7)
)
_CspTcpCountersClearTime_Type = TimeStamp
_CspTcpCountersClearTime_Object = MibScalar
cspTcpCountersClearTime = _CspTcpCountersClearTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 7, 1),
    _CspTcpCountersClearTime_Type()
)
cspTcpCountersClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTcpCountersClearTime.setStatus("current")
_CspTcpCounters_ObjectIdentity = ObjectIdentity
cspTcpCounters = _CspTcpCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 8)
)
_CspTcConnInit_Type = Counter32
_CspTcConnInit_Object = MibScalar
cspTcConnInit = _CspTcConnInit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 8, 1),
    _CspTcConnInit_Type()
)
cspTcConnInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTcConnInit.setStatus("current")
if mibBuilder.loadTexts:
    cspTcConnInit.setUnits("number of connections")
_CspTcConnAccept_Type = Counter32
_CspTcConnAccept_Object = MibScalar
cspTcConnAccept = _CspTcConnAccept_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 8, 2),
    _CspTcConnAccept_Type()
)
cspTcConnAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTcConnAccept.setStatus("current")
if mibBuilder.loadTexts:
    cspTcConnAccept.setUnits("number of connections")
_CspTcConnEstab_Type = Counter32
_CspTcConnEstab_Object = MibScalar
cspTcConnEstab = _CspTcConnEstab_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 8, 3),
    _CspTcConnEstab_Type()
)
cspTcConnEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTcConnEstab.setStatus("current")
if mibBuilder.loadTexts:
    cspTcConnEstab.setUnits("number of connections")
_CspTcConnDrop_Type = Counter32
_CspTcConnDrop_Object = MibScalar
cspTcConnDrop = _CspTcConnDrop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 8, 4),
    _CspTcConnDrop_Type()
)
cspTcConnDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTcConnDrop.setStatus("current")
if mibBuilder.loadTexts:
    cspTcConnDrop.setUnits("number of connections")
_CspTcConnClosed_Type = Counter32
_CspTcConnClosed_Object = MibScalar
cspTcConnClosed = _CspTcConnClosed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 8, 5),
    _CspTcConnClosed_Type()
)
cspTcConnClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTcConnClosed.setStatus("current")
if mibBuilder.loadTexts:
    cspTcConnClosed.setUnits("number of connections")
_CspTcSynTimeOuts_Type = Counter32
_CspTcSynTimeOuts_Object = MibScalar
cspTcSynTimeOuts = _CspTcSynTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 8, 6),
    _CspTcSynTimeOuts_Type()
)
cspTcSynTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTcSynTimeOuts.setStatus("current")
_CspTcIdleTimeOuts_Type = Counter32
_CspTcIdleTimeOuts_Object = MibScalar
cspTcIdleTimeOuts = _CspTcIdleTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 8, 7),
    _CspTcIdleTimeOuts_Type()
)
cspTcIdleTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTcIdleTimeOuts.setStatus("current")
_CspTcTotalPktSent_Type = Counter32
_CspTcTotalPktSent_Object = MibScalar
cspTcTotalPktSent = _CspTcTotalPktSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 8, 8),
    _CspTcTotalPktSent_Type()
)
cspTcTotalPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTcTotalPktSent.setStatus("current")
if mibBuilder.loadTexts:
    cspTcTotalPktSent.setUnits("number of packets")
_CspTcDataPktSent_Type = Counter32
_CspTcDataPktSent_Object = MibScalar
cspTcDataPktSent = _CspTcDataPktSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 8, 9),
    _CspTcDataPktSent_Type()
)
cspTcDataPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTcDataPktSent.setStatus("current")
if mibBuilder.loadTexts:
    cspTcDataPktSent.setUnits("number of packets")
_CspTcDataByteSent_Type = Counter32
_CspTcDataByteSent_Object = MibScalar
cspTcDataByteSent = _CspTcDataByteSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 8, 10),
    _CspTcDataByteSent_Type()
)
cspTcDataByteSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTcDataByteSent.setStatus("current")
if mibBuilder.loadTexts:
    cspTcDataByteSent.setUnits("bytes")
_CspTcTotalPktRcv_Type = Counter32
_CspTcTotalPktRcv_Object = MibScalar
cspTcTotalPktRcv = _CspTcTotalPktRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 8, 11),
    _CspTcTotalPktRcv_Type()
)
cspTcTotalPktRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTcTotalPktRcv.setStatus("current")
if mibBuilder.loadTexts:
    cspTcTotalPktRcv.setUnits("number of packets")
_CspTcPktRcvSeq_Type = Counter32
_CspTcPktRcvSeq_Object = MibScalar
cspTcPktRcvSeq = _CspTcPktRcvSeq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 8, 12),
    _CspTcPktRcvSeq_Type()
)
cspTcPktRcvSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTcPktRcvSeq.setStatus("current")
if mibBuilder.loadTexts:
    cspTcPktRcvSeq.setUnits("number of packets")
_CspTcByteRcvSeq_Type = Counter32
_CspTcByteRcvSeq_Object = MibScalar
cspTcByteRcvSeq = _CspTcByteRcvSeq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 8, 13),
    _CspTcByteRcvSeq_Type()
)
cspTcByteRcvSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTcByteRcvSeq.setStatus("current")
if mibBuilder.loadTexts:
    cspTcByteRcvSeq.setUnits("bytes")
_CspSslCountersInfo_ObjectIdentity = ObjectIdentity
cspSslCountersInfo = _CspSslCountersInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 9)
)
_CspSslCountersClearTime_Type = TimeStamp
_CspSslCountersClearTime_Object = MibScalar
cspSslCountersClearTime = _CspSslCountersClearTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 9, 1),
    _CspSslCountersClearTime_Type()
)
cspSslCountersClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSslCountersClearTime.setStatus("current")
_CspSslCounters_ObjectIdentity = ObjectIdentity
cspSslCounters = _CspSslCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 10)
)
_CspScConnAttempt_Type = Counter32
_CspScConnAttempt_Object = MibScalar
cspScConnAttempt = _CspScConnAttempt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 10, 1),
    _CspScConnAttempt_Type()
)
cspScConnAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspScConnAttempt.setStatus("current")
if mibBuilder.loadTexts:
    cspScConnAttempt.setUnits("number of connections")
_CspScConnComplete_Type = Counter32
_CspScConnComplete_Object = MibScalar
cspScConnComplete = _CspScConnComplete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 10, 2),
    _CspScConnComplete_Type()
)
cspScConnComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspScConnComplete.setStatus("current")
if mibBuilder.loadTexts:
    cspScConnComplete.setUnits("number of connections")
_CspScConnInHandShake_Type = Gauge32
_CspScConnInHandShake_Object = MibScalar
cspScConnInHandShake = _CspScConnInHandShake_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 10, 3),
    _CspScConnInHandShake_Type()
)
cspScConnInHandShake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspScConnInHandShake.setStatus("current")
if mibBuilder.loadTexts:
    cspScConnInHandShake.setUnits("number of connections")
_CspScConnInDataPhase_Type = Gauge32
_CspScConnInDataPhase_Object = MibScalar
cspScConnInDataPhase = _CspScConnInDataPhase_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 10, 4),
    _CspScConnInDataPhase_Type()
)
cspScConnInDataPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspScConnInDataPhase.setStatus("current")
if mibBuilder.loadTexts:
    cspScConnInDataPhase.setUnits("number of connections")
_CspScRenegAttempt_Type = Counter32
_CspScRenegAttempt_Object = MibScalar
cspScRenegAttempt = _CspScRenegAttempt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 10, 5),
    _CspScRenegAttempt_Type()
)
cspScRenegAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspScRenegAttempt.setStatus("current")
_CspScConnInReneg_Type = Gauge32
_CspScConnInReneg_Object = MibScalar
cspScConnInReneg = _CspScConnInReneg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 10, 6),
    _CspScConnInReneg_Type()
)
cspScConnInReneg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspScConnInReneg.setStatus("current")
if mibBuilder.loadTexts:
    cspScConnInReneg.setUnits("number of connections")
_CspScActiveSessions_Type = Gauge32
_CspScActiveSessions_Object = MibScalar
cspScActiveSessions = _CspScActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 10, 7),
    _CspScActiveSessions_Type()
)
cspScActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspScActiveSessions.setStatus("current")
_CspScMaxHandShakeConns_Type = Gauge32
_CspScMaxHandShakeConns_Object = MibScalar
cspScMaxHandShakeConns = _CspScMaxHandShakeConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 10, 8),
    _CspScMaxHandShakeConns_Type()
)
cspScMaxHandShakeConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspScMaxHandShakeConns.setStatus("current")
_CspScCurrDeviceQLen_Type = Gauge32
_CspScCurrDeviceQLen_Object = MibScalar
cspScCurrDeviceQLen = _CspScCurrDeviceQLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 10, 9),
    _CspScCurrDeviceQLen_Type()
)
cspScCurrDeviceQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspScCurrDeviceQLen.setStatus("current")
_CspScMaxDeviceQLen_Type = Gauge32
_CspScMaxDeviceQLen_Object = MibScalar
cspScMaxDeviceQLen = _CspScMaxDeviceQLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 10, 10),
    _CspScMaxDeviceQLen_Type()
)
cspScMaxDeviceQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspScMaxDeviceQLen.setStatus("current")
_CspScSessionReuses_Type = Counter32
_CspScSessionReuses_Object = MibScalar
cspScSessionReuses = _CspScSessionReuses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 10, 11),
    _CspScSessionReuses_Type()
)
cspScSessionReuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspScSessionReuses.setStatus("current")
_CspSsl3Counters_ObjectIdentity = ObjectIdentity
cspSsl3Counters = _CspSsl3Counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 11)
)
_CspS3cFullHandShake_Type = Counter32
_CspS3cFullHandShake_Object = MibScalar
cspS3cFullHandShake = _CspS3cFullHandShake_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 11, 1),
    _CspS3cFullHandShake_Type()
)
cspS3cFullHandShake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspS3cFullHandShake.setStatus("current")
_CspS3cResumedHandShake_Type = Counter32
_CspS3cResumedHandShake_Object = MibScalar
cspS3cResumedHandShake = _CspS3cResumedHandShake_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 11, 2),
    _CspS3cResumedHandShake_Type()
)
cspS3cResumedHandShake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspS3cResumedHandShake.setStatus("current")
_CspS3cHandShakeFailed_Type = Counter32
_CspS3cHandShakeFailed_Object = MibScalar
cspS3cHandShakeFailed = _CspS3cHandShakeFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 11, 3),
    _CspS3cHandShakeFailed_Type()
)
cspS3cHandShakeFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspS3cHandShakeFailed.setStatus("current")
_CspS3cDataFailed_Type = Counter32
_CspS3cDataFailed_Object = MibScalar
cspS3cDataFailed = _CspS3cDataFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 11, 4),
    _CspS3cDataFailed_Type()
)
cspS3cDataFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspS3cDataFailed.setStatus("current")
_CspS3cBadMacRcvd_Type = Counter32
_CspS3cBadMacRcvd_Object = MibScalar
cspS3cBadMacRcvd = _CspS3cBadMacRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 11, 5),
    _CspS3cBadMacRcvd_Type()
)
cspS3cBadMacRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspS3cBadMacRcvd.setStatus("current")
_CspS3cPadErrors_Type = Counter32
_CspS3cPadErrors_Object = MibScalar
cspS3cPadErrors = _CspS3cPadErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 11, 6),
    _CspS3cPadErrors_Type()
)
cspS3cPadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspS3cPadErrors.setStatus("current")
_CspS3cRSArc4128md5_Type = Counter32
_CspS3cRSArc4128md5_Object = MibScalar
cspS3cRSArc4128md5 = _CspS3cRSArc4128md5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 11, 7),
    _CspS3cRSArc4128md5_Type()
)
cspS3cRSArc4128md5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspS3cRSArc4128md5.setStatus("current")
if mibBuilder.loadTexts:
    cspS3cRSArc4128md5.setUnits("number of connections")
_CspS3cRSArc4128sha_Type = Counter32
_CspS3cRSArc4128sha_Object = MibScalar
cspS3cRSArc4128sha = _CspS3cRSArc4128sha_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 11, 8),
    _CspS3cRSArc4128sha_Type()
)
cspS3cRSArc4128sha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspS3cRSArc4128sha.setStatus("current")
if mibBuilder.loadTexts:
    cspS3cRSArc4128sha.setUnits("number of connections")
_CspS3cRSAdescbcsha_Type = Counter32
_CspS3cRSAdescbcsha_Object = MibScalar
cspS3cRSAdescbcsha = _CspS3cRSAdescbcsha_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 11, 9),
    _CspS3cRSAdescbcsha_Type()
)
cspS3cRSAdescbcsha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspS3cRSAdescbcsha.setStatus("current")
if mibBuilder.loadTexts:
    cspS3cRSAdescbcsha.setUnits("number of connections")
_CspS3cRSA3desedecbcsha_Type = Counter32
_CspS3cRSA3desedecbcsha_Object = MibScalar
cspS3cRSA3desedecbcsha = _CspS3cRSA3desedecbcsha_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 11, 10),
    _CspS3cRSA3desedecbcsha_Type()
)
cspS3cRSA3desedecbcsha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspS3cRSA3desedecbcsha.setStatus("current")
if mibBuilder.loadTexts:
    cspS3cRSA3desedecbcsha.setUnits("number of connections")
_CspTls1Counters_ObjectIdentity = ObjectIdentity
cspTls1Counters = _CspTls1Counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 12)
)
_CspTlcFullHandShake_Type = Counter32
_CspTlcFullHandShake_Object = MibScalar
cspTlcFullHandShake = _CspTlcFullHandShake_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 12, 1),
    _CspTlcFullHandShake_Type()
)
cspTlcFullHandShake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTlcFullHandShake.setStatus("current")
_CspTlcResumedHandShake_Type = Counter32
_CspTlcResumedHandShake_Object = MibScalar
cspTlcResumedHandShake = _CspTlcResumedHandShake_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 12, 2),
    _CspTlcResumedHandShake_Type()
)
cspTlcResumedHandShake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTlcResumedHandShake.setStatus("current")
_CspTlcHandShakeFailed_Type = Counter32
_CspTlcHandShakeFailed_Object = MibScalar
cspTlcHandShakeFailed = _CspTlcHandShakeFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 12, 3),
    _CspTlcHandShakeFailed_Type()
)
cspTlcHandShakeFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTlcHandShakeFailed.setStatus("current")
if mibBuilder.loadTexts:
    cspTlcHandShakeFailed.setUnits("number of connections")
_CspTlcDataFailed_Type = Counter32
_CspTlcDataFailed_Object = MibScalar
cspTlcDataFailed = _CspTlcDataFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 12, 4),
    _CspTlcDataFailed_Type()
)
cspTlcDataFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTlcDataFailed.setStatus("current")
if mibBuilder.loadTexts:
    cspTlcDataFailed.setUnits("number of connections")
_CspTlcBadMacRcvd_Type = Counter32
_CspTlcBadMacRcvd_Object = MibScalar
cspTlcBadMacRcvd = _CspTlcBadMacRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 12, 5),
    _CspTlcBadMacRcvd_Type()
)
cspTlcBadMacRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTlcBadMacRcvd.setStatus("current")
_CspTlcPadErrors_Type = Counter32
_CspTlcPadErrors_Object = MibScalar
cspTlcPadErrors = _CspTlcPadErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 12, 6),
    _CspTlcPadErrors_Type()
)
cspTlcPadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTlcPadErrors.setStatus("current")
_CspTlcRSArc4128md5_Type = Counter32
_CspTlcRSArc4128md5_Object = MibScalar
cspTlcRSArc4128md5 = _CspTlcRSArc4128md5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 12, 7),
    _CspTlcRSArc4128md5_Type()
)
cspTlcRSArc4128md5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTlcRSArc4128md5.setStatus("current")
if mibBuilder.loadTexts:
    cspTlcRSArc4128md5.setUnits("number of connections")
_CspTlcRSArc4128sha_Type = Counter32
_CspTlcRSArc4128sha_Object = MibScalar
cspTlcRSArc4128sha = _CspTlcRSArc4128sha_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 12, 8),
    _CspTlcRSArc4128sha_Type()
)
cspTlcRSArc4128sha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTlcRSArc4128sha.setStatus("current")
if mibBuilder.loadTexts:
    cspTlcRSArc4128sha.setUnits("number of connections")
_CspTlcRSAdescbcsha_Type = Counter32
_CspTlcRSAdescbcsha_Object = MibScalar
cspTlcRSAdescbcsha = _CspTlcRSAdescbcsha_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 12, 9),
    _CspTlcRSAdescbcsha_Type()
)
cspTlcRSAdescbcsha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTlcRSAdescbcsha.setStatus("current")
if mibBuilder.loadTexts:
    cspTlcRSAdescbcsha.setUnits("number of connections")
_CspTlcRSA3desedecbcsha_Type = Counter32
_CspTlcRSA3desedecbcsha_Object = MibScalar
cspTlcRSA3desedecbcsha = _CspTlcRSA3desedecbcsha_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 12, 10),
    _CspTlcRSA3desedecbcsha_Type()
)
cspTlcRSA3desedecbcsha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspTlcRSA3desedecbcsha.setStatus("current")
if mibBuilder.loadTexts:
    cspTlcRSA3desedecbcsha.setUnits("number of connections")
_CspSslCryptoCounters_ObjectIdentity = ObjectIdentity
cspSslCryptoCounters = _CspSslCryptoCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 13)
)
_CspSccBlksEncrypted_Type = Counter32
_CspSccBlksEncrypted_Object = MibScalar
cspSccBlksEncrypted = _CspSccBlksEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 13, 1),
    _CspSccBlksEncrypted_Type()
)
cspSccBlksEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSccBlksEncrypted.setStatus("current")
_CspSccBlksDecrypted_Type = Counter32
_CspSccBlksDecrypted_Object = MibScalar
cspSccBlksDecrypted = _CspSccBlksDecrypted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 13, 2),
    _CspSccBlksDecrypted_Type()
)
cspSccBlksDecrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSccBlksDecrypted.setStatus("current")
_CspSccBytesEncrypted_Type = Counter32
_CspSccBytesEncrypted_Object = MibScalar
cspSccBytesEncrypted = _CspSccBytesEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 13, 3),
    _CspSccBytesEncrypted_Type()
)
cspSccBytesEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSccBytesEncrypted.setStatus("current")
if mibBuilder.loadTexts:
    cspSccBytesEncrypted.setUnits("bytes")
_CspSccBytesDecrypted_Type = Counter32
_CspSccBytesDecrypted_Object = MibScalar
cspSccBytesDecrypted = _CspSccBytesDecrypted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 13, 4),
    _CspSccBytesDecrypted_Type()
)
cspSccBytesDecrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSccBytesDecrypted.setStatus("current")
if mibBuilder.loadTexts:
    cspSccBytesDecrypted.setUnits("bytes")
_CspSccPublicKeyOpers_Type = Counter32
_CspSccPublicKeyOpers_Object = MibScalar
cspSccPublicKeyOpers = _CspSccPublicKeyOpers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 13, 5),
    _CspSccPublicKeyOpers_Type()
)
cspSccPublicKeyOpers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSccPublicKeyOpers.setStatus("current")
_CspSccPrivateKeyOpers_Type = Counter32
_CspSccPrivateKeyOpers_Object = MibScalar
cspSccPrivateKeyOpers = _CspSccPrivateKeyOpers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 13, 6),
    _CspSccPrivateKeyOpers_Type()
)
cspSccPrivateKeyOpers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSccPrivateKeyOpers.setStatus("current")
_CspSccCryptoFails_Type = Counter32
_CspSccCryptoFails_Object = MibScalar
cspSccCryptoFails = _CspSccCryptoFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 13, 7),
    _CspSccCryptoFails_Type()
)
cspSccCryptoFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSccCryptoFails.setStatus("current")
_CspSccDmaErrors_Type = Counter32
_CspSccDmaErrors_Object = MibScalar
cspSccDmaErrors = _CspSccDmaErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 13, 8),
    _CspSccDmaErrors_Type()
)
cspSccDmaErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSccDmaErrors.setStatus("current")
_CspSslErrorCounters_ObjectIdentity = ObjectIdentity
cspSslErrorCounters = _CspSslErrorCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 14)
)
_CspSecSessAllocFailed_Type = Counter32
_CspSecSessAllocFailed_Object = MibScalar
cspSecSessAllocFailed = _CspSecSessAllocFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 14, 1),
    _CspSecSessAllocFailed_Type()
)
cspSecSessAllocFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSecSessAllocFailed.setStatus("current")
_CspSecSessLimitExceed_Type = Counter32
_CspSecSessLimitExceed_Object = MibScalar
cspSecSessLimitExceed = _CspSecSessLimitExceed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 14, 2),
    _CspSecSessLimitExceed_Type()
)
cspSecSessLimitExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSecSessLimitExceed.setStatus("current")
_CspSecHShakeInitFailed_Type = Counter32
_CspSecHShakeInitFailed_Object = MibScalar
cspSecHShakeInitFailed = _CspSecHShakeInitFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 14, 3),
    _CspSecHShakeInitFailed_Type()
)
cspSecHShakeInitFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSecHShakeInitFailed.setStatus("current")
_CspSecRenegFailed_Type = Counter32
_CspSecRenegFailed_Object = MibScalar
cspSecRenegFailed = _CspSecRenegFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 14, 4),
    _CspSecRenegFailed_Type()
)
cspSecRenegFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSecRenegFailed.setStatus("current")
_CspSecFatalAlertsRcvd_Type = Counter32
_CspSecFatalAlertsRcvd_Object = MibScalar
cspSecFatalAlertsRcvd = _CspSecFatalAlertsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 14, 5),
    _CspSecFatalAlertsRcvd_Type()
)
cspSecFatalAlertsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSecFatalAlertsRcvd.setStatus("current")
_CspSecFatalAlertsSent_Type = Counter32
_CspSecFatalAlertsSent_Object = MibScalar
cspSecFatalAlertsSent = _CspSecFatalAlertsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 14, 6),
    _CspSecFatalAlertsSent_Type()
)
cspSecFatalAlertsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSecFatalAlertsSent.setStatus("current")
_CspSecNoCipherAlerts_Type = Counter32
_CspSecNoCipherAlerts_Object = MibScalar
cspSecNoCipherAlerts = _CspSecNoCipherAlerts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 14, 7),
    _CspSecNoCipherAlerts_Type()
)
cspSecNoCipherAlerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSecNoCipherAlerts.setStatus("current")
_CspSecVerMismatchAlerts_Type = Counter32
_CspSecVerMismatchAlerts_Object = MibScalar
cspSecVerMismatchAlerts = _CspSecVerMismatchAlerts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 14, 8),
    _CspSecVerMismatchAlerts_Type()
)
cspSecVerMismatchAlerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSecVerMismatchAlerts.setStatus("current")
_CspSecNoComprsnAlerts_Type = Counter32
_CspSecNoComprsnAlerts_Object = MibScalar
cspSecNoComprsnAlerts = _CspSecNoComprsnAlerts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 14, 9),
    _CspSecNoComprsnAlerts_Type()
)
cspSecNoComprsnAlerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSecNoComprsnAlerts.setStatus("current")
_CspSecHShakeHndleMemFail_Type = Counter32
_CspSecHShakeHndleMemFail_Object = MibScalar
cspSecHShakeHndleMemFail = _CspSecHShakeHndleMemFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 14, 10),
    _CspSecHShakeHndleMemFail_Type()
)
cspSecHShakeHndleMemFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSecHShakeHndleMemFail.setStatus("current")
_CspSecStalePakDrop_Type = Counter32
_CspSecStalePakDrop_Object = MibScalar
cspSecStalePakDrop = _CspSecStalePakDrop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 14, 11),
    _CspSecStalePakDrop_Type()
)
cspSecStalePakDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSecStalePakDrop.setStatus("current")
_CspSecServiceIdDiscard_Type = Counter32
_CspSecServiceIdDiscard_Object = MibScalar
cspSecServiceIdDiscard = _CspSecServiceIdDiscard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 14, 12),
    _CspSecServiceIdDiscard_Type()
)
cspSecServiceIdDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSecServiceIdDiscard.setStatus("current")
_CspSecHShakeLimitExceed_Type = Counter32
_CspSecHShakeLimitExceed_Object = MibScalar
cspSecHShakeLimitExceed = _CspSecHShakeLimitExceed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 14, 13),
    _CspSecHShakeLimitExceed_Type()
)
cspSecHShakeLimitExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSecHShakeLimitExceed.setStatus("current")
_CspSecDevConnCtxtFail_Type = Counter32
_CspSecDevConnCtxtFail_Object = MibScalar
cspSecDevConnCtxtFail = _CspSecDevConnCtxtFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 14, 14),
    _CspSecDevConnCtxtFail_Type()
)
cspSecDevConnCtxtFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSecDevConnCtxtFail.setStatus("current")
_CspSecMemAllocFailed_Type = Counter32
_CspSecMemAllocFailed_Object = MibScalar
cspSecMemAllocFailed = _CspSecMemAllocFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 14, 15),
    _CspSecMemAllocFailed_Type()
)
cspSecMemAllocFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSecMemAllocFailed.setStatus("current")
_CspSecBuffAllocFailed_Type = Counter32
_CspSecBuffAllocFailed_Object = MibScalar
cspSecBuffAllocFailed = _CspSecBuffAllocFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 14, 16),
    _CspSecBuffAllocFailed_Type()
)
cspSecBuffAllocFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSecBuffAllocFailed.setStatus("current")
_CspSecAlertSendFailed_Type = Counter32
_CspSecAlertSendFailed_Object = MibScalar
cspSecAlertSendFailed = _CspSecAlertSendFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 14, 17),
    _CspSecAlertSendFailed_Type()
)
cspSecAlertSendFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSecAlertSendFailed.setStatus("current")
_CspSecOverloadDropped_Type = Counter32
_CspSecOverloadDropped_Object = MibScalar
cspSecOverloadDropped = _CspSecOverloadDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 14, 18),
    _CspSecOverloadDropped_Type()
)
cspSecOverloadDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSecOverloadDropped.setStatus("current")
_CspSecConnAborted_Type = Counter32
_CspSecConnAborted_Object = MibScalar
cspSecConnAborted = _CspSecConnAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 14, 19),
    _CspSecConnAborted_Type()
)
cspSecConnAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSecConnAborted.setStatus("current")
if mibBuilder.loadTexts:
    cspSecConnAborted.setUnits("number of connections")
_CspPsCounters_ObjectIdentity = ObjectIdentity
cspPsCounters = _CspPsCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15)
)
_CspPsCountersTable_Object = MibTable
cspPsCountersTable = _CspPsCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15, 1)
)
if mibBuilder.loadTexts:
    cspPsCountersTable.setStatus("current")
_CspPsCounterEntry_Object = MibTableRow
cspPsCounterEntry = _CspPsCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15, 1, 1)
)
cspPsCounterEntry.setIndexNames(
    (0, "CISCO-SSL-PROXY-MIB", "cspPsName"),
    (0, "CISCO-SSL-PROXY-MIB", "cspPsListIndex"),
)
if mibBuilder.loadTexts:
    cspPsCounterEntry.setStatus("current")
_CspPscClearTime_Type = TimeStamp
_CspPscClearTime_Object = MibTableColumn
cspPscClearTime = _CspPscClearTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15, 1, 1, 1),
    _CspPscClearTime_Type()
)
cspPscClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPscClearTime.setStatus("current")
_CspPscConnAttempt_Type = Counter32
_CspPscConnAttempt_Object = MibTableColumn
cspPscConnAttempt = _CspPscConnAttempt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15, 1, 1, 2),
    _CspPscConnAttempt_Type()
)
cspPscConnAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPscConnAttempt.setStatus("current")
if mibBuilder.loadTexts:
    cspPscConnAttempt.setUnits("number of connections")
_CspPscConnComplete_Type = Counter32
_CspPscConnComplete_Object = MibTableColumn
cspPscConnComplete = _CspPscConnComplete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15, 1, 1, 3),
    _CspPscConnComplete_Type()
)
cspPscConnComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPscConnComplete.setStatus("current")
if mibBuilder.loadTexts:
    cspPscConnComplete.setUnits("number of connections")
_CspPscFullHandShake_Type = Counter32
_CspPscFullHandShake_Object = MibTableColumn
cspPscFullHandShake = _CspPscFullHandShake_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15, 1, 1, 4),
    _CspPscFullHandShake_Type()
)
cspPscFullHandShake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPscFullHandShake.setStatus("current")
_CspPscResumedHandShake_Type = Counter32
_CspPscResumedHandShake_Object = MibTableColumn
cspPscResumedHandShake = _CspPscResumedHandShake_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15, 1, 1, 5),
    _CspPscResumedHandShake_Type()
)
cspPscResumedHandShake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPscResumedHandShake.setStatus("current")
_CspPscConnInHandShake_Type = Gauge32
_CspPscConnInHandShake_Object = MibTableColumn
cspPscConnInHandShake = _CspPscConnInHandShake_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15, 1, 1, 6),
    _CspPscConnInHandShake_Type()
)
cspPscConnInHandShake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPscConnInHandShake.setStatus("current")
if mibBuilder.loadTexts:
    cspPscConnInHandShake.setUnits("number of connections")
_CspPscConnInDataPhase_Type = Gauge32
_CspPscConnInDataPhase_Object = MibTableColumn
cspPscConnInDataPhase = _CspPscConnInDataPhase_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15, 1, 1, 7),
    _CspPscConnInDataPhase_Type()
)
cspPscConnInDataPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPscConnInDataPhase.setStatus("current")
if mibBuilder.loadTexts:
    cspPscConnInDataPhase.setUnits("number of connections")
_CspPscRenegAttempt_Type = Counter32
_CspPscRenegAttempt_Object = MibTableColumn
cspPscRenegAttempt = _CspPscRenegAttempt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15, 1, 1, 8),
    _CspPscRenegAttempt_Type()
)
cspPscRenegAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPscRenegAttempt.setStatus("current")
_CspPscConnInReneg_Type = Gauge32
_CspPscConnInReneg_Object = MibTableColumn
cspPscConnInReneg = _CspPscConnInReneg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15, 1, 1, 9),
    _CspPscConnInReneg_Type()
)
cspPscConnInReneg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPscConnInReneg.setStatus("current")
if mibBuilder.loadTexts:
    cspPscConnInReneg.setUnits("number of connections")
_CspPscBlksEncrypted_Type = Counter32
_CspPscBlksEncrypted_Object = MibTableColumn
cspPscBlksEncrypted = _CspPscBlksEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15, 1, 1, 10),
    _CspPscBlksEncrypted_Type()
)
cspPscBlksEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPscBlksEncrypted.setStatus("current")
_CspPscBlksDecrypted_Type = Counter32
_CspPscBlksDecrypted_Object = MibTableColumn
cspPscBlksDecrypted = _CspPscBlksDecrypted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15, 1, 1, 11),
    _CspPscBlksDecrypted_Type()
)
cspPscBlksDecrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPscBlksDecrypted.setStatus("current")
_CspPscBytesEncrypted_Type = Counter32
_CspPscBytesEncrypted_Object = MibTableColumn
cspPscBytesEncrypted = _CspPscBytesEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15, 1, 1, 12),
    _CspPscBytesEncrypted_Type()
)
cspPscBytesEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPscBytesEncrypted.setStatus("current")
if mibBuilder.loadTexts:
    cspPscBytesEncrypted.setUnits("bytes")
_CspPscBytesDecrypted_Type = Counter32
_CspPscBytesDecrypted_Object = MibTableColumn
cspPscBytesDecrypted = _CspPscBytesDecrypted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15, 1, 1, 13),
    _CspPscBytesDecrypted_Type()
)
cspPscBytesDecrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPscBytesDecrypted.setStatus("current")
if mibBuilder.loadTexts:
    cspPscBytesDecrypted.setUnits("bytes")
_CspPscValidSessions_Type = Counter32
_CspPscValidSessions_Object = MibTableColumn
cspPscValidSessions = _CspPscValidSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15, 1, 1, 14),
    _CspPscValidSessions_Type()
)
cspPscValidSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPscValidSessions.setStatus("current")
_CspPscSessLimitExceed_Type = Counter32
_CspPscSessLimitExceed_Object = MibTableColumn
cspPscSessLimitExceed = _CspPscSessLimitExceed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15, 1, 1, 15),
    _CspPscSessLimitExceed_Type()
)
cspPscSessLimitExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPscSessLimitExceed.setStatus("current")
_CspPscHandShakeFailed_Type = Counter32
_CspPscHandShakeFailed_Object = MibTableColumn
cspPscHandShakeFailed = _CspPscHandShakeFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15, 1, 1, 16),
    _CspPscHandShakeFailed_Type()
)
cspPscHandShakeFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPscHandShakeFailed.setStatus("current")
_CspPscDataFailed_Type = Counter32
_CspPscDataFailed_Object = MibTableColumn
cspPscDataFailed = _CspPscDataFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15, 1, 1, 17),
    _CspPscDataFailed_Type()
)
cspPscDataFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPscDataFailed.setStatus("current")
_CspPscFatalAlertsRcvd_Type = Counter32
_CspPscFatalAlertsRcvd_Object = MibTableColumn
cspPscFatalAlertsRcvd = _CspPscFatalAlertsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15, 1, 1, 18),
    _CspPscFatalAlertsRcvd_Type()
)
cspPscFatalAlertsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPscFatalAlertsRcvd.setStatus("current")
_CspPscFatalAlertsSent_Type = Counter32
_CspPscFatalAlertsSent_Object = MibTableColumn
cspPscFatalAlertsSent = _CspPscFatalAlertsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15, 1, 1, 19),
    _CspPscFatalAlertsSent_Type()
)
cspPscFatalAlertsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPscFatalAlertsSent.setStatus("current")
_CspPscBadMacRcvd_Type = Counter32
_CspPscBadMacRcvd_Object = MibTableColumn
cspPscBadMacRcvd = _CspPscBadMacRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15, 1, 1, 20),
    _CspPscBadMacRcvd_Type()
)
cspPscBadMacRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPscBadMacRcvd.setStatus("current")
_CspPscPadErrors_Type = Counter32
_CspPscPadErrors_Object = MibTableColumn
cspPscPadErrors = _CspPscPadErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15, 1, 1, 21),
    _CspPscPadErrors_Type()
)
cspPscPadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPscPadErrors.setStatus("current")
_CspPscNoCipherAlerts_Type = Counter32
_CspPscNoCipherAlerts_Object = MibTableColumn
cspPscNoCipherAlerts = _CspPscNoCipherAlerts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15, 1, 1, 22),
    _CspPscNoCipherAlerts_Type()
)
cspPscNoCipherAlerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPscNoCipherAlerts.setStatus("current")
_CspPscNoComprsnAlerts_Type = Counter32
_CspPscNoComprsnAlerts_Object = MibTableColumn
cspPscNoComprsnAlerts = _CspPscNoComprsnAlerts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15, 1, 1, 23),
    _CspPscNoComprsnAlerts_Type()
)
cspPscNoComprsnAlerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPscNoComprsnAlerts.setStatus("current")
_CspPscVerMismatchAlerts_Type = Counter32
_CspPscVerMismatchAlerts_Object = MibTableColumn
cspPscVerMismatchAlerts = _CspPscVerMismatchAlerts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 15, 1, 1, 24),
    _CspPscVerMismatchAlerts_Type()
)
cspPscVerMismatchAlerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPscVerMismatchAlerts.setStatus("current")
_CspPsSsl3Counters_ObjectIdentity = ObjectIdentity
cspPsSsl3Counters = _CspPsSsl3Counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 16)
)
_CspPsSsl3CountersTable_Object = MibTable
cspPsSsl3CountersTable = _CspPsSsl3CountersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 16, 1)
)
if mibBuilder.loadTexts:
    cspPsSsl3CountersTable.setStatus("current")
_CspPsSsl3CounterEntry_Object = MibTableRow
cspPsSsl3CounterEntry = _CspPsSsl3CounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 16, 1, 1)
)
cspPsSsl3CounterEntry.setIndexNames(
    (0, "CISCO-SSL-PROXY-MIB", "cspPsName"),
    (0, "CISCO-SSL-PROXY-MIB", "cspPsListIndex"),
)
if mibBuilder.loadTexts:
    cspPsSsl3CounterEntry.setStatus("current")
_CspPs3cClearTime_Type = TimeStamp
_CspPs3cClearTime_Object = MibTableColumn
cspPs3cClearTime = _CspPs3cClearTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 16, 1, 1, 1),
    _CspPs3cClearTime_Type()
)
cspPs3cClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPs3cClearTime.setStatus("current")
_CspPs3cFullHandShake_Type = Counter32
_CspPs3cFullHandShake_Object = MibTableColumn
cspPs3cFullHandShake = _CspPs3cFullHandShake_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 16, 1, 1, 2),
    _CspPs3cFullHandShake_Type()
)
cspPs3cFullHandShake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPs3cFullHandShake.setStatus("current")
_CspPs3cResumedHandShake_Type = Counter32
_CspPs3cResumedHandShake_Object = MibTableColumn
cspPs3cResumedHandShake = _CspPs3cResumedHandShake_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 16, 1, 1, 3),
    _CspPs3cResumedHandShake_Type()
)
cspPs3cResumedHandShake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPs3cResumedHandShake.setStatus("current")
_CspPs3cHandShakeFailed_Type = Counter32
_CspPs3cHandShakeFailed_Object = MibTableColumn
cspPs3cHandShakeFailed = _CspPs3cHandShakeFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 16, 1, 1, 4),
    _CspPs3cHandShakeFailed_Type()
)
cspPs3cHandShakeFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPs3cHandShakeFailed.setStatus("current")
_CspPs3cDataFailed_Type = Counter32
_CspPs3cDataFailed_Object = MibTableColumn
cspPs3cDataFailed = _CspPs3cDataFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 16, 1, 1, 5),
    _CspPs3cDataFailed_Type()
)
cspPs3cDataFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPs3cDataFailed.setStatus("current")
_CspPs3cBadMacRcvd_Type = Counter32
_CspPs3cBadMacRcvd_Object = MibTableColumn
cspPs3cBadMacRcvd = _CspPs3cBadMacRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 16, 1, 1, 6),
    _CspPs3cBadMacRcvd_Type()
)
cspPs3cBadMacRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPs3cBadMacRcvd.setStatus("current")
_CspPs3cPadErrors_Type = Counter32
_CspPs3cPadErrors_Object = MibTableColumn
cspPs3cPadErrors = _CspPs3cPadErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 16, 1, 1, 7),
    _CspPs3cPadErrors_Type()
)
cspPs3cPadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPs3cPadErrors.setStatus("current")
_CspPs3cRSArc4128md5_Type = Counter32
_CspPs3cRSArc4128md5_Object = MibTableColumn
cspPs3cRSArc4128md5 = _CspPs3cRSArc4128md5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 16, 1, 1, 8),
    _CspPs3cRSArc4128md5_Type()
)
cspPs3cRSArc4128md5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPs3cRSArc4128md5.setStatus("current")
if mibBuilder.loadTexts:
    cspPs3cRSArc4128md5.setUnits("number of connections")
_CspPs3cRSArc4128sha_Type = Counter32
_CspPs3cRSArc4128sha_Object = MibTableColumn
cspPs3cRSArc4128sha = _CspPs3cRSArc4128sha_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 16, 1, 1, 9),
    _CspPs3cRSArc4128sha_Type()
)
cspPs3cRSArc4128sha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPs3cRSArc4128sha.setStatus("current")
if mibBuilder.loadTexts:
    cspPs3cRSArc4128sha.setUnits("number of connections")
_CspPs3cRSAdescbcsha_Type = Counter32
_CspPs3cRSAdescbcsha_Object = MibTableColumn
cspPs3cRSAdescbcsha = _CspPs3cRSAdescbcsha_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 16, 1, 1, 10),
    _CspPs3cRSAdescbcsha_Type()
)
cspPs3cRSAdescbcsha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPs3cRSAdescbcsha.setStatus("current")
if mibBuilder.loadTexts:
    cspPs3cRSAdescbcsha.setUnits("number of connections")
_CspPs3cRSA3desedecbcsha_Type = Counter32
_CspPs3cRSA3desedecbcsha_Object = MibTableColumn
cspPs3cRSA3desedecbcsha = _CspPs3cRSA3desedecbcsha_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 16, 1, 1, 11),
    _CspPs3cRSA3desedecbcsha_Type()
)
cspPs3cRSA3desedecbcsha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPs3cRSA3desedecbcsha.setStatus("current")
if mibBuilder.loadTexts:
    cspPs3cRSA3desedecbcsha.setUnits("number of connections")
_CspPsTls1Counters_ObjectIdentity = ObjectIdentity
cspPsTls1Counters = _CspPsTls1Counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 17)
)
_CspPsTls1CountersTable_Object = MibTable
cspPsTls1CountersTable = _CspPsTls1CountersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 17, 1)
)
if mibBuilder.loadTexts:
    cspPsTls1CountersTable.setStatus("current")
_CspPsTls1CounterEntry_Object = MibTableRow
cspPsTls1CounterEntry = _CspPsTls1CounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 17, 1, 1)
)
cspPsTls1CounterEntry.setIndexNames(
    (0, "CISCO-SSL-PROXY-MIB", "cspPsName"),
    (0, "CISCO-SSL-PROXY-MIB", "cspPsListIndex"),
)
if mibBuilder.loadTexts:
    cspPsTls1CounterEntry.setStatus("current")
_CspPt1cClearTime_Type = TimeStamp
_CspPt1cClearTime_Object = MibTableColumn
cspPt1cClearTime = _CspPt1cClearTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 17, 1, 1, 1),
    _CspPt1cClearTime_Type()
)
cspPt1cClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPt1cClearTime.setStatus("current")
_CspPt1cFullHandShake_Type = Counter32
_CspPt1cFullHandShake_Object = MibTableColumn
cspPt1cFullHandShake = _CspPt1cFullHandShake_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 17, 1, 1, 2),
    _CspPt1cFullHandShake_Type()
)
cspPt1cFullHandShake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPt1cFullHandShake.setStatus("current")
_CspPt1cResumedHandShake_Type = Counter32
_CspPt1cResumedHandShake_Object = MibTableColumn
cspPt1cResumedHandShake = _CspPt1cResumedHandShake_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 17, 1, 1, 3),
    _CspPt1cResumedHandShake_Type()
)
cspPt1cResumedHandShake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPt1cResumedHandShake.setStatus("current")
_CspPt1cHandShakeFailed_Type = Counter32
_CspPt1cHandShakeFailed_Object = MibTableColumn
cspPt1cHandShakeFailed = _CspPt1cHandShakeFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 17, 1, 1, 4),
    _CspPt1cHandShakeFailed_Type()
)
cspPt1cHandShakeFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPt1cHandShakeFailed.setStatus("current")
_CspPt1cDataFailed_Type = Counter32
_CspPt1cDataFailed_Object = MibTableColumn
cspPt1cDataFailed = _CspPt1cDataFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 17, 1, 1, 5),
    _CspPt1cDataFailed_Type()
)
cspPt1cDataFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPt1cDataFailed.setStatus("current")
_CspPt1cBadMacRcvd_Type = Counter32
_CspPt1cBadMacRcvd_Object = MibTableColumn
cspPt1cBadMacRcvd = _CspPt1cBadMacRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 17, 1, 1, 6),
    _CspPt1cBadMacRcvd_Type()
)
cspPt1cBadMacRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPt1cBadMacRcvd.setStatus("current")
_CspPt1cPadErrors_Type = Counter32
_CspPt1cPadErrors_Object = MibTableColumn
cspPt1cPadErrors = _CspPt1cPadErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 17, 1, 1, 7),
    _CspPt1cPadErrors_Type()
)
cspPt1cPadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPt1cPadErrors.setStatus("current")
_CspPt1cRSArc4128md5_Type = Counter32
_CspPt1cRSArc4128md5_Object = MibTableColumn
cspPt1cRSArc4128md5 = _CspPt1cRSArc4128md5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 17, 1, 1, 8),
    _CspPt1cRSArc4128md5_Type()
)
cspPt1cRSArc4128md5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPt1cRSArc4128md5.setStatus("current")
if mibBuilder.loadTexts:
    cspPt1cRSArc4128md5.setUnits("number of connections")
_CspPt1cRSArc4128sha_Type = Counter32
_CspPt1cRSArc4128sha_Object = MibTableColumn
cspPt1cRSArc4128sha = _CspPt1cRSArc4128sha_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 17, 1, 1, 9),
    _CspPt1cRSArc4128sha_Type()
)
cspPt1cRSArc4128sha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPt1cRSArc4128sha.setStatus("current")
if mibBuilder.loadTexts:
    cspPt1cRSArc4128sha.setUnits("number of connections")
_CspPt1cRSAdescbcsha_Type = Counter32
_CspPt1cRSAdescbcsha_Object = MibTableColumn
cspPt1cRSAdescbcsha = _CspPt1cRSAdescbcsha_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 17, 1, 1, 10),
    _CspPt1cRSAdescbcsha_Type()
)
cspPt1cRSAdescbcsha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPt1cRSAdescbcsha.setStatus("current")
if mibBuilder.loadTexts:
    cspPt1cRSAdescbcsha.setUnits("number of connections")
_CspPt1cRSA3desedecbcsha_Type = Counter32
_CspPt1cRSA3desedecbcsha_Object = MibTableColumn
cspPt1cRSA3desedecbcsha = _CspPt1cRSA3desedecbcsha_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 17, 1, 1, 11),
    _CspPt1cRSA3desedecbcsha_Type()
)
cspPt1cRSA3desedecbcsha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspPt1cRSA3desedecbcsha.setStatus("current")
if mibBuilder.loadTexts:
    cspPt1cRSA3desedecbcsha.setUnits("number of connections")
_CspCpuStatusInfo_ObjectIdentity = ObjectIdentity
cspCpuStatusInfo = _CspCpuStatusInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 18)
)
_CspCpuStatusTable_Object = MibTable
cspCpuStatusTable = _CspCpuStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 18, 1)
)
if mibBuilder.loadTexts:
    cspCpuStatusTable.setStatus("current")
_CspCpuStatusEntry_Object = MibTableRow
cspCpuStatusEntry = _CspCpuStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 18, 1, 1)
)
cspCpuStatusEntry.setIndexNames(
    (0, "CISCO-SSL-PROXY-MIB", "cspCpuName"),
)
if mibBuilder.loadTexts:
    cspCpuStatusEntry.setStatus("current")


class _CspCpuName_Type(SnmpAdminString):
    """Custom type cspCpuName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CspCpuName_Type.__name__ = "SnmpAdminString"
_CspCpuName_Object = MibTableColumn
cspCpuName = _CspCpuName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 18, 1, 1, 1),
    _CspCpuName_Type()
)
cspCpuName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cspCpuName.setStatus("current")


class _CspCpuStatus_Type(Integer32):
    """Custom type cspCpuStatus based on Integer32"""
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


_CspCpuStatus_Type.__name__ = "Integer32"
_CspCpuStatus_Object = MibTableColumn
cspCpuStatus = _CspCpuStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 18, 1, 1, 2),
    _CspCpuStatus_Type()
)
cspCpuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspCpuStatus.setStatus("current")
_CspCpuClearTime_Type = TimeStamp
_CspCpuClearTime_Object = MibTableColumn
cspCpuClearTime = _CspCpuClearTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 18, 1, 1, 3),
    _CspCpuClearTime_Type()
)
cspCpuClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspCpuClearTime.setStatus("current")
_CspCpuProcessUtil_Type = Gauge32
_CspCpuProcessUtil_Object = MibTableColumn
cspCpuProcessUtil = _CspCpuProcessUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 18, 1, 1, 4),
    _CspCpuProcessUtil_Type()
)
cspCpuProcessUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspCpuProcessUtil.setStatus("current")
if mibBuilder.loadTexts:
    cspCpuProcessUtil.setUnits("percentage")
_CspCpuInterruptUtil_Type = Gauge32
_CspCpuInterruptUtil_Object = MibTableColumn
cspCpuInterruptUtil = _CspCpuInterruptUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 18, 1, 1, 5),
    _CspCpuInterruptUtil_Type()
)
cspCpuInterruptUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspCpuInterruptUtil.setStatus("current")
if mibBuilder.loadTexts:
    cspCpuInterruptUtil.setUnits("percentage")
_CspCpuProcessUtilIn5Sec_Type = Gauge32
_CspCpuProcessUtilIn5Sec_Object = MibTableColumn
cspCpuProcessUtilIn5Sec = _CspCpuProcessUtilIn5Sec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 18, 1, 1, 6),
    _CspCpuProcessUtilIn5Sec_Type()
)
cspCpuProcessUtilIn5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspCpuProcessUtilIn5Sec.setStatus("current")
if mibBuilder.loadTexts:
    cspCpuProcessUtilIn5Sec.setUnits("percentage")
_CspCpuProcessUtilIn1Min_Type = Gauge32
_CspCpuProcessUtilIn1Min_Object = MibTableColumn
cspCpuProcessUtilIn1Min = _CspCpuProcessUtilIn1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 18, 1, 1, 7),
    _CspCpuProcessUtilIn1Min_Type()
)
cspCpuProcessUtilIn1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspCpuProcessUtilIn1Min.setStatus("current")
if mibBuilder.loadTexts:
    cspCpuProcessUtilIn1Min.setUnits("percentage")
_CspCpuProcessUtilIn5Min_Type = Gauge32
_CspCpuProcessUtilIn5Min_Object = MibTableColumn
cspCpuProcessUtilIn5Min = _CspCpuProcessUtilIn5Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 18, 1, 1, 8),
    _CspCpuProcessUtilIn5Min_Type()
)
cspCpuProcessUtilIn5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspCpuProcessUtilIn5Min.setStatus("current")
if mibBuilder.loadTexts:
    cspCpuProcessUtilIn5Min.setUnits("percentage")
_CspCpuInterruptUtilIn5Sec_Type = Gauge32
_CspCpuInterruptUtilIn5Sec_Object = MibTableColumn
cspCpuInterruptUtilIn5Sec = _CspCpuInterruptUtilIn5Sec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 18, 1, 1, 9),
    _CspCpuInterruptUtilIn5Sec_Type()
)
cspCpuInterruptUtilIn5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspCpuInterruptUtilIn5Sec.setStatus("current")
if mibBuilder.loadTexts:
    cspCpuInterruptUtilIn5Sec.setUnits("percentage")
_CspCpuInterruptUtilIn1Min_Type = Gauge32
_CspCpuInterruptUtilIn1Min_Object = MibTableColumn
cspCpuInterruptUtilIn1Min = _CspCpuInterruptUtilIn1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 18, 1, 1, 10),
    _CspCpuInterruptUtilIn1Min_Type()
)
cspCpuInterruptUtilIn1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspCpuInterruptUtilIn1Min.setStatus("current")
if mibBuilder.loadTexts:
    cspCpuInterruptUtilIn1Min.setUnits("percentage")
_CspCpuInterruptUtilIn5Min_Type = Gauge32
_CspCpuInterruptUtilIn5Min_Object = MibTableColumn
cspCpuInterruptUtilIn5Min = _CspCpuInterruptUtilIn5Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 18, 1, 1, 11),
    _CspCpuInterruptUtilIn5Min_Type()
)
cspCpuInterruptUtilIn5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspCpuInterruptUtilIn5Min.setStatus("current")
if mibBuilder.loadTexts:
    cspCpuInterruptUtilIn5Min.setUnits("percentage")
_CspHttpHeaderInsertedInfo_ObjectIdentity = ObjectIdentity
cspHttpHeaderInsertedInfo = _CspHttpHeaderInsertedInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 19)
)
_CspHttpHeaderInsertedSslInfoStats_ObjectIdentity = ObjectIdentity
cspHttpHeaderInsertedSslInfoStats = _CspHttpHeaderInsertedSslInfoStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 19, 1)
)
_CspNumOfSslInfoSuccessInserted_Type = Counter32
_CspNumOfSslInfoSuccessInserted_Object = MibScalar
cspNumOfSslInfoSuccessInserted = _CspNumOfSslInfoSuccessInserted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 19, 1, 1),
    _CspNumOfSslInfoSuccessInserted_Type()
)
cspNumOfSslInfoSuccessInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspNumOfSslInfoSuccessInserted.setStatus("current")
_CspNumOfSslInfoFailedInserted_Type = Counter32
_CspNumOfSslInfoFailedInserted_Object = MibScalar
cspNumOfSslInfoFailedInserted = _CspNumOfSslInfoFailedInserted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 19, 1, 2),
    _CspNumOfSslInfoFailedInserted_Type()
)
cspNumOfSslInfoFailedInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspNumOfSslInfoFailedInserted.setStatus("current")
_CspNumOfSpoofHttpHeaderDeleted_Type = Counter32
_CspNumOfSpoofHttpHeaderDeleted_Object = MibScalar
cspNumOfSpoofHttpHeaderDeleted = _CspNumOfSpoofHttpHeaderDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 19, 1, 3),
    _CspNumOfSpoofHttpHeaderDeleted_Type()
)
cspNumOfSpoofHttpHeaderDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspNumOfSpoofHttpHeaderDeleted.setStatus("current")
_CspNumOfSslSessHeaderExtracted_Type = Counter32
_CspNumOfSslSessHeaderExtracted_Object = MibScalar
cspNumOfSslSessHeaderExtracted = _CspNumOfSslSessHeaderExtracted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 19, 1, 4),
    _CspNumOfSslSessHeaderExtracted_Type()
)
cspNumOfSslSessHeaderExtracted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspNumOfSslSessHeaderExtracted.setStatus("current")
_CspNumOfSslSessHeaderFailedExtracted_Type = Counter32
_CspNumOfSslSessHeaderFailedExtracted_Object = MibScalar
cspNumOfSslSessHeaderFailedExtracted = _CspNumOfSslSessHeaderFailedExtracted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 19, 1, 5),
    _CspNumOfSslSessHeaderFailedExtracted_Type()
)
cspNumOfSslSessHeaderFailedExtracted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspNumOfSslSessHeaderFailedExtracted.setStatus("current")
_CspNumOfSslServerCertHeaderExtracted_Type = Counter32
_CspNumOfSslServerCertHeaderExtracted_Object = MibScalar
cspNumOfSslServerCertHeaderExtracted = _CspNumOfSslServerCertHeaderExtracted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 19, 1, 6),
    _CspNumOfSslServerCertHeaderExtracted_Type()
)
cspNumOfSslServerCertHeaderExtracted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspNumOfSslServerCertHeaderExtracted.setStatus("current")
_CspNumOfSslServerCerHeaderFailedExtracted_Type = Counter32
_CspNumOfSslServerCerHeaderFailedExtracted_Object = MibScalar
cspNumOfSslServerCerHeaderFailedExtracted = _CspNumOfSslServerCerHeaderFailedExtracted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 19, 1, 7),
    _CspNumOfSslServerCerHeaderFailedExtracted_Type()
)
cspNumOfSslServerCerHeaderFailedExtracted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspNumOfSslServerCerHeaderFailedExtracted.setStatus("current")
_CspNumOfTimesSslHeaderTruncated_Type = Counter32
_CspNumOfTimesSslHeaderTruncated_Object = MibScalar
cspNumOfTimesSslHeaderTruncated = _CspNumOfTimesSslHeaderTruncated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 19, 1, 8),
    _CspNumOfTimesSslHeaderTruncated_Type()
)
cspNumOfTimesSslHeaderTruncated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspNumOfTimesSslHeaderTruncated.setStatus("current")
_CspHttpHeaderInsertedSslClientCertStats_ObjectIdentity = ObjectIdentity
cspHttpHeaderInsertedSslClientCertStats = _CspHttpHeaderInsertedSslClientCertStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 19, 2)
)
_CspNumOfSslClientCertHeaderExtracted_Type = Counter32
_CspNumOfSslClientCertHeaderExtracted_Object = MibScalar
cspNumOfSslClientCertHeaderExtracted = _CspNumOfSslClientCertHeaderExtracted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 19, 2, 1),
    _CspNumOfSslClientCertHeaderExtracted_Type()
)
cspNumOfSslClientCertHeaderExtracted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspNumOfSslClientCertHeaderExtracted.setStatus("current")
_CspNumOfSslClientCertHeaderFailedExtracted_Type = Counter32
_CspNumOfSslClientCertHeaderFailedExtracted_Object = MibScalar
cspNumOfSslClientCertHeaderFailedExtracted = _CspNumOfSslClientCertHeaderFailedExtracted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 19, 2, 2),
    _CspNumOfSslClientCertHeaderFailedExtracted_Type()
)
cspNumOfSslClientCertHeaderFailedExtracted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspNumOfSslClientCertHeaderFailedExtracted.setStatus("current")
_CspHttpRedirectInfo_ObjectIdentity = ObjectIdentity
cspHttpRedirectInfo = _CspHttpRedirectInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 20)
)
_CspHttpRedirectClientCertAuthFailedStats_ObjectIdentity = ObjectIdentity
cspHttpRedirectClientCertAuthFailedStats = _CspHttpRedirectClientCertAuthFailedStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 20, 1)
)
_CspCertNotYetValidRedirect_Type = Counter32
_CspCertNotYetValidRedirect_Object = MibScalar
cspCertNotYetValidRedirect = _CspCertNotYetValidRedirect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 20, 1, 1),
    _CspCertNotYetValidRedirect_Type()
)
cspCertNotYetValidRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspCertNotYetValidRedirect.setStatus("current")
_CspCertExpiredRedirect_Type = Counter32
_CspCertExpiredRedirect_Object = MibScalar
cspCertExpiredRedirect = _CspCertExpiredRedirect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 20, 1, 2),
    _CspCertExpiredRedirect_Type()
)
cspCertExpiredRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspCertExpiredRedirect.setStatus("current")
_CspIssuerCertNotFoundRedirect_Type = Counter32
_CspIssuerCertNotFoundRedirect_Object = MibScalar
cspIssuerCertNotFoundRedirect = _CspIssuerCertNotFoundRedirect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 20, 1, 3),
    _CspIssuerCertNotFoundRedirect_Type()
)
cspIssuerCertNotFoundRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspIssuerCertNotFoundRedirect.setStatus("current")
_CspCertRevokedRedirect_Type = Counter32
_CspCertRevokedRedirect_Object = MibScalar
cspCertRevokedRedirect = _CspCertRevokedRedirect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 20, 1, 4),
    _CspCertRevokedRedirect_Type()
)
cspCertRevokedRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspCertRevokedRedirect.setStatus("current")
_CspNoClientCertSentRedirect_Type = Counter32
_CspNoClientCertSentRedirect_Object = MibScalar
cspNoClientCertSentRedirect = _CspNoClientCertSentRedirect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 20, 1, 5),
    _CspNoClientCertSentRedirect_Type()
)
cspNoClientCertSentRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspNoClientCertSentRedirect.setStatus("current")
_CspNoCrlAvailableRedirect_Type = Counter32
_CspNoCrlAvailableRedirect_Object = MibScalar
cspNoCrlAvailableRedirect = _CspNoCrlAvailableRedirect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 20, 1, 6),
    _CspNoCrlAvailableRedirect_Type()
)
cspNoCrlAvailableRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspNoCrlAvailableRedirect.setStatus("current")
_CspCrlExpiredRedirect_Type = Counter32
_CspCrlExpiredRedirect_Object = MibScalar
cspCrlExpiredRedirect = _CspCrlExpiredRedirect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 20, 1, 7),
    _CspCrlExpiredRedirect_Type()
)
cspCrlExpiredRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspCrlExpiredRedirect.setStatus("current")
_CspCertSignatureFailedRedirect_Type = Counter32
_CspCertSignatureFailedRedirect_Object = MibScalar
cspCertSignatureFailedRedirect = _CspCertSignatureFailedRedirect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 20, 1, 8),
    _CspCertSignatureFailedRedirect_Type()
)
cspCertSignatureFailedRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspCertSignatureFailedRedirect.setStatus("current")
_CspOtherCertErrorRedirect_Type = Counter32
_CspOtherCertErrorRedirect_Object = MibScalar
cspOtherCertErrorRedirect = _CspOtherCertErrorRedirect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 20, 1, 9),
    _CspOtherCertErrorRedirect_Type()
)
cspOtherCertErrorRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspOtherCertErrorRedirect.setStatus("current")
_CspSslResourceNotifInfo_ObjectIdentity = ObjectIdentity
cspSslResourceNotifInfo = _CspSslResourceNotifInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 21)
)


class _CspSslTrapType_Type(Integer32):
    """Custom type cspSslTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fallingHighThresh", 3),
          ("risingHighThresh", 1))
    )


_CspSslTrapType_Type.__name__ = "Integer32"
_CspSslTrapType_Object = MibScalar
cspSslTrapType = _CspSslTrapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 21, 1),
    _CspSslTrapType_Type()
)
cspSslTrapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cspSslTrapType.setStatus("current")
_CspSslMaxConn_Type = Unsigned32
_CspSslMaxConn_Object = MibScalar
cspSslMaxConn = _CspSslMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 21, 2),
    _CspSslMaxConn_Type()
)
cspSslMaxConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cspSslMaxConn.setStatus("current")
if mibBuilder.loadTexts:
    cspSslMaxConn.setUnits("connections per system")
_CspSslActiveConn_Type = Gauge32
_CspSslActiveConn_Object = MibScalar
cspSslActiveConn = _CspSslActiveConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 21, 3),
    _CspSslActiveConn_Type()
)
cspSslActiveConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSslActiveConn.setStatus("current")
if mibBuilder.loadTexts:
    cspSslActiveConn.setUnits("connections per system")
_CspSslConfigHighConnPcnt_Type = Unsigned32
_CspSslConfigHighConnPcnt_Object = MibScalar
cspSslConfigHighConnPcnt = _CspSslConfigHighConnPcnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 21, 4),
    _CspSslConfigHighConnPcnt_Type()
)
cspSslConfigHighConnPcnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cspSslConfigHighConnPcnt.setStatus("current")
if mibBuilder.loadTexts:
    cspSslConfigHighConnPcnt.setUnits("percentage")
_CspSslActiveConnPcnt_Type = Unsigned32
_CspSslActiveConnPcnt_Object = MibScalar
cspSslActiveConnPcnt = _CspSslActiveConnPcnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 21, 5),
    _CspSslActiveConnPcnt_Type()
)
cspSslActiveConnPcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspSslActiveConnPcnt.setStatus("current")
if mibBuilder.loadTexts:
    cspSslActiveConnPcnt.setUnits("percentage")
_CspSslConfigWatermarkConnPcnt_Type = Unsigned32
_CspSslConfigWatermarkConnPcnt_Object = MibScalar
cspSslConfigWatermarkConnPcnt = _CspSslConfigWatermarkConnPcnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 1, 21, 6),
    _CspSslConfigWatermarkConnPcnt_Type()
)
cspSslConfigWatermarkConnPcnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cspSslConfigWatermarkConnPcnt.setStatus("current")
if mibBuilder.loadTexts:
    cspSslConfigWatermarkConnPcnt.setUnits("percentage")
_CspMIBConformance_ObjectIdentity = ObjectIdentity
cspMIBConformance = _CspMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 2)
)
_CspMIBCompliances_ObjectIdentity = ObjectIdentity
cspMIBCompliances = _CspMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 2, 1)
)
_CspMIBGroups_ObjectIdentity = ObjectIdentity
cspMIBGroups = _CspMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 2, 2)
)
cspPsEntry.registerAugmentions(
    ("CISCO-SSL-PROXY-MIB",
     "cspPsPolicyEntry")
)
cspPsPolicyEntry.setIndexNames(*cspPsEntry.getIndexNames())

# Managed Objects groups

cspGlobalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 2, 2, 1)
)
cspGlobalConfigGroup.setObjects(
      *(("CISCO-SSL-PROXY-MIB", "cspGcVersion"),
        ("CISCO-SSL-PROXY-MIB", "cspGcFIPSMode"),
        ("CISCO-SSL-PROXY-MIB", "cspGcRSArc4128md5"),
        ("CISCO-SSL-PROXY-MIB", "cspGcRSArc4128sha"),
        ("CISCO-SSL-PROXY-MIB", "cspGcRSAdescbcsha"),
        ("CISCO-SSL-PROXY-MIB", "cspGcRSA3descbcsha"),
        ("CISCO-SSL-PROXY-MIB", "cspGcNotifyProxyServOperStatus"),
        ("CISCO-SSL-PROXY-MIB", "cspGcNotifyPSCertExpiring"),
        ("CISCO-SSL-PROXY-MIB", "cspGcPSCertExpireInterval"))
)
if mibBuilder.loadTexts:
    cspGlobalConfigGroup.setStatus("current")

cspProxyServiceConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 2, 2, 2)
)
cspProxyServiceConfigGroup.setObjects(
      *(("CISCO-SSL-PROXY-MIB", "cspPsServiceType"),
        ("CISCO-SSL-PROXY-MIB", "cspPsVirtualAddressType"),
        ("CISCO-SSL-PROXY-MIB", "cspPsVirtualAddress"),
        ("CISCO-SSL-PROXY-MIB", "cspPsVirtualPort"),
        ("CISCO-SSL-PROXY-MIB", "cspPsServerAddressType"),
        ("CISCO-SSL-PROXY-MIB", "cspPsServerAddress"),
        ("CISCO-SSL-PROXY-MIB", "cspPsServerPort"),
        ("CISCO-SSL-PROXY-MIB", "cspPsAdminStatus"),
        ("CISCO-SSL-PROXY-MIB", "cspPsOperStatus"),
        ("CISCO-SSL-PROXY-MIB", "cspPsOperDownReason"),
        ("CISCO-SSL-PROXY-MIB", "cspPsConfigRowStatus"),
        ("CISCO-SSL-PROXY-MIB", "cspPspVirTcpPolicyName"),
        ("CISCO-SSL-PROXY-MIB", "cspPspSerTcpPolicyName"),
        ("CISCO-SSL-PROXY-MIB", "cspPspSslPolicyName"),
        ("CISCO-SSL-PROXY-MIB", "cspPspHttpHdrPolicyName"),
        ("CISCO-SSL-PROXY-MIB", "cspPspUrlRewritePolicyName"),
        ("CISCO-SSL-PROXY-MIB", "cspPskcTrustPointName"),
        ("CISCO-SSL-PROXY-MIB", "cspPskcCertFileName"),
        ("CISCO-SSL-PROXY-MIB", "cspPskcKeyName"),
        ("CISCO-SSL-PROXY-MIB", "cspPskcKeyFileName"),
        ("CISCO-SSL-PROXY-MIB", "cspPskcKeySize"),
        ("CISCO-SSL-PROXY-MIB", "cspPskcKeyTime"),
        ("CISCO-SSL-PROXY-MIB", "cspPskcCertStatus"),
        ("CISCO-SSL-PROXY-MIB", "cspPskcCertSubjName"),
        ("CISCO-SSL-PROXY-MIB", "cspPskcCertSerialNum"),
        ("CISCO-SSL-PROXY-MIB", "cspPskcIssuerName"),
        ("CISCO-SSL-PROXY-MIB", "cspPskcIssuerCertSerialNum"),
        ("CISCO-SSL-PROXY-MIB", "cspPskcCertStartDate"),
        ("CISCO-SSL-PROXY-MIB", "cspPskcCertEndDate"),
        ("CISCO-SSL-PROXY-MIB", "cspPskcConfigRowStatus"))
)
if mibBuilder.loadTexts:
    cspProxyServiceConfigGroup.setStatus("current")

cspPolicyConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 2, 2, 3)
)
cspPolicyConfigGroup.setObjects(
      *(("CISCO-SSL-PROXY-MIB", "cspTpSynTimeOut"),
        ("CISCO-SSL-PROXY-MIB", "cspTpInActivityTimeOut"),
        ("CISCO-SSL-PROXY-MIB", "cspTpNagleAlgo"),
        ("CISCO-SSL-PROXY-MIB", "cspTpFinWaitTimeOut"),
        ("CISCO-SSL-PROXY-MIB", "cspTpReassemTimeOut"),
        ("CISCO-SSL-PROXY-MIB", "cspTpRcvBufShrLim"),
        ("CISCO-SSL-PROXY-MIB", "cspTpTransBufShrLim"),
        ("CISCO-SSL-PROXY-MIB", "cspTpMss"),
        ("CISCO-SSL-PROXY-MIB", "cspTpPathMtuDisc"),
        ("CISCO-SSL-PROXY-MIB", "cspTpConfigRowStatus"),
        ("CISCO-SSL-PROXY-MIB", "cspSpRSArc4128md5"),
        ("CISCO-SSL-PROXY-MIB", "cspSpRSArc4128sha"),
        ("CISCO-SSL-PROXY-MIB", "cspSpRSAdescbcsha"),
        ("CISCO-SSL-PROXY-MIB", "cspSpRSA3descbcsha"),
        ("CISCO-SSL-PROXY-MIB", "cspSpProtocol"),
        ("CISCO-SSL-PROXY-MIB", "cspSpCloseProtocol"),
        ("CISCO-SSL-PROXY-MIB", "cspSpSessionCache"),
        ("CISCO-SSL-PROXY-MIB", "cspSpSessionTimeOut"),
        ("CISCO-SSL-PROXY-MIB", "cspSpConfigRowStatus"))
)
if mibBuilder.loadTexts:
    cspPolicyConfigGroup.setStatus("current")

cspTcpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 2, 2, 4)
)
cspTcpGroup.setObjects(
      *(("CISCO-SSL-PROXY-MIB", "cspTcpCountersClearTime"),
        ("CISCO-SSL-PROXY-MIB", "cspTcConnInit"),
        ("CISCO-SSL-PROXY-MIB", "cspTcConnAccept"),
        ("CISCO-SSL-PROXY-MIB", "cspTcConnEstab"),
        ("CISCO-SSL-PROXY-MIB", "cspTcConnDrop"),
        ("CISCO-SSL-PROXY-MIB", "cspTcConnClosed"),
        ("CISCO-SSL-PROXY-MIB", "cspTcSynTimeOuts"),
        ("CISCO-SSL-PROXY-MIB", "cspTcIdleTimeOuts"),
        ("CISCO-SSL-PROXY-MIB", "cspTcTotalPktSent"),
        ("CISCO-SSL-PROXY-MIB", "cspTcDataPktSent"),
        ("CISCO-SSL-PROXY-MIB", "cspTcDataByteSent"),
        ("CISCO-SSL-PROXY-MIB", "cspTcTotalPktRcv"),
        ("CISCO-SSL-PROXY-MIB", "cspTcPktRcvSeq"),
        ("CISCO-SSL-PROXY-MIB", "cspTcByteRcvSeq"))
)
if mibBuilder.loadTexts:
    cspTcpGroup.setStatus("current")

cspSslGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 2, 2, 5)
)
cspSslGroup.setObjects(
      *(("CISCO-SSL-PROXY-MIB", "cspSslCountersClearTime"),
        ("CISCO-SSL-PROXY-MIB", "cspScConnAttempt"),
        ("CISCO-SSL-PROXY-MIB", "cspScConnComplete"),
        ("CISCO-SSL-PROXY-MIB", "cspScConnInHandShake"),
        ("CISCO-SSL-PROXY-MIB", "cspScConnInDataPhase"),
        ("CISCO-SSL-PROXY-MIB", "cspScRenegAttempt"),
        ("CISCO-SSL-PROXY-MIB", "cspScConnInReneg"),
        ("CISCO-SSL-PROXY-MIB", "cspScActiveSessions"),
        ("CISCO-SSL-PROXY-MIB", "cspScMaxHandShakeConns"),
        ("CISCO-SSL-PROXY-MIB", "cspScCurrDeviceQLen"),
        ("CISCO-SSL-PROXY-MIB", "cspScMaxDeviceQLen"),
        ("CISCO-SSL-PROXY-MIB", "cspScSessionReuses"))
)
if mibBuilder.loadTexts:
    cspSslGroup.setStatus("current")

cspSsl3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 2, 2, 6)
)
cspSsl3Group.setObjects(
      *(("CISCO-SSL-PROXY-MIB", "cspS3cFullHandShake"),
        ("CISCO-SSL-PROXY-MIB", "cspS3cResumedHandShake"),
        ("CISCO-SSL-PROXY-MIB", "cspS3cHandShakeFailed"),
        ("CISCO-SSL-PROXY-MIB", "cspS3cDataFailed"),
        ("CISCO-SSL-PROXY-MIB", "cspS3cBadMacRcvd"),
        ("CISCO-SSL-PROXY-MIB", "cspS3cPadErrors"),
        ("CISCO-SSL-PROXY-MIB", "cspS3cRSArc4128md5"),
        ("CISCO-SSL-PROXY-MIB", "cspS3cRSArc4128sha"),
        ("CISCO-SSL-PROXY-MIB", "cspS3cRSAdescbcsha"),
        ("CISCO-SSL-PROXY-MIB", "cspS3cRSA3desedecbcsha"))
)
if mibBuilder.loadTexts:
    cspSsl3Group.setStatus("current")

cspTls1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 2, 2, 7)
)
cspTls1Group.setObjects(
      *(("CISCO-SSL-PROXY-MIB", "cspTlcFullHandShake"),
        ("CISCO-SSL-PROXY-MIB", "cspTlcResumedHandShake"),
        ("CISCO-SSL-PROXY-MIB", "cspTlcHandShakeFailed"),
        ("CISCO-SSL-PROXY-MIB", "cspTlcDataFailed"),
        ("CISCO-SSL-PROXY-MIB", "cspTlcBadMacRcvd"),
        ("CISCO-SSL-PROXY-MIB", "cspTlcPadErrors"),
        ("CISCO-SSL-PROXY-MIB", "cspTlcRSArc4128md5"),
        ("CISCO-SSL-PROXY-MIB", "cspTlcRSArc4128sha"),
        ("CISCO-SSL-PROXY-MIB", "cspTlcRSAdescbcsha"),
        ("CISCO-SSL-PROXY-MIB", "cspTlcRSA3desedecbcsha"))
)
if mibBuilder.loadTexts:
    cspTls1Group.setStatus("current")

cspSslCryptoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 2, 2, 8)
)
cspSslCryptoGroup.setObjects(
      *(("CISCO-SSL-PROXY-MIB", "cspSccBlksEncrypted"),
        ("CISCO-SSL-PROXY-MIB", "cspSccBlksDecrypted"),
        ("CISCO-SSL-PROXY-MIB", "cspSccBytesEncrypted"),
        ("CISCO-SSL-PROXY-MIB", "cspSccBytesDecrypted"),
        ("CISCO-SSL-PROXY-MIB", "cspSccPublicKeyOpers"),
        ("CISCO-SSL-PROXY-MIB", "cspSccPrivateKeyOpers"),
        ("CISCO-SSL-PROXY-MIB", "cspSccCryptoFails"),
        ("CISCO-SSL-PROXY-MIB", "cspSccDmaErrors"))
)
if mibBuilder.loadTexts:
    cspSslCryptoGroup.setStatus("current")

cspSslErrorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 2, 2, 9)
)
cspSslErrorGroup.setObjects(
      *(("CISCO-SSL-PROXY-MIB", "cspSecSessAllocFailed"),
        ("CISCO-SSL-PROXY-MIB", "cspSecSessLimitExceed"),
        ("CISCO-SSL-PROXY-MIB", "cspSecHShakeInitFailed"),
        ("CISCO-SSL-PROXY-MIB", "cspSecRenegFailed"),
        ("CISCO-SSL-PROXY-MIB", "cspSecFatalAlertsRcvd"),
        ("CISCO-SSL-PROXY-MIB", "cspSecFatalAlertsSent"),
        ("CISCO-SSL-PROXY-MIB", "cspSecNoCipherAlerts"),
        ("CISCO-SSL-PROXY-MIB", "cspSecVerMismatchAlerts"),
        ("CISCO-SSL-PROXY-MIB", "cspSecNoComprsnAlerts"),
        ("CISCO-SSL-PROXY-MIB", "cspSecHShakeHndleMemFail"),
        ("CISCO-SSL-PROXY-MIB", "cspSecStalePakDrop"),
        ("CISCO-SSL-PROXY-MIB", "cspSecServiceIdDiscard"),
        ("CISCO-SSL-PROXY-MIB", "cspSecHShakeLimitExceed"),
        ("CISCO-SSL-PROXY-MIB", "cspSecDevConnCtxtFail"),
        ("CISCO-SSL-PROXY-MIB", "cspSecMemAllocFailed"),
        ("CISCO-SSL-PROXY-MIB", "cspSecBuffAllocFailed"),
        ("CISCO-SSL-PROXY-MIB", "cspSecAlertSendFailed"),
        ("CISCO-SSL-PROXY-MIB", "cspSecOverloadDropped"),
        ("CISCO-SSL-PROXY-MIB", "cspSecConnAborted"))
)
if mibBuilder.loadTexts:
    cspSslErrorGroup.setStatus("current")

cspProxyServiceStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 2, 2, 10)
)
cspProxyServiceStatsGroup.setObjects(
      *(("CISCO-SSL-PROXY-MIB", "cspPscClearTime"),
        ("CISCO-SSL-PROXY-MIB", "cspPscConnAttempt"),
        ("CISCO-SSL-PROXY-MIB", "cspPscConnComplete"),
        ("CISCO-SSL-PROXY-MIB", "cspPscFullHandShake"),
        ("CISCO-SSL-PROXY-MIB", "cspPscResumedHandShake"),
        ("CISCO-SSL-PROXY-MIB", "cspPscConnInHandShake"),
        ("CISCO-SSL-PROXY-MIB", "cspPscConnInDataPhase"),
        ("CISCO-SSL-PROXY-MIB", "cspPscRenegAttempt"),
        ("CISCO-SSL-PROXY-MIB", "cspPscConnInReneg"),
        ("CISCO-SSL-PROXY-MIB", "cspPscBlksEncrypted"),
        ("CISCO-SSL-PROXY-MIB", "cspPscBlksDecrypted"),
        ("CISCO-SSL-PROXY-MIB", "cspPscBytesEncrypted"),
        ("CISCO-SSL-PROXY-MIB", "cspPscBytesDecrypted"),
        ("CISCO-SSL-PROXY-MIB", "cspPscValidSessions"),
        ("CISCO-SSL-PROXY-MIB", "cspPscSessLimitExceed"),
        ("CISCO-SSL-PROXY-MIB", "cspPscHandShakeFailed"),
        ("CISCO-SSL-PROXY-MIB", "cspPscDataFailed"),
        ("CISCO-SSL-PROXY-MIB", "cspPscFatalAlertsRcvd"),
        ("CISCO-SSL-PROXY-MIB", "cspPscFatalAlertsSent"),
        ("CISCO-SSL-PROXY-MIB", "cspPscBadMacRcvd"),
        ("CISCO-SSL-PROXY-MIB", "cspPscPadErrors"),
        ("CISCO-SSL-PROXY-MIB", "cspPscNoCipherAlerts"),
        ("CISCO-SSL-PROXY-MIB", "cspPscNoComprsnAlerts"),
        ("CISCO-SSL-PROXY-MIB", "cspPscVerMismatchAlerts"))
)
if mibBuilder.loadTexts:
    cspProxyServiceStatsGroup.setStatus("current")

cspProxyServiceSsl3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 2, 2, 11)
)
cspProxyServiceSsl3Group.setObjects(
      *(("CISCO-SSL-PROXY-MIB", "cspPs3cClearTime"),
        ("CISCO-SSL-PROXY-MIB", "cspPs3cFullHandShake"),
        ("CISCO-SSL-PROXY-MIB", "cspPs3cResumedHandShake"),
        ("CISCO-SSL-PROXY-MIB", "cspPs3cHandShakeFailed"),
        ("CISCO-SSL-PROXY-MIB", "cspPs3cDataFailed"),
        ("CISCO-SSL-PROXY-MIB", "cspPs3cBadMacRcvd"),
        ("CISCO-SSL-PROXY-MIB", "cspPs3cPadErrors"),
        ("CISCO-SSL-PROXY-MIB", "cspPs3cRSArc4128md5"),
        ("CISCO-SSL-PROXY-MIB", "cspPs3cRSArc4128sha"),
        ("CISCO-SSL-PROXY-MIB", "cspPs3cRSAdescbcsha"),
        ("CISCO-SSL-PROXY-MIB", "cspPs3cRSA3desedecbcsha"))
)
if mibBuilder.loadTexts:
    cspProxyServiceSsl3Group.setStatus("current")

cspProxyServiceTls1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 2, 2, 12)
)
cspProxyServiceTls1Group.setObjects(
      *(("CISCO-SSL-PROXY-MIB", "cspPt1cClearTime"),
        ("CISCO-SSL-PROXY-MIB", "cspPt1cFullHandShake"),
        ("CISCO-SSL-PROXY-MIB", "cspPt1cResumedHandShake"),
        ("CISCO-SSL-PROXY-MIB", "cspPt1cHandShakeFailed"),
        ("CISCO-SSL-PROXY-MIB", "cspPt1cDataFailed"),
        ("CISCO-SSL-PROXY-MIB", "cspPt1cBadMacRcvd"),
        ("CISCO-SSL-PROXY-MIB", "cspPt1cPadErrors"),
        ("CISCO-SSL-PROXY-MIB", "cspPt1cRSArc4128md5"),
        ("CISCO-SSL-PROXY-MIB", "cspPt1cRSArc4128sha"),
        ("CISCO-SSL-PROXY-MIB", "cspPt1cRSAdescbcsha"),
        ("CISCO-SSL-PROXY-MIB", "cspPt1cRSA3desedecbcsha"))
)
if mibBuilder.loadTexts:
    cspProxyServiceTls1Group.setStatus("current")

cspCpuStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 2, 2, 13)
)
cspCpuStatusGroup.setObjects(
      *(("CISCO-SSL-PROXY-MIB", "cspCpuStatus"),
        ("CISCO-SSL-PROXY-MIB", "cspCpuClearTime"),
        ("CISCO-SSL-PROXY-MIB", "cspCpuProcessUtil"),
        ("CISCO-SSL-PROXY-MIB", "cspCpuInterruptUtil"),
        ("CISCO-SSL-PROXY-MIB", "cspCpuProcessUtilIn5Sec"),
        ("CISCO-SSL-PROXY-MIB", "cspCpuProcessUtilIn1Min"),
        ("CISCO-SSL-PROXY-MIB", "cspCpuProcessUtilIn5Min"),
        ("CISCO-SSL-PROXY-MIB", "cspCpuInterruptUtilIn5Sec"),
        ("CISCO-SSL-PROXY-MIB", "cspCpuInterruptUtilIn1Min"),
        ("CISCO-SSL-PROXY-MIB", "cspCpuInterruptUtilIn5Min"))
)
if mibBuilder.loadTexts:
    cspCpuStatusGroup.setStatus("current")

cspHttpHeaderInsertedSslInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 2, 2, 15)
)
cspHttpHeaderInsertedSslInfoGroup.setObjects(
      *(("CISCO-SSL-PROXY-MIB", "cspNumOfSslInfoSuccessInserted"),
        ("CISCO-SSL-PROXY-MIB", "cspNumOfSslInfoFailedInserted"),
        ("CISCO-SSL-PROXY-MIB", "cspNumOfSpoofHttpHeaderDeleted"),
        ("CISCO-SSL-PROXY-MIB", "cspNumOfSslSessHeaderExtracted"),
        ("CISCO-SSL-PROXY-MIB", "cspNumOfSslSessHeaderFailedExtracted"),
        ("CISCO-SSL-PROXY-MIB", "cspNumOfSslServerCertHeaderExtracted"),
        ("CISCO-SSL-PROXY-MIB", "cspNumOfSslServerCerHeaderFailedExtracted"),
        ("CISCO-SSL-PROXY-MIB", "cspNumOfTimesSslHeaderTruncated"))
)
if mibBuilder.loadTexts:
    cspHttpHeaderInsertedSslInfoGroup.setStatus("current")

cspHttpHeaderInsertedSslClientCertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 2, 2, 16)
)
cspHttpHeaderInsertedSslClientCertGroup.setObjects(
      *(("CISCO-SSL-PROXY-MIB", "cspNumOfSslClientCertHeaderExtracted"),
        ("CISCO-SSL-PROXY-MIB", "cspNumOfSslClientCertHeaderFailedExtracted"))
)
if mibBuilder.loadTexts:
    cspHttpHeaderInsertedSslClientCertGroup.setStatus("current")

cspHttpRedirectInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 2, 2, 17)
)
cspHttpRedirectInfoGroup.setObjects(
      *(("CISCO-SSL-PROXY-MIB", "cspCertNotYetValidRedirect"),
        ("CISCO-SSL-PROXY-MIB", "cspCertExpiredRedirect"),
        ("CISCO-SSL-PROXY-MIB", "cspIssuerCertNotFoundRedirect"),
        ("CISCO-SSL-PROXY-MIB", "cspCertRevokedRedirect"),
        ("CISCO-SSL-PROXY-MIB", "cspNoClientCertSentRedirect"),
        ("CISCO-SSL-PROXY-MIB", "cspNoCrlAvailableRedirect"),
        ("CISCO-SSL-PROXY-MIB", "cspCrlExpiredRedirect"),
        ("CISCO-SSL-PROXY-MIB", "cspCertSignatureFailedRedirect"),
        ("CISCO-SSL-PROXY-MIB", "cspOtherCertErrorRedirect"))
)
if mibBuilder.loadTexts:
    cspHttpRedirectInfoGroup.setStatus("current")

cspSslResourceLimitNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 2, 2, 18)
)
cspSslResourceLimitNotifObjectsGroup.setObjects(
      *(("CISCO-SSL-PROXY-MIB", "cspSslTrapType"),
        ("CISCO-SSL-PROXY-MIB", "cspSslMaxConn"),
        ("CISCO-SSL-PROXY-MIB", "cspSslActiveConn"),
        ("CISCO-SSL-PROXY-MIB", "cspSslConfigHighConnPcnt"),
        ("CISCO-SSL-PROXY-MIB", "cspSslActiveConnPcnt"),
        ("CISCO-SSL-PROXY-MIB", "cspSslConfigWatermarkConnPcnt"))
)
if mibBuilder.loadTexts:
    cspSslResourceLimitNotifObjectsGroup.setStatus("current")


# Notification objects

cspServOperStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 0, 1)
)
cspServOperStatus.setObjects(
      *(("CISCO-SSL-PROXY-MIB", "cspPsOperStatus"),
        ("CISCO-SSL-PROXY-MIB", "cspPsOperDownReason"))
)
if mibBuilder.loadTexts:
    cspServOperStatus.setStatus(
        "current"
    )

cspServCertExpiring = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 0, 2)
)
cspServCertExpiring.setObjects(
      *(("CISCO-SSL-PROXY-MIB", "cspPskcCertSubjName"),
        ("CISCO-SSL-PROXY-MIB", "cspPskcCertSerialNum"),
        ("CISCO-SSL-PROXY-MIB", "cspPskcIssuerName"),
        ("CISCO-SSL-PROXY-MIB", "cspPskcIssuerCertSerialNum"),
        ("CISCO-SSL-PROXY-MIB", "cspPskcCertEndDate"))
)
if mibBuilder.loadTexts:
    cspServCertExpiring.setStatus(
        "current"
    )

cspSSLResourceLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 0, 3)
)
cspSSLResourceLimitReached.setObjects(
      *(("CISCO-SSL-PROXY-MIB", "cspSslTrapType"),
        ("CISCO-SSL-PROXY-MIB", "cspSslMaxConn"),
        ("CISCO-SSL-PROXY-MIB", "cspSslActiveConn"),
        ("CISCO-SSL-PROXY-MIB", "cspSslConfigHighConnPcnt"),
        ("CISCO-SSL-PROXY-MIB", "cspSslActiveConnPcnt"),
        ("CISCO-SSL-PROXY-MIB", "cspSslConfigWatermarkConnPcnt"))
)
if mibBuilder.loadTexts:
    cspSSLResourceLimitReached.setStatus(
        "current"
    )


# Notifications groups

cspProxyServiceNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 2, 2, 14)
)
cspProxyServiceNotificationGroup.setObjects(
      *(("CISCO-SSL-PROXY-MIB", "cspServOperStatus"),
        ("CISCO-SSL-PROXY-MIB", "cspServCertExpiring"))
)
if mibBuilder.loadTexts:
    cspProxyServiceNotificationGroup.setStatus(
        "current"
    )

cspSslResourceLimitNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 2, 2, 19)
)
cspSslResourceLimitNotifGroup.setObjects(
    ("CISCO-SSL-PROXY-MIB", "cspSSLResourceLimitReached")
)
if mibBuilder.loadTexts:
    cspSslResourceLimitNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cspMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cspMIBCompliance.setStatus(
        "deprecated"
    )

cspMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cspMIBComplianceRev1.setStatus(
        "deprecated"
    )

cspMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 370, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cspMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SSL-PROXY-MIB",
    **{"ciscoSslProxyMIB": ciscoSslProxyMIB,
       "cspMIBNotifications": cspMIBNotifications,
       "cspServOperStatus": cspServOperStatus,
       "cspServCertExpiring": cspServCertExpiring,
       "cspSSLResourceLimitReached": cspSSLResourceLimitReached,
       "cspMIBObjects": cspMIBObjects,
       "cspGlobalConfig": cspGlobalConfig,
       "cspGcVersion": cspGcVersion,
       "cspGcFIPSMode": cspGcFIPSMode,
       "cspGcRSArc4128md5": cspGcRSArc4128md5,
       "cspGcRSArc4128sha": cspGcRSArc4128sha,
       "cspGcRSAdescbcsha": cspGcRSAdescbcsha,
       "cspGcRSA3descbcsha": cspGcRSA3descbcsha,
       "cspGcNotifyProxyServOperStatus": cspGcNotifyProxyServOperStatus,
       "cspGcNotifyPSCertExpiring": cspGcNotifyPSCertExpiring,
       "cspGcPSCertExpireInterval": cspGcPSCertExpireInterval,
       "cspPsConfig": cspPsConfig,
       "cspPsTable": cspPsTable,
       "cspPsEntry": cspPsEntry,
       "cspPsName": cspPsName,
       "cspPsListIndex": cspPsListIndex,
       "cspPsServiceType": cspPsServiceType,
       "cspPsVirtualAddressType": cspPsVirtualAddressType,
       "cspPsVirtualAddress": cspPsVirtualAddress,
       "cspPsVirtualPort": cspPsVirtualPort,
       "cspPsServerAddressType": cspPsServerAddressType,
       "cspPsServerAddress": cspPsServerAddress,
       "cspPsServerPort": cspPsServerPort,
       "cspPsAdminStatus": cspPsAdminStatus,
       "cspPsOperStatus": cspPsOperStatus,
       "cspPsOperDownReason": cspPsOperDownReason,
       "cspPsConfigRowStatus": cspPsConfigRowStatus,
       "cspPsPolicyConfig": cspPsPolicyConfig,
       "cspPsPolicyTable": cspPsPolicyTable,
       "cspPsPolicyEntry": cspPsPolicyEntry,
       "cspPspVirTcpPolicyName": cspPspVirTcpPolicyName,
       "cspPspSerTcpPolicyName": cspPspSerTcpPolicyName,
       "cspPspSslPolicyName": cspPspSslPolicyName,
       "cspPspHttpHdrPolicyName": cspPspHttpHdrPolicyName,
       "cspPspUrlRewritePolicyName": cspPspUrlRewritePolicyName,
       "cspPsKeyCertConfig": cspPsKeyCertConfig,
       "cspPsKeyCertTable": cspPsKeyCertTable,
       "cspPsKeyCertEntry": cspPsKeyCertEntry,
       "cspPskcKeyUsage": cspPskcKeyUsage,
       "cspPskcTrustPointName": cspPskcTrustPointName,
       "cspPskcCertFileName": cspPskcCertFileName,
       "cspPskcKeyName": cspPskcKeyName,
       "cspPskcKeyFileName": cspPskcKeyFileName,
       "cspPskcKeySize": cspPskcKeySize,
       "cspPskcKeyTime": cspPskcKeyTime,
       "cspPskcCertStatus": cspPskcCertStatus,
       "cspPskcCertSubjName": cspPskcCertSubjName,
       "cspPskcCertSerialNum": cspPskcCertSerialNum,
       "cspPskcIssuerName": cspPskcIssuerName,
       "cspPskcIssuerCertSerialNum": cspPskcIssuerCertSerialNum,
       "cspPskcCertStartDate": cspPskcCertStartDate,
       "cspPskcCertEndDate": cspPskcCertEndDate,
       "cspPskcConfigRowStatus": cspPskcConfigRowStatus,
       "cspTcpPolicyConfig": cspTcpPolicyConfig,
       "cspTcpPolicyTable": cspTcpPolicyTable,
       "cspTcpPolicyEntry": cspTcpPolicyEntry,
       "cspTpPolicyName": cspTpPolicyName,
       "cspTpSynTimeOut": cspTpSynTimeOut,
       "cspTpInActivityTimeOut": cspTpInActivityTimeOut,
       "cspTpNagleAlgo": cspTpNagleAlgo,
       "cspTpFinWaitTimeOut": cspTpFinWaitTimeOut,
       "cspTpReassemTimeOut": cspTpReassemTimeOut,
       "cspTpRcvBufShrLim": cspTpRcvBufShrLim,
       "cspTpTransBufShrLim": cspTpTransBufShrLim,
       "cspTpMss": cspTpMss,
       "cspTpPathMtuDisc": cspTpPathMtuDisc,
       "cspTpConfigRowStatus": cspTpConfigRowStatus,
       "cspSslPolicyConfig": cspSslPolicyConfig,
       "cspSslPolicyTable": cspSslPolicyTable,
       "cspSslPolicyEntry": cspSslPolicyEntry,
       "cspSpPolicyName": cspSpPolicyName,
       "cspSpRSArc4128md5": cspSpRSArc4128md5,
       "cspSpRSArc4128sha": cspSpRSArc4128sha,
       "cspSpRSAdescbcsha": cspSpRSAdescbcsha,
       "cspSpRSA3descbcsha": cspSpRSA3descbcsha,
       "cspSpProtocol": cspSpProtocol,
       "cspSpCloseProtocol": cspSpCloseProtocol,
       "cspSpSessionCache": cspSpSessionCache,
       "cspSpSessionTimeOut": cspSpSessionTimeOut,
       "cspSpConfigRowStatus": cspSpConfigRowStatus,
       "cspTcpCountersInfo": cspTcpCountersInfo,
       "cspTcpCountersClearTime": cspTcpCountersClearTime,
       "cspTcpCounters": cspTcpCounters,
       "cspTcConnInit": cspTcConnInit,
       "cspTcConnAccept": cspTcConnAccept,
       "cspTcConnEstab": cspTcConnEstab,
       "cspTcConnDrop": cspTcConnDrop,
       "cspTcConnClosed": cspTcConnClosed,
       "cspTcSynTimeOuts": cspTcSynTimeOuts,
       "cspTcIdleTimeOuts": cspTcIdleTimeOuts,
       "cspTcTotalPktSent": cspTcTotalPktSent,
       "cspTcDataPktSent": cspTcDataPktSent,
       "cspTcDataByteSent": cspTcDataByteSent,
       "cspTcTotalPktRcv": cspTcTotalPktRcv,
       "cspTcPktRcvSeq": cspTcPktRcvSeq,
       "cspTcByteRcvSeq": cspTcByteRcvSeq,
       "cspSslCountersInfo": cspSslCountersInfo,
       "cspSslCountersClearTime": cspSslCountersClearTime,
       "cspSslCounters": cspSslCounters,
       "cspScConnAttempt": cspScConnAttempt,
       "cspScConnComplete": cspScConnComplete,
       "cspScConnInHandShake": cspScConnInHandShake,
       "cspScConnInDataPhase": cspScConnInDataPhase,
       "cspScRenegAttempt": cspScRenegAttempt,
       "cspScConnInReneg": cspScConnInReneg,
       "cspScActiveSessions": cspScActiveSessions,
       "cspScMaxHandShakeConns": cspScMaxHandShakeConns,
       "cspScCurrDeviceQLen": cspScCurrDeviceQLen,
       "cspScMaxDeviceQLen": cspScMaxDeviceQLen,
       "cspScSessionReuses": cspScSessionReuses,
       "cspSsl3Counters": cspSsl3Counters,
       "cspS3cFullHandShake": cspS3cFullHandShake,
       "cspS3cResumedHandShake": cspS3cResumedHandShake,
       "cspS3cHandShakeFailed": cspS3cHandShakeFailed,
       "cspS3cDataFailed": cspS3cDataFailed,
       "cspS3cBadMacRcvd": cspS3cBadMacRcvd,
       "cspS3cPadErrors": cspS3cPadErrors,
       "cspS3cRSArc4128md5": cspS3cRSArc4128md5,
       "cspS3cRSArc4128sha": cspS3cRSArc4128sha,
       "cspS3cRSAdescbcsha": cspS3cRSAdescbcsha,
       "cspS3cRSA3desedecbcsha": cspS3cRSA3desedecbcsha,
       "cspTls1Counters": cspTls1Counters,
       "cspTlcFullHandShake": cspTlcFullHandShake,
       "cspTlcResumedHandShake": cspTlcResumedHandShake,
       "cspTlcHandShakeFailed": cspTlcHandShakeFailed,
       "cspTlcDataFailed": cspTlcDataFailed,
       "cspTlcBadMacRcvd": cspTlcBadMacRcvd,
       "cspTlcPadErrors": cspTlcPadErrors,
       "cspTlcRSArc4128md5": cspTlcRSArc4128md5,
       "cspTlcRSArc4128sha": cspTlcRSArc4128sha,
       "cspTlcRSAdescbcsha": cspTlcRSAdescbcsha,
       "cspTlcRSA3desedecbcsha": cspTlcRSA3desedecbcsha,
       "cspSslCryptoCounters": cspSslCryptoCounters,
       "cspSccBlksEncrypted": cspSccBlksEncrypted,
       "cspSccBlksDecrypted": cspSccBlksDecrypted,
       "cspSccBytesEncrypted": cspSccBytesEncrypted,
       "cspSccBytesDecrypted": cspSccBytesDecrypted,
       "cspSccPublicKeyOpers": cspSccPublicKeyOpers,
       "cspSccPrivateKeyOpers": cspSccPrivateKeyOpers,
       "cspSccCryptoFails": cspSccCryptoFails,
       "cspSccDmaErrors": cspSccDmaErrors,
       "cspSslErrorCounters": cspSslErrorCounters,
       "cspSecSessAllocFailed": cspSecSessAllocFailed,
       "cspSecSessLimitExceed": cspSecSessLimitExceed,
       "cspSecHShakeInitFailed": cspSecHShakeInitFailed,
       "cspSecRenegFailed": cspSecRenegFailed,
       "cspSecFatalAlertsRcvd": cspSecFatalAlertsRcvd,
       "cspSecFatalAlertsSent": cspSecFatalAlertsSent,
       "cspSecNoCipherAlerts": cspSecNoCipherAlerts,
       "cspSecVerMismatchAlerts": cspSecVerMismatchAlerts,
       "cspSecNoComprsnAlerts": cspSecNoComprsnAlerts,
       "cspSecHShakeHndleMemFail": cspSecHShakeHndleMemFail,
       "cspSecStalePakDrop": cspSecStalePakDrop,
       "cspSecServiceIdDiscard": cspSecServiceIdDiscard,
       "cspSecHShakeLimitExceed": cspSecHShakeLimitExceed,
       "cspSecDevConnCtxtFail": cspSecDevConnCtxtFail,
       "cspSecMemAllocFailed": cspSecMemAllocFailed,
       "cspSecBuffAllocFailed": cspSecBuffAllocFailed,
       "cspSecAlertSendFailed": cspSecAlertSendFailed,
       "cspSecOverloadDropped": cspSecOverloadDropped,
       "cspSecConnAborted": cspSecConnAborted,
       "cspPsCounters": cspPsCounters,
       "cspPsCountersTable": cspPsCountersTable,
       "cspPsCounterEntry": cspPsCounterEntry,
       "cspPscClearTime": cspPscClearTime,
       "cspPscConnAttempt": cspPscConnAttempt,
       "cspPscConnComplete": cspPscConnComplete,
       "cspPscFullHandShake": cspPscFullHandShake,
       "cspPscResumedHandShake": cspPscResumedHandShake,
       "cspPscConnInHandShake": cspPscConnInHandShake,
       "cspPscConnInDataPhase": cspPscConnInDataPhase,
       "cspPscRenegAttempt": cspPscRenegAttempt,
       "cspPscConnInReneg": cspPscConnInReneg,
       "cspPscBlksEncrypted": cspPscBlksEncrypted,
       "cspPscBlksDecrypted": cspPscBlksDecrypted,
       "cspPscBytesEncrypted": cspPscBytesEncrypted,
       "cspPscBytesDecrypted": cspPscBytesDecrypted,
       "cspPscValidSessions": cspPscValidSessions,
       "cspPscSessLimitExceed": cspPscSessLimitExceed,
       "cspPscHandShakeFailed": cspPscHandShakeFailed,
       "cspPscDataFailed": cspPscDataFailed,
       "cspPscFatalAlertsRcvd": cspPscFatalAlertsRcvd,
       "cspPscFatalAlertsSent": cspPscFatalAlertsSent,
       "cspPscBadMacRcvd": cspPscBadMacRcvd,
       "cspPscPadErrors": cspPscPadErrors,
       "cspPscNoCipherAlerts": cspPscNoCipherAlerts,
       "cspPscNoComprsnAlerts": cspPscNoComprsnAlerts,
       "cspPscVerMismatchAlerts": cspPscVerMismatchAlerts,
       "cspPsSsl3Counters": cspPsSsl3Counters,
       "cspPsSsl3CountersTable": cspPsSsl3CountersTable,
       "cspPsSsl3CounterEntry": cspPsSsl3CounterEntry,
       "cspPs3cClearTime": cspPs3cClearTime,
       "cspPs3cFullHandShake": cspPs3cFullHandShake,
       "cspPs3cResumedHandShake": cspPs3cResumedHandShake,
       "cspPs3cHandShakeFailed": cspPs3cHandShakeFailed,
       "cspPs3cDataFailed": cspPs3cDataFailed,
       "cspPs3cBadMacRcvd": cspPs3cBadMacRcvd,
       "cspPs3cPadErrors": cspPs3cPadErrors,
       "cspPs3cRSArc4128md5": cspPs3cRSArc4128md5,
       "cspPs3cRSArc4128sha": cspPs3cRSArc4128sha,
       "cspPs3cRSAdescbcsha": cspPs3cRSAdescbcsha,
       "cspPs3cRSA3desedecbcsha": cspPs3cRSA3desedecbcsha,
       "cspPsTls1Counters": cspPsTls1Counters,
       "cspPsTls1CountersTable": cspPsTls1CountersTable,
       "cspPsTls1CounterEntry": cspPsTls1CounterEntry,
       "cspPt1cClearTime": cspPt1cClearTime,
       "cspPt1cFullHandShake": cspPt1cFullHandShake,
       "cspPt1cResumedHandShake": cspPt1cResumedHandShake,
       "cspPt1cHandShakeFailed": cspPt1cHandShakeFailed,
       "cspPt1cDataFailed": cspPt1cDataFailed,
       "cspPt1cBadMacRcvd": cspPt1cBadMacRcvd,
       "cspPt1cPadErrors": cspPt1cPadErrors,
       "cspPt1cRSArc4128md5": cspPt1cRSArc4128md5,
       "cspPt1cRSArc4128sha": cspPt1cRSArc4128sha,
       "cspPt1cRSAdescbcsha": cspPt1cRSAdescbcsha,
       "cspPt1cRSA3desedecbcsha": cspPt1cRSA3desedecbcsha,
       "cspCpuStatusInfo": cspCpuStatusInfo,
       "cspCpuStatusTable": cspCpuStatusTable,
       "cspCpuStatusEntry": cspCpuStatusEntry,
       "cspCpuName": cspCpuName,
       "cspCpuStatus": cspCpuStatus,
       "cspCpuClearTime": cspCpuClearTime,
       "cspCpuProcessUtil": cspCpuProcessUtil,
       "cspCpuInterruptUtil": cspCpuInterruptUtil,
       "cspCpuProcessUtilIn5Sec": cspCpuProcessUtilIn5Sec,
       "cspCpuProcessUtilIn1Min": cspCpuProcessUtilIn1Min,
       "cspCpuProcessUtilIn5Min": cspCpuProcessUtilIn5Min,
       "cspCpuInterruptUtilIn5Sec": cspCpuInterruptUtilIn5Sec,
       "cspCpuInterruptUtilIn1Min": cspCpuInterruptUtilIn1Min,
       "cspCpuInterruptUtilIn5Min": cspCpuInterruptUtilIn5Min,
       "cspHttpHeaderInsertedInfo": cspHttpHeaderInsertedInfo,
       "cspHttpHeaderInsertedSslInfoStats": cspHttpHeaderInsertedSslInfoStats,
       "cspNumOfSslInfoSuccessInserted": cspNumOfSslInfoSuccessInserted,
       "cspNumOfSslInfoFailedInserted": cspNumOfSslInfoFailedInserted,
       "cspNumOfSpoofHttpHeaderDeleted": cspNumOfSpoofHttpHeaderDeleted,
       "cspNumOfSslSessHeaderExtracted": cspNumOfSslSessHeaderExtracted,
       "cspNumOfSslSessHeaderFailedExtracted": cspNumOfSslSessHeaderFailedExtracted,
       "cspNumOfSslServerCertHeaderExtracted": cspNumOfSslServerCertHeaderExtracted,
       "cspNumOfSslServerCerHeaderFailedExtracted": cspNumOfSslServerCerHeaderFailedExtracted,
       "cspNumOfTimesSslHeaderTruncated": cspNumOfTimesSslHeaderTruncated,
       "cspHttpHeaderInsertedSslClientCertStats": cspHttpHeaderInsertedSslClientCertStats,
       "cspNumOfSslClientCertHeaderExtracted": cspNumOfSslClientCertHeaderExtracted,
       "cspNumOfSslClientCertHeaderFailedExtracted": cspNumOfSslClientCertHeaderFailedExtracted,
       "cspHttpRedirectInfo": cspHttpRedirectInfo,
       "cspHttpRedirectClientCertAuthFailedStats": cspHttpRedirectClientCertAuthFailedStats,
       "cspCertNotYetValidRedirect": cspCertNotYetValidRedirect,
       "cspCertExpiredRedirect": cspCertExpiredRedirect,
       "cspIssuerCertNotFoundRedirect": cspIssuerCertNotFoundRedirect,
       "cspCertRevokedRedirect": cspCertRevokedRedirect,
       "cspNoClientCertSentRedirect": cspNoClientCertSentRedirect,
       "cspNoCrlAvailableRedirect": cspNoCrlAvailableRedirect,
       "cspCrlExpiredRedirect": cspCrlExpiredRedirect,
       "cspCertSignatureFailedRedirect": cspCertSignatureFailedRedirect,
       "cspOtherCertErrorRedirect": cspOtherCertErrorRedirect,
       "cspSslResourceNotifInfo": cspSslResourceNotifInfo,
       "cspSslTrapType": cspSslTrapType,
       "cspSslMaxConn": cspSslMaxConn,
       "cspSslActiveConn": cspSslActiveConn,
       "cspSslConfigHighConnPcnt": cspSslConfigHighConnPcnt,
       "cspSslActiveConnPcnt": cspSslActiveConnPcnt,
       "cspSslConfigWatermarkConnPcnt": cspSslConfigWatermarkConnPcnt,
       "cspMIBConformance": cspMIBConformance,
       "cspMIBCompliances": cspMIBCompliances,
       "cspMIBCompliance": cspMIBCompliance,
       "cspMIBComplianceRev1": cspMIBComplianceRev1,
       "cspMIBComplianceRev2": cspMIBComplianceRev2,
       "cspMIBGroups": cspMIBGroups,
       "cspGlobalConfigGroup": cspGlobalConfigGroup,
       "cspProxyServiceConfigGroup": cspProxyServiceConfigGroup,
       "cspPolicyConfigGroup": cspPolicyConfigGroup,
       "cspTcpGroup": cspTcpGroup,
       "cspSslGroup": cspSslGroup,
       "cspSsl3Group": cspSsl3Group,
       "cspTls1Group": cspTls1Group,
       "cspSslCryptoGroup": cspSslCryptoGroup,
       "cspSslErrorGroup": cspSslErrorGroup,
       "cspProxyServiceStatsGroup": cspProxyServiceStatsGroup,
       "cspProxyServiceSsl3Group": cspProxyServiceSsl3Group,
       "cspProxyServiceTls1Group": cspProxyServiceTls1Group,
       "cspCpuStatusGroup": cspCpuStatusGroup,
       "cspProxyServiceNotificationGroup": cspProxyServiceNotificationGroup,
       "cspHttpHeaderInsertedSslInfoGroup": cspHttpHeaderInsertedSslInfoGroup,
       "cspHttpHeaderInsertedSslClientCertGroup": cspHttpHeaderInsertedSslClientCertGroup,
       "cspHttpRedirectInfoGroup": cspHttpRedirectInfoGroup,
       "cspSslResourceLimitNotifObjectsGroup": cspSslResourceLimitNotifObjectsGroup,
       "cspSslResourceLimitNotifGroup": cspSslResourceLimitNotifGroup}
)
