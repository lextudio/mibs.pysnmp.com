# SNMP MIB module (LIEBERT-GP-REGISTRATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LIEBERT-GP-REGISTRATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:52 2024
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

liebertGlobalProductsRegistrationModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 1, 1)
)
liebertGlobalProductsRegistrationModule.setRevisions(
        ("2015-02-02 00:00",
         "2014-09-17 00:00",
         "2014-06-24 00:00",
         "2014-03-27 00:00",
         "2013-07-10 00:00",
         "2013-05-14 00:00",
         "2009-04-17 00:00",
         "2008-07-02 00:00",
         "2008-01-10 00:00",
         "2006-02-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Emerson_ObjectIdentity = ObjectIdentity
emerson = _Emerson_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476)
)
if mibBuilder.loadTexts:
    emerson.setStatus("current")
_LiebertCorp_ObjectIdentity = ObjectIdentity
liebertCorp = _LiebertCorp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1)
)
if mibBuilder.loadTexts:
    liebertCorp.setStatus("current")
_LiebertGlobalProducts_ObjectIdentity = ObjectIdentity
liebertGlobalProducts = _LiebertGlobalProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42)
)
if mibBuilder.loadTexts:
    liebertGlobalProducts.setStatus("current")
_LgpModuleReg_ObjectIdentity = ObjectIdentity
lgpModuleReg = _LgpModuleReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1)
)
if mibBuilder.loadTexts:
    lgpModuleReg.setStatus("current")
_LiebertModuleReg_ObjectIdentity = ObjectIdentity
liebertModuleReg = _LiebertModuleReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 1)
)
if mibBuilder.loadTexts:
    liebertModuleReg.setStatus("current")
_LiebertAgentModuleReg_ObjectIdentity = ObjectIdentity
liebertAgentModuleReg = _LiebertAgentModuleReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 2)
)
if mibBuilder.loadTexts:
    liebertAgentModuleReg.setStatus("current")
_LiebertConditionsModuleReg_ObjectIdentity = ObjectIdentity
liebertConditionsModuleReg = _LiebertConditionsModuleReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 3)
)
if mibBuilder.loadTexts:
    liebertConditionsModuleReg.setStatus("current")
_LiebertNotificationsModuleReg_ObjectIdentity = ObjectIdentity
liebertNotificationsModuleReg = _LiebertNotificationsModuleReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 4)
)
if mibBuilder.loadTexts:
    liebertNotificationsModuleReg.setStatus("current")
_LiebertEnvironmentalModuleReg_ObjectIdentity = ObjectIdentity
liebertEnvironmentalModuleReg = _LiebertEnvironmentalModuleReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 5)
)
if mibBuilder.loadTexts:
    liebertEnvironmentalModuleReg.setStatus("current")
_LiebertPowerModuleReg_ObjectIdentity = ObjectIdentity
liebertPowerModuleReg = _LiebertPowerModuleReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 6)
)
if mibBuilder.loadTexts:
    liebertPowerModuleReg.setStatus("current")
_LiebertControllerModuleReg_ObjectIdentity = ObjectIdentity
liebertControllerModuleReg = _LiebertControllerModuleReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 7)
)
if mibBuilder.loadTexts:
    liebertControllerModuleReg.setStatus("current")
_LiebertSystemModuleReg_ObjectIdentity = ObjectIdentity
liebertSystemModuleReg = _LiebertSystemModuleReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 8)
)
if mibBuilder.loadTexts:
    liebertSystemModuleReg.setStatus("current")
_LiebertPduModuleReg_ObjectIdentity = ObjectIdentity
liebertPduModuleReg = _LiebertPduModuleReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 9)
)
if mibBuilder.loadTexts:
    liebertPduModuleReg.setStatus("current")
_LiebertFlexibleModuleReg_ObjectIdentity = ObjectIdentity
liebertFlexibleModuleReg = _LiebertFlexibleModuleReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 10)
)
if mibBuilder.loadTexts:
    liebertFlexibleModuleReg.setStatus("current")
_LiebertFlexibleConditionsModuleReg_ObjectIdentity = ObjectIdentity
liebertFlexibleConditionsModuleReg = _LiebertFlexibleConditionsModuleReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 11)
)
if mibBuilder.loadTexts:
    liebertFlexibleConditionsModuleReg.setStatus("current")
_LgpAgent_ObjectIdentity = ObjectIdentity
lgpAgent = _LgpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2)
)
if mibBuilder.loadTexts:
    lgpAgent.setStatus("current")
_LgpAgentIdent_ObjectIdentity = ObjectIdentity
lgpAgentIdent = _LgpAgentIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 1)
)
if mibBuilder.loadTexts:
    lgpAgentIdent.setStatus("current")
_LgpAgentNotifications_ObjectIdentity = ObjectIdentity
lgpAgentNotifications = _LgpAgentNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 3)
)
if mibBuilder.loadTexts:
    lgpAgentNotifications.setStatus("current")
_LgpAgentDevice_ObjectIdentity = ObjectIdentity
lgpAgentDevice = _LgpAgentDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4)
)
if mibBuilder.loadTexts:
    lgpAgentDevice.setStatus("current")
_LgpAgentControl_ObjectIdentity = ObjectIdentity
lgpAgentControl = _LgpAgentControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 5)
)
if mibBuilder.loadTexts:
    lgpAgentControl.setStatus("current")
_LgpFoundation_ObjectIdentity = ObjectIdentity
lgpFoundation = _LgpFoundation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3)
)
if mibBuilder.loadTexts:
    lgpFoundation.setStatus("current")
_LgpConditions_ObjectIdentity = ObjectIdentity
lgpConditions = _LgpConditions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2)
)
if mibBuilder.loadTexts:
    lgpConditions.setStatus("current")
