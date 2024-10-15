# SNMP MIB module (Unisphere-Data-ERX-Registry) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-ERX-Registry
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:37 2024
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

(usDataAdmin,) = mibBuilder.importSymbols(
    "Unisphere-Data-Registry",
    "usDataAdmin")


# MODULE-IDENTITY

usdErxRegistry = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2)
)
usdErxRegistry.setRevisions(
        ("2002-10-10 18:51",
         "2002-05-08 12:34",
         "2002-05-07 14:05",
         "2001-08-20 16:08",
         "2001-06-12 18:27",
         "2001-06-04 20:11")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdErxEntPhysicalType_ObjectIdentity = ObjectIdentity
usdErxEntPhysicalType = _UsdErxEntPhysicalType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1)
)
_ErxChassis_ObjectIdentity = ObjectIdentity
erxChassis = _ErxChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    erxChassis.setStatus("current")
_Erx700Chassis_ObjectIdentity = ObjectIdentity
erx700Chassis = _Erx700Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    erx700Chassis.setStatus("current")
_Erx1400Chassis_ObjectIdentity = ObjectIdentity
erx1400Chassis = _Erx1400Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    erx1400Chassis.setStatus("current")
_ErxFanAssembly_ObjectIdentity = ObjectIdentity
erxFanAssembly = _ErxFanAssembly_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    erxFanAssembly.setStatus("current")
_Erx700FanAssembly_ObjectIdentity = ObjectIdentity
erx700FanAssembly = _Erx700FanAssembly_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    erx700FanAssembly.setStatus("current")
_Erx1400FanAssembly_ObjectIdentity = ObjectIdentity
erx1400FanAssembly = _Erx1400FanAssembly_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    erx1400FanAssembly.setStatus("current")
_ErxPowerInput_ObjectIdentity = ObjectIdentity
erxPowerInput = _ErxPowerInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    erxPowerInput.setStatus("current")
_ErxMidplane_ObjectIdentity = ObjectIdentity
erxMidplane = _ErxMidplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    erxMidplane.setStatus("current")
_Erx700Midplane_ObjectIdentity = ObjectIdentity
erx700Midplane = _Erx700Midplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    erx700Midplane.setStatus("current")
_Erx1400Midplane_ObjectIdentity = ObjectIdentity
erx1400Midplane = _Erx1400Midplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    erx1400Midplane.setStatus("current")
_Erx1Plus1RedundantT1E1Midplane_ObjectIdentity = ObjectIdentity
erx1Plus1RedundantT1E1Midplane = _Erx1Plus1RedundantT1E1Midplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    erx1Plus1RedundantT1E1Midplane.setStatus("current")
_Erx2Plus1RedundantT1E1Midplane_ObjectIdentity = ObjectIdentity
erx2Plus1RedundantT1E1Midplane = _Erx2Plus1RedundantT1E1Midplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 4)
)
if mibBuilder.loadTexts:
    erx2Plus1RedundantT1E1Midplane.setStatus("current")
_Erx3Plus1RedundantT1E1Midplane_ObjectIdentity = ObjectIdentity
erx3Plus1RedundantT1E1Midplane = _Erx3Plus1RedundantT1E1Midplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 5)
)
if mibBuilder.loadTexts:
    erx3Plus1RedundantT1E1Midplane.setStatus("current")
_Erx4Plus1RedundantT1E1Midplane_ObjectIdentity = ObjectIdentity
erx4Plus1RedundantT1E1Midplane = _Erx4Plus1RedundantT1E1Midplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 6)
)
if mibBuilder.loadTexts:
    erx4Plus1RedundantT1E1Midplane.setStatus("current")
_Erx5Plus1RedundantT1E1Midplane_ObjectIdentity = ObjectIdentity
erx5Plus1RedundantT1E1Midplane = _Erx5Plus1RedundantT1E1Midplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 7)
)
if mibBuilder.loadTexts:
    erx5Plus1RedundantT1E1Midplane.setStatus("current")
_Erx1Plus1RedundantT3E3Midplane_ObjectIdentity = ObjectIdentity
erx1Plus1RedundantT3E3Midplane = _Erx1Plus1RedundantT3E3Midplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 8)
)
if mibBuilder.loadTexts:
    erx1Plus1RedundantT3E3Midplane.setStatus("current")
