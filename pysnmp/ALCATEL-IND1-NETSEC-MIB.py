# SNMP MIB module (ALCATEL-IND1-NETSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-NETSEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:37 2024
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

(softentIND1NetSec,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1NetSec")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alcatelIND1NETSECMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1)
)
alcatelIND1NETSECMIB.setRevisions(
        ("2010-05-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaAnomalyType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("arpaddressscan", 1),
          ("arpfailure", 4),
          ("arpflood", 2),
          ("finackdiff", 14),
          ("finscan", 13),
          ("icmpaddressscan", 5),
          ("icmpflood", 6),
          ("icmpunreachable", 7),
          ("reserved", 3),
          ("rstcount", 15),
          ("synackscan", 12),
          ("synfailure", 11),
          ("synflood", 10),
          ("tcpaddressscan", 9),
          ("tcpportscan", 8))
    )



class AlaPacketType(Integer32, TextualConvention):
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
        *(("arpreply", 1),
          ("arprequest", 2),
          ("icmpdnr", 5),
          ("icmpechoreply", 3),
          ("icmpechorequest", 4),
          ("tcpfinack", 9),
          ("tcpfinnack", 10),
          ("tcprst", 11),
          ("tcpsynack", 7),
          ("tcpsynnack", 8),
          ("tcpsynonly", 6))
    )



class AlaNetsecStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("disable", 2),
          ("enable", 1))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1NETSECMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1NETSECMIBNotifications = _AlcatelIND1NETSECMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1NETSECMIBNotifications.setStatus("current")
_AlcatelIND1NETSECMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1NETSECMIBObjects = _AlcatelIND1NETSECMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1)
)
_AlaNetSecPortRangeConfig_ObjectIdentity = ObjectIdentity
alaNetSecPortRangeConfig = _AlaNetSecPortRangeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 1)
)
_AlaNetSecPortRangeGroupTable_Object = MibTable
alaNetSecPortRangeGroupTable = _AlaNetSecPortRangeGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaNetSecPortRangeGroupTable.setStatus("current")
_AlaNetSecPortRangeGroupEntry_Object = MibTableRow
alaNetSecPortRangeGroupEntry = _AlaNetSecPortRangeGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 1, 1, 1)
)
alaNetSecPortRangeGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortRangeGroupStartIfId"),
    (0, "ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortRangeGroupEndIfId"),
)
if mibBuilder.loadTexts:
    alaNetSecPortRangeGroupEntry.setStatus("current")
_AlaNetSecPortRangeGroupStartIfId_Type = InterfaceIndex
_AlaNetSecPortRangeGroupStartIfId_Object = MibTableColumn
alaNetSecPortRangeGroupStartIfId = _AlaNetSecPortRangeGroupStartIfId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 1, 1, 1, 1),
    _AlaNetSecPortRangeGroupStartIfId_Type()
)
alaNetSecPortRangeGroupStartIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNetSecPortRangeGroupStartIfId.setStatus("current")
_AlaNetSecPortRangeGroupEndIfId_Type = InterfaceIndex
_AlaNetSecPortRangeGroupEndIfId_Object = MibTableColumn
alaNetSecPortRangeGroupEndIfId = _AlaNetSecPortRangeGroupEndIfId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 1, 1, 1, 2),
    _AlaNetSecPortRangeGroupEndIfId_Type()
)
alaNetSecPortRangeGroupEndIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNetSecPortRangeGroupEndIfId.setStatus("current")


class _AlaNetSecPortRangeGroupName_Type(SnmpAdminString):
    """Custom type alaNetSecPortRangeGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaNetSecPortRangeGroupName_Type.__name__ = "SnmpAdminString"
_AlaNetSecPortRangeGroupName_Object = MibTableColumn
alaNetSecPortRangeGroupName = _AlaNetSecPortRangeGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 1, 1, 1, 3),
    _AlaNetSecPortRangeGroupName_Type()
)
alaNetSecPortRangeGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaNetSecPortRangeGroupName.setStatus("current")
_AlaNetSecPortRangeGroupRowStatus_Type = RowStatus
_AlaNetSecPortRangeGroupRowStatus_Object = MibTableColumn
alaNetSecPortRangeGroupRowStatus = _AlaNetSecPortRangeGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 1, 1, 1, 4),
    _AlaNetSecPortRangeGroupRowStatus_Type()
)
alaNetSecPortRangeGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaNetSecPortRangeGroupRowStatus.setStatus("current")
_AlaNetSecMonitoringGroupConfig_ObjectIdentity = ObjectIdentity
alaNetSecMonitoringGroupConfig = _AlaNetSecMonitoringGroupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 2)
)
_AlaNetSecMonitoringGroupTable_Object = MibTable
alaNetSecMonitoringGroupTable = _AlaNetSecMonitoringGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaNetSecMonitoringGroupTable.setStatus("current")
_AlaNetSecMonitoringGroupEntry_Object = MibTableRow
alaNetSecMonitoringGroupEntry = _AlaNetSecMonitoringGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 2, 1, 1)
)
alaNetSecMonitoringGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-NETSEC-MIB", "alaNetSecMonitoringGroupName"),
    (0, "ALCATEL-IND1-NETSEC-MIB", "alaNetSecMonitoringGroupAnomaly"),
)
if mibBuilder.loadTexts:
    alaNetSecMonitoringGroupEntry.setStatus("current")


class _AlaNetSecMonitoringGroupName_Type(SnmpAdminString):
    """Custom type alaNetSecMonitoringGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaNetSecMonitoringGroupName_Type.__name__ = "SnmpAdminString"
_AlaNetSecMonitoringGroupName_Object = MibTableColumn
alaNetSecMonitoringGroupName = _AlaNetSecMonitoringGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 2, 1, 1, 1),
    _AlaNetSecMonitoringGroupName_Type()
)
alaNetSecMonitoringGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNetSecMonitoringGroupName.setStatus("current")
_AlaNetSecMonitoringGroupAnomaly_Type = AlaAnomalyType
_AlaNetSecMonitoringGroupAnomaly_Object = MibTableColumn
alaNetSecMonitoringGroupAnomaly = _AlaNetSecMonitoringGroupAnomaly_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 2, 1, 1, 2),
    _AlaNetSecMonitoringGroupAnomaly_Type()
)
alaNetSecMonitoringGroupAnomaly.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNetSecMonitoringGroupAnomaly.setStatus("current")


