# SNMP MIB module (STN-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STN-AAA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:01 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(stnNotification,
 stnSystems) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-SMI",
    "stnNotification",
    "stnSystems")

(stnEngineCpu,
 stnEngineIndex,
 stnEngineSlot) = mibBuilder.importSymbols(
    "STN-CHASSIS-MIB",
    "stnEngineCpu",
    "stnEngineIndex",
    "stnEngineSlot")

(stnRouterIndex,) = mibBuilder.importSymbols(
    "STN-ROUTER-MIB",
    "stnRouterIndex")


# MODULE-IDENTITY

stnAAA = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StnAAAObjects_ObjectIdentity = ObjectIdentity
stnAAAObjects = _StnAAAObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1)
)
_StnAAAConfig_ObjectIdentity = ObjectIdentity
stnAAAConfig = _StnAAAConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1)
)
_StnStackingRuleGroup_ObjectIdentity = ObjectIdentity
stnStackingRuleGroup = _StnStackingRuleGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 1)
)


class _StnStackingRuleProtocol_Type(Integer32):
    """Custom type stnStackingRuleProtocol based on Integer32"""
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
          ("ppp", 2))
    )


_StnStackingRuleProtocol_Type.__name__ = "Integer32"
_StnStackingRuleProtocol_Object = MibScalar
stnStackingRuleProtocol = _StnStackingRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 1, 1),
    _StnStackingRuleProtocol_Type()
)
stnStackingRuleProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnStackingRuleProtocol.setStatus("current")


class _StnStackingRuleTunnelType_Type(Integer32):
    """Custom type stnStackingRuleTunnelType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("l2tp", 4),
          ("none", 1),
          ("pptp", 2))
    )


_StnStackingRuleTunnelType_Type.__name__ = "Integer32"
_StnStackingRuleTunnelType_Object = MibScalar
stnStackingRuleTunnelType = _StnStackingRuleTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 1, 2),
    _StnStackingRuleTunnelType_Type()
)
stnStackingRuleTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnStackingRuleTunnelType.setStatus("current")


class _StnStackingRuleTunnelEndPoint_Type(DisplayString):
    """Custom type stnStackingRuleTunnelEndPoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StnStackingRuleTunnelEndPoint_Type.__name__ = "DisplayString"
_StnStackingRuleTunnelEndPoint_Object = MibScalar
stnStackingRuleTunnelEndPoint = _StnStackingRuleTunnelEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 1, 3),
    _StnStackingRuleTunnelEndPoint_Type()
)
stnStackingRuleTunnelEndPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnStackingRuleTunnelEndPoint.setStatus("current")
_StnEndPointTable_Object = MibTable
stnEndPointTable = _StnEndPointTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 2)
)
if mibBuilder.loadTexts:
    stnEndPointTable.setStatus("current")
_StnEndPointEntry_Object = MibTableRow
stnEndPointEntry = _StnEndPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 2, 1)
)
stnEndPointEntry.setIndexNames(
    (0, "STN-AAA-MIB", "stnEndPointIndex"),
)
if mibBuilder.loadTexts:
    stnEndPointEntry.setStatus("current")
_StnEndPointIndex_Type = Integer32
_StnEndPointIndex_Object = MibTableColumn
stnEndPointIndex = _StnEndPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 2, 1, 1),
    _StnEndPointIndex_Type()
)
stnEndPointIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnEndPointIndex.setStatus("current")
_StnEndPointIpAddress_Type = IpAddress
_StnEndPointIpAddress_Object = MibTableColumn
stnEndPointIpAddress = _StnEndPointIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 2, 1, 2),
    _StnEndPointIpAddress_Type()
)
stnEndPointIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnEndPointIpAddress.setStatus("current")


class _StnEndPointName_Type(DisplayString):
    """Custom type stnEndPointName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StnEndPointName_Type.__name__ = "DisplayString"
_StnEndPointName_Object = MibTableColumn
stnEndPointName = _StnEndPointName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 2, 1, 3),
    _StnEndPointName_Type()
)
stnEndPointName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnEndPointName.setStatus("current")


class _StnEndPointPassword_Type(OctetString):
    """Custom type stnEndPointPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StnEndPointPassword_Type.__name__ = "OctetString"
_StnEndPointPassword_Object = MibTableColumn
stnEndPointPassword = _StnEndPointPassword_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 2, 1, 4),
    _StnEndPointPassword_Type()
)
stnEndPointPassword.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stnEndPointPassword.setStatus("current")
_StnAddressPoolTable_Object = MibTable
stnAddressPoolTable = _StnAddressPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 3)
)
if mibBuilder.loadTexts:
    stnAddressPoolTable.setStatus("current")
_StnAddressPoolEntry_Object = MibTableRow
stnAddressPoolEntry = _StnAddressPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 3, 1)
)
stnAddressPoolEntry.setIndexNames(
    (0, "STN-AAA-MIB", "stnAddressPoolIndex"),
)
if mibBuilder.loadTexts:
    stnAddressPoolEntry.setStatus("current")
_StnAddressPoolIndex_Type = Integer32
_StnAddressPoolIndex_Object = MibTableColumn
stnAddressPoolIndex = _StnAddressPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 3, 1, 1),
    _StnAddressPoolIndex_Type()
)
stnAddressPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stnAddressPoolIndex.setStatus("current")
_StnStartIpAddress_Type = IpAddress
_StnStartIpAddress_Object = MibTableColumn
stnStartIpAddress = _StnStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 3, 1, 2),
    _StnStartIpAddress_Type()
)
stnStartIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnStartIpAddress.setStatus("current")
_StnEndIpAddress_Type = IpAddress
_StnEndIpAddress_Object = MibTableColumn
stnEndIpAddress = _StnEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 3, 1, 3),
    _StnEndIpAddress_Type()
)
stnEndIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnEndIpAddress.setStatus("current")
_StnNetworkAccessGroup_ObjectIdentity = ObjectIdentity
stnNetworkAccessGroup = _StnNetworkAccessGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 4)
)


class _StnNetworkAccessUserAuthenType_Type(Bits):
    """Custom type stnNetworkAccessUserAuthenType based on Bits"""
    namedValues = NamedValues(
        *(("internal", 1),
          ("none", 0),
          ("radius", 2))
    )

_StnNetworkAccessUserAuthenType_Type.__name__ = "Bits"
_StnNetworkAccessUserAuthenType_Object = MibScalar
stnNetworkAccessUserAuthenType = _StnNetworkAccessUserAuthenType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 4, 1),
    _StnNetworkAccessUserAuthenType_Type()
)
stnNetworkAccessUserAuthenType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNetworkAccessUserAuthenType.setStatus("current")


class _StnNetworkAccessEndPointAuthenType_Type(Bits):
    """Custom type stnNetworkAccessEndPointAuthenType based on Bits"""
    namedValues = NamedValues(
        *(("internal", 1),
          ("none", 0),
          ("radius", 2))
    )

_StnNetworkAccessEndPointAuthenType_Type.__name__ = "Bits"
_StnNetworkAccessEndPointAuthenType_Object = MibScalar
stnNetworkAccessEndPointAuthenType = _StnNetworkAccessEndPointAuthenType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 4, 2),
    _StnNetworkAccessEndPointAuthenType_Type()
)
stnNetworkAccessEndPointAuthenType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNetworkAccessEndPointAuthenType.setStatus("current")


class _StnNetworkAccessUserAccType_Type(Bits):
    """Custom type stnNetworkAccessUserAccType based on Bits"""
    namedValues = NamedValues(
        *(("internal", 1),
          ("none", 0),
          ("radius", 2))
    )

_StnNetworkAccessUserAccType_Type.__name__ = "Bits"
_StnNetworkAccessUserAccType_Object = MibScalar
stnNetworkAccessUserAccType = _StnNetworkAccessUserAccType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 4, 3),
    _StnNetworkAccessUserAccType_Type()
)
stnNetworkAccessUserAccType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNetworkAccessUserAccType.setStatus("current")


class _StnNetworkAccessEndPointAccType_Type(Bits):
    """Custom type stnNetworkAccessEndPointAccType based on Bits"""
    namedValues = NamedValues(
        *(("internal", 1),
          ("none", 0),
          ("radius", 2))
    )

_StnNetworkAccessEndPointAccType_Type.__name__ = "Bits"
_StnNetworkAccessEndPointAccType_Object = MibScalar
stnNetworkAccessEndPointAccType = _StnNetworkAccessEndPointAccType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 4, 4),
    _StnNetworkAccessEndPointAccType_Type()
)
stnNetworkAccessEndPointAccType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNetworkAccessEndPointAccType.setStatus("current")


class _StnNetworkAccessDomainName_Type(DisplayString):
    """Custom type stnNetworkAccessDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StnNetworkAccessDomainName_Type.__name__ = "DisplayString"
_StnNetworkAccessDomainName_Object = MibScalar
stnNetworkAccessDomainName = _StnNetworkAccessDomainName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 4, 5),
    _StnNetworkAccessDomainName_Type()
)
stnNetworkAccessDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNetworkAccessDomainName.setStatus("current")


class _StnNetworkAccessServiceNameRadiusAttrType_Type(Integer32):
    """Custom type stnNetworkAccessServiceNameRadiusAttrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("class", 3),
          ("filterid", 2),
          ("servicename", 1))
    )


_StnNetworkAccessServiceNameRadiusAttrType_Type.__name__ = "Integer32"
_StnNetworkAccessServiceNameRadiusAttrType_Object = MibScalar
stnNetworkAccessServiceNameRadiusAttrType = _StnNetworkAccessServiceNameRadiusAttrType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 4, 6),
    _StnNetworkAccessServiceNameRadiusAttrType_Type()
)
stnNetworkAccessServiceNameRadiusAttrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNetworkAccessServiceNameRadiusAttrType.setStatus("current")
_StnNetworkAccessLdapAuthorizationUpdateTime_Type = Integer32
_StnNetworkAccessLdapAuthorizationUpdateTime_Object = MibScalar
stnNetworkAccessLdapAuthorizationUpdateTime = _StnNetworkAccessLdapAuthorizationUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 4, 7),
    _StnNetworkAccessLdapAuthorizationUpdateTime_Type()
)
stnNetworkAccessLdapAuthorizationUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNetworkAccessLdapAuthorizationUpdateTime.setStatus("current")
_StnNetworkAccessLdapUpdateNotification_Type = DisplayString
_StnNetworkAccessLdapUpdateNotification_Object = MibScalar
stnNetworkAccessLdapUpdateNotification = _StnNetworkAccessLdapUpdateNotification_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 4, 8),
    _StnNetworkAccessLdapUpdateNotification_Type()
)
stnNetworkAccessLdapUpdateNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stnNetworkAccessLdapUpdateNotification.setStatus("current")