_Erx2Plus1RedundantT3E3Midplane_ObjectIdentity = ObjectIdentity
erx2Plus1RedundantT3E3Midplane = _Erx2Plus1RedundantT3E3Midplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 9)
)
if mibBuilder.loadTexts:
    erx2Plus1RedundantT3E3Midplane.setStatus("current")
_Erx3Plus1RedundantT3E3Midplane_ObjectIdentity = ObjectIdentity
erx3Plus1RedundantT3E3Midplane = _Erx3Plus1RedundantT3E3Midplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 10)
)
if mibBuilder.loadTexts:
    erx3Plus1RedundantT3E3Midplane.setStatus("current")
_Erx4Plus1RedundantT3E3Midplane_ObjectIdentity = ObjectIdentity
erx4Plus1RedundantT3E3Midplane = _Erx4Plus1RedundantT3E3Midplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 11)
)
if mibBuilder.loadTexts:
    erx4Plus1RedundantT3E3Midplane.setStatus("current")
_Erx5Plus1RedundantT3E3Midplane_ObjectIdentity = ObjectIdentity
erx5Plus1RedundantT3E3Midplane = _Erx5Plus1RedundantT3E3Midplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 12)
)
if mibBuilder.loadTexts:
    erx5Plus1RedundantT3E3Midplane.setStatus("current")
_Erx1Plus1RedundantOcMidplane_ObjectIdentity = ObjectIdentity
erx1Plus1RedundantOcMidplane = _Erx1Plus1RedundantOcMidplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 13)
)
if mibBuilder.loadTexts:
    erx1Plus1RedundantOcMidplane.setStatus("current")
_Erx2Plus1RedundantOcMidplane_ObjectIdentity = ObjectIdentity
erx2Plus1RedundantOcMidplane = _Erx2Plus1RedundantOcMidplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 14)
)
if mibBuilder.loadTexts:
    erx2Plus1RedundantOcMidplane.setStatus("current")
_Erx3Plus1RedundantOcMidplane_ObjectIdentity = ObjectIdentity
erx3Plus1RedundantOcMidplane = _Erx3Plus1RedundantOcMidplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 15)
)
if mibBuilder.loadTexts:
    erx3Plus1RedundantOcMidplane.setStatus("current")
_Erx4Plus1RedundantOcMidplane_ObjectIdentity = ObjectIdentity
erx4Plus1RedundantOcMidplane = _Erx4Plus1RedundantOcMidplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 16)
)
if mibBuilder.loadTexts:
    erx4Plus1RedundantOcMidplane.setStatus("current")
_Erx5Plus1RedundantOcMidplane_ObjectIdentity = ObjectIdentity
erx5Plus1RedundantOcMidplane = _Erx5Plus1RedundantOcMidplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 17)
)
if mibBuilder.loadTexts:
    erx5Plus1RedundantOcMidplane.setStatus("current")
_ErxSrpModule_ObjectIdentity = ObjectIdentity
erxSrpModule = _ErxSrpModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    erxSrpModule.setStatus("current")
_ErxSrp5_ObjectIdentity = ObjectIdentity
erxSrp5 = _ErxSrp5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    erxSrp5.setStatus("current")
_ErxSrp10_ObjectIdentity = ObjectIdentity
erxSrp10 = _ErxSrp10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    erxSrp10.setStatus("current")
_ErxSrp10Ecc_ObjectIdentity = ObjectIdentity
erxSrp10Ecc = _ErxSrp10Ecc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5, 3)
)
if mibBuilder.loadTexts:
    erxSrp10Ecc.setStatus("current")
_ErxSrp40_ObjectIdentity = ObjectIdentity
erxSrp40 = _ErxSrp40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5, 4)
)
if mibBuilder.loadTexts:
    erxSrp40.setStatus("current")
_ErxSrp5Plus_ObjectIdentity = ObjectIdentity
erxSrp5Plus = _ErxSrp5Plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5, 5)
)
if mibBuilder.loadTexts:
    erxSrp5Plus.setStatus("current")
_ErxSrp40Plus_ObjectIdentity = ObjectIdentity
erxSrp40Plus = _ErxSrp40Plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5, 6)
)
if mibBuilder.loadTexts:
    erxSrp40Plus.setStatus("current")
