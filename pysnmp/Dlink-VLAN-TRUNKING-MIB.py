# SNMP MIB module (Dlink-VLAN-TRUNKING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Dlink-VLAN-TRUNKING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:35:57 2024
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

(rnd,) = mibBuilder.importSymbols(
    "DLINK-3100-MIB",
    "rnd")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlVlanTrunking = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 136)
)
rlVlanTrunking.setRevisions(
        ("2007-11-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RlVlanTrunkingEnabled_Type(TruthValue):
    """Custom type rlVlanTrunkingEnabled based on TruthValue"""


_RlVlanTrunkingEnabled_Object = MibScalar
rlVlanTrunkingEnabled = _RlVlanTrunkingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 136, 1),
    _RlVlanTrunkingEnabled_Type()
)
rlVlanTrunkingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlVlanTrunkingEnabled.setStatus("current")
_RlVlanTrunkingUplinkPorts_Type = PortList
_RlVlanTrunkingUplinkPorts_Object = MibScalar
rlVlanTrunkingUplinkPorts = _RlVlanTrunkingUplinkPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 136, 2),
    _RlVlanTrunkingUplinkPorts_Type()
)
rlVlanTrunkingUplinkPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlVlanTrunkingUplinkPorts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Dlink-VLAN-TRUNKING-MIB",
    **{"rlVlanTrunking": rlVlanTrunking,
       "rlVlanTrunkingEnabled": rlVlanTrunkingEnabled,
       "rlVlanTrunkingUplinkPorts": rlVlanTrunkingUplinkPorts}
)
