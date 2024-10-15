# SNMP MIB module (HUAWEI-ETHARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-ETHARP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:46 2024
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

(PhysicalIndex,
 entPhysicalIndex,
 entPhysicalName) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex",
    "entPhysicalName")

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddressIPv4,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwEthernetARPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123)
)
hwEthernetARPMIB.setRevisions(
        ("2014-04-23 10:44",
         "2013-09-07 00:00",
         "2006-06-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwEthernetARPObjects_ObjectIdentity = ObjectIdentity
hwEthernetARPObjects = _HwEthernetARPObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1)
)


class _HwEthernetARPAntiAttackLog_Type(Integer32):
    """Custom type hwEthernetARPAntiAttackLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_HwEthernetARPAntiAttackLog_Type.__name__ = "Integer32"
_HwEthernetARPAntiAttackLog_Object = MibScalar
hwEthernetARPAntiAttackLog = _HwEthernetARPAntiAttackLog_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 1),
    _HwEthernetARPAntiAttackLog_Type()
)
hwEthernetARPAntiAttackLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEthernetARPAntiAttackLog.setStatus("current")


class _HwEthernetARPLearningStrict_Type(Integer32):
    """Custom type hwEthernetARPLearningStrict based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwEthernetARPLearningStrict_Type.__name__ = "Integer32"
_HwEthernetARPLearningStrict_Object = MibScalar
hwEthernetARPLearningStrict = _HwEthernetARPLearningStrict_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 2),
    _HwEthernetARPLearningStrict_Type()
)
hwEthernetARPLearningStrict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEthernetARPLearningStrict.setStatus("current")
_HwEthernetARPSpeedLimitTable_Object = MibTable
hwEthernetARPSpeedLimitTable = _HwEthernetARPSpeedLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 3)
)
if mibBuilder.loadTexts:
    hwEthernetARPSpeedLimitTable.setStatus("current")
_HwEthernetARPSpeedLimitEntry_Object = MibTableRow
hwEthernetARPSpeedLimitEntry = _HwEthernetARPSpeedLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 3, 1)
)
hwEthernetARPSpeedLimitEntry.setIndexNames(
    (0, "HUAWEI-ETHARP-MIB", "hwEthernetARPLimitSlot"),
    (0, "HUAWEI-ETHARP-MIB", "hwEthernetARPLimitType"),
    (0, "HUAWEI-ETHARP-MIB", "hwEthernetARPLimitIPType"),
)
if mibBuilder.loadTexts:
    hwEthernetARPSpeedLimitEntry.setStatus("current")


class _HwEthernetARPLimitSlot_Type(Integer32):
    """Custom type hwEthernetARPLimitSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwEthernetARPLimitSlot_Type.__name__ = "Integer32"
_HwEthernetARPLimitSlot_Object = MibTableColumn
hwEthernetARPLimitSlot = _HwEthernetARPLimitSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 3, 1, 1),
    _HwEthernetARPLimitSlot_Type()
)
hwEthernetARPLimitSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEthernetARPLimitSlot.setStatus("current")


class _HwEthernetARPLimitType_Type(Integer32):
    """Custom type hwEthernetARPLimitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("arp", 1),
          ("arpmiss", 2))
    )


_HwEthernetARPLimitType_Type.__name__ = "Integer32"
_HwEthernetARPLimitType_Object = MibTableColumn
hwEthernetARPLimitType = _HwEthernetARPLimitType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 3, 1, 2),
    _HwEthernetARPLimitType_Type()
)
hwEthernetARPLimitType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEthernetARPLimitType.setStatus("current")


class _HwEthernetARPLimitIPType_Type(Integer32):
    """Custom type hwEthernetARPLimitIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("destinationip", 8),
          ("sourceip", 4))
    )


_HwEthernetARPLimitIPType_Type.__name__ = "Integer32"
_HwEthernetARPLimitIPType_Object = MibTableColumn
hwEthernetARPLimitIPType = _HwEthernetARPLimitIPType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 3, 1, 3),
    _HwEthernetARPLimitIPType_Type()
)
hwEthernetARPLimitIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEthernetARPLimitIPType.setStatus("current")


class _HwEthernetARPLimitSpeedValue_Type(Unsigned32):
    """Custom type hwEthernetARPLimitSpeedValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_HwEthernetARPLimitSpeedValue_Type.__name__ = "Unsigned32"
_HwEthernetARPLimitSpeedValue_Object = MibTableColumn
hwEthernetARPLimitSpeedValue = _HwEthernetARPLimitSpeedValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 3, 1, 4),
    _HwEthernetARPLimitSpeedValue_Type()
)
hwEthernetARPLimitSpeedValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEthernetARPLimitSpeedValue.setStatus("current")
_HwEthernetARPSpeedLimitIfIndex_Type = InterfaceIndex
_HwEthernetARPSpeedLimitIfIndex_Object = MibScalar
hwEthernetARPSpeedLimitIfIndex = _HwEthernetARPSpeedLimitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 4),
    _HwEthernetARPSpeedLimitIfIndex_Type()
)
hwEthernetARPSpeedLimitIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPSpeedLimitIfIndex.setStatus("current")
_HwEthernetARPSpeedLimitConfigured_Type = Counter32
_HwEthernetARPSpeedLimitConfigured_Object = MibScalar
hwEthernetARPSpeedLimitConfigured = _HwEthernetARPSpeedLimitConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 5),
    _HwEthernetARPSpeedLimitConfigured_Type()
)
hwEthernetARPSpeedLimitConfigured.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPSpeedLimitConfigured.setStatus("current")
_HwEthernetARPSpeedLimitCurrent_Type = Counter32
_HwEthernetARPSpeedLimitCurrent_Object = MibScalar
hwEthernetARPSpeedLimitCurrent = _HwEthernetARPSpeedLimitCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 6),
    _HwEthernetARPSpeedLimitCurrent_Type()
)
hwEthernetARPSpeedLimitCurrent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPSpeedLimitCurrent.setStatus("current")
_HwEthernetARPSpeedLimitType_Type = DisplayString
_HwEthernetARPSpeedLimitType_Object = MibScalar
hwEthernetARPSpeedLimitType = _HwEthernetARPSpeedLimitType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 7),
    _HwEthernetARPSpeedLimitType_Type()
)
hwEthernetARPSpeedLimitType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPSpeedLimitType.setStatus("current")
_HwEthernetARPSpeedLimitSrcIPAddr_Type = IpAddress
_HwEthernetARPSpeedLimitSrcIPAddr_Object = MibScalar
hwEthernetARPSpeedLimitSrcIPAddr = _HwEthernetARPSpeedLimitSrcIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 8),
    _HwEthernetARPSpeedLimitSrcIPAddr_Type()
)
hwEthernetARPSpeedLimitSrcIPAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPSpeedLimitSrcIPAddr.setStatus("current")
_HwEthernetARPSpeedLimitDstIPAddr_Type = IpAddress
_HwEthernetARPSpeedLimitDstIPAddr_Object = MibScalar
hwEthernetARPSpeedLimitDstIPAddr = _HwEthernetARPSpeedLimitDstIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 9),
    _HwEthernetARPSpeedLimitDstIPAddr_Type()
)
hwEthernetARPSpeedLimitDstIPAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPSpeedLimitDstIPAddr.setStatus("current")
_HwEthernetARPSpeedLimitVPNinstance_Type = DisplayString
_HwEthernetARPSpeedLimitVPNinstance_Object = MibScalar
hwEthernetARPSpeedLimitVPNinstance = _HwEthernetARPSpeedLimitVPNinstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 10),
    _HwEthernetARPSpeedLimitVPNinstance_Type()
)
hwEthernetARPSpeedLimitVPNinstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPSpeedLimitVPNinstance.setStatus("current")
_HwEthernetARPStaticsTable_Object = MibTable
hwEthernetARPStaticsTable = _HwEthernetARPStaticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 11)
)
if mibBuilder.loadTexts:
    hwEthernetARPStaticsTable.setStatus("current")
_HwEthernetARPStaticsEntry_Object = MibTableRow
hwEthernetARPStaticsEntry = _HwEthernetARPStaticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 11, 1)
)
hwEthernetARPStaticsEntry.setIndexNames(
    (0, "HUAWEI-ETHARP-MIB", "hwEthernetARPStaticsSlot"),
)
if mibBuilder.loadTexts:
    hwEthernetARPStaticsEntry.setStatus("current")


class _HwEthernetARPStaticsSlot_Type(Integer32):
    """Custom type hwEthernetARPStaticsSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
        ValueRangeConstraint(65535, 65535),
    )


_HwEthernetARPStaticsSlot_Type.__name__ = "Integer32"
_HwEthernetARPStaticsSlot_Object = MibTableColumn
hwEthernetARPStaticsSlot = _HwEthernetARPStaticsSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 11, 1, 1),
    _HwEthernetARPStaticsSlot_Type()
)
hwEthernetARPStaticsSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEthernetARPStaticsSlot.setStatus("current")
_HwEthernetARPStaticsLearnTotal_Type = Counter32
_HwEthernetARPStaticsLearnTotal_Object = MibTableColumn
hwEthernetARPStaticsLearnTotal = _HwEthernetARPStaticsLearnTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 11, 1, 2),
    _HwEthernetARPStaticsLearnTotal_Type()
)
hwEthernetARPStaticsLearnTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEthernetARPStaticsLearnTotal.setStatus("current")
_HwEthernetARPDropForLimit_Type = Counter32
_HwEthernetARPDropForLimit_Object = MibTableColumn
hwEthernetARPDropForLimit = _HwEthernetARPDropForLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 11, 1, 3),
    _HwEthernetARPDropForLimit_Type()
)
hwEthernetARPDropForLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEthernetARPDropForLimit.setStatus("current")
_HwEthernetARPDropForARPSuppress_Type = Counter32
_HwEthernetARPDropForARPSuppress_Object = MibTableColumn
hwEthernetARPDropForARPSuppress = _HwEthernetARPDropForARPSuppress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 11, 1, 4),
    _HwEthernetARPDropForARPSuppress_Type()
)
hwEthernetARPDropForARPSuppress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEthernetARPDropForARPSuppress.setStatus("current")
_HwEthernetARPDropForARPMissSuppress_Type = Counter32
_HwEthernetARPDropForARPMissSuppress_Object = MibTableColumn
hwEthernetARPDropForARPMissSuppress = _HwEthernetARPDropForARPMissSuppress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 11, 1, 5),
    _HwEthernetARPDropForARPMissSuppress_Type()
)
hwEthernetARPDropForARPMissSuppress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEthernetARPDropForARPMissSuppress.setStatus("current")
_HwEthernetARPDropForOther_Type = Counter32
_HwEthernetARPDropForOther_Object = MibTableColumn
hwEthernetARPDropForOther = _HwEthernetARPDropForOther_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 11, 1, 6),
    _HwEthernetARPDropForOther_Type()
)
hwEthernetARPDropForOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEthernetARPDropForOther.setStatus("current")
_HwEthernetARPMissDropForOther_Type = Counter32
_HwEthernetARPMissDropForOther_Object = MibTableColumn
hwEthernetARPMissDropForOther = _HwEthernetARPMissDropForOther_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 11, 1, 7),
    _HwEthernetARPMissDropForOther_Type()
)
hwEthernetARPMissDropForOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEthernetARPMissDropForOther.setStatus("current")
_HwEthernetARPRcvNum_Type = Counter32
_HwEthernetARPRcvNum_Object = MibTableColumn
hwEthernetARPRcvNum = _HwEthernetARPRcvNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 11, 1, 8),
    _HwEthernetARPRcvNum_Type()
)
hwEthernetARPRcvNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEthernetARPRcvNum.setStatus("current")
_HwEthernetARPMissRcvNum_Type = Counter32
_HwEthernetARPMissRcvNum_Object = MibTableColumn
hwEthernetARPMissRcvNum = _HwEthernetARPMissRcvNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 11, 1, 9),
    _HwEthernetARPMissRcvNum_Type()
)
hwEthernetARPMissRcvNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEthernetARPMissRcvNum.setStatus("current")


class _HwEthernetARPStaticsOperation_Type(Integer32):
    """Custom type hwEthernetARPStaticsOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("unused", 2))
    )


