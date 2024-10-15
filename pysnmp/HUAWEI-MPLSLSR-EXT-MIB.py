# SNMP MIB module (HUAWEI-MPLSLSR-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MPLSLSR-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:11 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(MplsLabel,) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsLabel")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwMplsLsrExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182)
)
hwMplsLsrExtMIB.setRevisions(
        ("2013-09-24 16:55",
         "2011-07-30 11:00",
         "2010-11-22 16:00",
         "2010-08-11 16:00",
         "2010-07-12 16:00",
         "2009-03-10 16:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwMplsLsrExtObject_ObjectIdentity = ObjectIdentity
hwMplsLsrExtObject = _HwMplsLsrExtObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1)
)
_HwMplsLsrId_Type = IpAddress
_HwMplsLsrId_Object = MibScalar
hwMplsLsrId = _HwMplsLsrId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 1),
    _HwMplsLsrId_Type()
)
hwMplsLsrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsLsrId.setStatus("current")
_HwMplsCapabilityConfig_Type = EnabledStatus
_HwMplsCapabilityConfig_Object = MibScalar
hwMplsCapabilityConfig = _HwMplsCapabilityConfig_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 2),
    _HwMplsCapabilityConfig_Type()
)
hwMplsCapabilityConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsCapabilityConfig.setStatus("current")


class _HwMplsLabelAdvertise_Type(Integer32):
    """Custom type hwMplsLabelAdvertise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("explicitNull", 1),
          ("implicitNull", 2),
          ("nonNull", 3))
    )


_HwMplsLabelAdvertise_Type.__name__ = "Integer32"
_HwMplsLabelAdvertise_Object = MibScalar
hwMplsLabelAdvertise = _HwMplsLabelAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 3),
    _HwMplsLabelAdvertise_Type()
)
hwMplsLabelAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsLabelAdvertise.setStatus("current")


class _HwMplsStatisticsIntervalTimer_Type(Integer32):
    """Custom type hwMplsStatisticsIntervalTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwMplsStatisticsIntervalTimer_Type.__name__ = "Integer32"
_HwMplsStatisticsIntervalTimer_Object = MibScalar
hwMplsStatisticsIntervalTimer = _HwMplsStatisticsIntervalTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 4),
    _HwMplsStatisticsIntervalTimer_Type()
)
hwMplsStatisticsIntervalTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsStatisticsIntervalTimer.setStatus("current")
_HwMplsBfdCapabilityConfig_Type = EnabledStatus
_HwMplsBfdCapabilityConfig_Object = MibScalar
hwMplsBfdCapabilityConfig = _HwMplsBfdCapabilityConfig_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 5),
    _HwMplsBfdCapabilityConfig_Type()
)
hwMplsBfdCapabilityConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsBfdCapabilityConfig.setStatus("current")
_HwMplsBfdMinTx_Type = Integer32
_HwMplsBfdMinTx_Object = MibScalar
hwMplsBfdMinTx = _HwMplsBfdMinTx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 6),
    _HwMplsBfdMinTx_Type()
)
hwMplsBfdMinTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsBfdMinTx.setStatus("current")
_HwMplsBfdMinRx_Type = Integer32
_HwMplsBfdMinRx_Object = MibScalar
hwMplsBfdMinRx = _HwMplsBfdMinRx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 7),
    _HwMplsBfdMinRx_Type()
)
hwMplsBfdMinRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsBfdMinRx.setStatus("current")
_HwMplsBfdDetectMultiplier_Type = Integer32
_HwMplsBfdDetectMultiplier_Object = MibScalar
hwMplsBfdDetectMultiplier = _HwMplsBfdDetectMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 8),
    _HwMplsBfdDetectMultiplier_Type()
)
hwMplsBfdDetectMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsBfdDetectMultiplier.setStatus("current")
_HwMplsFecListName_Type = DisplayString
_HwMplsFecListName_Object = MibScalar
hwMplsFecListName = _HwMplsFecListName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 9),
    _HwMplsFecListName_Type()
)
hwMplsFecListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsFecListName.setStatus("current")


