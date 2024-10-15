# SNMP MIB module (WS-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WS-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:25 2024
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

symbol = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 388)
)
symbol.setRevisions(
        ("2006-05-24 13:46",
         "2005-09-24 23:37",
         "2005-07-07 12:02",
         "2005-05-17 11:07",
         "2005-05-05 11:11",
         "2005-05-04 10:22")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Spectrum24_ObjectIdentity = ObjectIdentity
spectrum24 = _Spectrum24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 1)
)
_Wnms_ObjectIdentity = ObjectIdentity
wnms = _Wnms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 2)
)
_Wlan_ObjectIdentity = ObjectIdentity
wlan = _Wlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 3)
)
_CustomProducts1_ObjectIdentity = ObjectIdentity
customProducts1 = _CustomProducts1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 4)
)
_CustomProducts2_ObjectIdentity = ObjectIdentity
customProducts2 = _CustomProducts2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 5)
)
_Ws5000_ObjectIdentity = ObjectIdentity
ws5000 = _Ws5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 6)
)
_SymbolProducts_ObjectIdentity = ObjectIdentity
symbolProducts = _SymbolProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 7)
)
_Uk_ObjectIdentity = ObjectIdentity
uk = _Uk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 8)
)
_Emm_ObjectIdentity = ObjectIdentity
emm = _Emm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 9)
)
_Mk_ObjectIdentity = ObjectIdentity
mk = _Mk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 10)
)
_Wsd_ObjectIdentity = ObjectIdentity
wsd = _Wsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11)
)
_Sysoids_ObjectIdentity = ObjectIdentity
sysoids = _Sysoids_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 1)
)
_Ws2000_ObjectIdentity = ObjectIdentity
ws2000 = _Ws2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 1, 1)
)
if mibBuilder.loadTexts:
    ws2000.setStatus("current")
_Ap513_ObjectIdentity = ObjectIdentity
ap513 = _Ap513_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 1, 2)
)
if mibBuilder.loadTexts:
    ap513.setStatus("current")
_Pinnacle_ObjectIdentity = ObjectIdentity
pinnacle = _Pinnacle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 1, 3)
)
if mibBuilder.loadTexts:
    pinnacle.setStatus("current")
_WsdProduct_ObjectIdentity = ObjectIdentity
wsdProduct = _WsdProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 3)
)
if mibBuilder.loadTexts:
    wsdProduct.setStatus("current")
_WsdFeature_ObjectIdentity = ObjectIdentity
wsdFeature = _WsdFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 11, 4)
)
if mibBuilder.loadTexts:
    wsdFeature.setStatus("current")
_Ws_ObjectIdentity = ObjectIdentity
ws = _Ws_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14)
)
_WsInfra_ObjectIdentity = ObjectIdentity
wsInfra = _WsInfra_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1)
)
_WsSw_ObjectIdentity = ObjectIdentity
wsSw = _WsSw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 2)
)
_WsCc_ObjectIdentity = ObjectIdentity
wsCc = _WsCc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 3)
)
_WsMgmt_ObjectIdentity = ObjectIdentity
wsMgmt = _WsMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 4)
)
_WsTrap_ObjectIdentity = ObjectIdentity
wsTrap = _WsTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 5)
)
_WsSec_ObjectIdentity = ObjectIdentity
wsSec = _WsSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WS-SMI",
    **{"symbol": symbol,
       "spectrum24": spectrum24,
       "wnms": wnms,
       "wlan": wlan,
       "customProducts1": customProducts1,
       "customProducts2": customProducts2,
       "ws5000": ws5000,
       "symbolProducts": symbolProducts,
       "uk": uk,
       "emm": emm,
       "mk": mk,
       "wsd": wsd,
       "sysoids": sysoids,
       "ws2000": ws2000,
       "ap513": ap513,
       "pinnacle": pinnacle,
       "wsdProduct": wsdProduct,
       "wsdFeature": wsdFeature,
       "ws": ws,
       "wsInfra": wsInfra,
       "wsSw": wsSw,
       "wsCc": wsCc,
       "wsMgmt": wsMgmt,
       "wsTrap": wsTrap,
       "wsSec": wsSec}
)
