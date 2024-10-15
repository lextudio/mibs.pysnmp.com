# SNMP MIB module (HP-USER-AUTH) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-USER-AUTH
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:10 2024
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

(HpAutzUserRoleName,) = mibBuilder.importSymbols(
    "HP-AUTZ-MIB",
    "HpAutzUserRoleName")

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfUsrAuthMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19)
)
hpicfUsrAuthMIB.setRevisions(
        ("2017-10-12 00:00",
         "2017-09-13 00:00",
         "2017-06-29 00:00",
         "2016-11-11 00:00",
         "2016-07-27 00:00",
         "2016-02-18 00:00",
         "2016-02-13 00:00",
         "2016-01-15 22:07",
         "2015-09-11 04:13",
         "2013-06-12 00:00",
         "2013-02-25 00:00",
         "2012-05-28 00:00",
         "2011-08-29 00:00",
         "2011-07-21 00:00",
         "2010-01-28 00:00",
         "2009-12-15 00:00",
         "2009-07-08 00:00",
         "2009-03-09 00:00",
         "2008-08-06 12:00",
         "2007-08-29 00:00",
         "2007-06-22 12:00",
         "2005-08-05 00:00",
         "2003-05-23 10:20")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfUsrAuthNotifications_ObjectIdentity = ObjectIdentity
hpicfUsrAuthNotifications = _HpicfUsrAuthNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 0)
)
_HpicfUsrAuthSystem_ObjectIdentity = ObjectIdentity
hpicfUsrAuthSystem = _HpicfUsrAuthSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1)
)
_HpicfUsrAuthWebAuthDhcpBaseAddress_Type = IpAddress
_HpicfUsrAuthWebAuthDhcpBaseAddress_Object = MibScalar
hpicfUsrAuthWebAuthDhcpBaseAddress = _HpicfUsrAuthWebAuthDhcpBaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 1),
    _HpicfUsrAuthWebAuthDhcpBaseAddress_Type()
)
hpicfUsrAuthWebAuthDhcpBaseAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthDhcpBaseAddress.setStatus("current")
_HpicfUsrAuthWebAuthDhcpMask_Type = IpAddress
_HpicfUsrAuthWebAuthDhcpMask_Object = MibScalar
hpicfUsrAuthWebAuthDhcpMask = _HpicfUsrAuthWebAuthDhcpMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 2),
    _HpicfUsrAuthWebAuthDhcpMask_Type()
)
hpicfUsrAuthWebAuthDhcpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthDhcpMask.setStatus("current")


class _HpicfUsrAuthWebAuthDhcpLease_Type(Integer32):
    """Custom type hpicfUsrAuthWebAuthDhcpLease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_HpicfUsrAuthWebAuthDhcpLease_Type.__name__ = "Integer32"
_HpicfUsrAuthWebAuthDhcpLease_Object = MibScalar
hpicfUsrAuthWebAuthDhcpLease = _HpicfUsrAuthWebAuthDhcpLease_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 3),
    _HpicfUsrAuthWebAuthDhcpLease_Type()
)
hpicfUsrAuthWebAuthDhcpLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthDhcpLease.setStatus("current")


class _HpicfUsrAuthMacAuthAddrFormat_Type(Integer32):
    """Custom type hpicfUsrAuthMacAuthAddrFormat based on Integer32"""
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
        *(("multiColon", 4),
          ("multiColonUppercase", 8),
          ("multiDash", 3),
          ("multiDashUppercase", 7),
          ("noDelimiter", 1),
          ("noDelimiterUppercase", 5),
          ("singleDash", 2),
          ("singleDashUppercase", 6))
    )


_HpicfUsrAuthMacAuthAddrFormat_Type.__name__ = "Integer32"
_HpicfUsrAuthMacAuthAddrFormat_Object = MibScalar
hpicfUsrAuthMacAuthAddrFormat = _HpicfUsrAuthMacAuthAddrFormat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 4),
    _HpicfUsrAuthMacAuthAddrFormat_Type()
)
hpicfUsrAuthMacAuthAddrFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthAddrFormat.setStatus("current")


class _HpicfUsrAuthCliNotifyEnable_Type(Integer32):
    """Custom type hpicfUsrAuthCliNotifyEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfUsrAuthCliNotifyEnable_Type.__name__ = "Integer32"
_HpicfUsrAuthCliNotifyEnable_Object = MibScalar
hpicfUsrAuthCliNotifyEnable = _HpicfUsrAuthCliNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 5),
    _HpicfUsrAuthCliNotifyEnable_Type()
)
hpicfUsrAuthCliNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthCliNotifyEnable.setStatus("current")


class _HpicfUsrAuthCLIInterface_Type(Integer32):
    """Custom type hpicfUsrAuthCLIInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              9)
        )
    )
    namedValues = NamedValues(
        *(("other", 9),
          ("portAccess", 6),
          ("serial", 1),
          ("ssh", 3),
          ("sshPublicKey", 4),
          ("telnet", 2),
          ("webui", 5))
    )


_HpicfUsrAuthCLIInterface_Type.__name__ = "Integer32"
_HpicfUsrAuthCLIInterface_Object = MibScalar
hpicfUsrAuthCLIInterface = _HpicfUsrAuthCLIInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 6),
    _HpicfUsrAuthCLIInterface_Type()
)
hpicfUsrAuthCLIInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfUsrAuthCLIInterface.setStatus("current")
_HpicfUsrAuthCLIPasswdSet_Type = TruthValue
_HpicfUsrAuthCLIPasswdSet_Object = MibScalar
hpicfUsrAuthCLIPasswdSet = _HpicfUsrAuthCLIPasswdSet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 7),
    _HpicfUsrAuthCLIPasswdSet_Type()
)
hpicfUsrAuthCLIPasswdSet.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfUsrAuthCLIPasswdSet.setStatus("current")
_HpicfUsrAuthCLIFailCnt_Type = Integer32
_HpicfUsrAuthCLIFailCnt_Object = MibScalar
hpicfUsrAuthCLIFailCnt = _HpicfUsrAuthCLIFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 8),
    _HpicfUsrAuthCLIFailCnt_Type()
)
hpicfUsrAuthCLIFailCnt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfUsrAuthCLIFailCnt.setStatus("current")
_HpicfUsrAuthCLIPwdNotifyCnt_Type = Unsigned32
_HpicfUsrAuthCLIPwdNotifyCnt_Object = MibScalar
hpicfUsrAuthCLIPwdNotifyCnt = _HpicfUsrAuthCLIPwdNotifyCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 9),
    _HpicfUsrAuthCLIPwdNotifyCnt_Type()
)
hpicfUsrAuthCLIPwdNotifyCnt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfUsrAuthCLIPwdNotifyCnt.setStatus("current")
_HpicfUsrAuthWMAFailCnt_Type = Unsigned32
_HpicfUsrAuthWMAFailCnt_Object = MibScalar
hpicfUsrAuthWMAFailCnt = _HpicfUsrAuthWMAFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 10),
    _HpicfUsrAuthWMAFailCnt_Type()
)
hpicfUsrAuthWMAFailCnt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfUsrAuthWMAFailCnt.setStatus("current")
_HpicfUsrAuthWMAFailMAC_Type = MacAddress
_HpicfUsrAuthWMAFailMAC_Object = MibScalar
hpicfUsrAuthWMAFailMAC = _HpicfUsrAuthWMAFailMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 11),
    _HpicfUsrAuthWMAFailMAC_Type()
)
hpicfUsrAuthWMAFailMAC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfUsrAuthWMAFailMAC.setStatus("current")
_HpicfUsrAuthWMAFailPort_Type = Integer32
_HpicfUsrAuthWMAFailPort_Object = MibScalar
hpicfUsrAuthWMAFailPort = _HpicfUsrAuthWMAFailPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 12),
    _HpicfUsrAuthWMAFailPort_Type()
)
hpicfUsrAuthWMAFailPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfUsrAuthWMAFailPort.setStatus("current")
_HpicfUsrAuthWMAFailVlan_Type = Integer32
_HpicfUsrAuthWMAFailVlan_Object = MibScalar
hpicfUsrAuthWMAFailVlan = _HpicfUsrAuthWMAFailVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 13),
    _HpicfUsrAuthWMAFailVlan_Type()
)
hpicfUsrAuthWMAFailVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfUsrAuthWMAFailVlan.setStatus("current")


class _HpicfUsrAuthPortSecNotifyEnable_Type(Integer32):
    """Custom type hpicfUsrAuthPortSecNotifyEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfUsrAuthPortSecNotifyEnable_Type.__name__ = "Integer32"
_HpicfUsrAuthPortSecNotifyEnable_Object = MibScalar
hpicfUsrAuthPortSecNotifyEnable = _HpicfUsrAuthPortSecNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 14),
    _HpicfUsrAuthPortSecNotifyEnable_Type()
)
hpicfUsrAuthPortSecNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthPortSecNotifyEnable.setStatus("current")


class _HpicfUsrAuthPasswdNotifyEnable_Type(Integer32):
    """Custom type hpicfUsrAuthPasswdNotifyEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfUsrAuthPasswdNotifyEnable_Type.__name__ = "Integer32"
_HpicfUsrAuthPasswdNotifyEnable_Object = MibScalar
hpicfUsrAuthPasswdNotifyEnable = _HpicfUsrAuthPasswdNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 15),
    _HpicfUsrAuthPasswdNotifyEnable_Type()
)
hpicfUsrAuthPasswdNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthPasswdNotifyEnable.setStatus("current")
_HpicfUsrAuthWMAEWAServerTable_Object = MibTable
hpicfUsrAuthWMAEWAServerTable = _HpicfUsrAuthWMAEWAServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 16)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthWMAEWAServerTable.setStatus("current")
_HpicfUsrAuthWMAEWAServerEntry_Object = MibTableRow
hpicfUsrAuthWMAEWAServerEntry = _HpicfUsrAuthWMAEWAServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 16, 1)
)
hpicfUsrAuthWMAEWAServerEntry.setIndexNames(
    (0, "HP-USER-AUTH", "hpicfUsrAuthWMAeWAServerIndex"),
)
if mibBuilder.loadTexts:
    hpicfUsrAuthWMAEWAServerEntry.setStatus("current")
_HpicfUsrAuthWMAeWAServerIndex_Type = Integer32
_HpicfUsrAuthWMAeWAServerIndex_Object = MibTableColumn
hpicfUsrAuthWMAeWAServerIndex = _HpicfUsrAuthWMAeWAServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 16, 1, 1),
    _HpicfUsrAuthWMAeWAServerIndex_Type()
)
hpicfUsrAuthWMAeWAServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfUsrAuthWMAeWAServerIndex.setStatus("current")


class _HpicfUsrAuthWMAeWAServerIPAddressType_Type(InetAddressType):
    """Custom type hpicfUsrAuthWMAeWAServerIPAddressType based on InetAddressType"""


_HpicfUsrAuthWMAeWAServerIPAddressType_Object = MibTableColumn
hpicfUsrAuthWMAeWAServerIPAddressType = _HpicfUsrAuthWMAeWAServerIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 16, 1, 2),
    _HpicfUsrAuthWMAeWAServerIPAddressType_Type()
)
hpicfUsrAuthWMAeWAServerIPAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrAuthWMAeWAServerIPAddressType.setStatus("current")
_HpicfUsrAuthWMAeWAServerIPAddress_Type = InetAddress
_HpicfUsrAuthWMAeWAServerIPAddress_Object = MibTableColumn
hpicfUsrAuthWMAeWAServerIPAddress = _HpicfUsrAuthWMAeWAServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 16, 1, 3),
    _HpicfUsrAuthWMAeWAServerIPAddress_Type()
)
hpicfUsrAuthWMAeWAServerIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrAuthWMAeWAServerIPAddress.setStatus("current")
_HpicfUsrAuthWMAeWAServerPath_Type = OctetString
_HpicfUsrAuthWMAeWAServerPath_Object = MibTableColumn
hpicfUsrAuthWMAeWAServerPath = _HpicfUsrAuthWMAeWAServerPath_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 16, 1, 4),
    _HpicfUsrAuthWMAeWAServerPath_Type()
)
hpicfUsrAuthWMAeWAServerPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrAuthWMAeWAServerPath.setStatus("current")
_HpicfUsrAUthWMAeWAServerRowStatus_Type = RowStatus
_HpicfUsrAUthWMAeWAServerRowStatus_Object = MibTableColumn
hpicfUsrAUthWMAeWAServerRowStatus = _HpicfUsrAUthWMAeWAServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 16, 1, 5),
    _HpicfUsrAUthWMAeWAServerRowStatus_Type()
)
hpicfUsrAUthWMAeWAServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrAUthWMAeWAServerRowStatus.setStatus("current")
_HpicfUsrAuthRedirectServerTable_Object = MibTable
hpicfUsrAuthRedirectServerTable = _HpicfUsrAuthRedirectServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 17)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthRedirectServerTable.setStatus("current")
_HpicfUsrAuthRedirectServerEntry_Object = MibTableRow
hpicfUsrAuthRedirectServerEntry = _HpicfUsrAuthRedirectServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 17, 1)
)
hpicfUsrAuthRedirectServerEntry.setIndexNames(
    (0, "HP-USER-AUTH", "hpicfUsrAuthRedirectServerIndex"),
)
if mibBuilder.loadTexts:
    hpicfUsrAuthRedirectServerEntry.setStatus("current")
_HpicfUsrAuthRedirectServerIndex_Type = Integer32
_HpicfUsrAuthRedirectServerIndex_Object = MibTableColumn
hpicfUsrAuthRedirectServerIndex = _HpicfUsrAuthRedirectServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 17, 1, 1),
    _HpicfUsrAuthRedirectServerIndex_Type()
)
hpicfUsrAuthRedirectServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfUsrAuthRedirectServerIndex.setStatus("current")
_HpicfUsrAuthRedirectServerURL_Type = OctetString
_HpicfUsrAuthRedirectServerURL_Object = MibTableColumn
hpicfUsrAuthRedirectServerURL = _HpicfUsrAuthRedirectServerURL_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 17, 1, 2),
    _HpicfUsrAuthRedirectServerURL_Type()
)
hpicfUsrAuthRedirectServerURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrAuthRedirectServerURL.setStatus("current")
_HpicfUsrAuthRedirectServerRowStatus_Type = RowStatus
_HpicfUsrAuthRedirectServerRowStatus_Object = MibTableColumn
hpicfUsrAuthRedirectServerRowStatus = _HpicfUsrAuthRedirectServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 17, 1, 3),
    _HpicfUsrAuthRedirectServerRowStatus_Type()
)
hpicfUsrAuthRedirectServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrAuthRedirectServerRowStatus.setStatus("current")


class _HpicfUsrAuthRedirectServerRestrictiveFilter_Type(Integer32):
    """Custom type hpicfUsrAuthRedirectServerRestrictiveFilter based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfUsrAuthRedirectServerRestrictiveFilter_Type.__name__ = "Integer32"
