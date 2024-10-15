# SNMP MIB module (Juniper-MIBs) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-MIBs
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:35 2024
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

(juniperUniMibs,) = mibBuilder.importSymbols(
    "Juniper-UNI-SMI",
    "juniperUniMibs")

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


# MODULE-IDENTITY

juniMibs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2)
)
juniMibs.setRevisions(
        ("2006-01-01 00:00",
         "2005-08-19 14:21",
         "2005-06-30 18:03",
         "2004-06-07 20:57",
         "2003-11-24 21:02",
         "2003-11-24 18:29",
         "2003-05-05 21:25",
         "2003-04-29 14:18",
         "2003-04-23 13:56",
         "2002-05-31 14:33",
         "2001-11-30 14:12",
         "2000-12-27 15:50",
         "2000-11-22 00:00",
         "2000-09-19 15:40",
         "1999-12-15 15:44",
         "1999-11-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniTextualConventions_ObjectIdentity = ObjectIdentity
juniTextualConventions = _JuniTextualConventions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 1)
)
_JuniSystemMIB_ObjectIdentity = ObjectIdentity
juniSystemMIB = _JuniSystemMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2)
)
_JuniIfMIB_ObjectIdentity = ObjectIdentity
juniIfMIB = _JuniIfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3)
)
_JuniDs3MIB_ObjectIdentity = ObjectIdentity
juniDs3MIB = _JuniDs3MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4)
)
_JuniDs1MIB_ObjectIdentity = ObjectIdentity
juniDs1MIB = _JuniDs1MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5)
)
_JuniFt1MIB_ObjectIdentity = ObjectIdentity
juniFt1MIB = _JuniFt1MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6)
)
_JuniSonetMIB_ObjectIdentity = ObjectIdentity
juniSonetMIB = _JuniSonetMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7)
)
_JuniAtmMIB_ObjectIdentity = ObjectIdentity
juniAtmMIB = _JuniAtmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8)
)
_JuniHdlcMIB_ObjectIdentity = ObjectIdentity
juniHdlcMIB = _JuniHdlcMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9)
)
_JuniFrameRelayMIB_ObjectIdentity = ObjectIdentity
juniFrameRelayMIB = _JuniFrameRelayMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10)
)
_JuniPppMIB_ObjectIdentity = ObjectIdentity
juniPppMIB = _JuniPppMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11)
)
_JuniIpMIB_ObjectIdentity = ObjectIdentity
juniIpMIB = _JuniIpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12)
)
_JuniIpPolicyMIB_ObjectIdentity = ObjectIdentity
juniIpPolicyMIB = _JuniIpPolicyMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13)
)
_JuniOspfMIB_ObjectIdentity = ObjectIdentity
juniOspfMIB = _JuniOspfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14)
)
_JuniSlepMIBS_ObjectIdentity = ObjectIdentity
juniSlepMIBS = _JuniSlepMIBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15)
)
_JuniSnmpMIB_ObjectIdentity = ObjectIdentity
juniSnmpMIB = _JuniSnmpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16)
)
_JuniERXSysMIB_ObjectIdentity = ObjectIdentity
juniERXSysMIB = _JuniERXSysMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17)
)
_JuniPPPoEMIB_ObjectIdentity = ObjectIdentity
juniPPPoEMIB = _JuniPPPoEMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18)
)
_JuniRadiusClientMIB_ObjectIdentity = ObjectIdentity
juniRadiusClientMIB = _JuniRadiusClientMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19)
)
_JuniAaaMIB_ObjectIdentity = ObjectIdentity
juniAaaMIB = _JuniAaaMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20)
)
_JuniAddressPoolMIB_ObjectIdentity = ObjectIdentity
juniAddressPoolMIB = _JuniAddressPoolMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21)
)
_JuniDhcpMIB_ObjectIdentity = ObjectIdentity
juniDhcpMIB = _JuniDhcpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22)
)
_JuniFileXferMIB_ObjectIdentity = ObjectIdentity
juniFileXferMIB = _JuniFileXferMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23)
)
_JuniAcctngMIB_ObjectIdentity = ObjectIdentity
juniAcctngMIB = _JuniAcctngMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24)
)
_JuniProfileMIB_ObjectIdentity = ObjectIdentity
juniProfileMIB = _JuniProfileMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25)
)
_JuniIpProfileMIB_ObjectIdentity = ObjectIdentity
juniIpProfileMIB = _JuniIpProfileMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26)
)
_JuniPolicyMIB_ObjectIdentity = ObjectIdentity
juniPolicyMIB = _JuniPolicyMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27)
)
_JuniLogMIB_ObjectIdentity = ObjectIdentity
juniLogMIB = _JuniLogMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28)
)
_JuniBgpMIB_ObjectIdentity = ObjectIdentity
juniBgpMIB = _JuniBgpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29)
)
_JuniCliMIB_ObjectIdentity = ObjectIdentity
juniCliMIB = _JuniCliMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30)
)
_JuniBridgeEthernetMIB_ObjectIdentity = ObjectIdentity
juniBridgeEthernetMIB = _JuniBridgeEthernetMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31)
)
_JuniRouterMIB_ObjectIdentity = ObjectIdentity
juniRouterMIB = _JuniRouterMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32)
)
_JuniHostMIB_ObjectIdentity = ObjectIdentity
juniHostMIB = _JuniHostMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 33)
)
_JuniEthernetMIB_ObjectIdentity = ObjectIdentity
juniEthernetMIB = _JuniEthernetMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34)
)
_JuniL2tpMIB_ObjectIdentity = ObjectIdentity
juniL2tpMIB = _JuniL2tpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35)
)
_JuniSscClientMIB_ObjectIdentity = ObjectIdentity
juniSscClientMIB = _JuniSscClientMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36)
)
_JuniCopsProtocolMIB_ObjectIdentity = ObjectIdentity
juniCopsProtocolMIB = _JuniCopsProtocolMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37)
)
_JuniIsisMIB_ObjectIdentity = ObjectIdentity
juniIsisMIB = _JuniIsisMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38)
)
_JuniPingMIB_ObjectIdentity = ObjectIdentity
juniPingMIB = _JuniPingMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 39)
)
_JuniIgmpMIB_ObjectIdentity = ObjectIdentity
juniIgmpMIB = _JuniIgmpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40)
)
_JuniTraceRouteMIB_ObjectIdentity = ObjectIdentity
juniTraceRouteMIB = _JuniTraceRouteMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 41)
)
_JuniLookupMIB_ObjectIdentity = ObjectIdentity
juniLookupMIB = _JuniLookupMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 42)
)
_JuniPimMIB_ObjectIdentity = ObjectIdentity
juniPimMIB = _JuniPimMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43)
)
_JuniDvmrpMIB_ObjectIdentity = ObjectIdentity
juniDvmrpMIB = _JuniDvmrpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44)
)
_JuniPppProfileMIB_ObjectIdentity = ObjectIdentity
juniPppProfileMIB = _JuniPppProfileMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45)
)
_JuniPppoeProfileMIB_ObjectIdentity = ObjectIdentity
juniPppoeProfileMIB = _JuniPppoeProfileMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46)
)
_JuniDnsMIB_ObjectIdentity = ObjectIdentity
juniDnsMIB = _JuniDnsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47)
)
_JuniAutoConfMIB_ObjectIdentity = ObjectIdentity
juniAutoConfMIB = _JuniAutoConfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48)
)
_JuniSubscriberMIB_ObjectIdentity = ObjectIdentity
juniSubscriberMIB = _JuniSubscriberMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49)
)
_JuniSmdsMIB_ObjectIdentity = ObjectIdentity
juniSmdsMIB = _JuniSmdsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50)
)
_JuniIpTunnelMIB_ObjectIdentity = ObjectIdentity
juniIpTunnelMIB = _JuniIpTunnelMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51)
)
_JuniCbfMIB_ObjectIdentity = ObjectIdentity
juniCbfMIB = _JuniCbfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52)
)
_JuniL2fMIB_ObjectIdentity = ObjectIdentity
juniL2fMIB = _JuniL2fMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53)
)
_JuniMplsMIB_ObjectIdentity = ObjectIdentity
juniMplsMIB = _JuniMplsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54)
)
_JuniMrxSystemMIB_ObjectIdentity = ObjectIdentity
juniMrxSystemMIB = _JuniMrxSystemMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 55)
)
_JuniSysClockMIB_ObjectIdentity = ObjectIdentity
juniSysClockMIB = _JuniSysClockMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56)
)
_JuniQosMIB_ObjectIdentity = ObjectIdentity
juniQosMIB = _JuniQosMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57)
)
_JuniAtm1483ProfileMIB_ObjectIdentity = ObjectIdentity
juniAtm1483ProfileMIB = _JuniAtm1483ProfileMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58)
)
_JuniV35MIB_ObjectIdentity = ObjectIdentity
juniV35MIB = _JuniV35MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59)
)
_JuniTacacsPlusClientMIB_ObjectIdentity = ObjectIdentity
juniTacacsPlusClientMIB = _JuniTacacsPlusClientMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60)
)
_JuniL2tpDialoutMIB_ObjectIdentity = ObjectIdentity
juniL2tpDialoutMIB = _JuniL2tpDialoutMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62)
)
_JuniBridgeMIB_ObjectIdentity = ObjectIdentity
juniBridgeMIB = _JuniBridgeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 63)
)
_JuniBridgingMgrMIB_ObjectIdentity = ObjectIdentity
juniBridgingMgrMIB = _JuniBridgingMgrMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64)
)
_JuniMRouterMIB_ObjectIdentity = ObjectIdentity
juniMRouterMIB = _JuniMRouterMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65)
)
_JuniDismanEventMIB_ObjectIdentity = ObjectIdentity
juniDismanEventMIB = _JuniDismanEventMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 66)
)
_JuniRadiusDisconnectMIB_ObjectIdentity = ObjectIdentity
juniRadiusDisconnectMIB = _JuniRadiusDisconnectMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 67)
)
_JuniIpv6ProfileMIB_ObjectIdentity = ObjectIdentity
juniIpv6ProfileMIB = _JuniIpv6ProfileMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 68)
)
_JuniDhcpv6MIB_ObjectIdentity = ObjectIdentity
juniDhcpv6MIB = _JuniDhcpv6MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 69)
)
_JuniIpsecTunnelMIB_ObjectIdentity = ObjectIdentity
juniIpsecTunnelMIB = _JuniIpsecTunnelMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70)
)
_JuniIkeMIB_ObjectIdentity = ObjectIdentity
juniIkeMIB = _JuniIkeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71)
)
_JuniTsmMIB_ObjectIdentity = ObjectIdentity
juniTsmMIB = _JuniTsmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72)
)
_JuniRadiusProxyMIB_ObjectIdentity = ObjectIdentity
juniRadiusProxyMIB = _JuniRadiusProxyMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 73)
)
_JuniRedundancyMIB_ObjectIdentity = ObjectIdentity
juniRedundancyMIB = _JuniRedundancyMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74)
)
_JuniRadiusRequestMIB_ObjectIdentity = ObjectIdentity
juniRadiusRequestMIB = _JuniRadiusRequestMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 75)
)
_JuniLicenseMgrMIB_ObjectIdentity = ObjectIdentity
juniLicenseMgrMIB = _JuniLicenseMgrMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 76)
)
_JuniPacketMirrorMIB_ObjectIdentity = ObjectIdentity
juniPacketMirrorMIB = _JuniPacketMirrorMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77)
)
_JuniHttpMIB_ObjectIdentity = ObjectIdentity
juniHttpMIB = _JuniHttpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 78)
)
_JuniHttpProfileMIB_ObjectIdentity = ObjectIdentity
juniHttpProfileMIB = _JuniHttpProfileMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 79)
)
_JuniDosProtectionMIB_ObjectIdentity = ObjectIdentity
juniDosProtectionMIB = _JuniDosProtectionMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 80)
)
_JuniDosProtectionPlatformMIB_ObjectIdentity = ObjectIdentity
juniDosProtectionPlatformMIB = _JuniDosProtectionPlatformMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81)
)
_JuniInetMIB_ObjectIdentity = ObjectIdentity
juniInetMIB = _JuniInetMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 82)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-MIBs",
    **{"juniMibs": juniMibs,
       "juniTextualConventions": juniTextualConventions,
       "juniSystemMIB": juniSystemMIB,
       "juniIfMIB": juniIfMIB,
       "juniDs3MIB": juniDs3MIB,
       "juniDs1MIB": juniDs1MIB,
       "juniFt1MIB": juniFt1MIB,
       "juniSonetMIB": juniSonetMIB,
       "juniAtmMIB": juniAtmMIB,
       "juniHdlcMIB": juniHdlcMIB,
       "juniFrameRelayMIB": juniFrameRelayMIB,
       "juniPppMIB": juniPppMIB,
       "juniIpMIB": juniIpMIB,
       "juniIpPolicyMIB": juniIpPolicyMIB,
       "juniOspfMIB": juniOspfMIB,
       "juniSlepMIBS": juniSlepMIBS,
       "juniSnmpMIB": juniSnmpMIB,
       "juniERXSysMIB": juniERXSysMIB,
       "juniPPPoEMIB": juniPPPoEMIB,
       "juniRadiusClientMIB": juniRadiusClientMIB,
       "juniAaaMIB": juniAaaMIB,
       "juniAddressPoolMIB": juniAddressPoolMIB,
       "juniDhcpMIB": juniDhcpMIB,
       "juniFileXferMIB": juniFileXferMIB,
       "juniAcctngMIB": juniAcctngMIB,
       "juniProfileMIB": juniProfileMIB,
       "juniIpProfileMIB": juniIpProfileMIB,
       "juniPolicyMIB": juniPolicyMIB,
       "juniLogMIB": juniLogMIB,
       "juniBgpMIB": juniBgpMIB,
       "juniCliMIB": juniCliMIB,
       "juniBridgeEthernetMIB": juniBridgeEthernetMIB,
       "juniRouterMIB": juniRouterMIB,
       "juniHostMIB": juniHostMIB,
       "juniEthernetMIB": juniEthernetMIB,
       "juniL2tpMIB": juniL2tpMIB,
       "juniSscClientMIB": juniSscClientMIB,
       "juniCopsProtocolMIB": juniCopsProtocolMIB,
       "juniIsisMIB": juniIsisMIB,
       "juniPingMIB": juniPingMIB,
       "juniIgmpMIB": juniIgmpMIB,
       "juniTraceRouteMIB": juniTraceRouteMIB,
       "juniLookupMIB": juniLookupMIB,
       "juniPimMIB": juniPimMIB,
       "juniDvmrpMIB": juniDvmrpMIB,
       "juniPppProfileMIB": juniPppProfileMIB,
       "juniPppoeProfileMIB": juniPppoeProfileMIB,
       "juniDnsMIB": juniDnsMIB,
       "juniAutoConfMIB": juniAutoConfMIB,
       "juniSubscriberMIB": juniSubscriberMIB,
       "juniSmdsMIB": juniSmdsMIB,
       "juniIpTunnelMIB": juniIpTunnelMIB,
       "juniCbfMIB": juniCbfMIB,
       "juniL2fMIB": juniL2fMIB,
       "juniMplsMIB": juniMplsMIB,
       "juniMrxSystemMIB": juniMrxSystemMIB,
       "juniSysClockMIB": juniSysClockMIB,
       "juniQosMIB": juniQosMIB,
       "juniAtm1483ProfileMIB": juniAtm1483ProfileMIB,
       "juniV35MIB": juniV35MIB,
       "juniTacacsPlusClientMIB": juniTacacsPlusClientMIB,
       "juniL2tpDialoutMIB": juniL2tpDialoutMIB,
       "juniBridgeMIB": juniBridgeMIB,
       "juniBridgingMgrMIB": juniBridgingMgrMIB,
       "juniMRouterMIB": juniMRouterMIB,
       "juniDismanEventMIB": juniDismanEventMIB,
       "juniRadiusDisconnectMIB": juniRadiusDisconnectMIB,
       "juniIpv6ProfileMIB": juniIpv6ProfileMIB,
       "juniDhcpv6MIB": juniDhcpv6MIB,
       "juniIpsecTunnelMIB": juniIpsecTunnelMIB,
       "juniIkeMIB": juniIkeMIB,
       "juniTsmMIB": juniTsmMIB,
       "juniRadiusProxyMIB": juniRadiusProxyMIB,
       "juniRedundancyMIB": juniRedundancyMIB,
       "juniRadiusRequestMIB": juniRadiusRequestMIB,
       "juniLicenseMgrMIB": juniLicenseMgrMIB,
       "juniPacketMirrorMIB": juniPacketMirrorMIB,
       "juniHttpMIB": juniHttpMIB,
       "juniHttpProfileMIB": juniHttpProfileMIB,
       "juniDosProtectionMIB": juniDosProtectionMIB,
       "juniDosProtectionPlatformMIB": juniDosProtectionPlatformMIB,
       "juniInetMIB": juniInetMIB}
)