_HwEthernetARPStaticsOperation_Type.__name__ = "Integer32"
_HwEthernetARPStaticsOperation_Object = MibTableColumn
hwEthernetARPStaticsOperation = _HwEthernetARPStaticsOperation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 11, 1, 10),
    _HwEthernetARPStaticsOperation_Type()
)
hwEthernetARPStaticsOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEthernetARPStaticsOperation.setStatus("current")
_HwEthernetARPDropForARPProxySuppress_Type = Counter32
_HwEthernetARPDropForARPProxySuppress_Object = MibTableColumn
hwEthernetARPDropForARPProxySuppress = _HwEthernetARPDropForARPProxySuppress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 11, 1, 11),
    _HwEthernetARPDropForARPProxySuppress_Type()
)
hwEthernetARPDropForARPProxySuppress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEthernetARPDropForARPProxySuppress.setStatus("current")
_HwEthARPShowWithInterAndVidTable_Object = MibTable
hwEthARPShowWithInterAndVidTable = _HwEthARPShowWithInterAndVidTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 12)
)
if mibBuilder.loadTexts:
    hwEthARPShowWithInterAndVidTable.setStatus("current")
_HwEthARPShowWithInterAndVidEntry_Object = MibTableRow
hwEthARPShowWithInterAndVidEntry = _HwEthARPShowWithInterAndVidEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 12, 1)
)
hwEthARPShowWithInterAndVidEntry.setIndexNames(
    (0, "HUAWEI-ETHARP-MIB", "hwEthARPShowIfindex"),
    (0, "HUAWEI-ETHARP-MIB", "hwEthARPShowVid"),
    (0, "HUAWEI-ETHARP-MIB", "hwEthARPIpAddr"),
)
if mibBuilder.loadTexts:
    hwEthARPShowWithInterAndVidEntry.setStatus("current")
_HwEthARPShowIfindex_Type = InterfaceIndex
_HwEthARPShowIfindex_Object = MibTableColumn
hwEthARPShowIfindex = _HwEthARPShowIfindex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 12, 1, 1),
    _HwEthARPShowIfindex_Type()
)
hwEthARPShowIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEthARPShowIfindex.setStatus("current")


class _HwEthARPShowVid_Type(Integer32):
    """Custom type hwEthARPShowVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwEthARPShowVid_Type.__name__ = "Integer32"
_HwEthARPShowVid_Object = MibTableColumn
hwEthARPShowVid = _HwEthARPShowVid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 12, 1, 2),
    _HwEthARPShowVid_Type()
)
hwEthARPShowVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEthARPShowVid.setStatus("current")
_HwEthARPIpAddr_Type = IpAddress
_HwEthARPIpAddr_Object = MibTableColumn
hwEthARPIpAddr = _HwEthARPIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 12, 1, 3),
    _HwEthARPIpAddr_Type()
)
hwEthARPIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEthARPIpAddr.setStatus("current")
_HwEthARPMacAddr_Type = PhysAddress
_HwEthARPMacAddr_Object = MibTableColumn
hwEthARPMacAddr = _HwEthARPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 12, 1, 4),
    _HwEthARPMacAddr_Type()
)
hwEthARPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEthARPMacAddr.setStatus("current")
_HwEthARPLimitTable_Object = MibTable
hwEthARPLimitTable = _HwEthARPLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 13)
)
if mibBuilder.loadTexts:
    hwEthARPLimitTable.setStatus("current")
_HwEthARPLimitEntry_Object = MibTableRow
hwEthARPLimitEntry = _HwEthARPLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 13, 1)
)
hwEthARPLimitEntry.setIndexNames(
    (0, "HUAWEI-ETHARP-MIB", "hwEthARPLimitCfgIfindex"),
    (0, "HUAWEI-ETHARP-MIB", "hwEthARPVLANFirst"),
    (0, "HUAWEI-ETHARP-MIB", "hwEthARPVLANLast"),
)
if mibBuilder.loadTexts:
    hwEthARPLimitEntry.setStatus("current")
_HwEthARPLimitCfgIfindex_Type = InterfaceIndex
_HwEthARPLimitCfgIfindex_Object = MibTableColumn
hwEthARPLimitCfgIfindex = _HwEthARPLimitCfgIfindex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 13, 1, 1),
    _HwEthARPLimitCfgIfindex_Type()
)
hwEthARPLimitCfgIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEthARPLimitCfgIfindex.setStatus("current")


class _HwEthARPVLANFirst_Type(Integer32):
    """Custom type hwEthARPVLANFirst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwEthARPVLANFirst_Type.__name__ = "Integer32"
_HwEthARPVLANFirst_Object = MibTableColumn
hwEthARPVLANFirst = _HwEthARPVLANFirst_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 13, 1, 2),
    _HwEthARPVLANFirst_Type()
)
hwEthARPVLANFirst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEthARPVLANFirst.setStatus("current")


class _HwEthARPVLANLast_Type(Integer32):
    """Custom type hwEthARPVLANLast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwEthARPVLANLast_Type.__name__ = "Integer32"
_HwEthARPVLANLast_Object = MibTableColumn
hwEthARPVLANLast = _HwEthARPVLANLast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 13, 1, 3),
    _HwEthARPVLANLast_Type()
)
hwEthARPVLANLast.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEthARPVLANLast.setStatus("current")


class _HwEthARPLimitNum_Type(Integer32):
    """Custom type hwEthARPLimitNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwEthARPLimitNum_Type.__name__ = "Integer32"
_HwEthARPLimitNum_Object = MibTableColumn
hwEthARPLimitNum = _HwEthARPLimitNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 13, 1, 4),
    _HwEthARPLimitNum_Type()
)
hwEthARPLimitNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEthARPLimitNum.setStatus("current")
_HwEthARPLimitRowStatus_Type = RowStatus
_HwEthARPLimitRowStatus_Object = MibTableColumn
hwEthARPLimitRowStatus = _HwEthARPLimitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 13, 1, 5),
    _HwEthARPLimitRowStatus_Type()
)
hwEthARPLimitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEthARPLimitRowStatus.setStatus("current")
_HwEthernetARPLearningStrictInterfaceTable_Object = MibTable
hwEthernetARPLearningStrictInterfaceTable = _HwEthernetARPLearningStrictInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 14)
)
if mibBuilder.loadTexts:
    hwEthernetARPLearningStrictInterfaceTable.setStatus("current")
_HwEthernetARPLearningStrictInterfaceEntry_Object = MibTableRow
hwEthernetARPLearningStrictInterfaceEntry = _HwEthernetARPLearningStrictInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 14, 1)
)
hwEthernetARPLearningStrictInterfaceEntry.setIndexNames(
    (0, "HUAWEI-ETHARP-MIB", "hwEthernetARPLearningStrictIfindex"),
)
if mibBuilder.loadTexts:
    hwEthernetARPLearningStrictInterfaceEntry.setStatus("current")
_HwEthernetARPLearningStrictIfindex_Type = InterfaceIndex
_HwEthernetARPLearningStrictIfindex_Object = MibTableColumn
hwEthernetARPLearningStrictIfindex = _HwEthernetARPLearningStrictIfindex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 14, 1, 1),
    _HwEthernetARPLearningStrictIfindex_Type()
)
hwEthernetARPLearningStrictIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEthernetARPLearningStrictIfindex.setStatus("current")


class _HwEthernetARPLearningStrictState_Type(Integer32):
    """Custom type hwEthernetARPLearningStrictState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceDisable", 2),
          ("forceEnable", 1))
    )


_HwEthernetARPLearningStrictState_Type.__name__ = "Integer32"
_HwEthernetARPLearningStrictState_Object = MibTableColumn
hwEthernetARPLearningStrictState = _HwEthernetARPLearningStrictState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 14, 1, 2),
    _HwEthernetARPLearningStrictState_Type()
)
hwEthernetARPLearningStrictState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEthernetARPLearningStrictState.setStatus("current")
_HwEthernetARPLearningStrictRowStatus_Type = RowStatus
_HwEthernetARPLearningStrictRowStatus_Object = MibTableColumn
hwEthernetARPLearningStrictRowStatus = _HwEthernetARPLearningStrictRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 14, 1, 3),
    _HwEthernetARPLearningStrictRowStatus_Type()
)
hwEthernetARPLearningStrictRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEthernetARPLearningStrictRowStatus.setStatus("current")
_HwArpLinkInterfaceTable_Object = MibTable
hwArpLinkInterfaceTable = _HwArpLinkInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 15)
)
if mibBuilder.loadTexts:
    hwArpLinkInterfaceTable.setStatus("current")
_HwArpLinkInterfaceEntry_Object = MibTableRow
hwArpLinkInterfaceEntry = _HwArpLinkInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 15, 1)
)
hwArpLinkInterfaceEntry.setIndexNames(
    (0, "HUAWEI-ETHARP-MIB", "hwArpLinkIfIndex"),
)
if mibBuilder.loadTexts:
    hwArpLinkInterfaceEntry.setStatus("current")


class _HwArpLinkIfIndex_Type(Integer32):
    """Custom type hwArpLinkIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwArpLinkIfIndex_Type.__name__ = "Integer32"
_HwArpLinkIfIndex_Object = MibTableColumn
hwArpLinkIfIndex = _HwArpLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 15, 1, 1),
    _HwArpLinkIfIndex_Type()
)
hwArpLinkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwArpLinkIfIndex.setStatus("current")
_HwArpLinkPeerIp_Type = InetAddressIPv4
_HwArpLinkPeerIp_Object = MibTableColumn
hwArpLinkPeerIp = _HwArpLinkPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 15, 1, 11),
    _HwArpLinkPeerIp_Type()
)
hwArpLinkPeerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwArpLinkPeerIp.setStatus("current")