_HpicfUsrAuthRedirectServerRestrictiveFilter_Object = MibScalar
hpicfUsrAuthRedirectServerRestrictiveFilter = _HpicfUsrAuthRedirectServerRestrictiveFilter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 18),
    _HpicfUsrAuthRedirectServerRestrictiveFilter_Type()
)
hpicfUsrAuthRedirectServerRestrictiveFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthRedirectServerRestrictiveFilter.setStatus("current")


class _HpicfUsrAuthRedirectServerClientTimeout_Type(Integer32):
    """Custom type hpicfUsrAuthRedirectServerClientTimeout based on Integer32"""
    defaultValue = 180


_HpicfUsrAuthRedirectServerClientTimeout_Object = MibScalar
hpicfUsrAuthRedirectServerClientTimeout = _HpicfUsrAuthRedirectServerClientTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 19),
    _HpicfUsrAuthRedirectServerClientTimeout_Type()
)
hpicfUsrAuthRedirectServerClientTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthRedirectServerClientTimeout.setStatus("current")
_HpicfUsrAuthRedirectServerAuthFailureStats_Type = Counter32
_HpicfUsrAuthRedirectServerAuthFailureStats_Object = MibScalar
hpicfUsrAuthRedirectServerAuthFailureStats = _HpicfUsrAuthRedirectServerAuthFailureStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 20),
    _HpicfUsrAuthRedirectServerAuthFailureStats_Type()
)
hpicfUsrAuthRedirectServerAuthFailureStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthRedirectServerAuthFailureStats.setStatus("current")


class _HpicfUsrAuthCacheCredTimeOut_Type(Integer32):
    """Custom type hpicfUsrAuthCacheCredTimeOut based on Integer32"""
    defaultValue = 600


_HpicfUsrAuthCacheCredTimeOut_Object = MibScalar
hpicfUsrAuthCacheCredTimeOut = _HpicfUsrAuthCacheCredTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 21),
    _HpicfUsrAuthCacheCredTimeOut_Type()
)
hpicfUsrAuthCacheCredTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthCacheCredTimeOut.setStatus("current")
_HpicfUsrAuthClientReauthenticateTable_Object = MibTable
hpicfUsrAuthClientReauthenticateTable = _HpicfUsrAuthClientReauthenticateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 22)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthClientReauthenticateTable.setStatus("current")
_HpicfUsrAuthClientReauthenticateEntry_Object = MibTableRow
hpicfUsrAuthClientReauthenticateEntry = _HpicfUsrAuthClientReauthenticateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 22, 1)
)
hpicfUsrAuthClientReauthenticateEntry.setIndexNames(
    (0, "HP-USER-AUTH", "hpicfUsrAuthClientReauthenticateInterfaceIndex"),
    (0, "HP-USER-AUTH", "hpicfUsrAuthClientReauthenticateMacAddress"),
)
if mibBuilder.loadTexts:
    hpicfUsrAuthClientReauthenticateEntry.setStatus("current")
_HpicfUsrAuthClientReauthenticateInterfaceIndex_Type = InterfaceIndex
_HpicfUsrAuthClientReauthenticateInterfaceIndex_Object = MibTableColumn
hpicfUsrAuthClientReauthenticateInterfaceIndex = _HpicfUsrAuthClientReauthenticateInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 22, 1, 1),
    _HpicfUsrAuthClientReauthenticateInterfaceIndex_Type()
)
hpicfUsrAuthClientReauthenticateInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfUsrAuthClientReauthenticateInterfaceIndex.setStatus("current")
_HpicfUsrAuthClientReauthenticateMacAddress_Type = MacAddress
_HpicfUsrAuthClientReauthenticateMacAddress_Object = MibTableColumn
hpicfUsrAuthClientReauthenticateMacAddress = _HpicfUsrAuthClientReauthenticateMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 22, 1, 2),
    _HpicfUsrAuthClientReauthenticateMacAddress_Type()
)
hpicfUsrAuthClientReauthenticateMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfUsrAuthClientReauthenticateMacAddress.setStatus("current")
_HpicfUsrAuthClientReauthenticate_Type = TruthValue
_HpicfUsrAuthClientReauthenticate_Object = MibTableColumn
hpicfUsrAuthClientReauthenticate = _HpicfUsrAuthClientReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 22, 1, 3),
    _HpicfUsrAuthClientReauthenticate_Type()
)
hpicfUsrAuthClientReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthClientReauthenticate.setStatus("current")
_HpicfUsrAuthMacAuthPassword_Type = OctetString
_HpicfUsrAuthMacAuthPassword_Object = MibScalar
hpicfUsrAuthMacAuthPassword = _HpicfUsrAuthMacAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 23),
    _HpicfUsrAuthMacAuthPassword_Type()
)
hpicfUsrAuthMacAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthPassword.setStatus("current")


class _HpicfUsrAuthWebAuthAccessDeniedMode_Type(Integer32):
    """Custom type hpicfUsrAuthWebAuthAccessDeniedMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("custom", 2),
          ("disabled", 1),
          ("radius", 3))
    )


_HpicfUsrAuthWebAuthAccessDeniedMode_Type.__name__ = "Integer32"
_HpicfUsrAuthWebAuthAccessDeniedMode_Object = MibScalar
hpicfUsrAuthWebAuthAccessDeniedMode = _HpicfUsrAuthWebAuthAccessDeniedMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 24),
    _HpicfUsrAuthWebAuthAccessDeniedMode_Type()
)
hpicfUsrAuthWebAuthAccessDeniedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthAccessDeniedMode.setStatus("current")


class _HpicfUsrAuthWebAuthAccessDeniedMessage_Type(OctetString):
    """Custom type hpicfUsrAuthWebAuthAccessDeniedMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_HpicfUsrAuthWebAuthAccessDeniedMessage_Type.__name__ = "OctetString"
_HpicfUsrAuthWebAuthAccessDeniedMessage_Object = MibScalar
hpicfUsrAuthWebAuthAccessDeniedMessage = _HpicfUsrAuthWebAuthAccessDeniedMessage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 25),
    _HpicfUsrAuthWebAuthAccessDeniedMessage_Type()
)
hpicfUsrAuthWebAuthAccessDeniedMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthAccessDeniedMessage.setStatus("current")
_HpicfUsrAuthMacAuthUsrNumberCnt_Type = Counter32
_HpicfUsrAuthMacAuthUsrNumberCnt_Object = MibScalar
hpicfUsrAuthMacAuthUsrNumberCnt = _HpicfUsrAuthMacAuthUsrNumberCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 26),
    _HpicfUsrAuthMacAuthUsrNumberCnt_Type()
)
hpicfUsrAuthMacAuthUsrNumberCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthUsrNumberCnt.setStatus("current")


class _HpicfUsrAuthLastLoginNotifyStatus_Type(Integer32):
    """Custom type hpicfUsrAuthLastLoginNotifyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("failedLockOut", 3),
          ("lockedOut", 4),
          ("successful", 1),
          ("tableFull", 5),
          ("unknown", 0))
    )


_HpicfUsrAuthLastLoginNotifyStatus_Type.__name__ = "Integer32"
_HpicfUsrAuthLastLoginNotifyStatus_Object = MibScalar
hpicfUsrAuthLastLoginNotifyStatus = _HpicfUsrAuthLastLoginNotifyStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 27),
    _HpicfUsrAuthLastLoginNotifyStatus_Type()
)
hpicfUsrAuthLastLoginNotifyStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfUsrAuthLastLoginNotifyStatus.setStatus("current")
_HpicfUsrAuthLastLoginNotifyAddrType_Type = InetAddressType
_HpicfUsrAuthLastLoginNotifyAddrType_Object = MibScalar
hpicfUsrAuthLastLoginNotifyAddrType = _HpicfUsrAuthLastLoginNotifyAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 28),
    _HpicfUsrAuthLastLoginNotifyAddrType_Type()
)
hpicfUsrAuthLastLoginNotifyAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfUsrAuthLastLoginNotifyAddrType.setStatus("current")
_HpicfUsrAuthLastLoginNotifyAddr_Type = InetAddress
_HpicfUsrAuthLastLoginNotifyAddr_Object = MibScalar
hpicfUsrAuthLastLoginNotifyAddr = _HpicfUsrAuthLastLoginNotifyAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 29),
    _HpicfUsrAuthLastLoginNotifyAddr_Type()
)
hpicfUsrAuthLastLoginNotifyAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfUsrAuthLastLoginNotifyAddr.setStatus("current")


class _HpicfUsrAuthUseLLDPData_Type(TruthValue):
    """Custom type hpicfUsrAuthUseLLDPData based on TruthValue"""


_HpicfUsrAuthUseLLDPData_Object = MibScalar
hpicfUsrAuthUseLLDPData = _HpicfUsrAuthUseLLDPData_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 30),
    _HpicfUsrAuthUseLLDPData_Type()
)
hpicfUsrAuthUseLLDPData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthUseLLDPData.setStatus("current")


class _HpicfUsrAuthMacAuthPasswordEncrypted_Type(OctetString):
    """Custom type hpicfUsrAuthMacAuthPasswordEncrypted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpicfUsrAuthMacAuthPasswordEncrypted_Type.__name__ = "OctetString"
_HpicfUsrAuthMacAuthPasswordEncrypted_Object = MibScalar
hpicfUsrAuthMacAuthPasswordEncrypted = _HpicfUsrAuthMacAuthPasswordEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 1, 31),
    _HpicfUsrAuthMacAuthPasswordEncrypted_Type()
)
hpicfUsrAuthMacAuthPasswordEncrypted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthPasswordEncrypted.setStatus("current")
_HpicfUsrAuthPorts_ObjectIdentity = ObjectIdentity
hpicfUsrAuthPorts = _HpicfUsrAuthPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 2)
)
_HpicfUsrAuthPortTable_Object = MibTable
hpicfUsrAuthPortTable = _HpicfUsrAuthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthPortTable.setStatus("current")
_HpicfUsrAuthPortEntry_Object = MibTableRow
hpicfUsrAuthPortEntry = _HpicfUsrAuthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 2, 1, 1)
)
hpicfUsrAuthPortEntry.setIndexNames(
    (0, "HP-USER-AUTH", "hpicfUsrAuthPortNumber"),
)
if mibBuilder.loadTexts:
    hpicfUsrAuthPortEntry.setStatus("current")
_HpicfUsrAuthPortNumber_Type = InterfaceIndex
_HpicfUsrAuthPortNumber_Object = MibTableColumn
hpicfUsrAuthPortNumber = _HpicfUsrAuthPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 2, 1, 1, 1),
    _HpicfUsrAuthPortNumber_Type()
)
hpicfUsrAuthPortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfUsrAuthPortNumber.setStatus("current")
_HpicfUsrAuthWebAuthAdminStatus_Type = TruthValue
_HpicfUsrAuthWebAuthAdminStatus_Object = MibTableColumn
hpicfUsrAuthWebAuthAdminStatus = _HpicfUsrAuthWebAuthAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 2, 1, 1, 2),
    _HpicfUsrAuthWebAuthAdminStatus_Type()
)
hpicfUsrAuthWebAuthAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthAdminStatus.setStatus("current")
_HpicfUsrAuthMacAuthAdminStatus_Type = TruthValue
_HpicfUsrAuthMacAuthAdminStatus_Object = MibTableColumn
hpicfUsrAuthMacAuthAdminStatus = _HpicfUsrAuthMacAuthAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 2, 1, 1, 3),
    _HpicfUsrAuthMacAuthAdminStatus_Type()
)
hpicfUsrAuthMacAuthAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthAdminStatus.setStatus("current")
_HpicfUsrAuthPortReauthenticate_Type = TruthValue
_HpicfUsrAuthPortReauthenticate_Object = MibTableColumn
hpicfUsrAuthPortReauthenticate = _HpicfUsrAuthPortReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 2, 1, 1, 4),
    _HpicfUsrAuthPortReauthenticate_Type()
)
hpicfUsrAuthPortReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthPortReauthenticate.setStatus("current")
_HpicfUsrAuthLMAAdminStatus_Type = TruthValue
_HpicfUsrAuthLMAAdminStatus_Object = MibTableColumn
hpicfUsrAuthLMAAdminStatus = _HpicfUsrAuthLMAAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 2, 1, 1, 5),
    _HpicfUsrAuthLMAAdminStatus_Type()
)
hpicfUsrAuthLMAAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthLMAAdminStatus.setStatus("current")


class _HpicfUsrAuthLLDPBypassAdminStatus_Type(TruthValue):
    """Custom type hpicfUsrAuthLLDPBypassAdminStatus based on TruthValue"""


_HpicfUsrAuthLLDPBypassAdminStatus_Object = MibTableColumn
hpicfUsrAuthLLDPBypassAdminStatus = _HpicfUsrAuthLLDPBypassAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 2, 1, 1, 6),
    _HpicfUsrAuthLLDPBypassAdminStatus_Type()
)
hpicfUsrAuthLLDPBypassAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthLLDPBypassAdminStatus.setStatus("current")
_HpicfUsrAuthWebAuthConfig_ObjectIdentity = ObjectIdentity
hpicfUsrAuthWebAuthConfig = _HpicfUsrAuthWebAuthConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 3)
)
_HpicfUsrAuthWebAuthConfigTable_Object = MibTable
hpicfUsrAuthWebAuthConfigTable = _HpicfUsrAuthWebAuthConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 3, 1)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthConfigTable.setStatus("current")
_HpicfUsrAuthWebAuthConfigEntry_Object = MibTableRow
hpicfUsrAuthWebAuthConfigEntry = _HpicfUsrAuthWebAuthConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 3, 1, 1)
)
hpicfUsrAuthWebAuthConfigEntry.setIndexNames(
    (0, "HP-USER-AUTH", "hpicfUsrAuthPortNumber"),
)
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthConfigEntry.setStatus("current")


class _HpicfUsrAuthWebAuthClientLimit_Type(Integer32):
    """Custom type hpicfUsrAuthWebAuthClientLimit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_HpicfUsrAuthWebAuthClientLimit_Type.__name__ = "Integer32"
_HpicfUsrAuthWebAuthClientLimit_Object = MibTableColumn
hpicfUsrAuthWebAuthClientLimit = _HpicfUsrAuthWebAuthClientLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 3, 1, 1, 1),
    _HpicfUsrAuthWebAuthClientLimit_Type()
)
hpicfUsrAuthWebAuthClientLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthClientLimit.setStatus("current")


class _HpicfUsrAuthWebAuthClientMoves_Type(Integer32):
    """Custom type hpicfUsrAuthWebAuthClientMoves based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HpicfUsrAuthWebAuthClientMoves_Type.__name__ = "Integer32"