class _HwMplsBfdTrigger_Type(Integer32):
    """Custom type hwMplsBfdTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("triggerFeclist", 2),
          ("triggerHost", 1))
    )


_HwMplsBfdTrigger_Type.__name__ = "Integer32"
_HwMplsBfdTrigger_Object = MibScalar
hwMplsBfdTrigger = _HwMplsBfdTrigger_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 10),
    _HwMplsBfdTrigger_Type()
)
hwMplsBfdTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsBfdTrigger.setStatus("current")
_HwMplsBfdTriggerNextHop_Type = IpAddress
_HwMplsBfdTriggerNextHop_Object = MibScalar
hwMplsBfdTriggerNextHop = _HwMplsBfdTriggerNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 11),
    _HwMplsBfdTriggerNextHop_Type()
)
hwMplsBfdTriggerNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsBfdTriggerNextHop.setStatus("current")
_HwMplsBfdTriggerInterface_Type = Unsigned32
_HwMplsBfdTriggerInterface_Object = MibScalar
hwMplsBfdTriggerInterface = _HwMplsBfdTriggerInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 12),
    _HwMplsBfdTriggerInterface_Type()
)
hwMplsBfdTriggerInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsBfdTriggerInterface.setStatus("current")
_HwMplsBfdTriggerFecListName_Type = DisplayString
_HwMplsBfdTriggerFecListName_Object = MibScalar
hwMplsBfdTriggerFecListName = _HwMplsBfdTriggerFecListName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 13),
    _HwMplsBfdTriggerFecListName_Type()
)
hwMplsBfdTriggerFecListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsBfdTriggerFecListName.setStatus("current")
_HwLdpVirtualTunnelFEC_Type = Unsigned32
_HwLdpVirtualTunnelFEC_Object = MibScalar
hwLdpVirtualTunnelFEC = _HwLdpVirtualTunnelFEC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 14),
    _HwLdpVirtualTunnelFEC_Type()
)
hwLdpVirtualTunnelFEC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLdpVirtualTunnelFEC.setStatus("current")
_HwMplsBgpBfdCapabilityConfig_Type = EnabledStatus
_HwMplsBgpBfdCapabilityConfig_Object = MibScalar
hwMplsBgpBfdCapabilityConfig = _HwMplsBgpBfdCapabilityConfig_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 15),
    _HwMplsBgpBfdCapabilityConfig_Type()
)
hwMplsBgpBfdCapabilityConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsBgpBfdCapabilityConfig.setStatus("current")
_HwMplsBgpBfdMinTx_Type = Integer32
_HwMplsBgpBfdMinTx_Object = MibScalar
hwMplsBgpBfdMinTx = _HwMplsBgpBfdMinTx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 16),
    _HwMplsBgpBfdMinTx_Type()
)
hwMplsBgpBfdMinTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsBgpBfdMinTx.setStatus("current")
_HwMplsBgpBfdMinRx_Type = Integer32
_HwMplsBgpBfdMinRx_Object = MibScalar
hwMplsBgpBfdMinRx = _HwMplsBgpBfdMinRx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 17),
    _HwMplsBgpBfdMinRx_Type()
)
hwMplsBgpBfdMinRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsBgpBfdMinRx.setStatus("current")
_HwMplsBgpBfdDetectMultiplier_Type = Integer32
_HwMplsBgpBfdDetectMultiplier_Object = MibScalar
hwMplsBgpBfdDetectMultiplier = _HwMplsBgpBfdDetectMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 18),
    _HwMplsBgpBfdDetectMultiplier_Type()
)
hwMplsBgpBfdDetectMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsBgpBfdDetectMultiplier.setStatus("current")


class _HwMplsBgpBfdTriggerTunnel_Type(Integer32):
    """Custom type hwMplsBgpBfdTriggerTunnel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("triggerHost", 1),
          ("triggerIpPrefix", 2))
    )


_HwMplsBgpBfdTriggerTunnel_Type.__name__ = "Integer32"
_HwMplsBgpBfdTriggerTunnel_Object = MibScalar
hwMplsBgpBfdTriggerTunnel = _HwMplsBgpBfdTriggerTunnel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 19),
    _HwMplsBgpBfdTriggerTunnel_Type()
)
hwMplsBgpBfdTriggerTunnel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsBgpBfdTriggerTunnel.setStatus("current")
_HwMplsBgpBfdTriggerTunnelIpprefix_Type = DisplayString
_HwMplsBgpBfdTriggerTunnelIpprefix_Object = MibScalar
hwMplsBgpBfdTriggerTunnelIpprefix = _HwMplsBgpBfdTriggerTunnelIpprefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 20),
    _HwMplsBgpBfdTriggerTunnelIpprefix_Type()
)
hwMplsBgpBfdTriggerTunnelIpprefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsBgpBfdTriggerTunnelIpprefix.setStatus("current")
_HwMplsFecListTable_Object = MibTable
hwMplsFecListTable = _HwMplsFecListTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 50)
)
if mibBuilder.loadTexts:
    hwMplsFecListTable.setStatus("current")
