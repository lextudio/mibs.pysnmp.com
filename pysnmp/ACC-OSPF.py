# SNMP MIB module (ACC-OSPF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-OSPF
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:41 2024
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

(AreaID,
 InterfaceIndex,
 RouterID,
 Status,
 TruthValue,
 ospfASBdrRtrStatus,
 ospfAdminStat,
 ospfAreaAggregateAreaID,
 ospfAreaAggregateMask,
 ospfAreaAggregateNet,
 ospfAreaId,
 ospfIfIpAddress,
 ospfIfType,
 ospfLsdbType,
 ospfMulticastExtensions,
 ospfNbrIpAddr,
 ospfRouterId,
 ospfTOSSupport,
 ospfVirtIfAreaId,
 ospfVirtIfNeighbor,
 ospfVirtNbrArea) = mibBuilder.importSymbols(
    "ACC-FAKE",
    "AreaID",
    "InterfaceIndex",
    "RouterID",
    "Status",
    "TruthValue",
    "ospfASBdrRtrStatus",
    "ospfAdminStat",
    "ospfAreaAggregateAreaID",
    "ospfAreaAggregateMask",
    "ospfAreaAggregateNet",
    "ospfAreaId",
    "ospfIfIpAddress",
    "ospfIfType",
    "ospfLsdbType",
    "ospfMulticastExtensions",
    "ospfNbrIpAddr",
    "ospfRouterId",
    "ospfTOSSupport",
    "ospfVirtIfAreaId",
    "ospfVirtIfNeighbor",
    "ospfVirtNbrArea")

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

(ospfLsdbAreaId,) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "ospfLsdbAreaId")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class OspfNbrIpAddr(IpAddress):
    """Custom type OspfNbrIpAddr based on IpAddress"""




class OspfNbrAddressLessIndex(Integer32):
    """Custom type OspfNbrAddressLessIndex based on Integer32"""




class OspfIfIpAddress(IpAddress):
    """Custom type OspfIfIpAddress based on IpAddress"""




class OspfAreaId(IpAddress):
    """Custom type OspfAreaId based on IpAddress"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccOspf_ObjectIdentity = ObjectIdentity
accOspf = _AccOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52)
)
_AccOspfGeneral_ObjectIdentity = ObjectIdentity
accOspfGeneral = _AccOspfGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 1)
)


class _AccOspfMessageLevel_Type(Integer32):
    """Custom type accOspfMessageLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccOspfMessageLevel_Type.__name__ = "Integer32"
_AccOspfMessageLevel_Object = MibScalar
accOspfMessageLevel = _AccOspfMessageLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 1, 1),
    _AccOspfMessageLevel_Type()
)
accOspfMessageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accOspfMessageLevel.setStatus("mandatory")
_AccOspfAreaTable_Object = MibTable
accOspfAreaTable = _AccOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 3)
)
if mibBuilder.loadTexts:
    accOspfAreaTable.setStatus("mandatory")
_AccOspfAreaEntry_Object = MibTableRow
accOspfAreaEntry = _AccOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 3, 1)
)
accOspfAreaEntry.setIndexNames(
    (0, "ACC-FAKE", "ospfAreaId"),
)
if mibBuilder.loadTexts:
    accOspfAreaEntry.setStatus("mandatory")


class _AccOspfAreaMessageLevel_Type(Integer32):
    """Custom type accOspfAreaMessageLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccOspfAreaMessageLevel_Type.__name__ = "Integer32"
_AccOspfAreaMessageLevel_Object = MibTableColumn
accOspfAreaMessageLevel = _AccOspfAreaMessageLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 3, 1, 1),
    _AccOspfAreaMessageLevel_Type()
)
accOspfAreaMessageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accOspfAreaMessageLevel.setStatus("mandatory")
_AccOspfIfTable_Object = MibTable
accOspfIfTable = _AccOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 4)
)
if mibBuilder.loadTexts:
    accOspfIfTable.setStatus("mandatory")
_AccOspfIfEntry_Object = MibTableRow
accOspfIfEntry = _AccOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 4, 1)
)
accOspfIfEntry.setIndexNames(
    (0, "ACC-FAKE", "ospfIfIpAddress"),
    (0, "ACC-OSPF", "ospfAddressLessIf"),
)
if mibBuilder.loadTexts:
    accOspfIfEntry.setStatus("mandatory")


class _AccOspfIfMessageLevel_Type(Integer32):
    """Custom type accOspfIfMessageLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccOspfIfMessageLevel_Type.__name__ = "Integer32"
