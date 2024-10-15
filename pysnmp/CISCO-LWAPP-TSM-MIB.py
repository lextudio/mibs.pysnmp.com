# SNMP MIB module (CISCO-LWAPP-TSM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-TSM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:04 2024
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

(cLApDot11IfSlotId,
 cLApSysMacAddress) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApDot11IfSlotId",
    "cLApSysMacAddress")

(CLTsmDot11CurrentPackets,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-TC-MIB",
    "CLTsmDot11CurrentPackets")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappTsmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 525)
)
ciscoLwappTsmMIB.setRevisions(
        ("2012-01-31 00:00",
         "2006-04-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappTsmMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappTsmMIBNotifs = _CiscoLwappTsmMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 0)
)
_CiscoLwappTsmMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappTsmMIBObjects = _CiscoLwappTsmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1)
)
_CiscoLwappTsmDot11Config_ObjectIdentity = ObjectIdentity
ciscoLwappTsmDot11Config = _CiscoLwappTsmDot11Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 1)
)


class _CLTsmDot11aConfig_Type(TruthValue):
    """Custom type cLTsmDot11aConfig based on TruthValue"""


_CLTsmDot11aConfig_Object = MibScalar
cLTsmDot11aConfig = _CLTsmDot11aConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 1, 1),
    _CLTsmDot11aConfig_Type()
)
cLTsmDot11aConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLTsmDot11aConfig.setStatus("current")


class _CLTsmDot11bgConfig_Type(TruthValue):
    """Custom type cLTsmDot11bgConfig based on TruthValue"""


_CLTsmDot11bgConfig_Object = MibScalar
cLTsmDot11bgConfig = _CLTsmDot11bgConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 1, 2),
    _CLTsmDot11bgConfig_Type()
)
cLTsmDot11bgConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLTsmDot11bgConfig.setStatus("current")


class _CLTsmDot11MaxClientsPerDot11Intf_Type(Unsigned32):
    """Custom type cLTsmDot11MaxClientsPerDot11Intf based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CLTsmDot11MaxClientsPerDot11Intf_Type.__name__ = "Unsigned32"
_CLTsmDot11MaxClientsPerDot11Intf_Object = MibScalar
cLTsmDot11MaxClientsPerDot11Intf = _CLTsmDot11MaxClientsPerDot11Intf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 1, 3),
    _CLTsmDot11MaxClientsPerDot11Intf_Type()
)
cLTsmDot11MaxClientsPerDot11Intf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLTsmDot11MaxClientsPerDot11Intf.setStatus("current")


class _CLTsmDot11MaxTsmStatsEntries_Type(Unsigned32):
    """Custom type cLTsmDot11MaxTsmStatsEntries based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_CLTsmDot11MaxTsmStatsEntries_Type.__name__ = "Unsigned32"
_CLTsmDot11MaxTsmStatsEntries_Object = MibScalar
cLTsmDot11MaxTsmStatsEntries = _CLTsmDot11MaxTsmStatsEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 1, 4),
    _CLTsmDot11MaxTsmStatsEntries_Type()
)
cLTsmDot11MaxTsmStatsEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLTsmDot11MaxTsmStatsEntries.setStatus("current")
_CiscoLwappTsmDot11Stats_ObjectIdentity = ObjectIdentity
ciscoLwappTsmDot11Stats = _CiscoLwappTsmDot11Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2)
)
_CLTsmDot11ClientTable_Object = MibTable
cLTsmDot11ClientTable = _CLTsmDot11ClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cLTsmDot11ClientTable.setStatus("current")
_CLTsmDot11ClientEntry_Object = MibTableRow
cLTsmDot11ClientEntry = _CLTsmDot11ClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 1, 1)
)
cLTsmDot11ClientEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
    (0, "CISCO-LWAPP-TSM-MIB", "cLTsmDot11ClientIndex"),
)
if mibBuilder.loadTexts:
    cLTsmDot11ClientEntry.setStatus("current")