_LgpNotifications_ObjectIdentity = ObjectIdentity
lgpNotifications = _LgpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3)
)
if mibBuilder.loadTexts:
    lgpNotifications.setStatus("current")
_LgpEnvironmental_ObjectIdentity = ObjectIdentity
lgpEnvironmental = _LgpEnvironmental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4)
)
if mibBuilder.loadTexts:
    lgpEnvironmental.setStatus("current")
_LgpPower_ObjectIdentity = ObjectIdentity
lgpPower = _LgpPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5)
)
if mibBuilder.loadTexts:
    lgpPower.setStatus("current")
_LgpController_ObjectIdentity = ObjectIdentity
lgpController = _LgpController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6)
)
if mibBuilder.loadTexts:
    lgpController.setStatus("current")
_LgpSystem_ObjectIdentity = ObjectIdentity
lgpSystem = _LgpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7)
)
if mibBuilder.loadTexts:
    lgpSystem.setStatus("current")
_LgpPdu_ObjectIdentity = ObjectIdentity
lgpPdu = _LgpPdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8)
)
if mibBuilder.loadTexts:
    lgpPdu.setStatus("current")
_LgpFlexible_ObjectIdentity = ObjectIdentity
lgpFlexible = _LgpFlexible_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9)
)
if mibBuilder.loadTexts:
    lgpFlexible.setStatus("current")
_LgpProductSpecific_ObjectIdentity = ObjectIdentity
lgpProductSpecific = _LgpProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4)
)
if mibBuilder.loadTexts:
    lgpProductSpecific.setStatus("current")
_LgpUpsProducts_ObjectIdentity = ObjectIdentity
lgpUpsProducts = _LgpUpsProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2)
)
if mibBuilder.loadTexts:
    lgpUpsProducts.setStatus("current")
_LgpSeries7200_ObjectIdentity = ObjectIdentity
lgpSeries7200 = _LgpSeries7200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 1)
)
if mibBuilder.loadTexts:
    lgpSeries7200.setStatus("current")
_LgpUPStationGXT_ObjectIdentity = ObjectIdentity
lgpUPStationGXT = _LgpUPStationGXT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 2)
)
if mibBuilder.loadTexts:
    lgpUPStationGXT.setStatus("current")
_LgpPowerSureInteractive_ObjectIdentity = ObjectIdentity
lgpPowerSureInteractive = _LgpPowerSureInteractive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 3)
)
if mibBuilder.loadTexts:
    lgpPowerSureInteractive.setStatus("current")
_LgpNfinity_ObjectIdentity = ObjectIdentity
lgpNfinity = _LgpNfinity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 4)
)
if mibBuilder.loadTexts:
    lgpNfinity.setStatus("current")
_LgpNpower_ObjectIdentity = ObjectIdentity
lgpNpower = _LgpNpower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 5)
)
if mibBuilder.loadTexts:
    lgpNpower.setStatus("current")
_LgpGXT2Dual_ObjectIdentity = ObjectIdentity
lgpGXT2Dual = _LgpGXT2Dual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 6)
)
if mibBuilder.loadTexts:
    lgpGXT2Dual.setStatus("current")
_LgpPowerSureInteractive2_ObjectIdentity = ObjectIdentity
lgpPowerSureInteractive2 = _LgpPowerSureInteractive2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 7)
)
if mibBuilder.loadTexts:
    lgpPowerSureInteractive2.setStatus("current")
_LgpNX_ObjectIdentity = ObjectIdentity
lgpNX = _LgpNX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 8)
)
if mibBuilder.loadTexts:
    lgpNX.setStatus("current")
_LgpHiNet_ObjectIdentity = ObjectIdentity
lgpHiNet = _LgpHiNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 9)
)
if mibBuilder.loadTexts:
    lgpHiNet.setStatus("current")
_LgpNXL_ObjectIdentity = ObjectIdentity
lgpNXL = _LgpNXL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 10)
)
if mibBuilder.loadTexts:
    lgpNXL.setStatus("current")
_LgpNXLJD_ObjectIdentity = ObjectIdentity
lgpNXLJD = _LgpNXLJD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 10, 1)
)
if mibBuilder.loadTexts:
    lgpNXLJD.setStatus("current")
_LgpSuper400_ObjectIdentity = ObjectIdentity
lgpSuper400 = _LgpSuper400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 11)
)
if mibBuilder.loadTexts:
    lgpSuper400.setStatus("current")
_LgpSeries600or610_ObjectIdentity = ObjectIdentity
lgpSeries600or610 = _LgpSeries600or610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 12)
)
if mibBuilder.loadTexts:
    lgpSeries600or610.setStatus("current")
_LgpSeries300_ObjectIdentity = ObjectIdentity
lgpSeries300 = _LgpSeries300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 13)
)
if mibBuilder.loadTexts:
    lgpSeries300.setStatus("current")
_LgpSeries610SMS_ObjectIdentity = ObjectIdentity
lgpSeries610SMS = _LgpSeries610SMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 14)
)
if mibBuilder.loadTexts:
    lgpSeries610SMS.setStatus("current")
_LgpSeries610MMU_ObjectIdentity = ObjectIdentity
lgpSeries610MMU = _LgpSeries610MMU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 15)
)
if mibBuilder.loadTexts:
    lgpSeries610MMU.setStatus("current")
_LgpSeries610SCC_ObjectIdentity = ObjectIdentity
lgpSeries610SCC = _LgpSeries610SCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 16)
)
if mibBuilder.loadTexts:
    lgpSeries610SCC.setStatus("current")
