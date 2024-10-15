# SNMP MIB module (HPN-ICF-PRODUCT-ID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-PRODUCT-ID-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:32 2024
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

(nm,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "nm")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpSystem_ObjectIdentity = ObjectIdentity
hpSystem = _HpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3)
)
_NetElement_ObjectIdentity = ObjectIdentity
netElement = _NetElement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7)
)
_Hpn_ObjectIdentity = ObjectIdentity
hpn = _Hpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 15)
)
_HpnProducts_ObjectIdentity = ObjectIdentity
hpnProducts = _HpnProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 15, 1)
)
_HpnSwitch_ObjectIdentity = ObjectIdentity
hpnSwitch = _HpnSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 15, 1, 1)
)
_HpnRouter_ObjectIdentity = ObjectIdentity
hpnRouter = _HpnRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 15, 1, 2)
)
_HpnWireless_ObjectIdentity = ObjectIdentity
hpnWireless = _HpnWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 15, 1, 3)
)
_HpnLSU3WCMD0_ObjectIdentity = ObjectIdentity
hpnLSU3WCMD0 = _HpnLSU3WCMD0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 15, 1, 3, 1)
)
_Hpn83024P_ObjectIdentity = ObjectIdentity
hpn83024P = _Hpn83024P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 15, 1, 3, 2)
)
_Hpn83024PLSW_ObjectIdentity = ObjectIdentity
hpn83024PLSW = _Hpn83024PLSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 15, 1, 3, 3)
)
_Hpn8308P_ObjectIdentity = ObjectIdentity
hpn8308P = _Hpn8308P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 15, 1, 3, 4)
)
_Hpn8308PLSW_ObjectIdentity = ObjectIdentity
hpn8308PLSW = _Hpn8308PLSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 15, 1, 3, 5)
)
_HpnLSU3WCMD0TAA_ObjectIdentity = ObjectIdentity
hpnLSU3WCMD0TAA = _HpnLSU3WCMD0TAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 15, 1, 3, 6)
)
_Hpn83024PTAA_ObjectIdentity = ObjectIdentity
hpn83024PTAA = _Hpn83024PTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 15, 1, 3, 7)
)
_Hpn83024PTAALSW_ObjectIdentity = ObjectIdentity
hpn83024PTAALSW = _Hpn83024PTAALSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 15, 1, 3, 8)
)
_Hpn8308PTAA_ObjectIdentity = ObjectIdentity
hpn8308PTAA = _Hpn8308PTAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 15, 1, 3, 9)
)
_Hpn8308PTAALSW_ObjectIdentity = ObjectIdentity
hpn8308PTAALSW = _Hpn8308PTAALSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 15, 1, 3, 10)
)
_Hpn870WCM_ObjectIdentity = ObjectIdentity
hpn870WCM = _Hpn870WCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 15, 1, 3, 11)
)
_Hpn870LSW_ObjectIdentity = ObjectIdentity
hpn870LSW = _Hpn870LSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 15, 1, 3, 12)
)
_Hpn850_ObjectIdentity = ObjectIdentity
hpn850 = _Hpn850_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 15, 1, 3, 13)
)
_Hpn870TAAWCM_ObjectIdentity = ObjectIdentity
hpn870TAAWCM = _Hpn870TAAWCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 15, 1, 3, 14)
)
_Hpn870TAALSW_ObjectIdentity = ObjectIdentity
hpn870TAALSW = _Hpn870TAALSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 15, 1, 3, 15)
)
_Hpn850TAA_ObjectIdentity = ObjectIdentity
hpn850TAA = _Hpn850TAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 15, 1, 3, 16)
)
_HpnSecurity_ObjectIdentity = ObjectIdentity
hpnSecurity = _HpnSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 15, 1, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-PRODUCT-ID-MIB",
    **{"hpSystem": hpSystem,
       "netElement": netElement,
       "hpn": hpn,
       "hpnProducts": hpnProducts,
       "hpnSwitch": hpnSwitch,
       "hpnRouter": hpnRouter,
       "hpnWireless": hpnWireless,
       "hpnLSU3WCMD0": hpnLSU3WCMD0,
       "hpn83024P": hpn83024P,
       "hpn83024PLSW": hpn83024PLSW,
       "hpn8308P": hpn8308P,
       "hpn8308PLSW": hpn8308PLSW,
       "hpnLSU3WCMD0TAA": hpnLSU3WCMD0TAA,
       "hpn83024PTAA": hpn83024PTAA,
       "hpn83024PTAALSW": hpn83024PTAALSW,
       "hpn8308PTAA": hpn8308PTAA,
       "hpn8308PTAALSW": hpn8308PTAALSW,
       "hpn870WCM": hpn870WCM,
       "hpn870LSW": hpn870LSW,
       "hpn850": hpn850,
       "hpn870TAAWCM": hpn870TAAWCM,
       "hpn870TAALSW": hpn870TAALSW,
       "hpn850TAA": hpn850TAA,
       "hpnSecurity": hpnSecurity}
)
