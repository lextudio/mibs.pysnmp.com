# SNMP MIB module (TPT-TPAMIBS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPT-TPAMIBS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:54 2024
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

(tpt_products,
 tpt_reg) = mibBuilder.importSymbols(
    "TIPPINGPOINT-REG-MIB",
    "tpt-products",
    "tpt-reg")


# MODULE-IDENTITY

tpt_tpaMIBs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3)
)
tpt_tpaMIBs.setRevisions(
        ("2016-06-08 17:24",
         "2016-05-25 18:54")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tpt_tpa_family_ObjectIdentity = ObjectIdentity
tpt_tpa_family = _Tpt_tpa_family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3)
)
if mibBuilder.loadTexts:
    tpt_tpa_family.setStatus("current")
_Tpt_model_2000_ObjectIdentity = ObjectIdentity
tpt_model_2000 = _Tpt_model_2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tpt_model_2000.setStatus("current")
_Tpt_model_600_ObjectIdentity = ObjectIdentity
tpt_model_600 = _Tpt_model_600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tpt_model_600.setStatus("current")
_Tpt_model_600A_ObjectIdentity = ObjectIdentity
tpt_model_600A = _Tpt_model_600A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 4)
)
if mibBuilder.loadTexts:
    tpt_model_600A.setStatus("current")
_Tpt_model_400_ObjectIdentity = ObjectIdentity
tpt_model_400 = _Tpt_model_400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 5)
)
if mibBuilder.loadTexts:
    tpt_model_400.setStatus("current")
_Tpt_model_50_ObjectIdentity = ObjectIdentity
tpt_model_50 = _Tpt_model_50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 6)
)
if mibBuilder.loadTexts:
    tpt_model_50.setStatus("current")
_Tpt_model_1200_ObjectIdentity = ObjectIdentity
tpt_model_1200 = _Tpt_model_1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 7)
)
if mibBuilder.loadTexts:
    tpt_model_1200.setStatus("current")
_Tpt_model_2400_ObjectIdentity = ObjectIdentity
tpt_model_2400 = _Tpt_model_2400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 8)
)
if mibBuilder.loadTexts:
    tpt_model_2400.setStatus("current")
_Tpt_model_5000_ObjectIdentity = ObjectIdentity
tpt_model_5000 = _Tpt_model_5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 9)
)
if mibBuilder.loadTexts:
    tpt_model_5000.setStatus("current")
_Tpt_model_200_ObjectIdentity = ObjectIdentity
tpt_model_200 = _Tpt_model_200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 10)
)
if mibBuilder.loadTexts:
    tpt_model_200.setStatus("current")
_Tpt_model_10_ObjectIdentity = ObjectIdentity
tpt_model_10 = _Tpt_model_10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 11)
)
if mibBuilder.loadTexts:
    tpt_model_10.setStatus("current")
_Tpt_model_100_ObjectIdentity = ObjectIdentity
tpt_model_100 = _Tpt_model_100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 12)
)
if mibBuilder.loadTexts:
    tpt_model_100.setStatus("current")
_Tpt_model_X505_ObjectIdentity = ObjectIdentity
tpt_model_X505 = _Tpt_model_X505_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 13)
)
if mibBuilder.loadTexts:
    tpt_model_X505.setStatus("current")
_Tpt_model_X5_ObjectIdentity = ObjectIdentity
tpt_model_X5 = _Tpt_model_X5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 14)
)
if mibBuilder.loadTexts:
    tpt_model_X5.setStatus("current")
_Tpt_model_T200_ObjectIdentity = ObjectIdentity
tpt_model_T200 = _Tpt_model_T200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 15)
)
if mibBuilder.loadTexts:
    tpt_model_T200.setStatus("current")
_Tpt_model_X506_ObjectIdentity = ObjectIdentity
tpt_model_X506 = _Tpt_model_X506_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 16)
)
if mibBuilder.loadTexts:
    tpt_model_X506.setStatus("current")
_Tpt_model_X5_25_ObjectIdentity = ObjectIdentity
tpt_model_X5_25 = _Tpt_model_X5_25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 17)
)
if mibBuilder.loadTexts:
    tpt_model_X5_25.setStatus("current")
_Tpt_model_X710_ObjectIdentity = ObjectIdentity
tpt_model_X710 = _Tpt_model_X710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 18)
)
if mibBuilder.loadTexts:
    tpt_model_X710.setStatus("current")
_Tpt_model_T210E_ObjectIdentity = ObjectIdentity
tpt_model_T210E = _Tpt_model_T210E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 19)
)
if mibBuilder.loadTexts:
    tpt_model_T210E.setStatus("current")
_Tpt_model_T600E_ObjectIdentity = ObjectIdentity
tpt_model_T600E = _Tpt_model_T600E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 20)
)
if mibBuilder.loadTexts:
    tpt_model_T600E.setStatus("current")
