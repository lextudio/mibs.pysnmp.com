# SNMP MIB module (CISCO-DOT11-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DOT11-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:55 2024
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

(CDot11IfVlanIdOrZero,) = mibBuilder.importSymbols(
    "CISCO-DOT11-IF-MIB",
    "CDot11IfVlanIdOrZero")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoDot11QosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 416)
)
ciscoDot11QosMIB.setRevisions(
        ("2006-05-09 00:00",
         "2003-11-24 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Cdot11QosTrafficClass(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("background", 0),
          ("bestEffort", 1),
          ("video", 2),
          ("voice", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoDot11QosMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoDot11QosMIBNotifs = _CiscoDot11QosMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 0)
)
_CiscoDot11QosMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDot11QosMIBObjects = _CiscoDot11QosMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1)
)
_CiscoDot11QosConfig_ObjectIdentity = ObjectIdentity
ciscoDot11QosConfig = _CiscoDot11QosConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1)
)
_Cdot11QosConfigTable_Object = MibTable
cdot11QosConfigTable = _Cdot11QosConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cdot11QosConfigTable.setStatus("current")
_Cdot11QosConfigEntry_Object = MibTableRow
cdot11QosConfigEntry = _Cdot11QosConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 1, 1)
)
cdot11QosConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOT11-QOS-MIB", "cdot11TrafficQueue"),
)
if mibBuilder.loadTexts:
    cdot11QosConfigEntry.setStatus("current")
_Cdot11TrafficQueue_Type = Unsigned32
_Cdot11TrafficQueue_Object = MibTableColumn
cdot11TrafficQueue = _Cdot11TrafficQueue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 1, 1, 1),
    _Cdot11TrafficQueue_Type()
)
cdot11TrafficQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdot11TrafficQueue.setStatus("current")
_Cdot11TrafficClass_Type = Cdot11QosTrafficClass
_Cdot11TrafficClass_Object = MibTableColumn
cdot11TrafficClass = _Cdot11TrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 1, 1, 2),
    _Cdot11TrafficClass_Type()
)
cdot11TrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot11TrafficClass.setStatus("current")


class _Cdot11QosCWmin_Type(Unsigned32):
    """Custom type cdot11QosCWmin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Cdot11QosCWmin_Type.__name__ = "Unsigned32"
_Cdot11QosCWmin_Object = MibTableColumn
cdot11QosCWmin = _Cdot11QosCWmin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 1, 1, 3),
    _Cdot11QosCWmin_Type()
)
cdot11QosCWmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot11QosCWmin.setStatus("current")


class _Cdot11QosCWmax_Type(Unsigned32):
    """Custom type cdot11QosCWmax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Cdot11QosCWmax_Type.__name__ = "Unsigned32"
_Cdot11QosCWmax_Object = MibTableColumn
cdot11QosCWmax = _Cdot11QosCWmax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 1, 1, 4),
    _Cdot11QosCWmax_Type()
)
cdot11QosCWmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot11QosCWmax.setStatus("current")


class _Cdot11QosBackoffOffset_Type(Unsigned32):
    """Custom type cdot11QosBackoffOffset based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_Cdot11QosBackoffOffset_Type.__name__ = "Unsigned32"
_Cdot11QosBackoffOffset_Object = MibTableColumn
cdot11QosBackoffOffset = _Cdot11QosBackoffOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 1, 1, 5),
    _Cdot11QosBackoffOffset_Type()
)
cdot11QosBackoffOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot11QosBackoffOffset.setStatus("current")


class _Cdot11QosMaxRetry_Type(Unsigned32):
    """Custom type cdot11QosMaxRetry based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdot11QosMaxRetry_Type.__name__ = "Unsigned32"
