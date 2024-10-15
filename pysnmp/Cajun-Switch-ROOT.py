# SNMP MIB module (Cajun-Switch-ROOT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Cajun-Switch-ROOT
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:29 2024
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

lucent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1)
)
_CajunSwitchProduct_ObjectIdentity = ObjectIdentity
cajunSwitchProduct = _CajunSwitchProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 45)
)
_CajunL2P550_ObjectIdentity = ObjectIdentity
cajunL2P550 = _CajunL2P550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 45, 1)
)
_CajunL3P550_ObjectIdentity = ObjectIdentity
cajunL3P550 = _CajunL3P550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 45, 2)
)
_CajunP220G_ObjectIdentity = ObjectIdentity
cajunP220G = _CajunP220G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 45, 3)
)
_CajunP220FE_ObjectIdentity = ObjectIdentity
cajunP220FE = _CajunP220FE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 45, 4)
)
_CajunL2P660_ObjectIdentity = ObjectIdentity
cajunL2P660 = _CajunL2P660_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 45, 5)
)
_CajunL3P660_ObjectIdentity = ObjectIdentity
cajunL3P660 = _CajunL3P660_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 45, 6)
)
_CajunL2P850_ObjectIdentity = ObjectIdentity
cajunL2P850 = _CajunL2P850_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 45, 7)
)
_CajunL3P850_ObjectIdentity = ObjectIdentity
cajunL3P850 = _CajunL3P850_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 45, 8)
)
_CajunL2P880_ObjectIdentity = ObjectIdentity
cajunL2P880 = _CajunL2P880_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 45, 9)
)
_CajunL3P880_ObjectIdentity = ObjectIdentity
cajunL3P880 = _CajunL3P880_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 45, 10)
)
_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2)
)
_CajunSwitch_ObjectIdentity = ObjectIdentity
cajunSwitch = _CajunSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 45)
)
_CajunAgentGen_ObjectIdentity = ObjectIdentity
cajunAgentGen = _CajunAgentGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 45, 1)
)
_CajunAgentCommunity_ObjectIdentity = ObjectIdentity
cajunAgentCommunity = _CajunAgentCommunity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 45, 2)
)
_CajunChassis_ObjectIdentity = ObjectIdentity
cajunChassis = _CajunChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 45, 3)
)
_CajunLayer2Switching_ObjectIdentity = ObjectIdentity
cajunLayer2Switching = _CajunLayer2Switching_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 45, 4)
)
_CajunVlanMgt_ObjectIdentity = ObjectIdentity
cajunVlanMgt = _CajunVlanMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 45, 5)
)
_CajunEvents_ObjectIdentity = ObjectIdentity
cajunEvents = _CajunEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 45, 6)
)
_CajunlarmMgt_ObjectIdentity = ObjectIdentity
cajunlarmMgt = _CajunlarmMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 45, 7)
)
_CajunSnmpTraps_ObjectIdentity = ObjectIdentity
cajunSnmpTraps = _CajunSnmpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 45, 8)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Cajun-Switch-ROOT",
    **{"lucent": lucent,
       "products": products,
       "cajunSwitchProduct": cajunSwitchProduct,
       "cajunL2P550": cajunL2P550,
       "cajunL3P550": cajunL3P550,
       "cajunP220G": cajunP220G,
       "cajunP220FE": cajunP220FE,
       "cajunL2P660": cajunL2P660,
       "cajunL3P660": cajunL3P660,
       "cajunL2P850": cajunL2P850,
       "cajunL3P850": cajunL3P850,
       "cajunL2P880": cajunL2P880,
       "cajunL3P880": cajunL3P880,
       "mibs": mibs,
       "cajunSwitch": cajunSwitch,
       "cajunAgentGen": cajunAgentGen,
       "cajunAgentCommunity": cajunAgentCommunity,
       "cajunChassis": cajunChassis,
       "cajunLayer2Switching": cajunLayer2Switching,
       "cajunVlanMgt": cajunVlanMgt,
       "cajunEvents": cajunEvents,
       "cajunlarmMgt": cajunlarmMgt,
       "cajunSnmpTraps": cajunSnmpTraps}
)
