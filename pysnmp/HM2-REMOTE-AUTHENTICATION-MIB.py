# SNMP MIB module (HM2-REMOTE-AUTHENTICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-REMOTE-AUTHENTICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:30 2024
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
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "hm2ConfigurationMibs")

(Hm2UserAccessRoles,) = mibBuilder.importSymbols(
    "HM2-USERMGMT-MIB",
    "Hm2UserAccessRoles")

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

hm2RemoteAuthMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 26)
)
hm2RemoteAuthMib.setRevisions(
        ("2014-03-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2RemoteAuthMibNotifications_ObjectIdentity = ObjectIdentity
hm2RemoteAuthMibNotifications = _Hm2RemoteAuthMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 0)
)
_Hm2RemoteAuthMibObjects_ObjectIdentity = ObjectIdentity
hm2RemoteAuthMibObjects = _Hm2RemoteAuthMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1)
)
_Hm2LdapGroup_ObjectIdentity = ObjectIdentity
hm2LdapGroup = _Hm2LdapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1)
)
_Hm2LdapConfigGroup_ObjectIdentity = ObjectIdentity
hm2LdapConfigGroup = _Hm2LdapConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 10)
)


class _Hm2LdapClientAdminState_Type(HmEnabledStatus):
    """Custom type hm2LdapClientAdminState based on HmEnabledStatus"""


_Hm2LdapClientAdminState_Object = MibScalar
hm2LdapClientAdminState = _Hm2LdapClientAdminState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 10, 1),
    _Hm2LdapClientAdminState_Type()
)
hm2LdapClientAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LdapClientAdminState.setStatus("current")


class _Hm2LdapClientCacheTimeout_Type(Integer32):
    """Custom type hm2LdapClientCacheTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_Hm2LdapClientCacheTimeout_Type.__name__ = "Integer32"
_Hm2LdapClientCacheTimeout_Object = MibScalar
hm2LdapClientCacheTimeout = _Hm2LdapClientCacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 10, 2),
    _Hm2LdapClientCacheTimeout_Type()
)
hm2LdapClientCacheTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LdapClientCacheTimeout.setStatus("current")


class _Hm2LdapClientServerBaseDN_Type(SnmpAdminString):
    """Custom type hm2LdapClientServerBaseDN based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hm2LdapClientServerBaseDN_Type.__name__ = "SnmpAdminString"
_Hm2LdapClientServerBaseDN_Object = MibScalar
hm2LdapClientServerBaseDN = _Hm2LdapClientServerBaseDN_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 10, 3),
    _Hm2LdapClientServerBaseDN_Type()
)
hm2LdapClientServerBaseDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LdapClientServerBaseDN.setStatus("current")


class _Hm2LdapClientServerSearchAttribute_Type(SnmpAdminString):
    """Custom type hm2LdapClientServerSearchAttribute based on SnmpAdminString"""
    defaultValue = OctetString("userPrincipalName")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hm2LdapClientServerSearchAttribute_Type.__name__ = "SnmpAdminString"
_Hm2LdapClientServerSearchAttribute_Object = MibScalar
hm2LdapClientServerSearchAttribute = _Hm2LdapClientServerSearchAttribute_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 10, 4),
    _Hm2LdapClientServerSearchAttribute_Type()
)
hm2LdapClientServerSearchAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LdapClientServerSearchAttribute.setStatus("current")


class _Hm2LdapClientServerBindUser_Type(SnmpAdminString):
    """Custom type hm2LdapClientServerBindUser based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hm2LdapClientServerBindUser_Type.__name__ = "SnmpAdminString"
_Hm2LdapClientServerBindUser_Object = MibScalar
hm2LdapClientServerBindUser = _Hm2LdapClientServerBindUser_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 10, 5),
    _Hm2LdapClientServerBindUser_Type()
)
hm2LdapClientServerBindUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LdapClientServerBindUser.setStatus("current")


class _Hm2LdapClientServerBindUserPasswd_Type(SnmpAdminString):
    """Custom type hm2LdapClientServerBindUserPasswd based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hm2LdapClientServerBindUserPasswd_Type.__name__ = "SnmpAdminString"
