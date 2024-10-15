# SNMP MIB module (RDN-CHANNEL-BONDING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RDN-CHANNEL-BONDING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:02 2024
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

(docsIfCmtsCmStatusIndex,) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "docsIfCmtsCmStatusIndex")

(ChSetId,
 IfDirection) = mibBuilder.importSymbols(
    "DOCS-IF3-MIB",
    "ChSetId",
    "IfDirection")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

(riverdelta,) = mibBuilder.importSymbols(
    "RDN-MIB",
    "riverdelta")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

rdnChannelBondingMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 9)
)
rdnChannelBondingMib.setRevisions(
        ("2011-07-20 00:00",
         "2011-05-17 00:00",
         "2011-05-02 00:00",
         "2008-08-08 00:00",
         "2007-02-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ChSetListStr(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 176),
    )



# MIB Managed Objects in the order of their OIDs

_RdnBondingGroupTable_Object = MibTable
rdnBondingGroupTable = _RdnBondingGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 9, 5)
)
if mibBuilder.loadTexts:
    rdnBondingGroupTable.setStatus("current")
_RdnBondingGroupEntry_Object = MibTableRow
rdnBondingGroupEntry = _RdnBondingGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 9, 5, 1)
)
rdnBondingGroupEntry.setIndexNames(
    (0, "RDN-CHANNEL-BONDING-MIB", "rdnBondingGroupMacIfIndex"),
    (0, "RDN-CHANNEL-BONDING-MIB", "rdnBondingGroupDir"),
    (0, "RDN-CHANNEL-BONDING-MIB", "rdnBondingGroupId"),
    (0, "RDN-CHANNEL-BONDING-MIB", "rdnBondingGroupChanIndex"),
)
if mibBuilder.loadTexts:
    rdnBondingGroupEntry.setStatus("current")
_RdnBondingGroupMacIfIndex_Type = Integer32
_RdnBondingGroupMacIfIndex_Object = MibTableColumn
rdnBondingGroupMacIfIndex = _RdnBondingGroupMacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 9, 5, 1, 1),
    _RdnBondingGroupMacIfIndex_Type()
)
rdnBondingGroupMacIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnBondingGroupMacIfIndex.setStatus("current")
_RdnBondingGroupDir_Type = IfDirection
_RdnBondingGroupDir_Object = MibTableColumn
rdnBondingGroupDir = _RdnBondingGroupDir_Object(
    (1, 3, 6, 1, 4, 1, 4981, 9, 5, 1, 2),
    _RdnBondingGroupDir_Type()
)
rdnBondingGroupDir.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnBondingGroupDir.setStatus("current")


class _RdnBondingGroupId_Type(Integer32):
    """Custom type rdnBondingGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RdnBondingGroupId_Type.__name__ = "Integer32"
_RdnBondingGroupId_Object = MibTableColumn
rdnBondingGroupId = _RdnBondingGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4981, 9, 5, 1, 3),
    _RdnBondingGroupId_Type()
)
rdnBondingGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnBondingGroupId.setStatus("current")


class _RdnBondingGroupChanIndex_Type(Integer32):
    """Custom type rdnBondingGroupChanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RdnBondingGroupChanIndex_Type.__name__ = "Integer32"
_RdnBondingGroupChanIndex_Object = MibTableColumn
rdnBondingGroupChanIndex = _RdnBondingGroupChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 9, 5, 1, 4),
    _RdnBondingGroupChanIndex_Type()
)
rdnBondingGroupChanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnBondingGroupChanIndex.setStatus("current")


