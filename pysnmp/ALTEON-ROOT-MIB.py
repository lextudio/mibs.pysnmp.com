# SNMP MIB module (ALTEON-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTEON-ROOT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:48 2024
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

_Alteon_ObjectIdentity = ObjectIdentity
alteon = _Alteon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872)
)
_Registration_ObjectIdentity = ObjectIdentity
registration = _Registration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1)
)
_Aceswitch110_ObjectIdentity = ObjectIdentity
aceswitch110 = _Aceswitch110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 1)
)
_Acedirector_ObjectIdentity = ObjectIdentity
acedirector = _Acedirector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 2)
)
_Aceswitch180_ObjectIdentity = ObjectIdentity
aceswitch180 = _Aceswitch180_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 3)
)
_Acedirector2_ObjectIdentity = ObjectIdentity
acedirector2 = _Acedirector2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 4)
)
_Aceswitch180e_ObjectIdentity = ObjectIdentity
aceswitch180e = _Aceswitch180e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 5)
)
_Acedirector3_ObjectIdentity = ObjectIdentity
acedirector3 = _Acedirector3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 6)
)
_Cachedirector_ObjectIdentity = ObjectIdentity
cachedirector = _Cachedirector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 7)
)
_Gs_switches_ObjectIdentity = ObjectIdentity
gs_switches = _Gs_switches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 8)
)
_Chas_switch_ObjectIdentity = ObjectIdentity
chas_switch = _Chas_switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 8, 1)
)
_Chas_switch_reg_ObjectIdentity = ObjectIdentity
chas_switch_reg = _Chas_switch_reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 1)
)
_Alteon708_ObjectIdentity = ObjectIdentity
alteon708 = _Alteon708_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 1, 1)
)
_Chas_switch_comp_reg_ObjectIdentity = ObjectIdentity
chas_switch_comp_reg = _Chas_switch_comp_reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2)
)
_AlteonACPowerSupply7xx_ObjectIdentity = ObjectIdentity
alteonACPowerSupply7xx = _AlteonACPowerSupply7xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2, 1)
)
_AlteonDCPowerSupply7xx_ObjectIdentity = ObjectIdentity
alteonDCPowerSupply7xx = _AlteonDCPowerSupply7xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2, 2)
)
_AlteonFan708_ObjectIdentity = ObjectIdentity
alteonFan708 = _AlteonFan708_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2, 3)
)
_AlteonModuleMP_ObjectIdentity = ObjectIdentity
alteonModuleMP = _AlteonModuleMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2, 5)
)
_AlteonModuleSF_ObjectIdentity = ObjectIdentity
alteonModuleSF = _AlteonModuleSF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2, 6)
)
_AlteonModuleFE_UTP_ObjectIdentity = ObjectIdentity
alteonModuleFE_UTP = _AlteonModuleFE_UTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2, 7)
)
_AlteonModuleGE_SX_ObjectIdentity = ObjectIdentity
alteonModuleGE_SX = _AlteonModuleGE_SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2, 8)
)
_AlteonModuleGE_UTP_ObjectIdentity = ObjectIdentity
alteonModuleGE_UTP = _AlteonModuleGE_UTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2, 9)
)
_Aceswitch184_ObjectIdentity = ObjectIdentity
aceswitch184 = _Aceswitch184_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 9)
)
_Acedirector4_ObjectIdentity = ObjectIdentity
acedirector4 = _Acedirector4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 10)
)
_Isd_reg_ObjectIdentity = ObjectIdentity
isd_reg = _Isd_reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 11)
)
_AlteonContentDirector_ObjectIdentity = ObjectIdentity
alteonContentDirector = _AlteonContentDirector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 11, 1)
)
_AlteonSSLOffload_ObjectIdentity = ObjectIdentity
alteonSSLOffload = _AlteonSSLOffload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 11, 2)
)
_AlteonPersonalContentCache_ObjectIdentity = ObjectIdentity
alteonPersonalContentCache = _AlteonPersonalContentCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 11, 3)
)
_AlteonFirewall_ObjectIdentity = ObjectIdentity
alteonFirewall = _AlteonFirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 11, 4)
)
_AlteonWSS_ObjectIdentity = ObjectIdentity
alteonWSS = _AlteonWSS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 11, 5)
)
_Webswitch_module_ObjectIdentity = ObjectIdentity
webswitch_module = _Webswitch_module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 12)
)
_Aws_switches_ObjectIdentity = ObjectIdentity
aws_switches = _Aws_switches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 13)
)
_Aws2000_switches_ObjectIdentity = ObjectIdentity
aws2000_switches = _Aws2000_switches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 13, 1)
)
_Aws2424_ObjectIdentity = ObjectIdentity
aws2424 = _Aws2424_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 1)
)
_Aws2448_ObjectIdentity = ObjectIdentity
aws2448 = _Aws2448_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 2)
)
_Aws2224_ObjectIdentity = ObjectIdentity
aws2224 = _Aws2224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 3)
)
_Aas2424s_ObjectIdentity = ObjectIdentity
aas2424s = _Aas2424s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 4)
)
_Aas2208_ObjectIdentity = ObjectIdentity
aas2208 = _Aas2208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 5)
)
_Aas2216_ObjectIdentity = ObjectIdentity
aas2216 = _Aas2216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 6)
)
_Aws2424E5_ObjectIdentity = ObjectIdentity
aws2424E5 = _Aws2424E5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 7)
)
_Aas2424sE5_ObjectIdentity = ObjectIdentity
aas2424sE5 = _Aas2424sE5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 8)
)
_Aas2208E5_ObjectIdentity = ObjectIdentity
aas2208E5 = _Aas2208E5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 9)
)
_Aas2216E5_ObjectIdentity = ObjectIdentity
aas2216E5 = _Aas2216E5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 10)
)
_Aws3000_switches_ObjectIdentity = ObjectIdentity
aws3000_switches = _Aws3000_switches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 13, 2)
)
_Aws3408_ObjectIdentity = ObjectIdentity
aws3408 = _Aws3408_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 13, 2, 1)
)
_Aws3416_ObjectIdentity = ObjectIdentity
aws3416 = _Aws3416_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 13, 2, 2)
)
_Aws3408E5_ObjectIdentity = ObjectIdentity
aws3408E5 = _Aws3408E5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 13, 2, 3)
)
_Radwarealteon_switches_ObjectIdentity = ObjectIdentity
radwarealteon_switches = _Radwarealteon_switches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 13, 3)
)
_Ods4416_ObjectIdentity = ObjectIdentity
ods4416 = _Ods4416_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 13, 3, 1)
)
_Ods5412_ObjectIdentity = ObjectIdentity
ods5412 = _Ods5412_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 13, 3, 2)
)
_Ods_virt_ac_ObjectIdentity = ObjectIdentity
ods_virt_ac = _Ods_virt_ac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 13, 3, 2, 1)
)
_Ods_virt_vadc_ObjectIdentity = ObjectIdentity
ods_virt_vadc = _Ods_virt_vadc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 13, 3, 2, 2)
)
_Ods4408_ObjectIdentity = ObjectIdentity
ods4408 = _Ods4408_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 13, 3, 3)
)
_Odsva_ObjectIdentity = ObjectIdentity
odsva = _Odsva_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 13, 3, 4)
)
_Ods5224_ObjectIdentity = ObjectIdentity
ods5224 = _Ods5224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 13, 3, 5)
)
_AlteonLinkOptimizer_ObjectIdentity = ObjectIdentity
alteonLinkOptimizer = _AlteonLinkOptimizer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 14)
)
_Wsm_BladeCenter_ObjectIdentity = ObjectIdentity
wsm_BladeCenter = _Wsm_BladeCenter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 15)
)
_AlteonLinkOptimizer143_ObjectIdentity = ObjectIdentity
alteonLinkOptimizer143 = _AlteonLinkOptimizer143_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 16)
)
_AlteonLinkOptimizer150_ObjectIdentity = ObjectIdentity
alteonLinkOptimizer150 = _AlteonLinkOptimizer150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 17)
)
_Ibm_BladeCenterL3_ObjectIdentity = ObjectIdentity
ibm_BladeCenterL3 = _Ibm_BladeCenterL3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 18)
)
_CopperModule_ObjectIdentity = ObjectIdentity
copperModule = _CopperModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 18, 1)
)
_FiberModule_ObjectIdentity = ObjectIdentity
fiberModule = _FiberModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 1, 18, 2)
)
_Private_mibs_ObjectIdentity = ObjectIdentity
private_mibs = _Private_mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2)
)
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1)
)
_Gs_switch_ObjectIdentity = ObjectIdentity
gs_switch = _Gs_switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 2)
)
_Isd_ObjectIdentity = ObjectIdentity
isd = _Isd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3)
)
_Platform_ObjectIdentity = ObjectIdentity
platform = _Platform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1)
)
_SslOffload_ObjectIdentity = ObjectIdentity
sslOffload = _SslOffload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 2)
)
_Firewall_ObjectIdentity = ObjectIdentity
firewall = _Firewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3)
)
_ContentDirector_ObjectIdentity = ObjectIdentity
contentDirector = _ContentDirector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 4)
)
_Switch_chassis_ObjectIdentity = ObjectIdentity
switch_chassis = _Switch_chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 4)
)
_Chassis_8600_ObjectIdentity = ObjectIdentity
chassis_8600 = _Chassis_8600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 4, 1)
)
_Wsm4Traps_ObjectIdentity = ObjectIdentity
wsm4Traps = _Wsm4Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 4, 1, 2)
)
_Aws_switch_ObjectIdentity = ObjectIdentity
aws_switch = _Aws_switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5)
)
_Virt_admin_ObjectIdentity = ObjectIdentity
virt_admin = _Virt_admin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6)
)
_PersonalContentCache_ObjectIdentity = ObjectIdentity
personalContentCache = _PersonalContentCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 3)
)
_Ics_ObjectIdentity = ObjectIdentity
ics = _Ics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 3, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTEON-ROOT-MIB",
    **{"alteon": alteon,
       "registration": registration,
       "aceswitch110": aceswitch110,
       "acedirector": acedirector,
       "aceswitch180": aceswitch180,
       "acedirector2": acedirector2,
       "aceswitch180e": aceswitch180e,
       "acedirector3": acedirector3,
       "cachedirector": cachedirector,
       "gs-switches": gs_switches,
       "chas-switch": chas_switch,
       "chas-switch-reg": chas_switch_reg,
       "alteon708": alteon708,
       "chas-switch-comp-reg": chas_switch_comp_reg,
       "alteonACPowerSupply7xx": alteonACPowerSupply7xx,
       "alteonDCPowerSupply7xx": alteonDCPowerSupply7xx,
       "alteonFan708": alteonFan708,
       "alteonModuleMP": alteonModuleMP,
       "alteonModuleSF": alteonModuleSF,
       "alteonModuleFE-UTP": alteonModuleFE_UTP,
       "alteonModuleGE-SX": alteonModuleGE_SX,
       "alteonModuleGE-UTP": alteonModuleGE_UTP,
       "aceswitch184": aceswitch184,
       "acedirector4": acedirector4,
       "isd-reg": isd_reg,
       "alteonContentDirector": alteonContentDirector,
       "alteonSSLOffload": alteonSSLOffload,
       "alteonPersonalContentCache": alteonPersonalContentCache,
       "alteonFirewall": alteonFirewall,
       "alteonWSS": alteonWSS,
       "webswitch-module": webswitch_module,
       "aws-switches": aws_switches,
       "aws2000-switches": aws2000_switches,
       "aws2424": aws2424,
       "aws2448": aws2448,
       "aws2224": aws2224,
       "aas2424s": aas2424s,
       "aas2208": aas2208,
       "aas2216": aas2216,
       "aws2424E5": aws2424E5,
       "aas2424sE5": aas2424sE5,
       "aas2208E5": aas2208E5,
       "aas2216E5": aas2216E5,
       "aws3000-switches": aws3000_switches,
       "aws3408": aws3408,
       "aws3416": aws3416,
       "aws3408E5": aws3408E5,
       "radwarealteon-switches": radwarealteon_switches,
       "ods4416": ods4416,
       "ods5412": ods5412,
       "ods-virt-ac": ods_virt_ac,
       "ods-virt-vadc": ods_virt_vadc,
       "ods4408": ods4408,
       "odsva": odsva,
       "ods5224": ods5224,
       "alteonLinkOptimizer": alteonLinkOptimizer,
       "wsm-BladeCenter": wsm_BladeCenter,
       "alteonLinkOptimizer143": alteonLinkOptimizer143,
       "alteonLinkOptimizer150": alteonLinkOptimizer150,
       "ibm-BladeCenterL3": ibm_BladeCenterL3,
       "copperModule": copperModule,
       "fiberModule": fiberModule,
       "private-mibs": private_mibs,
       "switch": switch,
       "gs-switch": gs_switch,
       "isd": isd,
       "platform": platform,
       "sslOffload": sslOffload,
       "firewall": firewall,
       "contentDirector": contentDirector,
       "switch-chassis": switch_chassis,
       "chassis-8600": chassis_8600,
       "wsm4Traps": wsm4Traps,
       "aws-switch": aws_switch,
       "virt-admin": virt_admin,
       "personalContentCache": personalContentCache,
       "ics": ics}
)