_CLTsmDot11ClientIndex_Type = Unsigned32
_CLTsmDot11ClientIndex_Object = MibTableColumn
cLTsmDot11ClientIndex = _CLTsmDot11ClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 1, 1, 1),
    _CLTsmDot11ClientIndex_Type()
)
cLTsmDot11ClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLTsmDot11ClientIndex.setStatus("current")
_CLTsmDot11ClientMacAddress_Type = MacAddress
_CLTsmDot11ClientMacAddress_Object = MibTableColumn
cLTsmDot11ClientMacAddress = _CLTsmDot11ClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 1, 1, 2),
    _CLTsmDot11ClientMacAddress_Type()
)
cLTsmDot11ClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLTsmDot11ClientMacAddress.setStatus("current")
_CLTsmDot11UplinkTable_Object = MibTable
cLTsmDot11UplinkTable = _CLTsmDot11UplinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cLTsmDot11UplinkTable.setStatus("current")
_CLTsmDot11UplinkEntry_Object = MibTableRow
cLTsmDot11UplinkEntry = _CLTsmDot11UplinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 2, 1)
)
cLTsmDot11UplinkEntry.setIndexNames(
    (0, "CISCO-LWAPP-TSM-MIB", "cLTsmDot11ClientMacAddress"),
    (0, "CISCO-LWAPP-TSM-MIB", "cLTsmDot11UplinkApMacAddress"),
    (0, "CISCO-LWAPP-TSM-MIB", "cLTsmDot11UplinkApIfSlotId"),
    (0, "CISCO-LWAPP-TSM-MIB", "cLTsmDot11UplinkTimeStamp"),
)
if mibBuilder.loadTexts:
    cLTsmDot11UplinkEntry.setStatus("current")
_CLTsmDot11UplinkApMacAddress_Type = MacAddress
_CLTsmDot11UplinkApMacAddress_Object = MibTableColumn
cLTsmDot11UplinkApMacAddress = _CLTsmDot11UplinkApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 2, 1, 1),
    _CLTsmDot11UplinkApMacAddress_Type()
)
cLTsmDot11UplinkApMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLTsmDot11UplinkApMacAddress.setStatus("current")


