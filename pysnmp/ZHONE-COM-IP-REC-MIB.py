# SNMP MIB module (ZHONE-COM-IP-REC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-COM-IP-REC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:09 2024
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

(AtmVcIdentifier,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVcIdentifier",
    "AtmVpIdentifier")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(ZhoneRDIndex,) = mibBuilder.importSymbols(
    "ZHONE-COM-IP-RD-MIB",
    "ZhoneRDIndex")

(zhoneIp,
 zhoneModules) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneIp",
    "zhoneModules")

(ZhoneAdminString,
 ZhoneRowStatus) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAdminString",
    "ZhoneRowStatus")


# MODULE-IDENTITY

ipRecord = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 59)
)
ipRecord.setRevisions(
        ("2010-09-01 09:17",
         "2010-05-04 02:24",
         "2008-06-27 08:14",
         "2006-02-17 17:37",
         "2006-01-23 09:26",
         "2005-07-20 17:22",
         "2004-07-21 08:46",
         "2004-05-27 09:56",
         "2004-04-28 14:02",
         "2003-04-18 10:03",
         "2002-04-17 16:48",
         "2002-02-11 16:57",
         "2001-10-30 10:44",
         "2001-06-06 16:00",
         "2001-03-15 10:28",
         "2001-02-26 13:58",
         "2001-02-13 11:13",
         "2001-01-19 18:16",
         "2001-01-17 16:18",
         "2000-11-20 10:18",
         "2000-10-05 15:12",
         "2000-09-15 14:30",
         "2000-09-12 10:06")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpRecordObjects_ObjectIdentity = ObjectIdentity
ipRecordObjects = _IpRecordObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9)
)
if mibBuilder.loadTexts:
    ipRecordObjects.setStatus("current")
_IpInterfaceTable_Object = MibTable
ipInterfaceTable = _IpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2)
)
if mibBuilder.loadTexts:
    ipInterfaceTable.setStatus("current")
_IpInterfaceEntry_Object = MibTableRow
ipInterfaceEntry = _IpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1)
)
ipInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ipInterfaceEntry.setStatus("current")


class _IpIfLgId_Type(Integer32):
    """Custom type ipIfLgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpIfLgId_Type.__name__ = "Integer32"
_IpIfLgId_Object = MibTableColumn
ipIfLgId = _IpIfLgId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 1),
    _IpIfLgId_Type()
)
ipIfLgId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfLgId.setStatus("obsolete")


class _IpIfVpi_Type(AtmVpIdentifier):
    """Custom type ipIfVpi based on AtmVpIdentifier"""
    defaultValue = 0


_IpIfVpi_Object = MibTableColumn
ipIfVpi = _IpIfVpi_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 2),
    _IpIfVpi_Type()
)
ipIfVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfVpi.setStatus("current")


class _IpIfVci_Type(AtmVcIdentifier):
    """Custom type ipIfVci based on AtmVcIdentifier"""
    defaultValue = 0


_IpIfVci_Object = MibTableColumn
ipIfVci = _IpIfVci_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 3),
    _IpIfVci_Type()
)
ipIfVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfVci.setStatus("current")


class _IpIfRDIndex_Type(ZhoneRDIndex):
    """Custom type ipIfRDIndex based on ZhoneRDIndex"""
    defaultValue = 0


_IpIfRDIndex_Object = MibTableColumn
ipIfRDIndex = _IpIfRDIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 4),
    _IpIfRDIndex_Type()
)
ipIfRDIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfRDIndex.setStatus("current")


class _IpIfDhcp_Type(Integer32):
    """Custom type ipIfDhcp based on Integer32"""
    defaultValue = 1

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
        *(("dhcpBoth", 4),
          ("dhcpClient", 2),
          ("dhcpServer", 3),
          ("noDhcp", 1))
    )


_IpIfDhcp_Type.__name__ = "Integer32"
_IpIfDhcp_Object = MibTableColumn
ipIfDhcp = _IpIfDhcp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 5),
    _IpIfDhcp_Type()
)
ipIfDhcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfDhcp.setStatus("deprecated")


class _IpIfAddr_Type(IpAddress):
    """Custom type ipIfAddr based on IpAddress"""
    defaultHexValue = "00000000"


_IpIfAddr_Object = MibTableColumn
ipIfAddr = _IpIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 6),
    _IpIfAddr_Type()
)
ipIfAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfAddr.setStatus("current")


class _IpIfNetMask_Type(IpAddress):
    """Custom type ipIfNetMask based on IpAddress"""
    defaultHexValue = "00000000"


_IpIfNetMask_Object = MibTableColumn
ipIfNetMask = _IpIfNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 7),
    _IpIfNetMask_Type()
)
ipIfNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfNetMask.setStatus("current")


class _IpIfBcastAddr_Type(IpAddress):
    """Custom type ipIfBcastAddr based on IpAddress"""
    defaultHexValue = "00000000"


_IpIfBcastAddr_Object = MibTableColumn
ipIfBcastAddr = _IpIfBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 8),
    _IpIfBcastAddr_Type()
)
ipIfBcastAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfBcastAddr.setStatus("current")


class _IpIfDestAddr_Type(IpAddress):
    """Custom type ipIfDestAddr based on IpAddress"""
    defaultHexValue = "00000000"


_IpIfDestAddr_Object = MibTableColumn
ipIfDestAddr = _IpIfDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 9),
    _IpIfDestAddr_Type()
)
ipIfDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfDestAddr.setStatus("current")


class _IpIfFarEndAddr_Type(IpAddress):
    """Custom type ipIfFarEndAddr based on IpAddress"""
    defaultHexValue = "00000000"


_IpIfFarEndAddr_Object = MibTableColumn
ipIfFarEndAddr = _IpIfFarEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 10),
    _IpIfFarEndAddr_Type()
)
ipIfFarEndAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfFarEndAddr.setStatus("current")


class _IpIfMru_Type(Unsigned32):
    """Custom type ipIfMru based on Unsigned32"""
    defaultValue = 1500


_IpIfMru_Object = MibTableColumn
ipIfMru = _IpIfMru_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 11),
    _IpIfMru_Type()
)
ipIfMru.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfMru.setStatus("current")


class _IpIfReasmMaxSize_Type(Integer32):
    """Custom type ipIfReasmMaxSize based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpIfReasmMaxSize_Type.__name__ = "Integer32"