class _AlaNetSecMonitoringGroupAnomalyState_Type(AlaNetsecStatus):
    """Custom type alaNetSecMonitoringGroupAnomalyState based on AlaNetsecStatus"""


_AlaNetSecMonitoringGroupAnomalyState_Object = MibTableColumn
alaNetSecMonitoringGroupAnomalyState = _AlaNetSecMonitoringGroupAnomalyState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 2, 1, 1, 3),
    _AlaNetSecMonitoringGroupAnomalyState_Type()
)
alaNetSecMonitoringGroupAnomalyState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaNetSecMonitoringGroupAnomalyState.setStatus("current")


class _AlaNetSecMonitoringGroupAnomalyLog_Type(AlaNetsecStatus):
    """Custom type alaNetSecMonitoringGroupAnomalyLog based on AlaNetsecStatus"""


_AlaNetSecMonitoringGroupAnomalyLog_Object = MibTableColumn
alaNetSecMonitoringGroupAnomalyLog = _AlaNetSecMonitoringGroupAnomalyLog_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 2, 1, 1, 4),
    _AlaNetSecMonitoringGroupAnomalyLog_Type()
)
alaNetSecMonitoringGroupAnomalyLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaNetSecMonitoringGroupAnomalyLog.setStatus("current")


class _AlaNetSecMonitoringGroupAnomalyTrap_Type(AlaNetsecStatus):
    """Custom type alaNetSecMonitoringGroupAnomalyTrap based on AlaNetsecStatus"""


_AlaNetSecMonitoringGroupAnomalyTrap_Object = MibTableColumn
alaNetSecMonitoringGroupAnomalyTrap = _AlaNetSecMonitoringGroupAnomalyTrap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 2, 1, 1, 5),
    _AlaNetSecMonitoringGroupAnomalyTrap_Type()
)
alaNetSecMonitoringGroupAnomalyTrap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaNetSecMonitoringGroupAnomalyTrap.setStatus("current")


class _AlaNetSecMonitoringGroupAnomalyQuarantine_Type(AlaNetsecStatus):
    """Custom type alaNetSecMonitoringGroupAnomalyQuarantine based on AlaNetsecStatus"""


_AlaNetSecMonitoringGroupAnomalyQuarantine_Object = MibTableColumn
alaNetSecMonitoringGroupAnomalyQuarantine = _AlaNetSecMonitoringGroupAnomalyQuarantine_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 2, 1, 1, 6),
    _AlaNetSecMonitoringGroupAnomalyQuarantine_Type()
)
alaNetSecMonitoringGroupAnomalyQuarantine.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaNetSecMonitoringGroupAnomalyQuarantine.setStatus("current")


class _AlaNetSecMonitoringGroupAnomalyCount_Type(Integer32):
    """Custom type alaNetSecMonitoringGroupAnomalyCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_AlaNetSecMonitoringGroupAnomalyCount_Type.__name__ = "Integer32"
_AlaNetSecMonitoringGroupAnomalyCount_Object = MibTableColumn
alaNetSecMonitoringGroupAnomalyCount = _AlaNetSecMonitoringGroupAnomalyCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 2, 1, 1, 7),
    _AlaNetSecMonitoringGroupAnomalyCount_Type()
)
alaNetSecMonitoringGroupAnomalyCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaNetSecMonitoringGroupAnomalyCount.setStatus("current")


class _AlaNetSecMonitoringGroupAnomalySensitivity_Type(Integer32):
    """Custom type alaNetSecMonitoringGroupAnomalySensitivity based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AlaNetSecMonitoringGroupAnomalySensitivity_Type.__name__ = "Integer32"
_AlaNetSecMonitoringGroupAnomalySensitivity_Object = MibTableColumn
alaNetSecMonitoringGroupAnomalySensitivity = _AlaNetSecMonitoringGroupAnomalySensitivity_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 2, 1, 1, 8),
    _AlaNetSecMonitoringGroupAnomalySensitivity_Type()
)
alaNetSecMonitoringGroupAnomalySensitivity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaNetSecMonitoringGroupAnomalySensitivity.setStatus("current")