_Hm2LdapClientServerBindUserPasswd_Object = MibScalar
hm2LdapClientServerBindUserPasswd = _Hm2LdapClientServerBindUserPasswd_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 10, 6),
    _Hm2LdapClientServerBindUserPasswd_Type()
)
hm2LdapClientServerBindUserPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LdapClientServerBindUserPasswd.setStatus("current")


class _Hm2LdapClientServerDefaultDomain_Type(SnmpAdminString):
    """Custom type hm2LdapClientServerDefaultDomain based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hm2LdapClientServerDefaultDomain_Type.__name__ = "SnmpAdminString"
_Hm2LdapClientServerDefaultDomain_Object = MibScalar
hm2LdapClientServerDefaultDomain = _Hm2LdapClientServerDefaultDomain_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 10, 7),
    _Hm2LdapClientServerDefaultDomain_Type()
)
hm2LdapClientServerDefaultDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LdapClientServerDefaultDomain.setStatus("current")


class _Hm2LdapClientTlsVersions_Type(Hm2TlsVersions):
    """Custom type hm2LdapClientTlsVersions based on Hm2TlsVersions"""
    defaultBinValue = "101"


_Hm2LdapClientTlsVersions_Object = MibScalar
hm2LdapClientTlsVersions = _Hm2LdapClientTlsVersions_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 10, 8),
    _Hm2LdapClientTlsVersions_Type()
)
hm2LdapClientTlsVersions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LdapClientTlsVersions.setStatus("current")


class _Hm2LdapClientTlsCipherSuites_Type(Hm2TlsCipherSuites):
    """Custom type hm2LdapClientTlsCipherSuites based on Hm2TlsCipherSuites"""
    defaultBinValue = "0010101"


_Hm2LdapClientTlsCipherSuites_Object = MibScalar
hm2LdapClientTlsCipherSuites = _Hm2LdapClientTlsCipherSuites_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 10, 9),
    _Hm2LdapClientTlsCipherSuites_Type()
)
hm2LdapClientTlsCipherSuites.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LdapClientTlsCipherSuites.setStatus("current")
_Hm2LdapClientServerAddrTable_Object = MibTable
hm2LdapClientServerAddrTable = _Hm2LdapClientServerAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 10, 20)
)
if mibBuilder.loadTexts:
    hm2LdapClientServerAddrTable.setStatus("current")
_Hm2LdapClientServerAddrEntry_Object = MibTableRow
hm2LdapClientServerAddrEntry = _Hm2LdapClientServerAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 10, 20, 1)
)
hm2LdapClientServerAddrEntry.setIndexNames(
    (0, "HM2-REMOTE-AUTHENTICATION-MIB", "hm2LdapClientServerIndex"),
)
if mibBuilder.loadTexts:
    hm2LdapClientServerAddrEntry.setStatus("current")


class _Hm2LdapClientServerIndex_Type(Integer32):
    """Custom type hm2LdapClientServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Hm2LdapClientServerIndex_Type.__name__ = "Integer32"
_Hm2LdapClientServerIndex_Object = MibTableColumn
hm2LdapClientServerIndex = _Hm2LdapClientServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 10, 20, 1, 1),
    _Hm2LdapClientServerIndex_Type()
)
hm2LdapClientServerIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2LdapClientServerIndex.setStatus("current")