_AccOspfIfMessageLevel_Object = MibTableColumn
accOspfIfMessageLevel = _AccOspfIfMessageLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 4, 1, 1),
    _AccOspfIfMessageLevel_Type()
)
accOspfIfMessageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accOspfIfMessageLevel.setStatus("mandatory")
_AccOspfNbrTable_Object = MibTable
accOspfNbrTable = _AccOspfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 5)
)
if mibBuilder.loadTexts:
    accOspfNbrTable.setStatus("mandatory")
_AccOspfNbrEntry_Object = MibTableRow
accOspfNbrEntry = _AccOspfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 5, 1)
)
accOspfNbrEntry.setIndexNames(
    (0, "ACC-FAKE", "ospfNbrIpAddr"),
    (0, "ACC-OSPF", "ospfNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    accOspfNbrEntry.setStatus("mandatory")


class _AccOspfNbrMessageLevel_Type(Integer32):
    """Custom type accOspfNbrMessageLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccOspfNbrMessageLevel_Type.__name__ = "Integer32"
_AccOspfNbrMessageLevel_Object = MibTableColumn
accOspfNbrMessageLevel = _AccOspfNbrMessageLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 5, 1, 1),
    _AccOspfNbrMessageLevel_Type()
)
accOspfNbrMessageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accOspfNbrMessageLevel.setStatus("mandatory")
_AccOspfExportTable_Object = MibTable
accOspfExportTable = _AccOspfExportTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 6)
)
if mibBuilder.loadTexts:
    accOspfExportTable.setStatus("mandatory")
_AccOspfExportEntry_Object = MibTableRow
accOspfExportEntry = _AccOspfExportEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 6, 1)
)
accOspfExportEntry.setIndexNames(
    (0, "ACC-OSPF", "accOspfExportProtocol"),
    (0, "ACC-OSPF", "accOspfExportSpecific2"),
    (0, "ACC-OSPF", "accOspfExportSpecific1"),
    (0, "ACC-OSPF", "accOspfExportNetwork"),
    (0, "ACC-OSPF", "accOspfExportMask"),
)
if mibBuilder.loadTexts:
    accOspfExportEntry.setStatus("mandatory")


class _AccOspfExportProtocol_Type(Integer32):
    """Custom type accOspfExportProtocol based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("ebgp", 7),
          ("eospf", 5),
          ("ibgp", 8),
          ("iospf", 4),
          ("local", 2),
          ("rip", 6),
          ("static", 3))
    )


_AccOspfExportProtocol_Type.__name__ = "Integer32"
_AccOspfExportProtocol_Object = MibTableColumn
accOspfExportProtocol = _AccOspfExportProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 6, 1, 1),
    _AccOspfExportProtocol_Type()
)
accOspfExportProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accOspfExportProtocol.setStatus("mandatory")
_AccOspfExportSpecific2_Type = Integer32
_AccOspfExportSpecific2_Object = MibTableColumn
accOspfExportSpecific2 = _AccOspfExportSpecific2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 6, 1, 2),
    _AccOspfExportSpecific2_Type()
)
accOspfExportSpecific2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accOspfExportSpecific2.setStatus("mandatory")
_AccOspfExportSpecific1_Type = Integer32
_AccOspfExportSpecific1_Object = MibTableColumn
accOspfExportSpecific1 = _AccOspfExportSpecific1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 6, 1, 3),
    _AccOspfExportSpecific1_Type()
)
accOspfExportSpecific1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accOspfExportSpecific1.setStatus("mandatory")
_AccOspfExportNetwork_Type = IpAddress
_AccOspfExportNetwork_Object = MibTableColumn
accOspfExportNetwork = _AccOspfExportNetwork_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 6, 1, 4),
    _AccOspfExportNetwork_Type()
)
accOspfExportNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accOspfExportNetwork.setStatus("mandatory")
_AccOspfExportMask_Type = IpAddress
_AccOspfExportMask_Object = MibTableColumn
accOspfExportMask = _AccOspfExportMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 6, 1, 5),
    _AccOspfExportMask_Type()
)
accOspfExportMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accOspfExportMask.setStatus("mandatory")


class _AccOspfExportAction_Type(Integer32):
    """Custom type accOspfExportAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("export", 1))
    )


_AccOspfExportAction_Type.__name__ = "Integer32"
_AccOspfExportAction_Object = MibTableColumn
accOspfExportAction = _AccOspfExportAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 6, 1, 6),
    _AccOspfExportAction_Type()
)
accOspfExportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accOspfExportAction.setStatus("mandatory")


class _AccOspfExportMetric_Type(Integer32):
    """Custom type accOspfExportMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AccOspfExportMetric_Type.__name__ = "Integer32"