_Cdot11QosMaxRetry_Object = MibTableColumn
cdot11QosMaxRetry = _Cdot11QosMaxRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 1, 1, 6),
    _Cdot11QosMaxRetry_Type()
)
cdot11QosMaxRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot11QosMaxRetry.setStatus("current")
_Cdot11QosSupportTable_Object = MibTable
cdot11QosSupportTable = _Cdot11QosSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cdot11QosSupportTable.setStatus("current")
_Cdot11QosSupportEntry_Object = MibTableRow
cdot11QosSupportEntry = _Cdot11QosSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 2, 1)
)
cdot11QosSupportEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdot11QosSupportEntry.setStatus("current")
_Cdot11QosOptionImplemented_Type = TruthValue
_Cdot11QosOptionImplemented_Object = MibTableColumn
cdot11QosOptionImplemented = _Cdot11QosOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 2, 1, 1),
    _Cdot11QosOptionImplemented_Type()
)
cdot11QosOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot11QosOptionImplemented.setStatus("current")
_Cdot11QosOptionEnabled_Type = TruthValue
_Cdot11QosOptionEnabled_Object = MibTableColumn
cdot11QosOptionEnabled = _Cdot11QosOptionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 2, 1, 2),
    _Cdot11QosOptionEnabled_Type()
)
cdot11QosOptionEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot11QosOptionEnabled.setStatus("current")


class _Cdot11QosQueuesAvailable_Type(Unsigned32):
    """Custom type cdot11QosQueuesAvailable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 64),
    )


_Cdot11QosQueuesAvailable_Type.__name__ = "Unsigned32"
_Cdot11QosQueuesAvailable_Object = MibTableColumn
cdot11QosQueuesAvailable = _Cdot11QosQueuesAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 2, 1, 3),
    _Cdot11QosQueuesAvailable_Type()
)
cdot11QosQueuesAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot11QosQueuesAvailable.setStatus("current")
_Cdot11QosIfVlanTable_Object = MibTable
cdot11QosIfVlanTable = _Cdot11QosIfVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cdot11QosIfVlanTable.setStatus("current")
_Cdot11QosIfVlanEntry_Object = MibTableRow
cdot11QosIfVlanEntry = _Cdot11QosIfVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 3, 1)
)
cdot11QosIfVlanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOT11-QOS-MIB", "cdot11QosIfVlanId"),
)
if mibBuilder.loadTexts:
    cdot11QosIfVlanEntry.setStatus("current")


class _Cdot11QosIfVlanId_Type(CDot11IfVlanIdOrZero):
    """Custom type cdot11QosIfVlanId based on CDot11IfVlanIdOrZero"""
    subtypeSpec = CDot11IfVlanIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Cdot11QosIfVlanId_Type.__name__ = "CDot11IfVlanIdOrZero"
_Cdot11QosIfVlanId_Object = MibTableColumn
cdot11QosIfVlanId = _Cdot11QosIfVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 3, 1, 1),
    _Cdot11QosIfVlanId_Type()
)
cdot11QosIfVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdot11QosIfVlanId.setStatus("current")
_Cdot11QosIfVlanTrafficClass_Type = Cdot11QosTrafficClass
_Cdot11QosIfVlanTrafficClass_Object = MibTableColumn
cdot11QosIfVlanTrafficClass = _Cdot11QosIfVlanTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 1, 3, 1, 2),
    _Cdot11QosIfVlanTrafficClass_Type()
)
cdot11QosIfVlanTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot11QosIfVlanTrafficClass.setStatus("current")
_CiscoDot11QosQueue_ObjectIdentity = ObjectIdentity
ciscoDot11QosQueue = _CiscoDot11QosQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 2)
)
_Cdot11QosQueueTable_Object = MibTable
cdot11QosQueueTable = _Cdot11QosQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cdot11QosQueueTable.setStatus("current")
_Cdot11QosQueueEntry_Object = MibTableRow
cdot11QosQueueEntry = _Cdot11QosQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 2, 1, 1)
)
cdot11QosQueueEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOT11-QOS-MIB", "cdot11TrafficQueue"),
)
if mibBuilder.loadTexts:
    cdot11QosQueueEntry.setStatus("current")


class _Cdot11QosQueueQuota_Type(Unsigned32):
    """Custom type cdot11QosQueueQuota based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdot11QosQueueQuota_Type.__name__ = "Unsigned32"
