# SNMP MIB module (NCD-MIB-1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NCD-MIB-1
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:07 2024
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
 iso,
 private) = mibBuilder.importSymbols(
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
    "iso",
    "private")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ncd_ObjectIdentity = ObjectIdentity
ncd = _Ncd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 82)
)
_Ncd_products_ObjectIdentity = ObjectIdentity
ncd_products = _Ncd_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 82, 1)
)
_Ncd16_ObjectIdentity = ObjectIdentity
ncd16 = _Ncd16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 82, 1, 1)
)
_Ncd19_ObjectIdentity = ObjectIdentity
ncd19 = _Ncd19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 82, 1, 2)
)
_Ncd17c_ObjectIdentity = ObjectIdentity
ncd17c = _Ncd17c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 82, 1, 3)
)
_Ncd16e_ObjectIdentity = ObjectIdentity
ncd16e = _Ncd16e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 82, 1, 4)
)
_Ncd_mibs_ObjectIdentity = ObjectIdentity
ncd_mibs = _Ncd_mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 82, 2)
)
_Ncd_mibs_mib1_ObjectIdentity = ObjectIdentity
ncd_mibs_mib1 = _Ncd_mibs_mib1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 82, 2, 1)
)
_NcdSystem_ObjectIdentity = ObjectIdentity
ncdSystem = _NcdSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 1)
)
_NcdSysMemTotal_Type = Integer32
_NcdSysMemTotal_Object = MibScalar
ncdSysMemTotal = _NcdSysMemTotal_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 1, 1),
    _NcdSysMemTotal_Type()
)
ncdSysMemTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdSysMemTotal.setStatus("optional")
_NcdSysMemAvail_Type = Gauge32
_NcdSysMemAvail_Object = MibScalar
ncdSysMemAvail = _NcdSysMemAvail_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 1, 2),
    _NcdSysMemAvail_Type()
)
ncdSysMemAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdSysMemAvail.setStatus("optional")
_NcdSysMemFrags_Type = Gauge32
_NcdSysMemFrags_Object = MibScalar
ncdSysMemFrags = _NcdSysMemFrags_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 1, 3),
    _NcdSysMemFrags_Type()
)
ncdSysMemFrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdSysMemFrags.setStatus("optional")
_NcdSysIdleTime_Type = TimeTicks
_NcdSysIdleTime_Object = MibScalar
ncdSysIdleTime = _NcdSysIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 1, 4),
    _NcdSysIdleTime_Type()
)
ncdSysIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdSysIdleTime.setStatus("optional")
_NcdMbuf_ObjectIdentity = ObjectIdentity
ncdMbuf = _NcdMbuf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 2)
)
_NcdMbufTotal_Type = Integer32
_NcdMbufTotal_Object = MibScalar
ncdMbufTotal = _NcdMbufTotal_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 2, 1),
    _NcdMbufTotal_Type()
)
ncdMbufTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdMbufTotal.setStatus("optional")
_NcdMbufFree_Type = Gauge32
_NcdMbufFree_Object = MibScalar
ncdMbufFree = _NcdMbufFree_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 2, 2),
    _NcdMbufFree_Type()
)
ncdMbufFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdMbufFree.setStatus("optional")
_NcdMbufClusterTotal_Type = Integer32
_NcdMbufClusterTotal_Object = MibScalar
ncdMbufClusterTotal = _NcdMbufClusterTotal_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 2, 3),
    _NcdMbufClusterTotal_Type()
)
ncdMbufClusterTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdMbufClusterTotal.setStatus("optional")
_NcdMbufClusterFree_Type = Gauge32
_NcdMbufClusterFree_Object = MibScalar
ncdMbufClusterFree = _NcdMbufClusterFree_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 2, 4),
    _NcdMbufClusterFree_Type()
)
ncdMbufClusterFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdMbufClusterFree.setStatus("optional")
_NcdMbufReserved_Type = Gauge32
_NcdMbufReserved_Object = MibScalar
ncdMbufReserved = _NcdMbufReserved_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 2, 5),
    _NcdMbufReserved_Type()
)
ncdMbufReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdMbufReserved.setStatus("optional")
_NcdMbufDrops_Type = Counter32
_NcdMbufDrops_Object = MibScalar
ncdMbufDrops = _NcdMbufDrops_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 2, 6),
    _NcdMbufDrops_Type()
)
ncdMbufDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdMbufDrops.setStatus("optional")
_NcdMbufWaits_Type = Counter32
_NcdMbufWaits_Object = MibScalar
ncdMbufWaits = _NcdMbufWaits_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 2, 7),
    _NcdMbufWaits_Type()
)
ncdMbufWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdMbufWaits.setStatus("optional")
_NcdMbufData_Type = Gauge32
_NcdMbufData_Object = MibScalar
ncdMbufData = _NcdMbufData_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 2, 8),
    _NcdMbufData_Type()
)
ncdMbufData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdMbufData.setStatus("optional")
_NcdMbufHeader_Type = Gauge32
_NcdMbufHeader_Object = MibScalar
ncdMbufHeader = _NcdMbufHeader_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 2, 9),
    _NcdMbufHeader_Type()
)
ncdMbufHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdMbufHeader.setStatus("optional")
_NcdMbufSocket_Type = Gauge32
_NcdMbufSocket_Object = MibScalar
ncdMbufSocket = _NcdMbufSocket_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 2, 10),
    _NcdMbufSocket_Type()
)
ncdMbufSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdMbufSocket.setStatus("optional")
_NcdMbufProtoCtrlBlock_Type = Gauge32
_NcdMbufProtoCtrlBlock_Object = MibScalar
ncdMbufProtoCtrlBlock = _NcdMbufProtoCtrlBlock_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 2, 11),
    _NcdMbufProtoCtrlBlock_Type()
)
ncdMbufProtoCtrlBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdMbufProtoCtrlBlock.setStatus("optional")
_NcdMbufRouteTable_Type = Gauge32
_NcdMbufRouteTable_Object = MibScalar
ncdMbufRouteTable = _NcdMbufRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 2, 12),
    _NcdMbufRouteTable_Type()
)
ncdMbufRouteTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdMbufRouteTable.setStatus("optional")
_NcdMbufAtTable_Type = Gauge32
_NcdMbufAtTable_Object = MibScalar
ncdMbufAtTable = _NcdMbufAtTable_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 2, 13),
    _NcdMbufAtTable_Type()
)
ncdMbufAtTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdMbufAtTable.setStatus("optional")
_NcdMbufSocketName_Type = Gauge32
_NcdMbufSocketName_Object = MibScalar
ncdMbufSocketName = _NcdMbufSocketName_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 2, 14),
    _NcdMbufSocketName_Type()
)
ncdMbufSocketName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdMbufSocketName.setStatus("optional")
_NcdMbufSocketOptions_Type = Gauge32
_NcdMbufSocketOptions_Object = MibScalar
ncdMbufSocketOptions = _NcdMbufSocketOptions_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 2, 15),
    _NcdMbufSocketOptions_Type()
)
ncdMbufSocketOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdMbufSocketOptions.setStatus("optional")
_NcdMbufFrags_Type = Gauge32
_NcdMbufFrags_Object = MibScalar
ncdMbufFrags = _NcdMbufFrags_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 2, 16),
    _NcdMbufFrags_Type()
)
ncdMbufFrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdMbufFrags.setStatus("optional")
_NcdMbufInterfaceAddr_Type = Gauge32
_NcdMbufInterfaceAddr_Object = MibScalar
ncdMbufInterfaceAddr = _NcdMbufInterfaceAddr_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 2, 17),
    _NcdMbufInterfaceAddr_Type()
)
ncdMbufInterfaceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdMbufInterfaceAddr.setStatus("optional")
_NcdEther_ObjectIdentity = ObjectIdentity
ncdEther = _NcdEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 3)
)
_NcdEtherTable_Object = MibTable
ncdEtherTable = _NcdEtherTable_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ncdEtherTable.setStatus("optional")
_NcdEtherEntry_Object = MibTableRow
ncdEtherEntry = _NcdEtherEntry_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ncdEtherEntry.setStatus("optional")
_NcdEtherInCrcErrors_Type = Counter32
_NcdEtherInCrcErrors_Object = MibTableColumn
ncdEtherInCrcErrors = _NcdEtherInCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 3, 1, 1, 1),
    _NcdEtherInCrcErrors_Type()
)
ncdEtherInCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdEtherInCrcErrors.setStatus("optional")
_NcdEtherInMissed_Type = Counter32
_NcdEtherInMissed_Object = MibTableColumn
ncdEtherInMissed = _NcdEtherInMissed_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 3, 1, 1, 2),
    _NcdEtherInMissed_Type()
)
ncdEtherInMissed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdEtherInMissed.setStatus("optional")
_NcdEtherInFrameErrors_Type = Counter32
_NcdEtherInFrameErrors_Object = MibTableColumn
ncdEtherInFrameErrors = _NcdEtherInFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 3, 1, 1, 3),
    _NcdEtherInFrameErrors_Type()
)
ncdEtherInFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdEtherInFrameErrors.setStatus("optional")
_NcdEtherSingleCollisions_Type = Counter32
_NcdEtherSingleCollisions_Object = MibTableColumn
ncdEtherSingleCollisions = _NcdEtherSingleCollisions_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 3, 1, 1, 4),
    _NcdEtherSingleCollisions_Type()
)
ncdEtherSingleCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdEtherSingleCollisions.setStatus("optional")
_NcdEtherMultipleCollisions_Type = Counter32
_NcdEtherMultipleCollisions_Object = MibTableColumn
ncdEtherMultipleCollisions = _NcdEtherMultipleCollisions_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 3, 1, 1, 5),
    _NcdEtherMultipleCollisions_Type()
)
ncdEtherMultipleCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdEtherMultipleCollisions.setStatus("optional")
_NcdEtherLateCollisions_Type = Counter32
_NcdEtherLateCollisions_Object = MibTableColumn
ncdEtherLateCollisions = _NcdEtherLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 3, 1, 1, 6),
    _NcdEtherLateCollisions_Type()
)
ncdEtherLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdEtherLateCollisions.setStatus("optional")
_NcdEtherOutDeferred_Type = Counter32
_NcdEtherOutDeferred_Object = MibTableColumn
ncdEtherOutDeferred = _NcdEtherOutDeferred_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 3, 1, 1, 7),
    _NcdEtherOutDeferred_Type()
)
ncdEtherOutDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdEtherOutDeferred.setStatus("optional")
_NcdEtherOutRetryErrors_Type = Counter32
_NcdEtherOutRetryErrors_Object = MibTableColumn
ncdEtherOutRetryErrors = _NcdEtherOutRetryErrors_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 3, 1, 1, 8),
    _NcdEtherOutRetryErrors_Type()
)
ncdEtherOutRetryErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdEtherOutRetryErrors.setStatus("optional")
_NcdEtherLostCarrier_Type = Counter32
_NcdEtherLostCarrier_Object = MibTableColumn
ncdEtherLostCarrier = _NcdEtherLostCarrier_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 3, 1, 1, 9),
    _NcdEtherLostCarrier_Type()
)
ncdEtherLostCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdEtherLostCarrier.setStatus("optional")
_NcdEtherRestarts_Type = Counter32
_NcdEtherRestarts_Object = MibTableColumn
ncdEtherRestarts = _NcdEtherRestarts_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 3, 1, 1, 10),
    _NcdEtherRestarts_Type()
)
ncdEtherRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdEtherRestarts.setStatus("optional")
_NcdSerial_ObjectIdentity = ObjectIdentity
ncdSerial = _NcdSerial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 4)
)
_NcdSerialTable_Object = MibTable
ncdSerialTable = _NcdSerialTable_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ncdSerialTable.setStatus("optional")
_NcdSerialEntry_Object = MibTableRow
ncdSerialEntry = _NcdSerialEntry_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    ncdSerialEntry.setStatus("optional")
_NcdSerialInOverruns_Type = Counter32
_NcdSerialInOverruns_Object = MibTableColumn
ncdSerialInOverruns = _NcdSerialInOverruns_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 4, 1, 1, 1),
    _NcdSerialInOverruns_Type()
)
ncdSerialInOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdSerialInOverruns.setStatus("optional")
_NcdSerialInFrameErrors_Type = Counter32
_NcdSerialInFrameErrors_Object = MibTableColumn
ncdSerialInFrameErrors = _NcdSerialInFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 4, 1, 1, 2),
    _NcdSerialInFrameErrors_Type()
)
ncdSerialInFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdSerialInFrameErrors.setStatus("optional")
_NcdSerialInParityErrors_Type = Counter32
_NcdSerialInParityErrors_Object = MibTableColumn
ncdSerialInParityErrors = _NcdSerialInParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 4, 1, 1, 3),
    _NcdSerialInParityErrors_Type()
)
ncdSerialInParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdSerialInParityErrors.setStatus("optional")
_NcdSerialInBreakErrors_Type = Counter32
_NcdSerialInBreakErrors_Object = MibTableColumn
ncdSerialInBreakErrors = _NcdSerialInBreakErrors_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 4, 1, 1, 4),
    _NcdSerialInBreakErrors_Type()
)
ncdSerialInBreakErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdSerialInBreakErrors.setStatus("optional")
_NcdTcp_ObjectIdentity = ObjectIdentity
ncdTcp = _NcdTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 5)
)
_NcdTcpRetransDrops_Type = Counter32
_NcdTcpRetransDrops_Object = MibScalar
ncdTcpRetransDrops = _NcdTcpRetransDrops_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 5, 1),
    _NcdTcpRetransDrops_Type()
)
ncdTcpRetransDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdTcpRetransDrops.setStatus("optional")
_NcdTcpOutKeepAlives_Type = Counter32
_NcdTcpOutKeepAlives_Object = MibScalar
ncdTcpOutKeepAlives = _NcdTcpOutKeepAlives_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 5, 2),
    _NcdTcpOutKeepAlives_Type()
)
ncdTcpOutKeepAlives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdTcpOutKeepAlives.setStatus("optional")
_NcdTcpKeepAliveDrops_Type = Counter32
_NcdTcpKeepAliveDrops_Object = MibScalar
ncdTcpKeepAliveDrops = _NcdTcpKeepAliveDrops_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 5, 3),
    _NcdTcpKeepAliveDrops_Type()
)
ncdTcpKeepAliveDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdTcpKeepAliveDrops.setStatus("optional")
_NcdTcpInAcks_Type = Counter32
_NcdTcpInAcks_Object = MibScalar
ncdTcpInAcks = _NcdTcpInAcks_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 5, 4),
    _NcdTcpInAcks_Type()
)
ncdTcpInAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdTcpInAcks.setStatus("optional")
_NcdTcpOutBareAcks_Type = Counter32
_NcdTcpOutBareAcks_Object = MibScalar
ncdTcpOutBareAcks = _NcdTcpOutBareAcks_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 5, 5),
    _NcdTcpOutBareAcks_Type()
)
ncdTcpOutBareAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdTcpOutBareAcks.setStatus("optional")
_NcdTftp_ObjectIdentity = ObjectIdentity
ncdTftp = _NcdTftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 7)
)
_NcdTftpClientReadReqs_Type = Counter32
_NcdTftpClientReadReqs_Object = MibScalar
ncdTftpClientReadReqs = _NcdTftpClientReadReqs_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 7, 1),
    _NcdTftpClientReadReqs_Type()
)
ncdTftpClientReadReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdTftpClientReadReqs.setStatus("optional")
_NcdTftpClientWriteReqs_Type = Counter32
_NcdTftpClientWriteReqs_Object = MibScalar
ncdTftpClientWriteReqs = _NcdTftpClientWriteReqs_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 7, 2),
    _NcdTftpClientWriteReqs_Type()
)
ncdTftpClientWriteReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdTftpClientWriteReqs.setStatus("optional")
_NcdTftpClientInDataPkts_Type = Counter32
_NcdTftpClientInDataPkts_Object = MibScalar
ncdTftpClientInDataPkts = _NcdTftpClientInDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 7, 3),
    _NcdTftpClientInDataPkts_Type()
)
ncdTftpClientInDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdTftpClientInDataPkts.setStatus("optional")
_NcdTftpClientInAcks_Type = Counter32
_NcdTftpClientInAcks_Object = MibScalar
ncdTftpClientInAcks = _NcdTftpClientInAcks_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 7, 4),
    _NcdTftpClientInAcks_Type()
)
ncdTftpClientInAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdTftpClientInAcks.setStatus("optional")
_NcdTftpClientInNoFileErrors_Type = Counter32
_NcdTftpClientInNoFileErrors_Object = MibScalar
ncdTftpClientInNoFileErrors = _NcdTftpClientInNoFileErrors_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 7, 5),
    _NcdTftpClientInNoFileErrors_Type()
)
ncdTftpClientInNoFileErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdTftpClientInNoFileErrors.setStatus("optional")
_NcdTftpClientInAccessErrors_Type = Counter32
_NcdTftpClientInAccessErrors_Object = MibScalar
ncdTftpClientInAccessErrors = _NcdTftpClientInAccessErrors_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 7, 6),
    _NcdTftpClientInAccessErrors_Type()
)
ncdTftpClientInAccessErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdTftpClientInAccessErrors.setStatus("optional")
_NcdTftpClientInDiskFullErrors_Type = Counter32
_NcdTftpClientInDiskFullErrors_Object = MibScalar
ncdTftpClientInDiskFullErrors = _NcdTftpClientInDiskFullErrors_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 7, 7),
    _NcdTftpClientInDiskFullErrors_Type()
)
ncdTftpClientInDiskFullErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdTftpClientInDiskFullErrors.setStatus("optional")
_NcdTftpClientNoBufs_Type = Counter32
_NcdTftpClientNoBufs_Object = MibScalar
ncdTftpClientNoBufs = _NcdTftpClientNoBufs_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 7, 8),
    _NcdTftpClientNoBufs_Type()
)
ncdTftpClientNoBufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdTftpClientNoBufs.setStatus("optional")
_NcdTftpClientOutDataPkts_Type = Counter32
_NcdTftpClientOutDataPkts_Object = MibScalar
ncdTftpClientOutDataPkts = _NcdTftpClientOutDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 7, 9),
    _NcdTftpClientOutDataPkts_Type()
)
ncdTftpClientOutDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdTftpClientOutDataPkts.setStatus("optional")
_NcdTftpClientOutAcks_Type = Counter32
_NcdTftpClientOutAcks_Object = MibScalar
ncdTftpClientOutAcks = _NcdTftpClientOutAcks_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 7, 10),
    _NcdTftpClientOutAcks_Type()
)
ncdTftpClientOutAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdTftpClientOutAcks.setStatus("optional")
_NcdTftpClientRetrans_Type = Counter32
_NcdTftpClientRetrans_Object = MibScalar
ncdTftpClientRetrans = _NcdTftpClientRetrans_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 7, 11),
    _NcdTftpClientRetrans_Type()
)
ncdTftpClientRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdTftpClientRetrans.setStatus("optional")
_NcdTftpClientRetries_Type = Integer32
_NcdTftpClientRetries_Object = MibScalar
ncdTftpClientRetries = _NcdTftpClientRetries_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 7, 12),
    _NcdTftpClientRetries_Type()
)
ncdTftpClientRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncdTftpClientRetries.setStatus("optional")
_NcdTftpClientTimeout_Type = TimeTicks
_NcdTftpClientTimeout_Object = MibScalar
ncdTftpClientTimeout = _NcdTftpClientTimeout_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 7, 13),
    _NcdTftpClientTimeout_Type()
)
ncdTftpClientTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncdTftpClientTimeout.setStatus("optional")
_NcdNfs_ObjectIdentity = ObjectIdentity
ncdNfs = _NcdNfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8)
)
_NcdNfsClientNulls_Type = Counter32
_NcdNfsClientNulls_Object = MibScalar
ncdNfsClientNulls = _NcdNfsClientNulls_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 1),
    _NcdNfsClientNulls_Type()
)
ncdNfsClientNulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdNfsClientNulls.setStatus("optional")
_NcdNfsClientGetAttributes_Type = Counter32
_NcdNfsClientGetAttributes_Object = MibScalar
ncdNfsClientGetAttributes = _NcdNfsClientGetAttributes_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 2),
    _NcdNfsClientGetAttributes_Type()
)
ncdNfsClientGetAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdNfsClientGetAttributes.setStatus("optional")
_NcdNfsClientSetAttributes_Type = Counter32
_NcdNfsClientSetAttributes_Object = MibScalar
ncdNfsClientSetAttributes = _NcdNfsClientSetAttributes_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 3),
    _NcdNfsClientSetAttributes_Type()
)
ncdNfsClientSetAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdNfsClientSetAttributes.setStatus("optional")
_NcdNfsClientGetRoots_Type = Counter32
_NcdNfsClientGetRoots_Object = MibScalar
ncdNfsClientGetRoots = _NcdNfsClientGetRoots_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 4),
    _NcdNfsClientGetRoots_Type()
)
ncdNfsClientGetRoots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdNfsClientGetRoots.setStatus("optional")
_NcdNfsClientLookups_Type = Counter32
_NcdNfsClientLookups_Object = MibScalar
ncdNfsClientLookups = _NcdNfsClientLookups_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 5),
    _NcdNfsClientLookups_Type()
)
ncdNfsClientLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdNfsClientLookups.setStatus("optional")
_NcdNfsClientReadLinks_Type = Counter32
_NcdNfsClientReadLinks_Object = MibScalar
ncdNfsClientReadLinks = _NcdNfsClientReadLinks_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 6),
    _NcdNfsClientReadLinks_Type()
)
ncdNfsClientReadLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdNfsClientReadLinks.setStatus("optional")
_NcdNfsClientReads_Type = Counter32
_NcdNfsClientReads_Object = MibScalar
ncdNfsClientReads = _NcdNfsClientReads_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 7),
    _NcdNfsClientReads_Type()
)
ncdNfsClientReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdNfsClientReads.setStatus("optional")
_NcdNfsClientWriteCaches_Type = Counter32
_NcdNfsClientWriteCaches_Object = MibScalar
ncdNfsClientWriteCaches = _NcdNfsClientWriteCaches_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 8),
    _NcdNfsClientWriteCaches_Type()
)
ncdNfsClientWriteCaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdNfsClientWriteCaches.setStatus("optional")
_NcdNfsClientWrites_Type = Counter32
_NcdNfsClientWrites_Object = MibScalar
ncdNfsClientWrites = _NcdNfsClientWrites_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 9),
    _NcdNfsClientWrites_Type()
)
ncdNfsClientWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdNfsClientWrites.setStatus("optional")
_NcdNfsClientCreates_Type = Counter32
_NcdNfsClientCreates_Object = MibScalar
ncdNfsClientCreates = _NcdNfsClientCreates_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 10),
    _NcdNfsClientCreates_Type()
)
ncdNfsClientCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdNfsClientCreates.setStatus("optional")
_NcdNfsClientRemoves_Type = Counter32
_NcdNfsClientRemoves_Object = MibScalar
ncdNfsClientRemoves = _NcdNfsClientRemoves_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 11),
    _NcdNfsClientRemoves_Type()
)
ncdNfsClientRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdNfsClientRemoves.setStatus("optional")
_NcdNfsClientRenames_Type = Counter32
_NcdNfsClientRenames_Object = MibScalar
ncdNfsClientRenames = _NcdNfsClientRenames_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 12),
    _NcdNfsClientRenames_Type()
)
ncdNfsClientRenames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdNfsClientRenames.setStatus("optional")
_NcdNfsClientCreateLinks_Type = Counter32
_NcdNfsClientCreateLinks_Object = MibScalar
ncdNfsClientCreateLinks = _NcdNfsClientCreateLinks_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 13),
    _NcdNfsClientCreateLinks_Type()
)
ncdNfsClientCreateLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdNfsClientCreateLinks.setStatus("optional")
_NcdNfsClientCreateSymlinks_Type = Counter32
_NcdNfsClientCreateSymlinks_Object = MibScalar
ncdNfsClientCreateSymlinks = _NcdNfsClientCreateSymlinks_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 14),
    _NcdNfsClientCreateSymlinks_Type()
)
ncdNfsClientCreateSymlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdNfsClientCreateSymlinks.setStatus("optional")
_NcdNfsClientMakeDir_Type = Counter32
_NcdNfsClientMakeDir_Object = MibScalar
ncdNfsClientMakeDir = _NcdNfsClientMakeDir_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 15),
    _NcdNfsClientMakeDir_Type()
)
ncdNfsClientMakeDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdNfsClientMakeDir.setStatus("optional")
_NcdNfsClientRemoveDir_Type = Counter32
_NcdNfsClientRemoveDir_Object = MibScalar
ncdNfsClientRemoveDir = _NcdNfsClientRemoveDir_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 16),
    _NcdNfsClientRemoveDir_Type()
)
ncdNfsClientRemoveDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdNfsClientRemoveDir.setStatus("optional")
_NcdNfsClientReadDir_Type = Counter32
_NcdNfsClientReadDir_Object = MibScalar
ncdNfsClientReadDir = _NcdNfsClientReadDir_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 17),
    _NcdNfsClientReadDir_Type()
)
ncdNfsClientReadDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdNfsClientReadDir.setStatus("optional")
_NcdNfsClientStatFileSys_Type = Counter32
_NcdNfsClientStatFileSys_Object = MibScalar
ncdNfsClientStatFileSys = _NcdNfsClientStatFileSys_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 18),
    _NcdNfsClientStatFileSys_Type()
)
ncdNfsClientStatFileSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdNfsClientStatFileSys.setStatus("optional")
_NcdNfsMountTable_Object = MibTable
ncdNfsMountTable = _NcdNfsMountTable_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 19)
)
if mibBuilder.loadTexts:
    ncdNfsMountTable.setStatus("optional")
