# SNMP MIB module (CISCO-IETF-DOT11-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-DOT11-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:31 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoIetfDot11QosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 89)
)
ciscoIetfDot11QosMIB.setRevisions(
        ("2002-03-28 00:00",
         "2002-01-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Cid11QosTrafficCategory(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("background", 1),
          ("bestEffort", 0),
          ("controlledLoad", 4),
          ("excellentEffort", 3),
          ("interactiveVideo", 5),
          ("interactiveVoice", 6),
          ("networkControl", 7),
          ("spare", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoIetfDot11QosMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIetfDot11QosMIBObjects = _CiscoIetfDot11QosMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1)
)
_CiscoIetfDot11QosConfig_ObjectIdentity = ObjectIdentity
ciscoIetfDot11QosConfig = _CiscoIetfDot11QosConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 1)
)
_Cid11QosConfigTable_Object = MibTable
cid11QosConfigTable = _Cid11QosConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cid11QosConfigTable.setStatus("current")
_Cid11QosConfigEntry_Object = MibTableRow
cid11QosConfigEntry = _Cid11QosConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 1, 1, 1)
)
cid11QosConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IETF-DOT11-QOS-MIB", "cid11TrafficCategory"),
)
if mibBuilder.loadTexts:
    cid11QosConfigEntry.setStatus("current")
_Cid11TrafficCategory_Type = Cid11QosTrafficCategory
_Cid11TrafficCategory_Object = MibTableColumn
cid11TrafficCategory = _Cid11TrafficCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 1, 1, 1, 1),
    _Cid11TrafficCategory_Type()
)
cid11TrafficCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cid11TrafficCategory.setStatus("current")


class _Cid11CWmin_Type(Unsigned32):
    """Custom type cid11CWmin based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_Cid11CWmin_Type.__name__ = "Unsigned32"
_Cid11CWmin_Object = MibTableColumn
cid11CWmin = _Cid11CWmin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 1, 1, 1, 2),
    _Cid11CWmin_Type()
)
cid11CWmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cid11CWmin.setStatus("current")


class _Cid11CWmax_Type(Unsigned32):
    """Custom type cid11CWmax based on Unsigned32"""
    defaultValue = 1023

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_Cid11CWmax_Type.__name__ = "Unsigned32"
_Cid11CWmax_Object = MibTableColumn
cid11CWmax = _Cid11CWmax_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 1, 1, 1, 3),
    _Cid11CWmax_Type()
)
cid11CWmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cid11CWmax.setStatus("current")


class _Cid11CWPFactor_Type(Unsigned32):
    """Custom type cid11CWPFactor based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cid11CWPFactor_Type.__name__ = "Unsigned32"
_Cid11CWPFactor_Object = MibTableColumn
cid11CWPFactor = _Cid11CWPFactor_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 1, 1, 1, 4),
    _Cid11CWPFactor_Type()
)
cid11CWPFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cid11CWPFactor.setStatus("current")


class _Cid11AIFS_Type(Unsigned32):
    """Custom type cid11AIFS based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_Cid11AIFS_Type.__name__ = "Unsigned32"
_Cid11AIFS_Object = MibTableColumn
cid11AIFS = _Cid11AIFS_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 1, 1, 1, 5),
    _Cid11AIFS_Type()
)
cid11AIFS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cid11AIFS.setStatus("current")


class _Cid11TrafficPriority_Type(Unsigned32):
    """Custom type cid11TrafficPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cid11TrafficPriority_Type.__name__ = "Unsigned32"
_Cid11TrafficPriority_Object = MibTableColumn
cid11TrafficPriority = _Cid11TrafficPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 1, 1, 1, 6),
    _Cid11TrafficPriority_Type()
)
cid11TrafficPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cid11TrafficPriority.setStatus("current")


class _Cid11MSDULifetime_Type(Unsigned32):
    """Custom type cid11MSDULifetime based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cid11MSDULifetime_Type.__name__ = "Unsigned32"
_Cid11MSDULifetime_Object = MibTableColumn
cid11MSDULifetime = _Cid11MSDULifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 1, 1, 1, 7),
    _Cid11MSDULifetime_Type()
)
cid11MSDULifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cid11MSDULifetime.setStatus("current")
_Cid11QosSupportTable_Object = MibTable
cid11QosSupportTable = _Cid11QosSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cid11QosSupportTable.setStatus("current")
_Cid11QosSupportEntry_Object = MibTableRow
cid11QosSupportEntry = _Cid11QosSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 1, 2, 1)
)
cid11QosSupportEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cid11QosSupportEntry.setStatus("current")
_Cid11QosOptionImplemented_Type = TruthValue
_Cid11QosOptionImplemented_Object = MibTableColumn
cid11QosOptionImplemented = _Cid11QosOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 1, 2, 1, 1),
    _Cid11QosOptionImplemented_Type()
)
cid11QosOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cid11QosOptionImplemented.setStatus("current")


class _Cid11QueuesAvailable_Type(Unsigned32):
    """Custom type cid11QueuesAvailable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 8),
    )


