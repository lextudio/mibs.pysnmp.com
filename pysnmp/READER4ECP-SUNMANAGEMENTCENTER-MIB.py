# SNMP MIB module (READER4ECP-SUNMANAGEMENTCENTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/READER4ECP-SUNMANAGEMENTCENTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:16 2024
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

_Sun_ObjectIdentity = ObjectIdentity
sun = _Sun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42)
)
_Prod_ObjectIdentity = ObjectIdentity
prod = _Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2)
)
_Sunsymon_ObjectIdentity = ObjectIdentity
sunsymon = _Sunsymon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12)
)
_Agent_ObjectIdentity = ObjectIdentity
agent = _Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2)
)
_Base_ObjectIdentity = ObjectIdentity
base = _Base_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1)
)
_Modules_ObjectIdentity = ObjectIdentity
modules = _Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2)
)
_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 1)
)
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 1, 1)
)
_Reader4u_ObjectIdentity = ObjectIdentity
reader4u = _Reader4u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 1, 1, 1)
)
_Reader4udt_ObjectIdentity = ObjectIdentity
reader4udt = _Reader4udt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 1, 1, 2)
)
_Reader4uwg_ObjectIdentity = ObjectIdentity
reader4uwg = _Reader4uwg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 1, 1, 3)
)
_Reader4u1P_ObjectIdentity = ObjectIdentity
reader4u1P = _Reader4u1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 1, 1, 4)
)
_Reader4u1D_ObjectIdentity = ObjectIdentity
reader4u1D = _Reader4u1D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 1, 1, 5)
)
_Reader4unt_ObjectIdentity = ObjectIdentity
reader4unt = _Reader4unt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 1, 1, 6)
)
_ReaderSerengeti_ObjectIdentity = ObjectIdentity
readerSerengeti = _ReaderSerengeti_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 1, 1, 7)
)
_Reader4uvh_ObjectIdentity = ObjectIdentity
reader4uvh = _Reader4uvh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 1, 1, 8)
)
_ReaderECP_ObjectIdentity = ObjectIdentity
readerECP = _ReaderECP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 1, 1, 9)
)
_ReaderELP_ObjectIdentity = ObjectIdentity
readerELP = _ReaderELP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 1, 1, 10)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "READER4ECP-SUNMANAGEMENTCENTER-MIB",
    **{"sun": sun,
       "prod": prod,
       "sunsymon": sunsymon,
       "agent": agent,
       "base": base,
       "modules": modules,
       "hardware": hardware,
       "config": config,
       "reader4u": reader4u,
       "reader4udt": reader4udt,
       "reader4uwg": reader4uwg,
       "reader4u1P": reader4u1P,
       "reader4u1D": reader4u1D,
       "reader4unt": reader4unt,
       "readerSerengeti": readerSerengeti,
       "reader4uvh": reader4uvh,
       "readerECP": readerECP,
       "readerELP": readerELP}
)