_HwMplsFecListEntry_Object = MibTableRow
hwMplsFecListEntry = _HwMplsFecListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 50, 1)
)
hwMplsFecListEntry.setIndexNames(
    (0, "HUAWEI-MPLSLSR-EXT-MIB", "hwMplsFecNodeIpAddress"),
    (0, "HUAWEI-MPLSLSR-EXT-MIB", "hwMplsFecNodeInterface"),
    (0, "HUAWEI-MPLSLSR-EXT-MIB", "hwMplsFecNodeNextHop"),
)
if mibBuilder.loadTexts:
    hwMplsFecListEntry.setStatus("current")
_HwMplsFecNodeIpAddress_Type = IpAddress
_HwMplsFecNodeIpAddress_Object = MibTableColumn
hwMplsFecNodeIpAddress = _HwMplsFecNodeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 50, 1, 2),
    _HwMplsFecNodeIpAddress_Type()
)
hwMplsFecNodeIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsFecNodeIpAddress.setStatus("current")
_HwMplsFecNodeInterface_Type = Unsigned32
_HwMplsFecNodeInterface_Object = MibTableColumn
hwMplsFecNodeInterface = _HwMplsFecNodeInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 50, 1, 3),
    _HwMplsFecNodeInterface_Type()
)
hwMplsFecNodeInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsFecNodeInterface.setStatus("current")
_HwMplsFecNodeNextHop_Type = IpAddress
_HwMplsFecNodeNextHop_Object = MibTableColumn
hwMplsFecNodeNextHop = _HwMplsFecNodeNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 50, 1, 4),
    _HwMplsFecNodeNextHop_Type()
)
hwMplsFecNodeNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsFecNodeNextHop.setStatus("current")
_HwMplsFecListRowStatus_Type = RowStatus
_HwMplsFecListRowStatus_Object = MibTableColumn
hwMplsFecListRowStatus = _HwMplsFecListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 50, 1, 51),
    _HwMplsFecListRowStatus_Type()
)
hwMplsFecListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsFecListRowStatus.setStatus("current")
_HwMplsInterfaceTable_Object = MibTable
hwMplsInterfaceTable = _HwMplsInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 51)
)
if mibBuilder.loadTexts:
    hwMplsInterfaceTable.setStatus("current")
_HwMplsInterfaceEntry_Object = MibTableRow
hwMplsInterfaceEntry = _HwMplsInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 51, 1)
)
hwMplsInterfaceEntry.setIndexNames(
    (0, "HUAWEI-MPLSLSR-EXT-MIB", "hwMplsInterfaceIndex"),
)
if mibBuilder.loadTexts:
    hwMplsInterfaceEntry.setStatus("current")
_HwMplsInterfaceIndex_Type = InterfaceIndex
_HwMplsInterfaceIndex_Object = MibTableColumn
hwMplsInterfaceIndex = _HwMplsInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 51, 1, 1),
    _HwMplsInterfaceIndex_Type()
)
hwMplsInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsInterfaceIndex.setStatus("current")
_HwMplsMtu_Type = Integer32
_HwMplsMtu_Object = MibTableColumn
hwMplsMtu = _HwMplsMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 51, 1, 11),
    _HwMplsMtu_Type()
)
hwMplsMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsMtu.setStatus("current")
_HwMplsInterfaceRowStatus_Type = RowStatus
_HwMplsInterfaceRowStatus_Object = MibTableColumn
hwMplsInterfaceRowStatus = _HwMplsInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 51, 1, 51),
    _HwMplsInterfaceRowStatus_Type()
)
hwMplsInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsInterfaceRowStatus.setStatus("current")
_HwLdpStaticFrrInterfaceTable_Object = MibTable
hwLdpStaticFrrInterfaceTable = _HwLdpStaticFrrInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 52)
)
if mibBuilder.loadTexts:
    hwLdpStaticFrrInterfaceTable.setStatus("current")