class _StnNetworkAccessRealmAttrType_Type(Integer32):
    """Custom type stnNetworkAccessRealmAttrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cisco-Avpair", 1),
          ("springTide-ST-Realm-Name", 0))
    )


_StnNetworkAccessRealmAttrType_Type.__name__ = "Integer32"
_StnNetworkAccessRealmAttrType_Object = MibScalar
stnNetworkAccessRealmAttrType = _StnNetworkAccessRealmAttrType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 4, 9),
    _StnNetworkAccessRealmAttrType_Type()
)
stnNetworkAccessRealmAttrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNetworkAccessRealmAttrType.setStatus("current")
_StnRadiusAccServerTable_Object = MibTable
stnRadiusAccServerTable = _StnRadiusAccServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 5)
)
if mibBuilder.loadTexts:
    stnRadiusAccServerTable.setStatus("current")
_StnRadiusAccServerEntry_Object = MibTableRow
stnRadiusAccServerEntry = _StnRadiusAccServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 5, 1)
)
stnRadiusAccServerEntry.setIndexNames(
    (0, "STN-AAA-MIB", "stnRadiusAccServerIndex"),
)
if mibBuilder.loadTexts:
    stnRadiusAccServerEntry.setStatus("current")
_StnRadiusAccServerIndex_Type = Integer32
_StnRadiusAccServerIndex_Object = MibTableColumn
stnRadiusAccServerIndex = _StnRadiusAccServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 5, 1, 1),
    _StnRadiusAccServerIndex_Type()
)
stnRadiusAccServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stnRadiusAccServerIndex.setStatus("current")
_StnRadiusAccServerAddress_Type = IpAddress
_StnRadiusAccServerAddress_Object = MibTableColumn
stnRadiusAccServerAddress = _StnRadiusAccServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 5, 1, 2),
    _StnRadiusAccServerAddress_Type()
)
stnRadiusAccServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRadiusAccServerAddress.setStatus("current")
_StnRadiusAccServerDestPort_Type = Integer32
_StnRadiusAccServerDestPort_Object = MibTableColumn
stnRadiusAccServerDestPort = _StnRadiusAccServerDestPort_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 5, 1, 3),
    _StnRadiusAccServerDestPort_Type()
)
stnRadiusAccServerDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRadiusAccServerDestPort.setStatus("current")


class _StnRadiusAccServerRetrans_Type(Integer32):
    """Custom type stnRadiusAccServerRetrans based on Integer32"""
    defaultValue = 10


_StnRadiusAccServerRetrans_Object = MibTableColumn
stnRadiusAccServerRetrans = _StnRadiusAccServerRetrans_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 5, 1, 4),
    _StnRadiusAccServerRetrans_Type()
)
stnRadiusAccServerRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRadiusAccServerRetrans.setStatus("current")


class _StnRadiusAccServerTimeOut_Type(Integer32):
    """Custom type stnRadiusAccServerTimeOut based on Integer32"""
    defaultValue = 60


_StnRadiusAccServerTimeOut_Object = MibTableColumn
stnRadiusAccServerTimeOut = _StnRadiusAccServerTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 5, 1, 5),
    _StnRadiusAccServerTimeOut_Type()
)
stnRadiusAccServerTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRadiusAccServerTimeOut.setStatus("current")


class _StnRadiusAccServerSecret_Type(OctetString):
    """Custom type stnRadiusAccServerSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StnRadiusAccServerSecret_Type.__name__ = "OctetString"
_StnRadiusAccServerSecret_Object = MibTableColumn
stnRadiusAccServerSecret = _StnRadiusAccServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 5, 1, 6),
    _StnRadiusAccServerSecret_Type()
)
stnRadiusAccServerSecret.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stnRadiusAccServerSecret.setStatus("current")


class _StnRadiusAccServerName_Type(DisplayString):
    """Custom type stnRadiusAccServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StnRadiusAccServerName_Type.__name__ = "DisplayString"
_StnRadiusAccServerName_Object = MibTableColumn
stnRadiusAccServerName = _StnRadiusAccServerName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 5, 1, 7),
    _StnRadiusAccServerName_Type()
)
stnRadiusAccServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRadiusAccServerName.setStatus("current")
_StnRadiusAccServerConfigInstance_Type = Integer32
_StnRadiusAccServerConfigInstance_Object = MibTableColumn
stnRadiusAccServerConfigInstance = _StnRadiusAccServerConfigInstance_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 5, 1, 8),
    _StnRadiusAccServerConfigInstance_Type()
)
stnRadiusAccServerConfigInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRadiusAccServerConfigInstance.setStatus("current")
_StnRadiusAuthServerTable_Object = MibTable
stnRadiusAuthServerTable = _StnRadiusAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 6)
)
if mibBuilder.loadTexts:
    stnRadiusAuthServerTable.setStatus("current")
_StnRadiusAuthServerEntry_Object = MibTableRow
stnRadiusAuthServerEntry = _StnRadiusAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 6, 1)
)
stnRadiusAuthServerEntry.setIndexNames(
    (0, "STN-AAA-MIB", "stnRadiusAuthServerIndex"),
)
if mibBuilder.loadTexts:
    stnRadiusAuthServerEntry.setStatus("current")
_StnRadiusAuthServerIndex_Type = Integer32
_StnRadiusAuthServerIndex_Object = MibTableColumn
stnRadiusAuthServerIndex = _StnRadiusAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 6, 1, 1),
    _StnRadiusAuthServerIndex_Type()
)
stnRadiusAuthServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stnRadiusAuthServerIndex.setStatus("current")
_StnRadiusAuthServerAddress_Type = IpAddress
_StnRadiusAuthServerAddress_Object = MibTableColumn
stnRadiusAuthServerAddress = _StnRadiusAuthServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 6, 1, 2),
    _StnRadiusAuthServerAddress_Type()
)
stnRadiusAuthServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRadiusAuthServerAddress.setStatus("current")
_StnRadiusAuthServerDestPort_Type = Integer32
_StnRadiusAuthServerDestPort_Object = MibTableColumn
stnRadiusAuthServerDestPort = _StnRadiusAuthServerDestPort_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 6, 1, 3),
    _StnRadiusAuthServerDestPort_Type()
)
stnRadiusAuthServerDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRadiusAuthServerDestPort.setStatus("current")


class _StnRadiusAuthServerRetrans_Type(Integer32):
    """Custom type stnRadiusAuthServerRetrans based on Integer32"""
    defaultValue = 6


_StnRadiusAuthServerRetrans_Object = MibTableColumn
stnRadiusAuthServerRetrans = _StnRadiusAuthServerRetrans_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 6, 1, 4),
    _StnRadiusAuthServerRetrans_Type()
)
stnRadiusAuthServerRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRadiusAuthServerRetrans.setStatus("current")


class _StnRadiusAuthServerTimeOut_Type(Integer32):
    """Custom type stnRadiusAuthServerTimeOut based on Integer32"""
    defaultValue = 5


_StnRadiusAuthServerTimeOut_Object = MibTableColumn
stnRadiusAuthServerTimeOut = _StnRadiusAuthServerTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 6, 1, 5),
    _StnRadiusAuthServerTimeOut_Type()
)
stnRadiusAuthServerTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRadiusAuthServerTimeOut.setStatus("current")


class _StnRadiusAuthServerSecret_Type(OctetString):
    """Custom type stnRadiusAuthServerSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StnRadiusAuthServerSecret_Type.__name__ = "OctetString"
_StnRadiusAuthServerSecret_Object = MibTableColumn
stnRadiusAuthServerSecret = _StnRadiusAuthServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 6, 1, 6),
    _StnRadiusAuthServerSecret_Type()
)
stnRadiusAuthServerSecret.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stnRadiusAuthServerSecret.setStatus("current")


class _StnRadiusAuthServerName_Type(DisplayString):
    """Custom type stnRadiusAuthServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StnRadiusAuthServerName_Type.__name__ = "DisplayString"
_StnRadiusAuthServerName_Object = MibTableColumn
stnRadiusAuthServerName = _StnRadiusAuthServerName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 6, 1, 7),
    _StnRadiusAuthServerName_Type()
)
stnRadiusAuthServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRadiusAuthServerName.setStatus("current")
_StnRadiusAuthServerConfigInstance_Type = Integer32
_StnRadiusAuthServerConfigInstance_Object = MibTableColumn
stnRadiusAuthServerConfigInstance = _StnRadiusAuthServerConfigInstance_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 6, 1, 8),
    _StnRadiusAuthServerConfigInstance_Type()
)
stnRadiusAuthServerConfigInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRadiusAuthServerConfigInstance.setStatus("current")
_StnUserTable_Object = MibTable
stnUserTable = _StnUserTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7)
)
if mibBuilder.loadTexts:
    stnUserTable.setStatus("current")
_StnUserEntry_Object = MibTableRow
stnUserEntry = _StnUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1)
)
stnUserEntry.setIndexNames(
    (0, "STN-AAA-MIB", "stnUserIndex"),
)
if mibBuilder.loadTexts:
    stnUserEntry.setStatus("current")
_StnUserIndex_Type = Integer32
_StnUserIndex_Object = MibTableColumn
stnUserIndex = _StnUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 1),
    _StnUserIndex_Type()
)
stnUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserIndex.setStatus("current")


class _StnUserName_Type(DisplayString):
    """Custom type stnUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StnUserName_Type.__name__ = "DisplayString"