class _AlaNetSecMonitoringGroupAnomalyPeriod_Type(Integer32):
    """Custom type alaNetSecMonitoringGroupAnomalyPeriod based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_AlaNetSecMonitoringGroupAnomalyPeriod_Type.__name__ = "Integer32"
_AlaNetSecMonitoringGroupAnomalyPeriod_Object = MibTableColumn
alaNetSecMonitoringGroupAnomalyPeriod = _AlaNetSecMonitoringGroupAnomalyPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 2, 1, 1, 9),
    _AlaNetSecMonitoringGroupAnomalyPeriod_Type()
)
alaNetSecMonitoringGroupAnomalyPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaNetSecMonitoringGroupAnomalyPeriod.setStatus("current")
_AlaNetSecMonitoringGroupRowStatus_Type = RowStatus
_AlaNetSecMonitoringGroupRowStatus_Object = MibTableColumn
alaNetSecMonitoringGroupRowStatus = _AlaNetSecMonitoringGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 2, 1, 1, 10),
    _AlaNetSecMonitoringGroupRowStatus_Type()
)
alaNetSecMonitoringGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaNetSecMonitoringGroupRowStatus.setStatus("current")
_AlaNetSecPortStats_ObjectIdentity = ObjectIdentity
alaNetSecPortStats = _AlaNetSecPortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 3)
)
_AlaNetSecPortStatsTable_Object = MibTable
alaNetSecPortStatsTable = _AlaNetSecPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alaNetSecPortStatsTable.setStatus("current")
_AlaNetSecPortStatsEntry_Object = MibTableRow
alaNetSecPortStatsEntry = _AlaNetSecPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 3, 1, 1)
)
alaNetSecPortStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortStatsIfId"),
    (0, "ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortStatsPacket"),
)
if mibBuilder.loadTexts:
    alaNetSecPortStatsEntry.setStatus("current")
_AlaNetSecPortStatsIfId_Type = InterfaceIndex
_AlaNetSecPortStatsIfId_Object = MibTableColumn
alaNetSecPortStatsIfId = _AlaNetSecPortStatsIfId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 3, 1, 1, 1),
    _AlaNetSecPortStatsIfId_Type()
)
alaNetSecPortStatsIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNetSecPortStatsIfId.setStatus("current")
_AlaNetSecPortStatsPacket_Type = AlaPacketType
_AlaNetSecPortStatsPacket_Object = MibTableColumn
alaNetSecPortStatsPacket = _AlaNetSecPortStatsPacket_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 3, 1, 1, 2),
    _AlaNetSecPortStatsPacket_Type()
)
alaNetSecPortStatsPacket.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNetSecPortStatsPacket.setStatus("current")
_AlaNetSecPortStatsLastIngress_Type = Counter32
_AlaNetSecPortStatsLastIngress_Object = MibTableColumn
alaNetSecPortStatsLastIngress = _AlaNetSecPortStatsLastIngress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 3, 1, 1, 3),
    _AlaNetSecPortStatsLastIngress_Type()
)
alaNetSecPortStatsLastIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNetSecPortStatsLastIngress.setStatus("current")
_AlaNetSecPortStatsLastEgress_Type = Counter32
_AlaNetSecPortStatsLastEgress_Object = MibTableColumn
alaNetSecPortStatsLastEgress = _AlaNetSecPortStatsLastEgress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 3, 1, 1, 4),
    _AlaNetSecPortStatsLastEgress_Type()
)
alaNetSecPortStatsLastEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNetSecPortStatsLastEgress.setStatus("current")
_AlaNetSecPortStatsTotalIngress_Type = Counter32
_AlaNetSecPortStatsTotalIngress_Object = MibTableColumn
alaNetSecPortStatsTotalIngress = _AlaNetSecPortStatsTotalIngress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 3, 1, 1, 5),
    _AlaNetSecPortStatsTotalIngress_Type()
)
alaNetSecPortStatsTotalIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNetSecPortStatsTotalIngress.setStatus("current")
_AlaNetSecPortStatsTotalEgress_Type = Counter32
_AlaNetSecPortStatsTotalEgress_Object = MibTableColumn
alaNetSecPortStatsTotalEgress = _AlaNetSecPortStatsTotalEgress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 3, 1, 1, 6),
    _AlaNetSecPortStatsTotalEgress_Type()
)
alaNetSecPortStatsTotalEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNetSecPortStatsTotalEgress.setStatus("current")
_AlaNetSecPortAnomalyStats_ObjectIdentity = ObjectIdentity
alaNetSecPortAnomalyStats = _AlaNetSecPortAnomalyStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 4)
)
_AlaNetSecPortAnomalyStatsTable_Object = MibTable
alaNetSecPortAnomalyStatsTable = _AlaNetSecPortAnomalyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    alaNetSecPortAnomalyStatsTable.setStatus("current")
_AlaNetSecPortAnomalyStatsEntry_Object = MibTableRow
alaNetSecPortAnomalyStatsEntry = _AlaNetSecPortAnomalyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 4, 1, 1)
)
alaNetSecPortAnomalyStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortAnomalyStatsIfId"),
    (0, "ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortAnomalyStatsAnomaly"),
    (0, "ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortAnomalyStatsPacket"),
)
if mibBuilder.loadTexts:
    alaNetSecPortAnomalyStatsEntry.setStatus("current")
_AlaNetSecPortAnomalyStatsIfId_Type = InterfaceIndex
_AlaNetSecPortAnomalyStatsIfId_Object = MibTableColumn
alaNetSecPortAnomalyStatsIfId = _AlaNetSecPortAnomalyStatsIfId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 4, 1, 1, 1),
    _AlaNetSecPortAnomalyStatsIfId_Type()
)
alaNetSecPortAnomalyStatsIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNetSecPortAnomalyStatsIfId.setStatus("current")
_AlaNetSecPortAnomalyStatsAnomaly_Type = AlaAnomalyType
_AlaNetSecPortAnomalyStatsAnomaly_Object = MibTableColumn
alaNetSecPortAnomalyStatsAnomaly = _AlaNetSecPortAnomalyStatsAnomaly_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 4, 1, 1, 2),
    _AlaNetSecPortAnomalyStatsAnomaly_Type()
)
alaNetSecPortAnomalyStatsAnomaly.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNetSecPortAnomalyStatsAnomaly.setStatus("current")
_AlaNetSecPortAnomalyStatsPacket_Type = AlaPacketType
_AlaNetSecPortAnomalyStatsPacket_Object = MibTableColumn
alaNetSecPortAnomalyStatsPacket = _AlaNetSecPortAnomalyStatsPacket_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 4, 1, 1, 3),
    _AlaNetSecPortAnomalyStatsPacket_Type()
)
alaNetSecPortAnomalyStatsPacket.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNetSecPortAnomalyStatsPacket.setStatus("current")
_AlaNetSecPortAnomalyStatsCurrentIngress_Type = Counter32
_AlaNetSecPortAnomalyStatsCurrentIngress_Object = MibTableColumn
alaNetSecPortAnomalyStatsCurrentIngress = _AlaNetSecPortAnomalyStatsCurrentIngress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 4, 1, 1, 4),
    _AlaNetSecPortAnomalyStatsCurrentIngress_Type()
)
alaNetSecPortAnomalyStatsCurrentIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNetSecPortAnomalyStatsCurrentIngress.setStatus("current")
_AlaNetSecPortAnomalyStatsCurrentEgress_Type = Counter32
_AlaNetSecPortAnomalyStatsCurrentEgress_Object = MibTableColumn
alaNetSecPortAnomalyStatsCurrentEgress = _AlaNetSecPortAnomalyStatsCurrentEgress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 4, 1, 1, 5),
    _AlaNetSecPortAnomalyStatsCurrentEgress_Type()
)
alaNetSecPortAnomalyStatsCurrentEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNetSecPortAnomalyStatsCurrentEgress.setStatus("current")
_AlaNetSecPortAnomalyStatsLastIngress_Type = Counter32
_AlaNetSecPortAnomalyStatsLastIngress_Object = MibTableColumn
alaNetSecPortAnomalyStatsLastIngress = _AlaNetSecPortAnomalyStatsLastIngress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 4, 1, 1, 6),
    _AlaNetSecPortAnomalyStatsLastIngress_Type()
)
alaNetSecPortAnomalyStatsLastIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNetSecPortAnomalyStatsLastIngress.setStatus("current")
_AlaNetSecPortAnomalyStatsLastEgress_Type = Counter32
_AlaNetSecPortAnomalyStatsLastEgress_Object = MibTableColumn
alaNetSecPortAnomalyStatsLastEgress = _AlaNetSecPortAnomalyStatsLastEgress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 4, 1, 1, 7),
    _AlaNetSecPortAnomalyStatsLastEgress_Type()
)
alaNetSecPortAnomalyStatsLastEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNetSecPortAnomalyStatsLastEgress.setStatus("current")
_AlaNetSecPortAnomalySummary_ObjectIdentity = ObjectIdentity
alaNetSecPortAnomalySummary = _AlaNetSecPortAnomalySummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 5)
)
_AlaNetSecPortAnomalySummaryTable_Object = MibTable
alaNetSecPortAnomalySummaryTable = _AlaNetSecPortAnomalySummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    alaNetSecPortAnomalySummaryTable.setStatus("current")
_AlaNetSecPortAnomalySummaryEntry_Object = MibTableRow
alaNetSecPortAnomalySummaryEntry = _AlaNetSecPortAnomalySummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 5, 1, 1)
)
alaNetSecPortAnomalySummaryEntry.setIndexNames(
    (0, "ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortAnomalySummaryIfId"),
    (0, "ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortAnomalySummaryAnomaly"),
)
if mibBuilder.loadTexts:
    alaNetSecPortAnomalySummaryEntry.setStatus("current")
_AlaNetSecPortAnomalySummaryIfId_Type = InterfaceIndex
_AlaNetSecPortAnomalySummaryIfId_Object = MibTableColumn
alaNetSecPortAnomalySummaryIfId = _AlaNetSecPortAnomalySummaryIfId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 5, 1, 1, 1),
    _AlaNetSecPortAnomalySummaryIfId_Type()
)
alaNetSecPortAnomalySummaryIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNetSecPortAnomalySummaryIfId.setStatus("current")
_AlaNetSecPortAnomalySummaryAnomaly_Type = AlaAnomalyType
_AlaNetSecPortAnomalySummaryAnomaly_Object = MibTableColumn
alaNetSecPortAnomalySummaryAnomaly = _AlaNetSecPortAnomalySummaryAnomaly_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 5, 1, 1, 2),
    _AlaNetSecPortAnomalySummaryAnomaly_Type()
)
alaNetSecPortAnomalySummaryAnomaly.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNetSecPortAnomalySummaryAnomaly.setStatus("current")
_AlaNetSecPortAnomalySummaryObserved_Type = Counter32
_AlaNetSecPortAnomalySummaryObserved_Object = MibTableColumn
alaNetSecPortAnomalySummaryObserved = _AlaNetSecPortAnomalySummaryObserved_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 5, 1, 1, 3),
    _AlaNetSecPortAnomalySummaryObserved_Type()
)
alaNetSecPortAnomalySummaryObserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNetSecPortAnomalySummaryObserved.setStatus("current")
_AlaNetSecPortAnomalySummaryDetected_Type = Counter32
_AlaNetSecPortAnomalySummaryDetected_Object = MibTableColumn
alaNetSecPortAnomalySummaryDetected = _AlaNetSecPortAnomalySummaryDetected_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 5, 1, 1, 4),
    _AlaNetSecPortAnomalySummaryDetected_Type()
)
alaNetSecPortAnomalySummaryDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNetSecPortAnomalySummaryDetected.setStatus("current")
_AlaNetSecPortOp_ObjectIdentity = ObjectIdentity
alaNetSecPortOp = _AlaNetSecPortOp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 6)
)
_AlaNetSecPortOpTable_Object = MibTable
alaNetSecPortOpTable = _AlaNetSecPortOpTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    alaNetSecPortOpTable.setStatus("current")
_AlaNetSecPortOpEntry_Object = MibTableRow
alaNetSecPortOpEntry = _AlaNetSecPortOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 6, 1, 1)
)
alaNetSecPortOpEntry.setIndexNames(
    (0, "ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortOpIfId"),
    (0, "ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortOpAnomaly"),
)
if mibBuilder.loadTexts:
    alaNetSecPortOpEntry.setStatus("current")
_AlaNetSecPortOpIfId_Type = InterfaceIndex
_AlaNetSecPortOpIfId_Object = MibTableColumn
alaNetSecPortOpIfId = _AlaNetSecPortOpIfId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 6, 1, 1, 1),
    _AlaNetSecPortOpIfId_Type()
)
alaNetSecPortOpIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNetSecPortOpIfId.setStatus("current")
_AlaNetSecPortOpAnomaly_Type = AlaAnomalyType
_AlaNetSecPortOpAnomaly_Object = MibTableColumn
alaNetSecPortOpAnomaly = _AlaNetSecPortOpAnomaly_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 6, 1, 1, 2),
    _AlaNetSecPortOpAnomaly_Type()
)
alaNetSecPortOpAnomaly.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNetSecPortOpAnomaly.setStatus("current")
_AlaNetSecPortOpState_Type = AlaNetsecStatus
_AlaNetSecPortOpState_Object = MibTableColumn
alaNetSecPortOpState = _AlaNetSecPortOpState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 6, 1, 1, 3),
    _AlaNetSecPortOpState_Type()
)
alaNetSecPortOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNetSecPortOpState.setStatus("current")
_AlaNetSecPortOpLog_Type = AlaNetsecStatus
_AlaNetSecPortOpLog_Object = MibTableColumn
alaNetSecPortOpLog = _AlaNetSecPortOpLog_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 6, 1, 1, 4),
    _AlaNetSecPortOpLog_Type()
)
alaNetSecPortOpLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNetSecPortOpLog.setStatus("current")
_AlaNetSecPortOpTrap_Type = AlaNetsecStatus
_AlaNetSecPortOpTrap_Object = MibTableColumn
alaNetSecPortOpTrap = _AlaNetSecPortOpTrap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 6, 1, 1, 5),
    _AlaNetSecPortOpTrap_Type()
)
alaNetSecPortOpTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNetSecPortOpTrap.setStatus("current")
_AlaNetSecPortOpQuarantine_Type = AlaNetsecStatus
_AlaNetSecPortOpQuarantine_Object = MibTableColumn
alaNetSecPortOpQuarantine = _AlaNetSecPortOpQuarantine_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 6, 1, 1, 6),
    _AlaNetSecPortOpQuarantine_Type()
)
alaNetSecPortOpQuarantine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNetSecPortOpQuarantine.setStatus("current")


class _AlaNetSecPortOpCount_Type(Integer32):
    """Custom type alaNetSecPortOpCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_AlaNetSecPortOpCount_Type.__name__ = "Integer32"
