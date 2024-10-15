# SNMP MIB module (ALTIGA-LBSSF-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-LBSSF-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:15 2024
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

(alLBSSFMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alLBSSFMibModule")

(alLBSSFGroup,
 alStatsLBSSF) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alLBSSFGroup",
    "alStatsLBSSF")

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

altigaLBSSFStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 41, 2)
)
altigaLBSSFStatsMibModule.setRevisions(
        ("2002-09-05 13:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DeviceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("vpn3002", 8),
          ("vpn3005", 3),
          ("vpn3015", 4),
          ("vpn3030", 5),
          ("vpn3060", 6),
          ("vpn3080", 7))
    )



class DeviceRole(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("slave", 2),
          ("virtualMaster", 1))
    )



# MIB Managed Objects in the order of their OIDs

_AltigaLBSSFStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaLBSSFStatsMibConformance = _AltigaLBSSFStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 41, 2, 1)
)
_AltigaLBSSFStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaLBSSFStatsMibCompliances = _AltigaLBSSFStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 41, 2, 1, 1)
)
_AlStatsLBSSFGlobal_ObjectIdentity = ObjectIdentity
alStatsLBSSFGlobal = _AlStatsLBSSFGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 36, 1)
)
_AlLBSSFRole_Type = DeviceRole
_AlLBSSFRole_Object = MibScalar
alLBSSFRole = _AlLBSSFRole_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 36, 1, 1),
    _AlLBSSFRole_Type()
)
alLBSSFRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLBSSFRole.setStatus("current")
_AlLBSSFDeviceType_Type = DeviceType
_AlLBSSFDeviceType_Object = MibScalar
alLBSSFDeviceType = _AlLBSSFDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 36, 1, 2),
    _AlLBSSFDeviceType_Type()
)
alLBSSFDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLBSSFDeviceType.setStatus("current")
_AlLBSSFActive_Type = TruthValue
_AlLBSSFActive_Object = MibScalar
alLBSSFActive = _AlLBSSFActive_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 36, 1, 3),
    _AlLBSSFActive_Type()
)
alLBSSFActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLBSSFActive.setStatus("current")


class _AlLBSSFNumberOfPeers_Type(Gauge32):
    """Custom type alLBSSFNumberOfPeers based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_AlLBSSFNumberOfPeers_Type.__name__ = "Gauge32"
_AlLBSSFNumberOfPeers_Object = MibScalar
alLBSSFNumberOfPeers = _AlLBSSFNumberOfPeers_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 36, 1, 4),
    _AlLBSSFNumberOfPeers_Type()
)
alLBSSFNumberOfPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLBSSFNumberOfPeers.setStatus("current")


class _AlLBSSFLoad_Type(Gauge32):
    """Custom type alLBSSFLoad based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AlLBSSFLoad_Type.__name__ = "Gauge32"
_AlLBSSFLoad_Object = MibScalar
alLBSSFLoad = _AlLBSSFLoad_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 36, 1, 5),
    _AlLBSSFLoad_Type()
)
alLBSSFLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLBSSFLoad.setStatus("current")
_AlLBSSFPeerTable_Object = MibTable
alLBSSFPeerTable = _AlLBSSFPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 36, 2)
)
if mibBuilder.loadTexts:
    alLBSSFPeerTable.setStatus("current")
_AlLBSSFPeerEntry_Object = MibTableRow
alLBSSFPeerEntry = _AlLBSSFPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 36, 2, 1)
)
alLBSSFPeerEntry.setIndexNames(
    (0, "ALTIGA-LBSSF-STATS-MIB", "alLBSSFPeerPrivIpAddress"),
)
if mibBuilder.loadTexts:
    alLBSSFPeerEntry.setStatus("current")
