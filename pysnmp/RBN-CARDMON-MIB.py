# SNMP MIB module (RBN-CARDMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-CARDMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:00 2024
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

(RbnAlarmId,
 RbnAlarmPerceivedSeverity,
 RbnAlarmProbableCause,
 RbnAlarmServiceAffecting,
 RbnAlarmType) = mibBuilder.importSymbols(
    "RBN-ALARM-TC",
    "RbnAlarmId",
    "RbnAlarmPerceivedSeverity",
    "RbnAlarmProbableCause",
    "RbnAlarmServiceAffecting",
    "RbnAlarmType")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(RbnSlot,) = mibBuilder.importSymbols(
    "RBN-TC",
    "RbnSlot")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

rbnCardMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31)
)
rbnCardMonMIB.setRevisions(
        ("2006-10-02 00:00",
         "2005-05-09 00:00",
         "2004-09-27 00:00",
         "2004-06-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnCardMonMIBNotifications_ObjectIdentity = ObjectIdentity
rbnCardMonMIBNotifications = _RbnCardMonMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 0)
)
_RbnCardMonMIBObjects_ObjectIdentity = ObjectIdentity
rbnCardMonMIBObjects = _RbnCardMonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1)
)
_RbnCardAlarmActiveTable_Object = MibTable
rbnCardAlarmActiveTable = _RbnCardAlarmActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 1)
)
if mibBuilder.loadTexts:
    rbnCardAlarmActiveTable.setStatus("current")
_RbnCardAlarmActiveEntry_Object = MibTableRow
rbnCardAlarmActiveEntry = _RbnCardAlarmActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 1, 1)
)
rbnCardAlarmActiveEntry.setIndexNames(
    (0, "RBN-CARDMON-MIB", "rbnCardAlarmSlot"),
    (0, "RBN-CARDMON-MIB", "rbnCardAlarmActiveIndex"),
)
if mibBuilder.loadTexts:
    rbnCardAlarmActiveEntry.setStatus("current")
_RbnCardAlarmSlot_Type = RbnSlot
_RbnCardAlarmSlot_Object = MibTableColumn
rbnCardAlarmSlot = _RbnCardAlarmSlot_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 1, 1, 1),
    _RbnCardAlarmSlot_Type()
)
rbnCardAlarmSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnCardAlarmSlot.setStatus("current")


class _RbnCardAlarmActiveIndex_Type(Unsigned32):
    """Custom type rbnCardAlarmActiveIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RbnCardAlarmActiveIndex_Type.__name__ = "Unsigned32"
_RbnCardAlarmActiveIndex_Object = MibTableColumn
rbnCardAlarmActiveIndex = _RbnCardAlarmActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 1, 1, 2),
    _RbnCardAlarmActiveIndex_Type()
)
rbnCardAlarmActiveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnCardAlarmActiveIndex.setStatus("current")
_RbnCardAlarmId_Type = RbnAlarmId
_RbnCardAlarmId_Object = MibTableColumn
rbnCardAlarmId = _RbnCardAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 1, 1, 3),
    _RbnCardAlarmId_Type()
)
rbnCardAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardAlarmId.setStatus("current")
_RbnCardAlarmType_Type = RbnAlarmType
_RbnCardAlarmType_Object = MibTableColumn
rbnCardAlarmType = _RbnCardAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 1, 1, 4),
    _RbnCardAlarmType_Type()
)
rbnCardAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardAlarmType.setStatus("current")
_RbnCardAlarmDateAndTime_Type = DateAndTime
_RbnCardAlarmDateAndTime_Object = MibTableColumn
rbnCardAlarmDateAndTime = _RbnCardAlarmDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 1, 1, 5),
    _RbnCardAlarmDateAndTime_Type()
)
rbnCardAlarmDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardAlarmDateAndTime.setStatus("current")


class _RbnCardAlarmDescription_Type(SnmpAdminString):
    """Custom type rbnCardAlarmDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RbnCardAlarmDescription_Type.__name__ = "SnmpAdminString"