class _CLTsmDot11UplinkApIfSlotId_Type(Unsigned32):
    """Custom type cLTsmDot11UplinkApIfSlotId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CLTsmDot11UplinkApIfSlotId_Type.__name__ = "Unsigned32"
_CLTsmDot11UplinkApIfSlotId_Object = MibTableColumn
cLTsmDot11UplinkApIfSlotId = _CLTsmDot11UplinkApIfSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 2, 1, 2),
    _CLTsmDot11UplinkApIfSlotId_Type()
)
cLTsmDot11UplinkApIfSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLTsmDot11UplinkApIfSlotId.setStatus("current")
_CLTsmDot11UplinkTimeStamp_Type = TimeStamp
_CLTsmDot11UplinkTimeStamp_Object = MibTableColumn
cLTsmDot11UplinkTimeStamp = _CLTsmDot11UplinkTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 2, 1, 3),
    _CLTsmDot11UplinkTimeStamp_Type()
)
cLTsmDot11UplinkTimeStamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLTsmDot11UplinkTimeStamp.setStatus("current")
_CLTsmDot11UplinkAvgPktQDelay_Type = TimeInterval
_CLTsmDot11UplinkAvgPktQDelay_Object = MibTableColumn
cLTsmDot11UplinkAvgPktQDelay = _CLTsmDot11UplinkAvgPktQDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 2, 1, 4),
    _CLTsmDot11UplinkAvgPktQDelay_Type()
)
cLTsmDot11UplinkAvgPktQDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLTsmDot11UplinkAvgPktQDelay.setStatus("current")
if mibBuilder.loadTexts:
    cLTsmDot11UplinkAvgPktQDelay.setUnits("hundredths-seconds")
_CLTsmDot11UplinkLt10Packets_Type = CLTsmDot11CurrentPackets
_CLTsmDot11UplinkLt10Packets_Object = MibTableColumn
cLTsmDot11UplinkLt10Packets = _CLTsmDot11UplinkLt10Packets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 2, 1, 5),
    _CLTsmDot11UplinkLt10Packets_Type()
)
cLTsmDot11UplinkLt10Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLTsmDot11UplinkLt10Packets.setStatus("current")
if mibBuilder.loadTexts:
    cLTsmDot11UplinkLt10Packets.setUnits("packets")
_CLTsmDot11UplinkPktGt10Lt20Packets_Type = CLTsmDot11CurrentPackets
_CLTsmDot11UplinkPktGt10Lt20Packets_Object = MibTableColumn
cLTsmDot11UplinkPktGt10Lt20Packets = _CLTsmDot11UplinkPktGt10Lt20Packets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 2, 1, 6),
    _CLTsmDot11UplinkPktGt10Lt20Packets_Type()
)
cLTsmDot11UplinkPktGt10Lt20Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLTsmDot11UplinkPktGt10Lt20Packets.setStatus("current")
if mibBuilder.loadTexts:
    cLTsmDot11UplinkPktGt10Lt20Packets.setUnits("packets")
_CLTsmDot11UplinkPktGt20Lt40Packets_Type = CLTsmDot11CurrentPackets
_CLTsmDot11UplinkPktGt20Lt40Packets_Object = MibTableColumn
cLTsmDot11UplinkPktGt20Lt40Packets = _CLTsmDot11UplinkPktGt20Lt40Packets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 2, 1, 7),
    _CLTsmDot11UplinkPktGt20Lt40Packets_Type()
)
cLTsmDot11UplinkPktGt20Lt40Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLTsmDot11UplinkPktGt20Lt40Packets.setStatus("current")
if mibBuilder.loadTexts:
    cLTsmDot11UplinkPktGt20Lt40Packets.setUnits("packets")
_CLTsmDot11UplinkPktGt40Packets_Type = CLTsmDot11CurrentPackets
_CLTsmDot11UplinkPktGt40Packets_Object = MibTableColumn
cLTsmDot11UplinkPktGt40Packets = _CLTsmDot11UplinkPktGt40Packets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 2, 1, 8),
    _CLTsmDot11UplinkPktGt40Packets_Type()
)
cLTsmDot11UplinkPktGt40Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLTsmDot11UplinkPktGt40Packets.setStatus("current")
if mibBuilder.loadTexts:
    cLTsmDot11UplinkPktGt40Packets.setUnits("packets")
_CLTsmDot11UplinkLostPackets_Type = CLTsmDot11CurrentPackets
_CLTsmDot11UplinkLostPackets_Object = MibTableColumn
cLTsmDot11UplinkLostPackets = _CLTsmDot11UplinkLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 2, 1, 9),
    _CLTsmDot11UplinkLostPackets_Type()
)
cLTsmDot11UplinkLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLTsmDot11UplinkLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    cLTsmDot11UplinkLostPackets.setUnits("packets")
_CLTsmDot11UplinkTotalPackets_Type = CLTsmDot11CurrentPackets
_CLTsmDot11UplinkTotalPackets_Object = MibTableColumn
cLTsmDot11UplinkTotalPackets = _CLTsmDot11UplinkTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 2, 1, 10),
    _CLTsmDot11UplinkTotalPackets_Type()
)
cLTsmDot11UplinkTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLTsmDot11UplinkTotalPackets.setStatus("current")
if mibBuilder.loadTexts:
    cLTsmDot11UplinkTotalPackets.setUnits("packets")
_CLTsmDot11UplinkRoamingPackets_Type = CLTsmDot11CurrentPackets
_CLTsmDot11UplinkRoamingPackets_Object = MibTableColumn
cLTsmDot11UplinkRoamingPackets = _CLTsmDot11UplinkRoamingPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 2, 1, 11),
    _CLTsmDot11UplinkRoamingPackets_Type()
)
cLTsmDot11UplinkRoamingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLTsmDot11UplinkRoamingPackets.setStatus("current")
if mibBuilder.loadTexts:
    cLTsmDot11UplinkRoamingPackets.setUnits("packets")
_CLTsmDot11UplinkRoamingDelay_Type = TimeInterval
_CLTsmDot11UplinkRoamingDelay_Object = MibTableColumn
cLTsmDot11UplinkRoamingDelay = _CLTsmDot11UplinkRoamingDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 2, 1, 12),
    _CLTsmDot11UplinkRoamingDelay_Type()
)
cLTsmDot11UplinkRoamingDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLTsmDot11UplinkRoamingDelay.setStatus("current")
if mibBuilder.loadTexts:
    cLTsmDot11UplinkRoamingDelay.setUnits("hundredths-seconds")
_CLTsmDot11DnlinkTable_Object = MibTable
cLTsmDot11DnlinkTable = _CLTsmDot11DnlinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cLTsmDot11DnlinkTable.setStatus("current")
_CLTsmDot11DnlinkEntry_Object = MibTableRow
cLTsmDot11DnlinkEntry = _CLTsmDot11DnlinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 3, 1)
)
cLTsmDot11DnlinkEntry.setIndexNames(
    (0, "CISCO-LWAPP-TSM-MIB", "cLTsmDot11ClientMacAddress"),
    (0, "CISCO-LWAPP-TSM-MIB", "cLTsmDot11DnlinkApMacAddress"),
    (0, "CISCO-LWAPP-TSM-MIB", "cLTsmDot11DnlinkApIfSlotId"),
    (0, "CISCO-LWAPP-TSM-MIB", "cLTsmDot11DnlinkTimeStamp"),
)
if mibBuilder.loadTexts:
    cLTsmDot11DnlinkEntry.setStatus("current")
_CLTsmDot11DnlinkApMacAddress_Type = MacAddress
_CLTsmDot11DnlinkApMacAddress_Object = MibTableColumn
cLTsmDot11DnlinkApMacAddress = _CLTsmDot11DnlinkApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 3, 1, 1),
    _CLTsmDot11DnlinkApMacAddress_Type()
)
cLTsmDot11DnlinkApMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLTsmDot11DnlinkApMacAddress.setStatus("current")


class _CLTsmDot11DnlinkApIfSlotId_Type(Unsigned32):
    """Custom type cLTsmDot11DnlinkApIfSlotId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CLTsmDot11DnlinkApIfSlotId_Type.__name__ = "Unsigned32"