_StnUserName_Object = MibTableColumn
stnUserName = _StnUserName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 2),
    _StnUserName_Type()
)
stnUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserName.setStatus("current")


class _StnUserPassword_Type(OctetString):
    """Custom type stnUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StnUserPassword_Type.__name__ = "OctetString"
_StnUserPassword_Object = MibTableColumn
stnUserPassword = _StnUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 3),
    _StnUserPassword_Type()
)
stnUserPassword.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stnUserPassword.setStatus("current")
_StnUserIpAddress_Type = IpAddress
_StnUserIpAddress_Object = MibTableColumn
stnUserIpAddress = _StnUserIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 4),
    _StnUserIpAddress_Type()
)
stnUserIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserIpAddress.setStatus("current")
_StnUserIpNetMask_Type = IpAddress
_StnUserIpNetMask_Object = MibTableColumn
stnUserIpNetMask = _StnUserIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 5),
    _StnUserIpNetMask_Type()
)
stnUserIpNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserIpNetMask.setStatus("current")


class _StnUserIpRouting_Type(Integer32):
    """Custom type stnUserIpRouting based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("listen", 3),
          ("none", 1),
          ("send", 2),
          ("unset", 0))
    )


_StnUserIpRouting_Type.__name__ = "Integer32"
_StnUserIpRouting_Object = MibTableColumn
stnUserIpRouting = _StnUserIpRouting_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 6),
    _StnUserIpRouting_Type()
)
stnUserIpRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserIpRouting.setStatus("current")


class _StnUserMTU_Type(Integer32):
    """Custom type stnUserMTU based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 65532),
    )


_StnUserMTU_Type.__name__ = "Integer32"
_StnUserMTU_Object = MibTableColumn
stnUserMTU = _StnUserMTU_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 7),
    _StnUserMTU_Type()
)
stnUserMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserMTU.setStatus("current")


class _StnUserIpCompression_Type(Integer32):
    """Custom type stnUserIpCompression based on Integer32"""
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
          ("vj", 2))
    )


_StnUserIpCompression_Type.__name__ = "Integer32"
_StnUserIpCompression_Object = MibTableColumn
stnUserIpCompression = _StnUserIpCompression_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 8),
    _StnUserIpCompression_Type()
)
stnUserIpCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserIpCompression.setStatus("current")


class _StnUserTimeOut_Type(Integer32):
    """Custom type stnUserTimeOut based on Integer32"""
    defaultValue = 0


_StnUserTimeOut_Object = MibTableColumn
stnUserTimeOut = _StnUserTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 9),
    _StnUserTimeOut_Type()
)
stnUserTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserTimeOut.setStatus("current")


class _StnUserIdleTime_Type(Integer32):
    """Custom type stnUserIdleTime based on Integer32"""
    defaultValue = 0


_StnUserIdleTime_Object = MibTableColumn
stnUserIdleTime = _StnUserIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 10),
    _StnUserIdleTime_Type()
)
stnUserIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserIdleTime.setStatus("current")


class _StnUserTunnelType_Type(Integer32):
    """Custom type stnUserTunnelType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("l2tp", 4),
          ("none", 1),
          ("pptp", 2),
          ("unset", 0))
    )


_StnUserTunnelType_Type.__name__ = "Integer32"
_StnUserTunnelType_Object = MibTableColumn
stnUserTunnelType = _StnUserTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 11),
    _StnUserTunnelType_Type()
)
stnUserTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserTunnelType.setStatus("current")


class _StnUserTunnelServerEndPoint_Type(DisplayString):
    """Custom type stnUserTunnelServerEndPoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StnUserTunnelServerEndPoint_Type.__name__ = "DisplayString"
_StnUserTunnelServerEndPoint_Object = MibTableColumn
stnUserTunnelServerEndPoint = _StnUserTunnelServerEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 12),
    _StnUserTunnelServerEndPoint_Type()
)
stnUserTunnelServerEndPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserTunnelServerEndPoint.setStatus("current")


class _StnUserTunnelClientEndPoint_Type(DisplayString):
    """Custom type stnUserTunnelClientEndPoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StnUserTunnelClientEndPoint_Type.__name__ = "DisplayString"
_StnUserTunnelClientEndPoint_Object = MibTableColumn
stnUserTunnelClientEndPoint = _StnUserTunnelClientEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 13),
    _StnUserTunnelClientEndPoint_Type()
)
stnUserTunnelClientEndPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserTunnelClientEndPoint.setStatus("current")
_StnUserAssignedTunnelName_Type = DisplayString
_StnUserAssignedTunnelName_Object = MibTableColumn
stnUserAssignedTunnelName = _StnUserAssignedTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 14),
    _StnUserAssignedTunnelName_Type()
)
stnUserAssignedTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserAssignedTunnelName.setStatus("current")


class _StnUserTunnelPassword_Type(OctetString):
    """Custom type stnUserTunnelPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StnUserTunnelPassword_Type.__name__ = "OctetString"
_StnUserTunnelPassword_Object = MibTableColumn
stnUserTunnelPassword = _StnUserTunnelPassword_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 15),
    _StnUserTunnelPassword_Type()
)
stnUserTunnelPassword.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stnUserTunnelPassword.setStatus("current")


class _StnUserServiceType_Type(Integer32):
    """Custom type stnUserServiceType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              6,
              101)
        )
    )
    namedValues = NamedValues(
        *(("administrative", 6),
          ("framed", 2),
          ("login", 1),
          ("provisioner", 101),
          ("unset", 0))
    )


_StnUserServiceType_Type.__name__ = "Integer32"
_StnUserServiceType_Object = MibTableColumn
stnUserServiceType = _StnUserServiceType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 16),
    _StnUserServiceType_Type()
)
stnUserServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserServiceType.setStatus("current")


class _StnUserIpFilters_Type(OctetString):
    """Custom type stnUserIpFilters based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_StnUserIpFilters_Type.__name__ = "OctetString"
_StnUserIpFilters_Object = MibTableColumn
stnUserIpFilters = _StnUserIpFilters_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 17),
    _StnUserIpFilters_Type()
)
stnUserIpFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserIpFilters.setStatus("obsolete")


class _StnUserIpRoutes_Type(OctetString):
    """Custom type stnUserIpRoutes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_StnUserIpRoutes_Type.__name__ = "OctetString"
_StnUserIpRoutes_Object = MibTableColumn
stnUserIpRoutes = _StnUserIpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 18),
    _StnUserIpRoutes_Type()
)
stnUserIpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserIpRoutes.setStatus("current")
_StnUserPrimaryDNSServer_Type = IpAddress
_StnUserPrimaryDNSServer_Object = MibTableColumn
stnUserPrimaryDNSServer = _StnUserPrimaryDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 19),
    _StnUserPrimaryDNSServer_Type()
)
stnUserPrimaryDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserPrimaryDNSServer.setStatus("current")
_StnUserSecondaryDNSServer_Type = IpAddress
_StnUserSecondaryDNSServer_Object = MibTableColumn
stnUserSecondaryDNSServer = _StnUserSecondaryDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 20),
    _StnUserSecondaryDNSServer_Type()
)
stnUserSecondaryDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserSecondaryDNSServer.setStatus("current")
_StnUserPrimaryNBNSServer_Type = IpAddress
_StnUserPrimaryNBNSServer_Object = MibTableColumn
stnUserPrimaryNBNSServer = _StnUserPrimaryNBNSServer_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 21),
    _StnUserPrimaryNBNSServer_Type()
)
stnUserPrimaryNBNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserPrimaryNBNSServer.setStatus("current")
_StnUserSecondaryNBNSServer_Type = IpAddress
_StnUserSecondaryNBNSServer_Object = MibTableColumn
stnUserSecondaryNBNSServer = _StnUserSecondaryNBNSServer_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 22),
    _StnUserSecondaryNBNSServer_Type()
)
stnUserSecondaryNBNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserSecondaryNBNSServer.setStatus("current")


class _StnUserServiceName_Type(DisplayString):
    """Custom type stnUserServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_StnUserServiceName_Type.__name__ = "DisplayString"
_StnUserServiceName_Object = MibTableColumn
stnUserServiceName = _StnUserServiceName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 23),
    _StnUserServiceName_Type()
)
stnUserServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserServiceName.setStatus("current")
_StnUserPhysicalPort_Type = Integer32
_StnUserPhysicalPort_Object = MibTableColumn
stnUserPhysicalPort = _StnUserPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 24),
    _StnUserPhysicalPort_Type()
)
stnUserPhysicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserPhysicalPort.setStatus("current")
_StnUserPhysicalSlot_Type = Integer32
_StnUserPhysicalSlot_Object = MibTableColumn
stnUserPhysicalSlot = _StnUserPhysicalSlot_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 25),
    _StnUserPhysicalSlot_Type()
)
stnUserPhysicalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserPhysicalSlot.setStatus("current")
_StnUserVirtualPathId_Type = Integer32
_StnUserVirtualPathId_Object = MibTableColumn
stnUserVirtualPathId = _StnUserVirtualPathId_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 26),
    _StnUserVirtualPathId_Type()
)
stnUserVirtualPathId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserVirtualPathId.setStatus("current")
_StnUserVirtualCircuitId_Type = Integer32
_StnUserVirtualCircuitId_Object = MibTableColumn
stnUserVirtualCircuitId = _StnUserVirtualCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 27),
    _StnUserVirtualCircuitId_Type()
)
stnUserVirtualCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserVirtualCircuitId.setStatus("current")
_StnUserRealmInstance_Type = Integer32
_StnUserRealmInstance_Object = MibTableColumn
stnUserRealmInstance = _StnUserRealmInstance_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 7, 1, 28),
    _StnUserRealmInstance_Type()
)
stnUserRealmInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserRealmInstance.setStatus("current")
_StnDefaultPppUserGroup_ObjectIdentity = ObjectIdentity
stnDefaultPppUserGroup = _StnDefaultPppUserGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 8)
)
_StnDefaultUserIpAddress_Type = IpAddress
_StnDefaultUserIpAddress_Object = MibScalar
stnDefaultUserIpAddress = _StnDefaultUserIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 8, 1),
    _StnDefaultUserIpAddress_Type()
)
stnDefaultUserIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnDefaultUserIpAddress.setStatus("current")
_StnDefaultUserIpNetMask_Type = IpAddress
_StnDefaultUserIpNetMask_Object = MibScalar
stnDefaultUserIpNetMask = _StnDefaultUserIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 8, 2),
    _StnDefaultUserIpNetMask_Type()
)
stnDefaultUserIpNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnDefaultUserIpNetMask.setStatus("current")


class _StnDefaultUserIpRouting_Type(Integer32):
    """Custom type stnDefaultUserIpRouting based on Integer32"""
    defaultValue = 1

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
        *(("both", 4),
          ("listen", 3),
          ("none", 1),
          ("send", 2))
    )


_StnDefaultUserIpRouting_Type.__name__ = "Integer32"
_StnDefaultUserIpRouting_Object = MibScalar
stnDefaultUserIpRouting = _StnDefaultUserIpRouting_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 8, 3),
    _StnDefaultUserIpRouting_Type()
)
stnDefaultUserIpRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnDefaultUserIpRouting.setStatus("current")


class _StnDefaultUserMTU_Type(Integer32):
    """Custom type stnDefaultUserMTU based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 65532),
    )