_RbnCardAlarmDescription_Object = MibTableColumn
rbnCardAlarmDescription = _RbnCardAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 1, 1, 6),
    _RbnCardAlarmDescription_Type()
)
rbnCardAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardAlarmDescription.setStatus("current")
_RbnCardAlarmProbableCause_Type = RbnAlarmProbableCause
_RbnCardAlarmProbableCause_Object = MibTableColumn
rbnCardAlarmProbableCause = _RbnCardAlarmProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 1, 1, 7),
    _RbnCardAlarmProbableCause_Type()
)
rbnCardAlarmProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardAlarmProbableCause.setStatus("current")
_RbnCardAlarmSeverity_Type = RbnAlarmPerceivedSeverity
_RbnCardAlarmSeverity_Object = MibTableColumn
rbnCardAlarmSeverity = _RbnCardAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 1, 1, 8),
    _RbnCardAlarmSeverity_Type()
)
rbnCardAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardAlarmSeverity.setStatus("current")
_RbnCardAlarmServiceAffecting_Type = RbnAlarmServiceAffecting
_RbnCardAlarmServiceAffecting_Object = MibTableColumn
rbnCardAlarmServiceAffecting = _RbnCardAlarmServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 1, 1, 9),
    _RbnCardAlarmServiceAffecting_Type()
)
rbnCardAlarmServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardAlarmServiceAffecting.setStatus("current")
_RbnCardStatsTable_Object = MibTable
rbnCardStatsTable = _RbnCardStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2)
)
if mibBuilder.loadTexts:
    rbnCardStatsTable.setStatus("current")
_RbnCardStatsEntry_Object = MibTableRow
rbnCardStatsEntry = _RbnCardStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1)
)
rbnCardStatsEntry.setIndexNames(
    (0, "RBN-CARDMON-MIB", "rbnCardStatsSlot"),
)
if mibBuilder.loadTexts:
    rbnCardStatsEntry.setStatus("current")