class _RdnBondingGroupChanId_Type(Integer32):
    """Custom type rdnBondingGroupChanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RdnBondingGroupChanId_Type.__name__ = "Integer32"
_RdnBondingGroupChanId_Object = MibTableColumn
rdnBondingGroupChanId = _RdnBondingGroupChanId_Object(
    (1, 3, 6, 1, 4, 1, 4981, 9, 5, 1, 5),
    _RdnBondingGroupChanId_Type()
)
rdnBondingGroupChanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnBondingGroupChanId.setStatus("current")
_RdnBondingGroupStatsTable_Object = MibTable
rdnBondingGroupStatsTable = _RdnBondingGroupStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 9, 6)
)
if mibBuilder.loadTexts:
    rdnBondingGroupStatsTable.setStatus("current")
_RdnBondingGroupStatsEntry_Object = MibTableRow
rdnBondingGroupStatsEntry = _RdnBondingGroupStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 9, 6, 1)
)
rdnBondingGroupStatsEntry.setIndexNames(
    (0, "RDN-CHANNEL-BONDING-MIB", "rdnBondingGroupMacIfIndex"),
    (0, "RDN-CHANNEL-BONDING-MIB", "rdnBondingGroupDir"),
    (0, "RDN-CHANNEL-BONDING-MIB", "rdnBondingGroupId"),
    (0, "RDN-CHANNEL-BONDING-MIB", "rdnBondingGroupChanIndex"),
)
if mibBuilder.loadTexts:
    rdnBondingGroupStatsEntry.setStatus("current")


class _RdnBondingGroupStatsChanId_Type(Integer32):
    """Custom type rdnBondingGroupStatsChanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RdnBondingGroupStatsChanId_Type.__name__ = "Integer32"
_RdnBondingGroupStatsChanId_Object = MibTableColumn
rdnBondingGroupStatsChanId = _RdnBondingGroupStatsChanId_Object(
    (1, 3, 6, 1, 4, 1, 4981, 9, 6, 1, 1),
    _RdnBondingGroupStatsChanId_Type()
)
rdnBondingGroupStatsChanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnBondingGroupStatsChanId.setStatus("current")
_RdnBondingGroupStatsOctetCount_Type = Counter64
_RdnBondingGroupStatsOctetCount_Object = MibTableColumn
rdnBondingGroupStatsOctetCount = _RdnBondingGroupStatsOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 9, 6, 1, 2),
    _RdnBondingGroupStatsOctetCount_Type()
)
rdnBondingGroupStatsOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnBondingGroupStatsOctetCount.setStatus("current")
_RdnBondingGroupStatsPacketCount_Type = Counter64
_RdnBondingGroupStatsPacketCount_Object = MibTableColumn
rdnBondingGroupStatsPacketCount = _RdnBondingGroupStatsPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 9, 6, 1, 3),
    _RdnBondingGroupStatsPacketCount_Type()
)
rdnBondingGroupStatsPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnBondingGroupStatsPacketCount.setStatus("current")
_RdnBondingGroupCmTable_Object = MibTable
rdnBondingGroupCmTable = _RdnBondingGroupCmTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 9, 7)
)
if mibBuilder.loadTexts:
    rdnBondingGroupCmTable.setStatus("current")
_RdnBondingGroupCmEntry_Object = MibTableRow
rdnBondingGroupCmEntry = _RdnBondingGroupCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 9, 7, 1)
)
rdnBondingGroupCmEntry.setIndexNames(
    (0, "RDN-CHANNEL-BONDING-MIB", "rdnBondingGroupMacIfIndex"),
    (0, "RDN-CHANNEL-BONDING-MIB", "rdnBondingGroupDir"),
    (0, "RDN-CHANNEL-BONDING-MIB", "rdnBondingGroupId"),
)
if mibBuilder.loadTexts:
    rdnBondingGroupCmEntry.setStatus("current")