_AlaNetSecPortOpCount_Object = MibTableColumn
alaNetSecPortOpCount = _AlaNetSecPortOpCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 6, 1, 1, 7),
    _AlaNetSecPortOpCount_Type()
)
alaNetSecPortOpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNetSecPortOpCount.setStatus("current")


class _AlaNetSecPortOpSensitivity_Type(Integer32):
    """Custom type alaNetSecPortOpSensitivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AlaNetSecPortOpSensitivity_Type.__name__ = "Integer32"
_AlaNetSecPortOpSensitivity_Object = MibTableColumn
alaNetSecPortOpSensitivity = _AlaNetSecPortOpSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 6, 1, 1, 8),
    _AlaNetSecPortOpSensitivity_Type()
)
alaNetSecPortOpSensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNetSecPortOpSensitivity.setStatus("current")


class _AlaNetSecPortOpPeriod_Type(Integer32):
    """Custom type alaNetSecPortOpPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_AlaNetSecPortOpPeriod_Type.__name__ = "Integer32"
_AlaNetSecPortOpPeriod_Object = MibTableColumn
alaNetSecPortOpPeriod = _AlaNetSecPortOpPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 6, 1, 1, 9),
    _AlaNetSecPortOpPeriod_Type()
)
alaNetSecPortOpPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNetSecPortOpPeriod.setStatus("current")
_AlaNetSecGroupOp_ObjectIdentity = ObjectIdentity
alaNetSecGroupOp = _AlaNetSecGroupOp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 7)
)
_AlaNetSecGroupOpTable_Object = MibTable
alaNetSecGroupOpTable = _AlaNetSecGroupOpTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    alaNetSecGroupOpTable.setStatus("current")
_AlaNetSecGroupOpEntry_Object = MibTableRow
alaNetSecGroupOpEntry = _AlaNetSecGroupOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 7, 1, 1)
)
alaNetSecGroupOpEntry.setIndexNames(
    (0, "ALCATEL-IND1-NETSEC-MIB", "alaNetSecGroupOpName"),
    (0, "ALCATEL-IND1-NETSEC-MIB", "alaNetSecGroupOpAnomaly"),
)
if mibBuilder.loadTexts:
    alaNetSecGroupOpEntry.setStatus("current")


