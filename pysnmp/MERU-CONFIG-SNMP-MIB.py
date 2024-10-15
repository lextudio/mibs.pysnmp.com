# SNMP MIB module (MERU-CONFIG-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MERU-CONFIG-SNMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:08 2024
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(mwConfiguration,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "mwConfiguration")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mwConfigSnmp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwWncTrapCommunityTable_Object = MibTable
mwWncTrapCommunityTable = _MwWncTrapCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12, 2)
)
if mibBuilder.loadTexts:
    mwWncTrapCommunityTable.setStatus("current")
_MwWncTrapCommunityEntry_Object = MibTableRow
mwWncTrapCommunityEntry = _MwWncTrapCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12, 2, 1)
)
mwWncTrapCommunityEntry.setIndexNames(
    (0, "MERU-CONFIG-SNMP-MIB", "mwWncTrapCommunityTableIndex"),
)
if mibBuilder.loadTexts:
    mwWncTrapCommunityEntry.setStatus("current")
_MwWncTrapCommunityTableIndex_Type = Integer32
_MwWncTrapCommunityTableIndex_Object = MibTableColumn
mwWncTrapCommunityTableIndex = _MwWncTrapCommunityTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12, 2, 1, 1),
    _MwWncTrapCommunityTableIndex_Type()
)
mwWncTrapCommunityTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwWncTrapCommunityTableIndex.setStatus("current")


class _MwWncTrapCommunitypCommunityStr_Type(DisplayString):
    """Custom type mwWncTrapCommunitypCommunityStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MwWncTrapCommunitypCommunityStr_Type.__name__ = "DisplayString"
_MwWncTrapCommunitypCommunityStr_Object = MibTableColumn
mwWncTrapCommunitypCommunityStr = _MwWncTrapCommunitypCommunityStr_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12, 2, 1, 2),
    _MwWncTrapCommunitypCommunityStr_Type()
)
mwWncTrapCommunitypCommunityStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwWncTrapCommunitypCommunityStr.setStatus("current")
_MwWncTrapCommunityClientIpAddress_Type = IpAddress
_MwWncTrapCommunityClientIpAddress_Object = MibTableColumn
mwWncTrapCommunityClientIpAddress = _MwWncTrapCommunityClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12, 2, 1, 3),
    _MwWncTrapCommunityClientIpAddress_Type()
)
mwWncTrapCommunityClientIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwWncTrapCommunityClientIpAddress.setStatus("current")
_MwWncTrapCommunityRowStatus_Type = RowStatus
_MwWncTrapCommunityRowStatus_Object = MibTableColumn
mwWncTrapCommunityRowStatus = _MwWncTrapCommunityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12, 2, 1, 4),
    _MwWncTrapCommunityRowStatus_Type()
)
mwWncTrapCommunityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwWncTrapCommunityRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-CONFIG-SNMP-MIB",
    **{"mwConfigSnmp": mwConfigSnmp,
       "mwWncTrapCommunityTable": mwWncTrapCommunityTable,
       "mwWncTrapCommunityEntry": mwWncTrapCommunityEntry,
       "mwWncTrapCommunityTableIndex": mwWncTrapCommunityTableIndex,
       "mwWncTrapCommunitypCommunityStr": mwWncTrapCommunitypCommunityStr,
       "mwWncTrapCommunityClientIpAddress": mwWncTrapCommunityClientIpAddress,
       "mwWncTrapCommunityRowStatus": mwWncTrapCommunityRowStatus}
)