_HwLdpStaticFrrInterfaceEntry_Object = MibTableRow
hwLdpStaticFrrInterfaceEntry = _HwLdpStaticFrrInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 52, 1)
)
hwLdpStaticFrrInterfaceEntry.setIndexNames(
    (0, "HUAWEI-MPLSLSR-EXT-MIB", "hwMplsInterfaceIndex"),
    (0, "HUAWEI-MPLSLSR-EXT-MIB", "hwLdpStaticFrrPriority"),
)
if mibBuilder.loadTexts:
    hwLdpStaticFrrInterfaceEntry.setStatus("current")


class _HwLdpStaticFrrPriority_Type(Integer32):
    """Custom type hwLdpStaticFrrPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwLdpStaticFrrPriority_Type.__name__ = "Integer32"
_HwLdpStaticFrrPriority_Object = MibTableColumn
hwLdpStaticFrrPriority = _HwLdpStaticFrrPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 52, 1, 1),
    _HwLdpStaticFrrPriority_Type()
)
hwLdpStaticFrrPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwLdpStaticFrrPriority.setStatus("current")
_HwLdpStaticFrrNextHop_Type = IpAddress
_HwLdpStaticFrrNextHop_Object = MibTableColumn
hwLdpStaticFrrNextHop = _HwLdpStaticFrrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 52, 1, 11),
    _HwLdpStaticFrrNextHop_Type()
)
hwLdpStaticFrrNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpStaticFrrNextHop.setStatus("current")
_HwLdpStaticFrrIpPrefix_Type = DisplayString
_HwLdpStaticFrrIpPrefix_Object = MibTableColumn
hwLdpStaticFrrIpPrefix = _HwLdpStaticFrrIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 52, 1, 12),
    _HwLdpStaticFrrIpPrefix_Type()
)
hwLdpStaticFrrIpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpStaticFrrIpPrefix.setStatus("current")
_HwLdpStaticFrrInterfaceRowStatus_Type = RowStatus
_HwLdpStaticFrrInterfaceRowStatus_Object = MibTableColumn
hwLdpStaticFrrInterfaceRowStatus = _HwLdpStaticFrrInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 52, 1, 51),
    _HwLdpStaticFrrInterfaceRowStatus_Type()
)
hwLdpStaticFrrInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpStaticFrrInterfaceRowStatus.setStatus("current")
_HwLdpVirtualTunnelTable_Object = MibTable
hwLdpVirtualTunnelTable = _HwLdpVirtualTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 53)
)
if mibBuilder.loadTexts:
    hwLdpVirtualTunnelTable.setStatus("current")
_HwLdpVirtualTunnelEntry_Object = MibTableRow
hwLdpVirtualTunnelEntry = _HwLdpVirtualTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 53, 1)
)
hwLdpVirtualTunnelEntry.setIndexNames(
    (0, "HUAWEI-MPLSLSR-EXT-MIB", "hwLdpVirtualTunnelIndex"),
)
if mibBuilder.loadTexts:
    hwLdpVirtualTunnelEntry.setStatus("current")
_HwLdpVirtualTunnelIndex_Type = Unsigned32
_HwLdpVirtualTunnelIndex_Object = MibTableColumn
hwLdpVirtualTunnelIndex = _HwLdpVirtualTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 53, 1, 1),
    _HwLdpVirtualTunnelIndex_Type()
)
hwLdpVirtualTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwLdpVirtualTunnelIndex.setStatus("current")


class _HwLdpVirtualStatus_Type(Integer32):
    """Custom type hwLdpVirtualStatus based on Integer32"""
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


_HwLdpVirtualStatus_Type.__name__ = "Integer32"
_HwLdpVirtualStatus_Object = MibTableColumn
hwLdpVirtualStatus = _HwLdpVirtualStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 53, 1, 2),
    _HwLdpVirtualStatus_Type()
)
hwLdpVirtualStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLdpVirtualStatus.setStatus("current")
_HwLdpXcIndexArray_Type = OctetString
_HwLdpXcIndexArray_Object = MibTableColumn
hwLdpXcIndexArray = _HwLdpXcIndexArray_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 53, 1, 3),
    _HwLdpXcIndexArray_Type()
)
hwLdpXcIndexArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLdpXcIndexArray.setStatus("current")
_HwLdpOutSegmentIndexArray_Type = OctetString
_HwLdpOutSegmentIndexArray_Object = MibTableColumn
hwLdpOutSegmentIndexArray = _HwLdpOutSegmentIndexArray_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 53, 1, 4),
    _HwLdpOutSegmentIndexArray_Type()
)
hwLdpOutSegmentIndexArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLdpOutSegmentIndexArray.setStatus("current")
_HwLdpVirtualTunnelTrap_ObjectIdentity = ObjectIdentity
hwLdpVirtualTunnelTrap = _HwLdpVirtualTunnelTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 54)
)
_HwMplsStaticLspTable_Object = MibTable
hwMplsStaticLspTable = _HwMplsStaticLspTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 55)
)
if mibBuilder.loadTexts:
    hwMplsStaticLspTable.setStatus("current")
_HwMplsStaticLspEntry_Object = MibTableRow
hwMplsStaticLspEntry = _HwMplsStaticLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 55, 1)
)
hwMplsStaticLspEntry.setIndexNames(
    (0, "HUAWEI-MPLSLSR-EXT-MIB", "hwMplsStaticLspName"),
)
if mibBuilder.loadTexts:
    hwMplsStaticLspEntry.setStatus("current")
_HwMplsStaticLspName_Type = DisplayString
_HwMplsStaticLspName_Object = MibTableColumn
hwMplsStaticLspName = _HwMplsStaticLspName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 55, 1, 1),
    _HwMplsStaticLspName_Type()
)
hwMplsStaticLspName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsStaticLspName.setStatus("current")


class _HwMplsStaticLspType_Type(Integer32):
    """Custom type hwMplsStaticLspType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("egress", 3),
          ("ingress", 1),
          ("ingressBindTunnel", 4),
          ("transit", 2))
    )


