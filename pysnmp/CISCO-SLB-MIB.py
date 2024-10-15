# SNMP MIB module (CISCO-SLB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SLB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:26 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoIpProtocol,
 CiscoPort) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoIpProtocol",
    "CiscoPort")

(entPhysicalParentRelPos,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalParentRelPos")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

ciscoSlbMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 161)
)
ciscoSlbMIB.setRevisions(
        ("2008-05-15 00:00",
         "2008-04-15 00:00",
         "2008-02-12 00:00",
         "2007-06-20 00:00",
         "2007-04-20 00:00",
         "2006-10-26 00:00",
         "2006-01-13 00:00",
         "2005-03-31 00:00",
         "2002-03-18 00:00",
         "2002-01-15 15:00",
         "2000-10-20 00:00",
         "2000-05-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SlbServerString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 96),
    )



class SlbPasswordString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class SlbConnectionState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("closing", 8),
          ("conclient", 10),
          ("conserver", 11),
          ("estab", 5),
          ("finClient", 6),
          ("finServer", 7),
          ("init", 1),
          ("synBoth", 4),
          ("synClient", 2),
          ("synServer", 3),
          ("zombie", 9))
    )



class SlbPredictor(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("forward", 7),
          ("httpContentHash", 14),
          ("httpCookieHash", 9),
          ("httpHeaderHash", 10),
          ("ipHash", 3),
          ("ipHashDest", 5),
          ("ipHashSrc", 4),
          ("layer4PayloadHash", 11),
          ("leastBandwidth", 13),
          ("leastConns", 2),
          ("leastLoaded", 8),
          ("responseTime", 12),
          ("roundRobin", 1),
          ("urlHash", 6))
    )



class SlbRealServerState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("arpFailed", 15),
          ("dfpThrottle", 8),
          ("failed", 3),
          ("inService", 2),
          ("inactive", 17),
          ("inbandProbeFailed", 13),
          ("maxClientsThrottle", 7),
          ("maxConnsThrottle", 6),
          ("maxLoad", 18),
          ("operWait", 11),
          ("outOfService", 1),
          ("probeFailed", 9),
          ("probeTesting", 10),
          ("readyToTest", 4),
          ("returnCodeFailed", 14),
          ("standby", 16),
          ("testWait", 12),
          ("testing", 5))
    )



class SlbVirtualServState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("inOperReal", 4),
          ("inService", 2),
          ("outOfMemory", 7),
          ("outOfService", 1),
          ("standby", 3),
          ("stbInOperReal", 5),
          ("testReal", 6))
    )



class SlbVirtualService(Integer32, TextualConvention):
    status = "current"
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
        *(("ftp", 2),
          ("gtp", 4),
          ("none", 1),
          ("rtsp", 5),
          ("wsp", 3))
    )



class SlbDfpAgentState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("connecting", 3),
          ("failed", 5),
          ("notOpen", 1),
          ("open", 4),
          ("securityError", 6),
          ("trying", 2))
    )



class SlbSaspLBHealth(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("healthy", 10),
          ("heavyLoad", 7),
          ("idle", 2),
          ("lightLoad", 9),
          ("moderateLoad", 8),
          ("msgLimitReached", 6),
          ("other", 1),
          ("overUsed", 5),
          ("saturated", 4))
    )



class SlbSaspRedundancy(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 3),
          ("master", 2),
          ("other", 1))
    )



class SlbSaspAgentState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("closed", 3),
          ("connecting", 5),
          ("down", 9),
          ("downDuplicate", 8),
          ("downTrying", 7),
          ("established", 6),
          ("initialized", 2),
          ("other", 1),
          ("trying", 4))
    )



class SlbNatSetting(Integer32, TextualConvention):
    status = "current"
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
        *(("clientAndServerNat", 4),
          ("clientNat", 2),
          ("noNat", 1),
          ("serverNat", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSlbMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSlbMIBObjects = _CiscoSlbMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1)
)
_SlbStats_ObjectIdentity = ObjectIdentity
slbStats = _SlbStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 1)
)
_SlbStatsTable_Object = MibTable
slbStatsTable = _SlbStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 1, 1)
)
if mibBuilder.loadTexts:
    slbStatsTable.setStatus("current")
_SlbStatsTableEntry_Object = MibTableRow
slbStatsTableEntry = _SlbStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 1, 1, 1)
)
slbStatsTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
)
if mibBuilder.loadTexts:
    slbStatsTableEntry.setStatus("current")
_SlbEntity_Type = Unsigned32
_SlbEntity_Object = MibTableColumn
slbEntity = _SlbEntity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 1, 1, 1, 1),
    _SlbEntity_Type()
)
slbEntity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbEntity.setStatus("current")
_SlbStatsUnassistedSwitchingPkts_Type = Counter32
_SlbStatsUnassistedSwitchingPkts_Object = MibTableColumn
slbStatsUnassistedSwitchingPkts = _SlbStatsUnassistedSwitchingPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 1, 1, 1, 2),
    _SlbStatsUnassistedSwitchingPkts_Type()
)
slbStatsUnassistedSwitchingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsUnassistedSwitchingPkts.setStatus("current")
if mibBuilder.loadTexts:
    slbStatsUnassistedSwitchingPkts.setUnits("packets")
_SlbStatsUnassistedSwitchingHCPks_Type = Counter64
_SlbStatsUnassistedSwitchingHCPks_Object = MibTableColumn
slbStatsUnassistedSwitchingHCPks = _SlbStatsUnassistedSwitchingHCPks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 1, 1, 1, 3),
    _SlbStatsUnassistedSwitchingHCPks_Type()
)
slbStatsUnassistedSwitchingHCPks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsUnassistedSwitchingHCPks.setStatus("current")
if mibBuilder.loadTexts:
    slbStatsUnassistedSwitchingHCPks.setUnits("packets")
_SlbStatsAssistedSwitchingPkts_Type = Counter32
_SlbStatsAssistedSwitchingPkts_Object = MibTableColumn
slbStatsAssistedSwitchingPkts = _SlbStatsAssistedSwitchingPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 1, 1, 1, 4),
    _SlbStatsAssistedSwitchingPkts_Type()
)
slbStatsAssistedSwitchingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsAssistedSwitchingPkts.setStatus("current")
if mibBuilder.loadTexts:
    slbStatsAssistedSwitchingPkts.setUnits("packets")
_SlbStatsAssistedSwitchingHCPkts_Type = Counter64
_SlbStatsAssistedSwitchingHCPkts_Object = MibTableColumn
slbStatsAssistedSwitchingHCPkts = _SlbStatsAssistedSwitchingHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 1, 1, 1, 5),
    _SlbStatsAssistedSwitchingHCPkts_Type()
)
slbStatsAssistedSwitchingHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsAssistedSwitchingHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    slbStatsAssistedSwitchingHCPkts.setUnits("packets")
_SlbStatsCreatedConnections_Type = Counter32
_SlbStatsCreatedConnections_Object = MibTableColumn
slbStatsCreatedConnections = _SlbStatsCreatedConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 1, 1, 1, 6),
    _SlbStatsCreatedConnections_Type()
)
slbStatsCreatedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsCreatedConnections.setStatus("current")
if mibBuilder.loadTexts:
    slbStatsCreatedConnections.setUnits("connections")
_SlbStatsCreatedHCConnections_Type = Counter64
_SlbStatsCreatedHCConnections_Object = MibTableColumn
slbStatsCreatedHCConnections = _SlbStatsCreatedHCConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 1, 1, 1, 7),
    _SlbStatsCreatedHCConnections_Type()
)
slbStatsCreatedHCConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsCreatedHCConnections.setStatus("current")
if mibBuilder.loadTexts:
    slbStatsCreatedHCConnections.setUnits("connections")
_SlbStatsEstablishedConnections_Type = Counter32
_SlbStatsEstablishedConnections_Object = MibTableColumn
slbStatsEstablishedConnections = _SlbStatsEstablishedConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 1, 1, 1, 8),
    _SlbStatsEstablishedConnections_Type()
)
slbStatsEstablishedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsEstablishedConnections.setStatus("current")
if mibBuilder.loadTexts:
    slbStatsEstablishedConnections.setUnits("connections")
_SlbStatsEstablishedHCConnections_Type = Counter64
_SlbStatsEstablishedHCConnections_Object = MibTableColumn
slbStatsEstablishedHCConnections = _SlbStatsEstablishedHCConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 1, 1, 1, 9),
    _SlbStatsEstablishedHCConnections_Type()
)
slbStatsEstablishedHCConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsEstablishedHCConnections.setStatus("current")
if mibBuilder.loadTexts:
    slbStatsEstablishedHCConnections.setUnits("connections")
_SlbStatsDestroyedConnections_Type = Counter32
_SlbStatsDestroyedConnections_Object = MibTableColumn
slbStatsDestroyedConnections = _SlbStatsDestroyedConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 1, 1, 1, 10),
    _SlbStatsDestroyedConnections_Type()
)
slbStatsDestroyedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsDestroyedConnections.setStatus("current")
if mibBuilder.loadTexts:
    slbStatsDestroyedConnections.setUnits("connections")
_SlbStatsDestroyedHCConnections_Type = Counter64
_SlbStatsDestroyedHCConnections_Object = MibTableColumn
slbStatsDestroyedHCConnections = _SlbStatsDestroyedHCConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 1, 1, 1, 11),
    _SlbStatsDestroyedHCConnections_Type()
)
slbStatsDestroyedHCConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsDestroyedHCConnections.setStatus("current")
if mibBuilder.loadTexts:
    slbStatsDestroyedHCConnections.setUnits("connections")
_SlbStatsReassignedConnections_Type = Counter32
_SlbStatsReassignedConnections_Object = MibTableColumn
slbStatsReassignedConnections = _SlbStatsReassignedConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 1, 1, 1, 12),
    _SlbStatsReassignedConnections_Type()
)
slbStatsReassignedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsReassignedConnections.setStatus("current")
if mibBuilder.loadTexts:
    slbStatsReassignedConnections.setUnits("connections")
_SlbStatsReassignedHCConnections_Type = Counter64
_SlbStatsReassignedHCConnections_Object = MibTableColumn
slbStatsReassignedHCConnections = _SlbStatsReassignedHCConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 1, 1, 1, 13),
    _SlbStatsReassignedHCConnections_Type()
)
slbStatsReassignedHCConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsReassignedHCConnections.setStatus("current")
if mibBuilder.loadTexts:
    slbStatsReassignedHCConnections.setUnits("connections")
_SlbStatsZombies_Type = Counter32
_SlbStatsZombies_Object = MibTableColumn
slbStatsZombies = _SlbStatsZombies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 1, 1, 1, 14),
    _SlbStatsZombies_Type()
)
slbStatsZombies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsZombies.setStatus("current")
if mibBuilder.loadTexts:
    slbStatsZombies.setUnits("zombies")
_SlbStatsHCZombies_Type = Counter64
_SlbStatsHCZombies_Object = MibTableColumn
slbStatsHCZombies = _SlbStatsHCZombies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 1, 1, 1, 15),
    _SlbStatsHCZombies_Type()
)
slbStatsHCZombies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsHCZombies.setStatus("current")
if mibBuilder.loadTexts:
    slbStatsHCZombies.setUnits("zombies")
_SlbServerFarms_ObjectIdentity = ObjectIdentity
slbServerFarms = _SlbServerFarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 2)
)
_SlbServerFarmTable_Object = MibTable
slbServerFarmTable = _SlbServerFarmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 2, 1)
)
if mibBuilder.loadTexts:
    slbServerFarmTable.setStatus("current")
_SlbServerFarmTableEntry_Object = MibTableRow
slbServerFarmTableEntry = _SlbServerFarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 2, 1, 1)
)
slbServerFarmTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-MIB", "slbServerFarmName"),
)
if mibBuilder.loadTexts:
    slbServerFarmTableEntry.setStatus("current")
_SlbServerFarmName_Type = SlbServerString
_SlbServerFarmName_Object = MibTableColumn
slbServerFarmName = _SlbServerFarmName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 2, 1, 1, 1),
    _SlbServerFarmName_Type()
)
slbServerFarmName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbServerFarmName.setStatus("current")


class _SlbServerFarmPredictor_Type(SlbPredictor):
    """Custom type slbServerFarmPredictor based on SlbPredictor"""


_SlbServerFarmPredictor_Object = MibTableColumn
slbServerFarmPredictor = _SlbServerFarmPredictor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 2, 1, 1, 2),
    _SlbServerFarmPredictor_Type()
)
slbServerFarmPredictor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbServerFarmPredictor.setStatus("current")


class _SlbServerFarmNat_Type(SlbNatSetting):
    """Custom type slbServerFarmNat based on SlbNatSetting"""


_SlbServerFarmNat_Object = MibTableColumn
slbServerFarmNat = _SlbServerFarmNat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 2, 1, 1, 3),
    _SlbServerFarmNat_Type()
)
slbServerFarmNat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbServerFarmNat.setStatus("current")


class _SlbServerFarmNumberOfRealServers_Type(Unsigned32):
    """Custom type slbServerFarmNumberOfRealServers based on Unsigned32"""
    defaultValue = 0


_SlbServerFarmNumberOfRealServers_Object = MibTableColumn
slbServerFarmNumberOfRealServers = _SlbServerFarmNumberOfRealServers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 2, 1, 1, 4),
    _SlbServerFarmNumberOfRealServers_Type()
)
slbServerFarmNumberOfRealServers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbServerFarmNumberOfRealServers.setStatus("current")


class _SlbServerFarmBindId_Type(Unsigned32):
    """Custom type slbServerFarmBindId based on Unsigned32"""
    defaultValue = 0


_SlbServerFarmBindId_Object = MibTableColumn
slbServerFarmBindId = _SlbServerFarmBindId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 2, 1, 1, 5),
    _SlbServerFarmBindId_Type()
)
slbServerFarmBindId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbServerFarmBindId.setStatus("current")
_SlbServerFarmRowStatus_Type = RowStatus
_SlbServerFarmRowStatus_Object = MibTableColumn
slbServerFarmRowStatus = _SlbServerFarmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 2, 1, 1, 6),
    _SlbServerFarmRowStatus_Type()
)
slbServerFarmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbServerFarmRowStatus.setStatus("current")
_SlbRealServers_ObjectIdentity = ObjectIdentity
slbRealServers = _SlbRealServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 3)
)
_SlbRealTable_Object = MibTable
slbRealTable = _SlbRealTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 3, 1)
)
if mibBuilder.loadTexts:
    slbRealTable.setStatus("current")
_SlbRealTableEntry_Object = MibTableRow
slbRealTableEntry = _SlbRealTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 3, 1, 1)
)
slbRealTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-MIB", "slbRealServerFarmName"),
    (0, "CISCO-SLB-MIB", "slbRealIpAddress"),
    (0, "CISCO-SLB-MIB", "slbRealPort"),
)
if mibBuilder.loadTexts:
    slbRealTableEntry.setStatus("current")
_SlbRealServerFarmName_Type = SlbServerString
_SlbRealServerFarmName_Object = MibTableColumn
slbRealServerFarmName = _SlbRealServerFarmName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 3, 1, 1, 1),
    _SlbRealServerFarmName_Type()
)
slbRealServerFarmName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbRealServerFarmName.setStatus("current")
_SlbRealIpAddress_Type = IpAddress
_SlbRealIpAddress_Object = MibTableColumn
slbRealIpAddress = _SlbRealIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 3, 1, 1, 2),
    _SlbRealIpAddress_Type()
)
slbRealIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbRealIpAddress.setStatus("current")
_SlbRealPort_Type = CiscoPort
_SlbRealPort_Object = MibTableColumn
slbRealPort = _SlbRealPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 3, 1, 1, 3),
    _SlbRealPort_Type()
)
slbRealPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbRealPort.setStatus("current")


