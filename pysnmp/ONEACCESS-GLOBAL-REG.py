# SNMP MIB module (ONEACCESS-GLOBAL-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEACCESS-GLOBAL-REG
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:30 2024
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

oneAccessMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 100, 1)
)
oneAccessMIBModule.setRevisions(
        ("2015-04-21 00:00",
         "2014-09-05 00:00",
         "2013-10-16 00:00",
         "2013-06-25 00:00",
         "2013-04-25 00:00",
         "2012-03-20 00:00",
         "2011-07-29 00:00",
         "2011-06-15 00:00",
         "2011-04-10 00:01",
         "2010-08-10 00:01",
         "2010-07-08 00:01")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OneAccess_ObjectIdentity = ObjectIdentity
oneAccess = _OneAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191)
)
_OacRegistration_ObjectIdentity = ObjectIdentity
oacRegistration = _OacRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1)
)
_OacOneOsDevices_ObjectIdentity = ObjectIdentity
oacOneOsDevices = _OacOneOsDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1)
)
_OacOne10_ObjectIdentity = ObjectIdentity
oacOne10 = _OacOne10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 1)
)
_OacOne20_ObjectIdentity = ObjectIdentity
oacOne20 = _OacOne20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 2)
)
_OacOne30_ObjectIdentity = ObjectIdentity
oacOne30 = _OacOne30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 3)
)
_OacOne40_ObjectIdentity = ObjectIdentity
oacOne40 = _OacOne40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 4)
)
_OacOne50_ObjectIdentity = ObjectIdentity
oacOne50 = _OacOne50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 5)
)
_OacOne60_ObjectIdentity = ObjectIdentity
oacOne60 = _OacOne60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 6)
)
_OacOne20D_ObjectIdentity = ObjectIdentity
oacOne20D = _OacOne20D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 7)
)
_OacOne80_ObjectIdentity = ObjectIdentity
oacOne80 = _OacOne80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 8)
)
_OacOne80XM_ObjectIdentity = ObjectIdentity
oacOne80XM = _OacOne80XM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 9)
)
_OacOne100_ObjectIdentity = ObjectIdentity
oacOne100 = _OacOne100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 10)
)
_OacOne100D_ObjectIdentity = ObjectIdentity
oacOne100D = _OacOne100D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 11)
)
_OacOne150_ObjectIdentity = ObjectIdentity
oacOne150 = _OacOne150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 15)
)
_OacOne180_ObjectIdentity = ObjectIdentity
oacOne180 = _OacOne180_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 18)
)
_OacOne200_ObjectIdentity = ObjectIdentity
oacOne200 = _OacOne200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 20)
)
_OacOneCell25_ObjectIdentity = ObjectIdentity
oacOneCell25 = _OacOneCell25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 25)
)
_OacOne300_ObjectIdentity = ObjectIdentity
oacOne300 = _OacOne300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 30)
)
_OacOneCell35_ObjectIdentity = ObjectIdentity
oacOneCell35 = _OacOneCell35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 35)
)
_OacOne400_ObjectIdentity = ObjectIdentity
oacOne400 = _OacOne400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 40)
)
_OacOne70_ObjectIdentity = ObjectIdentity
oacOne70 = _OacOne70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 70)
)
_OacOne800_ObjectIdentity = ObjectIdentity
oacOne800 = _OacOne800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 80)
)
_OacOne90_ObjectIdentity = ObjectIdentity
oacOne90 = _OacOne90_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 90)
)
_OacPBXplug8_ObjectIdentity = ObjectIdentity
oacPBXplug8 = _OacPBXplug8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 100)
)
_OacPBXplug30_ObjectIdentity = ObjectIdentity
oacPBXplug30 = _OacPBXplug30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 110)
)
_OacPBXPLUG_1P_2B_ObjectIdentity = ObjectIdentity
oacPBXPLUG_1P_2B = _OacPBXPLUG_1P_2B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 111)
)
_OacPBXPLUG_1P_2B_L_ObjectIdentity = ObjectIdentity
oacPBXPLUG_1P_2B_L = _OacPBXPLUG_1P_2B_L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 112)
)
_OacPBXPLUG_4B_ObjectIdentity = ObjectIdentity
oacPBXPLUG_4B = _OacPBXPLUG_4B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 113)
)
_OacPBXPLUG_4B_L_ObjectIdentity = ObjectIdentity
oacPBXPLUG_4B_L = _OacPBXPLUG_4B_L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 114)
)
_OacPBXPLUG_4B_V2_ObjectIdentity = ObjectIdentity
oacPBXPLUG_4B_V2 = _OacPBXPLUG_4B_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 115)
)
_OacPBXPLUG_6B_ObjectIdentity = ObjectIdentity
oacPBXPLUG_6B = _OacPBXPLUG_6B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 116)
)
_OacPBXPLUG_6B_L_ObjectIdentity = ObjectIdentity
oacPBXPLUG_6B_L = _OacPBXPLUG_6B_L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 117)
)
_OacLbb130_ObjectIdentity = ObjectIdentity
oacLbb130 = _OacLbb130_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 130)
)
_OacLbb131_ObjectIdentity = ObjectIdentity
oacLbb131 = _OacLbb131_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 131)
)
_OacLbb132_ObjectIdentity = ObjectIdentity
oacLbb132 = _OacLbb132_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 132)
)
_OacLbb133_ObjectIdentity = ObjectIdentity
oacLbb133 = _OacLbb133_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 133)
)
_OacLbb134_ObjectIdentity = ObjectIdentity
oacLbb134 = _OacLbb134_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 134)
)
_OacLbb135_ObjectIdentity = ObjectIdentity
oacLbb135 = _OacLbb135_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 135)
)
_OacLbb139_ObjectIdentity = ObjectIdentity
oacLbb139 = _OacLbb139_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 139)
)
_OacLbb140_ObjectIdentity = ObjectIdentity
oacLbb140 = _OacLbb140_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 140)
)
_OacLbb141_ObjectIdentity = ObjectIdentity
oacLbb141 = _OacLbb141_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 141)
)
_OacLbb142_ObjectIdentity = ObjectIdentity
oacLbb142 = _OacLbb142_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 142)
)
_OacLbb148_ObjectIdentity = ObjectIdentity
oacLbb148 = _OacLbb148_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 148)
)
_OacLbb210_ObjectIdentity = ObjectIdentity
oacLbb210 = _OacLbb210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 210)
)
_OacLbb219_ObjectIdentity = ObjectIdentity
oacLbb219 = _OacLbb219_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 219)
)
_OacLbb230_ObjectIdentity = ObjectIdentity
oacLbb230 = _OacLbb230_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 230)
)
_OacLbb231_ObjectIdentity = ObjectIdentity
oacLbb231 = _OacLbb231_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 231)
)
_OacLbb236_ObjectIdentity = ObjectIdentity
oacLbb236 = _OacLbb236_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 236)
)
_OacLbb310_ObjectIdentity = ObjectIdentity
oacLbb310 = _OacLbb310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 310)
)
_OacLbb320_ObjectIdentity = ObjectIdentity
oacLbb320 = _OacLbb320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 320)
)
_OacLbb329_ObjectIdentity = ObjectIdentity
oacLbb329 = _OacLbb329_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 329)
)
_OacLbb330_ObjectIdentity = ObjectIdentity
oacLbb330 = _OacLbb330_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 330)
)
_OacOne410_ObjectIdentity = ObjectIdentity
oacOne410 = _OacOne410_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 410)
)
_OacOne420_ObjectIdentity = ObjectIdentity
oacOne420 = _OacOne420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 420)
)
_OacOne425_ObjectIdentity = ObjectIdentity
oacOne425 = _OacOne425_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 425)
)
_OacOne445_ObjectIdentity = ObjectIdentity
oacOne445 = _OacOne445_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 445)
)
_OacOne540_ObjectIdentity = ObjectIdentity
oacOne540 = _OacOne540_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 540)
)
_OacOne560_ObjectIdentity = ObjectIdentity
oacOne560 = _OacOne560_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 560)
)
_OacOne700_ObjectIdentity = ObjectIdentity
oacOne700 = _OacOne700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 700)
)
_OacLbb4G_ObjectIdentity = ObjectIdentity
oacLbb4G = _OacLbb4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 1000)
)
_Oac1440_ObjectIdentity = ObjectIdentity
oac1440 = _Oac1440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 1440)
)
_OacOne1510_ObjectIdentity = ObjectIdentity
oacOne1510 = _OacOne1510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 1510)
)
_OacOne1520_ObjectIdentity = ObjectIdentity
oacOne1520 = _OacOne1520_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 1520)
)
_OacOne1540_ObjectIdentity = ObjectIdentity
oacOne1540 = _OacOne1540_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 1540)
)
_OacOne1560_ObjectIdentity = ObjectIdentity
oacOne1560 = _OacOne1560_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 1, 1560)
)
_OacMIBModules_ObjectIdentity = ObjectIdentity
oacMIBModules = _OacMIBModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 100)
)
_OacProductSpecific_ObjectIdentity = ObjectIdentity
oacProductSpecific = _OacProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 2)
)
_OacGeneric_ObjectIdentity = ObjectIdentity
oacGeneric = _OacGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 3)
)
_OacGenProtocols_ObjectIdentity = ObjectIdentity
oacGenProtocols = _OacGenProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 3, 1)
)
_OacGenManagement_ObjectIdentity = ObjectIdentity
oacGenManagement = _OacGenManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 3, 10)
)
_OacEmbeddedAgentMIB_ObjectIdentity = ObjectIdentity
oacEmbeddedAgentMIB = _OacEmbeddedAgentMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 3, 10, 1)
)
_OacCapabilities_ObjectIdentity = ObjectIdentity
oacCapabilities = _OacCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 4)
)
_OacRequirements_ObjectIdentity = ObjectIdentity
oacRequirements = _OacRequirements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 5)
)
_OacExperimental_ObjectIdentity = ObjectIdentity
oacExperimental = _OacExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10)
)
_OacExpNewMIBs_ObjectIdentity = ObjectIdentity
oacExpNewMIBs = _OacExpNewMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 1)
)
_OacExpInternetDrafts_ObjectIdentity = ObjectIdentity
oacExpInternetDrafts = _OacExpInternetDrafts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 2)
)
_OacExpInternalModules_ObjectIdentity = ObjectIdentity
oacExpInternalModules = _OacExpInternalModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3)
)
_OacExpIMIp_ObjectIdentity = ObjectIdentity
oacExpIMIp = _OacExpIMIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1)
)
_OacExpIMIpNat_ObjectIdentity = ObjectIdentity
oacExpIMIpNat = _OacExpIMIpNat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1)
)
_OacExpIMIpNatStatistics_ObjectIdentity = ObjectIdentity
oacExpIMIpNatStatistics = _OacExpIMIpNatStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1)
)
_OacExpIMIpNatNotifications_ObjectIdentity = ObjectIdentity
oacExpIMIpNatNotifications = _OacExpIMIpNatNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 2)
)
_OacExpIMIpAcl_ObjectIdentity = ObjectIdentity
oacExpIMIpAcl = _OacExpIMIpAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2)
)
_OacExpIMIpAclStatistics_ObjectIdentity = ObjectIdentity
oacExpIMIpAclStatistics = _OacExpIMIpAclStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1)
)
_OacExpIMIPSec_ObjectIdentity = ObjectIdentity
oacExpIMIPSec = _OacExpIMIPSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 4)
)
_OacExpIMIpVrrp_ObjectIdentity = ObjectIdentity
oacExpIMIpVrrp = _OacExpIMIpVrrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 5)
)
_OacExpIMVrrpNotifications_ObjectIdentity = ObjectIdentity
oacExpIMVrrpNotifications = _OacExpIMVrrpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 5, 1)
)
_OacExpIMZbFw_ObjectIdentity = ObjectIdentity
oacExpIMZbFw = _OacExpIMZbFw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9)
)
_OacExpIMIPPerformanceCounters_ObjectIdentity = ObjectIdentity
oacExpIMIPPerformanceCounters = _OacExpIMIPPerformanceCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 10)
)
_OacExpIMAtm_ObjectIdentity = ObjectIdentity
oacExpIMAtm = _OacExpIMAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2)
)
_OacExpIMAtmStatistics_ObjectIdentity = ObjectIdentity
oacExpIMAtmStatistics = _OacExpIMAtmStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1)
)
_OacExpIMAtmOamStatistics_ObjectIdentity = ObjectIdentity
oacExpIMAtmOamStatistics = _OacExpIMAtmOamStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2)
)
_OacExpIMAtmAal5_ObjectIdentity = ObjectIdentity
oacExpIMAtmAal5 = _OacExpIMAtmAal5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 3)
)
_OacExpIMSystem_ObjectIdentity = ObjectIdentity
oacExpIMSystem = _OacExpIMSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3)
)
_OacExpIMManagement_ObjectIdentity = ObjectIdentity
oacExpIMManagement = _OacExpIMManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4)
)
_OacExpIMEvents_ObjectIdentity = ObjectIdentity
oacExpIMEvents = _OacExpIMEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2)
)
_OacExpIMPing_ObjectIdentity = ObjectIdentity
oacExpIMPing = _OacExpIMPing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3)
)
_OacExpIMVoice_ObjectIdentity = ObjectIdentity
oacExpIMVoice = _OacExpIMVoice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5)
)
_OacExpIMVoiceGlobalStat_ObjectIdentity = ObjectIdentity
oacExpIMVoiceGlobalStat = _OacExpIMVoiceGlobalStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 1)
)
_OacExpIMPstn_ObjectIdentity = ObjectIdentity
oacExpIMPstn = _OacExpIMPstn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 6)
)
_OacExpIMPstnNotifications_ObjectIdentity = ObjectIdentity
oacExpIMPstnNotifications = _OacExpIMPstnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 6, 0)
)
_OacExpIMIsdn_ObjectIdentity = ObjectIdentity
oacExpIMIsdn = _OacExpIMIsdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 7)
)
_OacExpIMIsdnNotifications_ObjectIdentity = ObjectIdentity
oacExpIMIsdnNotifications = _OacExpIMIsdnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 7, 0)
)
_OacExpIMDot11_ObjectIdentity = ObjectIdentity
oacExpIMDot11 = _OacExpIMDot11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 8)
)
_OacExpIMCellRadio_ObjectIdentity = ObjectIdentity
oacExpIMCellRadio = _OacExpIMCellRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 9)
)
_OacExpIMEthernet_ObjectIdentity = ObjectIdentity
oacExpIMEthernet = _OacExpIMEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 10)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-GLOBAL-REG",
    **{"oneAccess": oneAccess,
       "oacRegistration": oacRegistration,
       "oacOneOsDevices": oacOneOsDevices,
       "oacOne10": oacOne10,
       "oacOne20": oacOne20,
       "oacOne30": oacOne30,
       "oacOne40": oacOne40,
       "oacOne50": oacOne50,
       "oacOne60": oacOne60,
       "oacOne20D": oacOne20D,
       "oacOne80": oacOne80,
       "oacOne80XM": oacOne80XM,
       "oacOne100": oacOne100,
       "oacOne100D": oacOne100D,
       "oacOne150": oacOne150,
       "oacOne180": oacOne180,
       "oacOne200": oacOne200,
       "oacOneCell25": oacOneCell25,
       "oacOne300": oacOne300,
       "oacOneCell35": oacOneCell35,
       "oacOne400": oacOne400,
       "oacOne70": oacOne70,
       "oacOne800": oacOne800,
       "oacOne90": oacOne90,
       "oacPBXplug8": oacPBXplug8,
       "oacPBXplug30": oacPBXplug30,
       "oacPBXPLUG-1P-2B": oacPBXPLUG_1P_2B,
       "oacPBXPLUG-1P-2B-L": oacPBXPLUG_1P_2B_L,
       "oacPBXPLUG-4B": oacPBXPLUG_4B,
       "oacPBXPLUG-4B-L": oacPBXPLUG_4B_L,
       "oacPBXPLUG-4B-V2": oacPBXPLUG_4B_V2,
       "oacPBXPLUG-6B": oacPBXPLUG_6B,
       "oacPBXPLUG-6B-L": oacPBXPLUG_6B_L,
       "oacLbb130": oacLbb130,
       "oacLbb131": oacLbb131,
       "oacLbb132": oacLbb132,
       "oacLbb133": oacLbb133,
       "oacLbb134": oacLbb134,
       "oacLbb135": oacLbb135,
       "oacLbb139": oacLbb139,
       "oacLbb140": oacLbb140,
       "oacLbb141": oacLbb141,
       "oacLbb142": oacLbb142,
       "oacLbb148": oacLbb148,
       "oacLbb210": oacLbb210,
       "oacLbb219": oacLbb219,
       "oacLbb230": oacLbb230,
       "oacLbb231": oacLbb231,
       "oacLbb236": oacLbb236,
       "oacLbb310": oacLbb310,
       "oacLbb320": oacLbb320,
       "oacLbb329": oacLbb329,
       "oacLbb330": oacLbb330,
       "oacOne410": oacOne410,
       "oacOne420": oacOne420,
       "oacOne425": oacOne425,
       "oacOne445": oacOne445,
       "oacOne540": oacOne540,
       "oacOne560": oacOne560,
       "oacOne700": oacOne700,
       "oacLbb4G": oacLbb4G,
       "oac1440": oac1440,
       "oacOne1510": oacOne1510,
       "oacOne1520": oacOne1520,
       "oacOne1540": oacOne1540,
       "oacOne1560": oacOne1560,
       "oacMIBModules": oacMIBModules,
       "oneAccessMIBModule": oneAccessMIBModule,
       "oacProductSpecific": oacProductSpecific,
       "oacGeneric": oacGeneric,
       "oacGenProtocols": oacGenProtocols,
       "oacGenManagement": oacGenManagement,
       "oacEmbeddedAgentMIB": oacEmbeddedAgentMIB,
       "oacCapabilities": oacCapabilities,
       "oacRequirements": oacRequirements,
       "oacExperimental": oacExperimental,
       "oacExpNewMIBs": oacExpNewMIBs,
       "oacExpInternetDrafts": oacExpInternetDrafts,
       "oacExpInternalModules": oacExpInternalModules,
       "oacExpIMIp": oacExpIMIp,
       "oacExpIMIpNat": oacExpIMIpNat,
       "oacExpIMIpNatStatistics": oacExpIMIpNatStatistics,
       "oacExpIMIpNatNotifications": oacExpIMIpNatNotifications,
       "oacExpIMIpAcl": oacExpIMIpAcl,
       "oacExpIMIpAclStatistics": oacExpIMIpAclStatistics,
       "oacExpIMIPSec": oacExpIMIPSec,
       "oacExpIMIpVrrp": oacExpIMIpVrrp,
       "oacExpIMVrrpNotifications": oacExpIMVrrpNotifications,
       "oacExpIMZbFw": oacExpIMZbFw,
       "oacExpIMIPPerformanceCounters": oacExpIMIPPerformanceCounters,
       "oacExpIMAtm": oacExpIMAtm,
       "oacExpIMAtmStatistics": oacExpIMAtmStatistics,
       "oacExpIMAtmOamStatistics": oacExpIMAtmOamStatistics,
       "oacExpIMAtmAal5": oacExpIMAtmAal5,
       "oacExpIMSystem": oacExpIMSystem,
       "oacExpIMManagement": oacExpIMManagement,
       "oacExpIMEvents": oacExpIMEvents,
       "oacExpIMPing": oacExpIMPing,
       "oacExpIMVoice": oacExpIMVoice,
       "oacExpIMVoiceGlobalStat": oacExpIMVoiceGlobalStat,
       "oacExpIMPstn": oacExpIMPstn,
       "oacExpIMPstnNotifications": oacExpIMPstnNotifications,
       "oacExpIMIsdn": oacExpIMIsdn,
       "oacExpIMIsdnNotifications": oacExpIMIsdnNotifications,
       "oacExpIMDot11": oacExpIMDot11,
       "oacExpIMCellRadio": oacExpIMCellRadio,
       "oacExpIMEthernet": oacExpIMEthernet}
)