_Cdot11QosQueueQuota_Object = MibTableColumn
cdot11QosQueueQuota = _Cdot11QosQueueQuota_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 2, 1, 1, 1),
    _Cdot11QosQueueQuota_Type()
)
cdot11QosQueueQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot11QosQueueQuota.setStatus("current")
_Cdot11QosQueueSize_Type = Gauge32
_Cdot11QosQueueSize_Object = MibTableColumn
cdot11QosQueueSize = _Cdot11QosQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 2, 1, 1, 2),
    _Cdot11QosQueueSize_Type()
)
cdot11QosQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot11QosQueueSize.setStatus("current")
_Cdot11QosQueuePeakSize_Type = Counter32
_Cdot11QosQueuePeakSize_Object = MibTableColumn
cdot11QosQueuePeakSize = _Cdot11QosQueuePeakSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 2, 1, 1, 3),
    _Cdot11QosQueuePeakSize_Type()
)
cdot11QosQueuePeakSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot11QosQueuePeakSize.setStatus("current")
_CiscoDot11QosStatistics_ObjectIdentity = ObjectIdentity
ciscoDot11QosStatistics = _CiscoDot11QosStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 3)
)
_Cdot11QosStatisticsTable_Object = MibTable
cdot11QosStatisticsTable = _Cdot11QosStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cdot11QosStatisticsTable.setStatus("current")
_Cdot11QosStatisticsEntry_Object = MibTableRow
cdot11QosStatisticsEntry = _Cdot11QosStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 3, 1, 1)
)
cdot11QosStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOT11-QOS-MIB", "cdot11TrafficQueue"),
)
if mibBuilder.loadTexts:
    cdot11QosStatisticsEntry.setStatus("current")
_Cdot11QosDiscardedFrames_Type = Counter32
_Cdot11QosDiscardedFrames_Object = MibTableColumn
cdot11QosDiscardedFrames = _Cdot11QosDiscardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 3, 1, 1, 1),
    _Cdot11QosDiscardedFrames_Type()
)
cdot11QosDiscardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot11QosDiscardedFrames.setStatus("current")
_Cdot11QosFails_Type = Counter32
_Cdot11QosFails_Object = MibTableColumn
cdot11QosFails = _Cdot11QosFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 3, 1, 1, 2),
    _Cdot11QosFails_Type()
)
cdot11QosFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot11QosFails.setStatus("current")
_Cdot11QosRetries_Type = Counter32
_Cdot11QosRetries_Object = MibTableColumn
cdot11QosRetries = _Cdot11QosRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 3, 1, 1, 3),
    _Cdot11QosRetries_Type()
)
cdot11QosRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot11QosRetries.setStatus("current")
_Cdot11QosMutipleRetries_Type = Counter32
_Cdot11QosMutipleRetries_Object = MibTableColumn
cdot11QosMutipleRetries = _Cdot11QosMutipleRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 3, 1, 1, 4),
    _Cdot11QosMutipleRetries_Type()
)
cdot11QosMutipleRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot11QosMutipleRetries.setStatus("current")
_Cdot11QosTransmittedFrames_Type = Counter32
_Cdot11QosTransmittedFrames_Object = MibTableColumn
cdot11QosTransmittedFrames = _Cdot11QosTransmittedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 3, 1, 1, 5),
    _Cdot11QosTransmittedFrames_Type()
)
cdot11QosTransmittedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot11QosTransmittedFrames.setStatus("current")
_Cdot11QosIfStatisticsTable_Object = MibTable
cdot11QosIfStatisticsTable = _Cdot11QosIfStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cdot11QosIfStatisticsTable.setStatus("current")
_Cdot11QosIfStatisticsEntry_Object = MibTableRow
cdot11QosIfStatisticsEntry = _Cdot11QosIfStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 3, 2, 1)
)
cdot11QosIfStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdot11QosIfStatisticsEntry.setStatus("current")
_Cdot11QosIfDiscardedFragments_Type = Counter32
_Cdot11QosIfDiscardedFragments_Object = MibTableColumn
cdot11QosIfDiscardedFragments = _Cdot11QosIfDiscardedFragments_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 3, 2, 1, 1),
    _Cdot11QosIfDiscardedFragments_Type()
)
cdot11QosIfDiscardedFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot11QosIfDiscardedFragments.setStatus("current")
_CiscoDot11QosNotifControl_ObjectIdentity = ObjectIdentity
ciscoDot11QosNotifControl = _CiscoDot11QosNotifControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 4)
)