_RbnCardStatsSlot_Type = RbnSlot
_RbnCardStatsSlot_Object = MibTableColumn
rbnCardStatsSlot = _RbnCardStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 1),
    _RbnCardStatsSlot_Type()
)
rbnCardStatsSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnCardStatsSlot.setStatus("current")
_RbnCardStatsTotalCircuits_Type = Gauge32
_RbnCardStatsTotalCircuits_Object = MibTableColumn
rbnCardStatsTotalCircuits = _RbnCardStatsTotalCircuits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 2),
    _RbnCardStatsTotalCircuits_Type()
)
rbnCardStatsTotalCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardStatsTotalCircuits.setStatus("current")
_RbnCardStatsUpCircuits_Type = Gauge32
_RbnCardStatsUpCircuits_Object = MibTableColumn
rbnCardStatsUpCircuits = _RbnCardStatsUpCircuits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 3),
    _RbnCardStatsUpCircuits_Type()
)
rbnCardStatsUpCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardStatsUpCircuits.setStatus("current")
_RbnCardStatsDownCircuits_Type = Gauge32
_RbnCardStatsDownCircuits_Object = MibTableColumn
rbnCardStatsDownCircuits = _RbnCardStatsDownCircuits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 4),
    _RbnCardStatsDownCircuits_Type()
)
rbnCardStatsDownCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardStatsDownCircuits.setStatus("current")
_RbnCardStatsUnboundCircuits_Type = Gauge32
_RbnCardStatsUnboundCircuits_Object = MibTableColumn
rbnCardStatsUnboundCircuits = _RbnCardStatsUnboundCircuits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 5),
    _RbnCardStatsUnboundCircuits_Type()
)
rbnCardStatsUnboundCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardStatsUnboundCircuits.setStatus("current")
_RbnCardStatsNoBindCircuits_Type = Gauge32
_RbnCardStatsNoBindCircuits_Object = MibTableColumn
rbnCardStatsNoBindCircuits = _RbnCardStatsNoBindCircuits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 6),
    _RbnCardStatsNoBindCircuits_Type()
)
rbnCardStatsNoBindCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardStatsNoBindCircuits.setStatus("current")
_RbnCardStatsBindTotalCircuits_Type = Gauge32
_RbnCardStatsBindTotalCircuits_Object = MibTableColumn
rbnCardStatsBindTotalCircuits = _RbnCardStatsBindTotalCircuits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 7),
    _RbnCardStatsBindTotalCircuits_Type()
)
rbnCardStatsBindTotalCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardStatsBindTotalCircuits.setStatus("current")
_RbnCardStatsBindIfCircuits_Type = Gauge32
_RbnCardStatsBindIfCircuits_Object = MibTableColumn
rbnCardStatsBindIfCircuits = _RbnCardStatsBindIfCircuits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 8),
    _RbnCardStatsBindIfCircuits_Type()
)
rbnCardStatsBindIfCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardStatsBindIfCircuits.setStatus("current")
_RbnCardStatsBindAuthCircuits_Type = Gauge32
_RbnCardStatsBindAuthCircuits_Object = MibTableColumn
rbnCardStatsBindAuthCircuits = _RbnCardStatsBindAuthCircuits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 9),
    _RbnCardStatsBindAuthCircuits_Type()
)
rbnCardStatsBindAuthCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardStatsBindAuthCircuits.setStatus("current")
_RbnCardStatsBindSubCircuits_Type = Gauge32
_RbnCardStatsBindSubCircuits_Object = MibTableColumn
rbnCardStatsBindSubCircuits = _RbnCardStatsBindSubCircuits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 10),
    _RbnCardStatsBindSubCircuits_Type()
)
rbnCardStatsBindSubCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardStatsBindSubCircuits.setStatus("current")
_RbnCardStatsAtmCircuits_Type = Gauge32
_RbnCardStatsAtmCircuits_Object = MibTableColumn
rbnCardStatsAtmCircuits = _RbnCardStatsAtmCircuits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 11),
    _RbnCardStatsAtmCircuits_Type()
)
rbnCardStatsAtmCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardStatsAtmCircuits.setStatus("current")
_RbnCardStatsEthCircuits_Type = Gauge32
_RbnCardStatsEthCircuits_Object = MibTableColumn
rbnCardStatsEthCircuits = _RbnCardStatsEthCircuits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 12),
    _RbnCardStatsEthCircuits_Type()
)
rbnCardStatsEthCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardStatsEthCircuits.setStatus("current")
_RbnCardStatsPppCircuits_Type = Gauge32
_RbnCardStatsPppCircuits_Object = MibTableColumn
rbnCardStatsPppCircuits = _RbnCardStatsPppCircuits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 13),
    _RbnCardStatsPppCircuits_Type()
)
rbnCardStatsPppCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardStatsPppCircuits.setStatus("current")
_RbnCardStatsPppoeCircuits_Type = Gauge32
_RbnCardStatsPppoeCircuits_Object = MibTableColumn
rbnCardStatsPppoeCircuits = _RbnCardStatsPppoeCircuits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 14),
    _RbnCardStatsPppoeCircuits_Type()
)
rbnCardStatsPppoeCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardStatsPppoeCircuits.setStatus("current")
_RbnCardStatsDot1qCircuits_Type = Gauge32
_RbnCardStatsDot1qCircuits_Object = MibTableColumn
rbnCardStatsDot1qCircuits = _RbnCardStatsDot1qCircuits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 15),
    _RbnCardStatsDot1qCircuits_Type()
)
rbnCardStatsDot1qCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardStatsDot1qCircuits.setStatus("current")
_RbnCardStatsFrCircuits_Type = Gauge32
_RbnCardStatsFrCircuits_Object = MibTableColumn
rbnCardStatsFrCircuits = _RbnCardStatsFrCircuits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 16),
    _RbnCardStatsFrCircuits_Type()
)
rbnCardStatsFrCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardStatsFrCircuits.setStatus("current")
_RbnCardStatsChdlcCircuits_Type = Gauge32
_RbnCardStatsChdlcCircuits_Object = MibTableColumn
rbnCardStatsChdlcCircuits = _RbnCardStatsChdlcCircuits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 17),
    _RbnCardStatsChdlcCircuits_Type()
)
rbnCardStatsChdlcCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardStatsChdlcCircuits.setStatus("current")
_RbnCardStatsGreCircuits_Type = Gauge32
_RbnCardStatsGreCircuits_Object = MibTableColumn
rbnCardStatsGreCircuits = _RbnCardStatsGreCircuits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 18),
    _RbnCardStatsGreCircuits_Type()
)
rbnCardStatsGreCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardStatsGreCircuits.setStatus("current")
_RbnCardStatsMplsCircuits_Type = Gauge32
_RbnCardStatsMplsCircuits_Object = MibTableColumn
rbnCardStatsMplsCircuits = _RbnCardStatsMplsCircuits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 19),
    _RbnCardStatsMplsCircuits_Type()
)
rbnCardStatsMplsCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardStatsMplsCircuits.setStatus("current")
_RbnCardStatsClipsCircuits_Type = Gauge32
_RbnCardStatsClipsCircuits_Object = MibTableColumn
rbnCardStatsClipsCircuits = _RbnCardStatsClipsCircuits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 20),
    _RbnCardStatsClipsCircuits_Type()
)
rbnCardStatsClipsCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardStatsClipsCircuits.setStatus("current")
_RbnCardStatsVplsCircuits_Type = Gauge32
_RbnCardStatsVplsCircuits_Object = MibTableColumn
rbnCardStatsVplsCircuits = _RbnCardStatsVplsCircuits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 21),
    _RbnCardStatsVplsCircuits_Type()
)
rbnCardStatsVplsCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardStatsVplsCircuits.setStatus("current")
_RbnCardStatsIpipCircuits_Type = Gauge32
_RbnCardStatsIpipCircuits_Object = MibTableColumn
rbnCardStatsIpipCircuits = _RbnCardStatsIpipCircuits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 22),
    _RbnCardStatsIpipCircuits_Type()
)
rbnCardStatsIpipCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardStatsIpipCircuits.setStatus("current")
_RbnCardStatsIpv6v4ManualCircuits_Type = Gauge32
_RbnCardStatsIpv6v4ManualCircuits_Object = MibTableColumn
rbnCardStatsIpv6v4ManualCircuits = _RbnCardStatsIpv6v4ManualCircuits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 23),
    _RbnCardStatsIpv6v4ManualCircuits_Type()
)
rbnCardStatsIpv6v4ManualCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardStatsIpv6v4ManualCircuits.setStatus("current")
_RbnCardStatsIpv6v4AutoCircuits_Type = Gauge32
_RbnCardStatsIpv6v4AutoCircuits_Object = MibTableColumn
rbnCardStatsIpv6v4AutoCircuits = _RbnCardStatsIpv6v4AutoCircuits_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 1, 2, 1, 24),
    _RbnCardStatsIpv6v4AutoCircuits_Type()
)
rbnCardStatsIpv6v4AutoCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCardStatsIpv6v4AutoCircuits.setStatus("current")
_RbnCardMonMIBConformance_ObjectIdentity = ObjectIdentity
rbnCardMonMIBConformance = _RbnCardMonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 2)
)
_RbnCardMonMIBGroups_ObjectIdentity = ObjectIdentity
rbnCardMonMIBGroups = _RbnCardMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 2, 1)
)
_RbnCardMonMIBCompliances_ObjectIdentity = ObjectIdentity
rbnCardMonMIBCompliances = _RbnCardMonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 2, 2)
)

