# SNMP MIB module (TIARA-NETWORKS-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIARA-NETWORKS-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:42 2024
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
 NotificationType,
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
    "NotificationType",
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

(tiaraMgmt,) = mibBuilder.importSymbols(
    "TIARA-NETWORKS-SMI",
    "tiaraMgmt")


# MODULE-IDENTITY

tiaraSystemMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1)
)
tiaraSystemMib.setRevisions(
        ("1900-08-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SystemObjects_ObjectIdentity = ObjectIdentity
systemObjects = _SystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 1)
)
_SysIpAddr_Type = IpAddress
_SysIpAddr_Object = MibScalar
sysIpAddr = _SysIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 1, 1),
    _SysIpAddr_Type()
)
sysIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIpAddr.setStatus("current")
_SysNetMask_Type = IpAddress
_SysNetMask_Object = MibScalar
sysNetMask = _SysNetMask_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 1, 2),
    _SysNetMask_Type()
)
sysNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysNetMask.setStatus("current")
_SysBroadcast_Type = IpAddress
_SysBroadcast_Object = MibScalar
sysBroadcast = _SysBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 1, 3),
    _SysBroadcast_Type()
)
sysBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBroadcast.setStatus("current")


class _SysVersion_Type(DisplayString):
    """Custom type sysVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SysVersion_Type.__name__ = "DisplayString"
_SysVersion_Object = MibScalar
sysVersion = _SysVersion_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 1, 4),
    _SysVersion_Type()
)
sysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVersion.setStatus("current")


class _SysHostName_Type(DisplayString):
    """Custom type sysHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SysHostName_Type.__name__ = "DisplayString"
_SysHostName_Object = MibScalar
sysHostName = _SysHostName_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 1, 6),
    _SysHostName_Type()
)
sysHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysHostName.setStatus("current")


class _SysDomainName_Type(DisplayString):
    """Custom type sysDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SysDomainName_Type.__name__ = "DisplayString"
_SysDomainName_Object = MibScalar
sysDomainName = _SysDomainName_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 1, 7),
    _SysDomainName_Type()
)
sysDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDomainName.setStatus("current")


class _SysAlarmStatus_Type(Integer32):
    """Custom type sysAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("major", 3),
          ("minor", 2))
    )


_SysAlarmStatus_Type.__name__ = "Integer32"
_SysAlarmStatus_Object = MibScalar
sysAlarmStatus = _SysAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 1, 8),
    _SysAlarmStatus_Type()
)
sysAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAlarmStatus.setStatus("current")


class _SysReset_Type(Integer32):
    """Custom type sysReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_SysReset_Type.__name__ = "Integer32"
_SysReset_Object = MibScalar
sysReset = _SysReset_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 1, 10),
    _SysReset_Type()
)
sysReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysReset.setStatus("current")


class _SysDateTime_Type(OctetString):
    """Custom type sysDateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_SysDateTime_Type.__name__ = "OctetString"
_SysDateTime_Object = MibScalar
sysDateTime = _SysDateTime_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 1, 11),
    _SysDateTime_Type()
)
sysDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDateTime.setStatus("current")
_ArpClearAtTable_Type = Integer32
_ArpClearAtTable_Object = MibScalar
arpClearAtTable = _ArpClearAtTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 1, 12),
    _ArpClearAtTable_Type()
)
arpClearAtTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpClearAtTable.setStatus("current")
_IpClearRouteTable_Type = Integer32
_IpClearRouteTable_Object = MibScalar
ipClearRouteTable = _IpClearRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 1, 13),
    _IpClearRouteTable_Type()
)
ipClearRouteTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipClearRouteTable.setStatus("current")
_DnsGroup_ObjectIdentity = ObjectIdentity
dnsGroup = _DnsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 2)
)


class _DnsEnable_Type(Integer32):
    """Custom type dnsEnable based on Integer32"""
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


_DnsEnable_Type.__name__ = "Integer32"
_DnsEnable_Object = MibScalar
dnsEnable = _DnsEnable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 2, 1),
    _DnsEnable_Type()
)
dnsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsEnable.setStatus("current")
_DnsServerTable_Object = MibTable
dnsServerTable = _DnsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dnsServerTable.setStatus("current")
_DnsServerEntry_Object = MibTableRow
dnsServerEntry = _DnsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 2, 2, 1)
)
dnsServerEntry.setIndexNames(
    (0, "TIARA-NETWORKS-SYSTEM-MIB", "dnsServerAddr"),
)
if mibBuilder.loadTexts:
    dnsServerEntry.setStatus("current")


