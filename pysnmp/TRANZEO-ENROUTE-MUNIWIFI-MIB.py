# SNMP MIB module (TRANZEO-ENROUTE-MUNIWIFI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENROUTE-245-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:38 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

enRoute = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 24350)
)
enRoute.setRevisions(
        ("2008-07-01 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Version_ObjectIdentity = ObjectIdentity
version = _Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 1)
)
_VersionDriver80211_Type = OctetString
_VersionDriver80211_Object = MibScalar
versionDriver80211 = _VersionDriver80211_Object(
    (1, 3, 6, 1, 4, 1, 24350, 1, 1),
    _VersionDriver80211_Type()
)
versionDriver80211.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionDriver80211.setStatus("current")
_VersionFirmware_Type = OctetString
_VersionFirmware_Object = MibScalar
versionFirmware = _VersionFirmware_Object(
    (1, 3, 6, 1, 4, 1, 24350, 1, 2),
    _VersionFirmware_Type()
)
versionFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionFirmware.setStatus("current")
_VersionLoaded_profile_Type = OctetString
_VersionLoaded_profile_Object = MibScalar
versionLoaded_profile = _VersionLoaded_profile_Object(
    (1, 3, 6, 1, 4, 1, 24350, 1, 3),
    _VersionLoaded_profile_Type()
)
versionLoaded_profile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionLoaded_profile.setStatus("current")
_VersionMcm_Type = OctetString
_VersionMcm_Object = MibScalar
versionMcm = _VersionMcm_Object(
    (1, 3, 6, 1, 4, 1, 24350, 1, 4),
    _VersionMcm_Type()
)
versionMcm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionMcm.setStatus("current")
_VersionPatches_Type = OctetString
_VersionPatches_Object = MibScalar
versionPatches = _VersionPatches_Object(
    (1, 3, 6, 1, 4, 1, 24350, 1, 5),
    _VersionPatches_Type()
)
versionPatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionPatches.setStatus("current")
_VersionQos_Type = OctetString
_VersionQos_Object = MibScalar
versionQos = _VersionQos_Object(
    (1, 3, 6, 1, 4, 1, 24350, 1, 6),
    _VersionQos_Type()
)
versionQos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionQos.setStatus("current")
_VersionRelease_Type = OctetString
_VersionRelease_Object = MibScalar
versionRelease = _VersionRelease_Object(
    (1, 3, 6, 1, 4, 1, 24350, 1, 7),
    _VersionRelease_Type()
)
versionRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionRelease.setStatus("current")
_Sys_ObjectIdentity = ObjectIdentity
sys = _Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2)
)
_SysApply_ObjectIdentity = ObjectIdentity
sysApply = _SysApply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 1)
)
_SysApplyEffect_Type = OctetString
_SysApplyEffect_Object = MibScalar
sysApplyEffect = _SysApplyEffect_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 1, 1),
    _SysApplyEffect_Type()
)
sysApplyEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplyEffect.setStatus("current")
_SysApplyTime_Type = Integer32
_SysApplyTime_Object = MibScalar
sysApplyTime = _SysApplyTime_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 1, 2),
    _SysApplyTime_Type()
)
sysApplyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplyTime.setStatus("current")
_SysDev_ObjectIdentity = ObjectIdentity
sysDev = _SysDev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 2)
)
_SysDevBattery_ObjectIdentity = ObjectIdentity
sysDevBattery = _SysDevBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 2, 1)
)
_SysDevBatteryEnable_Type = OctetString
_SysDevBatteryEnable_Object = MibScalar
sysDevBatteryEnable = _SysDevBatteryEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 2, 1, 1),
    _SysDevBatteryEnable_Type()
)
sysDevBatteryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevBatteryEnable.setStatus("current")
_SysDevBatteryInstalled_Type = OctetString
_SysDevBatteryInstalled_Object = MibScalar
sysDevBatteryInstalled = _SysDevBatteryInstalled_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 2, 1, 2),
    _SysDevBatteryInstalled_Type()
)
sysDevBatteryInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevBatteryInstalled.setStatus("current")
_SysDevLed_ObjectIdentity = ObjectIdentity
sysDevLed = _SysDevLed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 2, 2)
)
_SysDevLedEnable_Type = OctetString
_SysDevLedEnable_Object = MibScalar
sysDevLedEnable = _SysDevLedEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 2, 2, 1),
    _SysDevLedEnable_Type()
)
sysDevLedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevLedEnable.setStatus("current")
_SysDevPoe_ObjectIdentity = ObjectIdentity
sysDevPoe = _SysDevPoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 2, 3)
)
_SysDevPoeEnable_Type = OctetString
_SysDevPoeEnable_Object = MibScalar
sysDevPoeEnable = _SysDevPoeEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 2, 3, 1),
    _SysDevPoeEnable_Type()
)
sysDevPoeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevPoeEnable.setStatus("current")
_SysDevPoeInstalled_Type = OctetString
_SysDevPoeInstalled_Object = MibScalar
sysDevPoeInstalled = _SysDevPoeInstalled_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 2, 3, 2),
    _SysDevPoeInstalled_Type()
)
sysDevPoeInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevPoeInstalled.setStatus("current")
_SysDevPoeVoltage_Type = OctetString
_SysDevPoeVoltage_Object = MibScalar
sysDevPoeVoltage = _SysDevPoeVoltage_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 2, 3, 3),
    _SysDevPoeVoltage_Type()
)
sysDevPoeVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevPoeVoltage.setStatus("current")
_SysDevWlan_ObjectIdentity = ObjectIdentity
sysDevWlan = _SysDevWlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 2, 4)
)
_SysDevWlanCountry_Type = Integer32
_SysDevWlanCountry_Object = MibScalar
sysDevWlanCountry = _SysDevWlanCountry_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 2, 4, 1),
    _SysDevWlanCountry_Type()
)
sysDevWlanCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevWlanCountry.setStatus("current")
_SysDhcp_ObjectIdentity = ObjectIdentity
sysDhcp = _SysDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 3)
)
_SysDhcpArgs_Type = OctetString
_SysDhcpArgs_Object = MibScalar
sysDhcpArgs = _SysDhcpArgs_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 3, 1),
    _SysDhcpArgs_Type()
)
sysDhcpArgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDhcpArgs.setStatus("current")
_SysDhcpEnableserver_Type = OctetString
_SysDhcpEnableserver_Object = MibScalar
sysDhcpEnableserver = _SysDhcpEnableserver_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 3, 2),
    _SysDhcpEnableserver_Type()
)
sysDhcpEnableserver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpEnableserver.setStatus("current")
_SysDhcpRelay_ObjectIdentity = ObjectIdentity
sysDhcpRelay = _SysDhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 3, 3)
)
_SysDhcpRelayAgent_ObjectIdentity = ObjectIdentity
sysDhcpRelayAgent = _SysDhcpRelayAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 3, 3, 1)
)
_SysDhcpRelayAgentBase_Type = OctetString
_SysDhcpRelayAgentBase_Object = MibScalar
sysDhcpRelayAgentBase = _SysDhcpRelayAgentBase_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 3, 3, 1, 1),
    _SysDhcpRelayAgentBase_Type()
)
sysDhcpRelayAgentBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpRelayAgentBase.setStatus("current")
_SysDhcpRelayArgs_Type = OctetString
_SysDhcpRelayArgs_Object = MibScalar
sysDhcpRelayArgs = _SysDhcpRelayArgs_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 3, 3, 2),
    _SysDhcpRelayArgs_Type()
)
sysDhcpRelayArgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpRelayArgs.setStatus("current")
_SysDhcpRelayArpnumbc_Type = Integer32
_SysDhcpRelayArpnumbc_Object = MibScalar
sysDhcpRelayArpnumbc = _SysDhcpRelayArpnumbc_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 3, 3, 3),
    _SysDhcpRelayArpnumbc_Type()
)
sysDhcpRelayArpnumbc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpRelayArpnumbc.setStatus("current")
_SysDhcpRelayBindretries_Type = Integer32
_SysDhcpRelayBindretries_Object = MibScalar
sysDhcpRelayBindretries = _SysDhcpRelayBindretries_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 3, 3, 4),
    _SysDhcpRelayBindretries_Type()
)
sysDhcpRelayBindretries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpRelayBindretries.setStatus("current")
_SysDhcpRelayEnable_Type = OctetString
_SysDhcpRelayEnable_Object = MibScalar
sysDhcpRelayEnable = _SysDhcpRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 3, 3, 5),
    _SysDhcpRelayEnable_Type()
)
sysDhcpRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpRelayEnable.setStatus("current")
_SysDhcpRelayExtrahosts_Type = OctetString
_SysDhcpRelayExtrahosts_Object = MibScalar
sysDhcpRelayExtrahosts = _SysDhcpRelayExtrahosts_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 3, 3, 6),
    _SysDhcpRelayExtrahosts_Type()
)
sysDhcpRelayExtrahosts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpRelayExtrahosts.setStatus("current")
_SysDhcpRelayGateway_Type = OctetString
_SysDhcpRelayGateway_Object = MibScalar
sysDhcpRelayGateway = _SysDhcpRelayGateway_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 3, 3, 7),
    _SysDhcpRelayGateway_Type()
)
sysDhcpRelayGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpRelayGateway.setStatus("current")
_SysDhcpRelayImr_ObjectIdentity = ObjectIdentity
sysDhcpRelayImr = _SysDhcpRelayImr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 3, 3, 8)
)
_SysDhcpRelayImrNumbc_Type = Integer32
_SysDhcpRelayImrNumbc_Object = MibScalar
sysDhcpRelayImrNumbc = _SysDhcpRelayImrNumbc_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 3, 3, 8, 1),
    _SysDhcpRelayImrNumbc_Type()
)
sysDhcpRelayImrNumbc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpRelayImrNumbc.setStatus("current")
_SysDhcpRelayProxy_Type = OctetString
_SysDhcpRelayProxy_Object = MibScalar
sysDhcpRelayProxy = _SysDhcpRelayProxy_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 3, 3, 9),
    _SysDhcpRelayProxy_Type()
)
sysDhcpRelayProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpRelayProxy.setStatus("current")
_SysDhcpRelayServer_Type = OctetString
_SysDhcpRelayServer_Object = MibScalar
sysDhcpRelayServer = _SysDhcpRelayServer_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 3, 3, 10),
    _SysDhcpRelayServer_Type()
)
sysDhcpRelayServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpRelayServer.setStatus("current")
_SysDhcpRelayStalecheckinterval_Type = Integer32
_SysDhcpRelayStalecheckinterval_Object = MibScalar
sysDhcpRelayStalecheckinterval = _SysDhcpRelayStalecheckinterval_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 3, 3, 11),
    _SysDhcpRelayStalecheckinterval_Type()
)
sysDhcpRelayStalecheckinterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpRelayStalecheckinterval.setStatus("current")
_SysDhcpRelayStatic_ObjectIdentity = ObjectIdentity
sysDhcpRelayStatic = _SysDhcpRelayStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 3, 3, 12)
)
_SysDhcpRelayStaticBegin_Type = OctetString
_SysDhcpRelayStaticBegin_Object = MibScalar
sysDhcpRelayStaticBegin = _SysDhcpRelayStaticBegin_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 3, 3, 12, 1),
    _SysDhcpRelayStaticBegin_Type()
)
sysDhcpRelayStaticBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpRelayStaticBegin.setStatus("current")
_SysDhcpRelayStaticEnable_Type = OctetString
_SysDhcpRelayStaticEnable_Object = MibScalar
sysDhcpRelayStaticEnable = _SysDhcpRelayStaticEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 3, 3, 12, 2),
    _SysDhcpRelayStaticEnable_Type()
)
sysDhcpRelayStaticEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpRelayStaticEnable.setStatus("current")
_SysDhcpRelayStaticEnd_Type = OctetString
_SysDhcpRelayStaticEnd_Object = MibScalar
sysDhcpRelayStaticEnd = _SysDhcpRelayStaticEnd_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 3, 3, 12, 3),
    _SysDhcpRelayStaticEnd_Type()
)
sysDhcpRelayStaticEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpRelayStaticEnd.setStatus("current")
_SysDhcpRelaySubnet_Type = OctetString
_SysDhcpRelaySubnet_Object = MibScalar
sysDhcpRelaySubnet = _SysDhcpRelaySubnet_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 3, 3, 13),
    _SysDhcpRelaySubnet_Type()
)
sysDhcpRelaySubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpRelaySubnet.setStatus("current")
_SysDhcpRelayTunnel_ObjectIdentity = ObjectIdentity
sysDhcpRelayTunnel = _SysDhcpRelayTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 3, 3, 14)
)
_SysDhcpRelayTunnelEndpoint_Type = OctetString
_SysDhcpRelayTunnelEndpoint_Object = MibScalar
sysDhcpRelayTunnelEndpoint = _SysDhcpRelayTunnelEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 3, 3, 14, 1),
    _SysDhcpRelayTunnelEndpoint_Type()
)
sysDhcpRelayTunnelEndpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpRelayTunnelEndpoint.setStatus("current")
_SysDhcpRelayTunnelKeepalive_Type = Integer32
_SysDhcpRelayTunnelKeepalive_Object = MibScalar
sysDhcpRelayTunnelKeepalive = _SysDhcpRelayTunnelKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 3, 3, 14, 2),
    _SysDhcpRelayTunnelKeepalive_Type()
)
sysDhcpRelayTunnelKeepalive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpRelayTunnelKeepalive.setStatus("current")
_SysDhcpRelayTunnelTimeoutfactor_Type = Integer32
_SysDhcpRelayTunnelTimeoutfactor_Object = MibScalar
sysDhcpRelayTunnelTimeoutfactor = _SysDhcpRelayTunnelTimeoutfactor_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 3, 3, 14, 3),
    _SysDhcpRelayTunnelTimeoutfactor_Type()
)
sysDhcpRelayTunnelTimeoutfactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDhcpRelayTunnelTimeoutfactor.setStatus("current")
_SysDns_ObjectIdentity = ObjectIdentity
sysDns = _SysDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 4)
)
_SysDnsServers_Type = OctetString
_SysDnsServers_Object = MibScalar
sysDnsServers = _SysDnsServers_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 4, 1),
    _SysDnsServers_Type()
)
sysDnsServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDnsServers.setStatus("current")
_SysDnsUpdatestyle_Type = OctetString
_SysDnsUpdatestyle_Object = MibScalar
sysDnsUpdatestyle = _SysDnsUpdatestyle_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 4, 2),
    _SysDnsUpdatestyle_Type()
)
sysDnsUpdatestyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDnsUpdatestyle.setStatus("current")
_SysDnsproxy_ObjectIdentity = ObjectIdentity
sysDnsproxy = _SysDnsproxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 5)
)
_SysDnsproxyEnable_Type = OctetString
_SysDnsproxyEnable_Object = MibScalar
sysDnsproxyEnable = _SysDnsproxyEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 5, 1),
    _SysDnsproxyEnable_Type()
)
sysDnsproxyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDnsproxyEnable.setStatus("current")
_SysDnsproxyHosts_Type = OctetString
_SysDnsproxyHosts_Object = MibScalar
sysDnsproxyHosts = _SysDnsproxyHosts_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 5, 2),
    _SysDnsproxyHosts_Type()
)
sysDnsproxyHosts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDnsproxyHosts.setStatus("current")
_SysDomain_Type = OctetString
_SysDomain_Object = MibScalar
sysDomain = _SysDomain_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 6),
    _SysDomain_Type()
)
sysDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDomain.setStatus("current")
_SysGui_ObjectIdentity = ObjectIdentity
sysGui = _SysGui_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 7)
)
_SysGuiUpgrade_ObjectIdentity = ObjectIdentity
sysGuiUpgrade = _SysGuiUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 7, 1)
)
_SysGuiUpgradeForce_Type = OctetString
_SysGuiUpgradeForce_Object = MibScalar
sysGuiUpgradeForce = _SysGuiUpgradeForce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 7, 1, 1),
    _SysGuiUpgradeForce_Type()
)
sysGuiUpgradeForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGuiUpgradeForce.setStatus("current")
_SysHostname_Type = OctetString
_SysHostname_Object = MibScalar
sysHostname = _SysHostname_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 8),
    _SysHostname_Type()
)
sysHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysHostname.setStatus("current")
_SysHosts_ObjectIdentity = ObjectIdentity
sysHosts = _SysHosts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 9)
)
_SysHostsNms_Type = OctetString
_SysHostsNms_Object = MibScalar
sysHostsNms = _SysHostsNms_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 9, 1),
    _SysHostsNms_Type()
)
sysHostsNms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysHostsNms.setStatus("current")
_SysId_ObjectIdentity = ObjectIdentity
sysId = _SysId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 10)
)
_SysIdLanprefix_Type = OctetString
_SysIdLanprefix_Object = MibScalar
sysIdLanprefix = _SysIdLanprefix_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 10, 1),
    _SysIdLanprefix_Type()
)
sysIdLanprefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIdLanprefix.setStatus("current")
_SysIdMesh_Type = OctetString
_SysIdMesh_Object = MibScalar
sysIdMesh = _SysIdMesh_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 10, 2),
    _SysIdMesh_Type()
)
sysIdMesh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIdMesh.setStatus("current")
_SysIdMeshprefix_Type = OctetString
_SysIdMeshprefix_Object = MibScalar
sysIdMeshprefix = _SysIdMeshprefix_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 10, 3),
    _SysIdMeshprefix_Type()
)
sysIdMeshprefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIdMeshprefix.setStatus("current")
_SysIdNode_Type = OctetString
_SysIdNode_Object = MibScalar
sysIdNode = _SysIdNode_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 10, 4),
    _SysIdNode_Type()
)
sysIdNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIdNode.setStatus("current")
_SysImplicit_ObjectIdentity = ObjectIdentity
sysImplicit = _SysImplicit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 11)
)
_SysImplicitEnable_Type = OctetString
_SysImplicitEnable_Object = MibScalar
sysImplicitEnable = _SysImplicitEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 11, 1),
    _SysImplicitEnable_Type()
)
sysImplicitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysImplicitEnable.setStatus("current")
_SysInfo_ObjectIdentity = ObjectIdentity
sysInfo = _SysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 12)
)
_SysInfoCluster_Type = OctetString
_SysInfoCluster_Object = MibScalar
sysInfoCluster = _SysInfoCluster_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 12, 1),
    _SysInfoCluster_Type()
)
sysInfoCluster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysInfoCluster.setStatus("current")
_SysL2_ObjectIdentity = ObjectIdentity
sysL2 = _SysL2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 13)
)
_SysL2Bridge_ObjectIdentity = ObjectIdentity
sysL2Bridge = _SysL2Bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 13, 1)
)
_SysL2BridgeEnable_Type = OctetString
_SysL2BridgeEnable_Object = MibScalar
sysL2BridgeEnable = _SysL2BridgeEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 13, 1, 1),
    _SysL2BridgeEnable_Type()
)
sysL2BridgeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysL2BridgeEnable.setStatus("current")
_SysL2Clientmacfwd_Type = OctetString
_SysL2Clientmacfwd_Object = MibScalar
sysL2Clientmacfwd = _SysL2Clientmacfwd_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 13, 2),
    _SysL2Clientmacfwd_Type()
)
sysL2Clientmacfwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysL2Clientmacfwd.setStatus("current")
_SysL2Hideinternal_ObjectIdentity = ObjectIdentity
sysL2Hideinternal = _SysL2Hideinternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 13, 3)
)
_SysL2HideinternalEnable_Type = OctetString
_SysL2HideinternalEnable_Object = MibScalar
sysL2HideinternalEnable = _SysL2HideinternalEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 13, 3, 1),
    _SysL2HideinternalEnable_Type()
)
sysL2HideinternalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysL2HideinternalEnable.setStatus("current")
_SysL2HideinternalGateway_ObjectIdentity = ObjectIdentity
sysL2HideinternalGateway = _SysL2HideinternalGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 13, 3, 2)
)
_SysL2HideinternalGatewayAllow_ObjectIdentity = ObjectIdentity
sysL2HideinternalGatewayAllow = _SysL2HideinternalGatewayAllow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 13, 3, 2, 1)
)
_SysL2HideinternalGatewayAllowRelaydhcp_Type = OctetString
_SysL2HideinternalGatewayAllowRelaydhcp_Object = MibScalar
sysL2HideinternalGatewayAllowRelaydhcp = _SysL2HideinternalGatewayAllowRelaydhcp_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 13, 3, 2, 1, 1),
    _SysL2HideinternalGatewayAllowRelaydhcp_Type()
)
sysL2HideinternalGatewayAllowRelaydhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysL2HideinternalGatewayAllowRelaydhcp.setStatus("current")
_SysL2HideinternalGatewayDeny_ObjectIdentity = ObjectIdentity
sysL2HideinternalGatewayDeny = _SysL2HideinternalGatewayDeny_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 13, 3, 2, 2)
)
_SysL2HideinternalGatewayDenyAll_Type = OctetString
_SysL2HideinternalGatewayDenyAll_Object = MibScalar
sysL2HideinternalGatewayDenyAll = _SysL2HideinternalGatewayDenyAll_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 13, 3, 2, 2, 1),
    _SysL2HideinternalGatewayDenyAll_Type()
)
sysL2HideinternalGatewayDenyAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysL2HideinternalGatewayDenyAll.setStatus("current")
_SysL2HideinternalGatewayDenyMesh_Type = OctetString
_SysL2HideinternalGatewayDenyMesh_Object = MibScalar
sysL2HideinternalGatewayDenyMesh = _SysL2HideinternalGatewayDenyMesh_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 13, 3, 2, 2, 2),
    _SysL2HideinternalGatewayDenyMesh_Type()
)
sysL2HideinternalGatewayDenyMesh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysL2HideinternalGatewayDenyMesh.setStatus("current")
_SysLocation_ObjectIdentity = ObjectIdentity
sysLocation = _SysLocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 14)
)
_SysLocationGps_ObjectIdentity = ObjectIdentity
sysLocationGps = _SysLocationGps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 14, 1)
)
_SysLocationGpsAltitude_Type = OctetString
_SysLocationGpsAltitude_Object = MibScalar
sysLocationGpsAltitude = _SysLocationGpsAltitude_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 14, 1, 1),
    _SysLocationGpsAltitude_Type()
)
sysLocationGpsAltitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocationGpsAltitude.setStatus("current")
_SysLocationGpsLatitude_Type = OctetString
_SysLocationGpsLatitude_Object = MibScalar
sysLocationGpsLatitude = _SysLocationGpsLatitude_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 14, 1, 2),
    _SysLocationGpsLatitude_Type()
)
sysLocationGpsLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocationGpsLatitude.setStatus("current")
_SysLocationGpsLongitude_Type = OctetString
_SysLocationGpsLongitude_Object = MibScalar
sysLocationGpsLongitude = _SysLocationGpsLongitude_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 14, 1, 3),
    _SysLocationGpsLongitude_Type()
)
sysLocationGpsLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocationGpsLongitude.setStatus("current")
_SysLocationPostal_Type = OctetString
_SysLocationPostal_Object = MibScalar
sysLocationPostal = _SysLocationPostal_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 14, 2),
    _SysLocationPostal_Type()
)
sysLocationPostal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocationPostal.setStatus("current")
_SysMainstub_ObjectIdentity = ObjectIdentity
sysMainstub = _SysMainstub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 15)
)
_SysMainstubIf_Type = OctetString
_SysMainstubIf_Object = MibScalar
sysMainstubIf = _SysMainstubIf_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 15, 1),
    _SysMainstubIf_Type()
)
sysMainstubIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMainstubIf.setStatus("current")
_SysMainstubProxyarp_Type = OctetString
_SysMainstubProxyarp_Object = MibScalar
sysMainstubProxyarp = _SysMainstubProxyarp_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 15, 2),
    _SysMainstubProxyarp_Type()
)
sysMainstubProxyarp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMainstubProxyarp.setStatus("current")
_SysMonitor_ObjectIdentity = ObjectIdentity
sysMonitor = _SysMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 16)
)
_SysMonitorHealth_ObjectIdentity = ObjectIdentity
sysMonitorHealth = _SysMonitorHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 16, 1)
)
_SysMonitorHealthEnable_Type = OctetString
_SysMonitorHealthEnable_Object = MibScalar
sysMonitorHealthEnable = _SysMonitorHealthEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 16, 1, 1),
    _SysMonitorHealthEnable_Type()
)
sysMonitorHealthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMonitorHealthEnable.setStatus("current")
_SysMonitorHealthHost_Type = OctetString
_SysMonitorHealthHost_Object = MibScalar
sysMonitorHealthHost = _SysMonitorHealthHost_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 16, 1, 2),
    _SysMonitorHealthHost_Type()
)
sysMonitorHealthHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMonitorHealthHost.setStatus("current")
_SysNat_ObjectIdentity = ObjectIdentity
sysNat = _SysNat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 17)
)
_SysNatEnable_Type = OctetString
_SysNatEnable_Object = MibScalar
sysNatEnable = _SysNatEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 17, 1),
    _SysNatEnable_Type()
)
sysNatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNatEnable.setStatus("current")
_SysNetbios_ObjectIdentity = ObjectIdentity
sysNetbios = _SysNetbios_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 18)
)
_SysNetbiosServers_Type = OctetString
_SysNetbiosServers_Object = MibScalar
sysNetbiosServers = _SysNetbiosServers_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 18, 1),
    _SysNetbiosServers_Type()
)
sysNetbiosServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNetbiosServers.setStatus("current")
_SysNets_ObjectIdentity = ObjectIdentity
sysNets = _SysNets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 19)
)
_SysNetsExternal_ObjectIdentity = ObjectIdentity
sysNetsExternal = _SysNetsExternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 19, 1)
)
_SysNetsExternalCombined_Type = OctetString
_SysNetsExternalCombined_Object = MibScalar
sysNetsExternalCombined = _SysNetsExternalCombined_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 19, 1, 1),
    _SysNetsExternalCombined_Type()
)
sysNetsExternalCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysNetsExternalCombined.setStatus("current")
_SysNetsExternalDefault_Type = OctetString
_SysNetsExternalDefault_Object = MibScalar
sysNetsExternalDefault = _SysNetsExternalDefault_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 19, 1, 2),
    _SysNetsExternalDefault_Type()
)
sysNetsExternalDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysNetsExternalDefault.setStatus("current")
_SysNetsExternalExtra_Type = OctetString
_SysNetsExternalExtra_Object = MibScalar
sysNetsExternalExtra = _SysNetsExternalExtra_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 19, 1, 3),
    _SysNetsExternalExtra_Type()
)
sysNetsExternalExtra.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNetsExternalExtra.setStatus("current")
_SysNetsInternal_ObjectIdentity = ObjectIdentity
sysNetsInternal = _SysNetsInternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 19, 2)
)
_SysNetsInternalCombined_Type = OctetString
_SysNetsInternalCombined_Object = MibScalar
sysNetsInternalCombined = _SysNetsInternalCombined_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 19, 2, 1),
    _SysNetsInternalCombined_Type()
)
sysNetsInternalCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysNetsInternalCombined.setStatus("current")
_SysNetsInternalDefault_Type = OctetString
_SysNetsInternalDefault_Object = MibScalar
sysNetsInternalDefault = _SysNetsInternalDefault_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 19, 2, 2),
    _SysNetsInternalDefault_Type()
)
sysNetsInternalDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysNetsInternalDefault.setStatus("current")
_SysNetsInternalExtra_Type = OctetString
_SysNetsInternalExtra_Object = MibScalar
sysNetsInternalExtra = _SysNetsInternalExtra_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 19, 2, 3),
    _SysNetsInternalExtra_Type()
)
sysNetsInternalExtra.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNetsInternalExtra.setStatus("current")
_SysNetsInternalFlexipdefault_Type = OctetString
_SysNetsInternalFlexipdefault_Object = MibScalar
sysNetsInternalFlexipdefault = _SysNetsInternalFlexipdefault_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 19, 2, 4),
    _SysNetsInternalFlexipdefault_Type()
)
sysNetsInternalFlexipdefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNetsInternalFlexipdefault.setStatus("current")
_SysOrganization_ObjectIdentity = ObjectIdentity
sysOrganization = _SysOrganization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 20)
)
_SysOrganizationCity_Type = OctetString
_SysOrganizationCity_Object = MibScalar
sysOrganizationCity = _SysOrganizationCity_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 20, 1),
    _SysOrganizationCity_Type()
)
sysOrganizationCity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysOrganizationCity.setStatus("current")
_SysOrganizationCountry_Type = OctetString
_SysOrganizationCountry_Object = MibScalar
sysOrganizationCountry = _SysOrganizationCountry_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 20, 2),
    _SysOrganizationCountry_Type()
)
sysOrganizationCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysOrganizationCountry.setStatus("current")
_SysOrganizationName_Type = OctetString
_SysOrganizationName_Object = MibScalar
sysOrganizationName = _SysOrganizationName_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 20, 3),
    _SysOrganizationName_Type()
)
sysOrganizationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysOrganizationName.setStatus("current")
_SysOrganizationState_Type = OctetString
_SysOrganizationState_Object = MibScalar
sysOrganizationState = _SysOrganizationState_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 20, 4),
    _SysOrganizationState_Type()
)
sysOrganizationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysOrganizationState.setStatus("current")
_SysPassword_ObjectIdentity = ObjectIdentity
sysPassword = _SysPassword_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 21)
)
_SysPasswordAdmin_Type = OctetString
_SysPasswordAdmin_Object = MibScalar
sysPasswordAdmin = _SysPasswordAdmin_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 21, 1),
    _SysPasswordAdmin_Type()
)
sysPasswordAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPasswordAdmin.setStatus("current")
_SysPasswordMonitor_Type = OctetString
_SysPasswordMonitor_Object = MibScalar
sysPasswordMonitor = _SysPasswordMonitor_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 21, 2),
    _SysPasswordMonitor_Type()
)
sysPasswordMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPasswordMonitor.setStatus("current")
_SysPlatform_Type = OctetString
_SysPlatform_Object = MibScalar
sysPlatform = _SysPlatform_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 22),
    _SysPlatform_Type()
)
sysPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPlatform.setStatus("current")
_SysProvisioning_ObjectIdentity = ObjectIdentity
sysProvisioning = _SysProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 23)
)
_SysProvisioningEnable_Type = OctetString
_SysProvisioningEnable_Object = MibScalar
sysProvisioningEnable = _SysProvisioningEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 23, 1),
    _SysProvisioningEnable_Type()
)
sysProvisioningEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysProvisioningEnable.setStatus("current")
_SysRouting_ObjectIdentity = ObjectIdentity
sysRouting = _SysRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 24)
)
_SysRoutingOspf_Type = OctetString
_SysRoutingOspf_Object = MibScalar
sysRoutingOspf = _SysRoutingOspf_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 24, 1),
    _SysRoutingOspf_Type()
)
sysRoutingOspf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRoutingOspf.setStatus("current")
_SysRoutingRip_Type = OctetString
_SysRoutingRip_Object = MibScalar
sysRoutingRip = _SysRoutingRip_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 24, 2),
    _SysRoutingRip_Type()
)
sysRoutingRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRoutingRip.setStatus("current")
_SysScheme_Type = OctetString
_SysScheme_Object = MibScalar
sysScheme = _SysScheme_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 25),
    _SysScheme_Type()
)
sysScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysScheme.setStatus("current")
_SysShell_ObjectIdentity = ObjectIdentity
sysShell = _SysShell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 26)
)
_SysShellTimeout_Type = Integer32
_SysShellTimeout_Object = MibScalar
sysShellTimeout = _SysShellTimeout_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 26, 1),
    _SysShellTimeout_Type()
)
sysShellTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysShellTimeout.setStatus("current")
_SysSnmp_ObjectIdentity = ObjectIdentity
sysSnmp = _SysSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 27)
)
_SysSnmpCommunity_ObjectIdentity = ObjectIdentity
sysSnmpCommunity = _SysSnmpCommunity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 27, 1)
)
_SysSnmpCommunityRo_Type = OctetString
_SysSnmpCommunityRo_Object = MibScalar
sysSnmpCommunityRo = _SysSnmpCommunityRo_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 27, 1, 1),
    _SysSnmpCommunityRo_Type()
)
sysSnmpCommunityRo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnmpCommunityRo.setStatus("current")
_SysSnmpCommunityRw_Type = OctetString
_SysSnmpCommunityRw_Object = MibScalar
sysSnmpCommunityRw = _SysSnmpCommunityRw_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 27, 1, 2),
    _SysSnmpCommunityRw_Type()
)
sysSnmpCommunityRw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnmpCommunityRw.setStatus("current")
_SysSnmpCommunityTrap_Type = OctetString
_SysSnmpCommunityTrap_Object = MibScalar
sysSnmpCommunityTrap = _SysSnmpCommunityTrap_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 27, 1, 3),
    _SysSnmpCommunityTrap_Type()
)
sysSnmpCommunityTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnmpCommunityTrap.setStatus("current")
_SysSnmpContact_Type = OctetString
_SysSnmpContact_Object = MibScalar
sysSnmpContact = _SysSnmpContact_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 27, 2),
    _SysSnmpContact_Type()
)
sysSnmpContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnmpContact.setStatus("current")
_SysSnmpLocation_Type = OctetString
_SysSnmpLocation_Object = MibScalar
sysSnmpLocation = _SysSnmpLocation_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 27, 3),
    _SysSnmpLocation_Type()
)
sysSnmpLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnmpLocation.setStatus("current")
_SysSnmpPort_Type = Integer32
_SysSnmpPort_Object = MibScalar
sysSnmpPort = _SysSnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 27, 4),
    _SysSnmpPort_Type()
)
sysSnmpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnmpPort.setStatus("current")
_SysSnmpTrap_ObjectIdentity = ObjectIdentity
sysSnmpTrap = _SysSnmpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 27, 5)
)
_SysSnmpTrapHost_Type = OctetString
_SysSnmpTrapHost_Object = MibScalar
sysSnmpTrapHost = _SysSnmpTrapHost_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 27, 5, 1),
    _SysSnmpTrapHost_Type()
)
sysSnmpTrapHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnmpTrapHost.setStatus("current")
_SysSplash_ObjectIdentity = ObjectIdentity
sysSplash = _SysSplash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28)
)
_SysSplashAuth_ObjectIdentity = ObjectIdentity
sysSplashAuth = _SysSplashAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 1)
)
_SysSplashAuthServer_ObjectIdentity = ObjectIdentity
sysSplashAuthServer = _SysSplashAuthServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 1, 1)
)
_SysSplashAuthServerWlan1_ObjectIdentity = ObjectIdentity
sysSplashAuthServerWlan1 = _SysSplashAuthServerWlan1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 1, 1, 1)
)
_SysSplashAuthServerWlan1Enable_Type = OctetString
_SysSplashAuthServerWlan1Enable_Object = MibScalar
sysSplashAuthServerWlan1Enable = _SysSplashAuthServerWlan1Enable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 1, 1, 1, 1),
    _SysSplashAuthServerWlan1Enable_Type()
)
sysSplashAuthServerWlan1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashAuthServerWlan1Enable.setStatus("current")
_SysSplashAuthServerWlan1Host_Type = OctetString
_SysSplashAuthServerWlan1Host_Object = MibScalar
sysSplashAuthServerWlan1Host = _SysSplashAuthServerWlan1Host_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 1, 1, 1, 2),
    _SysSplashAuthServerWlan1Host_Type()
)
sysSplashAuthServerWlan1Host.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashAuthServerWlan1Host.setStatus("current")
_SysSplashAuthServerWlan1Port_Type = Integer32
_SysSplashAuthServerWlan1Port_Object = MibScalar
sysSplashAuthServerWlan1Port = _SysSplashAuthServerWlan1Port_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 1, 1, 1, 3),
    _SysSplashAuthServerWlan1Port_Type()
)
sysSplashAuthServerWlan1Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashAuthServerWlan1Port.setStatus("current")
_SysSplashAuthServerWlan1Secret_Type = OctetString
_SysSplashAuthServerWlan1Secret_Object = MibScalar
sysSplashAuthServerWlan1Secret = _SysSplashAuthServerWlan1Secret_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 1, 1, 1, 4),
    _SysSplashAuthServerWlan1Secret_Type()
)
sysSplashAuthServerWlan1Secret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashAuthServerWlan1Secret.setStatus("current")
_SysSplashAuthServerWlan2_ObjectIdentity = ObjectIdentity
sysSplashAuthServerWlan2 = _SysSplashAuthServerWlan2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 1, 1, 2)
)
_SysSplashAuthServerWlan2Enable_Type = OctetString
_SysSplashAuthServerWlan2Enable_Object = MibScalar
sysSplashAuthServerWlan2Enable = _SysSplashAuthServerWlan2Enable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 1, 1, 2, 1),
    _SysSplashAuthServerWlan2Enable_Type()
)
sysSplashAuthServerWlan2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashAuthServerWlan2Enable.setStatus("current")
_SysSplashAuthServerWlan2Host_Type = OctetString
_SysSplashAuthServerWlan2Host_Object = MibScalar
sysSplashAuthServerWlan2Host = _SysSplashAuthServerWlan2Host_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 1, 1, 2, 2),
    _SysSplashAuthServerWlan2Host_Type()
)
sysSplashAuthServerWlan2Host.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashAuthServerWlan2Host.setStatus("current")
_SysSplashAuthServerWlan2Port_Type = Integer32
_SysSplashAuthServerWlan2Port_Object = MibScalar
sysSplashAuthServerWlan2Port = _SysSplashAuthServerWlan2Port_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 1, 1, 2, 3),
    _SysSplashAuthServerWlan2Port_Type()
)
sysSplashAuthServerWlan2Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashAuthServerWlan2Port.setStatus("current")
_SysSplashAuthServerWlan2Secret_Type = OctetString
_SysSplashAuthServerWlan2Secret_Object = MibScalar
sysSplashAuthServerWlan2Secret = _SysSplashAuthServerWlan2Secret_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 1, 1, 2, 4),
    _SysSplashAuthServerWlan2Secret_Type()
)
sysSplashAuthServerWlan2Secret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashAuthServerWlan2Secret.setStatus("current")
_SysSplashAuthServerWlan3_ObjectIdentity = ObjectIdentity
sysSplashAuthServerWlan3 = _SysSplashAuthServerWlan3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 1, 1, 3)
)
_SysSplashAuthServerWlan3Enable_Type = OctetString
_SysSplashAuthServerWlan3Enable_Object = MibScalar
sysSplashAuthServerWlan3Enable = _SysSplashAuthServerWlan3Enable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 1, 1, 3, 1),
    _SysSplashAuthServerWlan3Enable_Type()
)
sysSplashAuthServerWlan3Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashAuthServerWlan3Enable.setStatus("current")
_SysSplashAuthServerWlan3Host_Type = OctetString
_SysSplashAuthServerWlan3Host_Object = MibScalar
sysSplashAuthServerWlan3Host = _SysSplashAuthServerWlan3Host_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 1, 1, 3, 2),
    _SysSplashAuthServerWlan3Host_Type()
)
sysSplashAuthServerWlan3Host.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashAuthServerWlan3Host.setStatus("current")
_SysSplashAuthServerWlan3Port_Type = Integer32
_SysSplashAuthServerWlan3Port_Object = MibScalar
sysSplashAuthServerWlan3Port = _SysSplashAuthServerWlan3Port_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 1, 1, 3, 3),
    _SysSplashAuthServerWlan3Port_Type()
)
sysSplashAuthServerWlan3Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashAuthServerWlan3Port.setStatus("current")
_SysSplashAuthServerWlan3Secret_Type = OctetString
_SysSplashAuthServerWlan3Secret_Object = MibScalar
sysSplashAuthServerWlan3Secret = _SysSplashAuthServerWlan3Secret_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 1, 1, 3, 4),
    _SysSplashAuthServerWlan3Secret_Type()
)
sysSplashAuthServerWlan3Secret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashAuthServerWlan3Secret.setStatus("current")
_SysSplashAuthServerWlan4_ObjectIdentity = ObjectIdentity
sysSplashAuthServerWlan4 = _SysSplashAuthServerWlan4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 1, 1, 4)
)
_SysSplashAuthServerWlan4Enable_Type = OctetString
_SysSplashAuthServerWlan4Enable_Object = MibScalar
sysSplashAuthServerWlan4Enable = _SysSplashAuthServerWlan4Enable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 1, 1, 4, 1),
    _SysSplashAuthServerWlan4Enable_Type()
)
sysSplashAuthServerWlan4Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashAuthServerWlan4Enable.setStatus("current")
_SysSplashAuthServerWlan4Host_Type = OctetString
_SysSplashAuthServerWlan4Host_Object = MibScalar
sysSplashAuthServerWlan4Host = _SysSplashAuthServerWlan4Host_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 1, 1, 4, 2),
    _SysSplashAuthServerWlan4Host_Type()
)
sysSplashAuthServerWlan4Host.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashAuthServerWlan4Host.setStatus("current")
_SysSplashAuthServerWlan4Port_Type = Integer32
_SysSplashAuthServerWlan4Port_Object = MibScalar
sysSplashAuthServerWlan4Port = _SysSplashAuthServerWlan4Port_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 1, 1, 4, 3),
    _SysSplashAuthServerWlan4Port_Type()
)
sysSplashAuthServerWlan4Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashAuthServerWlan4Port.setStatus("current")
_SysSplashAuthServerWlan4Secret_Type = OctetString
_SysSplashAuthServerWlan4Secret_Object = MibScalar
sysSplashAuthServerWlan4Secret = _SysSplashAuthServerWlan4Secret_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 1, 1, 4, 4),
    _SysSplashAuthServerWlan4Secret_Type()
)
sysSplashAuthServerWlan4Secret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashAuthServerWlan4Secret.setStatus("current")
_SysSplashBypasshosts_Type = OctetString
_SysSplashBypasshosts_Object = MibScalar
sysSplashBypasshosts = _SysSplashBypasshosts_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 2),
    _SysSplashBypasshosts_Type()
)
sysSplashBypasshosts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashBypasshosts.setStatus("current")
_SysSplashEnable_ObjectIdentity = ObjectIdentity
sysSplashEnable = _SysSplashEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 3)
)
_SysSplashEnableWlan1_Type = OctetString
_SysSplashEnableWlan1_Object = MibScalar
sysSplashEnableWlan1 = _SysSplashEnableWlan1_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 3, 1),
    _SysSplashEnableWlan1_Type()
)
sysSplashEnableWlan1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashEnableWlan1.setStatus("current")
_SysSplashEnableWlan2_Type = OctetString
_SysSplashEnableWlan2_Object = MibScalar
sysSplashEnableWlan2 = _SysSplashEnableWlan2_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 3, 2),
    _SysSplashEnableWlan2_Type()
)
sysSplashEnableWlan2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashEnableWlan2.setStatus("current")
_SysSplashEnableWlan3_Type = OctetString
_SysSplashEnableWlan3_Object = MibScalar
sysSplashEnableWlan3 = _SysSplashEnableWlan3_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 3, 3),
    _SysSplashEnableWlan3_Type()
)
sysSplashEnableWlan3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashEnableWlan3.setStatus("current")
_SysSplashEnableWlan4_Type = OctetString
_SysSplashEnableWlan4_Object = MibScalar
sysSplashEnableWlan4 = _SysSplashEnableWlan4_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 3, 4),
    _SysSplashEnableWlan4_Type()
)
sysSplashEnableWlan4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashEnableWlan4.setStatus("current")
_SysSplashExternal_Type = OctetString
_SysSplashExternal_Object = MibScalar
sysSplashExternal = _SysSplashExternal_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 4),
    _SysSplashExternal_Type()
)
sysSplashExternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashExternal.setStatus("current")
_SysSplashInternal_Type = OctetString
_SysSplashInternal_Object = MibScalar
sysSplashInternal = _SysSplashInternal_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 5),
    _SysSplashInternal_Type()
)
sysSplashInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSplashInternal.setStatus("current")
_SysSplashTrustedmacs_Type = OctetString
_SysSplashTrustedmacs_Object = MibScalar
sysSplashTrustedmacs = _SysSplashTrustedmacs_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 6),
    _SysSplashTrustedmacs_Type()
)
sysSplashTrustedmacs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashTrustedmacs.setStatus("current")
_SysSplashUrl_ObjectIdentity = ObjectIdentity
sysSplashUrl = _SysSplashUrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 7)
)
_SysSplashUrlWlan1_ObjectIdentity = ObjectIdentity
sysSplashUrlWlan1 = _SysSplashUrlWlan1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 7, 1)
)
_SysSplashUrlWlan1Error_Type = OctetString
_SysSplashUrlWlan1Error_Object = MibScalar
sysSplashUrlWlan1Error = _SysSplashUrlWlan1Error_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 7, 1, 1),
    _SysSplashUrlWlan1Error_Type()
)
sysSplashUrlWlan1Error.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashUrlWlan1Error.setStatus("current")
_SysSplashUrlWlan1Fail_Type = OctetString
_SysSplashUrlWlan1Fail_Object = MibScalar
sysSplashUrlWlan1Fail = _SysSplashUrlWlan1Fail_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 7, 1, 2),
    _SysSplashUrlWlan1Fail_Type()
)
sysSplashUrlWlan1Fail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashUrlWlan1Fail.setStatus("current")
_SysSplashUrlWlan1Login_Type = OctetString
_SysSplashUrlWlan1Login_Object = MibScalar
sysSplashUrlWlan1Login = _SysSplashUrlWlan1Login_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 7, 1, 3),
    _SysSplashUrlWlan1Login_Type()
)
sysSplashUrlWlan1Login.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashUrlWlan1Login.setStatus("current")
_SysSplashUrlWlan1Success_Type = OctetString
_SysSplashUrlWlan1Success_Object = MibScalar
sysSplashUrlWlan1Success = _SysSplashUrlWlan1Success_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 7, 1, 4),
    _SysSplashUrlWlan1Success_Type()
)
sysSplashUrlWlan1Success.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashUrlWlan1Success.setStatus("current")
_SysSplashUrlWlan2_ObjectIdentity = ObjectIdentity
sysSplashUrlWlan2 = _SysSplashUrlWlan2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 7, 2)
)
_SysSplashUrlWlan2Error_Type = OctetString
_SysSplashUrlWlan2Error_Object = MibScalar
sysSplashUrlWlan2Error = _SysSplashUrlWlan2Error_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 7, 2, 1),
    _SysSplashUrlWlan2Error_Type()
)
sysSplashUrlWlan2Error.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashUrlWlan2Error.setStatus("current")
_SysSplashUrlWlan2Fail_Type = OctetString
_SysSplashUrlWlan2Fail_Object = MibScalar
sysSplashUrlWlan2Fail = _SysSplashUrlWlan2Fail_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 7, 2, 2),
    _SysSplashUrlWlan2Fail_Type()
)
sysSplashUrlWlan2Fail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashUrlWlan2Fail.setStatus("current")
_SysSplashUrlWlan2Login_Type = OctetString
_SysSplashUrlWlan2Login_Object = MibScalar
sysSplashUrlWlan2Login = _SysSplashUrlWlan2Login_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 7, 2, 3),
    _SysSplashUrlWlan2Login_Type()
)
sysSplashUrlWlan2Login.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashUrlWlan2Login.setStatus("current")
_SysSplashUrlWlan2Success_Type = OctetString
_SysSplashUrlWlan2Success_Object = MibScalar
sysSplashUrlWlan2Success = _SysSplashUrlWlan2Success_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 7, 2, 4),
    _SysSplashUrlWlan2Success_Type()
)
sysSplashUrlWlan2Success.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashUrlWlan2Success.setStatus("current")
_SysSplashUrlWlan3_ObjectIdentity = ObjectIdentity
sysSplashUrlWlan3 = _SysSplashUrlWlan3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 7, 3)
)
_SysSplashUrlWlan3Error_Type = OctetString
_SysSplashUrlWlan3Error_Object = MibScalar
sysSplashUrlWlan3Error = _SysSplashUrlWlan3Error_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 7, 3, 1),
    _SysSplashUrlWlan3Error_Type()
)
sysSplashUrlWlan3Error.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashUrlWlan3Error.setStatus("current")
_SysSplashUrlWlan3Fail_Type = OctetString
_SysSplashUrlWlan3Fail_Object = MibScalar
sysSplashUrlWlan3Fail = _SysSplashUrlWlan3Fail_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 7, 3, 2),
    _SysSplashUrlWlan3Fail_Type()
)
sysSplashUrlWlan3Fail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashUrlWlan3Fail.setStatus("current")
_SysSplashUrlWlan3Login_Type = OctetString
_SysSplashUrlWlan3Login_Object = MibScalar
sysSplashUrlWlan3Login = _SysSplashUrlWlan3Login_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 7, 3, 3),
    _SysSplashUrlWlan3Login_Type()
)
sysSplashUrlWlan3Login.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashUrlWlan3Login.setStatus("current")
_SysSplashUrlWlan3Success_Type = OctetString
_SysSplashUrlWlan3Success_Object = MibScalar
sysSplashUrlWlan3Success = _SysSplashUrlWlan3Success_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 7, 3, 4),
    _SysSplashUrlWlan3Success_Type()
)
sysSplashUrlWlan3Success.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashUrlWlan3Success.setStatus("current")
_SysSplashUrlWlan4_ObjectIdentity = ObjectIdentity
sysSplashUrlWlan4 = _SysSplashUrlWlan4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 7, 4)
)
_SysSplashUrlWlan4Error_Type = OctetString
_SysSplashUrlWlan4Error_Object = MibScalar
sysSplashUrlWlan4Error = _SysSplashUrlWlan4Error_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 7, 4, 1),
    _SysSplashUrlWlan4Error_Type()
)
sysSplashUrlWlan4Error.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashUrlWlan4Error.setStatus("current")
_SysSplashUrlWlan4Fail_Type = OctetString
_SysSplashUrlWlan4Fail_Object = MibScalar
sysSplashUrlWlan4Fail = _SysSplashUrlWlan4Fail_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 7, 4, 2),
    _SysSplashUrlWlan4Fail_Type()
)
sysSplashUrlWlan4Fail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashUrlWlan4Fail.setStatus("current")
_SysSplashUrlWlan4Login_Type = OctetString
_SysSplashUrlWlan4Login_Object = MibScalar
sysSplashUrlWlan4Login = _SysSplashUrlWlan4Login_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 7, 4, 3),
    _SysSplashUrlWlan4Login_Type()
)
sysSplashUrlWlan4Login.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashUrlWlan4Login.setStatus("current")
_SysSplashUrlWlan4Success_Type = OctetString
_SysSplashUrlWlan4Success_Object = MibScalar
sysSplashUrlWlan4Success = _SysSplashUrlWlan4Success_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 28, 7, 4, 4),
    _SysSplashUrlWlan4Success_Type()
)
sysSplashUrlWlan4Success.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSplashUrlWlan4Success.setStatus("current")
_SysTime_ObjectIdentity = ObjectIdentity
sysTime = _SysTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 29)
)
_SysTimeRfc868_ObjectIdentity = ObjectIdentity
sysTimeRfc868 = _SysTimeRfc868_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 2, 29, 1)
)
_SysTimeRfc868Server_Type = OctetString
_SysTimeRfc868Server_Object = MibScalar
sysTimeRfc868Server = _SysTimeRfc868Server_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 29, 1, 1),
    _SysTimeRfc868Server_Type()
)
sysTimeRfc868Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeRfc868Server.setStatus("current")
_SysTimeSyncdelay_Type = Integer32
_SysTimeSyncdelay_Object = MibScalar
sysTimeSyncdelay = _SysTimeSyncdelay_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 29, 2),
    _SysTimeSyncdelay_Type()
)
sysTimeSyncdelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeSyncdelay.setStatus("current")
_SysUnits_Type = OctetString
_SysUnits_Object = MibScalar
sysUnits = _SysUnits_Object(
    (1, 3, 6, 1, 4, 1, 24350, 2, 30),
    _SysUnits_Type()
)
sysUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysUnits.setStatus("current")
_Firewall_ObjectIdentity = ObjectIdentity
firewall = _Firewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 3)
)
_FirewallConntrack_ObjectIdentity = ObjectIdentity
firewallConntrack = _FirewallConntrack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 3, 1)
)
_FirewallConntrackConnlimit_ObjectIdentity = ObjectIdentity
firewallConntrackConnlimit = _FirewallConntrackConnlimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 3, 1, 1)
)
_FirewallConntrackConnlimitConnections_Type = Integer32
_FirewallConntrackConnlimitConnections_Object = MibScalar
firewallConntrackConnlimitConnections = _FirewallConntrackConnlimitConnections_Object(
    (1, 3, 6, 1, 4, 1, 24350, 3, 1, 1, 1),
    _FirewallConntrackConnlimitConnections_Type()
)
firewallConntrackConnlimitConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallConntrackConnlimitConnections.setStatus("current")
_FirewallConntrackConnlimitEnable_Type = OctetString
_FirewallConntrackConnlimitEnable_Object = MibScalar
firewallConntrackConnlimitEnable = _FirewallConntrackConnlimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 3, 1, 1, 2),
    _FirewallConntrackConnlimitEnable_Type()
)
firewallConntrackConnlimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallConntrackConnlimitEnable.setStatus("current")
_FirewallConntrackTablesize_Type = Integer32
_FirewallConntrackTablesize_Object = MibScalar
firewallConntrackTablesize = _FirewallConntrackTablesize_Object(
    (1, 3, 6, 1, 4, 1, 24350, 3, 1, 2),
    _FirewallConntrackTablesize_Type()
)
firewallConntrackTablesize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallConntrackTablesize.setStatus("current")
_FirewallConntrackTcptimeoutestablished_Type = Integer32
_FirewallConntrackTcptimeoutestablished_Object = MibScalar
firewallConntrackTcptimeoutestablished = _FirewallConntrackTcptimeoutestablished_Object(
    (1, 3, 6, 1, 4, 1, 24350, 3, 1, 3),
    _FirewallConntrackTcptimeoutestablished_Type()
)
firewallConntrackTcptimeoutestablished.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallConntrackTcptimeoutestablished.setStatus("current")
_FirewallGateway_ObjectIdentity = ObjectIdentity
firewallGateway = _FirewallGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 3, 2)
)
_FirewallGatewayEnable_Type = OctetString
_FirewallGatewayEnable_Object = MibScalar
firewallGatewayEnable = _FirewallGatewayEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 3, 2, 1),
    _FirewallGatewayEnable_Type()
)
firewallGatewayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallGatewayEnable.setStatus("current")
_FirewallNode_ObjectIdentity = ObjectIdentity
firewallNode = _FirewallNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 3, 3)
)
_FirewallNodeAllowc2c_ObjectIdentity = ObjectIdentity
firewallNodeAllowc2c = _FirewallNodeAllowc2c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 3, 3, 1)
)
_FirewallNodeAllowc2cEth0_Type = OctetString
_FirewallNodeAllowc2cEth0_Object = MibScalar
firewallNodeAllowc2cEth0 = _FirewallNodeAllowc2cEth0_Object(
    (1, 3, 6, 1, 4, 1, 24350, 3, 3, 1, 1),
    _FirewallNodeAllowc2cEth0_Type()
)
firewallNodeAllowc2cEth0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallNodeAllowc2cEth0.setStatus("current")
_FirewallNodeAllowc2cWlan1_Type = OctetString
_FirewallNodeAllowc2cWlan1_Object = MibScalar
firewallNodeAllowc2cWlan1 = _FirewallNodeAllowc2cWlan1_Object(
    (1, 3, 6, 1, 4, 1, 24350, 3, 3, 1, 2),
    _FirewallNodeAllowc2cWlan1_Type()
)
firewallNodeAllowc2cWlan1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallNodeAllowc2cWlan1.setStatus("current")
_FirewallNodeAllowc2cWlan2_Type = OctetString
_FirewallNodeAllowc2cWlan2_Object = MibScalar
firewallNodeAllowc2cWlan2 = _FirewallNodeAllowc2cWlan2_Object(
    (1, 3, 6, 1, 4, 1, 24350, 3, 3, 1, 3),
    _FirewallNodeAllowc2cWlan2_Type()
)
firewallNodeAllowc2cWlan2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallNodeAllowc2cWlan2.setStatus("current")
_FirewallNodeAllowc2cWlan3_Type = OctetString
_FirewallNodeAllowc2cWlan3_Object = MibScalar
firewallNodeAllowc2cWlan3 = _FirewallNodeAllowc2cWlan3_Object(
    (1, 3, 6, 1, 4, 1, 24350, 3, 3, 1, 4),
    _FirewallNodeAllowc2cWlan3_Type()
)
firewallNodeAllowc2cWlan3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallNodeAllowc2cWlan3.setStatus("current")
_FirewallNodeAllowc2cWlan4_Type = OctetString
_FirewallNodeAllowc2cWlan4_Object = MibScalar
firewallNodeAllowc2cWlan4 = _FirewallNodeAllowc2cWlan4_Object(
    (1, 3, 6, 1, 4, 1, 24350, 3, 3, 1, 5),
    _FirewallNodeAllowc2cWlan4_Type()
)
firewallNodeAllowc2cWlan4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallNodeAllowc2cWlan4.setStatus("current")
_FirewallNodeEnable_Type = OctetString
_FirewallNodeEnable_Object = MibScalar
firewallNodeEnable = _FirewallNodeEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 3, 3, 2),
    _FirewallNodeEnable_Type()
)
firewallNodeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallNodeEnable.setStatus("current")
_FirewallNodeTcp_ObjectIdentity = ObjectIdentity
firewallNodeTcp = _FirewallNodeTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 3, 3, 3)
)
_FirewallNodeTcpAllow_ObjectIdentity = ObjectIdentity
firewallNodeTcpAllow = _FirewallNodeTcpAllow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 3, 3, 3, 1)
)
_FirewallNodeTcpAllowDest_Type = OctetString
_FirewallNodeTcpAllowDest_Object = MibScalar
firewallNodeTcpAllowDest = _FirewallNodeTcpAllowDest_Object(
    (1, 3, 6, 1, 4, 1, 24350, 3, 3, 3, 1, 1),
    _FirewallNodeTcpAllowDest_Type()
)
firewallNodeTcpAllowDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallNodeTcpAllowDest.setStatus("current")
_FirewallNodeTcpAllowSource_Type = OctetString
_FirewallNodeTcpAllowSource_Object = MibScalar
firewallNodeTcpAllowSource = _FirewallNodeTcpAllowSource_Object(
    (1, 3, 6, 1, 4, 1, 24350, 3, 3, 3, 1, 2),
    _FirewallNodeTcpAllowSource_Type()
)
firewallNodeTcpAllowSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallNodeTcpAllowSource.setStatus("current")
_FirewallNodeUdp_ObjectIdentity = ObjectIdentity
firewallNodeUdp = _FirewallNodeUdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 3, 3, 4)
)
_FirewallNodeUdpAllow_ObjectIdentity = ObjectIdentity
firewallNodeUdpAllow = _FirewallNodeUdpAllow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 3, 3, 4, 1)
)
_FirewallNodeUdpAllowDest_Type = OctetString
_FirewallNodeUdpAllowDest_Object = MibScalar
firewallNodeUdpAllowDest = _FirewallNodeUdpAllowDest_Object(
    (1, 3, 6, 1, 4, 1, 24350, 3, 3, 4, 1, 1),
    _FirewallNodeUdpAllowDest_Type()
)
firewallNodeUdpAllowDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallNodeUdpAllowDest.setStatus("current")
_FirewallNodeUdpAllowSource_Type = OctetString
_FirewallNodeUdpAllowSource_Object = MibScalar
firewallNodeUdpAllowSource = _FirewallNodeUdpAllowSource_Object(
    (1, 3, 6, 1, 4, 1, 24350, 3, 3, 4, 1, 2),
    _FirewallNodeUdpAllowSource_Type()
)
firewallNodeUdpAllowSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallNodeUdpAllowSource.setStatus("current")
_Qos_ObjectIdentity = ObjectIdentity
qos = _Qos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4)
)
_QosEnable_Type = OctetString
_QosEnable_Object = MibScalar
qosEnable = _QosEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 1),
    _QosEnable_Type()
)
qosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosEnable.setStatus("current")
_QosExtra_Type = OctetString
_QosExtra_Object = MibScalar
qosExtra = _QosExtra_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 2),
    _QosExtra_Type()
)
qosExtra.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosExtra.setStatus("current")
_QosIn_ObjectIdentity = ObjectIdentity
qosIn = _QosIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3)
)
_QosInDefault_ObjectIdentity = ObjectIdentity
qosInDefault = _QosInDefault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 1)
)
_QosInDefaultFlowpriority_Type = OctetString
_QosInDefaultFlowpriority_Object = MibScalar
qosInDefaultFlowpriority = _QosInDefaultFlowpriority_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 1, 1),
    _QosInDefaultFlowpriority_Type()
)
qosInDefaultFlowpriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosInDefaultFlowpriority.setStatus("current")
_QosInDefaultHwpri_ObjectIdentity = ObjectIdentity
qosInDefaultHwpri = _QosInDefaultHwpri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 1, 2)
)
_QosInDefaultHwpriMax_Type = OctetString
_QosInDefaultHwpriMax_Object = MibScalar
qosInDefaultHwpriMax = _QosInDefaultHwpriMax_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 1, 2, 1),
    _QosInDefaultHwpriMax_Type()
)
qosInDefaultHwpriMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosInDefaultHwpriMax.setStatus("current")
_QosInDefaultHwpriMin_Type = OctetString
_QosInDefaultHwpriMin_Object = MibScalar
qosInDefaultHwpriMin = _QosInDefaultHwpriMin_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 1, 2, 2),
    _QosInDefaultHwpriMin_Type()
)
qosInDefaultHwpriMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosInDefaultHwpriMin.setStatus("current")
_QosInEth0_ObjectIdentity = ObjectIdentity
qosInEth0 = _QosInEth0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 2)
)
_QosInEth0Flowpriority_Type = OctetString
_QosInEth0Flowpriority_Object = MibScalar
qosInEth0Flowpriority = _QosInEth0Flowpriority_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 2, 1),
    _QosInEth0Flowpriority_Type()
)
qosInEth0Flowpriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosInEth0Flowpriority.setStatus("current")
_QosInEth0Hwpri_ObjectIdentity = ObjectIdentity
qosInEth0Hwpri = _QosInEth0Hwpri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 2, 2)
)
_QosInEth0HwpriMax_Type = OctetString
_QosInEth0HwpriMax_Object = MibScalar
qosInEth0HwpriMax = _QosInEth0HwpriMax_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 2, 2, 1),
    _QosInEth0HwpriMax_Type()
)
qosInEth0HwpriMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosInEth0HwpriMax.setStatus("current")
_QosInEth0HwpriMin_Type = OctetString
_QosInEth0HwpriMin_Object = MibScalar
qosInEth0HwpriMin = _QosInEth0HwpriMin_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 2, 2, 2),
    _QosInEth0HwpriMin_Type()
)
qosInEth0HwpriMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosInEth0HwpriMin.setStatus("current")
_QosInLocal_ObjectIdentity = ObjectIdentity
qosInLocal = _QosInLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 3)
)
_QosInLocalFlowpriority_Type = OctetString
_QosInLocalFlowpriority_Object = MibScalar
qosInLocalFlowpriority = _QosInLocalFlowpriority_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 3, 1),
    _QosInLocalFlowpriority_Type()
)
qosInLocalFlowpriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosInLocalFlowpriority.setStatus("current")
_QosInLocalHwpri_ObjectIdentity = ObjectIdentity
qosInLocalHwpri = _QosInLocalHwpri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 3, 2)
)
_QosInLocalHwpriMax_Type = OctetString
_QosInLocalHwpriMax_Object = MibScalar
qosInLocalHwpriMax = _QosInLocalHwpriMax_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 3, 2, 1),
    _QosInLocalHwpriMax_Type()
)
qosInLocalHwpriMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosInLocalHwpriMax.setStatus("current")
_QosInLocalHwpriMin_Type = OctetString
_QosInLocalHwpriMin_Object = MibScalar
qosInLocalHwpriMin = _QosInLocalHwpriMin_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 3, 2, 2),
    _QosInLocalHwpriMin_Type()
)
qosInLocalHwpriMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosInLocalHwpriMin.setStatus("current")
_QosInWlan0_ObjectIdentity = ObjectIdentity
qosInWlan0 = _QosInWlan0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 4)
)
_QosInWlan0Flowpriority_Type = OctetString
_QosInWlan0Flowpriority_Object = MibScalar
qosInWlan0Flowpriority = _QosInWlan0Flowpriority_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 4, 1),
    _QosInWlan0Flowpriority_Type()
)
qosInWlan0Flowpriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosInWlan0Flowpriority.setStatus("current")
_QosInWlan0Hwpri_ObjectIdentity = ObjectIdentity
qosInWlan0Hwpri = _QosInWlan0Hwpri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 4, 2)
)
_QosInWlan0HwpriMax_Type = OctetString
_QosInWlan0HwpriMax_Object = MibScalar
qosInWlan0HwpriMax = _QosInWlan0HwpriMax_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 4, 2, 1),
    _QosInWlan0HwpriMax_Type()
)
qosInWlan0HwpriMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosInWlan0HwpriMax.setStatus("current")
_QosInWlan0HwpriMin_Type = OctetString
_QosInWlan0HwpriMin_Object = MibScalar
qosInWlan0HwpriMin = _QosInWlan0HwpriMin_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 4, 2, 2),
    _QosInWlan0HwpriMin_Type()
)
qosInWlan0HwpriMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosInWlan0HwpriMin.setStatus("current")
_QosInWlan1_ObjectIdentity = ObjectIdentity
qosInWlan1 = _QosInWlan1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 5)
)
_QosInWlan1Flowpriority_Type = OctetString
_QosInWlan1Flowpriority_Object = MibScalar
qosInWlan1Flowpriority = _QosInWlan1Flowpriority_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 5, 1),
    _QosInWlan1Flowpriority_Type()
)
qosInWlan1Flowpriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosInWlan1Flowpriority.setStatus("current")
_QosInWlan1Hwpri_ObjectIdentity = ObjectIdentity
qosInWlan1Hwpri = _QosInWlan1Hwpri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 5, 2)
)
_QosInWlan1HwpriMax_Type = OctetString
_QosInWlan1HwpriMax_Object = MibScalar
qosInWlan1HwpriMax = _QosInWlan1HwpriMax_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 5, 2, 1),
    _QosInWlan1HwpriMax_Type()
)
qosInWlan1HwpriMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosInWlan1HwpriMax.setStatus("current")
_QosInWlan1HwpriMin_Type = OctetString
_QosInWlan1HwpriMin_Object = MibScalar
qosInWlan1HwpriMin = _QosInWlan1HwpriMin_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 5, 2, 2),
    _QosInWlan1HwpriMin_Type()
)
qosInWlan1HwpriMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosInWlan1HwpriMin.setStatus("current")
_QosInWlan2_ObjectIdentity = ObjectIdentity
qosInWlan2 = _QosInWlan2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 6)
)
_QosInWlan2Flowpriority_Type = OctetString
_QosInWlan2Flowpriority_Object = MibScalar
qosInWlan2Flowpriority = _QosInWlan2Flowpriority_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 6, 1),
    _QosInWlan2Flowpriority_Type()
)
qosInWlan2Flowpriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosInWlan2Flowpriority.setStatus("current")
_QosInWlan2Hwpri_ObjectIdentity = ObjectIdentity
qosInWlan2Hwpri = _QosInWlan2Hwpri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 6, 2)
)
_QosInWlan2HwpriMax_Type = OctetString
_QosInWlan2HwpriMax_Object = MibScalar
qosInWlan2HwpriMax = _QosInWlan2HwpriMax_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 6, 2, 1),
    _QosInWlan2HwpriMax_Type()
)
qosInWlan2HwpriMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosInWlan2HwpriMax.setStatus("current")
_QosInWlan2HwpriMin_Type = OctetString
_QosInWlan2HwpriMin_Object = MibScalar
qosInWlan2HwpriMin = _QosInWlan2HwpriMin_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 6, 2, 2),
    _QosInWlan2HwpriMin_Type()
)
qosInWlan2HwpriMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosInWlan2HwpriMin.setStatus("current")
_QosInWlan3_ObjectIdentity = ObjectIdentity
qosInWlan3 = _QosInWlan3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 7)
)
_QosInWlan3Flowpriority_Type = OctetString
_QosInWlan3Flowpriority_Object = MibScalar
qosInWlan3Flowpriority = _QosInWlan3Flowpriority_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 7, 1),
    _QosInWlan3Flowpriority_Type()
)
qosInWlan3Flowpriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosInWlan3Flowpriority.setStatus("current")
_QosInWlan3Hwpri_ObjectIdentity = ObjectIdentity
qosInWlan3Hwpri = _QosInWlan3Hwpri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 7, 2)
)
_QosInWlan3HwpriMax_Type = OctetString
_QosInWlan3HwpriMax_Object = MibScalar
qosInWlan3HwpriMax = _QosInWlan3HwpriMax_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 7, 2, 1),
    _QosInWlan3HwpriMax_Type()
)
qosInWlan3HwpriMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosInWlan3HwpriMax.setStatus("current")
_QosInWlan3HwpriMin_Type = OctetString
_QosInWlan3HwpriMin_Object = MibScalar
qosInWlan3HwpriMin = _QosInWlan3HwpriMin_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 7, 2, 2),
    _QosInWlan3HwpriMin_Type()
)
qosInWlan3HwpriMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosInWlan3HwpriMin.setStatus("current")
_QosInWlan4_ObjectIdentity = ObjectIdentity
qosInWlan4 = _QosInWlan4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 8)
)
_QosInWlan4Flowpriority_Type = OctetString
_QosInWlan4Flowpriority_Object = MibScalar
qosInWlan4Flowpriority = _QosInWlan4Flowpriority_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 8, 1),
    _QosInWlan4Flowpriority_Type()
)
qosInWlan4Flowpriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosInWlan4Flowpriority.setStatus("current")
_QosInWlan4Hwpri_ObjectIdentity = ObjectIdentity
qosInWlan4Hwpri = _QosInWlan4Hwpri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 8, 2)
)
_QosInWlan4HwpriMax_Type = OctetString
_QosInWlan4HwpriMax_Object = MibScalar
qosInWlan4HwpriMax = _QosInWlan4HwpriMax_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 8, 2, 1),
    _QosInWlan4HwpriMax_Type()
)
qosInWlan4HwpriMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosInWlan4HwpriMax.setStatus("current")
_QosInWlan4HwpriMin_Type = OctetString
_QosInWlan4HwpriMin_Object = MibScalar
qosInWlan4HwpriMin = _QosInWlan4HwpriMin_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 3, 8, 2, 2),
    _QosInWlan4HwpriMin_Type()
)
qosInWlan4HwpriMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosInWlan4HwpriMin.setStatus("current")
_QosOut_ObjectIdentity = ObjectIdentity
qosOut = _QosOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4)
)
_QosOutDefault_ObjectIdentity = ObjectIdentity
qosOutDefault = _QosOutDefault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 1)
)
_QosOutDefaultDefault_ObjectIdentity = ObjectIdentity
qosOutDefaultDefault = _QosOutDefaultDefault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 1, 1)
)
_QosOutDefaultDefaultLimit_Type = OctetString
_QosOutDefaultDefaultLimit_Object = MibScalar
qosOutDefaultDefaultLimit = _QosOutDefaultDefaultLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 1, 1, 1),
    _QosOutDefaultDefaultLimit_Type()
)
qosOutDefaultDefaultLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutDefaultDefaultLimit.setStatus("current")
_QosOutDefaultDefaultReserve_Type = OctetString
_QosOutDefaultDefaultReserve_Object = MibScalar
qosOutDefaultDefaultReserve = _QosOutDefaultDefaultReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 1, 1, 2),
    _QosOutDefaultDefaultReserve_Type()
)
qosOutDefaultDefaultReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutDefaultDefaultReserve.setStatus("current")
_QosOutDefaultEth0_ObjectIdentity = ObjectIdentity
qosOutDefaultEth0 = _QosOutDefaultEth0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 1, 2)
)
_QosOutDefaultEth0Limit_Type = OctetString
_QosOutDefaultEth0Limit_Object = MibScalar
qosOutDefaultEth0Limit = _QosOutDefaultEth0Limit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 1, 2, 1),
    _QosOutDefaultEth0Limit_Type()
)
qosOutDefaultEth0Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutDefaultEth0Limit.setStatus("current")
_QosOutDefaultEth0Reserve_Type = OctetString
_QosOutDefaultEth0Reserve_Object = MibScalar
qosOutDefaultEth0Reserve = _QosOutDefaultEth0Reserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 1, 2, 2),
    _QosOutDefaultEth0Reserve_Type()
)
qosOutDefaultEth0Reserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutDefaultEth0Reserve.setStatus("current")
_QosOutDefaultLimit_Type = OctetString
_QosOutDefaultLimit_Object = MibScalar
qosOutDefaultLimit = _QosOutDefaultLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 1, 3),
    _QosOutDefaultLimit_Type()
)
qosOutDefaultLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutDefaultLimit.setStatus("current")
_QosOutDefaultLocal_ObjectIdentity = ObjectIdentity
qosOutDefaultLocal = _QosOutDefaultLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 1, 4)
)
_QosOutDefaultLocalLimit_Type = OctetString
_QosOutDefaultLocalLimit_Object = MibScalar
qosOutDefaultLocalLimit = _QosOutDefaultLocalLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 1, 4, 1),
    _QosOutDefaultLocalLimit_Type()
)
qosOutDefaultLocalLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutDefaultLocalLimit.setStatus("current")
_QosOutDefaultLocalReserve_Type = OctetString
_QosOutDefaultLocalReserve_Object = MibScalar
qosOutDefaultLocalReserve = _QosOutDefaultLocalReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 1, 4, 2),
    _QosOutDefaultLocalReserve_Type()
)
qosOutDefaultLocalReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutDefaultLocalReserve.setStatus("current")
_QosOutDefaultWlan0_ObjectIdentity = ObjectIdentity
qosOutDefaultWlan0 = _QosOutDefaultWlan0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 1, 5)
)
_QosOutDefaultWlan0Limit_Type = OctetString
_QosOutDefaultWlan0Limit_Object = MibScalar
qosOutDefaultWlan0Limit = _QosOutDefaultWlan0Limit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 1, 5, 1),
    _QosOutDefaultWlan0Limit_Type()
)
qosOutDefaultWlan0Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutDefaultWlan0Limit.setStatus("current")
_QosOutDefaultWlan0Reserve_Type = OctetString
_QosOutDefaultWlan0Reserve_Object = MibScalar
qosOutDefaultWlan0Reserve = _QosOutDefaultWlan0Reserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 1, 5, 2),
    _QosOutDefaultWlan0Reserve_Type()
)
qosOutDefaultWlan0Reserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutDefaultWlan0Reserve.setStatus("current")
_QosOutDefaultWlan1_ObjectIdentity = ObjectIdentity
qosOutDefaultWlan1 = _QosOutDefaultWlan1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 1, 6)
)
_QosOutDefaultWlan1Limit_Type = OctetString
_QosOutDefaultWlan1Limit_Object = MibScalar
qosOutDefaultWlan1Limit = _QosOutDefaultWlan1Limit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 1, 6, 1),
    _QosOutDefaultWlan1Limit_Type()
)
qosOutDefaultWlan1Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutDefaultWlan1Limit.setStatus("current")
_QosOutDefaultWlan1Reserve_Type = OctetString
_QosOutDefaultWlan1Reserve_Object = MibScalar
qosOutDefaultWlan1Reserve = _QosOutDefaultWlan1Reserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 1, 6, 2),
    _QosOutDefaultWlan1Reserve_Type()
)
qosOutDefaultWlan1Reserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutDefaultWlan1Reserve.setStatus("current")
_QosOutDefaultWlan2_ObjectIdentity = ObjectIdentity
qosOutDefaultWlan2 = _QosOutDefaultWlan2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 1, 7)
)
_QosOutDefaultWlan2Limit_Type = OctetString
_QosOutDefaultWlan2Limit_Object = MibScalar
qosOutDefaultWlan2Limit = _QosOutDefaultWlan2Limit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 1, 7, 1),
    _QosOutDefaultWlan2Limit_Type()
)
qosOutDefaultWlan2Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutDefaultWlan2Limit.setStatus("current")
_QosOutDefaultWlan2Reserve_Type = OctetString
_QosOutDefaultWlan2Reserve_Object = MibScalar
qosOutDefaultWlan2Reserve = _QosOutDefaultWlan2Reserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 1, 7, 2),
    _QosOutDefaultWlan2Reserve_Type()
)
qosOutDefaultWlan2Reserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutDefaultWlan2Reserve.setStatus("current")
_QosOutDefaultWlan3_ObjectIdentity = ObjectIdentity
qosOutDefaultWlan3 = _QosOutDefaultWlan3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 1, 8)
)
_QosOutDefaultWlan3Limit_Type = OctetString
_QosOutDefaultWlan3Limit_Object = MibScalar
qosOutDefaultWlan3Limit = _QosOutDefaultWlan3Limit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 1, 8, 1),
    _QosOutDefaultWlan3Limit_Type()
)
qosOutDefaultWlan3Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutDefaultWlan3Limit.setStatus("current")
_QosOutDefaultWlan3Reserve_Type = OctetString
_QosOutDefaultWlan3Reserve_Object = MibScalar
qosOutDefaultWlan3Reserve = _QosOutDefaultWlan3Reserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 1, 8, 2),
    _QosOutDefaultWlan3Reserve_Type()
)
qosOutDefaultWlan3Reserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutDefaultWlan3Reserve.setStatus("current")
_QosOutDefaultWlan4_ObjectIdentity = ObjectIdentity
qosOutDefaultWlan4 = _QosOutDefaultWlan4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 1, 9)
)
_QosOutDefaultWlan4Limit_Type = OctetString
_QosOutDefaultWlan4Limit_Object = MibScalar
qosOutDefaultWlan4Limit = _QosOutDefaultWlan4Limit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 1, 9, 1),
    _QosOutDefaultWlan4Limit_Type()
)
qosOutDefaultWlan4Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutDefaultWlan4Limit.setStatus("current")
_QosOutDefaultWlan4Reserve_Type = OctetString
_QosOutDefaultWlan4Reserve_Object = MibScalar
qosOutDefaultWlan4Reserve = _QosOutDefaultWlan4Reserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 1, 9, 2),
    _QosOutDefaultWlan4Reserve_Type()
)
qosOutDefaultWlan4Reserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutDefaultWlan4Reserve.setStatus("current")
_QosOutWlan0_ObjectIdentity = ObjectIdentity
qosOutWlan0 = _QosOutWlan0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2)
)
_QosOutWlan0Default_ObjectIdentity = ObjectIdentity
qosOutWlan0Default = _QosOutWlan0Default_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 1)
)
_QosOutWlan0DefaultBe_ObjectIdentity = ObjectIdentity
qosOutWlan0DefaultBe = _QosOutWlan0DefaultBe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 1, 1)
)
_QosOutWlan0DefaultBeLimit_Type = OctetString
_QosOutWlan0DefaultBeLimit_Object = MibScalar
qosOutWlan0DefaultBeLimit = _QosOutWlan0DefaultBeLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 1, 1, 1),
    _QosOutWlan0DefaultBeLimit_Type()
)
qosOutWlan0DefaultBeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0DefaultBeLimit.setStatus("current")
_QosOutWlan0DefaultBeReserve_Type = OctetString
_QosOutWlan0DefaultBeReserve_Object = MibScalar
qosOutWlan0DefaultBeReserve = _QosOutWlan0DefaultBeReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 1, 1, 2),
    _QosOutWlan0DefaultBeReserve_Type()
)
qosOutWlan0DefaultBeReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0DefaultBeReserve.setStatus("current")
_QosOutWlan0DefaultBk_ObjectIdentity = ObjectIdentity
qosOutWlan0DefaultBk = _QosOutWlan0DefaultBk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 1, 2)
)
_QosOutWlan0DefaultBkLimit_Type = OctetString
_QosOutWlan0DefaultBkLimit_Object = MibScalar
qosOutWlan0DefaultBkLimit = _QosOutWlan0DefaultBkLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 1, 2, 1),
    _QosOutWlan0DefaultBkLimit_Type()
)
qosOutWlan0DefaultBkLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0DefaultBkLimit.setStatus("current")
_QosOutWlan0DefaultBkReserve_Type = OctetString
_QosOutWlan0DefaultBkReserve_Object = MibScalar
qosOutWlan0DefaultBkReserve = _QosOutWlan0DefaultBkReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 1, 2, 2),
    _QosOutWlan0DefaultBkReserve_Type()
)
qosOutWlan0DefaultBkReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0DefaultBkReserve.setStatus("current")
_QosOutWlan0DefaultLimit_Type = OctetString
_QosOutWlan0DefaultLimit_Object = MibScalar
qosOutWlan0DefaultLimit = _QosOutWlan0DefaultLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 1, 3),
    _QosOutWlan0DefaultLimit_Type()
)
qosOutWlan0DefaultLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0DefaultLimit.setStatus("current")
_QosOutWlan0DefaultReserve_Type = OctetString
_QosOutWlan0DefaultReserve_Object = MibScalar
qosOutWlan0DefaultReserve = _QosOutWlan0DefaultReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 1, 4),
    _QosOutWlan0DefaultReserve_Type()
)
qosOutWlan0DefaultReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0DefaultReserve.setStatus("current")
_QosOutWlan0DefaultVi_ObjectIdentity = ObjectIdentity
qosOutWlan0DefaultVi = _QosOutWlan0DefaultVi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 1, 5)
)
_QosOutWlan0DefaultViLimit_Type = OctetString
_QosOutWlan0DefaultViLimit_Object = MibScalar
qosOutWlan0DefaultViLimit = _QosOutWlan0DefaultViLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 1, 5, 1),
    _QosOutWlan0DefaultViLimit_Type()
)
qosOutWlan0DefaultViLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0DefaultViLimit.setStatus("current")
_QosOutWlan0DefaultViReserve_Type = OctetString
_QosOutWlan0DefaultViReserve_Object = MibScalar
qosOutWlan0DefaultViReserve = _QosOutWlan0DefaultViReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 1, 5, 2),
    _QosOutWlan0DefaultViReserve_Type()
)
qosOutWlan0DefaultViReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0DefaultViReserve.setStatus("current")
_QosOutWlan0DefaultVo_ObjectIdentity = ObjectIdentity
qosOutWlan0DefaultVo = _QosOutWlan0DefaultVo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 1, 6)
)
_QosOutWlan0DefaultVoLimit_Type = OctetString
_QosOutWlan0DefaultVoLimit_Object = MibScalar
qosOutWlan0DefaultVoLimit = _QosOutWlan0DefaultVoLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 1, 6, 1),
    _QosOutWlan0DefaultVoLimit_Type()
)
qosOutWlan0DefaultVoLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0DefaultVoLimit.setStatus("current")
_QosOutWlan0DefaultVoReserve_Type = OctetString
_QosOutWlan0DefaultVoReserve_Object = MibScalar
qosOutWlan0DefaultVoReserve = _QosOutWlan0DefaultVoReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 1, 6, 2),
    _QosOutWlan0DefaultVoReserve_Type()
)
qosOutWlan0DefaultVoReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0DefaultVoReserve.setStatus("current")
_QosOutWlan0Eth0_ObjectIdentity = ObjectIdentity
qosOutWlan0Eth0 = _QosOutWlan0Eth0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 2)
)
_QosOutWlan0Eth0Be_ObjectIdentity = ObjectIdentity
qosOutWlan0Eth0Be = _QosOutWlan0Eth0Be_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 2, 1)
)
_QosOutWlan0Eth0BeLimit_Type = OctetString
_QosOutWlan0Eth0BeLimit_Object = MibScalar
qosOutWlan0Eth0BeLimit = _QosOutWlan0Eth0BeLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 2, 1, 1),
    _QosOutWlan0Eth0BeLimit_Type()
)
qosOutWlan0Eth0BeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Eth0BeLimit.setStatus("current")
_QosOutWlan0Eth0BeReserve_Type = OctetString
_QosOutWlan0Eth0BeReserve_Object = MibScalar
qosOutWlan0Eth0BeReserve = _QosOutWlan0Eth0BeReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 2, 1, 2),
    _QosOutWlan0Eth0BeReserve_Type()
)
qosOutWlan0Eth0BeReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Eth0BeReserve.setStatus("current")
_QosOutWlan0Eth0Bk_ObjectIdentity = ObjectIdentity
qosOutWlan0Eth0Bk = _QosOutWlan0Eth0Bk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 2, 2)
)
_QosOutWlan0Eth0BkLimit_Type = OctetString
_QosOutWlan0Eth0BkLimit_Object = MibScalar
qosOutWlan0Eth0BkLimit = _QosOutWlan0Eth0BkLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 2, 2, 1),
    _QosOutWlan0Eth0BkLimit_Type()
)
qosOutWlan0Eth0BkLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Eth0BkLimit.setStatus("current")
_QosOutWlan0Eth0BkReserve_Type = OctetString
_QosOutWlan0Eth0BkReserve_Object = MibScalar
qosOutWlan0Eth0BkReserve = _QosOutWlan0Eth0BkReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 2, 2, 2),
    _QosOutWlan0Eth0BkReserve_Type()
)
qosOutWlan0Eth0BkReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Eth0BkReserve.setStatus("current")
_QosOutWlan0Eth0Limit_Type = OctetString
_QosOutWlan0Eth0Limit_Object = MibScalar
qosOutWlan0Eth0Limit = _QosOutWlan0Eth0Limit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 2, 3),
    _QosOutWlan0Eth0Limit_Type()
)
qosOutWlan0Eth0Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Eth0Limit.setStatus("current")
_QosOutWlan0Eth0Reserve_Type = OctetString
_QosOutWlan0Eth0Reserve_Object = MibScalar
qosOutWlan0Eth0Reserve = _QosOutWlan0Eth0Reserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 2, 4),
    _QosOutWlan0Eth0Reserve_Type()
)
qosOutWlan0Eth0Reserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Eth0Reserve.setStatus("current")
_QosOutWlan0Eth0Vi_ObjectIdentity = ObjectIdentity
qosOutWlan0Eth0Vi = _QosOutWlan0Eth0Vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 2, 5)
)
_QosOutWlan0Eth0ViLimit_Type = OctetString
_QosOutWlan0Eth0ViLimit_Object = MibScalar
qosOutWlan0Eth0ViLimit = _QosOutWlan0Eth0ViLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 2, 5, 1),
    _QosOutWlan0Eth0ViLimit_Type()
)
qosOutWlan0Eth0ViLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Eth0ViLimit.setStatus("current")
_QosOutWlan0Eth0ViReserve_Type = OctetString
_QosOutWlan0Eth0ViReserve_Object = MibScalar
qosOutWlan0Eth0ViReserve = _QosOutWlan0Eth0ViReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 2, 5, 2),
    _QosOutWlan0Eth0ViReserve_Type()
)
qosOutWlan0Eth0ViReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Eth0ViReserve.setStatus("current")
_QosOutWlan0Eth0Vo_ObjectIdentity = ObjectIdentity
qosOutWlan0Eth0Vo = _QosOutWlan0Eth0Vo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 2, 6)
)
_QosOutWlan0Eth0VoLimit_Type = OctetString
_QosOutWlan0Eth0VoLimit_Object = MibScalar
qosOutWlan0Eth0VoLimit = _QosOutWlan0Eth0VoLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 2, 6, 1),
    _QosOutWlan0Eth0VoLimit_Type()
)
qosOutWlan0Eth0VoLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Eth0VoLimit.setStatus("current")
_QosOutWlan0Eth0VoReserve_Type = OctetString
_QosOutWlan0Eth0VoReserve_Object = MibScalar
qosOutWlan0Eth0VoReserve = _QosOutWlan0Eth0VoReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 2, 6, 2),
    _QosOutWlan0Eth0VoReserve_Type()
)
qosOutWlan0Eth0VoReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Eth0VoReserve.setStatus("current")
_QosOutWlan0Limit_Type = OctetString
_QosOutWlan0Limit_Object = MibScalar
qosOutWlan0Limit = _QosOutWlan0Limit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 3),
    _QosOutWlan0Limit_Type()
)
qosOutWlan0Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Limit.setStatus("current")
_QosOutWlan0Local_ObjectIdentity = ObjectIdentity
qosOutWlan0Local = _QosOutWlan0Local_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 4)
)
_QosOutWlan0LocalBe_ObjectIdentity = ObjectIdentity
qosOutWlan0LocalBe = _QosOutWlan0LocalBe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 4, 1)
)
_QosOutWlan0LocalBeLimit_Type = OctetString
_QosOutWlan0LocalBeLimit_Object = MibScalar
qosOutWlan0LocalBeLimit = _QosOutWlan0LocalBeLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 4, 1, 1),
    _QosOutWlan0LocalBeLimit_Type()
)
qosOutWlan0LocalBeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0LocalBeLimit.setStatus("current")
_QosOutWlan0LocalBeReserve_Type = OctetString
_QosOutWlan0LocalBeReserve_Object = MibScalar
qosOutWlan0LocalBeReserve = _QosOutWlan0LocalBeReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 4, 1, 2),
    _QosOutWlan0LocalBeReserve_Type()
)
qosOutWlan0LocalBeReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0LocalBeReserve.setStatus("current")
_QosOutWlan0LocalBk_ObjectIdentity = ObjectIdentity
qosOutWlan0LocalBk = _QosOutWlan0LocalBk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 4, 2)
)
_QosOutWlan0LocalBkLimit_Type = OctetString
_QosOutWlan0LocalBkLimit_Object = MibScalar
qosOutWlan0LocalBkLimit = _QosOutWlan0LocalBkLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 4, 2, 1),
    _QosOutWlan0LocalBkLimit_Type()
)
qosOutWlan0LocalBkLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0LocalBkLimit.setStatus("current")
_QosOutWlan0LocalBkReserve_Type = OctetString
_QosOutWlan0LocalBkReserve_Object = MibScalar
qosOutWlan0LocalBkReserve = _QosOutWlan0LocalBkReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 4, 2, 2),
    _QosOutWlan0LocalBkReserve_Type()
)
qosOutWlan0LocalBkReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0LocalBkReserve.setStatus("current")
_QosOutWlan0LocalLimit_Type = OctetString
_QosOutWlan0LocalLimit_Object = MibScalar
qosOutWlan0LocalLimit = _QosOutWlan0LocalLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 4, 3),
    _QosOutWlan0LocalLimit_Type()
)
qosOutWlan0LocalLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0LocalLimit.setStatus("current")
_QosOutWlan0LocalReserve_Type = OctetString
_QosOutWlan0LocalReserve_Object = MibScalar
qosOutWlan0LocalReserve = _QosOutWlan0LocalReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 4, 4),
    _QosOutWlan0LocalReserve_Type()
)
qosOutWlan0LocalReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0LocalReserve.setStatus("current")
_QosOutWlan0LocalVi_ObjectIdentity = ObjectIdentity
qosOutWlan0LocalVi = _QosOutWlan0LocalVi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 4, 5)
)
_QosOutWlan0LocalViLimit_Type = OctetString
_QosOutWlan0LocalViLimit_Object = MibScalar
qosOutWlan0LocalViLimit = _QosOutWlan0LocalViLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 4, 5, 1),
    _QosOutWlan0LocalViLimit_Type()
)
qosOutWlan0LocalViLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0LocalViLimit.setStatus("current")
_QosOutWlan0LocalViReserve_Type = OctetString
_QosOutWlan0LocalViReserve_Object = MibScalar
qosOutWlan0LocalViReserve = _QosOutWlan0LocalViReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 4, 5, 2),
    _QosOutWlan0LocalViReserve_Type()
)
qosOutWlan0LocalViReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0LocalViReserve.setStatus("current")
_QosOutWlan0LocalVo_ObjectIdentity = ObjectIdentity
qosOutWlan0LocalVo = _QosOutWlan0LocalVo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 4, 6)
)
_QosOutWlan0LocalVoLimit_Type = OctetString
_QosOutWlan0LocalVoLimit_Object = MibScalar
qosOutWlan0LocalVoLimit = _QosOutWlan0LocalVoLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 4, 6, 1),
    _QosOutWlan0LocalVoLimit_Type()
)
qosOutWlan0LocalVoLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0LocalVoLimit.setStatus("current")
_QosOutWlan0LocalVoReserve_Type = OctetString
_QosOutWlan0LocalVoReserve_Object = MibScalar
qosOutWlan0LocalVoReserve = _QosOutWlan0LocalVoReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 4, 6, 2),
    _QosOutWlan0LocalVoReserve_Type()
)
qosOutWlan0LocalVoReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0LocalVoReserve.setStatus("current")
_QosOutWlan0Wlan0_ObjectIdentity = ObjectIdentity
qosOutWlan0Wlan0 = _QosOutWlan0Wlan0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 5)
)
_QosOutWlan0Wlan0Be_ObjectIdentity = ObjectIdentity
qosOutWlan0Wlan0Be = _QosOutWlan0Wlan0Be_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 5, 1)
)
_QosOutWlan0Wlan0BeLimit_Type = OctetString
_QosOutWlan0Wlan0BeLimit_Object = MibScalar
qosOutWlan0Wlan0BeLimit = _QosOutWlan0Wlan0BeLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 5, 1, 1),
    _QosOutWlan0Wlan0BeLimit_Type()
)
qosOutWlan0Wlan0BeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan0BeLimit.setStatus("current")
_QosOutWlan0Wlan0BeReserve_Type = OctetString
_QosOutWlan0Wlan0BeReserve_Object = MibScalar
qosOutWlan0Wlan0BeReserve = _QosOutWlan0Wlan0BeReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 5, 1, 2),
    _QosOutWlan0Wlan0BeReserve_Type()
)
qosOutWlan0Wlan0BeReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan0BeReserve.setStatus("current")
_QosOutWlan0Wlan0Bk_ObjectIdentity = ObjectIdentity
qosOutWlan0Wlan0Bk = _QosOutWlan0Wlan0Bk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 5, 2)
)
_QosOutWlan0Wlan0BkLimit_Type = OctetString
_QosOutWlan0Wlan0BkLimit_Object = MibScalar
qosOutWlan0Wlan0BkLimit = _QosOutWlan0Wlan0BkLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 5, 2, 1),
    _QosOutWlan0Wlan0BkLimit_Type()
)
qosOutWlan0Wlan0BkLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan0BkLimit.setStatus("current")
_QosOutWlan0Wlan0BkReserve_Type = OctetString
_QosOutWlan0Wlan0BkReserve_Object = MibScalar
qosOutWlan0Wlan0BkReserve = _QosOutWlan0Wlan0BkReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 5, 2, 2),
    _QosOutWlan0Wlan0BkReserve_Type()
)
qosOutWlan0Wlan0BkReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan0BkReserve.setStatus("current")
_QosOutWlan0Wlan0Limit_Type = OctetString
_QosOutWlan0Wlan0Limit_Object = MibScalar
qosOutWlan0Wlan0Limit = _QosOutWlan0Wlan0Limit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 5, 3),
    _QosOutWlan0Wlan0Limit_Type()
)
qosOutWlan0Wlan0Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan0Limit.setStatus("current")
_QosOutWlan0Wlan0Reserve_Type = OctetString
_QosOutWlan0Wlan0Reserve_Object = MibScalar
qosOutWlan0Wlan0Reserve = _QosOutWlan0Wlan0Reserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 5, 4),
    _QosOutWlan0Wlan0Reserve_Type()
)
qosOutWlan0Wlan0Reserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan0Reserve.setStatus("current")
_QosOutWlan0Wlan0Vi_ObjectIdentity = ObjectIdentity
qosOutWlan0Wlan0Vi = _QosOutWlan0Wlan0Vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 5, 5)
)
_QosOutWlan0Wlan0ViLimit_Type = OctetString
_QosOutWlan0Wlan0ViLimit_Object = MibScalar
qosOutWlan0Wlan0ViLimit = _QosOutWlan0Wlan0ViLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 5, 5, 1),
    _QosOutWlan0Wlan0ViLimit_Type()
)
qosOutWlan0Wlan0ViLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan0ViLimit.setStatus("current")
_QosOutWlan0Wlan0ViReserve_Type = OctetString
_QosOutWlan0Wlan0ViReserve_Object = MibScalar
qosOutWlan0Wlan0ViReserve = _QosOutWlan0Wlan0ViReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 5, 5, 2),
    _QosOutWlan0Wlan0ViReserve_Type()
)
qosOutWlan0Wlan0ViReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan0ViReserve.setStatus("current")
_QosOutWlan0Wlan0Vo_ObjectIdentity = ObjectIdentity
qosOutWlan0Wlan0Vo = _QosOutWlan0Wlan0Vo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 5, 6)
)
_QosOutWlan0Wlan0VoLimit_Type = OctetString
_QosOutWlan0Wlan0VoLimit_Object = MibScalar
qosOutWlan0Wlan0VoLimit = _QosOutWlan0Wlan0VoLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 5, 6, 1),
    _QosOutWlan0Wlan0VoLimit_Type()
)
qosOutWlan0Wlan0VoLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan0VoLimit.setStatus("current")
_QosOutWlan0Wlan0VoReserve_Type = OctetString
_QosOutWlan0Wlan0VoReserve_Object = MibScalar
qosOutWlan0Wlan0VoReserve = _QosOutWlan0Wlan0VoReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 5, 6, 2),
    _QosOutWlan0Wlan0VoReserve_Type()
)
qosOutWlan0Wlan0VoReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan0VoReserve.setStatus("current")
_QosOutWlan0Wlan1_ObjectIdentity = ObjectIdentity
qosOutWlan0Wlan1 = _QosOutWlan0Wlan1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 6)
)
_QosOutWlan0Wlan1Be_ObjectIdentity = ObjectIdentity
qosOutWlan0Wlan1Be = _QosOutWlan0Wlan1Be_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 6, 1)
)
_QosOutWlan0Wlan1BeLimit_Type = OctetString
_QosOutWlan0Wlan1BeLimit_Object = MibScalar
qosOutWlan0Wlan1BeLimit = _QosOutWlan0Wlan1BeLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 6, 1, 1),
    _QosOutWlan0Wlan1BeLimit_Type()
)
qosOutWlan0Wlan1BeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan1BeLimit.setStatus("current")
_QosOutWlan0Wlan1BeReserve_Type = OctetString
_QosOutWlan0Wlan1BeReserve_Object = MibScalar
qosOutWlan0Wlan1BeReserve = _QosOutWlan0Wlan1BeReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 6, 1, 2),
    _QosOutWlan0Wlan1BeReserve_Type()
)
qosOutWlan0Wlan1BeReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan1BeReserve.setStatus("current")
_QosOutWlan0Wlan1Bk_ObjectIdentity = ObjectIdentity
qosOutWlan0Wlan1Bk = _QosOutWlan0Wlan1Bk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 6, 2)
)
_QosOutWlan0Wlan1BkLimit_Type = OctetString
_QosOutWlan0Wlan1BkLimit_Object = MibScalar
qosOutWlan0Wlan1BkLimit = _QosOutWlan0Wlan1BkLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 6, 2, 1),
    _QosOutWlan0Wlan1BkLimit_Type()
)
qosOutWlan0Wlan1BkLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan1BkLimit.setStatus("current")
_QosOutWlan0Wlan1BkReserve_Type = OctetString
_QosOutWlan0Wlan1BkReserve_Object = MibScalar
qosOutWlan0Wlan1BkReserve = _QosOutWlan0Wlan1BkReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 6, 2, 2),
    _QosOutWlan0Wlan1BkReserve_Type()
)
qosOutWlan0Wlan1BkReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan1BkReserve.setStatus("current")
_QosOutWlan0Wlan1Limit_Type = OctetString
_QosOutWlan0Wlan1Limit_Object = MibScalar
qosOutWlan0Wlan1Limit = _QosOutWlan0Wlan1Limit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 6, 3),
    _QosOutWlan0Wlan1Limit_Type()
)
qosOutWlan0Wlan1Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan1Limit.setStatus("current")
_QosOutWlan0Wlan1Reserve_Type = OctetString
_QosOutWlan0Wlan1Reserve_Object = MibScalar
qosOutWlan0Wlan1Reserve = _QosOutWlan0Wlan1Reserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 6, 4),
    _QosOutWlan0Wlan1Reserve_Type()
)
qosOutWlan0Wlan1Reserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan1Reserve.setStatus("current")
_QosOutWlan0Wlan1Vi_ObjectIdentity = ObjectIdentity
qosOutWlan0Wlan1Vi = _QosOutWlan0Wlan1Vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 6, 5)
)
_QosOutWlan0Wlan1ViLimit_Type = OctetString
_QosOutWlan0Wlan1ViLimit_Object = MibScalar
qosOutWlan0Wlan1ViLimit = _QosOutWlan0Wlan1ViLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 6, 5, 1),
    _QosOutWlan0Wlan1ViLimit_Type()
)
qosOutWlan0Wlan1ViLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan1ViLimit.setStatus("current")
_QosOutWlan0Wlan1ViReserve_Type = OctetString
_QosOutWlan0Wlan1ViReserve_Object = MibScalar
qosOutWlan0Wlan1ViReserve = _QosOutWlan0Wlan1ViReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 6, 5, 2),
    _QosOutWlan0Wlan1ViReserve_Type()
)
qosOutWlan0Wlan1ViReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan1ViReserve.setStatus("current")
_QosOutWlan0Wlan1Vo_ObjectIdentity = ObjectIdentity
qosOutWlan0Wlan1Vo = _QosOutWlan0Wlan1Vo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 6, 6)
)
_QosOutWlan0Wlan1VoLimit_Type = OctetString
_QosOutWlan0Wlan1VoLimit_Object = MibScalar
qosOutWlan0Wlan1VoLimit = _QosOutWlan0Wlan1VoLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 6, 6, 1),
    _QosOutWlan0Wlan1VoLimit_Type()
)
qosOutWlan0Wlan1VoLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan1VoLimit.setStatus("current")
_QosOutWlan0Wlan1VoReserve_Type = OctetString
_QosOutWlan0Wlan1VoReserve_Object = MibScalar
qosOutWlan0Wlan1VoReserve = _QosOutWlan0Wlan1VoReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 6, 6, 2),
    _QosOutWlan0Wlan1VoReserve_Type()
)
qosOutWlan0Wlan1VoReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan1VoReserve.setStatus("current")
_QosOutWlan0Wlan2_ObjectIdentity = ObjectIdentity
qosOutWlan0Wlan2 = _QosOutWlan0Wlan2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 7)
)
_QosOutWlan0Wlan2Be_ObjectIdentity = ObjectIdentity
qosOutWlan0Wlan2Be = _QosOutWlan0Wlan2Be_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 7, 1)
)
_QosOutWlan0Wlan2BeLimit_Type = OctetString
_QosOutWlan0Wlan2BeLimit_Object = MibScalar
qosOutWlan0Wlan2BeLimit = _QosOutWlan0Wlan2BeLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 7, 1, 1),
    _QosOutWlan0Wlan2BeLimit_Type()
)
qosOutWlan0Wlan2BeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan2BeLimit.setStatus("current")
_QosOutWlan0Wlan2BeReserve_Type = OctetString
_QosOutWlan0Wlan2BeReserve_Object = MibScalar
qosOutWlan0Wlan2BeReserve = _QosOutWlan0Wlan2BeReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 7, 1, 2),
    _QosOutWlan0Wlan2BeReserve_Type()
)
qosOutWlan0Wlan2BeReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan2BeReserve.setStatus("current")
_QosOutWlan0Wlan2Bk_ObjectIdentity = ObjectIdentity
qosOutWlan0Wlan2Bk = _QosOutWlan0Wlan2Bk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 7, 2)
)
_QosOutWlan0Wlan2BkLimit_Type = OctetString
_QosOutWlan0Wlan2BkLimit_Object = MibScalar
qosOutWlan0Wlan2BkLimit = _QosOutWlan0Wlan2BkLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 7, 2, 1),
    _QosOutWlan0Wlan2BkLimit_Type()
)
qosOutWlan0Wlan2BkLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan2BkLimit.setStatus("current")
_QosOutWlan0Wlan2BkReserve_Type = OctetString
_QosOutWlan0Wlan2BkReserve_Object = MibScalar
qosOutWlan0Wlan2BkReserve = _QosOutWlan0Wlan2BkReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 7, 2, 2),
    _QosOutWlan0Wlan2BkReserve_Type()
)
qosOutWlan0Wlan2BkReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan2BkReserve.setStatus("current")
_QosOutWlan0Wlan2Limit_Type = OctetString
_QosOutWlan0Wlan2Limit_Object = MibScalar
qosOutWlan0Wlan2Limit = _QosOutWlan0Wlan2Limit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 7, 3),
    _QosOutWlan0Wlan2Limit_Type()
)
qosOutWlan0Wlan2Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan2Limit.setStatus("current")
_QosOutWlan0Wlan2Reserve_Type = OctetString
_QosOutWlan0Wlan2Reserve_Object = MibScalar
qosOutWlan0Wlan2Reserve = _QosOutWlan0Wlan2Reserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 7, 4),
    _QosOutWlan0Wlan2Reserve_Type()
)
qosOutWlan0Wlan2Reserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan2Reserve.setStatus("current")
_QosOutWlan0Wlan2Vi_ObjectIdentity = ObjectIdentity
qosOutWlan0Wlan2Vi = _QosOutWlan0Wlan2Vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 7, 5)
)
_QosOutWlan0Wlan2ViLimit_Type = OctetString
_QosOutWlan0Wlan2ViLimit_Object = MibScalar
qosOutWlan0Wlan2ViLimit = _QosOutWlan0Wlan2ViLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 7, 5, 1),
    _QosOutWlan0Wlan2ViLimit_Type()
)
qosOutWlan0Wlan2ViLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan2ViLimit.setStatus("current")
_QosOutWlan0Wlan2ViReserve_Type = OctetString
_QosOutWlan0Wlan2ViReserve_Object = MibScalar
qosOutWlan0Wlan2ViReserve = _QosOutWlan0Wlan2ViReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 7, 5, 2),
    _QosOutWlan0Wlan2ViReserve_Type()
)
qosOutWlan0Wlan2ViReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan2ViReserve.setStatus("current")
_QosOutWlan0Wlan2Vo_ObjectIdentity = ObjectIdentity
qosOutWlan0Wlan2Vo = _QosOutWlan0Wlan2Vo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 7, 6)
)
_QosOutWlan0Wlan2VoLimit_Type = OctetString
_QosOutWlan0Wlan2VoLimit_Object = MibScalar
qosOutWlan0Wlan2VoLimit = _QosOutWlan0Wlan2VoLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 7, 6, 1),
    _QosOutWlan0Wlan2VoLimit_Type()
)
qosOutWlan0Wlan2VoLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan2VoLimit.setStatus("current")
_QosOutWlan0Wlan2VoReserve_Type = OctetString
_QosOutWlan0Wlan2VoReserve_Object = MibScalar
qosOutWlan0Wlan2VoReserve = _QosOutWlan0Wlan2VoReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 7, 6, 2),
    _QosOutWlan0Wlan2VoReserve_Type()
)
qosOutWlan0Wlan2VoReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan2VoReserve.setStatus("current")
_QosOutWlan0Wlan3_ObjectIdentity = ObjectIdentity
qosOutWlan0Wlan3 = _QosOutWlan0Wlan3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 8)
)
_QosOutWlan0Wlan3Be_ObjectIdentity = ObjectIdentity
qosOutWlan0Wlan3Be = _QosOutWlan0Wlan3Be_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 8, 1)
)
_QosOutWlan0Wlan3BeLimit_Type = OctetString
_QosOutWlan0Wlan3BeLimit_Object = MibScalar
qosOutWlan0Wlan3BeLimit = _QosOutWlan0Wlan3BeLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 8, 1, 1),
    _QosOutWlan0Wlan3BeLimit_Type()
)
qosOutWlan0Wlan3BeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan3BeLimit.setStatus("current")
_QosOutWlan0Wlan3BeReserve_Type = OctetString
_QosOutWlan0Wlan3BeReserve_Object = MibScalar
qosOutWlan0Wlan3BeReserve = _QosOutWlan0Wlan3BeReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 8, 1, 2),
    _QosOutWlan0Wlan3BeReserve_Type()
)
qosOutWlan0Wlan3BeReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan3BeReserve.setStatus("current")
_QosOutWlan0Wlan3Bk_ObjectIdentity = ObjectIdentity
qosOutWlan0Wlan3Bk = _QosOutWlan0Wlan3Bk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 8, 2)
)
_QosOutWlan0Wlan3BkLimit_Type = OctetString
_QosOutWlan0Wlan3BkLimit_Object = MibScalar
qosOutWlan0Wlan3BkLimit = _QosOutWlan0Wlan3BkLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 8, 2, 1),
    _QosOutWlan0Wlan3BkLimit_Type()
)
qosOutWlan0Wlan3BkLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan3BkLimit.setStatus("current")
_QosOutWlan0Wlan3BkReserve_Type = OctetString
_QosOutWlan0Wlan3BkReserve_Object = MibScalar
qosOutWlan0Wlan3BkReserve = _QosOutWlan0Wlan3BkReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 8, 2, 2),
    _QosOutWlan0Wlan3BkReserve_Type()
)
qosOutWlan0Wlan3BkReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan3BkReserve.setStatus("current")
_QosOutWlan0Wlan3Limit_Type = OctetString
_QosOutWlan0Wlan3Limit_Object = MibScalar
qosOutWlan0Wlan3Limit = _QosOutWlan0Wlan3Limit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 8, 3),
    _QosOutWlan0Wlan3Limit_Type()
)
qosOutWlan0Wlan3Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan3Limit.setStatus("current")
_QosOutWlan0Wlan3Reserve_Type = OctetString
_QosOutWlan0Wlan3Reserve_Object = MibScalar
qosOutWlan0Wlan3Reserve = _QosOutWlan0Wlan3Reserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 8, 4),
    _QosOutWlan0Wlan3Reserve_Type()
)
qosOutWlan0Wlan3Reserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan3Reserve.setStatus("current")
_QosOutWlan0Wlan3Vi_ObjectIdentity = ObjectIdentity
qosOutWlan0Wlan3Vi = _QosOutWlan0Wlan3Vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 8, 5)
)
_QosOutWlan0Wlan3ViLimit_Type = OctetString
_QosOutWlan0Wlan3ViLimit_Object = MibScalar
qosOutWlan0Wlan3ViLimit = _QosOutWlan0Wlan3ViLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 8, 5, 1),
    _QosOutWlan0Wlan3ViLimit_Type()
)
qosOutWlan0Wlan3ViLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan3ViLimit.setStatus("current")
_QosOutWlan0Wlan3ViReserve_Type = OctetString
_QosOutWlan0Wlan3ViReserve_Object = MibScalar
qosOutWlan0Wlan3ViReserve = _QosOutWlan0Wlan3ViReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 8, 5, 2),
    _QosOutWlan0Wlan3ViReserve_Type()
)
qosOutWlan0Wlan3ViReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan3ViReserve.setStatus("current")
_QosOutWlan0Wlan3Vo_ObjectIdentity = ObjectIdentity
qosOutWlan0Wlan3Vo = _QosOutWlan0Wlan3Vo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 8, 6)
)
_QosOutWlan0Wlan3VoLimit_Type = OctetString
_QosOutWlan0Wlan3VoLimit_Object = MibScalar
qosOutWlan0Wlan3VoLimit = _QosOutWlan0Wlan3VoLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 8, 6, 1),
    _QosOutWlan0Wlan3VoLimit_Type()
)
qosOutWlan0Wlan3VoLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan3VoLimit.setStatus("current")
_QosOutWlan0Wlan3VoReserve_Type = OctetString
_QosOutWlan0Wlan3VoReserve_Object = MibScalar
qosOutWlan0Wlan3VoReserve = _QosOutWlan0Wlan3VoReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 8, 6, 2),
    _QosOutWlan0Wlan3VoReserve_Type()
)
qosOutWlan0Wlan3VoReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan3VoReserve.setStatus("current")
_QosOutWlan0Wlan4_ObjectIdentity = ObjectIdentity
qosOutWlan0Wlan4 = _QosOutWlan0Wlan4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 9)
)
_QosOutWlan0Wlan4Be_ObjectIdentity = ObjectIdentity
qosOutWlan0Wlan4Be = _QosOutWlan0Wlan4Be_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 9, 1)
)
_QosOutWlan0Wlan4BeLimit_Type = OctetString
_QosOutWlan0Wlan4BeLimit_Object = MibScalar
qosOutWlan0Wlan4BeLimit = _QosOutWlan0Wlan4BeLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 9, 1, 1),
    _QosOutWlan0Wlan4BeLimit_Type()
)
qosOutWlan0Wlan4BeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan4BeLimit.setStatus("current")
_QosOutWlan0Wlan4BeReserve_Type = OctetString
_QosOutWlan0Wlan4BeReserve_Object = MibScalar
qosOutWlan0Wlan4BeReserve = _QosOutWlan0Wlan4BeReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 9, 1, 2),
    _QosOutWlan0Wlan4BeReserve_Type()
)
qosOutWlan0Wlan4BeReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan4BeReserve.setStatus("current")
_QosOutWlan0Wlan4Bk_ObjectIdentity = ObjectIdentity
qosOutWlan0Wlan4Bk = _QosOutWlan0Wlan4Bk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 9, 2)
)
_QosOutWlan0Wlan4BkLimit_Type = OctetString
_QosOutWlan0Wlan4BkLimit_Object = MibScalar
qosOutWlan0Wlan4BkLimit = _QosOutWlan0Wlan4BkLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 9, 2, 1),
    _QosOutWlan0Wlan4BkLimit_Type()
)
qosOutWlan0Wlan4BkLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan4BkLimit.setStatus("current")
_QosOutWlan0Wlan4BkReserve_Type = OctetString
_QosOutWlan0Wlan4BkReserve_Object = MibScalar
qosOutWlan0Wlan4BkReserve = _QosOutWlan0Wlan4BkReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 9, 2, 2),
    _QosOutWlan0Wlan4BkReserve_Type()
)
qosOutWlan0Wlan4BkReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan4BkReserve.setStatus("current")
_QosOutWlan0Wlan4Limit_Type = OctetString
_QosOutWlan0Wlan4Limit_Object = MibScalar
qosOutWlan0Wlan4Limit = _QosOutWlan0Wlan4Limit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 9, 3),
    _QosOutWlan0Wlan4Limit_Type()
)
qosOutWlan0Wlan4Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan4Limit.setStatus("current")
_QosOutWlan0Wlan4Reserve_Type = OctetString
_QosOutWlan0Wlan4Reserve_Object = MibScalar
qosOutWlan0Wlan4Reserve = _QosOutWlan0Wlan4Reserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 9, 4),
    _QosOutWlan0Wlan4Reserve_Type()
)
qosOutWlan0Wlan4Reserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan4Reserve.setStatus("current")
_QosOutWlan0Wlan4Vi_ObjectIdentity = ObjectIdentity
qosOutWlan0Wlan4Vi = _QosOutWlan0Wlan4Vi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 9, 5)
)
_QosOutWlan0Wlan4ViLimit_Type = OctetString
_QosOutWlan0Wlan4ViLimit_Object = MibScalar
qosOutWlan0Wlan4ViLimit = _QosOutWlan0Wlan4ViLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 9, 5, 1),
    _QosOutWlan0Wlan4ViLimit_Type()
)
qosOutWlan0Wlan4ViLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan4ViLimit.setStatus("current")
_QosOutWlan0Wlan4ViReserve_Type = OctetString
_QosOutWlan0Wlan4ViReserve_Object = MibScalar
qosOutWlan0Wlan4ViReserve = _QosOutWlan0Wlan4ViReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 9, 5, 2),
    _QosOutWlan0Wlan4ViReserve_Type()
)
qosOutWlan0Wlan4ViReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan4ViReserve.setStatus("current")
_QosOutWlan0Wlan4Vo_ObjectIdentity = ObjectIdentity
qosOutWlan0Wlan4Vo = _QosOutWlan0Wlan4Vo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 9, 6)
)
_QosOutWlan0Wlan4VoLimit_Type = OctetString
_QosOutWlan0Wlan4VoLimit_Object = MibScalar
qosOutWlan0Wlan4VoLimit = _QosOutWlan0Wlan4VoLimit_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 9, 6, 1),
    _QosOutWlan0Wlan4VoLimit_Type()
)
qosOutWlan0Wlan4VoLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan4VoLimit.setStatus("current")
_QosOutWlan0Wlan4VoReserve_Type = OctetString
_QosOutWlan0Wlan4VoReserve_Object = MibScalar
qosOutWlan0Wlan4VoReserve = _QosOutWlan0Wlan4VoReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 4, 4, 2, 9, 6, 2),
    _QosOutWlan0Wlan4VoReserve_Type()
)
qosOutWlan0Wlan4VoReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosOutWlan0Wlan4VoReserve.setStatus("current")
_Logs_ObjectIdentity = ObjectIdentity
logs = _Logs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 5)
)
_LogsMconfd_ObjectIdentity = ObjectIdentity
logsMconfd = _LogsMconfd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 5, 1)
)
_LogsMconfdFiles_Type = Integer32
_LogsMconfdFiles_Object = MibScalar
logsMconfdFiles = _LogsMconfdFiles_Object(
    (1, 3, 6, 1, 4, 1, 24350, 5, 1, 1),
    _LogsMconfdFiles_Type()
)
logsMconfdFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logsMconfdFiles.setStatus("current")
_LogsMconfdSize_Type = OctetString
_LogsMconfdSize_Object = MibScalar
logsMconfdSize = _LogsMconfdSize_Object(
    (1, 3, 6, 1, 4, 1, 24350, 5, 1, 2),
    _LogsMconfdSize_Type()
)
logsMconfdSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logsMconfdSize.setStatus("current")
_LogsSecure_ObjectIdentity = ObjectIdentity
logsSecure = _LogsSecure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 5, 2)
)
_LogsSecureFiles_Type = Integer32
_LogsSecureFiles_Object = MibScalar
logsSecureFiles = _LogsSecureFiles_Object(
    (1, 3, 6, 1, 4, 1, 24350, 5, 2, 1),
    _LogsSecureFiles_Type()
)
logsSecureFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logsSecureFiles.setStatus("current")
_LogsSecureSize_Type = OctetString
_LogsSecureSize_Object = MibScalar
logsSecureSize = _LogsSecureSize_Object(
    (1, 3, 6, 1, 4, 1, 24350, 5, 2, 2),
    _LogsSecureSize_Type()
)
logsSecureSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logsSecureSize.setStatus("current")
_LogsSnmp_ObjectIdentity = ObjectIdentity
logsSnmp = _LogsSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 5, 3)
)
_LogsSnmpFiles_Type = Integer32
_LogsSnmpFiles_Object = MibScalar
logsSnmpFiles = _LogsSnmpFiles_Object(
    (1, 3, 6, 1, 4, 1, 24350, 5, 3, 1),
    _LogsSnmpFiles_Type()
)
logsSnmpFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logsSnmpFiles.setStatus("current")
_LogsSnmpSize_Type = OctetString
_LogsSnmpSize_Object = MibScalar
logsSnmpSize = _LogsSnmpSize_Object(
    (1, 3, 6, 1, 4, 1, 24350, 5, 3, 2),
    _LogsSnmpSize_Type()
)
logsSnmpSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logsSnmpSize.setStatus("current")
_LogsSyslog_ObjectIdentity = ObjectIdentity
logsSyslog = _LogsSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 5, 4)
)
_LogsSyslogFiles_Type = Integer32
_LogsSyslogFiles_Object = MibScalar
logsSyslogFiles = _LogsSyslogFiles_Object(
    (1, 3, 6, 1, 4, 1, 24350, 5, 4, 1),
    _LogsSyslogFiles_Type()
)
logsSyslogFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logsSyslogFiles.setStatus("current")
_LogsSyslogSize_Type = OctetString
_LogsSyslogSize_Object = MibScalar
logsSyslogSize = _LogsSyslogSize_Object(
    (1, 3, 6, 1, 4, 1, 24350, 5, 4, 2),
    _LogsSyslogSize_Type()
)
logsSyslogSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logsSyslogSize.setStatus("current")
_Eth0_ObjectIdentity = ObjectIdentity
eth0 = _Eth0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 6)
)
_Eth0Acl_ObjectIdentity = ObjectIdentity
eth0Acl = _Eth0Acl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 6, 1)
)
_Eth0AclMode_Type = OctetString
_Eth0AclMode_Object = MibScalar
eth0AclMode = _Eth0AclMode_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 1, 1),
    _Eth0AclMode_Type()
)
eth0AclMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth0AclMode.setStatus("current")
_Eth0Dhcp_ObjectIdentity = ObjectIdentity
eth0Dhcp = _Eth0Dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 6, 2)
)
_Eth0DhcpAlwaysbroadcast_Type = OctetString
_Eth0DhcpAlwaysbroadcast_Object = MibScalar
eth0DhcpAlwaysbroadcast = _Eth0DhcpAlwaysbroadcast_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 2, 1),
    _Eth0DhcpAlwaysbroadcast_Type()
)
eth0DhcpAlwaysbroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth0DhcpAlwaysbroadcast.setStatus("current")
_Eth0DhcpDefaultleasetime_Type = Integer32
_Eth0DhcpDefaultleasetime_Object = MibScalar
eth0DhcpDefaultleasetime = _Eth0DhcpDefaultleasetime_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 2, 2),
    _Eth0DhcpDefaultleasetime_Type()
)
eth0DhcpDefaultleasetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth0DhcpDefaultleasetime.setStatus("current")
_Eth0DhcpMaxleasetime_Type = Integer32
_Eth0DhcpMaxleasetime_Object = MibScalar
eth0DhcpMaxleasetime = _Eth0DhcpMaxleasetime_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 2, 3),
    _Eth0DhcpMaxleasetime_Type()
)
eth0DhcpMaxleasetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth0DhcpMaxleasetime.setStatus("current")
_Eth0DhcpRelay_ObjectIdentity = ObjectIdentity
eth0DhcpRelay = _Eth0DhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 6, 2, 4)
)
_Eth0DhcpRelayEnable_Type = OctetString
_Eth0DhcpRelayEnable_Object = MibScalar
eth0DhcpRelayEnable = _Eth0DhcpRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 2, 4, 1),
    _Eth0DhcpRelayEnable_Type()
)
eth0DhcpRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth0DhcpRelayEnable.setStatus("current")
_Eth0DhcpReserve_Type = Integer32
_Eth0DhcpReserve_Object = MibScalar
eth0DhcpReserve = _Eth0DhcpReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 2, 5),
    _Eth0DhcpReserve_Type()
)
eth0DhcpReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth0DhcpReserve.setStatus("current")
_Eth0DhcpRole_Type = OctetString
_Eth0DhcpRole_Object = MibScalar
eth0DhcpRole = _Eth0DhcpRole_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 2, 6),
    _Eth0DhcpRole_Type()
)
eth0DhcpRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth0DhcpRole.setStatus("current")
_Eth0Enable_Type = OctetString
_Eth0Enable_Object = MibScalar
eth0Enable = _Eth0Enable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 3),
    _Eth0Enable_Type()
)
eth0Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth0Enable.setStatus("current")
_Eth0If_Type = OctetString
_Eth0If_Object = MibScalar
eth0If = _Eth0If_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 4),
    _Eth0If_Type()
)
eth0If.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth0If.setStatus("current")
_Eth0Ip_ObjectIdentity = ObjectIdentity
eth0Ip = _Eth0Ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 6, 5)
)
_Eth0IpAddress_Type = OctetString
_Eth0IpAddress_Object = MibScalar
eth0IpAddress = _Eth0IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 5, 1),
    _Eth0IpAddress_Type()
)
eth0IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth0IpAddress.setStatus("current")
_Eth0IpAddressforce_Type = OctetString
_Eth0IpAddressforce_Object = MibScalar
eth0IpAddressforce = _Eth0IpAddressforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 5, 2),
    _Eth0IpAddressforce_Type()
)
eth0IpAddressforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth0IpAddressforce.setStatus("current")
_Eth0IpBroadcast_Type = OctetString
_Eth0IpBroadcast_Object = MibScalar
eth0IpBroadcast = _Eth0IpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 5, 3),
    _Eth0IpBroadcast_Type()
)
eth0IpBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth0IpBroadcast.setStatus("current")
_Eth0IpBroadcastforce_Type = OctetString
_Eth0IpBroadcastforce_Object = MibScalar
eth0IpBroadcastforce = _Eth0IpBroadcastforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 5, 4),
    _Eth0IpBroadcastforce_Type()
)
eth0IpBroadcastforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth0IpBroadcastforce.setStatus("current")
_Eth0IpGateway_Type = OctetString
_Eth0IpGateway_Object = MibScalar
eth0IpGateway = _Eth0IpGateway_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 5, 5),
    _Eth0IpGateway_Type()
)
eth0IpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth0IpGateway.setStatus("current")
_Eth0IpGatewayforce_Type = OctetString
_Eth0IpGatewayforce_Object = MibScalar
eth0IpGatewayforce = _Eth0IpGatewayforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 5, 6),
    _Eth0IpGatewayforce_Type()
)
eth0IpGatewayforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth0IpGatewayforce.setStatus("current")
_Eth0IpImplicit_ObjectIdentity = ObjectIdentity
eth0IpImplicit = _Eth0IpImplicit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 6, 5, 7)
)
_Eth0IpImplicitSize_ObjectIdentity = ObjectIdentity
eth0IpImplicitSize = _Eth0IpImplicitSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 6, 5, 7, 1)
)
_Eth0IpImplicitSizeActual_Type = Integer32
_Eth0IpImplicitSizeActual_Object = MibScalar
eth0IpImplicitSizeActual = _Eth0IpImplicitSizeActual_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 5, 7, 1, 1),
    _Eth0IpImplicitSizeActual_Type()
)
eth0IpImplicitSizeActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth0IpImplicitSizeActual.setStatus("current")
_Eth0IpImplicitSizeRequested_Type = OctetString
_Eth0IpImplicitSizeRequested_Object = MibScalar
eth0IpImplicitSizeRequested = _Eth0IpImplicitSizeRequested_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 5, 7, 1, 2),
    _Eth0IpImplicitSizeRequested_Type()
)
eth0IpImplicitSizeRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth0IpImplicitSizeRequested.setStatus("current")
_Eth0IpImplicitStart_ObjectIdentity = ObjectIdentity
eth0IpImplicitStart = _Eth0IpImplicitStart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 6, 5, 7, 2)
)
_Eth0IpImplicitStartActual_Type = Integer32
_Eth0IpImplicitStartActual_Object = MibScalar
eth0IpImplicitStartActual = _Eth0IpImplicitStartActual_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 5, 7, 2, 1),
    _Eth0IpImplicitStartActual_Type()
)
eth0IpImplicitStartActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth0IpImplicitStartActual.setStatus("current")
_Eth0IpImplicitStartRequested_Type = OctetString
_Eth0IpImplicitStartRequested_Object = MibScalar
eth0IpImplicitStartRequested = _Eth0IpImplicitStartRequested_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 5, 7, 2, 2),
    _Eth0IpImplicitStartRequested_Type()
)
eth0IpImplicitStartRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth0IpImplicitStartRequested.setStatus("current")
_Eth0IpNetmask_Type = OctetString
_Eth0IpNetmask_Object = MibScalar
eth0IpNetmask = _Eth0IpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 5, 8),
    _Eth0IpNetmask_Type()
)
eth0IpNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth0IpNetmask.setStatus("current")
_Eth0IpNetmaskforce_Type = OctetString
_Eth0IpNetmaskforce_Object = MibScalar
eth0IpNetmaskforce = _Eth0IpNetmaskforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 5, 9),
    _Eth0IpNetmaskforce_Type()
)
eth0IpNetmaskforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth0IpNetmaskforce.setStatus("current")
_Eth0Role_Type = OctetString
_Eth0Role_Object = MibScalar
eth0Role = _Eth0Role_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 6),
    _Eth0Role_Type()
)
eth0Role.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth0Role.setStatus("current")
_Eth0Routes_ObjectIdentity = ObjectIdentity
eth0Routes = _Eth0Routes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 6, 7)
)
_Eth0RoutesStatic_Type = OctetString
_Eth0RoutesStatic_Object = MibScalar
eth0RoutesStatic = _Eth0RoutesStatic_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 7, 1),
    _Eth0RoutesStatic_Type()
)
eth0RoutesStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth0RoutesStatic.setStatus("current")
_Eth0Vlan_ObjectIdentity = ObjectIdentity
eth0Vlan = _Eth0Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 6, 8)
)
_Eth0VlanEnable_Type = OctetString
_Eth0VlanEnable_Object = MibScalar
eth0VlanEnable = _Eth0VlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 8, 1),
    _Eth0VlanEnable_Type()
)
eth0VlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth0VlanEnable.setStatus("current")
_Eth0VlanId_Type = Integer32
_Eth0VlanId_Object = MibScalar
eth0VlanId = _Eth0VlanId_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 8, 2),
    _Eth0VlanId_Type()
)
eth0VlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth0VlanId.setStatus("current")
_Eth0Vpn_ObjectIdentity = ObjectIdentity
eth0Vpn = _Eth0Vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 6, 9)
)
_Eth0VpnDevice_Type = OctetString
_Eth0VpnDevice_Object = MibScalar
eth0VpnDevice = _Eth0VpnDevice_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 9, 1),
    _Eth0VpnDevice_Type()
)
eth0VpnDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth0VpnDevice.setStatus("current")
_Eth0VpnEnable_Type = OctetString
_Eth0VpnEnable_Object = MibScalar
eth0VpnEnable = _Eth0VpnEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 9, 2),
    _Eth0VpnEnable_Type()
)
eth0VpnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth0VpnEnable.setStatus("current")
_Eth0VpnKeyfile_Type = OctetString
_Eth0VpnKeyfile_Object = MibScalar
eth0VpnKeyfile = _Eth0VpnKeyfile_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 9, 3),
    _Eth0VpnKeyfile_Type()
)
eth0VpnKeyfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth0VpnKeyfile.setStatus("current")
_Eth0VpnPort_Type = Integer32
_Eth0VpnPort_Object = MibScalar
eth0VpnPort = _Eth0VpnPort_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 9, 4),
    _Eth0VpnPort_Type()
)
eth0VpnPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth0VpnPort.setStatus("current")
_Eth0VpnProtocol_Type = OctetString
_Eth0VpnProtocol_Object = MibScalar
eth0VpnProtocol = _Eth0VpnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 9, 5),
    _Eth0VpnProtocol_Type()
)
eth0VpnProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth0VpnProtocol.setStatus("current")
_Eth0VpnServer_Type = OctetString
_Eth0VpnServer_Object = MibScalar
eth0VpnServer = _Eth0VpnServer_Object(
    (1, 3, 6, 1, 4, 1, 24350, 6, 9, 6),
    _Eth0VpnServer_Type()
)
eth0VpnServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth0VpnServer.setStatus("current")
_Br0_ObjectIdentity = ObjectIdentity
br0 = _Br0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 7)
)
_Br0Acl_ObjectIdentity = ObjectIdentity
br0Acl = _Br0Acl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 7, 1)
)
_Br0AclMode_Type = OctetString
_Br0AclMode_Object = MibScalar
br0AclMode = _Br0AclMode_Object(
    (1, 3, 6, 1, 4, 1, 24350, 7, 1, 1),
    _Br0AclMode_Type()
)
br0AclMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    br0AclMode.setStatus("current")
_Br0Dhcp_ObjectIdentity = ObjectIdentity
br0Dhcp = _Br0Dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 7, 2)
)
_Br0DhcpAlwaysbroadcast_Type = OctetString
_Br0DhcpAlwaysbroadcast_Object = MibScalar
br0DhcpAlwaysbroadcast = _Br0DhcpAlwaysbroadcast_Object(
    (1, 3, 6, 1, 4, 1, 24350, 7, 2, 1),
    _Br0DhcpAlwaysbroadcast_Type()
)
br0DhcpAlwaysbroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    br0DhcpAlwaysbroadcast.setStatus("current")
_Br0DhcpDefaultleasetime_Type = Integer32
_Br0DhcpDefaultleasetime_Object = MibScalar
br0DhcpDefaultleasetime = _Br0DhcpDefaultleasetime_Object(
    (1, 3, 6, 1, 4, 1, 24350, 7, 2, 2),
    _Br0DhcpDefaultleasetime_Type()
)
br0DhcpDefaultleasetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    br0DhcpDefaultleasetime.setStatus("current")
_Br0DhcpMaxleasetime_Type = Integer32
_Br0DhcpMaxleasetime_Object = MibScalar
br0DhcpMaxleasetime = _Br0DhcpMaxleasetime_Object(
    (1, 3, 6, 1, 4, 1, 24350, 7, 2, 3),
    _Br0DhcpMaxleasetime_Type()
)
br0DhcpMaxleasetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    br0DhcpMaxleasetime.setStatus("current")
_Br0DhcpRelay_ObjectIdentity = ObjectIdentity
br0DhcpRelay = _Br0DhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 7, 2, 4)
)
_Br0DhcpRelayEnable_Type = OctetString
_Br0DhcpRelayEnable_Object = MibScalar
br0DhcpRelayEnable = _Br0DhcpRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 7, 2, 4, 1),
    _Br0DhcpRelayEnable_Type()
)
br0DhcpRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    br0DhcpRelayEnable.setStatus("current")
_Br0DhcpReserve_Type = Integer32
_Br0DhcpReserve_Object = MibScalar
br0DhcpReserve = _Br0DhcpReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 7, 2, 5),
    _Br0DhcpReserve_Type()
)
br0DhcpReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    br0DhcpReserve.setStatus("current")
_Br0DhcpRole_Type = OctetString
_Br0DhcpRole_Object = MibScalar
br0DhcpRole = _Br0DhcpRole_Object(
    (1, 3, 6, 1, 4, 1, 24350, 7, 2, 6),
    _Br0DhcpRole_Type()
)
br0DhcpRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    br0DhcpRole.setStatus("current")
_Br0Enable_Type = OctetString
_Br0Enable_Object = MibScalar
br0Enable = _Br0Enable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 7, 3),
    _Br0Enable_Type()
)
br0Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    br0Enable.setStatus("current")
_Br0Forwardingdelay_Type = Integer32
_Br0Forwardingdelay_Object = MibScalar
br0Forwardingdelay = _Br0Forwardingdelay_Object(
    (1, 3, 6, 1, 4, 1, 24350, 7, 4),
    _Br0Forwardingdelay_Type()
)
br0Forwardingdelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    br0Forwardingdelay.setStatus("current")
_Br0If_Type = OctetString
_Br0If_Object = MibScalar
br0If = _Br0If_Object(
    (1, 3, 6, 1, 4, 1, 24350, 7, 5),
    _Br0If_Type()
)
br0If.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    br0If.setStatus("current")
_Br0Ip_ObjectIdentity = ObjectIdentity
br0Ip = _Br0Ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 7, 6)
)
_Br0IpAddress_Type = OctetString
_Br0IpAddress_Object = MibScalar
br0IpAddress = _Br0IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 24350, 7, 6, 1),
    _Br0IpAddress_Type()
)
br0IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    br0IpAddress.setStatus("current")
_Br0IpAddressforce_Type = OctetString
_Br0IpAddressforce_Object = MibScalar
br0IpAddressforce = _Br0IpAddressforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 7, 6, 2),
    _Br0IpAddressforce_Type()
)
br0IpAddressforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    br0IpAddressforce.setStatus("current")
_Br0IpBroadcast_Type = OctetString
_Br0IpBroadcast_Object = MibScalar
br0IpBroadcast = _Br0IpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 24350, 7, 6, 3),
    _Br0IpBroadcast_Type()
)
br0IpBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    br0IpBroadcast.setStatus("current")
_Br0IpBroadcastforce_Type = OctetString
_Br0IpBroadcastforce_Object = MibScalar
br0IpBroadcastforce = _Br0IpBroadcastforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 7, 6, 4),
    _Br0IpBroadcastforce_Type()
)
br0IpBroadcastforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    br0IpBroadcastforce.setStatus("current")
_Br0IpGateway_Type = OctetString
_Br0IpGateway_Object = MibScalar
br0IpGateway = _Br0IpGateway_Object(
    (1, 3, 6, 1, 4, 1, 24350, 7, 6, 5),
    _Br0IpGateway_Type()
)
br0IpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    br0IpGateway.setStatus("current")
_Br0IpGatewayforce_Type = OctetString
_Br0IpGatewayforce_Object = MibScalar
br0IpGatewayforce = _Br0IpGatewayforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 7, 6, 6),
    _Br0IpGatewayforce_Type()
)
br0IpGatewayforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    br0IpGatewayforce.setStatus("current")
_Br0IpNetmask_Type = OctetString
_Br0IpNetmask_Object = MibScalar
br0IpNetmask = _Br0IpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 24350, 7, 6, 7),
    _Br0IpNetmask_Type()
)
br0IpNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    br0IpNetmask.setStatus("current")
_Br0IpNetmaskforce_Type = OctetString
_Br0IpNetmaskforce_Object = MibScalar
br0IpNetmaskforce = _Br0IpNetmaskforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 7, 6, 8),
    _Br0IpNetmaskforce_Type()
)
br0IpNetmaskforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    br0IpNetmaskforce.setStatus("current")
_Br0Role_Type = OctetString
_Br0Role_Object = MibScalar
br0Role = _Br0Role_Object(
    (1, 3, 6, 1, 4, 1, 24350, 7, 7),
    _Br0Role_Type()
)
br0Role.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    br0Role.setStatus("current")
_Br0Routes_ObjectIdentity = ObjectIdentity
br0Routes = _Br0Routes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 7, 8)
)
_Br0RoutesStatic_Type = OctetString
_Br0RoutesStatic_Object = MibScalar
br0RoutesStatic = _Br0RoutesStatic_Object(
    (1, 3, 6, 1, 4, 1, 24350, 7, 8, 1),
    _Br0RoutesStatic_Type()
)
br0RoutesStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    br0RoutesStatic.setStatus("current")
_Br0Stp_ObjectIdentity = ObjectIdentity
br0Stp = _Br0Stp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 7, 9)
)
_Br0StpEnable_Type = OctetString
_Br0StpEnable_Object = MibScalar
br0StpEnable = _Br0StpEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 7, 9, 1),
    _Br0StpEnable_Type()
)
br0StpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    br0StpEnable.setStatus("current")
_Alias99_ObjectIdentity = ObjectIdentity
alias99 = _Alias99_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 8)
)
_Alias99If_Type = OctetString
_Alias99If_Object = MibScalar
alias99If = _Alias99If_Object(
    (1, 3, 6, 1, 4, 1, 24350, 8, 1),
    _Alias99If_Type()
)
alias99If.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alias99If.setStatus("current")
_Alias99Ip_ObjectIdentity = ObjectIdentity
alias99Ip = _Alias99Ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 8, 2)
)
_Alias99IpAddress_Type = OctetString
_Alias99IpAddress_Object = MibScalar
alias99IpAddress = _Alias99IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 24350, 8, 2, 1),
    _Alias99IpAddress_Type()
)
alias99IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alias99IpAddress.setStatus("current")
_Alias99IpBroadcast_Type = OctetString
_Alias99IpBroadcast_Object = MibScalar
alias99IpBroadcast = _Alias99IpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 24350, 8, 2, 2),
    _Alias99IpBroadcast_Type()
)
alias99IpBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alias99IpBroadcast.setStatus("current")
_Alias99IpGateway_Type = OctetString
_Alias99IpGateway_Object = MibScalar
alias99IpGateway = _Alias99IpGateway_Object(
    (1, 3, 6, 1, 4, 1, 24350, 8, 2, 3),
    _Alias99IpGateway_Type()
)
alias99IpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alias99IpGateway.setStatus("current")
_Alias99IpNetmask_Type = OctetString
_Alias99IpNetmask_Object = MibScalar
alias99IpNetmask = _Alias99IpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 24350, 8, 2, 4),
    _Alias99IpNetmask_Type()
)
alias99IpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alias99IpNetmask.setStatus("current")
_Radio0_ObjectIdentity = ObjectIdentity
radio0 = _Radio0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 9)
)
_Radio0Channel_Type = Integer32
_Radio0Channel_Object = MibScalar
radio0Channel = _Radio0Channel_Object(
    (1, 3, 6, 1, 4, 1, 24350, 9, 1),
    _Radio0Channel_Type()
)
radio0Channel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radio0Channel.setStatus("current")
_Radio0Chansize_Type = OctetString
_Radio0Chansize_Object = MibScalar
radio0Chansize = _Radio0Chansize_Object(
    (1, 3, 6, 1, 4, 1, 24350, 9, 2),
    _Radio0Chansize_Type()
)
radio0Chansize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radio0Chansize.setStatus("current")
_Radio0Distance_Type = OctetString
_Radio0Distance_Object = MibScalar
radio0Distance = _Radio0Distance_Object(
    (1, 3, 6, 1, 4, 1, 24350, 9, 3),
    _Radio0Distance_Type()
)
radio0Distance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radio0Distance.setStatus("current")
_Radio0Distancemeters_Type = OctetString
_Radio0Distancemeters_Object = MibScalar
radio0Distancemeters = _Radio0Distancemeters_Object(
    (1, 3, 6, 1, 4, 1, 24350, 9, 4),
    _Radio0Distancemeters_Type()
)
radio0Distancemeters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radio0Distancemeters.setStatus("current")
_Radio0Frequency_Type = OctetString
_Radio0Frequency_Object = MibScalar
radio0Frequency = _Radio0Frequency_Object(
    (1, 3, 6, 1, 4, 1, 24350, 9, 5),
    _Radio0Frequency_Type()
)
radio0Frequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radio0Frequency.setStatus("current")
_Radio0Mode_Type = Integer32
_Radio0Mode_Object = MibScalar
radio0Mode = _Radio0Mode_Object(
    (1, 3, 6, 1, 4, 1, 24350, 9, 6),
    _Radio0Mode_Type()
)
radio0Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radio0Mode.setStatus("current")
_Radio0Modes_Type = OctetString
_Radio0Modes_Object = MibScalar
radio0Modes = _Radio0Modes_Object(
    (1, 3, 6, 1, 4, 1, 24350, 9, 7),
    _Radio0Modes_Type()
)
radio0Modes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radio0Modes.setStatus("current")
_Radio0Pureg_Type = OctetString
_Radio0Pureg_Object = MibScalar
radio0Pureg = _Radio0Pureg_Object(
    (1, 3, 6, 1, 4, 1, 24350, 9, 8),
    _Radio0Pureg_Type()
)
radio0Pureg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radio0Pureg.setStatus("current")
_Radio0Ratectl_Type = OctetString
_Radio0Ratectl_Object = MibScalar
radio0Ratectl = _Radio0Ratectl_Object(
    (1, 3, 6, 1, 4, 1, 24350, 9, 9),
    _Radio0Ratectl_Type()
)
radio0Ratectl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radio0Ratectl.setStatus("current")
_Radio0Rts_Type = OctetString
_Radio0Rts_Object = MibScalar
radio0Rts = _Radio0Rts_Object(
    (1, 3, 6, 1, 4, 1, 24350, 9, 10),
    _Radio0Rts_Type()
)
radio0Rts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radio0Rts.setStatus("current")
_Radio0Shortpreamble_Type = OctetString
_Radio0Shortpreamble_Object = MibScalar
radio0Shortpreamble = _Radio0Shortpreamble_Object(
    (1, 3, 6, 1, 4, 1, 24350, 9, 11),
    _Radio0Shortpreamble_Type()
)
radio0Shortpreamble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radio0Shortpreamble.setStatus("current")
_Radio0Turbo_Type = OctetString
_Radio0Turbo_Object = MibScalar
radio0Turbo = _Radio0Turbo_Object(
    (1, 3, 6, 1, 4, 1, 24350, 9, 12),
    _Radio0Turbo_Type()
)
radio0Turbo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radio0Turbo.setStatus("current")
_Radio0Txpower_Type = OctetString
_Radio0Txpower_Object = MibScalar
radio0Txpower = _Radio0Txpower_Object(
    (1, 3, 6, 1, 4, 1, 24350, 9, 13),
    _Radio0Txpower_Type()
)
radio0Txpower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radio0Txpower.setStatus("current")
_Radio0Wlans_Type = OctetString
_Radio0Wlans_Object = MibScalar
radio0Wlans = _Radio0Wlans_Object(
    (1, 3, 6, 1, 4, 1, 24350, 9, 14),
    _Radio0Wlans_Type()
)
radio0Wlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radio0Wlans.setStatus("current")
_Radio0Wlansextra_Type = OctetString
_Radio0Wlansextra_Object = MibScalar
radio0Wlansextra = _Radio0Wlansextra_Object(
    (1, 3, 6, 1, 4, 1, 24350, 9, 15),
    _Radio0Wlansextra_Type()
)
radio0Wlansextra.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radio0Wlansextra.setStatus("current")
_Radio1_ObjectIdentity = ObjectIdentity
radio1 = _Radio1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 10)
)
_Radio1Channel_Type = Integer32
_Radio1Channel_Object = MibScalar
radio1Channel = _Radio1Channel_Object(
    (1, 3, 6, 1, 4, 1, 24350, 10, 1),
    _Radio1Channel_Type()
)
radio1Channel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radio1Channel.setStatus("current")
_Radio1Chansize_Type = OctetString
_Radio1Chansize_Object = MibScalar
radio1Chansize = _Radio1Chansize_Object(
    (1, 3, 6, 1, 4, 1, 24350, 10, 2),
    _Radio1Chansize_Type()
)
radio1Chansize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radio1Chansize.setStatus("current")
_Radio1Distance_Type = OctetString
_Radio1Distance_Object = MibScalar
radio1Distance = _Radio1Distance_Object(
    (1, 3, 6, 1, 4, 1, 24350, 10, 3),
    _Radio1Distance_Type()
)
radio1Distance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radio1Distance.setStatus("current")
_Radio1Distancemeters_Type = OctetString
_Radio1Distancemeters_Object = MibScalar
radio1Distancemeters = _Radio1Distancemeters_Object(
    (1, 3, 6, 1, 4, 1, 24350, 10, 4),
    _Radio1Distancemeters_Type()
)
radio1Distancemeters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radio1Distancemeters.setStatus("current")
_Radio1Frequency_Type = OctetString
_Radio1Frequency_Object = MibScalar
radio1Frequency = _Radio1Frequency_Object(
    (1, 3, 6, 1, 4, 1, 24350, 10, 5),
    _Radio1Frequency_Type()
)
radio1Frequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radio1Frequency.setStatus("current")
_Radio1Mode_Type = Integer32
_Radio1Mode_Object = MibScalar
radio1Mode = _Radio1Mode_Object(
    (1, 3, 6, 1, 4, 1, 24350, 10, 6),
    _Radio1Mode_Type()
)
radio1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radio1Mode.setStatus("current")
_Radio1Modes_Type = OctetString
_Radio1Modes_Object = MibScalar
radio1Modes = _Radio1Modes_Object(
    (1, 3, 6, 1, 4, 1, 24350, 10, 7),
    _Radio1Modes_Type()
)
radio1Modes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radio1Modes.setStatus("current")
_Radio1Pureg_Type = OctetString
_Radio1Pureg_Object = MibScalar
radio1Pureg = _Radio1Pureg_Object(
    (1, 3, 6, 1, 4, 1, 24350, 10, 8),
    _Radio1Pureg_Type()
)
radio1Pureg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radio1Pureg.setStatus("current")
_Radio1Ratectl_Type = OctetString
_Radio1Ratectl_Object = MibScalar
radio1Ratectl = _Radio1Ratectl_Object(
    (1, 3, 6, 1, 4, 1, 24350, 10, 9),
    _Radio1Ratectl_Type()
)
radio1Ratectl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radio1Ratectl.setStatus("current")
_Radio1Rts_Type = OctetString
_Radio1Rts_Object = MibScalar
radio1Rts = _Radio1Rts_Object(
    (1, 3, 6, 1, 4, 1, 24350, 10, 10),
    _Radio1Rts_Type()
)
radio1Rts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radio1Rts.setStatus("current")
_Radio1Shortpreamble_Type = OctetString
_Radio1Shortpreamble_Object = MibScalar
radio1Shortpreamble = _Radio1Shortpreamble_Object(
    (1, 3, 6, 1, 4, 1, 24350, 10, 11),
    _Radio1Shortpreamble_Type()
)
radio1Shortpreamble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radio1Shortpreamble.setStatus("current")
_Radio1Turbo_Type = OctetString
_Radio1Turbo_Object = MibScalar
radio1Turbo = _Radio1Turbo_Object(
    (1, 3, 6, 1, 4, 1, 24350, 10, 12),
    _Radio1Turbo_Type()
)
radio1Turbo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radio1Turbo.setStatus("current")
_Radio1Txpower_Type = OctetString
_Radio1Txpower_Object = MibScalar
radio1Txpower = _Radio1Txpower_Object(
    (1, 3, 6, 1, 4, 1, 24350, 10, 13),
    _Radio1Txpower_Type()
)
radio1Txpower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radio1Txpower.setStatus("current")
_Radio1Wlans_Type = OctetString
_Radio1Wlans_Object = MibScalar
radio1Wlans = _Radio1Wlans_Object(
    (1, 3, 6, 1, 4, 1, 24350, 10, 14),
    _Radio1Wlans_Type()
)
radio1Wlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radio1Wlans.setStatus("current")
_Radio1Wlansextra_Type = OctetString
_Radio1Wlansextra_Object = MibScalar
radio1Wlansextra = _Radio1Wlansextra_Object(
    (1, 3, 6, 1, 4, 1, 24350, 10, 15),
    _Radio1Wlansextra_Type()
)
radio1Wlansextra.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radio1Wlansextra.setStatus("current")
_Wlan0_ObjectIdentity = ObjectIdentity
wlan0 = _Wlan0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 11)
)
_Wlan0Acl_ObjectIdentity = ObjectIdentity
wlan0Acl = _Wlan0Acl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 11, 1)
)
_Wlan0AclMode_Type = OctetString
_Wlan0AclMode_Object = MibScalar
wlan0AclMode = _Wlan0AclMode_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 1, 1),
    _Wlan0AclMode_Type()
)
wlan0AclMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0AclMode.setStatus("current")
_Wlan0Beaconinterval_Type = Integer32
_Wlan0Beaconinterval_Object = MibScalar
wlan0Beaconinterval = _Wlan0Beaconinterval_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 2),
    _Wlan0Beaconinterval_Type()
)
wlan0Beaconinterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0Beaconinterval.setStatus("current")
_Wlan0Cellid_Type = OctetString
_Wlan0Cellid_Object = MibScalar
wlan0Cellid = _Wlan0Cellid_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 3),
    _Wlan0Cellid_Type()
)
wlan0Cellid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan0Cellid.setStatus("current")
_Wlan0Dhcp_ObjectIdentity = ObjectIdentity
wlan0Dhcp = _Wlan0Dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 11, 4)
)
_Wlan0DhcpAlwaysbroadcast_Type = OctetString
_Wlan0DhcpAlwaysbroadcast_Object = MibScalar
wlan0DhcpAlwaysbroadcast = _Wlan0DhcpAlwaysbroadcast_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 4, 1),
    _Wlan0DhcpAlwaysbroadcast_Type()
)
wlan0DhcpAlwaysbroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0DhcpAlwaysbroadcast.setStatus("current")
_Wlan0DhcpDefaultleasetime_Type = Integer32
_Wlan0DhcpDefaultleasetime_Object = MibScalar
wlan0DhcpDefaultleasetime = _Wlan0DhcpDefaultleasetime_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 4, 2),
    _Wlan0DhcpDefaultleasetime_Type()
)
wlan0DhcpDefaultleasetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0DhcpDefaultleasetime.setStatus("current")
_Wlan0DhcpMaxleasetime_Type = Integer32
_Wlan0DhcpMaxleasetime_Object = MibScalar
wlan0DhcpMaxleasetime = _Wlan0DhcpMaxleasetime_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 4, 3),
    _Wlan0DhcpMaxleasetime_Type()
)
wlan0DhcpMaxleasetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0DhcpMaxleasetime.setStatus("current")
_Wlan0DhcpRelay_ObjectIdentity = ObjectIdentity
wlan0DhcpRelay = _Wlan0DhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 11, 4, 4)
)
_Wlan0DhcpRelayEnable_Type = OctetString
_Wlan0DhcpRelayEnable_Object = MibScalar
wlan0DhcpRelayEnable = _Wlan0DhcpRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 4, 4, 1),
    _Wlan0DhcpRelayEnable_Type()
)
wlan0DhcpRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0DhcpRelayEnable.setStatus("current")
_Wlan0DhcpReserve_Type = Integer32
_Wlan0DhcpReserve_Object = MibScalar
wlan0DhcpReserve = _Wlan0DhcpReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 4, 5),
    _Wlan0DhcpReserve_Type()
)
wlan0DhcpReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0DhcpReserve.setStatus("current")
_Wlan0DhcpRole_Type = OctetString
_Wlan0DhcpRole_Object = MibScalar
wlan0DhcpRole = _Wlan0DhcpRole_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 4, 6),
    _Wlan0DhcpRole_Type()
)
wlan0DhcpRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0DhcpRole.setStatus("current")
_Wlan0Enable_Type = OctetString
_Wlan0Enable_Object = MibScalar
wlan0Enable = _Wlan0Enable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 5),
    _Wlan0Enable_Type()
)
wlan0Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0Enable.setStatus("current")
_Wlan0Enhsec_Type = OctetString
_Wlan0Enhsec_Object = MibScalar
wlan0Enhsec = _Wlan0Enhsec_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 6),
    _Wlan0Enhsec_Type()
)
wlan0Enhsec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0Enhsec.setStatus("current")
_Wlan0Essid_Type = OctetString
_Wlan0Essid_Object = MibScalar
wlan0Essid = _Wlan0Essid_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 7),
    _Wlan0Essid_Type()
)
wlan0Essid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0Essid.setStatus("current")
_Wlan0Fabric_ObjectIdentity = ObjectIdentity
wlan0Fabric = _Wlan0Fabric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 11, 8)
)
_Wlan0FabricArgs_Type = OctetString
_Wlan0FabricArgs_Object = MibScalar
wlan0FabricArgs = _Wlan0FabricArgs_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 8, 1),
    _Wlan0FabricArgs_Type()
)
wlan0FabricArgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0FabricArgs.setStatus("current")
_Wlan0FabricBridge_Type = OctetString
_Wlan0FabricBridge_Object = MibScalar
wlan0FabricBridge = _Wlan0FabricBridge_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 8, 2),
    _Wlan0FabricBridge_Type()
)
wlan0FabricBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0FabricBridge.setStatus("current")
_Wlan0FabricCmd1_Type = OctetString
_Wlan0FabricCmd1_Object = MibScalar
wlan0FabricCmd1 = _Wlan0FabricCmd1_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 8, 3),
    _Wlan0FabricCmd1_Type()
)
wlan0FabricCmd1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0FabricCmd1.setStatus("current")
_Wlan0FabricCmd2_Type = OctetString
_Wlan0FabricCmd2_Object = MibScalar
wlan0FabricCmd2 = _Wlan0FabricCmd2_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 8, 4),
    _Wlan0FabricCmd2_Type()
)
wlan0FabricCmd2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0FabricCmd2.setStatus("current")
_Wlan0FabricEnable_Type = OctetString
_Wlan0FabricEnable_Object = MibScalar
wlan0FabricEnable = _Wlan0FabricEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 8, 5),
    _Wlan0FabricEnable_Type()
)
wlan0FabricEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0FabricEnable.setStatus("current")
_Wlan0FabricGateway_ObjectIdentity = ObjectIdentity
wlan0FabricGateway = _Wlan0FabricGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 11, 8, 6)
)
_Wlan0FabricGatewayEnable_Type = OctetString
_Wlan0FabricGatewayEnable_Object = MibScalar
wlan0FabricGatewayEnable = _Wlan0FabricGatewayEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 8, 6, 1),
    _Wlan0FabricGatewayEnable_Type()
)
wlan0FabricGatewayEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan0FabricGatewayEnable.setStatus("current")
_Wlan0FabricGatewayIf_Type = OctetString
_Wlan0FabricGatewayIf_Object = MibScalar
wlan0FabricGatewayIf = _Wlan0FabricGatewayIf_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 8, 6, 2),
    _Wlan0FabricGatewayIf_Type()
)
wlan0FabricGatewayIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan0FabricGatewayIf.setStatus("current")
_Wlan0FabricMargin_Type = Integer32
_Wlan0FabricMargin_Object = MibScalar
wlan0FabricMargin = _Wlan0FabricMargin_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 8, 7),
    _Wlan0FabricMargin_Type()
)
wlan0FabricMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0FabricMargin.setStatus("current")
_Wlan0FabricRouteadvert_Type = OctetString
_Wlan0FabricRouteadvert_Object = MibScalar
wlan0FabricRouteadvert = _Wlan0FabricRouteadvert_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 8, 8),
    _Wlan0FabricRouteadvert_Type()
)
wlan0FabricRouteadvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0FabricRouteadvert.setStatus("current")
_Wlan0FabricRssi_ObjectIdentity = ObjectIdentity
wlan0FabricRssi = _Wlan0FabricRssi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 11, 8, 9)
)
_Wlan0FabricRssiJoin_Type = Integer32
_Wlan0FabricRssiJoin_Object = MibScalar
wlan0FabricRssiJoin = _Wlan0FabricRssiJoin_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 8, 9, 1),
    _Wlan0FabricRssiJoin_Type()
)
wlan0FabricRssiJoin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0FabricRssiJoin.setStatus("current")
_Wlan0FabricRssiMargin_Type = Integer32
_Wlan0FabricRssiMargin_Object = MibScalar
wlan0FabricRssiMargin = _Wlan0FabricRssiMargin_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 8, 9, 2),
    _Wlan0FabricRssiMargin_Type()
)
wlan0FabricRssiMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0FabricRssiMargin.setStatus("current")
_Wlan0Frag_Type = OctetString
_Wlan0Frag_Object = MibScalar
wlan0Frag = _Wlan0Frag_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 9),
    _Wlan0Frag_Type()
)
wlan0Frag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0Frag.setStatus("current")
_Wlan0Hideessid_Type = OctetString
_Wlan0Hideessid_Object = MibScalar
wlan0Hideessid = _Wlan0Hideessid_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 10),
    _Wlan0Hideessid_Type()
)
wlan0Hideessid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0Hideessid.setStatus("current")
_Wlan0If_Type = OctetString
_Wlan0If_Object = MibScalar
wlan0If = _Wlan0If_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 11),
    _Wlan0If_Type()
)
wlan0If.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan0If.setStatus("current")
_Wlan0Ip_ObjectIdentity = ObjectIdentity
wlan0Ip = _Wlan0Ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 11, 12)
)
_Wlan0IpAddress_Type = OctetString
_Wlan0IpAddress_Object = MibScalar
wlan0IpAddress = _Wlan0IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 12, 1),
    _Wlan0IpAddress_Type()
)
wlan0IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan0IpAddress.setStatus("current")
_Wlan0IpAddressforce_Type = OctetString
_Wlan0IpAddressforce_Object = MibScalar
wlan0IpAddressforce = _Wlan0IpAddressforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 12, 2),
    _Wlan0IpAddressforce_Type()
)
wlan0IpAddressforce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan0IpAddressforce.setStatus("current")
_Wlan0IpBroadcast_Type = OctetString
_Wlan0IpBroadcast_Object = MibScalar
wlan0IpBroadcast = _Wlan0IpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 12, 3),
    _Wlan0IpBroadcast_Type()
)
wlan0IpBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan0IpBroadcast.setStatus("current")
_Wlan0IpBroadcastforce_Type = OctetString
_Wlan0IpBroadcastforce_Object = MibScalar
wlan0IpBroadcastforce = _Wlan0IpBroadcastforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 12, 4),
    _Wlan0IpBroadcastforce_Type()
)
wlan0IpBroadcastforce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan0IpBroadcastforce.setStatus("current")
_Wlan0IpGateway_Type = OctetString
_Wlan0IpGateway_Object = MibScalar
wlan0IpGateway = _Wlan0IpGateway_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 12, 5),
    _Wlan0IpGateway_Type()
)
wlan0IpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan0IpGateway.setStatus("current")
_Wlan0IpGatewayforce_Type = OctetString
_Wlan0IpGatewayforce_Object = MibScalar
wlan0IpGatewayforce = _Wlan0IpGatewayforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 12, 6),
    _Wlan0IpGatewayforce_Type()
)
wlan0IpGatewayforce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan0IpGatewayforce.setStatus("current")
_Wlan0IpNetmask_Type = OctetString
_Wlan0IpNetmask_Object = MibScalar
wlan0IpNetmask = _Wlan0IpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 12, 7),
    _Wlan0IpNetmask_Type()
)
wlan0IpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0IpNetmask.setStatus("current")
_Wlan0IpNetmaskforce_Type = OctetString
_Wlan0IpNetmaskforce_Object = MibScalar
wlan0IpNetmaskforce = _Wlan0IpNetmaskforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 12, 8),
    _Wlan0IpNetmaskforce_Type()
)
wlan0IpNetmaskforce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan0IpNetmaskforce.setStatus("current")
_Wlan0Iwconfig_ObjectIdentity = ObjectIdentity
wlan0Iwconfig = _Wlan0Iwconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 11, 13)
)
_Wlan0IwconfigCmd_Type = OctetString
_Wlan0IwconfigCmd_Object = MibScalar
wlan0IwconfigCmd = _Wlan0IwconfigCmd_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 13, 1),
    _Wlan0IwconfigCmd_Type()
)
wlan0IwconfigCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0IwconfigCmd.setStatus("current")
_Wlan0Iwpriv_ObjectIdentity = ObjectIdentity
wlan0Iwpriv = _Wlan0Iwpriv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 11, 14)
)
_Wlan0IwprivCmd_Type = OctetString
_Wlan0IwprivCmd_Object = MibScalar
wlan0IwprivCmd = _Wlan0IwprivCmd_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 14, 1),
    _Wlan0IwprivCmd_Type()
)
wlan0IwprivCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0IwprivCmd.setStatus("current")
_Wlan0Key_Type = OctetString
_Wlan0Key_Object = MibScalar
wlan0Key = _Wlan0Key_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 15),
    _Wlan0Key_Type()
)
wlan0Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0Key.setStatus("current")
_Wlan0Keys_ObjectIdentity = ObjectIdentity
wlan0Keys = _Wlan0Keys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 11, 16)
)
_Wlan0Keys1_Type = OctetString
_Wlan0Keys1_Object = MibScalar
wlan0Keys1 = _Wlan0Keys1_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 16, 1),
    _Wlan0Keys1_Type()
)
wlan0Keys1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0Keys1.setStatus("current")
_Wlan0Keys2_Type = OctetString
_Wlan0Keys2_Object = MibScalar
wlan0Keys2 = _Wlan0Keys2_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 16, 2),
    _Wlan0Keys2_Type()
)
wlan0Keys2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0Keys2.setStatus("current")
_Wlan0Keys3_Type = OctetString
_Wlan0Keys3_Object = MibScalar
wlan0Keys3 = _Wlan0Keys3_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 16, 3),
    _Wlan0Keys3_Type()
)
wlan0Keys3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0Keys3.setStatus("current")
_Wlan0Keys4_Type = OctetString
_Wlan0Keys4_Object = MibScalar
wlan0Keys4 = _Wlan0Keys4_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 16, 4),
    _Wlan0Keys4_Type()
)
wlan0Keys4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0Keys4.setStatus("current")
_Wlan0KeysDefault_Type = OctetString
_Wlan0KeysDefault_Object = MibScalar
wlan0KeysDefault = _Wlan0KeysDefault_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 16, 5),
    _Wlan0KeysDefault_Type()
)
wlan0KeysDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0KeysDefault.setStatus("current")
_Wlan0Mconfd_ObjectIdentity = ObjectIdentity
wlan0Mconfd = _Wlan0Mconfd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 11, 17)
)
_Wlan0MconfdEnable_Type = OctetString
_Wlan0MconfdEnable_Object = MibScalar
wlan0MconfdEnable = _Wlan0MconfdEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 17, 1),
    _Wlan0MconfdEnable_Type()
)
wlan0MconfdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0MconfdEnable.setStatus("current")
_Wlan0MconfdExternalhosts_Type = OctetString
_Wlan0MconfdExternalhosts_Object = MibScalar
wlan0MconfdExternalhosts = _Wlan0MconfdExternalhosts_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 17, 2),
    _Wlan0MconfdExternalhosts_Type()
)
wlan0MconfdExternalhosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan0MconfdExternalhosts.setStatus("current")
_Wlan0Mode_Type = OctetString
_Wlan0Mode_Object = MibScalar
wlan0Mode = _Wlan0Mode_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 18),
    _Wlan0Mode_Type()
)
wlan0Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0Mode.setStatus("current")
_Wlan0Mroute_ObjectIdentity = ObjectIdentity
wlan0Mroute = _Wlan0Mroute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 11, 19)
)
_Wlan0MrouteArgs_Type = OctetString
_Wlan0MrouteArgs_Object = MibScalar
wlan0MrouteArgs = _Wlan0MrouteArgs_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 19, 1),
    _Wlan0MrouteArgs_Type()
)
wlan0MrouteArgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0MrouteArgs.setStatus("current")
_Wlan0MrouteCmd_Type = OctetString
_Wlan0MrouteCmd_Object = MibScalar
wlan0MrouteCmd = _Wlan0MrouteCmd_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 19, 2),
    _Wlan0MrouteCmd_Type()
)
wlan0MrouteCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0MrouteCmd.setStatus("current")
_Wlan0MrouteEnable_Type = OctetString
_Wlan0MrouteEnable_Object = MibScalar
wlan0MrouteEnable = _Wlan0MrouteEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 19, 3),
    _Wlan0MrouteEnable_Type()
)
wlan0MrouteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0MrouteEnable.setStatus("current")
_Wlan0Mtu_Type = Integer32
_Wlan0Mtu_Object = MibScalar
wlan0Mtu = _Wlan0Mtu_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 20),
    _Wlan0Mtu_Type()
)
wlan0Mtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0Mtu.setStatus("current")
_Wlan0Radio_Type = OctetString
_Wlan0Radio_Object = MibScalar
wlan0Radio = _Wlan0Radio_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 21),
    _Wlan0Radio_Type()
)
wlan0Radio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0Radio.setStatus("current")
_Wlan0Rate_Type = OctetString
_Wlan0Rate_Object = MibScalar
wlan0Rate = _Wlan0Rate_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 22),
    _Wlan0Rate_Type()
)
wlan0Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0Rate.setStatus("current")
_Wlan0Role_Type = OctetString
_Wlan0Role_Object = MibScalar
wlan0Role = _Wlan0Role_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 23),
    _Wlan0Role_Type()
)
wlan0Role.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0Role.setStatus("current")
_Wlan0Routes_ObjectIdentity = ObjectIdentity
wlan0Routes = _Wlan0Routes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 11, 24)
)
_Wlan0RoutesAddprivnets_Type = OctetString
_Wlan0RoutesAddprivnets_Object = MibScalar
wlan0RoutesAddprivnets = _Wlan0RoutesAddprivnets_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 24, 1),
    _Wlan0RoutesAddprivnets_Type()
)
wlan0RoutesAddprivnets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0RoutesAddprivnets.setStatus("current")
_Wlan0RoutesStatic_Type = OctetString
_Wlan0RoutesStatic_Object = MibScalar
wlan0RoutesStatic = _Wlan0RoutesStatic_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 24, 2),
    _Wlan0RoutesStatic_Type()
)
wlan0RoutesStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0RoutesStatic.setStatus("current")
_Wlan0Topomc_ObjectIdentity = ObjectIdentity
wlan0Topomc = _Wlan0Topomc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 11, 25)
)
_Wlan0TopomcArgs_Type = OctetString
_Wlan0TopomcArgs_Object = MibScalar
wlan0TopomcArgs = _Wlan0TopomcArgs_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 25, 1),
    _Wlan0TopomcArgs_Type()
)
wlan0TopomcArgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0TopomcArgs.setStatus("current")
_Wlan0TopomcCmd_Type = OctetString
_Wlan0TopomcCmd_Object = MibScalar
wlan0TopomcCmd = _Wlan0TopomcCmd_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 25, 2),
    _Wlan0TopomcCmd_Type()
)
wlan0TopomcCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0TopomcCmd.setStatus("current")
_Wlan0TopomcEnable_Type = OctetString
_Wlan0TopomcEnable_Object = MibScalar
wlan0TopomcEnable = _Wlan0TopomcEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 11, 25, 3),
    _Wlan0TopomcEnable_Type()
)
wlan0TopomcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan0TopomcEnable.setStatus("current")
_Wlan1_ObjectIdentity = ObjectIdentity
wlan1 = _Wlan1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 12)
)
_Wlan1Acl_ObjectIdentity = ObjectIdentity
wlan1Acl = _Wlan1Acl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 12, 1)
)
_Wlan1AclMode_Type = OctetString
_Wlan1AclMode_Object = MibScalar
wlan1AclMode = _Wlan1AclMode_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 1, 1),
    _Wlan1AclMode_Type()
)
wlan1AclMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1AclMode.setStatus("current")
_Wlan1Beaconinterval_Type = Integer32
_Wlan1Beaconinterval_Object = MibScalar
wlan1Beaconinterval = _Wlan1Beaconinterval_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 2),
    _Wlan1Beaconinterval_Type()
)
wlan1Beaconinterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1Beaconinterval.setStatus("current")
_Wlan1Cellid_Type = OctetString
_Wlan1Cellid_Object = MibScalar
wlan1Cellid = _Wlan1Cellid_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 3),
    _Wlan1Cellid_Type()
)
wlan1Cellid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1Cellid.setStatus("current")
_Wlan1Dhcp_ObjectIdentity = ObjectIdentity
wlan1Dhcp = _Wlan1Dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 12, 4)
)
_Wlan1DhcpAlwaysbroadcast_Type = OctetString
_Wlan1DhcpAlwaysbroadcast_Object = MibScalar
wlan1DhcpAlwaysbroadcast = _Wlan1DhcpAlwaysbroadcast_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 4, 1),
    _Wlan1DhcpAlwaysbroadcast_Type()
)
wlan1DhcpAlwaysbroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1DhcpAlwaysbroadcast.setStatus("current")
_Wlan1DhcpDefaultleasetime_Type = Integer32
_Wlan1DhcpDefaultleasetime_Object = MibScalar
wlan1DhcpDefaultleasetime = _Wlan1DhcpDefaultleasetime_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 4, 2),
    _Wlan1DhcpDefaultleasetime_Type()
)
wlan1DhcpDefaultleasetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1DhcpDefaultleasetime.setStatus("current")
_Wlan1DhcpMaxleasetime_Type = Integer32
_Wlan1DhcpMaxleasetime_Object = MibScalar
wlan1DhcpMaxleasetime = _Wlan1DhcpMaxleasetime_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 4, 3),
    _Wlan1DhcpMaxleasetime_Type()
)
wlan1DhcpMaxleasetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1DhcpMaxleasetime.setStatus("current")
_Wlan1DhcpRelay_ObjectIdentity = ObjectIdentity
wlan1DhcpRelay = _Wlan1DhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 12, 4, 4)
)
_Wlan1DhcpRelayEnable_Type = OctetString
_Wlan1DhcpRelayEnable_Object = MibScalar
wlan1DhcpRelayEnable = _Wlan1DhcpRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 4, 4, 1),
    _Wlan1DhcpRelayEnable_Type()
)
wlan1DhcpRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1DhcpRelayEnable.setStatus("current")
_Wlan1DhcpReserve_Type = Integer32
_Wlan1DhcpReserve_Object = MibScalar
wlan1DhcpReserve = _Wlan1DhcpReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 4, 5),
    _Wlan1DhcpReserve_Type()
)
wlan1DhcpReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1DhcpReserve.setStatus("current")
_Wlan1DhcpRole_Type = OctetString
_Wlan1DhcpRole_Object = MibScalar
wlan1DhcpRole = _Wlan1DhcpRole_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 4, 6),
    _Wlan1DhcpRole_Type()
)
wlan1DhcpRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1DhcpRole.setStatus("current")
_Wlan1Enable_Type = OctetString
_Wlan1Enable_Object = MibScalar
wlan1Enable = _Wlan1Enable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 5),
    _Wlan1Enable_Type()
)
wlan1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1Enable.setStatus("current")
_Wlan1Enhsec_Type = OctetString
_Wlan1Enhsec_Object = MibScalar
wlan1Enhsec = _Wlan1Enhsec_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 6),
    _Wlan1Enhsec_Type()
)
wlan1Enhsec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1Enhsec.setStatus("current")
_Wlan1Essid_Type = OctetString
_Wlan1Essid_Object = MibScalar
wlan1Essid = _Wlan1Essid_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 7),
    _Wlan1Essid_Type()
)
wlan1Essid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1Essid.setStatus("current")
_Wlan1Frag_Type = OctetString
_Wlan1Frag_Object = MibScalar
wlan1Frag = _Wlan1Frag_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 8),
    _Wlan1Frag_Type()
)
wlan1Frag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1Frag.setStatus("current")
_Wlan1Hideessid_Type = OctetString
_Wlan1Hideessid_Object = MibScalar
wlan1Hideessid = _Wlan1Hideessid_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 9),
    _Wlan1Hideessid_Type()
)
wlan1Hideessid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1Hideessid.setStatus("current")
_Wlan1If_Type = OctetString
_Wlan1If_Object = MibScalar
wlan1If = _Wlan1If_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 10),
    _Wlan1If_Type()
)
wlan1If.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan1If.setStatus("current")
_Wlan1Ip_ObjectIdentity = ObjectIdentity
wlan1Ip = _Wlan1Ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 12, 11)
)
_Wlan1IpAddress_Type = OctetString
_Wlan1IpAddress_Object = MibScalar
wlan1IpAddress = _Wlan1IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 11, 1),
    _Wlan1IpAddress_Type()
)
wlan1IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan1IpAddress.setStatus("current")
_Wlan1IpAddressforce_Type = OctetString
_Wlan1IpAddressforce_Object = MibScalar
wlan1IpAddressforce = _Wlan1IpAddressforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 11, 2),
    _Wlan1IpAddressforce_Type()
)
wlan1IpAddressforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1IpAddressforce.setStatus("current")
_Wlan1IpBroadcast_Type = OctetString
_Wlan1IpBroadcast_Object = MibScalar
wlan1IpBroadcast = _Wlan1IpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 11, 3),
    _Wlan1IpBroadcast_Type()
)
wlan1IpBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan1IpBroadcast.setStatus("current")
_Wlan1IpBroadcastforce_Type = OctetString
_Wlan1IpBroadcastforce_Object = MibScalar
wlan1IpBroadcastforce = _Wlan1IpBroadcastforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 11, 4),
    _Wlan1IpBroadcastforce_Type()
)
wlan1IpBroadcastforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1IpBroadcastforce.setStatus("current")
_Wlan1IpGateway_Type = OctetString
_Wlan1IpGateway_Object = MibScalar
wlan1IpGateway = _Wlan1IpGateway_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 11, 5),
    _Wlan1IpGateway_Type()
)
wlan1IpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan1IpGateway.setStatus("current")
_Wlan1IpGatewayforce_Type = OctetString
_Wlan1IpGatewayforce_Object = MibScalar
wlan1IpGatewayforce = _Wlan1IpGatewayforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 11, 6),
    _Wlan1IpGatewayforce_Type()
)
wlan1IpGatewayforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1IpGatewayforce.setStatus("current")
_Wlan1IpImplicit_ObjectIdentity = ObjectIdentity
wlan1IpImplicit = _Wlan1IpImplicit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 12, 11, 7)
)
_Wlan1IpImplicitSize_ObjectIdentity = ObjectIdentity
wlan1IpImplicitSize = _Wlan1IpImplicitSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 12, 11, 7, 1)
)
_Wlan1IpImplicitSizeActual_Type = Integer32
_Wlan1IpImplicitSizeActual_Object = MibScalar
wlan1IpImplicitSizeActual = _Wlan1IpImplicitSizeActual_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 11, 7, 1, 1),
    _Wlan1IpImplicitSizeActual_Type()
)
wlan1IpImplicitSizeActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan1IpImplicitSizeActual.setStatus("current")
_Wlan1IpImplicitSizeRequested_Type = OctetString
_Wlan1IpImplicitSizeRequested_Object = MibScalar
wlan1IpImplicitSizeRequested = _Wlan1IpImplicitSizeRequested_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 11, 7, 1, 2),
    _Wlan1IpImplicitSizeRequested_Type()
)
wlan1IpImplicitSizeRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1IpImplicitSizeRequested.setStatus("current")
_Wlan1IpImplicitStart_ObjectIdentity = ObjectIdentity
wlan1IpImplicitStart = _Wlan1IpImplicitStart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 12, 11, 7, 2)
)
_Wlan1IpImplicitStartActual_Type = Integer32
_Wlan1IpImplicitStartActual_Object = MibScalar
wlan1IpImplicitStartActual = _Wlan1IpImplicitStartActual_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 11, 7, 2, 1),
    _Wlan1IpImplicitStartActual_Type()
)
wlan1IpImplicitStartActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan1IpImplicitStartActual.setStatus("current")
_Wlan1IpImplicitStartRequested_Type = OctetString
_Wlan1IpImplicitStartRequested_Object = MibScalar
wlan1IpImplicitStartRequested = _Wlan1IpImplicitStartRequested_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 11, 7, 2, 2),
    _Wlan1IpImplicitStartRequested_Type()
)
wlan1IpImplicitStartRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1IpImplicitStartRequested.setStatus("current")
_Wlan1IpNetmask_Type = OctetString
_Wlan1IpNetmask_Object = MibScalar
wlan1IpNetmask = _Wlan1IpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 11, 8),
    _Wlan1IpNetmask_Type()
)
wlan1IpNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan1IpNetmask.setStatus("current")
_Wlan1IpNetmaskforce_Type = OctetString
_Wlan1IpNetmaskforce_Object = MibScalar
wlan1IpNetmaskforce = _Wlan1IpNetmaskforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 11, 9),
    _Wlan1IpNetmaskforce_Type()
)
wlan1IpNetmaskforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1IpNetmaskforce.setStatus("current")
_Wlan1Iwconfig_ObjectIdentity = ObjectIdentity
wlan1Iwconfig = _Wlan1Iwconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 12, 12)
)
_Wlan1IwconfigCmd_Type = OctetString
_Wlan1IwconfigCmd_Object = MibScalar
wlan1IwconfigCmd = _Wlan1IwconfigCmd_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 12, 1),
    _Wlan1IwconfigCmd_Type()
)
wlan1IwconfigCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1IwconfigCmd.setStatus("current")
_Wlan1Iwpriv_ObjectIdentity = ObjectIdentity
wlan1Iwpriv = _Wlan1Iwpriv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 12, 13)
)
_Wlan1IwprivCmd_Type = OctetString
_Wlan1IwprivCmd_Object = MibScalar
wlan1IwprivCmd = _Wlan1IwprivCmd_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 13, 1),
    _Wlan1IwprivCmd_Type()
)
wlan1IwprivCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1IwprivCmd.setStatus("current")
_Wlan1Key_Type = OctetString
_Wlan1Key_Object = MibScalar
wlan1Key = _Wlan1Key_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 14),
    _Wlan1Key_Type()
)
wlan1Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1Key.setStatus("current")
_Wlan1Keys_ObjectIdentity = ObjectIdentity
wlan1Keys = _Wlan1Keys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 12, 15)
)
_Wlan1Keys1_Type = OctetString
_Wlan1Keys1_Object = MibScalar
wlan1Keys1 = _Wlan1Keys1_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 15, 1),
    _Wlan1Keys1_Type()
)
wlan1Keys1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1Keys1.setStatus("current")
_Wlan1Keys2_Type = OctetString
_Wlan1Keys2_Object = MibScalar
wlan1Keys2 = _Wlan1Keys2_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 15, 2),
    _Wlan1Keys2_Type()
)
wlan1Keys2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1Keys2.setStatus("current")
_Wlan1Keys3_Type = OctetString
_Wlan1Keys3_Object = MibScalar
wlan1Keys3 = _Wlan1Keys3_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 15, 3),
    _Wlan1Keys3_Type()
)
wlan1Keys3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1Keys3.setStatus("current")
_Wlan1Keys4_Type = OctetString
_Wlan1Keys4_Object = MibScalar
wlan1Keys4 = _Wlan1Keys4_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 15, 4),
    _Wlan1Keys4_Type()
)
wlan1Keys4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1Keys4.setStatus("current")
_Wlan1KeysDefault_Type = OctetString
_Wlan1KeysDefault_Object = MibScalar
wlan1KeysDefault = _Wlan1KeysDefault_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 15, 5),
    _Wlan1KeysDefault_Type()
)
wlan1KeysDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1KeysDefault.setStatus("current")
_Wlan1Mode_Type = OctetString
_Wlan1Mode_Object = MibScalar
wlan1Mode = _Wlan1Mode_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 16),
    _Wlan1Mode_Type()
)
wlan1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1Mode.setStatus("current")
_Wlan1Mtu_Type = Integer32
_Wlan1Mtu_Object = MibScalar
wlan1Mtu = _Wlan1Mtu_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 17),
    _Wlan1Mtu_Type()
)
wlan1Mtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1Mtu.setStatus("current")
_Wlan1Radio_Type = OctetString
_Wlan1Radio_Object = MibScalar
wlan1Radio = _Wlan1Radio_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 18),
    _Wlan1Radio_Type()
)
wlan1Radio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1Radio.setStatus("current")
_Wlan1Rate_Type = OctetString
_Wlan1Rate_Object = MibScalar
wlan1Rate = _Wlan1Rate_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 19),
    _Wlan1Rate_Type()
)
wlan1Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1Rate.setStatus("current")
_Wlan1Role_Type = OctetString
_Wlan1Role_Object = MibScalar
wlan1Role = _Wlan1Role_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 20),
    _Wlan1Role_Type()
)
wlan1Role.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1Role.setStatus("current")
_Wlan1Routes_ObjectIdentity = ObjectIdentity
wlan1Routes = _Wlan1Routes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 12, 21)
)
_Wlan1RoutesStatic_Type = OctetString
_Wlan1RoutesStatic_Object = MibScalar
wlan1RoutesStatic = _Wlan1RoutesStatic_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 21, 1),
    _Wlan1RoutesStatic_Type()
)
wlan1RoutesStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1RoutesStatic.setStatus("current")
_Wlan1Vlan_ObjectIdentity = ObjectIdentity
wlan1Vlan = _Wlan1Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 12, 22)
)
_Wlan1VlanEnable_Type = OctetString
_Wlan1VlanEnable_Object = MibScalar
wlan1VlanEnable = _Wlan1VlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 22, 1),
    _Wlan1VlanEnable_Type()
)
wlan1VlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1VlanEnable.setStatus("current")
_Wlan1VlanId_Type = Integer32
_Wlan1VlanId_Object = MibScalar
wlan1VlanId = _Wlan1VlanId_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 22, 2),
    _Wlan1VlanId_Type()
)
wlan1VlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1VlanId.setStatus("current")
_Wlan1Wpa_ObjectIdentity = ObjectIdentity
wlan1Wpa = _Wlan1Wpa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23)
)
_Wlan1WpaAuth_ObjectIdentity = ObjectIdentity
wlan1WpaAuth = _Wlan1WpaAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 1)
)
_Wlan1WpaAuthArgs_Type = OctetString
_Wlan1WpaAuthArgs_Object = MibScalar
wlan1WpaAuthArgs = _Wlan1WpaAuthArgs_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 1, 1),
    _Wlan1WpaAuthArgs_Type()
)
wlan1WpaAuthArgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1WpaAuthArgs.setStatus("current")
_Wlan1WpaAuthCustom_Type = OctetString
_Wlan1WpaAuthCustom_Object = MibScalar
wlan1WpaAuthCustom = _Wlan1WpaAuthCustom_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 1, 2),
    _Wlan1WpaAuthCustom_Type()
)
wlan1WpaAuthCustom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1WpaAuthCustom.setStatus("current")
_Wlan1WpaAuthInternal_Type = OctetString
_Wlan1WpaAuthInternal_Object = MibScalar
wlan1WpaAuthInternal = _Wlan1WpaAuthInternal_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 1, 3),
    _Wlan1WpaAuthInternal_Type()
)
wlan1WpaAuthInternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1WpaAuthInternal.setStatus("current")
_Wlan1WpaAuthServer_ObjectIdentity = ObjectIdentity
wlan1WpaAuthServer = _Wlan1WpaAuthServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 1, 4)
)
_Wlan1WpaAuthServerAddr_Type = OctetString
_Wlan1WpaAuthServerAddr_Object = MibScalar
wlan1WpaAuthServerAddr = _Wlan1WpaAuthServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 1, 4, 1),
    _Wlan1WpaAuthServerAddr_Type()
)
wlan1WpaAuthServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1WpaAuthServerAddr.setStatus("current")
_Wlan1WpaAuthServerPort_Type = Integer32
_Wlan1WpaAuthServerPort_Object = MibScalar
wlan1WpaAuthServerPort = _Wlan1WpaAuthServerPort_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 1, 4, 2),
    _Wlan1WpaAuthServerPort_Type()
)
wlan1WpaAuthServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1WpaAuthServerPort.setStatus("current")
_Wlan1WpaAuthServerSharedsecret_Type = OctetString
_Wlan1WpaAuthServerSharedsecret_Object = MibScalar
wlan1WpaAuthServerSharedsecret = _Wlan1WpaAuthServerSharedsecret_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 1, 4, 3),
    _Wlan1WpaAuthServerSharedsecret_Type()
)
wlan1WpaAuthServerSharedsecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1WpaAuthServerSharedsecret.setStatus("current")
_Wlan1WpaAuthType_Type = OctetString
_Wlan1WpaAuthType_Object = MibScalar
wlan1WpaAuthType = _Wlan1WpaAuthType_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 1, 5),
    _Wlan1WpaAuthType_Type()
)
wlan1WpaAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1WpaAuthType.setStatus("current")
_Wlan1WpaBridge_Type = OctetString
_Wlan1WpaBridge_Object = MibScalar
wlan1WpaBridge = _Wlan1WpaBridge_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 2),
    _Wlan1WpaBridge_Type()
)
wlan1WpaBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan1WpaBridge.setStatus("current")
_Wlan1WpaCa_ObjectIdentity = ObjectIdentity
wlan1WpaCa = _Wlan1WpaCa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 3)
)
_Wlan1WpaCaCert_ObjectIdentity = ObjectIdentity
wlan1WpaCaCert = _Wlan1WpaCaCert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 3, 1)
)
_Wlan1WpaCaCertFile_Type = OctetString
_Wlan1WpaCaCertFile_Object = MibScalar
wlan1WpaCaCertFile = _Wlan1WpaCaCertFile_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 3, 1, 1),
    _Wlan1WpaCaCertFile_Type()
)
wlan1WpaCaCertFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1WpaCaCertFile.setStatus("current")
_Wlan1WpaEapol_ObjectIdentity = ObjectIdentity
wlan1WpaEapol = _Wlan1WpaEapol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 4)
)
_Wlan1WpaEapolVersion_Type = OctetString
_Wlan1WpaEapolVersion_Object = MibScalar
wlan1WpaEapolVersion = _Wlan1WpaEapolVersion_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 4, 1),
    _Wlan1WpaEapolVersion_Type()
)
wlan1WpaEapolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1WpaEapolVersion.setStatus("current")
_Wlan1WpaEnable_Type = OctetString
_Wlan1WpaEnable_Object = MibScalar
wlan1WpaEnable = _Wlan1WpaEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 5),
    _Wlan1WpaEnable_Type()
)
wlan1WpaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1WpaEnable.setStatus("current")
_Wlan1WpaEssid_Type = OctetString
_Wlan1WpaEssid_Object = MibScalar
wlan1WpaEssid = _Wlan1WpaEssid_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 6),
    _Wlan1WpaEssid_Type()
)
wlan1WpaEssid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1WpaEssid.setStatus("current")
_Wlan1WpaIf_Type = OctetString
_Wlan1WpaIf_Object = MibScalar
wlan1WpaIf = _Wlan1WpaIf_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 7),
    _Wlan1WpaIf_Type()
)
wlan1WpaIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan1WpaIf.setStatus("current")
_Wlan1WpaKeymgmt_Type = OctetString
_Wlan1WpaKeymgmt_Object = MibScalar
wlan1WpaKeymgmt = _Wlan1WpaKeymgmt_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 8),
    _Wlan1WpaKeymgmt_Type()
)
wlan1WpaKeymgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1WpaKeymgmt.setStatus("current")
_Wlan1WpaMode_Type = Integer32
_Wlan1WpaMode_Object = MibScalar
wlan1WpaMode = _Wlan1WpaMode_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 9),
    _Wlan1WpaMode_Type()
)
wlan1WpaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1WpaMode.setStatus("current")
_Wlan1WpaNode_ObjectIdentity = ObjectIdentity
wlan1WpaNode = _Wlan1WpaNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 10)
)
_Wlan1WpaNodeCert_ObjectIdentity = ObjectIdentity
wlan1WpaNodeCert = _Wlan1WpaNodeCert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 10, 1)
)
_Wlan1WpaNodeCertFile_Type = OctetString
_Wlan1WpaNodeCertFile_Object = MibScalar
wlan1WpaNodeCertFile = _Wlan1WpaNodeCertFile_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 10, 1, 1),
    _Wlan1WpaNodeCertFile_Type()
)
wlan1WpaNodeCertFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1WpaNodeCertFile.setStatus("current")
_Wlan1WpaNodeKey_ObjectIdentity = ObjectIdentity
wlan1WpaNodeKey = _Wlan1WpaNodeKey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 10, 2)
)
_Wlan1WpaNodeKeyFile_Type = OctetString
_Wlan1WpaNodeKeyFile_Object = MibScalar
wlan1WpaNodeKeyFile = _Wlan1WpaNodeKeyFile_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 10, 2, 1),
    _Wlan1WpaNodeKeyFile_Type()
)
wlan1WpaNodeKeyFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1WpaNodeKeyFile.setStatus("current")
_Wlan1WpaNodeKeyPassphrase_Type = OctetString
_Wlan1WpaNodeKeyPassphrase_Object = MibScalar
wlan1WpaNodeKeyPassphrase = _Wlan1WpaNodeKeyPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 10, 2, 2),
    _Wlan1WpaNodeKeyPassphrase_Type()
)
wlan1WpaNodeKeyPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1WpaNodeKeyPassphrase.setStatus("current")
_Wlan1WpaPairwise_Type = OctetString
_Wlan1WpaPairwise_Object = MibScalar
wlan1WpaPairwise = _Wlan1WpaPairwise_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 11),
    _Wlan1WpaPairwise_Type()
)
wlan1WpaPairwise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1WpaPairwise.setStatus("current")
_Wlan1WpaPassphrase_Type = OctetString
_Wlan1WpaPassphrase_Object = MibScalar
wlan1WpaPassphrase = _Wlan1WpaPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 24350, 12, 23, 12),
    _Wlan1WpaPassphrase_Type()
)
wlan1WpaPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan1WpaPassphrase.setStatus("current")
_Wlan2_ObjectIdentity = ObjectIdentity
wlan2 = _Wlan2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 13)
)
_Wlan2Acl_ObjectIdentity = ObjectIdentity
wlan2Acl = _Wlan2Acl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 13, 1)
)
_Wlan2AclMode_Type = OctetString
_Wlan2AclMode_Object = MibScalar
wlan2AclMode = _Wlan2AclMode_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 1, 1),
    _Wlan2AclMode_Type()
)
wlan2AclMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2AclMode.setStatus("current")
_Wlan2Beaconinterval_Type = Integer32
_Wlan2Beaconinterval_Object = MibScalar
wlan2Beaconinterval = _Wlan2Beaconinterval_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 2),
    _Wlan2Beaconinterval_Type()
)
wlan2Beaconinterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2Beaconinterval.setStatus("current")
_Wlan2Cellid_Type = OctetString
_Wlan2Cellid_Object = MibScalar
wlan2Cellid = _Wlan2Cellid_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 3),
    _Wlan2Cellid_Type()
)
wlan2Cellid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2Cellid.setStatus("current")
_Wlan2Dhcp_ObjectIdentity = ObjectIdentity
wlan2Dhcp = _Wlan2Dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 13, 4)
)
_Wlan2DhcpAlwaysbroadcast_Type = OctetString
_Wlan2DhcpAlwaysbroadcast_Object = MibScalar
wlan2DhcpAlwaysbroadcast = _Wlan2DhcpAlwaysbroadcast_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 4, 1),
    _Wlan2DhcpAlwaysbroadcast_Type()
)
wlan2DhcpAlwaysbroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2DhcpAlwaysbroadcast.setStatus("current")
_Wlan2DhcpDefaultleasetime_Type = Integer32
_Wlan2DhcpDefaultleasetime_Object = MibScalar
wlan2DhcpDefaultleasetime = _Wlan2DhcpDefaultleasetime_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 4, 2),
    _Wlan2DhcpDefaultleasetime_Type()
)
wlan2DhcpDefaultleasetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2DhcpDefaultleasetime.setStatus("current")
_Wlan2DhcpMaxleasetime_Type = Integer32
_Wlan2DhcpMaxleasetime_Object = MibScalar
wlan2DhcpMaxleasetime = _Wlan2DhcpMaxleasetime_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 4, 3),
    _Wlan2DhcpMaxleasetime_Type()
)
wlan2DhcpMaxleasetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2DhcpMaxleasetime.setStatus("current")
_Wlan2DhcpRelay_ObjectIdentity = ObjectIdentity
wlan2DhcpRelay = _Wlan2DhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 13, 4, 4)
)
_Wlan2DhcpRelayEnable_Type = OctetString
_Wlan2DhcpRelayEnable_Object = MibScalar
wlan2DhcpRelayEnable = _Wlan2DhcpRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 4, 4, 1),
    _Wlan2DhcpRelayEnable_Type()
)
wlan2DhcpRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2DhcpRelayEnable.setStatus("current")
_Wlan2DhcpReserve_Type = Integer32
_Wlan2DhcpReserve_Object = MibScalar
wlan2DhcpReserve = _Wlan2DhcpReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 4, 5),
    _Wlan2DhcpReserve_Type()
)
wlan2DhcpReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2DhcpReserve.setStatus("current")
_Wlan2DhcpRole_Type = OctetString
_Wlan2DhcpRole_Object = MibScalar
wlan2DhcpRole = _Wlan2DhcpRole_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 4, 6),
    _Wlan2DhcpRole_Type()
)
wlan2DhcpRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2DhcpRole.setStatus("current")
_Wlan2Enable_Type = OctetString
_Wlan2Enable_Object = MibScalar
wlan2Enable = _Wlan2Enable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 5),
    _Wlan2Enable_Type()
)
wlan2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2Enable.setStatus("current")
_Wlan2Enhsec_Type = OctetString
_Wlan2Enhsec_Object = MibScalar
wlan2Enhsec = _Wlan2Enhsec_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 6),
    _Wlan2Enhsec_Type()
)
wlan2Enhsec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2Enhsec.setStatus("current")
_Wlan2Essid_Type = OctetString
_Wlan2Essid_Object = MibScalar
wlan2Essid = _Wlan2Essid_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 7),
    _Wlan2Essid_Type()
)
wlan2Essid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2Essid.setStatus("current")
_Wlan2Frag_Type = OctetString
_Wlan2Frag_Object = MibScalar
wlan2Frag = _Wlan2Frag_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 8),
    _Wlan2Frag_Type()
)
wlan2Frag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2Frag.setStatus("current")
_Wlan2Hideessid_Type = OctetString
_Wlan2Hideessid_Object = MibScalar
wlan2Hideessid = _Wlan2Hideessid_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 9),
    _Wlan2Hideessid_Type()
)
wlan2Hideessid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2Hideessid.setStatus("current")
_Wlan2If_Type = OctetString
_Wlan2If_Object = MibScalar
wlan2If = _Wlan2If_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 10),
    _Wlan2If_Type()
)
wlan2If.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan2If.setStatus("current")
_Wlan2Ip_ObjectIdentity = ObjectIdentity
wlan2Ip = _Wlan2Ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 13, 11)
)
_Wlan2IpAddress_Type = OctetString
_Wlan2IpAddress_Object = MibScalar
wlan2IpAddress = _Wlan2IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 11, 1),
    _Wlan2IpAddress_Type()
)
wlan2IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan2IpAddress.setStatus("current")
_Wlan2IpAddressforce_Type = OctetString
_Wlan2IpAddressforce_Object = MibScalar
wlan2IpAddressforce = _Wlan2IpAddressforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 11, 2),
    _Wlan2IpAddressforce_Type()
)
wlan2IpAddressforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2IpAddressforce.setStatus("current")
_Wlan2IpBroadcast_Type = OctetString
_Wlan2IpBroadcast_Object = MibScalar
wlan2IpBroadcast = _Wlan2IpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 11, 3),
    _Wlan2IpBroadcast_Type()
)
wlan2IpBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan2IpBroadcast.setStatus("current")
_Wlan2IpBroadcastforce_Type = OctetString
_Wlan2IpBroadcastforce_Object = MibScalar
wlan2IpBroadcastforce = _Wlan2IpBroadcastforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 11, 4),
    _Wlan2IpBroadcastforce_Type()
)
wlan2IpBroadcastforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2IpBroadcastforce.setStatus("current")
_Wlan2IpGateway_Type = OctetString
_Wlan2IpGateway_Object = MibScalar
wlan2IpGateway = _Wlan2IpGateway_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 11, 5),
    _Wlan2IpGateway_Type()
)
wlan2IpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan2IpGateway.setStatus("current")
_Wlan2IpGatewayforce_Type = OctetString
_Wlan2IpGatewayforce_Object = MibScalar
wlan2IpGatewayforce = _Wlan2IpGatewayforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 11, 6),
    _Wlan2IpGatewayforce_Type()
)
wlan2IpGatewayforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2IpGatewayforce.setStatus("current")
_Wlan2IpImplicit_ObjectIdentity = ObjectIdentity
wlan2IpImplicit = _Wlan2IpImplicit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 13, 11, 7)
)
_Wlan2IpImplicitSize_ObjectIdentity = ObjectIdentity
wlan2IpImplicitSize = _Wlan2IpImplicitSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 13, 11, 7, 1)
)
_Wlan2IpImplicitSizeActual_Type = Integer32
_Wlan2IpImplicitSizeActual_Object = MibScalar
wlan2IpImplicitSizeActual = _Wlan2IpImplicitSizeActual_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 11, 7, 1, 1),
    _Wlan2IpImplicitSizeActual_Type()
)
wlan2IpImplicitSizeActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan2IpImplicitSizeActual.setStatus("current")
_Wlan2IpImplicitSizeRequested_Type = OctetString
_Wlan2IpImplicitSizeRequested_Object = MibScalar
wlan2IpImplicitSizeRequested = _Wlan2IpImplicitSizeRequested_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 11, 7, 1, 2),
    _Wlan2IpImplicitSizeRequested_Type()
)
wlan2IpImplicitSizeRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2IpImplicitSizeRequested.setStatus("current")
_Wlan2IpImplicitStart_ObjectIdentity = ObjectIdentity
wlan2IpImplicitStart = _Wlan2IpImplicitStart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 13, 11, 7, 2)
)
_Wlan2IpImplicitStartActual_Type = Integer32
_Wlan2IpImplicitStartActual_Object = MibScalar
wlan2IpImplicitStartActual = _Wlan2IpImplicitStartActual_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 11, 7, 2, 1),
    _Wlan2IpImplicitStartActual_Type()
)
wlan2IpImplicitStartActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan2IpImplicitStartActual.setStatus("current")
_Wlan2IpImplicitStartRequested_Type = OctetString
_Wlan2IpImplicitStartRequested_Object = MibScalar
wlan2IpImplicitStartRequested = _Wlan2IpImplicitStartRequested_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 11, 7, 2, 2),
    _Wlan2IpImplicitStartRequested_Type()
)
wlan2IpImplicitStartRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2IpImplicitStartRequested.setStatus("current")
_Wlan2IpNetmask_Type = OctetString
_Wlan2IpNetmask_Object = MibScalar
wlan2IpNetmask = _Wlan2IpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 11, 8),
    _Wlan2IpNetmask_Type()
)
wlan2IpNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan2IpNetmask.setStatus("current")
_Wlan2IpNetmaskforce_Type = OctetString
_Wlan2IpNetmaskforce_Object = MibScalar
wlan2IpNetmaskforce = _Wlan2IpNetmaskforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 11, 9),
    _Wlan2IpNetmaskforce_Type()
)
wlan2IpNetmaskforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2IpNetmaskforce.setStatus("current")
_Wlan2Iwconfig_ObjectIdentity = ObjectIdentity
wlan2Iwconfig = _Wlan2Iwconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 13, 12)
)
_Wlan2IwconfigCmd_Type = OctetString
_Wlan2IwconfigCmd_Object = MibScalar
wlan2IwconfigCmd = _Wlan2IwconfigCmd_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 12, 1),
    _Wlan2IwconfigCmd_Type()
)
wlan2IwconfigCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2IwconfigCmd.setStatus("current")
_Wlan2Iwpriv_ObjectIdentity = ObjectIdentity
wlan2Iwpriv = _Wlan2Iwpriv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 13, 13)
)
_Wlan2IwprivCmd_Type = OctetString
_Wlan2IwprivCmd_Object = MibScalar
wlan2IwprivCmd = _Wlan2IwprivCmd_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 13, 1),
    _Wlan2IwprivCmd_Type()
)
wlan2IwprivCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2IwprivCmd.setStatus("current")
_Wlan2Key_Type = OctetString
_Wlan2Key_Object = MibScalar
wlan2Key = _Wlan2Key_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 14),
    _Wlan2Key_Type()
)
wlan2Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2Key.setStatus("current")
_Wlan2Keys_ObjectIdentity = ObjectIdentity
wlan2Keys = _Wlan2Keys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 13, 15)
)
_Wlan2Keys1_Type = OctetString
_Wlan2Keys1_Object = MibScalar
wlan2Keys1 = _Wlan2Keys1_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 15, 1),
    _Wlan2Keys1_Type()
)
wlan2Keys1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2Keys1.setStatus("current")
_Wlan2Keys2_Type = OctetString
_Wlan2Keys2_Object = MibScalar
wlan2Keys2 = _Wlan2Keys2_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 15, 2),
    _Wlan2Keys2_Type()
)
wlan2Keys2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2Keys2.setStatus("current")
_Wlan2Keys3_Type = OctetString
_Wlan2Keys3_Object = MibScalar
wlan2Keys3 = _Wlan2Keys3_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 15, 3),
    _Wlan2Keys3_Type()
)
wlan2Keys3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2Keys3.setStatus("current")
_Wlan2Keys4_Type = OctetString
_Wlan2Keys4_Object = MibScalar
wlan2Keys4 = _Wlan2Keys4_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 15, 4),
    _Wlan2Keys4_Type()
)
wlan2Keys4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2Keys4.setStatus("current")
_Wlan2KeysDefault_Type = OctetString
_Wlan2KeysDefault_Object = MibScalar
wlan2KeysDefault = _Wlan2KeysDefault_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 15, 5),
    _Wlan2KeysDefault_Type()
)
wlan2KeysDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2KeysDefault.setStatus("current")
_Wlan2Mode_Type = OctetString
_Wlan2Mode_Object = MibScalar
wlan2Mode = _Wlan2Mode_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 16),
    _Wlan2Mode_Type()
)
wlan2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2Mode.setStatus("current")
_Wlan2Mtu_Type = Integer32
_Wlan2Mtu_Object = MibScalar
wlan2Mtu = _Wlan2Mtu_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 17),
    _Wlan2Mtu_Type()
)
wlan2Mtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2Mtu.setStatus("current")
_Wlan2Radio_Type = OctetString
_Wlan2Radio_Object = MibScalar
wlan2Radio = _Wlan2Radio_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 18),
    _Wlan2Radio_Type()
)
wlan2Radio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2Radio.setStatus("current")
_Wlan2Rate_Type = OctetString
_Wlan2Rate_Object = MibScalar
wlan2Rate = _Wlan2Rate_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 19),
    _Wlan2Rate_Type()
)
wlan2Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2Rate.setStatus("current")
_Wlan2Role_Type = OctetString
_Wlan2Role_Object = MibScalar
wlan2Role = _Wlan2Role_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 20),
    _Wlan2Role_Type()
)
wlan2Role.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2Role.setStatus("current")
_Wlan2Routes_ObjectIdentity = ObjectIdentity
wlan2Routes = _Wlan2Routes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 13, 21)
)
_Wlan2RoutesStatic_Type = OctetString
_Wlan2RoutesStatic_Object = MibScalar
wlan2RoutesStatic = _Wlan2RoutesStatic_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 21, 1),
    _Wlan2RoutesStatic_Type()
)
wlan2RoutesStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2RoutesStatic.setStatus("current")
_Wlan2Vlan_ObjectIdentity = ObjectIdentity
wlan2Vlan = _Wlan2Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 13, 22)
)
_Wlan2VlanEnable_Type = OctetString
_Wlan2VlanEnable_Object = MibScalar
wlan2VlanEnable = _Wlan2VlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 22, 1),
    _Wlan2VlanEnable_Type()
)
wlan2VlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2VlanEnable.setStatus("current")
_Wlan2VlanId_Type = Integer32
_Wlan2VlanId_Object = MibScalar
wlan2VlanId = _Wlan2VlanId_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 22, 2),
    _Wlan2VlanId_Type()
)
wlan2VlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2VlanId.setStatus("current")
_Wlan2Wpa_ObjectIdentity = ObjectIdentity
wlan2Wpa = _Wlan2Wpa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23)
)
_Wlan2WpaAuth_ObjectIdentity = ObjectIdentity
wlan2WpaAuth = _Wlan2WpaAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 1)
)
_Wlan2WpaAuthArgs_Type = OctetString
_Wlan2WpaAuthArgs_Object = MibScalar
wlan2WpaAuthArgs = _Wlan2WpaAuthArgs_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 1, 1),
    _Wlan2WpaAuthArgs_Type()
)
wlan2WpaAuthArgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2WpaAuthArgs.setStatus("current")
_Wlan2WpaAuthCustom_Type = OctetString
_Wlan2WpaAuthCustom_Object = MibScalar
wlan2WpaAuthCustom = _Wlan2WpaAuthCustom_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 1, 2),
    _Wlan2WpaAuthCustom_Type()
)
wlan2WpaAuthCustom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2WpaAuthCustom.setStatus("current")
_Wlan2WpaAuthInternal_Type = OctetString
_Wlan2WpaAuthInternal_Object = MibScalar
wlan2WpaAuthInternal = _Wlan2WpaAuthInternal_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 1, 3),
    _Wlan2WpaAuthInternal_Type()
)
wlan2WpaAuthInternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2WpaAuthInternal.setStatus("current")
_Wlan2WpaAuthServer_ObjectIdentity = ObjectIdentity
wlan2WpaAuthServer = _Wlan2WpaAuthServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 1, 4)
)
_Wlan2WpaAuthServerAddr_Type = OctetString
_Wlan2WpaAuthServerAddr_Object = MibScalar
wlan2WpaAuthServerAddr = _Wlan2WpaAuthServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 1, 4, 1),
    _Wlan2WpaAuthServerAddr_Type()
)
wlan2WpaAuthServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2WpaAuthServerAddr.setStatus("current")
_Wlan2WpaAuthServerPort_Type = Integer32
_Wlan2WpaAuthServerPort_Object = MibScalar
wlan2WpaAuthServerPort = _Wlan2WpaAuthServerPort_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 1, 4, 2),
    _Wlan2WpaAuthServerPort_Type()
)
wlan2WpaAuthServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2WpaAuthServerPort.setStatus("current")
_Wlan2WpaAuthServerSharedsecret_Type = OctetString
_Wlan2WpaAuthServerSharedsecret_Object = MibScalar
wlan2WpaAuthServerSharedsecret = _Wlan2WpaAuthServerSharedsecret_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 1, 4, 3),
    _Wlan2WpaAuthServerSharedsecret_Type()
)
wlan2WpaAuthServerSharedsecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2WpaAuthServerSharedsecret.setStatus("current")
_Wlan2WpaAuthType_Type = OctetString
_Wlan2WpaAuthType_Object = MibScalar
wlan2WpaAuthType = _Wlan2WpaAuthType_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 1, 5),
    _Wlan2WpaAuthType_Type()
)
wlan2WpaAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2WpaAuthType.setStatus("current")
_Wlan2WpaBridge_Type = OctetString
_Wlan2WpaBridge_Object = MibScalar
wlan2WpaBridge = _Wlan2WpaBridge_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 2),
    _Wlan2WpaBridge_Type()
)
wlan2WpaBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan2WpaBridge.setStatus("current")
_Wlan2WpaCa_ObjectIdentity = ObjectIdentity
wlan2WpaCa = _Wlan2WpaCa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 3)
)
_Wlan2WpaCaCert_ObjectIdentity = ObjectIdentity
wlan2WpaCaCert = _Wlan2WpaCaCert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 3, 1)
)
_Wlan2WpaCaCertFile_Type = OctetString
_Wlan2WpaCaCertFile_Object = MibScalar
wlan2WpaCaCertFile = _Wlan2WpaCaCertFile_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 3, 1, 1),
    _Wlan2WpaCaCertFile_Type()
)
wlan2WpaCaCertFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2WpaCaCertFile.setStatus("current")
_Wlan2WpaEapol_ObjectIdentity = ObjectIdentity
wlan2WpaEapol = _Wlan2WpaEapol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 4)
)
_Wlan2WpaEapolVersion_Type = OctetString
_Wlan2WpaEapolVersion_Object = MibScalar
wlan2WpaEapolVersion = _Wlan2WpaEapolVersion_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 4, 1),
    _Wlan2WpaEapolVersion_Type()
)
wlan2WpaEapolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2WpaEapolVersion.setStatus("current")
_Wlan2WpaEnable_Type = OctetString
_Wlan2WpaEnable_Object = MibScalar
wlan2WpaEnable = _Wlan2WpaEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 5),
    _Wlan2WpaEnable_Type()
)
wlan2WpaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2WpaEnable.setStatus("current")
_Wlan2WpaEssid_Type = OctetString
_Wlan2WpaEssid_Object = MibScalar
wlan2WpaEssid = _Wlan2WpaEssid_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 6),
    _Wlan2WpaEssid_Type()
)
wlan2WpaEssid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2WpaEssid.setStatus("current")
_Wlan2WpaIf_Type = OctetString
_Wlan2WpaIf_Object = MibScalar
wlan2WpaIf = _Wlan2WpaIf_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 7),
    _Wlan2WpaIf_Type()
)
wlan2WpaIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan2WpaIf.setStatus("current")
_Wlan2WpaKeymgmt_Type = OctetString
_Wlan2WpaKeymgmt_Object = MibScalar
wlan2WpaKeymgmt = _Wlan2WpaKeymgmt_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 8),
    _Wlan2WpaKeymgmt_Type()
)
wlan2WpaKeymgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2WpaKeymgmt.setStatus("current")
_Wlan2WpaMode_Type = Integer32
_Wlan2WpaMode_Object = MibScalar
wlan2WpaMode = _Wlan2WpaMode_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 9),
    _Wlan2WpaMode_Type()
)
wlan2WpaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2WpaMode.setStatus("current")
_Wlan2WpaNode_ObjectIdentity = ObjectIdentity
wlan2WpaNode = _Wlan2WpaNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 10)
)
_Wlan2WpaNodeCert_ObjectIdentity = ObjectIdentity
wlan2WpaNodeCert = _Wlan2WpaNodeCert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 10, 1)
)
_Wlan2WpaNodeCertFile_Type = OctetString
_Wlan2WpaNodeCertFile_Object = MibScalar
wlan2WpaNodeCertFile = _Wlan2WpaNodeCertFile_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 10, 1, 1),
    _Wlan2WpaNodeCertFile_Type()
)
wlan2WpaNodeCertFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2WpaNodeCertFile.setStatus("current")
_Wlan2WpaNodeKey_ObjectIdentity = ObjectIdentity
wlan2WpaNodeKey = _Wlan2WpaNodeKey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 10, 2)
)
_Wlan2WpaNodeKeyFile_Type = OctetString
_Wlan2WpaNodeKeyFile_Object = MibScalar
wlan2WpaNodeKeyFile = _Wlan2WpaNodeKeyFile_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 10, 2, 1),
    _Wlan2WpaNodeKeyFile_Type()
)
wlan2WpaNodeKeyFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2WpaNodeKeyFile.setStatus("current")
_Wlan2WpaNodeKeyPassphrase_Type = OctetString
_Wlan2WpaNodeKeyPassphrase_Object = MibScalar
wlan2WpaNodeKeyPassphrase = _Wlan2WpaNodeKeyPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 10, 2, 2),
    _Wlan2WpaNodeKeyPassphrase_Type()
)
wlan2WpaNodeKeyPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2WpaNodeKeyPassphrase.setStatus("current")
_Wlan2WpaPairwise_Type = OctetString
_Wlan2WpaPairwise_Object = MibScalar
wlan2WpaPairwise = _Wlan2WpaPairwise_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 11),
    _Wlan2WpaPairwise_Type()
)
wlan2WpaPairwise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2WpaPairwise.setStatus("current")
_Wlan2WpaPassphrase_Type = OctetString
_Wlan2WpaPassphrase_Object = MibScalar
wlan2WpaPassphrase = _Wlan2WpaPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 24350, 13, 23, 12),
    _Wlan2WpaPassphrase_Type()
)
wlan2WpaPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan2WpaPassphrase.setStatus("current")
_Wlan3_ObjectIdentity = ObjectIdentity
wlan3 = _Wlan3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 14)
)
_Wlan3Acl_ObjectIdentity = ObjectIdentity
wlan3Acl = _Wlan3Acl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 14, 1)
)
_Wlan3AclMode_Type = OctetString
_Wlan3AclMode_Object = MibScalar
wlan3AclMode = _Wlan3AclMode_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 1, 1),
    _Wlan3AclMode_Type()
)
wlan3AclMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3AclMode.setStatus("current")
_Wlan3Beaconinterval_Type = Integer32
_Wlan3Beaconinterval_Object = MibScalar
wlan3Beaconinterval = _Wlan3Beaconinterval_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 2),
    _Wlan3Beaconinterval_Type()
)
wlan3Beaconinterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3Beaconinterval.setStatus("current")
_Wlan3Cellid_Type = OctetString
_Wlan3Cellid_Object = MibScalar
wlan3Cellid = _Wlan3Cellid_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 3),
    _Wlan3Cellid_Type()
)
wlan3Cellid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3Cellid.setStatus("current")
_Wlan3Dhcp_ObjectIdentity = ObjectIdentity
wlan3Dhcp = _Wlan3Dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 14, 4)
)
_Wlan3DhcpAlwaysbroadcast_Type = OctetString
_Wlan3DhcpAlwaysbroadcast_Object = MibScalar
wlan3DhcpAlwaysbroadcast = _Wlan3DhcpAlwaysbroadcast_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 4, 1),
    _Wlan3DhcpAlwaysbroadcast_Type()
)
wlan3DhcpAlwaysbroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3DhcpAlwaysbroadcast.setStatus("current")
_Wlan3DhcpDefaultleasetime_Type = Integer32
_Wlan3DhcpDefaultleasetime_Object = MibScalar
wlan3DhcpDefaultleasetime = _Wlan3DhcpDefaultleasetime_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 4, 2),
    _Wlan3DhcpDefaultleasetime_Type()
)
wlan3DhcpDefaultleasetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3DhcpDefaultleasetime.setStatus("current")
_Wlan3DhcpMaxleasetime_Type = Integer32
_Wlan3DhcpMaxleasetime_Object = MibScalar
wlan3DhcpMaxleasetime = _Wlan3DhcpMaxleasetime_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 4, 3),
    _Wlan3DhcpMaxleasetime_Type()
)
wlan3DhcpMaxleasetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3DhcpMaxleasetime.setStatus("current")
_Wlan3DhcpRelay_ObjectIdentity = ObjectIdentity
wlan3DhcpRelay = _Wlan3DhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 14, 4, 4)
)
_Wlan3DhcpRelayEnable_Type = OctetString
_Wlan3DhcpRelayEnable_Object = MibScalar
wlan3DhcpRelayEnable = _Wlan3DhcpRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 4, 4, 1),
    _Wlan3DhcpRelayEnable_Type()
)
wlan3DhcpRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3DhcpRelayEnable.setStatus("current")
_Wlan3DhcpReserve_Type = Integer32
_Wlan3DhcpReserve_Object = MibScalar
wlan3DhcpReserve = _Wlan3DhcpReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 4, 5),
    _Wlan3DhcpReserve_Type()
)
wlan3DhcpReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3DhcpReserve.setStatus("current")
_Wlan3DhcpRole_Type = OctetString
_Wlan3DhcpRole_Object = MibScalar
wlan3DhcpRole = _Wlan3DhcpRole_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 4, 6),
    _Wlan3DhcpRole_Type()
)
wlan3DhcpRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3DhcpRole.setStatus("current")
_Wlan3Enable_Type = OctetString
_Wlan3Enable_Object = MibScalar
wlan3Enable = _Wlan3Enable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 5),
    _Wlan3Enable_Type()
)
wlan3Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3Enable.setStatus("current")
_Wlan3Enhsec_Type = OctetString
_Wlan3Enhsec_Object = MibScalar
wlan3Enhsec = _Wlan3Enhsec_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 6),
    _Wlan3Enhsec_Type()
)
wlan3Enhsec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3Enhsec.setStatus("current")
_Wlan3Essid_Type = OctetString
_Wlan3Essid_Object = MibScalar
wlan3Essid = _Wlan3Essid_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 7),
    _Wlan3Essid_Type()
)
wlan3Essid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3Essid.setStatus("current")
_Wlan3Frag_Type = OctetString
_Wlan3Frag_Object = MibScalar
wlan3Frag = _Wlan3Frag_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 8),
    _Wlan3Frag_Type()
)
wlan3Frag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3Frag.setStatus("current")
_Wlan3Hideessid_Type = OctetString
_Wlan3Hideessid_Object = MibScalar
wlan3Hideessid = _Wlan3Hideessid_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 9),
    _Wlan3Hideessid_Type()
)
wlan3Hideessid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3Hideessid.setStatus("current")
_Wlan3If_Type = OctetString
_Wlan3If_Object = MibScalar
wlan3If = _Wlan3If_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 10),
    _Wlan3If_Type()
)
wlan3If.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan3If.setStatus("current")
_Wlan3Ip_ObjectIdentity = ObjectIdentity
wlan3Ip = _Wlan3Ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 14, 11)
)
_Wlan3IpAddress_Type = OctetString
_Wlan3IpAddress_Object = MibScalar
wlan3IpAddress = _Wlan3IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 11, 1),
    _Wlan3IpAddress_Type()
)
wlan3IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan3IpAddress.setStatus("current")
_Wlan3IpAddressforce_Type = OctetString
_Wlan3IpAddressforce_Object = MibScalar
wlan3IpAddressforce = _Wlan3IpAddressforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 11, 2),
    _Wlan3IpAddressforce_Type()
)
wlan3IpAddressforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3IpAddressforce.setStatus("current")
_Wlan3IpBroadcast_Type = OctetString
_Wlan3IpBroadcast_Object = MibScalar
wlan3IpBroadcast = _Wlan3IpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 11, 3),
    _Wlan3IpBroadcast_Type()
)
wlan3IpBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan3IpBroadcast.setStatus("current")
_Wlan3IpBroadcastforce_Type = OctetString
_Wlan3IpBroadcastforce_Object = MibScalar
wlan3IpBroadcastforce = _Wlan3IpBroadcastforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 11, 4),
    _Wlan3IpBroadcastforce_Type()
)
wlan3IpBroadcastforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3IpBroadcastforce.setStatus("current")
_Wlan3IpGateway_Type = OctetString
_Wlan3IpGateway_Object = MibScalar
wlan3IpGateway = _Wlan3IpGateway_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 11, 5),
    _Wlan3IpGateway_Type()
)
wlan3IpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan3IpGateway.setStatus("current")
_Wlan3IpGatewayforce_Type = OctetString
_Wlan3IpGatewayforce_Object = MibScalar
wlan3IpGatewayforce = _Wlan3IpGatewayforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 11, 6),
    _Wlan3IpGatewayforce_Type()
)
wlan3IpGatewayforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3IpGatewayforce.setStatus("current")
_Wlan3IpImplicit_ObjectIdentity = ObjectIdentity
wlan3IpImplicit = _Wlan3IpImplicit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 14, 11, 7)
)
_Wlan3IpImplicitSize_ObjectIdentity = ObjectIdentity
wlan3IpImplicitSize = _Wlan3IpImplicitSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 14, 11, 7, 1)
)
_Wlan3IpImplicitSizeActual_Type = Integer32
_Wlan3IpImplicitSizeActual_Object = MibScalar
wlan3IpImplicitSizeActual = _Wlan3IpImplicitSizeActual_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 11, 7, 1, 1),
    _Wlan3IpImplicitSizeActual_Type()
)
wlan3IpImplicitSizeActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan3IpImplicitSizeActual.setStatus("current")
_Wlan3IpImplicitSizeRequested_Type = OctetString
_Wlan3IpImplicitSizeRequested_Object = MibScalar
wlan3IpImplicitSizeRequested = _Wlan3IpImplicitSizeRequested_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 11, 7, 1, 2),
    _Wlan3IpImplicitSizeRequested_Type()
)
wlan3IpImplicitSizeRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3IpImplicitSizeRequested.setStatus("current")
_Wlan3IpImplicitStart_ObjectIdentity = ObjectIdentity
wlan3IpImplicitStart = _Wlan3IpImplicitStart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 14, 11, 7, 2)
)
_Wlan3IpImplicitStartActual_Type = Integer32
_Wlan3IpImplicitStartActual_Object = MibScalar
wlan3IpImplicitStartActual = _Wlan3IpImplicitStartActual_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 11, 7, 2, 1),
    _Wlan3IpImplicitStartActual_Type()
)
wlan3IpImplicitStartActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan3IpImplicitStartActual.setStatus("current")
_Wlan3IpImplicitStartRequested_Type = OctetString
_Wlan3IpImplicitStartRequested_Object = MibScalar
wlan3IpImplicitStartRequested = _Wlan3IpImplicitStartRequested_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 11, 7, 2, 2),
    _Wlan3IpImplicitStartRequested_Type()
)
wlan3IpImplicitStartRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3IpImplicitStartRequested.setStatus("current")
_Wlan3IpNetmask_Type = OctetString
_Wlan3IpNetmask_Object = MibScalar
wlan3IpNetmask = _Wlan3IpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 11, 8),
    _Wlan3IpNetmask_Type()
)
wlan3IpNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan3IpNetmask.setStatus("current")
_Wlan3IpNetmaskforce_Type = OctetString
_Wlan3IpNetmaskforce_Object = MibScalar
wlan3IpNetmaskforce = _Wlan3IpNetmaskforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 11, 9),
    _Wlan3IpNetmaskforce_Type()
)
wlan3IpNetmaskforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3IpNetmaskforce.setStatus("current")
_Wlan3Iwconfig_ObjectIdentity = ObjectIdentity
wlan3Iwconfig = _Wlan3Iwconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 14, 12)
)
_Wlan3IwconfigCmd_Type = OctetString
_Wlan3IwconfigCmd_Object = MibScalar
wlan3IwconfigCmd = _Wlan3IwconfigCmd_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 12, 1),
    _Wlan3IwconfigCmd_Type()
)
wlan3IwconfigCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3IwconfigCmd.setStatus("current")
_Wlan3Iwpriv_ObjectIdentity = ObjectIdentity
wlan3Iwpriv = _Wlan3Iwpriv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 14, 13)
)
_Wlan3IwprivCmd_Type = OctetString
_Wlan3IwprivCmd_Object = MibScalar
wlan3IwprivCmd = _Wlan3IwprivCmd_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 13, 1),
    _Wlan3IwprivCmd_Type()
)
wlan3IwprivCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3IwprivCmd.setStatus("current")
_Wlan3Key_Type = OctetString
_Wlan3Key_Object = MibScalar
wlan3Key = _Wlan3Key_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 14),
    _Wlan3Key_Type()
)
wlan3Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3Key.setStatus("current")
_Wlan3Keys_ObjectIdentity = ObjectIdentity
wlan3Keys = _Wlan3Keys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 14, 15)
)
_Wlan3Keys1_Type = OctetString
_Wlan3Keys1_Object = MibScalar
wlan3Keys1 = _Wlan3Keys1_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 15, 1),
    _Wlan3Keys1_Type()
)
wlan3Keys1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3Keys1.setStatus("current")
_Wlan3Keys2_Type = OctetString
_Wlan3Keys2_Object = MibScalar
wlan3Keys2 = _Wlan3Keys2_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 15, 2),
    _Wlan3Keys2_Type()
)
wlan3Keys2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3Keys2.setStatus("current")
_Wlan3Keys3_Type = OctetString
_Wlan3Keys3_Object = MibScalar
wlan3Keys3 = _Wlan3Keys3_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 15, 3),
    _Wlan3Keys3_Type()
)
wlan3Keys3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3Keys3.setStatus("current")
_Wlan3Keys4_Type = OctetString
_Wlan3Keys4_Object = MibScalar
wlan3Keys4 = _Wlan3Keys4_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 15, 4),
    _Wlan3Keys4_Type()
)
wlan3Keys4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3Keys4.setStatus("current")
_Wlan3KeysDefault_Type = OctetString
_Wlan3KeysDefault_Object = MibScalar
wlan3KeysDefault = _Wlan3KeysDefault_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 15, 5),
    _Wlan3KeysDefault_Type()
)
wlan3KeysDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3KeysDefault.setStatus("current")
_Wlan3Mode_Type = OctetString
_Wlan3Mode_Object = MibScalar
wlan3Mode = _Wlan3Mode_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 16),
    _Wlan3Mode_Type()
)
wlan3Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3Mode.setStatus("current")
_Wlan3Mtu_Type = Integer32
_Wlan3Mtu_Object = MibScalar
wlan3Mtu = _Wlan3Mtu_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 17),
    _Wlan3Mtu_Type()
)
wlan3Mtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3Mtu.setStatus("current")
_Wlan3Radio_Type = OctetString
_Wlan3Radio_Object = MibScalar
wlan3Radio = _Wlan3Radio_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 18),
    _Wlan3Radio_Type()
)
wlan3Radio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3Radio.setStatus("current")
_Wlan3Rate_Type = OctetString
_Wlan3Rate_Object = MibScalar
wlan3Rate = _Wlan3Rate_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 19),
    _Wlan3Rate_Type()
)
wlan3Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3Rate.setStatus("current")
_Wlan3Role_Type = OctetString
_Wlan3Role_Object = MibScalar
wlan3Role = _Wlan3Role_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 20),
    _Wlan3Role_Type()
)
wlan3Role.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3Role.setStatus("current")
_Wlan3Routes_ObjectIdentity = ObjectIdentity
wlan3Routes = _Wlan3Routes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 14, 21)
)
_Wlan3RoutesStatic_Type = OctetString
_Wlan3RoutesStatic_Object = MibScalar
wlan3RoutesStatic = _Wlan3RoutesStatic_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 21, 1),
    _Wlan3RoutesStatic_Type()
)
wlan3RoutesStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3RoutesStatic.setStatus("current")
_Wlan3Vlan_ObjectIdentity = ObjectIdentity
wlan3Vlan = _Wlan3Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 14, 22)
)
_Wlan3VlanEnable_Type = OctetString
_Wlan3VlanEnable_Object = MibScalar
wlan3VlanEnable = _Wlan3VlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 22, 1),
    _Wlan3VlanEnable_Type()
)
wlan3VlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3VlanEnable.setStatus("current")
_Wlan3VlanId_Type = Integer32
_Wlan3VlanId_Object = MibScalar
wlan3VlanId = _Wlan3VlanId_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 22, 2),
    _Wlan3VlanId_Type()
)
wlan3VlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3VlanId.setStatus("current")
_Wlan3Wpa_ObjectIdentity = ObjectIdentity
wlan3Wpa = _Wlan3Wpa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23)
)
_Wlan3WpaAuth_ObjectIdentity = ObjectIdentity
wlan3WpaAuth = _Wlan3WpaAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 1)
)
_Wlan3WpaAuthArgs_Type = OctetString
_Wlan3WpaAuthArgs_Object = MibScalar
wlan3WpaAuthArgs = _Wlan3WpaAuthArgs_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 1, 1),
    _Wlan3WpaAuthArgs_Type()
)
wlan3WpaAuthArgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3WpaAuthArgs.setStatus("current")
_Wlan3WpaAuthCustom_Type = OctetString
_Wlan3WpaAuthCustom_Object = MibScalar
wlan3WpaAuthCustom = _Wlan3WpaAuthCustom_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 1, 2),
    _Wlan3WpaAuthCustom_Type()
)
wlan3WpaAuthCustom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3WpaAuthCustom.setStatus("current")
_Wlan3WpaAuthInternal_Type = OctetString
_Wlan3WpaAuthInternal_Object = MibScalar
wlan3WpaAuthInternal = _Wlan3WpaAuthInternal_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 1, 3),
    _Wlan3WpaAuthInternal_Type()
)
wlan3WpaAuthInternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3WpaAuthInternal.setStatus("current")
_Wlan3WpaAuthServer_ObjectIdentity = ObjectIdentity
wlan3WpaAuthServer = _Wlan3WpaAuthServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 1, 4)
)
_Wlan3WpaAuthServerAddr_Type = OctetString
_Wlan3WpaAuthServerAddr_Object = MibScalar
wlan3WpaAuthServerAddr = _Wlan3WpaAuthServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 1, 4, 1),
    _Wlan3WpaAuthServerAddr_Type()
)
wlan3WpaAuthServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3WpaAuthServerAddr.setStatus("current")
_Wlan3WpaAuthServerPort_Type = Integer32
_Wlan3WpaAuthServerPort_Object = MibScalar
wlan3WpaAuthServerPort = _Wlan3WpaAuthServerPort_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 1, 4, 2),
    _Wlan3WpaAuthServerPort_Type()
)
wlan3WpaAuthServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3WpaAuthServerPort.setStatus("current")
_Wlan3WpaAuthServerSharedsecret_Type = OctetString
_Wlan3WpaAuthServerSharedsecret_Object = MibScalar
wlan3WpaAuthServerSharedsecret = _Wlan3WpaAuthServerSharedsecret_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 1, 4, 3),
    _Wlan3WpaAuthServerSharedsecret_Type()
)
wlan3WpaAuthServerSharedsecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3WpaAuthServerSharedsecret.setStatus("current")
_Wlan3WpaAuthType_Type = OctetString
_Wlan3WpaAuthType_Object = MibScalar
wlan3WpaAuthType = _Wlan3WpaAuthType_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 1, 5),
    _Wlan3WpaAuthType_Type()
)
wlan3WpaAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3WpaAuthType.setStatus("current")
_Wlan3WpaBridge_Type = OctetString
_Wlan3WpaBridge_Object = MibScalar
wlan3WpaBridge = _Wlan3WpaBridge_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 2),
    _Wlan3WpaBridge_Type()
)
wlan3WpaBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan3WpaBridge.setStatus("current")
_Wlan3WpaCa_ObjectIdentity = ObjectIdentity
wlan3WpaCa = _Wlan3WpaCa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 3)
)
_Wlan3WpaCaCert_ObjectIdentity = ObjectIdentity
wlan3WpaCaCert = _Wlan3WpaCaCert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 3, 1)
)
_Wlan3WpaCaCertFile_Type = OctetString
_Wlan3WpaCaCertFile_Object = MibScalar
wlan3WpaCaCertFile = _Wlan3WpaCaCertFile_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 3, 1, 1),
    _Wlan3WpaCaCertFile_Type()
)
wlan3WpaCaCertFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3WpaCaCertFile.setStatus("current")
_Wlan3WpaEapol_ObjectIdentity = ObjectIdentity
wlan3WpaEapol = _Wlan3WpaEapol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 4)
)
_Wlan3WpaEapolVersion_Type = OctetString
_Wlan3WpaEapolVersion_Object = MibScalar
wlan3WpaEapolVersion = _Wlan3WpaEapolVersion_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 4, 1),
    _Wlan3WpaEapolVersion_Type()
)
wlan3WpaEapolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3WpaEapolVersion.setStatus("current")
_Wlan3WpaEnable_Type = OctetString
_Wlan3WpaEnable_Object = MibScalar
wlan3WpaEnable = _Wlan3WpaEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 5),
    _Wlan3WpaEnable_Type()
)
wlan3WpaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3WpaEnable.setStatus("current")
_Wlan3WpaEssid_Type = OctetString
_Wlan3WpaEssid_Object = MibScalar
wlan3WpaEssid = _Wlan3WpaEssid_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 6),
    _Wlan3WpaEssid_Type()
)
wlan3WpaEssid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3WpaEssid.setStatus("current")
_Wlan3WpaIf_Type = OctetString
_Wlan3WpaIf_Object = MibScalar
wlan3WpaIf = _Wlan3WpaIf_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 7),
    _Wlan3WpaIf_Type()
)
wlan3WpaIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan3WpaIf.setStatus("current")
_Wlan3WpaKeymgmt_Type = OctetString
_Wlan3WpaKeymgmt_Object = MibScalar
wlan3WpaKeymgmt = _Wlan3WpaKeymgmt_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 8),
    _Wlan3WpaKeymgmt_Type()
)
wlan3WpaKeymgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3WpaKeymgmt.setStatus("current")
_Wlan3WpaMode_Type = Integer32
_Wlan3WpaMode_Object = MibScalar
wlan3WpaMode = _Wlan3WpaMode_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 9),
    _Wlan3WpaMode_Type()
)
wlan3WpaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3WpaMode.setStatus("current")
_Wlan3WpaNode_ObjectIdentity = ObjectIdentity
wlan3WpaNode = _Wlan3WpaNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 10)
)
_Wlan3WpaNodeCert_ObjectIdentity = ObjectIdentity
wlan3WpaNodeCert = _Wlan3WpaNodeCert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 10, 1)
)
_Wlan3WpaNodeCertFile_Type = OctetString
_Wlan3WpaNodeCertFile_Object = MibScalar
wlan3WpaNodeCertFile = _Wlan3WpaNodeCertFile_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 10, 1, 1),
    _Wlan3WpaNodeCertFile_Type()
)
wlan3WpaNodeCertFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3WpaNodeCertFile.setStatus("current")
_Wlan3WpaNodeKey_ObjectIdentity = ObjectIdentity
wlan3WpaNodeKey = _Wlan3WpaNodeKey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 10, 2)
)
_Wlan3WpaNodeKeyFile_Type = OctetString
_Wlan3WpaNodeKeyFile_Object = MibScalar
wlan3WpaNodeKeyFile = _Wlan3WpaNodeKeyFile_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 10, 2, 1),
    _Wlan3WpaNodeKeyFile_Type()
)
wlan3WpaNodeKeyFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3WpaNodeKeyFile.setStatus("current")
_Wlan3WpaNodeKeyPassphrase_Type = OctetString
_Wlan3WpaNodeKeyPassphrase_Object = MibScalar
wlan3WpaNodeKeyPassphrase = _Wlan3WpaNodeKeyPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 10, 2, 2),
    _Wlan3WpaNodeKeyPassphrase_Type()
)
wlan3WpaNodeKeyPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3WpaNodeKeyPassphrase.setStatus("current")
_Wlan3WpaPairwise_Type = OctetString
_Wlan3WpaPairwise_Object = MibScalar
wlan3WpaPairwise = _Wlan3WpaPairwise_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 11),
    _Wlan3WpaPairwise_Type()
)
wlan3WpaPairwise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3WpaPairwise.setStatus("current")
_Wlan3WpaPassphrase_Type = OctetString
_Wlan3WpaPassphrase_Object = MibScalar
wlan3WpaPassphrase = _Wlan3WpaPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 24350, 14, 23, 12),
    _Wlan3WpaPassphrase_Type()
)
wlan3WpaPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan3WpaPassphrase.setStatus("current")
_Wlan4_ObjectIdentity = ObjectIdentity
wlan4 = _Wlan4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 15)
)
_Wlan4Acl_ObjectIdentity = ObjectIdentity
wlan4Acl = _Wlan4Acl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 15, 1)
)
_Wlan4AclMode_Type = OctetString
_Wlan4AclMode_Object = MibScalar
wlan4AclMode = _Wlan4AclMode_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 1, 1),
    _Wlan4AclMode_Type()
)
wlan4AclMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4AclMode.setStatus("current")
_Wlan4Beaconinterval_Type = Integer32
_Wlan4Beaconinterval_Object = MibScalar
wlan4Beaconinterval = _Wlan4Beaconinterval_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 2),
    _Wlan4Beaconinterval_Type()
)
wlan4Beaconinterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4Beaconinterval.setStatus("current")
_Wlan4Cellid_Type = OctetString
_Wlan4Cellid_Object = MibScalar
wlan4Cellid = _Wlan4Cellid_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 3),
    _Wlan4Cellid_Type()
)
wlan4Cellid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4Cellid.setStatus("current")
_Wlan4Dhcp_ObjectIdentity = ObjectIdentity
wlan4Dhcp = _Wlan4Dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 15, 4)
)
_Wlan4DhcpAlwaysbroadcast_Type = OctetString
_Wlan4DhcpAlwaysbroadcast_Object = MibScalar
wlan4DhcpAlwaysbroadcast = _Wlan4DhcpAlwaysbroadcast_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 4, 1),
    _Wlan4DhcpAlwaysbroadcast_Type()
)
wlan4DhcpAlwaysbroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4DhcpAlwaysbroadcast.setStatus("current")
_Wlan4DhcpDefaultleasetime_Type = Integer32
_Wlan4DhcpDefaultleasetime_Object = MibScalar
wlan4DhcpDefaultleasetime = _Wlan4DhcpDefaultleasetime_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 4, 2),
    _Wlan4DhcpDefaultleasetime_Type()
)
wlan4DhcpDefaultleasetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4DhcpDefaultleasetime.setStatus("current")
_Wlan4DhcpMaxleasetime_Type = Integer32
_Wlan4DhcpMaxleasetime_Object = MibScalar
wlan4DhcpMaxleasetime = _Wlan4DhcpMaxleasetime_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 4, 3),
    _Wlan4DhcpMaxleasetime_Type()
)
wlan4DhcpMaxleasetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4DhcpMaxleasetime.setStatus("current")
_Wlan4DhcpRelay_ObjectIdentity = ObjectIdentity
wlan4DhcpRelay = _Wlan4DhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 15, 4, 4)
)
_Wlan4DhcpRelayEnable_Type = OctetString
_Wlan4DhcpRelayEnable_Object = MibScalar
wlan4DhcpRelayEnable = _Wlan4DhcpRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 4, 4, 1),
    _Wlan4DhcpRelayEnable_Type()
)
wlan4DhcpRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4DhcpRelayEnable.setStatus("current")
_Wlan4DhcpReserve_Type = Integer32
_Wlan4DhcpReserve_Object = MibScalar
wlan4DhcpReserve = _Wlan4DhcpReserve_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 4, 5),
    _Wlan4DhcpReserve_Type()
)
wlan4DhcpReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4DhcpReserve.setStatus("current")
_Wlan4DhcpRole_Type = OctetString
_Wlan4DhcpRole_Object = MibScalar
wlan4DhcpRole = _Wlan4DhcpRole_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 4, 6),
    _Wlan4DhcpRole_Type()
)
wlan4DhcpRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4DhcpRole.setStatus("current")
_Wlan4Enable_Type = OctetString
_Wlan4Enable_Object = MibScalar
wlan4Enable = _Wlan4Enable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 5),
    _Wlan4Enable_Type()
)
wlan4Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4Enable.setStatus("current")
_Wlan4Enhsec_Type = OctetString
_Wlan4Enhsec_Object = MibScalar
wlan4Enhsec = _Wlan4Enhsec_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 6),
    _Wlan4Enhsec_Type()
)
wlan4Enhsec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4Enhsec.setStatus("current")
_Wlan4Essid_Type = OctetString
_Wlan4Essid_Object = MibScalar
wlan4Essid = _Wlan4Essid_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 7),
    _Wlan4Essid_Type()
)
wlan4Essid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4Essid.setStatus("current")
_Wlan4Frag_Type = OctetString
_Wlan4Frag_Object = MibScalar
wlan4Frag = _Wlan4Frag_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 8),
    _Wlan4Frag_Type()
)
wlan4Frag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4Frag.setStatus("current")
_Wlan4Hideessid_Type = OctetString
_Wlan4Hideessid_Object = MibScalar
wlan4Hideessid = _Wlan4Hideessid_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 9),
    _Wlan4Hideessid_Type()
)
wlan4Hideessid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4Hideessid.setStatus("current")
_Wlan4If_Type = OctetString
_Wlan4If_Object = MibScalar
wlan4If = _Wlan4If_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 10),
    _Wlan4If_Type()
)
wlan4If.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan4If.setStatus("current")
_Wlan4Ip_ObjectIdentity = ObjectIdentity
wlan4Ip = _Wlan4Ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 15, 11)
)
_Wlan4IpAddress_Type = OctetString
_Wlan4IpAddress_Object = MibScalar
wlan4IpAddress = _Wlan4IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 11, 1),
    _Wlan4IpAddress_Type()
)
wlan4IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan4IpAddress.setStatus("current")
_Wlan4IpAddressforce_Type = OctetString
_Wlan4IpAddressforce_Object = MibScalar
wlan4IpAddressforce = _Wlan4IpAddressforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 11, 2),
    _Wlan4IpAddressforce_Type()
)
wlan4IpAddressforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4IpAddressforce.setStatus("current")
_Wlan4IpBroadcast_Type = OctetString
_Wlan4IpBroadcast_Object = MibScalar
wlan4IpBroadcast = _Wlan4IpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 11, 3),
    _Wlan4IpBroadcast_Type()
)
wlan4IpBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan4IpBroadcast.setStatus("current")
_Wlan4IpBroadcastforce_Type = OctetString
_Wlan4IpBroadcastforce_Object = MibScalar
wlan4IpBroadcastforce = _Wlan4IpBroadcastforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 11, 4),
    _Wlan4IpBroadcastforce_Type()
)
wlan4IpBroadcastforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4IpBroadcastforce.setStatus("current")
_Wlan4IpGateway_Type = OctetString
_Wlan4IpGateway_Object = MibScalar
wlan4IpGateway = _Wlan4IpGateway_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 11, 5),
    _Wlan4IpGateway_Type()
)
wlan4IpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan4IpGateway.setStatus("current")
_Wlan4IpGatewayforce_Type = OctetString
_Wlan4IpGatewayforce_Object = MibScalar
wlan4IpGatewayforce = _Wlan4IpGatewayforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 11, 6),
    _Wlan4IpGatewayforce_Type()
)
wlan4IpGatewayforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4IpGatewayforce.setStatus("current")
_Wlan4IpImplicit_ObjectIdentity = ObjectIdentity
wlan4IpImplicit = _Wlan4IpImplicit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 15, 11, 7)
)
_Wlan4IpImplicitSize_ObjectIdentity = ObjectIdentity
wlan4IpImplicitSize = _Wlan4IpImplicitSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 15, 11, 7, 1)
)
_Wlan4IpImplicitSizeActual_Type = Integer32
_Wlan4IpImplicitSizeActual_Object = MibScalar
wlan4IpImplicitSizeActual = _Wlan4IpImplicitSizeActual_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 11, 7, 1, 1),
    _Wlan4IpImplicitSizeActual_Type()
)
wlan4IpImplicitSizeActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan4IpImplicitSizeActual.setStatus("current")
_Wlan4IpImplicitSizeRequested_Type = OctetString
_Wlan4IpImplicitSizeRequested_Object = MibScalar
wlan4IpImplicitSizeRequested = _Wlan4IpImplicitSizeRequested_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 11, 7, 1, 2),
    _Wlan4IpImplicitSizeRequested_Type()
)
wlan4IpImplicitSizeRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4IpImplicitSizeRequested.setStatus("current")
_Wlan4IpImplicitStart_ObjectIdentity = ObjectIdentity
wlan4IpImplicitStart = _Wlan4IpImplicitStart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 15, 11, 7, 2)
)
_Wlan4IpImplicitStartActual_Type = Integer32
_Wlan4IpImplicitStartActual_Object = MibScalar
wlan4IpImplicitStartActual = _Wlan4IpImplicitStartActual_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 11, 7, 2, 1),
    _Wlan4IpImplicitStartActual_Type()
)
wlan4IpImplicitStartActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan4IpImplicitStartActual.setStatus("current")
_Wlan4IpImplicitStartRequested_Type = OctetString
_Wlan4IpImplicitStartRequested_Object = MibScalar
wlan4IpImplicitStartRequested = _Wlan4IpImplicitStartRequested_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 11, 7, 2, 2),
    _Wlan4IpImplicitStartRequested_Type()
)
wlan4IpImplicitStartRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4IpImplicitStartRequested.setStatus("current")
_Wlan4IpNetmask_Type = OctetString
_Wlan4IpNetmask_Object = MibScalar
wlan4IpNetmask = _Wlan4IpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 11, 8),
    _Wlan4IpNetmask_Type()
)
wlan4IpNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan4IpNetmask.setStatus("current")
_Wlan4IpNetmaskforce_Type = OctetString
_Wlan4IpNetmaskforce_Object = MibScalar
wlan4IpNetmaskforce = _Wlan4IpNetmaskforce_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 11, 9),
    _Wlan4IpNetmaskforce_Type()
)
wlan4IpNetmaskforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4IpNetmaskforce.setStatus("current")
_Wlan4Iwconfig_ObjectIdentity = ObjectIdentity
wlan4Iwconfig = _Wlan4Iwconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 15, 12)
)
_Wlan4IwconfigCmd_Type = OctetString
_Wlan4IwconfigCmd_Object = MibScalar
wlan4IwconfigCmd = _Wlan4IwconfigCmd_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 12, 1),
    _Wlan4IwconfigCmd_Type()
)
wlan4IwconfigCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4IwconfigCmd.setStatus("current")
_Wlan4Iwpriv_ObjectIdentity = ObjectIdentity
wlan4Iwpriv = _Wlan4Iwpriv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 15, 13)
)
_Wlan4IwprivCmd_Type = OctetString
_Wlan4IwprivCmd_Object = MibScalar
wlan4IwprivCmd = _Wlan4IwprivCmd_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 13, 1),
    _Wlan4IwprivCmd_Type()
)
wlan4IwprivCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4IwprivCmd.setStatus("current")
_Wlan4Key_Type = OctetString
_Wlan4Key_Object = MibScalar
wlan4Key = _Wlan4Key_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 14),
    _Wlan4Key_Type()
)
wlan4Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4Key.setStatus("current")
_Wlan4Keys_ObjectIdentity = ObjectIdentity
wlan4Keys = _Wlan4Keys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 15, 15)
)
_Wlan4Keys1_Type = OctetString
_Wlan4Keys1_Object = MibScalar
wlan4Keys1 = _Wlan4Keys1_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 15, 1),
    _Wlan4Keys1_Type()
)
wlan4Keys1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4Keys1.setStatus("current")
_Wlan4Keys2_Type = OctetString
_Wlan4Keys2_Object = MibScalar
wlan4Keys2 = _Wlan4Keys2_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 15, 2),
    _Wlan4Keys2_Type()
)
wlan4Keys2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4Keys2.setStatus("current")
_Wlan4Keys3_Type = OctetString
_Wlan4Keys3_Object = MibScalar
wlan4Keys3 = _Wlan4Keys3_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 15, 3),
    _Wlan4Keys3_Type()
)
wlan4Keys3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4Keys3.setStatus("current")
_Wlan4Keys4_Type = OctetString
_Wlan4Keys4_Object = MibScalar
wlan4Keys4 = _Wlan4Keys4_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 15, 4),
    _Wlan4Keys4_Type()
)
wlan4Keys4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4Keys4.setStatus("current")
_Wlan4KeysDefault_Type = OctetString
_Wlan4KeysDefault_Object = MibScalar
wlan4KeysDefault = _Wlan4KeysDefault_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 15, 5),
    _Wlan4KeysDefault_Type()
)
wlan4KeysDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4KeysDefault.setStatus("current")
_Wlan4Mode_Type = OctetString
_Wlan4Mode_Object = MibScalar
wlan4Mode = _Wlan4Mode_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 16),
    _Wlan4Mode_Type()
)
wlan4Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4Mode.setStatus("current")
_Wlan4Mtu_Type = Integer32
_Wlan4Mtu_Object = MibScalar
wlan4Mtu = _Wlan4Mtu_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 17),
    _Wlan4Mtu_Type()
)
wlan4Mtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4Mtu.setStatus("current")
_Wlan4Radio_Type = OctetString
_Wlan4Radio_Object = MibScalar
wlan4Radio = _Wlan4Radio_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 18),
    _Wlan4Radio_Type()
)
wlan4Radio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4Radio.setStatus("current")
_Wlan4Rate_Type = OctetString
_Wlan4Rate_Object = MibScalar
wlan4Rate = _Wlan4Rate_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 19),
    _Wlan4Rate_Type()
)
wlan4Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4Rate.setStatus("current")
_Wlan4Role_Type = OctetString
_Wlan4Role_Object = MibScalar
wlan4Role = _Wlan4Role_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 20),
    _Wlan4Role_Type()
)
wlan4Role.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4Role.setStatus("current")
_Wlan4Routes_ObjectIdentity = ObjectIdentity
wlan4Routes = _Wlan4Routes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 15, 21)
)
_Wlan4RoutesStatic_Type = OctetString
_Wlan4RoutesStatic_Object = MibScalar
wlan4RoutesStatic = _Wlan4RoutesStatic_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 21, 1),
    _Wlan4RoutesStatic_Type()
)
wlan4RoutesStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4RoutesStatic.setStatus("current")
_Wlan4Vlan_ObjectIdentity = ObjectIdentity
wlan4Vlan = _Wlan4Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 15, 22)
)
_Wlan4VlanEnable_Type = OctetString
_Wlan4VlanEnable_Object = MibScalar
wlan4VlanEnable = _Wlan4VlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 22, 1),
    _Wlan4VlanEnable_Type()
)
wlan4VlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4VlanEnable.setStatus("current")
_Wlan4VlanId_Type = Integer32
_Wlan4VlanId_Object = MibScalar
wlan4VlanId = _Wlan4VlanId_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 22, 2),
    _Wlan4VlanId_Type()
)
wlan4VlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4VlanId.setStatus("current")
_Wlan4Wpa_ObjectIdentity = ObjectIdentity
wlan4Wpa = _Wlan4Wpa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23)
)
_Wlan4WpaAuth_ObjectIdentity = ObjectIdentity
wlan4WpaAuth = _Wlan4WpaAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 1)
)
_Wlan4WpaAuthArgs_Type = OctetString
_Wlan4WpaAuthArgs_Object = MibScalar
wlan4WpaAuthArgs = _Wlan4WpaAuthArgs_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 1, 1),
    _Wlan4WpaAuthArgs_Type()
)
wlan4WpaAuthArgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4WpaAuthArgs.setStatus("current")
_Wlan4WpaAuthCustom_Type = OctetString
_Wlan4WpaAuthCustom_Object = MibScalar
wlan4WpaAuthCustom = _Wlan4WpaAuthCustom_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 1, 2),
    _Wlan4WpaAuthCustom_Type()
)
wlan4WpaAuthCustom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4WpaAuthCustom.setStatus("current")
_Wlan4WpaAuthInternal_Type = OctetString
_Wlan4WpaAuthInternal_Object = MibScalar
wlan4WpaAuthInternal = _Wlan4WpaAuthInternal_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 1, 3),
    _Wlan4WpaAuthInternal_Type()
)
wlan4WpaAuthInternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4WpaAuthInternal.setStatus("current")
_Wlan4WpaAuthServer_ObjectIdentity = ObjectIdentity
wlan4WpaAuthServer = _Wlan4WpaAuthServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 1, 4)
)
_Wlan4WpaAuthServerAddr_Type = OctetString
_Wlan4WpaAuthServerAddr_Object = MibScalar
wlan4WpaAuthServerAddr = _Wlan4WpaAuthServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 1, 4, 1),
    _Wlan4WpaAuthServerAddr_Type()
)
wlan4WpaAuthServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4WpaAuthServerAddr.setStatus("current")
_Wlan4WpaAuthServerPort_Type = Integer32
_Wlan4WpaAuthServerPort_Object = MibScalar
wlan4WpaAuthServerPort = _Wlan4WpaAuthServerPort_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 1, 4, 2),
    _Wlan4WpaAuthServerPort_Type()
)
wlan4WpaAuthServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4WpaAuthServerPort.setStatus("current")
_Wlan4WpaAuthServerSharedsecret_Type = OctetString
_Wlan4WpaAuthServerSharedsecret_Object = MibScalar
wlan4WpaAuthServerSharedsecret = _Wlan4WpaAuthServerSharedsecret_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 1, 4, 3),
    _Wlan4WpaAuthServerSharedsecret_Type()
)
wlan4WpaAuthServerSharedsecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4WpaAuthServerSharedsecret.setStatus("current")
_Wlan4WpaAuthType_Type = OctetString
_Wlan4WpaAuthType_Object = MibScalar
wlan4WpaAuthType = _Wlan4WpaAuthType_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 1, 5),
    _Wlan4WpaAuthType_Type()
)
wlan4WpaAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4WpaAuthType.setStatus("current")
_Wlan4WpaBridge_Type = OctetString
_Wlan4WpaBridge_Object = MibScalar
wlan4WpaBridge = _Wlan4WpaBridge_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 2),
    _Wlan4WpaBridge_Type()
)
wlan4WpaBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan4WpaBridge.setStatus("current")
_Wlan4WpaCa_ObjectIdentity = ObjectIdentity
wlan4WpaCa = _Wlan4WpaCa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 3)
)
_Wlan4WpaCaCert_ObjectIdentity = ObjectIdentity
wlan4WpaCaCert = _Wlan4WpaCaCert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 3, 1)
)
_Wlan4WpaCaCertFile_Type = OctetString
_Wlan4WpaCaCertFile_Object = MibScalar
wlan4WpaCaCertFile = _Wlan4WpaCaCertFile_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 3, 1, 1),
    _Wlan4WpaCaCertFile_Type()
)
wlan4WpaCaCertFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4WpaCaCertFile.setStatus("current")
_Wlan4WpaEapol_ObjectIdentity = ObjectIdentity
wlan4WpaEapol = _Wlan4WpaEapol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 4)
)
_Wlan4WpaEapolVersion_Type = OctetString
_Wlan4WpaEapolVersion_Object = MibScalar
wlan4WpaEapolVersion = _Wlan4WpaEapolVersion_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 4, 1),
    _Wlan4WpaEapolVersion_Type()
)
wlan4WpaEapolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4WpaEapolVersion.setStatus("current")
_Wlan4WpaEnable_Type = OctetString
_Wlan4WpaEnable_Object = MibScalar
wlan4WpaEnable = _Wlan4WpaEnable_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 5),
    _Wlan4WpaEnable_Type()
)
wlan4WpaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4WpaEnable.setStatus("current")
_Wlan4WpaEssid_Type = OctetString
_Wlan4WpaEssid_Object = MibScalar
wlan4WpaEssid = _Wlan4WpaEssid_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 6),
    _Wlan4WpaEssid_Type()
)
wlan4WpaEssid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4WpaEssid.setStatus("current")
_Wlan4WpaIf_Type = OctetString
_Wlan4WpaIf_Object = MibScalar
wlan4WpaIf = _Wlan4WpaIf_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 7),
    _Wlan4WpaIf_Type()
)
wlan4WpaIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlan4WpaIf.setStatus("current")
_Wlan4WpaKeymgmt_Type = OctetString
_Wlan4WpaKeymgmt_Object = MibScalar
wlan4WpaKeymgmt = _Wlan4WpaKeymgmt_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 8),
    _Wlan4WpaKeymgmt_Type()
)
wlan4WpaKeymgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4WpaKeymgmt.setStatus("current")
_Wlan4WpaMode_Type = Integer32
_Wlan4WpaMode_Object = MibScalar
wlan4WpaMode = _Wlan4WpaMode_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 9),
    _Wlan4WpaMode_Type()
)
wlan4WpaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4WpaMode.setStatus("current")
_Wlan4WpaNode_ObjectIdentity = ObjectIdentity
wlan4WpaNode = _Wlan4WpaNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 10)
)
_Wlan4WpaNodeCert_ObjectIdentity = ObjectIdentity
wlan4WpaNodeCert = _Wlan4WpaNodeCert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 10, 1)
)
_Wlan4WpaNodeCertFile_Type = OctetString
_Wlan4WpaNodeCertFile_Object = MibScalar
wlan4WpaNodeCertFile = _Wlan4WpaNodeCertFile_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 10, 1, 1),
    _Wlan4WpaNodeCertFile_Type()
)
wlan4WpaNodeCertFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4WpaNodeCertFile.setStatus("current")
_Wlan4WpaNodeKey_ObjectIdentity = ObjectIdentity
wlan4WpaNodeKey = _Wlan4WpaNodeKey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 10, 2)
)
_Wlan4WpaNodeKeyFile_Type = OctetString
_Wlan4WpaNodeKeyFile_Object = MibScalar
wlan4WpaNodeKeyFile = _Wlan4WpaNodeKeyFile_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 10, 2, 1),
    _Wlan4WpaNodeKeyFile_Type()
)
wlan4WpaNodeKeyFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4WpaNodeKeyFile.setStatus("current")
_Wlan4WpaNodeKeyPassphrase_Type = OctetString
_Wlan4WpaNodeKeyPassphrase_Object = MibScalar
wlan4WpaNodeKeyPassphrase = _Wlan4WpaNodeKeyPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 10, 2, 2),
    _Wlan4WpaNodeKeyPassphrase_Type()
)
wlan4WpaNodeKeyPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4WpaNodeKeyPassphrase.setStatus("current")
_Wlan4WpaPairwise_Type = OctetString
_Wlan4WpaPairwise_Object = MibScalar
wlan4WpaPairwise = _Wlan4WpaPairwise_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 11),
    _Wlan4WpaPairwise_Type()
)
wlan4WpaPairwise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4WpaPairwise.setStatus("current")
_Wlan4WpaPassphrase_Type = OctetString
_Wlan4WpaPassphrase_Object = MibScalar
wlan4WpaPassphrase = _Wlan4WpaPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 24350, 15, 23, 12),
    _Wlan4WpaPassphrase_Type()
)
wlan4WpaPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlan4WpaPassphrase.setStatus("current")
_EnRouteTraps_ObjectIdentity = ObjectIdentity
enRouteTraps = _EnRouteTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24350, 100)
)

# Managed Objects groups


# Notification objects

enRouteConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 24350, 100, 0, 1)
)
enRouteConfigChange.setObjects(
    ("TRANZEO-ENROUTE-MUNIWIFI-MIB", "lastModification")
)
if mibBuilder.loadTexts:
    enRouteConfigChange.setStatus(
        ""
    )

enRouteConfigReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 24350, 100, 0, 2)
)
enRouteConfigReset.setObjects(
    ("TRANZEO-ENROUTE-MUNIWIFI-MIB", "lastModification")
)
if mibBuilder.loadTexts:
    enRouteConfigReset.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRANZEO-ENROUTE-MUNIWIFI-MIB",
    **{"enRoute": enRoute,
       "version": version,
       "versionDriver80211": versionDriver80211,
       "versionFirmware": versionFirmware,
       "versionLoaded-profile": versionLoaded_profile,
       "versionMcm": versionMcm,
       "versionPatches": versionPatches,
       "versionQos": versionQos,
       "versionRelease": versionRelease,
       "sys": sys,
       "sysApply": sysApply,
       "sysApplyEffect": sysApplyEffect,
       "sysApplyTime": sysApplyTime,
       "sysDev": sysDev,
       "sysDevBattery": sysDevBattery,
       "sysDevBatteryEnable": sysDevBatteryEnable,
       "sysDevBatteryInstalled": sysDevBatteryInstalled,
       "sysDevLed": sysDevLed,
       "sysDevLedEnable": sysDevLedEnable,
       "sysDevPoe": sysDevPoe,
       "sysDevPoeEnable": sysDevPoeEnable,
       "sysDevPoeInstalled": sysDevPoeInstalled,
       "sysDevPoeVoltage": sysDevPoeVoltage,
       "sysDevWlan": sysDevWlan,
       "sysDevWlanCountry": sysDevWlanCountry,
       "sysDhcp": sysDhcp,
       "sysDhcpArgs": sysDhcpArgs,
       "sysDhcpEnableserver": sysDhcpEnableserver,
       "sysDhcpRelay": sysDhcpRelay,
       "sysDhcpRelayAgent": sysDhcpRelayAgent,
       "sysDhcpRelayAgentBase": sysDhcpRelayAgentBase,
       "sysDhcpRelayArgs": sysDhcpRelayArgs,
       "sysDhcpRelayArpnumbc": sysDhcpRelayArpnumbc,
       "sysDhcpRelayBindretries": sysDhcpRelayBindretries,
       "sysDhcpRelayEnable": sysDhcpRelayEnable,
       "sysDhcpRelayExtrahosts": sysDhcpRelayExtrahosts,
       "sysDhcpRelayGateway": sysDhcpRelayGateway,
       "sysDhcpRelayImr": sysDhcpRelayImr,
       "sysDhcpRelayImrNumbc": sysDhcpRelayImrNumbc,
       "sysDhcpRelayProxy": sysDhcpRelayProxy,
       "sysDhcpRelayServer": sysDhcpRelayServer,
       "sysDhcpRelayStalecheckinterval": sysDhcpRelayStalecheckinterval,
       "sysDhcpRelayStatic": sysDhcpRelayStatic,
       "sysDhcpRelayStaticBegin": sysDhcpRelayStaticBegin,
       "sysDhcpRelayStaticEnable": sysDhcpRelayStaticEnable,
       "sysDhcpRelayStaticEnd": sysDhcpRelayStaticEnd,
       "sysDhcpRelaySubnet": sysDhcpRelaySubnet,
       "sysDhcpRelayTunnel": sysDhcpRelayTunnel,
       "sysDhcpRelayTunnelEndpoint": sysDhcpRelayTunnelEndpoint,
       "sysDhcpRelayTunnelKeepalive": sysDhcpRelayTunnelKeepalive,
       "sysDhcpRelayTunnelTimeoutfactor": sysDhcpRelayTunnelTimeoutfactor,
       "sysDns": sysDns,
       "sysDnsServers": sysDnsServers,
       "sysDnsUpdatestyle": sysDnsUpdatestyle,
       "sysDnsproxy": sysDnsproxy,
       "sysDnsproxyEnable": sysDnsproxyEnable,
       "sysDnsproxyHosts": sysDnsproxyHosts,
       "sysDomain": sysDomain,
       "sysGui": sysGui,
       "sysGuiUpgrade": sysGuiUpgrade,
       "sysGuiUpgradeForce": sysGuiUpgradeForce,
       "sysHostname": sysHostname,
       "sysHosts": sysHosts,
       "sysHostsNms": sysHostsNms,
       "sysId": sysId,
       "sysIdLanprefix": sysIdLanprefix,
       "sysIdMesh": sysIdMesh,
       "sysIdMeshprefix": sysIdMeshprefix,
       "sysIdNode": sysIdNode,
       "sysImplicit": sysImplicit,
       "sysImplicitEnable": sysImplicitEnable,
       "sysInfo": sysInfo,
       "sysInfoCluster": sysInfoCluster,
       "sysL2": sysL2,
       "sysL2Bridge": sysL2Bridge,
       "sysL2BridgeEnable": sysL2BridgeEnable,
       "sysL2Clientmacfwd": sysL2Clientmacfwd,
       "sysL2Hideinternal": sysL2Hideinternal,
       "sysL2HideinternalEnable": sysL2HideinternalEnable,
       "sysL2HideinternalGateway": sysL2HideinternalGateway,
       "sysL2HideinternalGatewayAllow": sysL2HideinternalGatewayAllow,
       "sysL2HideinternalGatewayAllowRelaydhcp": sysL2HideinternalGatewayAllowRelaydhcp,
       "sysL2HideinternalGatewayDeny": sysL2HideinternalGatewayDeny,
       "sysL2HideinternalGatewayDenyAll": sysL2HideinternalGatewayDenyAll,
       "sysL2HideinternalGatewayDenyMesh": sysL2HideinternalGatewayDenyMesh,
       "sysLocation": sysLocation,
       "sysLocationGps": sysLocationGps,
       "sysLocationGpsAltitude": sysLocationGpsAltitude,
       "sysLocationGpsLatitude": sysLocationGpsLatitude,
       "sysLocationGpsLongitude": sysLocationGpsLongitude,
       "sysLocationPostal": sysLocationPostal,
       "sysMainstub": sysMainstub,
       "sysMainstubIf": sysMainstubIf,
       "sysMainstubProxyarp": sysMainstubProxyarp,
       "sysMonitor": sysMonitor,
       "sysMonitorHealth": sysMonitorHealth,
       "sysMonitorHealthEnable": sysMonitorHealthEnable,
       "sysMonitorHealthHost": sysMonitorHealthHost,
       "sysNat": sysNat,
       "sysNatEnable": sysNatEnable,
       "sysNetbios": sysNetbios,
       "sysNetbiosServers": sysNetbiosServers,
       "sysNets": sysNets,
       "sysNetsExternal": sysNetsExternal,
       "sysNetsExternalCombined": sysNetsExternalCombined,
       "sysNetsExternalDefault": sysNetsExternalDefault,
       "sysNetsExternalExtra": sysNetsExternalExtra,
       "sysNetsInternal": sysNetsInternal,
       "sysNetsInternalCombined": sysNetsInternalCombined,
       "sysNetsInternalDefault": sysNetsInternalDefault,
       "sysNetsInternalExtra": sysNetsInternalExtra,
       "sysNetsInternalFlexipdefault": sysNetsInternalFlexipdefault,
       "sysOrganization": sysOrganization,
       "sysOrganizationCity": sysOrganizationCity,
       "sysOrganizationCountry": sysOrganizationCountry,
       "sysOrganizationName": sysOrganizationName,
       "sysOrganizationState": sysOrganizationState,
       "sysPassword": sysPassword,
       "sysPasswordAdmin": sysPasswordAdmin,
       "sysPasswordMonitor": sysPasswordMonitor,
       "sysPlatform": sysPlatform,
       "sysProvisioning": sysProvisioning,
       "sysProvisioningEnable": sysProvisioningEnable,
       "sysRouting": sysRouting,
       "sysRoutingOspf": sysRoutingOspf,
       "sysRoutingRip": sysRoutingRip,
       "sysScheme": sysScheme,
       "sysShell": sysShell,
       "sysShellTimeout": sysShellTimeout,
       "sysSnmp": sysSnmp,
       "sysSnmpCommunity": sysSnmpCommunity,
       "sysSnmpCommunityRo": sysSnmpCommunityRo,
       "sysSnmpCommunityRw": sysSnmpCommunityRw,
       "sysSnmpCommunityTrap": sysSnmpCommunityTrap,
       "sysSnmpContact": sysSnmpContact,
       "sysSnmpLocation": sysSnmpLocation,
       "sysSnmpPort": sysSnmpPort,
       "sysSnmpTrap": sysSnmpTrap,
       "sysSnmpTrapHost": sysSnmpTrapHost,
       "sysSplash": sysSplash,
       "sysSplashAuth": sysSplashAuth,
       "sysSplashAuthServer": sysSplashAuthServer,
       "sysSplashAuthServerWlan1": sysSplashAuthServerWlan1,
       "sysSplashAuthServerWlan1Enable": sysSplashAuthServerWlan1Enable,
       "sysSplashAuthServerWlan1Host": sysSplashAuthServerWlan1Host,
       "sysSplashAuthServerWlan1Port": sysSplashAuthServerWlan1Port,
       "sysSplashAuthServerWlan1Secret": sysSplashAuthServerWlan1Secret,
       "sysSplashAuthServerWlan2": sysSplashAuthServerWlan2,
       "sysSplashAuthServerWlan2Enable": sysSplashAuthServerWlan2Enable,
       "sysSplashAuthServerWlan2Host": sysSplashAuthServerWlan2Host,
       "sysSplashAuthServerWlan2Port": sysSplashAuthServerWlan2Port,
       "sysSplashAuthServerWlan2Secret": sysSplashAuthServerWlan2Secret,
       "sysSplashAuthServerWlan3": sysSplashAuthServerWlan3,
       "sysSplashAuthServerWlan3Enable": sysSplashAuthServerWlan3Enable,
       "sysSplashAuthServerWlan3Host": sysSplashAuthServerWlan3Host,
       "sysSplashAuthServerWlan3Port": sysSplashAuthServerWlan3Port,
       "sysSplashAuthServerWlan3Secret": sysSplashAuthServerWlan3Secret,
       "sysSplashAuthServerWlan4": sysSplashAuthServerWlan4,
       "sysSplashAuthServerWlan4Enable": sysSplashAuthServerWlan4Enable,
       "sysSplashAuthServerWlan4Host": sysSplashAuthServerWlan4Host,
       "sysSplashAuthServerWlan4Port": sysSplashAuthServerWlan4Port,
       "sysSplashAuthServerWlan4Secret": sysSplashAuthServerWlan4Secret,
       "sysSplashBypasshosts": sysSplashBypasshosts,
       "sysSplashEnable": sysSplashEnable,
       "sysSplashEnableWlan1": sysSplashEnableWlan1,
       "sysSplashEnableWlan2": sysSplashEnableWlan2,
       "sysSplashEnableWlan3": sysSplashEnableWlan3,
       "sysSplashEnableWlan4": sysSplashEnableWlan4,
       "sysSplashExternal": sysSplashExternal,
       "sysSplashInternal": sysSplashInternal,
       "sysSplashTrustedmacs": sysSplashTrustedmacs,
       "sysSplashUrl": sysSplashUrl,
       "sysSplashUrlWlan1": sysSplashUrlWlan1,
       "sysSplashUrlWlan1Error": sysSplashUrlWlan1Error,
       "sysSplashUrlWlan1Fail": sysSplashUrlWlan1Fail,
       "sysSplashUrlWlan1Login": sysSplashUrlWlan1Login,
       "sysSplashUrlWlan1Success": sysSplashUrlWlan1Success,
       "sysSplashUrlWlan2": sysSplashUrlWlan2,
       "sysSplashUrlWlan2Error": sysSplashUrlWlan2Error,
       "sysSplashUrlWlan2Fail": sysSplashUrlWlan2Fail,
       "sysSplashUrlWlan2Login": sysSplashUrlWlan2Login,
       "sysSplashUrlWlan2Success": sysSplashUrlWlan2Success,
       "sysSplashUrlWlan3": sysSplashUrlWlan3,
       "sysSplashUrlWlan3Error": sysSplashUrlWlan3Error,
       "sysSplashUrlWlan3Fail": sysSplashUrlWlan3Fail,
       "sysSplashUrlWlan3Login": sysSplashUrlWlan3Login,
       "sysSplashUrlWlan3Success": sysSplashUrlWlan3Success,
       "sysSplashUrlWlan4": sysSplashUrlWlan4,
       "sysSplashUrlWlan4Error": sysSplashUrlWlan4Error,
       "sysSplashUrlWlan4Fail": sysSplashUrlWlan4Fail,
       "sysSplashUrlWlan4Login": sysSplashUrlWlan4Login,
       "sysSplashUrlWlan4Success": sysSplashUrlWlan4Success,
       "sysTime": sysTime,
       "sysTimeRfc868": sysTimeRfc868,
       "sysTimeRfc868Server": sysTimeRfc868Server,
       "sysTimeSyncdelay": sysTimeSyncdelay,
       "sysUnits": sysUnits,
       "firewall": firewall,
       "firewallConntrack": firewallConntrack,
       "firewallConntrackConnlimit": firewallConntrackConnlimit,
       "firewallConntrackConnlimitConnections": firewallConntrackConnlimitConnections,
       "firewallConntrackConnlimitEnable": firewallConntrackConnlimitEnable,
       "firewallConntrackTablesize": firewallConntrackTablesize,
       "firewallConntrackTcptimeoutestablished": firewallConntrackTcptimeoutestablished,
       "firewallGateway": firewallGateway,
       "firewallGatewayEnable": firewallGatewayEnable,
       "firewallNode": firewallNode,
       "firewallNodeAllowc2c": firewallNodeAllowc2c,
       "firewallNodeAllowc2cEth0": firewallNodeAllowc2cEth0,
       "firewallNodeAllowc2cWlan1": firewallNodeAllowc2cWlan1,
       "firewallNodeAllowc2cWlan2": firewallNodeAllowc2cWlan2,
       "firewallNodeAllowc2cWlan3": firewallNodeAllowc2cWlan3,
       "firewallNodeAllowc2cWlan4": firewallNodeAllowc2cWlan4,
       "firewallNodeEnable": firewallNodeEnable,
       "firewallNodeTcp": firewallNodeTcp,
       "firewallNodeTcpAllow": firewallNodeTcpAllow,
       "firewallNodeTcpAllowDest": firewallNodeTcpAllowDest,
       "firewallNodeTcpAllowSource": firewallNodeTcpAllowSource,
       "firewallNodeUdp": firewallNodeUdp,
       "firewallNodeUdpAllow": firewallNodeUdpAllow,
       "firewallNodeUdpAllowDest": firewallNodeUdpAllowDest,
       "firewallNodeUdpAllowSource": firewallNodeUdpAllowSource,
       "qos": qos,
       "qosEnable": qosEnable,
       "qosExtra": qosExtra,
       "qosIn": qosIn,
       "qosInDefault": qosInDefault,
       "qosInDefaultFlowpriority": qosInDefaultFlowpriority,
       "qosInDefaultHwpri": qosInDefaultHwpri,
       "qosInDefaultHwpriMax": qosInDefaultHwpriMax,
       "qosInDefaultHwpriMin": qosInDefaultHwpriMin,
       "qosInEth0": qosInEth0,
       "qosInEth0Flowpriority": qosInEth0Flowpriority,
       "qosInEth0Hwpri": qosInEth0Hwpri,
       "qosInEth0HwpriMax": qosInEth0HwpriMax,
       "qosInEth0HwpriMin": qosInEth0HwpriMin,
       "qosInLocal": qosInLocal,
       "qosInLocalFlowpriority": qosInLocalFlowpriority,
       "qosInLocalHwpri": qosInLocalHwpri,
       "qosInLocalHwpriMax": qosInLocalHwpriMax,
       "qosInLocalHwpriMin": qosInLocalHwpriMin,
       "qosInWlan0": qosInWlan0,
       "qosInWlan0Flowpriority": qosInWlan0Flowpriority,
       "qosInWlan0Hwpri": qosInWlan0Hwpri,
       "qosInWlan0HwpriMax": qosInWlan0HwpriMax,
       "qosInWlan0HwpriMin": qosInWlan0HwpriMin,
       "qosInWlan1": qosInWlan1,
       "qosInWlan1Flowpriority": qosInWlan1Flowpriority,
       "qosInWlan1Hwpri": qosInWlan1Hwpri,
       "qosInWlan1HwpriMax": qosInWlan1HwpriMax,
       "qosInWlan1HwpriMin": qosInWlan1HwpriMin,
       "qosInWlan2": qosInWlan2,
       "qosInWlan2Flowpriority": qosInWlan2Flowpriority,
       "qosInWlan2Hwpri": qosInWlan2Hwpri,
       "qosInWlan2HwpriMax": qosInWlan2HwpriMax,
       "qosInWlan2HwpriMin": qosInWlan2HwpriMin,
       "qosInWlan3": qosInWlan3,
       "qosInWlan3Flowpriority": qosInWlan3Flowpriority,
       "qosInWlan3Hwpri": qosInWlan3Hwpri,
       "qosInWlan3HwpriMax": qosInWlan3HwpriMax,
       "qosInWlan3HwpriMin": qosInWlan3HwpriMin,
       "qosInWlan4": qosInWlan4,
       "qosInWlan4Flowpriority": qosInWlan4Flowpriority,
       "qosInWlan4Hwpri": qosInWlan4Hwpri,
       "qosInWlan4HwpriMax": qosInWlan4HwpriMax,
       "qosInWlan4HwpriMin": qosInWlan4HwpriMin,
       "qosOut": qosOut,
       "qosOutDefault": qosOutDefault,
       "qosOutDefaultDefault": qosOutDefaultDefault,
       "qosOutDefaultDefaultLimit": qosOutDefaultDefaultLimit,
       "qosOutDefaultDefaultReserve": qosOutDefaultDefaultReserve,
       "qosOutDefaultEth0": qosOutDefaultEth0,
       "qosOutDefaultEth0Limit": qosOutDefaultEth0Limit,
       "qosOutDefaultEth0Reserve": qosOutDefaultEth0Reserve,
       "qosOutDefaultLimit": qosOutDefaultLimit,
       "qosOutDefaultLocal": qosOutDefaultLocal,
       "qosOutDefaultLocalLimit": qosOutDefaultLocalLimit,
       "qosOutDefaultLocalReserve": qosOutDefaultLocalReserve,
       "qosOutDefaultWlan0": qosOutDefaultWlan0,
       "qosOutDefaultWlan0Limit": qosOutDefaultWlan0Limit,
       "qosOutDefaultWlan0Reserve": qosOutDefaultWlan0Reserve,
       "qosOutDefaultWlan1": qosOutDefaultWlan1,
       "qosOutDefaultWlan1Limit": qosOutDefaultWlan1Limit,
       "qosOutDefaultWlan1Reserve": qosOutDefaultWlan1Reserve,
       "qosOutDefaultWlan2": qosOutDefaultWlan2,
       "qosOutDefaultWlan2Limit": qosOutDefaultWlan2Limit,
       "qosOutDefaultWlan2Reserve": qosOutDefaultWlan2Reserve,
       "qosOutDefaultWlan3": qosOutDefaultWlan3,
       "qosOutDefaultWlan3Limit": qosOutDefaultWlan3Limit,
       "qosOutDefaultWlan3Reserve": qosOutDefaultWlan3Reserve,
       "qosOutDefaultWlan4": qosOutDefaultWlan4,
       "qosOutDefaultWlan4Limit": qosOutDefaultWlan4Limit,
       "qosOutDefaultWlan4Reserve": qosOutDefaultWlan4Reserve,
       "qosOutWlan0": qosOutWlan0,
       "qosOutWlan0Default": qosOutWlan0Default,
       "qosOutWlan0DefaultBe": qosOutWlan0DefaultBe,
       "qosOutWlan0DefaultBeLimit": qosOutWlan0DefaultBeLimit,
       "qosOutWlan0DefaultBeReserve": qosOutWlan0DefaultBeReserve,
       "qosOutWlan0DefaultBk": qosOutWlan0DefaultBk,
       "qosOutWlan0DefaultBkLimit": qosOutWlan0DefaultBkLimit,
       "qosOutWlan0DefaultBkReserve": qosOutWlan0DefaultBkReserve,
       "qosOutWlan0DefaultLimit": qosOutWlan0DefaultLimit,
       "qosOutWlan0DefaultReserve": qosOutWlan0DefaultReserve,
       "qosOutWlan0DefaultVi": qosOutWlan0DefaultVi,
       "qosOutWlan0DefaultViLimit": qosOutWlan0DefaultViLimit,
       "qosOutWlan0DefaultViReserve": qosOutWlan0DefaultViReserve,
       "qosOutWlan0DefaultVo": qosOutWlan0DefaultVo,
       "qosOutWlan0DefaultVoLimit": qosOutWlan0DefaultVoLimit,
       "qosOutWlan0DefaultVoReserve": qosOutWlan0DefaultVoReserve,
       "qosOutWlan0Eth0": qosOutWlan0Eth0,
       "qosOutWlan0Eth0Be": qosOutWlan0Eth0Be,
       "qosOutWlan0Eth0BeLimit": qosOutWlan0Eth0BeLimit,
       "qosOutWlan0Eth0BeReserve": qosOutWlan0Eth0BeReserve,
       "qosOutWlan0Eth0Bk": qosOutWlan0Eth0Bk,
       "qosOutWlan0Eth0BkLimit": qosOutWlan0Eth0BkLimit,
       "qosOutWlan0Eth0BkReserve": qosOutWlan0Eth0BkReserve,
       "qosOutWlan0Eth0Limit": qosOutWlan0Eth0Limit,
       "qosOutWlan0Eth0Reserve": qosOutWlan0Eth0Reserve,
       "qosOutWlan0Eth0Vi": qosOutWlan0Eth0Vi,
       "qosOutWlan0Eth0ViLimit": qosOutWlan0Eth0ViLimit,
       "qosOutWlan0Eth0ViReserve": qosOutWlan0Eth0ViReserve,
       "qosOutWlan0Eth0Vo": qosOutWlan0Eth0Vo,
       "qosOutWlan0Eth0VoLimit": qosOutWlan0Eth0VoLimit,
       "qosOutWlan0Eth0VoReserve": qosOutWlan0Eth0VoReserve,
       "qosOutWlan0Limit": qosOutWlan0Limit,
       "qosOutWlan0Local": qosOutWlan0Local,
       "qosOutWlan0LocalBe": qosOutWlan0LocalBe,
       "qosOutWlan0LocalBeLimit": qosOutWlan0LocalBeLimit,
       "qosOutWlan0LocalBeReserve": qosOutWlan0LocalBeReserve,
       "qosOutWlan0LocalBk": qosOutWlan0LocalBk,
       "qosOutWlan0LocalBkLimit": qosOutWlan0LocalBkLimit,
       "qosOutWlan0LocalBkReserve": qosOutWlan0LocalBkReserve,
       "qosOutWlan0LocalLimit": qosOutWlan0LocalLimit,
       "qosOutWlan0LocalReserve": qosOutWlan0LocalReserve,
       "qosOutWlan0LocalVi": qosOutWlan0LocalVi,
       "qosOutWlan0LocalViLimit": qosOutWlan0LocalViLimit,
       "qosOutWlan0LocalViReserve": qosOutWlan0LocalViReserve,
       "qosOutWlan0LocalVo": qosOutWlan0LocalVo,
       "qosOutWlan0LocalVoLimit": qosOutWlan0LocalVoLimit,
       "qosOutWlan0LocalVoReserve": qosOutWlan0LocalVoReserve,
       "qosOutWlan0Wlan0": qosOutWlan0Wlan0,
       "qosOutWlan0Wlan0Be": qosOutWlan0Wlan0Be,
       "qosOutWlan0Wlan0BeLimit": qosOutWlan0Wlan0BeLimit,
       "qosOutWlan0Wlan0BeReserve": qosOutWlan0Wlan0BeReserve,
       "qosOutWlan0Wlan0Bk": qosOutWlan0Wlan0Bk,
       "qosOutWlan0Wlan0BkLimit": qosOutWlan0Wlan0BkLimit,
       "qosOutWlan0Wlan0BkReserve": qosOutWlan0Wlan0BkReserve,
       "qosOutWlan0Wlan0Limit": qosOutWlan0Wlan0Limit,
       "qosOutWlan0Wlan0Reserve": qosOutWlan0Wlan0Reserve,
       "qosOutWlan0Wlan0Vi": qosOutWlan0Wlan0Vi,
       "qosOutWlan0Wlan0ViLimit": qosOutWlan0Wlan0ViLimit,
       "qosOutWlan0Wlan0ViReserve": qosOutWlan0Wlan0ViReserve,
       "qosOutWlan0Wlan0Vo": qosOutWlan0Wlan0Vo,
       "qosOutWlan0Wlan0VoLimit": qosOutWlan0Wlan0VoLimit,
       "qosOutWlan0Wlan0VoReserve": qosOutWlan0Wlan0VoReserve,
       "qosOutWlan0Wlan1": qosOutWlan0Wlan1,
       "qosOutWlan0Wlan1Be": qosOutWlan0Wlan1Be,
       "qosOutWlan0Wlan1BeLimit": qosOutWlan0Wlan1BeLimit,
       "qosOutWlan0Wlan1BeReserve": qosOutWlan0Wlan1BeReserve,
       "qosOutWlan0Wlan1Bk": qosOutWlan0Wlan1Bk,
       "qosOutWlan0Wlan1BkLimit": qosOutWlan0Wlan1BkLimit,
       "qosOutWlan0Wlan1BkReserve": qosOutWlan0Wlan1BkReserve,
       "qosOutWlan0Wlan1Limit": qosOutWlan0Wlan1Limit,
       "qosOutWlan0Wlan1Reserve": qosOutWlan0Wlan1Reserve,
       "qosOutWlan0Wlan1Vi": qosOutWlan0Wlan1Vi,
       "qosOutWlan0Wlan1ViLimit": qosOutWlan0Wlan1ViLimit,
       "qosOutWlan0Wlan1ViReserve": qosOutWlan0Wlan1ViReserve,
       "qosOutWlan0Wlan1Vo": qosOutWlan0Wlan1Vo,
       "qosOutWlan0Wlan1VoLimit": qosOutWlan0Wlan1VoLimit,
       "qosOutWlan0Wlan1VoReserve": qosOutWlan0Wlan1VoReserve,
       "qosOutWlan0Wlan2": qosOutWlan0Wlan2,
       "qosOutWlan0Wlan2Be": qosOutWlan0Wlan2Be,
       "qosOutWlan0Wlan2BeLimit": qosOutWlan0Wlan2BeLimit,
       "qosOutWlan0Wlan2BeReserve": qosOutWlan0Wlan2BeReserve,
       "qosOutWlan0Wlan2Bk": qosOutWlan0Wlan2Bk,
       "qosOutWlan0Wlan2BkLimit": qosOutWlan0Wlan2BkLimit,
       "qosOutWlan0Wlan2BkReserve": qosOutWlan0Wlan2BkReserve,
       "qosOutWlan0Wlan2Limit": qosOutWlan0Wlan2Limit,
       "qosOutWlan0Wlan2Reserve": qosOutWlan0Wlan2Reserve,
       "qosOutWlan0Wlan2Vi": qosOutWlan0Wlan2Vi,
       "qosOutWlan0Wlan2ViLimit": qosOutWlan0Wlan2ViLimit,
       "qosOutWlan0Wlan2ViReserve": qosOutWlan0Wlan2ViReserve,
       "qosOutWlan0Wlan2Vo": qosOutWlan0Wlan2Vo,
       "qosOutWlan0Wlan2VoLimit": qosOutWlan0Wlan2VoLimit,
       "qosOutWlan0Wlan2VoReserve": qosOutWlan0Wlan2VoReserve,
       "qosOutWlan0Wlan3": qosOutWlan0Wlan3,
       "qosOutWlan0Wlan3Be": qosOutWlan0Wlan3Be,
       "qosOutWlan0Wlan3BeLimit": qosOutWlan0Wlan3BeLimit,
       "qosOutWlan0Wlan3BeReserve": qosOutWlan0Wlan3BeReserve,
       "qosOutWlan0Wlan3Bk": qosOutWlan0Wlan3Bk,
       "qosOutWlan0Wlan3BkLimit": qosOutWlan0Wlan3BkLimit,
       "qosOutWlan0Wlan3BkReserve": qosOutWlan0Wlan3BkReserve,
       "qosOutWlan0Wlan3Limit": qosOutWlan0Wlan3Limit,
       "qosOutWlan0Wlan3Reserve": qosOutWlan0Wlan3Reserve,
       "qosOutWlan0Wlan3Vi": qosOutWlan0Wlan3Vi,
       "qosOutWlan0Wlan3ViLimit": qosOutWlan0Wlan3ViLimit,
       "qosOutWlan0Wlan3ViReserve": qosOutWlan0Wlan3ViReserve,
       "qosOutWlan0Wlan3Vo": qosOutWlan0Wlan3Vo,
       "qosOutWlan0Wlan3VoLimit": qosOutWlan0Wlan3VoLimit,
       "qosOutWlan0Wlan3VoReserve": qosOutWlan0Wlan3VoReserve,
       "qosOutWlan0Wlan4": qosOutWlan0Wlan4,
       "qosOutWlan0Wlan4Be": qosOutWlan0Wlan4Be,
       "qosOutWlan0Wlan4BeLimit": qosOutWlan0Wlan4BeLimit,
       "qosOutWlan0Wlan4BeReserve": qosOutWlan0Wlan4BeReserve,
       "qosOutWlan0Wlan4Bk": qosOutWlan0Wlan4Bk,
       "qosOutWlan0Wlan4BkLimit": qosOutWlan0Wlan4BkLimit,
       "qosOutWlan0Wlan4BkReserve": qosOutWlan0Wlan4BkReserve,
       "qosOutWlan0Wlan4Limit": qosOutWlan0Wlan4Limit,
       "qosOutWlan0Wlan4Reserve": qosOutWlan0Wlan4Reserve,
       "qosOutWlan0Wlan4Vi": qosOutWlan0Wlan4Vi,
       "qosOutWlan0Wlan4ViLimit": qosOutWlan0Wlan4ViLimit,
       "qosOutWlan0Wlan4ViReserve": qosOutWlan0Wlan4ViReserve,
       "qosOutWlan0Wlan4Vo": qosOutWlan0Wlan4Vo,
       "qosOutWlan0Wlan4VoLimit": qosOutWlan0Wlan4VoLimit,
       "qosOutWlan0Wlan4VoReserve": qosOutWlan0Wlan4VoReserve,
       "logs": logs,
       "logsMconfd": logsMconfd,
       "logsMconfdFiles": logsMconfdFiles,
       "logsMconfdSize": logsMconfdSize,
       "logsSecure": logsSecure,
       "logsSecureFiles": logsSecureFiles,
       "logsSecureSize": logsSecureSize,
       "logsSnmp": logsSnmp,
       "logsSnmpFiles": logsSnmpFiles,
       "logsSnmpSize": logsSnmpSize,
       "logsSyslog": logsSyslog,
       "logsSyslogFiles": logsSyslogFiles,
       "logsSyslogSize": logsSyslogSize,
       "eth0": eth0,
       "eth0Acl": eth0Acl,
       "eth0AclMode": eth0AclMode,
       "eth0Dhcp": eth0Dhcp,
       "eth0DhcpAlwaysbroadcast": eth0DhcpAlwaysbroadcast,
       "eth0DhcpDefaultleasetime": eth0DhcpDefaultleasetime,
       "eth0DhcpMaxleasetime": eth0DhcpMaxleasetime,
       "eth0DhcpRelay": eth0DhcpRelay,
       "eth0DhcpRelayEnable": eth0DhcpRelayEnable,
       "eth0DhcpReserve": eth0DhcpReserve,
       "eth0DhcpRole": eth0DhcpRole,
       "eth0Enable": eth0Enable,
       "eth0If": eth0If,
       "eth0Ip": eth0Ip,
       "eth0IpAddress": eth0IpAddress,
       "eth0IpAddressforce": eth0IpAddressforce,
       "eth0IpBroadcast": eth0IpBroadcast,
       "eth0IpBroadcastforce": eth0IpBroadcastforce,
       "eth0IpGateway": eth0IpGateway,
       "eth0IpGatewayforce": eth0IpGatewayforce,
       "eth0IpImplicit": eth0IpImplicit,
       "eth0IpImplicitSize": eth0IpImplicitSize,
       "eth0IpImplicitSizeActual": eth0IpImplicitSizeActual,
       "eth0IpImplicitSizeRequested": eth0IpImplicitSizeRequested,
       "eth0IpImplicitStart": eth0IpImplicitStart,
       "eth0IpImplicitStartActual": eth0IpImplicitStartActual,
       "eth0IpImplicitStartRequested": eth0IpImplicitStartRequested,
       "eth0IpNetmask": eth0IpNetmask,
       "eth0IpNetmaskforce": eth0IpNetmaskforce,
       "eth0Role": eth0Role,
       "eth0Routes": eth0Routes,
       "eth0RoutesStatic": eth0RoutesStatic,
       "eth0Vlan": eth0Vlan,
       "eth0VlanEnable": eth0VlanEnable,
       "eth0VlanId": eth0VlanId,
       "eth0Vpn": eth0Vpn,
       "eth0VpnDevice": eth0VpnDevice,
       "eth0VpnEnable": eth0VpnEnable,
       "eth0VpnKeyfile": eth0VpnKeyfile,
       "eth0VpnPort": eth0VpnPort,
       "eth0VpnProtocol": eth0VpnProtocol,
       "eth0VpnServer": eth0VpnServer,
       "br0": br0,
       "br0Acl": br0Acl,
       "br0AclMode": br0AclMode,
       "br0Dhcp": br0Dhcp,
       "br0DhcpAlwaysbroadcast": br0DhcpAlwaysbroadcast,
       "br0DhcpDefaultleasetime": br0DhcpDefaultleasetime,
       "br0DhcpMaxleasetime": br0DhcpMaxleasetime,
       "br0DhcpRelay": br0DhcpRelay,
       "br0DhcpRelayEnable": br0DhcpRelayEnable,
       "br0DhcpReserve": br0DhcpReserve,
       "br0DhcpRole": br0DhcpRole,
       "br0Enable": br0Enable,
       "br0Forwardingdelay": br0Forwardingdelay,
       "br0If": br0If,
       "br0Ip": br0Ip,
       "br0IpAddress": br0IpAddress,
       "br0IpAddressforce": br0IpAddressforce,
       "br0IpBroadcast": br0IpBroadcast,
       "br0IpBroadcastforce": br0IpBroadcastforce,
       "br0IpGateway": br0IpGateway,
       "br0IpGatewayforce": br0IpGatewayforce,
       "br0IpNetmask": br0IpNetmask,
       "br0IpNetmaskforce": br0IpNetmaskforce,
       "br0Role": br0Role,
       "br0Routes": br0Routes,
       "br0RoutesStatic": br0RoutesStatic,
       "br0Stp": br0Stp,
       "br0StpEnable": br0StpEnable,
       "alias99": alias99,
       "alias99If": alias99If,
       "alias99Ip": alias99Ip,
       "alias99IpAddress": alias99IpAddress,
       "alias99IpBroadcast": alias99IpBroadcast,
       "alias99IpGateway": alias99IpGateway,
       "alias99IpNetmask": alias99IpNetmask,
       "radio0": radio0,
       "radio0Channel": radio0Channel,
       "radio0Chansize": radio0Chansize,
       "radio0Distance": radio0Distance,
       "radio0Distancemeters": radio0Distancemeters,
       "radio0Frequency": radio0Frequency,
       "radio0Mode": radio0Mode,
       "radio0Modes": radio0Modes,
       "radio0Pureg": radio0Pureg,
       "radio0Ratectl": radio0Ratectl,
       "radio0Rts": radio0Rts,
       "radio0Shortpreamble": radio0Shortpreamble,
       "radio0Turbo": radio0Turbo,
       "radio0Txpower": radio0Txpower,
       "radio0Wlans": radio0Wlans,
       "radio0Wlansextra": radio0Wlansextra,
       "radio1": radio1,
       "radio1Channel": radio1Channel,
       "radio1Chansize": radio1Chansize,
       "radio1Distance": radio1Distance,
       "radio1Distancemeters": radio1Distancemeters,
       "radio1Frequency": radio1Frequency,
       "radio1Mode": radio1Mode,
       "radio1Modes": radio1Modes,
       "radio1Pureg": radio1Pureg,
       "radio1Ratectl": radio1Ratectl,
       "radio1Rts": radio1Rts,
       "radio1Shortpreamble": radio1Shortpreamble,
       "radio1Turbo": radio1Turbo,
       "radio1Txpower": radio1Txpower,
       "radio1Wlans": radio1Wlans,
       "radio1Wlansextra": radio1Wlansextra,
       "wlan0": wlan0,
       "wlan0Acl": wlan0Acl,
       "wlan0AclMode": wlan0AclMode,
       "wlan0Beaconinterval": wlan0Beaconinterval,
       "wlan0Cellid": wlan0Cellid,
       "wlan0Dhcp": wlan0Dhcp,
       "wlan0DhcpAlwaysbroadcast": wlan0DhcpAlwaysbroadcast,
       "wlan0DhcpDefaultleasetime": wlan0DhcpDefaultleasetime,
       "wlan0DhcpMaxleasetime": wlan0DhcpMaxleasetime,
       "wlan0DhcpRelay": wlan0DhcpRelay,
       "wlan0DhcpRelayEnable": wlan0DhcpRelayEnable,
       "wlan0DhcpReserve": wlan0DhcpReserve,
       "wlan0DhcpRole": wlan0DhcpRole,
       "wlan0Enable": wlan0Enable,
       "wlan0Enhsec": wlan0Enhsec,
       "wlan0Essid": wlan0Essid,
       "wlan0Fabric": wlan0Fabric,
       "wlan0FabricArgs": wlan0FabricArgs,
       "wlan0FabricBridge": wlan0FabricBridge,
       "wlan0FabricCmd1": wlan0FabricCmd1,
       "wlan0FabricCmd2": wlan0FabricCmd2,
       "wlan0FabricEnable": wlan0FabricEnable,
       "wlan0FabricGateway": wlan0FabricGateway,
       "wlan0FabricGatewayEnable": wlan0FabricGatewayEnable,
       "wlan0FabricGatewayIf": wlan0FabricGatewayIf,
       "wlan0FabricMargin": wlan0FabricMargin,
       "wlan0FabricRouteadvert": wlan0FabricRouteadvert,
       "wlan0FabricRssi": wlan0FabricRssi,
       "wlan0FabricRssiJoin": wlan0FabricRssiJoin,
       "wlan0FabricRssiMargin": wlan0FabricRssiMargin,
       "wlan0Frag": wlan0Frag,
       "wlan0Hideessid": wlan0Hideessid,
       "wlan0If": wlan0If,
       "wlan0Ip": wlan0Ip,
       "wlan0IpAddress": wlan0IpAddress,
       "wlan0IpAddressforce": wlan0IpAddressforce,
       "wlan0IpBroadcast": wlan0IpBroadcast,
       "wlan0IpBroadcastforce": wlan0IpBroadcastforce,
       "wlan0IpGateway": wlan0IpGateway,
       "wlan0IpGatewayforce": wlan0IpGatewayforce,
       "wlan0IpNetmask": wlan0IpNetmask,
       "wlan0IpNetmaskforce": wlan0IpNetmaskforce,
       "wlan0Iwconfig": wlan0Iwconfig,
       "wlan0IwconfigCmd": wlan0IwconfigCmd,
       "wlan0Iwpriv": wlan0Iwpriv,
       "wlan0IwprivCmd": wlan0IwprivCmd,
       "wlan0Key": wlan0Key,
       "wlan0Keys": wlan0Keys,
       "wlan0Keys1": wlan0Keys1,
       "wlan0Keys2": wlan0Keys2,
       "wlan0Keys3": wlan0Keys3,
       "wlan0Keys4": wlan0Keys4,
       "wlan0KeysDefault": wlan0KeysDefault,
       "wlan0Mconfd": wlan0Mconfd,
       "wlan0MconfdEnable": wlan0MconfdEnable,
       "wlan0MconfdExternalhosts": wlan0MconfdExternalhosts,
       "wlan0Mode": wlan0Mode,
       "wlan0Mroute": wlan0Mroute,
       "wlan0MrouteArgs": wlan0MrouteArgs,
       "wlan0MrouteCmd": wlan0MrouteCmd,
       "wlan0MrouteEnable": wlan0MrouteEnable,
       "wlan0Mtu": wlan0Mtu,
       "wlan0Radio": wlan0Radio,
       "wlan0Rate": wlan0Rate,
       "wlan0Role": wlan0Role,
       "wlan0Routes": wlan0Routes,
       "wlan0RoutesAddprivnets": wlan0RoutesAddprivnets,
       "wlan0RoutesStatic": wlan0RoutesStatic,
       "wlan0Topomc": wlan0Topomc,
       "wlan0TopomcArgs": wlan0TopomcArgs,
       "wlan0TopomcCmd": wlan0TopomcCmd,
       "wlan0TopomcEnable": wlan0TopomcEnable,
       "wlan1": wlan1,
       "wlan1Acl": wlan1Acl,
       "wlan1AclMode": wlan1AclMode,
       "wlan1Beaconinterval": wlan1Beaconinterval,
       "wlan1Cellid": wlan1Cellid,
       "wlan1Dhcp": wlan1Dhcp,
       "wlan1DhcpAlwaysbroadcast": wlan1DhcpAlwaysbroadcast,
       "wlan1DhcpDefaultleasetime": wlan1DhcpDefaultleasetime,
       "wlan1DhcpMaxleasetime": wlan1DhcpMaxleasetime,
       "wlan1DhcpRelay": wlan1DhcpRelay,
       "wlan1DhcpRelayEnable": wlan1DhcpRelayEnable,
       "wlan1DhcpReserve": wlan1DhcpReserve,
       "wlan1DhcpRole": wlan1DhcpRole,
       "wlan1Enable": wlan1Enable,
       "wlan1Enhsec": wlan1Enhsec,
       "wlan1Essid": wlan1Essid,
       "wlan1Frag": wlan1Frag,
       "wlan1Hideessid": wlan1Hideessid,
       "wlan1If": wlan1If,
       "wlan1Ip": wlan1Ip,
       "wlan1IpAddress": wlan1IpAddress,
       "wlan1IpAddressforce": wlan1IpAddressforce,
       "wlan1IpBroadcast": wlan1IpBroadcast,
       "wlan1IpBroadcastforce": wlan1IpBroadcastforce,
       "wlan1IpGateway": wlan1IpGateway,
       "wlan1IpGatewayforce": wlan1IpGatewayforce,
       "wlan1IpImplicit": wlan1IpImplicit,
       "wlan1IpImplicitSize": wlan1IpImplicitSize,
       "wlan1IpImplicitSizeActual": wlan1IpImplicitSizeActual,
       "wlan1IpImplicitSizeRequested": wlan1IpImplicitSizeRequested,
       "wlan1IpImplicitStart": wlan1IpImplicitStart,
       "wlan1IpImplicitStartActual": wlan1IpImplicitStartActual,
       "wlan1IpImplicitStartRequested": wlan1IpImplicitStartRequested,
       "wlan1IpNetmask": wlan1IpNetmask,
       "wlan1IpNetmaskforce": wlan1IpNetmaskforce,
       "wlan1Iwconfig": wlan1Iwconfig,
       "wlan1IwconfigCmd": wlan1IwconfigCmd,
       "wlan1Iwpriv": wlan1Iwpriv,
       "wlan1IwprivCmd": wlan1IwprivCmd,
       "wlan1Key": wlan1Key,
       "wlan1Keys": wlan1Keys,
       "wlan1Keys1": wlan1Keys1,
       "wlan1Keys2": wlan1Keys2,
       "wlan1Keys3": wlan1Keys3,
       "wlan1Keys4": wlan1Keys4,
       "wlan1KeysDefault": wlan1KeysDefault,
       "wlan1Mode": wlan1Mode,
       "wlan1Mtu": wlan1Mtu,
       "wlan1Radio": wlan1Radio,
       "wlan1Rate": wlan1Rate,
       "wlan1Role": wlan1Role,
       "wlan1Routes": wlan1Routes,
       "wlan1RoutesStatic": wlan1RoutesStatic,
       "wlan1Vlan": wlan1Vlan,
       "wlan1VlanEnable": wlan1VlanEnable,
       "wlan1VlanId": wlan1VlanId,
       "wlan1Wpa": wlan1Wpa,
       "wlan1WpaAuth": wlan1WpaAuth,
       "wlan1WpaAuthArgs": wlan1WpaAuthArgs,
       "wlan1WpaAuthCustom": wlan1WpaAuthCustom,
       "wlan1WpaAuthInternal": wlan1WpaAuthInternal,
       "wlan1WpaAuthServer": wlan1WpaAuthServer,
       "wlan1WpaAuthServerAddr": wlan1WpaAuthServerAddr,
       "wlan1WpaAuthServerPort": wlan1WpaAuthServerPort,
       "wlan1WpaAuthServerSharedsecret": wlan1WpaAuthServerSharedsecret,
       "wlan1WpaAuthType": wlan1WpaAuthType,
       "wlan1WpaBridge": wlan1WpaBridge,
       "wlan1WpaCa": wlan1WpaCa,
       "wlan1WpaCaCert": wlan1WpaCaCert,
       "wlan1WpaCaCertFile": wlan1WpaCaCertFile,
       "wlan1WpaEapol": wlan1WpaEapol,
       "wlan1WpaEapolVersion": wlan1WpaEapolVersion,
       "wlan1WpaEnable": wlan1WpaEnable,
       "wlan1WpaEssid": wlan1WpaEssid,
       "wlan1WpaIf": wlan1WpaIf,
       "wlan1WpaKeymgmt": wlan1WpaKeymgmt,
       "wlan1WpaMode": wlan1WpaMode,
       "wlan1WpaNode": wlan1WpaNode,
       "wlan1WpaNodeCert": wlan1WpaNodeCert,
       "wlan1WpaNodeCertFile": wlan1WpaNodeCertFile,
       "wlan1WpaNodeKey": wlan1WpaNodeKey,
       "wlan1WpaNodeKeyFile": wlan1WpaNodeKeyFile,
       "wlan1WpaNodeKeyPassphrase": wlan1WpaNodeKeyPassphrase,
       "wlan1WpaPairwise": wlan1WpaPairwise,
       "wlan1WpaPassphrase": wlan1WpaPassphrase,
       "wlan2": wlan2,
       "wlan2Acl": wlan2Acl,
       "wlan2AclMode": wlan2AclMode,
       "wlan2Beaconinterval": wlan2Beaconinterval,
       "wlan2Cellid": wlan2Cellid,
       "wlan2Dhcp": wlan2Dhcp,
       "wlan2DhcpAlwaysbroadcast": wlan2DhcpAlwaysbroadcast,
       "wlan2DhcpDefaultleasetime": wlan2DhcpDefaultleasetime,
       "wlan2DhcpMaxleasetime": wlan2DhcpMaxleasetime,
       "wlan2DhcpRelay": wlan2DhcpRelay,
       "wlan2DhcpRelayEnable": wlan2DhcpRelayEnable,
       "wlan2DhcpReserve": wlan2DhcpReserve,
       "wlan2DhcpRole": wlan2DhcpRole,
       "wlan2Enable": wlan2Enable,
       "wlan2Enhsec": wlan2Enhsec,
       "wlan2Essid": wlan2Essid,
       "wlan2Frag": wlan2Frag,
       "wlan2Hideessid": wlan2Hideessid,
       "wlan2If": wlan2If,
       "wlan2Ip": wlan2Ip,
       "wlan2IpAddress": wlan2IpAddress,
       "wlan2IpAddressforce": wlan2IpAddressforce,
       "wlan2IpBroadcast": wlan2IpBroadcast,
       "wlan2IpBroadcastforce": wlan2IpBroadcastforce,
       "wlan2IpGateway": wlan2IpGateway,
       "wlan2IpGatewayforce": wlan2IpGatewayforce,
       "wlan2IpImplicit": wlan2IpImplicit,
       "wlan2IpImplicitSize": wlan2IpImplicitSize,
       "wlan2IpImplicitSizeActual": wlan2IpImplicitSizeActual,
       "wlan2IpImplicitSizeRequested": wlan2IpImplicitSizeRequested,
       "wlan2IpImplicitStart": wlan2IpImplicitStart,
       "wlan2IpImplicitStartActual": wlan2IpImplicitStartActual,
       "wlan2IpImplicitStartRequested": wlan2IpImplicitStartRequested,
       "wlan2IpNetmask": wlan2IpNetmask,
       "wlan2IpNetmaskforce": wlan2IpNetmaskforce,
       "wlan2Iwconfig": wlan2Iwconfig,
       "wlan2IwconfigCmd": wlan2IwconfigCmd,
       "wlan2Iwpriv": wlan2Iwpriv,
       "wlan2IwprivCmd": wlan2IwprivCmd,
       "wlan2Key": wlan2Key,
       "wlan2Keys": wlan2Keys,
       "wlan2Keys1": wlan2Keys1,
       "wlan2Keys2": wlan2Keys2,
       "wlan2Keys3": wlan2Keys3,
       "wlan2Keys4": wlan2Keys4,
       "wlan2KeysDefault": wlan2KeysDefault,
       "wlan2Mode": wlan2Mode,
       "wlan2Mtu": wlan2Mtu,
       "wlan2Radio": wlan2Radio,
       "wlan2Rate": wlan2Rate,
       "wlan2Role": wlan2Role,
       "wlan2Routes": wlan2Routes,
       "wlan2RoutesStatic": wlan2RoutesStatic,
       "wlan2Vlan": wlan2Vlan,
       "wlan2VlanEnable": wlan2VlanEnable,
       "wlan2VlanId": wlan2VlanId,
       "wlan2Wpa": wlan2Wpa,
       "wlan2WpaAuth": wlan2WpaAuth,
       "wlan2WpaAuthArgs": wlan2WpaAuthArgs,
       "wlan2WpaAuthCustom": wlan2WpaAuthCustom,
       "wlan2WpaAuthInternal": wlan2WpaAuthInternal,
       "wlan2WpaAuthServer": wlan2WpaAuthServer,
       "wlan2WpaAuthServerAddr": wlan2WpaAuthServerAddr,
       "wlan2WpaAuthServerPort": wlan2WpaAuthServerPort,
       "wlan2WpaAuthServerSharedsecret": wlan2WpaAuthServerSharedsecret,
       "wlan2WpaAuthType": wlan2WpaAuthType,
       "wlan2WpaBridge": wlan2WpaBridge,
       "wlan2WpaCa": wlan2WpaCa,
       "wlan2WpaCaCert": wlan2WpaCaCert,
       "wlan2WpaCaCertFile": wlan2WpaCaCertFile,
       "wlan2WpaEapol": wlan2WpaEapol,
       "wlan2WpaEapolVersion": wlan2WpaEapolVersion,
       "wlan2WpaEnable": wlan2WpaEnable,
       "wlan2WpaEssid": wlan2WpaEssid,
       "wlan2WpaIf": wlan2WpaIf,
       "wlan2WpaKeymgmt": wlan2WpaKeymgmt,
       "wlan2WpaMode": wlan2WpaMode,
       "wlan2WpaNode": wlan2WpaNode,
       "wlan2WpaNodeCert": wlan2WpaNodeCert,
       "wlan2WpaNodeCertFile": wlan2WpaNodeCertFile,
       "wlan2WpaNodeKey": wlan2WpaNodeKey,
       "wlan2WpaNodeKeyFile": wlan2WpaNodeKeyFile,
       "wlan2WpaNodeKeyPassphrase": wlan2WpaNodeKeyPassphrase,
       "wlan2WpaPairwise": wlan2WpaPairwise,
       "wlan2WpaPassphrase": wlan2WpaPassphrase,
       "wlan3": wlan3,
       "wlan3Acl": wlan3Acl,
       "wlan3AclMode": wlan3AclMode,
       "wlan3Beaconinterval": wlan3Beaconinterval,
       "wlan3Cellid": wlan3Cellid,
       "wlan3Dhcp": wlan3Dhcp,
       "wlan3DhcpAlwaysbroadcast": wlan3DhcpAlwaysbroadcast,
       "wlan3DhcpDefaultleasetime": wlan3DhcpDefaultleasetime,
       "wlan3DhcpMaxleasetime": wlan3DhcpMaxleasetime,
       "wlan3DhcpRelay": wlan3DhcpRelay,
       "wlan3DhcpRelayEnable": wlan3DhcpRelayEnable,
       "wlan3DhcpReserve": wlan3DhcpReserve,
       "wlan3DhcpRole": wlan3DhcpRole,
       "wlan3Enable": wlan3Enable,
       "wlan3Enhsec": wlan3Enhsec,
       "wlan3Essid": wlan3Essid,
       "wlan3Frag": wlan3Frag,
       "wlan3Hideessid": wlan3Hideessid,
       "wlan3If": wlan3If,
       "wlan3Ip": wlan3Ip,
       "wlan3IpAddress": wlan3IpAddress,
       "wlan3IpAddressforce": wlan3IpAddressforce,
       "wlan3IpBroadcast": wlan3IpBroadcast,
       "wlan3IpBroadcastforce": wlan3IpBroadcastforce,
       "wlan3IpGateway": wlan3IpGateway,
       "wlan3IpGatewayforce": wlan3IpGatewayforce,
       "wlan3IpImplicit": wlan3IpImplicit,
       "wlan3IpImplicitSize": wlan3IpImplicitSize,
       "wlan3IpImplicitSizeActual": wlan3IpImplicitSizeActual,
       "wlan3IpImplicitSizeRequested": wlan3IpImplicitSizeRequested,
       "wlan3IpImplicitStart": wlan3IpImplicitStart,
       "wlan3IpImplicitStartActual": wlan3IpImplicitStartActual,
       "wlan3IpImplicitStartRequested": wlan3IpImplicitStartRequested,
       "wlan3IpNetmask": wlan3IpNetmask,
       "wlan3IpNetmaskforce": wlan3IpNetmaskforce,
       "wlan3Iwconfig": wlan3Iwconfig,
       "wlan3IwconfigCmd": wlan3IwconfigCmd,
       "wlan3Iwpriv": wlan3Iwpriv,
       "wlan3IwprivCmd": wlan3IwprivCmd,
       "wlan3Key": wlan3Key,
       "wlan3Keys": wlan3Keys,
       "wlan3Keys1": wlan3Keys1,
       "wlan3Keys2": wlan3Keys2,
       "wlan3Keys3": wlan3Keys3,
       "wlan3Keys4": wlan3Keys4,
       "wlan3KeysDefault": wlan3KeysDefault,
       "wlan3Mode": wlan3Mode,
       "wlan3Mtu": wlan3Mtu,
       "wlan3Radio": wlan3Radio,
       "wlan3Rate": wlan3Rate,
       "wlan3Role": wlan3Role,
       "wlan3Routes": wlan3Routes,
       "wlan3RoutesStatic": wlan3RoutesStatic,
       "wlan3Vlan": wlan3Vlan,
       "wlan3VlanEnable": wlan3VlanEnable,
       "wlan3VlanId": wlan3VlanId,
       "wlan3Wpa": wlan3Wpa,
       "wlan3WpaAuth": wlan3WpaAuth,
       "wlan3WpaAuthArgs": wlan3WpaAuthArgs,
       "wlan3WpaAuthCustom": wlan3WpaAuthCustom,
       "wlan3WpaAuthInternal": wlan3WpaAuthInternal,
       "wlan3WpaAuthServer": wlan3WpaAuthServer,
       "wlan3WpaAuthServerAddr": wlan3WpaAuthServerAddr,
       "wlan3WpaAuthServerPort": wlan3WpaAuthServerPort,
       "wlan3WpaAuthServerSharedsecret": wlan3WpaAuthServerSharedsecret,
       "wlan3WpaAuthType": wlan3WpaAuthType,
       "wlan3WpaBridge": wlan3WpaBridge,
       "wlan3WpaCa": wlan3WpaCa,
       "wlan3WpaCaCert": wlan3WpaCaCert,
       "wlan3WpaCaCertFile": wlan3WpaCaCertFile,
       "wlan3WpaEapol": wlan3WpaEapol,
       "wlan3WpaEapolVersion": wlan3WpaEapolVersion,
       "wlan3WpaEnable": wlan3WpaEnable,
       "wlan3WpaEssid": wlan3WpaEssid,
       "wlan3WpaIf": wlan3WpaIf,
       "wlan3WpaKeymgmt": wlan3WpaKeymgmt,
       "wlan3WpaMode": wlan3WpaMode,
       "wlan3WpaNode": wlan3WpaNode,
       "wlan3WpaNodeCert": wlan3WpaNodeCert,
       "wlan3WpaNodeCertFile": wlan3WpaNodeCertFile,
       "wlan3WpaNodeKey": wlan3WpaNodeKey,
       "wlan3WpaNodeKeyFile": wlan3WpaNodeKeyFile,
       "wlan3WpaNodeKeyPassphrase": wlan3WpaNodeKeyPassphrase,
       "wlan3WpaPairwise": wlan3WpaPairwise,
       "wlan3WpaPassphrase": wlan3WpaPassphrase,
       "wlan4": wlan4,
       "wlan4Acl": wlan4Acl,
       "wlan4AclMode": wlan4AclMode,
       "wlan4Beaconinterval": wlan4Beaconinterval,
       "wlan4Cellid": wlan4Cellid,
       "wlan4Dhcp": wlan4Dhcp,
       "wlan4DhcpAlwaysbroadcast": wlan4DhcpAlwaysbroadcast,
       "wlan4DhcpDefaultleasetime": wlan4DhcpDefaultleasetime,
       "wlan4DhcpMaxleasetime": wlan4DhcpMaxleasetime,
       "wlan4DhcpRelay": wlan4DhcpRelay,
       "wlan4DhcpRelayEnable": wlan4DhcpRelayEnable,
       "wlan4DhcpReserve": wlan4DhcpReserve,
       "wlan4DhcpRole": wlan4DhcpRole,
       "wlan4Enable": wlan4Enable,
       "wlan4Enhsec": wlan4Enhsec,
       "wlan4Essid": wlan4Essid,
       "wlan4Frag": wlan4Frag,
       "wlan4Hideessid": wlan4Hideessid,
       "wlan4If": wlan4If,
       "wlan4Ip": wlan4Ip,
       "wlan4IpAddress": wlan4IpAddress,
       "wlan4IpAddressforce": wlan4IpAddressforce,
       "wlan4IpBroadcast": wlan4IpBroadcast,
       "wlan4IpBroadcastforce": wlan4IpBroadcastforce,
       "wlan4IpGateway": wlan4IpGateway,
       "wlan4IpGatewayforce": wlan4IpGatewayforce,
       "wlan4IpImplicit": wlan4IpImplicit,
       "wlan4IpImplicitSize": wlan4IpImplicitSize,
       "wlan4IpImplicitSizeActual": wlan4IpImplicitSizeActual,
       "wlan4IpImplicitSizeRequested": wlan4IpImplicitSizeRequested,
       "wlan4IpImplicitStart": wlan4IpImplicitStart,
       "wlan4IpImplicitStartActual": wlan4IpImplicitStartActual,
       "wlan4IpImplicitStartRequested": wlan4IpImplicitStartRequested,
       "wlan4IpNetmask": wlan4IpNetmask,
       "wlan4IpNetmaskforce": wlan4IpNetmaskforce,
       "wlan4Iwconfig": wlan4Iwconfig,
       "wlan4IwconfigCmd": wlan4IwconfigCmd,
       "wlan4Iwpriv": wlan4Iwpriv,
       "wlan4IwprivCmd": wlan4IwprivCmd,
       "wlan4Key": wlan4Key,
       "wlan4Keys": wlan4Keys,
       "wlan4Keys1": wlan4Keys1,
       "wlan4Keys2": wlan4Keys2,
       "wlan4Keys3": wlan4Keys3,
       "wlan4Keys4": wlan4Keys4,
       "wlan4KeysDefault": wlan4KeysDefault,
       "wlan4Mode": wlan4Mode,
       "wlan4Mtu": wlan4Mtu,
       "wlan4Radio": wlan4Radio,
       "wlan4Rate": wlan4Rate,
       "wlan4Role": wlan4Role,
       "wlan4Routes": wlan4Routes,
       "wlan4RoutesStatic": wlan4RoutesStatic,
       "wlan4Vlan": wlan4Vlan,
       "wlan4VlanEnable": wlan4VlanEnable,
       "wlan4VlanId": wlan4VlanId,
       "wlan4Wpa": wlan4Wpa,
       "wlan4WpaAuth": wlan4WpaAuth,
       "wlan4WpaAuthArgs": wlan4WpaAuthArgs,
       "wlan4WpaAuthCustom": wlan4WpaAuthCustom,
       "wlan4WpaAuthInternal": wlan4WpaAuthInternal,
       "wlan4WpaAuthServer": wlan4WpaAuthServer,
       "wlan4WpaAuthServerAddr": wlan4WpaAuthServerAddr,
       "wlan4WpaAuthServerPort": wlan4WpaAuthServerPort,
       "wlan4WpaAuthServerSharedsecret": wlan4WpaAuthServerSharedsecret,
       "wlan4WpaAuthType": wlan4WpaAuthType,
       "wlan4WpaBridge": wlan4WpaBridge,
       "wlan4WpaCa": wlan4WpaCa,
       "wlan4WpaCaCert": wlan4WpaCaCert,
       "wlan4WpaCaCertFile": wlan4WpaCaCertFile,
       "wlan4WpaEapol": wlan4WpaEapol,
       "wlan4WpaEapolVersion": wlan4WpaEapolVersion,
       "wlan4WpaEnable": wlan4WpaEnable,
       "wlan4WpaEssid": wlan4WpaEssid,
       "wlan4WpaIf": wlan4WpaIf,
       "wlan4WpaKeymgmt": wlan4WpaKeymgmt,
       "wlan4WpaMode": wlan4WpaMode,
       "wlan4WpaNode": wlan4WpaNode,
       "wlan4WpaNodeCert": wlan4WpaNodeCert,
       "wlan4WpaNodeCertFile": wlan4WpaNodeCertFile,
       "wlan4WpaNodeKey": wlan4WpaNodeKey,
       "wlan4WpaNodeKeyFile": wlan4WpaNodeKeyFile,
       "wlan4WpaNodeKeyPassphrase": wlan4WpaNodeKeyPassphrase,
       "wlan4WpaPairwise": wlan4WpaPairwise,
       "wlan4WpaPassphrase": wlan4WpaPassphrase,
       "enRouteTraps": enRouteTraps,
       "enRouteConfigChange": enRouteConfigChange,
       "enRouteConfigReset": enRouteConfigReset}
)
