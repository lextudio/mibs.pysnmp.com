# SNMP MIB module (Chromatis-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Chromatis-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:33 2024
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

chromatis = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3695)
)
chromatis.setRevisions(
        ("1999-05-17 18:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ChrCommon_ObjectIdentity = ObjectIdentity
chrCommon = _ChrCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1)
)
_ChrComHW_ObjectIdentity = ObjectIdentity
chrComHW = _ChrComHW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 1)
)
_ChrComHwNe_ObjectIdentity = ObjectIdentity
chrComHwNe = _ChrComHwNe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 1, 1)
)
_ChrComIf_ObjectIdentity = ObjectIdentity
chrComIf = _ChrComIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2)
)
_ChrComIfSonet_ObjectIdentity = ObjectIdentity
chrComIfSonet = _ChrComIfSonet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 1)
)
_ChrComIfAtm_ObjectIdentity = ObjectIdentity
chrComIfAtm = _ChrComIfAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 2)
)
_ChrComIfOptics_ObjectIdentity = ObjectIdentity
chrComIfOptics = _ChrComIfOptics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 3)
)
_ChrComIfDS3_ObjectIdentity = ObjectIdentity
chrComIfDS3 = _ChrComIfDS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 4)
)
_ChrComIfEthernet_ObjectIdentity = ObjectIdentity
chrComIfEthernet = _ChrComIfEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 2, 5)
)
_ChrComConfigVersion_ObjectIdentity = ObjectIdentity
chrComConfigVersion = _ChrComConfigVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 3)
)
_ChrComSwVersion_ObjectIdentity = ObjectIdentity
chrComSwVersion = _ChrComSwVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 4)
)
_ChrComAccess_ObjectIdentity = ObjectIdentity
chrComAccess = _ChrComAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 5)
)
_ChrComTrap_ObjectIdentity = ObjectIdentity
chrComTrap = _ChrComTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 6)
)
_ChrComActions_ObjectIdentity = ObjectIdentity
chrComActions = _ChrComActions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 7)
)
_ChrComCompressData_ObjectIdentity = ObjectIdentity
chrComCompressData = _ChrComCompressData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 8)
)
_ChrComAtm_ObjectIdentity = ObjectIdentity
chrComAtm = _ChrComAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 9)
)
_ChrComAtmVpl_ObjectIdentity = ObjectIdentity
chrComAtmVpl = _ChrComAtmVpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 9, 1)
)
_ChrComAtmVcl_ObjectIdentity = ObjectIdentity
chrComAtmVcl = _ChrComAtmVcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 9, 2)
)
_ChrComPM_ObjectIdentity = ObjectIdentity
chrComPM = _ChrComPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10)
)
_ChrComPmOptics_ObjectIdentity = ObjectIdentity
chrComPmOptics = _ChrComPmOptics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 1)
)
_ChrComPmSonet_ObjectIdentity = ObjectIdentity
chrComPmSonet = _ChrComPmSonet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 2)
)
_ChrComPmDs3_ObjectIdentity = ObjectIdentity
chrComPmDs3 = _ChrComPmDs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 3)
)
_ChrComPmAtm_ObjectIdentity = ObjectIdentity
chrComPmAtm = _ChrComPmAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4)
)
_ChrComPmEth_ObjectIdentity = ObjectIdentity
chrComPmEth = _ChrComPmEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5)
)
_ChrComFM_ObjectIdentity = ObjectIdentity
chrComFM = _ChrComFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 11)
)
_ChrComProtection_ObjectIdentity = ObjectIdentity
chrComProtection = _ChrComProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 12)
)
_ChrComProtectionGroup_ObjectIdentity = ObjectIdentity
chrComProtectionGroup = _ChrComProtectionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 12, 1)
)
_ChrComProtectionVp_ObjectIdentity = ObjectIdentity
chrComProtectionVp = _ChrComProtectionVp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 12, 2)
)
_ChrComProtectionVc_ObjectIdentity = ObjectIdentity
chrComProtectionVc = _ChrComProtectionVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 12, 3)
)
_ChrComProtectSinglePath_ObjectIdentity = ObjectIdentity
chrComProtectSinglePath = _ChrComProtectSinglePath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 12, 4)
)
_ChrComProtectEquip_ObjectIdentity = ObjectIdentity
chrComProtectEquip = _ChrComProtectEquip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 12, 5)
)
_ChrComNetwork_ObjectIdentity = ObjectIdentity
chrComNetwork = _ChrComNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 13)
)
_ChrComNetClockSync_ObjectIdentity = ObjectIdentity
chrComNetClockSync = _ChrComNetClockSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 1, 13, 1)
)
_ChrProducts_ObjectIdentity = ObjectIdentity
chrProducts = _ChrProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 2)
)
_ChrProductsMetropolis2000_ObjectIdentity = ObjectIdentity
chrProductsMetropolis2000 = _ChrProductsMetropolis2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 2, 1)
)
_ChrProductsMetropolis2500_ObjectIdentity = ObjectIdentity
chrProductsMetropolis2500 = _ChrProductsMetropolis2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 2, 2)
)
_ChrProductsMetropolis4000_ObjectIdentity = ObjectIdentity
chrProductsMetropolis4000 = _ChrProductsMetropolis4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 2, 3)
)
_ChrProductsMetropolis4500_ObjectIdentity = ObjectIdentity
chrProductsMetropolis4500 = _ChrProductsMetropolis4500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3695, 2, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Chromatis-MIB",
    **{"chromatis": chromatis,
       "chrCommon": chrCommon,
       "chrComHW": chrComHW,
       "chrComHwNe": chrComHwNe,
       "chrComIf": chrComIf,
       "chrComIfSonet": chrComIfSonet,
       "chrComIfAtm": chrComIfAtm,
       "chrComIfOptics": chrComIfOptics,
       "chrComIfDS3": chrComIfDS3,
       "chrComIfEthernet": chrComIfEthernet,
       "chrComConfigVersion": chrComConfigVersion,
       "chrComSwVersion": chrComSwVersion,
       "chrComAccess": chrComAccess,
       "chrComTrap": chrComTrap,
       "chrComActions": chrComActions,
       "chrComCompressData": chrComCompressData,
       "chrComAtm": chrComAtm,
       "chrComAtmVpl": chrComAtmVpl,
       "chrComAtmVcl": chrComAtmVcl,
       "chrComPM": chrComPM,
       "chrComPmOptics": chrComPmOptics,
       "chrComPmSonet": chrComPmSonet,
       "chrComPmDs3": chrComPmDs3,
       "chrComPmAtm": chrComPmAtm,
       "chrComPmEth": chrComPmEth,
       "chrComFM": chrComFM,
       "chrComProtection": chrComProtection,
       "chrComProtectionGroup": chrComProtectionGroup,
       "chrComProtectionVp": chrComProtectionVp,
       "chrComProtectionVc": chrComProtectionVc,
       "chrComProtectSinglePath": chrComProtectSinglePath,
       "chrComProtectEquip": chrComProtectEquip,
       "chrComNetwork": chrComNetwork,
       "chrComNetClockSync": chrComNetClockSync,
       "chrProducts": chrProducts,
       "chrProductsMetropolis2000": chrProductsMetropolis2000,
       "chrProductsMetropolis2500": chrProductsMetropolis2500,
       "chrProductsMetropolis4000": chrProductsMetropolis4000,
       "chrProductsMetropolis4500": chrProductsMetropolis4500}
)
