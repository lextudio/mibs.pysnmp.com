# SNMP MIB module (HUAWEI-MPLS-EXTEND-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MPLS-EXTEND-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:06 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(MplsIndexType,) = mibBuilder.importSymbols(
    "MPLS-LSR-STD-MIB",
    "MplsIndexType")

(MplsExtendedTunnelId,
 MplsLsrIdentifier,
 MplsTunnelIndex,
 MplsTunnelInstanceIndex) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsExtendedTunnelId",
    "MplsLsrIdentifier",
    "MplsTunnelIndex",
    "MplsTunnelInstanceIndex")

(mplsTunnelAdminStatus,
 mplsTunnelOperStatus) = mibBuilder.importSymbols(
    "MPLS-TE-STD-MIB",
    "mplsTunnelAdminStatus",
    "mplsTunnelOperStatus")

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
 Bits,
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

hwMplsExtendMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121)
)
hwMplsExtendMib.setRevisions(
        ("2015-08-01 12:00",
         "2015-04-11 12:00",
         "2015-03-31 14:19",
         "2015-03-19 17:00",
         "2015-01-22 19:16",
         "2015-01-12 20:16",
         "2014-11-21 18:00",
         "2014-11-14 18:00",
         "2014-11-06 16:30",
         "2014-08-12 14:50",
         "2014-07-21 14:27",
         "2014-06-16 14:17",
         "2014-02-17 19:05",
         "2014-02-07 11:00",
         "2014-01-27 11:00",
         "2014-01-13 13:45",
         "2013-11-07 17:45",
         "2013-09-11 17:45",
         "2013-04-13 16:52",
         "2013-01-14 15:25",
         "2012-07-05 20:25",
         "2012-06-08 14:05",
         "2012-06-05 11:00",
         "2012-05-09 11:00",
         "2012-05-04 11:00",
         "2011-11-29 11:00",
         "2011-11-18 11:00",
         "2011-10-24 11:00",
         "2011-07-30 11:00",
         "2010-11-23 11:55",
         "2010-07-13 15:35",
         "2006-06-30 15:54")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwMplsExtendMibTunnel_ObjectIdentity = ObjectIdentity
hwMplsExtendMibTunnel = _HwMplsExtendMibTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1)
)
_HwMplsTunnelTable_Object = MibTable
hwMplsTunnelTable = _HwMplsTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1)
)
if mibBuilder.loadTexts:
    hwMplsTunnelTable.setStatus("current")
_HwMplsTunnelEntry_Object = MibTableRow
hwMplsTunnelEntry = _HwMplsTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1)
)
hwMplsTunnelEntry.setIndexNames(
    (0, "HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelIndex"),
    (0, "HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInstance"),
    (0, "HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelIngressLSRId"),
    (0, "HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelEgressLSRId"),
)
if mibBuilder.loadTexts:
    hwMplsTunnelEntry.setStatus("current")
_HwMplsTunnelIndex_Type = MplsTunnelIndex
_HwMplsTunnelIndex_Object = MibTableColumn
hwMplsTunnelIndex = _HwMplsTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 1),
    _HwMplsTunnelIndex_Type()
)
hwMplsTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsTunnelIndex.setStatus("current")
_HwMplsTunnelInstance_Type = MplsTunnelInstanceIndex
_HwMplsTunnelInstance_Object = MibTableColumn
hwMplsTunnelInstance = _HwMplsTunnelInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 2),
    _HwMplsTunnelInstance_Type()
)
hwMplsTunnelInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsTunnelInstance.setStatus("current")
_HwMplsTunnelIngressLSRId_Type = MplsExtendedTunnelId
_HwMplsTunnelIngressLSRId_Object = MibTableColumn
hwMplsTunnelIngressLSRId = _HwMplsTunnelIngressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 3),
    _HwMplsTunnelIngressLSRId_Type()
)
hwMplsTunnelIngressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsTunnelIngressLSRId.setStatus("current")
_HwMplsTunnelEgressLSRId_Type = MplsExtendedTunnelId
_HwMplsTunnelEgressLSRId_Object = MibTableColumn
hwMplsTunnelEgressLSRId = _HwMplsTunnelEgressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 4),
    _HwMplsTunnelEgressLSRId_Type()
)
hwMplsTunnelEgressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsTunnelEgressLSRId.setStatus("current")


class _HwMplsTunnelClassType_Type(Integer32):
    """Custom type hwMplsTunnelClassType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bc0", 1),
          ("bc1", 2),
          ("invalidValue", 3))
    )


_HwMplsTunnelClassType_Type.__name__ = "Integer32"
_HwMplsTunnelClassType_Object = MibTableColumn
hwMplsTunnelClassType = _HwMplsTunnelClassType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 5),
    _HwMplsTunnelClassType_Type()
)
hwMplsTunnelClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelClassType.setStatus("current")
_HwMplsTunnelBandwidth_Type = Integer32
_HwMplsTunnelBandwidth_Object = MibTableColumn
hwMplsTunnelBandwidth = _HwMplsTunnelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 6),
    _HwMplsTunnelBandwidth_Type()
)
hwMplsTunnelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelBandwidth.setStatus("current")


class _HwMplsTunnelAdminStatus_Type(Integer32):
    """Custom type hwMplsTunnelAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_HwMplsTunnelAdminStatus_Type.__name__ = "Integer32"
_HwMplsTunnelAdminStatus_Object = MibTableColumn
hwMplsTunnelAdminStatus = _HwMplsTunnelAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 7),
    _HwMplsTunnelAdminStatus_Type()
)
hwMplsTunnelAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelAdminStatus.setStatus("current")


class _HwMplsTunnelOperStatus_Type(Integer32):
    """Custom type hwMplsTunnelOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_HwMplsTunnelOperStatus_Type.__name__ = "Integer32"
_HwMplsTunnelOperStatus_Object = MibTableColumn
hwMplsTunnelOperStatus = _HwMplsTunnelOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 8),
    _HwMplsTunnelOperStatus_Type()
)
hwMplsTunnelOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelOperStatus.setStatus("current")


class _HwMplsTunnelSessionAttr_Type(Bits):
    """Custom type hwMplsTunnelSessionAttr based on Bits"""
    namedValues = NamedValues(
        *(("bandwidthProtectionDesired", 2),
          ("localProtectionDesired", 0),
          ("nodeProtectionDesired", 1))
    )

_HwMplsTunnelSessionAttr_Type.__name__ = "Bits"
_HwMplsTunnelSessionAttr_Object = MibTableColumn
hwMplsTunnelSessionAttr = _HwMplsTunnelSessionAttr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 9),
    _HwMplsTunnelSessionAttr_Type()
)
hwMplsTunnelSessionAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelSessionAttr.setStatus("current")
_HwMplsTunnelFrrSetupPrio_Type = Unsigned32
_HwMplsTunnelFrrSetupPrio_Object = MibTableColumn
hwMplsTunnelFrrSetupPrio = _HwMplsTunnelFrrSetupPrio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 10),
    _HwMplsTunnelFrrSetupPrio_Type()
)
hwMplsTunnelFrrSetupPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelFrrSetupPrio.setStatus("current")
_HwMplsTunnelFrrHoldingPrio_Type = Unsigned32
_HwMplsTunnelFrrHoldingPrio_Object = MibTableColumn
hwMplsTunnelFrrHoldingPrio = _HwMplsTunnelFrrHoldingPrio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 11),
    _HwMplsTunnelFrrHoldingPrio_Type()
)
hwMplsTunnelFrrHoldingPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelFrrHoldingPrio.setStatus("current")
_HwMplsTunnelFrrBandwidth_Type = Unsigned32
_HwMplsTunnelFrrBandwidth_Object = MibTableColumn
hwMplsTunnelFrrBandwidth = _HwMplsTunnelFrrBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 12),
    _HwMplsTunnelFrrBandwidth_Type()
)
hwMplsTunnelFrrBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelFrrBandwidth.setStatus("current")
_HwMplsTunnelFrrSwitchover_Type = Counter32
_HwMplsTunnelFrrSwitchover_Object = MibTableColumn
hwMplsTunnelFrrSwitchover = _HwMplsTunnelFrrSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 13),
    _HwMplsTunnelFrrSwitchover_Type()
)
hwMplsTunnelFrrSwitchover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelFrrSwitchover.setStatus("current")
_HwMplsTunnelFrrBypassTableIndex_Type = Unsigned32
_HwMplsTunnelFrrBypassTableIndex_Object = MibTableColumn
hwMplsTunnelFrrBypassTableIndex = _HwMplsTunnelFrrBypassTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 14),
    _HwMplsTunnelFrrBypassTableIndex_Type()
)
hwMplsTunnelFrrBypassTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelFrrBypassTableIndex.setStatus("current")
_HwMplsTunnelFrrARHopTableIndex_Type = Unsigned32
_HwMplsTunnelFrrARHopTableIndex_Object = MibTableColumn
hwMplsTunnelFrrARHopTableIndex = _HwMplsTunnelFrrARHopTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 15),
    _HwMplsTunnelFrrARHopTableIndex_Type()
)
hwMplsTunnelFrrARHopTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelFrrARHopTableIndex.setStatus("current")
_HwMplsTunnelName_Type = SnmpAdminString
_HwMplsTunnelName_Object = MibTableColumn
hwMplsTunnelName = _HwMplsTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 16),
    _HwMplsTunnelName_Type()
)
hwMplsTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelName.setStatus("current")
_HwMplsTunnelIfIndex_Type = Unsigned32
_HwMplsTunnelIfIndex_Object = MibTableColumn
hwMplsTunnelIfIndex = _HwMplsTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 17),
    _HwMplsTunnelIfIndex_Type()
)
hwMplsTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelIfIndex.setStatus("current")
_HwMplsTunnelPreBandwidth_Type = Unsigned32
_HwMplsTunnelPreBandwidth_Object = MibTableColumn
hwMplsTunnelPreBandwidth = _HwMplsTunnelPreBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 18),
    _HwMplsTunnelPreBandwidth_Type()
)
hwMplsTunnelPreBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelPreBandwidth.setStatus("current")
_HwMplsTunnelNextBandwidth_Type = Unsigned32
_HwMplsTunnelNextBandwidth_Object = MibTableColumn
hwMplsTunnelNextBandwidth = _HwMplsTunnelNextBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 19),
    _HwMplsTunnelNextBandwidth_Type()
)
hwMplsTunnelNextBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelNextBandwidth.setStatus("current")
_HwMplsTunnelCt0Bandwidth_Type = Unsigned32
_HwMplsTunnelCt0Bandwidth_Object = MibTableColumn
hwMplsTunnelCt0Bandwidth = _HwMplsTunnelCt0Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 20),
    _HwMplsTunnelCt0Bandwidth_Type()
)
hwMplsTunnelCt0Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelCt0Bandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsTunnelCt0Bandwidth.setUnits("kilobits per second")
_HwMplsTunnelCt1Bandwidth_Type = Unsigned32
_HwMplsTunnelCt1Bandwidth_Object = MibTableColumn
hwMplsTunnelCt1Bandwidth = _HwMplsTunnelCt1Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 21),
    _HwMplsTunnelCt1Bandwidth_Type()
)
hwMplsTunnelCt1Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelCt1Bandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsTunnelCt1Bandwidth.setUnits("kilobits per second")
_HwMplsTunnelCt2Bandwidth_Type = Unsigned32
_HwMplsTunnelCt2Bandwidth_Object = MibTableColumn
hwMplsTunnelCt2Bandwidth = _HwMplsTunnelCt2Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 22),
    _HwMplsTunnelCt2Bandwidth_Type()
)
hwMplsTunnelCt2Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelCt2Bandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsTunnelCt2Bandwidth.setUnits("kilobits per second")
_HwMplsTunnelCt3Bandwidth_Type = Unsigned32
_HwMplsTunnelCt3Bandwidth_Object = MibTableColumn
hwMplsTunnelCt3Bandwidth = _HwMplsTunnelCt3Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 23),
    _HwMplsTunnelCt3Bandwidth_Type()
)
hwMplsTunnelCt3Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelCt3Bandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsTunnelCt3Bandwidth.setUnits("kilobits per second")
_HwMplsTunnelCt4Bandwidth_Type = Unsigned32
_HwMplsTunnelCt4Bandwidth_Object = MibTableColumn
hwMplsTunnelCt4Bandwidth = _HwMplsTunnelCt4Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 24),
    _HwMplsTunnelCt4Bandwidth_Type()
)
hwMplsTunnelCt4Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelCt4Bandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsTunnelCt4Bandwidth.setUnits("kilobits per second")
_HwMplsTunnelCt5Bandwidth_Type = Unsigned32
_HwMplsTunnelCt5Bandwidth_Object = MibTableColumn
hwMplsTunnelCt5Bandwidth = _HwMplsTunnelCt5Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 25),
    _HwMplsTunnelCt5Bandwidth_Type()
)
hwMplsTunnelCt5Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelCt5Bandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsTunnelCt5Bandwidth.setUnits("kilobits per second")
_HwMplsTunnelCt6Bandwidth_Type = Unsigned32
_HwMplsTunnelCt6Bandwidth_Object = MibTableColumn
hwMplsTunnelCt6Bandwidth = _HwMplsTunnelCt6Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 26),
    _HwMplsTunnelCt6Bandwidth_Type()
)
hwMplsTunnelCt6Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelCt6Bandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsTunnelCt6Bandwidth.setUnits("kilobits per second")
_HwMplsTunnelCt7Bandwidth_Type = Unsigned32
_HwMplsTunnelCt7Bandwidth_Object = MibTableColumn
hwMplsTunnelCt7Bandwidth = _HwMplsTunnelCt7Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 27),
    _HwMplsTunnelCt7Bandwidth_Type()
)
hwMplsTunnelCt7Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelCt7Bandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsTunnelCt7Bandwidth.setUnits("kilobits per second")


class _HwMplsTunnelLspType_Type(Integer32):
    """Custom type hwMplsTunnelLspType based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("bestEffort", 7),
          ("bestEffortModifing", 8),
          ("hotStandby", 3),
          ("hotStandbyModifing", 4),
          ("invalid", 0),
          ("ordinary", 5),
          ("ordinaryModifing", 6),
          ("primary", 1),
          ("primaryModifing", 2))
    )


_HwMplsTunnelLspType_Type.__name__ = "Integer32"
_HwMplsTunnelLspType_Object = MibTableColumn
hwMplsTunnelLspType = _HwMplsTunnelLspType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 28),
    _HwMplsTunnelLspType_Type()
)
hwMplsTunnelLspType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelLspType.setStatus("current")
_HwMplsTunnelInterfaceName_Type = SnmpAdminString
_HwMplsTunnelInterfaceName_Object = MibTableColumn
hwMplsTunnelInterfaceName = _HwMplsTunnelInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 29),
    _HwMplsTunnelInterfaceName_Type()
)
hwMplsTunnelInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelInterfaceName.setStatus("current")


class _HwMplsTunnelSignalProto_Type(Integer32):
    """Custom type hwMplsTunnelSignalProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rsvpTE", 1),
          ("static", 2),
          ("staticCR", 3))
    )


_HwMplsTunnelSignalProto_Type.__name__ = "Integer32"
_HwMplsTunnelSignalProto_Object = MibTableColumn
hwMplsTunnelSignalProto = _HwMplsTunnelSignalProto_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 30),
    _HwMplsTunnelSignalProto_Type()
)
hwMplsTunnelSignalProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelSignalProto.setStatus("current")


class _HwMplsTunnelType_Type(Integer32):
    """Custom type hwMplsTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bypassTunnel", 3),
          ("invalid", 1),
          ("primaryTunnel", 2))
    )


_HwMplsTunnelType_Type.__name__ = "Integer32"
_HwMplsTunnelType_Object = MibTableColumn
hwMplsTunnelType = _HwMplsTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 1, 1, 31),
    _HwMplsTunnelType_Type()
)
hwMplsTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelType.setStatus("current")
_HwTunnelFrrBypassTable_Object = MibTable
hwTunnelFrrBypassTable = _HwTunnelFrrBypassTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 2)
)
if mibBuilder.loadTexts:
    hwTunnelFrrBypassTable.setStatus("current")