_IpIfReasmMaxSize_Object = MibTableColumn
ipIfReasmMaxSize = _IpIfReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 12),
    _IpIfReasmMaxSize_Type()
)
ipIfReasmMaxSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfReasmMaxSize.setStatus("current")
_IpIfIngressFilterName_Type = ZhoneAdminString
_IpIfIngressFilterName_Object = MibTableColumn
ipIfIngressFilterName = _IpIfIngressFilterName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 13),
    _IpIfIngressFilterName_Type()
)
ipIfIngressFilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfIngressFilterName.setStatus("deprecated")
_IpIfEgressFilterName_Type = ZhoneAdminString
_IpIfEgressFilterName_Object = MibTableColumn
ipIfEgressFilterName = _IpIfEgressFilterName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 14),
    _IpIfEgressFilterName_Type()
)
ipIfEgressFilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfEgressFilterName.setStatus("deprecated")


class _IpIfPointToPoint_Type(TruthValue):
    """Custom type ipIfPointToPoint based on TruthValue"""


_IpIfPointToPoint_Object = MibTableColumn
ipIfPointToPoint = _IpIfPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 15),
    _IpIfPointToPoint_Type()
)
ipIfPointToPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfPointToPoint.setStatus("current")


class _IpIfMcastEnabled_Type(TruthValue):
    """Custom type ipIfMcastEnabled based on TruthValue"""


_IpIfMcastEnabled_Object = MibTableColumn
ipIfMcastEnabled = _IpIfMcastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 16),
    _IpIfMcastEnabled_Type()
)
ipIfMcastEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfMcastEnabled.setStatus("current")


class _IpIfIpFwdEnabled_Type(TruthValue):
    """Custom type ipIfIpFwdEnabled based on TruthValue"""


_IpIfIpFwdEnabled_Object = MibTableColumn
ipIfIpFwdEnabled = _IpIfIpFwdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 17),
    _IpIfIpFwdEnabled_Type()
)
ipIfIpFwdEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfIpFwdEnabled.setStatus("current")


class _IpIfMcastFwdEnabled_Type(TruthValue):
    """Custom type ipIfMcastFwdEnabled based on TruthValue"""


_IpIfMcastFwdEnabled_Object = MibTableColumn
ipIfMcastFwdEnabled = _IpIfMcastFwdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 18),
    _IpIfMcastFwdEnabled_Type()
)
ipIfMcastFwdEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfMcastFwdEnabled.setStatus("current")