# Managed Objects groups

rbnCardMonMIBObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 2, 1, 1)
)
rbnCardMonMIBObjectGroup.setObjects(
      *(("RBN-CARDMON-MIB", "rbnCardAlarmId"),
        ("RBN-CARDMON-MIB", "rbnCardAlarmType"),
        ("RBN-CARDMON-MIB", "rbnCardAlarmDateAndTime"),
        ("RBN-CARDMON-MIB", "rbnCardAlarmDescription"),
        ("RBN-CARDMON-MIB", "rbnCardAlarmProbableCause"),
        ("RBN-CARDMON-MIB", "rbnCardAlarmSeverity"))
)
if mibBuilder.loadTexts:
    rbnCardMonMIBObjectGroup.setStatus("current")

rbnCardStatsMIBObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 2, 1, 3)
)
rbnCardStatsMIBObjectGroup.setObjects(
      *(("RBN-CARDMON-MIB", "rbnCardStatsTotalCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsUpCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsDownCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsUnboundCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsNoBindCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsBindTotalCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsBindIfCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsBindAuthCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsBindSubCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsAtmCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsEthCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsPppCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsPppoeCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsDot1qCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsFrCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsChdlcCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsGreCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsMplsCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsClipsCircuits"))
)
if mibBuilder.loadTexts:
    rbnCardStatsMIBObjectGroup.setStatus("current")

rbnCardMonMIBObjectGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 2, 1, 4)
)
rbnCardMonMIBObjectGroup2.setObjects(
      *(("RBN-CARDMON-MIB", "rbnCardAlarmId"),
        ("RBN-CARDMON-MIB", "rbnCardAlarmType"),
        ("RBN-CARDMON-MIB", "rbnCardAlarmDateAndTime"),
        ("RBN-CARDMON-MIB", "rbnCardAlarmDescription"),
        ("RBN-CARDMON-MIB", "rbnCardAlarmProbableCause"),
        ("RBN-CARDMON-MIB", "rbnCardAlarmSeverity"),
        ("RBN-CARDMON-MIB", "rbnCardAlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    rbnCardMonMIBObjectGroup2.setStatus("current")

rbnCardStatsMIBObjectGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 2, 1, 5)
)
rbnCardStatsMIBObjectGroup2.setObjects(
      *(("RBN-CARDMON-MIB", "rbnCardStatsTotalCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsUpCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsDownCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsUnboundCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsNoBindCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsBindTotalCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsBindIfCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsBindAuthCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsBindSubCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsAtmCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsEthCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsPppCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsPppoeCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsDot1qCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsFrCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsChdlcCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsGreCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsMplsCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsClipsCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsVplsCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsIpipCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsIpv6v4ManualCircuits"),
        ("RBN-CARDMON-MIB", "rbnCardStatsIpv6v4AutoCircuits"))
)
if mibBuilder.loadTexts:
    rbnCardStatsMIBObjectGroup2.setStatus("current")


# Notification objects

rbnCardAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 0, 1)
)
rbnCardAlarm.setObjects(
      *(("RBN-CARDMON-MIB", "rbnCardAlarmId"),
        ("RBN-CARDMON-MIB", "rbnCardAlarmType"),
        ("RBN-CARDMON-MIB", "rbnCardAlarmDateAndTime"),
        ("RBN-CARDMON-MIB", "rbnCardAlarmDescription"),
        ("RBN-CARDMON-MIB", "rbnCardAlarmProbableCause"),
        ("RBN-CARDMON-MIB", "rbnCardAlarmSeverity"))
)
if mibBuilder.loadTexts:
    rbnCardAlarm.setStatus(
        "current"
    )


# Notifications groups

rbnCardMonMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 2, 1, 2)
)
rbnCardMonMIBNotificationGroup.setObjects(
    ("RBN-CARDMON-MIB", "rbnCardAlarm")
)
if mibBuilder.loadTexts:
    rbnCardMonMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rbnCardMonMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rbnCardMonMIBCompliance.setStatus(
        "current"
    )

rbnCardMonMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 2, 2, 2)
)
if mibBuilder.loadTexts:
    rbnCardMonMIBCompliance2.setStatus(
        "current"
    )

rbnCardMonMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 2, 2, 3)
)
if mibBuilder.loadTexts:
    rbnCardMonMIBCompliance3.setStatus(
        "current"
    )

rbnCardMonMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 31, 2, 2, 4)
)
if mibBuilder.loadTexts:
    rbnCardMonMIBCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-CARDMON-MIB",
    **{"rbnCardMonMIB": rbnCardMonMIB,
       "rbnCardMonMIBNotifications": rbnCardMonMIBNotifications,
       "rbnCardAlarm": rbnCardAlarm,
       "rbnCardMonMIBObjects": rbnCardMonMIBObjects,
       "rbnCardAlarmActiveTable": rbnCardAlarmActiveTable,
       "rbnCardAlarmActiveEntry": rbnCardAlarmActiveEntry,
       "rbnCardAlarmSlot": rbnCardAlarmSlot,
       "rbnCardAlarmActiveIndex": rbnCardAlarmActiveIndex,
       "rbnCardAlarmId": rbnCardAlarmId,
       "rbnCardAlarmType": rbnCardAlarmType,
       "rbnCardAlarmDateAndTime": rbnCardAlarmDateAndTime,
       "rbnCardAlarmDescription": rbnCardAlarmDescription,
       "rbnCardAlarmProbableCause": rbnCardAlarmProbableCause,
       "rbnCardAlarmSeverity": rbnCardAlarmSeverity,
       "rbnCardAlarmServiceAffecting": rbnCardAlarmServiceAffecting,
       "rbnCardStatsTable": rbnCardStatsTable,
       "rbnCardStatsEntry": rbnCardStatsEntry,
       "rbnCardStatsSlot": rbnCardStatsSlot,
       "rbnCardStatsTotalCircuits": rbnCardStatsTotalCircuits,
       "rbnCardStatsUpCircuits": rbnCardStatsUpCircuits,
       "rbnCardStatsDownCircuits": rbnCardStatsDownCircuits,
       "rbnCardStatsUnboundCircuits": rbnCardStatsUnboundCircuits,
       "rbnCardStatsNoBindCircuits": rbnCardStatsNoBindCircuits,
       "rbnCardStatsBindTotalCircuits": rbnCardStatsBindTotalCircuits,
       "rbnCardStatsBindIfCircuits": rbnCardStatsBindIfCircuits,
       "rbnCardStatsBindAuthCircuits": rbnCardStatsBindAuthCircuits,
       "rbnCardStatsBindSubCircuits": rbnCardStatsBindSubCircuits,
       "rbnCardStatsAtmCircuits": rbnCardStatsAtmCircuits,
       "rbnCardStatsEthCircuits": rbnCardStatsEthCircuits,
       "rbnCardStatsPppCircuits": rbnCardStatsPppCircuits,
       "rbnCardStatsPppoeCircuits": rbnCardStatsPppoeCircuits,
       "rbnCardStatsDot1qCircuits": rbnCardStatsDot1qCircuits,
       "rbnCardStatsFrCircuits": rbnCardStatsFrCircuits,
       "rbnCardStatsChdlcCircuits": rbnCardStatsChdlcCircuits,
       "rbnCardStatsGreCircuits": rbnCardStatsGreCircuits,
       "rbnCardStatsMplsCircuits": rbnCardStatsMplsCircuits,
       "rbnCardStatsClipsCircuits": rbnCardStatsClipsCircuits,
       "rbnCardStatsVplsCircuits": rbnCardStatsVplsCircuits,
       "rbnCardStatsIpipCircuits": rbnCardStatsIpipCircuits,
       "rbnCardStatsIpv6v4ManualCircuits": rbnCardStatsIpv6v4ManualCircuits,
       "rbnCardStatsIpv6v4AutoCircuits": rbnCardStatsIpv6v4AutoCircuits,
       "rbnCardMonMIBConformance": rbnCardMonMIBConformance,
       "rbnCardMonMIBGroups": rbnCardMonMIBGroups,
       "rbnCardMonMIBObjectGroup": rbnCardMonMIBObjectGroup,
       "rbnCardMonMIBNotificationGroup": rbnCardMonMIBNotificationGroup,
       "rbnCardStatsMIBObjectGroup": rbnCardStatsMIBObjectGroup,
       "rbnCardMonMIBObjectGroup2": rbnCardMonMIBObjectGroup2,
       "rbnCardStatsMIBObjectGroup2": rbnCardStatsMIBObjectGroup2,
       "rbnCardMonMIBCompliances": rbnCardMonMIBCompliances,
       "rbnCardMonMIBCompliance": rbnCardMonMIBCompliance,
       "rbnCardMonMIBCompliance2": rbnCardMonMIBCompliance2,
       "rbnCardMonMIBCompliance3": rbnCardMonMIBCompliance3,
       "rbnCardMonMIBCompliance4": rbnCardMonMIBCompliance4}
)