_HwTunnelFrrBypassEntry_Object = MibTableRow
hwTunnelFrrBypassEntry = _HwTunnelFrrBypassEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 2, 1)
)
hwTunnelFrrBypassEntry.setIndexNames(
    (0, "HUAWEI-MPLS-EXTEND-MIB", "hwTunnelFrrBypassListIndex"),
    (0, "HUAWEI-MPLS-EXTEND-MIB", "hwTunnelFrrBypassIndex"),
)
if mibBuilder.loadTexts:
    hwTunnelFrrBypassEntry.setStatus("current")
_HwTunnelFrrBypassListIndex_Type = Unsigned32
_HwTunnelFrrBypassListIndex_Object = MibTableColumn
hwTunnelFrrBypassListIndex = _HwTunnelFrrBypassListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 2, 1, 1),
    _HwTunnelFrrBypassListIndex_Type()
)
hwTunnelFrrBypassListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTunnelFrrBypassListIndex.setStatus("current")
_HwTunnelFrrBypassIndex_Type = Unsigned32
_HwTunnelFrrBypassIndex_Object = MibTableColumn
hwTunnelFrrBypassIndex = _HwTunnelFrrBypassIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 2, 1, 2),
    _HwTunnelFrrBypassIndex_Type()
)
hwTunnelFrrBypassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTunnelFrrBypassIndex.setStatus("current")
_HwTunnelFrrBypassProtIfIndex_Type = Unsigned32
_HwTunnelFrrBypassProtIfIndex_Object = MibTableColumn
hwTunnelFrrBypassProtIfIndex = _HwTunnelFrrBypassProtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 2, 1, 3),
    _HwTunnelFrrBypassProtIfIndex_Type()
)
hwTunnelFrrBypassProtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTunnelFrrBypassProtIfIndex.setStatus("current")
_HwTunnelFrrARHopTable_Object = MibTable
hwTunnelFrrARHopTable = _HwTunnelFrrARHopTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 3)
)
if mibBuilder.loadTexts:
    hwTunnelFrrARHopTable.setStatus("current")
_HwTunnelFrrARHopEntry_Object = MibTableRow
hwTunnelFrrARHopEntry = _HwTunnelFrrARHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 3, 1)
)
hwTunnelFrrARHopEntry.setIndexNames(
    (0, "HUAWEI-MPLS-EXTEND-MIB", "hwTunnelFrrARHopListIndex"),
    (0, "HUAWEI-MPLS-EXTEND-MIB", "hwTunnelFrrARHopIndex"),
)
if mibBuilder.loadTexts:
    hwTunnelFrrARHopEntry.setStatus("current")
_HwTunnelFrrARHopListIndex_Type = Unsigned32
_HwTunnelFrrARHopListIndex_Object = MibTableColumn
hwTunnelFrrARHopListIndex = _HwTunnelFrrARHopListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 3, 1, 1),
    _HwTunnelFrrARHopListIndex_Type()
)
hwTunnelFrrARHopListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTunnelFrrARHopListIndex.setStatus("current")
_HwTunnelFrrARHopIndex_Type = Unsigned32
_HwTunnelFrrARHopIndex_Object = MibTableColumn
hwTunnelFrrARHopIndex = _HwTunnelFrrARHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 3, 1, 2),
    _HwTunnelFrrARHopIndex_Type()
)
hwTunnelFrrARHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTunnelFrrARHopIndex.setStatus("current")


class _HwTunnelFrrARHopProtDesired_Type(Bits):
    """Custom type hwTunnelFrrARHopProtDesired based on Bits"""
    namedValues = NamedValues(
        *(("bandwidthProtection", 2),
          ("localProtection", 0),
          ("nodeProtection", 1))
    )

_HwTunnelFrrARHopProtDesired_Type.__name__ = "Bits"
_HwTunnelFrrARHopProtDesired_Object = MibTableColumn
hwTunnelFrrARHopProtDesired = _HwTunnelFrrARHopProtDesired_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 3, 1, 3),
    _HwTunnelFrrARHopProtDesired_Type()
)
hwTunnelFrrARHopProtDesired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTunnelFrrARHopProtDesired.setStatus("current")


class _HwTunnelFrrARHopProtActual_Type(Bits):
    """Custom type hwTunnelFrrARHopProtActual based on Bits"""
    namedValues = NamedValues(
        *(("bandwidthProtection", 2),
          ("localProtection", 0),
          ("nodeProtection", 1),
          ("protectionInuse", 3))
    )

_HwTunnelFrrARHopProtActual_Type.__name__ = "Bits"
_HwTunnelFrrARHopProtActual_Object = MibTableColumn
hwTunnelFrrARHopProtActual = _HwTunnelFrrARHopProtActual_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 3, 1, 4),
    _HwTunnelFrrARHopProtActual_Type()
)
hwTunnelFrrARHopProtActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTunnelFrrARHopProtActual.setStatus("current")
_HwTunnelFrrRouteDBTable_Object = MibTable
hwTunnelFrrRouteDBTable = _HwTunnelFrrRouteDBTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 4)
)
if mibBuilder.loadTexts:
    hwTunnelFrrRouteDBTable.setStatus("current")
_HwTunnelFrrRouteDBEntry_Object = MibTableRow
hwTunnelFrrRouteDBEntry = _HwTunnelFrrRouteDBEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 4, 1)
)
hwTunnelFrrRouteDBEntry.setIndexNames(
    (0, "HUAWEI-MPLS-EXTEND-MIB", "hwTunnelFrrRouteDBTunnelIndex"),
    (0, "HUAWEI-MPLS-EXTEND-MIB", "hwTunnelFrrRouteDBTunnelInstance"),
    (0, "HUAWEI-MPLS-EXTEND-MIB", "hwTunnelFrrRouteDBTunnelIngressLSRId"),
    (0, "HUAWEI-MPLS-EXTEND-MIB", "hwTunnelFrrRouteDBTunnelEngressLSRId"),
)
if mibBuilder.loadTexts:
    hwTunnelFrrRouteDBEntry.setStatus("current")
_HwTunnelFrrRouteDBTunnelIndex_Type = Unsigned32
_HwTunnelFrrRouteDBTunnelIndex_Object = MibTableColumn
hwTunnelFrrRouteDBTunnelIndex = _HwTunnelFrrRouteDBTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 4, 1, 1),
    _HwTunnelFrrRouteDBTunnelIndex_Type()
)
hwTunnelFrrRouteDBTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTunnelFrrRouteDBTunnelIndex.setStatus("current")
_HwTunnelFrrRouteDBTunnelInstance_Type = Unsigned32
_HwTunnelFrrRouteDBTunnelInstance_Object = MibTableColumn
hwTunnelFrrRouteDBTunnelInstance = _HwTunnelFrrRouteDBTunnelInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 4, 1, 2),
    _HwTunnelFrrRouteDBTunnelInstance_Type()
)
hwTunnelFrrRouteDBTunnelInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTunnelFrrRouteDBTunnelInstance.setStatus("current")
_HwTunnelFrrRouteDBTunnelIngressLSRId_Type = Unsigned32
_HwTunnelFrrRouteDBTunnelIngressLSRId_Object = MibTableColumn
hwTunnelFrrRouteDBTunnelIngressLSRId = _HwTunnelFrrRouteDBTunnelIngressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 4, 1, 3),
    _HwTunnelFrrRouteDBTunnelIngressLSRId_Type()
)
hwTunnelFrrRouteDBTunnelIngressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTunnelFrrRouteDBTunnelIngressLSRId.setStatus("current")
_HwTunnelFrrRouteDBTunnelEngressLSRId_Type = Unsigned32
_HwTunnelFrrRouteDBTunnelEngressLSRId_Object = MibTableColumn
hwTunnelFrrRouteDBTunnelEngressLSRId = _HwTunnelFrrRouteDBTunnelEngressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 4, 1, 4),
    _HwTunnelFrrRouteDBTunnelEngressLSRId_Type()
)
hwTunnelFrrRouteDBTunnelEngressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTunnelFrrRouteDBTunnelEngressLSRId.setStatus("current")
_HwTunnelFrrRouteDBBypassIfIndex_Type = Unsigned32
_HwTunnelFrrRouteDBBypassIfIndex_Object = MibTableColumn
hwTunnelFrrRouteDBBypassIfIndex = _HwTunnelFrrRouteDBBypassIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 4, 1, 5),
    _HwTunnelFrrRouteDBBypassIfIndex_Type()
)
hwTunnelFrrRouteDBBypassIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTunnelFrrRouteDBBypassIfIndex.setStatus("current")
_HwTunnelFrrRouteDBInnerLabel_Type = Unsigned32
_HwTunnelFrrRouteDBInnerLabel_Object = MibTableColumn
hwTunnelFrrRouteDBInnerLabel = _HwTunnelFrrRouteDBInnerLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 4, 1, 6),
    _HwTunnelFrrRouteDBInnerLabel_Type()
)
hwTunnelFrrRouteDBInnerLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTunnelFrrRouteDBInnerLabel.setStatus("current")
_HwStaticLspTable_Object = MibTable
hwStaticLspTable = _HwStaticLspTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 5)
)
if mibBuilder.loadTexts:
    hwStaticLspTable.setStatus("current")
_HwStaticLspEntry_Object = MibTableRow
hwStaticLspEntry = _HwStaticLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 5, 1)
)
hwStaticLspEntry.setIndexNames(
    (0, "HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspIndex"),
    (0, "HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspInSegmentIndex"),
    (0, "HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspOutSegmentIndex"),
)
if mibBuilder.loadTexts:
    hwStaticLspEntry.setStatus("current")
_HwStaticLspIndex_Type = MplsIndexType
_HwStaticLspIndex_Object = MibTableColumn
hwStaticLspIndex = _HwStaticLspIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 5, 1, 1),
    _HwStaticLspIndex_Type()
)
hwStaticLspIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwStaticLspIndex.setStatus("current")
_HwStaticLspInSegmentIndex_Type = MplsIndexType
_HwStaticLspInSegmentIndex_Object = MibTableColumn
hwStaticLspInSegmentIndex = _HwStaticLspInSegmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 5, 1, 2),
    _HwStaticLspInSegmentIndex_Type()
)
hwStaticLspInSegmentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwStaticLspInSegmentIndex.setStatus("current")
_HwStaticLspOutSegmentIndex_Type = MplsIndexType
_HwStaticLspOutSegmentIndex_Object = MibTableColumn
hwStaticLspOutSegmentIndex = _HwStaticLspOutSegmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 5, 1, 3),
    _HwStaticLspOutSegmentIndex_Type()
)
hwStaticLspOutSegmentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwStaticLspOutSegmentIndex.setStatus("current")


class _HwStaticLspOwner_Type(Integer32):
    """Custom type hwStaticLspOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crstatic", 2),
          ("other", 3),
          ("static", 1))
    )


_HwStaticLspOwner_Type.__name__ = "Integer32"
_HwStaticLspOwner_Object = MibTableColumn
hwStaticLspOwner = _HwStaticLspOwner_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 5, 1, 4),
    _HwStaticLspOwner_Type()
)
hwStaticLspOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaticLspOwner.setStatus("current")
_HwStaticLspName_Type = SnmpAdminString
_HwStaticLspName_Object = MibTableColumn
hwStaticLspName = _HwStaticLspName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 5, 1, 5),
    _HwStaticLspName_Type()
)
hwStaticLspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaticLspName.setStatus("current")


class _HwStaticLspStatus_Type(Integer32):
    """Custom type hwStaticLspStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_HwStaticLspStatus_Type.__name__ = "Integer32"
_HwStaticLspStatus_Object = MibTableColumn
hwStaticLspStatus = _HwStaticLspStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 5, 1, 6),
    _HwStaticLspStatus_Type()
)
hwStaticLspStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaticLspStatus.setStatus("current")