_AlLBSSFPeerRowStatus_Type = RowStatus
_AlLBSSFPeerRowStatus_Object = MibTableColumn
alLBSSFPeerRowStatus = _AlLBSSFPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 36, 2, 1, 1),
    _AlLBSSFPeerRowStatus_Type()
)
alLBSSFPeerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLBSSFPeerRowStatus.setStatus("current")
_AlLBSSFPeerPrivIpAddress_Type = IpAddress
_AlLBSSFPeerPrivIpAddress_Object = MibTableColumn
alLBSSFPeerPrivIpAddress = _AlLBSSFPeerPrivIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 36, 2, 1, 2),
    _AlLBSSFPeerPrivIpAddress_Type()
)
alLBSSFPeerPrivIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLBSSFPeerPrivIpAddress.setStatus("current")
_AlLBSSFPeerPubIpAddress_Type = IpAddress
_AlLBSSFPeerPubIpAddress_Object = MibTableColumn
alLBSSFPeerPubIpAddress = _AlLBSSFPeerPubIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 36, 2, 1, 3),
    _AlLBSSFPeerPubIpAddress_Type()
)
alLBSSFPeerPubIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLBSSFPeerPubIpAddress.setStatus("current")
_AlLBSSFPeerMappedPubIpAddress_Type = IpAddress
_AlLBSSFPeerMappedPubIpAddress_Object = MibTableColumn
alLBSSFPeerMappedPubIpAddress = _AlLBSSFPeerMappedPubIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 36, 2, 1, 4),
    _AlLBSSFPeerMappedPubIpAddress_Type()
)
alLBSSFPeerMappedPubIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLBSSFPeerMappedPubIpAddress.setStatus("current")
_AlLBSSFPeerActive_Type = TruthValue
_AlLBSSFPeerActive_Object = MibTableColumn
alLBSSFPeerActive = _AlLBSSFPeerActive_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 36, 2, 1, 5),
    _AlLBSSFPeerActive_Type()
)
alLBSSFPeerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLBSSFPeerActive.setStatus("current")


class _AlLBSSFPeerFaultZone_Type(Integer32):
    """Custom type alLBSSFPeerFaultZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_AlLBSSFPeerFaultZone_Type.__name__ = "Integer32"
_AlLBSSFPeerFaultZone_Object = MibTableColumn
alLBSSFPeerFaultZone = _AlLBSSFPeerFaultZone_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 36, 2, 1, 6),
    _AlLBSSFPeerFaultZone_Type()
)
alLBSSFPeerFaultZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLBSSFPeerFaultZone.setStatus("current")
_AlLBSSFPeerRole_Type = DeviceRole
_AlLBSSFPeerRole_Object = MibTableColumn
alLBSSFPeerRole = _AlLBSSFPeerRole_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 36, 2, 1, 7),
    _AlLBSSFPeerRole_Type()
)
alLBSSFPeerRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLBSSFPeerRole.setStatus("current")
_AlLBSSFPeerDeviceType_Type = DeviceType
_AlLBSSFPeerDeviceType_Object = MibTableColumn
alLBSSFPeerDeviceType = _AlLBSSFPeerDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 36, 2, 1, 8),
    _AlLBSSFPeerDeviceType_Type()
)
alLBSSFPeerDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLBSSFPeerDeviceType.setStatus("current")


class _AlLBSSFPeerLoad_Type(Gauge32):
    """Custom type alLBSSFPeerLoad based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AlLBSSFPeerLoad_Type.__name__ = "Gauge32"
_AlLBSSFPeerLoad_Object = MibTableColumn
alLBSSFPeerLoad = _AlLBSSFPeerLoad_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 36, 2, 1, 9),
    _AlLBSSFPeerLoad_Type()
)
alLBSSFPeerLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLBSSFPeerLoad.setStatus("current")


class _AlLBSSFPeerPriority_Type(Integer32):
    """Custom type alLBSSFPeerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AlLBSSFPeerPriority_Type.__name__ = "Integer32"
_AlLBSSFPeerPriority_Object = MibTableColumn
alLBSSFPeerPriority = _AlLBSSFPeerPriority_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 36, 2, 1, 10),
    _AlLBSSFPeerPriority_Type()
)
alLBSSFPeerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLBSSFPeerPriority.setStatus("current")


class _AlLBSSFPeerActiveSessions_Type(Gauge32):
    """Custom type alLBSSFPeerActiveSessions based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_AlLBSSFPeerActiveSessions_Type.__name__ = "Gauge32"
_AlLBSSFPeerActiveSessions_Object = MibTableColumn
alLBSSFPeerActiveSessions = _AlLBSSFPeerActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 36, 2, 1, 11),
    _AlLBSSFPeerActiveSessions_Type()
)
alLBSSFPeerActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLBSSFPeerActiveSessions.setStatus("current")
_AlLBSSFPeerJoinTime_Type = TimeTicks
_AlLBSSFPeerJoinTime_Object = MibTableColumn
alLBSSFPeerJoinTime = _AlLBSSFPeerJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 36, 2, 1, 12),
    _AlLBSSFPeerJoinTime_Type()
)
alLBSSFPeerJoinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLBSSFPeerJoinTime.setStatus("current")