_LgpGXT3_ObjectIdentity = ObjectIdentity
lgpGXT3 = _LgpGXT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 17)
)
if mibBuilder.loadTexts:
    lgpGXT3.setStatus("current")
_LgpGXT3Dual_ObjectIdentity = ObjectIdentity
lgpGXT3Dual = _LgpGXT3Dual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 18)
)
if mibBuilder.loadTexts:
    lgpGXT3Dual.setStatus("current")
_LgpNXr_ObjectIdentity = ObjectIdentity
lgpNXr = _LgpNXr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 19)
)
if mibBuilder.loadTexts:
    lgpNXr.setStatus("current")
_LgpITA_ObjectIdentity = ObjectIdentity
lgpITA = _LgpITA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 19, 1)
)
if mibBuilder.loadTexts:
    lgpITA.setStatus("current")
_LgpNXRb_ObjectIdentity = ObjectIdentity
lgpNXRb = _LgpNXRb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 19, 2)
)
if mibBuilder.loadTexts:
    lgpNXRb.setStatus("current")
_LgpNXC_ObjectIdentity = ObjectIdentity
lgpNXC = _LgpNXC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 19, 3)
)
if mibBuilder.loadTexts:
    lgpNXC.setStatus("current")
_LgpNXC30to40k_ObjectIdentity = ObjectIdentity
lgpNXC30to40k = _LgpNXC30to40k_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 19, 4)
)
if mibBuilder.loadTexts:
    lgpNXC30to40k.setStatus("current")
_LgpITA30to40k_ObjectIdentity = ObjectIdentity
lgpITA30to40k = _LgpITA30to40k_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 19, 5)
)
if mibBuilder.loadTexts:
    lgpITA30to40k.setStatus("current")
_LgpAPS_ObjectIdentity = ObjectIdentity
lgpAPS = _LgpAPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 20)
)
if mibBuilder.loadTexts:
    lgpAPS.setStatus("current")
_LgpMUNiMx_ObjectIdentity = ObjectIdentity
lgpMUNiMx = _LgpMUNiMx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 22)
)
if mibBuilder.loadTexts:
    lgpMUNiMx.setStatus("current")
_LgpNX225to600k_ObjectIdentity = ObjectIdentity
lgpNX225to600k = _LgpNX225to600k_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 22, 1)
)
if mibBuilder.loadTexts:
    lgpNX225to600k.setStatus("current")
_LgpGXT4_ObjectIdentity = ObjectIdentity
lgpGXT4 = _LgpGXT4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 23)
)
if mibBuilder.loadTexts:
    lgpGXT4.setStatus("current")
_LgpGXT4Dual_ObjectIdentity = ObjectIdentity
lgpGXT4Dual = _LgpGXT4Dual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 24)
)
if mibBuilder.loadTexts:
    lgpGXT4Dual.setStatus("current")
_LgpEXL_ObjectIdentity = ObjectIdentity
lgpEXL = _LgpEXL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 25)
)
if mibBuilder.loadTexts:
    lgpEXL.setStatus("current")
_LgpEXM_ObjectIdentity = ObjectIdentity
lgpEXM = _LgpEXM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 26)
)
if mibBuilder.loadTexts:
    lgpEXM.setStatus("current")
_LgpEXM208v_ObjectIdentity = ObjectIdentity
lgpEXM208v = _LgpEXM208v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 26, 1)
)
if mibBuilder.loadTexts:
    lgpEXM208v.setStatus("current")
_LgpEXM400v_ObjectIdentity = ObjectIdentity
lgpEXM400v = _LgpEXM400v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 26, 2)
)
if mibBuilder.loadTexts:
    lgpEXM400v.setStatus("current")
_LgpEXM480v_ObjectIdentity = ObjectIdentity
lgpEXM480v = _LgpEXM480v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 26, 3)
)
if mibBuilder.loadTexts:
    lgpEXM480v.setStatus("current")
_LgpEPM_ObjectIdentity = ObjectIdentity
lgpEPM = _LgpEPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 27)
)
if mibBuilder.loadTexts:
    lgpEPM.setStatus("current")
_LgpEPM300k_ObjectIdentity = ObjectIdentity
lgpEPM300k = _LgpEPM300k_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 27, 1)
)
if mibBuilder.loadTexts:
    lgpEPM300k.setStatus("current")
_LgpEPM400k_ObjectIdentity = ObjectIdentity
lgpEPM400k = _LgpEPM400k_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 27, 2)
)
if mibBuilder.loadTexts:
    lgpEPM400k.setStatus("current")
_LgpEPM500k_ObjectIdentity = ObjectIdentity
lgpEPM500k = _LgpEPM500k_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 27, 3)
)
if mibBuilder.loadTexts:
    lgpEPM500k.setStatus("current")
_LgpEPM600k_ObjectIdentity = ObjectIdentity
lgpEPM600k = _LgpEPM600k_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 27, 4)
)
if mibBuilder.loadTexts:
    lgpEPM600k.setStatus("current")
_LgpEPM800k_ObjectIdentity = ObjectIdentity
lgpEPM800k = _LgpEPM800k_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 27, 5)
)
if mibBuilder.loadTexts:
    lgpEPM800k.setStatus("current")
_LgpEXMMSR_ObjectIdentity = ObjectIdentity
lgpEXMMSR = _LgpEXMMSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 29)
)
if mibBuilder.loadTexts:
    lgpEXMMSR.setStatus("current")
_LgpAcProducts_ObjectIdentity = ObjectIdentity
lgpAcProducts = _LgpAcProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3)
)
if mibBuilder.loadTexts:
    lgpAcProducts.setStatus("current")
_LgpAdvancedMicroprocessor_ObjectIdentity = ObjectIdentity
lgpAdvancedMicroprocessor = _LgpAdvancedMicroprocessor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 1)
)
if mibBuilder.loadTexts:
    lgpAdvancedMicroprocessor.setStatus("current")