class _DnsServerEntryType_Type(Integer32):
    """Custom type dnsServerEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("other", 3),
          ("primary", 2))
    )


_DnsServerEntryType_Type.__name__ = "Integer32"
_DnsServerEntryType_Object = MibTableColumn
dnsServerEntryType = _DnsServerEntryType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 2, 2, 1, 1),
    _DnsServerEntryType_Type()
)
dnsServerEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServerEntryType.setStatus("current")
_DnsServerAddr_Type = IpAddress
_DnsServerAddr_Object = MibTableColumn
dnsServerAddr = _DnsServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 2, 2, 1, 2),
    _DnsServerAddr_Type()
)
dnsServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServerAddr.setStatus("current")
_SystemEnableNotification_ObjectIdentity = ObjectIdentity
systemEnableNotification = _SystemEnableNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 3)
)


class _EnableSysShutDownNotification_Type(TruthValue):
    """Custom type enableSysShutDownNotification based on TruthValue"""


_EnableSysShutDownNotification_Object = MibScalar
enableSysShutDownNotification = _EnableSysShutDownNotification_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 3, 1),
    _EnableSysShutDownNotification_Type()
)
enableSysShutDownNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableSysShutDownNotification.setStatus("current")


class _EnableUserLoginNotification_Type(TruthValue):
    """Custom type enableUserLoginNotification based on TruthValue"""


_EnableUserLoginNotification_Object = MibScalar
enableUserLoginNotification = _EnableUserLoginNotification_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 3, 2),
    _EnableUserLoginNotification_Type()
)
enableUserLoginNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableUserLoginNotification.setStatus("current")


class _EnableUserLogOffNotification_Type(TruthValue):
    """Custom type enableUserLogOffNotification based on TruthValue"""


_EnableUserLogOffNotification_Object = MibScalar
enableUserLogOffNotification = _EnableUserLogOffNotification_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 3, 3),
    _EnableUserLogOffNotification_Type()
)
enableUserLogOffNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableUserLogOffNotification.setStatus("current")


class _EnableUserLoginFailNotification_Type(TruthValue):
    """Custom type enableUserLoginFailNotification based on TruthValue"""


_EnableUserLoginFailNotification_Object = MibScalar
enableUserLoginFailNotification = _EnableUserLoginFailNotification_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 3, 4),
    _EnableUserLoginFailNotification_Type()
)
enableUserLoginFailNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableUserLoginFailNotification.setStatus("current")
_SystemNotifications_ObjectIdentity = ObjectIdentity
systemNotifications = _SystemNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 4)
)
_UserAdminGroup_ObjectIdentity = ObjectIdentity
userAdminGroup = _UserAdminGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 5)
)


class _UserName_Type(DisplayString):
    """Custom type userName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_UserName_Type.__name__ = "DisplayString"
_UserName_Object = MibScalar
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 5, 1),
    _UserName_Type()
)
userName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userName.setStatus("current")
_EthernetFailOverGroup_ObjectIdentity = ObjectIdentity
ethernetFailOverGroup = _EthernetFailOverGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 6)
)
_TiaraEthernetFailOverTable_Object = MibTable
tiaraEthernetFailOverTable = _TiaraEthernetFailOverTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    tiaraEthernetFailOverTable.setStatus("current")
_TiaraEthernetFailOverEntry_Object = MibTableRow
tiaraEthernetFailOverEntry = _TiaraEthernetFailOverEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 6, 1, 1)
)
tiaraEthernetFailOverEntry.setIndexNames(
    (0, "TIARA-NETWORKS-SYSTEM-MIB", "tiaraFailOverIndex"),
)
if mibBuilder.loadTexts:
    tiaraEthernetFailOverEntry.setStatus("current")
