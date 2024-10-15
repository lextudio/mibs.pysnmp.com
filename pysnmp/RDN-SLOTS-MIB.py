# SNMP MIB module (RDN-SLOTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RDN-SLOTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:14 2024
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

(rdnDefinitions,) = mibBuilder.importSymbols(
    "RDN-DEFINITIONS-MIB",
    "rdnDefinitions")

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

rdnSlots = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 3)
)
rdnSlots.setRevisions(
        ("2008-08-08 00:00",
         "2003-11-05 00:00",
         "2003-04-29 00:00",
         "2001-04-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RdnSlotsUnknown_ObjectIdentity = ObjectIdentity
rdnSlotsUnknown = _RdnSlotsUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 3, 0)
)
_RdnSlotsBSR64000Master_ObjectIdentity = ObjectIdentity
rdnSlotsBSR64000Master = _RdnSlotsBSR64000Master_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 3, 1)
)
_RdnSlotsBSR64000IO_ObjectIdentity = ObjectIdentity
rdnSlotsBSR64000IO = _RdnSlotsBSR64000IO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 3, 2)
)
_RdnSlotsBSR1000_ObjectIdentity = ObjectIdentity
rdnSlotsBSR1000 = _RdnSlotsBSR1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 3, 3)
)
_RdnSlotsOSR2000_ObjectIdentity = ObjectIdentity
rdnSlotsOSR2000 = _RdnSlotsOSR2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 3, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RDN-SLOTS-MIB",
    **{"rdnSlots": rdnSlots,
       "rdnSlotsUnknown": rdnSlotsUnknown,
       "rdnSlotsBSR64000Master": rdnSlotsBSR64000Master,
       "rdnSlotsBSR64000IO": rdnSlotsBSR64000IO,
       "rdnSlotsBSR1000": rdnSlotsBSR1000,
       "rdnSlotsOSR2000": rdnSlotsOSR2000}
)