class _IpIfNATEnabled_Type(TruthValue):
    """Custom type ipIfNATEnabled based on TruthValue"""


_IpIfNATEnabled_Object = MibTableColumn
ipIfNATEnabled = _IpIfNATEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 19),
    _IpIfNATEnabled_Type()
)
ipIfNATEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfNATEnabled.setStatus("current")


class _IpIfBcastEnabled_Type(TruthValue):
    """Custom type ipIfBcastEnabled based on TruthValue"""


_IpIfBcastEnabled_Object = MibTableColumn
ipIfBcastEnabled = _IpIfBcastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 20),
    _IpIfBcastEnabled_Type()
)
ipIfBcastEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfBcastEnabled.setStatus("current")
_IpIfRowStatus_Type = ZhoneRowStatus
_IpIfRowStatus_Object = MibTableColumn
ipIfRowStatus = _IpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 21),
    _IpIfRowStatus_Type()
)
ipIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfRowStatus.setStatus("current")


class _IpIfAdminStatus_Type(Integer32):
    """Custom type ipIfAdminStatus based on Integer32"""
    defaultValue = 1

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


_IpIfAdminStatus_Type.__name__ = "Integer32"
_IpIfAdminStatus_Object = MibTableColumn
ipIfAdminStatus = _IpIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 22),
    _IpIfAdminStatus_Type()
)
ipIfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfAdminStatus.setStatus("current")


class _IpIfIngressPacketRuleGroupIndex_Type(Integer32):
    """Custom type ipIfIngressPacketRuleGroupIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpIfIngressPacketRuleGroupIndex_Type.__name__ = "Integer32"
_IpIfIngressPacketRuleGroupIndex_Object = MibTableColumn
ipIfIngressPacketRuleGroupIndex = _IpIfIngressPacketRuleGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 23),
    _IpIfIngressPacketRuleGroupIndex_Type()
)
ipIfIngressPacketRuleGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfIngressPacketRuleGroupIndex.setStatus("current")


class _IpIfEgressPacketRuleGroupIndex_Type(Integer32):
    """Custom type ipIfEgressPacketRuleGroupIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpIfEgressPacketRuleGroupIndex_Type.__name__ = "Integer32"
_IpIfEgressPacketRuleGroupIndex_Object = MibTableColumn
ipIfEgressPacketRuleGroupIndex = _IpIfEgressPacketRuleGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 24),
    _IpIfEgressPacketRuleGroupIndex_Type()
)
ipIfEgressPacketRuleGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfEgressPacketRuleGroupIndex.setStatus("current")
_IpIfLowerIfIndex_Type = InterfaceIndexOrZero
_IpIfLowerIfIndex_Object = MibTableColumn
ipIfLowerIfIndex = _IpIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 25),
    _IpIfLowerIfIndex_Type()
)
ipIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfLowerIfIndex.setStatus("current")


class _IpIfPppEnabled_Type(TruthValue):
    """Custom type ipIfPppEnabled based on TruthValue"""


_IpIfPppEnabled_Object = MibTableColumn
ipIfPppEnabled = _IpIfPppEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 26),
    _IpIfPppEnabled_Type()
)
ipIfPppEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfPppEnabled.setStatus("current")


class _IpAddrDynamic_Type(Integer32):
    """Custom type ipAddrDynamic based on Integer32"""
    defaultValue = 1

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
        *(("cpemgr", 5),
          ("dhcpclient", 3),
          ("ppp", 2),
          ("static", 1),
          ("unnumbered", 4))
    )


_IpAddrDynamic_Type.__name__ = "Integer32"
_IpAddrDynamic_Object = MibTableColumn
ipAddrDynamic = _IpAddrDynamic_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 27),
    _IpAddrDynamic_Type()
)
ipAddrDynamic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipAddrDynamic.setStatus("current")


class _DhcpServerEnable_Type(TruthValue):
    """Custom type dhcpServerEnable based on TruthValue"""


_DhcpServerEnable_Object = MibTableColumn
dhcpServerEnable = _DhcpServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 28),
    _DhcpServerEnable_Type()
)
dhcpServerEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpServerEnable.setStatus("current")


class _DhcpSubnetGroup_Type(Integer32):
    """Custom type dhcpSubnetGroup based on Integer32"""
    defaultBinValue = 0


_DhcpSubnetGroup_Object = MibTableColumn
dhcpSubnetGroup = _DhcpSubnetGroup_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 29),
    _DhcpSubnetGroup_Type()
)
dhcpSubnetGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSubnetGroup.setStatus("current")