_CLTsmDot11DnlinkApIfSlotId_Object = MibTableColumn
cLTsmDot11DnlinkApIfSlotId = _CLTsmDot11DnlinkApIfSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 3, 1, 2),
    _CLTsmDot11DnlinkApIfSlotId_Type()
)
cLTsmDot11DnlinkApIfSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLTsmDot11DnlinkApIfSlotId.setStatus("current")
_CLTsmDot11DnlinkTimeStamp_Type = TimeStamp
_CLTsmDot11DnlinkTimeStamp_Object = MibTableColumn
cLTsmDot11DnlinkTimeStamp = _CLTsmDot11DnlinkTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 3, 1, 3),
    _CLTsmDot11DnlinkTimeStamp_Type()
)
cLTsmDot11DnlinkTimeStamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLTsmDot11DnlinkTimeStamp.setStatus("current")
_CLTsmDot11DnlinkAvgPktQDelay_Type = TimeInterval
_CLTsmDot11DnlinkAvgPktQDelay_Object = MibTableColumn
cLTsmDot11DnlinkAvgPktQDelay = _CLTsmDot11DnlinkAvgPktQDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 3, 1, 4),
    _CLTsmDot11DnlinkAvgPktQDelay_Type()
)
cLTsmDot11DnlinkAvgPktQDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLTsmDot11DnlinkAvgPktQDelay.setStatus("current")
if mibBuilder.loadTexts:
    cLTsmDot11DnlinkAvgPktQDelay.setUnits("hundredths-seconds")
_CLTsmDot11DnlinkLt10Packets_Type = CLTsmDot11CurrentPackets
_CLTsmDot11DnlinkLt10Packets_Object = MibTableColumn
cLTsmDot11DnlinkLt10Packets = _CLTsmDot11DnlinkLt10Packets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 3, 1, 5),
    _CLTsmDot11DnlinkLt10Packets_Type()
)
cLTsmDot11DnlinkLt10Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLTsmDot11DnlinkLt10Packets.setStatus("current")
if mibBuilder.loadTexts:
    cLTsmDot11DnlinkLt10Packets.setUnits("packets")