class _Cdot11QosNotifEnabled_Type(TruthValue):
    """Custom type cdot11QosNotifEnabled based on TruthValue"""


_Cdot11QosNotifEnabled_Object = MibScalar
cdot11QosNotifEnabled = _Cdot11QosNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 1, 4, 1),
    _Cdot11QosNotifEnabled_Type()
)
cdot11QosNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot11QosNotifEnabled.setStatus("current")
_CiscoDot11QosMIBConformance_ObjectIdentity = ObjectIdentity
ciscoDot11QosMIBConformance = _CiscoDot11QosMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 2)
)
_CiscoDot11QosMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDot11QosMIBCompliances = _CiscoDot11QosMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 2, 1)
)
_CiscoDot11QosMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDot11QosMIBGroups = _CiscoDot11QosMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 2, 2)
)

# Managed Objects groups

ciscoDot11QosConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 2, 2, 1)
)
ciscoDot11QosConfigGroup.setObjects(
      *(("CISCO-DOT11-QOS-MIB", "cdot11TrafficClass"),
        ("CISCO-DOT11-QOS-MIB", "cdot11QosCWmin"),
        ("CISCO-DOT11-QOS-MIB", "cdot11QosCWmax"),
        ("CISCO-DOT11-QOS-MIB", "cdot11QosBackoffOffset"),
        ("CISCO-DOT11-QOS-MIB", "cdot11QosMaxRetry"),
        ("CISCO-DOT11-QOS-MIB", "cdot11QosOptionImplemented"),
        ("CISCO-DOT11-QOS-MIB", "cdot11QosOptionEnabled"),
        ("CISCO-DOT11-QOS-MIB", "cdot11QosQueuesAvailable"),
        ("CISCO-DOT11-QOS-MIB", "cdot11QosQueueQuota"),
        ("CISCO-DOT11-QOS-MIB", "cdot11QosQueueSize"),
        ("CISCO-DOT11-QOS-MIB", "cdot11QosQueuePeakSize"),
        ("CISCO-DOT11-QOS-MIB", "cdot11QosIfVlanTrafficClass"))
)
if mibBuilder.loadTexts:
    ciscoDot11QosConfigGroup.setStatus("current")

ciscoDot11QosStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 2, 2, 2)
)
ciscoDot11QosStatsGroup.setObjects(
      *(("CISCO-DOT11-QOS-MIB", "cdot11QosIfDiscardedFragments"),
        ("CISCO-DOT11-QOS-MIB", "cdot11QosDiscardedFrames"),
        ("CISCO-DOT11-QOS-MIB", "cdot11QosFails"),
        ("CISCO-DOT11-QOS-MIB", "cdot11QosRetries"),
        ("CISCO-DOT11-QOS-MIB", "cdot11QosMutipleRetries"),
        ("CISCO-DOT11-QOS-MIB", "cdot11QosTransmittedFrames"))
)
if mibBuilder.loadTexts:
    ciscoDot11QosStatsGroup.setStatus("current")

ciscoDot11QosNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 2, 2, 3)
)
ciscoDot11QosNotifControlGroup.setObjects(
    ("CISCO-DOT11-QOS-MIB", "cdot11QosNotifEnabled")
)
if mibBuilder.loadTexts:
    ciscoDot11QosNotifControlGroup.setStatus("current")


# Notification objects

cdot11QosChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 0, 1)
)
cdot11QosChangeNotif.setObjects(
    ("CISCO-DOT11-QOS-MIB", "cdot11TrafficClass")
)
if mibBuilder.loadTexts:
    cdot11QosChangeNotif.setStatus(
        "current"
    )


# Notifications groups