_StnDefaultUserMTU_Type.__name__ = "Integer32"
_StnDefaultUserMTU_Object = MibScalar
stnDefaultUserMTU = _StnDefaultUserMTU_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 8, 4),
    _StnDefaultUserMTU_Type()
)
stnDefaultUserMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnDefaultUserMTU.setStatus("current")


class _StnDefaultUserIpCompression_Type(Integer32):
    """Custom type stnDefaultUserIpCompression based on Integer32"""
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
          ("vj", 2))
    )


_StnDefaultUserIpCompression_Type.__name__ = "Integer32"
_StnDefaultUserIpCompression_Object = MibScalar
stnDefaultUserIpCompression = _StnDefaultUserIpCompression_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 8, 5),
    _StnDefaultUserIpCompression_Type()
)
stnDefaultUserIpCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnDefaultUserIpCompression.setStatus("current")


class _StnDefaultUserTimeOut_Type(Integer32):
    """Custom type stnDefaultUserTimeOut based on Integer32"""
    defaultValue = 0


_StnDefaultUserTimeOut_Object = MibScalar
stnDefaultUserTimeOut = _StnDefaultUserTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 8, 6),
    _StnDefaultUserTimeOut_Type()
)
stnDefaultUserTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnDefaultUserTimeOut.setStatus("current")


class _StnDefaultUserIdleTime_Type(Integer32):
    """Custom type stnDefaultUserIdleTime based on Integer32"""
    defaultValue = 0


_StnDefaultUserIdleTime_Object = MibScalar
stnDefaultUserIdleTime = _StnDefaultUserIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 8, 7),
    _StnDefaultUserIdleTime_Type()
)
stnDefaultUserIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnDefaultUserIdleTime.setStatus("current")


class _StnDefaultUserTunnelType_Type(Integer32):
    """Custom type stnDefaultUserTunnelType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("l2tp", 4),
          ("none", 1),
          ("pptp", 2))
    )


_StnDefaultUserTunnelType_Type.__name__ = "Integer32"
_StnDefaultUserTunnelType_Object = MibScalar
stnDefaultUserTunnelType = _StnDefaultUserTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 8, 8),
    _StnDefaultUserTunnelType_Type()
)
stnDefaultUserTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnDefaultUserTunnelType.setStatus("current")


class _StnDefaultUserTunnelServerEndPoint_Type(DisplayString):
    """Custom type stnDefaultUserTunnelServerEndPoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StnDefaultUserTunnelServerEndPoint_Type.__name__ = "DisplayString"
_StnDefaultUserTunnelServerEndPoint_Object = MibScalar
stnDefaultUserTunnelServerEndPoint = _StnDefaultUserTunnelServerEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 8, 9),
    _StnDefaultUserTunnelServerEndPoint_Type()
)
stnDefaultUserTunnelServerEndPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnDefaultUserTunnelServerEndPoint.setStatus("current")


class _StnDefaultUserTunnelClientEndPoint_Type(DisplayString):
    """Custom type stnDefaultUserTunnelClientEndPoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StnDefaultUserTunnelClientEndPoint_Type.__name__ = "DisplayString"
_StnDefaultUserTunnelClientEndPoint_Object = MibScalar
stnDefaultUserTunnelClientEndPoint = _StnDefaultUserTunnelClientEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 8, 10),
    _StnDefaultUserTunnelClientEndPoint_Type()
)
stnDefaultUserTunnelClientEndPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnDefaultUserTunnelClientEndPoint.setStatus("current")


class _StnDefaultUserIpFilters_Type(OctetString):
    """Custom type stnDefaultUserIpFilters based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_StnDefaultUserIpFilters_Type.__name__ = "OctetString"
_StnDefaultUserIpFilters_Object = MibScalar
stnDefaultUserIpFilters = _StnDefaultUserIpFilters_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 8, 11),
    _StnDefaultUserIpFilters_Type()
)
stnDefaultUserIpFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnDefaultUserIpFilters.setStatus("obsolete")


class _StnDefaultUserIpRoutes_Type(OctetString):
    """Custom type stnDefaultUserIpRoutes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_StnDefaultUserIpRoutes_Type.__name__ = "OctetString"
_StnDefaultUserIpRoutes_Object = MibScalar
stnDefaultUserIpRoutes = _StnDefaultUserIpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 8, 12),
    _StnDefaultUserIpRoutes_Type()
)
stnDefaultUserIpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnDefaultUserIpRoutes.setStatus("current")
_StnDefaultUserPrimaryDNSServer_Type = IpAddress
_StnDefaultUserPrimaryDNSServer_Object = MibScalar
stnDefaultUserPrimaryDNSServer = _StnDefaultUserPrimaryDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 8, 13),
    _StnDefaultUserPrimaryDNSServer_Type()
)
stnDefaultUserPrimaryDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnDefaultUserPrimaryDNSServer.setStatus("current")
_StnDefaultUserSecondaryDNSServer_Type = IpAddress
_StnDefaultUserSecondaryDNSServer_Object = MibScalar
stnDefaultUserSecondaryDNSServer = _StnDefaultUserSecondaryDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 8, 14),
    _StnDefaultUserSecondaryDNSServer_Type()
)
stnDefaultUserSecondaryDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnDefaultUserSecondaryDNSServer.setStatus("current")
_StnDefaultUserPrimaryNBNSServer_Type = IpAddress
_StnDefaultUserPrimaryNBNSServer_Object = MibScalar
stnDefaultUserPrimaryNBNSServer = _StnDefaultUserPrimaryNBNSServer_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 8, 15),
    _StnDefaultUserPrimaryNBNSServer_Type()
)
stnDefaultUserPrimaryNBNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnDefaultUserPrimaryNBNSServer.setStatus("current")
_StnDefaultUserSecondaryNBNSServer_Type = IpAddress
_StnDefaultUserSecondaryNBNSServer_Object = MibScalar
stnDefaultUserSecondaryNBNSServer = _StnDefaultUserSecondaryNBNSServer_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 8, 16),
    _StnDefaultUserSecondaryNBNSServer_Type()
)
stnDefaultUserSecondaryNBNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnDefaultUserSecondaryNBNSServer.setStatus("current")


class _StnDefaultUserServiceName_Type(DisplayString):
    """Custom type stnDefaultUserServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_StnDefaultUserServiceName_Type.__name__ = "DisplayString"
_StnDefaultUserServiceName_Object = MibScalar
stnDefaultUserServiceName = _StnDefaultUserServiceName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 8, 17),
    _StnDefaultUserServiceName_Type()
)
stnDefaultUserServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnDefaultUserServiceName.setStatus("current")
_StnNoAuthPppUserGroup_ObjectIdentity = ObjectIdentity
stnNoAuthPppUserGroup = _StnNoAuthPppUserGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 9)
)


class _StnNoAuthPppUserName_Type(DisplayString):
    """Custom type stnNoAuthPppUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StnNoAuthPppUserName_Type.__name__ = "DisplayString"
_StnNoAuthPppUserName_Object = MibScalar
stnNoAuthPppUserName = _StnNoAuthPppUserName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 9, 1),
    _StnNoAuthPppUserName_Type()
)
stnNoAuthPppUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNoAuthPppUserName.setStatus("current")


class _StnNoAuthPppUserPassword_Type(OctetString):
    """Custom type stnNoAuthPppUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StnNoAuthPppUserPassword_Type.__name__ = "OctetString"
_StnNoAuthPppUserPassword_Object = MibScalar
stnNoAuthPppUserPassword = _StnNoAuthPppUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 9, 2),
    _StnNoAuthPppUserPassword_Type()
)
stnNoAuthPppUserPassword.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stnNoAuthPppUserPassword.setStatus("current")
_StnUserIpFilterTable_Object = MibTable
stnUserIpFilterTable = _StnUserIpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 10)
)
if mibBuilder.loadTexts:
    stnUserIpFilterTable.setStatus("obsolete")
_StnUserIpFilterEntry_Object = MibTableRow
stnUserIpFilterEntry = _StnUserIpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 10, 1)
)
stnUserIpFilterEntry.setIndexNames(
    (0, "STN-AAA-MIB", "stnUserIpFilterIndex"),
)
if mibBuilder.loadTexts:
    stnUserIpFilterEntry.setStatus("obsolete")
_StnUserIpFilterIndex_Type = Integer32
_StnUserIpFilterIndex_Object = MibTableColumn
stnUserIpFilterIndex = _StnUserIpFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 10, 1, 1),
    _StnUserIpFilterIndex_Type()
)
stnUserIpFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserIpFilterIndex.setStatus("obsolete")


class _StnUserIpFilterName_Type(DisplayString):
    """Custom type stnUserIpFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StnUserIpFilterName_Type.__name__ = "DisplayString"
_StnUserIpFilterName_Object = MibTableColumn
stnUserIpFilterName = _StnUserIpFilterName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 10, 1, 2),
    _StnUserIpFilterName_Type()
)
stnUserIpFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserIpFilterName.setStatus("obsolete")


class _StnUserIpFilterRules_Type(OctetString):
    """Custom type stnUserIpFilterRules based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_StnUserIpFilterRules_Type.__name__ = "OctetString"