class _AlaNetSecGroupOpName_Type(SnmpAdminString):
    """Custom type alaNetSecGroupOpName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaNetSecGroupOpName_Type.__name__ = "SnmpAdminString"
_AlaNetSecGroupOpName_Object = MibTableColumn
alaNetSecGroupOpName = _AlaNetSecGroupOpName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 7, 1, 1, 1),
    _AlaNetSecGroupOpName_Type()
)
alaNetSecGroupOpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNetSecGroupOpName.setStatus("current")
_AlaNetSecGroupOpAnomaly_Type = AlaAnomalyType
_AlaNetSecGroupOpAnomaly_Object = MibTableColumn
alaNetSecGroupOpAnomaly = _AlaNetSecGroupOpAnomaly_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 7, 1, 1, 2),
    _AlaNetSecGroupOpAnomaly_Type()
)
alaNetSecGroupOpAnomaly.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNetSecGroupOpAnomaly.setStatus("current")
_AlaNetSecGroupOpState_Type = AlaNetsecStatus
_AlaNetSecGroupOpState_Object = MibTableColumn
alaNetSecGroupOpState = _AlaNetSecGroupOpState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 7, 1, 1, 3),
    _AlaNetSecGroupOpState_Type()
)
alaNetSecGroupOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNetSecGroupOpState.setStatus("current")
_AlaNetSecGroupOpLog_Type = AlaNetsecStatus
_AlaNetSecGroupOpLog_Object = MibTableColumn
alaNetSecGroupOpLog = _AlaNetSecGroupOpLog_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 7, 1, 1, 4),
    _AlaNetSecGroupOpLog_Type()
)
alaNetSecGroupOpLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNetSecGroupOpLog.setStatus("current")
_AlaNetSecGroupOpTrap_Type = AlaNetsecStatus
_AlaNetSecGroupOpTrap_Object = MibTableColumn
alaNetSecGroupOpTrap = _AlaNetSecGroupOpTrap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 7, 1, 1, 5),
    _AlaNetSecGroupOpTrap_Type()
)
alaNetSecGroupOpTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNetSecGroupOpTrap.setStatus("current")
_AlaNetSecGroupOpQuarantine_Type = AlaNetsecStatus
_AlaNetSecGroupOpQuarantine_Object = MibTableColumn
alaNetSecGroupOpQuarantine = _AlaNetSecGroupOpQuarantine_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 7, 1, 1, 6),
    _AlaNetSecGroupOpQuarantine_Type()
)
alaNetSecGroupOpQuarantine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNetSecGroupOpQuarantine.setStatus("current")


class _AlaNetSecGroupOpCount_Type(Integer32):
    """Custom type alaNetSecGroupOpCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_AlaNetSecGroupOpCount_Type.__name__ = "Integer32"
_AlaNetSecGroupOpCount_Object = MibTableColumn
alaNetSecGroupOpCount = _AlaNetSecGroupOpCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 7, 1, 1, 7),
    _AlaNetSecGroupOpCount_Type()
)
alaNetSecGroupOpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNetSecGroupOpCount.setStatus("current")


class _AlaNetSecGroupOpSensitivity_Type(Integer32):
    """Custom type alaNetSecGroupOpSensitivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AlaNetSecGroupOpSensitivity_Type.__name__ = "Integer32"
_AlaNetSecGroupOpSensitivity_Object = MibTableColumn
alaNetSecGroupOpSensitivity = _AlaNetSecGroupOpSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 7, 1, 1, 8),
    _AlaNetSecGroupOpSensitivity_Type()
)
alaNetSecGroupOpSensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNetSecGroupOpSensitivity.setStatus("current")


class _AlaNetSecGroupOpPeriod_Type(Integer32):
    """Custom type alaNetSecGroupOpPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_AlaNetSecGroupOpPeriod_Type.__name__ = "Integer32"
_AlaNetSecGroupOpPeriod_Object = MibTableColumn
alaNetSecGroupOpPeriod = _AlaNetSecGroupOpPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 7, 1, 1, 9),
    _AlaNetSecGroupOpPeriod_Type()
)
alaNetSecGroupOpPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNetSecGroupOpPeriod.setStatus("current")
_AlaNetSecGroup_ObjectIdentity = ObjectIdentity
alaNetSecGroup = _AlaNetSecGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 8)
)
_AlaNetSecGroupTable_Object = MibTable
alaNetSecGroupTable = _AlaNetSecGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    alaNetSecGroupTable.setStatus("current")
_AlaNetSecGroupEntry_Object = MibTableRow
alaNetSecGroupEntry = _AlaNetSecGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 8, 1, 1)
)
alaNetSecGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-NETSEC-MIB", "alaNetSecGroupName"),
)
if mibBuilder.loadTexts:
    alaNetSecGroupEntry.setStatus("current")