_ErxSrpIoAdapter_ObjectIdentity = ObjectIdentity
erxSrpIoAdapter = _ErxSrpIoAdapter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 6)
)
if mibBuilder.loadTexts:
    erxSrpIoAdapter.setStatus("current")
_ErxLineModule_ObjectIdentity = ObjectIdentity
erxLineModule = _ErxLineModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7)
)
if mibBuilder.loadTexts:
    erxLineModule.setStatus("current")
_ErxCt1_ObjectIdentity = ObjectIdentity
erxCt1 = _ErxCt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    erxCt1.setStatus("current")
_ErxCe1_ObjectIdentity = ObjectIdentity
erxCe1 = _ErxCe1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    erxCe1.setStatus("current")
_ErxCt3_ObjectIdentity = ObjectIdentity
erxCt3 = _ErxCt3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 4)
)
if mibBuilder.loadTexts:
    erxCt3.setStatus("current")
_ErxT3Atm_ObjectIdentity = ObjectIdentity
erxT3Atm = _ErxT3Atm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 5)
)
if mibBuilder.loadTexts:
    erxT3Atm.setStatus("current")
_ErxT3Frame_ObjectIdentity = ObjectIdentity
erxT3Frame = _ErxT3Frame_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 6)
)
if mibBuilder.loadTexts:
    erxT3Frame.setStatus("current")
_ErxE3Atm_ObjectIdentity = ObjectIdentity
erxE3Atm = _ErxE3Atm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 7)
)
if mibBuilder.loadTexts:
    erxE3Atm.setStatus("current")
_ErxE3Frame_ObjectIdentity = ObjectIdentity
erxE3Frame = _ErxE3Frame_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 8)
)
if mibBuilder.loadTexts:
    erxE3Frame.setStatus("current")
_ErxOc3_ObjectIdentity = ObjectIdentity
erxOc3 = _ErxOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 9)
)
if mibBuilder.loadTexts:
    erxOc3.setStatus("current")
_ErxOc3Oc12Atm_ObjectIdentity = ObjectIdentity
erxOc3Oc12Atm = _ErxOc3Oc12Atm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 10)
)
if mibBuilder.loadTexts:
    erxOc3Oc12Atm.setStatus("current")
_ErxOc3Oc12Pos_ObjectIdentity = ObjectIdentity
erxOc3Oc12Pos = _ErxOc3Oc12Pos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 11)
)
if mibBuilder.loadTexts:
    erxOc3Oc12Pos.setStatus("current")
_ErxCOcx_ObjectIdentity = ObjectIdentity
erxCOcx = _ErxCOcx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 12)
)
if mibBuilder.loadTexts:
    erxCOcx.setStatus("current")
_ErxFe2_ObjectIdentity = ObjectIdentity
erxFe2 = _ErxFe2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 13)
)
if mibBuilder.loadTexts:
    erxFe2.setStatus("current")
_ErxGeFe_ObjectIdentity = ObjectIdentity
erxGeFe = _ErxGeFe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 14)
)
if mibBuilder.loadTexts:
    erxGeFe.setStatus("current")
_ErxTunnelService_ObjectIdentity = ObjectIdentity
erxTunnelService = _ErxTunnelService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 15)
)
if mibBuilder.loadTexts:
    erxTunnelService.setStatus("current")
_ErxHssi_ObjectIdentity = ObjectIdentity
erxHssi = _ErxHssi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 16)
)
if mibBuilder.loadTexts:
    erxHssi.setStatus("current")
_ErxVts_ObjectIdentity = ObjectIdentity
erxVts = _ErxVts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 17)
)
if mibBuilder.loadTexts:
    erxVts.setStatus("current")
_ErxCt3P12_ObjectIdentity = ObjectIdentity
erxCt3P12 = _ErxCt3P12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 18)
)
if mibBuilder.loadTexts:
    erxCt3P12.setStatus("current")
_ErxV35_ObjectIdentity = ObjectIdentity
erxV35 = _ErxV35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 19)
)
if mibBuilder.loadTexts:
    erxV35.setStatus("current")