_TiaraFailOverIndex_Type = Integer32
_TiaraFailOverIndex_Object = MibTableColumn
tiaraFailOverIndex = _TiaraFailOverIndex_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 6, 1, 1, 1),
    _TiaraFailOverIndex_Type()
)
tiaraFailOverIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tiaraFailOverIndex.setStatus("current")
_TiaraFailOverEnable_Type = TruthValue
_TiaraFailOverEnable_Object = MibTableColumn
tiaraFailOverEnable = _TiaraFailOverEnable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 6, 1, 1, 2),
    _TiaraFailOverEnable_Type()
)
tiaraFailOverEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tiaraFailOverEnable.setStatus("current")


class _TiaraHoldDownTime_Type(Integer32):
    """Custom type tiaraHoldDownTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 900),
    )


_TiaraHoldDownTime_Type.__name__ = "Integer32"
_TiaraHoldDownTime_Object = MibTableColumn
tiaraHoldDownTime = _TiaraHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 6, 1, 1, 3),
    _TiaraHoldDownTime_Type()
)
tiaraHoldDownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tiaraHoldDownTime.setStatus("current")
_FailOverEnableNotifications_ObjectIdentity = ObjectIdentity
failOverEnableNotifications = _FailOverEnableNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 7)
)


class _EnableFailOverNotification_Type(TruthValue):
    """Custom type enableFailOverNotification based on TruthValue"""


_EnableFailOverNotification_Object = MibScalar
enableFailOverNotification = _EnableFailOverNotification_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 7, 1),
    _EnableFailOverNotification_Type()
)
enableFailOverNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableFailOverNotification.setStatus("current")


class _EnableFailOverFailNotification_Type(TruthValue):
    """Custom type enableFailOverFailNotification based on TruthValue"""


_EnableFailOverFailNotification_Object = MibScalar
enableFailOverFailNotification = _EnableFailOverFailNotification_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 7, 2),
    _EnableFailOverFailNotification_Type()
)
enableFailOverFailNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableFailOverFailNotification.setStatus("current")
_FailOverNotifications_ObjectIdentity = ObjectIdentity
failOverNotifications = _FailOverNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 8)
)
_VlanGroup_ObjectIdentity = ObjectIdentity
vlanGroup = _VlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 9)
)
_VlanType_Type = Integer32
_VlanType_Object = MibScalar
vlanType = _VlanType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 9, 1),
    _VlanType_Type()
)
vlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanType.setStatus("current")
_VlanStatsTable_Object = MibTable
vlanStatsTable = _VlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 9, 2)
)
if mibBuilder.loadTexts:
    vlanStatsTable.setStatus("current")
_VlanStatsEntry_Object = MibTableRow
vlanStatsEntry = _VlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 9, 2, 1)
)
vlanStatsEntry.setIndexNames(
    (0, "TIARA-NETWORKS-SYSTEM-MIB", "vlanTag"),
)
if mibBuilder.loadTexts:
    vlanStatsEntry.setStatus("current")
_VlanTag_Type = Integer32
_VlanTag_Object = MibTableColumn
vlanTag = _VlanTag_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 9, 2, 1, 1),
    _VlanTag_Type()
)
vlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTag.setStatus("current")
_VlanInterfaceList_Type = DisplayString
_VlanInterfaceList_Object = MibTableColumn
vlanInterfaceList = _VlanInterfaceList_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 9, 2, 1, 2),
    _VlanInterfaceList_Type()
)
vlanInterfaceList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanInterfaceList.setStatus("current")
_VlanTxPkts_Type = Counter32
_VlanTxPkts_Object = MibTableColumn
vlanTxPkts = _VlanTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 9, 2, 1, 3),
    _VlanTxPkts_Type()
)
vlanTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTxPkts.setStatus("current")
_VlanRxPkts_Type = Counter32
_VlanRxPkts_Object = MibTableColumn
vlanRxPkts = _VlanRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 9, 2, 1, 4),
    _VlanRxPkts_Type()
)
vlanRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanRxPkts.setStatus("current")
_VlanDroppedPkts_Type = Counter32
_VlanDroppedPkts_Object = MibTableColumn
vlanDroppedPkts = _VlanDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 9, 2, 1, 5),
    _VlanDroppedPkts_Type()
)
vlanDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanDroppedPkts.setStatus("current")

# Managed Objects groups


# Notification objects

shutDownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 4, 0, 1)
)
if mibBuilder.loadTexts:
    shutDownNotification.setStatus(
        ""
    )

userLoginNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 4, 0, 2)
)
userLoginNotification.setObjects(
    ("TIARA-NETWORKS-SYSTEM-MIB", "userName")
)
if mibBuilder.loadTexts:
    userLoginNotification.setStatus(
        ""
    )

userLogOffNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 4, 0, 3)
)
userLogOffNotification.setObjects(
    ("TIARA-NETWORKS-SYSTEM-MIB", "userName")
)
if mibBuilder.loadTexts:
    userLogOffNotification.setStatus(
        ""
    )

userLoginFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 4, 0, 4)
)
userLoginFailNotification.setObjects(
    ("TIARA-NETWORKS-SYSTEM-MIB", "userName")
)
if mibBuilder.loadTexts:
    userLoginFailNotification.setStatus(
        ""
    )

failOverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 8, 0, 1)
)
failOverNotification.setObjects(
    ("TIARA-NETWORKS-SYSTEM-MIB", "tiaraFailOverIndex")
)
if mibBuilder.loadTexts:
    failOverNotification.setStatus(
        ""
    )

failOverFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3174, 2, 1, 8, 0, 2)
)
failOverFailNotification.setObjects(
    ("TIARA-NETWORKS-SYSTEM-MIB", "tiaraFailOverIndex")
)
if mibBuilder.loadTexts:
    failOverFailNotification.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIARA-NETWORKS-SYSTEM-MIB",
    **{"tiaraSystemMib": tiaraSystemMib,
       "systemObjects": systemObjects,
       "sysIpAddr": sysIpAddr,
       "sysNetMask": sysNetMask,
       "sysBroadcast": sysBroadcast,
       "sysVersion": sysVersion,
       "sysHostName": sysHostName,
       "sysDomainName": sysDomainName,
       "sysAlarmStatus": sysAlarmStatus,
       "sysReset": sysReset,
       "sysDateTime": sysDateTime,
       "arpClearAtTable": arpClearAtTable,
       "ipClearRouteTable": ipClearRouteTable,
       "dnsGroup": dnsGroup,
       "dnsEnable": dnsEnable,
       "dnsServerTable": dnsServerTable,
       "dnsServerEntry": dnsServerEntry,
       "dnsServerEntryType": dnsServerEntryType,
       "dnsServerAddr": dnsServerAddr,
       "systemEnableNotification": systemEnableNotification,
       "enableSysShutDownNotification": enableSysShutDownNotification,
       "enableUserLoginNotification": enableUserLoginNotification,
       "enableUserLogOffNotification": enableUserLogOffNotification,
       "enableUserLoginFailNotification": enableUserLoginFailNotification,
       "systemNotifications": systemNotifications,
       "shutDownNotification": shutDownNotification,
       "userLoginNotification": userLoginNotification,
       "userLogOffNotification": userLogOffNotification,
       "userLoginFailNotification": userLoginFailNotification,
       "userAdminGroup": userAdminGroup,
       "userName": userName,
       "ethernetFailOverGroup": ethernetFailOverGroup,
       "tiaraEthernetFailOverTable": tiaraEthernetFailOverTable,
       "tiaraEthernetFailOverEntry": tiaraEthernetFailOverEntry,
       "tiaraFailOverIndex": tiaraFailOverIndex,
       "tiaraFailOverEnable": tiaraFailOverEnable,
       "tiaraHoldDownTime": tiaraHoldDownTime,
       "failOverEnableNotifications": failOverEnableNotifications,
       "enableFailOverNotification": enableFailOverNotification,
       "enableFailOverFailNotification": enableFailOverFailNotification,
       "failOverNotifications": failOverNotifications,
       "failOverNotification": failOverNotification,
       "failOverFailNotification": failOverFailNotification,
       "vlanGroup": vlanGroup,
       "vlanType": vlanType,
       "vlanStatsTable": vlanStatsTable,
       "vlanStatsEntry": vlanStatsEntry,
       "vlanTag": vlanTag,
       "vlanInterfaceList": vlanInterfaceList,
       "vlanTxPkts": vlanTxPkts,
       "vlanRxPkts": vlanRxPkts,
       "vlanDroppedPkts": vlanDroppedPkts}
)