_StnUserIpFilterRules_Object = MibTableColumn
stnUserIpFilterRules = _StnUserIpFilterRules_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 10, 1, 3),
    _StnUserIpFilterRules_Type()
)
stnUserIpFilterRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserIpFilterRules.setStatus("obsolete")
_StnUserIpFilterRuleTable_Object = MibTable
stnUserIpFilterRuleTable = _StnUserIpFilterRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 11)
)
if mibBuilder.loadTexts:
    stnUserIpFilterRuleTable.setStatus("obsolete")
_StnUserIpFilterRuleEntry_Object = MibTableRow
stnUserIpFilterRuleEntry = _StnUserIpFilterRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 11, 1)
)
stnUserIpFilterRuleEntry.setIndexNames(
    (0, "STN-AAA-MIB", "stnUserIpFilterRuleIndex"),
)
if mibBuilder.loadTexts:
    stnUserIpFilterRuleEntry.setStatus("obsolete")
_StnUserIpFilterRuleIndex_Type = Integer32
_StnUserIpFilterRuleIndex_Object = MibTableColumn
stnUserIpFilterRuleIndex = _StnUserIpFilterRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 11, 1, 1),
    _StnUserIpFilterRuleIndex_Type()
)
stnUserIpFilterRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserIpFilterRuleIndex.setStatus("obsolete")
_StnUserIpFilterRuleSrcAddress_Type = IpAddress
_StnUserIpFilterRuleSrcAddress_Object = MibTableColumn
stnUserIpFilterRuleSrcAddress = _StnUserIpFilterRuleSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 11, 1, 2),
    _StnUserIpFilterRuleSrcAddress_Type()
)
stnUserIpFilterRuleSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserIpFilterRuleSrcAddress.setStatus("obsolete")
_StnUserIpFilterRuleSrcNetMask_Type = IpAddress
_StnUserIpFilterRuleSrcNetMask_Object = MibTableColumn
stnUserIpFilterRuleSrcNetMask = _StnUserIpFilterRuleSrcNetMask_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 11, 1, 3),
    _StnUserIpFilterRuleSrcNetMask_Type()
)
stnUserIpFilterRuleSrcNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserIpFilterRuleSrcNetMask.setStatus("obsolete")
_StnUserIpFilterRuleSrcPort_Type = Integer32
_StnUserIpFilterRuleSrcPort_Object = MibTableColumn
stnUserIpFilterRuleSrcPort = _StnUserIpFilterRuleSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 11, 1, 4),
    _StnUserIpFilterRuleSrcPort_Type()
)
stnUserIpFilterRuleSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserIpFilterRuleSrcPort.setStatus("obsolete")
_StnUserIpFilterRuleDestAddress_Type = IpAddress
_StnUserIpFilterRuleDestAddress_Object = MibTableColumn
stnUserIpFilterRuleDestAddress = _StnUserIpFilterRuleDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 11, 1, 5),
    _StnUserIpFilterRuleDestAddress_Type()
)
stnUserIpFilterRuleDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserIpFilterRuleDestAddress.setStatus("obsolete")
_StnUserIpFilterRuleDestNetMask_Type = IpAddress
_StnUserIpFilterRuleDestNetMask_Object = MibTableColumn
stnUserIpFilterRuleDestNetMask = _StnUserIpFilterRuleDestNetMask_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 11, 1, 6),
    _StnUserIpFilterRuleDestNetMask_Type()
)
stnUserIpFilterRuleDestNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserIpFilterRuleDestNetMask.setStatus("obsolete")
_StnUserIpFilterRuleDestPort_Type = Integer32
_StnUserIpFilterRuleDestPort_Object = MibTableColumn
stnUserIpFilterRuleDestPort = _StnUserIpFilterRuleDestPort_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 11, 1, 7),
    _StnUserIpFilterRuleDestPort_Type()
)
stnUserIpFilterRuleDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserIpFilterRuleDestPort.setStatus("obsolete")
_StnUserIpFilterRuleProtocol_Type = Integer32
_StnUserIpFilterRuleProtocol_Object = MibTableColumn
stnUserIpFilterRuleProtocol = _StnUserIpFilterRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 11, 1, 8),
    _StnUserIpFilterRuleProtocol_Type()
)
stnUserIpFilterRuleProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserIpFilterRuleProtocol.setStatus("obsolete")
_StnUserIpFilterRuleAction_Type = Integer32
_StnUserIpFilterRuleAction_Object = MibTableColumn
stnUserIpFilterRuleAction = _StnUserIpFilterRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 11, 1, 9),
    _StnUserIpFilterRuleAction_Type()
)
stnUserIpFilterRuleAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserIpFilterRuleAction.setStatus("obsolete")


class _StnUserIpFilterRuleEndPoint_Type(DisplayString):
    """Custom type stnUserIpFilterRuleEndPoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StnUserIpFilterRuleEndPoint_Type.__name__ = "DisplayString"
_StnUserIpFilterRuleEndPoint_Object = MibTableColumn
stnUserIpFilterRuleEndPoint = _StnUserIpFilterRuleEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 11, 1, 10),
    _StnUserIpFilterRuleEndPoint_Type()
)
stnUserIpFilterRuleEndPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserIpFilterRuleEndPoint.setStatus("obsolete")
_StnUserIpRouteTable_Object = MibTable
stnUserIpRouteTable = _StnUserIpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 12)
)
if mibBuilder.loadTexts:
    stnUserIpRouteTable.setStatus("current")
_StnUserIpRouteEntry_Object = MibTableRow
stnUserIpRouteEntry = _StnUserIpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 12, 1)
)
stnUserIpRouteEntry.setIndexNames(
    (0, "STN-AAA-MIB", "stnUserIpRouteIndex"),
)
if mibBuilder.loadTexts:
    stnUserIpRouteEntry.setStatus("current")
_StnUserIpRouteIndex_Type = Integer32
_StnUserIpRouteIndex_Object = MibTableColumn
stnUserIpRouteIndex = _StnUserIpRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 12, 1, 1),
    _StnUserIpRouteIndex_Type()
)
stnUserIpRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserIpRouteIndex.setStatus("current")
_StnUserIpRouteDestAddress_Type = IpAddress
_StnUserIpRouteDestAddress_Object = MibTableColumn
stnUserIpRouteDestAddress = _StnUserIpRouteDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 12, 1, 2),
    _StnUserIpRouteDestAddress_Type()
)
stnUserIpRouteDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserIpRouteDestAddress.setStatus("current")
_StnUserIpRouteDestNetMask_Type = IpAddress
_StnUserIpRouteDestNetMask_Object = MibTableColumn
stnUserIpRouteDestNetMask = _StnUserIpRouteDestNetMask_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 12, 1, 3),
    _StnUserIpRouteDestNetMask_Type()
)
stnUserIpRouteDestNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserIpRouteDestNetMask.setStatus("current")
_StnUserIpRouteDestGateway_Type = IpAddress
_StnUserIpRouteDestGateway_Object = MibTableColumn
stnUserIpRouteDestGateway = _StnUserIpRouteDestGateway_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 12, 1, 4),
    _StnUserIpRouteDestGateway_Type()
)
stnUserIpRouteDestGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserIpRouteDestGateway.setStatus("current")


class _StnUserIpRouteMetric_Type(Integer32):
    """Custom type stnUserIpRouteMetric based on Integer32"""
    defaultValue = 1


_StnUserIpRouteMetric_Object = MibTableColumn
stnUserIpRouteMetric = _StnUserIpRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 12, 1, 5),
    _StnUserIpRouteMetric_Type()
)
stnUserIpRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUserIpRouteMetric.setStatus("current")
_StnLDAPAuthorServerTable_Object = MibTable
stnLDAPAuthorServerTable = _StnLDAPAuthorServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 13)
)
if mibBuilder.loadTexts:
    stnLDAPAuthorServerTable.setStatus("current")
_StnLDAPAuthorServerEntry_Object = MibTableRow
stnLDAPAuthorServerEntry = _StnLDAPAuthorServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 13, 1)
)
stnLDAPAuthorServerEntry.setIndexNames(
    (0, "STN-AAA-MIB", "stnLDAPAuthorServerIndex"),
)
if mibBuilder.loadTexts:
    stnLDAPAuthorServerEntry.setStatus("current")
_StnLDAPAuthorServerIndex_Type = Integer32
_StnLDAPAuthorServerIndex_Object = MibTableColumn
stnLDAPAuthorServerIndex = _StnLDAPAuthorServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 13, 1, 1),
    _StnLDAPAuthorServerIndex_Type()
)
stnLDAPAuthorServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stnLDAPAuthorServerIndex.setStatus("current")
_StnLDAPAuthorServerAddress_Type = IpAddress
_StnLDAPAuthorServerAddress_Object = MibTableColumn
stnLDAPAuthorServerAddress = _StnLDAPAuthorServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 13, 1, 2),
    _StnLDAPAuthorServerAddress_Type()
)
stnLDAPAuthorServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLDAPAuthorServerAddress.setStatus("current")


class _StnLDAPAuthorClientServerPortNumber_Type(Integer32):
    """Custom type stnLDAPAuthorClientServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StnLDAPAuthorClientServerPortNumber_Type.__name__ = "Integer32"