_ErxUt3E3Ocx_ObjectIdentity = ObjectIdentity
erxUt3E3Ocx = _ErxUt3E3Ocx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 20)
)
if mibBuilder.loadTexts:
    erxUt3E3Ocx.setStatus("current")
_ErxLineIoAdapter_ObjectIdentity = ObjectIdentity
erxLineIoAdapter = _ErxLineIoAdapter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8)
)
if mibBuilder.loadTexts:
    erxLineIoAdapter.setStatus("current")
_ErxCt1Ioa_ObjectIdentity = ObjectIdentity
erxCt1Ioa = _ErxCt1Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    erxCt1Ioa.setStatus("current")
_ErxCe1Ioa_ObjectIdentity = ObjectIdentity
erxCe1Ioa = _ErxCe1Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 2)
)
if mibBuilder.loadTexts:
    erxCe1Ioa.setStatus("current")
_ErxCe1TIoa_ObjectIdentity = ObjectIdentity
erxCe1TIoa = _ErxCe1TIoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 3)
)
if mibBuilder.loadTexts:
    erxCe1TIoa.setStatus("current")
_ErxCt3Ioa_ObjectIdentity = ObjectIdentity
erxCt3Ioa = _ErxCt3Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 4)
)
if mibBuilder.loadTexts:
    erxCt3Ioa.setStatus("current")
_ErxE3Ioa_ObjectIdentity = ObjectIdentity
erxE3Ioa = _ErxE3Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 5)
)
if mibBuilder.loadTexts:
    erxE3Ioa.setStatus("current")
_ErxOc3Mm2Ioa_ObjectIdentity = ObjectIdentity
erxOc3Mm2Ioa = _ErxOc3Mm2Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 6)
)
if mibBuilder.loadTexts:
    erxOc3Mm2Ioa.setStatus("current")
_ErxOc3Sm2Ioa_ObjectIdentity = ObjectIdentity
erxOc3Sm2Ioa = _ErxOc3Sm2Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 7)
)
if mibBuilder.loadTexts:
    erxOc3Sm2Ioa.setStatus("current")
_ErxOc3Mm4Ioa_ObjectIdentity = ObjectIdentity
erxOc3Mm4Ioa = _ErxOc3Mm4Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 8)
)
if mibBuilder.loadTexts:
    erxOc3Mm4Ioa.setStatus("current")
_ErxOc3SmIr4Ioa_ObjectIdentity = ObjectIdentity
erxOc3SmIr4Ioa = _ErxOc3SmIr4Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 9)
)
if mibBuilder.loadTexts:
    erxOc3SmIr4Ioa.setStatus("current")
_ErxOc3SmLr4Ioa_ObjectIdentity = ObjectIdentity
erxOc3SmLr4Ioa = _ErxOc3SmLr4Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 10)
)
if mibBuilder.loadTexts:
    erxOc3SmLr4Ioa.setStatus("current")
_ErxCOc3Mm4Ioa_ObjectIdentity = ObjectIdentity
erxCOc3Mm4Ioa = _ErxCOc3Mm4Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 11)
)
if mibBuilder.loadTexts:
    erxCOc3Mm4Ioa.setStatus("current")
_ErxCOc3SmIr4Ioa_ObjectIdentity = ObjectIdentity
erxCOc3SmIr4Ioa = _ErxCOc3SmIr4Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 12)
)
if mibBuilder.loadTexts:
    erxCOc3SmIr4Ioa.setStatus("current")
_ErxCOc3SmLr4Ioa_ObjectIdentity = ObjectIdentity
erxCOc3SmLr4Ioa = _ErxCOc3SmLr4Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 13)
)
if mibBuilder.loadTexts:
    erxCOc3SmLr4Ioa.setStatus("current")
_ErxOc12Mm1Ioa_ObjectIdentity = ObjectIdentity
erxOc12Mm1Ioa = _ErxOc12Mm1Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 14)
)
if mibBuilder.loadTexts:
    erxOc12Mm1Ioa.setStatus("current")
_ErxOc12SmIr1Ioa_ObjectIdentity = ObjectIdentity
erxOc12SmIr1Ioa = _ErxOc12SmIr1Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 15)
)
if mibBuilder.loadTexts:
    erxOc12SmIr1Ioa.setStatus("current")
_ErxOc12SmLr1Ioa_ObjectIdentity = ObjectIdentity
erxOc12SmLr1Ioa = _ErxOc12SmLr1Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 16)
)
if mibBuilder.loadTexts:
    erxOc12SmLr1Ioa.setStatus("current")