class _UnnumberedIndex_Type(Integer32):
    """Custom type unnumberedIndex based on Integer32"""
    defaultBinValue = 0


_UnnumberedIndex_Object = MibTableColumn
unnumberedIndex = _UnnumberedIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 30),
    _UnnumberedIndex_Type()
)
unnumberedIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unnumberedIndex.setStatus("current")
_McastControlList_Type = SnmpAdminString
_McastControlList_Object = MibTableColumn
mcastControlList = _McastControlList_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 31),
    _McastControlList_Type()
)
mcastControlList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mcastControlList.setStatus("current")


class _Vlanid_Type(Integer32):
    """Custom type vlanid based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Vlanid_Type.__name__ = "Integer32"
_Vlanid_Object = MibTableColumn
vlanid = _Vlanid_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 32),
    _Vlanid_Type()
)
vlanid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanid.setStatus("current")


class _MaxVideoStreams_Type(Unsigned32):
    """Custom type maxVideoStreams based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_MaxVideoStreams_Type.__name__ = "Unsigned32"
_MaxVideoStreams_Object = MibTableColumn
maxVideoStreams = _MaxVideoStreams_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 33),
    _MaxVideoStreams_Type()
)
maxVideoStreams.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    maxVideoStreams.setStatus("current")


class _TosOption_Type(Integer32):
    """Custom type tosOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tosOptionAll", 3),
          ("tosOptionDisable", 1),
          ("tosOptionOriginate", 2))
    )


_TosOption_Type.__name__ = "Integer32"
_TosOption_Object = MibTableColumn
tosOption = _TosOption_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 34),
    _TosOption_Type()
)
tosOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tosOption.setStatus("current")


class _TosCOS_Type(Integer32):
    """Custom type tosCOS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TosCOS_Type.__name__ = "Integer32"
_TosCOS_Object = MibTableColumn
tosCOS = _TosCOS_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 35),
    _TosCOS_Type()
)
tosCOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tosCOS.setStatus("current")


class _VlanCOS_Type(Integer32):
    """Custom type vlanCOS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VlanCOS_Type.__name__ = "Integer32"
_VlanCOS_Object = MibTableColumn
vlanCOS = _VlanCOS_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 36),
    _VlanCOS_Type()
)
vlanCOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanCOS.setStatus("current")


class _IpStagTPID_Type(Integer32):
    """Custom type ipStagTPID based on Integer32"""
    defaultHexValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(33024, 33024),
        ValueRangeConstraint(34984, 34984),
        ValueRangeConstraint(37120, 37120),
        ValueRangeConstraint(37376, 37376),
    )


_IpStagTPID_Type.__name__ = "Integer32"
_IpStagTPID_Object = MibTableColumn
ipStagTPID = _IpStagTPID_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 37),
    _IpStagTPID_Type()
)
ipStagTPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipStagTPID.setStatus("current")


class _IpStagId_Type(Integer32):
    """Custom type ipStagId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_IpStagId_Type.__name__ = "Integer32"
_IpStagId_Object = MibTableColumn
ipStagId = _IpStagId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 38),
    _IpStagId_Type()
)
ipStagId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipStagId.setStatus("current")