_LgpStandardMicroprocessor_ObjectIdentity = ObjectIdentity
lgpStandardMicroprocessor = _LgpStandardMicroprocessor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 2)
)
if mibBuilder.loadTexts:
    lgpStandardMicroprocessor.setStatus("current")
_LgpMiniMate2_ObjectIdentity = ObjectIdentity
lgpMiniMate2 = _LgpMiniMate2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 3)
)
if mibBuilder.loadTexts:
    lgpMiniMate2.setStatus("current")
_LgpHimod_ObjectIdentity = ObjectIdentity
lgpHimod = _LgpHimod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 4)
)
if mibBuilder.loadTexts:
    lgpHimod.setStatus("current")
_LgpCEMS100orLECS15_ObjectIdentity = ObjectIdentity
lgpCEMS100orLECS15 = _LgpCEMS100orLECS15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 5)
)
if mibBuilder.loadTexts:
    lgpCEMS100orLECS15.setStatus("current")
_LgpIcom_ObjectIdentity = ObjectIdentity
lgpIcom = _LgpIcom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 6)
)
if mibBuilder.loadTexts:
    lgpIcom.setStatus("current")
_LgpIcomPA_ObjectIdentity = ObjectIdentity
lgpIcomPA = _LgpIcomPA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 7)
)
if mibBuilder.loadTexts:
    lgpIcomPA.setStatus("current")
_LgpIcomPAtypeDS_ObjectIdentity = ObjectIdentity
lgpIcomPAtypeDS = _LgpIcomPAtypeDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 7, 1)
)
if mibBuilder.loadTexts:
    lgpIcomPAtypeDS.setStatus("current")
_LgpIcomPAtypeHPM_ObjectIdentity = ObjectIdentity
lgpIcomPAtypeHPM = _LgpIcomPAtypeHPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 7, 2)
)
if mibBuilder.loadTexts:
    lgpIcomPAtypeHPM.setStatus("current")
_LgpIcomPAtypeChallenger_ObjectIdentity = ObjectIdentity
lgpIcomPAtypeChallenger = _LgpIcomPAtypeChallenger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 7, 3)
)
if mibBuilder.loadTexts:
    lgpIcomPAtypeChallenger.setStatus("current")
_LgpIcomPAtypePeX_ObjectIdentity = ObjectIdentity
lgpIcomPAtypePeX = _LgpIcomPAtypePeX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 7, 4)
)
if mibBuilder.loadTexts:
    lgpIcomPAtypePeX.setStatus("current")
_LgpIcomPAtypeDeluxeSys3_ObjectIdentity = ObjectIdentity
lgpIcomPAtypeDeluxeSys3 = _LgpIcomPAtypeDeluxeSys3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 7, 5)
)
if mibBuilder.loadTexts:
    lgpIcomPAtypeDeluxeSys3.setStatus("current")
_LgpIcomPAtypeDeluxeSystem3_ObjectIdentity = ObjectIdentity
lgpIcomPAtypeDeluxeSystem3 = _LgpIcomPAtypeDeluxeSystem3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 7, 5, 1)
)
if mibBuilder.loadTexts:
    lgpIcomPAtypeDeluxeSystem3.setStatus("current")
_LgpIcomPAtypeCW_ObjectIdentity = ObjectIdentity
lgpIcomPAtypeCW = _LgpIcomPAtypeCW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 7, 5, 2)
)
if mibBuilder.loadTexts:
    lgpIcomPAtypeCW.setStatus("current")
_LgpIcomPAtypeJumboCW_ObjectIdentity = ObjectIdentity
lgpIcomPAtypeJumboCW = _LgpIcomPAtypeJumboCW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 7, 6)
)
if mibBuilder.loadTexts:
    lgpIcomPAtypeJumboCW.setStatus("current")
_LgpIcomPAtypeDSE_ObjectIdentity = ObjectIdentity
lgpIcomPAtypeDSE = _LgpIcomPAtypeDSE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 7, 7)
)
if mibBuilder.loadTexts:
    lgpIcomPAtypeDSE.setStatus("current")
_LgpIcomPAtypePEXS_ObjectIdentity = ObjectIdentity
lgpIcomPAtypePEXS = _LgpIcomPAtypePEXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 7, 8)
)
if mibBuilder.loadTexts:
    lgpIcomPAtypePEXS.setStatus("current")
_LgpIcomPAtypePDXsmall_ObjectIdentity = ObjectIdentity
lgpIcomPAtypePDXsmall = _LgpIcomPAtypePDXsmall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 7, 8, 1)
)
if mibBuilder.loadTexts:
    lgpIcomPAtypePDXsmall.setStatus("current")
_LgpIcomPAtypePCWsmall_ObjectIdentity = ObjectIdentity
lgpIcomPAtypePCWsmall = _LgpIcomPAtypePCWsmall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 7, 8, 2)
)
if mibBuilder.loadTexts:
    lgpIcomPAtypePCWsmall.setStatus("current")
_LgpIcomPAtypePDX_ObjectIdentity = ObjectIdentity
lgpIcomPAtypePDX = _LgpIcomPAtypePDX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 7, 9)
)
if mibBuilder.loadTexts:
    lgpIcomPAtypePDX.setStatus("current")
_LgpIcomPAtypePDXlarge_ObjectIdentity = ObjectIdentity
lgpIcomPAtypePDXlarge = _LgpIcomPAtypePDXlarge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 7, 9, 1)
)
if mibBuilder.loadTexts:
    lgpIcomPAtypePDXlarge.setStatus("current")