_Cid11QueuesAvailable_Type.__name__ = "Unsigned32"
_Cid11QueuesAvailable_Object = MibTableColumn
cid11QueuesAvailable = _Cid11QueuesAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 1, 2, 1, 2),
    _Cid11QueuesAvailable_Type()
)
cid11QueuesAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cid11QueuesAvailable.setStatus("current")
_CiscoIetfDot11QosQueue_ObjectIdentity = ObjectIdentity
ciscoIetfDot11QosQueue = _CiscoIetfDot11QosQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 2)
)
_Cid11QueueTable_Object = MibTable
cid11QueueTable = _Cid11QueueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cid11QueueTable.setStatus("current")
_Cid11QueueEntry_Object = MibTableRow
cid11QueueEntry = _Cid11QueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 2, 1, 1)
)
cid11QueueEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IETF-DOT11-QOS-MIB", "cid11TrafficCategory"),
)
if mibBuilder.loadTexts:
    cid11QueueEntry.setStatus("current")


class _Cid11QueueSize_Type(Unsigned32):
    """Custom type cid11QueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_Cid11QueueSize_Type.__name__ = "Unsigned32"
_Cid11QueueSize_Object = MibTableColumn
cid11QueueSize = _Cid11QueueSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 2, 1, 1, 1),
    _Cid11QueueSize_Type()
)
cid11QueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cid11QueueSize.setStatus("current")
_Cid11QueuePeakSize_Type = Counter32
_Cid11QueuePeakSize_Object = MibTableColumn
cid11QueuePeakSize = _Cid11QueuePeakSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 2, 1, 1, 2),
    _Cid11QueuePeakSize_Type()
)
cid11QueuePeakSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cid11QueuePeakSize.setStatus("current")
_CiscoIetfDot11QosStatistics_ObjectIdentity = ObjectIdentity
ciscoIetfDot11QosStatistics = _CiscoIetfDot11QosStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 3)
)
_Cid11QosStatisticsTable_Object = MibTable
cid11QosStatisticsTable = _Cid11QosStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cid11QosStatisticsTable.setStatus("current")
_Cid11QosStatisticsEntry_Object = MibTableRow
cid11QosStatisticsEntry = _Cid11QosStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 3, 1, 1)
)
cid11QosStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IETF-DOT11-QOS-MIB", "cid11TrafficCategory"),
)
if mibBuilder.loadTexts:
    cid11QosStatisticsEntry.setStatus("current")
_Cid11QosReceivedMPDUs_Type = Counter32
_Cid11QosReceivedMPDUs_Object = MibTableColumn
cid11QosReceivedMPDUs = _Cid11QosReceivedMPDUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 3, 1, 1, 1),
    _Cid11QosReceivedMPDUs_Type()
)
cid11QosReceivedMPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cid11QosReceivedMPDUs.setStatus("current")
_Cid11QosReceivedRetries_Type = Counter32
_Cid11QosReceivedRetries_Object = MibTableColumn
cid11QosReceivedRetries = _Cid11QosReceivedRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 3, 1, 1, 2),
    _Cid11QosReceivedRetries_Type()
)
cid11QosReceivedRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cid11QosReceivedRetries.setStatus("current")
_Cid11QosDiscardedFrames_Type = Counter32
_Cid11QosDiscardedFrames_Object = MibTableColumn
cid11QosDiscardedFrames = _Cid11QosDiscardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 3, 1, 1, 3),
    _Cid11QosDiscardedFrames_Type()
)
cid11QosDiscardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cid11QosDiscardedFrames.setStatus("current")
_Cid11QosTransmittedFragments_Type = Counter32
_Cid11QosTransmittedFragments_Object = MibTableColumn
cid11QosTransmittedFragments = _Cid11QosTransmittedFragments_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 3, 1, 1, 4),
    _Cid11QosTransmittedFragments_Type()
)
cid11QosTransmittedFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cid11QosTransmittedFragments.setStatus("current")
_Cid11QosFails_Type = Counter32
_Cid11QosFails_Object = MibTableColumn
cid11QosFails = _Cid11QosFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 3, 1, 1, 5),
    _Cid11QosFails_Type()
)
cid11QosFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cid11QosFails.setStatus("current")
_Cid11QosRetries_Type = Counter32
_Cid11QosRetries_Object = MibTableColumn
cid11QosRetries = _Cid11QosRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 3, 1, 1, 6),
    _Cid11QosRetries_Type()
)
cid11QosRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cid11QosRetries.setStatus("current")
_Cid11QosMutipleRetries_Type = Counter32
_Cid11QosMutipleRetries_Object = MibTableColumn
cid11QosMutipleRetries = _Cid11QosMutipleRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 3, 1, 1, 7),
    _Cid11QosMutipleRetries_Type()
)
cid11QosMutipleRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cid11QosMutipleRetries.setStatus("current")
_Cid11QosFrameDuplicates_Type = Counter32
_Cid11QosFrameDuplicates_Object = MibTableColumn
cid11QosFrameDuplicates = _Cid11QosFrameDuplicates_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 3, 1, 1, 8),
    _Cid11QosFrameDuplicates_Type()
)
cid11QosFrameDuplicates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cid11QosFrameDuplicates.setStatus("current")
_Cid11QosReceivedFragments_Type = Counter32
_Cid11QosReceivedFragments_Object = MibTableColumn
cid11QosReceivedFragments = _Cid11QosReceivedFragments_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 3, 1, 1, 9),
    _Cid11QosReceivedFragments_Type()
)
cid11QosReceivedFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cid11QosReceivedFragments.setStatus("current")
_Cid11QosTransmittedFrames_Type = Counter32
_Cid11QosTransmittedFrames_Object = MibTableColumn
cid11QosTransmittedFrames = _Cid11QosTransmittedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 3, 1, 1, 10),
    _Cid11QosTransmittedFrames_Type()
)
cid11QosTransmittedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cid11QosTransmittedFrames.setStatus("current")
_Cid11QosIfStatisticsTable_Object = MibTable
cid11QosIfStatisticsTable = _Cid11QosIfStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cid11QosIfStatisticsTable.setStatus("current")
_Cid11QosIfStatisticsEntry_Object = MibTableRow
cid11QosIfStatisticsEntry = _Cid11QosIfStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 3, 2, 1)
)
cid11QosIfStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cid11QosIfStatisticsEntry.setStatus("current")
_Cid11QosIfDiscardedFragments_Type = Counter32
_Cid11QosIfDiscardedFragments_Object = MibTableColumn
cid11QosIfDiscardedFragments = _Cid11QosIfDiscardedFragments_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 1, 3, 2, 1, 1),
    _Cid11QosIfDiscardedFragments_Type()
)
cid11QosIfDiscardedFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cid11QosIfDiscardedFragments.setStatus("current")
_CiscoIetfDot11QosMIBConformance_ObjectIdentity = ObjectIdentity
ciscoIetfDot11QosMIBConformance = _CiscoIetfDot11QosMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 2)
)
_CiscoIetfDot11QosMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIetfDot11QosMIBCompliances = _CiscoIetfDot11QosMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 2, 1)
)
_CiscoIetfDot11QosMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIetfDot11QosMIBGroups = _CiscoIetfDot11QosMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 2, 2)
)

# Managed Objects groups

ciscoIetfDot11QosConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 2, 2, 1)
)
ciscoIetfDot11QosConfigGroup.setObjects(
      *(("CISCO-IETF-DOT11-QOS-MIB", "cid11CWmin"),
        ("CISCO-IETF-DOT11-QOS-MIB", "cid11CWmax"),
        ("CISCO-IETF-DOT11-QOS-MIB", "cid11CWPFactor"),
        ("CISCO-IETF-DOT11-QOS-MIB", "cid11AIFS"),
        ("CISCO-IETF-DOT11-QOS-MIB", "cid11TrafficPriority"),
        ("CISCO-IETF-DOT11-QOS-MIB", "cid11MSDULifetime"),
        ("CISCO-IETF-DOT11-QOS-MIB", "cid11QosOptionImplemented"),
        ("CISCO-IETF-DOT11-QOS-MIB", "cid11QueuesAvailable"))
)
if mibBuilder.loadTexts:
    ciscoIetfDot11QosConfigGroup.setStatus("current")

ciscoIetfDot11QosQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 2, 2, 2)
)
ciscoIetfDot11QosQueueGroup.setObjects(
      *(("CISCO-IETF-DOT11-QOS-MIB", "cid11QueueSize"),
        ("CISCO-IETF-DOT11-QOS-MIB", "cid11QueuePeakSize"))
)
if mibBuilder.loadTexts:
    ciscoIetfDot11QosQueueGroup.setStatus("current")

ciscoIetfDot11QosStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 2, 2, 3)
)
ciscoIetfDot11QosStatsGroup.setObjects(
      *(("CISCO-IETF-DOT11-QOS-MIB", "cid11QosIfDiscardedFragments"),
        ("CISCO-IETF-DOT11-QOS-MIB", "cid11QosReceivedMPDUs"),
        ("CISCO-IETF-DOT11-QOS-MIB", "cid11QosReceivedRetries"),
        ("CISCO-IETF-DOT11-QOS-MIB", "cid11QosDiscardedFrames"),
        ("CISCO-IETF-DOT11-QOS-MIB", "cid11QosTransmittedFragments"),
        ("CISCO-IETF-DOT11-QOS-MIB", "cid11QosFails"),
        ("CISCO-IETF-DOT11-QOS-MIB", "cid11QosRetries"),
        ("CISCO-IETF-DOT11-QOS-MIB", "cid11QosMutipleRetries"),
        ("CISCO-IETF-DOT11-QOS-MIB", "cid11QosFrameDuplicates"),
        ("CISCO-IETF-DOT11-QOS-MIB", "cid11QosReceivedFragments"),
        ("CISCO-IETF-DOT11-QOS-MIB", "cid11QosTransmittedFrames"))
)
if mibBuilder.loadTexts:
    ciscoIetfDot11QosStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoIetfDot11QosMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 89, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIetfDot11QosMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-DOT11-QOS-MIB",
    **{"Cid11QosTrafficCategory": Cid11QosTrafficCategory,
       "ciscoIetfDot11QosMIB": ciscoIetfDot11QosMIB,
       "ciscoIetfDot11QosMIBObjects": ciscoIetfDot11QosMIBObjects,
       "ciscoIetfDot11QosConfig": ciscoIetfDot11QosConfig,
       "cid11QosConfigTable": cid11QosConfigTable,
       "cid11QosConfigEntry": cid11QosConfigEntry,
       "cid11TrafficCategory": cid11TrafficCategory,
       "cid11CWmin": cid11CWmin,
       "cid11CWmax": cid11CWmax,
       "cid11CWPFactor": cid11CWPFactor,
       "cid11AIFS": cid11AIFS,
       "cid11TrafficPriority": cid11TrafficPriority,
       "cid11MSDULifetime": cid11MSDULifetime,
       "cid11QosSupportTable": cid11QosSupportTable,
       "cid11QosSupportEntry": cid11QosSupportEntry,
       "cid11QosOptionImplemented": cid11QosOptionImplemented,
       "cid11QueuesAvailable": cid11QueuesAvailable,
       "ciscoIetfDot11QosQueue": ciscoIetfDot11QosQueue,
       "cid11QueueTable": cid11QueueTable,
       "cid11QueueEntry": cid11QueueEntry,
       "cid11QueueSize": cid11QueueSize,
       "cid11QueuePeakSize": cid11QueuePeakSize,
       "ciscoIetfDot11QosStatistics": ciscoIetfDot11QosStatistics,
       "cid11QosStatisticsTable": cid11QosStatisticsTable,
       "cid11QosStatisticsEntry": cid11QosStatisticsEntry,
       "cid11QosReceivedMPDUs": cid11QosReceivedMPDUs,
       "cid11QosReceivedRetries": cid11QosReceivedRetries,
       "cid11QosDiscardedFrames": cid11QosDiscardedFrames,
       "cid11QosTransmittedFragments": cid11QosTransmittedFragments,
       "cid11QosFails": cid11QosFails,
       "cid11QosRetries": cid11QosRetries,
       "cid11QosMutipleRetries": cid11QosMutipleRetries,
       "cid11QosFrameDuplicates": cid11QosFrameDuplicates,
       "cid11QosReceivedFragments": cid11QosReceivedFragments,
       "cid11QosTransmittedFrames": cid11QosTransmittedFrames,
       "cid11QosIfStatisticsTable": cid11QosIfStatisticsTable,
       "cid11QosIfStatisticsEntry": cid11QosIfStatisticsEntry,
       "cid11QosIfDiscardedFragments": cid11QosIfDiscardedFragments,
       "ciscoIetfDot11QosMIBConformance": ciscoIetfDot11QosMIBConformance,
       "ciscoIetfDot11QosMIBCompliances": ciscoIetfDot11QosMIBCompliances,
       "ciscoIetfDot11QosMIBCompliance": ciscoIetfDot11QosMIBCompliance,
       "ciscoIetfDot11QosMIBGroups": ciscoIetfDot11QosMIBGroups,
       "ciscoIetfDot11QosConfigGroup": ciscoIetfDot11QosConfigGroup,
       "ciscoIetfDot11QosQueueGroup": ciscoIetfDot11QosQueueGroup,
       "ciscoIetfDot11QosStatsGroup": ciscoIetfDot11QosStatsGroup}
)