ciscoDot11QosNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 2, 2, 4)
)
ciscoDot11QosNotificationGroup.setObjects(
    ("CISCO-DOT11-QOS-MIB", "cdot11QosChangeNotif")
)
if mibBuilder.loadTexts:
    ciscoDot11QosNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoDot11QosMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 416, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDot11QosMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DOT11-QOS-MIB",
    **{"Cdot11QosTrafficClass": Cdot11QosTrafficClass,
       "ciscoDot11QosMIB": ciscoDot11QosMIB,
       "ciscoDot11QosMIBNotifs": ciscoDot11QosMIBNotifs,
       "cdot11QosChangeNotif": cdot11QosChangeNotif,
       "ciscoDot11QosMIBObjects": ciscoDot11QosMIBObjects,
       "ciscoDot11QosConfig": ciscoDot11QosConfig,
       "cdot11QosConfigTable": cdot11QosConfigTable,
       "cdot11QosConfigEntry": cdot11QosConfigEntry,
       "cdot11TrafficQueue": cdot11TrafficQueue,
       "cdot11TrafficClass": cdot11TrafficClass,
       "cdot11QosCWmin": cdot11QosCWmin,
       "cdot11QosCWmax": cdot11QosCWmax,
       "cdot11QosBackoffOffset": cdot11QosBackoffOffset,
       "cdot11QosMaxRetry": cdot11QosMaxRetry,
       "cdot11QosSupportTable": cdot11QosSupportTable,
       "cdot11QosSupportEntry": cdot11QosSupportEntry,
       "cdot11QosOptionImplemented": cdot11QosOptionImplemented,
       "cdot11QosOptionEnabled": cdot11QosOptionEnabled,
       "cdot11QosQueuesAvailable": cdot11QosQueuesAvailable,
       "cdot11QosIfVlanTable": cdot11QosIfVlanTable,
       "cdot11QosIfVlanEntry": cdot11QosIfVlanEntry,
       "cdot11QosIfVlanId": cdot11QosIfVlanId,
       "cdot11QosIfVlanTrafficClass": cdot11QosIfVlanTrafficClass,
       "ciscoDot11QosQueue": ciscoDot11QosQueue,
       "cdot11QosQueueTable": cdot11QosQueueTable,
       "cdot11QosQueueEntry": cdot11QosQueueEntry,
       "cdot11QosQueueQuota": cdot11QosQueueQuota,
       "cdot11QosQueueSize": cdot11QosQueueSize,
       "cdot11QosQueuePeakSize": cdot11QosQueuePeakSize,
       "ciscoDot11QosStatistics": ciscoDot11QosStatistics,
       "cdot11QosStatisticsTable": cdot11QosStatisticsTable,
       "cdot11QosStatisticsEntry": cdot11QosStatisticsEntry,
       "cdot11QosDiscardedFrames": cdot11QosDiscardedFrames,
       "cdot11QosFails": cdot11QosFails,
       "cdot11QosRetries": cdot11QosRetries,
       "cdot11QosMutipleRetries": cdot11QosMutipleRetries,
       "cdot11QosTransmittedFrames": cdot11QosTransmittedFrames,
       "cdot11QosIfStatisticsTable": cdot11QosIfStatisticsTable,
       "cdot11QosIfStatisticsEntry": cdot11QosIfStatisticsEntry,
       "cdot11QosIfDiscardedFragments": cdot11QosIfDiscardedFragments,
       "ciscoDot11QosNotifControl": ciscoDot11QosNotifControl,
       "cdot11QosNotifEnabled": cdot11QosNotifEnabled,
       "ciscoDot11QosMIBConformance": ciscoDot11QosMIBConformance,
       "ciscoDot11QosMIBCompliances": ciscoDot11QosMIBCompliances,
       "ciscoDot11QosMIBCompliance": ciscoDot11QosMIBCompliance,
       "ciscoDot11QosMIBGroups": ciscoDot11QosMIBGroups,
       "ciscoDot11QosConfigGroup": ciscoDot11QosConfigGroup,
       "ciscoDot11QosStatsGroup": ciscoDot11QosStatsGroup,
       "ciscoDot11QosNotifControlGroup": ciscoDot11QosNotifControlGroup,
       "ciscoDot11QosNotificationGroup": ciscoDot11QosNotificationGroup}
)