class _SlbRealState_Type(SlbRealServerState):
    """Custom type slbRealState based on SlbRealServerState"""


_SlbRealState_Object = MibTableColumn
slbRealState = _SlbRealState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 3, 1, 1, 4),
    _SlbRealState_Type()
)
slbRealState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbRealState.setStatus("current")
_SlbRealNumberOfConnections_Type = Gauge32
_SlbRealNumberOfConnections_Object = MibTableColumn
slbRealNumberOfConnections = _SlbRealNumberOfConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 3, 1, 1, 5),
    _SlbRealNumberOfConnections_Type()
)
slbRealNumberOfConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealNumberOfConnections.setStatus("current")
_SlbRealNumberOfDummyConnections_Type = Unsigned32
_SlbRealNumberOfDummyConnections_Object = MibTableColumn
slbRealNumberOfDummyConnections = _SlbRealNumberOfDummyConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 3, 1, 1, 6),
    _SlbRealNumberOfDummyConnections_Type()
)
slbRealNumberOfDummyConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealNumberOfDummyConnections.setStatus("current")


class _SlbRealMaxConnections_Type(Unsigned32):
    """Custom type slbRealMaxConnections based on Unsigned32"""
    defaultValue = 4294967295


_SlbRealMaxConnections_Object = MibTableColumn
slbRealMaxConnections = _SlbRealMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 3, 1, 1, 7),
    _SlbRealMaxConnections_Type()
)
slbRealMaxConnections.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbRealMaxConnections.setStatus("current")


class _SlbRealAdminWeight_Type(Unsigned32):
    """Custom type slbRealAdminWeight based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlbRealAdminWeight_Type.__name__ = "Unsigned32"
_SlbRealAdminWeight_Object = MibTableColumn
slbRealAdminWeight = _SlbRealAdminWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 3, 1, 1, 8),
    _SlbRealAdminWeight_Type()
)
slbRealAdminWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbRealAdminWeight.setStatus("current")
_SlbRealOperWeight_Type = Gauge32
_SlbRealOperWeight_Object = MibTableColumn
slbRealOperWeight = _SlbRealOperWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 3, 1, 1, 9),
    _SlbRealOperWeight_Type()
)
slbRealOperWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealOperWeight.setStatus("current")
_SlbRealMetric_Type = Gauge32
_SlbRealMetric_Object = MibTableColumn
slbRealMetric = _SlbRealMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 3, 1, 1, 10),
    _SlbRealMetric_Type()
)
slbRealMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealMetric.setStatus("current")


class _SlbRealReassign_Type(Unsigned32):
    """Custom type slbRealReassign based on Unsigned32"""
    defaultValue = 3


_SlbRealReassign_Object = MibTableColumn
slbRealReassign = _SlbRealReassign_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 3, 1, 1, 11),
    _SlbRealReassign_Type()
)
slbRealReassign.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbRealReassign.setStatus("current")


class _SlbRealRetryInterval_Type(TimeInterval):
    """Custom type slbRealRetryInterval based on TimeInterval"""
    defaultValue = 60


_SlbRealRetryInterval_Object = MibTableColumn
slbRealRetryInterval = _SlbRealRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 3, 1, 1, 12),
    _SlbRealRetryInterval_Type()
)
slbRealRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbRealRetryInterval.setStatus("current")


class _SlbRealFailedConnections_Type(Unsigned32):
    """Custom type slbRealFailedConnections based on Unsigned32"""
    defaultValue = 8


_SlbRealFailedConnections_Object = MibTableColumn
slbRealFailedConnections = _SlbRealFailedConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 3, 1, 1, 13),
    _SlbRealFailedConnections_Type()
)
slbRealFailedConnections.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbRealFailedConnections.setStatus("current")


class _SlbRealFailedClients_Type(Unsigned32):
    """Custom type slbRealFailedClients based on Unsigned32"""
    defaultValue = 8


_SlbRealFailedClients_Object = MibTableColumn
slbRealFailedClients = _SlbRealFailedClients_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 3, 1, 1, 14),
    _SlbRealFailedClients_Type()
)
slbRealFailedClients.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbRealFailedClients.setStatus("current")
_SlbRealConsecutiveFails_Type = Gauge32
_SlbRealConsecutiveFails_Object = MibTableColumn
slbRealConsecutiveFails = _SlbRealConsecutiveFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 3, 1, 1, 15),
    _SlbRealConsecutiveFails_Type()
)
slbRealConsecutiveFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealConsecutiveFails.setStatus("current")
_SlbRealTotalFails_Type = Counter32
_SlbRealTotalFails_Object = MibTableColumn
slbRealTotalFails = _SlbRealTotalFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 3, 1, 1, 16),
    _SlbRealTotalFails_Type()
)
slbRealTotalFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealTotalFails.setStatus("current")
_SlbRealRowStatus_Type = RowStatus
_SlbRealRowStatus_Object = MibTableColumn
slbRealRowStatus = _SlbRealRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 3, 1, 1, 17),
    _SlbRealRowStatus_Type()
)
slbRealRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbRealRowStatus.setStatus("current")
_SlbRealTotalConnections_Type = Counter32
_SlbRealTotalConnections_Object = MibTableColumn
slbRealTotalConnections = _SlbRealTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 3, 1, 1, 18),
    _SlbRealTotalConnections_Type()
)
slbRealTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealTotalConnections.setStatus("current")
_SlbRealHCTotalConnections_Type = Counter64
_SlbRealHCTotalConnections_Object = MibTableColumn
slbRealHCTotalConnections = _SlbRealHCTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 3, 1, 1, 19),
    _SlbRealHCTotalConnections_Type()
)
slbRealHCTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealHCTotalConnections.setStatus("current")
_SlbVirtualServers_ObjectIdentity = ObjectIdentity
slbVirtualServers = _SlbVirtualServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4)
)
_SlbVirtualServerTable_Object = MibTable
slbVirtualServerTable = _SlbVirtualServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 1)
)
if mibBuilder.loadTexts:
    slbVirtualServerTable.setStatus("current")
_SlbVirtualServerTableEntry_Object = MibTableRow
slbVirtualServerTableEntry = _SlbVirtualServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 1, 1)
)
slbVirtualServerTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-MIB", "slbVirtualServerName"),
)
if mibBuilder.loadTexts:
    slbVirtualServerTableEntry.setStatus("current")
_SlbVirtualServerName_Type = SlbServerString
_SlbVirtualServerName_Object = MibTableColumn
slbVirtualServerName = _SlbVirtualServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 1, 1, 1),
    _SlbVirtualServerName_Type()
)
slbVirtualServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbVirtualServerName.setStatus("current")


class _SlbVirtualServerState_Type(SlbVirtualServState):
    """Custom type slbVirtualServerState based on SlbVirtualServState"""


_SlbVirtualServerState_Object = MibTableColumn
slbVirtualServerState = _SlbVirtualServerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 1, 1, 2),
    _SlbVirtualServerState_Type()
)
slbVirtualServerState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbVirtualServerState.setStatus("current")
_SlbVirtualIndex_Type = Unsigned32
_SlbVirtualIndex_Object = MibTableColumn
slbVirtualIndex = _SlbVirtualIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 1, 1, 3),
    _SlbVirtualIndex_Type()
)
slbVirtualIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVirtualIndex.setStatus("current")


class _SlbVirtualIpAddress_Type(IpAddress):
    """Custom type slbVirtualIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_SlbVirtualIpAddress_Object = MibTableColumn
slbVirtualIpAddress = _SlbVirtualIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 1, 1, 4),
    _SlbVirtualIpAddress_Type()
)
slbVirtualIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbVirtualIpAddress.setStatus("current")


class _SlbVirtualPort_Type(CiscoPort):
    """Custom type slbVirtualPort based on CiscoPort"""
    defaultValue = 0


_SlbVirtualPort_Object = MibTableColumn
slbVirtualPort = _SlbVirtualPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 1, 1, 5),
    _SlbVirtualPort_Type()
)
slbVirtualPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbVirtualPort.setStatus("current")


class _SlbVirtualProtocol_Type(CiscoIpProtocol):
    """Custom type slbVirtualProtocol based on CiscoIpProtocol"""
    defaultValue = 0


_SlbVirtualProtocol_Object = MibTableColumn
slbVirtualProtocol = _SlbVirtualProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 1, 1, 6),
    _SlbVirtualProtocol_Type()
)
slbVirtualProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbVirtualProtocol.setStatus("current")


class _SlbVirtualService_Type(SlbVirtualService):
    """Custom type slbVirtualService based on SlbVirtualService"""


_SlbVirtualService_Object = MibTableColumn
slbVirtualService = _SlbVirtualService_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 1, 1, 7),
    _SlbVirtualService_Type()
)
slbVirtualService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbVirtualService.setStatus("current")


class _SlbVirtualAdvertise_Type(TruthValue):
    """Custom type slbVirtualAdvertise based on TruthValue"""


_SlbVirtualAdvertise_Object = MibTableColumn
slbVirtualAdvertise = _SlbVirtualAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 1, 1, 8),
    _SlbVirtualAdvertise_Type()
)
slbVirtualAdvertise.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbVirtualAdvertise.setStatus("current")


class _SlbVirtualFarmName_Type(SlbServerString):
    """Custom type slbVirtualFarmName based on SlbServerString"""
    defaultValue = OctetString("               ")


_SlbVirtualFarmName_Object = MibTableColumn
slbVirtualFarmName = _SlbVirtualFarmName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 1, 1, 9),
    _SlbVirtualFarmName_Type()
)
slbVirtualFarmName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbVirtualFarmName.setStatus("current")


class _SlbVirtualDelayTimer_Type(Unsigned32):
    """Custom type slbVirtualDelayTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_SlbVirtualDelayTimer_Type.__name__ = "Unsigned32"
_SlbVirtualDelayTimer_Object = MibTableColumn
slbVirtualDelayTimer = _SlbVirtualDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 1, 1, 10),
    _SlbVirtualDelayTimer_Type()
)
slbVirtualDelayTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbVirtualDelayTimer.setStatus("current")
if mibBuilder.loadTexts:
    slbVirtualDelayTimer.setUnits("seconds")


class _SlbVirtualIdleTimer_Type(Unsigned32):
    """Custom type slbVirtualIdleTimer based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_SlbVirtualIdleTimer_Type.__name__ = "Unsigned32"
_SlbVirtualIdleTimer_Object = MibTableColumn
slbVirtualIdleTimer = _SlbVirtualIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 1, 1, 11),
    _SlbVirtualIdleTimer_Type()
)
slbVirtualIdleTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbVirtualIdleTimer.setStatus("current")
if mibBuilder.loadTexts:
    slbVirtualIdleTimer.setUnits("seconds")


class _SlbVirtualStickyTimer_Type(TimeInterval):
    """Custom type slbVirtualStickyTimer based on TimeInterval"""
    defaultValue = 0


_SlbVirtualStickyTimer_Object = MibTableColumn
slbVirtualStickyTimer = _SlbVirtualStickyTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 1, 1, 12),
    _SlbVirtualStickyTimer_Type()
)
slbVirtualStickyTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbVirtualStickyTimer.setStatus("current")


class _SlbVirtualStickyGroup_Type(Unsigned32):
    """Custom type slbVirtualStickyGroup based on Unsigned32"""
    defaultValue = 0


_SlbVirtualStickyGroup_Object = MibTableColumn
slbVirtualStickyGroup = _SlbVirtualStickyGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 1, 1, 13),
    _SlbVirtualStickyGroup_Type()
)
slbVirtualStickyGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbVirtualStickyGroup.setStatus("current")


class _SlbVirtualSynguardCount_Type(Unsigned32):
    """Custom type slbVirtualSynguardCount based on Unsigned32"""
    defaultValue = 0


_SlbVirtualSynguardCount_Object = MibTableColumn
slbVirtualSynguardCount = _SlbVirtualSynguardCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 1, 1, 14),
    _SlbVirtualSynguardCount_Type()
)
slbVirtualSynguardCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbVirtualSynguardCount.setStatus("current")


class _SlbVirtualSynguardPeriod_Type(Unsigned32):
    """Custom type slbVirtualSynguardPeriod based on Unsigned32"""
    defaultValue = 0


_SlbVirtualSynguardPeriod_Object = MibTableColumn
slbVirtualSynguardPeriod = _SlbVirtualSynguardPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 1, 1, 15),
    _SlbVirtualSynguardPeriod_Type()
)
slbVirtualSynguardPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbVirtualSynguardPeriod.setStatus("current")
if mibBuilder.loadTexts:
    slbVirtualSynguardPeriod.setUnits("milliseconds")
_SlbVirtualRowStatus_Type = RowStatus
_SlbVirtualRowStatus_Object = MibTableColumn
slbVirtualRowStatus = _SlbVirtualRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 1, 1, 16),
    _SlbVirtualRowStatus_Type()
)
slbVirtualRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbVirtualRowStatus.setStatus("current")
_SlbVirtualNumberOfConnections_Type = Gauge32
_SlbVirtualNumberOfConnections_Object = MibTableColumn
slbVirtualNumberOfConnections = _SlbVirtualNumberOfConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 1, 1, 17),
    _SlbVirtualNumberOfConnections_Type()
)
slbVirtualNumberOfConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVirtualNumberOfConnections.setStatus("current")
_SlbVirtualTotalConnections_Type = Counter32
_SlbVirtualTotalConnections_Object = MibTableColumn
slbVirtualTotalConnections = _SlbVirtualTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 1, 1, 18),
    _SlbVirtualTotalConnections_Type()
)
slbVirtualTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVirtualTotalConnections.setStatus("current")
_SlbVirtualHCTotalConnections_Type = Counter64
_SlbVirtualHCTotalConnections_Object = MibTableColumn
slbVirtualHCTotalConnections = _SlbVirtualHCTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 1, 1, 19),
    _SlbVirtualHCTotalConnections_Type()
)
slbVirtualHCTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVirtualHCTotalConnections.setStatus("current")


class _SlbVirtualMask_Type(IpAddress):
    """Custom type slbVirtualMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_SlbVirtualMask_Object = MibTableColumn
slbVirtualMask = _SlbVirtualMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 1, 1, 20),
    _SlbVirtualMask_Type()
)
slbVirtualMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbVirtualMask.setStatus("current")
_SlbVServerInfoTable_Object = MibTable
slbVServerInfoTable = _SlbVServerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 2)
)
if mibBuilder.loadTexts:
    slbVServerInfoTable.setStatus("current")
_SlbVServerInfoTableEntry_Object = MibTableRow
slbVServerInfoTableEntry = _SlbVServerInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 2, 1)
)
slbVServerInfoTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-MIB", "slbVServerIndex"),
)
if mibBuilder.loadTexts:
    slbVServerInfoTableEntry.setStatus("current")


class _SlbVServerIndex_Type(Unsigned32):
    """Custom type slbVServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SlbVServerIndex_Type.__name__ = "Unsigned32"
