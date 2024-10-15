# SNMP MIB module (DEVNM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DEVNM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:10 2024
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

(device,) = mibBuilder.importSymbols(
    "ANIROOT-MIB",
    "device")

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

aniDevNetworkManager = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _AniDevNumManagingHosts_Type(Integer32):
    """Custom type aniDevNumManagingHosts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AniDevNumManagingHosts_Type.__name__ = "Integer32"
_AniDevNumManagingHosts_Object = MibScalar
aniDevNumManagingHosts = _AniDevNumManagingHosts_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 7, 1),
    _AniDevNumManagingHosts_Type()
)
aniDevNumManagingHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevNumManagingHosts.setStatus("current")
_AniDevNetworkMgrAccessTable_Object = MibTable
aniDevNetworkMgrAccessTable = _AniDevNetworkMgrAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 7, 2)
)
if mibBuilder.loadTexts:
    aniDevNetworkMgrAccessTable.setStatus("current")
_AniDevNetworkMgrAccessEntry_Object = MibTableRow
aniDevNetworkMgrAccessEntry = _AniDevNetworkMgrAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 7, 2, 1)
)
aniDevNetworkMgrAccessEntry.setIndexNames(
    (0, "DEVNM-MIB", "aniDevNMAccessIndex"),
)
if mibBuilder.loadTexts:
    aniDevNetworkMgrAccessEntry.setStatus("current")


class _AniDevNMAccessIndex_Type(Integer32):
    """Custom type aniDevNMAccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AniDevNMAccessIndex_Type.__name__ = "Integer32"
_AniDevNMAccessIndex_Object = MibTableColumn
aniDevNMAccessIndex = _AniDevNMAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 7, 2, 1, 1),
    _AniDevNMAccessIndex_Type()
)
aniDevNMAccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aniDevNMAccessIndex.setStatus("current")
_AniDevNMAccessIp_Type = IpAddress
_AniDevNMAccessIp_Object = MibTableColumn
aniDevNMAccessIp = _AniDevNMAccessIp_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 7, 2, 1, 2),
    _AniDevNMAccessIp_Type()
)
aniDevNMAccessIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevNMAccessIp.setStatus("current")


class _AniDevNMReadAccessCommunity_Type(DisplayString):
    """Custom type aniDevNMReadAccessCommunity based on DisplayString"""
    defaultValue = OctetString("public")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AniDevNMReadAccessCommunity_Type.__name__ = "DisplayString"
_AniDevNMReadAccessCommunity_Object = MibTableColumn
aniDevNMReadAccessCommunity = _AniDevNMReadAccessCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 7, 2, 1, 3),
    _AniDevNMReadAccessCommunity_Type()
)
aniDevNMReadAccessCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevNMReadAccessCommunity.setStatus("current")


class _AniDevNMWriteAccessCommunity_Type(DisplayString):
    """Custom type aniDevNMWriteAccessCommunity based on DisplayString"""
    defaultValue = OctetString("private")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AniDevNMWriteAccessCommunity_Type.__name__ = "DisplayString"
_AniDevNMWriteAccessCommunity_Object = MibTableColumn
aniDevNMWriteAccessCommunity = _AniDevNMWriteAccessCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 7, 2, 1, 4),
    _AniDevNMWriteAccessCommunity_Type()
)
aniDevNMWriteAccessCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevNMWriteAccessCommunity.setStatus("current")


class _AniDevNMAccessControl_Type(Integer32):
    """Custom type aniDevNMAccessControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("read", 1),
          ("readWrite", 2),
          ("roWithTraps", 3),
          ("rwWithTraps", 4),
          ("trapsOnly", 5))
    )


_AniDevNMAccessControl_Type.__name__ = "Integer32"
_AniDevNMAccessControl_Object = MibTableColumn
aniDevNMAccessControl = _AniDevNMAccessControl_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 7, 2, 1, 5),
    _AniDevNMAccessControl_Type()
)
aniDevNMAccessControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevNMAccessControl.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DEVNM-MIB",
    **{"aniDevNetworkManager": aniDevNetworkManager,
       "aniDevNumManagingHosts": aniDevNumManagingHosts,
       "aniDevNetworkMgrAccessTable": aniDevNetworkMgrAccessTable,
       "aniDevNetworkMgrAccessEntry": aniDevNetworkMgrAccessEntry,
       "aniDevNMAccessIndex": aniDevNMAccessIndex,
       "aniDevNMAccessIp": aniDevNMAccessIp,
       "aniDevNMReadAccessCommunity": aniDevNMReadAccessCommunity,
       "aniDevNMWriteAccessCommunity": aniDevNMWriteAccessCommunity,
       "aniDevNMAccessControl": aniDevNMAccessControl}
)
