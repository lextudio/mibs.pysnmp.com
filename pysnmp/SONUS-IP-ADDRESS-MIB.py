# SNMP MIB module (SONUS-IP-ADDRESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-IP-ADDRESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:58 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(sonusPacketMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusPacketMIBs")


# MODULE-IDENTITY

sonusIpAddressMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusIpAddrTable_Object = MibTable
sonusIpAddrTable = _SonusIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    sonusIpAddrTable.setStatus("current")
_SonusIpAddrEntry_Object = MibTableRow
sonusIpAddrEntry = _SonusIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 2, 1, 1)
)
sonusIpAddrEntry.setIndexNames(
    (0, "SONUS-IP-ADDRESS-MIB", "sonusIpAdEntShelf"),
    (0, "SONUS-IP-ADDRESS-MIB", "sonusIpAdEntSlot"),
    (0, "SONUS-IP-ADDRESS-MIB", "sonusIpAdEntInstance"),
    (0, "SONUS-IP-ADDRESS-MIB", "sonusIpAdEntAddr"),
)
if mibBuilder.loadTexts:
    sonusIpAddrEntry.setStatus("current")
_SonusIpAdEntAddr_Type = IpAddress
_SonusIpAdEntAddr_Object = MibTableColumn
sonusIpAdEntAddr = _SonusIpAdEntAddr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 2, 1, 1, 1),
    _SonusIpAdEntAddr_Type()
)
sonusIpAdEntAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpAdEntAddr.setStatus("current")


class _SonusIpAdEntIfIndex_Type(Integer32):
    """Custom type sonusIpAdEntIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SonusIpAdEntIfIndex_Type.__name__ = "Integer32"
_SonusIpAdEntIfIndex_Object = MibTableColumn
sonusIpAdEntIfIndex = _SonusIpAdEntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 2, 1, 1, 2),
    _SonusIpAdEntIfIndex_Type()
)
sonusIpAdEntIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpAdEntIfIndex.setStatus("current")
_SonusIpAdEntNetMask_Type = IpAddress
_SonusIpAdEntNetMask_Object = MibTableColumn
sonusIpAdEntNetMask = _SonusIpAdEntNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 2, 1, 1, 3),
    _SonusIpAdEntNetMask_Type()
)
sonusIpAdEntNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpAdEntNetMask.setStatus("current")


class _SonusIpAdEntBcastAddr_Type(Integer32):
    """Custom type sonusIpAdEntBcastAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SonusIpAdEntBcastAddr_Type.__name__ = "Integer32"
_SonusIpAdEntBcastAddr_Object = MibTableColumn
sonusIpAdEntBcastAddr = _SonusIpAdEntBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 2, 1, 1, 4),
    _SonusIpAdEntBcastAddr_Type()
)
sonusIpAdEntBcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpAdEntBcastAddr.setStatus("current")


class _SonusIpAdEntReasmMaxSize_Type(Integer32):
    """Custom type sonusIpAdEntReasmMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusIpAdEntReasmMaxSize_Type.__name__ = "Integer32"
_SonusIpAdEntReasmMaxSize_Object = MibTableColumn
sonusIpAdEntReasmMaxSize = _SonusIpAdEntReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 2, 1, 1, 5),
    _SonusIpAdEntReasmMaxSize_Type()
)
sonusIpAdEntReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpAdEntReasmMaxSize.setStatus("current")
_SonusIpAdEntShelf_Type = Integer32
_SonusIpAdEntShelf_Object = MibTableColumn
sonusIpAdEntShelf = _SonusIpAdEntShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 2, 1, 1, 6),
    _SonusIpAdEntShelf_Type()
)
sonusIpAdEntShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIpAdEntShelf.setStatus("current")
_SonusIpAdEntSlot_Type = Integer32
_SonusIpAdEntSlot_Object = MibTableColumn
sonusIpAdEntSlot = _SonusIpAdEntSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 2, 1, 1, 7),
    _SonusIpAdEntSlot_Type()
)
sonusIpAdEntSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIpAdEntSlot.setStatus("current")
_SonusIpAdEntInstance_Type = Integer32
_SonusIpAdEntInstance_Object = MibTableColumn
sonusIpAdEntInstance = _SonusIpAdEntInstance_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 2, 1, 1, 8),
    _SonusIpAdEntInstance_Type()
)
sonusIpAdEntInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIpAdEntInstance.setStatus("current")
_SonusIpNetToMediaTable_Object = MibTable
sonusIpNetToMediaTable = _SonusIpNetToMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 2, 2)
)
if mibBuilder.loadTexts:
    sonusIpNetToMediaTable.setStatus("current")
_SonusIpNetToMediaEntry_Object = MibTableRow
sonusIpNetToMediaEntry = _SonusIpNetToMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 2, 2, 1)
)
sonusIpNetToMediaEntry.setIndexNames(
    (0, "SONUS-IP-ADDRESS-MIB", "sonusIpNetToMediaShelf"),
    (0, "SONUS-IP-ADDRESS-MIB", "sonusIpNetToMediaSlot"),
    (0, "SONUS-IP-ADDRESS-MIB", "sonusIpNetToMediaInstance"),
    (0, "SONUS-IP-ADDRESS-MIB", "sonusIpNetToMediaIfIndex"),
    (0, "SONUS-IP-ADDRESS-MIB", "sonusIpNetToMediaNetAddress"),
)
if mibBuilder.loadTexts:
    sonusIpNetToMediaEntry.setStatus("current")


class _SonusIpNetToMediaIfIndex_Type(Integer32):
    """Custom type sonusIpNetToMediaIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SonusIpNetToMediaIfIndex_Type.__name__ = "Integer32"