_HpicfUsrAuthWebAuthClientMoves_Object = MibTableColumn
hpicfUsrAuthWebAuthClientMoves = _HpicfUsrAuthWebAuthClientMoves_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 3, 1, 1, 2),
    _HpicfUsrAuthWebAuthClientMoves_Type()
)
hpicfUsrAuthWebAuthClientMoves.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthClientMoves.setStatus("current")


class _HpicfUsrAuthWebAuthSSLState_Type(Integer32):
    """Custom type hpicfUsrAuthWebAuthSSLState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HpicfUsrAuthWebAuthSSLState_Type.__name__ = "Integer32"
_HpicfUsrAuthWebAuthSSLState_Object = MibTableColumn
hpicfUsrAuthWebAuthSSLState = _HpicfUsrAuthWebAuthSSLState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 3, 1, 1, 3),
    _HpicfUsrAuthWebAuthSSLState_Type()
)
hpicfUsrAuthWebAuthSSLState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthSSLState.setStatus("current")


class _HpicfUsrAuthWebAuthRedirectUrl_Type(OctetString):
    """Custom type hpicfUsrAuthWebAuthRedirectUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpicfUsrAuthWebAuthRedirectUrl_Type.__name__ = "OctetString"
_HpicfUsrAuthWebAuthRedirectUrl_Object = MibTableColumn
hpicfUsrAuthWebAuthRedirectUrl = _HpicfUsrAuthWebAuthRedirectUrl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 3, 1, 1, 4),
    _HpicfUsrAuthWebAuthRedirectUrl_Type()
)
hpicfUsrAuthWebAuthRedirectUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthRedirectUrl.setStatus("current")


class _HpicfUsrAuthWebAuthQuietPeriod_Type(Integer32):
    """Custom type hpicfUsrAuthWebAuthQuietPeriod based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfUsrAuthWebAuthQuietPeriod_Type.__name__ = "Integer32"
_HpicfUsrAuthWebAuthQuietPeriod_Object = MibTableColumn
hpicfUsrAuthWebAuthQuietPeriod = _HpicfUsrAuthWebAuthQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 3, 1, 1, 5),
    _HpicfUsrAuthWebAuthQuietPeriod_Type()
)
hpicfUsrAuthWebAuthQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthQuietPeriod.setStatus("current")


class _HpicfUsrAuthWebAuthServerTimeout_Type(Integer32):
    """Custom type hpicfUsrAuthWebAuthServerTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_HpicfUsrAuthWebAuthServerTimeout_Type.__name__ = "Integer32"
_HpicfUsrAuthWebAuthServerTimeout_Object = MibTableColumn
hpicfUsrAuthWebAuthServerTimeout = _HpicfUsrAuthWebAuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 3, 1, 1, 6),
    _HpicfUsrAuthWebAuthServerTimeout_Type()
)
hpicfUsrAuthWebAuthServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthServerTimeout.setStatus("current")


class _HpicfUsrAuthWebAuthServerMaxReq_Type(Integer32):
    """Custom type hpicfUsrAuthWebAuthServerMaxReq based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HpicfUsrAuthWebAuthServerMaxReq_Type.__name__ = "Integer32"
_HpicfUsrAuthWebAuthServerMaxReq_Object = MibTableColumn
hpicfUsrAuthWebAuthServerMaxReq = _HpicfUsrAuthWebAuthServerMaxReq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 3, 1, 1, 7),
    _HpicfUsrAuthWebAuthServerMaxReq_Type()
)
hpicfUsrAuthWebAuthServerMaxReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthServerMaxReq.setStatus("current")


class _HpicfUsrAuthWebAuthMaxRetries_Type(Integer32):
    """Custom type hpicfUsrAuthWebAuthMaxRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HpicfUsrAuthWebAuthMaxRetries_Type.__name__ = "Integer32"
_HpicfUsrAuthWebAuthMaxRetries_Object = MibTableColumn
hpicfUsrAuthWebAuthMaxRetries = _HpicfUsrAuthWebAuthMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 3, 1, 1, 8),
    _HpicfUsrAuthWebAuthMaxRetries_Type()
)
hpicfUsrAuthWebAuthMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthMaxRetries.setStatus("current")


class _HpicfUsrAuthWebAuthLogoffPeriod_Type(Integer32):
    """Custom type hpicfUsrAuthWebAuthLogoffPeriod based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999999),
    )


_HpicfUsrAuthWebAuthLogoffPeriod_Type.__name__ = "Integer32"
_HpicfUsrAuthWebAuthLogoffPeriod_Object = MibTableColumn
hpicfUsrAuthWebAuthLogoffPeriod = _HpicfUsrAuthWebAuthLogoffPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 3, 1, 1, 9),
    _HpicfUsrAuthWebAuthLogoffPeriod_Type()
)
hpicfUsrAuthWebAuthLogoffPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthLogoffPeriod.setStatus("current")


class _HpicfUsrAuthWebAuthReAuthPeriod_Type(Integer32):
    """Custom type hpicfUsrAuthWebAuthReAuthPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999999),
    )


_HpicfUsrAuthWebAuthReAuthPeriod_Type.__name__ = "Integer32"
_HpicfUsrAuthWebAuthReAuthPeriod_Object = MibTableColumn
hpicfUsrAuthWebAuthReAuthPeriod = _HpicfUsrAuthWebAuthReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 3, 1, 1, 10),
    _HpicfUsrAuthWebAuthReAuthPeriod_Type()
)
hpicfUsrAuthWebAuthReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthReAuthPeriod.setStatus("current")
_HpicfUsrAuthWebAuthAuthVid_Type = VlanIndex
_HpicfUsrAuthWebAuthAuthVid_Object = MibTableColumn
hpicfUsrAuthWebAuthAuthVid = _HpicfUsrAuthWebAuthAuthVid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 3, 1, 1, 11),
    _HpicfUsrAuthWebAuthAuthVid_Type()
)
hpicfUsrAuthWebAuthAuthVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthAuthVid.setStatus("current")
_HpicfUsrAuthWebAuthUnauthVid_Type = VlanIndex
_HpicfUsrAuthWebAuthUnauthVid_Object = MibTableColumn
hpicfUsrAuthWebAuthUnauthVid = _HpicfUsrAuthWebAuthUnauthVid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 3, 1, 1, 12),
    _HpicfUsrAuthWebAuthUnauthVid_Type()
)
hpicfUsrAuthWebAuthUnauthVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthUnauthVid.setStatus("current")


class _HpicfUsrAuthWebAuthCacheCredentials_Type(Integer32):
    """Custom type hpicfUsrAuthWebAuthCacheCredentials based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HpicfUsrAuthWebAuthCacheCredentials_Type.__name__ = "Integer32"
_HpicfUsrAuthWebAuthCacheCredentials_Object = MibTableColumn
hpicfUsrAuthWebAuthCacheCredentials = _HpicfUsrAuthWebAuthCacheCredentials_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 3, 1, 1, 13),
    _HpicfUsrAuthWebAuthCacheCredentials_Type()
)
hpicfUsrAuthWebAuthCacheCredentials.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthCacheCredentials.setStatus("current")


class _HpicfUsrAuthWebAuthCachedReauthPeriod_Type(Unsigned32):
    """Custom type hpicfUsrAuthWebAuthCachedReauthPeriod based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpicfUsrAuthWebAuthCachedReauthPeriod_Type.__name__ = "Unsigned32"
_HpicfUsrAuthWebAuthCachedReauthPeriod_Object = MibTableColumn
hpicfUsrAuthWebAuthCachedReauthPeriod = _HpicfUsrAuthWebAuthCachedReauthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 3, 1, 1, 14),
    _HpicfUsrAuthWebAuthCachedReauthPeriod_Type()
)
hpicfUsrAuthWebAuthCachedReauthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthCachedReauthPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthCachedReauthPeriod.setUnits("seconds")
_HpicfUsrAuthWebAuthClientReauthenticateTable_Object = MibTable
hpicfUsrAuthWebAuthClientReauthenticateTable = _HpicfUsrAuthWebAuthClientReauthenticateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 3, 2)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthClientReauthenticateTable.setStatus("current")
_HpicfUsrAuthWebAuthClientReauthenticateEntry_Object = MibTableRow
hpicfUsrAuthWebAuthClientReauthenticateEntry = _HpicfUsrAuthWebAuthClientReauthenticateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 3, 2, 1)
)
hpicfUsrAuthWebAuthClientReauthenticateEntry.setIndexNames(
    (0, "HP-USER-AUTH", "hpicfUsrAuthWebAuthClientReauthenticateInterfaceIndex"),
    (0, "HP-USER-AUTH", "hpicfUsrAuthWebAuthClientReauthenticateMacAddress"),
)
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthClientReauthenticateEntry.setStatus("current")
_HpicfUsrAuthWebAuthClientReauthenticateInterfaceIndex_Type = InterfaceIndex
_HpicfUsrAuthWebAuthClientReauthenticateInterfaceIndex_Object = MibTableColumn
hpicfUsrAuthWebAuthClientReauthenticateInterfaceIndex = _HpicfUsrAuthWebAuthClientReauthenticateInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 3, 2, 1, 1),
    _HpicfUsrAuthWebAuthClientReauthenticateInterfaceIndex_Type()
)
hpicfUsrAuthWebAuthClientReauthenticateInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthClientReauthenticateInterfaceIndex.setStatus("current")
_HpicfUsrAuthWebAuthClientReauthenticateMacAddress_Type = MacAddress
_HpicfUsrAuthWebAuthClientReauthenticateMacAddress_Object = MibTableColumn
hpicfUsrAuthWebAuthClientReauthenticateMacAddress = _HpicfUsrAuthWebAuthClientReauthenticateMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 3, 2, 1, 2),
    _HpicfUsrAuthWebAuthClientReauthenticateMacAddress_Type()
)
hpicfUsrAuthWebAuthClientReauthenticateMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthClientReauthenticateMacAddress.setStatus("current")
_HpicfUsrAuthWebAuthClientReauthenticate_Type = TruthValue
_HpicfUsrAuthWebAuthClientReauthenticate_Object = MibTableColumn
hpicfUsrAuthWebAuthClientReauthenticate = _HpicfUsrAuthWebAuthClientReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 3, 2, 1, 3),
    _HpicfUsrAuthWebAuthClientReauthenticate_Type()
)
hpicfUsrAuthWebAuthClientReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthClientReauthenticate.setStatus("current")
_HpicfUsrAuthMacAuthConfig_ObjectIdentity = ObjectIdentity
hpicfUsrAuthMacAuthConfig = _HpicfUsrAuthMacAuthConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 4)
)
_HpicfUsrAuthMacAuthConfigTable_Object = MibTable
hpicfUsrAuthMacAuthConfigTable = _HpicfUsrAuthMacAuthConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 4, 1)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthConfigTable.setStatus("current")
_HpicfUsrAuthMacAuthConfigEntry_Object = MibTableRow
hpicfUsrAuthMacAuthConfigEntry = _HpicfUsrAuthMacAuthConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 4, 1, 1)
)
hpicfUsrAuthMacAuthConfigEntry.setIndexNames(
    (0, "HP-USER-AUTH", "hpicfUsrAuthPortNumber"),
)
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthConfigEntry.setStatus("current")


class _HpicfUsrAuthMacAuthClientLimit_Type(Integer32):
    """Custom type hpicfUsrAuthMacAuthClientLimit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_HpicfUsrAuthMacAuthClientLimit_Type.__name__ = "Integer32"
_HpicfUsrAuthMacAuthClientLimit_Object = MibTableColumn
hpicfUsrAuthMacAuthClientLimit = _HpicfUsrAuthMacAuthClientLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 4, 1, 1, 1),
    _HpicfUsrAuthMacAuthClientLimit_Type()
)
hpicfUsrAuthMacAuthClientLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthClientLimit.setStatus("current")


class _HpicfUsrAuthMacAuthClientMoves_Type(Integer32):
    """Custom type hpicfUsrAuthMacAuthClientMoves based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HpicfUsrAuthMacAuthClientMoves_Type.__name__ = "Integer32"
_HpicfUsrAuthMacAuthClientMoves_Object = MibTableColumn
hpicfUsrAuthMacAuthClientMoves = _HpicfUsrAuthMacAuthClientMoves_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 4, 1, 1, 2),
    _HpicfUsrAuthMacAuthClientMoves_Type()
)
hpicfUsrAuthMacAuthClientMoves.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthClientMoves.setStatus("current")


class _HpicfUsrAuthMacAuthQuietPeriod_Type(Integer32):
    """Custom type hpicfUsrAuthMacAuthQuietPeriod based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfUsrAuthMacAuthQuietPeriod_Type.__name__ = "Integer32"
_HpicfUsrAuthMacAuthQuietPeriod_Object = MibTableColumn
hpicfUsrAuthMacAuthQuietPeriod = _HpicfUsrAuthMacAuthQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 4, 1, 1, 3),
    _HpicfUsrAuthMacAuthQuietPeriod_Type()
)
hpicfUsrAuthMacAuthQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthQuietPeriod.setStatus("current")


class _HpicfUsrAuthMacAuthServerTimeout_Type(Integer32):
    """Custom type hpicfUsrAuthMacAuthServerTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_HpicfUsrAuthMacAuthServerTimeout_Type.__name__ = "Integer32"
_HpicfUsrAuthMacAuthServerTimeout_Object = MibTableColumn
hpicfUsrAuthMacAuthServerTimeout = _HpicfUsrAuthMacAuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 4, 1, 1, 4),
    _HpicfUsrAuthMacAuthServerTimeout_Type()
)
hpicfUsrAuthMacAuthServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthServerTimeout.setStatus("current")


class _HpicfUsrAuthMacAuthServerMaxReq_Type(Integer32):
    """Custom type hpicfUsrAuthMacAuthServerMaxReq based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HpicfUsrAuthMacAuthServerMaxReq_Type.__name__ = "Integer32"
_HpicfUsrAuthMacAuthServerMaxReq_Object = MibTableColumn
hpicfUsrAuthMacAuthServerMaxReq = _HpicfUsrAuthMacAuthServerMaxReq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 4, 1, 1, 5),
    _HpicfUsrAuthMacAuthServerMaxReq_Type()
)
hpicfUsrAuthMacAuthServerMaxReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthServerMaxReq.setStatus("current")


class _HpicfUsrAuthMacAuthLogoffPeriod_Type(Integer32):
    """Custom type hpicfUsrAuthMacAuthLogoffPeriod based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999999),
    )


_HpicfUsrAuthMacAuthLogoffPeriod_Type.__name__ = "Integer32"
_HpicfUsrAuthMacAuthLogoffPeriod_Object = MibTableColumn
hpicfUsrAuthMacAuthLogoffPeriod = _HpicfUsrAuthMacAuthLogoffPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 4, 1, 1, 6),
    _HpicfUsrAuthMacAuthLogoffPeriod_Type()
)
hpicfUsrAuthMacAuthLogoffPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthLogoffPeriod.setStatus("current")