class _HwStaticLspClassType_Type(Integer32):
    """Custom type hwStaticLspClassType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ct0", 1),
          ("ct1", 2),
          ("ct2", 3),
          ("ct3", 4),
          ("ct4", 5),
          ("ct5", 6),
          ("ct6", 7),
          ("ct7", 8),
          ("none", 9))
    )


_HwStaticLspClassType_Type.__name__ = "Integer32"
_HwStaticLspClassType_Object = MibTableColumn
hwStaticLspClassType = _HwStaticLspClassType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 5, 1, 7),
    _HwStaticLspClassType_Type()
)
hwStaticLspClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaticLspClassType.setStatus("current")
_HwStaticLspBandwidth_Type = Unsigned32
_HwStaticLspBandwidth_Object = MibTableColumn
hwStaticLspBandwidth = _HwStaticLspBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 5, 1, 8),
    _HwStaticLspBandwidth_Type()
)
hwStaticLspBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaticLspBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwStaticLspBandwidth.setUnits("kilobits per second")
_HwMplsTeClassTable_Object = MibTable
hwMplsTeClassTable = _HwMplsTeClassTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 6)
)
if mibBuilder.loadTexts:
    hwMplsTeClassTable.setStatus("current")
_HwMplsTeClassEntry_Object = MibTableRow
hwMplsTeClassEntry = _HwMplsTeClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 6, 1)
)
hwMplsTeClassEntry.setIndexNames(
    (0, "HUAWEI-MPLS-EXTEND-MIB", "hwMplsTeClassId"),
)
if mibBuilder.loadTexts:
    hwMplsTeClassEntry.setStatus("current")
_HwMplsTeClassId_Type = Unsigned32
_HwMplsTeClassId_Object = MibTableColumn
hwMplsTeClassId = _HwMplsTeClassId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 6, 1, 1),
    _HwMplsTeClassId_Type()
)
hwMplsTeClassId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsTeClassId.setStatus("current")


class _HwMplsTeClassClassType_Type(Integer32):
    """Custom type hwMplsTeClassClassType based on Integer32"""
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
        *(("ct0", 1),
          ("ct1", 2),
          ("ct2", 3),
          ("ct3", 4),
          ("ct4", 5),
          ("ct5", 6),
          ("ct6", 7),
          ("ct7", 8))
    )


_HwMplsTeClassClassType_Type.__name__ = "Integer32"
_HwMplsTeClassClassType_Object = MibTableColumn
hwMplsTeClassClassType = _HwMplsTeClassClassType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 6, 1, 2),
    _HwMplsTeClassClassType_Type()
)
hwMplsTeClassClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTeClassClassType.setStatus("current")
_HwMplsTeClassPriority_Type = Unsigned32
_HwMplsTeClassPriority_Object = MibTableColumn
hwMplsTeClassPriority = _HwMplsTeClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 6, 1, 3),
    _HwMplsTeClassPriority_Type()
)
hwMplsTeClassPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTeClassPriority.setStatus("current")
_HwMplsTeClassDescription_Type = OctetString
_HwMplsTeClassDescription_Object = MibTableColumn
hwMplsTeClassDescription = _HwMplsTeClassDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 6, 1, 4),
    _HwMplsTeClassDescription_Type()
)
hwMplsTeClassDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTeClassDescription.setStatus("current")
_HwMplsIfBcTable_Object = MibTable
hwMplsIfBcTable = _HwMplsIfBcTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 7)
)
if mibBuilder.loadTexts:
    hwMplsIfBcTable.setStatus("current")
_HwMplsIfBcEntry_Object = MibTableRow
hwMplsIfBcEntry = _HwMplsIfBcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 7, 1)
)
hwMplsIfBcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hwMplsIfBcEntry.setStatus("current")
_HwMplsIfMaxResvBandwidth_Type = Unsigned32
_HwMplsIfMaxResvBandwidth_Object = MibTableColumn
hwMplsIfMaxResvBandwidth = _HwMplsIfMaxResvBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 7, 1, 1),
    _HwMplsIfMaxResvBandwidth_Type()
)
hwMplsIfMaxResvBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsIfMaxResvBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsIfMaxResvBandwidth.setUnits("kilobits per second")
_HwMplsIfBc0Bandwidth_Type = Unsigned32
_HwMplsIfBc0Bandwidth_Object = MibTableColumn
hwMplsIfBc0Bandwidth = _HwMplsIfBc0Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 7, 1, 2),
    _HwMplsIfBc0Bandwidth_Type()
)
hwMplsIfBc0Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsIfBc0Bandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsIfBc0Bandwidth.setUnits("kilobits per second")
_HwMplsIfBc1Bandwidth_Type = Unsigned32
_HwMplsIfBc1Bandwidth_Object = MibTableColumn
hwMplsIfBc1Bandwidth = _HwMplsIfBc1Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 7, 1, 3),
    _HwMplsIfBc1Bandwidth_Type()
)
hwMplsIfBc1Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsIfBc1Bandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsIfBc1Bandwidth.setUnits("kilobits per second")
_HwMplsIfBc2Bandwidth_Type = Unsigned32
_HwMplsIfBc2Bandwidth_Object = MibTableColumn
hwMplsIfBc2Bandwidth = _HwMplsIfBc2Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 7, 1, 4),
    _HwMplsIfBc2Bandwidth_Type()
)
hwMplsIfBc2Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsIfBc2Bandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsIfBc2Bandwidth.setUnits("kilobits per second")
_HwMplsIfBc3Bandwidth_Type = Unsigned32
_HwMplsIfBc3Bandwidth_Object = MibTableColumn
hwMplsIfBc3Bandwidth = _HwMplsIfBc3Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 7, 1, 5),
    _HwMplsIfBc3Bandwidth_Type()
)
hwMplsIfBc3Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsIfBc3Bandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsIfBc3Bandwidth.setUnits("kilobits per second")
_HwMplsIfBc4Bandwidth_Type = Unsigned32
_HwMplsIfBc4Bandwidth_Object = MibTableColumn
hwMplsIfBc4Bandwidth = _HwMplsIfBc4Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 7, 1, 6),
    _HwMplsIfBc4Bandwidth_Type()
)
hwMplsIfBc4Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsIfBc4Bandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsIfBc4Bandwidth.setUnits("kilobits per second")
_HwMplsIfBc5Bandwidth_Type = Unsigned32
_HwMplsIfBc5Bandwidth_Object = MibTableColumn
hwMplsIfBc5Bandwidth = _HwMplsIfBc5Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 7, 1, 7),
    _HwMplsIfBc5Bandwidth_Type()
)
hwMplsIfBc5Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsIfBc5Bandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsIfBc5Bandwidth.setUnits("kilobits per second")
_HwMplsIfBc6Bandwidth_Type = Unsigned32
_HwMplsIfBc6Bandwidth_Object = MibTableColumn
hwMplsIfBc6Bandwidth = _HwMplsIfBc6Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 7, 1, 8),
    _HwMplsIfBc6Bandwidth_Type()
)
hwMplsIfBc6Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsIfBc6Bandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsIfBc6Bandwidth.setUnits("kilobits per second")
_HwMplsIfBc7Bandwidth_Type = Unsigned32
_HwMplsIfBc7Bandwidth_Object = MibTableColumn
hwMplsIfBc7Bandwidth = _HwMplsIfBc7Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 7, 1, 9),
    _HwMplsIfBc7Bandwidth_Type()
)
hwMplsIfBc7Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsIfBc7Bandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsIfBc7Bandwidth.setUnits("kilobits per second")
_HwStaticLspTnlTable_Object = MibTable
hwStaticLspTnlTable = _HwStaticLspTnlTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 8)
)
if mibBuilder.loadTexts:
    hwStaticLspTnlTable.setStatus("current")
_HwStaticLspTnlEntry_Object = MibTableRow
hwStaticLspTnlEntry = _HwStaticLspTnlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 8, 1)
)
hwStaticLspTnlEntry.setIndexNames(
    (0, "HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspTnlName"),
)
if mibBuilder.loadTexts:
    hwStaticLspTnlEntry.setStatus("current")
_HwStaticLspTnlName_Type = SnmpAdminString
_HwStaticLspTnlName_Object = MibTableColumn
hwStaticLspTnlName = _HwStaticLspTnlName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 8, 1, 1),
    _HwStaticLspTnlName_Type()
)
hwStaticLspTnlName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwStaticLspTnlName.setStatus("current")
_HwStaticLspTnlToken_Type = Unsigned32
_HwStaticLspTnlToken_Object = MibTableColumn
hwStaticLspTnlToken = _HwStaticLspTnlToken_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 8, 1, 2),
    _HwStaticLspTnlToken_Type()
)
hwStaticLspTnlToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaticLspTnlToken.setStatus("current")
_HwMplsTeVpnQosTable_Object = MibTable
hwMplsTeVpnQosTable = _HwMplsTeVpnQosTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 9)
)
if mibBuilder.loadTexts:
    hwMplsTeVpnQosTable.setStatus("current")
_HwMplsTeVpnQosEntry_Object = MibTableRow
hwMplsTeVpnQosEntry = _HwMplsTeVpnQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 9, 1)
)
hwMplsTeVpnQosEntry.setIndexNames(
    (0, "HUAWEI-MPLS-EXTEND-MIB", "hwMplsTnlID"),
)
if mibBuilder.loadTexts:
    hwMplsTeVpnQosEntry.setStatus("current")
_HwMplsTnlID_Type = Unsigned32
_HwMplsTnlID_Object = MibTableColumn
hwMplsTnlID = _HwMplsTnlID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 9, 1, 1),
    _HwMplsTnlID_Type()
)
hwMplsTnlID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsTnlID.setStatus("current")
_HwMplsTeVpnMaxBandwidth_Type = Unsigned32
_HwMplsTeVpnMaxBandwidth_Object = MibTableColumn
hwMplsTeVpnMaxBandwidth = _HwMplsTeVpnMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 9, 1, 2),
    _HwMplsTeVpnMaxBandwidth_Type()
)
hwMplsTeVpnMaxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTeVpnMaxBandwidth.setStatus("current")
_HwMplsTeVpnAllocatedBandwidth_Type = Unsigned32
_HwMplsTeVpnAllocatedBandwidth_Object = MibTableColumn
hwMplsTeVpnAllocatedBandwidth = _HwMplsTeVpnAllocatedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 9, 1, 3),
    _HwMplsTeVpnAllocatedBandwidth_Type()
)
hwMplsTeVpnAllocatedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTeVpnAllocatedBandwidth.setStatus("current")
_HwStaticLspInIfIndex_Type = OctetString
_HwStaticLspInIfIndex_Object = MibScalar
hwStaticLspInIfIndex = _HwStaticLspInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 11),
    _HwStaticLspInIfIndex_Type()
)
hwStaticLspInIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStaticLspInIfIndex.setStatus("current")
_HwStaticLspInIfName_Type = OctetString
_HwStaticLspInIfName_Object = MibScalar
hwStaticLspInIfName = _HwStaticLspInIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 12),
    _HwStaticLspInIfName_Type()
)
hwStaticLspInIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStaticLspInIfName.setStatus("current")
_HwStaticLspDownReason_Type = Integer32
_HwStaticLspDownReason_Object = MibScalar
hwStaticLspDownReason = _HwStaticLspDownReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 13),
    _HwStaticLspDownReason_Type()
)
hwStaticLspDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStaticLspDownReason.setStatus("current")
_HwMplsTunnelStatisticsTable_Object = MibTable
hwMplsTunnelStatisticsTable = _HwMplsTunnelStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 14)
)
if mibBuilder.loadTexts:
    hwMplsTunnelStatisticsTable.setStatus("current")
_HwMplsTunnelStatisticsEntry_Object = MibTableRow
hwMplsTunnelStatisticsEntry = _HwMplsTunnelStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 14, 1)
)
hwMplsTunnelStatisticsEntry.setIndexNames(
    (0, "HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelStatisticsTunnelIndex"),
    (0, "HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelStatisticsIngressLSRId"),
    (0, "HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelStatisticsEgressLSRId"),
)
if mibBuilder.loadTexts:
    hwMplsTunnelStatisticsEntry.setStatus("current")
_HwMplsTunnelStatisticsTunnelIndex_Type = Unsigned32
_HwMplsTunnelStatisticsTunnelIndex_Object = MibTableColumn
hwMplsTunnelStatisticsTunnelIndex = _HwMplsTunnelStatisticsTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 14, 1, 1),
    _HwMplsTunnelStatisticsTunnelIndex_Type()
)
hwMplsTunnelStatisticsTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsTunnelStatisticsTunnelIndex.setStatus("current")
_HwMplsTunnelStatisticsIngressLSRId_Type = IpAddress
_HwMplsTunnelStatisticsIngressLSRId_Object = MibTableColumn
hwMplsTunnelStatisticsIngressLSRId = _HwMplsTunnelStatisticsIngressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 14, 1, 2),
    _HwMplsTunnelStatisticsIngressLSRId_Type()
)
hwMplsTunnelStatisticsIngressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsTunnelStatisticsIngressLSRId.setStatus("current")
_HwMplsTunnelStatisticsEgressLSRId_Type = IpAddress
_HwMplsTunnelStatisticsEgressLSRId_Object = MibTableColumn
hwMplsTunnelStatisticsEgressLSRId = _HwMplsTunnelStatisticsEgressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 14, 1, 3),
    _HwMplsTunnelStatisticsEgressLSRId_Type()
)
hwMplsTunnelStatisticsEgressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsTunnelStatisticsEgressLSRId.setStatus("current")
_HwMplsTunnelStatisticsHCInOctets_Type = Counter64
_HwMplsTunnelStatisticsHCInOctets_Object = MibTableColumn
hwMplsTunnelStatisticsHCInOctets = _HwMplsTunnelStatisticsHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 14, 1, 4),
    _HwMplsTunnelStatisticsHCInOctets_Type()
)
hwMplsTunnelStatisticsHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelStatisticsHCInOctets.setStatus("current")
_HwMplsTunnelStatisticsHCOutOctets_Type = Counter64
_HwMplsTunnelStatisticsHCOutOctets_Object = MibTableColumn
hwMplsTunnelStatisticsHCOutOctets = _HwMplsTunnelStatisticsHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 1, 14, 1, 5),
    _HwMplsTunnelStatisticsHCOutOctets_Type()
)
hwMplsTunnelStatisticsHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTunnelStatisticsHCOutOctets.setStatus("current")
_HwMplsExtendTrap_ObjectIdentity = ObjectIdentity
hwMplsExtendTrap = _HwMplsExtendTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2)
)
_HwLspTrap_ObjectIdentity = ObjectIdentity
hwLspTrap = _HwLspTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1)
)
_HwMplsTrapObjects_ObjectIdentity = ObjectIdentity
hwMplsTrapObjects = _HwMplsTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 2)
)
_HwMplsTunnelIfName_Type = SnmpAdminString
_HwMplsTunnelIfName_Object = MibScalar
hwMplsTunnelIfName = _HwMplsTunnelIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 2, 1),
    _HwMplsTunnelIfName_Type()
)
hwMplsTunnelIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsTunnelIfName.setStatus("obsolete")


class _HwMplsTunnelFrrConfigOper_Type(Integer32):
    """Custom type hwMplsTunnelFrrConfigOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config", 1),
          ("unconfig", 0),
          ("unknow", 2))
    )


_HwMplsTunnelFrrConfigOper_Type.__name__ = "Integer32"
_HwMplsTunnelFrrConfigOper_Object = MibScalar
hwMplsTunnelFrrConfigOper = _HwMplsTunnelFrrConfigOper_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 2, 2),
    _HwMplsTunnelFrrConfigOper_Type()
)
hwMplsTunnelFrrConfigOper.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsTunnelFrrConfigOper.setStatus("obsolete")


class _HwMplsTunnelDownReason_Type(Integer32):
    """Custom type hwMplsTunnelDownReason based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("bypassTunnelDownOrUnbinded", 8),
          ("clear", 100),
          ("cspfComputeFail", 9),
          ("mplsOamBdi", 23),
          ("mplsOamDOamFail", 27),
          ("mplsOamExcess", 19),
          ("mplsOamFdi", 24),
          ("mplsOamLocv", 18),
          ("mplsOamMisMatch", 20),
          ("mplsOamMisMerge", 21),
          ("mplsOamSD", 26),
          ("mplsOamSF", 25),
          ("mplsOamUnknown", 22),
          ("other", 1),
          ("outIfDown", 4),
          ("resourcePreempted", 5),
          ("rsvpMessageTimeout", 6),
          ("rsvpNeighborLost", 7),
          ("serviceDelete", 29),
          ("serviceResume", 28),
          ("staticCrlspDown", 3),
          ("staticLspDown", 2),
          ("tpoamAlarmIndicationSignal", 12),
          ("tpoamLossOfContinuity", 11),
          ("tpoamLossSF", 16),
          ("tpoamPeriod", 17),
          ("tpoamRemoteDefectIndication", 13),
          ("tpoamUnexpectedMEG", 14),
          ("tpoamUnexpectedMEP", 15),
          ("userShutdown", 10))
    )


_HwMplsTunnelDownReason_Type.__name__ = "Integer32"
_HwMplsTunnelDownReason_Object = MibScalar
hwMplsTunnelDownReason = _HwMplsTunnelDownReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 2, 3),
    _HwMplsTunnelDownReason_Type()
)
hwMplsTunnelDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsTunnelDownReason.setStatus("current")


class _HwMplsLspProtocol_Type(Integer32):
    """Custom type hwMplsLspProtocol based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 2),
          ("bgpEgress", 12),
          ("bgpIngress", 11),
          ("bgpv6", 3),
          ("bgpv6Egress", 14),
          ("bgpv6Ingress", 13),
          ("ldp", 1),
          ("ldpEgress", 10),
          ("ldpIngress", 8),
          ("ldpTransit", 9),
          ("ldpfrr", 4),
          ("privateNetBgp", 26),
          ("rsvp", 5),
          ("rsvpEgress", 17),
          ("rsvpIngress", 15),
          ("rsvpTransit", 16),
          ("totalCrLsp", 7),
          ("totalCrLspEgress", 23),
          ("totalCrLspIngress", 21),
          ("totalCrLspTransit", 22),
          ("totalLsp", 6),
          ("totalLspEgress", 20),
          ("totalLspIngress", 18),
          ("totalLspTransit", 19),
          ("totalPublicNetLspIngressTransit", 24),
          ("totalPublicNetLspTransitEgress", 25),
          ("unknown", 100))
    )


_HwMplsLspProtocol_Type.__name__ = "Integer32"
_HwMplsLspProtocol_Object = MibScalar
hwMplsLspProtocol = _HwMplsLspProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 2, 4),
    _HwMplsLspProtocol_Type()
)
hwMplsLspProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsLspProtocol.setStatus("current")
_HwMplsLspThreshold_Type = Integer32
_HwMplsLspThreshold_Object = MibScalar
hwMplsLspThreshold = _HwMplsLspThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 2, 5),
    _HwMplsLspThreshold_Type()
)
hwMplsLspThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsLspThreshold.setStatus("current")
_HwMplsLspTotalCount_Type = Integer32
_HwMplsLspTotalCount_Object = MibScalar
hwMplsLspTotalCount = _HwMplsLspTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 2, 6),
    _HwMplsLspTotalCount_Type()
)
hwMplsLspTotalCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsLspTotalCount.setStatus("current")
_HwMplsLspCurrentCount_Type = Integer32
_HwMplsLspCurrentCount_Object = MibScalar
hwMplsLspCurrentCount = _HwMplsLspCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 2, 7),
    _HwMplsLspCurrentCount_Type()
)
hwMplsLspCurrentCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsLspCurrentCount.setStatus("current")
_HwMplsTunnelDownLSRID_Type = MplsLsrIdentifier
_HwMplsTunnelDownLSRID_Object = MibScalar
hwMplsTunnelDownLSRID = _HwMplsTunnelDownLSRID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 2, 8),
    _HwMplsTunnelDownLSRID_Type()
)
hwMplsTunnelDownLSRID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsTunnelDownLSRID.setStatus("current")
_HwMplsTunnelDownIfIpAddr_Type = InetAddress
_HwMplsTunnelDownIfIpAddr_Object = MibScalar
hwMplsTunnelDownIfIpAddr = _HwMplsTunnelDownIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 2, 9),
    _HwMplsTunnelDownIfIpAddr_Type()
)
hwMplsTunnelDownIfIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsTunnelDownIfIpAddr.setStatus("current")
_HwMplsTunnelDownIfIpAddrType_Type = InetAddressType
_HwMplsTunnelDownIfIpAddrType_Object = MibScalar
hwMplsTunnelDownIfIpAddrType = _HwMplsTunnelDownIfIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 2, 10),
    _HwMplsTunnelDownIfIpAddrType_Type()
)
hwMplsTunnelDownIfIpAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsTunnelDownIfIpAddrType.setStatus("current")