_SonusIpNetToMediaIfIndex_Object = MibTableColumn
sonusIpNetToMediaIfIndex = _SonusIpNetToMediaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 2, 2, 1, 1),
    _SonusIpNetToMediaIfIndex_Type()
)
sonusIpNetToMediaIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusIpNetToMediaIfIndex.setStatus("current")
_SonusIpNetToMediaPhysAddress_Type = PhysAddress
_SonusIpNetToMediaPhysAddress_Object = MibTableColumn
sonusIpNetToMediaPhysAddress = _SonusIpNetToMediaPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 2, 2, 1, 2),
    _SonusIpNetToMediaPhysAddress_Type()
)
sonusIpNetToMediaPhysAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusIpNetToMediaPhysAddress.setStatus("current")
_SonusIpNetToMediaNetAddress_Type = IpAddress
_SonusIpNetToMediaNetAddress_Object = MibTableColumn
sonusIpNetToMediaNetAddress = _SonusIpNetToMediaNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 2, 2, 1, 3),
    _SonusIpNetToMediaNetAddress_Type()
)
sonusIpNetToMediaNetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusIpNetToMediaNetAddress.setStatus("current")


class _SonusIpNetToMediaType_Type(Integer32):
    """Custom type sonusIpNetToMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 3),
          ("invalid", 2),
          ("other", 1),
          ("static", 4))
    )


_SonusIpNetToMediaType_Type.__name__ = "Integer32"
_SonusIpNetToMediaType_Object = MibTableColumn
sonusIpNetToMediaType = _SonusIpNetToMediaType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 2, 2, 1, 4),
    _SonusIpNetToMediaType_Type()
)
sonusIpNetToMediaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusIpNetToMediaType.setStatus("current")
_SonusIpNetToMediaShelf_Type = Integer32
_SonusIpNetToMediaShelf_Object = MibTableColumn
sonusIpNetToMediaShelf = _SonusIpNetToMediaShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 2, 2, 1, 5),
    _SonusIpNetToMediaShelf_Type()
)
sonusIpNetToMediaShelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusIpNetToMediaShelf.setStatus("current")
_SonusIpNetToMediaSlot_Type = Integer32
_SonusIpNetToMediaSlot_Object = MibTableColumn
sonusIpNetToMediaSlot = _SonusIpNetToMediaSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 2, 2, 1, 6),
    _SonusIpNetToMediaSlot_Type()
)
sonusIpNetToMediaSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusIpNetToMediaSlot.setStatus("current")
_SonusIpNetToMediaInstance_Type = Integer32
_SonusIpNetToMediaInstance_Object = MibTableColumn
sonusIpNetToMediaInstance = _SonusIpNetToMediaInstance_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 2, 2, 1, 7),
    _SonusIpNetToMediaInstance_Type()
)
sonusIpNetToMediaInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusIpNetToMediaInstance.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-IP-ADDRESS-MIB",
    **{"sonusIpAddressMIB": sonusIpAddressMIB,
       "sonusIpAddrTable": sonusIpAddrTable,
       "sonusIpAddrEntry": sonusIpAddrEntry,
       "sonusIpAdEntAddr": sonusIpAdEntAddr,
       "sonusIpAdEntIfIndex": sonusIpAdEntIfIndex,
       "sonusIpAdEntNetMask": sonusIpAdEntNetMask,
       "sonusIpAdEntBcastAddr": sonusIpAdEntBcastAddr,
       "sonusIpAdEntReasmMaxSize": sonusIpAdEntReasmMaxSize,
       "sonusIpAdEntShelf": sonusIpAdEntShelf,
       "sonusIpAdEntSlot": sonusIpAdEntSlot,
       "sonusIpAdEntInstance": sonusIpAdEntInstance,
       "sonusIpNetToMediaTable": sonusIpNetToMediaTable,
       "sonusIpNetToMediaEntry": sonusIpNetToMediaEntry,
       "sonusIpNetToMediaIfIndex": sonusIpNetToMediaIfIndex,
       "sonusIpNetToMediaPhysAddress": sonusIpNetToMediaPhysAddress,
       "sonusIpNetToMediaNetAddress": sonusIpNetToMediaNetAddress,
       "sonusIpNetToMediaType": sonusIpNetToMediaType,
       "sonusIpNetToMediaShelf": sonusIpNetToMediaShelf,
       "sonusIpNetToMediaSlot": sonusIpNetToMediaSlot,
       "sonusIpNetToMediaInstance": sonusIpNetToMediaInstance}
)
