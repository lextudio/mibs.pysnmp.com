# SNMP MIB module (COMMUNITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COMMUNITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:45 2024
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

_Cabletron_ObjectIdentity = ObjectIdentity
cabletron = _Cabletron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52)
)
_CommsDevice_ObjectIdentity = ObjectIdentity
commsDevice = _CommsDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1)
)
_Community_ObjectIdentity = ObjectIdentity
community = _Community_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 52)
)
_CommunityTable_Object = MibTable
communityTable = _CommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 52, 2)
)
if mibBuilder.loadTexts:
    communityTable.setStatus("mandatory")
_CommunityEntry_Object = MibTableRow
communityEntry = _CommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 52, 2, 1)
)
communityEntry.setIndexNames(
    (0, "COMMUNITY-MIB", "communityIndex"),
)
if mibBuilder.loadTexts:
    communityEntry.setStatus("mandatory")


class _CommunityName_Type(OctetString):
    """Custom type communityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CommunityName_Type.__name__ = "OctetString"
_CommunityName_Object = MibTableColumn
communityName = _CommunityName_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 52, 2, 1, 1),
    _CommunityName_Type()
)
communityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    communityName.setStatus("mandatory")
_CommunityTrap_Type = Integer32
_CommunityTrap_Object = MibTableColumn
communityTrap = _CommunityTrap_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 52, 2, 1, 2),
    _CommunityTrap_Type()
)
communityTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    communityTrap.setStatus("mandatory")
_CommunityIPAddr_Type = IpAddress
_CommunityIPAddr_Object = MibTableColumn
communityIPAddr = _CommunityIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 52, 2, 1, 3),
    _CommunityIPAddr_Type()
)
communityIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    communityIPAddr.setStatus("mandatory")
_CommunityIndex_Type = Integer32
_CommunityIndex_Object = MibTableColumn
communityIndex = _CommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 52, 2, 1, 4),
    _CommunityIndex_Type()
)
communityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    communityIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COMMUNITY-MIB",
    **{"cabletron": cabletron,
       "commsDevice": commsDevice,
       "community": community,
       "communityTable": communityTable,
       "communityEntry": communityEntry,
       "communityName": communityName,
       "communityTrap": communityTrap,
       "communityIPAddr": communityIPAddr,
       "communityIndex": communityIndex}
)