class _HwArpLinkDetectTime_Type(Integer32):
    """Custom type hwArpLinkDetectTime based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 10000),
    )


_HwArpLinkDetectTime_Type.__name__ = "Integer32"
_HwArpLinkDetectTime_Object = MibTableColumn
hwArpLinkDetectTime = _HwArpLinkDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 15, 1, 12),
    _HwArpLinkDetectTime_Type()
)
hwArpLinkDetectTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwArpLinkDetectTime.setStatus("current")


class _HwArpLinkDetectTimes_Type(Integer32):
    """Custom type hwArpLinkDetectTimes based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwArpLinkDetectTimes_Type.__name__ = "Integer32"
_HwArpLinkDetectTimes_Object = MibTableColumn
hwArpLinkDetectTimes = _HwArpLinkDetectTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 15, 1, 13),
    _HwArpLinkDetectTimes_Type()
)
hwArpLinkDetectTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwArpLinkDetectTimes.setStatus("current")


class _HwArpLinkDetectMode_Type(Integer32):
    """Custom type hwArpLinkDetectMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loose", 1),
          ("strict", 2))
    )


_HwArpLinkDetectMode_Type.__name__ = "Integer32"
_HwArpLinkDetectMode_Object = MibTableColumn
hwArpLinkDetectMode = _HwArpLinkDetectMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 15, 1, 14),
    _HwArpLinkDetectMode_Type()
)
hwArpLinkDetectMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwArpLinkDetectMode.setStatus("current")


class _HwArpLinkStatus_Type(Integer32):
    """Custom type hwArpLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_HwArpLinkStatus_Type.__name__ = "Integer32"
_HwArpLinkStatus_Object = MibTableColumn
hwArpLinkStatus = _HwArpLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 15, 1, 15),
    _HwArpLinkStatus_Type()
)
hwArpLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwArpLinkStatus.setStatus("current")
_HwArpLinkRowStatus_Type = RowStatus
_HwArpLinkRowStatus_Object = MibTableColumn
hwArpLinkRowStatus = _HwArpLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 15, 1, 51),
    _HwArpLinkRowStatus_Type()
)
hwArpLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwArpLinkRowStatus.setStatus("current")
_HwArpEntryExpireControlTable_Object = MibTable
hwArpEntryExpireControlTable = _HwArpEntryExpireControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 16)
)
if mibBuilder.loadTexts:
    hwArpEntryExpireControlTable.setStatus("current")
_HwArpEntryExpireControlEntry_Object = MibTableRow
hwArpEntryExpireControlEntry = _HwArpEntryExpireControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 16, 1)
)
hwArpEntryExpireControlEntry.setIndexNames(
    (0, "HUAWEI-ETHARP-MIB", "hwArpEntryExpireIfIndex"),
)
if mibBuilder.loadTexts:
    hwArpEntryExpireControlEntry.setStatus("current")
_HwArpEntryExpireIfIndex_Type = InterfaceIndex
_HwArpEntryExpireIfIndex_Object = MibTableColumn
hwArpEntryExpireIfIndex = _HwArpEntryExpireIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 16, 1, 1),
    _HwArpEntryExpireIfIndex_Type()
)
hwArpEntryExpireIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwArpEntryExpireIfIndex.setStatus("current")


class _HwArpEntryExpireDetectMode_Type(Integer32):
    """Custom type hwArpEntryExpireDetectMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("unicast", 2))
    )


_HwArpEntryExpireDetectMode_Type.__name__ = "Integer32"
_HwArpEntryExpireDetectMode_Object = MibTableColumn
hwArpEntryExpireDetectMode = _HwArpEntryExpireDetectMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 16, 1, 2),
    _HwArpEntryExpireDetectMode_Type()
)
hwArpEntryExpireDetectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwArpEntryExpireDetectMode.setStatus("current")


class _HwArpEntryExpireFakeTime_Type(Integer32):
    """Custom type hwArpEntryExpireFakeTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 36000),
    )


_HwArpEntryExpireFakeTime_Type.__name__ = "Integer32"
_HwArpEntryExpireFakeTime_Object = MibTableColumn
hwArpEntryExpireFakeTime = _HwArpEntryExpireFakeTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 16, 1, 3),
    _HwArpEntryExpireFakeTime_Type()
)
hwArpEntryExpireFakeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwArpEntryExpireFakeTime.setStatus("current")
_HwArpDynTable_Object = MibTable
hwArpDynTable = _HwArpDynTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 17)
)
if mibBuilder.loadTexts:
    hwArpDynTable.setStatus("current")
_HwArpDynEntry_Object = MibTableRow
hwArpDynEntry = _HwArpDynEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 17, 1)
)
hwArpDynEntry.setIndexNames(
    (0, "HUAWEI-ETHARP-MIB", "hwArpDynIfIndex"),
    (0, "HUAWEI-ETHARP-MIB", "hwArpDynIpAdd"),
    (0, "HUAWEI-ETHARP-MIB", "hwArpDynVrf"),
)
if mibBuilder.loadTexts:
    hwArpDynEntry.setStatus("current")


class _HwArpDynIfIndex_Type(Integer32):
    """Custom type hwArpDynIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwArpDynIfIndex_Type.__name__ = "Integer32"
_HwArpDynIfIndex_Object = MibTableColumn
hwArpDynIfIndex = _HwArpDynIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 17, 1, 1),
    _HwArpDynIfIndex_Type()
)
hwArpDynIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwArpDynIfIndex.setStatus("current")
_HwArpDynIpAdd_Type = InetAddressIPv4
_HwArpDynIpAdd_Object = MibTableColumn
hwArpDynIpAdd = _HwArpDynIpAdd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 17, 1, 2),
    _HwArpDynIpAdd_Type()
)
hwArpDynIpAdd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwArpDynIpAdd.setStatus("current")


class _HwArpDynVrf_Type(OctetString):
    """Custom type hwArpDynVrf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwArpDynVrf_Type.__name__ = "OctetString"
_HwArpDynVrf_Object = MibTableColumn
hwArpDynVrf = _HwArpDynVrf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 17, 1, 3),
    _HwArpDynVrf_Type()
)
hwArpDynVrf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwArpDynVrf.setStatus("current")
_HwArpDynMacAdd_Type = PhysAddress
_HwArpDynMacAdd_Object = MibTableColumn
hwArpDynMacAdd = _HwArpDynMacAdd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 17, 1, 11),
    _HwArpDynMacAdd_Type()
)
hwArpDynMacAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwArpDynMacAdd.setStatus("current")


class _HwArpDynVlanId_Type(Integer32):
    """Custom type hwArpDynVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_HwArpDynVlanId_Type.__name__ = "Integer32"
_HwArpDynVlanId_Object = MibTableColumn
hwArpDynVlanId = _HwArpDynVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 17, 1, 12),
    _HwArpDynVlanId_Type()
)
hwArpDynVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwArpDynVlanId.setStatus("current")


class _HwArpDynCeVlanId_Type(Integer32):
    """Custom type hwArpDynCeVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_HwArpDynCeVlanId_Type.__name__ = "Integer32"
_HwArpDynCeVlanId_Object = MibTableColumn
hwArpDynCeVlanId = _HwArpDynCeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 17, 1, 13),
    _HwArpDynCeVlanId_Type()
)
hwArpDynCeVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwArpDynCeVlanId.setStatus("current")
_HwArpDynOutIfIndex_Type = InterfaceIndex
_HwArpDynOutIfIndex_Object = MibTableColumn
hwArpDynOutIfIndex = _HwArpDynOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 17, 1, 14),
    _HwArpDynOutIfIndex_Type()
)
hwArpDynOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwArpDynOutIfIndex.setStatus("current")


class _HwArpDynExpireTime_Type(Integer32):
    """Custom type hwArpDynExpireTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwArpDynExpireTime_Type.__name__ = "Integer32"
_HwArpDynExpireTime_Object = MibTableColumn
hwArpDynExpireTime = _HwArpDynExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 17, 1, 15),
    _HwArpDynExpireTime_Type()
)
hwArpDynExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwArpDynExpireTime.setStatus("current")
_HwArpCfgTable_Object = MibTable
hwArpCfgTable = _HwArpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 18)
)
if mibBuilder.loadTexts:
    hwArpCfgTable.setStatus("current")
_HwArpCfgEntry_Object = MibTableRow
hwArpCfgEntry = _HwArpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 18, 1)
)
hwArpCfgEntry.setIndexNames(
    (0, "HUAWEI-ETHARP-MIB", "hwArpCfgIpAdd"),
    (0, "HUAWEI-ETHARP-MIB", "hwArpCfgVrf"),
)
if mibBuilder.loadTexts:
    hwArpCfgEntry.setStatus("current")
_HwArpCfgIpAdd_Type = InetAddressIPv4
_HwArpCfgIpAdd_Object = MibTableColumn
hwArpCfgIpAdd = _HwArpCfgIpAdd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 18, 1, 1),
    _HwArpCfgIpAdd_Type()
)
hwArpCfgIpAdd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwArpCfgIpAdd.setStatus("current")
_HwArpCfgMacAdd_Type = MacAddress
_HwArpCfgMacAdd_Object = MibTableColumn
hwArpCfgMacAdd = _HwArpCfgMacAdd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 18, 1, 2),
    _HwArpCfgMacAdd_Type()
)
hwArpCfgMacAdd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwArpCfgMacAdd.setStatus("current")


class _HwArpCfgVrf_Type(OctetString):
    """Custom type hwArpCfgVrf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwArpCfgVrf_Type.__name__ = "OctetString"
_HwArpCfgVrf_Object = MibTableColumn
hwArpCfgVrf = _HwArpCfgVrf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 18, 1, 3),
    _HwArpCfgVrf_Type()
)
hwArpCfgVrf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwArpCfgVrf.setStatus("current")


class _HwArpCfgVlanId_Type(Integer32):
    """Custom type hwArpCfgVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_HwArpCfgVlanId_Type.__name__ = "Integer32"
_HwArpCfgVlanId_Object = MibTableColumn
hwArpCfgVlanId = _HwArpCfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 18, 1, 11),
    _HwArpCfgVlanId_Type()
)
hwArpCfgVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwArpCfgVlanId.setStatus("current")


class _HwArpCfgCeVlanId_Type(Integer32):
    """Custom type hwArpCfgCeVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_HwArpCfgCeVlanId_Type.__name__ = "Integer32"
_HwArpCfgCeVlanId_Object = MibTableColumn
hwArpCfgCeVlanId = _HwArpCfgCeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 18, 1, 12),
    _HwArpCfgCeVlanId_Type()
)
hwArpCfgCeVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwArpCfgCeVlanId.setStatus("current")