_SlbVServerIndex_Object = MibTableColumn
slbVServerIndex = _SlbVServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 2, 1, 1),
    _SlbVServerIndex_Type()
)
slbVServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbVServerIndex.setStatus("current")
_SlbVServerClassMap_Type = SnmpAdminString
_SlbVServerClassMap_Object = MibTableColumn
slbVServerClassMap = _SlbVServerClassMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 2, 1, 2),
    _SlbVServerClassMap_Type()
)
slbVServerClassMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVServerClassMap.setStatus("current")
_SlbVServerPolicyMap_Type = SnmpAdminString
_SlbVServerPolicyMap_Object = MibTableColumn
slbVServerPolicyMap = _SlbVServerPolicyMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 2, 1, 3),
    _SlbVServerPolicyMap_Type()
)
slbVServerPolicyMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVServerPolicyMap.setStatus("current")
_SlbVServerState_Type = SlbVirtualServState
_SlbVServerState_Object = MibTableColumn
slbVServerState = _SlbVServerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 2, 1, 4),
    _SlbVServerState_Type()
)
slbVServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVServerState.setStatus("current")
_SlbVServerStateChangeDescr_Type = SnmpAdminString
_SlbVServerStateChangeDescr_Object = MibTableColumn
slbVServerStateChangeDescr = _SlbVServerStateChangeDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 2, 1, 5),
    _SlbVServerStateChangeDescr_Type()
)
slbVServerStateChangeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVServerStateChangeDescr.setStatus("current")
_SlbVServerNumberOfConnections_Type = Gauge32
_SlbVServerNumberOfConnections_Object = MibTableColumn
slbVServerNumberOfConnections = _SlbVServerNumberOfConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 2, 1, 6),
    _SlbVServerNumberOfConnections_Type()
)
slbVServerNumberOfConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVServerNumberOfConnections.setStatus("current")
_SlbVServerTotalConnections_Type = Counter32
_SlbVServerTotalConnections_Object = MibTableColumn
slbVServerTotalConnections = _SlbVServerTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 2, 1, 7),
    _SlbVServerTotalConnections_Type()
)
slbVServerTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVServerTotalConnections.setStatus("current")
_SlbVServerDroppedConnections_Type = Counter32
_SlbVServerDroppedConnections_Object = MibTableColumn
slbVServerDroppedConnections = _SlbVServerDroppedConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 2, 1, 8),
    _SlbVServerDroppedConnections_Type()
)
slbVServerDroppedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVServerDroppedConnections.setStatus("current")
if mibBuilder.loadTexts:
    slbVServerDroppedConnections.setUnits("connections")
_SlbVServerClientPacketCounts_Type = Counter32
_SlbVServerClientPacketCounts_Object = MibTableColumn
slbVServerClientPacketCounts = _SlbVServerClientPacketCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 2, 1, 9),
    _SlbVServerClientPacketCounts_Type()
)
slbVServerClientPacketCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVServerClientPacketCounts.setStatus("current")
if mibBuilder.loadTexts:
    slbVServerClientPacketCounts.setUnits("packets")
_SlbVServerPacketCounts_Type = Counter32
_SlbVServerPacketCounts_Object = MibTableColumn
slbVServerPacketCounts = _SlbVServerPacketCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 2, 1, 10),
    _SlbVServerPacketCounts_Type()
)
slbVServerPacketCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVServerPacketCounts.setStatus("current")
if mibBuilder.loadTexts:
    slbVServerPacketCounts.setUnits("packets")
_SlbVServerClientByteCounts_Type = Counter64
_SlbVServerClientByteCounts_Object = MibTableColumn
slbVServerClientByteCounts = _SlbVServerClientByteCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 2, 1, 11),
    _SlbVServerClientByteCounts_Type()
)
slbVServerClientByteCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVServerClientByteCounts.setStatus("current")
if mibBuilder.loadTexts:
    slbVServerClientByteCounts.setUnits("bytes")
_SlbVServerByteCounts_Type = Counter64
_SlbVServerByteCounts_Object = MibTableColumn
slbVServerByteCounts = _SlbVServerByteCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 2, 1, 12),
    _SlbVServerByteCounts_Type()
)
slbVServerByteCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVServerByteCounts.setStatus("current")
if mibBuilder.loadTexts:
    slbVServerByteCounts.setUnits("bytes")
_SlbVServerMaxConnLimitDropCounts_Type = Counter32
_SlbVServerMaxConnLimitDropCounts_Object = MibTableColumn
slbVServerMaxConnLimitDropCounts = _SlbVServerMaxConnLimitDropCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 2, 1, 13),
    _SlbVServerMaxConnLimitDropCounts_Type()
)
slbVServerMaxConnLimitDropCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVServerMaxConnLimitDropCounts.setStatus("current")
if mibBuilder.loadTexts:
    slbVServerMaxConnLimitDropCounts.setUnits("connections")
_SlbVServerConnRateLimitDropCounts_Type = Counter32
_SlbVServerConnRateLimitDropCounts_Object = MibTableColumn
slbVServerConnRateLimitDropCounts = _SlbVServerConnRateLimitDropCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 2, 1, 14),
    _SlbVServerConnRateLimitDropCounts_Type()
)
slbVServerConnRateLimitDropCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVServerConnRateLimitDropCounts.setStatus("current")
if mibBuilder.loadTexts:
    slbVServerConnRateLimitDropCounts.setUnits("connections")
_SlbVServerBWRateLimitDropCounts_Type = Counter32
_SlbVServerBWRateLimitDropCounts_Object = MibTableColumn
slbVServerBWRateLimitDropCounts = _SlbVServerBWRateLimitDropCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 2, 1, 15),
    _SlbVServerBWRateLimitDropCounts_Type()
)
slbVServerBWRateLimitDropCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVServerBWRateLimitDropCounts.setStatus("deprecated")
if mibBuilder.loadTexts:
    slbVServerBWRateLimitDropCounts.setUnits("connections")
_SlbVServerBandWidthRateLimitDropCounts_Type = Counter32
_SlbVServerBandWidthRateLimitDropCounts_Object = MibTableColumn
slbVServerBandWidthRateLimitDropCounts = _SlbVServerBandWidthRateLimitDropCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 2, 1, 16),
    _SlbVServerBandWidthRateLimitDropCounts_Type()
)
slbVServerBandWidthRateLimitDropCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVServerBandWidthRateLimitDropCounts.setStatus("current")
if mibBuilder.loadTexts:
    slbVServerBandWidthRateLimitDropCounts.setUnits("bytes")
_SlbVServerL4Decisions_Type = Counter32
_SlbVServerL4Decisions_Object = MibTableColumn
slbVServerL4Decisions = _SlbVServerL4Decisions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 2, 1, 17),
    _SlbVServerL4Decisions_Type()
)
slbVServerL4Decisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVServerL4Decisions.setStatus("current")
if mibBuilder.loadTexts:
    slbVServerL4Decisions.setUnits("connections")
_SlbVServerL7Decisions_Type = Counter32
_SlbVServerL7Decisions_Object = MibTableColumn
slbVServerL7Decisions = _SlbVServerL7Decisions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 2, 1, 18),
    _SlbVServerL7Decisions_Type()
)
slbVServerL7Decisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVServerL7Decisions.setStatus("current")
if mibBuilder.loadTexts:
    slbVServerL7Decisions.setUnits("connections")
_SlbVServerEstablishedConnections_Type = Gauge32
_SlbVServerEstablishedConnections_Object = MibTableColumn
slbVServerEstablishedConnections = _SlbVServerEstablishedConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 2, 1, 19),
    _SlbVServerEstablishedConnections_Type()
)
slbVServerEstablishedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVServerEstablishedConnections.setStatus("current")
if mibBuilder.loadTexts:
    slbVServerEstablishedConnections.setUnits("connections")
_SlbVServerIPTable_Object = MibTable
slbVServerIPTable = _SlbVServerIPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 3)
)
if mibBuilder.loadTexts:
    slbVServerIPTable.setStatus("current")
_SlbVServerIPTableEntry_Object = MibTableRow
slbVServerIPTableEntry = _SlbVServerIPTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 3, 1)
)
slbVServerIPTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-MIB", "slbVServerIndex"),
    (0, "CISCO-SLB-MIB", "slbVServerObjectIndex"),
)
if mibBuilder.loadTexts:
    slbVServerIPTableEntry.setStatus("current")


class _SlbVServerObjectIndex_Type(Unsigned32):
    """Custom type slbVServerObjectIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SlbVServerObjectIndex_Type.__name__ = "Unsigned32"
_SlbVServerObjectIndex_Object = MibTableColumn
slbVServerObjectIndex = _SlbVServerObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 3, 1, 1),
    _SlbVServerObjectIndex_Type()
)
slbVServerObjectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbVServerObjectIndex.setStatus("current")


class _SlbVServerIpAddressType_Type(InetAddressType):
    """Custom type slbVServerIpAddressType based on InetAddressType"""


_SlbVServerIpAddressType_Object = MibTableColumn
slbVServerIpAddressType = _SlbVServerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 3, 1, 2),
    _SlbVServerIpAddressType_Type()
)
slbVServerIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbVServerIpAddressType.setStatus("current")
_SlbVServerIpAddress_Type = InetAddress
_SlbVServerIpAddress_Object = MibTableColumn
slbVServerIpAddress = _SlbVServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 3, 1, 3),
    _SlbVServerIpAddress_Type()
)
slbVServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbVServerIpAddress.setStatus("current")


class _SlbVServerIpMask_Type(InetAddressPrefixLength):
    """Custom type slbVServerIpMask based on InetAddressPrefixLength"""
    defaultValue = 0


_SlbVServerIpMask_Object = MibTableColumn
slbVServerIpMask = _SlbVServerIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 3, 1, 4),
    _SlbVServerIpMask_Type()
)
slbVServerIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbVServerIpMask.setStatus("current")
_SlbVServerProtocol_Type = CiscoIpProtocol
_SlbVServerProtocol_Object = MibTableColumn
slbVServerProtocol = _SlbVServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 3, 1, 5),
    _SlbVServerProtocol_Type()
)
slbVServerProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbVServerProtocol.setStatus("current")


class _SlbVServerPortLow_Type(InetPortNumber):
    """Custom type slbVServerPortLow based on InetPortNumber"""
    defaultValue = 0


_SlbVServerPortLow_Object = MibTableColumn
slbVServerPortLow = _SlbVServerPortLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 3, 1, 6),
    _SlbVServerPortLow_Type()
)
slbVServerPortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbVServerPortLow.setStatus("current")


class _SlbVServerPortHigh_Type(InetPortNumber):
    """Custom type slbVServerPortHigh based on InetPortNumber"""
    defaultValue = 0


_SlbVServerPortHigh_Object = MibTableColumn
slbVServerPortHigh = _SlbVServerPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 3, 1, 7),
    _SlbVServerPortHigh_Type()
)
slbVServerPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbVServerPortHigh.setStatus("current")


class _SlbVServerStorageType_Type(StorageType):
    """Custom type slbVServerStorageType based on StorageType"""


_SlbVServerStorageType_Object = MibTableColumn
slbVServerStorageType = _SlbVServerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 3, 1, 8),
    _SlbVServerStorageType_Type()
)
slbVServerStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbVServerStorageType.setStatus("current")
_SlbVServerRowStatus_Type = RowStatus
_SlbVServerRowStatus_Object = MibTableColumn
slbVServerRowStatus = _SlbVServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 4, 3, 1, 9),
    _SlbVServerRowStatus_Type()
)
slbVServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbVServerRowStatus.setStatus("current")
_SlbConnections_ObjectIdentity = ObjectIdentity
slbConnections = _SlbConnections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 5)
)
_SlbConnectionTable_Object = MibTable
slbConnectionTable = _SlbConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 5, 1)
)
if mibBuilder.loadTexts:
    slbConnectionTable.setStatus("current")
_SlbConnectionTableEntry_Object = MibTableRow
slbConnectionTableEntry = _SlbConnectionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 5, 1, 1)
)
slbConnectionTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-MIB", "slbConnectionIndex"),
    (0, "CISCO-SLB-MIB", "slbConnectionVirtualIpAddress"),
    (0, "CISCO-SLB-MIB", "slbConnectionVirtualPort"),
    (0, "CISCO-SLB-MIB", "slbConnectionProtocol"),
    (0, "CISCO-SLB-MIB", "slbConnectionClientIpAddr"),
    (0, "CISCO-SLB-MIB", "slbConnectionClientPort"),
)
if mibBuilder.loadTexts:
    slbConnectionTableEntry.setStatus("current")
_SlbConnectionIndex_Type = Unsigned32
_SlbConnectionIndex_Object = MibTableColumn
slbConnectionIndex = _SlbConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 5, 1, 1, 1),
    _SlbConnectionIndex_Type()
)
slbConnectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbConnectionIndex.setStatus("current")
_SlbConnectionVirtualIpAddress_Type = IpAddress
_SlbConnectionVirtualIpAddress_Object = MibTableColumn
slbConnectionVirtualIpAddress = _SlbConnectionVirtualIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 5, 1, 1, 2),
    _SlbConnectionVirtualIpAddress_Type()
)
slbConnectionVirtualIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbConnectionVirtualIpAddress.setStatus("current")
_SlbConnectionVirtualPort_Type = CiscoPort
_SlbConnectionVirtualPort_Object = MibTableColumn
slbConnectionVirtualPort = _SlbConnectionVirtualPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 5, 1, 1, 3),
    _SlbConnectionVirtualPort_Type()
)
slbConnectionVirtualPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbConnectionVirtualPort.setStatus("current")
_SlbConnectionProtocol_Type = CiscoIpProtocol
_SlbConnectionProtocol_Object = MibTableColumn
slbConnectionProtocol = _SlbConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 5, 1, 1, 4),
    _SlbConnectionProtocol_Type()
)
slbConnectionProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbConnectionProtocol.setStatus("current")
_SlbConnectionClientIpAddr_Type = IpAddress
_SlbConnectionClientIpAddr_Object = MibTableColumn
slbConnectionClientIpAddr = _SlbConnectionClientIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 5, 1, 1, 5),
    _SlbConnectionClientIpAddr_Type()
)
slbConnectionClientIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbConnectionClientIpAddr.setStatus("current")
_SlbConnectionClientPort_Type = CiscoPort
_SlbConnectionClientPort_Object = MibTableColumn
slbConnectionClientPort = _SlbConnectionClientPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 5, 1, 1, 6),
    _SlbConnectionClientPort_Type()
)
slbConnectionClientPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbConnectionClientPort.setStatus("current")
_SlbConnectionState_Type = SlbConnectionState
_SlbConnectionState_Object = MibTableColumn
slbConnectionState = _SlbConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 5, 1, 1, 7),
    _SlbConnectionState_Type()
)
slbConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbConnectionState.setStatus("current")
_SlbConnectionRealIpAddr_Type = IpAddress
_SlbConnectionRealIpAddr_Object = MibTableColumn
slbConnectionRealIpAddr = _SlbConnectionRealIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 5, 1, 1, 8),
    _SlbConnectionRealIpAddr_Type()
)
slbConnectionRealIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbConnectionRealIpAddr.setStatus("current")
_SlbConnectionServerPort_Type = CiscoPort
_SlbConnectionServerPort_Object = MibTableColumn
slbConnectionServerPort = _SlbConnectionServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 5, 1, 1, 9),
    _SlbConnectionServerPort_Type()
)
slbConnectionServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbConnectionServerPort.setStatus("current")
_SlbConnectionNumCacheEntries_Type = Gauge32
_SlbConnectionNumCacheEntries_Object = MibTableColumn
slbConnectionNumCacheEntries = _SlbConnectionNumCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 5, 1, 1, 10),
    _SlbConnectionNumCacheEntries_Type()
)
slbConnectionNumCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbConnectionNumCacheEntries.setStatus("current")
_SlbConnectionSynCount_Type = Counter32
_SlbConnectionSynCount_Object = MibTableColumn
slbConnectionSynCount = _SlbConnectionSynCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 5, 1, 1, 11),
    _SlbConnectionSynCount_Type()
)
slbConnectionSynCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbConnectionSynCount.setStatus("current")
_SlbVirtualClients_ObjectIdentity = ObjectIdentity
slbVirtualClients = _SlbVirtualClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 6)
)
_SlbVirtualClientTable_Object = MibTable
slbVirtualClientTable = _SlbVirtualClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 6, 1)
)
if mibBuilder.loadTexts:
    slbVirtualClientTable.setStatus("current")
_SlbVirtualClientTableEntry_Object = MibTableRow
slbVirtualClientTableEntry = _SlbVirtualClientTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 6, 1, 1)
)
slbVirtualClientTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-MIB", "slbVirtualServerName"),
    (0, "CISCO-SLB-MIB", "slbVirtualClientIpAddress"),
    (0, "CISCO-SLB-MIB", "slbVirtualClientMask"),
)
if mibBuilder.loadTexts:
    slbVirtualClientTableEntry.setStatus("current")
_SlbVirtualClientIpAddress_Type = IpAddress
_SlbVirtualClientIpAddress_Object = MibTableColumn
slbVirtualClientIpAddress = _SlbVirtualClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 6, 1, 1, 1),
    _SlbVirtualClientIpAddress_Type()
)
slbVirtualClientIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbVirtualClientIpAddress.setStatus("current")
_SlbVirtualClientMask_Type = IpAddress
_SlbVirtualClientMask_Object = MibTableColumn
slbVirtualClientMask = _SlbVirtualClientMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 6, 1, 1, 2),
    _SlbVirtualClientMask_Type()
)
slbVirtualClientMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbVirtualClientMask.setStatus("current")


class _SlbVirtualClientExclude_Type(TruthValue):
    """Custom type slbVirtualClientExclude based on TruthValue"""


_SlbVirtualClientExclude_Object = MibTableColumn
slbVirtualClientExclude = _SlbVirtualClientExclude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 6, 1, 1, 3),
    _SlbVirtualClientExclude_Type()
)
slbVirtualClientExclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbVirtualClientExclude.setStatus("current")
_SlbVirtualClientRowStatus_Type = RowStatus
_SlbVirtualClientRowStatus_Object = MibTableColumn
slbVirtualClientRowStatus = _SlbVirtualClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 6, 1, 1, 4),
    _SlbVirtualClientRowStatus_Type()
)
slbVirtualClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbVirtualClientRowStatus.setStatus("current")
_SlbStickyObjects_ObjectIdentity = ObjectIdentity
slbStickyObjects = _SlbStickyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 7)
)
_SlbStickyObjectTable_Object = MibTable
slbStickyObjectTable = _SlbStickyObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 7, 1)
)
if mibBuilder.loadTexts:
    slbStickyObjectTable.setStatus("current")
_SlbStickyObjectTableEntry_Object = MibTableRow
slbStickyObjectTableEntry = _SlbStickyObjectTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 7, 1, 1)
)
slbStickyObjectTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-MIB", "slbStickyObjectGroupId"),
    (0, "CISCO-SLB-MIB", "slbStickyObjectClientIpAddress"),
)
if mibBuilder.loadTexts:
    slbStickyObjectTableEntry.setStatus("current")


class _SlbStickyObjectGroupId_Type(Unsigned32):
    """Custom type slbStickyObjectGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SlbStickyObjectGroupId_Type.__name__ = "Unsigned32"
