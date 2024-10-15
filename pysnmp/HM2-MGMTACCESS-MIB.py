# SNMP MIB module (HM2-MGMTACCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-MGMTACCESS-MIB
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

(HmEnabledStatus,
 HmLargeDisplayString,
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "HmLargeDisplayString",
    "hm2ConfigurationMibs")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
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

hm2MgmtAccessMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 25)
)
hm2MgmtAccessMib.setRevisions(
        ("2011-03-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hm2RestartAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("restart", 2))
    )



class Hm2TlsVersions(Bits, TextualConvention):
    status = "current"


class Hm2TlsCipherSuites(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Hm2MgmtAccessMibNotifications_ObjectIdentity = ObjectIdentity
hm2MgmtAccessMibNotifications = _Hm2MgmtAccessMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 0)
)
_Hm2MgmtAccessMibObjects_ObjectIdentity = ObjectIdentity
hm2MgmtAccessMibObjects = _Hm2MgmtAccessMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1)
)
_Hm2MgmtAccessSnmpGroup_ObjectIdentity = ObjectIdentity
hm2MgmtAccessSnmpGroup = _Hm2MgmtAccessSnmpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 1)
)


class _Hm2SnmpV1AdminStatus_Type(HmEnabledStatus):
    """Custom type hm2SnmpV1AdminStatus based on HmEnabledStatus"""


_Hm2SnmpV1AdminStatus_Object = MibScalar
hm2SnmpV1AdminStatus = _Hm2SnmpV1AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 1, 1),
    _Hm2SnmpV1AdminStatus_Type()
)
hm2SnmpV1AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SnmpV1AdminStatus.setStatus("current")


class _Hm2SnmpV2AdminStatus_Type(HmEnabledStatus):
    """Custom type hm2SnmpV2AdminStatus based on HmEnabledStatus"""


_Hm2SnmpV2AdminStatus_Object = MibScalar
hm2SnmpV2AdminStatus = _Hm2SnmpV2AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 1, 2),
    _Hm2SnmpV2AdminStatus_Type()
)
hm2SnmpV2AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SnmpV2AdminStatus.setStatus("current")


class _Hm2SnmpV3AdminStatus_Type(HmEnabledStatus):
    """Custom type hm2SnmpV3AdminStatus based on HmEnabledStatus"""


_Hm2SnmpV3AdminStatus_Object = MibScalar
hm2SnmpV3AdminStatus = _Hm2SnmpV3AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 1, 3),
    _Hm2SnmpV3AdminStatus_Type()
)
hm2SnmpV3AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SnmpV3AdminStatus.setStatus("current")


class _Hm2SnmpPortNumber_Type(InetPortNumber):
    """Custom type hm2SnmpPortNumber based on InetPortNumber"""
    defaultValue = 161


_Hm2SnmpPortNumber_Object = MibScalar
hm2SnmpPortNumber = _Hm2SnmpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 1, 4),
    _Hm2SnmpPortNumber_Type()
)
hm2SnmpPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SnmpPortNumber.setStatus("current")


class _Hm2SnmpOver802AdminStatus_Type(HmEnabledStatus):
    """Custom type hm2SnmpOver802AdminStatus based on HmEnabledStatus"""


_Hm2SnmpOver802AdminStatus_Object = MibScalar
hm2SnmpOver802AdminStatus = _Hm2SnmpOver802AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 1, 5),
    _Hm2SnmpOver802AdminStatus_Type()
)
hm2SnmpOver802AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SnmpOver802AdminStatus.setStatus("current")


class _Hm2SnmpTrapServiceAdminStatus_Type(HmEnabledStatus):
    """Custom type hm2SnmpTrapServiceAdminStatus based on HmEnabledStatus"""


_Hm2SnmpTrapServiceAdminStatus_Object = MibScalar
hm2SnmpTrapServiceAdminStatus = _Hm2SnmpTrapServiceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 1, 6),
    _Hm2SnmpTrapServiceAdminStatus_Type()
)
hm2SnmpTrapServiceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SnmpTrapServiceAdminStatus.setStatus("current")
_Hm2MgmtAccessWebGroup_ObjectIdentity = ObjectIdentity
hm2MgmtAccessWebGroup = _Hm2MgmtAccessWebGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 2)
)


class _Hm2WebHttpAdminStatus_Type(HmEnabledStatus):
    """Custom type hm2WebHttpAdminStatus based on HmEnabledStatus"""


_Hm2WebHttpAdminStatus_Object = MibScalar
hm2WebHttpAdminStatus = _Hm2WebHttpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 2, 1),
    _Hm2WebHttpAdminStatus_Type()
)
hm2WebHttpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WebHttpAdminStatus.setStatus("current")


class _Hm2WebHttpsAdminStatus_Type(HmEnabledStatus):
    """Custom type hm2WebHttpsAdminStatus based on HmEnabledStatus"""


_Hm2WebHttpsAdminStatus_Object = MibScalar
hm2WebHttpsAdminStatus = _Hm2WebHttpsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 2, 2),
    _Hm2WebHttpsAdminStatus_Type()
)
hm2WebHttpsAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WebHttpsAdminStatus.setStatus("current")


class _Hm2WebHttpPortNumber_Type(InetPortNumber):
    """Custom type hm2WebHttpPortNumber based on InetPortNumber"""
    defaultValue = 80


_Hm2WebHttpPortNumber_Object = MibScalar
hm2WebHttpPortNumber = _Hm2WebHttpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 2, 3),
    _Hm2WebHttpPortNumber_Type()
)
hm2WebHttpPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WebHttpPortNumber.setStatus("current")


class _Hm2WebHttpsPortNumber_Type(InetPortNumber):
    """Custom type hm2WebHttpsPortNumber based on InetPortNumber"""
    defaultValue = 443


_Hm2WebHttpsPortNumber_Object = MibScalar
hm2WebHttpsPortNumber = _Hm2WebHttpsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 2, 4),
    _Hm2WebHttpsPortNumber_Type()
)
hm2WebHttpsPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WebHttpsPortNumber.setStatus("current")


class _Hm2WebHttpsCertPresent_Type(Integer32):
    """Custom type hm2WebHttpsCertPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("pem", 1))
    )


_Hm2WebHttpsCertPresent_Type.__name__ = "Integer32"
_Hm2WebHttpsCertPresent_Object = MibScalar
hm2WebHttpsCertPresent = _Hm2WebHttpsCertPresent_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 2, 5),
    _Hm2WebHttpsCertPresent_Type()
)
hm2WebHttpsCertPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WebHttpsCertPresent.setStatus("current")


class _Hm2WebHttpsCertControl_Type(Integer32):
    """Custom type hm2WebHttpsCertControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("generate", 2),
          ("noop", 1))
    )


_Hm2WebHttpsCertControl_Type.__name__ = "Integer32"
_Hm2WebHttpsCertControl_Object = MibScalar
hm2WebHttpsCertControl = _Hm2WebHttpsCertControl_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 2, 6),
    _Hm2WebHttpsCertControl_Type()
)
hm2WebHttpsCertControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WebHttpsCertControl.setStatus("current")