_StnLDAPAuthorClientServerPortNumber_Object = MibTableColumn
stnLDAPAuthorClientServerPortNumber = _StnLDAPAuthorClientServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 13, 1, 3),
    _StnLDAPAuthorClientServerPortNumber_Type()
)
stnLDAPAuthorClientServerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLDAPAuthorClientServerPortNumber.setStatus("current")
_StnLDAPAuthorServerTimeout_Type = Integer32
_StnLDAPAuthorServerTimeout_Object = MibTableColumn
stnLDAPAuthorServerTimeout = _StnLDAPAuthorServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 13, 1, 4),
    _StnLDAPAuthorServerTimeout_Type()
)
stnLDAPAuthorServerTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLDAPAuthorServerTimeout.setStatus("current")
_StnLDAPAuthorConnectionEstablishTimeout_Type = Integer32
_StnLDAPAuthorConnectionEstablishTimeout_Object = MibTableColumn
stnLDAPAuthorConnectionEstablishTimeout = _StnLDAPAuthorConnectionEstablishTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 13, 1, 5),
    _StnLDAPAuthorConnectionEstablishTimeout_Type()
)
stnLDAPAuthorConnectionEstablishTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLDAPAuthorConnectionEstablishTimeout.setStatus("current")
_StnLDAPAuthorBindPassword_Type = OctetString
_StnLDAPAuthorBindPassword_Object = MibTableColumn
stnLDAPAuthorBindPassword = _StnLDAPAuthorBindPassword_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 13, 1, 6),
    _StnLDAPAuthorBindPassword_Type()
)
stnLDAPAuthorBindPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLDAPAuthorBindPassword.setStatus("current")
_StnLDAPAuthorRootDirectory_Type = DisplayString
_StnLDAPAuthorRootDirectory_Object = MibTableColumn
stnLDAPAuthorRootDirectory = _StnLDAPAuthorRootDirectory_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 13, 1, 7),
    _StnLDAPAuthorRootDirectory_Type()
)
stnLDAPAuthorRootDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLDAPAuthorRootDirectory.setStatus("current")
_StnLDAPAuthorServiceDirectoryName_Type = DisplayString
_StnLDAPAuthorServiceDirectoryName_Object = MibTableColumn
stnLDAPAuthorServiceDirectoryName = _StnLDAPAuthorServiceDirectoryName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 13, 1, 8),
    _StnLDAPAuthorServiceDirectoryName_Type()
)
stnLDAPAuthorServiceDirectoryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLDAPAuthorServiceDirectoryName.setStatus("current")
_StnLDAPAuthorBindOrganizationalUnit_Type = DisplayString
_StnLDAPAuthorBindOrganizationalUnit_Object = MibTableColumn
stnLDAPAuthorBindOrganizationalUnit = _StnLDAPAuthorBindOrganizationalUnit_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 13, 1, 9),
    _StnLDAPAuthorBindOrganizationalUnit_Type()
)
stnLDAPAuthorBindOrganizationalUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLDAPAuthorBindOrganizationalUnit.setStatus("current")
_StnLDAPAuthorBindUserId_Type = DisplayString
_StnLDAPAuthorBindUserId_Object = MibTableColumn
stnLDAPAuthorBindUserId = _StnLDAPAuthorBindUserId_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 13, 1, 10),
    _StnLDAPAuthorBindUserId_Type()
)
stnLDAPAuthorBindUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLDAPAuthorBindUserId.setStatus("current")


class _StnLDAPAuthorServerName_Type(DisplayString):
    """Custom type stnLDAPAuthorServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StnLDAPAuthorServerName_Type.__name__ = "DisplayString"
_StnLDAPAuthorServerName_Object = MibTableColumn
stnLDAPAuthorServerName = _StnLDAPAuthorServerName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 13, 1, 11),
    _StnLDAPAuthorServerName_Type()
)
stnLDAPAuthorServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLDAPAuthorServerName.setStatus("current")
_StnLDAPAuthorServerConfigInstance_Type = Integer32
_StnLDAPAuthorServerConfigInstance_Object = MibTableColumn
stnLDAPAuthorServerConfigInstance = _StnLDAPAuthorServerConfigInstance_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 13, 1, 12),
    _StnLDAPAuthorServerConfigInstance_Type()
)
stnLDAPAuthorServerConfigInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLDAPAuthorServerConfigInstance.setStatus("current")
_StnRealmTable_Object = MibTable
stnRealmTable = _StnRealmTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 14)
)
if mibBuilder.loadTexts:
    stnRealmTable.setStatus("current")
_StnRealmEntry_Object = MibTableRow
stnRealmEntry = _StnRealmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 14, 1)
)
stnRealmEntry.setIndexNames(
    (0, "STN-AAA-MIB", "stnRealmIndex"),
)
if mibBuilder.loadTexts:
    stnRealmEntry.setStatus("current")
_StnRealmIndex_Type = Integer32
_StnRealmIndex_Object = MibTableColumn
stnRealmIndex = _StnRealmIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 14, 1, 1),
    _StnRealmIndex_Type()
)
stnRealmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRealmIndex.setStatus("current")


class _StnRealmName_Type(DisplayString):
    """Custom type stnRealmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StnRealmName_Type.__name__ = "DisplayString"
_StnRealmName_Object = MibTableColumn
stnRealmName = _StnRealmName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 14, 1, 2),
    _StnRealmName_Type()
)
stnRealmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRealmName.setStatus("current")
_StnRealmAddrPoolInstance_Type = Integer32
_StnRealmAddrPoolInstance_Object = MibTableColumn
stnRealmAddrPoolInstance = _StnRealmAddrPoolInstance_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 14, 1, 3),
    _StnRealmAddrPoolInstance_Type()
)
stnRealmAddrPoolInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRealmAddrPoolInstance.setStatus("current")
_StnRealmForcedNextHop_Type = IpAddress
_StnRealmForcedNextHop_Object = MibTableColumn
stnRealmForcedNextHop = _StnRealmForcedNextHop_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 14, 1, 4),
    _StnRealmForcedNextHop_Type()
)
stnRealmForcedNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRealmForcedNextHop.setStatus("current")
_StnRealmRADIUSAuthenTable_Object = MibTable
stnRealmRADIUSAuthenTable = _StnRealmRADIUSAuthenTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 15)
)
if mibBuilder.loadTexts:
    stnRealmRADIUSAuthenTable.setStatus("current")
_StnRealmRADIUSAuthenEntry_Object = MibTableRow
stnRealmRADIUSAuthenEntry = _StnRealmRADIUSAuthenEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 15, 1)
)
stnRealmRADIUSAuthenEntry.setIndexNames(
    (0, "STN-AAA-MIB", "stnRealmIndex"),
    (0, "STN-AAA-MIB", "stnRealmRADIUSAuthenServerIndex"),
)
if mibBuilder.loadTexts:
    stnRealmRADIUSAuthenEntry.setStatus("current")
_StnRealmRADIUSAuthenServerIndex_Type = Integer32
_StnRealmRADIUSAuthenServerIndex_Object = MibTableColumn
stnRealmRADIUSAuthenServerIndex = _StnRealmRADIUSAuthenServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 15, 1, 1),
    _StnRealmRADIUSAuthenServerIndex_Type()
)
stnRealmRADIUSAuthenServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRealmRADIUSAuthenServerIndex.setStatus("current")
_StnRealmRADIUSAuthenServerInstance_Type = Integer32
_StnRealmRADIUSAuthenServerInstance_Object = MibTableColumn
stnRealmRADIUSAuthenServerInstance = _StnRealmRADIUSAuthenServerInstance_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 15, 1, 2),
    _StnRealmRADIUSAuthenServerInstance_Type()
)
stnRealmRADIUSAuthenServerInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRealmRADIUSAuthenServerInstance.setStatus("current")
_StnRealmRADIUSAuthenServerAddress_Type = IpAddress
_StnRealmRADIUSAuthenServerAddress_Object = MibTableColumn
stnRealmRADIUSAuthenServerAddress = _StnRealmRADIUSAuthenServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 15, 1, 3),
    _StnRealmRADIUSAuthenServerAddress_Type()
)
stnRealmRADIUSAuthenServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRealmRADIUSAuthenServerAddress.setStatus("current")
_StnRealmRADIUSAuthenServerDestPort_Type = Integer32
_StnRealmRADIUSAuthenServerDestPort_Object = MibTableColumn
stnRealmRADIUSAuthenServerDestPort = _StnRealmRADIUSAuthenServerDestPort_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 15, 1, 4),
    _StnRealmRADIUSAuthenServerDestPort_Type()
)
stnRealmRADIUSAuthenServerDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRealmRADIUSAuthenServerDestPort.setStatus("current")


class _StnRealmRADIUSAuthenServerRetrans_Type(Integer32):
    """Custom type stnRealmRADIUSAuthenServerRetrans based on Integer32"""
    defaultValue = 6


_StnRealmRADIUSAuthenServerRetrans_Object = MibTableColumn
stnRealmRADIUSAuthenServerRetrans = _StnRealmRADIUSAuthenServerRetrans_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 15, 1, 5),
    _StnRealmRADIUSAuthenServerRetrans_Type()
)
stnRealmRADIUSAuthenServerRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRealmRADIUSAuthenServerRetrans.setStatus("current")


class _StnRealmRADIUSAuthenServerTimeOut_Type(Integer32):
    """Custom type stnRealmRADIUSAuthenServerTimeOut based on Integer32"""
    defaultValue = 5


_StnRealmRADIUSAuthenServerTimeOut_Object = MibTableColumn
stnRealmRADIUSAuthenServerTimeOut = _StnRealmRADIUSAuthenServerTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 15, 1, 6),
    _StnRealmRADIUSAuthenServerTimeOut_Type()
)
stnRealmRADIUSAuthenServerTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRealmRADIUSAuthenServerTimeOut.setStatus("current")


class _StnRealmRADIUSAuthenServerSecret_Type(OctetString):
    """Custom type stnRealmRADIUSAuthenServerSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StnRealmRADIUSAuthenServerSecret_Type.__name__ = "OctetString"
_StnRealmRADIUSAuthenServerSecret_Object = MibTableColumn
stnRealmRADIUSAuthenServerSecret = _StnRealmRADIUSAuthenServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 15, 1, 7),
    _StnRealmRADIUSAuthenServerSecret_Type()
)
stnRealmRADIUSAuthenServerSecret.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stnRealmRADIUSAuthenServerSecret.setStatus("current")


class _StnRealmRADIUSAuthenServerName_Type(DisplayString):
    """Custom type stnRealmRADIUSAuthenServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StnRealmRADIUSAuthenServerName_Type.__name__ = "DisplayString"
