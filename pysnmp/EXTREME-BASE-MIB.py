# SNMP MIB module (EXTREME-BASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:19 2024
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



class PortList(OctetString, TextualConvention):
    status = "current"


class L4Port(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )



class ExtremeGenAddr(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class ExtremeDeviceId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class WPACipherSet(Bits, TextualConvention):
    status = "current"


class WPAKeyMgmtSet(Bits, TextualConvention):
    status = "current"


class ClientAuthType(Integer32, TextualConvention):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("dot1x", 4),
          ("mac-based", 3),
          ("none", 0),
          ("open", 1),
          ("web-based", 6),
          ("wep", 2),
          ("wpa", 7),
          ("wpa-psk", 5),
          ("wpa2", 8),
          ("wpa2-psk", 9))
    )



class WirelessRemoteConnectBindingType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip-address", 3),
          ("mac-address", 1),
          ("none", 0),
          ("serial-number", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Extremenetworks_ObjectIdentity = ObjectIdentity
extremenetworks = _Extremenetworks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916)
)
_ExtremeV1Traps_ObjectIdentity = ObjectIdentity
extremeV1Traps = _ExtremeV1Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 0)
)
_ExtremeAgent_ObjectIdentity = ObjectIdentity
extremeAgent = _ExtremeAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1)
)
_ExtremeSystem_ObjectIdentity = ObjectIdentity
extremeSystem = _ExtremeSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1)
)
_ExtremeVlan_ObjectIdentity = ObjectIdentity
extremeVlan = _ExtremeVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2)
)
_ExtremeQos_ObjectIdentity = ObjectIdentity
extremeQos = _ExtremeQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3)
)
_ExtremePort_ObjectIdentity = ObjectIdentity
extremePort = _ExtremePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4)
)
_ExtremeVC_ObjectIdentity = ObjectIdentity
extremeVC = _ExtremeVC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 5)
)
_ExtremeTrapPoll_ObjectIdentity = ObjectIdentity
extremeTrapPoll = _ExtremeTrapPoll_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 6)
)
_ExtremeQosPolicy_ObjectIdentity = ObjectIdentity
extremeQosPolicy = _ExtremeQosPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7)
)
_ExtremeDlcs_ObjectIdentity = ObjectIdentity
extremeDlcs = _ExtremeDlcs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 8)
)
_ExtremeFileTransfer_ObjectIdentity = ObjectIdentity
extremeFileTransfer = _ExtremeFileTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 10)
)
_ExtremeRtStats_ObjectIdentity = ObjectIdentity
extremeRtStats = _ExtremeRtStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 11)
)
_ExtremeEsrp_ObjectIdentity = ObjectIdentity
extremeEsrp = _ExtremeEsrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12)
)
_ExtremeEdp_ObjectIdentity = ObjectIdentity
extremeEdp = _ExtremeEdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 13)
)
_ExtremeSlb_ObjectIdentity = ObjectIdentity
extremeSlb = _ExtremeSlb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 14)
)
_ExtremeOspf_ObjectIdentity = ObjectIdentity
extremeOspf = _ExtremeOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 15)
)
_ExtremeFdb_ObjectIdentity = ObjectIdentity
extremeFdb = _ExtremeFdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16)
)
_ExtremeStp_ObjectIdentity = ObjectIdentity
extremeStp = _ExtremeStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17)
)
_ExtremePOSMib_ObjectIdentity = ObjectIdentity
extremePOSMib = _ExtremePOSMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20)
)
_ExtremeNPMib_ObjectIdentity = ObjectIdentity
extremeNPMib = _ExtremeNPMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21)
)
_ExtremeNetFlow_ObjectIdentity = ObjectIdentity
extremeNetFlow = _ExtremeNetFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22)
)
_ExtremeSnmpv3_ObjectIdentity = ObjectIdentity
extremeSnmpv3 = _ExtremeSnmpv3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 23)
)
_ExtremeCable_ObjectIdentity = ObjectIdentity
extremeCable = _ExtremeCable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24)
)
_ExtremeWireless_ObjectIdentity = ObjectIdentity
extremeWireless = _ExtremeWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25)
)
_ExtremeAP_ObjectIdentity = ObjectIdentity
extremeAP = _ExtremeAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1)
)
_ExtremeLAC_ObjectIdentity = ObjectIdentity
extremeLAC = _ExtremeLAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2)
)
_ExtremeDosMib_ObjectIdentity = ObjectIdentity
extremeDosMib = _ExtremeDosMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 28)
)
_ExtremeEnhDosMib_ObjectIdentity = ObjectIdentity
extremeEnhDosMib = _ExtremeEnhDosMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29)
)
_ExtremeEntity_ObjectIdentity = ObjectIdentity
extremeEntity = _ExtremeEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 31)
)
_ExtremeProduct_ObjectIdentity = ObjectIdentity
extremeProduct = _ExtremeProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2)
)
_Summit1_ObjectIdentity = ObjectIdentity
summit1 = _Summit1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 1)
)
_Summit2_ObjectIdentity = ObjectIdentity
summit2 = _Summit2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 2)
)
_Summit3_ObjectIdentity = ObjectIdentity
summit3 = _Summit3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 3)
)
_Summit4_ObjectIdentity = ObjectIdentity
summit4 = _Summit4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 4)
)
_Summit4fx_ObjectIdentity = ObjectIdentity
summit4fx = _Summit4fx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 5)
)
_Summit48_ObjectIdentity = ObjectIdentity
summit48 = _Summit48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 6)
)
_Summit24_ObjectIdentity = ObjectIdentity
summit24 = _Summit24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 7)
)
_BlackDiamond6800_ObjectIdentity = ObjectIdentity
blackDiamond6800 = _BlackDiamond6800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 8)
)
_BlackDiamond6808_ObjectIdentity = ObjectIdentity
blackDiamond6808 = _BlackDiamond6808_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 11)
)
_Summit7iSX_ObjectIdentity = ObjectIdentity
summit7iSX = _Summit7iSX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 12)
)
_Summit7iTX_ObjectIdentity = ObjectIdentity
summit7iTX = _Summit7iTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 13)
)
_Summit1iTX_ObjectIdentity = ObjectIdentity
summit1iTX = _Summit1iTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 14)
)
_Summit5i_ObjectIdentity = ObjectIdentity
summit5i = _Summit5i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 15)
)
_Summit48i_ObjectIdentity = ObjectIdentity
summit48i = _Summit48i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 16)
)
_Alpine3808_ObjectIdentity = ObjectIdentity
alpine3808 = _Alpine3808_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 17)
)
_Summit1iSX_ObjectIdentity = ObjectIdentity
summit1iSX = _Summit1iSX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 19)
)
_Alpine3804_ObjectIdentity = ObjectIdentity
alpine3804 = _Alpine3804_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 20)
)
_Summit5iLX_ObjectIdentity = ObjectIdentity
summit5iLX = _Summit5iLX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 21)
)
_Summit5iTX_ObjectIdentity = ObjectIdentity
summit5iTX = _Summit5iTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 22)
)
_EnetSwitch24Port_ObjectIdentity = ObjectIdentity
enetSwitch24Port = _EnetSwitch24Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 23)
)
_BlackDiamond6816_ObjectIdentity = ObjectIdentity
blackDiamond6816 = _BlackDiamond6816_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 24)
)
_Summit24e3_ObjectIdentity = ObjectIdentity
summit24e3 = _Summit24e3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 25)
)
_Alpine3802_ObjectIdentity = ObjectIdentity
alpine3802 = _Alpine3802_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 26)
)
_BlackDiamond6804_ObjectIdentity = ObjectIdentity
blackDiamond6804 = _BlackDiamond6804_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 27)
)
_Summit48si_ObjectIdentity = ObjectIdentity
summit48si = _Summit48si_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 28)
)
_SummitPx1_ObjectIdentity = ObjectIdentity
summitPx1 = _SummitPx1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 30)
)
_Summit24e2TX_ObjectIdentity = ObjectIdentity
summit24e2TX = _Summit24e2TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 40)
)
_Summit24e2SX_ObjectIdentity = ObjectIdentity
summit24e2SX = _Summit24e2SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 41)
)
_Summit200_24_ObjectIdentity = ObjectIdentity
summit200_24 = _Summit200_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 53)
)
_Summit200_48_ObjectIdentity = ObjectIdentity
summit200_48 = _Summit200_48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 54)
)
_Summit300_48_ObjectIdentity = ObjectIdentity
summit300_48 = _Summit300_48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 55)
)
_Summit400_48t_ObjectIdentity = ObjectIdentity
summit400_48t = _Summit400_48t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 58)
)
_Summit400_24x_ObjectIdentity = ObjectIdentity
summit400_24x = _Summit400_24x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 59)
)
_Summit300_24_ObjectIdentity = ObjectIdentity
summit300_24 = _Summit300_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 61)
)
_Summit400_24t_ObjectIdentity = ObjectIdentity
summit400_24t = _Summit400_24t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 63)
)
_Summit400_24p_ObjectIdentity = ObjectIdentity
summit400_24p = _Summit400_24p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 64)
)
_ExtremeStack_ObjectIdentity = ObjectIdentity
extremeStack = _ExtremeStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 67)
)
_Summit200_24fx_ObjectIdentity = ObjectIdentity
summit200_24fx = _Summit200_24fx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 70)
)
_ExtremeMisc_ObjectIdentity = ObjectIdentity
extremeMisc = _ExtremeMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3)
)
_ExtremeOids_ObjectIdentity = ObjectIdentity
extremeOids = _ExtremeOids_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1)
)
_ExtremeMauType_ObjectIdentity = ObjectIdentity
extremeMauType = _ExtremeMauType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1)
)
_ExtremeMauType1000BaseSX_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseSX = _ExtremeMauType1000BaseSX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 1)
)
_ExtremeMauType1000BaseLX_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseLX = _ExtremeMauType1000BaseLX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 2)
)
_ExtremeMauType1000BaseCX_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseCX = _ExtremeMauType1000BaseCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 3)
)
_ExtremeMauType1000BaseSXFD_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseSXFD = _ExtremeMauType1000BaseSXFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 4)
)
_ExtremeMauType1000BaseLXFD_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseLXFD = _ExtremeMauType1000BaseLXFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 5)
)
_ExtremeMauType1000BaseCXFD_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseCXFD = _ExtremeMauType1000BaseCXFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 6)
)
_ExtremeMauType1000BaseWDMHD_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseWDMHD = _ExtremeMauType1000BaseWDMHD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 7)
)
_ExtremeMauType1000BaseWDMFD_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseWDMFD = _ExtremeMauType1000BaseWDMFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 8)
)
_ExtremeMauType1000BaseLX70HD_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseLX70HD = _ExtremeMauType1000BaseLX70HD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 9)
)
_ExtremeMauType1000BaseLX70FD_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseLX70FD = _ExtremeMauType1000BaseLX70FD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 10)
)
_ExtremeMauType1000BaseZXHD_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseZXHD = _ExtremeMauType1000BaseZXHD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 11)
)
_ExtremeMauType1000BaseZXFD_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseZXFD = _ExtremeMauType1000BaseZXFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 12)
)
_ExtremeMauType1000BaseLX100HD_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseLX100HD = _ExtremeMauType1000BaseLX100HD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 13)
)
_ExtremeMauType1000BaseLX100FD_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseLX100FD = _ExtremeMauType1000BaseLX100FD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 14)
)
_ExtremeV2Traps_ObjectIdentity = ObjectIdentity
extremeV2Traps = _ExtremeV2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-BASE-MIB",
    **{"PortList": PortList,
       "L4Port": L4Port,
       "ExtremeGenAddr": ExtremeGenAddr,
       "ExtremeDeviceId": ExtremeDeviceId,
       "WPACipherSet": WPACipherSet,
       "WPAKeyMgmtSet": WPAKeyMgmtSet,
       "ClientAuthType": ClientAuthType,
       "WirelessRemoteConnectBindingType": WirelessRemoteConnectBindingType,
       "extremenetworks": extremenetworks,
       "extremeV1Traps": extremeV1Traps,
       "extremeAgent": extremeAgent,
       "extremeSystem": extremeSystem,
       "extremeVlan": extremeVlan,
       "extremeQos": extremeQos,
       "extremePort": extremePort,
       "extremeVC": extremeVC,
       "extremeTrapPoll": extremeTrapPoll,
       "extremeQosPolicy": extremeQosPolicy,
       "extremeDlcs": extremeDlcs,
       "extremeFileTransfer": extremeFileTransfer,
       "extremeRtStats": extremeRtStats,
       "extremeEsrp": extremeEsrp,
       "extremeEdp": extremeEdp,
       "extremeSlb": extremeSlb,
       "extremeOspf": extremeOspf,
       "extremeFdb": extremeFdb,
       "extremeStp": extremeStp,
       "extremePOSMib": extremePOSMib,
       "extremeNPMib": extremeNPMib,
       "extremeNetFlow": extremeNetFlow,
       "extremeSnmpv3": extremeSnmpv3,
       "extremeCable": extremeCable,
       "extremeWireless": extremeWireless,
       "extremeAP": extremeAP,
       "extremeLAC": extremeLAC,
       "extremeDosMib": extremeDosMib,
       "extremeEnhDosMib": extremeEnhDosMib,
       "extremeEntity": extremeEntity,
       "extremeProduct": extremeProduct,
       "summit1": summit1,
       "summit2": summit2,
       "summit3": summit3,
       "summit4": summit4,
       "summit4fx": summit4fx,
       "summit48": summit48,
       "summit24": summit24,
       "blackDiamond6800": blackDiamond6800,
       "blackDiamond6808": blackDiamond6808,
       "summit7iSX": summit7iSX,
       "summit7iTX": summit7iTX,
       "summit1iTX": summit1iTX,
       "summit5i": summit5i,
       "summit48i": summit48i,
       "alpine3808": alpine3808,
       "summit1iSX": summit1iSX,
       "alpine3804": alpine3804,
       "summit5iLX": summit5iLX,
       "summit5iTX": summit5iTX,
       "enetSwitch24Port": enetSwitch24Port,
       "blackDiamond6816": blackDiamond6816,
       "summit24e3": summit24e3,
       "alpine3802": alpine3802,
       "blackDiamond6804": blackDiamond6804,
       "summit48si": summit48si,
       "summitPx1": summitPx1,
       "summit24e2TX": summit24e2TX,
       "summit24e2SX": summit24e2SX,
       "summit200-24": summit200_24,
       "summit200-48": summit200_48,
       "summit300-48": summit300_48,
       "summit400-48t": summit400_48t,
       "summit400-24x": summit400_24x,
       "summit300-24": summit300_24,
       "summit400-24t": summit400_24t,
       "summit400-24p": summit400_24p,
       "extremeStack": extremeStack,
       "summit200-24fx": summit200_24fx,
       "extremeMisc": extremeMisc,
       "extremeOids": extremeOids,
       "extremeMauType": extremeMauType,
       "extremeMauType1000BaseSX": extremeMauType1000BaseSX,
       "extremeMauType1000BaseLX": extremeMauType1000BaseLX,
       "extremeMauType1000BaseCX": extremeMauType1000BaseCX,
       "extremeMauType1000BaseSXFD": extremeMauType1000BaseSXFD,
       "extremeMauType1000BaseLXFD": extremeMauType1000BaseLXFD,
       "extremeMauType1000BaseCXFD": extremeMauType1000BaseCXFD,
       "extremeMauType1000BaseWDMHD": extremeMauType1000BaseWDMHD,
       "extremeMauType1000BaseWDMFD": extremeMauType1000BaseWDMFD,
       "extremeMauType1000BaseLX70HD": extremeMauType1000BaseLX70HD,
       "extremeMauType1000BaseLX70FD": extremeMauType1000BaseLX70FD,
       "extremeMauType1000BaseZXHD": extremeMauType1000BaseZXHD,
       "extremeMauType1000BaseZXFD": extremeMauType1000BaseZXFD,
       "extremeMauType1000BaseLX100HD": extremeMauType1000BaseLX100HD,
       "extremeMauType1000BaseLX100FD": extremeMauType1000BaseLX100FD,
       "extremeV2Traps": extremeV2Traps}
)