_ErxCOc12Mm1Ioa_ObjectIdentity = ObjectIdentity
erxCOc12Mm1Ioa = _ErxCOc12Mm1Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 17)
)
if mibBuilder.loadTexts:
    erxCOc12Mm1Ioa.setStatus("current")
_ErxCOc12SmIr1Ioa_ObjectIdentity = ObjectIdentity
erxCOc12SmIr1Ioa = _ErxCOc12SmIr1Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 18)
)
if mibBuilder.loadTexts:
    erxCOc12SmIr1Ioa.setStatus("current")
_ErxCOc12SmLr1Ioa_ObjectIdentity = ObjectIdentity
erxCOc12SmLr1Ioa = _ErxCOc12SmLr1Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 19)
)
if mibBuilder.loadTexts:
    erxCOc12SmLr1Ioa.setStatus("current")
_ErxFe2Ioa_ObjectIdentity = ObjectIdentity
erxFe2Ioa = _ErxFe2Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 20)
)
if mibBuilder.loadTexts:
    erxFe2Ioa.setStatus("current")
_ErxFe8Ioa_ObjectIdentity = ObjectIdentity
erxFe8Ioa = _ErxFe8Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 21)
)
if mibBuilder.loadTexts:
    erxFe8Ioa.setStatus("current")
_ErxGeMm1Ioa_ObjectIdentity = ObjectIdentity
erxGeMm1Ioa = _ErxGeMm1Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 22)
)
if mibBuilder.loadTexts:
    erxGeMm1Ioa.setStatus("current")
_ErxGeSm1Ioa_ObjectIdentity = ObjectIdentity
erxGeSm1Ioa = _ErxGeSm1Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 23)
)
if mibBuilder.loadTexts:
    erxGeSm1Ioa.setStatus("current")
_ErxHssiIoa_ObjectIdentity = ObjectIdentity
erxHssiIoa = _ErxHssiIoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 24)
)
if mibBuilder.loadTexts:
    erxHssiIoa.setStatus("current")
_ErxCt3P12Ioa_ObjectIdentity = ObjectIdentity
erxCt3P12Ioa = _ErxCt3P12Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 25)
)
if mibBuilder.loadTexts:
    erxCt3P12Ioa.setStatus("current")
_ErxV35Ioa_ObjectIdentity = ObjectIdentity
erxV35Ioa = _ErxV35Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 26)
)
if mibBuilder.loadTexts:
    erxV35Ioa.setStatus("current")
_ErxGeSfpIoa_ObjectIdentity = ObjectIdentity
erxGeSfpIoa = _ErxGeSfpIoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 27)
)
if mibBuilder.loadTexts:
    erxGeSfpIoa.setStatus("current")
_ErxE3P12Ioa_ObjectIdentity = ObjectIdentity
erxE3P12Ioa = _ErxE3P12Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 28)
)
if mibBuilder.loadTexts:
    erxE3P12Ioa.setStatus("current")
_ErxCOc12Mm2Ioa_ObjectIdentity = ObjectIdentity
erxCOc12Mm2Ioa = _ErxCOc12Mm2Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 30)
)
if mibBuilder.loadTexts:
    erxCOc12Mm2Ioa.setStatus("current")
_ErxCOc12SmIr2Ioa_ObjectIdentity = ObjectIdentity
erxCOc12SmIr2Ioa = _ErxCOc12SmIr2Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 31)
)
if mibBuilder.loadTexts:
    erxCOc12SmIr2Ioa.setStatus("current")
_ErxCOc12SmLr2Ioa_ObjectIdentity = ObjectIdentity
erxCOc12SmLr2Ioa = _ErxCOc12SmLr2Ioa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 32)
)
if mibBuilder.loadTexts:
    erxCOc12SmLr2Ioa.setStatus("current")
_ErxOc12Mm2ApsIoa_ObjectIdentity = ObjectIdentity
erxOc12Mm2ApsIoa = _ErxOc12Mm2ApsIoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 33)
)
if mibBuilder.loadTexts:
    erxOc12Mm2ApsIoa.setStatus("current")