_CLTsmDot11DnlinkPktGt10Lt20Packets_Type = CLTsmDot11CurrentPackets
_CLTsmDot11DnlinkPktGt10Lt20Packets_Object = MibTableColumn
cLTsmDot11DnlinkPktGt10Lt20Packets = _CLTsmDot11DnlinkPktGt10Lt20Packets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 3, 1, 6),
    _CLTsmDot11DnlinkPktGt10Lt20Packets_Type()
)
cLTsmDot11DnlinkPktGt10Lt20Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLTsmDot11DnlinkPktGt10Lt20Packets.setStatus("current")
if mibBuilder.loadTexts:
    cLTsmDot11DnlinkPktGt10Lt20Packets.setUnits("packets")
_CLTsmDot11DnlinkPktGt20Lt40Packets_Type = CLTsmDot11CurrentPackets
_CLTsmDot11DnlinkPktGt20Lt40Packets_Object = MibTableColumn
cLTsmDot11DnlinkPktGt20Lt40Packets = _CLTsmDot11DnlinkPktGt20Lt40Packets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 3, 1, 7),
    _CLTsmDot11DnlinkPktGt20Lt40Packets_Type()
)
cLTsmDot11DnlinkPktGt20Lt40Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLTsmDot11DnlinkPktGt20Lt40Packets.setStatus("current")
if mibBuilder.loadTexts:
    cLTsmDot11DnlinkPktGt20Lt40Packets.setUnits("packets")
_CLTsmDot11DnlinkPktGt40Packets_Type = CLTsmDot11CurrentPackets
_CLTsmDot11DnlinkPktGt40Packets_Object = MibTableColumn
cLTsmDot11DnlinkPktGt40Packets = _CLTsmDot11DnlinkPktGt40Packets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 3, 1, 8),
    _CLTsmDot11DnlinkPktGt40Packets_Type()
)
cLTsmDot11DnlinkPktGt40Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLTsmDot11DnlinkPktGt40Packets.setStatus("current")
if mibBuilder.loadTexts:
    cLTsmDot11DnlinkPktGt40Packets.setUnits("packets")
_CLTsmDot11DnlinkLostPackets_Type = CLTsmDot11CurrentPackets
_CLTsmDot11DnlinkLostPackets_Object = MibTableColumn
cLTsmDot11DnlinkLostPackets = _CLTsmDot11DnlinkLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 3, 1, 9),
    _CLTsmDot11DnlinkLostPackets_Type()
)
cLTsmDot11DnlinkLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLTsmDot11DnlinkLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    cLTsmDot11DnlinkLostPackets.setUnits("packets")
_CLTsmDot11DnlinkTotalPackets_Type = CLTsmDot11CurrentPackets
_CLTsmDot11DnlinkTotalPackets_Object = MibTableColumn
cLTsmDot11DnlinkTotalPackets = _CLTsmDot11DnlinkTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 3, 1, 10),
    _CLTsmDot11DnlinkTotalPackets_Type()
)
cLTsmDot11DnlinkTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLTsmDot11DnlinkTotalPackets.setStatus("current")
if mibBuilder.loadTexts:
    cLTsmDot11DnlinkTotalPackets.setUnits("packets")
_CLTsmDot11CUTable_Object = MibTable
cLTsmDot11CUTable = _CLTsmDot11CUTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cLTsmDot11CUTable.setStatus("current")
_CLTsmDot11CUEntry_Object = MibTableRow
cLTsmDot11CUEntry = _CLTsmDot11CUEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 4, 1)
)
cLTsmDot11CUEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
    (0, "CISCO-LWAPP-TSM-MIB", "cLTsmDot11CUTimeStamp"),
)
if mibBuilder.loadTexts:
    cLTsmDot11CUEntry.setStatus("current")
_CLTsmDot11CUTimeStamp_Type = TimeStamp
_CLTsmDot11CUTimeStamp_Object = MibTableColumn
cLTsmDot11CUTimeStamp = _CLTsmDot11CUTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 4, 1, 1),
    _CLTsmDot11CUTimeStamp_Type()
)
cLTsmDot11CUTimeStamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLTsmDot11CUTimeStamp.setStatus("current")