class _HpicfUsrAuthMacAuthReAuthPeriod_Type(Integer32):
    """Custom type hpicfUsrAuthMacAuthReAuthPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999999),
    )


_HpicfUsrAuthMacAuthReAuthPeriod_Type.__name__ = "Integer32"
_HpicfUsrAuthMacAuthReAuthPeriod_Object = MibTableColumn
hpicfUsrAuthMacAuthReAuthPeriod = _HpicfUsrAuthMacAuthReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 4, 1, 1, 7),
    _HpicfUsrAuthMacAuthReAuthPeriod_Type()
)
hpicfUsrAuthMacAuthReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthReAuthPeriod.setStatus("current")
_HpicfUsrAuthMacAuthAuthVid_Type = VlanIndex
_HpicfUsrAuthMacAuthAuthVid_Object = MibTableColumn
hpicfUsrAuthMacAuthAuthVid = _HpicfUsrAuthMacAuthAuthVid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 4, 1, 1, 8),
    _HpicfUsrAuthMacAuthAuthVid_Type()
)
hpicfUsrAuthMacAuthAuthVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthAuthVid.setStatus("current")
_HpicfUsrAuthMacAuthUnauthVid_Type = VlanIndex
_HpicfUsrAuthMacAuthUnauthVid_Object = MibTableColumn
hpicfUsrAuthMacAuthUnauthVid = _HpicfUsrAuthMacAuthUnauthVid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 4, 1, 1, 9),
    _HpicfUsrAuthMacAuthUnauthVid_Type()
)
hpicfUsrAuthMacAuthUnauthVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthUnauthVid.setStatus("current")


class _HpicfUsrAuthMacAuthCachedReauthPeriod_Type(Unsigned32):
    """Custom type hpicfUsrAuthMacAuthCachedReauthPeriod based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpicfUsrAuthMacAuthCachedReauthPeriod_Type.__name__ = "Unsigned32"
_HpicfUsrAuthMacAuthCachedReauthPeriod_Object = MibTableColumn
hpicfUsrAuthMacAuthCachedReauthPeriod = _HpicfUsrAuthMacAuthCachedReauthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 4, 1, 1, 10),
    _HpicfUsrAuthMacAuthCachedReauthPeriod_Type()
)
hpicfUsrAuthMacAuthCachedReauthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthCachedReauthPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthCachedReauthPeriod.setUnits("seconds")


class _HpicfUsrAuthMacAuthUnAuthPeriod_Type(Integer32):
    """Custom type hpicfUsrAuthMacAuthUnAuthPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfUsrAuthMacAuthUnAuthPeriod_Type.__name__ = "Integer32"
_HpicfUsrAuthMacAuthUnAuthPeriod_Object = MibTableColumn
hpicfUsrAuthMacAuthUnAuthPeriod = _HpicfUsrAuthMacAuthUnAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 4, 1, 1, 11),
    _HpicfUsrAuthMacAuthUnAuthPeriod_Type()
)
hpicfUsrAuthMacAuthUnAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthUnAuthPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthUnAuthPeriod.setUnits("seconds")


class _HpicfUsrAuthMacAuthMode_Type(Integer32):
    """Custom type hpicfUsrAuthMacAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portBased", 2),
          ("userBased", 1))
    )


_HpicfUsrAuthMacAuthMode_Type.__name__ = "Integer32"
_HpicfUsrAuthMacAuthMode_Object = MibTableColumn
hpicfUsrAuthMacAuthMode = _HpicfUsrAuthMacAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 4, 1, 1, 12),
    _HpicfUsrAuthMacAuthMode_Type()
)
hpicfUsrAuthMacAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthMode.setStatus("current")


class _HpicfUsrAuthMacPin_Type(TruthValue):
    """Custom type hpicfUsrAuthMacPin based on TruthValue"""
    defaultValue = 2


_HpicfUsrAuthMacPin_Object = MibTableColumn
hpicfUsrAuthMacPin = _HpicfUsrAuthMacPin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 4, 1, 1, 13),
    _HpicfUsrAuthMacPin_Type()
)
hpicfUsrAuthMacPin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacPin.setStatus("current")


class _HpicfMacAuthRetainUnauthClients_Type(TruthValue):
    """Custom type hpicfMacAuthRetainUnauthClients based on TruthValue"""


_HpicfMacAuthRetainUnauthClients_Object = MibTableColumn
hpicfMacAuthRetainUnauthClients = _HpicfMacAuthRetainUnauthClients_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 4, 1, 1, 14),
    _HpicfMacAuthRetainUnauthClients_Type()
)
hpicfMacAuthRetainUnauthClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMacAuthRetainUnauthClients.setStatus("current")
_HpicfUsrAuthMacAuthClientReauthenticateTable_Object = MibTable
hpicfUsrAuthMacAuthClientReauthenticateTable = _HpicfUsrAuthMacAuthClientReauthenticateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 4, 2)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthClientReauthenticateTable.setStatus("current")
_HpicfUsrAuthMacAuthClientReauthenticateEntry_Object = MibTableRow
hpicfUsrAuthMacAuthClientReauthenticateEntry = _HpicfUsrAuthMacAuthClientReauthenticateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 4, 2, 1)
)
hpicfUsrAuthMacAuthClientReauthenticateEntry.setIndexNames(
    (0, "HP-USER-AUTH", "hpicfUsrAuthMacAuthClientReauthenticateInterfaceIndex"),
    (0, "HP-USER-AUTH", "hpicfUsrAuthMacAuthClientReauthenticateMacAddress"),
)
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthClientReauthenticateEntry.setStatus("current")
_HpicfUsrAuthMacAuthClientReauthenticateInterfaceIndex_Type = InterfaceIndex
_HpicfUsrAuthMacAuthClientReauthenticateInterfaceIndex_Object = MibTableColumn
hpicfUsrAuthMacAuthClientReauthenticateInterfaceIndex = _HpicfUsrAuthMacAuthClientReauthenticateInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 4, 2, 1, 1),
    _HpicfUsrAuthMacAuthClientReauthenticateInterfaceIndex_Type()
)
hpicfUsrAuthMacAuthClientReauthenticateInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthClientReauthenticateInterfaceIndex.setStatus("current")
_HpicfUsrAuthMacAuthClientReauthenticateMacAddress_Type = MacAddress
_HpicfUsrAuthMacAuthClientReauthenticateMacAddress_Object = MibTableColumn
hpicfUsrAuthMacAuthClientReauthenticateMacAddress = _HpicfUsrAuthMacAuthClientReauthenticateMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 4, 2, 1, 2),
    _HpicfUsrAuthMacAuthClientReauthenticateMacAddress_Type()
)
hpicfUsrAuthMacAuthClientReauthenticateMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthClientReauthenticateMacAddress.setStatus("current")
_HpicfUsrAuthMacAuthClientReauthenticate_Type = TruthValue
_HpicfUsrAuthMacAuthClientReauthenticate_Object = MibTableColumn
hpicfUsrAuthMacAuthClientReauthenticate = _HpicfUsrAuthMacAuthClientReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 4, 2, 1, 3),
    _HpicfUsrAuthMacAuthClientReauthenticate_Type()
)
hpicfUsrAuthMacAuthClientReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthClientReauthenticate.setStatus("current")
_HpicfUsrAuthWebAuthStats_ObjectIdentity = ObjectIdentity
hpicfUsrAuthWebAuthStats = _HpicfUsrAuthWebAuthStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 5)
)
_HpicfUsrAuthWebAuthSessionStatsTable_Object = MibTable
hpicfUsrAuthWebAuthSessionStatsTable = _HpicfUsrAuthWebAuthSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 5, 1)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthSessionStatsTable.setStatus("current")
_HpicfUsrAuthWebAuthSessionStatsEntry_Object = MibTableRow
hpicfUsrAuthWebAuthSessionStatsEntry = _HpicfUsrAuthWebAuthSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 5, 1, 1)
)
hpicfUsrAuthWebAuthSessionStatsEntry.setIndexNames(
    (0, "HP-USER-AUTH", "hpicfUsrAuthPortNumber"),
    (0, "HP-USER-AUTH", "hpicfUsrAuthWebAuthSessionMacAddr"),
)
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthSessionStatsEntry.setStatus("current")
_HpicfUsrAuthWebAuthSessionMacAddr_Type = MacAddress
_HpicfUsrAuthWebAuthSessionMacAddr_Object = MibTableColumn
hpicfUsrAuthWebAuthSessionMacAddr = _HpicfUsrAuthWebAuthSessionMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 5, 1, 1, 1),
    _HpicfUsrAuthWebAuthSessionMacAddr_Type()
)
hpicfUsrAuthWebAuthSessionMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthSessionMacAddr.setStatus("current")
_HpicfUsrAuthWebAuthSessionName_Type = SnmpAdminString
_HpicfUsrAuthWebAuthSessionName_Object = MibTableColumn
hpicfUsrAuthWebAuthSessionName = _HpicfUsrAuthWebAuthSessionName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 5, 1, 1, 2),
    _HpicfUsrAuthWebAuthSessionName_Type()
)
hpicfUsrAuthWebAuthSessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthSessionName.setStatus("current")


class _HpicfUsrAuthWebAuthSessionState_Type(Integer32):
    """Custom type hpicfUsrAuthWebAuthSessionState based on Integer32"""
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
        *(("authReqRejectNoVlan", 4),
          ("authReqRejectUnauthVlan", 5),
          ("authReqTimeoutNoVlan", 6),
          ("authReqTimeoutUnauthVlan", 7),
          ("authenticated", 1),
          ("authenticating", 3),
          ("criticalAuth", 10),
          ("initialRole", 8),
          ("initialRoleFailed", 9),
          ("openAuth", 11),
          ("unauthenticated", 2))
    )


_HpicfUsrAuthWebAuthSessionState_Type.__name__ = "Integer32"
_HpicfUsrAuthWebAuthSessionState_Object = MibTableColumn
hpicfUsrAuthWebAuthSessionState = _HpicfUsrAuthWebAuthSessionState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 5, 1, 1, 3),
    _HpicfUsrAuthWebAuthSessionState_Type()
)
hpicfUsrAuthWebAuthSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthSessionState.setStatus("current")
_HpicfUsrAuthWebAuthSessionStateTime_Type = Unsigned32
_HpicfUsrAuthWebAuthSessionStateTime_Object = MibTableColumn
hpicfUsrAuthWebAuthSessionStateTime = _HpicfUsrAuthWebAuthSessionStateTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 5, 1, 1, 4),
    _HpicfUsrAuthWebAuthSessionStateTime_Type()
)
hpicfUsrAuthWebAuthSessionStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthSessionStateTime.setStatus("current")
_HpicfUsrAuthWebAuthSessionAuthVid_Type = VlanIndex
_HpicfUsrAuthWebAuthSessionAuthVid_Object = MibTableColumn
hpicfUsrAuthWebAuthSessionAuthVid = _HpicfUsrAuthWebAuthSessionAuthVid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 5, 1, 1, 5),
    _HpicfUsrAuthWebAuthSessionAuthVid_Type()
)
hpicfUsrAuthWebAuthSessionAuthVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthSessionAuthVid.setStatus("current")
_HpicfUsrAuthWebAuthSessionUnauthVid_Type = VlanIndex
_HpicfUsrAuthWebAuthSessionUnauthVid_Object = MibTableColumn
hpicfUsrAuthWebAuthSessionUnauthVid = _HpicfUsrAuthWebAuthSessionUnauthVid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 5, 1, 1, 6),
    _HpicfUsrAuthWebAuthSessionUnauthVid_Type()
)
hpicfUsrAuthWebAuthSessionUnauthVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthSessionUnauthVid.setStatus("current")


class _HpicfUsrAuthWebAuthSessionTimeout_Type(Unsigned32):
    """Custom type hpicfUsrAuthWebAuthSessionTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpicfUsrAuthWebAuthSessionTimeout_Type.__name__ = "Unsigned32"
_HpicfUsrAuthWebAuthSessionTimeout_Object = MibTableColumn
hpicfUsrAuthWebAuthSessionTimeout = _HpicfUsrAuthWebAuthSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 5, 1, 1, 7),
    _HpicfUsrAuthWebAuthSessionTimeout_Type()
)
hpicfUsrAuthWebAuthSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthSessionTimeout.setUnits("seconds")
_HpicfUsrAuthWebAuthSessionRole_Type = HpAutzUserRoleName
_HpicfUsrAuthWebAuthSessionRole_Object = MibTableColumn
hpicfUsrAuthWebAuthSessionRole = _HpicfUsrAuthWebAuthSessionRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 5, 1, 1, 8),
    _HpicfUsrAuthWebAuthSessionRole_Type()
)
hpicfUsrAuthWebAuthSessionRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthSessionRole.setStatus("current")
_HpicfUsrAuthMacAuthStats_ObjectIdentity = ObjectIdentity
hpicfUsrAuthMacAuthStats = _HpicfUsrAuthMacAuthStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 6)
)
_HpicfUsrAuthMacAuthSessionStatsTable_Object = MibTable
hpicfUsrAuthMacAuthSessionStatsTable = _HpicfUsrAuthMacAuthSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 6, 1)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthSessionStatsTable.setStatus("current")
_HpicfUsrAuthMacAuthSessionStatsEntry_Object = MibTableRow
hpicfUsrAuthMacAuthSessionStatsEntry = _HpicfUsrAuthMacAuthSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 6, 1, 1)
)
hpicfUsrAuthMacAuthSessionStatsEntry.setIndexNames(
    (0, "HP-USER-AUTH", "hpicfUsrAuthPortNumber"),
    (0, "HP-USER-AUTH", "hpicfUsrAuthMacAuthSessionMacAddr"),
)
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthSessionStatsEntry.setStatus("current")
_HpicfUsrAuthMacAuthSessionMacAddr_Type = MacAddress
_HpicfUsrAuthMacAuthSessionMacAddr_Object = MibTableColumn
hpicfUsrAuthMacAuthSessionMacAddr = _HpicfUsrAuthMacAuthSessionMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 6, 1, 1, 1),
    _HpicfUsrAuthMacAuthSessionMacAddr_Type()
)
hpicfUsrAuthMacAuthSessionMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthSessionMacAddr.setStatus("current")


class _HpicfUsrAuthMacAuthSessionState_Type(Integer32):
    """Custom type hpicfUsrAuthMacAuthSessionState based on Integer32"""
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
        *(("authReqRejectNoVlan", 4),
          ("authReqRejectUnauthVlan", 5),
          ("authReqTimeoutNoVlan", 6),
          ("authReqTimeoutUnauthVlan", 7),
          ("authenticated", 1),
          ("authenticating", 3),
          ("criticalAuth", 10),
          ("initialRole", 8),
          ("initialRoleFailed", 9),
          ("openAuth", 11),
          ("unauthenticated", 2))
    )


_HpicfUsrAuthMacAuthSessionState_Type.__name__ = "Integer32"
_HpicfUsrAuthMacAuthSessionState_Object = MibTableColumn
hpicfUsrAuthMacAuthSessionState = _HpicfUsrAuthMacAuthSessionState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 6, 1, 1, 2),
    _HpicfUsrAuthMacAuthSessionState_Type()
)
hpicfUsrAuthMacAuthSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthSessionState.setStatus("current")
_HpicfUsrAuthMacAuthSessionStateTime_Type = Unsigned32
_HpicfUsrAuthMacAuthSessionStateTime_Object = MibTableColumn
hpicfUsrAuthMacAuthSessionStateTime = _HpicfUsrAuthMacAuthSessionStateTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 6, 1, 1, 3),
    _HpicfUsrAuthMacAuthSessionStateTime_Type()
)
hpicfUsrAuthMacAuthSessionStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthSessionStateTime.setStatus("current")
_HpicfUsrAuthMacAuthSessionAuthVid_Type = VlanIndex
_HpicfUsrAuthMacAuthSessionAuthVid_Object = MibTableColumn
hpicfUsrAuthMacAuthSessionAuthVid = _HpicfUsrAuthMacAuthSessionAuthVid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 6, 1, 1, 4),
    _HpicfUsrAuthMacAuthSessionAuthVid_Type()
)
hpicfUsrAuthMacAuthSessionAuthVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthSessionAuthVid.setStatus("current")
_HpicfUsrAuthMacAuthSessionUnauthVid_Type = VlanIndex
_HpicfUsrAuthMacAuthSessionUnauthVid_Object = MibTableColumn
hpicfUsrAuthMacAuthSessionUnauthVid = _HpicfUsrAuthMacAuthSessionUnauthVid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 6, 1, 1, 5),
    _HpicfUsrAuthMacAuthSessionUnauthVid_Type()
)
hpicfUsrAuthMacAuthSessionUnauthVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthSessionUnauthVid.setStatus("current")


class _HpicfUsrAuthMacAuthSessionTimeout_Type(Unsigned32):
    """Custom type hpicfUsrAuthMacAuthSessionTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpicfUsrAuthMacAuthSessionTimeout_Type.__name__ = "Unsigned32"