class _HwArpCfgOutIfIndex_Type(Integer32):
    """Custom type hwArpCfgOutIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwArpCfgOutIfIndex_Type.__name__ = "Integer32"
_HwArpCfgOutIfIndex_Object = MibTableColumn
hwArpCfgOutIfIndex = _HwArpCfgOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 18, 1, 13),
    _HwArpCfgOutIfIndex_Type()
)
hwArpCfgOutIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwArpCfgOutIfIndex.setStatus("current")
_HwArpCfgRowstatus_Type = RowStatus
_HwArpCfgRowstatus_Object = MibTableColumn
hwArpCfgRowstatus = _HwArpCfgRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 18, 1, 51),
    _HwArpCfgRowstatus_Type()
)
hwArpCfgRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwArpCfgRowstatus.setStatus("current")


class _HwEthernetARPAntiAttackStatus_Type(Integer32):
    """Custom type hwEthernetARPAntiAttackStatus based on Integer32"""
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
        *(("disable", 0),
          ("fixAll", 2),
          ("fixMac", 1),
          ("sendAck", 3))
    )


_HwEthernetARPAntiAttackStatus_Type.__name__ = "Integer32"
_HwEthernetARPAntiAttackStatus_Object = MibScalar
hwEthernetARPAntiAttackStatus = _HwEthernetARPAntiAttackStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 19),
    _HwEthernetARPAntiAttackStatus_Type()
)
hwEthernetARPAntiAttackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEthernetARPAntiAttackStatus.setStatus("current")
_HwEthernetARPAntiGateWayConflict_Type = EnabledStatus
_HwEthernetARPAntiGateWayConflict_Object = MibScalar
hwEthernetARPAntiGateWayConflict = _HwEthernetARPAntiGateWayConflict_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 20),
    _HwEthernetARPAntiGateWayConflict_Type()
)
hwEthernetARPAntiGateWayConflict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEthernetARPAntiGateWayConflict.setStatus("current")


class _HwEthernetARPLogAndTrapTimer_Type(Integer32):
    """Custom type hwEthernetARPLogAndTrapTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_HwEthernetARPLogAndTrapTimer_Type.__name__ = "Integer32"
_HwEthernetARPLogAndTrapTimer_Object = MibScalar
hwEthernetARPLogAndTrapTimer = _HwEthernetARPLogAndTrapTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 21),
    _HwEthernetARPLogAndTrapTimer_Type()
)
hwEthernetARPLogAndTrapTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEthernetARPLogAndTrapTimer.setStatus("current")
_HwEthernetARPAntiAttackObjects_ObjectIdentity = ObjectIdentity
hwEthernetARPAntiAttackObjects = _HwEthernetARPAntiAttackObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 22)
)
_HwEthernetARPAntiAttackIpAddress_Type = IpAddress
_HwEthernetARPAntiAttackIpAddress_Object = MibScalar
hwEthernetARPAntiAttackIpAddress = _HwEthernetARPAntiAttackIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 22, 1),
    _HwEthernetARPAntiAttackIpAddress_Type()
)
hwEthernetARPAntiAttackIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPAntiAttackIpAddress.setStatus("current")
_HwEthernetARPAntiAttackMacAddress_Type = OctetString
_HwEthernetARPAntiAttackMacAddress_Object = MibScalar
hwEthernetARPAntiAttackMacAddress = _HwEthernetARPAntiAttackMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 22, 2),
    _HwEthernetARPAntiAttackMacAddress_Type()
)
hwEthernetARPAntiAttackMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPAntiAttackMacAddress.setStatus("current")


class _HwEthernetARPAntiAttackVlanId_Type(Integer32):
    """Custom type hwEthernetARPAntiAttackVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwEthernetARPAntiAttackVlanId_Type.__name__ = "Integer32"
_HwEthernetARPAntiAttackVlanId_Object = MibScalar
hwEthernetARPAntiAttackVlanId = _HwEthernetARPAntiAttackVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 22, 3),
    _HwEthernetARPAntiAttackVlanId_Type()
)
hwEthernetARPAntiAttackVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPAntiAttackVlanId.setStatus("current")
_HwEthernetARPAntiAttackIfName_Type = OctetString
_HwEthernetARPAntiAttackIfName_Object = MibScalar
hwEthernetARPAntiAttackIfName = _HwEthernetARPAntiAttackIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 22, 4),
    _HwEthernetARPAntiAttackIfName_Type()
)
hwEthernetARPAntiAttackIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPAntiAttackIfName.setStatus("current")
_HwArpEntryGatewayConflictTable_Object = MibTable
hwArpEntryGatewayConflictTable = _HwArpEntryGatewayConflictTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 23)
)
if mibBuilder.loadTexts:
    hwArpEntryGatewayConflictTable.setStatus("current")
_HwArpEntryGatewayConflictEntry_Object = MibTableRow
hwArpEntryGatewayConflictEntry = _HwArpEntryGatewayConflictEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 23, 1)
)
hwArpEntryGatewayConflictEntry.setIndexNames(
    (0, "HUAWEI-ETHARP-MIB", "hwEthernetARPAntiGatewayConflictIndex"),
)
if mibBuilder.loadTexts:
    hwArpEntryGatewayConflictEntry.setStatus("current")


class _HwEthernetARPAntiGatewayConflictIndex_Type(Integer32):
    """Custom type hwEthernetARPAntiGatewayConflictIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwEthernetARPAntiGatewayConflictIndex_Type.__name__ = "Integer32"
_HwEthernetARPAntiGatewayConflictIndex_Object = MibTableColumn
hwEthernetARPAntiGatewayConflictIndex = _HwEthernetARPAntiGatewayConflictIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 23, 1, 1),
    _HwEthernetARPAntiGatewayConflictIndex_Type()
)
hwEthernetARPAntiGatewayConflictIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEthernetARPAntiGatewayConflictIndex.setStatus("current")
_HwEthernetARPAntiGatewayConflictIpAddress_Type = IpAddress
_HwEthernetARPAntiGatewayConflictIpAddress_Object = MibTableColumn
hwEthernetARPAntiGatewayConflictIpAddress = _HwEthernetARPAntiGatewayConflictIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 23, 1, 2),
    _HwEthernetARPAntiGatewayConflictIpAddress_Type()
)
hwEthernetARPAntiGatewayConflictIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEthernetARPAntiGatewayConflictIpAddress.setStatus("current")
_HwEthernetARPAntiGatewayConflictMacAddress_Type = OctetString
_HwEthernetARPAntiGatewayConflictMacAddress_Object = MibTableColumn
hwEthernetARPAntiGatewayConflictMacAddress = _HwEthernetARPAntiGatewayConflictMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 23, 1, 3),
    _HwEthernetARPAntiGatewayConflictMacAddress_Type()
)
hwEthernetARPAntiGatewayConflictMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEthernetARPAntiGatewayConflictMacAddress.setStatus("current")


class _HwEthernetARPAntiGatewayConflictVlanId_Type(Integer32):
    """Custom type hwEthernetARPAntiGatewayConflictVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwEthernetARPAntiGatewayConflictVlanId_Type.__name__ = "Integer32"
_HwEthernetARPAntiGatewayConflictVlanId_Object = MibTableColumn
hwEthernetARPAntiGatewayConflictVlanId = _HwEthernetARPAntiGatewayConflictVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 23, 1, 4),
    _HwEthernetARPAntiGatewayConflictVlanId_Type()
)
hwEthernetARPAntiGatewayConflictVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEthernetARPAntiGatewayConflictVlanId.setStatus("current")
_HwEthernetARPAntiGatewayConflictIfName_Type = OctetString
_HwEthernetARPAntiGatewayConflictIfName_Object = MibTableColumn
hwEthernetARPAntiGatewayConflictIfName = _HwEthernetARPAntiGatewayConflictIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 23, 1, 5),
    _HwEthernetARPAntiGatewayConflictIfName_Type()
)
hwEthernetARPAntiGatewayConflictIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEthernetARPAntiGatewayConflictIfName.setStatus("current")
_HwArpSecValidateTable_Object = MibTable
hwArpSecValidateTable = _HwArpSecValidateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 24)
)
if mibBuilder.loadTexts:
    hwArpSecValidateTable.setStatus("current")
_HwArpSecValidateEntry_Object = MibTableRow
hwArpSecValidateEntry = _HwArpSecValidateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 24, 1)
)
hwArpSecValidateEntry.setIndexNames(
    (0, "HUAWEI-ETHARP-MIB", "hwArpSecValidateIfIndex"),
)
if mibBuilder.loadTexts:
    hwArpSecValidateEntry.setStatus("current")
_HwArpSecValidateIfIndex_Type = InterfaceIndex
_HwArpSecValidateIfIndex_Object = MibTableColumn
hwArpSecValidateIfIndex = _HwArpSecValidateIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 24, 1, 1),
    _HwArpSecValidateIfIndex_Type()
)
hwArpSecValidateIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwArpSecValidateIfIndex.setStatus("current")


class _HwArpSecValidateSmac_Type(EnabledStatus):
    """Custom type hwArpSecValidateSmac based on EnabledStatus"""


_HwArpSecValidateSmac_Object = MibTableColumn
hwArpSecValidateSmac = _HwArpSecValidateSmac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 24, 1, 2),
    _HwArpSecValidateSmac_Type()
)
hwArpSecValidateSmac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwArpSecValidateSmac.setStatus("current")


class _HwArpSecValidateDmac_Type(EnabledStatus):
    """Custom type hwArpSecValidateDmac based on EnabledStatus"""


_HwArpSecValidateDmac_Object = MibTableColumn
hwArpSecValidateDmac = _HwArpSecValidateDmac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 24, 1, 3),
    _HwArpSecValidateDmac_Type()
)
hwArpSecValidateDmac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwArpSecValidateDmac.setStatus("current")
_HwArpSecValidateRowStatus_Type = RowStatus
_HwArpSecValidateRowStatus_Object = MibTableColumn
hwArpSecValidateRowStatus = _HwArpSecValidateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 24, 1, 51),
    _HwArpSecValidateRowStatus_Type()
)
hwArpSecValidateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwArpSecValidateRowStatus.setStatus("current")
_HwARPGratuitousSendTable_Object = MibTable
hwARPGratuitousSendTable = _HwARPGratuitousSendTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 25)
)
if mibBuilder.loadTexts:
    hwARPGratuitousSendTable.setStatus("current")
_HwARPGratuitousSendEntry_Object = MibTableRow
hwARPGratuitousSendEntry = _HwARPGratuitousSendEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 25, 1)
)
hwARPGratuitousSendEntry.setIndexNames(
    (0, "HUAWEI-ETHARP-MIB", "hwARPGratuitousSendIfIndex"),
)
if mibBuilder.loadTexts:
    hwARPGratuitousSendEntry.setStatus("current")
_HwARPGratuitousSendIfIndex_Type = InterfaceIndex
_HwARPGratuitousSendIfIndex_Object = MibTableColumn
hwARPGratuitousSendIfIndex = _HwARPGratuitousSendIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 25, 1, 1),
    _HwARPGratuitousSendIfIndex_Type()
)
hwARPGratuitousSendIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwARPGratuitousSendIfIndex.setStatus("current")
_HwARPGratuitousSendEnable_Type = EnabledStatus
_HwARPGratuitousSendEnable_Object = MibTableColumn
hwARPGratuitousSendEnable = _HwARPGratuitousSendEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 25, 1, 2),
    _HwARPGratuitousSendEnable_Type()
)
hwARPGratuitousSendEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwARPGratuitousSendEnable.setStatus("current")


class _HwARPArpGratuitousSendInterval_Type(Integer32):
    """Custom type hwARPArpGratuitousSendInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_HwARPArpGratuitousSendInterval_Type.__name__ = "Integer32"
