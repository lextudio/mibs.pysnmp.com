# SNMP MIB module (HP-LOADBALANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-LOADBALANCE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:33 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfLoadBalanceMod = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76)
)
hpicfLoadBalanceMod.setRevisions(
        ("2011-03-22 22:22",
         "2010-06-22 22:22")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfLoadBalanceNotifications_ObjectIdentity = ObjectIdentity
hpicfLoadBalanceNotifications = _HpicfLoadBalanceNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 0)
)
_HpicfLoadBalanceMethodMod_ObjectIdentity = ObjectIdentity
hpicfLoadBalanceMethodMod = _HpicfLoadBalanceMethodMod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1)
)


class _HpicfTrunkLoadBalanceMethod_Type(Integer32):
    """Custom type hpicfTrunkLoadBalanceMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l2based", 3),
          ("l3based", 1),
          ("l4based", 2))
    )


_HpicfTrunkLoadBalanceMethod_Type.__name__ = "Integer32"
_HpicfTrunkLoadBalanceMethod_Object = MibScalar
hpicfTrunkLoadBalanceMethod = _HpicfTrunkLoadBalanceMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 1),
    _HpicfTrunkLoadBalanceMethod_Type()
)
hpicfTrunkLoadBalanceMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfTrunkLoadBalanceMethod.setStatus("current")
_HpicfTrunkClearStatsTable_Object = MibTable
hpicfTrunkClearStatsTable = _HpicfTrunkClearStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfTrunkClearStatsTable.setStatus("current")
_HpicfTrunkClearStatsEntry_Object = MibTableRow
hpicfTrunkClearStatsEntry = _HpicfTrunkClearStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 2, 1)
)
hpicfTrunkClearStatsEntry.setIndexNames(
    (0, "HP-LOADBALANCE-MIB", "hpicfTrunkId"),
)
if mibBuilder.loadTexts:
    hpicfTrunkClearStatsEntry.setStatus("current")


class _HpicfTrunkId_Type(Integer32):
    """Custom type hpicfTrunkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfTrunkId_Type.__name__ = "Integer32"
_HpicfTrunkId_Object = MibTableColumn
hpicfTrunkId = _HpicfTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 2, 1, 1),
    _HpicfTrunkId_Type()
)
hpicfTrunkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfTrunkId.setStatus("current")
_HpicfTrunkStatsClear_Type = TruthValue
_HpicfTrunkStatsClear_Object = MibTableColumn
hpicfTrunkStatsClear = _HpicfTrunkStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 2, 1, 2),
    _HpicfTrunkStatsClear_Type()
)
hpicfTrunkStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfTrunkStatsClear.setStatus("current")
_HpicfTrunkStatsTable_Object = MibTable
hpicfTrunkStatsTable = _HpicfTrunkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfTrunkStatsTable.setStatus("current")
_HpicfTrunkStatsEntry_Object = MibTableRow
hpicfTrunkStatsEntry = _HpicfTrunkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 3, 1)
)
hpicfTrunkStatsEntry.setIndexNames(
    (0, "HP-LOADBALANCE-MIB", "hpicfTrunkId"),
)
if mibBuilder.loadTexts:
    hpicfTrunkStatsEntry.setStatus("current")
_HpicfTrunkUpTime_Type = Unsigned32
_HpicfTrunkUpTime_Object = MibTableColumn
hpicfTrunkUpTime = _HpicfTrunkUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 3, 1, 1),
    _HpicfTrunkUpTime_Type()
)
hpicfTrunkUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfTrunkUpTime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfTrunkUpTime.setUnits("minutes")
_HpicfTrunkTotalBytesRx_Type = Counter64
_HpicfTrunkTotalBytesRx_Object = MibTableColumn
hpicfTrunkTotalBytesRx = _HpicfTrunkTotalBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 3, 1, 2),
    _HpicfTrunkTotalBytesRx_Type()
)
hpicfTrunkTotalBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfTrunkTotalBytesRx.setStatus("current")
if mibBuilder.loadTexts:
    hpicfTrunkTotalBytesRx.setUnits("Bytes")
_HpicfTrunkTotalBytesTx_Type = Counter64
_HpicfTrunkTotalBytesTx_Object = MibTableColumn
hpicfTrunkTotalBytesTx = _HpicfTrunkTotalBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 3, 1, 3),
    _HpicfTrunkTotalBytesTx_Type()
)
hpicfTrunkTotalBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfTrunkTotalBytesTx.setStatus("current")
if mibBuilder.loadTexts:
    hpicfTrunkTotalBytesTx.setUnits("Bytes")