_HpicfUsrAuthMacAuthSessionTimeout_Object = MibTableColumn
hpicfUsrAuthMacAuthSessionTimeout = _HpicfUsrAuthMacAuthSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 6, 1, 1, 6),
    _HpicfUsrAuthMacAuthSessionTimeout_Type()
)
hpicfUsrAuthMacAuthSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthSessionTimeout.setUnits("seconds")


class _HpicfUsrAuthMacAuthSessionUsrNumberCnt_Type(Counter32):
    """Custom type hpicfUsrAuthMacAuthSessionUsrNumberCnt based on Counter32"""
    defaultValue = 0


_HpicfUsrAuthMacAuthSessionUsrNumberCnt_Object = MibTableColumn
hpicfUsrAuthMacAuthSessionUsrNumberCnt = _HpicfUsrAuthMacAuthSessionUsrNumberCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 6, 1, 1, 7),
    _HpicfUsrAuthMacAuthSessionUsrNumberCnt_Type()
)
hpicfUsrAuthMacAuthSessionUsrNumberCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthSessionUsrNumberCnt.setStatus("current")
_HpicfUsrAuthMacAuthSessionName_Type = SnmpAdminString
_HpicfUsrAuthMacAuthSessionName_Object = MibTableColumn
hpicfUsrAuthMacAuthSessionName = _HpicfUsrAuthMacAuthSessionName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 6, 1, 1, 8),
    _HpicfUsrAuthMacAuthSessionName_Type()
)
hpicfUsrAuthMacAuthSessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthSessionName.setStatus("current")
_HpicfUsrAuthMacAuthSessionRole_Type = HpAutzUserRoleName
_HpicfUsrAuthMacAuthSessionRole_Object = MibTableColumn
hpicfUsrAuthMacAuthSessionRole = _HpicfUsrAuthMacAuthSessionRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 6, 1, 1, 9),
    _HpicfUsrAuthMacAuthSessionRole_Type()
)
hpicfUsrAuthMacAuthSessionRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthSessionRole.setStatus("current")
_HpicfUsrAuthConformance_ObjectIdentity = ObjectIdentity
hpicfUsrAuthConformance = _HpicfUsrAuthConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7)
)
_HpicfUsrAuthGroups_ObjectIdentity = ObjectIdentity
hpicfUsrAuthGroups = _HpicfUsrAuthGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 2)
)
_HpicfUsrAuthCompliances_ObjectIdentity = ObjectIdentity
hpicfUsrAuthCompliances = _HpicfUsrAuthCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 4)
)
_HpicfUsrAuthNotifyConformance_ObjectIdentity = ObjectIdentity
hpicfUsrAuthNotifyConformance = _HpicfUsrAuthNotifyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 8)
)
_HpicfUsrAuthMacGlobalConformance_ObjectIdentity = ObjectIdentity
hpicfUsrAuthMacGlobalConformance = _HpicfUsrAuthMacGlobalConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 9)
)
_HpicfUsrAuthWebAuthAccessDeniedConformance_ObjectIdentity = ObjectIdentity
hpicfUsrAuthWebAuthAccessDeniedConformance = _HpicfUsrAuthWebAuthAccessDeniedConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 10)
)
_HpicfUsrAuthMacAuthUsrNumberConformance_ObjectIdentity = ObjectIdentity
hpicfUsrAuthMacAuthUsrNumberConformance = _HpicfUsrAuthMacAuthUsrNumberConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 11)
)
_HpicfUsrAuthLastLogin_ObjectIdentity = ObjectIdentity
hpicfUsrAuthLastLogin = _HpicfUsrAuthLastLogin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 12)
)
_HpicfUsrAuthLastLoginCurrentGeneration_Type = Unsigned32
_HpicfUsrAuthLastLoginCurrentGeneration_Object = MibScalar
hpicfUsrAuthLastLoginCurrentGeneration = _HpicfUsrAuthLastLoginCurrentGeneration_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 12, 1),
    _HpicfUsrAuthLastLoginCurrentGeneration_Type()
)
hpicfUsrAuthLastLoginCurrentGeneration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthLastLoginCurrentGeneration.setStatus("current")
_HpicfUsrAuthLastLoginTable_Object = MibTable
hpicfUsrAuthLastLoginTable = _HpicfUsrAuthLastLoginTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 12, 2)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthLastLoginTable.setStatus("current")
_HpicfUsrAuthLastLoginEntry_Object = MibTableRow
hpicfUsrAuthLastLoginEntry = _HpicfUsrAuthLastLoginEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 12, 2, 1)
)
hpicfUsrAuthLastLoginEntry.setIndexNames(
    (0, "HP-USER-AUTH", "hpicfUsrAuthLastLoginIndex"),
)
if mibBuilder.loadTexts:
    hpicfUsrAuthLastLoginEntry.setStatus("current")


class _HpicfUsrAuthLastLoginIndex_Type(Unsigned32):
    """Custom type hpicfUsrAuthLastLoginIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64511),
    )


_HpicfUsrAuthLastLoginIndex_Type.__name__ = "Unsigned32"
_HpicfUsrAuthLastLoginIndex_Object = MibTableColumn
hpicfUsrAuthLastLoginIndex = _HpicfUsrAuthLastLoginIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 12, 2, 1, 1),
    _HpicfUsrAuthLastLoginIndex_Type()
)
hpicfUsrAuthLastLoginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfUsrAuthLastLoginIndex.setStatus("current")


class _HpicfUsrAuthLastLoginName_Type(DisplayString):
    """Custom type hpicfUsrAuthLastLoginName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HpicfUsrAuthLastLoginName_Type.__name__ = "DisplayString"
_HpicfUsrAuthLastLoginName_Object = MibTableColumn
hpicfUsrAuthLastLoginName = _HpicfUsrAuthLastLoginName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 12, 2, 1, 2),
    _HpicfUsrAuthLastLoginName_Type()
)
hpicfUsrAuthLastLoginName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthLastLoginName.setStatus("current")


class _HpicfUsrAuthLastLoginPrivilege_Type(Integer32):
    """Custom type hpicfUsrAuthLastLoginPrivilege based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manager", 2),
          ("operator", 1),
          ("superuser", 3))
    )


_HpicfUsrAuthLastLoginPrivilege_Type.__name__ = "Integer32"
_HpicfUsrAuthLastLoginPrivilege_Object = MibTableColumn
hpicfUsrAuthLastLoginPrivilege = _HpicfUsrAuthLastLoginPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 12, 2, 1, 3),
    _HpicfUsrAuthLastLoginPrivilege_Type()
)
hpicfUsrAuthLastLoginPrivilege.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthLastLoginPrivilege.setStatus("current")
_HpicfUsrAuthLastLoginSuccTime_Type = DateAndTime
_HpicfUsrAuthLastLoginSuccTime_Object = MibTableColumn
hpicfUsrAuthLastLoginSuccTime = _HpicfUsrAuthLastLoginSuccTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 12, 2, 1, 4),
    _HpicfUsrAuthLastLoginSuccTime_Type()
)
hpicfUsrAuthLastLoginSuccTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthLastLoginSuccTime.setStatus("current")
_HpicfUsrAuthLastLoginSuccAddrType_Type = InetAddressType
_HpicfUsrAuthLastLoginSuccAddrType_Object = MibTableColumn
hpicfUsrAuthLastLoginSuccAddrType = _HpicfUsrAuthLastLoginSuccAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 12, 2, 1, 5),
    _HpicfUsrAuthLastLoginSuccAddrType_Type()
)
hpicfUsrAuthLastLoginSuccAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthLastLoginSuccAddrType.setStatus("current")
_HpicfUsrAuthLastLoginSuccAddr_Type = InetAddress
_HpicfUsrAuthLastLoginSuccAddr_Object = MibTableColumn
hpicfUsrAuthLastLoginSuccAddr = _HpicfUsrAuthLastLoginSuccAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 12, 2, 1, 6),
    _HpicfUsrAuthLastLoginSuccAddr_Type()
)
hpicfUsrAuthLastLoginSuccAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthLastLoginSuccAddr.setStatus("current")
_HpicfUsrAuthLastLoginUnsuccTime_Type = DateAndTime
_HpicfUsrAuthLastLoginUnsuccTime_Object = MibTableColumn
hpicfUsrAuthLastLoginUnsuccTime = _HpicfUsrAuthLastLoginUnsuccTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 12, 2, 1, 7),
    _HpicfUsrAuthLastLoginUnsuccTime_Type()
)
hpicfUsrAuthLastLoginUnsuccTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthLastLoginUnsuccTime.setStatus("current")
_HpicfUsrAuthLastLoginUnsuccCount_Type = Counter32
_HpicfUsrAuthLastLoginUnsuccCount_Object = MibTableColumn
hpicfUsrAuthLastLoginUnsuccCount = _HpicfUsrAuthLastLoginUnsuccCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 12, 2, 1, 8),
    _HpicfUsrAuthLastLoginUnsuccCount_Type()
)
hpicfUsrAuthLastLoginUnsuccCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthLastLoginUnsuccCount.setStatus("current")
_HpicfUsrAuthLastLoginGeneration_Type = Unsigned32
_HpicfUsrAuthLastLoginGeneration_Object = MibTableColumn
hpicfUsrAuthLastLoginGeneration = _HpicfUsrAuthLastLoginGeneration_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 12, 2, 1, 9),
    _HpicfUsrAuthLastLoginGeneration_Type()
)
hpicfUsrAuthLastLoginGeneration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthLastLoginGeneration.setStatus("current")


class _HpicfUsrAuthLastLoginDeleteAll_Type(TruthValue):
    """Custom type hpicfUsrAuthLastLoginDeleteAll based on TruthValue"""


_HpicfUsrAuthLastLoginDeleteAll_Object = MibScalar
hpicfUsrAuthLastLoginDeleteAll = _HpicfUsrAuthLastLoginDeleteAll_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 12, 3),
    _HpicfUsrAuthLastLoginDeleteAll_Type()
)
hpicfUsrAuthLastLoginDeleteAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthLastLoginDeleteAll.setStatus("current")
_HpicfUsrAuthCaptivePortal_ObjectIdentity = ObjectIdentity
hpicfUsrAuthCaptivePortal = _HpicfUsrAuthCaptivePortal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 13)
)
_HpicfUsrAuthCaptivePortalConfig_ObjectIdentity = ObjectIdentity
hpicfUsrAuthCaptivePortalConfig = _HpicfUsrAuthCaptivePortalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 13, 1)
)


class _HpicfUsrAuthCaptivePortalConfigEnabled_Type(TruthValue):
    """Custom type hpicfUsrAuthCaptivePortalConfigEnabled based on TruthValue"""


_HpicfUsrAuthCaptivePortalConfigEnabled_Object = MibScalar
hpicfUsrAuthCaptivePortalConfigEnabled = _HpicfUsrAuthCaptivePortalConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 13, 1, 1),
    _HpicfUsrAuthCaptivePortalConfigEnabled_Type()
)
hpicfUsrAuthCaptivePortalConfigEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthCaptivePortalConfigEnabled.setStatus("current")


class _HpicfUsrAuthCaptivePortalUrlHashKey_Type(OctetString):
    """Custom type hpicfUsrAuthCaptivePortalUrlHashKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpicfUsrAuthCaptivePortalUrlHashKey_Type.__name__ = "OctetString"
_HpicfUsrAuthCaptivePortalUrlHashKey_Object = MibScalar
hpicfUsrAuthCaptivePortalUrlHashKey = _HpicfUsrAuthCaptivePortalUrlHashKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 13, 1, 2),
    _HpicfUsrAuthCaptivePortalUrlHashKey_Type()
)
hpicfUsrAuthCaptivePortalUrlHashKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthCaptivePortalUrlHashKey.setStatus("current")