_LgpIcomPAtypePCWlarge_ObjectIdentity = ObjectIdentity
lgpIcomPAtypePCWlarge = _LgpIcomPAtypePCWlarge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 7, 9, 2)
)
if mibBuilder.loadTexts:
    lgpIcomPAtypePCWlarge.setStatus("current")
_LgpIcomPAtypeHPS_ObjectIdentity = ObjectIdentity
lgpIcomPAtypeHPS = _LgpIcomPAtypeHPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 7, 10)
)
if mibBuilder.loadTexts:
    lgpIcomPAtypeHPS.setStatus("current")
_LgpIcomXD_ObjectIdentity = ObjectIdentity
lgpIcomXD = _LgpIcomXD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 8)
)
if mibBuilder.loadTexts:
    lgpIcomXD.setStatus("current")
_LgpIcomXDtypeXDF_ObjectIdentity = ObjectIdentity
lgpIcomXDtypeXDF = _LgpIcomXDtypeXDF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 8, 1)
)
if mibBuilder.loadTexts:
    lgpIcomXDtypeXDF.setStatus("current")
_LgpIcomXDtypeXDFN_ObjectIdentity = ObjectIdentity
lgpIcomXDtypeXDFN = _LgpIcomXDtypeXDFN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 8, 2)
)
if mibBuilder.loadTexts:
    lgpIcomXDtypeXDFN.setStatus("current")
_LgpIcomXP_ObjectIdentity = ObjectIdentity
lgpIcomXP = _LgpIcomXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 9)
)
if mibBuilder.loadTexts:
    lgpIcomXP.setStatus("current")
_LgpIcomXPtypeXDP_ObjectIdentity = ObjectIdentity
lgpIcomXPtypeXDP = _LgpIcomXPtypeXDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 9, 1)
)
if mibBuilder.loadTexts:
    lgpIcomXPtypeXDP.setStatus("current")
_LgpIcomXPtypeXDPCray_ObjectIdentity = ObjectIdentity
lgpIcomXPtypeXDPCray = _LgpIcomXPtypeXDPCray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 9, 1, 1)
)
if mibBuilder.loadTexts:
    lgpIcomXPtypeXDPCray.setStatus("current")
_LgpIcomXPtypeXDC_ObjectIdentity = ObjectIdentity
lgpIcomXPtypeXDC = _LgpIcomXPtypeXDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 9, 2)
)
if mibBuilder.loadTexts:
    lgpIcomXPtypeXDC.setStatus("current")
_LgpIcomXPtypeXDPW_ObjectIdentity = ObjectIdentity
lgpIcomXPtypeXDPW = _LgpIcomXPtypeXDPW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 9, 3)
)
if mibBuilder.loadTexts:
    lgpIcomXPtypeXDPW.setStatus("current")
_LgpIcomSC_ObjectIdentity = ObjectIdentity
lgpIcomSC = _LgpIcomSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 10)
)
if mibBuilder.loadTexts:
    lgpIcomSC.setStatus("current")
_LgpIcomSCtypeHPC_ObjectIdentity = ObjectIdentity
lgpIcomSCtypeHPC = _LgpIcomSCtypeHPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 10, 1)
)
if mibBuilder.loadTexts:
    lgpIcomSCtypeHPC.setStatus("current")
_LgpIcomSCtypeHPCSSmall_ObjectIdentity = ObjectIdentity
lgpIcomSCtypeHPCSSmall = _LgpIcomSCtypeHPCSSmall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 10, 1, 1)
)
if mibBuilder.loadTexts:
    lgpIcomSCtypeHPCSSmall.setStatus("current")
_LgpIcomSCtypeHPCSLarge_ObjectIdentity = ObjectIdentity
lgpIcomSCtypeHPCSLarge = _LgpIcomSCtypeHPCSLarge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 10, 1, 2)
)
if mibBuilder.loadTexts:
    lgpIcomSCtypeHPCSLarge.setStatus("current")
_LgpIcomSCtypeHPCR_ObjectIdentity = ObjectIdentity
lgpIcomSCtypeHPCR = _LgpIcomSCtypeHPCR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 10, 1, 3)
)
if mibBuilder.loadTexts:
    lgpIcomSCtypeHPCR.setStatus("current")
_LgpIcomSCtypeHPCM_ObjectIdentity = ObjectIdentity
lgpIcomSCtypeHPCM = _LgpIcomSCtypeHPCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 10, 1, 4)
)
if mibBuilder.loadTexts:
    lgpIcomSCtypeHPCM.setStatus("current")
_LgpIcomSCtypeHPCL_ObjectIdentity = ObjectIdentity
lgpIcomSCtypeHPCL = _LgpIcomSCtypeHPCL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 10, 1, 5)
)
if mibBuilder.loadTexts:
    lgpIcomSCtypeHPCL.setStatus("current")
_LgpIcomSCtypeHPCW_ObjectIdentity = ObjectIdentity
lgpIcomSCtypeHPCW = _LgpIcomSCtypeHPCW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 10, 1, 6)
)
if mibBuilder.loadTexts:
    lgpIcomSCtypeHPCW.setStatus("current")
_LgpIcomCR_ObjectIdentity = ObjectIdentity
lgpIcomCR = _LgpIcomCR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 11)
)
if mibBuilder.loadTexts:
    lgpIcomCR.setStatus("current")
_LgpIcomCRtypeCRV_ObjectIdentity = ObjectIdentity
lgpIcomCRtypeCRV = _LgpIcomCRtypeCRV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 11, 1)
)
if mibBuilder.loadTexts:
    lgpIcomCRtypeCRV.setStatus("current")
_LgpIcomAH_ObjectIdentity = ObjectIdentity
lgpIcomAH = _LgpIcomAH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 12)
)
if mibBuilder.loadTexts:
    lgpIcomAH.setStatus("current")