_StnRealmRADIUSAuthenServerName_Object = MibTableColumn
stnRealmRADIUSAuthenServerName = _StnRealmRADIUSAuthenServerName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 15, 1, 8),
    _StnRealmRADIUSAuthenServerName_Type()
)
stnRealmRADIUSAuthenServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRealmRADIUSAuthenServerName.setStatus("current")
_StnNamedAddressPoolTable_Object = MibTable
stnNamedAddressPoolTable = _StnNamedAddressPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 16)
)
if mibBuilder.loadTexts:
    stnNamedAddressPoolTable.setStatus("current")
_StnNamedAddressPoolEntry_Object = MibTableRow
stnNamedAddressPoolEntry = _StnNamedAddressPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 16, 1)
)
stnNamedAddressPoolEntry.setIndexNames(
    (0, "STN-AAA-MIB", "stnNamedAddressPoolIndex"),
)
if mibBuilder.loadTexts:
    stnNamedAddressPoolEntry.setStatus("current")
_StnNamedAddressPoolIndex_Type = Integer32
_StnNamedAddressPoolIndex_Object = MibTableColumn
stnNamedAddressPoolIndex = _StnNamedAddressPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 16, 1, 1),
    _StnNamedAddressPoolIndex_Type()
)
stnNamedAddressPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNamedAddressPoolIndex.setStatus("current")