class _Hm2LdapClientServerDescr_Type(SnmpAdminString):
    """Custom type hm2LdapClientServerDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hm2LdapClientServerDescr_Type.__name__ = "SnmpAdminString"
_Hm2LdapClientServerDescr_Object = MibTableColumn
hm2LdapClientServerDescr = _Hm2LdapClientServerDescr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 10, 20, 1, 2),
    _Hm2LdapClientServerDescr_Type()
)
hm2LdapClientServerDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LdapClientServerDescr.setStatus("current")


class _Hm2LdapClientServerAddrType_Type(InetAddressType):
    """Custom type hm2LdapClientServerAddrType based on InetAddressType"""


_Hm2LdapClientServerAddrType_Object = MibTableColumn
hm2LdapClientServerAddrType = _Hm2LdapClientServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 10, 20, 1, 3),
    _Hm2LdapClientServerAddrType_Type()
)
hm2LdapClientServerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LdapClientServerAddrType.setStatus("current")


class _Hm2LdapClientServerAddr_Type(InetAddress):
    """Custom type hm2LdapClientServerAddr based on InetAddress"""
    defaultHexValue = "00000000"


_Hm2LdapClientServerAddr_Object = MibTableColumn
hm2LdapClientServerAddr = _Hm2LdapClientServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 10, 20, 1, 4),
    _Hm2LdapClientServerAddr_Type()
)
hm2LdapClientServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LdapClientServerAddr.setStatus("current")


class _Hm2LdapClientServerPort_Type(InetPortNumber):
    """Custom type hm2LdapClientServerPort based on InetPortNumber"""
    defaultValue = 389


_Hm2LdapClientServerPort_Object = MibTableColumn
hm2LdapClientServerPort = _Hm2LdapClientServerPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 10, 20, 1, 5),
    _Hm2LdapClientServerPort_Type()
)
hm2LdapClientServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LdapClientServerPort.setStatus("current")


class _Hm2LdapClientServerSecurity_Type(Integer32):
    """Custom type hm2LdapClientServerSecurity based on Integer32"""
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
        *(("none", 1),
          ("ssl", 2),
          ("startTLS", 3))
    )


_Hm2LdapClientServerSecurity_Type.__name__ = "Integer32"
_Hm2LdapClientServerSecurity_Object = MibTableColumn
hm2LdapClientServerSecurity = _Hm2LdapClientServerSecurity_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 10, 20, 1, 6),
    _Hm2LdapClientServerSecurity_Type()
)
hm2LdapClientServerSecurity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LdapClientServerSecurity.setStatus("current")


class _Hm2LdapClientServerStatus_Type(Integer32):
    """Custom type hm2LdapClientServerStatus based on Integer32"""
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
        *(("ok", 1),
          ("other", 3),
          ("unreachable", 2))
    )


_Hm2LdapClientServerStatus_Type.__name__ = "Integer32"
_Hm2LdapClientServerStatus_Object = MibTableColumn
hm2LdapClientServerStatus = _Hm2LdapClientServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 10, 20, 1, 7),
    _Hm2LdapClientServerStatus_Type()
)
hm2LdapClientServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LdapClientServerStatus.setStatus("current")
_Hm2LdapClientServerRowStatus_Type = RowStatus
_Hm2LdapClientServerRowStatus_Object = MibTableColumn
hm2LdapClientServerRowStatus = _Hm2LdapClientServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 10, 20, 1, 8),
    _Hm2LdapClientServerRowStatus_Type()
)
hm2LdapClientServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LdapClientServerRowStatus.setStatus("current")
_Hm2LdapMappingGroup_ObjectIdentity = ObjectIdentity
hm2LdapMappingGroup = _Hm2LdapMappingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 20)
)


class _Hm2LdapRoleMatchingPolicy_Type(Integer32):
    """Custom type hm2LdapRoleMatchingPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("first", 2),
          ("highest", 1))
    )


