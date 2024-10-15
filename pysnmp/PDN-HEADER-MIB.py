# SNMP MIB module (PDN-HEADER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-HEADER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:50 2024
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

_Pdyn_ObjectIdentity = ObjectIdentity
pdyn = _Pdyn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795)
)
_Pdn_products_ObjectIdentity = ObjectIdentity
pdn_products = _Pdn_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1)
)
_ParadyneNMS_products_ObjectIdentity = ObjectIdentity
paradyneNMS_products = _ParadyneNMS_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 13)
)
_Nms_6700_products_ObjectIdentity = ObjectIdentity
nms_6700_products = _Nms_6700_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 13, 2)
)
_Nms_dce_products_ObjectIdentity = ObjectIdentity
nms_dce_products = _Nms_dce_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 13, 3)
)
_Nms_gem_products_ObjectIdentity = ObjectIdentity
nms_gem_products = _Nms_gem_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 13, 4)
)
_Gem_aac_341_ObjectIdentity = ObjectIdentity
gem_aac_341 = _Gem_aac_341_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 13, 4, 1)
)
_Nms_logical_products_ObjectIdentity = ObjectIdentity
nms_logical_products = _Nms_logical_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 13, 5)
)
_Iso_physical_ObjectIdentity = ObjectIdentity
iso_physical = _Iso_physical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 13, 5, 1)
)
_Iso_link_ObjectIdentity = ObjectIdentity
iso_link = _Iso_link_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 13, 5, 2)
)
_Iso_network_ObjectIdentity = ObjectIdentity
iso_network = _Iso_network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 13, 5, 3)
)
_Access_router_ObjectIdentity = ObjectIdentity
access_router = _Access_router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 13, 5, 3, 1)
)
_Iso_transport_ObjectIdentity = ObjectIdentity
iso_transport = _Iso_transport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 13, 5, 4)
)
_Iso_session_ObjectIdentity = ObjectIdentity
iso_session = _Iso_session_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 13, 5, 5)
)
_Iso_presentation_ObjectIdentity = ObjectIdentity
iso_presentation = _Iso_presentation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 13, 5, 6)
)
_Iso_application_ObjectIdentity = ObjectIdentity
iso_application = _Iso_application_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 13, 5, 7)
)
_Chassis_manager_ObjectIdentity = ObjectIdentity
chassis_manager = _Chassis_manager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 13, 5, 7, 1)
)
_Paradyne_products_ObjectIdentity = ObjectIdentity
paradyne_products = _Paradyne_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14)
)
_Pdn_cellRelay_products_ObjectIdentity = ObjectIdentity
pdn_cellRelay_products = _Pdn_cellRelay_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 1)
)
_Pdn_snmp_products_ObjectIdentity = ObjectIdentity
pdn_snmp_products = _Pdn_snmp_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2)
)
_Csu_ObjectIdentity = ObjectIdentity
csu = _Csu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 1)
)
_T1_3150_ObjectIdentity = ObjectIdentity
t1_3150 = _T1_3150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 1, 1)
)
_T1_3151_ObjectIdentity = ObjectIdentity
t1_3151 = _T1_3151_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 1, 2)
)
_Dsu_csu_ObjectIdentity = ObjectIdentity
dsu_csu = _Dsu_csu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 2)
)
_T1_3160_ObjectIdentity = ObjectIdentity
t1_3160 = _T1_3160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 2, 1)
)
_T1_3164_ObjectIdentity = ObjectIdentity
t1_3164 = _T1_3164_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 2, 2)
)
_T1_3165_ObjectIdentity = ObjectIdentity
t1_3165 = _T1_3165_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 2, 3)
)
_T1_3161_ObjectIdentity = ObjectIdentity
t1_3161 = _T1_3161_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 2, 4)
)
_E1_3172_ObjectIdentity = ObjectIdentity
e1_3172 = _E1_3172_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 2, 5)
)
_E1_3174_ObjectIdentity = ObjectIdentity
e1_3174 = _E1_3174_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 2, 6)
)
_T1_3162_ObjectIdentity = ObjectIdentity
t1_3162 = _T1_3162_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 2, 7)
)
_T1_3166_ObjectIdentity = ObjectIdentity
t1_3166 = _T1_3166_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 2, 8)
)
_Ntu_ObjectIdentity = ObjectIdentity
ntu = _Ntu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 3)
)
_E1_3350_ObjectIdentity = ObjectIdentity
e1_3350 = _E1_3350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 3, 1)
)
_E1_3360_ObjectIdentity = ObjectIdentity
e1_3360 = _E1_3360_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 3, 2)
)
_E1_3364_ObjectIdentity = ObjectIdentity
e1_3364 = _E1_3364_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 3, 3)
)
_E1_3365_ObjectIdentity = ObjectIdentity
e1_3365 = _E1_3365_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 3, 4)
)
_Dev9XXX_ObjectIdentity = ObjectIdentity
dev9XXX = _Dev9XXX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4)
)
_Fr_96XX_ObjectIdentity = ObjectIdentity
fr_96XX = _Fr_96XX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 1)
)
_Fr_9620_ObjectIdentity = ObjectIdentity
fr_9620 = _Fr_9620_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 1, 1)
)
_Fr_2slot_ObjectIdentity = ObjectIdentity
fr_2slot = _Fr_2slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 1, 2)
)
_Fr_naf_ObjectIdentity = ObjectIdentity
fr_naf = _Fr_naf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 1, 3)
)
_Fr_nac_ObjectIdentity = ObjectIdentity
fr_nac = _Fr_nac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 1, 4)
)
_Fr_9624_ObjectIdentity = ObjectIdentity
fr_9624 = _Fr_9624_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 1, 5)
)
_Fr_9626_ObjectIdentity = ObjectIdentity
fr_9626 = _Fr_9626_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 1, 6)
)
_Fr_9623_ObjectIdentity = ObjectIdentity
fr_9623 = _Fr_9623_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 1, 7)
)
_Fr_9624_OS_ObjectIdentity = ObjectIdentity
fr_9624_OS = _Fr_9624_OS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 1, 8)
)
_Bonaire_ObjectIdentity = ObjectIdentity
bonaire = _Bonaire_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 2)
)
_Bonaire_1slot_ObjectIdentity = ObjectIdentity
bonaire_1slot = _Bonaire_1slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 2, 1)
)
_Bonaire_2slot_ObjectIdentity = ObjectIdentity
bonaire_2slot = _Bonaire_2slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 2, 2)
)
_Bonaire_naf_ObjectIdentity = ObjectIdentity
bonaire_naf = _Bonaire_naf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 2, 3)
)
_Bonaire_nac_ObjectIdentity = ObjectIdentity
bonaire_nac = _Bonaire_nac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 2, 4)
)
_T1_916X_ObjectIdentity = ObjectIdentity
t1_916X = _T1_916X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 3)
)
_T1_1slot_ObjectIdentity = ObjectIdentity
t1_1slot = _T1_1slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 3, 1)
)
_T1_9162_ObjectIdentity = ObjectIdentity
t1_9162 = _T1_9162_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 3, 2)
)
_T1_9165_ObjectIdentity = ObjectIdentity
t1_9165 = _T1_9165_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 3, 3)
)
_T1_nac_ObjectIdentity = ObjectIdentity
t1_nac = _T1_nac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 3, 4)
)
_T1_9262_ObjectIdentity = ObjectIdentity
t1_9262 = _T1_9262_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 3, 5)
)
_T1_9265_ObjectIdentity = ObjectIdentity
t1_9265 = _T1_9265_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 3, 6)
)
_T1_9161_ObjectIdentity = ObjectIdentity
t1_9161 = _T1_9161_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 3, 7)
)
_T1_9261_ObjectIdentity = ObjectIdentity
t1_9261 = _T1_9261_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 3, 8)
)
_T1fr_912X_ObjectIdentity = ObjectIdentity
t1fr_912X = _T1fr_912X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 4)
)
_T1fr_9121_ObjectIdentity = ObjectIdentity
t1fr_9121 = _T1fr_9121_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 4, 1)
)
_T1fr_2slot_ObjectIdentity = ObjectIdentity
t1fr_2slot = _T1fr_2slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 4, 2)
)
_T1fr_naf_ObjectIdentity = ObjectIdentity
t1fr_naf = _T1fr_naf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 4, 3)
)
_T1fr_nac_ObjectIdentity = ObjectIdentity
t1fr_nac = _T1fr_nac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 4, 4)
)
_T1fr_9124_ObjectIdentity = ObjectIdentity
t1fr_9124 = _T1fr_9124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 4, 5)
)
_T1fr_9124_NNI_ObjectIdentity = ObjectIdentity
t1fr_9124_NNI = _T1fr_9124_NNI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 4, 6)
)
_T1fr_9126_ObjectIdentity = ObjectIdentity
t1fr_9126 = _T1fr_9126_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 4, 7)
)
_T1fr_9128_ObjectIdentity = ObjectIdentity
t1fr_9128 = _T1fr_9128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 4, 8)
)
_T1fr_9124_II_ObjectIdentity = ObjectIdentity
t1fr_9124_II = _T1fr_9124_II_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 4, 9)
)
_T1fr_9124_L_ObjectIdentity = ObjectIdentity
t1fr_9124_L = _T1fr_9124_L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 4, 10)
)
_T1fr_9123_ObjectIdentity = ObjectIdentity
t1fr_9123 = _T1fr_9123_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 4, 11)
)
_T1fr_9124_OS_ObjectIdentity = ObjectIdentity
t1fr_9124_OS = _T1fr_9124_OS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 4, 12)
)
_Atm_95XX_ObjectIdentity = ObjectIdentity
atm_95XX = _Atm_95XX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 5)
)
_Atm_9580_ObjectIdentity = ObjectIdentity
atm_9580 = _Atm_9580_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 5, 1)
)
_Atm_9520_ilm_ObjectIdentity = ObjectIdentity
atm_9520_ilm = _Atm_9520_ilm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 5, 2)
)
_Atm_9520_ObjectIdentity = ObjectIdentity
atm_9520 = _Atm_9520_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 5, 3)
)
_Msa_919X_ObjectIdentity = ObjectIdentity
msa_919X = _Msa_919X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 6)
)
_Msa_9192_ObjectIdentity = ObjectIdentity
msa_9192 = _Msa_9192_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 6, 1)
)
_Msa_9195_ObjectIdentity = ObjectIdentity
msa_9195 = _Msa_9195_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 6, 2)
)
_Msa_9292_ObjectIdentity = ObjectIdentity
msa_9292 = _Msa_9292_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 6, 3)
)
_Msa_9295_ObjectIdentity = ObjectIdentity
msa_9295 = _Msa_9295_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 6, 4)
)
_Int_98XX_ObjectIdentity = ObjectIdentity
int_98XX = _Int_98XX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 7)
)
_Int_9820_ObjectIdentity = ObjectIdentity
int_9820 = _Int_9820_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 7, 1)
)
_Int_9820_C_ObjectIdentity = ObjectIdentity
int_9820_C = _Int_9820_C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 7, 2)
)
_Int_9820_8M_ObjectIdentity = ObjectIdentity
int_9820_8M = _Int_9820_8M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 7, 3)
)
_Int_9820_45M_ObjectIdentity = ObjectIdentity
int_9820_45M = _Int_9820_45M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 7, 4)
)
_Nni_9XXX_ObjectIdentity = ObjectIdentity
nni_9XXX = _Nni_9XXX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 8)
)
_Nni_9110_ObjectIdentity = ObjectIdentity
nni_9110 = _Nni_9110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 8, 1)
)
_Msdsl_9XXX_ObjectIdentity = ObjectIdentity
msdsl_9XXX = _Msdsl_9XXX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 9)
)
_Msdsl_9723_ObjectIdentity = ObjectIdentity
msdsl_9723 = _Msdsl_9723_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 9, 1)
)
_Msdsl_9783_ObjectIdentity = ObjectIdentity
msdsl_9783 = _Msdsl_9783_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 9, 2)
)
_Msdsl_9720_ObjectIdentity = ObjectIdentity
msdsl_9720 = _Msdsl_9720_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 9, 3)
)
_Msdsl_9788_ObjectIdentity = ObjectIdentity
msdsl_9788 = _Msdsl_9788_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 9, 4)
)
_Isdn_9XXX_ObjectIdentity = ObjectIdentity
isdn_9XXX = _Isdn_9XXX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 10)
)
_Isdn_9664_ObjectIdentity = ObjectIdentity
isdn_9664 = _Isdn_9664_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 10, 1)
)
_Rtr_9XXX_ObjectIdentity = ObjectIdentity
rtr_9XXX = _Rtr_9XXX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 11)
)
_Rtr_9783_ObjectIdentity = ObjectIdentity
rtr_9783 = _Rtr_9783_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 11, 1)
)
_Rtr_9720_ObjectIdentity = ObjectIdentity
rtr_9720 = _Rtr_9720_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 11, 2)
)
_Rtr_9788_ObjectIdentity = ObjectIdentity
rtr_9788 = _Rtr_9788_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 11, 3)
)
_Rtr_9126_ObjectIdentity = ObjectIdentity
rtr_9126 = _Rtr_9126_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 11, 4)
)
_Rtr_9123_ObjectIdentity = ObjectIdentity
rtr_9123 = _Rtr_9123_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 11, 5)
)
_Rtr_9623_ObjectIdentity = ObjectIdentity
rtr_9623 = _Rtr_9623_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 11, 6)
)
_T1_7XXX_ObjectIdentity = ObjectIdentity
t1_7XXX = _T1_7XXX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 12)
)
_T1_7123_ObjectIdentity = ObjectIdentity
t1_7123 = _T1_7123_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 4, 12, 1)
)
_Dev7XXX_ObjectIdentity = ObjectIdentity
dev7XXX = _Dev7XXX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 5)
)
_Dds_76XX_ObjectIdentity = ObjectIdentity
dds_76XX = _Dds_76XX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 5, 1)
)
_Dds_7610_ObjectIdentity = ObjectIdentity
dds_7610 = _Dds_7610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 5, 1, 1)
)
_Dds_7612_ObjectIdentity = ObjectIdentity
dds_7612 = _Dds_7612_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 5, 1, 2)
)
_Dds_7613_ObjectIdentity = ObjectIdentity
dds_7613 = _Dds_7613_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 5, 1, 3)
)
_T1_71XX_ObjectIdentity = ObjectIdentity
t1_71XX = _T1_71XX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 5, 2)
)
_T1_7110_ObjectIdentity = ObjectIdentity
t1_7110 = _T1_7110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 5, 2, 1)
)
_T1_7112_ObjectIdentity = ObjectIdentity
t1_7112 = _T1_7112_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 2, 5, 2, 2)
)
_Pdn_36xx_products_ObjectIdentity = ObjectIdentity
pdn_36xx_products = _Pdn_36xx_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 3)
)
_Pdn_aac_products_ObjectIdentity = ObjectIdentity
pdn_aac_products = _Pdn_aac_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 4)
)
_Aac_34_ObjectIdentity = ObjectIdentity
aac_34 = _Aac_34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 4, 1)
)
_Aac_34X_ObjectIdentity = ObjectIdentity
aac_34X = _Aac_34X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 4, 2)
)
_Aac_FL_ObjectIdentity = ObjectIdentity
aac_FL = _Aac_FL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 4, 2, 1)
)
_Aac_UE_ObjectIdentity = ObjectIdentity
aac_UE = _Aac_UE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 4, 2, 2)
)
_Aac_FP_ObjectIdentity = ObjectIdentity
aac_FP = _Aac_FP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 4, 2, 3)
)
_Aac_300_ObjectIdentity = ObjectIdentity
aac_300 = _Aac_300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 4, 2, 4)
)
_Aac_cards_ObjectIdentity = ObjectIdentity
aac_cards = _Aac_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 4, 3)
)
_Aac_frs_ObjectIdentity = ObjectIdentity
aac_frs = _Aac_frs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 4, 3, 1)
)
_Aac_ipc_ObjectIdentity = ObjectIdentity
aac_ipc = _Aac_ipc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 4, 3, 2)
)
_Aac_atm_ObjectIdentity = ObjectIdentity
aac_atm = _Aac_atm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 4, 3, 3)
)
_Aac_4X_ObjectIdentity = ObjectIdentity
aac_4X = _Aac_4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 4, 4)
)
_Aac_4XFL_ObjectIdentity = ObjectIdentity
aac_4XFL = _Aac_4XFL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 4, 4, 1)
)
_Aac_4XUE_ObjectIdentity = ObjectIdentity
aac_4XUE = _Aac_4XUE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 4, 4, 2)
)
_Aac_4XFP_ObjectIdentity = ObjectIdentity
aac_4XFP = _Aac_4XFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 4, 4, 3)
)
_Aac_4X300_ObjectIdentity = ObjectIdentity
aac_4X300 = _Aac_4X300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 4, 4, 4)
)
_Pdn_common_products_ObjectIdentity = ObjectIdentity
pdn_common_products = _Pdn_common_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 5)
)
_Pdn_testOIDs_ObjectIdentity = ObjectIdentity
pdn_testOIDs = _Pdn_testOIDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 5, 1)
)
_PdnLoopbackTest_ObjectIdentity = ObjectIdentity
pdnLoopbackTest = _PdnLoopbackTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 5, 1, 1)
)
_PdnBertTest_ObjectIdentity = ObjectIdentity
pdnBertTest = _PdnBertTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 5, 1, 2)
)
_PdnPingTest_ObjectIdentity = ObjectIdentity
pdnPingTest = _PdnPingTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 5, 1, 3)
)
_PdnTraceRouteTest_ObjectIdentity = ObjectIdentity
pdnTraceRouteTest = _PdnTraceRouteTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 5, 1, 4)
)
_PdnBlertTest_ObjectIdentity = ObjectIdentity
pdnBlertTest = _PdnBlertTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 5, 1, 5)
)
_Pdn_eagle_products_ObjectIdentity = ObjectIdentity
pdn_eagle_products = _Pdn_eagle_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 6)
)
_Pdn_ar_products_ObjectIdentity = ObjectIdentity
pdn_ar_products = _Pdn_ar_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 7)
)
_Ar_541_ObjectIdentity = ObjectIdentity
ar_541 = _Ar_541_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 7, 1)
)
_Ar_611_ObjectIdentity = ObjectIdentity
ar_611 = _Ar_611_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 7, 2)
)
_Ar_621_ObjectIdentity = ObjectIdentity
ar_621 = _Ar_621_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 7, 3)
)
_Ar_641_ObjectIdentity = ObjectIdentity
ar_641 = _Ar_641_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 7, 4)
)
_Ar_712_ObjectIdentity = ObjectIdentity
ar_712 = _Ar_712_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 7, 5)
)
_Ar_722_ObjectIdentity = ObjectIdentity
ar_722 = _Ar_722_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 7, 6)
)
_Ar_928_ObjectIdentity = ObjectIdentity
ar_928 = _Ar_928_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 7, 7)
)
_Ar_711_ObjectIdentity = ObjectIdentity
ar_711 = _Ar_711_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 7, 8)
)
_Pdn_as_products_ObjectIdentity = ObjectIdentity
pdn_as_products = _Pdn_as_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 8)
)
_As_4_ObjectIdentity = ObjectIdentity
as_4 = _As_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 8, 1)
)
_As_8_ObjectIdentity = ObjectIdentity
as_8 = _As_8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 8, 2)
)
_As_24_ObjectIdentity = ObjectIdentity
as_24 = _As_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 8, 3)
)
_Pdn_xdsl_products_ObjectIdentity = ObjectIdentity
pdn_xdsl_products = _Pdn_xdsl_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9)
)
_Xdsl_5100_ObjectIdentity = ObjectIdentity
xdsl_5100 = _Xdsl_5100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 1)
)
_Xdsl_unused1_ObjectIdentity = ObjectIdentity
xdsl_unused1 = _Xdsl_unused1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 2)
)
_Xdsl_8800_old_ObjectIdentity = ObjectIdentity
xdsl_8800_old = _Xdsl_8800_old_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 3)
)
_Xdsl_unused2_ObjectIdentity = ObjectIdentity
xdsl_unused2 = _Xdsl_unused2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 4)
)
_Xdsl_8600_old_ObjectIdentity = ObjectIdentity
xdsl_8600_old = _Xdsl_8600_old_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 5)
)
_Xdsl_ipc_ObjectIdentity = ObjectIdentity
xdsl_ipc = _Xdsl_ipc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 6)
)
_Xdsl_8100_ObjectIdentity = ObjectIdentity
xdsl_8100 = _Xdsl_8100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 6, 1)
)
_Xdsl_8200_ObjectIdentity = ObjectIdentity
xdsl_8200 = _Xdsl_8200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 6, 2)
)
_Xdsl_chassis_ObjectIdentity = ObjectIdentity
xdsl_chassis = _Xdsl_chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 8)
)
_Xdsl_8600_ObjectIdentity = ObjectIdentity
xdsl_8600 = _Xdsl_8600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 8, 1)
)
_Xdsl_8800_ObjectIdentity = ObjectIdentity
xdsl_8800 = _Xdsl_8800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 8, 2)
)
_Xdsl_8610_ObjectIdentity = ObjectIdentity
xdsl_8610 = _Xdsl_8610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 8, 3)
)
_Xdsl_8810_ObjectIdentity = ObjectIdentity
xdsl_8810 = _Xdsl_8810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 8, 4)
)
_Xdsl_8820_ObjectIdentity = ObjectIdentity
xdsl_8820 = _Xdsl_8820_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 8, 5)
)
_Xdsl_8610_X_ObjectIdentity = ObjectIdentity
xdsl_8610_X = _Xdsl_8610_X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 8, 6)
)
_Xdsl_8810_X_ObjectIdentity = ObjectIdentity
xdsl_8810_X = _Xdsl_8810_X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 8, 7)
)
_Xdsl_8820_X_ObjectIdentity = ObjectIdentity
xdsl_8820_X = _Xdsl_8820_X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 8, 8)
)
_Xdsl_8620_ObjectIdentity = ObjectIdentity
xdsl_8620 = _Xdsl_8620_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 8, 9)
)
_Xdsl_remote_ObjectIdentity = ObjectIdentity
xdsl_remote = _Xdsl_remote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9)
)
_Xdsl_5446_ObjectIdentity = ObjectIdentity
xdsl_5446 = _Xdsl_5446_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 1)
)
_Xdsl_7914_ObjectIdentity = ObjectIdentity
xdsl_7914 = _Xdsl_7914_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 2)
)
_Xdsl_5246_ObjectIdentity = ObjectIdentity
xdsl_5246 = _Xdsl_5246_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 3)
)
_Xdsl_5216_ObjectIdentity = ObjectIdentity
xdsl_5216 = _Xdsl_5216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 4)
)
_Xdsl_5170_ObjectIdentity = ObjectIdentity
xdsl_5170 = _Xdsl_5170_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 5)
)
_Xdsl_5171_ObjectIdentity = ObjectIdentity
xdsl_5171 = _Xdsl_5171_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 6)
)
_Xdsl_5546_ObjectIdentity = ObjectIdentity
xdsl_5546 = _Xdsl_5546_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 7)
)
_Xdsl_5620_ObjectIdentity = ObjectIdentity
xdsl_5620 = _Xdsl_5620_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 8)
)
_Xdsl_6310_ObjectIdentity = ObjectIdentity
xdsl_6310 = _Xdsl_6310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 9)
)
_Xdsl_7975_ObjectIdentity = ObjectIdentity
xdsl_7975 = _Xdsl_7975_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 10)
)
_Xdsl_7976_ObjectIdentity = ObjectIdentity
xdsl_7976 = _Xdsl_7976_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 11)
)
_Xdsl_7974_ObjectIdentity = ObjectIdentity
xdsl_7974 = _Xdsl_7974_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 12)
)
_Xdsl_7986_ObjectIdentity = ObjectIdentity
xdsl_7986 = _Xdsl_7986_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 13)
)
_Xdsl_7985_ObjectIdentity = ObjectIdentity
xdsl_7985 = _Xdsl_7985_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 14)
)
_Xdsl_7984_ObjectIdentity = ObjectIdentity
xdsl_7984 = _Xdsl_7984_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 15)
)
_Xdsl_6341_ObjectIdentity = ObjectIdentity
xdsl_6341 = _Xdsl_6341_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 16)
)
_Xdsl_6342_ObjectIdentity = ObjectIdentity
xdsl_6342 = _Xdsl_6342_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 17)
)
_Xdsl_6331_ObjectIdentity = ObjectIdentity
xdsl_6331 = _Xdsl_6331_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 18)
)
_Xdsl_6332_ObjectIdentity = ObjectIdentity
xdsl_6332 = _Xdsl_6332_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 19)
)
_Xdsl_6371_ObjectIdentity = ObjectIdentity
xdsl_6371 = _Xdsl_6371_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 20)
)
_Xdsl_6372_ObjectIdentity = ObjectIdentity
xdsl_6372 = _Xdsl_6372_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 21)
)
_Xdsl_6321_ObjectIdentity = ObjectIdentity
xdsl_6321 = _Xdsl_6321_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 23)
)
_Xdsl_6322_ObjectIdentity = ObjectIdentity
xdsl_6322 = _Xdsl_6322_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 24)
)
_Xdsl_6341R2_ObjectIdentity = ObjectIdentity
xdsl_6341R2 = _Xdsl_6341R2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 25)
)
_Xdsl_6342R2_ObjectIdentity = ObjectIdentity
xdsl_6342R2 = _Xdsl_6342R2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 26)
)
_Xdsl_6331R2_ObjectIdentity = ObjectIdentity
xdsl_6331R2 = _Xdsl_6331R2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 27)
)
_Xdsl_6332R2_ObjectIdentity = ObjectIdentity
xdsl_6332R2 = _Xdsl_6332R2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 28)
)
_Xdsl_6371R2_ObjectIdentity = ObjectIdentity
xdsl_6371R2 = _Xdsl_6371R2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 29)
)
_Xdsl_6372R2_ObjectIdentity = ObjectIdentity
xdsl_6372R2 = _Xdsl_6372R2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 30)
)
_Xdsl_6321R2_ObjectIdentity = ObjectIdentity
xdsl_6321R2 = _Xdsl_6321R2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 31)
)
_Xdsl_6322R2_ObjectIdentity = ObjectIdentity
xdsl_6322R2 = _Xdsl_6322R2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 32)
)
_Xdsl_6328_ObjectIdentity = ObjectIdentity
xdsl_6328 = _Xdsl_6328_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 33)
)
_Xdsl_6329_ObjectIdentity = ObjectIdentity
xdsl_6329 = _Xdsl_6329_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 34)
)
_Xdsl_6301R2_ObjectIdentity = ObjectIdentity
xdsl_6301R2 = _Xdsl_6301R2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 35)
)
_Xdsl_6302R2_ObjectIdentity = ObjectIdentity
xdsl_6302R2 = _Xdsl_6302R2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 36)
)
_Xdsl_6350_ObjectIdentity = ObjectIdentity
xdsl_6350 = _Xdsl_6350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 38)
)
_Xdsl_6351_ObjectIdentity = ObjectIdentity
xdsl_6351 = _Xdsl_6351_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 39)
)
_Xdsl_6385_ObjectIdentity = ObjectIdentity
xdsl_6385 = _Xdsl_6385_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 40)
)
_Xdsl_7994_ObjectIdentity = ObjectIdentity
xdsl_7994 = _Xdsl_7994_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 41)
)
_Xdsl_7995_ObjectIdentity = ObjectIdentity
xdsl_7995 = _Xdsl_7995_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 42)
)
_Xdsl_7996_ObjectIdentity = ObjectIdentity
xdsl_7996 = _Xdsl_7996_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 9, 43)
)
_Xdsl_cards_ObjectIdentity = ObjectIdentity
xdsl_cards = _Xdsl_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10)
)
_Card_mcc_ObjectIdentity = ObjectIdentity
card_mcc = _Card_mcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 1)
)
_Card_adsl_ObjectIdentity = ObjectIdentity
card_adsl = _Card_adsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 2)
)
_Card_radsl_ObjectIdentity = ObjectIdentity
card_radsl = _Card_radsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 3)
)
_Card_sdsl_ObjectIdentity = ObjectIdentity
card_sdsl = _Card_sdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 4)
)
_Card_vdsl_ObjectIdentity = ObjectIdentity
card_vdsl = _Card_vdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 5)
)
_Card_8774_ObjectIdentity = ObjectIdentity
card_8774 = _Card_8774_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 6)
)
_Card_8540_ObjectIdentity = ObjectIdentity
card_8540 = _Card_8540_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 7)
)
_Card_8775_ObjectIdentity = ObjectIdentity
card_8775 = _Card_8775_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 8)
)
_Card_8776_ObjectIdentity = ObjectIdentity
card_8776 = _Card_8776_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 9)
)
_Card_8786_ObjectIdentity = ObjectIdentity
card_8786 = _Card_8786_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 10)
)
_Card_8946_ObjectIdentity = ObjectIdentity
card_8946 = _Card_8946_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 11)
)
_Card_8510_ObjectIdentity = ObjectIdentity
card_8510 = _Card_8510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 12)
)
_Card_8310_ObjectIdentity = ObjectIdentity
card_8310 = _Card_8310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 13)
)
_Card_e1_sdsl_ObjectIdentity = ObjectIdentity
card_e1_sdsl = _Card_e1_sdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 14)
)
_Card_mcc2_ObjectIdentity = ObjectIdentity
card_mcc2 = _Card_mcc2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 15)
)
_Card_8785_ObjectIdentity = ObjectIdentity
card_8785 = _Card_8785_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 16)
)
_Card_8784_ObjectIdentity = ObjectIdentity
card_8784 = _Card_8784_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 17)
)
_Card_8312_ObjectIdentity = ObjectIdentity
card_8312 = _Card_8312_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 18)
)
_Card_8344_ObjectIdentity = ObjectIdentity
card_8344 = _Card_8344_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 19)
)
_Card_mcc_plus_ObjectIdentity = ObjectIdentity
card_mcc_plus = _Card_mcc_plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 20)
)
_Card_mcp_ObjectIdentity = ObjectIdentity
card_mcp = _Card_mcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 21)
)
_Card_8334_ObjectIdentity = ObjectIdentity
card_8334 = _Card_8334_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 22)
)
_Card_xxxx_ObjectIdentity = ObjectIdentity
card_xxxx = _Card_xxxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 23)
)
_Card_8343_ObjectIdentity = ObjectIdentity
card_8343 = _Card_8343_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 24)
)
_Card_8333_ObjectIdentity = ObjectIdentity
card_8333 = _Card_8333_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 25)
)
_Card_8719_ObjectIdentity = ObjectIdentity
card_8719 = _Card_8719_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 26)
)
_Card_8747_ObjectIdentity = ObjectIdentity
card_8747 = _Card_8747_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 27)
)
_Card_8777_ObjectIdentity = ObjectIdentity
card_8777 = _Card_8777_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 28)
)
_Card_8779_ObjectIdentity = ObjectIdentity
card_8779 = _Card_8779_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 29)
)
_Card_8021_ObjectIdentity = ObjectIdentity
card_8021 = _Card_8021_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 30)
)
_Card_8022_ObjectIdentity = ObjectIdentity
card_8022 = _Card_8022_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 31)
)
_Card_8373_ObjectIdentity = ObjectIdentity
card_8373 = _Card_8373_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 32)
)
_Card_8374_ObjectIdentity = ObjectIdentity
card_8374 = _Card_8374_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 33)
)
_Card_8323_ObjectIdentity = ObjectIdentity
card_8323 = _Card_8323_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 34)
)
_Card_8324_ObjectIdentity = ObjectIdentity
card_8324 = _Card_8324_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 35)
)
_Card_8023_ObjectIdentity = ObjectIdentity
card_8023 = _Card_8023_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 36)
)
_Card_8024_ObjectIdentity = ObjectIdentity
card_8024 = _Card_8024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 37)
)
_Card_8335_ObjectIdentity = ObjectIdentity
card_8335 = _Card_8335_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 38)
)
_Card_8365_ObjectIdentity = ObjectIdentity
card_8365 = _Card_8365_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 39)
)
_Card_83xx_ObjectIdentity = ObjectIdentity
card_83xx = _Card_83xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 40)
)
_Card_8314_ObjectIdentity = ObjectIdentity
card_8314 = _Card_8314_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 41)
)
_Card_8328_ObjectIdentity = ObjectIdentity
card_8328 = _Card_8328_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 42)
)
_Card_8329_ObjectIdentity = ObjectIdentity
card_8329 = _Card_8329_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 43)
)
_Card_8303_ObjectIdentity = ObjectIdentity
card_8303 = _Card_8303_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 44)
)
_Card_8304_ObjectIdentity = ObjectIdentity
card_8304 = _Card_8304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 45)
)
_Card_8025_ObjectIdentity = ObjectIdentity
card_8025 = _Card_8025_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 46)
)
_Card_8026_ObjectIdentity = ObjectIdentity
card_8026 = _Card_8026_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 47)
)
_Card_8027_ObjectIdentity = ObjectIdentity
card_8027 = _Card_8027_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 48)
)
_Card_8028_ObjectIdentity = ObjectIdentity
card_8028 = _Card_8028_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 49)
)
_Card_8379_ObjectIdentity = ObjectIdentity
card_8379 = _Card_8379_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 50)
)
_Card_8312_ReachDSL_ObjectIdentity = ObjectIdentity
card_8312_ReachDSL = _Card_8312_ReachDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 51)
)
_Card_8314_ReachDSL_ObjectIdentity = ObjectIdentity
card_8314_ReachDSL = _Card_8314_ReachDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 52)
)
_Card_8385_ObjectIdentity = ObjectIdentity
card_8385 = _Card_8385_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 53)
)
_Card_8395_ObjectIdentity = ObjectIdentity
card_8395 = _Card_8395_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 54)
)
_Card_8396_ObjectIdentity = ObjectIdentity
card_8396 = _Card_8396_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 55)
)
_Card_8797_ObjectIdentity = ObjectIdentity
card_8797 = _Card_8797_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 56)
)
_Card_8799_ObjectIdentity = ObjectIdentity
card_8799 = _Card_8799_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 57)
)
_Card_8355_ObjectIdentity = ObjectIdentity
card_8355 = _Card_8355_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 58)
)
_Card_mcp8900_ObjectIdentity = ObjectIdentity
card_mcp8900 = _Card_mcp8900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 10, 59)
)
_Xdsl_ports_ObjectIdentity = ObjectIdentity
xdsl_ports = _Xdsl_ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 11)
)
_Port_dsl_ObjectIdentity = ObjectIdentity
port_dsl = _Port_dsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 11, 1)
)
_Port_mvl_ObjectIdentity = ObjectIdentity
port_mvl = _Port_mvl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 11, 2)
)
_Port_eth10_ObjectIdentity = ObjectIdentity
port_eth10 = _Port_eth10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 11, 3)
)
_Port_eth100_ObjectIdentity = ObjectIdentity
port_eth100 = _Port_eth100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 11, 4)
)
_Port_oc3_ObjectIdentity = ObjectIdentity
port_oc3 = _Port_oc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 11, 5)
)
_Port_ds3_ObjectIdentity = ObjectIdentity
port_ds3 = _Port_ds3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 11, 6)
)
_Port_sar_ObjectIdentity = ObjectIdentity
port_sar = _Port_sar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 11, 7)
)
_Port_hdlc_ObjectIdentity = ObjectIdentity
port_hdlc = _Port_hdlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 11, 8)
)
_Port_e3_ObjectIdentity = ObjectIdentity
port_e3 = _Port_e3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 11, 9)
)
_Port_ds1_ObjectIdentity = ObjectIdentity
port_ds1 = _Port_ds1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 11, 10)
)
_Port_e1_ObjectIdentity = ObjectIdentity
port_e1 = _Port_e1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 11, 11)
)
_Port_ima_ObjectIdentity = ObjectIdentity
port_ima = _Port_ima_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 11, 12)
)
_Port_reachDsl_ObjectIdentity = ObjectIdentity
port_reachDsl = _Port_reachDsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 11, 13)
)
_Port_reachDslV3_ObjectIdentity = ObjectIdentity
port_reachDslV3 = _Port_reachDslV3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 11, 14)
)
_Xdsl_slots_ObjectIdentity = ObjectIdentity
xdsl_slots = _Xdsl_slots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 12)
)
_Slot_std_ObjectIdentity = ObjectIdentity
slot_std = _Slot_std_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 12, 1)
)
_Xdsl_components_ObjectIdentity = ObjectIdentity
xdsl_components = _Xdsl_components_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 13)
)
_Comp_powerA_ObjectIdentity = ObjectIdentity
comp_powerA = _Comp_powerA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 13, 1)
)
_Comp_powerB_ObjectIdentity = ObjectIdentity
comp_powerB = _Comp_powerB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 13, 2)
)
_Comp_fan_ObjectIdentity = ObjectIdentity
comp_fan = _Comp_fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 13, 3)
)
_Comp_mgmt_ObjectIdentity = ObjectIdentity
comp_mgmt = _Comp_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 13, 4)
)
_Comp_atm_ObjectIdentity = ObjectIdentity
comp_atm = _Comp_atm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 13, 5)
)
_Comp_pld_ObjectIdentity = ObjectIdentity
comp_pld = _Comp_pld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 13, 6)
)
_Comp_sensor_ObjectIdentity = ObjectIdentity
comp_sensor = _Comp_sensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 13, 7)
)
_Xdsl_sme_ObjectIdentity = ObjectIdentity
xdsl_sme = _Xdsl_sme_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14)
)
_Sme_scp_cards_ObjectIdentity = ObjectIdentity
sme_scp_cards = _Sme_scp_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 1)
)
_Sme_scp_8412_card_ObjectIdentity = ObjectIdentity
sme_scp_8412_card = _Sme_scp_8412_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 1, 1)
)
_Sme_scp_8413_card_ObjectIdentity = ObjectIdentity
sme_scp_8413_card = _Sme_scp_8413_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 1, 2)
)
_Sme_scp_8414_card_ObjectIdentity = ObjectIdentity
sme_scp_8414_card = _Sme_scp_8414_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 1, 3)
)
_Sme_scp_8416_card_ObjectIdentity = ObjectIdentity
sme_scp_8416_card = _Sme_scp_8416_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 1, 4)
)
_Sme_scp_8417_card_ObjectIdentity = ObjectIdentity
sme_scp_8417_card = _Sme_scp_8417_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 1, 5)
)
_Sme_scp_8418_card_ObjectIdentity = ObjectIdentity
sme_scp_8418_card = _Sme_scp_8418_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 1, 6)
)
_Sme_childcards_ObjectIdentity = ObjectIdentity
sme_childcards = _Sme_childcards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 2)
)
_Sme_t1e1_uplink_child_ObjectIdentity = ObjectIdentity
sme_t1e1_uplink_child = _Sme_t1e1_uplink_child_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 2, 1)
)
_Sme_ports_ObjectIdentity = ObjectIdentity
sme_ports = _Sme_ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 3)
)
_Sme_reachDsl_port_ObjectIdentity = ObjectIdentity
sme_reachDsl_port = _Sme_reachDsl_port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 3, 1)
)
_Sme_adsl_a_port_ObjectIdentity = ObjectIdentity
sme_adsl_a_port = _Sme_adsl_a_port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 3, 2)
)
_Sme_adsl_b_port_ObjectIdentity = ObjectIdentity
sme_adsl_b_port = _Sme_adsl_b_port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 3, 3)
)
_Sme_shdsl_port_ObjectIdentity = ObjectIdentity
sme_shdsl_port = _Sme_shdsl_port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 3, 4)
)
_Sme_t1e1_port_ObjectIdentity = ObjectIdentity
sme_t1e1_port = _Sme_t1e1_port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 3, 5)
)
_Sme_oc3_port_ObjectIdentity = ObjectIdentity
sme_oc3_port = _Sme_oc3_port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 3, 6)
)
_Sme_rs232_port_ObjectIdentity = ObjectIdentity
sme_rs232_port = _Sme_rs232_port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 3, 7)
)
_Sme_eth_port_ObjectIdentity = ObjectIdentity
sme_eth_port = _Sme_eth_port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 3, 8)
)
_Sme_ds3_port_ObjectIdentity = ObjectIdentity
sme_ds3_port = _Sme_ds3_port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 3, 9)
)
_Sme_portcards_ObjectIdentity = ObjectIdentity
sme_portcards = _Sme_portcards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 4)
)
_Sme_8965_card_ObjectIdentity = ObjectIdentity
sme_8965_card = _Sme_8965_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 4, 1)
)
_Sme_8955_card_ObjectIdentity = ObjectIdentity
sme_8955_card = _Sme_8955_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 4, 2)
)
_Sme_8985_card_ObjectIdentity = ObjectIdentity
sme_8985_card = _Sme_8985_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 4, 3)
)
_Sme_chassis_ObjectIdentity = ObjectIdentity
sme_chassis = _Sme_chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 5)
)
_Sme_chassis_8820_ObjectIdentity = ObjectIdentity
sme_chassis_8820 = _Sme_chassis_8820_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 5, 1)
)
_Sme_chassis_8620_ObjectIdentity = ObjectIdentity
sme_chassis_8620 = _Sme_chassis_8620_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 5, 2)
)
_Sme_components_ObjectIdentity = ObjectIdentity
sme_components = _Sme_components_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 6)
)
_Sme_comp_fan_ObjectIdentity = ObjectIdentity
sme_comp_fan = _Sme_comp_fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 6, 1)
)
_Sme_comp_pld_ObjectIdentity = ObjectIdentity
sme_comp_pld = _Sme_comp_pld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 6, 2)
)
_Sme_comp_sensor_ObjectIdentity = ObjectIdentity
sme_comp_sensor = _Sme_comp_sensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 6, 3)
)
_Sme_comp_powersupply_ObjectIdentity = ObjectIdentity
sme_comp_powersupply = _Sme_comp_powersupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 6, 4)
)
_Sme_comp_spf_ObjectIdentity = ObjectIdentity
sme_comp_spf = _Sme_comp_spf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 6, 5)
)
_Sme_container_ObjectIdentity = ObjectIdentity
sme_container = _Sme_container_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 9, 14, 7)
)
_Pdn_comp_products_ObjectIdentity = ObjectIdentity
pdn_comp_products = _Pdn_comp_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 10)
)
_Comp_9028_ObjectIdentity = ObjectIdentity
comp_9028 = _Comp_9028_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 10, 1)
)
_Pdn_ptc_products_ObjectIdentity = ObjectIdentity
pdn_ptc_products = _Pdn_ptc_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 11)
)
_Xdsl_xdsl_ObjectIdentity = ObjectIdentity
xdsl_xdsl = _Xdsl_xdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 11, 1)
)
_PdnDslEndpoint_ObjectIdentity = ObjectIdentity
pdnDslEndpoint = _PdnDslEndpoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 12)
)
_Reserved13_ObjectIdentity = ObjectIdentity
reserved13 = _Reserved13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 13)
)
_Reserved14_ObjectIdentity = ObjectIdentity
reserved14 = _Reserved14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 14)
)
_Pdn_cellsaver_ObjectIdentity = ObjectIdentity
pdn_cellsaver = _Pdn_cellsaver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 15)
)
_Cellsaver_9510_ObjectIdentity = ObjectIdentity
cellsaver_9510 = _Cellsaver_9510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 15, 1)
)
_Cellsaver_9550_ObjectIdentity = ObjectIdentity
cellsaver_9550 = _Cellsaver_9550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 15, 2)
)
_Pdn_cornet_ObjectIdentity = ObjectIdentity
pdn_cornet = _Pdn_cornet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 16)
)
_Cornet_xxxx_ObjectIdentity = ObjectIdentity
cornet_xxxx = _Cornet_xxxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 16, 1)
)
_Ip_stackable_ObjectIdentity = ObjectIdentity
ip_stackable = _Ip_stackable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17)
)
_Ips_stack_ObjectIdentity = ObjectIdentity
ips_stack = _Ips_stack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 1)
)
_Ips_4800_ObjectIdentity = ObjectIdentity
ips_4800 = _Ips_4800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 1, 1)
)
_Ips_2600_ObjectIdentity = ObjectIdentity
ips_2600 = _Ips_2600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 1, 2)
)
_Ips_4200_ObjectIdentity = ObjectIdentity
ips_4200 = _Ips_4200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 1, 3)
)
_Ips_chassis_ObjectIdentity = ObjectIdentity
ips_chassis = _Ips_chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 2)
)
_Ips_4821_ObjectIdentity = ObjectIdentity
ips_4821 = _Ips_4821_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 2, 1)
)
_Ips_2611_ObjectIdentity = ObjectIdentity
ips_2611 = _Ips_2611_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 2, 2)
)
_Ips_2621_ObjectIdentity = ObjectIdentity
ips_2621 = _Ips_2621_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 2, 3)
)
_Ips_4219_ObjectIdentity = ObjectIdentity
ips_4219 = _Ips_4219_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 2, 4)
)
_Ips_4229_ObjectIdentity = ObjectIdentity
ips_4229 = _Ips_4229_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 2, 5)
)
_Ips_fixed_cards_ObjectIdentity = ObjectIdentity
ips_fixed_cards = _Ips_fixed_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 3)
)
_Ips_24port_adsl_main_card_ObjectIdentity = ObjectIdentity
ips_24port_adsl_main_card = _Ips_24port_adsl_main_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 3, 1)
)
_Ips_24port_adsl_child_card_ObjectIdentity = ObjectIdentity
ips_24port_adsl_child_card = _Ips_24port_adsl_child_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 3, 2)
)
_Ips_maui_card_ObjectIdentity = ObjectIdentity
ips_maui_card = _Ips_maui_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 3, 3)
)
_Ips_pots_splitter_child_card_ObjectIdentity = ObjectIdentity
ips_pots_splitter_child_card = _Ips_pots_splitter_child_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 3, 4)
)
_Ips_24port_reachDsl_main_card_ObjectIdentity = ObjectIdentity
ips_24port_reachDsl_main_card = _Ips_24port_reachDsl_main_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 3, 5)
)
_Ips_24port_reachDsl_child_card_ObjectIdentity = ObjectIdentity
ips_24port_reachDsl_child_card = _Ips_24port_reachDsl_child_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 3, 6)
)
_Ips_pluggable_cards_ObjectIdentity = ObjectIdentity
ips_pluggable_cards = _Ips_pluggable_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 4)
)
_Ips_mgmt_no_wan_ObjectIdentity = ObjectIdentity
ips_mgmt_no_wan = _Ips_mgmt_no_wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 4, 1)
)
_Ips_mgmt_with_v35x21_wan_ObjectIdentity = ObjectIdentity
ips_mgmt_with_v35x21_wan = _Ips_mgmt_with_v35x21_wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 4, 2)
)
_Ips_mgmt_with_t1e1_mlppp_wan_ObjectIdentity = ObjectIdentity
ips_mgmt_with_t1e1_mlppp_wan = _Ips_mgmt_with_t1e1_mlppp_wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 4, 3)
)
_Ips_mgmt_with_t1e1_ima_wan_ObjectIdentity = ObjectIdentity
ips_mgmt_with_t1e1_ima_wan = _Ips_mgmt_with_t1e1_ima_wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 4, 4)
)
_Ips_ports_ObjectIdentity = ObjectIdentity
ips_ports = _Ips_ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 5)
)
_Ips_rs232_dte_port_ObjectIdentity = ObjectIdentity
ips_rs232_dte_port = _Ips_rs232_dte_port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 5, 1)
)
_Ips_rs232_dce_port_ObjectIdentity = ObjectIdentity
ips_rs232_dce_port = _Ips_rs232_dce_port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 5, 2)
)
_Ips_v35_dte_port_ObjectIdentity = ObjectIdentity
ips_v35_dte_port = _Ips_v35_dte_port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 5, 3)
)
_Ips_adsl_port_ObjectIdentity = ObjectIdentity
ips_adsl_port = _Ips_adsl_port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 5, 4)
)
_Ips_ethernet_port_ObjectIdentity = ObjectIdentity
ips_ethernet_port = _Ips_ethernet_port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 5, 5)
)
_Ips_t1e1_port_ObjectIdentity = ObjectIdentity
ips_t1e1_port = _Ips_t1e1_port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 5, 6)
)
_Ips_adsl_a_port_ObjectIdentity = ObjectIdentity
ips_adsl_a_port = _Ips_adsl_a_port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 5, 7)
)
_Ips_reachDslPort_ObjectIdentity = ObjectIdentity
ips_reachDslPort = _Ips_reachDslPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 5, 8)
)
_Ips_components_ObjectIdentity = ObjectIdentity
ips_components = _Ips_components_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 6)
)
_Ips_fan_ObjectIdentity = ObjectIdentity
ips_fan = _Ips_fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 6, 1)
)
_Ips_temperature_sensor_ObjectIdentity = ObjectIdentity
ips_temperature_sensor = _Ips_temperature_sensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 6, 2)
)
_Ips_processor_ObjectIdentity = ObjectIdentity
ips_processor = _Ips_processor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 6, 3)
)
_Ips_pld_ObjectIdentity = ObjectIdentity
ips_pld = _Ips_pld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 6, 4)
)
_Ips_speed_sensor_ObjectIdentity = ObjectIdentity
ips_speed_sensor = _Ips_speed_sensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 6, 5)
)
_Ips_alarm_relay_contact_ObjectIdentity = ObjectIdentity
ips_alarm_relay_contact = _Ips_alarm_relay_contact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 6, 6)
)
_Ips_dot1dBasePortCircuit_ObjectIdentity = ObjectIdentity
ips_dot1dBasePortCircuit = _Ips_dot1dBasePortCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 7)
)
_Ips_piwg_1_ObjectIdentity = ObjectIdentity
ips_piwg_1 = _Ips_piwg_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 7, 1)
)
_Ips_piwg_2_ObjectIdentity = ObjectIdentity
ips_piwg_2 = _Ips_piwg_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 7, 2)
)
_Ips_piwg_3_ObjectIdentity = ObjectIdentity
ips_piwg_3 = _Ips_piwg_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 7, 3)
)
_Ips_piwg_4_ObjectIdentity = ObjectIdentity
ips_piwg_4 = _Ips_piwg_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 7, 4)
)
_Ips_piwg_5_ObjectIdentity = ObjectIdentity
ips_piwg_5 = _Ips_piwg_5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 7, 5)
)
_Ips_piwg_6_ObjectIdentity = ObjectIdentity
ips_piwg_6 = _Ips_piwg_6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 7, 6)
)
_Ips_piwg_7_ObjectIdentity = ObjectIdentity
ips_piwg_7 = _Ips_piwg_7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 7, 7)
)
_Ips_piwg_8_ObjectIdentity = ObjectIdentity
ips_piwg_8 = _Ips_piwg_8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 17, 7, 8)
)
_Etherloop_ObjectIdentity = ObjectIdentity
etherloop = _Etherloop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 18)
)
_Eloop_shelf_ObjectIdentity = ObjectIdentity
eloop_shelf = _Eloop_shelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 18, 1)
)
_Eloop_2400_ObjectIdentity = ObjectIdentity
eloop_2400 = _Eloop_2400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 18, 1, 1)
)
_Eloop_unit_ObjectIdentity = ObjectIdentity
eloop_unit = _Eloop_unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 18, 2)
)
_Eloop_2461_ObjectIdentity = ObjectIdentity
eloop_2461 = _Eloop_2461_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 18, 2, 1)
)
_Eloop_modem_stick_ObjectIdentity = ObjectIdentity
eloop_modem_stick = _Eloop_modem_stick_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 18, 3)
)
_Eloop_intf_card_ObjectIdentity = ObjectIdentity
eloop_intf_card = _Eloop_intf_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 18, 4)
)
_Eloop_switch_card_ObjectIdentity = ObjectIdentity
eloop_switch_card = _Eloop_switch_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 18, 5)
)
_Atm_stackable_ObjectIdentity = ObjectIdentity
atm_stackable = _Atm_stackable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19)
)
_Atmstk_stack_ObjectIdentity = ObjectIdentity
atmstk_stack = _Atmstk_stack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 1)
)
_Atmstk_4200_ObjectIdentity = ObjectIdentity
atmstk_4200 = _Atmstk_4200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 1, 1)
)
_Atmstk_chassis_ObjectIdentity = ObjectIdentity
atmstk_chassis = _Atmstk_chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 2)
)
_Atmstk_4216_ObjectIdentity = ObjectIdentity
atmstk_4216 = _Atmstk_4216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 2, 1)
)
_Atmstk_4218_ObjectIdentity = ObjectIdentity
atmstk_4218 = _Atmstk_4218_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 2, 2)
)
_Atmstk_4210_ObjectIdentity = ObjectIdentity
atmstk_4210 = _Atmstk_4210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 2, 3)
)
_Atmstk_4211_ObjectIdentity = ObjectIdentity
atmstk_4211 = _Atmstk_4211_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 2, 4)
)
_Atmstk_4212_ObjectIdentity = ObjectIdentity
atmstk_4212 = _Atmstk_4212_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 2, 5)
)
_Atmstk_4213_ObjectIdentity = ObjectIdentity
atmstk_4213 = _Atmstk_4213_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 2, 6)
)
_Atmstk_4221_ObjectIdentity = ObjectIdentity
atmstk_4221 = _Atmstk_4221_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 2, 7)
)
_Atmstk_4222_ObjectIdentity = ObjectIdentity
atmstk_4222 = _Atmstk_4222_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 2, 8)
)
_Atmstk_4223_ObjectIdentity = ObjectIdentity
atmstk_4223 = _Atmstk_4223_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 2, 9)
)
_Atmstk_4231_ObjectIdentity = ObjectIdentity
atmstk_4231 = _Atmstk_4231_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 2, 10)
)
_Atmstk_4232_ObjectIdentity = ObjectIdentity
atmstk_4232 = _Atmstk_4232_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 2, 11)
)
_Atmstk_4233_ObjectIdentity = ObjectIdentity
atmstk_4233 = _Atmstk_4233_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 2, 12)
)
_Atmstk_cards_ObjectIdentity = ObjectIdentity
atmstk_cards = _Atmstk_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 3)
)
_Atmstk_24Port_main_reach_ObjectIdentity = ObjectIdentity
atmstk_24Port_main_reach = _Atmstk_24Port_main_reach_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 3, 1)
)
_Atmstk_24Port_main_adsl_a_ObjectIdentity = ObjectIdentity
atmstk_24Port_main_adsl_a = _Atmstk_24Port_main_adsl_a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 3, 2)
)
_Atmstk_24Port_main_adsl_b_ObjectIdentity = ObjectIdentity
atmstk_24Port_main_adsl_b = _Atmstk_24Port_main_adsl_b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 3, 3)
)
_Atmstk_child_cards_ObjectIdentity = ObjectIdentity
atmstk_child_cards = _Atmstk_child_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 4)
)
_Atmstk_4201_t1_uplink_ObjectIdentity = ObjectIdentity
atmstk_4201_t1_uplink = _Atmstk_4201_t1_uplink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 4, 1)
)
_Atmstk_4202_e1_uplink_ObjectIdentity = ObjectIdentity
atmstk_4202_e1_uplink = _Atmstk_4202_e1_uplink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 4, 2)
)
_Atmstk_4203_t1e1_ima_uplink_ObjectIdentity = ObjectIdentity
atmstk_4203_t1e1_ima_uplink = _Atmstk_4203_t1e1_ima_uplink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 4, 3)
)
_Atmstk_oc3_uplink_ObjectIdentity = ObjectIdentity
atmstk_oc3_uplink = _Atmstk_oc3_uplink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 4, 4)
)
_Atmstk_splitter_ObjectIdentity = ObjectIdentity
atmstk_splitter = _Atmstk_splitter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 4, 5)
)
_Atmstk_24Port_ext_ObjectIdentity = ObjectIdentity
atmstk_24Port_ext = _Atmstk_24Port_ext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 4, 6)
)
_Atmstk_ports_ObjectIdentity = ObjectIdentity
atmstk_ports = _Atmstk_ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 5)
)
_Atmstk_reachDsl_port_ObjectIdentity = ObjectIdentity
atmstk_reachDsl_port = _Atmstk_reachDsl_port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 5, 1)
)
_Atmstk_t1e1_port_ObjectIdentity = ObjectIdentity
atmstk_t1e1_port = _Atmstk_t1e1_port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 5, 2)
)
_Atmstk_rs232_dce_port_ObjectIdentity = ObjectIdentity
atmstk_rs232_dce_port = _Atmstk_rs232_dce_port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 5, 3)
)
_Atmstk_ethernet_port_ObjectIdentity = ObjectIdentity
atmstk_ethernet_port = _Atmstk_ethernet_port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 5, 4)
)
_Atmstk_ADSL_annexa_port_ObjectIdentity = ObjectIdentity
atmstk_ADSL_annexa_port = _Atmstk_ADSL_annexa_port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 5, 5)
)
_Atmstk_ADSL_annexb_port_ObjectIdentity = ObjectIdentity
atmstk_ADSL_annexb_port = _Atmstk_ADSL_annexb_port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 5, 6)
)
_Atmstk_components_ObjectIdentity = ObjectIdentity
atmstk_components = _Atmstk_components_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 6)
)
_Atmstk_comp_fan_ObjectIdentity = ObjectIdentity
atmstk_comp_fan = _Atmstk_comp_fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 6, 1)
)
_Atmstk_comp_temp_sensor_ObjectIdentity = ObjectIdentity
atmstk_comp_temp_sensor = _Atmstk_comp_temp_sensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 6, 2)
)
_Atmstk_comp_pld_ObjectIdentity = ObjectIdentity
atmstk_comp_pld = _Atmstk_comp_pld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 1, 14, 19, 6, 3)
)
_Pdn_mgmt_ObjectIdentity = ObjectIdentity
pdn_mgmt = _Pdn_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2)
)
_ParadyneNMS_ObjectIdentity = ObjectIdentity
paradyneNMS = _ParadyneNMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 23)
)
_Nms_6700_ObjectIdentity = ObjectIdentity
nms_6700 = _Nms_6700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 23, 5)
)
_Paradyne_ObjectIdentity = ObjectIdentity
paradyne = _Paradyne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24)
)
_Pdn_cellRelay_ObjectIdentity = ObjectIdentity
pdn_cellRelay = _Pdn_cellRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 1)
)
_Pdn_common_ObjectIdentity = ObjectIdentity
pdn_common = _Pdn_common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2)
)
_Pdn_frontPanel_ObjectIdentity = ObjectIdentity
pdn_frontPanel = _Pdn_frontPanel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 1)
)
_Pdn_chassis_ObjectIdentity = ObjectIdentity
pdn_chassis = _Pdn_chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 2)
)
_Pdn_callDir_ObjectIdentity = ObjectIdentity
pdn_callDir = _Pdn_callDir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 3)
)
_Pdn_devStatus_ObjectIdentity = ObjectIdentity
pdn_devStatus = _Pdn_devStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 4)
)
_Pdn_devID_ObjectIdentity = ObjectIdentity
pdn_devID = _Pdn_devID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 5)
)
_Pdn_interfaces_ObjectIdentity = ObjectIdentity
pdn_interfaces = _Pdn_interfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6)
)
_Ent_ds1_ObjectIdentity = ObjectIdentity
ent_ds1 = _Ent_ds1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5)
)
_CrossConnect_ObjectIdentity = ObjectIdentity
crossConnect = _CrossConnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 7)
)
_Xdsl_ObjectIdentity = ObjectIdentity
xdsl = _Xdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 8)
)
_PdnFrameRelay_ObjectIdentity = ObjectIdentity
pdnFrameRelay = _PdnFrameRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 9)
)
_PdnAtm_ObjectIdentity = ObjectIdentity
pdnAtm = _PdnAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11)
)
_PdnIfExt_ObjectIdentity = ObjectIdentity
pdnIfExt = _PdnIfExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12)
)
_PdnSonetMIB_ObjectIdentity = ObjectIdentity
pdnSonetMIB = _PdnSonetMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13)
)
_PdnDs3MIB_ObjectIdentity = ObjectIdentity
pdnDs3MIB = _PdnDs3MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14)
)
_Pdnmsdsl_ObjectIdentity = ObjectIdentity
pdnmsdsl = _Pdnmsdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 15)
)
_PdnIsdn_ObjectIdentity = ObjectIdentity
pdnIsdn = _PdnIsdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 16)
)
_PdnMgmtLink_ObjectIdentity = ObjectIdentity
pdnMgmtLink = _PdnMgmtLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 17)
)
_PdnDiagPortal_ObjectIdentity = ObjectIdentity
pdnDiagPortal = _PdnDiagPortal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 18)
)
_PdnReachDSL_ObjectIdentity = ObjectIdentity
pdnReachDSL = _PdnReachDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20)
)
_Pdn_devConfig_ObjectIdentity = ObjectIdentity
pdn_devConfig = _Pdn_devConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7)
)
_Pdn_security_ObjectIdentity = ObjectIdentity
pdn_security = _Pdn_security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 8)
)
_Pdn_traps_ObjectIdentity = ObjectIdentity
pdn_traps = _Pdn_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 9)
)
_Pdn_ipInjection_ObjectIdentity = ObjectIdentity
pdn_ipInjection = _Pdn_ipInjection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 11)
)
_Pdn_ip_ObjectIdentity = ObjectIdentity
pdn_ip = _Pdn_ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 12)
)
_Pdn_fileXfer_ObjectIdentity = ObjectIdentity
pdn_fileXfer = _Pdn_fileXfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 14)
)
_Pdn_feature_ObjectIdentity = ObjectIdentity
pdn_feature = _Pdn_feature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 15)
)
_Pdn_diagnostics_ObjectIdentity = ObjectIdentity
pdn_diagnostics = _Pdn_diagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16)
)
_Pdn_dns_ObjectIdentity = ObjectIdentity
pdn_dns = _Pdn_dns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17)
)
_Pdn_ether_ObjectIdentity = ObjectIdentity
pdn_ether = _Pdn_ether_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18)
)
_Pdn_socket_ObjectIdentity = ObjectIdentity
pdn_socket = _Pdn_socket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19)
)
_Pdn_time_ObjectIdentity = ObjectIdentity
pdn_time = _Pdn_time_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20)
)
_Pdn_bridge_ObjectIdentity = ObjectIdentity
pdn_bridge = _Pdn_bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 21)
)
_Pdn_domain_ObjectIdentity = ObjectIdentity
pdn_domain = _Pdn_domain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22)
)
_Pdn_filter_ObjectIdentity = ObjectIdentity
pdn_filter = _Pdn_filter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 23)
)
_Pdn_dslam_ObjectIdentity = ObjectIdentity
pdn_dslam = _Pdn_dslam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24)
)
_Pdn_radius_ObjectIdentity = ObjectIdentity
pdn_radius = _Pdn_radius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 25)
)
_Pdn_inet_ObjectIdentity = ObjectIdentity
pdn_inet = _Pdn_inet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26)
)
_Pdn_arp_ObjectIdentity = ObjectIdentity
pdn_arp = _Pdn_arp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 27)
)
_Pdn_devStats_ObjectIdentity = ObjectIdentity
pdn_devStats = _Pdn_devStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 28)
)
_Pdn_dhcp_ObjectIdentity = ObjectIdentity
pdn_dhcp = _Pdn_dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 29)
)
_Pdn_nat_ObjectIdentity = ObjectIdentity
pdn_nat = _Pdn_nat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 30)
)
_Pdn_syslog_ObjectIdentity = ObjectIdentity
pdn_syslog = _Pdn_syslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 31)
)
_Pdn_dialControl_ObjectIdentity = ObjectIdentity
pdn_dialControl = _Pdn_dialControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 32)
)
_Pdn_devNetTiming_ObjectIdentity = ObjectIdentity
pdn_devNetTiming = _Pdn_devNetTiming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 33)
)
_PdnIPSec_ObjectIdentity = ObjectIdentity
pdnIPSec = _PdnIPSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 34)
)
_MpeEntitySensor_ObjectIdentity = ObjectIdentity
mpeEntitySensor = _MpeEntitySensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 35)
)
_PdnStackable_ObjectIdentity = ObjectIdentity
pdnStackable = _PdnStackable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36)
)
_PdnUplinkTagging_ObjectIdentity = ObjectIdentity
pdnUplinkTagging = _PdnUplinkTagging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37)
)
_PdnSpectrumMgr_ObjectIdentity = ObjectIdentity
pdnSpectrumMgr = _PdnSpectrumMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 38)
)
_Pdn_dot1q_ObjectIdentity = ObjectIdentity
pdn_dot1q = _Pdn_dot1q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39)
)
_PdnLinkFaultMgmt_ObjectIdentity = ObjectIdentity
pdnLinkFaultMgmt = _PdnLinkFaultMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 40)
)
_PdnEntityRedundancy_ObjectIdentity = ObjectIdentity
pdnEntityRedundancy = _PdnEntityRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41)
)
_PdnLinkLoadSharing_ObjectIdentity = ObjectIdentity
pdnLinkLoadSharing = _PdnLinkLoadSharing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 42)
)
_PdnAtmBridgeIwfMIB_ObjectIdentity = ObjectIdentity
pdnAtmBridgeIwfMIB = _PdnAtmBridgeIwfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43)
)
_PdnMpdExt_ObjectIdentity = ObjectIdentity
pdnMpdExt = _PdnMpdExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44)
)
_PdnEntitySensorExtMIB_ObjectIdentity = ObjectIdentity
pdnEntitySensorExtMIB = _PdnEntitySensorExtMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 45)
)
_PdnVlanMIB_ObjectIdentity = ObjectIdentity
pdnVlanMIB = _PdnVlanMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46)
)
_PdnIgmpStdExtMIB_ObjectIdentity = ObjectIdentity
pdnIgmpStdExtMIB = _PdnIgmpStdExtMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47)
)
_PdnIpMcastMIB_ObjectIdentity = ObjectIdentity
pdnIpMcastMIB = _PdnIpMcastMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48)
)
_PdnCpIwf_ObjectIdentity = ObjectIdentity
pdnCpIwf = _PdnCpIwf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50)
)
_Pdn_snmp_ObjectIdentity = ObjectIdentity
pdn_snmp = _Pdn_snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 3)
)
_Ent_9XXX_ObjectIdentity = ObjectIdentity
ent_9XXX = _Ent_9XXX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 3, 1)
)
_Ent_96XX_ObjectIdentity = ObjectIdentity
ent_96XX = _Ent_96XX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 3, 1, 1)
)
_Ent_bonaire_ObjectIdentity = ObjectIdentity
ent_bonaire = _Ent_bonaire_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 3, 1, 2)
)
_Ent_91XX_ObjectIdentity = ObjectIdentity
ent_91XX = _Ent_91XX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 3, 1, 3)
)
_Pdn_36xx_ObjectIdentity = ObjectIdentity
pdn_36xx = _Pdn_36xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 4)
)
_Pdn_aac_ObjectIdentity = ObjectIdentity
pdn_aac = _Pdn_aac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 5)
)
_Pdn_eagle_ObjectIdentity = ObjectIdentity
pdn_eagle = _Pdn_eagle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 6)
)
_Pdn_ar_ObjectIdentity = ObjectIdentity
pdn_ar = _Pdn_ar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 7)
)
_Pdn_as_ObjectIdentity = ObjectIdentity
pdn_as = _Pdn_as_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 8)
)
_Pdn_xdsl_ObjectIdentity = ObjectIdentity
pdn_xdsl = _Pdn_xdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9)
)
_Ent_5100_ObjectIdentity = ObjectIdentity
ent_5100 = _Ent_5100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 1)
)
_Ent_8800_ObjectIdentity = ObjectIdentity
ent_8800 = _Ent_8800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3)
)
_Ent_8600_ObjectIdentity = ObjectIdentity
ent_8600 = _Ent_8600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 5)
)
_Pdn_sle_ObjectIdentity = ObjectIdentity
pdn_sle = _Pdn_sle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 6)
)
_Pdn_comp_ObjectIdentity = ObjectIdentity
pdn_comp = _Pdn_comp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 10)
)
_Ent_9028_ObjectIdentity = ObjectIdentity
ent_9028 = _Ent_9028_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 10, 1)
)
_Pdn_ptc_ObjectIdentity = ObjectIdentity
pdn_ptc = _Pdn_ptc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 11)
)
_Ent_ptc_ObjectIdentity = ObjectIdentity
ent_ptc = _Ent_ptc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 11, 1)
)
_Pdn_mpe_ObjectIdentity = ObjectIdentity
pdn_mpe = _Pdn_mpe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12)
)
_Mpe_mib2_ObjectIdentity = ObjectIdentity
mpe_mib2 = _Mpe_mib2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 4)
)
_Mpe_devHealth_ObjectIdentity = ObjectIdentity
mpe_devHealth = _Mpe_devHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 7)
)
_Mpe_bridge_ObjectIdentity = ObjectIdentity
mpe_bridge = _Mpe_bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21)
)
_Mpe_domain_ObjectIdentity = ObjectIdentity
mpe_domain = _Mpe_domain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22)
)
_Mpe_filter_ObjectIdentity = ObjectIdentity
mpe_filter = _Mpe_filter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23)
)
_Mpe_dslam_ObjectIdentity = ObjectIdentity
mpe_dslam = _Mpe_dslam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24)
)
_Mpe_arp_ObjectIdentity = ObjectIdentity
mpe_arp = _Mpe_arp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27)
)
_Mpe_devStats_ObjectIdentity = ObjectIdentity
mpe_devStats = _Mpe_devStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 28)
)
_Mpe_devConfig_ObjectIdentity = ObjectIdentity
mpe_devConfig = _Mpe_devConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 29)
)
_Mpe_atm_ObjectIdentity = ObjectIdentity
mpe_atm = _Mpe_atm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 30)
)
_Pdn_experimental_ObjectIdentity = ObjectIdentity
pdn_experimental = _Pdn_experimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 13)
)
_Pdn_ietf_drafts_ObjectIdentity = ObjectIdentity
pdn_ietf_drafts = _Pdn_ietf_drafts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14)
)
_Cellsaver_mibs_ObjectIdentity = ObjectIdentity
cellsaver_mibs = _Cellsaver_mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 15)
)
_Cornet_mibs_ObjectIdentity = ObjectIdentity
cornet_mibs = _Cornet_mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 16)
)
_Ip_stackable_mibs_ObjectIdentity = ObjectIdentity
ip_stackable_mibs = _Ip_stackable_mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 17)
)
_Etherloop_mib_ObjectIdentity = ObjectIdentity
etherloop_mib = _Etherloop_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 18)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-HEADER-MIB",
    **{"pdyn": pdyn,
       "pdn-products": pdn_products,
       "paradyneNMS-products": paradyneNMS_products,
       "nms-6700-products": nms_6700_products,
       "nms-dce-products": nms_dce_products,
       "nms-gem-products": nms_gem_products,
       "gem-aac-341": gem_aac_341,
       "nms-logical-products": nms_logical_products,
       "iso-physical": iso_physical,
       "iso-link": iso_link,
       "iso-network": iso_network,
       "access-router": access_router,
       "iso-transport": iso_transport,
       "iso-session": iso_session,
       "iso-presentation": iso_presentation,
       "iso-application": iso_application,
       "chassis-manager": chassis_manager,
       "paradyne-products": paradyne_products,
       "pdn-cellRelay-products": pdn_cellRelay_products,
       "pdn-snmp-products": pdn_snmp_products,
       "csu": csu,
       "t1-3150": t1_3150,
       "t1-3151": t1_3151,
       "dsu-csu": dsu_csu,
       "t1-3160": t1_3160,
       "t1-3164": t1_3164,
       "t1-3165": t1_3165,
       "t1-3161": t1_3161,
       "e1-3172": e1_3172,
       "e1-3174": e1_3174,
       "t1-3162": t1_3162,
       "t1-3166": t1_3166,
       "ntu": ntu,
       "e1-3350": e1_3350,
       "e1-3360": e1_3360,
       "e1-3364": e1_3364,
       "e1-3365": e1_3365,
       "dev9XXX": dev9XXX,
       "fr-96XX": fr_96XX,
       "fr-9620": fr_9620,
       "fr-2slot": fr_2slot,
       "fr-naf": fr_naf,
       "fr-nac": fr_nac,
       "fr-9624": fr_9624,
       "fr-9626": fr_9626,
       "fr-9623": fr_9623,
       "fr-9624-OS": fr_9624_OS,
       "bonaire": bonaire,
       "bonaire-1slot": bonaire_1slot,
       "bonaire-2slot": bonaire_2slot,
       "bonaire-naf": bonaire_naf,
       "bonaire-nac": bonaire_nac,
       "t1-916X": t1_916X,
       "t1-1slot": t1_1slot,
       "t1-9162": t1_9162,
       "t1-9165": t1_9165,
       "t1-nac": t1_nac,
       "t1-9262": t1_9262,
       "t1-9265": t1_9265,
       "t1-9161": t1_9161,
       "t1-9261": t1_9261,
       "t1fr-912X": t1fr_912X,
       "t1fr-9121": t1fr_9121,
       "t1fr-2slot": t1fr_2slot,
       "t1fr-naf": t1fr_naf,
       "t1fr-nac": t1fr_nac,
       "t1fr-9124": t1fr_9124,
       "t1fr-9124-NNI": t1fr_9124_NNI,
       "t1fr-9126": t1fr_9126,
       "t1fr-9128": t1fr_9128,
       "t1fr-9124-II": t1fr_9124_II,
       "t1fr-9124-L": t1fr_9124_L,
       "t1fr-9123": t1fr_9123,
       "t1fr-9124-OS": t1fr_9124_OS,
       "atm-95XX": atm_95XX,
       "atm-9580": atm_9580,
       "atm-9520-ilm": atm_9520_ilm,
       "atm-9520": atm_9520,
       "msa-919X": msa_919X,
       "msa-9192": msa_9192,
       "msa-9195": msa_9195,
       "msa-9292": msa_9292,
       "msa-9295": msa_9295,
       "int-98XX": int_98XX,
       "int-9820": int_9820,
       "int-9820-C": int_9820_C,
       "int-9820-8M": int_9820_8M,
       "int-9820-45M": int_9820_45M,
       "nni-9XXX": nni_9XXX,
       "nni-9110": nni_9110,
       "msdsl-9XXX": msdsl_9XXX,
       "msdsl-9723": msdsl_9723,
       "msdsl-9783": msdsl_9783,
       "msdsl-9720": msdsl_9720,
       "msdsl-9788": msdsl_9788,
       "isdn-9XXX": isdn_9XXX,
       "isdn-9664": isdn_9664,
       "rtr-9XXX": rtr_9XXX,
       "rtr-9783": rtr_9783,
       "rtr-9720": rtr_9720,
       "rtr-9788": rtr_9788,
       "rtr-9126": rtr_9126,
       "rtr-9123": rtr_9123,
       "rtr-9623": rtr_9623,
       "t1-7XXX": t1_7XXX,
       "t1-7123": t1_7123,
       "dev7XXX": dev7XXX,
       "dds-76XX": dds_76XX,
       "dds-7610": dds_7610,
       "dds-7612": dds_7612,
       "dds-7613": dds_7613,
       "t1-71XX": t1_71XX,
       "t1-7110": t1_7110,
       "t1-7112": t1_7112,
       "pdn-36xx-products": pdn_36xx_products,
       "pdn-aac-products": pdn_aac_products,
       "aac-34": aac_34,
       "aac-34X": aac_34X,
       "aac-FL": aac_FL,
       "aac-UE": aac_UE,
       "aac-FP": aac_FP,
       "aac-300": aac_300,
       "aac-cards": aac_cards,
       "aac-frs": aac_frs,
       "aac-ipc": aac_ipc,
       "aac-atm": aac_atm,
       "aac-4X": aac_4X,
       "aac-4XFL": aac_4XFL,
       "aac-4XUE": aac_4XUE,
       "aac-4XFP": aac_4XFP,
       "aac-4X300": aac_4X300,
       "pdn-common-products": pdn_common_products,
       "pdn-testOIDs": pdn_testOIDs,
       "pdnLoopbackTest": pdnLoopbackTest,
       "pdnBertTest": pdnBertTest,
       "pdnPingTest": pdnPingTest,
       "pdnTraceRouteTest": pdnTraceRouteTest,
       "pdnBlertTest": pdnBlertTest,
       "pdn-eagle-products": pdn_eagle_products,
       "pdn-ar-products": pdn_ar_products,
       "ar-541": ar_541,
       "ar-611": ar_611,
       "ar-621": ar_621,
       "ar-641": ar_641,
       "ar-712": ar_712,
       "ar-722": ar_722,
       "ar-928": ar_928,
       "ar-711": ar_711,
       "pdn-as-products": pdn_as_products,
       "as-4": as_4,
       "as-8": as_8,
       "as-24": as_24,
       "pdn-xdsl-products": pdn_xdsl_products,
       "xdsl-5100": xdsl_5100,
       "xdsl-unused1": xdsl_unused1,
       "xdsl-8800-old": xdsl_8800_old,
       "xdsl-unused2": xdsl_unused2,
       "xdsl-8600-old": xdsl_8600_old,
       "xdsl-ipc": xdsl_ipc,
       "xdsl-8100": xdsl_8100,
       "xdsl-8200": xdsl_8200,
       "xdsl-chassis": xdsl_chassis,
       "xdsl-8600": xdsl_8600,
       "xdsl-8800": xdsl_8800,
       "xdsl-8610": xdsl_8610,
       "xdsl-8810": xdsl_8810,
       "xdsl-8820": xdsl_8820,
       "xdsl-8610-X": xdsl_8610_X,
       "xdsl-8810-X": xdsl_8810_X,
       "xdsl-8820-X": xdsl_8820_X,
       "xdsl-8620": xdsl_8620,
       "xdsl-remote": xdsl_remote,
       "xdsl-5446": xdsl_5446,
       "xdsl-7914": xdsl_7914,
       "xdsl-5246": xdsl_5246,
       "xdsl-5216": xdsl_5216,
       "xdsl-5170": xdsl_5170,
       "xdsl-5171": xdsl_5171,
       "xdsl-5546": xdsl_5546,
       "xdsl-5620": xdsl_5620,
       "xdsl-6310": xdsl_6310,
       "xdsl-7975": xdsl_7975,
       "xdsl-7976": xdsl_7976,
       "xdsl-7974": xdsl_7974,
       "xdsl-7986": xdsl_7986,
       "xdsl-7985": xdsl_7985,
       "xdsl-7984": xdsl_7984,
       "xdsl-6341": xdsl_6341,
       "xdsl-6342": xdsl_6342,
       "xdsl-6331": xdsl_6331,
       "xdsl-6332": xdsl_6332,
       "xdsl-6371": xdsl_6371,
       "xdsl-6372": xdsl_6372,
       "xdsl-6321": xdsl_6321,
       "xdsl-6322": xdsl_6322,
       "xdsl-6341R2": xdsl_6341R2,
       "xdsl-6342R2": xdsl_6342R2,
       "xdsl-6331R2": xdsl_6331R2,
       "xdsl-6332R2": xdsl_6332R2,
       "xdsl-6371R2": xdsl_6371R2,
       "xdsl-6372R2": xdsl_6372R2,
       "xdsl-6321R2": xdsl_6321R2,
       "xdsl-6322R2": xdsl_6322R2,
       "xdsl-6328": xdsl_6328,
       "xdsl-6329": xdsl_6329,
       "xdsl-6301R2": xdsl_6301R2,
       "xdsl-6302R2": xdsl_6302R2,
       "xdsl-6350": xdsl_6350,
       "xdsl-6351": xdsl_6351,
       "xdsl-6385": xdsl_6385,
       "xdsl-7994": xdsl_7994,
       "xdsl-7995": xdsl_7995,
       "xdsl-7996": xdsl_7996,
       "xdsl-cards": xdsl_cards,
       "card-mcc": card_mcc,
       "card-adsl": card_adsl,
       "card-radsl": card_radsl,
       "card-sdsl": card_sdsl,
       "card-vdsl": card_vdsl,
       "card-8774": card_8774,
       "card-8540": card_8540,
       "card-8775": card_8775,
       "card-8776": card_8776,
       "card-8786": card_8786,
       "card-8946": card_8946,
       "card-8510": card_8510,
       "card-8310": card_8310,
       "card-e1-sdsl": card_e1_sdsl,
       "card-mcc2": card_mcc2,
       "card-8785": card_8785,
       "card-8784": card_8784,
       "card-8312": card_8312,
       "card-8344": card_8344,
       "card-mcc-plus": card_mcc_plus,
       "card-mcp": card_mcp,
       "card-8334": card_8334,
       "card-xxxx": card_xxxx,
       "card-8343": card_8343,
       "card-8333": card_8333,
       "card-8719": card_8719,
       "card-8747": card_8747,
       "card-8777": card_8777,
       "card-8779": card_8779,
       "card-8021": card_8021,
       "card-8022": card_8022,
       "card-8373": card_8373,
       "card-8374": card_8374,
       "card-8323": card_8323,
       "card-8324": card_8324,
       "card-8023": card_8023,
       "card-8024": card_8024,
       "card-8335": card_8335,
       "card-8365": card_8365,
       "card-83xx": card_83xx,
       "card-8314": card_8314,
       "card-8328": card_8328,
       "card-8329": card_8329,
       "card-8303": card_8303,
       "card-8304": card_8304,
       "card-8025": card_8025,
       "card-8026": card_8026,
       "card-8027": card_8027,
       "card-8028": card_8028,
       "card-8379": card_8379,
       "card-8312-ReachDSL": card_8312_ReachDSL,
       "card-8314-ReachDSL": card_8314_ReachDSL,
       "card-8385": card_8385,
       "card-8395": card_8395,
       "card-8396": card_8396,
       "card-8797": card_8797,
       "card-8799": card_8799,
       "card-8355": card_8355,
       "card-mcp8900": card_mcp8900,
       "xdsl-ports": xdsl_ports,
       "port-dsl": port_dsl,
       "port-mvl": port_mvl,
       "port-eth10": port_eth10,
       "port-eth100": port_eth100,
       "port-oc3": port_oc3,
       "port-ds3": port_ds3,
       "port-sar": port_sar,
       "port-hdlc": port_hdlc,
       "port-e3": port_e3,
       "port-ds1": port_ds1,
       "port-e1": port_e1,
       "port-ima": port_ima,
       "port-reachDsl": port_reachDsl,
       "port-reachDslV3": port_reachDslV3,
       "xdsl-slots": xdsl_slots,
       "slot-std": slot_std,
       "xdsl-components": xdsl_components,
       "comp-powerA": comp_powerA,
       "comp-powerB": comp_powerB,
       "comp-fan": comp_fan,
       "comp-mgmt": comp_mgmt,
       "comp-atm": comp_atm,
       "comp-pld": comp_pld,
       "comp-sensor": comp_sensor,
       "xdsl-sme": xdsl_sme,
       "sme-scp-cards": sme_scp_cards,
       "sme-scp-8412-card": sme_scp_8412_card,
       "sme-scp-8413-card": sme_scp_8413_card,
       "sme-scp-8414-card": sme_scp_8414_card,
       "sme-scp-8416-card": sme_scp_8416_card,
       "sme-scp-8417-card": sme_scp_8417_card,
       "sme-scp-8418-card": sme_scp_8418_card,
       "sme-childcards": sme_childcards,
       "sme-t1e1-uplink-child": sme_t1e1_uplink_child,
       "sme-ports": sme_ports,
       "sme-reachDsl-port": sme_reachDsl_port,
       "sme-adsl-a-port": sme_adsl_a_port,
       "sme-adsl-b-port": sme_adsl_b_port,
       "sme-shdsl-port": sme_shdsl_port,
       "sme-t1e1-port": sme_t1e1_port,
       "sme-oc3-port": sme_oc3_port,
       "sme-rs232-port": sme_rs232_port,
       "sme-eth-port": sme_eth_port,
       "sme-ds3-port": sme_ds3_port,
       "sme-portcards": sme_portcards,
       "sme-8965-card": sme_8965_card,
       "sme-8955-card": sme_8955_card,
       "sme-8985-card": sme_8985_card,
       "sme-chassis": sme_chassis,
       "sme-chassis-8820": sme_chassis_8820,
       "sme-chassis-8620": sme_chassis_8620,
       "sme-components": sme_components,
       "sme-comp-fan": sme_comp_fan,
       "sme-comp-pld": sme_comp_pld,
       "sme-comp-sensor": sme_comp_sensor,
       "sme-comp-powersupply": sme_comp_powersupply,
       "sme-comp-spf": sme_comp_spf,
       "sme-container": sme_container,
       "pdn-comp-products": pdn_comp_products,
       "comp-9028": comp_9028,
       "pdn-ptc-products": pdn_ptc_products,
       "xdsl-xdsl": xdsl_xdsl,
       "pdnDslEndpoint": pdnDslEndpoint,
       "reserved13": reserved13,
       "reserved14": reserved14,
       "pdn-cellsaver": pdn_cellsaver,
       "cellsaver-9510": cellsaver_9510,
       "cellsaver-9550": cellsaver_9550,
       "pdn-cornet": pdn_cornet,
       "cornet-xxxx": cornet_xxxx,
       "ip-stackable": ip_stackable,
       "ips-stack": ips_stack,
       "ips-4800": ips_4800,
       "ips-2600": ips_2600,
       "ips-4200": ips_4200,
       "ips-chassis": ips_chassis,
       "ips-4821": ips_4821,
       "ips-2611": ips_2611,
       "ips-2621": ips_2621,
       "ips-4219": ips_4219,
       "ips-4229": ips_4229,
       "ips-fixed-cards": ips_fixed_cards,
       "ips-24port-adsl-main-card": ips_24port_adsl_main_card,
       "ips-24port-adsl-child-card": ips_24port_adsl_child_card,
       "ips-maui-card": ips_maui_card,
       "ips-pots-splitter-child-card": ips_pots_splitter_child_card,
       "ips-24port-reachDsl-main-card": ips_24port_reachDsl_main_card,
       "ips-24port-reachDsl-child-card": ips_24port_reachDsl_child_card,
       "ips-pluggable-cards": ips_pluggable_cards,
       "ips-mgmt-no-wan": ips_mgmt_no_wan,
       "ips-mgmt-with-v35x21-wan": ips_mgmt_with_v35x21_wan,
       "ips-mgmt-with-t1e1-mlppp-wan": ips_mgmt_with_t1e1_mlppp_wan,
       "ips-mgmt-with-t1e1-ima-wan": ips_mgmt_with_t1e1_ima_wan,
       "ips-ports": ips_ports,
       "ips-rs232-dte-port": ips_rs232_dte_port,
       "ips-rs232-dce-port": ips_rs232_dce_port,
       "ips-v35-dte-port": ips_v35_dte_port,
       "ips-adsl-port": ips_adsl_port,
       "ips-ethernet-port": ips_ethernet_port,
       "ips-t1e1-port": ips_t1e1_port,
       "ips-adsl-a-port": ips_adsl_a_port,
       "ips-reachDslPort": ips_reachDslPort,
       "ips-components": ips_components,
       "ips-fan": ips_fan,
       "ips-temperature-sensor": ips_temperature_sensor,
       "ips-processor": ips_processor,
       "ips-pld": ips_pld,
       "ips-speed-sensor": ips_speed_sensor,
       "ips-alarm-relay-contact": ips_alarm_relay_contact,
       "ips-dot1dBasePortCircuit": ips_dot1dBasePortCircuit,
       "ips-piwg-1": ips_piwg_1,
       "ips-piwg-2": ips_piwg_2,
       "ips-piwg-3": ips_piwg_3,
       "ips-piwg-4": ips_piwg_4,
       "ips-piwg-5": ips_piwg_5,
       "ips-piwg-6": ips_piwg_6,
       "ips-piwg-7": ips_piwg_7,
       "ips-piwg-8": ips_piwg_8,
       "etherloop": etherloop,
       "eloop-shelf": eloop_shelf,
       "eloop-2400": eloop_2400,
       "eloop-unit": eloop_unit,
       "eloop-2461": eloop_2461,
       "eloop-modem-stick": eloop_modem_stick,
       "eloop-intf-card": eloop_intf_card,
       "eloop-switch-card": eloop_switch_card,
       "atm-stackable": atm_stackable,
       "atmstk-stack": atmstk_stack,
       "atmstk-4200": atmstk_4200,
       "atmstk-chassis": atmstk_chassis,
       "atmstk-4216": atmstk_4216,
       "atmstk-4218": atmstk_4218,
       "atmstk-4210": atmstk_4210,
       "atmstk-4211": atmstk_4211,
       "atmstk-4212": atmstk_4212,
       "atmstk-4213": atmstk_4213,
       "atmstk-4221": atmstk_4221,
       "atmstk-4222": atmstk_4222,
       "atmstk-4223": atmstk_4223,
       "atmstk-4231": atmstk_4231,
       "atmstk-4232": atmstk_4232,
       "atmstk-4233": atmstk_4233,
       "atmstk-cards": atmstk_cards,
       "atmstk-24Port-main-reach": atmstk_24Port_main_reach,
       "atmstk-24Port-main-adsl-a": atmstk_24Port_main_adsl_a,
       "atmstk-24Port-main-adsl-b": atmstk_24Port_main_adsl_b,
       "atmstk-child-cards": atmstk_child_cards,
       "atmstk-4201-t1-uplink": atmstk_4201_t1_uplink,
       "atmstk-4202-e1-uplink": atmstk_4202_e1_uplink,
       "atmstk-4203-t1e1-ima-uplink": atmstk_4203_t1e1_ima_uplink,
       "atmstk-oc3-uplink": atmstk_oc3_uplink,
       "atmstk-splitter": atmstk_splitter,
       "atmstk-24Port-ext": atmstk_24Port_ext,
       "atmstk-ports": atmstk_ports,
       "atmstk-reachDsl-port": atmstk_reachDsl_port,
       "atmstk-t1e1-port": atmstk_t1e1_port,
       "atmstk-rs232-dce-port": atmstk_rs232_dce_port,
       "atmstk-ethernet-port": atmstk_ethernet_port,
       "atmstk-ADSL-annexa-port": atmstk_ADSL_annexa_port,
       "atmstk-ADSL-annexb-port": atmstk_ADSL_annexb_port,
       "atmstk-components": atmstk_components,
       "atmstk-comp-fan": atmstk_comp_fan,
       "atmstk-comp-temp-sensor": atmstk_comp_temp_sensor,
       "atmstk-comp-pld": atmstk_comp_pld,
       "pdn-mgmt": pdn_mgmt,
       "paradyneNMS": paradyneNMS,
       "nms-6700": nms_6700,
       "paradyne": paradyne,
       "pdn-cellRelay": pdn_cellRelay,
       "pdn-common": pdn_common,
       "pdn-frontPanel": pdn_frontPanel,
       "pdn-chassis": pdn_chassis,
       "pdn-callDir": pdn_callDir,
       "pdn-devStatus": pdn_devStatus,
       "pdn-devID": pdn_devID,
       "pdn-interfaces": pdn_interfaces,
       "ent-ds1": ent_ds1,
       "crossConnect": crossConnect,
       "xdsl": xdsl,
       "pdnFrameRelay": pdnFrameRelay,
       "pdnAtm": pdnAtm,
       "pdnIfExt": pdnIfExt,
       "pdnSonetMIB": pdnSonetMIB,
       "pdnDs3MIB": pdnDs3MIB,
       "pdnmsdsl": pdnmsdsl,
       "pdnIsdn": pdnIsdn,
       "pdnMgmtLink": pdnMgmtLink,
       "pdnDiagPortal": pdnDiagPortal,
       "pdnReachDSL": pdnReachDSL,
       "pdn-devConfig": pdn_devConfig,
       "pdn-security": pdn_security,
       "pdn-traps": pdn_traps,
       "pdn-ipInjection": pdn_ipInjection,
       "pdn-ip": pdn_ip,
       "pdn-fileXfer": pdn_fileXfer,
       "pdn-feature": pdn_feature,
       "pdn-diagnostics": pdn_diagnostics,
       "pdn-dns": pdn_dns,
       "pdn-ether": pdn_ether,
       "pdn-socket": pdn_socket,
       "pdn-time": pdn_time,
       "pdn-bridge": pdn_bridge,
       "pdn-domain": pdn_domain,
       "pdn-filter": pdn_filter,
       "pdn-dslam": pdn_dslam,
       "pdn-radius": pdn_radius,
       "pdn-inet": pdn_inet,
       "pdn-arp": pdn_arp,
       "pdn-devStats": pdn_devStats,
       "pdn-dhcp": pdn_dhcp,
       "pdn-nat": pdn_nat,
       "pdn-syslog": pdn_syslog,
       "pdn-dialControl": pdn_dialControl,
       "pdn-devNetTiming": pdn_devNetTiming,
       "pdnIPSec": pdnIPSec,
       "mpeEntitySensor": mpeEntitySensor,
       "pdnStackable": pdnStackable,
       "pdnUplinkTagging": pdnUplinkTagging,
       "pdnSpectrumMgr": pdnSpectrumMgr,
       "pdn-dot1q": pdn_dot1q,
       "pdnLinkFaultMgmt": pdnLinkFaultMgmt,
       "pdnEntityRedundancy": pdnEntityRedundancy,
       "pdnLinkLoadSharing": pdnLinkLoadSharing,
       "pdnAtmBridgeIwfMIB": pdnAtmBridgeIwfMIB,
       "pdnMpdExt": pdnMpdExt,
       "pdnEntitySensorExtMIB": pdnEntitySensorExtMIB,
       "pdnVlanMIB": pdnVlanMIB,
       "pdnIgmpStdExtMIB": pdnIgmpStdExtMIB,
       "pdnIpMcastMIB": pdnIpMcastMIB,
       "pdnCpIwf": pdnCpIwf,
       "pdn-snmp": pdn_snmp,
       "ent-9XXX": ent_9XXX,
       "ent-96XX": ent_96XX,
       "ent-bonaire": ent_bonaire,
       "ent-91XX": ent_91XX,
       "pdn-36xx": pdn_36xx,
       "pdn-aac": pdn_aac,
       "pdn-eagle": pdn_eagle,
       "pdn-ar": pdn_ar,
       "pdn-as": pdn_as,
       "pdn-xdsl": pdn_xdsl,
       "ent-5100": ent_5100,
       "ent-8800": ent_8800,
       "ent-8600": ent_8600,
       "pdn-sle": pdn_sle,
       "pdn-comp": pdn_comp,
       "ent-9028": ent_9028,
       "pdn-ptc": pdn_ptc,
       "ent-ptc": ent_ptc,
       "pdn-mpe": pdn_mpe,
       "mpe-mib2": mpe_mib2,
       "mpe-devHealth": mpe_devHealth,
       "mpe-bridge": mpe_bridge,
       "mpe-domain": mpe_domain,
       "mpe-filter": mpe_filter,
       "mpe-dslam": mpe_dslam,
       "mpe-arp": mpe_arp,
       "mpe-devStats": mpe_devStats,
       "mpe-devConfig": mpe_devConfig,
       "mpe-atm": mpe_atm,
       "pdn-experimental": pdn_experimental,
       "pdn-ietf-drafts": pdn_ietf_drafts,
       "cellsaver-mibs": cellsaver_mibs,
       "cornet-mibs": cornet_mibs,
       "ip-stackable-mibs": ip_stackable_mibs,
       "etherloop-mib": etherloop_mib}
)