_HpicfTrunkTotalFramesRx_Type = Counter64
_HpicfTrunkTotalFramesRx_Object = MibTableColumn
hpicfTrunkTotalFramesRx = _HpicfTrunkTotalFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 3, 1, 4),
    _HpicfTrunkTotalFramesRx_Type()
)
hpicfTrunkTotalFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfTrunkTotalFramesRx.setStatus("current")
if mibBuilder.loadTexts:
    hpicfTrunkTotalFramesRx.setUnits("Frames")
_HpicfTrunkTotalFramesTx_Type = Counter64
_HpicfTrunkTotalFramesTx_Object = MibTableColumn
hpicfTrunkTotalFramesTx = _HpicfTrunkTotalFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 3, 1, 5),
    _HpicfTrunkTotalFramesTx_Type()
)
hpicfTrunkTotalFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfTrunkTotalFramesTx.setStatus("current")
if mibBuilder.loadTexts:
    hpicfTrunkTotalFramesTx.setUnits("Frames")
_HpicfTrunkTotalDropsTx_Type = Counter64
_HpicfTrunkTotalDropsTx_Object = MibTableColumn
hpicfTrunkTotalDropsTx = _HpicfTrunkTotalDropsTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 3, 1, 6),
    _HpicfTrunkTotalDropsTx_Type()
)
hpicfTrunkTotalDropsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfTrunkTotalDropsTx.setStatus("current")
if mibBuilder.loadTexts:
    hpicfTrunkTotalDropsTx.setUnits("Frames")
_HpicfTrunkPortStatsTable_Object = MibTable
hpicfTrunkPortStatsTable = _HpicfTrunkPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfTrunkPortStatsTable.setStatus("current")
_HpicfTrunkPortStatsEntry_Object = MibTableRow
hpicfTrunkPortStatsEntry = _HpicfTrunkPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 4, 1)
)
hpicfTrunkPortStatsEntry.setIndexNames(
    (0, "HP-LOADBALANCE-MIB", "hpicfTrunkId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfTrunkPortStatsEntry.setStatus("current")
_HpicfTrunkPortBytesRx_Type = Counter64
_HpicfTrunkPortBytesRx_Object = MibTableColumn
hpicfTrunkPortBytesRx = _HpicfTrunkPortBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 4, 1, 1),
    _HpicfTrunkPortBytesRx_Type()
)
hpicfTrunkPortBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfTrunkPortBytesRx.setStatus("current")
if mibBuilder.loadTexts:
    hpicfTrunkPortBytesRx.setUnits("Bytes")
_HpicfTrunkPortBytesTx_Type = Counter64
_HpicfTrunkPortBytesTx_Object = MibTableColumn
hpicfTrunkPortBytesTx = _HpicfTrunkPortBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 4, 1, 2),
    _HpicfTrunkPortBytesTx_Type()
)
hpicfTrunkPortBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfTrunkPortBytesTx.setStatus("current")
if mibBuilder.loadTexts:
    hpicfTrunkPortBytesTx.setUnits("Bytes")
_HpicfTrunkPortFramesRx_Type = Counter64
_HpicfTrunkPortFramesRx_Object = MibTableColumn
hpicfTrunkPortFramesRx = _HpicfTrunkPortFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 4, 1, 3),
    _HpicfTrunkPortFramesRx_Type()
)
hpicfTrunkPortFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfTrunkPortFramesRx.setStatus("current")
if mibBuilder.loadTexts:
    hpicfTrunkPortFramesRx.setUnits("Frames")
_HpicfTrunkPortFramesTx_Type = Counter64
_HpicfTrunkPortFramesTx_Object = MibTableColumn
hpicfTrunkPortFramesTx = _HpicfTrunkPortFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 4, 1, 4),
    _HpicfTrunkPortFramesTx_Type()
)
hpicfTrunkPortFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfTrunkPortFramesTx.setStatus("current")
if mibBuilder.loadTexts:
    hpicfTrunkPortFramesTx.setUnits("Frames")
_HpicfTrunkPortFramesDropTx_Type = Counter64
_HpicfTrunkPortFramesDropTx_Object = MibTableColumn
hpicfTrunkPortFramesDropTx = _HpicfTrunkPortFramesDropTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 4, 1, 5),
    _HpicfTrunkPortFramesDropTx_Type()
)
hpicfTrunkPortFramesDropTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfTrunkPortFramesDropTx.setStatus("current")
if mibBuilder.loadTexts:
    hpicfTrunkPortFramesDropTx.setUnits("Frames")