class _HwMplsResourceType_Type(Integer32):
    """Custom type hwMplsResourceType based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("autoBypassTunnelIf", 1),
          ("autoPrimaryTunnelIf", 9),
          ("cspfLink", 12),
          ("cspfNlsa", 13),
          ("cspfNode", 11),
          ("cspfSrlg", 14),
          ("ldpBfd", 4),
          ("ldpTotalLocalAdjacency", 10),
          ("ldpTotalRemoteAdjacency", 7),
          ("mldpTotalBranch", 6),
          ("mldpTotalTree", 5),
          ("outSegment", 8),
          ("p2mpAutoTunnelIf", 2),
          ("teBfd", 3),
          ("unknown", 100))
    )


_HwMplsResourceType_Type.__name__ = "Integer32"
_HwMplsResourceType_Object = MibScalar
hwMplsResourceType = _HwMplsResourceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 2, 11),
    _HwMplsResourceType_Type()
)
hwMplsResourceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsResourceType.setStatus("current")
_HwMplsResourceCurrentCount_Type = Integer32
_HwMplsResourceCurrentCount_Object = MibScalar
hwMplsResourceCurrentCount = _HwMplsResourceCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 2, 12),
    _HwMplsResourceCurrentCount_Type()
)
hwMplsResourceCurrentCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsResourceCurrentCount.setStatus("current")
_HwMplsResourceThreshold_Type = Integer32
_HwMplsResourceThreshold_Object = MibScalar
hwMplsResourceThreshold = _HwMplsResourceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 2, 13),
    _HwMplsResourceThreshold_Type()
)
hwMplsResourceThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsResourceThreshold.setStatus("current")
_HwMplsResourceTotalCount_Type = Integer32
_HwMplsResourceTotalCount_Object = MibScalar
hwMplsResourceTotalCount = _HwMplsResourceTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 2, 14),
    _HwMplsResourceTotalCount_Type()
)
hwMplsResourceTotalCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsResourceTotalCount.setStatus("current")
_HwMplsSessionTunnelId_Type = Integer32
_HwMplsSessionTunnelId_Object = MibScalar
hwMplsSessionTunnelId = _HwMplsSessionTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 2, 15),
    _HwMplsSessionTunnelId_Type()
)
hwMplsSessionTunnelId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsSessionTunnelId.setStatus("current")
_HwMplsLocalLspId_Type = Integer32
_HwMplsLocalLspId_Object = MibScalar
hwMplsLocalLspId = _HwMplsLocalLspId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 2, 16),
    _HwMplsLocalLspId_Type()
)
hwMplsLocalLspId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsLocalLspId.setStatus("current")
_HwMplsIngressLsrId_Type = MplsLsrIdentifier
_HwMplsIngressLsrId_Object = MibScalar
hwMplsIngressLsrId = _HwMplsIngressLsrId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 2, 17),
    _HwMplsIngressLsrId_Type()
)
hwMplsIngressLsrId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsIngressLsrId.setStatus("current")
_HwMplsEgressLsrId_Type = MplsLsrIdentifier
_HwMplsEgressLsrId_Object = MibScalar
hwMplsEgressLsrId = _HwMplsEgressLsrId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 2, 18),
    _HwMplsEgressLsrId_Type()
)
hwMplsEgressLsrId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsEgressLsrId.setStatus("current")
_HwMplsLspName_Type = SnmpAdminString
_HwMplsLspName_Object = MibScalar
hwMplsLspName = _HwMplsLspName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 2, 19),
    _HwMplsLspName_Type()
)
hwMplsLspName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsLspName.setStatus("current")
_HwMplsGlobalObject_ObjectIdentity = ObjectIdentity
hwMplsGlobalObject = _HwMplsGlobalObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 3)
)


class _HwMplsGlobalWorkMode_Type(Integer32):
    """Custom type hwMplsGlobalWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonstandard", 2),
          ("standard", 1))
    )


_HwMplsGlobalWorkMode_Type.__name__ = "Integer32"
_HwMplsGlobalWorkMode_Object = MibScalar
hwMplsGlobalWorkMode = _HwMplsGlobalWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 3, 1),
    _HwMplsGlobalWorkMode_Type()
)
hwMplsGlobalWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsGlobalWorkMode.setStatus("current")


