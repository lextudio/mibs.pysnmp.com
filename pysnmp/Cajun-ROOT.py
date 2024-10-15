# SNMP MIB module (Cajun-ROOT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Cajun-ROOT
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:50 2024
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

cajunRtr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lucent_ObjectIdentity = ObjectIdentity
lucent = _Lucent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1)
)
_CajunRtrProduct_ObjectIdentity = ObjectIdentity
cajunRtrProduct = _CajunRtrProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 43)
)
_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2)
)
_CjnSystem_ObjectIdentity = ObjectIdentity
cjnSystem = _CjnSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 1)
)
_CjnCli_ObjectIdentity = ObjectIdentity
cjnCli = _CjnCli_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 1, 1)
)
_CjnDload_ObjectIdentity = ObjectIdentity
cjnDload = _CjnDload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 1, 2)
)
_CjnProtocol_ObjectIdentity = ObjectIdentity
cjnProtocol = _CjnProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2)
)
_CjnIpv4_ObjectIdentity = ObjectIdentity
cjnIpv4 = _CjnIpv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1)
)
_CjnIpv6_ObjectIdentity = ObjectIdentity
cjnIpv6 = _CjnIpv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 2)
)
_CjnIpx_ObjectIdentity = ObjectIdentity
cjnIpx = _CjnIpx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3)
)
_CjnAtalk_ObjectIdentity = ObjectIdentity
cjnAtalk = _CjnAtalk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4)
)
_CjnIpv4Serv_ObjectIdentity = ObjectIdentity
cjnIpv4Serv = _CjnIpv4Serv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5)
)
_CjnIpv6Serv_ObjectIdentity = ObjectIdentity
cjnIpv6Serv = _CjnIpv6Serv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 6)
)
_CjnIpxServ_ObjectIdentity = ObjectIdentity
cjnIpxServ = _CjnIpxServ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 7)
)
_CjnAtalkServ_ObjectIdentity = ObjectIdentity
cjnAtalkServ = _CjnAtalkServ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 8)
)
_CjnOspf_ObjectIdentity = ObjectIdentity
cjnOspf = _CjnOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9)
)
_CjnRip_ObjectIdentity = ObjectIdentity
cjnRip = _CjnRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10)
)
_CjnIgmp_ObjectIdentity = ObjectIdentity
cjnIgmp = _CjnIgmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11)
)
_CjnRtm_ObjectIdentity = ObjectIdentity
cjnRtm = _CjnRtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 12)
)
_CjnDvmrp_ObjectIdentity = ObjectIdentity
cjnDvmrp = _CjnDvmrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13)
)
_CjnPimSm_ObjectIdentity = ObjectIdentity
cjnPimSm = _CjnPimSm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 14)
)
_CjnPimDm_ObjectIdentity = ObjectIdentity
cjnPimDm = _CjnPimDm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 15)
)
_CjnRsvp_ObjectIdentity = ObjectIdentity
cjnRsvp = _CjnRsvp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 16)
)
_CjnSnmp_ObjectIdentity = ObjectIdentity
cjnSnmp = _CjnSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 17)
)
_CjnBgp_ObjectIdentity = ObjectIdentity
cjnBgp = _CjnBgp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 18)
)
_CjnLrrp_ObjectIdentity = ObjectIdentity
cjnLrrp = _CjnLrrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19)
)
_CjnIpxRip_ObjectIdentity = ObjectIdentity
cjnIpxRip = _CjnIpxRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20)
)
_CjnIpxSap_ObjectIdentity = ObjectIdentity
cjnIpxSap = _CjnIpxSap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21)
)
_CjnMgmt_ObjectIdentity = ObjectIdentity
cjnMgmt = _CjnMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3)
)
_CjnIpIfMgmt_ObjectIdentity = ObjectIdentity
cjnIpIfMgmt = _CjnIpIfMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1)
)
_CjnIpxIfMgmt_ObjectIdentity = ObjectIdentity
cjnIpxIfMgmt = _CjnIpxIfMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 2)
)
_CjnAtalkIfMgmt_ObjectIdentity = ObjectIdentity
cjnAtalkIfMgmt = _CjnAtalkIfMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 3)
)
_CjnResourceMgr_ObjectIdentity = ObjectIdentity
cjnResourceMgr = _CjnResourceMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 4)
)
_CjnIpAListMgmt_ObjectIdentity = ObjectIdentity
cjnIpAListMgmt = _CjnIpAListMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5)
)
_CjnIpForwardCtlMgt_ObjectIdentity = ObjectIdentity
cjnIpForwardCtlMgt = _CjnIpForwardCtlMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 6)
)
_CjnIpFwdMgmt_ObjectIdentity = ObjectIdentity
cjnIpFwdMgmt = _CjnIpFwdMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 7)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Cajun-ROOT",
    **{"lucent": lucent,
       "products": products,
       "cajunRtrProduct": cajunRtrProduct,
       "mibs": mibs,
       "cajunRtr": cajunRtr,
       "cjnSystem": cjnSystem,
       "cjnCli": cjnCli,
       "cjnDload": cjnDload,
       "cjnProtocol": cjnProtocol,
       "cjnIpv4": cjnIpv4,
       "cjnIpv6": cjnIpv6,
       "cjnIpx": cjnIpx,
       "cjnAtalk": cjnAtalk,
       "cjnIpv4Serv": cjnIpv4Serv,
       "cjnIpv6Serv": cjnIpv6Serv,
       "cjnIpxServ": cjnIpxServ,
       "cjnAtalkServ": cjnAtalkServ,
       "cjnOspf": cjnOspf,
       "cjnRip": cjnRip,
       "cjnIgmp": cjnIgmp,
       "cjnRtm": cjnRtm,
       "cjnDvmrp": cjnDvmrp,
       "cjnPimSm": cjnPimSm,
       "cjnPimDm": cjnPimDm,
       "cjnRsvp": cjnRsvp,
       "cjnSnmp": cjnSnmp,
       "cjnBgp": cjnBgp,
       "cjnLrrp": cjnLrrp,
       "cjnIpxRip": cjnIpxRip,
       "cjnIpxSap": cjnIpxSap,
       "cjnMgmt": cjnMgmt,
       "cjnIpIfMgmt": cjnIpIfMgmt,
       "cjnIpxIfMgmt": cjnIpxIfMgmt,
       "cjnAtalkIfMgmt": cjnAtalkIfMgmt,
       "cjnResourceMgr": cjnResourceMgr,
       "cjnIpAListMgmt": cjnIpAListMgmt,
       "cjnIpForwardCtlMgt": cjnIpForwardCtlMgt,
       "cjnIpFwdMgmt": cjnIpFwdMgmt}
)