_HpicfTrunkPortRxFramePercent_Type = Unsigned32
_HpicfTrunkPortRxFramePercent_Object = MibTableColumn
hpicfTrunkPortRxFramePercent = _HpicfTrunkPortRxFramePercent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 4, 1, 6),
    _HpicfTrunkPortRxFramePercent_Type()
)
hpicfTrunkPortRxFramePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfTrunkPortRxFramePercent.setStatus("current")
if mibBuilder.loadTexts:
    hpicfTrunkPortRxFramePercent.setUnits("Percent")
_HpicfTrunkPortTxFramePercent_Type = Unsigned32
_HpicfTrunkPortTxFramePercent_Object = MibTableColumn
hpicfTrunkPortTxFramePercent = _HpicfTrunkPortTxFramePercent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 4, 1, 7),
    _HpicfTrunkPortTxFramePercent_Type()
)
hpicfTrunkPortTxFramePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfTrunkPortTxFramePercent.setStatus("current")
if mibBuilder.loadTexts:
    hpicfTrunkPortTxFramePercent.setUnits("Percent")
_HpicfTrunkPortDropTxFramePercent_Type = Unsigned32
_HpicfTrunkPortDropTxFramePercent_Object = MibTableColumn
hpicfTrunkPortDropTxFramePercent = _HpicfTrunkPortDropTxFramePercent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 4, 1, 8),
    _HpicfTrunkPortDropTxFramePercent_Type()
)
hpicfTrunkPortDropTxFramePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfTrunkPortDropTxFramePercent.setStatus("current")
_HpicfLoadBalanceObjects_ObjectIdentity = ObjectIdentity
hpicfLoadBalanceObjects = _HpicfLoadBalanceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5)
)
_HpicfLoadBalanceTable_Object = MibTable
hpicfLoadBalanceTable = _HpicfLoadBalanceTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hpicfLoadBalanceTable.setStatus("current")
_HpicfLoadBalanceEntry_Object = MibTableRow
hpicfLoadBalanceEntry = _HpicfLoadBalanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1)
)
hpicfLoadBalanceEntry.setIndexNames(
    (0, "HP-LOADBALANCE-MIB", "hpicfLoadBalanceIndex"),
)
if mibBuilder.loadTexts:
    hpicfLoadBalanceEntry.setStatus("current")


class _HpicfLoadBalanceIndex_Type(Integer32):
    """Custom type hpicfLoadBalanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfLoadBalanceIndex_Type.__name__ = "Integer32"
_HpicfLoadBalanceIndex_Object = MibTableColumn
hpicfLoadBalanceIndex = _HpicfLoadBalanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 1),
    _HpicfLoadBalanceIndex_Type()
)
hpicfLoadBalanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfLoadBalanceIndex.setStatus("current")
_HpicfLoadBalanceTrunkId_Type = InterfaceIndex
_HpicfLoadBalanceTrunkId_Object = MibTableColumn
hpicfLoadBalanceTrunkId = _HpicfLoadBalanceTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 2),
    _HpicfLoadBalanceTrunkId_Type()
)
hpicfLoadBalanceTrunkId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLoadBalanceTrunkId.setStatus("current")
_HpicfLoadBalanceSourceMacAddr_Type = MacAddress
_HpicfLoadBalanceSourceMacAddr_Object = MibTableColumn
hpicfLoadBalanceSourceMacAddr = _HpicfLoadBalanceSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 3),
    _HpicfLoadBalanceSourceMacAddr_Type()
)
hpicfLoadBalanceSourceMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLoadBalanceSourceMacAddr.setStatus("current")
_HpicfLoadBalanceDestMacAddr_Type = MacAddress
_HpicfLoadBalanceDestMacAddr_Object = MibTableColumn
hpicfLoadBalanceDestMacAddr = _HpicfLoadBalanceDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 4),
    _HpicfLoadBalanceDestMacAddr_Type()
)
hpicfLoadBalanceDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLoadBalanceDestMacAddr.setStatus("current")
_HpicfLoadBalanceIPSourceAddrType_Type = InetAddressType
_HpicfLoadBalanceIPSourceAddrType_Object = MibTableColumn
hpicfLoadBalanceIPSourceAddrType = _HpicfLoadBalanceIPSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 5),
    _HpicfLoadBalanceIPSourceAddrType_Type()
)
hpicfLoadBalanceIPSourceAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLoadBalanceIPSourceAddrType.setStatus("current")


class _HpicfLoadBalanceIPSourceAddr_Type(InetAddress):
    """Custom type hpicfLoadBalanceIPSourceAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_HpicfLoadBalanceIPSourceAddr_Type.__name__ = "InetAddress"