class _Hm2WebHttpsCertOperStatus_Type(Integer32):
    """Custom type hm2WebHttpsCertOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("generate", 1),
          ("none", 3))
    )


_Hm2WebHttpsCertOperStatus_Type.__name__ = "Integer32"
_Hm2WebHttpsCertOperStatus_Object = MibScalar
hm2WebHttpsCertOperStatus = _Hm2WebHttpsCertOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 2, 7),
    _Hm2WebHttpsCertOperStatus_Type()
)
hm2WebHttpsCertOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WebHttpsCertOperStatus.setStatus("current")


class _Hm2WebIntfTimeOut_Type(Integer32):
    """Custom type hm2WebIntfTimeOut based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160),
    )


_Hm2WebIntfTimeOut_Type.__name__ = "Integer32"
_Hm2WebIntfTimeOut_Object = MibScalar
hm2WebIntfTimeOut = _Hm2WebIntfTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 2, 8),
    _Hm2WebIntfTimeOut_Type()
)
hm2WebIntfTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WebIntfTimeOut.setStatus("current")


class _Hm2WebTrapEnable_Type(HmEnabledStatus):
    """Custom type hm2WebTrapEnable based on HmEnabledStatus"""


_Hm2WebTrapEnable_Object = MibScalar
hm2WebTrapEnable = _Hm2WebTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 2, 9),
    _Hm2WebTrapEnable_Type()
)
hm2WebTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WebTrapEnable.setStatus("current")


class _Hm2WebLastLogoutUserName_Type(SnmpAdminString):
    """Custom type hm2WebLastLogoutUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2WebLastLogoutUserName_Type.__name__ = "SnmpAdminString"
_Hm2WebLastLogoutUserName_Object = MibScalar
hm2WebLastLogoutUserName = _Hm2WebLastLogoutUserName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 2, 10),
    _Hm2WebLastLogoutUserName_Type()
)
hm2WebLastLogoutUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WebLastLogoutUserName.setStatus("current")


class _Hm2WebLastLoginUserName_Type(SnmpAdminString):
    """Custom type hm2WebLastLoginUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2WebLastLoginUserName_Type.__name__ = "SnmpAdminString"
_Hm2WebLastLoginUserName_Object = MibScalar
hm2WebLastLoginUserName = _Hm2WebLastLoginUserName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 2, 11),
    _Hm2WebLastLoginUserName_Type()
)
hm2WebLastLoginUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WebLastLoginUserName.setStatus("current")
_Hm2WebLastLoginInetAddressType_Type = InetAddressType
_Hm2WebLastLoginInetAddressType_Object = MibScalar
hm2WebLastLoginInetAddressType = _Hm2WebLastLoginInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 2, 12),
    _Hm2WebLastLoginInetAddressType_Type()
)
hm2WebLastLoginInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WebLastLoginInetAddressType.setStatus("current")
_Hm2WebLastLoginInetAddress_Type = InetAddress
_Hm2WebLastLoginInetAddress_Object = MibScalar
hm2WebLastLoginInetAddress = _Hm2WebLastLoginInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 2, 13),
    _Hm2WebLastLoginInetAddress_Type()
)
hm2WebLastLoginInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WebLastLoginInetAddress.setStatus("current")


class _Hm2WebHttpsCertFingerPrintType_Type(Integer32):
    """Custom type hm2WebHttpsCertFingerPrintType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sha1", 1),
          ("sha256", 2))
    )


_Hm2WebHttpsCertFingerPrintType_Type.__name__ = "Integer32"
_Hm2WebHttpsCertFingerPrintType_Object = MibScalar
hm2WebHttpsCertFingerPrintType = _Hm2WebHttpsCertFingerPrintType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 2, 14),
    _Hm2WebHttpsCertFingerPrintType_Type()
)
hm2WebHttpsCertFingerPrintType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WebHttpsCertFingerPrintType.setStatus("current")
_Hm2WebHttpsCertFingerPrint_Type = DisplayString
_Hm2WebHttpsCertFingerPrint_Object = MibScalar
hm2WebHttpsCertFingerPrint = _Hm2WebHttpsCertFingerPrint_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 2, 15),
    _Hm2WebHttpsCertFingerPrint_Type()
)
hm2WebHttpsCertFingerPrint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2WebHttpsCertFingerPrint.setStatus("current")
_Hm2WebHttpsServerRestart_Type = Hm2RestartAction
_Hm2WebHttpsServerRestart_Object = MibScalar
hm2WebHttpsServerRestart = _Hm2WebHttpsServerRestart_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 2, 16),
    _Hm2WebHttpsServerRestart_Type()
)
hm2WebHttpsServerRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WebHttpsServerRestart.setStatus("current")


class _Hm2WebHttpsServerTlsVersions_Type(Hm2TlsVersions):
    """Custom type hm2WebHttpsServerTlsVersions based on Hm2TlsVersions"""
    defaultBinValue = "101"


_Hm2WebHttpsServerTlsVersions_Object = MibScalar
hm2WebHttpsServerTlsVersions = _Hm2WebHttpsServerTlsVersions_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 2, 17),
    _Hm2WebHttpsServerTlsVersions_Type()
)
hm2WebHttpsServerTlsVersions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WebHttpsServerTlsVersions.setStatus("current")


class _Hm2WebHttpsServerTlsCipherSuites_Type(Hm2TlsCipherSuites):
    """Custom type hm2WebHttpsServerTlsCipherSuites based on Hm2TlsCipherSuites"""
    defaultBinValue = "1010101"


_Hm2WebHttpsServerTlsCipherSuites_Object = MibScalar
hm2WebHttpsServerTlsCipherSuites = _Hm2WebHttpsServerTlsCipherSuites_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 2, 18),
    _Hm2WebHttpsServerTlsCipherSuites_Type()
)
hm2WebHttpsServerTlsCipherSuites.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2WebHttpsServerTlsCipherSuites.setStatus("current")
_Hm2MgmtAccessTelnetGroup_ObjectIdentity = ObjectIdentity
hm2MgmtAccessTelnetGroup = _Hm2MgmtAccessTelnetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 3)
)


class _Hm2TelnetServerAdminStatus_Type(HmEnabledStatus):
    """Custom type hm2TelnetServerAdminStatus based on HmEnabledStatus"""


_Hm2TelnetServerAdminStatus_Object = MibScalar
hm2TelnetServerAdminStatus = _Hm2TelnetServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 3, 1),
    _Hm2TelnetServerAdminStatus_Type()
)
hm2TelnetServerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TelnetServerAdminStatus.setStatus("current")


class _Hm2TelnetServerPort_Type(InetPortNumber):
    """Custom type hm2TelnetServerPort based on InetPortNumber"""
    defaultValue = 23


_Hm2TelnetServerPort_Object = MibScalar
hm2TelnetServerPort = _Hm2TelnetServerPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 3, 2),
    _Hm2TelnetServerPort_Type()
)
hm2TelnetServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TelnetServerPort.setStatus("current")
_Hm2TelnetServerSessionsCount_Type = Integer32
_Hm2TelnetServerSessionsCount_Object = MibScalar
hm2TelnetServerSessionsCount = _Hm2TelnetServerSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 3, 3),
    _Hm2TelnetServerSessionsCount_Type()
)
hm2TelnetServerSessionsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2TelnetServerSessionsCount.setStatus("current")


class _Hm2TelnetServerMaxSessions_Type(Integer32):
    """Custom type hm2TelnetServerMaxSessions based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Hm2TelnetServerMaxSessions_Type.__name__ = "Integer32"
_Hm2TelnetServerMaxSessions_Object = MibScalar
hm2TelnetServerMaxSessions = _Hm2TelnetServerMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 3, 4),
    _Hm2TelnetServerMaxSessions_Type()
)
hm2TelnetServerMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TelnetServerMaxSessions.setStatus("current")