_RdnBondingGroupCmRegisteredModems_Type = Integer32
_RdnBondingGroupCmRegisteredModems_Object = MibTableColumn
rdnBondingGroupCmRegisteredModems = _RdnBondingGroupCmRegisteredModems_Object(
    (1, 3, 6, 1, 4, 1, 4981, 9, 7, 1, 1),
    _RdnBondingGroupCmRegisteredModems_Type()
)
rdnBondingGroupCmRegisteredModems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnBondingGroupCmRegisteredModems.setStatus("current")
_RdnCmtsCmPartialServiceTable_Object = MibTable
rdnCmtsCmPartialServiceTable = _RdnCmtsCmPartialServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 9, 8)
)
if mibBuilder.loadTexts:
    rdnCmtsCmPartialServiceTable.setStatus("current")
_RdnCmtsCmPartialServiceEntry_Object = MibTableRow
rdnCmtsCmPartialServiceEntry = _RdnCmtsCmPartialServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 9, 8, 1)
)
rdnCmtsCmPartialServiceEntry.setIndexNames(
    (0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"),
    (0, "RDN-CHANNEL-BONDING-MIB", "rdnCmtsCmPSDir"),
)
if mibBuilder.loadTexts:
    rdnCmtsCmPartialServiceEntry.setStatus("current")
_RdnCmtsCmPSDir_Type = IfDirection
_RdnCmtsCmPSDir_Object = MibTableColumn
rdnCmtsCmPSDir = _RdnCmtsCmPSDir_Object(
    (1, 3, 6, 1, 4, 1, 4981, 9, 8, 1, 1),
    _RdnCmtsCmPSDir_Type()
)
rdnCmtsCmPSDir.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnCmtsCmPSDir.setStatus("current")
_RdnCmtsCmPSMacDomainIfIndex_Type = InterfaceIndex
_RdnCmtsCmPSMacDomainIfIndex_Object = MibTableColumn
rdnCmtsCmPSMacDomainIfIndex = _RdnCmtsCmPSMacDomainIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 9, 8, 1, 2),
    _RdnCmtsCmPSMacDomainIfIndex_Type()
)
rdnCmtsCmPSMacDomainIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCmtsCmPSMacDomainIfIndex.setStatus("current")
_RdnCmtsCmPSMacAddress_Type = MacAddress
_RdnCmtsCmPSMacAddress_Object = MibTableColumn
rdnCmtsCmPSMacAddress = _RdnCmtsCmPSMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4981, 9, 8, 1, 3),
    _RdnCmtsCmPSMacAddress_Type()
)
rdnCmtsCmPSMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCmtsCmPSMacAddress.setStatus("current")
_RdnCmtsCmPSAssignedChSetId_Type = ChSetId
_RdnCmtsCmPSAssignedChSetId_Object = MibTableColumn
rdnCmtsCmPSAssignedChSetId = _RdnCmtsCmPSAssignedChSetId_Object(
    (1, 3, 6, 1, 4, 1, 4981, 9, 8, 1, 4),
    _RdnCmtsCmPSAssignedChSetId_Type()
)
rdnCmtsCmPSAssignedChSetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCmtsCmPSAssignedChSetId.setStatus("current")
_RdnCmtsCmPSActiveChSetId_Type = ChSetId
_RdnCmtsCmPSActiveChSetId_Object = MibTableColumn
rdnCmtsCmPSActiveChSetId = _RdnCmtsCmPSActiveChSetId_Object(
    (1, 3, 6, 1, 4, 1, 4981, 9, 8, 1, 5),
    _RdnCmtsCmPSActiveChSetId_Type()
)
rdnCmtsCmPSActiveChSetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCmtsCmPSActiveChSetId.setStatus("current")
_RdnCmtsCmPSAssignedChSetList_Type = ChSetListStr
_RdnCmtsCmPSAssignedChSetList_Object = MibTableColumn
rdnCmtsCmPSAssignedChSetList = _RdnCmtsCmPSAssignedChSetList_Object(
    (1, 3, 6, 1, 4, 1, 4981, 9, 8, 1, 6),
    _RdnCmtsCmPSAssignedChSetList_Type()
)
rdnCmtsCmPSAssignedChSetList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCmtsCmPSAssignedChSetList.setStatus("current")
_RdnCmtsCmPSNonActiveChList_Type = ChSetListStr
_RdnCmtsCmPSNonActiveChList_Object = MibTableColumn
rdnCmtsCmPSNonActiveChList = _RdnCmtsCmPSNonActiveChList_Object(
    (1, 3, 6, 1, 4, 1, 4981, 9, 8, 1, 7),
    _RdnCmtsCmPSNonActiveChList_Type()
)
rdnCmtsCmPSNonActiveChList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCmtsCmPSNonActiveChList.setStatus("current")
_RdnCmtsCmPSIpv4Addr_Type = IpAddress
_RdnCmtsCmPSIpv4Addr_Object = MibTableColumn
rdnCmtsCmPSIpv4Addr = _RdnCmtsCmPSIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 4981, 9, 8, 1, 8),
    _RdnCmtsCmPSIpv4Addr_Type()
)
rdnCmtsCmPSIpv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCmtsCmPSIpv4Addr.setStatus("current")
_RdnCmtsCmPSIpv6Addr_Type = InetAddressIPv6
_RdnCmtsCmPSIpv6Addr_Object = MibTableColumn
rdnCmtsCmPSIpv6Addr = _RdnCmtsCmPSIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 4981, 9, 8, 1, 9),
    _RdnCmtsCmPSIpv6Addr_Type()
)
rdnCmtsCmPSIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCmtsCmPSIpv6Addr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RDN-CHANNEL-BONDING-MIB",
    **{"ChSetListStr": ChSetListStr,
       "rdnChannelBondingMib": rdnChannelBondingMib,
       "rdnBondingGroupTable": rdnBondingGroupTable,
       "rdnBondingGroupEntry": rdnBondingGroupEntry,
       "rdnBondingGroupMacIfIndex": rdnBondingGroupMacIfIndex,
       "rdnBondingGroupDir": rdnBondingGroupDir,
       "rdnBondingGroupId": rdnBondingGroupId,
       "rdnBondingGroupChanIndex": rdnBondingGroupChanIndex,
       "rdnBondingGroupChanId": rdnBondingGroupChanId,
       "rdnBondingGroupStatsTable": rdnBondingGroupStatsTable,
       "rdnBondingGroupStatsEntry": rdnBondingGroupStatsEntry,
       "rdnBondingGroupStatsChanId": rdnBondingGroupStatsChanId,
       "rdnBondingGroupStatsOctetCount": rdnBondingGroupStatsOctetCount,
       "rdnBondingGroupStatsPacketCount": rdnBondingGroupStatsPacketCount,
       "rdnBondingGroupCmTable": rdnBondingGroupCmTable,
       "rdnBondingGroupCmEntry": rdnBondingGroupCmEntry,
       "rdnBondingGroupCmRegisteredModems": rdnBondingGroupCmRegisteredModems,
       "rdnCmtsCmPartialServiceTable": rdnCmtsCmPartialServiceTable,
       "rdnCmtsCmPartialServiceEntry": rdnCmtsCmPartialServiceEntry,
       "rdnCmtsCmPSDir": rdnCmtsCmPSDir,
       "rdnCmtsCmPSMacDomainIfIndex": rdnCmtsCmPSMacDomainIfIndex,
       "rdnCmtsCmPSMacAddress": rdnCmtsCmPSMacAddress,
       "rdnCmtsCmPSAssignedChSetId": rdnCmtsCmPSAssignedChSetId,
       "rdnCmtsCmPSActiveChSetId": rdnCmtsCmPSActiveChSetId,
       "rdnCmtsCmPSAssignedChSetList": rdnCmtsCmPSAssignedChSetList,
       "rdnCmtsCmPSNonActiveChList": rdnCmtsCmPSNonActiveChList,
       "rdnCmtsCmPSIpv4Addr": rdnCmtsCmPSIpv4Addr,
       "rdnCmtsCmPSIpv6Addr": rdnCmtsCmPSIpv6Addr}
)