_HwARPArpGratuitousSendInterval_Object = MibTableColumn
hwARPArpGratuitousSendInterval = _HwARPArpGratuitousSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 25, 1, 3),
    _HwARPArpGratuitousSendInterval_Type()
)
hwARPArpGratuitousSendInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwARPArpGratuitousSendInterval.setStatus("current")
_HwEthernetARPThresholdObjects_ObjectIdentity = ObjectIdentity
hwEthernetARPThresholdObjects = _HwEthernetARPThresholdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 26)
)
_HwEthernetARPThresholdValue_Type = Counter32
_HwEthernetARPThresholdValue_Object = MibScalar
hwEthernetARPThresholdValue = _HwEthernetARPThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 26, 1),
    _HwEthernetARPThresholdValue_Type()
)
hwEthernetARPThresholdValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPThresholdValue.setStatus("current")
_HwEthernetARPThresholdDynamicNumber_Type = Counter32
_HwEthernetARPThresholdDynamicNumber_Object = MibScalar
hwEthernetARPThresholdDynamicNumber = _HwEthernetARPThresholdDynamicNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 26, 2),
    _HwEthernetARPThresholdDynamicNumber_Type()
)
hwEthernetARPThresholdDynamicNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPThresholdDynamicNumber.setStatus("current")
_HwEthernetARPThresholdStaticNumber_Type = Counter32
_HwEthernetARPThresholdStaticNumber_Object = MibScalar
hwEthernetARPThresholdStaticNumber = _HwEthernetARPThresholdStaticNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 26, 3),
    _HwEthernetARPThresholdStaticNumber_Type()
)
hwEthernetARPThresholdStaticNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPThresholdStaticNumber.setStatus("current")


class _HwEthernetARPConflictDetect_Type(Integer32):
    """Custom type hwEthernetARPConflictDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwEthernetARPConflictDetect_Type.__name__ = "Integer32"
_HwEthernetARPConflictDetect_Object = MibScalar
hwEthernetARPConflictDetect = _HwEthernetARPConflictDetect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 27),
    _HwEthernetARPConflictDetect_Type()
)
hwEthernetARPConflictDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEthernetARPConflictDetect.setStatus("current")
_HwETHARPIPConflictObjects_ObjectIdentity = ObjectIdentity
hwETHARPIPConflictObjects = _HwETHARPIPConflictObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 28)
)
_HwEthernetARPIPConflictIPAddress_Type = IpAddress
_HwEthernetARPIPConflictIPAddress_Object = MibScalar
hwEthernetARPIPConflictIPAddress = _HwEthernetARPIPConflictIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 28, 1),
    _HwEthernetARPIPConflictIPAddress_Type()
)
hwEthernetARPIPConflictIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPIPConflictIPAddress.setStatus("current")
_HwEthernetARPIPConflictLocalInterfaceName_Type = OctetString
_HwEthernetARPIPConflictLocalInterfaceName_Object = MibScalar
hwEthernetARPIPConflictLocalInterfaceName = _HwEthernetARPIPConflictLocalInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 28, 2),
    _HwEthernetARPIPConflictLocalInterfaceName_Type()
)
hwEthernetARPIPConflictLocalInterfaceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPIPConflictLocalInterfaceName.setStatus("current")
_HwEthernetARPIPConflictLocalMAC_Type = OctetString
_HwEthernetARPIPConflictLocalMAC_Object = MibScalar
hwEthernetARPIPConflictLocalMAC = _HwEthernetARPIPConflictLocalMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 28, 3),
    _HwEthernetARPIPConflictLocalMAC_Type()
)
hwEthernetARPIPConflictLocalMAC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPIPConflictLocalMAC.setStatus("current")


class _HwEthernetARPIPConflictLocalVLAN_Type(Integer32):
    """Custom type hwEthernetARPIPConflictLocalVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwEthernetARPIPConflictLocalVLAN_Type.__name__ = "Integer32"
_HwEthernetARPIPConflictLocalVLAN_Object = MibScalar
hwEthernetARPIPConflictLocalVLAN = _HwEthernetARPIPConflictLocalVLAN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 28, 4),
    _HwEthernetARPIPConflictLocalVLAN_Type()
)
hwEthernetARPIPConflictLocalVLAN.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPIPConflictLocalVLAN.setStatus("current")


class _HwEthernetARPIPConflictLocalCEVLAN_Type(Integer32):
    """Custom type hwEthernetARPIPConflictLocalCEVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwEthernetARPIPConflictLocalCEVLAN_Type.__name__ = "Integer32"
_HwEthernetARPIPConflictLocalCEVLAN_Object = MibScalar
hwEthernetARPIPConflictLocalCEVLAN = _HwEthernetARPIPConflictLocalCEVLAN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 28, 5),
    _HwEthernetARPIPConflictLocalCEVLAN_Type()
)
hwEthernetARPIPConflictLocalCEVLAN.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPIPConflictLocalCEVLAN.setStatus("current")
_HwEthernetARPIPConflictReceiveInterfaceName_Type = OctetString
_HwEthernetARPIPConflictReceiveInterfaceName_Object = MibScalar
hwEthernetARPIPConflictReceiveInterfaceName = _HwEthernetARPIPConflictReceiveInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 28, 6),
    _HwEthernetARPIPConflictReceiveInterfaceName_Type()
)
hwEthernetARPIPConflictReceiveInterfaceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPIPConflictReceiveInterfaceName.setStatus("current")
_HwEthernetARPIPConflictReceiveMAC_Type = OctetString
_HwEthernetARPIPConflictReceiveMAC_Object = MibScalar
hwEthernetARPIPConflictReceiveMAC = _HwEthernetARPIPConflictReceiveMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 28, 7),
    _HwEthernetARPIPConflictReceiveMAC_Type()
)
hwEthernetARPIPConflictReceiveMAC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPIPConflictReceiveMAC.setStatus("current")


class _HwEthernetARPIPConflictReceiveVLAN_Type(Integer32):
    """Custom type hwEthernetARPIPConflictReceiveVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwEthernetARPIPConflictReceiveVLAN_Type.__name__ = "Integer32"
_HwEthernetARPIPConflictReceiveVLAN_Object = MibScalar
hwEthernetARPIPConflictReceiveVLAN = _HwEthernetARPIPConflictReceiveVLAN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 28, 8),
    _HwEthernetARPIPConflictReceiveVLAN_Type()
)
hwEthernetARPIPConflictReceiveVLAN.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPIPConflictReceiveVLAN.setStatus("current")


class _HwEthernetARPIPConflictReceiveCEVLAN_Type(Integer32):
    """Custom type hwEthernetARPIPConflictReceiveCEVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwEthernetARPIPConflictReceiveCEVLAN_Type.__name__ = "Integer32"
_HwEthernetARPIPConflictReceiveCEVLAN_Object = MibScalar
hwEthernetARPIPConflictReceiveCEVLAN = _HwEthernetARPIPConflictReceiveCEVLAN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 28, 9),
    _HwEthernetARPIPConflictReceiveCEVLAN_Type()
)
hwEthernetARPIPConflictReceiveCEVLAN.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPIPConflictReceiveCEVLAN.setStatus("current")
_HwEthernetARPIPConflictType_Type = OctetString
_HwEthernetARPIPConflictType_Object = MibScalar
hwEthernetARPIPConflictType = _HwEthernetARPIPConflictType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 28, 10),
    _HwEthernetARPIPConflictType_Type()
)
hwEthernetARPIPConflictType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPIPConflictType.setStatus("current")
_HwEthernetARPReceiveDstIPAddr_Type = IpAddress
_HwEthernetARPReceiveDstIPAddr_Object = MibScalar
hwEthernetARPReceiveDstIPAddr = _HwEthernetARPReceiveDstIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 28, 11),
    _HwEthernetARPReceiveDstIPAddr_Type()
)
hwEthernetARPReceiveDstIPAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPReceiveDstIPAddr.setStatus("current")
_HwEthernetARPReceiveDstMAC_Type = OctetString
_HwEthernetARPReceiveDstMAC_Object = MibScalar
hwEthernetARPReceiveDstMAC = _HwEthernetARPReceiveDstMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 28, 12),
    _HwEthernetARPReceiveDstMAC_Type()
)
hwEthernetARPReceiveDstMAC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPReceiveDstMAC.setStatus("current")
_HwEthernetARPLearnStopTable_Object = MibTable
hwEthernetARPLearnStopTable = _HwEthernetARPLearnStopTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 29)
)
if mibBuilder.loadTexts:
    hwEthernetARPLearnStopTable.setStatus("current")
_HwEthernetARPLearnStopEntry_Object = MibTableRow
hwEthernetARPLearnStopEntry = _HwEthernetARPLearnStopEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 29, 1)
)
hwEthernetARPLearnStopEntry.setIndexNames(
    (0, "HUAWEI-ETHARP-MIB", "hwEthernetARPLearnStopSlot"),
)
if mibBuilder.loadTexts:
    hwEthernetARPLearnStopEntry.setStatus("current")


class _HwEthernetARPLearnStopSlot_Type(Integer32):
    """Custom type hwEthernetARPLearnStopSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwEthernetARPLearnStopSlot_Type.__name__ = "Integer32"
_HwEthernetARPLearnStopSlot_Object = MibTableColumn
hwEthernetARPLearnStopSlot = _HwEthernetARPLearnStopSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 29, 1, 1),
    _HwEthernetARPLearnStopSlot_Type()
)
hwEthernetARPLearnStopSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPLearnStopSlot.setStatus("current")
_HwEthernetARPLearnStopThreshold_Type = Counter32
_HwEthernetARPLearnStopThreshold_Object = MibTableColumn
hwEthernetARPLearnStopThreshold = _HwEthernetARPLearnStopThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 29, 1, 2),
    _HwEthernetARPLearnStopThreshold_Type()
)
hwEthernetARPLearnStopThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEthernetARPLearnStopThreshold.setStatus("current")
_HwArpStatisticsTable_Object = MibTable
hwArpStatisticsTable = _HwArpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 30)
)
if mibBuilder.loadTexts:
    hwArpStatisticsTable.setStatus("current")