_Tpt_model_T1000E_ObjectIdentity = ObjectIdentity
tpt_model_T1000E = _Tpt_model_T1000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 21)
)
if mibBuilder.loadTexts:
    tpt_model_T1000E.setStatus("current")
_Tpt_model_T2000E_ObjectIdentity = ObjectIdentity
tpt_model_T2000E = _Tpt_model_T2000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 22)
)
if mibBuilder.loadTexts:
    tpt_model_T2000E.setStatus("current")
_Tpt_model_T5000E_ObjectIdentity = ObjectIdentity
tpt_model_T5000E = _Tpt_model_T5000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 23)
)
if mibBuilder.loadTexts:
    tpt_model_T5000E.setStatus("current")
_Tpt_model_660N_ObjectIdentity = ObjectIdentity
tpt_model_660N = _Tpt_model_660N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 27)
)
if mibBuilder.loadTexts:
    tpt_model_660N.setStatus("current")
_Tpt_model_1400N_ObjectIdentity = ObjectIdentity
tpt_model_1400N = _Tpt_model_1400N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 28)
)
if mibBuilder.loadTexts:
    tpt_model_1400N.setStatus("current")
_Tpt_model_2500N_ObjectIdentity = ObjectIdentity
tpt_model_2500N = _Tpt_model_2500N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 29)
)
if mibBuilder.loadTexts:
    tpt_model_2500N.setStatus("current")
_Tpt_model_5100N_ObjectIdentity = ObjectIdentity
tpt_model_5100N = _Tpt_model_5100N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 30)
)
if mibBuilder.loadTexts:
    tpt_model_5100N.setStatus("current")
_Tpt_model_110_ObjectIdentity = ObjectIdentity
tpt_model_110 = _Tpt_model_110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 31)
)
if mibBuilder.loadTexts:
    tpt_model_110.setStatus("current")
_Tpt_model_330_ObjectIdentity = ObjectIdentity
tpt_model_330 = _Tpt_model_330_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 32)
)
if mibBuilder.loadTexts:
    tpt_model_330.setStatus("current")
_Tpt_model_SB1200N_ObjectIdentity = ObjectIdentity
tpt_model_SB1200N = _Tpt_model_SB1200N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 33)
)
if mibBuilder.loadTexts:
    tpt_model_SB1200N.setStatus("current")
_Tpt_model_6100N_ObjectIdentity = ObjectIdentity
tpt_model_6100N = _Tpt_model_6100N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 34)
)
if mibBuilder.loadTexts:
    tpt_model_6100N.setStatus("current")
_Tpt_model_7100NX_ObjectIdentity = ObjectIdentity
tpt_model_7100NX = _Tpt_model_7100NX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 35)
)
if mibBuilder.loadTexts:
    tpt_model_7100NX.setStatus("current")
_Tpt_model_5200NX_ObjectIdentity = ObjectIdentity
tpt_model_5200NX = _Tpt_model_5200NX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 36)
)
if mibBuilder.loadTexts:
    tpt_model_5200NX.setStatus("current")
_Tpt_model_2600NX_ObjectIdentity = ObjectIdentity
tpt_model_2600NX = _Tpt_model_2600NX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 44)
)
if mibBuilder.loadTexts:
    tpt_model_2600NX.setStatus("current")
_Tpt_model_6200NX_ObjectIdentity = ObjectIdentity
tpt_model_6200NX = _Tpt_model_6200NX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 45)
)
if mibBuilder.loadTexts:
    tpt_model_6200NX.setStatus("current")
_Tpt_model_7500NX_ObjectIdentity = ObjectIdentity
tpt_model_7500NX = _Tpt_model_7500NX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 46)
)
if mibBuilder.loadTexts:
    tpt_model_7500NX.setStatus("current")
_Tpt_model_440T_IPS_ObjectIdentity = ObjectIdentity
tpt_model_440T_IPS = _Tpt_model_440T_IPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 47)
)
if mibBuilder.loadTexts:
    tpt_model_440T_IPS.setStatus("current")
_Tpt_model_2200T_IPS_ObjectIdentity = ObjectIdentity
tpt_model_2200T_IPS = _Tpt_model_2200T_IPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 48)
)
if mibBuilder.loadTexts:
    tpt_model_2200T_IPS.setStatus("current")
_Tpt_model_VTPS_Standard_IPS_ObjectIdentity = ObjectIdentity
tpt_model_VTPS_Standard_IPS = _Tpt_model_VTPS_Standard_IPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 49)
)
if mibBuilder.loadTexts:
    tpt_model_VTPS_Standard_IPS.setStatus("current")