_HpicfLoadBalanceIPSourceAddr_Object = MibTableColumn
hpicfLoadBalanceIPSourceAddr = _HpicfLoadBalanceIPSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 6),
    _HpicfLoadBalanceIPSourceAddr_Type()
)
hpicfLoadBalanceIPSourceAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLoadBalanceIPSourceAddr.setStatus("current")
_HpicfLoadBalanceIPDestAddrType_Type = InetAddressType
_HpicfLoadBalanceIPDestAddrType_Object = MibTableColumn
hpicfLoadBalanceIPDestAddrType = _HpicfLoadBalanceIPDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 7),
    _HpicfLoadBalanceIPDestAddrType_Type()
)
hpicfLoadBalanceIPDestAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLoadBalanceIPDestAddrType.setStatus("current")


class _HpicfLoadBalanceIPDestAddr_Type(InetAddress):
    """Custom type hpicfLoadBalanceIPDestAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_HpicfLoadBalanceIPDestAddr_Type.__name__ = "InetAddress"
_HpicfLoadBalanceIPDestAddr_Object = MibTableColumn
hpicfLoadBalanceIPDestAddr = _HpicfLoadBalanceIPDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 8),
    _HpicfLoadBalanceIPDestAddr_Type()
)
hpicfLoadBalanceIPDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLoadBalanceIPDestAddr.setStatus("current")
_HpicfLoadBalanceSourcePort_Type = Integer32
_HpicfLoadBalanceSourcePort_Object = MibTableColumn
hpicfLoadBalanceSourcePort = _HpicfLoadBalanceSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 9),
    _HpicfLoadBalanceSourcePort_Type()
)
hpicfLoadBalanceSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLoadBalanceSourcePort.setStatus("current")
_HpicfLoadBalanceDestPort_Type = Integer32
_HpicfLoadBalanceDestPort_Object = MibTableColumn
hpicfLoadBalanceDestPort = _HpicfLoadBalanceDestPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 10),
    _HpicfLoadBalanceDestPort_Type()
)
hpicfLoadBalanceDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLoadBalanceDestPort.setStatus("current")
_HpicfLoadBalanceEtherType_Type = Integer32
_HpicfLoadBalanceEtherType_Object = MibTableColumn
hpicfLoadBalanceEtherType = _HpicfLoadBalanceEtherType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 11),
    _HpicfLoadBalanceEtherType_Type()
)
hpicfLoadBalanceEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLoadBalanceEtherType.setStatus("current")
_HpicfLoadBalanceInboundVlan_Type = Integer32
_HpicfLoadBalanceInboundVlan_Object = MibTableColumn
hpicfLoadBalanceInboundVlan = _HpicfLoadBalanceInboundVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 12),
    _HpicfLoadBalanceInboundVlan_Type()
)
hpicfLoadBalanceInboundVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLoadBalanceInboundVlan.setStatus("current")
_HpicfLoadBalanceInboundPort_Type = InterfaceIndex
_HpicfLoadBalanceInboundPort_Object = MibTableColumn
hpicfLoadBalanceInboundPort = _HpicfLoadBalanceInboundPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 13),
    _HpicfLoadBalanceInboundPort_Type()
)
hpicfLoadBalanceInboundPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLoadBalanceInboundPort.setStatus("current")
_HpicfLoadBalanceOutboundPort_Type = InterfaceIndex
_HpicfLoadBalanceOutboundPort_Object = MibTableColumn
hpicfLoadBalanceOutboundPort = _HpicfLoadBalanceOutboundPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 14),
    _HpicfLoadBalanceOutboundPort_Type()
)
hpicfLoadBalanceOutboundPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfLoadBalanceOutboundPort.setStatus("current")
_HpicfLoadBalanceStatus_Type = RowStatus
_HpicfLoadBalanceStatus_Object = MibTableColumn
hpicfLoadBalanceStatus = _HpicfLoadBalanceStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 15),
    _HpicfLoadBalanceStatus_Type()
)
hpicfLoadBalanceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLoadBalanceStatus.setStatus("current")
_HpicfLoadBalanceConformance_ObjectIdentity = ObjectIdentity
hpicfLoadBalanceConformance = _HpicfLoadBalanceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 2)
)
_HpicfLoadBalanceCompliances_ObjectIdentity = ObjectIdentity
hpicfLoadBalanceCompliances = _HpicfLoadBalanceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 2, 1)
)
_HpicfLoadBalanceGroups_ObjectIdentity = ObjectIdentity
hpicfLoadBalanceGroups = _HpicfLoadBalanceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 2, 2)
)

# Managed Objects groups

hpicfLoadBalanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 2, 2, 1)
)
hpicfLoadBalanceGroup.setObjects(
    ("HP-LOADBALANCE-MIB", "hpicfTrunkLoadBalanceMethod")
)
if mibBuilder.loadTexts:
    hpicfLoadBalanceGroup.setStatus("current")

hpicfTrunkStatsClearGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 2, 2, 2)
)
hpicfTrunkStatsClearGroup.setObjects(
    ("HP-LOADBALANCE-MIB", "hpicfTrunkStatsClear")
)
if mibBuilder.loadTexts:
    hpicfTrunkStatsClearGroup.setStatus("current")

hpicfTrunkStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 2, 2, 3)
)
hpicfTrunkStatsGroup.setObjects(
      *(("HP-LOADBALANCE-MIB", "hpicfTrunkUpTime"),
        ("HP-LOADBALANCE-MIB", "hpicfTrunkTotalBytesRx"),
        ("HP-LOADBALANCE-MIB", "hpicfTrunkTotalBytesTx"),
        ("HP-LOADBALANCE-MIB", "hpicfTrunkTotalFramesTx"),
        ("HP-LOADBALANCE-MIB", "hpicfTrunkTotalFramesRx"),
        ("HP-LOADBALANCE-MIB", "hpicfTrunkTotalDropsTx"))
)
if mibBuilder.loadTexts:
    hpicfTrunkStatsGroup.setStatus("current")

hpicfTrunkPortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 2, 2, 4)
)
hpicfTrunkPortStatsGroup.setObjects(
      *(("HP-LOADBALANCE-MIB", "hpicfTrunkPortBytesRx"),
        ("HP-LOADBALANCE-MIB", "hpicfTrunkPortBytesTx"),
        ("HP-LOADBALANCE-MIB", "hpicfTrunkPortFramesRx"),
        ("HP-LOADBALANCE-MIB", "hpicfTrunkPortFramesTx"),
        ("HP-LOADBALANCE-MIB", "hpicfTrunkPortFramesDropTx"),
        ("HP-LOADBALANCE-MIB", "hpicfTrunkPortRxFramePercent"),
        ("HP-LOADBALANCE-MIB", "hpicfTrunkPortTxFramePercent"),
        ("HP-LOADBALANCE-MIB", "hpicfTrunkPortDropTxFramePercent"))
)
if mibBuilder.loadTexts:
    hpicfTrunkPortStatsGroup.setStatus("current")

hpicfLoadBalanceGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 2, 2, 5)
)
hpicfLoadBalanceGroup5.setObjects(
      *(("HP-LOADBALANCE-MIB", "hpicfLoadBalanceTrunkId"),
        ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceSourceMacAddr"),
        ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceDestMacAddr"),
        ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceIPSourceAddrType"),
        ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceIPSourceAddr"),
        ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceIPDestAddrType"),
        ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceIPDestAddr"),
        ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceSourcePort"),
        ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceDestPort"),
        ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceEtherType"),
        ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceInboundVlan"),
        ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceInboundPort"),
        ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceOutboundPort"),
        ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceStatus"))
)
if mibBuilder.loadTexts:
    hpicfLoadBalanceGroup5.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfLoadBalanceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfLoadBalanceCompliance.setStatus(
        "current"
    )

hpicfTrunkStatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfTrunkStatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-LOADBALANCE-MIB",
    **{"hpicfLoadBalanceMod": hpicfLoadBalanceMod,
       "hpicfLoadBalanceNotifications": hpicfLoadBalanceNotifications,
       "hpicfLoadBalanceMethodMod": hpicfLoadBalanceMethodMod,
       "hpicfTrunkLoadBalanceMethod": hpicfTrunkLoadBalanceMethod,
       "hpicfTrunkClearStatsTable": hpicfTrunkClearStatsTable,
       "hpicfTrunkClearStatsEntry": hpicfTrunkClearStatsEntry,
       "hpicfTrunkId": hpicfTrunkId,
       "hpicfTrunkStatsClear": hpicfTrunkStatsClear,
       "hpicfTrunkStatsTable": hpicfTrunkStatsTable,
       "hpicfTrunkStatsEntry": hpicfTrunkStatsEntry,
       "hpicfTrunkUpTime": hpicfTrunkUpTime,
       "hpicfTrunkTotalBytesRx": hpicfTrunkTotalBytesRx,
       "hpicfTrunkTotalBytesTx": hpicfTrunkTotalBytesTx,
       "hpicfTrunkTotalFramesRx": hpicfTrunkTotalFramesRx,
       "hpicfTrunkTotalFramesTx": hpicfTrunkTotalFramesTx,
       "hpicfTrunkTotalDropsTx": hpicfTrunkTotalDropsTx,
       "hpicfTrunkPortStatsTable": hpicfTrunkPortStatsTable,
       "hpicfTrunkPortStatsEntry": hpicfTrunkPortStatsEntry,
       "hpicfTrunkPortBytesRx": hpicfTrunkPortBytesRx,
       "hpicfTrunkPortBytesTx": hpicfTrunkPortBytesTx,
       "hpicfTrunkPortFramesRx": hpicfTrunkPortFramesRx,
       "hpicfTrunkPortFramesTx": hpicfTrunkPortFramesTx,
       "hpicfTrunkPortFramesDropTx": hpicfTrunkPortFramesDropTx,
       "hpicfTrunkPortRxFramePercent": hpicfTrunkPortRxFramePercent,
       "hpicfTrunkPortTxFramePercent": hpicfTrunkPortTxFramePercent,
       "hpicfTrunkPortDropTxFramePercent": hpicfTrunkPortDropTxFramePercent,
       "hpicfLoadBalanceObjects": hpicfLoadBalanceObjects,
       "hpicfLoadBalanceTable": hpicfLoadBalanceTable,
       "hpicfLoadBalanceEntry": hpicfLoadBalanceEntry,
       "hpicfLoadBalanceIndex": hpicfLoadBalanceIndex,
       "hpicfLoadBalanceTrunkId": hpicfLoadBalanceTrunkId,
       "hpicfLoadBalanceSourceMacAddr": hpicfLoadBalanceSourceMacAddr,
       "hpicfLoadBalanceDestMacAddr": hpicfLoadBalanceDestMacAddr,
       "hpicfLoadBalanceIPSourceAddrType": hpicfLoadBalanceIPSourceAddrType,
       "hpicfLoadBalanceIPSourceAddr": hpicfLoadBalanceIPSourceAddr,
       "hpicfLoadBalanceIPDestAddrType": hpicfLoadBalanceIPDestAddrType,
       "hpicfLoadBalanceIPDestAddr": hpicfLoadBalanceIPDestAddr,
       "hpicfLoadBalanceSourcePort": hpicfLoadBalanceSourcePort,
       "hpicfLoadBalanceDestPort": hpicfLoadBalanceDestPort,
       "hpicfLoadBalanceEtherType": hpicfLoadBalanceEtherType,
       "hpicfLoadBalanceInboundVlan": hpicfLoadBalanceInboundVlan,
       "hpicfLoadBalanceInboundPort": hpicfLoadBalanceInboundPort,
       "hpicfLoadBalanceOutboundPort": hpicfLoadBalanceOutboundPort,
       "hpicfLoadBalanceStatus": hpicfLoadBalanceStatus,
       "hpicfLoadBalanceConformance": hpicfLoadBalanceConformance,
       "hpicfLoadBalanceCompliances": hpicfLoadBalanceCompliances,
       "hpicfLoadBalanceCompliance": hpicfLoadBalanceCompliance,
       "hpicfTrunkStatsCompliance": hpicfTrunkStatsCompliance,
       "hpicfLoadBalanceGroups": hpicfLoadBalanceGroups,
       "hpicfLoadBalanceGroup": hpicfLoadBalanceGroup,
       "hpicfTrunkStatsClearGroup": hpicfTrunkStatsClearGroup,
       "hpicfTrunkStatsGroup": hpicfTrunkStatsGroup,
       "hpicfTrunkPortStatsGroup": hpicfTrunkPortStatsGroup,
       "hpicfLoadBalanceGroup5": hpicfLoadBalanceGroup5}
)