class _Hm2TelnetServerSessionsTimeOut_Type(Integer32):
    """Custom type hm2TelnetServerSessionsTimeOut based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160),
    )


_Hm2TelnetServerSessionsTimeOut_Type.__name__ = "Integer32"
_Hm2TelnetServerSessionsTimeOut_Object = MibScalar
hm2TelnetServerSessionsTimeOut = _Hm2TelnetServerSessionsTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 3, 5),
    _Hm2TelnetServerSessionsTimeOut_Type()
)
hm2TelnetServerSessionsTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TelnetServerSessionsTimeOut.setStatus("current")


class _Hm2TelnetTrapEnable_Type(HmEnabledStatus):
    """Custom type hm2TelnetTrapEnable based on HmEnabledStatus"""


_Hm2TelnetTrapEnable_Object = MibScalar
hm2TelnetTrapEnable = _Hm2TelnetTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 3, 6),
    _Hm2TelnetTrapEnable_Type()
)
hm2TelnetTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TelnetTrapEnable.setStatus("current")


class _Hm2TelnetLastLogoutUserName_Type(SnmpAdminString):
    """Custom type hm2TelnetLastLogoutUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2TelnetLastLogoutUserName_Type.__name__ = "SnmpAdminString"
_Hm2TelnetLastLogoutUserName_Object = MibScalar
hm2TelnetLastLogoutUserName = _Hm2TelnetLastLogoutUserName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 3, 7),
    _Hm2TelnetLastLogoutUserName_Type()
)
hm2TelnetLastLogoutUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2TelnetLastLogoutUserName.setStatus("current")


class _Hm2TelnetLastLoginUserName_Type(SnmpAdminString):
    """Custom type hm2TelnetLastLoginUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2TelnetLastLoginUserName_Type.__name__ = "SnmpAdminString"
_Hm2TelnetLastLoginUserName_Object = MibScalar
hm2TelnetLastLoginUserName = _Hm2TelnetLastLoginUserName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 3, 8),
    _Hm2TelnetLastLoginUserName_Type()
)
hm2TelnetLastLoginUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2TelnetLastLoginUserName.setStatus("current")
_Hm2TelnetLastLoginInetAddressType_Type = InetAddressType
_Hm2TelnetLastLoginInetAddressType_Object = MibScalar
hm2TelnetLastLoginInetAddressType = _Hm2TelnetLastLoginInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 3, 9),
    _Hm2TelnetLastLoginInetAddressType_Type()
)
hm2TelnetLastLoginInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2TelnetLastLoginInetAddressType.setStatus("current")
_Hm2TelnetLastLoginInetAddress_Type = InetAddress
_Hm2TelnetLastLoginInetAddress_Object = MibScalar
hm2TelnetLastLoginInetAddress = _Hm2TelnetLastLoginInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 3, 10),
    _Hm2TelnetLastLoginInetAddress_Type()
)
hm2TelnetLastLoginInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2TelnetLastLoginInetAddress.setStatus("current")
_Hm2MgmtAccessSshGroup_ObjectIdentity = ObjectIdentity
hm2MgmtAccessSshGroup = _Hm2MgmtAccessSshGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 4)
)


class _Hm2SshAdminStatus_Type(HmEnabledStatus):
    """Custom type hm2SshAdminStatus based on HmEnabledStatus"""


_Hm2SshAdminStatus_Object = MibScalar
hm2SshAdminStatus = _Hm2SshAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 4, 1),
    _Hm2SshAdminStatus_Type()
)
hm2SshAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SshAdminStatus.setStatus("current")


class _Hm2SshProtocolLevel_Type(Integer32):
    """Custom type hm2SshProtocolLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("ssh20", 2)
    )


_Hm2SshProtocolLevel_Type.__name__ = "Integer32"
_Hm2SshProtocolLevel_Object = MibScalar
hm2SshProtocolLevel = _Hm2SshProtocolLevel_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 4, 2),
    _Hm2SshProtocolLevel_Type()
)
hm2SshProtocolLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SshProtocolLevel.setStatus("current")


class _Hm2SshPortNumber_Type(InetPortNumber):
    """Custom type hm2SshPortNumber based on InetPortNumber"""
    defaultValue = 22


_Hm2SshPortNumber_Object = MibScalar
hm2SshPortNumber = _Hm2SshPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 4, 3),
    _Hm2SshPortNumber_Type()
)
hm2SshPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SshPortNumber.setStatus("current")
_Hm2SshSessionsCount_Type = Integer32
_Hm2SshSessionsCount_Object = MibScalar
hm2SshSessionsCount = _Hm2SshSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 4, 4),
    _Hm2SshSessionsCount_Type()
)
hm2SshSessionsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SshSessionsCount.setStatus("current")


class _Hm2SshMaxSessionsCount_Type(Integer32):
    """Custom type hm2SshMaxSessionsCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Hm2SshMaxSessionsCount_Type.__name__ = "Integer32"
_Hm2SshMaxSessionsCount_Object = MibScalar
hm2SshMaxSessionsCount = _Hm2SshMaxSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 4, 5),
    _Hm2SshMaxSessionsCount_Type()
)
hm2SshMaxSessionsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SshMaxSessionsCount.setStatus("current")


class _Hm2SshSessionTimeout_Type(Integer32):
    """Custom type hm2SshSessionTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160),
    )


_Hm2SshSessionTimeout_Type.__name__ = "Integer32"
_Hm2SshSessionTimeout_Object = MibScalar
hm2SshSessionTimeout = _Hm2SshSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 4, 6),
    _Hm2SshSessionTimeout_Type()
)
hm2SshSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SshSessionTimeout.setStatus("current")


class _Hm2SshKeysPresent_Type(Integer32):
    """Custom type hm2SshKeysPresent based on Integer32"""
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
        *(("both", 3),
          ("dsa", 1),
          ("none", 4),
          ("rsa", 2))
    )


_Hm2SshKeysPresent_Type.__name__ = "Integer32"
_Hm2SshKeysPresent_Object = MibScalar
hm2SshKeysPresent = _Hm2SshKeysPresent_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 4, 7),
    _Hm2SshKeysPresent_Type()
)
hm2SshKeysPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SshKeysPresent.setStatus("current")


class _Hm2SshKeyOperStatus_Type(Integer32):
    """Custom type hm2SshKeyOperStatus based on Integer32"""
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
        *(("both", 3),
          ("dsa", 1),
          ("none", 4),
          ("rsa", 2))
    )


_Hm2SshKeyOperStatus_Type.__name__ = "Integer32"
_Hm2SshKeyOperStatus_Object = MibScalar
hm2SshKeyOperStatus = _Hm2SshKeyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 4, 8),
    _Hm2SshKeyOperStatus_Type()
)
hm2SshKeyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SshKeyOperStatus.setStatus("current")


class _Hm2SshRSAKeyControl_Type(Integer32):
    """Custom type hm2SshRSAKeyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("generate", 2),
          ("noop", 1))
    )


_Hm2SshRSAKeyControl_Type.__name__ = "Integer32"
_Hm2SshRSAKeyControl_Object = MibScalar
hm2SshRSAKeyControl = _Hm2SshRSAKeyControl_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 4, 9),
    _Hm2SshRSAKeyControl_Type()
)
hm2SshRSAKeyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SshRSAKeyControl.setStatus("current")


class _Hm2SshDSAKeyControl_Type(Integer32):
    """Custom type hm2SshDSAKeyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("generate", 2),
          ("noop", 1))
    )