_ErxOc12SmIr2ApsIoa_ObjectIdentity = ObjectIdentity
erxOc12SmIr2ApsIoa = _ErxOc12SmIr2ApsIoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 34)
)
if mibBuilder.loadTexts:
    erxOc12SmIr2ApsIoa.setStatus("current")
_ErxOc12SmLr2ApsIoa_ObjectIdentity = ObjectIdentity
erxOc12SmLr2ApsIoa = _ErxOc12SmLr2ApsIoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 35)
)
if mibBuilder.loadTexts:
    erxOc12SmLr2ApsIoa.setStatus("current")
_ErxT1E1RMidSpareIoa_ObjectIdentity = ObjectIdentity
erxT1E1RMidSpareIoa = _ErxT1E1RMidSpareIoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 42)
)
if mibBuilder.loadTexts:
    erxT1E1RMidSpareIoa.setStatus("current")
_ErxT3E3RMidSpareIoa_ObjectIdentity = ObjectIdentity
erxT3E3RMidSpareIoa = _ErxT3E3RMidSpareIoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 43)
)
if mibBuilder.loadTexts:
    erxT3E3RMidSpareIoa.setStatus("current")
_ErxCt3RMidSpareIoa_ObjectIdentity = ObjectIdentity
erxCt3RMidSpareIoa = _ErxCt3RMidSpareIoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 44)
)
if mibBuilder.loadTexts:
    erxCt3RMidSpareIoa.setStatus("current")
_ErxOcxRMidSpareIoa_ObjectIdentity = ObjectIdentity
erxOcxRMidSpareIoa = _ErxOcxRMidSpareIoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 45)
)
if mibBuilder.loadTexts:
    erxOcxRMidSpareIoa.setStatus("current")
