# SNMP MIB module (NOKIA-OID-REGISTRATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOKIA-OID-REGISTRATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:31 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nokia_ObjectIdentity = ObjectIdentity
nokia = _Nokia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94)
)
_NokiaProducts_ObjectIdentity = ObjectIdentity
nokiaProducts = _NokiaProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1)
)
_LocalBridge_ObjectIdentity = ObjectIdentity
localBridge = _LocalBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 1)
)
_RemoteBridge_ObjectIdentity = ObjectIdentity
remoteBridge = _RemoteBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 2)
)
_FrameRelayBridge_ObjectIdentity = ObjectIdentity
frameRelayBridge = _FrameRelayBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 3)
)
_FrameRelayBrouter_ObjectIdentity = ObjectIdentity
frameRelayBrouter = _FrameRelayBrouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 4)
)
_HubFamily_ObjectIdentity = ObjectIdentity
hubFamily = _HubFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 5)
)
_LanGateway_ObjectIdentity = ObjectIdentity
lanGateway = _LanGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 6)
)
_LocalBrouter_ObjectIdentity = ObjectIdentity
localBrouter = _LocalBrouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 7)
)
_AccessManager_ObjectIdentity = ObjectIdentity
accessManager = _AccessManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 8)
)
_NmsProxy_ObjectIdentity = ObjectIdentity
nmsProxy = _NmsProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 9)
)
_DynaModemMIB_ObjectIdentity = ObjectIdentity
dynaModemMIB = _DynaModemMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 11)
)
_Nawe_ObjectIdentity = ObjectIdentity
nawe = _Nawe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 12)
)
_StTropez_ObjectIdentity = ObjectIdentity
stTropez = _StTropez_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 13)
)
_Nms300_ObjectIdentity = ObjectIdentity
nms300 = _Nms300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 14)
)
_Ian_ObjectIdentity = ObjectIdentity
ian = _Ian_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 15)
)
_NtcCommon_ObjectIdentity = ObjectIdentity
ntcCommon = _NtcCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16)
)
_Ntm10_ObjectIdentity = ObjectIdentity
ntm10 = _Ntm10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 17)
)
_EtIfRel1_ObjectIdentity = ObjectIdentity
etIfRel1 = _EtIfRel1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 18)
)
_EtIfRel2_ObjectIdentity = ObjectIdentity
etIfRel2 = _EtIfRel2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 19)
)
_AtmVoiceDataMux_ObjectIdentity = ObjectIdentity
atmVoiceDataMux = _AtmVoiceDataMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 20)
)
_IpsoProducts_ObjectIdentity = ObjectIdentity
ipsoProducts = _IpsoProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21)
)
_Bban_ObjectIdentity = ObjectIdentity
bban = _Bban_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 22)
)
_Namp_ObjectIdentity = ObjectIdentity
namp = _Namp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 23)
)
_Ggsn_ObjectIdentity = ObjectIdentity
ggsn = _Ggsn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 24)
)
_Nms10_ObjectIdentity = ObjectIdentity
nms10 = _Nms10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 25)
)
_WirelessAccessPoint_ObjectIdentity = ObjectIdentity
wirelessAccessPoint = _WirelessAccessPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 26)
)
_WirelessLANclient_ObjectIdentity = ObjectIdentity
wirelessLANclient = _WirelessLANclient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 27)
)
_Els_ObjectIdentity = ObjectIdentity
els = _Els_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 28)
)
_AccessServer_ObjectIdentity = ObjectIdentity
accessServer = _AccessServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 29)
)
_Cg_ObjectIdentity = ObjectIdentity
cg = _Cg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 30)
)
_Sgsn_ObjectIdentity = ObjectIdentity
sgsn = _Sgsn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 31)
)
_Azc_ObjectIdentity = ObjectIdentity
azc = _Azc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 32)
)
_WapServer_ObjectIdentity = ObjectIdentity
wapServer = _WapServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 33)
)
_S30_ObjectIdentity = ObjectIdentity
s30 = _S30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 34)
)
_IpTelephony_ObjectIdentity = ObjectIdentity
ipTelephony = _IpTelephony_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 35)
)
_Max_ObjectIdentity = ObjectIdentity
max = _Max_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 36)
)
_Twiss_ObjectIdentity = ObjectIdentity
twiss = _Twiss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 37)
)
_NokiaRFCExtensions_ObjectIdentity = ObjectIdentity
nokiaRFCExtensions = _NokiaRFCExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 38)
)
_Ost_ObjectIdentity = ObjectIdentity
ost = _Ost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 39)
)
_Nsg_ObjectIdentity = ObjectIdentity
nsg = _Nsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 40)
)
_NokiaVPN_ObjectIdentity = ObjectIdentity
nokiaVPN = _NokiaVPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41)
)
_Mmsc_ObjectIdentity = ObjectIdentity
mmsc = _Mmsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 42)
)
_NokiaLoopmaster_ObjectIdentity = ObjectIdentity
nokiaLoopmaster = _NokiaLoopmaster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 43)
)
_NokiaSSL_ObjectIdentity = ObjectIdentity
nokiaSSL = _NokiaSSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 44)
)
_NokiaAlchemyOS_ObjectIdentity = ObjectIdentity
nokiaAlchemyOS = _NokiaAlchemyOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 45)
)
_Nals_ObjectIdentity = ObjectIdentity
nals = _Nals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 46)
)
_IpTrunk_ObjectIdentity = ObjectIdentity
ipTrunk = _IpTrunk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 47)
)
_Nawg_ObjectIdentity = ObjectIdentity
nawg = _Nawg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 48)
)
_NokiaPKI_ObjectIdentity = ObjectIdentity
nokiaPKI = _NokiaPKI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 49)
)
_Asg_ObjectIdentity = ObjectIdentity
asg = _Asg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 50)
)
_Nap_ObjectIdentity = ObjectIdentity
nap = _Nap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 51)
)
_MPlatform_ObjectIdentity = ObjectIdentity
mPlatform = _MPlatform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 52)
)
_NetAct4BB_ObjectIdentity = ObjectIdentity
netAct4BB = _NetAct4BB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 53)
)
_Nwr_ObjectIdentity = ObjectIdentity
nwr = _Nwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 54)
)
_OssLDAP_ObjectIdentity = ObjectIdentity
ossLDAP = _OssLDAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 55)
)
_Dx200IptGateway_ObjectIdentity = ObjectIdentity
dx200IptGateway = _Dx200IptGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 56)
)
_DownloadServer_ObjectIdentity = ObjectIdentity
downloadServer = _DownloadServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 57)
)
_MPES_ObjectIdentity = ObjectIdentity
mPES = _MPES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 58)
)
_MicroWaveRadioProducts_ObjectIdentity = ObjectIdentity
microWaveRadioProducts = _MicroWaveRadioProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 59)
)
_AppGateway_ObjectIdentity = ObjectIdentity
appGateway = _AppGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 60)
)
_Pts_ObjectIdentity = ObjectIdentity
pts = _Pts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 61)
)
_Nawp_ObjectIdentity = ObjectIdentity
nawp = _Nawp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 62)
)
_FlexiServerLDAP_ObjectIdentity = ObjectIdentity
flexiServerLDAP = _FlexiServerLDAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 63)
)
_NokiaVars_ObjectIdentity = ObjectIdentity
nokiaVars = _NokiaVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 2)
)
_NokiaSystem_ObjectIdentity = ObjectIdentity
nokiaSystem = _NokiaSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 2, 1)
)
_NokiaInterface_ObjectIdentity = ObjectIdentity
nokiaInterface = _NokiaInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 2, 2)
)
_NokiaDot1d_ObjectIdentity = ObjectIdentity
nokiaDot1d = _NokiaDot1d_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 2, 3)
)
_NokiaDot3_ObjectIdentity = ObjectIdentity
nokiaDot3 = _NokiaDot3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 2, 4)
)
_Dot3Rptr_ObjectIdentity = ObjectIdentity
dot3Rptr = _Dot3Rptr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 2, 4, 1)
)
_NokiaVirtualPort_ObjectIdentity = ObjectIdentity
nokiaVirtualPort = _NokiaVirtualPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 2, 5)
)
_NokiaIpRouting_ObjectIdentity = ObjectIdentity
nokiaIpRouting = _NokiaIpRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 2, 6)
)
_NokiaIp_ObjectIdentity = ObjectIdentity
nokiaIp = _NokiaIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 2, 6, 1)
)
_NokiaIcmp_ObjectIdentity = ObjectIdentity
nokiaIcmp = _NokiaIcmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 2, 6, 2)
)
_NokiaUdp_ObjectIdentity = ObjectIdentity
nokiaUdp = _NokiaUdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 2, 6, 3)
)
_NokiaRip_ObjectIdentity = ObjectIdentity
nokiaRip = _NokiaRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 2, 6, 4)
)
_NokiaArp_ObjectIdentity = ObjectIdentity
nokiaArp = _NokiaArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 2, 6, 5)
)
_NokiaSnmp_ObjectIdentity = ObjectIdentity
nokiaSnmp = _NokiaSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 2, 7)
)
_NokiaInterfaceModules_ObjectIdentity = ObjectIdentity
nokiaInterfaceModules = _NokiaInterfaceModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 3)
)
_NokiaManufacturing_ObjectIdentity = ObjectIdentity
nokiaManufacturing = _NokiaManufacturing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 5)
)
_Smd_ObjectIdentity = ObjectIdentity
smd = _Smd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 5, 1)
)
_NokiaTesting_ObjectIdentity = ObjectIdentity
nokiaTesting = _NokiaTesting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 6)
)
_Nms300Testing_ObjectIdentity = ObjectIdentity
nms300Testing = _Nms300Testing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 6, 1)
)
_Nms10Testing_ObjectIdentity = ObjectIdentity
nms10Testing = _Nms10Testing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 6, 2)
)
_IanTesting_ObjectIdentity = ObjectIdentity
ianTesting = _IanTesting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 6, 3)
)
_MpdTesting_ObjectIdentity = ObjectIdentity
mpdTesting = _MpdTesting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 6, 4)
)
_WirelessAPTesting_ObjectIdentity = ObjectIdentity
wirelessAPTesting = _WirelessAPTesting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 6, 5)
)
_AzTesting_ObjectIdentity = ObjectIdentity
azTesting = _AzTesting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 6, 6)
)
_NhcTesting_ObjectIdentity = ObjectIdentity
nhcTesting = _NhcTesting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 6, 7)
)
_NsgTesting_ObjectIdentity = ObjectIdentity
nsgTesting = _NsgTesting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 6, 8)
)
_AsgTesting_ObjectIdentity = ObjectIdentity
asgTesting = _AsgTesting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 6, 9)
)
_MPlatformTesting_ObjectIdentity = ObjectIdentity
mPlatformTesting = _MPlatformTesting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 6, 10)
)
_NwrTesting_ObjectIdentity = ObjectIdentity
nwrTesting = _NwrTesting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 6, 11)
)
_NokiaSnmpInterface_ObjectIdentity = ObjectIdentity
nokiaSnmpInterface = _NokiaSnmpInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 7)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOKIA-OID-REGISTRATION-MIB",
    **{"nokia": nokia,
       "nokiaProducts": nokiaProducts,
       "localBridge": localBridge,
       "remoteBridge": remoteBridge,
       "frameRelayBridge": frameRelayBridge,
       "frameRelayBrouter": frameRelayBrouter,
       "hubFamily": hubFamily,
       "lanGateway": lanGateway,
       "localBrouter": localBrouter,
       "accessManager": accessManager,
       "nmsProxy": nmsProxy,
       "dynaModemMIB": dynaModemMIB,
       "nawe": nawe,
       "stTropez": stTropez,
       "nms300": nms300,
       "ian": ian,
       "ntcCommon": ntcCommon,
       "ntm10": ntm10,
       "etIfRel1": etIfRel1,
       "etIfRel2": etIfRel2,
       "atmVoiceDataMux": atmVoiceDataMux,
       "ipsoProducts": ipsoProducts,
       "bban": bban,
       "namp": namp,
       "ggsn": ggsn,
       "nms10": nms10,
       "wirelessAccessPoint": wirelessAccessPoint,
       "wirelessLANclient": wirelessLANclient,
       "els": els,
       "accessServer": accessServer,
       "cg": cg,
       "sgsn": sgsn,
       "azc": azc,
       "wapServer": wapServer,
       "s30": s30,
       "ipTelephony": ipTelephony,
       "max": max,
       "twiss": twiss,
       "nokiaRFCExtensions": nokiaRFCExtensions,
       "ost": ost,
       "nsg": nsg,
       "nokiaVPN": nokiaVPN,
       "mmsc": mmsc,
       "nokiaLoopmaster": nokiaLoopmaster,
       "nokiaSSL": nokiaSSL,
       "nokiaAlchemyOS": nokiaAlchemyOS,
       "nals": nals,
       "ipTrunk": ipTrunk,
       "nawg": nawg,
       "nokiaPKI": nokiaPKI,
       "asg": asg,
       "nap": nap,
       "mPlatform": mPlatform,
       "netAct4BB": netAct4BB,
       "nwr": nwr,
       "ossLDAP": ossLDAP,
       "dx200IptGateway": dx200IptGateway,
       "downloadServer": downloadServer,
       "mPES": mPES,
       "microWaveRadioProducts": microWaveRadioProducts,
       "appGateway": appGateway,
       "pts": pts,
       "nawp": nawp,
       "flexiServerLDAP": flexiServerLDAP,
       "nokiaVars": nokiaVars,
       "nokiaSystem": nokiaSystem,
       "nokiaInterface": nokiaInterface,
       "nokiaDot1d": nokiaDot1d,
       "nokiaDot3": nokiaDot3,
       "dot3Rptr": dot3Rptr,
       "nokiaVirtualPort": nokiaVirtualPort,
       "nokiaIpRouting": nokiaIpRouting,
       "nokiaIp": nokiaIp,
       "nokiaIcmp": nokiaIcmp,
       "nokiaUdp": nokiaUdp,
       "nokiaRip": nokiaRip,
       "nokiaArp": nokiaArp,
       "nokiaSnmp": nokiaSnmp,
       "nokiaInterfaceModules": nokiaInterfaceModules,
       "nokiaManufacturing": nokiaManufacturing,
       "smd": smd,
       "nokiaTesting": nokiaTesting,
       "nms300Testing": nms300Testing,
       "nms10Testing": nms10Testing,
       "ianTesting": ianTesting,
       "mpdTesting": mpdTesting,
       "wirelessAPTesting": wirelessAPTesting,
       "azTesting": azTesting,
       "nhcTesting": nhcTesting,
       "nsgTesting": nsgTesting,
       "asgTesting": asgTesting,
       "mPlatformTesting": mPlatformTesting,
       "nwrTesting": nwrTesting,
       "nokiaSnmpInterface": nokiaSnmpInterface}
)