_LgpIcomAHStandard_ObjectIdentity = ObjectIdentity
lgpIcomAHStandard = _LgpIcomAHStandard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 12, 1)
)
if mibBuilder.loadTexts:
    lgpIcomAHStandard.setStatus("current")
_LgpIcomDCL_ObjectIdentity = ObjectIdentity
lgpIcomDCL = _LgpIcomDCL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 13)
)
if mibBuilder.loadTexts:
    lgpIcomDCL.setStatus("current")
_LgpIcomEEV_ObjectIdentity = ObjectIdentity
lgpIcomEEV = _LgpIcomEEV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 14)
)
if mibBuilder.loadTexts:
    lgpIcomEEV.setStatus("current")
_LgpPowerConditioningProducts_ObjectIdentity = ObjectIdentity
lgpPowerConditioningProducts = _LgpPowerConditioningProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 4)
)
if mibBuilder.loadTexts:
    lgpPowerConditioningProducts.setStatus("current")
_LgpPMP_ObjectIdentity = ObjectIdentity
lgpPMP = _LgpPMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 4, 1)
)
if mibBuilder.loadTexts:
    lgpPMP.setStatus("current")
_LgpEPMP_ObjectIdentity = ObjectIdentity
lgpEPMP = _LgpEPMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 4, 2)
)
if mibBuilder.loadTexts:
    lgpEPMP.setStatus("current")
_LgpTransferSwitchProducts_ObjectIdentity = ObjectIdentity
lgpTransferSwitchProducts = _LgpTransferSwitchProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 5)
)
if mibBuilder.loadTexts:
    lgpTransferSwitchProducts.setStatus("current")
_LgpStaticTransferSwitchEDS_ObjectIdentity = ObjectIdentity
lgpStaticTransferSwitchEDS = _LgpStaticTransferSwitchEDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 5, 1)
)
if mibBuilder.loadTexts:
    lgpStaticTransferSwitchEDS.setStatus("current")
_LgpStaticTransferSwitch1_ObjectIdentity = ObjectIdentity
lgpStaticTransferSwitch1 = _LgpStaticTransferSwitch1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 5, 2)
)
if mibBuilder.loadTexts:
    lgpStaticTransferSwitch1.setStatus("current")
_LgpStaticTransferSwitch2_ObjectIdentity = ObjectIdentity
lgpStaticTransferSwitch2 = _LgpStaticTransferSwitch2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 5, 3)
)
if mibBuilder.loadTexts:
    lgpStaticTransferSwitch2.setStatus("current")
_LgpStaticTransferSwitch2FourPole_ObjectIdentity = ObjectIdentity
lgpStaticTransferSwitch2FourPole = _LgpStaticTransferSwitch2FourPole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 5, 4)
)
if mibBuilder.loadTexts:
    lgpStaticTransferSwitch2FourPole.setStatus("current")
_LgpMultiLinkProducts_ObjectIdentity = ObjectIdentity
lgpMultiLinkProducts = _LgpMultiLinkProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 7)
)
if mibBuilder.loadTexts:
    lgpMultiLinkProducts.setStatus("current")
_LgpMultiLinkBasicNotification_ObjectIdentity = ObjectIdentity
lgpMultiLinkBasicNotification = _LgpMultiLinkBasicNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 7, 1)
)
if mibBuilder.loadTexts:
    lgpMultiLinkBasicNotification.setStatus("current")
_LgpPowerDistributionProducts_ObjectIdentity = ObjectIdentity
lgpPowerDistributionProducts = _LgpPowerDistributionProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 8)
)
if mibBuilder.loadTexts:
    lgpPowerDistributionProducts.setStatus("current")
_LgpRackPDU_ObjectIdentity = ObjectIdentity
lgpRackPDU = _LgpRackPDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 8, 2)
)
if mibBuilder.loadTexts:
    lgpRackPDU.setStatus("current")
_LgpMPX_ObjectIdentity = ObjectIdentity
lgpMPX = _LgpMPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 8, 2, 1)
)
if mibBuilder.loadTexts:
    lgpMPX.setStatus("current")
_LgpMPH_ObjectIdentity = ObjectIdentity
lgpMPH = _LgpMPH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 8, 2, 2)
)
if mibBuilder.loadTexts:
    lgpMPH.setStatus("current")
_LgpRackPDU2_ObjectIdentity = ObjectIdentity
lgpRackPDU2 = _LgpRackPDU2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 8, 4)
)
if mibBuilder.loadTexts:
    lgpRackPDU2.setStatus("current")
_LgpRPC2kMPX_ObjectIdentity = ObjectIdentity
lgpRPC2kMPX = _LgpRPC2kMPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 8, 4, 1)
)
if mibBuilder.loadTexts:
    lgpRPC2kMPX.setStatus("current")
_LgpRPC2kMPH_ObjectIdentity = ObjectIdentity
lgpRPC2kMPH = _LgpRPC2kMPH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 8, 4, 2)
)
if mibBuilder.loadTexts:
    lgpRPC2kMPH.setStatus("current")
_LgpCombinedSystemProducts_ObjectIdentity = ObjectIdentity
lgpCombinedSystemProducts = _LgpCombinedSystemProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 10)
)
if mibBuilder.loadTexts:
    lgpCombinedSystemProducts.setStatus("current")
_LgpPMPandLDMF_ObjectIdentity = ObjectIdentity
lgpPMPandLDMF = _LgpPMPandLDMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 10, 1)
)
if mibBuilder.loadTexts:
    lgpPMPandLDMF.setStatus("current")
_LgpPMPgeneric_ObjectIdentity = ObjectIdentity
lgpPMPgeneric = _LgpPMPgeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 10, 1, 1)
)
if mibBuilder.loadTexts:
    lgpPMPgeneric.setStatus("current")