class _CLTsmDot11CUFiftyPercentilePicc_Type(Unsigned32):
    """Custom type cLTsmDot11CUFiftyPercentilePicc based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLTsmDot11CUFiftyPercentilePicc_Type.__name__ = "Unsigned32"
_CLTsmDot11CUFiftyPercentilePicc_Object = MibTableColumn
cLTsmDot11CUFiftyPercentilePicc = _CLTsmDot11CUFiftyPercentilePicc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 4, 1, 2),
    _CLTsmDot11CUFiftyPercentilePicc_Type()
)
cLTsmDot11CUFiftyPercentilePicc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLTsmDot11CUFiftyPercentilePicc.setStatus("current")
if mibBuilder.loadTexts:
    cLTsmDot11CUFiftyPercentilePicc.setUnits("percent")


class _CLTsmDot11CUNinetyPercentilePicc_Type(Unsigned32):
    """Custom type cLTsmDot11CUNinetyPercentilePicc based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLTsmDot11CUNinetyPercentilePicc_Type.__name__ = "Unsigned32"
_CLTsmDot11CUNinetyPercentilePicc_Object = MibTableColumn
cLTsmDot11CUNinetyPercentilePicc = _CLTsmDot11CUNinetyPercentilePicc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 4, 1, 3),
    _CLTsmDot11CUNinetyPercentilePicc_Type()
)
cLTsmDot11CUNinetyPercentilePicc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLTsmDot11CUNinetyPercentilePicc.setStatus("current")
if mibBuilder.loadTexts:
    cLTsmDot11CUNinetyPercentilePicc.setUnits("percent")


class _CLTsmDot11CUFiftyPercentilePib_Type(Unsigned32):
    """Custom type cLTsmDot11CUFiftyPercentilePib based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLTsmDot11CUFiftyPercentilePib_Type.__name__ = "Unsigned32"
_CLTsmDot11CUFiftyPercentilePib_Object = MibTableColumn
cLTsmDot11CUFiftyPercentilePib = _CLTsmDot11CUFiftyPercentilePib_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 4, 1, 4),
    _CLTsmDot11CUFiftyPercentilePib_Type()
)
cLTsmDot11CUFiftyPercentilePib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLTsmDot11CUFiftyPercentilePib.setStatus("current")
if mibBuilder.loadTexts:
    cLTsmDot11CUFiftyPercentilePib.setUnits("percent")


class _CLTsmDot11CUNinetyPercentilePib_Type(Unsigned32):
    """Custom type cLTsmDot11CUNinetyPercentilePib based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLTsmDot11CUNinetyPercentilePib_Type.__name__ = "Unsigned32"
_CLTsmDot11CUNinetyPercentilePib_Object = MibTableColumn
cLTsmDot11CUNinetyPercentilePib = _CLTsmDot11CUNinetyPercentilePib_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 1, 2, 4, 1, 5),
    _CLTsmDot11CUNinetyPercentilePib_Type()
)
cLTsmDot11CUNinetyPercentilePib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLTsmDot11CUNinetyPercentilePib.setStatus("current")
if mibBuilder.loadTexts:
    cLTsmDot11CUNinetyPercentilePib.setUnits("percent")
_CiscoLwappTsmMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappTsmMIBConform = _CiscoLwappTsmMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 2)
)
_CiscoLwappTsmMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappTsmMIBCompliances = _CiscoLwappTsmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 2, 1)
)
_CiscoLwappTsmMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappTsmMIBGroups = _CiscoLwappTsmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 2, 2)
)

# Managed Objects groups

ciscoLwappTsmDot11ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 2, 2, 1)
)
ciscoLwappTsmDot11ConfigGroup.setObjects(
      *(("CISCO-LWAPP-TSM-MIB", "cLTsmDot11aConfig"),
        ("CISCO-LWAPP-TSM-MIB", "cLTsmDot11bgConfig"),
        ("CISCO-LWAPP-TSM-MIB", "cLTsmDot11MaxClientsPerDot11Intf"),
        ("CISCO-LWAPP-TSM-MIB", "cLTsmDot11MaxTsmStatsEntries"))
)
if mibBuilder.loadTexts:
    ciscoLwappTsmDot11ConfigGroup.setStatus("current")

