# SNMP MIB module (NET-SNMP-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NET-SNMP-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:25 2024
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

(netSnmpModuleIDs,
 netSnmpObjects) = mibBuilder.importSymbols(
    "NET-SNMP-MIB",
    "netSnmpModuleIDs",
    "netSnmpObjects")

(Float,) = mibBuilder.importSymbols(
    "NET-SNMP-TC",
    "Float")

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

netSnmpSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 4)
)
netSnmpSystemMIB.setRevisions(
        ("2002-02-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsMemory_ObjectIdentity = ObjectIdentity
nsMemory = _NsMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 31)
)
_NsSwap_ObjectIdentity = ObjectIdentity
nsSwap = _NsSwap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 32)
)
_NsCPU_ObjectIdentity = ObjectIdentity
nsCPU = _NsCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 33)
)
_NsLoad_ObjectIdentity = ObjectIdentity
nsLoad = _NsLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 34)
)
_NsDiskIO_ObjectIdentity = ObjectIdentity
nsDiskIO = _NsDiskIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 1, 35)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NET-SNMP-SYSTEM-MIB",
    **{"nsMemory": nsMemory,
       "nsSwap": nsSwap,
       "nsCPU": nsCPU,
       "nsLoad": nsLoad,
       "nsDiskIO": nsDiskIO,
       "netSnmpSystemMIB": netSnmpSystemMIB}
)