_LgpPMPonFPC_ObjectIdentity = ObjectIdentity
lgpPMPonFPC = _LgpPMPonFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 10, 1, 2)
)
if mibBuilder.loadTexts:
    lgpPMPonFPC.setStatus("current")
_LgpPMPonPPC_ObjectIdentity = ObjectIdentity
lgpPMPonPPC = _LgpPMPonPPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 10, 1, 3)
)
if mibBuilder.loadTexts:
    lgpPMPonPPC.setStatus("current")
_LgpPMPonFDC_ObjectIdentity = ObjectIdentity
lgpPMPonFDC = _LgpPMPonFDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 10, 1, 4)
)
if mibBuilder.loadTexts:
    lgpPMPonFDC.setStatus("current")
_LgpPMPonRDC_ObjectIdentity = ObjectIdentity
lgpPMPonRDC = _LgpPMPonRDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 10, 1, 5)
)
if mibBuilder.loadTexts:
    lgpPMPonRDC.setStatus("current")
_LgpPMPonEXC_ObjectIdentity = ObjectIdentity
lgpPMPonEXC = _LgpPMPonEXC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 10, 1, 6)
)
if mibBuilder.loadTexts:
    lgpPMPonEXC.setStatus("current")
_LgpPMPonSTS2_ObjectIdentity = ObjectIdentity
lgpPMPonSTS2 = _LgpPMPonSTS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 10, 1, 7)
)
if mibBuilder.loadTexts:
    lgpPMPonSTS2.setStatus("current")