ciscoLwappTsmDot11StatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 2, 2, 2)
)
ciscoLwappTsmDot11StatsGroup.setObjects(
      *(("CISCO-LWAPP-TSM-MIB", "cLTsmDot11ClientMacAddress"),
        ("CISCO-LWAPP-TSM-MIB", "cLTsmDot11UplinkAvgPktQDelay"),
        ("CISCO-LWAPP-TSM-MIB", "cLTsmDot11UplinkLt10Packets"),
        ("CISCO-LWAPP-TSM-MIB", "cLTsmDot11UplinkPktGt10Lt20Packets"),
        ("CISCO-LWAPP-TSM-MIB", "cLTsmDot11UplinkPktGt20Lt40Packets"),
        ("CISCO-LWAPP-TSM-MIB", "cLTsmDot11UplinkPktGt40Packets"),
        ("CISCO-LWAPP-TSM-MIB", "cLTsmDot11UplinkLostPackets"),
        ("CISCO-LWAPP-TSM-MIB", "cLTsmDot11UplinkTotalPackets"),
        ("CISCO-LWAPP-TSM-MIB", "cLTsmDot11UplinkRoamingPackets"),
        ("CISCO-LWAPP-TSM-MIB", "cLTsmDot11UplinkRoamingDelay"),
        ("CISCO-LWAPP-TSM-MIB", "cLTsmDot11DnlinkAvgPktQDelay"),
        ("CISCO-LWAPP-TSM-MIB", "cLTsmDot11DnlinkLt10Packets"),
        ("CISCO-LWAPP-TSM-MIB", "cLTsmDot11DnlinkPktGt10Lt20Packets"),
        ("CISCO-LWAPP-TSM-MIB", "cLTsmDot11DnlinkPktGt20Lt40Packets"),
        ("CISCO-LWAPP-TSM-MIB", "cLTsmDot11DnlinkPktGt40Packets"),
        ("CISCO-LWAPP-TSM-MIB", "cLTsmDot11DnlinkLostPackets"),
        ("CISCO-LWAPP-TSM-MIB", "cLTsmDot11DnlinkTotalPackets"))
)
if mibBuilder.loadTexts:
    ciscoLwappTsmDot11StatsGroup.setStatus("current")