class _AlaNetSecGroupName_Type(SnmpAdminString):
    """Custom type alaNetSecGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaNetSecGroupName_Type.__name__ = "SnmpAdminString"
_AlaNetSecGroupName_Object = MibTableColumn
alaNetSecGroupName = _AlaNetSecGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 8, 1, 1, 1),
    _AlaNetSecGroupName_Type()
)
alaNetSecGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNetSecGroupName.setStatus("current")
_AlaNetSecGroupMemberPorts_Type = TruthValue
_AlaNetSecGroupMemberPorts_Object = MibTableColumn
alaNetSecGroupMemberPorts = _AlaNetSecGroupMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 8, 1, 1, 2),
    _AlaNetSecGroupMemberPorts_Type()
)
alaNetSecGroupMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNetSecGroupMemberPorts.setStatus("current")
_AlaNetSecGroupAnomalyCfg_Type = TruthValue
_AlaNetSecGroupAnomalyCfg_Object = MibTableColumn
alaNetSecGroupAnomalyCfg = _AlaNetSecGroupAnomalyCfg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 8, 1, 1, 3),
    _AlaNetSecGroupAnomalyCfg_Type()
)
alaNetSecGroupAnomalyCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNetSecGroupAnomalyCfg.setStatus("current")
_AlaNetSecPortTrapsObj_ObjectIdentity = ObjectIdentity
alaNetSecPortTrapsObj = _AlaNetSecPortTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 9)
)
_AlaNetSecPortTrapInfoIfId_Type = InterfaceIndex
_AlaNetSecPortTrapInfoIfId_Object = MibScalar
alaNetSecPortTrapInfoIfId = _AlaNetSecPortTrapInfoIfId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 9, 1),
    _AlaNetSecPortTrapInfoIfId_Type()
)
alaNetSecPortTrapInfoIfId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaNetSecPortTrapInfoIfId.setStatus("current")
_AlaNetSecPortTrapInfoAnomaly_Type = AlaAnomalyType
_AlaNetSecPortTrapInfoAnomaly_Object = MibScalar
alaNetSecPortTrapInfoAnomaly = _AlaNetSecPortTrapInfoAnomaly_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 9, 2),
    _AlaNetSecPortTrapInfoAnomaly_Type()
)
alaNetSecPortTrapInfoAnomaly.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaNetSecPortTrapInfoAnomaly.setStatus("current")


class _AlaNetSecPortTrapInfoType_Type(Integer32):
    """Custom type alaNetSecPortTrapInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("source", 2),
          ("target", 3),
          ("unknown", 1))
    )


_AlaNetSecPortTrapInfoType_Type.__name__ = "Integer32"
_AlaNetSecPortTrapInfoType_Object = MibScalar
alaNetSecPortTrapInfoType = _AlaNetSecPortTrapInfoType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 1, 9, 3),
    _AlaNetSecPortTrapInfoType_Type()
)
alaNetSecPortTrapInfoType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaNetSecPortTrapInfoType.setStatus("current")
_AlcatelIND1NETSECMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1NETSECMIBConformance = _AlcatelIND1NETSECMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1NETSECMIBConformance.setStatus("current")
_AlcatelIND1NETSECMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1NETSECMIBGroups = _AlcatelIND1NETSECMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1NETSECMIBGroups.setStatus("current")
_AlcatelIND1NETSECMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1NETSECMIBCompliances = _AlcatelIND1NETSECMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1NETSECMIBCompliances.setStatus("current")

# Managed Objects groups

alaNetSecPortRangeComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 2, 1, 1)
)
alaNetSecPortRangeComplianceGroup.setObjects(
    ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortRangeGroupRowStatus")
)
if mibBuilder.loadTexts:
    alaNetSecPortRangeComplianceGroup.setStatus("current")

alaNetSecMonitoringGroupComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 2, 1, 2)
)
alaNetSecMonitoringGroupComplianceGroup.setObjects(
    ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecMonitoringGroupRowStatus")
)
if mibBuilder.loadTexts:
    alaNetSecMonitoringGroupComplianceGroup.setStatus("current")

alaNetSecPortStatsComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 2, 1, 4)
)
alaNetSecPortStatsComplianceGroup.setObjects(
      *(("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortStatsLastIngress"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortStatsLastEgress"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortStatsTotalIngress"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortStatsTotalEgress"))
)
if mibBuilder.loadTexts:
    alaNetSecPortStatsComplianceGroup.setStatus("current")

alaNetSecPortAnomalyStatsComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 2, 1, 5)
)
alaNetSecPortAnomalyStatsComplianceGroup.setObjects(
      *(("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortAnomalyStatsCurrentIngress"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortAnomalyStatsCurrentEgress"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortAnomalyStatsLastIngress"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortAnomalyStatsLastEgress"))
)
if mibBuilder.loadTexts:
    alaNetSecPortAnomalyStatsComplianceGroup.setStatus("current")

alaNetSecPortAnomalySummaryComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 2, 1, 6)
)
alaNetSecPortAnomalySummaryComplianceGroup.setObjects(
      *(("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortAnomalySummaryObserved"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortAnomalySummaryDetected"))
)
if mibBuilder.loadTexts:
    alaNetSecPortAnomalySummaryComplianceGroup.setStatus("current")

alaNetSecPortOpComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 2, 1, 7)
)
alaNetSecPortOpComplianceGroup.setObjects(
      *(("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortOpState"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortOpLog"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortOpTrap"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortOpQuarantine"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortOpCount"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortOpSensitivity"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortOpPeriod"))
)
if mibBuilder.loadTexts:
    alaNetSecPortOpComplianceGroup.setStatus("current")

alaNetSecGroupOpComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 2, 1, 8)
)
alaNetSecGroupOpComplianceGroup.setObjects(
      *(("ALCATEL-IND1-NETSEC-MIB", "alaNetSecGroupOpState"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecGroupOpLog"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecGroupOpTrap"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecGroupOpQuarantine"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecGroupOpCount"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecGroupOpSensitivity"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecGroupOpPeriod"))
)
if mibBuilder.loadTexts:
    alaNetSecGroupOpComplianceGroup.setStatus("current")

alaNetSecGroupComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 2, 1, 9)
)
alaNetSecGroupComplianceGroup.setObjects(
      *(("ALCATEL-IND1-NETSEC-MIB", "alaNetSecGroupMemberPorts"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecGroupAnomalyCfg"))
)
if mibBuilder.loadTexts:
    alaNetSecGroupComplianceGroup.setStatus("current")

alaNetSecMonitoringGroupEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 2, 1, 10)
)
alaNetSecMonitoringGroupEntryGroup.setObjects(
      *(("ALCATEL-IND1-NETSEC-MIB", "alaNetSecMonitoringGroupAnomalyState"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecMonitoringGroupAnomalyLog"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecMonitoringGroupAnomalyTrap"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecMonitoringGroupAnomalyQuarantine"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecMonitoringGroupAnomalyCount"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecMonitoringGroupAnomalySensitivity"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecMonitoringGroupAnomalyPeriod"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecMonitoringGroupRowStatus"))
)
if mibBuilder.loadTexts:
    alaNetSecMonitoringGroupEntryGroup.setStatus("current")

alaNetSecPortRangeGroupEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 2, 1, 11)
)
alaNetSecPortRangeGroupEntryGroup.setObjects(
      *(("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortRangeGroupName"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortRangeGroupRowStatus"))
)
if mibBuilder.loadTexts:
    alaNetSecPortRangeGroupEntryGroup.setStatus("current")

alaNetSecPortTrapAnomalyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 2, 1, 12)
)
alaNetSecPortTrapAnomalyGroup.setObjects(
      *(("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortTrapInfoIfId"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortTrapInfoAnomaly"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortTrapInfoType"))
)
if mibBuilder.loadTexts:
    alaNetSecPortTrapAnomalyGroup.setStatus("current")


# Notification objects

alaNetSecPortTrapAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 0, 1)
)
alaNetSecPortTrapAnomaly.setObjects(
      *(("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortTrapInfoIfId"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortTrapInfoAnomaly"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortTrapInfoType"))
)
if mibBuilder.loadTexts:
    alaNetSecPortTrapAnomaly.setStatus(
        "current"
    )

alaNetSecPortTrapQuarantine = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 0, 2)
)
alaNetSecPortTrapQuarantine.setObjects(
    ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortTrapInfoIfId")
)
if mibBuilder.loadTexts:
    alaNetSecPortTrapQuarantine.setStatus(
        "current"
    )


# Notifications groups

alaNetSecPortTrapsComplianceGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 2, 1, 3)
)
alaNetSecPortTrapsComplianceGroup.setObjects(
      *(("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortTrapAnomaly"),
        ("ALCATEL-IND1-NETSEC-MIB", "alaNetSecPortTrapQuarantine"))
)
if mibBuilder.loadTexts:
    alaNetSecPortTrapsComplianceGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1NETSECMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1NETSECMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-NETSEC-MIB",
    **{"AlaAnomalyType": AlaAnomalyType,
       "AlaPacketType": AlaPacketType,
       "AlaNetsecStatus": AlaNetsecStatus,
       "alcatelIND1NETSECMIB": alcatelIND1NETSECMIB,
       "alcatelIND1NETSECMIBNotifications": alcatelIND1NETSECMIBNotifications,
       "alaNetSecPortTrapAnomaly": alaNetSecPortTrapAnomaly,
       "alaNetSecPortTrapQuarantine": alaNetSecPortTrapQuarantine,
       "alcatelIND1NETSECMIBObjects": alcatelIND1NETSECMIBObjects,
       "alaNetSecPortRangeConfig": alaNetSecPortRangeConfig,
       "alaNetSecPortRangeGroupTable": alaNetSecPortRangeGroupTable,
       "alaNetSecPortRangeGroupEntry": alaNetSecPortRangeGroupEntry,
       "alaNetSecPortRangeGroupStartIfId": alaNetSecPortRangeGroupStartIfId,
       "alaNetSecPortRangeGroupEndIfId": alaNetSecPortRangeGroupEndIfId,
       "alaNetSecPortRangeGroupName": alaNetSecPortRangeGroupName,
       "alaNetSecPortRangeGroupRowStatus": alaNetSecPortRangeGroupRowStatus,
       "alaNetSecMonitoringGroupConfig": alaNetSecMonitoringGroupConfig,
       "alaNetSecMonitoringGroupTable": alaNetSecMonitoringGroupTable,
       "alaNetSecMonitoringGroupEntry": alaNetSecMonitoringGroupEntry,
       "alaNetSecMonitoringGroupName": alaNetSecMonitoringGroupName,
       "alaNetSecMonitoringGroupAnomaly": alaNetSecMonitoringGroupAnomaly,
       "alaNetSecMonitoringGroupAnomalyState": alaNetSecMonitoringGroupAnomalyState,
       "alaNetSecMonitoringGroupAnomalyLog": alaNetSecMonitoringGroupAnomalyLog,
       "alaNetSecMonitoringGroupAnomalyTrap": alaNetSecMonitoringGroupAnomalyTrap,
       "alaNetSecMonitoringGroupAnomalyQuarantine": alaNetSecMonitoringGroupAnomalyQuarantine,
       "alaNetSecMonitoringGroupAnomalyCount": alaNetSecMonitoringGroupAnomalyCount,
       "alaNetSecMonitoringGroupAnomalySensitivity": alaNetSecMonitoringGroupAnomalySensitivity,
       "alaNetSecMonitoringGroupAnomalyPeriod": alaNetSecMonitoringGroupAnomalyPeriod,
       "alaNetSecMonitoringGroupRowStatus": alaNetSecMonitoringGroupRowStatus,
       "alaNetSecPortStats": alaNetSecPortStats,
       "alaNetSecPortStatsTable": alaNetSecPortStatsTable,
       "alaNetSecPortStatsEntry": alaNetSecPortStatsEntry,
       "alaNetSecPortStatsIfId": alaNetSecPortStatsIfId,
       "alaNetSecPortStatsPacket": alaNetSecPortStatsPacket,
       "alaNetSecPortStatsLastIngress": alaNetSecPortStatsLastIngress,
       "alaNetSecPortStatsLastEgress": alaNetSecPortStatsLastEgress,
       "alaNetSecPortStatsTotalIngress": alaNetSecPortStatsTotalIngress,
       "alaNetSecPortStatsTotalEgress": alaNetSecPortStatsTotalEgress,
       "alaNetSecPortAnomalyStats": alaNetSecPortAnomalyStats,
       "alaNetSecPortAnomalyStatsTable": alaNetSecPortAnomalyStatsTable,
       "alaNetSecPortAnomalyStatsEntry": alaNetSecPortAnomalyStatsEntry,
       "alaNetSecPortAnomalyStatsIfId": alaNetSecPortAnomalyStatsIfId,
       "alaNetSecPortAnomalyStatsAnomaly": alaNetSecPortAnomalyStatsAnomaly,
       "alaNetSecPortAnomalyStatsPacket": alaNetSecPortAnomalyStatsPacket,
       "alaNetSecPortAnomalyStatsCurrentIngress": alaNetSecPortAnomalyStatsCurrentIngress,
       "alaNetSecPortAnomalyStatsCurrentEgress": alaNetSecPortAnomalyStatsCurrentEgress,
       "alaNetSecPortAnomalyStatsLastIngress": alaNetSecPortAnomalyStatsLastIngress,
       "alaNetSecPortAnomalyStatsLastEgress": alaNetSecPortAnomalyStatsLastEgress,
       "alaNetSecPortAnomalySummary": alaNetSecPortAnomalySummary,
       "alaNetSecPortAnomalySummaryTable": alaNetSecPortAnomalySummaryTable,
       "alaNetSecPortAnomalySummaryEntry": alaNetSecPortAnomalySummaryEntry,
       "alaNetSecPortAnomalySummaryIfId": alaNetSecPortAnomalySummaryIfId,
       "alaNetSecPortAnomalySummaryAnomaly": alaNetSecPortAnomalySummaryAnomaly,
       "alaNetSecPortAnomalySummaryObserved": alaNetSecPortAnomalySummaryObserved,
       "alaNetSecPortAnomalySummaryDetected": alaNetSecPortAnomalySummaryDetected,
       "alaNetSecPortOp": alaNetSecPortOp,
       "alaNetSecPortOpTable": alaNetSecPortOpTable,
       "alaNetSecPortOpEntry": alaNetSecPortOpEntry,
       "alaNetSecPortOpIfId": alaNetSecPortOpIfId,
       "alaNetSecPortOpAnomaly": alaNetSecPortOpAnomaly,
       "alaNetSecPortOpState": alaNetSecPortOpState,
       "alaNetSecPortOpLog": alaNetSecPortOpLog,
       "alaNetSecPortOpTrap": alaNetSecPortOpTrap,
       "alaNetSecPortOpQuarantine": alaNetSecPortOpQuarantine,
       "alaNetSecPortOpCount": alaNetSecPortOpCount,
       "alaNetSecPortOpSensitivity": alaNetSecPortOpSensitivity,
       "alaNetSecPortOpPeriod": alaNetSecPortOpPeriod,
       "alaNetSecGroupOp": alaNetSecGroupOp,
       "alaNetSecGroupOpTable": alaNetSecGroupOpTable,
       "alaNetSecGroupOpEntry": alaNetSecGroupOpEntry,
       "alaNetSecGroupOpName": alaNetSecGroupOpName,
       "alaNetSecGroupOpAnomaly": alaNetSecGroupOpAnomaly,
       "alaNetSecGroupOpState": alaNetSecGroupOpState,
       "alaNetSecGroupOpLog": alaNetSecGroupOpLog,
       "alaNetSecGroupOpTrap": alaNetSecGroupOpTrap,
       "alaNetSecGroupOpQuarantine": alaNetSecGroupOpQuarantine,
       "alaNetSecGroupOpCount": alaNetSecGroupOpCount,
       "alaNetSecGroupOpSensitivity": alaNetSecGroupOpSensitivity,
       "alaNetSecGroupOpPeriod": alaNetSecGroupOpPeriod,
       "alaNetSecGroup": alaNetSecGroup,
       "alaNetSecGroupTable": alaNetSecGroupTable,
       "alaNetSecGroupEntry": alaNetSecGroupEntry,
       "alaNetSecGroupName": alaNetSecGroupName,
       "alaNetSecGroupMemberPorts": alaNetSecGroupMemberPorts,
       "alaNetSecGroupAnomalyCfg": alaNetSecGroupAnomalyCfg,
       "alaNetSecPortTrapsObj": alaNetSecPortTrapsObj,
       "alaNetSecPortTrapInfoIfId": alaNetSecPortTrapInfoIfId,
       "alaNetSecPortTrapInfoAnomaly": alaNetSecPortTrapInfoAnomaly,
       "alaNetSecPortTrapInfoType": alaNetSecPortTrapInfoType,
       "alcatelIND1NETSECMIBConformance": alcatelIND1NETSECMIBConformance,
       "alcatelIND1NETSECMIBGroups": alcatelIND1NETSECMIBGroups,
       "alaNetSecPortRangeComplianceGroup": alaNetSecPortRangeComplianceGroup,
       "alaNetSecMonitoringGroupComplianceGroup": alaNetSecMonitoringGroupComplianceGroup,
       "alaNetSecPortTrapsComplianceGroup": alaNetSecPortTrapsComplianceGroup,
       "alaNetSecPortStatsComplianceGroup": alaNetSecPortStatsComplianceGroup,
       "alaNetSecPortAnomalyStatsComplianceGroup": alaNetSecPortAnomalyStatsComplianceGroup,
       "alaNetSecPortAnomalySummaryComplianceGroup": alaNetSecPortAnomalySummaryComplianceGroup,
       "alaNetSecPortOpComplianceGroup": alaNetSecPortOpComplianceGroup,
       "alaNetSecGroupOpComplianceGroup": alaNetSecGroupOpComplianceGroup,
       "alaNetSecGroupComplianceGroup": alaNetSecGroupComplianceGroup,
       "alaNetSecMonitoringGroupEntryGroup": alaNetSecMonitoringGroupEntryGroup,
       "alaNetSecPortRangeGroupEntryGroup": alaNetSecPortRangeGroupEntryGroup,
       "alaNetSecPortTrapAnomalyGroup": alaNetSecPortTrapAnomalyGroup,
       "alcatelIND1NETSECMIBCompliances": alcatelIND1NETSECMIBCompliances,
       "alcatelIND1NETSECMIBCompliance": alcatelIND1NETSECMIBCompliance}
)