_Hm2SshDSAKeyControl_Type.__name__ = "Integer32"
_Hm2SshDSAKeyControl_Object = MibScalar
hm2SshDSAKeyControl = _Hm2SshDSAKeyControl_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 4, 10),
    _Hm2SshDSAKeyControl_Type()
)
hm2SshDSAKeyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SshDSAKeyControl.setStatus("current")


class _Hm2SshFingerPrintDSA_Type(DisplayString):
    """Custom type hm2SshFingerPrintDSA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2SshFingerPrintDSA_Type.__name__ = "DisplayString"
_Hm2SshFingerPrintDSA_Object = MibScalar
hm2SshFingerPrintDSA = _Hm2SshFingerPrintDSA_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 4, 11),
    _Hm2SshFingerPrintDSA_Type()
)
hm2SshFingerPrintDSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SshFingerPrintDSA.setStatus("current")


class _Hm2SshFingerPrintRSA_Type(DisplayString):
    """Custom type hm2SshFingerPrintRSA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2SshFingerPrintRSA_Type.__name__ = "DisplayString"
_Hm2SshFingerPrintRSA_Object = MibScalar
hm2SshFingerPrintRSA = _Hm2SshFingerPrintRSA_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 4, 12),
    _Hm2SshFingerPrintRSA_Type()
)
hm2SshFingerPrintRSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SshFingerPrintRSA.setStatus("current")


class _Hm2SshTrapEnable_Type(HmEnabledStatus):
    """Custom type hm2SshTrapEnable based on HmEnabledStatus"""


_Hm2SshTrapEnable_Object = MibScalar
hm2SshTrapEnable = _Hm2SshTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 4, 13),
    _Hm2SshTrapEnable_Type()
)
hm2SshTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SshTrapEnable.setStatus("current")


class _Hm2SshLastLogoutUserName_Type(SnmpAdminString):
    """Custom type hm2SshLastLogoutUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2SshLastLogoutUserName_Type.__name__ = "SnmpAdminString"
_Hm2SshLastLogoutUserName_Object = MibScalar
hm2SshLastLogoutUserName = _Hm2SshLastLogoutUserName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 4, 14),
    _Hm2SshLastLogoutUserName_Type()
)
hm2SshLastLogoutUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SshLastLogoutUserName.setStatus("current")


class _Hm2SshLastLoginUserName_Type(SnmpAdminString):
    """Custom type hm2SshLastLoginUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2SshLastLoginUserName_Type.__name__ = "SnmpAdminString"
_Hm2SshLastLoginUserName_Object = MibScalar
hm2SshLastLoginUserName = _Hm2SshLastLoginUserName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 4, 15),
    _Hm2SshLastLoginUserName_Type()
)
hm2SshLastLoginUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SshLastLoginUserName.setStatus("current")
_Hm2SshLastLoginInetAddressType_Type = InetAddressType
_Hm2SshLastLoginInetAddressType_Object = MibScalar
hm2SshLastLoginInetAddressType = _Hm2SshLastLoginInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 4, 16),
    _Hm2SshLastLoginInetAddressType_Type()
)
hm2SshLastLoginInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SshLastLoginInetAddressType.setStatus("current")
_Hm2SshLastLoginInetAddress_Type = InetAddress
_Hm2SshLastLoginInetAddress_Object = MibScalar
hm2SshLastLoginInetAddress = _Hm2SshLastLoginInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 4, 17),
    _Hm2SshLastLoginInetAddress_Type()
)
hm2SshLastLoginInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SshLastLoginInetAddress.setStatus("current")
_Hm2SshOutboundSessionsCount_Type = Integer32
_Hm2SshOutboundSessionsCount_Object = MibScalar
hm2SshOutboundSessionsCount = _Hm2SshOutboundSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 4, 50),
    _Hm2SshOutboundSessionsCount_Type()
)
hm2SshOutboundSessionsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SshOutboundSessionsCount.setStatus("current")


class _Hm2SshOutboundMaxSessionsCount_Type(Integer32):
    """Custom type hm2SshOutboundMaxSessionsCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Hm2SshOutboundMaxSessionsCount_Type.__name__ = "Integer32"
_Hm2SshOutboundMaxSessionsCount_Object = MibScalar
hm2SshOutboundMaxSessionsCount = _Hm2SshOutboundMaxSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 4, 51),
    _Hm2SshOutboundMaxSessionsCount_Type()
)
hm2SshOutboundMaxSessionsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SshOutboundMaxSessionsCount.setStatus("current")


class _Hm2SshOutboundSessionTimeout_Type(Integer32):
    """Custom type hm2SshOutboundSessionTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160),
    )


_Hm2SshOutboundSessionTimeout_Type.__name__ = "Integer32"
_Hm2SshOutboundSessionTimeout_Object = MibScalar
hm2SshOutboundSessionTimeout = _Hm2SshOutboundSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 4, 52),
    _Hm2SshOutboundSessionTimeout_Type()
)
hm2SshOutboundSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SshOutboundSessionTimeout.setStatus("current")
_Hm2MgmtAccessPreLoginBannerGroup_ObjectIdentity = ObjectIdentity
hm2MgmtAccessPreLoginBannerGroup = _Hm2MgmtAccessPreLoginBannerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 5)
)


class _Hm2PreLoginBannerAdminStatus_Type(HmEnabledStatus):
    """Custom type hm2PreLoginBannerAdminStatus based on HmEnabledStatus"""


_Hm2PreLoginBannerAdminStatus_Object = MibScalar
hm2PreLoginBannerAdminStatus = _Hm2PreLoginBannerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 5, 1),
    _Hm2PreLoginBannerAdminStatus_Type()
)
hm2PreLoginBannerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PreLoginBannerAdminStatus.setStatus("current")


class _Hm2PreLoginBannerText_Type(HmLargeDisplayString):
    """Custom type hm2PreLoginBannerText based on HmLargeDisplayString"""
    subtypeSpec = HmLargeDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_Hm2PreLoginBannerText_Type.__name__ = "HmLargeDisplayString"
_Hm2PreLoginBannerText_Object = MibScalar
hm2PreLoginBannerText = _Hm2PreLoginBannerText_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 5, 2),
    _Hm2PreLoginBannerText_Type()
)
hm2PreLoginBannerText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PreLoginBannerText.setStatus("current")
_Hm2MgmtAccessCliGroup_ObjectIdentity = ObjectIdentity
hm2MgmtAccessCliGroup = _Hm2MgmtAccessCliGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 6)
)


class _Hm2CliLoginPrompt_Type(DisplayString):
    """Custom type hm2CliLoginPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2CliLoginPrompt_Type.__name__ = "DisplayString"
_Hm2CliLoginPrompt_Object = MibScalar
hm2CliLoginPrompt = _Hm2CliLoginPrompt_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 6, 1),
    _Hm2CliLoginPrompt_Type()
)
hm2CliLoginPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2CliLoginPrompt.setStatus("current")


class _Hm2CliLoginTimeoutSerial_Type(Integer32):
    """Custom type hm2CliLoginTimeoutSerial based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160),
    )


_Hm2CliLoginTimeoutSerial_Type.__name__ = "Integer32"
_Hm2CliLoginTimeoutSerial_Object = MibScalar
hm2CliLoginTimeoutSerial = _Hm2CliLoginTimeoutSerial_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 6, 3),
    _Hm2CliLoginTimeoutSerial_Type()
)
hm2CliLoginTimeoutSerial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2CliLoginTimeoutSerial.setStatus("current")