ciscoLwappTsmDot11StatsGroupSupR01 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 2, 2, 3)
)
ciscoLwappTsmDot11StatsGroupSupR01.setObjects(
      *(("CISCO-LWAPP-TSM-MIB", "cLTsmDot11CUFiftyPercentilePicc"),
        ("CISCO-LWAPP-TSM-MIB", "cLTsmDot11CUNinetyPercentilePicc"),
        ("CISCO-LWAPP-TSM-MIB", "cLTsmDot11CUFiftyPercentilePib"),
        ("CISCO-LWAPP-TSM-MIB", "cLTsmDot11CUNinetyPercentilePib"))
)
if mibBuilder.loadTexts:
    ciscoLwappTsmDot11StatsGroupSupR01.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappTsmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappTsmMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappTsmMIBComplianceRev01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 525, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappTsmMIBComplianceRev01.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-TSM-MIB",
    **{"ciscoLwappTsmMIB": ciscoLwappTsmMIB,
       "ciscoLwappTsmMIBNotifs": ciscoLwappTsmMIBNotifs,
       "ciscoLwappTsmMIBObjects": ciscoLwappTsmMIBObjects,
       "ciscoLwappTsmDot11Config": ciscoLwappTsmDot11Config,
       "cLTsmDot11aConfig": cLTsmDot11aConfig,
       "cLTsmDot11bgConfig": cLTsmDot11bgConfig,
       "cLTsmDot11MaxClientsPerDot11Intf": cLTsmDot11MaxClientsPerDot11Intf,
       "cLTsmDot11MaxTsmStatsEntries": cLTsmDot11MaxTsmStatsEntries,
       "ciscoLwappTsmDot11Stats": ciscoLwappTsmDot11Stats,
       "cLTsmDot11ClientTable": cLTsmDot11ClientTable,
       "cLTsmDot11ClientEntry": cLTsmDot11ClientEntry,
       "cLTsmDot11ClientIndex": cLTsmDot11ClientIndex,
       "cLTsmDot11ClientMacAddress": cLTsmDot11ClientMacAddress,
       "cLTsmDot11UplinkTable": cLTsmDot11UplinkTable,
       "cLTsmDot11UplinkEntry": cLTsmDot11UplinkEntry,
       "cLTsmDot11UplinkApMacAddress": cLTsmDot11UplinkApMacAddress,
       "cLTsmDot11UplinkApIfSlotId": cLTsmDot11UplinkApIfSlotId,
       "cLTsmDot11UplinkTimeStamp": cLTsmDot11UplinkTimeStamp,
       "cLTsmDot11UplinkAvgPktQDelay": cLTsmDot11UplinkAvgPktQDelay,
       "cLTsmDot11UplinkLt10Packets": cLTsmDot11UplinkLt10Packets,
       "cLTsmDot11UplinkPktGt10Lt20Packets": cLTsmDot11UplinkPktGt10Lt20Packets,
       "cLTsmDot11UplinkPktGt20Lt40Packets": cLTsmDot11UplinkPktGt20Lt40Packets,
       "cLTsmDot11UplinkPktGt40Packets": cLTsmDot11UplinkPktGt40Packets,
       "cLTsmDot11UplinkLostPackets": cLTsmDot11UplinkLostPackets,
       "cLTsmDot11UplinkTotalPackets": cLTsmDot11UplinkTotalPackets,
       "cLTsmDot11UplinkRoamingPackets": cLTsmDot11UplinkRoamingPackets,
       "cLTsmDot11UplinkRoamingDelay": cLTsmDot11UplinkRoamingDelay,
       "cLTsmDot11DnlinkTable": cLTsmDot11DnlinkTable,
       "cLTsmDot11DnlinkEntry": cLTsmDot11DnlinkEntry,
       "cLTsmDot11DnlinkApMacAddress": cLTsmDot11DnlinkApMacAddress,
       "cLTsmDot11DnlinkApIfSlotId": cLTsmDot11DnlinkApIfSlotId,
       "cLTsmDot11DnlinkTimeStamp": cLTsmDot11DnlinkTimeStamp,
       "cLTsmDot11DnlinkAvgPktQDelay": cLTsmDot11DnlinkAvgPktQDelay,
       "cLTsmDot11DnlinkLt10Packets": cLTsmDot11DnlinkLt10Packets,
       "cLTsmDot11DnlinkPktGt10Lt20Packets": cLTsmDot11DnlinkPktGt10Lt20Packets,
       "cLTsmDot11DnlinkPktGt20Lt40Packets": cLTsmDot11DnlinkPktGt20Lt40Packets,
       "cLTsmDot11DnlinkPktGt40Packets": cLTsmDot11DnlinkPktGt40Packets,
       "cLTsmDot11DnlinkLostPackets": cLTsmDot11DnlinkLostPackets,
       "cLTsmDot11DnlinkTotalPackets": cLTsmDot11DnlinkTotalPackets,
       "cLTsmDot11CUTable": cLTsmDot11CUTable,
       "cLTsmDot11CUEntry": cLTsmDot11CUEntry,
       "cLTsmDot11CUTimeStamp": cLTsmDot11CUTimeStamp,
       "cLTsmDot11CUFiftyPercentilePicc": cLTsmDot11CUFiftyPercentilePicc,
       "cLTsmDot11CUNinetyPercentilePicc": cLTsmDot11CUNinetyPercentilePicc,
       "cLTsmDot11CUFiftyPercentilePib": cLTsmDot11CUFiftyPercentilePib,
       "cLTsmDot11CUNinetyPercentilePib": cLTsmDot11CUNinetyPercentilePib,
       "ciscoLwappTsmMIBConform": ciscoLwappTsmMIBConform,
       "ciscoLwappTsmMIBCompliances": ciscoLwappTsmMIBCompliances,
       "ciscoLwappTsmMIBCompliance": ciscoLwappTsmMIBCompliance,
       "ciscoLwappTsmMIBComplianceRev01": ciscoLwappTsmMIBComplianceRev01,
       "ciscoLwappTsmMIBGroups": ciscoLwappTsmMIBGroups,
       "ciscoLwappTsmDot11ConfigGroup": ciscoLwappTsmDot11ConfigGroup,
       "ciscoLwappTsmDot11StatsGroup": ciscoLwappTsmDot11StatsGroup,
       "ciscoLwappTsmDot11StatsGroupSupR01": ciscoLwappTsmDot11StatsGroupSupR01}
)