class _HpicfUsrAuthCaptivePortalUrlHashKeyEncrypted_Type(OctetString):
    """Custom type hpicfUsrAuthCaptivePortalUrlHashKeyEncrypted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfUsrAuthCaptivePortalUrlHashKeyEncrypted_Type.__name__ = "OctetString"
_HpicfUsrAuthCaptivePortalUrlHashKeyEncrypted_Object = MibScalar
hpicfUsrAuthCaptivePortalUrlHashKeyEncrypted = _HpicfUsrAuthCaptivePortalUrlHashKeyEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 13, 1, 3),
    _HpicfUsrAuthCaptivePortalUrlHashKeyEncrypted_Type()
)
hpicfUsrAuthCaptivePortalUrlHashKeyEncrypted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrAuthCaptivePortalUrlHashKeyEncrypted.setStatus("current")
_HpicfUsrAuthCaptivePortalProfileTable_Object = MibTable
hpicfUsrAuthCaptivePortalProfileTable = _HpicfUsrAuthCaptivePortalProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 13, 2)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthCaptivePortalProfileTable.setStatus("current")
_HpicfUsrAuthCaptivePortalProfileEntry_Object = MibTableRow
hpicfUsrAuthCaptivePortalProfileEntry = _HpicfUsrAuthCaptivePortalProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 13, 2, 1)
)
hpicfUsrAuthCaptivePortalProfileEntry.setIndexNames(
    (0, "HP-USER-AUTH", "hpicfUsrAuthCaptivePortalProfileName"),
)
if mibBuilder.loadTexts:
    hpicfUsrAuthCaptivePortalProfileEntry.setStatus("current")


class _HpicfUsrAuthCaptivePortalProfileName_Type(OctetString):
    """Custom type hpicfUsrAuthCaptivePortalProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpicfUsrAuthCaptivePortalProfileName_Type.__name__ = "OctetString"
_HpicfUsrAuthCaptivePortalProfileName_Object = MibTableColumn
hpicfUsrAuthCaptivePortalProfileName = _HpicfUsrAuthCaptivePortalProfileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 13, 2, 1, 1),
    _HpicfUsrAuthCaptivePortalProfileName_Type()
)
hpicfUsrAuthCaptivePortalProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfUsrAuthCaptivePortalProfileName.setStatus("current")
_HpicfUsrAuthCaptivePortalProfileRowStatus_Type = RowStatus
_HpicfUsrAuthCaptivePortalProfileRowStatus_Object = MibTableColumn
hpicfUsrAuthCaptivePortalProfileRowStatus = _HpicfUsrAuthCaptivePortalProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 13, 2, 1, 2),
    _HpicfUsrAuthCaptivePortalProfileRowStatus_Type()
)
hpicfUsrAuthCaptivePortalProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrAuthCaptivePortalProfileRowStatus.setStatus("current")


class _HpicfUsrAuthCaptivePortalProfileType_Type(Integer32):
    """Custom type hpicfUsrAuthCaptivePortalProfileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("custom", 2),
          ("predefined", 1))
    )


_HpicfUsrAuthCaptivePortalProfileType_Type.__name__ = "Integer32"
_HpicfUsrAuthCaptivePortalProfileType_Object = MibTableColumn
hpicfUsrAuthCaptivePortalProfileType = _HpicfUsrAuthCaptivePortalProfileType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 13, 2, 1, 3),
    _HpicfUsrAuthCaptivePortalProfileType_Type()
)
hpicfUsrAuthCaptivePortalProfileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrAuthCaptivePortalProfileType.setStatus("current")


class _HpicfUsrAuthCaptivePortalProfileRedirectUrl_Type(OctetString):
    """Custom type hpicfUsrAuthCaptivePortalProfileRedirectUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 247),
    )


_HpicfUsrAuthCaptivePortalProfileRedirectUrl_Type.__name__ = "OctetString"
_HpicfUsrAuthCaptivePortalProfileRedirectUrl_Object = MibTableColumn
hpicfUsrAuthCaptivePortalProfileRedirectUrl = _HpicfUsrAuthCaptivePortalProfileRedirectUrl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 13, 2, 1, 4),
    _HpicfUsrAuthCaptivePortalProfileRedirectUrl_Type()
)
hpicfUsrAuthCaptivePortalProfileRedirectUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrAuthCaptivePortalProfileRedirectUrl.setStatus("current")

# Managed Objects groups

hpicfUsrAuthSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 2, 1)
)
hpicfUsrAuthSystemGroup.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthWebAuthDhcpBaseAddress"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthDhcpMask"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthDhcpLease"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthAddrFormat"),
        ("HP-USER-AUTH", "hpicfUsrAuthCLIPasswdSet"),
        ("HP-USER-AUTH", "hpicfUsrAuthCLIInterface"),
        ("HP-USER-AUTH", "hpicfUsrAuthCacheCredTimeOut"),
        ("HP-USER-AUTH", "hpicfUsrAuthUseLLDPData"))
)
if mibBuilder.loadTexts:
    hpicfUsrAuthSystemGroup.setStatus("current")

hpicfUsrAuthPortsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 2, 2)
)
hpicfUsrAuthPortsGroup.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthPortNumber"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthAdminStatus"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthAdminStatus"),
        ("HP-USER-AUTH", "hpicfUsrAuthPortReauthenticate"))
)
if mibBuilder.loadTexts:
    hpicfUsrAuthPortsGroup.setStatus("deprecated")

hpicfUsrAuthWebAuthConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 2, 3)
)
hpicfUsrAuthWebAuthConfigGroup.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthWebAuthClientLimit"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthClientMoves"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthSSLState"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthRedirectUrl"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthQuietPeriod"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthServerTimeout"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthServerMaxReq"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthMaxRetries"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthLogoffPeriod"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthReAuthPeriod"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthAuthVid"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthUnauthVid"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthCacheCredentials"))
)
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthConfigGroup.setStatus("current")

hpicfUsrAuthMacAuthConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 2, 4)
)
hpicfUsrAuthMacAuthConfigGroup.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthMacAuthClientLimit"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthClientMoves"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthQuietPeriod"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthServerTimeout"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthServerMaxReq"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthLogoffPeriod"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthReAuthPeriod"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthAuthVid"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthUnauthVid"))
)
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthConfigGroup.setStatus("current")

hpicfUsrAuthWebAuthSessionStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 2, 5)
)
hpicfUsrAuthWebAuthSessionStatsGroup.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthWebAuthSessionMacAddr"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthSessionName"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthSessionState"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthSessionStateTime"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthSessionAuthVid"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthSessionUnauthVid"))
)
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthSessionStatsGroup.setStatus("deprecated")

hpicfUsrAuthMacAuthSessionStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 2, 6)
)
hpicfUsrAuthMacAuthSessionStatsGroup.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthMacAuthSessionMacAddr"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthSessionState"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthSessionStateTime"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthSessionAuthVid"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthSessionUnauthVid"))
)
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthSessionStatsGroup.setStatus("deprecated")

hpicfUsrAuthWebAuthConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 2, 7)
)
hpicfUsrAuthWebAuthConfigGroup1.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthWebAuthClientLimit"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthClientMoves"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthSSLState"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthRedirectUrl"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthQuietPeriod"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthServerTimeout"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthServerMaxReq"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthMaxRetries"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthLogoffPeriod"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthReAuthPeriod"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthAuthVid"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthUnauthVid"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthCacheCredentials"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthCachedReauthPeriod"))
)
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthConfigGroup1.setStatus("current")

hpicfUsrAuthMacAuthConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 2, 8)
)
hpicfUsrAuthMacAuthConfigGroup1.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthMacAuthClientLimit"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthClientMoves"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthQuietPeriod"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthServerTimeout"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthServerMaxReq"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthLogoffPeriod"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthReAuthPeriod"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthAuthVid"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthUnauthVid"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthCachedReauthPeriod"))
)
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthConfigGroup1.setStatus("current")

hpicfUsrAuthMacAuthConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 2, 9)
)
hpicfUsrAuthMacAuthConfigGroup2.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthMacAuthClientLimit"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthClientMoves"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthQuietPeriod"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthServerTimeout"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthServerMaxReq"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthLogoffPeriod"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthReAuthPeriod"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthAuthVid"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthUnauthVid"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthUnAuthPeriod"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthCachedReauthPeriod"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthMode"))
)
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthConfigGroup2.setStatus("deprecated")

hpicfUsrAuthRedirectServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 2, 10)
)
hpicfUsrAuthRedirectServerGroup.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthRedirectServerURL"),
        ("HP-USER-AUTH", "hpicfUsrAuthRedirectServerRestrictiveFilter"),
        ("HP-USER-AUTH", "hpicfUsrAuthRedirectServerClientTimeout"),
        ("HP-USER-AUTH", "hpicfUsrAuthRedirectServerAuthFailureStats"),
        ("HP-USER-AUTH", "hpicfUsrAuthRedirectServerRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfUsrAuthRedirectServerGroup.setStatus("current")

hpicfUsrAuthWMAeWAServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 2, 11)
)
hpicfUsrAuthWMAeWAServerGroup.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthWMAeWAServerIPAddressType"),
        ("HP-USER-AUTH", "hpicfUsrAuthWMAeWAServerIPAddress"),
        ("HP-USER-AUTH", "hpicfUsrAuthWMAeWAServerPath"),
        ("HP-USER-AUTH", "hpicfUsrAUthWMAeWAServerRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfUsrAuthWMAeWAServerGroup.setStatus("current")

hpicfUsrAuthClientReauthenticateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 2, 12)
)
hpicfUsrAuthClientReauthenticateGroup.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthClientReauthenticate"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthClientReauthenticate"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthClientReauthenticate"))
)
if mibBuilder.loadTexts:
    hpicfUsrAuthClientReauthenticateGroup.setStatus("current")

hpicfUsrAuthMacAuthSessionStatsGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 2, 13)
)
hpicfUsrAuthMacAuthSessionStatsGroup1.setObjects(
    ("HP-USER-AUTH", "hpicfUsrAuthMacAuthSessionTimeout")
)
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthSessionStatsGroup1.setStatus("current")

hpicfUsrAuthWebAuthSessionStatsGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 2, 14)
)
hpicfUsrAuthWebAuthSessionStatsGroup1.setObjects(
    ("HP-USER-AUTH", "hpicfUsrAuthWebAuthSessionTimeout")
)
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthSessionStatsGroup1.setStatus("current")

hpicfUsrAuthLastLoginGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 2, 15)
)
hpicfUsrAuthLastLoginGroup.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthLastLoginCurrentGeneration"),
        ("HP-USER-AUTH", "hpicfUsrAuthLastLoginDeleteAll"),
        ("HP-USER-AUTH", "hpicfUsrAuthLastLoginName"),
        ("HP-USER-AUTH", "hpicfUsrAuthLastLoginPrivilege"),
        ("HP-USER-AUTH", "hpicfUsrAuthLastLoginSuccTime"),
        ("HP-USER-AUTH", "hpicfUsrAuthLastLoginSuccAddrType"),
        ("HP-USER-AUTH", "hpicfUsrAuthLastLoginSuccAddr"),
        ("HP-USER-AUTH", "hpicfUsrAuthLastLoginUnsuccTime"),
        ("HP-USER-AUTH", "hpicfUsrAuthLastLoginUnsuccCount"),
        ("HP-USER-AUTH", "hpicfUsrAuthLastLoginGeneration"))
)
if mibBuilder.loadTexts:
    hpicfUsrAuthLastLoginGroup.setStatus("current")

hpicfUsrAuthPortsGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 2, 16)
)
hpicfUsrAuthPortsGroup1.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthPortNumber"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthAdminStatus"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthAdminStatus"),
        ("HP-USER-AUTH", "hpicfUsrAuthPortReauthenticate"),
        ("HP-USER-AUTH", "hpicfUsrAuthLMAAdminStatus"))
)
if mibBuilder.loadTexts:
    hpicfUsrAuthPortsGroup1.setStatus("deprecated")

hpicfUsrAuthCaptivePortalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 2, 17)
)
hpicfUsrAuthCaptivePortalGroup.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthCaptivePortalConfigEnabled"),
        ("HP-USER-AUTH", "hpicfUsrAuthCaptivePortalUrlHashKey"),
        ("HP-USER-AUTH", "hpicfUsrAuthCaptivePortalUrlHashKeyEncrypted"))
)
if mibBuilder.loadTexts:
    hpicfUsrAuthCaptivePortalGroup.setStatus("current")

hpicfUsrAuthCaptivePortalProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 2, 18)
)
hpicfUsrAuthCaptivePortalProfileGroup.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthCaptivePortalProfileRowStatus"),
        ("HP-USER-AUTH", "hpicfUsrAuthCaptivePortalProfileType"),
        ("HP-USER-AUTH", "hpicfUsrAuthCaptivePortalProfileRedirectUrl"))
)
if mibBuilder.loadTexts:
    hpicfUsrAuthCaptivePortalProfileGroup.setStatus("current")

hpicfUsrAuthWebAuthSessionStatsGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 2, 19)
)
hpicfUsrAuthWebAuthSessionStatsGroup2.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthWebAuthSessionMacAddr"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthSessionName"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthSessionState"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthSessionStateTime"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthSessionAuthVid"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthSessionUnauthVid"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthSessionRole"))
)
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthSessionStatsGroup2.setStatus("current")

hpicfUsrAuthMacAuthSessionStatsGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 2, 20)
)
hpicfUsrAuthMacAuthSessionStatsGroup2.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthMacAuthSessionMacAddr"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthSessionState"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthSessionStateTime"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthSessionAuthVid"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthSessionUnauthVid"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthSessionName"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthSessionRole"))
)
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthSessionStatsGroup2.setStatus("current")

hpicfUsrAuthPortsGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 2, 21)
)
hpicfUsrAuthPortsGroup2.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthPortNumber"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthAdminStatus"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthAdminStatus"),
        ("HP-USER-AUTH", "hpicfUsrAuthPortReauthenticate"),
        ("HP-USER-AUTH", "hpicfUsrAuthLMAAdminStatus"),
        ("HP-USER-AUTH", "hpicfUsrAuthLLDPBypassAdminStatus"))
)
if mibBuilder.loadTexts:
    hpicfUsrAuthPortsGroup2.setStatus("current")

hpicfUsrAuthMacAuthConfigGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 2, 22)
)
hpicfUsrAuthMacAuthConfigGroup3.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthMacAuthClientLimit"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthClientMoves"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthQuietPeriod"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthServerTimeout"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthServerMaxReq"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthLogoffPeriod"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthReAuthPeriod"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthAuthVid"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthUnauthVid"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthUnAuthPeriod"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthCachedReauthPeriod"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthMode"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacPin"),
        ("HP-USER-AUTH", "hpicfMacAuthRetainUnauthClients"))
)
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthConfigGroup3.setStatus("current")

hpicfNotifcationConfigDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 8, 2)
)
hpicfNotifcationConfigDataGroup.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthCLIFailCnt"),
        ("HP-USER-AUTH", "hpicfUsrAuthCLIPwdNotifyCnt"),
        ("HP-USER-AUTH", "hpicfUsrAuthWMAFailCnt"),
        ("HP-USER-AUTH", "hpicfUsrAuthWMAFailMAC"),
        ("HP-USER-AUTH", "hpicfUsrAuthWMAFailPort"),
        ("HP-USER-AUTH", "hpicfUsrAuthWMAFailVlan"),
        ("HP-USER-AUTH", "hpicfUsrAuthPasswdNotifyEnable"),
        ("HP-USER-AUTH", "hpicfUsrAuthCliNotifyEnable"),
        ("HP-USER-AUTH", "hpicfUsrAuthPortSecNotifyEnable"))
)
if mibBuilder.loadTexts:
    hpicfNotifcationConfigDataGroup.setStatus("deprecated")

hpicfNotificationConfigDataGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 8, 3)
)
hpicfNotificationConfigDataGroup1.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthCLIFailCnt"),
        ("HP-USER-AUTH", "hpicfUsrAuthCLIInterface"),
        ("HP-USER-AUTH", "hpicfUsrAuthLastLoginNotifyStatus"),
        ("HP-USER-AUTH", "hpicfUsrAuthLastLoginNotifyAddrType"),
        ("HP-USER-AUTH", "hpicfUsrAuthLastLoginNotifyAddr"),
        ("HP-USER-AUTH", "hpicfUsrAuthCLIPwdNotifyCnt"),
        ("HP-USER-AUTH", "hpicfUsrAuthWMAFailCnt"),
        ("HP-USER-AUTH", "hpicfUsrAuthWMAFailMAC"),
        ("HP-USER-AUTH", "hpicfUsrAuthWMAFailPort"),
        ("HP-USER-AUTH", "hpicfUsrAuthWMAFailVlan"),
        ("HP-USER-AUTH", "hpicfUsrAuthPasswdNotifyEnable"),
        ("HP-USER-AUTH", "hpicfUsrAuthCliNotifyEnable"),
        ("HP-USER-AUTH", "hpicfUsrAuthPortSecNotifyEnable"))
)
if mibBuilder.loadTexts:
    hpicfNotificationConfigDataGroup1.setStatus("current")

hpicfUsrAuthMacGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 9, 1)
)
hpicfUsrAuthMacGroup.setObjects(
    ("HP-USER-AUTH", "hpicfUsrAuthMacAuthPassword")
)
if mibBuilder.loadTexts:
    hpicfUsrAuthMacGroup.setStatus("deprecated")

hpicfUsrAuthMacGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 9, 2)
)
hpicfUsrAuthMacGroup1.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthMacAuthPassword"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthPasswordEncrypted"))
)
if mibBuilder.loadTexts:
    hpicfUsrAuthMacGroup1.setStatus("current")

hpicfUsrAuthWebAuthAccessDeniedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 10, 1)
)
hpicfUsrAuthWebAuthAccessDeniedGroup.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthWebAuthAccessDeniedMode"),
        ("HP-USER-AUTH", "hpicfUsrAuthWebAuthAccessDeniedMessage"))
)
if mibBuilder.loadTexts:
    hpicfUsrAuthWebAuthAccessDeniedGroup.setStatus("current")

hpicfUsrAuthMacAuthUsrNumberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 11, 1)
)
hpicfUsrAuthMacAuthUsrNumberGroup.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthMacAuthUsrNumberCnt"),
        ("HP-USER-AUTH", "hpicfUsrAuthMacAuthSessionUsrNumberCnt"))
)
if mibBuilder.loadTexts:
    hpicfUsrAuthMacAuthUsrNumberGroup.setStatus("current")


# Notification objects

hpicfUsrAuthCLIAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 0, 1)
)
hpicfUsrAuthCLIAuthFail.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthCLIFailCnt"),
        ("HP-USER-AUTH", "hpicfUsrAuthCLIInterface"))
)
if mibBuilder.loadTexts:
    hpicfUsrAuthCLIAuthFail.setStatus(
        "current"
    )

hpicfUsrAuthPasswdChng = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 0, 2)
)
hpicfUsrAuthPasswdChng.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthCLIPasswdSet"),
        ("HP-USER-AUTH", "hpicfUsrAuthCLIPwdNotifyCnt"))
)
if mibBuilder.loadTexts:
    hpicfUsrAuthPasswdChng.setStatus(
        "current"
    )

hpicfPortSecAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 0, 3)
)
hpicfPortSecAuthFailure.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthWMAFailCnt"),
        ("HP-USER-AUTH", "hpicfUsrAuthWMAFailVlan"),
        ("HP-USER-AUTH", "hpicfUsrAuthWMAFailPort"),
        ("HP-USER-AUTH", "hpicfUsrAuthWMAFailMAC"))
)
if mibBuilder.loadTexts:
    hpicfPortSecAuthFailure.setStatus(
        "current"
    )


# Notifications groups

hpicfUsrAuthNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 8, 1)
)
hpicfUsrAuthNotificationGroup.setObjects(
      *(("HP-USER-AUTH", "hpicfUsrAuthCLIAuthFail"),
        ("HP-USER-AUTH", "hpicfUsrAuthPasswdChng"),
        ("HP-USER-AUTH", "hpicfPortSecAuthFailure"))
)
if mibBuilder.loadTexts:
    hpicfUsrAuthNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfUsrAuthCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 4, 1)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthCompliance.setStatus(
        "deprecated"
    )

hpicfUsrAuthCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 4, 2)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthCompliance1.setStatus(
        "deprecated"
    )

hpicfUsrAuthCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 4, 3)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthCompliance2.setStatus(
        "deprecated"
    )

hpicfUsrAuthCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 4, 4)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthCompliance3.setStatus(
        "deprecated"
    )

hpicfUsrAuthCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 4, 5)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthCompliance4.setStatus(
        "deprecated"
    )

hpicfUsrAuthCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 4, 6)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthCompliance5.setStatus(
        "deprecated"
    )

hpicfUsrAuthCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 4, 7)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthCompliance6.setStatus(
        "current"
    )

hpicfUsrAuthCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 4, 8)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthCompliance7.setStatus(
        "deprecated"
    )

hpicfUsrAuthCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 4, 9)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthCompliance8.setStatus(
        "deprecated"
    )

hpicfUsrAuthCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 4, 10)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthCompliance9.setStatus(
        "deprecated"
    )

hpicfUsrAuthCompliance10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 4, 11)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthCompliance10.setStatus(
        "deprecated"
    )

hpicfUsrAuthCompliance11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 4, 12)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthCompliance11.setStatus(
        "deprecated"
    )

hpicfUsrAuthCompliance12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 4, 13)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthCompliance12.setStatus(
        "deprecated"
    )

hpicfUsrAuthCompliance13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 4, 14)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthCompliance13.setStatus(
        "current"
    )

hpicfUsrAuthCompliance14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 4, 15)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthCompliance14.setStatus(
        "deprecated"
    )

hpicfUsrAuthCompliance15 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 4, 16)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthCompliance15.setStatus(
        "current"
    )

