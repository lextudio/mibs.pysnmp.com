# SNMP MIB module (JUNIPER-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:17 2024
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

juniperMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636)
)
juniperMIB.setRevisions(
        ("2010-07-09 00:00",
         "2009-10-29 00:00",
         "2010-06-18 00:00",
         "2003-04-17 01:00",
         "2005-08-17 01:00",
         "2006-12-14 01:00",
         "2007-01-01 00:00",
         "2007-10-09 00:00",
         "2009-12-31 00:00",
         "2010-07-14 00:00",
         "2011-01-26 00:00",
         "2012-02-10 00:00",
         "2012-08-01 00:00",
         "2012-11-01 00:00",
         "2012-12-07 00:00",
         "2013-01-25 00:00",
         "2013-11-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxProducts_ObjectIdentity = ObjectIdentity
jnxProducts = _JnxProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1)
)
if mibBuilder.loadTexts:
    jnxProducts.setStatus("current")
_JnxMediaFlow_ObjectIdentity = ObjectIdentity
jnxMediaFlow = _JnxMediaFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 2)
)
_JnxJunosSpace_ObjectIdentity = ObjectIdentity
jnxJunosSpace = _JnxJunosSpace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 3)
)
_JnxReservedProducts3_ObjectIdentity = ObjectIdentity
jnxReservedProducts3 = _JnxReservedProducts3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 4)
)
_JnxReservedProducts4_ObjectIdentity = ObjectIdentity
jnxReservedProducts4 = _JnxReservedProducts4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 5)
)
_JnxReservedProducts5_ObjectIdentity = ObjectIdentity
jnxReservedProducts5 = _JnxReservedProducts5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 6)
)
_JnxSDKApplicationsRoot_ObjectIdentity = ObjectIdentity
jnxSDKApplicationsRoot = _JnxSDKApplicationsRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 7)
)
_JnxJAB_ObjectIdentity = ObjectIdentity
jnxJAB = _JnxJAB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 8)
)
_JnxStrm_ObjectIdentity = ObjectIdentity
jnxStrm = _JnxStrm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 9)
)
_JnxServices_ObjectIdentity = ObjectIdentity
jnxServices = _JnxServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 2)
)
if mibBuilder.loadTexts:
    jnxServices.setStatus("current")
_JnxMibs_ObjectIdentity = ObjectIdentity
jnxMibs = _JnxMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3)
)
if mibBuilder.loadTexts:
    jnxMibs.setStatus("current")