_HwMplsStaticLspType_Type.__name__ = "Integer32"
_HwMplsStaticLspType_Object = MibTableColumn
hwMplsStaticLspType = _HwMplsStaticLspType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 55, 1, 11),
    _HwMplsStaticLspType_Type()
)
hwMplsStaticLspType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsStaticLspType.setStatus("current")
_HwMplsStaticLspInIntfIndex_Type = Unsigned32
_HwMplsStaticLspInIntfIndex_Object = MibTableColumn
hwMplsStaticLspInIntfIndex = _HwMplsStaticLspInIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 55, 1, 12),
    _HwMplsStaticLspInIntfIndex_Type()
)
hwMplsStaticLspInIntfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsStaticLspInIntfIndex.setStatus("current")
_HwMplsStaticLspInLabel_Type = MplsLabel
_HwMplsStaticLspInLabel_Object = MibTableColumn
hwMplsStaticLspInLabel = _HwMplsStaticLspInLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 55, 1, 13),
    _HwMplsStaticLspInLabel_Type()
)
hwMplsStaticLspInLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsStaticLspInLabel.setStatus("current")
_HwMplsStaticLspLsrId_Type = IpAddress
_HwMplsStaticLspLsrId_Object = MibTableColumn
hwMplsStaticLspLsrId = _HwMplsStaticLspLsrId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 55, 1, 14),
    _HwMplsStaticLspLsrId_Type()
)
hwMplsStaticLspLsrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsStaticLspLsrId.setStatus("current")
_HwMplsStaticLspTunnelID_Type = Unsigned32
_HwMplsStaticLspTunnelID_Object = MibTableColumn
hwMplsStaticLspTunnelID = _HwMplsStaticLspTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 55, 1, 15),
    _HwMplsStaticLspTunnelID_Type()
)
hwMplsStaticLspTunnelID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsStaticLspTunnelID.setStatus("current")
_HwMplsStaticLspNextHop_Type = IpAddress
_HwMplsStaticLspNextHop_Object = MibTableColumn
hwMplsStaticLspNextHop = _HwMplsStaticLspNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 55, 1, 16),
    _HwMplsStaticLspNextHop_Type()
)
hwMplsStaticLspNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsStaticLspNextHop.setStatus("current")
_HwMplsStaticLspOutIntfIndex_Type = Unsigned32
_HwMplsStaticLspOutIntfIndex_Object = MibTableColumn
hwMplsStaticLspOutIntfIndex = _HwMplsStaticLspOutIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 55, 1, 17),
    _HwMplsStaticLspOutIntfIndex_Type()
)
hwMplsStaticLspOutIntfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsStaticLspOutIntfIndex.setStatus("current")
_HwMplsStaticLspOutLabel_Type = MplsLabel
_HwMplsStaticLspOutLabel_Object = MibTableColumn
hwMplsStaticLspOutLabel = _HwMplsStaticLspOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 55, 1, 18),
    _HwMplsStaticLspOutLabel_Type()
)
hwMplsStaticLspOutLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsStaticLspOutLabel.setStatus("current")
_HwMplsStaticLspDestAddr_Type = IpAddress
_HwMplsStaticLspDestAddr_Object = MibTableColumn
hwMplsStaticLspDestAddr = _HwMplsStaticLspDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 55, 1, 19),
    _HwMplsStaticLspDestAddr_Type()
)
hwMplsStaticLspDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsStaticLspDestAddr.setStatus("current")
_HwMplsStaticLspMaskLen_Type = Unsigned32
_HwMplsStaticLspMaskLen_Object = MibTableColumn
hwMplsStaticLspMaskLen = _HwMplsStaticLspMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 55, 1, 20),
    _HwMplsStaticLspMaskLen_Type()
)
hwMplsStaticLspMaskLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsStaticLspMaskLen.setStatus("current")
_HwMplsStaticLspRowStatus_Type = RowStatus
_HwMplsStaticLspRowStatus_Object = MibTableColumn
hwMplsStaticLspRowStatus = _HwMplsStaticLspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 55, 1, 51),
    _HwMplsStaticLspRowStatus_Type()
)
hwMplsStaticLspRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsStaticLspRowStatus.setStatus("current")
_HwMplsLsrExtConformance_ObjectIdentity = ObjectIdentity
hwMplsLsrExtConformance = _HwMplsLsrExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 2)
)
_HwMplsLsrExtCompliances_ObjectIdentity = ObjectIdentity
hwMplsLsrExtCompliances = _HwMplsLsrExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 2, 1)
)
_HwMplsLsrExtGroup_ObjectIdentity = ObjectIdentity
hwMplsLsrExtGroup = _HwMplsLsrExtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 2, 2)
)