_NcdNfsMountEntry_Object = MibTableRow
ncdNfsMountEntry = _NcdNfsMountEntry_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 19, 1)
)
if mibBuilder.loadTexts:
    ncdNfsMountEntry.setStatus("optional")
_NcdNfsMountEntryIndex_Type = Integer32
_NcdNfsMountEntryIndex_Object = MibTableColumn
ncdNfsMountEntryIndex = _NcdNfsMountEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 19, 1, 1),
    _NcdNfsMountEntryIndex_Type()
)
ncdNfsMountEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdNfsMountEntryIndex.setStatus("optional")
_NcdNfsMountEntryLocalDir_Type = OctetString
_NcdNfsMountEntryLocalDir_Object = MibTableColumn
ncdNfsMountEntryLocalDir = _NcdNfsMountEntryLocalDir_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 19, 1, 2),
    _NcdNfsMountEntryLocalDir_Type()
)
ncdNfsMountEntryLocalDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdNfsMountEntryLocalDir.setStatus("optional")
_NcdNfsMountEntryServerAddr_Type = IpAddress
_NcdNfsMountEntryServerAddr_Object = MibTableColumn
ncdNfsMountEntryServerAddr = _NcdNfsMountEntryServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 19, 1, 3),
    _NcdNfsMountEntryServerAddr_Type()
)
ncdNfsMountEntryServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdNfsMountEntryServerAddr.setStatus("optional")
_NcdNfsMountEntryServerDir_Type = OctetString
_NcdNfsMountEntryServerDir_Object = MibTableColumn
ncdNfsMountEntryServerDir = _NcdNfsMountEntryServerDir_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 19, 1, 4),
    _NcdNfsMountEntryServerDir_Type()
)
ncdNfsMountEntryServerDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncdNfsMountEntryServerDir.setStatus("optional")
_NcdNfsMountEntryReadSize_Type = Integer32
_NcdNfsMountEntryReadSize_Object = MibTableColumn
ncdNfsMountEntryReadSize = _NcdNfsMountEntryReadSize_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 19, 1, 5),
    _NcdNfsMountEntryReadSize_Type()
)
ncdNfsMountEntryReadSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncdNfsMountEntryReadSize.setStatus("optional")
_NcdNfsMountEntryWriteSize_Type = Integer32
_NcdNfsMountEntryWriteSize_Object = MibTableColumn
ncdNfsMountEntryWriteSize = _NcdNfsMountEntryWriteSize_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 19, 1, 6),
    _NcdNfsMountEntryWriteSize_Type()
)
ncdNfsMountEntryWriteSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncdNfsMountEntryWriteSize.setStatus("optional")
_NcdNfsMountEntryRetrans_Type = Integer32
_NcdNfsMountEntryRetrans_Object = MibScalar
ncdNfsMountEntryRetrans = _NcdNfsMountEntryRetrans_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 19, 1, 7),
    _NcdNfsMountEntryRetrans_Type()
)
ncdNfsMountEntryRetrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncdNfsMountEntryRetrans.setStatus("optional")
_NcdNfsMountEntryTimeout_Type = TimeTicks
_NcdNfsMountEntryTimeout_Object = MibTableColumn
ncdNfsMountEntryTimeout = _NcdNfsMountEntryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 82, 2, 1, 8, 19, 1, 8),
    _NcdNfsMountEntryTimeout_Type()
)
ncdNfsMountEntryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncdNfsMountEntryTimeout.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NCD-MIB-1",
    **{"ncd": ncd,
       "ncd-products": ncd_products,
       "ncd16": ncd16,
       "ncd19": ncd19,
       "ncd17c": ncd17c,
       "ncd16e": ncd16e,
       "ncd-mibs": ncd_mibs,
       "ncd-mibs-mib1": ncd_mibs_mib1,
       "ncdSystem": ncdSystem,
       "ncdSysMemTotal": ncdSysMemTotal,
       "ncdSysMemAvail": ncdSysMemAvail,
       "ncdSysMemFrags": ncdSysMemFrags,
       "ncdSysIdleTime": ncdSysIdleTime,
       "ncdMbuf": ncdMbuf,
       "ncdMbufTotal": ncdMbufTotal,
       "ncdMbufFree": ncdMbufFree,
       "ncdMbufClusterTotal": ncdMbufClusterTotal,
       "ncdMbufClusterFree": ncdMbufClusterFree,
       "ncdMbufReserved": ncdMbufReserved,
       "ncdMbufDrops": ncdMbufDrops,
       "ncdMbufWaits": ncdMbufWaits,
       "ncdMbufData": ncdMbufData,
       "ncdMbufHeader": ncdMbufHeader,
       "ncdMbufSocket": ncdMbufSocket,
       "ncdMbufProtoCtrlBlock": ncdMbufProtoCtrlBlock,
       "ncdMbufRouteTable": ncdMbufRouteTable,
       "ncdMbufAtTable": ncdMbufAtTable,
       "ncdMbufSocketName": ncdMbufSocketName,
       "ncdMbufSocketOptions": ncdMbufSocketOptions,
       "ncdMbufFrags": ncdMbufFrags,
       "ncdMbufInterfaceAddr": ncdMbufInterfaceAddr,
       "ncdEther": ncdEther,
       "ncdEtherTable": ncdEtherTable,
       "ncdEtherEntry": ncdEtherEntry,
       "ncdEtherInCrcErrors": ncdEtherInCrcErrors,
       "ncdEtherInMissed": ncdEtherInMissed,
       "ncdEtherInFrameErrors": ncdEtherInFrameErrors,
       "ncdEtherSingleCollisions": ncdEtherSingleCollisions,
       "ncdEtherMultipleCollisions": ncdEtherMultipleCollisions,
       "ncdEtherLateCollisions": ncdEtherLateCollisions,
       "ncdEtherOutDeferred": ncdEtherOutDeferred,
       "ncdEtherOutRetryErrors": ncdEtherOutRetryErrors,
       "ncdEtherLostCarrier": ncdEtherLostCarrier,
       "ncdEtherRestarts": ncdEtherRestarts,
       "ncdSerial": ncdSerial,
       "ncdSerialTable": ncdSerialTable,
       "ncdSerialEntry": ncdSerialEntry,
       "ncdSerialInOverruns": ncdSerialInOverruns,
       "ncdSerialInFrameErrors": ncdSerialInFrameErrors,
       "ncdSerialInParityErrors": ncdSerialInParityErrors,
       "ncdSerialInBreakErrors": ncdSerialInBreakErrors,
       "ncdTcp": ncdTcp,
       "ncdTcpRetransDrops": ncdTcpRetransDrops,
       "ncdTcpOutKeepAlives": ncdTcpOutKeepAlives,
       "ncdTcpKeepAliveDrops": ncdTcpKeepAliveDrops,
       "ncdTcpInAcks": ncdTcpInAcks,
       "ncdTcpOutBareAcks": ncdTcpOutBareAcks,
       "ncdTftp": ncdTftp,
       "ncdTftpClientReadReqs": ncdTftpClientReadReqs,
       "ncdTftpClientWriteReqs": ncdTftpClientWriteReqs,
       "ncdTftpClientInDataPkts": ncdTftpClientInDataPkts,
       "ncdTftpClientInAcks": ncdTftpClientInAcks,
       "ncdTftpClientInNoFileErrors": ncdTftpClientInNoFileErrors,
       "ncdTftpClientInAccessErrors": ncdTftpClientInAccessErrors,
       "ncdTftpClientInDiskFullErrors": ncdTftpClientInDiskFullErrors,
       "ncdTftpClientNoBufs": ncdTftpClientNoBufs,
       "ncdTftpClientOutDataPkts": ncdTftpClientOutDataPkts,
       "ncdTftpClientOutAcks": ncdTftpClientOutAcks,
       "ncdTftpClientRetrans": ncdTftpClientRetrans,
       "ncdTftpClientRetries": ncdTftpClientRetries,
       "ncdTftpClientTimeout": ncdTftpClientTimeout,
       "ncdNfs": ncdNfs,
       "ncdNfsClientNulls": ncdNfsClientNulls,
       "ncdNfsClientGetAttributes": ncdNfsClientGetAttributes,
       "ncdNfsClientSetAttributes": ncdNfsClientSetAttributes,
       "ncdNfsClientGetRoots": ncdNfsClientGetRoots,
       "ncdNfsClientLookups": ncdNfsClientLookups,
       "ncdNfsClientReadLinks": ncdNfsClientReadLinks,
       "ncdNfsClientReads": ncdNfsClientReads,
       "ncdNfsClientWriteCaches": ncdNfsClientWriteCaches,
       "ncdNfsClientWrites": ncdNfsClientWrites,
       "ncdNfsClientCreates": ncdNfsClientCreates,
       "ncdNfsClientRemoves": ncdNfsClientRemoves,
       "ncdNfsClientRenames": ncdNfsClientRenames,
       "ncdNfsClientCreateLinks": ncdNfsClientCreateLinks,
       "ncdNfsClientCreateSymlinks": ncdNfsClientCreateSymlinks,
       "ncdNfsClientMakeDir": ncdNfsClientMakeDir,
       "ncdNfsClientRemoveDir": ncdNfsClientRemoveDir,
       "ncdNfsClientReadDir": ncdNfsClientReadDir,
       "ncdNfsClientStatFileSys": ncdNfsClientStatFileSys,
       "ncdNfsMountTable": ncdNfsMountTable,
       "ncdNfsMountEntry": ncdNfsMountEntry,
       "ncdNfsMountEntryIndex": ncdNfsMountEntryIndex,
       "ncdNfsMountEntryLocalDir": ncdNfsMountEntryLocalDir,
       "ncdNfsMountEntryServerAddr": ncdNfsMountEntryServerAddr,
       "ncdNfsMountEntryServerDir": ncdNfsMountEntryServerDir,
       "ncdNfsMountEntryReadSize": ncdNfsMountEntryReadSize,
       "ncdNfsMountEntryWriteSize": ncdNfsMountEntryWriteSize,
       "ncdNfsMountEntryRetrans": ncdNfsMountEntryRetrans,
       "ncdNfsMountEntryTimeout": ncdNfsMountEntryTimeout}
)