_HwArpStatisticsEntry_Object = MibTableRow
hwArpStatisticsEntry = _HwArpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 30, 1)
)
hwArpStatisticsEntry.setIndexNames(
    (0, "HUAWEI-ETHARP-MIB", "hwArpStatisticsSlot"),
    (0, "HUAWEI-ETHARP-MIB", "hwArpStatisticsType"),
)
if mibBuilder.loadTexts:
    hwArpStatisticsEntry.setStatus("current")


class _HwArpStatisticsSlot_Type(Integer32):
    """Custom type hwArpStatisticsSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwArpStatisticsSlot_Type.__name__ = "Integer32"
_HwArpStatisticsSlot_Object = MibTableColumn
hwArpStatisticsSlot = _HwArpStatisticsSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 30, 1, 1),
    _HwArpStatisticsSlot_Type()
)
hwArpStatisticsSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwArpStatisticsSlot.setStatus("current")


class _HwArpStatisticsType_Type(Integer32):
    """Custom type hwArpStatisticsType based on Integer32"""
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
        *(("ethTrunk", 3),
          ("ethTrunkQinq", 6),
          ("phy", 1),
          ("phyQinq", 5),
          ("ve", 2),
          ("veQinq", 7),
          ("vlanif", 4))
    )


_HwArpStatisticsType_Type.__name__ = "Integer32"
_HwArpStatisticsType_Object = MibTableColumn
hwArpStatisticsType = _HwArpStatisticsType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 30, 1, 2),
    _HwArpStatisticsType_Type()
)
hwArpStatisticsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwArpStatisticsType.setStatus("current")
_HwArpStatisticsLearnedCount_Type = Counter32
_HwArpStatisticsLearnedCount_Object = MibTableColumn
hwArpStatisticsLearnedCount = _HwArpStatisticsLearnedCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 30, 1, 3),
    _HwArpStatisticsLearnedCount_Type()
)
hwArpStatisticsLearnedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwArpStatisticsLearnedCount.setStatus("current")
_HwArpStatisticsAvailableCount_Type = Counter32
_HwArpStatisticsAvailableCount_Object = MibTableColumn
hwArpStatisticsAvailableCount = _HwArpStatisticsAvailableCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 30, 1, 4),
    _HwArpStatisticsAvailableCount_Type()
)
hwArpStatisticsAvailableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwArpStatisticsAvailableCount.setStatus("current")
_HwEthernetARPRemoteBackupFailObjects_ObjectIdentity = ObjectIdentity
hwEthernetARPRemoteBackupFailObjects = _HwEthernetARPRemoteBackupFailObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 31)
)
_HwEthernetARPRemoteBackupFailMainIfName_Type = OctetString
_HwEthernetARPRemoteBackupFailMainIfName_Object = MibScalar
hwEthernetARPRemoteBackupFailMainIfName = _HwEthernetARPRemoteBackupFailMainIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 1, 31, 1),
    _HwEthernetARPRemoteBackupFailMainIfName_Type()
)
hwEthernetARPRemoteBackupFailMainIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEthernetARPRemoteBackupFailMainIfName.setStatus("current")
_HwEthernetARPNotifications_ObjectIdentity = ObjectIdentity
hwEthernetARPNotifications = _HwEthernetARPNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 2)
)
_HwEthernetARPConformance_ObjectIdentity = ObjectIdentity
hwEthernetARPConformance = _HwEthernetARPConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 3)
)
_HwEthernetARPGroups_ObjectIdentity = ObjectIdentity
hwEthernetARPGroups = _HwEthernetARPGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 3, 1)
)
_HwEthernetARPCompliances_ObjectIdentity = ObjectIdentity
hwEthernetARPCompliances = _HwEthernetARPCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 3, 2)
)

# Managed Objects groups

hwEthernetARPStaticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 3, 1, 1)
)
hwEthernetARPStaticsGroup.setObjects(
      *(("HUAWEI-ETHARP-MIB", "hwEthernetARPStaticsLearnTotal"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPDropForLimit"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPDropForARPSuppress"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPDropForARPMissSuppress"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPDropForOther"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPMissDropForOther"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPRcvNum"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPMissRcvNum"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPStaticsOperation"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPDropForARPProxySuppress"))
)
if mibBuilder.loadTexts:
    hwEthernetARPStaticsGroup.setStatus("current")

hwEthernetARPSpeedLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 3, 1, 2)
)
hwEthernetARPSpeedLimitGroup.setObjects(
    ("HUAWEI-ETHARP-MIB", "hwEthernetARPLimitSpeedValue")
)
if mibBuilder.loadTexts:
    hwEthernetARPSpeedLimitGroup.setStatus("current")

hwEthARPShowWithInterAndVidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 3, 1, 3)
)
hwEthARPShowWithInterAndVidGroup.setObjects(
    ("HUAWEI-ETHARP-MIB", "hwEthARPMacAddr")
)
if mibBuilder.loadTexts:
    hwEthARPShowWithInterAndVidGroup.setStatus("current")

hwEthARPLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 3, 1, 4)
)
hwEthARPLimitGroup.setObjects(
      *(("HUAWEI-ETHARP-MIB", "hwEthARPLimitNum"),
        ("HUAWEI-ETHARP-MIB", "hwEthARPLimitRowStatus"))
)
if mibBuilder.loadTexts:
    hwEthARPLimitGroup.setStatus("current")

hwEthernetARPBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 3, 1, 5)
)
hwEthernetARPBaseGroup.setObjects(
      *(("HUAWEI-ETHARP-MIB", "hwEthernetARPAntiAttackLog"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPLearningStrict"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPSpeedLimitIfIndex"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPSpeedLimitConfigured"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPSpeedLimitCurrent"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPSpeedLimitType"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPSpeedLimitSrcIPAddr"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPSpeedLimitDstIPAddr"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPSpeedLimitVPNinstance"),
        ("HUAWEI-ETHARP-MIB", "hwArpSecValidateSmac"),
        ("HUAWEI-ETHARP-MIB", "hwArpSecValidateDmac"),
        ("HUAWEI-ETHARP-MIB", "hwArpSecValidateRowStatus"))
)
if mibBuilder.loadTexts:
    hwEthernetARPBaseGroup.setStatus("current")

hwEthernetARPLearningStrictInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 3, 1, 7)
)
hwEthernetARPLearningStrictInterfaceGroup.setObjects(
      *(("HUAWEI-ETHARP-MIB", "hwEthernetARPLearningStrictState"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPLearningStrictRowStatus"))
)
if mibBuilder.loadTexts:
    hwEthernetARPLearningStrictInterfaceGroup.setStatus("current")

hwArpLinkInferaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 3, 1, 8)
)
hwArpLinkInferaceGroup.setObjects(
      *(("HUAWEI-ETHARP-MIB", "hwArpLinkPeerIp"),
        ("HUAWEI-ETHARP-MIB", "hwArpLinkDetectTime"),
        ("HUAWEI-ETHARP-MIB", "hwArpLinkDetectTimes"),
        ("HUAWEI-ETHARP-MIB", "hwArpLinkDetectMode"),
        ("HUAWEI-ETHARP-MIB", "hwArpLinkStatus"),
        ("HUAWEI-ETHARP-MIB", "hwArpLinkRowStatus"))
)
if mibBuilder.loadTexts:
    hwArpLinkInferaceGroup.setStatus("current")

hwArpEntryExpireControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 3, 1, 9)
)
hwArpEntryExpireControlGroup.setObjects(
      *(("HUAWEI-ETHARP-MIB", "hwArpEntryExpireDetectMode"),
        ("HUAWEI-ETHARP-MIB", "hwArpEntryExpireFakeTime"))
)
if mibBuilder.loadTexts:
    hwArpEntryExpireControlGroup.setStatus("current")

hwArpAntiAttackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 3, 1, 10)
)
hwArpAntiAttackGroup.setObjects(
      *(("HUAWEI-ETHARP-MIB", "hwEthernetARPAntiAttackStatus"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPAntiGateWayConflict"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPLogAndTrapTimer"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPAntiAttackIpAddress"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPAntiAttackMacAddress"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPAntiAttackVlanId"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPAntiAttackIfName"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPAntiGatewayConflictIpAddress"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPAntiGatewayConflictMacAddress"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPAntiGatewayConflictVlanId"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPAntiGatewayConflictIfName"),
        ("HUAWEI-ETHARP-MIB", "hwArpDynMacAdd"),
        ("HUAWEI-ETHARP-MIB", "hwArpDynVlanId"),
        ("HUAWEI-ETHARP-MIB", "hwArpDynCeVlanId"),
        ("HUAWEI-ETHARP-MIB", "hwArpDynOutIfIndex"),
        ("HUAWEI-ETHARP-MIB", "hwArpDynExpireTime"),
        ("HUAWEI-ETHARP-MIB", "hwArpCfgVlanId"),
        ("HUAWEI-ETHARP-MIB", "hwArpCfgCeVlanId"),
        ("HUAWEI-ETHARP-MIB", "hwArpCfgOutIfIndex"),
        ("HUAWEI-ETHARP-MIB", "hwArpCfgRowstatus"))
)
if mibBuilder.loadTexts:
    hwArpAntiAttackGroup.setStatus("current")

hwEthernetARPThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 3, 1, 11)
)
hwEthernetARPThresholdGroup.setObjects(
      *(("HUAWEI-ETHARP-MIB", "hwEthernetARPThresholdValue"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPThresholdDynamicNumber"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPThresholdStaticNumber"))
)
if mibBuilder.loadTexts:
    hwEthernetARPThresholdGroup.setStatus("current")

hwETHARPIPConflictGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 3, 1, 12)
)
hwETHARPIPConflictGroup.setObjects(
      *(("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictIPAddress"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictLocalInterfaceName"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictLocalMAC"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictLocalVLAN"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictLocalCEVLAN"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictReceiveInterfaceName"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictReceiveMAC"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictReceiveVLAN"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictReceiveCEVLAN"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictType"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPReceiveDstIPAddr"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPReceiveDstMAC"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPConflictDetect"))
)
if mibBuilder.loadTexts:
    hwETHARPIPConflictGroup.setStatus("current")

hwEthernetARPLearnStopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 3, 1, 13)
)
hwEthernetARPLearnStopGroup.setObjects(
      *(("HUAWEI-ETHARP-MIB", "hwEthernetARPLearnStopSlot"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPLearnStopThreshold"))
)
if mibBuilder.loadTexts:
    hwEthernetARPLearnStopGroup.setStatus("current")

hwArpStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 3, 1, 14)
)
hwArpStatisticsGroup.setObjects(
      *(("HUAWEI-ETHARP-MIB", "hwArpStatisticsSlot"),
        ("HUAWEI-ETHARP-MIB", "hwArpStatisticsType"),
        ("HUAWEI-ETHARP-MIB", "hwArpStatisticsLearnedCount"),
        ("HUAWEI-ETHARP-MIB", "hwArpStatisticsAvailableCount"))
)
if mibBuilder.loadTexts:
    hwArpStatisticsGroup.setStatus("current")

hwEthernetARPRemoteBackupFaidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 3, 1, 15)
)
hwEthernetARPRemoteBackupFaidGroup.setObjects(
    ("HUAWEI-ETHARP-MIB", "hwEthernetARPRemoteBackupFailMainIfName")
)
if mibBuilder.loadTexts:
    hwEthernetARPRemoteBackupFaidGroup.setStatus("current")


# Notification objects

hwEthernetARPSpeedLimitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 2, 1)
)
hwEthernetARPSpeedLimitAlarm.setObjects(
      *(("HUAWEI-ETHARP-MIB", "hwEthernetARPSpeedLimitIfIndex"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPSpeedLimitConfigured"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPSpeedLimitCurrent"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPSpeedLimitType"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPSpeedLimitSrcIPAddr"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPSpeedLimitDstIPAddr"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPSpeedLimitVPNinstance"))
)
if mibBuilder.loadTexts:
    hwEthernetARPSpeedLimitAlarm.setStatus(
        "current"
    )

hwEthernetARPAntiAttackAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 2, 2)
)
hwEthernetARPAntiAttackAlarm.setObjects(
      *(("HUAWEI-ETHARP-MIB", "hwEthernetARPAntiAttackIpAddress"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPAntiAttackMacAddress"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPAntiAttackVlanId"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPAntiAttackIfName"))
)
if mibBuilder.loadTexts:
    hwEthernetARPAntiAttackAlarm.setStatus(
        "current"
    )

hwEthernetARPAntiGatewayConflictAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 2, 3)
)
hwEthernetARPAntiGatewayConflictAlarm.setObjects(
      *(("HUAWEI-ETHARP-MIB", "hwEthernetARPAntiGatewayConflictIpAddress"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPAntiGatewayConflictMacAddress"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPAntiGatewayConflictVlanId"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPAntiGatewayConflictIfName"))
)
if mibBuilder.loadTexts:
    hwEthernetARPAntiGatewayConflictAlarm.setStatus(
        "current"
    )

hwEthernetARPThresholdExceedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 2, 4)
)
hwEthernetARPThresholdExceedAlarm.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPThresholdValue"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPThresholdDynamicNumber"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPThresholdStaticNumber"))
)
if mibBuilder.loadTexts:
    hwEthernetARPThresholdExceedAlarm.setStatus(
        "current"
    )

hwEthernetARPThresholdResumeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 2, 5)
)
hwEthernetARPThresholdResumeAlarm.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPThresholdValue"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPThresholdDynamicNumber"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPThresholdStaticNumber"))
)
if mibBuilder.loadTexts:
    hwEthernetARPThresholdResumeAlarm.setStatus(
        "current"
    )

hwEthernetARPIPConflictEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 2, 6)
)
hwEthernetARPIPConflictEvent.setObjects(
      *(("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictIPAddress"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictLocalInterfaceName"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictLocalMAC"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictLocalVLAN"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictLocalCEVLAN"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictReceiveInterfaceName"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictReceiveMAC"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictReceiveVLAN"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictReceiveCEVLAN"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictType"))
)
if mibBuilder.loadTexts:
    hwEthernetARPIPConflictEvent.setStatus(
        "current"
    )

hwEthernetARPMACIPConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 2, 7)
)
hwEthernetARPMACIPConflict.setObjects(
      *(("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictLocalInterfaceName"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictReceiveMAC"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictIPAddress"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPReceiveDstMAC"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPReceiveDstIPAddr"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictReceiveVLAN"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictReceiveCEVLAN"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictReceiveInterfaceName"))
)
if mibBuilder.loadTexts:
    hwEthernetARPMACIPConflict.setStatus(
        "current"
    )

hwEthernetARPMACIPConflictResolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 2, 8)
)
hwEthernetARPMACIPConflictResolved.setObjects(
      *(("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictLocalInterfaceName"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictReceiveMAC"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictIPAddress"))
)
if mibBuilder.loadTexts:
    hwEthernetARPMACIPConflictResolved.setStatus(
        "current"
    )

hwEthernetARPLearnStopAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 2, 9)
)
hwEthernetARPLearnStopAlarm.setObjects(
      *(("HUAWEI-ETHARP-MIB", "hwEthernetARPLearnStopSlot"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPLearnStopThreshold"))
)
if mibBuilder.loadTexts:
    hwEthernetARPLearnStopAlarm.setStatus(
        "current"
    )

hwEthernetARPLearnResumeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 2, 10)
)
hwEthernetARPLearnResumeAlarm.setObjects(
      *(("HUAWEI-ETHARP-MIB", "hwEthernetARPLearnStopSlot"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPLearnStopThreshold"))
)
if mibBuilder.loadTexts:
    hwEthernetARPLearnResumeAlarm.setStatus(
        "current"
    )

hwEthernetARPRemoteBackupFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 2, 11)
)
hwEthernetARPRemoteBackupFailAlarm.setObjects(
    ("HUAWEI-ETHARP-MIB", "hwEthernetARPRemoteBackupFailMainIfName")
)
if mibBuilder.loadTexts:
    hwEthernetARPRemoteBackupFailAlarm.setStatus(
        "current"
    )

hwEthernetARPRemoteBackupFailResumeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 2, 12)
)
hwEthernetARPRemoteBackupFailResumeAlarm.setObjects(
    ("HUAWEI-ETHARP-MIB", "hwEthernetARPRemoteBackupFailMainIfName")
)
if mibBuilder.loadTexts:
    hwEthernetARPRemoteBackupFailResumeAlarm.setStatus(
        "current"
    )


# Notifications groups

hwEthernetARPNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 3, 1, 6)
)
hwEthernetARPNotificationsGroup.setObjects(
      *(("HUAWEI-ETHARP-MIB", "hwEthernetARPSpeedLimitAlarm"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPAntiAttackAlarm"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPAntiGatewayConflictAlarm"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPThresholdExceedAlarm"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPThresholdResumeAlarm"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPIPConflictEvent"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPMACIPConflict"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPMACIPConflictResolved"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPLearnStopAlarm"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPLearnResumeAlarm"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPRemoteBackupFailAlarm"),
        ("HUAWEI-ETHARP-MIB", "hwEthernetARPRemoteBackupFailResumeAlarm"))
)
if mibBuilder.loadTexts:
    hwEthernetARPNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwEthernetARPCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 123, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hwEthernetARPCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-ETHARP-MIB",
    **{"hwEthernetARPMIB": hwEthernetARPMIB,
       "hwEthernetARPObjects": hwEthernetARPObjects,
       "hwEthernetARPAntiAttackLog": hwEthernetARPAntiAttackLog,
       "hwEthernetARPLearningStrict": hwEthernetARPLearningStrict,
       "hwEthernetARPSpeedLimitTable": hwEthernetARPSpeedLimitTable,
       "hwEthernetARPSpeedLimitEntry": hwEthernetARPSpeedLimitEntry,
       "hwEthernetARPLimitSlot": hwEthernetARPLimitSlot,
       "hwEthernetARPLimitType": hwEthernetARPLimitType,
       "hwEthernetARPLimitIPType": hwEthernetARPLimitIPType,
       "hwEthernetARPLimitSpeedValue": hwEthernetARPLimitSpeedValue,
       "hwEthernetARPSpeedLimitIfIndex": hwEthernetARPSpeedLimitIfIndex,
       "hwEthernetARPSpeedLimitConfigured": hwEthernetARPSpeedLimitConfigured,
       "hwEthernetARPSpeedLimitCurrent": hwEthernetARPSpeedLimitCurrent,
       "hwEthernetARPSpeedLimitType": hwEthernetARPSpeedLimitType,
       "hwEthernetARPSpeedLimitSrcIPAddr": hwEthernetARPSpeedLimitSrcIPAddr,
       "hwEthernetARPSpeedLimitDstIPAddr": hwEthernetARPSpeedLimitDstIPAddr,
       "hwEthernetARPSpeedLimitVPNinstance": hwEthernetARPSpeedLimitVPNinstance,
       "hwEthernetARPStaticsTable": hwEthernetARPStaticsTable,
       "hwEthernetARPStaticsEntry": hwEthernetARPStaticsEntry,
       "hwEthernetARPStaticsSlot": hwEthernetARPStaticsSlot,
       "hwEthernetARPStaticsLearnTotal": hwEthernetARPStaticsLearnTotal,
       "hwEthernetARPDropForLimit": hwEthernetARPDropForLimit,
       "hwEthernetARPDropForARPSuppress": hwEthernetARPDropForARPSuppress,
       "hwEthernetARPDropForARPMissSuppress": hwEthernetARPDropForARPMissSuppress,
       "hwEthernetARPDropForOther": hwEthernetARPDropForOther,
       "hwEthernetARPMissDropForOther": hwEthernetARPMissDropForOther,
       "hwEthernetARPRcvNum": hwEthernetARPRcvNum,
       "hwEthernetARPMissRcvNum": hwEthernetARPMissRcvNum,
       "hwEthernetARPStaticsOperation": hwEthernetARPStaticsOperation,
       "hwEthernetARPDropForARPProxySuppress": hwEthernetARPDropForARPProxySuppress,
       "hwEthARPShowWithInterAndVidTable": hwEthARPShowWithInterAndVidTable,
       "hwEthARPShowWithInterAndVidEntry": hwEthARPShowWithInterAndVidEntry,
       "hwEthARPShowIfindex": hwEthARPShowIfindex,
       "hwEthARPShowVid": hwEthARPShowVid,
       "hwEthARPIpAddr": hwEthARPIpAddr,
       "hwEthARPMacAddr": hwEthARPMacAddr,
       "hwEthARPLimitTable": hwEthARPLimitTable,
       "hwEthARPLimitEntry": hwEthARPLimitEntry,
       "hwEthARPLimitCfgIfindex": hwEthARPLimitCfgIfindex,
       "hwEthARPVLANFirst": hwEthARPVLANFirst,
       "hwEthARPVLANLast": hwEthARPVLANLast,
       "hwEthARPLimitNum": hwEthARPLimitNum,
       "hwEthARPLimitRowStatus": hwEthARPLimitRowStatus,
       "hwEthernetARPLearningStrictInterfaceTable": hwEthernetARPLearningStrictInterfaceTable,
       "hwEthernetARPLearningStrictInterfaceEntry": hwEthernetARPLearningStrictInterfaceEntry,
       "hwEthernetARPLearningStrictIfindex": hwEthernetARPLearningStrictIfindex,
       "hwEthernetARPLearningStrictState": hwEthernetARPLearningStrictState,
       "hwEthernetARPLearningStrictRowStatus": hwEthernetARPLearningStrictRowStatus,
       "hwArpLinkInterfaceTable": hwArpLinkInterfaceTable,
       "hwArpLinkInterfaceEntry": hwArpLinkInterfaceEntry,
       "hwArpLinkIfIndex": hwArpLinkIfIndex,
       "hwArpLinkPeerIp": hwArpLinkPeerIp,
       "hwArpLinkDetectTime": hwArpLinkDetectTime,
       "hwArpLinkDetectTimes": hwArpLinkDetectTimes,
       "hwArpLinkDetectMode": hwArpLinkDetectMode,
       "hwArpLinkStatus": hwArpLinkStatus,
       "hwArpLinkRowStatus": hwArpLinkRowStatus,
       "hwArpEntryExpireControlTable": hwArpEntryExpireControlTable,
       "hwArpEntryExpireControlEntry": hwArpEntryExpireControlEntry,
       "hwArpEntryExpireIfIndex": hwArpEntryExpireIfIndex,
       "hwArpEntryExpireDetectMode": hwArpEntryExpireDetectMode,
       "hwArpEntryExpireFakeTime": hwArpEntryExpireFakeTime,
       "hwArpDynTable": hwArpDynTable,
       "hwArpDynEntry": hwArpDynEntry,
       "hwArpDynIfIndex": hwArpDynIfIndex,
       "hwArpDynIpAdd": hwArpDynIpAdd,
       "hwArpDynVrf": hwArpDynVrf,
       "hwArpDynMacAdd": hwArpDynMacAdd,
       "hwArpDynVlanId": hwArpDynVlanId,
       "hwArpDynCeVlanId": hwArpDynCeVlanId,
       "hwArpDynOutIfIndex": hwArpDynOutIfIndex,
       "hwArpDynExpireTime": hwArpDynExpireTime,
       "hwArpCfgTable": hwArpCfgTable,
       "hwArpCfgEntry": hwArpCfgEntry,
       "hwArpCfgIpAdd": hwArpCfgIpAdd,
       "hwArpCfgMacAdd": hwArpCfgMacAdd,
       "hwArpCfgVrf": hwArpCfgVrf,
       "hwArpCfgVlanId": hwArpCfgVlanId,
       "hwArpCfgCeVlanId": hwArpCfgCeVlanId,
       "hwArpCfgOutIfIndex": hwArpCfgOutIfIndex,
       "hwArpCfgRowstatus": hwArpCfgRowstatus,
       "hwEthernetARPAntiAttackStatus": hwEthernetARPAntiAttackStatus,
       "hwEthernetARPAntiGateWayConflict": hwEthernetARPAntiGateWayConflict,
       "hwEthernetARPLogAndTrapTimer": hwEthernetARPLogAndTrapTimer,
       "hwEthernetARPAntiAttackObjects": hwEthernetARPAntiAttackObjects,
       "hwEthernetARPAntiAttackIpAddress": hwEthernetARPAntiAttackIpAddress,
       "hwEthernetARPAntiAttackMacAddress": hwEthernetARPAntiAttackMacAddress,
       "hwEthernetARPAntiAttackVlanId": hwEthernetARPAntiAttackVlanId,
       "hwEthernetARPAntiAttackIfName": hwEthernetARPAntiAttackIfName,
       "hwArpEntryGatewayConflictTable": hwArpEntryGatewayConflictTable,
       "hwArpEntryGatewayConflictEntry": hwArpEntryGatewayConflictEntry,
       "hwEthernetARPAntiGatewayConflictIndex": hwEthernetARPAntiGatewayConflictIndex,
       "hwEthernetARPAntiGatewayConflictIpAddress": hwEthernetARPAntiGatewayConflictIpAddress,
       "hwEthernetARPAntiGatewayConflictMacAddress": hwEthernetARPAntiGatewayConflictMacAddress,
       "hwEthernetARPAntiGatewayConflictVlanId": hwEthernetARPAntiGatewayConflictVlanId,
       "hwEthernetARPAntiGatewayConflictIfName": hwEthernetARPAntiGatewayConflictIfName,
       "hwArpSecValidateTable": hwArpSecValidateTable,
       "hwArpSecValidateEntry": hwArpSecValidateEntry,
       "hwArpSecValidateIfIndex": hwArpSecValidateIfIndex,
       "hwArpSecValidateSmac": hwArpSecValidateSmac,
       "hwArpSecValidateDmac": hwArpSecValidateDmac,
       "hwArpSecValidateRowStatus": hwArpSecValidateRowStatus,
       "hwARPGratuitousSendTable": hwARPGratuitousSendTable,
       "hwARPGratuitousSendEntry": hwARPGratuitousSendEntry,
       "hwARPGratuitousSendIfIndex": hwARPGratuitousSendIfIndex,
       "hwARPGratuitousSendEnable": hwARPGratuitousSendEnable,
       "hwARPArpGratuitousSendInterval": hwARPArpGratuitousSendInterval,
       "hwEthernetARPThresholdObjects": hwEthernetARPThresholdObjects,
       "hwEthernetARPThresholdValue": hwEthernetARPThresholdValue,
       "hwEthernetARPThresholdDynamicNumber": hwEthernetARPThresholdDynamicNumber,
       "hwEthernetARPThresholdStaticNumber": hwEthernetARPThresholdStaticNumber,
       "hwEthernetARPConflictDetect": hwEthernetARPConflictDetect,
       "hwETHARPIPConflictObjects": hwETHARPIPConflictObjects,
       "hwEthernetARPIPConflictIPAddress": hwEthernetARPIPConflictIPAddress,
       "hwEthernetARPIPConflictLocalInterfaceName": hwEthernetARPIPConflictLocalInterfaceName,
       "hwEthernetARPIPConflictLocalMAC": hwEthernetARPIPConflictLocalMAC,
       "hwEthernetARPIPConflictLocalVLAN": hwEthernetARPIPConflictLocalVLAN,
       "hwEthernetARPIPConflictLocalCEVLAN": hwEthernetARPIPConflictLocalCEVLAN,
       "hwEthernetARPIPConflictReceiveInterfaceName": hwEthernetARPIPConflictReceiveInterfaceName,
       "hwEthernetARPIPConflictReceiveMAC": hwEthernetARPIPConflictReceiveMAC,
       "hwEthernetARPIPConflictReceiveVLAN": hwEthernetARPIPConflictReceiveVLAN,
       "hwEthernetARPIPConflictReceiveCEVLAN": hwEthernetARPIPConflictReceiveCEVLAN,
       "hwEthernetARPIPConflictType": hwEthernetARPIPConflictType,
       "hwEthernetARPReceiveDstIPAddr": hwEthernetARPReceiveDstIPAddr,
       "hwEthernetARPReceiveDstMAC": hwEthernetARPReceiveDstMAC,
       "hwEthernetARPLearnStopTable": hwEthernetARPLearnStopTable,
       "hwEthernetARPLearnStopEntry": hwEthernetARPLearnStopEntry,
       "hwEthernetARPLearnStopSlot": hwEthernetARPLearnStopSlot,
       "hwEthernetARPLearnStopThreshold": hwEthernetARPLearnStopThreshold,
       "hwArpStatisticsTable": hwArpStatisticsTable,
       "hwArpStatisticsEntry": hwArpStatisticsEntry,
       "hwArpStatisticsSlot": hwArpStatisticsSlot,
       "hwArpStatisticsType": hwArpStatisticsType,
       "hwArpStatisticsLearnedCount": hwArpStatisticsLearnedCount,
       "hwArpStatisticsAvailableCount": hwArpStatisticsAvailableCount,
       "hwEthernetARPRemoteBackupFailObjects": hwEthernetARPRemoteBackupFailObjects,
       "hwEthernetARPRemoteBackupFailMainIfName": hwEthernetARPRemoteBackupFailMainIfName,
       "hwEthernetARPNotifications": hwEthernetARPNotifications,
       "hwEthernetARPSpeedLimitAlarm": hwEthernetARPSpeedLimitAlarm,
       "hwEthernetARPAntiAttackAlarm": hwEthernetARPAntiAttackAlarm,
       "hwEthernetARPAntiGatewayConflictAlarm": hwEthernetARPAntiGatewayConflictAlarm,
       "hwEthernetARPThresholdExceedAlarm": hwEthernetARPThresholdExceedAlarm,
       "hwEthernetARPThresholdResumeAlarm": hwEthernetARPThresholdResumeAlarm,
       "hwEthernetARPIPConflictEvent": hwEthernetARPIPConflictEvent,
       "hwEthernetARPMACIPConflict": hwEthernetARPMACIPConflict,
       "hwEthernetARPMACIPConflictResolved": hwEthernetARPMACIPConflictResolved,
       "hwEthernetARPLearnStopAlarm": hwEthernetARPLearnStopAlarm,
       "hwEthernetARPLearnResumeAlarm": hwEthernetARPLearnResumeAlarm,
       "hwEthernetARPRemoteBackupFailAlarm": hwEthernetARPRemoteBackupFailAlarm,
       "hwEthernetARPRemoteBackupFailResumeAlarm": hwEthernetARPRemoteBackupFailResumeAlarm,
       "hwEthernetARPConformance": hwEthernetARPConformance,
       "hwEthernetARPGroups": hwEthernetARPGroups,
       "hwEthernetARPStaticsGroup": hwEthernetARPStaticsGroup,
       "hwEthernetARPSpeedLimitGroup": hwEthernetARPSpeedLimitGroup,
       "hwEthARPShowWithInterAndVidGroup": hwEthARPShowWithInterAndVidGroup,
       "hwEthARPLimitGroup": hwEthARPLimitGroup,
       "hwEthernetARPBaseGroup": hwEthernetARPBaseGroup,
       "hwEthernetARPNotificationsGroup": hwEthernetARPNotificationsGroup,
       "hwEthernetARPLearningStrictInterfaceGroup": hwEthernetARPLearningStrictInterfaceGroup,
       "hwArpLinkInferaceGroup": hwArpLinkInferaceGroup,
       "hwArpEntryExpireControlGroup": hwArpEntryExpireControlGroup,
       "hwArpAntiAttackGroup": hwArpAntiAttackGroup,
       "hwEthernetARPThresholdGroup": hwEthernetARPThresholdGroup,
       "hwETHARPIPConflictGroup": hwETHARPIPConflictGroup,
       "hwEthernetARPLearnStopGroup": hwEthernetARPLearnStopGroup,
       "hwArpStatisticsGroup": hwArpStatisticsGroup,
       "hwEthernetARPRemoteBackupFaidGroup": hwEthernetARPRemoteBackupFaidGroup,
       "hwEthernetARPCompliances": hwEthernetARPCompliances,
       "hwEthernetARPCompliance": hwEthernetARPCompliance}
)