class _Hm2CliLoginBannerAdminStatus_Type(HmEnabledStatus):
    """Custom type hm2CliLoginBannerAdminStatus based on HmEnabledStatus"""


_Hm2CliLoginBannerAdminStatus_Object = MibScalar
hm2CliLoginBannerAdminStatus = _Hm2CliLoginBannerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 6, 10),
    _Hm2CliLoginBannerAdminStatus_Type()
)
hm2CliLoginBannerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2CliLoginBannerAdminStatus.setStatus("current")


class _Hm2CliLoginBannerText_Type(HmLargeDisplayString):
    """Custom type hm2CliLoginBannerText based on HmLargeDisplayString"""
    subtypeSpec = HmLargeDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_Hm2CliLoginBannerText_Type.__name__ = "HmLargeDisplayString"
_Hm2CliLoginBannerText_Object = MibScalar
hm2CliLoginBannerText = _Hm2CliLoginBannerText_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 6, 11),
    _Hm2CliLoginBannerText_Type()
)
hm2CliLoginBannerText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2CliLoginBannerText.setStatus("current")


class _Hm2ConsoleTrapEnable_Type(HmEnabledStatus):
    """Custom type hm2ConsoleTrapEnable based on HmEnabledStatus"""


_Hm2ConsoleTrapEnable_Object = MibScalar
hm2ConsoleTrapEnable = _Hm2ConsoleTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 6, 12),
    _Hm2ConsoleTrapEnable_Type()
)
hm2ConsoleTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2ConsoleTrapEnable.setStatus("current")


class _Hm2ConsoleLastLogoutUserName_Type(SnmpAdminString):
    """Custom type hm2ConsoleLastLogoutUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2ConsoleLastLogoutUserName_Type.__name__ = "SnmpAdminString"
_Hm2ConsoleLastLogoutUserName_Object = MibScalar
hm2ConsoleLastLogoutUserName = _Hm2ConsoleLastLogoutUserName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 6, 13),
    _Hm2ConsoleLastLogoutUserName_Type()
)
hm2ConsoleLastLogoutUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2ConsoleLastLogoutUserName.setStatus("current")


class _Hm2ConsoleLastLoginUserName_Type(SnmpAdminString):
    """Custom type hm2ConsoleLastLoginUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2ConsoleLastLoginUserName_Type.__name__ = "SnmpAdminString"
_Hm2ConsoleLastLoginUserName_Object = MibScalar
hm2ConsoleLastLoginUserName = _Hm2ConsoleLastLoginUserName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 6, 14),
    _Hm2ConsoleLastLoginUserName_Type()
)
hm2ConsoleLastLoginUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2ConsoleLastLoginUserName.setStatus("current")


class _Hm2ConsoleServiceShellAdminState_Type(HmEnabledStatus):
    """Custom type hm2ConsoleServiceShellAdminState based on HmEnabledStatus"""


_Hm2ConsoleServiceShellAdminState_Object = MibScalar
hm2ConsoleServiceShellAdminState = _Hm2ConsoleServiceShellAdminState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 6, 15),
    _Hm2ConsoleServiceShellAdminState_Type()
)
hm2ConsoleServiceShellAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2ConsoleServiceShellAdminState.setStatus("current")
_Hm2RestrictedMgmtAccessGroup_ObjectIdentity = ObjectIdentity
hm2RestrictedMgmtAccessGroup = _Hm2RestrictedMgmtAccessGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 7)
)
_Hm2RmaTable_Object = MibTable
hm2RmaTable = _Hm2RmaTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hm2RmaTable.setStatus("current")
_Hm2RmaEntry_Object = MibTableRow
hm2RmaEntry = _Hm2RmaEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 7, 1, 1)
)
hm2RmaEntry.setIndexNames(
    (0, "HM2-MGMTACCESS-MIB", "hm2RmaIndex"),
)
if mibBuilder.loadTexts:
    hm2RmaEntry.setStatus("current")


class _Hm2RmaIndex_Type(Integer32):
    """Custom type hm2RmaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Hm2RmaIndex_Type.__name__ = "Integer32"
_Hm2RmaIndex_Object = MibTableColumn
hm2RmaIndex = _Hm2RmaIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 7, 1, 1, 1),
    _Hm2RmaIndex_Type()
)
hm2RmaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2RmaIndex.setStatus("current")
_Hm2RmaRowStatus_Type = RowStatus
_Hm2RmaRowStatus_Object = MibTableColumn
hm2RmaRowStatus = _Hm2RmaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 7, 1, 1, 2),
    _Hm2RmaRowStatus_Type()
)
hm2RmaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2RmaRowStatus.setStatus("current")


class _Hm2RmaIpAddrType_Type(InetAddressType):
    """Custom type hm2RmaIpAddrType based on InetAddressType"""


_Hm2RmaIpAddrType_Object = MibTableColumn
hm2RmaIpAddrType = _Hm2RmaIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 7, 1, 1, 3),
    _Hm2RmaIpAddrType_Type()
)
hm2RmaIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2RmaIpAddrType.setStatus("current")


class _Hm2RmaIpAddr_Type(InetAddress):
    """Custom type hm2RmaIpAddr based on InetAddress"""
    defaultHexValue = "00000000"


_Hm2RmaIpAddr_Object = MibTableColumn
hm2RmaIpAddr = _Hm2RmaIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 7, 1, 1, 4),
    _Hm2RmaIpAddr_Type()
)
hm2RmaIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2RmaIpAddr.setStatus("current")


class _Hm2RmaPrefixLength_Type(InetAddressPrefixLength):
    """Custom type hm2RmaPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 0


_Hm2RmaPrefixLength_Object = MibTableColumn
hm2RmaPrefixLength = _Hm2RmaPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 7, 1, 1, 5),
    _Hm2RmaPrefixLength_Type()
)
hm2RmaPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2RmaPrefixLength.setStatus("current")


class _Hm2RmaSrvHttp_Type(HmEnabledStatus):
    """Custom type hm2RmaSrvHttp based on HmEnabledStatus"""


_Hm2RmaSrvHttp_Object = MibTableColumn
hm2RmaSrvHttp = _Hm2RmaSrvHttp_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 7, 1, 1, 6),
    _Hm2RmaSrvHttp_Type()
)
hm2RmaSrvHttp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2RmaSrvHttp.setStatus("current")


class _Hm2RmaSrvHttps_Type(HmEnabledStatus):
    """Custom type hm2RmaSrvHttps based on HmEnabledStatus"""


_Hm2RmaSrvHttps_Object = MibTableColumn
hm2RmaSrvHttps = _Hm2RmaSrvHttps_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 7, 1, 1, 7),
    _Hm2RmaSrvHttps_Type()
)
hm2RmaSrvHttps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2RmaSrvHttps.setStatus("current")


class _Hm2RmaSrvSnmp_Type(HmEnabledStatus):
    """Custom type hm2RmaSrvSnmp based on HmEnabledStatus"""


_Hm2RmaSrvSnmp_Object = MibTableColumn
hm2RmaSrvSnmp = _Hm2RmaSrvSnmp_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 7, 1, 1, 8),
    _Hm2RmaSrvSnmp_Type()
)
hm2RmaSrvSnmp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2RmaSrvSnmp.setStatus("current")


