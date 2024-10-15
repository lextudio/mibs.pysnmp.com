# SNMP MIB module (HP-IF-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-IF-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:32 2024
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

(hpProcurveCommon,) = mibBuilder.importSymbols(
    "HP-BASE-MIB",
    "hpProcurveCommon")

(ifEntry,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpIfExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 2)
)
hpIfExtMIB.setRevisions(
        ("2005-02-01 14:55",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpifMIBObjects_ObjectIdentity = ObjectIdentity
hpifMIBObjects = _HpifMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 2, 1)
)
_HpifStats_ObjectIdentity = ObjectIdentity
hpifStats = _HpifStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 2, 1, 1)
)
_HpifStatsTable_Object = MibTable
hpifStatsTable = _HpifStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpifStatsTable.setStatus("current")
_HpifStatsEntry_Object = MibTableRow
hpifStatsEntry = _HpifStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpifStatsEntry.setStatus("current")
_HpifStatsSlot_Type = Unsigned32
_HpifStatsSlot_Object = MibTableColumn
hpifStatsSlot = _HpifStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 2, 1, 1, 1, 1, 1),
    _HpifStatsSlot_Type()
)
hpifStatsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpifStatsSlot.setStatus("current")
_HpifStatsPort_Type = Unsigned32
_HpifStatsPort_Object = MibTableColumn
hpifStatsPort = _HpifStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 2, 1, 1, 1, 1, 2),
    _HpifStatsPort_Type()
)
hpifStatsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpifStatsPort.setStatus("current")
_HpifStatsNumClients_Type = Gauge32
_HpifStatsNumClients_Object = MibTableColumn
hpifStatsNumClients = _HpifStatsNumClients_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 2, 1, 1, 1, 1, 3),
    _HpifStatsNumClients_Type()
)
hpifStatsNumClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpifStatsNumClients.setStatus("current")
_HpifStatsExtRoamsTo_Type = Counter32
_HpifStatsExtRoamsTo_Object = MibTableColumn
hpifStatsExtRoamsTo = _HpifStatsExtRoamsTo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 2, 1, 1, 1, 1, 4),
    _HpifStatsExtRoamsTo_Type()
)
hpifStatsExtRoamsTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpifStatsExtRoamsTo.setStatus("current")
_HpifStatsExtRoamsFrom_Type = Counter32
_HpifStatsExtRoamsFrom_Object = MibTableColumn
hpifStatsExtRoamsFrom = _HpifStatsExtRoamsFrom_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 2, 1, 1, 1, 1, 5),
    _HpifStatsExtRoamsFrom_Type()
)
hpifStatsExtRoamsFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpifStatsExtRoamsFrom.setStatus("current")
_HpifStatsIntRoamsTo_Type = Counter32
_HpifStatsIntRoamsTo_Object = MibTableColumn
hpifStatsIntRoamsTo = _HpifStatsIntRoamsTo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 2, 1, 1, 1, 1, 6),
    _HpifStatsIntRoamsTo_Type()
)
hpifStatsIntRoamsTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpifStatsIntRoamsTo.setStatus("current")
_HpifStatsIntRoamsFrom_Type = Counter32
_HpifStatsIntRoamsFrom_Object = MibTableColumn
hpifStatsIntRoamsFrom = _HpifStatsIntRoamsFrom_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 2, 1, 1, 1, 1, 7),
    _HpifStatsIntRoamsFrom_Type()
)
hpifStatsIntRoamsFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpifStatsIntRoamsFrom.setStatus("current")
_HpifStatsNumSessions_Type = Gauge32
_HpifStatsNumSessions_Object = MibTableColumn
hpifStatsNumSessions = _HpifStatsNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 2, 1, 1, 1, 1, 8),
    _HpifStatsNumSessions_Type()
)
hpifStatsNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpifStatsNumSessions.setStatus("current")
_HpifNotificationConfig_ObjectIdentity = ObjectIdentity
hpifNotificationConfig = _HpifNotificationConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 2, 1, 3)
)
_HpifExtMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
hpifExtMIBNotificationsPrefix = _HpifExtMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 2, 2)
)
_HpifExtMIBNotifications_ObjectIdentity = ObjectIdentity
hpifExtMIBNotifications = _HpifExtMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 2, 2, 0)
)
_HpIfExtMIBConformance_ObjectIdentity = ObjectIdentity
hpIfExtMIBConformance = _HpIfExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 2, 3)
)
_HpifCompliances_ObjectIdentity = ObjectIdentity
hpifCompliances = _HpifCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 2, 3, 1)
)
_HpifGroups_ObjectIdentity = ObjectIdentity
hpifGroups = _HpifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 2, 3, 2)
)
ifEntry.registerAugmentions(
    ("HP-IF-EXT-MIB",
     "hpifStatsEntry")
)
hpifStatsEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups

hpifStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 2, 3, 2, 1)
)
hpifStatsGroup.setObjects(
      *(("HP-IF-EXT-MIB", "hpifStatsSlot"),
        ("HP-IF-EXT-MIB", "hpifStatsPort"),
        ("HP-IF-EXT-MIB", "hpifStatsNumClients"),
        ("HP-IF-EXT-MIB", "hpifStatsExtRoamsTo"),
        ("HP-IF-EXT-MIB", "hpifStatsExtRoamsFrom"),
        ("HP-IF-EXT-MIB", "hpifStatsIntRoamsTo"),
        ("HP-IF-EXT-MIB", "hpifStatsIntRoamsFrom"),
        ("HP-IF-EXT-MIB", "hpifStatsNumSessions"))
)
if mibBuilder.loadTexts:
    hpifStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpifExtMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpifExtMIBCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-IF-EXT-MIB",
    **{"hpIfExtMIB": hpIfExtMIB,
       "hpifMIBObjects": hpifMIBObjects,
       "hpifStats": hpifStats,
       "hpifStatsTable": hpifStatsTable,
       "hpifStatsEntry": hpifStatsEntry,
       "hpifStatsSlot": hpifStatsSlot,
       "hpifStatsPort": hpifStatsPort,
       "hpifStatsNumClients": hpifStatsNumClients,
       "hpifStatsExtRoamsTo": hpifStatsExtRoamsTo,
       "hpifStatsExtRoamsFrom": hpifStatsExtRoamsFrom,
       "hpifStatsIntRoamsTo": hpifStatsIntRoamsTo,
       "hpifStatsIntRoamsFrom": hpifStatsIntRoamsFrom,
       "hpifStatsNumSessions": hpifStatsNumSessions,
       "hpifNotificationConfig": hpifNotificationConfig,
       "hpifExtMIBNotificationsPrefix": hpifExtMIBNotificationsPrefix,
       "hpifExtMIBNotifications": hpifExtMIBNotifications,
       "hpIfExtMIBConformance": hpIfExtMIBConformance,
       "hpifCompliances": hpifCompliances,
       "hpifExtMIBCompliance1": hpifExtMIBCompliance1,
       "hpifGroups": hpifGroups,
       "hpifStatsGroup": hpifStatsGroup}
)