_Hm2LdapRoleMatchingPolicy_Type.__name__ = "Integer32"
_Hm2LdapRoleMatchingPolicy_Object = MibScalar
hm2LdapRoleMatchingPolicy = _Hm2LdapRoleMatchingPolicy_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 20, 1),
    _Hm2LdapRoleMatchingPolicy_Type()
)
hm2LdapRoleMatchingPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LdapRoleMatchingPolicy.setStatus("current")
_Hm2LdapRoleMappingTable_Object = MibTable
hm2LdapRoleMappingTable = _Hm2LdapRoleMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 20, 10)
)
if mibBuilder.loadTexts:
    hm2LdapRoleMappingTable.setStatus("current")
_Hm2LdapRoleMappingEntry_Object = MibTableRow
hm2LdapRoleMappingEntry = _Hm2LdapRoleMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 20, 10, 1)
)
hm2LdapRoleMappingEntry.setIndexNames(
    (0, "HM2-REMOTE-AUTHENTICATION-MIB", "hm2LdapRoleMappingIndex"),
)
if mibBuilder.loadTexts:
    hm2LdapRoleMappingEntry.setStatus("current")


class _Hm2LdapRoleMappingIndex_Type(Integer32):
    """Custom type hm2LdapRoleMappingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Hm2LdapRoleMappingIndex_Type.__name__ = "Integer32"
_Hm2LdapRoleMappingIndex_Object = MibTableColumn
hm2LdapRoleMappingIndex = _Hm2LdapRoleMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 20, 10, 1, 1),
    _Hm2LdapRoleMappingIndex_Type()
)
hm2LdapRoleMappingIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2LdapRoleMappingIndex.setStatus("current")
_Hm2LdapRoleMappingAccessRole_Type = Hm2UserAccessRoles
_Hm2LdapRoleMappingAccessRole_Object = MibTableColumn
hm2LdapRoleMappingAccessRole = _Hm2LdapRoleMappingAccessRole_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 20, 10, 1, 2),
    _Hm2LdapRoleMappingAccessRole_Type()
)
hm2LdapRoleMappingAccessRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LdapRoleMappingAccessRole.setStatus("current")


class _Hm2LdapRoleMappingType_Type(Integer32):
    """Custom type hm2LdapRoleMappingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("attribute", 1),
          ("group", 2))
    )


_Hm2LdapRoleMappingType_Type.__name__ = "Integer32"
_Hm2LdapRoleMappingType_Object = MibTableColumn
hm2LdapRoleMappingType = _Hm2LdapRoleMappingType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 20, 10, 1, 3),
    _Hm2LdapRoleMappingType_Type()
)
hm2LdapRoleMappingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LdapRoleMappingType.setStatus("current")


