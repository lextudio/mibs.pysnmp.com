# SNMP MIB module (Intel-Common-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Intel-Common-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:40 2024
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

_Intel_ObjectIdentity = ObjectIdentity
intel = _Intel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343)
)
_Identifiers_ObjectIdentity = ObjectIdentity
identifiers = _Identifiers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1)
)
_Systems_ObjectIdentity = ObjectIdentity
systems = _Systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 1)
)
_Pc_systems_ObjectIdentity = ObjectIdentity
pc_systems = _Pc_systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 1)
)
_Proxy_systems_ObjectIdentity = ObjectIdentity
proxy_systems = _Proxy_systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 2)
)
_Hub_systems_ObjectIdentity = ObjectIdentity
hub_systems = _Hub_systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 3)
)
_Express10_100Stack_ObjectIdentity = ObjectIdentity
express10_100Stack = _Express10_100Stack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 3, 1)
)
_Express12TX_ObjectIdentity = ObjectIdentity
express12TX = _Express12TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 3, 2)
)
_Express24TX_ObjectIdentity = ObjectIdentity
express24TX = _Express24TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 3, 3)
)
_ExpressReserved_ObjectIdentity = ObjectIdentity
expressReserved = _ExpressReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 3, 4)
)
_ExpressBridge_ObjectIdentity = ObjectIdentity
expressBridge = _ExpressBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 3, 6)
)
_Express210_12_ObjectIdentity = ObjectIdentity
express210_12 = _Express210_12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 3, 7)
)
_Express210_24_ObjectIdentity = ObjectIdentity
express210_24 = _Express210_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 3, 8)
)
_Express220_12_ObjectIdentity = ObjectIdentity
express220_12 = _Express220_12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 3, 9)
)
_Express220_24_ObjectIdentity = ObjectIdentity
express220_24 = _Express220_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 3, 10)
)
_Express300Stack_ObjectIdentity = ObjectIdentity
express300Stack = _Express300Stack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 3, 11)
)
_Express320_16_ObjectIdentity = ObjectIdentity
express320_16 = _Express320_16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 3, 12)
)
_Express320_24_ObjectIdentity = ObjectIdentity
express320_24 = _Express320_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 3, 13)
)
_Switch_systems_ObjectIdentity = ObjectIdentity
switch_systems = _Switch_systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 1, 4)
)
_Objects_ObjectIdentity = ObjectIdentity
objects = _Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 2)
)
_Comm_methods_ObjectIdentity = ObjectIdentity
comm_methods = _Comm_methods_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 3)
)
_Local_proxy_1_ObjectIdentity = ObjectIdentity
local_proxy_1 = _Local_proxy_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 3, 1)
)
_Pc_novell_1_ObjectIdentity = ObjectIdentity
pc_novell_1 = _Pc_novell_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 1, 3, 2)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2)
)
_Pc_products_ObjectIdentity = ObjectIdentity
pc_products = _Pc_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 1)
)
_Hub_products_ObjectIdentity = ObjectIdentity
hub_products = _Hub_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 2)
)
_Express110_ObjectIdentity = ObjectIdentity
express110 = _Express110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 2, 1)
)
_Proxy_ObjectIdentity = ObjectIdentity
proxy = _Proxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 3)
)
_Print_products_ObjectIdentity = ObjectIdentity
print_products = _Print_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 4)
)
_Netport_1_ObjectIdentity = ObjectIdentity
netport_1 = _Netport_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 4, 1)
)
_Netport_2_ObjectIdentity = ObjectIdentity
netport_2 = _Netport_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 4, 2)
)
_Netport_express_ObjectIdentity = ObjectIdentity
netport_express = _Netport_express_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 4, 3)
)
_Network_products_ObjectIdentity = ObjectIdentity
network_products = _Network_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 5)
)
_LanDesk_ObjectIdentity = ObjectIdentity
lanDesk = _LanDesk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 5, 1)
)
_Ld_alarms_ObjectIdentity = ObjectIdentity
ld_alarms = _Ld_alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 5, 1, 1)
)
_InternetServer_2_ObjectIdentity = ObjectIdentity
internetServer_2 = _InternetServer_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 5, 2)
)
_IS_alarms_ObjectIdentity = ObjectIdentity
iS_alarms = _IS_alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 5, 2, 1)
)
_Snmp_agents_ObjectIdentity = ObjectIdentity
snmp_agents = _Snmp_agents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 6)
)
_Nic_products_ObjectIdentity = ObjectIdentity
nic_products = _Nic_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 7)
)
_Server_management_ObjectIdentity = ObjectIdentity
server_management = _Server_management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 10)
)
_Switch_products_ObjectIdentity = ObjectIdentity
switch_products = _Switch_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 11)
)
_I2o_ObjectIdentity = ObjectIdentity
i2o = _I2o_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 120)
)
_Experimental_ObjectIdentity = ObjectIdentity
experimental = _Experimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 3)
)
_Information_technology_ObjectIdentity = ObjectIdentity
information_technology = _Information_technology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 4)
)
_SysProducts_ObjectIdentity = ObjectIdentity
sysProducts = _SysProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5)
)
_Mib2ext_ObjectIdentity = ObjectIdentity
mib2ext = _Mib2ext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6)
)
_Hw_ObjectIdentity = ObjectIdentity
hw = _Hw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 7)
)
_Wekiva_ObjectIdentity = ObjectIdentity
wekiva = _Wekiva_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 111)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Intel-Common-MIB",
    **{"intel": intel,
       "identifiers": identifiers,
       "systems": systems,
       "pc-systems": pc_systems,
       "proxy-systems": proxy_systems,
       "hub-systems": hub_systems,
       "express10-100Stack": express10_100Stack,
       "express12TX": express12TX,
       "express24TX": express24TX,
       "expressReserved": expressReserved,
       "expressBridge": expressBridge,
       "express210-12": express210_12,
       "express210-24": express210_24,
       "express220-12": express220_12,
       "express220-24": express220_24,
       "express300Stack": express300Stack,
       "express320-16": express320_16,
       "express320-24": express320_24,
       "switch-systems": switch_systems,
       "objects": objects,
       "comm-methods": comm_methods,
       "local-proxy-1": local_proxy_1,
       "pc-novell-1": pc_novell_1,
       "products": products,
       "pc-products": pc_products,
       "hub-products": hub_products,
       "express110": express110,
       "proxy": proxy,
       "print-products": print_products,
       "netport-1": netport_1,
       "netport-2": netport_2,
       "netport-express": netport_express,
       "network-products": network_products,
       "lanDesk": lanDesk,
       "ld-alarms": ld_alarms,
       "internetServer-2": internetServer_2,
       "iS-alarms": iS_alarms,
       "snmp-agents": snmp_agents,
       "nic-products": nic_products,
       "server-management": server_management,
       "switch-products": switch_products,
       "i2o": i2o,
       "experimental": experimental,
       "information-technology": information_technology,
       "sysProducts": sysProducts,
       "mib2ext": mib2ext,
       "hw": hw,
       "wekiva": wekiva}
)
