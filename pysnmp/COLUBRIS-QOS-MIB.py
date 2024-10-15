# SNMP MIB module (COLUBRIS-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COLUBRIS-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:23 2024
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

(colubrisMgmtV2,) = mibBuilder.importSymbols(
    "COLUBRIS-SMI",
    "colubrisMgmtV2")

(ColubrisPriorityQueue,) = mibBuilder.importSymbols(
    "COLUBRIS-TC",
    "ColubrisPriorityQueue")

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

colubrisQOS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 13)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ColubrisQOSMIBObjects_ObjectIdentity = ObjectIdentity
colubrisQOSMIBObjects = _ColubrisQOSMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 13, 1)
)
_CoQOSStatistics_ObjectIdentity = ObjectIdentity
coQOSStatistics = _CoQOSStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 13, 1, 1)
)
_CoQOSCountersTable_Object = MibTable
coQOSCountersTable = _CoQOSCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 13, 1, 1, 1)
)
if mibBuilder.loadTexts:
    coQOSCountersTable.setStatus("current")
_CoQOSCountersEntry_Object = MibTableRow
coQOSCountersEntry = _CoQOSCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 13, 1, 1, 1, 1)
)
coQOSCountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "COLUBRIS-QOS-MIB", "coQOSQueueId"),
)
if mibBuilder.loadTexts:
    coQOSCountersEntry.setStatus("current")
_CoQOSQueueId_Type = ColubrisPriorityQueue
_CoQOSQueueId_Object = MibTableColumn
coQOSQueueId = _CoQOSQueueId_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 13, 1, 1, 1, 1, 1),
    _CoQOSQueueId_Type()
)
coQOSQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coQOSQueueId.setStatus("current")
_CoQOSTransmittedFrameCount_Type = Counter32
_CoQOSTransmittedFrameCount_Object = MibTableColumn
coQOSTransmittedFrameCount = _CoQOSTransmittedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 13, 1, 1, 1, 1, 2),
    _CoQOSTransmittedFrameCount_Type()
)
coQOSTransmittedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coQOSTransmittedFrameCount.setStatus("current")
_CoQOSMulticastTransmittedFrameCount_Type = Counter32
_CoQOSMulticastTransmittedFrameCount_Object = MibTableColumn
coQOSMulticastTransmittedFrameCount = _CoQOSMulticastTransmittedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 13, 1, 1, 1, 1, 3),
    _CoQOSMulticastTransmittedFrameCount_Type()
)
coQOSMulticastTransmittedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coQOSMulticastTransmittedFrameCount.setStatus("current")
_CoQOSFailedCount_Type = Counter32
_CoQOSFailedCount_Object = MibTableColumn
coQOSFailedCount = _CoQOSFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 13, 1, 1, 1, 1, 4),
    _CoQOSFailedCount_Type()
)
coQOSFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coQOSFailedCount.setStatus("current")
_CoQOSRetryCount_Type = Counter32
_CoQOSRetryCount_Object = MibTableColumn
coQOSRetryCount = _CoQOSRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 13, 1, 1, 1, 1, 5),
    _CoQOSRetryCount_Type()
)
coQOSRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coQOSRetryCount.setStatus("current")
_CoQOSMultipleRetryCount_Type = Counter32
_CoQOSMultipleRetryCount_Object = MibTableColumn
coQOSMultipleRetryCount = _CoQOSMultipleRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 13, 1, 1, 1, 1, 6),
    _CoQOSMultipleRetryCount_Type()
)
coQOSMultipleRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coQOSMultipleRetryCount.setStatus("current")
_CoQOSFrameDuplicateCount_Type = Counter32
_CoQOSFrameDuplicateCount_Object = MibTableColumn
coQOSFrameDuplicateCount = _CoQOSFrameDuplicateCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 13, 1, 1, 1, 1, 7),
    _CoQOSFrameDuplicateCount_Type()
)
coQOSFrameDuplicateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coQOSFrameDuplicateCount.setStatus("current")
_CoQOSReceivedFrameCount_Type = Counter32
_CoQOSReceivedFrameCount_Object = MibTableColumn
coQOSReceivedFrameCount = _CoQOSReceivedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 13, 1, 1, 1, 1, 8),
    _CoQOSReceivedFrameCount_Type()
)
coQOSReceivedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coQOSReceivedFrameCount.setStatus("current")
_CoQOSMulticastReceivedFrameCount_Type = Counter32
_CoQOSMulticastReceivedFrameCount_Object = MibTableColumn
coQOSMulticastReceivedFrameCount = _CoQOSMulticastReceivedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 13, 1, 1, 1, 1, 9),
    _CoQOSMulticastReceivedFrameCount_Type()
)
coQOSMulticastReceivedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coQOSMulticastReceivedFrameCount.setStatus("current")
_CoQOSConformance_ObjectIdentity = ObjectIdentity
coQOSConformance = _CoQOSConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 13, 1, 2)
)
_CoQOSGroups_ObjectIdentity = ObjectIdentity
coQOSGroups = _CoQOSGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 13, 1, 2, 1)
)
_CoQOSCompliances_ObjectIdentity = ObjectIdentity
coQOSCompliances = _CoQOSCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 13, 1, 2, 2)
)

# Managed Objects groups

coQOSCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 13, 1, 2, 1, 1)
)
coQOSCountersGroup.setObjects(
      *(("COLUBRIS-QOS-MIB", "coQOSTransmittedFrameCount"),
        ("COLUBRIS-QOS-MIB", "coQOSMulticastTransmittedFrameCount"),
        ("COLUBRIS-QOS-MIB", "coQOSFailedCount"),
        ("COLUBRIS-QOS-MIB", "coQOSRetryCount"),
        ("COLUBRIS-QOS-MIB", "coQOSMultipleRetryCount"),
        ("COLUBRIS-QOS-MIB", "coQOSFrameDuplicateCount"),
        ("COLUBRIS-QOS-MIB", "coQOSReceivedFrameCount"),
        ("COLUBRIS-QOS-MIB", "coQOSMulticastReceivedFrameCount"))
)
if mibBuilder.loadTexts:
    coQOSCountersGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

coQOSCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8744, 5, 13, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    coQOSCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-QOS-MIB",
    **{"colubrisQOS": colubrisQOS,
       "colubrisQOSMIBObjects": colubrisQOSMIBObjects,
       "coQOSStatistics": coQOSStatistics,
       "coQOSCountersTable": coQOSCountersTable,
       "coQOSCountersEntry": coQOSCountersEntry,
       "coQOSQueueId": coQOSQueueId,
       "coQOSTransmittedFrameCount": coQOSTransmittedFrameCount,
       "coQOSMulticastTransmittedFrameCount": coQOSMulticastTransmittedFrameCount,
       "coQOSFailedCount": coQOSFailedCount,
       "coQOSRetryCount": coQOSRetryCount,
       "coQOSMultipleRetryCount": coQOSMultipleRetryCount,
       "coQOSFrameDuplicateCount": coQOSFrameDuplicateCount,
       "coQOSReceivedFrameCount": coQOSReceivedFrameCount,
       "coQOSMulticastReceivedFrameCount": coQOSMulticastReceivedFrameCount,
       "coQOSConformance": coQOSConformance,
       "coQOSGroups": coQOSGroups,
       "coQOSCountersGroup": coQOSCountersGroup,
       "coQOSCompliances": coQOSCompliances,
       "coQOSCompliance": coQOSCompliance}
)