hpicfUsrAuthCompliance16 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19, 7, 4, 17)
)
if mibBuilder.loadTexts:
    hpicfUsrAuthCompliance16.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-USER-AUTH",
    **{"hpicfUsrAuthMIB": hpicfUsrAuthMIB,
       "hpicfUsrAuthNotifications": hpicfUsrAuthNotifications,
       "hpicfUsrAuthCLIAuthFail": hpicfUsrAuthCLIAuthFail,
       "hpicfUsrAuthPasswdChng": hpicfUsrAuthPasswdChng,
       "hpicfPortSecAuthFailure": hpicfPortSecAuthFailure,
       "hpicfUsrAuthSystem": hpicfUsrAuthSystem,
       "hpicfUsrAuthWebAuthDhcpBaseAddress": hpicfUsrAuthWebAuthDhcpBaseAddress,
       "hpicfUsrAuthWebAuthDhcpMask": hpicfUsrAuthWebAuthDhcpMask,
       "hpicfUsrAuthWebAuthDhcpLease": hpicfUsrAuthWebAuthDhcpLease,
       "hpicfUsrAuthMacAuthAddrFormat": hpicfUsrAuthMacAuthAddrFormat,
       "hpicfUsrAuthCliNotifyEnable": hpicfUsrAuthCliNotifyEnable,
       "hpicfUsrAuthCLIInterface": hpicfUsrAuthCLIInterface,
       "hpicfUsrAuthCLIPasswdSet": hpicfUsrAuthCLIPasswdSet,
       "hpicfUsrAuthCLIFailCnt": hpicfUsrAuthCLIFailCnt,
       "hpicfUsrAuthCLIPwdNotifyCnt": hpicfUsrAuthCLIPwdNotifyCnt,
       "hpicfUsrAuthWMAFailCnt": hpicfUsrAuthWMAFailCnt,
       "hpicfUsrAuthWMAFailMAC": hpicfUsrAuthWMAFailMAC,
       "hpicfUsrAuthWMAFailPort": hpicfUsrAuthWMAFailPort,
       "hpicfUsrAuthWMAFailVlan": hpicfUsrAuthWMAFailVlan,
       "hpicfUsrAuthPortSecNotifyEnable": hpicfUsrAuthPortSecNotifyEnable,
       "hpicfUsrAuthPasswdNotifyEnable": hpicfUsrAuthPasswdNotifyEnable,
       "hpicfUsrAuthWMAEWAServerTable": hpicfUsrAuthWMAEWAServerTable,
       "hpicfUsrAuthWMAEWAServerEntry": hpicfUsrAuthWMAEWAServerEntry,
       "hpicfUsrAuthWMAeWAServerIndex": hpicfUsrAuthWMAeWAServerIndex,
       "hpicfUsrAuthWMAeWAServerIPAddressType": hpicfUsrAuthWMAeWAServerIPAddressType,
       "hpicfUsrAuthWMAeWAServerIPAddress": hpicfUsrAuthWMAeWAServerIPAddress,
       "hpicfUsrAuthWMAeWAServerPath": hpicfUsrAuthWMAeWAServerPath,
       "hpicfUsrAUthWMAeWAServerRowStatus": hpicfUsrAUthWMAeWAServerRowStatus,
       "hpicfUsrAuthRedirectServerTable": hpicfUsrAuthRedirectServerTable,
       "hpicfUsrAuthRedirectServerEntry": hpicfUsrAuthRedirectServerEntry,
       "hpicfUsrAuthRedirectServerIndex": hpicfUsrAuthRedirectServerIndex,
       "hpicfUsrAuthRedirectServerURL": hpicfUsrAuthRedirectServerURL,
       "hpicfUsrAuthRedirectServerRowStatus": hpicfUsrAuthRedirectServerRowStatus,
       "hpicfUsrAuthRedirectServerRestrictiveFilter": hpicfUsrAuthRedirectServerRestrictiveFilter,
       "hpicfUsrAuthRedirectServerClientTimeout": hpicfUsrAuthRedirectServerClientTimeout,
       "hpicfUsrAuthRedirectServerAuthFailureStats": hpicfUsrAuthRedirectServerAuthFailureStats,
       "hpicfUsrAuthCacheCredTimeOut": hpicfUsrAuthCacheCredTimeOut,
       "hpicfUsrAuthClientReauthenticateTable": hpicfUsrAuthClientReauthenticateTable,
       "hpicfUsrAuthClientReauthenticateEntry": hpicfUsrAuthClientReauthenticateEntry,
       "hpicfUsrAuthClientReauthenticateInterfaceIndex": hpicfUsrAuthClientReauthenticateInterfaceIndex,
       "hpicfUsrAuthClientReauthenticateMacAddress": hpicfUsrAuthClientReauthenticateMacAddress,
       "hpicfUsrAuthClientReauthenticate": hpicfUsrAuthClientReauthenticate,
       "hpicfUsrAuthMacAuthPassword": hpicfUsrAuthMacAuthPassword,
       "hpicfUsrAuthWebAuthAccessDeniedMode": hpicfUsrAuthWebAuthAccessDeniedMode,
       "hpicfUsrAuthWebAuthAccessDeniedMessage": hpicfUsrAuthWebAuthAccessDeniedMessage,
       "hpicfUsrAuthMacAuthUsrNumberCnt": hpicfUsrAuthMacAuthUsrNumberCnt,
       "hpicfUsrAuthLastLoginNotifyStatus": hpicfUsrAuthLastLoginNotifyStatus,
       "hpicfUsrAuthLastLoginNotifyAddrType": hpicfUsrAuthLastLoginNotifyAddrType,
       "hpicfUsrAuthLastLoginNotifyAddr": hpicfUsrAuthLastLoginNotifyAddr,
       "hpicfUsrAuthUseLLDPData": hpicfUsrAuthUseLLDPData,
       "hpicfUsrAuthMacAuthPasswordEncrypted": hpicfUsrAuthMacAuthPasswordEncrypted,
       "hpicfUsrAuthPorts": hpicfUsrAuthPorts,
       "hpicfUsrAuthPortTable": hpicfUsrAuthPortTable,
       "hpicfUsrAuthPortEntry": hpicfUsrAuthPortEntry,
       "hpicfUsrAuthPortNumber": hpicfUsrAuthPortNumber,
       "hpicfUsrAuthWebAuthAdminStatus": hpicfUsrAuthWebAuthAdminStatus,
       "hpicfUsrAuthMacAuthAdminStatus": hpicfUsrAuthMacAuthAdminStatus,
       "hpicfUsrAuthPortReauthenticate": hpicfUsrAuthPortReauthenticate,
       "hpicfUsrAuthLMAAdminStatus": hpicfUsrAuthLMAAdminStatus,
       "hpicfUsrAuthLLDPBypassAdminStatus": hpicfUsrAuthLLDPBypassAdminStatus,
       "hpicfUsrAuthWebAuthConfig": hpicfUsrAuthWebAuthConfig,
       "hpicfUsrAuthWebAuthConfigTable": hpicfUsrAuthWebAuthConfigTable,
       "hpicfUsrAuthWebAuthConfigEntry": hpicfUsrAuthWebAuthConfigEntry,
       "hpicfUsrAuthWebAuthClientLimit": hpicfUsrAuthWebAuthClientLimit,
       "hpicfUsrAuthWebAuthClientMoves": hpicfUsrAuthWebAuthClientMoves,
       "hpicfUsrAuthWebAuthSSLState": hpicfUsrAuthWebAuthSSLState,
       "hpicfUsrAuthWebAuthRedirectUrl": hpicfUsrAuthWebAuthRedirectUrl,
       "hpicfUsrAuthWebAuthQuietPeriod": hpicfUsrAuthWebAuthQuietPeriod,
       "hpicfUsrAuthWebAuthServerTimeout": hpicfUsrAuthWebAuthServerTimeout,
       "hpicfUsrAuthWebAuthServerMaxReq": hpicfUsrAuthWebAuthServerMaxReq,
       "hpicfUsrAuthWebAuthMaxRetries": hpicfUsrAuthWebAuthMaxRetries,
       "hpicfUsrAuthWebAuthLogoffPeriod": hpicfUsrAuthWebAuthLogoffPeriod,
       "hpicfUsrAuthWebAuthReAuthPeriod": hpicfUsrAuthWebAuthReAuthPeriod,
       "hpicfUsrAuthWebAuthAuthVid": hpicfUsrAuthWebAuthAuthVid,
       "hpicfUsrAuthWebAuthUnauthVid": hpicfUsrAuthWebAuthUnauthVid,
       "hpicfUsrAuthWebAuthCacheCredentials": hpicfUsrAuthWebAuthCacheCredentials,
       "hpicfUsrAuthWebAuthCachedReauthPeriod": hpicfUsrAuthWebAuthCachedReauthPeriod,
       "hpicfUsrAuthWebAuthClientReauthenticateTable": hpicfUsrAuthWebAuthClientReauthenticateTable,
       "hpicfUsrAuthWebAuthClientReauthenticateEntry": hpicfUsrAuthWebAuthClientReauthenticateEntry,
       "hpicfUsrAuthWebAuthClientReauthenticateInterfaceIndex": hpicfUsrAuthWebAuthClientReauthenticateInterfaceIndex,
       "hpicfUsrAuthWebAuthClientReauthenticateMacAddress": hpicfUsrAuthWebAuthClientReauthenticateMacAddress,
       "hpicfUsrAuthWebAuthClientReauthenticate": hpicfUsrAuthWebAuthClientReauthenticate,
       "hpicfUsrAuthMacAuthConfig": hpicfUsrAuthMacAuthConfig,
       "hpicfUsrAuthMacAuthConfigTable": hpicfUsrAuthMacAuthConfigTable,
       "hpicfUsrAuthMacAuthConfigEntry": hpicfUsrAuthMacAuthConfigEntry,
       "hpicfUsrAuthMacAuthClientLimit": hpicfUsrAuthMacAuthClientLimit,
       "hpicfUsrAuthMacAuthClientMoves": hpicfUsrAuthMacAuthClientMoves,
       "hpicfUsrAuthMacAuthQuietPeriod": hpicfUsrAuthMacAuthQuietPeriod,
       "hpicfUsrAuthMacAuthServerTimeout": hpicfUsrAuthMacAuthServerTimeout,
       "hpicfUsrAuthMacAuthServerMaxReq": hpicfUsrAuthMacAuthServerMaxReq,
       "hpicfUsrAuthMacAuthLogoffPeriod": hpicfUsrAuthMacAuthLogoffPeriod,
       "hpicfUsrAuthMacAuthReAuthPeriod": hpicfUsrAuthMacAuthReAuthPeriod,
       "hpicfUsrAuthMacAuthAuthVid": hpicfUsrAuthMacAuthAuthVid,
       "hpicfUsrAuthMacAuthUnauthVid": hpicfUsrAuthMacAuthUnauthVid,
       "hpicfUsrAuthMacAuthCachedReauthPeriod": hpicfUsrAuthMacAuthCachedReauthPeriod,
       "hpicfUsrAuthMacAuthUnAuthPeriod": hpicfUsrAuthMacAuthUnAuthPeriod,
       "hpicfUsrAuthMacAuthMode": hpicfUsrAuthMacAuthMode,
       "hpicfUsrAuthMacPin": hpicfUsrAuthMacPin,
       "hpicfMacAuthRetainUnauthClients": hpicfMacAuthRetainUnauthClients,
       "hpicfUsrAuthMacAuthClientReauthenticateTable": hpicfUsrAuthMacAuthClientReauthenticateTable,
       "hpicfUsrAuthMacAuthClientReauthenticateEntry": hpicfUsrAuthMacAuthClientReauthenticateEntry,
       "hpicfUsrAuthMacAuthClientReauthenticateInterfaceIndex": hpicfUsrAuthMacAuthClientReauthenticateInterfaceIndex,
       "hpicfUsrAuthMacAuthClientReauthenticateMacAddress": hpicfUsrAuthMacAuthClientReauthenticateMacAddress,
       "hpicfUsrAuthMacAuthClientReauthenticate": hpicfUsrAuthMacAuthClientReauthenticate,
       "hpicfUsrAuthWebAuthStats": hpicfUsrAuthWebAuthStats,
       "hpicfUsrAuthWebAuthSessionStatsTable": hpicfUsrAuthWebAuthSessionStatsTable,
       "hpicfUsrAuthWebAuthSessionStatsEntry": hpicfUsrAuthWebAuthSessionStatsEntry,
       "hpicfUsrAuthWebAuthSessionMacAddr": hpicfUsrAuthWebAuthSessionMacAddr,
       "hpicfUsrAuthWebAuthSessionName": hpicfUsrAuthWebAuthSessionName,
       "hpicfUsrAuthWebAuthSessionState": hpicfUsrAuthWebAuthSessionState,
       "hpicfUsrAuthWebAuthSessionStateTime": hpicfUsrAuthWebAuthSessionStateTime,
       "hpicfUsrAuthWebAuthSessionAuthVid": hpicfUsrAuthWebAuthSessionAuthVid,
       "hpicfUsrAuthWebAuthSessionUnauthVid": hpicfUsrAuthWebAuthSessionUnauthVid,
       "hpicfUsrAuthWebAuthSessionTimeout": hpicfUsrAuthWebAuthSessionTimeout,
       "hpicfUsrAuthWebAuthSessionRole": hpicfUsrAuthWebAuthSessionRole,
       "hpicfUsrAuthMacAuthStats": hpicfUsrAuthMacAuthStats,
       "hpicfUsrAuthMacAuthSessionStatsTable": hpicfUsrAuthMacAuthSessionStatsTable,
       "hpicfUsrAuthMacAuthSessionStatsEntry": hpicfUsrAuthMacAuthSessionStatsEntry,
       "hpicfUsrAuthMacAuthSessionMacAddr": hpicfUsrAuthMacAuthSessionMacAddr,
       "hpicfUsrAuthMacAuthSessionState": hpicfUsrAuthMacAuthSessionState,
       "hpicfUsrAuthMacAuthSessionStateTime": hpicfUsrAuthMacAuthSessionStateTime,
       "hpicfUsrAuthMacAuthSessionAuthVid": hpicfUsrAuthMacAuthSessionAuthVid,
       "hpicfUsrAuthMacAuthSessionUnauthVid": hpicfUsrAuthMacAuthSessionUnauthVid,
       "hpicfUsrAuthMacAuthSessionTimeout": hpicfUsrAuthMacAuthSessionTimeout,
       "hpicfUsrAuthMacAuthSessionUsrNumberCnt": hpicfUsrAuthMacAuthSessionUsrNumberCnt,
       "hpicfUsrAuthMacAuthSessionName": hpicfUsrAuthMacAuthSessionName,
       "hpicfUsrAuthMacAuthSessionRole": hpicfUsrAuthMacAuthSessionRole,
       "hpicfUsrAuthConformance": hpicfUsrAuthConformance,
       "hpicfUsrAuthGroups": hpicfUsrAuthGroups,
       "hpicfUsrAuthSystemGroup": hpicfUsrAuthSystemGroup,
       "hpicfUsrAuthPortsGroup": hpicfUsrAuthPortsGroup,
       "hpicfUsrAuthWebAuthConfigGroup": hpicfUsrAuthWebAuthConfigGroup,
       "hpicfUsrAuthMacAuthConfigGroup": hpicfUsrAuthMacAuthConfigGroup,
       "hpicfUsrAuthWebAuthSessionStatsGroup": hpicfUsrAuthWebAuthSessionStatsGroup,
       "hpicfUsrAuthMacAuthSessionStatsGroup": hpicfUsrAuthMacAuthSessionStatsGroup,
       "hpicfUsrAuthWebAuthConfigGroup1": hpicfUsrAuthWebAuthConfigGroup1,
       "hpicfUsrAuthMacAuthConfigGroup1": hpicfUsrAuthMacAuthConfigGroup1,
       "hpicfUsrAuthMacAuthConfigGroup2": hpicfUsrAuthMacAuthConfigGroup2,
       "hpicfUsrAuthRedirectServerGroup": hpicfUsrAuthRedirectServerGroup,
       "hpicfUsrAuthWMAeWAServerGroup": hpicfUsrAuthWMAeWAServerGroup,
       "hpicfUsrAuthClientReauthenticateGroup": hpicfUsrAuthClientReauthenticateGroup,
       "hpicfUsrAuthMacAuthSessionStatsGroup1": hpicfUsrAuthMacAuthSessionStatsGroup1,
       "hpicfUsrAuthWebAuthSessionStatsGroup1": hpicfUsrAuthWebAuthSessionStatsGroup1,
       "hpicfUsrAuthLastLoginGroup": hpicfUsrAuthLastLoginGroup,
       "hpicfUsrAuthPortsGroup1": hpicfUsrAuthPortsGroup1,
       "hpicfUsrAuthCaptivePortalGroup": hpicfUsrAuthCaptivePortalGroup,
       "hpicfUsrAuthCaptivePortalProfileGroup": hpicfUsrAuthCaptivePortalProfileGroup,
       "hpicfUsrAuthWebAuthSessionStatsGroup2": hpicfUsrAuthWebAuthSessionStatsGroup2,
       "hpicfUsrAuthMacAuthSessionStatsGroup2": hpicfUsrAuthMacAuthSessionStatsGroup2,
       "hpicfUsrAuthPortsGroup2": hpicfUsrAuthPortsGroup2,
       "hpicfUsrAuthMacAuthConfigGroup3": hpicfUsrAuthMacAuthConfigGroup3,
       "hpicfUsrAuthCompliances": hpicfUsrAuthCompliances,
       "hpicfUsrAuthCompliance": hpicfUsrAuthCompliance,
       "hpicfUsrAuthCompliance1": hpicfUsrAuthCompliance1,
       "hpicfUsrAuthCompliance2": hpicfUsrAuthCompliance2,
       "hpicfUsrAuthCompliance3": hpicfUsrAuthCompliance3,
       "hpicfUsrAuthCompliance4": hpicfUsrAuthCompliance4,
       "hpicfUsrAuthCompliance5": hpicfUsrAuthCompliance5,
       "hpicfUsrAuthCompliance6": hpicfUsrAuthCompliance6,
       "hpicfUsrAuthCompliance7": hpicfUsrAuthCompliance7,
       "hpicfUsrAuthCompliance8": hpicfUsrAuthCompliance8,
       "hpicfUsrAuthCompliance9": hpicfUsrAuthCompliance9,
       "hpicfUsrAuthCompliance10": hpicfUsrAuthCompliance10,
       "hpicfUsrAuthCompliance11": hpicfUsrAuthCompliance11,
       "hpicfUsrAuthCompliance12": hpicfUsrAuthCompliance12,
       "hpicfUsrAuthCompliance13": hpicfUsrAuthCompliance13,
       "hpicfUsrAuthCompliance14": hpicfUsrAuthCompliance14,
       "hpicfUsrAuthCompliance15": hpicfUsrAuthCompliance15,
       "hpicfUsrAuthCompliance16": hpicfUsrAuthCompliance16,
       "hpicfUsrAuthNotifyConformance": hpicfUsrAuthNotifyConformance,
       "hpicfUsrAuthNotificationGroup": hpicfUsrAuthNotificationGroup,
       "hpicfNotifcationConfigDataGroup": hpicfNotifcationConfigDataGroup,
       "hpicfNotificationConfigDataGroup1": hpicfNotificationConfigDataGroup1,
       "hpicfUsrAuthMacGlobalConformance": hpicfUsrAuthMacGlobalConformance,
       "hpicfUsrAuthMacGroup": hpicfUsrAuthMacGroup,
       "hpicfUsrAuthMacGroup1": hpicfUsrAuthMacGroup1,
       "hpicfUsrAuthWebAuthAccessDeniedConformance": hpicfUsrAuthWebAuthAccessDeniedConformance,
       "hpicfUsrAuthWebAuthAccessDeniedGroup": hpicfUsrAuthWebAuthAccessDeniedGroup,
       "hpicfUsrAuthMacAuthUsrNumberConformance": hpicfUsrAuthMacAuthUsrNumberConformance,
       "hpicfUsrAuthMacAuthUsrNumberGroup": hpicfUsrAuthMacAuthUsrNumberGroup,
       "hpicfUsrAuthLastLogin": hpicfUsrAuthLastLogin,
       "hpicfUsrAuthLastLoginCurrentGeneration": hpicfUsrAuthLastLoginCurrentGeneration,
       "hpicfUsrAuthLastLoginTable": hpicfUsrAuthLastLoginTable,
       "hpicfUsrAuthLastLoginEntry": hpicfUsrAuthLastLoginEntry,
       "hpicfUsrAuthLastLoginIndex": hpicfUsrAuthLastLoginIndex,
       "hpicfUsrAuthLastLoginName": hpicfUsrAuthLastLoginName,
       "hpicfUsrAuthLastLoginPrivilege": hpicfUsrAuthLastLoginPrivilege,
       "hpicfUsrAuthLastLoginSuccTime": hpicfUsrAuthLastLoginSuccTime,
       "hpicfUsrAuthLastLoginSuccAddrType": hpicfUsrAuthLastLoginSuccAddrType,
       "hpicfUsrAuthLastLoginSuccAddr": hpicfUsrAuthLastLoginSuccAddr,
       "hpicfUsrAuthLastLoginUnsuccTime": hpicfUsrAuthLastLoginUnsuccTime,
       "hpicfUsrAuthLastLoginUnsuccCount": hpicfUsrAuthLastLoginUnsuccCount,
       "hpicfUsrAuthLastLoginGeneration": hpicfUsrAuthLastLoginGeneration,
       "hpicfUsrAuthLastLoginDeleteAll": hpicfUsrAuthLastLoginDeleteAll,
       "hpicfUsrAuthCaptivePortal": hpicfUsrAuthCaptivePortal,
       "hpicfUsrAuthCaptivePortalConfig": hpicfUsrAuthCaptivePortalConfig,
       "hpicfUsrAuthCaptivePortalConfigEnabled": hpicfUsrAuthCaptivePortalConfigEnabled,
       "hpicfUsrAuthCaptivePortalUrlHashKey": hpicfUsrAuthCaptivePortalUrlHashKey,
       "hpicfUsrAuthCaptivePortalUrlHashKeyEncrypted": hpicfUsrAuthCaptivePortalUrlHashKeyEncrypted,
       "hpicfUsrAuthCaptivePortalProfileTable": hpicfUsrAuthCaptivePortalProfileTable,
       "hpicfUsrAuthCaptivePortalProfileEntry": hpicfUsrAuthCaptivePortalProfileEntry,
       "hpicfUsrAuthCaptivePortalProfileName": hpicfUsrAuthCaptivePortalProfileName,
       "hpicfUsrAuthCaptivePortalProfileRowStatus": hpicfUsrAuthCaptivePortalProfileRowStatus,
       "hpicfUsrAuthCaptivePortalProfileType": hpicfUsrAuthCaptivePortalProfileType,
       "hpicfUsrAuthCaptivePortalProfileRedirectUrl": hpicfUsrAuthCaptivePortalProfileRedirectUrl}
)