_SlbStickyObjectGroupId_Object = MibTableColumn
slbStickyObjectGroupId = _SlbStickyObjectGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 7, 1, 1, 1),
    _SlbStickyObjectGroupId_Type()
)
slbStickyObjectGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbStickyObjectGroupId.setStatus("current")
_SlbStickyObjectClientIpAddress_Type = IpAddress
_SlbStickyObjectClientIpAddress_Object = MibTableColumn
slbStickyObjectClientIpAddress = _SlbStickyObjectClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 7, 1, 1, 2),
    _SlbStickyObjectClientIpAddress_Type()
)
slbStickyObjectClientIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbStickyObjectClientIpAddress.setStatus("current")


class _SlbStickyObjectRealIpAddress_Type(IpAddress):
    """Custom type slbStickyObjectRealIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_SlbStickyObjectRealIpAddress_Object = MibTableColumn
slbStickyObjectRealIpAddress = _SlbStickyObjectRealIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 7, 1, 1, 3),
    _SlbStickyObjectRealIpAddress_Type()
)
slbStickyObjectRealIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbStickyObjectRealIpAddress.setStatus("current")
_SlbStickyObjectConnectionCount_Type = Gauge32
_SlbStickyObjectConnectionCount_Object = MibTableColumn
slbStickyObjectConnectionCount = _SlbStickyObjectConnectionCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 7, 1, 1, 4),
    _SlbStickyObjectConnectionCount_Type()
)
slbStickyObjectConnectionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStickyObjectConnectionCount.setStatus("current")
_SlbStickyObjectFtpControlCount_Type = Gauge32
_SlbStickyObjectFtpControlCount_Object = MibTableColumn
slbStickyObjectFtpControlCount = _SlbStickyObjectFtpControlCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 7, 1, 1, 5),
    _SlbStickyObjectFtpControlCount_Type()
)
slbStickyObjectFtpControlCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStickyObjectFtpControlCount.setStatus("current")
_SlbStickyObjectRowStatus_Type = RowStatus
_SlbStickyObjectRowStatus_Object = MibTableColumn
slbStickyObjectRowStatus = _SlbStickyObjectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 7, 1, 1, 6),
    _SlbStickyObjectRowStatus_Type()
)
slbStickyObjectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbStickyObjectRowStatus.setStatus("current")
_SlbNotificationObjects_ObjectIdentity = ObjectIdentity
slbNotificationObjects = _SlbNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 8)
)


class _CSlbVirtStateChangeNotifEnabled_Type(TruthValue):
    """Custom type cSlbVirtStateChangeNotifEnabled based on TruthValue"""


_CSlbVirtStateChangeNotifEnabled_Object = MibScalar
cSlbVirtStateChangeNotifEnabled = _CSlbVirtStateChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 8, 1),
    _CSlbVirtStateChangeNotifEnabled_Type()
)
cSlbVirtStateChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSlbVirtStateChangeNotifEnabled.setStatus("deprecated")


class _CSlbRealStateChangeNotifEnabled_Type(TruthValue):
    """Custom type cSlbRealStateChangeNotifEnabled based on TruthValue"""


_CSlbRealStateChangeNotifEnabled_Object = MibScalar
cSlbRealStateChangeNotifEnabled = _CSlbRealStateChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 8, 2),
    _CSlbRealStateChangeNotifEnabled_Type()
)
cSlbRealStateChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSlbRealStateChangeNotifEnabled.setStatus("deprecated")


class _CSlbVServerStateChangeNotifEnabled_Type(TruthValue):
    """Custom type cSlbVServerStateChangeNotifEnabled based on TruthValue"""


_CSlbVServerStateChangeNotifEnabled_Object = MibScalar
cSlbVServerStateChangeNotifEnabled = _CSlbVServerStateChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 8, 3),
    _CSlbVServerStateChangeNotifEnabled_Type()
)
cSlbVServerStateChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSlbVServerStateChangeNotifEnabled.setStatus("current")


class _CSlbVirtualServerStateChangeNotifEnabled_Type(TruthValue):
    """Custom type cSlbVirtualServerStateChangeNotifEnabled based on TruthValue"""


_CSlbVirtualServerStateChangeNotifEnabled_Object = MibScalar
cSlbVirtualServerStateChangeNotifEnabled = _CSlbVirtualServerStateChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 8, 4),
    _CSlbVirtualServerStateChangeNotifEnabled_Type()
)
cSlbVirtualServerStateChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSlbVirtualServerStateChangeNotifEnabled.setStatus("current")


class _CSlbRealServerStateChangeNotifEnabled_Type(TruthValue):
    """Custom type cSlbRealServerStateChangeNotifEnabled based on TruthValue"""


_CSlbRealServerStateChangeNotifEnabled_Object = MibScalar
cSlbRealServerStateChangeNotifEnabled = _CSlbRealServerStateChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 8, 5),
    _CSlbRealServerStateChangeNotifEnabled_Type()
)
cSlbRealServerStateChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSlbRealServerStateChangeNotifEnabled.setStatus("current")


class _SlbInetAddressType_Type(InetAddressType):
    """Custom type slbInetAddressType based on InetAddressType"""


_SlbInetAddressType_Object = MibScalar
slbInetAddressType = _SlbInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 8, 6),
    _SlbInetAddressType_Type()
)
slbInetAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    slbInetAddressType.setStatus("current")
_SlbInetAddress_Type = InetAddress
_SlbInetAddress_Object = MibScalar
slbInetAddress = _SlbInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 8, 7),
    _SlbInetAddress_Type()
)
slbInetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    slbInetAddress.setStatus("current")
_SlbName_Type = SlbServerString
_SlbName_Object = MibScalar
slbName = _SlbName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 8, 8),
    _SlbName_Type()
)
slbName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    slbName.setStatus("current")
_SlbPort_Type = CiscoPort
_SlbPort_Object = MibScalar
slbPort = _SlbPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 8, 9),
    _SlbPort_Type()
)
slbPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    slbPort.setStatus("current")
_SlbDfpPassword_ObjectIdentity = ObjectIdentity
slbDfpPassword = _SlbDfpPassword_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 9)
)
_SlbDfpPasswordTable_Object = MibTable
slbDfpPasswordTable = _SlbDfpPasswordTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 9, 1)
)
if mibBuilder.loadTexts:
    slbDfpPasswordTable.setStatus("current")
_SlbDfpPasswordTableEntry_Object = MibTableRow
slbDfpPasswordTableEntry = _SlbDfpPasswordTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 9, 1, 1)
)
slbDfpPasswordTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
)
if mibBuilder.loadTexts:
    slbDfpPasswordTableEntry.setStatus("current")
_SlbDfpPasswordPending_Type = SlbPasswordString
_SlbDfpPasswordPending_Object = MibTableColumn
slbDfpPasswordPending = _SlbDfpPasswordPending_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 9, 1, 1, 1),
    _SlbDfpPasswordPending_Type()
)
slbDfpPasswordPending.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbDfpPasswordPending.setStatus("current")


class _SlbDfpPasswordTimeout_Type(TimeInterval):
    """Custom type slbDfpPasswordTimeout based on TimeInterval"""
    defaultValue = 0


_SlbDfpPasswordTimeout_Object = MibTableColumn
slbDfpPasswordTimeout = _SlbDfpPasswordTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 9, 1, 1, 2),
    _SlbDfpPasswordTimeout_Type()
)
slbDfpPasswordTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbDfpPasswordTimeout.setStatus("current")
_SlbDfpPasswordRowStatus_Type = RowStatus
_SlbDfpPasswordRowStatus_Object = MibTableColumn
slbDfpPasswordRowStatus = _SlbDfpPasswordRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 9, 1, 1, 3),
    _SlbDfpPasswordRowStatus_Type()
)
slbDfpPasswordRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbDfpPasswordRowStatus.setStatus("current")
_SlbDfpAgents_ObjectIdentity = ObjectIdentity
slbDfpAgents = _SlbDfpAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 10)
)
_SlbDfpAgentTable_Object = MibTable
slbDfpAgentTable = _SlbDfpAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 10, 1)
)
if mibBuilder.loadTexts:
    slbDfpAgentTable.setStatus("current")
_SlbDfpAgentTableEntry_Object = MibTableRow
slbDfpAgentTableEntry = _SlbDfpAgentTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 10, 1, 1)
)
slbDfpAgentTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-MIB", "slbDfpAgentIpAddress"),
    (0, "CISCO-SLB-MIB", "slbDfpAgentPort"),
)
if mibBuilder.loadTexts:
    slbDfpAgentTableEntry.setStatus("current")
_SlbDfpAgentIpAddress_Type = IpAddress
_SlbDfpAgentIpAddress_Object = MibTableColumn
slbDfpAgentIpAddress = _SlbDfpAgentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 10, 1, 1, 1),
    _SlbDfpAgentIpAddress_Type()
)
slbDfpAgentIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbDfpAgentIpAddress.setStatus("current")
_SlbDfpAgentPort_Type = CiscoPort
_SlbDfpAgentPort_Object = MibTableColumn
slbDfpAgentPort = _SlbDfpAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 10, 1, 1, 2),
    _SlbDfpAgentPort_Type()
)
slbDfpAgentPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbDfpAgentPort.setStatus("current")
_SlbDfpAgentState_Type = SlbDfpAgentState
_SlbDfpAgentState_Object = MibTableColumn
slbDfpAgentState = _SlbDfpAgentState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 10, 1, 1, 3),
    _SlbDfpAgentState_Type()
)
slbDfpAgentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbDfpAgentState.setStatus("current")
_SlbDfpAgentTimeout_Type = TimeInterval
_SlbDfpAgentTimeout_Object = MibTableColumn
slbDfpAgentTimeout = _SlbDfpAgentTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 10, 1, 1, 4),
    _SlbDfpAgentTimeout_Type()
)
slbDfpAgentTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbDfpAgentTimeout.setStatus("current")


class _SlbDfpAgentRetryCount_Type(Unsigned32):
    """Custom type slbDfpAgentRetryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlbDfpAgentRetryCount_Type.__name__ = "Unsigned32"
_SlbDfpAgentRetryCount_Object = MibTableColumn
slbDfpAgentRetryCount = _SlbDfpAgentRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 10, 1, 1, 5),
    _SlbDfpAgentRetryCount_Type()
)
slbDfpAgentRetryCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbDfpAgentRetryCount.setStatus("current")
_SlbDfpAgentInterval_Type = TimeInterval
_SlbDfpAgentInterval_Object = MibTableColumn
slbDfpAgentInterval = _SlbDfpAgentInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 10, 1, 1, 6),
    _SlbDfpAgentInterval_Type()
)
slbDfpAgentInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbDfpAgentInterval.setStatus("current")
_SlbDfpAgentRowStatus_Type = RowStatus
_SlbDfpAgentRowStatus_Object = MibTableColumn
slbDfpAgentRowStatus = _SlbDfpAgentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 10, 1, 1, 7),
    _SlbDfpAgentRowStatus_Type()
)
slbDfpAgentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbDfpAgentRowStatus.setStatus("current")
_SlbDfpReal_ObjectIdentity = ObjectIdentity
slbDfpReal = _SlbDfpReal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 11)
)
_SlbDfpRealTable_Object = MibTable
slbDfpRealTable = _SlbDfpRealTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 11, 1)
)
if mibBuilder.loadTexts:
    slbDfpRealTable.setStatus("current")
_SlbDfpRealTableEntry_Object = MibTableRow
slbDfpRealTableEntry = _SlbDfpRealTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 11, 1, 1)
)
slbDfpRealTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-MIB", "slbDfpRealIpAddress"),
    (0, "CISCO-SLB-MIB", "slbDfpRealProtocol"),
    (0, "CISCO-SLB-MIB", "slbDfpRealPort"),
    (0, "CISCO-SLB-MIB", "slbDfpRealBindId"),
)
if mibBuilder.loadTexts:
    slbDfpRealTableEntry.setStatus("current")
_SlbDfpRealIpAddress_Type = IpAddress
_SlbDfpRealIpAddress_Object = MibTableColumn
slbDfpRealIpAddress = _SlbDfpRealIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 11, 1, 1, 1),
    _SlbDfpRealIpAddress_Type()
)
slbDfpRealIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbDfpRealIpAddress.setStatus("current")
_SlbDfpRealProtocol_Type = CiscoIpProtocol
_SlbDfpRealProtocol_Object = MibTableColumn
slbDfpRealProtocol = _SlbDfpRealProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 11, 1, 1, 2),
    _SlbDfpRealProtocol_Type()
)
slbDfpRealProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbDfpRealProtocol.setStatus("current")
_SlbDfpRealPort_Type = CiscoPort
_SlbDfpRealPort_Object = MibTableColumn
slbDfpRealPort = _SlbDfpRealPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 11, 1, 1, 3),
    _SlbDfpRealPort_Type()
)
slbDfpRealPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbDfpRealPort.setStatus("current")
_SlbDfpRealBindId_Type = Unsigned32
_SlbDfpRealBindId_Object = MibTableColumn
slbDfpRealBindId = _SlbDfpRealBindId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 11, 1, 1, 4),
    _SlbDfpRealBindId_Type()
)
slbDfpRealBindId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbDfpRealBindId.setStatus("current")


