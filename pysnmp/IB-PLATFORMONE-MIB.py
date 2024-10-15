# SNMP MIB module (IB-PLATFORMONE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IB-PLATFORMONE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:17 2024
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

(IbIpAddr,
 IbString,
 ibPlatformOne) = mibBuilder.importSymbols(
    "IB-SMI-MIB",
    "IbIpAddr",
    "IbString",
    "ibPlatformOne")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ibPlatformModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1)
)
ibPlatformModule.setRevisions(
        ("2010-11-15 00:00",
         "2010-10-19 00:00",
         "2010-07-28 00:00",
         "2009-06-05 00:00",
         "2008-09-29 00:00",
         "2005-01-10 00:00",
         "2004-05-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IbServiceStates(Integer32, TextualConvention):
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
        *(("failed", 3),
          ("inactive", 4),
          ("unknown", 5),
          ("warning", 2),
          ("working", 1))
    )



class IbServiceNames(Integer32, TextualConvention):
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 36),
          ("bloxtools", 9),
          ("bloxtools-move", 8),
          ("cpu-usage", 34),
          ("cpu1-temp", 30),
          ("cpu2-temp", 31),
          ("db-object", 19),
          ("dhcp", 1),
          ("disk-usage", 11),
          ("dns", 2),
          ("enet-ha", 14),
          ("enet-lan", 12),
          ("enet-lan2", 13),
          ("enet-mgmt", 15),
          ("fan1", 25),
          ("fan2", 26),
          ("fan3", 27),
          ("ftp", 7),
          ("http-file-dist", 6),
          ("lcd", 16),
          ("memory", 17),
          ("node-status", 10),
          ("ntp", 3),
          ("ntp-sync", 29),
          ("ospf", 35),
          ("power-supply", 28),
          ("radius", 4),
          ("raid-battery", 33),
          ("raid-disk1", 21),
          ("raid-disk2", 22),
          ("raid-disk3", 23),
          ("raid-disk4", 24),
          ("raid-summary", 20),
          ("replication", 18),
          ("sys-temp", 32),
          ("tftp", 5))
    )



# MIB Managed Objects in the order of their OIDs

_IbCPUTemperature_Type = IbString
_IbCPUTemperature_Object = MibScalar
ibCPUTemperature = _IbCPUTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 1),
    _IbCPUTemperature_Type()
)
ibCPUTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibCPUTemperature.setStatus("current")
_IbClusterReplicationStatusTable_Object = MibTable
ibClusterReplicationStatusTable = _IbClusterReplicationStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ibClusterReplicationStatusTable.setStatus("current")
_IbClusterReplicationStatusEntry_Object = MibTableRow
ibClusterReplicationStatusEntry = _IbClusterReplicationStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 2, 1)
)
ibClusterReplicationStatusEntry.setIndexNames(
    (0, "IB-PLATFORMONE-MIB", "ibNodeIPAddress"),
)
if mibBuilder.loadTexts:
    ibClusterReplicationStatusEntry.setStatus("current")
_IbNodeIPAddress_Type = IbIpAddr
_IbNodeIPAddress_Object = MibTableColumn
ibNodeIPAddress = _IbNodeIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 2, 1, 1),
    _IbNodeIPAddress_Type()
)
ibNodeIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNodeIPAddress.setStatus("current")
_IbNodeReplicationStatus_Type = IbString
_IbNodeReplicationStatus_Object = MibTableColumn
ibNodeReplicationStatus = _IbNodeReplicationStatus_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 2, 1, 2),
    _IbNodeReplicationStatus_Type()
)
ibNodeReplicationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNodeReplicationStatus.setStatus("current")
_IbNodeQueueFromMaster_Type = Integer32
_IbNodeQueueFromMaster_Object = MibTableColumn
ibNodeQueueFromMaster = _IbNodeQueueFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 2, 1, 3),
    _IbNodeQueueFromMaster_Type()
)
ibNodeQueueFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNodeQueueFromMaster.setStatus("current")
_IbNodeLastRepTimeFromMaster_Type = IbString
_IbNodeLastRepTimeFromMaster_Object = MibTableColumn
ibNodeLastRepTimeFromMaster = _IbNodeLastRepTimeFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 2, 1, 4),
    _IbNodeLastRepTimeFromMaster_Type()
)
ibNodeLastRepTimeFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNodeLastRepTimeFromMaster.setStatus("current")
_IbNodeQueueToMaster_Type = Integer32
_IbNodeQueueToMaster_Object = MibTableColumn
ibNodeQueueToMaster = _IbNodeQueueToMaster_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 2, 1, 5),
    _IbNodeQueueToMaster_Type()
)
ibNodeQueueToMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNodeQueueToMaster.setStatus("current")
_IbNodeLastRepTimeToMaster_Type = IbString
_IbNodeLastRepTimeToMaster_Object = MibTableColumn
ibNodeLastRepTimeToMaster = _IbNodeLastRepTimeToMaster_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 2, 1, 6),
    _IbNodeLastRepTimeToMaster_Type()
)
ibNodeLastRepTimeToMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNodeLastRepTimeToMaster.setStatus("current")
_IbNetworkMonitor_ObjectIdentity = ObjectIdentity
ibNetworkMonitor = _IbNetworkMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3)
)
_IbNetworkMonitorDNS_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNS = _IbNetworkMonitorDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1)
)


