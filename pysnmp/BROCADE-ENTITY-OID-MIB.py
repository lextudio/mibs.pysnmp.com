# SNMP MIB module (BROCADE-ENTITY-OID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BROCADE-ENTITY-OID-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:19 2024
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

(products,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "products")

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

brcdEntityOIDMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17)
)
brcdEntityOIDMIB.setRevisions(
        ("2013-02-06 09:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BrcdEntityOIDMIBObjects_ObjectIdentity = ObjectIdentity
brcdEntityOIDMIBObjects = _BrcdEntityOIDMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1)
)
_BrcdEntityOIDOther_ObjectIdentity = ObjectIdentity
brcdEntityOIDOther = _BrcdEntityOIDOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 1)
)
_BrcdEntityOIDUnknown_ObjectIdentity = ObjectIdentity
brcdEntityOIDUnknown = _BrcdEntityOIDUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 2)
)
_BrcdEntityOIDChassis_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassis = _BrcdEntityOIDChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3)
)
_BrcdEntityOIDChassisUnknown_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisUnknown = _BrcdEntityOIDChassisUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 1)
)
_BrcdEntityOIDChassisNetIronCes2000Family_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisNetIronCes2000Family = _BrcdEntityOIDChassisNetIronCes2000Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 2)
)
_BrcdEntityOIDChassisNetIronCes2024F_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisNetIronCes2024F = _BrcdEntityOIDChassisNetIronCes2024F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 2, 1)
)
_BrcdEntityOIDChassisNetIronCes2024C_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisNetIronCes2024C = _BrcdEntityOIDChassisNetIronCes2024C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 2, 2)
)
_BrcdEntityOIDChassisNetIronCes2048F_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisNetIronCes2048F = _BrcdEntityOIDChassisNetIronCes2048F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 2, 3)
)
_BrcdEntityOIDChassisNetIronCes2048C_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisNetIronCes2048C = _BrcdEntityOIDChassisNetIronCes2048C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 2, 4)
)
_BrcdEntityOIDChassisNetIronCes2048FX_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisNetIronCes2048FX = _BrcdEntityOIDChassisNetIronCes2048FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 2, 5)
)
_BrcdEntityOIDChassisNetIronCes2048CX_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisNetIronCes2048CX = _BrcdEntityOIDChassisNetIronCes2048CX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 2, 6)
)
_BrcdEntityOIDChassisNetIronCes2024F4X_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisNetIronCes2024F4X = _BrcdEntityOIDChassisNetIronCes2024F4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 2, 7)
)
_BrcdEntityOIDChassisNetIronCes2024C4X_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisNetIronCes2024C4X = _BrcdEntityOIDChassisNetIronCes2024C4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 2, 8)
)
_BrcdEntityOIDChassisNetIronCer2000Family_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisNetIronCer2000Family = _BrcdEntityOIDChassisNetIronCer2000Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 3)
)
_BrcdEntityOIDChassisNetIronCer2024F_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisNetIronCer2024F = _BrcdEntityOIDChassisNetIronCer2024F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 3, 1)
)
_BrcdEntityOIDChassisNetIronCer2024C_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisNetIronCer2024C = _BrcdEntityOIDChassisNetIronCer2024C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 3, 2)
)
_BrcdEntityOIDChassisNetIronCer2048F_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisNetIronCer2048F = _BrcdEntityOIDChassisNetIronCer2048F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 3, 3)
)
_BrcdEntityOIDChassisNetIronCer2048C_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisNetIronCer2048C = _BrcdEntityOIDChassisNetIronCer2048C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 3, 4)
)
_BrcdEntityOIDChassisNetIronCer2048FX_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisNetIronCer2048FX = _BrcdEntityOIDChassisNetIronCer2048FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 3, 5)
)
_BrcdEntityOIDChassisNetIronCer2048CX_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisNetIronCer2048CX = _BrcdEntityOIDChassisNetIronCer2048CX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 3, 6)
)
_BrcdEntityOIDChassisNetIronCer2024F4X_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisNetIronCer2024F4X = _BrcdEntityOIDChassisNetIronCer2024F4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 3, 7)
)
_BrcdEntityOIDChassisNetIronCer2024C4X_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisNetIronCer2024C4X = _BrcdEntityOIDChassisNetIronCer2024C4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 3, 8)
)
_BrcdEntityOIDChassisNetIronXMRFamily_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisNetIronXMRFamily = _BrcdEntityOIDChassisNetIronXMRFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 4)
)
_BrcdEntityOIDChassisNetIronXMR4000_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisNetIronXMR4000 = _BrcdEntityOIDChassisNetIronXMR4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 4, 1)
)
_BrcdEntityOIDChassisNetIronXMR8000_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisNetIronXMR8000 = _BrcdEntityOIDChassisNetIronXMR8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 4, 2)
)
_BrcdEntityOIDChassisNetIronXMR16000_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisNetIronXMR16000 = _BrcdEntityOIDChassisNetIronXMR16000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 4, 3)
)
_BrcdEntityOIDChassisNetIronXMR32000_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisNetIronXMR32000 = _BrcdEntityOIDChassisNetIronXMR32000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 4, 4)
)
_BrcdEntityOIDChassisMLXFamily_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisMLXFamily = _BrcdEntityOIDChassisMLXFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 5)
)
_BrcdEntityOIDChassisMLX4_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisMLX4 = _BrcdEntityOIDChassisMLX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 5, 1)
)
_BrcdEntityOIDChassisMLX8_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisMLX8 = _BrcdEntityOIDChassisMLX8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 5, 2)
)
_BrcdEntityOIDChassisMLX16_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisMLX16 = _BrcdEntityOIDChassisMLX16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 5, 3)
)
_BrcdEntityOIDChassisMLX32_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisMLX32 = _BrcdEntityOIDChassisMLX32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 5, 4)
)
_BrcdEntityOIDChassisMLXeFamily_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisMLXeFamily = _BrcdEntityOIDChassisMLXeFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 6)
)
_BrcdEntityOIDChassisMLXe4_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisMLXe4 = _BrcdEntityOIDChassisMLXe4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 6, 1)
)
_BrcdEntityOIDChassisMLXe8_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisMLXe8 = _BrcdEntityOIDChassisMLXe8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 6, 2)
)
_BrcdEntityOIDChassisMLXe16_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisMLXe16 = _BrcdEntityOIDChassisMLXe16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 6, 3)
)
_BrcdEntityOIDChassisMLXe32_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisMLXe32 = _BrcdEntityOIDChassisMLXe32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 6, 4)
)
_BrcdEntityOIDBackplane_ObjectIdentity = ObjectIdentity
brcdEntityOIDBackplane = _BrcdEntityOIDBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 4)
)
_BrcdEntityOIDBackplaneUnknown_ObjectIdentity = ObjectIdentity
brcdEntityOIDBackplaneUnknown = _BrcdEntityOIDBackplaneUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 4, 1)
)
_BrcdEntityOIDBackplaneNetIronFamily_ObjectIdentity = ObjectIdentity
brcdEntityOIDBackplaneNetIronFamily = _BrcdEntityOIDBackplaneNetIronFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 4, 2)
)
_BrcdEntityOIDBackplaneNetIronCes2000_ObjectIdentity = ObjectIdentity
brcdEntityOIDBackplaneNetIronCes2000 = _BrcdEntityOIDBackplaneNetIronCes2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 4, 2, 1)
)
_BrcdEntityOIDBackplaneNetIronCer2000_ObjectIdentity = ObjectIdentity
brcdEntityOIDBackplaneNetIronCer2000 = _BrcdEntityOIDBackplaneNetIronCer2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 4, 2, 2)
)
_BrcdEntityOIDBackplaneNetIronXMR_ObjectIdentity = ObjectIdentity
brcdEntityOIDBackplaneNetIronXMR = _BrcdEntityOIDBackplaneNetIronXMR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 4, 2, 3)
)
_BrcdEntityOIDBackplaneMlxFamily_ObjectIdentity = ObjectIdentity
brcdEntityOIDBackplaneMlxFamily = _BrcdEntityOIDBackplaneMlxFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 4, 3)
)
_BrcdEntityOIDBackplaneMLX_ObjectIdentity = ObjectIdentity
brcdEntityOIDBackplaneMLX = _BrcdEntityOIDBackplaneMLX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 4, 3, 1)
)
_BrcdEntityOIDBackplaneMLXe_ObjectIdentity = ObjectIdentity
brcdEntityOIDBackplaneMLXe = _BrcdEntityOIDBackplaneMLXe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 4, 3, 2)
)
_BrcdEntityOIDContainer_ObjectIdentity = ObjectIdentity
brcdEntityOIDContainer = _BrcdEntityOIDContainer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 5)
)
_BrcdEntityOIDContainerUnknown_ObjectIdentity = ObjectIdentity
brcdEntityOIDContainerUnknown = _BrcdEntityOIDContainerUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 5, 1)
)
_BrcdEntityOIDContainerPowerSupply_ObjectIdentity = ObjectIdentity
brcdEntityOIDContainerPowerSupply = _BrcdEntityOIDContainerPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 5, 2)
)
_BrcdEntityOIDContainerFanTray_ObjectIdentity = ObjectIdentity
brcdEntityOIDContainerFanTray = _BrcdEntityOIDContainerFanTray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 5, 3)
)
_BrcdEntityOIDContainerMgmtModuleSlot_ObjectIdentity = ObjectIdentity
brcdEntityOIDContainerMgmtModuleSlot = _BrcdEntityOIDContainerMgmtModuleSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 5, 4)
)
_BrcdEntityOIDContainerSwitchFabricModuleSlot_ObjectIdentity = ObjectIdentity
brcdEntityOIDContainerSwitchFabricModuleSlot = _BrcdEntityOIDContainerSwitchFabricModuleSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 5, 5)
)
_BrcdEntityOIDContainerIntfModuleSlot_ObjectIdentity = ObjectIdentity
brcdEntityOIDContainerIntfModuleSlot = _BrcdEntityOIDContainerIntfModuleSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 5, 6)
)
_BrcdEntityOIDPowerSupply_ObjectIdentity = ObjectIdentity
brcdEntityOIDPowerSupply = _BrcdEntityOIDPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6)
)
_BrcdEntityOIDPowerSupplyUnknown_ObjectIdentity = ObjectIdentity
brcdEntityOIDPowerSupplyUnknown = _BrcdEntityOIDPowerSupplyUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 1)
)
_BrcdEntityOIDPowerSupplyAC500W_ObjectIdentity = ObjectIdentity
brcdEntityOIDPowerSupplyAC500W = _BrcdEntityOIDPowerSupplyAC500W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 2)
)
_BrcdEntityOIDPowerSupplyDC500W_ObjectIdentity = ObjectIdentity
brcdEntityOIDPowerSupplyDC500W = _BrcdEntityOIDPowerSupplyDC500W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 3)
)
_BrcdEntityOIDPowerSupplyAC1200W_ObjectIdentity = ObjectIdentity
brcdEntityOIDPowerSupplyAC1200W = _BrcdEntityOIDPowerSupplyAC1200W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 4)
)
_BrcdEntityOIDPowerSupplyDC1200W_ObjectIdentity = ObjectIdentity
brcdEntityOIDPowerSupplyDC1200W = _BrcdEntityOIDPowerSupplyDC1200W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 5)
)
_BrcdEntityOIDPowerSupplyAC1200WA_ObjectIdentity = ObjectIdentity
brcdEntityOIDPowerSupplyAC1200WA = _BrcdEntityOIDPowerSupplyAC1200WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 6)
)
_BrcdEntityOIDPowerSupplyDC1200WA_ObjectIdentity = ObjectIdentity
brcdEntityOIDPowerSupplyDC1200WA = _BrcdEntityOIDPowerSupplyDC1200WA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 7)
)
_BrcdEntityOIDPowerSupplyAC1800W_ObjectIdentity = ObjectIdentity
brcdEntityOIDPowerSupplyAC1800W = _BrcdEntityOIDPowerSupplyAC1800W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 8)
)
_BrcdEntityOIDPowerSupplyDC1800W_ObjectIdentity = ObjectIdentity
brcdEntityOIDPowerSupplyDC1800W = _BrcdEntityOIDPowerSupplyDC1800W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 9)
)
_BrcdEntityOIDPowerSupplyAC2100W_ObjectIdentity = ObjectIdentity
brcdEntityOIDPowerSupplyAC2100W = _BrcdEntityOIDPowerSupplyAC2100W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 10)
)
_BrcdEntityOIDPowerSupplyDC2100W_ObjectIdentity = ObjectIdentity
brcdEntityOIDPowerSupplyDC2100W = _BrcdEntityOIDPowerSupplyDC2100W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 11)
)
_BrcdEntityOIDPowerSupplyAC2400W_ObjectIdentity = ObjectIdentity
brcdEntityOIDPowerSupplyAC2400W = _BrcdEntityOIDPowerSupplyAC2400W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 12)
)
_BrcdEntityOIDPowerSupplyDC2400W_ObjectIdentity = ObjectIdentity
brcdEntityOIDPowerSupplyDC2400W = _BrcdEntityOIDPowerSupplyDC2400W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 13)
)
_BrcdEntityOIDPowerSupplyAC3000W_ObjectIdentity = ObjectIdentity
brcdEntityOIDPowerSupplyAC3000W = _BrcdEntityOIDPowerSupplyAC3000W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 14)
)
_BrcdEntityOIDPowerSupplyDC3000W_ObjectIdentity = ObjectIdentity
brcdEntityOIDPowerSupplyDC3000W = _BrcdEntityOIDPowerSupplyDC3000W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 15)
)
_BrcdEntityOIDFan_ObjectIdentity = ObjectIdentity
brcdEntityOIDFan = _BrcdEntityOIDFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 7)
)
_BrcdEntityOIDFanUnknown_ObjectIdentity = ObjectIdentity
brcdEntityOIDFanUnknown = _BrcdEntityOIDFanUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 7, 1)
)
_BrcdEntityOIDChassisFanTray_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisFanTray = _BrcdEntityOIDChassisFanTray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 7, 2)
)
_BrcdEntityOIDChassisFan_ObjectIdentity = ObjectIdentity
brcdEntityOIDChassisFan = _BrcdEntityOIDChassisFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 7, 3)
)
_BrcdEntityOIDSensor_ObjectIdentity = ObjectIdentity
brcdEntityOIDSensor = _BrcdEntityOIDSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 8)
)
_BrcdEntityOIDSensorUnknown_ObjectIdentity = ObjectIdentity
brcdEntityOIDSensorUnknown = _BrcdEntityOIDSensorUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 8, 1)
)
_BrcdEntityOIDSensorChipTemp_ObjectIdentity = ObjectIdentity
brcdEntityOIDSensorChipTemp = _BrcdEntityOIDSensorChipTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 8, 2)
)
_BrcdEntityOIDSensorModuleTemp_ObjectIdentity = ObjectIdentity
brcdEntityOIDSensorModuleTemp = _BrcdEntityOIDSensorModuleTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 8, 3)
)
_BrcdEntityOIDModule_ObjectIdentity = ObjectIdentity
brcdEntityOIDModule = _BrcdEntityOIDModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9)
)
_BrcdEntityOIDModuleUnknown_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleUnknown = _BrcdEntityOIDModuleUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 1)
)
_BrcdEntityOIDModuleMgmt_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleMgmt = _BrcdEntityOIDModuleMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 2)
)
_BrcdEntityOIDModuleMgmtUnknown_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleMgmtUnknown = _BrcdEntityOIDModuleMgmtUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 2, 1)
)
_BrcdEntityOIDModuleMgmtNetIronFamily_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleMgmtNetIronFamily = _BrcdEntityOIDModuleMgmtNetIronFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 2, 2)
)
_BrcdEntityOIDModuleMgmtNiMlxMr_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleMgmtNiMlxMr = _BrcdEntityOIDModuleMgmtNiMlxMr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 2, 2, 1)
)
_BrcdEntityOIDModuleMgmtNiMlx32Mr_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleMgmtNiMlx32Mr = _BrcdEntityOIDModuleMgmtNiMlx32Mr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 2, 2, 2)
)
_BrcdEntityOIDModuleMgmtNiXmrMr_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleMgmtNiXmrMr = _BrcdEntityOIDModuleMgmtNiXmrMr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 2, 2, 3)
)
_BrcdEntityOIDModuleMgmtNiXmr32Mr_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleMgmtNiXmr32Mr = _BrcdEntityOIDModuleMgmtNiXmr32Mr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 2, 2, 4)
)
_BrcdEntityOIDModuleMgmtMlxFamily_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleMgmtMlxFamily = _BrcdEntityOIDModuleMgmtMlxFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 2, 3)
)
_BrcdEntityOIDModuleMgmtBrMlxMr2M_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleMgmtBrMlxMr2M = _BrcdEntityOIDModuleMgmtBrMlxMr2M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 2, 3, 1)
)
_BrcdEntityOIDModuleMgmtBrMlxMr2X_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleMgmtBrMlxMr2X = _BrcdEntityOIDModuleMgmtBrMlxMr2X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 2, 3, 2)
)
_BrcdEntityOIDModuleMgmtBrMlx32Mr2M_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleMgmtBrMlx32Mr2M = _BrcdEntityOIDModuleMgmtBrMlx32Mr2M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 2, 3, 3)
)
_BrcdEntityOIDModuleMgmtBrMlx32Mr2X_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleMgmtBrMlx32Mr2X = _BrcdEntityOIDModuleMgmtBrMlx32Mr2X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 2, 3, 4)
)
_BrcdEntityOIDModuleSfm_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleSfm = _BrcdEntityOIDModuleSfm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 3)
)
_BrcdEntityOIDModuleSfmUnknown_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleSfmUnknown = _BrcdEntityOIDModuleSfmUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 3, 1)
)
_BrcdEntityOIDModuleSfmNetIronFamily_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleSfmNetIronFamily = _BrcdEntityOIDModuleSfmNetIronFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 3, 2)
)
_BrcdEntityOIDModuleSfmNiXSf1_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleSfmNiXSf1 = _BrcdEntityOIDModuleSfmNiXSf1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 3, 2, 1)
)
_BrcdEntityOIDModuleSfmNiXSf3_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleSfmNiXSf3 = _BrcdEntityOIDModuleSfmNiXSf3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 3, 2, 2)
)
_BrcdEntityOIDModuleSfmNiX32Sf_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleSfmNiX32Sf = _BrcdEntityOIDModuleSfmNiX32Sf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 3, 2, 3)
)
_BrcdEntityOIDModuleSfmNiX4Hsf_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleSfmNiX4Hsf = _BrcdEntityOIDModuleSfmNiX4Hsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 3, 2, 4)
)
_BrcdEntityOIDModuleSfmNiX16n8Hsf_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleSfmNiX16n8Hsf = _BrcdEntityOIDModuleSfmNiX16n8Hsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 3, 2, 5)
)
_BrcdEntityOIDModuleSfmNiX32Hsf_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleSfmNiX32Hsf = _BrcdEntityOIDModuleSfmNiX32Hsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 3, 2, 6)
)
_BrcdEntityOIDModuleIntf_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntf = _BrcdEntityOIDModuleIntf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4)
)
_BrcdEntityOIDModuleIntfUnknown_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfUnknown = _BrcdEntityOIDModuleIntfUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 1)
)
_BrcdEntityOIDModuleIntfNetIronFamily_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfNetIronFamily = _BrcdEntityOIDModuleIntfNetIronFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 2)
)
_BrcdEntityOIDModuleIntfNiMlx1Gx20Gc_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfNiMlx1Gx20Gc = _BrcdEntityOIDModuleIntfNiMlx1Gx20Gc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 2, 1)
)
_BrcdEntityOIDModuleIntfNiXmr1Gx20Gc_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfNiXmr1Gx20Gc = _BrcdEntityOIDModuleIntfNiXmr1Gx20Gc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 2, 2)
)
_BrcdEntityOIDModuleIntfNiMlx1Gx48Ta_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfNiMlx1Gx48Ta = _BrcdEntityOIDModuleIntfNiMlx1Gx48Ta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 2, 3)
)
_BrcdEntityOIDModuleIntfNiMlx1Gx20Sfp_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfNiMlx1Gx20Sfp = _BrcdEntityOIDModuleIntfNiMlx1Gx20Sfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 2, 4)
)
_BrcdEntityOIDModuleIntfNiXmr1Gx20Sfp_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfNiXmr1Gx20Sfp = _BrcdEntityOIDModuleIntfNiXmr1Gx20Sfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 2, 5)
)
_BrcdEntityOIDModuleIntfNiMlx10Gx2_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfNiMlx10Gx2 = _BrcdEntityOIDModuleIntfNiMlx10Gx2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 2, 6)
)
_BrcdEntityOIDModuleIntfNiXmr10Gx2_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfNiXmr10Gx2 = _BrcdEntityOIDModuleIntfNiXmr10Gx2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 2, 7)
)
_BrcdEntityOIDModuleIntfNiMlx10Gx4_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfNiMlx10Gx4 = _BrcdEntityOIDModuleIntfNiMlx10Gx4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 2, 8)
)
_BrcdEntityOIDModuleIntfNiXmr10Gx4_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfNiXmr10Gx4 = _BrcdEntityOIDModuleIntfNiXmr10Gx4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 2, 9)
)
_BrcdEntityOIDModuleIntfNiMlx10Gx8D_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfNiMlx10Gx8D = _BrcdEntityOIDModuleIntfNiMlx10Gx8D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 2, 10)
)
_BrcdEntityOIDModuleIntfNiMlx10Gx8M_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfNiMlx10Gx8M = _BrcdEntityOIDModuleIntfNiMlx10Gx8M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 2, 11)
)
_BrcdEntityOIDModuleIntfMlxFamily_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfMlxFamily = _BrcdEntityOIDModuleIntfMlxFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3)
)
_BrcdEntityOIDModuleIntfBrMlx1Gcx24X_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfBrMlx1Gcx24X = _BrcdEntityOIDModuleIntfBrMlx1Gcx24X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 1)
)
_BrcdEntityOIDModuleIntfBrMlx1Gcx24xMl_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfBrMlx1Gcx24xMl = _BrcdEntityOIDModuleIntfBrMlx1Gcx24xMl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 2)
)
_BrcdEntityOIDModuleIntfBrMlx1Gfx24X_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfBrMlx1Gfx24X = _BrcdEntityOIDModuleIntfBrMlx1Gfx24X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 3)
)
_BrcdEntityOIDModuleIntfBrMlx1Gfx24xMl_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfBrMlx1Gfx24xMl = _BrcdEntityOIDModuleIntfBrMlx1Gfx24xMl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 4)
)
_BrcdEntityOIDModuleIntfBrMlx10Gx4X_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfBrMlx10Gx4X = _BrcdEntityOIDModuleIntfBrMlx10Gx4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 5)
)
_BrcdEntityOIDModuleIntfBrMlx10Gx4xMl_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfBrMlx10Gx4xMl = _BrcdEntityOIDModuleIntfBrMlx10Gx4xMl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 6)
)
_BrcdEntityOIDModuleIntfBrMlx10Gx8X_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfBrMlx10Gx8X = _BrcdEntityOIDModuleIntfBrMlx10Gx8X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 7)
)
_BrcdEntityOIDModuleIntfBrMlx10Gx24Dm_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfBrMlx10Gx24Dm = _BrcdEntityOIDModuleIntfBrMlx10Gx24Dm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 8)
)
_BrcdEntityOIDModuleIntfBrMlx40Gx2_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfBrMlx40Gx2 = _BrcdEntityOIDModuleIntfBrMlx40Gx2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 9)
)
_BrcdEntityOIDModuleIntfBrMlx40Gx4_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfBrMlx40Gx4 = _BrcdEntityOIDModuleIntfBrMlx40Gx4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 10)
)
_BrcdEntityOIDModuleIntfBrMlx100Gx1_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfBrMlx100Gx1 = _BrcdEntityOIDModuleIntfBrMlx100Gx1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 11)
)
_BrcdEntityOIDModuleIntfBrMlx100Gx2_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfBrMlx100Gx2 = _BrcdEntityOIDModuleIntfBrMlx100Gx2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 12)
)
_BrcdEntityOIDModuleIntfBrMlx100Gx2CFP2_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfBrMlx100Gx2CFP2 = _BrcdEntityOIDModuleIntfBrMlx100Gx2CFP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 13)
)
_BrcdEntityOIDModuleIntfBrMlx10Gx20_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfBrMlx10Gx20 = _BrcdEntityOIDModuleIntfBrMlx10Gx20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 14)
)
_BrcdEntityOIDModuleIntfBrMlx10Gx4IPSecModule_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleIntfBrMlx10Gx4IPSecModule = _BrcdEntityOIDModuleIntfBrMlx10Gx4IPSecModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 15)
)
_BrcdEntityOIDModuleOptics_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleOptics = _BrcdEntityOIDModuleOptics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 5)
)
_BrcdEntityOIDModuleOpticsUnknown_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleOpticsUnknown = _BrcdEntityOIDModuleOpticsUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 5, 1)
)
_BrcdEntityOIDModuleOpticsSFP_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleOpticsSFP = _BrcdEntityOIDModuleOpticsSFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 5, 2)
)
_BrcdEntityOIDModuleOpticsSFPP_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleOpticsSFPP = _BrcdEntityOIDModuleOpticsSFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 5, 3)
)
_BrcdEntityOIDModuleOpticsXFP_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleOpticsXFP = _BrcdEntityOIDModuleOpticsXFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 5, 4)
)
_BrcdEntityOIDModuleOpticsCFP_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleOpticsCFP = _BrcdEntityOIDModuleOpticsCFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 5, 5)
)
_BrcdEntityOIDModuleOpticsQSFPP_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleOpticsQSFPP = _BrcdEntityOIDModuleOpticsQSFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 5, 6)
)
_BrcdEntityOIDModuleOpticsCFP2_ObjectIdentity = ObjectIdentity
brcdEntityOIDModuleOpticsCFP2 = _BrcdEntityOIDModuleOpticsCFP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 5, 7)
)
_BrcdEntityOIDPort_ObjectIdentity = ObjectIdentity
brcdEntityOIDPort = _BrcdEntityOIDPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 10)
)
_BrcdEntityOIDPortUnknown_ObjectIdentity = ObjectIdentity
brcdEntityOIDPortUnknown = _BrcdEntityOIDPortUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 10, 1)
)
_BrcdEntityOIDPortMgmtSerial_ObjectIdentity = ObjectIdentity
brcdEntityOIDPortMgmtSerial = _BrcdEntityOIDPortMgmtSerial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 10, 2)
)
_BrcdEntityOIDPortMgmtEth_ObjectIdentity = ObjectIdentity
brcdEntityOIDPortMgmtEth = _BrcdEntityOIDPortMgmtEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 10, 3)
)
_BrcdEntityOIDPort100BaseTx_ObjectIdentity = ObjectIdentity
brcdEntityOIDPort100BaseTx = _BrcdEntityOIDPort100BaseTx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 10, 4)
)
_BrcdEntityOIDPort100BaseFx_ObjectIdentity = ObjectIdentity
brcdEntityOIDPort100BaseFx = _BrcdEntityOIDPort100BaseFx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 10, 5)
)
_BrcdEntityOIDPortGigBaseTx_ObjectIdentity = ObjectIdentity
brcdEntityOIDPortGigBaseTx = _BrcdEntityOIDPortGigBaseTx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 10, 6)
)
_BrcdEntityOIDPortGigBaseFx_ObjectIdentity = ObjectIdentity
brcdEntityOIDPortGigBaseFx = _BrcdEntityOIDPortGigBaseFx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 10, 7)
)
_BrcdEntityOIDPort10GigBaseFx_ObjectIdentity = ObjectIdentity
brcdEntityOIDPort10GigBaseFx = _BrcdEntityOIDPort10GigBaseFx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 10, 8)
)
_BrcdEntityOIDPort40GigBaseFx_ObjectIdentity = ObjectIdentity
brcdEntityOIDPort40GigBaseFx = _BrcdEntityOIDPort40GigBaseFx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 10, 9)
)
_BrcdEntityOIDPort100GigBaseFx_ObjectIdentity = ObjectIdentity
brcdEntityOIDPort100GigBaseFx = _BrcdEntityOIDPort100GigBaseFx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 10, 10)
)
_BrcdEntityOIDPort10GigBaseTx_ObjectIdentity = ObjectIdentity
brcdEntityOIDPort10GigBaseTx = _BrcdEntityOIDPort10GigBaseTx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 10, 11)
)
_BrcdEntityOIDStack_ObjectIdentity = ObjectIdentity
brcdEntityOIDStack = _BrcdEntityOIDStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 11)
)
_BrcdEntityOIDStackUnknown_ObjectIdentity = ObjectIdentity
brcdEntityOIDStackUnknown = _BrcdEntityOIDStackUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 11, 1)
)
_BrcdEntityOIDCpu_ObjectIdentity = ObjectIdentity
brcdEntityOIDCpu = _BrcdEntityOIDCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 12)
)
_BrcdEntityOIDCpuUnknown_ObjectIdentity = ObjectIdentity
brcdEntityOIDCpuUnknown = _BrcdEntityOIDCpuUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 12, 1)
)
_BrcdEntityOIDCpuPPC7447A_ObjectIdentity = ObjectIdentity
brcdEntityOIDCpuPPC7447A = _BrcdEntityOIDCpuPPC7447A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 12, 2)
)
_BrcdEntityOIDCpuPPC7448_ObjectIdentity = ObjectIdentity
brcdEntityOIDCpuPPC7448 = _BrcdEntityOIDCpuPPC7448_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 12, 3)
)
_BrcdEntityOIDCpuPPC7451_ObjectIdentity = ObjectIdentity
brcdEntityOIDCpuPPC7451 = _BrcdEntityOIDCpuPPC7451_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 12, 4)
)
_BrcdEntityOIDCpuPPC7455_ObjectIdentity = ObjectIdentity
brcdEntityOIDCpuPPC7455 = _BrcdEntityOIDCpuPPC7455_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 12, 5)
)
_BrcdEntityOIDCpuPPC7457_ObjectIdentity = ObjectIdentity
brcdEntityOIDCpuPPC7457 = _BrcdEntityOIDCpuPPC7457_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 12, 6)
)
_BrcdEntityOIDCpuPPC8541_ObjectIdentity = ObjectIdentity
brcdEntityOIDCpuPPC8541 = _BrcdEntityOIDCpuPPC8541_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 12, 7)
)
_BrcdEntityOIDCpuPPC8541E_ObjectIdentity = ObjectIdentity
brcdEntityOIDCpuPPC8541E = _BrcdEntityOIDCpuPPC8541E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 12, 8)
)
_BrcdEntityOIDCpuPPC8544_ObjectIdentity = ObjectIdentity
brcdEntityOIDCpuPPC8544 = _BrcdEntityOIDCpuPPC8544_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 12, 9)
)
_BrcdEntityOIDCpuPPC8544E_ObjectIdentity = ObjectIdentity
brcdEntityOIDCpuPPC8544E = _BrcdEntityOIDCpuPPC8544E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 12, 10)
)
_BrcdEntityOIDCpuPPC8572_ObjectIdentity = ObjectIdentity
brcdEntityOIDCpuPPC8572 = _BrcdEntityOIDCpuPPC8572_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 12, 11)
)
_BrcdEntityOIDCpuPPC8572E_ObjectIdentity = ObjectIdentity
brcdEntityOIDCpuPPC8572E = _BrcdEntityOIDCpuPPC8572E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 12, 12)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROCADE-ENTITY-OID-MIB",
    **{"brcdEntityOIDMIB": brcdEntityOIDMIB,
       "brcdEntityOIDMIBObjects": brcdEntityOIDMIBObjects,
       "brcdEntityOIDOther": brcdEntityOIDOther,
       "brcdEntityOIDUnknown": brcdEntityOIDUnknown,
       "brcdEntityOIDChassis": brcdEntityOIDChassis,
       "brcdEntityOIDChassisUnknown": brcdEntityOIDChassisUnknown,
       "brcdEntityOIDChassisNetIronCes2000Family": brcdEntityOIDChassisNetIronCes2000Family,
       "brcdEntityOIDChassisNetIronCes2024F": brcdEntityOIDChassisNetIronCes2024F,
       "brcdEntityOIDChassisNetIronCes2024C": brcdEntityOIDChassisNetIronCes2024C,
       "brcdEntityOIDChassisNetIronCes2048F": brcdEntityOIDChassisNetIronCes2048F,
       "brcdEntityOIDChassisNetIronCes2048C": brcdEntityOIDChassisNetIronCes2048C,
       "brcdEntityOIDChassisNetIronCes2048FX": brcdEntityOIDChassisNetIronCes2048FX,
       "brcdEntityOIDChassisNetIronCes2048CX": brcdEntityOIDChassisNetIronCes2048CX,
       "brcdEntityOIDChassisNetIronCes2024F4X": brcdEntityOIDChassisNetIronCes2024F4X,
       "brcdEntityOIDChassisNetIronCes2024C4X": brcdEntityOIDChassisNetIronCes2024C4X,
       "brcdEntityOIDChassisNetIronCer2000Family": brcdEntityOIDChassisNetIronCer2000Family,
       "brcdEntityOIDChassisNetIronCer2024F": brcdEntityOIDChassisNetIronCer2024F,
       "brcdEntityOIDChassisNetIronCer2024C": brcdEntityOIDChassisNetIronCer2024C,
       "brcdEntityOIDChassisNetIronCer2048F": brcdEntityOIDChassisNetIronCer2048F,
       "brcdEntityOIDChassisNetIronCer2048C": brcdEntityOIDChassisNetIronCer2048C,
       "brcdEntityOIDChassisNetIronCer2048FX": brcdEntityOIDChassisNetIronCer2048FX,
       "brcdEntityOIDChassisNetIronCer2048CX": brcdEntityOIDChassisNetIronCer2048CX,
       "brcdEntityOIDChassisNetIronCer2024F4X": brcdEntityOIDChassisNetIronCer2024F4X,
       "brcdEntityOIDChassisNetIronCer2024C4X": brcdEntityOIDChassisNetIronCer2024C4X,
       "brcdEntityOIDChassisNetIronXMRFamily": brcdEntityOIDChassisNetIronXMRFamily,
       "brcdEntityOIDChassisNetIronXMR4000": brcdEntityOIDChassisNetIronXMR4000,
       "brcdEntityOIDChassisNetIronXMR8000": brcdEntityOIDChassisNetIronXMR8000,
       "brcdEntityOIDChassisNetIronXMR16000": brcdEntityOIDChassisNetIronXMR16000,
       "brcdEntityOIDChassisNetIronXMR32000": brcdEntityOIDChassisNetIronXMR32000,
       "brcdEntityOIDChassisMLXFamily": brcdEntityOIDChassisMLXFamily,
       "brcdEntityOIDChassisMLX4": brcdEntityOIDChassisMLX4,
       "brcdEntityOIDChassisMLX8": brcdEntityOIDChassisMLX8,
       "brcdEntityOIDChassisMLX16": brcdEntityOIDChassisMLX16,
       "brcdEntityOIDChassisMLX32": brcdEntityOIDChassisMLX32,
       "brcdEntityOIDChassisMLXeFamily": brcdEntityOIDChassisMLXeFamily,
       "brcdEntityOIDChassisMLXe4": brcdEntityOIDChassisMLXe4,
       "brcdEntityOIDChassisMLXe8": brcdEntityOIDChassisMLXe8,
       "brcdEntityOIDChassisMLXe16": brcdEntityOIDChassisMLXe16,
       "brcdEntityOIDChassisMLXe32": brcdEntityOIDChassisMLXe32,
       "brcdEntityOIDBackplane": brcdEntityOIDBackplane,
       "brcdEntityOIDBackplaneUnknown": brcdEntityOIDBackplaneUnknown,
       "brcdEntityOIDBackplaneNetIronFamily": brcdEntityOIDBackplaneNetIronFamily,
       "brcdEntityOIDBackplaneNetIronCes2000": brcdEntityOIDBackplaneNetIronCes2000,
       "brcdEntityOIDBackplaneNetIronCer2000": brcdEntityOIDBackplaneNetIronCer2000,
       "brcdEntityOIDBackplaneNetIronXMR": brcdEntityOIDBackplaneNetIronXMR,
       "brcdEntityOIDBackplaneMlxFamily": brcdEntityOIDBackplaneMlxFamily,
       "brcdEntityOIDBackplaneMLX": brcdEntityOIDBackplaneMLX,
       "brcdEntityOIDBackplaneMLXe": brcdEntityOIDBackplaneMLXe,
       "brcdEntityOIDContainer": brcdEntityOIDContainer,
       "brcdEntityOIDContainerUnknown": brcdEntityOIDContainerUnknown,
       "brcdEntityOIDContainerPowerSupply": brcdEntityOIDContainerPowerSupply,
       "brcdEntityOIDContainerFanTray": brcdEntityOIDContainerFanTray,
       "brcdEntityOIDContainerMgmtModuleSlot": brcdEntityOIDContainerMgmtModuleSlot,
       "brcdEntityOIDContainerSwitchFabricModuleSlot": brcdEntityOIDContainerSwitchFabricModuleSlot,
       "brcdEntityOIDContainerIntfModuleSlot": brcdEntityOIDContainerIntfModuleSlot,
       "brcdEntityOIDPowerSupply": brcdEntityOIDPowerSupply,
       "brcdEntityOIDPowerSupplyUnknown": brcdEntityOIDPowerSupplyUnknown,
       "brcdEntityOIDPowerSupplyAC500W": brcdEntityOIDPowerSupplyAC500W,
       "brcdEntityOIDPowerSupplyDC500W": brcdEntityOIDPowerSupplyDC500W,
       "brcdEntityOIDPowerSupplyAC1200W": brcdEntityOIDPowerSupplyAC1200W,
       "brcdEntityOIDPowerSupplyDC1200W": brcdEntityOIDPowerSupplyDC1200W,
       "brcdEntityOIDPowerSupplyAC1200WA": brcdEntityOIDPowerSupplyAC1200WA,
       "brcdEntityOIDPowerSupplyDC1200WA": brcdEntityOIDPowerSupplyDC1200WA,
       "brcdEntityOIDPowerSupplyAC1800W": brcdEntityOIDPowerSupplyAC1800W,
       "brcdEntityOIDPowerSupplyDC1800W": brcdEntityOIDPowerSupplyDC1800W,
       "brcdEntityOIDPowerSupplyAC2100W": brcdEntityOIDPowerSupplyAC2100W,
       "brcdEntityOIDPowerSupplyDC2100W": brcdEntityOIDPowerSupplyDC2100W,
       "brcdEntityOIDPowerSupplyAC2400W": brcdEntityOIDPowerSupplyAC2400W,
       "brcdEntityOIDPowerSupplyDC2400W": brcdEntityOIDPowerSupplyDC2400W,
       "brcdEntityOIDPowerSupplyAC3000W": brcdEntityOIDPowerSupplyAC3000W,
       "brcdEntityOIDPowerSupplyDC3000W": brcdEntityOIDPowerSupplyDC3000W,
       "brcdEntityOIDFan": brcdEntityOIDFan,
       "brcdEntityOIDFanUnknown": brcdEntityOIDFanUnknown,
       "brcdEntityOIDChassisFanTray": brcdEntityOIDChassisFanTray,
       "brcdEntityOIDChassisFan": brcdEntityOIDChassisFan,
       "brcdEntityOIDSensor": brcdEntityOIDSensor,
       "brcdEntityOIDSensorUnknown": brcdEntityOIDSensorUnknown,
       "brcdEntityOIDSensorChipTemp": brcdEntityOIDSensorChipTemp,
       "brcdEntityOIDSensorModuleTemp": brcdEntityOIDSensorModuleTemp,
       "brcdEntityOIDModule": brcdEntityOIDModule,
       "brcdEntityOIDModuleUnknown": brcdEntityOIDModuleUnknown,
       "brcdEntityOIDModuleMgmt": brcdEntityOIDModuleMgmt,
       "brcdEntityOIDModuleMgmtUnknown": brcdEntityOIDModuleMgmtUnknown,
       "brcdEntityOIDModuleMgmtNetIronFamily": brcdEntityOIDModuleMgmtNetIronFamily,
       "brcdEntityOIDModuleMgmtNiMlxMr": brcdEntityOIDModuleMgmtNiMlxMr,
       "brcdEntityOIDModuleMgmtNiMlx32Mr": brcdEntityOIDModuleMgmtNiMlx32Mr,
       "brcdEntityOIDModuleMgmtNiXmrMr": brcdEntityOIDModuleMgmtNiXmrMr,
       "brcdEntityOIDModuleMgmtNiXmr32Mr": brcdEntityOIDModuleMgmtNiXmr32Mr,
       "brcdEntityOIDModuleMgmtMlxFamily": brcdEntityOIDModuleMgmtMlxFamily,
       "brcdEntityOIDModuleMgmtBrMlxMr2M": brcdEntityOIDModuleMgmtBrMlxMr2M,
       "brcdEntityOIDModuleMgmtBrMlxMr2X": brcdEntityOIDModuleMgmtBrMlxMr2X,
       "brcdEntityOIDModuleMgmtBrMlx32Mr2M": brcdEntityOIDModuleMgmtBrMlx32Mr2M,
       "brcdEntityOIDModuleMgmtBrMlx32Mr2X": brcdEntityOIDModuleMgmtBrMlx32Mr2X,
       "brcdEntityOIDModuleSfm": brcdEntityOIDModuleSfm,
       "brcdEntityOIDModuleSfmUnknown": brcdEntityOIDModuleSfmUnknown,
       "brcdEntityOIDModuleSfmNetIronFamily": brcdEntityOIDModuleSfmNetIronFamily,
       "brcdEntityOIDModuleSfmNiXSf1": brcdEntityOIDModuleSfmNiXSf1,
       "brcdEntityOIDModuleSfmNiXSf3": brcdEntityOIDModuleSfmNiXSf3,
       "brcdEntityOIDModuleSfmNiX32Sf": brcdEntityOIDModuleSfmNiX32Sf,
       "brcdEntityOIDModuleSfmNiX4Hsf": brcdEntityOIDModuleSfmNiX4Hsf,
       "brcdEntityOIDModuleSfmNiX16n8Hsf": brcdEntityOIDModuleSfmNiX16n8Hsf,
       "brcdEntityOIDModuleSfmNiX32Hsf": brcdEntityOIDModuleSfmNiX32Hsf,
       "brcdEntityOIDModuleIntf": brcdEntityOIDModuleIntf,
       "brcdEntityOIDModuleIntfUnknown": brcdEntityOIDModuleIntfUnknown,
       "brcdEntityOIDModuleIntfNetIronFamily": brcdEntityOIDModuleIntfNetIronFamily,
       "brcdEntityOIDModuleIntfNiMlx1Gx20Gc": brcdEntityOIDModuleIntfNiMlx1Gx20Gc,
       "brcdEntityOIDModuleIntfNiXmr1Gx20Gc": brcdEntityOIDModuleIntfNiXmr1Gx20Gc,
       "brcdEntityOIDModuleIntfNiMlx1Gx48Ta": brcdEntityOIDModuleIntfNiMlx1Gx48Ta,
       "brcdEntityOIDModuleIntfNiMlx1Gx20Sfp": brcdEntityOIDModuleIntfNiMlx1Gx20Sfp,
       "brcdEntityOIDModuleIntfNiXmr1Gx20Sfp": brcdEntityOIDModuleIntfNiXmr1Gx20Sfp,
       "brcdEntityOIDModuleIntfNiMlx10Gx2": brcdEntityOIDModuleIntfNiMlx10Gx2,
       "brcdEntityOIDModuleIntfNiXmr10Gx2": brcdEntityOIDModuleIntfNiXmr10Gx2,
       "brcdEntityOIDModuleIntfNiMlx10Gx4": brcdEntityOIDModuleIntfNiMlx10Gx4,
       "brcdEntityOIDModuleIntfNiXmr10Gx4": brcdEntityOIDModuleIntfNiXmr10Gx4,
       "brcdEntityOIDModuleIntfNiMlx10Gx8D": brcdEntityOIDModuleIntfNiMlx10Gx8D,
       "brcdEntityOIDModuleIntfNiMlx10Gx8M": brcdEntityOIDModuleIntfNiMlx10Gx8M,
       "brcdEntityOIDModuleIntfMlxFamily": brcdEntityOIDModuleIntfMlxFamily,
       "brcdEntityOIDModuleIntfBrMlx1Gcx24X": brcdEntityOIDModuleIntfBrMlx1Gcx24X,
       "brcdEntityOIDModuleIntfBrMlx1Gcx24xMl": brcdEntityOIDModuleIntfBrMlx1Gcx24xMl,
       "brcdEntityOIDModuleIntfBrMlx1Gfx24X": brcdEntityOIDModuleIntfBrMlx1Gfx24X,
       "brcdEntityOIDModuleIntfBrMlx1Gfx24xMl": brcdEntityOIDModuleIntfBrMlx1Gfx24xMl,
       "brcdEntityOIDModuleIntfBrMlx10Gx4X": brcdEntityOIDModuleIntfBrMlx10Gx4X,
       "brcdEntityOIDModuleIntfBrMlx10Gx4xMl": brcdEntityOIDModuleIntfBrMlx10Gx4xMl,
       "brcdEntityOIDModuleIntfBrMlx10Gx8X": brcdEntityOIDModuleIntfBrMlx10Gx8X,
       "brcdEntityOIDModuleIntfBrMlx10Gx24Dm": brcdEntityOIDModuleIntfBrMlx10Gx24Dm,
       "brcdEntityOIDModuleIntfBrMlx40Gx2": brcdEntityOIDModuleIntfBrMlx40Gx2,
       "brcdEntityOIDModuleIntfBrMlx40Gx4": brcdEntityOIDModuleIntfBrMlx40Gx4,
       "brcdEntityOIDModuleIntfBrMlx100Gx1": brcdEntityOIDModuleIntfBrMlx100Gx1,
       "brcdEntityOIDModuleIntfBrMlx100Gx2": brcdEntityOIDModuleIntfBrMlx100Gx2,
       "brcdEntityOIDModuleIntfBrMlx100Gx2CFP2": brcdEntityOIDModuleIntfBrMlx100Gx2CFP2,
       "brcdEntityOIDModuleIntfBrMlx10Gx20": brcdEntityOIDModuleIntfBrMlx10Gx20,
       "brcdEntityOIDModuleIntfBrMlx10Gx4IPSecModule": brcdEntityOIDModuleIntfBrMlx10Gx4IPSecModule,
       "brcdEntityOIDModuleOptics": brcdEntityOIDModuleOptics,
       "brcdEntityOIDModuleOpticsUnknown": brcdEntityOIDModuleOpticsUnknown,
       "brcdEntityOIDModuleOpticsSFP": brcdEntityOIDModuleOpticsSFP,
       "brcdEntityOIDModuleOpticsSFPP": brcdEntityOIDModuleOpticsSFPP,
       "brcdEntityOIDModuleOpticsXFP": brcdEntityOIDModuleOpticsXFP,
       "brcdEntityOIDModuleOpticsCFP": brcdEntityOIDModuleOpticsCFP,
       "brcdEntityOIDModuleOpticsQSFPP": brcdEntityOIDModuleOpticsQSFPP,
       "brcdEntityOIDModuleOpticsCFP2": brcdEntityOIDModuleOpticsCFP2,
       "brcdEntityOIDPort": brcdEntityOIDPort,
       "brcdEntityOIDPortUnknown": brcdEntityOIDPortUnknown,
       "brcdEntityOIDPortMgmtSerial": brcdEntityOIDPortMgmtSerial,
       "brcdEntityOIDPortMgmtEth": brcdEntityOIDPortMgmtEth,
       "brcdEntityOIDPort100BaseTx": brcdEntityOIDPort100BaseTx,
       "brcdEntityOIDPort100BaseFx": brcdEntityOIDPort100BaseFx,
       "brcdEntityOIDPortGigBaseTx": brcdEntityOIDPortGigBaseTx,
       "brcdEntityOIDPortGigBaseFx": brcdEntityOIDPortGigBaseFx,
       "brcdEntityOIDPort10GigBaseFx": brcdEntityOIDPort10GigBaseFx,
       "brcdEntityOIDPort40GigBaseFx": brcdEntityOIDPort40GigBaseFx,
       "brcdEntityOIDPort100GigBaseFx": brcdEntityOIDPort100GigBaseFx,
       "brcdEntityOIDPort10GigBaseTx": brcdEntityOIDPort10GigBaseTx,
       "brcdEntityOIDStack": brcdEntityOIDStack,
       "brcdEntityOIDStackUnknown": brcdEntityOIDStackUnknown,
       "brcdEntityOIDCpu": brcdEntityOIDCpu,
       "brcdEntityOIDCpuUnknown": brcdEntityOIDCpuUnknown,
       "brcdEntityOIDCpuPPC7447A": brcdEntityOIDCpuPPC7447A,
       "brcdEntityOIDCpuPPC7448": brcdEntityOIDCpuPPC7448,
       "brcdEntityOIDCpuPPC7451": brcdEntityOIDCpuPPC7451,
       "brcdEntityOIDCpuPPC7455": brcdEntityOIDCpuPPC7455,
       "brcdEntityOIDCpuPPC7457": brcdEntityOIDCpuPPC7457,
       "brcdEntityOIDCpuPPC8541": brcdEntityOIDCpuPPC8541,
       "brcdEntityOIDCpuPPC8541E": brcdEntityOIDCpuPPC8541E,
       "brcdEntityOIDCpuPPC8544": brcdEntityOIDCpuPPC8544,
       "brcdEntityOIDCpuPPC8544E": brcdEntityOIDCpuPPC8544E,
       "brcdEntityOIDCpuPPC8572": brcdEntityOIDCpuPPC8572,
       "brcdEntityOIDCpuPPC8572E": brcdEntityOIDCpuPPC8572E}
)