_JnxJsMibRoot_ObjectIdentity = ObjectIdentity
jnxJsMibRoot = _JnxJsMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39)
)
_JnxExMibRoot_ObjectIdentity = ObjectIdentity
jnxExMibRoot = _JnxExMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40)
)
_JnxWxMibRoot_ObjectIdentity = ObjectIdentity
jnxWxMibRoot = _JnxWxMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41)
)
_JnxDcfMibRoot_ObjectIdentity = ObjectIdentity
jnxDcfMibRoot = _JnxDcfMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42)
)
_JnxReservedMibs5_ObjectIdentity = ObjectIdentity
jnxReservedMibs5 = _JnxReservedMibs5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 43)
)
_JnxPfeMibRoot_ObjectIdentity = ObjectIdentity
jnxPfeMibRoot = _JnxPfeMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 44)
)
_JnxBfdMibRoot_ObjectIdentity = ObjectIdentity
jnxBfdMibRoot = _JnxBfdMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45)
)
_JnxXstpMibs_ObjectIdentity = ObjectIdentity
jnxXstpMibs = _JnxXstpMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 46)
)
_JnxUtilMibRoot_ObjectIdentity = ObjectIdentity
jnxUtilMibRoot = _JnxUtilMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47)
)
_Jnxl2aldMibRoot_ObjectIdentity = ObjectIdentity
jnxl2aldMibRoot = _Jnxl2aldMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 48)
)
_JnxL2tpMibRoot_ObjectIdentity = ObjectIdentity
jnxL2tpMibRoot = _JnxL2tpMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49)
)
_JnxRpmMibRoot_ObjectIdentity = ObjectIdentity
jnxRpmMibRoot = _JnxRpmMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 50)
)
_JnxUserAAAMibRoot_ObjectIdentity = ObjectIdentity
jnxUserAAAMibRoot = _JnxUserAAAMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51)
)
_JnxIpSecMibRoot_ObjectIdentity = ObjectIdentity
jnxIpSecMibRoot = _JnxIpSecMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52)
)
_JnxL2cpMibRoot_ObjectIdentity = ObjectIdentity
jnxL2cpMibRoot = _JnxL2cpMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 53)
)
_JnxPwTdmMibRoot_ObjectIdentity = ObjectIdentity
jnxPwTdmMibRoot = _JnxPwTdmMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 54)
)
_JnxPwTCMibRoot_ObjectIdentity = ObjectIdentity
jnxPwTCMibRoot = _JnxPwTCMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 55)
)
_JnxOtnMibRoot_ObjectIdentity = ObjectIdentity
jnxOtnMibRoot = _JnxOtnMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 56)
)
_JnxPsuMIBRoot_ObjectIdentity = ObjectIdentity
jnxPsuMIBRoot = _JnxPsuMIBRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 58)
)
_JnxSvcsMibRoot_ObjectIdentity = ObjectIdentity
jnxSvcsMibRoot = _JnxSvcsMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59)
)
_JnxDomMibRoot_ObjectIdentity = ObjectIdentity
jnxDomMibRoot = _JnxDomMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 60)
)
_JnxJdhcpMibRoot_ObjectIdentity = ObjectIdentity
jnxJdhcpMibRoot = _JnxJdhcpMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61)
)
_JnxJdhcpv6MibRoot_ObjectIdentity = ObjectIdentity
jnxJdhcpv6MibRoot = _JnxJdhcpv6MibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62)
)
_JnxLicenseMibRoot_ObjectIdentity = ObjectIdentity
jnxLicenseMibRoot = _JnxLicenseMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 63)
)
_JnxSubscriberMibRoot_ObjectIdentity = ObjectIdentity
jnxSubscriberMibRoot = _JnxSubscriberMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64)
)
_JnxMagMibRoot_ObjectIdentity = ObjectIdentity
jnxMagMibRoot = _JnxMagMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 65)
)
_JnxMobileGatewayMibRoot_ObjectIdentity = ObjectIdentity
jnxMobileGatewayMibRoot = _JnxMobileGatewayMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66)
)
_JnxPppoeMibRoot_ObjectIdentity = ObjectIdentity
jnxPppoeMibRoot = _JnxPppoeMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67)
)
_JnxPppMibRoot_ObjectIdentity = ObjectIdentity
jnxPppMibRoot = _JnxPppMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68)
)
_JnxJVAEMibRoot_ObjectIdentity = ObjectIdentity
jnxJVAEMibRoot = _JnxJVAEMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 69)
)
_JnxIfOtnMibRoot_ObjectIdentity = ObjectIdentity
jnxIfOtnMibRoot = _JnxIfOtnMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 70)
)
_JnxOpticsMibRoot_ObjectIdentity = ObjectIdentity
jnxOpticsMibRoot = _JnxOpticsMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71)
)
_JnxAlarmExtMibRoot_ObjectIdentity = ObjectIdentity
jnxAlarmExtMibRoot = _JnxAlarmExtMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 72)
)
_JnxoptIfMibRoot_ObjectIdentity = ObjectIdentity
jnxoptIfMibRoot = _JnxoptIfMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 73)
)
_JnxFruMibRoot_ObjectIdentity = ObjectIdentity
jnxFruMibRoot = _JnxFruMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 74)
)
_JnxTimingNotfnsMIBRoot_ObjectIdentity = ObjectIdentity
jnxTimingNotfnsMIBRoot = _JnxTimingNotfnsMIBRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75)
)
_JnxSnmpSetMibRoot_ObjectIdentity = ObjectIdentity
jnxSnmpSetMibRoot = _JnxSnmpSetMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 76)
)
_JnxTraps_ObjectIdentity = ObjectIdentity
jnxTraps = _JnxTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4)
)
if mibBuilder.loadTexts:
    jnxTraps.setStatus("current")