class _Hm2RmaSrvTelnet_Type(HmEnabledStatus):
    """Custom type hm2RmaSrvTelnet based on HmEnabledStatus"""


_Hm2RmaSrvTelnet_Object = MibTableColumn
hm2RmaSrvTelnet = _Hm2RmaSrvTelnet_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 7, 1, 1, 9),
    _Hm2RmaSrvTelnet_Type()
)
hm2RmaSrvTelnet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2RmaSrvTelnet.setStatus("current")


class _Hm2RmaSrvSsh_Type(HmEnabledStatus):
    """Custom type hm2RmaSrvSsh based on HmEnabledStatus"""


_Hm2RmaSrvSsh_Object = MibTableColumn
hm2RmaSrvSsh = _Hm2RmaSrvSsh_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 7, 1, 1, 10),
    _Hm2RmaSrvSsh_Type()
)
hm2RmaSrvSsh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2RmaSrvSsh.setStatus("current")


class _Hm2RmaSrvIEC61850_Type(HmEnabledStatus):
    """Custom type hm2RmaSrvIEC61850 based on HmEnabledStatus"""


_Hm2RmaSrvIEC61850_Object = MibTableColumn
hm2RmaSrvIEC61850 = _Hm2RmaSrvIEC61850_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 7, 1, 1, 11),
    _Hm2RmaSrvIEC61850_Type()
)
hm2RmaSrvIEC61850.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2RmaSrvIEC61850.setStatus("current")


class _Hm2RmaSrvModbusTcp_Type(HmEnabledStatus):
    """Custom type hm2RmaSrvModbusTcp based on HmEnabledStatus"""


_Hm2RmaSrvModbusTcp_Object = MibTableColumn
hm2RmaSrvModbusTcp = _Hm2RmaSrvModbusTcp_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 7, 1, 1, 12),
    _Hm2RmaSrvModbusTcp_Type()
)
hm2RmaSrvModbusTcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2RmaSrvModbusTcp.setStatus("current")


class _Hm2RmaSrvEthernetIP_Type(HmEnabledStatus):
    """Custom type hm2RmaSrvEthernetIP based on HmEnabledStatus"""


_Hm2RmaSrvEthernetIP_Object = MibTableColumn
hm2RmaSrvEthernetIP = _Hm2RmaSrvEthernetIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 7, 1, 1, 13),
    _Hm2RmaSrvEthernetIP_Type()
)
hm2RmaSrvEthernetIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2RmaSrvEthernetIP.setStatus("current")


class _Hm2RmaSrvProfinetIO_Type(HmEnabledStatus):
    """Custom type hm2RmaSrvProfinetIO based on HmEnabledStatus"""


_Hm2RmaSrvProfinetIO_Object = MibTableColumn
hm2RmaSrvProfinetIO = _Hm2RmaSrvProfinetIO_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 7, 1, 1, 14),
    _Hm2RmaSrvProfinetIO_Type()
)
hm2RmaSrvProfinetIO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2RmaSrvProfinetIO.setStatus("current")


class _Hm2RmaOperation_Type(HmEnabledStatus):
    """Custom type hm2RmaOperation based on HmEnabledStatus"""


_Hm2RmaOperation_Object = MibScalar
hm2RmaOperation = _Hm2RmaOperation_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 1, 7, 2),
    _Hm2RmaOperation_Type()
)
hm2RmaOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2RmaOperation.setStatus("current")
_Hm2MgmtAccessMibSNMPExtensionGroup_ObjectIdentity = ObjectIdentity
hm2MgmtAccessMibSNMPExtensionGroup = _Hm2MgmtAccessMibSNMPExtensionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 3)
)
_Hm2MgmtAccessSnmpSESGroup_ObjectIdentity = ObjectIdentity
hm2MgmtAccessSnmpSESGroup = _Hm2MgmtAccessSnmpSESGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 3, 1)
)
_Hm2MgmtAccessWebSESGroup_ObjectIdentity = ObjectIdentity
hm2MgmtAccessWebSESGroup = _Hm2MgmtAccessWebSESGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 3, 2)
)
_Hm2MgmtAccessWebSESCertGenInProgress_ObjectIdentity = ObjectIdentity
hm2MgmtAccessWebSESCertGenInProgress = _Hm2MgmtAccessWebSESCertGenInProgress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hm2MgmtAccessWebSESCertGenInProgress.setStatus("current")
_Hm2MgmtAccessWebSESCertNotPresent_ObjectIdentity = ObjectIdentity
hm2MgmtAccessWebSESCertNotPresent = _Hm2MgmtAccessWebSESCertNotPresent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 3, 2, 2)
)
if mibBuilder.loadTexts:
    hm2MgmtAccessWebSESCertNotPresent.setStatus("current")
_Hm2MgmtAccessTelnetSESGroup_ObjectIdentity = ObjectIdentity
hm2MgmtAccessTelnetSESGroup = _Hm2MgmtAccessTelnetSESGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 3, 3)
)
_Hm2MgmtAccessSshSESGroup_ObjectIdentity = ObjectIdentity
hm2MgmtAccessSshSESGroup = _Hm2MgmtAccessSshSESGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 3, 4)
)
_Hm2MgmtAccessSshSESServerEnabled_ObjectIdentity = ObjectIdentity
hm2MgmtAccessSshSESServerEnabled = _Hm2MgmtAccessSshSESServerEnabled_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 3, 4, 1)
)
if mibBuilder.loadTexts:
    hm2MgmtAccessSshSESServerEnabled.setStatus("current")
_Hm2MgmtAccessSshSESKeyGenInProgress_ObjectIdentity = ObjectIdentity
hm2MgmtAccessSshSESKeyGenInProgress = _Hm2MgmtAccessSshSESKeyGenInProgress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 3, 4, 2)
)
if mibBuilder.loadTexts:
    hm2MgmtAccessSshSESKeyGenInProgress.setStatus("current")
_Hm2MgmtAccessSshSESKeyNotAvailable_ObjectIdentity = ObjectIdentity
hm2MgmtAccessSshSESKeyNotAvailable = _Hm2MgmtAccessSshSESKeyNotAvailable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 3, 4, 3)
)
if mibBuilder.loadTexts:
    hm2MgmtAccessSshSESKeyNotAvailable.setStatus("current")
_Hm2MgmtAccessPreLoginBannerSESGroup_ObjectIdentity = ObjectIdentity
hm2MgmtAccessPreLoginBannerSESGroup = _Hm2MgmtAccessPreLoginBannerSESGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 3, 5)
)
_Hm2MgmtAccessCliSESGroup_ObjectIdentity = ObjectIdentity
hm2MgmtAccessCliSESGroup = _Hm2MgmtAccessCliSESGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 3, 6)
)
_Hm2RestrictedMgmtAccessSESGroup_ObjectIdentity = ObjectIdentity
hm2RestrictedMgmtAccessSESGroup = _Hm2RestrictedMgmtAccessSESGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 3, 7)
)

# Managed Objects groups


# Notification objects

hm2WebLoginSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 0, 1)
)
hm2WebLoginSuccessTrap.setObjects(
      *(("HM2-MGMTACCESS-MIB", "hm2WebLastLoginUserName"),
        ("HM2-MGMTACCESS-MIB", "hm2WebLastLoginInetAddressType"),
        ("HM2-MGMTACCESS-MIB", "hm2WebLastLoginInetAddress"))
)
if mibBuilder.loadTexts:
    hm2WebLoginSuccessTrap.setStatus(
        "current"
    )