class _StnNamedAddressPoolName_Type(DisplayString):
    """Custom type stnNamedAddressPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StnNamedAddressPoolName_Type.__name__ = "DisplayString"
_StnNamedAddressPoolName_Object = MibTableColumn
stnNamedAddressPoolName = _StnNamedAddressPoolName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 16, 1, 2),
    _StnNamedAddressPoolName_Type()
)
stnNamedAddressPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNamedAddressPoolName.setStatus("current")
_StnNamedAddressPoolRangeTable_Object = MibTable
stnNamedAddressPoolRangeTable = _StnNamedAddressPoolRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 17)
)
if mibBuilder.loadTexts:
    stnNamedAddressPoolRangeTable.setStatus("current")
_StnNamedAddressPoolRangeEntry_Object = MibTableRow
stnNamedAddressPoolRangeEntry = _StnNamedAddressPoolRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 17, 1)
)
stnNamedAddressPoolRangeEntry.setIndexNames(
    (0, "STN-AAA-MIB", "stnNamedAddressPoolIndex"),
    (0, "STN-AAA-MIB", "stnNamedAddressPoolRangeIndex"),
)
if mibBuilder.loadTexts:
    stnNamedAddressPoolRangeEntry.setStatus("current")
_StnNamedAddressPoolRangeIndex_Type = Integer32
_StnNamedAddressPoolRangeIndex_Object = MibTableColumn
stnNamedAddressPoolRangeIndex = _StnNamedAddressPoolRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 17, 1, 1),
    _StnNamedAddressPoolRangeIndex_Type()
)
stnNamedAddressPoolRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNamedAddressPoolRangeIndex.setStatus("current")
_StnNamedAddressPoolStartIpAddress_Type = IpAddress
_StnNamedAddressPoolStartIpAddress_Object = MibTableColumn
stnNamedAddressPoolStartIpAddress = _StnNamedAddressPoolStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 17, 1, 2),
    _StnNamedAddressPoolStartIpAddress_Type()
)
stnNamedAddressPoolStartIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNamedAddressPoolStartIpAddress.setStatus("current")
_StnNamedAddressPoolEndIpAddress_Type = IpAddress
_StnNamedAddressPoolEndIpAddress_Object = MibTableColumn
stnNamedAddressPoolEndIpAddress = _StnNamedAddressPoolEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 1, 17, 1, 3),
    _StnNamedAddressPoolEndIpAddress_Type()
)
stnNamedAddressPoolEndIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNamedAddressPoolEndIpAddress.setStatus("current")
_StnAAAStats_ObjectIdentity = ObjectIdentity
stnAAAStats = _StnAAAStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 1, 2)
)
_StnAAAMibConformance_ObjectIdentity = ObjectIdentity
stnAAAMibConformance = _StnAAAMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 2)
)
_StnAAATrapVars_ObjectIdentity = ObjectIdentity
stnAAATrapVars = _StnAAATrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 3)
)
_StnNotificationRadiusAuthServerIndex_Type = Integer32
_StnNotificationRadiusAuthServerIndex_Object = MibScalar
stnNotificationRadiusAuthServerIndex = _StnNotificationRadiusAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 3, 1),
    _StnNotificationRadiusAuthServerIndex_Type()
)
stnNotificationRadiusAuthServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNotificationRadiusAuthServerIndex.setStatus("current")
_StnNotificationRadiusAccServerIndex_Type = Integer32
_StnNotificationRadiusAccServerIndex_Object = MibScalar
stnNotificationRadiusAccServerIndex = _StnNotificationRadiusAccServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 10, 3, 2),
    _StnNotificationRadiusAccServerIndex_Type()
)
stnNotificationRadiusAccServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNotificationRadiusAccServerIndex.setStatus("current")

# Managed Objects groups


# Notification objects

stnMaxUserSessionLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 20)
)
stnMaxUserSessionLimitExceeded.setObjects(
      *(("STN-CHASSIS-MIB", "stnEngineIndex"),
        ("STN-CHASSIS-MIB", "stnEngineSlot"),
        ("STN-CHASSIS-MIB", "stnEngineCpu"))
)
if mibBuilder.loadTexts:
    stnMaxUserSessionLimitExceeded.setStatus(
        "current"
    )

stnRadiusAuthenMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 21)
)
stnRadiusAuthenMismatch.setObjects(
      *(("STN-AAA-MIB", "stnNotificationRadiusAuthServerIndex"),
        ("STN-AAA-MIB", "stnRadiusAuthServerName"),
        ("STN-AAA-MIB", "stnRadiusAuthServerConfigInstance"),
        ("STN-ROUTER-MIB", "stnRouterIndex"))
)
if mibBuilder.loadTexts:
    stnRadiusAuthenMismatch.setStatus(
        "current"
    )

stnPrimaryBillingServerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 22)
)
stnPrimaryBillingServerFailure.setObjects(
      *(("STN-AAA-MIB", "stnNotificationRadiusAccServerIndex"),
        ("STN-AAA-MIB", "stnRadiusAccServerName"),
        ("STN-AAA-MIB", "stnRadiusAccServerConfigInstance"),
        ("STN-ROUTER-MIB", "stnRouterIndex"))
)
if mibBuilder.loadTexts:
    stnPrimaryBillingServerFailure.setStatus(
        "current"
    )

stnNoAddressesAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 23)
)
stnNoAddressesAvailable.setObjects(
    ("STN-ROUTER-MIB", "stnRouterIndex")
)
if mibBuilder.loadTexts:
    stnNoAddressesAvailable.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STN-AAA-MIB",
    **{"stnAAA": stnAAA,
       "stnAAAObjects": stnAAAObjects,
       "stnAAAConfig": stnAAAConfig,
       "stnStackingRuleGroup": stnStackingRuleGroup,
       "stnStackingRuleProtocol": stnStackingRuleProtocol,
       "stnStackingRuleTunnelType": stnStackingRuleTunnelType,
       "stnStackingRuleTunnelEndPoint": stnStackingRuleTunnelEndPoint,
       "stnEndPointTable": stnEndPointTable,
       "stnEndPointEntry": stnEndPointEntry,
       "stnEndPointIndex": stnEndPointIndex,
       "stnEndPointIpAddress": stnEndPointIpAddress,
       "stnEndPointName": stnEndPointName,
       "stnEndPointPassword": stnEndPointPassword,
       "stnAddressPoolTable": stnAddressPoolTable,
       "stnAddressPoolEntry": stnAddressPoolEntry,
       "stnAddressPoolIndex": stnAddressPoolIndex,
       "stnStartIpAddress": stnStartIpAddress,
       "stnEndIpAddress": stnEndIpAddress,
       "stnNetworkAccessGroup": stnNetworkAccessGroup,
       "stnNetworkAccessUserAuthenType": stnNetworkAccessUserAuthenType,
       "stnNetworkAccessEndPointAuthenType": stnNetworkAccessEndPointAuthenType,
       "stnNetworkAccessUserAccType": stnNetworkAccessUserAccType,
       "stnNetworkAccessEndPointAccType": stnNetworkAccessEndPointAccType,
       "stnNetworkAccessDomainName": stnNetworkAccessDomainName,
       "stnNetworkAccessServiceNameRadiusAttrType": stnNetworkAccessServiceNameRadiusAttrType,
       "stnNetworkAccessLdapAuthorizationUpdateTime": stnNetworkAccessLdapAuthorizationUpdateTime,
       "stnNetworkAccessLdapUpdateNotification": stnNetworkAccessLdapUpdateNotification,
       "stnNetworkAccessRealmAttrType": stnNetworkAccessRealmAttrType,
       "stnRadiusAccServerTable": stnRadiusAccServerTable,
       "stnRadiusAccServerEntry": stnRadiusAccServerEntry,
       "stnRadiusAccServerIndex": stnRadiusAccServerIndex,
       "stnRadiusAccServerAddress": stnRadiusAccServerAddress,
       "stnRadiusAccServerDestPort": stnRadiusAccServerDestPort,
       "stnRadiusAccServerRetrans": stnRadiusAccServerRetrans,
       "stnRadiusAccServerTimeOut": stnRadiusAccServerTimeOut,
       "stnRadiusAccServerSecret": stnRadiusAccServerSecret,
       "stnRadiusAccServerName": stnRadiusAccServerName,
       "stnRadiusAccServerConfigInstance": stnRadiusAccServerConfigInstance,
       "stnRadiusAuthServerTable": stnRadiusAuthServerTable,
       "stnRadiusAuthServerEntry": stnRadiusAuthServerEntry,
       "stnRadiusAuthServerIndex": stnRadiusAuthServerIndex,
       "stnRadiusAuthServerAddress": stnRadiusAuthServerAddress,
       "stnRadiusAuthServerDestPort": stnRadiusAuthServerDestPort,
       "stnRadiusAuthServerRetrans": stnRadiusAuthServerRetrans,
       "stnRadiusAuthServerTimeOut": stnRadiusAuthServerTimeOut,
       "stnRadiusAuthServerSecret": stnRadiusAuthServerSecret,
       "stnRadiusAuthServerName": stnRadiusAuthServerName,
       "stnRadiusAuthServerConfigInstance": stnRadiusAuthServerConfigInstance,
       "stnUserTable": stnUserTable,
       "stnUserEntry": stnUserEntry,
       "stnUserIndex": stnUserIndex,
       "stnUserName": stnUserName,
       "stnUserPassword": stnUserPassword,
       "stnUserIpAddress": stnUserIpAddress,
       "stnUserIpNetMask": stnUserIpNetMask,
       "stnUserIpRouting": stnUserIpRouting,
       "stnUserMTU": stnUserMTU,
       "stnUserIpCompression": stnUserIpCompression,
       "stnUserTimeOut": stnUserTimeOut,
       "stnUserIdleTime": stnUserIdleTime,
       "stnUserTunnelType": stnUserTunnelType,
       "stnUserTunnelServerEndPoint": stnUserTunnelServerEndPoint,
       "stnUserTunnelClientEndPoint": stnUserTunnelClientEndPoint,
       "stnUserAssignedTunnelName": stnUserAssignedTunnelName,
       "stnUserTunnelPassword": stnUserTunnelPassword,
       "stnUserServiceType": stnUserServiceType,
       "stnUserIpFilters": stnUserIpFilters,
       "stnUserIpRoutes": stnUserIpRoutes,
       "stnUserPrimaryDNSServer": stnUserPrimaryDNSServer,
       "stnUserSecondaryDNSServer": stnUserSecondaryDNSServer,
       "stnUserPrimaryNBNSServer": stnUserPrimaryNBNSServer,
       "stnUserSecondaryNBNSServer": stnUserSecondaryNBNSServer,
       "stnUserServiceName": stnUserServiceName,
       "stnUserPhysicalPort": stnUserPhysicalPort,
       "stnUserPhysicalSlot": stnUserPhysicalSlot,
       "stnUserVirtualPathId": stnUserVirtualPathId,
       "stnUserVirtualCircuitId": stnUserVirtualCircuitId,
       "stnUserRealmInstance": stnUserRealmInstance,
       "stnDefaultPppUserGroup": stnDefaultPppUserGroup,
       "stnDefaultUserIpAddress": stnDefaultUserIpAddress,
       "stnDefaultUserIpNetMask": stnDefaultUserIpNetMask,
       "stnDefaultUserIpRouting": stnDefaultUserIpRouting,
       "stnDefaultUserMTU": stnDefaultUserMTU,
       "stnDefaultUserIpCompression": stnDefaultUserIpCompression,
       "stnDefaultUserTimeOut": stnDefaultUserTimeOut,
       "stnDefaultUserIdleTime": stnDefaultUserIdleTime,
       "stnDefaultUserTunnelType": stnDefaultUserTunnelType,
       "stnDefaultUserTunnelServerEndPoint": stnDefaultUserTunnelServerEndPoint,
       "stnDefaultUserTunnelClientEndPoint": stnDefaultUserTunnelClientEndPoint,
       "stnDefaultUserIpFilters": stnDefaultUserIpFilters,
       "stnDefaultUserIpRoutes": stnDefaultUserIpRoutes,
       "stnDefaultUserPrimaryDNSServer": stnDefaultUserPrimaryDNSServer,
       "stnDefaultUserSecondaryDNSServer": stnDefaultUserSecondaryDNSServer,
       "stnDefaultUserPrimaryNBNSServer": stnDefaultUserPrimaryNBNSServer,
       "stnDefaultUserSecondaryNBNSServer": stnDefaultUserSecondaryNBNSServer,
       "stnDefaultUserServiceName": stnDefaultUserServiceName,
       "stnNoAuthPppUserGroup": stnNoAuthPppUserGroup,
       "stnNoAuthPppUserName": stnNoAuthPppUserName,
       "stnNoAuthPppUserPassword": stnNoAuthPppUserPassword,
       "stnUserIpFilterTable": stnUserIpFilterTable,
       "stnUserIpFilterEntry": stnUserIpFilterEntry,
       "stnUserIpFilterIndex": stnUserIpFilterIndex,
       "stnUserIpFilterName": stnUserIpFilterName,
       "stnUserIpFilterRules": stnUserIpFilterRules,
       "stnUserIpFilterRuleTable": stnUserIpFilterRuleTable,
       "stnUserIpFilterRuleEntry": stnUserIpFilterRuleEntry,
       "stnUserIpFilterRuleIndex": stnUserIpFilterRuleIndex,
       "stnUserIpFilterRuleSrcAddress": stnUserIpFilterRuleSrcAddress,
       "stnUserIpFilterRuleSrcNetMask": stnUserIpFilterRuleSrcNetMask,
       "stnUserIpFilterRuleSrcPort": stnUserIpFilterRuleSrcPort,
       "stnUserIpFilterRuleDestAddress": stnUserIpFilterRuleDestAddress,
       "stnUserIpFilterRuleDestNetMask": stnUserIpFilterRuleDestNetMask,
       "stnUserIpFilterRuleDestPort": stnUserIpFilterRuleDestPort,
       "stnUserIpFilterRuleProtocol": stnUserIpFilterRuleProtocol,
       "stnUserIpFilterRuleAction": stnUserIpFilterRuleAction,
       "stnUserIpFilterRuleEndPoint": stnUserIpFilterRuleEndPoint,
       "stnUserIpRouteTable": stnUserIpRouteTable,
       "stnUserIpRouteEntry": stnUserIpRouteEntry,
       "stnUserIpRouteIndex": stnUserIpRouteIndex,
       "stnUserIpRouteDestAddress": stnUserIpRouteDestAddress,
       "stnUserIpRouteDestNetMask": stnUserIpRouteDestNetMask,
       "stnUserIpRouteDestGateway": stnUserIpRouteDestGateway,
       "stnUserIpRouteMetric": stnUserIpRouteMetric,
       "stnLDAPAuthorServerTable": stnLDAPAuthorServerTable,
       "stnLDAPAuthorServerEntry": stnLDAPAuthorServerEntry,
       "stnLDAPAuthorServerIndex": stnLDAPAuthorServerIndex,
       "stnLDAPAuthorServerAddress": stnLDAPAuthorServerAddress,
       "stnLDAPAuthorClientServerPortNumber": stnLDAPAuthorClientServerPortNumber,
       "stnLDAPAuthorServerTimeout": stnLDAPAuthorServerTimeout,
       "stnLDAPAuthorConnectionEstablishTimeout": stnLDAPAuthorConnectionEstablishTimeout,
       "stnLDAPAuthorBindPassword": stnLDAPAuthorBindPassword,
       "stnLDAPAuthorRootDirectory": stnLDAPAuthorRootDirectory,
       "stnLDAPAuthorServiceDirectoryName": stnLDAPAuthorServiceDirectoryName,
       "stnLDAPAuthorBindOrganizationalUnit": stnLDAPAuthorBindOrganizationalUnit,
       "stnLDAPAuthorBindUserId": stnLDAPAuthorBindUserId,
       "stnLDAPAuthorServerName": stnLDAPAuthorServerName,
       "stnLDAPAuthorServerConfigInstance": stnLDAPAuthorServerConfigInstance,
       "stnRealmTable": stnRealmTable,
       "stnRealmEntry": stnRealmEntry,
       "stnRealmIndex": stnRealmIndex,
       "stnRealmName": stnRealmName,
       "stnRealmAddrPoolInstance": stnRealmAddrPoolInstance,
       "stnRealmForcedNextHop": stnRealmForcedNextHop,
       "stnRealmRADIUSAuthenTable": stnRealmRADIUSAuthenTable,
       "stnRealmRADIUSAuthenEntry": stnRealmRADIUSAuthenEntry,
       "stnRealmRADIUSAuthenServerIndex": stnRealmRADIUSAuthenServerIndex,
       "stnRealmRADIUSAuthenServerInstance": stnRealmRADIUSAuthenServerInstance,
       "stnRealmRADIUSAuthenServerAddress": stnRealmRADIUSAuthenServerAddress,
       "stnRealmRADIUSAuthenServerDestPort": stnRealmRADIUSAuthenServerDestPort,
       "stnRealmRADIUSAuthenServerRetrans": stnRealmRADIUSAuthenServerRetrans,
       "stnRealmRADIUSAuthenServerTimeOut": stnRealmRADIUSAuthenServerTimeOut,
       "stnRealmRADIUSAuthenServerSecret": stnRealmRADIUSAuthenServerSecret,
       "stnRealmRADIUSAuthenServerName": stnRealmRADIUSAuthenServerName,
       "stnNamedAddressPoolTable": stnNamedAddressPoolTable,
       "stnNamedAddressPoolEntry": stnNamedAddressPoolEntry,
       "stnNamedAddressPoolIndex": stnNamedAddressPoolIndex,
       "stnNamedAddressPoolName": stnNamedAddressPoolName,
       "stnNamedAddressPoolRangeTable": stnNamedAddressPoolRangeTable,
       "stnNamedAddressPoolRangeEntry": stnNamedAddressPoolRangeEntry,
       "stnNamedAddressPoolRangeIndex": stnNamedAddressPoolRangeIndex,
       "stnNamedAddressPoolStartIpAddress": stnNamedAddressPoolStartIpAddress,
       "stnNamedAddressPoolEndIpAddress": stnNamedAddressPoolEndIpAddress,
       "stnAAAStats": stnAAAStats,
       "stnAAAMibConformance": stnAAAMibConformance,
       "stnAAATrapVars": stnAAATrapVars,
       "stnNotificationRadiusAuthServerIndex": stnNotificationRadiusAuthServerIndex,
       "stnNotificationRadiusAccServerIndex": stnNotificationRadiusAccServerIndex,
       "stnMaxUserSessionLimitExceeded": stnMaxUserSessionLimitExceeded,
       "stnRadiusAuthenMismatch": stnRadiusAuthenMismatch,
       "stnPrimaryBillingServerFailure": stnPrimaryBillingServerFailure,
       "stnNoAddressesAvailable": stnNoAddressesAvailable}
)