class _Hm2LdapRoleMappingParameter_Type(SnmpAdminString):
    """Custom type hm2LdapRoleMappingParameter based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hm2LdapRoleMappingParameter_Type.__name__ = "SnmpAdminString"
_Hm2LdapRoleMappingParameter_Object = MibTableColumn
hm2LdapRoleMappingParameter = _Hm2LdapRoleMappingParameter_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 20, 10, 1, 4),
    _Hm2LdapRoleMappingParameter_Type()
)
hm2LdapRoleMappingParameter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LdapRoleMappingParameter.setStatus("current")
_Hm2LdapRoleMappingRowStatus_Type = RowStatus
_Hm2LdapRoleMappingRowStatus_Object = MibTableColumn
hm2LdapRoleMappingRowStatus = _Hm2LdapRoleMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 1, 1, 20, 10, 1, 5),
    _Hm2LdapRoleMappingRowStatus_Type()
)
hm2LdapRoleMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2LdapRoleMappingRowStatus.setStatus("current")
_Hm2RemoteAuthMibSNMPExtensionGroup_ObjectIdentity = ObjectIdentity
hm2RemoteAuthMibSNMPExtensionGroup = _Hm2RemoteAuthMibSNMPExtensionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 3)
)
_Hm2LdapSESGroup_ObjectIdentity = ObjectIdentity
hm2LdapSESGroup = _Hm2LdapSESGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 3, 1)
)
_Hm2LdapSESDuplicateIPorHost_ObjectIdentity = ObjectIdentity
hm2LdapSESDuplicateIPorHost = _Hm2LdapSESDuplicateIPorHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hm2LdapSESDuplicateIPorHost.setStatus("current")

# Managed Objects groups


# Notification objects

hm2LdapConfigStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 26, 0, 1)
)
hm2LdapConfigStatusTrap.setObjects(
      *(("HM2-REMOTE-AUTHENTICATION-MIB", "hm2LdapClientServerIndex"),
        ("HM2-REMOTE-AUTHENTICATION-MIB", "hm2LdapClientServerStatus"))
)
if mibBuilder.loadTexts:
    hm2LdapConfigStatusTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-REMOTE-AUTHENTICATION-MIB",
    **{"hm2RemoteAuthMib": hm2RemoteAuthMib,
       "hm2RemoteAuthMibNotifications": hm2RemoteAuthMibNotifications,
       "hm2LdapConfigStatusTrap": hm2LdapConfigStatusTrap,
       "hm2RemoteAuthMibObjects": hm2RemoteAuthMibObjects,
       "hm2LdapGroup": hm2LdapGroup,
       "hm2LdapConfigGroup": hm2LdapConfigGroup,
       "hm2LdapClientAdminState": hm2LdapClientAdminState,
       "hm2LdapClientCacheTimeout": hm2LdapClientCacheTimeout,
       "hm2LdapClientServerBaseDN": hm2LdapClientServerBaseDN,
       "hm2LdapClientServerSearchAttribute": hm2LdapClientServerSearchAttribute,
       "hm2LdapClientServerBindUser": hm2LdapClientServerBindUser,
       "hm2LdapClientServerBindUserPasswd": hm2LdapClientServerBindUserPasswd,
       "hm2LdapClientServerDefaultDomain": hm2LdapClientServerDefaultDomain,
       "hm2LdapClientTlsVersions": hm2LdapClientTlsVersions,
       "hm2LdapClientTlsCipherSuites": hm2LdapClientTlsCipherSuites,
       "hm2LdapClientServerAddrTable": hm2LdapClientServerAddrTable,
       "hm2LdapClientServerAddrEntry": hm2LdapClientServerAddrEntry,
       "hm2LdapClientServerIndex": hm2LdapClientServerIndex,
       "hm2LdapClientServerDescr": hm2LdapClientServerDescr,
       "hm2LdapClientServerAddrType": hm2LdapClientServerAddrType,
       "hm2LdapClientServerAddr": hm2LdapClientServerAddr,
       "hm2LdapClientServerPort": hm2LdapClientServerPort,
       "hm2LdapClientServerSecurity": hm2LdapClientServerSecurity,
       "hm2LdapClientServerStatus": hm2LdapClientServerStatus,
       "hm2LdapClientServerRowStatus": hm2LdapClientServerRowStatus,
       "hm2LdapMappingGroup": hm2LdapMappingGroup,
       "hm2LdapRoleMatchingPolicy": hm2LdapRoleMatchingPolicy,
       "hm2LdapRoleMappingTable": hm2LdapRoleMappingTable,
       "hm2LdapRoleMappingEntry": hm2LdapRoleMappingEntry,
       "hm2LdapRoleMappingIndex": hm2LdapRoleMappingIndex,
       "hm2LdapRoleMappingAccessRole": hm2LdapRoleMappingAccessRole,
       "hm2LdapRoleMappingType": hm2LdapRoleMappingType,
       "hm2LdapRoleMappingParameter": hm2LdapRoleMappingParameter,
       "hm2LdapRoleMappingRowStatus": hm2LdapRoleMappingRowStatus,
       "hm2RemoteAuthMibSNMPExtensionGroup": hm2RemoteAuthMibSNMPExtensionGroup,
       "hm2LdapSESGroup": hm2LdapSESGroup,
       "hm2LdapSESDuplicateIPorHost": hm2LdapSESDuplicateIPorHost}
)