_JnxChassisTraps_ObjectIdentity = ObjectIdentity
jnxChassisTraps = _JnxChassisTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 1)
)
_JnxChassisOKTraps_ObjectIdentity = ObjectIdentity
jnxChassisOKTraps = _JnxChassisOKTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 2)
)
_JnxRmonTraps_ObjectIdentity = ObjectIdentity
jnxRmonTraps = _JnxRmonTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 3)
)
_JnxLdpTraps_ObjectIdentity = ObjectIdentity
jnxLdpTraps = _JnxLdpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 4)
)
_JnxCmNotifications_ObjectIdentity = ObjectIdentity
jnxCmNotifications = _JnxCmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 5)
)
_JnxSonetNotifications_ObjectIdentity = ObjectIdentity
jnxSonetNotifications = _JnxSonetNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 6)
)
_JnxPMonNotifications_ObjectIdentity = ObjectIdentity
jnxPMonNotifications = _JnxPMonNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 7)
)
_JnxCollectorNotifications_ObjectIdentity = ObjectIdentity
jnxCollectorNotifications = _JnxCollectorNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 8)
)
_JnxPingNotifications_ObjectIdentity = ObjectIdentity
jnxPingNotifications = _JnxPingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 9)
)
_JnxSpNotifications_ObjectIdentity = ObjectIdentity
jnxSpNotifications = _JnxSpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 10)
)
_JnxDfcNotifications_ObjectIdentity = ObjectIdentity
jnxDfcNotifications = _JnxDfcNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 11)
)
_JnxSyslogNotifications_ObjectIdentity = ObjectIdentity
jnxSyslogNotifications = _JnxSyslogNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 12)
)
_JnxEventNotifications_ObjectIdentity = ObjectIdentity
jnxEventNotifications = _JnxEventNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 13)
)
_JnxVccpNotifications_ObjectIdentity = ObjectIdentity
jnxVccpNotifications = _JnxVccpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 14)
)
_JnxOtnNotifications_ObjectIdentity = ObjectIdentity
jnxOtnNotifications = _JnxOtnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 15)
)
_JnxSAIDPNotifications_ObjectIdentity = ObjectIdentity
jnxSAIDPNotifications = _JnxSAIDPNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 16)
)
_JnxCosNotifications_ObjectIdentity = ObjectIdentity
jnxCosNotifications = _JnxCosNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 17)
)
_JnxDomNotifications_ObjectIdentity = ObjectIdentity
jnxDomNotifications = _JnxDomNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 18)
)
_JnxFabricChassisTraps_ObjectIdentity = ObjectIdentity
jnxFabricChassisTraps = _JnxFabricChassisTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 19)
)
_JnxFabricChassisOKTraps_ObjectIdentity = ObjectIdentity
jnxFabricChassisOKTraps = _JnxFabricChassisOKTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 20)
)
_JnxIfOtnNotifications_ObjectIdentity = ObjectIdentity
jnxIfOtnNotifications = _JnxIfOtnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 21)
)
_JnxOpticsNotifications_ObjectIdentity = ObjectIdentity
jnxOpticsNotifications = _JnxOpticsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 22)
)
_JnxFruTraps_ObjectIdentity = ObjectIdentity
jnxFruTraps = _JnxFruTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 23)
)
_JnxSnmpSetTraps_ObjectIdentity = ObjectIdentity
jnxSnmpSetTraps = _JnxSnmpSetTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 24)
)
_JnxExperiment_ObjectIdentity = ObjectIdentity
jnxExperiment = _JnxExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5)
)
_JnxNsm_ObjectIdentity = ObjectIdentity
jnxNsm = _JnxNsm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 6)
)
_JnxCA_ObjectIdentity = ObjectIdentity
jnxCA = _JnxCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 7)
)
_JnxAAA_ObjectIdentity = ObjectIdentity
jnxAAA = _JnxAAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 8)
)
_JnxAdvancedInsightMgr_ObjectIdentity = ObjectIdentity
jnxAdvancedInsightMgr = _JnxAdvancedInsightMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 9)
)
_JnxBxMibRoot_ObjectIdentity = ObjectIdentity
jnxBxMibRoot = _JnxBxMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 10)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-SMI",
    **{"juniperMIB": juniperMIB,
       "jnxProducts": jnxProducts,
       "jnxMediaFlow": jnxMediaFlow,
       "jnxJunosSpace": jnxJunosSpace,
       "jnxReservedProducts3": jnxReservedProducts3,
       "jnxReservedProducts4": jnxReservedProducts4,
       "jnxReservedProducts5": jnxReservedProducts5,
       "jnxSDKApplicationsRoot": jnxSDKApplicationsRoot,
       "jnxJAB": jnxJAB,
       "jnxStrm": jnxStrm,
       "jnxServices": jnxServices,
       "jnxMibs": jnxMibs,
       "jnxJsMibRoot": jnxJsMibRoot,
       "jnxExMibRoot": jnxExMibRoot,
       "jnxWxMibRoot": jnxWxMibRoot,
       "jnxDcfMibRoot": jnxDcfMibRoot,
       "jnxReservedMibs5": jnxReservedMibs5,
       "jnxPfeMibRoot": jnxPfeMibRoot,
       "jnxBfdMibRoot": jnxBfdMibRoot,
       "jnxXstpMibs": jnxXstpMibs,
       "jnxUtilMibRoot": jnxUtilMibRoot,
       "jnxl2aldMibRoot": jnxl2aldMibRoot,
       "jnxL2tpMibRoot": jnxL2tpMibRoot,
       "jnxRpmMibRoot": jnxRpmMibRoot,
       "jnxUserAAAMibRoot": jnxUserAAAMibRoot,
       "jnxIpSecMibRoot": jnxIpSecMibRoot,
       "jnxL2cpMibRoot": jnxL2cpMibRoot,
       "jnxPwTdmMibRoot": jnxPwTdmMibRoot,
       "jnxPwTCMibRoot": jnxPwTCMibRoot,
       "jnxOtnMibRoot": jnxOtnMibRoot,
       "jnxPsuMIBRoot": jnxPsuMIBRoot,
       "jnxSvcsMibRoot": jnxSvcsMibRoot,
       "jnxDomMibRoot": jnxDomMibRoot,
       "jnxJdhcpMibRoot": jnxJdhcpMibRoot,
       "jnxJdhcpv6MibRoot": jnxJdhcpv6MibRoot,
       "jnxLicenseMibRoot": jnxLicenseMibRoot,
       "jnxSubscriberMibRoot": jnxSubscriberMibRoot,
       "jnxMagMibRoot": jnxMagMibRoot,
       "jnxMobileGatewayMibRoot": jnxMobileGatewayMibRoot,
       "jnxPppoeMibRoot": jnxPppoeMibRoot,
       "jnxPppMibRoot": jnxPppMibRoot,
       "jnxJVAEMibRoot": jnxJVAEMibRoot,
       "jnxIfOtnMibRoot": jnxIfOtnMibRoot,
       "jnxOpticsMibRoot": jnxOpticsMibRoot,
       "jnxAlarmExtMibRoot": jnxAlarmExtMibRoot,
       "jnxoptIfMibRoot": jnxoptIfMibRoot,
       "jnxFruMibRoot": jnxFruMibRoot,
       "jnxTimingNotfnsMIBRoot": jnxTimingNotfnsMIBRoot,
       "jnxSnmpSetMibRoot": jnxSnmpSetMibRoot,
       "jnxTraps": jnxTraps,
       "jnxChassisTraps": jnxChassisTraps,
       "jnxChassisOKTraps": jnxChassisOKTraps,
       "jnxRmonTraps": jnxRmonTraps,
       "jnxLdpTraps": jnxLdpTraps,
       "jnxCmNotifications": jnxCmNotifications,
       "jnxSonetNotifications": jnxSonetNotifications,
       "jnxPMonNotifications": jnxPMonNotifications,
       "jnxCollectorNotifications": jnxCollectorNotifications,
       "jnxPingNotifications": jnxPingNotifications,
       "jnxSpNotifications": jnxSpNotifications,
       "jnxDfcNotifications": jnxDfcNotifications,
       "jnxSyslogNotifications": jnxSyslogNotifications,
       "jnxEventNotifications": jnxEventNotifications,
       "jnxVccpNotifications": jnxVccpNotifications,
       "jnxOtnNotifications": jnxOtnNotifications,
       "jnxSAIDPNotifications": jnxSAIDPNotifications,
       "jnxCosNotifications": jnxCosNotifications,
       "jnxDomNotifications": jnxDomNotifications,
       "jnxFabricChassisTraps": jnxFabricChassisTraps,
       "jnxFabricChassisOKTraps": jnxFabricChassisOKTraps,
       "jnxIfOtnNotifications": jnxIfOtnNotifications,
       "jnxOpticsNotifications": jnxOpticsNotifications,
       "jnxFruTraps": jnxFruTraps,
       "jnxSnmpSetTraps": jnxSnmpSetTraps,
       "jnxExperiment": jnxExperiment,
       "jnxNsm": jnxNsm,
       "jnxCA": jnxCA,
       "jnxAAA": jnxAAA,
       "jnxAdvancedInsightMgr": jnxAdvancedInsightMgr,
       "jnxBxMibRoot": jnxBxMibRoot}
)