# Managed Objects groups

hwMplsBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 2, 2, 1)
)
hwMplsBasicGroup.setObjects(
      *(("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsLsrId"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsCapabilityConfig"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsLabelAdvertise"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsStatisticsIntervalTimer"))
)
if mibBuilder.loadTexts:
    hwMplsBasicGroup.setStatus("current")

hwMplsBfdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 2, 2, 2)
)
hwMplsBfdGroup.setObjects(
      *(("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsBfdCapabilityConfig"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsBfdMinTx"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsBfdMinRx"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsBfdDetectMultiplier"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsFecListName"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsBfdTrigger"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsBfdTriggerNextHop"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsBfdTriggerInterface"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsBfdTriggerFecListName"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsFecListRowStatus"))
)
if mibBuilder.loadTexts:
    hwMplsBfdGroup.setStatus("current")

hwLdpStaticFrrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 2, 2, 3)
)
hwLdpStaticFrrGroup.setObjects(
      *(("HUAWEI-MPLSLSR-EXT-MIB", "hwLdpStaticFrrNextHop"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwLdpStaticFrrIpPrefix"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwLdpStaticFrrInterfaceRowStatus"))
)
if mibBuilder.loadTexts:
    hwLdpStaticFrrGroup.setStatus("current")

hwMplsInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 2, 2, 4)
)
hwMplsInterfaceGroup.setObjects(
      *(("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsMtu"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsInterfaceRowStatus"))
)
if mibBuilder.loadTexts:
    hwMplsInterfaceGroup.setStatus("current")

hwMplsLdpVirtualTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 2, 2, 5)
)
hwMplsLdpVirtualTunnelGroup.setObjects(
      *(("HUAWEI-MPLSLSR-EXT-MIB", "hwLdpVirtualTunnelFEC"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwLdpVirtualStatus"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwLdpXcIndexArray"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwLdpOutSegmentIndexArray"))
)
if mibBuilder.loadTexts:
    hwMplsLdpVirtualTunnelGroup.setStatus("current")

hwMplsStaticLspGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 2, 2, 7)
)
hwMplsStaticLspGroup.setObjects(
      *(("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsStaticLspType"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsStaticLspInIntfIndex"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsStaticLspInLabel"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsStaticLspLsrId"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsStaticLspTunnelID"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsStaticLspNextHop"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsStaticLspOutIntfIndex"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsStaticLspOutLabel"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsStaticLspDestAddr"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsStaticLspMaskLen"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsStaticLspRowStatus"))
)
if mibBuilder.loadTexts:
    hwMplsStaticLspGroup.setStatus("current")

hwMplsBgpBfdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 2, 2, 8)
)
hwMplsBgpBfdGroup.setObjects(
      *(("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsBgpBfdCapabilityConfig"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsBgpBfdMinTx"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsBgpBfdMinRx"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsBgpBfdDetectMultiplier"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsBgpBfdTriggerTunnel"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsBgpBfdTriggerTunnelIpprefix"))
)
if mibBuilder.loadTexts:
    hwMplsBgpBfdGroup.setStatus("current")


# Notification objects

hwMplsLdpVirtualTunnelUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 54, 1)
)
hwMplsLdpVirtualTunnelUp.setObjects(
    ("HUAWEI-MPLSLSR-EXT-MIB", "hwLdpVirtualTunnelFEC")
)
if mibBuilder.loadTexts:
    hwMplsLdpVirtualTunnelUp.setStatus(
        "current"
    )

hwMplsLdpVirtualTunnelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 1, 54, 2)
)
hwMplsLdpVirtualTunnelDown.setObjects(
    ("HUAWEI-MPLSLSR-EXT-MIB", "hwLdpVirtualTunnelFEC")
)
if mibBuilder.loadTexts:
    hwMplsLdpVirtualTunnelDown.setStatus(
        "current"
    )


# Notifications groups

hwMplsLdpVirtualTunnelNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 2, 2, 6)
)
hwMplsLdpVirtualTunnelNotificationGroup.setObjects(
      *(("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsLdpVirtualTunnelUp"),
        ("HUAWEI-MPLSLSR-EXT-MIB", "hwMplsLdpVirtualTunnelDown"))
)
if mibBuilder.loadTexts:
    hwMplsLdpVirtualTunnelNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwMplsModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 182, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwMplsModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MPLSLSR-EXT-MIB",
    **{"hwMplsLsrExtMIB": hwMplsLsrExtMIB,
       "hwMplsLsrExtObject": hwMplsLsrExtObject,
       "hwMplsLsrId": hwMplsLsrId,
       "hwMplsCapabilityConfig": hwMplsCapabilityConfig,
       "hwMplsLabelAdvertise": hwMplsLabelAdvertise,
       "hwMplsStatisticsIntervalTimer": hwMplsStatisticsIntervalTimer,
       "hwMplsBfdCapabilityConfig": hwMplsBfdCapabilityConfig,
       "hwMplsBfdMinTx": hwMplsBfdMinTx,
       "hwMplsBfdMinRx": hwMplsBfdMinRx,
       "hwMplsBfdDetectMultiplier": hwMplsBfdDetectMultiplier,
       "hwMplsFecListName": hwMplsFecListName,
       "hwMplsBfdTrigger": hwMplsBfdTrigger,
       "hwMplsBfdTriggerNextHop": hwMplsBfdTriggerNextHop,
       "hwMplsBfdTriggerInterface": hwMplsBfdTriggerInterface,
       "hwMplsBfdTriggerFecListName": hwMplsBfdTriggerFecListName,
       "hwLdpVirtualTunnelFEC": hwLdpVirtualTunnelFEC,
       "hwMplsBgpBfdCapabilityConfig": hwMplsBgpBfdCapabilityConfig,
       "hwMplsBgpBfdMinTx": hwMplsBgpBfdMinTx,
       "hwMplsBgpBfdMinRx": hwMplsBgpBfdMinRx,
       "hwMplsBgpBfdDetectMultiplier": hwMplsBgpBfdDetectMultiplier,
       "hwMplsBgpBfdTriggerTunnel": hwMplsBgpBfdTriggerTunnel,
       "hwMplsBgpBfdTriggerTunnelIpprefix": hwMplsBgpBfdTriggerTunnelIpprefix,
       "hwMplsFecListTable": hwMplsFecListTable,
       "hwMplsFecListEntry": hwMplsFecListEntry,
       "hwMplsFecNodeIpAddress": hwMplsFecNodeIpAddress,
       "hwMplsFecNodeInterface": hwMplsFecNodeInterface,
       "hwMplsFecNodeNextHop": hwMplsFecNodeNextHop,
       "hwMplsFecListRowStatus": hwMplsFecListRowStatus,
       "hwMplsInterfaceTable": hwMplsInterfaceTable,
       "hwMplsInterfaceEntry": hwMplsInterfaceEntry,
       "hwMplsInterfaceIndex": hwMplsInterfaceIndex,
       "hwMplsMtu": hwMplsMtu,
       "hwMplsInterfaceRowStatus": hwMplsInterfaceRowStatus,
       "hwLdpStaticFrrInterfaceTable": hwLdpStaticFrrInterfaceTable,
       "hwLdpStaticFrrInterfaceEntry": hwLdpStaticFrrInterfaceEntry,
       "hwLdpStaticFrrPriority": hwLdpStaticFrrPriority,
       "hwLdpStaticFrrNextHop": hwLdpStaticFrrNextHop,
       "hwLdpStaticFrrIpPrefix": hwLdpStaticFrrIpPrefix,
       "hwLdpStaticFrrInterfaceRowStatus": hwLdpStaticFrrInterfaceRowStatus,
       "hwLdpVirtualTunnelTable": hwLdpVirtualTunnelTable,
       "hwLdpVirtualTunnelEntry": hwLdpVirtualTunnelEntry,
       "hwLdpVirtualTunnelIndex": hwLdpVirtualTunnelIndex,
       "hwLdpVirtualStatus": hwLdpVirtualStatus,
       "hwLdpXcIndexArray": hwLdpXcIndexArray,
       "hwLdpOutSegmentIndexArray": hwLdpOutSegmentIndexArray,
       "hwLdpVirtualTunnelTrap": hwLdpVirtualTunnelTrap,
       "hwMplsLdpVirtualTunnelUp": hwMplsLdpVirtualTunnelUp,
       "hwMplsLdpVirtualTunnelDown": hwMplsLdpVirtualTunnelDown,
       "hwMplsStaticLspTable": hwMplsStaticLspTable,
       "hwMplsStaticLspEntry": hwMplsStaticLspEntry,
       "hwMplsStaticLspName": hwMplsStaticLspName,
       "hwMplsStaticLspType": hwMplsStaticLspType,
       "hwMplsStaticLspInIntfIndex": hwMplsStaticLspInIntfIndex,
       "hwMplsStaticLspInLabel": hwMplsStaticLspInLabel,
       "hwMplsStaticLspLsrId": hwMplsStaticLspLsrId,
       "hwMplsStaticLspTunnelID": hwMplsStaticLspTunnelID,
       "hwMplsStaticLspNextHop": hwMplsStaticLspNextHop,
       "hwMplsStaticLspOutIntfIndex": hwMplsStaticLspOutIntfIndex,
       "hwMplsStaticLspOutLabel": hwMplsStaticLspOutLabel,
       "hwMplsStaticLspDestAddr": hwMplsStaticLspDestAddr,
       "hwMplsStaticLspMaskLen": hwMplsStaticLspMaskLen,
       "hwMplsStaticLspRowStatus": hwMplsStaticLspRowStatus,
       "hwMplsLsrExtConformance": hwMplsLsrExtConformance,
       "hwMplsLsrExtCompliances": hwMplsLsrExtCompliances,
       "hwMplsModuleCompliance": hwMplsModuleCompliance,
       "hwMplsLsrExtGroup": hwMplsLsrExtGroup,
       "hwMplsBasicGroup": hwMplsBasicGroup,
       "hwMplsBfdGroup": hwMplsBfdGroup,
       "hwLdpStaticFrrGroup": hwLdpStaticFrrGroup,
       "hwMplsInterfaceGroup": hwMplsInterfaceGroup,
       "hwMplsLdpVirtualTunnelGroup": hwMplsLdpVirtualTunnelGroup,
       "hwMplsLdpVirtualTunnelNotificationGroup": hwMplsLdpVirtualTunnelNotificationGroup,
       "hwMplsStaticLspGroup": hwMplsStaticLspGroup,
       "hwMplsBgpBfdGroup": hwMplsBgpBfdGroup}
)