class _SlbDfpRealWeight_Type(Unsigned32):
    """Custom type slbDfpRealWeight based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlbDfpRealWeight_Type.__name__ = "Unsigned32"
_SlbDfpRealWeight_Object = MibTableColumn
slbDfpRealWeight = _SlbDfpRealWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 11, 1, 1, 5),
    _SlbDfpRealWeight_Type()
)
slbDfpRealWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbDfpRealWeight.setStatus("current")
_SlbDfpRealRowStatus_Type = RowStatus
_SlbDfpRealRowStatus_Object = MibTableColumn
slbDfpRealRowStatus = _SlbDfpRealRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 11, 1, 1, 6),
    _SlbDfpRealRowStatus_Type()
)
slbDfpRealRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbDfpRealRowStatus.setStatus("current")
_SlbSasp_ObjectIdentity = ObjectIdentity
slbSasp = _SlbSasp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 12)
)
_SlbSaspTable_Object = MibTable
slbSaspTable = _SlbSaspTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 12, 1)
)
if mibBuilder.loadTexts:
    slbSaspTable.setStatus("current")
_SlbSaspTableEntry_Object = MibTableRow
slbSaspTableEntry = _SlbSaspTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 12, 1, 1)
)
slbSaspTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
)
if mibBuilder.loadTexts:
    slbSaspTableEntry.setStatus("current")
_SlbSaspIdentifier_Type = SnmpAdminString
_SlbSaspIdentifier_Object = MibTableColumn
slbSaspIdentifier = _SlbSaspIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 12, 1, 1, 1),
    _SlbSaspIdentifier_Type()
)
slbSaspIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbSaspIdentifier.setStatus("current")
_SlbSaspEnabled_Type = TruthValue
_SlbSaspEnabled_Object = MibTableColumn
slbSaspEnabled = _SlbSaspEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 12, 1, 1, 2),
    _SlbSaspEnabled_Type()
)
slbSaspEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbSaspEnabled.setStatus("current")
_SlbSaspHealth_Type = SlbSaspLBHealth
_SlbSaspHealth_Object = MibTableColumn
slbSaspHealth = _SlbSaspHealth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 12, 1, 1, 3),
    _SlbSaspHealth_Type()
)
slbSaspHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSaspHealth.setStatus("current")
_SlbSaspRedundancy_Type = SlbSaspRedundancy
_SlbSaspRedundancy_Object = MibTableColumn
slbSaspRedundancy = _SlbSaspRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 12, 1, 1, 4),
    _SlbSaspRedundancy_Type()
)
slbSaspRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSaspRedundancy.setStatus("current")
_SlbSaspMaxAgents_Type = Unsigned32
_SlbSaspMaxAgents_Object = MibTableColumn
slbSaspMaxAgents = _SlbSaspMaxAgents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 12, 1, 1, 5),
    _SlbSaspMaxAgents_Type()
)
slbSaspMaxAgents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSaspMaxAgents.setStatus("current")
_SlbSaspMaxLbWeight_Type = Unsigned32
_SlbSaspMaxLbWeight_Object = MibTableColumn
slbSaspMaxLbWeight = _SlbSaspMaxLbWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 12, 1, 1, 6),
    _SlbSaspMaxLbWeight_Type()
)
slbSaspMaxLbWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSaspMaxLbWeight.setStatus("current")
_SlbSaspAgents_ObjectIdentity = ObjectIdentity
slbSaspAgents = _SlbSaspAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 13)
)
_SlbSaspAgentTable_Object = MibTable
slbSaspAgentTable = _SlbSaspAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 13, 1)
)
if mibBuilder.loadTexts:
    slbSaspAgentTable.setStatus("current")
_SlbSaspAgentTableEntry_Object = MibTableRow
slbSaspAgentTableEntry = _SlbSaspAgentTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 13, 1, 1)
)
slbSaspAgentTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-MIB", "slbSaspAgentIpAddressType"),
    (0, "CISCO-SLB-MIB", "slbSaspAgentIpAddress"),
    (0, "CISCO-SLB-MIB", "slbSaspAgentPort"),
)
if mibBuilder.loadTexts:
    slbSaspAgentTableEntry.setStatus("current")
_SlbSaspAgentIpAddressType_Type = InetAddressType
_SlbSaspAgentIpAddressType_Object = MibTableColumn
slbSaspAgentIpAddressType = _SlbSaspAgentIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 13, 1, 1, 1),
    _SlbSaspAgentIpAddressType_Type()
)
slbSaspAgentIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbSaspAgentIpAddressType.setStatus("current")
_SlbSaspAgentIpAddress_Type = InetAddress
_SlbSaspAgentIpAddress_Object = MibTableColumn
slbSaspAgentIpAddress = _SlbSaspAgentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 13, 1, 1, 2),
    _SlbSaspAgentIpAddress_Type()
)
slbSaspAgentIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbSaspAgentIpAddress.setStatus("current")
_SlbSaspAgentPort_Type = InetPortNumber
_SlbSaspAgentPort_Object = MibTableColumn
slbSaspAgentPort = _SlbSaspAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 13, 1, 1, 3),
    _SlbSaspAgentPort_Type()
)
slbSaspAgentPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbSaspAgentPort.setStatus("current")
_SlbSaspAgentLabel_Type = SnmpAdminString
_SlbSaspAgentLabel_Object = MibTableColumn
slbSaspAgentLabel = _SlbSaspAgentLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 13, 1, 1, 4),
    _SlbSaspAgentLabel_Type()
)
slbSaspAgentLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbSaspAgentLabel.setStatus("current")
_SlbSaspAgentState_Type = SlbSaspAgentState
_SlbSaspAgentState_Object = MibTableColumn
slbSaspAgentState = _SlbSaspAgentState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 13, 1, 1, 5),
    _SlbSaspAgentState_Type()
)
slbSaspAgentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSaspAgentState.setStatus("current")
_SlbSaspAgentLastStateChange_Type = DateAndTime
_SlbSaspAgentLastStateChange_Object = MibTableColumn
slbSaspAgentLastStateChange = _SlbSaspAgentLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 13, 1, 1, 6),
    _SlbSaspAgentLastStateChange_Type()
)
slbSaspAgentLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSaspAgentLastStateChange.setStatus("current")
_SlbSaspAgentRowStatus_Type = RowStatus
_SlbSaspAgentRowStatus_Object = MibTableColumn
slbSaspAgentRowStatus = _SlbSaspAgentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 13, 1, 1, 7),
    _SlbSaspAgentRowStatus_Type()
)
slbSaspAgentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbSaspAgentRowStatus.setStatus("current")
_SlbSaspGroups_ObjectIdentity = ObjectIdentity
slbSaspGroups = _SlbSaspGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 14)
)
_SlbSaspGroupTable_Object = MibTable
slbSaspGroupTable = _SlbSaspGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 14, 1)
)
if mibBuilder.loadTexts:
    slbSaspGroupTable.setStatus("current")
_SlbSaspGroupTableEntry_Object = MibTableRow
slbSaspGroupTableEntry = _SlbSaspGroupTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 14, 1, 1)
)
slbSaspGroupTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-MIB", "slbSaspGroupName"),
)
if mibBuilder.loadTexts:
    slbSaspGroupTableEntry.setStatus("current")
_SlbSaspGroupName_Type = SnmpAdminString
_SlbSaspGroupName_Object = MibTableColumn
slbSaspGroupName = _SlbSaspGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 14, 1, 1, 1),
    _SlbSaspGroupName_Type()
)
slbSaspGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbSaspGroupName.setStatus("current")
_SlbSaspGroupRowStatus_Type = RowStatus
_SlbSaspGroupRowStatus_Object = MibTableColumn
slbSaspGroupRowStatus = _SlbSaspGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 14, 1, 1, 2),
    _SlbSaspGroupRowStatus_Type()
)
slbSaspGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbSaspGroupRowStatus.setStatus("current")
_SlbSaspMembers_ObjectIdentity = ObjectIdentity
slbSaspMembers = _SlbSaspMembers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 15)
)
_SlbSaspMemberTable_Object = MibTable
slbSaspMemberTable = _SlbSaspMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 15, 1)
)
if mibBuilder.loadTexts:
    slbSaspMemberTable.setStatus("current")
_SlbSaspMemberTableEntry_Object = MibTableRow
slbSaspMemberTableEntry = _SlbSaspMemberTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 15, 1, 1)
)
slbSaspMemberTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-MIB", "slbSaspAgentIpAddressType"),
    (0, "CISCO-SLB-MIB", "slbSaspAgentIpAddress"),
    (0, "CISCO-SLB-MIB", "slbSaspAgentPort"),
    (0, "CISCO-SLB-MIB", "slbSaspGroupName"),
    (0, "CISCO-SLB-MIB", "slbSaspMemberIpAddressType"),
    (0, "CISCO-SLB-MIB", "slbSaspMemberIpAddress"),
    (0, "CISCO-SLB-MIB", "slbSaspMemberPort"),
    (0, "CISCO-SLB-MIB", "slbSaspMemberProtocol"),
)
if mibBuilder.loadTexts:
    slbSaspMemberTableEntry.setStatus("current")
_SlbSaspMemberIpAddressType_Type = InetAddressType
_SlbSaspMemberIpAddressType_Object = MibTableColumn
slbSaspMemberIpAddressType = _SlbSaspMemberIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 15, 1, 1, 1),
    _SlbSaspMemberIpAddressType_Type()
)
slbSaspMemberIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbSaspMemberIpAddressType.setStatus("current")
_SlbSaspMemberIpAddress_Type = InetAddress
_SlbSaspMemberIpAddress_Object = MibTableColumn
slbSaspMemberIpAddress = _SlbSaspMemberIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 15, 1, 1, 2),
    _SlbSaspMemberIpAddress_Type()
)
slbSaspMemberIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbSaspMemberIpAddress.setStatus("current")
_SlbSaspMemberPort_Type = InetPortNumber
_SlbSaspMemberPort_Object = MibTableColumn
slbSaspMemberPort = _SlbSaspMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 15, 1, 1, 3),
    _SlbSaspMemberPort_Type()
)
slbSaspMemberPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbSaspMemberPort.setStatus("current")
_SlbSaspMemberProtocol_Type = CiscoIpProtocol
_SlbSaspMemberProtocol_Object = MibTableColumn
slbSaspMemberProtocol = _SlbSaspMemberProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 15, 1, 1, 4),
    _SlbSaspMemberProtocol_Type()
)
slbSaspMemberProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbSaspMemberProtocol.setStatus("current")


class _SlbSaspMemberSaspWeight_Type(Unsigned32):
    """Custom type slbSaspMemberSaspWeight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlbSaspMemberSaspWeight_Type.__name__ = "Unsigned32"
_SlbSaspMemberSaspWeight_Object = MibTableColumn
slbSaspMemberSaspWeight = _SlbSaspMemberSaspWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 15, 1, 1, 5),
    _SlbSaspMemberSaspWeight_Type()
)
slbSaspMemberSaspWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSaspMemberSaspWeight.setStatus("current")
_SlbSaspMemberConfidentWeight_Type = TruthValue
_SlbSaspMemberConfidentWeight_Object = MibTableColumn
slbSaspMemberConfidentWeight = _SlbSaspMemberConfidentWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 15, 1, 1, 6),
    _SlbSaspMemberConfidentWeight_Type()
)
slbSaspMemberConfidentWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSaspMemberConfidentWeight.setStatus("current")


class _SlbSaspMemberConvertedWeight_Type(Unsigned32):
    """Custom type slbSaspMemberConvertedWeight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlbSaspMemberConvertedWeight_Type.__name__ = "Unsigned32"
_SlbSaspMemberConvertedWeight_Object = MibTableColumn
slbSaspMemberConvertedWeight = _SlbSaspMemberConvertedWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 15, 1, 1, 7),
    _SlbSaspMemberConvertedWeight_Type()
)
slbSaspMemberConvertedWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSaspMemberConvertedWeight.setStatus("current")


class _SlbSaspMemberDefaultWeight_Type(Unsigned32):
    """Custom type slbSaspMemberDefaultWeight based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlbSaspMemberDefaultWeight_Type.__name__ = "Unsigned32"
_SlbSaspMemberDefaultWeight_Object = MibTableColumn
slbSaspMemberDefaultWeight = _SlbSaspMemberDefaultWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 15, 1, 1, 8),
    _SlbSaspMemberDefaultWeight_Type()
)
slbSaspMemberDefaultWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbSaspMemberDefaultWeight.setStatus("current")
_SlbSaspMemberWeightChanges_Type = Counter32
_SlbSaspMemberWeightChanges_Object = MibTableColumn
slbSaspMemberWeightChanges = _SlbSaspMemberWeightChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 15, 1, 1, 9),
    _SlbSaspMemberWeightChanges_Type()
)
slbSaspMemberWeightChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSaspMemberWeightChanges.setStatus("current")
_SlbSaspMemberLastWeightChange_Type = DateAndTime
_SlbSaspMemberLastWeightChange_Object = MibTableColumn
slbSaspMemberLastWeightChange = _SlbSaspMemberLastWeightChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 15, 1, 1, 10),
    _SlbSaspMemberLastWeightChange_Type()
)
slbSaspMemberLastWeightChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSaspMemberLastWeightChange.setStatus("current")
_SlbSaspMemberRowStatus_Type = RowStatus
_SlbSaspMemberRowStatus_Object = MibTableColumn
slbSaspMemberRowStatus = _SlbSaspMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 15, 1, 1, 11),
    _SlbSaspMemberRowStatus_Type()
)
slbSaspMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbSaspMemberRowStatus.setStatus("current")
_SlbSaspStats_ObjectIdentity = ObjectIdentity
slbSaspStats = _SlbSaspStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 16)
)
_SlbSaspStatsTable_Object = MibTable
slbSaspStatsTable = _SlbSaspStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 16, 1)
)
if mibBuilder.loadTexts:
    slbSaspStatsTable.setStatus("current")
_SlbSaspStatsTableEntry_Object = MibTableRow
slbSaspStatsTableEntry = _SlbSaspStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 16, 1, 1)
)
slbSaspStatsTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-MIB", "slbSaspAgentIpAddressType"),
    (0, "CISCO-SLB-MIB", "slbSaspAgentIpAddress"),
    (0, "CISCO-SLB-MIB", "slbSaspAgentPort"),
)
if mibBuilder.loadTexts:
    slbSaspStatsTableEntry.setStatus("current")
