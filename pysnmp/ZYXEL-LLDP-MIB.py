# SNMP MIB module (ZYXEL-LLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-LLDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:13 2024
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelLldp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 43)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelLldpSetup_ObjectIdentity = ObjectIdentity
zyxelLldpSetup = _ZyxelLldpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 43, 1)
)
_ZyLldpState_Type = EnabledStatus
_ZyLldpState_Object = MibScalar
zyLldpState = _ZyLldpState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 43, 1, 1),
    _ZyLldpState_Type()
)
zyLldpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLldpState.setStatus("current")
_ZyxelLldpStatus_ObjectIdentity = ObjectIdentity
zyxelLldpStatus = _ZyxelLldpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 43, 2)
)
_ZyLldpRemoteInfoClear_Type = EnabledStatus
_ZyLldpRemoteInfoClear_Object = MibScalar
zyLldpRemoteInfoClear = _ZyLldpRemoteInfoClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 43, 2, 1),
    _ZyLldpRemoteInfoClear_Type()
)
zyLldpRemoteInfoClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLldpRemoteInfoClear.setStatus("current")
_ZyLldpRemoteInfoClearPorts_Type = PortList
_ZyLldpRemoteInfoClearPorts_Object = MibScalar
zyLldpRemoteInfoClearPorts = _ZyLldpRemoteInfoClearPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 43, 2, 2),
    _ZyLldpRemoteInfoClearPorts_Type()
)
zyLldpRemoteInfoClearPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLldpRemoteInfoClearPorts.setStatus("current")
_ZyLldpStatisticsClear_Type = EnabledStatus
_ZyLldpStatisticsClear_Object = MibScalar
zyLldpStatisticsClear = _ZyLldpStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 43, 2, 3),
    _ZyLldpStatisticsClear_Type()
)
zyLldpStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLldpStatisticsClear.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-LLDP-MIB",
    **{"zyxelLldp": zyxelLldp,
       "zyxelLldpSetup": zyxelLldpSetup,
       "zyLldpState": zyLldpState,
       "zyxelLldpStatus": zyxelLldpStatus,
       "zyLldpRemoteInfoClear": zyLldpRemoteInfoClear,
       "zyLldpRemoteInfoClearPorts": zyLldpRemoteInfoClearPorts,
       "zyLldpStatisticsClear": zyLldpStatisticsClear}
)
