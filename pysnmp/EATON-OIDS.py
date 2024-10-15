# SNMP MIB module (EATON-OIDS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EATON-OIDS
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:18 2024
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

eaton = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 534)
)
eaton.setRevisions(
        ("2014-02-19 00:00",
         "2010-01-24 00:00",
         "2009-06-18 00:00",
         "2007-08-06 00:00",
         "2007-07-05 00:00",
         "2006-10-15 00:00",
         "2006-05-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PositiveInteger(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class NonNegativeInteger(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_XupsMIB_ObjectIdentity = ObjectIdentity
xupsMIB = _XupsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1)
)
_XupsEnvironment_ObjectIdentity = ObjectIdentity
xupsEnvironment = _XupsEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 6)
)
_XupsObjectId_ObjectIdentity = ObjectIdentity
xupsObjectId = _XupsObjectId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 2)
)
_PowerwareEthernetSnmpAdapter_ObjectIdentity = ObjectIdentity
powerwareEthernetSnmpAdapter = _PowerwareEthernetSnmpAdapter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 2, 1)
)
_PowerwareNetworkSnmpAdapterEther_ObjectIdentity = ObjectIdentity
powerwareNetworkSnmpAdapterEther = _PowerwareNetworkSnmpAdapterEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 2, 2)
)
_PowerwareNetworkSnmpAdapterToken_ObjectIdentity = ObjectIdentity
powerwareNetworkSnmpAdapterToken = _PowerwareNetworkSnmpAdapterToken_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 2, 3)
)
_OnlinetDaemon_ObjectIdentity = ObjectIdentity
onlinetDaemon = _OnlinetDaemon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 2, 4)
)
_ConnectUPSAdapterEthernet_ObjectIdentity = ObjectIdentity
connectUPSAdapterEthernet = _ConnectUPSAdapterEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 2, 5)
)
_PowerwareNetworkDigitalIOEther_ObjectIdentity = ObjectIdentity
powerwareNetworkDigitalIOEther = _PowerwareNetworkDigitalIOEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 2, 6)
)
_ConnectUPSAdapterTokenRing_ObjectIdentity = ObjectIdentity
connectUPSAdapterTokenRing = _ConnectUPSAdapterTokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 2, 7)
)
_SimpleSnmpAdapter_ObjectIdentity = ObjectIdentity
simpleSnmpAdapter = _SimpleSnmpAdapter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 2, 8)
)
_PowerwareEliSnmpAdapter_ObjectIdentity = ObjectIdentity
powerwareEliSnmpAdapter = _PowerwareEliSnmpAdapter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 2, 9)
)
_PowerwareBasicEmbeddedEthernet_ObjectIdentity = ObjectIdentity
powerwareBasicEmbeddedEthernet = _PowerwareBasicEmbeddedEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 2, 10)
)
_EatonPowerChainGateway_ObjectIdentity = ObjectIdentity
eatonPowerChainGateway = _EatonPowerChainGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 2, 11)
)
_EatonPowerChainDevice_ObjectIdentity = ObjectIdentity
eatonPowerChainDevice = _EatonPowerChainDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 2, 12)
)
_EatonPowerXpertMeter_ObjectIdentity = ObjectIdentity
eatonPowerXpertMeter = _EatonPowerXpertMeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 2, 13)
)
_XupsIoMIB_ObjectIdentity = ObjectIdentity
xupsIoMIB = _XupsIoMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 3)
)
_PowerVision_ObjectIdentity = ObjectIdentity
powerVision = _PowerVision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 4)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6)
)
_PduAgent_ObjectIdentity = ObjectIdentity
pduAgent = _PduAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6)
)
_Hdpdu_ObjectIdentity = ObjectIdentity
hdpdu = _Hdpdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 2)
)
_EatonPdu_ObjectIdentity = ObjectIdentity
eatonPdu = _EatonPdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4)
)
_DataCenter_ObjectIdentity = ObjectIdentity
dataCenter = _DataCenter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7)
)
_EnvironmentalMonitor_ObjectIdentity = ObjectIdentity
environmentalMonitor = _EnvironmentalMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 7, 1)
)
_ItProjects_ObjectIdentity = ObjectIdentity
itProjects = _ItProjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 7)
)
_Pki_ObjectIdentity = ObjectIdentity
pki = _Pki_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 7, 1)
)
_PowerChain_ObjectIdentity = ObjectIdentity
powerChain = _PowerChain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 8)
)
_PowerCmnd_ObjectIdentity = ObjectIdentity
powerCmnd = _PowerCmnd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 9)
)
_Sts_ObjectIdentity = ObjectIdentity
sts = _Sts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EATON-OIDS",
    **{"PositiveInteger": PositiveInteger,
       "NonNegativeInteger": NonNegativeInteger,
       "eaton": eaton,
       "xupsMIB": xupsMIB,
       "xupsEnvironment": xupsEnvironment,
       "xupsObjectId": xupsObjectId,
       "powerwareEthernetSnmpAdapter": powerwareEthernetSnmpAdapter,
       "powerwareNetworkSnmpAdapterEther": powerwareNetworkSnmpAdapterEther,
       "powerwareNetworkSnmpAdapterToken": powerwareNetworkSnmpAdapterToken,
       "onlinetDaemon": onlinetDaemon,
       "connectUPSAdapterEthernet": connectUPSAdapterEthernet,
       "powerwareNetworkDigitalIOEther": powerwareNetworkDigitalIOEther,
       "connectUPSAdapterTokenRing": connectUPSAdapterTokenRing,
       "simpleSnmpAdapter": simpleSnmpAdapter,
       "powerwareEliSnmpAdapter": powerwareEliSnmpAdapter,
       "powerwareBasicEmbeddedEthernet": powerwareBasicEmbeddedEthernet,
       "eatonPowerChainGateway": eatonPowerChainGateway,
       "eatonPowerChainDevice": eatonPowerChainDevice,
       "eatonPowerXpertMeter": eatonPowerXpertMeter,
       "xupsIoMIB": xupsIoMIB,
       "powerVision": powerVision,
       "products": products,
       "pduAgent": pduAgent,
       "hdpdu": hdpdu,
       "eatonPdu": eatonPdu,
       "dataCenter": dataCenter,
       "environmentalMonitor": environmentalMonitor,
       "itProjects": itProjects,
       "pki": pki,
       "powerChain": powerChain,
       "powerCmnd": powerCmnd,
       "sts": sts}
)