class _IpStagIdCOS_Type(Integer32):
    """Custom type ipStagIdCOS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_IpStagIdCOS_Type.__name__ = "Integer32"
_IpStagIdCOS_Object = MibTableColumn
ipStagIdCOS = _IpStagIdCOS_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 39),
    _IpStagIdCOS_Type()
)
ipStagIdCOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipStagIdCOS.setStatus("current")


class _IpOnDemandStatsEnabled_Type(TruthValue):
    """Custom type ipOnDemandStatsEnabled based on TruthValue"""


_IpOnDemandStatsEnabled_Object = MibTableColumn
ipOnDemandStatsEnabled = _IpOnDemandStatsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 2, 1, 40),
    _IpOnDemandStatsEnabled_Type()
)
ipOnDemandStatsEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipOnDemandStatsEnabled.setStatus("current")
_IpIfAliasTable_Object = MibTable
ipIfAliasTable = _IpIfAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 5)
)
if mibBuilder.loadTexts:
    ipIfAliasTable.setStatus("current")
_IpIfAliasEntry_Object = MibTableRow
ipIfAliasEntry = _IpIfAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 5, 1)
)
ipIfAliasEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZHONE-COM-IP-REC-MIB", "ipIfAliasAddr"),
)
if mibBuilder.loadTexts:
    ipIfAliasEntry.setStatus("current")
_IpIfAliasAddr_Type = IpAddress
_IpIfAliasAddr_Object = MibTableColumn
ipIfAliasAddr = _IpIfAliasAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 5, 1, 1),
    _IpIfAliasAddr_Type()
)
ipIfAliasAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipIfAliasAddr.setStatus("current")
_IpIfAliasRowStatus_Type = ZhoneRowStatus
_IpIfAliasRowStatus_Object = MibTableColumn
ipIfAliasRowStatus = _IpIfAliasRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 5, 1, 2),
    _IpIfAliasRowStatus_Type()
)
ipIfAliasRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfAliasRowStatus.setStatus("current")


class _IpIfAliasNetMask_Type(IpAddress):
    """Custom type ipIfAliasNetMask based on IpAddress"""
    defaultHexValue = "00000000"


_IpIfAliasNetMask_Object = MibTableColumn
ipIfAliasNetMask = _IpIfAliasNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 5, 1, 3),
    _IpIfAliasNetMask_Type()
)
ipIfAliasNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfAliasNetMask.setStatus("current")


class _IpIfAliasBcastAddr_Type(IpAddress):
    """Custom type ipIfAliasBcastAddr based on IpAddress"""
    defaultHexValue = "00000000"


_IpIfAliasBcastAddr_Object = MibTableColumn
ipIfAliasBcastAddr = _IpIfAliasBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 9, 5, 1, 4),
    _IpIfAliasBcastAddr_Type()
)
ipIfAliasBcastAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipIfAliasBcastAddr.setStatus("current")
_IpUnnumbered_ObjectIdentity = ObjectIdentity
ipUnnumbered = _IpUnnumbered_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 10)
)
if mibBuilder.loadTexts:
    ipUnnumbered.setStatus("deprecated")


class _IpUnnumberedEnabled_Type(TruthValue):
    """Custom type ipUnnumberedEnabled based on TruthValue"""


_IpUnnumberedEnabled_Object = MibScalar
ipUnnumberedEnabled = _IpUnnumberedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 10, 1),
    _IpUnnumberedEnabled_Type()
)
ipUnnumberedEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipUnnumberedEnabled.setStatus("deprecated")


class _IpUnnumberedInterfaceIndex_Type(InterfaceIndexOrZero):
    """Custom type ipUnnumberedInterfaceIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_IpUnnumberedInterfaceIndex_Object = MibScalar
ipUnnumberedInterfaceIndex = _IpUnnumberedInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 10, 2),
    _IpUnnumberedInterfaceIndex_Type()
)
ipUnnumberedInterfaceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipUnnumberedInterfaceIndex.setStatus("deprecated")
_IpUnnumberedObjects_ObjectIdentity = ObjectIdentity
ipUnnumberedObjects = _IpUnnumberedObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 14)
)
_IpUnnumberedObjectNext_Type = Integer32
_IpUnnumberedObjectNext_Object = MibScalar
ipUnnumberedObjectNext = _IpUnnumberedObjectNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 14, 1),
    _IpUnnumberedObjectNext_Type()
)
ipUnnumberedObjectNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipUnnumberedObjectNext.setStatus("current")
_IpUnnumberedTable_Object = MibTable
ipUnnumberedTable = _IpUnnumberedTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 14, 2)
)
if mibBuilder.loadTexts:
    ipUnnumberedTable.setStatus("current")
_IpUnnumberedEntry_Object = MibTableRow
ipUnnumberedEntry = _IpUnnumberedEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 14, 2, 1)
)
ipUnnumberedEntry.setIndexNames(
    (0, "ZHONE-COM-IP-REC-MIB", "ipUnnumberedIndex"),
)
if mibBuilder.loadTexts:
    ipUnnumberedEntry.setStatus("current")


