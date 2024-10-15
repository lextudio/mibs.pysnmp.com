# SNMP MIB module (CISCO-PFC-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PFC-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:43 2024
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

(QosQueueNumber,) = mibBuilder.importSymbols(
    "CISCO-QOS-TC-MIB",
    "QosQueueNumber")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoPfcExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 813)
)
ciscoPfcExtMIB.setRevisions(
        ("2016-04-28 00:00",
         "2013-09-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoPfcExtMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoPfcExtMIBNotifs = _CiscoPfcExtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 0)
)
_CiscoPfcExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoPfcExtMIBObjects = _CiscoPfcExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 1)
)
_CpfcIfTable_Object = MibTable
cpfcIfTable = _CpfcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 1, 1)
)
if mibBuilder.loadTexts:
    cpfcIfTable.setStatus("current")
_CpfcIfEntry_Object = MibTableRow
cpfcIfEntry = _CpfcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 1, 1, 1)
)
cpfcIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cpfcIfEntry.setStatus("current")
_CpfcIfRequests_Type = Counter64
_CpfcIfRequests_Object = MibTableColumn
cpfcIfRequests = _CpfcIfRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 1, 1, 1, 1),
    _CpfcIfRequests_Type()
)
cpfcIfRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfcIfRequests.setStatus("current")
_CpfcIfIndications_Type = Counter64
_CpfcIfIndications_Object = MibTableColumn
cpfcIfIndications = _CpfcIfIndications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 1, 1, 1, 2),
    _CpfcIfIndications_Type()
)
cpfcIfIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfcIfIndications.setStatus("current")
_CpfcIfPriorityTable_Object = MibTable
cpfcIfPriorityTable = _CpfcIfPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 1, 2)
)
if mibBuilder.loadTexts:
    cpfcIfPriorityTable.setStatus("current")
_CpfcIfPriorityEntry_Object = MibTableRow
cpfcIfPriorityEntry = _CpfcIfPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 1, 2, 1)
)
cpfcIfPriorityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-PFC-EXT-MIB", "cpfcIfPriorityValue"),
)
if mibBuilder.loadTexts:
    cpfcIfPriorityEntry.setStatus("current")


class _CpfcIfPriorityValue_Type(Integer32):
    """Custom type cpfcIfPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CpfcIfPriorityValue_Type.__name__ = "Integer32"
_CpfcIfPriorityValue_Object = MibTableColumn
cpfcIfPriorityValue = _CpfcIfPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 1, 2, 1, 1),
    _CpfcIfPriorityValue_Type()
)
cpfcIfPriorityValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpfcIfPriorityValue.setStatus("current")
_CpfcIfPriorityRequests_Type = Counter64
_CpfcIfPriorityRequests_Object = MibTableColumn
cpfcIfPriorityRequests = _CpfcIfPriorityRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 1, 2, 1, 2),
    _CpfcIfPriorityRequests_Type()
)
cpfcIfPriorityRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfcIfPriorityRequests.setStatus("current")
_CpfcIfPriorityIndications_Type = Counter64
_CpfcIfPriorityIndications_Object = MibTableColumn
cpfcIfPriorityIndications = _CpfcIfPriorityIndications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 1, 2, 1, 3),
    _CpfcIfPriorityIndications_Type()
)
cpfcIfPriorityIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfcIfPriorityIndications.setStatus("current")
_CpfcWatchdogIfQueueInfoTable_Object = MibTable
cpfcWatchdogIfQueueInfoTable = _CpfcWatchdogIfQueueInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 1, 3)
)
if mibBuilder.loadTexts:
    cpfcWatchdogIfQueueInfoTable.setStatus("current")
_CpfcWatchdogIfQueueInfoEntry_Object = MibTableRow
cpfcWatchdogIfQueueInfoEntry = _CpfcWatchdogIfQueueInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 1, 3, 1)
)
cpfcWatchdogIfQueueInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-PFC-EXT-MIB", "cpfcWatchdogIfQueueNumber"),
)
if mibBuilder.loadTexts:
    cpfcWatchdogIfQueueInfoEntry.setStatus("current")
_CpfcWatchdogIfQueueNumber_Type = QosQueueNumber
_CpfcWatchdogIfQueueNumber_Object = MibTableColumn
cpfcWatchdogIfQueueNumber = _CpfcWatchdogIfQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 1, 3, 1, 1),
    _CpfcWatchdogIfQueueNumber_Type()
)
cpfcWatchdogIfQueueNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpfcWatchdogIfQueueNumber.setStatus("current")


class _CpfcWatchdogIfQueueState_Type(Integer32):
    """Custom type cpfcWatchdogIfQueueState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notApplicable", 3),
          ("shutdown", 2))
    )


