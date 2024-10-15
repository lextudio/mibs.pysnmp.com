# SNMP MIB module (HUAWEI-MA5200-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MA5200-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:50 2024
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

(hwProducts,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwProducts")

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

musa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwMA5200Mib_ObjectIdentity = ObjectIdentity
hwMA5200Mib = _HwMA5200Mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2)
)
_HwMA5200G_16_ObjectIdentity = ObjectIdentity
hwMA5200G_16 = _HwMA5200G_16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 29)
)
_HwMA5200G_8_ObjectIdentity = ObjectIdentity
hwMA5200G_8 = _HwMA5200G_8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 30)
)
_HwMA5200G_4_ObjectIdentity = ObjectIdentity
hwMA5200G_4 = _HwMA5200G_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 31)
)
_HwMA5200G_2_ObjectIdentity = ObjectIdentity
hwMA5200G_2 = _HwMA5200G_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 32)
)
_HwMA5200Ifcfg_ObjectIdentity = ObjectIdentity
hwMA5200Ifcfg = _HwMA5200Ifcfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 100)
)
_HwMA5200L2tp_ObjectIdentity = ObjectIdentity
hwMA5200L2tp = _HwMA5200L2tp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 101)
)
_HwMA5200PPPoX_ObjectIdentity = ObjectIdentity
hwMA5200PPPoX = _HwMA5200PPPoX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 102)
)
_HwMA5200Srvcfg_ObjectIdentity = ObjectIdentity
hwMA5200Srvcfg = _HwMA5200Srvcfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 103)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MA5200-MIB",
    **{"musa": musa,
       "hwMA5200Mib": hwMA5200Mib,
       "hwMA5200G-16": hwMA5200G_16,
       "hwMA5200G-8": hwMA5200G_8,
       "hwMA5200G-4": hwMA5200G_4,
       "hwMA5200G-2": hwMA5200G_2,
       "hwMA5200Ifcfg": hwMA5200Ifcfg,
       "hwMA5200L2tp": hwMA5200L2tp,
       "hwMA5200PPPoX": hwMA5200PPPoX,
       "hwMA5200Srvcfg": hwMA5200Srvcfg}
)