_LgpPMPonSTS2PDU_ObjectIdentity = ObjectIdentity
lgpPMPonSTS2PDU = _LgpPMPonSTS2PDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 10, 1, 8)
)
if mibBuilder.loadTexts:
    lgpPMPonSTS2PDU.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIEBERT-GP-REGISTRATION-MIB",
    **{"emerson": emerson,
       "liebertCorp": liebertCorp,
       "liebertGlobalProducts": liebertGlobalProducts,
       "lgpModuleReg": lgpModuleReg,
       "liebertModuleReg": liebertModuleReg,
       "liebertGlobalProductsRegistrationModule": liebertGlobalProductsRegistrationModule,
       "liebertAgentModuleReg": liebertAgentModuleReg,
       "liebertConditionsModuleReg": liebertConditionsModuleReg,
       "liebertNotificationsModuleReg": liebertNotificationsModuleReg,
       "liebertEnvironmentalModuleReg": liebertEnvironmentalModuleReg,
       "liebertPowerModuleReg": liebertPowerModuleReg,
       "liebertControllerModuleReg": liebertControllerModuleReg,
       "liebertSystemModuleReg": liebertSystemModuleReg,
       "liebertPduModuleReg": liebertPduModuleReg,
       "liebertFlexibleModuleReg": liebertFlexibleModuleReg,
       "liebertFlexibleConditionsModuleReg": liebertFlexibleConditionsModuleReg,
       "lgpAgent": lgpAgent,
       "lgpAgentIdent": lgpAgentIdent,
       "lgpAgentNotifications": lgpAgentNotifications,
       "lgpAgentDevice": lgpAgentDevice,
       "lgpAgentControl": lgpAgentControl,
       "lgpFoundation": lgpFoundation,
       "lgpConditions": lgpConditions,
       "lgpNotifications": lgpNotifications,
       "lgpEnvironmental": lgpEnvironmental,
       "lgpPower": lgpPower,
       "lgpController": lgpController,
       "lgpSystem": lgpSystem,
       "lgpPdu": lgpPdu,
       "lgpFlexible": lgpFlexible,
       "lgpProductSpecific": lgpProductSpecific,
       "lgpUpsProducts": lgpUpsProducts,
       "lgpSeries7200": lgpSeries7200,
       "lgpUPStationGXT": lgpUPStationGXT,
       "lgpPowerSureInteractive": lgpPowerSureInteractive,
       "lgpNfinity": lgpNfinity,
       "lgpNpower": lgpNpower,
       "lgpGXT2Dual": lgpGXT2Dual,
       "lgpPowerSureInteractive2": lgpPowerSureInteractive2,
       "lgpNX": lgpNX,
       "lgpHiNet": lgpHiNet,
       "lgpNXL": lgpNXL,
       "lgpNXLJD": lgpNXLJD,
       "lgpSuper400": lgpSuper400,
       "lgpSeries600or610": lgpSeries600or610,
       "lgpSeries300": lgpSeries300,
       "lgpSeries610SMS": lgpSeries610SMS,
       "lgpSeries610MMU": lgpSeries610MMU,
       "lgpSeries610SCC": lgpSeries610SCC,
       "lgpGXT3": lgpGXT3,
       "lgpGXT3Dual": lgpGXT3Dual,
       "lgpNXr": lgpNXr,
       "lgpITA": lgpITA,
       "lgpNXRb": lgpNXRb,
       "lgpNXC": lgpNXC,
       "lgpNXC30to40k": lgpNXC30to40k,
       "lgpITA30to40k": lgpITA30to40k,
       "lgpAPS": lgpAPS,
       "lgpMUNiMx": lgpMUNiMx,
       "lgpNX225to600k": lgpNX225to600k,
       "lgpGXT4": lgpGXT4,
       "lgpGXT4Dual": lgpGXT4Dual,
       "lgpEXL": lgpEXL,
       "lgpEXM": lgpEXM,
       "lgpEXM208v": lgpEXM208v,
       "lgpEXM400v": lgpEXM400v,
       "lgpEXM480v": lgpEXM480v,
       "lgpEPM": lgpEPM,
       "lgpEPM300k": lgpEPM300k,
       "lgpEPM400k": lgpEPM400k,
       "lgpEPM500k": lgpEPM500k,
       "lgpEPM600k": lgpEPM600k,
       "lgpEPM800k": lgpEPM800k,
       "lgpEXMMSR": lgpEXMMSR,
       "lgpAcProducts": lgpAcProducts,
       "lgpAdvancedMicroprocessor": lgpAdvancedMicroprocessor,
       "lgpStandardMicroprocessor": lgpStandardMicroprocessor,
       "lgpMiniMate2": lgpMiniMate2,
       "lgpHimod": lgpHimod,
       "lgpCEMS100orLECS15": lgpCEMS100orLECS15,
       "lgpIcom": lgpIcom,
       "lgpIcomPA": lgpIcomPA,
       "lgpIcomPAtypeDS": lgpIcomPAtypeDS,
       "lgpIcomPAtypeHPM": lgpIcomPAtypeHPM,
       "lgpIcomPAtypeChallenger": lgpIcomPAtypeChallenger,
       "lgpIcomPAtypePeX": lgpIcomPAtypePeX,
       "lgpIcomPAtypeDeluxeSys3": lgpIcomPAtypeDeluxeSys3,
       "lgpIcomPAtypeDeluxeSystem3": lgpIcomPAtypeDeluxeSystem3,
       "lgpIcomPAtypeCW": lgpIcomPAtypeCW,
       "lgpIcomPAtypeJumboCW": lgpIcomPAtypeJumboCW,
       "lgpIcomPAtypeDSE": lgpIcomPAtypeDSE,
       "lgpIcomPAtypePEXS": lgpIcomPAtypePEXS,
       "lgpIcomPAtypePDXsmall": lgpIcomPAtypePDXsmall,
       "lgpIcomPAtypePCWsmall": lgpIcomPAtypePCWsmall,
       "lgpIcomPAtypePDX": lgpIcomPAtypePDX,
       "lgpIcomPAtypePDXlarge": lgpIcomPAtypePDXlarge,
       "lgpIcomPAtypePCWlarge": lgpIcomPAtypePCWlarge,
       "lgpIcomPAtypeHPS": lgpIcomPAtypeHPS,
       "lgpIcomXD": lgpIcomXD,
       "lgpIcomXDtypeXDF": lgpIcomXDtypeXDF,
       "lgpIcomXDtypeXDFN": lgpIcomXDtypeXDFN,
       "lgpIcomXP": lgpIcomXP,
       "lgpIcomXPtypeXDP": lgpIcomXPtypeXDP,
       "lgpIcomXPtypeXDPCray": lgpIcomXPtypeXDPCray,
       "lgpIcomXPtypeXDC": lgpIcomXPtypeXDC,
       "lgpIcomXPtypeXDPW": lgpIcomXPtypeXDPW,
       "lgpIcomSC": lgpIcomSC,
       "lgpIcomSCtypeHPC": lgpIcomSCtypeHPC,
       "lgpIcomSCtypeHPCSSmall": lgpIcomSCtypeHPCSSmall,
       "lgpIcomSCtypeHPCSLarge": lgpIcomSCtypeHPCSLarge,
       "lgpIcomSCtypeHPCR": lgpIcomSCtypeHPCR,
       "lgpIcomSCtypeHPCM": lgpIcomSCtypeHPCM,
       "lgpIcomSCtypeHPCL": lgpIcomSCtypeHPCL,
       "lgpIcomSCtypeHPCW": lgpIcomSCtypeHPCW,
       "lgpIcomCR": lgpIcomCR,
       "lgpIcomCRtypeCRV": lgpIcomCRtypeCRV,
       "lgpIcomAH": lgpIcomAH,
       "lgpIcomAHStandard": lgpIcomAHStandard,
       "lgpIcomDCL": lgpIcomDCL,
       "lgpIcomEEV": lgpIcomEEV,
       "lgpPowerConditioningProducts": lgpPowerConditioningProducts,
       "lgpPMP": lgpPMP,
       "lgpEPMP": lgpEPMP,
       "lgpTransferSwitchProducts": lgpTransferSwitchProducts,
       "lgpStaticTransferSwitchEDS": lgpStaticTransferSwitchEDS,
       "lgpStaticTransferSwitch1": lgpStaticTransferSwitch1,
       "lgpStaticTransferSwitch2": lgpStaticTransferSwitch2,
       "lgpStaticTransferSwitch2FourPole": lgpStaticTransferSwitch2FourPole,
       "lgpMultiLinkProducts": lgpMultiLinkProducts,
       "lgpMultiLinkBasicNotification": lgpMultiLinkBasicNotification,
       "lgpPowerDistributionProducts": lgpPowerDistributionProducts,
       "lgpRackPDU": lgpRackPDU,
       "lgpMPX": lgpMPX,
       "lgpMPH": lgpMPH,
       "lgpRackPDU2": lgpRackPDU2,
       "lgpRPC2kMPX": lgpRPC2kMPX,
       "lgpRPC2kMPH": lgpRPC2kMPH,
       "lgpCombinedSystemProducts": lgpCombinedSystemProducts,
       "lgpPMPandLDMF": lgpPMPandLDMF,
       "lgpPMPgeneric": lgpPMPgeneric,
       "lgpPMPonFPC": lgpPMPonFPC,
       "lgpPMPonPPC": lgpPMPonPPC,
       "lgpPMPonFDC": lgpPMPonFDC,
       "lgpPMPonRDC": lgpPMPonRDC,
       "lgpPMPonEXC": lgpPMPonEXC,
       "lgpPMPonSTS2": lgpPMPonSTS2,
       "lgpPMPonSTS2PDU": lgpPMPonSTS2PDU}
)