_CpfcWatchdogIfQueueState_Type.__name__ = "Integer32"
_CpfcWatchdogIfQueueState_Object = MibTableColumn
cpfcWatchdogIfQueueState = _CpfcWatchdogIfQueueState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 1, 3, 1, 2),
    _CpfcWatchdogIfQueueState_Type()
)
cpfcWatchdogIfQueueState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfcWatchdogIfQueueState.setStatus("current")
_CpfcWatchdogIfQueueShutdowns_Type = Counter64
_CpfcWatchdogIfQueueShutdowns_Object = MibTableColumn
cpfcWatchdogIfQueueShutdowns = _CpfcWatchdogIfQueueShutdowns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 1, 3, 1, 3),
    _CpfcWatchdogIfQueueShutdowns_Type()
)
cpfcWatchdogIfQueueShutdowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfcWatchdogIfQueueShutdowns.setStatus("current")
_CpfcWatchdogIfQueueRestores_Type = Counter64
_CpfcWatchdogIfQueueRestores_Object = MibTableColumn
cpfcWatchdogIfQueueRestores = _CpfcWatchdogIfQueueRestores_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 1, 3, 1, 4),
    _CpfcWatchdogIfQueueRestores_Type()
)
cpfcWatchdogIfQueueRestores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfcWatchdogIfQueueRestores.setStatus("current")
_CpfcWatchdogIfQueueTotalDropPkts_Type = Counter64
_CpfcWatchdogIfQueueTotalDropPkts_Object = MibTableColumn
cpfcWatchdogIfQueueTotalDropPkts = _CpfcWatchdogIfQueueTotalDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 1, 3, 1, 5),
    _CpfcWatchdogIfQueueTotalDropPkts_Type()
)
cpfcWatchdogIfQueueTotalDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfcWatchdogIfQueueTotalDropPkts.setStatus("current")
_CpfcWatchdogIfQueueDropPkts_Type = CounterBasedGauge64
_CpfcWatchdogIfQueueDropPkts_Object = MibTableColumn
cpfcWatchdogIfQueueDropPkts = _CpfcWatchdogIfQueueDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 1, 3, 1, 6),
    _CpfcWatchdogIfQueueDropPkts_Type()
)
cpfcWatchdogIfQueueDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpfcWatchdogIfQueueDropPkts.setStatus("current")
_CiscoPfcExtMIBConform_ObjectIdentity = ObjectIdentity
ciscoPfcExtMIBConform = _CiscoPfcExtMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 2)
)
_CiscoPfcExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoPfcExtMIBCompliances = _CiscoPfcExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 2, 1)
)
_CiscoPfcExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoPfcExtMIBGroups = _CiscoPfcExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 2, 2)
)

# Managed Objects groups

ciscoPfcExtIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 2, 2, 1)
)
ciscoPfcExtIfGroup.setObjects(
      *(("CISCO-PFC-EXT-MIB", "cpfcIfRequests"),
        ("CISCO-PFC-EXT-MIB", "cpfcIfIndications"))
)
if mibBuilder.loadTexts:
    ciscoPfcExtIfGroup.setStatus("current")

ciscoPfcExtIfPriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 2, 2, 2)
)
ciscoPfcExtIfPriorityGroup.setObjects(
      *(("CISCO-PFC-EXT-MIB", "cpfcIfPriorityRequests"),
        ("CISCO-PFC-EXT-MIB", "cpfcIfPriorityIndications"))
)
if mibBuilder.loadTexts:
    ciscoPfcExtIfPriorityGroup.setStatus("current")

ciscoPfcExtWatchdogIfQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 2, 2, 3)
)
ciscoPfcExtWatchdogIfQueueGroup.setObjects(
      *(("CISCO-PFC-EXT-MIB", "cpfcWatchdogIfQueueState"),
        ("CISCO-PFC-EXT-MIB", "cpfcWatchdogIfQueueShutdowns"),
        ("CISCO-PFC-EXT-MIB", "cpfcWatchdogIfQueueRestores"),
        ("CISCO-PFC-EXT-MIB", "cpfcWatchdogIfQueueTotalDropPkts"),
        ("CISCO-PFC-EXT-MIB", "cpfcWatchdogIfQueueDropPkts"))
)
if mibBuilder.loadTexts:
    ciscoPfcExtWatchdogIfQueueGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoPfcExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoPfcExtMIBCompliance.setStatus(
        "deprecated"
    )

ciscoPfcExtMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 813, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoPfcExtMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PFC-EXT-MIB",
    **{"ciscoPfcExtMIB": ciscoPfcExtMIB,
       "ciscoPfcExtMIBNotifs": ciscoPfcExtMIBNotifs,
       "ciscoPfcExtMIBObjects": ciscoPfcExtMIBObjects,
       "cpfcIfTable": cpfcIfTable,
       "cpfcIfEntry": cpfcIfEntry,
       "cpfcIfRequests": cpfcIfRequests,
       "cpfcIfIndications": cpfcIfIndications,
       "cpfcIfPriorityTable": cpfcIfPriorityTable,
       "cpfcIfPriorityEntry": cpfcIfPriorityEntry,
       "cpfcIfPriorityValue": cpfcIfPriorityValue,
       "cpfcIfPriorityRequests": cpfcIfPriorityRequests,
       "cpfcIfPriorityIndications": cpfcIfPriorityIndications,
       "cpfcWatchdogIfQueueInfoTable": cpfcWatchdogIfQueueInfoTable,
       "cpfcWatchdogIfQueueInfoEntry": cpfcWatchdogIfQueueInfoEntry,
       "cpfcWatchdogIfQueueNumber": cpfcWatchdogIfQueueNumber,
       "cpfcWatchdogIfQueueState": cpfcWatchdogIfQueueState,
       "cpfcWatchdogIfQueueShutdowns": cpfcWatchdogIfQueueShutdowns,
       "cpfcWatchdogIfQueueRestores": cpfcWatchdogIfQueueRestores,
       "cpfcWatchdogIfQueueTotalDropPkts": cpfcWatchdogIfQueueTotalDropPkts,
       "cpfcWatchdogIfQueueDropPkts": cpfcWatchdogIfQueueDropPkts,
       "ciscoPfcExtMIBConform": ciscoPfcExtMIBConform,
       "ciscoPfcExtMIBCompliances": ciscoPfcExtMIBCompliances,
       "ciscoPfcExtMIBCompliance": ciscoPfcExtMIBCompliance,
       "ciscoPfcExtMIBCompliance2": ciscoPfcExtMIBCompliance2,
       "ciscoPfcExtMIBGroups": ciscoPfcExtMIBGroups,
       "ciscoPfcExtIfGroup": ciscoPfcExtIfGroup,
       "ciscoPfcExtIfPriorityGroup": ciscoPfcExtIfPriorityGroup,
       "ciscoPfcExtWatchdogIfQueueGroup": ciscoPfcExtWatchdogIfQueueGroup}
)