hm2WebLoginFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 0, 2)
)
hm2WebLoginFailedTrap.setObjects(
      *(("HM2-MGMTACCESS-MIB", "hm2WebLastLoginUserName"),
        ("HM2-MGMTACCESS-MIB", "hm2WebLastLoginInetAddressType"),
        ("HM2-MGMTACCESS-MIB", "hm2WebLastLoginInetAddress"))
)
if mibBuilder.loadTexts:
    hm2WebLoginFailedTrap.setStatus(
        "current"
    )

hm2WebLogoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 0, 3)
)
hm2WebLogoutTrap.setObjects(
    ("HM2-MGMTACCESS-MIB", "hm2WebLastLogoutUserName")
)
if mibBuilder.loadTexts:
    hm2WebLogoutTrap.setStatus(
        "current"
    )

hm2TelnetLoginSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 0, 4)
)
hm2TelnetLoginSuccessTrap.setObjects(
      *(("HM2-MGMTACCESS-MIB", "hm2TelnetLastLoginUserName"),
        ("HM2-MGMTACCESS-MIB", "hm2TelnetLastLoginInetAddressType"),
        ("HM2-MGMTACCESS-MIB", "hm2TelnetLastLoginInetAddress"))
)
if mibBuilder.loadTexts:
    hm2TelnetLoginSuccessTrap.setStatus(
        "current"
    )

hm2TelnetLoginFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 0, 5)
)
hm2TelnetLoginFailedTrap.setObjects(
      *(("HM2-MGMTACCESS-MIB", "hm2TelnetLastLoginUserName"),
        ("HM2-MGMTACCESS-MIB", "hm2TelnetLastLoginInetAddressType"),
        ("HM2-MGMTACCESS-MIB", "hm2TelnetLastLoginInetAddress"))
)
if mibBuilder.loadTexts:
    hm2TelnetLoginFailedTrap.setStatus(
        "current"
    )

hm2TelnetLogoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 0, 6)
)
hm2TelnetLogoutTrap.setObjects(
    ("HM2-MGMTACCESS-MIB", "hm2TelnetLastLogoutUserName")
)
if mibBuilder.loadTexts:
    hm2TelnetLogoutTrap.setStatus(
        "current"
    )

hm2SshLoginSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 0, 7)
)
hm2SshLoginSuccessTrap.setObjects(
      *(("HM2-MGMTACCESS-MIB", "hm2SshLastLoginUserName"),
        ("HM2-MGMTACCESS-MIB", "hm2SshLastLoginInetAddressType"),
        ("HM2-MGMTACCESS-MIB", "hm2SshLastLoginInetAddress"))
)
if mibBuilder.loadTexts:
    hm2SshLoginSuccessTrap.setStatus(
        "current"
    )

hm2SshLoginFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 0, 8)
)
hm2SshLoginFailedTrap.setObjects(
      *(("HM2-MGMTACCESS-MIB", "hm2SshLastLoginUserName"),
        ("HM2-MGMTACCESS-MIB", "hm2SshLastLoginInetAddressType"),
        ("HM2-MGMTACCESS-MIB", "hm2SshLastLoginInetAddress"))
)
if mibBuilder.loadTexts:
    hm2SshLoginFailedTrap.setStatus(
        "current"
    )

hm2SshLogoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 0, 9)
)
hm2SshLogoutTrap.setObjects(
    ("HM2-MGMTACCESS-MIB", "hm2SshLastLogoutUserName")
)
if mibBuilder.loadTexts:
    hm2SshLogoutTrap.setStatus(
        "current"
    )

hm2ConsoleLoginSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 0, 10)
)
hm2ConsoleLoginSuccessTrap.setObjects(
    ("HM2-MGMTACCESS-MIB", "hm2ConsoleLastLoginUserName")
)
if mibBuilder.loadTexts:
    hm2ConsoleLoginSuccessTrap.setStatus(
        "current"
    )

hm2ConsoleLoginFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 0, 11)
)
hm2ConsoleLoginFailedTrap.setObjects(
    ("HM2-MGMTACCESS-MIB", "hm2ConsoleLastLoginUserName")
)
if mibBuilder.loadTexts:
    hm2ConsoleLoginFailedTrap.setStatus(
        "current"
    )

