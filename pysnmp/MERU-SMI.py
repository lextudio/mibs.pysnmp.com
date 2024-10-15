# SNMP MIB module (MERU-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MERU-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:59 2024
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

meru = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Meru_reg_ObjectIdentity = ObjectIdentity
meru_reg = _Meru_reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1)
)
_Meru_wlan_ObjectIdentity = ObjectIdentity
meru_wlan = _Meru_wlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1)
)
_MwStatistics_ObjectIdentity = ObjectIdentity
mwStatistics = _MwStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mwStatistics.setStatus("current")
_MwConfiguration_ObjectIdentity = ObjectIdentity
mwConfiguration = _MwConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4)
)
if mibBuilder.loadTexts:
    mwConfiguration.setStatus("current")
_MwDiagnostics_ObjectIdentity = ObjectIdentity
mwDiagnostics = _MwDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 5)
)
if mibBuilder.loadTexts:
    mwDiagnostics.setStatus("current")
_MeruAgentCapability_ObjectIdentity = ObjectIdentity
meruAgentCapability = _MeruAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 6)
)
if mibBuilder.loadTexts:
    meruAgentCapability.setStatus("current")
_MwControllers_ObjectIdentity = ObjectIdentity
mwControllers = _MwControllers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 7)
)
if mibBuilder.loadTexts:
    mwControllers.setStatus("current")
_Mc500_ObjectIdentity = ObjectIdentity
mc500 = _Mc500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 1)
)
_Mc1000_ObjectIdentity = ObjectIdentity
mc1000 = _Mc1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 2)
)
_Mc1100_ObjectIdentity = ObjectIdentity
mc1100 = _Mc1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 3)
)
_Mc3000_ObjectIdentity = ObjectIdentity
mc3000 = _Mc3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 4)
)
_Mc500a_ObjectIdentity = ObjectIdentity
mc500a = _Mc500a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 5)
)
_Mc5000_ObjectIdentity = ObjectIdentity
mc5000 = _Mc5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 6)
)
_Mc4000_ObjectIdentity = ObjectIdentity
mc4000 = _Mc4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 7)
)
_Mc4100_ObjectIdentity = ObjectIdentity
mc4100 = _Mc4100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 8)
)
_Mc1500_ObjectIdentity = ObjectIdentity
mc1500 = _Mc1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 9)
)
_Mc3200_ObjectIdentity = ObjectIdentity
mc3200 = _Mc3200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 10)
)
_Mc4200_ObjectIdentity = ObjectIdentity
mc4200 = _Mc4200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 11)
)
_Mc6000_ObjectIdentity = ObjectIdentity
mc6000 = _Mc6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 12)
)
_Mc1500v_ObjectIdentity = ObjectIdentity
mc1500v = _Mc1500v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 13)
)
_Mc3200v_ObjectIdentity = ObjectIdentity
mc3200v = _Mc3200v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 14)
)
_Mc4200v_ObjectIdentity = ObjectIdentity
mc4200v = _Mc4200v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 15)
)
_Mc1550_ObjectIdentity = ObjectIdentity
mc1550 = _Mc1550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 16)
)
_Mc1550v_ObjectIdentity = ObjectIdentity
mc1550v = _Mc1550v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 17)
)
_Meru_modules_ObjectIdentity = ObjectIdentity
meru_modules = _Meru_modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-SMI",
    **{"meru": meru,
       "meru-reg": meru_reg,
       "meru-wlan": meru_wlan,
       "mwStatistics": mwStatistics,
       "mwConfiguration": mwConfiguration,
       "mwDiagnostics": mwDiagnostics,
       "meruAgentCapability": meruAgentCapability,
       "mwControllers": mwControllers,
       "mc500": mc500,
       "mc1000": mc1000,
       "mc1100": mc1100,
       "mc3000": mc3000,
       "mc500a": mc500a,
       "mc5000": mc5000,
       "mc4000": mc4000,
       "mc4100": mc4100,
       "mc1500": mc1500,
       "mc3200": mc3200,
       "mc4200": mc4200,
       "mc6000": mc6000,
       "mc1500v": mc1500v,
       "mc3200v": mc3200v,
       "mc4200v": mc4200v,
       "mc1550": mc1550,
       "mc1550v": mc1550v,
       "meru-modules": meru_modules}
)