class _IpUnnumberedIndex_Type(Integer32):
    """Custom type ipUnnumberedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IpUnnumberedIndex_Type.__name__ = "Integer32"
_IpUnnumberedIndex_Object = MibTableColumn
ipUnnumberedIndex = _IpUnnumberedIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 14, 2, 1, 1),
    _IpUnnumberedIndex_Type()
)
ipUnnumberedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipUnnumberedIndex.setStatus("current")
_IpUnnumberedRowStatus_Type = ZhoneRowStatus
_IpUnnumberedRowStatus_Object = MibTableColumn
ipUnnumberedRowStatus = _IpUnnumberedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 14, 2, 1, 2),
    _IpUnnumberedRowStatus_Type()
)
ipUnnumberedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipUnnumberedRowStatus.setStatus("current")


class _IpUnnumberedIfIName_Type(InterfaceIndex):
    """Custom type ipUnnumberedIfIName based on InterfaceIndex"""
    defaultBinValue = 1


_IpUnnumberedIfIName_Object = MibTableColumn
ipUnnumberedIfIName = _IpUnnumberedIfIName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 14, 2, 1, 3),
    _IpUnnumberedIfIName_Type()
)
ipUnnumberedIfIName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipUnnumberedIfIName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-COM-IP-REC-MIB",
    **{"ipRecordObjects": ipRecordObjects,
       "ipInterfaceTable": ipInterfaceTable,
       "ipInterfaceEntry": ipInterfaceEntry,
       "ipIfLgId": ipIfLgId,
       "ipIfVpi": ipIfVpi,
       "ipIfVci": ipIfVci,
       "ipIfRDIndex": ipIfRDIndex,
       "ipIfDhcp": ipIfDhcp,
       "ipIfAddr": ipIfAddr,
       "ipIfNetMask": ipIfNetMask,
       "ipIfBcastAddr": ipIfBcastAddr,
       "ipIfDestAddr": ipIfDestAddr,
       "ipIfFarEndAddr": ipIfFarEndAddr,
       "ipIfMru": ipIfMru,
       "ipIfReasmMaxSize": ipIfReasmMaxSize,
       "ipIfIngressFilterName": ipIfIngressFilterName,
       "ipIfEgressFilterName": ipIfEgressFilterName,
       "ipIfPointToPoint": ipIfPointToPoint,
       "ipIfMcastEnabled": ipIfMcastEnabled,
       "ipIfIpFwdEnabled": ipIfIpFwdEnabled,
       "ipIfMcastFwdEnabled": ipIfMcastFwdEnabled,
       "ipIfNATEnabled": ipIfNATEnabled,
       "ipIfBcastEnabled": ipIfBcastEnabled,
       "ipIfRowStatus": ipIfRowStatus,
       "ipIfAdminStatus": ipIfAdminStatus,
       "ipIfIngressPacketRuleGroupIndex": ipIfIngressPacketRuleGroupIndex,
       "ipIfEgressPacketRuleGroupIndex": ipIfEgressPacketRuleGroupIndex,
       "ipIfLowerIfIndex": ipIfLowerIfIndex,
       "ipIfPppEnabled": ipIfPppEnabled,
       "ipAddrDynamic": ipAddrDynamic,
       "dhcpServerEnable": dhcpServerEnable,
       "dhcpSubnetGroup": dhcpSubnetGroup,
       "unnumberedIndex": unnumberedIndex,
       "mcastControlList": mcastControlList,
       "vlanid": vlanid,
       "maxVideoStreams": maxVideoStreams,
       "tosOption": tosOption,
       "tosCOS": tosCOS,
       "vlanCOS": vlanCOS,
       "ipStagTPID": ipStagTPID,
       "ipStagId": ipStagId,
       "ipStagIdCOS": ipStagIdCOS,
       "ipOnDemandStatsEnabled": ipOnDemandStatsEnabled,
       "ipIfAliasTable": ipIfAliasTable,
       "ipIfAliasEntry": ipIfAliasEntry,
       "ipIfAliasAddr": ipIfAliasAddr,
       "ipIfAliasRowStatus": ipIfAliasRowStatus,
       "ipIfAliasNetMask": ipIfAliasNetMask,
       "ipIfAliasBcastAddr": ipIfAliasBcastAddr,
       "ipUnnumbered": ipUnnumbered,
       "ipUnnumberedEnabled": ipUnnumberedEnabled,
       "ipUnnumberedInterfaceIndex": ipUnnumberedInterfaceIndex,
       "ipUnnumberedObjects": ipUnnumberedObjects,
       "ipUnnumberedObjectNext": ipUnnumberedObjectNext,
       "ipUnnumberedTable": ipUnnumberedTable,
       "ipUnnumberedEntry": ipUnnumberedEntry,
       "ipUnnumberedIndex": ipUnnumberedIndex,
       "ipUnnumberedRowStatus": ipUnnumberedRowStatus,
       "ipUnnumberedIfIName": ipUnnumberedIfIName,
       "ipRecord": ipRecord}
)