_Tpt_model_VTPS_Trial_IPS_ObjectIdentity = ObjectIdentity
tpt_model_VTPS_Trial_IPS = _Tpt_model_VTPS_Trial_IPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 3, 50)
)
if mibBuilder.loadTexts:
    tpt_model_VTPS_Trial_IPS.setStatus("current")
_Tpt_tpa_conf_ObjectIdentity = ObjectIdentity
tpt_tpa_conf = _Tpt_tpa_conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 1)
)
if mibBuilder.loadTexts:
    tpt_tpa_conf.setStatus("current")
_Tpt_tpa_groups_ObjectIdentity = ObjectIdentity
tpt_tpa_groups = _Tpt_tpa_groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tpt_tpa_groups.setStatus("current")
_Tpt_tpa_compls_ObjectIdentity = ObjectIdentity
tpt_tpa_compls = _Tpt_tpa_compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    tpt_tpa_compls.setStatus("current")
_Tpt_tpa_objs_ObjectIdentity = ObjectIdentity
tpt_tpa_objs = _Tpt_tpa_objs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2)
)
if mibBuilder.loadTexts:
    tpt_tpa_objs.setStatus("current")
_Tpt_tpa_events_ObjectIdentity = ObjectIdentity
tpt_tpa_events = _Tpt_tpa_events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3)
)
if mibBuilder.loadTexts:
    tpt_tpa_events.setStatus("current")
_Tpt_tpa_eventsV2_ObjectIdentity = ObjectIdentity
tpt_tpa_eventsV2 = _Tpt_tpa_eventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0)
)
if mibBuilder.loadTexts:
    tpt_tpa_eventsV2.setStatus("current")
_Tpt_tpa_unkparams_ObjectIdentity = ObjectIdentity
tpt_tpa_unkparams = _Tpt_tpa_unkparams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    tpt_tpa_unkparams.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-TPAMIBS-MIB",
    **{"tpt-tpa-family": tpt_tpa_family,
       "tpt-model-2000": tpt_model_2000,
       "tpt-model-600": tpt_model_600,
       "tpt-model-600A": tpt_model_600A,
       "tpt-model-400": tpt_model_400,
       "tpt-model-50": tpt_model_50,
       "tpt-model-1200": tpt_model_1200,
       "tpt-model-2400": tpt_model_2400,
       "tpt-model-5000": tpt_model_5000,
       "tpt-model-200": tpt_model_200,
       "tpt-model-10": tpt_model_10,
       "tpt-model-100": tpt_model_100,
       "tpt-model-X505": tpt_model_X505,
       "tpt-model-X5": tpt_model_X5,
       "tpt-model-T200": tpt_model_T200,
       "tpt-model-X506": tpt_model_X506,
       "tpt-model-X5-25": tpt_model_X5_25,
       "tpt-model-X710": tpt_model_X710,
       "tpt-model-T210E": tpt_model_T210E,
       "tpt-model-T600E": tpt_model_T600E,
       "tpt-model-T1000E": tpt_model_T1000E,
       "tpt-model-T2000E": tpt_model_T2000E,
       "tpt-model-T5000E": tpt_model_T5000E,
       "tpt-model-660N": tpt_model_660N,
       "tpt-model-1400N": tpt_model_1400N,
       "tpt-model-2500N": tpt_model_2500N,
       "tpt-model-5100N": tpt_model_5100N,
       "tpt-model-110": tpt_model_110,
       "tpt-model-330": tpt_model_330,
       "tpt-model-SB1200N": tpt_model_SB1200N,
       "tpt-model-6100N": tpt_model_6100N,
       "tpt-model-7100NX": tpt_model_7100NX,
       "tpt-model-5200NX": tpt_model_5200NX,
       "tpt-model-2600NX": tpt_model_2600NX,
       "tpt-model-6200NX": tpt_model_6200NX,
       "tpt-model-7500NX": tpt_model_7500NX,
       "tpt-model-440T-IPS": tpt_model_440T_IPS,
       "tpt-model-2200T-IPS": tpt_model_2200T_IPS,
       "tpt-model-VTPS-Standard-IPS": tpt_model_VTPS_Standard_IPS,
       "tpt-model-VTPS-Trial-IPS": tpt_model_VTPS_Trial_IPS,
       "tpt-tpaMIBs": tpt_tpaMIBs,
       "tpt-tpa-conf": tpt_tpa_conf,
       "tpt-tpa-groups": tpt_tpa_groups,
       "tpt-tpa-compls": tpt_tpa_compls,
       "tpt-tpa-objs": tpt_tpa_objs,
       "tpt-tpa-events": tpt_tpa_events,
       "tpt-tpa-eventsV2": tpt_tpa_eventsV2,
       "tpt-tpa-unkparams": tpt_tpa_unkparams}
)