_ErxCOcxRMidSpareIoa_ObjectIdentity = ObjectIdentity
erxCOcxRMidSpareIoa = _ErxCOcxRMidSpareIoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 46)
)
if mibBuilder.loadTexts:
    erxCOcxRMidSpareIoa.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-ERX-Registry",
    **{"usdErxRegistry": usdErxRegistry,
       "usdErxEntPhysicalType": usdErxEntPhysicalType,
       "erxChassis": erxChassis,
       "erx700Chassis": erx700Chassis,
       "erx1400Chassis": erx1400Chassis,
       "erxFanAssembly": erxFanAssembly,
       "erx700FanAssembly": erx700FanAssembly,
       "erx1400FanAssembly": erx1400FanAssembly,
       "erxPowerInput": erxPowerInput,
       "erxMidplane": erxMidplane,
       "erx700Midplane": erx700Midplane,
       "erx1400Midplane": erx1400Midplane,
       "erx1Plus1RedundantT1E1Midplane": erx1Plus1RedundantT1E1Midplane,
       "erx2Plus1RedundantT1E1Midplane": erx2Plus1RedundantT1E1Midplane,
       "erx3Plus1RedundantT1E1Midplane": erx3Plus1RedundantT1E1Midplane,
       "erx4Plus1RedundantT1E1Midplane": erx4Plus1RedundantT1E1Midplane,
       "erx5Plus1RedundantT1E1Midplane": erx5Plus1RedundantT1E1Midplane,
       "erx1Plus1RedundantT3E3Midplane": erx1Plus1RedundantT3E3Midplane,
       "erx2Plus1RedundantT3E3Midplane": erx2Plus1RedundantT3E3Midplane,
       "erx3Plus1RedundantT3E3Midplane": erx3Plus1RedundantT3E3Midplane,
       "erx4Plus1RedundantT3E3Midplane": erx4Plus1RedundantT3E3Midplane,
       "erx5Plus1RedundantT3E3Midplane": erx5Plus1RedundantT3E3Midplane,
       "erx1Plus1RedundantOcMidplane": erx1Plus1RedundantOcMidplane,
       "erx2Plus1RedundantOcMidplane": erx2Plus1RedundantOcMidplane,
       "erx3Plus1RedundantOcMidplane": erx3Plus1RedundantOcMidplane,
       "erx4Plus1RedundantOcMidplane": erx4Plus1RedundantOcMidplane,
       "erx5Plus1RedundantOcMidplane": erx5Plus1RedundantOcMidplane,
       "erxSrpModule": erxSrpModule,
       "erxSrp5": erxSrp5,
       "erxSrp10": erxSrp10,
       "erxSrp10Ecc": erxSrp10Ecc,
       "erxSrp40": erxSrp40,
       "erxSrp5Plus": erxSrp5Plus,
       "erxSrp40Plus": erxSrp40Plus,
       "erxSrpIoAdapter": erxSrpIoAdapter,
       "erxLineModule": erxLineModule,
       "erxCt1": erxCt1,
       "erxCe1": erxCe1,
       "erxCt3": erxCt3,
       "erxT3Atm": erxT3Atm,
       "erxT3Frame": erxT3Frame,
       "erxE3Atm": erxE3Atm,
       "erxE3Frame": erxE3Frame,
       "erxOc3": erxOc3,
       "erxOc3Oc12Atm": erxOc3Oc12Atm,
       "erxOc3Oc12Pos": erxOc3Oc12Pos,
       "erxCOcx": erxCOcx,
       "erxFe2": erxFe2,
       "erxGeFe": erxGeFe,
       "erxTunnelService": erxTunnelService,
       "erxHssi": erxHssi,
       "erxVts": erxVts,
       "erxCt3P12": erxCt3P12,
       "erxV35": erxV35,
       "erxUt3E3Ocx": erxUt3E3Ocx,
       "erxLineIoAdapter": erxLineIoAdapter,
       "erxCt1Ioa": erxCt1Ioa,
       "erxCe1Ioa": erxCe1Ioa,
       "erxCe1TIoa": erxCe1TIoa,
       "erxCt3Ioa": erxCt3Ioa,
       "erxE3Ioa": erxE3Ioa,
       "erxOc3Mm2Ioa": erxOc3Mm2Ioa,
       "erxOc3Sm2Ioa": erxOc3Sm2Ioa,
       "erxOc3Mm4Ioa": erxOc3Mm4Ioa,
       "erxOc3SmIr4Ioa": erxOc3SmIr4Ioa,
       "erxOc3SmLr4Ioa": erxOc3SmLr4Ioa,
       "erxCOc3Mm4Ioa": erxCOc3Mm4Ioa,
       "erxCOc3SmIr4Ioa": erxCOc3SmIr4Ioa,
       "erxCOc3SmLr4Ioa": erxCOc3SmLr4Ioa,
       "erxOc12Mm1Ioa": erxOc12Mm1Ioa,
       "erxOc12SmIr1Ioa": erxOc12SmIr1Ioa,
       "erxOc12SmLr1Ioa": erxOc12SmLr1Ioa,
       "erxCOc12Mm1Ioa": erxCOc12Mm1Ioa,
       "erxCOc12SmIr1Ioa": erxCOc12SmIr1Ioa,
       "erxCOc12SmLr1Ioa": erxCOc12SmLr1Ioa,
       "erxFe2Ioa": erxFe2Ioa,
       "erxFe8Ioa": erxFe8Ioa,
       "erxGeMm1Ioa": erxGeMm1Ioa,
       "erxGeSm1Ioa": erxGeSm1Ioa,
       "erxHssiIoa": erxHssiIoa,
       "erxCt3P12Ioa": erxCt3P12Ioa,
       "erxV35Ioa": erxV35Ioa,
       "erxGeSfpIoa": erxGeSfpIoa,
       "erxE3P12Ioa": erxE3P12Ioa,
       "erxCOc12Mm2Ioa": erxCOc12Mm2Ioa,
       "erxCOc12SmIr2Ioa": erxCOc12SmIr2Ioa,
       "erxCOc12SmLr2Ioa": erxCOc12SmLr2Ioa,
       "erxOc12Mm2ApsIoa": erxOc12Mm2ApsIoa,
       "erxOc12SmIr2ApsIoa": erxOc12SmIr2ApsIoa,
       "erxOc12SmLr2ApsIoa": erxOc12SmLr2ApsIoa,
       "erxT1E1RMidSpareIoa": erxT1E1RMidSpareIoa,
       "erxT3E3RMidSpareIoa": erxT3E3RMidSpareIoa,
       "erxCt3RMidSpareIoa": erxCt3RMidSpareIoa,
       "erxOcxRMidSpareIoa": erxOcxRMidSpareIoa,
       "erxCOcxRMidSpareIoa": erxCOcxRMidSpareIoa}
)