_SlbSaspStatsTxRegMsgs_Type = Counter32
_SlbSaspStatsTxRegMsgs_Object = MibTableColumn
slbSaspStatsTxRegMsgs = _SlbSaspStatsTxRegMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 16, 1, 1, 1),
    _SlbSaspStatsTxRegMsgs_Type()
)
slbSaspStatsTxRegMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSaspStatsTxRegMsgs.setStatus("current")
_SlbSaspStatsTxDeregMsgs_Type = Counter32
_SlbSaspStatsTxDeregMsgs_Object = MibTableColumn
slbSaspStatsTxDeregMsgs = _SlbSaspStatsTxDeregMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 16, 1, 1, 2),
    _SlbSaspStatsTxDeregMsgs_Type()
)
slbSaspStatsTxDeregMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSaspStatsTxDeregMsgs.setStatus("current")
_SlbSaspStatsTxGetWeightMsgs_Type = Counter32
_SlbSaspStatsTxGetWeightMsgs_Object = MibTableColumn
slbSaspStatsTxGetWeightMsgs = _SlbSaspStatsTxGetWeightMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 16, 1, 1, 3),
    _SlbSaspStatsTxGetWeightMsgs_Type()
)
slbSaspStatsTxGetWeightMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSaspStatsTxGetWeightMsgs.setStatus("current")
_SlbSaspStatsTxSetLBStateMsgs_Type = Counter32
_SlbSaspStatsTxSetLBStateMsgs_Object = MibTableColumn
slbSaspStatsTxSetLBStateMsgs = _SlbSaspStatsTxSetLBStateMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 16, 1, 1, 4),
    _SlbSaspStatsTxSetLBStateMsgs_Type()
)
slbSaspStatsTxSetLBStateMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSaspStatsTxSetLBStateMsgs.setStatus("current")
_SlbSaspStatsTxSetMemStateMsgs_Type = Counter32
_SlbSaspStatsTxSetMemStateMsgs_Object = MibTableColumn
slbSaspStatsTxSetMemStateMsgs = _SlbSaspStatsTxSetMemStateMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 16, 1, 1, 5),
    _SlbSaspStatsTxSetMemStateMsgs_Type()
)
slbSaspStatsTxSetMemStateMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSaspStatsTxSetMemStateMsgs.setStatus("current")
_SlbSaspStatsRxSendWeightMsgs_Type = Counter32
_SlbSaspStatsRxSendWeightMsgs_Object = MibTableColumn
slbSaspStatsRxSendWeightMsgs = _SlbSaspStatsRxSendWeightMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 16, 1, 1, 6),
    _SlbSaspStatsRxSendWeightMsgs_Type()
)
slbSaspStatsRxSendWeightMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSaspStatsRxSendWeightMsgs.setStatus("current")
_SlbSaspStatsRxRegMsgs_Type = Counter32
_SlbSaspStatsRxRegMsgs_Object = MibTableColumn
slbSaspStatsRxRegMsgs = _SlbSaspStatsRxRegMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 16, 1, 1, 7),
    _SlbSaspStatsRxRegMsgs_Type()
)
slbSaspStatsRxRegMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSaspStatsRxRegMsgs.setStatus("current")
_SlbSaspStatsRxDeregMsgs_Type = Counter32
_SlbSaspStatsRxDeregMsgs_Object = MibTableColumn
slbSaspStatsRxDeregMsgs = _SlbSaspStatsRxDeregMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 16, 1, 1, 8),
    _SlbSaspStatsRxDeregMsgs_Type()
)
slbSaspStatsRxDeregMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSaspStatsRxDeregMsgs.setStatus("current")
_SlbSaspStatsRxGetWeightMsgs_Type = Counter32
_SlbSaspStatsRxGetWeightMsgs_Object = MibTableColumn
slbSaspStatsRxGetWeightMsgs = _SlbSaspStatsRxGetWeightMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 16, 1, 1, 9),
    _SlbSaspStatsRxGetWeightMsgs_Type()
)
slbSaspStatsRxGetWeightMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSaspStatsRxGetWeightMsgs.setStatus("current")
_SlbSaspStatsRxSetLBStateMsgs_Type = Counter32
_SlbSaspStatsRxSetLBStateMsgs_Object = MibTableColumn
slbSaspStatsRxSetLBStateMsgs = _SlbSaspStatsRxSetLBStateMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 16, 1, 1, 10),
    _SlbSaspStatsRxSetLBStateMsgs_Type()
)
slbSaspStatsRxSetLBStateMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSaspStatsRxSetLBStateMsgs.setStatus("current")
_SlbSaspStatsRxSetMemStateMsgs_Type = Counter32
_SlbSaspStatsRxSetMemStateMsgs_Object = MibTableColumn
slbSaspStatsRxSetMemStateMsgs = _SlbSaspStatsRxSetMemStateMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 1, 16, 1, 1, 11),
    _SlbSaspStatsRxSetMemStateMsgs_Type()
)
slbSaspStatsRxSetMemStateMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSaspStatsRxSetMemStateMsgs.setStatus("current")
_CiscoSlbMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoSlbMIBNotificationPrefix = _CiscoSlbMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 2)
)
_CiscoSlbMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoSlbMIBNotifications = _CiscoSlbMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 2, 0)
)
_CiscoSlbMIBConformance_ObjectIdentity = ObjectIdentity
ciscoSlbMIBConformance = _CiscoSlbMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3)
)
_CiscoSlbMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSlbMIBCompliances = _CiscoSlbMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 1)
)
_CiscoSlbMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSlbMIBGroups = _CiscoSlbMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2)
)

# Managed Objects groups

ciscoSlbStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 1)
)
ciscoSlbStatsGroup.setObjects(
      *(("CISCO-SLB-MIB", "slbStatsUnassistedSwitchingPkts"),
        ("CISCO-SLB-MIB", "slbStatsUnassistedSwitchingHCPks"),
        ("CISCO-SLB-MIB", "slbStatsAssistedSwitchingPkts"),
        ("CISCO-SLB-MIB", "slbStatsAssistedSwitchingHCPkts"),
        ("CISCO-SLB-MIB", "slbStatsCreatedConnections"),
        ("CISCO-SLB-MIB", "slbStatsCreatedHCConnections"),
        ("CISCO-SLB-MIB", "slbStatsEstablishedConnections"),
        ("CISCO-SLB-MIB", "slbStatsEstablishedHCConnections"),
        ("CISCO-SLB-MIB", "slbStatsDestroyedConnections"),
        ("CISCO-SLB-MIB", "slbStatsDestroyedHCConnections"),
        ("CISCO-SLB-MIB", "slbStatsReassignedConnections"),
        ("CISCO-SLB-MIB", "slbStatsReassignedHCConnections"),
        ("CISCO-SLB-MIB", "slbStatsZombies"),
        ("CISCO-SLB-MIB", "slbStatsHCZombies"))
)
if mibBuilder.loadTexts:
    ciscoSlbStatsGroup.setStatus("current")

ciscoSlbServerFarmsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 2)
)
ciscoSlbServerFarmsGroup.setObjects(
      *(("CISCO-SLB-MIB", "slbServerFarmPredictor"),
        ("CISCO-SLB-MIB", "slbServerFarmNat"),
        ("CISCO-SLB-MIB", "slbServerFarmNumberOfRealServers"),
        ("CISCO-SLB-MIB", "slbServerFarmBindId"),
        ("CISCO-SLB-MIB", "slbServerFarmRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoSlbServerFarmsGroup.setStatus("current")

ciscoSlbRealServersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 3)
)
ciscoSlbRealServersGroup.setObjects(
      *(("CISCO-SLB-MIB", "slbRealState"),
        ("CISCO-SLB-MIB", "slbRealNumberOfConnections"),
        ("CISCO-SLB-MIB", "slbRealNumberOfDummyConnections"),
        ("CISCO-SLB-MIB", "slbRealMaxConnections"),
        ("CISCO-SLB-MIB", "slbRealAdminWeight"),
        ("CISCO-SLB-MIB", "slbRealOperWeight"),
        ("CISCO-SLB-MIB", "slbRealMetric"),
        ("CISCO-SLB-MIB", "slbRealReassign"),
        ("CISCO-SLB-MIB", "slbRealRetryInterval"),
        ("CISCO-SLB-MIB", "slbRealFailedConnections"),
        ("CISCO-SLB-MIB", "slbRealFailedClients"),
        ("CISCO-SLB-MIB", "slbRealConsecutiveFails"),
        ("CISCO-SLB-MIB", "slbRealTotalFails"),
        ("CISCO-SLB-MIB", "slbRealRowStatus"),
        ("CISCO-SLB-MIB", "slbRealTotalConnections"),
        ("CISCO-SLB-MIB", "slbRealHCTotalConnections"))
)
if mibBuilder.loadTexts:
    ciscoSlbRealServersGroup.setStatus("current")

ciscoSlbVirtualServersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 4)
)
ciscoSlbVirtualServersGroup.setObjects(
      *(("CISCO-SLB-MIB", "slbVirtualServerState"),
        ("CISCO-SLB-MIB", "slbVirtualIndex"),
        ("CISCO-SLB-MIB", "slbVirtualIpAddress"),
        ("CISCO-SLB-MIB", "slbVirtualPort"),
        ("CISCO-SLB-MIB", "slbVirtualProtocol"),
        ("CISCO-SLB-MIB", "slbVirtualService"),
        ("CISCO-SLB-MIB", "slbVirtualAdvertise"),
        ("CISCO-SLB-MIB", "slbVirtualFarmName"),
        ("CISCO-SLB-MIB", "slbVirtualDelayTimer"),
        ("CISCO-SLB-MIB", "slbVirtualIdleTimer"),
        ("CISCO-SLB-MIB", "slbVirtualStickyTimer"),
        ("CISCO-SLB-MIB", "slbVirtualStickyGroup"),
        ("CISCO-SLB-MIB", "slbVirtualSynguardCount"),
        ("CISCO-SLB-MIB", "slbVirtualSynguardPeriod"),
        ("CISCO-SLB-MIB", "slbVirtualRowStatus"),
        ("CISCO-SLB-MIB", "slbVirtualNumberOfConnections"),
        ("CISCO-SLB-MIB", "slbVirtualTotalConnections"),
        ("CISCO-SLB-MIB", "slbVirtualHCTotalConnections"))
)
if mibBuilder.loadTexts:
    ciscoSlbVirtualServersGroup.setStatus("current")

ciscoSlbConnectionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 5)
)
ciscoSlbConnectionsGroup.setObjects(
      *(("CISCO-SLB-MIB", "slbConnectionState"),
        ("CISCO-SLB-MIB", "slbConnectionRealIpAddr"),
        ("CISCO-SLB-MIB", "slbConnectionServerPort"),
        ("CISCO-SLB-MIB", "slbConnectionNumCacheEntries"),
        ("CISCO-SLB-MIB", "slbConnectionSynCount"))
)
if mibBuilder.loadTexts:
    ciscoSlbConnectionsGroup.setStatus("current")

ciscoSlbVirtualClientsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 6)
)
ciscoSlbVirtualClientsGroup.setObjects(
      *(("CISCO-SLB-MIB", "slbVirtualClientExclude"),
        ("CISCO-SLB-MIB", "slbVirtualClientRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoSlbVirtualClientsGroup.setStatus("current")

ciscoSlbStickyObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 7)
)
ciscoSlbStickyObjectsGroup.setObjects(
      *(("CISCO-SLB-MIB", "slbStickyObjectRealIpAddress"),
        ("CISCO-SLB-MIB", "slbStickyObjectConnectionCount"),
        ("CISCO-SLB-MIB", "slbStickyObjectFtpControlCount"),
        ("CISCO-SLB-MIB", "slbStickyObjectRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoSlbStickyObjectsGroup.setStatus("current")

ciscoSlbDfpPasswordGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 8)
)
ciscoSlbDfpPasswordGroup.setObjects(
      *(("CISCO-SLB-MIB", "slbDfpPasswordPending"),
        ("CISCO-SLB-MIB", "slbDfpPasswordTimeout"),
        ("CISCO-SLB-MIB", "slbDfpPasswordRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoSlbDfpPasswordGroup.setStatus("current")

ciscoSlbDfpAgentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 9)
)
ciscoSlbDfpAgentGroup.setObjects(
      *(("CISCO-SLB-MIB", "slbDfpAgentState"),
        ("CISCO-SLB-MIB", "slbDfpAgentTimeout"),
        ("CISCO-SLB-MIB", "slbDfpAgentRetryCount"),
        ("CISCO-SLB-MIB", "slbDfpAgentInterval"),
        ("CISCO-SLB-MIB", "slbDfpAgentRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoSlbDfpAgentGroup.setStatus("current")

ciscoSlbDfpRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 10)
)
ciscoSlbDfpRealGroup.setObjects(
      *(("CISCO-SLB-MIB", "slbDfpRealWeight"),
        ("CISCO-SLB-MIB", "slbDfpRealRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoSlbDfpRealGroup.setStatus("current")

ciscoSlbNotifEnabledGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 11)
)
ciscoSlbNotifEnabledGroup.setObjects(
      *(("CISCO-SLB-MIB", "cSlbVirtStateChangeNotifEnabled"),
        ("CISCO-SLB-MIB", "cSlbRealStateChangeNotifEnabled"))
)
if mibBuilder.loadTexts:
    ciscoSlbNotifEnabledGroup.setStatus("deprecated")

ciscoSlbVirtualServersAddGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 12)
)
ciscoSlbVirtualServersAddGroup.setObjects(
    ("CISCO-SLB-MIB", "slbVirtualMask")
)
if mibBuilder.loadTexts:
    ciscoSlbVirtualServersAddGroup.setStatus("current")

ciscoSlbSaspGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 14)
)
ciscoSlbSaspGroup.setObjects(
      *(("CISCO-SLB-MIB", "slbSaspIdentifier"),
        ("CISCO-SLB-MIB", "slbSaspEnabled"),
        ("CISCO-SLB-MIB", "slbSaspHealth"),
        ("CISCO-SLB-MIB", "slbSaspRedundancy"),
        ("CISCO-SLB-MIB", "slbSaspMaxAgents"),
        ("CISCO-SLB-MIB", "slbSaspMaxLbWeight"))
)
if mibBuilder.loadTexts:
    ciscoSlbSaspGroup.setStatus("current")

ciscoSlbSaspAgentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 15)
)
ciscoSlbSaspAgentGroup.setObjects(
      *(("CISCO-SLB-MIB", "slbSaspAgentLabel"),
        ("CISCO-SLB-MIB", "slbSaspAgentState"),
        ("CISCO-SLB-MIB", "slbSaspAgentLastStateChange"),
        ("CISCO-SLB-MIB", "slbSaspAgentRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoSlbSaspAgentGroup.setStatus("current")

ciscoSlbSaspGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 16)
)
ciscoSlbSaspGroupGroup.setObjects(
    ("CISCO-SLB-MIB", "slbSaspGroupRowStatus")
)
if mibBuilder.loadTexts:
    ciscoSlbSaspGroupGroup.setStatus("current")

ciscoSlbSaspMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 17)
)
ciscoSlbSaspMemberGroup.setObjects(
      *(("CISCO-SLB-MIB", "slbSaspMemberSaspWeight"),
        ("CISCO-SLB-MIB", "slbSaspMemberConfidentWeight"),
        ("CISCO-SLB-MIB", "slbSaspMemberConvertedWeight"),
        ("CISCO-SLB-MIB", "slbSaspMemberDefaultWeight"),
        ("CISCO-SLB-MIB", "slbSaspMemberWeightChanges"),
        ("CISCO-SLB-MIB", "slbSaspMemberLastWeightChange"),
        ("CISCO-SLB-MIB", "slbSaspMemberRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoSlbSaspMemberGroup.setStatus("current")

ciscoSlbSaspStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 18)
)
ciscoSlbSaspStatsGroup.setObjects(
      *(("CISCO-SLB-MIB", "slbSaspStatsTxRegMsgs"),
        ("CISCO-SLB-MIB", "slbSaspStatsTxDeregMsgs"),
        ("CISCO-SLB-MIB", "slbSaspStatsTxGetWeightMsgs"),
        ("CISCO-SLB-MIB", "slbSaspStatsTxSetLBStateMsgs"),
        ("CISCO-SLB-MIB", "slbSaspStatsTxSetMemStateMsgs"),
        ("CISCO-SLB-MIB", "slbSaspStatsRxSendWeightMsgs"),
        ("CISCO-SLB-MIB", "slbSaspStatsRxRegMsgs"),
        ("CISCO-SLB-MIB", "slbSaspStatsRxDeregMsgs"),
        ("CISCO-SLB-MIB", "slbSaspStatsRxGetWeightMsgs"),
        ("CISCO-SLB-MIB", "slbSaspStatsRxSetLBStateMsgs"),
        ("CISCO-SLB-MIB", "slbSaspStatsRxSetMemStateMsgs"))
)
if mibBuilder.loadTexts:
    ciscoSlbSaspStatsGroup.setStatus("current")

ciscoSlbVServerInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 21)
)
ciscoSlbVServerInfoGroup.setObjects(
      *(("CISCO-SLB-MIB", "slbVServerClassMap"),
        ("CISCO-SLB-MIB", "slbVServerPolicyMap"),
        ("CISCO-SLB-MIB", "slbVServerState"),
        ("CISCO-SLB-MIB", "slbVServerStateChangeDescr"),
        ("CISCO-SLB-MIB", "slbVServerNumberOfConnections"),
        ("CISCO-SLB-MIB", "slbVServerTotalConnections"))
)
if mibBuilder.loadTexts:
    ciscoSlbVServerInfoGroup.setStatus("deprecated")

ciscoSlbVServerIPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 22)
)
ciscoSlbVServerIPGroup.setObjects(
      *(("CISCO-SLB-MIB", "slbVServerIpAddressType"),
        ("CISCO-SLB-MIB", "slbVServerIpAddress"),
        ("CISCO-SLB-MIB", "slbVServerIpMask"),
        ("CISCO-SLB-MIB", "slbVServerProtocol"),
        ("CISCO-SLB-MIB", "slbVServerPortLow"),
        ("CISCO-SLB-MIB", "slbVServerPortHigh"),
        ("CISCO-SLB-MIB", "slbVServerStorageType"),
        ("CISCO-SLB-MIB", "slbVServerRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoSlbVServerIPGroup.setStatus("current")

ciscoSlbVServerNotifEnabledGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 23)
)
ciscoSlbVServerNotifEnabledGroup.setObjects(
    ("CISCO-SLB-MIB", "cSlbVServerStateChangeNotifEnabled")
)
if mibBuilder.loadTexts:
    ciscoSlbVServerNotifEnabledGroup.setStatus("current")

ciscoSlbNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 25)
)
ciscoSlbNotifObjectsGroup.setObjects(
      *(("CISCO-SLB-MIB", "slbInetAddressType"),
        ("CISCO-SLB-MIB", "slbInetAddress"),
        ("CISCO-SLB-MIB", "slbName"),
        ("CISCO-SLB-MIB", "slbPort"))
)
if mibBuilder.loadTexts:
    ciscoSlbNotifObjectsGroup.setStatus("current")

ciscoSlbNotifEnabledGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 26)
)
ciscoSlbNotifEnabledGroupRev2.setObjects(
      *(("CISCO-SLB-MIB", "cSlbVirtualServerStateChangeNotifEnabled"),
        ("CISCO-SLB-MIB", "cSlbRealServerStateChangeNotifEnabled"))
)
if mibBuilder.loadTexts:
    ciscoSlbNotifEnabledGroupRev2.setStatus("current")

ciscoSlbVServerInfoGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 28)
)
ciscoSlbVServerInfoGroupRev1.setObjects(
      *(("CISCO-SLB-MIB", "slbVServerClassMap"),
        ("CISCO-SLB-MIB", "slbVServerPolicyMap"),
        ("CISCO-SLB-MIB", "slbVServerState"),
        ("CISCO-SLB-MIB", "slbVServerStateChangeDescr"),
        ("CISCO-SLB-MIB", "slbVServerNumberOfConnections"),
        ("CISCO-SLB-MIB", "slbVServerTotalConnections"),
        ("CISCO-SLB-MIB", "slbVServerDroppedConnections"),
        ("CISCO-SLB-MIB", "slbVServerClientPacketCounts"),
        ("CISCO-SLB-MIB", "slbVServerPacketCounts"),
        ("CISCO-SLB-MIB", "slbVServerClientByteCounts"),
        ("CISCO-SLB-MIB", "slbVServerByteCounts"),
        ("CISCO-SLB-MIB", "slbVServerMaxConnLimitDropCounts"),
        ("CISCO-SLB-MIB", "slbVServerConnRateLimitDropCounts"),
        ("CISCO-SLB-MIB", "slbVServerBWRateLimitDropCounts"))
)
if mibBuilder.loadTexts:
    ciscoSlbVServerInfoGroupRev1.setStatus("deprecated")

ciscoSlbVServerInfoGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 29)
)
ciscoSlbVServerInfoGroupRev2.setObjects(
      *(("CISCO-SLB-MIB", "slbVServerClassMap"),
        ("CISCO-SLB-MIB", "slbVServerPolicyMap"),
        ("CISCO-SLB-MIB", "slbVServerState"),
        ("CISCO-SLB-MIB", "slbVServerStateChangeDescr"),
        ("CISCO-SLB-MIB", "slbVServerNumberOfConnections"),
        ("CISCO-SLB-MIB", "slbVServerTotalConnections"),
        ("CISCO-SLB-MIB", "slbVServerDroppedConnections"),
        ("CISCO-SLB-MIB", "slbVServerClientPacketCounts"),
        ("CISCO-SLB-MIB", "slbVServerPacketCounts"),
        ("CISCO-SLB-MIB", "slbVServerClientByteCounts"),
        ("CISCO-SLB-MIB", "slbVServerByteCounts"),
        ("CISCO-SLB-MIB", "slbVServerMaxConnLimitDropCounts"),
        ("CISCO-SLB-MIB", "slbVServerConnRateLimitDropCounts"),
        ("CISCO-SLB-MIB", "slbVServerBandWidthRateLimitDropCounts"),
        ("CISCO-SLB-MIB", "slbVServerL4Decisions"),
        ("CISCO-SLB-MIB", "slbVServerL7Decisions"),
        ("CISCO-SLB-MIB", "slbVServerEstablishedConnections"))
)
if mibBuilder.loadTexts:
    ciscoSlbVServerInfoGroupRev2.setStatus("current")


# Notification objects

ciscoSlbVirtualStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 2, 0, 1)
)
ciscoSlbVirtualStateChange.setObjects(
    ("CISCO-SLB-MIB", "slbVirtualServerState")
)
if mibBuilder.loadTexts:
    ciscoSlbVirtualStateChange.setStatus(
        "deprecated"
    )

ciscoSlbRealStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 2, 0, 2)
)
ciscoSlbRealStateChange.setObjects(
    ("CISCO-SLB-MIB", "slbRealState")
)
if mibBuilder.loadTexts:
    ciscoSlbRealStateChange.setStatus(
        "deprecated"
    )

ciscoSlbSaspStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 2, 0, 3)
)
ciscoSlbSaspStateChange.setObjects(
    ("CISCO-SLB-MIB", "slbSaspEnabled")
)
if mibBuilder.loadTexts:
    ciscoSlbSaspStateChange.setStatus(
        "current"
    )

ciscoSlbSaspAgentStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 2, 0, 4)
)
ciscoSlbSaspAgentStateChange.setObjects(
    ("CISCO-SLB-MIB", "slbSaspAgentState")
)
if mibBuilder.loadTexts:
    ciscoSlbSaspAgentStateChange.setStatus(
        "current"
    )

ciscoSlbVServerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 2, 0, 5)
)
ciscoSlbVServerStateChange.setObjects(
      *(("CISCO-SLB-MIB", "slbVServerState"),
        ("CISCO-SLB-MIB", "slbVServerStateChangeDescr"),
        ("CISCO-SLB-MIB", "slbVServerClassMap"),
        ("CISCO-SLB-MIB", "slbVServerPolicyMap"))
)
if mibBuilder.loadTexts:
    ciscoSlbVServerStateChange.setStatus(
        "current"
    )

ciscoSlbVServerVIPStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 2, 0, 6)
)
ciscoSlbVServerVIPStateChange.setObjects(
      *(("CISCO-SLB-MIB", "slbVServerState"),
        ("CISCO-SLB-MIB", "slbVServerStateChangeDescr"),
        ("CISCO-SLB-MIB", "slbVServerClassMap"),
        ("CISCO-SLB-MIB", "slbVServerPolicyMap"),
        ("CISCO-SLB-MIB", "slbVServerIpAddressType"),
        ("CISCO-SLB-MIB", "slbVServerIpAddress"),
        ("CISCO-SLB-MIB", "slbVServerProtocol"))
)
if mibBuilder.loadTexts:
    ciscoSlbVServerVIPStateChange.setStatus(
        "current"
    )

ciscoSlbVirtualServerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 2, 0, 7)
)
ciscoSlbVirtualServerStateChange.setObjects(
      *(("ENTITY-MIB", "entPhysicalParentRelPos"),
        ("CISCO-SLB-MIB", "slbVirtualServerState"),
        ("CISCO-SLB-MIB", "slbVirtualIpAddress"),
        ("CISCO-SLB-MIB", "slbVirtualProtocol"),
        ("CISCO-SLB-MIB", "slbVirtualPort"),
        ("CISCO-SLB-MIB", "slbName"))
)
if mibBuilder.loadTexts:
    ciscoSlbVirtualServerStateChange.setStatus(
        "current"
    )

ciscoSlbRealServerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 2, 0, 8)
)
ciscoSlbRealServerStateChange.setObjects(
      *(("ENTITY-MIB", "entPhysicalParentRelPos"),
        ("CISCO-SLB-MIB", "slbRealState"),
        ("CISCO-SLB-MIB", "slbInetAddressType"),
        ("CISCO-SLB-MIB", "slbInetAddress"),
        ("CISCO-SLB-MIB", "slbPort"),
        ("CISCO-SLB-MIB", "slbName"))
)
if mibBuilder.loadTexts:
    ciscoSlbRealServerStateChange.setStatus(
        "current"
    )


# Notifications groups

ciscoSlbNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 13)
)
ciscoSlbNotifGroup.setObjects(
      *(("CISCO-SLB-MIB", "ciscoSlbVirtualStateChange"),
        ("CISCO-SLB-MIB", "ciscoSlbRealStateChange"))
)
if mibBuilder.loadTexts:
    ciscoSlbNotifGroup.setStatus(
        "deprecated"
    )

ciscoSlbSaspNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 19)
)
ciscoSlbSaspNotifGroup.setObjects(
      *(("CISCO-SLB-MIB", "ciscoSlbSaspStateChange"),
        ("CISCO-SLB-MIB", "ciscoSlbSaspAgentStateChange"))
)
if mibBuilder.loadTexts:
    ciscoSlbSaspNotifGroup.setStatus(
        "current"
    )

ciscoSlbVServerNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 24)
)
ciscoSlbVServerNotifGroup.setObjects(
      *(("CISCO-SLB-MIB", "ciscoSlbVServerStateChange"),
        ("CISCO-SLB-MIB", "ciscoSlbVServerVIPStateChange"))
)
if mibBuilder.loadTexts:
    ciscoSlbVServerNotifGroup.setStatus(
        "current"
    )

ciscoSlbNotifGroupRev2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 2, 27)
)
ciscoSlbNotifGroupRev2.setObjects(
      *(("CISCO-SLB-MIB", "ciscoSlbVirtualServerStateChange"),
        ("CISCO-SLB-MIB", "ciscoSlbRealServerStateChange"))
)
if mibBuilder.loadTexts:
    ciscoSlbNotifGroupRev2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoSlbMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSlbMIBCompliance.setStatus(
        "deprecated"
    )

ciscoSlbMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoSlbMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoSlbMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoSlbMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoSlbMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoSlbMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoSlbMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoSlbMIBComplianceRev4.setStatus(
        "deprecated"
    )

ciscoSlbMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoSlbMIBComplianceRev5.setStatus(
        "deprecated"
    )

ciscoSlbMIBComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 161, 3, 1, 7)
)
if mibBuilder.loadTexts:
    ciscoSlbMIBComplianceRev6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SLB-MIB",
    **{"SlbServerString": SlbServerString,
       "SlbPasswordString": SlbPasswordString,
       "SlbConnectionState": SlbConnectionState,
       "SlbPredictor": SlbPredictor,
       "SlbRealServerState": SlbRealServerState,
       "SlbVirtualServState": SlbVirtualServState,
       "SlbVirtualService": SlbVirtualService,
       "SlbDfpAgentState": SlbDfpAgentState,
       "SlbSaspLBHealth": SlbSaspLBHealth,
       "SlbSaspRedundancy": SlbSaspRedundancy,
       "SlbSaspAgentState": SlbSaspAgentState,
       "SlbNatSetting": SlbNatSetting,
       "ciscoSlbMIB": ciscoSlbMIB,
       "ciscoSlbMIBObjects": ciscoSlbMIBObjects,
       "slbStats": slbStats,
       "slbStatsTable": slbStatsTable,
       "slbStatsTableEntry": slbStatsTableEntry,
       "slbEntity": slbEntity,
       "slbStatsUnassistedSwitchingPkts": slbStatsUnassistedSwitchingPkts,
       "slbStatsUnassistedSwitchingHCPks": slbStatsUnassistedSwitchingHCPks,
       "slbStatsAssistedSwitchingPkts": slbStatsAssistedSwitchingPkts,
       "slbStatsAssistedSwitchingHCPkts": slbStatsAssistedSwitchingHCPkts,
       "slbStatsCreatedConnections": slbStatsCreatedConnections,
       "slbStatsCreatedHCConnections": slbStatsCreatedHCConnections,
       "slbStatsEstablishedConnections": slbStatsEstablishedConnections,
       "slbStatsEstablishedHCConnections": slbStatsEstablishedHCConnections,
       "slbStatsDestroyedConnections": slbStatsDestroyedConnections,
       "slbStatsDestroyedHCConnections": slbStatsDestroyedHCConnections,
       "slbStatsReassignedConnections": slbStatsReassignedConnections,
       "slbStatsReassignedHCConnections": slbStatsReassignedHCConnections,
       "slbStatsZombies": slbStatsZombies,
       "slbStatsHCZombies": slbStatsHCZombies,
       "slbServerFarms": slbServerFarms,
       "slbServerFarmTable": slbServerFarmTable,
       "slbServerFarmTableEntry": slbServerFarmTableEntry,
       "slbServerFarmName": slbServerFarmName,
       "slbServerFarmPredictor": slbServerFarmPredictor,
       "slbServerFarmNat": slbServerFarmNat,
       "slbServerFarmNumberOfRealServers": slbServerFarmNumberOfRealServers,
       "slbServerFarmBindId": slbServerFarmBindId,
       "slbServerFarmRowStatus": slbServerFarmRowStatus,
       "slbRealServers": slbRealServers,
       "slbRealTable": slbRealTable,
       "slbRealTableEntry": slbRealTableEntry,
       "slbRealServerFarmName": slbRealServerFarmName,
       "slbRealIpAddress": slbRealIpAddress,
       "slbRealPort": slbRealPort,
       "slbRealState": slbRealState,
       "slbRealNumberOfConnections": slbRealNumberOfConnections,
       "slbRealNumberOfDummyConnections": slbRealNumberOfDummyConnections,
       "slbRealMaxConnections": slbRealMaxConnections,
       "slbRealAdminWeight": slbRealAdminWeight,
       "slbRealOperWeight": slbRealOperWeight,
       "slbRealMetric": slbRealMetric,
       "slbRealReassign": slbRealReassign,
       "slbRealRetryInterval": slbRealRetryInterval,
       "slbRealFailedConnections": slbRealFailedConnections,
       "slbRealFailedClients": slbRealFailedClients,
       "slbRealConsecutiveFails": slbRealConsecutiveFails,
       "slbRealTotalFails": slbRealTotalFails,
       "slbRealRowStatus": slbRealRowStatus,
       "slbRealTotalConnections": slbRealTotalConnections,
       "slbRealHCTotalConnections": slbRealHCTotalConnections,
       "slbVirtualServers": slbVirtualServers,
       "slbVirtualServerTable": slbVirtualServerTable,
       "slbVirtualServerTableEntry": slbVirtualServerTableEntry,
       "slbVirtualServerName": slbVirtualServerName,
       "slbVirtualServerState": slbVirtualServerState,
       "slbVirtualIndex": slbVirtualIndex,
       "slbVirtualIpAddress": slbVirtualIpAddress,
       "slbVirtualPort": slbVirtualPort,
       "slbVirtualProtocol": slbVirtualProtocol,
       "slbVirtualService": slbVirtualService,
       "slbVirtualAdvertise": slbVirtualAdvertise,
       "slbVirtualFarmName": slbVirtualFarmName,
       "slbVirtualDelayTimer": slbVirtualDelayTimer,
       "slbVirtualIdleTimer": slbVirtualIdleTimer,
       "slbVirtualStickyTimer": slbVirtualStickyTimer,
       "slbVirtualStickyGroup": slbVirtualStickyGroup,
       "slbVirtualSynguardCount": slbVirtualSynguardCount,
       "slbVirtualSynguardPeriod": slbVirtualSynguardPeriod,
       "slbVirtualRowStatus": slbVirtualRowStatus,
       "slbVirtualNumberOfConnections": slbVirtualNumberOfConnections,
       "slbVirtualTotalConnections": slbVirtualTotalConnections,
       "slbVirtualHCTotalConnections": slbVirtualHCTotalConnections,
       "slbVirtualMask": slbVirtualMask,
       "slbVServerInfoTable": slbVServerInfoTable,
       "slbVServerInfoTableEntry": slbVServerInfoTableEntry,
       "slbVServerIndex": slbVServerIndex,
       "slbVServerClassMap": slbVServerClassMap,
       "slbVServerPolicyMap": slbVServerPolicyMap,
       "slbVServerState": slbVServerState,
       "slbVServerStateChangeDescr": slbVServerStateChangeDescr,
       "slbVServerNumberOfConnections": slbVServerNumberOfConnections,
       "slbVServerTotalConnections": slbVServerTotalConnections,
       "slbVServerDroppedConnections": slbVServerDroppedConnections,
       "slbVServerClientPacketCounts": slbVServerClientPacketCounts,
       "slbVServerPacketCounts": slbVServerPacketCounts,
       "slbVServerClientByteCounts": slbVServerClientByteCounts,
       "slbVServerByteCounts": slbVServerByteCounts,
       "slbVServerMaxConnLimitDropCounts": slbVServerMaxConnLimitDropCounts,
       "slbVServerConnRateLimitDropCounts": slbVServerConnRateLimitDropCounts,
       "slbVServerBWRateLimitDropCounts": slbVServerBWRateLimitDropCounts,
       "slbVServerBandWidthRateLimitDropCounts": slbVServerBandWidthRateLimitDropCounts,
       "slbVServerL4Decisions": slbVServerL4Decisions,
       "slbVServerL7Decisions": slbVServerL7Decisions,
       "slbVServerEstablishedConnections": slbVServerEstablishedConnections,
       "slbVServerIPTable": slbVServerIPTable,
       "slbVServerIPTableEntry": slbVServerIPTableEntry,
       "slbVServerObjectIndex": slbVServerObjectIndex,
       "slbVServerIpAddressType": slbVServerIpAddressType,
       "slbVServerIpAddress": slbVServerIpAddress,
       "slbVServerIpMask": slbVServerIpMask,
       "slbVServerProtocol": slbVServerProtocol,
       "slbVServerPortLow": slbVServerPortLow,
       "slbVServerPortHigh": slbVServerPortHigh,
       "slbVServerStorageType": slbVServerStorageType,
       "slbVServerRowStatus": slbVServerRowStatus,
       "slbConnections": slbConnections,
       "slbConnectionTable": slbConnectionTable,
       "slbConnectionTableEntry": slbConnectionTableEntry,
       "slbConnectionIndex": slbConnectionIndex,
       "slbConnectionVirtualIpAddress": slbConnectionVirtualIpAddress,
       "slbConnectionVirtualPort": slbConnectionVirtualPort,
       "slbConnectionProtocol": slbConnectionProtocol,
       "slbConnectionClientIpAddr": slbConnectionClientIpAddr,
       "slbConnectionClientPort": slbConnectionClientPort,
       "slbConnectionState": slbConnectionState,
       "slbConnectionRealIpAddr": slbConnectionRealIpAddr,
       "slbConnectionServerPort": slbConnectionServerPort,
       "slbConnectionNumCacheEntries": slbConnectionNumCacheEntries,
       "slbConnectionSynCount": slbConnectionSynCount,
       "slbVirtualClients": slbVirtualClients,
       "slbVirtualClientTable": slbVirtualClientTable,
       "slbVirtualClientTableEntry": slbVirtualClientTableEntry,
       "slbVirtualClientIpAddress": slbVirtualClientIpAddress,
       "slbVirtualClientMask": slbVirtualClientMask,
       "slbVirtualClientExclude": slbVirtualClientExclude,
       "slbVirtualClientRowStatus": slbVirtualClientRowStatus,
       "slbStickyObjects": slbStickyObjects,
       "slbStickyObjectTable": slbStickyObjectTable,
       "slbStickyObjectTableEntry": slbStickyObjectTableEntry,
       "slbStickyObjectGroupId": slbStickyObjectGroupId,
       "slbStickyObjectClientIpAddress": slbStickyObjectClientIpAddress,
       "slbStickyObjectRealIpAddress": slbStickyObjectRealIpAddress,
       "slbStickyObjectConnectionCount": slbStickyObjectConnectionCount,
       "slbStickyObjectFtpControlCount": slbStickyObjectFtpControlCount,
       "slbStickyObjectRowStatus": slbStickyObjectRowStatus,
       "slbNotificationObjects": slbNotificationObjects,
       "cSlbVirtStateChangeNotifEnabled": cSlbVirtStateChangeNotifEnabled,
       "cSlbRealStateChangeNotifEnabled": cSlbRealStateChangeNotifEnabled,
       "cSlbVServerStateChangeNotifEnabled": cSlbVServerStateChangeNotifEnabled,
       "cSlbVirtualServerStateChangeNotifEnabled": cSlbVirtualServerStateChangeNotifEnabled,
       "cSlbRealServerStateChangeNotifEnabled": cSlbRealServerStateChangeNotifEnabled,
       "slbInetAddressType": slbInetAddressType,
       "slbInetAddress": slbInetAddress,
       "slbName": slbName,
       "slbPort": slbPort,
       "slbDfpPassword": slbDfpPassword,
       "slbDfpPasswordTable": slbDfpPasswordTable,
       "slbDfpPasswordTableEntry": slbDfpPasswordTableEntry,
       "slbDfpPasswordPending": slbDfpPasswordPending,
       "slbDfpPasswordTimeout": slbDfpPasswordTimeout,
       "slbDfpPasswordRowStatus": slbDfpPasswordRowStatus,
       "slbDfpAgents": slbDfpAgents,
       "slbDfpAgentTable": slbDfpAgentTable,
       "slbDfpAgentTableEntry": slbDfpAgentTableEntry,
       "slbDfpAgentIpAddress": slbDfpAgentIpAddress,
       "slbDfpAgentPort": slbDfpAgentPort,
       "slbDfpAgentState": slbDfpAgentState,
       "slbDfpAgentTimeout": slbDfpAgentTimeout,
       "slbDfpAgentRetryCount": slbDfpAgentRetryCount,
       "slbDfpAgentInterval": slbDfpAgentInterval,
       "slbDfpAgentRowStatus": slbDfpAgentRowStatus,
       "slbDfpReal": slbDfpReal,
       "slbDfpRealTable": slbDfpRealTable,
       "slbDfpRealTableEntry": slbDfpRealTableEntry,
       "slbDfpRealIpAddress": slbDfpRealIpAddress,
       "slbDfpRealProtocol": slbDfpRealProtocol,
       "slbDfpRealPort": slbDfpRealPort,
       "slbDfpRealBindId": slbDfpRealBindId,
       "slbDfpRealWeight": slbDfpRealWeight,
       "slbDfpRealRowStatus": slbDfpRealRowStatus,
       "slbSasp": slbSasp,
       "slbSaspTable": slbSaspTable,
       "slbSaspTableEntry": slbSaspTableEntry,
       "slbSaspIdentifier": slbSaspIdentifier,
       "slbSaspEnabled": slbSaspEnabled,
       "slbSaspHealth": slbSaspHealth,
       "slbSaspRedundancy": slbSaspRedundancy,
       "slbSaspMaxAgents": slbSaspMaxAgents,
       "slbSaspMaxLbWeight": slbSaspMaxLbWeight,
       "slbSaspAgents": slbSaspAgents,
       "slbSaspAgentTable": slbSaspAgentTable,
       "slbSaspAgentTableEntry": slbSaspAgentTableEntry,
       "slbSaspAgentIpAddressType": slbSaspAgentIpAddressType,
       "slbSaspAgentIpAddress": slbSaspAgentIpAddress,
       "slbSaspAgentPort": slbSaspAgentPort,
       "slbSaspAgentLabel": slbSaspAgentLabel,
       "slbSaspAgentState": slbSaspAgentState,
       "slbSaspAgentLastStateChange": slbSaspAgentLastStateChange,
       "slbSaspAgentRowStatus": slbSaspAgentRowStatus,
       "slbSaspGroups": slbSaspGroups,
       "slbSaspGroupTable": slbSaspGroupTable,
       "slbSaspGroupTableEntry": slbSaspGroupTableEntry,
       "slbSaspGroupName": slbSaspGroupName,
       "slbSaspGroupRowStatus": slbSaspGroupRowStatus,
       "slbSaspMembers": slbSaspMembers,
       "slbSaspMemberTable": slbSaspMemberTable,
       "slbSaspMemberTableEntry": slbSaspMemberTableEntry,
       "slbSaspMemberIpAddressType": slbSaspMemberIpAddressType,
       "slbSaspMemberIpAddress": slbSaspMemberIpAddress,
       "slbSaspMemberPort": slbSaspMemberPort,
       "slbSaspMemberProtocol": slbSaspMemberProtocol,
       "slbSaspMemberSaspWeight": slbSaspMemberSaspWeight,
       "slbSaspMemberConfidentWeight": slbSaspMemberConfidentWeight,
       "slbSaspMemberConvertedWeight": slbSaspMemberConvertedWeight,
       "slbSaspMemberDefaultWeight": slbSaspMemberDefaultWeight,
       "slbSaspMemberWeightChanges": slbSaspMemberWeightChanges,
       "slbSaspMemberLastWeightChange": slbSaspMemberLastWeightChange,
       "slbSaspMemberRowStatus": slbSaspMemberRowStatus,
       "slbSaspStats": slbSaspStats,
       "slbSaspStatsTable": slbSaspStatsTable,
       "slbSaspStatsTableEntry": slbSaspStatsTableEntry,
       "slbSaspStatsTxRegMsgs": slbSaspStatsTxRegMsgs,
       "slbSaspStatsTxDeregMsgs": slbSaspStatsTxDeregMsgs,
       "slbSaspStatsTxGetWeightMsgs": slbSaspStatsTxGetWeightMsgs,
       "slbSaspStatsTxSetLBStateMsgs": slbSaspStatsTxSetLBStateMsgs,
       "slbSaspStatsTxSetMemStateMsgs": slbSaspStatsTxSetMemStateMsgs,
       "slbSaspStatsRxSendWeightMsgs": slbSaspStatsRxSendWeightMsgs,
       "slbSaspStatsRxRegMsgs": slbSaspStatsRxRegMsgs,
       "slbSaspStatsRxDeregMsgs": slbSaspStatsRxDeregMsgs,
       "slbSaspStatsRxGetWeightMsgs": slbSaspStatsRxGetWeightMsgs,
       "slbSaspStatsRxSetLBStateMsgs": slbSaspStatsRxSetLBStateMsgs,
       "slbSaspStatsRxSetMemStateMsgs": slbSaspStatsRxSetMemStateMsgs,
       "ciscoSlbMIBNotificationPrefix": ciscoSlbMIBNotificationPrefix,
       "ciscoSlbMIBNotifications": ciscoSlbMIBNotifications,
       "ciscoSlbVirtualStateChange": ciscoSlbVirtualStateChange,
       "ciscoSlbRealStateChange": ciscoSlbRealStateChange,
       "ciscoSlbSaspStateChange": ciscoSlbSaspStateChange,
       "ciscoSlbSaspAgentStateChange": ciscoSlbSaspAgentStateChange,
       "ciscoSlbVServerStateChange": ciscoSlbVServerStateChange,
       "ciscoSlbVServerVIPStateChange": ciscoSlbVServerVIPStateChange,
       "ciscoSlbVirtualServerStateChange": ciscoSlbVirtualServerStateChange,
       "ciscoSlbRealServerStateChange": ciscoSlbRealServerStateChange,
       "ciscoSlbMIBConformance": ciscoSlbMIBConformance,
       "ciscoSlbMIBCompliances": ciscoSlbMIBCompliances,
       "ciscoSlbMIBCompliance": ciscoSlbMIBCompliance,
       "ciscoSlbMIBComplianceRev1": ciscoSlbMIBComplianceRev1,
       "ciscoSlbMIBComplianceRev2": ciscoSlbMIBComplianceRev2,
       "ciscoSlbMIBComplianceRev3": ciscoSlbMIBComplianceRev3,
       "ciscoSlbMIBComplianceRev4": ciscoSlbMIBComplianceRev4,
       "ciscoSlbMIBComplianceRev5": ciscoSlbMIBComplianceRev5,
       "ciscoSlbMIBComplianceRev6": ciscoSlbMIBComplianceRev6,
       "ciscoSlbMIBGroups": ciscoSlbMIBGroups,
       "ciscoSlbStatsGroup": ciscoSlbStatsGroup,
       "ciscoSlbServerFarmsGroup": ciscoSlbServerFarmsGroup,
       "ciscoSlbRealServersGroup": ciscoSlbRealServersGroup,
       "ciscoSlbVirtualServersGroup": ciscoSlbVirtualServersGroup,
       "ciscoSlbConnectionsGroup": ciscoSlbConnectionsGroup,
       "ciscoSlbVirtualClientsGroup": ciscoSlbVirtualClientsGroup,
       "ciscoSlbStickyObjectsGroup": ciscoSlbStickyObjectsGroup,
       "ciscoSlbDfpPasswordGroup": ciscoSlbDfpPasswordGroup,
       "ciscoSlbDfpAgentGroup": ciscoSlbDfpAgentGroup,
       "ciscoSlbDfpRealGroup": ciscoSlbDfpRealGroup,
       "ciscoSlbNotifEnabledGroup": ciscoSlbNotifEnabledGroup,
       "ciscoSlbVirtualServersAddGroup": ciscoSlbVirtualServersAddGroup,
       "ciscoSlbNotifGroup": ciscoSlbNotifGroup,
       "ciscoSlbSaspGroup": ciscoSlbSaspGroup,
       "ciscoSlbSaspAgentGroup": ciscoSlbSaspAgentGroup,
       "ciscoSlbSaspGroupGroup": ciscoSlbSaspGroupGroup,
       "ciscoSlbSaspMemberGroup": ciscoSlbSaspMemberGroup,
       "ciscoSlbSaspStatsGroup": ciscoSlbSaspStatsGroup,
       "ciscoSlbSaspNotifGroup": ciscoSlbSaspNotifGroup,
       "ciscoSlbVServerInfoGroup": ciscoSlbVServerInfoGroup,
       "ciscoSlbVServerIPGroup": ciscoSlbVServerIPGroup,
       "ciscoSlbVServerNotifEnabledGroup": ciscoSlbVServerNotifEnabledGroup,
       "ciscoSlbVServerNotifGroup": ciscoSlbVServerNotifGroup,
       "ciscoSlbNotifObjectsGroup": ciscoSlbNotifObjectsGroup,
       "ciscoSlbNotifEnabledGroupRev2": ciscoSlbNotifEnabledGroupRev2,
       "ciscoSlbNotifGroupRev2": ciscoSlbNotifGroupRev2,
       "ciscoSlbVServerInfoGroupRev1": ciscoSlbVServerInfoGroupRev1,
       "ciscoSlbVServerInfoGroupRev2": ciscoSlbVServerInfoGroupRev2}
)