class _HwMplsGlobalBcModel_Type(Integer32):
    """Custom type hwMplsGlobalBcModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("extendMam", 3),
          ("mam", 2),
          ("rdm", 1))
    )


_HwMplsGlobalBcModel_Type.__name__ = "Integer32"
_HwMplsGlobalBcModel_Object = MibScalar
hwMplsGlobalBcModel = _HwMplsGlobalBcModel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 3, 2),
    _HwMplsGlobalBcModel_Type()
)
hwMplsGlobalBcModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsGlobalBcModel.setStatus("current")
_HwMplsDynamicLabelTotalCount_Type = Unsigned32
_HwMplsDynamicLabelTotalCount_Object = MibScalar
hwMplsDynamicLabelTotalCount = _HwMplsDynamicLabelTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 3, 3),
    _HwMplsDynamicLabelTotalCount_Type()
)
hwMplsDynamicLabelTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsDynamicLabelTotalCount.setStatus("current")
_HwMplsDynamicLabelCurrentCount_Type = Unsigned32
_HwMplsDynamicLabelCurrentCount_Object = MibScalar
hwMplsDynamicLabelCurrentCount = _HwMplsDynamicLabelCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 3, 4),
    _HwMplsDynamicLabelCurrentCount_Type()
)
hwMplsDynamicLabelCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsDynamicLabelCurrentCount.setStatus("current")
_HwMplsDynamicLabelThresholdUpperLimit_Type = Unsigned32
_HwMplsDynamicLabelThresholdUpperLimit_Object = MibScalar
hwMplsDynamicLabelThresholdUpperLimit = _HwMplsDynamicLabelThresholdUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 3, 5),
    _HwMplsDynamicLabelThresholdUpperLimit_Type()
)
hwMplsDynamicLabelThresholdUpperLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsDynamicLabelThresholdUpperLimit.setStatus("current")
_HwMplsDynamicLabelThresholdLowerLimit_Type = Unsigned32
_HwMplsDynamicLabelThresholdLowerLimit_Object = MibScalar
hwMplsDynamicLabelThresholdLowerLimit = _HwMplsDynamicLabelThresholdLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 3, 6),
    _HwMplsDynamicLabelThresholdLowerLimit_Type()
)
hwMplsDynamicLabelThresholdLowerLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsDynamicLabelThresholdLowerLimit.setStatus("current")
_HwMplsLspStatistics_ObjectIdentity = ObjectIdentity
hwMplsLspStatistics = _HwMplsLspStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 4)
)
_HwMplsLspStatisticsTable_Object = MibTable
hwMplsLspStatisticsTable = _HwMplsLspStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 4, 1)
)
if mibBuilder.loadTexts:
    hwMplsLspStatisticsTable.setStatus("current")
_HwMplsLspStatisticsEntry_Object = MibTableRow
hwMplsLspStatisticsEntry = _HwMplsLspStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 4, 1, 1)
)
hwMplsLspStatisticsEntry.setIndexNames(
    (0, "HUAWEI-MPLS-EXTEND-MIB", "hwMplsLspStatisticsLspType"),
)
if mibBuilder.loadTexts:
    hwMplsLspStatisticsEntry.setStatus("current")


class _HwMplsLspStatisticsLspType_Type(Integer32):
    """Custom type hwMplsLspStatisticsLspType based on Integer32"""
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
        *(("asbrLsp", 6),
          ("bgpIpv6Lsp", 7),
          ("bgpLsp", 5),
          ("l3vpnIpv6Lsp", 8),
          ("ldpLsp", 3),
          ("rsvpCrLsp", 4),
          ("staticCrLsp", 2),
          ("staticLsp", 1))
    )


_HwMplsLspStatisticsLspType_Type.__name__ = "Integer32"
_HwMplsLspStatisticsLspType_Object = MibTableColumn
hwMplsLspStatisticsLspType = _HwMplsLspStatisticsLspType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 4, 1, 1, 1),
    _HwMplsLspStatisticsLspType_Type()
)
hwMplsLspStatisticsLspType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsLspStatisticsLspType.setStatus("current")
_HwMplsLspStatisticsIngressLspCount_Type = Unsigned32
_HwMplsLspStatisticsIngressLspCount_Object = MibTableColumn
hwMplsLspStatisticsIngressLspCount = _HwMplsLspStatisticsIngressLspCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 4, 1, 1, 2),
    _HwMplsLspStatisticsIngressLspCount_Type()
)
hwMplsLspStatisticsIngressLspCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLspStatisticsIngressLspCount.setStatus("current")
_HwMplsLspStatisticsTransitLspCount_Type = Unsigned32
_HwMplsLspStatisticsTransitLspCount_Object = MibTableColumn
hwMplsLspStatisticsTransitLspCount = _HwMplsLspStatisticsTransitLspCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 4, 1, 1, 3),
    _HwMplsLspStatisticsTransitLspCount_Type()
)
hwMplsLspStatisticsTransitLspCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLspStatisticsTransitLspCount.setStatus("current")
_HwMplsLspStatisticsEgressLspCount_Type = Unsigned32
_HwMplsLspStatisticsEgressLspCount_Object = MibTableColumn
hwMplsLspStatisticsEgressLspCount = _HwMplsLspStatisticsEgressLspCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 4, 1, 1, 4),
    _HwMplsLspStatisticsEgressLspCount_Type()
)
hwMplsLspStatisticsEgressLspCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLspStatisticsEgressLspCount.setStatus("current")
_HwMplsLspStatisticsTotalLspCount_Type = Unsigned32
_HwMplsLspStatisticsTotalLspCount_Object = MibTableColumn
hwMplsLspStatisticsTotalLspCount = _HwMplsLspStatisticsTotalLspCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 4, 1, 1, 5),
    _HwMplsLspStatisticsTotalLspCount_Type()
)
hwMplsLspStatisticsTotalLspCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLspStatisticsTotalLspCount.setStatus("current")
_HwMplsTrafficStatisticsStaticLspTable_Object = MibTable
hwMplsTrafficStatisticsStaticLspTable = _HwMplsTrafficStatisticsStaticLspTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 4, 2)
)
if mibBuilder.loadTexts:
    hwMplsTrafficStatisticsStaticLspTable.setStatus("current")
_HwMplsTrafficStatisticsStaticLspEntry_Object = MibTableRow
hwMplsTrafficStatisticsStaticLspEntry = _HwMplsTrafficStatisticsStaticLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 4, 2, 1)
)
hwMplsTrafficStatisticsStaticLspEntry.setIndexNames(
    (0, "HUAWEI-MPLS-EXTEND-MIB", "hwMplsTrafficStatisticsStaticLspName"),
)
if mibBuilder.loadTexts:
    hwMplsTrafficStatisticsStaticLspEntry.setStatus("current")
_HwMplsTrafficStatisticsStaticLspName_Type = SnmpAdminString
_HwMplsTrafficStatisticsStaticLspName_Object = MibTableColumn
hwMplsTrafficStatisticsStaticLspName = _HwMplsTrafficStatisticsStaticLspName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 4, 2, 1, 1),
    _HwMplsTrafficStatisticsStaticLspName_Type()
)
hwMplsTrafficStatisticsStaticLspName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsTrafficStatisticsStaticLspName.setStatus("current")
_HwMplsTrafficStatisticsStaticLspForwardInBytes_Type = Counter64
_HwMplsTrafficStatisticsStaticLspForwardInBytes_Object = MibTableColumn
hwMplsTrafficStatisticsStaticLspForwardInBytes = _HwMplsTrafficStatisticsStaticLspForwardInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 4, 2, 1, 2),
    _HwMplsTrafficStatisticsStaticLspForwardInBytes_Type()
)
hwMplsTrafficStatisticsStaticLspForwardInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTrafficStatisticsStaticLspForwardInBytes.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsTrafficStatisticsStaticLspForwardInBytes.setUnits("bytes")
_HwMplsTrafficStatisticsStaticLspForwardInPackets_Type = Counter64
_HwMplsTrafficStatisticsStaticLspForwardInPackets_Object = MibTableColumn
hwMplsTrafficStatisticsStaticLspForwardInPackets = _HwMplsTrafficStatisticsStaticLspForwardInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 4, 2, 1, 3),
    _HwMplsTrafficStatisticsStaticLspForwardInPackets_Type()
)
hwMplsTrafficStatisticsStaticLspForwardInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTrafficStatisticsStaticLspForwardInPackets.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsTrafficStatisticsStaticLspForwardInPackets.setUnits("packets")
_HwMplsTrafficStatisticsStaticLspForwardOutBytes_Type = Counter64
_HwMplsTrafficStatisticsStaticLspForwardOutBytes_Object = MibTableColumn
hwMplsTrafficStatisticsStaticLspForwardOutBytes = _HwMplsTrafficStatisticsStaticLspForwardOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 4, 2, 1, 4),
    _HwMplsTrafficStatisticsStaticLspForwardOutBytes_Type()
)
hwMplsTrafficStatisticsStaticLspForwardOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTrafficStatisticsStaticLspForwardOutBytes.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsTrafficStatisticsStaticLspForwardOutBytes.setUnits("bytes")
_HwMplsTrafficStatisticsStaticLspForwardOutPackets_Type = Counter64
_HwMplsTrafficStatisticsStaticLspForwardOutPackets_Object = MibTableColumn
hwMplsTrafficStatisticsStaticLspForwardOutPackets = _HwMplsTrafficStatisticsStaticLspForwardOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 4, 2, 1, 5),
    _HwMplsTrafficStatisticsStaticLspForwardOutPackets_Type()
)
hwMplsTrafficStatisticsStaticLspForwardOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTrafficStatisticsStaticLspForwardOutPackets.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsTrafficStatisticsStaticLspForwardOutPackets.setUnits("packets")
_HwMplsTrafficStatisticsStaticLspBackwardInBytes_Type = Counter64
_HwMplsTrafficStatisticsStaticLspBackwardInBytes_Object = MibTableColumn
hwMplsTrafficStatisticsStaticLspBackwardInBytes = _HwMplsTrafficStatisticsStaticLspBackwardInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 4, 2, 1, 6),
    _HwMplsTrafficStatisticsStaticLspBackwardInBytes_Type()
)
hwMplsTrafficStatisticsStaticLspBackwardInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTrafficStatisticsStaticLspBackwardInBytes.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsTrafficStatisticsStaticLspBackwardInBytes.setUnits("bytes")
_HwMplsTrafficStatisticsStaticLspBackwardInPackets_Type = Counter64
_HwMplsTrafficStatisticsStaticLspBackwardInPackets_Object = MibTableColumn
hwMplsTrafficStatisticsStaticLspBackwardInPackets = _HwMplsTrafficStatisticsStaticLspBackwardInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 4, 2, 1, 7),
    _HwMplsTrafficStatisticsStaticLspBackwardInPackets_Type()
)
hwMplsTrafficStatisticsStaticLspBackwardInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTrafficStatisticsStaticLspBackwardInPackets.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsTrafficStatisticsStaticLspBackwardInPackets.setUnits("packets")
_HwMplsTrafficStatisticsStaticLspBackwardOutBytes_Type = Counter64
_HwMplsTrafficStatisticsStaticLspBackwardOutBytes_Object = MibTableColumn
hwMplsTrafficStatisticsStaticLspBackwardOutBytes = _HwMplsTrafficStatisticsStaticLspBackwardOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 4, 2, 1, 8),
    _HwMplsTrafficStatisticsStaticLspBackwardOutBytes_Type()
)
hwMplsTrafficStatisticsStaticLspBackwardOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTrafficStatisticsStaticLspBackwardOutBytes.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsTrafficStatisticsStaticLspBackwardOutBytes.setUnits("bytes")
_HwMplsTrafficStatisticsStaticLspBackwardOutPackets_Type = Counter64
_HwMplsTrafficStatisticsStaticLspBackwardOutPackets_Object = MibTableColumn
hwMplsTrafficStatisticsStaticLspBackwardOutPackets = _HwMplsTrafficStatisticsStaticLspBackwardOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 4, 2, 1, 9),
    _HwMplsTrafficStatisticsStaticLspBackwardOutPackets_Type()
)
hwMplsTrafficStatisticsStaticLspBackwardOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsTrafficStatisticsStaticLspBackwardOutPackets.setStatus("current")
if mibBuilder.loadTexts:
    hwMplsTrafficStatisticsStaticLspBackwardOutPackets.setUnits("packets")
_HwMplsExtendConformance_ObjectIdentity = ObjectIdentity
hwMplsExtendConformance = _HwMplsExtendConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 6)
)
_HwMplsExtendGroups_ObjectIdentity = ObjectIdentity
hwMplsExtendGroups = _HwMplsExtendGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 6, 1)
)
_HwMplsExtendCompliances_ObjectIdentity = ObjectIdentity
hwMplsExtendCompliances = _HwMplsExtendCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 6, 2)
)
_HwMplsRingMib_ObjectIdentity = ObjectIdentity
hwMplsRingMib = _HwMplsRingMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7)
)
_HwMplsRingTable_Object = MibTable
hwMplsRingTable = _HwMplsRingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 1)
)
if mibBuilder.loadTexts:
    hwMplsRingTable.setStatus("current")
_HwMplsRingEntry_Object = MibTableRow
hwMplsRingEntry = _HwMplsRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 1, 1)
)
hwMplsRingEntry.setIndexNames(
    (0, "HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingID"),
)
if mibBuilder.loadTexts:
    hwMplsRingEntry.setStatus("current")
_HwMplsRingID_Type = Unsigned32
_HwMplsRingID_Object = MibTableColumn
hwMplsRingID = _HwMplsRingID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 1, 1, 1),
    _HwMplsRingID_Type()
)
hwMplsRingID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsRingID.setStatus("current")
_HwMplsRingNodeID_Type = Unsigned32
_HwMplsRingNodeID_Object = MibTableColumn
hwMplsRingNodeID = _HwMplsRingNodeID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 1, 1, 2),
    _HwMplsRingNodeID_Type()
)
hwMplsRingNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsRingNodeID.setStatus("current")
_HwMplsRingName_Type = OctetString
_HwMplsRingName_Object = MibTableColumn
hwMplsRingName = _HwMplsRingName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 1, 1, 3),
    _HwMplsRingName_Type()
)
hwMplsRingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsRingName.setStatus("current")
_HwMplsRingDirection_Type = OctetString
_HwMplsRingDirection_Object = MibTableColumn
hwMplsRingDirection = _HwMplsRingDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 1, 1, 4),
    _HwMplsRingDirection_Type()
)
hwMplsRingDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsRingDirection.setStatus("current")
_HwMplsRingSwitchReason_Type = OctetString
_HwMplsRingSwitchReason_Object = MibTableColumn
hwMplsRingSwitchReason = _HwMplsRingSwitchReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 1, 1, 5),
    _HwMplsRingSwitchReason_Type()
)
hwMplsRingSwitchReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsRingSwitchReason.setStatus("current")
_HwMplsRingTrap_ObjectIdentity = ObjectIdentity
hwMplsRingTrap = _HwMplsRingTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2)
)

# Managed Objects groups

hwMplsTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 6, 1, 1)
)
hwMplsTunnelGroup.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwTunnelFrrRouteDBInnerLabel"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwTunnelFrrRouteDBBypassIfIndex"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwTunnelFrrARHopProtActual"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwTunnelFrrARHopProtDesired"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwTunnelFrrBypassProtIfIndex"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspOwner"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelClassType"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSessionAttr"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelFrrARHopTableIndex"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelIfIndex"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelPreBandwidth"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelNextBandwidth"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelFrrSwitchover"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelFrrBandwidth"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelOperStatus"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelAdminStatus"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelBandwidth"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTeVpnMaxBandwidth"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTeVpnAllocatedBandwidth"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelFrrHoldingPrio"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelFrrSetupPrio"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelFrrBypassTableIndex"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelLspType"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelType"))
)
if mibBuilder.loadTexts:
    hwMplsTunnelGroup.setStatus("current")

hwStaticLspGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 6, 1, 2)
)
hwStaticLspGroup.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspStatus"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspTnlToken"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspInIfIndex"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspInIfName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspDownReason"))
)
if mibBuilder.loadTexts:
    hwStaticLspGroup.setStatus("current")

hwMplsDsTeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 6, 1, 3)
)
hwMplsDsTeGroup.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelCt0Bandwidth"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelCt1Bandwidth"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelCt2Bandwidth"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelCt3Bandwidth"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelCt4Bandwidth"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelCt5Bandwidth"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelCt6Bandwidth"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelCt7Bandwidth"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspClassType"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspBandwidth"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTeClassClassType"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTeClassPriority"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTeClassDescription"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsGlobalBcModel"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsGlobalWorkMode"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsIfBc7Bandwidth"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsIfBc6Bandwidth"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsIfBc5Bandwidth"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsIfBc4Bandwidth"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsIfBc3Bandwidth"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsIfBc2Bandwidth"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsIfBc1Bandwidth"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsIfBc0Bandwidth"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsIfMaxResvBandwidth"))
)
if mibBuilder.loadTexts:
    hwMplsDsTeGroup.setStatus("current")

hwMplsLspStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 6, 1, 4)
)
hwMplsLspStatisticsGroup.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLspStatisticsIngressLspCount"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLspStatisticsTransitLspCount"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLspStatisticsEgressLspCount"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLspStatisticsTotalLspCount"))
)
if mibBuilder.loadTexts:
    hwMplsLspStatisticsGroup.setStatus("current")

hwMplsObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 6, 1, 5)
)
hwMplsObsoleteGroup.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelIfName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelFrrConfigOper"))
)
if mibBuilder.loadTexts:
    hwMplsObsoleteGroup.setStatus("obsolete")

hwMplsTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 6, 1, 6)
)
hwMplsTrapGroup.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDownReason"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDownLSRID"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDownIfIpAddrType"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDownIfIpAddr"))
)
if mibBuilder.loadTexts:
    hwMplsTrapGroup.setStatus("current")

hwMplsRingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 6, 1, 7)
)
hwMplsRingGroup.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingNodeID"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingDirection"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingSwitchReason"))
)
if mibBuilder.loadTexts:
    hwMplsRingGroup.setStatus("current")

hwMplsGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 6, 1, 8)
)
hwMplsGlobalGroup.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsDynamicLabelTotalCount"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsDynamicLabelCurrentCount"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsDynamicLabelThresholdUpperLimit"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsDynamicLabelThresholdLowerLimit"))
)
if mibBuilder.loadTexts:
    hwMplsGlobalGroup.setStatus("current")

hwMplsLspGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 6, 1, 9)
)
hwMplsLspGroup.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLspCurrentCount"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLspTotalCount"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLspProtocol"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLspThreshold"))
)
if mibBuilder.loadTexts:
    hwMplsLspGroup.setStatus("current")

hwMplsLspTrafficStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 6, 1, 10)
)
hwMplsLspTrafficStatisticGroup.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTrafficStatisticsStaticLspForwardInBytes"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTrafficStatisticsStaticLspForwardInPackets"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTrafficStatisticsStaticLspForwardOutBytes"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTrafficStatisticsStaticLspForwardOutPackets"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTrafficStatisticsStaticLspBackwardInBytes"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTrafficStatisticsStaticLspBackwardInPackets"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTrafficStatisticsStaticLspBackwardOutBytes"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTrafficStatisticsStaticLspBackwardOutPackets"))
)
if mibBuilder.loadTexts:
    hwMplsLspTrafficStatisticGroup.setStatus("current")

hwMplsResourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 6, 1, 11)
)
hwMplsResourceGroup.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsResourceType"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsResourceCurrentCount"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsResourceThreshold"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsResourceTotalCount"))
)
if mibBuilder.loadTexts:
    hwMplsResourceGroup.setStatus("current")


# Notification objects

hwMplsStaticLspUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 1)
)
hwMplsStaticLspUp.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspStatus"),
        ("IF-MIB", "ifName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspInIfIndex"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspInIfName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspDownReason"))
)
if mibBuilder.loadTexts:
    hwMplsStaticLspUp.setStatus(
        "current"
    )

hwMplsStaticLspDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 2)
)
hwMplsStaticLspDown.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspStatus"),
        ("IF-MIB", "ifName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspInIfIndex"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspInIfName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspDownReason"))
)
if mibBuilder.loadTexts:
    hwMplsStaticLspDown.setStatus(
        "current"
    )

hwMplsStaticCRLspUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 3)
)
hwMplsStaticCRLspUp.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspStatus"),
        ("IF-MIB", "ifName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspInIfIndex"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspInIfName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspDownReason"))
)
if mibBuilder.loadTexts:
    hwMplsStaticCRLspUp.setStatus(
        "current"
    )

hwMplsStaticCRLspDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 4)
)
hwMplsStaticCRLspDown.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspStatus"),
        ("IF-MIB", "ifName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspInIfIndex"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspInIfName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwStaticLspDownReason"))
)
if mibBuilder.loadTexts:
    hwMplsStaticCRLspDown.setStatus(
        "current"
    )

hwMplsTeFrrProtAval = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 5)
)
hwMplsTeFrrProtAval.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwTunnelFrrRouteDBBypassIfIndex"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwTunnelFrrRouteDBInnerLabel"))
)
if mibBuilder.loadTexts:
    hwMplsTeFrrProtAval.setStatus(
        "current"
    )

hwMplsTeFrrProtNotAval = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 6)
)
hwMplsTeFrrProtNotAval.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwTunnelFrrRouteDBBypassIfIndex")
)
if mibBuilder.loadTexts:
    hwMplsTeFrrProtNotAval.setStatus(
        "current"
    )

hwMplsTeFrrSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 7)
)
hwMplsTeFrrSwitch.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelAdminStatus"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelOperStatus"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsSessionTunnelId"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLocalLspId"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsIngressLsrId"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsEgressLsrId"))
)
if mibBuilder.loadTexts:
    hwMplsTeFrrSwitch.setStatus(
        "current"
    )

hwMplsTeFrrResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 8)
)
hwMplsTeFrrResume.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelAdminStatus"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelOperStatus"))
)
if mibBuilder.loadTexts:
    hwMplsTeFrrResume.setStatus(
        "current"
    )

hwMplsTunnelHSBSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 9)
)
hwMplsTunnelHSBSwitch.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelAdminStatus"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelOperStatus"))
)
if mibBuilder.loadTexts:
    hwMplsTunnelHSBSwitch.setStatus(
        "current"
    )

hwMplsTunnelHSBResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 10)
)
hwMplsTunnelHSBResume.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelAdminStatus"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelOperStatus"))
)
if mibBuilder.loadTexts:
    hwMplsTunnelHSBResume.setStatus(
        "current"
    )

hwMplsTunnelOBSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 11)
)
hwMplsTunnelOBSwitch.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelAdminStatus"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelOperStatus"))
)
if mibBuilder.loadTexts:
    hwMplsTunnelOBSwitch.setStatus(
        "current"
    )

hwMplsTunnelOBResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 12)
)
hwMplsTunnelOBResume.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelAdminStatus"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelOperStatus"))
)
if mibBuilder.loadTexts:
    hwMplsTunnelOBResume.setStatus(
        "current"
    )

hwMplsTunnelUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 13)
)
hwMplsTunnelUp.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelAdminStatus"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelOperStatus"))
)
if mibBuilder.loadTexts:
    hwMplsTunnelUp.setStatus(
        "obsolete"
    )

hwMplsTunnelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 14)
)
hwMplsTunnelDown.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelAdminStatus"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelOperStatus"))
)
if mibBuilder.loadTexts:
    hwMplsTunnelDown.setStatus(
        "obsolete"
    )

hwMplsTunnelChangeBw = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 15)
)
hwMplsTunnelChangeBw.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelIfIndex"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelPreBandwidth"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelNextBandwidth"))
)
if mibBuilder.loadTexts:
    hwMplsTunnelChangeBw.setStatus(
        "current"
    )

hwMplsTunnelTpOamLossSD = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 16)
)
hwMplsTunnelTpOamLossSD.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsTunnelTpOamLossSD.setStatus(
        "current"
    )

hwMplsOamSDRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 17)
)
hwMplsOamSDRecovery.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamSDRecovery.setStatus(
        "current"
    )

hwMplsOamLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 18)
)
hwMplsOamLoss.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwMplsOamLoss.setStatus(
        "current"
    )

hwMplsOamLossRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 19)
)
hwMplsOamLossRecovery.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamLossRecovery.setStatus(
        "current"
    )

hwMplsOamAis = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 20)
)
hwMplsOamAis.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamAis.setStatus(
        "current"
    )

hwMplsOamAisRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 21)
)
hwMplsOamAisRecovery.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamAisRecovery.setStatus(
        "current"
    )

hwMplsOamRdi = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 22)
)
hwMplsOamRdi.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwMplsOamRdi.setStatus(
        "current"
    )

hwMplsOamRdiRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 23)
)
hwMplsOamRdiRecovery.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamRdiRecovery.setStatus(
        "current"
    )

hwMplsOamMeg = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 24)
)
hwMplsOamMeg.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamMeg.setStatus(
        "current"
    )

hwMplsOamMegRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 25)
)
hwMplsOamMegRecovery.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamMegRecovery.setStatus(
        "current"
    )

hwMplsOamMep = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 26)
)
hwMplsOamMep.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamMep.setStatus(
        "current"
    )

hwMplsOamMepRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 27)
)
hwMplsOamMepRecovery.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamMepRecovery.setStatus(
        "current"
    )

hwMplsOamSF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 28)
)
hwMplsOamSF.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamSF.setStatus(
        "current"
    )

hwMplsOamSFRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 29)
)
hwMplsOamSFRecovery.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamSFRecovery.setStatus(
        "current"
    )

hwMplsOamPeriod = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 30)
)
hwMplsOamPeriod.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamPeriod.setStatus(
        "current"
    )

hwMplsOamPeriodRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 31)
)
hwMplsOamPeriodRecovery.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamPeriodRecovery.setStatus(
        "current"
    )

hwMplsOamLck = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 32)
)
hwMplsOamLck.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamLck.setStatus(
        "current"
    )

hwMplsOamLckRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 33)
)
hwMplsOamLckRecovery.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamLckRecovery.setStatus(
        "current"
    )

hwMplsOamExcess = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 34)
)
hwMplsOamExcess.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamExcess.setStatus(
        "current"
    )

hwMplsOamExcessRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 35)
)
hwMplsOamExcessRecovery.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamExcessRecovery.setStatus(
        "current"
    )

hwMplsOamMisMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 36)
)
hwMplsOamMisMatch.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamMisMatch.setStatus(
        "current"
    )

hwMplsOamMisMatchRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 37)
)
hwMplsOamMisMatchRecovery.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamMisMatchRecovery.setStatus(
        "current"
    )

hwMplsOamMisMerge = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 38)
)
hwMplsOamMisMerge.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamMisMerge.setStatus(
        "current"
    )

hwMplsOamMisMergeRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 39)
)
hwMplsOamMisMergeRecovery.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamMisMergeRecovery.setStatus(
        "current"
    )

hwMplsOamUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 40)
)
hwMplsOamUnknown.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamUnknown.setStatus(
        "current"
    )

hwMplsOamUnknownRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 41)
)
hwMplsOamUnknownRecovery.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamUnknownRecovery.setStatus(
        "current"
    )

hwMplsOamBDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 42)
)
hwMplsOamBDI.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwMplsOamBDI.setStatus(
        "current"
    )

hwMplsOamBDIRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 43)
)
hwMplsOamBDIRecovery.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamBDIRecovery.setStatus(
        "current"
    )

hwMplsOamFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 44)
)
hwMplsOamFail.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwMplsOamFail.setStatus(
        "current"
    )

hwMplsOamFailRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 45)
)
hwMplsOamFailRecovery.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamFailRecovery.setStatus(
        "current"
    )

hwMplsTunnelPrimaryUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 46)
)
hwMplsTunnelPrimaryUp.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName")
)
if mibBuilder.loadTexts:
    hwMplsTunnelPrimaryUp.setStatus(
        "current"
    )

hwMplsTunnelPrimaryDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 47)
)
hwMplsTunnelPrimaryDown.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDownReason"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDownLSRID"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDownIfIpAddrType"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDownIfIpAddr"))
)
if mibBuilder.loadTexts:
    hwMplsTunnelPrimaryDown.setStatus(
        "current"
    )

hwMplsTunnelHotstandbyUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 48)
)
hwMplsTunnelHotstandbyUp.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName")
)
if mibBuilder.loadTexts:
    hwMplsTunnelHotstandbyUp.setStatus(
        "current"
    )

hwMplsTunnelHotstandbyDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 49)
)
hwMplsTunnelHotstandbyDown.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDownReason"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDownLSRID"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDownIfIpAddrType"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDownIfIpAddr"))
)
if mibBuilder.loadTexts:
    hwMplsTunnelHotstandbyDown.setStatus(
        "current"
    )

hwMplsTunnelOrdinaryUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 50)
)
hwMplsTunnelOrdinaryUp.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName")
)
if mibBuilder.loadTexts:
    hwMplsTunnelOrdinaryUp.setStatus(
        "current"
    )

hwMplsTunnelOrdinaryDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 51)
)
hwMplsTunnelOrdinaryDown.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDownReason"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDownLSRID"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDownIfIpAddrType"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDownIfIpAddr"))
)
if mibBuilder.loadTexts:
    hwMplsTunnelOrdinaryDown.setStatus(
        "current"
    )

hwMplsTunnelBesteffortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 52)
)
hwMplsTunnelBesteffortUp.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName")
)
if mibBuilder.loadTexts:
    hwMplsTunnelBesteffortUp.setStatus(
        "current"
    )

hwMplsTunnelBesteffortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 53)
)
hwMplsTunnelBesteffortDown.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDownReason"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDownLSRID"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDownIfIpAddrType"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDownIfIpAddr"))
)
if mibBuilder.loadTexts:
    hwMplsTunnelBesteffortDown.setStatus(
        "current"
    )

hwMplsTeAutoTunnelDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 54)
)
hwMplsTeAutoTunnelDownClear.setObjects(
      *(("MPLS-TE-STD-MIB", "mplsTunnelAdminStatus"),
        ("MPLS-TE-STD-MIB", "mplsTunnelOperStatus"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelIfName"))
)
if mibBuilder.loadTexts:
    hwMplsTeAutoTunnelDownClear.setStatus(
        "current"
    )

hwMplsTeAutoTunnelPrimaryDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 55)
)
hwMplsTeAutoTunnelPrimaryDownClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName")
)
if mibBuilder.loadTexts:
    hwMplsTeAutoTunnelPrimaryDownClear.setStatus(
        "current"
    )

hwMplsTunnelBBSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 56)
)
hwMplsTunnelBBSwitch.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelAdminStatus"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelOperStatus"))
)
if mibBuilder.loadTexts:
    hwMplsTunnelBBSwitch.setStatus(
        "current"
    )

hwMplsTunnelBBResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 57)
)
hwMplsTunnelBBResume.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelAdminStatus"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelOperStatus"))
)
if mibBuilder.loadTexts:
    hwMplsTunnelBBResume.setStatus(
        "current"
    )

hwMplsExtTunnelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 58)
)
hwMplsExtTunnelDown.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelType"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelAdminStatus"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelOperStatus"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDownReason"),
        ("IF-MIB", "ifName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDownLSRID"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDownIfIpAddrType"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDownIfIpAddr"))
)
if mibBuilder.loadTexts:
    hwMplsExtTunnelDown.setStatus(
        "current"
    )

hwMplsExtTunnelDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 59)
)
hwMplsExtTunnelDownClear.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelType"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelAdminStatus"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelOperStatus"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDownReason"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwMplsExtTunnelDownClear.setStatus(
        "current"
    )

hwMplsOamLocalLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 60)
)
hwMplsOamLocalLock.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamLocalLock.setStatus(
        "current"
    )

hwMplsOamLocalLockRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 61)
)
hwMplsOamLocalLockRecovery.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsOamLocalLockRecovery.setStatus(
        "current"
    )

hwMplsTunnelDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 62)
)
hwMplsTunnelDelete.setObjects(
      *(("MPLS-TE-STD-MIB", "mplsTunnelAdminStatus"),
        ("MPLS-TE-STD-MIB", "mplsTunnelOperStatus"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelIfName"))
)
if mibBuilder.loadTexts:
    hwMplsTunnelDelete.setStatus(
        "current"
    )

hwMplsLspThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 63)
)
hwMplsLspThresholdExceed.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLspProtocol"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLspCurrentCount"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLspThreshold"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLspTotalCount"))
)
if mibBuilder.loadTexts:
    hwMplsLspThresholdExceed.setStatus(
        "current"
    )

hwMplsLspThresholdExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 64)
)
hwMplsLspThresholdExceedClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLspProtocol")
)
if mibBuilder.loadTexts:
    hwMplsLspThresholdExceedClear.setStatus(
        "current"
    )

hwMplsLspTotalCountExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 65)
)
hwMplsLspTotalCountExceed.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLspProtocol"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLspTotalCount"))
)
if mibBuilder.loadTexts:
    hwMplsLspTotalCountExceed.setStatus(
        "current"
    )

hwMplsLspTotalCountExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 66)
)
hwMplsLspTotalCountExceedClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLspProtocol")
)
if mibBuilder.loadTexts:
    hwMplsLspTotalCountExceedClear.setStatus(
        "current"
    )

hwMplsDynamicLabelThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 67)
)
hwMplsDynamicLabelThresholdExceed.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsDynamicLabelTotalCount"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsDynamicLabelCurrentCount"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsDynamicLabelThresholdUpperLimit"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsDynamicLabelThresholdLowerLimit"))
)
if mibBuilder.loadTexts:
    hwMplsDynamicLabelThresholdExceed.setStatus(
        "current"
    )

hwMplsDynamicLabelThresholdExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 68)
)
hwMplsDynamicLabelThresholdExceedClear.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsDynamicLabelTotalCount"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsDynamicLabelCurrentCount"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsDynamicLabelThresholdUpperLimit"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsDynamicLabelThresholdLowerLimit"))
)
if mibBuilder.loadTexts:
    hwMplsDynamicLabelThresholdExceedClear.setStatus(
        "current"
    )

hwMplsDynamicLabelTotalCountExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 69)
)
hwMplsDynamicLabelTotalCountExceed.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsDynamicLabelTotalCount"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsDynamicLabelCurrentCount"))
)
if mibBuilder.loadTexts:
    hwMplsDynamicLabelTotalCountExceed.setStatus(
        "current"
    )

hwMplsDynamicLabelTotalCountExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 70)
)
hwMplsDynamicLabelTotalCountExceedClear.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsDynamicLabelTotalCount"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsDynamicLabelCurrentCount"))
)
if mibBuilder.loadTexts:
    hwMplsDynamicLabelTotalCountExceedClear.setStatus(
        "current"
    )

hwMplsResourceThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 71)
)
hwMplsResourceThresholdExceed.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsResourceType"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsResourceCurrentCount"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsResourceThreshold"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsResourceTotalCount"))
)
if mibBuilder.loadTexts:
    hwMplsResourceThresholdExceed.setStatus(
        "current"
    )

hwMplsResourceThresholdExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 72)
)
hwMplsResourceThresholdExceedClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsResourceType")
)
if mibBuilder.loadTexts:
    hwMplsResourceThresholdExceedClear.setStatus(
        "current"
    )

hwMplsResourceTotalCountExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 73)
)
hwMplsResourceTotalCountExceed.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsResourceType"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsResourceTotalCount"))
)
if mibBuilder.loadTexts:
    hwMplsResourceTotalCountExceed.setStatus(
        "current"
    )

hwMplsResourceTotalCountExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 74)
)
hwMplsResourceTotalCountExceedClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsResourceType")
)
if mibBuilder.loadTexts:
    hwMplsResourceTotalCountExceedClear.setStatus(
        "current"
    )

hwMplsLspLoopBack = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 75)
)
hwMplsLspLoopBack.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsSessionTunnelId"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLocalLspId"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsIngressLsrId"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsEgressLsrId"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLspName"))
)
if mibBuilder.loadTexts:
    hwMplsLspLoopBack.setStatus(
        "current"
    )

hwMplsLspLoopBackClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 76)
)
hwMplsLspLoopBackClear.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsSessionTunnelId"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLocalLspId"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsIngressLsrId"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsEgressLsrId"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLspName"))
)
if mibBuilder.loadTexts:
    hwMplsLspLoopBackClear.setStatus(
        "current"
    )

hwMplsTunnelCommitLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 77)
)
if mibBuilder.loadTexts:
    hwMplsTunnelCommitLost.setStatus(
        "current"
    )

hwMplsTunnelCommitLostClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 78)
)
if mibBuilder.loadTexts:
    hwMplsTunnelCommitLostClear.setStatus(
        "current"
    )

hwMplsTunnelHotstandbySwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 79)
)
hwMplsTunnelHotstandbySwitch.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName")
)
if mibBuilder.loadTexts:
    hwMplsTunnelHotstandbySwitch.setStatus(
        "current"
    )

hwMplsTunnelHotstandbyResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 1, 80)
)
hwMplsTunnelHotstandbyResume.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelInterfaceName")
)
if mibBuilder.loadTexts:
    hwMplsTunnelHotstandbyResume.setStatus(
        "current"
    )

hwMplsTunnelFrrConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 2, 3)
)
hwMplsTunnelFrrConfigChange.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelIfName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelFrrConfigOper"))
)
if mibBuilder.loadTexts:
    hwMplsTunnelFrrConfigChange.setStatus(
        "obsolete"
    )

hwMplsRingSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 1)
)
hwMplsRingSwitch.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingNodeID"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingDirection"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingSwitchReason"))
)
if mibBuilder.loadTexts:
    hwMplsRingSwitch.setStatus(
        "obsolete"
    )

hwMplsRingResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 2)
)
hwMplsRingResume.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingNodeID"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingDirection"))
)
if mibBuilder.loadTexts:
    hwMplsRingResume.setStatus(
        "obsolete"
    )

hwMplsRingWestOamLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 3)
)
hwMplsRingWestOamLoss.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingWestOamLoss.setStatus(
        "current"
    )

hwMplsRingWestOamLossClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 4)
)
hwMplsRingWestOamLossClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingWestOamLossClear.setStatus(
        "current"
    )

hwMplsRingEastOamLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 5)
)
hwMplsRingEastOamLoss.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingEastOamLoss.setStatus(
        "current"
    )

hwMplsRingEastOamLossClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 6)
)
hwMplsRingEastOamLossClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingEastOamLossClear.setStatus(
        "current"
    )

hwMplsRingWestOamRDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 7)
)
hwMplsRingWestOamRDI.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingWestOamRDI.setStatus(
        "current"
    )

hwMplsRingWestOamRDIClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 8)
)
hwMplsRingWestOamRDIClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingWestOamRDIClear.setStatus(
        "current"
    )

hwMplsRingEastOamRDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 9)
)
hwMplsRingEastOamRDI.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingEastOamRDI.setStatus(
        "current"
    )

hwMplsRingEastOamRDIClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 10)
)
hwMplsRingEastOamRDIClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingEastOamRDIClear.setStatus(
        "current"
    )

hwMplsRingWestOamUnexpectedMEG = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 11)
)
hwMplsRingWestOamUnexpectedMEG.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingWestOamUnexpectedMEG.setStatus(
        "current"
    )

hwMplsRingWestOamUnexpectedMEGClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 12)
)
hwMplsRingWestOamUnexpectedMEGClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingWestOamUnexpectedMEGClear.setStatus(
        "current"
    )

hwMplsRingEastOamUnexpectedMEG = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 13)
)
hwMplsRingEastOamUnexpectedMEG.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingEastOamUnexpectedMEG.setStatus(
        "current"
    )

hwMplsRingEastOamUnexpectedMEGClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 14)
)
hwMplsRingEastOamUnexpectedMEGClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingEastOamUnexpectedMEGClear.setStatus(
        "current"
    )

hwMplsRingWestOamUnexpectedPeriod = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 15)
)
hwMplsRingWestOamUnexpectedPeriod.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingWestOamUnexpectedPeriod.setStatus(
        "current"
    )

hwMplsRingWestOamUnexpectedPeriodClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 16)
)
hwMplsRingWestOamUnexpectedPeriodClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingWestOamUnexpectedPeriodClear.setStatus(
        "current"
    )

hwMplsRingEastOamUnexpectedPeriod = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 17)
)
hwMplsRingEastOamUnexpectedPeriod.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingEastOamUnexpectedPeriod.setStatus(
        "current"
    )

hwMplsRingEastOamUnexpectedPeriodClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 18)
)
hwMplsRingEastOamUnexpectedPeriodClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingEastOamUnexpectedPeriodClear.setStatus(
        "current"
    )

hwMplsRingWestOamExcess = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 19)
)
hwMplsRingWestOamExcess.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingWestOamExcess.setStatus(
        "current"
    )

hwMplsRingWestOamExcessClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 20)
)
hwMplsRingWestOamExcessClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingWestOamExcessClear.setStatus(
        "current"
    )

hwMplsRingEastOamExcess = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 21)
)
hwMplsRingEastOamExcess.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingEastOamExcess.setStatus(
        "current"
    )

hwMplsRingEastOamExcessClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 22)
)
hwMplsRingEastOamExcessClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingEastOamExcessClear.setStatus(
        "current"
    )

hwMplsRingWestOamSD = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 23)
)
hwMplsRingWestOamSD.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingWestOamSD.setStatus(
        "current"
    )

hwMplsRingWestOamSDClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 24)
)
hwMplsRingWestOamSDClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingWestOamSDClear.setStatus(
        "current"
    )

hwMplsRingEastOamSD = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 25)
)
hwMplsRingEastOamSD.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingEastOamSD.setStatus(
        "current"
    )

hwMplsRingEastOamSDClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 26)
)
hwMplsRingEastOamSDClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingEastOamSDClear.setStatus(
        "current"
    )

hwMplsRingWestOamSF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 27)
)
hwMplsRingWestOamSF.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingWestOamSF.setStatus(
        "current"
    )

hwMplsRingWestOamSFClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 28)
)
hwMplsRingWestOamSFClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingWestOamSFClear.setStatus(
        "current"
    )

hwMplsRingEastOamSF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 29)
)
hwMplsRingEastOamSF.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingEastOamSF.setStatus(
        "current"
    )

hwMplsRingEastOamSFClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 30)
)
hwMplsRingEastOamSFClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingEastOamSFClear.setStatus(
        "current"
    )

hwMplsRingWestAPSSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 31)
)
hwMplsRingWestAPSSwitch.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingWestAPSSwitch.setStatus(
        "current"
    )

hwMplsRingWestAPSResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 32)
)
hwMplsRingWestAPSResume.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingWestAPSResume.setStatus(
        "current"
    )

hwMplsRingEastAPSSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 33)
)
hwMplsRingEastAPSSwitch.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingEastAPSSwitch.setStatus(
        "current"
    )

hwMplsRingEastAPSResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 34)
)
hwMplsRingEastAPSResume.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingEastAPSResume.setStatus(
        "current"
    )

hwMplsRingWestAPSSwitchFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 35)
)
hwMplsRingWestAPSSwitchFail.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingWestAPSSwitchFail.setStatus(
        "current"
    )

hwMplsRingWestAPSSwitchFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 36)
)
hwMplsRingWestAPSSwitchFailClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingWestAPSSwitchFailClear.setStatus(
        "current"
    )

hwMplsRingEastAPSSwitchFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 37)
)
hwMplsRingEastAPSSwitchFail.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingEastAPSSwitchFail.setStatus(
        "current"
    )

hwMplsRingEastAPSSwitchFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 38)
)
hwMplsRingEastAPSSwitchFailClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingEastAPSSwitchFailClear.setStatus(
        "current"
    )

hwMplsRingWestAPSLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 39)
)
hwMplsRingWestAPSLost.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingWestAPSLost.setStatus(
        "current"
    )

hwMplsRingWestAPSLostClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 40)
)
hwMplsRingWestAPSLostClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingWestAPSLostClear.setStatus(
        "current"
    )

hwMplsRingEastAPSLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 41)
)
hwMplsRingEastAPSLost.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingEastAPSLost.setStatus(
        "current"
    )

hwMplsRingEastAPSLostClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 42)
)
hwMplsRingEastAPSLostClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingEastAPSLostClear.setStatus(
        "current"
    )

hwMplsRingWestAPSMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 43)
)
hwMplsRingWestAPSMismatch.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingWestAPSMismatch.setStatus(
        "current"
    )

hwMplsRingWestAPSMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 44)
)
hwMplsRingWestAPSMismatchClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingWestAPSMismatchClear.setStatus(
        "current"
    )

hwMplsRingEastAPSMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 45)
)
hwMplsRingEastAPSMismatch.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingEastAPSMismatch.setStatus(
        "current"
    )

hwMplsRingEastAPSMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 46)
)
hwMplsRingEastAPSMismatchClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingEastAPSMismatchClear.setStatus(
        "current"
    )

hwMplsRingWestOamUnexpectedMEP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 47)
)
hwMplsRingWestOamUnexpectedMEP.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingWestOamUnexpectedMEP.setStatus(
        "current"
    )

hwMplsRingWestOamUnexpectedMEPClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 48)
)
hwMplsRingWestOamUnexpectedMEPClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingWestOamUnexpectedMEPClear.setStatus(
        "current"
    )

hwMplsRingEastOamUnexpectedMEP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 49)
)
hwMplsRingEastOamUnexpectedMEP.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingEastOamUnexpectedMEP.setStatus(
        "current"
    )

hwMplsRingEastOamUnexpectedMEPClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 7, 2, 50)
)
hwMplsRingEastOamUnexpectedMEPClear.setObjects(
    ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingName")
)
if mibBuilder.loadTexts:
    hwMplsRingEastOamUnexpectedMEPClear.setStatus(
        "current"
    )


# Notifications groups

hwExtendTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 6, 2, 1)
)
hwExtendTrapGroup.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTeFrrProtAval"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTeFrrProtNotAval"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsStaticLspUp"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsStaticLspDown"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsStaticCRLspUp"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsStaticCRLspDown"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTeFrrSwitch"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTeFrrResume"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelHSBSwitch"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelHSBResume"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelOBSwitch"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelOBResume"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelChangeBw"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelTpOamLossSD"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamSDRecovery"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamLoss"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamLossRecovery"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamAis"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamAisRecovery"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamRdi"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamRdiRecovery"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamMeg"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamMegRecovery"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamMep"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamMepRecovery"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamSF"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamSFRecovery"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamPeriod"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamPeriodRecovery"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamLck"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamLckRecovery"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamExcess"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamExcessRecovery"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamMisMatch"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamMisMatchRecovery"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamMisMerge"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamMisMergeRecovery"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamUnknown"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamUnknownRecovery"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamBDI"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamBDIRecovery"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamFail"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamFailRecovery"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelPrimaryUp"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelPrimaryDown"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelHotstandbyUp"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelHotstandbyDown"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelOrdinaryUp"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelOrdinaryDown"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelBesteffortUp"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelBesteffortDown"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTeAutoTunnelDownClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTeAutoTunnelPrimaryDownClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelBBSwitch"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelBBResume"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsExtTunnelDown"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsExtTunnelDownClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamLocalLock"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsOamLocalLockRecovery"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingWestOamLoss"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingWestOamLossClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingEastOamLoss"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingEastOamLossClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingWestOamRDI"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingWestOamRDIClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingEastOamRDI"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingEastOamRDIClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingWestOamUnexpectedMEG"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingWestOamUnexpectedMEGClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingEastOamUnexpectedMEG"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingEastOamUnexpectedMEGClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingWestOamUnexpectedPeriod"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingWestOamUnexpectedPeriodClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingEastOamUnexpectedPeriod"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingEastOamUnexpectedPeriodClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingWestOamExcess"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingWestOamExcessClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingEastOamExcess"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingEastOamExcessClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingWestOamSD"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingWestOamSDClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingEastOamSD"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingEastOamSDClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingWestOamSF"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingWestOamSFClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingEastOamSF"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingEastOamSFClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingWestAPSSwitch"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingWestAPSResume"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingEastAPSSwitch"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingEastAPSResume"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingWestAPSSwitchFail"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingWestAPSSwitchFailClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingEastAPSSwitchFail"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingEastAPSSwitchFailClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingSwitch"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingResume"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingWestAPSLost"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingWestAPSLostClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingEastAPSLost"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingEastAPSLostClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingWestAPSMismatch"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingWestAPSMismatchClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingEastAPSMismatch"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingEastAPSMismatchClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingWestOamUnexpectedMEP"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingWestOamUnexpectedMEPClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingEastOamUnexpectedMEP"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingEastOamUnexpectedMEPClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDelete"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLspTotalCountExceed"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLspThresholdExceed"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLspTotalCountExceedClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLspThresholdExceedClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsDynamicLabelThresholdExceed"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsDynamicLabelThresholdExceedClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsDynamicLabelTotalCountExceed"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsDynamicLabelTotalCountExceedClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsResourceThresholdExceed"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsResourceThresholdExceedClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsResourceTotalCountExceed"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsResourceTotalCountExceedClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLspLoopBack"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsLspLoopBackClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelCommitLost"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelCommitLostClear"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelHotstandbySwitch"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelHotstandbyResume"))
)
if mibBuilder.loadTexts:
    hwExtendTrapGroup.setStatus(
        "current"
    )

hwObsoleteTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 6, 2, 2)
)
hwObsoleteTrapGroup.setObjects(
      *(("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelFrrConfigChange"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelUp"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelDown"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingSwitch"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsRingResume"))
)
if mibBuilder.loadTexts:
    hwObsoleteTrapGroup.setStatus(
        "obsolete"
    )


# Agent capabilities


# Module compliance

hwMplsModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 121, 6, 2, 3)
)
if mibBuilder.loadTexts:
    hwMplsModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MPLS-EXTEND-MIB",
    **{"hwMplsExtendMib": hwMplsExtendMib,
       "hwMplsExtendMibTunnel": hwMplsExtendMibTunnel,
       "hwMplsTunnelTable": hwMplsTunnelTable,
       "hwMplsTunnelEntry": hwMplsTunnelEntry,
       "hwMplsTunnelIndex": hwMplsTunnelIndex,
       "hwMplsTunnelInstance": hwMplsTunnelInstance,
       "hwMplsTunnelIngressLSRId": hwMplsTunnelIngressLSRId,
       "hwMplsTunnelEgressLSRId": hwMplsTunnelEgressLSRId,
       "hwMplsTunnelClassType": hwMplsTunnelClassType,
       "hwMplsTunnelBandwidth": hwMplsTunnelBandwidth,
       "hwMplsTunnelAdminStatus": hwMplsTunnelAdminStatus,
       "hwMplsTunnelOperStatus": hwMplsTunnelOperStatus,
       "hwMplsTunnelSessionAttr": hwMplsTunnelSessionAttr,
       "hwMplsTunnelFrrSetupPrio": hwMplsTunnelFrrSetupPrio,
       "hwMplsTunnelFrrHoldingPrio": hwMplsTunnelFrrHoldingPrio,
       "hwMplsTunnelFrrBandwidth": hwMplsTunnelFrrBandwidth,
       "hwMplsTunnelFrrSwitchover": hwMplsTunnelFrrSwitchover,
       "hwMplsTunnelFrrBypassTableIndex": hwMplsTunnelFrrBypassTableIndex,
       "hwMplsTunnelFrrARHopTableIndex": hwMplsTunnelFrrARHopTableIndex,
       "hwMplsTunnelName": hwMplsTunnelName,
       "hwMplsTunnelIfIndex": hwMplsTunnelIfIndex,
       "hwMplsTunnelPreBandwidth": hwMplsTunnelPreBandwidth,
       "hwMplsTunnelNextBandwidth": hwMplsTunnelNextBandwidth,
       "hwMplsTunnelCt0Bandwidth": hwMplsTunnelCt0Bandwidth,
       "hwMplsTunnelCt1Bandwidth": hwMplsTunnelCt1Bandwidth,
       "hwMplsTunnelCt2Bandwidth": hwMplsTunnelCt2Bandwidth,
       "hwMplsTunnelCt3Bandwidth": hwMplsTunnelCt3Bandwidth,
       "hwMplsTunnelCt4Bandwidth": hwMplsTunnelCt4Bandwidth,
       "hwMplsTunnelCt5Bandwidth": hwMplsTunnelCt5Bandwidth,
       "hwMplsTunnelCt6Bandwidth": hwMplsTunnelCt6Bandwidth,
       "hwMplsTunnelCt7Bandwidth": hwMplsTunnelCt7Bandwidth,
       "hwMplsTunnelLspType": hwMplsTunnelLspType,
       "hwMplsTunnelInterfaceName": hwMplsTunnelInterfaceName,
       "hwMplsTunnelSignalProto": hwMplsTunnelSignalProto,
       "hwMplsTunnelType": hwMplsTunnelType,
       "hwTunnelFrrBypassTable": hwTunnelFrrBypassTable,
       "hwTunnelFrrBypassEntry": hwTunnelFrrBypassEntry,
       "hwTunnelFrrBypassListIndex": hwTunnelFrrBypassListIndex,
       "hwTunnelFrrBypassIndex": hwTunnelFrrBypassIndex,
       "hwTunnelFrrBypassProtIfIndex": hwTunnelFrrBypassProtIfIndex,
       "hwTunnelFrrARHopTable": hwTunnelFrrARHopTable,
       "hwTunnelFrrARHopEntry": hwTunnelFrrARHopEntry,
       "hwTunnelFrrARHopListIndex": hwTunnelFrrARHopListIndex,
       "hwTunnelFrrARHopIndex": hwTunnelFrrARHopIndex,
       "hwTunnelFrrARHopProtDesired": hwTunnelFrrARHopProtDesired,
       "hwTunnelFrrARHopProtActual": hwTunnelFrrARHopProtActual,
       "hwTunnelFrrRouteDBTable": hwTunnelFrrRouteDBTable,
       "hwTunnelFrrRouteDBEntry": hwTunnelFrrRouteDBEntry,
       "hwTunnelFrrRouteDBTunnelIndex": hwTunnelFrrRouteDBTunnelIndex,
       "hwTunnelFrrRouteDBTunnelInstance": hwTunnelFrrRouteDBTunnelInstance,
       "hwTunnelFrrRouteDBTunnelIngressLSRId": hwTunnelFrrRouteDBTunnelIngressLSRId,
       "hwTunnelFrrRouteDBTunnelEngressLSRId": hwTunnelFrrRouteDBTunnelEngressLSRId,
       "hwTunnelFrrRouteDBBypassIfIndex": hwTunnelFrrRouteDBBypassIfIndex,
       "hwTunnelFrrRouteDBInnerLabel": hwTunnelFrrRouteDBInnerLabel,
       "hwStaticLspTable": hwStaticLspTable,
       "hwStaticLspEntry": hwStaticLspEntry,
       "hwStaticLspIndex": hwStaticLspIndex,
       "hwStaticLspInSegmentIndex": hwStaticLspInSegmentIndex,
       "hwStaticLspOutSegmentIndex": hwStaticLspOutSegmentIndex,
       "hwStaticLspOwner": hwStaticLspOwner,
       "hwStaticLspName": hwStaticLspName,
       "hwStaticLspStatus": hwStaticLspStatus,
       "hwStaticLspClassType": hwStaticLspClassType,
       "hwStaticLspBandwidth": hwStaticLspBandwidth,
       "hwMplsTeClassTable": hwMplsTeClassTable,
       "hwMplsTeClassEntry": hwMplsTeClassEntry,
       "hwMplsTeClassId": hwMplsTeClassId,
       "hwMplsTeClassClassType": hwMplsTeClassClassType,
       "hwMplsTeClassPriority": hwMplsTeClassPriority,
       "hwMplsTeClassDescription": hwMplsTeClassDescription,
       "hwMplsIfBcTable": hwMplsIfBcTable,
       "hwMplsIfBcEntry": hwMplsIfBcEntry,
       "hwMplsIfMaxResvBandwidth": hwMplsIfMaxResvBandwidth,
       "hwMplsIfBc0Bandwidth": hwMplsIfBc0Bandwidth,
       "hwMplsIfBc1Bandwidth": hwMplsIfBc1Bandwidth,
       "hwMplsIfBc2Bandwidth": hwMplsIfBc2Bandwidth,
       "hwMplsIfBc3Bandwidth": hwMplsIfBc3Bandwidth,
       "hwMplsIfBc4Bandwidth": hwMplsIfBc4Bandwidth,
       "hwMplsIfBc5Bandwidth": hwMplsIfBc5Bandwidth,
       "hwMplsIfBc6Bandwidth": hwMplsIfBc6Bandwidth,
       "hwMplsIfBc7Bandwidth": hwMplsIfBc7Bandwidth,
       "hwStaticLspTnlTable": hwStaticLspTnlTable,
       "hwStaticLspTnlEntry": hwStaticLspTnlEntry,
       "hwStaticLspTnlName": hwStaticLspTnlName,
       "hwStaticLspTnlToken": hwStaticLspTnlToken,
       "hwMplsTeVpnQosTable": hwMplsTeVpnQosTable,
       "hwMplsTeVpnQosEntry": hwMplsTeVpnQosEntry,
       "hwMplsTnlID": hwMplsTnlID,
       "hwMplsTeVpnMaxBandwidth": hwMplsTeVpnMaxBandwidth,
       "hwMplsTeVpnAllocatedBandwidth": hwMplsTeVpnAllocatedBandwidth,
       "hwStaticLspInIfIndex": hwStaticLspInIfIndex,
       "hwStaticLspInIfName": hwStaticLspInIfName,
       "hwStaticLspDownReason": hwStaticLspDownReason,
       "hwMplsTunnelStatisticsTable": hwMplsTunnelStatisticsTable,
       "hwMplsTunnelStatisticsEntry": hwMplsTunnelStatisticsEntry,
       "hwMplsTunnelStatisticsTunnelIndex": hwMplsTunnelStatisticsTunnelIndex,
       "hwMplsTunnelStatisticsIngressLSRId": hwMplsTunnelStatisticsIngressLSRId,
       "hwMplsTunnelStatisticsEgressLSRId": hwMplsTunnelStatisticsEgressLSRId,
       "hwMplsTunnelStatisticsHCInOctets": hwMplsTunnelStatisticsHCInOctets,
       "hwMplsTunnelStatisticsHCOutOctets": hwMplsTunnelStatisticsHCOutOctets,
       "hwMplsExtendTrap": hwMplsExtendTrap,
       "hwLspTrap": hwLspTrap,
       "hwMplsStaticLspUp": hwMplsStaticLspUp,
       "hwMplsStaticLspDown": hwMplsStaticLspDown,
       "hwMplsStaticCRLspUp": hwMplsStaticCRLspUp,
       "hwMplsStaticCRLspDown": hwMplsStaticCRLspDown,
       "hwMplsTeFrrProtAval": hwMplsTeFrrProtAval,
       "hwMplsTeFrrProtNotAval": hwMplsTeFrrProtNotAval,
       "hwMplsTeFrrSwitch": hwMplsTeFrrSwitch,
       "hwMplsTeFrrResume": hwMplsTeFrrResume,
       "hwMplsTunnelHSBSwitch": hwMplsTunnelHSBSwitch,
       "hwMplsTunnelHSBResume": hwMplsTunnelHSBResume,
       "hwMplsTunnelOBSwitch": hwMplsTunnelOBSwitch,
       "hwMplsTunnelOBResume": hwMplsTunnelOBResume,
       "hwMplsTunnelUp": hwMplsTunnelUp,
       "hwMplsTunnelDown": hwMplsTunnelDown,
       "hwMplsTunnelChangeBw": hwMplsTunnelChangeBw,
       "hwMplsTunnelTpOamLossSD": hwMplsTunnelTpOamLossSD,
       "hwMplsOamSDRecovery": hwMplsOamSDRecovery,
       "hwMplsOamLoss": hwMplsOamLoss,
       "hwMplsOamLossRecovery": hwMplsOamLossRecovery,
       "hwMplsOamAis": hwMplsOamAis,
       "hwMplsOamAisRecovery": hwMplsOamAisRecovery,
       "hwMplsOamRdi": hwMplsOamRdi,
       "hwMplsOamRdiRecovery": hwMplsOamRdiRecovery,
       "hwMplsOamMeg": hwMplsOamMeg,
       "hwMplsOamMegRecovery": hwMplsOamMegRecovery,
       "hwMplsOamMep": hwMplsOamMep,
       "hwMplsOamMepRecovery": hwMplsOamMepRecovery,
       "hwMplsOamSF": hwMplsOamSF,
       "hwMplsOamSFRecovery": hwMplsOamSFRecovery,
       "hwMplsOamPeriod": hwMplsOamPeriod,
       "hwMplsOamPeriodRecovery": hwMplsOamPeriodRecovery,
       "hwMplsOamLck": hwMplsOamLck,
       "hwMplsOamLckRecovery": hwMplsOamLckRecovery,
       "hwMplsOamExcess": hwMplsOamExcess,
       "hwMplsOamExcessRecovery": hwMplsOamExcessRecovery,
       "hwMplsOamMisMatch": hwMplsOamMisMatch,
       "hwMplsOamMisMatchRecovery": hwMplsOamMisMatchRecovery,
       "hwMplsOamMisMerge": hwMplsOamMisMerge,
       "hwMplsOamMisMergeRecovery": hwMplsOamMisMergeRecovery,
       "hwMplsOamUnknown": hwMplsOamUnknown,
       "hwMplsOamUnknownRecovery": hwMplsOamUnknownRecovery,
       "hwMplsOamBDI": hwMplsOamBDI,
       "hwMplsOamBDIRecovery": hwMplsOamBDIRecovery,
       "hwMplsOamFail": hwMplsOamFail,
       "hwMplsOamFailRecovery": hwMplsOamFailRecovery,
       "hwMplsTunnelPrimaryUp": hwMplsTunnelPrimaryUp,
       "hwMplsTunnelPrimaryDown": hwMplsTunnelPrimaryDown,
       "hwMplsTunnelHotstandbyUp": hwMplsTunnelHotstandbyUp,
       "hwMplsTunnelHotstandbyDown": hwMplsTunnelHotstandbyDown,
       "hwMplsTunnelOrdinaryUp": hwMplsTunnelOrdinaryUp,
       "hwMplsTunnelOrdinaryDown": hwMplsTunnelOrdinaryDown,
       "hwMplsTunnelBesteffortUp": hwMplsTunnelBesteffortUp,
       "hwMplsTunnelBesteffortDown": hwMplsTunnelBesteffortDown,
       "hwMplsTeAutoTunnelDownClear": hwMplsTeAutoTunnelDownClear,
       "hwMplsTeAutoTunnelPrimaryDownClear": hwMplsTeAutoTunnelPrimaryDownClear,
       "hwMplsTunnelBBSwitch": hwMplsTunnelBBSwitch,
       "hwMplsTunnelBBResume": hwMplsTunnelBBResume,
       "hwMplsExtTunnelDown": hwMplsExtTunnelDown,
       "hwMplsExtTunnelDownClear": hwMplsExtTunnelDownClear,
       "hwMplsOamLocalLock": hwMplsOamLocalLock,
       "hwMplsOamLocalLockRecovery": hwMplsOamLocalLockRecovery,
       "hwMplsTunnelDelete": hwMplsTunnelDelete,
       "hwMplsLspThresholdExceed": hwMplsLspThresholdExceed,
       "hwMplsLspThresholdExceedClear": hwMplsLspThresholdExceedClear,
       "hwMplsLspTotalCountExceed": hwMplsLspTotalCountExceed,
       "hwMplsLspTotalCountExceedClear": hwMplsLspTotalCountExceedClear,
       "hwMplsDynamicLabelThresholdExceed": hwMplsDynamicLabelThresholdExceed,
       "hwMplsDynamicLabelThresholdExceedClear": hwMplsDynamicLabelThresholdExceedClear,
       "hwMplsDynamicLabelTotalCountExceed": hwMplsDynamicLabelTotalCountExceed,
       "hwMplsDynamicLabelTotalCountExceedClear": hwMplsDynamicLabelTotalCountExceedClear,
       "hwMplsResourceThresholdExceed": hwMplsResourceThresholdExceed,
       "hwMplsResourceThresholdExceedClear": hwMplsResourceThresholdExceedClear,
       "hwMplsResourceTotalCountExceed": hwMplsResourceTotalCountExceed,
       "hwMplsResourceTotalCountExceedClear": hwMplsResourceTotalCountExceedClear,
       "hwMplsLspLoopBack": hwMplsLspLoopBack,
       "hwMplsLspLoopBackClear": hwMplsLspLoopBackClear,
       "hwMplsTunnelCommitLost": hwMplsTunnelCommitLost,
       "hwMplsTunnelCommitLostClear": hwMplsTunnelCommitLostClear,
       "hwMplsTunnelHotstandbySwitch": hwMplsTunnelHotstandbySwitch,
       "hwMplsTunnelHotstandbyResume": hwMplsTunnelHotstandbyResume,
       "hwMplsTrapObjects": hwMplsTrapObjects,
       "hwMplsTunnelIfName": hwMplsTunnelIfName,
       "hwMplsTunnelFrrConfigOper": hwMplsTunnelFrrConfigOper,
       "hwMplsTunnelDownReason": hwMplsTunnelDownReason,
       "hwMplsLspProtocol": hwMplsLspProtocol,
       "hwMplsLspThreshold": hwMplsLspThreshold,
       "hwMplsLspTotalCount": hwMplsLspTotalCount,
       "hwMplsLspCurrentCount": hwMplsLspCurrentCount,
       "hwMplsTunnelDownLSRID": hwMplsTunnelDownLSRID,
       "hwMplsTunnelDownIfIpAddr": hwMplsTunnelDownIfIpAddr,
       "hwMplsTunnelDownIfIpAddrType": hwMplsTunnelDownIfIpAddrType,
       "hwMplsResourceType": hwMplsResourceType,
       "hwMplsResourceCurrentCount": hwMplsResourceCurrentCount,
       "hwMplsResourceThreshold": hwMplsResourceThreshold,
       "hwMplsResourceTotalCount": hwMplsResourceTotalCount,
       "hwMplsSessionTunnelId": hwMplsSessionTunnelId,
       "hwMplsLocalLspId": hwMplsLocalLspId,
       "hwMplsIngressLsrId": hwMplsIngressLsrId,
       "hwMplsEgressLsrId": hwMplsEgressLsrId,
       "hwMplsLspName": hwMplsLspName,
       "hwMplsTunnelFrrConfigChange": hwMplsTunnelFrrConfigChange,
       "hwMplsGlobalObject": hwMplsGlobalObject,
       "hwMplsGlobalWorkMode": hwMplsGlobalWorkMode,
       "hwMplsGlobalBcModel": hwMplsGlobalBcModel,
       "hwMplsDynamicLabelTotalCount": hwMplsDynamicLabelTotalCount,
       "hwMplsDynamicLabelCurrentCount": hwMplsDynamicLabelCurrentCount,
       "hwMplsDynamicLabelThresholdUpperLimit": hwMplsDynamicLabelThresholdUpperLimit,
       "hwMplsDynamicLabelThresholdLowerLimit": hwMplsDynamicLabelThresholdLowerLimit,
       "hwMplsLspStatistics": hwMplsLspStatistics,
       "hwMplsLspStatisticsTable": hwMplsLspStatisticsTable,
       "hwMplsLspStatisticsEntry": hwMplsLspStatisticsEntry,
       "hwMplsLspStatisticsLspType": hwMplsLspStatisticsLspType,
       "hwMplsLspStatisticsIngressLspCount": hwMplsLspStatisticsIngressLspCount,
       "hwMplsLspStatisticsTransitLspCount": hwMplsLspStatisticsTransitLspCount,
       "hwMplsLspStatisticsEgressLspCount": hwMplsLspStatisticsEgressLspCount,
       "hwMplsLspStatisticsTotalLspCount": hwMplsLspStatisticsTotalLspCount,
       "hwMplsTrafficStatisticsStaticLspTable": hwMplsTrafficStatisticsStaticLspTable,
       "hwMplsTrafficStatisticsStaticLspEntry": hwMplsTrafficStatisticsStaticLspEntry,
       "hwMplsTrafficStatisticsStaticLspName": hwMplsTrafficStatisticsStaticLspName,
       "hwMplsTrafficStatisticsStaticLspForwardInBytes": hwMplsTrafficStatisticsStaticLspForwardInBytes,
       "hwMplsTrafficStatisticsStaticLspForwardInPackets": hwMplsTrafficStatisticsStaticLspForwardInPackets,
       "hwMplsTrafficStatisticsStaticLspForwardOutBytes": hwMplsTrafficStatisticsStaticLspForwardOutBytes,
       "hwMplsTrafficStatisticsStaticLspForwardOutPackets": hwMplsTrafficStatisticsStaticLspForwardOutPackets,
       "hwMplsTrafficStatisticsStaticLspBackwardInBytes": hwMplsTrafficStatisticsStaticLspBackwardInBytes,
       "hwMplsTrafficStatisticsStaticLspBackwardInPackets": hwMplsTrafficStatisticsStaticLspBackwardInPackets,
       "hwMplsTrafficStatisticsStaticLspBackwardOutBytes": hwMplsTrafficStatisticsStaticLspBackwardOutBytes,
       "hwMplsTrafficStatisticsStaticLspBackwardOutPackets": hwMplsTrafficStatisticsStaticLspBackwardOutPackets,
       "hwMplsExtendConformance": hwMplsExtendConformance,
       "hwMplsExtendGroups": hwMplsExtendGroups,
       "hwMplsTunnelGroup": hwMplsTunnelGroup,
       "hwStaticLspGroup": hwStaticLspGroup,
       "hwMplsDsTeGroup": hwMplsDsTeGroup,
       "hwMplsLspStatisticsGroup": hwMplsLspStatisticsGroup,
       "hwMplsObsoleteGroup": hwMplsObsoleteGroup,
       "hwMplsTrapGroup": hwMplsTrapGroup,
       "hwMplsRingGroup": hwMplsRingGroup,
       "hwMplsGlobalGroup": hwMplsGlobalGroup,
       "hwMplsLspGroup": hwMplsLspGroup,
       "hwMplsLspTrafficStatisticGroup": hwMplsLspTrafficStatisticGroup,
       "hwMplsResourceGroup": hwMplsResourceGroup,
       "hwMplsExtendCompliances": hwMplsExtendCompliances,
       "hwExtendTrapGroup": hwExtendTrapGroup,
       "hwObsoleteTrapGroup": hwObsoleteTrapGroup,
       "hwMplsModuleCompliance": hwMplsModuleCompliance,
       "hwMplsRingMib": hwMplsRingMib,
       "hwMplsRingTable": hwMplsRingTable,
       "hwMplsRingEntry": hwMplsRingEntry,
       "hwMplsRingID": hwMplsRingID,
       "hwMplsRingNodeID": hwMplsRingNodeID,
       "hwMplsRingName": hwMplsRingName,
       "hwMplsRingDirection": hwMplsRingDirection,
       "hwMplsRingSwitchReason": hwMplsRingSwitchReason,
       "hwMplsRingTrap": hwMplsRingTrap,
       "hwMplsRingSwitch": hwMplsRingSwitch,
       "hwMplsRingResume": hwMplsRingResume,
       "hwMplsRingWestOamLoss": hwMplsRingWestOamLoss,
       "hwMplsRingWestOamLossClear": hwMplsRingWestOamLossClear,
       "hwMplsRingEastOamLoss": hwMplsRingEastOamLoss,
       "hwMplsRingEastOamLossClear": hwMplsRingEastOamLossClear,
       "hwMplsRingWestOamRDI": hwMplsRingWestOamRDI,
       "hwMplsRingWestOamRDIClear": hwMplsRingWestOamRDIClear,
       "hwMplsRingEastOamRDI": hwMplsRingEastOamRDI,
       "hwMplsRingEastOamRDIClear": hwMplsRingEastOamRDIClear,
       "hwMplsRingWestOamUnexpectedMEG": hwMplsRingWestOamUnexpectedMEG,
       "hwMplsRingWestOamUnexpectedMEGClear": hwMplsRingWestOamUnexpectedMEGClear,
       "hwMplsRingEastOamUnexpectedMEG": hwMplsRingEastOamUnexpectedMEG,
       "hwMplsRingEastOamUnexpectedMEGClear": hwMplsRingEastOamUnexpectedMEGClear,
       "hwMplsRingWestOamUnexpectedPeriod": hwMplsRingWestOamUnexpectedPeriod,
       "hwMplsRingWestOamUnexpectedPeriodClear": hwMplsRingWestOamUnexpectedPeriodClear,
       "hwMplsRingEastOamUnexpectedPeriod": hwMplsRingEastOamUnexpectedPeriod,
       "hwMplsRingEastOamUnexpectedPeriodClear": hwMplsRingEastOamUnexpectedPeriodClear,
       "hwMplsRingWestOamExcess": hwMplsRingWestOamExcess,
       "hwMplsRingWestOamExcessClear": hwMplsRingWestOamExcessClear,
       "hwMplsRingEastOamExcess": hwMplsRingEastOamExcess,
       "hwMplsRingEastOamExcessClear": hwMplsRingEastOamExcessClear,
       "hwMplsRingWestOamSD": hwMplsRingWestOamSD,
       "hwMplsRingWestOamSDClear": hwMplsRingWestOamSDClear,
       "hwMplsRingEastOamSD": hwMplsRingEastOamSD,
       "hwMplsRingEastOamSDClear": hwMplsRingEastOamSDClear,
       "hwMplsRingWestOamSF": hwMplsRingWestOamSF,
       "hwMplsRingWestOamSFClear": hwMplsRingWestOamSFClear,
       "hwMplsRingEastOamSF": hwMplsRingEastOamSF,
       "hwMplsRingEastOamSFClear": hwMplsRingEastOamSFClear,
       "hwMplsRingWestAPSSwitch": hwMplsRingWestAPSSwitch,
       "hwMplsRingWestAPSResume": hwMplsRingWestAPSResume,
       "hwMplsRingEastAPSSwitch": hwMplsRingEastAPSSwitch,
       "hwMplsRingEastAPSResume": hwMplsRingEastAPSResume,
       "hwMplsRingWestAPSSwitchFail": hwMplsRingWestAPSSwitchFail,
       "hwMplsRingWestAPSSwitchFailClear": hwMplsRingWestAPSSwitchFailClear,
       "hwMplsRingEastAPSSwitchFail": hwMplsRingEastAPSSwitchFail,
       "hwMplsRingEastAPSSwitchFailClear": hwMplsRingEastAPSSwitchFailClear,
       "hwMplsRingWestAPSLost": hwMplsRingWestAPSLost,
       "hwMplsRingWestAPSLostClear": hwMplsRingWestAPSLostClear,
       "hwMplsRingEastAPSLost": hwMplsRingEastAPSLost,
       "hwMplsRingEastAPSLostClear": hwMplsRingEastAPSLostClear,
       "hwMplsRingWestAPSMismatch": hwMplsRingWestAPSMismatch,
       "hwMplsRingWestAPSMismatchClear": hwMplsRingWestAPSMismatchClear,
       "hwMplsRingEastAPSMismatch": hwMplsRingEastAPSMismatch,
       "hwMplsRingEastAPSMismatchClear": hwMplsRingEastAPSMismatchClear,
       "hwMplsRingWestOamUnexpectedMEP": hwMplsRingWestOamUnexpectedMEP,
       "hwMplsRingWestOamUnexpectedMEPClear": hwMplsRingWestOamUnexpectedMEPClear,
       "hwMplsRingEastOamUnexpectedMEP": hwMplsRingEastOamUnexpectedMEP,
       "hwMplsRingEastOamUnexpectedMEPClear": hwMplsRingEastOamUnexpectedMEPClear}
)