_AccOspfExportMetric_Object = MibTableColumn
accOspfExportMetric = _AccOspfExportMetric_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 6, 1, 7),
    _AccOspfExportMetric_Type()
)
accOspfExportMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accOspfExportMetric.setStatus("mandatory")


class _AccOspfExportTag_Type(Integer32):
    """Custom type accOspfExportTag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AccOspfExportTag_Type.__name__ = "Integer32"
_AccOspfExportTag_Object = MibTableColumn
accOspfExportTag = _AccOspfExportTag_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 6, 1, 8),
    _AccOspfExportTag_Type()
)
accOspfExportTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accOspfExportTag.setStatus("mandatory")
_AccOspfExportStatus_Type = RowStatus
_AccOspfExportStatus_Object = MibTableColumn
accOspfExportStatus = _AccOspfExportStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 6, 1, 9),
    _AccOspfExportStatus_Type()
)
accOspfExportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accOspfExportStatus.setStatus("mandatory")
_AccOspfTraps_ObjectIdentity = ObjectIdentity
accOspfTraps = _AccOspfTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7)
)
_AccOspfTrapMsg_Type = DisplayString
_AccOspfTrapMsg_Object = MibScalar
accOspfTrapMsg = _AccOspfTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 1),
    _AccOspfTrapMsg_Type()
)
accOspfTrapMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accOspfTrapMsg.setStatus("mandatory")

# Managed Objects groups


# Notification objects

accOspfIntfNotNBMATrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 1)
)
accOspfIntfNotNBMATrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfIfIpAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfIntfNotNBMATrap.setStatus(
        ""
    )

accOspfAllocPolNodeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 2)
)
accOspfAllocPolNodeTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-OSPF", "accOspfExportNetwork"),
        ("ACC-OSPF", "accOspfExportMask"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfAllocPolNodeTrap.setStatus(
        ""
    )

accOspfNotificationIdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 3)
)
accOspfNotificationIdTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfNotificationIdTrap.setStatus(
        ""
    )

accOspfAreaTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 4)
)
accOspfAreaTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfAreaId"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfAreaTrap.setStatus(
        ""
    )

accOspfPrioTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 5)
)
accOspfPrioTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfIfIpAddress"),
        ("ACC-FAKE", "ospfIfType"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfPrioTrap.setStatus(
        ""
    )

accOspfPollIntTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 6)
)
accOspfPollIntTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfIfIpAddress"),
        ("ACC-FAKE", "ospfIfType"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfPollIntTrap.setStatus(
        ""
    )

accOspfBckboneAreaTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 7)
)
accOspfBckboneAreaTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfVirtIfAreaId"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfBckboneAreaTrap.setStatus(
        ""
    )

accOspfTransitAreaTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 8)
)
accOspfTransitAreaTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfVirtIfAreaId"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfTransitAreaTrap.setStatus(
        ""
    )

accOspfVirtLnkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 9)
)
accOspfVirtLnkTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfRouterId"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfVirtLnkTrap.setStatus(
        ""
    )

accOspfConfigBackboneTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 10)
)
accOspfConfigBackboneTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfAreaId"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfConfigBackboneTrap.setStatus(
        ""
    )

accOspfEnableAreaTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 11)
)
accOspfEnableAreaTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfAreaId"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfEnableAreaTrap.setStatus(
        ""
    )

accOspfAreaTransitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 12)
)
accOspfAreaTransitTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfAreaId"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfAreaTransitTrap.setStatus(
        ""
    )

accOspfDisableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 13)
)
accOspfDisableTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfDisableTrap.setStatus(
        ""
    )

accOspfInvASBRTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 14)
)
accOspfInvASBRTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfASBdrRtrStatus"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfInvASBRTrap.setStatus(
        ""
    )

accOspfNotifIdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 15)
)
accOspfNotifIdTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfNotifIdTrap.setStatus(
        ""
    )

accOspfInvTOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 16)
)
accOspfInvTOSTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfTOSSupport"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfInvTOSTrap.setStatus(
        ""
    )

accOspfInvMcastTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 17)
)
accOspfInvMcastTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfMulticastExtensions"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfInvMcastTrap.setStatus(
        ""
    )

accOspfEnableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 18)
)
accOspfEnableTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfAdminStat"),
        ("ACC-FAKE", "ospfRouterId"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfEnableTrap.setStatus(
        ""
    )

accOspfCreateAreaTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 19)
)
accOspfCreateAreaTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfAreaId"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfCreateAreaTrap.setStatus(
        ""
    )

accOspfCreateBckboneAreaTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 20)
)
accOspfCreateBckboneAreaTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfAreaId"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfCreateBckboneAreaTrap.setStatus(
        ""
    )

accOspfAddImpPolTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 21)
)
accOspfAddImpPolTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-OSPF", "accOspfExportNetwork"),
        ("ACC-OSPF", "accOspfExportMask"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfAddImpPolTrap.setStatus(
        ""
    )

accOspfTrap22 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 22)
)
accOspfTrap22.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfAreaId"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfTrap22.setStatus(
        ""
    )

accOspfCantEnableAreaTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 23)
)
accOspfCantEnableAreaTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfAreaId"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfCantEnableAreaTrap.setStatus(
        ""
    )

accOspfDelSummaryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 24)
)
accOspfDelSummaryTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfAreaAggregateAreaID"),
        ("ACC-FAKE", "ospfAreaAggregateNet"),
        ("ACC-FAKE", "ospfAreaAggregateMask"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfDelSummaryTrap.setStatus(
        ""
    )

accOspfAddRangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 25)
)
accOspfAddRangeTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfAreaAggregateAreaID"),
        ("ACC-FAKE", "ospfAreaAggregateNet"),
        ("ACC-FAKE", "ospfAreaAggregateMask"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfAddRangeTrap.setStatus(
        ""
    )

accOspfCreateIntfTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 26)
)
accOspfCreateIntfTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfIfIpAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfCreateIntfTrap.setStatus(
        ""
    )

accOspfEnableIntfTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 27)
)
accOspfEnableIntfTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfIfIpAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfEnableIntfTrap.setStatus(
        ""
    )

accOspfLocateIntfTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 28)
)
accOspfLocateIntfTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfIfIpAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfLocateIntfTrap.setStatus(
        ""
    )

accOspfLocateTransitAreaTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 29)
)
accOspfLocateTransitAreaTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfVirtNbrArea"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfLocateTransitAreaTrap.setStatus(
        ""
    )

accOspfEnableVirtIntfTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 30)
)
accOspfEnableVirtIntfTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfVirtNbrArea"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfEnableVirtIntfTrap.setStatus(
        ""
    )

accOspfCreateNbmaNbrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 31)
)
accOspfCreateNbmaNbrTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfNbrIpAddr"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfCreateNbmaNbrTrap.setStatus(
        ""
    )

accOspfAckTqTmrAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 32)
)
accOspfAckTqTmrAllocTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfRouterId"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfAckTqTmrAllocTrap.setStatus(
        ""
    )

accOspfSumTqTmrAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 33)
)
accOspfSumTqTmrAllocTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfRouterId"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfSumTqTmrAllocTrap.setStatus(
        ""
    )

accOspfDbageTqTmrAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 34)
)
accOspfDbageTqTmrAllocTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfRouterId"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfDbageTqTmrAllocTrap.setStatus(
        ""
    )

accOspfAseTqTmrAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 35)
)
accOspfAseTqTmrAllocTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfRouterId"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfAseTqTmrAllocTrap.setStatus(
        ""
    )

accOspfDbhAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 36)
)
accOspfDbhAllocTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfLsdbType"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfDbhAllocTrap.setStatus(
        ""
    )

accOspfTrap37 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 37)
)
accOspfTrap37.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfVirtIfAreaId"),
        ("ACC-FAKE", "ospfVirtIfNeighbor"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfTrap37.setStatus(
        ""
    )

accOspfInitSbTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 38)
)
accOspfInitSbTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfLsdbType"),
        ("OSPF-MIB", "ospfLsdbAreaId"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfInitSbTrap.setStatus(
        ""
    )

accOspfFreingNotifiIdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 39)
)
accOspfFreingNotifiIdTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfFreingNotifiIdTrap.setStatus(
        ""
    )

accOspfNoBackboneTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 52, 7, 0, 40)
)
accOspfNoBackboneTrap.setObjects(
      *(("ACC-OSPF", "accOspfTrapMsg"),
        ("ACC-FAKE", "ospfVirtNbrArea"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accOspfNoBackboneTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-OSPF",
    **{"OspfNbrIpAddr": OspfNbrIpAddr,
       "OspfNbrAddressLessIndex": OspfNbrAddressLessIndex,
       "OspfIfIpAddress": OspfIfIpAddress,
       "OspfAreaId": OspfAreaId,
       "accOspf": accOspf,
       "accOspfGeneral": accOspfGeneral,
       "accOspfMessageLevel": accOspfMessageLevel,
       "accOspfAreaTable": accOspfAreaTable,
       "accOspfAreaEntry": accOspfAreaEntry,
       "accOspfAreaMessageLevel": accOspfAreaMessageLevel,
       "accOspfIfTable": accOspfIfTable,
       "accOspfIfEntry": accOspfIfEntry,
       "accOspfIfMessageLevel": accOspfIfMessageLevel,
       "accOspfNbrTable": accOspfNbrTable,
       "accOspfNbrEntry": accOspfNbrEntry,
       "accOspfNbrMessageLevel": accOspfNbrMessageLevel,
       "accOspfExportTable": accOspfExportTable,
       "accOspfExportEntry": accOspfExportEntry,
       "accOspfExportProtocol": accOspfExportProtocol,
       "accOspfExportSpecific2": accOspfExportSpecific2,
       "accOspfExportSpecific1": accOspfExportSpecific1,
       "accOspfExportNetwork": accOspfExportNetwork,
       "accOspfExportMask": accOspfExportMask,
       "accOspfExportAction": accOspfExportAction,
       "accOspfExportMetric": accOspfExportMetric,
       "accOspfExportTag": accOspfExportTag,
       "accOspfExportStatus": accOspfExportStatus,
       "accOspfTraps": accOspfTraps,
       "accOspfIntfNotNBMATrap": accOspfIntfNotNBMATrap,
       "accOspfAllocPolNodeTrap": accOspfAllocPolNodeTrap,
       "accOspfNotificationIdTrap": accOspfNotificationIdTrap,
       "accOspfAreaTrap": accOspfAreaTrap,
       "accOspfPrioTrap": accOspfPrioTrap,
       "accOspfPollIntTrap": accOspfPollIntTrap,
       "accOspfBckboneAreaTrap": accOspfBckboneAreaTrap,
       "accOspfTransitAreaTrap": accOspfTransitAreaTrap,
       "accOspfVirtLnkTrap": accOspfVirtLnkTrap,
       "accOspfConfigBackboneTrap": accOspfConfigBackboneTrap,
       "accOspfEnableAreaTrap": accOspfEnableAreaTrap,
       "accOspfAreaTransitTrap": accOspfAreaTransitTrap,
       "accOspfDisableTrap": accOspfDisableTrap,
       "accOspfInvASBRTrap": accOspfInvASBRTrap,
       "accOspfNotifIdTrap": accOspfNotifIdTrap,
       "accOspfInvTOSTrap": accOspfInvTOSTrap,
       "accOspfInvMcastTrap": accOspfInvMcastTrap,
       "accOspfEnableTrap": accOspfEnableTrap,
       "accOspfCreateAreaTrap": accOspfCreateAreaTrap,
       "accOspfCreateBckboneAreaTrap": accOspfCreateBckboneAreaTrap,
       "accOspfAddImpPolTrap": accOspfAddImpPolTrap,
       "accOspfTrap22": accOspfTrap22,
       "accOspfCantEnableAreaTrap": accOspfCantEnableAreaTrap,
       "accOspfDelSummaryTrap": accOspfDelSummaryTrap,
       "accOspfAddRangeTrap": accOspfAddRangeTrap,
       "accOspfCreateIntfTrap": accOspfCreateIntfTrap,
       "accOspfEnableIntfTrap": accOspfEnableIntfTrap,
       "accOspfLocateIntfTrap": accOspfLocateIntfTrap,
       "accOspfLocateTransitAreaTrap": accOspfLocateTransitAreaTrap,
       "accOspfEnableVirtIntfTrap": accOspfEnableVirtIntfTrap,
       "accOspfCreateNbmaNbrTrap": accOspfCreateNbmaNbrTrap,
       "accOspfAckTqTmrAllocTrap": accOspfAckTqTmrAllocTrap,
       "accOspfSumTqTmrAllocTrap": accOspfSumTqTmrAllocTrap,
       "accOspfDbageTqTmrAllocTrap": accOspfDbageTqTmrAllocTrap,
       "accOspfAseTqTmrAllocTrap": accOspfAseTqTmrAllocTrap,
       "accOspfDbhAllocTrap": accOspfDbhAllocTrap,
       "accOspfTrap37": accOspfTrap37,
       "accOspfInitSbTrap": accOspfInitSbTrap,
       "accOspfFreingNotifiIdTrap": accOspfFreingNotifiIdTrap,
       "accOspfNoBackboneTrap": accOspfNoBackboneTrap,
       "accOspfTrapMsg": accOspfTrapMsg}
)
