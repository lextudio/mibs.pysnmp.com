# SNMP MIB module (TPT-SMSMIBS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPT-SMSMIBS
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:10 2024
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

tpt_smsMIBs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tpt_sms_family_ObjectIdentity = ObjectIdentity
tpt_sms_family = _Tpt_sms_family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 4)
)
if mibBuilder.loadTexts:
    tpt_sms_family.setStatus("current")
_Tpt_sms_model_1750_ObjectIdentity = ObjectIdentity
tpt_sms_model_1750 = _Tpt_sms_model_1750_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tpt_sms_model_1750.setStatus("deprecated")
_Tpt_sms_model_1850_ObjectIdentity = ObjectIdentity
tpt_sms_model_1850 = _Tpt_sms_model_1850_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 4, 2)
)
if mibBuilder.loadTexts:
    tpt_sms_model_1850.setStatus("deprecated")
_Tpt_sms_model_1950_ObjectIdentity = ObjectIdentity
tpt_sms_model_1950 = _Tpt_sms_model_1950_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 4, 3)
)
if mibBuilder.loadTexts:
    tpt_sms_model_1950.setStatus("deprecated")
_Tpt_sms_model_vmware_ObjectIdentity = ObjectIdentity
tpt_sms_model_vmware = _Tpt_sms_model_vmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 4, 4)
)
if mibBuilder.loadTexts:
    tpt_sms_model_vmware.setStatus("deprecated")
_Tpt_sms_model_h1_ObjectIdentity = ObjectIdentity
tpt_sms_model_h1 = _Tpt_sms_model_h1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 4, 5)
)
if mibBuilder.loadTexts:
    tpt_sms_model_h1.setStatus("current")
_Tpt_sms_model_xl_ObjectIdentity = ObjectIdentity
tpt_sms_model_xl = _Tpt_sms_model_xl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 4, 6)
)
if mibBuilder.loadTexts:
    tpt_sms_model_xl.setStatus("current")
_Tpt_sms_model_vsms_ObjectIdentity = ObjectIdentity
tpt_sms_model_vsms = _Tpt_sms_model_vsms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 4, 7)
)
if mibBuilder.loadTexts:
    tpt_sms_model_vsms.setStatus("current")
_Tpt_sms_model_hp_2000_ObjectIdentity = ObjectIdentity
tpt_sms_model_hp_2000 = _Tpt_sms_model_hp_2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 4, 8)
)
if mibBuilder.loadTexts:
    tpt_sms_model_hp_2000.setStatus("current")
_Tpt_sms_model_hp_xl2000_ObjectIdentity = ObjectIdentity
tpt_sms_model_hp_xl2000 = _Tpt_sms_model_hp_xl2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 4, 9)
)
if mibBuilder.loadTexts:
    tpt_sms_model_hp_xl2000.setStatus("current")
_Tpt_sms_model_vsmslite_ObjectIdentity = ObjectIdentity
tpt_sms_model_vsmslite = _Tpt_sms_model_vsmslite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 4, 10)
)
if mibBuilder.loadTexts:
    tpt_sms_model_vsmslite.setStatus("current")
_Tpt_sms_model_h3_ObjectIdentity = ObjectIdentity
tpt_sms_model_h3 = _Tpt_sms_model_h3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 4, 11)
)
if mibBuilder.loadTexts:
    tpt_sms_model_h3.setStatus("current")
_Tpt_sms_model_h3_xl_ObjectIdentity = ObjectIdentity
tpt_sms_model_h3_xl = _Tpt_sms_model_h3_xl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 4, 12)
)
if mibBuilder.loadTexts:
    tpt_sms_model_h3_xl.setStatus("current")
_Tpt_sms_conf_ObjectIdentity = ObjectIdentity
tpt_sms_conf = _Tpt_sms_conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 1)
)
if mibBuilder.loadTexts:
    tpt_sms_conf.setStatus("current")
_Tpt_sms_groups_ObjectIdentity = ObjectIdentity
tpt_sms_groups = _Tpt_sms_groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    tpt_sms_groups.setStatus("current")
_Tpt_sms_compls_ObjectIdentity = ObjectIdentity
tpt_sms_compls = _Tpt_sms_compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 1, 2)
)
if mibBuilder.loadTexts:
    tpt_sms_compls.setStatus("current")
_Tpt_sms_objs_ObjectIdentity = ObjectIdentity
tpt_sms_objs = _Tpt_sms_objs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 2)
)
if mibBuilder.loadTexts:
    tpt_sms_objs.setStatus("current")
_Tpt_sms_events_ObjectIdentity = ObjectIdentity
tpt_sms_events = _Tpt_sms_events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3)
)
if mibBuilder.loadTexts:
    tpt_sms_events.setStatus("current")
_Tpt_sms_eventsV2_ObjectIdentity = ObjectIdentity
tpt_sms_eventsV2 = _Tpt_sms_eventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0)
)
if mibBuilder.loadTexts:
    tpt_sms_eventsV2.setStatus("current")
_Tpt_sms_notifypayload_ObjectIdentity = ObjectIdentity
tpt_sms_notifypayload = _Tpt_sms_notifypayload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1)
)
if mibBuilder.loadTexts:
    tpt_sms_notifypayload.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-SMSMIBS",
    **{"tpt-sms-family": tpt_sms_family,
       "tpt-sms-model-1750": tpt_sms_model_1750,
       "tpt-sms-model-1850": tpt_sms_model_1850,
       "tpt-sms-model-1950": tpt_sms_model_1950,
       "tpt-sms-model-vmware": tpt_sms_model_vmware,
       "tpt-sms-model-h1": tpt_sms_model_h1,
       "tpt-sms-model-xl": tpt_sms_model_xl,
       "tpt-sms-model-vsms": tpt_sms_model_vsms,
       "tpt-sms-model-hp-2000": tpt_sms_model_hp_2000,
       "tpt-sms-model-hp-xl2000": tpt_sms_model_hp_xl2000,
       "tpt-sms-model-vsmslite": tpt_sms_model_vsmslite,
       "tpt-sms-model-h3": tpt_sms_model_h3,
       "tpt-sms-model-h3-xl": tpt_sms_model_h3_xl,
       "tpt-smsMIBs": tpt_smsMIBs,
       "tpt-sms-conf": tpt_sms_conf,
       "tpt-sms-groups": tpt_sms_groups,
       "tpt-sms-compls": tpt_sms_compls,
       "tpt-sms-objs": tpt_sms_objs,
       "tpt-sms-events": tpt_sms_events,
       "tpt-sms-eventsV2": tpt_sms_eventsV2,
       "tpt-sms-notifypayload": tpt_sms_notifypayload}
)