hm2ConsoleLogoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 25, 0, 12)
)
hm2ConsoleLogoutTrap.setObjects(
    ("HM2-MGMTACCESS-MIB", "hm2ConsoleLastLogoutUserName")
)
if mibBuilder.loadTexts:
    hm2ConsoleLogoutTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-MGMTACCESS-MIB",
    **{"Hm2RestartAction": Hm2RestartAction,
       "Hm2TlsVersions": Hm2TlsVersions,
       "Hm2TlsCipherSuites": Hm2TlsCipherSuites,
       "hm2MgmtAccessMib": hm2MgmtAccessMib,
       "hm2MgmtAccessMibNotifications": hm2MgmtAccessMibNotifications,
       "hm2WebLoginSuccessTrap": hm2WebLoginSuccessTrap,
       "hm2WebLoginFailedTrap": hm2WebLoginFailedTrap,
       "hm2WebLogoutTrap": hm2WebLogoutTrap,
       "hm2TelnetLoginSuccessTrap": hm2TelnetLoginSuccessTrap,
       "hm2TelnetLoginFailedTrap": hm2TelnetLoginFailedTrap,
       "hm2TelnetLogoutTrap": hm2TelnetLogoutTrap,
       "hm2SshLoginSuccessTrap": hm2SshLoginSuccessTrap,
       "hm2SshLoginFailedTrap": hm2SshLoginFailedTrap,
       "hm2SshLogoutTrap": hm2SshLogoutTrap,
       "hm2ConsoleLoginSuccessTrap": hm2ConsoleLoginSuccessTrap,
       "hm2ConsoleLoginFailedTrap": hm2ConsoleLoginFailedTrap,
       "hm2ConsoleLogoutTrap": hm2ConsoleLogoutTrap,
       "hm2MgmtAccessMibObjects": hm2MgmtAccessMibObjects,
       "hm2MgmtAccessSnmpGroup": hm2MgmtAccessSnmpGroup,
       "hm2SnmpV1AdminStatus": hm2SnmpV1AdminStatus,
       "hm2SnmpV2AdminStatus": hm2SnmpV2AdminStatus,
       "hm2SnmpV3AdminStatus": hm2SnmpV3AdminStatus,
       "hm2SnmpPortNumber": hm2SnmpPortNumber,
       "hm2SnmpOver802AdminStatus": hm2SnmpOver802AdminStatus,
       "hm2SnmpTrapServiceAdminStatus": hm2SnmpTrapServiceAdminStatus,
       "hm2MgmtAccessWebGroup": hm2MgmtAccessWebGroup,
       "hm2WebHttpAdminStatus": hm2WebHttpAdminStatus,
       "hm2WebHttpsAdminStatus": hm2WebHttpsAdminStatus,
       "hm2WebHttpPortNumber": hm2WebHttpPortNumber,
       "hm2WebHttpsPortNumber": hm2WebHttpsPortNumber,
       "hm2WebHttpsCertPresent": hm2WebHttpsCertPresent,
       "hm2WebHttpsCertControl": hm2WebHttpsCertControl,
       "hm2WebHttpsCertOperStatus": hm2WebHttpsCertOperStatus,
       "hm2WebIntfTimeOut": hm2WebIntfTimeOut,
       "hm2WebTrapEnable": hm2WebTrapEnable,
       "hm2WebLastLogoutUserName": hm2WebLastLogoutUserName,
       "hm2WebLastLoginUserName": hm2WebLastLoginUserName,
       "hm2WebLastLoginInetAddressType": hm2WebLastLoginInetAddressType,
       "hm2WebLastLoginInetAddress": hm2WebLastLoginInetAddress,
       "hm2WebHttpsCertFingerPrintType": hm2WebHttpsCertFingerPrintType,
       "hm2WebHttpsCertFingerPrint": hm2WebHttpsCertFingerPrint,
       "hm2WebHttpsServerRestart": hm2WebHttpsServerRestart,
       "hm2WebHttpsServerTlsVersions": hm2WebHttpsServerTlsVersions,
       "hm2WebHttpsServerTlsCipherSuites": hm2WebHttpsServerTlsCipherSuites,
       "hm2MgmtAccessTelnetGroup": hm2MgmtAccessTelnetGroup,
       "hm2TelnetServerAdminStatus": hm2TelnetServerAdminStatus,
       "hm2TelnetServerPort": hm2TelnetServerPort,
       "hm2TelnetServerSessionsCount": hm2TelnetServerSessionsCount,
       "hm2TelnetServerMaxSessions": hm2TelnetServerMaxSessions,
       "hm2TelnetServerSessionsTimeOut": hm2TelnetServerSessionsTimeOut,
       "hm2TelnetTrapEnable": hm2TelnetTrapEnable,
       "hm2TelnetLastLogoutUserName": hm2TelnetLastLogoutUserName,
       "hm2TelnetLastLoginUserName": hm2TelnetLastLoginUserName,
       "hm2TelnetLastLoginInetAddressType": hm2TelnetLastLoginInetAddressType,
       "hm2TelnetLastLoginInetAddress": hm2TelnetLastLoginInetAddress,
       "hm2MgmtAccessSshGroup": hm2MgmtAccessSshGroup,
       "hm2SshAdminStatus": hm2SshAdminStatus,
       "hm2SshProtocolLevel": hm2SshProtocolLevel,
       "hm2SshPortNumber": hm2SshPortNumber,
       "hm2SshSessionsCount": hm2SshSessionsCount,
       "hm2SshMaxSessionsCount": hm2SshMaxSessionsCount,
       "hm2SshSessionTimeout": hm2SshSessionTimeout,
       "hm2SshKeysPresent": hm2SshKeysPresent,
       "hm2SshKeyOperStatus": hm2SshKeyOperStatus,
       "hm2SshRSAKeyControl": hm2SshRSAKeyControl,
       "hm2SshDSAKeyControl": hm2SshDSAKeyControl,
       "hm2SshFingerPrintDSA": hm2SshFingerPrintDSA,
       "hm2SshFingerPrintRSA": hm2SshFingerPrintRSA,
       "hm2SshTrapEnable": hm2SshTrapEnable,
       "hm2SshLastLogoutUserName": hm2SshLastLogoutUserName,
       "hm2SshLastLoginUserName": hm2SshLastLoginUserName,
       "hm2SshLastLoginInetAddressType": hm2SshLastLoginInetAddressType,
       "hm2SshLastLoginInetAddress": hm2SshLastLoginInetAddress,
       "hm2SshOutboundSessionsCount": hm2SshOutboundSessionsCount,
       "hm2SshOutboundMaxSessionsCount": hm2SshOutboundMaxSessionsCount,
       "hm2SshOutboundSessionTimeout": hm2SshOutboundSessionTimeout,
       "hm2MgmtAccessPreLoginBannerGroup": hm2MgmtAccessPreLoginBannerGroup,
       "hm2PreLoginBannerAdminStatus": hm2PreLoginBannerAdminStatus,
       "hm2PreLoginBannerText": hm2PreLoginBannerText,
       "hm2MgmtAccessCliGroup": hm2MgmtAccessCliGroup,
       "hm2CliLoginPrompt": hm2CliLoginPrompt,
       "hm2CliLoginTimeoutSerial": hm2CliLoginTimeoutSerial,
       "hm2CliLoginBannerAdminStatus": hm2CliLoginBannerAdminStatus,
       "hm2CliLoginBannerText": hm2CliLoginBannerText,
       "hm2ConsoleTrapEnable": hm2ConsoleTrapEnable,
       "hm2ConsoleLastLogoutUserName": hm2ConsoleLastLogoutUserName,
       "hm2ConsoleLastLoginUserName": hm2ConsoleLastLoginUserName,
       "hm2ConsoleServiceShellAdminState": hm2ConsoleServiceShellAdminState,
       "hm2RestrictedMgmtAccessGroup": hm2RestrictedMgmtAccessGroup,
       "hm2RmaTable": hm2RmaTable,
       "hm2RmaEntry": hm2RmaEntry,
       "hm2RmaIndex": hm2RmaIndex,
       "hm2RmaRowStatus": hm2RmaRowStatus,
       "hm2RmaIpAddrType": hm2RmaIpAddrType,
       "hm2RmaIpAddr": hm2RmaIpAddr,
       "hm2RmaPrefixLength": hm2RmaPrefixLength,
       "hm2RmaSrvHttp": hm2RmaSrvHttp,
       "hm2RmaSrvHttps": hm2RmaSrvHttps,
       "hm2RmaSrvSnmp": hm2RmaSrvSnmp,
       "hm2RmaSrvTelnet": hm2RmaSrvTelnet,
       "hm2RmaSrvSsh": hm2RmaSrvSsh,
       "hm2RmaSrvIEC61850": hm2RmaSrvIEC61850,
       "hm2RmaSrvModbusTcp": hm2RmaSrvModbusTcp,
       "hm2RmaSrvEthernetIP": hm2RmaSrvEthernetIP,
       "hm2RmaSrvProfinetIO": hm2RmaSrvProfinetIO,
       "hm2RmaOperation": hm2RmaOperation,
       "hm2MgmtAccessMibSNMPExtensionGroup": hm2MgmtAccessMibSNMPExtensionGroup,
       "hm2MgmtAccessSnmpSESGroup": hm2MgmtAccessSnmpSESGroup,
       "hm2MgmtAccessWebSESGroup": hm2MgmtAccessWebSESGroup,
       "hm2MgmtAccessWebSESCertGenInProgress": hm2MgmtAccessWebSESCertGenInProgress,
       "hm2MgmtAccessWebSESCertNotPresent": hm2MgmtAccessWebSESCertNotPresent,
       "hm2MgmtAccessTelnetSESGroup": hm2MgmtAccessTelnetSESGroup,
       "hm2MgmtAccessSshSESGroup": hm2MgmtAccessSshSESGroup,
       "hm2MgmtAccessSshSESServerEnabled": hm2MgmtAccessSshSESServerEnabled,
       "hm2MgmtAccessSshSESKeyGenInProgress": hm2MgmtAccessSshSESKeyGenInProgress,
       "hm2MgmtAccessSshSESKeyNotAvailable": hm2MgmtAccessSshSESKeyNotAvailable,
       "hm2MgmtAccessPreLoginBannerSESGroup": hm2MgmtAccessPreLoginBannerSESGroup,
       "hm2MgmtAccessCliSESGroup": hm2MgmtAccessCliSESGroup,
       "hm2RestrictedMgmtAccessSESGroup": hm2RestrictedMgmtAccessSESGroup}
)