class _IbNetworkMonitorDNSActive_Type(Integer32):
    """Custom type ibNetworkMonitorDNSActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("nonactive", 0))
    )


_IbNetworkMonitorDNSActive_Type.__name__ = "Integer32"
_IbNetworkMonitorDNSActive_Object = MibScalar
ibNetworkMonitorDNSActive = _IbNetworkMonitorDNSActive_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 1),
    _IbNetworkMonitorDNSActive_Type()
)
ibNetworkMonitorDNSActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSActive.setStatus("current")
_IbNetworkMonitorDNSNonAA_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSNonAA = _IbNetworkMonitorDNSNonAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2)
)
_IbNetworkMonitorDNSNonAAT1_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSNonAAT1 = _IbNetworkMonitorDNSNonAAT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 1)
)
_IbNetworkMonitorDNSNonAAT1AvgLatency_Type = Integer32
_IbNetworkMonitorDNSNonAAT1AvgLatency_Object = MibScalar
ibNetworkMonitorDNSNonAAT1AvgLatency = _IbNetworkMonitorDNSNonAAT1AvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 1, 1),
    _IbNetworkMonitorDNSNonAAT1AvgLatency_Type()
)
ibNetworkMonitorDNSNonAAT1AvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSNonAAT1AvgLatency.setStatus("current")
_IbNetworkMonitorDNSNonAAT1Count_Type = Integer32
_IbNetworkMonitorDNSNonAAT1Count_Object = MibScalar
ibNetworkMonitorDNSNonAAT1Count = _IbNetworkMonitorDNSNonAAT1Count_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 1, 2),
    _IbNetworkMonitorDNSNonAAT1Count_Type()
)
ibNetworkMonitorDNSNonAAT1Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSNonAAT1Count.setStatus("current")
_IbNetworkMonitorDNSNonAAT5_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSNonAAT5 = _IbNetworkMonitorDNSNonAAT5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 2)
)
_IbNetworkMonitorDNSNonAAT5AvgLatency_Type = Integer32
_IbNetworkMonitorDNSNonAAT5AvgLatency_Object = MibScalar
ibNetworkMonitorDNSNonAAT5AvgLatency = _IbNetworkMonitorDNSNonAAT5AvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 2, 1),
    _IbNetworkMonitorDNSNonAAT5AvgLatency_Type()
)
ibNetworkMonitorDNSNonAAT5AvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSNonAAT5AvgLatency.setStatus("current")
_IbNetworkMonitorDNSNonAAT5Count_Type = Integer32
_IbNetworkMonitorDNSNonAAT5Count_Object = MibScalar
ibNetworkMonitorDNSNonAAT5Count = _IbNetworkMonitorDNSNonAAT5Count_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 2, 2),
    _IbNetworkMonitorDNSNonAAT5Count_Type()
)
ibNetworkMonitorDNSNonAAT5Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSNonAAT5Count.setStatus("current")
_IbNetworkMonitorDNSNonAAT15_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSNonAAT15 = _IbNetworkMonitorDNSNonAAT15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 3)
)
_IbNetworkMonitorDNSNonAAT15AvgLatency_Type = Integer32
_IbNetworkMonitorDNSNonAAT15AvgLatency_Object = MibScalar
ibNetworkMonitorDNSNonAAT15AvgLatency = _IbNetworkMonitorDNSNonAAT15AvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 3, 1),
    _IbNetworkMonitorDNSNonAAT15AvgLatency_Type()
)
ibNetworkMonitorDNSNonAAT15AvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSNonAAT15AvgLatency.setStatus("current")
_IbNetworkMonitorDNSNonAAT15Count_Type = Integer32
_IbNetworkMonitorDNSNonAAT15Count_Object = MibScalar
ibNetworkMonitorDNSNonAAT15Count = _IbNetworkMonitorDNSNonAAT15Count_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 3, 2),
    _IbNetworkMonitorDNSNonAAT15Count_Type()
)
ibNetworkMonitorDNSNonAAT15Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSNonAAT15Count.setStatus("current")
_IbNetworkMonitorDNSNonAAT60_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSNonAAT60 = _IbNetworkMonitorDNSNonAAT60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 4)
)
_IbNetworkMonitorDNSNonAAT60AvgLatency_Type = Integer32
_IbNetworkMonitorDNSNonAAT60AvgLatency_Object = MibScalar
ibNetworkMonitorDNSNonAAT60AvgLatency = _IbNetworkMonitorDNSNonAAT60AvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 4, 1),
    _IbNetworkMonitorDNSNonAAT60AvgLatency_Type()
)
ibNetworkMonitorDNSNonAAT60AvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSNonAAT60AvgLatency.setStatus("current")
_IbNetworkMonitorDNSNonAAT60Count_Type = Integer32
_IbNetworkMonitorDNSNonAAT60Count_Object = MibScalar
ibNetworkMonitorDNSNonAAT60Count = _IbNetworkMonitorDNSNonAAT60Count_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 4, 2),
    _IbNetworkMonitorDNSNonAAT60Count_Type()
)
ibNetworkMonitorDNSNonAAT60Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSNonAAT60Count.setStatus("current")
_IbNetworkMonitorDNSNonAAT1440_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSNonAAT1440 = _IbNetworkMonitorDNSNonAAT1440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 5)
)
_IbNetworkMonitorDNSNonAAT1440AvgLatency_Type = Integer32
_IbNetworkMonitorDNSNonAAT1440AvgLatency_Object = MibScalar
ibNetworkMonitorDNSNonAAT1440AvgLatency = _IbNetworkMonitorDNSNonAAT1440AvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 5, 1),
    _IbNetworkMonitorDNSNonAAT1440AvgLatency_Type()
)
ibNetworkMonitorDNSNonAAT1440AvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSNonAAT1440AvgLatency.setStatus("current")
_IbNetworkMonitorDNSNonAAT1440Count_Type = Integer32
_IbNetworkMonitorDNSNonAAT1440Count_Object = MibScalar
ibNetworkMonitorDNSNonAAT1440Count = _IbNetworkMonitorDNSNonAAT1440Count_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 5, 2),
    _IbNetworkMonitorDNSNonAAT1440Count_Type()
)
ibNetworkMonitorDNSNonAAT1440Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSNonAAT1440Count.setStatus("current")
_IbNetworkMonitorDNSAA_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSAA = _IbNetworkMonitorDNSAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3)
)
_IbNetworkMonitorDNSAAT1_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSAAT1 = _IbNetworkMonitorDNSAAT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 1)
)
_IbNetworkMonitorDNSAAT1AvgLatency_Type = Integer32
_IbNetworkMonitorDNSAAT1AvgLatency_Object = MibScalar
ibNetworkMonitorDNSAAT1AvgLatency = _IbNetworkMonitorDNSAAT1AvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 1, 1),
    _IbNetworkMonitorDNSAAT1AvgLatency_Type()
)
ibNetworkMonitorDNSAAT1AvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSAAT1AvgLatency.setStatus("current")
_IbNetworkMonitorDNSAAT1Count_Type = Integer32
_IbNetworkMonitorDNSAAT1Count_Object = MibScalar
ibNetworkMonitorDNSAAT1Count = _IbNetworkMonitorDNSAAT1Count_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 1, 2),
    _IbNetworkMonitorDNSAAT1Count_Type()
)
ibNetworkMonitorDNSAAT1Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSAAT1Count.setStatus("current")
_IbNetworkMonitorDNSAAT5_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSAAT5 = _IbNetworkMonitorDNSAAT5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 2)
)
_IbNetworkMonitorDNSAAT5AvgLatency_Type = Integer32
_IbNetworkMonitorDNSAAT5AvgLatency_Object = MibScalar
ibNetworkMonitorDNSAAT5AvgLatency = _IbNetworkMonitorDNSAAT5AvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 2, 1),
    _IbNetworkMonitorDNSAAT5AvgLatency_Type()
)
ibNetworkMonitorDNSAAT5AvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSAAT5AvgLatency.setStatus("current")
_IbNetworkMonitorDNSAAT5Count_Type = Integer32
_IbNetworkMonitorDNSAAT5Count_Object = MibScalar
ibNetworkMonitorDNSAAT5Count = _IbNetworkMonitorDNSAAT5Count_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 2, 2),
    _IbNetworkMonitorDNSAAT5Count_Type()
)
ibNetworkMonitorDNSAAT5Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSAAT5Count.setStatus("current")
_IbNetworkMonitorDNSAAT15_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSAAT15 = _IbNetworkMonitorDNSAAT15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 3)
)
_IbNetworkMonitorDNSAAT15AvgLatency_Type = Integer32
_IbNetworkMonitorDNSAAT15AvgLatency_Object = MibScalar
ibNetworkMonitorDNSAAT15AvgLatency = _IbNetworkMonitorDNSAAT15AvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 3, 1),
    _IbNetworkMonitorDNSAAT15AvgLatency_Type()
)
ibNetworkMonitorDNSAAT15AvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSAAT15AvgLatency.setStatus("current")
_IbNetworkMonitorDNSAAT15Count_Type = Integer32
_IbNetworkMonitorDNSAAT15Count_Object = MibScalar
ibNetworkMonitorDNSAAT15Count = _IbNetworkMonitorDNSAAT15Count_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 3, 2),
    _IbNetworkMonitorDNSAAT15Count_Type()
)
ibNetworkMonitorDNSAAT15Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSAAT15Count.setStatus("current")
_IbNetworkMonitorDNSAAT60_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSAAT60 = _IbNetworkMonitorDNSAAT60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 4)
)
_IbNetworkMonitorDNSAAT60AvgLatency_Type = Integer32
_IbNetworkMonitorDNSAAT60AvgLatency_Object = MibScalar
ibNetworkMonitorDNSAAT60AvgLatency = _IbNetworkMonitorDNSAAT60AvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 4, 1),
    _IbNetworkMonitorDNSAAT60AvgLatency_Type()
)
ibNetworkMonitorDNSAAT60AvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSAAT60AvgLatency.setStatus("current")
_IbNetworkMonitorDNSAAT60Count_Type = Integer32
_IbNetworkMonitorDNSAAT60Count_Object = MibScalar
ibNetworkMonitorDNSAAT60Count = _IbNetworkMonitorDNSAAT60Count_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 4, 2),
    _IbNetworkMonitorDNSAAT60Count_Type()
)
ibNetworkMonitorDNSAAT60Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSAAT60Count.setStatus("current")
_IbNetworkMonitorDNSAAT1440_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSAAT1440 = _IbNetworkMonitorDNSAAT1440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 5)
)
_IbNetworkMonitorDNSAAT1440AvgLatency_Type = Integer32
_IbNetworkMonitorDNSAAT1440AvgLatency_Object = MibScalar
ibNetworkMonitorDNSAAT1440AvgLatency = _IbNetworkMonitorDNSAAT1440AvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 5, 1),
    _IbNetworkMonitorDNSAAT1440AvgLatency_Type()
)
ibNetworkMonitorDNSAAT1440AvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSAAT1440AvgLatency.setStatus("current")
_IbNetworkMonitorDNSAAT1440Count_Type = Integer32
_IbNetworkMonitorDNSAAT1440Count_Object = MibScalar
ibNetworkMonitorDNSAAT1440Count = _IbNetworkMonitorDNSAAT1440Count_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 5, 2),
    _IbNetworkMonitorDNSAAT1440Count_Type()
)
ibNetworkMonitorDNSAAT1440Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSAAT1440Count.setStatus("current")
_IbNetworkMonitorDNSSecurity_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSSecurity = _IbNetworkMonitorDNSSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4)
)
_IbNetworkMonitorDNSSecurityInvalidPort_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSSecurityInvalidPort = _IbNetworkMonitorDNSSecurityInvalidPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 1)
)
_IbNetworkMonitorDNSSecurityInvalidPort1_Type = Integer32
_IbNetworkMonitorDNSSecurityInvalidPort1_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidPort1 = _IbNetworkMonitorDNSSecurityInvalidPort1_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 1, 1),
    _IbNetworkMonitorDNSSecurityInvalidPort1_Type()
)
ibNetworkMonitorDNSSecurityInvalidPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidPort1.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidPort5_Type = Integer32
_IbNetworkMonitorDNSSecurityInvalidPort5_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidPort5 = _IbNetworkMonitorDNSSecurityInvalidPort5_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 1, 2),
    _IbNetworkMonitorDNSSecurityInvalidPort5_Type()
)
ibNetworkMonitorDNSSecurityInvalidPort5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidPort5.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidPort15_Type = Integer32
_IbNetworkMonitorDNSSecurityInvalidPort15_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidPort15 = _IbNetworkMonitorDNSSecurityInvalidPort15_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 1, 3),
    _IbNetworkMonitorDNSSecurityInvalidPort15_Type()
)
ibNetworkMonitorDNSSecurityInvalidPort15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidPort15.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidPort60_Type = Integer32
_IbNetworkMonitorDNSSecurityInvalidPort60_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidPort60 = _IbNetworkMonitorDNSSecurityInvalidPort60_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 1, 4),
    _IbNetworkMonitorDNSSecurityInvalidPort60_Type()
)
ibNetworkMonitorDNSSecurityInvalidPort60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidPort60.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidPort1440_Type = Integer32
_IbNetworkMonitorDNSSecurityInvalidPort1440_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidPort1440 = _IbNetworkMonitorDNSSecurityInvalidPort1440_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 1, 5),
    _IbNetworkMonitorDNSSecurityInvalidPort1440_Type()
)
ibNetworkMonitorDNSSecurityInvalidPort1440.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidPort1440.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidPortCount_Type = Counter32
_IbNetworkMonitorDNSSecurityInvalidPortCount_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidPortCount = _IbNetworkMonitorDNSSecurityInvalidPortCount_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 1, 6),
    _IbNetworkMonitorDNSSecurityInvalidPortCount_Type()
)
ibNetworkMonitorDNSSecurityInvalidPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidPortCount.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidTxid_ObjectIdentity = ObjectIdentity
ibNetworkMonitorDNSSecurityInvalidTxid = _IbNetworkMonitorDNSSecurityInvalidTxid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 2)
)
_IbNetworkMonitorDNSSecurityInvalidTxid1_Type = Integer32
_IbNetworkMonitorDNSSecurityInvalidTxid1_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidTxid1 = _IbNetworkMonitorDNSSecurityInvalidTxid1_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 2, 1),
    _IbNetworkMonitorDNSSecurityInvalidTxid1_Type()
)
ibNetworkMonitorDNSSecurityInvalidTxid1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidTxid1.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidTxid5_Type = Integer32
_IbNetworkMonitorDNSSecurityInvalidTxid5_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidTxid5 = _IbNetworkMonitorDNSSecurityInvalidTxid5_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 2, 2),
    _IbNetworkMonitorDNSSecurityInvalidTxid5_Type()
)
ibNetworkMonitorDNSSecurityInvalidTxid5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidTxid5.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidTxid15_Type = Integer32
_IbNetworkMonitorDNSSecurityInvalidTxid15_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidTxid15 = _IbNetworkMonitorDNSSecurityInvalidTxid15_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 2, 3),
    _IbNetworkMonitorDNSSecurityInvalidTxid15_Type()
)
ibNetworkMonitorDNSSecurityInvalidTxid15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidTxid15.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidTxid60_Type = Integer32
_IbNetworkMonitorDNSSecurityInvalidTxid60_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidTxid60 = _IbNetworkMonitorDNSSecurityInvalidTxid60_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 2, 4),
    _IbNetworkMonitorDNSSecurityInvalidTxid60_Type()
)
ibNetworkMonitorDNSSecurityInvalidTxid60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidTxid60.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidTxid1440_Type = Integer32
_IbNetworkMonitorDNSSecurityInvalidTxid1440_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidTxid1440 = _IbNetworkMonitorDNSSecurityInvalidTxid1440_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 2, 5),
    _IbNetworkMonitorDNSSecurityInvalidTxid1440_Type()
)
ibNetworkMonitorDNSSecurityInvalidTxid1440.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidTxid1440.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidTxidCount_Type = Counter32
_IbNetworkMonitorDNSSecurityInvalidTxidCount_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidTxidCount = _IbNetworkMonitorDNSSecurityInvalidTxidCount_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 2, 6),
    _IbNetworkMonitorDNSSecurityInvalidTxidCount_Type()
)
ibNetworkMonitorDNSSecurityInvalidTxidCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidTxidCount.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidPortOnly_Type = Counter32
_IbNetworkMonitorDNSSecurityInvalidPortOnly_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidPortOnly = _IbNetworkMonitorDNSSecurityInvalidPortOnly_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 3),
    _IbNetworkMonitorDNSSecurityInvalidPortOnly_Type()
)
ibNetworkMonitorDNSSecurityInvalidPortOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidPortOnly.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidTxidOnly_Type = Counter32
_IbNetworkMonitorDNSSecurityInvalidTxidOnly_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidTxidOnly = _IbNetworkMonitorDNSSecurityInvalidTxidOnly_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 4),
    _IbNetworkMonitorDNSSecurityInvalidTxidOnly_Type()
)
ibNetworkMonitorDNSSecurityInvalidTxidOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidTxidOnly.setStatus("current")
_IbNetworkMonitorDNSSecurityInvalidTxidAndPort_Type = Counter32
_IbNetworkMonitorDNSSecurityInvalidTxidAndPort_Object = MibScalar
ibNetworkMonitorDNSSecurityInvalidTxidAndPort = _IbNetworkMonitorDNSSecurityInvalidTxidAndPort_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 5),
    _IbNetworkMonitorDNSSecurityInvalidTxidAndPort_Type()
)
ibNetworkMonitorDNSSecurityInvalidTxidAndPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNetworkMonitorDNSSecurityInvalidTxidAndPort.setStatus("current")
_IbHardwareType_Type = IbString
_IbHardwareType_Object = MibScalar
ibHardwareType = _IbHardwareType_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 4),
    _IbHardwareType_Type()
)
ibHardwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibHardwareType.setStatus("current")
_IbHardwareId_Type = IbString
_IbHardwareId_Object = MibScalar
ibHardwareId = _IbHardwareId_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 5),
    _IbHardwareId_Type()
)
ibHardwareId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibHardwareId.setStatus("current")
_IbSerialNumber_Type = IbString
_IbSerialNumber_Object = MibScalar
ibSerialNumber = _IbSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 6),
    _IbSerialNumber_Type()
)
ibSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSerialNumber.setStatus("current")
_IbNiosVersion_Type = IbString
_IbNiosVersion_Object = MibScalar
ibNiosVersion = _IbNiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 7),
    _IbNiosVersion_Type()
)
ibNiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNiosVersion.setStatus("current")
_IbSystemMonitor_ObjectIdentity = ObjectIdentity
ibSystemMonitor = _IbSystemMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8)
)
_IbSystemMonitorCpu_ObjectIdentity = ObjectIdentity
ibSystemMonitorCpu = _IbSystemMonitorCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 1)
)
_IbSystemMonitorCpuUsage_Type = Integer32
_IbSystemMonitorCpuUsage_Object = MibScalar
ibSystemMonitorCpuUsage = _IbSystemMonitorCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 1, 1),
    _IbSystemMonitorCpuUsage_Type()
)
ibSystemMonitorCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSystemMonitorCpuUsage.setStatus("current")
_IbSystemMonitorMem_ObjectIdentity = ObjectIdentity
ibSystemMonitorMem = _IbSystemMonitorMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 2)
)
_IbSystemMonitorMemUsage_Type = Integer32
_IbSystemMonitorMemUsage_Object = MibScalar
ibSystemMonitorMemUsage = _IbSystemMonitorMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 2, 1),
    _IbSystemMonitorMemUsage_Type()
)
ibSystemMonitorMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibSystemMonitorMemUsage.setStatus("current")
_IbMemberServiceStatusTable_Object = MibTable
ibMemberServiceStatusTable = _IbMemberServiceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    ibMemberServiceStatusTable.setStatus("current")
_IbMemberServiceStatusEntry_Object = MibTableRow
ibMemberServiceStatusEntry = _IbMemberServiceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 9, 1)
)
ibMemberServiceStatusEntry.setIndexNames(
    (0, "IB-PLATFORMONE-MIB", "ibServiceName"),
)
if mibBuilder.loadTexts:
    ibMemberServiceStatusEntry.setStatus("current")
_IbServiceName_Type = IbServiceNames
_IbServiceName_Object = MibTableColumn
ibServiceName = _IbServiceName_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 9, 1, 1),
    _IbServiceName_Type()
)
ibServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibServiceName.setStatus("current")
_IbServiceStatus_Type = IbServiceStates
_IbServiceStatus_Object = MibTableColumn
ibServiceStatus = _IbServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 9, 1, 2),
    _IbServiceStatus_Type()
)
ibServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibServiceStatus.setStatus("current")
_IbServiceDesc_Type = IbString
_IbServiceDesc_Object = MibTableColumn
ibServiceDesc = _IbServiceDesc_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 9, 1, 3),
    _IbServiceDesc_Type()
)
ibServiceDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibServiceDesc.setStatus("current")
_IbMemberNode1ServiceStatusTable_Object = MibTable
ibMemberNode1ServiceStatusTable = _IbMemberNode1ServiceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    ibMemberNode1ServiceStatusTable.setStatus("current")
_IbMemberNode1ServiceStatusEntry_Object = MibTableRow
ibMemberNode1ServiceStatusEntry = _IbMemberNode1ServiceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 10, 1)
)
ibMemberNode1ServiceStatusEntry.setIndexNames(
    (0, "IB-PLATFORMONE-MIB", "ibNode1ServiceName"),
)
if mibBuilder.loadTexts:
    ibMemberNode1ServiceStatusEntry.setStatus("current")
_IbNode1ServiceName_Type = IbServiceNames
_IbNode1ServiceName_Object = MibTableColumn
ibNode1ServiceName = _IbNode1ServiceName_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 10, 1, 1),
    _IbNode1ServiceName_Type()
)
ibNode1ServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNode1ServiceName.setStatus("current")
_IbNode1ServiceStatus_Type = IbServiceStates
_IbNode1ServiceStatus_Object = MibTableColumn
ibNode1ServiceStatus = _IbNode1ServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 10, 1, 2),
    _IbNode1ServiceStatus_Type()
)
ibNode1ServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNode1ServiceStatus.setStatus("current")
_IbNode1ServiceDesc_Type = IbString
_IbNode1ServiceDesc_Object = MibTableColumn
ibNode1ServiceDesc = _IbNode1ServiceDesc_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 10, 1, 3),
    _IbNode1ServiceDesc_Type()
)
ibNode1ServiceDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNode1ServiceDesc.setStatus("current")
_IbMemberNode2ServiceStatusTable_Object = MibTable
ibMemberNode2ServiceStatusTable = _IbMemberNode2ServiceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 11)
)
if mibBuilder.loadTexts:
    ibMemberNode2ServiceStatusTable.setStatus("current")
_IbMemberNode2ServiceStatusEntry_Object = MibTableRow
ibMemberNode2ServiceStatusEntry = _IbMemberNode2ServiceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 11, 1)
)
ibMemberNode2ServiceStatusEntry.setIndexNames(
    (0, "IB-PLATFORMONE-MIB", "ibNode2ServiceName"),
)
if mibBuilder.loadTexts:
    ibMemberNode2ServiceStatusEntry.setStatus("current")
_IbNode2ServiceName_Type = IbServiceNames
_IbNode2ServiceName_Object = MibTableColumn
ibNode2ServiceName = _IbNode2ServiceName_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 11, 1, 1),
    _IbNode2ServiceName_Type()
)
ibNode2ServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNode2ServiceName.setStatus("current")
_IbNode2ServiceStatus_Type = IbServiceStates
_IbNode2ServiceStatus_Object = MibTableColumn
ibNode2ServiceStatus = _IbNode2ServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 11, 1, 2),
    _IbNode2ServiceStatus_Type()
)
ibNode2ServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNode2ServiceStatus.setStatus("current")
_IbNode2ServiceDesc_Type = IbString
_IbNode2ServiceDesc_Object = MibTableColumn
ibNode2ServiceDesc = _IbNode2ServiceDesc_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 11, 1, 3),
    _IbNode2ServiceDesc_Type()
)
ibNode2ServiceDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibNode2ServiceDesc.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IB-PLATFORMONE-MIB",
    **{"IbServiceStates": IbServiceStates,
       "IbServiceNames": IbServiceNames,
       "ibPlatformModule": ibPlatformModule,
       "ibCPUTemperature": ibCPUTemperature,
       "ibClusterReplicationStatusTable": ibClusterReplicationStatusTable,
       "ibClusterReplicationStatusEntry": ibClusterReplicationStatusEntry,
       "ibNodeIPAddress": ibNodeIPAddress,
       "ibNodeReplicationStatus": ibNodeReplicationStatus,
       "ibNodeQueueFromMaster": ibNodeQueueFromMaster,
       "ibNodeLastRepTimeFromMaster": ibNodeLastRepTimeFromMaster,
       "ibNodeQueueToMaster": ibNodeQueueToMaster,
       "ibNodeLastRepTimeToMaster": ibNodeLastRepTimeToMaster,
       "ibNetworkMonitor": ibNetworkMonitor,
       "ibNetworkMonitorDNS": ibNetworkMonitorDNS,
       "ibNetworkMonitorDNSActive": ibNetworkMonitorDNSActive,
       "ibNetworkMonitorDNSNonAA": ibNetworkMonitorDNSNonAA,
       "ibNetworkMonitorDNSNonAAT1": ibNetworkMonitorDNSNonAAT1,
       "ibNetworkMonitorDNSNonAAT1AvgLatency": ibNetworkMonitorDNSNonAAT1AvgLatency,
       "ibNetworkMonitorDNSNonAAT1Count": ibNetworkMonitorDNSNonAAT1Count,
       "ibNetworkMonitorDNSNonAAT5": ibNetworkMonitorDNSNonAAT5,
       "ibNetworkMonitorDNSNonAAT5AvgLatency": ibNetworkMonitorDNSNonAAT5AvgLatency,
       "ibNetworkMonitorDNSNonAAT5Count": ibNetworkMonitorDNSNonAAT5Count,
       "ibNetworkMonitorDNSNonAAT15": ibNetworkMonitorDNSNonAAT15,
       "ibNetworkMonitorDNSNonAAT15AvgLatency": ibNetworkMonitorDNSNonAAT15AvgLatency,
       "ibNetworkMonitorDNSNonAAT15Count": ibNetworkMonitorDNSNonAAT15Count,
       "ibNetworkMonitorDNSNonAAT60": ibNetworkMonitorDNSNonAAT60,
       "ibNetworkMonitorDNSNonAAT60AvgLatency": ibNetworkMonitorDNSNonAAT60AvgLatency,
       "ibNetworkMonitorDNSNonAAT60Count": ibNetworkMonitorDNSNonAAT60Count,
       "ibNetworkMonitorDNSNonAAT1440": ibNetworkMonitorDNSNonAAT1440,
       "ibNetworkMonitorDNSNonAAT1440AvgLatency": ibNetworkMonitorDNSNonAAT1440AvgLatency,
       "ibNetworkMonitorDNSNonAAT1440Count": ibNetworkMonitorDNSNonAAT1440Count,
       "ibNetworkMonitorDNSAA": ibNetworkMonitorDNSAA,
       "ibNetworkMonitorDNSAAT1": ibNetworkMonitorDNSAAT1,
       "ibNetworkMonitorDNSAAT1AvgLatency": ibNetworkMonitorDNSAAT1AvgLatency,
       "ibNetworkMonitorDNSAAT1Count": ibNetworkMonitorDNSAAT1Count,
       "ibNetworkMonitorDNSAAT5": ibNetworkMonitorDNSAAT5,
       "ibNetworkMonitorDNSAAT5AvgLatency": ibNetworkMonitorDNSAAT5AvgLatency,
       "ibNetworkMonitorDNSAAT5Count": ibNetworkMonitorDNSAAT5Count,
       "ibNetworkMonitorDNSAAT15": ibNetworkMonitorDNSAAT15,
       "ibNetworkMonitorDNSAAT15AvgLatency": ibNetworkMonitorDNSAAT15AvgLatency,
       "ibNetworkMonitorDNSAAT15Count": ibNetworkMonitorDNSAAT15Count,
       "ibNetworkMonitorDNSAAT60": ibNetworkMonitorDNSAAT60,
       "ibNetworkMonitorDNSAAT60AvgLatency": ibNetworkMonitorDNSAAT60AvgLatency,
       "ibNetworkMonitorDNSAAT60Count": ibNetworkMonitorDNSAAT60Count,
       "ibNetworkMonitorDNSAAT1440": ibNetworkMonitorDNSAAT1440,
       "ibNetworkMonitorDNSAAT1440AvgLatency": ibNetworkMonitorDNSAAT1440AvgLatency,
       "ibNetworkMonitorDNSAAT1440Count": ibNetworkMonitorDNSAAT1440Count,
       "ibNetworkMonitorDNSSecurity": ibNetworkMonitorDNSSecurity,
       "ibNetworkMonitorDNSSecurityInvalidPort": ibNetworkMonitorDNSSecurityInvalidPort,
       "ibNetworkMonitorDNSSecurityInvalidPort1": ibNetworkMonitorDNSSecurityInvalidPort1,
       "ibNetworkMonitorDNSSecurityInvalidPort5": ibNetworkMonitorDNSSecurityInvalidPort5,
       "ibNetworkMonitorDNSSecurityInvalidPort15": ibNetworkMonitorDNSSecurityInvalidPort15,
       "ibNetworkMonitorDNSSecurityInvalidPort60": ibNetworkMonitorDNSSecurityInvalidPort60,
       "ibNetworkMonitorDNSSecurityInvalidPort1440": ibNetworkMonitorDNSSecurityInvalidPort1440,
       "ibNetworkMonitorDNSSecurityInvalidPortCount": ibNetworkMonitorDNSSecurityInvalidPortCount,
       "ibNetworkMonitorDNSSecurityInvalidTxid": ibNetworkMonitorDNSSecurityInvalidTxid,
       "ibNetworkMonitorDNSSecurityInvalidTxid1": ibNetworkMonitorDNSSecurityInvalidTxid1,
       "ibNetworkMonitorDNSSecurityInvalidTxid5": ibNetworkMonitorDNSSecurityInvalidTxid5,
       "ibNetworkMonitorDNSSecurityInvalidTxid15": ibNetworkMonitorDNSSecurityInvalidTxid15,
       "ibNetworkMonitorDNSSecurityInvalidTxid60": ibNetworkMonitorDNSSecurityInvalidTxid60,
       "ibNetworkMonitorDNSSecurityInvalidTxid1440": ibNetworkMonitorDNSSecurityInvalidTxid1440,
       "ibNetworkMonitorDNSSecurityInvalidTxidCount": ibNetworkMonitorDNSSecurityInvalidTxidCount,
       "ibNetworkMonitorDNSSecurityInvalidPortOnly": ibNetworkMonitorDNSSecurityInvalidPortOnly,
       "ibNetworkMonitorDNSSecurityInvalidTxidOnly": ibNetworkMonitorDNSSecurityInvalidTxidOnly,
       "ibNetworkMonitorDNSSecurityInvalidTxidAndPort": ibNetworkMonitorDNSSecurityInvalidTxidAndPort,
       "ibHardwareType": ibHardwareType,
       "ibHardwareId": ibHardwareId,
       "ibSerialNumber": ibSerialNumber,
       "ibNiosVersion": ibNiosVersion,
       "ibSystemMonitor": ibSystemMonitor,
       "ibSystemMonitorCpu": ibSystemMonitorCpu,
       "ibSystemMonitorCpuUsage": ibSystemMonitorCpuUsage,
       "ibSystemMonitorMem": ibSystemMonitorMem,
       "ibSystemMonitorMemUsage": ibSystemMonitorMemUsage,
       "ibMemberServiceStatusTable": ibMemberServiceStatusTable,
       "ibMemberServiceStatusEntry": ibMemberServiceStatusEntry,
       "ibServiceName": ibServiceName,
       "ibServiceStatus": ibServiceStatus,
       "ibServiceDesc": ibServiceDesc,
       "ibMemberNode1ServiceStatusTable": ibMemberNode1ServiceStatusTable,
       "ibMemberNode1ServiceStatusEntry": ibMemberNode1ServiceStatusEntry,
       "ibNode1ServiceName": ibNode1ServiceName,
       "ibNode1ServiceStatus": ibNode1ServiceStatus,
       "ibNode1ServiceDesc": ibNode1ServiceDesc,
       "ibMemberNode2ServiceStatusTable": ibMemberNode2ServiceStatusTable,
       "ibMemberNode2ServiceStatusEntry": ibMemberNode2ServiceStatusEntry,
       "ibNode2ServiceName": ibNode2ServiceName,
       "ibNode2ServiceStatus": ibNode2ServiceStatus,
       "ibNode2ServiceDesc": ibNode2ServiceDesc}
)