# Managed Objects groups

altigaStatsLBSSFGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 36, 3)
)
altigaStatsLBSSFGroup.setObjects(
      *(("ALTIGA-LBSSF-STATS-MIB", "alLBSSFRole"),
        ("ALTIGA-LBSSF-STATS-MIB", "alLBSSFDeviceType"),
        ("ALTIGA-LBSSF-STATS-MIB", "alLBSSFActive"),
        ("ALTIGA-LBSSF-STATS-MIB", "alLBSSFNumberOfPeers"),
        ("ALTIGA-LBSSF-STATS-MIB", "alLBSSFLoad"),
        ("ALTIGA-LBSSF-STATS-MIB", "alLBSSFPeerRowStatus"),
        ("ALTIGA-LBSSF-STATS-MIB", "alLBSSFPeerPrivIpAddress"),
        ("ALTIGA-LBSSF-STATS-MIB", "alLBSSFPeerPubIpAddress"),
        ("ALTIGA-LBSSF-STATS-MIB", "alLBSSFPeerMappedPubIpAddress"),
        ("ALTIGA-LBSSF-STATS-MIB", "alLBSSFPeerActive"),
        ("ALTIGA-LBSSF-STATS-MIB", "alLBSSFPeerFaultZone"),
        ("ALTIGA-LBSSF-STATS-MIB", "alLBSSFPeerRole"),
        ("ALTIGA-LBSSF-STATS-MIB", "alLBSSFPeerDeviceType"),
        ("ALTIGA-LBSSF-STATS-MIB", "alLBSSFPeerLoad"),
        ("ALTIGA-LBSSF-STATS-MIB", "alLBSSFPeerPriority"),
        ("ALTIGA-LBSSF-STATS-MIB", "alLBSSFPeerActiveSessions"),
        ("ALTIGA-LBSSF-STATS-MIB", "alLBSSFPeerJoinTime"))
)
if mibBuilder.loadTexts:
    altigaStatsLBSSFGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaLBSSFStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 41, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaLBSSFStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-LBSSF-STATS-MIB",
    **{"DeviceType": DeviceType,
       "DeviceRole": DeviceRole,
       "altigaLBSSFStatsMibModule": altigaLBSSFStatsMibModule,
       "altigaLBSSFStatsMibConformance": altigaLBSSFStatsMibConformance,
       "altigaLBSSFStatsMibCompliances": altigaLBSSFStatsMibCompliances,
       "altigaLBSSFStatsMibCompliance": altigaLBSSFStatsMibCompliance,
       "altigaStatsLBSSFGroup": altigaStatsLBSSFGroup,
       "alStatsLBSSFGlobal": alStatsLBSSFGlobal,
       "alLBSSFRole": alLBSSFRole,
       "alLBSSFDeviceType": alLBSSFDeviceType,
       "alLBSSFActive": alLBSSFActive,
       "alLBSSFNumberOfPeers": alLBSSFNumberOfPeers,
       "alLBSSFLoad": alLBSSFLoad,
       "alLBSSFPeerTable": alLBSSFPeerTable,
       "alLBSSFPeerEntry": alLBSSFPeerEntry,
       "alLBSSFPeerRowStatus": alLBSSFPeerRowStatus,
       "alLBSSFPeerPrivIpAddress": alLBSSFPeerPrivIpAddress,
       "alLBSSFPeerPubIpAddress": alLBSSFPeerPubIpAddress,
       "alLBSSFPeerMappedPubIpAddress": alLBSSFPeerMappedPubIpAddress,
       "alLBSSFPeerActive": alLBSSFPeerActive,
       "alLBSSFPeerFaultZone": alLBSSFPeerFaultZone,
       "alLBSSFPeerRole": alLBSSFPeerRole,
       "alLBSSFPeerDeviceType": alLBSSFPeerDeviceType,
       "alLBSSFPeerLoad": alLBSSFPeerLoad,
       "alLBSSFPeerPriority": alLBSSFPeerPriority,
       "alLBSSFPeerActiveSessions": alLBSSFPeerActiveSessions,
       "alLBSSFPeerJoinTime": alLBSSFPeerJoinTime}
)
